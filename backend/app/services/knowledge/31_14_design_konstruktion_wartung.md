# 31_14 — Design-Konstruktion Wartung

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Design_Konstruktion_Wartung  
**Version:** 3.0  
**Stand:** 2026-07-13  
**Relevanz:** Management von Konstruktions-Dokumentation, Revisionen, Klassifizierung, CE-Modulnachweis, Zeichnungsnormen, Konfigurationsmanagement

---

## Übersicht

Die Design-Konstruktions-Wartung umfasst **Dokumentations-Management**, **Revisions-Kontrolle**, **Klasse-Genehmigungen** und **Updates bei Modifikationen**. AYDI analysiert Drawing-Archive, Änderungs-Verwaltung und Langzeit-Dokument-Integrität.

**Fehleranalyse-Schwerpunkte:**
1. Veraltete Zeichnungen im Umlauf (nicht aktuelle Revision)
2. fehlende oder unvollständige Konstruktions-Dokumentation
3. Revisions-Nummern nicht konsistent (Verwirrung bei Produktion)
4. CAD-Datei-Versionen nicht synchronisiert (Rumpf-Design vs. Interieur)
5. Genehmigung(S) abgelaufen oder nicht dokumentiert
6. Änderungen-Anforderungen nicht formal nachverfolgt
7. Konfigurationskontrolle mangelhaft (Optionen nicht klar)
8. Metadaten verloren oder inkorrekt (Gewicht, CG, Performance)
9. Archivierung ungeordnet (Fund-barkeit schwach)
10. Nachbau/Umbau-Dokumentation unzureichend
11. Schad-Erkennung unvollständig (Risse, Verschleiß-Punkte)
12. Wartungs-Intervall-Dokumentation fehlt

---

## 1. Dokumentations-Struktur und Standards

### 1.1 Zeichnungs-Klassifizierung (nach DIN/ISO)

**Standard-Klassifizierungen:**

```
Typ A: Detailzeichnungen (spezifische Komponenten)
  Beispiel: Bolzen-Zeichnung, Laminat-Schicht-Detai
  Merkmale: Maßstab 1:1 oder 1:5, Toleranzen genau
  Format: A4 oder A3 (maximal)
  Archiv: permanent (wichtig für Reparatur/Ersatz)

Typ B: Montage-Zeichnungen (Zusammenstellung mehrerer Teile)
  Beispiel: Kielbefestigung (Kiel + Bolzen + Laminat)
  Merkmale: Schnitt-Ansichten, Zusammenhang deutlich
  Format: A2 oder A1 (größer)
  Archiv: permanent

Typ C: Allgemeine Arrangements (Übersicht-Pläne)
  Beispiel: Interieur-Layout, Deck-Plan, Längsschnitt
  Merkmale: große Übersicht, Details untergeordnet
  Format: A1 oder A0 (Plotter-Größe)
  Archiv: permanent

Typ D: Fertigungs-Zeichnungen (spezifisch für Herstellung)
  Beispiel: NC-Code-Daten, Schablonen-Maße, Sequenzen
  Merkmale: Toleranzen + Fertigungs-Angaben
  Format: variabel (digital CAM-Format bevorzugt)
  Archiv: 5–10 Jahre (später verfügbar, aber nicht täglich nötig)

Typ E: Änderungs-Blätter (Engineering Change Notices)
  Beispiel: "Mod Kit für Ruder-Upgrade"
  Merkmale: Referenz zu Original-Zeichnung, Delta-Information
  Format: A4 (zusammen mit Original)
  Archiv: permanent (Langzeit-Rückverfolgung)

Typ F: Wartungs-Richtlinien
  Beispiel: "Inspektions-Protokoll Kielbolzen"
  Merkmale: Checklisten, Intervalle, Toleranzen
  Format: A4 (digital + Papier)
  Archiv: permanent + Updates
```

### 1.2 Datei-Namenskonvention (Standard für Yachtdesign)

**Empfohlenes Namenssystem:**

```
Format: [ProjectCode]-[Zone]-[Komponente]-[Version]

Beispiele:
  AYDI-001-HULL-01.step
    → AYDI: Projekt-Präfix
    → 001: Rumpf-Code
    → HULL: Zone (Rumpf)
    → 01: Revisions-Nummer
    
  AYDI-101-KEEL-BOLT-02.dwg
    → AYDI: Projekt
    → 101: Kiel-Subsystem
    → KEEL-BOLT: Komponente
    → 02: Revisions-Nummer
    
  AYDI-201-INTERIOR-GALLEY-03.pdf
    → AYDI: Projekt
    → 201: Interieur-Zone
    → INTERIOR-GALLEY: spezifisches Element
    → 03: aktuelle Revision

Zonen-Kodierung:
  000–099: Rumpf + Struktur (001–010 Rumpf, 011–020 Kiel, etc.)
  100–199: Deck-Systeme
  200–299: Interieur + Lebensräume
  300–399: Antrieb + Mechanik
  400–499: Elektrik + Systeme
  500–599: Segel + Rigging (Segelboote)
  600–699: Sicherheit + Notfall
```

### 1.3 Revisions-Nummerierung System

**Ziffern-Signifikanz:**

```
Format: R.M.P (Release.Modification.Patch)

Beispiel: 02.05.01
  02 = 2. Release (große Umgestaltung)
  05 = 5. Modifikation in dieser Release
  01 = 1. Patch in dieser Modifikation
  
Bedeutung der Nummernstände:
  00.00.01 → 00.00.02: Kleine Korrektur (Tippfehler, Maß-Anpassung)
  00.00.XX → 00.01.00: Komponenten-Umbau (neue Toleranz, Material)
  00.XX.XX → 01.00.00: Großes Redesign (Geometrie-Änderung)
  01.XX.XX → 02.00.00: Major-Release (Klasse-Genehmigung neu)
```

**Revisions-Protokoll (Dokumentation):**

```
In Tabellenform (auf Zeichnung):

Rev | Date    | Author   | Change Description
----|---------|----------|----------------------------------
01  | 2025-05 | J.Smith  | Initial design, Class A1 approved
02  | 2025-06 | M.Brown  | Updated keel bolt layout
02a | 2025-06 | M.Brown  | Corrected dimension 340→350mm
03  | 2025-07 | K.Lee    | Integrated hydro optimization
03b | 2025-08 | K.Lee    | Minor adjustments post-analysis

Notation:
  Major-Revision: neue Zahl (02 → 03)
  Minor-Revision: Buchstab-Suffix (03 → 03a → 03b)
```

---

## 2. Konfigurationskontrolle und Tracking

### 2.1 Bill of Materials (BOM) Verwaltung

**BOM-Struktur für Yacht:**

```
Hierarchie:
  Level 1: Boot (z.B. "AYDI-001 Segelkutter 12m")
    ├─ Level 2: Subsysteme (Rumpf, Deck, Interieur, etc.)
    │   ├─ Level 3: Komponenten (z.B. Kiel, Bolzen, Laminat)
    │   │   └─ Level 4: Material/Teile (Stainless Steel M30, etc.)
    │   │       └─ Menge, Lieferant, Preis
```

**BOM-Datei (Excel/CSV Beispiel):**

```
ProjectID | Subsystem | Component | Part# | Desc | Material | Qty | Unit | Supplier | Cost/Unit | Total
----------|-----------|-----------|-------|------|----------|-----|------|----------|-----------|-------
AYDI-001  | Hull      | Keel      | K001  | Kiel | E-Glass+ | 1   | set  | Laminate | EUR 8000  | 8000
          |           |           | K002  | Bulb | Blei     | 1   | pcs  | Foundry  | EUR 3500  | 3500
          |           |           | K003  | Bolzen| St 316L | 8   | pcs  | FastenerCo| EUR 150  | 1200
AYDI-001  | Deck      | Railing   | D001  | Railing | St316L | 15  | m    | MetalSys | EUR 200/m | 3000
```

**Tracking-System (digital):**

```
Minimum erforderlich:
  - Projekt-ID + Boot-Name
  - Subsystem-Zuordnung (Rumpf, Deck, etc.)
  - Komponenten-Referenz (zu Zeichnung)
  - Menge + Einheit
  - Material-Spezifikation
  - Kosten-Tracking
  - Lieferant + Lead-Time
  
Ideale Ergänzung:
  - Seriennummern (für kritische Teile)
  - Verfallsdatum (Verschleiß-Teile)
  - Locations-Tracking (wo eingebaut?)
```

### 2.2 Change Control Procedures (Engineering Change Order)

**ECO-Prozess (Engineering Change Order):**

