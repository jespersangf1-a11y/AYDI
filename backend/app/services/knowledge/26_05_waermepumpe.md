---
category: "26_Heizung_Klima"
subcategory: "Waermepumpe"
title: "Wärmepumpen für Yachten – Reverse Cycle AC & Wärmequellen"
version: "1.0"
created: "2026-05-18"
language: "de"
confidence_badge: "documented"
---

# Wärmepumpen für Yachten – Reverse Cycle AC & Wärmequellen

## 1. Funktionsprinzip & Thermodynamik

### 1.1 Reverse-Cycle-AC Grundlagen

Eine Reverse-Cycle-Wärmepumpe nutzt denselben Kältekreislauf wie eine Standard-Klimaanlage, invertiert aber den Wärmestrom:

**Kühlmodus (Sommer):**
- Verdampfer innen, Kondensator außen
- Wärme wird aus der Kabine nach außen gepumpt

**Heizbetrieb (Winter):**
- Verdampfer außen, Kondensator innen
- Wärme wird von außen (Luft, Wasser) nach innen gepumpt
- 4-Wege-Magnetventil schaltet den Kältemittelfluss um

### 1.2 COP-Wert & Effizienz

**COP (Coefficient of Performance):**
- COP = Wärmeleistung [kW] / elektrische Leistung [kW]
- COP 3,5 bedeutet: 3,5 kW Wärme pro 1 kW Strom

**Typische COP-Werte nach Wärmequelle:**
| Wärmequelle | Verdampfer-Temp. | COP Heizen | COP Kühlen |
|---|---|---|---|
| Seewasser 15°C | +12°C | 4,2–5,1 | 4,8–5,5 |
| Seewasser 5°C | +2°C | 3,0–3,8 | 4,5–5,0 |
| Außenluft 10°C | +7°C | 2,8–3,5 | 3,8–4,2 |
| Außenluft 0°C | -3°C | 2,0–2,5 | 3,2–3,8 |
| Außenluft -10°C | -13°C | 1,2–1,8 | 2,5–3,0 |

**Carnot-Effizienz-Grenzwert:**
COP_Carnot = T_heiß / (T_heiß - T_kalt) in Kelvin
Bei Seewasser-Heizen (25°C → 45°C): max. COP_theo = 318K / 20K = 15,9

### 1.3 Verdichterkompressor-Typen

**Scroll-Verdichter** (80 % Marineanwendungen):
- Leise (70–78 dB)
- Guter Teillast-Betrieb
- Hohe Zuverlässigkeit
- Einsatzbereich: 5–35 kW Leistung

**Rotations-Verdichter:**
- Kompakt, hohe spez. Leistung
- Etwas höherer Verschleiß
- Dometic Cruisair nutzten häufig Rotationsverdichter

**Hubkolben-Verdichter:**
- Größere Anlagen (>40 kW)
- Höhere Wartung
- Selten unter 15m

## 2. Wärmequellen für Marine-Wärmepumpen

### 2.1 Seewasser-Wärmepumpen (Favorite)

**Vorteil:** Konstante Temp., höchster COP
**Nachteil:** Seewasser-Rohrsystem, Durchflusschalter, Verschmutzung

**Auslegung:**
- Durchfluss: ca. 2–3 m³/h pro 10 kW Heizleistung
- Max. Durchströmung: 1,2 m/s (Erosion vermeiden)
- Mindest-Durchfluss: 0,8 m/s (Biofilm-Prävention)
- Seewasser-Filter: 100 µm, 2–4 bar Druckverlust

**Typische Durchflussrohre:**
- 12 mm ø für <15 kW
- 16 mm ø für 15–30 kW
- 20 mm ø für 30–50 kW

> ⚠️ **ZU PRÜFEN (Audit):** Diese Rohr-Durchmesser widersprechen der Seewasser-Dimensionierung in Abschnitt 5.2. Nach der dortigen Formel (v = 1,0 m/s) benötigt bereits 12 kW ø 32 mm; mit den hier genannten 12–20 mm ergäben sich bei 2,5 m³/h pro 10 kW Strömungsgeschwindigkeiten von ~7 m/s und mehr — weit über der in diesem Abschnitt genannten Erosionsgrenze von 1,2 m/s. Durchmesser vor Installation nach Abschnitt 5.2 nachrechnen, nicht dieser Tabelle folgen.

**Kühlwasser-Temperatur-Überwachung:**
- Solltemperatur: 18–22°C (optimal 20°C)
- Wenn >28°C: Kondensator verschmutzt oder Durchfluss zu gering
- Wenn <10°C: Verdampfer-Frost-Risiko, Drehzahl senken

### 2.2 Luft-Wärmepumpen (Luftquellen)

**Vorteil:** Keine Rohrsysteme, einfache Installation
**Nachteil:** COP sinkt bei Kälte stark, Frost-Schutz erforderlich

**Defrost-Systeme:**
- Hot-Gas-Defrost (häufigste): heiße Gase umleiten, Verdampfer kurz aufwärmen
- Elektrischer Zusatz-Heizer bei <-5°C
- Elektronische Defrost-Steuerung prüft Verdampfer-Temp. & Außenluft-Temp.

**Kritische Parameter:**
- Lufteinlass-Position: mind. 1m vom Abgas-Auspuff, >0,5m von Regenwasser-Überläufen
- Verschmutzung der Lamellen: senkt COP um 10–20 %
- Lärmemission: 65–75 dB in 1m Abstand

### 2.3 Hybrid-Wärmepumpen

Kombiniert Seewasser + Luft:
- Im Sommer: Seewasser-Verdampfer (höchster COP)
- Im Winter: Je nach Außenluftstabilität umschalten
- Logik: Wenn T_Luft < -2°C oder Meereis droht, zu Luft wechseln

**Steuerung:**
```
IF T_seewasser > 0 AND T_seewasser < 25 THEN
  Modus = Seewasser (COP optimal)
ELSE IF T_seewasser <= 0 THEN
  Modus = Luft + E-Heizer (Frost-Prävention)
ELSE IF T_luft > 5 AND Durchfluss_seewasser > Min THEN
  Modus = Seewasser
ELSE
  Modus = Luft
END IF
```

## 3. Hersteller & Modelle – Marine-Wärmepumpen

### 3.1 Dometic Cruisair

**Modellreihe:** Cruisair Slim, Cruisair II, Cruisair Elite

| Modell | Leistung | Quelle | COP | Preis |
|---|---|---|---|---|
| Cruisair Slim 8 | 8 kW | Luft | 2,8–3,2 | 3.200 EUR |
| Cruisair Slim 12 | 12 kW | Luft | 2,9–3,3 | 3.800 EUR |
| Cruisair II 16 | 16 kW | Luft/Wasser | 3,2–4,0 | 5.100 EUR |
| Cruisair Elite 20 | 20 kW | Seewasser | 4,0–4,8 | 7.200 EUR |

**Besonderheiten:**
- Rotations-Verdichter (leise Akustik)
- Multi-Split-möglich (bis 4 Innen-Kassetten)
- Elektronische Steuerung über 24V Bordnetz
- Salzwasser-beständige Kondensatoren (Cu-Ni)

### 3.2 Webasto BlueCool

**Modellreihe:** BlueCool 5000–15000

| Modell | Leistung | Quelle | COP | Preis |
|---|---|---|---|---|
| BlueCool 5 | 5 kW | Luft | 2,6–3,0 | 2.400 EUR |
| BlueCool 8 | 8 kW | Luft | 2,8–3,1 | 3.100 EUR |
| BlueCool 12 | 12 kW | Seewasser | 3,8–4,5 | 5.800 EUR |
| BlueCool 15 | 15 kW | Seewasser | 4,2–4,9 | 6.900 EUR |

**Integration:**
- Kompatibel mit Webasto-Heizungs-Systemen (Diesel-Heizer)
- Intelligente Serienumschaltung: Im Winter zuerst Diesel-Heizer (schnelle Aufwärmung), dann Wärmepumpe (Effizienz)
- CAN-Bus für Marine-Bordnetze

### 3.3 Frigomar (italienisch)

**Modellreihe:** Maxicool, Minicool

| Modell | Leistung | Quelle | COP | Preis |
|---|---|---|---|---|
| Maxicool 15 | 15 kW | Seewasser | 4,1–4,8 | 6.500 EUR |
| Maxicool 20 | 20 kW | Seewasser | 4,3–5,0 | 7.800 EUR |
| Minicool 8 | 8 kW | Luft | 2,7–3,2 | 3.500 EUR |

**Stärken:**
- Hocheffiziente Seewasser-Wärmeaustauscher
- R410A + R32-Kältemittel-Optionen
- Platzsparend (70–80 kg Gewicht)

### 3.4 Climma (deutscher Spezialist)

**Modellreihe:** Climma Air, Climma Water, Climma Hybrid

| Modell | Leistung | Quelle | COP | Preis |
|---|---|---|---|---|
| Climma Air 10 | 10 kW | Luft | 2,9–3,3 | 3.900 EUR |
| Climma Water 16 | 16 kW | Seewasser | 4,0–4,6 | 6.400 EUR |
| Climma Hybrid 12 | 12 kW | Luft+Wasser | 3,5–4,3 | 5.900 EUR |

**Besonderheiten:**
- Deutsche Ingenieurqualität, lange Lebensdauer (15–18 Jahre)
- Einteilige Innen-/Außen-Kassetten (keine Rohrsysteme)
- Sehr gute Teillast-Effizienz

## 4. Auslegung & Dimensionierung

### 4.1 Wärmeleistungsberechnung

**Formel:**
Q [kW] = U [W/m²K] × A [m²] × ΔT [K]

**Typische U-Werte für Yachten:**
| Element | U-Wert |
|---|---|
| Fenster (Standard) | 4,5–5,5 |
| Fenster (thermisch gebrochen) | 2,8–3,5 |
| Rumpf (Holz 40mm) | 0,35–0,45 |
| Rumpf (FRP 50mm) | 0,25–0,35 |
| Decking (teak über Sperrholz) | 0,8–1,2 |
| Innenschott (Standard) | 1,5–2,0 |

**Beispiel – 12m Segelyacht, Mittelmeer-Winter (draußen 8°C, drin 20°C):**
- Rumpf: 45m² × 0,35 W/m²K × 12 K = 189 W
- Decking: 30m² × 1,0 W/m²K × 12 K = 360 W
- Fenster (8 Stck, je 0,4m²): 3,2m² × 5,0 W/m²K × 12 K = 192 W
- Lüftungsverluste (Austausch): 150 W/h × 12 K = 1.800 W
- **Gesamt-Wärmebedarf: ~2,5 kW**

→ Empfehlung: 8–10 kW Wärmepumpe (mit Reserve)

### 4.2 Stromverbrauch & Generatorauslegung

**Bei COP 3,5 und 8 kW Heizleistung:**
- Elektrische Leistung = 8 / 3,5 = 2,3 kW
- Generator (Dauerlast): mind. 4–5 kVA (mit Puffer)
- Wenn nur eine Kabine geheizt wird: 1,5–2 kW ausreichend

**Tagesverbrauch (Ostsee, Dezember):**
- 6 h Heizen à 2,3 kW = 13,8 kWh
- Mit Diesel-Generator (0,22 l/kWh): 3 Liter/Tag

### 4.3 Kältemittel-Charge

**Standard-Kältemittel:**
- R410A (HCFC-frei): 85–95 % aller neuen Anlagen
- R32 (GWP-optimiert): zunehmend, 30–40 % weniger Charge nötig
- R290 (Propan): in wenigen hochwertigen Systemen, höchste Effizienz, aber Flammbar

**Charge nach Hersteller:**
| Leistung | R410A-Charge | R32-Charge |
|---|---|---|
| 8 kW | 0,8–1,0 kg | 0,5–0,6 kg |
| 12 kW | 1,2–1,5 kg | 0,7–0,9 kg |
| 20 kW | 1,8–2,2 kg | 1,0–1,3 kg |

**Nachladung:** Alle 2 Jahre Check, bei Undichtheiten <0,5 kg/a normal.

## 5. Installation & Rohrsysteme

### 5.1 Kältemittel-Rohrleitungen

**Material:** Kupfer hart (EN 12735-1) oder mit Flare-Fittings

**Durchmesser nach Leistung:**
| Leistung | Flüssig | Dampf (Saugleitung) |
|---|---|---|
| <10 kW | 6 mm ø | 9–12 mm ø |
| 10–20 kW | 8 mm ø | 12–16 mm ø |
| 20–35 kW | 10 mm ø | 16–22 mm ø |

**Verlegung:**
- Horizontale Rohre: leichtes Gefälle (1–2 %) zur Innen-Kassette
- Vertikale Rohre: Rückschlag-Ventil in Saugleitung (Ölrücklauf bei Aus)
- Isolierung: 13–19 mm Schaumstoff (50 mm Wärmeschutz)
- Dämpfungsschleifen: gegen Vibrationen

### 5.2 Seewasser-Rohre

**Durchfluss-Anforderung:**
2,5 m³/h pro 10 kW Heizleistung

**Dimensionierung:**
```
D = √(4 × Q / (π × v)) mit v = 1,0 m/s
Beispiel: 12 kW = 3 m³/h = 0,00083 m³/s
D = √(4 × 0,00083 / (3,14159 × 1,0)) = 0,032 m = 32 mm ø
```

**Material:**
- Seewasser-Rohrleitungen: nur Kunststoff (Hart-PVC, Polyamid) oder Stahl mit Kupfer-Nickel-Beschichtung
- Niemals Kupfer direkt im Seewasser
- Adapter (Messing mit Nickel-Plattierung) zwischen Kunststoff und Edelstahl-Fitting

**Düsenoptimierung:**
- Expansion-Düse am Verdampfer-Einlass (Turbulenzen)
- Strömungs-Begrenzer nach Durchfluss-Schalter (Stabilität)

### 5.3 Kondenswasser-Ableitung

**Innen-Kassette:**
- Kondenswasser aus verdunsteter Raumluft sammelt sich am Verdampfer
- Ablaufleitung: 12–16 mm ø, Gefälle 2–3 %
- Mit Siphon (zur Geruchsprävention) und Dammensiphon (gegen Druckausgleich)

**Ablauf ins Bilgenwasser:**
- Nicht direkt ins Meer (könnte Biofilm im Seewasser-System fördern)
- Filter 100 µm vor Verdampfer-Einlass

## 6. Fehlerbild & Diagnose – Wärmepumpen

### FB-26-05-001: Kein Wärmebetrieb / Kompressor läuft nicht

**Ursachen:**
- Thermostat auf Kühlen gestellt
- 24V Stromzufuhr unterbrochen
- Thermische Überlastungsschutz ausgelöst (Druckschalter)
- Defekt: Kompressor verschweißt

**Diagnose:**
1. Thermostaten-Einstellung prüfen (Sollte auf "Heizen" stehen)
2. Stromspannung messen (24V ±10 % erforderlich)
3. Druckschalter testen (bei >28 bar sollte Strom abschalten)
4. Mit Manometer: Hochdruck messen bei Startversuch (sollte >8 bar bei Stillstand sein)

**Lösungen:**
- Sicherung/Schalter überprüfen
- Druck-Einstellschrauben am Druckschalter adjustieren (±0,5 bar)
- Kompressor-Wicklung prüfen (Ohmstab)
- Im Extremfall: Kompressor-Austausch

### FB-26-05-002: Sehr wenig Heizleistung / schwache Wärmung

**Ursachen:**
- Kältemittel-Unterlademenge (Verlust über Zeit)
- Verdampfer vereist (bei Luftquelle)
- Seewasser-Durchfluss zu gering
- Wärmeaustauscher verschmutzt (innen/außen)
- Thermostatic-Expansion-Ventil (TXV) fehlkalibriert

**Diagnose:**
1. Kältemittel-Druck (Manometer an Hochdruck + Niederdruck-Seite)
   - Normal: Hochdruck 18–25 bar, Niederdruck 3–7 bar (bei Seewasser-Verdampfer)
   - Wenn beide zu niedrig: Unterlademenge
   - Wenn Hochdruck zu hoch: Verflüssiger verschmutzt

2. Verdampfer-Temperatur prüfen (Thermometer auf Rohroberfläche):
   - Sollte bei Seewasser >8°C sein
   - Wenn <2°C: Frost-Warnung (TXV zu offen)

3. Seewasser-Durchfluss:
   - Mit Durchfluss-Schalter: muss Kontakt schließen
   - Mit Manometer: Druckverlust <0,1 bar = ausreichender Durchfluss

**Lösungen:**
- Kältemittel nachfüllen (0,1–0,3 kg, dann Druck erneut messen)
- Verdampfer abtauen (Heißgas umleiten, manuelle Defrost-Spülung)
- Seewasser-Filter wechseln / Rohre spülen
- Wärmeaustauscher mit Zitronensäure-Lösung reinigen (1:20 mit Wasser)
- TXV justieren oder austauschen

### FB-26-05-003: Kompressor-Störgeräusche (Klopfen, Rasseln)

**Ursachen:**
- Flüssigkeitsschlag (Liquid Slug): Tropfen im Saugkanal
- Hydraulischer Schlag durch TXV-Verschleiß
- Lagerschaden im Kompressor (Verschleiß)
- Vibration der Rohrleitungen

**Diagnose:**
- Sofort den Kompressor ausschalten (Schaden vermeiden)
- Saugleitung-Isolierung prüfen (eiskalt = Flüssigkeit)
- Öl-Farbe im Sichtfenster prüfen (dunkel/braun = Verschleiß, klares Öl = normal)

**Lösungen:**
- TXV ersetzen (Flüssigkeit absperren)
- Rückschlag-Ventil überprüfen (korrekte Richtung)
- Ölwechsel durchführen (50–80 % tauschen)
- Kompressor-Lager nachmachen oder austauschen
- Rohre mit Gummi-Dämplern befestigen

### FB-26-05-004: Hochdruck-Alarm (Druckschalter löst aus)

**Ursachen:**
- Kondensator (Verflüssiger) verschmutzt oder blockiert
- Zu viel Kältemittel (Übercharge)
- Non-condensable Gases (NCG) im System
- Verdampfer-Durchfluss zu gering (bei Seewasser-Quelle)

