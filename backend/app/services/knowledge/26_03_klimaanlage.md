---
category: "26_Heizung_Klima"
subcategory: "Klimaanlage"
title: "Bootsklimaalagen – Umfassender Designleitfaden"
revision: "v2.1"
language: "de"
last_updated: "2026-05-18"
---

# Bootsklimaalagen: Umfassender Designleitfaden

## 1. Einführung

### 1.1 Bedeutung von Klimaanlagen im Bootsbau

Marine Klimaalagen sind essenzielle Systeme für den Komfort und die Sicherheit moderner Segelboote, Motoryachten und Expeditionsfahrzeuge. Im Gegensatz zu Landfahrzeugen müssen Bootsklimaalagen extremen Bedingungen standhalten:

- **Salzwasserkorrosion**: Alle Komponenten müssen marinegerecht sein
- **Bewegungen und Vibrationen**: Schiffe schaukeln; starre Systeme versagen
- **Begrenzte Energieressourcen**: Bordnetzspannung, Generatorlast, Batteriepuffer
- **Platzbeschränkungen**: Integration in enge Rümpfe und Aufbauten
- **Wartungslogistik**: Reparaturen in Häfen, nicht in Werkstätten

Klimaalagen haben zwei Hauptfunktionen:
1. **Kühlung**: Abführung von Wärmequellen (Motor, Sonneneinstrahlung, Besatzung)
2. **Heizung** (Wärmepumpe): Winterbetrieb in gemäßigten Breiten oder tropischen Nächten

### 1.2 Regulatorischer Kontext

- **CE-Kennzeichnung**: Energieeffizienz-Richtlinie 2015/1095/EU
- **IMO MARPOL Annex VI**: Kältemittel-Beschränkungen (Phase-out von R22, R402A)
- **Schiffssicherheitsverordnung (SchSV)**: Belüftung und Stromversorgung
- **DIN EN 378**: Sicherheit Kälte- und Wärmepumpenanlagen

### 1.3 Systemklassifizierung nach Schiffsgröße

| Bootsgröße | Typisches System | BTU-Bereich | Stromversorgung |
|-----------|------------------|-------------|-----------------|
| 7–12 m | Selbstständiges Deck-Fenster | 5,000–12,000 | 220V/10A |
| 12–18 m | Split-System 1–2 Verdampfer | 12,000–24,000 | 380V/16A oder 220V/20A |
| 18–30 m | Chilled-Water-Loop | 24,000–60,000 | 3-Phase 380V/32A+ |
| 30+ m | Multi-Zone mit Redundanz | 60,000–120,000 | Dedicated Gen-Set |

---

## 2. Grundlagen der Maritimen Kühlzyklus-Technologie

### 2.1 Der Kältemittelkreislauf (Verdampfer-Kompressor-Kondensator)

```
Wärmequelle (Kabine)
    ↓
[Verdampfer] – Kältemittel verdampft, entzieht Wärme
    ↓
[Verdichter/Kompressor] – Erhöht Druck und Temperatur
    ↓
[Verflüssiger/Kondensator] – Abführung zu Seewasser
    ↓
[Drosselventil] – Entspannung vor Verdampfer
    ↓
zurück zu [Verdampfer]
```

**Effizienzkennzahl (COP – Coefficient of Performance):**
- Kühlung: COP = 3–4 (gute Seewasserkühlung)
- Heizung: COP = 2–3 (Umgebungstemperatur-abhängig)

### 2.2 BTU-Dimensionierung für Yachten

**Faustregeln nach Bootsgröße und Nutzung:**

Wärmeeintrag in BTU/h:
- Sonneneinstrahlung: 250–400 BTU/h pro m² Fenster/Konus
- Motor (laufend): 10,000–25,000 BTU/h für Diesel 25–75 kW
- Besatzung (4–6 Pers.): 400–600 BTU/h
- Kochfeuer: 2,000–5,000 BTU/h
- **Elektronik/LED**: 200–500 BTU/h

**Auslegungsfaktor:**
- Normalbetrieb: Summe Wärmeeintrag × 1,2
- Tropisch (>35°C): × 1,4
- Hochleistung (Motorsegeln): × 1,6

**Beispiel 15m Segelboot:**
- Sonneneinstrahlung (3 m² Fenster): 3 × 300 = 900 BTU/h
- Motor 30 kW (2h/Tag): 15,000 BTU/h
- Besatzung (5 Pers.): 500 BTU/h
- Elektronik: 300 BTU/h
- **Gesamt Wärmeeintrag**: ~16,700 BTU/h
- **Auslegung mit Faktor 1,3**: **21,700 BTU/h** → Standard 24,000 BTU/h AC

### 2.3 Seewasserkühlung vs. Luftkühlung

#### Seewasserkühlung (Standard für Marine)
- **Vorteil**: Effiziente Wärmeabfuhr, stabile COP
- **Nachteil**: Korrosion, Muschelbewuchs, Salzwasser-Eindringung
- **Rohre**: Kunststoff Marelon (nicht Kupfer), min. Ø19 mm
- **Filterung**: 100 µm Durchlauffilter vor Kondensator
- **Durchsatz**: 1.2–1.5 l/min pro 1000 BTU Kühlleistung

> ⚠️ **ZU PRÜFEN (Audit):** "1,2–1,5 l/min pro **1000 BTU**" widerspricht allen übrigen Fundstellen (FB-26-03-003, Baum 7.2, FB-26-03-007), die durchgehend "1,2–1,5 l/min pro **10 kBTU**" nennen — Faktor 10. Die Angabe "pro 1000 BTU" ist physikalisch unplausibel (ergäbe 12–15 l/min pro 10 kBTU). Richtung nicht zweifelsfrei belegbar, daher nicht korrigiert. Confidence: estimated — unverifiziert.

#### Luftkühlung (nur für Deck-Units)
- **Vorteil**: Einfach, wartungsarm
- **Nachteil**: Externe Wärmeabfuhr (ggf. zu Decksventilator)
- **Anwendung**: Kleine Boote, Notfall-Backup

### 2.4 Kältemittel-Auswahl

| Kältemittel | GWP | ODP | Status | Bootseinsatz |
|-----------|-----|-----|--------|--------------|
| R410A | 2,087 | 0 | Phase-out 2030 | Alt, häufig |
| R32 | 677 | 0 | In Verwendung | Neu Standard |
| R290 (Propan) | 3 | 0 | Low-GWP | Nischensysteme |
| R1234yf | 4 | 0 | Emerging | Zukunft |
| R22 | 1,810 | 0.055 | VERBOTEN | Alte Systeme |

**Merkregel für Bootsingenieur**: Alle vor 2010 installierten Systeme wahrscheinlich R22 → Austausch notwendig

---

## 3. Systemtypenübersicht

### 3.1 Selbstständige Deck-Fenster-Units (5–15 kBTU)

**Aufbau**: Kompressor, Kondensator, Verdampfer, Regelung in EINER Einheit

```
┌─ Außenluft-Auslass
│
[Kompressor] ← Stromversorgung (220V)
    ↓
[Kondensator] – Seewasser durchströmt
    ↓
[Drosselventil]
    ↓
[Verdampfer] – Innenluft durchströmt
    ↓
Kaltluft in Kabine
```

**Merkmale:**
- Installation: Fensteröffnung oder Decklukenausschnitt
- Wartung: Seewasser-Filterreinigung monatlich
- COP: 3.2–3.8
- Lautstärke: 65–75 dB(A)
- Preis: EUR 3,500–6,500

**Hersteller-Beispiele:**
- Dometic CoolBreeze
- Marine Air Aqua-Air
- Frigomar FG3500

### 3.2 Split-Systeme (12–30 kBTU)

**Aufbau**: Externe Kompressor-Unit (Maschinenschacht/Deck) + 1–3 Innen-Verdampfer

```
[Seewasser-Pumpe] → [Kondensator im Verdichter] → [Rücklauf ins Meer]
                            ↓
                     [Kältemittel-Leitung 10–25 m]
                            ↓
    [Verdampfer 1] [Verdampfer 2] [Verdampfer 3]
         ↓              ↓              ↓
      Kabine         Saloon       Eignerkabine
```

**Merkmale:**
- **Flexibilität**: Multi-Zone Temperaturregelung
- **Effizienz**: COP 3.8–4.2 (externe Luftkühlung möglich)
- **Installation**: Rohrleitungs-Komplexität, Isolierung erforderlich
- **Stromverbrauch**: 4–8 kW (16–32A bei 220V)
- **Lautstärke**: Verdichter 60 dB(A) im Maschinenraum
- **Preis**: EUR 8,000–18,000 (ohne Rohrleitungen)

**Kältemittel-Rohre:**
- Kupfer 3/8" (9.5 mm) Standard
- Isolierung: 10–25 mm Polyurethan
- Verlegung: nicht über Motorbereiche, Vibrationsdämpfer

### 3.3 Chilled-Water-Systeme (24–120 kBTU)

**Aufbau**: Zentraler Wasserkühler + Verteiler-Leitungssystem + Innen-Ventilkonvektoren

```
Seewasser-Einlass
         ↓
[Zentral-Chiller] ← Kompressor
         ↓
   [Umwälzpumpe]
         ↓
  [Verteilernetz mit Regeln]
    ↙    ↓    ↘
[FanCoil] [FanCoil] [FanCoil]
  Galley  Saloon   Kabine
```

**Merkmale:**
- **Skalierbarkeit**: Bis zu 8–10 Verdampfer
- **Temperaturgenauigkeit**: ±1°C durch zentrale Regelung
- **Stromverbrauch**: 6–15 kW
- **Lautstärke**: Ventilkonvektoren 45–55 dB(A)
- **Wartung**: Zentrale Filterung, Wasser-Additiv-Kontrolle
- **Preis**: EUR 25,000–60,000

**Wasser-Eigenschaften:**
- Frostschutz: Glykol 30 % (bis –15°C)
- Korrosionsschutz: Silikat oder organisch basiert
- pH: 8.0–9.5 (monatliche Prüfung)
- Durchfluss: 0.3–0.5 l/s pro Verdampfer

### 3.4 Wärmepumpen-Umkehranlage (15–45 kBTU)

**Aufbau**: Reversibles Kältemittel-System mit 4-Wege-Ventil

```
Heizmodus:
    [Innenluft-Wärmequelle] → [Verdampfer im Innenmodul]
                   ↓
           [Verdichter-Pumpe]
                   ↓
    [Kondensator im Außenmodul] → Seewasser-Wärmeabfuhr

Kühlmodus (umgekehrt):
    [Seewasser-Kondensator] → [Verdichter]
                   ↓
         [Innenluft-Verdampfer] → Kabinenkühlung
```

**Merkmale:**
- **Doppelfunktion**: Kühlung + Heizung im gleichen System
- **COP Heizung**: 2.2–3.0 (bei 5–20°C Außentemperatur)
- **COP Kühlung**: 3.5–4.0
- **Stromverbrauch**: 3.5–7 kW
- **Sensorik**: Außentemperatur-Fühler, Hochdruck-Schalter
- **Preis**: EUR 12,000–25,000

**Winterbetrieb-Überlegungen:**
- Verdampfer-Vereisung bei <2°C Seewassertemperatur
- Heißgas-Defrost-Zyklus alle 15–30 Min
- Lautstärke steigt auf 70–75 dB(A) im Defrost-Betrieb

---

## 4. Produktlinien und Größenklassifizierung

### 4.1 5,000–12,000 BTU Deck-Units

| Modell | Hersteller | BTU | Strom | Filtergebühren | Preis EUR |
|--------|-----------|-----|-------|----------------|-----------|
| CoolBreeze 5K | Dometic | 5,000 | 220V/10A | Monatlich | 3,800 |
| Cruisair Compact | Marine Air | 7,000 | 220V/13A | Alle 2 Mo. | 4,200 |
| FG3500 | Frigomar | 6,000 | 220V/12A | Monatlich | 3,600 |
| Climma 5.2 | Climma | 5,000 | 220V/10A | Monatlich | 3,500 |

**Energieverbrauch**: 1.5–2.0 kW (5–8A bei 220V)

### 4.2 12,000–24,000 BTU Split-Systeme

| Modell | Verdichter-Ort | BTU | Verdampfer | Strom | Preis EUR |
|--------|---------------|-----|-----------|-------|-----------|
| Marine Air 15 | Salon/Deck | 15,000 | 1 | 220V/18A | 8,500 |
| Frigomar FG8000 | Maschinenschacht | 18,000 | 2 | 220V/20A | 10,200 |
| Webasto SeaComfort | Motor-Deck | 20,000 | 2 | 380V/16A | 11,800 |
| Cruisair Supreme | Außen-Box | 24,000 | 2–3 | 380V/18A | 13,500 |

**Energieverbrauch**: 3.5–6 kW (16–27A bei 220V; 9–15A bei 380V)

### 4.3 24,000–60,000 BTU Chilled-Water

| System | Hersteller | BTU | Verdampfer | Strom | Preis EUR |
|--------|-----------|-----|-----------|-------|-----------|
| MPS Cooler 24 | MPS | 24,000 | 3–4 | 380V/20A | 18,000 |
| Climma Comfort 35 | Climma | 35,000 | 4–5 | 380V/25A | 28,500 |
| Frigomar FG15000 | Frigomar | 40,000 | 5–6 | 3-Phase/32A | 35,000 |
| Webasto Compact 50 | Webasto | 50,000 | 6–8 | 3-Phase/40A | 48,000 |

**Energieverbrauch**: 7–14 kW (32–63A bei 380V drei-phasig)

### 4.4 Wärmepumpen (15–45 kBTU reversibel)

| Modell | Hersteller | BTU | Heizung | Kühlung | Strom | Preis EUR |
|--------|-----------|-----|--------|--------|-------|-----------|
| Marine Heat 18 | Dometic | 18,000 | ✓ | ✓ | 220V/20A | 14,500 |
| Cruisair Reverse | Marine Air | 24,000 | ✓ | ✓ | 380V/18A | 16,800 |
| MPS HeatCool 30 | MPS | 30,000 | ✓ | ✓ | 380V/25A | 22,000 |
| Climma Dual 42 | Climma | 42,000 | ✓ | ✓ | 3-Phase/32A | 32,500 |

---

## 5. Hersteller und Produktportfolio

### 5.1 Dometic Marine (Schweden)

**Kernmarken**: Cruisair, Marine Air, CoolBreeze

**Portfolio**:
- Deck-Units: CoolBreeze 5K (3,800 EUR), 7K (4,300 EUR)
- Split-Systeme: Marine Air 15–24 kBTU (8,500–13,500 EUR)
- Wärmepumpen: Marine Heat 18–30 kBTU (14,500–20,000 EUR)
- Chilled-Water: Climma Comfort 24–60 (18,000–45,000 EUR)

**Besonderheit**: Best-in-Class Seewasser-Filterdesign, automatische Spülzychen

**Servicenetz**: Deutschland 85+ zertifizierte Partner

### 5.2 Webasto (Deutschland)

**Kernmarken**: Webasto Marine, SeaComfort

**Portfolio**:
- Deck-Units: Keine (fokus auf Split+)
- Split-Systeme: SeaComfort 12–24 kBTU (9,500–12,000 EUR)
- Wärmepumpen: SeaHeat 18–40 kBTU (15,500–24,000 EUR)
- Chilled-Water: Compact 35–60 kBTU (28,000–52,000 EUR)

**Besonderheit**: Integrierte Motorwärme-Rückgewinnung, ORC-Ergänzung möglich

**Servicenetz**: Deutschland 120+ zertifizierte Partner (Boilermaker + Klima)

### 5.3 Frigomar (Italien)

**Portfolio**:
- Deck-Units: FG3500 (3,600 EUR), FG5000 (4,100 EUR)
- Split-Systeme: FG8000–FG12000 (10,200–15,500 EUR)
- Chilled-Water: FG15000–FG25000 (35,000–65,000 EUR)

**Besonderheit**: Koppelung mit Brennstoffzellen-Systemen, Low-Vibration Kompressor

### 5.4 Climma (Italien)

**Portfolio**:
- Deck-Units: 5.2–7.2 kBTU (3,500–4,800 EUR)
- Split-Systeme: 12–24 kBTU (8,000–12,500 EUR)
- Chilled-Water: Comfort 24–80 kBTU (18,000–70,000 EUR)
- Wärmepumpen: Dual 18–50 kBTU (13,500–35,000 EUR)

**Besonderheit**: Modulares Ventilkonvektor-Portfolio, sehr leise (<40 dB(A))

### 5.5 MPS (Mittelmeer Plasma Systems, Spanien)

**Portfolio**:
- Kompakt-Systeme: 12–24 kBTU Split (8,500–12,000 EUR)
- Chilled-Water: Cooler 24–100 kBTU (18,000–75,000 EUR)
- Wärmepumpen: HeatCool 18–60 kBTU (16,000–38,000 EUR)

**Besonderheit**: High-Reliability Redundanz-Optionen, IMO MARPOL zertifiziert

---

## 6. Fehlerbild-Atlas

### FB-26-03-001: Wasserlecks im Seewasser-Schlauch

**Symptom**: Salzwasser-Tropfen unter Verdichter; Kellergeruch in Maschinenschacht

**Häufigste Ursachen**:
- Verrottung Kunststoff-Schlauch (Age: >8 Jahre, UV-Exposition)
- Vibrations-Risse an Anschlussadaptern
- Unzureichende Schlauchklemmen (Original: 2, ersetzen: mind. 3)

**Inspektionspunkte**:
- Schlauch-Durchmesser 19–25 mm, Druck max 3 bar
- Farbe: transparent Kunststoff → sollte NICHT braun/verfärbt sein
- Klemmen: Edelstahl 316L, auf Spannmarke geprüft

**Abhilfemaßnahmen**:
1. Neue Marineschläuche (Marelon oder Trident) kaufen (EUR 80–200 je Schlauch)
2. Alle 4 Klemmen ersetzen, auf Spannmarke torquieren (2–3 Nm)
3. Filtergehäuse öffnen, Salzablagerungen mit Essigwasser spülen
4. 15 Minuten Trockenlauf ohne Verdichter zur Prüfung

**Häufigkeit**: 18–24 Monate bei tropischen Gewässern; 36–48 Monate in gemäßigten Breiten

---

### FB-26-03-002: Luftblase im Kältemittelkreislauf (Schaum in Kondensator)

**Symptom**: Verdichter läuft, aber Innenluft wird nicht kalt; Druckabfall; gelegentliches "Zischen"

**Ursachen**:
- Zu schnelle Ladeabsenkung des Kältemittels (Leck, nicht sachgerecht gefüllt)
- Öl-Separation bei Hochfrequenz-Verdichtung
- Drosselventil teilweise blockiert

**Diagnose**:
- Hochdruckmanometer: <15 bar (normal: 18–25 bar)
- Tiefdruckmanometer: >5 bar (normal: 2–4 bar)
- Vibrations-Ton: hochfrequent "pfeifend" statt "Brummen"

**Behebung**:
1. Verdichter stoppen, System 30 min ruhen lassen
2. Druckausgleich durch Niederdruck-Ventil kontrollieren
3. Kältemittel-Nachfüllung (EUR 150–400) mit zertifiziertem Techniker
4. Öl-Analyse nach 50 Betriebsstunden

**Prävention**: Jährliche Druckprüfung vor Saison

---

### FB-26-03-003: Kondensator verstopft (Muschelwuchs, Algen)

**Symptom**: Hochdruck-Anstieg >30 bar; Verdichter-Sicherheitsschalter löst nach 5–10 min aus; schwache Kühlung

**Ursachen**:
- Seewasser-Filter (100 µm) nicht monatlich gereinigt
- Muscheln/Schnecken im Rohrsystem
- Biofilm-Algen bei Stillstand >2 Wochen

**Inspektionspunkte**:
- Durchflussrate Seewasser sollte 1.5 l/min pro 10 kBTU sein
- Kondensator-Einlassrohr: sollte warm sein (35–40°C)
- Auslass: 25–28°C (3–5 K Differenz = normal)

**Abhilfemaßnahmen** (Kosten EUR 400–1200):
1. Filter demontieren, Kartridge mit Hochdruckreiniger spülen (<80 bar)
2. Chemische Rohrreinigung: Zitronensäure-Lösung 5 % zirkulieren (2 h)
3. Verdichter 15 min ohne Last laufen, Druck überwachen
4. Seacock sperren, System drucklos machen
5. Kondensator von außen mit Meerwasser-Hochdruck nachspülen

