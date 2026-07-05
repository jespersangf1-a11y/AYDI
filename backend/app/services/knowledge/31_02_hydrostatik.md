# Kat 31.02 — Hydrostatik

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Hydrostatik  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Fundamentale Konzepte

Hydrostatik beschreibt die Kräfte von Wasser auf einen stillhaltenden oder quasistationären Rumpf. Sie ist Grundlage für:
- **Auftrieb (Buoyancy):** Vertikale Kraft durch Wasserverdrängung
- **Trimm (Trim):** Längiges Gleichgewicht
- **Stabilität (Stability):** Rückstellmoment bei Neigung
- **Freiwasser-Effekt:** Oberflächenspannung in Tanks

### 1.1 Archimedes Prinzip

```
Auftrieb = ρ_Wasser × g × Verdrängungsvolumen
F_B = ρ × g × ∇
```

Bei Gleichgewicht:
```
Gewicht = Auftrieb
m_gesamt × g = ρ_Wasser × g × ∇

Verdrängung ∇ = m_gesamt / ρ_Wasser
```

**Typische Wasserdichten:**
- Süßwasser: ρ = 1000 kg/m³
- Salzwasser (Atlantik): ρ = 1025 kg/m³
- Mittelmeer: ρ = 1023 kg/m³

---

## 2. Hydrostatische Stabilitäts-Kurven

### 2.1 Definition: GZ und Righting Moment

Bei Rumpf geneigt um Heel-Winkel θ:

```
GZ (θ) = Righting Moment Arm (m)
      = (Longitudinal distance between CG and Center of Buoyancy)
```

**Visuelle Interpretation:**
```
G = Center of Gravity (Schwerpunkt)
B = Center of Buoyancy (Auftriebsmittelpunkt)
M = Metacenter (Krümmungsmittelpunkt Wasserlinie)

Stabilitäts_Hebelarm GZ = GM × sin(θ)  [für kleine θ]
                        = (BM − BG) × sin(θ)

BM (Metacentric Radius) = I / ∇
  wobei I = zweites Moment der Wasserlinie um Längsmittellinie
```

**Stabilitäts-Klassifikation:**
- **Positiv stabil:** GZ > 0 für alle θ < 180° (Schiff kehrt auf Kurs zurück)
- **Neutral:** GZ = 0 (kritischer Punkt, Schiff bleibt geneigt)
- **Negativ stabil:** GZ < 0 (Schiff kippt um)

### 2.2 Kritische Stabilitäts-Parameter

**Initiale Stabilität (θ ≈ 0):**
```
GM = BM − BG  (Metacentric Height)
dGZ/dθ|_{θ=0} = GM
```

- GM > 0: Schiff ist initial stabil
- GM > 1.0m: Gute Stabilität (Cruiser-Standard)
- GM > 1.5m: Sehr steif (Racing-Standard, unbequem)
- GM < 0.5m: Kritisch (Bordpfeiler-Risiko)

**GZ-Maximum (Angle of Maximum Stability):**
```
θ_GZ_max = θ wo d(GZ)/dθ = 0
```

Normales Bereich: 25–40° (abhängig Boot-Klasse)

**Righting Moment (Dynamisch):**
```
RM(θ) = Schiffsgewicht × GZ(θ) × g
      = m × g × GZ(θ)  (N·m oder kN·m)
```

Integrierte Stabilität:
```
RA(θ_1 bis θ_2) = ∫ GZ(θ) dθ  (m·rad)
```

### 2.3 ISO 12217 Stabilitäts-Anforderungen

**Kategorie A (Ozean):**
```
GZ @ 30° ≥ 0.20m
GZ_max ≥ 0.25m
Winkel GZ_max ≥ 25°
RA(0–40°) ≥ 0.090 m·rad
RA(0–GZ_max) ≥ 0.055 m·rad
```

**Kategorie B (Offshore):**
```
GZ @ 30° ≥ 0.15m
GZ_max ≥ 0.20m
Winkel GZ_max ≥ 25°
RA(0–40°) ≥ 0.065 m·rad
RA(0–GZ_max) ≥ 0.040 m·rad
```

**Kategorie C (Inshore):**
```
GZ @ 30° ≥ 0.10m
GZ_max ≥ 0.12m
Winkel GZ_max ≥ 20°
RA(0–40°) ≥ 0.040 m·rad
RA(0–GZ_max) ≥ 0.020 m·rad
```