**Diagnose:**
1. Hochdruck messen (sollte <25 bar bei Normal-Betrieb sein)
2. Kondensator-Lamellen prüfen (Salzwasser-Ablagerungen?)
3. Druckschalter-Einstellung überprüfen (typ. Abschaltung bei 26–28 bar)
4. Kältemittel-Menge abwiegen (mit Waage, Sollwert auf Typenschild)

> ⚠️ **ZU PRÜFEN (Audit):** Hochdruck-Druckschalter-Abschaltung hier mit "26–28 bar" angegeben (auch FB-26-05-001: ">28 bar"), während Glossar, FAQ (F8/F19), Fehlerbild-Atlas (FB-26-05-002) und die Definition "Hochdruck-Schalter" durchgängig ">35 bar" nennen. Für R410A-Anlagen liegt der Hochdruck-Cutout typischerweise bei ~31–40 bar (450–575 psi). Der genaue Abschaltdruck ist sicherheitsrelevant und darf nicht geraten werden — verbindlich ist der Wert auf dem Typenschild bzw. Datenblatt der Einheit.

**Lösungen:**
- Kondensator mit Druckluft ausblasen oder mit Wasser spülen
- Ggf. professionelle Reinigung (Ultraschall)
- Überflüssiges Kältemittel zurückfüllen (mit Waage)
- NCG-Entlüftung durch Evakuierung
- Druckschalter-Schwellwert leicht erhöhen (max. 1 bar)

### FB-26-05-005: Niederdruck-Alarm / Druckschalter unten

**Ursachen:**
- Kältemittel-Leckage (Undichtheiten in Rohren/Fittings)
- Seewasser-Durchfluss unterbrochen (Kühlwasser-Schalter offen)
- Verdampfer völlig zugefroren (bei Luftquelle)
- Thermisches Expansions-Ventil (TXV) blockiert/geschlossen

**Diagnose:**
1. Niederdruck messen (<1 bar = zu niedrig)
2. Mit Seifenlauge alle Kupfer-Fittings überprüfen (Blasenbildung = Leck)
3. Kühlwasser-Durchfluss-Schalter prüfen (Kontakt?)
4. Verdampfer-Oberfläche prüfen (Eisbildung?)
5. TXV auditorisch testen (Zischen = funktioniert)

**Lösungen:**
- Lecks ausbessern (Fittings nachziehen, bei Kupferbruch ersetzen)
- Verdampfer abtauen (manuell wärmen oder Defrost-Zyklus)
- Kühlwasser-Schalter überprüfen und ggf. reinigen
- TXV ersetzen

### FB-26-05-006: Kompressor überlastet / schaltet ständig ab

**Ursachen:**
- Thermische Überlastung (Motorschutz)
- Hochdruck zu hoch (siehe FB-26-05-004)
- Verdampfer-Temperatur zu hoch (TXV zu offen)
- Stromspannung zu niedrig

**Diagnose:**
- Stromspannung messen (sollte 220V ±10 % sein, nicht <200V)
- Kompressor-Außentemperatur prüfen (sollte <80°C sein)
- Rückschlag-Ventil testen (sollte nur eine Richtung zulassen)

**Lösungen:**
- Stromversorgung überprüfen (Generator, Bordnetz-Spannung)
- Batterie laden oder Generator starten (zu geringe Spannung)
- Verdampfer-Luftstrom verbessern (Lamellen reinigen)
- Komprressor-Thermistance ersetzen (bei Sensor-Fehler)

### FB-26-05-007: Kondensat läuft aus / Wasserschaden innen

**Ursachen:**
- Kondenswasser-Ablaufleitung blockiert (Biofilm, Sediment)
- Ablauf-Siphon richtig versumpft (Wasser zu lange stehend)
- Verdampfer-Pfanne beschädigt oder rostig
- Druckverlust in Ablauf-Rohr (zu enge Querschnitte)

**Diagnose:**
- Ablauf-Leitungen mit Druckluft oder Spülanlage prüfen
- Siphon demontieren und reinigen
- Verdampfer-Pfanne mit Licht kontrollieren (Beschädigungen?)
- Mit Farbstoff-Injektor prüfen, wo Wasser auslaufen könnte

**Lösungen:**
- Ablauf-Rohr mit Rohrreiniger spülen (biologisches Mittel für Biofilm)
- Siphon ersetzen oder mit Desinfektions-Mittel spülen
- Verdampfer-Pfanne abdichten (Silikon) oder ersetzen
- Ablauf-Durchmesser vergrößern (mind. 12 mm ø)

### FB-26-05-008: Wärmeaustauscher im Verdampfer beschädigt / Seewasser im Kältemittel

**Ursachen:**
- Seewasser-Druck höher als Kältemittel-Druck (Rohrbruch im Wärmeaustauscher)
- Korrosion der Wärmeaustauscher-Platten
- Mechanische Beschädigung (Kavitation, Stoß)
- Biologische Verstopfung (Muschellarven, Biofilm) führt zu extremem Druckanstieg

**Diagnose:**
- Kältemittel mit Feuchtigkeit-Indikator prüfen (Farbwechsel = Wasser/Salzwasser im System)
- Öl-Farbe und -Viskosität prüfen (dunkelbraun/schwarz und dünn = Wasser/Salzwasser)
- Druckdifferenz zwischen Seewasser und Kältemittel prüfen (sollte Seewasser 0,5–1 bar höher sein)
- Verdampfer-Einlass und -Auslass kontrollieren (ungleiche Temperatur = Teilblockade)

**Lösungen:**
- Notfall-Abschaltung: System sofort auf Luftquelle umschalten (wenn Hybrid)
- Kompletten Kältekreislauf entleeren und evakuieren (mit Vakuumpumpe)
- Kältemittel und Öl ersetzen
- Wärmeaustauscher ersetzen (sehr häufig nicht reparabel)
- Seewasser-Einlass mit Bakterien-Filter (5 µm) schützen

### FB-26-05-009: Defrost-System funktioniert nicht / Verdampfer friert zu

**Ursachen:**
- Defrost-Timer defekt (bei älteren mechanischen Systemen)
- Sensor-Fehler (Verdampfer-Temperatur wird nicht gelesen)
- Hot-Gas-Magnetventil funktioniert nicht
- Defrost-Logik ist deaktiviert oder falsch kalibriert

**Diagnose:**
- Mit Thermometer auf Verdampfer-Oberfläche prüfen: sollte während Defrost >5°C sein
- Thermistor-Sensor mit Multimeter durchmessen (sollte Widerstand ändern bei Temperaturänderung)
- Hot-Gas-Leitung während Defrost prüfen (sollte warm sein)
- Magnetventil mit Prüfspannung aktivieren (sollte hörbares Klicken sein)

**Lösungen:**
- Defrost-Timer ersetzen (falls mechanisch)
- Elektronische Steuerung auf Defaults zurücksetzen
- Thermistor-Sensor ersetzen
- Magnetventil ersetzen oder reinigen (ggf. Verschmutzung)
- Defrost-Schwellwerte justieren (z.B. Start bei -3°C Verdampfer-Temp.)

### FB-26-05-010: Kältemittel-Leckage / ständiges Nachfüllen nötig

**Ursachen:**
- Micro-Lecks in Kupfer-Fittings (Vibrations-Ermüdung)
- Risse in Lötstellen (Schwachstelle)
- Verdampfer oder Kondensator-Rohrwunde
- O-Ring-Verschleiß in verschraubten Fittings

**Diagnose:**
1. Alle Fittings mit Seifenlauge überprüfen (Raumtemperatur und unter Druck)
2. UV-Leckdetektions-Öl injizieren, dann mit UV-Lampe prüfen
3. Helium-Schnüffeler einsetzen (professionell, <0,1 g/Jahr nachweisbar)
4. Druck-Test mit Stickstoff durchführen (niemals mit Kältemittel + Stickstoff mischen!)

**Lösungen:**
- Micro-Lecks in Fittings: Fitting um 0,25 Umdrehung nachziehen (nicht mehr!)
- Kleine Risse in Lötstellen: Fachmann-Reparatur (Lötprobe)
- Größere Schäden: Komponent-Austausch
- O-Ring ersetzen (bei verschraubten Fittings)
- Langzeit-Monitoring (>0,5 kg/a Nachfüllung = fachliche Inspektion)

### FB-26-05-011: Thermische Regelung schwach / Temperatur-Schwankungen

**Ursachen:**
- Thermostaten fehlkalibriert
- Raumluft-Sensor blockiert (Verschmutzung) oder positioniert schlecht
- Zu häufiges Ein-/Ausschalten (Hysteres-Bereich zu klein)
- Verdampfer-TXV-Steuerung instabil

**Diagnose:**
- Raumtemperatur mit kalibrierten Thermometer messen (gegen Bordnetz-Anzeige prüfen)
- Luftsensor-Position überprüfen (sollte >1m von Wärmequellen entfernt sein)
- Hysterese-Einstellung prüfen (typ. 1–2°C bei modernen Geräten)
- TXV-Einstellschraube lockern/anziehen (Feinabstimmung)

**Lösungen:**
- Thermostat kalibrieren (Prüfblock mit bekannter Temp. verwenden)
- Luftsensor reinigen und besser positionieren
- Hysterese-Fenster erhöhen (wenn zu häufiges Schalten)
- TXV-Schraube in Schritten von 0,25 Umdrehungen justieren und neu kalibrieren

### FB-26-05-012: Störgeräusche im Seewasser-Rohrsystem (Pfeifer, Vibration)

**Ursachen:**
- Zu hohe Durchfluss-Geschwindigkeit (>1,5 m/s Erosion)
- Strömungs-Turbulenzen hinter Düse oder Drosslung
- Lockerheit der Befestigungen (Schellen nicht angezogen)
- Kavitations-Geräusche (Druck fällt unter Sättigungsdruck, Bläschen entstehen)

**Diagnose:**
- Durchfluss-Geschwindigkeit berechnen: v = Q / A
- Mit Ohr am Rohr prüfen: hochfrequentes Pfeifen = Turbulenz oder Kavitation
- Befestigungsschrauben prüfen (sollten straffes Anzugsmoment haben)
- Druck und Temperatur am Verdampfer-Einlass/Auslass messen (Druckdifferenz vs. Durchfluss)

**Lösungen:**
- Rohrdurchmesser vergrößern (oder Leitung für niedrigere Durchfluss-Geschwindigkeit dimensionieren)
- Düse mit langem Übergang ausstatten (Turbulenzen-Minderung)
- Schrauben nachziehen (M6 = 8 Nm, M8 = 15 Nm)
- Strömungs-Stabilisatoren einbauen (Prallplatten)

## 7. Wartung & Service

### 7.1 Saisonale Wartung (Ostsee, Mittelmeer-Region)

**Frühjahrs-Inbetriebnahme (April–Mai):**
- Visuelle Inspektion aller Rohre (Kratzer, Rost-Flecken?)
- Kältemittel-Druck und -Öl prüfen
- Seewasser-Filter wechseln
- Defrost-System testen (falls noch aktiv)
- Verdampfer-Lamellen reinigen (Druckluft)
- Kondensator-Lamellen überprüfen

**Sommer-Betrieb (Juni–August):**
- Monatlich: Durchfluss-Schalter prüfen (Kontakt sollte während Betrieb geschlossen sein)
- Kondenswasser-Ablauf überprüfen (nicht blockiert?)
- Stromverbrauch überwachen (COP-Veränderungen?)

**Herbst-Vorbereitung (September–Oktober):**
- Defrost-System aktivieren/testen
- Seewasser-Filter austauschen
- Kältemittel-Charge überprüfen

**Winter-Überwinterung (November–März):**
- Alle 4 Wochen: kurzer Testbetrieb (10 min) zur Ölzirkulation
- Nach Sturm/Seegang: Seewasser-Rohre auf Beschädigungen prüfen
- Verdampfer-Frost-Schutz überprüfen (automatische Abschaltung bei <-5°C)

### 7.2 Professionelle Wartung (jährlich)

**Inspektion durch Fachwerkstatt:**
- Kältemittel-Charge wiegen und dokumentieren
- Hochdruck/Niederdruck-Prüfung unter Last
- Öl-Sichtprobe und -Färbung
- Einfüll- und Ablassventil-Dichtheit überprüfen
- Wärmeaustauscher-Effizienz testen (ΔT Einlass/Auslass)
- Rückschlag-Ventile überprüfen
- Elektrische Sicherheit (Erdung, Isolation)

**Ersatz-Intervalle:**
- Seewasser-Filter: alle 100 Betriebsstunden oder halbjährlich
- Kältemittel: nur bei Leckage oder Überalterung (>10 Jahre)
- Öl: bei Verschmutzung oder Feuchte-Indikator dunkel (alle 3–5 Jahre)
- Wärmeaustauscher-Spülung: jährlich mit Zitronensäure-Lösung (1:20)

## 8. Fallstudien

### Fallstudie 1: 15m Segelacht, Mittelmeer, Seewasser-Wärmepumpe

**Yacht-Daten:**
- LOA 15m, Breite 4,8m, Tiefgang 2,2m
- Langkielsegler mit Stahlrumpf (50mm, U=0,35 W/m²K)
- 3 Kabinen, Head mit Dusche, Kombüse, Salon
- Außentemperatur-Bereich: Winter 5–10°C, Sommer 25–35°C

**Wärmepumpen-Auslegung:**
- Seewasser-Temperatur Winter: 8°C (Mittelmeer Dezember)
- Verdampfer-Temperatur bei COP 4,2: (8 + 12) / 2 = 10°C (idealerweise)
- Wärmebedarfs-Berechnung:
  - Rumpf-Verluste: 45m² × 0,35 W/m²K × (20 - 8)K = 189 W
  - Deck-Verluste: 30m² × 1,0 W/m²K × 12 K = 360 W
  - Fenster (8×0,4m²): 3,2m² × 5 W/m²K × 12 K = 192 W
  - Lüftungsverluste: 100 m³/h Austausch × 1,2 kg/m³ × 1005 J/kg·K × 12 K ÷ 3600 = 400 W
  - **Gesamt-Wärmebedarf: 1,14 kW (baseline), mit Reserve 3–4 kW**

**Geplante Lösung:**
- Dometic Cruisair Elite 20 (20 kW Heizleistung, COP ~4,2)
- Seewasser-Durchfluss: 20 kW / (4,2 × 10 K ÷ 1,86 kJ/kg·K / 1000) ≈ 2,5 m³/h
- Rohrdurchmesser: 16 mm ø (v ≈ 1,1 m/s)

> ⚠️ **ZU PRÜFEN (Audit):** Widerspruch in sich — bei den zuvor genannten 2,5 m³/h ergibt ø 16 mm eine Strömungsgeschwindigkeit von ~3,4 m/s, nicht 1,1 m/s, und liegt damit weit über der Erosionsgrenze von 1,2 m/s (Abschnitt 2.1). Für v ≈ 1,1 m/s wäre ø ~28–30 mm nötig (vgl. Formel Abschnitt 5.2). Rohr-Durchmesser vor Umsetzung nachrechnen.

**Installation:**
- Seewasser-Einlass: Rumpf-Durchbruch auf Kielkante (Schutz vor Luft-Einzug)
- Seewasser-Filter: 100 µm, Druckschalter (Alarm bei >0,2 bar Druckverlust)
- Kältemittel-Rohr: 8 mm Durchfluss, 12 mm Saugleitung
- Innen-Kassette: 2 Split-Kassetten (Salon + Achterkabine)

**Stromversorgung:**
- Vollast 20 kW / 4,2 = 4,8 kW el.
- Generator: 10 kVA Diesel (mit Puffer für Start + Kochen)
- Betrieb: morgens 2h zum Aufwärmen = 9,6 kWh, mit Generator 2,1 Liter Diesel

**Ergebnis:**
- Winter: angenehme 20°C in 2 Stunden erreichbar
- Betriebskosten: ~2 EUR/Betriebsstunde (Diesel)
- COP-Messungen zeigen 4,0–4,5 in realem Betrieb (Modell-Prognose bestätigt)

---

### Fallstudie 2: 10m Motorboot, Ostsee, Luft-Wärmepumpe mit Defrost-Notwendigkeit

**Yacht-Daten:**
- Sportboot, GFK-Rumpf (60mm, U=0,25 W/m²K)
- Kabinenheizung primär beim Winterlager
- Außentemperatur-Bereich: Winter -8 bis +2°C
- Geplante Nutzung: September–Mai (Herbst/Winter/Frühjahr)

**Problem:**
- Seewasser <0°C im Januar/Februar (Frost-Risiko)
- Luft-Wärmepumpe muss mit Frost-Schutz arbeiten

**Lösung: Webasto BlueCool 8 mit Hot-Gas-Defrost**
- Luftquellen-Verdampfer, COP bei -5°C Außenluft: 2,2
- Defrost-Zyklus: Auto-Start bei Verdampfer <-3°C
- Elektrischer Zusatz-Heizer: 3 kW (für extreme Kälte <-10°C)

**Installation:**
- Verdampfer-Einlass: Decking-Lüftung mit Schore (gegen Schneeverwehung)
- Kondenswasser-Ablauf: direkt ins Bilgenwasser
- Thermistor-Sensor im Verdampfer-Gehäuse (Frost-Detektion)

**Betrieb bei -5°C Außenluft:**
- COP 2,2 → 8 kW Heizleistung erfordert 3,6 kW elektrisch
- Defrost-Zyklus alle 45 min. für 5–10 min. (Hot-Gas-Umschaltung)
- Während Defrost: Zusatz-Heizer aktivieren (1,5 kW el.)
- **Effektive Heizleistung: (8 - 1,5 Defrost-Verlust) = 6,5 kW kontinuierlich**

**Ergebnis:**
- Winter-Raumluftz Temperatur: stabil 16–18°C (ohne Luxus, aber komfortabel)
- Stromverbrauch bei Dauerheizen: 4–5 kW el. (5–6 kVA Generator erforderlich)
- Mit Zusatz-Diesel-Heizer (Webasto Airtop 2000): kombiniertes System erreicht 22°C schneller

---

### Fallstudie 3: 20m Segelyacht, Karibik, Hybrid-Wärmepumpe (Kühlen primär)

**Yacht-Daten:**
- Bluewater-Cruiser, 60 % Zeit auf See
- 4 Kabinen, Salon mit großen Fenstern
- Außentemperatur: ganzjährig 22–32°C
- Luftfeuchte: 70–90 % (Schimmel-Risiko ohne AC)

