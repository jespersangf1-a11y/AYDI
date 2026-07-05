---
category: "26_Heizung_Klima"
subcategory: "Heizung_Grundlagen"
title: "Marine Heating Fundamentals"
description: "Complete guide to yacht heating systems, sizing calculations, product types, manufacturers, diagnostics, troubleshooting."
created: 2026-05-18
language: "de"
target_audience: "Designers, service technicians, yacht owners"
---

# Heizung im Schiffbau — Grundlagen und Systemauslegung

## 1. Einführung

Die marine Heizung gehört zu den kritischen Komfortsystemen an Bord und prägt die Wintereignung eines Schiffs fundamental. Eine unzureichend dimensionierte Heizung führt zu Kondensation, Schimmelbildung und Unbewohnbarkeit. Überdimensionierung verschärft Energieverbrauch und Gewichtszuschlag.

Diese Dokumentation deckt:
- Berechnung des Wärmeverlusts nach maritimen Normen
- Systemauswahl für Segelyachten und Motorboote (2–30m)
- Konkrete Hersteller, Kosten, Lieferketten
- 12 Fehlerbilder mit Diagnosepfade
- 5 Troubleshooting-Entscheidungsbäume
- Pydantic v2 Datenmodelle für die AYDI-Integration

**Regulatorischer Rahmen:**
- ISO 11812 (Cockpits): Ventilation ≤ 2000 ppm CO₂
- ISO 9094-2 (Abgassicherheit): Abgasleitungen min. 100mm vom Innenraum entfernt
- EN 14687 (Schiffsgeräte): Heizleistung mit Überschreitung ≤ 10% betriebliches Maximum

---

## 2. Grundlagen der Wärmeverlustberechnung

### 2.1 Wärmeverlustvektoren

Wärmeverluste an Bord entstehen durch:

| Vektor | Anteil | Berechnung |
|--------|--------|-----------|
| Hülle (Rumpf, Deck, Kabinen) | 55–70% | U-Wert × Fläche × ΔT |
| Luftwechsel (Lecks, Fenster, Luken) | 15–25% | n₅₀ × Volumen × ΔT |
| Wasser im Bilgenraum | 8–15% | Wärmeleitung durch Rumpfboden |
| Bodenplatte (bei Schwimmer) | 5–10% | Kontakt zu Wasser (0°C) |

### 2.2 U-Wert-Standards nach Bootsklasse

**Segelboot Standard (Sardinien-Winter, +5°C außen, +20°C innen):**

| Bauteil | U-Wert [W/m²K] | Dicke (GFK) | Material |
|---------|----------------|-----------|---------|
| Rumpf (unterhalb WL) | 0.45–0.65 | 60–80mm | GFK + 40mm Schaum |
| Rumpf (oberhalb WL) | 0.35–0.55 | 60mm | GFK + 40mm Schaum |
| Deck | 0.25–0.40 | 100mm | GFK + 60mm Schaum + Teak |
| Kajüte-Schotten | 0.20–0.35 | 100mm | Sperrholz + Schaumkern |
| Fenster/Bullaugen | 1.80–2.50 | 4–6mm | Makrolon, einfach |
| Türen/Luken | 0.80–1.20 | 40–60mm | Holzrahmen + Dichtung |
| Bodenplatte | 0.55–0.80 | 50–70mm | GFK + Schaum |

**Motorboot Deluxe (Malta-Winter, +8°C außen, +22°C innen):**
- Alle U-Werte um 15–20% besser durch dickere Isolierung und Doppelverglasungen

### 2.3 Wärmeverlustformel (EN 12215-7)

```
Q_hull = Σ(U_i × A_i × ΔT_i)  [W]

Q_air = 0.34 × n₅₀ × V × ΔT    [W]
  mit n₅₀ = Luftwechselrate bei 50 Pa (1/h)
  V = Innenvolumen [m³]

Q_total = Q_hull + Q_air + Q_bilge + Q_water
```

**Beispiel: 12m Segelboot, Mittelmeer-Winter**
- Außentemperatur: +5°C
- Innentemperatur: +20°C
- ΔT = 15K
- Hülle: 35m² effektiv × 0.50 W/m²K × 15K = 262.5W
- Luftwechsel: 0.34 × 3 (1/h) × 40m³ × 15K = 612W
- Bilge/Wasser: 150W (Konservativ)
- **Q_total ≈ 1025W ≈ 1.0 kW**

Für Atlantic-Winter (+2°C außen, ΔT=18K) → 1.25 kW erforderlich.

### 2.4 BTU zu kW Konversion und Leistungsklassen

| kW | BTU/h | Bootsklasse | Raumgröße |
|----|-------|-------------|-----------|
| 2–4 | 6,800–13,600 | 8–12m Segler | Einzelkabine |
| 4–8 | 13,600–27,300 | 12–18m Segler/Motor | Hauptkabine |
| 8–15 | 27,300–51,200 | 18–25m Yacht | Gesamtschiff |
| 15–30 | 51,200–102,400 | 25m+ Super-Yacht | Multi-Zonen |

**Faustregel:** 100 W pro m³ Volumen für Mittelmeer-Winter; +15% Atlantic, +30% Nord-Europa.

### 2.5 Isolierungsoptimierung

**Wärmeverlust-Reduktion durch Material:**

| Maßnahme | U-Wert-Reduktion | Kosten EUR | ROI (5 Jahre) |
|----------|------------------|-----------|---------------|
| +20mm Polyurethan-Kern | 25–30% | 2,500 | Sehr hoch (geringere Heizung) |
| Doppelverglasung (Bullaugen) | 35–40% | 800 | Hoch |
| Dichtungsleisten (fenster) | 8–12% | 150 | Sehr hoch |
| Reflektive Innenisolierung | 10–15% | 600 | Mittel |
| Thermische Vorhänge (Kajüten) | 15–20% | 200 | Hoch |

---

## 3. Heizungstypologie

### 3.1 Diesel-Luftheizung (Hot Air)

**Funktionsprinzip:** Diesel-Brenner erhitzt Wärmetauscher, ein Ventilator bläst heiße Luft durch Kanäle.

**Vorteile:**
- Schnelle Aufwärmung (10–15 Min. bis 20°C)
- Kompakt, unter Motorraum installierbar
- Keine Zusatzinstallation (außer Abgasleitung)
- Effizient bei Segelbooten mit nur Motorraum-Heizung

**Nachteile:**
- Luftströmung oft ungleichmäßig
- Lautes Ventilator-Geräusch (70–80 dB)
- Höherer Dieselverbrauch als Wasserheizung
- Brandrisiko bei fehlerhaftem Einbau

**Typische Modelle:**
- Webasto Air Top 2000 ST (2 kW): 1,200 EUR
- Eberspächer D4 (4 kW): 1,800 EUR
- Wallas 50E (5 kW): 2,100 EUR (finnisch, robust)

### 3.2 Diesel-Wasserheizung (Hydronic)

**Funktionsprinzip:** Diesel-Brenner erhitzt Wasser, das durch Rohre zu Heizkörpern oder Fußbodenheizung zirkuliert.

**Vorteile:**
- Gleichmäßige Wärmeverteilung
- Leiser als Luftheizung (Pumpe ~60 dB)
- Kombinierbar mit Solarmodulen oder Motor-Abwärmenutzung
- Langsamere, tiefere Erwärmung (angenehmer)

**Nachteile:**
- Komplexere Installation (Rohre, Armaturen, Ausdehnungsgefäß)
- Frostschutzflüssigkeit erforderlich (Winterschutz)
- Störungsanfällig (Blockaden, Entlüftung)
- Höheres Gewicht (~80 kg System)

**Typische Modelle:**
- Webasto Thermo Top C (4 kW): 2,200 EUR
- Eberspächer Hydronic B5 (5 kW): 2,600 EUR
- Refleks RV 95 (9.5 kW, schwedisch): 3,100 EUR

### 3.3 Elektrische Heizung

**Funktionsprinzip:** Widerstandsheizelemente, 220V oder 380V Bordnetz.

**Vorteile:**
- Einfache Installation (nur Stecker + Steckdose)
- Leise und wartungsfrei
- Keine Abgasleitung

**Nachteile:**
- Hoher Stromverbrauch (3–5 kW bei 30A Bordnetz problematisch)
- Nur im Hafen mit Landstrom praktikabel
- Teuer im Betrieb (0.25 EUR/kWh Landstrom)

**Anwendung:** Ergänzungsheizung, nicht Primärsystem. Typische Kosten: 500–1,200 EUR für 1–2 kW Leuchten-Heizgeräte.

### 3.4 Wärmepumpe (Heat Pump)

**Funktionsprinzip:** Entzieht Wärme aus Seewasser (selbst bei +5°C noch vorhanden), verstärkt sie. COP = 2.5–3.5.

**Vorteile:**
- Energieeffizient: 2.5–3.5 kW Wärme pro 1 kW Strom
- Kühlung im Sommer möglich
- Nachhaltig, wenn Bordstrom aus Solar/Wind

**Nachteile:**
- Hohe Anschaffung: 8,000–15,000 EUR für komplettes System
- Lärm des Kompressors (60–75 dB)
- Seewasserpumpe + Durchlass erforderlich
- Vereisungsrisiko bei < 2°C Wasser

**Zielmarkt:** 18m+ Yachten mit großem Strombudget. Noch nicht im Standard-Segment.

### 3.5 Festbrennstoff (Kohleofen, Holzofen)

**Funktionsprinzip:** Traditionelle Verbrennung, Wärmeabstrahlung + Konvektion.

**Vorteile:**
- Romantisch, keine Stromabhängigkeit
- Hoch zuverlässig (Mechanik nur, keine Elektronik)
- Günstig zu kaufen (800–2,500 EUR)

**Nachteile:**
- Gefährlich bei Seegang (Brandrisiko)
- Umweltbelastung (Feinstaub, Soot)
- Regelmäßiges Beladen/Reinigung erforderlich
- Lagerproblem (Brennstoff-Lagerung)
- Regulatorisch in vielen Häfen verboten

**Anwendung:** Nur Nischen-Segment (klassische Yachten, Fernkreuzer mit Selbstversorgung). Dickinson Neptune (Kohleofen): 2,200 EUR.

---

## 4. Produktlinien und Systemarchitektur

### 4.1 Diesel-Luftheizung Produktlinien

**Webasto (Deutscher Marktführer, 85% Anteil):**
- Air Top 2000: 2 kW, 1.2 L/h Verbrauch, 12V/24V
- Air Top 3500: 3.5 kW, 1.8 L/h
- Air Top 5000: 5 kW, 2.5 L/h (für 15m+ Yachten)
- DBW 300: 3 kW, Wasser-Hybrid

**Eberspächer (Europäischer Konkurrent):**
- D4: 4 kW, 1.6 L/h, 24V Primär
- D5: 5 kW, 2.0 L/h
- Hydronic B5: 5 kW Wasser-Heizung

**Wallas (Finnischer Spezialist):**
- 50E: 5 kW, Luftheizung, geräusch­arm (68 dB)
- 50E-DW: 5 kW + Boilerfunktion
- Kosten: +20% über Webasto, aber Zuverlässigkeit

**Refleks (Schwedisch, Nischen-Segment):**
- RV 95: 9.5 kW Wasserheizung, für Superyachten
- Robust, gebrauchte oft noch im Einsatz

### 4.2 Systemkomponentenliste (8–12m Standard-Segelboot)

```
Heizgerät:              Webasto Air Top 2000ST    1,200 EUR
Abgasleitung (3m):      Stahlrohr + Isolierung     250 EUR
Brennstoffleitung:      Stainless 316L, Schläuche 150 EUR
Steuereinheit:          Digital 12V Regler          180 EUR
Thermisches Schutzrohr: Isoliertes Kanal-Set       400 EUR
Installation Labor:     4 Std. @ 80 EUR/h          320 EUR
─────────────────────────────────────────────────
TOTAL:                                            2,500 EUR
```

**Für Wasserheizung (+Aufpreis):**
```
Webasto Thermo Top C:   2,200 EUR
Heizkörper (2 Stück):    600 EUR
Rohrleitungen (50m):     800 EUR
Ausdehnungsgefäß:        200 EUR
Zirkulationspumpe:       150 EUR
Thermostat-Ventile:      300 EUR
Installation Labor:      600 EUR
─────────────────────────────────────────────────
TOTAL:                                            5,250 EUR
(Aufpreis: +2,750 EUR ≈ 110%)
```

---

## 5. Hersteller und Marktpreise

### 5.1 Primäre Heizungs-Hersteller

| Hersteller | Herkunft | Produktbereich | Marktanteil | Preisstrategie |
|-----------|----------|---------------|------------|-----------------|
| Webasto | Deutschland | Air/Water Diesel | 45% | Premium |
| Eberspächer | Deutschland | Air/Water Diesel | 35% | Premium |
| Wallas | Finnland | Air Diesel (robust) | 10% | +20% |
| Refleks | Schweden | Water Diesel (Super-Yacht) | 5% | Ultra-Premium |
| Dickinson | USA | Solid Fuel, Kochöfen | 3% | Nische |
| Hurricane | Dänemark | Diesel Compact | 2% | Budget |

### 5.2 Detailpreisliste (2026 EUR, inkl. MwSt.)

**Luftheizung:**
- Webasto Air Top 2000 ST: 1,200 EUR
- Webasto Air Top 3500: 1,450 EUR
- Webasto Air Top 5000: 1,850 EUR
- Eberspächer D4 (4kW): 1,800 EUR
- Eberspächer D5 (5kW): 2,050 EUR
- Wallas 50E: 2,100 EUR
- Hurricane HT-1000 (1kW, Budget): 850 EUR

**Wasserheizung:**
- Webasto Thermo Top C (4kW): 2,200 EUR
- Webasto DBW 300 (3kW, hybrid): 2,000 EUR
- Eberspächer Hydronic B5 (5kW): 2,600 EUR
- Refleks RV 95 (9.5kW): 3,100 EUR
- Refleks RV 55 (5.5kW): 2,500 EUR

**Zubehör (pro System):**
- Abgasleitung + Anschlüsse: 250–400 EUR
- Heizkörper (1 Stück): 250–350 EUR
- Thermostate + Regelung: 200–400 EUR
- Installation (Fachbetrieb): 1,500–3,000 EUR

**Gesamtbudget nach Bootsgröße:**
- 8–10m Segelboot: 3,500–4,500 EUR (Luftheizung)
- 12–15m Segelboot: 5,500–7,500 EUR (Wasserheizung bevorzugt)
- 18–22m Motor-Yacht: 8,000–12,000 EUR (Multi-Zone, Redundanz)

---

## 6. Fehlerbild-Atlas (12 Patterns)

### FB-26-01-001: Keine Zündung beim Kaltstart

**Symptom:** Heizgerät startet nicht, Steuereinheit zeigt Zündfehler nach 3–5 Sekunden.

**Ursachen (Priorisiert):**
1. Kein Diesel in Tank oder Leitungsluft (90% der Fälle)
2. Zündkerze verschmutzt/verdreckt (8%)
3. Ignition-Spule defekt (2%)

**Diagnoseschritte:**
```
IF Dieseltank leer THEN → Tanken + Leitungsentlüftung (Entlüftungsventil)
IF Diesel vorhanden THEN
  → Zündkerze ausbauen, visuell inspizieren
  → Farbe: weiß/grau = verschmutzt, schwarz = Ölabbrand
  IF Verschmutzt THEN → Reinigen mit Bürste, trocknen
  IF Schwarze Kruste THEN → Austausch erforderlich (15 EUR)
  IF Zündkerze i.O. THEN
    → Ignition-Spule-Spannung messen (12V beim Start?)
    → NEIN → Spule defekt (Austausch 80 EUR)
```

**Häufigkeit:** Saisonal nach Winterpause sehr häufig (25% aller Serviceaufträge März–Mai).

---

### FB-26-01-002: Heizung läuft unregelmäßig, Flammenschwankung

**Symptom:** Heizleistung fluktuiert; Temperatur springt ±3°C, manchmal Aussetzer.

**Ursachen:**
1. Luftblasen in Brennstoffleitung (35%)
2. Verschmutzte Brennerdüse (30%)
3. Defekter Brennstoff-Filter (20%)
4. Steuereinheit-Kalibrierung drift (15%)

**Diagnoseschritte:**
```
→ Brennstoffleitung auf Tropfen-Luftblasen prüfen (visuell)
  IF Blasen sichtbar THEN
    → Entlüftungsventil öffnen, 10 Sekunden halten
    → Schlauch am Rücklauf-Port öffnen, Diesel ablaufen lassen (50ml)
    → Ventil schließen, neu starten
→ IF immer noch fluktuierend THEN
  → Brennerdüse ausbauen (2 Sechskant-Schrauben)
  → Mit Druckluft (4 bar) durchpusten (RICHTUNG: von hinten!)
  → Brennstoff-Filter prüfen: wechseln wenn >6 Monate alt
  → Steuereinheit neu kalibrieren (Webasto-Software erforderlich)
```

**Häufigkeit:** Häufig nach Langzeitlagerung oder nach Druckabfall.

---

### FB-26-01-003: Abgasgeruch im Innenraum

**Symptom:** Distinct Diesel-Abgasgeruch in Kabine, eventuell mit Rußflecken um Augen/Bullaugen.

**Ursachen:**
1. Undichte Abgasleitung (40%)
2. Abgasleitung zu nah an Lüftung (25%)
3. Undichte Brennkammer (20%)
4. Rückstrom bei Seewasserpumpe (15%)

**Diagnoseschritte:**
```
→ Heizgerät starten, visuell nach Abgasleck suchen
  IF Sichtbare Lecks am Rohr THEN
    → Rohrverbindung überprüfen, Schellen festziehen
    → IF Rost durchgebrochen THEN → Rohrabschnitt austausch (100 EUR)
→ Abgasleitung-Routing überprüfen (sollte 100mm von Luft­einlässen entfernt)
  IF zu nah THEN
    → Abgasleitung umverlegen (Arbeit ~3 Std. @ 80 EUR/h)
→ Brennkammer auf Risse prüfen (Endoskop erforderlich, 50 EUR Inspektion)
→ Seewasserpumpen-Ventil überprüfen (Rückflussbremse?)
```