**Kategorie D (Sheltered):**
```
Keine strengen Anforderungen, aber
GZ @ 30° ≥ 0.05m empfohlen
```

---

## 3. Berechnung Stabilitäts-Kurven (Detailliert)

### 3.1 Hydrostatische Eingabe

Für jeden Heel-Winkel θ:

1. **Neue Wasserlinie ermitteln:** Rumpf wird um Längsmittellinie rotiert
2. **Verdrängungsvolumen ∇(θ) berechnen:** Integration über neue Wasserlinie
3. **Auftrieb-Mittelpunkt B(θ) bestimmen:** Position der integralen Kraft
4. **Schwerpunkt G:** Fixiert relativ zum Rumpf
5. **GZ(θ) berechnen:**
   ```
   GZ(θ) = Abstand von G zur Verticalen durch B
         = (x_B(θ) − x_G) × sin(θ) + (z_B(θ) − z_G) × cos(θ)
   ```

### 3.2 Numerische Methode

**Simpsonregel für Auftriebsberechnung:**

```
∇ = (h/3) × [A_0 + 4×A_1 + 2×A_2 + ... + A_n]

wobei h = Stationsabstand (mm)
      A_i = Spantfläche bei Station i (mm²)
```

**Für GZ-Kurven über Heel-Winkel:**

Typically 91 Heel-Positionen (0° to 180°, Schrittweite 2°)

```python
angles_deg = [0, 2, 4, 6, 8, ..., 178, 180]
gz_values = []

for θ in angles_deg:
    # Wasserlinie neu berechnen
    displ_volume = calculate_displaced_volume(θ)
    cg_new = rotate_cg_by_θ(θ)
    cb_new = calculate_center_of_buoyancy(θ)
    
    # GZ berechnen
    gz = calculate_gz(cb_new, cg_new, θ)
    gz_values.append(gz)
```

---

## 4. Freiwasser-Effekt (Free Surface Effect)

### 4.1 Problemstellung

Flüssig-Tanks (Fuel, Water, Holding Tank) haben freie Oberfläche. Bei Neigung bewegt sich Oberfläche parallel, reduziert effektiven Schwerpunkt.

### 4.2 Mathematik

**Freiwasser-Korrektions-Moment:**
```
ΔGM_FS = − (ρ_Flüssigkeit / ρ_Schiff) × (i / ∇)

wobei i = zweites Moment der freien Oberfläche um Längsmittellinie
      ∇ = Verdrängung (m³)
```

**Praktische Auswirkung:**
```
GM_effektiv = GM_geometrisch − ΔGM_FS
```

### 4.3 Typische Werte für Cruiser

**Fuel Tank (Diesel):**
- Länge: 1.5m, Breite: 0.8m, Tiefe: 0.6m
- i ≈ (1.5 × 0.8³ / 12) = 0.064 m⁴
- ΔGM_FS ≈ −0.010 bis −0.020m

**Water Tank:**
- Länge: 1.0m, Breite: 0.9m
- i ≈ 0.0675 m⁴
- ΔGM_FS ≈ −0.015 bis −0.025m

**Total mehrere Tanks:** ΔGM_FS_total ≈ −0.05 bis −0.10m (bedeutsam!)

### 4.4 Mitigations-Strategien

- **Längliche Tanks:** Reduzieren freie Oberfläche längs Schiffslängsrichtung
- **Unterteilung:** Längsschotte reduzieren i
- **Volle Tanks:** Keine freie Oberfläche bei vollen oder leeren Tanks
- **Passive Netz-Unterteiler:** Absorbieren Sloshing, reduzieren i-Effekt

---

## 5. Trimm (Longitudinal Equilibrium)

### 5.1 Trim-Gleichung

```
Trim_Moment = m_ship × g × (x_CG − x_CB)
            = 0  (bei Gleichgewicht)
```

Praktisch:
```
x_CG_längsmittellinie = x_CB_längsmittellinie
```

Wird nie perfekt erreicht, Abweichung = Trim-Winkel:
```
trim_deg = arctan((x_CG − x_CB) / LWL) × 180/π
```

### 5.2 Trim-Effekt auf Stabilität

**Bug-Trim (Positiv trim):**
- Tiefere Spanten vorne → höheres BM vorne
- GZ-Kurve: leicht erhöht
- Seegang: Pitching kann sich verschärfen

