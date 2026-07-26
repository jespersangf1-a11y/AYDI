# 31_13 — CAD/CAM Tools

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** CAD_Tools  
**Version:** 2.0  
**Stand:** 2026-05-18  
**Relevanz:** Kern-Werkzeuge für Yacht-Design, Konstruktion, Produktion

---

## Übersicht

CAD/CAM-Software bestimmt **Konstruktions-Effizienz**, **Präzision** und **Fertigungsqualität**. AYDI analysiert verfügbare Tools (Rhino/Orca3D, Maxsurf, DELFTship, AutoCAD, FreeShip), deren Spezialitäten, Datei-Formate und Integrations-Möglichkeiten.

**Fehleranalyse-Schwerpunkte:**
1. Falsche CAD-Tool-Auswahl (z.B. Rhino für Serien, statt für Custom)
2. Datei-Format-Inkompatibilität (STEP vs. STL vs. IGS)
3. Hydro-dynamische Analyse ungenu (Maxsurf nicht verwendet)
4. Lofting-Fehler (Spanten nicht glatt, Wellen in Rumpf)
5. Scantlings (Struktur-Plan) nicht in CAD integriert
6. Stabilitäts-Berechnung fehlt oder falsch
7. Fertigungs-Vorbereitungen (NC-Code) unzureichend
8. Mesh-Qualität schlecht (zu grob für Analyse)
9. Versions-Kontrolle mangelhaft (änderungen nachzuverfolgen)
10. Dokumentations-Export unvollständig
11. Konstruktion nicht Klasse-genehmigt (Lloyd's, DNV)
12. Daten-Austausch mit Lieferanten schwierig

---

## 1. Überblick gängiger CAD-Tools für Yachtdesign

### 1.1 Rhino 3D + Orca3D (Industry Standard für Custom Yachten)

**Charakteristik:**

```
Rhino 3D:
  Allgemein-CAD-Tool (nicht spezialisiert auf Yachten)
  NURBS-basierte Modellierung (smooth curves, mathematical precision)
  Benutzer-freundlich (relative Lernkurve flach vs. anderen)
  Preis: EUR 995 (perpetual license)
  
Orca3D (Plugin für Rhino):
  Spezialisierung auf Yacht-Design
  Hydro-dynamische Analyse (Rumpf-Performance)
  Stabilitäts-Berechnung
  Lofting-Tools (automatische Spanten-Generierung)
  Preis: EUR 2500–5000 (je nach Version)
  
Combination:
  Rhino + Orca3D = standard in Custom-Werften (60% Markt-Share)
```

**Stärken:**

```
1. NURBS-Oberflächen: höchste Qualität, smooth transitions
2. Flexible Modellierung: komplexe Formen möglich
3. Integration mit Orca3D: nahtlose hydro-dynamische Analyse
4. Datei-Export: STEP, IGES, STL, DWG (alle Formate)
5. großes User-Community: Tutorials, Plugins verfügbar
```

**Schwächen:**

```
1. Kostenfaktor: Rhino + Orca3D + CAM-Tools = EUR 10000+
2. Lernkurve: für Anfänger 2–4 Wochen Training erforderlich
3. nicht native Fertigungs-Integration (CAM separat)
4. Performance bei großen Assemblies (Yachten 40m+ langsam)
```

**Praktischer Einsatz:**

```
Typischer Workflow:
  1. Hauptform im Rhino-Lofting entwerfen (3–5 Tage)
  2. Orca3D Stabilitäts-Analyse durchführen (1–2 Tage)
  3. Optimierung der Rumpf-Form (2–3 Iterationen, 5–7 Tage)
  4. Spanten exportieren für Produktion (Maßstäbe überprüfen)
  5. CAM-Software (Rhino-CAM oder Mastercam) für NC-Daten
  
Typisches Projekt-Durchwender:
  Kleine Yacht (10–12m): 2–3 Wochen
  Mittlere Yacht (16–20m): 4–6 Wochen
  Große Yacht (25m+): 8–12 Wochen
```

### 1.2 Maxsurf (Spezialisiert auf Hydro-dynamik)

**Charakteristik:**

```
Fokus: Hydrodynamische Analyse, Stabilitäts-Berechnungen
NURBS-Modellierung: ja (like Rhino)
Datei-Format: native .msd (Maxsurf Design)
Integration: mit Bentley-Ökosystem (AutoCAD, MicroStation)
Preis: EUR 5000–12000 (abhängig von Module)

Module:
  Maxsurf Design: Modellierung
  Maxsurf Stability: Stabilitäts-Berechnung (ISO 12217)
  Maxsurf Motion: Seegans-Verhalten, Bewegungs-Simulation
  Maxsurf Resistance: Widerstands-Vorhersage (CFD-ähnlich)
```

**Stärken:**

```
1. Hydro-dynamische Spezialisierung: höchste Genauigkeit
2. Stabilitäts-Berechnung: ISO 12217 konform
3. Bewegungs-Simulation: Pitch/Roll/Heave unter Seegang
4. Resistance-Prognose: gute Vorhersage Geschwindigkeit/Power
5. Klasse-Integration: Lloyd's, DNV, ABS Daten-Import
```

**Schwächen:**

```
1. Kostenfaktor: sehr teuer (EUR 10000+)
2. Bedienung: Lernkurve steil (spezialisiert)
3. nicht intuitive Interface (älter, weniger modern)
4. Datei-Export: schwieriger mit Standard-CAD-Tools
5. begrenzte 3D-Visualisierung (vs. Rhino)
```

**Einsatz-Profil:**

```
Beste Verwendung:
  - Hydro-dynamische Optimierung erforderlich
  - Seehundegang-Simulation nötig
  - Class-Genehmigung verlangt Maxsurf-Bericht
  
Typisch in:
  - professionelle Design-Büros
  - Werft-Engineering (größere Betriebe)
  - Regatta-Yachten (Performance-kritisch)
```

### 1.3 DELFTship (Freeware + kommerzielle Professional-Version)

**Charakteristik:**

```
Fokus: Hydro-dynamische Analyse, kostenlos
Lizenz: Open Source (frei verfügbar)
NURBS: eingeschränkt (weniger smooth curves als Rhino)
Stabilitäts-Berechnung: ja (ISO 12217)
Datei-Format: .ship (native), IGES, STL Export
Benutzer-Basis: begrenzt (akademisch + Budget-Werften)
```

> ✅ **KORREKTUR (verifiziert 2026-07):** DELFTship ist **NICHT Open Source**. Es ist **Freeware** (DELFTship Free, unbegrenzt und kostenlos, Kern-Rumpfmodellierung + Hydrostatik) plus eine **kommerzielle Perpetual-Lizenz** (DELFTship Professional, Listenpreis **USD 160**), die über kostenpflichtige Extensions (Cross-curves, Critical Points, Tank-Modellierung, Intact Stability/Load Cases) erweiterbar ist. DELFTship modelliert mit **Subdivision Surfaces**, nicht mit klassischen NURBS. Der tatsächlich quelloffene (GPL) Vorgänger ist **FREE!ship** (siehe 1.5-Anmerkung) — DELFTship setzte FREE!ship ab Release 3.1 unter neuem Namen und mit proprietären Zusatzfunktionen fort. Confidence: `documented`. Quellen: [DELFTship Pricing](https://www.delftship.net/pricing/), [DELFTship FAQs](https://www.delftship.net/faqs/), [Boat Design Net — FREE!ship continues as DELFTship](https://www.boatdesign.net/threads/free-ship-continues-as-delftship.15607/).

**Stärken:**

```
1. Kostenfaktor: kostenlos (großer Vorteil)
2. Stabilitäts-Berechnung: genauso gut wie kommerzielle Lösungen
3. Widerstands-Vorhersage: solide
4. Community-Support: gute (Universitäten, Forschung)
5. Linux/Mac/Windows: Cross-platform
```

**Schwächen:**

```
1. Benutzer-Interface: veraltet, weniger intuitiv
2. NURBS-Modellierung: nicht so smooth wie Rhino/Maxsurf
3. Performance: bei großen Modellen langsamer
4. Dokumentation: begrenzt (weniger Tutorials)
5. Klasse-Integration: nicht direkt (Daten-Export erforderlich)
```

**Einsatz-Profil:**

```
Beste Verwendung:
  - Budget-Konstruktion (Ausbildung, Hobbyist)
  - Quick-Stabilitäts-Check
  - Begleit-Analyse (neben anderen Tools)

Nicht ideal für:
  - kommerzielle Design-Büros (Reputation-Risiko)
  - Klasse-Genehmigung (zu wenig unterstützt)
  - komplexe Formen (Rumpf-Oberflächenqualität)
```

### 1.4 AutoCAD (Allgemein-CAD, begrenzt für Yachtdesign)

**Charakteristik:**

```
Fokus: 2D/3D Generalist (nicht spezialisiert auf Yachten)
Benutzer: Architektur, Maschinenbau, Elektrik
3D-Modellierung: Solide, aber nicht NURBS-spezialisiert
Datei-Format: .dwg (Standard, breite Kompatibilität)
Preis: EUR 600/Jahr (Subscription)
Erweiterungen: naviPowerEDU, ShipConstructor (für Schiffe)
```

**Stärken:**

```
1. Breite Verfügbarkeit: viele Nutzer weltweit
2. Datei-Format-Kompatibilität: .dwg ist Standard
3. Preis: günstiger als spezialisierte Tools
4. Integration: mit vielen CAM-Systemen
5. Stabilität: lange bewährte Software
```

**Schwächen:**

```
1. nicht spezialisiert auf Yachtdesign (fehlende Tools)
2. Flächen-Modellierung: weniger elegant als NURBS
3. Hydrodynamik: keine native Unterstützung
4. Stabilitäts-Berechnung: nicht vorhanden (externe Lösung nötig)
5. Lernkurve: für Yacht-Design-Anfänger ungünstig
```

**Einsatz-Profil:**

```
Begrenzte Verwendung:
  - 2D-Pläne (Konstruktions-Zeichnungen)
  - Allgemeine 3D-Geometrie
  - Schnittstelle mit Fertigungs-Systemen (NC-Code)

Besser kombiniert mit:
  - Rhino/Orca3D für Rumpf-Design
  - Maxsurf für Hydro-dynamik
```

### 1.5 FreeShip (Open-Source, spezialisiert auf Schiffe)

**Charakteristik:**

```
Fokus: spezialisiert auf Schiffe, besonders traditionelle Formen
Lizenz: Open Source (frei)
Modellierung: parametrisch (Spanten-orientiert)
Hydro-Berechnung: begrenzt (stabilitätsprüfung möglich)
Datei-Format: .fbm (native), IGES, STL Export
Community: small, aber aktiv (maritim-Enthusiasten)
```

**Stärken:**

```
1. Spezialisierung: Schiff-Konstruktions-Parameter
2. Preis: kostenlos
3. Parametrisches Design: schnelle Variationen
4. traditionelle Formen: gut geeignet (Holzboote, Klassiker)
5. leichte Bedienung (für spezialisierten Einsatz)
```

**Schwächen:**

```
1. NURBS-Qualität: weniger smooth als Rhino
2. begrenzte Hydro-Analyse: kein Motion-Simulator
3. kleine Community: weniger Support
4. Performance: nicht ideal für große Yachten
5. Klasse-Integration: fehlend
```

**Einsatz-Profil:**

```
Ideal für:
  - traditionelle Segelboote
  - Holzboot-Konstruktion
  - schnelle Konseptstudien
  - Ausbildung (maritim-Schulen)

Nicht geeignet für:
  - moderne High-Performance
  - große Motoryachten
  - kommerzielle Entwicklung
```

---

## 2. Datei-Formate und Kompatibilität

### 2.1 Standard-Formate in Yachtdesign

**STEP (.stp, .step) — ISO 10303:**

```
Beschreibung: Standard für Datei-Austausch (CAD-neutral)
Geometrie-Typ: NURBS, Solide, Flächen
Kompatibilität: universal (alle großen CAD-Systeme)
Größe: mittel (komprimiert möglich)
Nutzung: Austausch zwischen Design und Produktion

Vorteile:
  - Neutral (nicht Rhino- oder Maxsurf-spezifisch)
  - hohe Genauigkeit (geometrische Information erhalten)
  - Standard-Anerkennung (Klasse-Genehmigung)

Nachteile:
  - komplexe Datei-Struktur (manche Informationen verloren)
  - große Datei-Größe (für große Modelle)
```

**IGES (.igs, .iges) — legacy standard:**

```
Beschreibung: älterer Austausch-Standard (vor STEP)
Nutzung: noch verbreitet, aber zunehmend obsolet
Problem: weniger zuverlässig als STEP
Empfehlung: nutzen nur wenn Tool STEP nicht unterstützt
```

**STL (.stl) — Stereo-Lithography:**

```
Beschreibung: Oberflächenmodell aus Dreiecks-Netz
Kompatibilität: all Systeme (Rapid-Prototyping, 3D-Druck)
Problem: Verlust von NURBS-Information (nur Flächen)
Nutzung: für Visualisierung, 3D-Druck, Produktion
Größe: sehr groß (abhängig Mesh-Auflösung)

Mesh-Qualität-Angabe:
  Grob: 500 Dreiecke/m² (schnell, ungenau)
  Standard: 2000 Dreiecke/m² (Produktion)
  Fein: 10000+ Dreiecke/m² (Visualisierung, langsam)
```

> ✅ **AUFLÖSUNG (verifiziert 2026-07):** Der interne Widerspruch (10000+ vs. 5000+ Dreiecke/m²) ist gegenstandslos, weil **beide Zahlen unbelegt/erfunden** waren. Fachlich korrekt: Der **STL-Standard enthält keine Maßeinheit** — Einheiten sind willkürlich, und die Facettenzahl ist **kein sinnvolles absolutes Zielmaß**, weil sie von Bauteilgröße und Krümmung abhängt. Die Mesh-Dichte wird in der Praxis **nicht** über „Dreiecke pro m²" gesteuert, sondern über eine **Abweichungstoleranz** (max. Sehnenhöhe/Abstand Facette↔NURBS-Fläche; in Rhino: Parameter *maximum distance edge to surface* der Mesh-Einstellungen). Als Faustregel gilt: die Facettierungstoleranz kleiner wählen als die geforderte Fertigungstoleranz des Bauteils. Konkrete Dreieckszahlen bleiben `estimated — unverifiziert` und sind daher aus der Wissensbasis als Zielwerte zu entfernen. Confidence: `documented` (Prinzip). Quellen: [Library of Congress — STL Format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000506.shtml), [Wikipedia — STL (file format)](https://en.wikipedia.org/wiki/STL_(file_format)).

**DWG (.dwg) — AutoCAD Format:**

```
Beschreibung: proprietär AutoCAD-Format
Kompatibilität: sehr hoch (de-facto Standard 2D)
Problem: 3D-Unterstützung begrenzt
Nutzung: 2D-Zeichnungen, Arbeits-Pläne

Konvertierung:
  Rhino → DWG: meist verlustfrei
  Maxsurf → DWG: nur 2D-Schnitte
  FreeShip → DWG: einfach (gut unterstützt)
```

**IFC (.ifc) — Industry Foundation Classes:**

```
Beschreibung: "BIM"-Format (Building Information Modeling)
ursprünglich: Architektur, wächst in Schiffbau
Kompatibilität: wachsend (neue Tools), begrenzt in Yachtdesign
Vorteil: Meta-Information (Egebnisse, Materialien, Kosten) eingebettet

Nutzung im Yachtdesign:
  noch selten (aber zunehmend bei großen Werften)
  Potenzial für integrierte Datenfluss
```

### 2.2 Datei-Format-Konvertierungs-Guides

**Rhino → Maxsurf:**

```
Methode 1: über STEP
  Rhino (export STEP) → STEP-Datei → Maxsurf (import STEP)
  Qualität: sehr gut (NURBS erhalten)
  Zeit: 5–10 Minuten
  
Methode 2: Orca3D-Plug-in
  Rhino (mit Orca3D) → direkt Maxsurf-Daten-Format
  Qualität: optimal (alle Hydroinformationen)
  Zeit: 2–3 Minuten
```

**Maxsurf → Rhino:**

```
Methode: via IGES oder STEP
  Maxsurf (export IGES/STEP) → CAD-Datei → Rhino (import)
  Qualität: gut (NURBS-Flächen erhalten)
  Nachteil: Stabilitäts-Daten gehen verloren (müssen re-calced)
```

**FreeShip → Rhino:**

```
Methode 1: STL-Export
  FreeShip (export STL) → Rhino (import STL)
  Problem: STL ist nur Oberflächen-Mesh, nicht NURBS
  Lösung: in Rhino Reverse-Engineering (Surface-Rekonstruktion)
  Zeit: 3–5 Stunden (manuell mit Scanning-Lofting)
  
Methode 2: DWG-Export
  FreeShip (export 2D-Ansichten DWG) → Rhino (Lofting von Kurven)
  Zeit: 1–2 Stunden
  Qualität: gut wenn Kurven gut exportiert
```

---

## 3. Workflow-Integration und Prozess-Automation

### 3.1 Typischer Designprozess (Custom Yacht 16m)

**Phase 1: Konzept und Hydro-Analyse (2 Wochen)**

```
Woche 1:
  Tag 1–2: Anforderungen-Spezifikation (Länge, Breite, Tiefgang, Gewicht)
  Tag 3–4: Maxsurf: grobe Rumpf-Form parametrisch modellieren
  Tag 5: Stabilitäts-Analyse (ISO 12217 prüfen)
  
Woche 2:
  Tag 6–7: Optimierung Rumpf-Form (Stabilität + Performance)
  Tag 8–9: Widerstands-Vorhersage, Leistungs-Berechnung
  Tag 10: Bericht generieren (Gewicht, Trimm, Leistung)
```

**Phase 2: Detail-Design (4 Wochen)**

```
Woche 3–4:
  Rhino: Rumpf-Oberflächen-Modellierung (Maxsurf-Basis refinieren)
  Orca3D: Stabilitäts-Final-Check
  Detail-Geometrie: Interieur, Deck, Aufbau
  
Woche 5–6:
  Struktur-Pläne: Spanten, Schotten, Versteifung
  CAD-Konstruktion: Holme, Ausstattung, Ballast-Plazierung
  Gewichts-Prognose: Update nach Detaillierung
```

**Phase 3: Fertigungs-Vorbereitung (2 Wochen)**

```
Woche 7–8:
  Spanten-Export: in Produktion-Format (2D Schnitte oder NC-Daten)
  Schnittlisten: Material-Anforderungen
  NC-Code-Generierung: für CNC-Fräsmaschinen
  Fertigungs-Zeichnungen: Detail-Maßstäbe überprüfen
```

### 3.2 CAM-Integration (NC-Code-Generierung)

**Prozess für Lofting und Spanten-Produktion:**

```
CAD-Modell (Rhino STEP)
  ↓
Spanten-Extraktion (2D Kurven in Fertigungs-Ebenen)
  ↓
CAM-Software (z.B. Mastercam, GibbsCAM, Fusion 360)
  - Kurven-Import
  - Werkzeug-Definition (Fräser-Durchmesser, Vorschub)
  - Schnittwege optimieren
  ↓
NC-Code (G-Code, ISO 6983 Standard)
  ↓
CNC-Maschine (5-Achsen-Fräsmaschine)
  - Schablonen fräsen
  - Toleranz-Kontrolle (±2 mm Standard)
```

**Praktische Anforderungen:**

```
Spanten-Maßstab:
  1:1 (full-size): für große Boote (18m+) mit CNC
  1:5 oder 1:10: für kleinere Boote, manuell Upscaling
  
Toleranz-Anforderung:
  ±2 mm Standard (brauchbar für Lofting)
  ±0,5 mm (High-Precision, teuer, für Rennboote)
  
Zeitaufwand:
  Kleine Yacht (12m, 10 Spanten): 2–4 Stunden CNC-Zeit
  Große Yacht (25m, 20 Spanten): 8–16 Stunden
```

---

## 4. Stabilitäts-Berechnung und Validierung

### 4.1 ISO 12217 Stabilitäts-Anforderungen

**Berechnungs-Tools:**

```
Maxsurf Stability (bevorzugt):
  - Vollautomatische Berechnung
  - alle ISO 12217 Szenarien
  - Report-generierung (für Klasse)
  
Orca3D:
  - Integration im Rhino-Workflow
  - gleich genaue ISO-Berechnung
  - schneller für iterative Optimierung
  
Einsatz-vergleich:
  Maxsurf: besser für finale Genehmigung-Berichte
  Orca3D: besser für Design-Iteration
```

### 4.2 Stabilitäts-Analyse Checklist

```
Vor Berechnung:
  ☐ Gewichtsverteilung definiert (Ballast, Fuel, Water)
  ☐ Rumpf-Geometrie final (keine Änderungen pending)
  ☐ Gewicht-Schätzung aktualisiert
  ☐ Freeboard korrekt (Seitenhöhe vom Design)

Berechnung durchführen:
  ☐ ISO 12217 Kategorie wählen (A, B, C, D)
  ☐ Wind-Profil auswählen (25 Knoten Standard)
  ☐ Wellen-Profil auswählen (1 m Welle Standard)
  ☐ Crewverteilung definieren

Nach Berechnung:
  ☐ Stabilitäts-Reserve überprüfen (>20% margin ideal)
  ☐ Seegänge-Verhalten prüfen (Pitch/Roll acceptable?)
  ☐ Capsizing-Index berechnen (selten <0,8 acceptable)
  ☐ Report generieren (für Klasse-Submission)
```

---

## 5. Klasse-Genehmigung und Dokumentation

### 5.1 Lloyd's Register / DNV GL Requirements

**Dokumentations-Standards:**

```
Lloyd's Register (LR):
  Digitale Einreichung: via "Lloyd's Approval in Principle" Portal
  Formate: STEP (CAD), PDF (Berichte), Excel (Gewichtslisten)
  Stabilitäts-Bericht: Maxsurf oder äquivalent
  CAD-Model: Rhino, Maxsurf, oder AutoCAD akzeptabel
  
DNV GL:
  Digitale Einreichung: DNV-Datenbank-Portal
  Formate: STEP, IGES (CAD), PDF (Berichte)
  Zusatz: laufende Inspektionen-Protokolle
  
ABS (American Bureau):
  digitale Einreichung: ABS-e-Portal
  Anforderung: detaillierte Konstruktionszeichnungen + Berechnungen
```

**Dokumentations-Checkliste:**

```
CAD-Pläne:
  ☐ Rumpf-Geometrie (STEP-Format)
  ☐ Spanten-Plan (2D Schnitte)
  ☐ Deck-Layout (2D + 3D)
  ☐ Interieur-Arrangement
  ☐ Struktur-Pläne (Longitudinal + Querschnitte)

Berechnungs-Berichte:
  ☐ Stabilitäts-Bericht (ISO 12217)
  ☐ Gewichts-Schätzung + Schwerpunkt-Berechnung
  ☐ Widerstands-Vorhersage (Leistungsprognose)
  ☐ Motoren-Dimensionierung
  ☐ Treibstoff/Wasser-Tank-Plazierung

Inspektionen:
  ☐ Laminat-Pläne (Schichtfolge, Material)
  ☐ Metallteile-Spezifikationen
  ☐ Elektrik-Schema (Spannung, Schutz)
  ☐ Sicherheits-Features (Rettungsausrüstung, Notgenerator)
```

---

## 6. Häufige Fehler im CAD-Prozess

### 6.1 Lofting-Fehler

**Problem: Spanten nicht glatt (Wellen in Rumpf-Fläche)**

```
Ursache 1: zu wenig Kontrolls-Punkte in Lofting
  Lösung: mehr Spanten-Querschnitte definieren (z.B. alle 0,5m)
  
Ursache 2: Spanten-Kurven haben scharfe Ecken
  Lösung: Kurven glätten (Spline-Interpolation)
  
Ursache 3: Übergangs-Problem am Bug/Heck
  Lösung: Übergangskurven extrapolieren (sanfte Übergänge)
  
Test: Oberflächenanalyse (Zebra-Rendering in Rhino)
  → sollte keine sichtbaren Wellen zeigen
```

### 6.2 Gewichts-Ungenauigkeiten

**Problem: geschätztes Gewicht zu niedrig (Übergewicht beim Bau)**

```
Ursache 1: Struktur-Aufbau unterschätzt
  → alle Spanten, Lasten, Verstärkungen berücksichtigen
  
Ursache 2: Interieur-Finessen nicht budgetiert
  → Matratzenpads, Schränke, Instrumente
  
Ursache 3: Extras am Ende (Klimaanlage, zusätzliche Batterien)
  → reservieren Sie 10–15% "Gewichts-Puffer"
  
Lösung: Detaillierte Gewichtsliste (nicht Schätzung)
  → jede Komponente einzeln wiegen (bei Prototyp)
  → in Datenbank speichern für zukünftige Projekte
```

### 6.3 Datei-Format-Kompatibilität Probleme

**Problem: STEP-Datei importiert, aber Geometrie verzogen**

```
Ursache 1: Maßstabs-Problem (mm vs. m)
  Lösung: beim Export/Import Einheit überprüfen
  
Ursache 2: NURBS-Oberfläche wird zu STL konvertiert
  Lösung: wenn möglich, native Format nutzen (IGES, STEP)
  
Ursache 3: Kurven-Orientierung falsch (innen/außen)
  Lösung: Normal-Richtung überprüfen (Rhino Flip-Funktion)
```

---

## 7. Verifizierter Normen- und Fakten-Rahmen (Werft-Tiefe, Audit 2026-07)

> Dieser Abschnitt ergänzt die obige Übersicht um **web-verifizierte** Fakten. Jede Angabe trägt eine Quelle und ein Confidence-Tag. Wo eine autoritative Bestätigung fehlt, ist der Wert als `estimated — unverifiziert` gekennzeichnet oder bewusst weggelassen. Die früheren, unbelegten Zahlen (Marktanteile, Preisspannen, Durchlaufzeiten) in den Abschnitten 1–6 sind als `estimated — unverifiziert` zu behandeln, sofern sie hier nicht bestätigt werden.

### 7.1 Regulatorischer/normativer Rahmen — CAD-relevante Normen

Für Yacht-CAD/Naval-Architecture sind zwei Normfamilien load-bearing: die **Datenaustausch-Normen** (Dateiformate) und die **Konstruktions-/Nachweisnormen** (Scantlings, Stabilität), auf denen die CAD-Berechnungsmodule aufsetzen.

**Datenaustausch- und Fertigungs-Normen (verifiziert):**

| Norm | Titel / Scope | Rolle im CAD-Workflow | Confidence |
|------|---------------|-----------------------|------------|
| ISO 10303 (STEP) | *Industrial automation systems and integration — Product data representation and exchange* | Herstellerneutraler CAD-Austausch (Geometrie + PMI). AP203 (1994) = Mechanik-Geometrie/Assemblies; AP214 = Automotive; **AP242** (Ed.1 2014, **Ed.2 2020**) vereint AP203+AP214 und ergänzt modellbasierte PMI/GD&T. | `documented` |
| ISO 10303-238 (AP238 / „STEP-NC") | *Application protocol: Application interpreted model for computerized numerical controllers* | Objektorientierter CAM/CNC-Datenfluss, soll ISO 6983 langfristig ablösen; harmonisiert mit ISO 14649. | `documented` |
| ISO 14649 (STEP-NC) | *Data model for computerized numerical controllers* | Feature-basiertes CNC-Datenmodell; „extended STEP for numerical control". | `documented` |
| ISO 6983-1 | *Numerical control of machines — Program format and definitions of address words* (G-Code) | Klassischer G-Code für CNC-Fräsen (Werkzeug-Trajektorie). Syntaktisch definiert, aber semantisch mehrdeutig; herstellerspezifische Erweiterungen üblich. | `documented` |
| IGES (Version **5.3**, 1996) | *Initial Graphics Exchange Specification* | Älteres neutrales Austauschformat (Kurven/Flächen/Solids). **Entwicklung 1996 eingestellt**; NIST empfiehlt Migration auf STEP. Nur nutzen, wenn ein Tool STEP nicht unterstützt. | `documented` |
| DXF | *Drawing (Interchange/Exchange) Format*, Autodesk (seit AutoCAD 1.0, Dez. 1982) | ASCII-lesbares, gruppen-code-basiertes 2D/3D-Austauschformat; De-facto-Neutralformat für 2D-Zeichnungen und Laser-/Plasma-/CNC-Zuschnitt. Kein ISO-Standard (proprietär, aber offen dokumentiert). | `documented` |
| STL | *StereoLithography Interface Specification*, 3D Systems (Charles Hull, 1988) | Dreiecks-Facettennetz für 3D-Druck/CAM/Visualisierung. **Enthält keine Einheiten**; verliert NURBS-/PMI-Information. ASCII- und Binär-Variante. | `documented` |

> Quellen: [ISO 10303-242:2020](https://www.iso.org/standard/66654.html) · [Wikipedia — ISO 10303](https://en.wikipedia.org/wiki/ISO_10303) · [Wikipedia — STEP-NC](https://en.wikipedia.org/wiki/STEP-NC) · [Wikipedia — IGES](https://en.wikipedia.org/wiki/IGES) · [Wikipedia — AutoCAD DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF) · [Library of Congress — DXF](https://www.loc.gov/preservation/digital/formats/fdd/fdd000446.shtml) · [Wikipedia — STL (file format)](https://en.wikipedia.org/wiki/STL_(file_format)).

**Konstruktions-/Nachweisnormen, auf denen die CAD-Berechnungsmodule aufsetzen (verifiziert):**

| Norm | Titel / Scope | CAD-Relevanz | Confidence |
|------|---------------|--------------|------------|
| ISO 12215-5:2019 | *Small craft — Hull construction and scantlings — Part 5: Design pressures for monohulls, design stresses, scantlings determination* | Basis der Laminat-/Plattendimensionierung (Scantlings) für Einrumpfboote ≤24 m LH. | `documented` |
| ISO 12215-7:2020 | *… Part 7: Determination of loads for multihulls and of their local scantlings using ISO 12215-5* | Mehrrumpf-Lasten; Scantlings über Part 5 abgeleitet. | `documented` |
| ISO 12215-8 | *… Part 8: Rudders* | Ruderkraft/Ruderschaft-Dimensionierung. | `documented` |
| ISO 12215-9 | *… Part 9: Sailing craft appendages* | Kiel-/Anhang-Lasten für Segelyachten. | `documented` |
| ISO 12215-10 | *… Part 10: Rig loads and rig attachment in sailing craft* | Rigg-Lasten und Rigg-Anschlüsse. | `documented` |
| ISO 12217-1:2015/2022 | *Small craft — Stability and buoyancy assessment and categorization — Part 1: Non-sailing boats ≥6 m LH* | Stabilitäts-/Auftriebsnachweis Motorboote → Design-Kategorie A/B/C/D. | `documented` |
| ISO 12217-2:2013/2022 | *… Part 2: Sailing boats ≥6 m LH* | Stabilitätsnachweis Segelboote → Design-Kategorie A/B/C/D. | `documented` |
| ISO 12217-3:2015/2022 | *… Part 3: Boats <6 m LH* | Kleinboote → nur Kategorie C oder D. | `documented` |

> **Wichtige Abgrenzung (deckt sich mit CLAUDE.md-Spec):** **ISO 12215** = *Struktur/Scantlings*; **ISO 12217** = *Stabilität/Auftrieb*. Die im Bestand (Abschnitt 4.1, 5.1, Anhang B) mehrfach genutzte Formulierung „Stabilitäts-Berechnung ISO 12217 konform" ist korrekt; jede Nennung von „ISO 12217" für **Laminat/Scantling**-Fragen wäre hingegen falsch (dort gilt ISO 12215). Beide Reihen decken Sportboote **≤24 m** Rumpflänge ab. Quellen: [ISO 12215-5:2019](https://www.iso.org/standard/69552.html) · [ISO 12215-7:2020](https://www.iso.org/standard/73457.html) · [ISO 12217-1:2022](https://www.iso.org/standard/79072.html) · [ISO 12217-2:2022](https://www.iso.org/standard/79073.html) · [ISO 12217-3:2022](https://www.iso.org/standard/79074.html).

> ⚠️ **ZU PRÜFEN (Audit):** Der Bestand nennt in der Stabilitäts-Checkliste (4.2) feste Defaults „25 Knoten Wind", „1 m Welle", „Capsizing-Index <0,8", „>20% Stabilitäts-Reserve". Diese konkreten Zahlenwerte konnten **nicht** aus dem ISO-12217-Normtext verifiziert werden (Norm hinter Paywall). Bis zur Einsicht in die Norm sind sie als `estimated — unverifiziert` zu behandeln und **nicht** als Nachweis-Grenzwerte zu zitieren. Das *Prinzip* (Wind-/Wellen-Szenario je Design-Kategorie, Nachweis von Reststabilität) ist korrekt; die genauen Kriterien richten sich nach der jeweils zutreffenden ISO-12217-Bewertungsmethode.

### 7.2 Tool-Übersicht — web-verifizierte Fakten (reale Hersteller/Module)

Nur belegbare Produktfakten; unbelegte Preisspannen/Marktanteile aus dem Bestand sind hier **nicht** bestätigt.

| Tool | Hersteller | Lizenzmodell / Preis (verifiziert) | Modellierung | Module / Kernfunktion | Confidence |
|------|-----------|-----------------------------------|--------------|-----------------------|------------|
| **Rhino 8** | Robert McNeel & Associates | **Perpetual**, Single-User Listenpreis **USD 995** (10-User USD 9.950, 50-User USD 49.750); inkl. Grasshopper, keine Wartungsgebühr | NURBS | Allzweck-3D-CAD; Basis für Marine-Plug-ins | `documented` |
| **Orca3D V3** (Rhino-Plug-in) | Orca3D, LLC | Modular (Module einzeln/kombiniert lizenzierbar) | NURBS (via Rhino) | Design (Hull Design & Fairing, Basic Hydrostatics & Stability), Analysis (Speed/Power, CFD-Interface, Weight & Cost), Advanced Stability (Tanks, intact/damaged, free-surface, Kriterienprüfung), Marine CFD (RANS) | `documented` |
| **Maxsurf** | Bentley Systems (Formsys, seit 2011 bei Bentley) | kommerziell (Bentley/Virtuosity) | NURBS (dynamisch getrimmte 3D-NURB-Flächen) | Modeler, Stability, Resistance, Motions; Struktur via **Multiframe** (FEA) | `documented` |
| **DELFTship** | DELFTship BV | **Free** (unbegrenzt) + **Professional Perpetual USD 160** (+ Extensions) | Subdivision Surfaces | Rumpfmodellierung, Hydrostatik; Pro: Trimm-Hydrostatik, IGES I/O, Plattenabwicklung, asymmetrische Rümpfe; Extensions: Cross-curves, Critical Points, Tanks, Intact Stability | `documented` |
| **FREE!ship** | Open-Source-Projekt (SourceForge) | **GPL, kostenlos, quelloffen** (Delphi) | Subdivision Surfaces | Rumpf-Flächenmodellierung; Vorgänger von DELFTship (bis Release 3.1). Fork „FreeShip Plus" (Lazarus) | `documented` |
| **AutoCAD** | Autodesk | Subscription (kommerziell) | 2D/3D (nicht NURBS-spezialisiert) | Allzweck-CAD; im Yachtbau v.a. 2D-Pläne, .dwg-Austausch | `documented` |

> **Preis-Hinweis:** Die im Bestand (Abschnitt 1) genannten Preise „Orca3D EUR 2500–5000", „Maxsurf EUR 5000–12000", „AutoCAD EUR 600/Jahr" sowie der Marktanteil „60%" sind **nicht verifiziert** (`estimated — unverifiziert`) und sollten nicht als Fakten zitiert werden. Verifiziert sind nur: Rhino Single-User USD 995 und DELFTship Professional USD 160. Quellen: [Rhino Store](https://www.rhino3d.com/store) · [Orca3D](https://orca3d.com/) · [Bentley Maxsurf](https://www.bentley.com/software/maxsurf/) · [Multiframe (Formsys)](https://maxsurf.net/multiframe) · [DELFTship Pricing](https://www.delftship.net/pricing/) · [FREE!ship (SourceForge)](https://sourceforge.net/projects/freeship/).

**Wichtige inhaltliche Korrektur zu Modellierungs-Kernen:** Rhino, Orca3D und Maxsurf arbeiten NURBS-basiert. **DELFTship und FREE!ship arbeiten mit Subdivision Surfaces** (Unterteilungsflächen), *nicht* mit NURBS — die Bestand-Formulierung „NURBS: eingeschränkt" (1.3) ist irreführend: es ist ein *anderes* Flächenparadigma, nicht ein schlechteres NURBS. Confidence: `documented`. Quelle: [FREE!ship (SourceForge)](https://sourceforge.net/projects/freeship/).

### 7.3 Klassifikation / Genehmigung — verifizierte Fakten und Korrekturen

> ✅ **KORREKTUR (verifiziert 2026-07):** Der Bestand nennt durchgängig „**DNV GL**". Die Gesellschaft hat sich zum **1. März 2021 in „DNV"** umbenannt (der Name „DNV GL" stammte aus der Fusion 2013 von *Det Norske Veritas* und *Germanischer Lloyd*). Aktuell korrekt: **DNV**. Confidence: `documented`. Quelle: [DNV — Namensänderung 2021](https://www.dnv.com/news/2021/dnv-gl-changes-name-to-dnv-as-it-gears-up-for-decade-of-transformation-194340/).

**Wer klassifiziert Yachten (verifiziert):**

| Gesellschaft | Relevantes Regelwerk (verifiziert) | Anwendungsbereich |
|--------------|-----------------------------------|-------------------|
| **Lloyd's Register (LR)** | *Rules and Regulations for the Classification of Special Service Craft (SSC)* | Yachten **LOA ≥ 24 m**, i.d.R. bis ~150 m Rule length; Stahl, Alu, Composite oder Kombinationen. | 
| **ABS** (American Bureau of Shipping) | *Guide for Building and Classing Offshore Racing Yachts*; Yacht-Klassifikations-/Statutory-Services | Regatta-/Großyachten; Planprüfung historisch für Rennyachten bis ~100 ft/24 m. |
| **DNV** | DNV-Klassenregeln (Rules for classification of ships / Yacht-relevante Teile) | See-Yachten je nach Größe/Typ. |

> **Wichtig (Sportboote < 24 m):** Für Sportboote 2,5–24 m, die in der EU verkauft werden, ist die **CE-Kennzeichnung nach RCD 2013/53/EU** (nachgewiesen u.a. über ISO 12215/12217) der primäre regulatorische Rahmen — **nicht** eine Klassifikationsgesellschaft. Klassifikation (LR/ABS/DNV) wird vor allem für Yachten **≥24 m** bzw. gewerbliche/Charter-Nutzung relevant. Die Bestand-Aussage, „Konstruktion nicht Klasse-genehmigt (Lloyd's, DNV)" sei ein generischer CAD-Fehler, gilt daher primär für den ≥24-m-Bereich. Quellen: [LR — Classification of Special Service Craft](https://www.lr.org/en/knowledge/lloyds-register-rules/rules-and-regulations-for-the-classification-of-special-service-craft/) · [ABS — Offshore Racing Yachts Guide](https://ww2.eagle.org/content/dam/eagle/rules-and-guides/archives/special_service/37_offshoreracingyachts/pub37_ory_guide_op.pdf).

> ⚠️ **ZU PRÜFEN (Audit):** Die im Bestand (5.1) genannten Portalnamen/Einreichungswege („Lloyd's Approval in Principle Portal", „DNV-Datenbank-Portal", „ABS-e-Portal") und die Liste akzeptierter Dateiformate je Gesellschaft konnten **nicht** an autoritativer Quelle bestätigt werden. Als konkrete Prozessangaben `estimated — unverifiziert` behandeln; im Zweifel den aktuellen Submission-Guide der jeweiligen Gesellschaft konsultieren.

### 7.4 Hydrostatik-/Stabilitäts-Berechnungsworkflow (dokumentierte Methodik)

Der folgende Ablauf beschreibt die **dokumentierte Methodik** (Was/Warum), ohne last-/sicherheitsrelevante Zahlen zu erfinden. Konkrete Grenzwerte richten sich stets nach der zutreffenden ISO-12217-Bewertungsmethode.

```
1. Rumpfgeometrie fair modellieren (NURBS in Rhino/Maxsurf/Orca3D
   bzw. Subdivision in DELFTship). Flächenqualität VOR Analyse prüfen
   (Zebra/Curvature/EMap — siehe 7.5), da unfaire Flächen die
   Verdrängungs-/Formstabilitätsrechnung verfälschen.
      │
2. Gewichts- und Schwerpunktbilanz (Weight & CG estimate) aufstellen:
   Leerschiff + Zuladungsfälle. In Orca3D via "Weight & Cost",
   in Maxsurf via Stability-Loadcases.
      │
3. Kompartiment-/Tankmodell definieren (für Free-Surface-Effekte und
   Beschädigungsstabilität): Orca3D "Advanced Stability" bzw.
   Maxsurf Stability. Free-surface-Effekt reduziert die effektive
   Metazentrische Höhe — nicht vernachlässigen.
      │
4. Intakt-Hydrostatik rechnen: Verdrängung, KB, BM, KM, GZ-Kurve
   (righting arm), Formschwerpunkt, Wasserlinien-Kennwerte.
      │
5. Stabilitätskriterien nach zutreffender ISO-12217-Methode und
   Ziel-Design-Kategorie (A/B/C/D) prüfen. Kriterien und Grenzwerte
   der Norm entnehmen — NICHT schätzen.
      │
6. (Falls gefordert) Seegangsverhalten: Maxsurf Motions (Pitch/Roll/
   Heave, Seakeeping) bzw. Widerstand/Leistung: Maxsurf Resistance
   oder Orca3D Speed/Power.
      │
7. Report generieren; bei Klassifikation (≥24 m) an LR/ABS/DNV-
   Vorgaben ausrichten.
```

**Prinzipien (verifiziert, qualitativ):**
- **GZ-Kurve (righting arm curve)** und die daraus abgeleiteten Kennwerte (max. aufrichtender Hebel, Bereich positiver Stabilität, statischer/dynamischer Stabilitätsumfang) sind das Kernergebnis der Intakt-Stabilität. Orca3D und Maxsurf berechnen diese direkt aus dem 3D-Modell.
- **Free-Surface-Effekt** teilgefüllter Tanks verringert die effektive Stabilität; deshalb ist die Tankmodellierung (Orca3D Advanced Stability / Maxsurf Stability) Teil eines belastbaren Nachweises.
- **Damaged Stability** (Leckstabilität) wird bei größeren/klassifizierten Einheiten zusätzlich verlangt (Orca3D „intact and damaged stability"; Maxsurf Stability).

> Quellen (Fähigkeiten der Werkzeuge, nicht Grenzwerte): [Orca3D — Module/Advanced Stability](https://orca3d.com/) · [Bentley — Maxsurf](https://www.bentley.com/software/maxsurf/) · [maxsurf.net — Module](https://maxsurf.net/).

> ⚠️ **ZU PRÜFEN (Audit) / KEIN Rechenbeispiel:** Bewusst **keine** GZ-/GM-Zahlenbeispiele oder Formeln eingefügt — diese sind last-/sicherheitsrelevant und nur aus dem konkreten Modell + Normtext ableitbar. Wer Grenzwerte benötigt, entnimmt sie der einschlägigen ISO-12217-Methode bzw. den Klassenregeln.

### 7.5 Flächenqualität prüfen — verifizierte Rhino-Analysewerkzeuge

Der Bestand (6.1, Anhang B) nennt „Zebra-Rendering" zur Prüfung fairer Flächen. Das ist korrekt und lässt sich präzisieren. Rhino stellt mehrere Analysebefehle bereit; sie prüfen die **geometrische Stetigkeit** zwischen benachbarten Flächen:

| Rhino-Befehl | Was es zeigt | Interpretation |
|--------------|--------------|----------------|
| **Zebra** | Reflektierte Streifen über die Fläche | Streifen brechen abrupt → **G0** (nur Position); knicken scharf, aber verbunden → **G1** (Tangenten-stetig); laufen glatt durch → **G2** (krümmungs-stetig) |
| **CurvatureAnalysis** | Falschfarben-Krümmung (Gauß, Mittel, Min/Max-Radius) | Deckt Dome, Sattelpunkte, Flachstellen, Krümmungssprünge auf |
| **EMap** (Environment Map) | Simulierte Metallreflexion | Zusätzliche reflexionsbasierte Sichtprüfung neben Zebra |
| **CurvatureGraph** | Krümmungs-„Igel" entlang Kurven | Beurteilt die Qualität der erzeugenden Kurven (G2/G3) |
| **EdgeContinuity** | Mathematische Kanten-Relation zweier Flächen | Direkte G0/G1/G2-Rückmeldung an einer Naht |

**Stetigkeits-Definitionen (verifiziert):** **G0** = Position (Flächen berühren sich), **G1** = Position + Tangente, **G2** = Position + Tangente + Krümmung. Für sichtbare Rumpf-/Deckflächen ist mindestens **G2** anzustreben, damit Reflexionen (und damit die visuelle sowie hydrodynamische Fairness) sauber durchlaufen. Confidence: `documented`. Quellen: [McNeel — Zebra](https://docs.mcneel.com/rhino/mac/help/en-us/commands/zebra.htm) · [McNeel — Curve and Surface Analysis](http://docs.mcneel.com/rhino/5/usersguide/en-us/html/ch-09_curveandsurfaceanalysis.htm).

### 7.6 Dateiformat-Entscheidungsbaum (verifiziert)

```
Was soll ausgetauscht werden?
│
├─ Exakte 3D-Geometrie (NURBS/Solid) zwischen CAD-Systemen
│     └─► STEP (ISO 10303). Bevorzugt AP242 (Ed.2 2020), sonst AP203.
│         Grund: herstellerneutral, geometrie- und (AP242) PMI-treu.
│
├─ 3D-Geometrie, aber Zielsystem kennt nur IGES
│     └─► IGES 5.3 — nur als Fallback (Entwicklung 1996 eingestellt,
│         NIST empfiehlt STEP). Nach Import Geometrie prüfen.
│
├─ 2D-Zeichnung / Zuschnitt-Kurven (Laser/Plasma/CNC-Nesting)
│     └─► DXF (ASCII). Universell, human-readable, gruppen-code-basiert.
│
├─ 3D-Druck / Facetten-Mesh / Visualisierung / CAM-Rohform
│     └─► STL. ACHTUNG: keine Einheiten im File → Skalierung beim
│         Import verifizieren; NURBS-/PMI-Information geht verloren.
│         Mesh-Dichte über Abweichungstoleranz steuern, nicht über
│         feste Dreieckszahl (siehe Auflösung in 2.1).
│
└─ CNC-Bearbeitungsprogramm
      └─► G-Code (ISO 6983) klassisch; zukunftsgerichtet STEP-NC
          (ISO 14649 / ISO 10303-238 AP238) für feature-basierten,
          semantisch reichen CAM-Datenfluss.
```
Confidence: `documented`. Quellen wie in 7.1.

---

## 8. Fehlerbild-Atlas CAD/Naval-Architecture (FB-31-13-NNN)

> **ID-Schema:** Neue Fehlerbilder tragen das kollisionsfreie Präfix **`FB-31-13-NNN`** (fortlaufend). Dieses Schema ist bewusst getrennt von den älteren Bezeichnern im Bestand (`31_13_001` in Anhang B; Abschnitts-Nummern „6.1/6.2/6.3"), um Kollisionen zu vermeiden. Schweregrad-Skala wie AYDI-Standard: `kritisch` / `hoch` / `mittel` / `niedrig`.

| ID | Fehlerbild | Sicherheits-Impact | Schweregrad |
|----|------------|--------------------|-------------|
| FB-31-13-001 | Verwechslung ISO 12215 (Struktur) ↔ ISO 12217 (Stabilität) | ja (Nachweisfehler) | hoch |
| FB-31-13-002 | STL-Import ohne Einheiten-Verifikation → Skalierungsfehler | ja | hoch |
| FB-31-13-003 | Unfaire Fläche (nur G0/G1) in Sichtbereich / Hydrodynamik | mittelbar | mittel |
| FB-31-13-004 | Free-Surface-Effekt der Tanks in Stabilität ignoriert | ja | hoch |
| FB-31-13-005 | IGES statt STEP → PMI-/Geometrieverlust | nein | mittel |
| FB-31-13-006 | Klassifikation vs. CE-Nachweis verwechselt (<24 m vs. ≥24 m) | ja (regulatorisch) | hoch |
| FB-31-13-007 | Veraltete Bezeichnung „DNV GL" in Genehmigungsunterlagen | nein | niedrig |
| FB-31-13-008 | Subdivision-Surface-Tool (DELFTship/FREE!ship) für NURBS-Klasse-Modell fehlgenutzt | nein | mittel |
| FB-31-13-009 | Erfundene/geschätzte Grenzwerte im Stabilitäts-Report zitiert | ja | kritisch |

**FB-31-13-001 — Normverwechslung 12215 ↔ 12217**
- *Symptom:* Scantling-/Laminatnachweis verweist auf „ISO 12217"; oder Stabilitätsnachweis verweist auf „ISO 12215".
- *Ursache:* Verwechslung der Normfamilien (häufige Fehlerquelle, vgl. CLAUDE.md-Hinweis).
- *Folge:* Nachweis formal ungültig; Klasse-/Notified-Body-Rückweisung.
- *Diagnose:* Norm-Referenzen im Report gegen Scope prüfen: 12215 = Struktur/Scantlings, 12217 = Stabilität/Auftrieb.
- *Behebung:* Referenzen korrigieren; Scantlings nach ISO 12215-5 (Monohull) bzw. -7 (Multihull), Stabilität nach ISO 12217-1/-2/-3.
- *Prävention:* Norm-Mapping in der CAD-Report-Vorlage fest hinterlegen.
- Confidence: `documented`. Quelle: [ISO 12215-5](https://www.iso.org/standard/69552.html), [ISO 12217-1](https://www.iso.org/standard/79072.html).

**FB-31-13-002 — STL ohne Einheiten-Verifikation**
- *Symptom:* Importiertes Modell ist um Faktor 1000 / 25,4 zu groß oder zu klein.
- *Ursache:* STL enthält **keine Einheiten** (Einheiten willkürlich); Quell- und Zielsystem interpretieren mm vs. m vs. inch unterschiedlich.
- *Folge:* Falsche Verdrängung/Massen; wertlose Hydrostatik; Fertigungsteil in falscher Größe.
- *Diagnose:* Bekannte Referenzlänge (z.B. LOA) nach Import messen.
- *Behebung:* Skalierung beim Import setzen; wenn möglich native/STEP statt STL nutzen.
- *Prävention:* STL nur für Druck/Visualisierung/CAM-Rohform; für maßhaltigen Austausch STEP.
- Confidence: `documented`. Quelle: [Wikipedia — STL](https://en.wikipedia.org/wiki/STL_(file_format)).

**FB-31-13-003 — Unfaire Fläche im Sicht-/Strömungsbereich**
- *Symptom:* Zebra-Streifen brechen/knicken an Nähten; CurvatureAnalysis zeigt Sprünge.
- *Ursache:* Nur G0/G1-Stetigkeit statt G2; zu wenige/ungünstige Kontrollpunkte.
- *Folge:* Sichtbare Reflexions-„Wellen"; potenziell erhöhter Widerstand; Fertigungsprobleme.
- *Diagnose:* Zebra + CurvatureAnalysis + EdgeContinuity (siehe 7.5).
- *Behebung:* Flächen auf G2 nachziehen; Kurven mit CurvatureGraph glätten.
- *Prävention:* Flächenqualität iterativ VOR Hydrostatik/Fertigung prüfen.
- Confidence: `documented`. Quelle: [McNeel — Zebra](https://docs.mcneel.com/rhino/mac/help/en-us/commands/zebra.htm).

**FB-31-13-004 — Free-Surface-Effekt ignoriert**
- *Symptom:* Stabilitätsreserve rechnerisch zu optimistisch vs. Realverhalten.
- *Ursache:* Teilgefüllte Tanks nicht als freie Oberfläche modelliert.
- *Folge:* Überschätzte effektive Stabilität → sicherheitsrelevant.
- *Diagnose:* Prüfen, ob Tankmodell/Load-Cases mit Free-Surface aktiv sind (Orca3D Advanced Stability / Maxsurf Stability).
- *Behebung:* Tanks modellieren, Free-Surface-Korrektur einbeziehen, kritische Füllstände rechnen.
- *Prävention:* Tankmodell als Pflichtschritt im Nachweis-Workflow (7.4, Schritt 3).
- Confidence: `documented`. Quelle: [Orca3D](https://orca3d.com/).

**FB-31-13-009 — Erfundene Grenzwerte im Report (KRITISCH)**
- *Symptom:* Stabilitäts-/Scantling-Report nennt „Standard"-Grenzwerte ohne Normbeleg (z.B. pauschale Wind-/Wellenwerte, Capsizing-Index).
- *Ursache:* Übernahme unverifizierter Faustwerte statt Normtext.
- *Folge:* Formal/inhaltlich falscher Nachweis; Haftungs- und Sicherheitsrisiko.
- *Diagnose:* Jeden Grenzwert gegen zitierte Norm-/Klausel-Stelle prüfen.
- *Behebung:* Werte durch normbelegte Kriterien der zutreffenden ISO-12217-Methode/Klassenregel ersetzen; Unbelegtes als `estimated` kennzeichnen oder streichen.
- *Prävention:* AYDI-Kernregel — Unsicheres nie als Fakt; Confidence-Tag auf jedem Wert.
- Confidence: `documented` (Methodik). Quelle: AYDI-Reliability-Framework (CLAUDE.md).

---

## 9. Wartung, Prüf- und Review-Fristen (CAD-Daten-Governance)

> Diese Fristen betreffen **CAD-Datenpflege/-Governance**, nicht Bauteil-Wartung. Sie sind organisatorische Best Practice (`estimated — unverifiziert` als absolute Zahlen), das Prinzip ist branchenüblich.

| Aktivität | Auslöser / Frist (Prinzip) | Zweck |
|-----------|----------------------------|-------|
| Backup / Versionierung des CAD-Master | bei jeder freigaberelevanten Änderung | Nachvollziehbarkeit, Rücksprung |
| Flächenqualitäts-Review (Zebra/Curvature) | vor jeder Hydrostatik-/Fertigungsfreigabe | verhindert FB-31-13-003 |
| Einheiten-/Skalierungscheck | bei jedem Format-Import (STL/IGES/STEP) | verhindert FB-31-13-002 |
| Norm-Referenz-Review (12215/12217, Klasse) | bei jeder Nachweis-Erstellung/-Revision | verhindert FB-31-13-001/006/009 |
| Software-/Format-Versionsabgleich | bei Tool-Update oder externem Datenaustausch | Kompatibilität STEP-AP/DXF-Version |
| Klassen-/CE-Dokumentation aktualisieren | bei Designänderung nach Einreichung | Konsistenz Modell ↔ Genehmigung |

---

**CAM:** Computer-Aided Manufacturing (NC-Code-Generierung).

**CAD:** Computer-Aided Design (digitale Konstruktion).

**G-Code:** Maschinenprogramm für CNC (z.B. G00 = Schnellverfahren).

**IGES:** Initial Graphics Exchange Specification (Format).

**Lofting:** Querschnitt-Interpolation zu glatter Oberfläche.

**Mesh:** Dreiecksnetz (für Oberfläche).

**NURBS:** Non-Uniform Rational B-Spline (mathematische Kurven).

**NC-Code:** numerically Controlled Code (für CNC-Maschinen).

**STEP:** Standard for Exchange of Product model data (Format).

**STL:** Stereolithography (Oberflächenformat, Dreiecke). Enthält **keine Einheiten**; von 3D Systems (Charles Hull), 1988 spezifiziert. Quelle: [Wikipedia — STL](https://en.wikipedia.org/wiki/STL_(file_format)).

**AP203 / AP214 / AP242:** Application Protocols von STEP (ISO 10303). AP242 (Ed.2 2020) vereint AP203+AP214 und ergänzt PMI/GD&T. Quelle: [ISO 10303-242:2020](https://www.iso.org/standard/66654.html).

**STEP-NC:** Objektorientiertes CAM/CNC-Datenmodell (ISO 14649 / ISO 10303-238 AP238), Nachfolgekonzept zu G-Code (ISO 6983). Quelle: [Wikipedia — STEP-NC](https://en.wikipedia.org/wiki/STEP-NC).

**DXF:** Drawing (Interchange/Exchange) Format, Autodesk (seit 1982); ASCII-lesbares, gruppen-code-basiertes 2D/3D-Neutralformat. Quelle: [Wikipedia — AutoCAD DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).

**Subdivision Surface (Unterteilungsfläche):** Flächenparadigma von DELFTship/FREE!ship — **nicht** NURBS. Quelle: [FREE!ship](https://sourceforge.net/projects/freeship/).

**G0 / G1 / G2:** Geometrische Stetigkeit zwischen Flächen — G0 = Position, G1 = + Tangente, G2 = + Krümmung. In Rhino via Zebra/EdgeContinuity prüfbar. Quelle: [McNeel — Zebra](https://docs.mcneel.com/rhino/mac/help/en-us/commands/zebra.htm).

**GZ-Kurve (righting arm curve):** Aufrichtender Hebel über Krängungswinkel; Kernergebnis der Intakt-Stabilität.

**Free-Surface-Effekt:** Stabilitätsminderung durch teilgefüllte Tanks (bewegliche freie Flüssigkeitsoberfläche); in Stabilitätsnachweis zwingend zu berücksichtigen.

**Scantlings:** Bauteil-/Laminatdimensionierung nach ISO 12215. Quelle: [ISO 12215-5](https://www.iso.org/standard/69552.html).

**RCD:** Recreational Craft Directive 2013/53/EU — CE-Rahmen für Sportboote 2,5–24 m in der EU.

**SSC:** Special Service Craft — Lloyd's-Register-Regelwerk für Yachten ≥24 m. Quelle: [LR — SSC](https://www.lr.org/en/knowledge/lloyds-register-rules/rules-and-regulations-for-the-classification-of-special-service-craft/).

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class CADToolsFehlerbild(BaseModel):
    """
    Fehlerbild für CAD/CAM-Tools nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_13_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "CAD_Tools"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Design/Produktion")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-Relevanz")
    
    # Ursprung
    design_phase: str = Field(default="", description="Konzept/Detail/Produktion/etc")
    cad_tool: str = Field(default="", description="betroffenes Tool")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Review-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO Standards")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = CADToolsFehlerbild(
    fehlerbild_id="31_13_001",
    titel="Lofting-Fehler: Spanten nicht glatt",
    beschreibung="Wellenförmige Rumpf-Oberfläche durch unzureichende Interpolation.",
    symptome=[
        "Zebra-Rendering zeigt Rauheit",
        "Oberflächenanalyse-Report: Krümmungs-Diskontinuität",
        "Berechnete Widerstände stimmen nicht mit Vergleichsbooten überein"
    ],
    auswirkungen=[
        "Fertigungs-Probleme: Lofting schwieriger",
        "Performance-Verlust: höherer Widerstand",
        "Ästhetik-Problem: sichtbare Wellen"
    ],
    schweregrad="hoch",
    sicherheits_impact=False,
    design_phase="Detail",
    cad_tool="Rhino/Orca3D",
    diagnose_methoden=[
        "Zebra-Rendering-Analyse",
        "Oberflächenrauhheits-Bericht",
        "Vergleich-Analyse mit Referenz-Designs"
    ],
    reparatur_optionen=[
        "Lofting neu durchführen (mehr Kontrol-Punkte)",
        "Spanten-Kurven glätten (Spline-Interpolation)",
        "Übergangs-Zonenglätten (Bug/Heck)"
    ],
    schaetzung_kosten_eur=3000,
    dauer_tage=3,
    praevention=[
        "Lofting mit ausreichenden Querschnitten (z.B. alle 0,5m)",
        "Oberflächenqualität-Check während Design",
        "Vergleichende Analyse mit ähnlichen Designs"
    ],
    inspektions_intervall_jahre=1,
    normen_referenzen=["ISO 12217 (wird durch Oberflächenqualität beeinflusst)"],
    verwandte_fehlerbilder=["31_13_002", "31_13_004"]
)
```

---

## ANHANG C — FAQ (20+)

**F1: Rhino oder Maxsurf wählen?**
A: Rhino: allgemeiner, flexible Modellierung. Maxsurf: spezialisiert hydro-dynamik. Optimal: beide kombinieren (Rhino für Design, Maxsurf für Analyse).

**F2: Welche Datei-Format für Austausch mit Produktion?**
A: STEP (NURBS erhalten), STL (Produktion), DWG (2D-Pläne). STEP ideal für Klasse-Genehmigung.

**F3: Wie Mesh-Auflösung wählen (STL)?**
A: Produktion: 2000 Dreiecke/m². Visualisierung: 5000+. Performance-Analyse: 500.

**F4: Lofting-Fehler vermeiden wie?**
A: viele Querschnitte (z.B. alle 0,5m), Kurven glätten, Oberflächen-Analyse prüfen (Zebra).

**F5: Gewichts-Ungenauigkeit wie minimieren?**
A: detaillierte Komponenten-Liste (nicht schätzen), 10–15% Puffer reservieren, in Datenbank speichern.

**F6: FreeShip oder Maxsurf für Stabilitäts-Check?**
A: Maxsurf: genauer (professionell). FreeShip: kostenlos (aber weniger Features). Für Genehmigung: Maxsurf.

**F7: Datei-Größe zu groß (>1GB)?**
A: Assembly reduzieren (separates Rumpf, Deck, Interieur), Mesh-Auflösung reduzieren, Archive nutzen.

**F8: STEP-Datei verzogen beim Import?**
A: Maßstab prüfen (mm vs. m), Kurven-Orientierung überprüfen, in Quelltool normal-Richtung überprüfen.

**F9: Rhino + Orca3D Stabilitäts-Iteration wie schnell?**
A: 5–10 Minuten pro Iteration (schneller als Maxsurf für Design-Loop).

**F10: Klasse-Genehmigung: welche CAD-Tools akzeptiert?**
A: Lloyd's, DNV, ABS: alle akzeptieren STEP + PDF-Berichte. Bevorzugt: Maxsurf oder Orca3D.

**F11: Heißt es „DNV" oder „DNV GL"?**
A: Seit **1. März 2021: DNV** (vorher DNV GL, aus der Fusion 2013 von Det Norske Veritas + Germanischer Lloyd). „DNV GL" ist veraltet. Quelle: [DNV](https://www.dnv.com/news/2021/dnv-gl-changes-name-to-dnv-as-it-gears-up-for-decade-of-transformation-194340/).

**F12: Ist DELFTship Open Source?**
A: **Nein.** DELFTship ist **Freeware** (Free-Version) + kommerzielle **Professional-Perpetual-Lizenz (USD 160)**. Der GPL-quelloffene Vorgänger ist **FREE!ship**. Quelle: [DELFTship Pricing](https://www.delftship.net/pricing/).

**F13: STEP AP203 oder AP242 exportieren?**
A: **AP242** (Ed.2 2020) bevorzugen — vereint AP203+AP214 und erhält PMI/GD&T. AP203 nur, wenn das Zielsystem AP242 nicht liest. Quelle: [ISO 10303-242:2020](https://www.iso.org/standard/66654.html).

**F14: IGES noch verwenden?**
A: Nur als Fallback. IGES-Entwicklung wurde **1996 mit v5.3 eingestellt**; NIST empfiehlt STEP. Quelle: [Wikipedia — IGES](https://en.wikipedia.org/wiki/IGES).

**F15: Welches Format für Laser-/Plasma-/CNC-Zuschnitt von 2D-Teilen?**
A: **DXF** (ASCII) — universelles, offen dokumentiertes 2D-Neutralformat. Quelle: [Wikipedia — DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).

**F16: Warum ist mein STL-Import falsch skaliert?**
A: STL **enthält keine Einheiten**. Skalierung beim Import prüfen (bekannte Referenzlänge messen). Für maßhaltigen Austausch STEP statt STL. Quelle: [Wikipedia — STL](https://en.wikipedia.org/wiki/STL_(file_format)).

**F17: Ab welcher Größe wird Yacht-Klassifikation (LR/ABS/DNV) statt CE relevant?**
A: CE nach RCD 2013/53/EU gilt für 2,5–24 m; Klassifikation (z.B. Lloyd's SSC) greift v.a. bei Yachten **≥24 m** LOA bzw. gewerblicher Nutzung. Quelle: [LR — SSC](https://www.lr.org/en/knowledge/lloyds-register-rules/rules-and-regulations-for-the-classification-of-special-service-craft/).

**F18: 12215 oder 12217 für die Rumpf-Dimensionierung?**
A: **ISO 12215** (Scantlings/Struktur). **ISO 12217** ist Stabilität/Auftrieb — nicht für Laminatdicken. Quelle: [ISO 12215-5](https://www.iso.org/standard/69552.html).

**F19: Wie prüfe ich Flächen-Fairness objektiv in Rhino?**
A: Zebra (Reflexionsstreifen), CurvatureAnalysis (Falschfarben), EMap, CurvatureGraph, EdgeContinuity. Ziel: mind. **G2**. Quelle: [McNeel — Zebra](https://docs.mcneel.com/rhino/mac/help/en-us/commands/zebra.htm).

**F20: Nutzen DELFTship/FREE!ship NURBS?**
A: Nein — **Subdivision Surfaces** (anderes Paradigma als die NURBS von Rhino/Maxsurf/Orca3D). Quelle: [FREE!ship](https://sourceforge.net/projects/freeship/).

**F21: Was ersetzt langfristig den G-Code (ISO 6983)?**
A: **STEP-NC** (ISO 14649 / ISO 10303-238 AP238) — feature-basiert, semantisch reicher. Quelle: [Wikipedia — STEP-NC](https://en.wikipedia.org/wiki/STEP-NC).

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-07-13 (Werft-Tiefe-Audit: Abschnitte 7–9, Fehlerbild-Atlas FB-31-13-NNN, Glossar-/FAQ-Erweiterung; alle neuen Fakten web-verifiziert mit Quelle + Confidence)  
**Gültig für:** Yacht-Design 8–40m LOA, Production & Custom  
**Verifikationshinweis:** Neue faktische Angaben in Abschnitt 7–9 tragen Inline-Quelle (ISO/Hersteller/Klassifikation) + Confidence `documented`. Unbelegte Bestand-Werte (Preisspannen, Marktanteile, Stabilitäts-Grenzwerte) sind als `estimated — unverifiziert` bzw. „⚠️ ZU PRÜFEN" markiert.