**Häufigkeit:** Häufig nach unsachgemäßer Installation oder Verschleiß (5+ Jahre).

---

### FB-26-01-004: Übertemperatur-Abschaltung, Sicherung gelöst

**Symptom:** Heizung schaltet nach 2–5 Minuten ab, Sicherungsschalter springt raus.

**Ursachen:**
1. Luftfilter blockiert (60%)
2. Wärmetauscher verstopft (25%)
3. Thermostat-Ventil klemmt (10%)
4. Elektronik-Defekt (5%)

**Diagnoseschritte:**
```
→ Luftfilter prüfen (visual check hinter Einlassblende)
  IF schwarz/braun verfärbt THEN → Austausch (20 EUR, 10 Min.)
→ Wärmetauscher-Eingang prüfen (Thermografie: sollte warm sein, nicht heiß)
  IF Eingang heiß, Ausgang kalt THEN → Blockade vermuten
    → Backflush mit Druckluft versuchen (Druck ≤ 3 bar!)
    → IF erfolglos THEN → Chemische Spülung (Citric Acid, 8 Std.)
→ Thermostat-Ventil prüfen (manuell öffnen möglich?)
  IF klemmt THEN → Öl WD-40 einspritzen, zyklisch öffnen
  → IF hart THEN → Ventil-Austausch (150 EUR)
→ Sicherungs-Schalter überprüfen (Bimetall-Typ?), ggf. Kalibrierung prüfen
```

**Häufigkeit:** Saisonal vor Wintersaison häufig (mangelnde Wartung).

---

### FB-26-01-005: Heizgerät startet, aber keine Wärmeleistung (Leerlauf-Flamme)

**Symptom:** Heizung läuft, aber Abgastemperatur niedrig (~80°C statt 200°C), Raumtemperatur steigt nicht.

**Ursachen:**
1. Fehlerhafte Flammenregelung (Sensor verdreckt) (50%)
2. Zu niedriger Brennstoff-Druck (25%)
3. Fehlerhafter Wärmeverteiler-Ventil (15%)
4. Thermosensor-Fehler (10%)

**Diagnoseschritte:**
```
→ Brennstoff-Druck messen (Messpunkt am Brenner, sollte 0.8–1.2 bar)
  IF < 0.8 bar THEN
    → Brennstoff-Pumpe prüfen (Impuls-Test mit Ohmmeter)
    → IF keine Pulsationen THEN → Pumpe defekt (Austausch 200 EUR)
→ Flammen-Sensor (Ionisierungs-Stab) prüfen
  → Sensor ausbauen, mit Feuchttuch reinigen
  → Unter UV-Licht prüfen (sollte blauschwarz glänzen, nicht matt)
  → IF matt/grau THEN → Austausch (40 EUR)
→ Wärmeverteiler-Ventil prüfen (handbetätigung möglich?)
  → Wenn Handbetrieb möglich, ist Steuerung fehlerhaft
→ Thermosensor-Durchgang messen (Ohmmeter, sollte <20Ω bei +20°C)
  → IF offen Schaltung THEN → Sensor-Austausch (60 EUR)
```

**Häufigkeit:** Mittel (10% aller Serviceaufträge).

---

### FB-26-01-006: Starker Rußauswurf, schwarzer Belag auf Abgasöffnung

**Symptom:** Sichtbarer schwarzer Ruß tritt aus Abgasöffnung aus, Rußflecken in Umgebung.

**Ursachen:**
1. Fetter Brennstoff-Gemisch (60%)
2. Abgenutzte Düse (Verschleiß, Erosion) (20%)
3. Schlechter Diesel (Kontamination) (15%)
4. Luftzufuhr-Drosselung (5%)

**Diagnoseschritte:**
```
→ Brennstoff-Gemisch-Einstellung prüfen (Verstellschraube am Brenner)
  → Schraube im Uhrzeigersinn drehen (magerer) um 0.5 Windungen
  → 30 Sekunden Betrieb, Rußauswurf beobachten
  → IF noch schwarz THEN wiederhole
  → (Normal: fast kein Ruß, höchstens grauer Hauch)
→ Brennerdüse prüfen (Durchmesser-Verschleiß?)
  → Ausbauen, unter Lupe: sollte Öffnung scharf und rund sein
  → IF aufgeraut/elliptisch THEN → Austausch (120 EUR)
→ Diesel-Proben aus Tank + Behälter testen
  → IF Verfärbung/Trübung THEN → Tank entleeren, spülen, neuer Diesel
→ Luft-Zufuhr überprüfen (Ansaugschlauch auf Blockade?)
  → IF verstopft THEN → Lüftungsöffnungen freimachen
```

**Häufigkeit:** Häufig bei älteren Geräten (>5 Jahre) ohne Wartung.

---

### FB-26-01-007: Wasserdruck-Abfall in Heizkreislauf (Wasserheizung)

**Symptom:** Manometer zeigt Druckabfall von 1.5 bar auf <0.8 bar über Nacht, Heizkörper weniger warm.

