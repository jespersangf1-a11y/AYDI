# Kat 31.06 — Propellerauslegung

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Propellerauslegung  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Grundlagen Propeller-Design

### 1.1 Funktionsweise und Klassifikation

Ein Propeller (Schraube) erzeugt Schubkraft durch Rotation von Blättern (Flügel), die Wasser nach hinten beschleunigen.

**Klassisches Momentum-Theorem:**
```
Schub = Massenstrom × Geschwindigkeit_Änderung
F = ṁ × Δv = ρ × A × v × Δv
```

wobei:
- ρ = Wasserdichte (1025 kg/m³ Salzwasser)
- A = Durchströmungs-Fläche des Propellers
- v = Anströmungsgeschwindigkeit
- Δv = Geschwindigkeit-Änderung durch Propeller

### 1.2 Propeller-Typen

**Feststoff-Propeller (Fixed Pitch):**
- Blatt-Winkel (Pitch) fest, nicht veränderlich
- Einfach, robust, wenig Wartung
- Standard für kleinere Motorboote und Segelboote mit Hilfs-Motor

**Verstellbarer Propeller (Controllable Pitch):**
- Blatt-Winkel kann während Fahrt verstellt werden
- Komplex, teuer, hohe Wartung
- Vorteil: optimale Leistung über Fahrtbereich
- Typisch für größere Motorboote und Arbeitsschiffe

**Azimuth-Propeller (Pod/Jet-Drive):**
- Propeller sitzt in separatem Antrieb, 360° drehbar
- Sehr manövrierbar
- Teuer, nicht für Segelboote
- Typisch für größere Motoryachten

**Wasserstahl (Waterjet):**
- Wasser wird angesaugt, durch Motor beschleunigt, nach hinten ausgestoßen
- Exzellent für Schnellboote
- Weniger für Cruiser (höherer Widerstand unter Last)

---

## 2. Propeller-Dimensionierung

### 2.1 Kritische Parameter

**Durchmesser (D):**
```
D = Durchmesser der größten Blattspitze (in mm oder Zoll)
Durchmesser skaliert mit Wellenleistung und Propellerdrehzahl (Gerr, § 11.2),
NICHT mit der Wasserlinienlänge:  D_in ≈ 632,7 · P_shaft_HP^0,2 / RPM_Prop^0,6
Beispiel-Grössenordnung 12 m Yacht: D ≈ 0,4–0,7 m
  (Segelyacht-Hilfspropeller werden in Zoll angegeben, ~15–18″)
Reale Durchmessergrenze: Tip-Clearance / Eintauchtiefe (§ 11.3)
```

> ✅ **Aufgeloest (Audit):** Die `LWL/6 … LWL/5`-Regel (→ 2,0–2,4 m bei 12 m LWL) ist falsch und wird zurückgezogen — der Propellerdurchmesser skaliert mit **Wellenleistung und Drehzahl** (Gerr-Methode, § 11.2), NICHT mit der Wasserlinienlänge. Reale Hilfspropeller einer 12-m-Yacht liegen bei ~0,4–0,7 m (Yacht-Propeller werden in Zoll angegeben, ~15–18″ ≈ 0,38–0,46 m); die tatsächliche Durchmessergrenze bestimmt das Tip-Clearance (§ 11.3). Quelle: D. Gerr, *The Propeller Handbook* (Durchmesser = f(Wellen-PS, Drehzahl)); Cruising World / Boat Design Net (reale Yacht-Propellergrössen in Zoll) — Confidence: documented.

**Steigung (Pitch, P):**
```
P = theoretische Vorwärtsbewegung pro Umdrehung (mm)
Pitch-Verhältnis = P / D (typisch 0.8–1.2)
- Niedriger Pitch (0.7–0.8): höhere Last, niedriger RPM erforderlich
- Standard Pitch (0.9–1.0): ausgewogen
- Hoher Pitch (1.1–1.2): höhere Geschwindigkeit, niedriger Schub
```

**Blatt-Fläche (Blade Area Ratio, BAR):**
```
BAR = Blatt-Projektionsfläche / (π × (D/2)²)
Typische Bereich: 0.4–0.8
- Niedrig (0.4–0.5): feiner Propeller, weniger Drag, aber höhere Kavitation
- Mittel (0.55–0.65): Standard, guter Kompromiß
- Hoch (0.7–0.8): dicker Propeller, höhere Last, weniger Kavitation
```

**Umdrehungsgeschwindigkeit (RPM):**
```
RPM = Engine Output / (Gearbox Ratio × Moment)
Typisch:
  Motorsegler: 800–1200 RPM
  Motorboot: 1200–2000 RPM
  Schnellboot: 2500–5000 RPM
```

### 2.2 Slip und Effizienz

**Slip (Schlupf):**
```
Slip = (Pitch × RPM / 60 − Schiff_Geschwindigkeit) / (Pitch × RPM / 60) × 100%

Theoretische Geschwindigkeit (ohne Slip):
  V_theo = Pitch_m × RPM / 60

Mit Slip ~10–20% (typisch):
  V_real = V_theo × (1 − Slip)
  
Beispiel:
  Pitch 0.5m, RPM 1000, Slip 15%
  V_theo = 0.5 × 1000 / 60 = 8.33 m/s
  V_real = 8.33 × 0.85 = 7.08 m/s (~13.8 Knoten)
```

**Propeller-Effizienz:**
```
η_propeller = (Schubkraft × Schiff_Geschwindigkeit) / (Input_Leistung) × 100%

Typisch:
  Motorsegler: 50–60% (Kompromiss, nicht optimiert)
  Motorboot: 60–75% (gut optimiert)
  Hochleistungs-Propeller: 75–85%
```

---

## 3. Kavitation und Belüftung

### 3.1 Kavitation-Phänomen

Kavitation tritt auf, wenn lokale Druck am Propeller-Blatt unter Dampfdruck von Wasser fällt. Blasen entstehen und implodieren, was Lärm, Vibration und Beschädigungen verursacht.

**Kavitations-Nummer:**
```
σ = (P_atm + P_hydro − P_vapor) / (0.5 × ρ × v²)

σ_crit ≈ 0.3–0.8 (abhängig Propeller-Design)

Risiko von Kavitation:
  − Hohe Geschwindigkeit (v)
  − Niedriger Druck (P_hydro, geringe Eintauchtiefe / nahe Wasseroberfläche)
  − Hohe Last (großer Schub)
  − Dünne Blätter (low BAR)
```

**Kavitations-Vermeidung:**
```
Maßnahmen:
  1. Propeller-Durchmesser erhöhen (größere Fläche, niedrigere Blatt-Last)
  2. BAR erhöhen (dickere Blätter)
  3. Pitch senken (niedrigere Geschwindigkeit, höherer Schub)
  4. RPM reduzieren
  5. Propeller tiefer eintauchen (höherer hydrostatischer Druck)
  6. Spezial-Propeller wählen (Cavitation-suppressing designs)
```

### 3.2 Belüftung (Ventilation)

Luft von der Oberfläche wird in Propeller gesaugt, reduziert Schubkraft. Tritt auf bei:
- Zu flacher Propeller-Position (nah Wasseroberfläche)
- Scharfe Manöver (Heel verursacht Blatt-Exposition)
- Hohe Last (Propeller "saugt" Luft)

**Vermeidung:**
- Propeller tiefer positionieren (typisch min. 0.3m unter Wasserlinie)
- Anti-Belüftungs-Blech (Hydrofoil) montieren

---

## 4. Schubberechnungs-Methoden

### 4.1 Empirische Formel (Vereinfacht)

```
Schub_kN ≈ 0.5 × ρ × A_disk × (v_rel)²

wobei:
  ρ = 1025 kg/m³ (Salzwasser)
  A_disk = π × (D/2)² (Scheibenfläche)
  v_rel = relative Geschwindigkeit (Wasser-Vorbeistrom)
```

**Beispiel:**
```
D = 0.5m (500mm Durchmesser)
Geschwindigkeit = 6 Knoten = 3.09 m/s

A_disk = π × (0.25)² = 0.196 m²
Schub ≈ 0.5 × 1025 × 0.196 × (3.09)² ≈ 970 N ≈ 1.0 kN

Realistische Effizienz ~55%:
  Schub_real = 1.0 × 0.55 ≈ 0.55 kN (realistisch)
```

### 4.2 Propeller-Entwurfs-Diagramme (Wageningen B-Series)

Standard-Entwurfs-Diagramme von Wageningen (Niederlande) zeigen Effizienz und Schubkoeffizient für verschiedene BAR und P/D Verhältnisse.

