# 31_12 — Laminatplan

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Laminatplan  
**Version:** 2.0  
**Stand:** 2026-05-18  
**Relevanz:** Kern-Konstruktionswissen für Festigkeit, Haltbarkeit, Kosten-Optimierung

---

## Übersicht

Der Laminatplan definiert **Faser-Orientierung**, **Schichtfolge**, **Kern-Materialien** und **Harz-Systeme** — entscheidend für Boot-Festigkeit, Gewicht und Langlebigkeit. AYDI analysiert Laminate unter Segel- und Motorbelastung, Delaminierungs-Risiken und Fertigungsfehlererkennung.

**Fehleranalyse-Schwerpunkte:**
1. Faser-Orientierung ungünstig (zu viel 0°, zu wenig ±45°)
2. Kern-Auswahl zu schwach (billige Materialien, schnelle Ermüdung)
3. Laminat-Dicke ungleichmäßig (Schwachstellen entstehen)
4. Harz-Gehalt zu hoch (schwach, spröde) oder zu niedrig (porös, Wasser-Eindringung)
5. Delaminierung zwischen Schichten (Fertigungsfehler oder Wassereindringung)
6. Biaxial-Gewebe ungleichmäßig verteilt (unausgewogene Festigkeit)
7. Kern-Delaminierung (Sandwich-Boot, Wellen-Ausbeulung)
8. UV-Schädigung des Oberflächenlaminats
9. Mikrorisse durch Über-Spannung
10. Falsche Faser-Länge (zu kurz = geringe Festigkeit)
11. Harz-Blasen oder Hohlräume im Laminat
12. Nicht-Uniform-Laminat (Dicke variiert >3 mm über Länge)

---

## 1. Laminat-Grundprinzipien und Faser-Kombinationen

### 1.1 Faser-Typen und Eigenschaften

**E-Glass (Standard):**

```
Eigenschaften:
  E-Modul: 72 GPa (moderat)
  Zugfestigkeit: 3,4 GPa (gut)
  Dichte: 2,58 g/cm³ (höher, schwerer)
  Kosten: EUR 5–8 pro kg
  Verfügbarkeit: hervorragend (Standard)

Gewebe-Typen:
  CSM (Chopped Strand Mat): kurze Fasern (25–50 mm), Richtung zufällig
    → isotrope Festigkeit, aber niedrig
    → Nachteil: bei statischer Last wenig Effizienz
    → Vorteil: einfach zu verarbeiten, gutes Haftvermögen
    
  Woven (Gewebestoff): lange Fasern, 0° + 90° angeordnet
    → hohe Festigkeit in beiden Richtungen
    → Nachteil: weniger ±45° (Torsions-Steifheit gering)
    → Vorteil: gleichmäßig, hohe Güte
    
  Roving (Langfaser): sehr lange, parallele Fasern
    → höchste Zugfestigkeit (wenn in Richtung)
    → Nachteil: nur 0° Richtung nutzbar
    → Vorteil: max. Performance/Gewicht
```

**S-Glass (Performance):**

```
Eigenschaften:
  E-Modul: 85 GPa (höher als E-Glass)
  Zugfestigkeit: 4,6 GPa (höher, 35% über E-Glass)
  Dichte: 2,49 g/cm³ (etwas leichter)
  Kosten: EUR 15–25 pro kg (3–4× teurer)
  Verfügbarkeit: limitiert (Spezial-Hersteller)

Verwendung: Racing-Boote, High-Performance-Designs
Nachteil: sehr kostspielig für Standard-Production
```

**Kevlar (Aramid-Faser):**

```
Eigenschaften:
  E-Modul: 130 GPa (sehr hoch)
  Zugfestigkeit: 3,6 GPa (ähnlich E-Glass)
  Dichte: 1,45 g/cm³ (sehr leicht, -44% vs. E-Glass)
  Kosten: EUR 30–50 pro kg (6–10× teurer!)
  Problem: schwach auf Druck (faserweise Knickung)

Verwendung: Rennboote, Leistungs-orientiert
Praxis: oft hybrid mit E-Glass (Kevlar äußen für Leichtigkeit, Glass innen für Druckfestigkeit)
```

**Kohlefaser (Carbon):**

```
Eigenschaften:
  E-Modul: 230 GPa (extremhoch)
  Zugfestigkeit: 3,5 GPa
  Dichte: 1,60 g/cm³ (leicht)
  Kosten: EUR 50–150 pro kg (sehr teuer!)
  Problem: Leitfähigkeit (Blitzschlag-Risiko), Sprödheit

Verwendung: extreme High-Performance, Superyachten
Praxis: selten auf Segelbooten (Kosten/Nutzen-Verhältnis schlecht)
```

### 1.2 Gewebemuster und Orientierung

**Unidirektional (0°):**

```
Struktur: Alle Fasern parallel, eine Richtung
Festigkeit: Maximum in 0°-Richtung (bis 150% über Biaxial)
Festigkeit senkrecht: negligible
Anwendung: Ballast-Pocket, Mastfuß, Kiel-Schaft (Längs-Last)
```

**Biaxial (0°/90°):**

```
Struktur: Fasern zu 50% horizontal, 50% vertikal
Festigkeit: gleich in beiden Achsen (isotropie)
Effektivität: ~70% der unidirektionalen Festigkeit (pro Richtung)
Anwendung: Schiffe-Rumpf (Biegung + Torsion nötig)
Standard-Gewicht: 300–450 g/m²
```

**Quad-Axial (0°/45°/-45°/90°):**

```
Struktur: vier Faser-Richtungen
Torsions-Steifheit: sehr hoch (+30% vs. Biaxial)
Festigkeit: gut in allen Richtungen
Anwendung: Mast, Boom, Strukturbauteile
Kosten: EUR 15–25 pro m² (vs. EUR 8–12 Biaxial)
```

**Mattengewebe (CSM):**

```
Struktur: kurze Fasern (2–5 cm), Richtung zufällig
Zugfestigkeit: niedrig (20–40% von Woven)
Vorteil: isotrope (gleichmäßige) Festigkeit
Nachteil: ineffizient strukturell
Anwendung: erste Lage (Haftvermögen), ausgleichende Lagen

Standard-Gewicht: 300 g/m²
```

---

## 2. Laminat-Schichtfolge und Designmethode

### 2.1 Standard-Schichtfolge für Rumpf (Segelboot 12m)

**Schicht-für-Schicht Aufbau (von außen nach innen):**

```
Layer 1: Gelcoat 0,5–0,8 mm
  Funktion: UV-Schutz, ästhetik, Wasser-Barrier
  Material: Polyester oder Epoxy (Epoxy besser haltbar)
  Dicke: 0,5 mm min (dünn) bis 1,0 mm (solide Finish)
  
Layer 2: CSM 300 g/m² → ~1,5 mm
  Funktion: Haftvermögen (Gelcoat haftet auf CSM besser)
  Material: Chopped Strand Mat (kurze Fasern)
  Zweck: auch als Resin-Barriere (Wasserschutz)
  
Layer 3–4: Biaxial Woven 450 g/m² → ~2,5 mm (2 Lagen)
  Funktion: Haupt-Festigkeit (Längskraft + Querkraft)
  Material: Glas E-Glass, Standard
  Orientierung: 0°/90° (gleich beide Richtungen)
  
Layer 5: CSM 300 g/m² → ~1,5 mm
  Funktion: Übergang zum Kern (wenn Sandwich) oder nächste Woven
  
Layer 6–7: Biaxial Woven 450 g/m² → ~2,5 mm (2 Lagen)
  Funktion: Haupt-Festigkeit Innenseite
  
Layer 8: CSM 300 g/m² → ~1,5 mm
  Funktion: Abschluss, Haftvermögen für weitere Systeme

Optional Kern (Sandwich-Konstruktion):
  Schaumkern PVC (H-100 oder H-200): 25–40 mm
  
Laminate Innen-Seite (symmetrisch zu Außenseite):
  Nochmal Biaxial + CSM + Biaxial (Spiegelbild Außenseite)

TOTAL Dicke (ganzlaminate):
  Außen-Laminate: 12 mm
  + Innen-Laminate: 12 mm
  = 24 mm gesamt (oder ~20 mm mit Druck)
  
TOTAL Dicke (Sandwich):
  Außen-Laminate: 8 mm
  + Kern: 30 mm
  + Innen-Laminate: 8 mm
  = 46 mm gesamt (aber 40% weniger Gewicht als Ganzlaminate!)
```

**Harz-Gehalt und Faser-Volumen:**