**Ursachen:**
1. Lecks in Rohrsystem (50%)
2. Entlüftung (Luftblasen bilden „Vakuum") (30%)
3. Ausdehnungsgefäß defekt (Membran gerissen) (15%)
4. Thermometer-Ventil leckend (5%)

**Diagnoseschritte:**
```
→ Rohrsystem auf sichtbare Lecks prüfen
  → Alle Verbindungen (Verschraubungen) visuell + feuchtes Tuch
  → IF Tropfen zu sehen THEN
    → Verschraubung mit Rohrzange festziehen (max. 1 Umdrehung!)
    → IF immer noch Tropfen THEN → Dichtring-Austausch erforderlich
→ Entlüftungs-Ventil öffnen (oben am Heizkörper oder Zirkulations-Punkt)
  → Sollte nach 10 Sekunden klares Wasser kommen (kein Zischen)
  → IF Zischen: Luft entweicht, neue Luft eintreten lassen, 2 Min. warten
→ Ausdehnungsgefäß überprüfen
  → Ventil am oberen Punkt: sollte 0.8 bar Vordruck haben
  → Mit Reifendruck-Prüfer messen
  → IF Druck gefallen THEN
    → Membran gerissen (nicht reparierbar)
    → Gefäß austausch (250 EUR)
```

**Häufigkeit:** Häufig bei Wasserheizung (Langzeitbetrieb >3 Jahre).

---

### FB-26-01-008: Heizgerät vibriert/poltert, Geräusch-Entwicklung

**Symptom:** Deutliches Klopf-Geräusch (100–120 Hz) aus Heizgerät-Bereich.

**Ursachen:**
1. Lockerer Brenner-Flansch (40%)
2. Expansions-Turbulenz (Wasser-Systeme) (35%)
3. Montage auf nicht-isoliertem Untergrund (20%)
4. Ventilator-Unbalance (5%)

**Diagnoseschritte:**
```
→ Heizgerät visuell überprüfen (Verschraubungen)
  → Alle Schrauben systematisch überprüfen + festziehen
  → Brenner-Flansch: 4 Schrauben sollten mit 10 Nm festgezogen sein
  → Prüf-Drehmoment-Schlüssel verwenden
→ Für Wasserheizung: Expansions-Entlüftung durchführen
  → Heizung ausschalten, 30 Minuten abkühlen
  → Entlüftungs-Ventil langsam öffnen (kleine Umdrehung)
  → Wasser sollte ohne Luftblasen austreten
→ Montagefläche überprüfen (fest? elastisch?)
  → Heizgerät sollte auf Gummi-Isolatoren oder Stahlrahmen ruhen
  → IF direkt auf Sperrholz-Boden THEN → Montage-Kit unter Gerät (80 EUR)
→ Ventilator-Schaufel visuell prüfen
  → IF Verschmutzung sichtbar THEN → Druckluft ausblasen
```

**Häufigkeit:** Mittel (5–8% der Serviceaufträge).

---

### FB-26-01-009: Digitale Steuereinheit zeigt Error-Code (E01, E02, E04, E05)

**Symptom:** Displayanzeige zeigt numerischen Fehlercode, Heizung läuft nicht oder stoppt sporadisch.

**Fehler-Code-Tabelle:**

| Code | Bedeutung | Lösungsschritte |
|------|-----------|-----------------|
| E01 | Zündfehler | → Zündkerze prüfen, Diesel checken |
| E02 | Flammen-Sensor | → Sensor reinigen oder austauschen |
| E04 | Überhitzung | → Luftfilter reinigen, Abgasleitung prüfen |
| E05 | Spannungsfehler | → Batterie-Spannung (11.5–14V?), Kontakte reinigen |
| E07 | Brennstoff-Pumpe | → Pumpenimpuls prüfen, Druck messen |
| E10 | Sensorbruch | → Thermosensor-Durchgang messen |

**Allgemeine Troubleshooting:**
```
→ Batterie-Spannung messen: sollte 11.5–14V sein
  → IF <11V THEN → Batterie laden/austausch
  → IF >14.5V THEN → Regler überprüfen (Ladeanlage?)
→ Error-Code merken, Heizung neustarten
  → Schalter aus 30 Sekunden, wieder an
  → IF Error persistiert THEN → Code notieren, Hersteller kontaktieren
→ Fehler-Reset nur wenn Behebung sicher:
  → Menü → Einstellungen → Factory Reset (bestätigen)
```

**Häufigkeit:** Häufig bei älteren Geräten (>8 Jahre), seltener bei modernen (Webasto 2015+).

---

### FB-26-01-010: Unzureichende Raumerwärmung trotz Betrieb

**Symptom:** Heizgerät läuft (Thermostat aktiv), aber Kabinentemperatur steigt nicht über +15°C (Zielwert: +20°C).

**Ursachen:**
1. Heizleistung unterdimensioniert für Volumen (30%)
2. Unzureichende Luftzirkulation (Kanal-Verstopfung) (25%)
3. Zu hoher Wärmeverlust (Lecks, mangelhafte Isolierung) (25%)
4. Defekter Thermostat (20%)

**Diagnoseschritte:**
```
→ Wärmeverlust-Audit durchführen
  → Infrarot-Thermometer: Messungen an Rumpf, Deck, Fenster (ΔT?)
  → Wenn Rumpf <+10°C, Deck <+8°C → massive Wärmeverluste
  → Fenster-Kondenswasser? Silikon-Fugen undicht?
→ Heizgerät-Leistung vs. Raumvolumen vergleichen (s. Abschnitt 2.4)
  → Faustregel: 100 W pro m³
  → 40 m³ Volumen benötigt ≥ 4 kW
  → IF aktuelles Gerät < erforderlich THEN → Upgrade notwendig
→ Luftzirkulations-System überprüfen
  → Alle Auslässe (Düsen) prüfen: sollten warme Luft blasen
  → IF einige kalt THEN → Kanal-Verstopfung oder Verschluss
  → Verstellbare Schieber alle öffnen
→ Thermostat-Funktion testen
  → Sollwert auf +25°C stellen, warten 10 Min.
  → Heizgerät sollte kontinuierlich laufen
  → IF Heizung bleibt aus THEN → Thermostat-Austausch (150 EUR)
```

**Häufigkeit:** Häufig bei Retrofit-Installationen (falsche Dimensionierung 20% der Fälle).

---

### FB-26-01-011: Kondensation und Schimmelbildung trotz Heizung

**Symptom:** Morgens Kondenswasser auf Bullaugen/Spiegeln, muffiger Geruch, erste Schimmel-Flecken an Deckeln/Holz.

**Ursachen:**
1. Relative Feuchte >70% (unangemessene Belüftung) (50%)
2. Heizung läuft zu kurz/nachts aus (30%)
3. Kabin-Dichtigkeit zu schlecht (Fenster-Undichtigkeit) (15%)
4. Schlechte Luftzirkulation (tote Winkel) (5%)

**Diagnoseschritte:**
```
→ Hygrometer-Messung durchführen (30 EUR Gerät)
  → Sollwert tagsüber: 45–55% rel. Feuchte
  → IF > 65% THEN
    → Lüftung erhöhen (Fenster 20 Min. öffnen, täglich morgens)
    → Heizung-Thermostat auf +20°C stellen (kontinuierliche Wärmequelle)
→ Fenster-Dichtung überprüfen
  → Feuchter Finger an Fenster-Rahmen halten, Luftzug spürbar?
  → IF Zug THEN
    → Silikon-Dichtung überprüfen (sollte elastisch sein, nicht rissig)
    → Austausch: 50–150 EUR pro Fenster
→ Nachts-Heizung-Programm prüfen
  → Viele Heizungen haben „Night Mode": Thermostat auf +18°C reduzieren
  → Besser: kontinuierlich +15–16°C halten
→ Luftzirkulation überprüfen
  → Mobile Lüfter in Kabinen-Ecken aufstellen (USB-Lüfter, 20 EUR)
  → Durchbruch-Lüftung zwischen Räumen (Türen nachts offen?)
```

**Häufigkeit:** Sehr häufig in Nordeuropa/Atlantic-Cruising (70% der Boots-Eigner berichten im Winter).

---

### FB-26-01-012: Heizgerät zündet mehrfach hintereinander (Sicherungs-Schleife)

**Symptom:** Heizgerät schaltet alle 5–10 Minuten aus/an, ständiges Pulterplustern, Stop-and-Start-Betrieb.

**Ursachen:**
1. Thermostat zu empfindlich (Sollwert-Hystérese falsch) (40%)
2. Luftzirkulation-Problem (heiße Lufttasche unter Sensor) (30%)
3. Thermosensor schlecht positioniert (15%)
4. Batterie-Spannungs-Schwankungen (15%)

**Diagnoseschritte:**
```
→ Thermostat-Einstellung prüfen
  → Normal-Einstellung: Sollwert +20°C mit ±2K Hystérese
  → IF Hystérese <1K THEN → Menü → Thermo-Einstellungen, +2K setzen
  → Heizung sollte dann Temperatur halten ohne Zyklisierung
→ Thermosensor-Position überprüfen (z.B. in Wohnbereich-Auslasskanal)
  → Sensor sollte in freier Luftströmung sein
  → IF verstellt/verbogen THEN → Gerade biegen
  → IF hinter Möbel THEN → Umverlegen (Arbeit 1 Std.)
→ Batterie-Spannungs-Stabilität prüfen
  → Voltmeter während Heizungs-Betrieb anschließen
  → Spannung sollte stabil ±0.2V bleiben
  → IF Schwankungen ±0.5V THEN
    → Batterieverbindungen reinigen (Grünspan?)
    → Batterie ggf. austausch oder alternatives Ladesystem
→ Sensor-Kalibrierung überprüfen
  → Factory Reset durchführen (Menü → Einstellungen)
  → Thermostat neu setzen und 1 Stunde beobachten
```

**Häufigkeit:** Mittel (5–10% der Serviceaufträge, typisch bei Retrofit/Steuereinheit-Upgrade).

---

## 7. Troubleshooting-Entscheidungsbäume

### Baum 1: Heizung startet nicht / Gar kein Leben

```
START: Heizgerät reagiert nicht auf Einschalten

├─ Ist die Batterie geladen? (12V oder 24V je nach System)
│  ├─ NEIN → Batterie laden, neu starten
│  └─ JA → weiter
│
├─ Batterie-Spannung unter Last? (Voltmeter während Heizung-Versuch)
│  ├─ < 10.5V → Batterie zu schwach, laden
│  ├─ 10.5–11.5V → Marginal, laden + Fehler-Reset versuchen
│  └─ > 11.5V → weiter
│
├─ Sicherung gebrannt? (Prüfen: 15A oder 20A je nach Hersteller)
│  ├─ JA → Sicherung austauschen, neu starten
│  │   └─ Wenn sofort wieder raus → Kurzschluss, Fachbetrieb
│  └─ NEIN → weiter
│
├─ Ist das Dieselventil offen? (Prüfen: manueller Hebel)
│  ├─ NEIN → Ventil öffnen, neu starten
│  └─ JA → weiter
│
├─ Ist Diesel im Tank? (Dipstab oder Tankgeber-Anzeige)
│  ├─ NEIN → Tanken, Luftblasen entlüften (Entlüftungsventil 10 Sekunden)
│  └─ JA → weiter
│
├─ Steuereinheit-Display aktiv? (LED-Kontrolle)
│  ├─ Keine Anzeige → Stromverlust, Batterie-Anschlüsse prüfen
│  ├─ Anzeige ohne Fehlermeldung → weiter
│  └─ Anzeige mit Fehler-Code → siehe Abschnitt FB-26-01-009
│
├─ Zündversuch hörbar? (Brenner sollte klicken/pult)
│  ├─ NEIN → Ignition-Spule defekt oder Flammen-Sensor unterbrochen
│  └─ JA → Zündung funktioniert, aber Flamme zündet nicht
│     ├─ Zündkerze sichtbar glühend? (Sichtloch im Brenner)
│     │  ├─ NEIN → Zündkerze wechseln (15 EUR, 15 Min.)
│     │  └─ JA → weiter
│     │
│     └─ Brennstoff-Druck ausreichend? (Messpunkt am Brenner, 0.8–1.2 bar)
│        ├─ NEIN → Brennstoff-Pumpe defekt (200 EUR)
│        └─ JA → Flammen-Sensor prüfen (reinigen oder austausch)

ENDE: Aktion durchgeführt, neu starten
```

### Baum 2: Heizung läuft, aber zu wenig Wärme

```
START: Heizgerät betriebsbereit, Temperatur-Sollwert nicht erreicht

├─ Raumtemperatur aktuell? (Thermometer)
│  ├─ < +10°C bei Sollwert +20°C → Heizleistung unzureichend
│  │  └─ Siehe Abschnitt 2.4: Leistungs-Dimensionierung prüfen
│  └─ +15–19°C bei Sollwert +20°C → Marginal, weiter
│
├─ Heizgerät-Auslegung für Bootsgröße? (m³ Volumen × 100W Faustformel)
│  ├─ Zu klein → Upgrade notwendig (+5,000–10,000 EUR)
│  └─ Korrekt dimensioniert → weiter
│
├─ Luftverteilungs-Kanäle offen und unverstopft?
│  ├─ Prüfe alle Aus-Düsen: sollten warme Luft blasen
│  ├─ NEIN → Kanäle freimachen (Verstopfung durch Spinnweben?)
│  └─ JA → weiter
│
├─ Räume zu sehr gelüftet? (Fenster, Luken offen?)
│  ├─ JA → Schließen, 30 Min. warten
│  └─ NEIN → weiter
│
├─ Wärmeverlust-Audit: Infra-Messung an Rumpf/Deck/Fenster
│  ├─ Rumpf-Oberfläche < +8°C → Isolierung unzureichend (teuer zu beheben)
│  ├─ Kondenswasser auf Bullaugen → Fenster-Dichtung defekt (Austausch-Option)
│  └─ Alles warm → weiter
│
├─ Heizgerät-Sensoren richtig kalibriert?
│  ├─ Factory Reset → Neu-Kalibrierung
│  └─ Wenn immer noch Problem → Thermo-Sensor austausch (60 EUR)

ENDE: Wärme sollte nun verteilt werden
```

### Baum 3: Heizung läuft, aber Geräuscharmes erforderlich

```
START: Lärm aus Heizgerät oder Kanal

├─ Geräusch-Typ identifizieren:
│  ├─ „Pfeifen" (hochfrequent) → Luft-Strömungs-Pfeife
│  │  └─ Luft-Auslässe überprüfen (verstopft? Blende schief?)
│  ├─ „Poltern/Klopfen" (tief) → Mechanische Vibration
│  │  └─ Siehe Abschnitt FB-26-01-008
│  ├─ „Ratteln" → Lockere Verschraubungen
│  │  └─ Systematisches Nachziehen aller Schrauben
│  └─ „Brummen" (Ventilator) → Normalgeräusch, meist <80 dB
│
├─ Nur bei Betrieb oder auch im Stillstand?
│  ├─ Im Stillstand → Problem anderswo (Rumpf-Strömung, Wind)
│  └─ Bei Betrieb → weiter
│
├─ Vibrationsisolierung prüfen
│  ├─ Gerät sollte auf Gummi-Isolatoren ruhen
│  ├─ NEIN → Montage-Kit unter Heizgerät (80 EUR)
│  └─ JA → weiter
│
├─ Geräusch durch Schnelle reduzieren?
│  ├─ Einige Heizgeräte: Gebläse-Drehzahl ist verstellbar
│  ├─ Menü → Fan Speed auf 50% reduzieren (weniger Wärme, weniger Lärm)
│  └─ Wenn nicht verstellbar → keine Lösung (Design-Limitation)

ENDE: Geräuschreduzierung optimal oder akzeptabel
```

### Baum 4: Heizung läuft, aber Fehler-Codes oder Abschaltung

```
START: Wiederkehrende Fehlermeldungen oder Abschaltungen

├─ Fehler-Code aus Display notieren (E01, E02, E04, E05 etc.)
│  └─ Siehe Abschnitt FB-26-01-009 für Code-Interpretation
│
├─ Häufigkeit der Fehler?
│  ├─ Einmalig, seit dem Neustart weg → Transient, evtl. Software-Reset
│  │  └─ Neu-Kalibrierung durchführen
│  └─ Wiederkehrend → weiter
│
├─ Zeitliche Muster?
│  ├─ Immer nach 10–15 Min. → Übertemperatur (siehe FB-26-01-004)
│  ├─ Alle 5 Min. aus/an → Thermostat-Zyklisierung (siehe FB-26-01-012)
│  └─ Unregelmäßig → weiter
│
├─ Batterie-Spannung während Fehler prüfen
│  ├─ Wenn < 11.5V beim Fehler → Stromversorgung verstärken
│  └─ Wenn stabil → weiter
│
├─ Hersteller-Support kontaktieren
│  ├─ Fehler-Code + Betriebsstunden + Heizgerät-Modell + Seriennummer
│  └─ Remote-Diagnose oft möglich (kostenlos bei <5 Jahre Alter)

ENDE: Reparatur oder Austausch eingeleitet
```

### Baum 5: Diesel-Verbrauch zu hoch

```
START: Verbrauch > erwartet (z.B. >2.5 L/h für 4 kW)

├─ Betriebsmodus überprüfen
│  ├─ Thermostat zu hoch gesetzt? (+25–30°C statt +20°C?)
│  │  └─ Reduzieren auf +18–20°C (Sparsamkeit: 20–30% Verbrauch)
│  └─ Normal: +20°C → weiter
│
├─ Verbrennungsqualität prüfen
│  ├─ Sichtbare Rußentwicklung aus Abgasöffnung?
│  │  ├─ JA → Brenner-Einstellung zu fett (siehe FB-26-01-006)
│  │  │  └─ Verstellschraube 0.5 Umdrehungen fetter-zu-mager drehen
│  │  └─ NEIN → weiter
│
├─ Diesel-Qualität prüfen
│  ├─ Diesel-Behälter / Kanister: Verfärbung oder Trübung sichtbar?
│  │  ├─ JA → Neuer Diesel erforderlich (Tank spülen)
│  │  └─ NEIN → weiter
│
├─ Heizungsvebrauch historisch vergleichen
│  ├─ Ist Betriebsdauer (h) höher als erwartet?
│  │  └─ Oft: kalter Winter oder schlechte Isolation Ursache
│  │  └─ Nicht zu beheben außer Isolation upgraden
│
├─ Düsen-Verschleiß / Brenner-Ineffizienz
│  └─ Nach >1000 Betriebsstunden: Düse austausch reduziert Verbrauch um 5–10%

ENDE: Verbrauch monitoren, nächste Wartung plane
```

---

## 8. Häufig Gestellte Fragen (FAQ 25+)

**F1: Kann ich eine Diesel-Luftheizung selbst einbauen?**
A: Ja, mit technischen Grundkenntnissen und Werkzeug. Allerdings: Abgasleitung erfordert maritimer Standard (ISO 9094), und Fehler führen zu Brandrisiko oder CO-Vergiftung. Empfehlung: Fachbetrieb (400 EUR Installation vs. 2,500 EUR neue Heizung bei Schaden). Video-Anleitungen von Webasto/Eberspächer helfen.

**F2: Wie lange dauert die Aufwärmung von +5°C auf +20°C in einer 12m-Kabine?**
A: Mit 4 kW Diesel-Heizung: 30–45 Minuten durchschnittlich. Wasser-Heizung: 60–90 Min. (Wärmespeicher). Luft-Heizung (2 kW): 60–90 Min.

**F3: Ist eine Heizung für einen Segelboot im Sommer notwendig?**
A: Nicht für Wärmeleistung, aber oft für Entfeuchtung sinnvoll (Heizung + Lüftung reduziert Kondenswasser). Nicht im Dauerbetrieb, aber sporadisch nachts sinnvoll.

**F4: Webasto vs. Eberspächer — welche ist besser?**
A: Funktional äquivalent. Webasto dominiert Markt (85%), hat bessere Ersatzteil-Verfügbarkeit. Eberspächer gilt als etwas robuster, ist aber 10 % teurer. Wallas (finnisch) hat kultige Reputation, 20 % Aufpreis.

**F5: Kann eine alte Öl-Standup-Heizung den Betrieb weiterführen?**
A: Ja, wenn Dicht und Funktion gegeben. Typischerweise 20–30 Jahre Lebensdauer. Aber: Einige Häfen (insbesondere Umweltzonen wie Mittelmeer) verbieten offene Flammen. Modernisierung ist Trend.

**F6: Heizungs-Sicherung gebrannt — warum?**
A: Normalerweise: 15A oder 20A je nach Heizleistung. Wenn sofort wieder raus: Kurzschluss im Stromkreis (Kabel-Beschädigung, feuchter Stecker). Fachbetrieb. Einmalig raus bei Übertemperatur ist normal (Überlast-Schutz).

**F7: Wie oft muss die Heizung gewartet werden?**
A: Jährlich vor Winter:
  - Luftfilter reinigen
  - Brennstoff-Filter wechseln (wenn >6 Monate alt)
  - Zündkerze prüfen
  - Abgasleitung visuell inspizieren
  Kosten: 200–400 EUR.

**F8: Kann ich die Heizung den ganzen Winter laufen lassen?**
A: Ja. Thermostaten steuern an/aus-Zyklen. Dauerfeuer ist automatisiert. Diesel-Verbrauch: ~2 L/Tag bei 4 kW, kontinuierlich. Budget: ~500 EUR/Monat Winterdiesel.

**F9: Was kostet die Heizung im Betrieb pro Stunde?**
A: Diesel-Heizung 4 kW: ~1.6 L/h. Dieselpreis aktuell ~1.50 EUR/L → 2.40 EUR/h.

**F10: Ist die Heizung beim Segeln aktiv?**
A: Ja. Manche Segler segeln mit Heizung (Komfort). Aber: Nur Segler mit Motor-Option ist das relevant. Reiner Segelbetrieb (no motor) kann Heizung nicht tanken. Design-Entscheidung beim Boot-Kauf.

**F11: Kann die Heizung an Bord überladen werden?**
A: Nein. Bordnetz 12V oder 24V ist begrenzt. Aber: Heizgerät braucht nur Startleistung (100–150A spike für Ignition), ansonsten 20–30A kontinuierlich. Standard Bordnetz OK.

**F12: Heizung läuft, aber Thermostat regelt nicht — Fehler?**
A: Häufig: Thermosensor-Position schlecht (unter Möbel, hinter Gardine). Oder Sensor verdreckt. Reinigen oder 50 EUR Sensor-Austausch.

**F13: Kann ich zwei Heizungen parallel betreiben?**
A: Technisch ja, aber: Bordnetz-Belastung verdoppelt (~60A), nicht praktisch. Besser: Eine größere Heizung (Upgrade) oder Zonen-Heizung (separate kleine Heizung in vorder Kabine).

**F14: Welche Heizung bei Superyacht (25m+)?**
A: Multi-Zone-System: Hauptanteil über zentrale Wasserheizung (8–15 kW Webasto/Eberspächer), plus Zonen-Luft-Heizung für Master Cabin (redundanz). Kosten: 15,000–30,000 EUR inkl. Installation.

**F15: Heizung brennt, aber keine Temperatur im Wasser-Kreislauf?**
A: Wasser-Heizung: Pumpe nicht pumpend (Blockade) oder Thermostat-Ventil sitzt (offen = kein Durchfluss). Prüfe: Manometer am Aus-Port, sollte Druck anzeigen. Wenn nicht: Pumpe oder Ventil.

**F16: Kann Solar-Solaranlage die Heizung ersetzen?**
A: Nein, nicht im Winter. Solar-Input zu niedrig. Aber: Kann Boiler-Vorwärm-Funktion übernehmen (Wasser-Heizung Hybrid). Spart 20–30% Diesel wenn 4m² Solar-Panel vorhanden.

**F17: Heizung braucht Lüftungsöffnung — wo soll die sein?**
A: Luft-Heizung: Außenluftzufuhr vorne (Höhe ≥ 300mm über WL für Sicherheit), Abluft durch normale Kabin-Luft. Abgasleitung: Durch Rumpf-Durchlass, minimal 100mm über WL.

**F18: Heizung mit Seewasser-Kreislauf — ist das möglich?**
A: Ja, aber nicht empfohlen. Seewasser-Korrosion und biologisches Fouling. Standard: Süßwasser-Kreislauf mit Glykol-Frostschutz.

**F19: Welche Heizung für Liveaboard in Hamburg (0°C Winter)?**
A: 5–8 kW Wasserheizung mit Redundanz (Elektro-Backup 2 kW). Isolierung upgraden. Kosten: 8,000–12,000 EUR.

**F20: Heizung-Thermostat-Einstellung — +20°C vs. +18°C, welche sparen?**
A: 2 K Reduktion = 10–15 % Diesel-Einsparung. Pro Monat: ~100–150 EUR. Nicht dramatisch, aber messbar.

**F21: Kann die Heizung explosive Dämpfe erzeugen?**
A: Diesel-Heizung: Nein, Flammen werden kontrolliert. Aber: Wenn Diesel-Tank beschädigt (Lecks), kann Dieseldampf explosiv sein. Heizung selbst: sicher wenn sachgemäß installiert.

**F22: Heizung braucht Service — wo finde ich einen Techniker?**
A: Marinas, Bootswerften haben Standard-Partner. Alternativ: Hersteller (Webasto, Eberspächer) führen zertifizierte Techniker-Listen. Kosten: 80–150 EUR/Stunde + Teile.

**F23: Gebrauchte Heizung kaufen — worauf achten?**
A: Betriebsstunden prüfen (unter 2000h = gut, >5000h = beäuge). Rostflecken an Brenner (normales Alter). Starten-Test durchführen. Erwartete Lebensdauer: 5000–8000 h. Preis: 50 % unter Neu.

**F24: Ist die Heizung für die CE-Zertifizierung vorgeschrieben?**
A: Nicht explizit. Aber: Kategorien A–B (Offshore, Ocean) brauchen oft verneinte Anforderung an Temperatur-Haltung. Praktisch: alle modern Yachten haben Heizung.

**F25: Kann ich die Heizung mit meinem Smartphone steuern?**
A: Moderne Geräte (Webasto 2020+, Eberspächer 2018+): Ja, via App (Bluetooth + Server). Ältere: Nein, nur manuelle Temperatur-Regler. Upgrade: 200–400 EUR für Smart-Modul.

---

## 9. Glossar (40+ Begriffe)

| Begriff | Definition |
|---------|-----------|
| **Abgasleitung** | Rohr zur Ableitung von Heizabgasen über Rumpf, ISO 9094 Standard min. 100mm über WL |
| **Ausdehnungsgefäß** | Puffer-Behälter in Wasserheizung, kompensiert thermische Expansion (typisch 2–5L) |
| **Backflush** | Rückwärts-Druckluft durch Wärmetauscher zum Entfernen von Ablagerungen |
| **Bimetall-Thermostat** | Mechanischer Schalter basierend auf Metall-Ausdehnung, kein Strom erforderlich |
| **Brennstoff-Filter** | Kartridge zum Filtern von Diesel vor Pumpe, Standard Austausch 6–12 Monate |
| **Brennstoff-Pumpe** | Elektro-Pumpe, drückt Diesel zum Brenner, typischerweise 12V oder 24V |
| **Brennerdüse** | Precisions-Sprühöffnung, Durchmesser 0.45–0.65 mm, Verschleiß nach 1000+ Betriebsstunden |
| **BTU** | British Thermal Unit, 1 BTU = 0.293 Watt, oft für Heizleistung angegeben |
| **Bypassventil** | Sicherheits-Ventil in Wasserheizung, öffnet wenn Druck >2.0 bar |
| **Cockpit-Sill** | Erhöhte Schwelle am Cockpit-Eingang, ISO 11812 spezifiziert Höhe nach Boots-Kategorie |
| **COP (Coefficient of Performance)** | Effizienz-Kennziffer Wärmepumpe: Wärme-Output / Strom-Input, typisch 2.5–3.5 |
| **Delta-T (ΔT)** | Temperaturdifferenz, z.B. Außen +5°C, Innen +20°C = ΔT 15K |
| **Diesel-Verbrauch** | Typisch 0.5–1.0 L/kW/h je nach Heizgerät, Betriebsmodus, Isolierung |
| **Doppelverglasung** | Bullaugen mit zwei Glasscheiben + Luftspalt, U-Wert ~1.8 W/m²K |
| **Entlüftungsventil** | Manuelles Ventil zum Entfernen von Luftblasen aus Wasserheizung, sollte täglich genutzt werden |
| **Frostschutzflüssigkeit** | Glykol-basiert (Propylenglykol marine, nicht Ethylenglykol), Gefrierpunkt -20°C bis -40°C |
| **Gebläse-Drehzahl** | Ventilator-Umdrehungen, steuerbar in modernen Heizungen zur Lärm-Reduktion |
| **Glykol-Wasser-Gemisch** | Standard für Wasserheizung: 40 % Glykol, 60 % Wasser, Frostschutz und Korrosionsschutz |
| **Heizleistung** | Thermale Power in Watt oder kW, dimensioniert nach Wärmeverlust + Reserven |
| **Heizkreislauf** | Geschlossene Rohrentwicklung mit Zirkulationspumpe, Heizkörper, Ventilen |
| **Hygrometer** | Feuchtemessgerät, zeigt relative Feuchte in %, ideal 45–55% für Kabinen |
| **Ignition-Spule** | Hochspannungs-Trafo zur Zündung der Zündkerze, 12/24V zu 10+ kV |
| **Infrarot-Thermometer** | Berührungslose Temperatur-Messung, für Oberflächen-Audits |
| **Integrale Luft-Sammelbox** | Kanal-Plenum, sammelt heiße Luft vor Verteilung zu Kabinen |
| **Ionisierungs-Sensor** | Flammen-Erkennungs-Element, elektrische Leitfähigkeit in Flammen messend |
| **ISO 12217** | Standard für Schiffs-Stabilität, beeinflusst CG-Anforderung (Gewichtsverteilung) |
| **ISO 9094-2** | Standard für Abgas-Sicherheit, min. Abstände zu Innenraum |
| **Kanal-Isolierung** | Schaumstoff oder Mineralwolle um Kanal-Rohre, reduziert Lautstärke um 10–15 dB |
| **Kondensation** | Wasserdampf kondensiert zu flüssigem Wasser bei Erreichen Taupunkt |
| **Lärm-Pegel (dB)** | Diesel-Luft-Heizung 70–80 dB, Wasserpumpe 60–70 dB, Standard-Grenze Nacht 55 dB |
| **Manometer** | Druckmessgerät in Wasserheizung, zeigt Betriebsdruck 1.0–2.0 bar |
| **Membran-Ausdehnungsgefäß** | Modern, mit innerer Gummi-Membran, 0.8 bar Vordruck erforderlich |
| **Modulation** | Variable Heizleistung (z.B. 20–100%), nicht nur Ein/Aus, reduziert Zyklisierung |
| **Motorraum-Temperatur** | Sollte unter +50°C bleiben, Heizgerät braucht Lüftung |
| **n₅₀-Wert** | Luftwechselrate bei 50 Pa Druckdifferenz, für Leckageverluste relevant |
| **Osmotische Bläschen** | GFK-Defekte durch Wasser-Eindringung in Harz, Oberflächenprobleme |
| **PTC-Heizer** | Positiver Temperatur Koeffizient, selbstregulierend, sicher (überhitzet nicht) |
| **Reflektive Isolierung** | Aluminiumfolie + Luftspalt, reflektiert 95 % Wärmestrahlung |
| **Redundanz** | Backup-Heizung, falls Primär-Heizung ausfällt (Standard für Superyachten) |
| **Rücklauf-Leitung** | Kaltes Wasser zurück zum Heizgerät, sollte temperiert ankommen (40–60°C) |
| **Schachtdeckel (Hatch)** | Luken-Zugang, ISO 12216 min. Öffnungsgröße 400×520mm für Notausgang |
| **Schlauch-Schellen** | Stahlband um Rohre, Anzugsdrehmoment 2–4 Nm (nicht zu fest!) |
| **Steuereinheit (ECU)** | Electronic Control Unit, regelt Zündung, Brennstoff-Zuführung, Temperatur |
| **Taupunkt** | Temperatur bei welcher Luftfeuchte zu Wasser kondensiert, abhängig von relativer Feuchte |
| **Thermischer Kurzschluss** | Warmes Abgas zu nah an Lüftungs-Einlass, Luft wird rückwärts erwärmt (ineffizient) |
| **Thermostat-Ventil** | Regulierendes Ventil, öffnet bei +20°C, schließt bei +22°C (Hysterese) |
| **U-Wert (Wärmedurchgangs-Koeffizient)** | Wärmestrom pro m², K, je niedriger desto besser. Standard GFK ~0.5 W/m²K |
| **Verbindungsschlauch** | Leitungsverbindung zwischen Tank und Heizgerät, muss marine-grade sein |
| **Verschleiß-Inspektionen** | Regelmäßige Brennerdüsen-Abnutzungs-Kontrolle nach 2000+ Betriebsstunden |
| **Vordruck (Ausdehnungsgefäß)** | Stickstoff-Vordruck, sollte 0.8 bar bei kaltem System sein |
| **Warmwasser-Speicher** | Tank zum Speichern von Wärme, (z.B. 50L), reduziert Häufigkeit von Heizung-Starts |
| **Wärmetauscher** | Metallisches Element, überträgt Heizwärme zu Luft oder Wasser |
| **Windschutz (Cockpit)** | Kunststoff-Windabweiser am Cockpit, vermindert Windkühlung, Effizienz +15 % |
| **Zündkerze** | Glühkeramik-Element, Heiz-Temperatur 1200–1300°C, Austausch 15 EUR |
| **Zirkulationspumpe** | Elektro-Pumpe, treibt Wasser durch Heizkreislauf, typisch 12V 10–20A |

---

## 10. Schnell-Referenz

### 10.1 Checkliste Heizungs-Inbetriebnahme (Saisonstart)

- [ ] Batterien-Spannung prüfen (12V oder 24V Nominell)
- [ ] Dieseltank inspizieren (Wasser-Kondensat?), ggf. Absperrhahn öffnen
- [ ] Brennstoff-Filter visuell überprüfen (alt >6 Monate?)
- [ ] Zündkerze ausbauen, inspizieren (grau OK, schwarz/krümelig → wechseln)
- [ ] Abgasleitung auf Dellen/Rost überprüfen
- [ ] Steuereinheit Batterie-Anschlüsse säubern
- [ ] Teststart durchführen (sollte <30 Sekunden zünden)
- [ ] Thermostat auf +20°C setzen, 15 Min. betrieb beobachten (Zustand?)
- [ ] Abgasgeruch-Test (sollte keinen Innenraum-Geruch geben)
- [ ] Luftzirkulation testen (alle Kanäle warm?)

### 10.2 Schnell-Diagnosechart

```
Kein Start         → Batterie (E1) → Diesel (E2) → Zündkerze (E3) → Fachbetrieb
Läuft, keine Wärme → Luftfilter → Wärmetauscher → Thermostat-Sensor
Zu laut            → Montage-Isolierung → Luft-Lecks → Ventilator-Drehzahl
Zu viel Verbrauch  → Brenner-Einstellung → Diesel-Qualität → Düse-Verschleiß
Fehler-Code        → Siehe Abschnitt FB-26-01-009 → Factory Reset → Hersteller
```

### 10.3 Kostenübersicht (2026 EUR)

| Komponente | Kosten |
|-----------|--------|
| Kleine Luft-Heizung (2 kW) | 1,000–1,300 EUR |
| Standard Luft-Heizung (4 kW) | 1,200–1,600 EUR |
| Premium Luft-Heizung (5 kW) | 1,800–2,200 EUR |
| Wasser-Heizung (4 kW) | 2,200–2,700 EUR |
| Installation (Fachbetrieb, 4–6 Std.) | 1,500–3,000 EUR |
| Jährliche Wartung | 200–400 EUR |
| Saisonaler Diesel-Verbrauch (5 Monate) | 2,000–4,000 EUR |

### 10.4 Garantien und Hersteller-Support

| Hersteller | Standard-Garantie | Erweiterte Garantie | Support |
|-----------|-------------------|-------------------|---------|
| Webasto | 2 Jahre | 5 Jahre (+300 EUR) | Online-Diagnose, deutsche Hotline |
| Eberspächer | 2 Jahre | 3 Jahre (+200 EUR) | Techniker-Netzwerk |
| Wallas | 3 Jahre | 6 Jahre (+150 EUR) | Direkter Hersteller-Support |
| Refleks | 3 Jahre | – | Limited (Nischen-Segment) |

---

## ANHANG A: Fallstudie 1 — 12m Segelboot Mittelmeer-Winter

**Schiff:** Beneteau Oceanis 40 (12m, 40m³ Wohnraum), Sardinien-Basis.

**Anforderung:** Heizung für Dezember–März, Temperatur stabil +20°C bei außen +5°C.

**Berechnung:**
- Wärmeverlust: 40 m³ × 100 W/m³ = 4.0 kW (Faustformel)
- Detailkalkulation: Hull 280W + Air 620W + Bilge 150W = 1.05 kW (realistisch)
- Reserv: +30% für schlechte Isolierung = 1.35 kW netto
- Empfehlung: 2.0 kW (um überdimensioniert zu sein) = Webasto Air Top 2000 ST

**Kosten:**
- Heizgerät: 1,200 EUR
- Installation: 800 EUR (4 Stunden)
- Abgasleitung: 250 EUR
- Steuerung: 180 EUR
- **Total: 2,430 EUR**

**Betriebskosten:**
- Diesel: 1.2 L/h × 1.50 EUR/L = 1.80 EUR/h
- Saisonal (5 Monate, 20 h/Woche): 1,800 EUR
- Wartung: 300 EUR/Jahr

**Ergebnis:** Akzeptabel für Mittelmeer-Wintersegeln. Boot ist bewohnbar.

---

## ANHANG B: Fallstudie 2 — 18m Motor-Yacht Hamburg (Liveaboard)

**Schiff:** Sunseeker Predator 52 (15m, 85 m³ Wohnraum), Hamburg Hafen (0°C Winter).

**Anforderung:** Ganzjahres-Bewohnbarkeit, +22°C komfortable Temperatur.

**Berechnung:**
- Wärmeverlust: 85 m³ × 140 W/m³ (North Europe) = 11.9 kW
- Isolierung durch Upgrade (dickere Schäume, Doppelverglasung): -20% = 9.5 kW netto
- Reserv: +25% für Extremkälte (-5°C) = 11.9 kW finale Anforderung

**System (Hybrid-Redundanz):**
- Primär: Webasto Thermo Top C (4 kW Wasserheizung) = 2,200 EUR
- Zusatz: Wallas 50E (5 kW Luftheizung) = 2,100 EUR
- Elektro-Backup: 2 kW Heizlüfter = 500 EUR
- Total Heizleistung: 11 kW (Redundanz gegeben)

**Installation:**
- Wassersystem (Rohre, Heizkörper x 3, Pumpe, Ventile): 2,500 EUR
- Luft-Kanäle: 1,200 EUR
- Doppel-Steuerung: 600 EUR
- Fachinstallation (15 Std.): 2,000 EUR
- **Total: 11,100 EUR**

**Betriebskosten:**
- Diesel (Wasserheizung): 1.6 L/h (4 kW × 0.4 L/kW/h) = 2.40 EUR/h
- Winter 24h/Tag, 150 Tage/Jahr = 8,640 EUR/Jahr Diesel
- + Elektro-Backup 20 h/Woche im März/April = 400 EUR (Landstrom)
- Wartung: 500 EUR/Jahr
- **Total Betrieb: 9,540 EUR/Jahr**

**Ergebnis:** Teuer, aber notwendig für Hamburg-Liveaboard. ROI: 0 (Komfort-Investition). Langfristig sinnvoll mit Isolation-Upgrade.

---

## ANHANG C: Fallstudie 3 — 8m Charteryacht Karibik (Ganzjahres-Nutzung)

**Schiff:** Catana 42 Katamaran (8m, 28 m³), Segelchart Virgin Islands.

**Anforderung:** Gelegentliche Heizung für Gäste (Dezember–Februar, +15°C min.), ansonsten Klima-Kühlung.

**Berechnung:**
- Wärmeverlust bei +15°C → +20°C: 28 m³ × 50 W/m³ (tropic, milder) = 1.4 kW
- + Gast-Komfort-Margin: 2.0 kW empfohlen
- Allerdings: Segelboot oft tagsüber unterwegs (Sonnen-Wärmeeintrag), Heizung nur nachts

**System (Minimalist):**
- Tragbare Diesel-Luftheizung Hurricane HT-1000 (1 kW) = 850 EUR
- Oder: Kombiniert mit Landstrom-Elektro-Heizlüfter 2 kW (Hafen-Nächte) = 400 EUR
- **Total: 1,250 EUR**

**Betriebskosten:**
- Saisonal 3 Monate, 5 h/Nacht = 450 h/Jahr
- Diesel: 0.5 L/h × 1.50 EUR/L = 225 EUR/Jahr
- Landstrom: 50 h/Jahr × 0.25 EUR/kWh × 2 kW = 25 EUR/Jahr
- Wartung: 100 EUR/Jahr
- **Total: 350 EUR/Jahr**

**Ergebnis:** Budgetfreundlich. Für Charteryacht akzeptabel. Gäste glücklich im Dezember.

---

## ANHANG D: Fallstudie 4 — Klassisches Segelyacht-Retrofit (Kutter aus den 1980ern)

**Schiff:** Albin Vega 27 (8m, 22 m³), Classic Segler, ohne Heizung.

**Anforderung:** Retrofit-Heizung für ganzjahres-Cruising Mittelmeer/Atlantic.

**Berechnung:**
- Wärmeverlust (alte Isolation, einfach Fenster): 22 m³ × 150 W/m³ = 3.3 kW
- Isolierungs-Verbesserung (Retrofit Styrofoam-Patches, Fenster-Dichtung): -25% = 2.5 kW

**Herausforderung Klassisches Boot:**
- Keine Motorraum-Platz (Diesel klein oder Segel-nur)
- Manche haben Motor später hinzugeführt
- Platz-Engpass: Heizgerät muss unter Bett oder Galley passen

**System (Compact):**
- Webasto Air Top 2000 ST (2 kW) = 1,200 EUR
- Retrofit-Kanal (Limited, nur Salon): 600 EUR
- DIY-Installation (Eigentümer technisch versiert): 400 EUR (Material)
- Labor (12 Stunden Fachbetrieb): 1,200 EUR
- Abgasleitung (Durchbruch durchs Deck): 350 EUR
- **Total: 3,750 EUR**

**Upgrade-Option (Isolation):**
- Styrofoam-Padding Rumpf (DIY): 500 EUR
- Dichtung-Pakete Fenster: 200 EUR
- → Gesamt-Investition: 4,450 EUR

**Ergebnis:** Möglich, aber aufwändig. Klassische Boote sind Raumengpässe. Planung mit Fachbetrieb notwendig.

---

## ANHANG E: Wärmeverlusts-Berechnungs-Werkzeug (Pseudo-Code)

```
FUNCTION calculate_heat_loss(boat_spec):
  INPUT:
    boat_spec = {
      loa: 12.5,           // Länge über alles, m
      beam: 3.8,           // Breite, m
      draft: 1.8,          // Tiefgang, m
      cabin_count: 2,      // Kabinen
      cabin_vol_m3: 40,    // Gesamtvolumen Wohnraum
      hull_material: "GFK",
      hull_insulation_mm: 60,
      deck_insulation_mm: 100,
      window_count: 8,
      window_area_m2: 0.6,  // pro Fenster
      door_count: 4,
      exterior_temp_c: 5,
      desired_interior_temp_c: 20,
      boat_class: "sailboat",  // sailboat | motorboat | superyacht
      location: "mediterranean" // mediterranean | atlantic | north_sea
    }

  delta_t = desired_interior_temp_c - exterior_temp_c

  // Hull U-value lookup table
  IF boat_class == "sailboat":
    IF hull_insulation_mm < 40:
      u_hull = 0.65
    ELSE IF hull_insulation_mm < 80:
      u_hull = 0.45
    ELSE:
      u_hull = 0.35
  END IF

  // Deck U-value
  IF deck_insulation_mm < 60:
    u_deck = 0.50
  ELSE IF deck_insulation_mm < 120:
    u_deck = 0.30
  ELSE:
    u_deck = 0.20
  END IF

  // Window U-value (single glaze)
  u_window = 2.0

  // Door U-value
  u_door = 0.95

  // Calculate surface areas (simplified)
  hull_area = 2 * loa * (draft + beam/2)  // Approximation
  deck_area = loa * beam
  window_area_total = window_count * window_area_m2
  door_area_total = door_count * 0.5  // Assume 0.5 m² per door

  // Conduction heat loss
  q_hull = u_hull * hull_area * delta_t
  q_deck = u_deck * deck_area * delta_t
  q_window = u_window * window_area_total * delta_t
  q_door = u_door * door_area_total * delta_t
  q_conduction = q_hull + q_deck + q_window + q_door

  // Air change rate (n50 = air changes at 50 Pa)
  IF boat_class == "sailboat":
    n50 = 4.0  // Older boats, leaky
  ELSE IF boat_class == "motorboat":
    n50 = 2.5
  ELSE:
    n50 = 1.5  // Superyacht, sealed
  END IF

  // Infiltration heat loss (EN 12215-7)
  q_air = 0.34 * n50 * cabin_vol_m3 * delta_t

  // Bilge/water heat loss (conservative estimate)
  q_bilge = 150  // Watts, constant

  // Regional factor
  IF location == "mediterranean":
    regional_factor = 1.0
  ELSE IF location == "atlantic":
    regional_factor = 1.15
  ELSE IF location == "north_sea":
    regional_factor = 1.35
  END IF

  // Total heat loss
  q_total = (q_conduction + q_air + q_bilge) * regional_factor

  // Add safety margin (30%)
  heater_power_required_kw = q_total * 1.30 / 1000

  RETURN {
    q_conduction_w: q_conduction,
    q_air_w: q_air,
    q_bilge_w: q_bilge,
    q_total_w: q_total,
    heater_power_kw: heater_power_required_kw,
    recommended_model: recommend_heater(heater_power_required_kw)
  }
END FUNCTION

FUNCTION recommend_heater(power_kw):
  IF power_kw < 2.0:
    RETURN "Webasto Air Top 2000 ST"
  ELSE IF power_kw < 4.0:
    RETURN "Webasto Air Top 3500 or Eberspächer D4"
  ELSE IF power_kw < 6.0:
    RETURN "Webasto Air Top 5000 or Wallas 50E"
  ELSE IF power_kw < 10.0:
    RETURN "Webasto Thermo Top C + Wallas 50E (dual zone)"
  ELSE:
    RETURN "Refleks RV95 + Electric Backup"
  END IF
END FUNCTION
```

---

## ANHANG F: Pydantic v2 Datenmodelle

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

# Heizgerät-Typen
class HeaterType(str, Enum):
    DIESEL_AIR = "diesel_air"
    DIESEL_WATER = "diesel_water"
    ELECTRIC = "electric"
    HEAT_PUMP = "heat_pump"
    SOLID_FUEL = "solid_fuel"

# Fehler-Codes
class ErrorCode(str, Enum):
    E01 = "ignition_failure"
    E02 = "flame_sensor"
    E04 = "overheat"
    E05 = "voltage"
    E07 = "fuel_pump"
    E10 = "sensor_break"

# Hersteller
class ManufacturerType(str, Enum):
    WEBASTO = "webasto"
    EBERSPACHER = "eberspacher"
    WALLAS = "wallas"
    REFLEKS = "refleks"
    DICKINSON = "dickinson"
    HURRICANE = "hurricane"

# Konfidenz-Level
class ConfidenceLevel(str, Enum):
    MEASURED = "measured"
    CALCULATED = "calculated"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"

# Fehlerbild-Definition
class FaultImage(BaseModel):
    model_config = {"from_attributes": True}
    
    fault_id: str = Field(..., description="FB-26-01-001 format")
    symptom: str = Field(..., description="Benutzer-sichtbares Symptom")
    causes: List[str] = Field(..., description="Geordnete Ursachen-Liste")
    diagnosis_steps: str = Field(..., description="Schritt-für-Schritt Diagnosepfad")
    frequency_percent: float = Field(..., description="Häufigkeit in % aller Serviceaufträge")
    resolution_time_hours: float = Field(..., description="Durchschnittliche Reparaturdauer")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    created_at: datetime = Field(default_factory=datetime.now)

# Heizgerät-Modell
class HeatingDevice(BaseModel):
    model_config = {"from_attributes": True}
    
    manufacturer: ManufacturerType
    model_name: str
    heater_type: HeaterType
    power_kw: float = Field(..., description="Nennleistung in kW")
    power_btu: float = Field(..., description="Nennleistung in BTU/h")
    fuel_consumption_lh: Optional[float] = Field(None, description="Dieselverbrauch L/h")
    voltage_v: int = Field(..., description="12V oder 24V")
    weight_kg: float
    dimensions_mm: str = Field(..., description="L x W x H in Millimetern")
    price_eur: float = Field(..., description="Marktpreis 2026 EUR")
    warranty_years: int = Field(default=2)
    noise_db: Optional[int] = Field(None, description="Schallpegel in dB(A)")
    maintenance_interval_hours: int = Field(default=500)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)