**Heck-Trim (Negativer trim):**
- Tiefere Spanten hinten → höheres BM hinten
- GZ-Kurve: leicht gesenkt
- Problematisch für Segler (Hintergewicht schädlich)

**Praxis-Regel für Cruiser:**
```
Optimal_trim = +0.5° bis +1.0° (Bug etwas tiefer)
```

---

## 6. Auftriebsverteilung und Stabilitäts-Kurven-Verbesserung

### 6.1 Integrated Stability

Zwei Schiffe können gleiche GZ bei 30° haben, aber unterschiedliches Seegang-Verhalten:

```
Schiff A: GZ kontinuierlich fallend, GZ_max @ 35°
Schiff B: GZ plateau, GZ_max @ 45°
```

**Dynamische Stabilität:**
```
RA(Area_Rule) = ∫[0 bis Winkel] GZ(θ) dθ
```

- Schiff A: RA(0–40°) = 0.085 m·rad (knapp ISO 12217)
- Schiff B: RA(0–40°) = 0.110 m·rad (sicherer)

### 6.2 Design-Strategien zur Verbesserung

**Breit-Rumpf Ansatz:**
- Erhöht BM (zweites Moment Wasserlinie)
- GZ bleibt länger positiv
- Nachteil: höherer Widerstand

**Ballast-Vertiefung:**
- Senkt Schwerpunkt (niedrigeres G)
- Erhöht GM
- Nachteil: Trimmung nötig, Kosten

**Zweck-Form:**
- Spitziger Bug (weniger Volumen oben)
- Breiterer Rumpf unten
- GZ-Kurve: steigt schneller, Plateau länger

---

## 7. Fehleranalyse — 12 Fehlermuster

### 7.1 [F7.1] Negatives GM (Initial Instabilität)

**Symptom:**
- GM berechnet: < 0 oder < 0.3m
- Schiff neigt sich spontan, kehrt nicht auf Kurs zurück

**Ursache:**
- Schwerpunkt zu hoch (Ladung falsch gestaut)
- Zu wenig Ballast
- Auftriebsverlust (Lecks, Verschlammung)

**Folge:**
- Kritisch: Kapseln-Risiko
- CE-Zertifizierung Fehler
- Unbewohnbar

**Empfohlene Korrektion:**
```
GM_target = 0.8m minimum für alle Ladesituationen
Ballast überprüfen und ggf. erhöhen
Ladungs-Schwerpunkt optimieren (niedrig/aft)
```

**Prüfkriterium:** GM < 0.5m → FEHLER

---

### 7.2 [F7.2] Zu hohes GM (Sehr steife Bewegung)

**Symptom:**
- GM > 2.0m für Cruiser
- Schiff schwingt schnell hin und her (Roll-Periode <8s)

**Ursache:**
- Übermäßiger Ballast
- Schwerpunkt zu tief
- Naives Design ohne Seakindliness-Analyse

**Folge:**
- Unbequeme Bewegung, höhere Strukturbelastung
- Crew-Ermüdung
- Kann zu Pitch-Resonanz führen (Slamming)

**Empfohlene Korrektion:**
```
GM_optimal = 0.8–1.2m für Cruiser (Komfort)
         = 1.2–1.8m für Racing (Steifheit gewünscht)

Roll_Periode_T = 2π × √(I/K)  (ungefähr T ≈ 0.4 × B [s])
Ziel: T > 8s für Komfort
```

**Prüfkriterium:** GM > 1.8m (außer Racing) → Überprüfung

---

### 7.3 [F7.3] Unrealistische Schwerpunkt-Annahme (CG-Fehler)

**Symptom:**
- CG angenommen in Projektdatei
- Keine detaillierte Gewichts-Aufstellung (Lightship-Gewichte)
- Hydrostatik-Berechnung basiert auf falschem CG

**Ursache:**
- Früher Entwurf: nur geschätztes Leergewicht
- Keine Aktualisierung während Design-Iteration
- Zu flaches Vertrauen in CAD-Modell-Eigenschaften

**Folge:**
- GZ-Kurve völlig falsch
- Stabilität kann zu hoch oder zu niedrig sein
- Test/Ladeprobe offenbart Fehler erst zu spät

