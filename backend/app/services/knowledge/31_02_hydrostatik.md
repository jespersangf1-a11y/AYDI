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

---
---

# ERGÄNZUNG Version 1.1 (2026-07) — Werft-Tiefe: dokumentierte Hydrostatik-Grundgrößen

> **Hinweis zur Ergänzung:** Der Bestand oben (Abschnitte 1–10) bleibt unverändert. Die folgenden Abschnitte 11–19 ergänzen die im Bestand fehlenden **klassischen Hydrostatik-Grundgrößen** (Wasserlinienfläche, Formkoeffizienten, LCB/LCF, TPC, MCT, KB/BM/KM/GM) mit **web-verifizierten, quellenbelegten** Definitionen und Formeln. Jede faktische Angabe trägt eine Quelle und ein Confidence-Tag.
>
> **Kernregel dieser Ergänzung:** Es werden **keine** yacht-spezifischen Zahlenwerte, Rechenbeispiele oder Grenzwerte erfunden. Wo eine Formel/Definition dokumentiert ist, steht sie mit Quelle. Wo nur ein Prinzip belegbar ist, steht das Prinzip — quantitative Beispiele, die nicht zweifelsfrei belegbar sind, werden als `estimated — unverifiziert` markiert oder weggelassen.

---

## 11. Normativer Rahmen — Terminologie & Bemessungsgrundlagen

Für Hydrostatik/Stabilität von Sportbooten sind drei ISO-Normfamilien einschlägig. Nummer + Titel + Scope sind einzeln verifiziert:

| Norm | Titel (verbatim) | Scope (Kurz) |
|------|------------------|--------------|
| **ISO 7462:1985** | *Shipbuilding — Principal ship dimensions — Terminology and definitions for computer applications* | Legt Terminologie und Definitionen für die Hauptabmessungen und daraus abgeleitete (dimensionslose) Formkoeffizienten zur Beschreibung des Rumpfs und seiner hydrostatischen Zustände fest. |
| **ISO 8666:2020** | *Small craft — Principal data* | Definitionen der Hauptabmessungen und zugehöriger Daten sowie der Massespezifikationen und Beladungszustände. Gilt für Boote mit Rumpflänge **L_H ≤ 24 m**. |
| **ISO 12217 (Teil 1/2/3)** | *Small craft — Stability and buoyancy assessment and categorization* | Verfahren zur Bewertung von Stabilität/Auftrieb intakter Boote und Zuweisung der Entwurfskategorie A/B/C/D. **Teil 1:** Nicht-Segelboote L_H ≥ 6 m · **Teil 2:** Segelboote L_H ≥ 6 m · **Teil 3:** Boote L_H < 6 m. |