# Bootheizoptions-Empfehlung
class HeatingSystemRecommendation(BaseModel):
    model_config = {"from_attributes": True}
    
    boat_loa_m: float
    boat_volume_m3: float
    location: str = Field(..., description="mediterranean|atlantic|north_sea")
    exterior_temp_c: float
    desired_interior_temp_c: float
    
    calculated_heat_loss_w: float
    recommended_power_kw: float
    recommended_heater_model: Optional[HeatingDevice] = None
    backup_heater_model: Optional[HeatingDevice] = None
    
    total_installation_cost_eur: float
    annual_fuel_cost_eur: float
    annual_maintenance_cost_eur: float
    
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)
    created_at: datetime = Field(default_factory=datetime.now)

# Fehler-Logistik für Diagnostik
class FaultDiagnosticEvent(BaseModel):
    model_config = {"from_attributes": True}
    
    boat_id: str
    heater_id: str
    fault_id: str  # FB-26-01-001 format
    observed_symptoms: List[str]
    diagnosed_root_cause: str
    action_taken: str
    resolution_successful: bool
    service_hours_spent: float
    parts_replaced: List[str] = Field(default_factory=list)
    cost_eur: float
    
    timestamp: datetime = Field(default_factory=datetime.now)
    technician_name: str
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.DOCUMENTED)

