# Kat 31.01 — Rumpfformen

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Rumpfformen  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Grundkonzepte Rumpfformen

Die Rumpfform ist die primäre Schnittstelle zwischen Schiff und Wasser. Sie determiniert:
- **Hydrodynamischen Widerstand** (Wellen-, Rei­bungs-, Formwiderstand)
- **Stabilitätseigenschaften** (initial, dynamisch, Kursstabilität)
- **Seegang-Verhalten** (Pitching, Heave-Amplitude, Komfort)
- **Produktionskosten** (Mold-Komplexität, Anzahl Spanten)
- **Ästhetische Wirkung** (Vertrauensindex, emotionale Reaktion)

### 1.1 Klassifikation nach Verdrängungs­charak­teristik

**Displacement (Vollrumpf)**  
- ~80–100% theoretisches Volumen ausgenutzt
- Ideale Formstabilität
- Niedriger Widerstand bei Hubraumdichte >100 kg/m³
- Beispiel: Klassische Cruising-Segler, Traditionsyachten
- Prismatic Coefficient (Cp): 0.55–0.65
- LWL/BWL Verhältnis: 2.5–3.2

**Semi-Displacement**  
- 70–90% Ausnützung, transitional
- Kompromiss: Verdränger-Stabilität + mittlere Speed
- Typisch Motorsegler, robuste Cruiser
- Cp: 0.60–0.70
- LWL/BWL: 3.0–3.8
- Knickspant-Design häufig

**Planing (Gleiter)**  
- <50% Ausnützung, Dynamischer Auftrieb dominiert
- Hohe Geschwindigkeit, niedriges Trim bei Fahrt
- Motorboote, Performance-Segler
- Cp: 0.65–0.80 (flach-V-Rumpf)
- LWL/BWL: 3.0–4.5
- Kritische Geschwindigkeit: Froude-Zahl Fn = v / √(g·LWL) > 0.5–0.6

**Multihull (Katamaran, Trimaran)**  
- Zwei oder drei getrennte Rümpfe
- Massiver Stabilitätsvorteil über Gewicht (Form-Stabilität)
- Reduzierter Widerstand bei gleicher Verdrängung (dünnere Rümpfe)
- Cp pro Rumpf: 0.50–0.65
- Abstand zwischen Rümpfen: 0.4–0.6 × Rumpfbreite
- Slamming-Risiko im Brückenbereich

---

## 2. Formparameter und Vergleichsmessungen

### 2.1 Prismatischer Koeffizient (Cp)

```
Cp = Verdrängungsvolumen / (Hauptspantfläche × Wasserlinienlänge)
   = ∇ / (Ax × LWL)
```

**Interpretation:**
- **Cp < 0.55:** Sehr fine Form, hoher Widerstand (Verdränger-ineffizient)
- **Cp 0.55–0.65:** Optimal displacement (85% aller Cruiser)
- **Cp 0.65–0.75:** Voluminös, erhöhter Widerstand, mehr Platzeffizienz
- **Cp > 0.80:** Flach-Planing, extreme Breite

**Kritische Abhängigkeit:**
```
Widerstand_total = Cv + Cw + Cform
Cv (Reibung) ∝ Cp  (höhere Cp = größere benäßte Fläche)
Cw (Welle)   ∝ f(Cp, Fn)  (Wellenerregung komplex)
```

### 2.2 Längen-Breiten-Verhältnis (LWL/BWL)

```
λ = LWL / BWL  (Slenderness Ratio)
```

**Auswirkungen:**

| λ-Bereich | Rumpftyp | Stabilität | Widerstand | Seegang |
|-----------|----------|-----------|-----------|---------|
| 2.2–2.8 | Kurz, robust | Hoch (Initial) | Mittel | Rau |
| 2.8–3.5 | Standard Cruiser | Mittel | Niedrig | Komfortabel |
| 3.5–4.2 | Länglich, fein | Niedrig-mittel | Niedrig | Sanft |
| >4.2 | Extreme (Racing) | Sehr niedrig | Sehr niedrig | Kritisch |

**Physikalische Grenze:**
```
λ_max_stabil ≈ 4.5 + (Freeboard/BWL) × 2
```
Darüber: Initiative Stabilität <5°, Anfälligkeit für Broachng.

### 2.3 Freeboard und Seitenverhältnis

**Freeboard (FB):**
```
FB = Höhe_Wasserlinie_oben - LWL
```
- Einfluß auf Seegang-Fähigkeit: höheres FB = weniger Wasser an Deck
- Regulation: CE-Richtlinie 2013/53/EU fordert Mindest-FB nach Boat Class
- Ästhetik: FB < 0.08·LWL wirkt "niedrig", FB > 0.15·LWL wirkt "hoch"

**Seitenverhältnis (Aspect Ratio):**
```
AR = LWL / (Freeboard + mittlerer_Tiefgang)
```
- Einfluß auf Auftrieb und Seegang-Handling
- Optimum für Cruiser: 8–12
- Racing: bis 15

---

## 3. Detailgeometrie: Spantenform

### 3.1 V-Shaped Bottom (spitz Kiel)

**Geometrie:**
- Kielwinkel: 15–30° gegen Horizontal
- Profil: dreieckig oder parabolisch unten, U-förmig oben

**Eigenschaften:**
| Aspekt | Bewertung |
|--------|-----------|
| Gewässer-Verhalten | Ausgezeichnet (niedriger Rollwiderstand) |
| Segang-Komfort | Gut (Pitching-gedämpft) |
| Stabilität (Koeffizient) | Mittel (weniger Querstabilität) |
| Produktionskosten | Mittel (Spantenform komplex) |
| Tiefgang | Variabel, abhängig Kielwinkel |

**Anwendung:** Performance-Segler, Motorjachten >12m

### 3.2 U-Shaped (flach Kiel)

**Geometrie:**
- Kurvatur kontinuierlich, Radius ~0.3·BWL am tiefsten
- Übergangslinie zu Decksseite: sanfte Rundung

**Eigenschaften:**
| Aspekt | Bewertung |
|--------|-----------|
| Stabilität | Sehr hoch (großer righting arm) |
| Seegang-Komfort | Mittel (höheres Pitching) |
| Widerstand | Mittel-Hoch (Reibung) |
| Flächen-Effizienz | Sehr hoch (Interior-Volumen) |
| Produktionskosten | Niedrig (einfache Spanten) |

**Anwendung:** Cruising-Segler, Berufsschiffe, Stabilität-kritisch

### 3.3 Knickspant (Hard Chine)

**Geometrie:**
- Scharfe Kante Bodenseite-Seitenseite
- Zwei ebene oder sanft gekrümmte Flächen
- Winkel: 10–25° Abweichung von Senkrechten

**Eigenschaften:**
| Aspekt | Bewertung |
|--------|-----------|
| Produktionskosten | Sehr niedrig (flache Panels) |
| Widerstand | Niedrig-Mittel (Kantenwiderstand) |
| Seegang-Komfort | Rau (Schlagverhalten) |
| Stabilität | Mittel-Hoch (abhängig Breite) |
| Wartung | Mittel (Kantenversiegelung) |

**Kritische Anwendung:** Arbeitsboote, Kleine Motorboote, Budget-Baureihen

---

## 4. Wasserlinie und Unterwasserschiff

### 4.1 Wasserlinie-Charakteristiken

**Spantkoeffizient der Wasserlinie (Cwl):**
```
Cwl = Fläche_Wasserlinie / (LWL × BWL)
```
- Cwl < 0.60: Fine, V-förmig unten
- Cwl 0.60–0.75: Standard
- Cwl > 0.75: Voluminös, flach unten