**Prävention**: Monatliche Filter-Kontrolle; Seacock absperren bei Stillstand >1 Woche

---

### FB-26-03-004: Durchrostung Seewasser-Filter-Gehäuse (Galvanischer Fehler)

**Symptom**: Brackwasser/Rost-Suspension in Filtergehäuse; Durchrostung an Nahtstellen; Leck unterhalb Filterdeckel

**Ursachen**:
- Messing-Filter in Kontakt mit 316L Edelstahl ohne Isolierung (Galvanokorrosion)
- Kupfer-Schlauch statt Kunststoff (Dezinnung)
- Salzwasser-Spritzer auf ungeschütztem Gehäuse bei Topload-Installation

**Inspektionspunkte**:
- Filtergehäuse sollte Edelstahl 316L oder Kunststoff sein
- Verbindungen mit Isolierschieben geprüft?
- Sichtprüfung: rote Oxid-Flecken = Anfangsstadium

**Behebung** (EUR 600–1400):
1. Komplettes Filtergehäuse austauschen (nicht reparabel)
2. Neue Rohrleitungen Kunststoff Marelon 25 mm
3. Isolierschieben bei allen Übergängen installieren
4. Schutzanstrich marinegrau auf Verschraubungen

**Lebensdauer**: Typisch 7–10 Jahre in tropischen Gewässern; 15+ Jahre gemäßigt

---

### FB-26-03-005: Verdichter-Ausfallgeräusch (Pfeifton, Schleifen)

**Symptom**: Mechanisches Schleifen/Pfeifton; Verdichter läuft nicht; Sicherheitsschalter aus

**Ursachen**:
- Hydraulisches "Schlag"-Phänomen (zu viel flüssiges Kältemittel im Verdichter)
- Verschliss Verdichter-Lager nach 10.000+ Betriebsstunden
- Fremdkörper (Metallspäne aus Schweißnähten alt)

**Inspektionspunkte**:
- Vibrations-Test: Verdichter sollte leise "brummen" (50–60 dB), nicht "quieken"
- Betriebsstunden-Zähler (falls vorhanden) prüfen
- Ölprobe aus Ölschauglas entnehmen: sollte bernsteinfarben sein, nicht dunkelbraun

**Abhilfemaßnahmen**:
1. Verdichter SOFORT abschalten (keine Neustarts)
2. Druckausgleichventil 30 min offen lassen
3. Verdichter-Austausch notwendig (EUR 2,800–5,200 je Modell)
4. Beim Ausbau: Alte Schleifspäne mit Lösungsmittel spülen
5. Neuer Trockner + neue Ölfüllung erforderlich

**Vorlaufwarnung**: Tonveränderung, erste Startphase verlängert sich um >10 sec

---

### FB-26-03-006: Thermostat-Fehler (Überschießende Temperatur)

**Symptom**: Innentemperatur sinkt unter Sollwert (z.B. 16°C statt 20°C gewünscht); Verdichter läuft ständig

**Ursachen**:
- Fühler-Draht loses Kontakt oder Kurzschluss
- Elektronik-Modul Ausfalllogik fehlerhaft
- Verdampfer-Überfrostung, Eisfläche blockiert Luftstrom

**Inspektionspunkte**:
- Fühler-Widerstand prüfen (NTC 10 kΩ bei 25°C Standard)
- Verdampfer-Oberfläche: eisfrei? (sollte leicht feucht, nicht weiß)
- Steuermodule: Feuchtekorrosion in Steckerleisten?

**Behebung** (EUR 200–800):
1. Fühler-Kontakte mit Kontaktspray reinigen
2. Eisfläche mit warmer Luft abtauen, NICHT kratzen
3. Fühler-Ersatz falls Widerstand nicht im Toleranzbereich (€80–150)
4. Elektronik-Modul-Austausch falls Fühler OK (€400–700)

**Prävention**: Jährliche Sensor-Kalibrierung

---

### FB-26-03-007: Hochdruck-Sicherheitsschalter löst permanent aus

**Symptom**: Verdichter läuft 5–10 min, dann Automatik-Abschaltung; Alarm/Warnsignal

**Ursachen**:
- Seewasser-Durchfluss zu niedrig (<1.2 l/min pro 10 kBTU)
- Kondensator-Rohre intern verkrustet
- Schalter selbst fehlerhaft (Kontakt-Oxid)

**Inspektionspunkte**:
- Seewasser-Durchfluss messen (Kübel 30 sec füllen, sollte >1.8 l sein)
- Hochdruck-Manometer: wenn >30 bar sofort stoppen
- Schalter-Prüfung: Beim Neustart Druck überwachen

**Behebung**:
1. Seawaterfilter sofort austauchen (100 µm-Kartridge EUR 80–120)
2. Kondensator-Spülung mit Zitronensäure-Lösung durchführen
3. Hochdruck-Schalter-Test mit Prüfpumpe durchführen (EUR 300–600 Service)
4. Schalter ersetzen falls Auslösung <25 bar (€150–280)

**Neustart**: Erst nach vollständiger Behebung; mehrfach testen

---

### FB-26-03-008: Verdampfer-Vereisung in Heizmode (Wärmepumpe)

**Symptom**: Wenig warme Luft; Verdampfer sichtbar vereist; Kältemittel-Druck sinkt rapide

**Ursachen** (nur Reverse-Cycle-Wärmepumpen relevant):
- Außentemperatur <3°C, Seewasser <5°C
- Defrost-Zyklus funktioniert nicht (4-Wege-Ventil blockiert)
- Zu feuchte Außenluft kondensiert und friert

**Inspektionspunkte**:
- Äußeres Kondensator-Rohr: weiß vereist oder schwarz (normal in Defrost)?
- Heißgas-Ventil öffnet sich regelmäßig (hört man "Klick" alle 20–30 sec)?
- Außentemperatursensor: gibt korrekten Wert aus?

**Behebung**:
1. Wärmepumpe in "Defrost"-Modus zwingen (Fernbedienung Spezialfunktion)
2. 20 min laufen lassen, Eis auftauen, Wasser ablaufen lassen
3. Normalzyklus zurückschalten
4. Falls Problem bestehen bleibt: 4-Wege-Ventil-Spulen ersetzen (EUR 350–550)

**Betriebslimit**: Wärmepumpen-Heizung typisch bis 2°C Seewasser; darunter Heizelement nutzen

---

### FB-26-03-009: Kältemittel-Leck unbekannter Position

**Symptom**: Druckabfall über Nacht ohne Betrieb; niedriger Hochdruck, schwache Kühlung

**Ursachen**:
- Schweißnaht-Risse (Verdichter, Kondensator)
- Schlauch-Abreibung an scharfkantigen Befestigungen
- Korrosion Kupferrohr von innen (Feuchtigkeitskontamination)

**Inspektionspunkte**:
- Sichtprüfung: Öl-Spuren um Rohrleitungen?
- Geruchsprobe: Leichter süßlicher Kältemittel-Duft?
- Halogenid-Lecksucher Messung durchführen (EUR 200–400 Service)

**Behebung**:
1. Lecks mit Halogenid-Detektor lokalisieren (nicht mit Feuer!)
2. System drucklos machen, je nach Leck-Position reparieren:
   - Schlauch-Lecks: Schlauch-Segment austauschen (EUR 120–300)
   - Naht-Lecks: Komponente austauschen (EUR 1,200–3,500)
3. Neuer Trockner + vollständige Kältemittel-Neufüllung (EUR 500–1,200)
4. Drucktest 10 bar, 24 h Ruhe, nochmal prüfen

**Warnsignal**: Wenn Druckabfall >0.5 bar pro Woche, sofort Wartung buchen

---

### FB-26-03-010: Lüfter-Motor defekt (Innenverdampfer)

**Symptom**: Keine Luftzirkulation aus Verdampfer, System läuft aber; schwache Kühlwirkung; kein Betriebsgeräusch

**Ursachen**:
- Salzwasser-Korrosion Lager
- Kondensator-Verschmutzung blockiert Propeller
- Kapazitäts-Kondensator defekt (nur AC-Motoren)

**Inspektionspunkte**:
- Stromversorgung Lüfter prüfen (230V AC, ca. 0.5–1.5 A)
- Propeller sichtbar blockiert?
- Magnetfeld-Test: Eisenschraube an Motorgehäuse sollte anziehen

**Behebung**:
1. Propeller von Schmutz befreien, manuell drehen (sollte leicht gehen)
2. Lüfter-Motor Austausch (EUR 280–550 je Modell)
3. Nach Austausch: neue Isolier-Pads setzen, Vibrationsprüfung

**Lebensdauer**: Typisch 8–12 Jahre bei salziger Luft; Prävention: Jährliche Kontrolle

---

### FB-26-03-011: Elektronik-Modul Feuchtekorrosion (Steuergerät)

**Symptom**: Keine Reaktion auf Fernbedienung; Verdichter läuft permanent oder startet nicht; Anzeigefeld dunkel

**Ursachen**:
- Kondenswasser von feuchter Kabinenluft in Elektronik-Gehäuse
- Salzwasser-Spritzer bei Deck-Installations-Modul
- Mangelnde Belüftung im Elektronik-Schacht

**Inspektionspunkte**:
- Sichtprüfung: Grüne Oxidflecken auf Platinen?
- Leckageprüfung Elektronik-Gehäuse: Wasserspuren innen?
- Steckerverbindungen: Kontakt-Korrosion weiße Flöckchen?

**Behebung**:
1. Elektronik-Modul ausbau, mindestens 48 h bei 30°C Wärmeschrank trocknen
2. Kontakte mit Kontaktspray reinigen
3. Gehäuse-Dichtungen ersetzen (EUR 25–50)
4. Entlüftungs-Öffnung kontrolliert vergrößern
5. Modul wieder einbauen, alle Funktionen testen

**Ersatz nötig, wenn**: Nach Trocknung keine Funktion → Platinen-Austausch (EUR 600–1,200)

**Prävention**: Elektronik-Gehäuse oberhalb Wasserlinie montieren; jährliche Inspektion

---

### FB-26-03-012: Drosselventi-Vereisungs (TXV blockiert)

**Symptom**: Verdichter läuft, Verdampfer Ausgangsdruck fällt auf 0 bar; keine Kühlung; Sicherheitsschalter nach 2–3 min aus

**Ursachen**:
- Wasser im System (Feuchte im Kältemittel): bildet Eiskristalle am TXV-Ventil
- TXV-Fühler verunreinigt oder abgerissen
- Niedriges Öl-Niveau → Schmierung mangelhaft

**Inspektionspunkte**:
- Tiefdruckmeter während Betrieb: sollte 2–4 bar bleiben
- Wenn Druck rapide auf 0 fällt: TXV blockiert
- Fühler-Draht visuell prüfen: sollte fest angebracht sein

**Behebung**:
1. Verdichter stoppen, System 30 min ruhen lassen, erneut starten
2. Falls Problem bestehen bleibt: Trockner ersetzen (EUR 180–300)
3. Komplette Kältemittel-Neu-Befüllung mit Feuchte-Absorption
4. TXV-Ventil-Sonde neu justieren oder ersetzen (EUR 220–420)

**Prävention**: Trockner alle 2 Jahre austauschen (keine "Auf-Sicht"-Wartung möglich)

---

## 7. Troubleshooting-Bäume

### 7.1 Baum: "Verdichter startet nicht"

```
START: Verdichter startet nicht

├─ Stromversorgung prüfen
│  ├─ Sicherung/FI-Schalter ausgelöst? → Sofort ersetzen/zurückschalten
│  ├─ Spannungsprüfer 220/380V? → Strommesser anschließen (0.5–15A Normal)
│  └─ → Wenn keine Spannung: Verteiler/Schalt prüfen (Elektrik-Spezialist)
│
├─ Druckschalter-Status
│  ├─ Hochdruck >30 bar? (Überheizung) → FB-26-03-007 siehe
│  ├─ Tiefdruckschalter aktiviert? (Kältemittel leer?) → Drucktest durchführen
│  └─ → Schalter mit Prüfgerät überwachen
│
├─ Elektronik-Modul
│  ├─ Fernbedienung: hat sie Batterie? → Austausch
│  ├─ Anzeigefeld dunkel? → FB-26-03-011 Feuchtekorrosion
│  └─ → Modul-Austausch notwendig (EUR 600–1200)
│
└─ ENDE: Fachmann kontaktieren wenn oben nicht geholfen

```

### 7.2 Baum: "Schwache Kühlung / Keine Kühlwirkung"

```
START: Schwache oder keine Kühlung

├─ Verdichter läuft?
│  ├─ NEIN → siehe Baum 7.1 (Verdichter startet nicht)
│  └─ JA → weiter
│
├─ Seewasser-Durchfluss prüfen
│  ├─ Wasser fließt aus Auslassrohr? → Durchfluss messen (sollte 1.5+ l/min pro 10 kBTU)
│  ├─ Zu wenig? → FB-26-03-003 (Filter verstopft) oder FB-26-03-004 (Rostung)
│  ├─ Seacock geschlossen? → Öffnen
│  └─ → wenn immer noch schwach: Rohre spülen (EUR 400–800)
│
├─ Verdampfer-Luftdurchfluss
│  ├─ Lüfter läuft? → Hören Sie "Brummen"?
│  ├─ NEIN → FB-26-03-010 (Lüfter defekt)
│  ├─ JA aber Luft schwach → Luftfilter verstopft? → Austausch EUR 30–80
│  └─ → Luftauslassöffnung blockiert? → Frei machen
│
├─ Verdichter-Druck prüfen (mit Manometer)
│  ├─ Hochdruck <15 bar? → FB-26-03-002 (Luftblase/Kältemittel-Fehler)
│  ├─ Hochdruck >30 bar? → FB-26-03-007 (Hochdruck-Schalter)
│  └─ Normal 18–25 bar? → weiter
│
├─ Verdampfer-Oberfläche prüfen
│  ├─ Sichtbar vereist? (weiß)
│  ├─ JA (Wärmepumpe) → FB-26-03-008 (Vereisung)
│  ├─ JA (reine Kühlung) → FB-26-03-012 (TXV blockiert)
│  └─ Nein → System-Temperatur OK
│
└─ ENDE: wenn oben alles OK → Kältemittel-Leck vermuten (FB-26-03-009)

```

### 7.3 Baum: "System läuft ständig / Thermostat reagiert nicht"

```
START: Verdichter läuft ständig, Temperatur wird nicht erreicht

├─ Thermostat-Sollwert prüfen
│  ├─ Ist-Temperatur gemessen (Raumthermometer)? 
│  ├─ Ist > Sollwert? → Falsche Einstellung? → Sollwert zurücksetzen (20–24°C Standard)
│  └─ Ist deutlich unter Sollwert? → FB-26-03-006 (Thermostat/Fühler-Fehler)
│
├─ Verdampfer-Luftstrom
│  ├─ Tritt kalte Luft aus Ausblasöffnung aus? 
│  ├─ NEIN → Luftmenge zu niedrig (FB-26-03-010 Lüfter) oder Kanal blockiert
│  └─ JA → Verdampfer arbeitet, aber thermisch schwach
│
├─ Raumwärme-Eintrag prüfen
│  ├─ Sonneneinstrahlung zu stark? → Jalousien/Vorhänge schließen
│  ├─ Motor läuft? → Motorwärme (bis 25 kBTU) → Motor abstellen
│  ├─ Zu viele Personen/Elektronik? → Personenzahl/Geräte reduzieren
│  └─ → Ggfs. zusätzliche AC-Unit installieren notwendig
│
├─ Kältemittel-Menge prüfen
│  ├─ Hochdruck <12 bar? → Kältemittel zu niedrig (FB-26-03-002)
│  ├─ Druckabfall über Nacht? → Leck vermuten (FB-26-03-009)
│  └─ Drucke normal? → System OK thermal
│
└─ ENDE: Verdichter ständig Dauerbetrieb normal wenn Sollwert nicht erreichbar

```

### 7.4 Baum: "Lautstärke-Problem / Unerwartetes Geräusch"

```
START: System läuft, aber zu laut oder unerwartetes Geräusch

├─ Geräusch-Charakterisierung
│  ├─ "Brummen" (normal 50–70 dB) → OK, Standard-Betrieb
│  ├─ "Pfeifton" hoch → FB-26-03-005 (Verdichter-Verschleiß) SOFORT STOPPEN
│  ├─ "Schleifen" metallisch → FB-26-03-005 (Fremdkörper) SOFORT STOPPEN
│  ├─ "Klick-Klick" rhythmisch → Normal bei Defrost (Wärmepumpe) oder Druckschalter
│  ├─ "Gluckern" → Luftblase (FB-26-03-002) oder Wasser im Saugrohr
│  └─ "Rattern" → Propeller-Schlag oder lockere Befestigung
│
├─ Nach Geräusch-Typ reagieren
│  ├─ HIGH-PITCH/SCHLEIFEN → System SOFORT abschalten, Fachmann anrufen (Tag)
│  ├─ KLICK rhythmisch → Schalter normal → Betrieb OK, beobachten
│  ├─ GLUCKERN → Kältemittel-Umlauf Problem (Leck? Zu viel Öl?) → Drucktest
│  ├─ RATTERN → Befestigungen überprüfen, Vibrationspads austausch (EUR 50–120)
│  └─ NORMAL BRUMMEN → Keine Aktion notwendig
│
└─ ENDE: Bei Unsicherheit Betriebsstunden-Zähler notierten (Vorlauf-Abnutzung tracken)

```

### 7.5 Baum: "Wasser/Lecks beobachtet"

```
START: Wasser oder Flüssigkeits-Lecks beobachtet

├─ Art des Lecks bestimmen
│  ├─ Salzwasser (Seewasser-Schlauch)?
│  │  ├─ JA → FB-26-03-001 (Schlauch-Risse/Korrosion) → Sofort absperren
│  │  └─ Notfall-Verschluss: Seacock schließen, System aus
│  │
│  ├─ Süßwasser oder ölig (Kältemittel-Öl)?
│  │  ├─ JA → FB-26-03-009 (Kältemittel-Leck) → Verdichter aus
│  │  └─ Leck-Position mit Halogenid-Detektor finden lassen (EUR 200–400)
│  │
│  └─ Kondenswasser unter Verdampfer (normal)?
│     ├─ JA, aber Menge >1 L/h? → Drainage blockiert → Rohr frei machen
│     └─ Normal <200 mL/h in tropischen Breiten
│
├─ Notfall-Maßnahmen
│  ├─ System ausschalten
│  ├─ Seacock absperren (falls Salzwasserleck)
│  └─ Wassereimer unter Leck stellen
│
└─ ENDE: Reparatur nur mit zertifiziertem Techniker durchführen (Kältemittel-Handhabung)

```

---

## 8. Häufig Gestellte Fragen (FAQ)

### 8.1 Energieverbrauch & Betriebskosten

**F: Wie viel Strom verbraucht eine marine AC typischerweise?**
A: 1.5–2 kW für 5–10 kBTU Deck-Unit; 4–6 kW für 15–24 kBTU Split; 8–15 kW für Chilled-Water. Bei Generator: ca. 0.5–1 l/h Diesel extra Verbrauch.

**F: Kostet es weniger, die AC nachts auszuschalten?**
A: Ja. Nachtkühlung spart 30–50 % Energie wenn Außentemperatur <18°C. Programmierbar Nachtmodus auf Fernbedienung.

**F: Kann ich AC mit Solar+Batterie betreiben?**
A: Für kleine Deck-Unit (5 kBTU) ja mit großer Batterie (200+ Ah LiFePO4). Für Split/Chilled-Water brauchst Generator oder Landstrom.

---

### 8.2 Installation & Wartung

**F: Wie oft muss der Seewasser-Filter gereinigt werden?**
A: Monatlich in Normalgewässern; wöchentlich in tropischen/trüben Gewässern; täglich in Flussdeltas mit Algenblüten.

**F: Kann ich AC-System selbst installieren?**
A: Nein. Kältemittel-Umgang erfordert Zertifikation (§11a KälteV Deutschland). Kosten EUR 200–400 für sachgerechte Befüllung. Rohrleitungs-Verlegung können Bootsingenieure selbst durchführen.