**Verwendung:**
1. Gewünschte Geschwindigkeit und Last eingeben
2. Auf Diagramm: Optimale P/D und BAR ablesen
3. Entsprechenden Propeller auswählen oder designer

---

## 5. Fehleranalyse — 12 Fehlermuster

### 5.1 [F6.1] Zu kleiner Propeller-Durchmesser (unterausgelegt)

**Symptom:**
- Motor läuft bei maximaler Last auf sehr hohem RPM (z.B. 2500 RPM)
- Schiff erreicht nicht erwartete Geschwindigkeit
- Motor klingt "überlastet" oder "heulend"

**Ursache:**
- Propeller-Durchmesser zu klein gewählt (Kostenersparnis, oder Entwurfs-Fehler)
- Schiff schwerer als erwartet (höhere Last)
- Widerstand höher als berechnet

**Folgen:**
```
Kleine Propeller erfordert höhere RPM für gleichen Schub:
  Schub = f(D², RPM) → kleiner D → höheres RPM nötig
  
Probleme:
  − Motor läuft bei suboptimaler Effizienz (Spritverbrauch hoch)
  − Vibration und Noise erhöht
  − Motor-Alterung schneller
  − Kavitations-Risiko erhöht
```

**Empforlicht Korrektion:**
```
Berechne erforderlichen Durchmesser:
  Schub_required = Widerstand @ Ziel-Geschwindigkeit (aus Hydrodynamik)
  
  D_min = sqrt(Schub_required / (0.5 × ρ × BAR × (v_rel)²))
  
  Praktisch: Erhöhe D um 5–10% über Minimum für Sicherheit

Wenn Schiff schwerer: Größeren Propeller wählen oder
  − Gearbox Ratio erhöhen (Getriebe-Einsatz)
  − RPM-Limit akzeptieren (langsamer fahren)
  − Propeller-Pitch senken (niedrigere Geschwindigkeit)
```

**Prüfkriterium:** RPM @ Maximum-Last > 80% der Engine-Max-RPM → Überprüfung

---

### 5.2 [F6.2] Zu großer Propeller-Durchmesser (überdimensioniert)

**Symptom:**
- Engine kann Propeller nicht durchdrehen ("lugging")
- Motor stottert, vibriert, oder geht aus bei Schub
- RPM bleibt unter Ziel (z.B. 700 RPM statt 1000)
- Geschwindigkeit sehr niedrig

**Ursache:**
- Propeller zu groß dimensioniert (Fehler in Entwurf)
- Schiff leichter als angenommen (geringerer Widerstand)
- Zu niedriges Getriebe-Verhältnis

**Folgen:**
- Motor läuft "zu schwer", kann nicht Volllast erreichen
- Schub unzureichend für normale Fahrt
- Motor-Schaden möglich (Überbelastung)

**Empforlicht Korrektion:**
```
Reduzieren Sie Propeller-Größe oder erhöhen Sie Pitch:
  − Kleinerer Durchmesser: D_neu = D_alt × (RPM_desired / RPM_actual)^0.5
  − Oder: Höherer Pitch: P_neu = P_alt × (RPM_desired / RPM_actual)
  
Test bei höherem Pitch:
  − Geschwindigkeit steigt, Schub sinkt
  − Ziel: RPM @ Volllast > 85% der Engine-Rating
```

**Prüfkriterium:** RPM @ Volllast < 60% der Engine-Rating → Fehler

---

### 5.3 [F6.3] Falsches Pitch-Verhältnis (P/D fehlerhaft)

**Symptom:**
- Entweder: Propeller "zu schnell" (hoher Pitch) → keine Kraft
- Oder: Propeller "zu langsam" (niedriger Pitch) → RPM zu niedrig
- Verhalten nicht ausgewogen über Fahrtbereich

**Ursache:**
- Propeller-Spezifikation falsch interpretiert
- Pitch von anderem Propeller übernommen
- Entwurfs-Fehler in BAR/P-D Auswahl

**Folgen:**
- Nicht-optimale Leistung (Spritverbrauch, Geschwindigkeit)
- Motor-Abstimmung schlecht

**Empforlicht Korrektion:**
```
Pitch überprüfen:
  Ideal P/D = 0.9–1.0 für Motorsegler
            = 1.0–1.2 für Motorboot

Wenn Pitch zu hoch (>1.3):
  − Propeller-Pitch reduzieren oder neuer Propeller mit P/D ~1.0
  − Oder: Größerer Durchmesser mit reduziertem P/D

Wenn Pitch zu niedrig (<0.7):
  − Pitch erhöhen oder neuer Propeller
```

**Prüfkriterium:** P/D < 0.7 oder > 1.3 → Überprüfung

---

### 5.4 [F6.4] Zu niedrige Blatt-Fläche (BAR < 0.45)

**Symptom:**
- Propeller schwingt oder vibriert stark
- Kavitations-Blasen sichtbar (weißliche Schliere)
- Lärm-Bildung beim Fahren
- Schub variiert bei Seegang-Bedingungen

**Ursache:**
- Propeller mit zu niedriger BAR gewählt (feiner Propeller für geringe Kraft)
- Falsch angenommen, daß niedrige BAR = weniger Drag (nicht true)

**Folgen:**
```
BAR < 0.45 ist kritisch für:
  − Kavitations-Neigung erhöht (Blattbelastung hoch)
  − Vibration und Noise
  − Schub-Variabilität unter Last
  − Langfristig: Propeller-Erosion durch Kavitations-Blasen
```

**Empforlicht Korrektion:**
```
Erhöhe BAR:
  − Typisch Ziel: BAR 0.55–0.65 für Motorsegler
  − Oder BAR 0.60–0.75 für Motorboot
  
Durch BAR erhöhen:
  − Dickere Blätter, weniger Kavitation
  − Höherer Schub bei gleicher RPM
  − Ruhigere Fahrt
```

**Prüfkriterium:** BAR < 0.50 → Überprüfung/Auswahl höherer BAR

---

### 5.5 [F6.5] Zu hohe Blatt-Fläche (BAR > 0.75)

**Symptom:**
- Propeller kann nicht zu erwarteter RPM hochfahren
- Engine "zieht schwer"
- Sehr hohe Kraft, aber niedrige Geschwindigkeit
- Motor-Belastung groß

**Ursache:**
- Propeller mit sehr hoher BAR gewählt (dicker Propeller für hohe Last)
- Aber Gewicht/Last unterschätzt

**Folgen:**
- Motor läuft suboptimal (nicht Volllast erreichbar)
- Schiff wird zum Schlepper reduziert (sehr niedrige Geschwindigkeit)

**Empforlicht Korrektion:**
```
Reduziere BAR oder erhöhe Pitch:
  − Typisch Ziel: BAR 0.55–0.65
  − Durch Pitch-Erhöhung ausgleichen (wenn nötig)
  
Wenn BAR > 0.75 und RPM problematisch:
  − Neuen Propeller mit BAR ~0.60 und P/D ~1.0 auswählen
```

**Prüfkriterium:** BAR > 0.80 und RPM @ Volllast < 75% → Überprüfung

---

### 5.6 [F6.6] Kavitations-Erosion (Blatt-Beschädigung durch Kavitation)

**Symptom:**
- Propeller-Blätter sichtbar erodiert/ausgehöhlt
- Oberflächenrauheit erhöht
- Schub vermindert (Propeller-Effizienz sinkt)
- Vibration und Lärm

**Ursache:**
- Propeller regelmäßig bei Bedingungen betrieben, die Kavitation fördern
- BAR zu niedrig oder RPM zu hoch
- Propeller zu nah an Oberfläche

**Folgen:**
- Propeller-Funktionsfähigkeit beeinträchtigt
- Erosion schreitet fort (Kavitations-Blasen immer größer)
- Langfristig: Propeller-Bruch möglich

**Empforlicht Korrektion:**
```
Prävention (Design):
  1. BAR erhöhen (0.60–0.70 statt < 0.50)
  2. Propeller tiefer montieren (min. 0.3m unter Wasserlinie)
  3. RPM-Limit beachten (nicht dauerhaft Überlast)
  4. Cavitation-Suppressing Propeller-Design auswählen

Wenn bereits erodiert:
  − Propeller neu beschichtet/repariert (teuer, wenig zweckmäßig)
  − Besser: Neuer Propeller mit besserer Kavitations-Resistenz
```

**Prüfkriterium:** Sichtbare Kavitations-Erosion → Propeller-Austausch empfohlen

---