**Empfohlene Korrektion:**
```
Detaillierte Gewichtsaufstellung erforderlich:
  − Struktur (Rumpf, Deck, Kajüte): CAD-Masse × Material-Dichte
  − Maschine, Antrieb: Katalog-Daten
  − Möbel, Ausbauten: Wiegungen oder Datenblatt-Schätzung
  − Ausrüstung, Rigg (Segler): Itemisierte Summe
  − Betriebsfluida (Öl, Kühlwasser, Treibstoff): Volume × Dichte

CG_Position muss gemessen oder detailliert berechnet sein
```

**Prüfkriterium:** CG basierend auf <80% detaillierte Gewichte → Überprüfung

---

### 7.4 [F7.4] GZ-Kurve sinkt nach GZ_max (Instabilität bei hohen Winkeln)

**Symptom:**
- GZ steigt bis θ ≈ 35°, dann fallend
- GZ wieder bei 90° < 0.05m
- GZ durchquert Null vor 180°

**Ursache:**
- Zu schmaler Rumpf oben (Auftrieb nach oben bei hohen Winkeln verloren)
- Falsches Ballast-Design
- Freibord oben nicht ausreichend breit

**Folge:**
- Unter Sturm-Bedingung: Schiff kann umkippen (< 120°)
- ISO 12217 Anforderung "GZ > 0 bis 180°" nicht erfüllt
- Kritisch für Category A/B

**Empfohlene Korrektion:**
```
Rumpf-Breite oben vergrößern (Sheer-Kurve beachten)
Ballast senken
Freibord erhöhen
GZ-Kurve über 120° überprüfen und Korrektion iterativ simulieren
```

**Prüfkriterium:** GZ < 0.05m @ 90° oder GZ durchkreuzt Null vor 120° → FEHLER

---

### 7.5 [F7.5] GZ_max bei zu hohem Winkel (>50°)

**Symptom:**
- GZ_max tritt erst bei θ > 50° auf
- GZ zwischen 30–50° steigt sehr langsam

**Ursache:**
- Zu schmaler Rumpf unten (U-förmiges Profil extremes Beispiel)
- Ballast zu hoch positioniert

**Folge:**
- Seegang-Verhalten: Unsicher, Roll-Neigung groß
- ISO 12217 fordert meist GZ_max @ 25–35° (streng bei Cat A)
- Crew-Unbehagen

**Empfohlene Korrektion:**
```
Ziel-Winkel GZ_max: 25–40° (abhängig Klasse)
  Falls > 50°:
  − Ballast senken (CG tiefer)
  − Rumpf unten breiter (höherer BM)
  − Freibord oben kontrollieren (nicht zu breit oben)
```

**Prüfkriterium:** GZ_max @ >50° → Überprüfung

---

### 7.6 [F7.6] Zu schneller GZ-Abfall nach GZ_max

**Symptom:**
- GZ_max @ 32°
- GZ @ 60° < 60% von GZ_max
- Kurve ist spitz (nicht plateau)

**Ursache:**
- Zu breiter Rumpf oben (Auftrieb verloren schnell bei Neigung)
- Ungenügend Freibord

**Folge:**
- Seegang: Schiff fällt leicht in Wellental
- ISO 12217 RA(0–40°) kann Anforderung knapp verfehlen
- Struktur: höhere Biegebeanspruchung durch schnelleres Righting

**Empfohlene Korrektion:**
```
Rumpf-Form optimieren:
  − Schmälerer oben (durchdachtes Sheer)
  − Ballast optimal positionieren
  − Freibord kann moderat erhöht werden
  − GZ sollte plateau-ähnlich sein (nicht zu spitz)
```

**Prüfkriterium:** GZ@60° < 0.4 × GZ_max und GZ_max > 35° → Überprüfung

---

### 7.7 [F7.7] Freiwasser-Effekt nicht berücksichtigt (GM falsch)

**Symptom:**
- GM berechnet: 1.0m (geometrisch)
- Mehrere halb-volle Tanks (Fuel, Water)
- Keine FS-Korrektion angewendet

**Ursache:**
- Designer ignoriert FS-Effekt oder unterschätzt
- Hydrostatik-Software ohne automatische FS-Korrektur

**Folge:**
- Reale GM: ~0.85m (15% Reduktion typisch)
- Stabilität-Überoptimistik
- Test/Ladeprobe später Fehler