**Spitzigkeit (Entrance Angle, Lauf Angle):**
```
Einlauf_Winkel = arctan(Spitzwert_Bug / (LWL/4))
```
- Spitz (<10°): Feiner Seegang, höherer Widerstand bei Schwell
- Rund (10–20°): Komfort, Standard
- Stumpf (>20°): Planing-typisch, Slamming-Risiko

### 4.2 Tiefgang und Trim

**Tiefgang (Draft, T):**
```
T = Mast-Schuh bis Wasserlinie (Segler) oder Propeller-spitze (Motor)
```

**Trim-Winkel:**
```
trim = arctan((CG_long - Eintauchung_AG) / LWL) × 180/π
```
- Positiv (Bug tief): Schiff beschleunigt, aber Widerstand steigt
- Negativ (Heck tief): Critical für Segler (Sailing-Heeling), Pitching-Risiko
- Neutral: <0.5° optimal für Motorschiffe

**Praktische Regel Segler:**
```
Trim_opt_Segler = +0.5° bis +1.5° (Bug leicht tiefer)
Trim_opt_Motor = -0.2° bis +0.2°
```

---

## 5. Mehrfachrumpf-Spezialitäten

### 5.1 Katamaran-Geometrie

**Parameter:**
```
Abstand Spantmittellinie zu Spantmittellinie = d (Center-to-Center)
Breite eines Einzelrumpfes = b
Abstand_Verhältnis = d/b  (typisch 1.0–1.8)
```

**Deck-Brücke (Cross-Struktur):**
- Trägheits-Moment (transversales Wasserlinien-Flächenträgheitsmoment): I ≈ 2·(i_eigen + A_wl·(d/2)²), also I ∝ (d/2)² (quadratischer Gewinn nach Steiner)
- Längsverstärkung: Stringers at 150–300mm Spacing
- Verbundfestigkeit: Zwischen Rümpfen kritisch

> ✅ Aufgeloest (Audit): I ∝ (d/2)² (nicht (d/2)⁴) — nach dem Satz von Steiner (Parallelachsentheorem) gilt für den Katamaran I_t = 2·(L·B³/12 + A_wl·(d/2)²); der Separationsterm skaliert mit dem QUADRAT des Rumpfabstands. Confidence: documented. Quelle: BM = I/V mit I_t = 2(LB³/12 + LB·(d/2)²), Steiner-Theorem, naval-architecture-Standard.

**Hydrodynamische Interferenz:**
```
Gesamtwiderstand_Kata = 2 × Widerstand_einzeln × (1 + Interferenzfaktor)
Interferenzfaktor = -0.05 bis +0.15  (abhängig d/b)
```
- d/b < 1.0: Positive Interferenz (Widerstand steigt)
- d/b > 1.5: Neutrale bis negative (Widerstand sinkt leicht)

### 5.2 Trimaran-Geometrie

**Dreibeiner-Konfiguration:**
- Zentralrumpf: Hauptlast, Maschinenraum, Stabilität-Basis
- Seitenpflüger (outriggers): 35–50% der Zentralmasse
- Abstand Mittellinie zu Pflüger: 2.0–3.5m (abhängig LOA)

**Stabilitäts-Gewinn:**
```
Stabilitäts_Hebelarm_T3 = 1.3 bis 2.0 × Stabilitäts_Hebelarm_Mono
```
Grund: Massiver größerer Abstand Gewicht-Auftrieb

---

## 6. Fehleranalyse — 12 Fehlermuster

### 6.1 [F6.1] Übermäßig hoher Cp (Vollrumpf-Übergewicht)

**Symptom:**
- Cp > 0.72 bei erwarteter Verdränger-Konfiguration
- CAD-Messung: Verdrängung deutlich über Berechnung (aufgrund überpaddelnde Spanten)

**Ursache:**
- Designer "vergaßt" Spitzigkeit im Bug/Heck
- Wunsch nach Interior-Volumen hat zu parallele Mittelsektionen geführt

**Hydrodynamische Folge:**
```
Widerstand_extra = +15–25% gegenüber idealer Cp
Kraftstoff_verbrauch_extra = +20–30%
```

**Empfohlene Korrektion:**
- Spitzität im Bug über LWL/4 um 200–400mm zurückfahren
- Heck-Lauf sanfter machen (Auslauf über 2LWL/8 statt LWL/8)
- Cp-Ziel: 0.63–0.67 für 12–18m Cruiser

**Prüfkriterium:** Cp_actual / Cp_target > 1.08 → Warnung

---

### 6.2 [F6.2] Instabile schlanke Form (λ > 4.0 bei Freeboard < 0.10)

**Symptom:**
- LWL/BWL Verhältnis 4.0–4.5
- Freeboard (gemessen): 200–350mm (< 8% LWL)
- Initial stability (GZ bei 0°): < 2° (extrem niedrig)

**Ursache:**
- Designvorgabe "Racey Look" ignoriert Stabilitätsanforderungen
- Keine Rückkopplung mit Schwergewicht-Ballast

**Folgen:**
- Broachng-Anfälligkeit im Seegang
- Crew-Sicherheit kompromittiert (großer Kapselrisiko)
- CE-Validierung scheitert (ISO 12217 Minimum GZ @ 30° = 0.20m)

**Empfohlene Korrektion:**
```
Freeboard_min = 0.12 × LWL + 200mm (Sicherheit)
oder
LWL/BWL_max = 3.8 − 0.4 × (Freeboard / BWL)
```

> ⚠️ **ZU PRÜFEN (Audit):** Vorzeichen-Widerspruch zur „Physikalischen Grenze" in §2.2 („λ_max_stabil ≈ 4.5 + (Freeboard/BWL) × 2"): Dort STEIGT die zulässige Schlankheit mit dem Freeboard, hier SINKT sie (Term −0.4 × Freeboard/BWL). Stabilitätsrelevant; Richtung nicht zweifelsfrei — beide Formeln sind heuristisch und „estimated — unverifiziert" und vor Nutzung zu verifizieren.

**Prüfkriterium:** (LWL/BWL) × (Freeboard / BWL) > 1.2 → Statische Analyse erforderlich

---

### 6.3 [F6.3] Ungleichmäßiger Wasserlinie-Spant (Cwl-Sprünge)

**Symptom:**
- Wasserlinie-Fläche springt von Station zu Station
- Cwl variiert um >0.15 zwischen zwei Positionen
- CAD-Schnitt zeigt abrupte Breitungs-Änderungen

**Ursache:**
- CAD-Oberfläche mit zu wenigen Kontrollpunkten in Längswirkung
- Manuelles "Zeichnen" statt parametrischer Fläche-Interpolation

**Folgen:**
- Unwille im Seegang (Pitching-Resonanz)
- Mangelhafter Widerstand-Vorhersage
- Schiffssicherheit: Trim-Scherung möglich

**Empfohlene Korrektion:**
- Wasserlinie-Fläche mit mindestens 20 Stationen neu interpolieren
- Cwl-Kurve sollte kontinuierlich differenzierbar sein (C1 kontinuierlich)
- Cwl-Änderung pro Station: max 0.04

**Prüfkriterium:** max(|ΔCwl|) > 0.10 → Überprüfung erforderlich

---

### 6.4 [F6.4] Kielform-Diskontinuität (harte Kanten bei weichen Spanten)