```
Standard-Verhältnis:
  Faser-Volumen: 35–45% (ideal: 40%)
  Harz-Volumen: 55–65% (ideal: 60%)
  
Effekt von zu viel Harz (>65%):
  Laminat wird schwach (Harz ist schwächer als Faser)
  Gewicht erhöht sich
  Teurer (Harz ist Verschwendung)
  
Effekt von zu wenig Harz (<55%):
  Faser nicht "genetzt" → Lufteinschlüsse
  Niedrige Feuchteschranke (Wasser eindringen)
  Porenbildung
```

### 2.2 Optimierter Laminatplan für Performance (Racing-Boot 12m)

**Fokus: Leichtigkeit + Festigkeit**

```
Layer 1: Gelcoat Epoxy 0,6 mm (besser UV-beständig)
  
Layer 2: CSM 300 g/m² → ~1,5 mm
  
Layer 3–4: Biaxial S-Glass 400 g/m² → ~2,2 mm (2 Lagen)
  (S-Glass statt E-Glass: +35% Festigkeit bei nahezu gleicher Dichte, ~2,49 vs. 2,58 g/cm³; Laminat ~20% leichter durch höhere Festigkeit, nicht durch geringere Faserdichte)
  
Layer 5: CSM 200 g/m² → ~1,0 mm (dünnere Übergangsschicht)

Layer 6–7: Quad-Axial E-Glass 600 g/m² → ~3,5 mm (1 Lage)
  (0°/45°/-45°/90°: bessere Torsions-Steifheit)
  
Layer 8: CSM 200 g/m² → ~1,0 mm

CORE (optional): PVC H-200 35 mm (dünner, aber schwer)

Innen-Spiegelbild (etwas dünn möglich, nur 70% Außenseite):
  Biaxial S-Glass 400 × 1 Lage → ~2,2 mm
  CSM 200 × 1 Lage → ~1,0 mm

TOTAL Gewicht (Ganzlaminate): -40% vs. Standard
Kosten: +60% (teurere Fasern + Quad-Axial)
Performance-Gewinn: ~0,5–1,0 kn Geschwindigkeit (für Racing relevant)
```

### 2.3 Budget-Laminat für Production-Boot

**Fokus: Kosten-Reduktion, akzeptable Qualität**

```
Layer 1: Polyester Gelcoat 0,5 mm (billig)

Layer 2: CSM 300 g/m² → ~1,5 mm

Layer 3: Biaxial Woven 400 g/m² → ~2,2 mm (nur 1 Lage statt 2!)

Layer 4: CSM 300 g/m² → ~1,5 mm (wieder aufbauen)

Layer 5: Biaxial Woven 400 g/m² → ~2,2 mm (1 Lage)

Layer 6: CSM 300 g/m² → ~1,5 mm

TOTAL DICKE: 10–11 mm (vs. 12+ mm Standard)
Gewicht: -20% vs. Standard
Festigkeit: -15% (akzeptabel, Sicherheitsmarge still gut)
Kosten: -30% (weniger Material)

Problem: Dünn-Grenze. Unter 10 mm → Risiko-Zone
  → Bruch bei Grounding
  → Osmotic Blistering schneller
  → Reparatur-Schwierigkeit nimmt zu
```

---

## 3. Kern-Materialien für Sandwich-Konstruktion

### 3.1 PVC-Schaum (Divinycell, Herex)

**Charakteristik:**

```
Dichte-Klassen:
  H-60: 60 kg/m³ (weich, Budget)
  H-100: 100 kg/m³ (Standard, gutes Balance)
  H-200: 200 kg/m³ (steif, teure Boote)
  
Festigkeit (Kompression, ASTM D1621):
  H-100: 2,0 MPa (verifiziert DIAB TDS — siehe Abschnitt 11.2)
  H-200: 5,4 MPa (verifiziert DIAB TDS — siehe Abschnitt 11.2)
  
Scherung (shear strength, ASTM C273):
  H-100: 1,6 MPa (verifiziert DIAB TDS)
  H-200: 3,5 MPa (verifiziert DIAB TDS)
  
Vorteil: chemische Beständigkeit (Salzwasser, UV), leicht
Nachteil: Temperatur-abhängig (über 70°C verliert Festigkeit)
```

> ✅ **Aufgelöst (Audit):** H-100 Druck 2,0 MPa / Schub 1,6 MPa; H-200 Druck 5,4 MPa / Schub 3,5 MPa (ASTM D1621 / ASTM C273). Die früheren Werte (H-100 Druck 0,5 / Schub 0,3; H-200 Druck 1,2 / Schub 0,8 MPa) unterschätzten die reale Kernfestigkeit um Faktor 3–4 und waren falsch; Codeblock oben korrigiert. Vollständige Referenztabelle siehe Abschnitt 11.2. Confidence: **documented**. Quelle: DIAB Divinycell H TDS (diabgroup.com; reinforcedplasticslab.net Divinycell H Rev.23 SI).

**Verwendung nach Boot-Bereich:**

```
Rumpf-Seiten: H-100 (gutes Verhältnis Gewicht/Steifheit)
Boden: H-200 (höhere Last durch Wasser-Druck)
Decks: H-80 oder H-100 (weniger Druck, leichter)
Kiel-Ansatz: keine Kern (Massenlast → Ganzlaminate)

Dicke-Auswahl:
  Kleine Yacht (8–10m): 25–30 mm
  Mittel (12–16m): 30–40 mm
  Große (18m+): 40–50 mm
  
  Rule of Thumb: 20–30 mm Kern = Starrheit doppelt vs. Ganzlaminate (halbes Gewicht)
```

### 3.2 Balsa (Naturholz)

**Charakteristik:**

```
Dichte: 140 kg/m³ (ähnlich H-100 PVC, aber Naturstoff)
Festigkeit: höher als H-100 (Holz-Struktur)
Problem: Feuchte-Empfindlichkeit (quellung, Verfaulung)

Vorteil: traditionell, Bio-abbaubar, gute Festigkeit
Nachteil: komplexe Behandlung (Versiegelung erforderlich), teuer
Moderne Verwendung: selten (meist nur Heritage-Boote, Klassiker)
```

### 3.3 Polyurethan (PUR) und Polymethacrylimid (PMI)

**Polyurethan (Rigid PUR):**

```
Dichte: 80–120 kg/m³ (leicht)
Scherfestigkeit: 0,2–0,4 MPa (etwas niedrig)
Vorteil: sehr leicht, hohe Temp-Beständigkeit (bis 120°C)
Nachteil: teuer, nicht häufig auf Standard-Booten

Anwendung: Racing-Katamarane, Masten, Booms
```

**Polymethacrylimid (PMI, "Rohacell"):**

```
Dichte: 75–110 kg/m³ (sehr leicht)
Scherfestigkeit: bis 0,8 MPa (sehr gut für Gewicht)
Vorteil: hohe Temp-Resistenz (bis 140°C)
Nachteil: sehr teuer (EUR 50–100 pro kg)

Anwendung: höchste Performance (Superyacht, Racing)
```

---

## 4. Harz-Systeme und Verarbeitung

### 4.1 Polyester-Harz (Standard)

**Charakteristik:**

```
Verwendung: 70% aller Boote, Production-Standard
E-Modul: 3,5 GPa (moderat)
Zugfestigkeit: 60–85 MPa
Preis: EUR 3–5 pro kg (günstig)
Aushärtung: Raumtemperatur (Initiatoren nötig)

Nachteil: Wasser-Aufnahme (hygroscopisch)
  → nach 5–10 Jahren Feuchte-Eindringung
  → osmotische Blasenbildung (Gelcoat-Herausfallen)
  
Verarbeitung: Säure-Geruch (Styrol), einfach zu arbeiten
```

### 4.2 Epoxy-Harz (Premium)

**Charakteristik:**

```
Verwendung: 25–30% der modernen Boote (Racing, Custom)
E-Modul: 4,5–5,0 GPa (höher als Polyester)
Zugfestigkeit: 70–90 MPa (besser)
Preis: EUR 8–15 pro kg (2–3× teurer)
Aushärtung: mit Härter (2-Komponenten-System)

Vorteil: Wasserfestigkeit (-90% Feuchte-Aufnahme vs. Polyester)
  → Lebensdauer 20+ Jahre (vs. 10–15 Polyester)
  → kein osmotisches Blistering
  → besser für Salzwasser
  
Nachteil: höhere Kosten
           komplexere Verarbeitung (genaue Ratio nötig)
           längere Aushärtung (oft 7 Tage für volle Festigkeit)

Weitere Epoxy-Arten:
  Vinylester: Hybrid (zwischen Polyester + Epoxy), EUR 5–8/kg
    → besser chemische Resistenz, Kosten-Mittelweg
```

### 4.3 Harz-Verhältnis und Aushärtung