```
Schritt 1: Anforderung einreichen
  Wer: Designer, Werft, Kunde, Klassifizierer
  Form: ECO-Formular (standardisiert)
  Inhalt:
    - Beschreibung Problem/Verbesserung
    - betroffene Zeichnungen/Komponenten
    - Grund für Änderung
    - geschätzter Aufwand/Kosten
    
Schritt 2: Bewertung + Genehmigung
  Review-Panel: Designer + Konstruktion + Produktion
  Kriterien:
    - Sicherheits-Impact? (Priorät hoch)
    - Kosten-Auswirkung? (Budget-Check)
    - Zeit-Impact? (Verzögerung?)
    - Klassfizierungs-Impact? (Genehmigung neu nötig?)
    
Schritt 3: Genehmigung + Implementierung
  Wenn genehmigt:
    - neue Revisions-Nummer zuordnen
    - Zeichnungen aktualisieren
    - BOM anpassen
    - Mitteilung an Produktion
    - Datum dokumentieren
    
Schritt 4: Archivierung
  ECO-Dokument archivieren (permanent)
  Revisions-Protokoll auf Zeichnung aktualisieren
  Impact-Liste speichern (welche Teile betroffen?)
```

**ECO-Formular Muster:**

```
ECO-Nummer: 2026-042
Projekt: AYDI-001
Betroffene Zeichnung(en): AYDI-001-KEEL-BOLT-01.dwg

Titel: Kielbolzen-Durchmesser erhöht (M30→M36)

Beschreibung:
  Hydro-dynamische Neuberechnung zeigt 20% höhere Grounding-Lasten.
  M30 Bolzen nur für 70% der Lasten ausreichend.
  Upgrade zu M36 erforderlich.

Sicherheits-Impact: JA (kritisch)
  Grund: Strukturale Integrität bei Grounding

Kosten-Impact:
  Material: +EUR 200 pro Bolzen × 8 = +EUR 1600
  Arbeit: +EUR 500 (neue Zeichnungen, Planung)
  Insgesamt: +EUR 2100

Zeit-Impact:
  Verzögerung: -2 Tage (Produktion-Umstellung)

Klassifizierungs-Impact:
  Ja, Mitteilung an Lloyd's erforderlich (Struktur-Änderung)
  Neuer Genehmigungsbericht: Ja
  
Genehmigt von: Chief Designer (2026-05-20)
              Produktion Manager (2026-05-20)
              Klassifizierer (2026-05-21)

Implementierungs-Datum: 2026-05-23
```

---

## 3. Klasse-Genehmigung und Compliance-Dokumentation

### 3.1 Genehmiggungs-Phasen (Lloyd's Register Beispiel)

**Schritt 1: Approval in Principle (AIP)**

```
Timing: vor oder während Konstruktion-Start
Dokumentation erforderlich:
  - allgemeine Arrangement-Pläne (Interieur, Deck)
  - Stabilitäts-Berechnungen (ISO 12217)
  - Rumpf-Form (Hydro-dynamische Daten)
  - Gewichts-Schätzung + CG-Position
  - allgemeine Struktur-Pläne
  
Ergebnis: AIP-Zertifikat (gültig 3 Jahre)
  → Genehmigung "im Prinzip", Details folgen später
```

**Schritt 2: Construction Survey (während Bau)**

```
Frequenz: regelmäßige Inspektionen (z.B. 4–6 Termine)
Inspektions-Punkte:
  - Laminat-Qualität (Oberflächenprüfung, UT-Messungen)
  - Struktur-Montage (Bolzenfestigkeit, Ausrichtung)
  - Leck-Tests (Wasserdichtigkeit-Prüfungen)
  - Sicherheits-Features (Notfall-Ausrüstung, Escape-Routen)
  - Elektrik/Mechanik (Isolierung, Erdung)

Dokumentation:
  - Inspektions-Berichte nach jedem Termin
  - Abweichungen + Korrektionsmaßnahmen
  - Zeichnungs-Abnahme (aktuell verwendete Revision?)
  - Gewichts-Kontrolle (Ist-Gewicht vs. Schätzung)
```

**Schritt 3: Sea Trial und Abnahme**

```
Timing: nach Fertigstellung, vor Übergabe
Tests:
  - Maschinenraum-Bedienung (Motor-Start, Hitze, Geräusche)
  - Ruder-Test (Manövrierbarkeit, Kraft-Anforderung)
  - Sicherheits-Ausrüstungs-Test (Rettungsboote, Signale)
  - Stabilitäts-Bestätigung (Boot sitzt richtig im Wasser?)

Dokumentation:
  - Sea Trial Report
  - final Class Certificate (gültig 5 Jahre)
  - Ausnahmeregelungen (falls nicht 100% Compliance)
```

### 3.2 Dokumente für Class-Submission

**Erforderliches Dokumentations-Paket:**

```
Strukturelle Pläne:
  ☐ Hauptspant (Master Section)
  ☐ Längsschnitt (Longitudinal Section)
  ☐ Querschnitte (Multiple Cross Sections)
  ☐ Spanten-Plan (Frame Plan)
  ☐ Schotten-Plan (Watertight Bulkheads)
  ☐ Laminat-Plan (Layer-by-Layer, Dicke, Material)

Hyd Daten:
  ☐ Hydrostatik-Tabellen (Gewicht, CG, Auftrieb vs. Draft)
  ☐ Stabilitäts-Daten (GM, Righting Arm, Capsizing-Index)
  ☐ Trim-Tabellen (Längstrimm vs. Ballast-Positionen)

Gewicht + Balance:
  ☐ Gewichtsliste (alle Komponenten + Gewicht)
  ☐ CG-Berechnung (Schwerpunkt-Position)
  ☐ Loading-Szenarien (Light Ship, Full Load, etc.)

Interieur + Sicherheit:
  ☐ Allgemeine Arrangement (Deck-Plan + Längsschnitt)
  ☐ Escape-Route Analyse (Notfalls-Zugänglichkeit)
  ☐ Rettungs-Ausrüstungs-Liste
  ☐ Feuer-Schutz-Maßnahmen (Feuerlösch-Systeme, Isolation)

Betriebs-Dokumente:
  ☐ Betriebs-Anleitung (für Besatzung)
  ☐ Wartungs-Plan (Inspektions-Intervalle)
  ☐ Sicherheits-Unterlagen (Notsignale, Rettungs-Prozeduren)

Digitale Dateien:
  ☐ CAD-Modell (STEP-Format)
  ☐ PDF-Pläne (alle Zeichnungen)
  ☐ Excel-BOM (Materialien + Kosten)
  ☐ Stabilitäts-Berichte (Maxsurf- oder Orca3D-Output)
```

---

## 4. Dokumentations-Archivierung und Retrieval

### 4.1 Archiv-Struktur (für langfristige Verwaltung)

**physisches Archiv (Papier):**

```
Schrank-System:
  Ordner 1: Allgemeine Pläne (Rumpf, Deck, Längsschnitt)
  Ordner 2: Detailzeichnungen (Kiel, Ruder, Mast)
  Ordner 3: Interieur-Pläne (Kabinen, Galley, Kopf)
  Ordner 4: Elektrik-Schemen + Rohrleitungs-Pläne
  Ordner 5: Genehmigungsdokumente (Class Certificates, AIP)
  Ordner 6: Engineering Change Orders (ECO-Historie)
  Ordner 7: Inspektions-Berichte (Sea Trial, Construction Survey)
  
Indizierung:
  Jede Zeichnung: Projekt-Nummer + Zone + Revision auf Rückseite notiert
  Suchregister: Excel-Tabelle mit Zeichnungs-Nummern + Standort
  
Lagerbedingung:
  18–24°C, <50% Feuchte (verhindert Papier-Verfall)
  kein direkt-Sonnenlicht (Vergilbung)
  Regalmaterial: Kunststoff oder verzinkt Stahl (nicht Holz)
```

**Digitales Archiv (bevorzugt):**