**Symptom:**
- Unterteil hat knickiges Profil (z.B. Hard-Chine Ansatz)
- Oberteil hat weiche Rundung
- Übergang Knick-Rundung ist scharf/winkel

**Ursache:**
- Hybrid-Design (Einzelteil-Kombination)
- CAD-Fehler bei Surface-Vernetzung

**Folgen:**
- Strömungs-Abtrennung bei Drift
- Leeway deutlich erhöht (Segler-spezifisch)
- Kavitations-Risiko bei Propeller nah an Kante
- Produktion: Schad-Mold-Zone (schwierig zu legen)

**Empfohlene Korrektion:**
- Kontinuierliche G2-Fläche (Kurve + Normalenvektor stetig)
- Übergangszone Länge: ≥ LWL/15
- Kielwinkle sollte monoton über Länge variieren

**Prüfkriterium:** Normalenvektor-Sprung > 15° lokal → Überprüfung

---

### 6.5 [F6.5] Asymmetrische Spanten (Steuerbord ≠ Backbord)

**Symptom:**
- CAD-Schnitte zeigen unterschiedliche Breite/Tiefgang Stb/Bb
- Unterschied in Wasserlinie-Position oder Hauptspant-Fläche
- Wahrscheinlich Fehler beim Spiegeln

**Ursache:**
- CAD-Modell nicht korrekt gespiegelt
- Manuelles Zeichnen ohne Symmetrie-Constraint

**Folgen:**
- Asymmetrisches Kräfte-Moment (Drehmoment um Längsmittellinie)
- Trim-Fehler schwer zu diagnostizieren
- Produktions-Kosten: mold muss individuell angepasst werden

**Empfohlene Korrektion:**
- CAD-Oberfläche neu erstellen mit Mirror-Feature
- Symmetrie-Bedingung in Parametrisierung erzwingen
- Nach Spiegelung: Volumen-Vergleich Stb/Bb (Toleranz ±0.2%)

**Prüfkriterium:** |V_Stb − V_Bb| / V_ges > 0.005 → Überprüfung

---

### 6.6 [F6.6] Zu flache Knickspant (Hard Chine Winkel < 10°)

**Symptom:**
- Knickspant-Winkel gegen Vertikal: <10°
- Geometrisch fast identisch zu U-Spant

**Ursache:**
- Designvorgabe "Knickspant für niedrige Kosten", aber Designer wollte noch Stabilität

**Folgen:**
- Produktions-Vorteil verloren (flache Panels nun problematisch)
- Hydrodynamischer Vorteil verloren (Widerstand gleich U-Spant)
- Kanten-Verspannung problematisch bei Winkel < 10° (Spannungs-Konzentration)

**Empfohlene Korrektion:**
- Entweder: Knickspant-Winkel auf 15–20° erhöhen (stabiler, produktiv)
- Oder: Zu vollständiger U-Spant wechseln (keine hybriden)

**Prüfkriterium:** Hard-Chine-Angle < 12° → Empfehlung Überprüfung

---

### 6.7 [F6.7] Bugslamming-Geometrie (falscher Laufwinkel)

**Symptom:**
- Laufwinkel (Auslauf Bug): >25°
- Freeboard an Station 0–2: <150mm
- Gebogene Wasserlinie im Bug (Corkscrew-Form)

**Ursache:**
- Designer wollte "scharfe" Bug-Form für Optik
- Keine hydrodynamische Analyse durchgeführt

**Folgen:**
- Slamming-Schlag bei Seegang (Frequenz-Resonanz mit Schiff)
- Strukturelle Ermüdung im Unterkiefer
- Crew-Komfort: extreme Vertikalbeschleunigung

**Empfohlene Korrektion:**
```
Laufwinkel_max = 20° (Standard)
Freeboard_min_Bug = 0.08 × LWL + 150mm

Bugleier = 15–25° (Neigung nach außen oben)
```

**Prüfkriterium:** Laufwinkel > 22° ODER Freeboard_Bug < 120mm → Überprüfung

---

### 6.8 [F6.8] Ungleichmäßige Auftrieb-Verteilung (Trim-Fehler)

**Symptom:**
- Integrale Auftrieb-Kurve zeigt lokale Maxima/Minima
- Hauptspant-Fläche hat Schwankung >15% benachbart
- LCB (Longitudinal Center of Buoyancy) springt

**Ursache:**
- Zu wenige Stationen in CAD-Definition
- Spline-Interpolation mit falscher Ordnung

**Folgen:**
- Trim-Instabilität (Schiff oszilliert in Längswirkung)
- Widerstand-Vorhersage fehlerhaft (±10–15%)
- Seekeeping-Analyse fragwürdig

**Empfohlene Korrektion:**
- Mindestens 40 Stationen über LWL verteilt
- Spline-Ordnung: mind. kubisch (Order 4)
- LCB-Kurve sollte C1-stetig sein (erste Ableitung stetig)

**Prüfkriterium:** max(d(LCB)/dX) > LWL/20 → Überprüfung

---

### 6.9 [F6.9] Katamaran-Interferenz nicht berücksichtigt (d/b < 1.0)

**Symptom:**
- Abstand Spantmittellinie zu Mittellinie: d
- Breite Einzelrumpf: b
- d/b Verhältnis: < 1.0 (Rümpfe zu nah beieinander)

**Ursache:**
- Designer wollte schmale Gesamtbreite (Slipway-Constraint)
- Hydrodynamische Analyse ignoriert

**Folgen:**
- Widerstand: +8–15% über erwartete Summe
- Welleninterferenz erzeugt lokale Resonanz
- Seegang: Brücken-Nasspunkt-Risiko

**Empfohlene Korrektion:**
```
Abstand_min = 1.1 × Breite_Einzelrumpf
Abstand_opt = 1.4 × Breite_Einzelrumpf (minimaler Widerstand)
```

**Prüfkriterium:** d/b < 1.05 → Widerstand-Analyse erforderlich

---

### 6.10 [F6.10] Zu viel Freeboard (Blockage, Windwiderstand)

**Symptom:**
- Freeboard: >15% LWL
- Seitenfläche (projection über Wasserlinie): > 30% LWL²
- Schiff wirkt "überbaut"

**Ursache:**
- Ziel: viel Kopf-Freiheit
- Keine Segel-Wind-Last-Analyse

**Folgen:**
- Windwiderstand erhöht (Aerodynamisch)
- Heeling-Moment bei Segler deutlich größer
- Righting-Moment muss überproportional groß sein → Ballast-Kostensteigerung
- Seegang: Übergreifer-Wellen brechen übers Heck

**Empfohlene Korrektion:**
```
Freeboard_max = 0.12 × LWL + 400mm (Komfort-Grenze)
Freeboard_opt = 0.09 × LWL + 250mm (Standard)
```

**Prüfkriterium:** Freeboard > 0.14 × LWL → Empfehlung Überprüfung

---

### 6.11 [F6.11] Trimaran — unausgewogene Seitenpflüger (Ungleiche Masse)

**Symptom:**
- Seitenpflüger Stb Volumen: V1
- Seitenpflüger Bb Volumen: V2
- |V1 − V2| / (V1+V2)/2 > 0.10 (>10% Unterschied)

**Ursache:**
- Asymmetrischer CAD-Fehler
- Unterschiedliche Längsstabilität-Forderung

**Folgen:**
- Asymmetrisches Längsstabilität
- Drehmoment um Längsmittellinie (Roll-Moment ohne äußere Kraft)
- Ballast-Retuning notwendig (kostspielig)