### 5.7 [F6.7] Propeller zu nah an Oberfläche (Belüftungs-Risiko)

**Symptom:**
- Besonders bei Heel/Manöver: Propeller verliert Schub plötzlich
- Lärm und Vibration wenn Luft eindringt
- Boot "springt" oder "schlupft" unter Kurven

**Ursache:**
- Propeller zu hoch montiert (nicht tief genug unter Wasserlinie)
- Entwurfs-Fehler oder Nachmontage-Problem
- Seeling oder Trimm-Fehler

**Folgen:**
- Belüftung: Luft wird angesaugt statt Wasser
- Schubkraft-Verlust
- Motor-Racing (RPM steigt unkontrolliert)

**Empforlicht Korrektion:**
```
Tiefe-Positionierung überprüfen:
  Ziel: Min. 0.3m unter mittlerer Wasserlinie (bei Fahrt)
  
Propeller-Position optimieren:
  − Schaftlinie evtl. senken (konstruktiver Aufwand, aber best)
  − Oder: Propeller mit größerem Durchmesser (zentriert tiefer)
  
Trim-Management:
  − Trim überprüfen (sollte neutral oder Bug leicht tiefer sein)
  − Ladung überprüfen (nicht zu viel Gewicht achtern)
```

**Prüfkriterium:** Propeller-Mittelpunkt < 250mm unter WL → Überprüfung

---

### 5.8 [F6.8] Propeller-Unausgewogenheit (Vibration)

**Symptom:**
- Vibration bei bestimmter RPM (Resonanz-Frequenz)
- Propeller wirkt "unwuchtig"
- Getriebe/Motor vibriert spürbar
- Struktur rund Antrieb-Einheit schwingt

**Ursache:**
- Propeller nicht zentrisch (Masse-Verteilung asymmetrisch)
- Blatt-Beschädigung oder ungleiche Erosion
- Falsche Montage/Balance

**Folgen:**
- Vibration-Ermüdung in Antrieb-Struktur
- Motor-Schäden auf Langzeit
- Unbehagen für Crew

**Empforlicht Korrektion:**
```
Balancierung durchführen:
  − Propeller wiegen und überprüfen (sollte innerhalb +/- 2% der idealen Masse sein)
  − Dynamisches Balancieren (mit Gerät) durchführen
  − Falls Blätter ungleich erodiert: neuer Propeller

Oder: RPM-Bereich meiden, wo Resonanz auftritt
  − Nicht kontinuierlich bei dieser RPM fahren
```

**Prüfkriterium:** Vibration-Amplitude > 2 mm @ Propeller-Schaft → Überprüfung/Balance

---

### 5.9 [F6.9] Propeller-Blatt-Bruch (strukturelles Versagen)

**Symptom:**
- Plötzlicher Schub-Verlust
- Ungewöhnlicher Lärm/Krach
- Propeller-Blatt teilweise oder vollständig abgerissen
- Vibration exzessiv

**Ursache:**
- Kavitations-Erosion über längere Zeit (Schwachstelle entstanden)
- Materialmüdigkeit (alte/abgenutzte Propeller)
- Schlag gegen Hindernis oder Fremdkörper
- Überlast-Kondition

**Folgen:**
- Schub-Verlust (Boot fahrunfähig oder sehr schwierig zu manövrieren)
- Motor kann Overrun gehen (RPM unkontrolliert steigen)
- Sicherheit-Risiko (vor allem in Notwendigkeiten)

**Empforlicht Korrektion:**
```
Sofort-Maßnahmen:
  − Propeller untersuchen und ersetzen
  − Kein Weiterbetrieb mit gebrochenem Blatt (starke Vibration → Strukturschaden)

Langfristig:
  − Regelmäßige Inspektionen durchführen (jährlich)
  − Kavitations-Bedingungen minimieren
  − Propeller-Material wählen (Bronze-Propeller robuster als Aluminium)
```

**Prüfkriterium:** Sichtbarer Blatt-Bruch → Sofort Propeller-Tausch erforderlich

---

### 5.10 [F6.10] Falsches Pitch für Lastfall (Trimm-Fehler)

**Symptom:**
- Propeller-Pitch für Fahrtbetrieb optimiert, aber Manövrieren schwach
- Oder: Manövrieren OK, aber Geschwindigkeit niedrig
- Kompromiss nicht geglückt

**Ursache:**
- Pitch-Auswahl nicht für charakteristische Lastfälle optimiert
- Entwurf folgte nur "cruising" spec, ignorierte andere Szenarien

**Folgen:**
- Nicht-optimale Leistung in realen Einsatz-Spektrum
- Spritverbrauch höher

**Empforlicht Korrektion:**
```
Mehrpunkt-Optimierung:
  1. Berechne Widerstand für mehrere Szenarien:
     − Fahrt mit Aufzugsegel (hull-speed)
     − Schnelle Fahrt ohne Segel
     − Manövrieren (niedriger Schub, hohe Kontrolle)
  
  2. Pitch-Auswahl sollte Kompromiss sein:
     − Eher höher Pitch für Fahrt (Effizienz)
     − Eher niedriger Pitch für Manövrieren (Kraft)
     
  3. Typisch: P/D = 0.9–1.0 ist guter Mittelweg

Oder: Verstellbarer Propeller (wenn Kosten & Komplexität akzeptiert)
  − Blatt-Winkel kann während Fahrt verstellt werden
  − Optimum für jeden Fahrtfall möglich
```

**Prüfkriterium:** Zwei-Punkt-Performance unterscheidet sich > 20% → Überprüfung

---

### 5.11 [F6.11] Material-Korrosion (Elektrolytische Korrosion)

**Symptom:**
- Propeller-Oberfläche rau oder ausgeglichen (Material abgetragen)
- Wenn Aluminium-Propeller: Green Oxidation sichtbar
- Propeller "verbrauch" sich mit der Zeit
- Schub-Verlust über Saison

**Ursache:**
- Galvanische Korrosion (unterschiedliche Metallverbindungen an Schacht/Propeller)
- Mangel-Schutzanode (Opfer-Anode sollte schneller korrodieren als Propeller)
- Wasser-Qualität (verschmutzt, hoher Salzgehalt)

**Folgen:**
```
Korrosion reduziert:
  − Blatt-Dicke (Effizienz sinkt)
  − Oberflächenfinish (Rauheit erhöht Widerstand)
  − Langfristig: Strukturelle Integrität gefährdet
```

**Empforlicht Korrektion:**
```
Prävention (Design):
  1. Schutzanode an Schaft/Propeller anbringen
     − Materialwahl: Zink (höchste Opferbereitschaft)
     − Größe: ca. 2–5% der Propeller-Masse
  
  2. Material-Wahl:
     − Bronze (90% Kupfer): höchste Korrosions-Resistenz (teuer)
     − Aluminium-Bronze: Kompromiß (mittlere Kosten)
     − Aluminium: Budget (Korrosion höher, aber leichter)
  
  3. Oberflächenfinish:
     − Polieren und Lackieren reduziert Korrosion
  
  4. Wartung:
     − Schutzanode regelmäßig überprüfen (sollte "verbrauch" werden)
     − Falls abgetragen: austauschen (kostet ~50–200 EUR)

Periodisch: Propeller reinigen/überprüfen (jährlich oder 2x pro Jahr)
```

**Prüfkriterium:** Propeller rauh/verfärbt oder Anode vollständig verbraucht → Anode austauschen

---

### 5.12 [F6.12] Getriebeöl-Kontamination (Lecks, Lagerung)

**Symptom:**
- Getriebeöl dunkelbraun/schwarz (statt helles Rot)
- Metallische Partikel sichtbar (unter Lupe)
- Getriebe macht Geräusche (Zähnefresser)
- Öl-Level sinkt (Leck)

**Ursache:**
- Heiß-Fahrt ohne Kühlung (Öl-Temperatur > 100°C)
- Wasser-Eindringlichkeit (Feuchtigkeit in Öl)
- Propeller-Ölwelle-Seal abgenutzt
- Material-Verschleiß (normale Alterung)

**Folgen:**
- Getriebe-Verschleiß schneller
- Zahnrad-Schäden möglich
- Getriebe-Ausfalls-Risiko