**Empfohlene Korrektion:**
```
FS-Korrektionen IMMER eingeben:
  − Alle Tanks aufzählen (Tankanzahl, Abmessungen, Befüllungsgrade)
  − i pro Tank berechnen: i = (Länge × Breite³) / 12
  − ΔGM_FS = −(ρ_Flüssigkeit / ρ_Schiff) × (i_sum / ∇)
  − GM_eff = GM_geo − ΔGM_FS

Ziel: GM_eff > 0.7m unter allen Ladesituationen
```

**Prüfkriterium:** Keine FS-Korrektionen eingegeben → Überprüfung

---

### 7.8 [F7.8] Asymmetrisches Laden (Querstabilität-Fehler)

**Symptom:**
- Ladung ungleich verteilt (z.B. Ballast nur Steuerbord)
- Schiff neigt sich permanent zur einen Seite
- GZ-Analyse zeigt unerwartete Asymmetrie

**Ursache:**
- Mangelhafte Ladungs-Planung
- Asymmetrischer Tank-Aufbau nicht ausgeglichen

**Folge:**
- Permanent Heeling-Winkel (Schiff läuft unter Winkel)
- Sicherheit: unsichtbares Problem, schwer zu diagnostizieren
- Crew-Unbehagen

**Empfohlene Korrektion:**
```
Ladungs-Massenverteilung überprüfen:
  − y_CG sollte auf Längsmittellinie liegen (y = 0)
  − Alle Massen symmetrisch steuern
  − Balance-Tanks prüfen (falls asymmetrisch)
  
Schiff-Test:
  − Still-Wasser Heeling-Winkel messen
  − Falls > 2°: Ladungs-Umverteilung durchführen
```

**Prüfkriterium:** |y_CG| > 100mm (auf LWL bezogen) → Überprüfung

---

### 7.9 [F7.9] Dynamische Stabilität (RA) zu niedrig

**Symptom:**
- GZ-Kurve insgesamt niedrig
- RA(0–40°) berechnet < ISO 12217 Anforderung
- Beispiel: RA = 0.085 m·rad für Cat A (Anforderung 0.090)

**Ursache:**
- Rumpf-Form zu fein (zu wenig Volumen)
- GM zu klein
- Kombination mehrerer Faktoren

**Folge:**
- Unter extremem Seegang: Schiff kann umkippen
- ISO 12217 Zertifizierung scheitert
- Marketing-Problem für Verkauf

**Empfohlene Korrektion:**
```
Mehrere Levers verfügbar:
  1. Rumpf breiter machen (höheres BM)
  2. Ballast senken oder erhöhen (GM optimieren)
  3. Freibord erhöhen (mehr Auftrieb bei hohem Winkel)
  4. Spant-Form optimieren (mehr Volumen Unterschiff)

Iterativ durchrechnen bis RA_result > Anforderung × 1.05
```

**Prüfkriterium:** RA < 1.02 × Anforderung → Überprüfung/Iteration

---

### 7.10 [F7.10] Kapselwinkel zu niedrig (Schiff zu stabil/steif)

**Symptom:**
- GZ wird erst nach >120° negativ
- Schiff würde kapseln bei ~130° Neigung
- Sollte bei ~100–110° negativ werden (sicherer)

**Ursache:**
- Zu viel Ballast, CG zu tief
- Rumpf zu breit oben

**Folge:**
- Zwar stabil, aber unkomfortabel steife Bewegung
- Höhere Strukturbelastung
- Roll-Periode sehr kurz (Unbehagen)

**Empfohlene Korrektion:**
```
Ballast leicht reduzieren oder höher positionieren
Rumpf oben schmäler gestalten (durchdachtes Design)
Ziel: Kapselwinkel 100–120° (Balance)
```

**Prüfkriterium:** Kapselwinkel > 140° → Überprüfung (ggf. Optimierung)

---

### 7.11 [F7.11] Unterschiedliche GZ-Kurven in verschiedenen Ladesituationen (unsystematisch)

**Symptom:**
- GZ-Kurven für verschiedene Ladesituationen kreuzwise
- Unerwartete Variation in GM, GZ_max-Position
- Keine logische Progression (volladen → leer)

**Ursache:**
- Fehler in CG-Berechnung pro Ladesituation
- FS-Effekt ungleichmäßig berücksichtigt
- Hydrostatik-Daten-Fehler

**Folge:**
- Ungewissheit über echte Stabilität
- Ladeplan-Validierung fragwürdig
- Sicherheit unsicher

