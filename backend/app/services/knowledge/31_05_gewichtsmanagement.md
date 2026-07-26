# Kat 31.05 — Gewichtsmanagement

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Gewichtsmanagement  
**Gültig ab:** 2025-01  
**Version:** 1.1  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Fundamentale Gewichts-Konzepte

### 1.1 Warum Gewicht kritisch ist

Bootsbau ist ein Optimierungs-Problem zwischen Widerstand, Stabilität, Geschwindigkeit und Kosten.

**Gewicht beeinflusst:**
- **Verdrängung (Displacement):** Heavier boat = more buoyancy needed = larger/heavier hull
- **Trimmung (Trim):** Schwerpunkt-Position beeinflusst Tiefgang und Pitching
- **Stabilität (Stability):** Niedriger Schwerpunkt = höhere Righting Moment
- **Geschwindigkeit:** Leichteres Schiff = weniger Widerstand = höhere Geschwindigkeit (bei gleicher Kraft)
- **Seakeeping:** Zu wenig Gewicht = schlagend, zu viel = träge

### 1.2 Gewichts-Hierarchie

```
Lightship Weight (Leergewicht)
├── Hull (Rumpf) — 30–40%
├── Deck — 8–12%
├── Cabin Superstructure — 5–10%
├── Engine & Machinery — 8–15%
├── Fuel & Fluids System — 3–5%
├── Water System — 2–4%
├── Electrical System — 2–4%
├── Rigging & Sails — 2–4%
├── Ballast (Keel/Internal) — 0–25%
├── Furniture & Interior — 10–15%
├── Deck Equipment — 5–8%
└── Contingency/Margin — 5–10%

Total Lightship = sum of above (typically 70–90% of displacement)

Fully Loaded Displacement = Lightship + Crew + Provisions + Fuel/Water
```

---

## 2. Methoden zur Gewichts-Schätzung

### 2.1 Frühe Entwurfs-Phase (Conceptual)

**Empirische Regression basierend auf Vergleichsboote:**

```
Lightship_Weight_kg ≈ a × LOA_m^b × BWL_m^c × Draft_m^d

Typische Koeffizienten (Cruising Segler 10–20m):
  Production Boat:     W ≈ 35 × LOA^1.2 × (Freeboard/LOA)^0.8
  Semi-Custom:         W ≈ 40 × LOA^1.2
  Displacement Segler: W ≈ 60 × LOA^1.1

Beispiel: 12m LOA Cruiser
  W_est ≈ 35 × 12^1.2 × 0.085^0.8 ≈ 8500 kg (mit Freeboard-Faktor)
```

**Fehlerbereich:** ±15–20% (akzeptabel für Konzept)

> ⚠️ **ZU PRÜFEN (Audit):** Die Beispiel-Rechnung `35 × 12^1.2 × 0.085^0.8` ergibt rechnerisch ≈ 96 kg, nicht die angegebenen ≈ 8500 kg — Koeffizient „35" bzw. der „Freeboard-Faktor" sind nicht schlüssig dokumentiert (Faktor ~88 Abweichung). Illustrative Regression mit undokumentierter Kalibrierung; korrekte Koeffizienten nicht zweifelsfrei ableitbar — unverifiziert, nicht als reale Schätzformel verwenden.

### 2.2 Mittlere Entwurfs-Phase (Preliminary)

**Itemized Weight Breakdown:**

```
1. Hull Structure
   − CAD-Volume × Material-Dichte × Faktor (abhängig Laminat-Dichte)
   − Beispiel: FRP-Rumpf 25 m³ × 0.06 t/m³ × 1.2 (Kern+Verstärkung) ≈ 1.8 t

2. Deck & Superstructure
   − Ähnliche Methode
   − Deck-Fläche × Dicke × Laminat-Dichte

3. Engine & Propulsion
   − Katalog-Daten vom Hersteller

4. Fuel & Water Systems
   − Tank-Volume × Fluid-Dichte

5. Ballast
   − (Wird später berechnet basierend auf Stability)

6. Interior Furniture
   − Schätzung basierend auf ähnliche Boote oder detailliertes CAD

7. Rigging & Sails
   − Katalog-Daten oder Erfahrungswerte
   − Mast: 5–12 kg/m (abhängig Material und Profil)
   − Boom: 2–5 kg/m
   − Segel: 50–150 g/m² (abhängig Material)

8. Deck Equipment & Hardware
   − Windlass, Pulpits, Stanchions, Cleats, Blocks: typisch 200–500 kg für Cruiser

9. Electrical & Plumbing
   − Batterie, Kabel, Rohre: typisch 100–300 kg
```

**Fehlerbereich:** ±8–12%

### 2.3 Finale Entwurfs-Phase (Detail Design)

**Vollständige Detaillierte Gewichtsaufstellung:**

Jedes Bauteil wird einzeln gewogen oder aus Designdatenblatt entnommen.

```
Item                  Quantity  Weight_kg  Subtotal_kg
Hull Structure        1         1850       1850
Deck                  1         420        420
Cabin Sides/Roof      1         280        280
Cabin Interior        1         550        550
Engine (Diesel 30kW)  1         280        280
Gearbox              1         120        120
Fuel Tank            100L       80         80
Freshwater Tank      100L       100        100
Greywater Tank       50L        50         50
Oil/Coolant System   —          40         40
Electrical System    —          180        180
Mast (Alu 50mm dia)  15m        150        150
Boom (Alu 40mm dia)  5m         40         40
Rigging (Shrouds/St) —          120        120
Sails (Main+Jib)     —          100        100
Deck Equipment       —          350        350
Furniture/Cabins     —          750        750
Plumbing/Machinery   —          280        280
Misc Hardware        —          200        200
Contingency (5%)     —          —          500

TOTAL LIGHTSHIP      ≈           9800 kg

Full Displacement (with crew, provisions, fuel/water) ≈ 12500 kg
```

> ⚠️ **ZU PRÜFEN (Audit):** Summe der Einzelposten dieser Tabelle = 6.440 kg (inkl. 500 kg Contingency) vs. ausgewiesenes TOTAL LIGHTSHIP 9.800 kg — Differenz 3.360 kg. Vermutlich fehlt eine Ballast-Position (Ballast zählt laut Abschn. 1.2 zum Leergewicht) oder die Summe ist falsch. Richtung nicht zweifelsfrei — Wert unverifiziert, nicht als Auslegungsbasis verwenden.

---

## 3. Schwerpunkt (Center of Gravity) Berechnung

### 3.1 3D CG-Position Berechnung

```
CG_x = (Σ(m_i × x_i)) / Σ(m_i)   [Längsposition, mm from Datum]
CG_y = (Σ(m_i × y_i)) / Σ(m_i)   [Transversale Position, mm from Centerline]
CG_z = (Σ(m_i × z_i)) / Σ(m_i)   [Vertikale Position, mm above Baseline]
```

**Beispiel für einfaches Boot (nur Längs-Position relevant):**

```
Komponente       Gewicht (kg)  Position (m ab Bug)  Moment (kg·m)
Hull/Structure   1900          6.0                  11400
Engine           300           5.5                  1650
Fuel Tank        80            6.2                  496
Water Tank       100           2.0                  200
Interior         750           5.8                  4350
Deck Equipment   350           2.5                  875
Misc             420           5.5                  2310

TOTAL            3900 kg       —                    21281 kg·m
CG_x = 21281 / 3900 = 5.46 m ab Bug
```

### 3.2 Einfluß CG auf Stabilität

**Tiefe des Schwerpunkts (VCG, Vertical CG above Baseline):**

```
Niedrigeres VCG → höheres GM (Stabilitäts-Hebelarm)
Formel: GM = BM − VCG + KB

Beispiel:
  BM = 1.5m (Metacentric Radius)
  VCG = 1.2m (Schwerpunkt niedrig)
  KB = 0.6m (Auftriebsmittelpunkt-Höhe)
  
  GM = 1.5 − 1.2 + 0.6 = 0.9m (gute Stabilität)
  
Wenn VCG = 1.4m (Schwerpunkt höher):
  GM = 1.5 − 1.4 + 0.6 = 0.7m (reduziert, aber noch OK)
```

### 3.3 Längs-Schwerpunkt (LCG) und Trim

```
LCB = Longitudinal Center of Buoyancy (abhängig Rumpf-Form)
Trim-Moment = m_ship × g × (LCG − LCB)
```

Bei Gleichgewicht: LCG = LCB
Abweichung erzeugt Trim-Winkel.