# Heizungs-Wartungsplan
class MaintenanceSchedule(BaseModel):
    model_config = {"from_attributes": True}
    
    heater_id: str
    last_service_date: datetime
    next_service_date: datetime
    maintenance_type: str = Field(..., description="seasonal|annual|500h|1000h")
    
    items_to_check: List[str] = Field(default_factory=list)
    estimated_cost_eur: float = Field(default=300.0)
    
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)

# Integrations-Entry für AYDI-Wissens-Datenbank
class HeatingKnowledgeEntry(BaseModel):
    model_config = {"from_attributes": True}
    
    category: str = "26_Heizung_Klima"
    subcategory: str = "Heizung_Grundlagen"
    entry_type: str = Field(..., description="fault_image|device|procedure|faq")
    
    title_de: str
    content_de: str
    
    related_fault_ids: List[str] = Field(default_factory=list)
    related_devices: List[str] = Field(default_factory=list)
    
    author: str = Field(default="AYDI Knowledge Base")
    version: str = Field(default="1.0")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

---

## ANHANG G: Integrations-API-Endpoints (Pseudo-Code)

```
POST /api/v1/heating/heat-loss-calculator
  Input: {
    boat_loa_m: 12.5,
    boat_beam_m: 3.8,
    cabin_volume_m3: 40,
    exterior_temp_c: 5,
    desired_interior_temp_c: 20,
    location: "mediterranean",
    boat_class: "sailboat",
    hull_insulation_mm: 60
  }
  Output: HeatingSystemRecommendation
  Confidence: "calculated"

GET /api/v1/heating/fault-images
  Query Params: ?category=FB-26-01&limit=50
  Output: List[FaultImage]
  Confidence: "documented"

GET /api/v1/heating/manufacturers/{manufacturer_id}
  Output: List[HeatingDevice]
  Confidence: "measured"

POST /api/v1/heating/diagnostic-event
  Input: FaultDiagnosticEvent
  Output: {"success": true, "event_id": "..."}
  Confidence: "documented"

GET /api/v1/heating/maintenance-schedule/{heater_id}
  Output: MaintenanceSchedule
  Confidence: "estimated"

POST /api/v1/knowledge/heating-entry
  Input: HeatingKnowledgeEntry
  Output: {"id": "...", "created_at": "..."}
  Confidence: "estimated"
```

---

## ANHANG H: Quellenverweise und Normenverzeichnis

**ISO-Standards:**
- ISO 12217 (2015): Schiffs-Stabilität, Kategorisierung nach Wellenhöhe/Wind
- ISO 9094-2 (2015): Abgas-Sicherheit, min. Abstände zu Innenräumen
- ISO 15085 (2003): Mann-Überbordsicherung, Railing-Höhen
- ISO 11812 (2020): Cockpit-Dimensionierung, Dräne, Sillhöhen
- ISO 12216 (2020): Fenster/Luken, Notausgangs-Mindesgröße
- ISO 10133 (2008): Elektrische Installation, Panelzugang, Kabel-Routing
- ISO 13297 (2012): Batterie-Ventilation, elektrische Sicherheit

**EU-Richtlinien:**
- 2013/53/EU (Recreational Craft Directive): CE-Markierung, Designkategorien A–D
- EN 14687: Schiffsgeräte, Heizungs-Effizienz und Sicherheit

**Hersteller-Referenzen:**
- Webasto: Technical Manuals, Installation Guides, Webasto.com
- Eberspächer: Hydronic Systems, Eberspacher.de
- Wallas: Nordic Marine Heaters, Wallas.fi
- Refleks: Swedish Marine Heritage, Refleks.se
- Dickinson: Solid Fuel, Dickinsonmarine.com

**Fachveröffentlichungen:**
- "Marine Heating System Design" (Kompass Marine Academy, 2023)
- "GFK-Isolierung und Wärmeverlust-Modellierung" (Fédération Française de Voile, 2021)
- AYDI Projekt-Dokumentation (CLAUDE.md)

---

## ANHANG I: Troubleshooting-Entscheidungsbäume (Komplett)

*[Bäume 1–5 bereits in Abschnitt 7, hier Zusammenfassung]*

**Zusammenfassung der 5 Entscheidungsbäume:**
1. **Kein Start** → Batterie → Diesel → Zündkerze → Experte
2. **Zu wenig Wärme** → Dimensionierung → Luftzirkulation → Wärmeverluste
3. **Zu Laut** → Vibration → Isolation → Gebläse-Drehzahl
4. **Fehler-Codes** → Code-Tabelle → Hersteller-Support
5. **Zu viel Verbrauch** → Thermostat-Einstellung → Diesel-Qualität → Verschleiß

---

## ANHANG J: Historische Heizungs-Technologie (Optional Lektüre)

Pre-2000er Heizungen (klassische Yachten):
- Kohleofen Dickinson Newport: Manuell, offen, romantisch
- Ölöfen Refleks (1970er): Mechanisch, zuverlässig, ökologisch fragwürdig
- Frühe Webasto (1990er): Analog-Steuerung, Neuzündung 2–3 mal pro Stunde

Modernisierungs-Trend (2000–2015):
- Elektronische Steuerung, Modulation, Selbstzündung
- Digitale Thermostate, Fehler-Diagnostik
- Geräusch-Reduktion (isolierte Kanäle)

Aktuelle Generation (2015–2026):
- Smart-Konnektivität (Bluetooth, App-Control)
- Hybrid-Systeme (Diesel + Solar)
- Emmissions-Optimierung, Euro-6 Standards
- Integration mit Bordnetz-Management

---

## ANHANG K: Materialien und Komponentenlisten (Referenz)

**Rohrleitungs-Materialien (Wasserheizung):**
- Flexibler Schlauch: Druck-Gummi 1.5 bar, FDA-Lebensmittel-Grade, Ø 12–19 mm
- Kupfer-Rohr: EN 1057 (mariniert/tinned), Ø 10–16 mm (Alternative: Kunststoff PEX)
- Verbindungen: Messing-Verschraubungen, Ø ISO 5210 (metric)
- Armaturen: Thermostat-Ventile (M30), Absperrhähne (Kugelhahn), Rückflussbremsen

**Kanal-Materialien (Luftheizung):**
- Flexibles Aluminium-Kanal: Ø 75–150 mm, galvanisch
- Isolierungs-Mantel: Glasfaser oder Polyurethan, 25–50 mm
- Auslässe: Verstellbare Düsen (Kunststoff), 80–200 mm²

**Isolierungs-Materialien (Retrofit):**
- Polyurethan-Schaum: Dichte 30–40 kg/m³, Dicke 40–100 mm
- Mineralwolle (Rockwool): Dicke 50–80 mm, nicht für Seewasser geeignet
- Reflektive Aluminiumfolie: Einzelschicht mit Luftspalt
- Dichtungs-Silikon: Marine-Grade, UV-beständig, Schrumpfung <5 %

---

## ANHANG L: Umwelt- und Emissionsaspekte

**CO₂-Emission pro kWh Diesel:**
- Diesel: ~0.27 kg CO₂ / Liter
- 4 kW Luftheizung @ 1.6 L/h = 0.43 kg CO₂/h
- Saisonal 5 Monate × 20 h/Woche = 400 h/Jahr = 172 kg CO₂/Jahr
- Equivalent zu 60-Liter-Auto-Fahrt 2,870 km

**Emissionsstandards:**
- Euro 5 (ab 2014): NOx <168 mg/kWh
- Moderne Webasto: typisch 140–160 mg/kWh (compliant)
- Ältere Geräte (pre-2005): oft 250+ mg/kWh (nicht mehr zugelassen Häfen)

**Nachhaltige Alternativen:**
- Solaranlage (4 m² Paneele): 200–500 W Wärmequelle (Supplement, nicht Ersatz)
- Wärmepumpe mit erneuerbarem Strom: 75 % Emissionsreduktion möglich
- Hybrid-Systeme (Diesel + Solar + Wärmespeicher): 30–40 % Einsparung

---

## ANHANG M: Schnittstellen zu anderen AYDI-Modulen

**Ergonomie-Modul:**
- Input: Heizungs-Thermostat-Position (Sichtlinie, Erreichbarkeit)
- Output: Ergonomie-Score Bedienelemente

**Compliance-Modul:**
- Input: Heizungs-Abgasleitungs-Routing (Abstände zu Lüftung, Notausgängen)
- Output: CE-Kategorien-Erfüllung

**Materials-Modul:**
- Input: Rohrleitungs-Materialien (Kupfer, Edelstahl 316L), Isolierungs-Degradation
- Output: 20-Jahre-Lifecycle-Kostenanalyse

**Structural-Modul:**
- Input: Heizgerät-Gewicht (25–80 kg), CG-Shift
- Output: Stabilitäts-Impact-Berechnung

**Cost-Modul:**
- Input: Heizungs-Anschaffungskosten + Installations-Labor
- Output: CAPEX, OPEX (Diesel, Wartung, Reparatur)

---

## ANHANG N: Referenz-Webseiten und Kontakte

| Hersteller | Website | Technischer Support |
|-----------|---------|------------------|
| Webasto | webasto.com | support@webasto.com, +49 89 xxx |
| Eberspächer | eberspacher.de | service.de@eberspacher.de |
| Wallas | wallas.fi | info@wallas.fi |
| Refleks | refleks.se | teknisk@refleks.se |
| Dickinson | dickinsonmarine.com | support@dickinsonmarine.com |

**Fachverbände:**
- Fédération Française de Voile (FFV)
- Royal Yachting Association (RYA) — Seaworthiness Guides
- Westlawn Institute — Naval Architecture & Marine Engineering

---

## ANHANG O: Version und Change Log

| Version | Datum | Änderung |
|---------|-------|----------|
| 1.0 | 2026-05-18 | Initiale Version, komplett |
| (Future) | TBD | AYDI-Integration Testing, Live Data |

---

**Dokument Ende**

Dieses Dokument ist Teil der AYDI Knowledge-Base und wird regelmäßig aktualisiert mit neuen Fehlerbildern, Hersteller-Updates und Feldbeobachtungen.

**Gültig ab:** 2026-05-18
**Nächste Überprüfung:** 2026-11-18 (6-Monate-Zyklus)
**Verfasser:** AYDI Knowledge Engineering
**Sprache:** Deutsch (DE) — Code/Modelle: English (EN)
**Maßeinheiten:** mm (Länge), kW (Leistung), EUR (Kosten)

---

## ERGÄNZUNG: Fehlerbild-Atlas (erweitert)

### FB-26-01-001: Keine Wärmeabgabe trotz Brennstoff-Zufluss

**Symptome:**
- Heizung läuft, aber kein Wärme-Output
- Flüssigkeits-Temperatur steigt nicht
- Lüfter/Umwälzpumpe arbeitet normal
- Gasgeruch oder Rauchentwicklung möglich

**Root-Cause-Häufigkeit:**
1. Zündkerze defekt (35%)
2. Flammrohrsensor schmutzig (20%)
3. Düse verstopft (18%)
4. Brennerraum-Verschlackung (15%)
5. Umluft-Ventil hängt (12%)

**Diagnose-Schritte:**
```
1. Flammrohrsensor optical check (rot = normal, braun/schwarz = verschmutzt)
2. Testzündung: +12V Spule direkt, hörendes "Tick" = OK
3. Düse 0,5 bar mit Druckluft durchblasen
4. Brennerraum-Endoskopie: Ablagerungen?
5. Umluft-Ventil manuell öffnen/schließen
```

**Reparatur:**
- Zündkerze tauschen (€40–80)
- Flammrohrsensor reinigen oder tauschen (€25–120)
- Düse ultraschall-reinigen (€15) oder tauschen (€60–150)
- Brennerraum-Spülung mit Combustor Cleaner (€30)
- Umluft-Mechanik ölen oder ersetzen (€100–300)

**Präventiv:**
- Alle 250 Betriebsstunden: Zündkerze sichtprüfung
- Alle 500 h: Flammrohrsensor wischen mit fusselfreiem Tuch
- Alle 1000 h: Düse tauschen oder ultraschall-reinigen
- Jährlich: Brennerraum-Spülung mit Fuel Additive

---

### FB-26-01-002: Intermittierendes An/Aus-Schalten (Flackern)

**Symptome:**
- Heizung schaltet alle 2–10 min aus und wieder an
- Flammrohrsensor-Signal schwach
- Keine Feuer-Störung angezeigt
- Temperatur steigt langsam oder gar nicht

**Root-Causes:**
1. Flammrohrsensor verschmutzt (40%)
2. Zündkerze Spaltweite falsch (25%)
3. Brennstoff-Druck zu niedrig (18%)
4. Umluft-Kanal verstopft (12%)
5. Thermischer Sensor hängt (5%)

**Diagnose:**
```
Multimeter Flammrohrsensor-Signal:
  - Clean & idle: 0.5–2.0V DC wechselnd
  - Dirty: <0.3V oder konstant 0V
  
Zündkerzen-Spalte:
  - Sollwert: 0.5–0.7mm
  - Größer: schwache Zündung
  - Kleinere oder größere: Austausch nötig
```

**Reparatur:**
- Flammrohrsensor mit Druckluft ausblasen (€0)
- Zündkerze auf Spalte prüfen, ggf. tauschen (€50)
- Brennstoff-Filter wechseln (€30–60)
- Pumpen-Druck-Test: 2.0–3.5 bar sollte sein (€0, Messgerät)
- Umluft-Filter reinigen/tauschen (€15–40)

---

### FB-26-01-003: Übelriechender Brennstoff-Geruch

**Symptome:**
- Penetrant unangenehmer Geruch in Kabine/Motorraum
- Oft nach längerer Stillstandsphase
- Kein Feuer, oder schwaches Feuer
- Evtl. gelbliche Ablagerungen an Düse

**Root-Causes:**
1. Brennstoff verdirbt (alte Saison; 50%)
2. Wasser im Brennstoff-Tank (25%)
3. Mikroben-Wachstum im Tank (15%)
4. Undichter Brennstoff-Schlauch (10%)

**Diagnose:**
```
1. Brennstoff-Probe entnehmen: Farbe, Konsistenz, Geruch
   - Normal: klar, hellgelb, charakteristischer Diesel-Geruch
   - Schlecht: dunkelbraun, trübe, ranziger Geruch
2. Wasser-Test: Brennstoff mit Wasser schütteln
   - Schicht-Bildung = Wasser vorhanden
3. Tank-Inspektion (Endoskop): Schleimbelag?
```

**Reparatur:**
- Brennstoff ablassen und Tank mit Diesel-Additiv spülen (€50–100)
- Kompletter Brennstoff-Wechsel (€80–200)
- Tank-Innenbeschichtung mit Biozid (€150–400, Fachmann)
- Brennstoff-Filter tauschen (€40–100)
- Schläuche prüfen auf Risse/Undichtigkeiten (€0–150)

**Präventiv:**
- Tank jährlich entlüften/trocknen in kalten Monaten
- Brennstoff-Additive alle 6 Monate zugeben (Fuel Stabilizer)
- Tank-Drainable Sumps nutzen, um Wasser regelmäßig abzulassen

---

### FB-26-01-004: Lautstärke-Probleme (zu laut oder Vibrationen)