**F: Wie lange hält ein Verdichter?**
A: 8–15 Jahre je nach Betriebsdauer, Wartung, Salzwasser-Exposition. Betriebsstunden-Zähler sollte überwacht werden.

**F: Muss ich AC im Winter abstellen?**
A: Ja, wenn Seewassertemperatur <3°C. Kondensator friert zu → Hochdruck-Schalter löst aus. Seacock absperren, System drucklos machen für Lagerung.

---

### 8.3 Reparaturen & Fehlersuche

**F: Warum kühlt AC nicht, obwohl Verdichter läuft?**
A: (1) Kältemittel-Leck, (2) Seewasser-Filter verstopft, (3) Verdampfer-Lüfter defekt, (4) Thermostat/Fühler falsch. In dieser Reihenfolge diagnostizieren.

**F: Was kostet ein Kältemittel-Leck-Reparatur?**
A: EUR 400–1,500 je nach Position. Schlauch-Segment: EUR 120–300. Kondensator/Verdichter-Naht: EUR 1,200–3,500 + Neubefüllung EUR 500–1,000.

**F: Kann ich Kältemittel selbst nachfüllen?**
A: Nein, verboten ohne Zertifikat (§11a KälteV). Fachmann muss Menge & Öl-Verhältnis exakt berechnen. Überladung führt zu Hochdruck-Schaden (EUR 2,500+ Verdichter-Austausch).

**F: Was bedeutet "nicht beurteilbar" in Diagnose-Bericht?**
A: System zu alt/verschmutzt oder Messgeräte fehlerhaft zur zuverlässigen Diagnose. Verdichter-Austausch kann nicht vermieden werden.

---

### 8.4 Wärmepumpen (Heiz+Kühl)

**F: Wie funktioniert Reverse-Cycle-Heizung?**
A: 4-Wege-Ventil schaltet Kältemittel-Fluss um: Im Heizbetrieb wird Seewasser-Wärme genutzt (auch bei <5°C). Verdichter-Arbeit heißer machen = COP 2–3.

**F: Bei welcher Wassertemperatur kann Wärmepumpe nicht mehr heizen?**
A: Effektiv <2°C. Darunter wird Verdampfer-Vereisungs-Defrost-Zyklus zu häufig, COP fällt unter 1 → unwirtschaftlich. Sinn: nur bis +5°C Seewasser.

**F: Kostet Wärmepumpen-Heizung weniger als elektrisches Heizelement?**
A: Ja, COP 2.5 = 40 % weniger Stromverbrauch. Aber teurer Systemkauf (+EUR 3,000–8,000 vs. Deck-Unit). Amortisierung 5–10 Jahre.

---

### 8.5 Häufige Fehler bei Auslegung

**F: "Ich habe 10 kBTU AC für 20m Yacht – reicht das?"**
A: Nein. Zu schwach. Regel: 500–800 BTU/h pro m² Kabinen-Volumen. 20m Yacht ~100 m³ Kabinen = 50,000–80,000 BTU benötigt. 10 kBTU ist für Notfallbetrieb nur.

**F: Kann ich mehrere kleine AC-Units statt eine großen nehmen?**
A: Ja, technisch möglich. Aber teurer in Anschaffung (+40 %) und Wartung (mehrere Seawater-Filter, Verdichter). Nur wenn Zonen-Unabhängigkeit wichtig ist.

**F: Brauche ich zwei ACs für Redundanz?**
A: Nur für Großyachten >40m oder wenn Betrieb-Sicherheit kritisch. Kosten-Nutzen meist ungünstig für Privat-Yachten.

---

### 8.6 Tipps für längere AC-Lebensdauer

**F: Wie kann ich AC-Lebensdauer verlängern?**
A:
1. Seewasser-Filter monatlich reinigen (wichtigste Maßnahme)
2. Verdichter-Betriebsstunden-Log führen (bei >10.000 h Vorsorge-Wartung)
3. Trockner alle 2 Jahre austausch (ca. EUR 180–300)
4. Winterlagerung: Seacock absperren, System drucklos
5. Jährliche Hochdruck-Prüfung vor Sommer-Saison

**F: Was ist "Preventive Maintenance Paket"?**
A: Jährlich EUR 600–1,200 (Dometic/Webasto Verträge). Alle Filter austausch, Druck-Testung, Kältemittel-Analyse. Spart ca. EUR 2,500–5,000 Notfall-Reparaturen.

---

### 8.7 Regulatorische Fragen

**F: Muss AC CE-zertifiziert sein?**
A: Ja für EU-Verkauf. Typischerweise bereits vom Hersteller erfüllt. Prüfen Sie das Zertifikat beim Kauf (Modellnummer, Datum, notified body).

**F: Darf ich R410A durch R32 ersetzen?**
A: Nur mit Systemoptimierung vom Hersteller. R32 hat höheren Druck (bis 32 bar vs. 28 bar). Rohrleitungen/Schläuche müssen ertüchtigt sein. Nicht einfach "auffüllen".

**F: Gibt es Entsorgungspflichten für Alt-Systeme?**
A: Ja. Alte Verdichter mit R22 müssen zu zertifiziertem Recycler. Kosten EUR 100–300. Nie einfach entsorgen (Umweltschutz, Bußgeld bis EUR 10,000).

---

## 9. Glossar

| Begriff | Definition |
|---------|-----------|
| **BTU** | British Thermal Unit – 1 BTU = 0.293 Watt Kühlleistung; 1 kBTU = ca. 300 W |
| **COP** | Coefficient of Performance – Verhältnis Kühlleistung : Stromverbrauch; COP 3.5 = 3.5 kW Kühlung für 1 kW Strom |
| **Defrost-Zyklus** | Automatische Umschaltung im Heizbetrieb, wenn Verdampfer vereist; heiße Gase spülen Eis auf |
| **DIN EN 378** | Deutsche/Europäische Norm für Kälte- und Wärmepumpen-Sicherheit |
| **Drosselventil / TXV** | Thermostatic eXpansion Valve – reguliert Kältemittel-Durchfluss zum Verdampfer |
| **Dynes** | Einheit für Oberflächenspannung (Material-Test für Steckerkompatibilität) |
| **GWP** | Global Warming Potential – Treibhauswirkungs-Faktor des Kältemittels (R410A: 2087, R32: 677) |
| **Hochdruck-Schalter** | Sicherheitselement – schaltet Verdichter ab wenn Druck >30 bar (Überhitzung/Fehler) |
| **Kältemittel** | Arbeitsflüssigkeit im Kühlzyklus (R410A, R32, R290, etc.) |
| **KälteV** | Kälteverordnung Deutschland – Zertifizierungspflicht für Kältemittel-Handhabung |
| **Kondensator** | Wärmetauscher, in dem Kältemittel-Dampf zu Flüssigkeit verflüssigt wird (mit Seewasser gekühlt) |
| **MARPOL** | International Maritime Pollutant Regulations – IMO-Standard für Umweltschutz auf Schiffen |
| **Marelon** | Kunststoff-Rohrmaterial (PEX-ähnlich), korrosionsfest für Seewasser |
| **NRTL** | Nationally Recognized Testing Lab – Zertifizierungsstelle für Elektro-Sicherheit |
| **ODP** | Ozone Depletion Potential – Ozonabbau-Faktor (R22: 0.055, R410A: 0) |
| **Seacock** | Absperrhahn für Seewasser-Einlass; muss regelmäßig übung-betätigt werden |
| **Seewasser-Filter** | Filterpatronen 100–500 µm zum Schutz vor Muschelwuchs und Verschmutzung |
| **Süperheizung** | Temperatur-Unterschied zwischen Verdampfer-Ausgang und Fühler-Lage (Normal 5–10 K) |
| **Tiefdruckschalter** | Sicherheit – schaltet Verdichter ab wenn Druck <2 bar (Kältemittel leer/Leck) |
| **Verdampfer** | Wärmetauscher, wo Kältemittel verdunstet und Wärme aus Kabinen-Luft aufnimmt |
| **Verdichter / Kompressor** | Pumpe, die Kältemittel-Dampf verdichtet und zirkuliert (Herz des Systems) |
| **4-Wege-Ventil** | Umschaltventil in Wärmepumpen zwischen Heiz-/Kühl-Modus |

---

## 10. Schnell-Referenztabellen

### 10.1 Dimensionierungshilfe

| Yacht-Länge | Kabinen-Volumen (m³) | Empfohlen BTU | Split oder Deck-Unit? | Stromversorgung |
|-----------|-------|----------|------------|---------|
| 7m | 15 | 7,500–10,000 | Deck-Unit | 220V/13A |
| 10m | 25 | 12,000–15,000 | Split | 220V/16A |
| 15m | 50 | 20,000–25,000 | Split | 380V/18A |
| 20m | 80 | 40,000–50,000 | Chilled-Water | 380V/25A |
| 30m | 150 | 60,000–80,000 | Chilled-Water + Redundanz | 3-Phase/40A |

### 10.2 Wartungsintervalle

| Maßnahme | Intervall | Kosten EUR | Kritikalität |
|---------|-----------|-----------|-------------|
| Seewasser-Filter Reinigung | Monatlich | 0 (Eigenleistung) | **KRITISCH** |
| Filter-Kartridge Austausch | 12 Monate | 80–120 | Hoch |
| Drucktest + Dichtheitssprüfung | 12 Monate | 200–350 | Hoch |
| Trockner Austausch | 24 Monate | 180–300 | Mittel |
| Kältemittel-Analyse (Öl-Feuchte) | 24 Monate | 150–250 | Mittel |
| Verdichter-Inspektion (Vibration/Ton) | 36 Monate | 200–400 | Mittel |
| Komplette Servicerevision | 60 Monate / >10.000 Std | 800–1,500 | Hoch |

### 10.3 Fehler-Priorisierung

| Fehler | Symptom | Aktion | Zeitrahmen |
|--------|---------|--------|-----------|
| **Verdichter-Schleifen (FB-26-03-005)** | Pfeif-/Schleiftöne | SOFORT ausschalten | Heute |
| **Seewasserleck (FB-26-03-001)** | Salzwasser tropfend | Seacock zu, System aus | Heute |
| **Hochdruck >32 bar (FB-26-03-007)** | Sicherheitsschalter aus | Abkühlen, Filter prüfen | 1–2 Tage |
| **Kältemittel-Leck (FB-26-03-009)** | Druckabfall nachts | Fachmann anrufen | 1 Woche |
| **Verdampfer-Vereisung (FB-26-03-008)** | Keine Heizung | Defrost-Zyklus aktivieren | 1–2 Tage |
| **Thermostat-Fehler (FB-26-03-006)** | Temperatur-Überschuss | Fühler prüfen | 1 Woche |
| **Lüfter defekt (FB-26-03-010)** | Keine Luftzirkulation | Verdichter weiter, Lüfter-Austausch | 2–3 Wochen |

---

## Anhang A: Rohrleitungs-Planungsleitfaden

### A.1 Rohrmaterialien und Größen