**Empfohlene Korrektion:**
```
Für jede Ladesituation:
  − CG detailliert neu berechnen (nicht extrapolieren)
  − FS-Effekte neu bewerten (Tankinhalte)
  − Hydrostatik neu laufen lassen
  − GZ-Kurven visualisieren und Trend überprüfen
  
Erwartung: Als Boot schwächer beladen wird,
  − GM steigt (CG sinkt typischerweise)
  − GZ_max_Winkel ändert sich weniger stark
```

**Prüfkriterium:** Unexplained variation > 10% in GM → Überprüfung

---

### 7.12 [F7.12] Hydrostatik-Eingangsdaten mit Widersprüchen

**Symptom:**
- Rumpf-Volumen aus CAD: 25 m³
- Aber Verdrängungs-Berechnung zeigt 27 m³
- Freibord überprüft, passt nicht

**Ursache:**
- CAD-Modell nicht aktuell mit Hydrostatik-Datensatz
- Manuelles Update nicht konsistent durchgeführt
- Verschiedene Datei-Versionen vermischt

**Folge:**
- GZ-Berechnung auf fehler­haften Eingaben basiert
- Zertifizierung verzögert
- Engineering-Glaubwürdigkeit untergraben

**Empfohlene Korrektion:**
```
Daten-Audit durchführen:
  1. CAD-Rumpf-Volumen messen (aus CAD direkt)
  2. Hydrostatik-Daten überprüfen (Spanten, Wasserlinie)
  3. Gewichtsaufstellung vs. CG-Annahme
  4. Alle Abweichungen dokumentieren und korrigieren
  5. Neue Hydrostatik-Berechnung durchlaufen

Einmal korrekt, dann versionskontrollen
```

**Prüfkriterium:** Inkonsistenzen > 2% → Überprüfung vor Freigabe

---

## 8. Stabilitäts-Kurven für Entwurfsphasen

### 8.1 Concept-Phase

Schnelle Abschätzung basierend auf Vergleichsboote:
```
GM_est = (Freeboard/BWL) × 0.5 bis 1.0 (empirisch)
GZ_max_est ≈ 35° ± 5°
RA_est ≈ 0.070–0.100 m·rad (abhängig Klasse)
```

### 8.2 Preliminary Design Phase

Detaillierte Hydrostatik mit CAD-Rumpf, geschätztem CG:
```
Alle Parameter wie Konzept berechnet
Toleranzbereich: ±15% auf GZ-Werte
Iteration auf CG-Annahme nur wenn notwendig
```

### 8.3 Final Design Phase

Vollständige Hydrostatik mit detailliertem CG:
```
Alle Gewichte itemisiert
FS-Effekte Tabelle vollständig
Multiple Ladesituationen
GZ-Kurven für Zertifizierung
```

---

## 9. Normen und Standards

### 9.1 ISO 12217 (Stabilitäts-Anforderungen)

Deckt ab: Rumpfform, Gewichtsverteilung, Stabilität über Neigung 0–180°

### 9.2 CE Recreational Craft Directive 2013/53/EU

Fordert Stabilitäts-Nachweis für Category A–D Boote (2.5–24m)

### 9.3 Class Society Rules (ABS, DNV-GL, Bureau Veritas etc.)

Optional für professionelle Yachten, zusätzliche Anforderungen

---

## 10. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class BoatCategoryEnum(str, Enum):
    CAT_A = "A"
    CAT_B = "B"
    CAT_C = "C"
    CAT_D = "D"

class LoadingConditionEnum(str, Enum):
    LIGHT_SHIP = "light_ship"
    FULL_DEPARTURE = "full_departure"
    ARRIVAL = "arrival"
    HALF_LOADED = "half_loaded"

class HydrostaticPoint(BaseModel):
    """Einzelner Punkt der Hydrostatik-Kurve"""
    model_config = {"from_attributes": True}
    
    heel_angle_deg: float = Field(..., description="Heel angle (degrees, 0-180)")
    gz_meter: float = Field(..., description="GZ righting arm (meters)")
    righting_moment_knm: Optional[float] = Field(None, description="Righting moment (kN·m)")
    righting_area_integral: Optional[float] = Field(None, description="Area integral (m·rad)")