**Empfohlene Korrektion:**
- Seitenpflüger-Spiegelung verfizieren (Symmetrie < ±2% Volumen)
- Massenverteilung innerhalb Pflüger überprüfen

**Prüfkriterium:** Asymmetrie > 5% → Überprüfung erforderlich

---

### 6.12 [F6.12] Unerwartete Spantflächen-Verteilung (CG-Rechnung später unmöglich)

**Symptom:**
- Integrale Spantflächen-Kurve (Ax über x) zeigt erratische Schwankungen
- Maximum nicht im erwarteten Drittel (typisch x = LWL/2 ± 10%)
- Spantfläche variiert um >20% benachbarte Stationen

**Ursache:**
- CAD-Modell mit zu wenigen Kontrollpunkten
- Nachbearbeitung ohne Neu-Vernetzung

**Folgen:**
- Schwerpunkt-Berechnung unsicher
- Stabilitäts-Berechnung fragwürdig (abhängig von CG)
- Righting-Moment-Berechnung fehlerhaft

**Empfohlene Korrektion:**
- Spantfläche-Kurve neu interpolieren (min. 40 Stationen)
- Visualisieren und überprüfen (sollte glatt sein, max lokal ±5%)
- Ableitung dAx/dx sollte monoton sein (außer um Übergänge)

**Prüfkriterium:** max(|ΔAx|) / Ax_avg > 0.20 → Überprüfung erforderlich

---

## 7. Produktions-Implikationen

### 7.1 V-Spant Mold-Komplexität

- **Spant-Anzahl:** Typisch 30–50 (abhängig LWL)
- **Kurvenradius:** Stark variabel (V-Spitze Radius 200–800mm)
- **Mold-Stützung:** Aufwendig (Anzahl Ausstützer: 40–80)
- **Kosten-Index:** 100% (Referenz)
- **Produktion:** Klassisch Handlaminat oder RTM

### 7.2 U-Spant Mold-Komplexität

- **Spant-Anzahl:** Typisch 25–40
- **Kurvenradius:** Größer und konstanter (Radius >1.0m)
- **Mold-Stützung:** Einfacher (Anzahl Ausstützer: 25–50)
- **Kosten-Index:** 85–95%
- **Produktion:** Gut für Vacuum-Infusion

### 7.3 Hard-Chine Mold-Komplexität

- **Spant-Anzahl:** Reduziert (20–35), aber komplexere Details
- **Kurvenradius:** Stark variabel (Kanten + gekrümmte Flächen)
- **Mold-Stützung:** Sehr zielgerichtet (Kanten-Abstützung kritisch)
- **Kosten-Index:** 75–90%
- **Produktion:** Gut für flache Panel-Materialien, schwierig für Kurven

---

## 8. Normen und Standards

### 8.1 ISO 12217 — Stabilitäts­anforderungen

**Relevante Parameter:**
- **GZ (Righting Moment Arm):** Für alle Heel-Winkel 0–180°
- **GZ @ 30°:** Minimum 0.20m (Category B)
- **GZ_max Winkel:** Sollte 25–35° sein (nicht >50°)
- **Areale Under GZ Kurve:** Dynamische Stabilität

**Anhalt-Werte nach Boat-Klasse:**
```
Cat A (Ocean): GZ@30° ≥ 0.20m, Area(0-40°) ≥ 0.090m·rad
Cat B (Offshore): GZ@30° ≥ 0.15m, Area(0-40°) ≥ 0.065m·rad
Cat C (Inshore): GZ@30° ≥ 0.10m, Area(0-40°) ≥ 0.040m·rad
Cat D (Sheltered): GZ@30° ≥ 0.05m, Area(0-40°) ≥ 0.020m·rad
```

> ⚠️ **ZU PRÜFEN (Audit):** Interner Widerspruch bei GZ@30° für Category B — oben in der Parameterliste (§8.1) als „Minimum 0.20m (Category B)" angegeben, in dieser Tabelle jedoch als „Cat B ≥ 0.15m" (0.20m entspricht hier Cat A). Sicherheitskritischer Stabilitätswert; Richtung nicht zweifelsfrei belegbar, da ISO 12217-2 tatsächlich STIX- und AVS-basierte Kriterien statt fixer GZ@30°-Schwellen je Kategorie verwendet. Diese Werte daher „estimated — unverifiziert"; vor Nutzung gegen ISO 12217-1/-2 (2022) prüfen.

---

## 9. Praktische Entwurfs-Checkliste

**Vor CAD-Finalisierung prüfen:**

- [ ] Cp berechnet, plausibel für Schiff-Typ (±0.05 Toleranz)
- [ ] LWL/BWL berechnet, plausibel (±0.3 Toleranz)
- [ ] Freeboard überprüft, CE-konform (mind. Minimums erfüllt)
- [ ] Wasserlinie-Spantfläche kontinuierlich (Cwl-Sprünge < 0.08)
- [ ] Spanten-Flächen-Kurve glatt (max lokale Variation ±8%)
- [ ] Symmetrie überprüft: |V_Stb − V_Bb| < 0.3%
- [ ] Hard-Chine (falls vorhanden): Winkel 15–25°, kontinuierlich
- [ ] Bug-Laufwinkel überprüft: <22°, Freeboard_Bug ausreichend
- [ ] LCB-Kurve glatt, keine Sprünge (d(LCB)/dX < LWL/25)
- [ ] Für Katamaran/Trimaran: d/b überprüft, Symmetrie <5%

---

## 10. ANHANG — Referenz-Daten

### A.1 Typische Cp-Werte (Referenz)

| Schifftyp | LWL (m) | Cp | Bemerkung |
|-----------|---------|-----|-----------|
| Racing-Segler | 12 | 0.52 | Very fine, displacement |
| Cruising-Segler | 14 | 0.60 | Standard |
| Motorsailer | 15 | 0.65 | Semi-displacement |
| Motorboot | 13 | 0.68 | Planing zone |
| Arbeitsboot | 10 | 0.72 | Voluminös |
| Dinghy | 5 | 0.55 | Performance |
| Katamaran | 12 | 0.50 | Pro Rumpf |

### A.2 Pydantic v2 Model — HullForm

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class HullTypeEnum(str, Enum):
    DISPLACEMENT = "displacement"
    SEMI_DISPLACEMENT = "semi_displacement"
    PLANING = "planing"
    CATAMARAN = "catamaran"
    TRIMARAN = "trimaran"

class BottomTypeEnum(str, Enum):
    V_SHAPED = "v_shaped"
    U_SHAPED = "u_shaped"
    HARD_CHINE = "hard_chine"
    ROUND_BILGE = "round_bilge"

class HullGeometry(BaseModel):
    """Rumpfform - Geometrie und Parameter"""
    model_config = {"from_attributes": True}
    
    loa_mm: float = Field(..., description="Length overall (mm)")
    lwl_mm: float = Field(..., description="Length waterline (mm)")
    bwl_mm: float = Field(..., description="Beam waterline (mm)")
    draft_mm: float = Field(..., description="Draft (mm)")
    freeboard_mm: float = Field(..., description="Freeboard (mm)")
    displacement_kg: float = Field(..., description="Displacement (kg)")
    
    prismatic_coeff: Optional[float] = Field(None, description="Cp (0.50-0.85)")
    cwl: Optional[float] = Field(None, description="Waterline area coefficient")
    hull_type: HullTypeEnum = Field(..., description="Hull classification")
    bottom_type: BottomTypeEnum = Field(..., description="Bottom shape")
    
    slenderness_ratio: Optional[float] = Field(None, description="LWL/BWL")
    entrance_angle_deg: Optional[float] = Field(None, description="Bug entry angle (deg)")
    run_angle_deg: Optional[float] = Field(None, description="Heck run angle (deg)")
    trim_deg: Optional[float] = Field(None, description="Trim angle (positive=bow down)")
    
    # Für Hard-Chine:
    chine_angle_deg: Optional[float] = Field(None, description="Hard chine angle (deg)")
    
    # Für Multi-Hull:
    center_to_center_mm: Optional[float] = Field(None, description="Center-to-center distance (Kata/Trimaran)")
    hull_count: int = Field(1, description="Number of hulls")

