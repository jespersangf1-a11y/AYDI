# 31_09 — Ruder-Design

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Ruder_Design  
**Version:** 2.0  
**Stand:** 2026-05-18  
**Relevanz:** Kern-Konstruktionswissen für Manöver, Kontrolle, Seelage

---

## Übersicht

Das Ruder ist der **primäre Kontroll-Element** für Kurshaltung, Manöver und Notfall-Handling. AYDI analysiert Ruderbauart (Spade, Skeg-hung, Transom), Profilwahl, Dimensionierung und kritische Ausfallszenarios.

**Fehleranalyse-Schwerpunkte:**
1. Ruder-Torque zu hoch (Kraft bei Drehen)
2. Ruder-Fläche zu klein (mangelhafte Kontrolle, besonders unter Motor)
3. Profilform nicht für Heel-Winkel optimiert
4. Kavitation bei hoher Fahrtgeschwindigkeit
5. Delamination / Hohlräume im Ruderlaminat
6. Bolzen-Korrosion + Festfressen
7. Lager-Verschleiß (Pintle/Gudgeon)
8. Dynamische Flattern-Resonanz
9. Ruderkopf-Bruch bei Übersteuerung
10. Seaweed-Wicklung / Verhängung
11. Notfall-Ruder-Versagen (Hydraulik-Ausfall bei Power-Steering)
12. Anschluss-Laminat zu dünn (Übergangszone)

---

## 1. Ruderbauarten und Auswahl

### 1.1 Spade Rudder (Spatenruder)

**Charakteristik:**
- Freistehende Flosse, vollständig im Wasser
- Befestigung: oben durch Ruderkopf/Flansch, unten am Ruderschaft
- Keine Unterstützung durch Skeg oder Transom

**Dimensionierung (Segelboot-Standard):**

```
Ruder_Fläche [m²] = (Segelplan_Area [m²] × 0.045) / Boot_Length [m]
Typisch: 8–14% der Segel-Fläche
Aspektverhältnis: 2,5–4,0 (höher → bessere Wendigkeit, weniger Kraft)

Beispiel 12m Segelboot:
  Segelplan = 120 m² (Hauptsegel + Vorsegel)
  Ruder_Fläche = (120 × 0.045) / 12 = 0,45 m²
  Tiefgang Ruder ≈ 1,0–1,3m
  Profil-Breite (Chord) ≈ 450–500 mm
```

**Profil-Auswahl:**

| Profil | Typ | L/D (Best) | Wendigkeit | Auftrieb @ Heel | Einsatz |
|--------|-----|-----------|-----------|-----------------|---------|
| NACA 0012 | Symmetrisch | 35 | Sehr hoch | Niedrig | Rennboot |
| NACA 63a618 | Laminar | 55 | Moderat | Moderat | Cruiser-Racing |
| NACA 64a618 | Laminar, robust | 50 | Moderat | Moderat | Production |
| Custom Laminar | Optimal | 70+ | Moderat | Hoch | Yacht-Design |

**Torque-Anforderung (Steuerrad):**