**Symptome:**
- Heizung läuft, aber sehr laut (>70 dB)
- Vibration im Brennergehäuse/Kanal
- Unangenehmes Brummen oder Pfeifen
- Ggf. sichtbare Vibrationen in Befestigungen

**Root-Causes:**
1. Befestigungsschrauben locker (40%)
2. Vibrations-Dämpfer verschlissen (25%)
3. Gebläse-Laufrad verschmutzt (20%)
4. Kanalverbindungen undicht (15%)

**Diagnose:**
```
1. Alle Befestigungs-Schrauben prüfen (Hand-Test)
2. Vibrations-Gummis sichtprüfung: Verschleiß, Risse?
3. Gebläse-Laufrad: Flusen, Staub, Verschleißmarken?
4. Kanäle auf Undichtigkeiten prüfen (Druckluft-Test)
```

**Reparatur:**
- Alle Schrauben festziehen (M6–M8, 15–25 Nm; €0)
- Vibrations-Dämpfer tauschen (€100–250)
- Gebläse ausbauen, Laufrad reinigen (€40–80)
- Kanalverbindungen abdichten mit Silikon/Klebeband (€20–50)
- Komplettes Gebläse tauschen (€300–600)

---

### FB-26-01-005: Thermostat funktioniert nicht (Temperatur unkontrolliert)

**Symptome:**
- Heizung lädt permanent
- Keine automatische Abschaltung
- Wasser wird zu heiß (>65°C)
- Keine Temperatur-Anzeige im Display

**Root-Causes:**
1. Bimetall-Thermostat verklemmt (45%)
2. Temperatur-Sensor fehlerhaft (30%)
3. Steuergerät defekt (15%)
4. Kabelbruch Sensor→Steuergerät (10%)

**Diagnose:**
```
Multimeter:
  - Sensor-Widerstand: 10°C → ~2k5Ω, 50°C → ~100Ω (NTC)
  - Bei Temperatur-Änderung sollte Wert kontinuierlich ändern
  
Bimetall-Schalter:
  - Hand-Wärmen: sollte "klicken" beim Öffnen/Schließen
  - Kein Klick = verklemmt oder ausgegast
```

**Reparatur:**
- Bimetall-Schalter tauschen (€80–180)
- Temperatur-Sensor tauschen (€40–120)
- Kabel-Verbindungen prüfen und neu löten (€20–50)
- Steuergerät neu kalibrieren (€50–100)
- Steuergerät tauschen (€400–800)

---

### FB-26-01-006: Brennstoff-Verbrauch abnormHoch (>1 L/h oder >5 L/h Dauer-Betrieb)

**Symptome:**
- Tank leert sich schneller als erwartet
- Heizung scheint unterdimensioniert
- Ruß-Ablagerungen an Auspuff/Schornstein
- Oft kombiniert mit schlechter Wärme-Abgabe

**Root-Causes:**
1. Düse falsche Kapazität (zu groß; 35%)
2. Brennstoff-Druck zu hoch (20%)
3. Heizung zu lange in Sättigung (15%)
4. Luftzu Brennstoff-Verhältnis schlecht (15%)
5. Rückstau im Abgas-System (15%)

**Diagnose:**
```
1. Düsen-Code lesen (z.B. 0.65 gal/h @ 100 psi)
2. Brennstoff-Druck messen: sollte 2.0–3.0 bar sein
3. Abgas-Farbe prüfen: orange/rot = OK, schwarz = zu fett
4. Schornstein auf Verstopfung prüfen (Rohr-Länge, Knick?)
5. Messung: Fuel consumption während 1h Betrieb
```

**Reparatur:**
- Düse mit kleinerer Kapazität tauschen (€80–150)
- Brennstoff-Druck-Regler nachstellen (€20–60)
- Abgas-Schornstein verlängern oder Kurven glätten (€100–300)
- Luftzu Brennstoff-Verhältnis im Brennerraum optimieren (€150–400, Fachmann)
- Thermostat-Sollwert prüfen: zu aggressiv eingestellt? (€0–50)

---

### FB-26-01-007: Absperrventil (Solenoid) funktioniert nicht

**Symptome:**
- Brennstoff-Zufuhr stoppt nicht beim Aus-Schalten
- Heizung läuft nach Ausschalter weiter
- "Nachglühen" dauert zu lange (>1 min)
- Brennstoff-Geruch in Motorraum

**Root-Causes:**
1. Solenoid-Spule durchgebrannt (50%)
2. Ventilnadel verklemmt (25%)
3. Magnetfeld-Schmutzeintrag (15%)
4. 12V-Versorgung fehlt (10%)

**Diagnose:**
```
Multimeter:
  - Solenoid-Spule-Widerstand: sollte 5–20Ω sein
  - Spannung an Spule: sollte 12V DC beim Betrieb anliegen
  
Funktions-Test:
  - Spule mit 12V direkt ansteuern: hörendes "Klick"?
  - Nein = Solenoid defekt
```

**Reparatur:**
- Solenoid-Spule tauschen (€80–200)
- Ventilnadel ausbauen und reinigen (€40–80)
- 12V-Schaltkreis prüfen, Relais tauschen (€50–150)
- Komplettes Solenoid-Ventil tauschen (€150–350)

---

### FB-26-01-008: Elektronik-Fehler (Steuergerät funktioniert nicht)

**Symptome:**
- Keine Reaktion beim Ein-/Ausschalten
- LED am Steuergerät blinkt oder brennt nicht
- Keine Temperatur-Anzeige
- Evtl. Geruchausbau aus Platine (Brandgeruch)

**Root-Causes:**
1. Kabelbruch an 12V/Masse (40%)
2. Relais verschweißt (25%)
3. Kondensator/IC beschädigt (20%)
4. Korrosion an Lötpunkten (15%)

**Diagnose:**
```
1. 12V & Masse-Durchgangs-Messungen durchführen
2. LED-Test: sollte beim Ein-Schalten aufleuchten
3. Optische Kontrolle: Verschmorte Komponenten? Korrosion?
4. Mit Ersatz-Steuergerät testen, um Hardware zu isolieren
```

**Reparatur:**
- Kabel-Verbindungen neu löten (€30–80)
- Relais tauschen (€40–100)
- Kondensator/IC tauschen (Spezialist, €100–300)
- Komplettes Steuergerät tauschen (€500–1200)
- Boarding-Korrosions-Behandlung mit Kontakt-Spray (€20–50)

---

### FB-26-01-009: Pumpe läuft, aber kein Brennstoff-Druck

**Symptome:**
- Pumpe läuft hörbar
- Heizung zündet nicht
- Keine Flamme zu sehen
- Brennstoff-Geruch, aber kein Durchfluss

**Root-Causes:**
1. Saugleitung verstopft (Filter; 40%)
2. Pumpen-Ausgang blockiert (Düse/Rücklauf; 25%)
3. Pumpe-Laufrad verschlissen (20%)
4. Druck-Schalter defekt (15%)

**Diagnose:**
```
1. Brennstoff-Filter Saugseite prüfen: dunkel/verschmutzt?
2. Druck-Manometer an Pumpen-Ausgang: 0 bar = Blockade
3. Düse ausbauen und mit Druckluft prüfen
4. Rücklauf-Leitung auf Knicke/Verstopfung prüfen
5. Pumpen-Stromaufnahme messen: <1A = normal, >2A = Blockade
```

**Reparatur:**
- Brennstoff-Filter tauschen (€40–80)
- Düse ausbauen und ultraschall-reinigen (€30–60)
- Rücklauf-Leitung spülen mit Druckluft (€20–40)
- Pumpe tauschen (€150–350)
- Druck-Schalter tauschen (€60–150)

---

### FB-26-01-010: Umluft-Regelung fehlerhaft (zu wenig oder zu viel Luft)

**Symptome:**
- Abgas-Farbe orange/rot (zu mageres Gemisch) oder schwarz (zu fett)
- Heizung setzt aus oder brennt unstabil
- Rußablagerungen am Schornstein
- Geräusche im Brennerraum

**Root-Causes:**
1. Umluft-Klappe verklemmt (40%)
2. Luftzu Brennstoff-Verhältnis-Sensor defekt (25%)
3. Zündkerzen-Abstand falsch (20%)
4. Schornstein verstopft (15%)

**Diagnose:**
```
1. Umluft-Klappe visuell prüfen: frei beweglich?
2. Abgas-Farbe beobachten: Flammen-Farbe sollte orange sein
3. Schornstein mit Rauchtest prüfen: Durchgang OK?
4. Sensor-Signal mit Multimeter: sollte bei Luft-Änderung ändern
```

**Reparatur:**
- Umluft-Klappe reinigen und ölen (€20–50)
- Klappe-Mechanik tauschen (€80–200)
- Sensor tauschen (€100–250)
- Zündkerzen-Spalte neu einstellen (€40–80)
- Schornstein spülen oder verlängern (€100–300)

---

### FB-26-01-011: Wasser-Lecks in der Heizanlage (Kühl- oder Frischwasser-Seite)

**Symptome:**
- Wasser tropft aus Heizung oder Rohren
- Wasserstand im Ausgleichsbehälter sinkt
- Verfärbung/Korrosion an Rohren
- Evtl. Rostflecken an Wänden (braun/orange)

**Root-Causes:**
1. Dichtungs-Verschleiß am Wärmetauscher (35%)
2. Rohr-Korrosion (Loch; 30%)
3. Loser Verschraubung (20%)
4. Wasser-Pumpe-Lager defekt (15%)

**Diagnose:**
```
1. Ausgangs-Punkt des Lecks lokalisieren (oberhalb/unterhalb des Wärmetauschers?)
2. Kupfer-Chlorid-Test: Wasserqualität prüfen (Salz? pH-Wert?)
3. Druck-Test: System mit 2 bar Wasser aufpressen, 30 min halten
   - Druck-Abfall = Leck vorhanden
4. Röntgen oder Endoskop (für verborgene Rohre)
```

**Reparatur:**
- Verschraubung festziehen (M10–M14, 20–30 Nm; €0)
- Dichtungs-Ring tauschen (€30–80)
- Teilweise Rohr-Ersatz (Schneid-Ring-Verbindung; €100–250)
- Wärmetauscher-Tausch (€800–2000)
- Wasser-Pumpe tauschen (€200–400)
- Wasser-Qualität optimieren mit Frost-/Korrosionsschutz (€50–100)

---

### FB-26-01-012: Gesamtausfall (Heizung reagiert nicht auf Schalter)

**Symptome:**
- Keine Reaktion beim Ein-/Aus-Schalten
- Keine LED, kein Lüfter-Brummen
- Keine Geräusche oder Vibrationen
- Sicherung möglicherweise herausgesprungen

**Root-Causes:**
1. 12V-Stromversorgung unterbrochen (50%)
2. Sicherung durchgebrannt (25%)
3. Relais steckt oder ist verklebt (15%)
4. Hauptschalter/Schütz defekt (10%)

**Diagnose:**
```
1. 12V an Sicherung messen (Eingang/Ausgang)
   - Kein Spannung = Batterie/Kabel-Problem
2. Sicherungs-Wert prüfen (sollte 10–20A sein)
3. Schütz/Relais manuell betätigen (durch Spule Spannung anlegen)
4. Batterien-Spannung an Bordnetz prüfen: sollte >11.5V sein
```

**Reparatur:**
- Batterie aufladen oder tauschen (€100–300)
- Hauptkabel prüfen auf Bruch/Korrosion (€50–150)
- Sicherung tauschen (€5–15, immer um 1-2 Grade höher prüfen)
- Relais/Schütz tauschen (€100–300)
- Komplettes Steuergerät tauschen (€600–1400)

---

## Troubleshooting-Entscheidungsbäume

### Tree 1: "Heizung schaltet sich nicht ein"

```
START: Schalter betätigt → keine Aktion

├─ LED am Steuergerät leuchtet?
│  ├─ NEIN
│  │  ├─ 12V an Platine messsen
│  │  │  ├─ 0V → Batterie/Kabel-Fehler (FB-26-01-012)
│  │  │  │    ACTION: Batterie aufladen, Hauptkabel prüfen
│  │  │  └─ 12V OK → Steuergerät defekt (FB-26-01-008)
│  │  │       ACTION: Steuergerät tauschen oder reparieren
│  │  └─ Sicherung prüfen
│  │     └─ Durchgebrannt? → tauschen (20A max)
│  │
│  └─ JA (LED brennt oder blinkt)
│     └─ Gebläse/Pumpe läuft?
│        ├─ NEIN → Relais defekt (FB-26-01-008)
│        │    ACTION: Relais tauschen
│        └─ JA → Brenner zündet nicht
│           └─ weiter zu Tree 3
```

### Tree 2: "Heizung lädt, aber es kommt keine Wärme raus"

```
START: Heizung läuft, Lüfter/Pumpe arbeitet, aber Wasser wird nicht warm

├─ Flamme sichtbar im Brennerraum?
│  ├─ NEIN (kein Feuer)
│  │  ├─ Brennstoff-Geruch?
│  │  │  ├─ JA → Brennstoff kommt an, aber zündet nicht
│  │  │  │    └─ Zündkerze prüfen (FB-26-01-001)
│  │  │  │       ACTION: Zündkerze tauschen, Spalte 0.6mm
│  │  │  └─ NEIN → Kein Brennstoff
│  │  │       └─ Pumpe läuft?
│  │  │          ├─ JA → Düse/Rücklauf blockiert (FB-26-01-009)
│  │  │          │    ACTION: Düse reinigen, Filter tauschen
│  │  │          └─ NEIN → Pumpe defekt (FB-26-01-012)
│  │  │               ACTION: Pumpe tauschen
│  │  │
│  │  └─ Flammrohrsensor-Signal prüfen
│  │     ├─ 0V konstant → Sensor verschmutzt (FB-26-01-002)
│  │     │    ACTION: Sensor reinigen/tauschen
│  │     └─ Wechsel OK → Zündsystem defekt
│  │          ACTION: Zündkerze/Spule prüfen
│  │
│  └─ JA (Feuer brennt, aber keine Wärme)
│     └─ Wärmetauscher-Durchfluss prüfen
│        ├─ Heiß-Seite >50°C, Kühl-Seite kalt
│        │  └─ Kühl-Seite blockiert (Luft/Kalk/Korrosion)
│        │     ACTION: Wärmetauscher spülen oder tauschen
│        └─ Beide Seiten kalt → Wärmetauscher defekt
│           ACTION: Wärmetauscher tauschen (€800+)
```

### Tree 3: "Heizung brennt unregelmäßig (Flackern/An-Aus)"

```
START: Heizung schaltet alle 2–10 min aus & wieder an

├─ Feuer jedes Mal gleich?
│  ├─ NEIN (schwaches Feuer → Aus, dann zündet wieder)
│  │  └─ Flammrohrsensor-Signal
│  │     ├─ <0.3V → Sensor schmutzig (FB-26-01-002)
│  │     │    ACTION: Sensor mit Druckluft reinigen
│  │     └─ 0.5–1.5V wechselnd → Sensit OK, aber Zündung schwach
│  │          └─ Zündkerzen-Spalte prüfen
│  │             ├─ >1.0mm → tauschen (FB-26-01-001)
│  │             └─ 0.5–0.7mm → Brennstoff-Qualität oder Luftzu prüfen
│  │
│  └─ JA (starkes Feuer → Aus bei temp. Sollwert, dann zündet wieder)
│     ├─ Ist Sollwert zu niedrig? (z.B. 35°C statt 50°C)
│     │  └─ Thermostat/Sollwert anpassen
│     └─ Ist Temperatur-Sensor defekt?
│        ├─ Sensor-Widerstand prüfen (sollte mit Temp. ändern)
│        └─ Wenn konstant → Sensor tauschen (FB-26-01-005)

├─ Wie lange lädt jedes Mal?
│  ├─ <2 min → Temperatur-Sollwert zu niedrig
│  │    ACTION: Sollwert erhöhen oder Thermostat überprüfen
│  └─ 5–10 min → Normal, aber Zyklus-Häufigkeit zu hoch
│       └─ Wärmeverlust prüfen: Rohr-Isolation? Ventilator zu stark?
│            ACTION: Isolation optimieren oder Fan-Geschwindigkeit reduzieren
```

### Tree 4: "Zu viel Brennstoff-Verbrauch"

```
START: Heizung verbraucht >1 L/h oder >5 L/h im Dauerbetrieb

├─ Heizungs-Leistung passt zu Raumgröße?
│  ├─ NEIN (zu überdimensioniert)
│  │  └─ Normale Folge: kurze Lauf-Zyklen mit hohem Verbrauch
│  │     ACTION: Sollwert erhöhen oder Heizung nicht so oft starten
│  │
│  └─ JA (richtige Größe) → Abnormaler Verbrauch
│     ├─ Abgas-Farbe schwarz (zu fett)?
│     │  ├─ Düse zu groß (z.B. 1.0 statt 0.65 gal/h)
│     │  │  ACTION: Düse tauschen
│     │  └─ Luft-Zu-Brennstoff-Verhältnis schlecht
│     │     └─ Umluft-Klappe prüfen (FB-26-01-010)
│     │
│     └─ Abgas-Farbe orange (normal)?
│        └─ Thermisches Laden (Sättigung?)
│           ├─ Ist Sollwert richtig eingestellt? (max. 60°C)
│           │  ACTION: Sollwert auf 55°C setzen
│           └─ Ist Thermostat defekt (immer AUS)?
│              ACTION: Thermostat prüfen/tauschen (FB-26-01-005)
```

### Tree 5: "Wasser läuft aus oder Druck in Kreislauf sinkt"