```
Trim_deg ≈ (LCG − LCB) / GML × 180/π   (kleine Winkel; GML = longitudinale metazentrische Höhe)
  Herleitung: tan(trim) = Trimm-Hebel / GML = (LCG − LCB) / GML
Ziel-Trim: +0.5° bis +1.0° (Bug etwas tiefer)
```

> Hinweis: Der Trimm-Hebel (LCG − LCB) ist durch **GML** (longitudinale metazentrische Höhe, sehr gross), NICHT durch LWL zu teilen — vollständige hydrostatische Auswertung siehe Abschnitt 13.

---

## 4. Ballast-Berechnung

### 4.1 Ballast-Zweck

Ballast (Kielgewicht oder interner Ballast) dient zwei Funktionen:
1. **Stabilitäts-Rückstellkraft:** Niedriger Schwerpunkt für höheres righting moment
2. **Trim-Korrektur:** Positioniert CG richtig längs und quer

### 4.2 Erforderliche Ballast-Menge

```
Ballast_Ratio = Ballast_Weight / Displacement

Typische Werte:
  Racing Segler:        30–50% (sehr schwer ballastiert, extreme GM)
  Cruising Segler:      30–40% (ausgewogen)
  Motorsailer:          20–30% (weniger kritisch)
  Motorboot:            10–20% (Ballast oft minimal)
```

**Berechnung basierend auf Stabilitäts-Anforderung:**

```
Angenommenes Leergewicht: W_light = 8500 kg
Angenommener Auftrieb-Mittelpunkt: KB = 0.6m
Angenommener Rumpf-Radius: BM = 1.5m
Ziel-Stabilitäts-Hebelarm: GM_target = 1.0m

Rückwärts-Rechnung:
  GM = BM − VCG + KB
  1.0 = 1.5 − VCG + 0.6
  VCG_target = 1.1m (Schwerpunkt 1.1m über Baseline erforderlich)

Mit Ballast:
  VCG = (m_hull × z_hull_cg + m_ballast × z_ballast) / (m_hull + m_ballast)
  
Annahmen:
  − Hull/misc CG: z = 1.5m
  − Ballast Position: z = 0.3m (tief im Kiel)
  − m_hull = 8500 kg
  
  1.1 = (8500 × 1.5 + m_ballast × 0.3) / (8500 + m_ballast)
  1.1 × (8500 + m_ballast) = 12750 + 0.3 × m_ballast
  9350 + 1.1 × m_ballast = 12750 + 0.3 × m_ballast
  0.8 × m_ballast = 3400
  m_ballast = 4250 kg

Displacement_total = 8500 + 4250 = 12750 kg
Ballast_Ratio = 4250 / 12750 = 33% (realistisch für Cruiser)
```

### 4.3 Ballast-Verteilung

**Kiel-Gewicht (Fin Keel):**
```
Typisch: 60–80% des Ballasts im Kiel unten
Vorteil: Maximale Hebelarm für Stabilität
Nachteil: Tief draft, Schwachstelle bei Grundberührung
```

**Interner Ballast:**
```
Typisch: 20–40% in Bilge-Taschen oder Ballast-Tanks
Vorteil: Geschützt, kann Trim anpassen, kein Draft-Problem
Nachteil: Höherer Ballast-Schwerpunkt (weniger Stabilität)
```

---

## 5. Gewichts-Management während Bau

### 5.1 Gewichts-Kontroll-Verfahren

**Vor Laminierung:**
- CAD-Modell-Massen überprüfen
- Material-Dicken und Aufbauten bestätigen

**Während Bau:**
- Rumpf nach Laminierung wiegen (wenn möglich)
- Systeme und Ausrüstung gegen Datenblatt überprüfen
- Laufende Tally halten

**Nach Bau (vor Inbetriebnahme):**
- Vollständige Boot-Wägung durchführen (Wiegebrücke oder Hängung)
- CG messen (tippy-test oder Neigungstest)
- Vergleich gegen Budget und Adjustments durchführen

### 5.2 "Schwere" Komponenten

**Top Gewichts-Verursacher:**

| Komponente | Typisches Gewicht | Kontroll-Potential |
|-----------|-------------------|-------------------|
| Hull (FRP) | 25–35% | Niedrig (Material-intensive) |
| Engine | 8–12% | Niedrig (Katalog-Spezifikation) |
| Ballast | 15–25% | Mittel (optimierbar) |
| Interior | 10–15% | Hoch (viele kleine Teile) |
| Deck Equipment | 5–10% | Mittel (spezifisch auswählbar) |

**Gewichts-Sparmaßnahmen (wenn nötig):**
- Leichte Möbel-Materialien (Kohlefaser, Leichtmetall)
- Optimierte Laminat-Dicken (Sandwich statt vollständiges Laminat)
- Kleinere oder weniger Ausrüstung
- Carbon-Rigg (teuer, aber leicht)
- Wassertank aus Kunststoff statt Metall

---

## 6. Fehleranalyse — 12 Fehlermuster

### 6.1 [F6.1] Gewichts-Schätzung zu niedrig (Design-Weight zu optimistisch)

**Symptom:**
- Design-Budget: 8500 kg
- Reales Gewicht nach Bau: 10200 kg
- Übergewicht: 1700 kg (20%)

**Ursache:**
- Empirische Formel nicht angepasst an spezifisches Design
- Material-Dichte unterschätzt
- Hidden weights nicht berücksichtigt (Verdrahtung, Rohre, Fittings)

**Folgen:**
```
Zu tieferes Tauchgang → Verdrängung größer → Auftrieb ausreichend
Aber: CG höher als erwartet → GM niedriger
       LCG falsch → Trim-Fehler
       Geschwindigkeit reduziert (höherer Widerstand)
       Treibstoff-Verbrauch erhöht
```

**Empforlicht Korrektion:**
```
In early phases: Gewichts-Schätzung mit 10–15% Sicherheits-Zuschlag
  Beispiel: Geschätztes Gewicht 8500 kg → Design-Budget 9700 kg (14% Marge)

In detail design: Detaillierte Itemisierung durchführen
  − Jede Komponente wiegen oder aus Datenblatt
  − Laufende Tally mit Ziel-Gewicht vergleichen
  − Abweichungen früh identifizieren
```

**Prüfkriterium:** Gewicht > Budget + 5% → Überprüfung/Korrektur

---

### 6.2 [F6.2] Schwerpunkt-Position falsch berechnet (CG-Fehler)

**Symptom:**
- Berechnet LCG: 5.5m ab Bug
- Real gemessen (nach Bau): 5.9m ab Bug
- Abweichung: 400 mm

**Ursache:**
- CG-Berechnung vereinfacht (nur Hauptkomponenten)
- Hidden weights nicht berücksichtigt
- Position-Annahmen falsch (z.B. Interior-Schwerpunkt)

**Folgen:**
- Trim verfälscht (Bug tiefer oder Heck tiefer als erwartet)
- Stabilität-Berechnung falsch (abhängig VCG)
- Ladungs-Planung ungültig

**Empforlicht Korrektion:**
```
Detaillierte CG-Berechnung:
  1. Jedes Item mit Gewicht UND Position auflisten
  2. Moment berechnen (Gewicht × Position)
  3. Summen: CG = Σ(Momente) / Σ(Gewichte)

Überprüfung nach Bau:
  − Neigungstest durchführen (Gewicht verschieben, Neigung messen)
  − Daraus wird echter CG berechnet
  − Wenn Abweichung > 200 mm: Ballast-Anpassung erforderlich

Ballast-Trim (falls notwendig):
  − Ballast verschieben oder hinzufügen/entfernen
  − Kleine Bleigüsse in verschiedene Positionen platzieren
  − Ziel: LCG ± 200 mm von Design
```

**Prüfkriterium:** |LCG_Design − LCG_Measured| > 300 mm → Anpassung erforderlich

---

### 6.3 [F6.3] Ballast-Gewicht zu niedrig (Stabilitäts-Defizit)

**Symptom:**
- Ballast geplant: 4500 kg
- Real verwendet: 3800 kg (Gewichts-Einsparung)
- Stabilitäts-Berechnung zeigt: GM nur 0.65m statt ziel 0.95m

**Ursache:**
- Zu aggressives Gewichts-Sparen
- Nachträglich erkannt, daß weniger Ballast erforderlich (falsch)
- Budgetiert-Ballast nicht verfügbar/teuer