**Problem:**
- Primärbedarf: Kühlen in Sommer (Karibik Januar–März)
- Sekundärbedarf: Heizen selten (nur bei Nacht-Segelfahrt, Wind-Abkühlung)

**Lösung: Climma Hybrid 16 (Seewasser-dominant, Luft als Backup)**
- Seewasser-Temp. Karibik: 24–28°C (Jahr um Jahr)
- COP Kühlen bei 26°C Seewasser: 5,2
- Luft-Fallback: nur wenn Seewasser >30°C oder Bypass-Filter blockiert

**Installation:**
- Seewasser-Verdampfer: 4 m³/h Durchfluss optimal
- Kondensator (zu Luft): Split-Innenkassetten in 4 Kabinen
- Kondenswasser-Sammlung: 3 Liter/Stunde bei 26°C Delta-T
- Ablauf-Rohr: 20 mm ø mit biologischem Filter (gegen Biofilm in Bilge)

**Betrieb:**
- Tagestemperatur (Karibik Mittag): 32°C außen, Meer 26°C → Auskühlen auf 22°C dauert 30 min.
- Nacht-Modus: Thermostat auf 24°C, Wärmepumpe zyklisch (5 min an, 15 min aus)
- Stromverbrauch: 3 kW kontinuierlich (16 / 5,2 = 3,1 kW el.)
- Betriebskosten: mit 5 kVA Solar-Generator + Windanlage, minimal

**Kritische Beobachtung:**
- Nach 3 Monaten Stilllegung: Seewasser-Filter mit Muschellarven verstopft (ganz blockiert)
- Folge: System schaltet zu Luft-Verdampfer um, COP fällt auf 3,2
- Lösung: Wöchentliche Inspektion/Spülung des Filters

**Ergebnis:**
- Karibik-Saison sehr komfortabel (22–24°C in allen Kabinen)
- Dieselgenerator lädt nur 2–3h/Tag (mit Solar/Wind ergänzt)
- Hybrid-Logik arbeitet zuverlässig (Seewasser bei Verfügbarkeit, Luft als Sicherung)

---

### Fallstudie 4: 12m Motorsailer, Skandinavien, Service-Issue: Verdampfer-Wärmeleistung sinkt progressiv

**Ausgangssituation:**
- Webasto BlueCool 12 Seewasser-Wärmepumpe (2 Jahre alt)
- Mittelmeer-Sommer: normale COP 4,3
- Nach Ostsee-Saison (Salzwasser, kälteres Wasser): COP sinkt auf 3,1 in wenigen Wochen

**Symptom:**
- Hochdruck (Kondensator): 19 bar (normal 22 bar)
- Niederdruck (Verdampfer): 2,5 bar (normal 5 bar)
- Beide zu niedrig → Kältemittel-Unterlademenge vermutet

**Diagnose im Service:**
1. Kältemittel-Charge abwägen: IST 1,2 kg (SOLL 1,4 kg) → 0,2 kg zu wenig
2. Mit UV-Leckdetektions-Öl (vorher injiziert): unter UV-Lampe keine Lecks sichtbar
3. Verdampfer-Temperatur-Sensor überprüft: funktioniert
4. Seewasser-Durchfluss gemessen: 2,8 m³/h (normal für 12 kW)

**Überraschender Fund:**
- Beim Öffnen des Saugventil-Abgangs: oranges/braunes Öl abgelaufen (statt klares Öl)
- Verdacht: nicht Leck, sondern Öl-Verdünnung durch Feuchtigkeit im System

**Root-Cause-Analyse:**
- Wärmepumpe war 2 Wochen bei Außentemperatur 0°C stillgestanden (Winter-Lagerung)
- Kondensator (Luftseite) war Frost ausgesetzt
- Frost-Kondenswasser ist in das System eingedrungen (Ventil nicht dicht, oder Bypass-Leckage)

**Reparatur:**
1. System vollständig entleert (mit Vakuumpumpe)
2. Verdampfer und Kondensator ausgebaut und mit Druckluft gespült
3. Neues Öl eingefüllt (50 ml PAO-Öl mit Feuchtigkeit-Indikator)
4. Lagerungsventile überprüft und Dichtungen erneuert
5. Kältemittel neu eingefüllt (1,4 kg R410A)
6. Vakuum-Test: 10 Minuten unter <0,1 mbar Druck ohne Drucksteigerung

**Resultat:**
- Nach Reparatur: COP wieder 4,2–4,3
- Empfehlung: Im Winter Lagerungsventile schließen (isolieren) oder Heizpanzer anbringen

---

### Fallstudie 5: 18m Superyacht, Mittelmeer, Defrost-Sensor-Fehler in extremer Kälte

**Yacht-Daten:**
- Aluminum-Rumpf, custom-gebaut
- 3-Split-System mit Climma Water 24 (24 kW Seewasser-Wärmepumpe)
- 5 Kabinen separat regelbar

**Notfall-Situation:**
- Überwinterung in Split (Kroatien), Januar
- Außentemperatur: -8 bis -2°C
- Seewasser-Temperatur: +2 bis +5°C

**Problem:**
- Nach 2 Tagen Betrieb: Verdampfer völlig mit Eis bedeckt
- Defrost-System aktiviert sich nicht automatisch
- Heizleistung bricht zusammen (gefroren)

**Analyse:**
- Verdampfer-Thermistor-Sensor zeigte Wert "Fehler 0°C" (Sensor-Kabel unterbrochen)
- Elektronische Steuerung wartet auf Verdampfer-Signal <-3°C (ist aber nicht erreichbar, weil Sensor defekt)
- Defrost-Zyklus startet nicht, solange die Condition nicht erfüllt ist

**Notfalls-Behebung:**
1. Manueller Override: Defrost-Taster permanent gedrückt (Hot-Gas-Magnetventil aktiviert)
2. Verdampfer taut in 15 Minuten auf
3. Thermistor-Sensor-Kabel überprüft → Isolations-Riss bei Rohrdurchführung (Vibration)

**Permanente Lösung:**
- Thermistor-Sensor-Kabel mit Spiral-Schutzschlauch neu verlegt
- Elektronische Steuerung auf Fallback-Logik aktualisiert: "Wenn Sensor-Signal >5 Minuten fehlend, dann Defrost-Zyklus aktivieren"
- Zusätz-Sensor (Backup-Thermistor) auf Verdampfer-Gehäuse angebracht

**Lernpunkt:**
- In extremer Kälte (<-5°C Außenluft): Sensor-Redundanz kritisch
- Manuelle Bedienung sollte immer möglich sein
- Regelmäßige Kontroll-Inspektionen der Sensor-Verkabelung in Winterlagerung

---

### Fallstudie 6: 12m Motoryacht, Tropen, biologische Verstopfung von Seewasser-Filter

**Yacht-Daten:**
- Philippinen-Wasser (tropisch, biologisch hochproduktiv)
- Frigomar Maxicool 15 Seewasser-Wärmepumpe (2 Jahre in Tropen stationiert)
- Überwiegend verankert (kein Fahrtbetrieb)

**Fehler-Symptomatik:**
- Seewasser-Durchfluss-Schalter schlägt Alarm aus (Druckverlust >0,3 bar)
- COP fällt von 4,6 auf 2,8 in wenigen Wochen
- System schaltet zyklisch ein/aus (Sicherheitsschutz)

**Diagnose:**
- Filter-Element sichtbar: dunkelbraun/grün verfärbt (biologische Biofilm-Schicht)
- Mikroskopisch: Muschellarven-Plankton mit Schleim zusammengeklebt
- Nicht chemisch rein, sondern biologisch verstopft

**Root-Cause:**
- Tropische Wassertemperatur 26–32°C: optimale Bedingungen für Plankton-Blüte
- Geringer Durchfluss bei Ankerbetrieb: Plankton kann sich ansiedeln
- Standard-100-µm-Filter nicht ausreichend für tropische Zustände

**Behandlung:**
1. Filter ausgebaut und mehrmals mit Süßwasser gespült
2. Nicht erfolgreich → Filter entsorgt
3. Neuer Filter eingebaut (gleiche 100 µm Spezifikation)
4. Nach 2 Wochen: erneut Verstopfung (Problem bleibt)

**Endlösung:**
- 50 µm Filter-Einsatz (feinere Struktur, reduziert Plankton-Durchgang)
- Zusätz-Chemikalter-Biozid (Kupfer-freie Formel, da Kupfer-Rohre beim Wärmetauscher verboten)
- Wartungs-Frequenz erhöht: alle 3 Wochen Filter-Spülung statt alle 2 Monate
- Langzeit-Lösung: Antifouling-Beschichtung der Seewasser-Rohre (Kupfer-frei, z.B. Silikon-basiert)

**Resultat:**
- Nach Umstellung: Filter bleibt 6–8 Wochen sauber
- COP stabil bei 4,3–4,5
- Betriebssicherheit in Tropen deutlich erhöht

---

## 9. FAQ – Wärmepumpen & Klimatisierung

**F1: Kann ich eine Wärmepumpe auch während der Fahrt betreiben?**
A: Ja, mit Seewasser-Quelle sogar optimal (höchster COP). Mit Luft-Quelle: weniger effizient bei Fahrtwind, aber machbar. Dynamischer Druck im Verdampfer-Einlass muss beachtet werden (ggf. Drosselventil).

**F2: Wieviel Kältemittel braucht meine Wärmepumpe?**
A: Typisch 0,8–2,2 kg je nach Leistung. Genaue Menge steht auf dem Typenschild der Einheit. Nie selbst auffüllen – fachliche Betriebsstätte mit Waage und Evakuierungs-Anlage erforderlich.

**F3: Kann ich die Wärmepumpe im Winter ausschalten und nur mit einem Diesel-Heizer heizen?**
A: Ja, möglich. Diesel-Heizer sind schneller (5–10 min bis Wärme), Wärmepumpe effizienter (3h gesamte Wärmebilanz besser). Kombi-Systeme nützen beide Stärken.

**F4: Ist salzwasser-Wärmepumpe in der Ostsee im Januar möglich?**
A: Ja. Seewasser-Temperatur ca. +2 bis +5°C gibt COP 3,0–3,5 (immer noch wirtschaftlich). Defrost-Schutz ist bei Luft-Quelle <0°C nötig, nicht bei Seewasser.

**F5: Warum kostet eine Seewasser-Wärmepumpe doppelt soviel wie Luft?**
A: Seewasser-Wärmeaustauscher (Cu-Ni oder Titan) sind teuer. Rohrsystem + Filter + Durchfluss-Schalter erforderlich. Aber COP-Vorteil (35 % höher) amortisiert Mehrkosten in 3–5 Jahren.

**F6: Kann ich zwei Wärmepumpen parallel betreiben?**
A: Technisch ja, aber kompliziert. Kältemittel-Systeme müssen von Fachleuten vernetzt werden. Meist reicht eine größere Einheit mit Split-Kassetten besser.

**F7: Wie oft muss ich die Wärmepumpe warten?**
A: Jährliche Profi-Wartung empfohlen. Monatliche Selbstkontrollen: Filter-Druck, Durchfluss, Stromverbrauch, Kondenswasser-Ablauf.

**F8: Was kostet ein Kältemittel-Nachfüllen?**
A: 150–300 EUR für Diagnostik + 0,1–0,3 kg Nachfüllung. Wenn >0,3 kg fehlt: Lecks finden + reparieren (teurer, 400–800 EUR).

**F9: Kann ich den Seewasser-Einlass selbst bauen / ändern?**
A: Besser nicht. Falsche Platzierung kann zu Luft-Einzug oder Erosion führen. Fachmann sollte prüfen (50–150 EUR Inspektionsgebühr).

**F10: Verdampfer vereist trotz Defrost – was machen?**
A: System ausschalten, manuell mit Wärme auftauen (Föhn, warmes Wasser auf Oberfläche), dann Sensor + Defrost-Logik von Fachmann überprüfen.

**F11: Kann ich eine Wärmepumpe installieren, wenn ich kein 380V habe?**
A: Ja. 230V ist möglich für Anlagen bis 10 kW. Größere brauchen 380V Drehstrom oder 3× 230V Phase.

**F12: Worauf sollte ich beim Kauf einer Wärmepumpe achten?**
A: (1) Welche Wärmequelle (Seewasser? Luft?), (2) Leistung (kW), (3) Hersteller-Service in meiner Region, (4) COP-Zertifikat prüfen, (5) Garantie (mind. 3 Jahre).

**F13: Ist eine Hybrid-Wärmepumpe komplizierter als Single-Source?**
A: Ja, minimal. Elektronische Steuerung komplexer. Aber Zuverlässigkeit oft höher (Fallback bei Quelle-Ausfall).

**F14: Kann ich die Wärmepumpe auch zur Warmwasser-Bereitung nutzen?**
A: Ja, mit Wasser-Wärmeaustauscher (Wassertank mit Heizschlange). COP sinkt leicht (2–3 statt 4), weil Wasser >60°C erforderlich ist.

**F15: Wie laut ist eine moderne Wärmepumpe?**
A: Innen-Kassette: 25–35 dB (wie Flüstern). Außen-Kondensator: 60–75 dB (wie Straßenverkehr). Bei Nachbarn Rücksicht nehmen.

**F16: Defrost-Zyklus senkt die Heizleistung – kann ich ihn ausschalten?**
A: Nein, gefährlich. Verdampfer vereist dann und zerstört den Kompressor. Defrost ist Schutz-Mechanismus.

**F17: Kann ich R290 (Propan) statt R410A nutzen?**
A: Nein, nicht ohne Fachmann + Neukalibrierung. R290 ist flammbar, braucht andere Sicherungs-Armaturen.

**F18: Nach Winter – erste Inbetriebnahme: was überprüfen?**
A: (1) Visuelle Schäden, (2) Kältemittel-Druck, (3) Seewasser-Filter (wenn vorhanden), (4) Stromspannung, (5) Defrost-Sensor (Luft), (6) Condenwater-Ablauf frei.

**F19: Kann ich die Wärmepumpe selbst reparieren?**
A: Nur einfache Dinge: Filter wechseln, Rohre prüfen. Alles mit Kältemittel: nur Profi (Zertifizierung erforderlich).

**F20: Wieviel kostet ein kompletter Austausch der Wärmepumpe?**
A: 4.000–10.000 EUR (Gerät + Installation). Nach 12–15 Jahren oft sinnvoll (Effizienz-Verbesserung, weniger Reparaturen).

**F21: Gibt es Umwelt-Bedenken bei Wärmepumpen?**
A: Kältemittel R410A ist HCFC-frei (Ozonfreundlich), aber GWP 1.900 (Treibhauswärung). R32 und R290 haben bessere GWP. Recycling beachten.

**F22: Kann ich die Wärmepumpe nachts ausschalten, um Diesel zu sparen?**
A: Ja. Raumtemperatur sinkt dann 1–2°C/h. Mit Isolation + Thermo-Management: Nachts 1–2°C kälter ist ok, morgens aufs neue aufwärmen.

**F23: Wärmeaustauscher-Wartung: wie oft?**
A: Seewasser-Verdampfer: jährlich mit Zitronensäure spülen. Luft-Kondensator: alle 2 Jahre Lamellen-Reinigung (Druckluft).

**F24: Kann ich während einer Reparatur die Wärmepumpe kurzzeitig abschalten?**
A: 1–2h ok. Länger: Raumtemperatur sinkt, Schimmel-Risiko steigt. Mit Zusatz-Heizer (Diesel) kombinieren.

**F25: Welche Tools brauche ich für einfache Wartung selbst?**
A: Manometer (Hoch/Niederdruck), Thermometer, Multimeter, Schraubenschlüssel-Set, Dichtmittel (Loctite), Reinigungsmittel.

## 10. Glossar – Wärmepumpen-Terminologie

**Absorbent:** Stoff, der Flüssigkeit aufnimmt (z.B. Silica-Gel in Trocknern).

**Hochdruck:** Druck auf der heißen Seite des Kältekreislaufs (nach Verdichter), typ. 18–25 bar.

**Niederdruck:** Druck auf der kalten Seite (Verdampfer), typ. 2–8 bar.

**Sättigungsdruck:** Druck, bei dem Kältemittel siedet/kondensiert bei gegebener Temperatur.

**Blizzard:** (ugs.) Eis-Ansammlung auf Verdampfer-Oberfläche bei Defrost-Fehler.

**Biofilm:** Mikrobielle Belag-Schicht in Seewasser-Rohren (braun/schwarz).

**Cavitation:** Blasenbildung durch Druck-Abfall unter Sättigungsdruck (Pfeif-Geräusche).

**Charge:** Gesamtmenge Kältemittel im System.

**Defrost:** Abtauungs-Zyklus (Hot-Gas oder E-Heizer).

**COP (Coefficient of Performance):** Wärmeleistung / Elektrische Leistung.

**Condenser:** Wärmeaustauscher, wo Kältemittel-Dampf zu Flüssigkeit kondensiert (außen bei Heizen).

**Drosselventil:** Drosslung des Drucks (Druckverlust erzeugt Kühlung).

**Evaporator:** Wärmeaustauscher, wo Kältemittel verdampft (innen beim Heizen).

**Expansion Valve (TXV):** Thermostatic oder elektronisches Drosselelement (Regelt Kältemittel-Durchfluss).

**GWP (Global Warming Potential):** Treibhauswärme-Äquivalenz eines Kältemittels (R410A: 1.900, R32: 675).

**Heißgasleitung:** Rohrleitung mit Kältemittel-Dampf auf der heißen Seite.

**Hysterese:** Temperatur-Fenster zwischen Ein- und Ausschalten (z.B. 22–24°C).

**Inverter-Kompressor:** Drehzahl-geregelter Verdichter (energieeffizient, Teillast-optimiert).

**Liquid Slug:** Tropfenförmiges Kältemittel im Saugkanal (Verdichter-Beschädigung).

**Magnetventil:** Elektromechanisches Ventil (4-Wege für Reverse-Cycle).

**Manometer:** Druck-Messinstrument für Hoch- und Niederdruck-Seiten.

**Ölrücklauf:** Rückfluss des Kompressor-Öls zum Verdichter (wichtig bei Stillstand).

**Osmotische Blase:** Wasser-Blasen in GFK-Rumpf durch Salz-Diffusion.

**ODP (Ozone Depletion Potential):** Ozonschicht-Abbau durch Kältemittel (R410A: 0, R12 alt: 1,0).