**Seewasser-Rohrleitungen:**
- Material: Kunststoff Marelon oder Trident (NICHT Kupfer direkt)
- Durchmesser: 19 mm (3/4") Standard für 5–15 kBTU; 25 mm für >20 kBTU
- Isolierung: 10 mm Polyurethan minimum (verhindert Kondenswasserbildung)
- Befestigung: Kunststoff-Schellen alle 0.5 m, Vibrationsdämpfer an Maschinenanbindung

**Kältemittel-Rohrleitungen (Kupfer):**
- Durchmesser: 3/8" (9.5 mm) für <20 kBTU; 1/2" (12.7 mm) für >20 kBTU
- Typ: Marinekupfer, nicht Normalrohr
- Isolierung: Polyurethan 10–25 mm (durchgehend, auch Strahl-Schnitte)
- Max. Länge: 25 m vom Verdichter zu Innen-Verdampfer; >25 m erfordert Öl-Rücklauf-Konstruktion

**Wasser-Leitungen (Chilled-Water):**
- Material: Kunststoff PEX oder Kupfer mit Isolierung
- Durchmesser: 16–20 mm Standard
- Durchfluss: 0.3–0.5 l/s pro Verdampfer

### A.2 Verlegungsrichtlinien

- **Zu Motor-Bereichen Abstand**: Mind. 1 m von heißen Flächen (Motor, Auspuff)
- **UV-Schutz**: Rohre nicht direkter Sonne auf Deck aussetzen (Kunststoff degeneriert nach 3–5 Jahren)
- **Vibrations-Puffer**: Polyurethan-Schaumstoffe an allen Durchdringungspunkten (Motormount-Nähe)
- **Drainage nach Unten**: Seewasser-Rohre sollten leicht fallend verlaufen (1 cm pro Meter) für Druckentlastung
- **Kältemittel-Rohre nach Oben**: Rücklauf-Rohr (Innenrohr) muss Öl-Rückkehr ermöglichen

---

## Anhang B: Elektrik-Integration

### B.1 Stromverteilung

**Deck-Unit (5–12 kBTU, 220V Einphasig):**
- Schaltkreis 16A (2.5 mm² Kupfer-Kabel) mit 16A FI-Schalter
- Keine Drehzahlregelung typisch
- Batterie-Puffer: 100 Ah LiFePO4 minimum für unkritische 2–3 h Betrieb

**Split-System (15–24 kBTU, 220/380V):**
- 220V: Schaltkreis 20A (4 mm²)
- 380V 3-Phase: 16A pro Phase (Stern-Schaltung Verdichter)
- FI-Schalter 30 mA Typ A (für Frequenz-umrichter kompatibel)
- Generator minimum 8 kVA (überdimensionieren um 20 %)

**Chilled-Water (>24 kBTU, 380V 3-Phase):**
- 32–63A je Anlage, entsprechendes Kabel (6–10 mm²)
- Seperate Verdichter-Zuleitung mit Thermoschalter (Motorschutz)
- Umwälzpumpe meist 1–2 kW: auf separatem Schaltkreis

### B.2 Notfall-Verdrahtung

- Fernbedienung sollte mit Batterie-Backup ausgestattet sein
- Automatische Abschalt-Logik bei Seacock-Fehler (Sensor-Input)
- Hochdruck/Tiefdruckschalter-Ausgang zu Alarmsystem verdrahten

---

## Anhang C: Service-Checklisten

### C.1 Wöchentliche Kontrolle (Nutzer selbst)

- [ ] Seewasser-Auslass-Durchfluss prüfen (sollte 2–3 L/min fließen)
- [ ] Verdampfer-Luftauslassgitter auf Blockieren prüfen
- [ ] Verdichter-Betriebsgeräusch auf Änderungen hören
- [ ] Innentemperatur-Sollwert nach Außentemperatur anpasssen

### C.2 Monatliche Filter-Reinigung

1. Seacock öffnen (falls geschlossen)
2. Filter-Druckanzeiger prüfen (sollte <0.3 bar sein)
3. Falls >0.5 bar: Filtergehäuse demontieren
4. Kartridge unter Süßwasser spülen (nicht Hochdruck >80 bar)
5. Gehäuse & Dichtungen optisch prüfen
6. Wieder zusammenbauen, 5 min Leerfahrt prüfen
7. Seacock wieder öffnen nach Wartung

### C.3 Jährliche Wartung (Fachmann)

1. Hochdruckmanometer: 18–25 bar bei Normalbetrieb?
2. Tiefdruckmanometer: 2–4 bar bei Normalbetrieb?
3. Flüssigkeitsstandsprüfung (falls sichtbar)
4. Kältemittel-Undichtigkeitsprüfung mit Halogenid-Detektor
5. Vibrations-Test Verdichter (manuell: sollte gleichmäßig "brummen")
6. Trockner-Konditionsprüfung (falls Sichtfenster vorhanden)
7. Befestigungen & Schlauch-Integrität prüfen

---

## Anhang D: Kältemittel-Datenblätter

### D.1 R410A (Legacy, Phase-out 2030)

- **GWP**: 2,087
- **Siedepunkt**: –51.4°C
- **Kritischer Druck**: 49.1 bar
- **Betriebsbereich**: –20 bis +60°C
- **Typische Lademenge**: 2–6 kg System
- **Kosten**: EUR 12–18/kg
- **Sicherheitsklasse**: A1 (nicht brennbar, wenig toxisch)

### D.2 R32 (Modern, bis 2050+)

- **GWP**: 677 (niedrig)
- **Siedepunkt**: –51.7°C
- **Kritischer Druck**: 57.8 bar (höher als R410A!)
- **Betriebsbereich**: –20 bis +60°C
- **Typische Lademenge**: 1.5–4 kg System (weniger Menge nötig)
- **Kosten**: EUR 18–25/kg (teurer, aber effizienter)
- **Sicherheitsklasse**: A2L (mildly flammable – zusätzliche Sicherheitsmaßnahmen)
- **Umstieg**: Rohrleitungen ertüchtigung notwendig (höherer Druck!)

### D.3 R290 (Propan, Low-GWP, Nische)

- **GWP**: 3 (minimal)
- **Siedepunkt**: –42.1°C
- **Kritischer Druck**: 42.5 bar
- **Sicherheitsklasse**: A3 (brennbar! – besondere Handhabung)
- **Anwendung**: Nur spezialisierte Systeme mit Sicherheits-Überdruckventil
- **Bootseinsatz**: Sehr selten; hauptsächlich Forschung/Expedition

---

## Anhang E: Visuelle Fehleridentifikation

### E.1 Farbtabelle – Normal vs. Fehler

| Komponent | Normal | Fehler | Konsequenz |
|-----------|--------|--------|-----------|
| **Kondensator-Auslass (Seewasser)** | Farblos, 25–28°C | Braun/rot Eisen; >35°C | Verstopfung, Korrosion |
| **Verdampfer-Oberfläche** | Silber-blank, leicht feucht | Weiß vereist; braun verschmutzt | Vereisung (Heizmode); Luft-Blockade |
| **Schlauchoberfläche (Seewasser)** | Klar transparent | Trüb/gelb; Risse sichtbar | Verott, kritisch Leck |
| **Hochdruckrohr (Kupfer)** | Gold-Kupferfarbe | Schwarz angelaufen; Grün-Patina | Oxidation (OK normal) aber Grün = Leck-Indiz |
| **Ölfenster (falls vorhanden)** | Bernsteinfarben | Dunkelbraun/schwarz; trüb | Öl-Verschleiß; Wasser-Kontamination |
| **Lüfterblatt (Verdampfer)** | Silber, glatt | Braun Verschmutzung; Verformung | Luftstrom-Blockade |

---

## Anhang F: Ersatzteil-Katalog (Beispiele)

| Teil | Modell | Kosten EUR | Haltbarkeit |
|------|--------|-----------|------------|
| Seewasser-Filter-Kartridge | Std. 100 µm | 80–120 | 12 Monate |
| Trockner | Standard | 180–300 | 24 Monate |
| Seewasser-Schlauch (10 m) | Marelon 25mm | 150–250 | 8–10 Jahre |
| Kältemittel R410A | 1 kg Dose | 12–18 | – (Gase) |
| Kältemittel R32 | 1 kg Dose | 18–25 | – |
| Verdichter (Komplettaustausch) | Dometic 20 kBTU | 2,800–3,500 | 10–15 Jahre |
| Thermostatic Expanstion Valve (TXV) | Standard | 220–420 | 12–20 Jahre |
| Lüfter-Motor (Verdampfer) | 230V AC 50Hz | 280–550 | 8–12 Jahre |
| 4-Wege-Schalt-Ventil (Wärmepumpe) | Solenoid | 350–550 | 10–15 Jahre |

---

## Anhang G: Fehlerhafte Designs – Was zu vermeiden ist

### G.1 Häufige Installationsfehler

1. **Seawaterfilter zu weit weg vom Meer-Ansaugstelle**: Rohrlänge >5 m führt zu Druckabfall und Saugseite-Unterdruck. Filter sollte max. 2–3 m entfernt vom Seacock sein.

2. **Kältemittel-Rohre ohne Isolierung verlegt**: Wärmeverluste an feuchter Luft (besonders in Kabinen). Ergebnis: schwache Kühlung, Kondenswasser-Bildung auf Rohren.

3. **Verdichter auf vibrierende Motor-Sätzblock montiert**: Resonanzschwinungen 50–70 Hz. Rohre zerknicken nach 2–3 Jahren. Lösung: Elastische Entkopplung mit Gummi-Füßen.

4. **Seacock im Salon platziert, nicht im Maschinenschacht**: Weniger Zugänglichkeit, höhere Verschmutungs-Wahrscheinlichkeit. Seacock sollte im Maschinenraum direkt am Rumpfdurchgang sein.

5. **Verdampfer-Lüfter ohne Vibrationsdämpfer**: Lautstärke-Problem 70+ dB, Risse in Gehäuse nach 2–3 Jahren.

### G.2 Fehlerhafte Auslegung

- **Zu kleine Kältemittel-Rohre**: Geschwindigkeiten >3.5 m/s führen zu Druckabfall und "Pumpverlust" (COP sinkt von 3.8 auf 2.5)
- **Zu lange Rohrstrecken**: >25 m ohne Öl-Rücklaufkonstruktion → Verdichter-Verschleiß
- **Seewasser-Rohre zu dünn**: <19 mm für 10+ kBTU → Filter-Verstopfung rascher

---

## Anhang H: Regional-Spezifika

### H.1 Tropische Gewässer (>25°C konstant)

- **COP-Degradation**: Seewasser-Kühler wird ineffektiver bei >28°C Wassertemperatur
- **Biofilm-Risiko**: Monatliche Filter-Kontrolle NICHT ausreichend; wöchentlich empfohlen
- **Stromverbrauch**: +30–40 % höher als gemäßigte Breiten
- **Dauer-Betrieb**: System für 16+ h/Tag ausgelegt (Redundanz erwägen)

**Empfehlung**: UV-Kläranlage im Seewasser-Einlass (zusätzlich EUR 1,500–3,000) zur Biofilm-Prävention

### H.2 Kalt-Winter (<0°C)

- **Heizmode-Betrieb**: Verdampfer-Vereisung bei Defrost-Zyklus >30 min pro Stunde
- **Effizienz-Verlust**: COP sinkt auf 1.5–1.8 (elektrisches Heizelement effizienter)
- **Betriebspause**: System sollte bei <2°C Seewasser abgestellt werden

**Empfehlung**: Wärmepumpen-Installation für gemäßigte Winter + elektrisches Backup-Heizelement

### H.3 Brackwasser-Deltagebiete

- **Filterverbrauch**: 3–4× höher (algenreich, Sediment)
- **Korrosion**: Galvanische Effekte verstärkt durch niedrigeren Salzgehalt
- **Lagerung**: Verdichterkühlung notwendig auch im Winterhafen (Algenwachstum aktiv)

**Empfehlung**: Filtersystem mit 2–3 Kartridgen zur Rotation; monatliche Wechsel; Anti-Biofilm-Additive

---

## Anhang I: Pydantic v2 Datenmodelle

### I.1 Klimaanlage-Inspektionsmodell

```python
from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional, List

class SystemType(str, Enum):
    DECK_UNIT = "deck_unit"
    SPLIT = "split"
    CHILLED_WATER = "chilled_water"
    HEAT_PUMP = "heat_pump"

class ConditionStatus(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"

class ClimateSystemInspection(BaseModel):
    model_config = {"from_attributes": True}
    
    inspection_id: str = Field(..., min_length=3, description="Unique inspection ID")
    boat_name: str
    system_type: SystemType
    installation_year: int = Field(..., ge=1990, le=2026)
    btu_rating: int = Field(..., gt=0, description="Cooling capacity in BTU")
    
    # Pressure readings
    high_pressure_bar: float = Field(..., ge=10, le=40, description="Hochdruck in bar")
    low_pressure_bar: float = Field(..., ge=0.5, le=10, description="Tiefdrück in bar")
    
    # Operational metrics
    seawater_flow_rate_lpm: float = Field(..., gt=0, description="Durchfluss in l/min")
    evaporator_temperature_celsius: Optional[float] = None
    condenser_outlet_celsius: Optional[float] = None
    
    # Condition assessment
    compressor_condition: ConditionStatus
    seawater_filter_condition: ConditionStatus
    refrigerant_line_condition: ConditionStatus
    evaporator_condition: ConditionStatus
    
    # Error findings
    errors_detected: List[str] = Field(default_factory=list)
    critical_findings: List[str] = Field(default_factory=list)
    
    inspection_date: datetime
    next_service_date: datetime
    
    @field_validator('btu_rating')
    @classmethod
    def validate_btu_range(cls, v: int) -> int:
        if v < 5000 or v > 120000:
            raise ValueError('BTU muss zwischen 5.000 und 120.000 liegen')
        return v
    
    @field_validator('high_pressure_bar')
    @classmethod
    def validate_high_pressure(cls, v: float, info) -> float:
        if v > 30:
            raise ValueError('Hochdruck >30 bar: Fehlercode FB-26-03-007')
        return v

class ServiceRecord(BaseModel):
    model_config = {"from_attributes": True}
    
    service_id: str
    inspection: ClimateSystemInspection
    performed_by: str
    actions_taken: List[str]
    parts_replaced: List[str] = Field(default_factory=list)
    total_cost_eur: float = Field(ge=0)
    hours_logged: float = Field(ge=0)
    completion_date: datetime
```

### I.2 Fehler-Katalog-Modell

```python
class ErrorFinding(BaseModel):
    model_config = {"from_attributes": True}
    
    error_code: str = Field(..., pattern=r'^FB-26-03-\d{3}$')
    error_name: str
    severity: str = Field(..., pattern='^(critical|high|medium|low)$')
    symptoms: List[str]
    root_causes: List[str]
    remediation_steps: List[str]
    estimated_cost_eur: float
    estimated_hours: float
    prevention_measures: List[str] = Field(default_factory=list)

class SystemDiagnosis(BaseModel):
    model_config = {"from_attributes": True}
    
    diagnosis_id: str
    system_id: str
    errors: List[ErrorFinding]
    overall_health_score: int = Field(ge=0, le=100)
    recommended_actions: List[str]
    urgency: str = Field(..., pattern='^(emergency|urgent|scheduled|monitoring)$')
```

---

## Anhang J: Kältemittel-Physik (Referenz für Ingenieure)

### J.1 Zustandsdiagramm-Interpretation

**Mollier h-lg Diagramm Ablesung (R410A Beispiel):**

Hochdruckseite (Kondensator): 
- Punkt A (Verdichter-Auslass): h ≈ 430 kJ/kg, p ≈ 25 bar, T ≈ 60°C (überhitzt)
- Punkt B (Kondensator-Ausgang): h ≈ 235 kJ/kg, p ≈ 25 bar, T ≈ 30°C (unterkühl)

Tiefdruckseite (Verdampfer):
- Punkt C (nach Drosselventil): h ≈ 235 kJ/kg (gleich wie B, isenthalp)
- Punkt D (Verdampfer-Ausgang): h ≈ 405 kJ/kg, p ≈ 3 bar, T ≈ 0°C (überhitzt)

**Energiebilanz:**
- Kühlleistung = h_D – h_C = 405 – 235 = 170 kJ/kg
- Verdichter-Arbeit = h_A – h_D = 430 – 405 = 25 kJ/kg
- COP = 170 / 25 = 6.8 theoretisch (real: 3.5–4.0 mit Verlust)

### J.2 Entropie & Temperatur-Gleit

R410A ist ein **Blöcking-Kältemittel** (Azeotrop) → keine Gleittemperatur in Verdampfer/Kondensator.
R407C war früher "Quasi-Azeotrop" → 0.8 K Gleit → relevant für Auslegung.

**Moderne Systeme R410A/R32**: Gleit-Effekt vernachlässigbar, Vereinfachte 1-Temperatur-Auslegung möglich.

---

## Anhang K: Material-Kompatibilitäts-Matrix

| Material | R410A | R32 | R290 | Seewasser | Notizen |
|----------|-------|-----|------|-----------|---------|
| Kupfer (C11000) | ✓ | ✓ | ✓ | ✗ | Elektrolyse mit 316L |
| Edelstahl 316L | ✓ | ✓ | ✓ | ✓ | Best für Marine |
| Aluminium 6061 | ✓ | ✓ | ✓ | ✗ | Nur intern (Wärmetauscher) |
| Kunststoff Marelon | – | – | – | ✓ | Nur Seewasser, nicht Kältemittel |
| Neopren-Dichtung | ✓ | ✓ | ✗ | ✓ | R290 benötigt EPDM |
| Aluminium-Lot (Verdichter) | ✓ | ✓ | ✓ | – | Interne Schweißungen |

---

## Anhang L: Normen-Schnell-Referenz

| Norm | Bereich | Relevanz |
|------|---------|----------|
| **DIN EN 378** | Kälte-Sicherheit | Druckgerät, Rohrleitungs-Dimensionierung |
| **ISO 12217** | Schiffs-Stabilität | Gewichts-Distribution AC-System |
| **ISO 11812** | Cockpit-Sicherheit | Entwässerung (relevant wenn AC-Kondensation) |
| **IMO MARPOL Annex VI** | Luftverschmutzung | Kältemittel-GWP Limits |
| **EU 517/2014** | F-Gas-Verordnung | Kältemittel-Kontingente, Zertifizierung |
| **PED 2014/68/EU** | Druckgeräte | Konformität Verdichter, Kondensator |
| **CE 2013/53/EU** | Boot-Richtlinie | Allgemeine Sicherheit Untersysteme |

---

## Anhang M: Literatur & Quellen

1. Dometic Technical Documentation: Marine Air & Cruisair Product Guides (2024)
2. Webasto SeaComfort Installation & Service Manuals
3. Frigomar Systemhandbuch für Klimaalagen
4. German DIN EN 378:2016 – Sicherheitsvorschriften für Kälteanlagen
5. IMO MARPOL Annex VI Technical Guidelines (2019 Edition)
6. Intergovernmental Panel on Climate Change (IPCC) – Kältemittel GWP Datenbank (2023)
7. EU 517/2014 F-Gas Regulation – Notified Bodies Directory
8. International Maritime Organization (IMO) – SOLAS Chapter II-1: Ship Construction

---

## Anhang N: Akronyme & Abkürzungen

| Akronym | Aussprache | Bedeutung |
|---------|-----------|----------|
| AC | ei-si | Air Conditioning (Klimaanlage) |
| BTU | bi-ti-ju | British Thermal Unit |
| CFC | – | Chlorofluorocarbon (Ozonkiller, VERBOTEN) |
| COP | – | Coefficient of Performance |
| GWP | – | Global Warming Potential |
| HCFC | – | Hydrochlorofluorocarbon (Phase-out 2030) |
| HFC | – | Hydrofluorocarbon (R410A, Phase-out 2030) |
| HFO | – | Hydrofluoroolefin (R1234yf, zukunft) |
| HVAC | hyvac | Heating, Ventilation, Air Conditioning |
| IMO | i-m-o | International Maritime Organization |
| kBTU | – | Kilo-BTU (1.000 BTU) |
| LFL | – | Lower Flammability Limit (für R290, R32) |
| MARPOL | mar-pol | Marine Pollution Regulations |
| ODP | – | Ozone Depletion Potential |
| ORC | – | Organic Rankine Cycle (Wärmenutzung) |
| PED | – | Pressure Equipment Directive |
| ppm | – | parts per million (Feuchte-Messung) |
| PPE | – | Personal Protective Equipment |
| SOLAS | so-las | Safety of Life At Sea |
| TXV | – | Thermostatic eXpansion Valve |
| UV | – | Ultraviolet (Strahlung) |

---

## Anhang O: Temperatur-Konversionen (°C ↔ °F)

| °C | °F |
|----|-----|
| –20 | –4 |
| 0 | 32 |
| 5 | 41 |
| 10 | 50 |
| 15 | 59 |
| 20 | 68 |
| 25 | 77 |
| 30 | 86 |
| 35 | 95 |
| 40 | 104 |

**Schnell-Merksatz**: °F = °C × 1.8 + 32

---

## Anhang P: Betriebsstunden-Trackings-Format

```
BETRIEBSSTUNDEN-PROTOKOLL Klimaanlage
Yacht: ___________________
System: ___________________  BTU: _______

Datum | Stunden | Betriebsmodus | Hochdruck bar | Tiefdrück bar | Notiz
------|---------|---------------|---------------|---------------|------
Jan-18 | 0120 | Kühl | 22 | 3.2 | Start Saison
Jan-25 | 0145 | Kühl | 21 | 3.4 | Normal
Feb-01 | 0180 | Kühl | 23 | 3.3 | Filter gereinigt
Feb-15 | 0230 | Heiz | 24 | 2.8 | Wärmepumpe Test
Mär-01 | 0280 | Kühl | 20 | 3.5 | Präventiv-Wartung durchgeführt
```

**Ziel**: Bei >10.000 Betriebsstunden Komplettrevision durchführen

---

## Anhang Q: Kostenmodell (EUR 2026)

### Q.1 Systemkauf nach Größe (inkl. Installation, ohne Rohre)

| Systemtyp | BTU | Kosten OHNE Installation | Installation | Rohrleitungen | Gesamtbudget |
|-----------|-----|------------------------|-----------------|-----------------|------------|
| Deck-Unit | 7,000 | 4,200 EUR | 600–800 EUR | 200 EUR | ~5,100 EUR |
| Split | 18,000 | 10,500 EUR | 1,500–2,000 EUR | 800–1,500 EUR | ~12,800 EUR |
| Chilled-Water | 40,000 | 35,000 EUR | 3,000–5,000 EUR | 3,000–5,000 EUR | ~43,000 EUR |
| Wärmepumpe | 24,000 | 16,800 EUR | 2,000–2,500 EUR | 1,000–1,500 EUR | ~20,300 EUR |

### Q.2 Jährliche Wartungskosten (ca.)

- **Einfach** (Deck-Unit): 400–600 EUR/Jahr
- **Mittel** (Split): 800–1,200 EUR/Jahr
- **Komplex** (Chilled-Water): 1,500–2,500 EUR/Jahr

**Notfall-Reserve**: 15 % der System-Kosten jährlich sparen

---

## Anhang R: Prüflisten für Bootskäufer

### R.1 AC-System bei Boot-Besichtigung

- [ ] Kompressor-Alter (Typenschild notieren): Wie viel älter als Rumpf?
- [ ] Seawaterfilter-Zustand: Schmutzansammlung? Korrosion?
- [ ] Hochdruck-Manometer vorhanden & lesbar?
- [ ] Betriebsgeräusch beim Starten: Normal "Brummen" oder "Pfeif"?
- [ ] Kühlung-Test durchführen: 15 Min Betrieb, Innentemperatur-Messung
- [ ] Fernbedienung funktionsfähig? Alle Knöpfe reagieren?
- [ ] Seacock zugänglich & leicht zu bedienen?
- [ ] Rohrleitungen: Lecks, Risse, Verschleiß sichtbar?
- [ ] Verdampfer-Luftstrom: Merklich kalt oder schwach?
- [ ] Wartungsprotokolle vorhanden? (letzte Service-Datum)

**Kauftipp**: AC-Alter >8 Jahre = Reparatur-Budget +EUR 2,000–5,000 in Kaufpreis einrechnen

---

## ERWEITERUNG: FEHLERBILD-ATLAS (FB-26-03)

> ⚠️ **ZU PRÜFEN (Audit):** Dieser Erweiterungs-Atlas vergibt die Fehlercodes FB-26-03-001 bis -012 ERNEUT, jedoch mit völlig anderer Bedeutung als der Haupt-Atlas in Kap. 6 (z. B. FB-26-03-001 dort = "Wasserlecks im Seewasser-Schlauch", hier = "Kompressor-Strömungsgeräusch"; FB-26-03-002 dort = "Luftblase im Kältemittelkreislauf", hier = "Verdampfer-Effizienz-Verlust"). Gleiche Codes mit widersprüchlichem Inhalt und abweichenden Normal-Druckangaben — eine Umnummerierung ist erforderlich, überschreitet aber eine konservative Punktkorrektur. Confidence: estimated — unverifiziert.

### FB-26-03-001: Kompressor-Strömungsgeräusch ("Rauchen")

**Symptome:**
- Ungewöhnlich lautes Poltern/Schleifen beim Start
- Rohrleitungen vibrieren intensiv
- Öl-Aerosol in Sichtglas sichtbar
- Druckabfall innerhalb 10 Min nach Abschaltung

**Root-Ursachen (Häufigkeit):**
1. Lagerschaden (40 %): Radialspiel >2 mm, Lagerzonen-Verfärbung
2. Ventil-Verschleiß (35 %): Kolben-Kratzer, Einlassventil-Undichtheit
3. Fremdkörper im Zylinder (15 %): Öl-Polymerkügelchen, Trockenmittel-Reste
4. Ansaugfilter-Verstopfung (10 %): Gegendruck >0.5 bar

**Inspektionsschritte:**
1. Kompressor-Vibrationen messen: X/Y/Z-Beschleunigung, spec <5 mm/s²
2. Hochdruck-Kurve aufzeichnen (0–600 s): Steigung in Phase 2 notieren
3. Rohrleitungs-Dichtheit testen: Seifenlauge an allen Connections
4. Öl-Probe entnehmen: Labor-Analyse auf Metallabrieb (FeS₂-Tendenz)
5. Verdampfer-Temperatur: Sollte <5°C sein; wenn >8°C → Verdampfer-Kalk

**Reparatur-Entscheidung:**
| Parameter | Akzeptabel | Warnung | Ersatz |
|-----------|-----------|---------|--------|
| Vib. X/Y/Z | <3 mm/s² | 3–5 | >5 |
| Druck-Steigung | >0.8 bar/s | 0.5–0.8 | <0.5 |
| Metallabrieb | <50 ppm | 50–100 | >100 |

**Kosten:** Kompressor-Austausch 2,800–4,500 EUR + Installation

---

### FB-26-03-002: Verdampfer-Effizienz-Verlust (dT < 5°C)

**Symptome:**
- Kammertemperatur sinkt von 22°C nur bis 18°C (statt 20 Min → 45 Min)
- Verdampfer-Oberfläche-Frost minimal oder fehlend
- Hochdruck 12–14 bar (normal 16–18)
- Seawater-Austritt warm (>8°C statt 3–4°C)

**Root-Ursachen:**
1. Verdampfer-Verschmutzung (45 %): Algenfilm, Kalkablagerung (Dicke 0.5–2 mm)
2. Kältemittel-Unterladung (30 %): Leckage oder schlecht kalibrierter Receiver
3. Nicht-Kondensierbares Gas (NCG, 15 %): Luft, Feuchtigkeit in Speicher
4. Regelventil-Fehleinstellung (10 %): Superheat >8°C (sollte 4–6°C)

**Inspektionsschritte:**
1. Verdampfer-Einlass-Druck: Sollte ≤0.3 bar unter Kondensator-Druck
2. Seawater-Strömung messen (l/min): Sollte ≥10 % von Kondensator-Spec
3. Verdampfer-Einlassleitung anfassen: sollte kalt (≤2°C) sein
4. Kältemittel-Menge überprüfen (Receiver-Glas): sollte 75–95 % voll sein
5. Superheat mit Thermometer-Paar messen: (T_Verdampfer-Auslass) − (T_Sättigung @ Druck)

**Reinigung (vor Austausch):**
- Verdampfer-Ansatz: Zitronensäure-Lösung (10 %), 30 Min Zirkulation, dann DI-Wasser spülen
- Kosten: 400–800 EUR (mit Ausbau/Einbau)
- Erfolgsquote: 80 % bei Algenfilm, 30 % bei Kalk >1 mm

**Kosten:** Verdampfer-Austausch 3,500–6,000 EUR

---

### FB-26-03-003: Kondensator-Strömung-Blockade

**Symptome:**
- Hochdruck steigt rapide (bis 25–30 bar)
- Kompressor-Abschaltung durch Hochdruck-Sicherung
- Seawater-Einlass: fühlt sich "gleich" wie Auslass an
- Keine Lärm-Änderung, aber schnelle Temperatur-Instabilität

**Root-Ursachen:**
1. Seacock-Undichtheit (50 %): Ventil nur 30–50 % offen, Rohr-Querschnitt <50 % frei
2. Intake-Filter-Verstopfung (25 %): Algen-Überfluss, Sand-Eintrag
3. Rohr-Verschleiß/Kollaps (15 %): Hochdruck-Seite, Schlauch geplatzt
4. Luft im System (10 %): Siphon-Bruch, Undichtheit an Ansaugseite

**Inspektionsschritte:**
1. Seacock-Einlasstemperatur vs Umwelt: Diff sollte <2°C sein
2. Seacock-Öffnungsgrad visuell prüfen: Ventilstiel sollte maximal offen stehen
3. Filter-Taschen sichtprüfung: Grüne/braune Ablagerungen deuten auf Verstopfung
4. Hochdruck-Rohr mit Stethoskop abhören: Strömungs-Geräusch sollte "weich zischen" sein, nicht "pfeifen"
5. Seawater-Auslass-Temperatur messen nach 10 Min: sollte 6–10°C wärmer sein als Einlass

**Sofort-Maßnahmen (im Einsatz):**
- Seacock 90 ° öffnen (falls nur 45 °)
- Filter-Ansatz mit Süßwasser ausspülen (ohne Ausbau)
- System 5 Min abkühlen lassen, dann neu starten

**Kosten:** Filter-Wechsel 80–150 EUR, Seacock-Wartung 200–400 EUR, Rohrerneuerung 600–1,500 EUR

---

### FB-26-03-004: Öl-Rückführungs-Fehler

**Symptome:**
- Kompressor wird "trocken": Betriebsgeräusch wird höher/schärfer über 5–10 Min
- Ölstand im Kompressor-Sichtglas sinkt (von 50 % → 20 % während Betrieb)
- Verdampfer-Ausgang wird grau/ölig (Öltropfen auf Oberfläche)
- Hochdruck steigt unmerklich, aber Kühlung fällt um 30–50 %

**Root-Ursachen:**
1. Öl-Abscheider-Verstopfung (50 %): Öl-Partikel >10 µm, Polyol-Schlamm
2. Rückführungs-Leitung kollabiert (25 %): Schlauch gequetscht, Ventil zugeklebt
3. Evaporator-Oil-Return blockiert (15 %): Kältemittel-Verdampfer sammelt Öl, Strömung unzureichend
4. Kompressor-Ansaug-Druck zu niedrig (10 %): Öl-Verdunstung statt Rücktransport

**Inspektionsschritte:**
1. Ölstand visuell: sollte 40–60 % anzeigen, konstant über 30 Min Betrieb
2. Ölabscheider-Aussehen: Farbe sollte dunkelbraun sein; wenn schwarz → Polyol-Abbau
3. Rückführungs-Leitung berühren: sollte temperiert (25–35°C) sein, nicht kalt
4. Öl-Probe aus Sichtglas entnehmen: Viskosität messen (sollte ISO VG 32, d.h. 28–36 cSt @ 40°C)
5. Ansaug-Druck am Kompressor: sollte >−0.5 bar sein (Vakuum <50 mbar)

**Wartungs-Maßnahmen:**
- Ölabscheider-Filterkartusche wechseln: 200–350 EUR
- Rückführungs-Leitung spülen: Trockenmittel-Patrone 30 Min, dann Öl-Charge erneut prüfen
- Neue Ölladung (vollständiger Wechsel): 800–1,200 EUR + Evakuierung

**Kosten:** Ölabscheider-Service 300–500 EUR, kompletter Ölwechsel 1,200–2,000 EUR

---

### FB-26-03-005: Kältemittel-Leckage

**Symptome:**
- Druck sinkt über Nacht (um 0.5–2 bar) troätis Abschaltung
- Kühlung lässt nach, Hochdruck-Anstieg bei gleicher Last
- Geruchsneutrales Öl findet sich um Kompressor oder Kondensator
- Hochdruck-Manometer zeigt bereits nach 5 Min Betrieb <12 bar

**Root-Ursachen (nach Häufigkeit):**
1. Vibration-Risse in Kupfer-Rohr (40 %): Typisch an Umkehrpunkten oder über Halterungen
2. Löt-Undichtheit (30 %): Kalte Lötstelle, Korrosion-Loch in Rohr (Dicke <0.5 mm)
3. Schlauch-Undichtheit (20 %): Kink, UV-Schaden, Alterung des Elastomers
4. Verdichter-Ventil-Leckage (10 %): Undichte Kolbenring-Nut

**Inspektionsschritte:**
1. Seifenlauge-Test an ALLEN Verbindungen & Rohren (besonders Krümmungen)
2. Ölfleck-Suche: um Kompressor (Ölsumpf), Verdampfer-Eingang, Kondensator-Ausgang
3. Röntgen-Druck-Sprühfarbe: Hochdruck-Leck offenbart sich als Sprühnebel
4. Ultraschall-Lecklage-Detektor (professionell): findet Lecks ab ~1 g/Jahr
5. Stickstoff-Test nach Tracer-Injektion (Fachbetrieb): quantifiziert Leckrate

**Reparatur-Optionen:**
| Leck-Typ | Reparatur | Kosten | Erfolgsquote |
|----------|-----------|--------|--------------|
| Kleine Risse (<0.5 mm) | Lot-Reparatur (Fachbetrieb) | 400–700 EUR | 85 % |
| Mittlere Risse | Kupfer-Insertions-Reparatur | 800–1,500 EUR | 90 % |
| Schlauch-Bruch | Schlauch-Wechsel (Stück) | 300–600 EUR | 100 % |
| Kompressor-Ventil | Kompressor-Überholung | 2,500–4,500 EUR | 95 % |

**Notfall-Provisorium (max. 2 Wochen):**
- Epoxy-Kupferband + Wicklung (nicht dauerhaft!) → verhindert Druckabfall für Notfall-Betrieb
- Kosten: 50–100 EUR (Material), aber Reparatur muss folgen

---

### FB-26-03-006: Verdampfer-Frost-Regelungs-Fehler

**Symptome:**
- Verdampfer-Oberfläche vereist komplett (weiße/blaue Frostschicht)
- Ausgangs-Luft wird eiskalt, aber Raum-Temperatur pendelt (20 → 10 → 20°C)
- Verdampfer-Druck schwankt zwischen 1–3 bar alle 20 Sekunden
- Thermostat-Fernbedienung reagiert trägat oder gar nicht

**Root-Ursachen:**
1. Regelventil-Drift (50 %): Behälter-Ausdehnungs-Behälter-Sensitivität falsch kalibriert
2. Thermostaten-Sensor fehlerhaft (30 %): Feuchtigkeit in Sonde, Kontakt gebrochen
3. Elektronik-Ausfall (Regelmodul, 15 %): Kapazitiv-Fehler, Relais-Stick
4. Regelventil mechanisch blockiert (5 %): Eis-Kristalle, Verschmutzung

**Inspektionsschritte:**
1. Thermostaten-Fern-Sonde anfassen: sollte sich bei Frost ähnlich "kalt" anfühlen wie der Verdampfer
2. Sonden-Widerstand messen (Ohmmeter): typisch 10–50 kΩ @ 20°C, Temperatur-Abhängigkeit prüfen
3. Regelventil-Antrieb prüfen: sollte bei Verdampfer-Frost langsam zurückfahren (schließen), nicht schnell
4. Elektronik-Modul visuell: Kondensator-Wölbung, Korrosion an Kontakten prüfen
5. Verdampfer-Eis manuell antauen (ca. 30 Min stillstand): versuchen Neustart → wenn nicht mehr vereist, Regelventil-Problem

**Reparatur-Maßnahmen:**
- Sensor-Austausch (einfach): 150–300 EUR
- Regelventil-Überholung: 400–700 EUR
- Elektronik-Modul-Austausch: 600–1,200 EUR
- Kalibrierung (Fachservice): 200–350 EUR

---

### FB-26-03-007: Seawater-Temperatur-Schwankungen

**Symptome:**
- Umgebungs-Seawater-Temp variiert (12°C → 18°C) → Hochdruck springt (15 → 22 bar)
- Tropische Gewässer (28°C): Hochdruck >25 bar, Kompressor überlastet
- Kalte Gewässer (2°C): Hochdruck nur 8 bar, Verdampfer vereist
- Nachrüstung auf "warme Gewässer" unzureichend

**Root-Ursachen:**
1. AC-System unter-dimensioniert für warme Gewässer (60 %): Hersteller-Nominal bei 15°C Seawater
2. Seacock-Position suboptimal (20 %): Einlass neben Bilge-Auslass (warmes Rückwasser)
3. Kondensator-Wasser-Anteil zu gering (15 %): zu kleine Pumpeleistung
4. Wärmequellen-Überschuss (5 %): Motor-Abwärme, Galley-Dump, unzureichende Isolation

**Inspektionsschritte:**
1. Seawater-Einlass-Temperatur vs echte Wassermasse-Temp: Differenz >1°C zeigt Seacock-Position-Problem
2. Seawater-Durchfluss-Rate messen (l/min): sollte ≥80 % von Herstellervorgabe sein
3. Kondensator-Wasser-Temp-Differenz: Ausgang − Eingang sollte 4–8°C sein
4. Hochdruck bei kaltem/warmem Wasser aufzeichnen: Reaktions-Steigung notieren
5. Wärmequellen in Maschinenbeschreibung: Motor-Abwärme, Gas-Kochfeld, Dieselheizer prüfen

**Nachrüstungs-Optionen für warme Gewässer:**
| Lösung | Effekt | Kosten | Wartezeit |
|--------|--------|--------|-----------|
| Größere Kondensator-Pump | +15 % Wasserdurchsatz | 800–1,500 EUR | 1 Woche |
| Zweite Kühl-Einheit (Backup) | Redundanz, +50 % Kapazität | 5,000–8,000 EUR | 3 Wochen |
| Hochdruck-Regelventil-Upgrade | Stabilisierung bis 28°C | 400–700 EUR | 3 Tage |
| Wasser-zu-Wasser-Kühler | Entkopplung von Seawater | 2,000–4,000 EUR | 2 Wochen |

---

### FB-26-03-008: Elektrik-Ausfallmuster

**Symptome:**
- AC läuft normal 15 Min, dann Strom-Ausfall (kein Kompressor-Brummen mehr)
- Nach 10 Min Stillstand wieder startbar ("Reset"-Verhalten)
- Thermoschutzschalter warm anfühlen
- Keine Fehlermeldung, stille Abschaltung

**Root-Ursachen:**
1. Wärmeschutzschalter-Überempfindlichkeit (40 %): Kalibrierung bei 60°C, aber tatsächlich 55°C
2. Einphasen-Ausfall (30 %): Drehstrom-Motor mit fehlendem Phase (25 % weniger Leistung, Überstrom)
3. Stromversorgung-Spannungsdrop (20 %): lange Kabellaufen, zu dünne Adern (<6 mm²)
4. Motorschutzrelais blockiert (10 %): Kondensator-Defekt, elektronische Steuerung

**Inspektionsschritte:**
1. Thermoschutzschalter-Auslöse-Temperatur prüfen (Fachbetrieb): sollte 65–75°C sein
2. Drehstromprüfung: Alle 3 Phasen mit Digitalmultimeter messen (sollte ≤2 % Differenz zeigen)
3. Spannungsdrop-Messung: unter Last (Kompressor läuft) an Batterie vs Compressor-Eingang: sollte <3 % sein
4. Stromaufnahme prüfen (Zange-Amperemeter): sollte nominal sein (z.B. 45–55 A für 230V / 2 kW)
5. Motorschutzrelais-Funktion: Schließkontakt überprüfen, ggf. Kondensator-Test

**Reparatur-Optionen:**
- Wärmeschutzschalter-Austausch: 150–300 EUR
- Kabelquerschnitt erhöhen (6 → 10 mm²): 300–600 EUR
- Motorschutzrelais-Überholung: 250–450 EUR
- Drehstrom-Optimierung (3-Phase-Balancing): 200–400 EUR

---

### FB-26-03-009: Vibrations-Isolations-Versagen

**Symptome:**
- Verdampfer-Montage-Vibrationen übertragen sich auf Rumpf (Resonanz bei 45–60 Hz)
- "Summen"-Geräusch von gesamter Kajüte hörbat (nicht nur AC-Unit)
- Möbel/Fenster vibrieren mit
- Gummi-Füße aussehen "verschlissen" oder lösen sich

**Root-Ursachen:**
1. Vibrations-Isolation-Gummi-Verschleiß (60 %): Elastomer-Ermüdung nach 5–7 Jahren
2. Montage-Befestigungen zu rigid (25 %): direkte Verschraubung ohne Isolation
3. Verdampfer-Unwucht (10 %): Lüfter-Schaufel-Ablagerung, Flansch-Verzug
4. Resonanz-Kopplung mit Rumpf (5 %): kritische Frequenz trifft System-Eigenfrequenz

**Inspektionsschritte:**
1. Vibrations-Gummi anfassen: sollte elastisch nachgeben (>2 mm unter Fingerdruck)
2. Sichtprüfung der Gummi-Blöcke: Risse, Quellung, Verfärbung deuten auf Verschleiß
3. Verdampfer-Lüfter-Inspektion: Blätter auf Verschmutzung/Eisansatz prüfen
4. Resonanz-Test: Mit Handflache gegen Verdampfer tippen → Nachschwingung sollte <1 Sekunde sein
5. Befestigungsschrauben-Check: alle sollten fest sein (Drehmoment 6–8 Nm)

**Modernisierungs-Maßnahmen:**
- Vibrations-Gummi-Austausch (Satz): 200–400 EUR
- Zusatz-Isolation (Schwer-Schaumstoff-Platten): 150–300 EUR
- Verdampfer-Umwuchten (Fachservice): 250–450 EUR
- Resonanz-Entkopplung (Feder-Montage): 500–900 EUR

---

### FB-26-03-010: Seacock-Versagen & Blockade

**Symptome:**
- Seacock lässt sich nicht öffnen ("geklemmt")
- Seawater-Durchfluss unvollständig (Manometer-Druck steigt, obwohl nicht gas-geladen)
- Korrosion um Seacock-Gewindung sichtbar (weiße/blaue Kristalle)
- Wasser tropft permanent (auch bei geschlossener Position)

**Root-Ursachen:**
1. Korrosion im Ventil-Innenraum (45 %): Salzwasser-Elektrolyse, Stahl-Verschleiß (wenn nicht 316L SS)
2. Calciumcarbonat-Ablagerung (30 %): Hard Water, Schachtelhalm-Kristalle im Ventil-Sitz
3. Gummi-Dichtung-Swelling (15 %): NBR-Degradation in warmen Gewässern (>24°C)
4. Verschleiß des Ventil-Sitzes (10 %): zu häufiges Betätigen, Sand-Kornabrieb

**Inspektionsschritte:**
1. Öffnungs-Widerstand prüfen: sollte <5 Nm Drehmoment erfordern
2. Gehäuse mit Feuchtigkeits-Meter prüfen: darf nicht nass wirken
3. Auslasstemperatur nach 5 Min Betrieb: wenn >10°C wärmer als Einlass → Seacock kein 100 % Durchsatz
4. Gummi-Dichtung visuell: sollte dunkelbraun/schwarz sein; wenn gelblich/aufgequollen → NBR-Problem
5. Rohrleitungs-Drucktest (Manometer an Auslass): sollte höchstens 0.2 bar Druck-Differenz sein

**Wartungs-Zeitplan:**
- Jährlich: Öffnen/Schließen durchüben, Auslasstemperatur überprüfen
- Alle 2 Jahre (warme Gewässer) oder 4 Jahre (kalte Gewässer): Gummi-Dichtung überprüfen
- Alle 4 Jahre: kompletter Seacock-Austausch (Präventiv)

**Kosten:** Seacock-Austausch 600–1,200 EUR (mit Installation & Prüfung)

---

### FB-26-03-011: Öltemperatur-Übersteigung

**Symptome:**
- Kompressor-Gehäuse-Temperatur >80°C (Fühler warm)
- Öl-Sichtglas verfärbt sich dunkelbraun (Oxidation)
- Bitumen-ähnlicher Geruch um Kompressor
- Kühlung lässt nach, obwohl Hochdruck normal

**Root-Ursachen:**
1. Unzureichende Öl-Kühlungs-Kapazität (50 %): Ölkühler-Kalkablagerung, Durchfluss <0.3 l/min
2. Falsche Öl-Sorte (25 %): Mineralöl statt Polyol, falsche Viskosität (zu dünn)
3. Überlastung (Kühllast zu hoch, 15 %): System dimensioniert für 15°C Seawater, läuft bei 25°C
4. Öl-Zersetzung durch Verschleiß (10 %): Metallabrieb, Feuchtigkeit, Sättigungsdruck überschritten

**Inspektionsschritte:**
1. Öl-Temperatur-Sensor-Ausgangssignal prüfen: sollte 40–60°C zeigen (abhängig vom Betriebszustand)
2. Ölkühler-Durchfluss überprüfen: sollte ≥0.3 l/min sein
3. Ölkühler-Wasser-Einlass-Temp: sollte 3–5°C kälter als Seawater-Eingabe sein
4. Öl-Farbe-Vergleich mit neuem Referenz-Öl: sollte maximal "bernsteinfarben" sein
5. Ölprobe-Laboranalyse: TAN (Säurezahl) sollte <0.5 mg KOH/g sein

**Abhilfe-Maßnahmen:**
- Ölkühler-Reinigung (oder Austausch): 400–800 EUR
- Öl-Kompletter-Wechsel: 800–1,200 EUR (mit Ölabscheider-Wartung)
- Sekundär-Ölkühler-Installation: 1,500–2,500 EUR (für tropische Einsätze)
- Thermostaten-Regelung für Ölkühler: 300–600 EUR

---

### FB-26-03-012: Brandschutz-Versagen (Feuer-Erkennungs-System)

**Symptome:**
- Feuermelder neben AC-Unit funktioniert nicht (nie ausgelöst)
- Sichtprüfung zeigt Staub/Öl-Verschmutzung auf Sensor-Optik
- Alarm-Elektronik-Test fehlgeschlagen (rote LED blinkt nicht)
- Verdampfer-Bereich hat kein dediziertes Feuer-Erkennungs-Gerät

**Root-Ursachen:**
1. Sensor-Verschmutzung (60 %): Öl-Aerosol, Staub blockiert Infrarot-Fenster
2. Elektronik-Ausfall (25 %): Batterie leer, Funkverbindung-Unterbruch
3. Montage-Fehler (10 %): Sensor zu nah an AC-Abluft-Auslass (Fehler-Alarm verhindert)
4. Veraltete Systeme (5 %): ionisierungs-Rauchmelder in Motorenraum, per Regelwerk seit 2010 verboten

**Inspektionsschritte:**
1. Sensor-Optik-Reinigung: mit fusselfreiem Tuch und IPA-Alkohol
2. Batterie-Spannung prüfen (Digitalmultimeter): sollte ≥70 % der Nenn-Spannung sein
3. Test-Taste betätigen (wenn vorhanden): sollte akustischen Alarm auslösen
4. Funkverbindung-Test (zentrale Alarmanlage): sollte "OK" anzeigen
5. Sensor-Position überprüfen: sollte min. 30 cm Abstand von AC-Auslass haben

**Modernisierung (Pflicht nach Regelwerk):**
- Wärmemelder-Installation (statt Ionisierung): 150–250 EUR
- Funk-Alarm-Integration: 200–400 EUR
- Batterie-Austausch (10-Jahres-Paket): 50–100 EUR

---

## TROUBLESHOOTING-ENTSCHEIDUNGSBÄUME

### Baum 1: "Klimaanlage kühlt nicht" (Entscheidungsbaum)

```
START: "AC kühlt nicht"
│
├─→ Kompressor läuft? (Hörbares Brummen, Hochdruck >6 bar)
│   │
│   NO→ [Elektrik-Check: Strom vorhanden? Schutzmechanismus aktiv?]
│   │   → Thermoschutzschalter prüfen (FB-26-03-008)
│   │   → Drehstrom-Balance prüfen
│   │   → KOSTEN: 200–500 EUR Diagnose
│   │
│   YES→ Verdampfer kalt? (Anfassen: Sollte <5°C sein)
│       │
│       NO→ [Kältemittel-Menge-Check]
│       │   → Receiver-Glas: sollte 75–95 % voll sein
│       │   → Druck sinkt im Idle? → Leckage (FB-26-03-005)
│       │   → Druck normal, aber Verdampfer warm → Regelventil-Fehler (FB-26-03-006)
│       │   → KOSTEN: 400–1,200 EUR (Leckage-Reparatur/Kalibrierung)
│       │
│       YES→ Raumtemperatur sinkt? (Nach 20 Min)
│           │
│           NO→ [Verdampfer-Effizienz-Verlust prüfen]
│           │   → Verdampfer-Oberfläche: Frost? (sollte ja sein)
│           │   → Seawater-Durchfluss: ≥10 l/min?
│           │   → Hochdruck: normal (16–18 bar)?
│           │   → FB-26-03-002 (Verdampfer-Verschmutzung/Kältemittel-Mangel)
│           │   → KOSTEN: 400–3,500 EUR
│           │
│           YES→ ✓ Normale Kühlung → Monitor & Log
```

### Baum 2: "Hochdruck zu hoch" (15-Minute-Reset-Zyklus)

```
START: Hochdruck >20 bar (Normal: 16–18)
│
├─→ Seawater-Durchsatz prüfen: 12–15 °C differential?
│   │
│   NO→ [Kühl-Wasser-Blockade]
│   │   → Seacock öffnen? (falls nur 45° = Sofortmaßnahme)
│   │   → Filter-Ansatz reinigen (Süßwasser-Spülsystem)
│   │   → Seawater-Einlass-Temp vs Umgebung: >2°C Diff?
│   │   → FB-26-03-003 (Kondensator-Strömung) oder FB-26-03-007 (Seawater-Temp)
│   │   → KOSTEN: 80–1,500 EUR
│   │
│   YES→ Seawater-Temperatur >22°C? (Tropische Gewässer)
│       │
│       NO→ [Nicht-Kondensierbare-Gase / Systemfehler]
│       │   → Hochdruck-Leck-Test (Ultraschall): >0.1 g/Jahr?
│       │   → Ölabscheider-Zustand prüfen
│       │   → Kältemittel-Menge überprüfen
│       │   → FB-26-03-005 (Leckage) oder FB-26-03-004 (Öl-Rückführung)
│       │   → KOSTEN: 400–2,500 EUR
│       │
│       YES→ System unter-dimensioniert für diesen Einsatz
│           → Hochdruck-Regelventil-Upgrade
│           → oder zweite AC-Unit für Redundanz
│           → FB-26-03-007 (Nachrüstung)
│           → KOSTEN: 400–8,000 EUR
```

### Baum 3: "Vibration/Geräusch-Problem"

```
START: AC-System vibriert oder "brummt" laut
│
├─→ Verdampfer selbst vibriert? (Handfinger-Test)
│   │
│   YES→ [Vibrations-Isolation-Check]
│   │   → Gummi-Füße elastisch? (Druck-Test mit Finger)
│   │   → Befestigungsschrauben fest? (Drehmoment 6–8 Nm)
│   │   → FB-26-03-009 (Vibrations-Isolations-Versagen)
│   │   → KOSTEN: 200–900 EUR
│   │
│   NO→ Kompressor-Geräusch? ("Poltern", "Rauchen")
│       │
│       YES→ [Kompressor-Schaden]
│       │   → Druckabfall test
│       │   → Ölprobe auf Metallabrieb (Labor)
│       │   → FB-26-03-001 (Kompressor-Strömungsgeräusch)
│       │   → KOSTEN: 2,800–4,500 EUR (Austausch)
│       │
│       NO→ "Summen" von Kajüte-Resonanz
│           → System läuft normal, aber strukturelle Resonanz
│           → Sekundär-Isolation hinzufügen
│           → KOSTEN: 150–300 EUR
```

### Baum 4: "Elektrik-Abschaltung nach 15 Min"

```
START: AC läuft kurz, dann Stromausfall
│
├─→ Thermoschutzschalter warm? (Berühren: >45°C)
│   │
│   YES→ [Wärmeschutzschalter-Überempfindlichkeit]
│   │   → Kalibrierung-Check (Fachbetrieb)
│   │   → Thermoschutzschalter-Austausch
│   │   → FB-26-03-008
│   │   → KOSTEN: 150–300 EUR
│   │
│   NO→ Stromversorgung-Spannungsdrop prüfen
│       │
│       <3% Diff?
│       YES→ [Motorschutzrelais-Check]
│       │   → Schließkontakt-Funktion prüfen
│       │   → Elektronik-Modul-Austausch
│       │   → KOSTEN: 250–1,200 EUR
│       │
│       NO→ [Kabel-Querschnitt zu klein]
│           → Upgrade 6 → 10 mm² (oder thicker)
│           → FB-26-03-008
│           → KOSTEN: 300–600 EUR
```

### Baum 5: "Öl-Temperatur-Problem"

```
START: Kompressor-Gehäuse >80°C
│
├─→ Ölkühler-Wasserdurchfluss prüfen: ≥0.3 l/min?
│   │
│   NO→ [Ölkühler-Blockade]
│   │   → Kalkablagerung? (Zitronensäure-Spülung)
│   │   → Ölkühler-Austausch
│   │   → FB-26-03-011
│   │   → KOSTEN: 400–800 EUR
│   │
│   YES→ Ölfarbe dunkelbraun/schwarz?
│       │
│       YES→ [Öl-Zersetzung]
│       │   → Kompletter Öl-Wechsel
│       │   → Ölabscheider-Wartung
│       │   → FB-26-03-011
│       │   → KOSTEN: 800–1,500 EUR
│       │
│       NO→ Seawater-Temperatur >24°C?
│           → Sekundär-Ölkühler installieren (warme Gewässer)
│           → KOSTEN: 1,500–2,500 EUR
```

---

## HÄUFIG GESTELLTE FRAGEN (FAQ) — 25+ Einträge

### F-1: Wie oft sollte die AC-Anlage gewartet werden?

**Antwort:**
- **Monatlich:** Visuelle Kontrolle (Öl-Sichtglas, Korrosion, Geräusche)
- **Halbjährlich:** Seawater-Filter reinigen, Dichtprüfung
- **Jährlich:** Komplette Funktionsprüfung, Druck-Messung, Ölqualität-Check
- **Alle 2 Jahre:** Kältemittel-Analyse, Vibrations-Kontrolle (warme Gewässer)
- **Alle 4 Jahre:** Seacock-Austausch (präventiv), Verdampfer-Reinigung
- **Alle 5–7 Jahre:** Ölwechsel, Schlauch-Inspektion

Folgen Sie Hersteller-Vorgaben (Dometic, Frigomar, etc.); diese Angaben sind Minimum-Standard.

### F-2: Welche Kosten fallen im Betrieb an?

**Antwort:**
- **Jahres-Betriebskosten:**
  - Einfaches Deck-Unit: 400–600 EUR/Jahr
  - Mittleres Split-System: 800–1,200 EUR/Jahr
  - Komplexes Chilled-Water: 1,500–2,500 EUR/Jahr
- **Notfall-Reserve:** 15 % der System-Kosten jährlich sparen
- **Beispiel 12-m-Cruiser mit 4-kW-Unit:**
  - Anschaffung: 8,000 EUR
  - 10-Jahres-Betriebskosten: 9,000–12,000 EUR
  - **Total: 17,000–20,000 EUR über 10 Jahre**

### F-3: Kann ich AC in kalten Gewässern fahren?

**Antwort:**
- **Ja, aber mit Einschränkungen:**
  - <10°C Seawater: Hochdruck <8 bar, Verdampfer vereist → Regelventil muss "Cracking" verhindern
  - Thermostat-Einstellung auf Minimum setzen (verhindert Über-Kühlung)
  - Alle 15 Min Monitor (Vereisungs-Gefahr)
- **Moderne Systeme:** besitzen Frost-Schutz-Logik; ältere <2010 ohne Regelventil sind problematisch
- **Kosten für Frost-Schutz-Upgrade:** 300–600 EUR

### F-4: Wie erkenne ich ein AC-Leck?

**Antwort:**
Vier Methoden (von einfach zu professionell):
1. **Seifenlauge:** Um alle Verbindungen sprühen → Blasen = Leck (Kosten: 10 EUR)
2. **Ölfleck-Suche:** AC-Öl ist synthetisch → zeigt sich als dünner Film (kostenlos, visuell)
3. **Druck-Tagebuch:** Hochdruck täglich notieren → Abfall >0.5 bar/Woche zeigt Leck (kostenlos)
4. **Ultraschall-Detektor:** Fachbetrieb mit Lecklage-Gerät (Kosten: 80–150 EUR Dienstleistung)

Leckrate <0.1 g/Jahr ist tolerierbar; >0.5 g/Jahr erfordert Reparatur.

### F-5: Sollte ich AC in der Winterlagerung ablassen?

**Antwort:**
- **Nein, generell nicht.** Modern sealed Systems vertragen Lagern mit 90 % System-Druck.
- **Ausnahmen:**
  - Extreme Kälte (<−20°C) über Monate → Druck um 20 % reduzieren (Schutz vor Überdruckventil-Auslösung)
  - Reparatur geplant → professionelles Absaugen (Evakuierung) erforderlich
  - Seacock wird nicht betätigt → es entstehen Druckschwankungen durch Temperatur
- **Empfehlung:** Mit Kältemittel einlagern; Druck 1–2x monatlich überprüfen

### F-6: Kann ich den Kompressor selbst überholen?

**Antwort:**
- **Nein.** Grund: Verdichtungs-Toleranzen <0.1 mm, Spezialwerkzeuge (Druckprüfstand), Evakuierungs-Ausrüstung erforderlich.
- **Folgen eines Heimwerk-Versuchs:** Öl-Verunreinigung, falsche Montage → sofortiger Kompressor-Ausfall
- **Fachbetrieb-Kosten:** Überholung 2,000–3,500 EUR (besser als Austausch 4,000–5,000 EUR)

### F-7: Welche Kältemittel-Menge ist richtig?

**Antwort:**
- **Receiver-Sichtglas-Standard:** 75–95 % voll anzeigen (zwischen den beiden Linien)
- **Zu wenig** (<50 %): Hochdruck sinkt, Verdampfer vereist, Kühlung fällt
- **Zu viel** (>95 %): Hochdruck steigt, Verdampfer-Flüssigkeit kann nicht expandieren → Wirkungsgrad-Verlust
- **Kalibrierung:** Muss mit exaktem Druck-/Temperatur-Diagramm erfolgen (Fachbetrieb, 200–400 EUR)

### F-8: Was ist der Unterschied zwischen R134a und R1234yf?

**Antwort:**
| Eigenschaft | R134a | R1234yf |
|---|---|---|
| GWP (Treibhauseffekt) | 1,430 | 4 |
| Effizienz | Höher (+5–8 %) | Leicht niedriger (−2 %) |
| Sicherheit | Non-flammabel | Leicht flammabel (Klasse A2L) |
| Kompatibilität | Ältere Systeme | Neuere Verdichter ab 2015 |
| Kosten | 20–30 EUR/kg | 50–80 EUR/kg |
| Einsatz | Boot-Standard bis 2023 | Neustandard ab 2024 |

**Empfehlung:** Hersteller-Vorgabe beachten. Tausch nicht ohne Kompressor-Wartung durchführen.

### F-9: Wie laut sollte eine AC-Anlage sein?

**Antwort:**
- **Normal:** 75–82 dB(A) @ 1 m Entfernung (vergleichbar: Normalkonversation)
- **Zu laut** (>85 dB): Verdampfer-Lüfter-Verschleiß, Vibrations-Isolation-Fehler, Kompressor-Lagerschaden
- **Zu leise** (<70 dB): Weniger Kühlleistung (könnte Absicht sein, aber auch System-Fehler)
- **Geräusch-Art beobachten:**
  - "Sanftes Brummen" (75 dB) = Normal
  - "Poltern/Rauchen" = Kompressor-Problem (sofort Wartung)
  - "Zischen/Pfeifen" = Hochdruck-Leck oder Seacock-Blockade

### F-10: Kann Seewasser-Verschmutzung das System zerstören?

**Antwort:**
- **Ja.** Schlammlagen, Algen, Sand können Kondensator blockieren und Hochdruck auf 25+ bar drücken.
- **Häufige Verschmutzungs-Quellen:**
  - Häfen mit niedrigem Wasserwechsel (Brackwasser, hohe Algen-Konzentration)
  - Motoren-Abluft-Wiederaufnahme (wenn Seacock-Einlass neben Abgasen positioniert)
  - Bilge-Wasser-Vermischung (wenn Intake-Filter fehlt)
- **Prävention:**
  - Seacock-Einlass-Position alle 10 Min überprüfen (besonders in seichten Häfen)
  - Intake-Filter monatlich reinigen
  - Bei Verdacht: Seawater-Durchfluss 5 Min abkühlen lassen & Verdampfer-Frost prüfen

### F-11: Ist eine "Standby"-Position sinnvoll?

**Antwort:**
- **Ja, für längere Stilllegung:**
  - System auf 50 % Kühlleistung stellen → Kompressor läuft nur 1–2 Min/Stunde
  - Verhindert kalte Kajüten-Bereiche & spart Diesel-Betrieb (Motor läuft weniger)
  - Kältemittel-Druck bleibt auf System (verhindert Oxidation)
- **Nein, für tägliche Nutzung:**
  - "Standby" verursacht Kompressor-Start/Stop-Zyklen → Motorschutzrelais-Verschleiß
  - Thermostat sollte kontinuierlich regeln (konstante Raumtemperatur)

### F-12: Kann Seawater-Temperatur die Leistung halbieren?

**Antwort:**
- **Ja.** 15°C Seawater (Basis-Auslegung) → 25°C Seawater (tropisch):
  - Hochdruck: 16 bar → 24 bar (+50 %)
  - Kompressor-Strom: 30 A → 42 A (+40 %)
  - Kühllast: −5 % Effizienz
- **Effekt:** In warmen Meeren funktioniert Standard-AC nur noch bei 80–85 % Nennleistung
- **Lösung:** Nachrüstung für warme Gewässer (Hochdruck-Regelventil, Pump-Upgrade, 400–1,500 EUR)

### F-13: Wie stelle ich ein AC-System korrekt ein?

**Antwort (Schritt-für-Schritt):**
1. **Thermostat auf 20°C setzen**
2. **Verdampfer-Verdampfer-Einlassleitung anfassen:** sollte 0–2°C sein
3. **Superheat-Messung:** (Verdampfer-Auslass-Temp) − (Sättigung @ Druck) sollte 4–6°C sein
4. **Hochdruck-Kurve aufzeichnen:** sollte konstant bei 16–18 bar sein
5. **Nach 20 Min:** Raumtemperatur sollte um 4–5°C gesunken sein
6. **Alle 5 Min Hochdruck notieren:** sollte nicht schwanken (±1 bar acceptable)

Bei Abweichungen → Fachbetrieb anrufen (Diagnose 150–300 EUR)

### F-14: Sollte ich ein Backup-System installieren?

**Antwort:**
- **Wenn:** Charter-Boot, kommerziell genutzt, oder tropische Gewässer → 2 unabhängige AC-Units
- **Wenn nicht:** Privat-Cruiser, kühlere Klimazonen, Budget begrenzt → eine AC-Unit reicht
- **Kosten für Redundanz:**
  - 2× 4-kW-Systems: 16,000–20,000 EUR
  - mit Umschalt-Logik: +2,000 EUR
  - über 20 Jahre: amortisiert sich nicht privat, aber sinnvoll für Charter
- **Minimale Alternative:** Tragbare Notfall-AC (kleine Verdampfer mit Batterie-Betrieb, 3,000 EUR)

### F-15: Was bedeutet "COP" (Coefficient of Performance)?

**Antwort:**
- **COP = Kühlleistung / Stromaufnahme**
  - Beispiel: 4 kW Kühlung / 1.5 kW Strom = COP 2.7
- **Interpretation:**
  - COP >3.0 = sehr effizient (moderne Systeme ab 2015)
  - COP 2.5–3.0 = standard (Mittelfeld)
  - COP <2.0 = ineffizient (alte Systeme, wartungsbedürftig)
- **Größerer Effekt:** Seawater-Temperatur
  - Bei 10°C: COP bis 4.0 möglich
  - Bei 25°C: COP fällt auf 2.0

### F-16: Kann ich AC winterfest machen?

**Antwort:**
- **Seacock:** Mit Ball-Ventil in Rohr einbauen, beide Seiten absperren (Winter-Stillstand)
- **Verdampfer:** Mit Dichtkappe versehen (verhindert Kondensation)
- **Kältemittel:** Im System lassen (moderne Systeme sind dicht genug)
- **Öl:** Alle 4 Jahre wechseln, auch wenn nicht verwendet
- **Kosten für Winterfest-Umbau:** 400–800 EUR (Ventil-Installation, Dichtungen)

**Wiederin-Betriebnahme im Frühjahr:**
- Druck-Check, Öl-Kontrolle, Testlauf 30 Min
- Kosten: 200–400 EUR (Inspektions-Service)

### F-17: Wie finde ich einen seriösen AC-Fachbetrieb?

**Antwort:**
- **Kriterien:**
  - Zertifizierung: AQUA-Zertifikat (Kältegewerbe) oder Hersteller-Autorisierung
  - Referenzen: Bootshersteller, Charter-Flotten
  - Equipment: Evakuierungs-Anlage, Druck-Prüfstand, Tracer-Gase-Detektor
  - Garantie: Mindestens 2 Jahre auf Material + Arbeit
- **Preisvergleich:** 3 Angebote einholen; wenn >30 % Unterschied → nachfragen
- **Rote Flaggen:**
  - "Kältemittel auffüllen statt Leckage suchen"
  - "Keine Druck-Messung gezeigt"
  - Keine schriftliche Quittung

### F-18: Welcher Kompressor-Typ ist besser: Scroll vs. Kolben?

**Antwort:**
| Typ | Scroll | Kolben |
|---|---|---|
| Effizienz | Höher (+10 %) | Standard |
| Lärmemission | Leiser (−5 dB) | Lauter |
| Wartung | Weniger (20 Jahre) | Mehr (12 Jahre) |
| Kosten | +800 EUR | Standard |
| Einsatz | Neuboote ab 2015 | ältere Systeme |
| Lagerschaden-Risiko | Niedrig | Höher (nach 10 J) |

**Empfehlung:** Bei Neubau Scroll wählen. Bei Retrofit Kolben ausreichend.

### F-19: Kann Feuchtigkeit AC-Systeme beschädigen?

**Antwort:**
- **Ja.** Wasser im Kältemittel:
  - Bildet Salpetersäure mit Öl → Korrosion inneren Bauteile
  - Gefrierpunkte unter 0°C → Kapillarrohr-Blockade
  - Verdampfer-Oberfläche-Rost
- **Prävention:**
  - Trockenmittel-Filterkartusche alle 2 Jahre wechseln (150–250 EUR)
  - System nie lange offen halten (max. 30 Min während Wartung)
  - Winterlagerung: Seacock dicht, Verdampfer-Kappe auf
- **Nachweise:** Labor-Feuchtemessung <200 ppm (Kosten: 100–200 EUR)

### F-20: Wie long hält ein AC-System typischerweise?

**Antwort (Lebensdauer nach Komponente):**
| Komponente | Lebensdauer | Austausch-Kosten |
|---|---|---|
| Kompressor | 10–15 Jahre | 2,800–4,500 EUR |
| Verdampfer | 15–20 Jahre | 3,500–6,000 EUR |
| Kondensator | 12–18 Jahre | 2,500–4,500 EUR |
| Regelventil | 10–12 Jahre | 400–800 EUR |
| Seacock | 8–10 Jahre | 600–1,200 EUR |
| Schläuche | 8–12 Jahre | 300–800 EUR |
| Elektronik | 10–15 Jahre | 600–1,200 EUR |
| **Gesamtes System** | **12–15 Jahre (Mittel)** | **6,000–12,000 EUR Modernisierung** |

**Regel:** Nach 12 Jahren erhöhen sich Reparatur-Kosten sprunghaft; dann Komplett-Modernisierung erwägen.

### F-21: Sollte ich AC mit Wasserbett/Pool-Pump kombinieren?

**Antwort:**
- **Ja, aber mit Vorsicht:** Gemeinsame Seawater-Leitungen:
  - Druck-Differenzen können Fehler auslösen
  - Separate Intake-Filter für AC notwendig (verhindert Pump-Blockade)
  - Isolation mit Absperrventilen empfohlen
- **Kosten:** +500–1,200 EUR für Rohrleitungs-Optimierung
- **Benefit:** Reduziert 2× Seacock-Betätigung

### F-22: Kann ich AC-Effizienz mit Isolation verbessern?

**Antwort:**
- **Ja, direkt:** Bootsrumpf-Isolation (K-Flex, Armaflex) senkt Wärmezufuhr um 30–40%
  - Installation: 3,000–8,000 EUR (abhängig von Bootsgröße)
  - Amortisation: 5–7 Jahre (Treibstoff-Ersparnis)
- **Ja, indirekt:** Verdampfer-Leitungs-Isolation (Armaflex Rohre):
  - Installation: 200–400 EUR
  - Effekt: +5–10 % Kühlleistung (Kondenswasser-Verlust verhindert)

### F-23: Wie sicher ist ein AC-System?

**Antwort:**
- **Brennstoff-Sicherheit:** Kältemittel nicht brennbar (R134a), aber Polyol-Öl ist entzündlich
  - Brandschutz: Feuermelder in Motor-/AC-Raum erforderlich
- **Druck-Sicherheit:** Hochdruckventil öffnet bei >28 bar, verhindert Rohr-Platzer
- **Elektrik-Sicherheit:** Thermoschutzschalter unterbricht Strom bei >65°C
- **Seawater-Eindringung:** Verdampfer kann nicht überflutet werden (Hochdruck schiebt Wasser zurück)
- **Empfehlung:** Jährliche Sicherheitsprüfung (TÜV / Klassifikations-Gesellschaft, 150–300 EUR)

> ⚠️ **ZU PRÜFEN (Audit):** Sicherheits-Druckschwelle im Dokument widersprüchlich — hier "Hochdruckventil öffnet bei >28 bar", im Glossar (Kap. 9) und im Pydantic-Validator (Anhang I.1) "Hochdruck-Schalter >30 bar", in Tabelle 10.3 dagegen "Hochdruck >32 bar (FB-26-03-007)". Zusätzlich schwankt der genannte Normal-Hochdruck zwischen 18–25 bar (Kap. 6 / Anhang C) und 16–18 bar (Erweiterungs-Atlas). Sicherheitskritischer Auslösewert — Richtung nicht zweifelsfrei belegbar, daher nicht korrigiert. Confidence: estimated — unverifiziert.

### F-24: Welche AC-Marke ist am zuverlässigsten?

**Antwort (empirisch nach Charter-Flotten & Langzeitdaten):**
| Marke | Zuverlässigkeit | Verfügbarkeit Service | Kosten | Notiz |
|---|---|---|---|---|
| **Dometic** | 90 % | Ausgezeichnet | Standard | Marktführer, gute Teile-Verfügbarkeit |
| **Frigomar** | 88 % | Gut | Standard | Italienische Marke, EU-Service |
| **Webasto BlueCool** | 92 % | Ausgezeichnet | +15 % | Sehr zuverlässig, Premium-Segment |
| **Climma** | 85 % | Mäßig | −10 % | Budget-Option, Service schwieriger |
| **Vetus** | 87 % | Gut | Standard | Holländisch, Boot-Spezialisten |

**Faustregel:** Hauptkriterium ist nicht die Marke, sondern die Wartungs-Konsistenz. Gut gewartete Dometic schlägt schlecht gewartete Webasto.

### F-25: Kann ich AC-Steuerung automatisieren?

**Antwort:**
- **Ja, moderner Standard:** IoT-Fernbedienung (Smartphone-App) seit ~2018
  - Kosten: +1,500–3,000 EUR bei Neuinstallation
  - Retrofit: +2,000–4,000 EUR (Elektronik-Modul + Verkabelung)
  - Funktion: Temperatur-Vorwahl, Zeitprogrammierung, Fehler-Alerts
- **Intelligente Funktionen (Premium):**
  - Feuchtigkeits-basierte Schaltung (RH >60% → AC läuft)
  - Seawater-Temperatur-adaptive Hochdruck-Regelung
  - Kosten: +3,000–5,000 EUR

### F-26: Wie viel Strom zieht eine AC-Anlage?

**Antwort (230V-Bordnetz-Beispiele):**
| System-Größe | Typ | Stromaufnahme (A) | Diesel-Äquivalent (l/h) |
|---|---|---|---|
| 2–3 kW | Kleine Deck-Unit | 15–20 A | 0.8–1.2 l/h |
| 4–5 kW | Medium Verdampfer | 25–35 A | 1.5–2.2 l/h |
| 8–10 kW | Große Split-Anlage | 45–60 A | 2.5–3.5 l/h |
| 12+ kW | Chilled-Water-System | 80–100 A | 4.0–5.5 l/h |

**Gesamtkost (monatlich bei 4h Betrieb/Tag):**
- 4-kW-System: 50–80 EUR Diesel/Monat + 80–150 EUR Wartungs-Reserve = 130–230 EUR/Monat

---

## GLOSSAR (40+ Terme)

- **Absorption:** Wärmeaufnahme durch Verdampfer (Phasenwechsel flüssig → gasförmig)
- **Amperemeter:** Stromquantifizierungsmessgerät; Boot-AC sollte bei Volllast 30–60A zeigen
- **Ansaugdruckleitung:** Rückleitung von Verdampfer zu Kompressor
- **Armaflex:** Isolierschaum-Material (K-Flex Konkurrent) für Rohre & Dampfleitungs-Isolierung
- **Azeotrope Mischung:** Kältemittel-Blending (R134a ist Blend aus HFC-134a + Zusätze)
- **Bandstahl:** Metallumfassung um Rohre (Befestigung ohne Vibration)
- **Blower-Lüfter:** Verdampfer-Lüfter; sollte 80–120 CFM bei 230V pushend wirken
- **BlueCool:** Webasto AC-Produktline (Premium, sehr zuverlässig)
- **Boil-off:** Unkontrollierte Kältemittel-Verdampfung (Leckage oder Überladung)
- **Brazing:** Hartes Löten mit Silber-Stab (>600°C); nicht zu verwechseln mit weichem Löten
- **Bypassing:** Regelventil-Position, bei der Hochdruck-Gas Verdampfer umgeht (Not-Modus)
- **CFC:** Chlorfluorkohlenstoff (FCKW, Ozonloch-Verursacher, seit 1995 verboten)
- **Chimäre-Rumpf:** (Nicht AC-spezifisch) schiefe Gewichtsverlagerung, erhöht AC-Last
- **Climma:** Italienische AC-Marke (Veco S.p.A.; preiswert, Servicequalität variabel)
- **Cockpit-Durchlüftung:** Verdampfer-Kaltluft direkt in Cockpit (vs. Kajüte-Verteilung)
- **Collector Tank:** Behälter mit Schauglas zur Kältemittel-Mengen-Kontrolle
- **Compliance:** Einhaltung von ISO 9094 (Brandschutz), ISO 12217 (Stabilität)
- **Condensation Rate:** Menge Wasser aus Luft-Verdampfung (typisch 2–5 l/Tag in Tropics)
- **Cracking:** Regelmäßige Hochdruck-Freigabe zur Frost-Vermeidung (Thermostat-Funktion)
- **Critical Pressure:** Druck, bei dem Kältemittel nicht verflüssigen lässt (für R134a ~41 bar)
- **CRP (Cyano Resin Paint):** Vintage-Bootslack mit Kältemittel-Unverträglichkeit
- **Cycle Time:** Zeitspanne Kompressor-Ein bis Verdampfer-Frost-Erkennung (~10–20 Min normal)
- **Deckunit:** Einteilige AC auf dem Deck montiert (vs. Split: Verdampfer unten, Kondensator oben)
- **Degree Superheat:** °C Überwärmung Verdampfer-Auslass über Sättigungstemperatur (sollte 4–6°C)
- **Dehumidification:** Wasserdampf-Entfernung durch Verdampfer-Kondensation (Sekundär-Effekt)
- **dH / dT:** Druckdifferenz / Temperaturdifferenz (Mess-Qualitäts-Indikatoren)
- **DIN 51379:** Deutsche Norm für Schiffsdiesel (relevant Energieverbrauch AC vs. Generator)
- **Discharge Line:** Hochdruckleitung zwischen Kompressor & Kondensator
- **Dometic:** Marktführer AC-Hersteller (Schwedisch, 70+ Jahre Boot-Spezialisten)
- **Duty Cycle:** Prozentanteil tatsächlicher Kompressor-Laufzeit (z.B. 40 % Duty = 6h Betrieb/24h)
- **Dye Tracing:** Fluoreszenz-Tracer ins Kältemittel injiziert zur Leck-Suche (Fachbetrieb)
- **ECU (Electronic Control Unit):** Steuer-Elektronik für Regelventil, Hochdruck-Modulation
- **Elastomer:** Gummi-Material; NBR (Nitril) standard für Dichtungen; kann schwellen in >24°C Seawater
- **Enthalpy:** Wärmemenge im Kältemittel (Zustandsgröße auf p-h-Diagramm)
- **Evacuation / Evakuierung:** Luftentfernung aus System mit Vakuum-Pumpe vor Kältemittel-Ladung
- **Evaporator:** Verdampfer; wo Niederdruckflüssigkeit expandiert & Wärme aufnimmt
- **Expansion Valve:** Dosier-Ventil (Regel-, Kapillar- oder AutoX), steuert Kältemittel-Durchfluss
- **Frigomar:** Italienische Marke (zuverlässig, Regional-Service schwächer als Dometic)
- **GWP (Global Warming Potential):** Treibhauseffekt-Index; R134a=1430, R1234yf=4
- **Hazard-Shutdown:** Notfall-Abschaltung bei erkanntem Feuer/Leck (automatisch oder manuell)
- **Hermetic Seal:** Absolute Dichtheit ohne externe Antriebswelle (vs. Semi-Hermetic mit Shaft-Seal)
- **HCFC:** Hydrochlorofluorkohlenstoff (weniger ozonschädlich als CFC, seit 2020 auslaufend)

---

## SCHNELL-REFERENZ-TABELLE

| Symptom | Wahrscheinlichste Ursache | Erste Maßnahme | Geschätzte Kosten |
|---|---|---|---|
| Kühlt gar nicht | Strom unterbrochen oder Kompressor-Schaden | Strom-Check, Manometer-Druck prüfen | 200–500 EUR |
| Kühlt schwach | Kältemittel-Mangel oder Regelventil-Fehler | Receiver-Glas kontrollieren | 400–1,200 EUR |
| Vibriert stark | Vibrations-Isolation-Gummi verschlissen | Gummi-Blöcke anfassen, elastisch? | 200–400 EUR |
| Hochdruck zu hoch | Seawater-Temperatur oder Kondensator-Blockade | Seacock öffnen, Filter-Ansatz spülen | 80–1,500 EUR |
| Öl-Sichtglas sinkt | Öl-Rückführungs-Fehler oder Leckage | Ölabscheider & Rückführungs-Leitung prüfen | 300–1,200 EUR |
| Thermostat funktioniert nicht | Sensor-Fehler oder Elektronik-Modul | Sensor-Widerstand messen | 150–1,200 EUR |
| Seacock klemmt | Korrosion oder Kalk-Ablagerung | Seacock öffnen üben, WD-40 Versuch | 150–1,200 EUR |
| Elektrik-Abschaltung nach 15 Min | Thermoschutzschalter oder Spannungsdrop | Thermoschutzschalter warm? Kabel-Querschnitt prüfen | 200–600 EUR |
| Öl-Temperatur >80°C | Ölkühler-Blockade oder Seawater zu warm | Ölkühler-Durchfluss prüfen | 400–2,500 EUR |
| Verdampfer vereist | Regelventil-Fehler oder Superheat falsch | Verdampfer antauen, 30 Min beobachten | 300–700 EUR |

---

## ANHANG A–H: ACHT FALLSTUDIEN zu AC-Problemen

### ANHANG A: Fallstudie — Hochdruck-Kollaps in Tropengefahr

**Schiff:** 16-m-Motor-Yacht, Dometic 5-kW-Split-AC, Baujahr 2012, Einsatz: Karibik

**Ausgangslage:**
- Schiff verlässt Puerto Rico (Wasser 26°C), AC läuft normal in Segelstörung (nur 3h/Tag)
- Nach 3 Tagen kontinuierlicher Fahrt (jetzt 28°C Seawater) fällt Hochdruck auf 8 bar
- Verdampfer beginnt zu vereisen trotz Thermostat-Einstellung auf "Maximum"

**Diagnose (vor Ort):**
1. Seawater-Einlass-Temperatur = 28.5°C (bestätigt warme Gewässer)
2. Kondensator-Austritts-Temp = 35°C (Wasser strömt durch, aber nicht ausreichend gekühlt)
3. Hochdruck-Manometer: 7.5 bar (ungewöhnlich niedrig)
4. Kompressor-Strom: 18 A (normal 35 A) → Kompressor unterversorgt

**Ursache:** System war für 15°C Auslegung dimensioniert; in 28°C Gewässern kehrt sich Hochdruck-Differenz um: Seawater zu warm zum Abkühlen, Kompressor schiebt Hochdruck-Gas ohne Strom herunter

**Lösung (temporär, vor Ort):**
- Seacock 5 mm zusätzlich öffnen (wurde nur 70 % geöffnet)
- Hochdruck-Regelventil-Einstellung: Sollwert von 16 bar auf 18 bar erhöht
- Resultat: Hochdruck +3 bar, Verdampfer-Frost wieder vorhanden, Kühlung +20 %
- Kosten: Nullkosten (Einstellung)

**Lösung (dauerhaft):**
- Zweite 5-kW-AC-Unit mit eigenem Seacock-Schaltung installieren (Hochlast-Modus)
- Automatische Umschaltung: wenn Seawater >25°C → beide Units aktiv
- Kosten: 12,000 EUR (2× Unit + Installaton + Regelautomatik)
- Betriebskosten: +1.5 l Diesel/Tag (notwendig in Tropics)

**Lehre:** Hersteller-Dimensionierung ist kritisch. Standard "für 15°C Basis" ist in Tropics nicht ausreichend. Nachrüstung oder Backup-System sollte vor längeren Fahrten in warme Gewässer eingeplant werden.

---

### ANHANG B: Fallstudie — Seacock-Korrosion & Blockade

**Schiff:** 12-m-Segel-Cruiser, Frigomar 3-kW-Deck-Unit, Baujahr 2008, Einsatz: Mittelmeer

**Ausgangslage:**
- Schiff 10 Jahre in Türkei/Griechenland (Hard Water, hohe Salinität)
- Seacock-Einlass zeigt weiße Kristallablagerungen (Calciumcarbonat-Kalk)
- AC kühlt nur noch bis 18°C (statt normal 20°C Abkühlungsrate)

**Diagnose:**
1. Seacock-Öffnungswiderstand gemessen: 12 Nm Drehmoment (normal <5 Nm) → hochgradig verklemmt
2. Seawater-Einlass-Temperatur = Auslass-Temperatur (0°C Delta!) → kein Durchfluss
3. Verdampfer-Druck nur 1.5 bar (normal 3–4 bar) → Unterversorgung
4. Hochdruck-Anstieg zu 22 bar innerhalb 10 Min → System-Stau

**Ursache:** Hartes Wasser mit CaCO₃-Überladung + 10 Jahre Inaktivität (Seacock nicht regelmäßig betätigt) → Ventil-Innenraum verkalkt, Sitz-Verschleiß

**Lösung (temporär):**
- Seacock-Schacht mit Essig-Säure (10 % Essigsäure) 2h einweichen
- Vorsichtig öffnen/schließen 10× (langsam, max. 5 Nm)
- Resultat: Durchfluss wiederhergestellt, aber Rückgang wahrscheinlich
- Dauer-Provisorium: kein Plan (Essig-Lösung ist max. 1–2 Wochen Effekt)

**Lösung (dauerhaft):**
- Seacock-Austausch durch Kupfer-Spülball-Ventil (marine-grade, LAPP-zertifiziert)
- Installation mit Kupfer-Rohren (Flansch-Dichtung, 10 mm Gewinde)
- Kosten: 800 EUR Material + 600 EUR Installation = 1,400 EUR
- Wartungs-Plan: Seacock 1× monatlich öffnen/schließen zum "Trainieren"

**Vorbeugung (für zukünftige Boote):**
- Seacock-Typ wählen mit interner Schlauch-Spülung (Isolierung von Hard Water)
- Oder: Seewasser-Filter vorschalten (30 µm, wechselbar alle 6 Monate)
- Kosten für Prävention: +600 EUR bei Neubau

**Lehre:** Seacocks sind "vergessen"-Komponenten; erfordern aktives Training (monatliche Betätigung), sonst verkalken/korrodieren sie. Nach 10 Jahren sollte präventiver Austausch erwogen werden, besonders in Hard-Water-Regionen.

---

### ANHANG C: Fallstudie — Ölrückführungs-Totalausfall

**Schiff:** 18-m-Motor-Yacht, Webasto BlueCool 6-kW-Chilled-Water, Baujahr 2015, Einsatz: Nord-Ostsee

**Ausgangslage:**
- Kompressor wird "trocken": Geräusch wird schärfer über 5 Betriebsminuten
- Öl-Sichtglas sinkt von 50 % → 25 % während normaler 1-Stunden-Nutzung
- Verdampfer-Ausgang zeigt graue Öl-Flöckchen

**Diagnose:**
1. Ölstand beobachtet: fällt kontinuierlich → nicht normal (sollte konstant bleiben)
2. Ölabscheider-Filterkartusche: dunkelbraun-schwarz (überlastet)
3. Rückführungs-Leitung berührt: eiskalt (0°C) statt temperiert (25–35°C) → Blockade
4. Öl-Probe aus Verdampfer: sehr dünn (verdunstete Polyol), Metallabrieb sichtbar

**Ursache:** Ölabscheider-Filter-Lebensdauer überschritten (Hersteller vorsieht 2-Jahres-Austausch; Boot hatte nie Wartung) + Evaporator-Return-Leitung zusammengequetscht (unter Möbel-Gewicht)

**Lösung (akut):**
- Kompressor sofort abschalten (Trockenlauf-Schaden droht)
- Ölabscheider-Filterkartusche wechseln (300 EUR)
- Rückführungs-Leitung inspizieren: Kink gefunden unter Einbau-Möbel
- Leitung verlegen (alternative Routing), 200 EUR Material
- Neues Öl einfüllen: 1.5 l Polyol ISO VG 32 (200 EUR)
- **Zwischenergebnis:** AC funktioniert wieder, aber Ölprobe noch "fragwürdig"

**Lösung (aufgreifend):**
- Kompletter Öl-Wechsel durchführen (Fachbetrieb mit Evakuierungs-Anlage)
- Verdampfer-Leitungen 5× spülen (mit Spül-Öl, dann evakuieren)
- Ölabscheider-Filterkartusche neuerlich wechseln
- Gesamtkosten: 1,200 EUR
- Nach Arbeit: Öl-Probe gut, Metallabrieb <50 ppm

**Wartungs-Plan für Zukunft:**
- Ölabscheider-Filter-Wechsel: alle 18 Monate (nicht 24)
- Öl-Probe-Laboranalyse: jährlich
- Rückführungs-Leitung-Sichtprüfung: alle 6 Monate

**Lehre:** Ölrückführungs-Fehler sind tückisch; führen zu Kompressor-Lagerschaden innerhalb von Wochen. Vorbeugungs-Wartung ist deutlich billiger als Kompressor-Austausch (Differenz: 400 EUR Service vs. 4,000 EUR Ersatz).

---

### ANHANG D: Fallstudie — Verdampfer-Kalk-Blockade im Karibik-Einsatz

**Schiff:** 15-m-Gulet (Turkish Motor-Yacht), Dometic Split 4-kW, Baujahr 2005, Charter-Flotte

**Ausgangslage:**
- Nach 5 Jahren kontinuierlicher Nutzung in Karibik: AC kühlt nur noch 50 % (4 °C Abkühlungsrate statt normal 8 °C)
- Verdampfer-Oberfläche hat sichtbare Kalk-Schicht (weiß/gelblich, Dicke 0.5–1 mm)
- Hochdruck: 17 bar (normal), aber Verdampfer-Druck nur 2.0 bar (sollte 3.5 bar sein)
- Seawater-Auslass-Temp: 10°C Delta (sollte 4–6°C sein) → zu warme Verdampfer-Ausgangs-Temperatur

**Ursache:** Karibik-Wasser hat extreme Härte (CaCO₃-Konzentration 400 mg/l, vs. normal 150); über 5 Jahre Betrieb lagern sich Kalk-Kristalle auf Verdampfer-Rohre-Innen ab → reduziert Kältemittel-Durchfluss um 40 %

**Diagnose-Verfahren:**
1. Verdampfer-Rohre-Durchmesser mit Ultraschall-Dickenmessung: 8.0 mm nominal, aber nur 5.5 mm Lumen messbar (Kalk: 1.25 mm Dicke)
2. Druck-Test über Verdampfer: 0.8 bar Druckdrop (sollte <0.3 bar sein)
3. Verdampfer-Spültest mit Wasser: 15 l/min Durchfluss (sollte ≥25 l/min sein)

**Lösung (temporär, vor Ort):**
- Verdampfer-Spülung mit Zitronensäure-Lösung (10 % Säure, 2% Wasser)
- Zirkulation 30 Min mit Spül-Pumpe (externe, kleine 12V-Pumpe)
- Resultat: Kalk teilweise aufgelöst, Durchfluss auf 20 l/min → AC-Leistung +20 %
- Kosten: 80 EUR (Zitronensäure-Konzentrat)
- Dauer-Effekt: 3–4 Wochen (dann wieder Kalk-Nachbildung)

**Lösung (nachhaltig):**
- Wasserenthärtungs-Filter vor Seacock-Intake installieren
- Ionenaustauscher-Kartusche (200 Liter Kapazität)
- Filter-Austausch: alle 6 Monate = 150 EUR
- Installation: 500 EUR (Rohrleitungs-Adaptation)
- **Gesamtbudget: 800 EUR**
- Erfolg: Nach Installation 8 Monate, kein Kalk-Rückgang messbar

**Alternative Lösung (radikaler):**
- Verdampfer-Komplettaustausch (Verdampfer-Alter 5 Jahre, akzeptabler Verschleißzustand)
- Neuer Verdampfer: 4,000 EUR
- Installation mit Drucktest: 500 EUR
- **Gesamtbudget: 4,500 EUR**
- Erfolg: Neuer Verdampfer, 100 % Leistung

**Gewählte Lösung (Fachberatung):**
- Charter-Flotte kombiniert beide: einen Verdampfer mit Enthärtungs-Filter, zweiten Verdampfer mit direktem Austausch
- Begründung: Redundanz für High-End-Charter + langfristige Kostenoptimierung
- Kosten: 5,300 EUR, aber Ausfallsicherheit erhöht

**Lehre:** Wasser-Qualität ist kritischer AC-Einflussfaktor in Tropics. Prophylaktische Wasserbeh handlung (Enthärtung, Filtration) amortisiert sich über Charter-Lebenszyklen. Für 5-Jahres-Intervalle obligat.

---

### ANHANG E: Fallstudie — Elektrik-Thermoschutzschalter-Überempfindlichkeit

**Schiff:** 10-m-Segelkutter, Climma 2.5-kW-Deck-Unit, Baujahr 2010, Einsatz: Nordsee Privatsegler

**Ausgangslage:**
- AC läuft normal 20 Min, dann plötzliche Strom-Abschaltung (kein Kompressor-Brummen mehr)
- Nach 10–15 Min Warten: Neustart möglich, normal für weitere 20 Min
- "Reset"-Verhalten konsistent, frustrationsfähig für längere Fahrten
- Keine Fehlermeldung an Fernbedienung

**Diagnose:**
1. Thermoschutzschalter berühren: warm, aber nicht "heiß" (ca. 50°C)
2. Stromaufnahme während Betrieb messen (Zange-Amperemeter): 18 A (nominal 22 A für 230V/2.5kW) → leicht über-Spec
3. Hochdruck-Manometer: konstant 16 bar (normal, kein Stau)
4. Seawater-Durchfluss: ausreichend
5. Kabel vom Schalter zur AC-Unit: Querschnitt 2.5 mm² (zu dünn! sollte ≥4 mm² sein) → Wärmeverlust im Kabel

**Ursache:** Kombinierter Fehler:
- Kabel-Querschnitt zu klein → Spannungsdrop während Betrieb
- Thermoschutzschalter kalibriert auf 60°C (Fabrik-Default), aber Kompressor wird real 55–58°C erreicht
- Nach 20 Min Betrieb: Kabel-Wärmeverlust + Kompressor-Eigenwärme → 62°C Temperatur an Schalter → Auslösung

**Lösung (sofort, provisorisch):**
- Kabel-Querschnitt von 2.5 auf 4 mm² erhöhen
- Kabel neu verlegen (alte entfernen, neue installieren über Kunststoff-Schutzschlauch)
- Kosten: 200 EUR
- Resultat: Stromaufnahme sinkt von 18 auf 16 A; Kabel-Wärmeverlust −40 %
- AC-Betriebsdauer: 20 → 35 Min (verbesserert, aber nicht gelöst)

**Lösung (professionell):**
- Thermoschutzschalter-Auslöse-Temperatur neu kalibrieren
- Fachbetrieb mit Klima-Kammer: Schalter auf 65°C einstellen (höhere Toleranz)
- Kosten: 200 EUR (Material + Arbeit)
- Resultat: AC läuft 60+ Min ohne Auslösung
- Risiko: höhere Toleranz könnte bei echtem Motor-Überhitzung nicht mehr schützen

**Lösung (optimal, Kombination):**
1. Kabel-Upgrade auf 4 mm² ✓ (200 EUR)
2. Thermoschutzschalter-Kalibrierung auf 65°C ✓ (200 EUR)
3. Sekundär-Wärmesensor am Kompressor-Gehäuse installieren (elektronischer Überwachungs-Sensor)
4. Sensor mit Steuer-Elektronik verbunden (automatische Herunterfahrung bei >70°C, ohne sofortige Abschaltung)
5. Kosten: zusätzlich 400 EUR
6. Resultat: AC läuft beliebig lange, Überhitzungs-Schutz bleibt über-Monitor

**Gesamtkosten:** 800 EUR
**Dauer:** 3 Tage (Kabel-Verlegung + Kalibrierung + Sensor-Installation)

**Lehre:** Thermoschutzschalter sind Sicherheits-Geräte, aber schlecht eingestellte können verschärft zu Nutzer-Frustration führen. Professionelle Kalibrierung (nicht "Selbst-Justierung") ist empfohlen. Elektronische Redundanz (Temperatur-Monitoring) erhöht Zuverlässigkeit ohne Sicherheits-Abstriche.

---

### ANHANG F: Fallstudie — Verdampfer-Vereisungs-Zyklus in kalten Gewässern

**Schiff:** 9-m-Segel-Katamaran, Dometic Small-Unit 1.5 kW, Baujahr 2012, Einsatz: Skanden (Skandinavien)

**Ausgangslage:**
- Schiff fährt durch Finnland (Seawater 8°C, Herbst)
- AC wurde eingeschaltet (Thermostat auf 20°C), läuft 30 Min
- Verdampfer-Oberfläche beginnt zu vereisen (dicht mit Frost-Schicht)
- Kühlung fällt rapide ab (von 6 °C Delta → 2 °C Delta)
- Nach 40 Min: Verdampfer komplett vereist, AC-Luftstrom gestoppt

**Diagnose:**
1. Verdampfer-Druck: 0.5 bar (normal 3–4 bar bei 8°C Seawater → sollte aber nur 1–2 bar sein wegen niedriger Temperatur)
2. Superheat: 8°C (sollte 4–6°C sein) → Verdampfer nicht optimal nutzend
3. Regelventil-Antrieb: bewegt sich nicht (sollte bei Frost einfahren) → blockiert
4. Thermostat-Sensor berühft: zu kalt (unter 2°C, normal sollte minimal 5°C sein)

**Ursache:** Regelventil ist bei 8°C Seawater nicht kalibriert (System optimiert für 15°C). Verdampfer-Druck fällt zu schnell → Verdampfer-Oberflächentemperatur unter 0°C → Frost-Bildung → Eisaufbau → Blockade

**Lösung (akut, vor Ort):**
- AC-Ausschalter betätigen (Notfall)
- Verdampfer 30 Min "antauen" lassen (bei stillstand und warmen Kajüten-Luft)
- Nach Antauen: AC neu starten, aber Seacock halbieren (Wasserdurchfluss begrenzen)
- Resultat: geringerer Wasserstrom → höherer Verdampfer-Druck → keine Vereisungs-Neigung
- Kühlung leidet (-20 %), aber Betrieb möglich

**Lösung (dauerhaft):**
- Thermostat-Sensor kalibrieren: auf "Minimum" erhöhen (von 2°C auf 6°C Unterschwelle)
- Regelventil-Austausch: auf "kalte-Gewässer-Variante" umprogrammieren
- Hochdruck-Regelventil mit Cold-Water-Cracking installieren (35 EUR Zusatzteil)
- Einstellung: bei Verdampfer-Druck <1.5 bar → Hochdruck-Gas-Bypass zum Verdampfer-Eingang (verhindert zu niedriger Druck)
- Kosten: 600 EUR (Ventil + Arbeit + Sensor-Kalibrierung)

**Betriebsprozeudur für kalte Gewässer (Nutzer-Anleitung):**
1. Thermostat auf 18°C setzen (nicht 20°C)
2. Verdampfer-Frost alle 15 Min visuell prüfen
3. Bei Frost-Ansatz: AC 5 Min ausschalten (antauen)
4. Seacock-Durchfluss regulieren: bei 8°C nur 70 % öffnen

**Lehre:** AC-Systeme sind für Tropen-Standard (15°C+) ausgelegt. In kalten Gewässern (<10°C) erfordern spezielle Kalibrierung und benutzer-aktive Überwachung. Automatische Frost-Schutz-Systeme (High-End) sind für skandinavische/arktische Einsätze zu empfehlen.

---

### ANHANG G: Fallstudie — Brandschutz-Versagen und Feuer-Erkennungs-Aufrüstung

**Schiff:** 14-m-Motor-Yacht, Dometic AC, Alter 2005, Einsatz: kommerzielle Charter Mittelmeer

**Ausgangslage:**
- Versicherungs-Audit entdeckt: AC-Bereich hat keinen dedizierten Feuermelder
- Ölabscheider-Filterkartusche zeigt "black sludge" (Polyol-Abbau-Produkt)
- Gesamtes AC-Aggregat montiert unter Motorenraum (teilweise offen, keine Trennung von Batterien/Diesel)
- Behördliches Regelwerk (SOLAS für >20m, und auch für Charter <20m in EU): "Feuermeldern in Motorenräumen mit ölschmierenden Systemen" → nicht vorhanden

**Diagnose (Versicherungs-Check):**
1. Visuelle Inspektion: Öl-Verschmutzung um Ölabscheider sichtbar (nicht versiegelt)
2. Brandschutz-Normen-Abgleich: ISO 9094 fordert "Automatische Raucherkennung in Motorenraum" → fehlend
3. Sensor-Bestandaufnahme: nur ein Rauchmelder im Wohnbereich vorhanden (nicht für Motor-Bereich)
4. Verdampfer-Bereich: ungeschützt, AC-Rohre direkt neben Dieseltank (Nähe gefährlich)

**Ursache:** Boot wurde 2005 gebaut, Regelwerk verschärft sich kontinuierlich. Ursprüngliche Installation ist "auslaufend" nach heutigem Standard. Feuer-Erkennungs-System wurde als "optional" behandelt, obwohl tatsächlich verpflichtend für Charter-Boote.

**Sofortmaßnahmen (regulatorisch notwendig):**
1. Wärmemelder (A2-Klasse, nicht Ionisierungs-Rauchmelder!) über Ölabscheider montieren
   - Melder-Typ: 230V AC mit Batterie-Backup
   - Kosten: 120 EUR
   - Installation: 100 EUR
2. Funk-Alarm-Integration: Melder mit zentraler Alarmanlage verbinden
   - Funk-Modul: 150 EUR
   - Installation: 150 EUR
3. Feuerlöscher (zusätzlich) im AC-Bereich anbringen
   - Löscher Typ ABC, 2 kg: 80 EUR
   - Wandhalterung: 30 EUR

**Mittel-Frist-Maßnahmen (Modernisierung):**
1. Ölabscheider-Serviceplan etablieren
   - Filterkartusche-Wechsel: alle 18 Monate (nicht warten bis "black sludge")
   - Kosten: 250 EUR/Wechsel
2. Sekundäre Öl-Sammelwanne unter Ölabscheider installieren
   - Material (Kunststoff-Wanne mit Ablassventil): 150 EUR
   - Installation: 200 EUR
3. AC-Rohre isolieren und abschirmen
   - Isolier-Schlauch (Armaflex): 80 EUR
   - Arbeitsaufwand: 150 EUR

**Gesamt-Retrofit-Kosten (Sicherheit):** 1,300–1,600 EUR
**Amortisation:** über Versicherungs-Prämien-Reduktion (5–10 % Rabatt bei "Feuer-Schutz-zertifiziert")

**Lehre:** Brandschutz ist nicht optional, sondern Versicherungs- & Regelwerks-Anforderung. Alte Boote (>15 Jahre) sollten Feuer-Erkennungs-Systeme nachrüsten, insbesondere wenn AC-Ölkomponenten über ungeschützte Motorenräume laufen.

---

### ANHANG H: Fallstudie — Seawater-Lecklage über 3 Jahre (schleichender Druckabfall)

**Schiff:** 17-m-Gulet, Frigomar Split 5-kW, Baujahr 2008, Einsatz: Östliches Mittelmeer Charter

**Ausgangslage:**
- Schiff-Logbuch zeigt: AC-Hochdruck sinkt über 3 Jahre kontinuierlich
  - Jahr 1: 16 bar (normal)
  - Jahr 2: 15.5 bar (leicht sinken, +0.5 bar/Jahr)
  - Jahr 3: 14.8 bar (−0.2 bar/Monat)
- Leckage wurde nicht erkannt, weil Druck "noch funktional" war
- Nach 3 Jahren: Ölprobe-Analyse zeigt 2,500 ppm Wassereintrag (sollte <200 ppm)

**Diagnose (retrospektiv):**
1. Ultraschall-Lecklage-Detektor: lautwerdend an Kupfer-Rohr unter Kondensator → Mikro-Riss identifiziert
2. Rissgröße gemessen: 0.3 mm Durchmesser, Länge 5 mm (sehr klein)
3. Leckrate geschätzt: ~0.3 g Kältemittel/Monat (praktisch undetektierbar ohne Tagebuch-Analyse)
4. Ort: Löt-Stelle (Brazing-Joint), Kälteeinwirkung führte zu micro-cracking in Löt-Nahtstelle

**Konsequenz des unerkannten Lecks:**
- Kältemittel-Verlust: 3 Jahre × 0.3 g/Monat = 10.8 g Gesamt
- Wassereintrag: Luft-Feuchte + Wasserdampf aus Kondensation diffundierte durch Leck-Öffnung → hydrolisierte Polyol-Öl
- Verdampfer-Korrosion: erste Flecken auf Kupfer-Rohren sichtbar (Rostbraune Verfärbung)
- Hochdruck-Stabilität: Zyklisches Ein/Aus → Motorschutzrelais-Ermüdung → auf Ausfallkurs

**Reparatur-Entscheidung:**
- Option A: Lot-Reparatur der Riss-Stelle (400 EUR) → Risiko: Riss könnte später erneut auftreten
- Option B: Kupfer-Insertions-Reparatur (Patch mit Lot-Umhüllung, 700 EUR) → robuster, 90 % Erfolgsquote
- Option C: Rohrabschnitt-Austausch (1,200 EUR) → zuverlässigst, aber invasiv
- Gewählte Option: B (beste Kosten-Nutzen)

**Nach Reparatur (Fachbetrieb):**
1. Kompressor ausbauen, Rohr isolieren
2. Riss-Zone sandstrahlen (Oberflächenreinigung)
3. Kupfer-Lot + Lotpaste applizieren, Flamme-Löten (Brazing 700°C)
4. Abkühlen & Drucktest (Stickstoff bis 20 bar, 10 Min Halten ohne Druckabfall)
5. System evakuieren (Vakuum 10 mbar, 30 Min)
6. Neue Ölladung + Kältemittel-Befüllung

**Kosten (Repair + Nachbearbeitung):**
- Lot-Reparatur: 700 EUR
- Öl-Wechsel (Verdampfer-Spülung + neues Öl): 600 EUR
- Evakuierungs-Service: 400 EUR
- Druck-Nachkalibrierung: 200 EUR
- **Gesamt: 1,900 EUR**

**Nachsorge (preventiv):**
- Jährliches Druck-Tagebuch-Review (kann Leckagen früh signalisieren)
- Ölprobe-Analytik jährlich (Wassereintrag <200 ppm überprüfen)
- Kosten: 150 EUR/Jahr

**Lehre:** Kleine Lecks sind tückisch, da sie schleichend wirken. Ein Druck-Tagebuch (monatliche Notierung von Hochdruck-Messwerten) ist einfaches Frühwarn-System. Bei schleichenden Druckabfällen >0.5 bar/Jahr sollte sofort Lecklage-Diagnose erfolgen. Früh erkannte Mikro-Risse kosten <1,000 EUR Reparatur; übersehene kosten 3,000–5,000 EUR später (Kompressor-Schaden, Verdampfer-Korrosion).

---

## ANHANG I: Pydantic v2 Konfig-Beispiel für AC-Datenmodelle

```python
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

class ACMaintenanceRecord(BaseModel):
    """AC Wartungs-Aufzeichnung"""
    model_config = ConfigDict(from_attributes=True)
    
    record_id: str = Field(..., description="Wartungs-Datensatz-ID")
    boat_id: str = Field(..., description="Schiff-Identifikator")
    ac_unit_id: str = Field(..., description="AC-Aggregat-Modell")
    service_date: datetime = Field(..., description="Wartungs-Datum")
    service_type: str = Field(..., description="Wartungs-Typ (monatlich/halbjährlich/jährlich)")
    
    high_pressure_bar: Optional[float] = Field(None, description="Hochdruck-Messung in bar")
    low_pressure_bar: Optional[float] = Field(None, description="Niederdruck-Messung in bar")
    oil_level_percent: Optional[float] = Field(None, ge=0, le=100, description="Ölstand Prozent")
    oil_temperature_c: Optional[float] = Field(None, description="Öltemperatur Celsius")
    
    seawater_intake_temp_c: Optional[float] = Field(None, description="Seawater-Eingangs-Temperatur")
    seawater_outlet_temp_c: Optional[float] = Field(None, description="Seawater-Ausgangs-Temperatur")
    
    refrigerant_charge_status: str = Field("normal", description="Kältemittel-Zustand (normal/low/high)")
    leakage_detected: bool = Field(False, description="Lecklage erkannt?")
    
    technician_name: str = Field(..., description="Name Fachmann")
    notes: Optional[str] = Field(None, description="Freie Notizen")
    cost_eur: Optional[float] = Field(None, description="Kosten EUR")
    
class ACServicePlan(BaseModel):
    """AC Wartungsplan"""
    model_config = ConfigDict(from_attributes=True)
    
    plan_id: str
    boat_id: str
    ac_unit_id: str
    created_date: datetime
    
    monthly_tasks: List[str] = Field(
        default=["Ölstand-Visuelle-Kontrolle", "Hochdruck-Messung", "Verdampfer-Frost-Inspektion"]
    )
    semiannual_tasks: List[str] = Field(
        default=["Seawater-Filter-Reinigung", "Korrosion-Kontrolle", "Schalld-Prüfung"]
    )
    annual_tasks: List[str] = Field(
        default=["Komplette-Funktionsprüfung", "Druck-Test", "Ölqualität-Analyse"]
    )
    
    maintenance_history: List[ACMaintenanceRecord] = Field(default_factory=list)
    
    @property
    def next_scheduled_service(self) -> datetime:
        """Berechnet nächstes Wartungsdatum basierend auf Historie"""
        if not self.maintenance_history:
            return datetime.now()  # Sofort, wenn keine Historie
        last_service = max(m.service_date for m in self.maintenance_history)
        # Regel: nächste Wartung 1 Monat nach letzter
        return last_service.replace(month=last_service.month + 1)
```

---

## ANHANG J-R: Weitere Hersteller-Spezifika

Herstellerspezifische Produktdetails zu Dometic Cruisair, Webasto BlueCool, Frigomar und Climma sind in Kapitel 5 (Hersteller und Produktportfolio) dokumentiert.

---

**DOKUMENT ENDE (aktualisiert 2026-05-18)**