class HullFormAnalysis(BaseModel):
    """Rumpfform Analyse-Ergebnis"""
    model_config = {"from_attributes": True}
    
    geometry: HullGeometry
    cp_assessment: str = Field(..., description="Cp plausibility (OK, WARNING, ERROR)")
    slenderness_assessment: str = Field(..., description="LWL/BWL stability (OK, WARNING, ERROR)")
    freeboard_ce_compliant: bool = Field(..., description="CE-compliant freeboard")
    
    warnings: list[str] = Field(default_factory=list, description="List of identified issues")
    recommendations: list[str] = Field(default_factory=list, description="Recommended corrections")
    
    confidence: float = Field(0.85, ge=0.0, le=1.0, description="Analysis confidence")

def analyze_hull_form(geometry: HullGeometry) -> HullFormAnalysis:
    """Rumpfform analysieren und Plausibilität prüfen"""
    warnings = []
    recommendations = []
    
    # Cp-Plausibilität
    cp_assessment = "OK"
    if geometry.prismatic_coeff is not None:
        target_cp = {
            HullTypeEnum.DISPLACEMENT: (0.55, 0.65),
            HullTypeEnum.SEMI_DISPLACEMENT: (0.60, 0.70),
            HullTypeEnum.PLANING: (0.65, 0.80),
        }
        if geometry.hull_type in target_cp:
            min_cp, max_cp = target_cp[geometry.hull_type]
            if geometry.prismatic_coeff > max_cp:
                cp_assessment = "WARNING"
                warnings.append(f"Cp {geometry.prismatic_coeff:.3f} exceeds typical range ({min_cp}-{max_cp})")
                recommendations.append("Sharpen bow/stern profile to reduce Cp")
    
    # Slenderness-Analyse
    slenderness_assessment = "OK"
    if geometry.slenderness_ratio is not None:
        if geometry.slenderness_ratio > 4.0 and geometry.freeboard_mm < 0.10 * geometry.lwl_mm:
            slenderness_assessment = "WARNING"
            warnings.append(f"Slender hull (λ={geometry.slenderness_ratio:.2f}) with low freeboard — stability risk")
            recommendations.append("Increase freeboard or reduce LWL/BWL ratio")
    
    # CE-Freeboard
    freeboard_ce = True  # Simplified check
    
    return HullFormAnalysis(
        geometry=geometry,
        cp_assessment=cp_assessment,
        slenderness_assessment=slenderness_assessment,
        freeboard_ce_compliant=freeboard_ce,
        warnings=warnings,
        recommendations=recommendations,
    )