**Plating-Out:** Öl-Ausfall auf Metall-Oberflächen (Zeichen von Feuchtigkeit im System).

**Rückschlag-Ventil:** One-Way-Ventil (nur eine Durchfluss-Richtung).

**Saugleitung:** Rohr vom Verdampfer zum Kompressor-Eingang (großer ø, niedriger Druck).

**Spätverflüssigung:** Zu hoher Druck, Flüssigkeit erreicht Kompressor (Schaden!).

**Subcooling:** Unterkühlung der Flüssigkeit nach Kondensator (Effizienz-Verbesserung).

**Superheat:** Überhitzung des Dampfes nach Verdampfer (Schutz vor Tropfennebel).

**Thermistor:** Widerstands-Temperaturfühler (ändert Widerstand mit Temperatur).

**TXV (Thermostatic Expansion Valve):** Temperatur-geregeltes Drosselelement.

**Verdampfer:** siehe Evaporator.

**Verdichter:** siehe Kompressor.

**Verflüssiger:** siehe Condenser.

**Verschleißöl:** Dunkles, Feuchtigkeit-haltige Öl (Zeichen von Alterung).

---

## 11. Zusammenfassung & Best-Practice-Checkliste

### Checkliste: Wärmepumpen-Auswahl

- [ ] Wärmequelle identifiziert (Seewasser, Luft, Hybrid)?
- [ ] Leistungsbedarf korrekt berechnet (Isolation, Fensterfläche, Lüftung)?
- [ ] COP-Zertifikat überprüft (für Leistungsnachweis)?
- [ ] Hersteller-Support in meiner Region vorhanden?
- [ ] Stromversorgung ausreichend? (Generator, Bordnetz-Spannung)
- [ ] Platzbedarf für Innen-/Außengeräte geklärt?
- [ ] Budget incl. Installation + 5 Jahre Service geplant?

### Checkliste: Installation

- [ ] Seewasser-Einlass fachgemäß positioniert (Fachmann-Freigabe)?
- [ ] Filter, Durchfluss-Schalter, Rückschlag-Ventile in Seewasser-Kreislauf?
- [ ] Kältemittel-Rohre isoliert und vibrations-sicher befestigt?
- [ ] Kondenswasser-Ablauf mit Siphon und Gefälle?
- [ ] Elektrische Installation nach Marine-Norm (Erdung, Schutzschalter)?
- [ ] Probefahrt + Druckprüfung (Hoch/Niederdruck) bestätigt?

### Checkliste: Wartung & Service

- [ ] Jährliche Profi-Wartung geplant?
- [ ] Seewasser-Filter alle 2 Monate überprüft (oder monatlich in Tropen)?
- [ ] Kältemittel-Druck dokumentiert (Trend überwachen)?
- [ ] Defrost-Sensor (Luft-Anlagen) funktioniert?
- [ ] Kondenswasser-Ablauf frei?
- [ ] Saisonale Ein-/Ausschaltung nach Plan?

### Best-Practice: Wirtschaftlichkeit

**Vergleich Diesel-Heizer vs. Wärmepumpe (12m Yacht, Winter):**
| Szenario | Heizer-Kosten | WP-Kosten | Effizienz |
|---|---|---|---|
| 8h Heizen/Tag, 60 Tage Winter | 90 EUR Diesel | 40 EUR Strom | 2,25× besser |
| 3h Heizen/Tag, 90 Tage Winter | 68 EUR Diesel | 20 EUR Strom | 3,4× besser |

**Amortisations-Beispiel:**
- Wärmepumpe 6.000 EUR (Anschaffung + Installation)
- Diesel-Heizer 2.500 EUR (Anschaffung + Installation)
- Jährliche Betriebskosten-Einsparung: 600 EUR (bei häufigem Winterbetrieb)
- **Amortisierungszeit: 5–6 Jahre (dann 10+ Jahre Kostenersparnis)**

---

**Dokument-Ende.**

Version: 1.0 – 18. Mai 2026
Nächste Überprüfung: 2027 (bei neuen R32-Modellen oder technischen Änderungen)

---

## Fehlerbild-Atlas: Wärmepumpen-Diagnose

### FB-26-05-001: Niederdruck zu niedrig (<2 bar, Stillstand)

**Symptome:**
- Verdampfer-Lamellen frieren zu
- Kompressor läuft, kein Kühl-/Heizbetrieb
- Manometer-Anzeige <2 bar (Niederdruck)

**Root Causes (Häufigkeit):**
1. Kältemittel-Mangel (40%) – Undichtheit, Leck, Vibrationskante
2. Defekt Niederdruck-Schalter (25%) – Falsch kalibriert, unterbrochen
3. Blockade Verdampfer (20%) – Verschmutzung, Eislage, Vibration
4. Luftzug durch Lamellen (10%) – Abdichtung defekt
5. Kompressor-Ventile (5%) – Kolben-Verschleiß

**Diagnose-Schritte:**
1. Hochdruck messen → <8 bar auch LI = Verdampfer-Blockade oder Verdichter-Fehler
2. Hochdruck >25 bar = Niederdruck-Schalter falsch
3. Sichtprüfung Verdampfer-Lamellen auf Verschmutzung, Eis
4. Druckprobe: Stickstoff 5 bar × 10 min ohne Druckabfall → Dichtheit OK
5. Kältemittel-Wiegen (Service-Waage): Soll vs. IST Menge

**Sofortmaßnahme (Segler):**
- Verdampfer-Ventil manuell schließen (Bypassleitung öffnen)
- Seewasser-Durchfluss erhöhen (falls Kühl-Modus)
- Elektrische Defrost ausschalten

**Kosten Reparatur:**
- Kleine Undichtheit: 280 EUR (lokalisiert + gelötet)
- Kältemittel-Nachfüllung: 150–250 EUR (nach Menge)
- Verdampfer-Lamellen reinigen: 120 EUR
- Niederdruck-Schalter austausch: 180 EUR
- Kompressor-Überholung: 1.200–2.000 EUR

---

### FB-26-05-002: Hochdruck zu hoch (>30 bar, Stillstand)

**Symptome:**
- Sicherheitsventil pfeift (bei >35 bar)
- Wärmeabgabe ungenügend (Heizmodus)
- Kühlleistung sinkt (Kühlmodus)
- Kondensator warm zum Anfassen

**Root Causes:**
1. Seewasser-Filter verstopft (35%) – Algen, Sand, Schmutz
2. Verdichter überhitzt (25%) – Falscher COP, zu lange Laufzeit
3. Kondensator-Lamellen verschmutzt (20%) – Salzverätigung, Biofilm
4. Kältemittel-Überfüllung (15%) – Service-Fehler
5. Ölschlamm im System (5%) – Alterung des Kältemittel-Öls

**Diagnose-Schritte:**
1. Seewasser-Durchfluss (Indikator) kontrollieren → Rot = Filter voll
2. Kondensator-Lamellen prüfen (Sichtprüfung, Druckluft-Test)
3. Hochdruck-Öltemperatur messen: >65°C = Überlastung
4. Kältemittel-Menge wiegen
5. Farbtest Kältemittel-Öl (dunkelbraun = Alterung)

**Sofortmaßnahme:**
- Seewasser-Filter reinigen oder tauschen (5–15 min)
- Kondensator mit Druckluft abblasen
- Betrieb 5 min stoppen, danach neu starten

**Kosten:**
- Seewasser-Filter wechsel: 150 EUR
- Kondensator-Reinigung: 120 EUR
- Kältemittel-Reduktion: 100 EUR
- Ölschlamm-Spülung: 300–500 EUR

---

### FB-26-05-003: Kompressor läuft, aber keine Kälteleistung

**Symptome:**
- Gerät brummt/läuft, aber Verdampfer bleibt warm
- Hochdruck normal (18–22 bar), Niederdruck zu hoch (>12 bar)
- Kondensator wird nicht warm (Heizmodus)

**Root Causes:**
1. Vier-Wege-Ventil blockiert (35%) – Umschaltung Heiz/Kühl fehlgeschlagen
2. Verdampfer-Bypassventil offen (30%) – Kältestrom umgeht Verdampfer
3. Thermostat falsch kalibriert (20%) – Soll-Temperatur unterschritten
4. Kompressor-Schaden (Kolben, Ventile) (10%) – Förderung <50%
5. Sensor-Fehler (5%) – Falsche Temperatur-Erfassung

**Diagnose:**
1. Vier-Wege-Ventil-Spule durchklopfen (sollte *klick* machen)
2. Druck-Differenz messen: Sollte >10 bar sein (HI - LI)
3. Verdampfer-Bypassventil manuell prüfen
4. Thermostat-Sollwert ändern und Reaktion beobachten
5. Kompressor mit Strommesszange prüfen (Stromaufnahme <80% nominal = Fehler)

**Sofortmaßnahme:**
- Vier-Wege-Ventil-Spule 3–5× schnell ein/aus schalten
- Bypassventil manuell schließen, Test laufen lassen

**Kosten:**
- Vier-Wege-Ventil-Spule: 220 EUR
- Verdampfer-Bypassventil austausch: 180 EUR
- Thermostat-Reset: 0 EUR (oft Software)
- Kompressor-Überholung: 1.200–2.000 EUR

---

### FB-26-05-004: Ölschlieren aus Verdichter-Gehäuse

**Symptome:**
- Öl tropft aus Verdichter-Ansaugstutzen
- Ölflecken auf Grundrahmen
- Kältemittel-Geruch intensiv
- Kompressor-Laufgeräusch rauer

**Root Causes:**
1. Verdichter-Verschleiß (50%) – Kolben, Ventile, Lagersitz
2. Falsche Öl-Menge im System (30%) – Überfüllung
3. Verdichter-Überlastung (15%) – Zu lange Laufzeiten, Ölverdünnung
4. Rückfluss Kältemittel-Öl (5%) – Defekt Rückschlag-Ventil

**Diagnose:**
1. Verdichter-Öltemperatur messen: >80°C = kritisch
2. Ölprobe entnehmen (Farbtest): gelb=OK, dunkelbraun=Verschleiß
3. Druckprobe mit Stickstoff 5 bar, 10 min → Verdichter-Gehäuse prüfen
4. Rückschlag-Ventil optisch prüfen (oft zugänglich)
5. Laufstunden-Zähler prüfen (>5.000h = Austausch empfohlen)

**Sofortmaßnahme:**
- Öl auffangen (Umweltschutz)
- Laufzeit auf 2h/Tag reduzieren
- Öltemperatur-Überwachung starten

**Kosten:**
- Verdichter-Austausch (Überholung): 1.800–2.500 EUR
- Ölmenge-Anpassung: 80 EUR
- Rückschlag-Ventil: 120 EUR

---

### FB-26-05-005: Defrost-Zyklus versagt (Eislage permanent)

**Symptome:**
- Verdampfer-Lamellen sichtbar mit Eis bedeckt
- Defrost-Signal leuchtet dauerhaft (oder nie)
- Heizbetrieb stoppt (Zyklus-Fehler)
- Druck-Differenz 0 bar (Eis blockiert Strömung)

**Root Causes:**
1. Defrost-Sensor defekt (45%) – Bi-Metall-Streifen korrodiert
2. Zeit-Relais falsch kalibriert (25%) – Zyklus startet nicht
3. Vier-Wege-Ventil blockiert (20%) – Umschaltung in Defrost-Modus unmöglich
4. Verdampfer-Lamellen zu verschmutzt (10%) – Luftzirkulation blockiert

**Diagnose:**
1. Sensor durchklopfen (sollte bei -5°C Widerstand ändern)
2. Zeit-Relais manuell auslösen (Test-Modus)
3. Vier-Wege-Ventil-Spule durchklopfen (klick?)
4. Visuelle Inspekt. Verdampfer (Schmutz, Eis?)
5. Kälteleistung messen (Verdampfer-Aus-Temperatur sollte >-10°C sein)

**Sofortmaßnahme:**
- Defrost-Sensor + Relais in Parallel-Schaltung überbrücken (временно, nur 30 min Test)
- Vier-Wege-Ventil-Spule durchklopfen

**Kosten:**
- Defrost-Sensor-Austausch: 95 EUR
- Zeit-Relais: 140 EUR
- Vier-Wege-Ventil-Spule: 220 EUR
- Verdampfer-Reinigung: 150 EUR

---

### FB-26-05-006: Seewasser-Durchfluss blockiert

**Symptome:**
- Seewasser-Indikator rot/gelb (nicht blau)
- Hochdruck steigt schnell (>30 bar in 2 min)
- Kondensator-Lamellen-Temperatur erhöht
- Alarm "Durchfluss blockiert" (falls Sensor verbaut)

**Root Causes:**
1. Seewasser-Filter verstopft (60%) – Muscheln, Sand, Algenfilm
2. Seewasser-Rohr geknickt/blockiert (20%) – Schlauch-Verschleiß, Korrosion
3. Durchfluss-Indikator falsch kalibriert (10%) – Sensor-Drift
4. Wasserpumpe ausgefallen (5%) – Lagerschaden, Laufrad blockiert
5. Durchfluss-Regelventil geschlossen (5%) – Bedienungsfehler

**Diagnose:**
1. Seewasser-Filter-Behälter optisch prüfen (Schmutz?)
2. Zu- und Ablauf-Rohre mit Hand prüfen (sollten warm sein)
3. Durchfluss-Indikator von innen inspizieren (Kugel bewegt sich?)
4. Wasserpumpen-Stromaufnahme messen (sollte <1A sein)
5. Druck vor/nach Filter messen (Differenz >0,5 bar = Filter voll)

**Sofortmaßnahme:**
- Seewasser-Filter wechseln oder rückspülen (10 min)
- Durchfluss-Indikator reinigen
- Wasserpumpe manuell drehen (sollte leicht gehen)

**Kosten:**
- Seewasser-Filter-Wechsel: 150 EUR
- Seewasser-Rohr-Austausch: 180–300 EUR
- Durchfluss-Indikator-Reinigung: 60 EUR
- Wasserpumpen-Austausch: 400–600 EUR

---

### FB-26-05-007: Kältemittel-Geruch im Salon

**Symptome:**
- Typischer "süßlicher" Kältemittel-Geruch
- Kleine Öl-Flecken an Rohranschlüssen
- Druck sinkt (Hochdruck fällt nach 2 Wochen um 2–3 bar)
- Kühllast nimmt ab

**Root Causes:**
1. Rohr-Vibrations-Leck (50%) – Reibung an scharfer Kante
2. Lötnaht-Riss (25%) – Thermoschock, Materialermüdung
3. O-Ring-Verschleiß (Flange) (15%) – Alterung, Mineral-Öl
4. Ventil-Undichtheit (10%) – Spindel oder Gehäuse

**Diagnose:**
1. Lecksuchspray auftragen (UV + Farbstoff) oder Ultraschall-Lecklaster
2. Alle Rohranschlüsse visuell prüfen auf Tropfen oder Flecken
3. Druckprobe mit Stickstoff 5 bar, 10 min (alle Komponenten einzeln prüfen)
4. Fahrt-Test: Vibration beobachten während Kompressor läuft
5. Manometer-Trend dokumentieren (Druck 3× täglich messen)

**Sofortmaßnahme:**
- Verdichter-Ausgang mit Isolier-Tape umwickeln (Vibration dämpfen)
- Laufzeit auf notwendiges Minimum reduzieren
- Druck-Monitoring täglich durchführen

**Kosten:**
- Kleine Leck-Stelle löten: 200–280 EUR
- Rohr-Austausch (komplett): 350–500 EUR
- O-Ring-Satz + Flange: 120 EUR
- Ventil-Austausch: 180–250 EUR

---

### FB-26-05-008: Elektrischer Schaden (Verdichter startet nicht)

**Symptome:**
- Verdichter läuft nicht, kein Summer/Brummen
- Stromversorgung OK (24V vorhanden)
- Relais klickt, aber Verdichter bleibt stumm
- Eventuelle Rauchentwicklung beim Schaltversuch

**Root Causes:**
1. Verdichter-Motor durchgebrannt (50%) – Überlastung, Schmoren
2. Startrelais defekt (25%) – Kontakt korrodiert
3. Thermoschutzschalter hat ausgelöst (15%) – Motortemperatur >90°C
4. Stromversorgung zu schwach (5%) – Spannungsabfall >2V
5. Erdschluss (5%) – Feuchte im Motor

**Diagnose:**
1. Stromversorgung 24V messen (sollte 22–26V sein)
2. Stromaufnahme mit Strommesszange prüfen (0A = Verdichter-Motor offen)
3. Widerstand Wicklung messen (Ohmmeter): sollte 5–15Ω sein (>100Ω = offen)
4. Thermoschutzschalter: mit der Hand drücken (Reset-Button suchen)
5. Relais durchklopfen (sollte deutlich klicken)

**Sofortmaßnahme:**
- Stromversorgung 5 min ausschalten, dann neu starten (Reset-Versuch)
- Batteriespannung erhöhen (falls möglich)
- Verdichter-Motor abkühlen lassen (1 h Pause)

**Kosten:**
- Startrelais-Austausch: 140 EUR
- Thermoschutzschalter: 95 EUR
- Verdichter-Motor-Wicklung: 800–1.200 EUR (oft Gesamttausch)
- Stromversorgung-Diagnostik: 60–100 EUR

---

### FB-26-05-009: Vibrationen/Lärm beim Betrieb

**Symptome:**
- Dumpfes Brummen oder Klopfen aus Verdichter
- Kältemittel-Rohre vibrieren sichtbar
- Geräuschlevel > 80 dB
- Eventuell Druckfluktuationen (Hochdruck pendelt 2–3 bar)

**Root Causes:**
1. Verdichter-Lagerung mangelhaft (40%) – Gummilager verschlissen
2. Rohr-Befestigung locker (30%) – Befestigungs-Klammer gelöst
3. Verdichter-Ventil verschlissen (20%) – Intermittente Förderung
4. Schmutz/Verschleiß-Partikel in Kreislauf (10%) – Verdichter-Trag-Lager

**Diagnose:**
1. Gummilager visuell inspizieren (sollten nicht gekippt sein)
2. Rohr-Befestigungen durchgehen (alle Schrauben/Klammern prüfen)
3. Verdichter-Druck-Pulsation messen (Hochdruck-Manometer: Pulsation >2 bar = kritisch)
4. Verdichter-Gehäuse mit Hand anfassen (sollte nicht heiß sein, vibration moderat)
5. Magnetisch-Filter am Verdichter-Ausgang prüfen (Schmutz-Partikel?)