```
Ordner-Struktur:
  /AYDI-001-Master/
    /01-Hull/
      /01-Main-Forms/
        AYDI-001-HULL-001.step
        AYDI-001-HULL-001-R03.pdf
      /02-Keel/
        AYDI-001-KEEL-001.dwg
        AYDI-001-KEEL-BOLT-002.pdf
    /02-Deck/
      /01-General/
        AYDI-001-DECK-001.pdf
      /02-Railing/
        AYDI-001-RAILING-001.pdf
    /03-Interior/
      ...
    /04-Class-Documents/
      AIP-Certificate-2025-05.pdf
      Construction-Survey-Reports.pdf
      Class-Certificate-Final.pdf
    /05-ECO-History/
      ECO-2026-042-KEEL-BOLT.pdf
      ECO-2026-043-LAMINAT.pdf
    /06-BOM/
      AYDI-001-BOM-R03.xlsx
      
Backup-Strategie:
  Primär: NAS (Network Attached Storage) mit RAID-1 (Spiegelung)
  Sekundär: externe HDD (archiviert, jährlich kopiert)
  Tertiary: Cloud-Backup (EUR 10–50/Monat für Boot-Daten)
  
Zugriffsrechte:
  Designer: Lese-/Schreib-Zugriff auf alle Dateien
  Produktion: Lese-Zugriff auf aktuelle Revisionen
  Klassifizierer: Lese-Zugriff auf genehmigte Dokumente
  Kunde: Lese-Zugriff auf relevante Betriebs-Dokumente (optional)
```

### 4.2 Versionierungs-Software (Git/Subversion Alternative)

**Version Control System (VCS) Einsatz:**

```
Begründung:
  - Verlauf aller Änderungen nachverfolgbar
  - Zusammenarbeit mehrerer Designer problemlos
  - Rollback zu früheren Versionen möglich
  - Conflicts automatisch erkannt + gemeldet

Typisches System:
  Git (kostenlos, weit verbreitet)
  oder Subversion (SVN)
  oder PLM-System (z.B. Windchill für große Werften)

Setup für Yacht-Design:
  Repository: zentrales Archiv (NAS oder Cloud)
  
  Commit-Prozedur:
    Designer macht Änderung (z.B. Kiel-Geometrie)
    ↓
    Test + Qualitäts-Prüfung lokal
    ↓
    Commit mit Nachricht ("Updated keel geometry per ECO-2026-042")
    ↓
    System speichert Änderung + Zeitstempel
    ↓
    andere Designer sehen Änderung (Pull)
  
  Merge-Konflikt-Szenario:
    Designer A: ändert Kiel-Dicke in Zeichnung
    Designer B: ändert Kiel-Bolzen in gleicher Zeichnung
    ↓
    VCS erkennt Konflikt (beide verschiedene Zeilen)
    ↓
    Automatische Zusammenführung oft möglich
    ↓ (wenn nicht)
    manuelle Auflösung erforderlich (Teams-Diskussion)
    ↓
    validierte Merge committed
```

---

## 5. Wartungs-Dokumentation und Serviceability

### 5.1 Wartungs-Handbücher (für Eigentümer/Werft)

**Struktur des Wartungs-Handbuchs:**

```
Kapitel 1: Übersicht
  - Boots-Daten (Länge, Breite, Material, Gewicht)
  - Systeme-Übersicht (Antrieb, Elektrik, Hydraulik)
  - Wartungs-Philosophie (präventiv vs. reaktiv)

Kapitel 2: Inspektions-Intervalle
  Jährlich:
    - Kielbolzen-Kontrolle (Drehmoment, Korrosion)
    - Reling-Bolzen-Kontrolle
    - Laminat-Oberflächenprüfung
    - Abdichtungs-Systeme prüfen
  
  Alle 5 Jahre:
    - Ultraschall-Laminat-Prüfung
    - Ruderlager-Kontrolle (Verschleiß-Spiel)
    - Seeleck-Ventile überprüfen
  
  Alle 10 Jahre:
    - Vollständige strukturale Inspektion
    - ggf. Bolzen-Austausch
    - Laminat-Reparatur (wenn nötig)

Kapitel 3: Häufige Probleme + Lösungen
  Problem: Wasser eindringen im Cockpit
  Diagnose: Hahnblock-Ventil-Prüfung
  Lösung: Ventil-Verschluss überprüfen, ggf. Reinigung
  
  Problem: Ruder-Flattern
  Diagnose: Lager-Spiel-Messung
  Lösung: Gleitlager austausch oder Bolzen-Festigung

Kapitel 4: Ersatzteil-Information
  Standardteile (mit Lieferanten):
    - Kielbolzen M30 × 316L Stainless: Lieferant XYZ
    - Reling-Bolzen M8 × 316L: Lieferant ABC
    - Seeleck-Ventil DN40 Ball-Ventil: Lieferant DEF
  
  kritische Teile (Original-Hersteller erforderlich):
    - Laminat-Rumpf (nur von Werft oder genehmigter Partner)
    - Ruder-Asselbly (baugleich, Genauigkeit kritisch)
    - Mast (bei Segelboot, Verformungs-Risiko)

Kapitel 5: Notfall-Verfahren
  Problem: Leck im Rumpf
  Sofortmaßnahme: Notfall-Patch (Holzpflock + Epoxy-Kleber)
  Langfrist: strukturales Reparatur-Verfahren
  
  Problem: Rudersystem-Ausfall
  Sofortmaßnahme: handbedienungs-Ruder (wenn vorhanden)
  Alternative: Seeanker + Funk-Notruf
```

### 5.2 Inspektions-Checklisten (für regelmäßige Überprüfung)

**Jährliche Inspektions-Checkliste (12m Segelboot):**

```
Struktur:
  ☐ Rumpf-Oberfläche: Risse, Kratzer, Kratzer <2 mm ok
  ☐ Kielbolzen: Drehmoment-Prüfung (250 N·m sollte halten)
  ☐ Kielschuh: Oberflächen-Verschleiß prüfen, Tiefe messen
  ☐ Laminat um Bolzen: Rissanzeichen?
  ☐ Wassereintritts-Stellen: trocken?

Deck:
  ☐ Reling-Stanchions: lose Bolzen? Korrosion?
  ☐ Sicherheits-Leinen: Verschleiß, Fasern-Ausfranzung?
  ☐ Deck-Drainage: Verstopfung? Hahnblock-Ventil funktioniert?
  ☐ Oberfläche: rutschsicher (nicht zu glatt)?
  ☐ Foredeck-Blöcke: Rollen drehen frei?

Ruder + Drehpunkt:
  ☐ Ruder-Flansch-Bolzen: fest? Korrosion?
  ☐ Ruderlager (Pintle/Gudgeon): Spiel <0,5 mm?
  ☐ Ruder-Oberfläche: Kratzer, Dellen, Delaminierung?
  ☐ Abdichtungs-Gummi: Risse? Verschleiß?

Interieur (beispielhaft):
  ☐ Galley-Gimbals: Bewegung frei? Sicherheits-Drähte intakt?
  ☐ Kopf-Ventil: Seewasser-Hahnblock funktioniert?
  ☐ Lüftungs-Bullaugen: dicht? kein Wasser-Eindringung?

Korrosion-Kontrolle:
  ☐ Stainless Steel-Teile: Fleckenbildung (Tea Staining)?
  ☐ verzinkte Stahlteile: Rost-Ansätze?
  ☐ Kupfer-Beschädigungen: Galvanische Korrosion-Zeichen?

Dokumentation:
  ☐ Inspektions-Datum: _______
  ☐ Inspekteur: _______
  ☐ Unterschrift: _______
  ☐ Nächste planmäßige Inspektion: _______
  ☐ Mängel-Bericht: (separate Seite if erforderlich)
```

---

## 6. Modifikationen und Upgrade-Management

### 6.1 Retrofit und Umbau-Prozess

**Stufe 1: Konzept und Machbarkeit**

```
Anforderung: z.B. "neues Antriebssystem installieren"

Schritt 1a: Konzept-Analyse
  - neuer Motor-Typ + Größe definieren
  - Platz vorhanden? (Maschinenraum-Abmessungen prüfen)
  - Gewichts-Auswirkung? (CG-Verschiebung, Trimm?)
  - Kosten-Schätzung

Schritt 1b: Dokumentation erstellen
  - Änderungs-Anfrage-Formular (wie ECO)
  - technische Beschreibung
  - betroffene Zeichnungen auflisten
  - Klassifizierungs-Auswirkung prüfen (neuer Genehmigungsbericht?)
```

**Stufe 2: Design und Engineering**

```
Schritt 2a: CAD-Modellierung
  - neue Motor-Position + Befestigungen CAD
  - Rohrleitungs- + Elektrik-Verläufe prüfen
  - Zugangs-Prüfung (Wartung, Reparatur möglich?)
  - Interferenz-Prüfung (kollisiert neue Installation mit bestehend?)

Schritt 2b: Strukturale Bewertung
  - neue Motorlast auf Fundamente berechnen
  - Bolzen-Dimensionierung überprüfen
  - ggf. Verstärkung erforderlich? (wo?, wie viel Laminat?)
  - Trimm-Auswirkung berechnen (Gewicht + Position)
  - neu Stabilitäts-Berechnung (wenn CG stark verändert)

Schritt 2c: Modifikations-Zeichnungen
  - Detail-Zeichnung Motor-Befestigung
  - Rohrleitungs-Umleitungen + Querschnitte
  - Elektrik-Schema (separate Versorgung? Schutz?)
  - Inspektions-Zugangs-Anforderungen dokumentieren
```