**Empforlicht Korrektion:**
```
Vorbeugung:
  1. Ölwechsel regelmäßig (typ. jährlich oder nach 200 Betriebsstunden)
  2. Öl-Sorte: synthetisches Getriebeöl (korrosionsresistent)
  3. Kühlung: Öl-Kühler falls langen Fahrtbetrieb
  4. Dichtungs-Wartung: Propeller-Welle-Seal regelmäßig überprüfen
  5. Lagerung trocken (Boot sollte im Winter gut belüftet sein)

Diagnose (Ölprobe):
  − Ölprobe an Labor schicken → Analyse auf Metallpartikel, Wasser etc.
  − Zählt ab Millionen → Verschleiß quantifizierbar
  
Wenn Kontaminierung erkannt:
  − Sofort Öl wechseln
  − Falls Metallpartikel: Getriebe inspizieren (ggf. Service erforderlich)
```

**Prüfkriterium:** Öl dunkelbraun oder Metallglanz sichtbar → Sofort Ölwechsel erforderlich

---

## 6. Propeller-Entwurfs-Prozess

### 6.1 Lastfall-Definition

```
1. Volllast-Fahrt (Max. Geschwindigkeit)
   − Segellos, Motor vollständig
   − Typisch: 6–8 Knoten für Motorsegler
   
2. Manövrieren-Betrieb
   − Unter Segel + Motor (Anluven, Manöver)
   − Typisch: 2–4 Knoten
   
3. Notfall-Betrieb
   − Schwerer Wind, höherer Widerstand
   − Langzeit-Motorbetrieb
```

### 6.2 Widerstandsberechnung

Aus Hydrodynamik-Berechnung (Rumpf-Widerstand):

```
Widerstand_bei_6kn = 5 kN (beispiel für 12m Motorsegler)
Erforderlicher_Schub = Widerstand
Daraus: Propeller-Dimensionierung ableiten
```

### 6.3 Propeller-Auswahl (iterativ)

```
1. Kandidaten auswählen (unterschiedliche D, P, BAR)
2. Für jeden Kandidaten:
   − RPM @ Volllast prüfen (sollte 80–100% Engine-Rating)
   − Effizienz prüfen (Wageningen-Diagramm)
   − Kavitations-Risiko prüfen (σ_crit)
   − Spritverbrauch schätzen
3. Best Candidate wählen (oft Kompromiß)
4. Bestell-Entwurf + Lieferant
5. Test nach Montage (Dynamometer-Test oder Probefahrt)
```

---

## 7. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class PropellerTypeEnum(str, Enum):
    FIXED_PITCH = "fixed_pitch"
    CONTROLLABLE_PITCH = "controllable_pitch"
    WATERJET = "waterjet"
    AZIMUTH = "azimuth"

class PropellerMaterialEnum(str, Enum):
    BRONZE = "bronze"
    ALUMINIUM_BRONZE = "alu_bronze"
    ALUMINIUM = "aluminium"
    STAINLESS_STEEL = "stainless"

class PropellerSpecification(BaseModel):
    """Propeller-Spezifikation"""
    model_config = {"from_attributes": True}
    
    propeller_id: str = Field(..., description="Unique propeller identifier")
    propeller_type: PropellerTypeEnum = Field(..., description="Propeller type")
    material: PropellerMaterialEnum = Field(..., description="Propeller material")
    
    # Dimensions
    diameter_mm: float = Field(..., gt=0, description="Propeller diameter (mm)")
    pitch_mm: float = Field(..., gt=0, description="Pitch (mm)")
    blade_count: int = Field(3, ge=2, le=5, description="Number of blades")
    blade_area_ratio: float = Field(..., gt=0, le=1.0, description="Blade area ratio (BAR)")
    
    # Performance
    rpm_design: float = Field(..., gt=0, description="Design RPM")
    thrust_kn: Optional[float] = Field(None, description="Design thrust (kN)")
    efficiency_percent: Optional[float] = Field(None, ge=0, le=100, description="Propeller efficiency (%)")
    
    # Hydrodynamics
    cavitation_index: Optional[float] = Field(None, description="Cavitation number (σ)")
    cavitation_risk: str = Field("LOW", description="Cavitation risk assessment")
    
    # Operating Conditions
    max_rpm: Optional[float] = Field(None, description="Maximum RPM allowed")
    min_submerged_depth_mm: Optional[float] = Field(None, description="Minimum submerged depth (mm)")
    
    notes: Optional[str] = Field(None, description="Notes on design/selection")

class PropulsionSystemAnalysis(BaseModel):
    """Komplett Propulsions-System Analyse"""
    model_config = {"from_attributes": True}
    
    vessel_name: str = Field(..., description="Yacht name")
    analysis_date: datetime = Field(default_factory=datetime.now)
    
    # Design Loadcases
    design_speed_kn: float = Field(..., description="Target design speed (knots)")
    design_resistance_kn: float = Field(..., description="Hull resistance @ design speed (kN)")
    
    # Engine Spec
    engine_power_kw: float = Field(..., description="Engine power output (kW)")
    engine_rpm_max: float = Field(..., description="Engine maximum RPM")
    gearbox_ratio: float = Field(1.0, description="Gearbox reduction ratio")
    
    # Propeller
    propeller: PropellerSpecification = Field(..., description="Selected propeller")
    
    # Analysis Results
    required_rpm: Optional[float] = Field(None, description="Required RPM for design speed")
    actual_speed_kn: Optional[float] = Field(None, description="Actual achievable speed (knots)")
    slip_percent: Optional[float] = Field(None, description="Propeller slip (%)")
    propulsive_efficiency: Optional[float] = Field(None, description="Overall propulsive efficiency (%)")
    fuel_consumption_lh: Optional[float] = Field(None, description="Fuel consumption (L/h)")
    
    # Compliance
    cavitation_compliant: bool = Field(True, description="Cavitation acceptable")
    aeration_risk: str = Field("LOW", description="Aeration risk assessment")
    
    warnings: List[str] = Field(default_factory=list, description="Design warnings")
    recommendations: List[str] = Field(default_factory=list, description="Recommendations")

def calculate_slip(
    pitch_mm: float, rpm: float, speed_kn: float
) -> float:
    """Berechne Propeller-Schlupf"""
    pitch_m = pitch_mm / 1000
    theoretical_speed_ms = (pitch_m * rpm) / 60
    actual_speed_ms = speed_kn * 0.5144  # Convert knots to m/s
    
    slip = (theoretical_speed_ms - actual_speed_ms) / theoretical_speed_ms * 100
    return slip

def calculate_thrust(
    diameter_mm: float,
    blade_area_ratio: float,
    relative_velocity_ms: float,
    efficiency: float = 0.55,
    water_density: float = 1025
) -> dict:
    """Berechne erforderlichen Propeller-Schub"""
    D_m = diameter_mm / 1000
    A_disk = 3.14159 * (D_m / 2) ** 2
    
    # Momentum theory
    thrust_ideal = 0.5 * water_density * A_disk * (relative_velocity_ms ** 2)
    thrust_real = thrust_ideal * efficiency
    
    return {
        "ideal_thrust_kn": thrust_ideal / 1000,
        "real_thrust_kn": thrust_real / 1000,
        "efficiency_applied": efficiency
    }

def assess_cavitation_risk(
    diameter_mm: float,
    blade_area_ratio: float,
    blade_count: int,
    submerged_depth_mm: float
) -> dict:
    """Bewertz Kavitations-Risiko"""
    # Vereinfacht: BAR > 0.65 und submerged_depth > 300 mm reduzieren Risiko
    
    risk_score = 0
    if blade_area_ratio < 0.45:
        risk_score += 3
    elif blade_area_ratio < 0.55:
        risk_score += 1
    
    if submerged_depth_mm < 250:
        risk_score += 2
    elif submerged_depth_mm < 300:
        risk_score += 1
    
    if blade_count == 2:
        risk_score += 1
    
    if risk_score >= 4:
        risk_level = "HIGH"
    elif risk_score >= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "recommendations": [
            "Increase BAR for lower risk",
            "Mount propeller deeper for lower risk",
            "Monitor for cavitation noise"
        ] if risk_level != "LOW" else []
    }