**Sofortmaßnahme:**
- Gummilager austausch (schnelle Reparatur, spart viel Ärger)
- Rohr-Befestigungen nachziehen
- Vibrations-Isolier-Matten unterlegen

**Kosten:**
- Gummilager-Satz (4 Stück): 80 EUR
- Rohr-Befestigungs-Hardware: 30 EUR
- Verdichter-Lageraustasch: 600–800 EUR
- Verdichter-Ventil-Überholung: 400–600 EUR

---

### FB-26-05-010: Thermostat-Fehler (Temperatur nicht regelbar)

**Symptome:**
- Sollwert-Änderung hat keine Wirkung
- Temperatur bleibt konstant oder driftet wild
- Thermostat-Display zeigt Fehlerwert oder blinkt
- Kompressor läuft permanent oder überhaupt nicht

**Root Causes:**
1. Temperatursensor defekt (55%) – NTC-Widerstand unterbrochen oder kurzgeschlossen
2. Thermostat-Software-Fehler (20%) – Firmware-Bug oder Reset nötig
3. Verdrahtet falsch (15%) – Sensor-Kabel verdreht oder locker
4. Sollwert-Potentiometer verschlissen (10%) – Reinigung oder Austausch

**Diagnose:**
1. Temperatursensor-Widerstand messen (bei 20°C sollte ca. 4,7 kΩ sein)
2. Sensor-Kabel durchklopfen (durchgang prüfen)
3. Thermostat-Spannungsversorgung prüfen (sollte 5V oder 24V sein)
4. Sollwert ändern und Reaktion beobachten (mindestens 30 s Verzögerung normal)
5. Thermostat-Reset durchführen (oft: Batterie raus 5 min, rein)

**Sofortmaßnahme:**
- Thermostat-Reset (Battery-Reset)
- Sollwert manuell auf Mittelposition stellen (Test)
- Verdichter 1h abkühlen lassen

**Kosten:**
- Temperatursensor-Austausch: 75 EUR
- Thermostat-Modul-Austausch: 250–400 EUR
- Verdrahtungs-Reparatur: 80 EUR
- Kalibrierung nach Austausch: 50 EUR

---

### FB-26-05-011: Wärmeaustauscher-Verschmutzung (Seewasser-Seite)

**Symptome:**
- Hochdruck steigt kontinuierlich (über 4 Wochen)
- Kondensator wird heiß, aber Seewasser-Ausgang bleibt kalt
- Seewasser-Durchfluss sinkt (Indikator dunkler)
- Wärmeleistung sinkt, obwohl Verdichter neu ist

**Root Causes:**
1. Kalkablagerungen (60%) – Seewasser-Mineralien, besonders in warmen Gewässern
2. Biofilm/Algen (25%) – Salzwasser-Bakterien, organische Verschmutzung
3. Korrosions-Produkte (10%) – Rost aus Rohren oder Kondensator
4. Fremdstoffe (5%) – Sand, Muschelbruchstücke, Schmutz

**Diagnose:**
1. Seewasser-Zu-/Ablauf-Temperatur messen (Differenz sollte >3°C sein)
2. Kondensator-Oberseite visuell prüfen (Kalkschicht?)
3. Zu- und Ablauf-Rohre mit Hand prüfen (sollten unterschiedlich warm sein)
4. Seewasser-Durchfluss-Indikator Position prüfen
5. Rückspül-Test: Verdichter aus, Seewasser-Reverse-Ventil öffnen, 1 min Gegenstrom

**Sofortmaßnahme:**
- Rückspülung mit Druckluft (wenn Ventil vorhanden)
- Chemische Spülung mit Zitronensäure-Lösung (1:10 Wasser)
- Seewasser-Filter wechseln (parallel)

**Kosten:**
- Chemische Spülung: 80–150 EUR
- Kondensator-Reinigung (öffnen + spülen): 200–300 EUR
- Seewasser-Rohre-Tausch (komplett): 250–400 EUR
- Kondensator-Austausch: 600–900 EUR

---

### FB-26-05-012: Verdichter-Effizienz sinkt (alte Anlagen >10 Jahre)

**Symptome:**
- Kühllast sinkt kontinuierlich (gleiche Einstellung, schlechtere Kühlung)
- Hochdruck und Niederdruck beide im Normalbereich, aber COP sinkt
- Verdichter läuft länger für gleiche Temperatur-Stabilisierung
- Stromaufnahme sinkt (Förderung schwächer)

**Root Causes:**
1. Verdichter-Verschleiß (Kolben, Ventile) (60%) – Mechanisches Play, reduzierte Förderung
2. Ölverbrauch (30%) – Verdampfer-Öl-Mangelversorgung
3. Magnetisch-Partikel im Kreislauf (5%) – Verdichter-Verschleiß-Produkte
4. Kältemittel-Alter (5%) – Öl-Oxidation, Säurebildung

**Diagnose:**
1. COP-Berechnung: QKälte / P-Eingang messen (sollte COP >2,5 sein)
2. Verdichter-Stromaufnahme mit Trend dokumentieren (IST vs. Nenndatenblatt)
3. Verdampfer-Austritt-Temperatur messen (sollte <-5°C sein bei normaler Kühlung)
4. Ölprobe aus Verdichter (Farbtest + Säurezahl-Check im Labor)
5. Magnetisch-Filter-Inspektion (schwarzer Schlamm = Verschleiß)

**Sofortmaßnahme:**
- Kältemittel-Öl nachfüllen (oft hilft, kurzfristig)
- Magnetisch-Filter wechseln
- Seewasser-Durchfluss erhöhen (falls verfügbar)
- Druck-Spülung (Stickstoff 5 bar, 5 min)

**Kosten:**
- Verdichter-Überholung: 1.200–1.800 EUR
- Verdichter-Austausch (Komplett): 2.500–3.500 EUR
- Ölspülung mit magnetisch-Filter: 150–200 EUR
- Kältemittel-Nachfüllung: 100–200 EUR

---

## Troubleshooting-Entscheidungsbäume

### Baum A: Verdichter startet nicht

```
START: Verdichter läuft nicht
├─ JA: Stromversorgung 24V? → NEIN → Batterie prüfen, Kabel prüfen (FB-26-05-008)
├─ JA: Relais klickt? → NEIN → Relais durchklopfen (FB-26-05-008)
│   ├─ JA: Stromaufnahme >5A während Versuch? → NEIN → Motor defekt (FB-26-05-008)
│   └─ JA: Verdichter brummt? → JA → Steckerrotor blockiert, Verdichter öffnen
└─ JA: Thermoschutzschalter greift? → JA → 2h Abkühlung, Reset versuchen (FB-26-05-008)
    └─ NEIN: Druckschalter prüfen (zu hoher Hochdruck?)
```

### Baum B: Keine Kälteleistung

```
START: Verdichter läuft, aber keine Kühlung
├─ Hochdruck <8 bar? → JA → Verdampfer blockiert oder Verdichter schwach (FB-26-05-001)
├─ Niederdruck >12 bar? → JA → Vier-Wege-Ventil falsch, Bypass offen (FB-26-05-003)
├─ Hochdruck 18–22 bar, Niederdruck 3–8 bar (normal)? 
│   ├─ JA: Verdampfer-Temperatur <-5°C? → JA → System arbeitet, aber Kalt-Zirkulation blockiert
│   └─ NEIN: Thermostat-Sollwert prüfen, neukalibrieren (FB-26-05-010)
└─ Druck-Differenz <5 bar? → JA → Kompressor-Schaden (Ventile, Kolben)
```

### Baum C: Hochdruck zu hoch (>30 bar)

```
START: Hochdruck >30 bar
├─ Seewasser-Indikator rot/gelb? → JA → Filter verstopft (FB-26-05-006)
├─ Kondensator-Lamellen verschmutzt? → JA → Abblasen oder Reinigung (FB-26-05-002)
├─ Kältemittel-Menge prüfen (Füll-Waage)? → ÜBER → Überfüllung reduzieren (FB-26-05-002)
├─ Verdichter-Öltemperatur >70°C? → JA → Abkühlung, Laufzeit reduzieren (FB-26-05-004)
└─ Hochdruck persistiert nach allen Maßnahmen? → Verdichter-Überholung (FB-26-05-012)
```

### Baum D: Undichtheit / Kältemittel-Verlust

```
START: Druck sinkt kontinuierlich
├─ Sichtbar Öl/Lecks? → JA → Lecksuch-Spray auftragen (UV+Farbstoff) (FB-26-05-007)
│   ├─ Rohr-Vibrations-Leck? → Verkleidung, dann löten oder Rohr-Austausch
│   ├─ Flansche undicht? → O-Ringe austausch
│   └─ Ventil-Undichtheit? → Ventil-Austausch
├─ Keine sichtbaren Lecks? → Mikroskopisches Leck → Druckprobe mit Stickstoff
│   ├─ Druckabfall <0,5 bar / 10 min → normale Diffusion (akzeptabel)
│   └─ Druckabfall >1 bar / 10 min → Leck vorhanden (lokalisiert nach Komponente)
└─ Druckprobe-negativ, aber Druck sinkt? → Ventil-Lecks (intern)
```

### Baum E: Seewasser-Kreislauf-Fehler

```
START: Hochdruck steigt oder Durchfluss blockiert
├─ Seewasser-Indikator? → ROT → Seewasser-Filter voll (FB-26-05-006)
│   └─ Sofort: Filter wechseln oder rückspülen
├─ Filter OK, aber Durchfluss immer noch niedrig?
│   ├─ Seewasser-Rohr geknickt/blockiert? → Visuell prüfen
│   ├─ Wasserpumpe fehlt Strom? → Stromprüfung
│   └─ Verdichter-Hochdruck >30 bar? → Wasserpumpe zu schwach, Druck-Relief prüfen
├─ Hochdruck bleibt hoch auch mit gutem Durchfluss?
│   ├─ Kondensator-Lamellen verschmutzt? → Druckluft abblasen (FB-26-05-011)
│   └─ Thermisch unzureichend? → Wärmeaustauscher-Kalkspülung (FB-26-05-011)
└─ Kompletter Wasserpumpen-Ausfall? → Motor prüfen, Laufrad blockiert? (FB-26-05-006)
```

---

## Häufig gestellte Fragen (FAQ)

**F1: Darf ich die Wärmepumpe Winter + Sommer einschalten?**
A: Ja, saisonal. Im Winter Heizbetrieb, im Sommer Kühlbetrieb. Umschaltung automatisch über Vier-Wege-Ventil. Allerdings: Gerät 3–4 Wochen vor Saisonwechsel prüfen (Drucktest, Sensor-Kalibrierung), da thermische Lasten unterschiedlich sind.

**F2: Wie oft braucht Seewasser-Filter-Wechsel?**
A: In gemäßigtem Klima (Nord-/Ostsee) alle 2–3 Monate. In tropischen Gewässern oder nach Algenblüten alle 2–4 Wochen. Indikatoren nutzen: wenn Hochdruck >30 bar und Durchfluss-Indikator rot, dann sofort wechseln.

**F3: Kann ich Verdichter selbst austausch?**
A: Nicht empfohlen. Verdichter-Austausch braucht: Vakuum-Pumpe, Kältemittel-Wiege, Druckprobe-Equipment. Kosten Spezialwerkzeug: 500–1.000 EUR. Besser: Fachbetrieb. Dauer: 4–6h.

**F4: Wie erkenne ich, ob Kältemittel zu wenig ist?**
A: Symptome: Niederdruck <3 bar, Verdampfer-Lamellen frieren, Hochdruck sinkt. Messung: Service-Techniker misst mit Waage (Sollmenge vs. IST). Typisch: Wärmepumpe 2–4 kg Kältemittel, Toleranz ±5%.

**F5: Was ist COP und warum sinkt es?**
A: COP (Leistungszahl) = abgegebene Wärmeenergie / eingesetzte Stromenergie. Sollte >2,5 sein. Sinkt durch: Verdichter-Verschleiß, Wärmeaustauscher-Verschmutzung, Öl-Mangel, falsche Kältemittel-Menge.

**F6: Muss ich Verdichter jährlich warten?**
A: Ja, empfohlen. Inspekt.: Druck-Messung, Ölprobe, Vibrations-Check, Stromaufnahme. Zeit: 1–1,5h. Kosten: 150–250 EUR.

**F7: Kann Defrost-Zyklus manuell ausgelöst werden?**
A: Ja, üblicherweise über Test-Knopf am Thermostat oder Vier-Wege-Ventil-Spule durchklopfen. Dauer: 10–15 min. Wenn danach Eis weg, Sensor OK. Falls Eis bleibt, Sensor defekt.

**F8: Warum pfeift das Sicherheitsventil?**
A: Hochdruck >35 bar, Sicherheitsventil öffnet. Ursachen: Seewasser-Filter voll, Kondensator verschmutzt, Kältemittel-Überfüllung. Sofortmaßnahme: Alle drei prüfen.

**F9: Ist Wärmepumpe energieeffizienter als Diesel-Heizer?**
A: Ja, 2–3× effizienter. Wärmepumpe COP 2,5 = 1 EUR Strom = 2,5 EUR Heizwert. Diesel-Heizer: 1 EUR Diesel = ca. 1 EUR Heizwert (effizienz ~90%). Aber: höhere Investition (+3.000–4.000 EUR).

**F10: Kann Wärmepumpe in Tropfen-Temperatur arbeiten?**
A: Grenze meist -5°C (Außentemperatur), manche bis -10°C. Unter -5°C: Defrost-Zyklus sehr häufig, COP sinkt auf <1,5. Nicht wirtschaftlich. Dann eher Diesel-Heizer + kleine Wärmepumpe für Frühjahr/Herbst.

**F11: Schädigt Salzwasser die Verdichter?**
A: Nein, Verdichter ist hermetisch versiegelt. Aber: Seewasser-Kondensator braucht spezielle Materialien (Kupfer-Nickel, Titan). Salzwasser-Rohre alle 2 Jahre prüfen auf Korrosion.

**F12: Was kostet Notfall-Reparatur in Marina?**
A: Verdichter-Austausch 2.500–3.500 EUR, dazu Arbeit 8–12h (200 EUR/h = 1.600–2.400 EUR). Total: 4.000–5.900 EUR. Keine Ersatzteile verfügbar? +2 Wochen Wartezeit. Deshalb: Prävention wichtig!

**F13: Darf ich Kältemittel selber nachfüllen?**
A: Nein, in EU illegal ohne Zertifikat (Kältemittel-Verordnung). Fachbetrieb muss dies machen. Kostenpunkt: 150–250 EUR.

**F14: Wie prüfe ich Verdichter auf Stromaufnahme?**
A: Strommesszange (Clamp Meter) an eine Phase-Leitung halten. Sollte während Betrieb 30–60A sein (abhängig Nennwert). <20A = schwache Förderung. >80A = Überlastung.

**F15: Welche Servicetemperatur für Vier-Wege-Ventil?**
A: Schalttemperatur üblicherweise zwischen Heizbetrieb (alle 5–10 min) und Kühlbetrieb (kontinuierlich). Sollte klick-Geräusch machen beim Umschalten. Falls nicht: Spule durchklopfen oder Austausch.

**F16: Kann ich Verdampfer selbst reinigen?**
A: Ja, vorsichtig. Lamellen sind fragil. Methode: Druckluft (max. 2 bar) oder warmes Wasser + feiner Bürste. NICHT: Druckwasser (>3 bar), Stahlbürste. Verdampfer öffnen: ca. 1–2h Arbeit, braucht spezial-Werkzeug.

**F17: Was ist beste Betriebstemperatur für Wärmepumpe?**
A: Sollte: 18–22°C. Nicht unter 16°C setzen (Defrost-Zyklus zu häufig). Nicht über 28°C setzen (COP sinkt, Stromverbrauch steigt). Saisonale Anpassung: Winter 19°C, Sommer 21°C.

**F18: Wie erkenne ich Ölschlamm?**
A: Ölprobe zeigen dunkle Färbung (nicht gelb). Laboranalyse: Säurezahl >0,5 = kritisch. Visuell: Verdichter-Ausgang-Filter dunkelbraun = Ölverschleiß. Dann: Spülung + Öl-Austausch.

**F19: Darf Wärmepumpe unbeaufsichtigt laufen?**
A: Ja, aber mit Sicherheitsventil + Hochdruckschalter. Überwachung empfohlen: Monatlich Druck-Check, Stromaufnahme-Trend, Öltemperatur. Automatische Abschaltung bei >35 bar (obligatorisch).

**F20: Was tun bei Vibrationen?**
A: Erst: Gummilager prüfen + austausch (80 EUR, löst 80% Vibrationen). Dann: Rohr-Befestigungen straffen. Zuletzt: Verdichter-Lagersitze prüfen (600–800 EUR). Vibrations-Isolier-Matten unterlegen (30 EUR, Erstmaßnahme).

**F21: Kann Wärmepumpe in Frostschutz-Modus fahren?**
A: Ja, viele moderne Geräte haben "Standby" bei <-15°C. Kompressor aus, aber Heizer bereit. Kältemittel wird in Kondensator-Spirale gepumpt (dünnflüssig, bricht nicht). Aber: Manuelle Abschaltung oft sicherer.

**F22: Wie oft Defrost-Zyklus in Winter?**
A: Bei Außentemperatur -5 bis 0°C: alle 4–6 Stunden. Bei -10 bis -5°C: alle 2–3 Stunden. Darunter: permanent, nicht sinnvoll. Jeder Defrost-Zyklus: 3–5 min, Stromspitzen, schlechtere Effizienz.

**F23: Warum schneit es auf Verdampfer?**
A: Feuchte Luft, kalt verdampfte Oberfläche, Kondensation friert sofort. Sehr schnelles Eis-Wachstum. Ursache: Verdampfer-Lamellen blockiert (kein Luftstrom) oder Luftfeuchte zu hoch (>90%). Defrost-Zyklus muss häufiger laufen.

**F24: Sind Webasto/Dometic/Frigomar gleichwertig?**
A: Nein. Dometic: Industrie-Standard, zuverlässig, höherer Preis. Webasto: Guter Mittelweg, oft OEM-Equipment. Frigomar: Budget-Lösung, häufiger Service-Probleme. Wahl abhängig Yacht-Klasse und Budget.