**Stufe 3: Genehmigung**

```
Klassifizierer-Einschaltung (wenn erforderlich):
  - Sicherheits-Auswirkung? (Gewicht, Stabilität)
  - Umwelt-Compliance? (Antrieb-Emissionen)
  - wenn umfangreich: neuer Genehmigungsbericht erforderlich
```

**Stufe 4: Durchführung und Dokumentation**

```
Während Umbau:
  - Inspektions-Kontrollpunkte dokumentieren
  - Zeichnungs-Abweichungen notieren (falls nötig)
  - Gewichts-Prüfung durchführen (Ist-Gewicht vs. Berechnung)

Nach Umbau:
  - Inspektions-Abnahme
  - funktionale Tests durchführen
  - Zeichnungen final aktualisieren (as-built)
  - Modifikations-Zeichnungen archivieren
  - BOM aktualisieren
  - neues Wartungs-Handbuch (wenn betroffen)
```

### 6.2 Upgrade-Tracking (für Kaufinteressenten/Verkäufer)

**Modifikations-Geschichte dokumentieren:**

```
beispiel: 10-Jahr-alte Yacht, mehrere Upgrades durchgeführt

Upgrade 1 (2020): Elektrik-System modernisiert
  - neues 24V-System installiert
  - alte 12V-Batterien durch Lithium ersetzt
  - Dokumente: ECO-Report, Inspektions-Report

Upgrade 2 (2022): Motor-Überhaul
  - Diesel-Motor Generalüberholung (10000h)
  - neue Lager, Injektoren
  - Dokumente: Werkstatt-Bericht, Serviceunterlagen

Upgrade 3 (2025): Ruder-Lager-Austausch
  - neues Ball-Lager-System installiert
  - Dokumentation: Inspektions-Abnahme, Photos

Gegenwarts-Status:
  - Boot in gutem Wartungs-Zustand
  - alle Upgrades ordnungsgemäß dokumentiert
  - Gewicht/CG nach Modernisierungen neu berechnet (Dokument vorhanden)

Verkaufs-Vorteil:
  - "Gut gepflegtes Boot" → glaubwürdig gemacht
  - Käufer sieht Inspektions-Historie
  - längere wirtschaftliche Lebensdauer
```

---

## 7. Dokumentations-Standards und Best Practices

### 7.1 ISO 12217 Compliance-Dokumentation

**erforderliche Dokumentations-Elemente:**

```
für alle Yachten >8m nach CE:

Stabilität-Dokumentation:
  ☐ Stabilitäts-Bericht (Maxsurf oder äquivalent)
  ☐ ISO 12217-Standard-Konformitäts-Erklärung
  ☐ Gewichtsliste + CG-Position
  ☐ Stabilitäts-Diagramme (GM vs. Heel, Righting Arm)
  ☐ kritische Szenarien (z.B. vollgesaugtes Boot)

Sicherheits-Dokumentation:
  ☐ Notfall-Flucht-Plan (Escape-Routen-Analyse)
  ☐ Rettungs-Ausrüstungs-List (Boot, Signale, etc.)
  ☐ Notfall-Verfahren (Seegang, Leck, Feuer)

Struktur-Dokumentation:
  ☐ Laminat-Schicht-Pläne
  ☐ Materialien-Spezifikation
  ☐ Struktur-Zeichnungen (Spanten, Schotten)

Betrieb-Dokumentation:
  ☐ Betriebs-Handbuch (Besatzung)
  ☐ Wartungs-Plan (Inspektions-Intervalle)
  ☐ Gewicht-Limits (Personen, Ladung)
```

### 7.2 Qualitäts-Assurance im Design-Prozess

**Design-Review Checkpoints:**

```
Checkpoint 1: Konzept-Phase Review
  Beteiligungen: Designer, Konstrukteur, Klassifizierer
  Checkliste:
    ☐ Anforderungs-Spezifikation klar?
    ☐ Stabilitäts-Anforderungen definiert?
    ☐ Klasse-Genehmigung erforderlich?
    ☐ Zeitplan + Budget realistisch?
  Ergebnis: Genehmigung zum Weitermachen

Checkpoint 2: detailliertes Design Review
  Beteiligungen: Design, Produktion, QA
  Checkliste:
    ☐ CAD-Modell-Qualität (Oberflächen glatt?)
    ☐ Fertigungsbarkeit prüfen (CNC möglich? Toleranzen ok?)
    ☐ Laminat-Plan aktuell + korrekt?
    ☐ Stabilität + Gewicht finale Berechnung ok?
  Ergebnis: Design release für Produktion

Checkpoint 3: Vor-Seriencheck
  Beteiligungen: Designer, Produktion, QA, ggf. Klassifizierer
  Checkliste:
    ☐ Prototyp-Konstruktion ok (Abweichungen dokumentiert?)
    ☐ Laminat-Qualität entspricht Standard?
    ☐ alle Komponenten vorhanden + korrekt?
    ☐ Inspektions-Punkte absolviert?
  Ergebnis: Freigabe zu Serie
```

---

## 8. Regulatorischer und normativer Rahmen (verifiziert)

> **Hinweis zur Belegtiefe:** Alle Normbezüge in diesem Abschnitt sind gegen die
> ausstellende Stelle (ISO, EU/EUR-Lex, Red Ensign Group) verifiziert. Nummer +
> Titel + Scope sind dokumentiert; abgeleitete Prozessbeschreibungen sind als
> `documented` bzw. — wo nur qualitativ belegbar — als `estimated` markiert.

### 8.1 Normen der technischen Dokumentation und Zeichnungserstellung

| Norm (verifiziert) | Titel / Scope | Relevanz für dieses Dokument | Confidence |
|--------------------|---------------|------------------------------|------------|
| **ISO 128-1:2020** | *Technical product documentation (TPD) — General principles of representation — Part 1: Introduction and fundamental requirements*. Gilt für Maschinenbau, Bau, Architektur **und Schiffbau**, 2D + 3D, manuell + rechnergestützt. | Grundregeln aller Konstruktionszeichnungen | documented |
| **ISO 128-2:2020** | *…— Part 2: Basic conventions for lines* (Linienarten/-breiten) | Linienkonvention (sichtbar/verdeckt/Mittellinie) | documented |
| **ISO 128-3:2022** | *…— Part 3: Views, sections and cuts* (Ansichten, Schnitte) | Spanten-/Längsschnitt-Darstellung | documented |
| **ISO 128-15:2013** | *…— Part 15: Presentation of shipbuilding drawings* | **schiffbauspezifische** Darstellungsregeln | documented |
| **ISO 5457:1999** *(EN ISO 5457)* | *Technical product documentation — Sizes and layout of drawing sheets* | Blattformate + Layout (Zeichnungsrahmen, Feldeinteilung) | documented |
| **ISO 7200:2004** | *Technical product documentation — Data fields in title blocks and document headers* | **Schriftfeld-Datenfelder** (Rev-Index, Ersteller, Prüfer, Freigabe, Maßstab, Blattnr.) | documented |
| **ISO 5455:1979** *(EN ISO 5455)* | *Technical drawings — Scales* | zulässige Maßstäbe + Bezeichnung „SCALE 1:x" | documented |
| **ISO 216:2007** | *Writing paper and certain classes of printed matter — Trimmed sizes — A and B series* | Papierformate A0–A4 | documented |
| **ISO 10209** | *Technical product documentation — Vocabulary* | Terminologie TPD (Begriffsbasis) | documented |

> Quellen: ISO 128-1/-3 (iso.org std 65296, 83356), ISO 128-15 (Schiffbau-Teil,
> ISO-128-Übersicht), ISO 7200:2004 (iso.org std 35446 / iteh sample), ISO 5457:1999
> (iteh sample 29017), ISO 5455:1979 (iso.org std 11500), ISO 216:2007 (iso.org std 36631).
> — Confidence: documented.

**Verifizierte Blattformate (ISO 216, A-Reihe, Seitenverhältnis √2):**

| Format | Maße (mm) | typische Nutzung Yacht-Zeichnung |
|--------|-----------|----------------------------------|
| A0 | 841 × 1189 | Generalplan, Längsschnitt, Rumpf-Linienriss (Plotter) |
| A1 | 594 × 841 | Deckplan, große Baugruppen |
| A2 | 420 × 594 | Baugruppen-/Montagezeichnung |
| A3 | 297 × 420 | Detail-/Komponentenzeichnung |
| A4 | 210 × 297 | Einzelteil, ECO-Blatt, Wartungsblatt |