**Folgen:**
- GM zu niedrig für CE-Anforderung (ISO 12217)
- Zertifizierung scheitert
- Sicherheit-Risiko (Kapselungs-Anfälligkeit)
- Seakeeping-Verhalten unzureichend

**Empforlicht Korrektion:**
```
Stabilitäts-Analyse durchführen:
  − GM für verschiedene Ballast-Gewichte berechnen
  − Finde Minimum-Ballast für GM_target
  
Wenn aktuelles Ballast zu niedrig:
  − Ballast erhöhen (weitere Bleigüsse)
  − Oder: Anderes Material tiefer positionieren (Maschinenraum)
  − Oder: Design-Änderung (breiterer Rumpf)
  
Budget-Impact: +1–2% Gesamtkosten für Ballast (normalerweise gering)
```

**Prüfkriterium:** GM < 0.7m für Cruiser oder unterhalb ISO-Anforderung → Fehler

---

### 6.4 [F6.4] Zu hoher VCG (Schwerpunkt-Höhe übertrieben)

**Symptom:**
- VCG berechnet: 1.5m
- Zielvorgabe: 1.1m
- Stabilitäts-Hebelarm GM reduziert sich von 1.0m auf 0.6m

**Ursache:**
- Möbel und Ausbauten höher positioniert als erwartet
- Ballast nicht tief genug
- Decks-Equipment zu schwer oben (z.B. Masten)

**Folgen:**
- GM signifikant reduziert
- CE-Zertifizierung kann scheitern
- Schiff instabil und unangenehm zu segeln

**Empforlicht Korrektion:**
```
VCG-Optimierung:
  − Schwere Ausbauten tiefer versetzen (z.B. Motor-Raum statt Kabine)
  − Ballast-Gewicht tiefer oder erhöht
  − Leichtere Materialien oben verwenden

Ziel: VCG ≤ Design-Ziel + 5% (Toleranz)
```

**Prüfkriterium:** VCG > VCG_Design + 10% → Überprüfung/Korrektur

---

### 6.5 [F6.5] Asymmetrisches Gewicht (transversale CG-Versatz)

**Symptom:**
- Transversale CG: 150 mm Steuerbord (sollte 0 sein)
- Boot hat permanente Heeling-Winkel ~1.5° zur falschen Seite
- Visuell: Schiff "sitzt schief"

**Ursache:**
- Asymmetrische Ausbauten
- Motor-Position nicht zentriert
- Ballast nur auf einer Seite

**Folgen:**
- Permanente Neigung (unkontrollierbar)
- Trimmung ungültig
- Seakeeping-Verhalten asymmetrisch
- Visuelle Problem (Kunden mögen das nicht)

**Empforlicht Korrektion:**
```
Asymmetrie-Überprüfung:
  − Alle Items nach Seite auflisten (Stb vs. Bb)
  − Balancieren: Gewichte sollten symmetrisch sein

Falls bereits verbaut:
  − Kleine Gewichte auf Light-Seite hinzufügen
  − Oder: Große Komponenten (z.B. Motor) verschieben (aufwendig)
  
Ziel: |y_CG| < 50 mm (unter 1% Breite)
```

**Prüfkriterium:** |y_CG| > 100 mm oder sichtbare Heeling > 1° → Korrektur

---

### 6.6 [F6.6] Interior-Gewichte nicht berücksichtigt (Hidden-Weights)

**Symptom:**
- Gewichts-Budget nur Struktur + Maschine berücksichtigt
- Vergessen: Möbel, Polsterung, Textilien, Geschirr, Persönliche Gegenstände
- Reales Gewicht +15–20% über erwartet

**Ursache:**
- Early Design-Phase: Detail-Items noch nicht geplant
- Annahme, daß Sie später "passen"
- Keine systematische Tally

**Folgen:**
- CG-Berechnung unsicher
- Stabilitäts-Vorhersage fehlerhaft
- Trim-Fehler

**Empforlicht Korrektion:**
```
Detaillierte Itemisierung durchführen:
  − Interior Items auflisten mit Gewicht-Schätzung
  − Textilien: Leinwand, Kissungen, Matratzen (20–30 kg pro Kabine)
  − Möbel: Tische, Bänke, Kästen (50–150 kg pro Kabine)
  − Küche: Herde, Spüle, Vorräte (100–200 kg)
  − Bad: Toilette, Waschbecken, Dusche (30–80 kg)
  − Misc: Bilder, Dekor, Sicherheitsausrüstung (50–100 kg)

Typisch für 12m Segler: 800–1500 kg "Hidden Weights"
Marge einplanen: +10% auf finales Gewicht
```

**Prüfkriterium:** Detaillierte Items < 60% von erwartung → Überprüfung

---

### 6.7 [F6.7] Ballast-Kiel zu tief/flach positioniert (Sub-optimale Stabilitäts-Hebelarm)

**Symptom:**
- Kiel-Tiefe unter Baseline: 1.2m (normal) vs. Design 1.5m
- VCG dadurch 0.15m höher als berechnet
- GM reduziert von 1.0m auf 0.85m

**Ursache:**
- Konstruktive Zwänge (Mastschuh, Wasserlinie-Anforderungen)
- Nachträgliche Änderung an Kiel-Position

**Folgen:**
- Stabilitäts-Verlust
- GM-Anforderung verfehlt möglich
- Seakeeping schlechter

**Empforlicht Korrektion:**
```
Kiel-Geometrie überprüfen:
  − Ziel: Tiefste Ballast-Punkt möglichst tief
  − Tiefe ≥ 1.3 × größte Ballast-Dicke
  
Alternativ: Ballast-Gewicht erhöhen (kompensiert höhere VCG)
  − Für jede 10 mm höhere VCG: ~30–50 kg Ballast hinzufügen (Boot-abhängig)

Oder: Interner Ballast tiefer legen (Bilge-Taschen)
```

**Prüfkriterium:** Kiel-Tiefe < Design − 50 mm → Überprüfung/Kompensation

---

### 6.8 [F6.8] Gewichts-Zuschläge nicht berücksichtigt (Verschleiß, Alterung)

**Symptom:**
- Design-Boot: 8500 kg
- 10 Jahre später: Boots-Gewicht 9200 kg
- Zusätzlich 700 kg (antifouling paint, Ausrüstung, Repair-Material)

**Ursache:**
- Antifouling paint: 10–20 kg pro Schicht (mehrere Schichten über Jahre)
- Engine-Öl, Hydraulik-Flüssigkeit: 50–100 kg
- Repair-Material, Ersatzteile: 100–200 kg
- Ausbauten-Verbesserungen: 100–300 kg

**Folgen:**
- Boot wird mit der Zeit "schwerer"
- CG verschiebt sich
- Stabilitäts-Verlust (wenn nicht geplant)

**Empforlicht Korrektion:**
```
Design-Phase: Gewichts-Zuschlag (Contingency) 5–10% einplanen
  − Für Production Boats: 5% (standardisiert)
  − Für Custom Boats: 7–10% (mehr Unsicherheit)

Beispiel: Design-Budget 8500 kg + 7% = 9095 kg Ziel
  Leert dann freien "Spielraum" für Additions später

Dokumentation: Dokumetieren, wo die Margin ist, damit sie gezielt genutzt wird
```

**Prüfkriterium:** Contingency < 3% → Zu knapp

---

### 6.9 [F6.9] Maschinen-Raum Gewicht unter-budgetiert (Engine + Systeme)

**Symptom:**
- Engine budget: 300 kg
- Real: Engine 350 + Gearbox 120 + Propeller 50 + Installation-Hardware 80 = 600 kg
- Überschuß: 300 kg

**Ursache:**
- Nur Engine-Gewicht budgetiert, nicht auxiliary systems
- Spätere Specification: schwerere Engine gewählt
- Installation-Gewichte unterschätzt

**Folgen:**
- CG verschiebt sich aft (wenn Maschine weiter hinten)
- Trim-Fehler möglich
- Stabilitäts-Hebelarm ändert sich

**Empforlicht Korrektion:**
```
Engines-System Gewicht-Breakdown:
  Engine Block:           350–400 kg (für 30 kW Diesel)
  Gearbox:                100–150 kg
  Propeller/Shaft:        50–80 kg
  Cooling System (Wasser): 80–150 kg (Wärmetauscher, Rohre, Flüssigkeit)
  Fuel System:            50–100 kg (Tank, Filter, Pumpe, Rohre)
  Exhaust:                50–80 kg (Muffler, Rohre, Anti-Siphon)
  Mounting/Hardware:      50–100 kg
  Misc Seals/Oil:         30–50 kg
  
TOTAL per complex system: 800–1100 kg

Early budget sollte: mindestens 900 kg für Standard-Installation sein
```