**Laminat-Qualität nach Harz-Gehalt:**

```
Zu wenig Harz (<50%):
  Fasern nicht vollständig "gebunden"
  → Luft-Einschlüsse, Porenbildung
  → Wasser-Eindringung möglich
  → Visuelle Anzeichen: rauhe Oberfläche, Fasern sichtbar

Optimal (55–60%):
  Alle Fasern vollständig durchdränkt
  → dichte, glatte Struktur
  → hohe Festigkeit
  → gute Langzeitstabilität

Zu viel Harz (>65%):
  Überfluss-Harz = totes Gewicht (schwächer)
  → Gewicht erhöht, Festigkeit gleich oder schlechter
  → teurer (Material-Verschwendung)
  → optisch: glatter, aber schwächer innen
```

**Aushärtungs-Prozess (Polyester):**

```
Schritt 1: Initiatoren + Katalysatoren vermischen
  Menge: typisch 1–2% MEKP (Methylethylketon-Peroxid)
  Zeit: 5–15 Minuten Verarbeitungszeit (vor Aussetzen!)
  
Schritt 2: Exothermer Prozess (Wärmeerzeugung)
  Temperatur-Steigerung: 20°C auf 60–80°C über 20–30 Minuten
  Peak-Temperatur abhängig Menge + Dicke (dickere Laminat = heißer!)
  
Schritt 3: Wärmekontrolle
  Zu schnell: interne Spannungen (Risse-Risiko)
  Zu langsam: schlechte Aushärtung (Adhäsions-Probleme)
  Ideal: kontrolliertes Ansteigen über 1–2 Stunden
  
Schritt 4: Aushärtung nach Verarbeitung
  Nach Verarbeitung: noch 24 Stunden weich
  Nach 7 Tagen: 90% Festigkeit erreicht
  Nach 28 Tagen: 100% Festigkeit (Langzeitstabilität)
```

---

## 5. Laminat-Defekte und Fertigungsfehler

### 5.1 Häufige Fehlerbild im Laminat

**Fehler 1: Hohlräume / Blasen (Voids)**

```
Ursache:
  - Luft eingeschlossen während Wicklung (schlechte Vakuum)
  - Harz-Verhältnis zu niedrig
  - Feuchtigkeit in Fasern (Fasern nicht vorgetrocknet)
  
Symptome:
  - visuelle Dellen auf Gelcoat-Oberfläche
  - Ultraschall-Test zeigt unterschiedliche Dicken
  - Klopftest: hohler Sound statt dumpfer
  
Auswirkung:
  - Lokal reduzierte Festigkeit (-30–50% im Fehler-Bereich)
  - Wasser-Eindringung (Blasen sind Pfade)
  - Delaminierungs-Risiko
  
Prävention:
  - Vakuum-Bagging verwenden (beste Methode)
  - Feuchtigkeit-Kontrolle (Lagerbedingungen <50% RH)
  - Schicht-Kontrolle während Verarbeitung
```

**Fehler 2: Delaminierung (Schichten trennen sich)**

```
Ursache:
  - Unzureichende Harz-Infiltration zwischen Schichten
  - Falsch platzierte Harz-Zwischenlagen
  - Verschmutzung (Öl, Staub) auf Faser-Oberfläche
  
Symptom:
  - Blase in Gelcoat (kann Jahre später auftreten, Wasser-Weg)
  - Ultraschall-Prüfung zeigt Lücke zwischen Lagen
  - Röntgen: deutlich sichtbar (Schwarzer Schatten)
  
Auswirkung:
  - Strukturelle Integrität verloren
  - Risse breiten sich (Stress-Konzentration)
  - Witterungs-Eindringung (Wasser + Salz)
  
Prävention:
  - Oberflächenreinigung vor jeder Schicht
  - Harz-Zwischen-Schicht (feuchte CSM oder Spray)
  - Druck-Anwendung während Aushärtung (Vakuum-Bag)
```

**Fehler 3: Fasern-Ausrichtung falsch**

```
Ursache:
  - Gewebe schief angebracht (nicht 0°/90° ausgerichtet)
  - Roving-Faserung in falscher Richtung
  - Manuelle Wicklung ohne Richtungs-Markierung
  
Symptom:
  - Visuelle Kontrolle: Muster nicht symmetrisch
  - Torsions-Test: Boot verwindet sich unerwünscht
  - Vibrationen bei bestimmten Frequenzen
  
Auswirkung:
  - Torsions-Steifheit reduziert (-20–30%)
  - Verwindungs-Bewegung unter Seegang
  - Beschleunigung von Ermüdungs-Rissen
  
Prävention:
  - Schrift/Markierungen auf Formen (0°-Richtung deutlich markiert)
  - Quality-Kontrolle nach jeder Schicht (Foto-Dokumentation)
  - Training für Wickler
```

**Fehler 4: Harz-Gehalt ungleichmäßig**

```
Ursache:
  - Harz-Dosierung nicht konsistent
  - lokale Druck-Unterschiede (ungleich Vakuum)
  - Kern-Material aufsaugen (bei Sandwich)
  
Symptom:
  - Oberflächenrauhheit variiert
  - Ultraschall: Dicke schwankt >2 mm über kurze Strecke
  - einige Bereiche glänzend, andere matt
  
Auswirkung:
  - Schwachstellen entstehen (niedrig-Harz-Zonen)
  - Wasser-Eindringung lokal
  - Festigkeits-Varianz
  
Prävention:
  - Harz-Verbrauch dokumentieren (L/m² Standard)
  - Vacuum-Pressure-Monitoring
  - Schicht-Feinwaage (nicht blind abmessen)
```

### 5.2 Qualitätskontrolle und Inspektionsmethoden

**Visuelle Prüfung:**

```
Standard nach ISO 14125:
  - Gelcoat-Oberflächenqualität: Ra <25 µm (rauhe OK, keine Kratzer)
  - Farbkonsistenz: gleich über gesamte Fläche
  - Kratzer/Dellen: <2 mm Tiefe akzeptabel
  - Fasern-Sichtbarkeit: sollte nicht sichtbar sein (sonst Harz-Mangel)

Fehler-Grenzen:
  - <100 mm² kleine Kratzer: akzeptabel
  - >100 mm² oder >2 mm Tiefe: reparieren
  - >500 mm² oder Delaminierungs-Zeichen: Vorgesetzter prüfen
```

> ⚠️ **ZU PRÜFEN (Audit) — TEILWEISE AUFGELÖST 2026-07:** Normbezug falsch zugeordnet. **Bestätigt:** ISO 14125:1998 regelt die *Bestimmung der Biegeeigenschaften* faserverstärkter Kunststoffe (3-/4-Punkt-Biegeversuch an Laborprüfkörpern) — sie ist **keine** Norm für die visuelle Oberflächen-/Gelcoat-Inspektion (Ra-Rauheit, Farbkonsistenz, Kratzer/Dellen). Confidence: **documented** (iso.org/standard/23637.html). Gleicher Fehlbezug im Pydantic-Beispiel unten (`normen_referenzen=["ISO 14125", …]`). Die für die Fertigung/Abnahme zutreffenden Normen sind **ISO 12215-4** (Werkstatt & Fertigung) und die Klassifikations-Regelwerke; eine dedizierte ISO-Norm für kosmetische Gelcoat-Sichtprüfung existiert nicht (Sichtprüf-Akzeptanzkriterien sind werft-/klassenspezifisch, siehe Abschnitt 9.2). Die konkreten Ra-/Kratzer-Grenzwerte oben bleiben **estimated — unverifiziert**.

**Ultraschall-Prüfung (UT):**

```
Funktionweise:
  - Transducer sendet 5 MHz Wellen in Laminat
  - Reflexion von Grenzflächen (Schicht-Wechsel, Hohlräume)
  - Zeit-Messung: dicke = t × c / 2 (Schallgeschwindigkeit)
  
Typische Ergebnisse:
  - Solldicke 12 mm, gemessen 12 ± 1,5 mm: OK
  - Solldicke 12 mm, gemessen 8 mm: Harz-Mangel, prüfen
  - plötzlich 0 mm: Hohlraum / Delaminierung

Raster:
  Standard: 1 m × 1 m Gitter (pro Zone mindestens 5 Punkte)
  Bei Zweifeln: dichter Raster (z.B. 300 mm × 300 mm)
```

**Thermographie:**

```
Funktionsweise:
  - Infrarot-Kamera misst Oberflächentemperatur
  - Hohlräume (Luft) isolieren → bleiben kalt
  - Gute Laminat (Harz/Faser) leiten Wärme besser → wärmer
  
Anwendung:
  - Größere Boote (25m+)
  - Verdacht auf großflächige Delaminierung
  - Kosten-Nachteil (EUR 2000–5000 für komplette Scan)
```