> A0 = 1 m² Fläche (vor Rundung); jede kleinere Größe halbiert die Fläche.
> Quelle: ISO 216:2007. — Confidence: documented.

**Verifizierte Maßstabsreihe (ISO 5455):**
- Vergrößerung: 50:1, 20:1, 10:1, 5:1, 2:1
- Natürlicher Maßstab: 1:1
- Verkleinerung: 1:2, 1:5, 1:10, 1:20, 1:50, 1:100, 1:200, 1:500, 1:1 000, 1:2 000, 1:5 000, 1:10 000
- Bezeichnung: Wort **„SCALE"** + Verhältnis, eingetragen im Schriftfeld.

> Quelle: ISO 5455:1979, iso.org/obp. — Confidence: documented.
> **Korrektur zum Bestand (Abschnitt 1.1):** die dort genannte pauschale Bindung
> „Detailzeichnung = 1:1 oder 1:5" ist nur eine von mehreren normgerechten Optionen;
> ISO 5455 lässt die volle obige Reihe zu.

**Verifizierte Schriftfeld-Datenfelder (ISO 7200:2004, dokumentmanagement-relevant):**
u. a. *legal owner, title / supplementary title, document type, document status,
identification number, revision index, date of issue, responsible department,
technical reference, created by, approved by, scale, sheet/page number, number of
sheets, projection symbol, paper size, part weight, language code, classification/keywords*.
Das Schriftfeld sitzt bei A0–A3 unten rechts im Zeichnungsraum.

> Quelle: ISO 7200:2004 (Data fields in title blocks and document headers); RoyMech
> ISO-7200-Zusammenfassung. — Confidence: documented.

### 8.2 Konfigurationsmanagement und Dokumentenlenkung

| Norm (verifiziert) | Titel / Scope | Relevanz | Confidence |
|--------------------|---------------|----------|------------|
| **ISO 10007:2017** | *Quality management — Guidelines for configuration management* | Rahmen für BOM-/Revisions-/Änderungs-/Konfigurations-Steuerung | documented |
| **ISO 9001:2015 Abschn. 7.5** | *Quality management systems — Requirements*, Klausel **7.5 Documented information** (7.5.2 Erstellen/Aktualisieren, 7.5.3 Lenkung) | Freigabe, Verteilung, Aufbewahrung, Änderungslenkung von Dokumenten | documented |
| **ISO 10303 (STEP)** | *Industrial automation systems and integration — Product data representation and exchange* | herstellerneutrales CAD-Austauschformat (.step/.stp) | documented |

**ISO 10007:2017 — die fünf Konfigurationsmanagement-Prozesse (verifiziert):**
1. **Configuration-Management-Planung** (CM-Plan)
2. **Configuration Identification** (Konfigurationseinheiten + Baseline festlegen)
3. **Change Control** (kontrollierte Änderung → deckt den ECO-Prozess in Abschnitt 2.2 ab)
4. **Configuration Status Accounting** (Status-/Revisionsbuchführung)
5. **Configuration Audit** (Soll-/Ist-Abgleich der Konfiguration)

> Quelle: ISO 10007:2017 (iso.org std 70400; TC176-Projektseite). — Confidence: documented.
> Anwendbar „von Konzept bis Außerdienststellung" (concept to disposal).

**ISO 9001:2015, 7.5.3 — Lenkungsanforderungen an dokumentierte Information (verifiziert):**
Verfügbarkeit/Eignung am Einsatzort; Schutz (Vertraulichkeit/Integrität);
**Verteilung, Zugriff, Auffindung, Verwendung**; Speicherung/Erhaltung;
**Änderungslenkung (Versionskontrolle)**; Aufbewahrung und Entsorgung
(retention & disposition). Erstellung/Aktualisierung (7.5.2): angemessene
Identifikation/Beschreibung, Format/Medium, **Prüfung und Freigabe** vor Gebrauch.

> Quelle: ISO 9001:2015 Klausel 7.5. — Confidence: documented.
> Diese Norm ist der belegte Unterbau für Abschnitt 1 (Revisionsführung) und
> Abschnitt 4 (Archiv/Zugriffsrechte) dieses Dokuments.

### 8.3 Kennzeichnung und Rückverfolgbarkeit (Traceability)

| Norm (verifiziert) | Titel / Scope | Relevanz | Confidence |
|--------------------|---------------|----------|------------|
| **ISO 10087:2022** | *Small craft — Craft identification — Coding system* (CIN/WIN, ehem. HIN); gilt bis **LH ≤ 24 m** | eindeutige Boots-ID als Anker jeder BOM/Doku | documented |
| **ISO 8666:2020** | *Small craft — Principal data* | Definition der Haupt-/Prinzipdaten (Basis der Metadaten in Abschnitt 3.2) | documented |

**CIN-Struktur (verifiziert, 14 Zeichen):** Ländercode (2 Buchstaben) · Hersteller­code
(3 Zeichen) · Seriennummer (5 Zeichen) · Herstellmonat (1 Buchstabe A=Jan … L=Dez) ·
letzte Ziffer des Herstelljahrs · Modelljahr (2 Ziffern).

> Quelle: ISO 10087:2022 (iso.org std 82383); ISO 8666:2020 (iso.org/obp).
> — Confidence: documented. Der CIN ist der empfohlene Primärschlüssel, an den
> Projektcode, BOM und Zeichnungsarchiv (Abschnitte 1.2, 2.1, 4.1) gebunden werden.

---

## 9. CE-Konformitätsbewertung — Modulnachweis (RCD 2013/53/EU)

> **Geltungsbereich:** Sportboote **2,5 m ≤ LH < 24 m**, in der EU in Verkehr
> gebracht. Rechtsgrundlage: **Richtlinie 2013/53/EU** (Recreational Craft Directive,
> RCD), ersetzt 94/25/EG. Quelle: EUR-Lex CELEX 32013L0053. — Confidence: documented.

### 9.1 Konformitätsbewertungsmodule (verifiziert)

Die Module folgen dem NLF-Baukasten (Beschluss 768/2008/EG); die RCD wählt daraus
zulässige Kombinationen je Entwurfskategorie und Länge.

| Modul | Vollname (verifiziert) | Notified Body (NB) nötig? |
|-------|------------------------|---------------------------|
| **A** | Internal production control (interne Fertigungskontrolle) | nein |
| **A1** | Internal production control plus supervised product testing | ja (überwachte Prüfung) |
| **B** | EU-type examination (EU-Baumusterprüfung) | ja |
| **C** | Conformity to type based on internal production control | nein (Basis B) |
| **C1** | Conformity to type based on internal production control plus supervised product testing | ja |
| **D** | Conformity to type based on quality assurance of the production process (setzt EN ISO 9001 voraus) | ja |
| **E** | Conformity to type based on product quality assurance (EN ISO 9001) | ja |
| **F** | Conformity to type based on product verification | ja |
| **G** | Conformity based on unit verification (Einzelstückprüfung) | ja |
| **H** | Conformity based on full quality assurance | ja |

> Quellen: RCD Application Guide (2. Aufl., Jan. 2022); Hellenic Register „CE
> Assessment Modules"; EUR-Lex 2013/53/EU. — Confidence: documented.

**Zulässige Wege für Entwurfskategorie A und B, LH 2,5 – < 12 m (verifiziert):**
Modul **A1**, ODER **B + (C, D, E oder F)**, ODER **G**, ODER **H**.
Für den strukturell/stabilitätskritischen Nachweis (Kat. A/B, größere Boote)
verlangt die RCD NB-Einbindung — reine Selbsterklärung (Modul A) reicht dann nicht.

> Quelle: RCD Application Guide 2022; Suchbeleg EUR-Lex-Zusammenfassung Anhang II.
> — Confidence: documented (Längen-Detailschwellen der Kategorien C/D: qualitativ
> belegt, exakte Modultabelle je Kombination siehe Directive Anhang II — bei
> konkretem Projekt dort gegenprüfen).

### 9.2 Post-Construction Assessment (PCA) — verifizierte Auslöser

Ein PCA (durch einen Notified Body) ist erforderlich, wenn:
1. ein **Privatimporteur** ein Produkt in Betrieb nimmt, für das der Hersteller
   **keine** Konformitätsbewertung durchgeführt hat;