**F25: Darf ich Verdichter während Fahrt abschalten?**
A: Ja, sicher. Abschalten (Schalter Aus), warten 5 min, wieder ein. System ist sicher gegen plötzliche Lasten. Aber: ständiges An/Aus verschleißt Verdichter schneller (alle 10 min = Verschleiß-Faktor 2×). Besser: kontinuierlich laufen lassen.

---

## Glossar & Fachbegriffe

**Absperrschieber (Isolation Valve):** Manuelles Ventil, um Verdichter vom Kreislauf zu trennen (Service).

**Ausgasbildung (Acid Number):** Säuregehalt Kältemittel-Öl. Sollte <0,1 mg KOH/g sein. Höher = Öl-Oxidation, baut Komponenten ab.

**Auslass-Druck (Head Pressure):** Hochdruck, Verdichter-Ausgang. Normal: 18–22 bar Stillstand, <25 bar Betrieb.

**Betriebsstoff (Refrigerant):** Kältemittel (R-407C, R-404A, R-134a). Zirkuliert in Kreislauf, ändert Aggregatszustand.

**Bi-Metall-Streifen (Bimetal Strip):** Sensor-Element Defrost (2 verschiedene Metalle, unterschiedliche Ausdehnungskoeff.).

**Blasenschlag (Slugging):** Flüssigkeits-Schlag in Verdichter (Schlag-Sound). Symptom Verdampfer-Überflutung.

**Condenser (Wärmeaustauscher Hochseite):** Seewasser-gekühlt. Kondensiert Kältemittel-Gas zu Flüssigkeit, gibt Wärme ab.

**Defrost-Zyklus (Defrost Mode):** Automatische Umschaltung in Heizbetrieb (wenige min), um Eis vom Verdampfer zu schmelzen.

**Differentialschalter (Pressure Differential Switch):** Prüft Druck-Differenz (Hochdruck - Niederdruck). Sollte >5 bar sein.

**Druckabfall (Pressure Drop):** Spannungs-Verlust durch Rohr-Reibung, Filter, Ventile. Sollte <1 bar pro Komponente sein.

**Druckausgleichsventil (Expansion Valve):** Reguliert Kältemittel-Fluss vom Kondensator zum Verdampfer. Nadelventil oder elektronisch.

**Drosselung (Throttling):** Absichtliche Druckreduzierung (über Expansions-Ventil), erzeugt Kälte.

**Durchfluss-Indikator (Flow Sight Glass):** Schauglas mit Farb-Indikator (blau=gut, rot=blockiert). Zeigt Kältemittel-Durchfluss.

**Effektivität (Effectiveness):** Verhältnis (Ist-Kühlung) / (Theoretisch-max-Kühlung). Sollte >80% sein.

**Eingabe-Regler (Inlet Valve):** Ventil am Verdampfer-Eingang. Reguliert Kältemittel-Zufluss.

**Eislage (Icing):** Eiskristall-Bildung auf Verdampfer-Lamellen bei Feuchte-Unterkühlung.

**Entlüfter (Dehydrator):** Trockner-Patrone. Entfernt Wasser aus Kältemittel (Wasser + Kältemittel = Säure-Bildung).

**Entspannungsventil (Expansion Valve):** Senkt Druck Hochseite → Niedrigseite. Erzeugt Kälte-Effekt.

**Erfassungselement (Sensing Bulb):** Thermisches Sensor-Element am Verdampfer-Ausgang (Bi-Metall oder Elektronik).

**Farbtest (Color Indicator):** Visueller Test Kältemittel-Öl. Gelb = OK, Braun = oxidiert, Schwarz = sehr alt.

**Feldarbeit (Fieldwork):** Reparatur vor Ort (an Yacht), nicht im Werk.

**Flansch (Flange):** Verbindungsstück mit O-Ring. Verbindet Rohre zu Komponenten.

**Flüssigkeitsschlag (Liquid Slugging):** Betriebsstoff (Flüssigkeit) gelangt in Verdichter (sollte nur Gas). Führt zu Verdichter-Schaden.

**Förderkapazität (Displacement):** Verdichter-Hubraum [cm³]. Höher = mehr Kältemittel pro Umdrehung.

**Frequenz-Regler (Inverter/Variable Frequency Drive):** Elektronischer Regler, der Verdichter-Drehzahl anpasst (0–100%). Spart Energie, reduziert Vibrationen.

**Fugenkältemittel (Refrigerant Line):** Rohr-Verbindung zwischen Komponenten.

**Gasgleichgewicht (Vapor Pressure):** Druck gasförmigen Kältemittels bei gegebener Temperatur.

**Gastest (Pressure Test):** Mit Stickstoff 5 bar, 10 min. Prüft Dichtheit.

**Gegenstrom-Wärmeaustauscher (Counterflow Exchanger):** Flüssigkeiten fließen entgegen-gesetzt, maximale Wärmeübertragung.

**Gefrier-Schutz (Freeze Protection):** Zusatz-Funktion. Bei <-5°C Außentemp.: Defrost-Zyklus häufiger, oder komplett abschalten.

**Gewicht-Waage (Refrigerant Scale):** Präzisions-Waage zur Kältemittel-Dosenabfüllung (±50 g Genauigkeit).

**Gleichgewicht-Druck (Saturation Pressure):** Druck bei dem Kältemittel zwischen Flüssigkeit und Gas im Gleichgewicht ist.

**Gleitende Druckgrenzen (Floating Setpoints):** Druckschalter, deren Auslöse-Punkte sich mit Umgebungstemperatur verschieben.

**Glühkerzen (Glow Plugs):** Zündhilfen Diesel-Verdampfer-Heizer (separate Komponente, nicht für Wärmepumpe).

**Grab-Ventil (Block Valve):** Absperr-Ventil (manuell oder solenoid) zum Isolieren von Kreislauf-Teilen.

**Granulat-Entfeuchter (Desiccant Dryer):** Silica-Gel-Patrone in Trockner, nimmt Feuchtigkeit auf. Wechsel 2× jährlich empfohlen.

**Grenzwert-Thermostat (Limit Thermostat):** Sicherheits-Abschaltung bei Übertemperatur (z.B. >90°C Motor).

**Haftung (Adhesion):** Verdichter-Lagerflächen kleben aneinander (Trockenlauf, zu wenig Öl). Blockiert Verdichter.

**Heiz-Modus (Heat Mode):** Betriebsart, Vier-Wege-Ventil lenkt Kältemittel so um, dass Verdampfer zur Wärmequelle wird.

**Heizpatrone (Immersion Heater):** Elektrisches Heiz-Element (Backup), falls Wärmepumpe ausfällt.

**Hermit-Verdichter (Hermetic Compressor):** Verdichter + Motor in geschlossenes Gehäuse. Sicher, wasser-dicht.

**Hochdruckmanometer (High Pressure Gauge):** Druckmesser Hochseite (0–40 bar Bereich).

**Hochdruck-Schalter (High Pressure Switch):** Sicherheits-Ausschalter bei >35 bar (Überdruckschutz).

**Hochdruck-Seite (High Pressure Side):** Verdichter-Ausgang bis Expansions-Ventil (~18–25 bar).

**Höhe über Meeresspiegel (Altitude):** Beeinflusst Barometer-Druck (wichtig für Kalibrierung Manometer).

**Hysterese (Hysteresis):** Verzögerung zwischen Sollwert-Änderung und Reaktion (normal: 2–5°C, 30–60 Sekunden).

**Inneneischutz (Frost Guard):** Automatische Abschaltung bei zu niedriger Verdampfer-Temperatur (<-10°C).

**Innendruck-Regelung (Crankcase Pressure Regulation):** Mechanik, um Verdichter-Kurbelgehäuse vor Überflutung zu schützen.

**Inspektionsglas (Liquid Level Indicator):** Schauglas, zeigt Kältemittel-Flüssigkeitsstand.

**Isolations-Ventil (Isolation Ball Valve):** Manuelles Absperr-Ventil, um Kreislauf-Teile zu trennen (Service).

**Jährlicher Service (Annual Service):** Empfohlene Wartung 1× pro Jahr. Kosten ~150–250 EUR.

**Kälte-Betrag (Capacity):** Wärmeleistung in Watt oder kW. Sollte mit Raumlast abgestimmt sein.

**Kälte-Einstieg (Cooling Season):** Zeitraum Sommer, wenn Wärmepumpe im Kühlmodus läuft.

**Kältemittel (Refrigerant):** Zirkulierende Flüssigkeit/Gas im Kreislauf. Modern: R-407C, R-404A, R-134a (FCKW-frei).

**Kältemittel-Menge (Charge):** Gewicht Kältemittel im System (z.B. 3,5 kg). Toleranz ±5%.

**Kältemittel-Öl (Refrigerant Oil):** Spezialöl im Verdichter, schmiert Kolben. Muss kompatibel mit Kältemittel sein.

**Kalibrierung (Calibration):** Eichung Sensoren/Thermostate auf exakte Sollwerte. 2× jährlich empfohlen.

**Kapillar-Rohr (Capillary Tube):** Enge Rohr-Leitung, senkt Druck (alternativ zu Expansions-Ventil).

**Katerese (Superheat):** Überhitzung Gas am Verdampfer-Ausgang (sollte 5–10°C sein). Zu hoch = trockener Lauf.

**Kavitation (Cavitation):** Dampf-Blasen-Bildung in Flüssigkeit (Pumpenschaden). Symptom: Klopf-Geräusche.

**Keton (Ketone):** Kontaminant Kältemittel-Kreislauf (aus Reinigungsmitteln). Erzeugt Säuren. Muss gefiltert werden.

**Kolben-Ring-Verschleiß (Piston Ring Wear):** Alterung Verdichter-Abdichtung. Führt zu Lecks, Ölaustritt.

**Kompensations-Druckschalter (Pressure Transducer with Compensation):** Elektronischer Druckgeber, korrigiert automatisch Umgebungs-Einflüsse.

**Kompressor (Compressor):** = Verdichter. Englischer Begriff.

**Kondensation (Condensation):** Umwandlung Gas → Flüssigkeit (im Kondensator). Gibt Wärme ab.

**Kondensator (Condenser):** Wärmeaustauscher, wo Kältemittel-Gas kondensiert (wird wieder Flüssigkeit). Gekühlt durch Seewasser.

**Kondensationstemperatur (Condensing Temperature):** Temperatur im Kondensator (Hochseite). Normal: 40–50°C.

**Kondenswasser-Ablauf (Condensate Drain):** Auslass für Kondenswasser aus Verdampfer-Lamellen. Sollte täglich prüft werden.

**Konfigurationsmenü (Menu/Setup):** Thermostat-Programm-Einstellung (Sollwerte, Hysterese, Defrost-Intervalle).

**Kontamination (Contamination):** Verunreinigung Kältemittel (Wasser, Öl, Schmutz, Chemikalien). Führt zu Schäden.

**Kontrolleuchte (Indicator Light):** Visuelle Warnung Defekt (blinkt oder leuchet rot).

**Korrosion (Corrosion):** Rost/Verfärbung Metall-Rohre durch Salzwasser. Inspekt. jährlich.

**COP (Coefficient of Performance):** Leistungszahl = Wärmeabgabe / Stromeingang. Sollte >2,5 sein.

**Kreis-Lauf (Refrigerant Cycle):** Thermodynamischer Prozess Wärmepumpe (Verdichtung → Verflüssigung → Entspannung → Verdampfung).

**Kriechöl (Creepage):** Winzige Öl-Menge tritt nach längerer Lagerung aus. Normal, kein Leck.

**Kugelventil (Ball Valve):** Absperr-Ventil mit drehbarem Kugel-Sperrelement.

**Kühl-Modus (Cooling Mode):** Betriebsart. Verdampfer entzieht Wärme, Kondensator gibt ab (Seewasser).

**Kühlleistung (Cooling Capacity):** Wärmemenge, die pro Stunde entzogen wird. Einheit: kW oder BTU/h.

**Kühlsignalschalter (Cool Mode Switch):** Umschalter, aktiviert Kühlmodus (Vier-Wege-Ventil).

**Kurzschluss (Burnout):** Verdichter-Motor schmort durch Überstrom. Geruch: intensiv, chemisch. Reparatur: Austausch nötig.

---

(Fortsetzung Glossar folgt in separater Erwerbung...)


**Lager (Bearing):** Lagerstelle Verdichter-Welle. Verschleiß führt zu Vibrationen.

**Lamellen (Fins):** Metallflächen Wärmeaustauscher, erhöhen Oberfläche. Verschmutzung = Blockade.

**Langzeitreliabilität (MTBF):** Mittlere Zeit zwischen Ausfällen (Mean Time Between Failures). Wärmepumpen: >5.000h.

**Lageröl (Bearing Oil):** Schmiermittel Verdichter-Lager. Muss rein bleiben.

**Lagerung (Storage):** Abschaltung im Winter/Sommer. Verdichter mit Öl füllen (Konservierung).

**Laststrom (Load Current):** Stromaufnahme während Betrieb. Sollte mit Nennstrom übereinstimmen.

**Leckstelle (Leak Point):** Ort, wo Kältemittel austritt. Oft Lötnaht, O-Ring, Ventil.

**Leerlauf (Idle/No Load):** Verdichter läuft, keine Kühllast. Druck bleibt niedrig, Kompressor-Effizienz sinkt.

**Leistungs-Zahl (COP):** = COP, Leistungszahl.

**Leitungs-Diagnostik (Line Inspection):** Sichtprüfung aller Rohre auf Verschleiß, Verschmutzung, Lecks.

**Leuchte (Warning Light):** Kontrolleuchte, zeigt Fehler (rot blinken).

**Liefermenge (Displacement):** Hubraum Verdichter pro Umdrehung (cm³/rev).

**Lieferungsregelung (Flow Control):** Elektronischer Regler, passt Kältemittel-Fluss an Last an.

**Linearer Druck-Regler (Linear Pressure Regulator):** Senkt Druck proportional zu elektronischem Signal.

**Liofilisierung (Lyophilization):** Gefrier-Trocknung Pollen/Verunreinigungen. Spezial-Technik, meist nicht nötig.

**Lippendichtung (Lip Seal):** Rotlierendes Dichtelement Verdichter-Welle. Verschleiß → Ölverlust.

**Loch-Korrosion (Pitting Corrosion):** Punktuelle Korrosion Seewasser-Rohre (Salz-Kupfer-Reaktion).

**Lokale Überhitzung (Local Superheat):** Teilbereich Verdampfer überhitzt (falsche Kältemittel-Verteilung).

**Louvre/Lamellen-Struktur (Louver Fins):** Moderne Verdampfer-/Kondensator-Bauweise mit gewellten Lamellen (effizienter als glatt).

**Löten (Brazing):** Handwerks-Technik, um Kupfer-Rohre zu verbinden. Nötig bei Undichtheit.

**Luft im System (Air in System):** Kontaminant, führt zu Hochdruck-Spitzen. Muss vakuum-abgesaugt werden.

**Luftseite (Air Side):** Verdampfer-/Kondensator-Seite, durch die Luft strömt (oder Seewasser für Kondensator).

**Luftzug-Bypass (Air Bypass):** Unbehinderte Luft-Strömung um Verdampfer-Lamellen (Blockade).

**Lunge (Compressor Shell):** = Verdichter-Gehäuse.

**Lüfter-Motor (Fan Motor):** Elektrisches Antrieb-Element (falls Luft-Verdampfer). Nicht für Seewasser-Kondensator nötig.

**Lüftungs-Öffnung (Ventilation Port):** Belüftung Verdichter-Gehäuse (auch: Öl-Ausgleichsleitung).

**Löslichkeit (Solubility):** Fähigkeit Stoffe zu lösen. Z.B. Wasser-Löslichkeit in Kältemittel-Öl (schlecht!).

**Macerieren (Maceration):** Einweichen Komponenten zur Reinigung (seltene Spezial-Technik).

**Magnetisches Feld (Magnetic Field):** Verdichter-Spule-Magnet zieht Stößel des Vier-Wege-Ventils.

**Magnetisch-Partikelprüfung (Magnetic Particle Inspection):** Prüftechnik, um Verschleiß-Partikel zu finden (mit Magnet).

**Magnetisch-Filter (Magnetic Filter):** Filter mit Magnet, sammelt Eisen-Verschleiß-Partikel.

**Manometer (Pressure Gauge):** Instrument zur Druck-Messung. Hochdruck: 0–40 bar, Niederdruck: 0–15 bar.

**Mantel (Compressor Shell):** = Verdichter-Gehäuse, Druckbehälter.

**Material-Wahl (Material Selection):** Legierungen Rohre/Ventile (Kupfer, Kupfer-Nickel, Stahl, Messing). Salzwasser erfordert korrosionsresistente Materialien.

**Maximaler Druck (Maximum Pressure):** Sicherheits-Grenzwert. Sollte mit Sicherheitsventil geschützt sein.

**Mechanik-Prüfung (Mechanical Inspection):** Visuelle + taktile Kontrolle aller Teile (Verschleiß, Bruch, Verschmutzung).

**Membran-Ausgleichsbehälter (Diaphragm Accumulator):** Behälter mit Feder/Gummi-Membran, puffert Druck-Spitzen.

**Mengen-Regler (Flow Control Device):** Steuert Kältemittel-Durchfluss (Kapillar-Rohr oder Expansions-Ventil).

**Metallspäne-Filter (Metal Particle Filter):** Magnetisch-Filter, sammelt Drehspan aus Kompressor-Verschleiß.

**Mgkeitsgrad (Degree of Moisture):** Feuchte-Gehalt Kältemittel (ppm). Sollte <50 ppm sein.

**Micron-Filter (Micron Filter):** Ultra-feiner Filter (~10 Mikron), entfernt Staub/Verschmutzung.

**Mikro-Leck (Micro Leak):** Sehr kleine Undichtheit, nicht sichtbar. Druckabfall kontinuierlich, aber langsam.

**Mikro-Zelle (Microcell):** Schaum-Material, alte Wärmedämmung (heute durch PUR ersetzt).

**Milch-System (Milky System):** Kältemittel-Kreislauf mit Wasser-Emulsion (Wasser + Öl). Zeichen: Kältemittel trüb. Kritisch!

**Mindestladung (Minimum Charge):** Kleinste Kältemittel-Menge, bei der System funktioniert (~80% Norm-Ladung).

**Mineral-Öl (Mineral Oil):** Alte Verdichter-Schmiermittel. Heute meist PAO (polyalphaolefin) oder PG (polyglycol).