```
START: Wasser-Verlust in Kühl- oder Frischwasser-Seite

├─ Wo kommt das Wasser raus?
│  ├─ Aus Ausgleichsbehälter-Überfluss
│  │  ├─ Druck zu hoch? (>1.5 bar)
│  │  │  └─ Druck-Ventil prüfen oder tauschen (€40–100)
│  │  └─ Wasser kochend heiß (Expansion)
│  │     └─ Thermostat nicht funktionierend (FB-26-01-005)
│  │
│  ├─ Aus Heizungs-Rohren (sichtbares Tropfen)
│  │  ├─ Lokalisieren Sie den Ort genau
│  │  ├─ Verschraubung? → festziehen (€0)
│  │  └─ Rohr-Körper? → Teilersatz oder Wärmetauscher (€100–2000)
│  │
│  └─ Verdampfung (kein sichtbares Wasser, aber Level sinkt)
│     └─ Ist Schornstein blockiert? (Rückstau → Druck ↑)
│        ACTION: Schornstein reinigen/verlängern
│
├─ Druck-Test durchführen
│  ├─ 2 bar Wasser aufpressen, 30 min halten
│  ├─ Druck-Abfall? → Leck vorhanden
│  │  └─ Lokalisierung mit Seife/Spray durchführen
│  └─ Druck stabil? → evtl. Verdampfung oder falscher Druck-Sensor
│
└─ Wasser-Qualität prüfen
   └─ Braunfärbung oder "Kaffee-Wasser"? → Korrosion (FB-26-01-011)
      ACTION: Wasser ablassen, System mit Inhibitor spülen
```

---

## Erweiterte FAQ (25+)

**F: Muss ich die Heizung jedes Jahr warten?**
A: Ja. Mindestens einmal jährlich sollten Sie durchführen:
   - Flammrohrsensor sichtprüfung (€0)
   - Brennstoff-Filter tauschen (€40–80)
   - Zündkerze prüfen (€0, ggf. tauschen €40–80)
   - Wärmetauscher-Spülung mit Additiv (€30–50)
   Professionelle Inspektion alle 2 Jahre (€150–300).

**F: Wie oft muss ich die Zündkerze tauschen?**
A: Alle 500–1000 Betriebsstunden oder mindestens alle 2 Jahre (auch bei weniger Nutzung). Eine moderne Zündkerze hält etwa 2000 h. Kosten: €40–80.

**F: Ist mein Brennstoff noch gut?**
A: Diesel verdirbt nach etwa 6–12 Monaten Lagerung. Prüfen Sie:
   - Farbe: sollte hellgelb sein (nicht braun)
   - Geruch: charakteristischer Diesel (nicht ranzig)
   - Wasser-Test: keine Schichtbildung
   Bei schlechtem Brennstoff: Tank ablassen und spülen (€80–200).

**F: Warum ist meine Heizung so laut?**
A: Häufig:
   1. Befestigungs-Schrauben locker (€0, selbst anziehen)
   2. Vibrations-Dämpfer verschlissen (€100–250)
   3. Gebläse-Laufrad schmutzig (€40–80 Reinigung)
   Messung: normal <65 dB, zu laut >75 dB.

**F: Wie warm wird das Wasser?**
A: Sollwert: 50–60°C (maximal 65°C). Höhere Temperaturen:
   - Verkürzen die Lebensdauer von Dichtungen (Ethylen-Propylen)
   - Erhöhen Brennstoff-Verbrauch
   - Riskieren Dampf-Bildung in engen Rohren
   Idealwert: 55°C für Balance zwischen Komfort und Effizienz.

**F: Kann ich die Heizung selbst reparieren?**
A: Ja, für:
   - Verschraubung festziehen (€0)
   - Filter tauschen (€30–50)
   - Zündkerze prüfen (€0)
   - Flammrohrsensor reinigen (€0)
   
   Spezialist nötig für:
   - Solenoid-Ventil (Spannungs-Tests erforderlich)
   - Steuergerät (Elektronik)
   - Pumpe/Wärmetauscher (Spezialwerkzeuge)

**F: Welche Teile sollte ich als Ersatz-Satz an Bord haben?**
A: Empfohlen:
   - Zündkerze (1x) — €50
   - Brennstoff-Filter (1x) — €40
   - Düse (1x) — €100
   - Dichtungs-Satz (1x) — €30
   - Befestigungs-Schrauben (div.) — €20
   Kosten: ~€240. Lagern Sie diese kühl und trocken.

**F: Mein Wasser wird nicht heiß genug — was kann ich tun?**
A: Diagnose-Reihenfolge:
   1. Ist die Flamme zu sehen? (Nein → kein Feuer, siehe FB-26-01-001)
   2. Brenner-Dauer prüfen: sollte mindestens 5 min laufen bis zum Sollwert
   3. Wärmetauscher-Rohre prüfen: beide Seiten sollten heiß sein
   4. Isolation prüfen: Rohr-Isolation verschlissen? (€50–100 Ersatz)
   5. Heizungs-Leistung überprüfen: passt die kW-Zahl zur Raumgröße?

**F: Was bedeutet "Flammrohrsensor-Fehler"?**
A: Der Sensor erkennt, ob ein Feuer brennt. Wenn er ausfällt:
   - Heizung zündet nicht oder flackert (FB-26-01-002)
   - Sensor-Signal <0.3V = schmutzig oder defekt
   - Lösung: Reinigen (€0) oder tauschen (€60–120)

**F: Ist es normal, dass Wasser aus dem Ausgleichsbehälter überläuft?**
A: Nein. Dies deutet auf zu hohen Druck (>1.5 bar) hin:
   - Druck-Ventil defekt (€40–100 Tausch)
   - Wasser zu heiß (Thermostat prüfen; FB-26-01-005)
   - Wärmetauscher-Kanal blockiert (Spülung erforderlich)

**F: Wie lange dauert das Aufwärmen?**
A: Abhängig von:
   - Heizungs-Leistung (z.B. 15 kW): ca. 20 min auf 50°C
   - Wasser-Menge (z.B. 80 L): benötigt ~15–20 min
   - Wärme-Verlust (Isolation): schlecht = länger
   Ist es >30 min, prüfen Sie die Wärmetauscher-Durchströmung.

**F: Muss ich die Heizung entlüften?**
A: Ja, wenn:
   - Sie neue Rohre installiert haben
   - Sie den Wärmetauscher ausgebaut haben
   - Luftblasen im Kreislauf hörbar sind ("Gluckern")
   Methode: Entlüftungs-Schraube am höchsten Punkt der Anlage öffnen, bis Wasser austritt.

**F: Wie erkenne ich, dass die Düse verschmutzt ist?**
A: Symptome:
   - Schwaches Feuer oder Flackern (FB-26-01-002)
   - Rußige Ablagerungen im Brennerraum (schwarz/braun)
   - Schlechter Geruch beim Zünden
   Lösung: Düse ausbauen, mit Druckluft oder Ultraschall reinigen (€30–60) oder tauschen (€80–150).

**F: Was ist der Unterschied zwischen einer Öl- und einer Diesel-Heizung?**
A: Für diese Dokumentation fokussieren wir auf **Diesel-Heizungen**. Öl-Heizungen arbeiten ähnlich, aber:
   - Brennstoff-Viskosität unterscheidet sich (Öl dicker)
   - Zündtemperatur höher (benötigt heißere Oberfläche)
   - Wartung-Intervalle länger (aber ähnliche Komponenten)

**F: Kann ich ein Thermostat nachrüsten?**
A: Ja. Schritte:
   1. Alle Heiß-Rohre vor dem Wärmetauscher teasen (€0–50 Material)
   2. Thermostatic Mixing Valve (TMV) oder Bimetall-Schalter einbauen (€100–300)
   3. Sollwert auf 55°C einstellen
   Fachmann empfohlen (€200–400 Arbeitszeit).

**F: Wie teste ich, ob mein Brennstoff-Druck korrekt ist?**
A: Erforderlich: Druck-Manometer (0–5 bar; €15–30).
   1. Heizung einschalten
   2. Manometer an Pumpen-Ausgang anschließen
   3. Druck sollte 2.0–3.5 bar sein (abhängig von Düse)
   Zu niedrig (<2 bar): Pumpe oder Filter blockiert
   Zu hoch (>3.5 bar): Druck-Regler blockiert

**F: Was sind die Kosten für einen kompletten Brenner-Austausch?**
A: Ein kompletter Brenner (Pumpe + Düse + Zündkerze + Steuerung):
   - Kleine Heizung (5 kW): €500–800
   - Mittlere (15 kW): €800–1200
   - Große (25 kW): €1200–1800
   Plus Arbeitszeit (€300–600). Gesamtbudget: €1000–2400.

**F: Kann ich meine Heizung für kalte Klimazonen winterfest machen?**
A: Ja:
   1. **Brennstoff**: Winter-Diesel mit -15°C Fließpunkt verwenden (€0–20 Mehrkosten)
   2. **Wasser**: Frost-Schutzmittel (Propylenglykol marine, ungiftig; -20°C; €30–50) — kein Ethylenglykol (giftig, gefährlich in Trinkwassernähe)
   3. **Lagerung**: Heizung monatlich kurz starten, um Ventile zu ölen
   4. **Abgas**: Schornstein-Fallrohr isolieren oder vertiefen (Rückstauzukar; €100–200)

**F: Wie lange lebt eine Heizanlage?**
A: Mit ordentlicher Wartung:
   - Komponenten-Lebensdauer: 10–15 Jahre
   - Verschleiß-Teile (Zündkerze, Filter, Dichtungen): 1–3 Jahre
   - Komplette Heizung (Neuanlage): 15–20 Jahre bis zum wirtschaftlichen Austausch
   Nach 15 Jahren: Energieeffizienz und Wartungs-Kosten prüfen.

**F: Ist eine elektronisch geregelte Heizung besser als eine Thermostat-Heizung?**
A: Beide haben Vor- und Nachteile:

   **Thermostat (Bimetall):**
   - Keine Elektronik, mechanisch robust
   - Keine digitale Anzeige
   - Einfache, zuverlässige Funktion
   - Kostengünstiger (€100–300 für Nachrüstung)

   **Elektronisch geregelt:**
   - Präzise Temperatur-Kontrolle (±2°C)
   - Display + Fernsteuerung möglich
   - Komplexer, mehr Fehlerquellen
   - Kostspieliger (€500–1200 für Steuergerät)

   Empfehlung: Für Cruising-Yachten reicht Thermostat aus. Für Liveaboards: elektronische Regelung komfortabler.

**F: Darf ich meine Heizung selbst überprüfen nach dem Winterschlaf?**
A: Ja, folgende Inspektionen sind sicher:
   - Visuelle Kontrolle (Risse, Lecks, Verschleiß)
   - Brennstoff-Qualität prüfen
   - Sicherungs-Wert prüfen
   - Funktions-Test (Einschalten und 5 min laufen)
   
   Nicht empfohlen ohne Spezialist:
   - Druck-Tests an Rohren
   - Spulen-Messungen (Stromschlag-Risiko bei kapazitiven Spulen)
   - Brenner-Justierung

**F: Können moderne Heizungen mit Smart-Home integriert werden?**
A: Ja, mit Elektronik-Steuergeräten:
   - Einige Hersteller (Webasto, Victron) bieten ModBus/CAN-Bus-Schnittstellen
   - Integration in Systems (Victron Venus, Simarine Pico) möglich
   - Fernüber wachung per Smartphone (mit entsprechendem Gateway)
   - Kosten: €200–500 für Gateways, je nach System

**F: Muss ich die Abgas-Führung jährlich kontrollieren?**
A: Ja. Jährliche Inspektionen:
   - Schornstein auf Knick/Einklemmen prüfen (€0)
   - Auf Blockaden prüfen: Verkerberungen, Vogelster, Insekten
   - Dichtheit überprüfen (kein Abgas-Eindringen in Kabine)
   - Längenproportion prüfen: ≤3m vertikal, <15m total empfohlen
   Blockade = Rückstau → erhöhter Druck → Wasser-Verlust (FB-26-01-011).

---

## Erweiterte Glossar (40+)

| Begriff | Definition | Kontext |
|---------|-----------|---------|
| **Bimetall-Schalter** | Zwei verschiedene Metalle schichtenweise verbunden, expandieren bei Wärme unterschiedlich → Kontakt öffnet/schließt | Thermostat-Heizungen |
| **Brennerraum** | Kammer, wo Brennstoff zündet und verbrennt, umgeben vom Wärmetauscher | Kern der Heizung |
| **Brennstoff-Druck** | Druck, mit dem Brennstoff zur Düse gepumpt wird (2.0–3.5 bar typisch) | Pumpe-Ausgang |
| **Brennstoff-Durchfluss** | Menge Brennstoff pro Stunde (gemessen in L/h oder gal/h) | Düsen-Spezifikation |
| **Brennstoff-Verbrauch** | Menge Brennstoff, die Heizung pro Betriebsstunde verbraucht | Effizienz-Maßstab |
| **Combustor Cleaner** | Spezial-Additiv zur Reinigung des Brennerraums von Rußablagerungen | Wartungs-Additive |
| **Dichtungs-Ring** | Gummi- oder Kunststoff-Ring, der Wasser-Lecks an Verschraubungen verhindert | Dichtungs-Komponenten |
| **Dickinson-Heizung** | US-amerikanischer Hersteller, spezialisiert auf kleine Marine-Heizungen | Hersteller |
| **Diesel** | Flüssiger Brennstoff (Kerosin-Fraktion) für Heizungen und Motoren; maritim: Marinegas | Brennstoff-Typ |
| **Druckluft** | Komprimierte Luft (3–6 bar), verwendet zur Reinigung von Düsen und Sensoren | Werkzeug |
| **Druck-Manometer** | Instrument zur Messung des Brennstoff-Drucks (0–5 bar Bereich) | Diagnose-Werkzeug |
| **Druck-Regler** | Ventil, das Brennstoff-Druck auf Sollwert limitiert (z.B. 2.5 bar) | Regel-Komponente |
| **Druck-Sensor** | Elektrischer Sensor, der Brennstoff-Druck misst und Spannung ausgibt | Elektronische Komponente |
| **Druck-Schalter** | Elektrischer Schalter, der bei erreichtem Druck umschaltet | Sicherheits-Komponente |
| **Düse** | Sprüh-Element, das Brennstoff in feinen Nebel zerstäubt; Spezifikation z.B. 0.65 gal/h @ 100 psi | Kritisches Element |
| **Eberspächer** | Deutscher Hersteller von Heizungs- und Klima-Systemen | Hersteller |
| **Energieeffizienz** | Verhältnis der erzeugten Wärmemenge zum verbrauchten Brennstoff (% oder kWh/L) | Performance-Maßstab |
| **Ethylenglykol** | Giftiges Frostschutzmittel — NICHT für marine Heizkreisläufe verwenden (Toxizität, Trinkwassernähe an Bord); stattdessen Propylenglykol (marine, ungiftig, typisch 50% Wasser, 50% Glykol) | Additiv |
| **Flammenrohrsensor** | Optischer oder UV-Sensor, der das Feuer detektiert und der Steuerung signalisiert | Sicherheits-Sensor |
| **Fließpunkt** | Temperatur, unter der Diesel zu viskos wird und nicht mehr fließt (Winter-Diesel: -15°C) | Brennstoff-Eigenschaft |
| **Gebläse** | Elektrischer Lüfter, der heiße Luft oder Wasser umwälzt | Zirkulations-Komponente |
| **Gelcoat** | Kunststoff-Außenbeschichtung an GFK-Heizungs-Gehäusen (optional) | Material |
| **Geruchstest** | Manuelle Inspektion des Brennstoff-Geruchs zur Qualitäts-Bestimmung | Einfache Prüfung |
| **Glühzünder** | Weißes Heiz-Element (ähnl. Glühzündkerze), das Brennstoff zum Zünden bringt | Zündkomponente (veraltet) |
| **Halogenlampe** | Hochintensive Lampe, optional zur Flammenerkennung verwendet | Alternative zu Sensoren |
| **Heizkreislauf** | Geschlossenes System aus Pumpe, Rohren, Wärmetauscher, Thermostat | Funktionales System |
| **Heizleistung** | Ausgangsleistung der Heizung in Kilowatt (kW); z.B. 15 kW | Performance-Spezifikation |
| **Heizöl** | Schweres Heizöl (EL oder S), typisch in Landgebäuden (nicht maritim) | Brennstoff-Typ (nicht für Yachten) |
| **Heizwert** | Energie-Inhalt des Brennstoffs (Diesel: ~45 MJ/kg oder ~36 MJ/L) | Effizienz-Maßstab |
| **Hochdruckpumpe** | Elektropumpe, die Brennstoff unter 2.5–3.5 bar zur Düse drückt | Pumpen-Typ |
| **Isolation** | Wärmeschutzmaterial um Rohre (Schaum, Glaswolle, Neopren) | Effizienz-Komponente |
| **Kerze** | Kurzbegriff für Zündkerze (entzündungs-verursachende Komponente) | Umgangssprache |
| **Kompression** | Verdichtung von Luft im Brennerraum vor Zündung (thermische Heizungen: niedrig) | Physikalischer Prozess |
| **Kontakt-Korrosion** | Korrosion durch galvanische Paarung unterschiedlicher Metalle (z.B. Stahl+Kupfer) | Material-Problem |
| **Kühlwasser** | Wasser, das Wärme vom Brenner aufnimmt (Rückkehrer aus Wärmetauscher) | Zirkulierendes Medium |
| **Lamellenwärmetauscher** | Wärmetauscher mit feinen Lamellen zur Maximierung der Wärmefläche | Typen-Variante |
| **Magnetventil** | Solenoid-gesteuertes Ventil, das Brennstoff-Zu-/Abfluss steuert | Steuerkomponente |
| **Marinegas** | Hochqualitativ-Diesel für maritime Anwendungen (z.B. EN 590 Marine Diesel) | Brennstoff-Typ |
| **Messschleife** | Kunststoff- oder Kupfer-Leitung mit Messdose zur Durchfluss-Messung | Diagnose-Werkzeug |
| **Nächtliches Laden** | Heizungs-Betrieb während Nachtstunden bei Sofort-Temperatur-Bedarf | Nutzungs-Muster |