2. ein Antriebsmotor oder Wasserfahrzeug nach **wesentlicher Umbau/Modifikation**
   („major modification or conversion") in Verkehr gebracht / in Betrieb genommen wird;
3. ein **Eigenbau** vor Ablauf der **5-Jahres-Frist** ab Inbetriebnahme in Verkehr
   gebracht wird.

> Quelle: RCD 2013/53/EU, PCA-Bestimmungen; IMCI DoC-for-PCA. — Confidence: documented.
> **Konsequenz für Abschnitt 6 (Retrofit/Umbau):** ein „wesentlicher Umbau" löst
> nicht nur Klassifizierer-Konsultation aus, sondern kann ein förmliches **PCA**
> erforderlich machen.

### 9.3 Technische Dokumentation (Technical File, Anhang IX) — verifizierter Inhalt

Die technische Dokumentation muss Auslegung, Herstellung und Betrieb des Produkts
verständlich machen und die Konformitätsbewertung ermöglichen. Sie enthält, soweit
relevant:
- **allgemeine Beschreibung** des Produkts;
- **Entwurfs- und Fertigungszeichnungen** sowie Schemata von Bauteilen, Baugruppen,
  Schaltkreisen usw.;
- **Beschreibungen/Erläuterungen** zum Verständnis dieser Zeichnungen und der Funktion;
- **Liste der angewandten Normen** (Art. 5), ganz oder teilweise; bei Nicht-Anwendung:
  Beschreibung der gewählten Lösungen zur Erfüllung der grundlegenden Anforderungen;
- **Ergebnisse der Konstruktionsberechnungen**, durchgeführte Prüfungen, **Prüfberichte**.

> Quelle: RCD 2013/53/EU, Art. 25 + Anhang IX. — Confidence: documented.

**Aufbewahrungsfrist (verifiziert):** Hersteller bewahren technische Dokumentation
und eine Kopie der EU-Konformitätserklärung **10 Jahre** ab Inverkehrbringen auf
(RCD Art. 7(3)/Art. 25).

> Quelle: RCD 2013/53/EU Art. 7(3). — Confidence: documented.
> **Präzisierung zum Bestand (FAQ F1 / Abschnitt 4):** rechtlich zwingend sind
> **10 Jahre**; „permanent/20+ Jahre" ist eine sinnvolle **Betriebs-Empfehlung**
> für Wartung/Reparatur, keine Normfrist.

### 9.4 Herstellerschild (Builder's Plate) — verifizierter Pflichtinhalt

Dauerhaft und getrennt von der CIN anzubringen; Pflichtangaben u. a.:
Herstellername / eingetragener Handelsname oder Marke, **CE-Kennzeichnung**,
**Entwurfskategorie** (A/B/C/D), **vom Hersteller empfohlene Höchstlast**
(ohne Inhalt fest eingebauter Tanks) und **empfohlene Personenzahl**.

> Quelle: RCD 2013/53/EU Anhang I Teil A (Herstellerschild); EU-Konformitäts-
> Leitfäden (Oceanskies/EBI). — Confidence: documented.

### 9.5 Fahrzeuge > 24 m — Klasse & Flaggenstaat statt reiner CE-Bewertung

Oberhalb 24 m LH greift die RCD nicht mehr; kommerziell genutzte Großyachten
folgen dem **REG Yacht Code** (Red Ensign Group), Part A, für Yachten
**> 24 m**, gewerblich, **≤ 12 Passagiere**; aktuelle Fassung **Juli-2024-Ausgabe**
(löste LY3 ab, erstveröffentlicht Nov. 2017). Der Code wirkt als Äquivalenz u. a.
zum **Load Lines Convention 1966** und SOLAS.

> Quelle: Red Ensign Group, REG Yacht Code Part A (Juli 2024); MCA MSN 1895 (M).
> — Confidence: documented.

**Klassifikations-Ablauf (Plan Approval → Bau-Survey → Zertifikat):** Pläne werden
beim Plan-Approval-Office der Klasse eingereicht und mit Endorsement zurückgegeben;
Bau folgt genehmigten Plänen unter Surveyor-Aufsicht; das **Class Certificate** ist
**5 Jahre** gültig (Erneuerung per Special Survey; dazwischen Annual/Intermediate
Surveys).

> Quelle: Klassifikations-Surveys (Bureau Veritas NR500 Yacht Rules; Boat
> International „Classification explained"). — Confidence: documented.
> Dies bestätigt die 5-Jahres-Angabe in Abschnitt 3.1 (Class Certificate).
> Der Begriff **„Approval in Principle" (AIP)** und dessen genaue Gültigkeit
> variieren je Klassegesellschaft — die im Bestand (Abschnitt 3.1) genannte
> „3 Jahre"-Frist ist gesellschaftsspezifisch und **estimated — vor Einreichung
> beim jeweiligen Register verifizieren**.

---

## 10. Fehlerbild-Atlas (FB-31-14-1xx)

> **ID-Schema:** Neue Fehlerbilder nutzen `FB-31-14-1NN`, um **Kollisionen** mit dem
> bestehenden `31_14_0NN`-Schema (Pydantic-Modell, Anhang B) und den 12 nummerierten
> Fehleranalyse-Schwerpunkten (Übersicht) zu vermeiden. Schweregrad: kritisch / hoch /
> mittel / niedrig. Jede Norm-Referenz ist gegen Abschnitt 8/9 verifiziert.

### FB-31-14-101 — Zeichnung ohne normgerechtes Schriftfeld
- **Symptom:** Rev-Index, Freigabe-/Prüferfeld, Maßstab oder Blattnummer fehlen.
- **Auswirkung:** Revision nicht eindeutig identifizierbar → veraltete Version gelangt
  in Fertigung (siehe FB-31-14-102).
- **Schweregrad:** hoch · **Norm:** ISO 7200:2004, ISO 5457:1999.
- **Diagnose:** Schriftfeld gegen ISO-7200-Pflichtfelder abgleichen.
- **Abhilfe:** CAD-Template mit ISO-7200-Schriftfeld erzwingen; Altzeichnungen nachziehen.
- **Prävention:** Freigabe nur mit vollständigem Schriftfeld (Gate im Freigabe-Workflow).

### FB-31-14-102 — Veraltete Revision im Umlauf
- **Symptom:** Fertigung arbeitet nach nicht-aktueller Zeichnung/BOM.
- **Auswirkung:** Maß-/Materialabweichung, Konformitätszweifel.
- **Schweregrad:** hoch (sicherheitsrelevant, wenn Struktur betroffen).
- **Norm:** ISO 9001:2015 §7.5.3 (Verteilung/Auffindung/Änderungslenkung), ISO 10007:2017.
- **Diagnose:** Status Accounting (ISO 10007) — Ist-Revision am Arbeitsplatz vs. Baseline.
- **Abhilfe:** kontrollierte Verteilung, „aktuell gültig"-Kennzeichnung, Rückzug alter Stände.
- **Prävention:** Einzige Wahrheitsquelle (PDM/VCS), Revisionszwang statt optional.
- **Verwandt:** Bestand `31_14_001`.

### FB-31-14-103 — Änderung ohne ECO / ohne Configuration Change Control
- **Symptom:** Geometrie/Material geändert, aber kein Änderungsantrag dokumentiert.
- **Auswirkung:** Rückverfolgbarkeit gebrochen; CE-Technikdokumentation inkonsistent.
- **Schweregrad:** hoch · **Norm:** ISO 10007:2017 (Change Control), RCD Anhang IX.
- **Diagnose:** Configuration Audit — Zeichnungsstand vs. ECO-Historie.
- **Abhilfe:** ECO nachträglich anlegen, Impact-Liste rekonstruieren.
- **Prävention:** Change Control als Pflichtprozess (Abschnitt 2.2 + ISO 10007 Schritt 3).

### FB-31-14-104 — Wesentlicher Umbau ohne PCA/Klassifizierer-Bewertung
- **Symptom:** Motor-/Struktur-/Stabilitätsrelevanter Retrofit ohne Konformitäts-Neubewertung.
- **Auswirkung:** Fahrzeug ggf. **nicht mehr konform**; Haftungs-/Zulassungsrisiko.
- **Schweregrad:** kritisch · **Norm:** RCD 2013/53/EU (PCA bei major modification/conversion).
- **Diagnose:** Umbau gegen PCA-Auslöser (Abschnitt 9.2) prüfen.
- **Abhilfe:** Notified Body einschalten; PCA bzw. bei > 24 m Klasse/Flaggenstaat.
- **Prävention:** Umbau-Freigabe-Gate mit Pflichtfrage „PCA-relevant?".
- **Verwandt:** Bestand `31_14_008` (Retrofit-Genehmigung).

### FB-31-14-105 — Technische Dokumentation unvollständig (Anhang IX)
- **Symptom:** Es fehlen z. B. Konstruktionsberechnungen, Normenliste oder Prüfberichte.
- **Auswirkung:** Konformitätsbewertung nicht nachweisbar; Marktzugang gefährdet.
- **Schweregrad:** hoch · **Norm:** RCD Art. 25 + Anhang IX.
- **Diagnose:** Technical-File-Checkliste (Abschnitt 9.3) abhaken.
- **Abhilfe:** fehlende Elemente ergänzen, vor Inverkehrbringen komplettieren.
- **Prävention:** File-Vollständigkeit als Freigabekriterium; 10-Jahres-Aufbewahrung sichern.

### FB-31-14-106 — CAD-Austausch ohne neutrales Format / Versionsdrift
- **Symptom:** Nur natives CAD archiviert; nach SW-Update nicht mehr öffenbar.
- **Auswirkung:** Langzeit-Lesbarkeit verloren (Reparatur nach Jahren unmöglich).
- **Schweregrad:** mittel · **Norm:** ISO 10303 (STEP).
- **Diagnose:** Archiv auf herstellerneutrales Format (.step) + PDF prüfen.
- **Abhilfe:** STEP-Export + PDF-Plot zusätzlich zum nativen Modell ablegen.
- **Prävention:** Ablage-Policy „nativ + STEP + PDF" pro Freigabe.

### FB-31-14-107 — Falscher Normbezug (Struktur vs. Stabilität)
- **Symptom:** Laminat-/Scantling-Nachweis auf ISO 12217 (Stabilität) statt ISO 12215 gestützt.
- **Auswirkung:** Nachweis formal falsch belegt; Prüfstelle beanstandet.
- **Schweregrad:** hoch · **Norm:** ISO 12215 (Struktur/Scantlings) vs. ISO 12217 (Stabilität).
- **Diagnose:** Berechnungs-Deckblatt-Normbezug prüfen.
- **Abhilfe:** korrekten Normbezug setzen; Berechnung ggf. neu referenzieren.
- **Prävention:** Normen-Cross-Check im Design-Review (Checkpoint 2, Abschnitt 7.2).

### FB-31-14-108 — Kennzeichnung/CIN nicht mit Doku verknüpft
- **Symptom:** Herstellerschild/CIN vorhanden, aber nicht als Schlüssel im Archiv/BOM.
- **Auswirkung:** Doku einer konkreten Rumpfnummer nicht eindeutig zuordenbar.
- **Schweregrad:** mittel · **Norm:** ISO 10087:2022, ISO 8666:2020.
- **Diagnose:** Stichprobe: CIN → findet man BOM, Zeichnungssatz, Zertifikate?
- **Abhilfe:** CIN als Primärschlüssel in Archiv/PDM einführen.
- **Prävention:** CIN-Feld im Schriftfeld/Metadaten verpflichtend.

### FB-31-14-109 — Herstellerschild-Pflichtangaben unvollständig
- **Symptom:** Entwurfskategorie, Höchstlast oder Personenzahl fehlt auf dem Schild.
- **Auswirkung:** Formaler CE-Mangel; Betrieb außerhalb ausgelegter Grenzen möglich.
- **Schweregrad:** hoch · **Norm:** RCD Anhang I Teil A (Herstellerschild).
- **Diagnose:** Schild gegen Pflichtinhalt (Abschnitt 9.4) abgleichen.
- **Abhilfe:** Schild korrigieren/ersetzen; Werte aus genehmigter Doku übernehmen.
- **Prävention:** Schild-Freigabe an Konformitätsdoku koppeln.

### FB-31-14-110 — Aufbewahrungsfrist unterschritten
- **Symptom:** Technische Doku/DoC vor Ablauf von 10 Jahren entsorgt.
- **Auswirkung:** Nachweisbarkeit bei Rückfrage/Marktüberwachung verloren.
- **Schweregrad:** hoch · **Norm:** RCD Art. 7(3) (10 Jahre).
- **Diagnose:** Retention-Schedule (ISO 9001 §7.5.3) prüfen.
- **Abhilfe:** Retention-Policy nachziehen; Backups wiederherstellen falls möglich.
- **Prävention:** Aufbewahrungsplan mit Mindestfrist 10 J. (Empfehlung: Lebensdauer).

---

## 11. Troubleshooting / Entscheidungsbäume

### 11.1 „Ist diese Änderung PCA-/klassepflichtig?"

```
Änderung geplant
  │
  ├─ Betrifft Struktur / Stabilität / Antrieb / Brandabschnitt / Wasserdichtigkeit?
  │      │
  │      ├─ NEIN → interner ECO (Abschnitt 2.2) genügt; Doku + Revision aktualisieren
  │      │
  │      └─ JA → „wesentlicher Umbau" (RCD)?
  │               │
  │               ├─ Fahrzeug ≤ 24 m, EU-Markt → Notified Body: PCA prüfen (Abschnitt 9.2)
  │               │
  │               └─ Fahrzeug > 24 m, gewerblich → Klasse + Flaggenstaat / REG Yacht Code
  │
  └─ In jedem Fall: ECO anlegen, Impact-Liste, Revision hochzählen, Technical File nachführen
```
> Logik abgeleitet aus RCD PCA-Auslösern (Abschnitt 9.2) + Klasse-Scope (Abschnitt 9.5).
> — Confidence: documented (Prozesslogik), Einzelfall stets mit NB/Klasse abstimmen.

### 11.2 „Welches CE-Modul wähle ich?" (Kat. A/B, 2,5 – < 12 m)

```
Serie oder Einzelstück?
  ├─ Einzelstück → Modul G (unit verification, NB)
  ├─ Serie, eigenes QM-System zertifiziert (ISO 9001)?
  │      ├─ JA → B + D  oder  B + E   (bzw. H = full QA)
  │      └─ NEIN → B + C/F   oder   A1 (internal control + supervised testing)
  └─ Immer: Technical File (Anhang IX) + DoC + Herstellerschild
```
> Quelle: RCD Application Guide 2022 (zulässige Modulwege). — Confidence: documented.
> Exakte Zulässigkeit je Länge/Kategorie in RCD Anhang II gegenprüfen.

### 11.3 „Veraltete Zeichnung entdeckt in Produktion" (Sofortmaßnahmen)

```
1. STOP: betroffene Fertigung anhalten (falls Struktur/Sicherheit)
2. Ist-Revision am Arbeitsplatz vs. Baseline (Status Accounting) feststellen
3. Delta ermitteln: welche Maße/Materialien weichen ab?
4. bereits gefertigte Teile bewerten (Nacharbeit / Ausschuss / Sonderfreigabe)
5. korrekte Revision kontrolliert verteilen, alten Stand einziehen
6. Ursache (fehlende Change Control?) → FB-31-14-102/103 abstellen
```
> Prozesslogik nach ISO 10007 (Status Accounting/Audit) + ISO 9001 §7.5.3.
> — Confidence: documented.

---

## ANHANG A — Glossar

**Archivierung:** permanente Speicherung von Dokumenten.

**BOM:** Bill of Materials, Stückliste.

**CAD:** Computer-Aided Design.

**ECO:** Engineering Change Order, Änderungs-Antrag.

**Repository:** zentrales Datei-Archiv (digital).

**Revision:** Version eines Dokuments (z.B. Rev 03).

**VCS:** Version Control System (Git, SVN, etc.).

**CIN / WIN:** Craft/Watercraft Identification Number, 14-stelliger Boots-Kenncode nach ISO 10087:2022 (früher HIN).

**DoC:** Declaration of Conformity, EU-Konformitätserklärung (RCD).

**PCA:** Post-Construction Assessment, nachträgliche Konformitätsbewertung durch Notified Body (RCD).

**Notified Body (NB):** benannte Stelle, die RCD-Konformitätsbewertungen durchführt.

**Technical File:** technische Dokumentation nach RCD Art. 25 + Anhang IX; 10 Jahre aufzubewahren.

**Configuration Management (CM):** Steuerung von Identifikation, Änderung, Status und Audit einer Konfiguration nach ISO 10007:2017.

**Baseline:** freigegebener, referenzierter Konfigurationsstand als Ausgangspunkt für kontrollierte Änderungen.

**STEP:** herstellerneutrales CAD-Austauschformat nach ISO 10303 (.step/.stp).

**Schriftfeld (Title Block):** Datenfeldblock der Zeichnung nach ISO 7200:2004 (unten rechts bei A0–A3).

**REG Yacht Code:** Red-Ensign-Group-Regelwerk für gewerbliche Yachten > 24 m (Part A, Juli-2024-Ausgabe).

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class DesignKonstruktionWartungFehlerbild(BaseModel):
    """
    Fehlerbild für Design-Konstruktion Wartung nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_14_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Design_Konstruktion_Wartung"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Verwaltung/Betrieb")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-Relevanz")
    
    # Ursprung
    dokument_type: str = Field(default="", description="Zeichnungen/BOM/Genehmigungen/etc")
    betroffene_zone: str = Field(default="", description="Rumpf/Interieur/Systeme/etc")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Kosten Korrektur")
    dauer_tage: Optional[int] = Field(None, description="Dauer Korrektur in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Review-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO, DIN, Lloyd's")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = DesignKonstruktionWartungFehlerbild(
    fehlerbild_id="31_14_001",
    titel="Veraltete Zeichnungen im Umlauf",
    beschreibung="alte Revisionen verwendet in Produktion (nicht aktuelle Version).",
    symptome=[
        "Zeichnungs-Revision nicht aktuell",
        "Maße oder Details unterscheiden sich von neuer Version",
        "Produktions-Fehler wegen veralteter Spezifikation"
    ],
    auswirkungen=[
        "Produkt-Variabilität (nicht konsistent)",
        "Qualitäts-Probleme (falsche Toleranzen/Materialien)",
        "Genehmigungszweifel (Klasse berücksichtigt neuen Plan?)"
    ],
    schweregrad="hoch",
    sicherheits_impact=True,
    dokument_type="Zeichnungen",
    betroffene_zone="mehrere",
    diagnose_methoden=[
        "Revisions-Check: ist aktuelle Revision vorhanden?",
        "Archiv-Vergleich: Original vs. im Umlauf",
        "Dokumentations-Audit: alle Referenzen aktuell?"
    ],
    reparatur_optionen=[
        "alle Zeichnungen aus Archiv aktualisieren",
        "Distributions-System einrichten (digital preferred)",
        "Härtungs-Kontrollprozess (ECO + Revision-Zwang)"
    ],
    schaetzung_kosten_eur=2000,
    dauer_tage=2,
    praevention=[
        "digitales Dokumentations-Management System",
        "Revisions-Nummern erzwingen (nicht optional)",
        "Regelmäßiges Audit (jährlich)"
    ],
    inspektions_intervall_jahre=1,
    normen_referenzen=["ISO 10303 (STEP)", "DIN 6771 (Zeichnungsformat)"],
    verwandte_fehlerbilder=["31_14_002", "31_14_005"]
)
```

---

## ANHANG C — FAQ (20+)

**F1: Wie lange Zeichnungen archivieren?**
A: permanent (nicht wegwerfen). Mindestens 20+ Jahre für Wartung/Reparatur.

**F2: Revision-Nummern wie formatieren?**
A: z.B. 01.02.03 (Release.Modification.Patch). oder Rev A, Rev B (einfacher).

**F3: ECO erforderlich für jede Änderung?**
A: ja, formal (für Nachverfolgung). kleine Tippfehler: optional, aber dokumentiert.

**F4: digitale vs. Papier-Archivierung?**
A: digital bevorzugt (einfacher Zugang, Sicherung). Papier-Backup für Backup.

**F5: Klassfizierungs-Genehmigung wie oft erneuern?**
A: Final Certificate: 5 Jahre gültig. Annual Survey während Betrieb erforderlich.

**F6: BOM aktualisieren wie oft?**
A: nach jeder ECO, mindestens jährlich.

**F7: Wartungs-Dokumentation für Käufer relevant?**
A: ja (Boot-Werterhaltung), aber Primärfokus auf Original-Konstruktions-Doku.

**F8: Retrofit-Genehmigung erforderlich?**
A: wenn Struktur/Stabilität betroffen: ja (Klassifizierer-Konsultation).

**F9: Archiv-Zugriffsrechte wie kontrollieren?**
A: Role-Based Access (Designer, Produktion, Klassifizierer).

**F10: Datenverlust-Schutz wie umsetzen?**
A: NAS + RAID, externe HDD Backup, optional Cloud.

**F11: Wie lange muss die technische Dokumentation *rechtlich* aufbewahrt werden?**
A: **10 Jahre** ab Inverkehrbringen für technische Doku + Kopie der DoC (RCD 2013/53/EU Art. 7(3)). „Permanent/20+ Jahre" ist Betriebs-Empfehlung, keine Normfrist. — documented.

**F12: Welche Normen regeln das Zeichnungs-Schriftfeld und Blattformat?**
A: Schriftfeld/Datenfelder → **ISO 7200:2004**; Blattgrößen/Layout → **ISO 5457:1999**; Papierformate → **ISO 216**; Maßstäbe → **ISO 5455:1979**; Darstellungsgrundlagen → **ISO 128** (Schiffbau: **ISO 128-15:2013**). — documented.

**F13: Welches CE-Modul brauche ich für eine Serien-Segelyacht Kat. A, 11 m?**
A: Zulässig: Modul **A1** ODER **B + (C/D/E/F)** ODER **G** ODER **H**; für Kat. A/B ist NB-Einbindung erforderlich. Exakte Wahl in RCD Anhang II gegenprüfen. — documented.

**F14: Wann wird aus einem Umbau ein PCA-Fall?**
A: Bei **wesentlichem Umbau/Modifikation** (Struktur/Stabilität/Antrieb) muss ein Notified Body ein **Post-Construction Assessment** durchführen (RCD). Bei > 24 m gewerblich: Klasse/Flaggenstaat (REG Yacht Code). — documented.

**F15: Was ist der offizielle Standard für Konfigurations-/Änderungsmanagement?**
A: **ISO 10007:2017** (fünf Prozesse: Planung, Identifikation, Change Control, Status Accounting, Audit) i. V. m. **ISO 9001:2015 §7.5** (Dokumentenlenkung). — documented.

**F16: Wie ist der CIN/HIN aufgebaut?**
A: 14 Zeichen nach **ISO 10087:2022**: Ländercode (2) · Herstellercode (3) · Serien-Nr. (5) · Monat (A–L) · Jahr-Endziffer · Modelljahr (2). — documented.

**F17: Wie lange ist ein Class Certificate gültig?**
A: In der Regel **5 Jahre** (Erneuerung per Special Survey; dazwischen Annual/Intermediate Surveys). — documented.

**F18: Welches CAD-Format fürs Langzeitarchiv?**
A: Zusätzlich zum nativen Modell **STEP (ISO 10303)** + PDF-Plot, um Lesbarkeit über SW-Generationen zu sichern. — documented.

**F19: Muss jede Zeichnung ein Schriftfeld nach ISO 7200 haben?**
A: Ja — ohne vollständiges Schriftfeld ist die Revision nicht eindeutig; Freigabe verweigern (siehe FB-31-14-101). — documented.

**F20: Was gehört zwingend auf das Herstellerschild?**
A: Herstellername/Marke, CE-Kennzeichnung, Entwurfskategorie, empfohlene Höchstlast (ohne Festtank-Inhalt), empfohlene Personenzahl (RCD Anhang I Teil A). — documented.

---

## ANHANG D — Quellenverzeichnis (verifiziert)

Alle Faktenzusätze der Abschnitte 8–11 sind gegen folgende autoritative Quellen verifiziert:

- **RCD 2013/53/EU** — EUR-Lex CELEX 32013L0053 (Art. 7, 25; Anhang I, II, IX).
- **RCD Application Guide**, 2. Auflage, Januar 2022 (Notified-Body-Register / IMCI).
- **ISO 128-1:2020, 128-3:2022, 128-15:2013** (iso.org) — Technical product documentation.
- **ISO 5457:1999**, **ISO 7200:2004**, **ISO 5455:1979**, **ISO 216:2007** (iso.org / iteh samples).
- **ISO 10007:2017** (iso.org std 70400) — Configuration management.
- **ISO 9001:2015 §7.5** — Documented information.
- **ISO 10303 (STEP)**, **ISO 10087:2022**, **ISO 8666:2020** (iso.org).
- **REG Yacht Code Part A**, Juli-2024-Ausgabe (Red Ensign Group); **MCA MSN 1895 (M)**.
- **Bureau Veritas NR500** — Rules for the Classification and Certification of Yachts.

> Confidence-Konvention: `documented` = gegen o. g. Quelle belegt; `estimated —
> unverifiziert` = Prinzip belegt, Einzelwert projekt-/gesellschaftsspezifisch und
> vor Verwendung gegenzuprüfen (so gekennzeichnet an Ort und Stelle).

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-07-13 (Abschnitte 8–11 + Anhang D web-verifiziert ergänzt)  
**Gültig für:** Yacht-Design 8–40m LOA, alle Baustile