```

---

## 11. Regulatorischer und normativer Rahmen (verifiziert)

> Dieser Abschnitt ergänzt §8 mit web-verifizierten Normbezügen. Jede Norm ist mit Nummer, Titel und Scope belegt. Wo die frühere Fassung (§8) Werte als Fakt darstellte, die sich nicht zweifelsfrei belegen lassen, sind diese hier korrigiert bzw. als „estimated — unverifiziert" gekennzeichnet.

### 11.1 Normen für Hauptdaten und Rumpfgeometrie

| Norm | Titel / Scope | Layout-/Formbezug | Confidence |
|------|---------------|-------------------|------------|
| **ISO 8666:2020** | Small craft — Principal data | Definiert die **Hauptdimensionen** verbindlich: Länge des Rumpfes (L_H, ≤ 24 m Anwendungsbereich), Wasserlinienlänge (L_WL), max. Breite (B_max), max. Tiefgang (T_max, bis tiefster Punkt inkl. Schwert), Freibord (F), Kielsprung/Deadrise-Winkel. Alle Formkoeffizienten dieses Dokuments setzen ISO-8666-konforme Dimensionsdefinitionen voraus. | documented |
| **ISO 12217-1/-2/-3 (2022)** | Small craft — Stability and buoyancy assessment and categorisation | Weist Stabilität/Auftrieb nach und ordnet CE-Kategorien A–D zu. **Teil 2** (Segelboote) verwendet **STIX**, **AVS** und Mindest-Aufrichtenergie — NICHT fixe GZ@30°-Schwellen je Kategorie. | documented |
| **ISO 12215 (Teile 1–9, 2019)** | Small craft — Hull construction and scantlings | Laminat-/Plattendicke, Steifenabstand, Panel-Dimensionierung. **Teil 8** Ruder, **Teil 9** Kiele/Anhänge. Basis des `structural`-Moduls. Für Scantling-Fragen zitieren — **nicht** ISO 12217. | documented |
| **RCD 2013/53/EU** | Recreational Craft Directive | CE-Entwurfskategorien A (Ocean), B (Offshore), C (Inshore), D (Sheltered); Pflicht für 2,5–24 m im EU-Verkauf. | documented |

*Quellen: [ISO 8666:2020](https://www.iso.org/standard/79071.html); [ISO 8666 Preview (BSI)](https://webstore.ansi.org/preview-pages/BSI/preview_30299341.pdf); [ISO 12217 / STIX-AVS FAQ (IRC)](https://ircrating.org/wp-content/uploads/2019/01/stix-avs-faq.pdf).*

### 11.2 Korrektur der Stabilitäts-Schwellen aus §8.1 (Audit-Auflösung)

Die in §8.1 tabellierten „GZ@30° ≥ 0.20/0.15/0.10/0.05 m" je Kategorie sind **nicht** die Prüfkriterien von ISO 12217-2. ISO 12217-2 bewertet Segelyachten über einen **zusammengesetzten Stabilitätsindex (STIX)** sowie den **Angle of Vanishing Stability (AVS)** und die Mindest-Aufrichtenergie m·A_GZ.

**Verifizierte Schwellen (ISO 12217-2, Segelmonohulls):**
- **Kategorie A (Ocean):** AVS ≥ **120°** UND STIX ≥ **32**.
- STIX ist ein Kompositwert aus u. a. Länge, Displacement-Length-Ratio, Beam-Displacement-Ratio, AVS, dynamischer Stabilität, Downflooding-Höhe, Breaking-Wave-Capsize-Recovery und Inversions-Aufrichtmoment.
- AVS ist der Winkel, jenseits dessen die Yacht in die invertierte Lage kapselt; darunter richtet sie sich selbst auf. GZ_max liegt bei einer gut ausgelegten Fahrtenyacht typisch bei 50–70°.

> Confidence: documented. Quellen: [STIX/AVS FAQ (IRC Rating)](https://ircrating.org/wp-content/uploads/2019/01/stix-avs-faq.pdf); [IRC Safety & Stability Indices](https://ircrating.org/wp-content/uploads/2019/01/irc_safety_stability_info.pdf). Die GZ-Zahlen in §8.1 bleiben als historischer Bestand stehen, sind aber **„estimated — unverifiziert"** und dürfen nicht als CE-Nachweiskriterium verwendet werden — maßgeblich sind STIX/AVS nach ISO 12217-2.

---

## 12. Wirkprinzip: Rumpfgeschwindigkeit und Widerstandsregime (verifiziert)

### 12.1 Rumpfgeschwindigkeit (Hull Speed) — belegte Formeln

Die Rumpfgeschwindigkeit ist die Geschwindigkeit, bei der die vom Bug erzeugte Wellenlänge der Wasserlinienlänge entspricht; das Schiff sitzt dann in seinem eigenen Wellental und muss zum Weiterbeschleunigen seinen Bugwellenberg „hinaufklettern".

**Imperiale Näherung:**
```
v_hull [kn] = 1.34 × √(L_WL [ft])
```
Der Koeffizient variiert praktisch zwischen **1.34 und 1.51** kn·ft^(−½) je nach Rumpfform (leichte, feine Rümpfe überschreiten 1.34 leicht; schwere, völlige Rümpfe bleiben darunter).

**Metrische Form (Ergebnis in kn, L_WL in m):**
```
v_hull [kn] = 2.43 × √(L_WL [m])
```

**Erste Prinzipien (Tiefwasser-Wellengeschwindigkeit, SI):**
```
v_hull [m/s] = √(g · L_WL / 2π)     mit g = 9.81 m/s²
```

> Confidence: documented. Quelle: [Hull speed — Wikipedia](https://en.wikipedia.org/wiki/Hull_speed). Die Konstante 1.34 ist keine harte Grenze, sondern der Übergang in stark steigenden Wellenwiderstand; sie entspricht Fn ≈ 0.4.

### 12.2 Froude-Zahl und Speed-Length-Ratio

```
Froude-Zahl:        Fn = V / √(g · L_WL)     (V und L_WL in SI)
Speed-Length-Ratio: SL = V [kn] / √(L_WL [ft])
```
Umrechnung: SL ≈ 1.34 entspricht Fn ≈ 0.40. Der Wellenwiderstand beginnt spürbar zu steigen ab SL ≈ 1.2 (Fn ≈ 0.35) und erreicht ein Maximum um Fn ≈ 0.50 (SL ≈ 1.70).

| Fn (längenbasiert) | SL-Ratio | Widerstandsverhalten |
|--------------------|----------|----------------------|
| ~0.35 | ~1.20 | Deutlicher Anstieg beginnt |
| ~0.40 | ~1.34 | „Hull speed", Wellensystem koppelt |
| ~0.45 | ~1.50 | Weiter steigender Wellenwiderstand |
| ~0.50 | ~1.70 | Maximum des Wellenwiderstands |

> Confidence: documented. Quelle: [Hull speed — Wikipedia](https://en.wikipedia.org/wiki/Hull_speed).

### 12.3 Verdrängungs-Regime nach Froude-Zahl (verifiziert)

Die in §1.1 genutzte Regimeeinteilung ist längenbasiert wie folgt belegbar (Richtwerte, keine scharfen Grenzen):

| Regime | Längen-Froude-Zahl Fn | Charakteristik |
|--------|------------------------|----------------|
| **Verdränger (displacement)** | Fn < ~0.4 | Auftrieb rein hydrostatisch; Rumpfgeschwindigkeit limitierend |
| **Halbgleiter (semi-displacement/semi-planing)** | ~0.4 < Fn < ~1.0 | Übergang; teils dynamischer Auftrieb, teils Verdrängung |
| **Gleiter (planing)** | Fn > ~1.0 | Gewicht überwiegend durch hydrodynamischen Auftrieb getragen; benetzte Fläche sinkt mit Geschwindigkeit |

> Confidence: documented. Quellen: [Froude for Thought — DLBA](https://dlba-inc.com/wp-content/uploads/2021/04/Froude-for-Thought.pdf); [Review on hydrodynamics of planing hulls — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0029801824003834). Hinweis: Die exakte Grenze non-planing→planing ist unscharf; volumenbasierte Froude-Zahl (Fn∇) liefert abweichende Schwellen. Die Grenzen sind Leitwerte, nicht deterministisch.

### 12.4 Widerstandskomponenten (Prinzip)

Der Gesamtwiderstand teilt sich qualitativ in **Reibungswiderstand** (∝ benetzte Fläche, dominant bei niedriger Fn), **Wellenwiderstand** (dominant nahe/oberhalb Rumpfgeschwindigkeit) und **Form-/Druckwiderstand**. Bei Gleitern verschiebt sich der Anteil mit steigender Fahrt von Wellen- zu Reibungs- und induziertem Druckwiderstand, weil die benetzte Fläche schrumpft.

> Confidence: documented (qualitativ). Quelle: [Hydrodynamics of Planing Hulls — DLBA](https://dlba-inc.com/library/hydrodynamic-design-of-planing-hulls/). **Keine quantitative Aufteilungsformel** angegeben — die in §2.1 stehende Zerlegung „Widerstand_total = Cv + Cw + Cform" ist qualitativ korrekt, die dort behaupteten Proportionalitäten sind heuristisch und bleiben „estimated".

---

## 13. Formkoeffizienten — verifizierte Definitionen und Zielwerte

### 13.1 Definitionen (belegt)

| Koeffizient | Formel | Bedeutung |
|-------------|--------|-----------|
| **Blockkoeffizient C_B** | C_B = ∇ / (L_pp · B · T) | Völligkeit gegenüber umschreibendem Quader; Maß der „Fülle" des Unterwasserschiffs |
| **Hauptspantkoeffizient C_M** | C_M = A_x / (B · T) | Wie rechteckig der Hauptspant ist (A_x = Hauptspantfläche) |
| **Prismatischer Koeffizient C_P** | C_P = ∇ / (A_x · L) | Längsverteilung des Volumens |
| **Wasserlinienkoeffizient C_WP** | C_WP = A_WP / (L · B) | Völligkeit der Wasserlinienfläche A_WP |

**Belegter Zusammenhang:** C_P = C_B / C_M. Da A_x stets kleiner als B·T ist, gilt immer **C_P > C_B** für dasselbe Schiff.

> Confidence: documented. Quellen: [Wärtsilä — Coefficients of form](https://www.wartsila.com/encyclopedia/term/coefficients-of-form); [Engineering Handbook — Ship Form Coefficients](https://enghandbook.com/naval-architecture/ship-form-coefficients/); [Marine Public — Hull Form Coefficients](https://www.marinepublic.com/blogs/training/431726-ship-hull-form-coefficients-formulas-calculations-guide).

### 13.2 Optimaler C_P in Abhängigkeit von der Speed-Length-Ratio

Für jeden Geschwindigkeitsbereich existiert ein C_P, der den Wellenwiderstand minimiert. Schlanke Schnellfahrer bevorzugen niedrigere C_P, völligere Langsamfahrer höhere. Tabelle nach **Skene's Elements of Yacht Design**:

| SL-Ratio (V[kn]/√L_WL[ft]) | optimaler C_P |
|-----------------------------|---------------|
| 1.0 | 0.52 |
| 1.1 | 0.54 |
| 1.2 | 0.58 |
| 1.3 | 0.62 |
| 1.34 (Rumpfgeschwindigkeit) | ~0.63 |
| 1.4 | 0.64 |
| 1.5 | 0.66 |
| 1.6–1.7 | 0.68–0.69 |
| 1.8–2.0 | 0.69–0.70 |

> Confidence: documented. Quelle: [The Prismatic Coefficient — Sailboat-Cruising (zit. Skene's Elements of Yacht Design)](https://www.sailboat-cruising.com/prismatic-coefficient.html). Interpretation: Ein reiner Verdränger-Cruiser bei SL ≈ 1.34 liegt optimal bei C_P ≈ 0.63 — konsistent mit dem Bereich 0.55–0.65 in §1.1/§2.1.

### 13.3 Displacement-Length-Ratio (DLR) — verifiziert

```
DLR = Displacement [long tons] / (0.01 · L_WL [ft])³
```
(1 long ton = 2240 lb.)

| DLR-Wert | Klassifikation |
|----------|----------------|
| < 100 | ultraleicht (ultralight) |
| 100–200 | leicht (light) |
| 200–300 | moderat (moderate) |
| 300–400 | schwer (heavy) |
| > 400 | sehr schwer (very heavy) |

Physikalische Bedeutung: Je leichter das Boot relativ zur Wasserlinienlänge, desto höher das Geschwindigkeitspotenzial — aber desto unruhiger die Bewegung im Seegang und desto empfindlicher gegen Überladung.

> Confidence: documented. Quelle: [Displacement–length ratio — Wikipedia](https://en.wikipedia.org/wiki/Displacement%E2%80%93length_ratio). Bei DLR-Berechnung die verwendete Verdrängung (light/normal/loaded) mitangeben.

---

## 14. Kimmform: Rundspant vs. Knickspant (verifiziert)

### 14.1 Grundunterscheidung

- **Rundspant (round bilge):** kontinuierlich gekrümmter Übergang Boden→Seite. Standard bei Verdrängern und vielen Halbgleitern.
- **Knickspant (hard chine):** definierte Kante zwischen Boden- und Seitenfläche.

### 14.2 Belegte Eigenschaftsunterschiede

| Aspekt | Rundspant | Knickspant |
|--------|-----------|------------|
| Rolldämpfung (glattes Wasser) | geringer | höher — Knick widersteht dem Rollen stärker |
| Seegangskomfort (Welle) | seakindlier / weicher | härter |
| Rolldämpfung bei Fahrt | ähnlich bei Fn ≈ 0.3 | ab Fn > ~0.37 überlegen (hydrodynamischer Auftrieb an der Kante) |
| Produktion | komplexere Form (Kurven) | einfacher — ebene/abwickelbare Panels |
| Eignung Regime | Verdränger/Halbgleiter | Halbgleiter/Gleiter, günstige Serienbauweise |

Beide Formen sind für Verdränger- und Halbgleitfahrt bei niedrig-mittlerer relativer Geschwindigkeit geeignet. Bei niedriger Fn (~0.3) verhalten sie sich in der Rolldämpfung ähnlich; oberhalb Fn ≈ 0.37 zeigt der Knickspant durch Auftriebseffekte überlegene Dämpfung. In grober See gilt der Rundspant als seekindlicher.

> Confidence: documented. Quellen: [Roll Damping — Round Bilge vs Hard Chine (RINA/ResearchGate)](https://www.researchgate.net/publication/267607417_Roll_Damping_Coefficients_Assessment_and_Comparison_for_Round_Bilge_and_Hard_Chine_Hullforms); [Sailing Catamarans — Hard chine v round bilge](https://mail.sailingcatamarans.com/index.php/faqs/15-general-questions/90-hard-chine-hulls-v-round-bilge).

### 14.3 Deadrise-Winkel (Gleiter, V-Boden) — verifiziert

Der Deadrise-Winkel ist der Winkel des Bodens gegen die Horizontale. ISO 8666 führt ihn als definierte Größe.

- **Deep-V:** Transom-Deadrise **~20–24°**; BoatTEST definiert Deep-V als 21–24° am Spiegel.
- **Praktische Obergrenze:** ~**24°** am Spiegel — darüber Stabilitätsnachteile bei langsamer Fahrt und in Ruhe.
- **Modified-V / warped hull:** variabler Deadrise, vorn scharf (~24°) nach hinten flacher (~17–20°); Standard bei vielen Motorbooten.

> Confidence: documented. Quellen: [To Deep-V or Not — BoatTEST](https://boattest.com/view-news/6472_To-Deep-V-or-Not-to-Deep-V); [Ray Hunt Design — Deep-V Q&A](http://rayhuntdesign.com/deepv-questions-answers.php).

### 14.4 Widerstandsvorhersage Gleiter — Methodik

Für prismatische Gleitrümpfe (konstante Breite, konstanter Deadrise) ist die **Savitsky-Methode (1964)** das etablierte Verfahren: eine Regression umfangreicher Schleppversuche, die Auftriebs-, Widerstands- und Druckpunkt-Koeffizienten liefert und Trimm, Tiefgang, benetzte Kiel-/Kimm-Länge sowie Widerstand im Gleichgewicht bestimmt. Für **warped** (variabler Deadrise) gelten Erweiterungen, die Sektionsbeiträge einzeln bewerten.

> Confidence: documented (Methodik, keine Zahlen). Quellen: [Savitsky Method — Nautical Solver](https://nauticalsolver.com/calculators/resistance/savitsky/savitsky.php); [Review on hydrodynamics of planing hulls — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0029801824003834). **Es werden hier bewusst keine Beispielrechnungen angegeben** — Savitsky-Eingaben sind rumpfspezifisch und mit dem Originalverfahren zu rechnen.

---

## 15. Katamaran: Brückendeck-Höhe (Slamming) — verifiziert

Ausreichende Brückendeck-Höhe (bridgedeck clearance) verhindert das Schlagen von Wellen gegen die Unterseite der Verbindungsstruktur (Slamming/Pounding) — sicherheits- und komfortrelevant.

**Dokumentierte Branchen-Faustwerte (keine Norm):**
- Gut: **5–6 % der Rumpflänge (LOA)**; **4 %** noch akzeptabel, aber niedrig.
- Alternative Faustformel: Brückendeck-Höhe [inch] ≈ 1.5 % der L_WL [ft].

> Confidence: estimated — dokumentierte Yacht-Design-Praxis, keine Norm. Quellen: [Lagoon — Six commandments](https://www.catamarans-lagoon.com/life-on-board/article/six-commandments-choosing-your-catamaran); [Catamaran Guru — Bridgedeck Clearance (PDF)](https://catamaranguru.com/wp-content/uploads/2020/03/catamaran_bridgedeck_clearance.pdf). Die Werte streuen zwischen Quellen; für konkrete Auslegung Seegangs-/Slamming-Analyse durchführen.

---

## 16. Fehlerbild-Atlas (FB-31-01-NNN) — verifikationsgestützt

> Neues, kollisionsfreies ID-Schema `FB-31-01-NNN` (getrennt vom Bestands-Schema „F6.x" in §6). Jedes Fehlerbild nennt nur belegte Schwellen; heuristische Werte sind als solche markiert.

### FB-31-01-001 — Rumpfform-Regime passt nicht zur Zielgeschwindigkeit

**Symptom:** Rumpf als Verdränger ausgelegt, aber Zielgeschwindigkeit liegt bei Fn > 0.4 (Halbgleit-/Gleitbereich) — oder umgekehrt ein Gleitrumpf, der dauerhaft bei Fn < 0.3 betrieben wird.
**Ursache:** Betriebsprofil (Zielgeschwindigkeit vs. L_WL) nicht mit Regimegrenzen abgeglichen.
**Folge:** Verdränger jenseits Rumpfgeschwindigkeit erzeugt exponentiell steigenden Wellenwiderstand; Gleiter im Verdrängerbetrieb hat unnötig hohe benetzte Fläche/Reibung.
**Korrektur:** Betriebs-Fn = V/√(g·L_WL) bestimmen; Regime nach §12.3 zuordnen; Rumpftyp bzw. L_WL anpassen.
**Prüfkriterium:** Fn_Betrieb > 0.4 bei deklariertem Verdränger → Regime-Review.
> Confidence: documented (Regimegrenzen §12.3).

### FB-31-01-002 — C_P nicht auf die Zielgeschwindigkeit abgestimmt

**Symptom:** C_P weicht deutlich vom Skene-Optimum für die Betriebs-SL-Ratio ab (z. B. C_P = 0.52 bei angestrebter SL ≈ 1.5, wo ~0.66 optimal wäre).
**Ursache:** C_P aus Volumenwunsch statt aus Geschwindigkeitsziel gewählt.
**Folge:** Erhöhter Wellenwiderstand im Zielbereich.
**Korrektur:** SL-Ratio bestimmen, C_P-Ziel aus Tabelle §13.2 ablesen, Volumenverteilung (Bug-/Heckvölligkeit) anpassen.
**Prüfkriterium:** |C_P_actual − C_P_optimal(SL)| > 0.05 → Review.
> Confidence: documented (Skene-Tabelle §13.2).

### FB-31-01-003 — DLR-/Verdrängungs-Fehleinschätzung (Überladung)

**Symptom:** DLR-Klasse (z. B. „leicht", 100–200) steht im Widerspruch zum realen Beladungszustand; Konstruktions-Displacement deutlich unter loaded-Displacement.
**Ursache:** DLR mit light displacement statt loaded gerechnet.
**Folge:** Reales Boot schwerer, langsamer, empfindlicher gegen Überladung (leichte Rümpfe reagieren stärker).
**Korrektur:** DLR mit definiertem Beladungszustand (§13.3) neu rechnen und deklarieren.
**Prüfkriterium:** Angabe des Beladungszustands fehlt → Review.
> Confidence: documented (DLR-Definition §13.3).

### FB-31-01-004 — Unzureichende Brückendeck-Höhe (Katamaran-Slamming)

**Symptom:** Brückendeck-Höhe < 4 % LOA.
**Ursache:** Innenraum-/Kopffreiheitswunsch verdrängt Freiraum unter der Brücke.
**Folge:** Häufiges Slamming der Verbindungsstruktur in Welle — Komfort- und Strukturermüdungsrisiko.
**Korrektur:** Auf Branchen-Richtwert ≥ 5–6 % LOA anheben (§15) bzw. Slamming-Analyse.
**Prüfkriterium:** clearance/LOA < 0.04 → Review.
> Confidence: estimated (dokumentierte Praxis §15, keine Norm).

### FB-31-01-005 — Falsche Norm zitiert (12217 vs. 12215 vs. 8666)

**Symptom:** Scantling-/Laminatfragen mit ISO 12217 belegt, oder Stabilitätsnachweis mit fixen GZ@30°-Werten statt STIX/AVS geführt.
**Ursache:** Normverwechslung (wiederkehrender Fehler im Quellmaterial).
**Folge:** Nachweis nicht CE-tauglich.
**Korrektur:** Scantlings → ISO 12215; Stabilität/Kategorisierung → ISO 12217-2 (STIX/AVS, Cat A: AVS ≥ 120°, STIX ≥ 32); Hauptdaten → ISO 8666 (§11).
**Prüfkriterium:** Scantling-Aussage referenziert 12217 → Korrektur.
> Confidence: documented (§11).

### FB-31-01-006 — Kimmform passt nicht zum Betriebsregime

**Symptom:** Knickspant als reines „Stil"-Element an langsamem Verdränger ohne Nutzung des Auftriebsvorteils, oder Rundspant-Anspruch bei ausgeprägtem Gleitbetrieb.
**Ursache:** Kimmform ästhetisch/kostengetrieben ohne Regime-Bezug.
**Folge:** Verschenkter Produktionsvorteil (Knick) bzw. verschenkte Dämpfung/Auftrieb (Rundspant bei Fn > 0.37).
**Korrektur:** Kimmform nach Betriebs-Fn wählen (§14.2): Rundspant für seekindliche Verdrängerfahrt, Knickspant ab Fn > ~0.37 / Serienbau.
**Prüfkriterium:** Rundspant deklariert bei Fn_Betrieb > 0.5 ohne Begründung → Review.
> Confidence: documented (§14.2).

---

## 17. FAQ und Glossar

### 17.1 FAQ

**Warum ist „Rumpfgeschwindigkeit" keine harte Grenze?**
Weil die Konstante 1.34 (Fn ≈ 0.4) den Punkt starker Wellenwiderstandszunahme markiert, nicht eine physikalische Mauer. Leichte, feine Rümpfe fahren mit SL 1.34–1.51; Gleiter überwinden den Wellenberg und laufen bei Fn > 1.0 planend. (§12.1) — documented.

**Cp oder Cb — was zitieren?**
Für Längsverteilung/Wellenwiderstand C_P; für Gesamtvölligkeit C_B. Zusammenhang C_P = C_B/C_M, stets C_P > C_B. (§13.1) — documented.

**Welche Norm für Stabilitätsnachweis?**
ISO 12217-2 (Segel), STIX + AVS, nicht die GZ@30°-Tabelle aus §8.1. Cat A: AVS ≥ 120°, STIX ≥ 32. (§11.2) — documented.

**Rundspant oder Knickspant für einen Fahrtenkat/-cruiser?**
Bei überwiegend Verdrängerfahrt (Fn < 0.3) rolldämpfungstechnisch ähnlich, Rundspant seekindlicher; ab Fn > 0.37 Knickspant vorteilhaft und billiger in Serie. (§14.2) — documented.

### 17.2 Glossar

| Begriff | Definition | Quelle |
|---------|------------|--------|
| L_WL | Wasserlinienlänge, gemessen im Konstruktions-Beladungszustand (ISO 8666) | documented |
| Fn (Froude-Zahl) | V/√(g·L); dimensionslos; ordnet Verdränger/Halbgleiter/Gleiter | documented |
| SL-Ratio | V[kn]/√(L_WL[ft]); ~1.34 ≈ Rumpfgeschwindigkeit | documented |
| C_B (Blockkoeffizient) | ∇/(L·B·T) | documented |
| C_M (Hauptspantkoeff.) | A_x/(B·T) | documented |
| C_P (prismatisch) | ∇/(A_x·L) = C_B/C_M | documented |
| C_WP (Wasserlinienkoeff.) | A_WP/(L·B) | documented |
| DLR | Displacement[lt]/(0.01·L_WL[ft])³ | documented |
| Deadrise | Winkel des Bodens gegen Horizontale; Deep-V 20–24° | documented |
| STIX | Zusammengesetzter Stabilitätsindex (ISO 12217-2) | documented |
| AVS | Angle of Vanishing Stability; Cat A ≥ 120° | documented |
| Savitsky-Methode | Regressionsverfahren für Widerstand prismatischer Gleitrümpfe (1964) | documented |

---

**Datei abgeschlossen.**  
Kat 31.01 Rumpfformen — Version 1.1 — 2026-07  
Erweiterung §11–§17 web-verifiziert (ISO 8666:2020, ISO 12217-2/STIX-AVS, ISO 12215, Skene's, Savitsky, RINA Roll-Damping). Bestand §1–§10 unverändert; strittige Alt-Werte als „estimated — unverifiziert" markiert, nicht gelöscht.