```

---

## 8. Regulatorischer & normativer Rahmen

> **Hinweis Confidence:** Alle Normbezüge in diesem Abschnitt sind gegen ISO/Herausgeber-Titel verifiziert (Confidence: documented). Zahlenwerte, die aus normpflichtigem Volltext stammen und hier nur aus Vorschau-/Sekundärquellen zitiert werden, sind entsprechend gekennzeichnet.

### 8.1 Fertigungs- und Auslegungsnormen (Propeller)

| Norm | Titel / Scope | Relevanz Auslegung |
|------|---------------|--------------------|
| **ISO 484-1:2015** | Shipbuilding — Ship screw propellers — Manufacturing tolerances — Part 1: Propellers of diameter greater than 2,50 m | Fertigungstoleranzen Grosspropeller (Superyacht-Bereich) |
| **ISO 484-2:2015** | Shipbuilding — Ship screw propellers — Manufacturing tolerances — Part 2: Propellers of diameter between 0,80 and 2,50 m inclusive | Fertigungstoleranzen im typischen Yacht-Durchmesserbereich; gilt für Monobloc-, gebaute und Verstellpropeller (CPP) |
| **ISO 12215-8** | Small craft — Hull construction and scantlings — Part 8: Rudders | Ruderkräfte/-schaft — angrenzend an Propellerstrahl-Anströmung des Ruders |
| **ISO 12215-9** | Small craft — Hull construction — Part 9: Sailing craft appendices (Kiele/Anhänge) | Anhangslasten (Wellenbock/Struts) — Krafteinleitung Antriebsstrang |

Quelle: ISO-Katalog (iso.org, Normnummern/Titel) — Confidence: documented.

> **Wichtig — kein Berechnungsstandard für Wirkungsgrad:** ISO 484 normiert ausschliesslich *Fertigungstoleranzen*, NICHT die hydrodynamische Auslegung. Für die Auslegung selbst gibt es keine verbindliche ISO/EN-Berechnungsnorm; verwendet werden dokumentierte Modellversuchsserien (Wageningen B-Serie, siehe §10) und Klassifikations-/Herstellerverfahren. Nicht ISO 484 für Steigungs-/Wirkungsgradfragen zitieren.

### 8.2 ISO 484 — Genauigkeitsklassen (Fertigungstoleranz Steigung)

ISO 484 definiert vier Genauigkeitsklassen; die Klasse wird vom Besteller gewählt. Absteigende Genauigkeit: **S (very high) → I (high) → II (medium) → III (wide)**.

| Klasse | Toleranz mittlere Steigung (Propeller) | Toleranz Steigung je Blatt | Anzahl Steigungs-Messschnitte |
|--------|----------------------------------------|----------------------------|-------------------------------|
| **S** | ± 0,5 % | ± 0,75 % | 4 |
| **I** | (hoch) | (hoch) | 3 |
| **II** | (mittel) | (mittel) | 2 |
| **III** | ± 3 % | ± 4 % | — |

Quelle: ISO 484-2:2015 (Vorschau/Sekundärzitate, u. a. Power & Motoryacht, TruePropSoftware) — Klassenbezeichnungen und Messschnittzahl: documented; Zwischenwerte Klasse I/II: **estimated — Volltext nicht öffentlich, vor verbindlicher Angabe im Normtext prüfen**.

> **Praxis:** Yacht-Serienpropeller werden i. d. R. nach Klasse S oder I bestellt; eine falsch gescannte/vermessene Steigung erklärt viele „unerklärliche" Drehzahl-/Slip-Abweichungen (siehe Fehlerbild FB-31-06-004).

---

## 9. Vertiefte Grundlagen — dimensionslose Kennwerte & Wirkungsgradkette

### 9.1 Standard-Kennwerte der Freifahrt (open water)

Die international standardisierte Beschreibung eines Propellers erfolgt dimensionslos über den **Fortschrittsgrad J** und die Beiwerte **K_T, K_Q** (ITTC / Modellversuchskonvention):

| Grösse | Definition | Einheiten |
|--------|-----------|-----------|
| Fortschrittsgrad **J** | `J = Va / (n · D)` | Va = Anströmgeschwindigkeit [m/s], n = Drehzahl [1/s], D = Durchmesser [m] |
| Schubbeiwert **K_T** | `K_T = T / (ρ · n² · D⁴)` | T = Schub [N] |
| Momentenbeiwert **K_Q** | `K_Q = Q / (ρ · n² · D⁵)` | Q = Drehmoment [Nm] |
| Freifahrt-Wirkungsgrad **η₀** | `η₀ = (J / 2π) · (K_T / K_Q)` | — |

Quelle: ITTC 7.5-02-03-02.1 Open Water Test; ScienceDirect *Advance Coefficient / Open Water Efficiency*; MARIN/Wageningen — Confidence: documented.

> **Wichtig — n in Umdrehungen pro Sekunde:** In K_T, K_Q und J ist `n` die Drehzahl in **1/s**, nicht 1/min. Der bestehende Slip-Abschnitt (§2.2) rechnet `RPM/60` — das ist konsistent (RPM/60 = n in 1/s).

### 9.2 Wirkungsgradkette Schiff ↔ Propeller (Propulsive Efficiency)

Der Freifahrt-Wirkungsgrad η₀ ist NICHT der Gesamtwirkungsgrad am Schiff. Die dokumentierte Kette (naval architecture Standard):

```
η_D (quasi-propulsiver Wirkungsgrad, QPC) = η₀ · η_H · η_R
```

| Komponente | Bedeutung | Typischer Bereich (Verdränger) |
|-----------|-----------|-------------------------------|
| **η₀** | Freifahrt-Wirkungsgrad des Propellers | Propellerabhängig |
| **η_H** (Rumpfwirkungsgrad, hull efficiency) | `η_H = (1 − t)/(1 − w)`; berücksichtigt Sog­ziffer t und Nachstromziffer w | ~1,0–1,25 |
| **η_R** (Gütegrad der Anordnung, relative rotative efficiency) | Wirkung Nachstromfeld vs. Freifahrt | ~0,98–1,02 |

Weitere Kenngrössen:
- **Nachstromziffer w (Taylor wake fraction):** korrigiert Schiffsgeschwindigkeit V auf Propelleranströmung: `Va = V · (1 − w)`. Für Verdrängerrümpfe typisch w ≈ 0,20–0,35.
- **Sogziffer t (thrust deduction):** der Propeller erhöht den Rumpfwiderstand; erforderlicher Schub `T = R / (1 − t)` (R = Schleppwiderstand).

Quelle: ScienceDirect *Hull Efficiency / Quasi-Propulsive Coefficient / Relative Rotative Efficiency*; Molland/Turnock/Hudson, *Ship Resistance and Propulsion* (Cambridge) — Confidence: documented.

> **Konsequenz für die Auslegung:** Die reine Scheiben-/Momentumrechnung in §4.1 liefert nur eine Grössenordnung. Der am Schiff nutzbare Schub folgt aus `T = R/(1−t)` bei Anströmung `Va = V(1−w)` — deshalb genügt „Widerstand = Schub" (§6.2) nur als Näherung. Confidence: documented (Prinzip); konkrete t/w-Werte sind rumpfspezifisch und **estimated**, solange nicht aus Schlepp-/CFD-Daten belegt.

---

## 10. Wageningen B-Serie — dokumentierte Grundlagen (vertieft)

Die Wageningen B-Serie (auch „Troost-Serie") ist die weltweit meistgenutzte systematische Propeller-Modellversuchsserie, getestet am Netherlands Ship Model Basin (heute MARIN) in Wageningen.

**Kerndaten (verifiziert):**
- Ursprünglich von **L. Troost** in Veröffentlichungen Ende der 1940er-Jahre vorgestellt; daher „Troost series".
- Umfang: **> 120 Propellermodelle**, **2 bis 7 Blätter**, Flächenverhältnisse (A_E/A_O) ca. **0,30 bis 1,05**.
- Freifahrtdaten als **K_T, K_Q über J** in Freifahrtdiagrammen; die gemessenen Daten wurden gefairt und auf eine einheitliche **Reynoldszahl 2 × 10⁶** skaliert.
- Später als **Polynome** (van Lammeren/van Manen/Oosterveld, „Further computer-analyzed data") formuliert: K_T und K_Q als Funktion von Blattzahl Z, Flächenverhältnis A_E/A_O, Steigungsverhältnis P/D und J.

Quelle: MARIN; Oosterveld & van Oossanen, *Further Computer-Analyzed Data of the Wageningen B-Screw Series*; ScienceDirect *Propeller Series* — Confidence: documented.

**Bezeichnungssystematik (Beispiel `B4.55`):**
- `B` = B-Serie
- erste Ziffer = **Blattzahl** (hier 4)
- Dezimalzahl = **Flächenverhältnis A_E/A_O** (hier 0,55)
- Für 4-Blatt-Propeller existieren Flächenverhältnisse 0,40 / 0,55 / 0,70 / 0,85 / 1,00.

Quelle: yumpu/docplayer *Wageningen B-screw series*; ScienceDirect — Confidence: documented.

> **Anwendung (Prinzip, ohne erfundene Zahlen):** Der klassische Entwurfsweg nutzt die B-Serien-Diagramme/Polynome, um bei gegebenem J das Paar (P/D, A_E/A_O) mit maximalem η₀ zu finden, das gleichzeitig das geforderte K_T (Schub) liefert und die Kavitationsgrenze (§3, Burrill-/σ-Kriterium) einhält. Konkrete Ablesewerte sind fallspezifisch und dürfen NICHT ohne eigene Rechnung/Diagramm angegeben werden (Confidence: documented für die Methodik, estimated für jeden Einzelwert).

> ⚠️ **Grenzen der B-Serie:** Die B-Serie beschreibt konventionelle Festpropeller in Freifahrt bei Re = 2×10⁶. Für Falt-/Feathering-Propeller (§12), stark kavitierende, oberflächendurchbrechende oder hochbelastete Propeller ist sie nicht repräsentativ — dann Hersteller-/Modellversuchsdaten verwenden.

---

## 11. Motor–Getriebe–Propeller-Matching (dokumentierte Verfahren)

### 11.1 Drehzahl-Kette

```
n_Propeller = n_Motor / i_Getriebe
```
`i_Getriebe` = Untersetzung (z. B. 2,5:1). Die Propellerdrehzahl (nicht die Motordrehzahl) geht in Slip/J/K_T ein. Confidence: documented (Definitionsgleichung).

### 11.2 Durchmesser- und Steigungs-Erstschätzung (Gerr / Crouch)

Für eine **dokumentierte Erstschätzung** (kein Ersatz für B-Serien-/Herstellerrechnung) sind die empirischen Formeln aus D. Gerr, *The Propeller Handbook* (International Marine/McGraw-Hill) gebräuchlich:

**Durchmesser-Erstwert (Zoll):**
```
D_in ≈ 632,7 · P_shaft_HP^0,2 / RPM_Propeller^0,6
```
(P in Wellen-PS, RPM = Propellerdrehzahl nach Getriebe.)

**Steigung aus Slip (Zoll):**
```
P_in = (V_kn · 1215,2) / (RPM_Propeller · (1 − Slip))
```
(1215,2 = ft/min·12 pro Knoten; Herleitung: 1 kn = 101,27 ft/min.)

**Faustregeln (Crouch, „sehr grob"):**
- 1″ Durchmesser bindet grob das Drehmoment von 2–3″ Steigung.
- 1″ Durchmesseränderung ≈ 300 RPM Änderung; 2″ Steigungsänderung ≈ ähnliche Grössenordnung. **Durchmesser hat grösseren Einfluss als Steigung.**

Quelle: D. Gerr, *The Propeller Handbook*; Crouch-Methode (FAO x0487e; hullmetric; Sekundärzitate) — Confidence: documented (als empirische Näherung); die resultierenden Einzelwerte sind **estimated** und per Probefahrt zu verifizieren (§11.4).

> **Warum das die `LWL/6`-Regel ersetzt:** Der Durchmesser skaliert dokumentiert mit **Wellenleistung und Drehzahl**, nicht mit der Wasserlinienlänge. Grosse, langsam drehende Propeller sind bei Verdrängern effizienter und kavitationssicherer (§13.3) — begrenzt allein durch den verfügbaren Tip-Clearance (§11.3).

### 11.3 Tip-Clearance / Einbaugrenzen

Der real montierbare Durchmesser ist durch den Abstand Blattspitze↔Rumpf/Wellenbock (tip clearance) und die Eintauchtiefe begrenzt, nicht durch eine Längen-Faustformel. Zu kleiner Tip-Clearance → druckinduzierte Rumpfvibration und Kavitation; zu geringe Eintauchung → Belüftung (§3.2, Fehlerbild FB-31-06-007).

> ⚠️ **ZU PRÜFEN:** Konkrete Mindest-Tip-Clearance-Prozentwerte (verbreitet werden 15–20 % von D genannt) konnten in dieser Recherche nicht an einer Primärquelle (Klassifikation/ISO) zweifelsfrei belegt werden → hier bewusst KEIN Zahlenwert. Vor verbindlicher Nutzung Klassenvorschrift (z. B. DNV/Lloyd's/GL Yacht-Regeln) prüfen. Confidence: estimated — unverifiziert.

### 11.4 Probefahrt-Kriterium (WOT / Wide Open Throttle)

Verbindlicher Praxis-Abgleich: Bei Volllast (WOT), **voll beladen**, muss der Motor seine Nenndrehzahl (rated RPM) erreichen — üblich innerhalb ca. **200 RPM** der Herstellernenndrehzahl.

| Befund WOT | Diagnose | Massnahme |
|-----------|----------|-----------|
| RPM **unter** Nenn, nicht erreichbar | **überbepitcht/überdimensioniert** (over-propped) | Steigung/Durchmesser reduzieren — Dauerbetrieb schädigt Motor (verbrannte Auslassventile, thermische Überlast) |
| RPM **über** Nenn | leicht unterbepitcht (under-propped) | i. d. R. tolerabel/leicht günstig; ggf. Steigung leicht erhöhen für Effizienz |
| RPM ≈ Nenn ± 200 | korrekt abgestimmt | ok |

Quelle: Volvo Penta *Propeller Guide*; RubexProps WOT-Charts; The Hull Truth (Diesel-Praxis) — Confidence: documented.

> **Diesel-Besonderheit:** Elektronisch geregelte Diesel sind etwas propeller-toleranter als mechanisch eingespritzte, aber die Nenndrehzahl muss bei vollen Tanks erreichbar bleiben. Dauer-WOT auf einem over-propped Diesel ist ein klassischer Schadensmechanismus.

---

## 12. Produkt-/Verfahrensübersicht — reale Propellertypen (Segelyacht-Antrieb)

Für Segelyachten mit Hilfsmotor sind schleppwiderstandsarme Falt-/Feathering-Propeller marktrelevant. Nur **belegte, reale Hersteller/Prinzipien** (keine erfundenen Modell-/Preisangaben):

| Hersteller / Marke | Prinzip | Belegte Merkmale |
|--------------------|---------|------------------|
| **Flexofold** (DK) | Faltpropeller (folding) | Blätter falten nach achtern zusammen; geringer Segelwiderstand, weniger Verfangen von Leinen/Kelp |
| **Gori** (DK, seit 1975) | Faltpropeller, 2-/3-Blatt | Bronze-Nabe/-Blätter, Edelstahlstifte; „Overdrive"-/Mehrgang-Faltmechanik |
| **Max-Prop** | Feathering (Blätter fahnen bei Segeln) | Sehr geringer Segelwiderstand, kein Freilauf in Neutral, verstellbare Steigung, starke Rückwärtswirkung |
| **Bruntons AutoProp** (seit 1987) | Feathering mit lastabhängiger Selbstverstellung | Blätter gekoppelt; Steigung stellt sich mit Drehzahl/Anströmung ein (H5-/H6-Serie) |
| **Volvo Penta** | Falt- und Feathering-Optionen | Zubehör zum eigenen Saildrive/Wellenantrieb |

Quelle: Practical Sailor *Folding vs. Feathering*; Yachting Monthly Propellertest; getaprop.com (Bruntons AutoProp H5/H6) — Confidence: documented (Herstellerexistenz/Prinzip). Konkrete Durchmesser/Steigungen/Preise sind modellspezifisch beim Hersteller zu verifizieren.

> **Auslegungshinweis:** Falt-/Feathering-Propeller haben andere K_T/K_Q-Charakteristik als B-Serien-Festpropeller (§10). Steigung/Durchmesser NICHT 1:1 vom Festpropeller übernehmen — Herstellerauslegung anfordern.

**Blattzahl-Auswahl (dokumentierte Tendenzen):**
- Mehr Blätter → geringere Anregungsamplitude je Umdrehung, i. d. R. ruhigerer Lauf; höhere Blattfolgefrequenz.
- **Blattfolgefrequenz** `f = Z · n` (Z = Blattzahl, n = Drehzahl in 1/s). Beispiel-Grössenordnung (Quelle continuouswave): 3 Blätter @ 500 RPM → 25 Hz; 4 Blätter @ 500 RPM → 33,3 Hz. Blattzahl verschiebt die Anregungsfrequenz — Ziel ist, Resonanzen der Rumpf-/Antriebsstruktur zu meiden (nicht „mehr Blätter = immer besser").

Quelle: continuouswave (Blattfolgefrequenz-Rechnung); BoatTEST/WakeMAKERS (3- vs. 4-Blatt) — Confidence: documented.

---

## 13. Slip, Kavitation & Tip Speed — Ergänzungen

### 13.1 Slip-Bandbreiten (verifiziert)

Typische **apparent slip**-Werte (dokumentiert):
- Verdränger-/Deplacement-Rümpfe: ca. **15–20 %** (teils bis 25 % genannt).
- Gleiter (planing): ca. **10–15 %**.

Quelle: Gerr/Crouch (Displacement 15–20 %); vif propellers / firgelli (Boote 15–25 %) — Confidence: documented. Die im Bestand (§2.2) genannten „~10–20 %" liegen im belegten Rahmen.

### 13.2 Kavitationszahl — konsistente Definition

Die Bestandsformel in §3.1 ist konsistent mit der dokumentierten Propeller-Definition:
```
σ = (P_atm + P_hydro − P_vapor) / (½ · ρ · Va²)
```
mit P_hydro = ρ·g·h (hydrostatischer Druck in Eintauchtiefe h). Niedriges σ → höheres Kavitationsrisiko.
Quelle: ScienceDirect *Cavitation Number*; Grokipedia/Numberanalytics — Confidence: documented.

> **Hinweis:** Die kritische Grenze σ_crit ist KEINE feste Zahl; sie hängt von Blattschnitt, Belastung (K_T) und Flächenverhältnis ab und wird klassisch über das **Burrill-Diagramm** bzw. Kavitationskriterien nach Flächenverhältnis bestimmt. Der Bestand-Bereich „0,3–0,8" ist als grobe Orientierung zu lesen (Confidence: estimated), nicht als Auslegungsgrenze.

### 13.3 Tip Speed / niedrige Drehzahl

Dokumentiert: Eine **niedrige Propellerdrehzahl** ist ein besonders wirksames Mittel, um Kavitation an der Saugseite zu verzögern; Verdränger profitieren von **grossem Durchmesser + niedriger Drehzahl**. Umgekehrt fördern hohe Drehzahl/hohe Umfangsgeschwindigkeit, zu geringe Blattfläche und Betrieb in Unterdruckzonen die Kavitation.
Quelle: ScienceDirect *Propeller Cavitation / Propeller RPM* — Confidence: documented.

---

## 14. Fehlerbild-Atlas (FB-31-06-NNN)

> ID-Schema: `FB-31-06-NNN`, fortlaufend, **kollisionsfrei** zum bestehenden `[F6.x]`-Schema in §5. Diese Einträge ergänzen §5 um belegte Diagnosekriterien; wo ein `[F6.x]`-Bezug besteht, ist er genannt.

### FB-31-06-001 — Over-propped (Nenndrehzahl bei WOT nicht erreichbar)
- **Bezug:** ergänzt [F6.2].
- **Symptom:** Motor erreicht bei Volllast/voll beladen die Nenndrehzahl nicht (> ~200 RPM darunter), schwarzer Rauch, thermische Überlast.
- **Ursache:** Steigung und/oder Durchmesser zu gross; Untersetzung zu klein; Bewuchs/Zusatzwiderstand.
- **Prüfkriterium:** WOT-RPM < (Nenn − 200) bei voller Beladung.
- **Massnahme:** Steigung/Durchmesser reduzieren (Faustregel §11.2). Kein Dauer-WOT (Ventil-/Turboschaden).
- Quelle: Volvo Penta Propeller Guide — Confidence: documented.

### FB-31-06-002 — Under-propped (WOT-RPM über Nenn)
- **Symptom:** Motor dreht bei WOT über Nenndrehzahl hoch.
- **Ursache:** Steigung/Durchmesser zu klein; Boot leichter als angenommen.
- **Prüfkriterium:** WOT-RPM > Nenndrehzahl.
- **Massnahme:** meist tolerabel; für Effizienz Steigung leicht erhöhen (Kontrolle: bleibt Nenn erreichbar).
- Quelle: RubexProps/Volvo Penta — Confidence: documented.

### FB-31-06-003 — Falsche Genauigkeitsklasse / vermessene Steigung
- **Symptom:** Rechnerisch korrekt ausgelegter Propeller trifft Drehzahl/Speed nicht; Blätter untereinander ungleich.
- **Ursache:** Fertigung/Reparatur ausserhalb ISO-484-Klasse; Steigung je Blatt unterschiedlich (Blade-to-blade-Abweichung).
- **Prüfkriterium:** Steigungs-Scan; Abweichung > zulässige Toleranz der bestellten Klasse (S: mittlere Steigung ±0,5 %; III: ±3 %).
- **Massnahme:** Propeller nachvermessen/nacharbeiten lassen, korrekte Klasse bestellen.
- Quelle: ISO 484-2:2015; TruePropSoftware Scan-Report — Confidence: documented (Klassenwerte S/III), estimated (I/II-Zwischenwerte).

### FB-31-06-004 — Falsch skalierte Wageningen-Ablesung (Re/Massstab)
- **Symptom:** Aus B-Serien-Diagramm abgeleiteter Wirkungsgrad/Schub wird real nicht erreicht.
- **Ursache:** B-Serie gilt für Re = 2×10⁶; Anwendung ohne Massstabs-/Rauheitskorrektur oder ausserhalb des Serienbereichs (Falt-/Feathering-Prop).
- **Prüfkriterium:** Prop-Typ nicht konventioneller Festpropeller ODER Betriebs-Re stark abweichend.
- **Massnahme:** Hersteller-/Modellversuchsdaten statt B-Serie; Korrekturen anwenden.
- Quelle: MARIN/Oosterveld — Confidence: documented.

### FB-31-06-005 — Nachstrom/Sog vernachlässigt (Schub-Fehldimensionierung)
- **Symptom:** „Widerstand = Schub"-Auslegung liefert zu wenig realen Schub.
- **Ursache:** Sogziffer t und Nachstromziffer w ignoriert; Va = V(1−w) und T = R/(1−t) nicht angesetzt.
- **Prüfkriterium:** Auslegung ohne t/w-Ansatz bei Verdrängerrumpf (w typ. 0,20–0,35).
- **Massnahme:** Wirkungsgradkette §9.2 ansetzen; t/w aus Schlepp-/CFD-Daten.
- Quelle: ScienceDirect Hull Efficiency/QPC — Confidence: documented (Prinzip).

### FB-31-06-006 — Galvanische Korrosion / falsches Anodenmaterial
- **Bezug:** ergänzt [F6.11].
- **Symptom:** Propeller/Welle abgetragen, Anode zu schnell/zu langsam verbraucht.
- **Ursache:** Anodenmaterial passt nicht zum Gewässer; gemischte Anodenmetalle.
- **Prüfkriterium (Materialwahl):** **Zink** = Salzwasser; **Aluminium** = Salz-/Brackwasser (breitere Abdeckung); **Magnesium** = Süsswasser (höhere Treibspannung bei geringer Leitfähigkeit). Anodenmetalle NICHT mischen.
- **Massnahme:** korrektes Material; Anode bei ~50 % Abtrag ersetzen (auch bei Passivierung/Lockerung).
- Quelle: West Marine / Fisheries Supply / Yachting Monthly — Confidence: documented.

### FB-31-06-007 — Belüftung durch zu geringe Eintauchung / Tip-Clearance
- **Bezug:** ergänzt [F6.7].
- **Symptom:** plötzlicher Schubverlust bei Krängung/Manöver, Motor „durchdreht".
- **Ursache:** Propeller zu hoch/zu wenig eingetaucht; zu geringer Tip-Clearance.
- **Prüfkriterium:** siehe §11.3 (Zahlenwert unverifiziert → Klassenregel prüfen).
- **Massnahme:** Eintauchung/Position optimieren; Trimm/Beladung achtern reduzieren.
- Quelle: ScienceDirect Cavitation/Ventilation-Prinzip — Confidence: documented (Prinzip).

### FB-31-06-008 — Resonante Blattfolgefrequenz (Vibration)
- **Bezug:** ergänzt [F6.8].
- **Symptom:** ausgeprägte Vibration in einem engen RPM-Band.
- **Ursache:** Blattfolgefrequenz `f = Z·n` trifft Eigenfrequenz Rumpf/Antriebsstrang.
- **Prüfkriterium:** Vibrationsmaximum bei bestimmter RPM; f = Z·n in Resonanznähe.
- **Massnahme:** Blattzahl ändern (verschiebt f), RPM-Band meiden, dynamisch auswuchten.
- Quelle: continuouswave/ScienceDirect Blade Rate — Confidence: documented.

---

## 15. Troubleshooting — Entscheidungsbaum (Drehzahl/Speed-Abweichung)

```
Boot erreicht Ziel-Speed/-RPM nicht?
│
├─ WOT-RPM UNTER Nenn (nicht erreichbar)?
│   ├─ Rumpf/Propeller bewachsen? → reinigen, erneut messen
│   ├─ nach Reinigung weiter zu niedrig? → OVER-PROPPED (FB-31-06-001)
│   │     → Steigung/Durchmesser reduzieren (§11.2), NICHT Dauer-WOT
│   └─ Steigung je Blatt ungleich (Scan)? → ISO-484-Toleranz verletzt (FB-31-06-003)
│
├─ WOT-RPM ÜBER Nenn?
│   → UNDER-PROPPED (FB-31-06-002) → Steigung leicht erhöhen, Nenn muss erreichbar bleiben
│
├─ RPM korrekt, aber Speed niedrig / hoher Slip?
│   ├─ Slip > belegter Bereich (Verdränger 15–20 %)? 
│   │     → t/w vernachlässigt (FB-31-06-005) ODER Kavitation/Belüftung
│   ├─ weisse Schlieren/Lärm/Erosion? → Kavitation (§3/§13) → BAR↑, D↑, RPM↓, tiefer
│   └─ Schubverlust bei Krängung/Manöver? → Belüftung (FB-31-06-007) → Eintauchung/Trimm
│
└─ Vibration in engem RPM-Band?
    → Resonante Blattfolgefrequenz (FB-31-06-008) → Blattzahl/RPM-Band/Wuchtung