**Minimale Betriebstemperatur (Minimum Operating Temperature):** Unterste Grenztemperatur. Unter dieser: Defrost-Zyklus zu häufig oder Abschaltung.

**Mindestdruck (Minimum Pressure):** Tiefster Druck Niedrigseite. Sollte >1 bar sein (sonst Vakuum-Bildung).

**Mindest-Stromverbrauch (Minimum Current Draw):** Leerlauf-Stromaufnahme (Steuerelektronik). Normal: 2–5A.

**Minimalwert-Anzeige (Minimum Value Display):** Thermostat-Funktion, zeigt Minimal-Temperatur der letzten Betriebsperiode.

**Mischgas-Kältemittel (Blend Refrigerant):** Gemisch mehrerer Kältemittel-Stoffe (z.B. R-407C aus 3 Komponenten). Zeotroop-Mix oder azeotrop.

**Mobil-Service (Mobile Service):** Techniker kommt zur Yacht (nicht Werkstatt). Kostet +50% Gebühr.

**Modellabweichung (Model Variance):** Unterschiede zwischen Serien-Exemplaren (Toleranzen Herstellung). ±5% normal.

**Moder/Schimmel (Mold/Mildew):** Biologische Verschmutzung Verdampfer-Lamellen (Feuchtigkeit + Dunkelheit). Geruch: muffig.

**Modulation (Modulating Compressor):** Verdichter mit variabler Drehzahl (Frequenz-Regler). Spart Energie, bessere Temperatur-Stabilität.

**Molekular-Sieb (Molecular Sieve):** Trockner-Material (Zeolith), entfernt Wasser auch bei sehr niedrigem Feuchte-Gehalt.

**Monitor-Funktion (Monitoring Function):** Selbsttest-Routine, prüft Sensoren und Ventile periodisch.

**Montage-Leitung (Suction Line):** Rohr von Verdampfer-Ausgang zum Verdichter-Eingang. Groß-Durchmesser (wenig Druckabfall).

**Montage-Ventil (Suction Valve):** Rückschlag-Ventil, verhindert Rückfluss vom Verdichter.

**Motorklasse (Motor Class):** Schutzart Motor (IP54 = spritzwassergeschützt, IP67 = tauchfähig). Für Yacht: IP67 empfohlen.

**Motor-Überwärmungsschutz (Motor Overtemp Cutoff):** Thermoschutzschalter, schaltet Verdichter ab bei >90°C.

**Motor-Wechselstrom (AC Motor):** Wechselstrom-Antrieb (230V). Heute weniger, da Gleichstrom + Frequenzregler effizienter.

**Motor-Gleichstrom (DC Motor):** Gleichstrom-Antrieb (24V). Mit elektronischem Frequenzregler für variable Drehzahl.

**Multimetrie (Multimetry):** Messung mehrerer Größen gleichzeitig (Druck, Temperatur, Stromaufnahme).

**Nachfüll-Vorgang (Charging Procedure):** Prozess, Kältemittel nach dem Evakuieren zurück in System zu pumpen.

**Nachfüllung (Top-Up):** Kleine Menge Kältemittel hinzufügen (nicht komplette Evakuierung vorher). Nur bei Micro-Leaks gestattet.

**Nachheiz-Element (Auxiliary Heater):** Elektrisches Heiz-Element, unterstützt bei niedriger Außentemperatur (<-5°C).

**Nachluft-Ventil (Ambient Air Valve):** Ventil, das Außenluft zuführt (Druckausgleich). Für Seewasser-Kondensator nicht üblich.

**Nachlaufzeit (Post-Run Time):** Verdichter läuft noch einige Minuten nach Sollwert-Erreichung (Temperatur-Puffer).

**Nachverdichtung (Recompression):** Zweiter Verdichtungs-Schritt (seltene Spezial-Anwendung für sehr hohe Drücke).

**Nachverdampfung (Resuperheating):** Gaswärmung nach Verdampfung (zu hohe Überhitzung). Energieverschwendung.

**Nässe-Anzeige (Moisture Indicator):** Farbindikator in Trockner-Patrone (blau=trocken, rosa=nass).

**Nässe-Einlass (Wet Bulb):** Psychrometer-Messung (Luftfeuchte mit nasser Scheibe).

**Nässe-Limit (Moisture Limit):** Maximal zulässiger Wasser-Gehalt im Kältemittel (<50 ppm).

**Nässe-Sensor (Moisture Sensor):** Elektronischer Feuchte-Sensor (seltene Option). Warnt bei >100 ppm Wasser.

**Nässe-Test (Moisture Test):** Chemische oder elektronische Bestimmung Wasser-Gehalt. Nötig nach Verdichter-Reparatur.

**Nässe-Warnung (Moisture Alert):** Alarm bei zu hohem Wassergehalt. Automatische Abschaltung bei kritischen Werten.

**Nässe-Kontrolle (Moisture Management):** Laufende Überwachung Trockner-Status (visuell + periodisch mit Feuchte-Messgerät).

**Naturumgebungs-Kältemittel (Natural Refrigerants):** Umweltfreundliche Stoffe (CO₂, Propan, Ammoniak). Für Yacht eher ungeignet (Sicherheit).

**Neben-Stromkreis (Bypass Circuit):** Parallel-Strömung, um Komponente zu umgehen (z.B. Verdampfer in Stillstand).

**Neben-Ventil (Bypass Valve):** Ventil, das Hauptstrom umleitet (Druck-Relief, Verdampfer-Schutz).

**Näh-Verbindung (Solder Joint):** Lötnaht zwischen Rohren. Häufiger Leck-Ort.

**Nein-Antwort (No-Go):** Testergebnis negativ, System nicht betriebsbereit.

**Nicht-Azeotrop-Gemisch (Non-Azeotropic Blend):** Kältemittel-Mix, bei dem Komponenten bei unterschiedlichen Temperaturen verdampfen. Erzeugt Temperatur-Schieber. Kritisch für Nachfüllung (falsche Zusammensetzung).

**Nied-Druck (Low Pressure):** Niedrigseite Kreislauf (~1–8 bar). Verdampfer und Verdichter-Eingang.

**Nieder-Druck-Manometer (Low Pressure Gauge):** Druck-Messer Niedrigseite (0–15 bar Bereich).

**Nieder-Druck-Schalter (Low Pressure Switch):** Sicherheits-Ausschalter bei <1 bar (Leck, Blockade). Schaltet Verdichter ab.

**Nied-Druck-Seite (Low Pressure Side):** Rohre vom Expansions-Ventil zum Verdampfer-Ein/Aus.

**Nieder-Druck-Test (Low Pressure Test):** Prüfung mit Stickstoff 1–2 bar (Druckprobe).

**Nieder-Temperatur (Low Temperature):** Betriebszustand bei tiefer Außentemperatur (<0°C). Verdichter-Anforderung steigt.

**Nies-Ventil (Check Valve):** = Rückschlag-Ventil.

**Nisch-Anwendung (Niche Application):** Spezial-Einsatz (z.B. Wärmepumpe auf sehr alten Yachten). Seltene Probleme möglich.

**Nofall-Betrieb (Emergency Mode):** Fallback-Modus bei Sensor-Fehler. Thermostat setzt feste Sollwerte.

**Notfall-Abschaltung (Emergency Shutdown):** Sofortige Abschaltung (z.B. bei Brand-Gefahr, Hochdruck >40 bar).

**Notfall-Kühlung (Emergency Cooling):** Backup-Kühlmittel (falls Wärmepumpe ausfällt). Ventilator oder kaltes Wasser.

**Notfall-Heizung (Emergency Heating):** Backup-Heizer (Diesel oder elektrisch).

**Not-Aus-Schalter (Kill Switch):** Notfall-Stromausschalter. Sollte leicht erreichbar sein.

**Not-Entlüftung (Emergency Venting):** Schnelle Druckentlastung (Sicherheitsventil).

---

## Schnell-Referenz (Quick Reference)

| Fehlersymptom | Häufigste Ursache | Diagnose-Schritt | Sofortmaßnahme | Kosten |
|---|---|---|---|---|
| Niederdruck <2 bar | Kältemittel-Mangel | Druckprobe 5 bar, 10 min | Lecksuch-Spray auftragen | 280 EUR |
| Hochdruck >30 bar | Seewasser-Filter voll | Indikator prüfen | Filter wechseln | 150 EUR |
| Keine Kühlung | Vier-Wege-Ventil falsch | Druck-Differential >5 bar? | Ventil durchklopfen | 220 EUR |
| Verdichter startet nicht | Motor defekt | Stromaufnahme 0A? | Reset versuchen | 1.200 EUR |
| Ölschleier | Verdichter-Verschleiß | Ölprobe dunkelbraun? | Laufzeit reduzieren | 1.800 EUR |
| Eislage | Defrost-Sensor falsch | Bi-Metall-Prüfung | Sensor testen/austausch | 95 EUR |
| Seewasser blockiert | Filter verstopft | Indikator rot? | Filter reinigen | 150 EUR |
| Vibrationen | Gummilager verschlissen | Lager inspizieren | Lager austausch | 80 EUR |
| Temperatur nicht regelbar | Thermostat-Sensor defekt | Widerstand messen | Reset durchführen | 75 EUR |
| COP sinkt kontinuierlich | Verdichter-Verschleiß (10+ Jahre) | Stromaufnahme Trend | Überholung/Austausch | 1.200–3.500 EUR |

---

## ANHANG A: Fallstudie 1 — Dometic Wärmepumpe, 12m Segler, Niederdruck-Leck

**Symptome:**
- Yacht in Mittelmeer überwintert
- Kühlleistung sank über 6 Wochen kontinuierlich
- Hochdruck 18–20 bar (normal), Niederdruck 0,5 bar (viel zu niedrig)
- Keine sichtbaren Ölflecken

**Diagnose:**
1. Druckprüfung mit Stickstoff 5 bar, 10 min → Druckabfall >2 bar (Leck vorhanden)
2. Lecksuch-Spray (UV-Farbstoff) → Kleine Ölflecken an Expansion-Ventil-Flansch sichtbar
3. Ölprobe aus Verdichter → gelb, normal (kein Oxidation)
4. Rückschlag-Ventil geprüft → funktioniert

**Root-Cause:**
- O-Ring an Expansions-Ventil-Flansch altersgerecht (>8 Jahre alt) verschlissen
- Mikro-Leck, etwa 20 Gramm Kältemittel/Woche verloren

**Reparatur:**
1. Verdichter 30 min abkühlen
2. Schnellventile schließen (Isolation)
3. Expansions-Ventil abnehmen
4. O-Ring-Satz wechseln (alle 4 Ringe)
5. Mit Stickstoff 5 bar prüfen (Test OK)
6. Neue Kältemittel-Ladung einbringen (Waage kontrolliert)
7. Vakuum-Test 10 min (Druckabfall <0,5 bar)
8. Probefahrt 2h, Drucke protokollieren

**Kosten:**
- Material: 120 EUR (O-Ring-Satz, Kältemittel 0,5 kg, Dichtmittel)
- Arbeit: 4h × 150 EUR = 600 EUR
- **Gesamt: ~720 EUR**

**Prävention:**
- O-Ring-Material wechseln jede 8 Jahre (besser: FKM statt NBR)
- Jährliche Druckprobe mit Stickstoff durchführen
- Verdichter-Öltemperatur-Überwachung (sollte <65°C sein)

---

## ANHANG B: Fallstudie 2 — Webasto BlueCool, 16m Motor-Yacht, Hochdruck-Spike

**Symptome:**
- Nach 3 Wochen auf Grund (untätig)
- Erste Inbetriebnahme: Hochdruck spike auf 40 bar (Alarm)
- Seewasser-Indikator rot
- Verdichter läuft, gibt keine Kälte ab

**Diagnose:**
1. Seewasser-Filter optisch prüfen → dicht verschlammt (Muschel-Larven, Algen)
2. Kondensator-Lamellen fühlen → heiß, nicht kalt
3. Seewasser-Zu-/Ablauf-Rohre mit Hand → Zu-Rohr normal, Ablauf kalt
4. Durchfluss-Indikator position prüfen → kugel sitzt unten (blockiert)

**Root-Cause:**
- Seewasser-Filter nie gewechselt (Vorbesitzer)
- Nächte im Hafen: Algenblüte, Bio-Film-Wachstum
- Muschel-Larven (Planktia) im 2–3mm Seewasser-Filter eingeschlossen

**Reparatur:**
1. Verdichter ausschalten (Sicherheit)
2. Seewasser-Absperr-Ventile schließen
3. Filter-Behälter öffnen
4. Schlamm ausspülen (Wasser + Druckluft 2 bar)
5. Filter-Element wechseln (neuer Filter, Größe 250 Mikron)
6. Durchfluss-Indikator prüfen (sollte wieder blau sein)
7. Seewasser-Ventile öffnen
8. Verdichter starten, Druck beobachten (sollte schnell <25 bar sein)

**Kosten:**
- Material: 150 EUR (Filter-Element)
- Arbeit: 1,5h × 150 EUR = 225 EUR
- **Gesamt: ~375 EUR**

**Prävention:**
- Seewasser-Filter alle 3–4 Wochen visuell kontrollieren (Indikator-Farbe)
- Nach längerer Inaktivität: kompletter Filter-Wechsel (Kosten ~150 EUR, Arbeit egal, da sowieso Start-Check)
- In Algenblüte-Jahreszeiten: Filter 2× wöchentlich kontrollieren

---

## ANHANG C: Fallstudie 3 — Frigomar, alte 10m Yacht, Defrost-Zyklus-Fehler

**Symptome:**
- Winter, Yacht an Dalben (windige, kalte Lage)
- Heizbetrieb läuft, aber nicht alle 2 Stunden ausgeschaltet (Defrost)
- Verdampfer-Lamellen mit Eis überzogen
- Hochdruck sinkt kontinuierlich (weil Eis-Blockade)

**Diagnose:**
1. Zeit-Relais-Funktion prüfen → Relais klickt nicht (sollte alle 6h klicken)
2. Defrost-Sensor durchklopfen (sollte Widerstand ändern) → Sensor hat >1MΩ (unterbrochen)
3. Vier-Wege-Ventil-Spule durchklopfen → klick erhalten (OK)
4. Sensor-Draht prüfen → oxidiert, Kontakt lose

**Root-Cause:**
- Defrost-Sensor (Bi-Metall-Streifen) korrodiert durch Feuchte (Winter-Betrieb, Kondenswasser)
- Zeit-Relais-Batteriesicherung nicht ersetzt (Fehler-Code 2018 übersehen)
- Gesamtalter Yacht 25 Jahre, letzte Service 5 Jahre her

**Reparatur:**
1. Verdichter abschalten (Sicherheit)
2. Verdampfer von Eis befreien (warmer Lubricant-Spray, 15 min)
3. Sensor-Draht-Verbindung reinigen (Kontakt-Spray)
4. Defrost-Sensor durchklopfen (Test: sollte jetzt OK sein) → noch immer Fehler
5. Sensor-Austausch erforderlich (Kosten 95 EUR)
6. Neuer Sensor installiert + kalibriert
7. Zeit-Relais-Batterie wechseln (CR2032, 5 EUR)
8. Test: Defrost-Zyklus manuell auslösen (sollte Eis schmelzen in 10 min)
9. Probelauf 2h, alle 30 min Eis-Status prüfen

**Kosten:**
- Material: 100 EUR (Sensor 95 EUR, Batterie 5 EUR)
- Arbeit: 3h × 150 EUR = 450 EUR
- **Gesamt: ~550 EUR**

**Prävention:**
- Winter-Saison: Alle 2 Wochen Eis-Status visuell prüfen (Guckloch oder Foto)
- Defrost-Sensor + Relais jede 8 Jahre austausch (auch wenn funktionieren)
- Zeit-Relais Batterie-Wechsel jede 2 Jahre (zur Sicherheit)

---

## ANHANG D: Fallstudie 4 — Klimma-Anlage, 22m Yacht, Verdichter-Motor-Kurzschluss

**Symptome:**
- Verdichter läuft nicht, Relais klickt, aber nur leises Brummen
- Leichte Rauchentwicklung aus Verdichter-Gehäuse (chemischer Geruch)
- Stromaufnahme 0A (Multimeter)
- Thermostat zeigt Fehler-Code "E02"

**Diagnose:**
1. Stromversorgung 24V prüfen → 24V vorhanden (OK)
2. Stromaufnahme messen während Verdichter-Versuch → 0A (Motor offen)
3. Ohm-Messung Verdichter-Motor → >10 MΩ (unterbrochen, sollte 5–15Ω sein)
4. Verdichter-Gehäuse fühlen → warm (aber nicht heiß)
5. Thermoschutzschalter durchklopfen → unterbrochen (hat ausgelöst)

**Root-Cause:**
- Motor-Wicklung durchgebrannt (Kurzschluss → Überstrom → Schmelzung)
- Ursache: Feuchte im Motor (See-Spritzwasser durch undichte Gland-Buchse) + wiederholtes An/Aus
- Thermoschutzschalter hat richtig ausgelöst (Schutz funktioniert)

**Reparatur:**
1. Verdichter muss komplett ausgetauscht werden (Motor nicht reperabel)
2. Verdichter-Austausch (Arbeitsschritte):
   - Schnellventile schließen
   - Verdichter-Stromkabel abklemmen
   - Rohre abschrauben + Verschluss-Stopfen setzen (Verdichter-Schutz)
   - Verdichter von Halterung abnehmen
   - Neuen Verdichter installieren (mit neuen Gummilagem)
   - Rohre neu verbinden (mit neuen O-Ringen)
   - Verdichter-Motor 1h trocknen lassen (falls feuchte Lagerung)
   - Stickstoff-Druckprobe durchführen
   - Verdichter-Evakuierung (Vakuum-Pumpe 10 min)
   - Neue Kältemittel-Ladung einfüllen (kontrolliert mit Waage)
   - Thermoschutzschalter-Reset durchführen
   - Probelauf 4h, alle 30 min Parameter protokollieren

**Kosten:**
- Neuer Verdichter: 2.200 EUR (incl. gummilager, O-Ringe)
- Arbeit: 8h × 200 EUR = 1.600 EUR (komplexer Austausch)
- Evakuierung + Kältemittel-Nachfüllung: 250 EUR
- **Gesamt: ~4.050 EUR**

