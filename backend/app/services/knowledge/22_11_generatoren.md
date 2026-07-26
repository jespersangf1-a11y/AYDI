# 22.11 — Generatoren und Stromerzeuger

> **AYDI Wissensdatei 22.11** — Kategorie 22: Elektrische Energieerzeugung an Bord
> **Confidence-Quelle:** measured (Hersteller-TDS, Leistungskurven, Typenpruefung), documented (ISO/DIN-Normen, Klassegesellschaften, CE-Konformitaet), estimated (Erfahrungswerte, Surveyor-Konsens, Werft-Berichte)
> **Letzte Aktualisierung:** 2026-05-08

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbaeume](#7-troubleshooting-entscheidungsbaeume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A-H — Fallstudien](#11-anhang-a-h-fallstudien)
12. [ANHANG I-R — Pydantic v2 Modelle](#12-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Der Generator als zentrale Energiequelle

Der Bordgenerator ist das Rueckgrat der elektrischen Energieversorgung auf Yachten, sobald die Batteriekapazitaet und regenerative Quellen (Solar, Wind) den Bordverbrauch nicht mehr decken. Ab einer systematischen Verbrauchsleistung von circa 2.500–3.000 Wh/Tag wird ein Generator zur wirtschaftlichen Notwendigkeit — insbesondere bei Klimaanlage, Wassermacher, elektrischem Kochen oder intensiver Elektroniknutzung.

**Dimensionierungsprinzip:**

| Bootsklasse | Typischer Tagesverbrauch | Generator-Empfehlung | Laufzeit/Tag |
|---|---|---|---|
| Segelyacht 8–10 m (Fahrtensegler) | 1.500–3.000 Wh | 2–3 kW oder Hydrogenerator | 1–2 h |
| Segelyacht 12–15 m (Blauwasser) | 3.000–8.000 Wh | 4–6 kW | 2–4 h |
| Motoryacht 10–14 m | 5.000–15.000 Wh | 6–8 kW | 3–5 h |
| Motoryacht 16–22 m | 15.000–40.000 Wh | 8–17 kW | 4–8 h |
| Superyacht 24–40 m | 40.000–150.000 Wh | 20–80 kW (2× redundant) | 12–24 h |
| Megayacht 40+ m | 150.000–500.000+ Wh | 80–350 kW (3× redundant) | 24 h |

**Kernaussage:** Die Generatorleistung muss mindestens 125% der maximalen Gleichzeitlast betragen. Ein unterdimensionierter Generator laeuft permanent im Hochlastbereich, was Lebensdauer drastisch reduziert und Kraftstoffverbrauch erhoet. Ein ueberdimensionierter Generator laeuft im unwirtschaftlichen Teillastbereich und neigt zu Nasslauf (wet stacking).

### 1.2 Abgrenzung dieser Wissensdatei

Diese Datei ergaenzt die bestehenden AYDI-Wissensdateien:
- **22_01** (Elektrik Grundlagen): Bordnetz-Architektur, Spannungsebenen
- **22_02** (Batterien): Speicherkapazitaet, Lade-Entlade-Zyklen
- **22_04** (Ladegeraete/Laderegler): Ladeprofile, Ladequellen-Management
- **22_05** (Solaranlage): Photovoltaik als Ergaenzung
- **22_06** (Windgenerator): Windenergie als Ergaenzung
- **22_07** (Wechselrichter/Landstrom): AC-Verteilung, Shore Power

Die vorliegende Datei 22_11 fokussiert auf:
- **Diesel-Generatoren** (konventionell und variable Drehzahl)
- **Hydrogeneratoren** (Schleppgeneratoren fuer Segelyachten)
- **Brennstoffzellen** (Methanol, Wasserstoff, EFOY, PEM)
- **DC-Generatoren** (Hochleistungs-Lichtmaschinen)
- **Hybrid-Systeme** (Generator + Batterie + Inverter)
- **Produktlinien** (Fischer Panda, Whisper Power, Onan/Cummins, Paguro, Watt & Sea, EFOY)
- **Fehlerbild-Atlas** und **Troubleshooting**

### 1.3 AYDI-Integrationsebenen

```
Pipeline A (Structured): Leistungsbilanz-Berechnung, Generator-Dimensionierung,
                          Kraftstoffverbrauchs-Prognose, Betriebsstunden-Tracking,
                          Vibrations-/Schall-Analyse, Abgassystem-Validierung
Pipeline B (Visual):      Zustandserkennung (Korrosion, Leckagen, Riemenabnutzung),
                          Montage-Bewertung, Abgas-Verfaerbung, Kuehlerinspektion,
                          Schwingungsdaempfer-Zustand, Schallkapsel-Integritaet
Pipeline C (Text):        Service-Report-Analyse (Betriebsstunden, Oelwechsel-Intervalle,
                          Fehlercodes, Leistungsabfall-Protokolle, Werft-Berichte)
```

### 1.4 Regulatorischer Rahmen

| Norm / Standard | Bezeichnung | Geltungsbereich | AYDI-Relevanz |
|---|---|---|---|
| **ISO 8528-1:2018** | Reciprocating IC engine driven AC generating sets — Application, ratings and performance | Leistungsangaben, Klassifizierung | Nennleistung vs. Dauerleistung |
| **ISO 8528-5:2018** | Generating sets — Part 5: Generating sets | Spannungs-/Frequenzregelung | Qualitaetsklassen G1–G4 |
| **ISO 8528-10:2022** | Sound power level measurement | Geraeuschmessung | Schalldruckpegel-Grenzwerte |
| **ISO 8178-4:2020** | Reciprocating IC engines — Exhaust emission measurement — Part 4: Steady-state cycles | Abgasemissionen | Emissionsgrenzwerte |
| **ISO 10088:2013** | Small craft — Permanently installed fuel systems | Kraftstoffsystem | Tankanschluss, Leitungen |
| **ISO 9094:2015** | Small craft — Fire protection | Brandschutz | Abstand Generator ↔ Brennbares |
| **ISO 11105:2020** | Small craft — Ventilation of petrol engine and petrol tank compartments | Belueftung Motorraum | Luftvolumenstrom |
| **EN 13016:2018** | Liquid petroleum products — Vapour pressure | Kraftstoffqualitaet | Diesel-Spezifikation |
| **ABYC E-11 (2023)** | AC and DC Electrical Systems | Elektrische Systeme | Generatoranschluss, Erdung |
| **ABYC P-4 (2023)** | Marine Inboard Engines and Transmissions | Motorseitig | Abgas (motorseitig), Kuehlung |
| **RCD 2013/53/EU** | Recreational Craft Directive | CE-Kennzeichnung | Geraeusch, Abgas, Sicherheit |
| **GL/DNV Rules** | Classification Rules for Yachts | Klassegesellschaften | Redundanz, Backup-Systeme |

### 1.5 Wirtschaftliche Betrachtung

| Aspekt | Diesel-Gen (konv.) | Diesel-Gen (var. Drehzahl) | Hydrogenerator | Brennstoffzelle |
|---|---|---|---|---|
| Anschaffung (5 kW Aequivalent) | 8.000–15.000 EUR | 12.000–22.000 EUR | 3.000–6.000 EUR | 5.000–12.000 EUR |
| Betriebskosten/h | 2,50–4,50 EUR | 1,80–3,50 EUR | 0 EUR | 1,50–3,00 EUR |
| Wartungsintervall | 250–500 h | 500–1.000 h | 2.000+ h | 2.500–5.000 h |
| Lebensdauer (h) | 5.000–12.000 | 8.000–15.000 | 15.000+ | 5.000–10.000 |
| Schallpegel (1 m) | 55–72 dB(A) | 48–62 dB(A) | 0–5 dB(A) | 35–45 dB(A) |
| CO₂-Emission | hoch | mittel | null | gering–null |

---

## 2. Grundlagen und Theorie

### 2.1 Synchrongenerator — Funktionsprinzip

Der marine Synchrongenerator wandelt mechanische Rotationsenergie in elektrische Wechselstromenergie um. Das Funktionsprinzip basiert auf dem Faraday'schen Induktionsgesetz: Ein rotierender Magnetfeld-Laeufer (Rotor/Polrad) induziert in den Statorwicklungen eine Wechselspannung.

**Kernkomponenten:**

| Komponente | Funktion | Marine-spezifisch |
|---|---|---|
| Stator (Staender) | Traegt die Leistungswicklungen | Salzwasser-resistente Isolierung, Epoxid-Tränkung |
| Rotor (Laeufer) | Erzeugt rotierendes Magnetfeld | Dynamisch ausgewuchtet fuer Vibrationsarmut |
| Erregerwicklung | Stellt Magnetfeld her | Selbsterregung oder PMG (Permanent Magnet Generator) |
| AVR (Automatic Voltage Regulator) | Regelt Ausgangsspannung | Spannungskonstanz ±1–3% |
| Kugellager | Lagert Rotor | Marine-gefettet, abgedichtet |
| Luefter | Kuehlt Generator | Korrosionsbestaendig |
| Klemmenkasten | Elektrischer Anschluss | IP55 oder hoeher |

**Mathematische Grundlagen:**

```
Induzierte Spannung:
  U = 4,44 × f × N × Φ_max

  U     = Effektivwert der induzierten Spannung [V]
  f     = Frequenz [Hz]
  N     = Windungszahl pro Phase
  Φ_max = Maximaler magnetischer Fluss [Wb]

Frequenz-Drehzahl-Beziehung:
  f = (n × p) / 60

  f = Frequenz [Hz]
  n = Drehzahl [min⁻¹]
  p = Polpaarzahl

Typische Konfigurationen:
  50 Hz, 2-polig:  n = 3.000 min⁻¹
  50 Hz, 4-polig:  n = 1.500 min⁻¹
  60 Hz, 2-polig:  n = 3.600 min⁻¹
  60 Hz, 4-polig:  n = 1.800 min⁻¹
```

### 2.2 Frequenzstabilitaet

Die Frequenzstabilitaet ist das primaere Qualitaetskriterium eines Generators. Abweichungen von der Sollfrequenz beschaedigen empfindliche Elektronik (Navigationsgeraete, Kommunikation, Computer).

**ISO 8528-5 Qualitaetsklassen:**

| Klasse | Frequenzschwankung (stationaer) | Frequenzeinbruch (Lastsprung) | Ruecklaufzeit | Anwendung |
|---|---|---|---|---|
| G1 | ±5,0% | −15% | 10 s | Einfache Verbraucher, Beleuchtung |
| G2 | ±2,5% | −10% | 5 s | Allgemeine Bordverbraucher |
| G3 | ±1,5% | −7% | 3 s | Empfindliche Elektronik |
| G4 | ±0,5% | −5% | 1,5 s | Datenverarbeitung, Labor |

**Marine-Anforderung:** Mindestens G2, empfohlen G3. Yachten mit Unterhaltungselektronik, Navigations-PCs und Klimaanlagen-Invertern benoetigen G3-Qualitaet.

**Frequenz-Droop vs. Isochronous:**
- **Droop-Regelung:** Frequenz sinkt proportional zur Last (typisch 3–5% Droop). Vorteil: einfach, stabil bei Parallelbetrieb.
- **Isochronous-Regelung:** Frequenz bleibt konstant unabhaengig von der Last. Vorteil: praezise 50/60 Hz. Nachteil: Schwierig bei Parallelbetrieb ohne Load-Sharing-Elektronik.

### 2.3 Leistungsfaktor (cos φ)

Der Leistungsfaktor beschreibt das Verhaeltnis von Wirkleistung zu Scheinleistung. Marine-Verbraucher haben unterschiedliche Leistungsfaktoren:

| Verbraucher | cos φ | Blindleistungsanteil |
|---|---|---|
| Gluehlampen, Heizung | 1,0 | 0% |
| LED-Netzteile | 0,92–0,99 | 1–8% |
| Klimaanlage (Kompressor) | 0,65–0,85 | 15–35% |
| Wassermacher (Hochdruckpumpe) | 0,80–0,90 | 10–20% |
| Waschmaschine (Motor) | 0,60–0,75 | 25–40% |
| Batterieladegeraet (modern PFC) | 0,95–0,99 | 1–5% |
| Wechselrichter (modern) | 0,95–1,0 | 0–5% |
| Bugstrahlruder (DC-Motor via Inverter) | 0,70–0,85 | 15–30% |

**Dimensionierungsformel:**

```
Erforderliche Scheinleistung:
  S = P / cos φ_mittel

  S         = Scheinleistung [kVA]
  P         = Wirkleistung (Summe aller Verbraucher) [kW]
  cos φ_mittel = Gewichteter mittlerer Leistungsfaktor

Beispiel:
  P = 6 kW, cos φ_mittel = 0,82
  S = 6 / 0,82 = 7,32 kVA
  → Generator mit mindestens 7,5 kVA waehlen
```

**Generatoren werden in kVA (Scheinleistung) angegeben.** Die nutzbare Wirkleistung in kW ergibt sich aus: P_kW = S_kVA × cos φ_nenn (Generator-Nennleistungsfaktor, meist 0,8).

### 2.4 Kuehlsysteme

Marine-Generatoren verwenden verschiedene Kuehlkonzepte:

**2.4.1 Seewasserkuehlung (Einkreis)**

Seewasser wird direkt durch den Motorblock geleitet. Einfach, aber korrosionsanfaellig. Nur noch bei kleinen, preiswerten Aggregaten.

- Vorteil: Geringer Bauraum, preiswert
- Nachteil: Korrosion, Salzablagerung, Temperaturschock bei kaltem Wasser
- Anwendung: Generatoren <3 kW, aeltere Modelle

**2.4.2 Suesswasserkuehlung mit Seewasser-Waermetauscher (Zweikreis)**

Geschlossener Suesswasserkreislauf kuehlt den Motor. Waerme wird ueber einen Waermetauscher an Seewasser abgegeben.

- Vorteil: Kein Korrosionsangriff auf Motor, stabile Betriebstemperatur
- Nachteil: Aufwaendiger, Waermetauscher muss gewartet werden
- Anwendung: Standard bei allen modernen Marine-Generatoren

**2.4.3 Kielkuehlung (geschlossener Kreislauf)**

Suesswasserkreislauf gibt Waerme ueber ein Plattensystem am Rumpf an das umgebende Seewasser ab. Kein Seewasser im Boot.

- Vorteil: Kein Seewassereinlass noetig, wartungsarm, vibrationsfrei (kein Impeller)
- Nachteil: Grosser Kuehlerflaeche noetig, teuer, Rumpfdurchbrueche fuer Montage
- Anwendung: Langfahrt-Yachten, Aluminium-Yachten, Expeditionsschiffe

**2.4.4 Luftkuehlung**

Selten bei Marine-Generatoren. Nur bei sehr kleinen Aggregaten (<2 kW) oder Notstromanlagen.

- Vorteil: Kein Kuehlwassersystem
- Nachteil: Laut, grosse Kuehlflaechenbedarf, temperaturabhaengig
- Anwendung: Tragbare Generatoren, Notfallgeraete

**Dimensionierung Kuehlwasserdurchfluss:**

```
Erforderlicher Seewasser-Volumenstrom:
  Q_sw = (P_therm) / (ρ × cp × ΔT)

  Q_sw    = Volumenstrom Seewasser [m³/s]
  P_therm = Abzufuehrende Waermeleistung [W] ≈ 0,35 × P_mech (bei η_therm ≈ 35%)
  ρ       = Dichte Seewasser ≈ 1.025 kg/m³
  cp      = Spez. Waermekapazitaet ≈ 3.900 J/(kg·K)
  ΔT      = Temperaturdifferenz Ein/Aus ≈ 8–12 K

Beispiel 6 kW Generator (P_mech ≈ 8 kW):
  P_therm = 0,35 × 8.000 = 2.800 W
  Q_sw = 2.800 / (1.025 × 3.900 × 10) = 0,000070 m³/s ≈ 4,2 l/min
```

### 2.5 Schalldaemmung

Schall ist der primaere Komfortfaktor bei Bordgeneratoren. Die Schalldaemmung umfasst drei Bereiche:

**2.5.1 Koerperschall (Structure-borne noise)**

Vibration des Motors wird ueber die Befestigung in die Bootsstruktur eingeleitet und breitet sich im gesamten Rumpf aus.

- **Massnahme:** Elastische Lagerung (Schwingmetalle, Sylomer-Pads)
- **Ziel:** Mindestens 20 dB Koerperschall-Daempfung
- **Frequenzbereich:** 20–200 Hz (besonders stoerend: Grundfrequenz der Zuendung)

**Schwingmetall-Auswahl:**

| Generatorgewicht | Shore-Haerte | Einfederung | Eigenfrequenz |
|---|---|---|---|
| 50–100 kg | 40–50 Shore A | 3–5 mm | 12–18 Hz |
| 100–200 kg | 50–60 Shore A | 4–6 mm | 10–15 Hz |
| 200–400 kg | 55–65 Shore A | 5–8 mm | 8–12 Hz |
| 400–800 kg | 60–70 Shore A | 6–10 mm | 6–10 Hz |

**Regel:** Eigenfrequenz der Lagerung muss mindestens Faktor 2,5 unter der Erregerfrequenz (Zuendfrequenz) liegen.

```
Zuendfrequenz:
  f_zuend = (n × z) / (2 × 60)    [4-Takt]
  f_zuend = (n × z) / 60           [2-Takt]

  n = Drehzahl [min⁻¹]
  z = Zylinderzahl

Beispiel: 3-Zylinder, 1.500 min⁻¹, 4-Takt:
  f_zuend = (1.500 × 3) / 120 = 37,5 Hz
  → Eigenfrequenz Lagerung < 15 Hz erforderlich
```

**2.5.2 Luftschall (Airborne noise)**

Direkter Schall vom Generator durch die Luft.

- **Massnahme:** Schallkapsel (Enclosure), Schallisolierung Maschinenraum
- **Material:** Blei-Schaumstoff-Sandwich, Masse-Feder-Systeme
- **Ziel:** 20–35 dB(A) Daempfung durch Kapsel

**Schallkapsel-Aufbau (typisch):**

```
Aussen → Innen:
1. GFK/Aluminium-Gehaeuse (2–3 mm) — Witterungsschutz
2. Schwere Folie/Bleifolie (1–3 kg/m²) — Masse-Daempfung
3. Offenporiger Akustikschaum (30–50 mm) — Absorber
4. Perforiertes Blech/Vlies — Schutz Absorber
5. Luftspalt (20–50 mm) — Entkopplung
```

**2.5.3 Abgasschall (Exhaust noise)**

Der Auspuff ist eine signifikante Schallquelle (oft 80–100 dB(A) ohne Daempfung).

- **Massnahme:** Wassereinspritz-Schalldaempfer (Waterlock + Muffler)
- **Ziel:** Abgasschall <55 dB(A) am Auspuffaustritt

**Wassereinspritz-Schalldaempfer-Kette:**

```
Motor-Abgaskruemmer
  → Mischkruemmer (Seewasser-Einspritzung, Temp. 80°C → 50°C)
    → Waterlock (Kondensatsammler, verhindert Wasserrueckfluss)
      → Schalldaempfer (Reflexions- oder Absorptionsdaempfer)
        → Schwanenhalsbogen (Hochpunkt ueber Wasserlinie)
          → Auspuffaustritt (Heckdurchbruch, ueber Wasserlinie)
```

### 2.6 Abgassystem — Detailbetrachtung

**Abgastemperaturen:**

| Position | Temperatur | Material |
|---|---|---|
| Austritt Zylinderkopf | 350–550°C | Gusseisen, Edelstahl |
| Nach Mischkruemmer (nass) | 45–65°C | GFK, Gummi, Edelstahl |
| Waterlock | 40–55°C | GFK, PE |
| Schalldaempfer | 35–50°C | GFK, PE, Gummi |
| Auspuffaustritt | 30–45°C | GFK, Gummi |

**Abgasgegendruck:**

```
Maximaler Abgasgegendruck (typische Werte):
  Saugmotor:     40–60 mbar
  Turbomotor:    25–40 mbar

Berechnung Druckverlust im Nassauspuff:
  Δp = λ × (L/D) × (ρ × v²/2) + Σ ζ × (ρ × v²/2) + ρ × g × h

  λ = Rohrreibungszahl (≈ 0,03 fuer Nassauspuff)
  L = Leitungslaenge [m]
  D = Innendurchmesser [m]
  ρ = Dichte Abgas-Wasser-Gemisch ≈ 980 kg/m³
  v = Stroemungsgeschwindigkeit [m/s]
  ζ = Einzelwiderstandsbeiwerte (Boegen, Reduktionen)
  h = Gesamthubhoehe [m]
```

**Abgasleitungs-Dimensionierung:**

| Generatorleistung | Min. Innendurchmesser (nass) | Max. Laenge |
|---|---|---|
| 2–4 kW | 38 mm (1,5") | 4 m |
| 4–8 kW | 45 mm (1,75") | 5 m |
| 8–15 kW | 50 mm (2") | 6 m |
| 15–25 kW | 60 mm (2,5") | 7 m |
| 25–50 kW | 75 mm (3") | 8 m |
| 50–100 kW | 90 mm (3,5") | 10 m |

### 2.7 Kraftstoffverbrauch

**Spezifischer Kraftstoffverbrauch (SFOC/be):**

```
Spezifischer Verbrauch:
  be = m_dot_fuel / P_eff

  be        = spez. Kraftstoffverbrauch [g/kWh]
  m_dot_fuel = Kraftstoff-Massenstrom [g/h]
  P_eff      = Effektive Leistung [kW]

Typische Werte (Marine-Diesel):
  Volllast (100%):  240–290 g/kWh
  Teillast (75%):   235–275 g/kWh  ← Optimum
  Teillast (50%):   260–310 g/kWh
  Teillast (25%):   320–420 g/kWh  ← Unwirtschaftlich

Variable-Drehzahl-Generatoren:
  Volllast (100%):  230–260 g/kWh
  Teillast (75%):   220–250 g/kWh
  Teillast (50%):   230–260 g/kWh  ← Deutlich besser als konventionell
  Teillast (25%):   250–300 g/kWh
```

**Betriebskostenformel:**

```
Kosten pro Betriebsstunde:
  K_h = be × P_eff × ρ_diesel⁻¹ × Preis_diesel + K_wartung

  Beispiel: 6 kW Generator bei 75% Last:
  K_h = 0,260 × 4,5 × (1/0,84) × 1,85 + 0,50
  K_h = 1,39 × 1,85 + 0,50 = 2,57 + 0,50 = 3,07 EUR/h

  (be=260 g/kWh, P_eff=4,5 kW, ρ_diesel=0,84 kg/l, Diesel=1,85 EUR/l, Wartung=0,50 EUR/h)
```

### 2.8 Lastmanagement und Lastverteilung

**Lastaufschaltung (Load Acceptance):**

Plotzliches Zuschalten grosser Verbraucher verursacht Frequenz- und Spannungseinbrueche. Marine-Generatoren muessen folgende Lastspruenge verarbeiten:

| Lastsprung | Max. Frequenzeinbruch | Max. Spannungseinbruch | Erholungszeit |
|---|---|---|---|
| 25% Nennlast | ≤5% | ≤10% | ≤3 s |
| 50% Nennlast | ≤8% | ≤15% | ≤5 s |
| 75% Nennlast | ≤12% | ≤20% | ≤8 s |
| 100% Nennlast | ≤15% | ≤25% | ≤10 s |

**Lastmanagement-Strategien:**

1. **Prioritaets-Lastabwurf:** Unwichtige Verbraucher werden bei Ueberlast abgeworfen
2. **Sanftanlauf (Soft-Start):** Kompressoren mit Anlaufstrombegrenzung
3. **Sequentielles Zuschalten:** Klimaanlage, Wassermacher, Ladegeraete zeitversetzt
4. **Inverter-Unterstuetzung:** Batterie-Inverter fangt Lastspitzen auf

### 2.9 Parallelbetrieb

Bei groesseren Yachten (ab ca. 20 m) werden zwei Generatoren parallel betrieben:

**Voraussetzungen:**
- Identische Frequenz (Synchronisation)
- Identische Spannung
- Identische Phasenlage
- Gleiche Phasenfolge

**Synchronisierungsverfahren:**
1. **Manuell:** Synchro-Instrument, Dunkelschaltung
2. **Automatisch:** Synchronisier-Relais, PLC-gesteuert

**Lastverteilung (Load Sharing):**
- Droop-Methode: Beide Generatoren mit 3–5% Droop → automatische Lastverteilung
- Isochronous Load Sharing: Elektronische Lastverteilung, konstante Frequenz

### 2.10 Wirkungsgrad-Kette

```
Kraftstoff (chemische Energie)
  → Dieselmotor (thermisch → mechanisch): η_therm = 30–38%
    → Generator (mechanisch → elektrisch): η_gen = 88–95%
      → Ladegeraet (AC → DC, Batterie): η_charge = 85–92%
        → Inverter (DC → AC, Verbraucher): η_inv = 90–95%

Gesamt-Wirkungsgrad Kraftstoff → AC-Verbraucher (ueber Batterie):
  η_total = 0,34 × 0,92 × 0,88 × 0,92 = 0,253 ≈ 25%

Gesamt-Wirkungsgrad Kraftstoff → AC-Verbraucher (direkt vom Generator):
  η_total = 0,34 × 0,92 = 0,313 ≈ 31%
```

### 2.11 Elektrische Sicherheit und Erdung

**Erdungssysteme fuer Bordgeneratoren:**

| System | Beschreibung | Anwendung | Vorteil |
|---|---|---|---|
| IT-Netz (uneerdet) | Sternpunkt nicht geerdet | Marine-Standard | Kein Erdstrom bei erstem Fehler |
| TN-S | Sternpunkt geerdet, PE separat | Grosse Yachten | Einfache Fehlerausloesung |
| TT | Sternpunkt geerdet, lokale Erdung | Selten marine | Landstrom-Kompatibel |

**Marine-Standard ist IT-Netz** (isoliertes System). Ein Isolationswaechter ueberwacht den Isolationswiderstand und warnt bei erstem Fehler, ohne den Betrieb zu unterbrechen.

**Galvanische Trennung:**
Der Generator muss galvanisch vom Landstromnetz getrennt sein (Umschaltung oder Trenntrafo), um galvanische Korrosion und Streustroeme zu vermeiden (→ Verweis 22_10).

---

## 3. Typenuebersicht

### 3.1 Diesel-Generatoren — Konventionell (Festdrehzahl)

**Prinzip:** Dieselmotor treibt Synchrongenerator mit fester Drehzahl an (1.500 oder 3.000 min⁻¹ fuer 50 Hz; 1.800 oder 3.600 min⁻¹ fuer 60 Hz).

**Vorteile:**
- Bewaehrte, robuste Technologie
- Hohe Zuverlaessigkeit (>95% Verfuegbarkeit)
- Breites Leistungsspektrum (1–500+ kW)
- Weltweit Service-Netzwerk
- Direkte AC-Einspeisung ohne Elektronik
- Lange Lebensdauer bei guter Wartung (10.000–15.000 h)

**Nachteile:**
- Laeuft immer bei gleicher Drehzahl (auch bei Teillast)
- Hoher Teillast-Verbrauch
- Vibrationen bei fester Drehzahl
- Geraeuschniveau 55–72 dB(A)
- Regelmaessige Wartung (Oelwechsel, Filter, Impeller)
- Nasslauf-Gefahr bei dauerhaft <30% Last

**Leistungsbereiche Marine:**

| Segment | Leistung | Drehzahl | Zylinder | Gewicht | Typische Motoren |
|---|---|---|---|---|---|
| Kompakt | 2–5 kW | 3.000/3.600 | 1–2 | 60–120 kg | Kubota Z482, Farymann |
| Standard | 5–12 kW | 1.500/1.800 | 2–3 | 150–350 kg | Kubota D1105, Yanmar 3TNV |
| Mittel | 12–30 kW | 1.500/1.800 | 3–4 | 300–700 kg | Kubota V2403, Yanmar 4TNV |
| Gross | 30–80 kW | 1.500/1.800 | 4–6 | 600–1.500 kg | John Deere, Cummins B3.3 |
| Superyacht | 80–350 kW | 1.500/1.800 | 6–12 | 1.500–5.000 kg | Caterpillar, MTU, Cummins QSB |

### 3.2 Diesel-Generatoren — Variable Drehzahl (VSD)

**Prinzip:** Dieselmotor laeuft mit variabler Drehzahl, angepasst an die aktuelle Last. Ein PMG (Permanent Magnet Generator) erzeugt Strom variabler Frequenz. Leistungselektronik (Inverter) wandelt in stabiles 230V/50Hz um.

**Vorteile:**
- 20–40% weniger Kraftstoffverbrauch bei Teillast
- Deutlich leiser bei Teillast (Drehzahl sinkt)
- Weniger Vibrationen bei niedriger Last
- Laengere Wartungsintervalle (weniger Betriebsstunden bei gleicher Energie)
- Kompaktere Bauweise (hoehere Leistungsdichte)
- Kein Nasslauf-Problem (Drehzahl folgt Last)

**Nachteile:**
- Teure Leistungselektronik
- Elektronik als potenzielle Fehlerquelle
- Komplexere Reparatur (Spezialwissen noetig)
- THD (Total Harmonic Distortion) der Ausgangsspannung hoeher
- Empfindlich gegen Seewasser-Kontakt der Elektronik
- Kuerzere Elektronik-Lebensdauer in feuchter Umgebung

**Technologie-Varianten:**

| Variante | Drehzahlbereich | Generator-Typ | Elektronik |
|---|---|---|---|
| PMG + Inverter | 1.200–3.600 min⁻¹ | Permanentmagnet | Vollbruecken-Wechselrichter |
| Asynchron + Inverter | 1.000–3.000 min⁻¹ | Asynchron (Kaefiglaeufer) | Frequenzumrichter |
| DC-Generator + Inverter | 1.200–3.000 min⁻¹ | Gleichstrom-Generator | DC/AC-Wechselrichter |

**Marktfuehrer Variable Drehzahl:**
- Fischer Panda iSeries (PMG-Technologie)
- Whisper Power M-GV (Variable Speed)
- Mastervolt Whisper (DC-Generator-Konzept)

### 3.3 Hydrogeneratoren

**Prinzip:** Ein Propeller oder eine Turbine wird vom Fahrtwind des Wassers angetrieben und treibt einen Generator. Funktioniert nur unter Segel (oder Schlepp). Keine Emissionen, kein Laerm, kein Kraftstoff.

**Typen:**

| Typ | Beschreibung | Leistung | Geschwindigkeit | Einsatz |
|---|---|---|---|---|
| Schleppgenerator (Towed) | Rotor am Seil hinter Boot | 100–500 W | ab 4 kn | Langfahrt-Segler |
| Festmontiert (Fixed) | Propeller am Heckspiegel/Ruder | 200–800 W | ab 3,5 kn | Performance-Cruiser |
| Saildrive-Integration | Nutzt vorhandenen Saildrive-Prop | 100–400 W | ab 4 kn | Nachruestung |
| Hochleistung | Spezieller Unterwasser-Propeller | 500–2.000 W | ab 5 kn | Regatta/Rekord |

**Leistungskurve (typisch Festmontiert):**

```
Geschwindigkeit [kn] → Leistung [W]
  3,0 kn →   20–40 W
  4,0 kn →   50–80 W
  5,0 kn →  100–160 W
  6,0 kn →  180–280 W
  7,0 kn →  300–450 W
  8,0 kn →  450–650 W
  9,0 kn →  600–900 W
 10,0 kn →  800–1.200 W
 12,0 kn → 1.200–2.000 W

Leistung steigt kubisch mit der Geschwindigkeit:
  P ∝ v³

  P_2/P_1 = (v_2/v_1)³

Beispiel: Verdopplung der Geschwindigkeit von 5 auf 10 kn:
  P_2 = P_1 × (10/5)³ = P_1 × 8
  → 8-fache Leistung
```

**Widerstandserhoehung durch Hydrogenerator:**

| Typ | Zusaetzlicher Widerstand | Geschwindigkeitsverlust |
|---|---|---|
| Schleppgenerator (Seil) | 5–15 kg | 0,2–0,5 kn |
| Festmontiert (klappbar) | 3–8 kg | 0,1–0,3 kn |
| Festmontiert (fest) | 8–20 kg | 0,3–0,7 kn |
| Saildrive-Regeneration | 2–5 kg | 0,1–0,2 kn |

### 3.4 Brennstoffzellen

**Prinzip:** Elektrochemische Umwandlung von Brennstoff (Methanol, Wasserstoff, Diesel-Reformat) in elektrische Energie. Leise, effizient, emissionsarm.

**3.4.1 DMFC — Direkt-Methanol-Brennstoffzelle**

| Merkmal | Wert |
|---|---|
| Brennstoff | Methanol (CH₃OH) |
| Leistung (marine) | 25–500 W (EFOY-Bereich), bis 5 kW (SFC) |
| Wirkungsgrad | 25–35% (elektrisch) |
| Betriebstemperatur | 60–90°C |
| Lebensdauer | 5.000–10.000 h |
| Startzeit | 15–60 min |
| Vorteil | Fluessiger Brennstoff, einfache Lagerung |
| Nachteil | Niedrige Leistungsdichte, langsamer Start |
| Hersteller | EFOY (SFC Energy), Blue World |

**3.4.2 PEM — Proton Exchange Membrane (Wasserstoff)**

| Merkmal | Wert |
|---|---|
| Brennstoff | Wasserstoff (H₂) |
| Leistung (marine) | 1–100+ kW |
| Wirkungsgrad | 45–60% (elektrisch) |
| Betriebstemperatur | 60–80°C |
| Lebensdauer | 5.000–20.000 h |
| Startzeit | Sekunden bis 2 min |
| Vorteil | Hoher Wirkungsgrad, schnelle Lastfolge, nur Wasser als Emission |
| Nachteil | H₂-Speicherung komplex (350/700 bar Tanks), Infrastruktur |
| Hersteller | Toyota (Marine-Adaptation), Ballard, PowerCell, Proton Motor |

**3.4.3 SOFC — Festoxid-Brennstoffzelle**

| Merkmal | Wert |
|---|---|
| Brennstoff | Diesel, LNG, Methanol (via Reformer) |
| Leistung (marine) | 5–300 kW |
| Wirkungsgrad | 50–65% (elektrisch), bis 85% mit Waermerueckgewinnung |
| Betriebstemperatur | 700–1.000°C |
| Lebensdauer | 20.000–40.000 h |
| Startzeit | 2–12 h (!) |
| Vorteil | Hoechster Wirkungsgrad, nutzt vorhandenen Diesel |
| Nachteil | Extrem lange Startzeit, Thermoschock-empfindlich |
| Hersteller | Bloom Energy (Marine-Adaptation), AVL |

**Vergleichstabelle Brennstoffzellen vs. Diesel-Generator:**

| Kriterium | Diesel-Gen 5 kW | EFOY 500 W | PEM 5 kW | SOFC 5 kW |
|---|---|---|---|---|
| Gewicht (System) | 200 kg | 8 kg | 80 kg | 120 kg |
| Volumen | 0,4 m³ | 0,02 m³ | 0,2 m³ | 0,3 m³ |
| Schall (1 m) | 55–65 dB(A) | 0–25 dB(A) | 35–45 dB(A) | 40–50 dB(A) |
| Wirkungsgrad (Last) | 25–34% | 25–35% | 45–55% | 50–60% |
| Brennstoff-Kosten/kWh | 0,50–0,80 EUR | 1,50–3,00 EUR | 0,80–2,00 EUR | 0,40–0,70 EUR |
| Wartungsintervall | 250 h | 5.000 h | 2.000 h | 5.000 h |
| Startzeit | 5–15 s | 15–60 min | 10–60 s | 2–12 h |
| Emissionen (CO₂) | 700–900 g/kWh | 500–700 g/kWh | 0 g/kWh | 400–600 g/kWh |

### 3.5 DC-Generatoren (Hochleistungs-Lichtmaschinen)

**Prinzip:** Hochleistungs-Gleichstromgenerator (Lichtmaschine), angetrieben vom Hauptmotor oder separatem Dieselmotor. Erzeugt DC-Strom direkt fuer Batterieladung.

**Typen:**

| Typ | Leistung | Antrieb | Anwendung |
|---|---|---|---|
| Riemengetriebene Hochleistungs-Lima | 100–300 A (12V), 50–150 A (24V) | Hauptmotor-Riemen | Standard-Nachruestung |
| Direkt gekoppelter DC-Generator | 200–500 A (12/24V) | Hauptmotor-Schwungrad | Professionelle Yachten |
| Separater DC-Generator | 100–400 A (24/48V) | Eigener Dieselmotor | Hochleistungs-Ladung |
| Zweite Lichtmaschine (Dual) | 80–200 A | Hauptmotor | Kostenguenstige Loesung |

**Marktfuehrer:**
- Balmar (USA) — XT-Series (170–310 A)
- Electrodyne (USA) — 200–600 A Hochleistung
- Mastervolt Alpha (NL) — 12/24V bis 200 A
- Victron Orion — DC/DC-Wandler (keine Lima, aber DC-DC)

**Vorteile DC-Generator:**
- Kein Wechselrichter noetig fuer Batterieladung
- Hoher Ladewirkungsgrad (92–97%)
- Kann waehrend der Fahrt laden (Hauptmotor sowieso an)
- Einfache Installation (Riemen nachruestbar)

**Nachteile:**
- Kein AC-Strom (Inverter zusaetzlich noetig)
- Bei Riemenantrieb: Riemenverschleiss, Riemenspannung
- Hauptmotor muss laufen (= Kraftstoff, Laerm)
- Lichtmaschinen-Regler muss auf Batterietype abgestimmt sein

### 3.6 Hybrid-Systeme

**Prinzip:** Kombination aus Generator, Batteriespeicher und Leistungselektronik. Der Generator laeuft nur im optimalen Betriebspunkt und laedt Batterien. Verbraucher werden aus Batterien ueber Inverter versorgt.

**Architektur-Varianten:**

```
Variante A — Serieller Hybrid:
  Generator → Ladegeraet → Batteriebank → Inverter → Verbraucher
  - Generator laeuft nur bei Bedarf, immer im Optimum
  - Grosse Batteriebank noetig

Variante B — Paralleler Hybrid:
  Generator → AC-Sammelschiene ← Inverter ← Batteriebank
  - Generator speist direkt + laedt Batterien
  - Inverter uebernimmt bei niedrigem Verbrauch
  - Kleinere Batteriebank moeglich

Variante C — DC-Bus-Hybrid:
  Generator → Gleichrichter → DC-Bus (48V) ← Solar/Wind
                                    ↓
                              Batteriebank
                                    ↓
                              Inverter → AC-Verbraucher
  - Alle Quellen speisen auf gemeinsamen DC-Bus
  - Maximal flexibel, optimal erweiterbar
  - Komplexe Steuerung (BMS + EMS)
```

**Hybrid-Steuerungslogik:**

| Zustand | SOC Batterie | Verbrauch | Generator | Inverter |
|---|---|---|---|---|
| Segeln, wenig Verbrauch | >60% | <500 W | AUS | EIN (Batterie) |
| Segeln, hoher Verbrauch | >40% | 500–2.000 W | AUS | EIN (Batterie) |
| Segeln, Batterie niedrig | <40% | beliebig | EIN (Ladung) | Bypass |
| Anker, Tag (Solar) | steigend | <1.000 W | AUS | EIN (Batterie+Solar) |
| Anker, Klima laeuft | sinkend | 2.000–5.000 W | EIN | Parallel |
| Motor laeuft | steigend | beliebig | AUS (Lima reicht) | EIN |
| Notfall/Ueberlast | <20% | >Nenn | EIN (Volllast) | EIN (Parallel) |

**Marktfuehrer Hybrid-Systeme:**
- Victron Energy (MultiPlus-II, Quattro, Cerbo GX)
- Mastervolt (CombiMaster, EasyPlus)
- Fischer Panda (iSeries + PMG)
- Torqeedo (Deep Blue Hybrid)
- Oceanvolt (ServoProp + Batterie)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Fischer Panda — iSeries (Variable Drehzahl)

Fischer Panda (Paderborn, Deutschland) ist Marktfuehrer fuer schallisolierte Marine-Generatoren mit variabler Drehzahl.

**iSeries-Technologie:**
- Permanentmagnet-Generator (PMG) mit variabler Drehzahl
- Inverter-Elektronik fuer sauberes 230V/50Hz (oder 120V/60Hz)
- Vollgekapselt in Schalldaemmgehaeuse
- Kielkuehlung oder Seewasserkuehlung
- Fernueberwachung via iControl/CAN-Bus

**Modellreihe iSeries:**

| Modell | Leistung (kW) | Leistung (kVA) | Motor | Zyl. | Drehzahl | Gewicht | Schall (7m) | Kuehlung |
|---|---|---|---|---|---|---|---|---|
| Panda 4000i | 3,4 | 4,0 | Kubota Z482 | 2 | 1.500–3.600 | 135 kg | 52 dB(A) | SW/Kiel |
| Panda 5000i | 4,2 | 5,0 | Kubota Z602 | 2 | 1.500–3.600 | 145 kg | 53 dB(A) | SW/Kiel |
| Panda 8000i | 7,0 | 8,0 | Kubota D722 | 3 | 1.200–3.000 | 195 kg | 54 dB(A) | SW/Kiel |
| Panda 10000i | 8,5 | 10,0 | Kubota D902 | 3 | 1.200–3.000 | 210 kg | 55 dB(A) | SW/Kiel |
| Panda 15000i | 12,5 | 15,0 | Kubota D1105 | 3 | 1.200–3.000 | 295 kg | 56 dB(A) | SW/Kiel |
| Panda 20000i | 17,0 | 20,0 | Kubota V1505 | 4 | 1.200–2.400 | 380 kg | 57 dB(A) | SW/Kiel |
| Panda 25000i | 21,0 | 25,0 | Kubota V2003 | 4 | 1.200–2.400 | 420 kg | 58 dB(A) | SW/Kiel |
| Panda 30000i | 25,5 | 30,0 | Kubota V2403 | 4 | 1.200–2.400 | 480 kg | 59 dB(A) | SW/Kiel |
| Panda 45000i | 38,0 | 45,0 | Kubota V3307 | 4 | 1.200–2.200 | 620 kg | 60 dB(A) | SW/Kiel |

**Fischer Panda AGT-Serie (Festdrehzahl, kostenguenstiger):**

| Modell | Leistung (kW) | Motor | Zyl. | Drehzahl | Gewicht | Schall (7m) |
|---|---|---|---|---|---|---|
| AGT 4000 | 3,5 | Kubota Z482 | 2 | 3.000 | 120 kg | 56 dB(A) |
| AGT 6000 | 5,2 | Kubota D722 | 3 | 3.000 | 155 kg | 58 dB(A) |
| AGT 8000 | 7,0 | Kubota D902 | 3 | 1.500 | 220 kg | 57 dB(A) |
| AGT 12000 | 10,5 | Kubota D1105 | 3 | 1.500 | 280 kg | 58 dB(A) |
| AGT 17000 | 14,5 | Kubota V1505 | 4 | 1.500 | 360 kg | 59 dB(A) |
| AGT 22000 | 19,0 | Kubota V2003 | 4 | 1.500 | 430 kg | 60 dB(A) |

**Fischer Panda Besonderheiten:**
- **Kielkuehlung als Standard-Option:** Eliminiert Seewasser-Impeller, reduziert Wartung
- **VCS (Vehicle Control System):** CAN-Bus-Integration, Autostart bei niedrigem SOC
- **iControl 2.0:** Touch-Display mit Echtzeit-Monitoring, Fernzugang via App
- **3-Punkt-Lagerung:** Patentierte schwimmende Aufhaengung fuer minimale Vibration
- **Schalldaemmung 2-schalig:** Blei-Composite + Akustikschaum, teilbar fuer Wartung

### 4.2 Whisper Power — M-GV Serie (Variable Speed)

Whisper Power (Drunen, Niederlande) bietet kompakte Variable-Speed-Generatoren fuer den europaeischen Markt.

**M-GV Serie (Marine Genverter):**

| Modell | Leistung (kW) | Motor | Zyl. | Drehzahlbereich | Gewicht | Schall (7m) |
|---|---|---|---|---|---|---|
| M-GV 3 | 2,8 | Yanmar L48N | 1 | 2.000–3.600 | 75 kg | 54 dB(A) |
| M-GV 4 | 3,5 | Yanmar L70N | 1 | 2.000–3.600 | 85 kg | 55 dB(A) |
| M-GV 5 | 4,5 | Kubota Z482 | 2 | 1.500–3.600 | 110 kg | 53 dB(A) |
| M-GV 7 | 6,0 | Kubota D722 | 3 | 1.200–3.000 | 145 kg | 54 dB(A) |
| M-GV 9 | 7,5 | Kubota D902 | 3 | 1.200–3.000 | 165 kg | 55 dB(A) |
| M-GV 12 | 10,0 | Kubota D1105 | 3 | 1.200–3.000 | 210 kg | 56 dB(A) |
| M-GV 15 | 12,5 | Kubota V1505 | 4 | 1.200–2.400 | 280 kg | 57 dB(A) |

**Whisper Power Piccolo Serie (Ultra-Kompakt):**

| Modell | Leistung (kW) | Motor | Gewicht | Besonderheit |
|---|---|---|---|---|
| Piccolo 3 | 2,5 | Yanmar L48V | 52 kg | Kleinster Marine-Gen am Markt |
| Piccolo 4 | 3,5 | Yanmar L70V | 62 kg | Fuer Segelyachten 9–12 m |
| Piccolo 5 | 4,0 | Kubota Z482 | 78 kg | Meistverkauft |
| Piccolo 8 | 6,5 | Kubota D722 | 105 kg | Kompakt fuer MY bis 14 m |

**Whisper Power Besonderheiten:**
- **Genverter-Technologie:** PMG + IGBT-Inverter, THD <3%
- **SuperQuiet-Enclosure:** Doppelwandiges Stahlgehaeuse mit Akustikfuellung
- **TouchView Display:** 4,3" Farb-Touch, NMEA2000-kompatibel
- **Auto-Start/Stop:** SOC-basiert oder Timer-gesteuert
- **Modulares System:** Gleiche Elektronik ueber alle Groessen

### 4.3 Onan/Cummins — Marine-Generatoren

Onan (heute Cummins Power Generation) ist der aelteste Marine-Generator-Hersteller (seit 1920er) und Marktfuehrer in Nordamerika.

**MDKAV/MDKBH Serie (Einphasig, Festdrehzahl):**

| Modell | Leistung (kW) | Motor | Zyl. | Drehzahl | Gewicht | Schall |
|---|---|---|---|---|---|---|
| MDKAV 5 | 5,0 | Cummins A1700 | 2 | 1.800 | 186 kg | 62 dB(A) |
| MDKBH 5.5 | 5,5 | Cummins A2300 | 3 | 1.800 | 218 kg | 61 dB(A) |
| MDKBH 7.5 | 7,5 | Cummins A2300 | 3 | 1.800 | 232 kg | 62 dB(A) |
| MDKBU 9 | 9,0 | Kubota D1105 | 3 | 1.800 | 268 kg | 63 dB(A) |
| MDKBU 12 | 12,0 | Kubota V1505 | 4 | 1.800 | 318 kg | 63 dB(A) |
| MDKBV 15 | 15,0 | Kubota V2003 | 4 | 1.800 | 385 kg | 64 dB(A) |
| MDKBZ 17.5 | 17,5 | Cummins QSD | 4 | 1.800 | 445 kg | 64 dB(A) |
| MDKBZ 21.5 | 21,5 | Cummins QSD | 4 | 1.800 | 478 kg | 65 dB(A) |

**Cummins QD-Serie (Dreiphasig, Superyacht):**

| Modell | Leistung (kW) | Motor | Zyl. | Gewicht |
|---|---|---|---|---|
| QD 25 | 25 | Cummins QSB 3.3 | 4 | 620 kg |
| QD 32 | 32 | Cummins QSB 3.3 | 4 | 680 kg |
| QD 40 | 40 | Cummins QSB 3.3 | 4 | 740 kg |
| QD 55 | 55 | Cummins QSB 5.9 | 6 | 980 kg |
| QD 65 | 65 | Cummins QSB 5.9 | 6 | 1.050 kg |
| QD 80 | 80 | Cummins QSB 6.7 | 6 | 1.180 kg |
| QD 100 | 100 | Cummins QSL 8.9 | 6 | 1.450 kg |
| QD 125 | 125 | Cummins QSL 8.9 | 6 | 1.580 kg |

**Onan/Cummins Besonderheiten:**
- **PowerCommand-Controller:** Digitale Steuerung, Ferndiagnose
- **InPower Software:** PC-basierte Service-Software
- **Weltweites Service-Netz:** >6.000 autorisierte Haendler
- **Heavy-Duty-Auslegung:** Konservative Leistungsangaben, lange Lebensdauer
- **Sound Shield:** Optionale Schallkapsel, dreiseitig zugaenglich

### 4.4 Paguro — Italienische Marine-Generatoren

Paguro (Ravenna, Italien) bietet Kompakt-Generatoren mit exzellenter Schalldaemmung.

| Modell | Leistung (kW) | Motor | Zyl. | Drehzahl | Gewicht | Schall (7m) |
|---|---|---|---|---|---|---|
| Paguro 2000 | 2,0 | Lombardini LDW502 | 1 | 3.000 | 72 kg | 56 dB(A) |
| Paguro 3000 | 3,0 | Lombardini LDW702 | 2 | 3.000 | 95 kg | 57 dB(A) |
| Paguro 4000 | 4,0 | Lombardini LDW1003 | 2 | 3.000 | 108 kg | 58 dB(A) |
| Paguro 5500 | 5,5 | Lombardini LDW1404 | 3 | 3.000 | 135 kg | 59 dB(A) |
| Paguro 6500 | 6,5 | Lombardini LDW1503 | 3 | 1.500 | 185 kg | 57 dB(A) |
| Paguro 8500 | 8,5 | Lombardini LDW2004 | 4 | 1.500 | 240 kg | 58 dB(A) |
| Paguro 12000 | 12,0 | Lombardini LDW2204 | 4 | 1.500 | 310 kg | 59 dB(A) |
| Paguro 14000 | 14,0 | Fiat/FPT F32 | 4 | 1.500 | 380 kg | 60 dB(A) |
| Paguro 18000 | 18,0 | FPT F34 | 4 | 1.500 | 450 kg | 61 dB(A) |

**Paguro Besonderheiten:**
- **Made in Italy:** Vollstaendig in Ravenna gefertigt
- **Kompakte Bauweise:** Kurzer Motor + Generator = minimale Bauraumlaenge
- **Modularer Schalldaemm-Aufbau:** Einfach zugaenglich fuer Wartung
- **Seewasser-/Kielkuehlung:** Beide Varianten ab Werk
- **Preis-Leistung:** Oft 15–25% guenstiger als Fischer Panda

### 4.5 Watt & Sea — Hydrogeneratoren

Watt & Sea (La Rochelle, Frankreich) ist der Marktfuehrer fuer maritime Hydrogeneratoren.

**Modellreihe:**

| Modell | Typ | Max. Leistung | Gewicht | Montage | Preis (ca.) |
|---|---|---|---|---|---|
| Cruising 300 | Festmontiert | 300 W | 5,5 kg (UW) | Heckspiegel | 4.500 EUR |
| Cruising 600 | Festmontiert | 600 W | 7,2 kg (UW) | Heckspiegel/Ruder | 5.800 EUR |
| Racing 600 | Festmontiert | 600 W | 4,8 kg (UW) | Heckspiegel | 7.200 EUR |
| POD 600 | Pod-Montage | 600 W | 8,5 kg (UW) | Unterwasser-Pod | 6.500 EUR |
| POD 1200 | Pod-Montage | 1.200 W | 12 kg (UW) | Unterwasser-Pod | 9.800 EUR |

**Technische Daten Cruising 600:**

```
Nennleistung:           600 W bei 10 kn (Maximum, strombegrenzt)
Startgeschwindigkeit:   2,5 kn
Spannung:              12V, 24V oder 48V (konfigurierbar)
Max. Strom:            25 A (24V-Version)
Propeller-Durchmesser: 250 mm (klappbar)
Unterwasser-Gewicht:   7,2 kg
Heben/Senken:          Manuell (Seil) oder elektrisch
Laderegler:            MPPT integriert (im Hydro-Charger)
Display:               Hydro-Monitor (optional)
```

**Leistungskurve Cruising 600 (24V):**

| Geschwindigkeit (kn) | Strom (A) | Leistung (W) |
|---|---|---|
| 3,0 | 0,5 | 12 |
| 4,0 | 1,8 | 43 |
| 5,0 | 4,0 | 96 |
| 6,0 | 7,5 | 180 |
| 7,0 | 12,0 | 288 |
| 8,0 | 17,5 | 420 |
| 9,0 | 22,0 | 528 |
| 10,0 | 25,0 | 600 (begrenzt) |

### 4.6 EFOY — Brennstoffzellen fuer Yachten

EFOY (SFC Energy, Brunnthal, Deutschland) ist Marktfuehrer fuer marine Methanol-Brennstoffzellen.

**EFOY Pro Series:**

| Modell | Dauerleistung | Energie/Tag | Brennstoff | Gewicht | Abmessungen |
|---|---|---|---|---|---|
| EFOY Pro 800 Duo | 40 W | 960 Wh | Methanol M5/M10 | 7,8 kg | 448×242×277 mm |
| EFOY Pro 2400 Duo | 110 W | 2.640 Wh | Methanol M5/M10 | 8,6 kg | 448×242×277 mm |
| EFOY Pro 12000 Duo | 500 W | 12.000 Wh | Methanol M28 | 21 kg | 653×350×514 mm |

**EFOY Comfort Series (Yacht/Camper):**

| Modell | Dauerleistung | Energie/Tag | Tankpatrone | Gewicht |
|---|---|---|---|---|
| EFOY Comfort 80 | 40 W | 960 Wh | M5 (5 l) / M10 (10 l) | 7,1 kg |
| EFOY Comfort 140 | 72 W | 1.728 Wh | M5 / M10 | 7,3 kg |
| EFOY Comfort 210 | 105 W | 2.520 Wh | M5 / M10 | 7,6 kg |

**Methanol-Verbrauch:**

```
EFOY Comfort 210:
  105 W Dauerleistung
  Methanol-Verbrauch: 0,9 l/kWh
  Energiegehalt M10-Patrone (10 l): ca. 11 kWh
  Laufzeit mit einer M10: ca. 4,5 Tage (Dauerbetrieb)

Kosten:
  M10-Patrone: ca. 55–65 EUR
  Kosten/kWh: 5,50–6,50 EUR/kWh (!)
  → Deutlich teurer als Diesel-Generator
  → Vorteil: Zero-Emission-Zonen, Nachtbetrieb ohne Laerm
```

**EFOY Besonderheiten:**
- **Vollautomatisch:** Startet/stoppt SOC-basiert
- **Null Laerm:** Nahezu geraeuschlos (<25 dB(A))
- **Keine Wartung:** Kein Oelwechsel, kein Filter (ausser Stack-Austausch nach Lebensdauer)
- **Frostfest:** Betrieb bis -20°C (mit Vorheizung)
- **Emissionsarm:** CO₂ + H₂O (kein NOx, kein Russ)
- **Nachteil:** Hohe Betriebskosten, geringe Leistung fuer Preis

### 4.7 Weitere Hersteller und Modelle

**Northern Lights (USA):**

| Modell | Leistung (kW) | Motor | Gewicht | Besonderheit |
|---|---|---|---|---|
| M673L3 | 6,0 | Mitsubishi S3L2 | 195 kg | Ultra-leise (54 dB) |
| M843NW | 8,0 | Mitsubishi S4L2 | 245 kg | Kielgekuehlt |
| M944T3 | 12,0 | Mitsubishi S4L2-T | 290 kg | Turbomotor |
| M1064T3 | 16,0 | Lugger 2CYL | 380 kg | Heavy Duty |
| M1273A3 | 20,0 | Lugger 3CYL | 480 kg | 3-Phase |

**Mastervolt Whisper (Niederlande):**

| Modell | Leistung (kW) | Technologie | Besonderheit |
|---|---|---|---|
| Whisper 3500 | 3,5 | DC-Variable-Speed | 48V DC-Ausgang |
| Whisper 5000 | 5,0 | DC-Variable-Speed | SystemBus-Integration |
| Whisper 7000 | 7,0 | DC-Variable-Speed | CZone-kompatibel |

**Mase (Italien):**

| Modell | Leistung (kW) | Motor | Gewicht |
|---|---|---|---|
| IS 2.6 | 2,5 | Yanmar L48 | 68 kg |
| IS 3.5 | 3,5 | Yanmar L70 | 82 kg |
| IS 5.0 | 5,0 | Kubota Z482 | 110 kg |
| IS 7.0 | 7,0 | Kubota D722 | 145 kg |
| IS 9.0 | 9,0 | Kubota D902 | 175 kg |
| IS 14.0 | 14,0 | Kubota V1505 | 310 kg |

---

## 5. Hersteller-Datenbank

### 5.1 Fischer Panda GmbH

| Attribut | Wert |
|---|---|
| **Firma** | Fischer Panda GmbH |
| **Sitz** | Paderborn, Deutschland |
| **Gruendung** | 1977 |
| **Spezialitaet** | Schallgedaemmte Variable-Speed Marine-Generatoren |
| **Leistungsbereich** | 3–150 kW |
| **Technologie** | PMG + Inverter (iSeries), Festdrehzahl (AGT) |
| **Motoren** | Kubota, Yanmar |
| **Besonderheit** | Kielkuehlung, iControl, 3-Punkt-Lagerung |
| **Zertifizierung** | CE, ABYC, GL/DNV, Lloyd's |
| **Service-Netz** | >80 Laender, >200 autorisierte Haendler |
| **Website** | fischerpanda.de |
| **Preis-Segment** | Premium (oberes Drittel) |
| **Garantie** | 2 Jahre / 2.000 h (verlaengerbar) |

### 5.2 Whisper Power B.V.

| Attribut | Wert |
|---|---|
| **Firma** | Whisper Power B.V. |
| **Sitz** | Drunen, Niederlande |
| **Gruendung** | 2002 |
| **Spezialitaet** | Kompakte Variable-Speed Generatoren, Energiesysteme |
| **Leistungsbereich** | 2,5–15 kW |
| **Technologie** | Genverter (PMG + IGBT), DC-Hybrid |
| **Motoren** | Yanmar, Kubota |
| **Besonderheit** | Sehr kompakt, NMEA2000-nativ, System-Integration |
| **Zertifizierung** | CE, ABYC, GL |
| **Service-Netz** | Europa, USA, Australien, 60+ Laender |
| **Website** | whisperpower.com |
| **Preis-Segment** | Mittel-Premium |
| **Garantie** | 2 Jahre / 2.000 h |

### 5.3 Cummins/Onan

| Attribut | Wert |
|---|---|
| **Firma** | Cummins Inc. (Marine Division, ehem. Onan) |
| **Sitz** | Columbus, Indiana, USA |
| **Gruendung** | 1920 (Onan), 1986 Akquisition durch Cummins |
| **Spezialitaet** | Robuste Festdrehzahl-Generatoren, Superyacht-Aggregate |
| **Leistungsbereich** | 4–2.000 kW |
| **Technologie** | Synchrongenerator, Festdrehzahl, PowerCommand |
| **Motoren** | Cummins-eigen (A-Serie, QSB, QSL, QSK) |
| **Besonderheit** | Groesstes Service-Netz weltweit, Heavy Duty |
| **Zertifizierung** | CE, ABYC, ABS, DNV, Lloyd's, BV, RINA |
| **Service-Netz** | >6.000 Haendler weltweit |
| **Website** | cummins.com/marine |
| **Preis-Segment** | Mittel (klein), Premium (gross) |
| **Garantie** | 2 Jahre / 2.000 h (Standardgarantie) |

### 5.4 SFC Energy AG (EFOY)

| Attribut | Wert |
|---|---|
| **Firma** | SFC Energy AG |
| **Sitz** | Brunnthal, Deutschland |
| **Gruendung** | 2000 |
| **Spezialitaet** | Methanol-Brennstoffzellen (DMFC) |
| **Leistungsbereich** | 25–500 W (Marine-Bereich) |
| **Technologie** | Direkt-Methanol-Brennstoffzelle |
| **Brennstoff** | Methanol (proprietaere Tankpatronen M5, M10, M28) |
| **Besonderheit** | Null Laerm, null Vibration, vollautomatisch |
| **Zertifizierung** | CE, BSH-zugelassen |
| **Service-Netz** | Europa, 40+ Laender |
| **Website** | efoy-pro.com |
| **Preis-Segment** | Premium (hohe Investition + hohe Betriebskosten) |
| **Garantie** | 2 Jahre |

### 5.5 Watt & Sea

| Attribut | Wert |
|---|---|
| **Firma** | Watt & Sea SAS |
| **Sitz** | La Rochelle, Frankreich |
| **Gruendung** | 2010 |
| **Spezialitaet** | Hydrogeneratoren (Wasser-Schleppgeneratoren) |
| **Leistungsbereich** | 300–1.200 W |
| **Technologie** | Permanentmagnet-Generator, klappbarer Unterwasserpropeller |
| **Brennstoff** | Keiner (kinetische Energie des Wassers) |
| **Besonderheit** | Keine Emissionen, keine Wartung, MPPT-Laderegler |
| **Zertifizierung** | CE |
| **Service-Netz** | Europa, weltweiter Online-Vertrieb |
| **Website** | wattandsea.com |
| **Preis-Segment** | Premium |
| **Garantie** | 2 Jahre |

### 5.6 Paguro (Fisco Generators)

| Attribut | Wert |
|---|---|
| **Firma** | Fisco S.r.l. (Marke: Paguro) |
| **Sitz** | Ravenna, Italien |
| **Gruendung** | 1995 |
| **Spezialitaet** | Kompakte, preiswerte Marine-Generatoren |
| **Leistungsbereich** | 2–18 kW |
| **Technologie** | Synchrongenerator, Festdrehzahl |
| **Motoren** | Lombardini/Kohler, Fiat/FPT |
| **Besonderheit** | Gutes Preis-Leistungs-Verhaeltnis, Made in Italy |
| **Zertifizierung** | CE, RINA |
| **Service-Netz** | Europa, Mittelmeer-Raum stark |
| **Website** | paguro.it |
| **Preis-Segment** | Mittel (15–25% unter Fischer Panda) |
| **Garantie** | 2 Jahre / 1.500 h |

### 5.7 Northern Lights

| Attribut | Wert |
|---|---|
| **Firma** | Northern Lights Inc. (Tochter von Lugger/Alaska Diesel Electric) |
| **Sitz** | Seattle, Washington, USA |
| **Gruendung** | 1969 |
| **Spezialitaet** | Extrem leise Festdrehzahl-Generatoren, Langlebigkeit |
| **Leistungsbereich** | 5–99 kW |
| **Technologie** | Synchrongenerator, Festdrehzahl, eigene Motoren |
| **Motoren** | Mitsubishi, eigene Lugger-Motoren |
| **Besonderheit** | 12.000-h-Service-Intervall, minimale Vibration |
| **Zertifizierung** | ABYC, CE, GL, Lloyd's |
| **Service-Netz** | USA stark, weltweit >50 Laender |
| **Website** | northern-lights.com |
| **Preis-Segment** | Premium |
| **Garantie** | 5 Jahre / 5.000 h (!) |

### 5.8 Mastervolt (Whisper)

| Attribut | Wert |
|---|---|
| **Firma** | Mastervolt (Teil von Power Solutions International) |
| **Sitz** | Amsterdam, Niederlande |
| **Gruendung** | 1991 |
| **Spezialitaet** | DC-Generatoren, Energiemanagement-Systeme |
| **Leistungsbereich** | 3,5–7 kW (Whisper-Serie) |
| **Technologie** | DC-Variable-Speed-Generator + externe Inverter |
| **Besonderheit** | Perfekte Integration in MasterBus/CZone-Systeme |
| **Zertifizierung** | CE, ABYC, GL |
| **Service-Netz** | Weltweit ueber Mastervolt-Haendler |
| **Website** | mastervolt.com |
| **Preis-Segment** | Premium |
| **Garantie** | 2 Jahre |

---

## 6. Fehlerbild-Atlas

### 6.1 Generator startet nicht

**Symptom:** Starter dreht, Motor springt nicht an. Oder: Starter dreht nicht.

**Visuelle Indikatoren:**
- Kein Abgas sichtbar beim Startversuch
- Kraftstoff-Leckage am Injektor/Filter
- Korrodierte Batteriepole
- Sicherungsausfall (durchgebrannt) am Starterpanel
- Gealterter/rissiger Kraftstoffschlauch

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| Batterie entladen/defekt | 30% | Mittel | Gering (Laden/Tauschen) |
| Kraftstofffilter verstopft | 20% | Mittel | Gering (Filter tauschen) |
| Luft im Kraftstoffsystem | 15% | Mittel | Gering (Entlueften) |
| Vorgluehanlagen defekt | 12% | Mittel | Mittel |
| Kraftstoffhebelpumpe defekt | 8% | Mittel | Mittel |
| Einspritzduesen verkokt | 5% | Hoch | Hoch |
| Stopmagnet/Abstellhebel defekt | 5% | Mittel | Mittel |
| Motorsteuerung/ECU Fehler | 3% | Hoch | Hoch |
| Kompression ungenuegend | 2% | Sehr hoch | Sehr hoch |

### 6.2 Generator laeuft, erzeugt keine Spannung

**Symptom:** Motor laeuft normal, Drehzahl stimmt, aber Ausgangsspannung = 0V oder sehr niedrig.

**Visuelle Indikatoren:**
- Durchgebrannte Sicherung am AVR
- Verfaerbte/geschmolzene Kabel im Klemmenkasten
- Kondenswasser im Generatorgehaeuse
- Korrodierte Schleifring-Kontakte (bei buerstenbehafteten Generatoren)

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| AVR defekt | 35% | Hoch | Mittel (AVR tauschen) |
| Erregerwicklung unterbrochen | 20% | Hoch | Hoch |
| Buerstenverschleiss | 15% | Mittel | Gering (Buersten tauschen) |
| Restmagnetismus verloren | 10% | Mittel | Gering (Flashen) |
| Statorwicklung Kurzschluss | 8% | Sehr hoch | Sehr hoch (Neuwicklung) |
| Diodenbruecke defekt (buerstenlos) | 7% | Hoch | Mittel |
| Kabelbruch intern | 5% | Mittel | Mittel |

**Sofortmassnahme bei Magnetismus-Verlust (Flashen):**
```
12V-Batterie kurz (1–2 s) an Erregerwicklung anlegen:
  - Plus an F+ des AVR
  - Minus an F- des AVR
  - Motor muss dabei laufen
  → Remanenz wird wiederhergestellt
  → Generator erzeugt wieder Spannung
```

### 6.3 Instabile Frequenz / Drehzahlschwankungen

**Symptom:** Frequenz schwankt (hoerbar als "Heulen"), Verbraucher blinken, Motorgeraeusch unregelmaessig.

**Visuelle Indikatoren:**
- Flackernde Bordbeleuchtung
- Klackernde Relais
- Schwarzer Rauch bei Drehzahlerhoehung
- Unregelmaessiger Auspuff-Wasserfluss

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| Drehzahlregler (Governor) verstellt | 25% | Mittel | Gering (Einstellen) |
| Kraftstoff-Verunreinigung (Wasser/Algen) | 20% | Mittel | Mittel (Tankreinigung) |
| Einspritzpumpe verschlissen | 15% | Hoch | Hoch |
| Luft im Kraftstoffsystem | 12% | Mittel | Gering |
| Gasgesteuerte Einheit defekt | 10% | Hoch | Hoch (Elektr. Governor) |
| Lastspruenge durch defekten Verbraucher | 8% | Mittel | Mittel (Verbraucher finden) |
| Kompressionsungleichheit | 5% | Sehr hoch | Sehr hoch |
| Generatorlager defekt (mechanischer Widerstand) | 5% | Hoch | Mittel–Hoch |

### 6.4 Ueberhitzung / Kuehlung

**Symptom:** Motortemperatur steigt ueber Grenzwert, Alarm/Abschaltung. Oder: Kuehlwasser-Alarm.

**Visuelle Indikatoren:**
- Dampf aus Kuehler-Entlueftung
- Verfaerbtes/trubes Kuehlwasser (Rost, Oelvermischung)
- Weisse Kalkablagerungen an Waermetauscher-Anschluessen
- Zerrissener/aufgeloester Impeller (Gummireste)
- Verstopftes Seewassersieb (Muscheln, Tang)

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| Impeller defekt/verschlissen | 30% | Mittel | Gering (Impeller tauschen) |
| Seewassersieb verstopft | 20% | Mittel | Gering (Reinigung) |
| Thermostat defekt (geschlossen) | 15% | Mittel | Gering |
| Waermetauscher verkalkt/verstopft | 12% | Hoch | Mittel (chem. Reinigung) |
| Keilriemen gerissen (Wasserpumpe) | 8% | Mittel | Gering |
| Kuehlwasserverlust (Leck) | 7% | Hoch | Mittel (Leck finden) |
| Zylinderkopfdichtung defekt | 5% | Sehr hoch | Hoch |
| Kielkuehler-Bewuchs (bei Kielkuehlung) | 3% | Mittel | Mittel (Taucher/Kran) |

### 6.5 Oelverlust / Oelverbrauch

**Symptom:** Oelstand sinkt zwischen Wechselintervallen, Oelflecken unter Generator, blauer Rauch.

**Visuelle Indikatoren:**
- Oelspuren an Ventildeckeldichtung
- Blauer Abgasrauch (Oelverbrennung)
- Oel in der Bilge unter dem Generator
- Verfaerbung/Oel am Turbolader (falls vorhanden)
- Undichte Oelkuehler-Anschluesse

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| Ventildeckeldichtung undicht | 25% | Gering | Gering |
| Kurbelwellen-Simmerring undicht | 20% | Mittel | Mittel |
| Oelfilter-Dichtung undicht | 15% | Gering | Gering |
| Oelkuehler-Anschluss undicht | 12% | Mittel | Mittel |
| Kolbenringe verschlissen (blauer Rauch) | 10% | Sehr hoch | Sehr hoch |
| Turbolader-Dichtung (Oeleintritt) | 8% | Hoch | Hoch |
| Oelwanne-Dichtung | 5% | Mittel | Mittel |
| Zylinderbuechsen-Verschleiss | 5% | Sehr hoch | Sehr hoch |

### 6.6 Abnormale Vibrationen

**Symptom:** Starke Vibrationen, Resonanzgeraeusche im Rumpf, lockere Befestigungen.

**Visuelle Indikatoren:**
- Gerissene/gequetschte Schwingmetalle
- Lose Befestigungsschrauben
- Rissbildung an Montage-Fundamenten
- Gebrochene Abgasschlauch-Verbindungen
- Verrueckte/schiefe Ausrichtung Generator-Motor

**Ursachen-Matrix:**

| Ursache | Haeufigkeit | Schwere | Reparaturaufwand |
|---|---|---|---|
| Schwingmetalle gealtert/verhaertet | 30% | Mittel | Gering (Tausch) |
| Motorlagerung lose | 20% | Mittel | Gering |
| Zuendaussetzer (Unwucht) | 15% | Mittel | Mittel |
| Kupplung verschlissen | 12% | Hoch | Mittel–Hoch |
| Generatorlager defekt | 10% | Hoch | Mittel |
| Resonanz mit Rumpfstruktur | 8% | Mittel | Schwierig (Drehzahl/Masse aendern) |
| Schwungrad-Unwucht | 5% | Hoch | Hoch |

### 6.7 Schwarzer Rauch

**Symptom:** Dauerhaft schwarzer/dunkler Abgasrauch, nicht nur beim Kaltstart.

**Ursachen:**
- Luftfilter verstopft (60% der Faelle)
- Einspritzduesen verkokt/falsch eingestellt (20%)
- Ueberlastung (Generator zu klein fuer Last) (10%)
- Turbolader defekt (5%)
- Einspritzpumpe falsch eingestellt (5%)

**AYDI-Bewertung:**
- Schwarzer Rauch nur beim Kaltstart (erste 30 s): Normal
- Schwarzer Rauch bei Lastaufschaltung (5–10 s): Akzeptabel
- Schwarzer Rauch dauerhaft: **Mangel — sofortige Ursachenermittlung**

### 6.8 Weisser Rauch

**Symptom:** Weisser/grauer Abgasrauch nach der Warmlaufphase.

**Ursachen:**
- Zylinderkopfdichtung defekt (Wasser im Brennraum) — 40%
- Riss im Zylinderkopf — 15%
- Einspritzpumpe falsch eingestellt (zu spaet) — 20%
- Motor zu kalt (Thermostat defekt/offen) — 15%
- Kraftstoff-Qualitaet (Wasser im Diesel) — 10%

**Diagnose:** Kuehlwasserverlust + weisser Rauch = Zylinderkopfdichtung (KRITISCH, sofort abstellen).

### 6.9 Nasslaeufer (Wet Stacking)

**Symptom:** Schwarze, oelige Ablagerungen am Auspuffaustritt. Unrunder Lauf. Leistungsverlust. Typisch bei Generatoren, die dauerhaft mit <30% Last laufen.

**Mechanismus:**
```
Niedrige Last → niedrige Verbrennungstemperatur → unvollstaendige Verbrennung
→ unverbrannter Kraftstoff + Oel sammelt sich im Abgassystem
→ Ablagerungen in Zylindern, Ventilen, Turbolader, Abgassystem
→ Leistungsverlust → noch niedrigere Temperaturen → Teufelskreis
```

**Massnahmen:**
1. Last erhoehen auf >50% fuer 2–4 Stunden (Load Banking)
2. Kuenftig Mindestlast >30% sicherstellen
3. Variable-Speed-Generator (laeuft immer im Optimum) — langfristige Loesung
4. Hybrid-System mit Batterie (Generator nur bei hoher Last) — langfristige Loesung

### 6.10 Elektronik-Fehler (Variable-Speed)

**Symptom:** Fehlercodes auf Display, Abschaltung, verzerrte Ausgangsspannung, THD-Alarm.

**Typische Fehlercodes (Fischer Panda iSeries):**

| Code | Bedeutung | Massnahme |
|---|---|---|
| E01 | Ueberspannung DC-Zwischenkreis | Last reduzieren, Batterie pruefen |
| E02 | Unterspannung DC-Zwischenkreis | Generator-Drehzahl pruefen |
| E03 | Uebertemperatur Inverter | Kuehlung pruefen, Entlueftung freihalten |
| E04 | Ueberstrom Ausgang | Last reduzieren, Kurzschluss suchen |
| E05 | Kommunikationsfehler CAN | Kabelverbindung pruefen |
| E06 | Motorueberdrehzahl | Drehzahlsensor, Governor |
| E07 | Motor Uebertemperatur | Kuehlung (Impeller, Thermostat) |
| E08 | Niedriger Oeldruck | Oelstand, Oeldruckschalter |
| E09 | Generator-Phase-Fehler | Wicklung, Verdrahtung pruefen |
| E10 | THD zu hoch | Last-Typ pruefen (nicht-lineare Lasten) |

### 6.11 Kraftstoff-Kontamination

**Symptom:** Motorleistungsabfall, Filterverstopfung in kurzen Intervallen, Algenwachstum im Tank.

**Visuelle Indikatoren:**
- Dunkle/truebe Verfaerbung im Kraftstoff-Schauglas
- Schleimige Ablagerungen am Tankboden (Dieselpest)
- Schnelle Filterverfaerbung (braun/schwarz statt gelblich)
- Wasser im Wasserabscheider-Glas

**Dieselpest (Microbial Contamination):**
```
Bedingungen:
  - Kondenswasser im Tank (Temperaturwechsel)
  - Biodiesel-Anteil >5% (B5+)
  - Lange Standzeiten (>4 Wochen)

Organismen:
  - Hormoconis resinae (Pilz)
  - Pseudomonas aeruginosa (Bakterie)
  - Cladosporium resinae (Pilz)

Massnahmen:
  - Biozid (Grotamar 82): 1:2.000 (praventiv), 1:1.000 (Schockbehandlung)
  - Tankgrundreinigung + Trocknung
  - Regelmaessig Wasser abpumpen (alle 4 Wochen)
  - Diesel-Stabilisator bei Langzeitlagerung
```

### 6.12 Abgas-Wasserrueckfluss

**Symptom:** Seewasser gelangt rueckwaerts durch das Abgassystem in den Motor. Katastrophaler Motorschaden moeglich.

**Visuelle Indikatoren:**
- Wasser im Oelfilm (milchig-weisses Oel)
- Wasserstand im Zylinder beim Startversuch (hydraulischer Schlag!)
- Nassealagerungen am Auspuffkruemmer motorseitig
- Fehlende oder defekte Antisiphon-Ventile

**Ursachen:**
- Waterlock zu tief montiert (unterhalb Wasserlinie bei Kraengung)
- Antisiphon-Ventil defekt/verklebt
- Abgas-Schwanenhalsbogen zu niedrig
- Motor abgewuergt unter Last (Nachsaugen durch Restunterdruck)
- Wellengang drueckt Wasser zurueck

**Praevention:**
```
Mindesthoehe Schwanenhalsbogen ueber Wasserlinie:
  Segelyacht (mit Kraengung): min. 400 mm + max. Kraengung beruecksichtigen
  Motoryacht: min. 300 mm ueber WL

Antisiphon-Ventil: Pflicht in jeder Installation
  → Hoechster Punkt der Abgasleitung
  → Jaehrlich pruefen (Kalkverklebung)

Waterlock-Volumen: min. 150% des Leitungsvolumens zwischen Motor und Waterlock
```

---

## 7. Troubleshooting-Entscheidungsbaeume

### 7.1 Entscheidungsbaum: Generator startet nicht

```
START: Generator startet nicht
│
├─ Starter dreht NICHT
│  ├─ Batteriespannung <11,5V (12V-System) / <23V (24V-System)?
│  │  ├─ JA → Batterie laden oder tauschen
│  │  └─ NEIN
│  │     ├─ Sicherung/Automat Generator-Starter OK?
│  │     │  ├─ NEIN → Sicherung ersetzen, Ursache suchen
│  │     │  └─ JA
│  │     │     ├─ Startrelais/Magnetschalter klickt?
│  │     │     │  ├─ NEIN → Startrelais defekt, Verdrahtung pruefen
│  │     │     │  └─ JA
│  │     │     │     ├─ Starter-Motor defekt → Starter pruefen/tauschen
│  │     │     │     └─ Motor mechanisch blockiert → Handkurbel versuchen
│  │     │     └─ Notaus-Schalter/Sicherheitsschalter ausgeloest?
│  │     │        └─ JA → Reset, Ursache pruefen
│  │
├─ Starter dreht, Motor springt NICHT an
│  ├─ Kraftstoff vorhanden? (Tank-Anzeige, Sichtpruefung)
│  │  ├─ NEIN → Tanken
│  │  └─ JA
│  │     ├─ Kraftstoff erreicht Einspritzpumpe? (Entlueftungsschraube oeffnen)
│  │     │  ├─ NEIN → Luft im System ODER Filter verstopft ODER Hebelpumpe defekt
│  │     │  │  ├─ Filter pruefen/tauschen
│  │     │  │  ├─ Handpumpe betaetigen (Entlueften)
│  │     │  │  └─ Hebelpumpe pruefen
│  │     │  └─ JA → Kraftstoff da
│  │     │     ├─ Abstell-Solenoid/Stopventil aktiv (stromlos = geschlossen)?
│  │     │     │  ├─ JA → Solenoid-Versorgung pruefen, Kabel
│  │     │     │  └─ NEIN (Solenoid OK)
│  │     │     │     ├─ Vorgluehanlagen funktioniert? (Kontrollleuchte)
│  │     │     │     │  ├─ NEIN → Gluehkerzen/Relais pruefen
│  │     │     │     │  └─ JA
│  │     │     │     │     ├─ Kompression ausreichend? (Drehen hoert sich normal an?)
│  │     │     │     │     │  ├─ Auffaellig schnelles Drehen → Kompression weg
│  │     │     │     │     │  │  → Ventilspiel, Kopfdichtung, Kolbenringe
│  │     │     │     │     │  └─ Normal → Einspritzduesen pruefen lassen
│  │     │     │     │     └─ Einspritzzeitpunkt verstellt? → Werkstatt
```

### 7.2 Entscheidungsbaum: Keine Spannung am Ausgang

```
START: Generator laeuft, keine Spannung
│
├─ Drehzahl korrekt? (Frequenzmeter oder Gehoer)
│  ├─ NEIN → Drehzahl einstellen (Governor/Drehzahlregler)
│  └─ JA (Drehzahl OK)
│     ├─ Sicherungsautomat am Generator-Ausgang ausgeloest?
│     │  ├─ JA → Kurzschluss in Bordnetz suchen, Automat reset
│     │  └─ NEIN
│     │     ├─ Spannung direkt am Generator-Klemmenkasten messen
│     │     │  ├─ Spannung am Klemmenkasten vorhanden → Kabelfehler zum Panel
│     │     │  └─ Keine Spannung am Generator
│     │     │     ├─ AVR-Sicherung pruefen
│     │     │     │  ├─ Durchgebrannt → AVR-Sicherung ersetzen, Last reduzieren
│     │     │     │  └─ OK
│     │     │     │     ├─ Restspannung messbar (5–20V)?
│     │     │     │     │  ├─ JA → AVR wahrscheinlich defekt → tauschen
│     │     │     │     │  └─ NEIN (0 V)
│     │     │     │     │     ├─ Restmagnetismus verloren
│     │     │     │     │     │  → Flashen mit 12V-Batterie (2 s an Erregerwicklung)
│     │     │     │     │     │  → Wenn danach Spannung: AVR pruefen
│     │     │     │     │     │  → Wenn keine Spannung: Wicklung messen
│     │     │     │     │     │     ├─ Erregerwicklung: Widerstand messen (Sollwert im Handbuch)
│     │     │     │     │     │     │  ├─ ∞ Ohm → Unterbrechung → Wicklung/Buersten
│     │     │     │     │     │     │  ├─ 0 Ohm → Kurzschluss → Wicklung defekt
│     │     │     │     │     │     │  └─ Sollwert → Weiter
│     │     │     │     │     │     └─ Statorwicklung: Widerstand messen
│     │     │     │     │     │        ├─ Unsymmetrisch → Wicklungsschaden
│     │     │     │     │     │        └─ Symmetrisch → Diodenbruecke (bei buerstenlos)
│     │     │     │     │     └─ Buersten pruefen (bei buerstenbehaftetem Generator)
│     │     │     │     │        ├─ Verschlissen (<5 mm) → Buersten tauschen
│     │     │     │     │        └─ OK → Schleifring reinigen
```

### 7.3 Entscheidungsbaum: Ueberhitzung

```
START: Generator ueberhitzt / Temperaturalarm
│
├─ Seewasserdurchfluss pruefen (Auspuff-Wasseraustritt)
│  ├─ KEIN Wasser am Auspuff
│  │  ├─ Seeventil offen?
│  │  │  ├─ NEIN → Seeventil oeffnen (!)
│  │  │  └─ JA
│  │  │     ├─ Seewassersieb verstopft? (Tang, Muscheln, Plastik)
│  │  │     │  ├─ JA → Reinigen
│  │  │     │  └─ NEIN
│  │  │     │     ├─ Impeller pruefen
│  │  │     │     │  ├─ Fluegel abgebrochen/verschlissen → Tauschen + Reste suchen!
│  │  │     │     │  └─ Impeller OK
│  │  │     │     │     ├─ Seewasserschlauch geknickt/verstopft?
│  │  │     │     │     └─ Seewasserpumpen-Gehaeuse ausgeschlagen?
│  │  │     │     └─ Seewasserleitung verstopft (Kalk, Muscheln intern)
│  │  └─ ACHTUNG: Impeller-Reste koennen Waermetauscher verstopfen!
│  │
├─ Wasser kommt am Auspuff (Seewasser-Kreislauf OK)
│  ├─ Suesswasser-Kreislauf pruefen
│  │  ├─ Kuehlwasserstand OK? (Ausgleichsbehaelter)
│  │  │  ├─ NEIN → Nachfuellen + Leck suchen
│  │  │  └─ JA
│  │  │     ├─ Thermostat pruefen (in heissem Wasser testen, oeffnet bei ~75–82°C?)
│  │  │     │  ├─ Defekt (bleibt geschlossen) → Tauschen
│  │  │     │  └─ OK
│  │  │     │     ├─ Waermetauscher-Effizienz → Reinigung/Tausch
│  │  │     │     ├─ Keilriemen Wasserpumpe rutscht/gerissen?
│  │  │     │     └─ Zylinderkopfdichtung → Kompressionsdrucktest, CO₂-Test im Kuehlwasser
│  │  └─ Bei Kielkuehlung: Kiel-Kuehlelemente auf Bewuchs pruefen (Taucher)
│  │
├─ Luft-Seite pruefen
│  ├─ Luftfilter verstopft?
│  │  ├─ JA → Reinigen/Tauschen
│  │  └─ NEIN
│  │     ├─ Maschinenraum-Belueftung ausreichend? (Zuluft!)
│  │     │  ├─ NEIN → Zuluft-Oeffnungen vergroessern
│  │     │  └─ JA → Motor intern (Einspritzzeitpunkt, Ventilspiel)
```

### 7.4 Entscheidungsbaum: Abnormale Vibrationen

```
START: Starke Vibrationen
│
├─ Vibrationen bei ALLEN Drehzahlen oder nur bei bestimmter Drehzahl?
│  ├─ Nur bei bestimmter Drehzahl → RESONANZ
│  │  ├─ Drehzahl aenderbar (Variable Speed)?
│  │  │  ├─ JA → Resonanzdrehzahl ausblenden (Sperrbereich programmieren)
│  │  │  └─ NEIN
│  │  │     ├─ Masse am Fundament aendern (Versteifung)
│  │  │     ├─ Schwingmetall-Haerte aendern
│  │  │     └─ Absorber-Masse anbringen
│  │  │
│  └─ Bei ALLEN Drehzahlen → Mechanische Ursache
│     ├─ Schwingmetalle pruefen
│     │  ├─ Gealtert/gerissen/verhaertet → Tauschen (Shore-Haerte beachten)
│     │  ├─ Schrauben lose → Nachziehen mit Drehmoment
│     │  └─ OK
│     │     ├─ Kupplung Motor-Generator pruefen
│     │     │  ├─ Gummielemente verschlissen → Kupplung tauschen
│     │     │  ├─ Fluchtung Motor-Generator (Alignment) pruefen
│     │     │  │  → Max. 0,1 mm Versatz, 0,05 mm/100 mm Winkel
│     │     │  └─ OK
│     │     │     ├─ Zuendaussetzer? (OBD-Fehlerspeicher, Abgasfarbe)
│     │     │     │  ├─ JA → Einspritzduese, Gluehkerze, Kompression
│     │     │     │  └─ NEIN
│     │     │     │     ├─ Generatorlager pruefen (Geraeusch, Spiel)
│     │     │     │     └─ Schwungrad-Befestigung, Schwingungsdaempfer
│     │     │     └─ Abgasleitung: flexible Verbindung vorhanden?
│     │     │        └─ Falls starr: flexible Muffe einbauen
```

### 7.5 Entscheidungsbaum: Variable-Speed-Elektronik-Fehler

```
START: Elektronik-Fehler (Fehlermeldung/Abschaltung)
│
├─ Fehlerspeicher auslesen (iControl/Display/Service-Tool)
│  ├─ Uebertemperatur Inverter (E03/aehnlich)
│  │  ├─ Zuluft zum Inverter-Gehaeuse frei? (Luefter-Gitter sauber?)
│  │  │  ├─ NEIN → Reinigen, Luftzufuhr sicherstellen
│  │  │  └─ JA
│  │  │     ├─ Umgebungstemperatur >45°C? (Maschinenraum zu heiss)
│  │  │     │  ├─ JA → Maschinenraum-Belueftung verbessern
│  │  │     │  └─ NEIN → Luefter im Inverter defekt → Service
│  │  │
│  ├─ Ueberspannung/Unterspannung DC-Bus (E01/E02)
│  │  ├─ Batteriespannung am Generator messen
│  │  │  ├─ <10V (12V-Sys.) oder <20V (24V) → Batterie, Kabelverbindung
│  │  │  ├─ >15V (12V-Sys.) oder >30V (24V) → Laderegler, Batterie defekt
│  │  │  └─ Normal → Internes Problem → Service
│  │  │
│  ├─ Ueberstrom (E04)
│  │  ├─ Kurzschluss im AC-Netz? (Isolationswiderstand messen)
│  │  │  ├─ JA → Kurzschluss lokalisieren und beheben
│  │  │  └─ NEIN
│  │  │     ├─ Verbraucher-Anlaufstrom zu hoch? (Klimakompressor, Wassermacher)
│  │  │     │  ├─ JA → Sanftanlauf installieren, Last reduzieren
│  │  │     │  └─ NEIN → IGBT-Modul im Inverter defekt → Werkstatt
│  │  │
│  ├─ Kommunikationsfehler CAN (E05)
│  │  ├─ CAN-Bus-Kabel pruefen (Korrosion, Bruch, Abschirmung)
│  │  ├─ CAN-Terminierung vorhanden? (120 Ohm an beiden Enden)
│  │  └─ Software-Version kompatibel? (Update noetig?)
│  │
│  └─ Motorschutz (E06–E08)
│     ├─ Ueberdrehzahl → Drehzahlsensor, Governor/ECU
│     ├─ Uebertemperatur → siehe Baum 7.3
│     └─ Oeldruck → Oelstand, Oeldruckschalter, Oelpumpe
```

---

## 8. FAQ

### 8.1 Grundlagen

**F1: Wie gross muss mein Generator sein?**
A: Erstellen Sie eine Leistungsbilanz aller gleichzeitig laufenden Verbraucher. Addieren Sie die Wirkleistungen, dividieren durch den mittleren Leistungsfaktor (typisch 0,8), und multiplizieren mit Faktor 1,25 (25% Reserve). Beispiel: 4.000 W Verbrauch → 4.000/0,8 × 1,25 = 6.250 VA → 6,5 kVA Generator waehlen.

**F2: Festdrehzahl oder Variable Speed?**
A: Variable Speed bei Teillastbetrieb (Segelyachten, selten Volllast), wenn Laermreduzierung wichtig ist und Budget vorhanden. Festdrehzahl wenn hohe Zuverlaessigkeit, einfache Wartung und niedrigere Anschaffungskosten Prioritaet haben.

**F3: 1.500 oder 3.000 U/min?**
A: 1.500 U/min (4-polig): leiser, laenger Lebensdauer, schwerer, teurer. Empfohlen ab 6 kW und fuer komfort-orientierte Yachten. 3.000 U/min (2-polig): kompakter, leichter, guenstiger, lauter, kuerzere Lebensdauer. Akzeptabel bis 5 kW oder wenn Bauraum/Gewicht kritisch.

**F4: Wie viel Kraftstoff verbraucht ein Generator?**
A: Faustregel: 0,3–0,4 Liter Diesel pro erzeugte kWh bei Festdrehzahl (75% Last). Ein 6-kW-Generator bei 75% Last verbraucht ca. 1,5–2,0 l/h. Variable-Speed-Generatoren liegen 20–35% niedriger bei Teillast.

**F5: Kann ich meinen Generator auch 24 Stunden durchlaufen lassen?**
A: Ja, sofern: Last dauerhaft >30% (kein Nasslauf), Kuehlung ausreichend, Kraftstoff vorratig, Oelstand ausreichend fuer Intervall. Dauerleistung (Continuous Rating, COP) des Generators beachten — nicht PRP (Prime Power) oder ESP (Emergency Standby).

### 8.2 Dimensionierung und Installation

**F6: Brauche ich einen Generator wenn ich Solarpanels und Lithium-Batterien habe?**
A: Abhaengig vom Verbrauchsprofil. Wenn Sie Klimaanlage, Wassermacher oder elektrisches Kochen nutzen, reicht Solar selten aus. Faustformel: Tagesverbrauch >3.000 Wh mit Klimaanlage → Generator sinnvoll. Ohne Klimaanlage und mit >600 Wp Solar + >400 Ah LiFePO₄ kann ein Generator entfallen (Fahrtensegler Tropen).

**F7: Wo installiere ich den Generator am besten?**
A: Moeglichst tief (Schwerpunkt), nahe der Bootsmitte (Trimmung), mit: (1) ausreichender Zuluft (min. 0,05 m² pro 10 kW), (2) freiem Zugang fuer Wartung (Oelwechsel, Filter, Impeller), (3) flexiblen Verbindungen (Abgas, Kuehlung, Elektrik, Kraftstoff), (4) Schwingungsisolierung zum Rumpf.

**F8: Welchen Kabelquerschnitt braucht die AC-Leitung vom Generator?**
A: Berechnung nach Strom und Laenge. Beispiel: 6 kW Generator, 230V, 26 A, 8 m Leitungslaenge, max. 3% Spannungsabfall → 6 mm² mindestens. Generell: AC-Zuleitungen vom Generator 4–10 mm² je nach Leistung und Laenge.

**F9: Ist Kielkuehlung besser als Seewasserkuehlung?**
A: Kielkuehlung eliminiert Impeller-Verschleiss (haeufigste Ausfallursache!), Seewassersieb-Verstopfung und Seewasser-Einlass. Nachteile: teurer, braucht mehr Rumpfflaeche, geringere Kuehlleistung bei warmem Wasser (>30°C). Ideal fuer Langfahrt und Aluminium-Yachten.

**F10: Wie sichere ich den Generator gegen Wasserrueckfluss im Abgassystem?**
A: (1) Antisiphon-Ventil am hoechsten Punkt der Abgasleitung, (2) Schwanenhalsbogen min. 300–400 mm ueber Wasserlinie, (3) Waterlock-Volumen min. 150% des Leitungsvolumens Motor→Waterlock, (4) Abgas-Rueckschlagklappe bei Heckwellen-gefaehrdeten Booten.

### 8.3 Betrieb und Wartung

**F11: Wie oft muss ich das Oel wechseln?**
A: Erste Oelwechsel nach 50 h (Einlaufoel). Danach: alle 100–250 h je nach Hersteller. Fischer Panda iSeries: 500 h. Onan: 150 h. Paguro: 200 h. Bei geringer Nutzung (<100 h/Jahr): mindestens einmal jaehrlich.

**F12: Welches Oel verwende ich?**
A: Marine-Dieselmotoroel SAE 15W-40 (mineralisch) oder 5W-40 (synthetisch). API-Klasse mindestens CI-4 oder CJ-4. NICHT PKW-Oel (fehlt Korrosionsschutz fuer marine Bedingungen). Hersteller-Freigabe beachten.

**F13: Wie oft den Impeller wechseln?**
A: Alle 250–500 Betriebsstunden ODER jaehrlich (Gummi altert auch ohne Betrieb). Bei Trockenlauf (vergessenes Seeventil): sofort. Immer Ersatz-Impeller an Bord haben — ist der haeufigste Grund fuer Generator-Ausfall.

**F14: Was tun bei laengerem Nichtgebrauch?**
A: (1) Tank voll fuellen (kein Kondenswasser), (2) Dieselstabilisator zugeben, (3) Generator 30 min unter Last laufen lassen, (4) Suesswasser-Kuehlsystem mit Frostschutz, (5) Seewasserseite entleeren, (6) Monatlich 15 min unter Last starten, (7) Batterie am Ladeerhaltungsgeraet.

**F15: Mein Generator raucht beim Kaltstart — ist das normal?**
A: Leichter weiss-blauer Rauch fuer 30–60 Sekunden bei Kaltstart ist normal (unverbrannter Kraftstoff bei kaltem Motor). Sollte nach Erreichen der Betriebstemperatur verschwinden. Dauerhafter Rauch nach 2–3 Minuten: Mangel (→ Fehlerbild 6.7/6.8).

**F16: Generator-Notstart bei kalter Batterie — was tun?**
A: (1) Vorgluehanlagen mehrfach betaetigen (3× je 15 s), (2) Falls startbar: 5 min im Leerlauf warmlaufen lassen, (3) Starthilfe von Bordbatterie-Bank (Vorsicht: Querschnitt!), (4) Notfall: Aether/Startpilot (nur einmalig, schaedigt Motor auf Dauer).

### 8.4 Spezialfragen

**F17: Kann ich Generator und Landstrom gleichzeitig nutzen?**
A: NEIN ohne Synchronisierung. Generatorstrom und Landstrom muessen ueber eine Umschaltung (manuell oder automatisch ATS — Automatic Transfer Switch) getrennt werden. Parallelbetrieb nur mit synchronisierungsfaehigen Systemen (Superyacht-Klasse).

**F18: Wie verbinde ich Generator, Wechselrichter und Landstrom?**
A: Empfohlene Hierarchie: Landstrom (Prioritaet 1) → Generator (Prioritaet 2) → Inverter (Prioritaet 3). Automatische Umschaltung durch ATS oder integrierte Inverter/Charger (Victron MultiPlus, Mastervolt CombiMaster). Generator startet automatisch bei niedrigem SOC, wenn kein Landstrom.

**F19: Brauche ich bei Lithium-Batterien einen speziellen Generator?**
A: Der Generator selbst muss nicht speziell sein, aber: Lithium-Batterien akzeptieren sehr hohe Ladeströme (1C und mehr). Ein zu kleiner Generator wird von einem Hochleistungs-Ladegeraet überlastet. Ladestrom auf 50–70% der Generator-Nennleistung begrenzen. BMS muss Ladegeraet abschalten koennen.

**F20: Ist ein Hydrogenerator ein vollwertiger Ersatz fuer einen Diesel-Generator?**
A: Nein. Ein Hydrogenerator liefert max. 500–1.200 W (nur unter Segel, ab 5+ kn). Er ist ideal als Ergaenzung zum Diesel-Generator oder als Hauptquelle fuer Segelyachten mit niedrigem Verbrauch (<2.000 Wh/Tag) und ausreichend Segeltagen.

**F21: Wie laut darf ein Generator im Hafen sein?**
A: Abhaengig von lokalen Hafenordnungen. Typisch: max. 50 dB(A) am naechsten Nachbar-Boot (nachts). Generator mit <52 dB(A) bei 7 m: Fischer Panda iSeries, Whisper Power M-GV. Uebliche Einschraenkung: kein Generatorbetrieb 22:00–07:00.

**F22: Was kostet der Austausch einer Fischer Panda iSeries-Elektronik?**
A: Inverter-Board: 2.500–5.000 EUR je nach Modell. iControl-Display: 800–1.500 EUR. AVR/Erreger-Modul: 600–1.200 EUR. Arbeitslohn: 2–4 Stunden (400–800 EUR). Gesamt typisch: 3.500–7.000 EUR fuer Elektronik-Totalausfall.

**F23: Brennstoffzelle oder Diesel-Generator fuer Langfahrt?**
A: Diesel-Generator fuer Langfahrt bevorzugt: Weltweit Diesel verfuegbar, hohe Leistung, bewaehrte Technik, Service ueberall. Brennstoffzelle (EFOY) als Ergaenzung fuer Nacht-Ladung (leise) und Naturschutzgebiete (emissionsfrei). Als alleinige Quelle fuer >5.000 Wh/Tag nicht wirtschaftlich.

**F24: Wie integriere ich den Generator in ein NMEA2000-Netzwerk?**
A: Die meisten modernen Generatoren bieten NMEA2000-Gateways (Fischer Panda, Whisper Power nativ; Onan via Maretron-Gateway). Uebertragene Daten: Betriebsstunden, Temperatur, Oeldruck, Ausgangsspannung/-strom, Kraftstoffverbrauch, Alarme. PGN 127488ff.

**F25: Wann lohnt sich ein zweiter Generator (Redundanz)?**
A: Ab 18–20 m Bootslaenge ODER wenn staendig AC-kritische Systeme laufen (Klimaanlage Tropensegeln, medizinische Geraete, Charter-Betrieb). Empfohlen: 2× 60–70% statt 1× 100%. Ein Generator kann ausfallen, der andere uebernimmt Grundlast.

**F26: Welche Emissionsvorschriften gelten?**
A: EU: Stage V (ab 2019, <19 kW exempt bis 2025). USA: EPA Tier 3/4. IMO: Tier II (MARPOL Annex VI). In der Praxis: Marine-Generatoren <19 kW waren lange ausgenommen. Ab 2024 gelten auch fuer kleine Marine-Motoren strengere Grenzwerte (RCD 2013/53/EU).

**F27: Kann ich meinen Generator mit HVO/GTL-Diesel betreiben?**
A: Ja. HVO (Hydrated Vegetable Oil) / GTL (Gas-to-Liquid) sind paraffinische Dieselkraftstoffe nach EN 15940. Vorteile: weniger Partikel, besser lagerbar (keine Dieselpest), kaeltetauglich. Alle modernen Diesel-Generatoren sind kompatibel. Dichtungen pruefen bei aelteren Modellen.

**F28: Was ist ein DC-Hybrid-System und wann ist es sinnvoll?**
A: DC-Hybrid: Generator erzeugt DC-Strom (oder wird gleichgerichtet) → DC-Sammelschiene (48V) → Batterien + Inverter. Sinnvoll wenn: mehrere DC-Quellen (Solar, Hydro, Wind, Generator), Batterie als Puffer, Verbraucher ueberwiegend DC oder ueber einen grossen Inverter versorgt. Erspart AC-Synchronisierung.

### 8.5 Hydrogeneratoren

**F29: Stoert ein Hydrogenerator beim Segeln?**
A: Minimaler Geschwindigkeitsverlust: 0,1–0,5 kn je nach Typ und Geschwindigkeit. Bei klappbarem Propeller (Watt & Sea): unter Motor fast kein Widerstand. Psychologisch: Die "kostenlose" Energie motiviert zum Segeln statt Motoren.

**F30: Kann ich den Hydrogenerator auch unter Motor nutzen?**
A: Ja, aber unwirtschaftlich. Der Diesel-Motor treibt das Boot an, der Hydrogenerator wandelt einen Teil dieser Energie zurueck in Strom — mit Verlusten. Effizienter ist eine Hochleistungs-Lichtmaschine direkt am Motor. Ausnahme: Saildrive-Regeneration bei Elektromotor-Antrieb.

---

## 9. Glossar

| Begriff | Erklaerung |
|---|---|
| **AVR** | Automatic Voltage Regulator — Spannungsregler des Generators, haelt Ausgangsspannung konstant |
| **be / SFOC** | Spezifischer Kraftstoffverbrauch (brake specific fuel consumption), Angabe in g/kWh |
| **Buerstenloser Generator** | Generator ohne Schleifringe/Buersten, Erregung ueber rotierende Dioden |
| **CAN-Bus** | Controller Area Network — digitaler Kommunikationsbus (Fischer Panda iControl) |
| **COP** | Continuous Operating Power — Dauerlast-Nennleistung (unbegrenzte Betriebszeit) |
| **cos φ** | Leistungsfaktor — Verhaeltnis Wirkleistung zu Scheinleistung |
| **Dieselpest** | Mikrobielle Kontamination im Dieselkraftstoff (Pilze, Bakterien) |
| **DMFC** | Direct Methanol Fuel Cell — Direkt-Methanol-Brennstoffzelle (EFOY) |
| **Droop** | Frequenzabsenkung proportional zur Last (Regelverhalten) |
| **Enclosure** | Schallkapsel / Schalldaemmgehaeuse um den Generator |
| **ESP** | Emergency Standby Power — Notleistung (max. 500 h/Jahr, variabel belastet) |
| **Erregerwicklung** | Feldwicklung im Rotor, erzeugt das Magnetfeld |
| **Flashen** | Wiederherstellung des Restmagnetismus durch kurzzeitige Gleichstromerregung |
| **Genverter** | Generator + Inverter — Whisper Power-Bezeichnung fuer Variable-Speed-System |
| **Governor** | Drehzahlregler — mechanisch (Fliehkraft) oder elektronisch (ECU-gesteuert) |
| **Hydrogenerator** | Stromerzeuger angetrieben durch Wasserbewegung (Fahrt/Stroemung) |
| **IGBT** | Insulated Gate Bipolar Transistor — Leistungshalbleiter im Inverter |
| **Impeller** | Gummi-Fluegelrad der Seewasserpumpe (Verschleissteil Nr. 1) |
| **Inverter** | Wechselrichter — wandelt DC in AC (oder variable AC in stabile AC) |
| **Isochronous** | Frequenzregelung die Last-unabhaengig konstante Frequenz haelt |
| **IT-Netz** | Isoliertes Stromnetz (kein Sternpunkt-Erde-Verbindung) — Marine-Standard |
| **Kielkuehlung** | Geschlossenes Kuehlsystem mit Waermeabgabe ueber Rumpf-Platten |
| **kVA** | Kilo-Volt-Ampere — Scheinleistung (Nenngroesse von Generatoren) |
| **kW** | Kilo-Watt — Wirkleistung (tatsaechlich nutzbare Leistung) |
| **Load Banking** | Betrieb unter kuenstlich hoher Last zur Beseitigung von Nasslaeufer-Ablagerungen |
| **Load Shedding** | Prioritaets-basierter Lastabwurf bei Ueberlast |
| **MPPT** | Maximum Power Point Tracking — Laderegler-Algorithmus (Hydrogenerator) |
| **Nasslaeufer / Wet Stacking** | Ablagerungen durch dauerhaften Teillastbetrieb <30% |
| **NMEA2000** | Digitales Bord-Kommunikationsnetzwerk (CAN-basiert) |
| **PEM** | Proton Exchange Membrane — Wasserstoff-Brennstoffzellen-Typ |
| **PMG** | Permanent Magnet Generator — Generator mit Permanentmagneten im Rotor |
| **PRP** | Prime Power — Dauerleistung mit variabler Last (unbegrenzte Betriebszeit) |
| **Restmagnetismus / Remanenz** | Verbleibender Magnetismus im Rotor nach Abschaltung (noetig fuer Selbsterregung) |
| **Shore-Haerte** | Haertenmass fuer Elastomere (Schwingmetalle), typisch 40–70 Shore A |
| **SOFC** | Solid Oxide Fuel Cell — Festoxid-Brennstoffzelle (Hochtemperatur) |
| **Synchrongenerator** | Generator dessen Rotordrehzahl exakt der Netzfrequenz entspricht |
| **THD** | Total Harmonic Distortion — Klirrfaktor der Ausgangsspannung (Qualitaetsmass) |
| **VSD / Variable Speed** | Variable Drehzahl — Generatorbetrieb mit lastabhaengiger Drehzahl |
| **Waterlock** | Kondensatfalle im Nassauspuff, verhindert Wasserrueckfluss zum Motor |
| **Wet Exhaust** | Nassauspuff — Seewasser wird in den Abgasstrom eingespritzt zur Kuehlung |

---

## 10. Schnell-Referenz

### 10.1 Generator-Auswahl nach Bootsgrösse

| Boot | Verbrauch/Tag | Generator | Empfehlung |
|---|---|---|---|
| Segelyacht 8–10 m | 1.500–2.500 Wh | 2–3 kW | Piccolo 3, Paguro 2000, Hydrogenerator |
| Segelyacht 11–13 m | 2.500–5.000 Wh | 3–5 kW | Panda 4000i, M-GV 4, EFOY+Solar |
| Segelyacht 14–17 m | 5.000–10.000 Wh | 5–8 kW | Panda 8000i, M-GV 7, Onan 7.5 |
| Motoryacht 10–13 m | 5.000–12.000 Wh | 5–8 kW | Panda 8000i, Paguro 6500 |
| Motoryacht 14–18 m | 12.000–25.000 Wh | 8–15 kW | Panda 15000i, Onan 12, Paguro 12000 |
| Motoryacht 19–24 m | 25.000–50.000 Wh | 15–25 kW | Panda 25000i, Onan 21.5, Northern Lights |
| Superyacht 25–35 m | 50.000–120.000 Wh | 25–65 kW (2×) | Cummins QD, Fischer Panda 45000i |
| Megayacht 35+ m | 120.000–500.000 Wh | 65–200 kW (2–3×) | Cummins QD/Caterpillar/MTU |

### 10.2 Wartungsintervalle (Standardwerte)

| Massnahme | Intervall (Stunden) | Intervall (Zeit) | Kritisch |
|---|---|---|---|
| Oelstand pruefen | 50 | Woechentlich | Nein |
| Impeller pruefen | 250 | Jaehrlich | JA |
| Oelwechsel + Filter | 100–250 | Jaehrlich | JA |
| Kraftstofffilter | 250–500 | Jaehrlich | JA |
| Keilriemen | 500 | Alle 2 Jahre | Mittel |
| Ventilspiel | 1.000–2.000 | Alle 3–5 Jahre | Mittel |
| Kuehlwasser (Suesswasser) | 500 | Jaehrlich | Mittel |
| Zink-Anoden (Waermetauscher) | 250 | Halbjaehrlich | JA |
| Einspritzduesen pruefen | 2.000–3.000 | Alle 5 Jahre | Mittel |
| Schwingmetalle pruefen | 1.000 | Alle 3 Jahre | Mittel |
| Generallueberholung | 8.000–12.000 | Alle 10–15 Jahre | — |

### 10.3 Typische Fehlercodes Fischer Panda

| Code | Bedeutung | Sofortmassnahme |
|---|---|---|
| E01 | DC-Ueberspannung | Last pruefen, Batterie |
| E02 | DC-Unterspannung | Batteriekabel, Sicherung |
| E03 | Inverter heiss | Lueftung, Last reduzieren |
| E04 | AC-Ueberstrom | Last reduzieren |
| E05 | CAN-Fehler | Kabel, Terminierung |
| E06 | Ueberdrehzahl | Drehzahlsensor |
| E07 | Motor heiss | Kuehlung (Impeller!) |
| E08 | Oeldruck niedrig | Oelstand, Sensor |
| E09 | Phasenfehler | Wicklung |
| E10 | THD hoch | Nicht-lineare Last |

### 10.4 Dieselverbrauch-Schnellrechner

```
Faustformel Dieselverbrauch:
  Verbrauch [l/h] ≈ Leistung [kW] × 0,28  (bei 75% Last)
  Verbrauch [l/h] ≈ Leistung [kW] × 0,35  (bei 100% Last)
  Verbrauch [l/h] ≈ Leistung [kW] × 0,38  (bei 50% Last)

Beispiele:
  5 kW Generator, 75% Last: 5 × 0,28 = 1,4 l/h
  8 kW Generator, 75% Last: 8 × 0,28 = 2,2 l/h
  15 kW Generator, 75% Last: 15 × 0,28 = 4,2 l/h

Variable Speed bei Teillast:
  Verbrauch [l/h] ≈ Leistung [kW] × 0,25  (bei 50% Last)
  → ca. 34% Ersparnis gegenueber Festdrehzahl bei 50% Last
```

### 10.5 Schall-Vergleich

| Generator-Typ | Schall 1 m | Schall 7 m | Vergleichbar mit |
|---|---|---|---|
| Festdrehzahl 3.000 min⁻¹ | 70–80 dB(A) | 58–65 dB(A) | Staubsauger |
| Festdrehzahl 1.500 min⁻¹ | 62–72 dB(A) | 55–62 dB(A) | Normale Unterhaltung |
| Variable Speed (Teillast) | 52–62 dB(A) | 48–55 dB(A) | Leise Unterhaltung |
| Fischer Panda iSeries | 50–58 dB(A) | 46–54 dB(A) | Kuehlschrank |
| Brennstoffzelle EFOY | 25–35 dB(A) | <30 dB(A) | Fluuestern |
| Hydrogenerator | 0–5 dB(A) | 0 dB(A) | Stille |

---

## 11. ANHANG A-H — Fallstudien

### ANHANG A — Fallstudie: 12m Segelyacht, Generator-Nachruestung

**Ausgangslage:**
- Boot: Bavaria 40 Cruiser (2018), 12,35 m
- Aktuell: 1× 115A Lichtmaschine, 200Ah AGM-Bank, 300 Wp Solar
- Problem: Tagesverbrauch 4.500 Wh bei Tropenfahrt (Kuehlschrank, Autopilot, Elektronik, Ventilator), Batterien jeden Abend bei 50%, taegliches Motoren zum Laden

**Anforderung:**
- Unabhaengigkeit min. 3 Tage auf Ankerplatz ohne Motoren
- Klimaanlage (5.000 BTU) gelegentlich
- Budget: max. 18.000 EUR

**Loesung:**
- Fischer Panda 4000i (3,4 kW)
- Kielkuehlung (kein Impeller-Verschleiss)
- Victron MultiPlus-II 3000 (Inverter/Charger)
- Upgrade Batterien auf 400 Ah LiFePO₄

**Ergebnis:**
- Generator laeuft 1,5–2 h/Tag bei 80% Last (optimal)
- Kraftstoffverbrauch: 1,0 l/h
- Schall im Cockpit: 48 dB(A) (kaum wahrnehmbar)
- 3+ Tage Ankerplatz ohne Generator moeglich (Solar + Batterie)
- Klimaanlage: Generator + Inverter parallel, funktioniert einwandfrei

**Kosten:**
- Generator Fischer Panda 4000i inkl. Kielkuehlung: 14.200 EUR
- Installation (Werft, 3 Tage): 2.800 EUR
- Victron MultiPlus-II 3000: bereits vorhanden
- Gesamt: 17.000 EUR

### ANHANG B — Fallstudie: 16m Motoryacht, Doppelgenerator-Upgrade

**Ausgangslage:**
- Boot: Princess V52 (2015), 16,2 m
- Aktuell: 1× Onan MDKBH 7.5 (7,5 kW), 12 Jahre alt, 6.800 h
- Problem: Generator laeuft 8–12 h/Tag (Klimaanlage), zeigt Verschleiss (Oelverbrauch, Vibrationen)

**Anforderung:**
- Zuverlaessige Klimatisierung in Mittelmeer-Sommern (40°C)
- Redundanz (Charter-Betrieb)
- Leiser Betrieb (Gaeste an Bord)

**Loesung:**
- 2× Fischer Panda 10000i (je 8,5 kW)
- Automatische Lastverteilung (iControl Load Sharing)
- Seewasserkuehlung mit redundantem Impeller-System
- Autostart bei SOC <50% oder Klimaanlage-Anforderung

**Ergebnis:**
- Nur 1 Generator noetig fuer Normalbetrief (6–7 kW Last)
- Beide parallel bei Volllast (Bugstrahlruder + Klima + Wassermacher = 14 kW)
- Wartung versetzt: immer ein Generator einsatzbereit
- Laerm: 52 dB(A) Cockpit (vorher 62 dB(A) mit altem Onan)
- Treibstoff: 1,8 l/h statt vorher 2,6 l/h (Variable Speed!)

**Kosten:**
- 2× Fischer Panda 10000i inkl. Zubehoer: 38.000 EUR
- Demontage alter Generator + Installation: 8.500 EUR
- Schallkapsel-Anpassung Maschinenraum: 3.200 EUR
- Gesamt: 49.700 EUR

### ANHANG C — Fallstudie: Langfahrt-Katamaran mit Hybrid-System

**Ausgangslage:**
- Boot: Lagoon 450 (2020), 13,96 m Katamaran
- Geplant: 3-Jahres-Weltumsegelung
- Anforderung: Maximale Autarkie, minimaler Generatorbetrieb

**System-Design:**
- 1× Whisper Power M-GV 7 (6 kW Variable Speed)
- 1× Watt & Sea Cruising 600 (Hydrogenerator)
- 1.200 Wp Solar (6× 200 Wp)
- 800 Ah LiFePO₄ (48V-System)
- Victron Quattro 48/8000 (Inverter/Charger)
- Cerbo GX (Energiemanagement)

**Energiebilanz (typischer Seetag, 6 kn):**
- Solar: 4.000–6.000 Wh/Tag (tropisch)
- Hydrogenerator: 2.500–4.000 Wh/Tag (bei 6 kn, 12 h Segeln)
- Gesamt regenerativ: 6.500–10.000 Wh/Tag
- Verbrauch (ohne Klima): 5.500 Wh/Tag
- → Generator NUR bei Klima oder Flaute noetig

**Ergebnis:**
- Durchschnittlich 0,5 h Generator/Tag (nur bei Windstille + Klima)
- Kraftstoff: 25–30 l/Woche statt 70–90 l (konventionell)
- Hydrogenerator liefert zuverlaessig 200–500 W ab 5 kn
- Gesamtsystem arbeitet vollautomatisch (Cerbo GX steuert Autostart)

**Kosten:**
- Whisper Power M-GV 7: 12.500 EUR
- Watt & Sea Cruising 600: 5.800 EUR
- Solar 1.200 Wp: 3.200 EUR
- LiFePO₄ 800 Ah/48V: 14.000 EUR
- Victron Quattro + Cerbo: 4.500 EUR
- Installation: 6.000 EUR
- Gesamt: 46.000 EUR

### ANHANG D — Fallstudie: Superyacht 28m, Brennstoffzellen-Ergaenzung

**Ausgangslage:**
- Boot: Custom Aluminium-Yacht, 28 m, Baujahr 2022
- Hauptgeneratoren: 2× Cummins QD 40 (je 40 kW)
- Problem: Nachtbetrieb in Ankerbuchten — Generator stoert (65 dB)
- Anforderung: Silent Mode fuer Nacht (22:00–07:00)

**Loesung:**
- 2× EFOY Pro 12000 Duo (je 500 W, gesamt 1.000 W)
- Ueberbrueckung Nachtverbrauch (Grundlast 600–800 W: Kuehlschraenke, Elektronik, LED)
- Grosser LiFePO₄-Puffer: 600 Ah / 48V (vorhandenes System)

**Nacht-Energiebilanz:**
- Nachtverbrauch (9 h × 700 W): 6.300 Wh
- EFOY-Lieferung (9 h × 1.000 W): 9.000 Wh
- → Ausreichend! Keine Generator-Laufzeit nachts

**Ergebnis:**
- Komplette Stille nachts (<25 dB)
- Gaeste-Zufriedenheit signifikant gestiegen
- Methanol-Verbrauch: ca. 8 l/Nacht (≈ 45 EUR)
- Generatoren starten automatisch morgens fuer Klimaanlage

**Kosten:**
- 2× EFOY Pro 12000 Duo: 24.000 EUR
- Installation + Integration: 4.500 EUR
- Methanol-Brennstoff (Saison, 100 Naechte): 4.500 EUR
- Gesamt Investition: 28.500 EUR

### ANHANG E — Fallstudie: Charteryacht, Generator-Generallueberholung

**Ausgangslage:**
- Boot: Jeanneau Sun Odyssey 490 (2017), Charter-Betrieb Kroatien
- Generator: Paguro 6500 (6,5 kW), 4.200 h, 7 Saisons
- Symptome: Oelverbrauch 0,3 l/100h, leichte Vibrationen, Leistungsabfall 10%

**Diagnose (AYDI Pipeline A + B):**
- Visuell: Schwingmetalle verhaertet, Oelspuren Ventildeckel, Impeller-Rest im Waermetauscher
- Strukturiert: Kompression Zyl. 3 nur 24 bar (Soll: 28–32 bar)
- Befund: Kolbenringe Zyl. 3 verschlissen, Waermetauscher teilvertstopft

**Massnahmen:**
1. Kolbenringe alle Zylinder erneuert
2. Ventilschaftdichtungen erneuert
3. Waermetauscher gereinigt + neue Zinkanode
4. Schwingmetalle getauscht (4 Stueck)
5. Impeller + Dichtung
6. Oelwechsel + alle Filter
7. Einspritzduesen pruefen lassen (OK)

**Ergebnis:**
- Kompression wiederhergestellt (alle Zylinder 29–31 bar)
- Oelverbrauch: <0,05 l/100h
- Vibrationen: deutlich reduziert
- Leistung: wieder 100%
- Prognose: weitere 4.000–5.000 h moeglich

**Kosten:**
- Ersatzteile: 1.800 EUR
- Arbeitslohn (Werft, 2,5 Tage): 2.000 EUR
- Gesamt: 3.800 EUR (vs. Neugenerator: 9.500 EUR)

### ANHANG F — Fallstudie: Nasslauf-Schaden durch Unterdimensionierung

**Ausgangslage:**
- Boot: Beneteau Oceanis 51.1 (2019)
- Generator: Paguro 4000 (4,0 kW)
- Nutzung: Typischer Last nur 800–1.200 W (Ladegeraet + Kuehlschrank)
- Problem: Seit 2 Jahren schwarze Ablagerungen am Auspuff, unrunder Lauf

**Diagnose:**
- Generator laeuft dauerhaft bei 20–30% Last (Wet Stacking!)
- Auspuff-System mit Russablagerungen verkrustet
- Kolbenringe verkokt
- Turbolader-Rueckseite oelig (kein Turbo, aber Abgas-Ventil verkokt)

**Ursache:**
- Generator zu gross fuer tatsaechlichen Verbrauch
- Klimaanlage (geplant bei Kauf) wurde nie installiert
- Effektive Last: 800–1.200 W = 20–30% von 4.000 W

**Loesung:**
1. Sofort: Load Banking (4 h bei 80% Last mit Heizluefter als Verbraucher)
2. Kurzfristig: Mindestlast 1.600 W durch automatisches Zuschalten Warmwasserboiler
3. Langfristig: Hybrid-System (Victron MultiPlus uebernimmt Grundlast, Generator nur bei hohem Bedarf)

**Kosten der Sanierung:**
- Load Banking + Reinigung: 600 EUR
- Victron MultiPlus 2000 (Hybrid-Modus): 1.800 EUR
- Installation: 800 EUR
- Gesamt: 3.200 EUR

### ANHANG G — Fallstudie: Hydrogenerator-Installation auf Fahrtensegler

**Ausgangslage:**
- Boot: Hallberg-Rassy 40 (2016), Langfahrt Atlantik
- Aktuell: Fischer Panda AGT 4000 (3,5 kW), funktioniert einwandfrei
- Wunsch: Generatorbetrieb auf Seetagen minimieren (Laerm stoert Wache)

**Installation:**
- Watt & Sea Cruising 600
- Montage: Heckspiegel, klappbarer Arm
- Laderegler: Watt & Sea Hydro-Charger (MPPT)
- Integration in Victron-System (VE.Direct)

**Ergebnis Atlantik-Ueberquerung (21 Tage, Durchschnitt 6,5 kn):**
- Hydrogenerator Tagesleistung: 3.200–5.800 Wh (je nach Wind/Geschwindigkeit)
- Tagesverbrauch: 4.000 Wh (Autopilot, Kuehlschrank, Elektronik, LED)
- Generator-Betrieb: 0 Stunden an 14 von 21 Tagen!
- Gesamt Generator-Laufzeit: 12 h (nur bei Flaute <4 kn)
- Diesel-Ersparnis: ca. 50 Liter gegenueber "Generator-jeden-Tag"

**Kosten:**
- Watt & Sea Cruising 600 + Zubehoer: 5.800 EUR
- Montage (Halterung, Kabel, Durchfuehrung): 1.200 EUR
- Gesamt: 7.000 EUR
- Amortisation: ca. 3–4 Jahre (Diesel-Ersparnis + weniger Generator-Wartung)

### ANHANG H — Fallstudie: Elektronik-Totalausfall Fischer Panda iSeries

**Ausgangslage:**
- Boot: Amel 55 (2021), auf Langfahrt in der Karibik
- Generator: Fischer Panda 8000i, 1.800 h
- Symptom: Ploetzliche Abschaltung, Fehlercode E03 (Inverter Uebertemperatur), danach kein Neustart moeglich (E09 — Phasenfehler)

**Diagnose (Ferndiagnose via Fischer Panda Service):**
- Inverter-Board IGBT-Modul durchgebrannt
- Ursache: Korrosion an Kuehlerrippen des Inverters (Salzluft + Kondenswasser)
- Sekundaerschaden: Eine Statorwicklungsphase durch Ueberstrom beschaedigt

**Reparatur (vor Ort Martinique):**
- Inverter-Board (Luftfracht aus Deutschland): 4.200 EUR + 380 EUR Fracht
- Stator-Neuwicklung (lokaler Motorwickler): 1.800 EUR
- Arbeitslohn (Fischer Panda-Service-Partner): 1.200 EUR
- Wartezeit: 14 Tage (Teilelieferung)

**Praevention:**
- Inverter-Gehaeuse regelmaessig auf Korrosion pruefen
- Entlueftungsoeffnungen frei halten, aber gegen Spritzwasser schuetzen
- In tropischen Revieren: Entfeuchterbeutel im Elektronikfach
- Jaehrliche Sichtpruefung der Leistungselektronik

**Gesamt-Kosten:** 7.580 EUR + 14 Tage ohne Generator

---

## 12. ANHANG I-R — Pydantic v2 Modelle

### ANHANG I — Generator-Stammdaten

```python
"""
AYDI Generator Domain Models — Stammdaten und Konfiguration.

Alle Modelle verwenden Pydantic v2 mit model_config = {"from_attributes": True}.
NEVER use class Config.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class GeneratorType(str, Enum):
    """Generatortyp-Klassifikation."""
    DIESEL_FIXED_SPEED = "diesel_fixed_speed"
    DIESEL_VARIABLE_SPEED = "diesel_variable_speed"
    HYDRO = "hydro"
    FUEL_CELL_DMFC = "fuel_cell_dmfc"
    FUEL_CELL_PEM = "fuel_cell_pem"
    FUEL_CELL_SOFC = "fuel_cell_sofc"
    DC_ALTERNATOR = "dc_alternator"
    HYBRID = "hybrid"


class CoolingType(str, Enum):
    """Kuehlsystem-Typ."""
    SEAWATER_DIRECT = "seawater_direct"
    FRESHWATER_HEAT_EXCHANGER = "freshwater_heat_exchanger"
    KEEL_COOLING = "keel_cooling"
    AIR_COOLED = "air_cooled"


class FuelType(str, Enum):
    """Brennstoff-Typ."""
    DIESEL = "diesel"
    METHANOL = "methanol"
    HYDROGEN = "hydrogen"
    LNG = "lng"
    NONE = "none"  # Hydrogenerator


class PhaseType(str, Enum):
    """Phasenkonfiguration."""
    SINGLE_PHASE = "single_phase"
    THREE_PHASE = "three_phase"
    DC = "dc"


class SpeedRegulation(str, Enum):
    """Drehzahlregelung."""
    MECHANICAL_GOVERNOR = "mechanical_governor"
    ELECTRONIC_GOVERNOR = "electronic_governor"
    VARIABLE_SPEED_INVERTER = "variable_speed_inverter"
    NONE = "none"  # Hydrogenerator


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


# --- Core Models ---

class GeneratorSpecification(BaseModel):
    """Technische Spezifikation eines Generators."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller (z.B. Fischer Panda)")
    model: str = Field(..., description="Modellbezeichnung (z.B. Panda 8000i)")
    generator_type: GeneratorType
    rated_power_kva: float = Field(..., gt=0, description="Nennscheinleistung [kVA]")
    rated_power_kw: float = Field(..., gt=0, description="Nennwirkleistung [kW]")
    voltage_v: float = Field(230.0, description="Nennspannung [V]")
    frequency_hz: float = Field(50.0, description="Nennfrequenz [Hz]")
    phase_type: PhaseType = PhaseType.SINGLE_PHASE
    power_factor: float = Field(0.8, ge=0.5, le=1.0, description="Nenn-Leistungsfaktor cos φ")

    # Motor
    engine_manufacturer: Optional[str] = Field(None, description="Motorhersteller")
    engine_model: Optional[str] = Field(None, description="Motor-Modell")
    cylinders: Optional[int] = Field(None, ge=1, le=16)
    displacement_cc: Optional[int] = Field(None, gt=0, description="Hubraum [cm³]")
    rpm_nominal: Optional[int] = Field(None, description="Nenndrehzahl [min⁻¹]")
    rpm_min: Optional[int] = Field(None, description="Min. Drehzahl (Variable Speed)")
    rpm_max: Optional[int] = Field(None, description="Max. Drehzahl (Variable Speed)")

    # Physisch
    weight_kg: Optional[float] = Field(None, gt=0, description="Gewicht [kg]")
    length_mm: Optional[int] = Field(None, gt=0, description="Laenge [mm]")
    width_mm: Optional[int] = Field(None, gt=0, description="Breite [mm]")
    height_mm: Optional[int] = Field(None, gt=0, description="Hoehe [mm]")

    # Kuehlung & Abgas
    cooling_type: CoolingType = CoolingType.FRESHWATER_HEAT_EXCHANGER
    fuel_type: FuelType = FuelType.DIESEL
    fuel_consumption_full_lph: Optional[float] = Field(
        None, gt=0, description="Kraftstoffverbrauch Volllast [l/h]"
    )
    fuel_consumption_75_lph: Optional[float] = Field(
        None, gt=0, description="Kraftstoffverbrauch 75% Last [l/h]"
    )

    # Schall
    sound_level_1m_dba: Optional[float] = Field(
        None, description="Schalldruckpegel 1m [dB(A)]"
    )
    sound_level_7m_dba: Optional[float] = Field(
        None, description="Schalldruckpegel 7m [dB(A)]"
    )

    # Regelung
    speed_regulation: SpeedRegulation = SpeedRegulation.ELECTRONIC_GOVERNOR
    voltage_regulation_percent: Optional[float] = Field(
        None, ge=0, le=10, description="Spannungsregelung ±[%]"
    )
    frequency_regulation_percent: Optional[float] = Field(
        None, ge=0, le=10, description="Frequenzregelung ±[%]"
    )
    thd_percent: Optional[float] = Field(
        None, ge=0, le=20, description="THD Ausgangsspannung [%]"
    )

    @field_validator("rated_power_kw")
    @classmethod
    def validate_power_ratio(cls, v: float, info) -> float:
        """kW muss kleiner/gleich kVA sein."""
        kva = info.data.get("rated_power_kva")
        if kva is not None and v > kva:
            raise ValueError(
                f"Wirkleistung ({v} kW) darf nicht groesser als "
                f"Scheinleistung ({kva} kVA) sein"
            )
        return v


class GeneratorInstallation(BaseModel):
    """Installation eines Generators auf einer bestimmten Yacht."""

    model_config = {"from_attributes": True}

    id: Optional[str] = None
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    specification: GeneratorSpecification
    installation_date: Optional[date] = None
    serial_number: Optional[str] = None
    operating_hours: float = Field(0.0, ge=0, description="Betriebsstunden")
    last_service_date: Optional[date] = None
    last_service_hours: Optional[float] = Field(None, ge=0)
    location_description: Optional[str] = Field(
        None, description="Einbauort (z.B. Maschinenraum Stb.)"
    )
    mounting_type: Optional[str] = Field(
        None, description="Lagerung (z.B. 4-Punkt elastisch)"
    )
    keel_cooling: bool = Field(False, description="Kielkuehlung vorhanden")
    sound_enclosure: bool = Field(True, description="Schallkapsel vorhanden")
    auto_start_enabled: bool = Field(False, description="Autostart konfiguriert")
    auto_start_soc_threshold: Optional[float] = Field(
        None, ge=0, le=100, description="SOC-Schwelle fuer Autostart [%]"
    )
```

### ANHANG J — Leistungsbilanz und Dimensionierung

```python
"""
AYDI Generator Domain Models — Leistungsbilanz und Dimensionierung.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class LoadPriority(str, Enum):
    """Last-Prioritaet fuer Load Shedding."""
    CRITICAL = "critical"       # Nie abwerfen (Bilgenpumpe, Navigation)
    HIGH = "high"              # Nur im Notfall abwerfen
    MEDIUM = "medium"          # Bei Ueberlast abwerfen
    LOW = "low"                # Zuerst abwerfen (Komfort)


class LoadType(str, Enum):
    """Lastcharakteristik."""
    RESISTIVE = "resistive"             # cos φ ≈ 1.0 (Heizung, Gluehlampen)
    INDUCTIVE = "inductive"             # cos φ < 1.0 (Motoren, Kompressoren)
    CAPACITIVE = "capacitive"           # cos φ < 1.0 voreilend (PFC-Netzteile)
    NON_LINEAR = "non_linear"           # THD-verursachend (Schaltnetzteile)
    MOTOR_START = "motor_start"         # Hoher Anlaufstrom (5-8× Nennstrom)


class ElectricalConsumer(BaseModel):
    """Einzelner elektrischer Verbraucher in der Leistungsbilanz."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Verbraucher-Bezeichnung")
    nominal_power_w: float = Field(..., gt=0, description="Nennleistung [W]")
    power_factor: float = Field(1.0, ge=0.5, le=1.0, description="Leistungsfaktor cos φ")
    load_type: LoadType = LoadType.RESISTIVE
    starting_factor: float = Field(
        1.0, ge=1.0, le=10.0,
        description="Anlaufstrom-Faktor (1.0 = kein Anlaufstrom)"
    )
    duty_cycle: float = Field(
        1.0, ge=0.0, le=1.0,
        description="Gleichzeitigkeitsfaktor / Einschaltdauer (0-1)"
    )
    priority: LoadPriority = LoadPriority.MEDIUM
    quantity: int = Field(1, ge=1, description="Anzahl identischer Verbraucher")
    zone: Optional[str] = Field(None, description="Yacht-Zone (z.B. Pantry, Salon)")
    operating_hours_per_day: Optional[float] = Field(
        None, ge=0, le=24, description="Betriebsstunden/Tag"
    )

    @computed_field
    @property
    def apparent_power_va(self) -> float:
        """Scheinleistung [VA]."""
        return self.nominal_power_w / self.power_factor

    @computed_field
    @property
    def effective_power_w(self) -> float:
        """Effektive Leistung (mit Gleichzeitigkeit) [W]."""
        return self.nominal_power_w * self.duty_cycle * self.quantity

    @computed_field
    @property
    def starting_power_va(self) -> float:
        """Anlauf-Scheinleistung [VA]."""
        return self.apparent_power_va * self.starting_factor * self.quantity

    @computed_field
    @property
    def daily_energy_wh(self) -> Optional[float]:
        """Tagesenergiebedarf [Wh]."""
        if self.operating_hours_per_day is not None:
            return self.nominal_power_w * self.operating_hours_per_day * self.quantity
        return None


class PowerBalance(BaseModel):
    """Leistungsbilanz einer Yacht fuer Generator-Dimensionierung."""

    model_config = {"from_attributes": True}

    yacht_id: str
    scenario_name: str = Field(
        "standard", description="Szenario (z.B. 'anker_sommer', 'seetag', 'hafen')"
    )
    consumers: list[ElectricalConsumer] = Field(default_factory=list)
    safety_factor: float = Field(
        1.25, ge=1.0, le=2.0, description="Sicherheitsfaktor (empfohlen 1.25)"
    )

    @computed_field
    @property
    def total_effective_power_w(self) -> float:
        """Gesamte effektive Wirkleistung [W]."""
        return sum(c.effective_power_w for c in self.consumers)

    @computed_field
    @property
    def total_apparent_power_va(self) -> float:
        """Gesamte Scheinleistung [VA]."""
        return sum(c.apparent_power_va * c.duty_cycle * c.quantity for c in self.consumers)

    @computed_field
    @property
    def max_starting_power_va(self) -> float:
        """Maximale Anlaufleistung [VA] (groesster Einzelanlauf + Grundlast)."""
        base_load = self.total_apparent_power_va
        max_start = max(
            (c.starting_power_va - c.apparent_power_va * c.quantity for c in self.consumers),
            default=0.0,
        )
        return base_load + max_start

    @computed_field
    @property
    def required_generator_kva(self) -> float:
        """Empfohlene Generator-Groesse [kVA]."""
        continuous = self.total_apparent_power_va * self.safety_factor / 1000
        starting = self.max_starting_power_va / 1000  # Ohne Safety fuer Anlauf
        return max(continuous, starting * 0.8)  # 80% fuer kurzen Anlauf OK

    @computed_field
    @property
    def total_daily_energy_wh(self) -> float:
        """Gesamter Tagesenergiebedarf [Wh]."""
        return sum(
            c.daily_energy_wh for c in self.consumers if c.daily_energy_wh is not None
        )

    @computed_field
    @property
    def average_power_factor(self) -> float:
        """Gewichteter mittlerer Leistungsfaktor."""
        total_w = self.total_effective_power_w
        if total_w == 0:
            return 0.8
        weighted = sum(
            c.effective_power_w * c.power_factor for c in self.consumers
        )
        return weighted / total_w


class GeneratorSizingResult(BaseModel):
    """Ergebnis der Generator-Dimensionierung."""

    model_config = {"from_attributes": True}

    power_balance: PowerBalance
    recommended_kva: float = Field(..., description="Empfohlene Nennleistung [kVA]")
    recommended_kw: float = Field(..., description="Empfohlene Wirkleistung [kW]")
    load_percentage_nominal: float = Field(
        ..., ge=0, le=100, description="Auslastung bei Normalbetrieb [%]"
    )
    suitable_models: list[str] = Field(
        default_factory=list, description="Passende Generator-Modelle"
    )
    warnings: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED
    notes: Optional[str] = None
```

### ANHANG K — Fehlerbild und Diagnose

```python
"""
AYDI Generator Domain Models — Fehlerbild und Diagnose.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Schweregrad eines Fehlerbilds."""
    CRITICAL = "critical"      # Sofortige Abstellung noetig
    HIGH = "high"              # Baldige Reparatur noetig
    MEDIUM = "medium"          # Planung innerhalb 30 Tage
    LOW = "low"                # Naechste regulaere Wartung
    INFO = "info"              # Hinweis, kein Handlungsbedarf


class FaultCategory(str, Enum):
    """Fehlerkategorie."""
    STARTING = "starting"                    # Startproblem
    NO_VOLTAGE = "no_voltage"                # Keine Spannung
    FREQUENCY_INSTABILITY = "frequency_instability"  # Frequenzschwankung
    OVERHEATING = "overheating"              # Ueberhitzung
    OIL_LOSS = "oil_loss"                    # Oelverlust
    VIBRATION = "vibration"                  # Vibration
    SMOKE_BLACK = "smoke_black"              # Schwarzer Rauch
    SMOKE_WHITE = "smoke_white"              # Weisser Rauch
    WET_STACKING = "wet_stacking"            # Nasslaeufer
    ELECTRONICS = "electronics"              # Elektronikfehler
    FUEL_CONTAMINATION = "fuel_contamination"  # Kraftstoff-Kontamination
    EXHAUST_BACKFLOW = "exhaust_backflow"     # Abgas-Wasserrueckfluss
    NOISE_ABNORMAL = "noise_abnormal"        # Abnormale Geraeusche
    COOLANT_LOSS = "coolant_loss"            # Kuehlmittelverlust


class DiagnosticFinding(BaseModel):
    """Einzelner diagnostischer Befund."""

    model_config = {"from_attributes": True}

    fault_category: FaultCategory
    severity: FaultSeverity
    description_de: str = Field(..., description="Befundbeschreibung (Deutsch)")
    probable_cause: str = Field(..., description="Wahrscheinliche Ursache")
    probability_percent: float = Field(
        ..., ge=0, le=100, description="Wahrscheinlichkeit [%]"
    )
    recommended_action: str = Field(..., description="Empfohlene Massnahme")
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschaetzte Reparaturkosten [EUR]"
    )
    estimated_hours: Optional[float] = Field(
        None, ge=0, description="Geschaetzter Arbeitsaufwand [h]"
    )
    requires_specialist: bool = Field(
        False, description="Fachwerkstatt erforderlich"
    )
    can_continue_operation: bool = Field(
        False, description="Weiterbetrieb moeglich (eingeschraenkt)"
    )
    confidence: ConfidenceLevel


class GeneratorDiagnosis(BaseModel):
    """Gesamtdiagnose eines Generator-Problems."""

    model_config = {"from_attributes": True}

    generator_installation_id: str
    diagnosis_timestamp: datetime = Field(default_factory=datetime.utcnow)
    reported_symptoms: list[str] = Field(
        ..., min_length=1, description="Beschriebene Symptome"
    )
    operating_hours_at_diagnosis: Optional[float] = Field(None, ge=0)
    visual_indicators: list[str] = Field(
        default_factory=list, description="Visuelle Indikatoren (Pipeline B)"
    )
    measured_values: dict[str, float] = Field(
        default_factory=dict,
        description="Messwerte (z.B. {'compression_bar_cyl1': 28.5})"
    )
    findings: list[DiagnosticFinding] = Field(
        ..., min_length=1, description="Diagnostische Befunde (sortiert nach Wahrscheinlichkeit)"
    )
    overall_severity: FaultSeverity
    immediate_action_required: bool = Field(False)
    next_steps: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel


class FaultHistoryEntry(BaseModel):
    """Eintrag in der Fehlerhistorie eines Generators."""

    model_config = {"from_attributes": True}

    timestamp: datetime
    fault_category: FaultCategory
    severity: FaultSeverity
    description: str
    resolution: Optional[str] = None
    resolution_date: Optional[datetime] = None
    cost_eur: Optional[float] = None
    operating_hours: Optional[float] = None
    recurring: bool = Field(False, description="Wiederkehrender Fehler")
```

### ANHANG L — Wartung und Service

```python
"""
AYDI Generator Domain Models — Wartung und Service-Tracking.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class MaintenanceType(str, Enum):
    """Wartungstyp."""
    OIL_CHANGE = "oil_change"
    IMPELLER = "impeller"
    FUEL_FILTER = "fuel_filter"
    AIR_FILTER = "air_filter"
    BELT = "belt"
    COOLANT = "coolant"
    ZINC_ANODE = "zinc_anode"
    VALVE_ADJUSTMENT = "valve_adjustment"
    INJECTOR_SERVICE = "injector_service"
    OVERHAUL = "overhaul"
    VIBRATION_MOUNT = "vibration_mount"
    GENERAL_INSPECTION = "general_inspection"
    ELECTRONICS_CHECK = "electronics_check"


class MaintenanceInterval(BaseModel):
    """Wartungsintervall-Definition."""

    model_config = {"from_attributes": True}

    maintenance_type: MaintenanceType
    interval_hours: Optional[int] = Field(None, gt=0, description="Intervall [h]")
    interval_months: Optional[int] = Field(None, gt=0, description="Intervall [Monate]")
    description_de: str = Field(..., description="Beschreibung (Deutsch)")
    is_critical: bool = Field(False, description="Kritisch bei Versaeumnis")
    estimated_duration_hours: float = Field(
        0.5, gt=0, description="Geschaetzter Zeitaufwand [h]"
    )
    estimated_cost_parts_eur: float = Field(
        0.0, ge=0, description="Geschaetzte Teilekosten [EUR]"
    )
    diy_possible: bool = Field(True, description="Selbst durchfuehrbar")
    tools_required: list[str] = Field(default_factory=list)
    parts_required: list[str] = Field(default_factory=list)


class MaintenanceRecord(BaseModel):
    """Durchgefuehrte Wartung — Einzeleintrag."""

    model_config = {"from_attributes": True}

    id: Optional[str] = None
    generator_installation_id: str
    maintenance_type: MaintenanceType
    date_performed: date
    operating_hours: float = Field(..., ge=0)
    performed_by: Optional[str] = Field(None, description="Durchfuehrender (Name/Werft)")
    notes: Optional[str] = None
    cost_parts_eur: Optional[float] = Field(None, ge=0)
    cost_labor_eur: Optional[float] = Field(None, ge=0)
    next_due_hours: Optional[float] = Field(None, ge=0)
    next_due_date: Optional[date] = None
    findings: list[str] = Field(
        default_factory=list, description="Befunde bei der Wartung"
    )


class MaintenanceSchedule(BaseModel):
    """Wartungsplan mit Status aller Intervalle."""

    model_config = {"from_attributes": True}

    generator_installation_id: str
    current_operating_hours: float = Field(..., ge=0)
    intervals: list[MaintenanceInterval] = Field(default_factory=list)
    history: list[MaintenanceRecord] = Field(default_factory=list)

    def get_overdue_items(self) -> list[dict]:
        """Gibt ueberfaellige Wartungspunkte zurueck."""
        overdue = []
        for interval in self.intervals:
            last_record = self._get_last_record(interval.maintenance_type)
            if last_record is None:
                # Nie durchgefuehrt
                overdue.append({
                    "type": interval.maintenance_type,
                    "description": interval.description_de,
                    "overdue_hours": self.current_operating_hours,
                    "critical": interval.is_critical,
                })
            elif interval.interval_hours:
                hours_since = self.current_operating_hours - last_record.operating_hours
                if hours_since > interval.interval_hours:
                    overdue.append({
                        "type": interval.maintenance_type,
                        "description": interval.description_de,
                        "overdue_hours": hours_since - interval.interval_hours,
                        "critical": interval.is_critical,
                    })
        return overdue

    def _get_last_record(self, mtype: MaintenanceType) -> Optional[MaintenanceRecord]:
        """Letzter Wartungseintrag eines Typs."""
        records = [r for r in self.history if r.maintenance_type == mtype]
        if not records:
            return None
        return max(records, key=lambda r: r.operating_hours)
```

### ANHANG M — Betriebsdaten und Monitoring

```python
"""
AYDI Generator Domain Models — Betriebsdaten, Monitoring, Telemetrie.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GeneratorState(str, Enum):
    """Betriebszustand des Generators."""
    OFF = "off"
    PREHEATING = "preheating"
    STARTING = "starting"
    WARMING_UP = "warming_up"
    RUNNING = "running"
    COOLING_DOWN = "cooling_down"
    FAULT = "fault"
    MAINTENANCE_MODE = "maintenance_mode"


class AlarmLevel(str, Enum):
    """Alarm-Stufe."""
    WARNING = "warning"        # Warnung, Weiterbetrieb moeglich
    ALARM = "alarm"            # Alarm, baldige Abstellung empfohlen
    SHUTDOWN = "shutdown"      # Automatische Abschaltung erfolgt
    CRITICAL = "critical"      # Notabschaltung, Schaden moeglich


class GeneratorTelemetry(BaseModel):
    """Einzelner Telemetrie-Datenpunkt."""

    model_config = {"from_attributes": True}

    timestamp: datetime = Field(default_factory=datetime.utcnow)
    generator_installation_id: str
    state: GeneratorState

    # Motorwerte
    rpm: Optional[int] = Field(None, ge=0, le=5000, description="Drehzahl [min⁻¹]")
    coolant_temp_c: Optional[float] = Field(None, description="Kuehlwassertemperatur [°C]")
    oil_pressure_bar: Optional[float] = Field(None, ge=0, description="Oeldruck [bar]")
    exhaust_temp_c: Optional[float] = Field(None, description="Abgastemperatur [°C]")
    fuel_rate_lph: Optional[float] = Field(None, ge=0, description="Kraftstofffluss [l/h]")

    # Elektrische Werte
    voltage_l1_v: Optional[float] = Field(None, ge=0, description="Spannung L1 [V]")
    voltage_l2_v: Optional[float] = Field(None, ge=0, description="Spannung L2 [V]")
    voltage_l3_v: Optional[float] = Field(None, ge=0, description="Spannung L3 [V]")
    current_l1_a: Optional[float] = Field(None, ge=0, description="Strom L1 [A]")
    current_l2_a: Optional[float] = Field(None, ge=0, description="Strom L2 [A]")
    current_l3_a: Optional[float] = Field(None, ge=0, description="Strom L3 [A]")
    frequency_hz: Optional[float] = Field(None, ge=0, le=70, description="Frequenz [Hz]")
    power_kw: Optional[float] = Field(None, ge=0, description="Aktuelle Wirkleistung [kW]")
    power_kva: Optional[float] = Field(None, ge=0, description="Aktuelle Scheinleistung [kVA]")
    power_factor: Optional[float] = Field(None, ge=0, le=1.0, description="Aktueller cos φ")
    thd_percent: Optional[float] = Field(None, ge=0, description="THD [%]")

    # Betriebszaehler
    operating_hours_total: Optional[float] = Field(None, ge=0)
    energy_produced_kwh: Optional[float] = Field(None, ge=0, description="Erzeugte Energie [kWh]")
    starts_total: Optional[int] = Field(None, ge=0, description="Anzahl Starts gesamt")

    # Zustand
    load_percent: Optional[float] = Field(None, ge=0, le=150, description="Auslastung [%]")
    battery_voltage_v: Optional[float] = Field(None, description="Starterbatterie [V]")


class GeneratorAlarm(BaseModel):
    """Generator-Alarm/Warnung."""

    model_config = {"from_attributes": True}

    timestamp: datetime = Field(default_factory=datetime.utcnow)
    generator_installation_id: str
    alarm_code: str = Field(..., description="Fehlercode (z.B. E03)")
    alarm_level: AlarmLevel
    description_de: str = Field(..., description="Alarmbeschreibung (Deutsch)")
    value: Optional[float] = Field(None, description="Ausloesewert")
    threshold: Optional[float] = Field(None, description="Grenzwert")
    acknowledged: bool = False
    resolved: bool = False
    resolution_timestamp: Optional[datetime] = None
    auto_shutdown_triggered: bool = False


class OperatingStatistics(BaseModel):
    """Betriebsstatistik ueber einen Zeitraum."""

    model_config = {"from_attributes": True}

    generator_installation_id: str
    period_start: datetime
    period_end: datetime
    total_running_hours: float = Field(0.0, ge=0)
    total_energy_kwh: float = Field(0.0, ge=0)
    total_fuel_liters: float = Field(0.0, ge=0)
    total_starts: int = Field(0, ge=0)
    average_load_percent: Optional[float] = Field(None, ge=0, le=100)
    peak_load_percent: Optional[float] = Field(None, ge=0, le=150)
    average_fuel_rate_lph: Optional[float] = Field(None, ge=0)
    alarms_count: int = Field(0, ge=0)
    shutdowns_count: int = Field(0, ge=0)
    availability_percent: Optional[float] = Field(None, ge=0, le=100)

    @computed_field
    @property
    def specific_fuel_consumption_lkwh(self) -> Optional[float]:
        """Spezifischer Kraftstoffverbrauch [l/kWh]."""
        if self.total_energy_kwh > 0:
            return self.total_fuel_liters / self.total_energy_kwh
        return None

    @computed_field
    @property
    def average_run_duration_h(self) -> Optional[float]:
        """Durchschnittliche Laufzeit pro Start [h]."""
        if self.total_starts > 0:
            return self.total_running_hours / self.total_starts
        return None
```

### ANHANG N — Hydrogenerator-Modelle

```python
"""
AYDI Generator Domain Models — Hydrogenerator-spezifische Modelle.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class HydroMountType(str, Enum):
    """Montagetyp Hydrogenerator."""
    TRANSOM_FIXED = "transom_fixed"
    TRANSOM_RETRACTABLE = "transom_retractable"
    RUDDER_MOUNTED = "rudder_mounted"
    POD_UNDERWATER = "pod_underwater"
    TOWED = "towed"
    SAILDRIVE_REGEN = "saildrive_regen"


class HydroPropellerType(str, Enum):
    """Propellertyp."""
    FIXED_BLADE = "fixed_blade"
    FOLDING = "folding"
    FEATHERING = "feathering"
    TOWED_SPINNER = "towed_spinner"


class HydroPerformancePoint(BaseModel):
    """Einzelner Leistungspunkt der Hydrogenerator-Kennlinie."""

    model_config = {"from_attributes": True}

    boat_speed_kn: float = Field(..., ge=0, le=30, description="Bootsgeschwindigkeit [kn]")
    power_output_w: float = Field(..., ge=0, description="Erzeugte Leistung [W]")
    current_output_a: Optional[float] = Field(None, ge=0, description="Strom [A]")
    drag_force_n: Optional[float] = Field(None, ge=0, description="Widerstandskraft [N]")
    efficiency_percent: Optional[float] = Field(None, ge=0, le=100)


class HydrogeneratorSpecification(BaseModel):
    """Technische Spezifikation eines Hydrogenerators."""

    model_config = {"from_attributes": True}

    manufacturer: str
    model: str
    mount_type: HydroMountType
    propeller_type: HydroPropellerType
    propeller_diameter_mm: int = Field(..., gt=0, description="Propellerdurchmesser [mm]")
    max_power_w: float = Field(..., gt=0, description="Maximale Leistung [W]")
    rated_speed_kn: float = Field(..., gt=0, description="Nenngeschwindigkeit [kn]")
    start_speed_kn: float = Field(..., gt=0, description="Startgeschwindigkeit [kn]")
    output_voltage_v: float = Field(..., gt=0, description="Ausgangsspannung [V]")
    max_current_a: float = Field(..., gt=0, description="Maximaler Strom [A]")
    weight_underwater_kg: float = Field(..., gt=0, description="Unterwasser-Gewicht [kg]")
    weight_total_kg: float = Field(..., gt=0, description="Gesamtgewicht [kg]")
    mppt_integrated: bool = Field(False, description="MPPT-Laderegler integriert")
    retractable: bool = Field(False, description="Einklappbar/hochziehbar")
    performance_curve: list[HydroPerformancePoint] = Field(default_factory=list)

    @computed_field
    @property
    def speed_to_power_ratio(self) -> float:
        """Leistung pro Knoten bei Nenngeschwindigkeit [W/kn]."""
        return self.max_power_w / self.rated_speed_kn

    def estimate_power_at_speed(self, speed_kn: float) -> float:
        """Schaetzt Leistung bei gegebener Geschwindigkeit (kubisches Modell)."""
        if speed_kn < self.start_speed_kn:
            return 0.0
        ratio = speed_kn / self.rated_speed_kn
        estimated = self.max_power_w * min(ratio ** 3, 1.0)
        return min(estimated, self.max_power_w)


class HydrogeneratorEnergyEstimate(BaseModel):
    """Energieertrags-Schaetzung fuer eine Passage."""

    model_config = {"from_attributes": True}

    hydro_spec: HydrogeneratorSpecification
    passage_distance_nm: float = Field(..., gt=0)
    average_speed_kn: float = Field(..., gt=0)
    sailing_hours: float = Field(..., gt=0)
    estimated_energy_wh: float = Field(..., ge=0)
    estimated_speed_loss_kn: float = Field(0.0, ge=0)
    equivalent_diesel_liters: float = Field(0.0, ge=0)
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
```

### ANHANG O — Brennstoffzellen-Modelle

```python
"""
AYDI Generator Domain Models — Brennstoffzellen-spezifische Modelle.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class FuelCellType(str, Enum):
    """Brennstoffzellen-Technologie."""
    DMFC = "dmfc"         # Direkt-Methanol
    PEM = "pem"           # Proton Exchange Membrane (H₂)
    SOFC = "sofc"         # Festoxid
    RMFC = "rmfc"         # Reformed Methanol


class FuelCellFuel(str, Enum):
    """Brennstoff fuer Brennstoffzelle."""
    METHANOL = "methanol"
    HYDROGEN_COMPRESSED = "hydrogen_compressed"
    HYDROGEN_METAL_HYDRIDE = "hydrogen_metal_hydride"
    LNG = "lng"
    DIESEL_REFORMED = "diesel_reformed"


class FuelCellSpecification(BaseModel):
    """Technische Spezifikation einer Brennstoffzelle."""

    model_config = {"from_attributes": True}

    manufacturer: str
    model: str
    cell_type: FuelCellType
    fuel: FuelCellFuel
    continuous_power_w: float = Field(..., gt=0, description="Dauerleistung [W]")
    peak_power_w: Optional[float] = Field(None, gt=0, description="Spitzenleistung [W]")
    output_voltage_v: float = Field(..., gt=0, description="Ausgangsspannung [V]")
    output_voltage_range: Optional[str] = Field(None, description="Spannungsbereich (z.B. '20-29V')")
    efficiency_percent: float = Field(..., ge=0, le=100, description="Elektrischer Wirkungsgrad [%]")
    fuel_consumption_per_kwh: float = Field(
        ..., gt=0, description="Brennstoffverbrauch [l/kWh oder g/kWh]"
    )
    fuel_consumption_unit: str = Field("l/kWh", description="Einheit Brennstoffverbrauch")
    operating_temp_min_c: float = Field(-20, description="Min. Betriebstemperatur [°C]")
    operating_temp_max_c: float = Field(50, description="Max. Betriebstemperatur [°C]")
    startup_time_min: float = Field(..., ge=0, description="Startzeit [min]")
    noise_level_dba: Optional[float] = Field(None, description="Schallpegel [dB(A)]")
    weight_kg: float = Field(..., gt=0)
    dimensions_mm: Optional[str] = Field(None, description="L×B×H [mm]")
    stack_lifetime_hours: float = Field(..., gt=0, description="Stack-Lebensdauer [h]")
    maintenance_interval_hours: Optional[float] = Field(None, gt=0)
    emissions_co2_g_per_kwh: Optional[float] = Field(None, ge=0)
    water_output: bool = Field(True, description="Produziert Wasser als Nebenprodukt")
    heat_output_w: Optional[float] = Field(None, ge=0, description="Abwaerme [W]")
    auto_start_capable: bool = Field(True)
    frost_protection: bool = Field(False)

    @computed_field
    @property
    def energy_per_day_wh(self) -> float:
        """Maximale Tagesenergie bei Dauerbetrieb [Wh]."""
        return self.continuous_power_w * 24

    @computed_field
    @property
    def cost_per_kwh_eur(self) -> Optional[float]:
        """Geschaetzte Brennstoffkosten/kWh [EUR] (Methanol ~6 EUR/l)."""
        if self.fuel == FuelCellFuel.METHANOL:
            methanol_price_per_liter = 6.0  # EUR, Tankpatronen-Preis
            return self.fuel_consumption_per_kwh * methanol_price_per_liter
        return None


class FuelCellInstallation(BaseModel):
    """Brennstoffzellen-Installation auf einer Yacht."""

    model_config = {"from_attributes": True}

    id: Optional[str] = None
    yacht_id: str
    specification: FuelCellSpecification
    quantity: int = Field(1, ge=1, description="Anzahl Zellen (z.B. 2× Duo)")
    installation_date: Optional[date] = None
    stack_hours: float = Field(0.0, ge=0, description="Stack-Betriebsstunden")
    fuel_tank_capacity_l: Optional[float] = Field(None, gt=0, description="Brennstoff-Vorrat [l]")
    auto_start_soc_threshold: Optional[float] = Field(None, ge=0, le=100)
    auto_stop_soc_threshold: Optional[float] = Field(None, ge=0, le=100)
    ventilation_adequate: bool = Field(True)
    location: Optional[str] = None

    @computed_field
    @property
    def total_continuous_power_w(self) -> float:
        """Gesamte Dauerleistung [W]."""
        return self.specification.continuous_power_w * self.quantity

    @computed_field
    @property
    def remaining_stack_life_hours(self) -> float:
        """Verbleibende Stack-Lebensdauer [h]."""
        return max(0, self.specification.stack_lifetime_hours - self.stack_hours)

    @computed_field
    @property
    def remaining_stack_life_percent(self) -> float:
        """Verbleibende Stack-Lebensdauer [%]."""
        return (self.remaining_stack_life_hours / self.specification.stack_lifetime_hours) * 100

    @computed_field
    @property
    def autonomy_hours(self) -> Optional[float]:
        """Autonomie mit vollem Tank [h]."""
        if self.fuel_tank_capacity_l and self.specification.fuel_consumption_per_kwh > 0:
            total_power_kw = self.total_continuous_power_w / 1000
            consumption_l_per_h = self.specification.fuel_consumption_per_kwh * total_power_kw
            if consumption_l_per_h > 0:
                return self.fuel_tank_capacity_l / consumption_l_per_h
        return None
```

### ANHANG P — Hybrid-System-Modelle

```python
"""
AYDI Generator Domain Models — Hybrid-System und Energiemanagement.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class HybridArchitecture(str, Enum):
    """Hybrid-Architektur."""
    SERIAL = "serial"             # Generator → Batterie → Inverter → Last
    PARALLEL = "parallel"         # Generator + Inverter → AC-Bus
    DC_BUS = "dc_bus"             # Alle Quellen → DC-Bus → Inverter
    AC_COUPLING = "ac_coupling"   # Quellen auf AC-Sammelschiene


class EnergySource(str, Enum):
    """Energiequelle im Hybrid-System."""
    GENERATOR = "generator"
    SOLAR = "solar"
    WIND = "wind"
    HYDRO = "hydro"
    FUEL_CELL = "fuel_cell"
    SHORE_POWER = "shore_power"
    MAIN_ENGINE_ALTERNATOR = "main_engine_alternator"


class OperatingMode(str, Enum):
    """Betriebsmodus des Hybrid-Systems."""
    BATTERY_ONLY = "battery_only"         # Nur Batterie (leise)
    GENERATOR_ONLY = "generator_only"     # Nur Generator (Ladung + Last)
    GENERATOR_CHARGING = "generator_charging"  # Generator laedt Batterie
    HYBRID_PARALLEL = "hybrid_parallel"   # Generator + Batterie parallel
    SOLAR_PRIORITY = "solar_priority"     # Solar bevorzugt, Generator Backup
    SHORE_POWER = "shore_power"           # Landstrom
    EMERGENCY = "emergency"               # Notbetrieb (minimale Last)


class EnergySourceConfig(BaseModel):
    """Konfiguration einer Energiequelle im Hybrid-System."""

    model_config = {"from_attributes": True}

    source_type: EnergySource
    max_power_w: float = Field(..., ge=0, description="Maximale Leistung [W]")
    priority: int = Field(..., ge=1, le=10, description="Prioritaet (1=hoechste)")
    available: bool = Field(True)
    auto_start: bool = Field(False, description="Automatischer Start moeglich")
    start_soc_threshold: Optional[float] = Field(None, ge=0, le=100)
    stop_soc_threshold: Optional[float] = Field(None, ge=0, le=100)
    min_run_time_min: Optional[int] = Field(
        None, ge=0, description="Mindestlaufzeit [min] (Generator)"
    )
    optimal_load_percent_min: Optional[float] = Field(
        None, ge=0, le=100, description="Optimale Mindestlast [%]"
    )
    optimal_load_percent_max: Optional[float] = Field(
        None, ge=0, le=100, description="Optimale Hoechstlast [%]"
    )


class HybridSystemConfig(BaseModel):
    """Gesamtkonfiguration des Hybrid-Energiesystems."""

    model_config = {"from_attributes": True}

    yacht_id: str
    architecture: HybridArchitecture
    dc_bus_voltage_v: Optional[float] = Field(None, description="DC-Bus-Spannung [V]")
    battery_capacity_ah: float = Field(..., gt=0, description="Batteriekapazitaet [Ah]")
    battery_voltage_v: float = Field(..., gt=0, description="Batterie-Nennspannung [V]")
    inverter_power_w: float = Field(..., gt=0, description="Inverter-Nennleistung [W]")
    sources: list[EnergySourceConfig] = Field(
        ..., min_length=1, description="Energiequellen"
    )
    operating_mode: OperatingMode = OperatingMode.SOLAR_PRIORITY
    soc_min_percent: float = Field(20.0, ge=0, le=100, description="Min. SOC [%]")
    soc_max_percent: float = Field(100.0, ge=0, le=100, description="Max. SOC [%]")
    generator_auto_start_soc: float = Field(
        40.0, ge=0, le=100, description="Generator-Start bei SOC [%]"
    )
    generator_auto_stop_soc: float = Field(
        85.0, ge=0, le=100, description="Generator-Stop bei SOC [%]"
    )

    @computed_field
    @property
    def battery_capacity_wh(self) -> float:
        """Batteriekapazitaet [Wh]."""
        return self.battery_capacity_ah * self.battery_voltage_v

    @computed_field
    @property
    def usable_capacity_wh(self) -> float:
        """Nutzbare Kapazitaet [Wh] (zwischen SOC-Grenzen)."""
        usable_fraction = (self.soc_max_percent - self.soc_min_percent) / 100
        return self.battery_capacity_wh * usable_fraction

    @computed_field
    @property
    def total_source_power_w(self) -> float:
        """Gesamte verfuegbare Quellleistung [W]."""
        return sum(s.max_power_w for s in self.sources if s.available)


class EnergyBalanceSimulation(BaseModel):
    """Simulation der Energiebilanz ueber einen Zeitraum."""

    model_config = {"from_attributes": True}

    hybrid_config: HybridSystemConfig
    simulation_hours: float = Field(24.0, gt=0, description="Simulationszeitraum [h]")
    average_load_w: float = Field(..., ge=0, description="Mittlere Last [W]")
    peak_load_w: float = Field(..., ge=0, description="Spitzenlast [W]")
    solar_yield_wh: float = Field(0.0, ge=0, description="Solar-Ertrag [Wh]")
    wind_yield_wh: float = Field(0.0, ge=0, description="Wind-Ertrag [Wh]")
    hydro_yield_wh: float = Field(0.0, ge=0, description="Hydro-Ertrag [Wh]")

    @computed_field
    @property
    def total_demand_wh(self) -> float:
        """Gesamtbedarf [Wh]."""
        return self.average_load_w * self.simulation_hours

    @computed_field
    @property
    def total_renewable_wh(self) -> float:
        """Gesamter regenerativer Ertrag [Wh]."""
        return self.solar_yield_wh + self.wind_yield_wh + self.hydro_yield_wh

    @computed_field
    @property
    def generator_deficit_wh(self) -> float:
        """Vom Generator zu deckender Fehlbetrag [Wh]."""
        deficit = self.total_demand_wh - self.total_renewable_wh
        return max(0, deficit)

    @computed_field
    @property
    def generator_runtime_hours(self) -> float:
        """Geschaetzte Generator-Laufzeit [h]."""
        gen_sources = [
            s for s in self.hybrid_config.sources
            if s.source_type == EnergySource.GENERATOR and s.available
        ]
        if not gen_sources:
            return 0.0
        gen_power = gen_sources[0].max_power_w * 0.75  # 75% Last
        if gen_power > 0:
            return self.generator_deficit_wh / gen_power
        return 0.0

    @computed_field
    @property
    def renewable_fraction_percent(self) -> float:
        """Anteil erneuerbarer Energien [%]."""
        if self.total_demand_wh > 0:
            return min(100, (self.total_renewable_wh / self.total_demand_wh) * 100)
        return 0.0
```

### ANHANG Q — AYDI-Analyse-Ergebnisse

```python
"""
AYDI Generator Domain Models — Analyse-Ergebnisse und Scoring.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GeneratorConditionScore(str, Enum):
    """Gesamtzustandsbewertung."""
    EXCELLENT = "excellent"      # 90–100 Punkte
    GOOD = "good"                # 75–89 Punkte
    FAIR = "fair"                # 60–74 Punkte
    POOR = "poor"                # 40–59 Punkte
    CRITICAL = "critical"        # <40 Punkte


class GeneratorAnalysisResult(BaseModel):
    """Gesamtergebnis der Generator-Analyse (AYDI-Modul)."""

    model_config = {"from_attributes": True}

    generator_installation_id: str
    analysis_timestamp: datetime = Field(default_factory=datetime.utcnow)
    analysis_version: str = Field("1.0.0")

    # Scoring (0–100)
    overall_score: float = Field(..., ge=0, le=100)
    condition: GeneratorConditionScore
    mechanical_score: float = Field(..., ge=0, le=100)
    electrical_score: float = Field(..., ge=0, le=100)
    cooling_score: float = Field(..., ge=0, le=100)
    exhaust_score: float = Field(..., ge=0, le=100)
    mounting_score: float = Field(..., ge=0, le=100)
    maintenance_compliance_score: float = Field(..., ge=0, le=100)

    # Befunde
    findings: list[DiagnosticFinding] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)

    # Verbleibende Lebensdauer
    estimated_remaining_hours: Optional[float] = Field(None, ge=0)
    estimated_remaining_years: Optional[float] = Field(None, ge=0)
    next_critical_maintenance: Optional[str] = None
    next_critical_maintenance_hours: Optional[float] = None

    # Meta
    confidence: ConfidenceLevel
    data_sources: list[str] = Field(
        default_factory=list,
        description="Genutzte Datenquellen (z.B. 'visual', 'telemetry', 'service_report')"
    )
    limitations: list[str] = Field(
        default_factory=list, description="Einschraenkungen der Analyse"
    )


class GeneratorComparisonEntry(BaseModel):
    """Einzelner Generator im Vergleich."""

    model_config = {"from_attributes": True}

    specification: GeneratorSpecification
    score_noise: float = Field(..., ge=0, le=100, description="Schallbewertung")
    score_efficiency: float = Field(..., ge=0, le=100, description="Effizienzbewertung")
    score_reliability: float = Field(..., ge=0, le=100, description="Zuverlaessigkeit")
    score_cost: float = Field(..., ge=0, le=100, description="Preis-Leistung")
    score_maintenance: float = Field(..., ge=0, le=100, description="Wartungsfreundlichkeit")
    score_weight_volume: float = Field(..., ge=0, le=100, description="Gewicht/Volumen")
    overall_score: float = Field(..., ge=0, le=100)
    suitable_for_yacht: bool = True
    notes: list[str] = Field(default_factory=list)


class GeneratorRecommendation(BaseModel):
    """AYDI Generator-Empfehlung basierend auf Anforderungsprofil."""

    model_config = {"from_attributes": True}

    yacht_id: str
    power_balance: PowerBalance
    recommended_type: GeneratorType
    recommended_models: list[GeneratorComparisonEntry] = Field(
        ..., min_length=1, max_length=5
    )
    hybrid_recommendation: Optional[str] = Field(
        None, description="Hybrid-System-Empfehlung"
    )
    supplementary_sources: list[str] = Field(
        default_factory=list,
        description="Empfohlene Ergaenzungsquellen (z.B. 'solar_600wp', 'hydro_watt_sea_600')"
    )
    estimated_annual_fuel_liters: float = Field(..., ge=0)
    estimated_annual_cost_eur: float = Field(..., ge=0)
    confidence: ConfidenceLevel
    reasoning: str = Field(..., description="Begruendung der Empfehlung (Deutsch)")
```

### ANHANG R — API-Response-Modelle

```python
"""
AYDI Generator Domain Models — API Response Modelle fuer Frontend.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class GeneratorStatusResponse(BaseModel):
    """API-Response: Aktueller Generator-Status fuer Dashboard."""

    model_config = {"from_attributes": True}

    generator_id: str
    manufacturer: str
    model: str
    state: GeneratorState
    operating_hours: float
    voltage_v: Optional[float] = None
    frequency_hz: Optional[float] = None
    power_kw: Optional[float] = None
    load_percent: Optional[float] = None
    coolant_temp_c: Optional[float] = None
    fuel_rate_lph: Optional[float] = None
    active_alarms: list[GeneratorAlarm] = Field(default_factory=list)
    maintenance_overdue: list[dict] = Field(default_factory=list)
    condition: GeneratorConditionScore
    overall_score: float
    last_updated: datetime


class GeneratorDimensioningRequest(BaseModel):
    """API-Request: Generator-Dimensionierung anfordern."""

    model_config = {"from_attributes": True}

    yacht_id: str
    yacht_length_m: float = Field(..., gt=0, le=100)
    yacht_type: str = Field(..., description="Typ (segelyacht, motoryacht, katamaran)")
    consumers: list[ElectricalConsumer]
    has_air_conditioning: bool = False
    has_watermaker: bool = False
    has_electric_cooking: bool = False
    cruising_area: Optional[str] = Field(None, description="Revier (tropen, mittelmeer, nordeuropa)")
    budget_eur: Optional[float] = Field(None, ge=0)
    noise_priority: bool = Field(False, description="Laermreduzierung hat hohe Prioritaet")
    eco_priority: bool = Field(False, description="Niedriger Verbrauch hat hohe Prioritaet")


class GeneratorDimensioningResponse(BaseModel):
    """API-Response: Ergebnis der Generator-Dimensionierung."""

    model_config = {"from_attributes": True}

    request: GeneratorDimensioningRequest
    power_balance: PowerBalance
    recommendation: GeneratorRecommendation
    alternative_solutions: list[str] = Field(default_factory=list)
    cost_comparison_10_years: dict[str, float] = Field(
        default_factory=dict,
        description="10-Jahres-Kostenvergleich verschiedener Loesungen"
    )
    confidence: ConfidenceLevel
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class GeneratorServiceReportAnalysis(BaseModel):
    """API-Response: Analyse eines Service-Reports (Pipeline C)."""

    model_config = {"from_attributes": True}

    generator_id: str
    report_date: Optional[datetime] = None
    report_source: str = Field(..., description="Quelle (z.B. 'werft_report', 'surveyor')")
    extracted_operating_hours: Optional[float] = None
    extracted_findings: list[DiagnosticFinding] = Field(default_factory=list)
    extracted_maintenance: list[MaintenanceRecord] = Field(default_factory=list)
    risk_assessment: Optional[str] = None
    recommended_actions: list[str] = Field(default_factory=list)
    urgency_level: FaultSeverity
    confidence: ConfidenceLevel
    raw_text_summary: Optional[str] = Field(
        None, description="Zusammenfassung des Reports (max. 500 Zeichen)"
    )


class VisualGeneratorAssessment(BaseModel):
    """API-Response: Visuelle Bewertung eines Generators (Pipeline B)."""

    model_config = {"from_attributes": True}

    generator_id: Optional[str] = None
    image_ids: list[str] = Field(..., min_length=1)
    assessment_timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Visuelle Befunde
    corrosion_detected: bool = False
    corrosion_severity: Optional[FaultSeverity] = None
    corrosion_locations: list[str] = Field(default_factory=list)

    oil_leaks_detected: bool = False
    oil_leak_severity: Optional[FaultSeverity] = None
    oil_leak_locations: list[str] = Field(default_factory=list)

    belt_condition: Optional[str] = Field(None, description="gut/verschlissen/gerissen")
    hose_condition: Optional[str] = Field(None, description="gut/alternd/rissig/aufgequollen")
    mounting_condition: Optional[str] = Field(None, description="gut/lose/gerissen")
    enclosure_condition: Optional[str] = Field(None, description="gut/beschaedigt/fehlend")

    exhaust_discoloration: bool = False
    exhaust_deposit_type: Optional[str] = Field(
        None, description="keine/schwarz_russ/weiss_kalk/oelig"
    )

    overall_visual_score: float = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel
    findings: list[DiagnosticFinding] = Field(default_factory=list)
    photo_quality_sufficient: bool = True
    additional_photos_needed: list[str] = Field(
        default_factory=list,
        description="Fehlende Perspektiven (z.B. 'impeller_gehaeuse', 'abgasaustritt')"
    )
```

---

## 13. Ergaenzende Technische Referenz

### 13.1 Elektromagnetische Vertraeglichkeit (EMV)

Marine-Generatoren muessen die EMV-Anforderungen der RCD 2013/53/EU erfuellen. Besonders Variable-Speed-Generatoren mit Inverter-Elektronik sind potenzielle Stoerquellen.

**EMV-Massnahmen:**

| Massnahme | Beschreibung | Wirksamkeit |
|---|---|---|
| Geschirmte Kabel | AC-Ausgangskabel geschirmt, Schirm einseitig geerdet | Hoch |
| Ferritkerne | Klapperferrite auf Steuer- und Sensorkabeln | Mittel |
| Netzfilter | EMV-Filter am AC-Ausgang (Gleichtakt + Gegentakt) | Hoch |
| Massekonzept | Sternfoermige Masseanbindung, kein Ground-Loop | Hoch |
| Abstand | Min. 1 m zu Funkgeraeten, GPS, AIS | Mittel |
| Metallgehaeuse | Schallkapsel als Faraday'scher Kaefig | Mittel–Hoch |

**Typische EMV-Probleme:**
- UKW-Funk-Stoerungen bei Generator-Betrieb (besonders Variable Speed)
- GPS-Empfangseinbussen durch HF-Emissionen des Inverters
- AIS-Performanceverlust
- SSB-Empfangsstoerungen (Kurzwelle besonders empfindlich)

**Diagnose:**
```
EMV-Problem erkennen:
1. Stoerung nur bei laufendem Generator? → Generator ist Quelle
2. Stoerung frequenzabhaengig? → Inverter-Schaltfrequenz (typisch 8–20 kHz)
3. Stoerung lastabhaengig? → Stromoberwellen
4. Stoerung verschwindet bei abgezogenem AC-Kabel? → Leitungsgebundene Stoerung
5. Stoerung bleibt bei abgezogenem AC-Kabel? → Abgestrahlte Stoerung
```

### 13.2 Kraftstoffsystem-Integration

**Tankanbindung fuer Generator:**

| Aspekt | Anforderung | Norm |
|---|---|---|
| Kraftstoff-Entnahme | Min. 50 mm ueber Tankboden (Sediment) | ISO 10088 |
| Kraftstoff-Ruecklauf | Separater Anschluss oder Loop | Hersteller |
| Absperrventil | Handbetaetigt, gut zugaenglich | ISO 10088 |
| Kraftstoff-Vorfilter | 30 µm Wasserabscheider (Racor-Typ) | Empfehlung |
| Feinfilter | 2–10 µm am Motor | Hersteller |
| Leitungsmaterial | Kraftstoff-bestaendiger Schlauch (ISO 7840 A1) | ISO 7840 |
| Schlauchschellen | Doppelschellen an allen Verbindungen | ABYC H-33 |
| Belüftung | Tank muss belueftet sein (Unterdruck bei Entnahme) | ISO 10088 |

**Dual-Tank-Umschaltung:**
Bei Yachten mit separatem Generator-Tank oder Umschaltmoeglichkeit zwischen Tanks:
- 3-Wege-Ventil mit eindeutiger Stellungsanzeige
- Ruecklauf IMMER in den Tank aus dem entnommen wird
- Keine Kreuzverbindung der Ruecklaufleitungen

### 13.3 Starterbatterie-Anforderungen

**Generator-Starterbatterie (separat von Bordbatterie-Bank):**

| Generator-Leistung | Min. Batteriekapazitaet | Kaltstartstrom (CCA) | Typ |
|---|---|---|---|
| 2–5 kW | 45–55 Ah | 350–450 A | AGM |
| 5–10 kW | 55–75 Ah | 450–600 A | AGM |
| 10–20 kW | 75–100 Ah | 600–800 A | AGM |
| 20–50 kW | 100–150 Ah | 800–1.200 A | AGM/GEL |
| 50–100 kW | 150–200 Ah | 1.200–1.800 A | AGM |

**Lade-Erhaltung:** Starterbatterie muss staendig auf Ladung gehalten werden (Laderegler oder DC-DC-Wandler von Bordbatterie). Entladung durch Steuerelektronik: ca. 0,5–2 A Standby-Verbrauch.

### 13.4 Abnahme und Inbetriebnahme

**Checkliste Erstinbetriebnahme Generator:**

```
□ Mechanisch
  □ Motoroel auf korrektem Stand (zwischen MIN und MAX)
  □ Kuehlwasser aufgefuellt (Suesswasser-Kreislauf)
  □ Seeventil offen, Sieb sauber
  □ Abgasleitung dicht, Waterlock korrekt montiert
  □ Schwanenhalsbogen ueber Wasserlinie
  □ Antisiphon-Ventil vorhanden und funktionsfaehig
  □ Kraftstoff vorhanden, System entlueftet
  □ Schwingmetalle korrekt montiert (Schrauben fest)
  □ Keilriemen Spannung korrekt (10–15 mm Durchbiegung)
  □ Auspuffklappe/Rueckschlagventil gängig

□ Elektrisch
  □ Starterbatterie voll geladen (>12,6V / >25,2V)
  □ Batteriekabel korrekt angezogen (Drehmoment!)
  □ AC-Sicherungsautomat AUS (vor Erststart)
  □ Erdungsleiter Generator → Bonding-System
  □ Isolationswiderstand >1 MΩ (Megger-Test)
  □ CAN-Bus/NMEA2000 verbunden (falls vorhanden)
  □ Fernstart-Panel getestet

□ Erststart-Prozedur
  □ Motor starten OHNE Last (Leerlauf)
  □ 5 Minuten warmlaufen lassen
  □ Seewasser-Austritt am Auspuff kontrollieren
  □ Oeldruck-Anzeige pruefen (min. 2,5 bar warm)
  □ Kuehlwassertemperatur beobachten (Sollwert 75–85°C)
  □ Drehzahl pruefen (1.500 oder 3.000 ±30 min⁻¹)
  □ Spannung messen (230V ±5% oder 120V ±5%)
  □ Frequenz messen (50 Hz ±1% oder 60 Hz ±1%)
  □ Last schrittweise zuschalten (25% → 50% → 75% → 100%)
  □ Spannungsabfall bei Lastzuschaltung pruefen
  □ Frequenzeinbruch bei Lastzuschaltung pruefen
  □ Vibrationen bewerten (Hand auf Fundament)
  □ Schallpegel messen (7 m Abstand)
  □ 2 Stunden Probelauf unter 75% Last
  □ Nach Probelauf: Oel- und Kuehlwasserniveau kontrollieren
  □ Dichtheitspruefung aller Anschluesse
```

### 13.5 Jahresplanung Generatorbetrieb

**Saison-Vorbereitung (Fruehjahr):**
1. Oelstand und -zustand pruefen (Farbe, Konsistenz)
2. Kuehlwasserstand und Frostschutz-Konzentration pruefen
3. Impeller inspizieren (Risse, Verformung)
4. Kraftstoff auf Wasser/Kontamination pruefen
5. Batteriekapazitaet testen (Belastungstest)
6. Abgasanlage auf Dichtheit pruefen
7. Schwingmetalle visuell inspizieren
8. Probelauf 30 min unter Last

**Mid-Season-Check (nach 150–200 h):**
1. Oelwechsel + Filter (bei intensiver Nutzung)
2. Kraftstoff-Vorfilter pruefen/wechseln
3. Keilriemen-Spannung pruefen
4. Seewassersieb reinigen
5. Betriebsstunden dokumentieren

**Einwinterung (Herbst):**
1. Oelwechsel (saeure Neutralisierung ueber Winter)
2. Kuehlsystem mit Frostschutz befuellen (-20°C)
3. Seewasserseite mit Frostschutz oder vollstaendig entleeren
4. Tank vollfuellen + Diesel-Stabilisator
5. Batterie an Erhaltungsladegeraet
6. Abgas-Endrohr verschliessen (Feuchtigkeit, Insekten)
7. Schallkapsel leicht oeffnen (Luftzirkulation gegen Kondenswasser)

### 13.6 Kostenvergleich 10-Jahres-TCO

**Szenario: 12m Segelyacht, 4.000 Wh/Tag Verbrauch, 200 Betriebstage/Jahr**

| Kostenposition | Diesel-Gen (Fest) | Diesel-Gen (Var.) | Hydro + Klein-Gen | EFOY + Solar |
|---|---|---|---|---|
| **Anschaffung** | 9.500 | 15.000 | 12.000 | 18.000 |
| **Installation** | 3.000 | 3.000 | 4.500 | 2.500 |
| **Kraftstoff/Jahr** | 1.350 | 950 | 650 | 2.800 |
| **Wartung/Jahr** | 600 | 450 | 200 | 100 |
| **Reparaturen (∅/Jahr)** | 400 | 500 | 150 | 300 |
| **10-Jahres-TCO** | **35.500** | **37.000** | **26.500** | **52.500** |
| **TCO/kWh** | **0,49 EUR** | **0,51 EUR** | **0,37 EUR** | **0,72 EUR** |

**Annahmen:** Generator laeuft 2h/Tag, Diesel 1,85 EUR/l, Methanol 6 EUR/l, Hydrogenerator deckt 60% des Bedarfs unter Segel.

**Fazit:** Hydrogenerator + kleiner Diesel-Generator ist fuer aktive Fahrtensegler die wirtschaftlichste Loesung. EFOY lohnt sich nur wenn Laermfreiheit absolute Prioritaet hat.

### 13.7 Umweltvorschriften und Emissionszonen

**Emissionsfreie Zonen (Zero Emission Zones):**

| Region | Regelung | Auswirkung |
|---|---|---|
| Amsterdam Grachten | Emissionsfrei ab 2025 | Generator-Betrieb verboten |
| Oslo Fjord (Teile) | Emissionsfrei ab 2024 | Generator-Betrieb verboten |
| Venedig Lagune | Geschwindigkeits- + Emissionsbeschraenkung | Generator nur mit Katalysator |
| Balearen (Naturschutz) | Ankerzonen-Beschraenkungen | Generator nachts verboten |
| Galapagos | Strenge Emissionsvorschriften | Nur mit Genehmigung |
| Schwedische Schaeren | Laeberichte, lokale Vorschriften | Generator-Betrieb eingeschraenkt |

**Loesung fuer Emissionszonen:**
- Brennstoffzelle (EFOY) fuer Grundlast
- Grosse Batteriebank + Solar fuer 24–48 h Autonomie
- HVO-Diesel (biogener Kraftstoff, CO₂-neutral)
- Elektrische Heizung/Kuehlung aus Batterie

### 13.8 Schnittstellen und Protokolle

**Digitale Schnittstellen moderner Marine-Generatoren:**

| Protokoll | Hersteller | Daten | AYDI-Integration |
|---|---|---|---|
| NMEA2000 (PGN 127488ff) | Fischer Panda, Whisper Power | RPM, Temp, Druck, Spannung | Direkt via CAN-Gateway |
| J1939 (CAN) | Cummins, John Deere | Motor-Daten vollstaendig | Via J1939-Gateway |
| Modbus RTU/TCP | Diverse (Comap, ComAp) | Alle Betriebsdaten | Via Modbus-Adapter |
| Proprietaer CAN | Fischer Panda (iControl) | Vollstaendig | Via FP-Gateway |
| VE.Can / VE.Direct | Victron-Integration | Ladezustand, Leistung | Cerbo GX API |
| MQTT/REST | Moderne Systeme | Telemetrie, Alarme | Direkt-Integration |

**AYDI-Datenanforderungen fuer Condition Monitoring:**
```
Minimal (Pipeline A Grundanalyse):
  - Betriebsstunden
  - Wartungshistorie
  - Letzte Fehler

Standard (Pipeline A + Telemetrie):
  - Betriebsstunden, Starts
  - Temperaturverlauf (Kuehlwasser, Abgas)
  - Oeldruck-Historie
  - Spannungs-/Frequenzverlauf
  - Lastverlauf
  - Kraftstoffverbrauch

Premium (Pipeline A + B + C):
  - Alle Standard-Daten
  - Vibrationsanalyse (Beschleunigungssensor)
  - Oelanalyse (Partikelzaehlung, Viskositaet)
  - Thermografie (IR-Bilder)
  - Abgasanalyse (Truebung, NOx)
  - Service-Berichte (NLP-Extraktion)
```

### 13.9 Reserveteile an Bord

**Empfohlene Ersatzteile nach Fahrgebiet:**

| Teil | Kuestensegler | Mittelmeer | Blauwasser | Expeditionsyacht |
|---|---|---|---|---|
| Impeller + Dichtung | 1× | 2× | 3× | 5× |
| Oelfilter | 1× | 2× | 4× | 6× |
| Kraftstofffilter | 1× | 2× | 4× | 6× |
| Keilriemen | 1× | 1× | 2× | 3× |
| Thermostat | — | 1× | 1× | 2× |
| Zinkanode Waermetauscher | 1× | 2× | 4× | 6× |
| AVR (gesamtes Board) | — | — | 1× | 1× |
| Startrelais | — | 1× | 1× | 2× |
| Gluehkerzen-Satz | — | — | 1× | 2× |
| Dichtungssatz Ventildeckel | — | — | 1× | 1× |
| Kraftstoff-Hebelpumpe | — | — | 1× | 1× |
| Seewasserpumpen-Gehaeuse | — | — | — | 1× |
| Motoroel (fuer 2 Wechsel) | 1× | 2× | 2× | 4× |
| Kuehlwasser-Konzentrat 2l | 1× | 1× | 2× | 2× |

**Gewicht Ersatzteil-Kit (6 kW Generator):**
- Kuestensegler: ca. 3 kg
- Blauwasser: ca. 12 kg
- Expeditionsyacht: ca. 25 kg

### 13.10 Vibrations-Analyse und Condition Monitoring

**Schwingungsueberwachung als praediktives Wartungsinstrument:**

Marine-Generatoren eignen sich hervorragend fuer zustandsorientierte Wartung (Condition-Based Maintenance, CBM) mittels Schwingungsanalyse. Die konstante Drehzahl (bei Festdrehzahl-Generatoren) ermoeglicht praezise Frequenzanalyse.

**Typische Schwingungsfrequenzen:**

| Quelle | Frequenz (bei 1.500 min⁻¹) | Richtung | Indikator fuer |
|---|---|---|---|
| 1. Ordnung (1× Drehzahl) | 25 Hz | Radial | Unwucht, Ausrichtung |
| 2. Ordnung (2× Drehzahl) | 50 Hz | Radial/Axial | Ausrichtungsfehler, Lager |
| Zuendfrequenz (3-Zyl) | 37,5 Hz | Vertikal | Zuendaussetzer, Kompression |
| Zuendfrequenz (4-Zyl) | 50 Hz | Vertikal | Zuendaussetzer, Kompression |
| Netzfrequenz (elektrisch) | 50 Hz | Tangential | Wicklungsfehler, Luftspalt |
| Kugellager-Defekt (BPFO) | 75–150 Hz | Radial | Lagerschaden Aussenlaufbahn |
| Kugellager-Defekt (BPFI) | 100–200 Hz | Radial | Lagerschaden Innenlaufbahn |
| Zahneingriff (Getriebe) | 375–750 Hz | Radial | Getriebeverschleiss |

**Grenzwerte nach ISO 10816-3:**

| Klasse | Effektivwert (mm/s) | Bewertung | Massnahme |
|---|---|---|---|
| Gut | <2,8 | Neuzustand | Keine |
| Akzeptabel | 2,8–7,1 | Normaler Betrieb | Monitoring |
| Noch zulaessig | 7,1–18,0 | Erhoehter Verschleiss | Wartung planen |
| Unzulaessig | >18,0 | Schadensgefahr | Sofort abstellen |

**Einfache Bordueberwachung ohne Spezialmessmittel:**
- Muenzen-Test: 10-Cent-Muenze hochkant auf Generatorgehaeuse → Faellt sie um, Vibration zu hoch
- Handauflage: Deutlich spuerbares Kribbeln = >4 mm/s → beobachten
- Handauflage: Schmerzhaftes Vibrieren = >10 mm/s → Ursache finden
- Wasserglastest: Halbgefuelltes Glas auf Maschinenraum-Fundament → Kreisfoermige Wellen = normal, Spritzen = zu viel
- Gehoer: Schlagende/klopfende Geraeusche immer abnormal

**AYDI Vibrations-Scoring:**

```
vibration_score = 100 - (measured_rms / threshold_rms) × 50

Beispiel:
  Gemessen: 4,2 mm/s
  Grenzwert (akzeptabel): 7,1 mm/s
  Score: 100 - (4,2 / 7,1) × 50 = 100 - 29,6 = 70,4 Punkte

Bewertung:
  >85 Punkte: Ausgezeichnet
  70-85 Punkte: Gut
  55-70 Punkte: Befriedigend (Monitoring erhoehen)
  40-55 Punkte: Mangelhaft (Wartung noetig)
  <40 Punkte: Kritisch (Sofortmassnahme)
```

### 13.11 Generator-Parallelbetrieb — Detailbetrachtung

**Lastverteilung bei zwei Generatoren (Beispiel Superyacht):**

| Gesamtlast (kW) | Generator 1 | Generator 2 | Modus |
|---|---|---|---|
| 0–15 | 100% | AUS | Einzelbetrieb |
| 15–20 | Ueberlast-Grenze | Autostart | Synchronisierung |
| 20–30 | 50% | 50% | Parallelbetrieb |
| 30–35 | 50% | 50% | Parallelbetrieb (Reserveregion) |
| 35–40 | Alarm | Alarm | Lastabwurf-Warnung |
| 15→10 (fallend) | 100% | Autostop (Nachlauf) | Rueckkehr Einzelbetrieb |

**Synchronisierungsablauf (automatisch):**

```
1. Generator 2 startet (Autostart bei Schwelle)
2. Warmlauf-Phase: 60–120 s (Last = 0)
3. Spannungsangleichung: AVR stellt auf Netzspannung (±1V)
4. Frequenzangleichung: Governor stellt auf Netzfrequenz (±0,1 Hz)
5. Phasenwinkel-Synchronisation: Synchro-Check-Relais ueberwacht
   → Phasendifferenz <10° → Generatorschuetz schliesst
6. Lastuebernahme: Rampe 30 s bis Lastgleichverteilung
7. Load-Sharing aktiv: Droop oder Isochronous mit Lastteiler
```

**Schutzfunktionen im Parallelbetrieb:**
- Rueckleistungsschutz (verhindert Motorbetrieb des Generators)
- Differentialschutz (Kurzschluss zwischen Generatoren)
- Ueberstromschutz (selektiv je Generator)
- Unterspannungsschutz (Generator-Ausfall erkennen)
- Frequenzschutz (Ueber-/Unterfrequenz)

### 13.12 Typische Lebensdauer-Erwartungen

| Komponente | Lebensdauer (Stunden) | Lebensdauer (Jahre) | Einflussfaktoren |
|---|---|---|---|
| Dieselmotor (gesamt) | 8.000–15.000 | 15–30 | Wartung, Lastprofil, Oelqualitaet |
| Generator-Wicklung | 15.000–25.000 | 20–40 | Feuchtigkeit, Ueberlast |
| AVR | 8.000–15.000 | 10–20 | Spannungsspitzen, Feuchtigkeit |
| Inverter-Elektronik (VSD) | 5.000–12.000 | 8–15 | Temperatur, Feuchtigkeit, Vibration |
| Impeller | 250–1.000 | 1–3 | Material, Trockenlauf, Temperatur |
| Keilriemen | 1.000–3.000 | 3–7 | Spannung, Fluchtung, Hitze |
| Schwingmetalle | 3.000–8.000 | 5–12 | UV, Oel-Kontakt, Dauerbelastung |
| Starterbatterie | 3.000–5.000 | 4–7 | Ladeerhaltung, Temperatur |
| Einspritzduesen | 5.000–10.000 | 10–20 | Kraftstoffqualitaet |
| Turbolader | 8.000–15.000 | 15–25 | Oelqualitaet, Heissabstellen |
| Thermostat | 3.000–6.000 | 5–10 | Kuehlmittelqualitaet |
| Waermetauscher | 5.000–10.000 | 10–20 | Seewasserqualitaet, Zinkanode |
| Schallkapsel | — | 15–25 | UV, Feuchtigkeit, mechanisch |
| Kraftstoffschlaeuche | — | 5–10 | UV, Waerme, Kraftstoff-Typ |
| EFOY Stack | 5.000–10.000 | 5–10 | Betriebszyklen, Temperatur |
| Hydrogenerator (mechanisch) | 15.000+ | 15+ | Seewasser, Bewuchs |

### 13.13 Abkuerzungsverzeichnis

| Abkuerzung | Bedeutung |
|---|---|
| AGT | Aggregate (Fischer Panda Festdrehzahl-Serie) |
| ATS | Automatic Transfer Switch |
| BMS | Battery Management System |
| CBM | Condition-Based Maintenance |
| CCA | Cold Cranking Amps |
| COP | Continuous Operating Power |
| EMS | Energy Management System |
| ESP | Emergency Standby Power |
| GFK | Glasfaserverstaerkter Kunststoff |
| HVO | Hydrated Vegetable Oil |
| GTL | Gas-to-Liquid |
| IGBT | Insulated Gate Bipolar Transistor |
| PGN | Parameter Group Number (NMEA2000) |
| PMS | Power Management System |
| PRP | Prime Rated Power |
| RCD | Recreational Craft Directive |
| TCO | Total Cost of Ownership |
| TDS | Technical Data Sheet |
| VSD | Variable Speed Drive |

---

*Ende der Wissensdatei 22.11 — Generatoren und Stromerzeuger*
*AYDI v6 — AI Yacht Design Intelligence*
*Letzte Aktualisierung: 2026-05-08*