class StabilityCharacteristics(BaseModel):
    """Stabilitäts-Charakteristiken eines Schiffs"""
    model_config = {"from_attributes": True}
    
    # Basis-Parameter
    gm_meter: float = Field(..., ge=0.0, description="Metacentric height (GM)")
    gz_at_30_deg: float = Field(..., description="GZ at 30° heel (meters)")
    gz_max_meter: float = Field(..., description="Maximum GZ (meters)")
    gz_max_angle_deg: float = Field(..., description="Angle of maximum GZ (degrees)")
    
    # Stabilität-Kurve
    stability_curve: List[HydrostaticPoint] = Field(default_factory=list, description="Full stability curve (0-180°)")
    
    # Righting Areas
    ra_0_to_40_deg: Optional[float] = Field(None, description="Righting area 0-40° (m·rad)")
    ra_0_to_gz_max: Optional[float] = Field(None, description="Righting area 0-GZ_max (m·rad)")
    capsize_angle_deg: Optional[float] = Field(None, description="Angle where GZ becomes negative")
    
    # Kategorisierung
    boat_category: BoatCategoryEnum = Field(..., description="CE Category A-D")
    loading_condition: LoadingConditionEnum = Field(..., description="Loading scenario")
    
    # Free Surface Correction
    fs_correction_meter: Optional[float] = Field(None, description="Free surface effect correction (meters)")
    
    # Compliance
    iso_12217_compliant: bool = Field(..., description="Meets ISO 12217 requirements")
    compliance_warnings: List[str] = Field(default_factory=list, description="Compliance issues")

class HydrostaticAnalysis(BaseModel):
    """Vollständige Hydrostatik-Analyse"""
    model_config = {"from_attributes": True}
    
    ship_name: str = Field(..., description="Schiff-Name")
    analysis_date: datetime = Field(default_factory=datetime.now, description="Analysis date")
    
    # Geometrische Eingaben
    loa_mm: float = Field(..., description="Length overall (mm)")
    lwl_mm: float = Field(..., description="Length waterline (mm)")
    bwl_mm: float = Field(..., description="Beam waterline (mm)")
    draft_mm: float = Field(..., description="Draft (mm)")
    displacement_kg: float = Field(..., description="Displacement (kg)")
    
    # Schwerpunkt
    cg_x_mm: float = Field(..., description="Longitudinal CG (mm from midships)")
    cg_y_mm: float = Field(0.0, description="Transverse CG (mm from centerline)")
    cg_z_mm: float = Field(..., description="Vertical CG above baseline (mm)")
    
    # Analyse-Ergebnisse
    characteristics_per_condition: List[StabilityCharacteristics] = Field(..., description="Stability by condition")
    
    # Gesamtbewertung
    overall_assessment: str = Field(..., description="Overall stability assessment")
    recommendations: List[str] = Field(default_factory=list, description="Design recommendations")
    
    confidence_level: float = Field(0.90, ge=0.0, le=1.0, description="Analysis confidence")

def calculate_gm(bm_meter: float, bg_meter: float) -> float:
    """Calculate metacentric height GM = BM - BG"""
    return bm_meter - bg_meter

def calculate_gz_at_angle(gm: float, heel_angle_rad: float) -> float:
    """Approximate GZ for small angles: GZ ≈ GM × sin(θ)"""
    import math
    return gm * math.sin(heel_angle_rad)

def evaluate_iso_12217_compliance(
    characteristics: StabilityCharacteristics
) -> tuple[bool, List[str]]:
    """Überprüfen ISO 12217 Anforderungen"""
    warnings = []
    compliant = True
    
    # ISO 12217 Anforderungen
    requirements = {
        "A": {"gz_30": 0.20, "ra_40": 0.090},
        "B": {"gz_30": 0.15, "ra_40": 0.065},
        "C": {"gz_30": 0.10, "ra_40": 0.040},
        "D": {"gz_30": 0.05, "ra_40": 0.020},
    }
    
    cat = characteristics.boat_category.value
    req = requirements.get(cat, {})
    
    if characteristics.gz_at_30_deg < req.get("gz_30", 0):
        warnings.append(f"GZ@30° below requirement: {characteristics.gz_at_30_deg:.3f} < {req.get('gz_30')}")
        compliant = False
    
    if characteristics.ra_0_to_40_deg is not None:
        if characteristics.ra_0_to_40_deg < req.get("ra_40", 0):
            warnings.append(f"RA(0-40°) below requirement: {characteristics.ra_0_to_40_deg:.4f} < {req.get('ra_40')}")
            compliant = False
    
    return compliant, warnings
```

---

**Datei abgeschlossen.**  
Kat 31.02 Hydrostatik — Version 1.0 — 2025-01