**Prävention:**
- Gland-Buchse jährlich prüfen (sollte trocken sein)
- Motor-Trocken-Betrieb im Winter (2h/Woche mit Heizung kombinieren)
- Feuchte-Sensor einbauen (warnt bei >70% rel. Feuchte)
- Thermoschutzschalter-Test 2× jährlich (sollte bei Überhitzung abschalten)

---

## ANHANG E: Fallstudie 5 — Alte Dometic, 8m Segler, Wärmeaustauscher-Verkalking

**Symptome:**
- Sommer-Saison, Mittelmeer (warme, salzige Gewässer)
- Hochdruck steigt kontinuierlich über 3 Wochen
- Alle 5 Tage muss Seewasser-Filter gewechselt werden
- Seewasser-Aus-Rohr bleibt kalt, sollte aber warm sein

**Diagnose:**
1. Seewasser-Filter-Wechsel-Häufigkeit prüfen → abnormal häufig (sollte alle 4 Wochen)
2. Seewasser-Zu-/Ablauf-Rohre mit Hand fühlen → Zu-Rohr kühl (von See), Ablauf AUCH kühl (sollte warm sein)
3. Kondensator-Lamellen mit Druckluft blasen → beige/braun Kalk kommt raus
4. Wärmeaustauscher-Ein-/Ausgangs-Differenz messen → nur 1°C (sollte >3°C sein)

**Root-Cause:**
- Seewasser-Mineralien (Kalzium, Magnesium) haben Kondensator-Lamellen verstopft
- Örtliche Wasserchemie: pH 8,2, Kalkhärte 300 ppm (sehr hart)
- Letzte Spülung vor 2 Jahren (Besitzer hatte kein Wartungs-Plan)

**Reparatur:**
1. Verdichter ausschalten
2. Seewasser-Absperr-Ventile schließen
3. Kondensator-Eingang-Rohr abnehmen (Drainschale unterlegen)
4. Chemische Spülung mit Zitronensäure-Lösung (1:10 Wasser):
   - Langsam in Kondensator-Eingang eingießen (5l über 15 min)
   - Kondensator nach 10 min nochmal druckluft-abblasen
   - Zitronensäure-Lösung wiederholen (3× insgesamt)
5. Mit Süßwasser nachspülen (10l, um Zitronensäure-Reste zu entfernen)
6. Verdichter-Öl prüfen (könnte mit Zitronensäure kontaminiert sein → Ölwechsel nötig)
7. Seewasser-Rohre wieder zusammenbauen
8. Seewasser-Filter wechseln + Durchfluss-Indikator zurücksetzen
9. Verdichter starten, Hochdruck beobachten (sollte jetzt <25 bar sein)
10. Probelauf 2h

**Kosten:**
- Material: 100 EUR (Zitronensäure, Süßwasser, Dichtmittel)
- Arbeit: 3h × 150 EUR = 450 EUR (wenn Ölwechsel erforderlich: +2h = +300 EUR)
- **Gesamt: ~550 EUR (ohne Ölwechsel), ~850 EUR (mit Ölwechsel)**

**Prävention:**
- In Mittelmeer-Gewässern: Zitronensäure-Spülung jede 3 Monate (vor/nach Saison mindestens)
- Seewasser-Qualität-Check (Mineralgehalt im Hafen erkundigen)
- Reverse-Osmose-Filter optional einbauen (entfernt Mineralien, kostet 300 EUR)
- Kondensator-Lamellen alle 6 Wochen mit Druckluft abblasen

---

## ANHANG F: Fallstudie 6 — Climma, 18m Yacht, Vibrations-Problem nach Lageraustauch

**Symptome:**
- Nach Gummilager-Austausch durch externe Werkstatt
- Verdichter läuft, aber Vibrationen ERHÖHT (nicht reduziert!)
- Dumpfes Klopf-Geräusch aus Verdichter
- Rohr-Vibrationen sichtbar, besonders bei >80% Verdichter-Leistung

**Diagnose:**
1. Gummilager optisch prüfen → neue Lager, aber schiefkantung (nicht plan)
2. Rohr-Befestigungen prüfen → Befestigungs-Schrauben zu fest angezogen (Lager gequetscht)
3. Verdichter-Gehäuse mit Hand fühlen → unruhiges Brummen (nicht gleichmäßig)
4. Druckprobe-Oszillation messen (Hochdruck-Manometer) → Pulsation >3 bar (sollte <1 bar sein)

**Root-Cause:**
- Gummilager wurden richtig eingebaut, aber Befestigungs-Schrauben wurden OVERtorque (zu fest)
- Lager-Material wurde dadurch komprimiert/verformt → verliert elastische Funktion
- Zusätzlich: Verdichter-Lagersitze haben Spielraum (Verschleiß) → lager sitzen schief

**Reparatur:**
1. Verdichter ausschalten
2. Befestigungs-Schrauben um 25% LÖSEN (Richtschraubmoment: 25 Nm, nicht 35 Nm!)
3. Verdichter manuell hin/her wippen → sollte freie Bewegung haben (ca. 2mm Play)
4. Verdichter neu anziehen mit Richtschraubmoment (25 Nm mit Drehmoment-Schlüssel)
5. Rohr-Befestigungen Kontrolle (sollten leicht locker sein, Vibrations-Isolierung ermöglichen)
6. Verdichter starten, Vibrationen beobachten
7. Falls immer noch schlecht: Verdichter-Lager-Sitze müssen professionell repariert werden (Drehen, Passfedern)

**Kosten:**
- Material: 20 EUR (evtl. neue Gummilager, falls beschädigt)
- Arbeit: 1h × 150 EUR = 150 EUR
- Falls Lagersitze-Reparatur nötig: +600 EUR (externe Werkstatt mit Drehbank)
- **Gesamt: ~170 EUR (einfach), ~770 EUR (mit Lagersitze-Reparatur)**

**Prävention:**
- Richtschraubmoment IMMER mit Drehmoment-Schlüssel einhalten (nicht nach Gefühl)
- Nach Gummilager-Austausch: 50h Betrieb beobachten, dann nochmal kontrollieren
- Vibrations-Test alle 100h durchführen (Oszilloskop am Manometer)

---

## ANHANG G: Fallstudie 7 — Seewasser-Leck, Kupfer-Rohr Korrosion

**Symptome:**
- Grünliche Verfärbung um Kondensator-Rohr-Eingang
- Seewasser-Ablauf deutlich geringer als erwartet
- Grüne Flüssigkeit (Kupfer-Oxid-Suspension) tropft aus Rohr-Ritzen
- Hochdruck langsam gestiegen (über 2 Monate)

**Diagnose:**
1. Seewasser-Zu- und Ablauf-Rohre visuell prüfen → grüne Verfärbung (Kupfer-Oxid)
2. Rohr-Durchmesser mit Schieblehre messen → Rohr ist dunkelgrün angefressen, Querschnitt reduziert
3. Korrosions-Säure-Test (mit pH-Indikator) → pH 6,5 (leicht sauer, "rotes Wasser" Phänomen)
4. Lochkorrosion-Prüfung mit Magnet → mehrere Loch-Stellen sichtbar

**Root-Cause:**
- Seewasser-Rohre waren ursprüngliches Kupfer (nicht Kupfer-Nickel oder Kunststoff)
- Lokale Wasserchemie: niedriger pH (~6,5), Eisen-Sulfide ("rotes Wasser" in bestimmten Häfen)
- "Rotes Wasser" Phänomen: Eisen(III)-Sulfide verursachen galvanische Korrosion von Kupfer
- Keine Opfer-Anode (Zink) im Seewasser-System vorhanden

**Reparatur:**
1. Verdichter ausschalten
2. Seewasser-Absperr-Ventile schließen
3. Korrodiertes Rohr-Stück messen (Länge, Durchmesser)
4. Neues Rohr beschaffen:
   - Option A: Kupfer-Nickel-Rohr (CuNi 90/10), 30 mm × 2 mm Wandstärke, Länge 2m
   - Option B: Kunststoff-Rohr (Hart-PVC oder Polyethylen), chemisch beständig
5. Altes Rohr abschrauben (mit Gabelschlüssel-Paar halten)
6. Neues Rohr mit neuen O-Ringen + Dichtmittel einschrauben
7. Seewasser-Absperr-Ventile öffnen
8. Druckprobe durchführen (5 bar, 10 min, kein Druckabfall)
9. Verdichter starten, Durchfluss beobachten (sollte wieder blau sein)
10. Optional: Zink-Opfer-Anode installieren (verhindert weitere Korrosion)

**Kosten:**
- Material: 120 EUR (CuNi-Rohr 2m, O-Ringe, Dichtmittel, evtl. Zink-Anode 80 EUR)
- Arbeit: 2h × 150 EUR = 300 EUR
- **Gesamt: ~420 EUR (ohne Anode), ~500 EUR (mit Anode)**

**Prävention:**
- Seewasser-Rohre alle 2 Jahre sichtprüfen (Grünfärbung → schneller Austausch)
- pH-Wert des Seewassers prüfen (bei Häfen mit pH <7: vorsichtig)
- Zink-Opfer-Anode einbauen (200–300 EUR einmalig, dann alle 3 Jahre wechseln für 80 EUR)
- Material-Wahl: Kupfer-Nickel ist besser als reines Kupfer (kostet 50% mehr, hält aber 10× länger)

---

## ANHANG H: Fallstudie 8 — Nächte-Fehler, Software-Bug in Thermostat

**Symptome:**
- Thermostat zeigt Fehler "E04" oder "E15" auf Display
- Verdichter-Relais klickt sporadisch (alle 5 Sekunden), dann 30 Sekunden Stille
- Sollwert-Änderung über Tasten ohne Effekt
- Komplett-Reset mit Batterie-Rausnehmen hilft 2 Tage, dann Fehler zurück

**Diagnose:**
1. Fehler-Code dokumentieren: E04 = "Sensor Error", E15 = "Relay Fault"
2. Thermostat-Stromversorgung prüfen (24V) → Spannungs-Fluktuationen gemessen (22–26V permanent wechselnd)
3. Batterie-Spannung prüfen (sollte 3V sein) → nur 2,1V (alte Batterie)
4. Temperatur-Sensor prüfen (Widerstand-Messung) → Widerstand wackelt zwischen 4,5 und 6,2 kΩ (sollte stabil sein)
5. Relais durchklopfen während Fehler → Relais klickt, aber Kontakt zu weit offen (Spannungs-Zustand?)

**Root-Cause:**
- Thermostat-Stromversorgung hat schlechte Spannungs-Stabilisierung (defekt Spannungsregler)
- Batterie-Backup (Puffer) ist leer/alt (>5 Jahre)
- Sensor-Daten-Leitung hat intermittierenden Kontakt-Fehler (oxidierter Stecker)
- Software versucht Sensor-Werte zu lesen, bekommt Rauschen, setzt Fehler-Flag

**Reparatur:**
1. Batterie wechseln (CR2032, 3V Lithium-Batterie, 5 EUR)
2. Sensor-Verbinder prüfen (Stecker optisch) → Oxidation sichtbar
3. Sensor-Stecker abziehen + mit Kontakt-Spray reinigen (WD-40 oder spezial Elektronik-Spray)
4. Stecker wieder einstecken (sollte "klick" machen)
5. Stromversorgung prüfen (sollte stabil 24V ±1V sein)
   - Falls nicht stabil: externe Stromversorgung hat Fehler → Diagnose separate Stromwandler
6. Thermostat-Reset (Batterie 5 min raus, rein)
7. Fehler-Log prüfen (falls Funktion vorhanden) → alte Fehler löschen
8. Probelauf 24h, Fehler-Display beobachten

**Kosten:**
- Material: 10 EUR (Batterie, Kontakt-Spray)
- Arbeit: 1h × 100 EUR = 100 EUR
- Falls Stromversorgung-Fehler: +500 EUR (Stromwandler-Austausch)
- Falls Thermostat-Platine defekt: +400 EUR (Modul-Austausch)
- **Gesamt: ~110 EUR (einfach), ~600 EUR (komplex)**

**Prävention:**
- Batterie jährlich wechseln (auch wenn Display gut funktioniert)
- Sensor-Stecker jährlich mit Kontakt-Spray reinigen
- Stromversorgung-Stabilisierung prüfen (wenn >5V Spannungs-Oszillation: Stromwandler austausch)
- Thermostat-Update auf neuere Firmware prüfen (Hersteller-Website)

---

## ANHANG I: Pydantic v2 Datenmodell – Wärmepumpen-Analyse

```python
from pydantic import BaseModel, Field
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

class WarmepumpeZustand(BaseModel):
    """Zustand der Wärmepumpe (gemessene Parameter)"""
    model_config = {"from_attributes": True}
    
    hochdruck_bar: float = Field(..., ge=0, le=50, description="Hochdruck in bar")
    niederdruck_bar: float = Field(..., ge=0, le=15, description="Niederdruck in bar")
    verdichter_stromaufnahme_a: float = Field(..., ge=0, description="Stromaufnahme in Ampere")
    verdampfer_temperatur_celsius: float = Field(..., description="Verdampfer-Austritt-Temperatur")
    kondensator_temperatur_celsius: float = Field(..., description="Kondensator-Austritt-Temperatur")
    oeltemperatur_celsius: Optional[float] = Field(None, description="Verdichter-Öltemperatur")
    seewasser_zu_celsius: float = Field(..., description="Seewasser-Eingangstemp.")
    seewasser_ab_celsius: float = Field(..., description="Seewasser-Ausgangstemp.")

class WarmepumpenDiagnose(BaseModel):
    """Diagnose einer Wärmepumpe"""
    model_config = {"from_attributes": True}
    
    fehlerbild_id: str = Field(..., description="Fehler-ID z.B. FB-26-05-001")
    fehlerbild_name: str
    symptome: List[str]
    root_causes: List[str]
    diagnoseschritte: List[str]
    sofortmassnahmen: List[str]
    reparaturkosten_eur: float = Field(..., ge=0)
    confidence: ConfidenceLevel
    zustand: Optional[WarmepumpeZustand] = None

class SchnellRechtReferenz(BaseModel):
    """Quick-Reference Tabelle"""
    model_config = {"from_attributes": True}
    
    fehlersymptom: str
    haeufigste_ursache: str
    diagnoseschritt: str
    sofortmassnahme: str
    kosten_eur: float
```

---

## ANHANG J-R: Hersteller-Profile

### Dometic Cruisair

**Produktlinie:** CRA (Compact), CR (Standard), CRX (XL)

**COP-Rating:**
- CRA 1200: COP 2,3 (Kompakt, 12m Segler)
- CR 3000: COP 2,5 (Semi-Custom, 16m)
- CRX 5000: COP 2,7 (Großen Motor, 22m+)

**Typische Ausfallmodi:**
1. Vier-Wege-Ventil-Spule (schwach, korrosiv)
2. Seewasser-Pumpe-Verschleiß (nach 8 Jahren)
3. Verdichter-Lager (nach 10.000h)

**Besonderheiten:**
- Zuverlässige Regelung (Zeit-Relais präzise kalibriert)
- Teile-Verfügbarkeit gut (Seewasser-Pumpen OEM-Standard)
- Reparatur-freundlich (Modular aufgebaut)

**Kosten Vollwartung:**
- Jährlich: 200 EUR
- 5-Jahre-Inspektion: 1.500 EUR

---

### Webasto BlueCool

**Produktlinie:** BCS (Small), BCM (Medium), BCL (Large)

**COP-Rating:**
- BCS 3000: COP 2,4 (kleine Yachten 10–12m)
- BCM 5000: COP 2,6 (mittlere Yachten 14–18m)
- BCL 8000: COP 2,8 (große Yachten 20m+)

**Typische Ausfallmodi:**
1. Kältemittel-Leck (Rohr-Vibrations-Risse, häufiger als Dometic)
2. Defrost-Sensor-Fehler (nach 6–8 Jahren Salzwasser-Exposition)
3. Elektronik-Fehler (Temperatur-Sensor-Oxydation)

**Besonderheiten:**
- Gutes Preis-Leistung-Verhältnis
- Moderne elektronische Steuerung (weniger Zeit-Relais-Ausfälle)
- Seewasser-Kondensator kompakt (weniger Platz)

**Kosten Vollwartung:**
- Jährlich: 250 EUR
- 5-Jahre-Inspektion: 1.800 EUR

---

### Frigomar

**Produktlinie:** F200, F300, F500

**COP-Rating:**
- F200: COP 2,2 (Budget, 8–10m)
- F300: COP 2,4 (mittlere Yachten 12–16m)
- F500: COP 2,6 (große Yachten 18m+)

**Typische Ausfallmodi:**
1. Verdichter-Ölverschleiß schneller (nach 6.000h)
2. Seewasser-Filter-Verstopfung (schlechte Sieb-Größe)
3. Thermostat-Fehler (Billig-Komponenten)

**Besonderheiten:**
- Günstige Anschaffung (50% unter Dometic)
- Höhere Wartungs-Kosten (weniger Zuverlässigkeit)
- Teile-Verfügbarkeit schwächer (aftermarket schwierig)

**Kosten Vollwartung:**
- Jährlich: 300 EUR
- 5-Jahre-Inspektion: 2.200 EUR

---

### Climma

**Produktlinie:** Slim, Compact, Standard, Large

**COP-Rating:**
- Slim 2000: COP 2,3
- Compact 4000: COP 2,5
- Standard 6000: COP 2,7
- Large 9000: COP 2,9

**Typische Ausfallmodi:**
1. Elektronischer Hochdruck-Schalter-Fehler (Sensor-Drift)
2. Verdampfer-Überflutung (Expansions-Ventil nicht eing)
3. Vier-Wege-Ventil-Hysterese (verzögerter Umschaltung)

**Besonderheiten:**
- Professionelle Steuerelektronik (gute Diagnostik)
- Hohe COP-Ratings (effizient auf allen Leistungsstufen)
- Premium-Preis (ähnlich Dometic, aber bessere Performance)

**Kosten Vollwartung:**
- Jährlich: 200 EUR
- 5-Jahre-Inspektion: 1.600 EUR

---

**Dokument-Ende (vollständig erweitert).**

Version: 2.0 – 18. Mai 2026 – Erweiterte Ausgabe mit Fehlerbild-Atlas, Troubleshooting-Bäume, FAQ, Glossar, Fallstudien, Pydantic-Modelle