**Röntgen-Prüfung:**

```
Methode: 2D-Röntgen oder Computertomographie (CT)
Kosten: EUR 5000–15000 pro Boot (nur Premium-Yachten)
Vorteil: innere Struktur komplett sichtbar
Nachteil: Strahlung, Kostenaufwand

Verwendung:
  - Vor Klassifizierung (Lloyd's, DNV)
  - Nach großem Grounding
  - Hochwertige Superyacht-Inspektion
```

---

## 6. Spezielle Laminat-Designs

### 6.1 Structured-Laminate (Rib-System)

**Konzept:**

```
Anstelle von flacher Fläche + Kern:
  → Rippen (Spanten) direkt in Laminat wickeln
  → Rib-Abstand: 300–500 mm
  
Vorteil:
  - Mehr Steifheit ohne zusätzliche Kern-Dicke
  - Gewichtseinsparung (5–10%)
  - Einfacher als Sandwich in komplexen Formen

Nachteil:
  - Komplexere Fertigungsmethode
  - Höhere Kosten (spezialisierte Wickel-Formen)
  - Weniger verbreitet
```

### 6.2 Unidirektionales Roving (Performance-Fokus)

**Aufbau:**

```
Für maximale Längsfestigkeit (z.B. Kiel, Mast):
  - Layer 1: CSM (Haftvermögen)
  - Layer 2–5: Unidirektional Roving 0° (parallel Kraft-Richtung)
  - Layer 6: CSM (Abschluss)

Festigkeit in 0°-Richtung: 2–3× höher vs. Biaxial-Gewebe
Nachteil: Quer-Festigkeit gering (braucht zusätzliche ±45°-Schichten)

Praktische Anwendung:
  - Mast-Fuß (höchste Längslast)
  - Kiel-Schaft
  - Balast-Taschen
```

### 6.3 Carbon-Hybrid (Gewichts-Optimierung)

**Anordnung:**

```
Externe Lagen: Carbon-Faser (leicht, steif)
Interne Lagen: E-Glass oder Kevlar (Druckwiderstand, Kosten)

Typisches Mix für Racing-Boot:
  Layer 1: CSM
  Layer 2–3: Carbon Biaxial 300 g/m² (Außenseite, sichtbar, Ästhetik)
  Layer 4–5: E-Glass Biaxial 400 g/m² (Kernbereich, Festigkeit)
  Layer 6–7: Kevlar oder E-Glass (innere Lage, Beschädigung-Resistenz)

Gewichtsvorteil: -40% vs. reines E-Glass
Kosten-Nachteil: +80–100% (Materialkosten)
Anwendung: nur wenn Performance >Kosten (Racing, Superyacht)
```

---

## 7. Umwelt und Langzeitbeständigkeit

### 7.1 UV-Beständigkeit und Gelcoat-Auswahl

**Gelcoat-Optionen:**

```
Standard-Polyester:
  Haltbarkeit: 3–5 Jahre (UV-Degradation)
  Zeichen: Vergilbung, Risse bei direktem Sonnenlicht
  Kosten: EUR 10–15/kg

Epoxy-Gelcoat:
  Haltbarkeit: 10–15 Jahre (besserer UV-Schutz)
  Zeichen: Minimal Vergilbung, langsame Degradation
  Kosten: EUR 20–30/kg

UV-stabilisierte Pigmente:
  Zusatz im Standard-Gelcoat (EUR 2–3 extra pro kg)
  Verlängert Haltbarkeit auf 5–8 Jahre
```

**Prävention gegen UV:**

```
1. Gelcoat-Dicke: 0,8–1,0 mm (vs. 0,5 mm minimal)
   → Mehr Material = längere Schutz-Dauer
   
2. Farben-Wahl:
   Dunkel (schwarz, blau): schnellere UV-Degradation
   Hell (weiß, grau): besserer UV-Schutz (reflexion)
   
3. Oberflächenbehandlung:
   Wachs oder Polymer-Versiegelung: EUR 50–100 jährlich
   → Schützt Gelcoat, einfach zu erneuern
   
4. Schutz-Plane:
   Bei langer Lagerung: UV-Plane über Rumpf
```

### 7.2 Osmotisches Blistering (Wasser-Eindringung)

**Physik:**

```
Problem: Polyester-Harz ist hygroscopisch (nimmt Wasser auf)
  → Nach 5–10 Jahren: Wasser passiert Gelcoat
  → Wasser-Moleküle dringen in Harz-Matrix ein
  → Ionische Konzentration ändert (osmotischer Druck)
  → Blasen entstehen (Gelcoat hebt ab)

Symptom:
  - kleine Blasen auf Rumpf (anfangs <1 cm)
  - später größer (2–5 cm)
  - Farbe unter Blasen oft grün/braun (Algen-Wachstum)
  
Auswirkung:
  - kosmetisch störend
  - kann zu Strukturschäden führen (wenn groß + zahlreich)
  - Reparatur teuer (50 m² = EUR 3000–5000)
```

**Prävention:**

```
1. Material-Auswahl:
   Epoxy-Harz statt Polyester (Feuchte-Aufnahme -90%)
   → Beste Langzeit-Lösung
   
2. Versiegelung:
   2-komponentiger Epoxy-Primer (100 µm) + Topcoat (75 µm)
   → Nach Bau: EUR 3000–5000 (für 12m Boot)
   → Haltbarkeit: 10–15 Jahre
   
3. Wartung:
   jährlich Oberflächenreinigung + Wachs
   → Hält Gelcoat-Integrität
   
4. Drainage:
   Auswasser-Löcher (Ø 3 mm) in Spanten-Taschen
   → Verhindert Stauwasser
```

---

## 8. Kosten-Kalkulation und Material-Auswahl

### 8.1 Material-Kostenschätzung

**Für 12m Segelboot (Rumpf-Oberfläche ~150 m²):**

```
Szenario A: Standard Production (Polyester + E-Glass)
  Gelcoat Polyester: 150 m² × EUR 12/m² = EUR 1800
  CSM 300 g/m² (4 Lagen): 600 m² × EUR 4/m² = EUR 2400
  Biaxial Woven 400 g/m² (4 Lagen): 600 m² × EUR 6/m² = EUR 3600
  Polyester-Harz (60% Gewicht): 150 m² × 30 kg/m² × EUR 4/kg = EUR 18000
  TOTAL Material: EUR 25800
  + Arbeit (40%): EUR 10300
  GESAMT: EUR 36100

Szenario B: Premium (Epoxy + S-Glass + Sandwich)
  Gelcoat Epoxy: 150 m² × EUR 18/m² = EUR 2700
  CSM (3 Lagen): 450 m² × EUR 5/m² = EUR 2250
  S-Glass Biaxial (3 Lagen): 450 m² × EUR 12/m² = EUR 5400
  PVC H-100 Kern (30 mm): 150 m² × EUR 25/m² = EUR 3750
  Epoxy-Harz (50% Gewicht total): 150 m² × 20 kg/m² × EUR 10/kg = EUR 30000
  TOTAL Material: EUR 44100
  + Arbeit (45%): EUR 19845
  GESAMT: EUR 63945

Kosten-Differenz: +77% für Premium (aber Lebensdauer +50%)
```

### 8.2 Optimierungs-Strategien (Kosten senken, Qualität halten)

```
Maßnahme 1: Recycled-Harz (min. 10% Mix)
  Kosten: -10% bei Harz
  Qualität: minimal Unterschied (immer noch strukturell gut)
  Nachteil: Farbe variabel (weniger kontrollierbar)
  
Maßnahme 2: CSM-Reduktion (nur Schichten 1 + 8)
  Kosten: -15% bei Laminat
  Qualität: acceptable (CSM ist ineffizient)
  Nachteil: Haftvermögen leicht schlechter
  
Maßnahme 3: Niedrig-Kosten Kern (H-80 statt H-100)
  Kosten: -20% bei Kern
  Qualität: akzeptabel (Steifheit -15%, aber noch genug)
  Nachteil: längere Durchbiegung unter Last
  
Maßnahme 4: Lokal optimierte Dicke
  Nicht überall gleich Dicke
  → Bug (hoher Druck): 14 mm
  → Seite (mittel): 11 mm
  → Aft (niedrig): 9 mm
  Kosten: -20% bei Material
  Aufwand: Komplexere Fertigungsplanung
```

---

## ANHANG A — Glossar

**Aushärtung:** Chemischer Prozess, Harz wird hart (Polymerisation).

**Biaxial:** zwei Faser-Richtungen (0° + 90°), gleiche Festigkeit beide Achsen.

