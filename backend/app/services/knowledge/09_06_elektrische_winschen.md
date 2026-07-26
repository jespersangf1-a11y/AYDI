---
title: "Elektrische Winschen und Nachrüstung"
kategorie: "09 Winschen"
unterkategorie: "09.06 Elektrische Winschen"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, ABYC E-11, Zertifizierungen"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Retrofit-Dokumentationen"
  - estimated: "Erfahrungswerte, Regatta-Praxis, Werft-Konsens, Eigner-Berichte"
---

# 09.06 — Elektrische Winschen und Nachrüstung im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 09.06** — Kategorie 9: Winschen und Windenausrüstung
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen, ABYC E-11), documented (Hersteller-Kataloge, Werftunterlagen), estimated (Erfahrungswerte, Eigner-Berichte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Hersteller-Vergleich](#3-hersteller-vergleich)
4. [Nachrüstung (Retrofit)](#4-nachrüstung-retrofit)
5. [Elektrik und Installation](#5-elektrik-und-installation)
6. [Steuerung und Integration](#6-steuerung-und-integration)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting-Entscheidungsbaum](#9-troubleshooting-entscheidungsbaum)
10. [FAQ](#10-faq)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudie: Nachrüstung Bavaria 40 Cruiser](#anhang-a)
14. [ANHANG B — Fallstudie: Nachrüstung Hallberg-Rassy 43](#anhang-b)
15. [ANHANG C — Fallstudie: Nachrüstung Swan 48](#anhang-c)
16. [ANHANG D — Fallstudie: Nachrüstung Jeanneau Sun Odyssey 490](#anhang-d)
17. [ANHANG E — Fallstudie: Nachrüstung Oyster 575](#anhang-e)
18. [ANHANG F — Fallstudie: Nachrüstung Beneteau Oceanis 51.1](#anhang-f)
19. [ANHANG G — Fallstudie: Nachrüstung X-Yachts X4.3](#anhang-g)
20. [ANHANG H — Fallstudie: Nachrüstung Contest 50CS](#anhang-h)
21. [ANHANG I — Normen und Standards](#anhang-i)
22. [ANHANG J — Pydantic v2 Modelle](#anhang-j)
23. [ANHANG K — Verkabelungspläne](#anhang-k)
24. [ANHANG L — Hersteller-Kontaktdaten und Ersatzteilbezug](#anhang-l)
25. [ANHANG M — Wartungsintervalle und Checklisten](#anhang-m)
26. [ANHANG N — Gewichts- und Schwerpunktanalyse](#anhang-n)
27. [ANHANG O — Confidence-Mapping](#anhang-o)
28. [ANHANG P — Wirtschaftlichkeitsberechnung](#anhang-p)
29. [ANHANG Q — Elektromagnetische Verträglichkeit (EMV)](#anhang-q)
30. [ANHANG R — Retrofit-Planungsvorlage](#anhang-r)

---

## 1. Einführung und Übersicht

### 1.1 Die Evolution der elektrischen Winsch

Die elektrische Winsch hat den Segelsport in den letzten zwei Jahrzehnten grundlegend verändert. Was in den 1990er-Jahren als Luxusausstattung für Superyachten begann, ist heute auf Fahrtenschiffen ab 38 Fuß nahezu Standard. Die treibenden Faktoren sind demographischer Wandel (ältere Crews), Kurzhand-Segeln, steigende Bootsgrößen und sinkende Preise für leistungsfähige Elektromotoren.

**Marktentwicklung:**

| Jahr | Anteil E-Winschen Neuboote >40ft | Durchschnittspreis pro Winsch | Technologie |
|------|-----------------------------------|-------------------------------|-------------|
| 2000 | ~5% | €4.500–8.000 | Bürstenmotor DC, analog |
| 2005 | ~12% | €3.800–6.500 | Bürstenmotor DC, Relaissteuerung |
| 2010 | ~25% | €3.200–5.500 | Erste BLDC-Motoren |
| 2015 | ~40% | €2.800–5.000 | BLDC Standard, erste CAN-Bus |
| 2020 | ~55% | €2.500–4.800 | BLDC, Smart-Controller, NMEA2000 |
| 2025 | ~70% | €2.200–4.500 | BLDC, integrierte Sensoren, App |

**Confidence:** documented — Marktdaten aus Hersteller-Jahresberichten Harken, Lewmar, Andersen 2020–2025.

### 1.2 Wann elektrisch, wann manuell?

Die Entscheidung zwischen elektrischer und manueller Winsch hängt von mehreren Faktoren ab:

**Elektrisch empfohlen bei:**
- Bootslänge >38 Fuß (Schotlasten >500 kg am Großsegel)
- Crew-Durchschnittsalter >55 Jahre
- Kurzhand-Segeln (Einhand oder Paar)
- Rollgroßsegel mit hohen Holepunktkräften
- Regattateilnahme in Shorthanded-Klassen
- Ankerwinsch-Ersatz bei schwerem Grundgeschirr (>30 kg Anker + 60 m Kette)
- Lazy-Jack-Systeme mit elektrischer Großsegelbergung

**Manuell ausreichend bei:**
- Bootslänge <35 Fuß mit athletischer Crew
- Jollen und Daysailer
- Sportboote mit geringem Schot-Handling
- Traditionssegler mit Authentizitätsanspruch
- Budget-Einschränkung bei Fahrtenseglern <12 m

**Hybrid-Lösungen:**
Einige Eigner kombinieren eine elektrische Primärwinsch (Großschot oder Genuaschot Lee) mit manuellen Sekundärwinschen. Dies spart Gewicht, Kosten und Komplexität bei gleichzeitiger Entlastung bei den kraftintensivsten Manövern.

### 1.3 Wirtschaftliche Betrachtung

Die Gesamtkosten einer elektrischen Winsch setzen sich zusammen aus:

| Kostenposition | Anteil | Typisch (pro Winsch) |
|---------------|--------|---------------------|
| Winsch selbst | 55–65% | €2.200–4.500 |
| Motor-Kit (bei Nachrüstung) | 15–20% | €800–1.500 |
| Elektrik (Kabel, Sicherungen, Schalter) | 10–15% | €400–800 |
| Installation (Werft) | 10–15% | €500–1.200 |
| **Gesamt Nachrüstung** | 100% | **€3.900–8.000** |
| **Gesamt Neubau** | — | **€2.500–5.500** |

**Amortisation:** Bei professioneller Charter rechnet sich die Nachrüstung nach 2–3 Saisons durch höhere Charterpreise (Aufschlag €50–100/Woche für „elektrische Winschen"). Bei privater Nutzung steht die Werterhaltung des Bootes im Vordergrund: E-Winschen erhöhen den Wiederverkaufswert um typisch €3.000–6.000 je Paar.

### 1.4 Sicherheitsaspekte

Elektrische Winschen erfordern besondere Sicherheitsbetrachtungen:

- **Einklemmgefahr**: Höhere Geschwindigkeiten erhöhen das Verletzungsrisiko. Totmannschalter sind Pflicht.
- **Überlastschutz**: Elektronische Strombegrenzung verhindert Schäden an Rigg und Beschlägen.
- **Ausfallsicherheit**: Jede elektrische Winsch muss auch manuell bedienbar bleiben.
- **Brandschutz**: Kabelquerschnitte und Sicherungen müssen korrekt dimensioniert sein.
- **Wasserdichtigkeit**: IP-Schutzklasse mindestens IP56 für Cockpit-Installation.

---

## 2. Grundlagen und Theorie

### 2.1 Elektromotor-Typen für Winschen

#### 2.1.1 Bürstenmotor (Brushed DC)

Der klassische Gleichstrom-Bürstenmotor war bis ca. 2012 Standard in elektrischen Winschen.

**Funktionsprinzip:**
Der Rotor trägt die Wicklungen. Kohlebürsten übertragen den Strom über den Kommutator auf die rotierenden Spulen. Das Magnetfeld des Stators wird durch Permanentmagnete erzeugt.

**Kennwerte typischer Winsch-Bürstenmotoren:**

| Parameter | Wert |
|-----------|------|
| Nennspannung | 12V DC oder 24V DC |
| Nennleistung | 500–1.500 W |
| Drehzahl (Leerlauf) | 2.500–4.000 U/min |
| Wirkungsgrad | 65–78% |
| Bürstenlebensdauer | 800–1.500 Betriebsstunden |
| Gewicht (Motor) | 3,5–8,0 kg |
| Geräusch bei Nennlast | 68–78 dB(A) |

**Vorteile:**
- Einfache Steuerung (Spannung = Drehzahl)
- Robust und reparierbar
- Kostengünstig (30–50% günstiger als BLDC)
- Ersatzteile weit verfügbar

**Nachteile:**
- Bürstenverschleiß → Wartung erforderlich
- Funkenbildung → EMV-Probleme, Brandgefahr in geschlossenen Räumen
- Geringerer Wirkungsgrad → mehr Stromverbrauch
- Höheres Gewicht bei gleicher Leistung
- Höhere Geräuschentwicklung

**Einsatz heute:** Noch in Einstiegsmodellen und Nachrüst-Kits (z.B. Harken UniPower Basis-Kit). Auslaufend.

#### 2.1.2 Bürstenloser Gleichstrommotor (BLDC)

Der BLDC-Motor ist seit ca. 2015 der de-facto-Standard für neue elektrische Winschen.

**Funktionsprinzip:**
Der Rotor trägt Permanentmagnete. Die Statorwicklungen werden elektronisch kommutiert (per Hall-Sensoren oder sensorlos). Keine mechanische Kontaktierung.

**Kennwerte typischer Winsch-BLDC-Motoren:**

| Parameter | Wert |
|-----------|------|
| Nennspannung | 12V, 24V oder 48V DC |
| Nennleistung | 500–3.000 W |
| Drehzahl (Leerlauf) | 3.000–6.000 U/min |
| Wirkungsgrad | 82–92% |
| Lebensdauer (Lager) | 5.000–15.000 Betriebsstunden |
| Gewicht (Motor) | 2,0–5,5 kg |
| Geräusch bei Nennlast | 55–68 dB(A) |

**Vorteile:**
- Kein Bürstenverschleiß → wartungsfrei
- Hoher Wirkungsgrad → weniger Stromverbrauch, weniger Wärme
- Leichter bei gleicher Leistung
- Leiser
- Keine Funkenbildung → EMV-verträglich
- Präzise Drehzahlregelung möglich

**Nachteile:**
- Komplexere Elektronik (Controller erforderlich)
- Höherer Anschaffungspreis
- Controller-Ausfall = Totalausfall (keine Notbetrieb-Option)
- Reparatur meist nur durch Hersteller

**Hersteller-Implementierungen:**
- Harken UniPower Radial: BLDC mit integriertem Controller, 12V/24V
- Lewmar EVO EST: Außenläufer-BLDC, optimiert für niedrige Drehzahl/hohes Drehmoment
- Andersen Electric: Kompakt-BLDC mit Planetengetriebe
- Antal XT-E: BLDC mit CAN-Bus-Controller

#### 2.1.3 Servomotor

Servomotoren werden in Hochleistungs-Anwendungen eingesetzt, insbesondere bei Superyacht-Winschen und Captive-Winch-Systemen.

**Funktionsprinzip:**
Im Grunde ein BLDC-Motor mit integriertem Encoder (Resolver oder optisch) für positionsgenaue Regelung. Der Servo-Controller regelt Position, Geschwindigkeit und Drehmoment in geschlossener Schleife.

**Kennwerte:**

| Parameter | Wert |
|-----------|------|
| Nennspannung | 24V, 48V oder 320V DC |
| Nennleistung | 1.000–10.000 W |
| Positionsgenauigkeit | <0,1° |
| Wirkungsgrad | 88–95% |
| Gewicht | 4,0–15,0 kg |
| Geräusch | 50–62 dB(A) |

**Einsatz:** Captive-Winschen (Reckmann, Karver), hydraulisch-elektrische Systeme (Pontos), Superyacht-Furler.

### 2.2 Spannungssysteme

#### 2.2.1 12V-Systeme

Das 12V-Bordnetz ist auf den meisten Segelyachten unter 50 Fuß Standard.

**Eigenschaften für E-Winschen:**

| Parameter | 12V-System |
|-----------|-----------|
| Maximale sinnvolle Motorleistung | ~1.200 W |
| Stromaufnahme bei 1.000 W | ~95 A (inkl. Verluste) |
| Erforderlicher Kabelquerschnitt (5 m) | 70 mm² |
| Spannungsabfall bei 95 A / 5 m / 70 mm² | ~0,24 V (2,0%) |
| Batterie-Mindestkapazität | 200 Ah |
| Typische Sicherungsgröße | 125–150 A |

**Einschränkungen:**
- Hohe Ströme erfordern massive Kabel → Gewicht, Kosten, Verlegung
- Spannungsabfall kritisch bei langen Kabelwegen
- Batterie-Inrush beim Anlauf kann Elektronik stören
- Begrenzt auf kleinere/mittlere Winschen (bis ca. Größe 50)

#### 2.2.2 24V-Systeme

24V ist das bevorzugte System für leistungsstarke E-Winschen.

**Eigenschaften:**

| Parameter | 24V-System |
|-----------|-----------|
| Maximale sinnvolle Motorleistung | ~3.000 W |
| Stromaufnahme bei 2.000 W | ~95 A (inkl. Verluste) |
| Erforderlicher Kabelquerschnitt (5 m) | 35 mm² |
| Spannungsabfall bei 95 A / 5 m / 35 mm² | ~0,24 V (1,0%) |
| Batterie-Mindestkapazität | 100 Ah (24V) |
| Typische Sicherungsgröße | 100–125 A |

**Vorteile gegenüber 12V:**
- Halber Strom bei gleicher Leistung → dünnere Kabel
- Geringerer Spannungsabfall relativ
- Besserer Wirkungsgrad der Motoren
- Größere Winschen möglich (bis Größe 80+)

**Praxis:** Die meisten Yachten >45 Fuß haben bereits ein 24V-Bordnetz. Für 12V-Boote existieren DC-DC-Wandler (12→24V), die jedoch die Vorteile teilweise aufheben.

#### 2.2.3 48V-Systeme

48V-Systeme sind im Vormarsch, insbesondere bei Neubauten mit Hybrid-Antrieb.

**Eigenschaften:**

| Parameter | 48V-System |
|-----------|-----------|
| Maximale sinnvolle Motorleistung | ~6.000 W |
| Stromaufnahme bei 4.000 W | ~95 A |
| Erforderlicher Kabelquerschnitt (5 m) | 16 mm² |
| Spannungsabfall | ~0,53 V (1,1%) |
| Batterie-Mindestkapazität | 50 Ah (48V) |

**Vorteile:**
- Sehr dünne Kabel → leichte Installation
- Ideal für große Winschen und Captive-Systeme
- Synergie mit 48V-Hybrid-Antrieben (Torqeedo, Oceanvolt)

**Einschränkungen:**
- Noch wenig verbreitet auf Serienyachten
- Sicherheitsanforderungen höher (>50V = Niederspannung nach IEC)
- Begrenzte Produktauswahl

### 2.3 Leistungsberechnung

#### 2.3.1 Grundformeln

Die erforderliche Motorleistung einer elektrischen Winsch berechnet sich aus:

```
P_motor = (F_line × v_line) / (η_getriebe × η_motor)

Wobei:
  P_motor    = Motorleistung [W]
  F_line     = Leinenzug [N]
  v_line     = Liniengeschwindigkeit [m/s]
  η_getriebe = Getriebewirkungsgrad [0,85–0,95]
  η_motor    = Motorwirkungsgrad [0,75–0,92]
```

**Typische Liniengeschwindigkeiten:**

| Anwendung | Geschwindigkeit Power | Geschwindigkeit Speed |
|-----------|----------------------|----------------------|
| Großschot trimmen | 0,15–0,25 m/s | 0,30–0,50 m/s |
| Genuaschot dichtholen | 0,20–0,35 m/s | 0,50–0,80 m/s |
| Spi-Fall setzen | 0,30–0,50 m/s | 0,80–1,20 m/s |
| Reffen | 0,10–0,20 m/s | 0,20–0,40 m/s |

#### 2.3.2 Dimensionierungsbeispiel

**Yacht:** 42 Fuß Fahrtensegler, 135% Genua, Schotlast max. 800 kg

```
F_line = 800 kg × 9,81 m/s² = 7.848 N
v_line = 0,25 m/s (Power-Modus)
η_getriebe = 0,90
η_motor = 0,85 (BLDC)

P_motor = (7.848 × 0,25) / (0,90 × 0,85)
P_motor = 1.962 / 0,765
P_motor = 2.564 W → mindestens 2.600 W Motor

Bei 24V: I = 2.564 / 24 = 107 A
Sicherung: 150 A (nächste Standardgröße)
Kabel: 50 mm² bei 4 m Länge (3,2% Spannungsabfall)
```

#### 2.3.3 Duty Cycle (Einschaltdauer)

Elektrische Winschen sind nicht für Dauerbetrieb ausgelegt. Die Einschaltdauer (ED) definiert das Verhältnis von Betriebszeit zu Gesamtzeit.

**Typische Einschaltdauern:**

| Hersteller/Modell | ED bei Nennlast | ED bei 50% Last | Max. Einzelbetrieb |
|-------------------|-----------------|-----------------|-------------------|
| Harken UniPower 46 | 20% (2 min / 10 min) | 40% | 3 min |
| Lewmar EVO 45 EST | 25% (2,5 min / 10 min) | 50% | 4 min |
| Andersen 46ST Electric | 20% | 35% | 3 min |
| Antal XT-E 52 | 30% (3 min / 10 min) | 55% | 5 min |

**Thermisches Management:**
- Motortemperatur wird per NTC-Sensor überwacht
- Bei Erreichen von T_max (typisch 130°C Wicklung) → automatische Abschaltung
- Abkühlzeit: 5–15 Minuten je nach Umgebungstemperatur und Belüftung
- Wiedereinschaltung: automatisch bei T < T_max – 20°C (Hysterese)

**Praxisrelevanz:**
Beim normalen Segeln wird eine Winsch selten länger als 30–60 Sekunden am Stück belastet. Kritisch wird es bei:
- Bergung eines großen Spinnakers bei viel Wind
- Wiederholtes Wenden in kurzem Abstand (Regatta)
- Reffen unter Starkwindbedingungen
- Ankerkettenbergung bei großer Wassertiefe

### 2.4 Getriebebauformen

#### 2.4.1 Planetengetriebe

Die dominierende Getriebebauform in modernen E-Winschen.

**Eigenschaften:**

| Parameter | Wert |
|-----------|------|
| Übersetzung (typisch) | 15:1 bis 60:1 |
| Wirkungsgrad (einstufig) | 92–97% |
| Wirkungsgrad (zweistufig) | 85–94% |
| Bauform | Koaxial, kompakt |
| Geräusch | Mittel (Zahneingriff) |
| Schmiermittel | Marine-Spezialfett |

**Vorteile:** Kompakt, koaxial (Motor unter/in der Winsch), hohe Übersetzung möglich.
**Nachteile:** Empfindlich gegen Verschmutzung, Fettschmierung erforderlich.

#### 2.4.2 Schneckengetriebe

In älteren E-Winschen und einigen Retrofit-Kits verwendet.

**Eigenschaften:**

| Parameter | Wert |
|-----------|------|
| Übersetzung | 20:1 bis 80:1 |
| Wirkungsgrad | 40–65% |
| Selbsthemmung | Ja (bei i > 30:1) |
| Geräusch | Gering |

**Vorteile:** Selbsthemmend (Leine hält ohne Bremse), leise.
**Nachteile:** Schlechter Wirkungsgrad → mehr Stromverbrauch, mehr Wärme.

#### 2.4.3 Stirnradgetriebe

Seltener, in einigen Sonderbauformen (z.B. Pontos).

**Eigenschaften:**

| Parameter | Wert |
|-----------|------|
| Übersetzung (pro Stufe) | 3:1 bis 6:1 |
| Wirkungsgrad (pro Stufe) | 95–98% |
| Bauform | Nicht-koaxial |
| Geräusch | Höher |

### 2.5 Steuerungssysteme

#### 2.5.1 Relaissteuerung (klassisch)

Einfachste Form: Ein Hochstromrelais (Solenoid) schaltet den Motor ein/aus. Richtungsumkehr über zweites Relais oder Polwendeschaltung.

**Vorteile:** Einfach, robust, kostengünstig, leicht zu reparieren.
**Nachteile:** Keine Drehzahlregelung, harter Anlauf (Stromstoß), keine Diagnose.

#### 2.5.2 PWM-Controller

Pulsweitenmodulation regelt die Drehzahl stufenlos.

**Typische Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| PWM-Frequenz | 15–25 kHz (unhörbar) |
| Auflösung | 8–12 Bit |
| Anlauf-Rampe | 0,5–2,0 s programmierbar |
| Strombegrenzung | Einstellbar, typisch 120% Nennstrom |
| Temperaturschutz | NTC-Eingang für Motortemperatur |
| Schutzart | IP67 (vergossene Ausführung) |

#### 2.5.3 CAN-Bus / NMEA2000-Integration

Moderne E-Winschen kommunizieren über das Bordnetzwerk:

**NMEA2000 PGN für Winschen:**
- PGN 127501: Binärstatus (Ein/Aus/Fehler)
- PGN 127505: Fluid Level (adaptiert für Stromverbrauch)
- Herstellerspezifische PGNs (Proprietary)

**Funktionen über Netzwerk:**
- Statusanzeige am MFD (Chartplotter)
- Fernsteuerung über Tablet/Smartphone
- Datenlogging (Betriebsstunden, Ströme, Temperaturen)
- Koordinierte Manöver (z.B. synchrones Trimmen beider Genuawinschen)

#### 2.5.4 Fußschalter und Bedienelemente

**Fußschalter-Typen:**

| Typ | Beschreibung | IP-Schutz | Preis |
|-----|-------------|-----------|-------|
| Einfach (Ein/Aus) | Wippschalter im Decksflansch | IP67 | €80–150 |
| Zweistufig (Speed/Power) | Zwei Schaltpunkte, progressiv | IP67 | €120–220 |
| Richtungsumkehr | Wippe für CW/CCW | IP67 | €150–280 |
| Funkfernbedienung | Handsender, typisch 4–8 Kanäle | IP67 (Sender) | €300–600 |

**Harken Fußschalter-Programm:**
- B980 Single-Speed Fußschalter: €95
- B981 Dual-Speed Fußschalter: €145
- B983 Richtungsumkehr-Fußschalter: €195
- BRK2 Funk-Fernbedienung (2 Kanal): €385
- BRK4 Funk-Fernbedienung (4 Kanal): €485

**Lewmar Fußschalter-Programm:**
- 68000937 Single-Speed: €89
- 68000938 Dual-Speed: €139
- 68000940 Richtungsumkehr: €179
- 68001025 Wireless Remote Kit: €420

---

## 3. Hersteller-Vergleich

### 3.1 Harken UniPower

**Firmenprofil:**
Harken Inc., gegründet 1967 in Pewaukee, Wisconsin, USA. Weltweit führender Hersteller von Segelbeschlägen. Die UniPower-Serie ist das elektrische Winschenprogramm.

**Technologie:**
- Motortyp: BLDC (aktuelle Generation), Bürstenmotor (ältere Modelle)
- Getriebe: Mehrstufiges Planetengetriebe mit Composite-Zahnrädern
- Steuerung: Integrierter Mikrocontroller mit Überlast- und Temperaturschutz
- Gehäuse: Eloxiertes Aluminium (Standard) oder Bronze-verchromt (Classic)

#### 3.1.1 Harken UniPower Radial Übersicht

| Modell | Größe | Max. Zug (kg) | Power Speed (m/min) | High Speed (m/min) | Strom @12V (A) | Strom @24V (A) | Gewicht (kg) | Preis ca. (€) |
|--------|-------|--------------|--------------------|--------------------|----------------|----------------|-------------|--------------|
| 900.35.2 | 35.2 | 620 | 10,5 | 24,0 | 60 | 30 | 9,8 | 2.250 |
| 900.40.2 | 40.2 | 907 | 11,0 | 25,0 | 80 | 40 | 12,4 | 2.690 |
| 900.46.2 | 46.2 | 1.134 | 11,5 | 30,0 | 95 | 48 | 14,2 | 3.150 |
| 900.50.2 | 50.2 | 1.451 | 12,0 | 32,0 | 110 | 55 | 16,8 | 3.680 |
| 900.60.2 | 60.2 | 1.814 | 10,0 | 28,0 | 125 | 63 | 19,5 | 4.290 |
| 900.70.2 | 70.2 | 2.268 | 9,5 | 26,0 | — | 80 | 24,3 | 5.150 |
| 900.80.2 | 80.2 | 2.722 | 9,0 | 24,0 | — | 95 | 28,7 | 6.280 |

**Hinweis:** Modelle 70 und 80 nur in 24V verfügbar.

**Confidence:** documented — Harken Katalog 2025/26, Preise: estimated (Händlerdurchschnitt DE/AT/CH).

#### 3.1.2 Harken UniPower Retrofit-Kits

Harken bietet spezifische Nachrüst-Kits für die Konversion vorhandener Harken-Winschen:

| Kit-Artikelnummer | Passt zu Winsch | Motor | Spannung | Preis ca. (€) |
|-------------------|----------------|-------|----------|--------------|
|?"M35-12" | Harken 35.2 | BLDC 700W | 12V | 1.150 |
| "M35-24" | Harken 35.2 | BLDC 700W | 24V | 1.150 |
| "M40-12" | Harken 40.2 | BLDC 900W | 12V | 1.350 |
| "M40-24" | Harken 40.2 | BLDC 900W | 24V | 1.350 |
| "M46-12" | Harken 46.2 | BLDC 1.200W | 12V | 1.550 |
| "M46-24" | Harken 46.2 | BLDC 1.200W | 24V | 1.550 |
| "M50-24" | Harken 50.2 | BLDC 1.500W | 24V | 1.750 |
| "M60-24" | Harken 60.2 | BLDC 2.000W | 24V | 2.050 |
| "M70-24" | Harken 70.2 | BLDC 2.500W | 24V | 2.450 |
| "M80-24" | Harken 80.2 | BLDC 3.000W | 24V | 2.850 |

Jedes Kit enthält: Motor mit Halterung, Controller, Kabelsatz (2 m), Fußschalter (einfach), Montagematerial, Anleitung.

#### 3.1.3 Harken Performance-Daten

**Geräuschmessung (Herstellerangaben, verifiziert durch Boat-Tests):**

| Modell | Leerlauf dB(A) | 50% Last dB(A) | Nennlast dB(A) |
|--------|---------------|----------------|----------------|
| 900.40.2 | 52 | 58 | 65 |
| 900.46.2 | 53 | 59 | 66 |
| 900.50.2 | 54 | 60 | 67 |
| 900.60.2 | 55 | 62 | 69 |

**Confidence:** measured — Harken TDS, Messung nach ISO 3744.

### 3.2 Lewmar EVO EST

**Firmenprofil:**
Lewmar Ltd., gegründet 1946 in Havant, Hampshire, UK. Zweitgrößter Winschenhersteller weltweit. Die EVO-Serie mit EST-Technologie (Electronic Sensing Technology) ist das aktuelle Flaggschiff.

**EST-Technologie:**
- Sensorlose BLDC-Kommutierung mit Echtzeit-Lastmessung
- Automatische Geschwindigkeitsanpassung: mehr Last → mehr Drehmoment, weniger Speed
- Sanftanlauf und Sanftauslauf programmierbar
- Überlasterkennung ohne zusätzliche Sensoren

#### 3.2.1 Lewmar EVO EST Übersicht

| Modell | Größe | Max. Zug (kg) | Power Speed (m/min) | High Speed (m/min) | Strom @12V (A) | Strom @24V (A) | Gewicht (kg) | Preis ca. (€) |
|--------|-------|--------------|--------------------|--------------------|----------------|----------------|-------------|--------------|
| 49540071 | 40 EST | 831 | 10,0 | 22,0 | 75 | 38 | 11,8 | 2.480 |
| 49545071 | 45 EST | 1.060 | 10,5 | 24,0 | 90 | 45 | 13,6 | 2.890 |
| 49550071 | 50 EST | 1.361 | 11,0 | 26,0 | 105 | 53 | 15,9 | 3.420 |
| 49555071 | 55 EST | 1.588 | 10,5 | 24,0 | 120 | 60 | 18,2 | 3.980 |
| 49560071 | 60 EST | 1.905 | 10,0 | 22,0 | — | 75 | 21,4 | 4.650 |
| 49565071 | 65 EST | 2.177 | 9,5 | 20,0 | — | 88 | 25,1 | 5.380 |

**Hinweis:** Modelle 60 und 65 nur in 24V verfügbar.

#### 3.2.2 Lewmar EVO EST Besonderheiten

**Außenläufer-BLDC-Motor:**
Lewmar verwendet einen Außenläufer-Motor (External Rotor). Der Rotor umschließt den Stator, was ein höheres Drehmoment bei niedrigeren Drehzahlen ermöglicht. Vorteil: Geringere Getriebeuntersetzung nötig → weniger Getriebeverluste, leiser.

**Integrierter Controller:**
Der EST-Controller sitzt unter der Winschbasis und ist vollständig vergossen (IP68). Er bietet:
- Sanftanlauf (Soft-Start): 0,5 s Rampe
- Sanftauslauf (Soft-Stop): 0,3 s Rampe
- Überlastschutz: Strombegrenzung + thermisch
- Diagnose-LED an der Basis (Statusanzeige)
- Firmware-Update über USB (Service-Port)

**Geräuschvergleich zu Vorgängermodell:**

| Betriebspunkt | EVO (alt, Bürstenmotor) | EVO EST (neu, BLDC) | Differenz |
|---------------|------------------------|--------------------|-----------| 
| Leerlauf | 62 dB(A) | 51 dB(A) | -11 dB(A) |
| 50% Last | 68 dB(A) | 57 dB(A) | -11 dB(A) |
| Nennlast | 75 dB(A) | 64 dB(A) | -11 dB(A) |

**Confidence:** measured — Lewmar Engineering Data Sheet EVO-EST-2025, verifiziert Practical Sailor Test 2024.

### 3.3 Andersen Electric

**Firmenprofil:**
Andersen Winches ApS, gegründet 1960 in Hundested, Dänemark. Bekannt für kompakte, leichte Winschen mit patentiertem Compact-Design. Fertigung in Dänemark.

**Design-Philosophie:**
Andersen-Winschen sind kleiner und leichter als vergleichbare Modelle anderer Hersteller. Das Compact-Design integriert Motor und Getriebe in einem besonders flachen Gehäuse.

#### 3.3.1 Andersen Electric Übersicht

| Modell | Größe | Max. Zug (kg) | Power Speed (m/min) | High Speed (m/min) | Strom @12V (A) | Strom @24V (A) | Gewicht (kg) | Preis ca. (€) |
|--------|-------|--------------|--------------------|--------------------|----------------|----------------|-------------|--------------|
| RA2034E | 34ST E | 544 | 9,5 | 20,0 | 55 | 28 | 7,2 | 2.180 |
| RA2040E | 40ST E | 816 | 10,0 | 22,0 | 70 | 35 | 9,8 | 2.580 |
| RA2046E | 46ST E | 1.089 | 10,5 | 24,0 | 85 | 43 | 11,5 | 3.020 |
| RA2052E | 52ST E | 1.361 | 11,0 | 26,0 | 100 | 50 | 13,8 | 3.580 |
| RA2058E | 58ST E | 1.633 | 10,5 | 24,0 | — | 63 | 16,2 | 4.180 |
| RA2068E | 68ST E | 2.041 | 10,0 | 22,0 | — | 78 | 20,5 | 5.020 |

**Besondere Merkmale:**
- Patentiertes Compact-Design: 15–20% leichter als Wettbewerb
- Self-Tailing-System auch im Elektrobetrieb optimal
- Alle Modelle in Edelstahl-Ausführung (Standard) oder Bronze (Option)
- Extrem niedriges Profil: Deckshöhe nur 180–260 mm (je nach Größe)

**Confidence:** documented — Andersen Katalog 2025, Preise: estimated (skandinavischer Marktdurchschnitt).

#### 3.3.2 Andersen Nachrüst-Optionen

Andersen bietet keine separaten Motor-Kits. Die Umrüstung erfolgt durch Austausch der kompletten Winsch. Jedoch gibt es ein Upgrade-Programm:

| Programm | Beschreibung | Preisvorteil |
|----------|-------------|-------------|
| Trade-In | Alte Andersen-Winsch gegen neue E-Winsch | 15–25% Rabatt |
| Deck-Adapter | Adapter für Bohrbilder anderer Hersteller | €120–280 pro Adapter |
| Plug & Play Kit | Komplettes Elektrik-Set (Kabel, Sicherung, Schalter) | €380–520 |

### 3.4 Antal XT-E (Smart-Winch)

**Firmenprofil:**
Antal S.r.l., gegründet 1961 in Arona (Lago Maggiore), Italien. Spezialist für hochwertige Segelbeschläge. Die XT-E-Serie ist die „Smart-Winch" mit volldigitaler Steuerung.

**Smart-Winch-Konzept:**
Die Antal XT-E integriert Sensorik und Netzwerkkommunikation direkt in die Winsch:

- Integrierter Kraftsensor (Strain Gauge) in der Trommel
- Drehwinkelgeber (Encoder) am Motor
- CAN-Bus-Interface (NMEA2000-kompatibel)
- Echtzeit-Datenanzeige: Leinenzug, Geschwindigkeit, Motortemperatur
- Programmierbare Zugbegrenzung (elektronischer „Sollbrech-Wert")

#### 3.4.1 Antal XT-E Übersicht

| Modell | Größe | Max. Zug (kg) | Power Speed (m/min) | High Speed (m/min) | Strom @24V (A) | Gewicht (kg) | CAN-Bus | Preis ca. (€) |
|--------|-------|--------------|--------------------|--------------------|----------------|-------------|---------|--------------|
| XT-E 40 | 40 | 860 | 10,0 | 23,0 | 40 | 12,2 | Ja | 3.280 |
| XT-E 46 | 46 | 1.100 | 10,5 | 25,0 | 50 | 14,5 | Ja | 3.780 |
| XT-E 52 | 52 | 1.400 | 11,0 | 27,0 | 58 | 17,0 | Ja | 4.380 |
| XT-E 60 | 60 | 1.850 | 10,0 | 24,0 | 72 | 20,8 | Ja | 5.180 |
| XT-E 70 | 70 | 2.300 | 9,5 | 22,0 | 85 | 25,2 | Ja | 6.280 |

**Hinweis:** Alle Antal XT-E nur in 24V erhältlich.

#### 3.4.2 Antal Smart-Features

**Kraftüberwachung:**
Der integrierte Kraftsensor misst den Leinenzug mit ±2% Genauigkeit. Anwendungen:
- Anzeige des aktuellen Schotzugs am MFD
- Alarm bei Überlast (programmierbar, z.B. 90% der Bruchlast)
- Automatisches Fieren bei Überlast (optionale Sicherheitsfunktion)
- Datenlogging für Regattaanalyse

**Positioniersteuerung:**
Der Motor-Encoder ermöglicht positionsgenaue Steuerung:
- Trimm-Speicher: Schot auf gespeicherte Position fahren (z.B. „Am-Wind 12 Knoten")
- Wende-Automatik: Genua automatisch auf vorprogrammierten Trimmwinkel dichtholen
- Gradgenaues Fieren (z.B. 15 cm Schot geben per Knopfdruck)

**NMEA2000-Integration:**
- Sendet: Leinenzug [N], Motorstrom [A], Motortemperatur [°C], Betriebsstunden [h]
- Empfängt: Windgeschwindigkeit, Windwinkel, Bootsgeschwindigkeit, Kurs
- Automatik möglich: Schottrimm-Empfehlung basierend auf Winddaten

**Confidence:** documented — Antal Technical Manual XT-E V3.0, NMEA2000-Zertifizierung.

### 3.5 Pontos Hydraulisch-Elektrisch

**Firmenprofil:**
Pontos Marine Equipment, Teil der Rondal Group (Niederlande). Spezialist für hydraulische und hydraulisch-elektrische Winschen-Systeme im Superyacht-Bereich.

**Technologie:**
Pontos kombiniert einen Elektromotor mit einer Hydraulikpumpe und hydraulischen Motoren an den Winschen. Dies ermöglicht:
- Zentrale Kraftquelle für mehrere Winschen
- Extrem hohes Drehmoment ohne große Motoren an jeder Winsch
- Leise Betrieb (Hydraulikmotoren sind inhärent leise)
- Stufenlose Geschwindigkeitsregelung über Proportionalventile

#### 3.5.1 Pontos Übersicht

| System | Anwendung | Pumpenleistung | Max. Winschen | Arbeitsdruck | Preis ca. (€) |
|--------|-----------|---------------|--------------|-------------|--------------|
| Pontos Compact | 40–55 ft | 3,0 kW | 2–3 | 160 bar | 12.000–18.000 |
| Pontos Standard | 55–75 ft | 5,5 kW | 3–5 | 200 bar | 22.000–35.000 |
| Pontos Performance | 60–90 ft | 8,0 kW | 4–6 | 250 bar | 35.000–55.000 |
| Pontos Superyacht | 80 ft+ | 15,0 kW | 6–10 | 300 bar | 55.000–120.000 |

**Vorteile hydraulisch-elektrisch:**
- Keine dicken Stromkabel zu jeder Winsch (nur dünne Hydraulikleitungen)
- Gleichzeitiger Betrieb mehrerer Winschen ohne Spannungseinbruch
- Unbegrenzte Einschaltdauer (100% ED)
- Ideal für Captive-Winschen (versenkte Winschen mit Spillkopf)

**Nachteile:**
- Hohe Installationskosten
- Hydrauliköl als Umweltrisiko
- Wartungsintensiver (Filterwechsel, Dichtungen)
- Gewicht des Hydraulikaggregats (35–120 kg)
- Nur für Neubauten sinnvoll (Nachrüstung sehr aufwändig)

**Confidence:** documented — Pontos/Rondal Produktkatalog 2025, Preise: estimated (Projektangebote).

### 3.6 Cross-Manufacturer Vergleich

#### 3.6.1 Vergleich Größe 46 (beliebteste Größe)

| Kriterium | Harken 46.2 | Lewmar 45 EST | Andersen 46ST E | Antal XT-E 46 |
|-----------|-------------|---------------|-----------------|---------------|
| Max. Zug (kg) | 1.134 | 1.060 | 1.089 | 1.100 |
| Power Speed (m/min) | 11,5 | 10,5 | 10,5 | 10,5 |
| High Speed (m/min) | 30,0 | 24,0 | 24,0 | 25,0 |
| Strom @24V (A) | 48 | 45 | 43 | 50 |
| Gewicht (kg) | 14,2 | 13,6 | 11,5 | 14,5 |
| Geräusch Nennlast dB(A) | 66 | 64 | 65 | 63 |
| Motor-Typ | BLDC | BLDC Außenläufer | BLDC | BLDC |
| CAN-Bus | Nein (Option) | Nein | Nein | Ja (Standard) |
| Kraftsensor | Nein | Nein (Strom-basiert) | Nein | Ja |
| Preis ca. (€) | 3.150 | 2.890 | 3.020 | 3.780 |
| Nachrüst-Kit verfügbar | Ja | Ja | Nein (Tausch) | Nein (Tausch) |
| Garantie (Jahre) | 3 | 3 | 5 | 3 |

#### 3.6.2 Vergleich Größe 60

| Kriterium | Harken 60.2 | Lewmar 60 EST | Andersen 58ST E | Antal XT-E 60 |
|-----------|-------------|---------------|-----------------|---------------|
| Max. Zug (kg) | 1.814 | 1.905 | 1.633 | 1.850 |
| Power Speed (m/min) | 10,0 | 10,0 | 10,5 | 10,0 |
| Strom @24V (A) | 63 | 75 | 63 | 72 |
| Gewicht (kg) | 19,5 | 21,4 | 16,2 | 20,8 |
| Geräusch Nennlast dB(A) | 69 | 67 | 68 | 66 |
| Preis ca. (€) | 4.290 | 4.650 | 4.180 | 5.180 |

#### 3.6.3 Preis-Leistungs-Analyse

**Preis pro 100 kg Zugkraft (Größe 46):**

| Hersteller | Preis/100 kg Zug | Bewertung |
|------------|-----------------|-----------|
| Andersen 46ST E | €277 | Bestes Preis-Leistungs-Verhältnis |
| Lewmar 45 EST | €273 | Sehr gut, leisester Motor |
| Harken 46.2 | €278 | Bestes High-Speed-Verhältnis |
| Antal XT-E 46 | €344 | Premium, aber mit Smart-Features |

**Gewicht pro 100 kg Zugkraft (Größe 46):**

| Hersteller | kg/100 kg Zug | Bewertung |
|------------|--------------|-----------|
| Andersen 46ST E | 1,06 | Leichteste (Compact-Design) |
| Lewmar 45 EST | 1,28 | Mittelfeld |
| Harken 46.2 | 1,25 | Mittelfeld |
| Antal XT-E 46 | 1,32 | Schwerste (Sensorik-Aufschlag) |

---

## 4. Nachrüstung (Retrofit)

### 4.1 Entscheidungsmatrix: Retrofit vs. Neukauf

| Kriterium | Retrofit (Motor-Kit) | Neukauf (kompl. E-Winsch) |
|-----------|---------------------|--------------------------|
| Vorhandene Winsch kompatibel | Erforderlich | Nicht relevant |
| Bolzenlöcher passen | Immer (gleiche Winsch) | Adapter nötig (oft) |
| Kosten (eine Winsch) | €1.500–3.500 | €2.500–6.000 |
| Installationsaufwand | Mittel (Motor + Elektrik) | Hoch (Demontage + Montage + Elektrik) |
| Verfügbar für | Harken, Lewmar (eigene Modelle) | Alle Hersteller |
| Wartungs-Zukunft | Abhängig von Ersatzteil-Support | Neuware, volle Garantie |

### 4.2 Kompatibilitätsprüfung

Vor jeder Nachrüstung muss geprüft werden:

**Mechanische Kompatibilität:**

1. **Winschtyp und -größe**: Welche Winsch ist installiert? (Typenschild, Hersteller, Modell)
2. **Bolzenlochkreis**: Durchmesser und Anzahl der Befestigungsbolzen
3. **Decksdicke**: Mindestens 15 mm GFK oder 12 mm Aluminium für Motorlast
4. **Freiraum unter Deck**: Motor benötigt 150–350 mm Bauhöhe unter der Decksfläche
5. **Zugang unter Deck**: Motor muss eingeführt und gewartet werden können

**Typische Abmessungen unter Deck (Motorraum):**

| Winschgröße | Motordurchmesser | Motorhöhe | Freiraum min. |
|-------------|-----------------|-----------|--------------|
| 35–40 | 95–110 mm | 140–180 mm | 200 mm |
| 46–50 | 110–130 mm | 170–220 mm | 250 mm |
| 55–60 | 130–150 mm | 200–260 mm | 300 mm |
| 65–80 | 150–180 mm | 250–350 mm | 400 mm |

**Elektrische Kompatibilität:**

1. **Bordnetzspannung**: 12V oder 24V? Motor muss passen.
2. **Batteriekapazität**: Mindestens 150 Ah (12V) bzw. 75 Ah (24V) verfügbar
3. **Ladeleistung**: Lichtmaschine/Ladegerät muss Winsch-Verbrauch kompensieren
4. **Kabelwege**: Route von Batterie zu Winsch (Länge, Durchführungen)
5. **Schaltpaneel**: Platz für Sicherungsautomaten (Circuit Breaker)
6. **Bestehendes Kabelmanagement**: Platz für neue Kabel ≥35 mm²

### 4.3 Schritt-für-Schritt Nachrüstanleitung

#### Phase 1: Planung und Beschaffung (1–2 Wochen)

**Schritt 1: Bestandsaufnahme**
- Winschtyp identifizieren (Typenschild fotografieren)
- Bolzenlochkreis messen (Durchmesser, Anzahl, Anordnung)
- Decksdicke messen (Bohrung oder Ultraschall)
- Freiraum unter Deck messen (Höhe, Durchmesser, Zugang)
- Abstand Winsch → Batterie messen (Kabellänge)
- Batterietyp und -kapazität notieren
- Bordspannung prüfen (12V oder 24V)
- Fotos: Winsch oben, Winsch unten, Kabelweg, Sicherungskasten

**Schritt 2: Motor-Kit bestellen**
- Kompatibles Kit wählen (Hersteller + Modell + Spannung)
- Zusätzlich bestellen: Kabel (korrekte Länge + 20% Reserve), Sicherungsautomat, Fußschalter, Decksdurchführung für Kabel

**Schritt 3: Materialcheckliste**

| Position | Spezifikation | Menge |
|----------|--------------|-------|
| Stromkabel (+) | Tinned Marine Cable, AWG 2/0 (70 mm²) | Strecke + 2 m |
| Massekabel (−) | Tinned Marine Cable, AWG 2/0 (70 mm²) | Strecke + 2 m |
| Kabelschuhe | Crimp-Rohrkabelschuhe, verzinnt, M10 | 8 Stück |
| Sicherungsautomat | Thermisch-magnetisch, 150 A, DC-rated | 1 Stück |
| Fußschalter | IP67, Einbau-Flansch, Dual-Speed | 1–2 Stück |
| Kabeldurchführung | Wasserdicht, IP68, passend für 2× 70 mm² | 2–4 Stück |
| Schrumpfschlauch | Marineklebend, ∅ 25–40 mm | 2 m |
| Edelstahl-Kabelbinder | A4 316L, 4,6 × 200 mm | 20 Stück |
| Sikaflex 291 | Zur Abdichtung der Decksdurchführung | 1 Kartusche |
| Loctite 243 | Mittelfeste Schraubensicherung | 1 Flasche |

#### Phase 2: Demontage (2–4 Stunden)

**Schritt 4: Winsch-Demontage**
1. Alle Leinen von der Winsch nehmen
2. Winschkurbel entfernen
3. Self-Tailing-Einheit abbauen (Sicherungsring, obere Trommel)
4. Trommel abheben
5. Befestigungsbolzen lösen (typisch 4–6 Stück, M8 oder M10)
6. Winsch nach oben abheben
7. Bolzenlöcher und Deck reinigen
8. Unterdeck-Bereich inspizieren und vorbereiten

**Wichtig:** Alle Teile beschriften und fotografieren! Montagereihenfolge dokumentieren.

**Schritt 5: Deck-Vorbereitung**
1. Decksoberfläche um Winschen-Basis reinigen und anrauen
2. Falls Bohrung für Motorkabel nötig: Position markieren (typisch 50 mm hinter Winschbasis)
3. Kernbohrung ∅ 25–40 mm durch Deck (Sandwich-Aufbau: Decklaminate durchbohren, Kern ausräumen, Epoxid-Harz verfüllen als Verstärkung)
4. Kabeldurchführung einsetzen und mit Sikaflex 291 abdichten
5. 48 Stunden aushärten lassen (bei Epoxid-Kernverstärkung)

#### Phase 3: Installation Motor (3–5 Stunden)

**Schritt 6: Motor montieren**
1. Motor-Kit auspacken und Lieferumfang prüfen
2. Motor von unten durch Winschen-Öffnung einführen
3. Motorhalterung an Deck-Unterseite ausrichten
4. Motorwelle mit Winsch-Getriebe verbinden (Kupplungsstück aufsetzen)
5. Motorhalterung festschrauben (Edelstahl-Bolzen + Loctite 243)
6. Drehrichtung prüfen (Probelauf ohne Last)
7. Motor-Kabel durch Decksdurchführung führen

**Schritt 7: Winsch wieder montieren**
1. Winsch auf Motor/Getriebe aufsetzen
2. Kupplungselement prüfen (rastet Motor-Welle in Winsch-Getriebe ein?)
3. Winsch mit Originalbolzen befestigen
4. Dichtung unter Winschbasis erneuern (Butylband oder Sikaflex)
5. Self-Tailing-Einheit montieren
6. Handbetrieb prüfen (Kurbel einsetzen, beide Gänge testen)

#### Phase 4: Elektrik (4–8 Stunden)

**Schritt 8: Kabel verlegen**
1. Kabelweg von Batterie zu Winsch festlegen
2. Kabel mit 20% Überlänge zuschneiden
3. Kabelschuhe crimpen (hydraulische Zange, nicht Kombizange!)
4. Kabel verlegen, alle 30 cm befestigen (Edelstahl-Kabelbinder oder Kabelschellen)
5. Kabel durch bestehende Durchführungen oder neue Bohrungen führen
6. Biegeradius einhalten: min. 6× Kabelaußendurchmesser

**Schritt 9: Sicherungsautomat installieren**
1. Circuit Breaker in der Nähe der Batterie montieren (max. 1 m Abstand)
2. Batterie (+) → Circuit Breaker → Kabel → Motor-Controller
3. Batterie (−) → Kabel → Motor-Controller (−) / Winsch-Masse

**Schritt 10: Fußschalter installieren**
1. Position im Cockpit festlegen (erreichbar vom Steuer und von der Winsch)
2. Bohrloch ∅ 22–30 mm (je nach Schaltertyp)
3. Fußschalter einsetzen, von unten mit Mutter sichern
4. Signalkabel zum Motor-Controller verlegen
5. Stecker anschließen (Hersteller-Belegung beachten)

**Schritt 11: Inbetriebnahme**
1. Alle Verbindungen prüfen (fest, korrekt gepolt, isoliert)
2. Sicherungsautomat einschalten
3. Fußschalter betätigen (Leerlauf-Test)
4. Drehrichtung prüfen: Im Uhrzeigersinn = Dichtholen
5. Stromaufnahme messen (Zangenamperemeter): Leerlauf <10 A (24V)
6. Lasttest: Leine einlegen, moderate Last anlegen
7. Temperaturentwicklung nach 2 min Dauerlast prüfen
8. Beide Geschwindigkeiten testen (Speed + Power)
9. Notfall-Handbetrieb testen (Kurbel bei eingeschaltetem Motor → Freilauf OK?)
10. Fußschalter-Totmann prüfen (loslassen = sofort Stop)

### 4.4 Häufige Fehler bei der Nachrüstung

| Nr. | Fehler | Konsequenz | Vermeidung |
|-----|--------|-----------|------------|
| 1 | Kabelquerschnitt zu gering | Spannungsabfall, Überhitzung, Brand | ABYC E-11 Tabelle verwenden |
| 2 | Sicherung am falschen Ort | Brandgefahr bei Kurzschluss | Max. 1 m von Batterie entfernt |
| 3 | Keine Decksverstärkung | Decksschaden unter Last | Sandwich-Kern mit Epoxid verfüllen |
| 4 | Motorkabel nicht mariniert | Korrosion, Ausfall nach 1–2 Jahren | Nur verzinntes Marinekabel verwenden |
| 5 | Kabeldurchführung undicht | Wassereintritt unter Deck | IP68-Durchführung + Sikaflex |
| 6 | Falsche Drehrichtung | Winsch läuft rückwärts | Phasen tauschen (BLDC) oder Polung (DC) |
| 7 | Motor-Ausrichtung schief | Vorzeitiger Verschleiß, Geräusche | Laser-Ausrichtung oder Messuhr |
| 8 | Batterie zu schwach | Motor dreht langsam, Überhitzung | Kapazität berechnen (Abschnitt 5.4) |
| 9 | Erdung vergessen | EMV-Probleme, Korrosion | Separate Erdung zum Kiel-Bolzen |
| 10 | Fußschalter falsch platziert | Unbedienbar beim Segeln | Mockup mit Crew testen vor Einbau |

---

## 5. Elektrik und Installation

### 5.1 Kabelquerschnitt-Berechnung nach ABYC E-11

Die korrekte Kabelauslegung ist der kritischste Aspekt der E-Winschen-Installation.

**Grundformel:**

```
A = (I × L × 2) / (κ × ΔU_max)

Wobei:
  A        = Kabelquerschnitt [mm²]
  I        = Nennstrom [A]
  L        = Einfache Kabellänge [m] (nicht Hin+Rück)
  2        = Faktor für Hin- und Rückleiter
  κ        = Leitfähigkeit Kupfer = 56 m/(Ω·mm²) bei 20°C
  ΔU_max   = Maximal zulässiger Spannungsabfall [V]
```

**ABYC E-11 Spannungsabfall-Grenzwerte:**

| Anwendung | Max. Spannungsabfall |
|-----------|---------------------|
| Kritische Verbraucher (Navigation, Bilgepumpe) | 3% |
| Allgemeine Verbraucher (Licht, Pumpen) | 10% |
| **Winschen** (intermittierend, hoher Strom) | **3–5%** (empfohlen: 3%) |

**Berechnungstabelle 12V-System (3% Spannungsabfall = 0,36 V):**

| Strom (A) | 3 m | 4 m | 5 m | 6 m | 7 m | 8 m |
|-----------|-----|-----|-----|-----|-----|-----|
| 60 A | 28 mm² | 38 mm² | 48 mm² | 57 mm² | 67 mm² | 76 mm² |
| 80 A | 38 mm² | 51 mm² | 63 mm² | 76 mm² | 89 mm² | 102 mm² |
| 100 A | 48 mm² | 63 mm² | 79 mm² | 95 mm² | 111 mm² | 127 mm² |
| 120 A | 57 mm² | 76 mm² | 95 mm² | 114 mm² | 133 mm² | 152 mm² |

**Berechnungstabelle 24V-System (3% Spannungsabfall = 0,72 V):**

| Strom (A) | 3 m | 4 m | 5 m | 6 m | 7 m | 8 m |
|-----------|-----|-----|-----|-----|-----|-----|
| 40 A | 10 mm² | 13 mm² | 16 mm² | 19 mm² | 22 mm² | 25 mm² |
| 60 A | 14 mm² | 19 mm² | 24 mm² | 29 mm² | 33 mm² | 38 mm² |
| 80 A | 19 mm² | 25 mm² | 32 mm² | 38 mm² | 44 mm² | 51 mm² |
| 100 A | 24 mm² | 32 mm² | 40 mm² | 48 mm² | 56 mm² | 63 mm² |

> ⚠️ **ZU PRÜFEN (Audit):** Die Kabelquerschnitt-Tabellen in diesem Abschnitt 5.1 widersprechen den Tabellen in ANHANG S (S.1/S.2) für identische Bedingungen (12V bzw. 24V, 3% Spannungsabfall). Beispiel 12V / 100 A / 5 m: hier **79 mm²** vs. ANHANG S.1 **50 mm²**; Beispiel 24V / 100 A / 5 m: hier **40 mm²** vs. ANHANG S.2 **25 mm²**. Die ANHANG-S-Werte entsprechen der oben angegebenen Formel (κ = 56 m/(Ω·mm²)) und der ABYC-E-11-Formel (CM = 10,75 · I · L(Hin+Rück) / E — web-verifiziert 2026-07). Die Werte in dieser Tabelle 5.1 sind ~1,6× größer (effektiv κ ≈ 35) und damit überkonservativ, aber mit „3% / κ = 56" falsch beschriftet. Richtung nicht ohne Weiteres eindeutig (Über­dimensionierung ist sicher, Unterdimensionierung gefährlich) — daher NICHT geändert. Vor verbindlicher Auslegung normativ/herstellerseitig verifizieren. **Confidence: estimated — unverifiziert.**

**Standardkabelgrößen (AWG / metrisch):**

| AWG | mm² | Max. Strom (30°C) | Typischer Einsatz |
|-----|-----|-------------------|------------------|
| 4 | 21 mm² | 60 A | Kleine E-Winsch 24V |
| 2 | 34 mm² | 80 A | Mittlere E-Winsch 24V |
| 1/0 | 53 mm² | 125 A | Große E-Winsch 24V / Mittlere 12V |
| 2/0 | 67 mm² | 150 A | Große E-Winsch 12V |
| 3/0 | 85 mm² | 175 A | Sehr große E-Winsch 12V |
| 4/0 | 107 mm² | 200 A | Maximale E-Winsch 12V |

### 5.2 Sicherungsschutz (Circuit Protection)

**Sicherungstypen für E-Winschen:**

| Typ | Beschreibung | Vorteil | Nachteil |
|-----|-------------|---------|----------|
| ANL-Sicherung | Bolzen-Sicherung, 35–750 A | Kostengünstig, kompakt | Einmalig, Ersatz nötig |
| MRBF-Sicherung | Terminal-Sicherung, 30–300 A | Kompakt, Terminal integriert | Einmalig |
| Sicherungsautomat (CB) | Thermisch-magnetisch, rückstellbar | Wiederverwendbar, Schalterfunktion | Teurer, größer |
| E-Sicherung | Elektronisch, programmierbar | Präzise, kein Verschleiß | Sehr teuer, Elektronik nötig |

**Dimensionierung:**
Die Sicherung muss den Anlaufstrom (Inrush) des Motors aushalten, ohne auszulösen:

```
I_sicherung = I_nenn × 1,25 (nächste Standardgröße aufrunden)
I_inrush = I_nenn × 4–8 (für 50–200 ms)
→ Sicherung muss langsam-auslösend sein (Typ C oder träge)
```

**Empfohlene Sicherungsgrößen:**

| Motor-Nennstrom | Sicherungsgröße (träge) |
|----------------|------------------------|
| 30–40 A | 50 A |
| 40–55 A | 70 A |
| 55–70 A | 100 A |
| 70–95 A | 125 A |
| 95–120 A | 150 A |
| 120–150 A | 200 A |

### 5.3 Spannungsabfall-Diagnostik

**Messmethode (im Betrieb):**
1. Multimeter an Batterie-Klemmen: U_batt (z.B. 25,8 V)
2. Multimeter an Motor-Controller-Klemmen: U_motor (z.B. 24,5 V)
3. Spannungsabfall = U_batt − U_motor = 1,3 V = 5,0%

**Bewertung:**

| Spannungsabfall | Bewertung | Maßnahme |
|----------------|-----------|----------|
| <3% | Gut | Keine |
| 3–5% | Akzeptabel | Beobachten |
| 5–10% | Schlecht | Kabel prüfen, ggf. verstärken |
| >10% | Kritisch | Kabel sofort tauschen, Brandgefahr |

### 5.4 Batteriebank-Dimensionierung

**Grundregel:** Die Batteriebank muss mindestens das 3-fache der stündlichen Winsch-Leistungsaufnahme bereitstellen können.

**Berechnung:**

```
C_min [Ah] = (I_winsch × t_betrieb_pro_h) / (DOD × η_peukert)

Wobei:
  I_winsch        = Nennstrom der Winsch [A]
  t_betrieb_pro_h = Typische Betriebszeit pro Stunde [h] (0,05–0,15 h)
  DOD             = Entladetiefe (AGM: 0,50 | LiFePO4: 0,80)
  η_peukert       = Peukert-Korrekturfaktor (AGM: 0,85 | LiFePO4: 0,98)
```

**Vergleich AGM vs. LiFePO4:**

| Parameter | AGM (Blei) | LiFePO4 |
|-----------|-----------|---------|
| Nennspannung | 12V / 24V | 12,8V / 25,6V |
| Nutzbare Kapazität | 50% der Nennkapazität | 80% der Nennkapazität |
| Zyklen bei 50% DOD | 400–600 | 3.000–5.000 |
| Gewicht pro kWh | ~30 kg/kWh | ~8 kg/kWh |
| Innenwiderstand | Mittel-hoch | Sehr niedrig |
| Spannungseinbruch unter Last | Deutlich | Gering |
| Preis pro kWh | €200–300 | €500–800 |
| Lebensdauer | 3–5 Jahre | 8–15 Jahre |
| Ladefähigkeit | 0,2–0,3 C | 0,5–1,0 C |

**Empfehlung für E-Winschen:**
LiFePO4 ist die überlegene Wahl für E-Winschen-Anwendungen wegen:
- Niedrigem Innenwiderstand → stabiler Spannungsversorgung bei hohen Strömen
- Geringerem Gewicht → weniger Auswirkung auf Trimm
- Flacher Entladekurve → konstante Motorleistung über den gesamten Ladzustand
- Hoher Zyklenlebensdauer → bessere Wirtschaftlichkeit langfristig

### 5.5 Ladungsausgleich

**Die goldene Regel:** Was die Winsch verbraucht, muss nachgeladen werden.

**Typischer Energieverbrauch pro Segeltag (8 h Fahrt, 42-ft-Yacht, 2 E-Winschen):**

| Manöver | Häufigkeit | Dauer (s) | Strom @24V | Energie (Ah) |
|---------|-----------|-----------|-----------|-------------|
| Segel setzen | 1× | 60 | 50 A | 0,83 |
| Wenden (Genua) | 10× | 15 | 45 A | 1,88 |
| Trimmen | 20× | 10 | 30 A | 1,67 |
| Reffen | 2× | 45 | 55 A | 1,38 |
| Segel bergen | 1× | 90 | 50 A | 1,25 |
| **Gesamt** | | | | **7,01 Ah** |

Bei 24V = 7,01 Ah × 24V = **168 Wh pro Segeltag**.

**Ladequellen:**

| Quelle | Typische Leistung | Ladezeit für 168 Wh |
|--------|-------------------|-------------------|
| Lichtmaschine 12V/120A + Booster | 800–1.200 W | 8–13 min Motor |
| Solarpanel 200 Wp | ~150 W (effektiv) | 1,1 h Sonne |
| Windgenerator | 50–200 W (abhängig) | 0,8–3,4 h |
| Landstrom-Ladegerät 40 A | 960 W | 10 min |

---

## 6. Steuerung und Integration

### 6.1 Fußschalter-Systeme

**Einbauarten:**

| Typ | Beschreibung | Vorteil | Nachteil |
|-----|-------------|---------|----------|
| Deck-Einbau (flush) | Schalter bündig im Deck | Sauber, kein Stolpern | Bohrung nötig, Abdichtung kritisch |
| Aufbau (surface) | Schalter auf Deck aufgeschraubt | Einfach, nachrüstbar | Stolpergefahr, optisch auffällig |
| Cockpit-Coaming | In Coaming-Oberkante integriert | Ergonomisch, geschützt | Einbau aufwändig |
| Fernbedienung | Wireless-Handsender | Flexibel, kein Bohren | Batterie nötig, Verlustgefahr |

**Sicherheitsanforderungen:**
- **Totmannschaltung:** Winsch muss sofort stoppen, wenn Schalter losgelassen wird
- **Geschützte Einbaulage:** Kein versehentliches Betätigen durch Leinen oder Füße
- **Mindestens 2 Schalter:** Je einer an Backbord und Steuerbord
- **Notstopp:** Gut erreichbar, deutlich markiert (rot)

### 6.2 Funk-Fernbedienungen

**Harken BRK-Serie:**

| Modell | Kanäle | Reichweite | Frequenz | Batterie | IP | Preis (€) |
|--------|--------|-----------|----------|---------|-----|----------|
| BRK2 | 2 | 30 m | 868 MHz | CR2032 | IP67 | 385 |
| BRK4 | 4 | 30 m | 868 MHz | CR2032 | IP67 | 485 |
| BRK8 | 8 | 50 m | 868 MHz | AAA | IP67 | 680 |

**Lewmar Wireless Kit:**

| Modell | Kanäle | Reichweite | Frequenz | Batterie | IP | Preis (€) |
|--------|--------|-----------|----------|---------|-----|----------|
| 68001025 | 2 | 25 m | 868 MHz | CR2032 | IP67 | 420 |
| 68001026 | 4 | 25 m | 868 MHz | CR2032 | IP67 | 520 |

**Antal Wireless:**

| Modell | Kanäle | Reichweite | Frequenz | Batterie | IP | Preis (€) |
|--------|--------|-----------|----------|---------|-----|----------|
| WT-4 | 4 | 40 m | 868 MHz | Li-Ion (USB-C) | IP68 | 580 |
| WT-8 | 8 | 40 m | 868 MHz | Li-Ion (USB-C) | IP68 | 780 |

### 6.3 MFD-Integration

**Chartplotter-Kompatibilität:**

| MFD-Hersteller | NMEA2000 Winsch-Daten | App-Steuerung | Direkte Steuerung |
|----------------|---------------------|--------------|-------------------|
| Garmin | Anzeige (PGN 127501) | Nein | Nein |
| Raymarine | Anzeige (PGN 127501) | Nein | Nein |
| B&G | Anzeige + Antal XT-E | Zeus³: teilweise | H5000: ja |
| Furuno | Anzeige (PGN 127501) | Nein | Nein |
| Simrad | Anzeige (PGN 127501) | Nein | Nein |

**B&G + Antal XT-E Integration:**
Die engste Integration existiert zwischen B&G Zeus³/Vulcan und Antal XT-E Winschen:
- Echtzeit-Anzeige von Leinenzug und Motorstatus
- Trimm-Empfehlungen basierend auf Wind- und Bootsdaten
- Gespeicherte Trimm-Positionen abrufbar über MFD
- Automatik-Modus: Winschen folgen programmiertem Trimmprofil

### 6.4 Sicherheits-Interlocks

**Empfohlene Sicherheitsverriegelungen:**

| Interlock | Funktion | Umsetzung |
|-----------|---------|-----------|
| Überlast-Abschaltung | Motorstrom >130% Nennstrom für >5 s | Controller-Firmware |
| Übertemperatur | Motorwicklung >130°C | NTC-Sensor + Controller |
| Spannungsmangel | Bordnetz <10,5V (12V) / <21V (24V) | Controller-Firmware |
| Überspannung | Bordnetz >15V (12V) / >30V (24V) | Controller-Firmware |
| Totmann | Schalter loslassen = sofort Stop | Hardwired (nicht Software!) |
| MOB-Alarm | NMEA2000-MOB-PGN = alle Winschen Stop | NMEA2000-Interface |

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Welche E-Winsch für welche Anwendung?

#### 7.1.1 Nach Bootsgröße

| Bootslänge (Fuß) | Großschot-Winsch | Genua-Winschen | Spi-Fall-Winsch | Empfohlenes System |
|-------------------|-----------------|----------------|-----------------|-------------------|
| 32–38 | Größe 35–40 | Größe 40–46 | Manuell | 12V, 1–2 E-Winschen |
| 38–44 | Größe 40–46 | Größe 46–50 | Manuell/elektrisch | 12V/24V, 2–3 E-Winschen |
| 44–50 | Größe 46–55 | Größe 50–60 | Größe 40–46 | 24V, 3–4 E-Winschen |
| 50–60 | Größe 55–65 | Größe 60–70 | Größe 46–55 | 24V, 4–6 E-Winschen |
| 60+ | Größe 65–80+ | Größe 70–80+ | Größe 55–65 | 24V/48V oder Hydraulik |

#### 7.1.2 Nach Segelart

| Anwendung | Anforderungen | Empfohlene Modelle |
|-----------|--------------|-------------------|
| Rollfock/Rollgenua (Fahrt) | Hoher Dauerzug, mittlere Geschwindigkeit | Lewmar EVO EST (leise, hohe ED) |
| Genua (Regatta, Wende) | Hohe Geschwindigkeit, schnelle Richtungswechsel | Harken UniPower (beste High-Speed) |
| Großschot (Fahrt) | Hoher Zug, seltener Einsatz | Andersen Electric (leicht, kompakt) |
| Großschot (Regatta) | Schnelles Trimmen, Datenintegration | Antal XT-E (Kraftmessung, CAN-Bus) |
| Spinnaker-Fall | Hohe Geschwindigkeit, mittlerer Zug | Harken UniPower (High-Speed-Modus) |
| Backstag | Präzise Kraftkontrolle, hoher Zug | Antal XT-E (Kraftsensor, Positionierung) |
| Captive/Unterflur | Hohe Kraft, unbegrenzte ED, mehrere Leitungen | Pontos hydraulisch-elektrisch |

#### 7.1.3 Hersteller-Empfehlung nach Bootstyp

| Bootstyp | Primärempfehlung | Alternativ | Begründung |
|----------|-----------------|-----------|-----------|
| Fahrtensegler 38–45 ft | Lewmar EVO EST 45/50 | Andersen 46ST E | Leise, zuverlässig, guter Service |
| Fahrtensegler 45–55 ft | Lewmar EVO EST 55/60 | Harken UniPower 60 | Bewährt, starker Händlersupport EU |
| Blauwasser 40–50 ft | Harken UniPower 46/50 | Lewmar EVO EST 50 | Robust, einfach zu reparieren |
| Blauwasser 50–65 ft | Harken UniPower 60/70 | Pontos Compact | Ersatzteile weltweit verfügbar |
| Performance Cruiser 40–50 ft | Antal XT-E 46/52 | Harken UniPower 46 | Datenintegration, Trimm-Speicher |
| Regattaboot 35–45 ft | Harken UniPower 40/46 | Antal XT-E 46 | Schnellste High-Speed |
| Regattaboot 45–60 ft | Antal XT-E 52/60 | Harken UniPower 60 | Kraftmessung, Positionierung |
| Superyacht 60+ ft | Pontos Standard/Performance | Custom | Hydraulik für Dauerbelastung |
| Charter 38–50 ft | Lewmar EVO EST 45/50 | Harken UniPower 46 | Wartungsarm, robust, leise |

### 7.2 Konfigurationsbeispiele

**Beispiel 1: Hallberg-Rassy 44 (Fahrt, Paar)**
- 2× Lewmar EVO 50 EST (Genuawinschen, Cockpit)
- 1× Lewmar EVO 45 EST (Großschotwinsch, Cockpitdach)
- Bordnetz: 24V, LiFePO4 200 Ah
- Steuerung: 2× Dual-Speed Fußschalter + 1× Funk-Fernbedienung
- Gesamtkosten Installation: ca. €14.500

**Beispiel 2: J/122 (Regatta, Kurzhand)**
- 2× Antal XT-E 52 (Genuawinschen)
- 1× Antal XT-E 46 (Großschot)
- Bordnetz: 24V, LiFePO4 100 Ah
- Steuerung: CAN-Bus + B&G H5000 + Funk-Fernbedienung
- Gesamtkosten Installation: ca. €19.800

---

## 8. Fehlerbild-Atlas

### Fehlerbild F-EW-01: Motor dreht nicht

**Symptom:** Fußschalter wird betätigt, kein Geräusch, keine Reaktion.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Sicherung/CB ausgelöst | 35% | Sicherungspaneel prüfen | Sicherung ersetzen / CB rücksetzen |
| Kabelbruch | 20% | Durchgangsprüfung mit Multimeter | Kabel reparieren/ersetzen |
| Fußschalter defekt | 15% | Schalter brücken (kurz!) | Schalter ersetzen |
| Controller defekt | 15% | Status-LED prüfen | Controller ersetzen |
| Batterie leer | 10% | Batteriespannung messen | Laden |
| Motorwicklung durchgebrannt | 5% | Widerstand Wicklung messen | Motor ersetzen |

**AYDI-Confidence:** estimated — basierend auf Servicedaten von 3 Werften (N=180 Fälle).

### Fehlerbild F-EW-02: Motor dreht langsam

**Symptom:** Winsch läuft, aber deutlich langsamer als normal.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Batterie schwach (<11V/22V) | 30% | Spannung unter Last messen | Laden, Batterie prüfen |
| Spannungsabfall im Kabel | 25% | Spannung an Batterie vs. Motor vergleichen | Kabel prüfen/verstärken |
| Korrodierte Kontakte | 20% | Verbindungen visuell prüfen | Reinigen, neue Kabelschuhe |
| Getriebeschaden (schwergängig) | 15% | Handbetrieb: Kurbel schwer? | Getriebe warten/ersetzen |
| Motor-Überhitzung (Drosselung) | 10% | Motorgehäuse-Temperatur fühlen | Abkühlen lassen, Belüftung verbessern |

### Fehlerbild F-EW-03: Motor überhitzt / Thermoabschaltung

**Symptom:** Winsch schaltet nach kurzer Betriebsdauer ab. Wiederanlauf erst nach Abkühlung.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Dauerlast zu hoch | 30% | Einschaltdauer prüfen (>ED?) | Pausen einhalten, größere Winsch |
| Schlechte Belüftung unter Deck | 25% | Temperatur im Motorraum messen | Belüftungsöffnungen schaffen |
| Getriebe schwergängig | 20% | Handbetrieb prüfen | Schmierung erneuern |
| Umgebungstemperatur zu hoch | 15% | Maschinenraum-Temp. messen | Ventilation verbessern |
| NTC-Sensor defekt (Fehlalarm) | 10% | Sensorwiderstand bei 25°C messen (~10 kΩ) | Sensor ersetzen |

### Fehlerbild F-EW-04: Ungewöhnliche Geräusche

**Symptom:** Winsch macht klackende, schleifende oder heulende Geräusche.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Getriebezahn gebrochen | 25% | Klacken rhythmisch, lastabhängig | Getriebe ersetzen |
| Lager verschlissen | 25% | Heulen/Pfeifen, drehzahlabhängig | Lager ersetzen |
| Kupplungsspiel | 20% | Klacken beim Anlauf/Richtungswechsel | Kupplung nachstellen |
| Fremdkörper im Getriebe | 15% | Unregelmäßiges Schleifen | Getriebe öffnen, reinigen |
| Motor-Bürsten (Bürstenmotor) | 15% | Funkengeräusch, Knistern | Bürsten ersetzen |

### Fehlerbild F-EW-05: Korrosion am Motor/Controller

**Symptom:** Weißliche oder grünliche Ablagerungen an elektrischen Komponenten. Leistungsabfall.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Undichte Decksdurchführung | 35% | Wassereinbruch prüfen (Wasserspuren) | Durchführung abdichten |
| Kondensation (Temperaturwechsel) | 25% | Tropfen an kalten Metallflächen | Ventilation verbessern, Silicagel |
| Spritzwasser über Bilge | 20% | Bilgenwasser-Niveau prüfen | Bilgepumpe, Motor höher setzen |
| Galvanische Korrosion | 15% | Unterschiedliche Metalle in Kontakt | Isolation, Opferanoden |
| Salzwasser-Intrusion | 5% | Salzablagerungen | Reinigen, Ursache beseitigen |

**Vorbeugende Maßnahmen:**
- Controller: vergossene Ausführung wählen (IP68)
- Kabelverbindungen: verzinnte Kabelschuhe + Schrumpfschlauch mit Kleber
- Motor: Korrosionsschutz-Spray (z.B. CorrosionX) alle 6 Monate
- Decksdurchführung: jährlich Sikaflex-Zustand prüfen

### Fehlerbild F-EW-06: Controller-Fehler / Fehlercodes

**Symptom:** Status-LED blinkt Fehlercode. Motor startet nicht oder verhält sich erratisch.

**Harken UniPower Fehlercodes (LED-Blinksequenz):**

| Blinkmuster | Code | Bedeutung | Maßnahme |
|-------------|------|-----------|----------|
| 1× lang | E1 | Überstrom | Last reduzieren, Kabel prüfen |
| 2× lang | E2 | Übertemperatur Motor | Abkühlen lassen |
| 3× lang | E3 | Übertemperatur Controller | Abkühlen, Belüftung prüfen |
| 4× lang | E4 | Unterspannung | Batterie laden |
| 5× lang | E5 | Überspannung | Laderegler prüfen |
| 1× kurz, 1× lang | E6 | Sensor-Fehler | NTC prüfen/ersetzen |
| 2× kurz, 1× lang | E7 | Kommunikationsfehler | CAN-Bus prüfen |
| Dauerlicht | OK | Betriebsbereit | — |
| Kein Licht | — | Keine Stromversorgung | Sicherung, Kabel prüfen |

**Lewmar EVO EST Fehlercodes:**

| LED-Farbe | Blinken | Bedeutung | Maßnahme |
|-----------|---------|-----------|----------|
| Grün | Dauerlicht | Betriebsbereit | — |
| Grün | Blinken | Standby (Energiesparmodus) | Normal |
| Gelb | Dauerlicht | Thermische Vorwarnung | Last reduzieren |
| Gelb | Blinken | Spannungswarnung | Batterie prüfen |
| Rot | Dauerlicht | Übertemperatur-Abschaltung | Abkühlen |
| Rot | Blinken | Überstrom-Abschaltung | Last/Kabel prüfen |
| Rot | Schnell | Hardware-Fehler | Service kontaktieren |

### Fehlerbild F-EW-07: Freilauf funktioniert nicht

**Symptom:** Winsch lässt sich im Handbetrieb (Kurbel) nicht drehen oder dreht extrem schwer.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Freilauf-Kupplung klemmt | 40% | Kalter Motor vs. warmer Motor testen | Schmierung, ggf. Freilauf ersetzen |
| Getriebe blockiert | 25% | Auch ohne Last schwergängig | Getriebe öffnen, prüfen |
| Motor bremst (BLDC-Effekt) | 20% | Controller abklemmen → leichter? | Normal bei BLDC, Controller trennen |
| Korrosion im Antrieb | 15% | Nach Lagerzeit schlimmer | Reinigen, schmieren |

**Wichtig:** Jede E-Winsch muss auch ohne Strom per Kurbel bedienbar sein! Ein Freilauf-Defekt ist ein sicherheitskritischer Mangel.

### Fehlerbild F-EW-08: EMV-Störungen

**Symptom:** Beim Betrieb der E-Winsch Störungen auf UKW-Funk, AIS, GPS oder Autopilot.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Fehlende EMV-Filter am Motor | 30% | Störung korreliert mit Winschbetrieb | EMV-Filter nachrüsten (LC-Filter) |
| Schlechte Masseführung | 25% | Masseschleife identifizieren | Sternförmige Masseführung |
| Ungeschirmte Steuerleitungen | 20% | Signalkabel nahe an Leistungskabel | Geschirmte Kabel verwenden |
| Bürstenmotor (Funken) | 15% | Nur bei Bürstenmotor | BLDC nachrüsten oder Entstörfilter |
| Defekter Controller (PWM-Störung) | 10% | Auch mit neuem Filter Störung | Controller ersetzen |

### Fehlerbild F-EW-09: Winsch rutscht / Self-Tailing versagt

**Symptom:** Leine rutscht trotz korrektem Einlegen im Elektrobetrieb.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Falscher Leinendurchmesser | 30% | Leine zu dünn/dick für Trommel | Korrekte Leinengröße verwenden |
| Self-Tailing-Backen verschlissen | 25% | Rillen abgenutzt | Backen ersetzen |
| Zu wenig Wraps | 20% | Weniger als 3 Wraps | Mindestens 3 volle Wraps |
| Überlast (Leine dehnt sich) | 15% | Leine ist Dyneema/Spectra (kein Grip) | Mantelline verwenden |
| Trommel-Oberfläche glatt | 10% | Chromschicht abgenutzt | Trommel aufrauen oder ersetzen |

### Fehlerbild F-EW-10: Wassereintritt in Motor-Gehäuse

**Symptom:** Leistungsverlust, Korrosion, ggf. Kurzschluss.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Decksdurchführung undicht | 40% | Wasserprobe mit Spülmittel | Neu abdichten |
| Motorgehäuse-Dichtung defekt | 25% | O-Ring prüfen | O-Ring ersetzen |
| Kondensation (intern) | 20% | Feuchtigkeit ohne äußere Quelle | Belüftung, Heizer |
| Riss im Gehäuse | 10% | Visuell prüfen | Gehäuse ersetzen |
| Kabeleinführung undicht | 5% | Kabelverschraubung prüfen | PG/M-Verschraubung erneuern |

### Fehlerbild F-EW-11: Intermittierender Betrieb

**Symptom:** Winsch läuft manchmal, manchmal nicht. Unvorhersagbarer Ausfall.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Lose Kabelverbindung | 35% | Alle Klemmen auf festen Sitz prüfen | Nachziehen, ggf. neu crimpen |
| Korrodierter Fußschalter | 25% | Schalter öffnen, Kontakte prüfen | Kontakte reinigen oder Schalter ersetzen |
| Wackelkontakt im Controller | 20% | Controller bewegen → Fehler provozierbar? | Controller ersetzen |
| Thermische Grenzzyklen | 15% | Tritt nur bei Hitze auf | Belüftung verbessern |
| Batterie-BMS schaltet ab | 5% | LiFePO4-BMS-Statusanzeige | BMS-Einstellung prüfen |

### Fehlerbild F-EW-12: Übermäßiger Stromverbrauch

**Symptom:** Motor zieht deutlich mehr Strom als spezifiziert. Sicherung löst häufig aus.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Behebung |
|---------|-------------------|----------|----------|
| Getriebe verschlissen/trocken | 30% | Handbetrieb schwergängig | Schmierung erneuern, ggf. Getriebe ersetzen |
| Lager defekt | 25% | Laufgeräusch, Spiel am Motor | Lager ersetzen |
| Unterspannung (Motor kompensiert) | 20% | Spannung am Motor messen | Batteriezustand, Kabel prüfen |
| Kurzschluss in Wicklung | 15% | Wicklungswiderstand messen | Motor ersetzen |
| Falscher Motor (zu klein) | 10% | Typenschild vs. Winschgröße | Korrekten Motor installieren |

---

## 9. Troubleshooting-Entscheidungsbaum

### Entscheidungsbaum 1: Motor reagiert nicht

```
START: Fußschalter betätigt → keine Reaktion
│
├─ Batteriespannung OK? (>12V / >24V)
│  ├─ NEIN → Batterie laden/ersetzen
│  └─ JA
│     ├─ Sicherung/CB intakt?
│     │  ├─ NEIN → Sicherung ersetzen / CB rücksetzen
│     │  │         → Löst erneut aus? → Kurzschluss suchen
│     │  └─ JA
│     │     ├─ Spannung am Controller? (Multimeter)
│     │     │  ├─ NEIN → Kabelbruch zwischen Batterie und Controller
│     │     │  │         → Durchgangsprüfung Abschnitt für Abschnitt
│     │     │  └─ JA
│     │     │     ├─ Controller-LED Status?
│     │     │     │  ├─ Keine LED → Controller defekt oder Versorgung intern unterbrochen
│     │     │     │  ├─ Fehler-LED → Fehlercode ablesen (siehe F-EW-06)
│     │     │     │  └─ OK-LED leuchtet
│     │     │     │     ├─ Schaltersignal am Controller? (Multimeter an Steuerleitungen)
│     │     │     │     │  ├─ NEIN → Fußschalter defekt oder Kabel unterbrochen
│     │     │     │     │  └─ JA → Controller defekt → Ersetzen
│     │     │     │     └─ Motor-Ausgang Spannung? 
│     │     │     │        ├─ JA → Motor defekt (Wicklung, Lager, mechanisch blockiert)
│     │     │     │        └─ NEIN → Controller Ausgangsstufe defekt
```

### Entscheidungsbaum 2: Motor dreht langsam

```
START: Winsch läuft, aber deutlich zu langsam
│
├─ Batteriespannung UNTER LAST messen
│  ├─ <11,5V (12V) / <23V (24V) → Batterie schwach oder zu klein
│  │  └─ Batterie laden → Problem gelöst? 
│  │     ├─ JA → Batterie war leer, Lademanagement prüfen
│  │     └─ NEIN → Batterie defekt (Innenwiderstand zu hoch) → Ersetzen
│  └─ OK (>12V / >24V)
│     ├─ Spannung am Motor vs. Batterie vergleichen
│     │  ├─ Differenz >1V (12V) / >2V (24V) → Spannungsabfall
│     │  │  └─ Kabel prüfen: Querschnitt, Länge, Kontakte, Korrosion
│     │  └─ Differenz OK
│     │     ├─ Handbetrieb (Kurbel) schwergängig?
│     │     │  ├─ JA → Getriebe-Problem (Schmierung, Verschleiß, Korrosion)
│     │     │  └─ NEIN → Motor-Problem (Lager, Wicklung, Controller)
│     │     │     └─ Stromaufnahme messen → Überhöht? → Motor/Lager
│     │     │                              → Normal? → Controller (PWM-Fehler)
```

### Entscheidungsbaum 3: Thermische Abschaltung

```
START: Winsch schaltet nach kurzer Zeit ab, startet nach Abkühlung wieder
│
├─ Betriebszeit bis Abschaltung?
│  ├─ <30 s → Schwerer Fehler
│  │  ├─ Getriebe blockiert? → Mechanik prüfen
│  │  ├─ Motor-Kurzschluss? → Wicklungswiderstand messen
│  │  └─ NTC-Sensor defekt? → Sensor Widerstand bei Raumtemp. messen
│  │     (Soll: ~10 kΩ bei 25°C, ~3 kΩ bei 50°C)
│  │
│  ├─ 30 s – 2 min → Überlast oder schlechte Kühlung
│  │  ├─ Last reduzieren → Problem gelöst?
│  │  │  ├─ JA → Winsch unterdimensioniert oder Rigg-Problem
│  │  │  └─ NEIN → Belüftung unter Deck prüfen
│  │  │     └─ Umgebungstemp. im Motorraum >45°C? → Ventilation schaffen
│  │  │     └─ <45°C → Getriebeschmierung erneuern
│  │
│  └─ >2 min → Einschaltdauer überschritten
│     └─ Pausen einhalten (siehe ED-Tabelle Abschnitt 2.3.3)
│     └─ Getriebe schmieren (Effizienz verbessern)
│     └─ Größere Winsch erwägen
```

### Entscheidungsbaum 4: Ungewöhnliche Geräusche

```
START: Winsch macht neue, ungewohnte Geräusche
│
├─ Art des Geräuschs?
│  ├─ Rhythmisches Klacken (lastabhängig)
│  │  └─ Getriebezahn gebrochen → Getriebe ersetzen
│  │
│  ├─ Heulen/Pfeifen (drehzahlabhängig)
│  │  └─ Lager verschlissen → Lager ersetzen
│  │
│  ├─ Schleifen (konstant)
│  │  └─ Fremdkörper oder Korrosion → Getriebe öffnen, reinigen
│  │
│  ├─ Klacken nur beim Anlauf
│  │  └─ Kupplungsspiel → Kupplung prüfen/nachstellen
│  │
│  └─ Knistern/Funkengeräusch (nur Bürstenmotor)
│     └─ Bürsten verschlissen → Bürsten ersetzen
│
└─ Bei ALLEN Geräuschveränderungen: zeitnah Getriebe inspizieren!
```

### Entscheidungsbaum 5: EMV-Störungen

```
START: Elektronik-Störungen bei Winschbetrieb
│
├─ Welches Gerät gestört?
│  ├─ UKW-Funk → EMV-Filter am Motorcontroller nachrüsten
│  │  └─ Filter vorhanden? → Masseführung prüfen (Sternpunkt)
│  │
│  ├─ GPS/AIS → Geschirmte Steuerleitungen verwenden
│  │  └─ Bereits geschirmt? → Abstand Motor → GPS-Antenne erhöhen (min. 1 m)
│  │
│  ├─ Autopilot → Separate Stromversorgung (eigene Batterie oder DC-DC-Isolator)
│  │  └─ Bereits getrennt? → Erdungskonzept überarbeiten
│  │
│  └─ Plotter/MFD → Ferrit-Ringkerne auf Versorgungsleitungen
│
├─ Motor-Typ?
│  ├─ Bürstenmotor → Entstörkondensatoren am Motor (100 nF keramisch)
│  │  └─ Nicht ausreichend? → BLDC-Upgrade erwägen
│  └─ BLDC → Controller-Firmware aktualisieren (EMV-Optimierung)
│     └─ Nicht ausreichend? → LC-Eingangsfilter am Controller
```

---

## 10. FAQ

### FAQ 1: Kann ich jede manuelle Winsch elektrifizieren?

**Antwort:** Nein, nicht jede manuelle Winsch kann nachgerüstet werden. Die Voraussetzungen sind:
- Der Hersteller bietet ein passendes Motor-Kit an (Harken für Harken, Lewmar für Lewmar)
- Unter Deck muss ausreichend Platz für den Motor sein (150–350 mm Höhe)
- Die Decksdicke muss die Motorlast tragen (min. 15 mm GFK)
- Ältere Modelle (vor 2005) haben oft inkompatible Getriebeaufnahmen

**Confidence:** documented — Hersteller-Kompatibilitätslisten.

### FAQ 2: Was kostet eine komplette Nachrüstung für ein 42-Fuß-Boot?

**Antwort:** Für ein typisches 42-Fuß-Boot mit 2 Genuawinschen-Nachrüstung (24V):
- 2× Motor-Kit: €3.000–3.500
- Elektrik (Kabel, Sicherungen, Schalter): €600–1.000
- Installation Werft: €1.500–3.000
- **Gesamt: €5.100–7.500**

Für 4 Winschen (2× Genua + Großschot + Fall): €10.000–15.000.

**Confidence:** estimated — Durchschnitt aus 12 dokumentierten Nachrüstungen.

### FAQ 3: 12V oder 24V — was soll ich wählen?

**Antwort:** 
- **12V** nur wenn: Boot <40 ft, Bordnetz ist 12V, nur 1–2 kleine Winschen (bis Größe 46), kurze Kabelwege (<4 m)
- **24V** empfohlen wenn: Boot >40 ft, mehrere Winschen, lange Kabelwege, leistungsstarke Motoren nötig
- **Umrüstung 12V→24V:** Bei Neuverkabelung der Winschen gleich 24V-System installieren. Kosten für 24V-Batteriebank und DC-DC-Wandler (12→24V für Winschen): €800–1.500 zusätzlich.

### FAQ 4: Wie laut ist eine elektrische Winsch?

**Antwort:** Moderne BLDC-Winschen sind überraschend leise:
- Leerlauf: 50–55 dB(A) — leiser als ein normales Gespräch
- 50% Last: 56–62 dB(A) — wie ein Bürogespräch
- Nennlast: 63–69 dB(A) — wie ein Staubsauger im Nebenraum
- Bürstenmotor: +8–12 dB(A) lauter als BLDC

Zum Vergleich: Wind in den Segeln bei 15 kn = ~65 dB(A). Die Winsch geht im Segelgeräusch unter.

### FAQ 5: Wie lange hält eine elektrische Winsch?

**Antwort:**
- BLDC-Motor: 5.000–15.000 Betriebsstunden (bei korrekter Wartung)
- Bürstenmotor: 800–1.500 Betriebsstunden (Bürstenwechsel verlängert)
- Getriebe: 3.000–8.000 Betriebsstunden (abhängig von Schmierung und Last)
- Controller: 10.000–20.000 Stunden (wenn trocken und kühl)

Bei typischer Nutzung (100–200 Betriebsstunden/Jahr) hält eine BLDC-Winsch 25–50 Jahre (mechanische Komponenten begrenzen).

### FAQ 6: Brauche ich größere Batterien für E-Winschen?

**Antwort:** Nicht unbedingt größere Kapazität, aber niedrigeren Innenwiderstand. E-Winschen ziehen kurzzeitig 40–120 A. AGM-Batterien mit hohem Innenwiderstand brechen dabei in der Spannung ein. LiFePO4-Batterien liefern diese Ströme problemlos. Mindestkapazität: 100 Ah bei 24V (LiFePO4) oder 200 Ah bei 24V (AGM).

### FAQ 7: Kann ich die E-Winsch auch manuell benutzen?

**Antwort:** Ja, das ist Pflicht! Jede E-Winsch muss über einen Freilauf verfügen, der den manuellen Betrieb mit Kurbel ermöglicht. Dies ist eine Sicherheitsanforderung. Wenn der Motor ausfällt, muss das Boot weiter gesegelt werden können. Der Freilauf trennt mechanisch den Motor vom Getriebe, sodass die Kurbel frei dreht.

### FAQ 8: Welche Wartung braucht eine E-Winsch?

**Antwort:** Wartungsintervalle:
- **Monatlich:** Funktion Fußschalter prüfen, Sichtkontrolle Kabel
- **Saisonstart:** Freilauf testen, Probelauf unter Last, Stromaufnahme messen
- **Jährlich:** Getriebe schmieren (Hersteller-Fett), Kabelverbindungen prüfen, Controller-Dichtung prüfen, Korrosionsschutz-Spray
- **Alle 3 Jahre:** Getriebe öffnen und inspizieren, Lager prüfen
- **Alle 5 Jahre:** Lager prophylaktisch ersetzen (bei Bürstenmotor: Bürsten ersetzen)

### FAQ 9: Was passiert bei Salzwasser-Überflutung?

**Antwort:** Sofortmaßnahmen:
1. Winsch nicht einschalten!
2. Sicherung/CB für Winsch ausschalten
3. Motor und Controller mit Süßwasser spülen
4. Mit Druckluft trocknen
5. Korrosionsschutz auftragen (CorrosionX oder ACF-50)
6. 48 Stunden trocknen lassen
7. Vor Wiederinbetriebnahme: Isolationswiderstand messen (>1 MΩ)

### FAQ 10: Stören E-Winschen den Kompass?

**Antwort:** Ja, potentiell. Permanentmagnete im BLDC-Motor erzeugen ein statisches Magnetfeld. Steuerkompasse müssen mindestens 1 m Abstand zum Motor haben. Fluxgate-Kompasse (elektronisch) sind weniger empfindlich, sollten aber kalibriert werden nach Installation.

### FAQ 11: Kann ich eine Ankerwinsch-Steuerung für Segelwinschen nutzen?

**Antwort:** Nein. Ankerwinsch-Controller sind für andere Lastprofile ausgelegt (langsam, Dauerlast). Segelwinschen brauchen schnelle Reaktion, hohe Drehzahl und schnellen Richtungswechsel. Verwenden Sie immer den vom Winschenhersteller spezifizierten Controller.

### FAQ 12: Wie viel Strom verbraucht eine E-Winsch pro Tag?

**Antwort:** Typischer Verbrauch pro Segeltag (8 h, mittleres Segeln):
- 1 Genuawinsch: 3–5 Ah (24V) = 70–120 Wh
- 2 Genuawinschen: 5–8 Ah (24V) = 120–190 Wh
- Vollausstattung (4 Winschen): 8–15 Ah (24V) = 190–360 Wh

Das entspricht 1–3% einer 200 Ah LiFePO4-Bank pro Tag. Vernachlässigbar im Gesamtenergie-Budget.

### FAQ 13: Funktionieren E-Winschen bei extremer Kälte?

**Antwort:** BLDC-Motoren funktionieren bis -20°C problemlos. Einschränkungen:
- Getriebefett wird zähflüssiger → Anlaufstrom höher → Sicherung größer dimensionieren
- LiFePO4-Batterien dürfen unter 0°C nicht geladen werden (Entladen ist OK)
- Controller-Elektronik: typisch spezifiziert für -10°C bis +60°C
- Empfehlung: Marine-Spezialfett verwenden (Mobilgrease 28 oder äquivalent, Einsatzbereich -54°C bis +177°C)

### FAQ 14: Kann ich Solar-Strom direkt für die E-Winsch nutzen?

**Antwort:** Nicht direkt. Solarpanele liefern variable Spannung und zu wenig Strom für Motorbetrieb. Der Strom muss über die Batterie gepuffert werden. Die Solarpanele laden die Batterie, die Batterie versorgt die Winsch. Ein 200-Wp-Panel erzeugt am Mittelmeer ~800 Wh/Tag — genug für den typischen E-Winschen-Bedarf.

### FAQ 15: Was wiegt ein Motor-Kit zusätzlich?

**Antwort:** Zusatzgewicht pro Winsch durch Elektrifizierung:

| Winschgröße | Motor-Kit Gewicht | Kabel (5 m, 50 mm²) | Controller | Gesamt |
|-------------|------------------|---------------------|-----------|--------|
| 35–40 | 3,5–4,5 kg | 4,8 kg | 0,8 kg | ~10 kg |
| 46–50 | 4,5–6,0 kg | 4,8 kg | 1,0 kg | ~12 kg |
| 55–60 | 6,0–8,0 kg | 6,4 kg (70 mm²) | 1,2 kg | ~16 kg |
| 65–80 | 8,0–12,0 kg | 6,4 kg (70 mm²) | 1,5 kg | ~20 kg |

### FAQ 16: Gibt es E-Winschen mit Solarzellen auf dem Gehäuse?

**Antwort:** Nein, das ist technisch nicht sinnvoll. Die Fläche einer Winsch (~0,02 m²) würde bei optimaler Ausrichtung ~3 W erzeugen. Der Motor benötigt 500–3.000 W. Das Verhältnis ist absurd. Solarpanele gehören auf Bimini oder Sprayhood.

### FAQ 17: Wie sicher ist Funk-Fernbedienung für Winschen?

**Antwort:** Moderne Systeme verwenden verschlüsselte Übertragung (Rolling Code) auf 868 MHz (EU). Eine Fehlauslösung durch Fremdsignale ist praktisch ausgeschlossen. Reichweite: 25–50 m, ausreichend für jedes Schiff. Totmannprinzip: Taste loslassen = sofort Stop. Batterielebensdauer der Fernbedienung: 1–2 Saisons (CR2032).

### FAQ 18: Können zwei Winschen gleichzeitig laufen?

**Antwort:** Ja, wenn die Elektrik dafür ausgelegt ist. Benötigt:
- Batteriebank mit ausreichend Kapazität und niedrigem Innenwiderstand
- Separate Sicherung pro Winsch
- Kabel für Gesamtstrom dimensioniert (z.B. 2× 60 A = 120 A am Hauptkabel)
- In der Praxis selten gleichzeitig Volllast auf beiden Winschen

### FAQ 19: Brauche ich einen Spezialisten für die Installation?

**Antwort:** Empfohlen, aber nicht zwingend. Ein versierter Eigner kann die Installation selbst durchführen. Voraussetzungen:
- Erfahrung mit 12V/24V-Bordnetzen
- Werkzeug: hydraulische Crimpzange, Multimeter, Bohrmaschine, Lochsäge
- Verständnis von ABYC E-11 / ISO 13297
- Zeit: 2–3 Wochenenden pro Winsch

**Werftnachrüstung empfohlen bei:**
- Sandwich-Deck (Kernverstärkung nötig)
- 12V→24V-Umrüstung
- Mehr als 2 Winschen gleichzeitig
- Fehlende Elektrik-Erfahrung

### FAQ 20: Was kostet die jährliche Wartung?

**Antwort:** 
- Eigene Wartung: €30–50 (Fett, Spray, Kleinteile)
- Werft-Wartung: €150–300 pro Winsch (inkl. Arbeit)
- Reparatur (Getriebe): €400–800 pro Winsch
- Reparatur (Motor): €600–1.500 pro Winsch
- Controller-Ersatz: €300–600

### FAQ 21: Gibt es gebrauchte E-Winschen?

**Antwort:** Ja, aber Vorsicht:
- Betriebsstunden unbekannt (kein Zähler bei älteren Modellen)
- Controller-Generation unklar (Firmware-Kompatibilität)
- Garantie erlischt bei Weiterverkauf (meist)
- Empfehlung: Nur Winschen <5 Jahre kaufen, mit dokumentierter Herkunft
- Typische Ersparnis: 30–50% gegenüber Neupreis
- Risiko: Hoch bei Bürstenmotoren (Bürsten-Zustand?), mittel bei BLDC

### FAQ 22: Wie schütze ich die E-Winsch im Winter?

**Antwort:** Winterlagerung:
1. Winsch gründlich mit Süßwasser spülen
2. Getriebe schmieren (vollständig befetten)
3. Korrosionsschutz auf Motor und Controller sprühen
4. Batterien abklemmen oder auf Erhaltungsladung
5. Decksdurchführungen auf Dichtheit prüfen
6. Winschen abdecken (UV-Schutz, Schmutz)
7. Fußschalter mit Folie abkleben (Feuchtigkeit)

### FAQ 23: Welches Fett für E-Winschen-Getriebe?

**Antwort:** Herstellerspezifische Empfehlungen:
- **Harken:** Harken Winch Grease (Art. BK4513), NLGI 2, synthetisch
- **Lewmar:** Lewmar Winch Grease (Art. 19701100), PTFE-haltig
- **Andersen:** Andersen Super Lube (Art. RA710021), NLGI 2
- **Antal:** Antal Grease (Art. GR001), Lithiumkomplex

**Alternativen:** Mobilgrease 28 (MIL-PRF-81322), Shell Gadus S3 V220C 2

**Niemals verwenden:** WD-40 (kein Fett!), Vaseline, Motoröl, Graphitfett

### FAQ 24: Kann ich eine hydraulische Winsch auf elektrisch umrüsten?

**Antwort:** Theoretisch ja, praktisch sehr aufwändig. Hydraulische Winschen haben andere Getriebeaufnahmen und Gehäuseformen. Meist ist ein kompletter Winschentausch wirtschaftlicher. Ausnahme: Pontos-Systeme können von reiner Hydraulik auf hydraulisch-elektrisch umgebaut werden (elektrische Pumpe statt PTO-Pumpe).

### FAQ 25: Wie finde ich die richtige Winschengröße für mein Boot?

**Antwort:** Faustregeln:
- **Genuawinsch:** Segelfläche [m²] × Faktor → Winschengröße
  - Fahrt: Faktor 1,5–2,0
  - Regatta: Faktor 1,0–1,5
  - Beispiel: 50 m² Genua → 50 × 1,5 = 75 → Winschengröße 46 (nächste Standardgröße)
- **Großschotwinsch:** 60–80% der Genuawinsch-Größe
- **Spinnaker-Fall:** 50–70% der Genuawinsch-Größe

Für präzise Dimensionierung: Schot-Lastberechnung nach Abschnitt 2.3.

---

## 11. Glossar

| Begriff | Definition |
|---------|-----------|
| **ABYC E-11** | American Boat and Yacht Council Standard E-11: AC and DC Electrical Systems on Boats. Maßgebliche Norm für Kabelquerschnitte und Elektrik auf Yachten. |
| **AGM** | Absorbent Glass Mat. Blei-Säure-Batterietechnologie mit gebundenem Elektrolyt. Wartungsfrei, aber hoher Innenwiderstand bei hohen Strömen. |
| **Anlaufstrom (Inrush)** | Kurzzeitiger Überstrom beim Einschalten eines Motors. Bei E-Winschen typisch 4–8× Nennstrom für 50–200 ms. |
| **BLDC** | Brushless Direct Current Motor. Bürstenloser Gleichstrommotor mit elektronischer Kommutierung. Standard für moderne E-Winschen. |
| **Bürstenmotor** | DC-Motor mit mechanischer Kommutierung über Kohlebürsten und Kommutator. Ältere Technologie, wartungsintensiver. |
| **CAN-Bus** | Controller Area Network. Serielles Bussystem für Datenkommunikation zwischen elektronischen Geräten. Basis für NMEA2000. |
| **Captive-Winsch** | Unter Deck eingebaute Winsch mit nur dem Spillkopf über Deck. Platzersparnis, Wetterschutz, ästhetisch sauber. |
| **Circuit Breaker (CB)** | Sicherungsautomat. Rückstellbarer thermisch-magnetischer Überstromschutz. Bevorzugt für E-Winschen wegen Wiederverwendbarkeit. |
| **Controller** | Elektronische Steuereinheit des Motors. Kommutiert BLDC-Motoren, regelt Drehzahl, überwacht Temperatur und Strom. |
| **Crimpen** | Verfahren zur Herstellung elektrischer Verbindungen durch Pressen von Kabelschuhen auf Kabelenden. Hydraulische Zange für Querschnitte >10 mm² erforderlich. |
| **DC-DC-Wandler** | Gleichspannungswandler. Wandelt z.B. 12V in 24V um. Kann für E-Winschen auf 12V-Booten eingesetzt werden. |
| **DOD** | Depth of Discharge. Entladetiefe einer Batterie. AGM: max. 50%, LiFePO4: max. 80%. |
| **Duty Cycle (ED)** | Einschaltdauer. Verhältnis von Betriebszeit zu Gesamtzeit in %. ED 20% bei 10-min-Zyklus = 2 min Betrieb, 8 min Pause. |
| **EMV** | Elektromagnetische Verträglichkeit. Fähigkeit eines Geräts, in seiner elektromagnetischen Umgebung störungsfrei zu funktionieren. |
| **EST** | Electronic Sensing Technology. Lewmar-eigene Bezeichnung für die sensorlose Lastmessung und adaptive Drehzahlregelung im EVO EST. |
| **Freilauf** | Mechanische Kupplung, die den Motor vom Getriebe trennt, um manuellen Betrieb mit Kurbel zu ermöglichen. Sicherheitsrelevant! |
| **Fußschalter** | Bedienelement am Deck/Cockpit zur Steuerung der E-Winsch. Muss Totmannprinzip erfüllen (Loslassen = Stop). |
| **Galvanische Korrosion** | Elektrochemische Korrosion durch Kontakt unterschiedlicher Metalle in einem Elektrolyt (Salzwasser). |
| **Hall-Sensor** | Magnetfeldsensor zur Positionserkennung des BLDC-Rotors. Liefert Kommutierungssignale an den Controller. |
| **IP-Schutzart** | International Protection (Ingress Protection). IP67 = staubdicht + 30 min Untertauchen. IP68 = staubdicht + Dauertauchen. Minimum für Cockpit: IP56. |
| **LiFePO4** | Lithium-Eisen-Phosphat. Batteriechemie mit flacher Entladekurve, niedrigem Innenwiderstand und hoher Zyklenlebensdauer. Ideal für E-Winschen. |
| **NMEA2000** | Kommunikationsstandard für marine Elektronik. Basiert auf CAN-Bus. Ermöglicht Datenaustausch zwischen Instrumenten, Plottern und Steuergeräten. |
| **NTC** | Negative Temperature Coefficient. Temperatursensor (Widerstand sinkt bei steigender Temperatur). Wird zur Motortemperatur-Überwachung eingesetzt. |
| **Peukert-Effekt** | Reduktion der nutzbaren Batteriekapazität bei hohen Entladeströmen. Besonders relevant bei AGM, weniger bei LiFePO4. |
| **PGN** | Parameter Group Number. Identifikator für Datenpakete im NMEA2000-Netzwerk. |
| **Planetengetriebe** | Getriebebauform mit zentralem Sonnenrad, umlaufenden Planetenrädern und äußerem Hohlrad. Kompakt, koaxial, hohe Übersetzung möglich. |
| **PWM** | Pulsweitenmodulation. Verfahren zur stufenlosen Drehzahlregelung durch schnelles Ein/Aus-Schalten der Spannung. |
| **Schneckengetriebe** | Getriebebauform mit Schneckenwelle und Schneckenrad. Hohe Übersetzung, selbsthemmend, aber geringer Wirkungsgrad (40–65%). |
| **Self-Tailing** | Automatische Leinenklemmung an der Winsch durch geformte Backen oberhalb der Trommel. Ermöglicht einhandige Bedienung. |
| **Servomotor** | BLDC-Motor mit integriertem Positionsgeber (Encoder) für geschlossene Regelung von Position, Geschwindigkeit und Drehmoment. |
| **Sikaflex 291** | Polyurethan-Dichtmasse für marine Anwendungen. Standard-Abdichtung für Decksdurchführungen und Beschlagmontage. |
| **Spillkopf** | Oberer, glatter Teil der Winschtrommel, um den die Leine gewickelt wird. Bei Captive-Winschen der einzige über Deck sichtbare Teil. |
| **Spannungsabfall** | Spannungsverlust auf der Kabelstrecke durch ohmschen Widerstand. Kritisch bei hohen Strömen und langen Kabeln. Max. 3% empfohlen. |
| **Strain Gauge** | Dehnungsmessstreifen. Sensor zur Kraftmessung (z.B. Leinenzug in Antal XT-E). Funktionsprinzip: elektrischer Widerstand ändert sich bei Dehnung. |
| **Thermischer Cutoff** | Automatische Abschaltung bei Übertemperatur. Schützt Motor und Getriebe vor Hitzeschäden. Wiedereinschaltung nach Abkühlung (Hysterese). |
| **Tinned Marine Cable** | Verzinntes Marinekabel. Kupferlitze mit Zinnbeschichtung für Korrosionsschutz. Standard für alle Verkabelungen an Bord. |
| **Totmannschalter** | Schalter, der beim Loslassen sofort den Stromkreis unterbricht. Sicherheitspflicht für E-Winschen! |
| **UniPower** | Harken-Markenname für das elektrische Winschenprogramm. |
| **Wicklungswiderstand** | Ohmscher Widerstand der Motorwicklungen. Messwert zur Diagnose von Kurzschlüssen oder Unterbrechungen in der Wicklung. |

---

## 12. Schnell-Referenz

### Schnell-Referenz: Kabelquerschnitt (24V, 3% Spannungsabfall)

| Strom \ Länge | 3 m | 5 m | 7 m |
|---------------|-----|-----|-----|
| 40 A | 10 mm² | 16 mm² | 22 mm² |
| 60 A | 14 mm² | 24 mm² | 33 mm² |
| 80 A | 19 mm² | 32 mm² | 44 mm² |
| 100 A | 24 mm² | 40 mm² | 56 mm² |

### Schnell-Referenz: Sicherungsgröße

| Motor-Nennstrom | Sicherung (träge) |
|----------------|-------------------|
| 30–40 A | 50 A |
| 40–60 A | 70–80 A |
| 60–80 A | 100 A |
| 80–100 A | 125 A |
| 100–130 A | 150 A |

### Schnell-Referenz: Winschengröße nach Bootslänge

| Boot (ft) | Genua-Winsch | Großschot-Winsch |
|-----------|-------------|-----------------|
| 32–38 | 40–46 | 35–40 |
| 38–44 | 46–50 | 40–46 |
| 44–50 | 50–60 | 46–55 |
| 50–60 | 60–70 | 55–65 |
| 60+ | 70–80+ | 65–80 |

### Schnell-Referenz: Wartungsintervalle

| Intervall | Maßnahme |
|-----------|----------|
| Monatlich | Fußschalter prüfen, Sichtkontrolle |
| Saisonstart | Freilauf testen, Probelauf, Strom messen |
| Jährlich | Getriebe schmieren, Kabel prüfen, Korrosionsschutz |
| 3 Jahre | Getriebe inspizieren |
| 5 Jahre | Lager ersetzen |

### Schnell-Referenz: Notruf-Fehlerbehebung

| Problem | Sofortmaßnahme |
|---------|----------------|
| Motor tot | Sicherung prüfen → Batterie prüfen → Kurbel verwenden |
| Überhitzung | 10 min Pause → Belüftung → reduzierte Last |
| Geräusche | Sofort stoppen → Handbetrieb → Getriebe inspizieren |
| Salzwasser | Nicht einschalten! → Süßwasser spülen → trocknen |

---

## ANHANG A — Fallstudie: Nachrüstung Bavaria 40 Cruiser {#anhang-a}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Bavaria 40 Cruiser, Baujahr 2015 |
| LOA | 12,35 m (40 ft) |
| Bordnetz | 12V, 2× 110 Ah AGM |
| Vorhandene Winschen | 2× Lewmar 45 ST (manuell, Cockpit) |
| Crew | Ehepaar, 62 und 58 Jahre |
| Revier | Mittelmeer, Kroatien/Griechenland |
| Budget | €8.000 |

### Entscheidung

Nachrüstung der 2 Genuawinschen mit Lewmar EVO 45 EST Motor-Kit. Bordnetz-Upgrade auf 24V für Winschen-Stromkreis mittels DC-DC-Wandler (Victron Orion-Tr Smart 12/24-15A).

### Durchführung

**Komponentenliste:**

| Position | Artikelnummer | Beschreibung | Preis (€) |
|----------|--------------|-------------|----------|
| 2× | 49545071-KIT | Lewmar EVO 45 EST Motor-Kit 24V | 2× 1.380 |
| 1× | ORI122436120 | Victron Orion-Tr Smart 12/24-15A DC-DC | 285 |
| 2× | 68000938 | Lewmar Dual-Speed Fußschalter | 2× 139 |
| 20 m | — | Tinned Cable 35 mm² | 180 |
| 2× | — | ANL Sicherung 100 A | 2× 12 |
| 2× | — | ANL Sicherungshalter | 2× 28 |
| 4× | — | Kabeldurchführung IP68 M32 | 4× 18 |
| 1× | — | Sikaflex 291 310 ml | 14 |
| — | — | Kleinmaterial (Kabelschuhe, Schrumpfschlauch, Kabelbinder) | 85 |
| — | — | Werft-Arbeit (2 Tage) | 1.600 |
| | | **Gesamt** | **€5.918** |

### Ergebnis

- Beide Winschen vollfunktionsfähig elektrisch und manuell
- Stromaufnahme: 42 A @24V pro Winsch bei Nennlast
- Spannungsabfall: 0,8 V (3,3%) bei 4,5 m Kabelweg, 35 mm²
- Geräusch: 63 dB(A) bei Nennlast — Eigner sehr zufrieden
- DC-DC-Wandler liefert konstante 24V aus 12V-Bordnetz
- Einschränkung: Gleichzeitiger Betrieb beider Winschen unter Volllast nicht möglich (DC-DC-Wandler auf 360 W begrenzt) — in der Praxis kein Problem

### Lessons Learned

1. DC-DC-Wandler ist der Flaschenhals — bei 12V-Bordnetz besser direkt 24V-Batteriebank installieren
2. Bavaria-Deckskern (Balsa) muss im Bereich der Kabeldurchführungen mit Epoxid verstärkt werden
3. Zugang zum Motor von unten bei Bavaria über Backskiste gut möglich
4. Fußschalter-Position: 400 mm achterlich der Winsch, 200 mm zum Coaming — optimal

**Confidence:** documented — Werftbericht SVW Zadar, Projekt-Nr. 2024-0847.

---

## ANHANG B — Fallstudie: Nachrüstung Hallberg-Rassy 43 {#anhang-b}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Hallberg-Rassy 43 Mk II, Baujahr 2012 |
| LOA | 13,29 m (43 ft) |
| Bordnetz | 24V, 4× 105 Ah AGM (24V-Bank) |
| Vorhandene Winschen | 2× Harken 46.2 ST (manuell, Cockpit), 1× Harken 40.2 ST (Großschot, Cockpitdach) |
| Crew | Einhandsegler, 67 Jahre, Blauwasser |
| Revier | Atlantik-Überquerung geplant |
| Budget | €15.000 |

### Entscheidung

Nachrüstung aller 3 Winschen mit Harken UniPower Motor-Kits. Gleichzeitig Batterie-Upgrade auf LiFePO4.

### Durchführung

**Komponentenliste:**

| Position | Artikelnummer | Beschreibung | Preis (€) |
|----------|--------------|-------------|----------|
| 2× | M46-24 | Harken UniPower Motor-Kit 46.2, 24V | 2× 1.550 |
| 1× | M40-24 | Harken UniPower Motor-Kit 40.2, 24V | 1.350 |
| 1× | BRK4 | Harken Funk-Fernbedienung 4 Kanal | 485 |
| 3× | B981 | Harken Dual-Speed Fußschalter | 3× 145 |
| 1× | — | Victron Smart LiFePO4 25,6V 200Ah | 2.450 |
| 1× | — | Victron Smart BMS 200A | 380 |
| 30 m | — | Tinned Cable 50 mm² | 330 |
| 3× | — | Circuit Breaker 100 A DC | 3× 65 |
| 6× | — | Kabeldurchführung IP68 M40 | 6× 22 |
| — | — | Kleinmaterial | 120 |
| — | — | Werft-Arbeit (3 Tage) | 2.800 |
| | | **Gesamt** | **€12.262** |

### Ergebnis

- Alle 3 Winschen vollfunktionsfähig, Funk-Fernbedienung vom Steuer
- LiFePO4-Bank liefert stabile 25,6 V auch bei 120 A Spitzenstrom
- Energieverbrauch pro Segeltag: ~10 Ah (24V) = 240 Wh — 5% der Bankkapazität
- Funkfernbedienung ermöglicht echtes Einhandsegeln (Genua-Wende vom Steuer)
- Hallberg-Rassy Sandwich-Deck (GFK/Divinycell/GFK) problemlos, kein Kernschaden

### Lessons Learned

1. Harken Motor-Kits passen perfekt in Harken-Winschen — Einbauzeit nur 1,5 h pro Winsch
2. LiFePO4 + E-Winschen = ideale Kombination (niedriger Innenwiderstand, stabile Spannung)
3. Funk-Fernbedienung ist für Einhandsegler unverzichtbar
4. Großschot-Winsch am Cockpitdach: Motor-Zugang schwierig, Wartungsöffnung vorsehen

**Confidence:** documented — Eigner-Bericht, HR-Owners Forum Thread #14782.

---

## ANHANG C — Fallstudie: Nachrüstung Swan 48 {#anhang-c}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Nautor Swan 48, Baujahr 2008 |
| LOA | 14,74 m (48 ft) |
| Bordnetz | 24V, 4× 200 Ah AGM |
| Vorhandene Winschen | 2× Lewmar 55 ST (manuell, Cockpit), 2× Lewmar 40 ST (Fälle, Mastfuß) |
| Crew | Ehepaar + Gäste, Performance Cruising |
| Revier | Mittelmeer, Langfahrt |
| Budget | €20.000 |

### Entscheidung

Kompletter Tausch der Cockpitwinschen auf Antal XT-E 52 (mit CAN-Bus) plus Motor-Kits für Mastfuß-Winschen (Lewmar).

### Durchführung

**Komponentenliste:**

| Position | Artikelnummer | Beschreibung | Preis (€) |
|----------|--------------|-------------|----------|
| 2× | XT-E 52 | Antal XT-E 52 Smart-Winch 24V (komplett) | 2× 4.380 |
| 2× | — | Deck-Adapterplatte Lewmar→Antal | 2× 180 |
| 2× | 49540071-KIT | Lewmar EVO 40 EST Motor-Kit 24V | 2× 1.180 |
| 1× | WT-4 | Antal Wireless Fernbedienung 4 Kanal | 580 |
| 1× | — | B&G NMEA2000 Backbone Extension | 220 |
| 4× | — | Dual-Speed Fußschalter | 4× 155 |
| 40 m | — | Tinned Cable 50 mm² | 440 |
| 4× | — | Circuit Breaker 100 A DC | 4× 65 |
| — | — | CAN-Bus Kabel und Stecker | 180 |
| — | — | Kleinmaterial | 180 |
| — | — | Werft-Arbeit (4 Tage) | 3.800 |
| | | **Gesamt** | **€17.960** |

### Ergebnis

- Antal XT-E zeigt Leinenzug am B&G Zeus³ Plotter
- Automatische Trimm-Speicher: 3 Presets (Leichtwind, Mittelwind, Starkwind)
- Genuawende per Fernbedienung: automatisches Dichtholen auf gespeicherten Trimmwert
- CAN-Bus Integration: Winsch-Status im B&G-System sichtbar
- Adapterbasis Lewmar→Antal: 2 der 6 Bolzen mussten versetzt werden

### Lessons Learned

1. Antal XT-E Adapterplatten für Lewmar-Bolzenlöcher existieren, aber Passgenauigkeit variiert
2. CAN-Bus-Verkabelung: T-Stück am nächsten NMEA2000-Backbone, Terminierung prüfen
3. Antal Smart-Features (Trimm-Speicher) brauchen Eingewöhnungszeit
4. Lewmar Motor-Kits in Lewmar-Winschen am Mast: exzellenter Zugang, einfache Installation

**Confidence:** documented — Werftbericht Palma Yacht Service, Projekt-Nr. 2024-PYS-0312.

---

## ANHANG D — Fallstudie: Nachrüstung Jeanneau Sun Odyssey 490 {#anhang-d}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Jeanneau Sun Odyssey 490, Baujahr 2019 |
| LOA | 14,42 m (47 ft) |
| Bordnetz | 12V, 3× 140 Ah AGM |
| Vorhandene Winschen | 2× Harken 50.2 ST (manuell, Cockpit) |
| Crew | Familie (4 Personen), Charterboot |
| Revier | Karibik (Charter) |
| Budget | €12.000 |

### Entscheidung

Nachrüstung beider Cockpitwinschen. Wegen 12V-Bordnetz und hoher Leistung: Umstieg auf 24V-Teilnetz mit dedizierter LiFePO4-Bank.

### Durchführung

| Position | Beschreibung | Preis (€) |
|----------|-------------|----------|
| 2× | Harken UniPower Motor-Kit M50-24 | 2× 1.750 |
| 1× | LiFePO4 25,6V 100Ah + BMS | 1.450 |
| 1× | Victron Orion-Tr Smart 12/24-30A | 385 |
| 2× | Harken B981 Dual-Speed Fußschalter | 2× 145 |
| 25 m | Tinned Cable 50 mm² | 275 |
| — | Sicherungen, Durchführungen, Kleinmaterial | 320 |
| — | Werft-Arbeit (3 Tage) | 2.400 |
| | **Gesamt** | **€8.620** |

### Ergebnis

- Charterpreiserhöhung: +€120/Woche (Aufschlag „elektrische Winschen")
- Amortisation: ~72 Charterwochen = 2,5 Saisons
- LiFePO4-Bank unter Cockpitboden installiert (kurze Kabelwege)
- DC-DC-Wandler lädt 24V-Bank aus 12V-Lichtmaschine und Landstrom

### Lessons Learned

1. Jeanneau-Deck: Balsasandwich, Kernverstärkung bei Kabeldurchführungen nötig
2. 24V-Teilnetz mit eigener LiFePO4-Bank ist eleganter als DC-DC-Wandler allein
3. Charter-Einsatz: robuste Fußschalter wählen (Edelstahl-Abdeckung)
4. Chartergrundlage: Betriebsanleitung in 4 Sprachen neben Fußschalter laminiert

**Confidence:** documented — Charterbetreiber-Dokumentation, Le Marin, Martinique.

---

## ANHANG E — Fallstudie: Nachrüstung Oyster 575 {#anhang-e}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Oyster 575, Baujahr 2016 |
| LOA | 17,52 m (57 ft) |
| Bordnetz | 24V, Victron Quattro + 800 Ah LiFePO4 |
| Vorhandene Winschen | 4× Lewmar 65 ST (manuell, 2 Cockpit + 2 Mast) |
| Crew | Ehepaar, Weltumsegelung |
| Revier | Weltweit |
| Budget | €25.000 |

### Entscheidung

Vollausstattung: alle 4 Winschen elektrisch. Lewmar EVO 65 EST. Zusätzlich Ankerwinsch-Upgrade.

### Durchführung

| Position | Beschreibung | Preis (€) |
|----------|-------------|----------|
| 4× | Lewmar EVO 65 EST Motor-Kit 24V | 4× 2.280 |
| 1× | Lewmar 68001026 Wireless Remote 4ch | 520 |
| 4× | Lewmar 68000938 Dual-Speed Fußschalter | 4× 139 |
| 50 m | Tinned Cable 70 mm² | 750 |
| 4× | Circuit Breaker 125 A DC | 4× 85 |
| — | Kabeldurchführungen, Kleinmaterial | 480 |
| — | Werft-Arbeit (5 Tage, 2 Techniker) | 6.200 |
| | **Gesamt** | **€19.826** |

### Ergebnis

- Vier vollelektrische Winschen, alle von Funk-Fernbedienung steuerbar
- 800 Ah LiFePO4-Bank versorgt alle Winschen problemlos gleichzeitig
- Stromverbrauch typischer Tag (Passatsegeln): ~15 Ah (24V) = 360 Wh
- Crew-Feedback: „Wie ein neues Boot. Wenden sind Einpersonen-Manöver geworden."

### Lessons Learned

1. Oyster: exzellenter Zugang unter Deck, gut vorbereitete Kabelwege
2. Bei 4 Winschen gleichzeitig: Hauptkabel von Batterie 95 mm² erforderlich
3. Funkfernbedienung: 4 Kanäle genau richtig (2× Cockpit + 2× Mast)
4. Lewmar Service-Netzwerk weltweit gut — wichtig für Blauwassersegler

**Confidence:** documented — Oyster-Owners-Netzwerk, Installationsbericht Southampton.

---

## ANHANG F — Fallstudie: Nachrüstung Beneteau Oceanis 51.1 {#anhang-f}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Beneteau Oceanis 51.1, Baujahr 2020 |
| LOA | 15,94 m (52 ft) |
| Bordnetz | 12V, 2× 200 Ah AGM |
| Vorhandene Winschen | 2× Harken 50.2 ST (Cockpit) |
| Crew | Ehepaar, 55 und 52 Jahre |
| Revier | Ostsee |
| Budget | €10.000 |

### Entscheidung

Nachrüstung der 2 Cockpitwinschen. Gleichzeitiger Umstieg auf 24V LiFePO4 für gesamtes Bordnetz (Inverter, Winschen, Bow-Thruster).

### Durchführung

| Position | Beschreibung | Preis (€) |
|----------|-------------|----------|
| 2× | Harken UniPower Motor-Kit M50-24 | 2× 1.750 |
| 1× | LiFePO4 24V 300 Ah + BMS (Victron Smart) | 3.280 |
| 2× | Harken B981 Dual-Speed Fußschalter | 2× 145 |
| 1× | Harken BRK2 Funkfernbedienung | 385 |
| 25 m | Tinned Cable 50 mm² | 275 |
| — | Sicherungen, Durchführungen, Kleinmaterial | 350 |
| — | Werft-Arbeit (3 Tage) | 2.600 |
| | **Gesamt** | **€10.680** |

**Hinweis:** Budget leicht überschritten, aber 24V-Umstieg bietet Mehrwert für gesamte Bordelektrik.

### Ergebnis

- Beide Winschen vollfunktionsfähig, Funkfernbedienung am Steuerrad
- 24V LiFePO4 versorgt auch Inverter und Bow-Thruster effizienter
- Gewichtsersparnis Batterien: 85 kg (AGM) → 32 kg (LiFePO4)
- Gesamtstromverbrauch Winschen pro Tag: ~7 Ah (24V)

### Lessons Learned

1. Beneteau-Deck: Balsasandwich, Verstärkung an Kabeldurchführungen Pflicht
2. 12V→24V-Umstieg: größtes Teilprojekt, aber langfristig die richtige Entscheidung
3. Ostsee: Kaltstartverhalten bei LiFePO4 beachten (Heizfolie empfohlen unter 5°C)
4. Harken M50-Kit: Motor passt in Harken 50.2 ohne jede Modifikation

**Confidence:** documented — Werftbericht Baltic Yachtservice Kiel, Projekt 2024-BYS-0156.

---

## ANHANG G — Fallstudie: Nachrüstung X-Yachts X4.3 {#anhang-g}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | X-Yachts X4.3, Baujahr 2017 |
| LOA | 13,29 m (43 ft) |
| Bordnetz | 24V, 2× 100 Ah AGM |
| Vorhandene Winschen | 2× Harken 46.2 ST (Cockpit), Performance-Setup |
| Crew | Einhandsegler, 45 Jahre, Regatta + Fahrt |
| Revier | Solent, Fastnet, Transatlantik |
| Budget | €18.000 |

### Entscheidung

Antal XT-E 52 als Komplettwinsch (Ersatz der Harken 46.2). Smart-Features für Regatta (Trimm-Speicher, Kraftmessung). Zusätzlich 2× Antal XT-E 40 am Mast (Fall-Winschen).

### Durchführung

| Position | Beschreibung | Preis (€) |
|----------|-------------|----------|
| 2× | Antal XT-E 52 Smart-Winch 24V | 2× 4.380 |
| 2× | Antal XT-E 40 Smart-Winch 24V | 2× 3.280 |
| 2× | Adapterplatte Harken→Antal (Cockpit) | 2× 195 |
| 1× | Antal WT-8 Wireless Remote 8ch | 780 |
| 1× | CAN-Bus Extension + T-Stücke | 280 |
| 40 m | Tinned Cable 50 mm² | 440 |
| 4× | Circuit Breaker 80 A DC | 4× 65 |
| — | Kleinmaterial | 250 |
| — | Werft-Arbeit (4 Tage) | 3.200 |
| | **Gesamt** | **€17.920** |

### Ergebnis

- 4 Smart-Winschen mit CAN-Bus, alle Daten auf B&G H5000 Prozessor
- Trimm-Speicher: 8 Presets für verschiedene Windstärken und Kurse
- Kraftmessung: Schot- und Fallasten in Echtzeit auf B&G Displays
- Regattaanalyse: Datenlogging aller Winsch-Aktionen mit Zeitstempel
- Funktion: Spi-Hissen per Fernbedienung in 4,2 Sekunden (12 m Fall)

### Lessons Learned

1. X-Yachts: exzellente Decksqualität, kein Balsasandwich (Divinycell/Corecell)
2. Antal Adapterplatten für Harken-Bohrbilder: gute Passform, minimale Nacharbeit
3. 8-Kanal-Fernbedienung: optimal für 4 Winschen (je 2 Richtungen)
4. CAN-Bus Diagnose: Antal Service-Tool (USB) für Firmware-Updates und Fehleranalyse

**Confidence:** documented — Eigner-Bericht, X-Yachts Owners Club.

---

## ANHANG H — Fallstudie: Nachrüstung Contest 50CS {#anhang-h}

### Ausgangslage

| Parameter | Wert |
|-----------|------|
| Boot | Contest 50CS, Baujahr 2014 |
| LOA | 15,22 m (50 ft) |
| Bordnetz | 24V, 4× 200 Ah AGM (24V-Bank) |
| Vorhandene Winschen | 2× Andersen 52ST (manuell, Cockpit), 1× Andersen 46ST (Großschot) |
| Crew | Ehepaar, 70 und 65 Jahre, Fahrt |
| Revier | Nordsee, Biskaya, Mittelmeer |
| Budget | €15.000 |

### Entscheidung

Andersen bietet keine Motor-Kits → Komplett-Tausch auf Andersen Electric. Trade-In-Programm nutzen (20% Rabatt auf Neuwinsch bei Rückgabe Altwinsch).

### Durchführung

| Position | Beschreibung | Preis (€) |
|----------|-------------|----------|
| 2× | Andersen RA2052E 52ST Electric 24V (Trade-In) | 2× 2.864 (statt 3.580) |
| 1× | Andersen RA2046E 46ST Electric 24V (Trade-In) | 2.416 (statt 3.020) |
| 3× | Andersen Plug & Play Elektrik-Kit | 3× 450 |
| 3× | Andersen Dual-Speed Fußschalter | 3× 155 |
| 1× | Lewmar 68001025 Wireless Remote 2ch | 420 |
| 30 m | Tinned Cable 50 mm² | 330 |
| — | Kleinmaterial | 220 |
| — | Werft-Arbeit (3 Tage) | 2.800 |
| | **Gesamt** | **€13.479** |

### Ergebnis

- Gewichtsersparnis: Andersen Electric leichter als manuelle Winschen + Motor-Kit
  - Alt: 2× 11,8 kg + 1× 9,5 kg = 33,1 kg
  - Neu: 2× 13,8 kg + 1× 11,5 kg = 39,1 kg → +6 kg (inklusive Motor!)
- Andersen Plug & Play Kit: vorkonfektionierte Kabel mit Steckern → Installationszeit halbiert
- Trade-In-Rabatt: €1.900 gespart
- Identisches Bohrlochbild Andersen→Andersen: keine Decksmodifikation nötig

### Lessons Learned

1. Andersen Trade-In lohnt sich finanziell und logistisch (Hersteller nimmt Altwinschen zurück)
2. Andersen Plug & Play Kit: beste Lösung für schnelle Installation
3. Contest-Deck: massives GFK-Laminat, keine Sandwich-Verstärkung nötig
4. Ältere Crew: Winsch-Bedienung muss intuitiv sein — Andersen Self-Tailing exzellent

**Confidence:** documented — Contest-Owners-Netzwerk, Werftbericht Jachtwerf Conyplex.

---

## ANHANG I — Normen und Standards {#anhang-i}

### Relevante Normen für elektrische Winschen

| Norm | Titel | Relevanz |
|------|-------|---------|
| ABYC E-11 | AC and DC Electrical Systems on Boats | Kabelquerschnitte, Sicherungen, Spannungsabfall |
| ISO 13297:2014 | Electrical systems — AC installations | Allgemeine elektrische Installation |
| ISO 10133:2012 | Electrical systems — Extra-low-voltage DC | DC-Installationen <50V |
| IEC 60092-507 | Electrical installations in ships — Pleasure craft | Schiffselektrik allgemein |
| ISO 12217 | Stability and buoyancy assessment | Gewichtsverteilung (Batterien, Motoren) |
| EN 55014 | EMC — Requirements for household appliances | EMV-Grenzwerte für Motoren |
| ISO 8846:1990 | Electrical devices — Protection against ignition | Zündschutz (wasserstoffbildende Batterien) |
| CE 2014/35/EU | Niederspannungsrichtlinie | Geräte 50–1000V AC, 75–1500V DC |
| CE 2006/42/EG | Maschinenrichtlinie | Sicherheitsanforderungen Winschen |
| ISO 15085:2003 | Man-overboard prevention | Sicherheit bei Decksbetrieb |

### ABYC E-11 Kernforderungen für E-Winschen

1. **Kabel:** Marine-Spezifikation (UL 1426 oder SAE J1127/J1128), verzinnt
2. **Querschnitt:** Basierend auf Strom, Länge und max. 3% Spannungsabfall
3. **Sicherung:** Innerhalb von 7 Zoll (180 mm) vom Batteriepol, oder max. 72 Zoll (1.830 mm) bei geschützter Verlegung
4. **Durchführungen:** Wasserdicht, flammhemmend
5. **Verbindungen:** Crimp oder Lötung mit mechanischer Sicherung, isoliert, korrosionsgeschützt
6. **Schalter:** Für DC-Last rated, mindestens 125% des Nennstroms
7. **Erdung:** Grün/gelber Leiter, Querschnitt mindestens wie der größte Verbraucherleiter

---

## ANHANG J — Pydantic v2 Modelle {#anhang-j}

```python
"""
AYDI Pydantic v2 Models — Elektrische Winschen und Nachrüstung
Module: 09_06_elektrische_winschen
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MotorType(str, Enum):
    """Typ des Elektromotors."""
    BRUSHED_DC = "brushed_dc"
    BLDC = "bldc"
    SERVO = "servo"


class VoltageSystem(str, Enum):
    """Bordnetzspannung."""
    V12 = "12V"
    V24 = "24V"
    V48 = "48V"


class GearboxType(str, Enum):
    """Getriebebauform."""
    PLANETARY = "planetary"
    WORM = "worm"
    SPUR = "spur"


class BatteryType(str, Enum):
    """Batterietechnologie."""
    AGM = "agm"
    GEL = "gel"
    LIFEPO4 = "lifepo4"
    LEAD_ACID = "lead_acid"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence-Stufe."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ControlType(str, Enum):
    """Steuerungsart."""
    RELAY = "relay"
    PWM = "pwm"
    CAN_BUS = "can_bus"
    NMEA2000 = "nmea2000"


class WinchManufacturer(str, Enum):
    """Winschenhersteller."""
    HARKEN = "harken"
    LEWMAR = "lewmar"
    ANDERSEN = "andersen"
    ANTAL = "antal"
    PONTOS = "pontos"


class ElectricWinchSpec(BaseModel):
    """Spezifikation einer elektrischen Winsch."""

    model_config = {"from_attributes": True}

    manufacturer: WinchManufacturer
    model_number: str = Field(..., description="Artikelnummer des Herstellers")
    size: int = Field(..., ge=30, le=120, description="Winschengröße (Herstellerangabe)")
    motor_type: MotorType
    voltage: VoltageSystem
    max_pull_kg: float = Field(..., ge=0, description="Maximaler Leinenzug in kg")
    power_speed_m_per_min: float = Field(..., ge=0, description="Liniengeschwindigkeit Power-Modus [m/min]")
    high_speed_m_per_min: float = Field(..., ge=0, description="Liniengeschwindigkeit High-Speed-Modus [m/min]")
    current_draw_a: float = Field(..., ge=0, description="Stromaufnahme bei Nennlast [A]")
    motor_power_w: Optional[float] = Field(None, ge=0, description="Nennleistung Motor [W]")
    weight_kg: float = Field(..., ge=0, description="Gewicht komplett [kg]")
    noise_db_a: Optional[float] = Field(None, ge=0, le=120, description="Geräusch bei Nennlast [dB(A)]")
    duty_cycle_percent: Optional[float] = Field(None, ge=0, le=100, description="Einschaltdauer [%]")
    has_can_bus: bool = Field(False, description="CAN-Bus / NMEA2000 Interface")
    has_force_sensor: bool = Field(False, description="Integrierter Kraftsensor")
    ip_rating: str = Field("IP56", description="Schutzart")
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis EUR (geschätzt)")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Confidence-Stufe der Daten"
    )


class RetrofitKit(BaseModel):
    """Motor-Kit zur Nachrüstung einer manuellen Winsch."""

    model_config = {"from_attributes": True}

    kit_article_number: str = Field(..., description="Artikelnummer des Kits")
    manufacturer: WinchManufacturer
    fits_winch_model: str = Field(..., description="Kompatible Winsch (Modell)")
    motor_type: MotorType
    motor_power_w: float = Field(..., ge=0, description="Motorleistung [W]")
    voltage: VoltageSystem
    includes_controller: bool = Field(True)
    includes_foot_switch: bool = Field(True)
    includes_cable_set: bool = Field(True)
    cable_length_m: float = Field(2.0, ge=0, description="Beiliegende Kabellänge [m]")
    weight_kg: float = Field(..., ge=0, description="Kit-Gewicht [kg]")
    price_eur: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel = Field(ConfidenceLevel.DOCUMENTED)


class CableCalculation(BaseModel):
    """Kabelquerschnitt-Berechnung nach ABYC E-11."""

    model_config = {"from_attributes": True}

    current_a: float = Field(..., ge=0, description="Nennstrom [A]")
    cable_length_m: float = Field(..., ge=0, description="Einfache Kabellänge [m]")
    voltage_system: VoltageSystem
    max_voltage_drop_percent: float = Field(3.0, ge=0, le=10, description="Max. Spannungsabfall [%]")
    calculated_cross_section_mm2: float = Field(..., ge=0, description="Berechneter Querschnitt [mm²]")
    recommended_cross_section_mm2: float = Field(..., ge=0, description="Empfohlener Standardquerschnitt [mm²]")
    recommended_awg: Optional[str] = Field(None, description="Empfohlene AWG-Größe")
    fuse_size_a: float = Field(..., ge=0, description="Empfohlene Sicherungsgröße [A]")
    actual_voltage_drop_percent: float = Field(..., ge=0, description="Tatsächlicher Spannungsabfall [%]")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.CALCULATED)


class RetrofitProject(BaseModel):
    """Komplettes Nachrüstprojekt."""

    model_config = {"from_attributes": True}

    project_name: str
    boat_name: Optional[str] = None
    boat_type: str = Field(..., description="Bootstyp (z.B. 'Bavaria 40 Cruiser')")
    boat_year: int = Field(..., ge=1970, le=2030)
    boat_loa_m: float = Field(..., ge=5, le=50)
    voltage_system: VoltageSystem
    battery_type: BatteryType
    battery_capacity_ah: float = Field(..., ge=0)
    winches: list[ElectricWinchSpec] = Field(default_factory=list)
    retrofit_kits: list[RetrofitKit] = Field(default_factory=list)
    cable_calculations: list[CableCalculation] = Field(default_factory=list)
    total_cost_eur: Optional[float] = Field(None, ge=0)
    installation_days: Optional[float] = Field(None, ge=0)
    notes: Optional[str] = None
    date_completed: Optional[date] = None
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED)


class ElectricWinchFinding(BaseModel):
    """Einzelbefund bei der Analyse einer elektrischen Winsch."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID (z.B. 'F-EW-01')")
    title: str = Field(..., description="Kurztitel des Befunds")
    description: str = Field(..., description="Detailbeschreibung")
    severity: str = Field(..., pattern="^(critical|major|minor|info)$")
    location: Optional[str] = Field(None, description="Betroffene Winsch / Position")
    recommendation: str = Field(..., description="Empfohlene Maßnahme")
    estimated_cost_eur: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel


class ElectricWinchAnalysis(BaseModel):
    """Gesamtanalyse der elektrischen Winschen an Bord."""

    model_config = {"from_attributes": True}

    boat_type: str
    boat_year: int
    analysis_date: date
    winches_analyzed: list[ElectricWinchSpec] = Field(default_factory=list)
    findings: list[ElectricWinchFinding] = Field(default_factory=list)
    overall_score: float = Field(..., ge=0, le=100, description="Gesamtbewertung 0–100")
    overall_confidence: ConfidenceLevel
    recommendations: list[str] = Field(default_factory=list)
    retrofit_viable: bool = Field(False, description="Nachrüstung sinnvoll?")
    estimated_retrofit_cost_eur: Optional[float] = Field(None, ge=0)
```

---

## ANHANG K — Verkabelungspläne {#anhang-k}

### K.1 Standard-Verkabelungsschema (1 E-Winsch, 24V)

```
┌─────────────┐
│  LiFePO4    │
│  25,6V      │
│  200 Ah     │
│             │
│  (+) ───────┼──── ■ CB 100A ────── Kabel 50mm², L=5m ──── (+) Controller
│             │     (max. 1m                                      │
│  (−) ───────┼──── von Batterie)                            (−) Controller
│             │         │                                         │
└─────────────┘         │                                    ┌────┴────┐
                        │                                    │  BLDC   │
                   ■ Masse-                                  │  Motor  │
                   Sammelschiene                             │ 1200W   │
                        │                                    └────┬────┘
                   ■ Kiel-Bolzen                                  │
                                                             ┌────┴────┐
                                                             │  Winsch  │
                                                             │  Getriebe│
                                                             └─────────┘

Steuerleitung:
Fußschalter ──── (2-Draht, 1,5mm²) ──── Controller Steuereingang

Masse:
Controller Gehäuse ── (16mm² grün/gelb) ── Masse-Sammelschiene
```

### K.2 Dual-Winsch-Verkabelung (2 E-Winschen, 24V)

```
┌─────────────┐
│  LiFePO4    │
│  25,6V      │
│  200 Ah     │
│             │
│  (+) ───────┼──── ■ Haupt-CB 200A
│             │           │
│  (−) ───────┼──── ──────┤
│             │           │
└─────────────┘     ┌─────┴─────┐
                    │           │
              ■ CB 100A   ■ CB 100A
                    │           │
              Kabel 50mm²  Kabel 50mm²
              L=4m         L=5m
                    │           │
              Controller  Controller
              Winsch BB   Winsch StB
                    │           │
              Motor BB    Motor StB
                    │           │
              Winsch BB   Winsch StB

Fußschalter BB ── (2×1,5mm²) ── Controller BB
Fußschalter StB ── (2×1,5mm²) ── Controller StB
Funk-Empfänger ── (4×1,5mm²) ── Controller BB + Controller StB
```

### K.3 Retrofit mit DC-DC-Wandler (12V-Boot, 24V-Winschen)

```
┌─────────────┐         ┌───────────────┐
│  12V AGM    │         │  DC-DC        │
│  2×110 Ah   │         │  12V → 24V    │
│             │         │  30A (720W)   │
│  (+) ───────┼── ■ CB ─┼── IN (+)      │
│             │   40A   │               │        ┌──────────┐
│  (−) ───────┼─────────┼── IN (−)      │        │ LiFePO4  │
│             │         │               │        │ 25,6V    │
└─────────────┘         │  OUT (+) ─────┼── ■ ───┤ 100 Ah   │
                        │               │  CB    │          │
                        │  OUT (−) ─────┼────────┤          │
                        └───────────────┘  50A   └────┬─────┘
                                                      │
                                                ┌─────┴─────┐
                                                │           │
                                          ■ CB 100A   ■ CB 100A
                                                │           │
                                          Controller  Controller
                                          Winsch BB   Winsch StB
```

---

## ANHANG L — Hersteller-Kontaktdaten und Ersatzteilbezug {#anhang-l}

### Harken

| Information | Details |
|-------------|---------|
| Hersteller | Harken, Inc. |
| Hauptsitz | Pewaukee, Wisconsin, USA |
| EU-Vertrieb | Harken Italy S.r.l., Limido Comasco (CO), Italien |
| Website | www.harken.com |
| Ersatzteil-Hotline EU | +39 031 895 866 |
| E-Mail | info@harken.it |
| Online-Ersatzteilkatalog | www.harken.com/en/support/parts |
| Händlernetz DE | ~45 autorisierte Händler |
| Lieferzeit Ersatzteile | Standard: 5–10 Werktage, Express: 2–3 Werktage |

### Lewmar

| Information | Details |
|-------------|---------|
| Hersteller | Lewmar Ltd. |
| Hauptsitz | Havant, Hampshire, UK |
| EU-Vertrieb | Lewmar B.V., Niederlande |
| Website | www.lewmar.com |
| Ersatzteil-Hotline EU | +31 (0) 75 684 8800 |
| E-Mail | customerservice@lewmar.com |
| Online-Ersatzteilkatalog | www.lewmar.com/parts |
| Händlernetz DE | ~35 autorisierte Händler |
| Lieferzeit Ersatzteile | Standard: 7–14 Werktage |

### Andersen

| Information | Details |
|-------------|---------|
| Hersteller | Andersen Winches ApS |
| Hauptsitz | Hundested, Dänemark |
| Website | www.andersen-winches.com |
| Ersatzteil-Hotline | +45 47 93 75 25 |
| E-Mail | info@andersen-winches.com |
| Online-Ersatzteilkatalog | www.andersen-winches.com/spare-parts |
| Händlernetz DE | ~20 autorisierte Händler |
| Lieferzeit Ersatzteile | Standard: 5–10 Werktage (ab Lager DK) |

### Antal

| Information | Details |
|-------------|---------|
| Hersteller | Antal S.r.l. |
| Hauptsitz | Arona (NO), Italien |
| Website | www.antal.it |
| Ersatzteil-Hotline | +39 0322 46696 |
| E-Mail | info@antal.it |
| Online-Ersatzteilkatalog | www.antal.it/spare-parts |
| Händlernetz DE | ~15 autorisierte Händler |
| Lieferzeit Ersatzteile | Standard: 7–14 Werktage |

---

## ANHANG M — Wartungsintervalle und Checklisten {#anhang-m}

### M.1 Monatliche Kontrolle (15 Minuten)

| Nr. | Prüfpunkt | Methode | OK-Kriterium |
|-----|-----------|---------|-------------|
| 1 | Fußschalter-Funktion | Betätigen | Winsch reagiert sofort |
| 2 | Totmann-Funktion | Loslassen | Winsch stoppt sofort |
| 3 | Sichtprüfung Kabel (sichtbare) | Visuell | Keine Beschädigung, keine Korrosion |
| 4 | Geräuschprüfung (Leerlauf) | Hören | Kein ungewöhnliches Geräusch |
| 5 | Self-Tailing-Funktion | Leine einlegen, belasten | Leine hält ohne Durchrutschen |

### M.2 Saisonstart-Inspektion (1 Stunde)

| Nr. | Prüfpunkt | Methode | OK-Kriterium |
|-----|-----------|---------|-------------|
| 1 | Batteriespannung | Multimeter | >12,6V (12V) / >25,2V (24V) |
| 2 | Freilauf-Test | Kurbel ohne Strom | Leichtgängig in beide Richtungen |
| 3 | Lasttest | Schot mit ~50% Last | Winsch holt zügig und gleichmäßig |
| 4 | Stromaufnahme Leerlauf | Zangenamperemeter | <10 A (24V) / <20 A (12V) |
| 5 | Stromaufnahme Last | Zangenamperemeter | Im Herstellerspezifikation |
| 6 | Drehrichtung | Beobachten | Im Uhrzeigersinn = Dichtholen |
| 7 | Beide Geschwindigkeiten | Fußschalter | Speed und Power funktionieren |
| 8 | Controller-LED | Visuell | Grünes Dauerlicht (kein Fehler) |
| 9 | Kabelverbindungen unter Deck | Rütteln, visuell | Fest, keine Korrosion |
| 10 | Decksdurchführungen | Visuell, Wassertest | Dicht |

### M.3 Jährliche Wartung (2–3 Stunden pro Winsch)

| Nr. | Maßnahme | Material |
|-----|----------|---------|
| 1 | Winsch demontieren (Trommel, Self-Tailing) | Werkzeug-Set |
| 2 | Getriebe reinigen (altes Fett entfernen) | Waschbenzin, Pinsel |
| 3 | Getriebe inspizieren (Zahnflanken, Lager) | Lupe, Licht |
| 4 | Getriebe neu fetten | Hersteller-Fett |
| 5 | Winsch zusammenbauen | — |
| 6 | Korrosionsschutz Motor und Controller | CorrosionX oder ACF-50 |
| 7 | Alle Kabelverbindungen nachziehen | Drehmomentschlüssel |
| 8 | Sicherungen/CB prüfen | Visuell, Multimeter |
| 9 | Fußschalter reinigen, Dichtung prüfen | Süßwasser, Silikonspray |
| 10 | Funktionstest komplett | — |

---

## ANHANG N — Gewichts- und Schwerpunktanalyse {#anhang-n}

### N.1 Gewichtsänderung durch Elektrifizierung

Die Nachrüstung elektrischer Winschen verändert die Gewichtsverteilung des Bootes. Bei AYDI-Analysen muss dies berücksichtigt werden.

**Typische Gewichtszunahme pro Winsch (Retrofit-Kit):**

| Winschgröße | Motor + Getriebe | Controller | Kabel (5 m) | Fußschalter | Gesamt |
|-------------|-----------------|-----------|-------------|-------------|--------|
| 35–40 | 3,5 kg | 0,8 kg | 4,8 kg | 0,3 kg | 9,4 kg |
| 46–50 | 5,0 kg | 1,0 kg | 4,8 kg | 0,3 kg | 11,1 kg |
| 55–60 | 7,0 kg | 1,2 kg | 6,4 kg | 0,3 kg | 14,9 kg |
| 65–80 | 10,0 kg | 1,5 kg | 6,4 kg | 0,3 kg | 18,2 kg |

**Zusätzlich: Batteriebank (falls Upgrade):**

| Upgrade | Gewichtsänderung |
|---------|-----------------|
| AGM 200 Ah → LiFePO4 200 Ah (24V) | -55 kg |
| AGM 400 Ah → LiFePO4 200 Ah (24V) | -90 kg (gleiche nutzbare Kapazität) |
| Keine Änderung (vorh. Bank reicht) | 0 kg |

**Schwerpunktlage:**
- Motoren: unter Deck, nahe Deckslinie → Schwerpunkt steigt leicht
- Batterien: typisch tief im Boot → Schwerpunkt sinkt bei LiFePO4-Upgrade
- Kabel: vertikal verteilt → neutraler Effekt
- **Netto-Effekt (typisch):** leichte Senkung des Schwerpunkts bei gleichzeitigem LiFePO4-Upgrade

### N.2 AYDI-Bewertungskriterien

| Kriterium | Gewichtung | Bewertungsskala |
|-----------|-----------|----------------|
| Gewichtszunahme <5% Verdrängung | 30% | 100 (OK) / 50 (grenzwertig) / 0 (kritisch) |
| Schwerpunktverschiebung <20 mm | 25% | 100 / 50 / 0 |
| Symmetrische Verteilung (BB=StB) | 20% | 100 / 75 / 50 |
| Trimm-Änderung <0,5° | 25% | 100 / 50 / 0 |

---

## ANHANG O — Confidence-Mapping {#anhang-o}

### O.1 Datenquellen und Confidence-Zuordnung

| Datentyp | Quelle | Confidence-Level |
|----------|--------|-----------------|
| Elektrische Spezifikationen | Hersteller-TDS | measured |
| Mechanische Spezifikationen | Hersteller-Katalog | measured |
| Geräuschmessungen | Hersteller + Fachzeitschriften | measured |
| Preise | Händler-Durchschnitt | estimated |
| Kabelquerschnitt-Berechnung | ABYC E-11 Formel | calculated |
| Einschaltdauer | Hersteller-TDS | measured |
| Fehlerstatistik | Werft-Servicedaten | documented |
| Wartungsintervalle | Hersteller + Praxis | documented |
| Retrofiterfahrungen | Eigner-Berichte, Foren | estimated |
| Kompatibilitätsdaten | Hersteller-Listen | documented |
| Markttrends | Branchenberichte | estimated |
| Lebensdauer-Prognosen | Erfahrungswerte | estimated |

### O.2 Confidence-Einschränkungen

| Bereich | Einschränkung | Auswirkung |
|---------|--------------|-----------|
| Preise | Schwanken nach Region, Saison, Händler | ±15% Ungenauigkeit |
| Geräusch | Messbedingungen variieren | ±3 dB(A) |
| Lebensdauer | Stark nutzungsabhängig | ±50% |
| Retrofit-Kosten | Werft-Stundensätze regional verschieden | ±25% |
| Batterie-Performance | Abhängig von Alter und Zustand | ±20% |

---

## ANHANG P — Wirtschaftlichkeitsberechnung {#anhang-p}

### P.1 Total Cost of Ownership (TCO) über 10 Jahre

**Szenario: 2 E-Winschen, 42-ft-Fahrtensegler, 24V, LiFePO4**

| Kostenposition | Jahr 0 | Jahr 1–5 (p.a.) | Jahr 6–10 (p.a.) | Gesamt 10 Jahre |
|---------------|--------|-----------------|------------------|----------------|
| Winschen (Motor-Kit) | €3.100 | — | — | €3.100 |
| Elektrik + Installation | €2.800 | — | — | €2.800 |
| LiFePO4-Batterie | €2.450 | — | — | €2.450 |
| Jährliche Wartung | — | €100 | €150 | €1.250 |
| Getriebe-Service (3+6 J.) | — | €400 (Jahr 3) | €400 (Jahr 6) | €800 |
| Lager-Tausch (Jahr 5) | — | €300 (Jahr 5) | — | €300 |
| **Gesamt** | **€8.350** | | | **€10.700** |

**Kosten pro Jahr:** €1.070
**Kosten pro Segeltag (80 Tage/Jahr):** €13,38

### P.2 Vergleich: Manuelle Winsch (Alternativkosten)

| Position | Manuelle Winsch (10 Jahre) |
|----------|--------------------------|
| Wartung (jährlich) | €50 × 10 = €500 |
| Getriebe-Service | €200 × 2 = €400 |
| Chiropraktiker / Physiotherapie | €300 × 10 = €3.000 |
| Crew-Aushilfe (kräftige Person) | €200 × 10 = €2.000 |
| **Gesamt** | **€5.900** |

**Differenz:** €10.700 − €5.900 = €4.800 Mehrkosten über 10 Jahre
**Pro Jahr:** €480 Mehrkosten = ca. €6/Segeltag

**Nicht monetäre Vorteile:** Sicherheit (weniger Verletzungen), Komfort, Unabhängigkeit (Einhandsegeln), Werterhaltung Boot (+€3.000–6.000 Wiederverkauf).

---

## ANHANG Q — Elektromagnetische Verträglichkeit (EMV) {#anhang-q}

### Q.1 EMV-Anforderungen

Elektrische Winschen müssen die EMV-Anforderungen nach EN 55014 und der EU-EMV-Richtlinie 2014/30/EU erfüllen.

**Grenzwerte für leitungsgebundene Störungen:**

| Frequenzbereich | Grenzwert (Quasi-Peak) | Grenzwert (Average) |
|----------------|----------------------|-------------------|
| 150 kHz – 500 kHz | 66–56 dBμV | 56–46 dBμV |
| 500 kHz – 5 MHz | 56 dBμV | 46 dBμV |
| 5 MHz – 30 MHz | 60 dBμV | 50 dBμV |

### Q.2 EMV-Maßnahmen bei der Installation

| Maßnahme | Wirkung | Aufwand |
|----------|---------|--------|
| Verdrillte Leistungskabel (+/−) | Reduziert abgestrahlte Störungen | Gering |
| Ferrit-Ringkerne auf Versorgung | Dämpft HF-Störungen | Gering (€5–15 pro Stück) |
| LC-Eingangsfilter am Controller | Reduziert leitungsgebundene Störungen | Mittel (€30–80) |
| Geschirmte Steuerleitungen | Verhindert Einkopplung | Mittel |
| Sternförmige Masseführung | Vermeidet Masseschleifen | Mittel |
| Mindestabstand Motor → Antenne: 1 m | Reduziert magnetische Kopplung | Planungsabhängig |
| Getrennte Stromkreise (Winsch / Navigation) | Galvanische Trennung | Hoch (DC-DC-Isolator) |

### Q.3 Typische EMV-Probleme und Lösungen

| Problem | Gestörtes Gerät | Lösung |
|---------|----------------|--------|
| Bürstenmotor-Funken | UKW-Funk, SSB | Entstörkondensatoren 100 nF am Motor + Ferrite |
| PWM-Oberwellen | AIS-Empfänger | LC-Filter am Controller-Eingang |
| Schaltregler-Störung (DC-DC) | GPS | Geschirmten DC-DC-Wandler verwenden |
| Masseschleife | Autopilot-Kompass | Sternpunkt-Erdung, Isolatoren |
| Motor-Permanentmagnete | Steuerkurkompass | Min. 1 m Abstand, Kompensation |

---

## ANHANG R — Retrofit-Planungsvorlage {#anhang-r}

### R.1 Checkliste vor der Bestellung

```
RETROFIT-PLANUNGSBOGEN — Elektrische Winschen

BOOT-DATEN:
□ Bootstyp: _________________________________
□ Baujahr: __________  LOA: __________ m
□ Bordnetzspannung: □ 12V  □ 24V  □ 48V
□ Batterietyp: □ AGM  □ GEL  □ LiFePO4  □ Blei-Säure
□ Batteriekapazität: __________ Ah  (__________ V)
□ Lichtmaschine: __________ A
□ Ladegerät (Landstrom): __________ A
□ Solar: □ Ja (__________ Wp)  □ Nein

VORHANDENE WINSCHEN:
□ Winsch 1: Hersteller: ____________ Modell: ____________ Größe: ____
  Position: □ Cockpit BB  □ Cockpit StB  □ Cockpitdach  □ Mast
□ Winsch 2: Hersteller: ____________ Modell: ____________ Größe: ____
  Position: □ Cockpit BB  □ Cockpit StB  □ Cockpitdach  □ Mast
□ Winsch 3: Hersteller: ____________ Modell: ____________ Größe: ____
  Position: _________________________________
□ Winsch 4: Hersteller: ____________ Modell: ____________ Größe: ____
  Position: _________________________________

MESSUNGEN:
□ Bolzenlochkreis Winsch 1: __________ mm, __________ Bolzen, M____
□ Bolzenlochkreis Winsch 2: __________ mm, __________ Bolzen, M____
□ Decksdicke an Winsch 1: __________ mm  Sandwich: □ Ja  □ Nein
□ Decksdicke an Winsch 2: __________ mm  Sandwich: □ Ja  □ Nein
□ Freiraum unter Deck Winsch 1: Höhe _____ mm, Ø _____ mm
□ Freiraum unter Deck Winsch 2: Höhe _____ mm, Ø _____ mm
□ Kabellänge Batterie → Winsch 1: __________ m
□ Kabellänge Batterie → Winsch 2: __________ m

ZUGANG:
□ Zugang unter Winsch 1: □ Gut  □ Eingeschränkt  □ Schwierig
□ Zugang unter Winsch 2: □ Gut  □ Eingeschränkt  □ Schwierig
□ Kabelweg frei: □ Ja  □ Teilweise  □ Nein (Beschreibung: ___________)

STEUERUNG:
□ Gewünschte Fußschalter: □ Single-Speed  □ Dual-Speed  □ Richtungsumkehr
□ Fußschalter-Positionen: _________________________________
□ Funk-Fernbedienung: □ Ja (__________ Kanäle)  □ Nein
□ CAN-Bus / NMEA2000: □ Ja  □ Nein
□ MFD-Typ: _________________________________

BUDGET:
□ Gesamtbudget: __________ EUR
□ Eigenleistung: □ Ja (Anteil: ____%)  □ Nein (Werft komplett)
□ Zeitrahmen: _________________________________
```

### R.2 Bestell-Checkliste

```
BESTELLLISTE — Elektrische Winschen Retrofit

HAUPTKOMPONENTEN:
□ ____× Motor-Kit / E-Winsch: _________________ Art.Nr.: _______________
□ Batterie-Upgrade: __________________________ Art.Nr.: _______________
□ DC-DC-Wandler (falls nötig): ________________ Art.Nr.: _______________

ELEKTRIK:
□ Kabel (+): _______ m × _______ mm²  Tinned Marine Cable
□ Kabel (−): _______ m × _______ mm²  Tinned Marine Cable
□ Kabelschuhe: _______ Stück, M_____, für _______ mm²
□ Sicherungsautomaten: _______ Stück × _______ A, DC-rated
□ Hauptsicherung: _______ A
□ Kabeldurchführungen: _______ Stück, IP68, M_____

STEUERUNG:
□ Fußschalter: _______ Stück, Typ: _______________________
□ Funk-Fernbedienung: Art.Nr.: _______________________
□ CAN-Bus-Kabel: _______ m

VERBRAUCHSMATERIAL:
□ Sikaflex 291: _______ Kartuschen
□ Loctite 243: 1 Flasche
□ Schrumpfschlauch (klebend): _______ m
□ Edelstahl-Kabelbinder: _______ Stück
□ Korrosionsschutz-Spray: 1 Dose
□ Winschenfett: 1 Dose
□ Epoxid-Harz (Kernverstärkung): _______ kg

WERKZEUG (falls nicht vorhanden):
□ Hydraulische Crimpzange (>50 mm²)
□ Lochsäge ∅ _______ mm
□ Zangenamperemeter (DC, >150 A)
□ Multimeter
□ Drehmomentschlüssel
```

---

## ANHANG S — Kabelquerschnitt-Tabellen (vollständig) {#anhang-s}

### S.1 Kabelquerschnitt 12V-System (3% max. Spannungsabfall)

Berechnung nach ABYC E-11: A = (I × L × 2) / (K × ΔU)
- K (Kupfer) = 56 m/(Ω·mm²)
- ΔU = U_nenn × max_drop% = 12V × 0,03 = 0,36V

| Strom [A] | 2 m | 3 m | 4 m | 5 m | 6 m | 7 m | 8 m | 10 m |
|-----------|-----|-----|-----|-----|-----|-----|-----|------|
| 20 | 4 mm² | 6 mm² | 8 mm² | 10 mm² | 12 mm² | 14 mm² | 16 mm² | 20 mm² |
| 30 | 6 mm² | 10 mm² | 12 mm² | 16 mm² | 18 mm² | 22 mm² | 24 mm² | 30 mm² |
| 40 | 8 mm² | 12 mm² | 16 mm² | 20 mm² | 24 mm² | 28 mm² | 32 mm² | 40 mm² |
| 50 | 10 mm² | 16 mm² | 20 mm² | 25 mm² | 30 mm² | 35 mm² | 40 mm² | 50 mm² |
| 60 | 12 mm² | 18 mm² | 24 mm² | 30 mm² | 36 mm² | 42 mm² | 48 mm² | 60 mm² |
| 80 | 16 mm² | 24 mm² | 32 mm² | 40 mm² | 48 mm² | 56 mm² | 64 mm² | 80 mm² |
| 100 | 20 mm² | 30 mm² | 40 mm² | 50 mm² | 60 mm² | 70 mm² | 80 mm² | 100 mm² |
| 120 | 24 mm² | 36 mm² | 48 mm² | 60 mm² | 72 mm² | 84 mm² | 96 mm² | 120 mm² |
| 150 | 30 mm² | 44 mm² | 60 mm² | 74 mm² | 90 mm² | 104 mm² | 120 mm² | 150 mm² |

**Hinweis:** Bei 12V-Systemen werden die Kabelquerschnitte sehr groß. Dies ist der Hauptgrund, warum E-Winschen bevorzugt in 24V-Systemen betrieben werden.

### S.2 Kabelquerschnitt 24V-System (3% max. Spannungsabfall)

| Strom [A] | 2 m | 3 m | 4 m | 5 m | 6 m | 7 m | 8 m | 10 m |
|-----------|-----|-----|-----|-----|-----|-----|-----|------|
| 20 | 2,5 mm² | 4 mm² | 4 mm² | 6 mm² | 6 mm² | 8 mm² | 8 mm² | 10 mm² |
| 30 | 4 mm² | 4 mm² | 6 mm² | 8 mm² | 10 mm² | 10 mm² | 12 mm² | 16 mm² |
| 40 | 4 mm² | 6 mm² | 8 mm² | 10 mm² | 12 mm² | 14 mm² | 16 mm² | 20 mm² |
| 50 | 6 mm² | 8 mm² | 10 mm² | 12 mm² | 16 mm² | 18 mm² | 20 mm² | 25 mm² |
| 60 | 6 mm² | 10 mm² | 12 mm² | 16 mm² | 18 mm² | 22 mm² | 24 mm² | 30 mm² |
| 80 | 8 mm² | 12 mm² | 16 mm² | 20 mm² | 24 mm² | 28 mm² | 32 mm² | 40 mm² |
| 100 | 10 mm² | 16 mm² | 20 mm² | 25 mm² | 30 mm² | 35 mm² | 40 mm² | 50 mm² |
| 120 | 12 mm² | 18 mm² | 24 mm² | 30 mm² | 36 mm² | 42 mm² | 48 mm² | 60 mm² |
| 150 | 16 mm² | 22 mm² | 30 mm² | 38 mm² | 44 mm² | 52 mm² | 60 mm² | 74 mm² |

### S.3 Kabelquerschnitt 48V-System (3% max. Spannungsabfall)

| Strom [A] | 2 m | 3 m | 4 m | 5 m | 6 m | 7 m | 8 m | 10 m |
|-----------|-----|-----|-----|-----|-----|-----|-----|------|
| 20 | 1,5 mm² | 2,5 mm² | 2,5 mm² | 4 mm² | 4 mm² | 4 mm² | 4 mm² | 6 mm² |
| 30 | 2,5 mm² | 2,5 mm² | 4 mm² | 4 mm² | 6 mm² | 6 mm² | 6 mm² | 8 mm² |
| 40 | 2,5 mm² | 4 mm² | 4 mm² | 6 mm² | 6 mm² | 8 mm² | 8 mm² | 10 mm² |
| 50 | 4 mm² | 4 mm² | 6 mm² | 6 mm² | 8 mm² | 10 mm² | 10 mm² | 12 mm² |
| 60 | 4 mm² | 6 mm² | 6 mm² | 8 mm² | 10 mm² | 10 mm² | 12 mm² | 16 mm² |
| 80 | 4 mm² | 6 mm² | 8 mm² | 10 mm² | 12 mm² | 14 mm² | 16 mm² | 20 mm² |
| 100 | 6 mm² | 8 mm² | 10 mm² | 12 mm² | 16 mm² | 18 mm² | 20 mm² | 25 mm² |

### S.4 AWG-Äquivalenztabelle

| mm² | AWG | Typische Anwendung (E-Winsch) |
|-----|-----|-------------------------------|
| 1,5 | 16 | Steuerleitungen, CAN-Bus |
| 2,5 | 14 | Steuerleitungen, Sensorik |
| 4 | 12 | Steuerrelais, kleine Verbraucher |
| 6 | 10 | Kleine E-Winschen (24V, kurze Strecke) |
| 10 | 8 | Mittlere E-Winschen (24V) |
| 16 | 6 | Standard E-Winschen (24V) |
| 25 | 4 | Große E-Winschen (24V), mittlere (12V) |
| 35 | 2 | Große E-Winschen (12V/24V) |
| 50 | 1/0 | Sehr große E-Winschen, 12V-Systeme |
| 70 | 2/0 | Extreme Ströme, lange 12V-Strecken |
| 95 | 3/0 | Selten für E-Winschen, eher Bugstrahlruder |
| 120 | 4/0 | Nicht typisch für E-Winschen |

### S.5 Sicherungstabelle nach Kabelquerschnitt

| Kabelquerschnitt [mm²] | Max. Dauerstrom [A] | Empf. Sicherung [A] |
|------------------------|--------------------|--------------------|
| 4 | 30 | 25 |
| 6 | 40 | 35 |
| 10 | 55 | 50 |
| 16 | 75 | 70 |
| 25 | 100 | 90 |
| 35 | 130 | 125 |
| 50 | 175 | 150 |
| 70 | 225 | 200 |
| 95 | 275 | 250 |

**AYDI-Confidence:** calculated — basierend auf ABYC E-11 und ISO 13297.

---

## ANHANG T — Visuelle Inspektions-Leitfaden {#anhang-t}

### T.1 AYDI Pipeline B: Visuelle Erkennung von E-Winschen-Defekten

Die visuelle Analyse von E-Winschen-Zuständen durch Fotos nutzt die AYDI Pipeline B (Claude Vision API). Folgend die Erkennungsmerkmale für die automatisierte Bildanalyse.

### T.2 Decksdurchführung — Visueller Zustand

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Intakt | Gleichmäßige Sikaflex-Raupe, keine Risse, keine Verfärbung | 0 | visual_high |
| Leichte Alterung | Sikaflex leicht vergilbt, noch elastisch, keine Risse | -5 | visual_medium |
| Rissig | Sichtbare Risse in der Dichtung, noch kein Wasserrand | -15 | visual_high |
| Undicht | Wasserränder, Salzablagerungen, Korrosionsspuren an Schrauben | -30 | visual_high |
| Schwer beschädigt | Dichtung fehlt teilweise, Spaltbildung, Rost | -50 | visual_high |

### T.3 Motor/Controller — Visueller Zustand (unter Deck)

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Neuwertig | Saubere Oberfläche, keine Korrosion, Kabel ordentlich | 0 | visual_high |
| Gut | Leichte Staubablagerung, keine Korrosion | -3 | visual_high |
| Korrosionsbeginn | Einzelne Korrosionspunkte am Gehäuse (Nicht-Edelstahl-Teile) | -15 | visual_medium |
| Korrodiert | Flächige Korrosion, weiße Salzablagerungen auf Aluminium | -25 | visual_high |
| Feuchteschaden | Wasserstand-Markierungen, aufgequollene Kabel, grüne Kupferpatina | -40 | visual_high |
| Schwer korrodiert | Massive Korrosion, gelöste Kontakte, aufgeblähte Stecker | -60 | visual_high |

### T.4 Kabelführung — Visueller Zustand

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Professionell | Kabelkanäle, Kabelbinder, Beschriftung, Knickschutz | 0 | visual_high |
| Akzeptabel | Kabelbinder, aber keine Kanäle, keine Beschriftung | -5 | visual_high |
| Mangelhaft | Lose Kabel, teilweise ungesichert, Scheuerstellen sichtbar | -20 | visual_high |
| Gefährlich | Blanke Kabel sichtbar, keine Zugentlastung, Kabel auf heißen Flächen | -40 | visual_high |

### T.5 Batterie-Installation — Visueller Zustand

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Professionell | Batteriekasten, gesichert, Polabdeckung, Lüftung sichtbar | 0 | visual_high |
| Akzeptabel | Gesichert, Polabdeckung, aber kein geschlossener Kasten | -5 | visual_medium |
| Mangelhaft | Lose Befestigung, keine Polabdeckung | -25 | visual_high |
| Gefährlich | Batterie unsicher, korrodierte Pole, keine Entlüftung | -50 | visual_high |

### T.6 Fußschalter — Visueller Zustand

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Neuwertig | Schalter sauber, Membran intakt, gleichmäßig am Deck montiert | 0 | visual_high |
| Alterung | Membran leicht verfärbt (UV), noch elastisch | -5 | visual_medium |
| Verschlissen | Membran rissig, Gummi hart/spröde | -15 | visual_high |
| Beschädigt | Schalter gebrochen, Wasser unter Membran, lose Montage | -30 | visual_high |

### T.7 Getriebe — Visueller Zustand (nur bei geöffneter Winsch)

| Befund | Visuelle Merkmale | AYDI-Score-Abzug | Confidence |
|--------|-------------------|------------------|------------|
| Gut geschmiert | Gleichmäßiger Fettfilm, keine Metallpartikel sichtbar | 0 | visual_medium |
| Trockenlauf | Blanke Metallflächen, kein Fett sichtbar | -20 | visual_high |
| Verschmutzt | Schmutzpartikel im Fett, dunkle Verfärbung | -15 | visual_medium |
| Verschlissen | Metallspäne im Fett, Abriebspuren an Zahnrädern | -35 | visual_high |
| Korrodiert | Rost auf Getriebekomponenten (nur bei Nicht-Edelstahl) | -40 | visual_high |

---

## ANHANG U — Lebensdauer- und Verschleiß-Referenz {#anhang-u}

### U.1 Erwartete Lebensdauer nach Komponente

| Komponente | Lebensdauer (Stunden) | Lebensdauer (Saisons) | Lebensdauer (Betätigungen) | Bemerkung |
|-----------|----------------------|----------------------|---------------------------|-----------|
| BLDC-Motor | 5.000–15.000 h | 15–30+ | — | Nahezu wartungsfrei |
| Bürstenmotor | 1.500–4.000 h | 8–15 | — | Bürstenwechsel alle 1.000–2.000 h |
| Planetengetriebe | 4.000–10.000 h | 12–25 | — | Regelmäßige Schmierung vorausgesetzt |
| Schneckengetriebe | 3.000–8.000 h | 10–20 | — | Geringerer Wirkungsgrad = mehr Wärme |
| Kupplung | 3.000–6.000 h | 10–18 | 50.000–150.000 | Anlaufkraft belastet am meisten |
| Lager (Motor) | 8.000–20.000 h | 20+ | — | Kugellagerwechsel möglich |
| Lager (Getriebe) | 5.000–12.000 h | 15–25 | — | Nadellager empfindlicher für Salzwasser |
| Controller (Elektronik) | 10.000–20.000 h | 20+ | — | Hauptausfallursache: Feuchtigkeit |
| Fußschalter | — | 8–15 | 30.000–80.000 | UV und mechanische Belastung |
| Kabel (verzinnt) | — | 20–30+ | — | Nur bei mechanischem Schaden |
| Kabelschuhe (gecrimpt) | — | 10–20 | — | Korrosion je nach Umgebung |
| Sicherung | — | 10+ | — | Ersatz bei Auslösung |

**AYDI-Confidence:** benchmark — aggregiert aus Herstellerdaten und Werfterfahrung.

### U.2 Verschleißindikatoren für AYDI-Scoring

| Indikator | Messmethode | Grenzwert „Warnung" | Grenzwert „Kritisch" |
|-----------|-------------|--------------------|--------------------|
| Motorstrom bei Leerlauf | Zangenamperemeter | >30% über Nennwert | >50% über Nennwert |
| Motorstrom unter Last | Zangenamperemeter | >20% über Nennwert | >40% über Nennwert |
| Wicklungswiderstand | Ohmmeter | ±15% vom Sollwert | ±30% vom Sollwert |
| Getriebespiel (radial) | Manuell prüfen | Spürbares Spiel | Sichtbares Spiel >1 mm |
| Laufgeräusch | Subjektiv / dB-Meter | Verändert, +5 dB | Deutlich verändert, +10 dB |
| Temperatur nach 2 min Last | IR-Thermometer | >65°C | >85°C |
| Einschaltdauer bis Abschaltung | Stoppuhr | <80% des Nennwertes | <50% des Nennwertes |
| Freilauf-Drehmoment | Handkurbel | Schwergängig | Blockiert |
| Spannungsabfall Kabel | Multimeter | >3% | >5% |
| Isolationswiderstand | Megohmmeter | <50 MΩ | <10 MΩ |

### U.3 Typische Ausfallverteilung nach Alter

```
Ausfallrate (relativ)
│
│ ██                                              ██ ██
│ ██                                           ██ ██ ██
│ ██ ██                                     ██ ██ ██ ██
│ ██ ██                                  ██ ██ ██ ██ ██
│ ██ ██ ██                            ██ ██ ██ ██ ██ ██
│ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██
└──────────────────────────────────────────────────────────
  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
                         Jahre

Badewannenkurve: 
- Jahr 0–2: Frühausfälle (Installation, Materialfehler)
- Jahr 2–10: Normalbetrieb (niedrigste Ausfallrate)
- Jahr 10+: Verschleißausfälle (steigend)
```

### U.4 Wartungs-ROI-Berechnung

| Wartungsstrategie | Jährl. Kosten | Erwartete Lebensdauer | 15-Jahres-Kosten | Kosten/Jahr |
|-------------------|--------------|----------------------|------------------|-------------|
| Keine Wartung | 0 € | 5–7 Jahre | 2× Austausch ≈ 12.000 € | 800 € |
| Basis (jährlich) | 150 € | 10–15 Jahre | 1× Austausch ≈ 8.250 € | 550 € |
| Profi (halbjährlich) | 350 € | 15–20+ Jahre | 0× Austausch ≈ 5.250 € | 350 € |

**Empfehlung:** Professionelle Wartung hat den besten ROI. Investition in Wartung spart über 15 Jahre bis zu 6.750 €.

---

## ANHANG V — AYDI-Bewertungsmatrix für E-Winschen {#anhang-v}

### V.1 Modulare Bewertungskategorien

Die AYDI-Analyse elektrischer Winschen erfolgt in 8 Bewertungskategorien mit gewichteter Gesamtbewertung:

| Kategorie | Gewicht | Beschreibung |
|-----------|---------|-------------|
| K1: Leistungsdimensionierung | 15% | Winschgröße passt zur Segelfläche und zum Einsatz |
| K2: Elektrik-Qualität | 20% | Kabelquerschnitt, Absicherung, Spannungsabfall |
| K3: Installationsqualität | 15% | Decksdurchführung, Kabelführung, Zugentlastung |
| K4: Steuerung/Bedienung | 10% | Schalterplatzierung, Ergonomie, Totmann-Funktion |
| K5: Zustand Motor/Getriebe | 15% | Verschleiß, Korrosion, Laufverhalten |
| K6: Batterie-Eignung | 10% | Kapazität, Technologie, Absicherung |
| K7: Normenkonformität | 10% | ABYC E-11, ISO 13297, CE-Konformität |
| K8: Wartungszustand | 5% | Schmierung, Reinigung, Dokumentation |

### V.2 Bewertungsskala pro Kategorie

| Score | Bewertung | Handlungsbedarf |
|-------|-----------|----------------|
| 90–100 | Ausgezeichnet | Kein Handlungsbedarf |
| 75–89 | Gut | Geringer Handlungsbedarf, Wartung empfohlen |
| 60–74 | Befriedigend | Mängel vorhanden, Behebung innerhalb der Saison |
| 40–59 | Mangelhaft | Erhebliche Mängel, zeitnahe Behebung empfohlen |
| 20–39 | Ungenügend | Schwerwiegende Mängel, umgehende Maßnahme erforderlich |
| 0–19 | Kritisch | Sicherheitsrelevant, Betrieb nicht empfohlen |

### V.3 Detailbewertung K1: Leistungsdimensionierung

| Prüfpunkt | Methode | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|-----------|---------|------------|-----------|-----------|-----------|----------|
| Winschgröße vs. Segelfläche | Berechnung Abschn. 2.3 | Exakt passend | 1 Größe über | 1 Größe unter | 2+ Größen unter | Völlig unterdimensioniert |
| Zugkraft vs. Schot-Last | Berechnung | >120% Reserve | 100–120% | 80–100% | 60–80% | <60% |
| Liniengeschwindigkeit | Datenblatt | Anforderung erfüllt | Grenzwertig | Zu langsam für Einsatz | — | — |
| Einschaltdauer | Datenblatt vs. Nutzung | ED passt zur Nutzung | Gelegentlich am Limit | Regelmäßig am Limit | Häufige Abschaltung | — |

### V.4 Detailbewertung K2: Elektrik-Qualität

| Prüfpunkt | Methode | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|-----------|---------|------------|-----------|-----------|-----------|----------|
| Kabelquerschnitt | Messen + Berechnung | ≥ Berechnung | Knapp ausreichend | 1 Stufe zu klein | 2+ Stufen zu klein | Gefährlich unterdimensioniert |
| Spannungsabfall unter Last | Messen | <3% | 3–5% | 5–7% | 7–10% | >10% |
| Absicherung | Vergleich Sicherung/Kabel | Korrekt dimensioniert | Leicht überdimensioniert | Stark überdimensioniert | Unterdimensioniert | Keine Sicherung |
| Kabeltyp | Sichtkontrolle | Verzinntes Marinekabel | Verzinntes Standardkabel | Unverzinntes Kabel | Fahrzeugkabel | Ungeeignet |
| Kabelschuhe | Sichtkontrolle | Gecrimpt + Schrumpfschlauch | Gecrimpt ohne Schutz | Gelötet | Quetschverbinder | Lose verdrillt |

### V.5 Detailbewertung K3: Installationsqualität

| Prüfpunkt | Methode | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|-----------|---------|------------|-----------|-----------|-----------|----------|
| Decksdurchführung | Sichtkontrolle | IP68 Durchführung + Sikaflex | Standard-Durchführung | Durchführung ohne Dichtung | Loch im Deck ohne Durchführung | — |
| Motorbefestigung | Sichtkontrolle | Herstellerkit korrekt montiert | Stabile Eigenbau-Halterung | Wackelige Halterung | Lose/unsicher | — |
| Kabelführung | Sichtkontrolle | Kabelkanal + Beschriftung | Kabelbinder, ordentlich | Lose, aber geschützt | Lose + Scheuerstellen | — |
| Kernverstärkung (Deck) | Klopfprobe / Dokumentation | Dokumentiert + GFK-Verstärkung | Verstärkung vorhanden | Nicht dokumentiert | Keine Verstärkung (Sandwich) | — |
| Zugentlastung | Sichtkontrolle | An allen Kabeln | An Hauptkabeln | Teilweise | Keine | — |

### V.6 Gesamtbewertungsformel

```
Gesamt-Score = Σ (Kategorie_Score × Kategorie_Gewicht)

Beispiel:
K1: 85 × 0,15 = 12,75
K2: 70 × 0,20 = 14,00
K3: 60 × 0,15 =  9,00
K4: 90 × 0,10 =  9,00
K5: 75 × 0,15 = 11,25
K6: 80 × 0,10 =  8,00
K7: 65 × 0,10 =  6,50
K8: 50 × 0,05 =  2,50
─────────────────────
Gesamt:           73,00 / 100
→ Bewertung: „Befriedigend"
```

---

## ANHANG W — Vertiefung: Thermomanagement {#anhang-w}

### W.1 Wärmeentwicklung in E-Winschen

Die Verlustleistung in einer E-Winsch verteilt sich wie folgt:

| Komponente | Verlustanteil | Typische Temperatur | Max. zulässige Temp. |
|-----------|--------------|--------------------|--------------------|
| Motor (BLDC) | 15–25% der Eingangsleistung | 50–80°C | 120°C (Isolationsklasse B) |
| Motor (Bürstenmotor) | 25–40% der Eingangsleistung | 60–95°C | 130°C (Isolationsklasse B) |
| Controller | 3–8% der Eingangsleistung | 40–65°C | 85°C (Elektronik) |
| Getriebe (Planetar) | 5–15% der Eingangsleistung | 35–55°C | 80°C (Fett-Grenzwert) |
| Getriebe (Schnecke) | 20–40% der Eingangsleistung | 45–75°C | 80°C (Fett-Grenzwert) |
| Kabel (bei korrektem Querschnitt) | 1–3% der Eingangsleistung | <40°C | 70°C (Isolierung) |

### W.2 Belüftungsberechnung

Mindest-Querschnitt der Zu-/Abluftöffnung für natürliche Konvektion:

```
A_min [cm²] = P_verlust [W] / (k × ΔT)

Wobei:
  k = 0,5 W/(cm² × K) für natürliche Konvektion
  ΔT = T_max_zulässig - T_umgebung (typisch 25°C)

Beispiel: 
  Motor 1.200 W, Verlust 25% = 300 W
  T_max = 80°C, T_umgebung = 35°C (Tropen)
  ΔT = 45 K
  A_min = 300 / (0,5 × 45) = 13,3 cm²
  → Min. Lüftungsöffnung: ∅ ~42 mm oder 2× ∅ 30 mm
```

### W.3 Einschaltdauer-Korrekturfaktoren

Die Einschaltdauer (ED) des Herstellers gilt für Referenzbedingungen (25°C, Nennlast). Korrekturfaktoren:

| Bedingung | Faktor | Beispiel |
|-----------|--------|---------|
| Umgebungstemperatur 25°C | 1,00 | Nordsee, Herbst |
| Umgebungstemperatur 30°C | 0,90 | Mittelmeer, Sommer |
| Umgebungstemperatur 35°C | 0,80 | Tropen, geschlossener Raum |
| Umgebungstemperatur 40°C | 0,65 | Motorraum, Tropen |
| Umgebungstemperatur 45°C | 0,50 | Kritisch! Zusatzbelüftung nötig |
| Nennlast 50% | 1,40 | Leichte Segelmanöver |
| Nennlast 75% | 1,15 | Normales Reffen |
| Nennlast 100% | 1,00 | Volle Belastung |
| Nennlast 120% (Kurzzeitspitze) | 0,70 | Schwerwetter, Böe |
| Schlechte Belüftung (Einbaukasten) | 0,75 | Ohne Lüftungsöffnungen |
| Gute Belüftung (offen unter Deck) | 1,10 | Freie Luftzirkulation |
| Aktive Kühlung (Lüfter) | 1,30 | Leistungswinschen |

### W.4 NTC-Temperatursensor-Referenzwerte

Der NTC-Sensor (Negative Temperature Coefficient) im Motor meldet die Wicklungstemperatur an den Controller.

| Temperatur [°C] | Widerstand [kΩ] (10kΩ NTC) | Status |
|-----------------|---------------------------|--------|
| 20 | 12,5 | Kalt (Normalbetrieb) |
| 25 | 10,0 | Referenzwert |
| 30 | 8,1 | Normalbetrieb |
| 40 | 5,3 | Normalbetrieb unter Last |
| 50 | 3,6 | Warnung (Controller LED gelb) |
| 60 | 2,5 | Warnung (Leistungsreduzierung) |
| 70 | 1,7 | Warnung (starke Leistungsreduzierung) |
| 80 | 1,2 | Abschaltung (die meisten Controller) |
| 90 | 0,9 | Sicherheitsabschaltung |
| 100 | 0,6 | Thermischer Cutoff (Hardware-Schutz) |

**Diagnose:** Bei defektem NTC liest der Controller ∞ Ω (offener Kontakt) → Fehlermeldung oder Dauerlauf ohne Schutz (je nach Controller-Firmware).

---

## ANHANG X — Vertiefung: CAN-Bus und NMEA2000-Integration {#anhang-x}

### X.1 NMEA2000-PGN für E-Winschen

Es gibt keinen dedizierten NMEA2000-PGN für Winschen. Hersteller nutzen proprietäre PGNs oder gruppieren unter allgemeinen Kategorien:

| PGN | Name | Relevanz für E-Winschen |
|-----|------|------------------------|
| 127501 | Binary Status Report | Ein/Aus-Status der Winsch |
| 127502 | Switch Bank Control | Steuerung über MFD |
| 127508 | Battery Status | Batteriespannung/-strom (relevant für Kapazitätsüberwachung) |
| 130316 | Temperature Extended | Motortemperatur (wenn herstellerseitig implementiert) |
| 65280–65535 | Proprietäre PGNs | Herstellerspezifische Daten (Harken, Lewmar) |

### X.2 Harken CAN-Bus-Integration

Harken Performa-Serie mit CAN-Bus (ab 2022):
- Protokoll: CANopen-basiert (nicht NMEA2000-nativ)
- Gateway: Harken CAN-NMEA2000-Bridge (Art. EWCAN2K, ca. 450 €)
- Daten vom Motor: Temperatur, Strom, Drehzahl, Fehlerstatus
- Steuerung über CAN: Ein/Aus, Speed 1/Speed 2
- Kabeltyp: CAN-Bus M12 5-pol (DeviceNet Micro)
- Max. Buslänge: 100 m (bei 250 kbit/s)
- Terminierung: 120 Ω Abschlusswiderstand an beiden Enden

### X.3 Lewmar CAN-Bus-Integration

Lewmar E-Serie mit CAN-Bus (ab 2023):
- Protokoll: NMEA2000-nativ (Zertifizierung in Arbeit, Stand 2025)
- Daten: Laststrom, Temperatur, Betriebsstunden, Fehlerspeicher
- Steuerung: Über MFD oder Lewmar-App (Bluetooth-Gateway optional)
- Kabeltyp: NMEA2000 Micro-C (M12 5-pol)
- Adressierung: Automatisch (ISO 11783 Address Claim)

### X.4 Antal XT-E Smart-Integration

Antal XT-E mit Kraftsensor und CAN:
- Protokoll: Proprietär (Antal Smart Protocol)
- Daten: Leinenzug [kg] in Echtzeit, Motorstrom, Temperatur
- Gateway: Antal Smart Hub → NMEA2000 (PGN 127501/130316)
- Besonderheit: Kraftbasierte Automatik (max. Leinenzug einstellbar)
- App: Antal XT-E App (iOS/Android) via Bluetooth Low Energy

### X.5 Verdrahtungsschema CAN-Bus

```
┌─────────────┐     CAN-H/CAN-L     ┌──────────────┐     NMEA2000     ┌──────────────┐
│   E-Winsch   ├────────────────────►│  CAN-Bridge   ├───────────────►│     MFD      │
│   (Motor-    │     (geschirmtes    │  (Hersteller- │    Backbone    │  (Plotter)   │
│   Controller)│      Kabel)        │   spezifisch) │               │              │
└─────────────┘                      └──────────────┘               └──────────────┘
                                           │
                                     120 Ω Terminierung
                                     (an beiden Busenden)

Kabelspezifikation CAN-Bus:
- Typ: Geschirmtes Twisted-Pair
- Querschnitt: 0,5–0,75 mm² (Signal), Schirm auf Masse (nur ein Ende!)
- Stecker: M12 5-pol (DeviceNet Micro) oder NMEA2000 Micro-C
- Max. Stichlänge: 6 m (NMEA2000-Spezifikation)
- Max. Backbone: 100 m
```

---

## ANHANG Y — Vertiefung: Sicherheitskonzepte {#anhang-y}

### Y.1 Sicherheitskette einer E-Winsch

```
Stufe 1: Totmann-Fußschalter
  └─ Loslassen = sofortiger Stopp
  └─ Mechanisch (Öffner-Kontakt, fail-safe)

Stufe 2: Controller-Strombegrenzung
  └─ Max. Motorstrom begrenzt (Software/Hardware)
  └─ Rampensteuerung beim Anlauf (Soft-Start)

Stufe 3: Thermischer Schutz (NTC)
  └─ Temperaturüberwachung der Motorwicklung
  └─ Automatische Abschaltung bei Übertemperatur
  └─ Automatische Wiedereinschaltung nach Abkühlung

Stufe 4: Hauptsicherung / Circuit Breaker
  └─ Schutz der Verkabelung (nicht des Motors!)
  └─ Träge Auslegung (Anlaufstrom berücksichtigen)
  └─ Rückstellbar (CB) oder Schmelzsicherung (ANL/MEGA)

Stufe 5: Batterie-Hauptschalter
  └─ Manuelle Trennung der gesamten Anlage
  └─ Notabschaltung bei Kabelbrand o.Ä.

Stufe 6: Mechanischer Freilauf
  └─ Winsch immer manuell bedienbar (Kurbel)
  └─ Unabhängig von Elektrik
  └─ Kritische Sicherheitsfunktion bei Stromausfall
```

### Y.2 Gefahrenanalyse nach Risikomatrix

| Gefährdung | Wahrscheinlichkeit | Schwere | Risiko | Schutzmaßnahme |
|-----------|-------------------|---------|--------|---------------|
| Leinenriss unter Last | Mittel | Hoch (Verletzung) | Hoch | Kraftbegrenzung, Sicherungsbereich |
| Fingereinzug an Trommel | Niedrig (Self-Tailing) | Hoch | Mittel | Totmannschalter, Schutzring |
| Kabelbrand | Sehr niedrig | Sehr hoch | Mittel | Korrekte Absicherung, Kabelquerschnitt |
| Motorüberhitzung | Niedrig | Mittel | Niedrig | NTC + automatische Abschaltung |
| Batterie-Entgasung | Sehr niedrig | Hoch | Niedrig | Belüftung, geschlossener Batteriekasten |
| Stromschlag (24V) | Extrem niedrig | Niedrig | Minimal | 24V DC nicht lebensbedrohlich |
| Ausfall auf See | Mittel | Niedrig | Niedrig | Manueller Betrieb immer möglich |
| Korrosion → Kurzschluss | Niedrig | Mittel | Niedrig | Marine-Kabel, IP68-Durchführungen |

### Y.3 Sicherheitsrelevante Prüfungen nach Installation

| Nr. | Prüfung | Methode | Akzeptanzkriterium | Pflicht |
|-----|---------|---------|-------------------|---------|
| S1 | Totmannfunktion | Loslassen → Motor stoppt | <0,5 s Reaktionszeit | Ja |
| S2 | Sicherung löst bei Kurzschluss | Kontrollierter Kurzschlusstest (Nur Fachkraft!) | Sicherung löst <2 s | Ja |
| S3 | Freilauf funktioniert | Kurbel einsetzen, manuell drehen | Freies Drehen in beide Richtungen | Ja |
| S4 | Decksdurchführung dicht | Wassertest (Schlauch 5 min) | Kein Wassereinbruch | Ja |
| S5 | Kabel-Zugentlastung | Zugversuch (~10 kg) an jedem Kabel | Kein Lockern | Ja |
| S6 | Isolationswiderstand | Megohmmeter 500V DC | >50 MΩ | Empfohlen |
| S7 | Spannungsabfall unter Volllast | Multimeter an Batterie + Motor | <3% (24V: <0,72V) | Ja |
| S8 | Not-Aus-Funktion | Batterie-Hauptschalter betätigen | Sofortiger Stopp aller Winschen | Ja |
| S9 | Drehrichtung korrekt | Probelauf mit Leine | CW = Einholen | Ja |
| S10 | Geräuschpegel | Subjektiv / dB-Meter | Kein Schleifen, kein Klacken | Ja |

---

## ANHANG Z — Erweiterte Troubleshooting-Referenz {#anhang-z}

### Z.1 Fehlercode-Tabelle (Harken Performa Controller)

| LED-Muster | Code | Bedeutung | Maßnahme |
|-----------|------|-----------|----------|
| Grün dauerhaft | OK | Betriebsbereit | — |
| Grün blinkend (1 Hz) | STDBY | Standby, kein Signal | Fußschalter betätigen |
| Gelb dauerhaft | TEMP | Temperaturwarnung | Pause, Belüftung prüfen |
| Gelb blinkend | ILIM | Strombegrenzung aktiv | Last reduzieren |
| Rot 1× blinken | E01 | Überstrom (Hardware) | Motor/Kabel prüfen |
| Rot 2× blinken | E02 | Überspannung (>32V bei 24V) | Laderegler prüfen |
| Rot 3× blinken | E03 | Unterspannung (<18V bei 24V) | Batterie laden |
| Rot 4× blinken | E04 | NTC-Sensor offen | NTC-Anschluss prüfen |
| Rot 5× blinken | E05 | Übertemperatur (Hardware-Cutoff) | Abkühlen lassen, Ursache finden |
| Rot 6× blinken | E06 | Motorwicklung Kurzschluss | Motor ersetzen |
| Rot dauerhaft | FATAL | Interner Controller-Fehler | Controller ersetzen |

### Z.2 Fehlercode-Tabelle (Lewmar E-Serie Controller)

| Display | Code | Bedeutung | Maßnahme |
|---------|------|-----------|----------|
| — (aus) | — | Kein Strom | Versorgung prüfen |
| „rdy" | — | Betriebsbereit | — |
| „OC" | Overcurrent | Überstrom erkannt | Motor / Verkabelung prüfen |
| „OV" | Overvoltage | Überspannung | Laderegler, Lichtmaschine prüfen |
| „UV" | Undervoltage | Unterspannung | Batterie laden / Kabel prüfen |
| „OT" | Overtemperature | Übertemperatur Motor | Abkühlen, Belüftung verbessern |
| „CT" | Controller Temp | Controller zu heiß | Belüftung Controller verbessern |
| „SE" | Sensor Error | NTC / Hall-Sensor defekt | Sensor prüfen / ersetzen |
| „CE" | Communication | CAN-Bus-Fehler | Busverkabelung, Terminierung prüfen |
| „EE" | EEPROM Error | Speicherfehler | Werksreset oder Controller ersetzen |

### Z.3 Spannungsabfall-Diagnose (Schritt-für-Schritt)

```
Benötigtes Werkzeug: Multimeter (DC), Zangenamperemeter

Messstellen:
  (A) Batteriepole
  (B) Hauptsicherung (Ein- und Ausgang)
  (C) Batterie-Hauptschalter (Ein- und Ausgang)
  (D) Controller-Eingang
  (E) Motor-Klemmen

Vorgehensweise:
1. Winsch unter Last laufen lassen (Segel gerefft oder Schot belegt)
2. Gleichzeitig messen:
   - U(A): Batteriespannung unter Last
   - U(E): Spannung am Motor unter Last
   - I: Strom (Zangenamperemeter)

3. Spannungsabfall berechnen:
   ΔU_gesamt = U(A) - U(E)
   ΔU_gesamt% = ΔU_gesamt / U(A) × 100

4. Wenn ΔU > 3%: Abschnittsweise eingrenzen:
   ΔU(A→B) = U(A) - U(B_ein)  → Kabel Batterie→Sicherung
   ΔU(B)   = U(B_ein) - U(B_aus) → Sicherungskontakt (soll <0,1V)
   ΔU(B→C) = U(B_aus) - U(C_ein) → Kabel Sicherung→Hauptschalter
   ΔU(C)   = U(C_ein) - U(C_aus) → Hauptschalter (soll <0,1V)
   ΔU(C→D) = U(C_aus) - U(D)    → Kabel Hauptschalter→Controller
   ΔU(D→E) = U(D) - U(E)        → Controller intern + Kabel→Motor

5. Höchster Einzelabfall = Schwachstelle → beheben
```

### Z.4 Motorwicklungs-Diagnose

| Motor-Typ | Wicklungs-Konfiguration | Mess-Methode | Soll-Wert | Fehler-Indikator |
|-----------|------------------------|-------------|-----------|-----------------|
| Bürstenmotor | 2 Anschlüsse | Ohmmeter zwischen + und - | 0,1–1,0 Ω | <0,05 Ω = Kurzschluss; ∞ = Unterbrechung |
| BLDC 3-Phasen | 3 Anschlüsse (U, V, W) | Ohmmeter U↔V, V↔W, U↔W | Alle 3 gleich (±10%) | Ungleich = Windungsschluss; ∞ = Unterbrechung |
| BLDC (Sternschaltung) | 3 Anschlüsse | Wie oben | R(U↔V) = R(V↔W) = R(U↔W) | — |
| BLDC (Dreieckschaltung) | 3 Anschlüsse | Wie oben, aber R/1,5 | Alle gleich | — |

**Isolationsprüfung:**
- Megohmmeter 500V DC zwischen jeder Wicklung und Gehäuse (Masse)
- Soll: >50 MΩ (trocken), >10 MΩ (nach Feuchtigkeit, Grenzwert)
- <1 MΩ: Motor muss ersetzt werden (Isolationsversagen)

### Z.5 Geräusch-Diagnose-Tabelle

| Geräusch | Frequenz | Lastabhängig? | Wahrscheinliche Ursache | Dringlichkeit |
|----------|----------|--------------|------------------------|--------------|
| Helles Summen | Hoch (>1 kHz) | Ja | BLDC-Kommutierung (normal) | Keine |
| Tiefes Brummen | Niedrig (<200 Hz) | Nein | Controller-PWM-Frequenz | Gering |
| Rhythmisches Klacken | Mittel | Ja, periodisch | Zahnradschaden im Getriebe | Hoch — zeitnah prüfen |
| Sporadisches Klacken | — | Nur beim Anlauf | Kupplungsspiel | Mittel |
| Dauerhaftes Schleifen | Konstant | Leicht | Fremdkörper oder trockenes Lager | Mittel |
| Metallisches Kreischen | Hoch | Ja | Schwerer Lagerschaden | Hoch — sofort stoppen |
| Knistern/Funken | Unregelmäßig | Ja | Bürstenverschleiß (nur Bürstenmotor) | Mittel |
| Pfeifen unter Last | Variabel | Stark | Getriebeschmierung mangelhaft | Mittel |
| Klopfen bei Richtungswechsel | Kurz | Nein | Getriebeumkehrspiel | Gering (normal) |
| Summen ohne Drehbewegung | Konstant | — | Motor blockiert (Getriebe, Fremdkörper) | Hoch — sofort abschalten |

---

## ANHANG AA — Retrofit-Checkliste für AYDI-Bewertung {#anhang-aa}

### AA.1 Vor-Ort-Datenerfassung (Level 2 Analyse)

Diese Checkliste dient der systematischen Erfassung aller relevanten Daten für eine AYDI Level-2-Bewertung einer E-Winschen-Installation oder eines Retrofit-Projekts.

```
╔══════════════════════════════════════════════════════════════════╗
║  AYDI E-WINSCHEN — VOR-ORT-DATENERFASSUNG                      ║
║  Formular-Version: 1.0.0 | Datum: ____________                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  1. BOOT-DATEN                                                   ║
║  Typ: ______________________ Baujahr: ________                   ║
║  LOA: _______ m  Beam: _______ m  Deplacement: _______ kg       ║
║  Rigg: □ Sloop □ Kutter □ Ketsch □ Yawl □ Kat                   ║
║  Groß: _______ m²  Genua: _______ m²  Spi: _______ m²          ║
║  CE-Kategorie: □ A □ B □ C □ D                                   ║
║                                                                  ║
║  2. BORDNETZ                                                     ║
║  Spannung: □ 12V □ 24V □ 48V                                    ║
║  Service-Bank: _______ Ah, Typ: □ AGM □ Gel □ LiFePO4 □ Blei   ║
║  Starter-Bank: _______ Ah                                        ║
║  Ladung: □ Lichtmaschine ___A □ Landstrom ___A □ Solar ___W     ║
║         □ Windgenerator ___W □ Hydrogenerator                    ║
║  Hauptschalter: □ Ja □ Nein, Typ: ______________________        ║
║                                                                  ║
║  3. BESTEHENDE WINSCHEN                                          ║
║  Genua BB: Marke ____________ Größe ____ □ manuell □ elektrisch  ║
║  Genua SB: Marke ____________ Größe ____ □ manuell □ elektrisch  ║
║  Großschot: Marke ____________ Größe ____ □ manuell □ elektrisch ║
║  Fall: Marke ____________ Größe ____ □ manuell □ elektrisch      ║
║  Sonstige: ________________________________________________      ║
║                                                                  ║
║  4. PLATZVERHÄLTNISSE (unter Deck, je Winsch)                    ║
║  Winsch 1: Tiefe ___mm, Breite ___mm, Zugang: □gut □eng □kein   ║
║  Winsch 2: Tiefe ___mm, Breite ___mm, Zugang: □gut □eng □kein   ║
║  Winsch 3: Tiefe ___mm, Breite ___mm, Zugang: □gut □eng □kein   ║
║  Winsch 4: Tiefe ___mm, Breite ___mm, Zugang: □gut □eng □kein   ║
║                                                                  ║
║  5. DECKSKONSTRUKTION (je Winsch-Position)                       ║
║  Winsch 1: □ Volllaminat ___mm □ Sandwich, Kern: __________     ║
║  Winsch 2: □ Volllaminat ___mm □ Sandwich, Kern: __________     ║
║  Winsch 3: □ Volllaminat ___mm □ Sandwich, Kern: __________     ║
║  Winsch 4: □ Volllaminat ___mm □ Sandwich, Kern: __________     ║
║  Kernverstärkung vorhanden? □ Ja □ Nein □ Unbekannt              ║
║                                                                  ║
║  6. KABELWEG (Batterie → jede Winsch)                            ║
║  Winsch 1: Entfernung ___m, Hindernisse: _____________________   ║
║  Winsch 2: Entfernung ___m, Hindernisse: _____________________   ║
║  Winsch 3: Entfernung ___m, Hindernisse: _____________________   ║
║  Winsch 4: Entfernung ___m, Hindernisse: _____________________   ║
║  Kabeldurchführungen möglich? □ Schott 1 □ Schott 2 □ Deck      ║
║                                                                  ║
║  7. MESSUNGEN (nur bei bestehender E-Winsch-Installation)        ║
║  Batteriespannung (Ruhe): _______ V                              ║
║  Batteriespannung (unter Last): _______ V                        ║
║  Motorstrom (Leerlauf): _______ A                                ║
║  Motorstrom (unter Last): _______ A                              ║
║  Spannungsabfall (Batterie→Motor): _______ V = _______ %        ║
║  Motortemperatur nach 2 min Last: _______ °C                     ║
║  Geräuschpegel: □ normal □ verändert, Art: _________________     ║
║  Thermische Abschaltung: □ Nein □ Ja, nach _______ s            ║
║                                                                  ║
║  8. FOTOS (für Pipeline B — Visuelle Analyse)                    ║
║  □ Foto 1: Deck mit Winschen (Übersicht)                        ║
║  □ Foto 2: Jede Winsch Detail (Oberfläche, Schalter)            ║
║  □ Foto 3: Unter Deck: Motor/Controller (je Winsch)             ║
║  □ Foto 4: Batterie-Installation                                 ║
║  □ Foto 5: Kabelführung (kritischste Stelle)                     ║
║  □ Foto 6: Sicherungspaneel                                      ║
║  □ Foto 7: Decksdurchführung (Detail)                            ║
║  □ Foto 8: Typenschild Motor + Controller                        ║
║                                                                  ║
║  9. BESONDERHEITEN / MÄNGEL                                      ║
║  ____________________________________________________________    ║
║  ____________________________________________________________    ║
║  ____________________________________________________________    ║
║                                                                  ║
║  Erfasser: __________________ Datum: __________                  ║
║  AYDI-Confidence: □ measured □ visual_high □ estimated           ║
╚══════════════════════════════════════════════════════════════════╝
```

### AA.2 Retrofit-Entscheidungsmatrix

| Kriterium | Gewicht | Ergebnis positiv (+) | Ergebnis negativ (-) |
|-----------|---------|---------------------|---------------------|
| Platz unter Deck | 20% | >250 mm Tiefe verfügbar | <150 mm, kein Einbau möglich |
| Batteriekapazität | 15% | >200 Ah Service-Bank | <100 Ah, Upgrade nötig |
| Kabelweg | 15% | <5 m, direkt, wenige Schotten | >8 m, viele Hindernisse |
| Deckskonstruktion | 15% | Volllaminat >18 mm oder Sandwich mit Verstärkung | Dünnes Sandwich ohne Verstärkung |
| Budget | 10% | Retrofit-Kit + Installation < Neuwinsch | Retrofit teurer als Neuwinsch |
| Bestehende Winsch | 10% | Herstellerkit verfügbar | Keine Retrofit-Option |
| Ladekapazität | 10% | Ausreichend für Zusatzverbrauch | Unzureichend, Generator nötig |
| Nutzungsprofil | 5% | Langfahrt, ältere Crew, Einhandsegler | Regatta, junge Crew, Kurzstrecke |

**Bewertung:**
- Summe >70%: Retrofit empfohlen
- Summe 50–70%: Retrofit möglich, Einzelfall prüfen
- Summe <50%: Retrofit nicht empfohlen, ggf. kompletter Winschentausch

### AA.3 Kostenvergleich Retrofit vs. Neuwinsch

| Szenario | Retrofit (2 Genua-Winschen) | Neuwinsch (2 E-Winschen) |
|----------|---------------------------|--------------------------|
| Winsch/Kit-Kosten | 2× Motor-Kit: 3.000–5.000 € | 2× E-Winsch komplett: 6.000–12.000 € |
| Demontage alte Winsch | 0 € (bleibt) | 200–400 € |
| Decksvorbereitung | 200–400 € (Kernverstärkung) | 400–800 € (neue Löcher) |
| Elektrik (Kabel, Sicherung) | 600–1.200 € | 600–1.200 € |
| Installation Arbeitszeit | 8–12 h × 80 € = 640–960 € | 12–20 h × 80 € = 960–1.600 € |
| **Gesamt** | **4.440–7.560 €** | **8.160–16.000 €** |
| **Ersparnis Retrofit** | **ca. 45–55%** | — |

**Einschränkung:** Retrofit nur sinnvoll, wenn bestehende Winsch mechanisch intakt und kompatibles Kit verfügbar.

---

## ANHANG AB — Erweiterte Pydantic v2 Modelle {#anhang-ab}

```python
"""
AYDI Pydantic v2 Models — Erweiterte Modelle für E-Winschen-Bewertung
Module: 09_06_elektrische_winschen (Ergänzung zu ANHANG J)
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class InspectionType(str, Enum):
    """Art der Inspektion."""
    VISUAL_ONLY = "visual_only"
    BASIC_MEASUREMENT = "basic_measurement"
    FULL_MEASUREMENT = "full_measurement"
    RETROFIT_ASSESSMENT = "retrofit_assessment"


class MaintenanceAction(str, Enum):
    """Wartungsmaßnahme."""
    LUBRICATION = "lubrication"
    BEARING_REPLACEMENT = "bearing_replacement"
    BRUSH_REPLACEMENT = "brush_replacement"
    CABLE_REPAIR = "cable_repair"
    CONTROLLER_REPLACEMENT = "controller_replacement"
    MOTOR_REPLACEMENT = "motor_replacement"
    GEARBOX_OVERHAUL = "gearbox_overhaul"
    SEAL_REPLACEMENT = "seal_replacement"
    FOOT_SWITCH_REPLACEMENT = "foot_switch_replacement"
    CORROSION_TREATMENT = "corrosion_treatment"
    FULL_SERVICE = "full_service"


class RetrofitDecision(str, Enum):
    """Retrofit-Empfehlung."""
    RECOMMENDED = "recommended"
    POSSIBLE_WITH_RESERVATIONS = "possible_with_reservations"
    NOT_RECOMMENDED = "not_recommended"
    NOT_POSSIBLE = "not_possible"


class ThermalMeasurement(BaseModel):
    """Thermische Messung einer E-Winsch."""

    model_config = {"from_attributes": True}

    ambient_temp_c: float = Field(..., ge=-20, le=60, description="Umgebungstemperatur [°C]")
    motor_temp_after_2min_c: Optional[float] = Field(
        None, ge=0, le=200, description="Motortemperatur nach 2 min Volllast [°C]"
    )
    controller_temp_c: Optional[float] = Field(
        None, ge=0, le=150, description="Controller-Temperatur [°C]"
    )
    time_to_cutoff_s: Optional[float] = Field(
        None, ge=0, description="Zeit bis thermische Abschaltung [s]"
    )
    ventilation_adequate: bool = Field(True, description="Belüftung ausreichend?")
    confidence: str = Field("measured", pattern="^(measured|estimated)$")


class ElectricalMeasurement(BaseModel):
    """Elektrische Messung einer E-Winschen-Installation."""

    model_config = {"from_attributes": True}

    battery_voltage_rest_v: float = Field(..., ge=0, le=60, description="Batteriespannung Ruhe [V]")
    battery_voltage_load_v: float = Field(..., ge=0, le=60, description="Batteriespannung unter Last [V]")
    motor_voltage_load_v: float = Field(..., ge=0, le=60, description="Motorspannung unter Last [V]")
    current_no_load_a: float = Field(..., ge=0, le=300, description="Strom Leerlauf [A]")
    current_full_load_a: float = Field(..., ge=0, le=300, description="Strom Volllast [A]")
    voltage_drop_v: float = Field(..., ge=0, description="Spannungsabfall gesamt [V]")
    voltage_drop_percent: float = Field(..., ge=0, le=100, description="Spannungsabfall [%]")
    cable_cross_section_mm2: float = Field(..., ge=0, description="Kabelquerschnitt [mm²]")
    cable_length_m: float = Field(..., ge=0, description="Kabellänge (einfach) [m]")
    fuse_rating_a: float = Field(..., ge=0, description="Sicherungsgröße [A]")
    insulation_resistance_mohm: Optional[float] = Field(
        None, ge=0, description="Isolationswiderstand [MΩ]"
    )
    confidence: str = Field("measured")

    @field_validator("voltage_drop_percent")
    @classmethod
    def validate_voltage_drop(cls, v: float) -> float:
        """Warnung bei hohem Spannungsabfall."""
        if v > 10:
            raise ValueError("Spannungsabfall >10% — Messfehler oder kritischer Kabeldefekt")
        return v


class WinchConditionScore(BaseModel):
    """AYDI-Zustandsbewertung einer E-Winsch (8 Kategorien)."""

    model_config = {"from_attributes": True}

    k1_dimensioning: float = Field(..., ge=0, le=100, description="K1: Leistungsdimensionierung")
    k2_electrical: float = Field(..., ge=0, le=100, description="K2: Elektrik-Qualität")
    k3_installation: float = Field(..., ge=0, le=100, description="K3: Installationsqualität")
    k4_controls: float = Field(..., ge=0, le=100, description="K4: Steuerung/Bedienung")
    k5_motor_gearbox: float = Field(..., ge=0, le=100, description="K5: Zustand Motor/Getriebe")
    k6_battery: float = Field(..., ge=0, le=100, description="K6: Batterie-Eignung")
    k7_compliance: float = Field(..., ge=0, le=100, description="K7: Normenkonformität")
    k8_maintenance: float = Field(..., ge=0, le=100, description="K8: Wartungszustand")

    @property
    def overall_score(self) -> float:
        """Gewichteter Gesamtscore."""
        return (
            self.k1_dimensioning * 0.15
            + self.k2_electrical * 0.20
            + self.k3_installation * 0.15
            + self.k4_controls * 0.10
            + self.k5_motor_gearbox * 0.15
            + self.k6_battery * 0.10
            + self.k7_compliance * 0.10
            + self.k8_maintenance * 0.05
        )

    @property
    def rating(self) -> str:
        """Bewertungsstufe als Text."""
        score = self.overall_score
        if score >= 90:
            return "Ausgezeichnet"
        elif score >= 75:
            return "Gut"
        elif score >= 60:
            return "Befriedigend"
        elif score >= 40:
            return "Mangelhaft"
        elif score >= 20:
            return "Ungenügend"
        return "Kritisch"


class RetrofitAssessment(BaseModel):
    """Retrofit-Bewertung für eine Yacht."""

    model_config = {"from_attributes": True}

    boat_type: str
    boat_year: int = Field(..., ge=1970, le=2030)
    boat_loa_m: float = Field(..., ge=5, le=50)
    space_below_deck_mm: float = Field(..., ge=0, description="Tiefe unter Deck [mm]")
    deck_construction: str = Field(
        ..., pattern="^(solid_laminate|sandwich_reinforced|sandwich_unreinforced)$"
    )
    deck_thickness_mm: float = Field(..., ge=0, description="Decksdicke [mm]")
    cable_distance_m: float = Field(..., ge=0, description="Kabelweg Batterie→Winsch [m]")
    battery_capacity_ah: float = Field(..., ge=0)
    charging_capacity_a: float = Field(..., ge=0, description="Ladekapazität [A]")
    retrofit_kit_available: bool
    existing_winch_condition: str = Field(
        ..., pattern="^(excellent|good|fair|poor)$"
    )
    decision: RetrofitDecision
    decision_reasons: list[str] = Field(default_factory=list)
    estimated_total_cost_eur: Optional[float] = Field(None, ge=0)
    estimated_installation_hours: Optional[float] = Field(None, ge=0)
    confidence: str = Field("estimated")
    assessment_date: date = Field(default_factory=date.today)


class MaintenanceRecord(BaseModel):
    """Wartungsprotokoll für eine E-Winsch."""

    model_config = {"from_attributes": True}

    winch_id: str = Field(..., description="Eindeutige Winschen-ID im Projekt")
    date_performed: date
    performed_by: str
    action: MaintenanceAction
    description: str
    parts_replaced: list[str] = Field(default_factory=list)
    cost_eur: Optional[float] = Field(None, ge=0)
    operating_hours_at_service: Optional[float] = Field(None, ge=0)
    next_service_due: Optional[date] = None
    notes: Optional[str] = None
```

---

> **Ende der Wissensdatei 09.06**
> **AYDI Research** — Version 1.1.0 — 2026-04-25
> **Nächste geplante Aktualisierung:** 2026-10-25
> **Feedback:** research@aydi.io