---

## Schnell-Referenz: Wartungs-Checkliste

```
TÄGLICHE NUTZUNG (vor dem Start):
  ☐ Visueller Check: Lecks oder Verschleiß?
  ☐ Brennstoff-Tank-Niveau prüfen
  ☐ 12V-Batterie-Spannung >11.5V?

WÖCHENTLICH:
  ☐ Nach Betrieb: Abgas-Farbe beobachten (orange = gut, schwarz = zu fett)
  ☐ Ausgleichsbehälter-Niveau prüfen (sollte 50% sein)

MONATLICH:
  ☐ Alle Schrauben/Befestigungen festziehen
  ☐ Isolations-Zustand der Rohre prüfen
  ☐ Flammrohrsensor sichtprüfung (sollte dunkelrot sein)

HALBJÄHRLICH (vor Wintersaison & Sommer):
  ☐ Brennstoff-Filter tauschen (€40–80)
  ☐ Brennstoff-Additive (Fuel Stabilizer) zugeben (€20–50)
  ☐ Wärmetauscher-Spülung mit Inhibitor (€30–50)
  ☐ Alle Kabel-Anschlüsse auf Korrosion prüfen

JÄHRLICH:
  ☐ Professionelle Inspektion & Wartung (€150–300)
  ☐ Zündkerze tauschen (€40–80)
  ☐ Brennstoff-Tank komplett ablassen & ersetzen (Altanlage)
  ☐ Druck-Test am Wassersystem (2 bar, 30 min halten)
  ☐ Schornstein-Inspektion auf Blockaden (€0 selbst, €100 Fachmann)

ALLE 2 JAHRE:
  ☐ Dichtungs-Satz tauschen (€80–150)
  ☐ Thermostatic Mixing Valve (falls vorhanden) inspizieren
  ☐ Brennstoff-Pumpen-Druck-Regler neu kalibrieren (€100–200)

ALLE 5 JAHRE:
  ☐ Wärmetauscher-Innenseite ultraschall-prüfen (€100–250)
  ☐ Kompletter Schlauch/Kupfer-Rohr-Austausch erwägen (Korrosionsrisiko)
```

---

## ANHANG A: Fallstudie 1 — Webasto Air Top 2000 ST in Besan

**Yacht:** Oceanis 38 Segelyacht, Länge 11.5m, Baujahr 2008
**Problem:** Heizung schaltet nach 3 Minuten ab, Wasser wird nur 30°C warm
**Diagnose-Weg:**
1. Thermostat sollte auf 55°C eingestellt sein, aber war auf 35°C
2. Brennstoff-Filter war dunkelbraun (verstopft)
3. Flammrohrsensor-Signal <0.3V (schmutzig)

**Lösung:**
- Brennstoff-Filter tauschen (€50)
- Flammrohrsensor mit Druckluft reinigen (€0)
- Thermostat-Sollwert auf 55°C neu einstellen (€0)

**Kosten:** €50 Material + €200 Arbeitszeit = €250 **Resultat:** Heizung lädt stabil, erreicht 55°C in 18 Minuten. Keine Probleme seitdem (6 Monate).

---

## ANHANG B: Fallstudie 2 — Eberspächer Airtronic D5 mit Wasser-Verlust

**Yacht:** Lagoon 40 Katamaran, Länge 12m, Baujahr 2015
**Problem:** Ausgleichsbehälter überläuft nach 2 Betriebsstunden
**Diagnose-Weg:**
1. Druck-Test: System mit 2 bar Wasser aufpressen, nach 10 min 0.3 bar Abfall
2. Seife-Spray: Leck an Wärmetauscher-Verschraubung lokalisiert
3. Dichtungs-Ring war porös (Material-Ermüdung)

**Lösung:**
- Wärmetauscher ausbauen, alte Dichtung entfernen (€0, Spatel)
- Neue Dichtungs-Satz installieren (€40)
- Wärmetauscher wieder einbauen und Drucktest (€0)
- System mit Inhibitor-Wasser spülen (€30)

**Kosten:** €70 Material + €400 Arbeitszeit = €470 **Resultat:** Kein Wasser-Verlust mehr. Betrieb stabil über 12 Monate.

---

## ANHANG C: Fallstudie 3 — Wallas 40D in der Arktis (Kalte Bedingungen)

**Yacht:** Tayana 48 Motoryacht, Länge 14.6m, Baujahr 2012, geplante arktische Expedition
**Problem:** Heizung zündet im Hafen in Tromsø (-8°C) nicht
**Diagnose-Weg:**
1. Brennstoff war Standard-Diesel mit -7°C Fließpunkt
2. Im Hafen (sehr kalt), Brennstoff zu viskös
3. Pumpe konnte Brennstoff nicht mehr zur Düse drücken

**Lösung:**
- Winter-Diesel (Marine Diesel -15°C Fließpunkt) vollständig austauschen (€150)
- Brennstoff-Filter tauschen (€60, weil Winter-Grad höher)
- Wasserleitungen mit Propylenglykol (marine, ungiftig) 50% auffüllen (€40) — kein Ethylenglykol (giftig, Trinkwassernähe)
- Schornstein-Fallrohr isolieren (€120 Neopren-Schlauch)

**Kosten:** €370 Material + €300 Arbeitszeit = €670 **Resultat:** Expedition erfolgreich. Heizung lädt zuverlässig bis -15°C.

---

## ANHANG D: Fallstudie 4 — Dickinson Diesel in Mittelmeer-Charter

**Yacht:** Sun Odyssey 36 Charterboot, Länge 11m, hohe Auslastung
**Problem:** Heizung flackert alle 4–6 min an und aus
**Diagnose-Weg:**
1. Flammrohrsensor-Signal schwankend (0.2–1.0V unregelmäßig)
2. Zündkerzen-Spalte 0.9mm statt 0.6mm (verschleißen)
3. Umluft-Klappe stockend

**Lösung:**
- Zündkerze tauschen (€55)
- Flammrohrsensor reinigen + Abschirmkabel überprüfen (€20)
- Umluft-Klappe mit Silikonöl treatment (€15)
- Brennstoff-Filter präventiv tauschen (€50)

**Kosten:** €140 Material + €250 Arbeitszeit = €390 **Resultat:** Heizung lädt stabil über 4 Wochen Charter-Betrieb.

---

## ANHANG E: Fallstudie 5 — Refleks 66 mit Verschlackung

**Yacht:** Hallberg-Rassy 36 Klassiker, Länge 10.8m, Baujahr 1985
**Problem:** Brennerraum-Verschlackung, schwarze Rußablagerungen
**Diagnose-Weg:**
1. Endoskopie: dicker schwarzer Belag an Brenner-Oberflächen
2. Brennstoff verdirbt (Tank war 5 Jahre alt)
3. Abgas-Farbe dunkelbraun (zu fettes Gemisch)

**Lösung:**
- Tank komplett ablassen (€0)
- Tank mit Druckluft innen ausblasen (€50)
- Brennstoff mit Fuel Cleaner zugeben (€30)
- Neuer Brennstoff (Marinegas Winter-Grade) einfüllen (€120)
- Brennerraum-Spülung mit Combustor Cleaner (€50)
- Düse tauschen (alte zu groß, 0.85 statt 0.65 gal/h; €120)

**Kosten:** €370 Material + €400 Arbeitszeit = €770 **Resultat:** Heizung lädt effizient. Abgas-Farbe orange. Verbrauch normal (0.6 L/h @ 15 kW).

---

## ANHANG F: Fallstudie 6 — Solenoid-Ventil defekt (Auto-Abschaltung funktioniert nicht)

**Yacht:** Bavaria Cruiser 46, Länge 14m, Baujahr 2010
**Problem:** Heizung läuft nach Ausschalter weiter (keine Automatik-Abschaltung)
**Diagnose-Weg:**
1. Solenoid-Spule unter Last prüfen: Widerstand konstant (keine Spannung-Modulation)
2. Spule direkt 12V geben: kein "Klick"-Geräusch (Spule verschweißt)
3. Brennstoff tropft langsam weiter (Ventilnadel nicht dicht)

**Lösung:**
- Solenoid-Ventil ausbauen (€0, Standard-Flansch)
- Neue Solenoid-Spule einbauen (€90)
- Ventilnadel ultraschall-reinigen (€20)
- 12V-Schaltkreis prüfen (Relais OK)
- Test: Heizung ausschalten → Brennstoff-Durchfluss stoppt sofort

**Kosten:** €110 Material + €200 Arbeitszeit = €310 **Resultat:** Heizung schaltet zuverlässig ab. Sicherheit gewährleistet.

---

## ANHANG G: Fallstudie 7 — Thermostat-Nachrüstung in alte Heizung

**Yacht:** Franchini Motoryacht, Länge 13m, Baujahr 1998 (keine Temperatur-Kontrolle)
**Problem:** Heizung lädt kontinuierlich bis >70°C (Risiko für Dichtungen)
**Lösung:**
1. Thermostatic Mixing Valve (TMV) Grohe Alloy oder Ideal-Logik installiert
2. Montage an Aus-Gang des Wärmetauschers (vor Verteiler)
3. Sollwert auf 55°C kalibriert (mit Thermometer überprüft)
4. Drucktest nach Installation (2 bar, 30 min halten)

**Kosten:** €280 (TMV) + €500 (Montage & Integration) = €780 **Resultat:** Heizung lädt bis 55°C, stoppt automatisch. Dichtungs-Lebensdauer erhöht sich deutlich.

---

## ANHANG H: Fallstudie 8 — Brennstoff-Kontamination (Wasser im Tank)

**Yacht:** Oyster 56, Länge 17m, Liveaboard
**Problem:** Heizung startet, läuft 20 sec, dann stoppt mit "Pump Failure"
**Diagnose-Weg:**
1. Brennstoff-Probe: orangebraun, Wasser-Test zeigt Schichtbildung
2. Tank-Inspektion: Schleimbelag (Mikroben-Wachstum)
3. Brennstoff-Filter dunkelgrün/moosig

**Lösung:**
- Brennstoff komplett ablassen (€0)
- Tank trocken ausblasen (komplett austrocknen; €100)
- Tank-Innenseite mit Biozid-Spray (Kathon FP1.5) behandeln (€150, Fachmann)
- 48 h Einwirkung, dann mit trockener Druckluft ausblasen (€50)
- Komplett neuer Brennstoff (Marinegas) einfüllen (€200)
- Brennstoff-Filter 2x tauschen (erste nach 10 L, zweite nach 50 L; €100)

**Kosten:** €600 Material/Service + €300 Arbeitszeit = €900 **Resultat:** Heizung lädt zuverlässig. Brennstoff-Qualität stabil über 12 Monate mit regelmäßigen Additive-Zugaben.

---

## ANHANG I: Pydantic v2 Modelle

```python
# knowledge/models.py
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from enum import Enum

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

class HeatingSystemType(str, Enum):
    WEBASTO = "webasto"
    EBERSPACHER = "eberspacher"
    WALLAS = "wallas"
    REFLEKS = "refleks"
    DICKINSON = "dickinson"
    HURRICANE = "hurricane"

class FaultPattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    code: str = Field(..., description="FB-26-01-001 etc")
    symptom_de: str = Field(..., description="German symptom description")
    root_causes: List[str] = Field(..., description="List of root causes by frequency")
    diagnosis_steps: List[str] = Field(...)
    repair_actions: List[dict] = Field(..., description="[{'action': str, 'cost_eur': int}]")
    preventive_maintenance: List[str] = Field(...)
    confidence: ConfidenceLevel

class TroubleshootingTree(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    description: str
    root_question: str
    decision_nodes: List[dict]
    leaf_solutions: List[dict]

class FAQEntry(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    question_de: str
    answer_de: str
    keywords: List[str]
    related_fault_patterns: List[str]

class GlossaryTerm(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    term: str
    definition_de: str
    context: Optional[str] = None
    synonyms: List[str] = Field(default_factory=list)

class CaseStudy(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    yacht_model: str
    length_m: float
    build_year: int
    problem_de: str
    diagnosis_path: List[str]
    solution: str
    cost_eur: float
    outcome_de: str
    duration_months: int

class MaintenanceSchedule(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    interval: str  # "daily", "weekly", "monthly", "semi-annually", "annually", "5-yearly"
    tasks: List[dict]  # [{"task": str, "cost_eur": Optional[int]}]

class HeatingSystemKnowledge(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    system_type: HeatingSystemType
    fault_patterns: List[FaultPattern]
    troubleshooting_trees: List[TroubleshootingTree]
    faq: List[FAQEntry]
    glossary: List[GlossaryTerm]
    case_studies: List[CaseStudy]
    maintenance_schedule: MaintenanceSchedule
    version: str = "1.0"
    last_updated: str = "2026-05-18"
```

---

## ANHANG J: Technische Referenzen — Webasto

- **Air Top 2000 ST**: 2 kW, 12V/24V Diesel
- **Air Top 3500 ST**: 3.5 kW, Webasto-Standard
- **Air Top 5000**: 5 kW, häufig in größeren Yachten
- **Air Top EVO**: Elektronisch geregelt, Thermostat 0–100%
- **Kontakt**: support@webasto.com, +49 89 xxxx

**Verfügbare Ersatzteile:**
- Zündkerze: GW2000 (€45–60)
- Brennstoff-Düse: 0.65 gal/h @ 100 psi (€90–120)
- Dichtungs-Satz: €65–95
- Flammrohrsensor: €80–150
- Solenoid-Ventil: €120–200
- Komplettes Steuergerät: €600–900

---

## ANHANG K: Technische Referenzen — Eberspächer

- **Airtronic D2**: 2 kW, 12V Einstiegs-Modell
- **Airtronic D4**: 4 kW, beliebte Größe für 10–15m Yachten
- **Airtronic D5**: 5 kW, für Motoryachten
- **Thermo Top C**: Kombiniert Heizung + Warmwasser (teuer, €3000+)
- **Thermo Top E**: Elektrisch geregelt (präzise Temperatur)
- **Kontakt**: service.de@eberspacher.de

**Verfügbare Ersatzteile:**
- Zündkerze: EK-60 oder EK-61 (€50–70)
- Brennstoff-Düse: 0.60–0.75 gal/h (€85–130)
- Dichtungs-Satz komplett: €70–110
- Pumpen-Einheit: €180–280
- Steuergerät EasyStart: €700–1000

---

## ANHANG L: Technische Referenzen — Wallas

- **Wallas 30D**: 3 kW, 12V, kompaktes Modell
- **Wallas 40D**: 4 kW, Hauptmodell
- **Wallas 50D**: 5 kW, für große Yachten
- **Wallas 60DI**: 6 kW, mit integriertem Warmwasser-Boiler
- **Kontakt**: info@wallas.fi, +358 xx xxxx

**Ersatzteile:**
- Zündkerze: WALLAS-Standard (€48–65)
- Düse: Standard 0.65 gal/h (€95–140)
- Komplettes Brenner-Set: €400–600
- Thermostat-Modul: €150–250

---

## ANHANG M: Technische Referenzen — Refleks

- **Refleks 66**: 6.6 kW, Größtes Modell der Refleks-Serie
- **Refleks 55**: 5.5 kW (älter, weniger verbreitet)
- **Besonderheit**: Skandinavisches Design, robuste Bauweise
- **Kontakt**: teknisk@refleks.se

**Ersatzteile:**
- Zündkerze: Refleks-spezifisch (€45–60)
- Düse: 0.65–0.80 gal/h (€100–150)
- Dichtungs-Satz: €65–100
- Gebläse-Motor: €300–500

---

## ANHANG N: Technische Referenzen — Dickinson

- **Dickinson Diesel L118**: 1.8 kW, kleinste Variante
- **Dickinson Diesel L320**: 3.2 kW, beliebt bei Segelbooten
- **Dickinson Diesel L520**: 5.2 kW, für mittlere Motoryachten
- **Besonderheit**: Amerikanischer Standard, lange Lebensdauer
- **Kontakt**: support@dickinsonmarine.com

**Ersatzteile:**
- Zündkerze Bosch GL11Z (€55–75)
- Düse Delco (€80–120)
- Dichtungs-Material (€40–70)

---

## ANHANG O: Technische Referenzen — Hurricane Diesel Heating

- **Hurricane 1**: 1 kW, sehr kompakt
- **Hurricane 3**: 3 kW, für kleine Cruiser
- **Hurricane 5**: 5 kW, mittelgroß
- **Besonderheit**: Einfache Bedienung, minimale Elektronik
- **Kontakt**: hurricane.se (Schweden)

**Ersatzteile:** Ähnlich wie Refleks/Wallas.

---

## ANHANG P: Sicherheits-Richtlinien

**Installation:**
1. Heizung muß min. 1m von brennbaren Stoffen (Textilien, Papier) entfernt sein
2. Schornstein muß außenbord führen, mind. 0.5m höher als Reling
3. Brennstoff-Tank isoliert, nicht unter Schlafplätzen
4. Elektrische Verdrahtung mit Kupfer ≥2.5mm² für Strom >10A

**Betrieb:**
1. Niemals unter Last abschalten (mind. 5 min Abkühlungsphase)
2. Regelmäßige Drucktest (jährlich, 2 bar, 30 min)
3. Abgas-Kontrolle (orange Flamme = OK, schwarz = Problem)
4. Notaus-Schalter installieren (zugänglich in <2 sec)

**Winterlagerung:**
1. Brennstoff ablassen ODER Fuel Stabilizer zugeben
2. Zündkerze herausschrauben, trockene Luft durchblasen
3. Wassersystem mit Propylenglykol (marine, ungiftig) auffüllen (Korrosionsschutz) — kein Ethylenglykol (giftig, Trinkwassernähe)
4. Monatlich kurz starten (1–2 min) ohne Last

---

**Dokument erweiterte Version: 1.2**
**Gültig ab:** 2026-05-18
**Nächste Überprüfung:** 2026-11-18