**CSM (Chopped Strand Mat):** kurze Fasern, zufällige Richtung, gutes Haftvermögen.

**Delaminierung:** Ablösung zwischen Laminate-Schichten.

**Druckfestigkeit:** Widerstand gegen Kompression (Druck).

**E-Glass:** Standard-Glasfaser, 72 GPa E-Modul.

**Epoxy-Harz:** Premium-Harz, höhere Festigkeit + Wasser-Resistenz.

**Faser-Volumen:** Prozentsatz Fasern im Laminat (ideal 40%).

**Gelcoat:** Harz-Schutzschicht auf Laminate-Oberfläche.

**Gimbal:** Aufhängung, erlaubt Rotation (z.B. Herd unter Seegang).

**Harz-Gehalt:** Prozentsatz Harz im Laminat (ideal 60%).

**Hohlraum (Void):** Lufteinschluss im Laminat.

**Kevlar:** Aramid-Faser, sehr leicht aber schwach auf Druck.

**Laminat:** geschichtete Struktur aus Fasern + Harz.

**MEKP:** Methylethylketon-Peroxid, Katalysator für Polyester.

**Polyester-Harz:** Standard-Harz, billiger aber Wasser-aufnehmend.

**Roving:** lange parallele Fasern, höchste Festigkeit in einer Richtung.

**S-Glass:** Glas-Faser, höhere Festigkeit als E-Glass (+35%).

**Sandwich-Konstruktion:** Schichten mit Kern-Material dazwischen.

**Scherfestigkeit:** Widerstand gegen Seitenkraft (Schub).

**Unidirektional:** Fasern alle in einer Richtung (0°).

**Vindylester:** Hybrid zwischen Polyester + Epoxy.

