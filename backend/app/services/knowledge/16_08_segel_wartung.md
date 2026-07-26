---
titel: "Segel — Wartung, Pflege und Reparatur"
kategorie: "Segel"
unterkategorie: "Wartung und Reparatur"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 16_08 — Segel — Wartung, Pflege und Reparatur

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Wartungsplan](#2-wartungsplan)
3. [Reinigung](#3-reinigung)
4. [UV-Schutz](#4-uv-schutz)
5. [Naht-Inspektion und Reparatur](#5-naht-inspektion-und-reparatur)
6. [Reparaturtechniken](#6-reparaturtechniken)
7. [Lagerung](#7-lagerung)
8. [Professionelle Beurteilung](#8-professionelle-beurteilung)
9. [Fehlerbild-Atlas](#9-fehlerbild-atlas)
10. [Troubleshooting](#10-troubleshooting)
11. [Bord-Reparaturkit](#11-bord-reparaturkit)
12. [Lebensdauer-Management](#12-lebensdauer-management)
13. [FAQ](#13-faq)
14. [Glossar](#14-glossar)
15. [Schnell-Referenz](#15-schnell-referenz)
16. [ANHANG A–H: Fallstudien](#16-anhang-ah-fallstudien)
17. [ANHANG I–R: Pydantic v2 Schemata](#17-anhang-ir-pydantic-v2-schemata)

---

## 1. Einführung

### 1.1 Warum Segelwartung unverzichtbar ist

Segel sind der Antrieb einer Segelyacht. Ihre Leistung, Haltbarkeit und Sicherheit hängen
unmittelbar von regelmäßiger Wartung und sachgerechter Pflege ab. Ein gut gepflegtes
Großsegel kann 8–12 Jahre halten, während ein vernachlässigtes Segel bereits nach
3–4 Jahren irreversibel geschädigt sein kann.

Die Kosten für ein neues Großsegel liegen je nach Bootsklasse zwischen:

| Bootsklasse | Dacron-Großsegel | Laminat-Großsegel | Membran-Großsegel |
|-------------|------------------|--------------------|-------------------|
| 8–10 m | 1.800–3.500 EUR | 3.000–5.500 EUR | 5.500–9.000 EUR |
| 10–13 m | 3.500–6.000 EUR | 5.500–10.000 EUR | 9.000–18.000 EUR |
| 13–16 m | 6.000–12.000 EUR | 10.000–20.000 EUR | 18.000–35.000 EUR |
| 16–20 m | 12.000–22.000 EUR | 20.000–40.000 EUR | 35.000–65.000 EUR |
| 20+ m | 22.000–60.000 EUR | 40.000–90.000 EUR | 65.000–150.000+ EUR |

Eine jährliche Wartung kostet dagegen nur 150–600 EUR (Eigenleistung) bzw.
400–1.500 EUR (professionell), je nach Segelgröße und Zustand.

### 1.2 Kosten der Vernachlässigung

Die folgenden Szenarien verdeutlichen die finanziellen Folgen mangelnder Wartung:

**Szenario 1: UV-Degradation am Großsegel**
- Ein Rollgroßsegel ohne UV-Schutzstreifen verliert innerhalb von 2 Sommersaisons
  seine Festigkeit im Achterliek um bis zu 40 %.
- Typische Reparaturkosten nachträglich: 800–1.500 EUR (UV-Streifen nachrüsten)
- Prävention: UV-Streifen bei Neukauf: 200–400 EUR Aufpreis

**Szenario 2: Salzablagerungen in Laminatsegeln**
- Salzkristalle dringen in die Laminatschichten ein und beschleunigen die Delamination.
- Nach 3 Jahren ohne Spülung: Delamination im Achterliek auf 15–25 % der Fläche.
- Reparaturkosten: 1.200–3.000 EUR (partielle Neukaschierung)
- Prävention: Süßwasserspülung nach jedem Törn: 0 EUR

**Szenario 3: Schimmelbefall durch unsachgemäße Lagerung**
- Ein feucht eingelagertes Dacron-Segel entwickelt innerhalb von 4–8 Wochen
  Schimmelflecken, die das Gewebe dauerhaft verfärben und schwächen.
- Professionelle Reinigung: 300–800 EUR
- Prävention: Trocknung vor Lagerung: 30 Minuten Aufwand

**Szenario 4: Nahtauflösung durch UV-Strahlung**
- Polyester-Nähgarn (V-69/V-92) verliert bei ungeschützter UV-Exposition
  50 % seiner Festigkeit nach 1.500–2.000 Sonnenstunden.
- Nachennähen eines Großsegel-Achterlieks (12 m Yacht): 600–1.200 EUR
- Prävention: Segelabdeckung + UV-Streifen: vermeidet das Problem vollständig

### 1.3 Segelmaterialien im Überblick

Für die Wartungsplanung ist das Verständnis der verwendeten Materialien entscheidend:

**Gewebte Materialien:**
- **Dacron (Polyester-Gewebe)**: Standard für Fahrtensegel. Robust, UV-beständiger
  als Nylon, moderate Dehnung. Hersteller: Dimension Polyant, Bainbridge, Contender.
- **Nylon (Polyamid)**: Primär für Spinnaker und Gennaker. Hohe Elastizität,
  geringe UV-Beständigkeit, leicht. Typisch 40–75 g/m².
- **Pentex (PEN-Faser)**: Höherwertige Alternative zu Dacron, ca. 40 % weniger
  Dehnung. Einsatz in Performance-Fahrtensegeln.

**Laminierte Materialien:**
- **Mylar/PET-Laminat**: Polyester-Film mit Faserverstärkung. Geringere Dehnung
  als Dacron, aber anfälliger für Delamination und Knickbruch.
- **Hydranet/Spectra-Laminat**: UHMWPE-Fasern in Laminataufbau. Sehr geringe
  Dehnung, hohe Festigkeit, gute UV-Beständigkeit (UHMWPE, vgl. Tabelle 4.1).
- **Kevlar/Twaron-Laminat**: Aramid-Fasern. Höchste Festigkeit-zu-Gewicht-Ratio,
  aber stark UV-empfindlich und feuchtigkeitsanfällig.
- **Technora-Laminat**: Verbesserte Aramid-Variante mit besserer UV- und
  Feuchtigkeitsbeständigkeit als Kevlar.

**Membran-Materialien:**
- **3Di (North Sails)**: Thermoplastisches Filament-Laminat. Dreidimensional
  geformt, extrem formstabil, hohe Lebensdauer bei Pflege.
- **D4 (Doyle Sails)**: Membrantechnologie mit eingespritzten Fasern.
  Ähnliche Eigenschaften wie 3Di.
- **Fusion M (Elvström)**: Membransegel mit patentiertem Faserverlauf.

**Beschichtungen und Veredelungen:**
- **Resin-Finish (Dacron)**: Harzappretierung für reduzierte Dehnung und
  Wasserabweisung. Verschleißt mit der Zeit (3–5 Saisons).
- **UV-Inhibitoren**: In das Garn eingebrachte UV-Stabilisatoren.
  Wirkung begrenzt auf 3.000–5.000 Sonnenstunden.
- **Anti-Fouling (Unterwassersegel)**: Spezialcoating für Langfahrt-Yachten,
  z. B. Coppercoat Sailclean.

### 1.4 Wartungsphilosophie

Die AYDI-Wartungsphilosophie basiert auf drei Grundsätzen:

1. **Prävention vor Reparatur**: Regelmäßige Inspektion und Pflege vermeiden
   kostspielige Reparaturen. 80 % aller Segelschäden sind vermeidbar.

2. **Materialgerechte Behandlung**: Jedes Segelmaterial erfordert spezifische
   Pflegemethoden. Was für Dacron gut ist, kann Laminat zerstören.

3. **Dokumentation**: Jede Inspektion, Reparatur und Beobachtung wird
   protokolliert. Nur so können Degradationstrends erkannt und die optimale
   Austauschzeit bestimmt werden.

---

## 2. Wartungsplan

### 2.1 Vor dem Segeln (Pre-Sail-Check)

Vor jedem Segeln sollte eine visuelle Kurzinspektion durchgeführt werden.
Dauer: 5–10 Minuten pro Segel.

#### Checkliste Pre-Sail

**Großsegel:**
- [ ] Segellatten korrekt eingesetzt und gesichert
- [ ] Kopfbrett-Verbindung intakt, Bolzen/Schäkel fest
- [ ] Schothorn-Kausch ohne Risse oder Deformation
- [ ] Hals-Befestigung am Lümmelbeschlag fest
- [ ] Vorliek-Rutscher oder Gleitschiene: keine fehlenden/beschädigten Elemente
- [ ] Achterliek-Trimmfaden vorhanden und frei
- [ ] Reffbänder und -leinen: richtige Lage, kein Verschleiß an Umlenkpunkten
- [ ] Lazy Jacks / Lazy Bag: kein Einklemmen des Segels
- [ ] UV-Schutzstreifen (bei Rollgroßsegel): keine Ablösung

**Vorsegel (Genua/Fock):**
- [ ] Vorliek: Lümmeltau im Rollprofilkanal frei laufend
- [ ] Schothorn-Kausch intakt
- [ ] Kopf-Verbindung zum Fall-Wirbel gesichert
- [ ] Schoten: keine Schamfilstellen, besonders an Salingen-Höhe
- [ ] UV-Streifen (bei Rollvorsegel): vollständig, keine Ablösung
- [ ] Rollanlage: Drehung leichtgängig, kein Blockieren

**Spinnaker/Gennaker:**
- [ ] Tuch auf Risse prüfen (besonders an Nahtkreuzungen)
- [ ] Kopf-, Hals-, Schothorn-Verstärkungen intakt
- [ ] Bergeschlauch (Snuffer) funktionsfähig
- [ ] Spinnaker-Fall und Barber-Hauler korrekt geschoren

### 2.2 Monatliche Wartung

Während der Segelsaison sollte monatlich eine gründlichere Inspektion erfolgen.
Dauer: 30–60 Minuten für alle Segel.

#### Monatliche Maßnahmen

**Alle Segel:**

1. **Süßwasserspülung**
   - Nach Salzwassereinsatz: Segel mit Süßwasser absprühen oder spülen.
   - Besonders kritisch: Nähte, Verstärkungen, Lattentaschen.
   - Methode: Gartenschlauch mit Brauseaufsatz, kein Hochdruckreiniger.
   - Wasser darf lauwarm sein (max. 30 °C), niemals heiß.

2. **Naht-Schnellcheck**
   - Sichtprüfung aller sichtbaren Nähte auf Fadenbrüche.
   - Stichprobenartig an 5 Stellen manuell am Faden ziehen.
   - Fokuspunkte: Schothorn, Kopfbrett, Reff-Ösen, Lattentaschen-Enden.

3. **Schamfilstellen kontrollieren**
   - Typische Stellen: Salingen, Wanten, Relingdrähte, Lazy Jacks.
   - Neuen Schamfilschutz anbringen, wenn Abrieb sichtbar (>0,3 mm Materialabtrag).
   - Produkte: Insignia Sailcloth Tape (selbstklebend, 25 EUR/10 m),
     Chafe Guard (Dyneema-Geflecht, 35 EUR/m).

4. **Schmutzentfernung**
   - Vogelkot sofort entfernen (Säure greift Beschichtung an).
   - Stockflecken behandeln, bevor sie sich ausbreiten.
   - Rost von Drahtresten (gerissene Litzen) sofort behandeln.

**Dacron-Segel zusätzlich:**
- Resin-Finish prüfen: Tuch knistern lassen → stumpfes Tuch = Finish abgebaut.
- Lose Fäden am Achterliek abschneiden (nicht ziehen!).

**Laminat-Segel zusätzlich:**
- Auf Blasenbildung (Delamination) an Nahtkreuzungen prüfen.
- Knickstellen vermeiden: Segel nicht unnötig oft bergen/setzen.
- Feuchtigkeit im Segelsack kontrollieren.

**Membran-Segel (3Di/D4) zusätzlich:**
- Oberfläche auf Mikrorisse in der Schutzschicht prüfen.
- Keine Knickfalten zulassen: Segel auf Baum oder in Lazy Bag lassen.
- Herstellerempfehlungen für Pflegemittel beachten.

### 2.3 Saisonale Wartung (Einwintern / Auswintern)

#### 2.3.1 Einwintern (Herbst)

Die Einwinterung ist die wichtigste Wartungsmaßnahme des Jahres.

**Schritt 1: Demontage**
- Segel vollständig vom Rigg abnehmen.
- Alle Beschläge (Rutscher, Schäkel, Kauschen) fotografisch dokumentieren.
- Reihenfolge und Position der Segellatten markieren (Steuerbord/Backbord).
- Rollvorsegel: von der Rollanlage abnehmen, nicht aufgerollt lassen.

**Schritt 2: Reinigung**
- Gründliche Reinigung gemäß Abschnitt 3 (Reinigung).
- Mindestens Süßwasserspülung, idealerweise Handwäsche.
- Alle Schimmelflecken behandeln.
- Alle Rost- und Grünspanflecken entfernen.

**Schritt 3: Trocknung**
- Segel vollständig trocknen lassen. Mindestens 24 Stunden bei Raumtemperatur.
- Bei Dacron: Im Freien bei trockenem Wetter ausbreiten (nicht in praller Sonne).
- Bei Laminat: In einem belüfteten Raum, nicht in direkter Sonne.
- Restfeuchte-Test: Segel zusammenlegen, 1 Stunde warten, auffalten →
  kein feuchter Geruch = trocken.

**Schritt 4: Inspektion**
- Vollständige Nahtinspektion gemäß Abschnitt 5.
- UV-Streifen-Zustand bewerten.
- Alle Beschädigungen fotografieren und dokumentieren.
- Reparaturbedarf festlegen und ggf. Segelmacher kontaktieren.
  Tipp: Im Herbst haben Segelmacher weniger Aufträge → schnellere Bearbeitung.

**Schritt 5: Reparaturen durchführen**
- Kleine Reparaturen (Patches, Nahtausbessern) selbst durchführen.
- Größere Reparaturen an den Segelmacher geben (Winterauftrag = günstiger).
- UV-Streifen erneuern lassen, wenn nötig.

**Schritt 6: Lagerung**
- Gemäß Abschnitt 7 (Lagerung) einlagern.
- Lagerort: trocken, dunkel, temperiert (5–25 °C), Luftfeuchtigkeit <60 %.
- Keine schweren Gegenstände auf die Segel legen.

**Schritt 7: Dokumentation**
- Segelbuch aktualisieren: Zustand, durchgeführte Maßnahmen, Segel-Stunden.
- Fotos archivieren für Vergleich mit Vorjahren.

#### 2.3.2 Auswintern (Frühjahr)

**Schritt 1: Sichtprüfung nach Lagerung**
- Segel entfalten und auf Schimmel, Stockflecken, Nagetierbefall prüfen.
- Nähte kontrollieren: Hat sich während der Lagerung etwas gelöst?
- Segellatten auf Bruch oder Delaminierung prüfen.

**Schritt 2: Leichtreinigung**
- Staub und Lagerrückstände entfernen.
- Bei Bedarf nochmals waschen.

**Schritt 3: Beschläge prüfen**
- Alle Kauschen, Ösen, Rutscher auf Korrosion und Verschleiß prüfen.
- Rutscherkugeln / Gleitelemente schmieren (Harken McLube, ca. 18 EUR).
- Reißverschlüsse an Lattentaschen gangbar machen (Zipper-Wax oder Bienenwachs).

**Schritt 4: Montage**
- Segel in umgekehrter Reihenfolge der Demontage anschlagen.
- Segellatten gemäß Markierung einsetzen.
- Vorliek-Spannung gemäß Herstellerangabe einstellen.

**Schritt 5: Funktionstest**
- Erstes Setzen des Segels an Land oder im Hafen.
- Rollanlage auf Leichtgängigkeit prüfen.
- Reffsystem testen.
- Trimm kontrollieren.

### 2.4 Jährliche Wartung

Zusätzlich zur saisonalen Wartung sollte jährlich eine vertiefte Inspektion
stattfinden, idealerweise durch einen qualifizierten Segelmacher.

#### Jährliche Maßnahmen

**1. Professionelle Segel-Inspektion**
- Segelmacher-Inspektion: 80–200 EUR pro Segel (je nach Größe).
- Beinhaltet: Nahtfestigkeitsmessung, Tuchdehnungstest, UV-Degradationscheck.
- Ergebnis: Zustandsbericht mit Empfehlungen und Restlebensdauer-Schätzung.

**2. Segelform-Analyse**
- Fotografische Segelform-Dokumentation (Profiltiefe, Twist, Eintrittwinkel).
- Vergleich mit Neuzustand bzw. Vorjahreswerten.
- Bei Dacron: Akzeptabler Formverlust ca. 5–8 % pro Saison.
- Bei Laminat: Formverlust sollte <3 % pro Saison sein.

**3. Hardware-Inspektion**
- Kopfbrett: Nietenverbindungen prüfen, Bolzen auf Materialermüdung testen.
- Kauschen an Schothorn, Hals, Reff-Ösen: auf Elongation und Rissbildung prüfen.
- Verstärkungspatches an Belastungspunkten: Ablösung, Risse, Durchscheuern.
- Segellatten: Biegeprofil messen und mit Sollwert vergleichen.
  Dacron-Latten: Austausch alle 5–7 Jahre.
  GFK-Latten: Austausch alle 8–12 Jahre.
  Carbon-Latten: Austausch alle 10–15 Jahre (bei unbeschädigter Oberfläche).

**4. Resin-Finish erneuern (nur Dacron)**
- McLube SailKote Anwendung: Spray-Applikation auf gereinigtes Segel.
- Wirkung: Reduziert Reibung, verbessert Wasserabweisung, schützt vor UV.
- Kosten: ca. 25 EUR pro Dose (reicht für ein Großsegel bis 12 m).
- Alternative: Ronstan Sailguard (ca. 30 EUR/Flasche).

**5. UV-Schutzstreifen-Erneuerung (bei Rollsegeln)**
- Alle 4–6 Jahre sollte der UV-Streifen erneuert werden.
- Kosten: 300–800 EUR je nach Segelgröße (professionell).
- Material: Sunbrella-Acrylstoff, Farbe an Segel angepasst.

### 2.5 Drei-Jahres-Wartung (Großinspektion)

Alle drei Jahre empfiehlt sich eine umfassende Überholung:

**Dacron-Segel:**
- Professionelle Wäsche in Segelwaschanlage: 150–400 EUR.
- Nahtrevision: alle Nähte prüfen, kritische Stellen nachennähen.
- Resin-Finish komplett erneuern.
- Segelform vermessen und ggf. Achterliek-Kurve nachjustieren.
- Geschätzte Gesamtkosten: 400–1.200 EUR.

**Laminat-Segel:**
- Professionelle Inspektion auf Delaminierung (Lichttisch-Prüfung).
- Kritische Klebestellen nachkaschieren.
- Schutzfilm erneuern (bei 3Di: Taffeta-Repair).
- Geschätzte Gesamtkosten: 600–2.500 EUR.

**Spinnaker/Gennaker:**
- Nahtrevision aller Triple-Punkt-Verstärkungen (Kopf, Hals, Schothorn).
- Riss-Reparaturen kumuliert durchführen.
- Bergeschlauch-Leine und -Ring erneuern.
- Geschätzte Gesamtkosten: 200–800 EUR.

### 2.6 Wartungsintervalle nach Materialtyp — Zusammenfassung

| Maßnahme | Dacron | Laminat | Membran (3Di) | Nylon (Spi) |
|----------|--------|---------|---------------|-------------|
| Süßwasserspülung | Monatlich | Nach jeder Nutzung | Nach jeder Nutzung | Nach jeder Nutzung |
| Naht-Schnellcheck | Monatlich | Monatlich | Vierteljährlich | Monatlich |
| Gründliche Reinigung | Saisonal | Saisonal | Saisonal | Saisonal |
| Naht-Vollinspektion | Jährlich | Jährlich | Jährlich | Jährlich |
| Professionelle Inspektion | Jährlich | Jährlich | Jährlich | Alle 2 Jahre |
| UV-Streifen erneuern | Alle 4–6 J. | Alle 4–6 J. | Alle 5–7 J. | n/a |
| Resin-Finish erneuern | Jährlich | n/a | n/a | n/a |
| Segelform vermessen | Alle 2 Jahre | Jährlich | Jährlich | n/a |
| Großinspektion (Segelmacher) | Alle 3 Jahre | Alle 2–3 Jahre | Alle 3 Jahre | Alle 3 Jahre |
| Latten-Austausch | 5–7 Jahre | 5–7 Jahre | nach Herst. | n/a |

### 2.7 Wartungs-Logbuch Vorlage

Für die systematische Dokumentation empfiehlt sich folgendes Logbuch-Format:

```
SEGEL-WARTUNGS-LOGBUCH
======================
Yacht: _________________ Segel: _________________ Segelnummer: _____
Hersteller: _____________ Material: ______________ Baujahr: _________
Fläche: _________ m²     Segelmacher: ____________ Letzte Überholung: _____

Datum | Maßnahme | Befund | Nächste Aktion | Stunden gesamt
------|----------|--------|----------------|---------------
      |          |        |                |
      |          |        |                |
```

---

## 3. Reinigung

### 3.1 Grundprinzipien der Segelreinigung

Die korrekte Reinigung ist entscheidend für die Segellebensdauer. Fehlerhafte
Reinigung kann mehr Schaden anrichten als Verschmutzung.

**Grundregeln:**
1. Kein Hochdruckreiniger — zerstört Beschichtungen und Laminatverbindungen.
2. Kein heißes Wasser über 40 °C — lässt Resin-Finish aufweichen.
3. Keine chlorhaltigen Reiniger — greift Nähgarn und Fasern an.
4. Keine aggressiven Lösungsmittel — Aceton, Toluol etc. zerstören Laminat.
5. Kein maschinelles Bürsten — scheuert Oberfläche auf.
6. Immer vollständig trocknen lassen vor Lagerung.
7. Reinigungsmittel immer zuerst an unauffälliger Stelle testen.

### 3.2 Handwäsche — Standardmethode

Die Handwäsche ist die schonendste und für alle Segeltypen geeignete Methode.

**Benötigtes Material:**
- Große, saubere Fläche (Rasen, sauberer Steg, Plane)
- Süßwasser (Schlauch mit Brauseaufsatz)
- Weicher Schwamm oder Segelbürste (keine Wurzelbürste!)
- Segelreiniger (siehe 3.4)
- Eimer (20 l)

**Vorgehensweise:**

1. **Vorbereitung**
   - Segel auf sauberer Fläche ausbreiten.
   - Untergrund darf keine scharfen Kanten oder Steine haben.
   - Bei Wind: Segel mit Gewichten fixieren.

2. **Vorspülung**
   - Gesamtes Segel gründlich mit Süßwasser abspülen.
   - Dabei Salzkristalle und losen Schmutz entfernen.
   - Besonders Nähte, Taschen und Verstärkungen durchspülen.
   - Einwirkzeit: 10–15 Minuten feucht halten.

3. **Reinigungslösung anmischen**
   - Reiniger gemäß Herstellerangabe verdünnen.
   - Typische Verdünnung: 50–100 ml auf 10 l Wasser.
   - Wasser: lauwarm (20–30 °C) für beste Wirkung.

4. **Reinigung**
   - Lösung mit Schwamm auftragen, in Tuchrichtung arbeiten.
   - Nicht schrubben, sondern mit leichtem Druck wischen.
   - Hartnäckige Flecken: Lösung 15–30 Minuten einwirken lassen.
   - Nähte besonders gründlich bearbeiten.
   - Obere Seite reinigen, dann Segel wenden und Unterseite reinigen.

5. **Nachspülung**
   - Gründlich mit klarem Süßwasser nachspülen.
   - Mindestens 2× komplett abspülen, um alle Reinigungsmittelreste zu entfernen.
   - Rückstände können Gewebe angreifen oder Schimmelwachstum fördern.

6. **Trocknung**
   - Segel aufhängen (am besten an einer Leine über die gesamte Länge).
   - Nicht in praller Sonne trocknen (UV-Belastung).
   - Beide Seiten müssen vollständig trocken sein.
   - Trocknungszeit: 4–8 Stunden bei guter Belüftung, 12–24 Stunden bei hoher Luftfeuchtigkeit.

### 3.3 Maschinenwäsche

Die maschinelle Reinigung ist nur für Dacron-Segel und Nylon-Spinnaker geeignet.
Laminate und Membransegel dürfen NICHT maschinell gewaschen werden.

**Voraussetzungen:**
- Industriewaschmaschine mit Frontlader (kein Toplader!).
  Haushaltswaschmaschine nur für Segel bis ca. 15 m².
- Kein Schleudern oder nur niedrige Drehzahl (max. 400 U/min).
- Keine Weichspüler.

**Einstellungen:**
- Temperatur: max. 30 °C (kalt für Nylon-Spinnaker).
- Programm: Feinwäsche / Wollprogramm.
- Schleuderdrehzahl: 0 oder max. 400 U/min.
- Waschmittel: spezieller Segelreiniger, KEIN Vollwaschmittel.

**Professionelle Segelwaschanlage:**
Einige Segelmacher und Segelwäschereien bieten maschinelle Großsegel-Reinigung an:
- Verfahren: Durchlaufwaschanlage mit Flachwalzen.
- Reiniger: spezielle Formulierung für Segeltuch.
- Kosten: 8–15 EUR/m² Segelfläche.
- Anbieter (Beispiele): Segel-Service Laboe, Quantum Sails Hamburg,
  Elvström Sails Service-Center.

### 3.4 Reinigungsmittel — Vergleich

#### Star brite Sail & Canvas Cleaner
- **Typ**: Alkalischer Reiniger, biologisch abbaubar
- **pH-Wert**: 9,5–10,5
- **Geeignet für**: Dacron, Nylon, Canvas, UV-Streifen
- **Nicht geeignet für**: Laminat (nur in starker Verdünnung)
- **Verdünnung**: 1:10 bis 1:20
- **Einwirkzeit**: 5–15 Minuten
- **Preis**: ca. 15 EUR / 500 ml Konzentrat
- **Besonderheit**: Entfernt auch leichte Schimmelflecken
- **Bezugsquelle**: Compass24, SVB, AWN

#### Snyder Manufacturing Sail Bath
- **Typ**: Enzymatischer Reiniger
- **pH-Wert**: 7,5–8,5 (nahezu neutral)
- **Geeignet für**: Alle Segeltypen inkl. Laminat
- **Verdünnung**: 50 ml auf 20 l Wasser
- **Einwirkzeit**: 30–60 Minuten (Enzyme brauchen Zeit)
- **Preis**: ca. 28 EUR / 1 l
- **Besonderheit**: Sehr schonend, ideal für hochwertige Segel
- **Bezugsquelle**: Segelmacher, Online-Fachhandel

#### Biovex Sail Cleaner
- **Typ**: Biologischer Reiniger auf Pflanzenbasis
- **pH-Wert**: 7,0–8,0 (pH-neutral)
- **Geeignet für**: Alle Segeltypen, besonders Laminat und Membran
- **Verdünnung**: 1:15 bis 1:25
- **Einwirkzeit**: 10–20 Minuten
- **Preis**: ca. 22 EUR / 750 ml
- **Besonderheit**: Umweltverträglich, hafentauglich, keine Umweltauflagen
- **Bezugsquelle**: Segelmacher, Online-Segelshops

#### Hausmittel (mit Vorsicht!)

| Mittel | Verdünnung | Anwendung | Risiko |
|--------|-----------|-----------|--------|
| Spülmittel (pH-neutral) | 5 ml / 10 l | Leichte Verschmutzung | Rückstände möglich |
| Backpulver | 2 EL / 10 l | Stockflecken, Geruch | Aufhellend bei Farbsegeln |
| Essig (5 %) | 1:4 mit Wasser | Kalkflecken, Salz | Kann Nähgarn angreifen |
| Oxalsäure (1 %) | 10 g / 1 l | Rostflecken | Nur punktuell, gut nachspülen |

### 3.5 Fleckenentfernung — Spezialmethoden

#### Schimmel und Stockflecken

Schimmel ist eines der häufigsten Probleme bei Segeln. Frühzeitige Behandlung
ist entscheidend — alter Schimmel lässt sich kaum noch vollständig entfernen.

**Methode 1: Leichter Schimmel (< 4 Wochen alt)**
1. Segel in der Sonne ausbreiten (UV tötet Schimmelsporen).
2. Trockenen Schimmel mit weicher Bürste abbürsten.
3. Star brite Mildew Stain Remover aufsprühen (ca. 14 EUR/500 ml).
4. 15 Minuten einwirken lassen.
5. Mit Schwamm und Wasser abwaschen.
6. Gründlich nachspülen.

**Methode 2: Mittlerer Schimmel (1–3 Monate alt)**
1. Segel 2 Stunden in Lösung einweichen:
   10 l Wasser + 100 ml Biovex Sail Cleaner + 50 ml Weißweinessig.
2. Mit weichem Schwamm behandeln.
3. Bei Dacron: Zusätzlich Star brite Sail & Canvas Cleaner unverdünnt
   auf die Flecken auftragen.
4. Gründlich nachspülen, trocknen lassen.

**Methode 3: Schwerer Schimmel (> 3 Monate, tiefgehend)**
1. Professionelle Behandlung empfohlen.
2. Segelmacher verwenden industrielle Enzyme oder Ozon-Behandlung.
3. Kosten: 150–400 EUR je nach Segelgröße.
4. Achtung: Tiefgehender Schimmel schwächt das Gewebe dauerhaft.
   Festigkeitsverlust von 10–25 % möglich.

#### Rostflecken

Rostflecken entstehen durch Kontakt mit korrodierenden Metallteilen
(Wantenspanner, Rutscher, lose Schrauben).

**Behandlung:**
1. Oxalsäure-Lösung (1 %): 10 g auf 1 l warmes Wasser.
2. Nur auf die Rostflecken auftragen (Wattebausch oder Sprühflasche).
3. 5–10 Minuten einwirken lassen.
4. Sofort und gründlich mit Süßwasser nachspülen.
5. Wiederholung bei Bedarf.
6. Alternative: Rust Remover von Star brite (ca. 12 EUR/500 ml).

**Wichtig:**
- Oxalsäure ist gesundheitsschädlich → Handschuhe und Schutzbrille tragen.
- Nicht auf Nylon-Spinnaker anwenden (Faserstruktur wird angegriffen).
- Anwendung nie länger als 15 Minuten.

#### Grünspan (Kupferoxid)

Entsteht durch Kontakt mit Kupfer- oder Bronzebeschlägen.

**Behandlung:**
1. Essiglösung (10 %): 100 ml Essigessenz auf 900 ml Wasser.
2. Mit Schwamm auf Fleck auftragen.
3. 10 Minuten einwirken lassen.
4. Gründlich nachspülen.
5. Bei hartnäckigen Flecken: Vorgang wiederholen mit Bürste.

#### Ölflecken (Motoröl, Schmierfett)

**Behandlung:**
1. Frisches Öl: Sofort mit Küchenpapier abtupfen (nicht reiben!).
2. Talkumpuder oder Babypuder auf den Fleck streuen, 2 Stunden einwirken lassen.
3. Puder abbürsten.
4. Star brite Sail & Canvas Cleaner unverdünnt auftragen.
5. 20 Minuten einwirken lassen.
6. Mit Schwamm und warmem Wasser abwaschen.
7. Gründlich nachspülen.

#### Vogelkot

**Behandlung:**
1. Sofort handeln — Vogelkot ist stark säurehaltig (pH 3–4).
2. Angetrockneten Kot einweichen: Nasses Tuch 10 Minuten auflegen.
3. Vorsichtig mit Schwamm entfernen.
4. Mit Segelreiniger nachwaschen.
5. Nachspülen.

#### Blutflecken

**Behandlung:**
1. Nur mit KALTEM Wasser behandeln (Hitze fixiert Protein).
2. Salzwasserlösung: 2 EL Salz auf 500 ml kaltes Wasser.
3. Fleck 30 Minuten einweichen.
4. Mit Schwamm und Segelreiniger nachwaschen.

### 3.6 Reinigung nach Materialtyp

#### Dacron-Segel

- Robustestes Material für Reinigung.
- Verträgt pH 6–11.
- Maschinenwäsche möglich (Feinwäsche, 30 °C).
- Nach Reinigung optional: McLube SailKote aufsprühen.
- Häufigkeit: Mindestens 1× pro Saison gründlich.
- Resin-Finish wird durch jede Wäsche etwas reduziert.

#### Laminat-Segel

- Sehr empfindlich! Nur pH-neutrale Reiniger verwenden (pH 7–8,5).
- Keine Maschinenwäsche.
- Nicht falten oder knicken beim Reinigen.
- Am besten auf flacher, sauberer Fläche liegend reinigen.
- Snyder Sail Bath oder Biovex Sail Cleaner empfohlen.
- Keine mechanische Beanspruchung (kein Schrubben).

#### Membran-Segel (3Di, D4)

- Herstellerempfehlung zwingend beachten.
- North Sails empfiehlt: nur Wasser und mildes Spülmittel.
- Keine Lösungsmittel, keine aggressiven Reiniger.
- Oberfläche nicht schrubben (Taffeta-Schutzschicht empfindlich).
- Professionelle Reinigung alle 3 Jahre empfohlen.

#### Nylon-Spinnaker / Gennaker

- Empfindlich gegenüber UV, Hitze und Chemikalien.
- Nur kaltes oder lauwarmes Wasser (max. 25 °C).
- pH-neutrale Reiniger (pH 6,5–8,0).
- Maschinenwäsche möglich (Kaltprogramm, ohne Schleudern).
- Sehr vorsichtig mit Fleckenentfernern — immer zuerst testen.
- Ripstop-Nylon: Klebstellen können sich bei zu viel Feuchtigkeit lösen.

### 3.7 Häufige Reinigungsfehler

| Fehler | Folge | Vermeidung |
|--------|-------|------------|
| Hochdruckreiniger | Delamination, Beschichtungsverlust | Nur Gartenschlauch |
| Bleichmittel (Chlor) | Nähgarn-Zerstörung, Faserabbau | Nur sauerstoffbasierte Mittel |
| Heißes Wasser (>40 °C) | Resin-Finish löst sich | Max. 30 °C |
| Trockner/Heißluft | Schrumpfung, Formverlust | An der Luft trocknen |
| Bürste auf Laminat | Delaminierung, Kratzer | Nur weichen Schwamm |
| Reiniger nicht abspülen | Gewebeschädigung, Schimmelförderung | Mindestens 2× nachspülen |
| Feucht einlagern | Schimmel innerhalb 4 Wochen | Komplett trocknen lassen |
| Vollwaschmittel | Optische Aufheller schädigen UV-Schutz | Nur Segelreiniger |

---

## 4. UV-Schutz

### 4.1 UV-Schädigung verstehen

UV-Strahlung ist der größte Feind von Segeltuch. Sie baut Polymer-Ketten ab
und reduziert Festigkeit, Elastizität und Farbbrillanz.

**UV-Empfindlichkeit nach Material:**

| Material | UV-Beständigkeit | Festigkeitsverlust/1000 h UV | Lebensdauer (Mittelmeer) |
|----------|-----------------|------------------------------|--------------------------|
| Dacron (Polyester) | Gut | 5–8 % | 8–12 Jahre |
| Pentex (PEN) | Gut | 4–7 % | 8–14 Jahre |
| Nylon (Polyamid) | Schlecht | 15–25 % | 3–5 Jahre |
| Dyneema (UHMWPE) | Gut (UV) | 3–5 % | 10–15 Jahre |
| Kevlar (Aramid) | Sehr schlecht | 20–35 % | 2–4 Jahre ungeschützt |
| Technora | Mäßig | 10–15 % | 5–8 Jahre |
| PBO (Zylon) | Extrem schlecht | 30–50 % | 1–3 Jahre ungeschützt |
| Carbon | Sehr gut | 1–3 % | 15+ Jahre |

**UV-Exposition nach Revier:**

| Revier | UV-Index (Sommer) | Jährl. Sonnenstunden | Degradationsfaktor |
|--------|-------------------|---------------------|-------------------|
| Ostsee (54°N) | 5–7 | 1.600–1.900 | 1,0 (Referenz) |
| Nordsee (53°N) | 5–7 | 1.500–1.800 | 0,95 |
| Mittelmeer (38–43°N) | 8–10 | 2.500–3.000 | 1,6–1,9 |
| Karibik (15–20°N) | 10–12 | 2.800–3.200 | 2,0–2,3 |
| Tropen (0–15°N/S) | 11–14 | 2.500–3.000 | 2,2–2,5 |
| Südpazifik (15–30°S) | 10–13 | 2.600–3.100 | 2,1–2,4 |

**Berechnung der UV-Belastung:**
```
Effektive UV-Stunden = Sonnenstunden × Degradationsfaktor × Expositionsanteil
```
Dabei ist der Expositionsanteil:
- Rollsegel ohne UV-Streifen, permanent aufgerollt: 0,15
- Rollsegel mit UV-Streifen: 0,03 (nur gesetzte Zeit)
- Segel mit Persenning/Abdeckung: 0,05
- Segel auf Baum ohne Abdeckung: 0,30
- Segel in Lazy Bag: 0,08

### 4.2 UV-Schutzstreifen

Der UV-Schutzstreifen (auch UV-Cover, UV-Leech Cover) ist der wichtigste
Schutz für Rollsegel.

#### Materialien

**Sunbrella Acrylstoff (Standard):**
- Hersteller: Glen Raven Mills (USA) / Dickson (EU-Lizenz)
- Material: Solution-dyed Acrylic (durchgefärbte Acrylfaser)
- UV-Blockierung: >98 % der UV-A und UV-B Strahlung
- Lebensdauer: 8–12 Jahre (Mittelmeer), 10–15 Jahre (Nordeuropa)
- Gewicht: 290–340 g/m² (je nach Ausführung)
- Farboptionen: >100 Farben, Standard: Navy, Pacific Blue, Captain Navy
- Preis: ca. 25–35 EUR/m (konfektioniert, inkl. Saum)

**Sattlerplane / PVC-beschichtetes Polyester:**
- Günstiger als Sunbrella, aber weniger UV-beständig.
- Lebensdauer: 4–6 Jahre.
- Neigt zum Verhärten und Reißen.
- Preis: ca. 12–20 EUR/m.

**Parasail-Tuch (beschichtetes Nylon):**
- Leicht, aber begrenzte UV-Beständigkeit.
- Nur für temporären Einsatz geeignet.
- Lebensdauer: 2–4 Jahre.

#### Breite des UV-Streifens berechnen

Die Breite des UV-Streifens hängt von der Wickeltrommel-Geometrie ab:

**Formel für Rollvorsegel:**
```
UV-Streifen-Breite = π × Wickeldurchmesser + 50 mm Überlappung
```

Wobei:
- Wickeldurchmesser = Rollstag-Durchmesser + 2 × (Anzahl Wicklungen × Tuchstärke)
- Typische Werte bei vollständig eingerolltem Segel:

| Vorliek-Länge | Rollstag-Ø | Tuchstärke | Typische Wicklungen | Wickel-Ø | UV-Streifen-Breite |
|---------------|-----------|-----------|---------------------|---------|-------------------|
| 8 m | 8 mm | 0,4 mm | 12–15 | 18–20 mm | 105–115 mm |
| 10 m | 10 mm | 0,5 mm | 14–18 | 24–28 mm | 125–140 mm |
| 12 m | 12 mm | 0,5 mm | 16–20 | 28–32 mm | 140–150 mm |
| 14 m | 14 mm | 0,6 mm | 18–22 | 36–40 mm | 165–175 mm |
| 16 m | 16 mm | 0,7 mm | 20–25 | 44–51 mm | 190–210 mm |

> ✅ Aufgeloest (Audit): 105–115 mm — Quelle: dokumentinterne Formel Abschnitt 4.2 (π × Wickel-Ø 18–20 mm + 50 mm = 106,5–112,8 mm), gerundet konsistent mit den Zeilen 10–16 m derselben Tabelle. Der frühere untere Wert „115" war ein Tippfehler.

**Praxis-Empfehlung:**
Die meisten Segelmacher verwenden Standardbreiten:
- Vorsegel bis 12 m Vorliek: 150 mm
- Vorsegel 12–16 m Vorliek: 200 mm
- Vorsegel >16 m Vorliek: 250–300 mm

Für Rollgroßsegel ist der UV-Streifen am Unterliek und Achterliek breiter
(200–400 mm), da der Wickeldurchmesser am Mast/Baum größer ist.

#### Montage des UV-Streifens

**Methode 1: Genäht (Standard, professionell)**
- Nahttyp: Dreifach-Steppstich (Zickzack + 2× gerade).
- Garn: V-69 oder V-92 Polyester, UV-stabilisiert.
  Besser: Tenara PTFE-Garn (Gore) für maximale UV-Beständigkeit.
- Nahtzugabe: 15–20 mm.
- Untere Kante: umgeschlagen und doppelt vernäht (Schutz vor Ausfransen).
- Kosten (professionell): 300–800 EUR je nach Segelgröße.

**Methode 2: Klebend (temporäre Reparatur)**
- Kleber: Bostik Simson ISR 70-03 oder Sika Sikaflex 295 UV.
- Nur als Notlösung, da Kleber unter UV-Belastung aushärtet und abblättert.
- Lebensdauer: 1–2 Saisons.
- Kosten: ca. 30 EUR Material.

**Methode 3: Klett (selten, spezielle Segelmacher)**
- Klett-Streifen am Segel und UV-Streifen.
- Vorteil: Austauschbar.
- Nachteil: Klett verschmutzt, Haltekraft lässt nach.

#### Farbauswahl und Lebensdauer

Die Farbe des UV-Streifens beeinflusst seine Lebensdauer signifikant:

| Farbe | UV-Blockierung | Typische Lebensdauer | Empfehlung |
|-------|----------------|---------------------|------------|
| Dunkelblau (Navy) | 99 % | 10–14 Jahre | Beste Wahl für Langlebigkeit |
| Schwarz | 99 % | 10–14 Jahre | Gut, aber hohe Wärmeaufnahme |
| Mittelblau | 98 % | 8–12 Jahre | Guter Kompromiss |
| Grau | 97 % | 8–11 Jahre | Unauffällig |
| Weiß | 92 % | 6–9 Jahre | Geringster UV-Schutz |
| Rot | 96 % | 6–10 Jahre | Verblasst schneller |
| Grün | 97 % | 7–11 Jahre | Mittlere Lebensdauer |
| Gelb | 94 % | 5–8 Jahre | Nicht empfohlen |

### 4.3 UV-Schutz-Beschichtung: 303 Aerospace Protectant

303 Aerospace Protectant ist ein Referenzprodukt für UV-Schutz auf Segeltuch
und Canvas.

**Produktdaten:**
- Hersteller: Gold Eagle / 303 Products
- Wirkstoff: UV-absorbierende Polymere + Antioxidantien
- UV-Blockierung: bis zu 96 % der UV-A und UV-B Strahlung
- Anwendung: Auf saubere, trockene Oberfläche aufsprühen und mit Tuch verteilen.
- Ergiebigkeit: ca. 3–5 m²/50 ml.
- Wiederholungsintervall: alle 4–6 Wochen (oder nach starkem Regen).
- Preis: ca. 18 EUR / 473 ml (Sprühflasche), ca. 35 EUR / 946 ml.

**Anwendung auf Segeln:**
1. Segel muss sauber und vollständig trocken sein.
2. Dünn und gleichmäßig aufsprühen (30 cm Abstand).
3. Mit sauberem Mikrofasertuch gleichmäßig verteilen.
4. 30 Minuten trocknen lassen.
5. Zweite Schicht empfohlen für maximalen Schutz.

**Geeignet für:**
- UV-Streifen aus Sunbrella/Acryl
- Dacron-Segeltuch (verbessert auch Wasserabweisung)
- Canvas-Abdeckungen und Persennings
- Lazy Bags und Lazy Jacks

**Nicht geeignet für:**
- Laminat-Segel (kann Klebeschichten anlösen)
- Nylon-Spinnaker (verändert Handling)
- Membransegel (Herstellerfreigabe erforderlich)

**Alternative Produkte:**
- McLube SailKote: Trockenes PTFE-Spray, primär als Gleitbeschichtung,
  geringer UV-Schutz. Ca. 25 EUR/300 ml.
- Ronstan Sailguard: UV-Schutz + Wasserabweisung für Dacron. Ca. 30 EUR/500 ml.
- Star brite Waterproofing & UV-Treatment: Kombinationsprodukt für Canvas
  und Dacron. Ca. 22 EUR/1 l.

### 4.4 Weitere UV-Schutzmaßnahmen

**Segelabdeckung / Persenning:**
- Beste Schutzmaßnahme neben UV-Streifen.
- Material: Sunbrella Acryl (290–340 g/m²) oder Weathermax
  (Polyester-Gewebe mit UV-Beschichtung, 230 g/m²).
- Muss belüftet sein (Schimmelprävention).
- Kosten (Maßanfertigung):
  - Großsegel-Persenning (10 m Yacht): 350–700 EUR
  - Großsegel-Persenning (13 m Yacht): 600–1.200 EUR
  - Lazy Bag (10 m Yacht): 500–900 EUR
  - Lazy Bag (13 m Yacht): 800–1.500 EUR

**In-Mast- / In-Baum-Rollsysteme:**
- Segel ist im gerollten Zustand nahezu vollständig vor UV geschützt.
- UV-Streifen entfällt (bei vollständiger Rollung).
- Nachteil: Einschränkungen in der Segelform (kein Vortrieb-optimaler Schnitt).

**Segellatten-Abdeckung (Battcar Covers):**
- Schützen die exponierten Segellatten-Enden vor UV.
- Einfache Nachrüstung.
- Kosten: 10–30 EUR pro Satz.

---

## 5. Naht-Inspektion und Reparatur

### 5.1 Nähgarn-Typen im Segelbau

Die Naht ist oft die schwächste Stelle eines Segels. Das Verständnis der
verwendeten Garntypen ist essenziell für Wartung und Reparatur.

#### Polyester-Nähgarn (Standard)

**V-69 (Tex 70):**
- Durchmesser: ca. 0,35 mm
- Reißfestigkeit: ca. 5,5 kg (Einzelfaden)
- Einsatz: Standardnähte, Saum, leichte Verstärkungen
- UV-Beständigkeit: mittel (50 % Festigkeitsverlust nach ca. 2.000 h direkte UV)
- Farbe: weiß, schwarz, blau, rot (diverse)
- Preis: ca. 15 EUR / 200 m Spule (Bei großen Rollen: 8 EUR / 200 m)
- Herstelle: A&E (Gütermann), By Annie, Bedalon Marine

**V-92 (Tex 90):**
- Durchmesser: ca. 0,45 mm
- Reißfestigkeit: ca. 8 kg (Einzelfaden)
>- Einsatz: Hochbelastete Nähte, Verstärkungen, Lattentaschen, Reffpunkte
- UV-Beständigkeit: mittel (ähnlich V-69)
- Preis: ca. 18 EUR / 200 m Spule
- Standard für die meisten Segelmacher als „Arbeitsgarn"

**V-138 (Tex 135):**
- Durchmesser: ca. 0,60 mm
- Reißfestigkeit: ca. 14 kg
- Einsatz: Schwerlast-Verstärkungen, Kopfbretter, Kauschen-Einfassungen
- Nur auf Industrienähmaschinen verarbeitbar
- Preis: ca. 25 EUR / 200 m Spule

#### Tenara PTFE-Garn (Gore)

- Material: Expanded PTFE (Polytetrafluorethylen)
- Durchmesser: variabel, typisch 0,25–0,50 mm
- Reißfestigkeit: geringer als Polyester (ca. 3,5 kg bei Tenara HTR)
- UV-Beständigkeit: **HERVORRAGEND** — praktisch kein UV-Abbau
- Chemikalienbeständigkeit: praktisch inert
- Lebensdauer: überdauert das Segeltuch
- Nachteil: teuer, glatt (neigt zum Rutschen wenn nicht korrekt vernäht)
- Preis: ca. 45 EUR / 120 m (Tenara HTR)
- Hersteller: W.L. Gore & Associates
- Bezugsquelle: Sailrite, Segelmacher-Fachhandel

**Empfehlung:**
- Für UV-exponierte Nähte (Achterliek, UV-Streifen): Tenara PTFE
- Für geschützte Nähte (Innenverstärkungen): V-92 Polyester
- Für Reparaturen an Bord: V-92 wegen einfacherer Handhabung

#### Dyneema-Nähgarn

- Material: UHMWPE (Ultra High Molecular Weight Polyethylene)
- Reißfestigkeit: sehr hoch (ca. 12 kg bei 0,40 mm Ø)
- UV-Beständigkeit: gut
- Hitzeempfindlich: Schmelzpunkt bei 144 °C → Nähmaschinennadel kann Garn schmelzen
- Einsatz: Spezialanwendungen, Hochlast-Punkte
- Preis: ca. 35 EUR / 100 m
- Verarbeitung: Nur von erfahrenen Segelmachern

### 5.2 Nahttypen und Sticharten

#### Gerade Steppstich (Lockstitch)

- Häufigster Stich im Segelbau.
- Oberfaden und Unterfaden verschlingen sich miteinander.
- Stichlänge: 4–6 mm (Standard), 3–4 mm (Hochlast).
- Vorteil: Gleichmäßig, maschinenfreundlich.
- Nachteil: Fadenschnitt an einer Stelle → Naht löst sich in beide Richtungen.
- Einsatz: Bahnen-Zusammennähte, Saum, UV-Streifen.

#### Zickzack-Stich

- Stich in Zickzack-Muster.
- Stichbreite: 5–10 mm, Stichlänge: 3–5 mm.
- Vorteil: Elastisch, verteilt Last auf größere Fläche.
- Nachteil: Weniger zugfest als gerader Steppstich.
- Einsatz: Elastische Verbindungen, Überlappungsränder, UV-Streifen.

#### Dreifach-Zickzack (Triple Zigzag)

- Drei Stiche pro Zickzack-Schritt.
- Höchste Elastizität und Scheuerfestigkeit.
- Einsatz: Spinnaker-Nähte, stark belastete Kanten.

#### Überwendling-Stich (Overlock)

- Umfasst die Kante des Tuchs.
- Verhindert Ausfransen.
- Einsatz: Schnittkanten, Liektau-Einfassung.

#### Handnähte

**Segelstich (Flat Seam Stitch):**
- Für flache Überlappungsnähte.
- Nadel geht abwechselnd durch beide Lagen.
- Stichlänge: 5–8 mm.

**Runden (Herring-Bone Stitch):**
- Für das Annähen von Liektau.
- Kreuzstich-Muster über die Kante.
- Sehr robust, traditionelle Segelmacher-Technik.

**Ringknoten (Ring Stitch):**
- Für Kauschen und Ösen.
- Garn wird spiralförmig um die Kausch geführt.
- Extrem belastbar.

### 5.3 UV-Degradation von Nähten

UV-Strahlung ist die Hauptursache für Nahtversagen. Die Degradation folgt
einem charakteristischen Muster:

**Stadium 1: Oberflächenabbau (500–1.000 UV-Stunden)**
- Garn verliert Glanz.
- Leichte Aufrauhung der Oberfläche.
- Festigkeitsverlust: 10–20 %.
- Optisch: Kaum erkennbar.

**Stadium 2: Fortgeschrittener Abbau (1.000–2.000 UV-Stunden)**
- Garn wird spröde und fasert auf.
- Fadenzug mit dem Fingernagel löst Fasern.
- Festigkeitsverlust: 30–50 %.
- Optisch: Aufgerauhte, matte Nahtoberfläche.

**Stadium 3: Kritischer Abbau (2.000–3.000 UV-Stunden)**
- Garn bricht bei leichtem Zug.
- Einzelne Stiche fehlen bereits.
- Festigkeitsverlust: 50–80 %.
- Optisch: Lose Fadenenden, Lücken in der Naht.

**Stadium 4: Nahtversagen (>3.000 UV-Stunden)**
- Naht öffnet sich unter normaler Belastung.
- Großflächiges Versagen.
- Segel nicht mehr sicher einsetzbar.

**Zeitliche Einordnung (Rollvorsegel, Mittelmeer, ohne UV-Streifen):**
- Stadium 1: nach 6–12 Monaten
- Stadium 2: nach 12–24 Monaten
- Stadium 3: nach 24–36 Monaten
- Stadium 4: nach 36–48 Monaten

**Zeitliche Einordnung (Großsegel mit Persenning, Ostsee):**
- Stadium 1: nach 3–5 Jahren
- Stadium 2: nach 5–8 Jahren
- Stadium 3: nach 8–12 Jahren
- Stadium 4: nach 12–15 Jahren

### 5.4 Naht-Inspektion — Methodik

#### Visuelle Inspektion

1. Segel auf sauberer Fläche ausbreiten (bei gutem Licht).
2. Systematisch alle Nähte abgehen (Vorliek → Achterliek → Unterliek).
3. Auf folgende Indikatoren achten:
   - Aufgerauhte Garnoberfläche (UV-Degradation)
   - Lose Fadenenden
   - Fehlende Stiche (Lücken in der Naht)
   - Ausfransungen an Garnkreuzungen
   - Farbveränderung des Garns (Verbleichen)

#### Zugtest

1. An der zu testenden Stelle den Faden mit dem Fingernagel anheben.
2. Seitlich ziehen (nicht herausziehen!).
3. Bewertung:
   - Faden hält problemlos: OK
   - Faden gibt leicht nach, hält aber: Beobachten
   - Faden bricht: Naht ersetzen!

4. Stichproben an mindestens 10 Stellen pro Segel:
   - 3 × Achterliek (oben, Mitte, unten)
   - 2 × Unterliek (Mitte, Schothorn)
   - 2 × Vorliek (oben, unten)
   - 2 × Bahnennähte (verschiedene Positionen)
   - 1 × Lattentasche

#### Lichttest (für Laminatsegel)

1. Segel gegen das Licht halten oder von hinten beleuchten.
2. UV-degradierte Nähte erscheinen heller (dünner).
3. Delaminierte Bereiche zeigen ungleichmäßige Lichtdurchlässigkeit.

### 5.5 Naht-Reparatur von Hand

#### Werkzeuge für Handnähen

**Segelmacher-Handschuh (Palm):**
- Rechtshand-Modell (für Rechtshänder) oder Linkshand-Modell.
- Material: Leder mit Metalldruckplatte (Eisen).
- Funktion: Drückt die Nadel durch das Segeltuch.
- Empfehlung: William Smith & Son Sailmaker's Palm (ca. 45 EUR).
- Alternative: Großes Fingerhut-Modell (weniger Kontrolle, ca. 8 EUR).

**Segelnadeln:**
- Dreieckig geschliffene Spitze (schneidet das Gewebe, statt es zu zerreißen).
- Größen: Nr. 13 (dünn) bis Nr. 19 (dick).
  - Nr. 14–15: Standard für V-69/V-92 Garn
  - Nr. 16–17: Für V-138 und Tenara
  - Nr. 18–19: Für schwere Verstärkungen, Kauschen
- Herstelle: William Smith & Son, John James, Rubi Needles
- Preis: ca. 5–10 EUR / Sortiment (10 Stück)

**Segelnadel-Ahle (Pricker/Fid):**
- Zum Vorstanzen von Löchern in schweres Tuch.
- Zum Spleißen von Tauwerk.
- Preis: ca. 8–15 EUR.

**Heißschneider (Hot Knife):**
- Elektrisch oder gasbetriebenem.
- Zum Schneiden und gleichzeitigen Versiegeln von synthetischen Fasern.
- Verhindert Ausfransen an Schnittkanten.
- Empfehlung: Sailrite Hot Knife (ca. 60 EUR) oder
  Dremel Versatip Butangas (ca. 45 EUR).

**Sonstiges:**
- Bienenwachs (für Garnwachsen): 3 EUR
- Scharfe Segelschere: 15–30 EUR
- Maßband: 5 EUR
- Kreide / Markierstift (wasserlöslich): 3 EUR

#### Grundtechnik: Flachnaht von Hand

1. **Garnvorbereitung:**
   - Fadenlänge: max. 90 cm (längere Fäden verheddern sich).
   - Faden doppelt nehmen, Enden zusammenknoten.
   - Faden durch Bienenwachsblock ziehen (verbessert Gleiten, verhindert Verknoten).

2. **Nahtbeginn:**
   - 30 mm vor der beschädigten Stelle beginnen (Überlappung mit intakter Naht).
   - Nadel von der Rückseite einstechen.
   - 2–3 Rückstiche zur Verankerung.

3. **Stichreihe:**
   - Stichlänge: 5–6 mm.
   - Nahtabstand zum Rand: mindestens 8 mm.
   - Nadel mit Palm durch das Tuch drücken.
   - Faden gleichmäßig festziehen (nicht zu straff → Tuch zieht sich zusammen).

4. **Nahtende:**
   - 30 mm über die beschädigte Stelle hinaus weiternähen.
   - 3 Rückstiche, dann den Faden mit 2 halben Schlägen sichern.
   - Fadenende 10 mm stehen lassen, mit Feuerzeug/Heißschneider verschmelzen.

#### Technik: Kausch-Einfassung (Ring Stitch)

1. Neue Kausch (Edelstahl 316L oder Titan) positionieren.
2. V-138 oder Tenara-Garn verwenden.
3. Nadel durch das Tuchauge stechen, Faden um die Kausch führen.
4. Stiche eng setzen (3–4 mm Abstand).
5. 2–3 Durchgänge (Lagen) für maximale Festigkeit.
6. Mindestens 20 Stiche pro Kausch-Umrundung.

### 5.6 Maschinelles Nachnähen

Für größere Nahtabschnitte ist das maschinelle Nachnähen effizienter und
gleichmäßiger als Handnähen.

**Geeignete Maschinen:**

| Maschine | Typ | Nadelsystem | Preis (neu) | Geeignet für |
|----------|-----|-------------|-------------|-------------|
| Sailrite Ultrafeed LSZ-1 | Wandernadel-Flachbett | 138×17 | ca. 850 EUR | Heimwerker, leichte Segel |
| Sailrite Fabricator | Heavy-Duty Flachbett | 135×17 | ca. 1.200 EUR | Fahrtensegel, UV-Streifen |
| Consew 206RB-5 | Walking-Foot | 135×17 | ca. 1.500 EUR | Profi-Heimwerker |
| Juki LU-1508NH | Industriell | DY×3 | ca. 2.800 EUR | Segelmacher-Werkstatt |
| Adler 367 | Industriell | 134-35 | ca. 3.500 EUR | Segelmacher-Werkstatt |

**Hinweise für maschinelles Nähen an Segeln:**
- Nadel: Leder-/Segelnadel (Schneidspitze), Stärke je nach Tuchgewicht.
  - Leichtes Tuch (Spinnaker, <100 g/m²): Nadelstärke 80–90
  - Mittleres Tuch (Dacron, 150–250 g/m²): Nadelstärke 100–110
  - Schweres Tuch (>250 g/m², Verstärkungen): Nadelstärke 120–140
- Fadenspannung: An Probstück einstellen, bis Verschlingung in der Tuchmitte liegt.
- Transporteur: Walking-Foot oder Differential-Transport obligatorisch.
  Normaler Transport verzieht das Segel.
- Stichlänge: 4–6 mm (maschinell konsistenter als von Hand).

---

## 6. Reparaturtechniken

### 6.1 Patch-Reparatur

#### Klebepatches (Adhesive Patches)

Klebepatches eignen sich für:
- Kleine Risse und Löcher (< 50 mm Länge)
- Notfallreparaturen an Bord
- Nicht-tragende Bereiche des Segels

**Produkt 1: Insignia Sailcloth Tape**
- Material: Selbstklebendes Dacron-Segeltuch
- Breiten: 25 mm, 50 mm, 75 mm, 100 mm, 150 mm
- Farben: Weiß, Creme, Grau, Blau
- Kleber: Druckempfindlicher Acrylkleber
- Haftfestigkeit: ca. 3,5 N/cm
- UV-Beständigkeit: gut (3–5 Jahre)
- Preis: ca. 20 EUR / 7,5 m (75 mm Breite)
- Bezugsquelle: Compass24, SVB, Sailrite

**Anwendung Insignia-Patch:**
1. Bereich um den Riss/das Loch reinigen (Segelreiniger, dann Isopropanol).
2. Vollständig trocknen lassen.
3. Patch-Größe: mindestens 30 mm über den Riss hinaus in alle Richtungen.
4. Patch zuschneiden — Ecken abrunden (verhindert Ablösung an Ecken).
5. Schutzfolie abziehen und Patch auflegen.
6. Von der Mitte nach außen fest andrücken (Rakel oder Kreditkarte verwenden).
7. Von beiden Seiten patchen (beidseitiger Patch).
8. 24 Stunden aushärten lassen bei Raumtemperatur.

**Produkt 2: Tear-Aid Type A**
- Material: Transparentes, dehnbares Reparatur-Laminat
- Universell einsetzbar: Dacron, Nylon, Laminat, Canvas
- Extrem hohe Reißfestigkeit (überrascht für ein Reparaturband)
- Selbstklebend, sofort belastbar
- Transparent → optisch unauffällig
- Preis: ca. 25 EUR / Reparaturset (Typ A, verschiedene Größen)
- Bezugsquelle: Amazon, Bootszubehör-Händler

**Anwendung Tear-Aid:**
1. Oberfläche reinigen und trocknen (wie bei Insignia).
2. Patch 30 mm über den Schaden hinaus zuschneiden.
3. Ecken abrunden.
4. Schutzfolie abziehen, von einer Seite langsam auflegen (Blasenfrei!).
5. Fest andrücken.
6. Rückseite ebenfalls patchen.
7. Sofort belastbar, volle Festigkeit nach 24 Stunden.

#### Genähte Patches (Sewn Patches)

Genähte Patches sind die permanente Lösung für:
- Risse >50 mm
- Tragende Bereiche des Segels
- Dauerhafte Reparaturen

**Material:**
- Patch-Tuch: Gleiches Material wie das Segel (Dacron auf Dacron, etc.)
  Idealerweise Resttuch vom Segelmacher oder Insignia-Segeltuch vom Meter.
- Garn: V-92 Polyester oder Tenara PTFE.
- Kleber (optional): Segelkleber als Fixierung vor dem Nähen
  (z. B. Bostik 1400 TF, ca. 12 EUR/Tube).

**Vorgehensweise genähter Patch:**

1. **Schaden begrenzen:**
   - Rissenden mit Heißschneider versiegeln (Stoppbrennung).
   - Losen Fäden abschneiden.
   - Rissform dokumentieren.

2. **Patch zuschneiden:**
   - Mindestens 40 mm über den Riss in alle Richtungen.
   - Tuchrichtung beachten! Schuss und Kette des Patches müssen
     mit dem Segel übereinstimmen.
   - Ecken abrunden (Radius 15–20 mm).
   - Kanten umlegen (10 mm Nahtzugabe) und mit Heißschneider versiegeln.

3. **Patch positionieren:**
   - Patch mit 2–3 Streifen Klebeband fixieren.
   - Oder: Dünne Schicht Segelkleber auftragen und andrücken.
   - 30 Minuten trocknen lassen.

4. **Nähen:**
   - Äußere Naht: 10 mm vom Patch-Rand, gerader Steppstich.
   - Innere Naht: 5 mm innerhalb der äußeren Naht, Zickzack-Stich.
   - Stichlänge: 5 mm.
   - Nahtanfang und -ende: 3 Rückstiche.

5. **Rückseite:**
   - Zweiten Patch auf der Rückseite anbringen (gleiche Methode).
   - Ergibt Sandwich-Reparatur: Patch-Segel-Patch.

6. **Nachbearbeitung:**
   - Alle Fadenenden verschmelzen.
   - Naht mit 303 Aerospace Protectant behandeln.

### 6.2 Naht-Reparatur

**Teilweise Nahtöffnung (< 300 mm):**
1. 50 mm vor der Öffnung die alte Naht heraustrennen.
2. Tuchkanten ausrichten.
3. Von Hand oder Maschine mit V-92 nachnähen.
4. 50 mm über die Öffnung hinaus weiternähen.
5. Fadenenden sichern und verschmelzen.

**Vollständige Nahtöffnung (> 300 mm oder tragende Naht):**
1. Alte Nahtlöcher als Führung nutzen.
2. Tuchkanten reinigen und ggf. mit Heißschneider versiegeln.
3. Naht maschinell erneuern (Walking-Foot-Nähmaschine).
4. Ggf. Verstärkungsstreifen unter die Naht legen (bei abgenutztem Tuch).
5. Bei tragenden Nähten: Segelmacher konsultieren!

### 6.3 Lattentaschen-Reparatur

Lattentaschen-Schäden sind häufig und entstehen durch:
- Lattenenden, die durch das Tuch stoßen
- Reißverschluss-Versagen
- Scheuern am Achterliek
- Überlastung bei starkem Wind

**Reparatur Lattenöffnung:**
1. Alten Reißverschluss oder Klettverschluss entfernen.
2. Tuchkanten mit Heißschneider versiegeln.
3. Neuen Reißverschluss (YKK Marine #5 oder #8) einnähen.
4. Alternativ: Klettverschluss (25 mm Breite) als einfachere Lösung.
5. Lattenstopper (Elastikband) am geschlossenen Ende kontrollieren.

**Reparatur Lattendurchstoß:**
1. Latte entfernen.
2. Durchstoßstelle von innen mit Segeltuch-Patch verstärken.
3. Genähten Patch anbringen (mindestens 30 × 30 mm).
4. Am Lattenende: Gummikappe anbringen oder Endstück erneuern.
5. Prüfen, ob Lattenlänge korrekt ist (zu lange Latten drücken durch).

### 6.4 Kopfbrett-Reparatur

Das Kopfbrett (Headboard) ist der am höchsten belastete Bereich des Großsegels.

**Typische Schäden:**
- Nieten lockern sich oder brechen aus.
- Tuch reißt um die Befestigungspunkte.
- Kopfbrett-Platte verbiegt sich.

**Reparatur (begrenzt möglich an Bord):**
1. Temporär: Durchziehen einer Dyneema-Leine durch die Kopfbrett-Öse als
   Fall-Notbefestigung.
2. An Land: Neue Nieten setzen (Monelbronze- oder Edelstahl-Blindnieten).
3. Bei Tuchriss: Verstärkungsschicht aus schwerem Dacron (300–380 g/m²)
   beidseitig aufnähen.
4. Kopfbrett-Platte ersetzen (Edelstahl 316L oder Aluminium 6061-T6).

**Wichtig:** Kopfbrett-Reparaturen an professionellen Segelmacher übergeben,
wenn irgend möglich. Fehler hier können zum Verlust des Segels führen.

### 6.5 UV-Streifen-Austausch

Der Austausch des UV-Streifens ist alle 4–8 Jahre erforderlich.

> ⚠️ **ZU PRÜFEN (Audit):** „4–8 Jahre" hier vs. „alle 4–6 Jahre" in Abschnitt 2.4, Tabelle 2.6 und Abschnitt 8.1 — dokumentinterne Abweichung. Dominant und maßgeblich ist 4–6 Jahre; nicht sicherheitskritisch.

**Entfernung des alten Streifens:**
1. Alte Nähte aufschneiden (Nahttrenner oder scharfes Messer).
2. Vorsichtig den alten Streifen ablösen.
3. Klebereste mit Isopropanol entfernen.
4. Segeltuch inspizieren: Ist das darunter liegende Tuch noch intakt?

**Montage des neuen Streifens:**
1. Neuen Sunbrella-Streifen zuschneiden (Breite: siehe Abschnitt 4.2).
2. Länge: Achterliek + 50 mm Zugabe an jeder Seite.
3. Kanten umlegen und mit Heißschneider fixieren.
4. Streifen mit Klebeband oder Segelkleber fixieren.
5. Dreifach-Naht: Zickzack + 2× gerader Steppstich.
6. Garn: Tenara PTFE (für maximale Lebensdauer) oder V-92 UV-stabilisiert.

**Kosten Selbstmontage:**
- Sunbrella-Stoff: 25–35 EUR/m
- Tenara-Garn: 45 EUR/Spule
- Gesamtkosten (Material): 80–150 EUR
- Zeitaufwand: 4–8 Stunden (je nach Erfahrung)

**Kosten Segelmacher:**
- Material + Arbeit: 300–800 EUR (je nach Segelgröße)
- Bearbeitungszeit: 2–5 Werktage

### 6.6 Schothorn- und Hals-Verstärkung

Die Ecken des Segels (Kopf, Schothorn, Hals) tragen die höchsten Lasten.

**Verstärkungsreparatur:**
1. Bereich inspizieren: Sind die Weblines (innere Verstärkungsbänder) intakt?
2. Äußere Verstärkungslage (Patchwork) auf Risse und Ablösung prüfen.
3. Bei Ablösung: Lage mit V-138 Garn nachnähen.
4. Bei Riss: Neue Verstärkungslage aus schwerem Dacron aufnähen.
5. Kausch prüfen und ggf. ersetzen.

### 6.7 DIY vs. Professionelle Reparatur — Entscheidungshilfe

| Schadenstyp | DIY möglich? | Geschätzte Kosten (DIY) | Geschätzte Kosten (Profi) |
|-------------|-------------|------------------------|--------------------------|
| Kleiner Riss (<50 mm) | Ja | 5–20 EUR | 50–120 EUR |
| Mittlerer Riss (50–200 mm) | Ja (mit Erfahrung) | 15–40 EUR | 100–300 EUR |
| Großer Riss (>200 mm) | Bedingt | 30–80 EUR | 200–600 EUR |
| Naht nachnähen (<500 mm) | Ja | 10–25 EUR | 80–200 EUR |
| Naht nachnähen (>500 mm) | Ja (Nähmaschine) | 15–40 EUR | 150–400 EUR |
| Lattentasche reparieren | Ja | 10–30 EUR | 60–180 EUR |
| UV-Streifen ersetzen | Bedingt (Nähmaschine) | 80–150 EUR | 300–800 EUR |
| Kopfbrett reparieren | Nein | — | 150–500 EUR |
| Schothorn verstärken | Bedingt | 30–60 EUR | 200–600 EUR |
| Lümmeltau ersetzen | Nein | — | 200–800 EUR |
| Delamination reparieren | Nein | — | 300–2.000 EUR |
| Segelform korrigieren | Nein | — | 400–1.500 EUR |

### 6.8 Werkzeugkasten für Segelreparaturen

**Basis-Set (an Bord):**
- Segelmacher-Palm (1×): 45 EUR
- Segelnadeln Sortiment (Nr. 14–18): 8 EUR
- V-92 Polyester-Garn (weiß, 50 m): 8 EUR
- Bienenwachs: 3 EUR
- Insignia Sailcloth Tape (75 mm × 7,5 m): 20 EUR
- Tear-Aid Type A Set: 25 EUR
- Heißschneider (Butangas): 45 EUR
- Segelschere: 20 EUR
- Maßband + Markierstift: 8 EUR
- **Gesamtkosten Basis-Set: ca. 182 EUR**

**Erweitertes Set (für ambitionierte Eigner):**
- Basis-Set: 182 EUR
- Sailrite Ultrafeed LSZ-1 Nähmaschine: 850 EUR
- Tenara PTFE-Garn (120 m): 45 EUR
- V-138 Garn (50 m): 15 EUR
- Segelkleber Bostik 1400 TF: 12 EUR
- Dacron-Segeltuch (1 m²): 15 EUR
- Sunbrella-Stoff (1 m): 30 EUR
- YKK Marine Reißverschluss (2 m): 12 EUR
- **Gesamtkosten Erweitertes Set: ca. 1.161 EUR**

---

## 7. Lagerung

### 7.1 Lagerungsprinzipien

Korrekte Lagerung ist entscheidend für die Segellebensdauer. Die meisten
Lagerschäden sind auf Feuchtigkeit, UV-Exposition oder mechanische
Belastung zurückzuführen.

**Grundregeln:**
1. Segel müssen vor der Lagerung vollständig trocken sein.
2. Lagerort: dunkel, trocken, belüftet, temperiert.
3. Keine schweren Gegenstände auf die Segel.
4. Keine scharfen Kanten oder spitze Gegenstände in der Nähe.
5. Regelmäßige Kontrolle während der Lagerzeit (monatlich).

### 7.2 Falten vs. Rollen

#### Falten (Flaking)

**Vorteile:**
- Kompakteres Packmaß.
- Einfacher bei großen Segeln.
- Traditionelle Methode.

**Nachteile:**
- Erzeugt Knickfalten (besonders schädlich für Laminatsegel).
- An Faltkanten höherer Verschleiß.
- Resin-Finish bei Dacron wird an Faltkanten beschädigt.

**Richtige Falttechnik:**
1. Segel auf sauberer Fläche ausbreiten.
2. In Bahnen parallel zum Unterliek zusammenfalten.
3. Faltenbreite: ca. 80–100 cm.
4. Dann von einem Ende her aufrollen.
5. Bei jedem Einlagern die Faltlinien leicht versetzen (→ keine permanenten Knicke).

#### Rollen (Rolling)

**Vorteile:**
- Keine scharfen Knickfalten.
- Besser für Laminatsegel und Membransegel.
- Gleichmäßigere Belastung des Tuchs.

**Nachteile:**
- Größeres Packmaß.
- Schwierig bei großen Segeln ohne Helfer.

**Richtige Rolltechnik:**
1. Segel auf sauberer Fläche ausbreiten.
2. Segellatten entfernen (wenn möglich).
3. Vom Kopf zum Fuß rollen (Vorliek als Achse).
4. Nicht zu straff rollen (→ Faltenabdruck).
5. Nicht zu lose rollen (→ Segel verrutscht im Sack).

#### Empfehlung nach Material

| Material | Empfohlene Methode | Begründung |
|----------|-------------------|------------|
| Dacron | Falten oder Rollen | Robust, verträgt beides |
| Laminat | Rollen (zwingend!) | Knickfalten zerstören Laminat |
| Membran (3Di) | Rollen oder gemäß Hersteller | Empfindlich gegen Knicke |
| Nylon (Spinnaker) | Lose Falten | Leicht, flexibel |

### 7.3 Segelsäcke

**Standard-Segelsack (Tuch):**
- Material: Dacron-Segeltuch oder Cordura-Nylon.
- Muss atmungsaktiv sein (kein luftdichter Sack!).
- Ventilationsöffnungen oder Mesh-Einsätze.
- Kosten: 30–80 EUR (je nach Größe).

**Langzeit-Lagersack:**
- Wasserabweisendes, aber dampfdurchlässiges Material (z. B. DuPont Tyvek).
- UV-stabil für den Fall, dass der Sack im Freien gelagert wird.
- Kosten: 50–120 EUR.

**Spinnaker-Turtle:**
- Spezieller Sack für den schnellen Einsatz des Spinnakers.
- Öffnung nach oben, sortierte Einpackmethode.
- Nicht als Langzeitlagerung geeignet.

### 7.4 Optimale Lagerbedingungen

| Parameter | Idealwert | Grenzwert | Folge bei Überschreitung |
|-----------|-----------|-----------|--------------------------|
| Temperatur | 10–20 °C | 5–35 °C | >35 °C: Kleber und Laminat weichen auf |
| Luftfeuchtigkeit | 40–55 % | <60 % | >60 %: Schimmelgefahr |
| Licht | Dunkel | Keine direkte Sonne | UV-Degradation auch bei Lagerung |
| Belüftung | Regelmäßig | Mind. alle 2 Wochen | Stehende Luft → Kondensat → Schimmel |
| Untergrund | Trocken, sauber | Kein Boden mit Feuchtigkeitsaufstieg | Feuchte dringt durch Sack |

**Anti-Schimmel-Maßnahmen:**
1. Silikagelpackungen in den Segelsack legen (50–100 g pro Segel).
   Kosten: ca. 5 EUR / 500 g (wiederverwendbar nach Trocknung im Ofen).
2. Kalziumchlorid-Entfeuchter in der Nähe aufstellen (nicht im Sack!).
3. Anti-Schimmel-Streifen (z. B. Star brite NosGUARD SG, ca. 8 EUR / 2 Stk.).
4. Lavendelsäckchen oder Zedernholzstücke: natürlicher Mottenschutz.

### 7.5 In-Boom- und In-Mast-Rollsysteme — Lagerung

Bei Yachten mit In-Boom- oder In-Mast-Rollsystemen bleiben die Segel
ganzjährig am Rigg.

**Wintermaßnahmen für In-Mast-Rollsegel:**
1. Segel komplett ausrollen und inspizieren (bei gutem Wetter).
2. Süßwasser-Spülung am Rigg durchführen.
3. Segel komplett einrollen und sicherstellen, dass kein Tuch exponiert ist.
4. Rollmechanismus konservieren (Spray-Wachs auf Lager und Getriebe).
5. Mastpersenning anbringen (falls vorhanden).

**Wintermaßnahmen für In-Baum-Rollsegel:**
1. Wie oben, zusätzlich Baumpersenning anbringen.
2. Drainageöffnungen am Baum freihalten.
3. Regelmäßig kontrollieren, ob Kondenswasser im Baum steht.

**Risiken bei ganzjähriger Lagerung am Rigg:**
- Kondenswasser im Mast/Baum führt zu Schimmel.
- Restfeuchtigkeit im Segel kann nicht entweichen.
- UV-Exposition geringer (da eingerollt), aber nicht null.
- Empfehlung: Trotzdem alle 2–3 Jahre Segel abnehmen, reinigen, inspizieren.

### 7.6 Lagerung von Spinnaker und Gennaker

Spinnaker und Gennaker aus Nylon erfordern besondere Aufmerksamkeit:

1. Nach Gebrauch sofort aus dem Bergeschlauch nehmen und trocknen lassen.
2. Nylon nimmt Feuchtigkeit auf (Hygroskopie) → Schimmelgefahr.
3. Lose zusammenfalten (keine engen Knicke).
4. In atmungsaktiven Sack legen.
5. Niemals in nassem Zustand lagern — auch nicht über Nacht!
6. Im Bergeschlauch nur während des aktiven Segelns aufbewahren.

---

## 8. Professionelle Beurteilung

### 8.1 Wann zum Segelmacher?

**Sofort (Sicherheitsrelevant):**
- Riss >300 mm in einem tragenden Bereich
- Kopfbrett-/Schothorn-/Hals-Beschädigung
- Lümmeltau-Beschädigung
- Mehr als 30 % der Nähte im Achterliek degradiert
- Strukturelles Versagen von Verstärkungen

**Zeitnah (nächste Wochen):**
- UV-Streifen hat >20 % Ablösung
- Delamination bei Laminatsegeln
- Mehrere Lattentaschen beschädigt
- Segel hat signifikant an Form verloren (Bauch gewandert)
- Vorliek-Lümmeltau hat Abrieb >30 %

**Planbar (nächste Saison):**
- UV-Streifen-Erneuerung (alle 4–6 Jahre)
- Umfassende Nahtrevision (alle 3 Jahre)
- Segelform-Korrektur
- Recut (Neuprofilierung)
- Umrüstung (z. B. zusätzliche Reff-Ebene)

### 8.2 Kosten professioneller Leistungen

| Leistung | 8–10 m Yacht | 10–13 m Yacht | 13–16 m Yacht | >16 m Yacht |
|----------|-------------|---------------|---------------|-------------|
| Segel-Inspektion | 60–100 EUR | 80–150 EUR | 100–200 EUR | 150–300 EUR |
| Nahtrevision (komplett) | 200–400 EUR | 350–700 EUR | 600–1.200 EUR | 1.000–2.500 EUR |
| UV-Streifen erneuern | 200–350 EUR | 300–550 EUR | 450–800 EUR | 700–1.500 EUR |
| Patch-Reparatur (mittel) | 80–180 EUR | 100–250 EUR | 150–350 EUR | 250–600 EUR |
| Kopfbrett-Reparatur | 120–250 EUR | 150–350 EUR | 200–500 EUR | 350–800 EUR |
| Recut / Reprofilierung | 300–600 EUR | 500–1.000 EUR | 800–1.800 EUR | 1.500–4.000 EUR |
| Waschen (professionell) | 100–200 EUR | 150–300 EUR | 250–500 EUR | 400–900 EUR |
| Lümmeltau erneuern | 150–350 EUR | 250–500 EUR | 350–700 EUR | 600–1.200 EUR |

### 8.3 Segel-Inspektionsprotokoll

Ein professioneller Segelmacher erstellt typischerweise folgenden Befund:

```
SEGEL-INSPEKTIONSBERICHT
========================
Datum: ________ Segelmacher: _____________ Betrieb: ______________
Yacht: ______________ Segel: _____________ Baujahr Segel: _______
Material: ____________ Fläche: ____ m²     Segelstunden (geschätzt): ____

NAHTBEWERTUNG (1-5, 1=Neuzustand, 5=Versagen)
  Vorliek:     [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5
  Achterliek:  [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5
  Unterliek:   [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5
  Bahnennähte: [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5
  Verstärk.:   [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5

TUCH-BEWERTUNG
  UV-Degradation:   [ ] Keine  [ ] Leicht  [ ] Mittel  [ ] Schwer
  Delamination:     [ ] Keine  [ ] Beginn  [ ] Lokal   [ ] Großflächig
  Form:             [ ] Gut    [ ] Akzeptabel  [ ] Verformt  [ ] Stark verformt
  Verschmutzung:    [ ] Sauber [ ] Leicht  [ ] Mittel  [ ] Stark

HARDWARE-BEWERTUNG
  Kopfbrett:    [ ] OK  [ ] Überwachen  [ ] Reparieren  [ ] Ersetzen
  Schothorn:    [ ] OK  [ ] Überwachen  [ ] Reparieren  [ ] Ersetzen
  Hals:         [ ] OK  [ ] Überwachen  [ ] Reparieren  [ ] Ersetzen
  Lattentaschen:[ ] OK  [ ] Überwachen  [ ] Reparieren  [ ] Ersetzen
  Segellatten:  [ ] OK  [ ] Überwachen  [ ] Reparieren  [ ] Ersetzen

UV-STREIFEN
  Zustand:      [ ] Gut  [ ] Verblasst  [ ] Ablösung  [ ] Ersetzen

GESAMTBEWERTUNG
  [ ] Kein Handlungsbedarf
  [ ] Kleine Reparaturen empfohlen
  [ ] Umfassende Reparatur nötig
  [ ] Segel am Ende der Lebensdauer — Ersatz planen
  [ ] Sicherheitsbedenken — sofortige Reparatur

Geschätzte Restlebensdauer: ________ Saisons
Empfohlene Maßnahmen: ____________________________________________
Geschätzte Kosten: _____________ EUR
```

### 8.4 Segelmacher in Deutschland — Auswahlkriterien

**Qualitätsmerkmale eines guten Segelmachers:**
1. Langjährige Erfahrung (>10 Jahre im Geschäft).
2. Eigene Werkstatt mit industriellen Nähmaschinen.
3. Lichttisch für Laminat-Inspektion.
4. Kenntnis der aktuellen Materialien und Technologien.
5. Bereitschaft zur Transparenz bei Kostenvoranschlag.
6. Referenzen von anderen Eignern.

**Regionale Empfehlung (ohne Vollständigkeit):**
- Ostsee: Latitude Sails (Kiel), Quantum Sails (Kiel/Hamburg), Sanders Segel (Flensburg)
- Nordsee: Hood Sails (Hamburg), Elvström Sails (Hamburg)
- Bodensee: Segelmacherei Erhart (Lindau), Ulmer Segel (Friedrichshafen)
- Mittelmeer (deutschsprachige): Sailpoint (Mallorca), OneSails (verschiedene Standorte)

---

## 9. Fehlerbild-Atlas

### F-16_08-01: UV-Fadendegradation

**Bezeichnung:** UV-bedingte Nähgarn-Degradation

**Beschreibung:**
Die Nähfäden an UV-exponierten Bereichen (Achterliek, Unterliek, UV-Streifen-Nähte)
zeigen fortschreitenden Festigkeitsverlust durch ultraviolette Strahlung.

**Visuelle Merkmale:**
- Aufgerauhte, fasrige Garnoberfläche
- Matte, verbleichte Fadenfarbe (weißes Garn wird gelblich-grau)
- Lose Fadenenden ragen aus der Naht
- In fortgeschrittenem Stadium: sichtbare Lücken in der Naht
- Faden bricht bei leichtem Fingernagel-Test

**Typische Lokalisierung:**
- Achterliek-Nähte (höchste UV-Exposition)
- UV-Streifen-Nähte (wenn Garn nicht UV-stabil)
- Unterliek-Nähte (bei Segel auf Baum ohne Abdeckung)
- Obere 30 % des Großsegels (längere Sonnenexposition)

**Ursachen:**
- Polyester-Nähgarn (V-69/V-92) ohne UV-Stabilisatoren
- Fehlender oder unzureichender UV-Schutz (Persenning, UV-Streifen)
- Hohe UV-Belastung (südliche Reviere)
- Segel dauerhaft gesetzt oder ohne Abdeckung

**Schweregrade:**
| Grad | Beschreibung | Maßnahme | Dringlichkeit |
|------|-------------|----------|---------------|
| 1 | Leichte Aufrauhung, Faden hält | Beobachten, UV-Schutz verbessern | Niedrig |
| 2 | Deutliche Aufrauhung, Faden unter Zug intakt | Nachnähen planen | Mittel |
| 3 | Faden bricht bei Zug, vereinzelte Lücken | Nachnähen nötig | Hoch |
| 4 | Großflächige Nahtöffnung | Sofortige Reparatur | Kritisch |

**Empfohlene Maßnahmen:**
- Grad 1–2: UV-Streifen prüfen/erneuern, Persenning anbringen, Tenara-Garn
  für nächste Nahtrevision einplanen
- Grad 3: Betroffene Nähte mit Tenara PTFE-Garn nachnähen
- Grad 4: Segel nicht verwenden, sofortige professionelle Reparatur

**Prävention:**
- Tenara PTFE-Garn für alle UV-exponierten Nähte
- UV-Streifen aus Sunbrella-Acryl in Dunkelblau
- Segelpersenning bei Nichtgebrauch
- 303 Aerospace Protectant auf exponierten Nähten

---

### F-16_08-02: Schimmel und Stockflecken

**Bezeichnung:** Biologischer Befall durch Schimmelpilze

**Beschreibung:**
Schimmelpilze und Stockflecken entstehen, wenn Segel in feuchtem Zustand gelagert
oder schlecht belüftet werden. Der Befall ist zunächst oberflächlich, dringt aber
mit der Zeit in die Faser ein und schwächt das Gewebe.

**Visuelle Merkmale:**
- Schwarze, graue oder grünliche Flecken (unregelmäßig verteilt)
- Modriger Geruch
- Stockflecken: runde, bräunliche Verfärbungen
- In schweren Fällen: sichtbarer Pilzrasen (samtartige Oberfläche)

**Typische Lokalisierung:**
- Bereiche, die nach dem Bergen innen liegen (Faltkern)
- Lattentaschen (Feuchtigkeit staut sich)
- Unterliek-Bereich (nimmt beim Segeln Spritzwasser auf)
- Segel in Lazy Bags ohne Drainage

**Schweregrade:**
| Grad | Beschreibung | Festigkeitsverlust | Maßnahme |
|------|-------------|-------------------|----------|
| 1 | Oberflächliche Flecken, <5 % der Fläche | <5 % | Reinigung, Trocknung |
| 2 | Moderate Flecken, 5–15 % der Fläche | 5–10 % | Professionelle Reinigung |
| 3 | Starker Befall, >15 % der Fläche, Geruch | 10–25 % | Professionelle Behandlung |
| 4 | Durchdringender Befall, Tuch mürbe | >25 % | Segel ersetzen |

**Empfohlene Maßnahmen:**
- Grad 1: Selbstreinigung (siehe Abschnitt 3.5)
- Grad 2: Enzymatische Reinigung (Snyder Sail Bath)
- Grad 3: Professionelle Ozon-Behandlung oder industrielle Reinigung
- Grad 4: Segel ist nicht mehr zuverlässig reparierbar

**Prävention:**
- Segel IMMER trocken einlagern
- Belüftete Segelsäcke verwenden
- Silikagelpackungen im Segelsack
- Lazy Bag mit Drainageöffnungen
- Bei Langfahrt: Segel regelmäßig entfalten und trocknen lassen

---

### F-16_08-03: Rostflecken

**Bezeichnung:** Korrosionsbedingte Verfärbung durch Eisenoxid

**Beschreibung:**
Rostflecken entstehen durch Kontakt mit korrodierenden Metallteilen. Sie sind
primär ein kosmetisches Problem, können aber bei dauerhafter Einwirkung die
Gewebestruktur schwächen.

**Visuelle Merkmale:**
- Braune bis orangefarbene Flecken
- Oft streifenförmig (entlang von Drähten oder Metallkanten)
- Manchmal punkt- oder ringförmig (von Schrauben/Nieten)

**Typische Lokalisierung:**
- Bereich der Salingen (Wantkontakt)
- Entlang des Vorlieks (Rollstag-Korrosion)
- Um Metallösen und Nieten (Kopfbrett, Reffpunkte)
- Achterlich bei Kontakt mit korrodierten Leinen-Kauschen

**Ursachen:**
- Korrodierte Edelstahlteile (crevice corrosion, 304 statt 316L)
- Rostige Schrauben oder Bolzen in der Nähe
- Lose Litzendrähte von beschädigten Wanten
- Nicht-marine Metallteile (falsches Material)

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Leichte Flecken, punktuell | Oxalsäure-Behandlung |
| 2 | Deutliche Flecken, mehrere Stellen | Reinigung + Ursache beheben |
| 3 | Großflächig, wiederkehrend | Professionelle Reinigung + Metallteile ersetzen |

**Empfohlene Maßnahmen:**
- Fleckenbehandlung mit Oxalsäure (1 %) gemäß Abschnitt 3.5
- Ursache identifizieren und beheben (korrodiertes Teil ersetzen)
- Metallteile auf 316L-Qualität prüfen

---

### F-16_08-04: Laminat-Delamination

**Bezeichnung:** Schichtentrennung bei Laminat-Segeln

**Beschreibung:**
Die Trennung der Laminatschichten (Film, Fasern, Taffeta) ist der häufigste
Schadenstyp bei Laminatsegeln. Sie beginnt typischerweise an Nahtdurchstichen,
Knickfalten oder Rändern und breitet sich mit der Zeit aus.

**Visuelle Merkmale:**
- Blasenbildung zwischen den Laminatschichten
- Milchig-trübe Bereiche (Luft zwischen den Schichten)
- Knistern beim Zusammendrücken
- In fortgeschrittenem Stadium: Sichtbare Trennung der Schichten
- Fasern lösen sich vom Film

**Typische Lokalisierung:**
- Entlang von Nahtlinien (Nadeldurchstiche als Startpunkte)
- Achterliek (höchste Belastung + UV)
- Knickfalten (von unsachgemäßer Lagerung)
- Bereiche mit wiederholter Schamfilbelastung

**Ursachen:**
- Unsachgemäße Lagerung (Knicke im Laminat)
- Feuchtigkeit dringt durch Nadellöcher ein und löst Kleber
- Salzkristalle in den Schichten (osmotischer Effekt)
- UV-Degradation des Klebstoffs
- Mechanische Ermüdung (zu viele Zyklen)
- Alter (Klebstoff hat begrenzte Lebensdauer)

**Schweregrade:**
| Grad | Beschreibung | Flächenanteil | Maßnahme |
|------|-------------|--------------|----------|
| 1 | Vereinzelte Blasen, <5 mm Ø | <2 % | Beobachten |
| 2 | Mehrere Blasen, teils >10 mm | 2–10 % | Nachkaschieren lassen |
| 3 | Zusammenhängende Delamination | 10–25 % | Professionelle Reparatur |
| 4 | Großflächige Trennung | >25 % | Segel ersetzen |

**Empfohlene Maßnahmen:**
- Grad 1: Monitoring, korrekte Lagerung (rollen, nicht knicken)
- Grad 2: Segelmacher: lokales Nachkaschieren (Heißpresse)
- Grad 3: Segelmacher: großflächige Reparatur oder Taffeta-Erneuerung
- Grad 4: Wirtschaftlicher Totalschaden, Neusegel empfohlen

**Prävention:**
- Laminatsegel IMMER rollen, niemals knicken
- Nach Salzwasser: immer mit Süßwasser spülen
- Feuchte Lagerung strikt vermeiden
- Segel nicht häufiger als nötig bergen und setzen

---

### F-16_08-05: Schamfilschaden an Salingen

**Bezeichnung:** Abriebschaden durch Kontakt mit Salingen und Wanten

**Beschreibung:**
Bei jedem Kreuzen berührt die Genua/Fock die Salingen und Wanten. Diese
Reibung führt zu progressivem Abrieb des Segeltuchs.

**Visuelle Merkmale:**
- Aufgerauhte, dünne Tuchstellen in Salingenhöhe
- Farbveränderung (hellere Stelle durch Abrieb der Oberfläche)
- Bei Laminat: Taffeta abgescheuert, Fasergelege sichtbar
- Im Extremfall: Durchscheuern des Tuchs

**Typische Lokalisierung:**
- Genua/Fock: Bereich auf Höhe der Salingen
- Position variiert mit Segeleinstellung (Schot-Fahr- und Trimmwinkel)
- Innenspannbereich bei gerollter Genua

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Leichte Aufrauhung, Tuch noch intakt | Schamfilschutz anbringen |
| 2 | Deutlicher Abrieb, Tuch gedünnt | Patch aufnähen + Schamfilschutz |
| 3 | Tuch fast durchgescheuert | Professionelle Reparatur |
| 4 | Durchgescheuert / Loch | Sofortige Reparatur (Segelmacher) |

**Empfohlene Maßnahmen:**
- Schamfilschutz an Salingen: Spreader Boots (Gummischoner), ca. 25 EUR/Paar
- Schamfilschutz am Segel: Dyneema-Chafe Patches aufnähen
- Trimmoptimierung: Genua nicht zu eng an den Salingen fahren
- Salingenwinkel prüfen: Zu spitze Salingen erhöhen Abrieb
- Salingenenden verrunden und polieren

---

### F-16_08-06: Killriss (Flogging Tear)

**Bezeichnung:** Riss durch Segelflattern (Killen)

**Beschreibung:**
Unkontrolliertes Flattern (Killen) des Segels erzeugt hohe dynamische Lasten,
die zu Materialermüdung und Rissen führen. Besonders bei Leichtwindsegeln
und Spinnakern.

**Visuelle Merkmale:**
- Riss entlang einer Naht oder parallel dazu
- Oft im oberen Drittel des Segels (höchste Flatter-Amplituden)
- Rissränder ausgefranst (bei gewebt) oder scharfkantig (bei Laminat)
- Tuch an der Rissstelle oft bereits ermüdet (dünn, weich)

**Typische Lokalisierung:**
- Achterliek des Großsegels (besonders ohne Lazylines)
- Vorliek des Vorsegels (beim Rollen)
- Spinnaker: gesamte Fläche bei Kollaps/Überraschungs-Halse
- Gennaker: im oberen Drittel

**Ursachen:**
- Segel zu lange im Killen gelassen (z. B. beim Wenden)
- Falscher Trimm (zu loses Achterliek)
- Gebrochene Segellatten (kein Halt im Achterliek)
- Automatische Wende ohne vorherige Segel-Sicherung

**Schweregrade:**
| Grad | Risslänge | Maßnahme |
|------|-----------|----------|
| 1 | <50 mm | Klebepatches beidseitig |
| 2 | 50–200 mm | Genähter Patch |
| 3 | 200–500 mm | Professionelle Reparatur |
| 4 | >500 mm | Segelmacher, ggf. Neusegel |

**Prävention:**
- Segel nie unnötig killen lassen
- Achterliek-Spannung korrekt einstellen
- Segellatten regelmäßig auf Bruch prüfen
- Bei Sturm: Segel rechtzeitig reffen oder bergen

---

### F-16_08-07: UV-Streifen-Versagen

**Bezeichnung:** Ablösung, Versprödung oder Zerfall des UV-Schutzstreifens

**Beschreibung:**
Der UV-Streifen an Rollsegeln ist selbst UV-exponiert und hat eine begrenzte
Lebensdauer. Versagen des UV-Streifens führt zu beschleunigter Degradation
des darunter liegenden Segeltuchs.

**Visuelle Merkmale:**
- Verblasste Farbe (besonders bei hellen Farben)
- Verhärtung und Versprödung des Stoffs
- Ablösung der Nähte (UV-degradiertes Garn)
- Risse im UV-Streifen-Material
- Sichtbares Segeltuch unter abgelöstem Streifen

**Typische Lokalisierung:**
- Achterliek-UV-Streifen (höchste Exposition)
- Unterliek-UV-Streifen (bei Rollgroßsegeln)
- Oberes Drittel (intensivere UV-Strahlung)

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Farbverblassung, Stoff noch intakt | Monitoring |
| 2 | Leichte Verhärtung, Nähte intakt | UV-Streifen-Erneuerung planen |
| 3 | Nähte lösen sich, Stoff brüchig | UV-Streifen ersetzen (zeitnah) |
| 4 | Großflächige Ablösung | Sofortige Erneuerung |

---

### F-16_08-08: Lattentaschen-Verschleiß

**Bezeichnung:** Verschleiß und Schäden an Segellatten-Taschen

**Beschreibung:**
Lattentaschen unterliegen mechanischem Verschleiß durch Lattenbewegung,
Halsen, und Reffen. Der Reißverschluss oder Klettverschluss ist oft die
erste Schwachstelle.

**Visuelle Merkmale:**
- Reißverschluss klemmt oder öffnet sich selbständig
- Klettverschluss haftet nicht mehr (Fusseln, Verformung)
- Tuch an den Lattenenden durchgescheuert
- Lattenstopper (Elastik) ausgeleiert
- Lattentasche längs aufgerissen

**Typische Lokalisierung:**
- Alle Lattentaschen, besonders die obere und untere
- Lattenenden (Innenseite der Tasche)
- Reißverschluss-/Klett-Öffnung

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Reißverschluss schwergängig | Schmieren (Zipper-Wax) |
| 2 | Klett haftet schwach, leichter Tuchverschleiß | Klett erneuern, Patch |
| 3 | Reißverschluss defekt, Tasche aufgerissen | Reparatur nötig |
| 4 | Latte drückt durch Tuch | Sofortige Reparatur |

---

### F-16_08-09: Kopfbrett- und Schothorn-Ausriss

**Bezeichnung:** Strukturversagen an den hochbelasteten Ecken des Segels

**Beschreibung:**
Die drei Ecken des Segels (Kopf, Schothorn, Hals) tragen die höchsten
punktuellen Lasten. Versagen tritt auf, wenn die Verstärkung nicht mehr
ausreicht oder Material ermüdet.

**Visuelle Merkmale:**
- Risse oder Verformung um Kauschen und Ösen
- Nieten locker oder ausgebrochen
- Verstärkungslagen ablösend
- Weblines (interne Verstärkungsbänder) gerissen
- Metallteile verbogen

**Typische Lokalisierung:**
- Kopfbrett: Bereich der Fallbefestigung
- Schothorn: Bereich der Schotbefestigung und Ausholer
- Hals: Bereich der Lümmelbeschlag-Befestigung

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Leichte Risse in äußerer Lage | Nachnähen |
| 2 | Nieten locker, Kausch elongiert | Segelmacher |
| 3 | Verstärkung teilweise gerissen | Professionelle Reparatur |
| 4 | Strukturelles Versagen | Sofortige Reparatur, Segel nicht verwenden |

**Empfohlene Maßnahmen:**
- IMMER zum Segelmacher (sicherheitsrelevant!)
- Temporäre Notmaßnahme: Dyneema-Leine durch die Öse als zusätzliche Sicherung

---

### F-16_08-10: Vorliek-Lümmeltau-Trennung

**Bezeichnung:** Ablösung des Vorliek-Liektaus oder Lümmeltaus vom Segeltuch

**Beschreibung:**
Das Vorliek-Liektau (oder Lümmeltau) verbindet das Segel mit dem Vorstag
(bei Fock/Genua) oder dem Mast (bei Großsegel). Eine Trennung macht das
Segel funktionsunfähig.

**Visuelle Merkmale:**
- Naht zwischen Liektau und Segeltuch öffnet sich
- Liektau steht ab oder wellt sich
- Tuch hat sich vom Liektau gelöst (sichtbarer Spalt)
- Bei Rollsegeln: Segel lässt sich nicht mehr einrollen (Tau springt aus Nut)

**Schweregrade:**
| Grad | Trennungslänge | Maßnahme |
|------|---------------|----------|
| 1 | <100 mm | Nachnähen möglich (Hand) |
| 2 | 100–500 mm | Segelmacher empfohlen |
| 3 | >500 mm | Segelmacher zwingend |
| 4 | Komplett | Liektau-Erneuerung |

---

### F-16_08-11: Reißverschluss-Versagen

**Bezeichnung:** Funktionsversagen von Reißverschlüssen an Segel-Komponenten

**Beschreibung:**
Reißverschlüsse kommen an Lattentaschen, Segelsäcken, Lazy Bags und
gelegentlich an Rollsegel-Abdeckungen vor. Sie sind anfällig für
Salzkorrosion und mechanischen Verschleiß.

**Visuelle Merkmale:**
- Reißverschluss lässt sich nicht schließen/öffnen
- Zähne stehen einzeln ab oder fehlen
- Schieber läuft nicht mehr
- Korrosion an Metallzähnen
- Stoff um den Reißverschluss ausgefranst

**Ursachen:**
- Salzkorrosion (bei nicht-marinen Reißverschlüssen)
- Mechanischer Verschleiß
- UV-Degradation des umgebenden Tuchs
- Sandkörner in den Zähnen

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Schwergängig | Reinigen, schmieren (Zipper-Wax) |
| 2 | Einzelne Zähne defekt | Reparatur möglich |
| 3 | Schieber defekt | Schieber ersetzen |
| 4 | Reißverschluss komplett defekt | Reißverschluss erneuern |

**Prävention:**
- Nur marine Reißverschlüsse verwenden (YKK Aquaguard, Lenzip)
- Regelmäßig mit Süßwasser spülen
- Zipper-Wax oder Bienenwachs auftragen (alle 2–4 Wochen)
- Sand und Schmutz entfernen vor dem Schließen

---

### F-16_08-12: Salzkristallisation

**Bezeichnung:** Salzablagerung und Kristallisation in Segeltuch und Nähten

**Beschreibung:**
Salz dringt in das Gewebe ein und kristallisiert beim Trocknen. Die Kristalle
sind abrasiv und wirken wie Schleifpapier auf die Fasern. Bei Laminatsegeln
können Salzkristalle die Delamination beschleunigen.

**Visuelle Merkmale:**
- Weißliche Ablagerungen auf der Segel-Oberfläche
- Segel fühlt sich steif und „knusprig" an
- An Nähten: weiße Kristallränder
- Bei Laminat: milchige Trübung zwischen den Schichten

**Typische Lokalisierung:**
- Gesamte Segelfläche bei Salzwassereinsatz
- Konzentration an Nähten (Salz dringt durch Nadellöcher)
- Unterliek-Bereich (Spritzwasser)
- Lattentaschen (Salz staut sich)

**Schweregrade:**
| Grad | Beschreibung | Maßnahme |
|------|-------------|----------|
| 1 | Oberflächliche Ablagerung | Süßwasserspülung |
| 2 | Tuch verhärtet, Salz in Nähten | Gründliche Wäsche |
| 3 | Salz zwischen Laminatschichten | Professionelle Reinigung |
| 4 | Delamination durch Salz | Segelmacher |

**Prävention:**
- Nach JEDER Salzwasserfahrt: Segel mit Süßwasser abspülen
- Mindestens monatlich gründliche Spülung der Nähte
- Bei Langfahrt: Segel gelegentlich im Süßwasser-Regen setzen
- Laminatsegel: besonders konsequent spülen

---

## 10. Troubleshooting

### 10.1 Entscheidungsbaum: Riss-Reparatur

```
RISS IM SEGEL ENTDECKT
│
├── Risslänge < 50 mm?
│   ├── JA → Riss im tragenden Bereich (Kopf, Schothorn, Hals, Vorliek)?
│   │   ├── JA → Professionelle Reparatur empfohlen
│   │   │         Temporär: Tear-Aid beidseitig + segeln mit Vorsicht
│   │   └── NEIN → DIY: Klebepatches beidseitig
│   │               Material: Insignia Tape oder Tear-Aid Type A
│   │               Kosten: 5–20 EUR
│   │               Haltbarkeit: 1–3 Saisons
│   │
│   └── NEIN → Risslänge 50–200 mm?
│       ├── JA → Material Laminat oder Membran?
│       │   ├── JA → Professionelle Reparatur (Nachkaschierung nötig)
│       │   │         Kosten: 150–400 EUR
│       │   └── NEIN (Dacron/Nylon) → DIY möglich mit Erfahrung
│       │         Genähter Patch beidseitig
│       │         Material: Dacron-Patch + V-92 Garn
│       │         Kosten: 15–40 EUR
│       │         Haltbarkeit: 3–8 Saisons (wenn gut ausgeführt)
│       │
│       └── NEIN → Risslänge > 200 mm
│           ├── Riss entlang einer Naht?
│           │   ├── JA → Naht komplett erneuern (maschinell empfohlen)
│           │   │         Segelmacher: 150–600 EUR
│           │   └── NEIN → Riss quer durch das Tuch?
│           │       ├── Tuch noch fest (Zugtest)?
│           │       │   ├── JA → Professioneller Patch mit Verstärkung
│           │       │   │         Kosten: 200–800 EUR
│           │       │   └── NEIN → Tuch materialmüde → Segel am Ende
│           │       │             Reparatur unwirtschaftlich wenn >30 % betroffen
│           │       │             → Neusegel planen
│           │       └── Riss strahlenförmig von Öse/Kausch?
│           │           → Strukturelles Versagen → Segelmacher sofort
│           └── Mehrere Risse vorhanden?
│               ├── JA → Materialermüdung wahrscheinlich
│               │         Professionelle Inspektion → Restlebensdauer bestimmen
│               └── NEIN → Einzelriss durch Ereignis (Salingen, Haken etc.)
│                         → Ursache beheben + Patch-Reparatur
```

### 10.2 Entscheidungsbaum: Schimmelbehandlung

```
SCHIMMEL/STOCKFLECKEN ENTDECKT
│
├── Schimmel oberflächlich (wischt sich ab)?
│   ├── JA → Befallsfläche < 5 %?
│   │   ├── JA → DIY: Sofortreinigung
│   │   │   1. In der Sonne ausbreiten (UV tötet Sporen)
│   │   │   2. Trocken abbürsten (weiche Bürste)
│   │   │   3. Star brite Mildew Remover aufsprühen
│   │   │   4. 15 Min. einwirken lassen
│   │   │   5. Mit Wasser und Schwamm abwaschen
│   │   │   6. Komplett trocknen lassen
│   │   │   → Kosten: 15–20 EUR
│   │   │
│   │   └── NEIN → Befallsfläche 5–20 %?
│   │       ├── JA → Einweich-Methode
│   │       │   1. Segel in Badewanne/Plane mit Reinigungslösung einweichen
│   │       │   2. 10 l Wasser + 100 ml Biovex + 50 ml Essig
│   │       │   3. 30–60 Min. einweichen
│   │       │   4. Mit Schwamm behandeln
│   │       │   5. Gründlich nachspülen
│   │       │   → Kosten: 25–40 EUR
│   │       │
│   │       └── NEIN (>20 %) → Professionelle Reinigung
│   │           → Kosten: 150–400 EUR
│   │
│   └── NEIN → Schimmel sitzt tief (lässt sich nicht abwischen)?
│       ├── Tuch noch fest (Zugtest)?
│       │   ├── JA → Professionelle enzymatische Behandlung
│       │   │         Ozon-Behandlung oder industrielle Enzyme
│       │   │         Kosten: 200–500 EUR
│       │   │         Restflecken bleiben wahrscheinlich
│       │   │
│       │   └── NEIN → Tuch geschwächt
│       │             Festigkeitstest beim Segelmacher
│       │             Wenn >20 % Festigkeitsverlust → Segel ersetzen
│       │
│       └── Befall an tragenden Stellen (Kopf, Schothorn, Nähte)?
│           → Professionelle Inspektion zwingend
│           → Festigkeitsprüfung erforderlich
│
└── PRÄVENTION für die Zukunft:
    1. Segel immer trocken einlagern
    2. Belüftete Segelsäcke
    3. Silikagelpackungen
    4. Regelmäßige Kontrolle (alle 2–4 Wochen in der Lagersaison)
```

### 10.3 Entscheidungsbaum: Nahtauflösung

```
NAHT LÖST SICH AUF
│
├── Ursache: UV-Degradation?
│   (Garn aufgerauht, spröde, nur an UV-exponierten Stellen)
│   ├── JA → Wie viel Prozent der Nahtlänge betroffen?
│   │   ├── < 10 % → Lokales Nachnähen (Hand oder Maschine)
│   │   │             Garn: Tenara PTFE für Dauerhaftigkeit
│   │   │             Kosten: 20–50 EUR (DIY)
│   │   │
│   │   ├── 10–30 % → Betroffene Abschnitte nachnähen
│   │   │              Segelmacher empfohlen
│   │   │              Kosten: 150–400 EUR
│   │   │
│   │   └── > 30 % → Vollständige Nahtrevision
│   │                 Segelmacher zwingend
│   │                 Kosten: 300–1.200 EUR
│   │                 → UV-Schutz verbessern (UV-Streifen/Persenning)
│   │
│   └── NEIN → Ursache: Mechanische Überlastung?
│       (Naht an einer Stelle gerissen, Rest intakt)
│       ├── JA → Belastungspunkt identifizieren
│       │   ├── Kopfbrett/Schothorn/Hals → Segelmacher
│       │   ├── Bahnennäht → Nachnähen mit Verstärkungsstreifen
│       │   └── Lattentasche → Naht erneuern + ggf. Tasche verstärken
│       │
│       └── NEIN → Ursache: Chemischer Abbau?
│           (Kontakt mit Reinigern, Chemikalien, Abgas)
│           ├── JA → Schadstoffe identifizieren und vermeiden
│           │         Betroffene Nähte ersetzen
│           │         Kontaminiertes Garn komplett entfernen
│           └── NEIN → Ursache unklar
│                     → Professionelle Inspektion empfohlen
│                     → Garnproben zur Analyse einschicken
```

### 10.4 Entscheidungsbaum: Laminat-Blasenbildung

```
BLASEN IM LAMINAT ENTDECKT
│
├── Blasengröße < 5 mm?
│   ├── JA → Einzelne Blasen oder Cluster?
│   │   ├── Einzeln → Beobachten (markieren und Größe dokumentieren)
│   │   │              Wenn stabil: kein Handlungsbedarf
│   │   │              Wenn wachsend: Segelmacher konsultieren
│   │   │
│   │   └── Cluster → Beginende Delamination wahrscheinlich
│   │                  Segelmacher konsultieren
│   │                  Möglicherweise Nachkaschierung nötig
│   │
│   └── NEIN → Blasen > 5 mm?
│       ├── Blasen < 20 mm?
│       │   ├── JA → Lokalisierung?
│       │   │   ├── Entlang Naht → Feuchtigkeit durch Nadellöcher
│       │   │   │                   Segelmacher: lokales Nachkleben
│       │   │   │                   Kosten: 80–200 EUR
│       │   │   │
│       │   │   ├── An Knickfalte → Lagerungsschaden
│       │   │   │                    Segelmacher: Nachkaschierung
│       │   │   │                    Kosten: 100–300 EUR
│       │   │   │                    → Künftig: ROLLEN statt falten!
│       │   │   │
│       │   │   └── Fläche (ohne Bezug) → Klebstoff-Degradation
│       │   │                              Alter des Segels prüfen
│       │   │                              → Restlebensdauer bestimmen lassen
│       │   │
│       │   └── NEIN → Blasen > 20 mm oder zusammenfließend?
│       │       → Fortgeschrittene Delamination
│       │       → Flächenanteil bestimmen:
│       │         ├── < 15 % → Reparatur möglicherweise wirtschaftlich
│       │         │             Segelmacher: Kostenvoranschlag einholen
│       │         └── > 15 % → Wirtschaftlicher Totalschaden wahrscheinlich
│       │                       Neusegel planen
│       │
│       └── NEIN → Ganze Schicht abgelöst?
│           → Segel nicht mehr einsetzbar
│           → Sofort aus dem Betrieb nehmen
│           → Segelmacher konsultieren (für Befund-Dokumentation)
│
└── PRÄVENTION:
    1. Laminatsegel IMMER rollen
    2. Süßwasserspülung nach jeder Salzwasserfahrt
    3. Trocken lagern (< 55 % Luftfeuchtigkeit)
    4. Nicht öfter als nötig bergen/setzen
```

### 10.5 Entscheidungsbaum: UV-Streifen-Erneuerung

```
UV-STREIFEN ZEIGT ALTERUNGSANZEICHEN
│
├── Nur Farbverblassung?
│   ├── JA → UV-Blockierung noch ausreichend?
│   │   ├── Farbe noch erkennbar (>50 % Sättigung) → Monitoring
│   │   │   Nächste Inspektion in 6 Monaten
│   │   │   303 Aerospace Protectant auftragen
│   │   │
│   │   └── Stark verblasst (<50 % Sättigung) → Erneuerung planen
│   │       Innerhalb der nächsten 1–2 Saisons
│   │
│   └── NEIN → Verhärtung/Versprödung?
│       ├── JA → Reißtest: Stoff an der Kante biegen
│       │   ├── Bricht → Sofortige Erneuerung
│       │   └── Federt zurück → Erneuerung innerhalb 1 Saison
│       │
│       └── NEIN → Nahtablösung?
│           ├── Ablösung < 20 % der Gesamtlänge → Nachnnähen
│           │   DIY möglich (Nähmaschine mit Walking-Foot)
│           │   Kosten: 20–50 EUR (Garn + Zeit)
│           │
│           ├── Ablösung 20–50 % → UV-Streifen erneuern
│           │   Segelmacher empfohlen
│           │   Kosten: 300–800 EUR
│           │
│           └── Ablösung > 50 % → UV-Streifen komplett ersetzen
│               Segelmacher: neuer Sunbrella-Streifen
│               Kosten: 300–800 EUR (wie oben)
│               → Garn: Tenara PTFE für längere Haltbarkeit empfohlen
│
├── UV-STREIFEN DIY-ERNEUERUNG:
│   Nähmaschine: Sailrite Ultrafeed LSZ-1 oder vergleichbar
│   Material: Sunbrella Acryl (Navy), 25–35 EUR/m
│   Garn: Tenara PTFE, 45 EUR/Spule
│   Nahttyp: Dreifach (Zickzack + 2× gerade)
│   Zeitaufwand: 4–8 Stunden
│   Gesamtkosten Material: 80–150 EUR
│
└── UV-STREIFEN PROFESSIONELL:
    Bearbeitungszeit: 2–5 Werktage
    Kosten: 300–800 EUR (Material + Arbeit)
    Im Herbst/Winter günstiger und schneller
```

---

## 11. Bord-Reparaturkit

### 11.1 Empfohlenes Bordkit

Jede Yacht sollte ein Segel-Reparaturkit an Bord haben. Die folgende
Zusammenstellung deckt die häufigsten Notfälle ab.

#### Basis-Kit (Küstenfahrt)

| Artikel | Produkt-Empfehlung | Menge | Preis (ca.) |
|---------|-------------------|-------|-------------|
| Segelmacher-Palm | William Smith & Son Traditional Palm | 1 | 45 EUR |
| Segelnadeln | William Smith Assorted Sail Needles Nr. 14–18 | 1 Set (10 Stk.) | 8 EUR |
| Nähgarn V-92 | A&E Strafil V-92, weiß | 1 Spule (50 m) | 8 EUR |
| Bienenwachs | Block | 1 | 3 EUR |
| Klebeband Segeltuch | Insignia Sailcloth Tape 75 mm | 1 Rolle (7,5 m) | 20 EUR |
| Universal-Reparaturband | Tear-Aid Type A, Reparaturset | 1 Set | 25 EUR |
| Heißschneider | Dremel Versatip (Butangas) | 1 | 45 EUR |
| Segelschere | Rostfreie Segeltuchschere | 1 | 20 EUR |
| Maßband + Markierstift | Wasserlöslicher Markierstift | 1 Set | 8 EUR |
| Schäkel-Sortiment | Edelstahl 316L, verschiedene Größen | 1 Set | 15 EUR |
| Kabelbinder | UV-stabilisiert, verschiedene Größen | 50 Stk. | 5 EUR |
| Isolierband | Rigging-Tape (selbstverschweißend) | 1 Rolle | 8 EUR |
| **Gesamtkosten** | | | **ca. 210 EUR** |

#### Erweitertes Kit (Langfahrt / Offshore)

Zusätzlich zum Basis-Kit:

| Artikel | Produkt-Empfehlung | Menge | Preis (ca.) |
|---------|-------------------|-------|-------------|
| Nähgarn Tenara PTFE | Gore Tenara HTR, weiß | 1 Spule (60 m) | 30 EUR |
| Nähgarn V-138 | A&E Strafil V-138 | 1 Spule (50 m) | 15 EUR |
| Dacron-Segeltuch | Resttuch vom Segelmacher, 0,5 m² | 2 Stk. | 15 EUR |
| Spinnaker-Nylon | Ripstop-Nylon 40 g/m², 0,25 m² | 2 Stk. | 8 EUR |
| Segelkleber | Bostik 1400 TF | 1 Tube | 12 EUR |
| Kauschen-Sortiment | Edelstahl 316L, 8–14 mm | 1 Set | 12 EUR |
| Webbing (Gurtband) | Dacron-Gurtband 25 mm | 3 m | 5 EUR |
| Reißverschluss-Reparatur | YKK Marine Schieber + Zähne-Reparaturset | 1 Set | 15 EUR |
| Pricker / Fid | Segelmacher-Ahle | 1 | 10 EUR |
| Nadel-Ahle (Sewing Awl) | Speedy Stitcher | 1 | 25 EUR |
| Dyneema-Leine | 3 mm, 10 m (für Notbefestigungen) | 1 | 12 EUR |
| 303 Aerospace Protectant | Sprühflasche | 1 (473 ml) | 18 EUR |
| Star brite Sail Cleaner | Konzentrat | 1 (500 ml) | 15 EUR |
| Zipper-Wax | Reißverschluss-Gleitmittel | 1 | 5 EUR |
| **Gesamtkosten Erweiterung** | | | **ca. 197 EUR** |
| **Gesamtkosten Kit komplett** | | | **ca. 407 EUR** |

### 11.2 Sailrite Segel-Reparaturkit

Sailrite bietet ein vorkonfektioniertes Reparaturset an:

**Sailrite Sail Repair Kit:**
- Inhalt: Segelmacher-Palm, Nadeln (5 Stk.), V-92 Garn (30 m), Bienenwachs,
  Insignia Tape (diverse Breiten), Anleitung
- Preis: ca. 65 EUR
- Bezugsquelle: Sailrite.com (Direktimport) oder europäische Fachhändler
- Bewertung: Guter Einstieg, aber für Langfahrt zu begrenzt

**Sailrite Deluxe Sail Repair Kit:**
- Zusätzlich: Heißschneider, Segelschere, Tenara-Garn, Dacron-Patches
- Preis: ca. 140 EUR
- Bewertung: Umfassender, gut für Küsten- und moderate Offshore-Fahrten

### 11.3 Notfall-Reparatur auf See

**Szenario: Riss im Großsegel während des Segelns**

1. **Sofort**: Segel bergen oder reffen, um weitere Schäden zu verhindern.
2. **Bewerten**: Risslänge und -position bestimmen.
3. **Stabilisieren**: Rissenden mit Heißschneider versiegeln (Stoppbrennung).
4. **Patchen**: Tear-Aid oder Insignia Tape beidseitig anbringen.
5. **Verstärken**: Bei tragenden Bereichen zusätzlich mit V-92 durchnähen.
6. **Test**: Segel unter reduzierter Last setzen.
7. **Monitoring**: Regelmäßig kontrollieren, ob Reparatur hält.

**Szenario: Kopfbrett-Befestigung locker**

1. **Sofort**: Segel bergen.
2. **Bewerten**: Ist das Kopfbrett noch sicher befestigt?
3. **Notfix**: Dyneema-Leine (3 mm) durch die Kopfbrett-Öse fädeln
   und als Backup-Befestigung zum Fall führen.
4. **Weiterfahrt**: Mit reduzierter Segelbelastung.
5. **An Land**: Professionelle Reparatur.

**Szenario: Vorliek-Lümmeltau gelöst (Rollsegel)**

1. **Sofort**: Segel bergen (manuell ausrollen und auf Deck ziehen).
2. **Notfix**: Lümmeltau mit Kabelbindern provisorisch am Segel befestigen.
   Alternativ: Durch die Nadellöcher mit V-138 Garn nachnähen.
3. **Segeln**: Nur unter moderaten Bedingungen möglich.
4. **An Land**: Segelmacher — Lümmeltau professionell erneuern.

---

## 12. Lebensdauer-Management

### 12.1 Typische Segel-Lebensdauern

| Segeltyp | Material | Fahrteinsatz | Regatta-Einsatz | Faktoren |
|----------|----------|-------------|-----------------|----------|
| Großsegel | Dacron | 8–12 Jahre | 4–6 Jahre | UV, Form, Nähte |
| Großsegel | Laminat | 5–8 Jahre | 3–5 Jahre | Delamination, Form |
| Großsegel | 3Di/Membran | 8–15 Jahre | 5–8 Jahre | Pflege entscheidend |
| Genua/Fock | Dacron | 6–10 Jahre | 3–5 Jahre | Schamfil, UV |
| Genua/Fock | Laminat | 4–7 Jahre | 2–4 Jahre | Delamination, Schamfil |
| Spinnaker | Nylon (0,75 oz) | 5–8 Jahre | 2–4 Jahre | Risse, UV |
| Gennaker | Nylon/Laminat | 4–7 Jahre | 2–3 Jahre | Risse, Form |
| Code 0 | Laminat | 5–8 Jahre | 3–5 Jahre | Schamfil, Form |
| Sturmfock | Dacron (schwer) | 15–20 Jahre | 10–15 Jahre | Selten im Einsatz |
| Trysegel | Dacron (schwer) | 15–20 Jahre | 10–15 Jahre | Selten im Einsatz |

**Lebensdauer-Verlängerung durch Pflege:**
Korrekte Wartung kann die Lebensdauer um 30–50 % verlängern.
Beispiel: Dacron-Großsegel:
- Ohne Pflege: 5–7 Jahre
- Mit Basis-Pflege: 8–10 Jahre
- Mit optimaler Pflege: 10–12 Jahre

### 12.2 Degradationsindikatoren

**Formverlust:**
- Dacron verliert mit der Zeit seine Form (Dehnung, Bauchverlagerung).
- Ein neues Dacron-Segel hat den Bauch bei ca. 40–45 % des Profiltiefenpunkts.
- Nach 5 Jahren: Bauch wandert auf 50–55 %.
- Nach 8 Jahren: Bauch bei 55–65 %, Twist im Achterliek unkontrolliert.
- Akzeptabler Leistungsverlust: bis 15 % (Fahrtenbereich).
- Regatta: Austausch bei >8 % Leistungsverlust.

**Tuch-Festigkeitsverlust:**
- Neuzustand: 100 % (Referenz).
- Akzeptabel (Fahrt): >60 % Restfestigkeit.
- Austausch empfohlen: <50 % Restfestigkeit.
- Sicherheitskritisch: <30 % Restfestigkeit → nicht mehr verwenden!

### 12.3 Restlebensdauer-Kalkulation

**Einfache Schätzformel (Dacron-Fahrtensegel):**
```
Restlebensdauer (Jahre) = Basis-Lebensdauer × Pflegefaktor × Revierfaktor
                          − Alter (Jahre)
```

Pflegefaktoren:
- Optimale Pflege: 1,3
- Standard-Pflege: 1,0
- Minimale Pflege: 0,7
- Keine Pflege: 0,5

Revierfaktoren:
- Ostsee / Nordeuropa: 1,0
- Atlantik: 0,85
- Mittelmeer: 0,75
- Tropen / Karibik: 0,60

**Beispiel:**
Dacron-Großsegel, Basis-Lebensdauer 10 Jahre, Standard-Pflege, Mittelmeer, 4 Jahre alt.
```
Restlebensdauer = 10 × 1,0 × 0,75 − 4 = 3,5 Jahre
```

### 12.4 Wirtschaftlichkeitsberechnung Reparatur vs. Neusegel

**Faustregel:**
- Reparaturkosten < 30 % des Neusegelpreises UND Restlebensdauer > 3 Jahre → Reparieren.
- Reparaturkosten 30–50 % des Neusegelpreises → Nur reparieren, wenn Restlebensdauer > 5 Jahre.
- Reparaturkosten > 50 % des Neusegelpreises → Neusegel bestellen.

**Beispiel-Kalkulation:**
```
Dacron-Großsegel (12 m Yacht)
Neupreis: 5.000 EUR
Aktuelle Reparatur: 1.200 EUR (Nahtrevision + UV-Streifen)
Alter: 6 Jahre
Geschätzte Restlebensdauer nach Reparatur: 4 Jahre
Kosten pro Jahr mit Reparatur: (6.000 bisherige + 1.200) / 10 = 720 EUR/Jahr
Kosten pro Jahr mit Neusegel: 5.000 / 10 = 500 EUR/Jahr

→ Neusegel ist langfristig günstiger, ABER: Reparatur hält noch 4 Jahre.
→ Empfehlung: Reparieren und Neusegel in 3–4 Jahren planen.
```

---

## 13. FAQ

### Allgemeine Fragen

**F1: Wie oft sollte ich meine Segel waschen?**
A: Mindestens einmal pro Saison gründlich reinigen. Bei Salzwassereinsatz
zusätzlich monatlich mit Süßwasser abspülen. Die Nähte besonders beachten.

**F2: Kann ich mein Segel in der Waschmaschine waschen?**
A: Dacron-Segel und Spinnaker können in einer ausreichend großen Waschmaschine
(Frontlader) bei 30 °C im Feinwaschprogramm gewaschen werden. KEIN Schleudern
über 400 U/min. Laminat- und Membransegel NIEMALS maschinell waschen.

**F3: Mein Segel hat Schimmelflecken. Was tun?**
A: Leichten Schimmel in der Sonne trocknen und abbürsten. Danach mit
Star brite Mildew Stain Remover behandeln. Bei schwerem Befall professionelle
Reinigung nötig. Immer die Ursache beheben (Feuchtigkeit beim Lagern).

**F4: Wie erkenne ich, ob mein Segel noch gut ist?**
A: Professionelle Inspektion beim Segelmacher (80–200 EUR). Selbst-Check:
Nähte prüfen (Zugtest), Tuchfestigkeit fühlen, Form beim Segeln beobachten,
UV-Streifen inspizieren.

**F5: Lohnt sich ein UV-Schutzstreifen?**
A: Absolut ja. Ohne UV-Streifen hält ein Rollvorsegel im Mittelmeer nur
2–4 Jahre. Mit UV-Streifen 8–12 Jahre. Kosten: 200–400 EUR Aufpreis bei
Neusegel, 300–800 EUR Nachrüstung.

**F6: Welche Farbe soll mein UV-Streifen haben?**
A: Dunkelblau (Navy) bietet den besten UV-Schutz und die längste Lebensdauer.
Schwarz ist gleichwertig, absorbiert aber mehr Wärme. Weiß hat den geringsten
UV-Schutz und ist nicht empfohlen.

**F7: Wie lagere ich mein Segel im Winter?**
A: Segel abnehmen, gründlich reinigen, vollständig trocknen (24+ Stunden).
In atmungsaktivem Segelsack lagern, dunkel, trocken (< 60 % Luftfeuchtigkeit),
temperiert (5–25 °C). Silikagelpackungen beilegen.

**F8: Kann ich Laminatsegel falten?**
A: NEIN. Laminatsegel immer rollen. Knickfalten zerstören die Laminatverbindung
und führen zu Delamination. Ausnahme: In-Mast-Rollsegel werden im Mast gerollt.

**F9: Wie lange halten Segellatten?**
A: Dacron-Latten: 5–7 Jahre, GFK-Latten: 8–12 Jahre, Carbon-Latten: 10–15 Jahre.
Regelmäßig auf Bruch und Delamination prüfen. Bei gebrochenem Biegeprofil austauschen.

**F10: Was ist Tenara-Garn und brauche ich das?**
A: Tenara ist PTFE-Nähgarn von Gore. Es ist UV-unempfindlich und chemisch inert.
Ideal für UV-exponierte Nähte (Achterliek, UV-Streifen). Teurer als Polyester
(45 EUR vs. 8 EUR pro Spule), aber die Naht hält 2–3× länger.

### Reinigung und Pflege

**F11: Darf ich einen Hochdruckreiniger verwenden?**
A: NEIN, niemals. Der Wasserstrahl zerstört Beschichtungen, treibt Schmutz in
das Gewebe und kann Laminatschichten trennen. Nur Gartenschlauch mit Brause.

**F12: Welchen Segelreiniger empfehlen Sie?**
A: Für Dacron: Star brite Sail & Canvas Cleaner (gutes Preis-Leistung-Verhältnis).
Für Laminat/Membran: Biovex Sail Cleaner oder Snyder Sail Bath (schonender, pH-neutral).
Für alle: Kein Vollwaschmittel, kein Chlor, keine Lösungsmittel.

**F13: Mein Segel ist steif und „knusprig" nach dem Trocknen. Warum?**
A: Salzkristallisation. Das Segel wurde ohne ausreichende Süßwasserspülung
getrocknet. Lösung: Nochmals gründlich mit Süßwasser einweichen und waschen.

**F14: Kann ich Hausmittel zur Segelreinigung verwenden?**
A: Bedingt. pH-neutrales Spülmittel (5 ml auf 10 l Wasser) für leichte
Verschmutzung. Oxalsäure (1 %) für Rostflecken (nur punktuell, mit Handschuhen).
Essig für Kalkflecken. KEIN Bleichmittel, kein Backofenreiniger.

**F15: Wie behandle ich Blutflecken auf dem Segel?**
A: Nur mit KALTEM Wasser! Salzwasserlösung (2 EL Salz / 500 ml kaltes Wasser)
30 Minuten einweichen. Danach mit Segelreiniger nachwaschen. Hitze fixiert
das Protein dauerhaft.

### Reparatur

**F16: Kann ich Risse im Segel selbst reparieren?**
A: Kleine Risse (< 50 mm) in nicht-tragenden Bereichen: Ja, mit Klebeband
(Insignia Tape oder Tear-Aid). Mittlere Risse: Mit Erfahrung und genähtem
Patch möglich. Große Risse und alle Schäden an Kopf/Schothorn/Hals: Segelmacher.

**F17: Was kostet eine professionelle Segelreparatur?**
A: Stark abhängig von Art und Umfang. Patch-Reparatur: 80–350 EUR.
Nahtrevision: 200–1.200 EUR. UV-Streifen erneuern: 300–800 EUR.
Kopfbrett-Reparatur: 150–500 EUR. Detailliert in Abschnitt 8.2.

**F18: Wann lohnt sich Reparatur, wann Neusegel?**
A: Reparaturkosten < 30 % des Neupreises UND Restlebensdauer > 3 Jahre → Reparieren.
Reparaturkosten > 50 % des Neupreises → Neusegel bestellen. Dazwischen:
Restlebensdauer und Nutzungsintensität berücksichtigen.

**F19: Welche Nähmaschine brauche ich für Segelreparaturen?**
A: Mindestens eine Walking-Foot-Maschine (z. B. Sailrite Ultrafeed LSZ-1,
ca. 850 EUR). Normale Haushaltsmaschinen können kein Segeltuch transportieren.
Für gelegentliche Reparaturen reicht Handnähen mit Palm und Nadel.

**F20: Was ist der Unterschied zwischen Insignia Tape und Tear-Aid?**
A: Insignia Tape ist selbstklebendes Dacron-Segeltuch (opak, robust, langlebig).
Tear-Aid ist ein transparentes, dehnbares Reparaturlaminat (universell, sehr reißfest).
Insignia für Dacron-Segel, Tear-Aid als Universal-Notreparatur.

### Lagerung und UV-Schutz

**F21: Kann ich mein Rollsegel den Winter über aufgerollt lassen?**
A: Möglich, aber nicht ideal. Besser: Segel abnehmen, reinigen, trocken lagern.
Wenn es aufgerollt bleibt: UV-Streifen muss intakt sein, Rollanlage konservieren,
regelmäßig kontrollieren (monatlich). Restfeuchtigkeit kann zu Schimmel führen.

**F22: Wie funktioniert 303 Aerospace Protectant?**
A: 303 enthält UV-absorbierende Polymere, die sich auf der Oberfläche anordnen
und UV-Strahlung blockieren (bis 96 %). Aufsprühen, verteilen, trocknen lassen.
Alle 4–6 Wochen erneuern. Für UV-Streifen, Persennings und Dacron-Segel geeignet.
NICHT für Laminat.

**F23: Brauche ich eine Segelpersenning, wenn ich einen UV-Streifen habe?**
A: Der UV-Streifen schützt das gerollte Segel. Eine Persenning bietet
zusätzlichen Schutz und schützt auch die Nähte, Beschläge und das Achterliek.
In südlichen Revieren sehr empfohlen, in Nordeuropa ein Plus, aber nicht zwingend.

**F24: Mein Lazy Bag hat Schimmel. Was tun?**
A: Lazy Bag abnehmen und wie Segeltuch reinigen (Star brite Sail Cleaner).
Drainageöffnungen prüfen und ggf. vergrößern. Lazy Bag muss belüftet sein.
Bei schwerem Befall: ersetzen. Lazy Bags aus Sunbrella sind schimmelresistenter.

**F25: Wie schütze ich meinen Spinnaker vor UV?**
A: Spinnaker nur während des Segelns setzen und danach sofort bergen.
Im Segelsack (dunkel) lagern. Nylon verliert bei UV-Exposition schnell an
Festigkeit (15–25 % pro 1.000 Sonnenstunden). Keinen UV-Schutz auftragen,
da dies die Handhabung beeinträchtigt. Bester Schutz = Nicht-Exposition.

### Spezialfragen

**F26: Mein 3Di-Segel hat Mikrorisse in der Oberfläche. Normal?**
A: Leichte Oberflächenrisse in der Taffeta-Schutzschicht können nach einigen
Jahren auftreten und sind zunächst kosmetisch. Wenn sie zunehmen oder sich
vertiefen, North Sails Servicepoint konsultieren. Die Schutzschicht kann
erneuert werden.

**F27: Kann ich meinem Segel eine zweite Reff-Ebene nachrüsten lassen?**
A: Ja, erfahrene Segelmacher können Reff-Ösen, Verstärkungen und Reff-Bänder
nachrüsten. Kosten: 400–1.200 EUR (je nach Segelgröße). Sinnvoll bei Langfahrt
oder Revier-Wechsel in rauere Gewässer.

**F28: Warum rostet mein Edelstahl-Kopfbrett?**
A: Wahrscheinlich ist das Kopfbrett aus Edelstahl 304 statt 316L. In Salzwasser
korrodiert 304 (Crevice Corrosion). Prüfen und durch 316L oder Titan ersetzen.
Auch 316L kann bei dauerhafter Feuchtigkeit in Spalten korrodieren.

**F29: Mein Segel quietscht auf dem Rollstag. Was hilft?**
A: Vorliek-Lümmeltau und Rollstag-Nut mit McLube SailKote (PTFE-Spray)
behandeln. Nicht zu viel auftragen (Überschuss zieht Schmutz an).
Regelmäßig erneuern (alle 2–4 Wochen in der Saison).

**F30: Wie bewahre ich den Resin-Finish meines Dacron-Segels?**
A: Der Resin-Finish (Harzappretierung) verschleißt natürlich durch Segeln,
Regen und Waschen. Nach 3–5 Saisons merklich reduziert. Auffrischen mit
McLube SailKote oder Ronstan Sailguard. Die professionelle Resin-Erneuerung
ist nicht möglich — der Finish wird werksseitig bei der Herstellung aufgebracht.

---

## 14. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Achterliek** | Hintere Kante des Segels (vom Kopf zum Schothorn). |
| **Bahnennaht** | Naht zwischen den horizontalen oder vertikalen Tuchbahnen des Segels. |
| **Batten / Segellatte** | Steife Stäbe (GFK, Carbon, Dacron) in Lattentaschen, die das Achterliek stützen. |
| **Bergeschlauch / Snuffer** | Zylindrischer Beutel zum Bergen von Spinnaker/Gennaker. |
| **Cunningham** | Trimmleine am Vorliek zum Spannen und Positionieren des Segelprofils. |
| **Dacron** | Markenname für Polyester-Gewebe, Standardmaterial für Fahrtensegel. |
| **Delamination** | Trennung der Schichten bei Laminatsegeln. |
| **Dyneema / Spectra** | Ultra-High-Molecular-Weight-Polyethylene (UHMWPE), hochfeste Faser. |
| **Fallen** | Leinen zum Setzen (Hochziehen) der Segel. |
| **Fock** | Kleines Vorsegel, das nicht bis zum Heck reicht. |
| **Gelcoat** | Schützende Harzschicht auf GFK-Oberflächen. |
| **Genua** | Großes Vorsegel, das über den Mast hinaus nach achtern reicht. |
| **GFK / FRP** | Glasfaserverstärkter Kunststoff (Fiberglass Reinforced Plastic). |
| **Großsegel** | Segel am Großmast, zwischen Mast und Baum. |
| **Hals** | Untere Vorderkante des Segels, Befestigungspunkt am Lümmelbeschlag/Baum. |
| **Headboard / Kopfbrett** | Verstärkungsplatte am Segelkopf. |
| **Heißschneider / Hot Knife** | Elektrisches oder gasbetriebenes Schneidwerkzeug, das Synthetikfasern schmilzt. |
| **Kausch** | Metallöse (Edelstahl/Titan) zur Verstärkung von Augen im Segel. |
| **Kevlar / Aramid** | Hochfeste, UV-empfindliche Kunstfaser (DuPont). |
| **Killen** | Unkontrolliertes Flattern des Segels bei fehlendem Winddruck. |
| **Kopf** | Obere Ecke des Segels. |
| **Lazy Bag** | Tuchbeutel auf dem Baum zur Aufnahme des geborgenen Großsegels. |
| **Lazy Jacks** | Leinen vom Mast zum Baum, die das Großsegel beim Bergen führen. |
| **Liek** | Kante eines Segels (Vor-, Achter-, Unterliek). |
| **Liektau / Lümmeltau** | Tau eingenäht in das Vorliek, das in die Mastnut oder Rollanlage eingeführt wird. |
| **Lümmelbeschlag** | Beschlag, der den Baum drehbar am Mast befestigt. |
| **Mylar** | PET-Folie, verwendet als Basis für Laminate. |
| **Nylon (Polyamid)** | Synthetikfaser, hauptsächlich für Spinnaker und Gennaker. |
| **Palm (Segelmacher-Handschuh)** | Lederhandschuh mit Metalldruckplatte zum Durchdrücken der Nadel. |
| **PBO (Zylon)** | Poly-p-phenylen-2,6-benzobisoxazol, hochfest, extrem UV-empfindlich. |
| **Pentex (PEN)** | Polyethylen-Naphthalat-Faser, leistungsstärker als Dacron. |
| **Persenning** | Schutzabdeckung (Canvas) für Segel und Decksausrüstung. |
| **Reffen** | Reduzierung der Segelfläche durch Einholen eines Segelteils. |
| **Resin-Finish** | Harzappretierung auf Dacron-Segeltuch zur Reduzierung der Dehnung. |
| **Rollanlage** | Mechanismus zum Auf- und Abrollen des Vorsegels oder Großsegels. |
| **Rutscher / Slide** | Gleitelement am Vorliek des Großsegels, das in der Mastschiene läuft. |
| **Salingen / Spreader** | Querstreben am Mast, die die Wanten spreizen. |
| **Schamfil** | Abrieb durch Reibung an Gegenständen (Salingen, Wanten etc.). |
| **Schothorn** | Hintere untere Ecke des Segels, Befestigung der Schot. |
| **Spinnaker** | Ballonförmiges Vorwindsegel. |
| **Sunbrella** | Markenname für durchgefärbtes Acrylgewebe (UV-beständig). |
| **Taffeta** | Dünnes Schutzgewebe auf Laminatsegeln. |
| **Tear-Aid** | Markenname für ein universelles Reparaturlaminat. |
| **Technora** | Aramid-Faser (Teijin), UV-beständiger als Kevlar. |
| **Tenara** | PTFE-Nähgarn (Gore), UV-unempfindlich. |
| **3Di** | Membran-Segeltechnologie von North Sails. |
| **Twist** | Verdrehung des Segelprofils vom Unterliek zum Kopf. |
| **UV-Streifen** | Schutzstreifen aus Acrylstoff am Achterliek von Rollsegeln. |
| **V-69 / V-92 / V-138** | Standardbezeichnungen für Polyester-Nähgarn nach Stärke (Tex-Wert). |
| **Webline** | Internes Verstärkungsband im Segel (läuft von Ecke zu Ecke). |

---

## 15. Schnell-Referenz

### 15.1 Wartungsintervalle — Kurzübersicht

```
VOR DEM SEGELN       → Visuelle Kurzinspektion (5 Min.)
MONATLICH (Saison)   → Süßwasserspülung, Naht-Schnellcheck, Schamfilkontrolle
SAISONAL (Herbst)    → Segel abnehmen, reinigen, trocknen, inspizieren, lagern
SAISONAL (Frühjahr)  → Sichtprüfung, Leichtreinigung, Beschläge, Montage
JÄHRLICH             → Professionelle Inspektion, Segelform, Hardware, UV-Streifen
ALLE 3 JAHRE         → Großinspektion, Nahtrevision, Resin-Finish, ggf. Recut
```

### 15.2 Notfall-Reparatur — Kurzanleitung

```
RISS < 50 mm:     Tear-Aid beidseitig aufkleben → weiter segeln
RISS 50–200 mm:   Bergen, Rissenden versiegeln (Heißschneider), Patch beidseitig,
                   von Hand nachnähen, unter reduzierter Last weitersegeln
RISS > 200 mm:    Bergen, provisorisch patchen, nächsten Hafen anlaufen,
                   Segelmacher kontaktieren
NAHT OFFEN:       Von Hand mit V-92 nachnähen (30 mm Überlappung beidseitig)
KOPFBRETT LOCKER:  Bergen, Dyneema-Backup durch Öse, nur bei moderatem Wind segeln
LATTENTASCHE AUF:  Latte sichern (Kabelbinder), Öffnung zukleben oder zunähen
```

### 15.3 Reinigungsmittel — Kurzübersicht

```
Dacron:      Star brite Sail Cleaner (1:10), pH 9,5–10,5
Laminat:     Biovex Sail Cleaner (1:15), pH 7–8
Membran:     Wasser + mildes Spülmittel, Herstellerangabe
Nylon:       Biovex oder Snyder Sail Bath, pH-neutral, kalt
Rostflecken: Oxalsäure 1 % (punktuell, max. 15 Min., Handschuhe!)
Schimmel:    Star brite Mildew Remover oder Biovex + Essig
Ölflecken:   Talkum → Star brite unverdünnt → waschen
```

### 15.4 Kosten-Richtwerte (10–13 m Yacht)

```
Segel-Inspektion (Segelmacher):      80–150 EUR
Nahtrevision (komplett):              350–700 EUR
UV-Streifen erneuern:                 300–550 EUR
Patch-Reparatur (mittel):             100–250 EUR
Kopfbrett-Reparatur:                  150–350 EUR
Professionelle Wäsche:                150–300 EUR
Bord-Reparaturkit (Basis):            ca. 210 EUR
Bord-Reparaturkit (Langfahrt):        ca. 410 EUR
Neues Dacron-Großsegel:               3.500–6.000 EUR
Neues Laminat-Großsegel:              5.500–10.000 EUR
```

---

## 16. ANHANG A–H: Fallstudien

### ANHANG A: Bavaria 37 — UV-Fadendegradation am Rollvorsegel

**Yacht:** Bavaria 37 Cruiser (2018), Stationierung: Kroatien (Dalmatien)
**Segel:** Genua (Dacron 160 g/m²), Elvström Sails, Baujahr 2018
**Problem:** Nähte am Achterliek lösen sich nach 5 Saisons

**Befund:**
- UV-Streifen (Sunbrella Pacific Blue) in gutem Zustand (erst 5 Jahre)
- ABER: Nähgarn V-69 Polyester ohne UV-Stabilisatoren verarbeitet
- Achterliek-Nähte in den oberen 40 % → Stadium 3 UV-Degradation
- Bahnennähte im unteren Bereich → Stadium 1–2
- Schothorn-Verstärkung → intakt

**Analyse:**
Der UV-Streifen schützt das Tuch, aber die Nähte am UV-Streifen selbst
waren mit Standard-Polyester V-69 genäht. Die Nadeldurchstiche durch den
UV-Streifen bilden UV-Eintrittspunkte. In Dalmatien (UV-Index 9–10)
akkumulieren die Nähte ca. 600–800 UV-Stunden pro Saison direkt.

**Maßnahmen:**
1. Achterliek-Nähte komplett mit Tenara PTFE nachnähen
2. UV-Streifen-Nähte ebenfalls mit Tenara erneuern
3. 303 Aerospace Protectant auf UV-Streifen auftragen

**Kosten:** 680 EUR (Segelmacher Split)
**Ergebnis:** Nähte nach 3 weiteren Saisons → Stadium 0 (Tenara zeigt keinen UV-Abbau)

**Lehre:** In südlichen Revieren: IMMER Tenara PTFE für UV-exponierte Nähte.
Aufpreis bei Neubestellung: ca. 100–200 EUR. Spart 680 EUR Reparatur nach 5 Jahren.

---

### ANHANG B: Hallberg-Rassy 40 — Delamination am Großsegel

**Yacht:** Hallberg-Rassy 40 MkII (2016), Stationierung: Göteborg, Schweden
**Segel:** Großsegel (Hydranet-Laminat), Elvström Sails, Baujahr 2019
**Problem:** Blasenbildung im Achterliek-Bereich nach 4 Saisons

**Befund:**
- Delamination auf ca. 8 % der Segelfläche (oberes Achterliek)
- Blasen 5–15 mm Durchmesser, entlang von Nahtlinien
- Kein Knickschaden (Segel wird korrekt in Lazy Bag gerollt)
- Ursache: Salzwasser dringt durch Nadellöcher der Bahnennähte

**Analyse:**
Obwohl das Segel korrekt gerollt und gelagert wurde, führte die unzureichende
Süßwasserspülung (nur 2–3× pro Saison statt nach jeder Salzwasserfahrt) zur
Salzakkumulation in den Nahtlöchern. Die Salzkristalle erzeugten osmotischen
Druck zwischen den Laminatschichten.

**Maßnahmen:**
1. Professionelle Nachkaschierung (Heißpresse) der betroffenen Bereiche
2. Belehrung über Süßwasserspülung nach jeder Fahrt
3. Jährliche Lichttisch-Inspektion angesetzt

**Kosten:** 1.450 EUR (Elvström Service-Center Göteborg)
**Ergebnis:** Delamination gestoppt, nach 2 weiteren Saisons keine neuen Blasen

**Lehre:** Auch in der Ostsee: Laminatsegel nach JEDER Fahrt mit Süßwasser spülen.
Besonders die Nähte gründlich durchspülen. 5 Minuten Aufwand vermeiden 1.450 EUR.

---

### ANHANG C: Jeanneau Sun Odyssey 440 — Schimmelbefall

**Yacht:** Jeanneau Sun Odyssey 440 (2020), Stationierung: La Rochelle, Frankreich
**Segel:** Großsegel (Dacron) + Genua (Dacron), Incidence Sails, Baujahr 2020
**Problem:** Massiver Schimmelbefall nach dem ersten Winter

**Befund:**
- Beide Segel: 15–25 % der Fläche mit Schimmel/Stockflecken
- Ursache: Segel wurden im Herbst 2020 nass im Lazy Bag belassen (COVID-Lockdown)
- 4 Monate ohne Kontrolle
- Tuch-Festigkeit: 90 % erhalten (Schimmel noch nicht tief eingedrungen)

**Maßnahmen:**
1. Segel abnehmen und auf dem Steg in der Sonne trocknen
2. Professionelle Reinigung (enzymatisch, Segelmacher La Rochelle)
3. Nachbehandlung mit Star brite NosGUARD SG
4. Neue Lazy Bags mit verbesserter Drainage

**Kosten:** 520 EUR (Reinigung beider Segel) + 180 EUR (NosGUARD + Silikagelpackungen)
**Ergebnis:** 90 % der Flecken entfernt, Rest kosmetisch. Kein Festigkeitsverlust.

**Lehre:** NIE Segel feucht überwintern. Auch bei erzwungener Abwesenheit:
jemanden beauftragen, die Segel zu trocknen und zu lagern.

---

### ANHANG D: Contest 42CS — Salingen-Schamfilschaden

**Yacht:** Contest 42CS (2015), Langfahrt Atlantik/Karibik
**Segel:** Genua 135 % (Dacron), Doyle Sails, Baujahr 2015
**Problem:** Tuch an Salingen-Position nach 2 Atlantiküberquerungen durchgescheuert

**Befund:**
- Durchscheuerstelle 80 × 40 mm auf Salingenhöhe (Backbordseite)
- Steuerbordseite: starke Aufrauhung, Durchscheuern in 1–2 Saisons
- Salingen nicht gerundet (scharfe Kanten)
- Kein Schamfilschutz am Segel oder an den Salingen

**Maßnahmen:**
1. Professionelle Patch-Reparatur: Doppelseitiger Dacron-Patch mit
   zusätzlicher Dyneema-Chafe-Auflage
2. Salingenenden abrunden und polieren
3. Spreader Boots anbringen (Wichard, 35 EUR/Paar)
4. Steuerbordseite vorsorglich mit Chafe-Patch verstärken

**Kosten:** 380 EUR (Reparatur) + 35 EUR (Spreader Boots)
**Ergebnis:** Genua seit 3 weiteren Saisons + 15.000 sm ohne weitere Schamfilprobleme

**Lehre:** Vor Langfahrt: Salingen abrunden, Spreader Boots anbringen,
Chafe Patches auf dem Segel anbringen. Kosten: ca. 100 EUR präventiv.

---

### ANHANG E: Beneteau First 36.7 — Spinnaker-Riss bei Regatta

**Yacht:** Beneteau First 36.7, Regatta-Einsatz, Kieler Woche
**Segel:** Spinnaker (Nylon 0,75 oz), North Sails, Baujahr 2022
**Problem:** 1,2 m langer L-förmiger Riss bei Kollaps und Füllung

**Befund:**
- Riss im oberen Drittel, beginnt an einer Bahnennaht
- Rissrichtung: quer zur Bahnennaht, dann parallel
- Tuch insgesamt noch in gutem Zustand
- Ursache: Spinnaker kollabierte und füllte sich schlagartig

**Maßnahmen (Notfall an Bord):**
1. Spinnaker sofort geborgen
2. Rissenden mit Heißschneider versiegelt
3. Tear-Aid Type A beidseitig aufgebracht
4. Spinnaker in der gleichen Regatta wiederverwendet (nächster Lauf)

**Maßnahmen (nach Regatta):**
1. Segelmacher: Tear-Aid entfernt
2. Genähter Patch aus originalem Nylon-Tuch beidseitig
3. Dreifach-Zickzack-Naht mit V-92

**Kosten:** 280 EUR (Segelmacher-Reparatur)
**Ergebnis:** Spinnaker hält seit 2 weiteren Saisons (Regattaeinsatz)

**Lehre:** Tear-Aid ist das beste Notfall-Reparaturmaterial für Spinnaker. Ein
Reparaturset gehört in jede Regatta-Tasche. Permanente Reparatur durch Segelmacher.

---

### ANHANG F: Oyster 56 — Kopfbrett-Ausriss beim Reffen

**Yacht:** Oyster 56 (2014), Blauwasser-Langfahrt
**Segel:** Großsegel (Dacron 280 g/m²), UK Sailmakers, Baujahr 2017
**Problem:** Kopfbrett-Befestigung teilweise ausgerissen bei Sturm-Reff

**Befund:**
- 2 von 4 Nieten am Kopfbrett ausgebrochen
- Tuchriss 60 mm von der Nieten-Position ausgehend
- Weblines intakt
- Ursache: Segel im Sturm (45 kn) schnell gerefft → Schlagartige Belastung

**Maßnahmen (Notfall auf See):**
1. Segel komplett geborgen
2. Dyneema-Leine (4 mm) als Backup durch die Kopfbrett-Öse geführt
3. Mit reduziertem Großsegel (3. Reff) weitergesegelt

**Maßnahmen (im Hafen):**
1. Segelmacher (Las Palmas): Kopfbrett komplett erneuert
2. Neue Edelstahl-316L-Platte (verstärkt)
3. 6 Nieten statt 4 (Monelbronze)
4. Tuchriss mit doppeltem Dacron-Patch repariert
5. Verstärkungslage vergrößert

**Kosten:** 750 EUR (Segelmacher Las Palmas)
**Ergebnis:** Kein weiterer Vorfall in 3 Jahren Langfahrt

**Lehre:** Kopfbrett bei Langfahrt-Segeln alle 2 Jahre professionell inspizieren.
Nieten auf Ermüdung prüfen. Emergency-Dyneema-Leine am Kopfbrett immer vorhalten.

---

### ANHANG G: Hanse 548 — UV-Streifen-Versagen nach 7 Jahren

**Yacht:** Hanse 548 (2017), Stationierung: Mallorca
**Segel:** Genua (Dacron), Elvström Sails, Baujahr 2017
**Problem:** UV-Streifen nach 7 Jahren in Mallorca komplett verhärtet und brüchig

**Befund:**
- UV-Streifen (Sunbrella Navy): Farbe gut, aber Stoff spröde
- Nähte (V-69 Polyester): 80 % degradiert (Stadium 3–4)
- Segeltuch unter UV-Streifen: in einwandfreiem Zustand
- UV-Streifen hat seinen Zweck 7 Jahre lang erfüllt

**Maßnahmen:**
1. UV-Streifen komplett entfernt
2. Neuer UV-Streifen (Sunbrella Navy, 200 mm Breite)
3. Nähte komplett mit Tenara PTFE
4. 303 Aerospace Protectant als zusätzlicher Schutz

**Kosten:** 620 EUR (Segelmacher Palma)
**Ergebnis:** UV-Streifen erneuert, Segeltuch in Top-Zustand

**Lehre:** UV-Streifen haben eine Lebensdauer von 7–12 Jahren (Mittelmeer).
Rechtzeitig erneuern, bevor das darunter liegende Tuch beschädigt wird.
Tenara PTFE-Garn für die Nähte ist Pflicht in südlichen Revieren.

---

### ANHANG H: X-Yachts Xp 44 — Laminat-Großsegel Totalschaden

**Yacht:** X-Yachts Xp 44 (2016), Regatta + Fahrt, Ostsee
**Segel:** Großsegel (Kevlar/Carbon-Laminat), North Sails 3Di RAW 760, Baujahr 2018
**Problem:** Großflächige Delamination nach 6 Saisons (Regatta + Fahrt)

**Befund:**
- Delamination auf ca. 35 % der Segelfläche
- Konzentration im oberen Achterliek und entlang der diagonalen Bahnen
- Taffeta an mehreren Stellen abgelöst
- Segelform um 18 % gegenüber Neuzustand verformt
- Nähte: 70 % Stadium 2 UV-Degradation

**Analyse:**
- 6 Saisons mit intensivem Einsatz (ca. 200 Stunden/Jahr = 1.200 Stunden)
- Regattaeinsatz mit hohen Lasten
- Materialermüdung bei Kevlar-Laminat nach 1.200 Stunden innerhalb der Spezifikation
- Kein Pflegefehler — Material hat seine normale Lebensdauer erreicht

**Maßnahmen:**
1. Reparatur unwirtschaftlich (Kosten > 8.000 EUR, >50 % des Neupreises)
2. Neusegel bestellt: North Sails 3Di RAW 780 (aktuellere Generation)
3. Altes Segel als Leichtwind-Reservesegel degradiert (nur bei <15 kn)

**Kosten:** 16.500 EUR (Neusegel)
**Ergebnis:** Neusegel liefert ca. 8 % bessere Performance als das alte (Neuzustand)

**Lehre:** Kevlar-Laminat hat eine begrenzte Lebensdauer (4–7 Jahre Regatta).
Kein Pflegefehler — Materialcharakteristik. Bei Regattaeinsatz: Segelbudget für
Austausch alle 5–6 Jahre einplanen. Carbon/Dyneema-Laminat hält länger (8–12 Jahre).

---

## 17. ANHANG I–R: Pydantic v2 Schemata

### ANHANG I: SailCondition (Segelzustand)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import date


class SailMaterial(str, Enum):
    DACRON = "dacron"
    LAMINATE = "laminate"
    MEMBRANE_3DI = "membrane_3di"
    MEMBRANE_D4 = "membrane_d4"
    NYLON = "nylon"
    PENTEX = "pentex"
    KEVLAR_LAMINATE = "kevlar_laminate"
    CARBON_LAMINATE = "carbon_laminate"
    DYNEEMA_LAMINATE = "dyneema_laminate"
    TECHNORA_LAMINATE = "technora_laminate"


class SailType(str, Enum):
    MAINSAIL = "mainsail"
    GENOA = "genoa"
    JIB = "jib"
    SPINNAKER = "spinnaker"
    GENNAKER = "gennaker"
    CODE_0 = "code_0"
    STORM_JIB = "storm_jib"
    TRYSAIL = "trysail"


class ConditionGrade(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    FAILED = "failed"


class SailCondition(BaseModel):
    model_config = {"from_attributes": True}

    sail_type: SailType = Field(..., description="Typ des Segels")
    material: SailMaterial = Field(..., description="Segelmaterial")
    manufacturer: str = Field(..., description="Segelhersteller")
    year_built: int = Field(..., ge=1970, le=2030, description="Baujahr des Segels")
    area_sqm: float = Field(..., gt=0, le=500, description="Segelfläche in m²")
    estimated_hours: Optional[float] = Field(
        None, ge=0, description="Geschätzte Nutzungsstunden"
    )
    overall_condition: ConditionGrade = Field(
        ..., description="Gesamtzustand des Segels"
    )
    seam_condition: ConditionGrade = Field(..., description="Zustand der Nähte")
    uv_strip_condition: Optional[ConditionGrade] = Field(
        None, description="Zustand des UV-Streifens (falls vorhanden)"
    )
    cloth_condition: ConditionGrade = Field(..., description="Zustand des Tuchs")
    hardware_condition: ConditionGrade = Field(
        ..., description="Zustand der Hardware (Kopfbrett, Kauschen etc.)"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, le=20, description="Geschätzte Restlebensdauer in Jahren"
    )
    last_inspection_date: Optional[date] = Field(
        None, description="Datum der letzten professionellen Inspektion"
    )
    notes: Optional[str] = Field(
        None, max_length=2000, description="Zusätzliche Anmerkungen"
    )
```

### ANHANG J: SailMaintenanceRecord (Wartungseintrag)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date
from decimal import Decimal


class MaintenanceType(str, Enum):
    PRE_SAIL_CHECK = "pre_sail_check"
    MONTHLY_CHECK = "monthly_check"
    SEASONAL_WINTERIZE = "seasonal_winterize"
    SEASONAL_COMMISSION = "seasonal_commission"
    ANNUAL_INSPECTION = "annual_inspection"
    THREE_YEAR_OVERHAUL = "three_year_overhaul"
    CLEANING = "cleaning"
    REPAIR = "repair"
    UV_STRIP_REPLACEMENT = "uv_strip_replacement"
    SEAM_REVISION = "seam_revision"
    PROFESSIONAL_INSPECTION = "professional_inspection"
    RECUT = "recut"


class MaintenanceProvider(str, Enum):
    OWNER = "owner"
    PROFESSIONAL_SAILMAKER = "professional_sailmaker"
    BOATYARD = "boatyard"


class SailMaintenanceRecord(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    maintenance_date: date = Field(..., description="Datum der Wartung")
    maintenance_type: MaintenanceType = Field(..., description="Art der Wartung")
    provider: MaintenanceProvider = Field(
        ..., description="Durchführender (Eigner oder Profi)"
    )
    provider_name: Optional[str] = Field(
        None, description="Name des Segelmachers/Betriebs"
    )
    description: str = Field(
        ..., max_length=2000, description="Beschreibung der durchgeführten Maßnahmen"
    )
    findings: Optional[str] = Field(
        None, max_length=2000, description="Befunde und Beobachtungen"
    )
    cost_eur: Optional[Decimal] = Field(
        None, ge=0, le=50000, description="Kosten in EUR"
    )
    parts_used: Optional[List[str]] = Field(
        None, description="Verwendete Materialien und Ersatzteile"
    )
    next_action: Optional[str] = Field(
        None, max_length=500, description="Empfohlene nächste Maßnahme"
    )
    next_action_date: Optional[date] = Field(
        None, description="Empfohlenes Datum für nächste Maßnahme"
    )
    cumulative_hours_at_maintenance: Optional[float] = Field(
        None, ge=0, description="Kumulative Segelstunden zum Wartungszeitpunkt"
    )
```

### ANHANG K: SailDamageReport (Schadensbericht)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date


class DamageType(str, Enum):
    UV_THREAD_DEGRADATION = "uv_thread_degradation"
    MOLD_MILDEW = "mold_mildew"
    RUST_STAINING = "rust_staining"
    LAMINATE_DELAMINATION = "laminate_delamination"
    CHAFE_SPREADER = "chafe_spreader"
    FLOGGING_TEAR = "flogging_tear"
    UV_STRIP_FAILURE = "uv_strip_failure"
    BATTEN_POCKET_WEAR = "batten_pocket_wear"
    HEADBOARD_PULLOUT = "headboard_pullout"
    LUFF_TAPE_SEPARATION = "luff_tape_separation"
    ZIPPER_FAILURE = "zipper_failure"
    SALT_CRYSTALLIZATION = "salt_crystallization"
    OTHER = "other"


class DamageSeverity(int, Enum):
    GRADE_1 = 1
    GRADE_2 = 2
    GRADE_3 = 3
    GRADE_4 = 4


class DamageLocation(str, Enum):
    HEAD = "head"
    TACK = "tack"
    CLEW = "clew"
    LUFF = "luff"
    LEECH = "leech"
    FOOT = "foot"
    BODY_UPPER = "body_upper"
    BODY_MIDDLE = "body_middle"
    BODY_LOWER = "body_lower"
    BATTEN_POCKET = "batten_pocket"
    REEF_POINT = "reef_point"
    UV_STRIP = "uv_strip"


class RepairRecommendation(str, Enum):
    MONITOR = "monitor"
    DIY_REPAIR = "diy_repair"
    PROFESSIONAL_REPAIR = "professional_repair"
    URGENT_PROFESSIONAL_REPAIR = "urgent_professional_repair"
    REPLACE_SAIL = "replace_sail"
    DO_NOT_USE = "do_not_use"


class SailDamageReport(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    damage_code: str = Field(
        ..., pattern=r"^F-16_08-\d{2}$",
        description="Fehlerbildcode (z. B. F-16_08-01)"
    )
    damage_type: DamageType = Field(..., description="Art des Schadens")
    severity: DamageSeverity = Field(..., description="Schweregrad 1–4")
    location: DamageLocation = Field(
        ..., description="Position des Schadens am Segel"
    )
    location_detail: Optional[str] = Field(
        None, max_length=200,
        description="Detaillierte Positionsbeschreibung"
    )
    discovery_date: date = Field(..., description="Entdeckungsdatum")
    description: str = Field(
        ..., max_length=2000, description="Beschreibung des Schadens"
    )
    affected_area_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Betroffener Flächenanteil in Prozent"
    )
    photo_references: Optional[List[str]] = Field(
        None, description="Referenzen zu Fotos des Schadens"
    )
    repair_recommendation: RepairRecommendation = Field(
        ..., description="Reparaturempfehlung"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, le=50000,
        description="Geschätzte Reparaturkosten in EUR"
    )
    is_safety_critical: bool = Field(
        False, description="Sicherheitsrelevanter Schaden?"
    )
```

### ANHANG L: SailCleaningProtocol (Reinigungsprotokoll)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date


class CleaningMethod(str, Enum):
    FRESH_WATER_RINSE = "fresh_water_rinse"
    HAND_WASH = "hand_wash"
    MACHINE_WASH = "machine_wash"
    PROFESSIONAL_WASH = "professional_wash"
    SPOT_CLEANING = "spot_cleaning"
    SOAK = "soak"


class CleaningProduct(str, Enum):
    STAR_BRITE_SAIL_CANVAS = "star_brite_sail_canvas_cleaner"
    SNYDER_SAIL_BATH = "snyder_sail_bath"
    BIOVEX_SAIL_CLEANER = "biovex_sail_cleaner"
    STAR_BRITE_MILDEW_REMOVER = "star_brite_mildew_remover"
    OXALIC_ACID = "oxalic_acid"
    MILD_DISH_SOAP = "mild_dish_soap"
    VINEGAR_SOLUTION = "vinegar_solution"
    WATER_ONLY = "water_only"
    OTHER = "other"


class StainType(str, Enum):
    MOLD_MILDEW = "mold_mildew"
    RUST = "rust"
    VERDIGRIS = "verdigris"
    OIL_GREASE = "oil_grease"
    BIRD_DROPPINGS = "bird_droppings"
    BLOOD = "blood"
    SALT_DEPOSITS = "salt_deposits"
    GENERAL_DIRT = "general_dirt"
    ALGAE = "algae"


class SailCleaningProtocol(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    cleaning_date: date = Field(..., description="Reinigungsdatum")
    method: CleaningMethod = Field(..., description="Reinigungsmethode")
    products_used: List[CleaningProduct] = Field(
        ..., min_length=1, description="Verwendete Reinigungsmittel"
    )
    product_dilution: Optional[str] = Field(
        None, description="Verdünnung (z. B. '1:10')"
    )
    water_temperature_c: Optional[float] = Field(
        None, ge=0, le=40, description="Wassertemperatur in °C"
    )
    soak_duration_min: Optional[int] = Field(
        None, ge=0, le=240, description="Einweichzeit in Minuten"
    )
    stains_treated: Optional[List[StainType]] = Field(
        None, description="Behandelte Fleckentypen"
    )
    stain_removal_success_pct: Optional[float] = Field(
        None, ge=0, le=100, description="Erfolgsrate der Fleckenentfernung in %"
    )
    drying_duration_hours: Optional[float] = Field(
        None, ge=0, le=72, description="Trocknungszeit in Stunden"
    )
    notes: Optional[str] = Field(
        None, max_length=1000, description="Anmerkungen"
    )
```

### ANHANG M: UVStripAssessment (UV-Streifen-Bewertung)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import date


class UVStripMaterial(str, Enum):
    SUNBRELLA_ACRYLIC = "sunbrella_acrylic"
    PVC_POLYESTER = "pvc_polyester"
    PARASAIL_NYLON = "parasail_nylon"
    OTHER = "other"


class UVStripColor(str, Enum):
    NAVY = "navy"
    BLACK = "black"
    PACIFIC_BLUE = "pacific_blue"
    GREY = "grey"
    WHITE = "white"
    RED = "red"
    GREEN = "green"
    OTHER = "other"


class UVStripConditionGrade(str, Enum):
    GOOD = "good"
    FADED = "faded"
    HARDENING = "hardening"
    SEAM_DETACHING = "seam_detaching"
    BRITTLE = "brittle"
    FAILED = "failed"


class UVStripAssessment(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    assessment_date: date = Field(..., description="Bewertungsdatum")
    material: UVStripMaterial = Field(..., description="UV-Streifen-Material")
    color: UVStripColor = Field(..., description="Farbe des UV-Streifens")
    width_mm: float = Field(
        ..., gt=0, le=500, description="Breite des UV-Streifens in mm"
    )
    year_installed: int = Field(
        ..., ge=1990, le=2030, description="Installationsjahr"
    )
    condition: UVStripConditionGrade = Field(
        ..., description="Zustandsbewertung"
    )
    color_retention_pct: Optional[float] = Field(
        None, ge=0, le=100, description="Farberhaltung in Prozent"
    )
    seam_thread_type: Optional[str] = Field(
        None, description="Nähgarntyp (z. B. 'V-92', 'Tenara PTFE')"
    )
    seam_condition: Optional[str] = Field(
        None, description="Zustand der UV-Streifen-Nähte"
    )
    replacement_recommended: bool = Field(
        ..., description="Erneuerung empfohlen?"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0, le=5000, description="Geschätzte Erneuerungskosten in EUR"
    )
    notes: Optional[str] = Field(
        None, max_length=1000, description="Anmerkungen"
    )
```

### ANHANG N: SeamInspectionResult (Naht-Inspektionsergebnis)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date


class SeamLocation(str, Enum):
    LUFF = "luff"
    LEECH = "leech"
    FOOT = "foot"
    PANEL_SEAMS = "panel_seams"
    REINFORCEMENT_PATCHES = "reinforcement_patches"
    BATTEN_POCKETS = "batten_pockets"
    REEF_POINTS = "reef_points"
    UV_STRIP_SEAMS = "uv_strip_seams"
    HEADBOARD = "headboard"
    CLEW = "clew"
    TACK = "tack"


class ThreadType(str, Enum):
    POLYESTER_V69 = "polyester_v69"
    POLYESTER_V92 = "polyester_v92"
    POLYESTER_V138 = "polyester_v138"
    TENARA_PTFE = "tenara_ptfe"
    DYNEEMA = "dyneema"
    UNKNOWN = "unknown"


class UVDegradationStage(int, Enum):
    STAGE_0 = 0  # Neuzustand
    STAGE_1 = 1  # Oberflächenabbau
    STAGE_2 = 2  # Fortgeschrittener Abbau
    STAGE_3 = 3  # Kritischer Abbau
    STAGE_4 = 4  # Nahtversagen


class SeamInspectionResult(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    inspection_date: date = Field(..., description="Inspektionsdatum")
    location: SeamLocation = Field(
        ..., description="Position der inspizierten Naht"
    )
    thread_type: ThreadType = Field(..., description="Nähgarntyp")
    stitch_type: Optional[str] = Field(
        None, description="Stichart (z. B. 'lockstitch', 'zigzag')"
    )
    stitch_length_mm: Optional[float] = Field(
        None, ge=1, le=15, description="Stichlänge in mm"
    )
    uv_degradation_stage: UVDegradationStage = Field(
        ..., description="UV-Degradationsstufe 0–4"
    )
    pull_test_passed: bool = Field(
        ..., description="Zugtest bestanden?"
    )
    gaps_found: bool = Field(
        ..., description="Lücken in der Naht gefunden?"
    )
    gap_count: Optional[int] = Field(
        None, ge=0, description="Anzahl der Nahtlücken"
    )
    affected_length_mm: Optional[float] = Field(
        None, ge=0, description="Betroffene Nahtlänge in mm"
    )
    repair_needed: bool = Field(
        ..., description="Reparatur erforderlich?"
    )
    repair_urgency: Optional[str] = Field(
        None, description="Dringlichkeit: 'niedrig', 'mittel', 'hoch', 'kritisch'"
    )
    notes: Optional[str] = Field(
        None, max_length=1000, description="Anmerkungen"
    )
```

### ANHANG O: SailStorageCondition (Lagerungsbedingungen)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import date


class StorageMethod(str, Enum):
    SAIL_BAG_FOLDED = "sail_bag_folded"
    SAIL_BAG_ROLLED = "sail_bag_rolled"
    LAZY_BAG = "lazy_bag"
    IN_MAST_FURLING = "in_mast_furling"
    IN_BOOM_FURLING = "in_boom_furling"
    ROLLER_FURLING_ON_STAY = "roller_furling_on_stay"
    LOOSE_IN_LOCKER = "loose_in_locker"
    PROFESSIONAL_STORAGE = "professional_storage"


class StorageLocation(str, Enum):
    ONBOARD_LOCKER = "onboard_locker"
    ONBOARD_CABIN = "onboard_cabin"
    ONBOARD_RIGGED = "onboard_rigged"
    SHORE_GARAGE = "shore_garage"
    SHORE_SAIL_LOFT = "shore_sail_loft"
    SHORE_CLIMATE_CONTROLLED = "shore_climate_controlled"


class SailStorageCondition(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    storage_start_date: date = Field(..., description="Beginn der Lagerung")
    storage_end_date: Optional[date] = Field(
        None, description="Ende der Lagerung"
    )
    method: StorageMethod = Field(..., description="Lagerungsmethode")
    location: StorageLocation = Field(..., description="Lagerort")
    temperature_range_c: Optional[str] = Field(
        None, description="Temperaturbereich (z. B. '5–20')"
    )
    humidity_pct: Optional[float] = Field(
        None, ge=0, le=100, description="Relative Luftfeuchtigkeit in %"
    )
    desiccant_used: bool = Field(
        False, description="Trockenmittel (Silikagel) verwendet?"
    )
    anti_mildew_used: bool = Field(
        False, description="Anti-Schimmel-Mittel verwendet?"
    )
    cleaned_before_storage: bool = Field(
        ..., description="Vor Lagerung gereinigt?"
    )
    dried_before_storage: bool = Field(
        ..., description="Vor Lagerung vollständig getrocknet?"
    )
    condition_at_storage_start: Optional[str] = Field(
        None, max_length=500,
        description="Zustandsbeschreibung bei Einlagerung"
    )
    condition_at_storage_end: Optional[str] = Field(
        None, max_length=500,
        description="Zustandsbeschreibung bei Auslagerung"
    )
    issues_during_storage: Optional[str] = Field(
        None, max_length=1000,
        description="Probleme während der Lagerung"
    )
```

### ANHANG P: SailLifecycleEstimate (Lebensdauer-Schätzung)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import date


class CruisingArea(str, Enum):
    BALTIC = "baltic"
    NORTH_SEA = "north_sea"
    ATLANTIC_NORTH = "atlantic_north"
    ATLANTIC_TRADE_WINDS = "atlantic_trade_winds"
    MEDITERRANEAN = "mediterranean"
    CARIBBEAN = "caribbean"
    TROPICS = "tropics"
    SOUTH_PACIFIC = "south_pacific"
    HIGH_LATITUDES = "high_latitudes"


class UsageIntensity(str, Enum):
    LIGHT = "light"           # < 100 h/Jahr
    MODERATE = "moderate"     # 100–300 h/Jahr
    HEAVY = "heavy"           # 300–600 h/Jahr
    PROFESSIONAL = "professional"  # > 600 h/Jahr


class MaintenanceLevel(str, Enum):
    OPTIMAL = "optimal"       # Pflegefaktor 1,3
    STANDARD = "standard"     # Pflegefaktor 1,0
    MINIMAL = "minimal"       # Pflegefaktor 0,7
    NONE = "none"             # Pflegefaktor 0,5


class SailLifecycleEstimate(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    estimation_date: date = Field(..., description="Datum der Schätzung")
    sail_material: str = Field(..., description="Segelmaterial")
    sail_type: str = Field(..., description="Segeltyp")
    year_built: int = Field(..., ge=1970, le=2030, description="Baujahr")
    base_lifetime_years: float = Field(
        ..., gt=0, le=30, description="Basis-Lebensdauer in Jahren"
    )
    cruising_area: CruisingArea = Field(..., description="Hauptrevier")
    area_factor: float = Field(
        ..., gt=0, le=2, description="Revierfaktor"
    )
    usage_intensity: UsageIntensity = Field(
        ..., description="Nutzungsintensität"
    )
    maintenance_level: MaintenanceLevel = Field(
        ..., description="Pflegeniveau"
    )
    maintenance_factor: float = Field(
        ..., gt=0, le=2, description="Pflegefaktor"
    )
    current_age_years: float = Field(
        ..., ge=0, le=30, description="Aktuelles Alter in Jahren"
    )
    estimated_remaining_life_years: float = Field(
        ..., ge=0, le=30, description="Geschätzte Restlebensdauer in Jahren"
    )
    estimated_total_life_years: float = Field(
        ..., gt=0, le=30, description="Geschätzte Gesamtlebensdauer in Jahren"
    )
    confidence: str = Field(
        ..., description="Konfidenzniveau der Schätzung"
    )
    recommendation: Optional[str] = Field(
        None, max_length=500, description="Empfehlung"
    )
```

### ANHANG Q: RepairKitInventory (Reparaturkit-Inventar)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date
from decimal import Decimal


class KitLevel(str, Enum):
    BASIC = "basic"           # Küstenfahrt
    EXTENDED = "extended"     # Langfahrt / Offshore
    PROFESSIONAL = "professional"  # Regatta / Werft


class KitItemCategory(str, Enum):
    TOOLS = "tools"
    THREAD = "thread"
    NEEDLES = "needles"
    TAPE_ADHESIVE = "tape_adhesive"
    CLOTH_PATCHES = "cloth_patches"
    HARDWARE = "hardware"
    CLEANING = "cleaning"
    MISCELLANEOUS = "miscellaneous"


class RepairKitItem(BaseModel):
    model_config = {"from_attributes": True}

    item_name: str = Field(..., max_length=200, description="Artikelbezeichnung")
    category: KitItemCategory = Field(..., description="Kategorie")
    product_name: Optional[str] = Field(
        None, max_length=200, description="Produktname / Marke"
    )
    quantity: int = Field(..., ge=1, description="Menge")
    unit: Optional[str] = Field(
        None, max_length=20, description="Einheit (Stk., m, ml etc.)"
    )
    price_eur: Optional[Decimal] = Field(
        None, ge=0, le=5000, description="Preis in EUR"
    )
    expiry_date: Optional[date] = Field(
        None, description="Verfallsdatum (falls zutreffend)"
    )
    last_checked: Optional[date] = Field(
        None, description="Letzter Kontrolltermin"
    )
    needs_replacement: bool = Field(
        False, description="Ersatz nötig?"
    )
    notes: Optional[str] = Field(
        None, max_length=500, description="Anmerkungen"
    )


class RepairKitInventory(BaseModel):
    model_config = {"from_attributes": True}

    yacht_id: str = Field(..., description="Referenz-ID der Yacht")
    kit_level: KitLevel = Field(..., description="Kit-Level")
    last_inventory_date: date = Field(
        ..., description="Datum der letzten Inventur"
    )
    items: List[RepairKitItem] = Field(
        ..., min_length=1, description="Kit-Inhalt"
    )
    total_value_eur: Optional[Decimal] = Field(
        None, ge=0, le=10000, description="Gesamtwert in EUR"
    )
    storage_location: Optional[str] = Field(
        None, max_length=200, description="Lagerort an Bord"
    )
    notes: Optional[str] = Field(
        None, max_length=1000, description="Anmerkungen"
    )
```

### ANHANG R: SailMaintenancePlan (Wartungsplan)

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from datetime import date


class PlanInterval(str, Enum):
    PRE_SAIL = "pre_sail"
    MONTHLY = "monthly"
    SEASONAL = "seasonal"
    ANNUAL = "annual"
    THREE_YEAR = "three_year"
    AS_NEEDED = "as_needed"


class PlanPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class PlanStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"
    SKIPPED = "skipped"


class MaintenancePlanItem(BaseModel):
    model_config = {"from_attributes": True}

    task_name: str = Field(..., max_length=200, description="Aufgabenbezeichnung")
    interval: PlanInterval = Field(..., description="Intervall")
    priority: PlanPriority = Field(..., description="Priorität")
    applicable_materials: Optional[List[str]] = Field(
        None, description="Anwendbare Materialtypen"
    )
    description: str = Field(
        ..., max_length=1000, description="Aufgabenbeschreibung"
    )
    estimated_duration_min: Optional[int] = Field(
        None, ge=0, le=480, description="Geschätzte Dauer in Minuten"
    )
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0, le=5000, description="Geschätzte Kosten in EUR"
    )
    diy_possible: bool = Field(
        True, description="In Eigenleistung durchführbar?"
    )
    tools_required: Optional[List[str]] = Field(
        None, description="Benötigte Werkzeuge"
    )
    reference_section: Optional[str] = Field(
        None, description="Verweis auf Abschnitt in dieser Wissensdatenbank"
    )


class SailMaintenancePlan(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    yacht_id: str = Field(..., description="Referenz-ID der Yacht")
    plan_created_date: date = Field(
        ..., description="Erstellungsdatum des Plans"
    )
    plan_valid_until: date = Field(
        ..., description="Gültigkeit des Plans"
    )
    sail_material: str = Field(..., description="Segelmaterial")
    sail_type: str = Field(..., description="Segeltyp")
    cruising_area: str = Field(..., description="Hauptrevier")
    tasks: List[MaintenancePlanItem] = Field(
        ..., min_length=1, description="Wartungsaufgaben"
    )
    next_professional_inspection: Optional[date] = Field(
        None, description="Nächste professionelle Inspektion"
    )
    next_seasonal_maintenance: Optional[date] = Field(
        None, description="Nächste saisonale Wartung"
    )
    notes: Optional[str] = Field(
        None, max_length=1000, description="Anmerkungen zum Plan"
    )


class SailMaintenanceScheduleEntry(BaseModel):
    model_config = {"from_attributes": True}

    sail_id: str = Field(..., description="Referenz-ID des Segels")
    task_name: str = Field(..., max_length=200, description="Aufgabe")
    scheduled_date: date = Field(..., description="Geplantes Datum")
    status: PlanStatus = Field(
        PlanStatus.PENDING, description="Status"
    )
    completed_date: Optional[date] = Field(
        None, description="Tatsächliches Durchführungsdatum"
    )
    performed_by: Optional[str] = Field(
        None, description="Durchgeführt von"
    )
    cost_eur: Optional[float] = Field(
        None, ge=0, le=10000, description="Tatsächliche Kosten in EUR"
    )
    findings: Optional[str] = Field(
        None, max_length=1000, description="Befunde"
    )
    next_scheduled_date: Optional[date] = Field(
        None, description="Nächster geplanter Termin"
    )
```

---

**Ende der Wissensdatenbank 16_08 — Segel — Wartung, Pflege und Reparatur**

*Erstellt: 2026-04 | Version 2.0 | AYDI Maritime Knowledge Base*
*Alle Preisangaben in EUR, Stand 2025/2026, ohne Gewähr.*
*Alle Angaben nach bestem Wissen und Gewissen, ersetzen aber keine professionelle Beratung.*