> ⚠️ **ZU PRÜFEN (Audit):** Rechenbeispiel inkonsistent und nicht nachvollziehbar. Die Formel 0,5·ρ·v²·A·C_f liefert eine Ruder*kraft* [N], kein Drehmoment [N·m] (hier fälschlich als „Rudertorque … N·m" bezeichnet). Zudem ergibt 0,5 × 1025 × 4,1² × 0,45 × 1,75 ≈ 6784 N, nicht 1685; auch der Schritt zur Lenkkraft (5,6 N) ist ohne ausgewiesene Übersetzung/Hebelarm nicht belegt. Steht im Widerspruch zur Methodik in §3.1 (dort werden Kraft und Schaftmoment über einen Hebelarm getrennt). Ruderkraft, Schaftmoment (Torque T) und Biegemoment M bitte nach ISO 12215-8 (Small craft — Rudders) auslegen. **Verifiziert (Web, 2026-07):** F = ½·ρ·v²·A·c_f ist physikalisch eine Kraft (mit den Beispielwerten ≈ 6784 N); ein Schaftmoment [N·m] entsteht erst über den Sehnen-Hebelarm r — nach ISO 12215-8 greift die Ruderkraft ≈ 0,30·c hinter der Profilnase an, r = 0,30·c − Schaftposition. Diese Schaftposition fehlt im Beispiel, daher ist kein belastbares Drehmoment ableitbar → Zahlen markiert, nicht korrigiert.

```
Rudertorque_ohne_Servo [N·m] = 0.5 × ρ × v² × Ruder_Fläche × C_f
ρ = 1025 kg/m³ (Salzwasser)
v = Boot-Geschwindigkeit [m/s]
C_f = Profil-abhängiger Kraftbeiwert (1,5–2,0 bei 30° Ausschlag)

Beispiel: 12m Boot, 8 kn (4,1 m/s), Spade 0,45 m², Ruder 30° ausgelenkt
Torque = 0.5 × 1025 × 4.1² × 0,45 × 1.75 = 1685 N·m ≈ 1,7 kN·m

Handradsystem erforderlich: Übersetzung mindestens 40:1
Lenkrad-Durchmesser 600 mm → Lenkkraft ≈ 5,6 N (sehr komfortabel)
```

**Vorteile:**
- Maximale Wendigkeit
- Keine Unterstützung durch Hull → komplett austauschbar
- Elegant, klassischer Look

**Nachteile:**
- Höchste Belastung auf Ruderkopf-Flansch
- Grounding-anfällig (tiefster Punkt)
- Komplexe Abdichtung an Ruderkopf
- Hull-Perforation erforderlich

### 1.2 Skeg-Hung Rudder (Skeg-aufgehängtes Ruder)

**Charakteristik:**
- Ruder hängt an Skeg (laterale Flossenstruktur)
- Skeg verläuft über 40–60% der Kiellänge
- Pintle/Gudgeon-Verbindung am Skegende

**Dimensionierung:**

```
Ruder_Tiefgang = Skeg_Höhe (typisch 0,6–1,0m)
Ruder_Breite reduziert (Chord ≈ 350–400 mm, nicht 450+)
  → Ruder_Fläche 60–75% des Spade-Equivalent

Skeg_Funktion:
  1. Träger für Ruder-Last
  2. Zusätzliche Stabilität (Leeway-Reduktion 5–10%)
  3. Schutz Ruder-Unterseite vor Grounding
```

**Typisches Dimensionungs-Beispiel (14m Segelboot):**

```
Skeg-Länge: 3,5m (25% der LOA)
Skeg-Höhe: 0,85m
Ruder-Fläche (Skeg-aufgehängt): 0,35 m² (70% des freien Spade)
Pintle-Positionen: 2–3 (Ober-, Mittel-, Unterseite)
```

**Vorteile:**
- Reduzierter Torque (Skeg trägt teilweise)
- Schutz vor Grundberührung
- Traditionell bewährt (robustes System)
- Einfachere Abdichtung (oben am Skeg)

**Nachteile:**
- Schwieriger auszutauschen (Skeg ist strukturell)
- Leicht höherer Widerstand (Skeg selbst)
- Wendigkeit nicht optimal (verteilte Aufhängung)
- Seegras-Wicklung häufiger

### 1.3 Transom-Hung Rudder (Heck-aufgehängtes Ruder)

**Charakteristik:**
- Ruder befestigt direkt am Heckspant (Transom)
- Typisch für Motor-Yachten, Motorsegler
- Pintle/Gudgeon-System vertikal

**Dimensionierung:**

```
Ruder_Position: unterhalb Wasserlinie, hinter Propeller
Ruder_Fläche: typisch 0,3–0,5 m² (20–30% der Segelboot-Fläche)
  → Ausreichend, da Boot unter Motor weniger wendigkeit-abhängig

Transom_Tiefe_erforderlich: mindestens 250 mm Struktur-Material
Motor_Clearance: 100 mm Abstand Propeller → Ruder_Vorderkante
```

**Profil-Wahl für Motorboot:**
- NACA 63a618: standard, robust
- Symmetrisch (0012): reduziert Moment-Drift bei Richtungswechsel

**Vorteile:**
- Einfache Befestigung
- Leicht zugänglich (keine Kielbohrung)
- Ideal für Retrofit auf Motorsysteme
- Robuster für Grounding (näher an Struktur)

**Nachteile:**
- Geringere Wendigkeit (kleinere Fläche, längere Hebel)
- Propeller-Blasstrom beeinträchtigt Ruder-Effizienz
- Cavitation-risiko höher (direkt hinter schnellem Propeller)
- Strukturelle Anforderung: Transom muss sehr rigid sein

### 1.4 Balanced Rudder (Ausgewogenes Ruder)

**Charakteristik:**
- Teil der Ruder-Fläche vor dem Drehpunkt-Schaft (Balancing Tab)
- Reduziert Torque bis 40%

**Physik:**
```
Torque_unbalanced = 0,5 × ρ × v² × A_total × C_f × c_neutral_point

Mit Balance (20% vor Schaft):
Balance_Force = 0,5 × ρ × v² × A_balance × C_f_opposite
Net_Torque = Torque_total − Balance_Force × Balance_Arm

Typisch: Torque_reduction 30–40%
```

**Praktischer Nutzen:**
- Boote <8m oder sehr hohe Geschwindigkeits-Anforderung
- Hydraulisch angetriebene Systeme (weniger Kraft erforderlich)
- Racing-Yachten (Servo-Motor-Fähigkeit erhöht)

**Beispiel-Dimensionierung:**

```
Unbalanced Spade, 0,45 m²:
  Schaftposition bei 35% Chord
  → 65% Fläche hinter Schaft, 35% davor = Imbalance!

Balanced Spade, 0,45 m²:
  Schaftposition bei 50% Chord
  → 50% hinter, 50% davor (ideal)
  → Aber: Stall-Verhalten anders (Profil-Asymmetrie)

Teilweise balanced (25% vor):
  Schaftposition bei 40% Chord
  → 60% hinter, 40% davor
  → Torque-Reduktion ≈ 30%, Stall-Punkt verbessert
```

**Nachteile:**
- Komplexere Herstellung
- Druckverteilung über Schaft ungleichmäßig
- Ventilations-Risiko bei hohem Anstellwinkel

---

## 2. NACA-Profilwahl und Aerodynamische Eigenschaften

### 2.1 Standard-Profile für Ruder

**NACA 63a618 (häufigste Wahl für Cruiser):**

```
Eigenschaften:
  Dicke: 18% der Tiefe (Chord)
  Laminar-Region: bis Cl ≈ 0,8
  Null-Auftrieb-Winkel: ca. 0° (symmetrisches Verhalten bei pos/neg Anstellwinkel)
  Max-L/D: ≈55 bei Cl ≈ 1,2
  Stall-Anstellwinkel: ±18–20°

Vorteile:
  - Robust gegen Verschmutzung
  - Gutes Kurvenverhalten über breites Heel-Spektrum
  - Gleiches Verhalten bei Rudder Left/Right (nicht pendling)

Nachteil:
  - Nicht optimal dünn (Widerstand 5–10% höher als Custom)
```

**NACA 0012 (reines Racing/symmetrisch):**

```
Eigenschaften:
  Dicke: 12% (sehr dünn)
  Profil: mathematisch symmetrisch
  Max-L/D: ≈35 (geringer als gewölbte Profile)
  Vorteil: Gleiches Verhalten bidirektional

Verwendung:
  - Nur für Rennboote, wo Manöver häufig (Wechsel von Links ↔ Rechts)
  - Match mit Double-Sided-Servolenkung
  - Höhere Antriebs-Kraft erforderlich (höheres Torque)
```

**Custom Laminar-Profile (Modern Racing):**

```
Kosten: EUR 20000–40000 für numerische Optimierung
Typischer Einsatz: IMS-Regel-Boote, Offshore-Rennsegler

Optimierung:
  - LES-CFD für Strömungs-Übergang (Laminar-Bereich maximiert)
  - Anpassung an typisches Heel-Spektrum (z.B. 0°–25°)
  - Torque-Charakteristik für Servo-Motor voroptimiert

Ergebnis:
  - L/D bis 70–80 (vs. 55 bei NACA 63a)
  - Torque-Reduktion 15–20% durch Profilform
  - Bestzeit-Gewinn: 0,5–1,0% Geschwindigkeit (ggf.)
```

### 2.2 Profilform-Effekt auf Heel-Verhalten

**Problem: Ruder-Auftrieb variiert mit Heel-Winkel**

```
Bei aufrechtem Boot (Heel 0°):
  Auftrieb-Richtung: senkrecht zum Profil (≈ horizontal)
  
Bei 20° Heel (typisch Segelboat):
  Boot neigt sich, Ruder neigt sich mit
  Auftrieb-Vektor: teilweise nach oben (hebt Boot)
  → "Weather Helm" Effekt (zusätzliches Drehmoment)

Auftrieb-Komponente-Analyse:
  L_total = Profil-Auftrieb basiert auf Anstellwinkel relativ Wasser-Strömung
  L_horizontal (Drehmoment-wirksam) = L_total × sin(heel_angle + angle_of_attack)
  L_vertical (Lifting-Effekt) = L_total × cos(heel_angle + angle_of_attack)

Konsequenz:
  - Flacheres Profil (geringere Wölbung) = konsistenteres Verhalten bei Heel
  - Tiefes Profil = größere Moment-Schwankung, aber mehr Auftrieb
```

**Praktische Auswirkung:**

```
Beispiel: 14m Segelkutter, Ruderprofil NACA 63a618

Heel 0°, Fahrt 7 kn:
  Anstellwinkel: 3° (leicht Ausschlag)
  Ruder-Auftrieb: 5,2 kN horizontal
  Drehmoment: 5,2 × 6m = 31 kN·m (Heck-Drehung)

Heel 25° (Dünung, harter Wind):
  Anstellwinkel: 3° (Steuermann versucht gleich zu halten)
  Aber: Ruder neigt mit, effektiver Anstellwinkel ≈ 3° − 6° (relativ Boot) = -3°!
  Ruder-Auftrieb: nur 2,8 kN (reduziert, sogar rückwärts)
  Drehmoment: 2,8 × 6m = 17 kN·m (nur 55% des aufrechten Falls)
  
Resultat:
  Steuermann muss 2–3× mehr Ausschlag geben (10–12° statt 3°)
  → Höherer Widerstand
  → Geschwindigkeit verloren
```

### 2.3 Cavitation und Hochgeschwindigkeits-Effekte

**Cavitation-Physik:**

```
Druck an Ruder-Oberfläche kann negativ werden (relativ Wasserdruck)
Wenn Druck < Dampfdruck von Wasser (~2,3 kPa @ 20°C):
  → Wasser verdampft lokal
  → Bläschen implodieren
  → Oberflächenerosion

Cavitation-Index (σ):
σ = (P_0 − P_v) / (0.5 × ρ × v²)
σ_critical ≈ 0,5–0,8 (abhängig Profil)

Wenn σ < σ_critical: Cavitation tritt auf

Beispiel: Motorboot, Geschwindigkeit 20 kn (10,3 m/s):
  P_0 = atmosphäre + Tiefe (≈100 kPa)
  P_v ≈ 2,3 kPa
  0.5 × ρ × v² = 0.5 × 1025 × 10,3² ≈ 54,4 kPa
  σ = (100 − 2,3) / 54,4 ≈ 1,8
  
  σ > σ_critical → kein Cavitation (OK)
  
  Aber: Bei 25 kn (12,9 m/s):
  0.5 × ρ × v² = 85,4 kPa
  σ = 97,7 / 85,4 ≈ 1,1
  σ ≈ σ_critical → Cavitation droht!
```

**Cavitation-Vermeidung:**

1. **Profil-Wahl:** dickere Profile (20%+) haben höhere σ_critical
2. **Tieferlage:** Rudder tiefer im Wasser → Druck erhöht
3. **Position:** Entfernung von Propeller (Sog-Effekt)
4. **Belüftungs-Öffnung:** kleine Bohrung am Ruderkopf (breitet Betriebsfenster)

---

## 3. Torque-Berechnung und Lenksystem-Dimensionierung

### 3.1 Statischer Torque (ohne Dynamik)

**Standardformel (Hydrodynamische Kraft):**

> ⚠️ **ZU PRÜFEN (Audit):** Die Rechenbeispiele stimmen nicht mit der angegebenen Formel überein: 0,5 × 1025 × 3,09² × 0,35 × 1,8 ≈ 3083 N (nicht 1034 N) und 0,5 × 1025 × 7,72² × 0,35 × 2,0 ≈ 21381 N (nicht 6480 N); die daraus abgeleiteten Torque-Werte (517 bzw. 3240 N·m) und Lenkkräfte sind entsprechend falsch. Außerdem ist der Hebelarm fragwürdig: Das Schaft-/Lenkmoment um die vertikale Schaftachse hängt vom Abstand Schaft→Druckpunkt in Profilsehnen-Richtung ab (Bruchteil der Chord, vgl. ISO 12215-8), nicht vom halben Ruder-Tiefgang — Letzterer betrifft das Biegemoment M. Auslegung bitte nach ISO 12215-8 (Ruderkraft, Schaftmoment T, Biegemoment M) verifizieren. **Verifiziert (Web, 2026-07 — ISO 12215-8 + klassische Ruderdrehmoment-Beziehung T ∝ A·c_p·v²·sin θ):** Die Ruderkraft greift ≈ 0,30·c hinter der Profilnase an; der Hebelarm für das Schaftmoment ist r = (0,30·c − Schaftposition entlang der Sehne), das Biegemoment M nutzt die Spannweite. Ein belastbarer Torque-Wert ist hier NICHT angebbar, weil die Schaft-/Balance-Position (und damit r) im Beispiel fehlt — daher Markierung statt Korrektur. Zahlen bis zur Klärung unverändert.

```
F_rudder [N] = 0.5 × ρ × v² × A_rudder × C_f

C_f = Profil-abhängiger Koeffizient (1,5–2,5 bei Anstellwinkel 20–35°)
  Typische Werte:
    NACA 63a618 @ 30°: C_f ≈ 1,8
    NACA 0012 @ 30°: C_f ≈ 1,9
    Custom Laminar @ 30°: C_f ≈ 1,65

Torque [N·m] = F_rudder × Hebelarm_vom_Drehpunkt

Hebelarm = distance vom Drehpunkt bis zur Kraft-Wirkung
  Typisch: Ruder-Tiefgang / 2 (Auftrieb wirkt am Druckmittelpunkt, ≈ 40–50% Tiefe)

Beispiel: Segelboot 10m, Spade 0,35 m², Anstellwinkel 30°:
v = 6 kn = 3,09 m/s
F = 0.5 × 1025 × 3,09² × 0,35 × 1,8 = 1034 N
Hebelarm = 1,0m (Ruder-Tiefgang) / 2 = 0,5m
Torque = 1034 × 0,5 = 517 N·m ≈ 0,5 kN·m
Lenkrad-Durchmesser 600 mm → Kraft = 1,7 N (sehr leicht!)

Aber bei 15 kn (7,72 m/s):
F = 0.5 × 1025 × 7,72² × 0,35 × 2,0 = 6480 N
Torque = 6480 × 0,5 = 3240 N·m ≈ 3,2 kN·m
Kraft = 10,8 N (immer noch OK, aber spürbar)
```

### 3.2 Dynamische Torque (Impuls-Lasten)

**Seegang-induzierte Ruderkräfte:**

```
Scenario: Kabbelige See, Boot schlägt über Wellenkamm
  Wellen-Periode: 8 Sekunden
  Pitch-Amplitude: 5° (Boot nickt um Längsmittelachse)
  Auswirkung: Ruderteil taucht/taucht auf
  
Drucksprung beim Eintauchen:
  Δv ≈ sqrt(2 × g × wave_height) = sqrt(2 × 9,81 × 2) ≈ 6,3 m/s (für 2m Welle)
  → Geschwindigkeit-Anstoß unabhängig von Schiff-Geschwindigkeit
  
Impact-Torque (konservativ 150% der Steady-State):
  Torque_dynamic ≈ 1,5 × Torque_steady_state
```

**Lenksystem-Anforderung:**
```
Wenn Motorboot 20 kn fährt, Torque ≈ 3 kN·m steady
Dann in Seegang: Torque_peak ≈ 4,5 kN·m

Servo-Motor Auslegung: min. 1,5x Faktor
→ Servo muss 6–7 kN·m Dauermoment liefern
```

### 3.3 Lenkgetriebe-Übersetzungen

**Mechanische Systeme (Segelboot):**

| Lenkrad-Ø [mm] | Übersetzung | Ideal-Torque [N·m] | Anwendung |
|----------------|-------------|------------------|-----------|
| 300–400 | 20–30 | 100–200 | Kleine Daysailer |
| 500–600 | 35–50 | 200–400 | Standard Cruiser 10–14m |
| 700–800 | 50–70 | 400–600 | Große Cruiser 16–20m |
| 900+ | 70–100 | 600–1000 | Mega-Yachten 25m+ |

**Hydraulische Systeme (Motorboot, große Segler):**

```
Servo-Motor: Electric oder Pump-gesteuert
Druck: 150–210 bar
Zylinder-Ø: 32–50 mm (je nach Torque-Anforderung)

Vorteile:
  - Unbegrenzte Übersetzung
  - Kraft-Verstärkung ideal
  - Autopilot Integration

Nachteile:
  - Fehlerhafte Abdichtung → Ölverlust
  - Elektrik-Abhängigkeit (kein Notfall-Ausweich)
```

---

## 4. Ruderkonstruktion und Laminat-Aufbau

### 4.1 Ganzlaminate (Solid Laminate)

**Klassische Bauweise für Segelboot-Ruder:**

```
Laminate-Schichtfolge (von außen nach innen):
1. Gelcoat 0,5–0,8 mm (UV-Schutz, optisch)
2. CSM 300 g/m² → 1,5 mm (Haftvermögen)
3. Woven 400 g/m² → 2,0 mm (Haupt-Festigkeit)
4. CSM 300 g/m² → 1,5 mm
5. Woven 400 g/m² → 2,0 mm (Symmetrie)
6. CSM 300 g/m² → 1,5 mm
7. Finale Oberflächenschicht: Woven oder CSM

Gesamt-Dicke: 10–15 mm (abhängig Boot-Größe)
Gewicht: 8–12 kg/m² × Ruderfläche

Festigkeit:
  Druck/Zug: 350–450 MPa (Haupt-Richtung)
  Schub: 60–80 MPa (gering, aber OK für Ruder)
```

**Material-Auswahl:**

- **Harz:** Epoxy (besser) vs. Polyester (kostengünstiger)
- **Faser:** Glas (Standard) vs. Kevlar (leichter, teurer, Racing only)
- **Faser-Gewichte:** 300–450 g/m² Standard

### 4.2 Sandwich-Konstruktion (Kern + Laminate)

**Leichte Alternative für große Ruder (>0,5 m²):**

```
Aufbau:
  Außen-Laminate: 5 Schichten (oben beschrieben) = 8 mm
  Kern: PVC-Schaum (H-100 oder H-200, 20–30 mm)
  Innen-Laminate: 5 Schichten (Mirror) = 8 mm

Gesamt-Dicke: 45–50 mm
Gewicht: 12–15 kg/m² (vs. 20–25 kg/m² Ganzlaminate)

Vorteil: 40% Gewichtseinsparung
Nachteil: Komplexere Fertigung, Kern-Crush-Risiko

Kern-Material Auswahl:
  H-100: 100 kg/m³, weich, für normale Lasten
  H-200: 200 kg/m³, steif, für Performance-Boote
  Balsa: 140 kg/m³, traditionell, aber Feuchte-anfällig
```

### 4.3 Hohlraum-Vermeidung und Qualitätskontrolle

**Fertigungsfehler — häufig bei Rudern:**

```
Fehler 1: Harz-Luft-Blasen in Kern-Material
  Ursache: Kern nicht vakuumiert vor Lamination
  Folge: Kern-Delaminierung nach 2–3 Jahren
  Prävention: Kern + Harz-benetzte Matte 24h vor Montage lagern

Fehler 2: Unzureichendes Harz-Impregnieren der Kern-Oberfläche
  Ursache: Schnelle Herstellung ohne Druck
  Folge: Stein-Schlag (Impact) führt zu Kern-Bruch
  Prävention: Vakuum-Bag-Verfahren verwenden (teurer, aber besser)

Fehler 3: Inverse Faser-Orientierung
  Ursache: Während Wicklung Faser-Richung falsch herum
  Folge: Ruder bricht bei Drehen (Querbelastung)
  Prävention: Ply-by-Ply Dokumentation + Markierungen

Qualitätskontrolle:
  ☐ Visuell: keine sichtbaren Blasen, glatte Oberfläche
  ☐ Ultraschall: Kerng-Dicke, Delaminierungs-Detektion
  ☐ Klopftest: Hohlraum-Lokalisierung (dumpfer Sound = Hohlraum)
  ☐ Röntgen (optional): innere Struktur prüfen
```

---

## 5. Ruderkopf-Flange und Abdichtungs-Systeme

### 5.1 Abdichtungs-Anforderungen

**Kritische Kontaktfläche: Ruderkopf-Hull-Interface**

```
Problem: Wasser-Eindringung zwischen Ruderkopf und Hull
  → Feuchtigkeit ins Laminat
  → Delaminierung
  → Ermüdungs-Risse um Befestigungslöcher

Lösung: Mehrschichtige Dichtung
```

### 5.2 Abdichtungs-Detail (Best Practice)

```
1. Ruderkopf-Flansch-Material:
   Edelstahl 316L oder Aluminum 6061-T6 (anodisiert)
   Dicke: 8–10 mm (Rigidität, minimale Verformung)

2. Durchführungs-Abdichtung:
   Primär: EPDM-Gummi-Ring (3–5 mm Dicke) um Schaftdurchmesser
   Sekundär: Epoxy-Dichtmasse rund um Flansch-Oberseite
   Tertär: Polyurethan-Top-Coat auf gesamten Kopf (UV-Schutz)

3. Befestigungslöcher:
   Bolzen: Stainless 316L (M8–M10, abhängig Spannweite)
   Gegenmutter + Feder-Unterlegscheibe (verhindert Lockerung)
   Anaerobes Dicht-Mittel (Loctite 243) auf Gewinde
   Drehmoment: 20–30 N·m (leicht vorgespannt)

4. Laminat-Vorbereitung:
   Oberflächenrauhheit: Ra 20 µm (mit Schleifpapier 80er Körnung)
   Feuchtigkeit: <2% (Feuchtemesser prüfen, mindestens 24h trocknen)
   
5. Abdichtungsprozess:
   Primer-Schicht auf Hull + Flansch-Unterseite (haftet besser)
   Flexible Epoxy-Paste auftragen (Flexibilität beim Schwingen)
   Flansch positionieren, Bolzen Finger-tight
   Bolzen überkreuz spannen (Stern-Muster, 50% → 75% → 100%)
   24h Aushärten vor Wasserkontakt
```

### 5.3 Typische Flansch-Geometrie

```
Für Spade-Ruder (frei stehend):
  Flansch-Außendurchmesser: 250–350 mm (je nach Schaftgröße)
  Bolzenloch-Anzahl: 6–8 (Verteilung um Kreis)
  Bolzenloch-Durchmesser: M8 (Ø 8,5 mm)
  Loch-Abstände vom Schaft-Zentrum: 100–150 mm
  Flansch-Dicke: 8–10 mm (ausreichend Gewindetiefe für M8)
```

---

## 6. Pintle/Gudgeon Lager-Systeme

### 6.1 Konventionelles Pintle-Gudgeon (Bolzen/Auge)

**Bauform (Skeg-hung Ruder typisch):**

```
Gudgeon (Auge, am Skeg/Hull angeschraubt):
  - Geschmiedeter oder gegossener Edelstahl-Block
  - Durchgangs-Bohrung (Pintle-Ø)
  - Flansch für Verschraubung an Struktur
  - 2–3 Gudgeons über Ruderhöhe verteilt (Oberkante, Mitte, Unterkante)

Pintle (Bolzen, am Ruderkopf angeschweißt):
  - Edelstahl-Bolzen (Ø 12–16 mm, für Skeg-Ruder typisch)
  - Schweißverbindung zum Ruderkopf
  - Kopf/Bund oben (Belastung nach oben)
  - Unteren Spitze scharf (fixiert Ruder axial)

Spielraum:
  Radial-Spiel: 0,2–0,5 mm (Reibung, aber nicht zu locker)
  Axial-Spiel: 5–10 mm (Ruder kann hoch/runter wandern, ±5 mm akzeptabel)

Lagerung:
  Kupfer-Buchsen oder Kunststoff-Gleitlager (Polyoxymethylen/Delrin)
  Regelmäßige Schmierung erforderlich (alle 12 Monate)
```

**Verschleiß und Wartung:**

```
Typischer Verschleiß nach 15 Jahren:
  Radiales Spiel: von 0,3 mm → 1,2 mm (4x)
  Folge: Ruder-Flattern (Vibrationen), schlechtere Kontrolle

Wartungsintervall:
  Jährlich: Visuelle Prüfung auf Verschleiß-Spiel
  Alle 3–5 Jahre: Gleitlager + Buchsen kontrollieren
  Nach großem Grounding oder Kollision: sofort prüfen

Austausch-Kosten:
  Ersatz Gleitlager: EUR 200–400 pro Gudgeon
  Arbeit: 4–6 Stunden
  Gesamt: EUR 800–1500 für komplettes Überhaul
```

### 6.2 Moderne Ball-Lager-Systeme (Racing/Premium)

**Vorteile:**
- Reibungsarm (Rotation smooth)
- Weniger Wartung (versiegelt)
- Langlebig (50000+ Zyklen)

**Nachteil:**
- Kosten (EUR 1500–3000)
- Nicht reparierbar (nur austauschbar)
- Anfällig für Salzwasser (Dichtung-Qualität kritisch)

---

## 7. Notfall-Ruder-Verhalten und Failsafe-Design

### 7.1 Hydraulik-Ausfall-Szenario (Power-Boat)

**Situation: Servo-Motor ausfallend, kein Handrad vorhanden**

```
Großmotor-Yacht, Hydraulik-Lenkung, kein mechanischer Backup:
  Problem: Propeller dreht, Boot fährt geradeaus, Ruder kann nicht bewegt werden
  Folge: Notwendig externe Hilfe oder Seeanker

Mitigation:
  1. Notfall-Handrad (tragbar, montierbar auf Ruder-Schaft)
     Kosten: EUR 3000–5000
     Montage-Zeit: 30–45 Minuten
  
  2. Elektro-Motor Backup (kleine Einheit, 12V DC)
     Kosten: EUR 2000–3500
     Leistung: 20–30% des Hauptsystems
     Batterie-Betrieb: 30–60 Minuten
  
  3. Seeanker + Funk-Verbindung zu Rettungsbooten
     Sichere Option, aber Zeitaufwand
```

### 7.2 Ruderbeschädigung im Betrieb

**Szenario A: Ruder trifft U-Boot-Kabel / Ankerkette**

```
Symptome:
  - Plötzlicher Widerstand beim Lenken
  - Öltemperatur Servo ansteigend (Pumpe unter Last)
  - Ggf. Knack-Geräusch (Ruder-Bruch)

Diagnose:
  - Visuell Ruder-Oberfläche kontrollieren (Kratzer, Dellen)
  - Ulraschall-Prüfung: Delaminierung?
  - Manöver-Test in flachem Wasser (Wendigkeit erhalten?)

Reparatur (provisorisch):
  - Wenn nur oberflächlich: weiterfahren, später reparieren
  - Wenn Delaminierung > 5 cm: Notfall-Hebel-Reparatur anbringen (Gurt um Ruder)
```

**Szenario B: Ruderstange bricht (mechanische Lenkung)**

```
Abhilfewege:
  1. Ersatz-Stange (wenige Segler führen mit)
  2. Improvisation: Boot um Segel-Trimm steuern
  3. Seeanker werfen, Signal geben
```

### 7.3 Flattern und Vibrationen (High-Speed)

**Flattern-Physik:**

```
Ruderblattes hat Eigenfrequenzen (z.B. 8 Hz, 15 Hz, ...)
Wenn Strömungs-induzierte Vortex-Frequenz = Eigenfrequenz:
  → Resonanz-Flattern
  → Vibrationen (spürbar im Lenkrad)
  → Delaminierungs-Risiko nach längerer Fahrt

Auslöser:
  Höhe Geschwindigkeit (>20 kn)
  Ungleichmäßige Strömung (Propeller-Blasstrom direkt)
  Schlechte Ruderlager-Qualität (Spiel zu groß)

Vermeidung:
  1. Lager regelmäßig warten (Spiel nicht >0,5 mm)
  2. Ruder-Laminat hinreichend steif (Dicke überprüfen)
  3. Propeller >0,5m entfernt vom Ruder (Strömungs-Stabilisierung)
```

---

## 8. Fertigungs-Toleranzen und Qualitätskontrolle

### 8.1 Kritische Abmessungen

| Element | Nominal | Toleranz | Prüfung |
|---------|---------|----------|---------|
| Ruder-Dicke (Chord) | 400 mm | ±5 mm | Messstab, 5 Punkte |
| Ruder-Tiefgang | 1200 mm | ±10 mm | Messstab, Wasserwaage |
| Profil-Rauhheit | Ra 20 µm | ±10 µm | Oberflächenrauhheitsprüfer |
| Flansch-Ebenheit | Referenz | ±1 mm | Stahllineal + Schublehre |
| Schaft-Konzentrität | ideal | ±1,5 mm | Umlauf-Messer |
| Laminat-Dicke (uniform) | 12 mm | ±1,5 mm | Ultraschall, 20-Punkt Raster |

### 8.2 Inspektions-Checkliste vor Übergabe

```
Visuelle Kontrolle:
  ☐ Keine sichtbaren Kratzer / Dellen (oberflächlich OK, Tiefe < 2 mm)
  ☐ Gelcoat: gleichmäßige Farbe, keine Kratzer/Blasen
  ☐ Flansch-Oberseite: flach, kein Verziehen
  ☐ Laminat-Schichtlinien sichtbar (gutes Zeichen, harte Aushärtung)

Dimensionelle Prüfung:
  ☐ Ruder-Tiefgang ±10 mm
  ☐ Profil-Dicke (Chord) ±5 mm
  ☐ Flansch-Bolzenlöcher korrekt positioniert (±2 mm)
  ☐ Schaft-Konzentrität ±1,5 mm (Laufruhe)

Zerstörungsfreie Prüfung:
  ☐ Ultraschall: Laminat-Dicke (±1,5 mm), keine Hohlräume
  ☐ Klopftest: komplettes Ruder abklopfen (dumpf = OK, hohl = Problem)
  ☐ (Optional) Thermographie: Hohlräume sichtbar machen

Belastungstest (Premium-Ruder):
  ☐ Statischer Biegetest: 0,5 × max. Betriebslast, halten 5 Minuten
  ☐ Nach Test: Risse? Oberflächenabdrücke?
```

---

## 9. Lagern und Transport

### 9.1 Lagerung-Richtlinien

```
Horizontale Lagerung:
  - Ruder flach auf 2–3 Unterlagen (alle 1 m)
  - Keine Belastung auf Flansch (Verbiegung!)
  - Trockener, 15–25°C Ort
  - Schutz vor UV (Plane oder Abdeckung)

Vertikale Lagerung (weniger empfohlen):
  - In Gestell, Schaft hängend (kein Druck auf Flansch)
  - Nicht länger als 3 Monate so lagern (Verformung-Risiko)

Feuchte-Schutz:
  - Nicht in feuchter Garage lagern
  - Silica-Gel Pakete in Karton (Feuchtigkeit absorbieren)
  - Regelmäßig lüften
```

### 9.2 Transport-Richtlinien

```
Im Auto/LKW:
  - Ruder waagerecht, gesichert mit Spanngurt
  - Flansch-Oberseite nach oben (Druck-Entlastung)
  - Rollen-Schutz unter Schaft (Kratzer vermeiden)

Mit Flugzeug/Schiff:
  - Robuste Holz-Kiste mit Dämmerung
  - Gewicht/Größe angeben (Versand-Kalkulation)
  - Versicherung empfohlen (EUR 1000–2000 Wert)
```

---

## 10. Wartung und Inspektions-Intervalle

### 10.1 Jährliche Kontrollen

```
Vor der Saison:
  ☐ Visuell: Kratzer, Risse, Farbveränderungen
  ☐ Flansch-Bolzen prüfen (lose? mit Schlüssel anziehen, 15–20 N·m)
  ☐ Pintle/Gudgeon-Lager: Spiel prüfen (Ruder mit Hand wackeln, max 0,5 mm)
  ☐ Gleitlager-Schmierung überprüfen (ggf. leichte Mengen Öl auftragen)
  ☐ Abdichtungs-Gummi-Ring: Risse, Verschleiß?

Nach der Saison:
  ☐ Süßwasser-Durchspülung (bei Salzwasser-Betrieb)
  ☐ Trocknung der Lager (um Korrosion zu minimieren)
  ☐ Reinigung + leichte Polierung der Gelcoat-Oberfläche
```

### 10.2 Inspektionen im 5-Jahre-Turnus

```
Alle 5 Jahre oder nach Grounding:
  ☐ Ultraschall-Prüfung (Delaminierung?)
  ☐ Laminat-Dickenmessung (Erosion/Korrosion?)
  ☐ Bolzen-Korrosions-Check (Kupferbelag bei Galvanic Pairs?)
  ☐ Eventuell: Gleitlager-Austausch (prophylaktisch bei Verschleiß)
```

### 10.3 Reparatur nach Beschädigung

**Stufe 1: Oberflächlliche Kratzer/kleine Dellen**

```
Schritte:
1. Kratzer schleifen (80er Körnung, dann 220er)
2. Epoxy-Paste + Quarzfüller auftragen
3. Nach Aushärtung: schleifen (Ra 20 µm)
4. Gelcoat-Finish auftragen (Spray oder Hand-Pinsel)

Kosten: EUR 200–500
Dauer: 1–2 Tage
```

**Stufe 2: Delaminierung / Kern-Bruch**

```
Schritte:
1. Beschädigte Laminat-Fläche ausschneiden (U-Form, Min. 50 mm über Schaden)
2. Kern nachfüllen (Epoxy-Paste oder PVC-Schaumstreifen)
3. Neue Lagen Laminat wickeln (3–4 Schichten, Faser-Orientierung beachten)
4. Oberflächen-Finish (wie oben)

Kosten: EUR 800–2000
Dauer: 3–5 Tage
```

**Stufe 3: Struktureller Bruch (Risse im Schaft, Flansch-Verformung)**

```
Erfordert Reparaturwerft / vollständiger Austausch
Kosten: EUR 3000–6000 (Austausch neues Ruder)
Dauer: 2–4 Wochen (ggf. Wartezeit auf Provisorisches)
```

---

## ANHANG A — Glossar

**Anstellwinkel:** Winkel zwischen Ruderprofil und Strömungsrichtung.

**Auftrieb:** Kraft senkrecht zur Strömung, erzeugt Drehmoment.

**Balanced Rudder:** Ruder mit Teil der Fläche vor dem Drehpunkt (reduziert Torque).

**Cavitation:** Dampfblasen-Bildung durch lokalen Druckabfall.

**Druckpunkt:** Ort der Auftriebswirkung auf dem Profil (typisch 30–50% Chord).

**Eigenfrequenz:** Natürliche Vibrationsfrequenz einer Struktur.

**Flansch:** Befestigungs-Platte am Ruderkopf für Anbringung am Hull.

**Flattern:** Resonanz-Vibrationen durch Strömungs-induzierte Vortex.

**Gleitzahl (L/D):** Auftrieb geteilt Widerstand (Effizienzmaß).

**Gudgeon:** Edelstahl-Auge für Pintle (Lager-Element).

**Laminat:** Geschichtete Struktur aus Fasern + Harz.

**NACA-Profil:** Systematische Profilbezeichnung.

**Pintle:** Edelstahl-Bolzen für Gudgeon-Drehpunkt.

**Profil-Dicke:** Maximale Vertikalabstand Saug- und Druckseite.

**Ruderfläche:** Gesamte Projektions-Fläche in Seitenansicht.

**Spade Rudder:** Freistehende Flosse (kein Skeg).

**Torque:** Drehmoment (Kraft × Hebelarm), erforderlich zum Lenken.

**Transom-hung:** An Heck-Spant befestigt.

**Wölbung:** Krümmung des Profils (camber).

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class RuderDesignFehlerbild(BaseModel):
    """
    Fehlerbild für Ruder-Design nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_09_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Ruder_Design"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Boot/Betrieb")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-relevanz")
    
    # Ursprung
    boots_typen: List[str] = Field(default_factory=list, description="Relevante Boot-Klassen")
    ruder_bauarten: List[str] = Field(default_factory=list, description="Betroffene Ruder-Typen")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Wartungs-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO, DNV, ABS")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = RuderDesignFehlerbild(
    fehlerbild_id="31_09_001",
    titel="Ruder-Torque zu hoch für manuelle Lenkung",
    beschreibung="Profil-Auswahl oder Fläche führt zu übermäßiger Steuerkraft.",
    symptome=[
        "Extreme Lenkrad-Kraft erforderlich (>10 N @ 15 kn)",
        "Ermüdung beim Langfahrt-Steuern",
        "Ggf. Servo-Motor-Überlast"
    ],
    auswirkungen=[
        "Reduzierte Manövrierbarkeit (Steuermann ermüdet)",
        "Notfall-Handling schwieriger",
        "Servo-System Überlast-Risiko"
    ],
    schweregrad="mittel",
    sicherheits_impact=True,
    boots_typen=["Segelboot", "Motorsegler"],
    ruder_bauarten=["Spade", "Balanced"],
    diagnose_methoden=[
        "Dynamometer-Test: Torque bei verschiedenen Geschwindigkeiten",
        "Vergleich zu ähnlichen Booten",
        "CFD-Analyse der Profilform"
    ],
    reparatur_optionen=[
        "Profil-Optimierung (Custom Laminar)",
        "Servo-Motor nachrüsten",
        "Lenkgetriebe-Übersetzung erhöhen"
    ],
    schaetzung_kosten_eur=5000,
    dauer_tage=10,
    praevention=[
        "Dimensionierung nach Ruder-Fläche-Standard prüfen",
        "CFD-Analyse für Profil-Wahl",
        "Prototyp-Test vor Serie"
    ],
    inspektions_intervall_jahre=2,
    normen_referenzen=["ISO 12217-3", "DNV GL Rules"],
    verwandte_fehlerbilder=["31_09_002", "31_09_005"]
)
```

---

## ANHANG C — FAQ (25+)

**F1: Was ist der Unterschied zwischen Spade und Skeg-hung Ruder?**
A: Spade: frei stehend, maximale Wendigkeit, höhere Torque. Skeg-hung: unterstützt vom Skeg, robuster, geringerer Torque, traditionell.

**F2: Wann ist ein Balanced Rudder sinnvoll?**
A: Bei Hochgeschwindigkeits-Motorbooten (>20 kn) oder sehr großen Segel-Yachten (>25m), wo Torque ein Problem ist.

**F3: Kann man ein Ruder während der Saison reparieren?**
A: Oberflächliche Kratzer: ja (1–2 Tage). Delaminierung: provisorisch (Boot kann fahren), dauerhafte Reparatur nach Saison.

**F4: Welcher NACA-Profil ist am besten?**
A: Für Cruiser: NACA 63a618 (Standard, robust). Für Racing: Custom Laminar. Symmetrisch (0012) nur für spezielle Hochleistung.

**F5: Wie oft muss das Ruder-Lager geschmiert werden?**
A: Alle 6–12 Monate (1–2× pro Saison). Bei intensivem Gebrauch (Chartern) öfter prüfen.

**F6: Was kostet ein neues Ruder?**
A: Segelboot 10–14m: EUR 2000–4000. Motorsegler 16–20m: EUR 4000–7000. Racing-Boot: EUR 6000–12000.

**F7: Kann Salzwasser das Ruder schneller verschleißen?**
A: Ja. Lager-Korrosion schneller (3–5 Jahre vs. 5–10 Jahre Süßwasser). Gleitlager-Austausch notwendiger.

**F8: Ist ein Balsa-Kern besser als PVC-Schaum?**
A: Traditionell ja (stabiler, leichter), aber Salzwasser-anfällig. Moderner Standard: PVC (H-200), wartungsfreier.

**F9: Kann man ein Ruder von einem anderen Boot verwenden?**
A: Nur wenn Dimensionen + Torque-Anforderung passen. Unterschiedliche Lager/Flansch-Systeme = kompliziert.

**F10: Was ist ein normales Ruder-Lager-Spiel?**
A: Radial 0,2–0,5 mm (neu), bis 1,5 mm akzeptabel. Wenn >2 mm: Verschleiß-Austausch.

**F11: Warum flutter mein Ruder bei Hochfahrt?**
A: Resonanz-Effekt. Lager-Spiel zu groß? Ruder-Laminate nicht steif genug? Propeller-Blasstrom? Prüfen!

**F12: Ist Cavitation beim Ruder ein großes Problem?**
A: Selten bei normalen Booten (<20 kn). Bei >25 kn Motorbooten: ja. Prävention: tiefere Position, dickeres Profil.

---

## ANHANG D — Fertigungs-Kosten-Übersicht (2026)

| Leistung | Kleine Segler 8–10m | Cruiser 12–16m | Rennboot 12–18m |
|----------|-----------------|------------|------------|
| Ganzlaminate Ruder | EUR 1500–2500 | EUR 2500–4000 | EUR 3500–6000 |
| Sandwich-Ruder | EUR 2000–3500 | EUR 3500–5500 | EUR 5000–8000 |
| Flansch + Bolzen | EUR 300–500 | EUR 500–800 | EUR 800–1200 |
| Lager-System (Pintle/Gudgeon) | EUR 200–400 | EUR 400–600 | EUR 600–1000 |
| Inspektions-Paket (UT+Visuell) | EUR 300–600 | EUR 600–1000 | EUR 800–1300 |
| Reparatur (Kratzer-Reparatur) | EUR 200–400 | EUR 400–700 | EUR 600–1000 |
| Reparatur (Delaminierung) | EUR 600–1500 | EUR 1200–2500 | EUR 1800–3500 |

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-05-18  
**Gültig für:** Segelboote, Motorsegler, Motorboote 8–40m LOA