```
Confidence: documented (jeder Ast auf belegte Kriterien der §§8–13 gestützt).

---

## 16. Wartung & Prüffristen

> **Confidence-Hinweis:** Intervalle sind Praxis-Richtwerte aus Hersteller-/Fachquellen (documented als Konvention), keine verbindliche Norm. Herstellervorgaben haben Vorrang.

| Objekt | Prüfung | Richtintervall | Kriterium / Quelle |
|--------|---------|----------------|--------------------|
| Opferanode (Welle/Propeller) | Sichtprüfung Abtrag | Saison / bei Slippen | Ersatz bei ~50 % Abtrag, Passivierung, Lockerung (West Marine — documented) |
| Anodenmaterial | Passt zum Gewässer? | bei Standortwechsel | Zink=Salz, Alu=Brack, Mg=Süss (documented) |
| Propellerblätter | Kavitationserosion, Dellen, Kantenschäden | jährlich (Slippen) | sichtbare Erosion → §3.1/FB-31-06 (documented Prinzip) |
| Steigung/Balance | Scan/Auswuchten nach Grundberührung | ereignisbezogen | Toleranz der ISO-484-Klasse; dynamisch wuchten |
| WOT-Drehzahl | Probefahrt voll beladen | nach Prop-/Motoränderung, jährlich | Nenn ± ~200 RPM (Volvo Penta — documented) |
| Wellendichtung/Getriebeöl | Lecks, Ölzustand | siehe [F6.12] | Herstellerintervall |

---

## 17. FAQ

**F: Grösserer Durchmesser oder mehr Steigung, wenn zu langsam?**
A: Zuerst prüfen, ob WOT-Nenndrehzahl erreichbar ist (§11.4). Durchmesser wirkt stärker auf die Drehzahlaufnahme als Steigung (Crouch, §11.2). Bei Verdrängern ist grösser + langsamer meist effizienter und kavitationssicherer — begrenzt durch Tip-Clearance. Confidence: documented.

**F: Warum stimmt meine „Widerstand = Schub"-Rechnung nicht?**
A: Weil Nachstrom (Va = V(1−w)) und Sog (T = R/(1−t)) fehlen. Realer Schubbedarf ist höher als der reine Schleppwiderstand. Siehe §9.2. Confidence: documented.

**F: Kann ich B-Serien-Diagrammwerte direkt auf meinen Faltpropeller anwenden?**
A: Nein. Die B-Serie beschreibt konventionelle Festpropeller (Re 2×10⁶). Für Falt-/Feathering-Propeller Herstellerdaten verwenden. Confidence: documented.

**F: Welche Anode — Zink, Aluminium oder Magnesium?**
A: Salzwasser Zink, Brackwasser Aluminium, Süsswasser Magnesium; Metalle nicht mischen; bei ~50 % Abtrag ersetzen. Confidence: documented.

**F: 3 oder 4 Blätter?**
A: Mehr Blätter → oft ruhiger und höhere Blattfolgefrequenz, aber kein Pauschalvorteil — entscheidend ist, Resonanzen (f = Z·n) zu meiden und die geforderte Fläche (Kavitation) bereitzustellen. Confidence: documented.

---

## 18. Glossar

| Begriff | Bedeutung |
|---------|-----------|
| **J** (Fortschrittsgrad) | Va/(n·D), dimensionslose Betriebskennzahl |
| **K_T / K_Q** | Schub-/Momentenbeiwert (dimensionslos) |
| **η₀** | Freifahrt-Wirkungsgrad des Propellers |
| **η_D / QPC** | Quasi-propulsiver Wirkungsgrad = η₀·η_H·η_R |
| **w** (Nachstromziffer) | Va = V(1−w); Verdränger typ. 0,20–0,35 |
| **t** (Sogziffer) | T = R/(1−t) |
| **A_E/A_O** | Flächenverhältnis (expanded area ratio); ≈ BAR |
| **P/D** | Steigungsverhältnis |
| **Slip** | Differenz theoretische (P·n) vs. reale Fahrt, in % |
| **σ (Kavitationszahl)** | (P_atm+P_hydro−P_vapor)/(½ρVa²) |
| **Blattfolgefrequenz** | f = Z·n (Z Blattzahl, n in 1/s) |
| **WOT** | Wide Open Throttle (Volllast-Probefahrt) |
| **CPP** | Controllable Pitch Propeller (Verstellpropeller) |
| **B-Serie / Troost-Serie** | Wageningen-Modellversuchsserie |

---

## 19. Quellen (verifiziert)

- ISO-Katalog: ISO 484-1:2015, ISO 484-2:2015 (Titel/Scope) — iso.org
- ISO 484-2:2015 Genauigkeitsklassen — ansi.org / iteh.ai Vorschau; TruePropSoftware; Power & Motoryacht (Sekundär)
- Wageningen/Troost B-Serie — MARIN (marin.nl); Oosterveld & van Oossanen *Further Computer-Analyzed Data of the Wageningen B-Screw Series*; ScienceDirect *Propeller Series*
- Freifahrt-Kennwerte J/K_T/K_Q/η₀ — ITTC 7.5-02-03-02.1 Open Water Test; ScienceDirect *Advance Coefficient / Open Water Efficiency*
- Wirkungsgradkette QPC/η_H/η_R/w/t — ScienceDirect *Hull Efficiency / Quasi-Propulsive Coefficient / Relative Rotative Efficiency*; Molland/Turnock/Hudson *Ship Resistance and Propulsion* (Cambridge)
- Kavitationszahl σ — ScienceDirect *Cavitation Number*; Numberanalytics
- Kavitation/Drehzahl (Verdränger) — ScienceDirect *Propeller Cavitation / Propeller RPM*
- Slip / Gerr / Crouch — D. Gerr *The Propeller Handbook*; FAO x0487e (Crouch); hullmetric; vif propellers; firgelli
- WOT / Propeller-Matching — Volvo Penta *Propeller Guide*; RubexProps WOT-Charts; The Hull Truth
- Blattzahl / Blattfolgefrequenz — continuouswave; BoatTEST; WakeMAKERS
- Falt-/Feathering-Propeller — Practical Sailor *Folding vs. Feathering*; Yachting Monthly Propellertest; getaprop.com (Bruntons AutoProp)
- Anoden/Galvanik — West Marine *Preventing Galvanic Corrosion*; Fisheries Supply; Yachting Monthly *guide to aluminium anodes*

---

**Datei abgeschlossen.**  
Kat 31.06 Propellerauslegung — Version 2.0 — 2026-07  
Änderungen v2.0: Normrahmen (ISO 484), dimensionslose Kennwerte & Wirkungsgradkette (QPC/w/t), Wageningen-B-Serie vertieft, Motor-Getriebe-Matching (Gerr/Crouch/WOT), reale Falt-/Feathering-Hersteller, Fehlerbild-Atlas FB-31-06-001…008, Entscheidungsbaum, Wartung/FAQ/Glossar. `LWL/6`-Durchmesserregel zurückgezogen (durch Gerr-Methode ersetzt). Alle Faktangaben web-verifiziert oder als „estimated/ZU PRÜFEN" gekennzeichnet.