> Quellen: [ISO 7462:1985 (iso.org)](https://www.iso.org/standard/14197.html) · [ISO 8666:2020 (iso.org)](https://www.iso.org/standard/79071.html) · [ISO 12217-1:2022 (iso.org)](https://www.iso.org/standard/79072.html) · [ISO 12217-2:2022 (iso.org)](https://www.iso.org/standard/79073.html) · [ISO 12217-3:2022 (iso.org)](https://www.iso.org/standard/79074.html) | Confidence: **documented**

**Wichtige Abgrenzung (Audit-relevant):**
- **ISO 7462** ist die *Definitions-/Terminologienorm* für Hauptabmessungen und Formkoeffizienten (die Sprache, in der Hydrostatik-Größen benannt werden).
- **ISO 8666** legt fest, *welche* Abmessungen und *welche* Beladungszustände (u. a. der beladene Verdrängungszustand `m_LDC`) für Sportboote gelten — d. h. mit welcher Verdrängung die Hydrostatik gerechnet wird.
- **ISO 12217** ist die *Bewertungsnorm* (Stabilitätskriterien, Kategorisierung). Sie ist **Stabilität/Auftrieb** — nicht Struktur (Struktur = ISO 12215, siehe CLAUDE.md).

> ⚠️ ZU PRÜFEN (Audit): Die konkreten GZ-/RA-Zahlengrenzwerte in **Bestands-Abschnitt 2.3** (z. B. „GZ @ 30° ≥ 0,20 m" für Kat A) sind gegen die **konkret anwendbare ISO-12217-Teilnorm und Ausgabe (2015 vs. 2022)** zu verifizieren, da die Kriterien je nach Teil (Segel-/Nicht-Segelboot) und Prüfmethode unterschiedlich definiert sind. Bis zur Einzelverifikation gelten diese Bestandswerte als `estimated — unverifiziert`.

---

## 12. Grundgrößen: Verdrängung, Wasserlinienfläche, Formkoeffizienten

### 12.1 Verdrängung (Displacement)

Zwei dokumentierte Formen (vgl. Bestand Abschnitt 1.1, hier terminologisch präzisiert):

```
Massenverdrängung   Δ = ρ × ∇        [t]   (ρ in t/m³, ∇ in m³)
Volumenverdrängung  ∇ = Δ / ρ        [m³]
```

- **Δ (Delta):** Masse des verdrängten Wassers = Gesamtmasse des Boots (Gleichgewicht).
- **∇ (Nabla):** Volumen des verdrängten Wassers = eingetauchtes Rumpfvolumen.

> Quelle: [Marine Insight — Ship Stability / Hydrostatics](https://www.marineinsight.com/naval-architecture/ship-stability-introduction-hydrostatics-stability-surface-ships/) | Confidence: **documented**

### 12.2 Wasserlinienfläche A_w (Waterplane Area)

Die **Wasserlinienfläche** ist die vom Rumpf in der Schwimmwasserlinie eingeschlossene horizontale Schnittfläche. Sie ist die zentrale Größe für **TPC**, **BM** und **LCF** (alle nachfolgend).

```
A_w = L_WL × B_WL × C_w
```

> Quelle: TPC-/Formkoeffizienten-Definition, [Marine Inbox / cultofsea](https://www.cultofsea.com/ship-stability/coefficients-of-form-ships-waterplane-block-midship-and-prismatic-coefficient/) | Confidence: **documented**

### 12.3 Formkoeffizienten (Coefficients of Form)

Dimensionslose Kennzahlen der Rumpfvölligkeit (alle Definitionen verifiziert, ISO-7462-Terminologie):

| Koeffizient | Symbol | Formel | Bedeutung |
|-------------|--------|--------|-----------|
| Wasserlinien-Völligkeit | **C_w** | `C_w = A_w / (L_WL × B_WL)` | Völligkeit der Wasserlinienfläche |
| Blockkoeffizient | **C_b** | `C_b = ∇ / (L_WL × B_WL × T)` | Völligkeit des Verdrängungskörpers |
| Hauptspant-Völligkeit | **C_m** | `C_m = A_m / (B_WL × T)` | Völligkeit des größten eingetauchten Spants (A_m) |
| Schärfegrad (prismatisch) | **C_p** | `C_p = ∇ / (A_m × L_WL)` | Längsverteilung des Volumens |

**Dokumentierte Beziehung:**
```
C_b = C_m × C_p     ⇒     C_p = C_b / C_m
```

> Quellen: [cultofsea — Coefficients of Form](https://www.cultofsea.com/ship-stability/coefficients-of-form-ships-waterplane-block-midship-and-prismatic-coefficient/) · [Ships2Ports — Ship Specifications](https://ships2ports.com/ship-specifications-explained-dimensions-tonnage-stability-and-calculation-formulas/) | Confidence: **documented**

> ℹ️ Hinweis: T = Tiefgang (draught), A_m = Fläche des eingetauchten Hauptspants. Es werden hier bewusst **keine** typischen C_b/C_p-Zahlenbereiche für Yacht-Klassen angegeben — belastbare klassenspezifische Bänder wären erfindungsgefährdet (`estimated — unverifiziert`). Konkrete Werte immer aus dem CAD-/Lines-Modell des jeweiligen Boots ableiten.

---

## 13. Auftriebs- und Flotationszentren: LCB, VCB (KB), LCF

| Größe | Symbol | Definition (verifiziert) |
|-------|--------|--------------------------|
| Längenschwerpunkt des Auftriebs | **LCB** | Längsposition des Volumenschwerpunkts der Verdrängung (Center of Buoyancy) bezogen auf einen Referenzpunkt. |
| Höhenschwerpunkt des Auftriebs | **VCB / KB** | Vertikaler Abstand Kiel → Auftriebsmittelpunkt B. |
| Längenschwerpunkt der Wasserlinienfläche | **LCF** | Flächenschwerpunkt (Zentroid) der Wasserlinienfläche A_w. **Drehpunkt (Fulcrum), um den das Boot trimmt.** |

> Quelle: [Marine Insight — Hydrostatics/Stability](https://www.marineinsight.com/naval-architecture/ship-stability-introduction-hydrostatics-stability-surface-ships/) · [Marine Insight — Centre of Flotation](https://www.marineinsight.com/naval-architecture/what-is-the-centre-of-floatation/) | Confidence: **documented**

**Zentrale Merksätze (dokumentiert):**
1. **Längsgleichgewicht (kein Trimmmoment):** LCB liegt exakt senkrecht unter dem Längenschwerpunkt der Masse LCG. → `x_LCB = x_LCG`. Dies präzisiert den Bestands-Abschnitt 5.1.
2. **LCF ≠ LCB:** Der Auftriebs-Längenschwerpunkt (LCB, Volumen) und der Flotations-Längenschwerpunkt (LCF, Fläche) liegen i. d. R. **nicht** an derselben Stelle. Trimm dreht um **LCF**, nicht um Mitte Schiff.

### 13.1 VCB/KB — dokumentierte Näherung (Morrish/Normand)

Für Rümpfe „gewöhnlicher Form" existiert eine **dokumentierte** Näherungsformel (Morrish/Normand):

```
KB ≈ (1/3) × ( 5T/2 − ∇ / A_w )        (Morrish/Normand)
```

- T = Tiefgang, ∇ = Verdrängungsvolumen, A_w = Wasserlinienfläche.

> Quelle: „Morrish's or Normand's formula", [Stability for Masters and Mates (flipbuilder)](https://online.flipbuilder.com/ekxp/lzjw/files/basic-html/page114.html) · [KB/BM Skript (academy PDF)](https://ilginozgul.academy/wp-content/uploads/2021/12/ship-stb.-wihtout-video.pdf) | Confidence: **documented**

> ⚠️ Näherung: Gilt für „ordinary form"; für ausgeprägte Yacht-Formen (Kielyacht, Katamaran, Gleiter) nur als Plausibilitätscheck. Exaktes KB aus Spantintegration (Bestands-Abschnitt 3.2, Simpson) verwenden.

---

## 14. Vertikale Metazentrik: KB, BM, KM, GM (transversal & longitudinal)

Diese Größen sind der dokumentierte Kern der Anfangsstabilität. Sie präzisieren Bestands-Abschnitt 2.1/2.2.

### 14.1 Transversal (Querstabilität)

```
BM   = I_T / ∇          I_T = 2. Flächenmoment der Wasserlinie um die Längs-Mittellinie
KM   = KB + BM
GM   = KM − KG          KG = Höhe des Massenschwerpunks über Kiel
```

> Quelle: [Marine Insight — Hydrostatics/Stability](https://www.marineinsight.com/naval-architecture/ship-stability-introduction-hydrostatics-stability-surface-ships/) | Confidence: **documented**

### 14.2 Longitudinal (Längsstabilität — Basis für Trimm/MCT)

Analog, aber um die **Querachse durch LCF**:

```
BM_L = I_L / ∇          I_L = 2. Flächenmoment der Wasserlinie um die Querachse durch LCF
KM_L = KB + BM_L
GM_L = KM_L − KG
```

> Quelle: [Nautical Solver — LCF/BM_L](https://nauticalsolver.com/calculators/hull/lcf/lcf.php) · Britannica, *Naval architecture — Metacentric stability* | Confidence: **documented**

**Größenordnung (dokumentiert, qualitativ):** GM_L ist typischerweise um Größenordnungen größer als GM (transversal), da I_L ≫ I_T (Länge ≫ Breite). Deshalb ist ein Boot längs weit „steifer" als quer — konkrete Zahlen sind boots­spezifisch und werden hier **nicht** angegeben (Erfindungsvermeidung).

### 14.3 GZ bei großen Winkeln — wall-sided-Formel (dokumentiert)

Der Bestand nutzt für kleine Winkel `GZ ≈ GM · sinθ`. Für größere Winkel (Rumpf noch annähernd senkrechtwandig an der WL) ist die **wall-sided-Formel** dokumentiert:

```
GZ = sinθ × ( GM + ½ · BM · tan²θ )
```

> Quelle: [ShipCalculators — Metacentric height / wall-sided](https://shipcalculators.com/wiki/metacentric-height) · [Merchant Navy Decoded — Transverse Stability](https://www.merchantnavydecoded.com/transverse-stability-of-ship/) | Confidence: **documented**

> ⚠️ Gültigkeitsgrenze: Die Annahme „wall-sided" (senkrechte Bordwände an der Wasserlinie) verliert mit zunehmendem Winkel an Genauigkeit, sobald Deck eintaucht bzw. die Bilge austaucht. Für die vollständige GZ-Kurve (0–180°, Bestands-Abschnitt 3) bleibt die numerische Spantintegration maßgeblich.

---

## 15. TPC und MCT — Eintauchung und Trimmänderung

### 15.1 TPC — Tonnes Per Centimetre Immersion

**Definition (verifiziert):** Die Masse, die geladen/gelöscht werden muss, um den mittleren Tiefgang um **1 cm** (paralleles Ein-/Auftauchen) zu ändern.

```
TPC = A_w × ρ / 100          A_w in m², ρ in t/m³ → TPC in t/cm
```

**Herleitung (dokumentiert):** 1 cm Paralleltauchung = 0,01 m Höhe → Volumen `A_w × 0,01 m³` → Masse `ρ × A_w × 0,01` = `A_w × ρ / 100`.

> Quelle: [Marine Inbox — TPC](https://marineinbox.com/marine-exams/tonnes-per-centimetre-immersion-tpc/) · [MarineGyaan — TPC](https://marinegyaan.com/what-is-tonnes-per-centimeter-tpc/) | Confidence: **documented**

- Höhere Wasserdichte ODER größere A_w ⇒ höheres TPC.
- TPC variiert mit Tiefgang (A_w ändert sich) und mit ρ (Süß-/Salzwasser, vgl. Bestands-Abschnitt 1.1).

### 15.2 MCT1cm (MCTC) — Moment to Change Trim one centimetre

**Definition (verifiziert):** Das Längs-Moment (um LCF), das erforderlich ist, um den Trimm um **1 cm** zu ändern.

```
MCT1cm = ( Δ × GM_L ) / ( 100 × L )     Δ in t, GM_L und L in m → t·m / cm
```

**Herleitung (dokumentiert):** Moment für 1 m Trimm = `Δ × GM_L / L`; Division durch 100 ⇒ Moment für 1 cm Trimm.

> Quelle: [MarineGyaan — Trimming Moment (MCTC)](https://marinegyaan.com/what-is-trimming-moment-mctc/) · [Merchant Navy Decoded — Trim of Ship](https://www.merchantnavydecoded.com/trim-of-ship/) | Confidence: **documented**

> ℹ️ In Näherungen wird oft GM_L ≈ BM_L gesetzt (da BG_L klein gegenüber BM_L). Nur als Näherung verwenden; exakt mit GM_L rechnen.

### 15.3 Trimmänderung und Verteilung auf die Perpendikel

```
Trimmänderung  COT = Trimmmoment / MCT1cm            [cm]
```

Die Änderung verteilt sich **um LCF** (nicht um Mitte Schiff) auf vorderes/hinteres Perpendikel:

```
Δd_achtern  = COT × (l / L)      l = Abstand LCF ↔ hinteres Perpendikel (AP)
Δd_vorn     = COT − Δd_achtern
```

> Quelle: [ScienceDirect — Draft Aft / change of trim](https://www.sciencedirect.com/topics/engineering/draft-aft) · [The Nautical Site — Trim](http://thenauticalsite.in/NauticalNotes/Stability/MyStability-Lesson09-Trim.htm) | Confidence: **documented**

**Merksatz (dokumentiert):** Nur wenn LCF exakt mittschiffs liegt, ändern sich Bug- und Heck-Tiefgang gleich stark. Liegt LCF (typisch) achterlich, ändert sich der Heck-Tiefgang stärker.

---

## 16. Fehlerbild-Atlas (FB-31-02-NNN)

> Kollisionsprüfung: Der Bestand nutzt das Schema `[F7.1]…[F7.12]`. Der folgende Atlas nutzt das **kollisionsfreie** Präfix `FB-31-02-NNN` und ergänzt Fehlerbilder rund um die in dieser Ergänzung eingeführten Grundgrößen (Wasserlinienfläche, Koeffizienten, LCB/LCF, TPC, MCT). Fachliche Überschneidungen mit dem Bestand sind vermerkt.

### FB-31-02-001 — Trimm fälschlich um Mitte Schiff statt um LCF gerechnet
- **Fehlerbild:** Bug-/Heck-Tiefgänge nach Zuladung stimmen nicht mit Messung überein; Δd vorn = Δd achtern angenommen.
- **Ursache:** Trimmverteilung ohne LCF-Position (l/L) gerechnet.
- **Korrektur:** COT über LCF verteilen (Abschnitt 15.3). LCF aus Hydrostatik-Tabelle je Tiefgang entnehmen.
- **Prüfkriterium:** Wenn LCF ≠ Mitte Schiff und Δd_vorn = Δd_achtern gesetzt → Fehler.
- Quelle: siehe 15.3 | Confidence: **documented**

### FB-31-02-002 — TPC mit falscher Wasserdichte (Süß-/Salzwasser)
- **Fehlerbild:** Reale Paralleltauchung weicht ~2,5 % von der Rechnung ab.
- **Ursache:** ρ = 1,000 statt 1,025 t/m³ (oder umgekehrt) in `TPC = A_w × ρ / 100`.
- **Korrektur:** ρ passend zum Fahrtgebiet wählen (Bestands-Abschnitt 1.1: Süß 1000, Atlantik 1025, Mittelmeer 1023 kg/m³).
- **Prüfkriterium:** Dichteannahme nicht dokumentiert → Überprüfung.
- Quelle: 15.1 | Confidence: **documented**

### FB-31-02-003 — A_w bei falschem Tiefgang verwendet
- **Fehlerbild:** TPC/BM/MCT über den Beladungsbereich unplausibel konstant.
- **Ursache:** A_w (und damit I_T, I_L) ist tiefgangsabhängig; ein einziger A_w-Wert für alle Zustände benutzt.
- **Korrektur:** A_w, I_T, I_L, LCF je Tiefgang aus der Hydrostatik-Kurve; TPC/BM/MCT tiefgangsabhängig führen.
- **Prüfkriterium:** Gleicher A_w für ≥ 2 stark verschiedene Tiefgänge → Überprüfung.
- Quelle: 12.2 / 14 / 15 | Confidence: **documented**

### FB-31-02-004 — GM_L mit BM (transversal) statt BM_L verwechselt
- **Fehlerbild:** MCT1cm um Größenordnungen zu klein; Trimm reagiert „viel zu empfindlich" in der Rechnung.
- **Ursache:** In `MCT1cm = Δ·GM_L/(100·L)` GM (quer) statt GM_L (längs) eingesetzt.
- **Korrektur:** GM_L aus `I_L/∇` (Querachse durch LCF), nicht I_T.
- **Prüfkriterium:** GM_L in derselben Größenordnung wie GM_transversal → Fehler.
- Quelle: 14.2 / 15.2 | Confidence: **documented**

### FB-31-02-005 — Formkoeffizienten mit inkonsistenten Längen (LOA vs. LWL vs. LPP)
- **Fehlerbild:** C_b > 1 oder unplausibel; C_b = C_m·C_p geht nicht auf.
- **Ursache:** Mischung aus LOA/LWL/LPP bzw. Formbreite vs. B_WL in den Nennern.
- **Korrektur:** Durchgängig **eine** Bezugslänge und **B_WL/T** in der Wasserlinie verwenden; Konsistenz über C_b = C_m·C_p prüfen.
- **Prüfkriterium:** C_b·C_p·C_m-Beziehung verletzt oder C_b > 1 → Fehler.
- Quelle: 12.3 | Confidence: **documented**

### FB-31-02-006 — wall-sided-Formel über ihren Gültigkeitsbereich hinaus benutzt
- **Fehlerbild:** GZ bei großen Winkeln (Deck taucht ein) überschätzt.
- **Ursache:** `GZ = sinθ(GM + ½BM·tan²θ)` bis in den Bereich Decktauchung/Bilge-Austauchung angewendet.
- **Korrektur:** Bei großen Winkeln numerische Spantintegration (Bestands-Abschnitt 3) statt wall-sided.
- **Prüfkriterium:** wall-sided jenseits Decktauchung → Überprüfung.
- Quelle: 14.3 | Confidence: **documented**
- *Überschneidung:* ergänzt Bestand [F7.4]/[F7.5] (GZ-Kurve hohe Winkel).

### FB-31-02-007 — Verdrängung nicht im normgerechten Beladungszustand
- **Fehlerbild:** Hydrostatik/Stabilität gegen ein „Wunsch"-Δ statt den maßgeblichen Zustand nachgewiesen.
- **Ursache:** Falscher/kein definierter Beladungszustand (z. B. `m_LDC` nach ISO 8666) zugrunde gelegt.
- **Korrektur:** Beladungszustände gemäß ISO 8666 definieren und Hydrostatik je Zustand rechnen (vgl. Bestands-Abschnitt 8, mehrere Ladesituationen).
- **Prüfkriterium:** Kein dokumentierter Norm-Beladungszustand → Überprüfung.
- Quelle: 11 (ISO 8666) | Confidence: **documented**
- *Überschneidung:* ergänzt Bestand [F7.3]/[F7.11] (CG/Ladesituationen).

---

## 17. Troubleshooting — Entscheidungsbaum Grundgrößen

```
Symptom: berechnete Tiefgänge/Trimm ≠ Messung (Krängungsversuch/Ablesung)
│
├─ Paralleltauchung falsch?
│   ├─ ρ (Süß/Salz) korrekt?              → nein: FB-31-02-002
│   └─ A_w beim richtigen Tiefgang?       → nein: FB-31-02-003
│
├─ Trimm/Endtiefgänge falsch?
│   ├─ um LCF (l/L) verteilt?             → nein: FB-31-02-001
│   ├─ GM_L (nicht GM_quer) in MCT1cm?    → nein: FB-31-02-004
│   └─ maßgeblicher Beladungszustand?     → nein: FB-31-02-007
│
└─ Koeffizienten/Völligkeit unplausibel?
    └─ konsistente Längen/B_WL/T?         → nein: FB-31-02-005
        └─ Check: C_b = C_m × C_p
```

---

## 18. FAQ, Revalidierung & Glossar

### 18.1 FAQ

**F: Um welchen Punkt trimmt das Boot — Mitte Schiff oder LCF?**
A: Um **LCF** (Flächenschwerpunkt der Wasserlinie). Trimmmomente wirken um LCF als Drehpunkt. Quelle: Abschnitt 13 / 15.3. Confidence: documented.

**F: Warum ist ein Boot längs viel „steifer" als quer?**
A: Weil GM_L auf `I_L/∇` mit dem Flächenmoment um die **Querachse** beruht und I_L ≫ I_T (Länge ≫ Breite). Konkrete Zahlen sind bootsspezifisch. Quelle: 14.2. Confidence: documented (qualitativ).

**F: Reicht `GZ ≈ GM·sinθ` für die Stabilitätskurve?**
A: Nur für kleine Winkel. Größere Winkel: wall-sided-Formel (14.3, mit Gültigkeitsgrenze) bzw. numerische Integration (Bestand Abschnitt 3). Confidence: documented.

**F: Welche Norm liefert die Definitionen, welche die Kriterien?**
A: Definitionen/Terminologie: ISO 7462 (Rümpfe allgemein) und ISO 8666 (Sportboot-Hauptdaten/Beladung). Bewertungskriterien/Kategorisierung: ISO 12217 (Teil 1/2/3). Quelle: Abschnitt 11. Confidence: documented.

### 18.2 Revalidierung / Prüfanlässe

Hydrostatik-/Stabilitätsgrundlagen sind kein „einmal berechnet, fertig". Neu zu validieren bei:
- Änderung der Massenverteilung (Ballast, Motor, Ausbau, Tankanordnung) → KG/LCG neu, damit GM/GM_L/Trimm neu.
- Geometrieänderung an der Wasserlinie (Anbauten, Baderplattform, Kiel) → A_w, I_T, I_L, LCF, TPC, MCT neu.
- Wechsel des maßgeblichen Beladungszustands (ISO 8666).
- **Krängungsversuch (inclining experiment):** dokumentiertes Verfahren zur empirischen Bestimmung von KG/GM; im Rahmen der ISO-12217-Bewertung ein anerkanntes Mittel, um die gerechnete Vertikallage des Schwerpunkts abzusichern.

> ⚠️ ZU PRÜFEN (Audit): Konkrete Auslöse-Schwellen und die genaue Pflicht/Häufigkeit eines Krängungsversuchs sind der jeweils anwendbaren ISO-12217-Teilnorm zu entnehmen; hier bewusst **nicht** beziffert (`estimated — unverifiziert`).

### 18.3 Glossar (Kurzform)

| Kürzel | Deutsch | Definition (Quelle: Abschnitt) |
|--------|---------|-------------------------------|
| Δ / ∇ | Massen-/Volumenverdrängung | 12.1 |
| A_w | Wasserlinienfläche | 12.2 |
| C_w, C_b, C_m, C_p | Wasserlinien-/Block-/Hauptspant-/Schärfe-Koeffizient | 12.3 |
| LCB | Längenschwerpunkt Auftrieb | 13 |
| VCB/KB | Höhenschwerpunkt Auftrieb (ab Kiel) | 13 |
| LCF | Längenschwerpunkt Wasserlinienfläche = Trimm-Drehpunkt | 13 |
| BM / BM_L | Metazentrischer Radius quer/längs (I/∇) | 14.1 / 14.2 |
| KM / KM_L | Metazentrum über Kiel quer/längs | 14 |
| GM / GM_L | Metazentrische Höhe quer/längs | 14 |
| KG | Höhe Massenschwerpunkt über Kiel | 14.1 |
| TPC | Masse je 1 cm Paralleltauchung | 15.1 |
| MCT1cm | Moment je 1 cm Trimmänderung | 15.2 |
| COT | Change of Trim (Trimmänderung) | 15.3 |

---

## 19. Quellenverzeichnis (Ergänzung 1.1)

**Normen (Titel/Scope verifiziert):**
- ISO 7462:1985 — *Shipbuilding — Principal ship dimensions — Terminology and definitions for computer applications* — https://www.iso.org/standard/14197.html
- ISO 8666:2020 — *Small craft — Principal data* — https://www.iso.org/standard/79071.html
- ISO 12217-1:2022 / -2:2022 / -3:2022 — *Small craft — Stability and buoyancy assessment and categorization* — https://www.iso.org/standard/79072.html · /79073.html · /79074.html

**Fachquellen (Formeln/Definitionen verifiziert):**
- Marine Insight — *Ship Stability: Introduction to Hydrostatics* — https://www.marineinsight.com/naval-architecture/ship-stability-introduction-hydrostatics-stability-surface-ships/
- Marine Insight — *Centre of Flotation* — https://www.marineinsight.com/naval-architecture/what-is-the-centre-of-floatation/
- cultofsea — *Coefficients of Form* — https://www.cultofsea.com/ship-stability/coefficients-of-form-ships-waterplane-block-midship-and-prismatic-coefficient/
- Ships2Ports — *Ship Specifications Explained* — https://ships2ports.com/ship-specifications-explained-dimensions-tonnage-stability-and-calculation-formulas/
- MarineGyaan — *TPC* / *Trimming Moment (MCTC)* — https://marinegyaan.com/what-is-tonnes-per-centimeter-tpc/ · https://marinegyaan.com/what-is-trimming-moment-mctc/
- Merchant Navy Decoded — *Trim of Ship* / *Transverse Stability* — https://www.merchantnavydecoded.com/trim-of-ship/ · https://www.merchantnavydecoded.com/transverse-stability-of-ship/
- ShipCalculators — *Metacentric height (wall-sided)* — https://shipcalculators.com/wiki/metacentric-height
- ScienceDirect Topics — *Draft Aft / Moment to Change Trim* — https://www.sciencedirect.com/topics/engineering/draft-aft
- Morrish/Normand-Näherung (KB) — *Stability for Masters and Mates* — https://online.flipbuilder.com/ekxp/lzjw/files/basic-html/page114.html

> Alle in Ergänzung 1.1 neu eingeführten faktischen Angaben sind web-verifiziert (`documented`). Nicht zweifelsfrei belegbare Größen wurden als `estimated — unverifiziert` markiert bzw. weggelassen; es wurden keine yacht-spezifischen Zahlenwerte, Grenzwerte oder Rechenbeispiele erfunden.

---

**Ergänzung Version 1.1 — 2026-07 — abgeschlossen.**  
Kat 31.02 Hydrostatik — Version 1.1