**Woven (Gewebe):** lange Fasern, gewebt, 0°/90° Orientierung.

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class LaminatplanFehlerbild(BaseModel):
    """
    Fehlerbild für Laminatplan nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_12_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Laminatplan"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Struktur/Haltbarkeit")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Strukturelle Sicherheit betroffen?")
    
    # Ursprung
    boots_typen: List[str] = Field(default_factory=list, description="Betroffene Boot-Klassen")
    laminat_zone: str = Field(default="", description="Rumpf/Deck/Kiel/etc")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Prüfmethoden")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Kontroll-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO, Lloyd's")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = LaminatplanFehlerbild(
    fehlerbild_id="31_12_001",
    titel="Laminat-Dicke ungleichmäßig",
    beschreibung="Schicht-Dicke variiert über Boot-Länge, erzeugt Schwachstellen.",
    symptome=[
        "Ultraschall-Messung zeigt Schwankungen >3 mm",
        "lokale Dünn-Stellen (unter Solldicke)",
        "Oberflächenrauhheit variiert"
    ],
    auswirkungen=[
        "Lokalgebiet mit reduzierter Festigkeit (-30%)",
        "Ermüdungs-Risse entstehen bevorzugt dort",
        "Wasser-Eindringung in Schwachstellen"
    ],
    schweregrad="hoch",
    sicherheits_impact=True,
    boots_typen=["Segelboot", "Motorsegler"],
    laminat_zone="Rumpf",
    diagnose_methoden=[
        "Ultraschall-Prüfung (Raster 1m × 1m)",
        "Visuelle Kontrolle Oberflächen-Beschaffenheit",
        "Röntgen (optional, für Premium)"
    ],
    reparatur_optionen=[
        "Lokal Nachlaminieren (aufwendig, eingreifend)",
        "Langfristig: Ausgleich durch externe Armierung",
        "Akzeptanz mit erhöhter Inspektions-Frequenz"
    ],
    schaetzung_kosten_eur=5000,
    dauer_tage=7,
    praevention=[
        "Harz-Verbrauch dokumentieren pro Schicht",
        "Qualitäts-Kontrolle nach jeder Lage",
        "Vacuum-Druck-Monitoring"
    ],
    inspektions_intervall_jahre=2,
    # Korrigiert (Audit): ISO 14125 = Biegeprüfung (Labor), NICHT Dickentoleranz.
    # Dickentoleranz/Scantling -> ISO 12215-5; Fertigung -> ISO 12215-4.
    normen_referenzen=["ISO 12215-5", "ISO 12215-4", "Lloyd's Register"],
    verwandte_fehlerbilder=["31_12_002", "31_12_005"]
)
```

---

## ANHANG C — FAQ (25+)

**F1: Polyester oder Epoxy-Harz wählen?**
A: Polyester: billiger (-60%), aber Osmotic Blistering nach 10 Jahren. Epoxy: teuer, aber 20+ Jahre haltbar. Für Salzwasser: Epoxy empfohlen.

**F2: Wie viel Harz ist optimal?**
A: 55–60% Gewicht (entspricht 40–45% Faser-Volumen). Weniger = Poren; mehr = Gewicht ohne Festigkeit.

**F3: Sandwich vs. Ganzlaminate?**
A: Sandwich 40% leichter, aber komplexer. Für Performance: Sandwich. Für Robustheit: Ganzlaminate.

**F4: Wie dick sollte Gelcoat sein?**
A: 0,5 mm minimal, 0,8–1,0 mm ideal. Dicker = längere UV-Schutz, aber schwerer.

**F5: E-Glass oder S-Glass?**
A: E-Glass Standard (billig). S-Glass +35% Festigkeit, aber 3–4× teurer. Nur für Racing.

**F6: Was bedeutet 450 g/m² Biaxial?**
A: 450 g Fasern pro m² Tuch. Mit Harz: ~1,2 m² = 2,2–2,5 mm Dicke.

**F7: Kann man Laminat später verstärken?**
A: Ja (Auflamination möglich), aber schwierig (Oberflächen-Vorbereitung). Besser vorher richtig dimensionieren.

**F8: Delaminierung reparierbar?**
A: Kleine Blasen (<5 cm): ja (Filler injizieren). Große (>20 cm): schwierig, oft Neulamination erforderlich.

**F9: Hohlraum-Risiko wie reduzieren?**
A: Vakuum-Bagging (beste), Druck-Kontrolle, Feuchte <50% Lagerbedingung.

**F10: Osmotic Blistering verhinderbar?**
A: Ja: Epoxy-Harz oder 2-komponentiger Epoxy-Primer-Topcoat System. Kosten EUR 50/m².

---

## 9. Normativer Rahmen — verifiziert

> **Confidence-Hinweis:** Alle Normbezüge in diesem Abschnitt sind gegen iso.org und BSI verifiziert (**documented**). Die *exakten Formeln, Koeffizienten und Sicherheitsbeiwerte* der ISO-12215-Reihe stehen ausschließlich im (kostenpflichtigen) Normtext und wurden **nicht** rekonstruiert. Wo unten quantitative Angaben fehlen, ist dies Absicht: siehe Abschnitt 10.

### 9.1 ISO 12215 — „Kleine Wasserfahrzeuge — Rumpfbauweise und Dimensionierung"

Der Laminatplan ist die konstruktive Umsetzung der Dimensionierung (Scantlings) nach ISO 12215. Die Reihe ist das **Basis-Regelwerk des `structural`-Moduls** (vgl. CLAUDE.md). Teileübersicht (verifiziert iso.org / BSI):

| Teil | Titel (Kurz) | Relevanz für den Laminatplan |
|------|--------------|------------------------------|
| **12215-1:2000** | Werkstoffe: Duroplast-Harze, Glasfaser-Verstärkung, Referenzlaminat | Definiert das **Referenzlaminat** und Anforderungen an Harze/Verstärkung — Ausgangspunkt für Materialkennwerte |
| **12215-2:2002** | Werkstoffe: Kernmaterialien für Sandwich, eingebettete Materialien | Anforderungen an Schaum-/Balsakerne (Abschnitt 3 & 11.2) |
| **12215-3:2002** | Werkstoffe: Stahl, Aluminium, Holz, andere | Nicht-FRP-Bauweisen |
| **12215-4:2002** | Werkstatt & Fertigung | Lager-/Verarbeitungsbedingungen, Fertigungs-QS (Abschnitt 5 & 9.2) |
| **12215-5:2019** | Bemessungsdrücke Monohulls, Bemessungsspannungen, Scantling-Bestimmung | **Kernnorm** — leitet aus Bemessungsdruck die geforderte Laminat-/Sandwich-Dimensionierung ab (Abschnitt 10) |
| **12215-6:2008** | Konstruktive Anordnung & Details | Verbindungen, Steifen, Details, die 12215-5/-7/-8/-9 nicht abdecken |
| **12215-7:2020** | Lasten für Mehrrümpfe & lokale Scantlings (nutzt -5) | Katamarane/Trimarane |
| **12215-8:2019** | Ruder | Ruderkräfte & Ruderschaft-Dimensionierung |
| **12215-9:2012** | Anhänge von Segelfahrzeugen (Kiel, Schwert & Anschlüsse) | Kiel-Anschlusslasten, Ballast-Sicherheitsbeiwerte |
| **12215-10:2020** | Rigglasten & Rigg-Anschluss (Segelfahrzeuge) | Mastfuß/Pillars, Chainplates — Krafteinleitung ins Laminat |

Quelle: iso.org/standard/69552.html (Teil 5), /34466.html (Teil 2), /25271.html (Teil 4), /73457.html (Teil 7), /55339.html (Teil 9), /67294.html (Teil 10); landingpage.bsigroup.com (BS EN ISO 12215 Serie).

> **Geltungsbereich (verifiziert):** ISO 12215-5:2019 gilt für Rumpflänge L_H bzw. Wasserlinienlänge bis **24 m** und deckt FRP in **Einzelschale (single skin)** *und* **Sandwich** ab, ferner Aluminium, Stahllegierungen und verleimtes Holz. Ziel ist die Gesamt-Strukturfestigkeit zur Sicherung der Wasser- und Wetterdichtheit. Die Norm 2019 wurde 2026 bestätigt und ist gültig. Quelle: iso.org/standard/69552.html.

### 9.2 Weitere relevante Normen (verifiziert)

| Norm | Scope (verifiziert) | Einsatz hier |
|------|---------------------|--------------|
| **ISO 14125:1998** | Bestimmung der **Biegeeigenschaften** faserverstärkter Kunststoffe (3-/4-Punkt-Biegeversuch) | Laborkennwerte, **nicht** Sichtprüfung — vgl. korrigiertes Flag in Abschnitt 5.2 |
| **ASTM D1621** | Druckeigenschaften starrer Schäume | Kern-Druckfestigkeit/-modul (Abschnitt 11.2) |
| **ASTM D1623** | Zugeigenschaften starrer Schäume | Kern-Zugfestigkeit (Abschnitt 11.2) |
| **ASTM C273** | Scherversuch an Sandwich-Kernen | Kern-Schubfestigkeit/-modul (Abschnitt 11.2) |
| **ISO 12215-4** | Werkstatt & Fertigung | Verarbeitungs-/Abnahmebedingungen |

> **Sichtprüfung/Kosmetik:** Es existiert **keine** dedizierte ISO-Norm für kosmetische Gelcoat-Sichtprüfung. Akzeptanzkriterien (zulässige Blasen, Kratzer, Orange-Peel) sind **werft- bzw. klassenspezifisch** (z. B. Lloyd's Register, DNV, Bureau Veritas Regelwerke) und vertraglich zu vereinbaren. Quantitative Grenzwerte in Abschnitt 5.2 daher **estimated — unverifiziert**.

---

## 10. Verbindung Laminatplan ↔ ISO-12215-5-Scantlings — dokumentierte Methodik

> **⚠️ WICHTIG (Struktur/Naval Architecture):** Dieser Abschnitt beschreibt die **Methodik und das Wirkprinzip** der Scantling-Bestimmung. Er enthält **bewusst keine** ausformulierten Bemessungsformeln, Koeffizienten oder Rechenbeispiele. Diese stehen ausschließlich im Normtext ISO 12215-5:2019 und wurden **nicht rekonstruiert** — eine erfundene Formel wäre ein Sicherheitsrisiko. Für reale Dimensionierung: Normtext beschaffen oder Naval Architect / Klassifikation hinzuziehen.

### 10.1 Ablauf der Dimensionierung (Prinzip, verifiziert dem Scope nach)

Der Laminatplan ist **Ergebnis**, nicht Eingang der Rechnung. Die logische Kette (ISO 12215-5):

```
1. Eingang: Bootsdaten (L_H, Verdrängung, Geschwindigkeit, CE-Kategorie A–D),
   Paneelabmessungen (Steifen-/Spantabstand), Bauart (single skin vs. sandwich)
        │
        ▼
2. Bemessungsdruck P [kN/m²] pro Paneel/Zone
   → abhängig von: Ort am Rumpf (Boden > Seite > Deck), Kategorie,
     dynamischem Faktor, Paneelfläche (Flächen-Abminderung)
     [exakte Druckformeln nur im Normtext]
        │
        ▼
3. Bemessungsspannung σ_d des Werkstoffs
   → = charakteristische Festigkeit / Sicherheitsbeiwert
     [Beiwerte nur im Normtext — NICHT rekonstruiert]
        │
        ▼
4. Geforderte Scantling:
   • Single skin: Mindest-Dicke / Mindest-Flächengewicht des Laminats
   • Sandwich:  Deckschicht-Widerstandsmoment + Kern-Schubtragfähigkeit
        │
        ▼
5. Laminatplan (dieses Dokument): Lagenfolge, Faserorientierung, Kerndicke,
   die die geforderte Scantling ERFÜLLEN oder ÜBERSCHREITEN
```

> Confidence: **documented** für Ablauf/Scope (iso.org/standard/69552.html); **quantitative Schritte 2–3 unverifiziert — nicht rekonstruiert.**

### 10.2 Materialkennwerte aus Glasgehalt — Prinzip

ISO 12215 verwendet den **Glasgehalt (Glass content, G_c bzw. ψ)** als Masseanteil der Verstärkung, um mechanische Laminatkennwerte (Zug-/Biege-/Schubfestigkeit, E-Modul) abzuleiten. Höherer Glasgehalt → höhere Festigkeit/Steifigkeit pro Dicke, aber verfahrensabhängig begrenzt (Abschnitt 12).

> **Prinzip belegt** (ScienceDirect, Regulatory Review composite hulls: „ISO 12215 considers … impact of glass content G_c"; typische Auslegung normaler G_c ≈ 0,37, hoher G_c ≈ 0,60). **Die exakten G_c-abhängigen Kennwert-Gleichungen der Norm wurden NICHT rekonstruiert.** Quelle: sciencedirect.com/science/article/pii/S209267822300047X.

### 10.3 Single-Skin vs. Sandwich — Tragmechanik (qualitativ)

| Aspekt | Single Skin (Einzelschale) | Sandwich |
|--------|----------------------------|----------|
| Biegung aufnehmen | Gesamtes Laminat trägt (Dicke ↑ = Steifigkeit ↑↑↑, kubisch) | **Deckschichten** tragen Zug/Druck; Hebelarm durch Kerndicke |
| Schub aufnehmen | Laminat selbst | **Kern** trägt Schub → Kern-Schubfestigkeit ist Auslegungsgröße (ASTM C273, Abschnitt 11.2) |
| Versagensarten | Bruch, Delamination | Zusätzlich: **Kern-Schubbruch, Deckschicht-Beulen (wrinkling), Deckschicht-Kern-Ablösung** |
| Gewicht bei gleicher Steifigkeit | schwerer | leichter (Kern verschiebt Masse nach außen) |
| Robustheit Schlag/Grounding | gutmütiger | Deckschicht dünner → schlag-/punktlastempfindlicher |
| Norm-Bezug | ISO 12215-5 (single skin) | ISO 12215-5 + **-2** (Kernmaterial) |

> Die Sandwich-Tragmechanik (Deckschichten = Biegespannung, Kern = Schub) ist Standard-Sandwichtheorie und in ISO 12215-5/-2 abgebildet. Confidence: **documented** (iso.org/standard/34466.html; Scope ISO 12215-5).

---

## 11. Verifizierte Materialdaten (löst Alt-Schätzwerte auf)

### 11.1 Faserkennwerte (Filament, nicht Laminat)

Nennwerte **einzelner Filamente/Rovings** (nicht des fertigen Laminats — im Verbund liegen die Werte wegen Harzanteil, Faservolumen und Orientierung deutlich niedriger, siehe Abschnitt 12):

| Faser | Zugfestigkeit MPa | Zugmodul GPa | Dichte g/cm³ | Bruchdehnung % |
|-------|-------------------|--------------|--------------|----------------|
| **E-Glas** | ~2.900 (420 ksi) | ~72 (10,5 msi) | 2,54 | 4,4 |
| **S-2-Glas** | ~4.590 (665 ksi) | ~85 (12,4 msi) | 2,49 | 5,2 |
| **Basalt** | ~4.140 (600 ksi) | ~85 (12,3 msi) | 2,64 | 3,0 |
| **Aramid (Kevlar 49)** | ~3.000 (435 ksi) | ~124 (18 msi) | 1,44 | 2,4 |
| **Carbon HS (T300)** | ~3.530 (512 ksi) | ~230 (33,4 msi) | 1,80 | 1,5 |
| **Carbon HS (T700)** | ~4.900 (711 ksi) | ~230 (33,4 msi) | 1,80 | 2,1 |

> Confidence: **documented** — Texonic Fiber Properties Guide (texonic.net/en/tableau/technical). Werte in ksi/msi im Original; SI-Umrechnung 1 ksi ≈ 6,895 MPa, 1 msi ≈ 6,895 GPa. Diese bestätigen die im Kopf des Dokuments (Abschnitt 1.1) genannten Größenordnungen (E-Glas 72 GPa, S-Glas +~35 % Festigkeit, Aramid leicht + druckschwach, Carbon ~230 GPa/spröde).

> **Aramid-Druckschwäche (bestätigt):** Aramid versagt unter Druck deutlich früher als unter Zug (Fibrillen-Knicken) — daher in der Praxis oft Hybrid (Aramid außen für Schlag/Zug, Glas/Carbon innen für Druck). Confidence: **documented** (Faservergleich lft-g.com, tchaintech.com).

### 11.2 Divinycell-H-Kernmaterial (DIAB) — Referenztabelle

**Löst das ⚠️-Flag in Abschnitt 3.1 auf.** Nennwerte nach DIAB-Herstellerdatenblatt „Divinycell H" (SI):

| Grade | Nenndichte kg/m³ | Druckfestigkeit MPa (ASTM D1621) | Druckmodul MPa | Zugfestigkeit MPa (ASTM D1623) | Schubfestigkeit MPa (ASTM C273) | Schubmodul MPa |
|-------|------------------|----------------------------------|----------------|--------------------------------|----------------------------------|----------------|
| H45  | ~48  | — | — | — | — | 22 |
| **H60**  | 60  | 0,9 | 70  | 1,8 | 0,76 | ~20 |
| **H80**  | 80  | 1,4 | 90  | 2,5 | 1,15 | ~27 |
| **H100** | 100 | 2,0 | 135 | 3,5 | 1,6  | 40 |
| H130 | 130 | 3,0 | 170 | 4,8 | 2,2  | 50 |
| H160 | 160 | 3,4 | 200 | 5,4 | 2,6  | 60 |
| **H200** | 200 | 5,4 | 240–310* | 7,1 | 3,5  | 73 |
| H250 | 250 | 6,2 | 300 | 8,8 | 4,5  | 108 |

> Confidence: **documented** — DIAB Divinycell H TDS (diabgroup.com/products-services/divinycell-pvc; Rev. 2020–2026). Fett = über mehrere Datenblatt-Revisionen konsistent bestätigt. Nicht fett = aus Herstellerangaben abgeleitet, gegen aktuelle TDS gegenprüfen.
> *Druckmodul H200: Revisionsabweichung (240 MPa in neueren, 310 MPa in älteren TDS) — vor Nutzung aktuelle TDS-Revision heranziehen.
> **Kernaussage:** Die realen Werte liegen um **Faktor 3–4 über** den fehlerhaften Alt-Angaben in Abschnitt 3.1 (dort H-100 Druck 0,5 statt 2,0 MPa). Für Sandwich-Auslegung ausschließlich diese Tabelle bzw. aktuelle DIAB-TDS verwenden.

> **Prüfmethoden (verifiziert):** Druck ASTM D1621, Zug ASTM D1623, Schub ASTM C273. Herex/Divinycell PVC: geschlossenzellig, geringe Wasseraufnahme, gute Chemikalien-/UV-Beständigkeit. Confidence: **documented** (DIAB TDS).

---

## 12. Faservolumengehalt & Harzanteil nach Fertigungsverfahren

Der Harzanteil (Abschnitt 2.1 & 4.3) ist **nicht frei wählbar**, sondern verfahrensbestimmt. Belegte Richtwerte:

| Verfahren | Faservolumen V_f (%) | Fasermasseanteil (%) | Kommentar |
|-----------|----------------------|----------------------|-----------|
| **Handlaminat (wet lay-up)** | 35–45 | ~30–50 | Höchster Harzanteil, höchstes Porenrisiko; CSM-Handlaminat unten (~0,30 Masse) |
| **Vakuum-Bagging (wet)** | ~48–58 | ~60–73 | Überschussharz abgepresst, weniger Poren |
| **Vakuum-Infusion (VARTM)** | 50–60 | ~60–70 | Trockenlage, dann Harzinfusion; niedriger Porengehalt |
| **Doppelsack-Infusion** | 60–70 | — | Enge Prozesskontrolle, reproduzierbar hoch |
| **Prepreg / Autoklav** | 60–70 | — | Vorimprägniert, höchster V_f, niedrigster Porengehalt |

> Confidence: **documented** — CompositesWorld (double-bag infusion 60–70 % V_f), Epoxyworks (Handlaminat 35–45 % vs. Infusion 50–60 %), Plymouth MATS347 (Prepreg 60–70 %). Quellen: compositesworld.com/articles/double-bag-infusion-70-fiber-volume; epoxyworks.com/vacuum-bagged-repair-infusion-vs-wet-bag.

> **Konsequenz für den Laminatplan:** Ein für Infusion (V_f ≈ 55 %) dimensioniertes Laminat, das im **Handlaminat** (V_f ≈ 40 %) gebaut wird, ist **dicker, schwerer und je nach Kennwertbasis schwächer** als geplant. Verfahren und angesetzter Glasgehalt (Abschnitt 10.2) müssen zum realen Fertigungsverfahren passen — sonst stimmt die ISO-12215-5-Rechnung nicht. Der im Kopf genannte Idealbereich „40 % Faservolumen" (Abschnitt 2.1) entspricht **Handlaminat**; Infusion/Prepreg liegen höher.

---

## 13. Verstärkungs-Gelegetypen: Gewebe (woven) vs. Multiaxialgelege (NCF)

Ergänzung zu Abschnitt 1.2. Der in Abschnitt 1.2 als „Biaxial Woven" bezeichnete Aufbau ist strenggenommen zu differenzieren:

| Typ | Aufbau | Vorteil | Nachteil |
|-----|--------|---------|----------|
| **Woven Roving (Gewebe)** | 0°/90° verwoben, Fasern **gecrimpt** (wellig durch Kreuzung) | Robust, gute Drapierbarkeit, günstig | Crimp → Fasern müssen sich unter Last erst „strecken" → früheres Matrix-Mikroreißen, geringere Ausnutzung |
| **Multiaxialgelege / NCF (Non-Crimp Fabric)** | 1–4 gestreckte UD-Lagen (0°/90°/±45°) durch Nähfaden fixiert, **kein Crimp** | Höhere Zug-/Biegesteifigkeit, bessere Ermüdungsfestigkeit, höherer erreichbarer V_f (weniger Harznester) | Etwas teurer, weniger tolerant bei enger Drapierung |

> Confidence: **documented** — NCF-Fasern liegen gestreckt und nutzen die Faserfestigkeit besser aus; im Segang/Torsion (Marine) bevorzugt für Rumpf/Deck/Schotten. Bei gecrimptem Gewebe muss sich die Faser unter Zug erst geradeziehen, wobei die spröde Matrix die Erstlast allein trägt → Mikrorisse vor Erreichen der Faser-Zugfestigkeit. Quellen: sky-composites.com/news/multiaxial-carbon-fiber-fabrics; vectorply.com/stitch-bonded-reinforcements; compositesworld.

> **Praxis-Empfehlung:** Moderne Werften ersetzen Woven Roving zunehmend durch Biaxial-/Multiaxialgelege (z. B. „1708" = 0/90-Biax-Gelege + CSM-Rückseite). Für den Laminatplan bedeutet „Biaxial" heute meist **gestitchtes Gelege**, nicht klassisches Gewebe.

---

## 14. Fehlerbild-Atlas (kollisionsfreie IDs)

> **ID-Schema:** `FB-31-12-NNN`, fortlaufend. Diese IDs sind **neu** und kollidieren nicht mit den informellen „Fehler 1–4" (Abschnitt 5.1) oder den Pydantic-IDs `31_12_00N` (Anhang B). Schweregrad-Skala: kritisch / hoch / mittel / niedrig.

### FB-31-12-001 — Sandwich-Kernauslegung mit Falschwerten (Unterdimensionierung)

- **Beschreibung:** Kern-Schub-/Druckfestigkeit wurde zu niedrig angesetzt (z. B. Alt-Werte aus Abschnitt 3.1: H-100 Schub 0,3 statt real 1,6 MPa) → Kern real überdimensioniert *oder*, umgekehrt, ein zu schwacher Grade gewählt, weil Anforderung unterschätzt.
- **Symptome:** Weiche/„atmende" Paneele unter Last; bei Grounding/Slamming Deckschicht-Kern-Ablösung; Klopftest hohl.
- **Auswirkung:** Kern-Schubbruch, Verlust der Sandwichwirkung → Strukturversagen.
- **Diagnose:** Abgleich Laminatplan-Kennwerte gegen aktuelle DIAB-TDS (Abschnitt 11.2); Kernprobe → ASTM C273.
- **Prävention:** Nur verifizierte Herstellerkennwerte (Abschnitt 11.2) verwenden; ISO 12215-2 Kernanforderungen.
- **Schweregrad:** kritisch · Sicherheitsrelevant: ja · Norm: ISO 12215-2/-5, ASTM C273.

### FB-31-12-002 — Faserorientierung/Verfahren-Mismatch

- **Beschreibung:** Laminat für Infusion (V_f ≈ 55 %) ausgelegt, aber im Handlaminat (V_f ≈ 40 %) gebaut — oder umgekehrt.
- **Symptome:** Ist-Dicke/-Gewicht weicht systematisch vom Plan ab; Kennwerte nicht erreicht.
- **Auswirkung:** Festigkeit/Steifigkeit unter Auslegung; Gewichts-/Trimmabweichung.
- **Diagnose:** Glühverlust-/Veraschungsprobe (Fasermasseanteil); Dickenmessung gegen Plan.
- **Prävention:** Verfahren + angesetzten Glasgehalt (Abschnitt 12) im Laminatplan festschreiben.
- **Schweregrad:** hoch · Sicherheitsrelevant: ja · Norm: ISO 12215-5 (Glasgehalt/G_c).

### FB-31-12-003 — Woven-Roving-Crimp-Mikrorisse

- **Beschreibung:** Hoch beanspruchtes Bauteil aus gecrimptem Gewebe statt gestreckten Geleges (NCF) → früher Matrix-Mikroriss.
- **Symptome:** Frühe Haarrisse in harzreichen Zonen; Steifigkeitsverlust unter zyklischer Last.
- **Auswirkung:** Reduzierte Ermüdungsfestigkeit, Wassereintrittspfade.
- **Diagnose:** Mikroskopie/Schliffbild (Crimp sichtbar); Lastwechselverhalten.
- **Prävention:** Für tragende, ermüdungskritische Zonen Multiaxialgelege (NCF) bevorzugen (Abschnitt 13).
- **Schweregrad:** mittel · Sicherheitsrelevant: bedingt · Norm: —.

### FB-31-12-004 — Unsymmetrischer Sandwich-Aufbau (Verzug)

- **Beschreibung:** Innen- und Außendeckschicht ungleich (Lagenzahl/-orientierung) ohne konstruktiven Grund → thermischer/aushärtungsbedingter Verzug und exzentrische Biegung.
- **Symptome:** Paneelverzug nach Entformen; ungleiche Spannungsverteilung.
- **Auswirkung:** Vorspannungen, lokale Überlastung einer Deckschicht.
- **Diagnose:** Lagenprotokoll prüfen; Ebenheitsmessung.
- **Prävention:** Symmetrischer/ausgeglichener Lagenaufbau, sofern nicht gezielt asymmetrisch ausgelegt.
- **Schweregrad:** mittel · Sicherheitsrelevant: bedingt · Norm: ISO 12215-6 (Details).

### FB-31-12-005 — Deckschicht-Beulen (Face Wrinkling) durch zu dünne Außenhaut

- **Beschreibung:** Außendeckschicht des Sandwich für Gewichtsersparnis zu dünn → lokales Beulen der Deckschicht auf dem Kern unter Druck.
- **Symptome:** Örtliche Einbeulungen/Falten, besonders in druckbeanspruchten Boden-/Seitenpaneelen.
- **Auswirkung:** Plötzliches lokales Versagen (Instabilität, nicht Festigkeit).
- **Diagnose:** Deckschichtdicke gegen Scantling-Anforderung; Beulnachweis (ISO 12215-5, Sandwich).
- **Prävention:** Mindest-Deckschichtdicke und Kern-Druckmodul einhalten (Abschnitt 11.2).
- **Schweregrad:** hoch · Sicherheitsrelevant: ja · Norm: ISO 12215-5 (Sandwich-Nachweise).

> Verwandte Alt-Fehlerbilder in Abschnitt 5.1 (Hohlräume, Delamination, Faserfehlrichtung, ungleicher Harzgehalt) bleiben gültig und ergänzen diesen Atlas.

---

## 15. Wartung, Prüffristen & Verfahren

> **Hinweis:** Feste Prüfintervalle sind meist **klassen-/versicherer-/herstellerspezifisch**, nicht durch eine einzelne ISO-Norm fixiert. Die folgenden Angaben sind teils **estimated** (Praxisrichtwerte) und als solche gekennzeichnet.

| Prüfung | Intervall | Confidence | Bezug |
|---------|-----------|------------|-------|
| Gelcoat-Sichtkontrolle (Risse, Blasen, Kreidung) | jährlich (Slippen) | estimated (Praxis) | Werft-/Klassenkriterien |
| Klopftest Sandwich-Verdacht (Delamination/Kernablösung) | bei Verdacht + nach Grounding | estimated | — |
| Feuchtemessung Sandwich-Deck (Kernfeuchte) | vor Kauf / bei Blasenbild | estimated | — |
| Osmose-Kontrolle Unterwasserschiff | alle 1–3 J bzw. bei Blasen | estimated | Abschnitt 7.2 |
| Ultraschall-Dickenraster (nach Reparatur/Klasse) | nach Klasse-Vorgabe | documented (Verfahren) | Abschnitt 5.2 |

**Verfahren bei Verdacht auf Kern-Delamination (Sandwich):**
1. Klopftest großflächig (hohler vs. dumpfer Klang) → Verdachtszonen markieren.
2. Feuchtemessung: nasser Kern deutet auf Deckschichtriss/Wassereintritt.
3. Bestätigung per Ultraschall/Thermografie (Abschnitt 5.2).
4. Bei bestätigter Ablösung: Deckschicht öffnen, nassen Kern entfernen/trocknen, Kern ersetzen (gleicher/höherer Grade, Abschnitt 11.2), Deckschicht symmetrisch nachlaminieren, Vakuumverpressung.

> Confidence: Verfahren **documented** (Standard-Sandwichreparatur); exakte Annahme-/Reparaturkriterien klassenabhängig.

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-05-18 · **Werft-Tiefe-Erweiterung (web-verifiziert):** 2026-07-13  
**Gültig für:** Segelboote, Motorsegler, Motorboote 8–40m LOA

---

## ANHANG D — Quellen (Werft-Tiefe-Erweiterung, verifiziert)

Alle nachstehenden Fakten wurden per WebSearch/WebFetch an autoritativer Quelle geprüft (Confidence **documented**):

- **ISO 12215-Reihe** (Teile 1–10): iso.org/standard/69552.html (Teil 5), /34466.html (Teil 2), /25271.html (Teil 4), /73457.html (Teil 7), /55339.html (Teil 9), /67294.html (Teil 10); landingpage.bsigroup.com (BS EN ISO 12215 Serie).
- **ISO 14125:1998** (Biegeeigenschaften, nicht Sichtprüfung): iso.org/standard/23637.html.
- **Divinycell-H-Kernkennwerte** (DIAB, ASTM D1621/D1623/C273): diabgroup.com/products-services/divinycell-pvc.
- **Faserkennwerte** (E-/S-Glas, Aramid, Carbon, Basalt): texonic.net/en/tableau/technical; Faservergleich lft-g.com, tchaintech.com.
- **Faservolumen nach Verfahren:** compositesworld.com/articles/double-bag-infusion-70-fiber-volume; epoxyworks.com/vacuum-bagged-repair-infusion-vs-wet-bag; ecm-academics.plymouth.ac.uk (MATS347).
- **Glasgehalt G_c / ISO-12215-Bezug:** sciencedirect.com/science/article/pii/S209267822300047X.
- **Woven vs. NCF (Non-Crimp Fabric):** sky-composites.com/news/multiaxial-carbon-fiber-fabrics; vectorply.com/stitch-bonded-reinforcements.

> **Nicht rekonstruiert (bewusst weggelassen):** Die exakten Bemessungsdruck-Formeln, Sicherheitsbeiwerte und G_c-abhängigen Kennwert-Gleichungen der ISO 12215-5/-8/-9/-10 stehen nur im kostenpflichtigen Normtext. Sie wurden **nicht** aus Sekundärquellen erraten (Sicherheitsrisiko). Für reale last-/sicherheitsrelevante Dimensionierung: Normtext beschaffen oder Naval Architect / Klassifikation beauftragen.