**Prüfkriterium:** Engine-System Budget < 700 kg → Zu niedrig (überprüfen)

---

### 6.10 [F6.10] Fuel/Water-System Gewicht variabel (Tank-Betrieb änder CG)

**Symptom:**
- Boot in Leer-Zustand (Tanks leer): LCG = 5.5m
- Boot voll betankt: LCG = 5.8m (Versatz 300 mm)
- Trim-Änderung: Bug tiefer um 1.5°

**Ursache:**
- Tank-Position nicht optimal (zu weit aft)
- Mehrere Tanks an verschiedenen Orten

**Folgen:**
- Trim variiert je nach Tankfüllung
- Stabilitäts-Änderung (wenn VCG deutlich unterschiedlich)
- Kunde muß Tanks strategisch füllen (unbequem)

**Empforlicht Korrektion:**
```
Tank-Platzierung optimieren:
  Ziel: Tank-CG nahe bei Lightship-CG
  
Beispiel: Lightship-CG @ 5.5m
  Fuel 250L @ 5.3m + Water 200L @ 5.7m = kombiniert ~ 5.5m (ideal)

Oder: Tank-Größen ändern (kleinere Tanks, mehrere Positionen)

Oder: Akzept die Trim-Variation und dokumentieren beste Füll-Sequenz
```

**Prüfkriterium:** Tank-CG-Unterschied zum Boot-CG > 1m → Überprüfung/Optimierung

---

### 6.11 [F6.11] Schwerpunkt-Versatz unter Segang-Bedingungen (dynamisch)

**Symptom:**
- Still-Wasser CG @ 5.5m (richtig berechnet)
- Unter Seegang (bei 25 kn Wind, Wellenberge): effektiver CG schwankt (5.3–5.7m)
- Stabilitäts-Verhalten "atmet" mit Wellen

**Ursache:**
- Wasser-Sloshing in halb-vollen Tanks (Free Surface Effect nicht vollständig berücksichtigt)
- Ladungs-Verschiebung bei Heel/Pitch
- Sails + Wind-Druck erzeugt dynamische Effekte

**Folgen:**
- Reale Stabilität schlechter als statische Berechnung
- Seakeeping-Verhalten unprediktabel
- Kapselungs-Neigung erhöht in extremen Bedingungen

**Empforlicht Korrektion:**
```
Free Surface Effect:
  Bereits in Hydrostatik-Berechnung berücksichtigt (Tank-by-Tank)
  
Aber: Wenn möglich, Tanks voller oder leerer halten (nicht halb-voll)

Ladungs-Sicherung:
  − Schwere Items nach unten/Mittschiff
  − Leichte Items oben/Bug/Heck (wo Bewegung akzeptiert wird)
  
Dynamik-Test (optional):
  − Für hochleistungs-Segler oder extreme Spezifikationen
  − CFD oder experimentelle Seakeeping-Tests
```

**Prüfkriterium:** FS-Effekt > 0.15m reduziert GM → Überprüfung

---

### 6.12 [F6.12] Gewichts-Obergrenzen überschritten (zulässiges Maximum-Gewicht)

**Symptom:**
- Zulässiges Maximum Gewicht (per Zertifizierung): 13000 kg
- Design-Gewicht: 13200 kg (über Limit)
- Zertifizierung kann nicht gewährt werden

**Ursache:**
- Zu aggressive Ausstattung/Ausbauten
- Gewichts-Schätzung falsch
- Spätere Specification schwerere Komponenten

**Folgen:**
- Zertifizierung nicht möglich (CE Anforderung-Fehler)
- Boot nicht zulässig für bestimmte Wasserkategorien
- Versicherungs-Probleme möglich

**Empforlicht Korrektion:**
```
Gewichts-Reduktion erforderlich:
  − Durchgehen alle Komponenten, Prioritäten setzen
  − Optional-Ausbauten entfernen oder lighter-Versionen nutzen
  − Carbon-Rigg (teuer, aber spart 50–100 kg)
  − Leichte Möbel-Materialien (20–50 kg Einsparung)
  
Realistisch: Ohne Design-Änderung ist 5–10% Reduction schwierig

Alternative: Design-Spezifikation ändern (z.B. weniger Kabinen, kleinere Engine)
```

**Prüfkriterium:** Gewicht > Maximum-zulässig → Fehler (Sofort-Korrektur erforderlich)

---

## 7. Gewichts-Budget Template

```
Item                              Budget  Actual  Delta  Notes
================================================== =====
STRUCTURE                         3500    3650    +150
  Hull (FRP)                      2800    2900    +100   Sandwich cores heavier
  Deck                            450     520     +70    Extra reinforcement
  Cabin                           250     230     -20
  
PROPULSION                        900     950     +50
  Engine (30kW Diesel)            350     350     —
  Gearbox                         120     120     —
  Cooling System                  150     180     +30
  Fuel System                     150     140     -10
  Exhaust                         80      80      —
  Propeller/Shaft                 50      80      +30    Larger size chosen

SYSTEMS                           600     620     +20
  Electrical (Batteries, Cables)  180     180     —
  Plumbing/Fresh-water            150     160     +10
  Ballast (Lead Keel)             180     180     —
  Misc Hardware                   90      100     +10

RIGGING & SAILS                   350     370     +20
  Mast                            150     160     +10    Thicker wall
  Boom                            40      45      +5
  Shrouds/Stays                   120     125     +5
  Sails                           40      40      —

DECK EQUIPMENT                    400     450     +50
  Windlass                        80      100     +20    Larger unit
  Pulpits/Stanchions              100     120     +20
  Deck Hardware                   150     160     +10
  Misc (Cleats, Blocks, etc)      70      70      —

FURNITURE & INTERIOR              1200    1400    +200
  Galley Furniture                300     380     +80    More cabinets
  Sleeping Berths                 400     450     +50    Cushions heavier
  Navigation Station              200     220     +20
  Interior Trim/Padding           300     350     +50

CONTINGENCY (7%)                  1200    —       —      Used for overruns
  
TOTAL LIGHTSHIP                   8150    8890    +740   10.8% over budget
DESIGN DISPLACEMENT               11000   11800   +800   Recompute ballast

BALLAST (calculated)              2850    2910    +60    Adjusted for weight gain
FULL DISPLACEMENT                 11000   12710   +1710  14% increase
```

> ⚠️ **ZU PRÜFEN (Audit):** Interne Rechen-Widersprüche im Beispiel-Budget: (a) „10.8% over budget" — 740/8150 = 9,1 %; (b) „14% increase" — 1710/11000 = 15,5 %; (c) Spalten-Summe der Ist-Werte (Actual) = 7.440 kg (Contingency „—"), passt nicht zum ausgewiesenen TOTAL LIGHTSHIP Actual 8.890 kg. Illustratives Template — Basis/Richtung nicht zweifelsfrei, Zahlen unverifiziert.

## 8. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class WeightItemCategory(str, Enum):
    STRUCTURE = "structure"
    PROPULSION = "propulsion"
    SYSTEMS = "systems"
    RIGGING = "rigging"
    DECK_EQUIPMENT = "deck_equipment"
    INTERIOR = "interior"
    BALLAST = "ballast"
    CONTINGENCY = "contingency"

class WeightItem(BaseModel):
    """Einzelnes Gewichts-Item"""
    model_config = {"from_attributes": True}
    
    item_id: str = Field(..., description="Unique item identifier")
    description: str = Field(..., description="Item description")
    category: WeightItemCategory = Field(..., description="Item category")
    
    # Position (3D)
    position_x_mm: Optional[float] = Field(None, description="Longitudinal position (mm from datum)")
    position_y_mm: Optional[float] = Field(None, description="Transverse position (mm from centerline)")
    position_z_mm: Optional[float] = Field(None, description="Vertical position (mm above baseline)")
    
    # Gewicht
    weight_kg: float = Field(..., gt=0, description="Item weight (kg)")
    
    # Status
    budgeted: bool = Field(True, description="Is this in the weight budget")
    actual: bool = Field(False, description="Is this actual measured weight")
    notes: Optional[str] = Field(None, description="Additional notes")

class CenterOfGravity(BaseModel):
    """Schwerpunkt-Position"""
    model_config = {"from_attributes": True}
    
    # Position
    lcg_mm: float = Field(..., description="Longitudinal CG (mm from datum)")
    tcg_mm: float = Field(0.0, description="Transverse CG (mm from centerline)")
    vcg_mm: float = Field(..., description="Vertical CG (mm above baseline)")
    
    # Status
    calculated: bool = Field(True, description="Calculated from itemized weights")
    measured: bool = Field(False, description="Measured (e.g., from tipping test)")
    method: str = Field(..., description="Calculation/measurement method")
    
    confidence: float = Field(0.85, ge=0.0, le=1.0, description="Confidence in CG position")

class WeightBudgetReport(BaseModel):
    """Gewichts-Budget und Analyse"""
    model_config = {"from_attributes": True}
    
    vessel_name: str = Field(..., description="Yacht name")
    report_date: datetime = Field(default_factory=datetime.now)
    
    # Items
    weight_items: List[WeightItem] = Field(default_factory=list, description="All weight items")
    
    # Totals
    lightship_budget_kg: Optional[float] = Field(None, description="Budgeted lightship weight (kg)")
    lightship_actual_kg: Optional[float] = Field(None, description="Actual measured lightship (kg)")
    
    ballast_budget_kg: Optional[float] = Field(None, description="Budgeted ballast (kg)")
    ballast_actual_kg: Optional[float] = Field(None, description="Actual ballast (kg)")
    
    displacement_budget_kg: Optional[float] = Field(None, description="Budgeted full displacement (kg)")
    displacement_actual_kg: Optional[float] = Field(None, description="Actual full displacement (kg)")
    
    # CG Analysis
    cg_budget: Optional[CenterOfGravity] = Field(None, description="Budgeted CG")
    cg_actual: Optional[CenterOfGravity] = Field(None, description="Actual measured CG")
    
    # Ballast Ratio
    ballast_ratio: Optional[float] = Field(None, description="Ballast/Displacement ratio")
    
    # Stability Impact
    gm_impact: Optional[str] = Field(None, description="Impact on stability (OK/WARNING/ERROR)")
    
    # Deviations
    variances: List[str] = Field(default_factory=list, description="Items over/under budget")
    recommendations: List[str] = Field(default_factory=list, description="Design recommendations")

def calculate_cg(items: List[WeightItem]) -> CenterOfGravity:
    """Berechne CG aus Item-Liste"""
    total_weight = sum(item.weight_kg for item in items if item.weight_kg > 0)
    
    if total_weight == 0:
        raise ValueError("Total weight is zero")
    
    lcg_moment = sum((item.weight_kg * item.position_x_mm) for item in items if item.position_x_mm is not None)
    tcg_moment = sum((item.weight_kg * item.position_y_mm) for item in items if item.position_y_mm is not None)
    vcg_moment = sum((item.weight_kg * item.position_z_mm) for item in items if item.position_z_mm is not None)
    
    lcg = lcg_moment / total_weight
    tcg = tcg_moment / total_weight if tcg_moment != 0 else 0.0
    vcg = vcg_moment / total_weight
    
    return CenterOfGravity(
        lcg_mm=lcg,
        tcg_mm=tcg,
        vcg_mm=vcg,
        method="itemized_calculation"
    )

def calculate_gm_impact(
    vcg_mm: float, vcg_target_mm: float, bm_mm: float, kb_mm: float
) -> tuple[float, str]:
    """Berechne GM und Status"""
    gm_mm = bm_mm - vcg_mm + kb_mm
    gm_target_mm = bm_mm - vcg_target_mm + kb_mm
    
    delta_gm = gm_mm - gm_target_mm
    
    if delta_gm < -50:
        status = "ERROR"
    elif delta_gm < 0:
        status = "WARNING"
    else:
        status = "OK"
    
    return gm_mm / 1000, status  # Return in meters
```

---

## 9. Normativer Rahmen (web-verifiziert)

> **Confidence-Hinweis:** Die Normbezüge und Definitionen dieses Abschnitts sind an autoritativen Quellen (ISO, IMO, Klassifikations-/Fachliteratur) verifiziert und mit `documented` markiert. Die **exakten Grenzwerte und Koeffizienten der ISO-Kriterien stehen ausschliesslich im kostenpflichtigen Normtext** und wurden hier NICHT rekonstruiert. Wo nur das Prinzip belegbar ist, steht dies explizit.

### 9.1 Stabilität & Verdrängung — die massgebliche Normfamilie

| Norm | Titel / Gegenstand | Bezug zum Gewichtsmanagement | Confidence |
|------|--------------------|------------------------------|------------|
| **ISO 12217-1** (2013/2015/2022; EN ISO 12217-1:2025) | Small craft — Stability and buoyancy assessment and categorization — **Part 1: Non-sailing boats ≥ 6 m** | Verdrängungs-/Beladungszustände, Zuordnung Auslegungskategorie A–D, Wägung/Rechnung | `documented` |
| **ISO 12217-2** (2013/2015/2022; EN ISO 12217-2:2025) | Stability and buoyancy — **Part 2: Sailing boats ≥ 6 m** | STIX, AVS, Krängungs-/Windkriterien für Segler | `documented` |
| **ISO 12217-3** | Stability and buoyancy — **Part 3: Boats < 6 m** | Kleinstboote | `documented` |
| **ISO 12215-8** | Scantlings — **Ruder** | Ruderkräfte/-schaft (Gewicht/Position Ruderanlage) | `documented` (siehe CLAUDE.md) |
| **ISO 12215-9** | Scantlings — **Kiele & Anhänge** | Kielbefestigungslasten, Ballast-Fixierung — direkt gewichts-/schwerpunktrelevant | `documented` (siehe CLAUDE.md) |
| **IMO Intact Stability (IS) Code 2008, Kap. 8** | Krängungsversuch (inclining test) für Schiffe **> 24 m** | Methodik Leichtschiff-Ermittlung + KG | `documented` |

> Quelle ISO 12217-Reihe: [ISO 12217-1:2022](https://www.iso.org/standard/79072.html), [ISO 12217-2:2022](https://www.iso.org/standard/79073.html), [ISO 12217-1:2015](https://www.iso.org/standard/68140.html). IMO IS-Code 2008 Kap. 8: [Inclining test — Wikipedia](https://en.wikipedia.org/wiki/Inclining_test).

**Abgrenzung (wichtig, wiederkehrende Verwechslung):**
- **ISO 12217** = *Stabilität & Auftrieb* (Gewicht, Schwerpunkt, Verdrängung, Kategorie-Zuordnung) — **die Norm dieses Dokuments**.
- **ISO 12215** = *Scantlings/Struktur* (Laminat-/Plattendicken). NICHT für Stabilitäts-/Gewichtsschwerpunkt-Fragen zitieren.
- CE-Richtlinie **2013/53/EU (RCD)** verweist für den Stabilitätsnachweis auf die harmonisierte ISO-12217-Reihe.

### 9.2 Anwendungsschwelle Krängungsversuch

- **> 24 m Rumpflänge / Handelsschiffe:** physischer Krängungsversuch nach **IMO IS-Code 2008, Kap. 8** verpflichtend bei Neubau und stabilitätsrelevanten Umbauten. [Quelle](https://en.wikipedia.org/wiki/Inclining_test) `documented`
- **Kleinfahrzeuge ≤ 24 m (RCD-Bereich 2,5–24 m):** ISO 12217 erlaubt Nachweis **rechnerisch** (wenn alle Daten aus Plänen bestimmbar) **oder** durch **physischen Test**; ist eine Grösse nicht rechnerisch bestimmbar, ist der physische Test erforderlich. [Quelle: Transport Canada — Using ISO 12217-1](https://tc.canada.ca/en/marine-transportation/vessel-design-construction-maintenance/using-iso-small-craft-stability-standard-iso-12217-1) `documented`
- Zuordnung: „the vessel is assigned the lowest design category appearing on any worksheet" — die **niedrigste** auf einem Arbeitsblatt erscheinende Kategorie ist massgeblich. [Quelle ebd.] `documented`

---

## 10. Grundlagen: Verdrängung & normierte Massebilanz

### 10.1 Archimedes — Verdrängung als Massebilanz

Im Schwimm-Gleichgewicht gilt: **verdrängte Wassermasse = Bootsmasse (Verdrängung Δ)**.

```
Δ  = ρ_wasser × V_eingetaucht           [Masse-Verdrängung]
```

- **Salzwasser** ρ ≈ **1025 kg/m³** (Referenzwert; Messungen 1025–1027 kg/m³).
- **Süsswasser** ρ ≈ **1000 kg/m³**.

Konsequenz für die Praxis: Dasselbe Boot **schwimmt im Salzwasser höher** (weniger Volumen nötig, um dieselbe Masse zu tragen) und **taucht im Süsswasser tiefer** ein. Tiefgang-/Freibordangaben immer mit Wasserdichte-Bezug. [Quelle: Archimedes' Principle — Lumen/OpenStax Physics; Virtue Marine „How Water Salinity Affects Ship Buoyancy"](https://courses.lumenlearning.com/suny-physics/chapter/11-7-archimedes-principle/) `documented`

> Merksatz Werft: Ein Nachweis in Salzwasser (ρ 1025) darf nicht 1:1 auf Binnenreviere (ρ ~1000) übertragen werden — der Tiefgang ändert sich, TPC/Trim-Kennwerte verschieben sich.

### 10.2 Normierte Beladungs-Terminologie (ISO 12217-1) — löst „Lightship" sauber auf

Die in Abschnitt 1–2 verwendeten Begriffe „Lightship" / „Full Displacement" entsprechen normativ:

| ISO-Term | Symbol | Bedeutung | Confidence |
|----------|--------|-----------|------------|
| Light craft condition | **mLCC** | Masse des **fertig gebauten, leeren** Boots im definierten Leerzustand (Grundausstattung; Tanks/Personen/Zuladung ausgenommen gemäss Normdefinition) | `documented` |
| Maximum total load | **mMTL** | **Summe** aus Besatzung, persönlicher Ausrüstung, Proviant, Frisch-/Brauchwasser, Kraftstoff, sonstigen Flüssigkeiten, Stores/Ersatzteilen, Ladung, optionaler Ausrüstung, Rettungsinsel/Beiboot **und Marge für spätere Ergänzungen** | `documented` |
| Loaded displacement mass | **mLDC** | **mLDC = mLCC + mMTL** — massgebliche Verdrängung für die Kategorie-Zuordnung | `documented` |

> Quelle: [ISO 12217-1:2022 (iso.org)](https://www.iso.org/standard/79072.html); Definitionen mMTL/mLDC bestätigt über ISO-Katalog-/Norm-Recherche. `documented`

**Normierte Personen-/Effekten-Ansätze (ISO 12217):** `documented`
- **Besatzungsmasse: 75 kg pro Person** (crew limit) für die Kategorie-Bewertung.
- **Persönliche Ausrüstung: nicht weniger als 20 kg pro Person** (Richtwert für bewohnbare Boote).

> Quelle: ISO-12217-Recherche (crew 75 kg/Person; personal effects ≥ 20 kg/Person). `documented`
> ⚠️ Diese Normwerte sind **Bewertungsansätze** der ISO, nicht die reale Zuladung eines konkreten Kunden — für das Weight-Budget beide dokumentieren (Norm-Nachweis vs. realistische Nutzung).

**Mapping auf die Begriffe in Abschnitt 1–8 dieses Dokuments:**
- „Lightship Weight (Leergewicht)" ≈ **mLCC** (Norm-Leerzustand beachten).
- „Fully Loaded Displacement" ≈ **mLDC**.
- „Contingency/Margin" ist in ISO Teil des **mMTL** („margin for future additions").

---

## 11. Krängungsversuch (Inclining Experiment) — verifizierte Methodik

Der Krängungsversuch bestimmt **experimentell** Leichtschiff-Verdrängung und **KG/VCG** — die einzige belastbare Methode, den real gebauten Schwerpunkt (statt des gerechneten) zu ermitteln. Zweck laut IMO IS-Code 2008, Kap. 8: Ermittlung von Leichtschiff-Masse und Schwerpunkt. [Quelle](https://en.wikipedia.org/wiki/Inclining_test) `documented`

### 11.1 Prinzip und verifizierte Formel

Ein bekanntes Gewicht `w` wird quer um die Distanz `d` verschoben; die resultierende kleine Krängung wird über ein Pendel (Lot) gemessen (Auslenkung `deflection` bei Pendellänge `L`). Über ähnliche Dreiecke gilt:

```
tan θ = deflection / L = GG₁ / GM
GG₁   = (w × d) / Δ                       [horizontale CG-Verschiebung]

  ⇒   GM = (w × d × L) / (Δ × deflection)
```

Daraus der Schwerpunkt über der Kiellinie:

```
KG (VCG) = KM − GM
```

- `w` = verschobenes Gewicht, `d` = Verschiebedistanz (quer), `L` = Pendellänge, `deflection` = Lot-Auslenkung, `Δ` = Verdrängung im Testzustand, `KM` = Metazentrische Höhe über Kiel aus den Hydrostatik-Daten.
- Zielkrängung klein: typ. **1–4°** (kleiner-Winkel-Näherung gültig). [Quelle: Wikipedia — Inclining test] `documented`

> Quelle Formel & KG-Ableitung: [Cult of Sea — The Inclining Experiment](https://www.cultofsea.com/ship-stability/the-inclining-experiment/) (`GM = (w·d·AB)/(Δ·BC)`, `KG = KM − GM`). `documented`

### 11.2 Verifizierte Vorbedingungen (sonst systematischer Fehler)

Laut Verfahrensbeschreibung müssen erfüllt sein: `documented`
1. Boot **aufrecht** und **frei schwimmend**.
2. **Festmacher lose** — Boot muss ungehindert krängen können (keine Zwangskraft der Leinen).
3. **Ruhiges Wasser**, **windstille** Bedingungen.
4. **Keine freien Flüssigkeitsoberflächen** in Tanks (Tanks voll **oder** leer pressen — siehe Free-Surface, Abschnitt 12), sonst verfälschtes GM.
5. **Wasserdichte** und alle Tankinhalte/Draughts genau erfasst; Testzustand dokumentiert.

> Quelle: [Cult of Sea — Inclining Experiment preconditions](https://www.cultofsea.com/ship-stability/the-inclining-experiment/) + [IMO IS-Code 2008 Kap. 8 via Wikipedia](https://en.wikipedia.org/wiki/Inclining_test). `documented`

**Werft-Praxis:** Mehrere Gewichts-Verschiebungen (typ. mehrere Schritte pro Seite) für eine Ausgleichsgerade; Torsions-/Ablesefehler durch **2–3 Pendel** (vorn/mittschiffs/achtern) reduzieren. Diese Detail-Anzahl variiert je Regelwerk — **exakte Schrittzahl/Pendellänge nach anzuwendendem Regelwerk (IMO IS-Code / Klasse / ISO)**; nicht aus einer Einzelquelle verallgemeinern. `documented` (Prinzip) / `estimated` (konkrete Anzahl)

### 11.3 Übertrag auf Kleinfahrzeuge

Für ≤ 24 m ist der Nachweis nach ISO 12217 wahlweise rechnerisch oder als physischer Krängungs-/Kipptest möglich (Abschnitt 9.2). Der in Abschnitt 5.1 genannte „Neigungstest/tippy-test" ist die kleinbootseitige Entsprechung; die Auswertung folgt derselben Geometrie (`GM = w·d·L/(Δ·deflection)`, `KG = KM − GM`). `documented`

---

## 12. Free-Surface-Effect (Freie Oberflächen) — verifizierte Methodik

Teilgefüllte Tanks verschieben bei Krängung ihren Flüssigkeitsschwerpunkt zur Tiefseite und erzeugen einen **virtuellen GM-Verlust** (scheinbare Anhebung des Schwerpunkts) — unabhängig von der Flüssigkeitsmenge, nur von der **freien Oberfläche** abhängig.

### 12.1 Verifizierte Formel

```
FSM      = i × ρ_flüssigkeit              [Free Surface Moment, Trägheitsmoment × Dichte]
ΔGM_frei = FSM / Δ  =  (i × ρ_flüssigkeit) / (ρ_wasser × V)
GM_eff   = GM_solid − ΔGM_frei
```

- `i` = **transversales Flächenträgheitsmoment** der freien Oberfläche um deren Längsachse [m⁴]; für einen Rechtecktank `i = l × b³ / 12` (l = Tanklänge, b = Tankbreite an der Oberfläche).
- `ρ_flüssigkeit` = Dichte der Tankflüssigkeit, `ρ_wasser` = Aussenwasserdichte, `V` = Verdrängungsvolumen, `Δ` = Verdrängung.

> Quelle: [ScienceDirect — Free Surface Effect (overview)](https://www.sciencedirect.com/topics/engineering/free-surface-effect) und [Marine Public — Free Surface Effect](https://www.marinepublic.com/blogs/training/883216-free-surface-effect-what-every-seafarer-must-know): „Loss in GM = Free surface moment (t·m) × SG der Flüssigkeit / Verdrängung (t)"; `i` = Trägheitsmoment der Tank-Oberfläche, `FSM = i × ρ`. `documented`

**Konstruktive Konsequenz (Kernaussage `i ∝ b³`):** Der Verlust wächst mit der **dritten Potenz der Tankbreite**. Halbierung der Tankbreite durch eine **Längs-Schwallschottung** senkt `i` und damit ΔGM_frei auf **1/8** je Kammer. Deshalb: breite Wasser-/Kraftstofftanks längs unterteilen (baffles). `documented` (Prinzip aus `i = l·b³/12`)

### 12.2 Bezug zu Fehlerbild [F6.11] und zum Krängungsversuch

- Der in [F6.11] beschriebene „atmende" CG unter Seegang ist teils Free-Surface-Effekt. Gegenmassnahme: Tanks **voll oder leer** fahren (nicht halbvoll), Schwallschotten.
- Beim **Krängungsversuch** (Abschnitt 11.2) müssen freie Oberflächen eliminiert sein, sonst wird GM zu niedrig gemessen.

---

## 13. Trimm & Tiefgang — Hydrostatik-Kennwerte (verifiziert)

### 13.1 Kennwerte aus der Hydrostatik-Tabelle

| Kennwert | Bedeutung | Formel (dokumentiert) | Confidence |
|----------|-----------|------------------------|------------|
| **TPC** | Tonnes Per Centimetre — Masse für 1 cm Tiefgangsänderung | `TPC = A_wasserlinie / 100 × ρ` (A in m², ρ in t/m³) | `documented` |
| **MCTC** | Moment to Change Trim by 1 cm | `MCTC = (Δ × GML) / (100 × LBP)` | `documented` |
| **LCF** | Longitudinal Centre of Flotation — Dreh-/Kipppunkt beim Trimmen | Bezugspunkt für Trimm-Hebel | `documented` |
| **LCB** | Longitudinal Centre of Buoyancy | im Gleichgewicht: LCG = LCB | `documented` |

> Quelle: [Ships2Ports — Trim of Ship](https://ships2ports.com/trim-of-ship-and-methods-to-calculate/), [Cult of Sea — Stability Definitions](https://www.cultofsea.com/ship-stability/stability-definitions/), [MarineGyaan — MCTC](https://marinegyaan.com/what-is-trimming-moment-mctc/). `documented`

### 13.2 Trimm-Änderung durch Gewichtsverschiebung

```
Trimm-Moment  = w × d_längs                 [w verschoben, d_längs Längsdistanz]
Trimm-Änderung = Trimm-Moment / MCTC        [in cm gesamt]
```

- Der **Trimm-Hebel** wird vom **LCF** (nicht von Bug/Heck) aus gemessen; die Aufteilung der Trimmänderung auf vorn/achtern folgt der LCF-Lage. [Quelle: Ships2Ports; Cult of Sea] `documented`
- Diese Beziehung ersetzt/präzisiert die Näherung in Abschnitt 3.3: Der Trimm ergibt sich sauber aus **Trimm-Moment / MCTC**, nicht aus einer freien Kleinwinkel-Formel.

> ✅ **Aufgelöst (Audit):** Der Trimm-Hebel (LCG − LCB) ist durch **GML** (longitudinale metazentrische Höhe) zu teilen, nicht durch LWL: `tan(trim) = (LCG − LCB)/GML`. Die Formel in Abschnitt 3.3 wurde entsprechend von `/LWL` auf `/GML` korrigiert (`documented`). Quelle: MCA Deck Stability Formulae (TRIM = L·(LCG−LCB)/GML; tan θ = trim/L); The Nautical Site — Trim; vgl. MCTC-Weg in Abschnitt 13.2.

---

## 14. Fehlerbild-Atlas (FB-31-05-NNN) — kollisionsfrei ergänzt

> **ID-Konvention:** Der bestehende Bestand nutzt `[F6.1]…[F6.12]` (Abschnitt 6). Die folgenden neuen, web-verifizierten Fehlerbilder verwenden das kollisionsfreie Schema **`FB-31-05-0NN`** und ergänzen — ohne den Bestand zu ersetzen.

### FB-31-05-001 — Krängungsversuch mit freier Oberfläche verfälscht (GM zu niedrig gemessen)
- **Symptom:** Gemessenes GM/KG weicht systematisch von der Rechnung ab; Streuung der Pendel-Ablesungen gross.
- **Ursache:** Tanks teilgefüllt → Free-Surface-Moment `FSM = i·ρ` reduziert das gemessene GM (Abschnitt 12). [Quelle: ScienceDirect Free Surface Effect] `documented`
- **Folge:** Falsches KG/VCG in der gesamten Stabilitätsdokumentation; Kategorie-Zuordnung unsicher.
- **Korrektur:** Vor dem Versuch alle Tanks **voll oder leer** pressen; Restmengen dokumentieren und FSM rechnerisch korrigieren; Festmacher lose, windstill (Abschnitt 11.2).
- **Prüfkriterium:** Freie Oberfläche in irgendeinem Tank vorhanden → Versuch ungültig, wiederholen.

### FB-31-05-002 — mLCC-Definition nicht normkonform (Leerzustand falsch abgegrenzt)
- **Symptom:** „Leergewicht" der Werft enthält/enthält nicht dieselben Posten wie ISO-**mLCC**; Nachweis und Realwägung unvergleichbar.
- **Ursache:** Uneinheitliche Abgrenzung, welche Flüssigkeiten/Ausrüstung im Leerzustand enthalten sind (vgl. Abschnitt 10.2). [Quelle: ISO 12217-1] `documented`
- **Folge:** mLDC = mLCC + mMTL falsch; Kategorie-Zuordnung (A–D) auf falscher Basis.
- **Korrektur:** Leerzustand exakt nach ISO-12217-Definition dokumentieren; jede enthaltene/ausgeschlossene Flüssigkeit auflisten.
- **Prüfkriterium:** mLCC-Postenliste nicht 1:1 gegen Normdefinition abgleichbar → Überprüfung.

### FB-31-05-003 — Zuladung mMTL unter Norm-Ansatz (Kategorie-Nachweis zu optimistisch)
- **Symptom:** Nachweis nutzt weniger als **75 kg/Person** bzw. **< 20 kg/Person** persönliche Ausrüstung.
- **Ursache:** „Realistische" statt normativer Ansätze im Kategorie-Nachweis. [Quelle: ISO 12217 crew 75 kg, effects ≥ 20 kg] `documented`
- **Folge:** mMTL/mLDC unterschätzt → Auslegungskategorie evtl. nicht haltbar; CE-Nachweis angreifbar.
- **Korrektur:** Für den Kategorie-Nachweis Normansätze verwenden; reale Nutzung separat als Betriebsfall führen.
- **Prüfkriterium:** Personen-Ansatz < 75 kg oder Effekten < 20 kg/Person im Nachweis → Fehler.

### FB-31-05-004 — Nachweis-Wasserdichte nicht zum Revier passend (Tiefgang/Trimm falsch)
- **Symptom:** Reale Schwimmlage (Süsswasser-Marina) tiefer als im Salzwasser-Nachweis.
- **Ursache:** Δ = ρ·V — Süsswasser (1000) vs. Salzwasser (1025) nicht berücksichtigt (Abschnitt 10.1). [Quelle: Archimedes/Salinity] `documented`
- **Folge:** Freibord-/Tiefgangsangaben, TPC/MCTC verschoben; Downflooding-Reserve real kleiner.
- **Korrektur:** Wasserdichte des Einsatzreviers dokumentieren; Hydrostatik für ρ 1000 und 1025 ausweisen.
- **Prüfkriterium:** Nachweis nur für eine Dichte, Betrieb im anderen Medium → Zusatzrechnung erforderlich.

### FB-31-05-005 — Breiter Tank ohne Schwallschott (überhöhter Free-Surface-Verlust)
- **Symptom:** Deutlicher GM-Verlust bei teilgefülltem Wasser-/Kraftstofftank; Schlingern verstärkt.
- **Ursache:** `i = l·b³/12` — Verlust ∝ Tankbreite³; breite ungeteilte Tanks (Abschnitt 12.1). [Quelle: FSE `i` ∝ b³] `documented`
- **Folge:** GM_eff unter Norm-/Zielwert in Teilfüllung; instabiles Verhalten in Zwischenständen.
- **Korrektur:** Längs-Schwallschott (baffle) → halbe Breite = 1/8 `i` je Kammer; alternativ schmale/hohe Tanks.
- **Prüfkriterium:** Tankbreite gross gegen Rumpfbreite ohne Unterteilung → FSM rechnerisch prüfen.

### FB-31-05-006 — Krängungsversuch bei Wind/straffen Leinen (Zwangskraft verfälscht Ergebnis)
- **Symptom:** Nicht reproduzierbare Krängungswinkel, Ausgleichsgerade streut.
- **Ursache:** Straffe Festmacher, Windmoment, unruhiges Wasser verletzen die Vorbedingungen (Abschnitt 11.2). [Quelle: Cult of Sea preconditions] `documented`
- **Folge:** GM/KG-Ergebnis unbrauchbar; darauf gestützte Stabilitätskurve falsch.
- **Korrektur:** Leinen lose, windgeschützt/windstill, ruhiges Wasser; ggf. Versuch verschieben.
- **Prüfkriterium:** Wind/Zwangskraft/Wellen während Versuch → Ergebnis verwerfen.

---

## 15. FAQ, Prüffristen, Glossar

### 15.1 FAQ

**F: Ist ein physischer Krängungsversuch für ein 12-m-Boot Pflicht?**
A: Nein — ISO 12217 lässt für ≤ 24 m den **rechnerischen** Nachweis zu, sofern alle Grössen aus den Plänen bestimmbar sind; andernfalls physischer Test. Über 24 m greift der IMO-IS-Code-Krängungsversuch. [Quellen: Transport Canada; Wikipedia inclining test] `documented`

**F: Warum weicht der reale Tiefgang vom Nachweis ab, obwohl das Gewicht stimmt?**
A: Häufig Wasserdichte (Süss- vs. Salzwasser, Abschnitt 10.1) oder teilgefüllte Tanks (Free Surface / Trimm). `documented`

**F: mLCC, mMTL, mLDC — was zählt für die CE-Kategorie?**
A: Die **mLDC = mLCC + mMTL** ist die massgebliche beladene Verdrängung für die Kategorie-Zuordnung. [Quelle: ISO 12217-1] `documented`

**F: Wie stark senkt ein halbvoller Tank die Stabilität?**
A: Um `ΔGM = i·ρ_flüssigkeit /(ρ_wasser·V)`, unabhängig von der Füllmenge — nur die freie Oberfläche zählt; Verlust ∝ Tankbreite³. `documented`

### 15.2 Prüf-/Wartungsfristen (gewichtsrelevant)

> Belastbar sind hier die **Auslöse-Ereignisse**; kalendarische Fristen variieren je Flagge/Klasse und sind dort zu verifizieren.

| Anlass | Massnahme | Norm/Quelle | Confidence |
|--------|-----------|-------------|------------|
| Neubau-Abnahme | Wägung + Schwerpunkt (Krängungs-/Kipptest oder Rechnung) | ISO 12217 / IMO IS-Code Kap. 8 | `documented` |
| **Stabilitätsrelevanter Umbau** (Rig, Ballast, Aufbau, schwere Anlagen) | erneuter Nachweis/Krängungsversuch | IMO IS-Code Kap. 8 | `documented` |
| Laufender Gewichtszuwachs (Antifouling-Schichten, Nachrüstung — vgl. [F6.8]) | Weight-Budget fortschreiben, Reserve gegen mLDC prüfen | interne Praxis | `estimated` |
| Revierwechsel Salz-/Süsswasser | Tiefgang/Trimm für neue ρ neu bewerten | Abschnitt 10.1 | `documented` |

> Konkrete Kalenderfristen (z. B. periodische Re-Inclining-Intervalle) stehen im jeweiligen Flaggenstaat-/Klasseregelwerk und werden hier **nicht** pauschaliert — `estimated — unverifiziert`, im Einzelfall prüfen.

### 15.3 Glossar (verifizierte Begriffe)

| Begriff | Definition | Quelle |
|---------|------------|--------|
| **Δ (Displacement)** | Verdrängung = Bootsmasse = ρ_wasser × V_eingetaucht | Archimedes `documented` |
| **mLCC** | Light craft condition mass (Norm-Leerzustand) | ISO 12217-1 `documented` |
| **mMTL** | Maximum total load (Zuladungssumme inkl. Marge) | ISO 12217-1 `documented` |
| **mLDC** | Loaded displacement mass = mLCC + mMTL | ISO 12217-1 `documented` |
| **KG / VCG** | Schwerpunkt über Kiel = KM − GM | Inclining test `documented` |
| **KM** | Metazentrum über Kiel (aus Hydrostatik) | Stability def. `documented` |
| **GM** | Metazentrische Höhe = KM − KG | Inclining test `documented` |
| **BM** | Metazentrischer Radius (BM = I_wasserlinie / V) | Stability def. `documented` |
| **LCB** | Longitudinaler Auftriebsschwerpunkt | Stability def. `documented` |
| **LCF** | Longitudinaler Flotationsschwerpunkt (Trimm-Drehpunkt) | Stability def. `documented` |
| **TPC** | Tonnes per Centimetre = A_WL/100 × ρ | Ship trim `documented` |
| **MCTC** | Moment to change trim 1 cm = Δ·GML/(100·LBP) | MarineGyaan/Ships2Ports `documented` |
| **FSM / Free Surface** | Free surface moment = i × ρ; senkt GM | ScienceDirect FSE `documented` |
| **STIX** | Stability Index (Segler), typ. 5–50 | ISO 12217-2 `documented` |
| **AVS** | Angle of Vanishing Stability | ISO 12217-2 `documented` |

> STIX/AVS-Quelle: [IRC — ISO 12217 STIX paper](https://ircrating.org/wp-content/uploads/2019/01/stixpaper.pdf), [STIX & AVS FAQ](https://ircrating.org/wp-content/uploads/2019/01/stix-avs-faq.pdf). STIX, AVS und minimale Aufrichtenergie `m·AGZ` sind die drei nach ISO 12217-2 geforderten Segler-Masse. `documented`
> ⚠️ Exakte Grenzwerte (STIX-Mindestwerte je Kategorie, AVS-Minima, Downflooding-Winkel je Kategorie A–D) stehen ausschliesslich im kostenpflichtigen ISO-12217-2-Normtext und wurden hier **nicht** rekonstruiert.

---

## Quellenverzeichnis (Abschnitte 9–15)

- ISO 12217-1:2022 — https://www.iso.org/standard/79072.html
- ISO 12217-2:2022 — https://www.iso.org/standard/79073.html
- ISO 12217-1:2015 — https://www.iso.org/standard/68140.html
- Transport Canada — Using ISO 12217-1 — https://tc.canada.ca/en/marine-transportation/vessel-design-construction-maintenance/using-iso-small-craft-stability-standard-iso-12217-1
- Inclining test (IMO IS-Code 2008 Kap. 8) — https://en.wikipedia.org/wiki/Inclining_test
- Cult of Sea — The Inclining Experiment — https://www.cultofsea.com/ship-stability/the-inclining-experiment/
- Cult of Sea — Stability Definitions — https://www.cultofsea.com/ship-stability/stability-definitions/
- ScienceDirect — Free Surface Effect — https://www.sciencedirect.com/topics/engineering/free-surface-effect
- Marine Public — Free Surface Effect — https://www.marinepublic.com/blogs/training/883216-free-surface-effect-what-every-seafarer-must-know
- Ships2Ports — Trim of Ship — https://ships2ports.com/trim-of-ship-and-methods-to-calculate/
- MarineGyaan — MCTC — https://marinegyaan.com/what-is-trimming-moment-mctc/
- IRC — ISO 12217 STIX paper — https://ircrating.org/wp-content/uploads/2019/01/stixpaper.pdf
- Lumen/OpenStax — Archimedes' Principle — https://courses.lumenlearning.com/suny-physics/chapter/11-7-archimedes-principle/

---

**Datei abgeschlossen.**  
Kat 31.05 Gewichtsmanagement — Version 1.1 — 2026-07 (Werft-Tiefe: normativer Rahmen ISO 12217/-2/-3, ISO 12215-8/-9, IMO IS-Code Kap. 8; Verdrängungs-/Beladungsterminologie mLCC/mMTL/mLDC; Krängungsversuch, Free-Surface-Effect, Trimm-Hydrostatik TPC/MCTC/LCF; Fehlerbild-Atlas FB-31-05-001…006 — alle Fakten web-verifiziert, unverifizierbare Werte explizit als solche markiert)
