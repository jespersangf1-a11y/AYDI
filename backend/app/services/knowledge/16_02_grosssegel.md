---
titel: "Großsegel — Typen, Materialien und Trimm"
kategorie: "Segel"
unterkategorie: "Großsegel"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 16_02 — Großsegel — Typen, Materialien und Trimm

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Großsegel-Typen](#2-großsegel-typen)
3. [Materialien](#3-materialien)
4. [Konstruktion und Schnitt](#4-konstruktion-und-schnitt)
5. [Trimm](#5-trimm)
6. [Reefing-Systeme](#6-reefing-systeme)
7. [Hersteller](#7-hersteller)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [Lebensdauer](#10-lebensdauer)
11. [Kosten](#11-kosten)
12. [FAQ](#12-faq)
13. [Glossar](#13-glossar)
14. [Schnell-Referenz](#14-schnell-referenz)
15. [ANHANG A–H: Fallstudien](#15-anhang-a-h-fallstudien)
16. [ANHANG I–R: Pydantic v2 Modelle](#16-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einführung

### 1.1 Rolle des Großsegels im Gesamtkonzept

Das Großsegel ist das primäre Antriebssegel auf nahezu allen Segelyachten und stellt
den zentralen Bestandteil des Riggs dar. Es ist achterlich des Mastes angeschlagen und
wird am Unterliek durch den Großbaum gespannt. Seine Funktion geht weit über die
bloße Erzeugung von Vortrieb hinaus — es bestimmt maßgeblich das Steuerverhalten,
die Krängung und die Balance der gesamten Yacht.

#### 1.1.1 Antriebsanteil nach Kursen

Der Antriebsanteil des Großsegels variiert erheblich je nach Kurs zum Wind:

| Kurs | Großsegel-Anteil | Vorsegel-Anteil | Anmerkung |
|------|------------------|-----------------|-----------|
| Hart am Wind (30–40°) | 35–45 % | 55–65 % | Vorsegel dominiert durch Slot-Effekt |
| Halbwind (60–90°) | 50–60 % | 40–50 % | Ausgewogene Lastverteilung |
| Raumschots (100–140°) | 55–70 % | 30–45 % | Großsegel gewinnt an Bedeutung |
| Vorwind (150–180°) | 40–50 % | 50–60 % | Mit Spinnaker/Gennaker Vorsegel dominant |

Diese Werte gelten für eine typische Slup-Takelung mit überlappender Genua.
Bei Nicht-überlappenden Vorsegeln (Selbstwendefock, J-Fock) verschiebt sich
der Anteil zugunsten des Großsegels um ca. 5–15 Prozentpunkte.

#### 1.1.2 Der Slot-Effekt

Der Slot-Effekt (auch Spalt-Effekt oder Düseneffekt) beschreibt die aerodynamische
Wechselwirkung zwischen Vorsegel und Großsegel. Die Luv-Seite des Großsegels wird
durch das vorgelagerte Vorsegel mit beschleunigter Luft angeströmt, was:

- Die Strömungsgeschwindigkeit auf der Lee-Seite des Großsegels erhöht
- Den effektiven Anstellwinkel des Großsegels verändert
- Die Ablösegefahr auf der Lee-Seite reduziert
- Den Gesamtauftrieb des Segelplans um 10–30 % steigert

Der optimale Slot-Abstand (Spalt zwischen Achterlik des Vorsegels und Vorliek des
Großsegels) beträgt typischerweise 10–15 % der Großsegeltiefe am jeweiligen
Querschnitt. Ein zu enger Slot erzeugt Rückstau; ein zu weiter Slot reduziert
den Düseneffekt.

#### 1.1.3 Steuerbalance und Ruderdruckminimierung

Das Großsegel beeinflusst den Lateralplan-Druckpunkt (Centre of Effort, CE)
maßgeblich. Ein korrekt getrimmtes Großsegel erzeugt ein leichtes Luvgiermoment
(3–5° Ruderwinkel bei mittlerer Windstärke), was als "Wetterluvigkeit" bezeichnet
wird und die Kursstabilität verbessert.

Zu viel Luvgierigkeit (>7° Ruderwinkel) deutet auf:
- Zu tiefes Großsegelprofil
- Zu viel Twist im oberen Bereich
- Achterlich verschobenen Druckpunkt
- Falsche Traveller-Position

### 1.2 Historische Entwicklung

#### 1.2.1 Baumwollsegel (bis ca. 1955)

Die frühesten Yachtsegel wurden aus ägyptischer Baumwolle gefertigt. Charakteristiken:
- Hohe Dehnung unter Last (5–8 %)
- Wasseraufnahme bis 15 % des Eigengewichts
- Schimmelbildung ohne vollständige Trocknung
- Lebensdauer: 2–4 Saisons
- Profil musste bewusst "eingesegelt" werden

Baumwollsegel erforderten erhebliche Erfahrung im Trimm, da das Profil sich mit
der Feuchtigkeit und der Belastung ständig veränderte.

#### 1.2.2 Dacron-Revolution (1955–1980)

Die Einführung von Polyester-Gewebe (Handelsname "Dacron" von DuPont, in Europa
auch "Terylene" von ICI) revolutionierte den Segelsport:
- Dehnung reduziert auf 1–3 %
- Keine Wasseraufnahme
- Formstabilität über Hunderte von Stunden
- Lebensdauer: 5–10 Saisons
- Sofort einsatzbereites Profil

Dacron ist bis heute das meistverwendete Segelmaterial für Fahrtenyachten
und dominiert den Markt im Bereich unter 45 Fuß.

#### 1.2.3 Laminatsegel (1980–2005)

Die Entwicklung von Laminaten — Verbundmaterialien aus Trägerschichten (Mylar,
Taffeta) und Verstärkungsfasern (Kevlar, Technora, Spectra) — ermöglichte:
- Dehnung unter 1 %
- Gezielte Faserausrichtung entlang der Lastpfade
- Geringeres Gewicht bei gleicher Festigkeit
- Komplexere Profilgestaltung

Nachteile der frühen Laminate: Delamination, UV-Empfindlichkeit der Aramid-Fasern,
begrenzte Knickfestigkeit, hohe Kosten.

#### 1.2.4 Membransegel und 3D-Technologie (2005–heute)

Moderne Membransegel (North 3Di, Elvström EPEX, Doyle Stratis) werden nicht mehr
geschnitten und genäht, sondern auf dreidimensionalen Formen laminiert oder
thermogeformt:

- Minimale Dehnung (0,2–0,5 %)
- Durchgehende Fasern über das gesamte Segel
- Keine Nähte als Schwachstellen
- Computeroptimierte Faserverteilung
- Lebensdauer: 8–15 Saisons (Fahrt), 3–6 Saisons (Regatta)

### 1.3 Normative Grundlagen

#### 1.3.1 Segelbezeichnungen nach ISAF/World Sailing

Das Großsegel wird in den World-Sailing-Vermessungsregeln als "Mainsail" (Abk. "M")
definiert. Die Vermessungspunkte sind:

- **Kopf** (Head): Oberstes Ende des Vorlieks
- **Hals** (Tack): Unteres vorderes Ende, Verbindung Mast/Baum
- **Schothorn** (Clew): Unteres hinteres Ende
- **Vorliek** (Luff): Vorderkante, am Mast befestigt
- **Unterliek** (Foot): Unterkante, am Baum befestigt oder lose
- **Achterliek** (Leech): Hinterkante, frei stehend
- **Brusttiefe** (Maximum Girth): Breiteste Stelle des Segels

#### 1.3.2 Vermessungsmaße

| Maß | Symbol | Beschreibung |
|-----|--------|-------------|
| P | P | Vorlieklänge (Luff length) |
| E | E | Unterlieklänge (Foot length) |
| Obere Segelbreite | HQW | Breite auf 7/8 Höhe |
| 3/4 Segelbreite | TQW | Breite auf 3/4 Höhe |
| Halbe Segelbreite | HW | Breite auf 1/2 Höhe |
| 1/4 Segelbreite | QW | Breite auf 1/4 Höhe |

Die Segelfläche wird nach der Formel berechnet:
```
A_main = P × E / 2 (vereinfacht)
A_main = P × E / 2 + Roach-Fläche (genau)
```

---

## 2. Großsegel-Typen

### 2.1 Konventionelles Großsegel (Slides/Slugs)

#### 2.1.1 Beschreibung

Das konventionelle Großsegel verwendet Rutscher (Slides) oder Slugs zur
Befestigung am Mastprofil. Das Vorliek wird durch eine Reihe von Kunststoff-
oder Edelstahl-Rutschern in die Mastnut (Luff Groove) oder an eine Mastschiene
(Luff Track) geführt.

#### 2.1.2 Befestigungssysteme

**Mastnut-System (Luff Groove):**
- Boltrope (Liektau) gleitet direkt in der Mastnut
- Einfachste und älteste Methode
- Problem: Hohe Reibung, schweres Setzen/Bergen
- Typisch für Boote unter 30 Fuß

**Mastschienen-System (Luff Track):**
- Slides/Slugs laufen auf einer externen Schiene
- Deutlich geringere Reibung
- Einfaches Setzen und Bergen
- Standard für Boote ab 30 Fuß
- Hersteller: Harken, Antal, Frederiksen, Rutgerson

**Slug-System:**
- Kunststoff- oder Edelstahl-Slugs werden mit Shackle oder Webbing
  am Vorliektau befestigt
- Slug-Abstand: 300–500 mm
- Ermöglicht einfachen Austausch einzelner Slugs
- Hersteller: Antal (V-Ball), Harken (Battcar), Tides Marine (SailTrack)

#### 2.1.3 Vor- und Nachteile

**Vorteile:**
- Kostengünstigste Option
- Einfache Reparatur und Austausch
- Bewährt und zuverlässig
- Kompatibel mit allen Reefing-Systemen
- Leichtes Gewicht

**Nachteile:**
- Begrenzte Roach-Fläche (max. 10–12 %)
- Ohne Latten: Achterliek killt
- Profilkontrolle im oberen Bereich begrenzt
- Slides können verklemmen (besonders bei Rollreff)

### 2.2 Volllatten-Großsegel (Full-Batten Mainsail)

#### 2.2.1 Beschreibung

Das Volllatten-Großsegel verwendet durchgehende Latten (Battens) vom Vorliek
bis zum Achterliek. Typischerweise 3–5 Latten, je nach Segelgröße. Die Latten
erzwingen ein kontrolliertes Profil und erlauben eine deutlich größere
Roach-Fläche (15–25 %).

#### 2.2.2 Lattenmaterialien

| Material | Gewicht | Steifigkeit | Lebensdauer | Preis |
|----------|---------|-------------|-------------|-------|
| Fiberglas (GFK) | Mittel | Mittel | 5–8 Jahre | € 15–35/Stk |
| Carbon (CFK) | Gering | Hoch | 8–12 Jahre | € 60–150/Stk |
| PVC-Schaum | Gering | Gering | 3–5 Jahre | € 8–20/Stk |
| Edelstahl (flach) | Hoch | Sehr hoch | 10+ Jahre | € 25–50/Stk |

#### 2.2.3 Lattentaschen und Kompression

Die Latten werden in genähte Lattentaschen eingeschoben. Am Vorliek-Ende sitzt
ein Kompressions-Mechanismus, der die Latte gegen das Vorliek drückt und so
das Profil kontrolliert.

**Kompressionssysteme:**
- Federbelasteter Kunststoffstopfen (Standard)
- Velcro-verstellbar (RBS Batten Systems)
- Schraubverstellbar (Bainbridge)
- Rutgersson Quick-Adjust

Die Lattenspannung beeinflusst das Segelverhalten erheblich:
- Zu wenig Spannung: Latte klappt bei Halse auf Lee-Seite
- Zu viel Spannung: Latte erzeugt harte Kante, keine Profilvariation
- Optimale Spannung: Latte liegt bei Nullwind flach, biegt unter Last
  gleichmäßig in das gewünschte Profil

#### 2.2.4 Battcar-Systeme

Für Volllatten-Segel werden spezielle Batten-Cars (Lattenwagen) am Mast
verwendet, die die erhöhte Querbelastung der durchgehenden Latten aufnehmen:

- **Harken Battcar**: Kugelgelagert, Aluminium, für Masten 80–180 mm
- **Antal V-Ball Battcar**: Kugelgelagert, kompatibel mit Antal-Schienen
- **Frederiksen Battcar**: Kompaktes Design, für kleinere Yachten
- **Tides Marine Strong Track**: Externes Schienensystem mit integrierten Cars

Battcars kosten € 80–250 pro Stück je nach Bootsgröße.

#### 2.2.5 Vor- und Nachteile

**Vorteile:**
- Größere Segelfläche durch Roach (+15–25 %)
- Ruhiges Stehen des Segels (kein Achterliek-Flattern)
- Bessere Profilkontrolle über die gesamte Segelhöhe
- Gleichmäßigeres Profil bei wechselnden Bedingungen
- Reduzierte Ermüdung des Segelmaterials (weniger Schlagen)
- Längere Lebensdauer (ca. 20–30 % mehr als konventionell)
- Einfacheres Reffen (Segel fällt kontrolliert)

**Nachteile:**
- Höheres Gewicht (Latten + Battcars: 3–8 kg Mehrgewicht)
- Höhere Kosten (€ 500–2.000 Mehrkosten)
- Latten können brechen
- Lattentaschen verschleißen
- Höhere Reibung beim Setzen/Bergen
- Bei Wind von achtern: Latten können am Mast/Wanten hängen bleiben
- Reffen erfordert angepasste Technik (Lazy Jacks empfohlen)

### 2.3 Teillatten-Großsegel (Semi-Batten Mainsail)

#### 2.3.1 Beschreibung

Das Teillatten-Großsegel kombiniert kurze Latten im oberen Bereich
(typischerweise 2–3 Latten, Länge 600–1.200 mm) mit einem lattenfreien
unteren Bereich. Dies ist ein Kompromiss zwischen konventionellem und
Volllatten-Segel.

#### 2.3.2 Typische Konfiguration

- Oberste Latte: Volle Breite (stützt den Kopfbereich)
- 2. Latte: 60–80 % der Segelbreite
- 3. Latte: 40–60 % der Segelbreite
- Unterer Bereich: Keine Latten

#### 2.3.3 Vor- und Nachteile

**Vorteile:**
- Moderate Roach möglich (8–15 %)
- Leichter als Volllatten
- Geringere Kosten als Volllatten
- Einfacheres Handling als Volllatten
- Kompatibler mit Standard-Slides

**Nachteile:**
- Weniger Profilkontrolle als Volllatten
- Unteres Achterliek kann noch flattern
- Kompromisslösung — weder volle Vorteile noch minimale Nachteile

### 2.4 Square-Top / Fathead-Großsegel

#### 2.4.1 Beschreibung

Das Square-Top-Großsegel (auch Fathead oder Pinhead genannt) hat einen
verbreiterten Kopfbereich, der statt einer spitzen Dreiecksform eine
nahezu rechteckige oder trapezförmige Kontur aufweist. Die Oberlatte
ist deutlich länger als bei konventionellen Segeln und kann bis zu
40–60 % der E-Maß-Breite erreichen.

#### 2.4.2 Aerodynamische Vorteile

- Reduzierter induzierter Widerstand (ähnlich Winglets bei Flugzeugen)
- Höherer effektiver Aspektratio
- Mehr Segelfläche im oberen, windreicheren Bereich
- Besseres Leistungsgewicht-Verhältnis
- Höherer Lateraldruckpunkt → weniger Krängung bei gleichem Vortrieb

#### 2.4.3 Konstruktionsanforderungen

- Mindestens 4 Volllatten erforderlich
- Obere Latte: Carbon empfohlen (Gewicht oben kritisch)
- Stärkeres Rigg erforderlich (höhere Toppbelastung)
- Angepasstes Achterstag (ggf. Backstagen)
- Spezielle Battcars für obere Latte

#### 2.4.4 Vor- und Nachteile

**Vorteile:**
- 10–20 % mehr Segelfläche im Kopfbereich
- Besseres Höhelaufen
- Geringerer induzierter Widerstand
- Höhere Geschwindigkeit am Wind
- Modernes, sportliches Erscheinungsbild

**Nachteile:**
- Hohe Belastung auf Rigg und Beschläge
- Reffen des oberen Bereichs komplex
- Carbon-Latten erforderlich (Kosten)
- Nicht kompatibel mit In-Mast-Rollreff
- Höherer Verschleiß am Achterliek
- Teurere Fertigung (€ 800–3.000 Aufpreis)

### 2.5 Loose-Footed Großsegel (Loses Unterliek)

#### 2.5.1 Beschreibung

Beim Loose-Footed-Großsegel ist das Unterliek nicht am Großbaum befestigt
(keine Lieknut, keine Slides). Nur das Schothorn und der Hals sind fixiert.
Das Segel kann zwischen Baum und Unterliek frei "atmen".

#### 2.5.2 Trimmvorteile

- Einfachere Outhaul-Verstellung → schnellere Profilanpassung
- Tieferes Profil bei wenig Wind (Bauch hängt natürlich)
- Flacheres Profil bei viel Wind (Outhaul dichtholen)
- Kein Reibungsverlust durch Unterliek-Nut
- Bessere Entwässerung (kein Wasser sammelt sich im Segel)

#### 2.5.3 Vor- und Nachteile

**Vorteile:**
- Schnellere Trimmreaktion
- Einfachere Bedienung
- Weniger Verschleiß am Unterliek
- Leichteres Setzen und Bergen
- Kein Verklemmen in der Baum-Nut

**Nachteile:**
- Leicht geringere projizierte Segelfläche
- Segel kann bei Leichtwind am Baum scheuern
- Optisch weniger "aufgeräumt"
- Cunningham-Effekt am Unterliek reduziert

### 2.6 In-Mast-Rollreff-Großsegel

#### 2.6.1 Funktionsprinzip

Das Großsegel wird in einen hohlen Mast (Profilmast) eingerollt. Eine Rolle
im Mastinneren, angetrieben durch ein Endlos-Fall oder elektrischen Antrieb,
wickelt das Segel um eine vertikale Achse auf.

#### 2.6.2 Schnitt und Konstruktion

In-Mast-Rollreff-Segel unterscheiden sich fundamental von konventionellen Segeln:

- **Flacher Schnitt**: Minimaler Luff-Curve, da sich ein tiefes Profil nicht
  gleichmäßig aufrollen lässt
- **Vertikale Latten**: Kurze, flexible Vertikallatten (200–400 mm) erlauben
  das Aufrollen, stützen aber das Achterliek minimal
- **Kein Roach**: Das Achterliek muss gerade oder leicht hohl geschnitten sein,
  da überstehende Roach beim Einrollen Falten bildet
- **Verstärktes Vorliek**: Das Vorliek nimmt die gesamte Rolllast auf
- **Keine Broadseams im Achterliekbereich**: Würden beim Rollen Falten erzeugen

#### 2.6.3 Mastprofile für In-Mast-Rollreff

| Hersteller | Profil | Bootsgröße | Material | Gewicht/m |
|------------|--------|------------|----------|-----------|
| Seldén | E-Mast | 30–45 ft | Aluminium | 4,5–7,2 kg |
| Seldén | C-Mast | 35–55 ft | Aluminium | 6,8–12,5 kg |
| Seldén | C-Mast Carbon | 40–65 ft | Carbon | 4,2–8,0 kg |
| Furlex/Facnor | FM-Profil | 30–50 ft | Aluminium | 5,0–9,0 kg |
| Z-Spars | Z-Mast | 35–55 ft | Aluminium | 5,5–10,0 kg |
| Hall Spars | Carbon In-Mast | 45–80 ft | Carbon | 3,8–7,5 kg |

#### 2.6.4 Antriebssysteme

**Manuell (Endlos-Fall):**
- Seil wird über eine Trommel geführt
- Bedienung aus dem Cockpit möglich
- Kostengünstig (€ 500–1.500)
- Fehleranfällig bei falscher Bedienung

**Elektrisch:**
- Motor in der Masttrommel oder am Mastfuß
- Fernbedienung oder Schaltpanel
- Kosten: € 3.000–8.000
- Hersteller: Seldén, Harken (UniPower), Lewmar
- Empfohlen ab 40 Fuß

#### 2.6.5 Vor- und Nachteile

**Vorteile:**
- Stufenloses Reffen aus dem Cockpit
- Kein Segel auf dem Baum (aufgeräumtes Deck)
- Einhandsegeln wesentlich erleichtert
- Segel geschützt im Mast (UV, Wetter)
- Kein Persenning erforderlich
- Sicherheit: Reffen ohne Vorschiff-Gang

**Nachteile:**
- 15–25 % Leistungseinbuße gegenüber Volllatten
- Flacherer Schnitt limitiert Leichtwind-Performance
- Kein Roach → weniger Segelfläche
- Teurer Profilmast (€ 5.000–15.000 Aufpreis)
- Mastprofil weniger aerodynamisch
- Rollmechanismus kann klemmen (Fehlerbild F-16_02-10)
- Reparatur schwierig (Segel muss aus Mast)
- Höherer Schwerpunkt durch schwereren Mast
- Bei Totalausfall des Rollsystems: Notfall
- Keine Carbon/Laminat-Segel möglich (Knickempfindlichkeit)

### 2.7 In-Boom-Rollreff-Großsegel

#### 2.7.1 Funktionsprinzip

Das Segel wird in einen speziellen Hohlbaum eingerollt, wobei es sich um
eine horizontale Achse wickelt. Im Gegensatz zum In-Mast-System bleibt der
Mast konventionell, und das Segel kann mit Latten und Roach ausgestattet werden.

#### 2.7.2 Systeme und Hersteller

| System | Hersteller | Bootsgröße | Preis (Baum) | Besonderheit |
|--------|------------|------------|-------------|-------------|
| Leisure Furl | Leisure Furl | 30–80 ft | € 6.000–25.000 | Marktführer, mandrel-System |
| Schaefer In-Boom | Schaefer Marine | 35–60 ft | € 7.000–18.000 | US-Hersteller, robust |
| Bartels In-Boom | Bartels GmbH | 30–50 ft | € 5.000–15.000 | Deutsches Qualitätsprodukt |
| Profurl C-420/C-580 | Profurl/Wichard | 40–70 ft | € 8.000–22.000 | Französisches Design |
| Bamar In-Boom | Bamar Italy | 35–65 ft | € 7.500–20.000 | Italienische Fertigung |

#### 2.7.3 Vor- und Nachteile

**Vorteile:**
- Latten und moderate Roach möglich
- Bessere Segelleistung als In-Mast
- Konventioneller Mast (weniger Gewicht oben)
- Stufenloses Reffen
- Segel geschützt im Baum
- Gute Performance bei allen Windstärken

**Nachteile:**
- Schwerer Baum (20–40 kg Mehrgewicht)
- Hohe Kosten (Baum + angepasstes Segel)
- Baum-Durchmesser größer → Sichtbehinderung
- Komplexe Mechanik
- Segelschnitt muss angepasst sein (spezielle Lattentaschen)
- Traveller-Verstellung eingeschränkt
- Reparatur/Service aufwendig

### 2.8 Reefing-Varianten im Überblick

#### 2.8.1 Bindereff (Slab Reefing, traditionell)

Das klassische Bindereff verwendet vorgefertigte Reffpunkte (typisch 1–3)
im Segel. Das Segel wird durch Fieren des Falls auf die gewünschte Reffhöhe
gebracht, dann werden Reffleine (Vorliek) und Reffausholer (Achterliek)
durchgesetzt. Das überschüssige Segeltuch wird mit Reffbändseln am Baum
gesichert.

**Reffpunkt-Positionen:**
| Reff | Segelflächenreduktion | Position (% von P) |
|------|----------------------|-------------------|
| 1. Reff | 15–20 % | 20–25 % |
| 2. Reff | 30–40 % | 40–45 % |
| 3. Reff | 50–60 % | 55–65 % |

#### 2.8.2 Einleinen-Reff (Single-Line Reefing)

Eine einzelne Leine pro Reffpunkt führt sowohl den Vorliek-Reffhaken als
auch den Achterliek-Reffausholer. Bedienung aus dem Cockpit möglich.

**Systeme:**
- Harken Single-Line: Blöcke im Baum, Rückführung zum Cockpit
- Antal Easyreff: Kompaktes System mit integrierten Umlenkungen
- Seldén: Integriert in Seldén-Bäume

#### 2.8.3 Zweileinen-Reff (Two-Line Reefing)

Getrennte Leinen für Vorliek (Cunningham/Tack Hook) und Achterliek (Clew
Outhaul). Mehr Kontrolle, aber zwei Bedienvorgänge pro Reff.

**Vor- und Nachteile aller Reff-Systeme:**

| System | Einfachheit | Kontrolle | Kosten | Empfehlung |
|--------|-------------|-----------|--------|-----------|
| Traditionell (Bändseln) | ★★☆☆☆ | ★★★★★ | € 200–500 | Langfahrt, Puristen |
| Einleinen | ★★★★★ | ★★★☆☆ | € 800–2.500 | Shorthanded, Charter |
| Zweileinen | ★★★★☆ | ★★★★☆ | € 600–1.800 | Performance-Cruiser |
| In-Mast-Roll | ★★★★☆ | ★★☆☆☆ | € 5.000–15.000 | Komfort-Cruiser |
| In-Boom-Roll | ★★★★☆ | ★★★☆☆ | € 6.000–25.000 | Semi-Custom ab 40 ft |

---

## 3. Materialien

### 3.1 Dacron (Polyester-Gewebe)

#### 3.1.1 Grundlagen

Dacron ist die Handelsbezeichnung für gewebtes Polyester-Filament (PET,
Polyethylenterephthalat). Es ist das Standard-Segelmaterial für Fahrtenyachten
weltweit und deckt ca. 65–70 % des Gesamtmarktes ab.

#### 3.1.2 Webarten

**Taffeta (einfache Leinwandbindung):**
- Kett- und Schussfäden kreuzen sich 1:1
- Gleichmäßige Festigkeit in beide Richtungen
- Leichtere Gewichte (100–180 g/m²)
- Für kleinere Segel und Leichtwind

**Fill-orientiert (Schuss-dominant):**
- Verstärkte Schussfäden (quer zur Webrichtung)
- Bessere Festigkeit in Querrichtung
- Standard für Cross-Cut-Großsegel
- Typisch 200–350 g/m²

**Warp-orientiert (Kette-dominant):**
- Verstärkte Kettfäden (längs zur Webrichtung)
- Für radiale Schnittmuster
- Bessere Dehnung entlang der Lastpfade

#### 3.1.3 Gewichtsklassen

| Gewicht (g/m²) | oz/yd² | Bootsgröße | Windbereich | Einsatz |
|----------------|--------|------------|-------------|---------|
| 130–160 | 3.8–4.7 | 24–30 ft | 0–15 kn | Leichtwind-Großsegel |
| 170–210 | 5.0–6.2 | 28–34 ft | 5–25 kn | Standard-Großsegel |
| 220–270 | 6.5–8.0 | 33–40 ft | 5–30 kn | Standard-Großsegel |
| 280–340 | 8.2–10.0 | 38–48 ft | 8–35 kn | Schwerwetter-Großsegel |
| 350–420 | 10.3–12.4 | 45–60 ft | 10–40 kn | Hochsee-Großsegel |

#### 3.1.4 Qualitätsstufen

**Standard-Dacron:**
- Bainbridge, Challenge, Dimension Polyant Standard
- Dehnung: 1,5–3,0 %
- UV-Beständigkeit: Gut (5–8 Jahre)
- Preis: € 12–20/m²
- Lebensdauer: 5–8 Saisons

**Premium-Dacron:**
- Dimension Polyant D4, Contender CX, Bainbridge Premium
- Engeres Gewebe, mehr Harzimprägnierung (Finish)
- Dehnung: 1,0–2,0 %
- UV-Beständigkeit: Sehr gut (7–10 Jahre)
- Preis: € 20–35/m²
- Lebensdauer: 7–12 Saisons

**Racing-Dacron:**
- Dimension Polyant WB, Contender Hydra Net Dacron
- Maximal imprägniert, steifste Ausführung
- Dehnung: 0,8–1,5 %
- UV-Beständigkeit: Gut (5–7 Jahre, Finish kann brechen)
- Preis: € 30–50/m²
- Lebensdauer: 4–7 Saisons

### 3.2 Pentex (PEN — Polyethylennaphthalat)

#### 3.2.1 Eigenschaften

Pentex ist ein verbessertes Polyester mit ca. 30 % höherem Elastizitätsmodul.
Es wird sowohl als Gewebe als auch als Verstärkungsfaser in Laminaten verwendet.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,8–1,5 % |
| UV-Beständigkeit | Sehr gut (vergleichbar Dacron) |
| Knickfestigkeit | Gut |
| Lebensdauer | 6–10 Saisons |
| Preis | € 35–55/m² |
| Farbe | Naturbraun/bronze |

#### 3.2.2 Einsatzbereich

Pentex ist die ideale Wahl für Performance-Cruiser:
- Bessere Formhaltung als Dacron
- Deutlich bessere UV-Beständigkeit als Aramide
- Gute Knickfestigkeit (Lattentaschen, Rollen)
- "Dacron-ähnliches" Handling mit besserer Performance

### 3.3 Technora

#### 3.3.1 Eigenschaften

Technora ist ein co-polyamid Aramid von Teijin (Japan), das spezifisch für
maritime Anwendungen entwickelt wurde. Es bietet deutlich bessere UV- und
Feuchtigkeitsbeständigkeit als Kevlar.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,4–0,8 % |
| UV-Beständigkeit | Mäßig (besser als Kevlar, schlechter als Dacron) |
| Bruchfestigkeit | 3,0 GPa |
| Knickfestigkeit | Mäßig |
| Lebensdauer | 5–8 Saisons (Fahrt), 3–5 (Regatta) |
| Preis | € 50–80/m² (als Laminat) |
| Farbe | Gold/bronze |

#### 3.3.2 Anwendung

- Verstärkungsfaser in Laminatsegeln
- Hauptfaser in Radial-Großsegeln
- Hersteller: Dimension Polyant (DSL-Laminat), Contender

### 3.4 Kevlar (Aramid)

#### 3.4.1 Eigenschaften

Kevlar (DuPont) war die erste Hochleistungsfaser im Segelbau. Heute
weitgehend durch Technora, Dyneema und Carbon ersetzt.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,3–0,6 % |
| UV-Beständigkeit | Schlecht (2–4 Jahre ohne Schutz) |
| Bruchfestigkeit | 3,6 GPa |
| Knickfestigkeit | Schlecht (bricht bei engem Radius) |
| Lebensdauer | 3–5 Saisons |
| Preis | € 45–70/m² |
| Farbe | Gelb |

**Warum Kevlar problematisch ist:**
- UV-Degradation: Kevlar verliert 30–50 % der Festigkeit nach 3 Jahren UV-Exposition
- Knickempfindlichkeit: Jede scharfe Falte reduziert die lokale Festigkeit um 20–40 %
- Feuchtigkeitsaufnahme: 4–7 % Wasseraufnahme → Gewichtszunahme

### 3.5 Carbon (Kohlenstofffaser)

#### 3.5.1 Eigenschaften

Kohlenstofffaser bietet das beste Festigkeits-zu-Dehnungs-Verhältnis aller
Segelfasern. Im Regattasegeln Standard, im Fahrtensegeln zunehmend verbreitet.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,2–0,5 % |
| UV-Beständigkeit | Ausgezeichnet |
| Bruchfestigkeit | 3,5–7,0 GPa (je nach Typ) |
| Elastizitätsmodul | 230–400 GPa |
| Knickfestigkeit | Schlecht (spröde Faser) |
| Lebensdauer | 5–10 Saisons (Fahrt), 2–4 (Regatta) |
| Preis | € 80–180/m² |
| Farbe | Schwarz |

#### 3.5.2 Carbon-Typen im Segelbau

- **Standard Modulus (SM)**: 230 GPa, gute Knickfestigkeit, Fahrtensegeln
- **Intermediate Modulus (IM)**: 290 GPa, Regatta-Cruising
- **High Modulus (HM)**: 350–400 GPa, reiner Regattaeinsatz
- **Spread Tow**: Flach ausgebreitete Faserbündel, dünnere Laminate möglich

### 3.6 Dyneema / Spectra (UHMWPE)

#### 3.6.1 Eigenschaften

Dyneema (DSM, Niederlande) und Spectra (Honeywell, USA) sind Ultra-High-
Molecular-Weight-Polyethylen-Fasern (UHMWPE). Extrem leicht und fest,
aber mit dem Problem des Kriechens (Creep) unter Dauerlast.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,5–1,0 % (initial), Creep: 1–3 % über Lebensdauer |
| UV-Beständigkeit | Gut |
| Bruchfestigkeit | 3,5 GPa |
| Dichte | 0,97 g/cm³ (schwimmt auf Wasser!) |
| Knickfestigkeit | Ausgezeichnet |
| Lebensdauer | 5–8 Saisons |
| Preis | € 60–120/m² |
| Farbe | Weiß |

#### 3.6.2 Creep-Problematik

Dyneema/Spectra-Fasern "kriechen" unter Dauerlast — sie dehnen sich
irreversibel, auch unter Lasten weit unter der Bruchfestigkeit:
- Bei 30 % der Bruchfestigkeit: ca. 0,5 % Creep nach 1.000 Stunden
- Bei 50 % der Bruchfestigkeit: ca. 1,5 % Creep nach 1.000 Stunden
- Ergebnis: Segel wird mit der Zeit "beulig" und verliert das Profil

**Gegenmaßnahmen:**
- Segel nicht permanent gesetzt lassen
- Lastpfade mit Carbon oder Technora verstärken
- Neuere Dyneema-Typen (SK99, DM20) mit reduziertem Creep verwenden

### 3.7 Vectran (LCP — Liquid Crystal Polymer)

#### 3.7.1 Eigenschaften

Vectran (Kuraray, Japan) ist ein flüssigkristallines Polymer mit
hervorragender Formstabilität und minimalem Creep.

| Eigenschaft | Wert |
|-------------|------|
| Dehnung | 0,3–0,7 % |
| UV-Beständigkeit | Schlecht (ähnlich Kevlar) |
| Bruchfestigkeit | 3,0 GPa |
| Creep | Nahezu null |
| Knickfestigkeit | Mäßig |
| Lebensdauer | 4–7 Saisons |
| Preis | € 55–90/m² |
| Farbe | Gold/braun |

#### 3.7.2 Anwendung

- Ideale Kombination mit Dyneema (Vectran für Formstabilität, Dyneema für
  Knickfestigkeit und UV-Schutz)
- Standard-Verstärkungsfaser in vielen Laminaten
- North Sails 3Di S-Serie verwendet Vectran als Primärfaser

### 3.8 Mylar (PET-Folie)

#### 3.8.1 Eigenschaften

Mylar ist eine biaxial orientierte Polyester-Folie, die als Trägerschicht
in Laminatsegeln dient. Mylar selbst ist keine Segelfaser, sondern die
"Matrix", in die Verstärkungsfasern eingebettet werden.

| Eigenschaft | Wert |
|-------------|------|
| Dicke | 12–75 µm |
| UV-Beständigkeit | Mäßig (wird spröde) |
| Lebensdauer | 4–8 Saisons |
| Funktion | Trägerfolie, Feuchtigkeitsbarriere |

#### 3.8.2 Delaminationsproblem

Die Verbindung zwischen Mylar-Folie und Taffeta-Gewebe bzw. Verstärkungsfasern
ist die Schwachstelle aller Laminatsegel. Ursachen für Delamination:
- UV-Degradation des Klebers
- Mechanische Ermüdung (Knicken, Flattern)
- Feuchtigkeitseintritt an den Kanten
- Chemische Degradation (Salzwasser, Diesel)

### 3.9 Hydra Net / DCF (Dyneema Composite Fabric)

#### 3.9.1 Beschreibung

Hydra Net (Dimension Polyant) und DCF (Dyneema Composite Fabric, ehemals
"Cuben Fiber") sind ultraleichte Laminate aus Dyneema-Fasern zwischen
dünnen Mylar- oder Polyester-Folien.

| Eigenschaft | Wert |
|-------------|------|
| Gewicht | 30–120 g/m² |
| Dehnung | 0,3–0,8 % |
| UV-Beständigkeit | Gut (Dyneema-seitig) |
| Knickfestigkeit | Mäßig |
| Lebensdauer | 4–7 Saisons |
| Preis | € 80–200/m² |

#### 3.9.2 Einsatz

- Regatta-Großsegel für Daysailer und Sportboote
- Ultratleichtwind-Segel
- Code-Segel und asymmetrische Spinnaker
- Nicht empfohlen für In-Mast oder In-Boom (zu knickempfindlich)

### 3.10 North 3Di

#### 3.10.1 Technologie

3Di (Three-Dimensional Design, Development, and Delivery) ist North Sails'
proprietäre Membrantechnologie. Filamente werden auf einem dreidimensionalen
Formkern abgelegt und unter Hitze und Druck zu einem monolithischen Segel
verschmolzen.

#### 3.10.2 Produktlinien

| Linie | Faser | Zielgruppe | Dehnung | Preis/m² | Lebensdauer |
|-------|-------|------------|---------|----------|-------------|
| 3Di RAW | Carbon HM | Grand-Prix-Regatta | 0,15–0,25 % | € 250–400 | 2–4 Saisons |
| 3Di NORDAC | Carbon SM + Dyneema | Performance Cruising | 0,25–0,40 % | € 150–250 | 6–10 Saisons |
| 3Di NPC (N. Perf. Cruising) | Carbon + Taffeta | Fahrtensegeln | 0,35–0,50 % | € 120–180 | 8–12 Saisons |
| 3Di ENDURE | Dyneema + Taffeta | Langfahrt | 0,40–0,60 % | € 100–150 | 10–15 Saisons |

#### 3.10.3 Vor- und Nachteile

**Vorteile:**
- Durchgehende Fasern (keine Nähte als Schwachstellen)
- Computeroptimierte Faserverteilung
- Dreidimensionale Formgebung (eingebautes Profil)
- Ausgezeichnete Formstabilität über die Lebensdauer
- Flexibel genug für Rollreff (3Di ENDURE)

**Nachteile:**
- Nur über North Sails-Lofts verfügbar
- Hohe Kosten (2–4× Dacron)
- Reparatur nur durch zertifizierte Lofts
- Keine lokale Reparatur möglich (muss eingeschickt werden)
- Proprietäre Technologie → Monopolstellung

### 3.11 EPEX (Elvström)

#### 3.11.1 Technologie

EPEX ist Elvström Sails' Membrantechnologie. Ähnlich wie 3Di werden Fasern
auf einem 3D-Formkern abgelegt, jedoch mit einem anderen Verklebungsprozess
(Epoxy-basiert statt thermisch).

#### 3.11.2 Produktlinien

| Linie | Faser | Zielgruppe | Preis/m² | Lebensdauer |
|-------|-------|------------|----------|-------------|
| EPEX Racing | Carbon HM | Regatta | € 200–350 | 3–5 Saisons |
| EPEX Performance | Carbon + Technora | Perf. Cruising | € 130–220 | 6–9 Saisons |
| EPEX Cruising | Technora + Dyneema | Fahrtensegeln | € 90–160 | 8–12 Saisons |
| EPEX Cruising Plus | Dyneema + Taffeta | Langfahrt | € 80–130 | 10–14 Saisons |

### 3.12 Doyle Stratis

#### 3.12.1 Technologie

Stratis ist Doyle Sails' proprietäres Membransystem. Fasern werden zwischen
laminierte Folien gelegt und in spezifischen Winkeln ausgerichtet.

#### 3.12.2 Produktlinien

| Linie | Beschreibung | Preis/m² | Lebensdauer |
|-------|-------------|----------|-------------|
| Stratis ICE | Carbon, Grand-Prix | € 220–380 | 2–4 Saisons |
| Stratis GTi | Carbon + Technora, Performance | € 140–240 | 5–8 Saisons |
| Stratis Delta | Technora + Dyneema, Cruising | € 90–160 | 7–11 Saisons |
| Stratis GP | Pentex, Einsteiger-Performance | € 70–120 | 6–10 Saisons |

### 3.13 Materialvergleichstabelle

| Material | Dehnung (%) | UV | Knick | Creep | Leben (J.) | €/m² | Empfehlung |
|----------|-------------|-----|-------|-------|-----------|------|-----------|
| Dacron Standard | 1,5–3,0 | ★★★★★ | ★★★★★ | Nein | 5–8 | 12–20 | Einsteiger, Charter |
| Dacron Premium | 1,0–2,0 | ★★★★★ | ★★★★★ | Nein | 7–12 | 20–35 | Fahrtenyachten |
| Pentex | 0,8–1,5 | ★★★★☆ | ★★★★☆ | Nein | 6–10 | 35–55 | Perf.-Cruiser |
| Technora | 0,4–0,8 | ★★★☆☆ | ★★★☆☆ | Nein | 5–8 | 50–80 | Regatta-Cruiser |
| Carbon | 0,2–0,5 | ★★★★★ | ★★☆☆☆ | Nein | 5–10 | 80–180 | Regatta |
| Dyneema | 0,5–1,0 | ★★★★☆ | ★★★★★ | Ja | 5–8 | 60–120 | Cruiser (mit Vorsicht) |
| Vectran | 0,3–0,7 | ★★☆☆☆ | ★★★☆☆ | Nein | 4–7 | 55–90 | Kombination |
| DCF/Hydra Net | 0,3–0,8 | ★★★★☆ | ★★★☆☆ | Ja | 4–7 | 80–200 | Regatta, ultra-leicht |
| 3Di NORDAC | 0,25–0,40 | ★★★★☆ | ★★★★☆ | Min. | 6–10 | 150–250 | Perf.-Cruiser |
| 3Di ENDURE | 0,40–0,60 | ★★★★★ | ★★★★★ | Min. | 10–15 | 100–150 | Langfahrt |
| EPEX Cruising | 0,35–0,55 | ★★★★☆ | ★★★★☆ | Min. | 8–12 | 90–160 | Fahrt |
| Stratis Delta | 0,35–0,50 | ★★★★☆ | ★★★★☆ | Min. | 7–11 | 90–160 | Fahrt |

---

## 4. Konstruktion und Schnitt

### 4.1 Schnittmuster (Panelayout)

#### 4.1.1 Cross-Cut (Horizontalschnitt)

Das älteste und häufigste Schnittmuster. Die Stoffbahnen verlaufen
horizontal (parallel zum Unterliek). Die Fill-Richtung (Schuss) liegt
annähernd entlang der Hauptlastpfade.

**Konstruktionsprinzip:**
- Stoffbahnen werden mit Broadseams (gekrümmten Nähten) verbunden
- Die Krümmung der Broadseams erzeugt das dreidimensionale Profil
- Maximale Broadseam-Tiefe typisch 20–40 mm pro Bahn
- Bahnenbreite: 900–1.400 mm (je nach Tuchmaterial)

**Vorteile:**
- Einfachste und kostengünstigste Fertigung
- Bewährt über Jahrzehnte
- Gute Ergebnisse mit Dacron
- Einfache Reparatur (Bahnen einzeln austauschbar)
- Material effizient (wenig Verschnitt)

**Nachteile:**
- Lastpfade nicht optimal mit Faserrichtung ausgerichtet
- Höhere Dehnung in Diagonalrichtung (Bias Stretch)
- Profilverlust schneller als bei Radialschnitt
- Nicht optimal für Hochleistungsmaterialien

#### 4.1.2 Tri-Radial-Schnitt

Die Stoffbahnen strahlen von den drei Ecken des Segels (Kopf, Hals,
Schothorn) radial aus. Die Faserrichtung folgt annähernd den Lastpfaden.

**Konstruktionsprinzip:**
- Drei Sektionen: Kopfsektor, Halssektor, Schothorn-Sektor
- Bahnen in jeder Sektion strahlen vom jeweiligen Eckpunkt aus
- Übergangszone zwischen den Sektionen (Fan Zone)
- Broadseams erzeugen das Profil in jeder Sektion

**Vorteile:**
- Bessere Ausrichtung Faser↔Lastpfad
- Geringere Bias-Dehnung
- Längere Profilhaltung
- Bessere Leistung bei höheren Windstärken
- Ideal für Pentex und Technora

**Nachteile:**
- Aufwendigere Fertigung (mehr Nähte)
- Höherer Materialverschnitt (15–25 %)
- Mehr Nähte = mehr potenzielle Schwachstellen
- Teurer als Cross-Cut (20–40 % Aufpreis)

#### 4.1.3 Radial-Schnitt (Vollradial)

Alle Bahnen strahlen von einem einzelnen Punkt (meist dem Kopf) radial
nach unten aus. Selten bei Großsegeln, häufiger bei Vorsegeln.

**Vorteile:**
- Optimale Lastverteilung vom Kopfpunkt
- Minimale Bias-Dehnung
- Gute Profilkontrolle im oberen Segel

**Nachteile:**
- Sehr hoher Materialverschnitt
- Komplexe Fertigung
- Teuer
- Suboptimale Faserausrichtung im unteren Bereich

#### 4.1.4 Membran / Molded (Geformte Segel)

Keine geschnittenen Bahnen — stattdessen werden Fasern direkt auf einen
dreidimensionalen Formkern aufgebracht und verklebt/verschmolzen.

**Technologien:**
- North 3Di: Filamente auf 3D-Form, thermisch verschmolzen
- Elvström EPEX: Fasern auf 3D-Form, Epoxy-verklebt
- Doyle Stratis: Fasern zwischen Folien, auf Form gepresst
- UK Sailmakers X-Drive: Tape-Streifen auf Trägerfolie
- OneSails 4T FORTE: Fasern zwischen Taffeta-Schichten

**Vorteile:**
- Computeroptimierte Faserverteilung
- Keine Nähte (höchste Integrität)
- Dreidimensionales Profil ab Werk
- Minimale Dehnung
- Längste Profilhaltung

**Nachteile:**
- Hohe Kosten
- Reparatur nur durch Hersteller
- Proprietäre Technologien
- Begrenzte Verfügbarkeit (Wartezeiten)

### 4.2 Broadseaming und Profilgebung

#### 4.2.1 Was ist Broadseaming?

Broadseaming ist die Technik, bei der die Nähte zwischen Stoffbahnen
nicht gerade, sondern gekrümmt verlaufen. Diese Krümmung (Broadseam)
"nimmt Material weg" und erzeugt so die dreidimensionale Form (Draft,
Bauch, Profil) des Segels.

#### 4.2.2 Profilparameter

| Parameter | Beschreibung | Typischer Wert |
|-----------|-------------|----------------|
| Draft (Tiefe) | Maximale Profiltiefe in % der Sehnenlänge | 8–15 % |
| Draft Position | Position der max. Tiefe, gemessen vom Vorliek | 35–50 % |
| Entry Angle | Eintrittswinkel am Vorliek | 15–30° |
| Exit Angle | Austrittswinkel am Achterliek | 3–8° |
| Twist | Verdrehung des Profils von unten nach oben | 5–15° |

#### 4.2.3 Profilverteilung über die Segelhöhe

| Höhe (% von P) | Draft | Draft Position | Anmerkung |
|-----------------|-------|---------------|-----------|
| 0–25 % (Fuß) | 10–14 % | 40–48 % | Tiefster Bauch, steuert Luvgierigkeit |
| 25–50 % | 10–13 % | 38–45 % | Hauptantriebsbereich |
| 50–75 % | 8–11 % | 35–42 % | Zunehmend flacher |
| 75–100 % (Kopf) | 6–9 % | 33–40 % | Flachstes Profil, Twist-Zone |

### 4.3 Vorliek-Kurve (Luff Curve)

#### 4.3.1 Funktion

Die Vorliek-Kurve (Luff Curve, Luff Round) ist die konvexe Krümmung des
Vorlieks relativ zur geraden Verbindung Kopf–Hals. Wenn das Vorliek an
einem geraden Mast befestigt wird, wird das überschüssige Material ins
Segel hineingedrückt und erzeugt Profiltiefe.

#### 4.3.2 Interaktion mit Mastbiegung

| Mast | Luff Curve | Segelbauch | Anmerkung |
|------|-----------|------------|-----------|
| Gerade | Positiv | Tief | Standard-Zustand |
| Leicht gebogen | Positiv | Mittel | Optimaler Trimmbereich |
| Stark gebogen | Positiv | Flach | Starkwind-Trimm |
| Überbogen | Positiv | Invertiert | Falten parallel zum Mast (zu viel!) |

Die Luff Curve muss auf den Masttyp abgestimmt sein:
- **Steifer Mast** (Fahrtenyacht): Geringere Luff Curve (30–60 mm bei 15 m P)
- **Flexibler Mast** (Regatta): Stärkere Luff Curve (60–120 mm bei 15 m P)

### 4.4 Achterliek: Hollow vs. Roach

#### 4.4.1 Definitionen

- **Hollow (hohl)**: Das Achterliek ist konkav — es liegt innerhalb der
  geraden Verbindung Kopf–Schothorn. Typisch: -2 bis -5 %.
- **Gerade**: Das Achterliek folgt der geraden Linie Kopf–Schothorn.
- **Roach (konvex)**: Das Achterliek ist konvex — es ragt über die gerade
  Linie hinaus. Typisch: +5 bis +25 %.

#### 4.4.2 Roach und Latten

Roach erfordert Latten, die das überstehende Segeltuch stützen:
- **Keine Latten**: Maximal 0–3 % Roach
- **Teillatten**: Maximal 8–15 % Roach
- **Volllatten**: Maximal 15–25 % Roach
- **Square-Top + Volllatten**: Maximal 20–30 % Roach

Mehr Roach = mehr Segelfläche = mehr Leistung, aber auch:
- Mehr Gewicht (Latten, Material)
- Höherer Druckpunkt
- Mehr Belastung auf Rigg
- Komplexeres Handling

#### 4.4.3 Leech Hollow für Rollreff

In-Mast-Rollreff-Segel erfordern ein hohles Achterliek (-2 bis -5 %),
damit sich das Segel gleichmäßig aufrollen lässt. Jede konvexe Roach
würde beim Einrollen Falten und Verklemmungen erzeugen.

### 4.5 Latten (Battens)

#### 4.5.1 Volllatten vs. Teillatten

| Merkmal | Volllatte | Teillatte |
|---------|-----------|-----------|
| Länge | 80–100 % der Segelbreite | 20–40 % der Segelbreite |
| Funktion | Profil + Roach-Stützung | Nur Achterliek-Stützung |
| Anzahl | 3–5 | 2–4 |
| Gewicht/Stk | 200–800 g | 50–200 g |
| Material | GFK oder CFK | GFK oder Kunststoff |
| Profil | Konisch (steifer am Vorliek) | Gleichmäßig |

#### 4.5.2 Lattenmaterial im Detail

**Glasfaser (GFK):**
- Standard-Material für Fahrtensegel
- Elastisch, bruchsicher (biegt, bricht nicht)
- Gewicht: 150–300 g/m (je nach Querschnitt)
- Kosten: € 15–35 pro Latte
- Lebensdauer: 5–8 Jahre

**Carbon (CFK):**
- Leichter und steifer als GFK
- Gewicht: 80–150 g/m
- Kosten: € 60–150 pro Latte
- Bruchgefahr bei Überbelastung (bricht spröde)
- Empfohlen für obere Latten und Square-Top-Segel
- Lebensdauer: 8–12 Jahre (wenn nicht gebrochen)

**Hybrid (GFK-Kern, CFK-Mantel):**
- Kombination aus Steifigkeit und Bruchsicherheit
- Gewicht zwischen GFK und CFK
- Kosten: € 40–80 pro Latte
- Zunehmend beliebt für Fahrtensegel

### 4.6 Kopfbrett (Headboard)

#### 4.6.1 Typen

- **Starres Kopfbrett** (Standard): Aluminium oder Kunststoff, 100–300 mm breit
- **Weiches Kopfbrett** (Soft Head): Nur Verstärkungslagen, kein starres Brett
- **Square-Top-Kopfbrett**: Breites Brett (300–600 mm) mit Carbon-Oberlatte
- **Racing-Kopfbrett**: Minimal, oft nur Öse mit Verstärkung

#### 4.6.2 Belastungen

Das Kopfbrett überträgt die gesamte Fall-Last in das Segel. Typische
Belastungen:

| Bootsgröße | Fall-Last (max) |
|-----------|----------------|
| 30 ft | 800–1.500 kg |
| 35 ft | 1.200–2.200 kg |
| 40 ft | 1.800–3.500 kg |
| 45 ft | 2.500–5.000 kg |
| 50 ft | 3.500–7.000 kg |

### 4.7 Cunningham-Integration

#### 4.7.1 Funktion

Die Cunningham (auch Cunningham-Strecker) ist eine Leine oder ein System,
das den Vorliekstrecker des Großsegels bedient. Sie zieht das Vorliek
nach unten und verschiebt den tiefsten Punkt des Segelprofils nach vorne.

#### 4.7.2 Ausführungen

- **Öse im Segel**: Standard, Cunningham-Leine durch Öse, zurück auf Deck
- **Integrierter Block**: Öse mit eingebautem Umlenkblock
- **Durch-Baum-Führung**: Leine läuft durch den Baum zum Cockpit
- **Hydraulisch** (Regatta/Superyacht): Hydraulikzylinder am Mastfuß

#### 4.7.3 Position der Cunningham-Öse

Die Cunningham-Öse befindet sich typischerweise 300–600 mm über dem Hals,
im Bereich der Vorliek-Verstärkung. Sie muss mindestens für die doppelte
Fall-Last ausgelegt sein, da die Cunningham-Kräfte additiv zu den
Fall-Kräften wirken.

### 4.8 Segelverstärkungen

#### 4.8.1 Eckenverstärkungen

| Ecke | Verstärkungsfläche | Material | Schichten |
|------|-------------------|----------|-----------|
| Kopf | 200×200 – 400×400 mm | Dacron 350+ g/m² | 4–8 |
| Hals | 300×300 – 500×500 mm | Dacron 350+ g/m² | 4–8 |
| Schothorn | 300×300 – 600×600 mm | Dacron 350+ g/m² | 6–12 |
| Reffhals (1. Reff) | 200×200 – 350×350 mm | Dacron 300+ g/m² | 3–6 |
| Reff-Schothorn (1. Reff) | 200×200 – 400×400 mm | Dacron 300+ g/m² | 4–8 |

#### 4.8.2 Nahtverstärkung

- **Leech Line**: Dünne Leine (2–3 mm) im Achterliek-Saum zur Kontrolle des Flatterns
- **Foot Line**: Leine im Unterliek-Saum
- **Boltrope**: Vorliektau (6–12 mm) — trägt die gesamte Vorlieklast
- **UV-Schutzstreifen**: Dacron-Streifen (80–150 mm breit) am Achterliek und Unterliek

---

## 5. Trimm

### 5.1 Grundlagen des Großsegeltrimms

Der Großsegeltrimm beeinflusst vier Hauptparameter:
1. **Profiltiefe** (Draft): Wie tief ist der Bauch des Segels?
2. **Profilposition** (Draft Position): Wo sitzt der tiefste Punkt?
3. **Twist**: Wie stark dreht sich das Profil von unten nach oben auf?
4. **Anstellwinkel** (Angle of Attack): In welchem Winkel trifft der Wind?

### 5.2 Trimminstrumente im Detail

#### 5.2.1 Großschot (Mainsheet)

**Funktion:** Kontrolliert primär den Twist und sekundär den Anstellwinkel.

**Dichtholen (Schot dicht):**
- Reduziert Twist
- Achterliek wird geschlossener
- Obere Telltales stehen (nicht killen)
- Boot zeigt zum Wind (Luvgierigkeit nimmt zu)
- Krängung nimmt zu

**Fieren (Schot los):**
- Erhöht Twist
- Achterliek öffnet sich
- Obere Telltales killen
- Boot fällt ab
- Krängung nimmt ab

**Trimmregel:** Die Großschot ist das am häufigsten verstellte Element.
In böigem Wind wird ständig nachgetrimmt (Traveller oder Schot).

#### 5.2.2 Baumniederholer / Kicker (Vang)

**Funktion:** Kontrolliert die Achterliekspannung (Twist) unabhängig
von der Großschotsstellung. Besonders wichtig auf Raumschots- und
Vorwindkursen, wo die Großschot nicht mehr nach unten zieht.

**Typen:**
| Typ | Übersetzung | Bootsgröße | Preis |
|-----|------------|------------|-------|
| Flaschenzug (Talje) | 4:1 – 8:1 | 24–35 ft | € 150–500 |
| Gasdruckfeder + Talje | 4:1 – 6:1 | 30–42 ft | € 400–1.200 |
| Hydraulisch (Seldén Rodkicker) | Stufenlos | 30–55 ft | € 1.500–5.000 |
| Solid Vang (starr) | Mechanisch | 28–50 ft | € 600–2.500 |

**Trimmregel Kicker:**
- Am Wind: Kicker nur leicht unter Spannung (Schot übernimmt Twist-Kontrolle)
- Halbwind: Kicker zunehmend wichtig (Schot horizontal)
- Raumschots: Kicker dominiert die Twist-Kontrolle
- Vorwind: Kicker verhindert, dass der Baum nach oben steigt (gefährlich!)

#### 5.2.3 Cunningham

**Funktion:** Verschiebt die Profiltiefe nach vorne, ohne die
Achterliekspannung zu verändern.

**Dichtholen:**
- Profil wandert nach vorne (Eintrittswinkel wird kleiner)
- Vorliek wird straffer (Falten am Vorliek verschwinden)
- Leichte Abflachung des Gesamtprofils
- Sinnvoll bei zunehmend Wind (15+ Knoten)

**Fieren:**
- Profil wandert nach achtern
- Vorliek lockerer
- Segel wird voller (mehr Draft)
- Sinnvoll bei Leichtwind

**Trimmregel:** Cunningham nur bei auflandigem Wind und unter Spannung
setzen, wenn Horizontalfalten am Vorliek auftreten. Im Leichtwind
komplett los.

#### 5.2.4 Outhaul (Unterliekstrecker)

**Funktion:** Kontrolliert die Profiltiefe im unteren Segeldrittel
durch Spannung/Lockerung des Unterlieks.

**Dichtholen:**
- Unterliek wird flach
- Fußbereich wird enger am Baum
- Weniger Widerstand
- Sinnvoll: Am Wind, Starkwind

**Fieren:**
- Unterliek wird bauchiger
- "Bauch" im Fußbereich
- Mehr Antrieb bei Leichtwind
- Sinnvoll: Leichtwind, Raumschots

**Systeme:**
- Intern durch Baum geführt (Standard)
- Extern über Block am Baumende
- Hydraulisch (Performance/Superyacht)
- Elektrische Winch (Superyacht)

#### 5.2.5 Traveller

**Funktion:** Kontrolliert den Anstellwinkel des Großsegels, ohne den
Twist zu verändern. Verschiebt den Schot-Angriffspunkt quer zum Boot.

**Luv fahren:**
- Segel wird flacher zum Boot gezogen (ohne Twist-Änderung)
- Effektiv: Segeldruckpunkt näher zur Mittellinie
- Weniger Lee-Helm
- Besonders bei Leichtwind sinnvoll

**Lee fahren:**
- Segeldruckpunkt weiter in Lee
- Schnelles Fieren bei Böen (statt Schot fieren → ändert Twist nicht)
- Effektiv für Böenmanagement

**Typen:**
| Typ | Bootsgröße | Preis |
|-----|------------|-------|
| Ball-Bearing, schienenmontiert | 25–40 ft | € 400–1.500 |
| Rollen-Traveller, Doppelschiene | 35–55 ft | € 800–3.000 |
| Hydraulischer Traveller | 45–80 ft | € 3.000–12.000 |
| Athwartship Traveller (am Cockpit) | 28–50 ft | € 600–2.500 |

#### 5.2.6 Achterstag (Backstay)

**Funktion:** Biegt den Mast nach achtern, was die Vorliek-Kurve
entlastet und das Großsegel abflacht.

**Dichtholen:**
- Mast biegt nach achtern
- Großsegel wird flacher
- Achterliek öffnet sich leicht
- Sinnvoll: Starkwind, Höhe laufen

**Fieren:**
- Mast wird gerader
- Großsegel wird bauchiger
- Achterliek schließt sich
- Sinnvoll: Leichtwind

**Achtung:** Nicht alle Yachten haben ein verstellbares Achterstag.
Fahrtenyachten mit festem Achterstag trimmen über Fall + Cunningham.

#### 5.2.7 Lattenspannung

**Funktion:** Beeinflusst die Profiltiefe und -form im Bereich der
jeweiligen Latte.

- **Mehr Spannung**: Flacheres Profil, Latte drückt gegen Vorliek
- **Weniger Spannung**: Tieferes Profil, Latte liegt lockerer
- **Optimale Spannung**: Latte beschreibt einen gleichmäßigen Bogen
  ohne harte Knicke oder Schlaffstellen

**Praxis:** Lattenspannung wird einmal eingestellt und nur selten
verändert (saisonale Kontrolle). Keine Verstellung während der Fahrt.

#### 5.2.8 Telltales (Trimmfäden)

**Position und Funktion:**
- **Vorliek-Telltales** (selten am Großsegel): Anströmung
- **Achterliek-Telltales**: Twist-Kontrolle
  - Typisch: 3 Stück, gleichmäßig verteilt
  - Alle strömen nach achtern = korrekt
  - Unterer killt = zu viel Twist
  - Oberer killt = zu wenig Twist (Achterliek zu geschlossen)
  - Oberer verschwindet hinter Segel = Achterliek zu geschlossen ("stalled")

**Trimmregel Telltales:**
- Am Wind: Oberer Telltale "bricht" gelegentlich (10–20 % der Zeit)
- Halbwind: Alle Telltales strömen gleichmäßig
- Raumschots: Telltales weniger aussagekräftig

### 5.3 Trimm nach Windstärke

#### 5.3.1 Leichtwind (0–8 Knoten)

| Element | Einstellung | Begründung |
|---------|------------|------------|
| Schot | Leicht | Twist zulassen für scheinbaren Wind oben |
| Traveller | Luv | Anstellwinkel erhöhen ohne Twist zu reduzieren |
| Cunningham | Los | Profil achterlich, maximale Tiefe |
| Outhaul | Los (30–50 % gefiert) | Unterliek bauchig für mehr Auftrieb |
| Kicker | Los | Kein Druck auf Achterliek |
| Achterstag | Los | Mast gerade, Segel voll |
| Fall | Mittlere Spannung | Keine Vorliekfalten |

**Ziel:** Maximale Profiltiefe, Profil weit achtern, viel Twist.
Boot aufrecht halten. Geschwindigkeit vor Höhe.

#### 5.3.2 Mittlerer Wind (8–16 Knoten)

| Element | Einstellung | Begründung |
|---------|------------|------------|
| Schot | Mittel bis dicht | Achterliek kontrolliert, mäßiger Twist |
| Traveller | Mittschiffs | Standardposition |
| Cunningham | Leicht | Profil leicht nach vorne |
| Outhaul | Mittel | Moderate Profiltiefe im Fuß |
| Kicker | Leicht unter Spannung | Achterliek-Kontrolle |
| Achterstag | Leicht | Mast leicht gebogen |
| Fall | Gute Spannung | Keine Falten, straffer Vorliek |

**Ziel:** Ausgewogenes Profil, Profil bei 40–45 % der Tiefe.
Höhe und Geschwindigkeit im Gleichgewicht.

#### 5.3.3 Starkwind (16–25 Knoten)

| Element | Einstellung | Begründung |
|---------|------------|------------|
| Schot | Fest (vor Reffen) | Twist minimieren |
| Traveller | Lee | Krängung reduzieren ohne Twist zu ändern |
| Cunningham | Voll dicht | Profil maximal nach vorne |
| Outhaul | Voll dicht | Fuß maximal flach |
| Kicker | Gespannt | Achterliek kontrolliert |
| Achterstag | Voll dicht | Mast maximal gebogen, Segel flach |
| Fall | Maximale Spannung | Straffes Vorliek |

**Ziel:** Flaches Profil, Profil weit vorne (35 %), offenes Achterliek.
Krängung minimieren. Luvseitiges Ruder reduzieren.

#### 5.3.4 Sturmstärke (25+ Knoten)

Ab 25 Knoten sollte grundsätzlich gerefft werden. Trimmreihenfolge
vor dem Reffen:

1. Traveller ganz nach Lee
2. Großschot fieren bis Achterliek-Telltales alle strömen
3. Wenn Boot noch zu viel krängt → 1. Reff
4. Bei weiter zunehmendem Wind → 2. Reff
5. Ab 35–40 Knoten → 3. Reff oder Trysegel

### 5.4 Trimm nach Kurs

#### 5.4.1 Hoch am Wind (Close-Hauled, 30–45°)

- Traveller: Luv oder Mitte
- Schot: Dicht (wenig Twist)
- Kicker: Leichte Spannung
- Profil: Flach bis mittel (8–12 %)
- Fokus: Höhe laufen, Achterliek kontrolliert schließen

#### 5.4.2 Am Wind (Close Reach, 45–60°)

- Traveller: Mitte
- Schot: Mittel
- Kicker: Gespannt
- Profil: Mittel (10–13 %)
- Fokus: Geschwindigkeit, ausgewogenes Profil

#### 5.4.3 Halbwind (Beam Reach, 60–90°)

- Traveller: Mitte bis leicht Lee
- Schot: Gefiert
- Kicker: Übernimmt Twist-Kontrolle
- Profil: Mittel bis tief (11–14 %)
- Fokus: Geschwindigkeit maximieren

#### 5.4.4 Raumschots (Broad Reach, 90–150°)

- Traveller: Ganz Lee
- Schot: Weit gefiert
- Kicker: Hauptkontrollelement für Twist
- Profil: Tief (12–15 %)
- Cunningham: Los
- Outhaul: Los
- Fokus: Segelfläche maximieren, kein Sonnenschuss

#### 5.4.5 Vorwind (Run, 150–180°)

- Schot: Maximal gefiert, Baum 80–90° vom Boot
- Kicker: Fest (verhindert Baum-Aufsteigen)
- Preventer/Bullenstander: PFLICHT (verhindert Patenthalse)
- Profil: So tief wie möglich
- Fokus: Segelfläche maximieren, Sicherheit

**WARNUNG:** Auf Vorwindkurs besteht erhöhte Gefahr der Patenthalse
(unkontrollierte Halse). Der Bullenstander (Preventer) ist eine
Sicherheitsausrüstung, die den Baum auf einer Seite fixiert.

### 5.5 Reffen — Technik

#### 5.5.1 Vorbereitung

1. Beidrehen oder auf halbem Wind gehen
2. Kicker leicht lösen
3. Fall klar zum Fieren
4. Reffleinen klar zum Dichtholen
5. Lazy Jacks aktiviert (falls vorhanden)

#### 5.5.2 Ablauf (Slab Reefing)

1. Fall fieren bis Reffhaken am Vorliek den Lümmelbeschlag erreicht
2. Reffhaken einsetzen (Hals-Reffpunkt)
3. Reff-Outhaul (Achterliek) dichtholen
4. Fall wieder auf Spannung setzen
5. Cunningham ggf. nachsetzen
6. Übriges Segeltuch mit Reffbändseln sichern (optional)

#### 5.5.3 Häufige Fehler beim Reffen

| Fehler | Auswirkung | Korrektur |
|--------|-----------|-----------|
| Fall zu viel gefiert | Segel schlägt unkontrolliert | Fall nur soweit fieren wie nötig |
| Reffhaken nicht eingehakt | Segel reißt am Vorliek | Immer Haken prüfen |
| Reff-Outhaul nicht dicht | Achterliek flattert, schlechtes Profil | Outhaul voll dichtholen |
| Fall nicht wieder auf Spannung | Schlaffes Vorliek, schlechter Trimm | Fall nach Reffen spannen |
| Reffbändseln um Baum | Nur um Segel, nie um Baum! | Beschädigt Segel |

---

## 6. Reefing-Systeme

### 6.1 Slab Reefing (Bindereff)

#### 6.1.1 Traditionelles Bindereff

Das älteste und bewährteste Reefing-System. Erfordert:
- Reffhaken oder Reffkauschen am Vorliek (1–3 Reffpunkte)
- Reffausholer-Ösen am Achterliek (1–3 Reffpunkte)
- Reffbändseln (optionale Sicherung des Tuchs)
- Fall-Winch
- Reffleinen-Führung

**Hardware:**
| Komponente | Hersteller | Preis |
|-----------|-----------|-------|
| Reffhaken (Lümmelbeschlag) | Seldén, Harken, RWO | € 50–200 |
| Reffblock (Baum-intern) | Harken, Ronstan | € 40–120 |
| Reffleinen (Dyneema, 8–10 mm) | Liros, Marlow, Robline | € 3–8/m |
| Klemmen (Spinlock, Antal) | Spinlock, Antal, Lewmar | € 40–120/Stk |

#### 6.1.2 Single-Line Reefing

Eine einzige Leine pro Reffpunkt bedient sowohl den Vorliek-Reffhaken
als auch den Achterliek-Reffausholer. Die Leine läuft durch den Baum
und wird über Umlenkrollen zum Cockpit zurückgeführt.

**Systeme:**
- **Harken MKIV Battcar**: Kompatibel mit Single-Line
- **Seldén Single-Line**: Integriert in Seldén-Bäume
- **Antal Easylock**: Kompaktes Klemmsystem für Single-Line

**Vorteile:**
- Ein Bedienschritt pro Reff
- Bedienung aus dem Cockpit
- Ideal für Shorthanded-Segeln
- Reduzierte Fehlerquote

**Nachteile:**
- Höhere Reibung (Seil läuft durch mehrere Umlenkungen)
- Weniger präzise als Zwei-Leinen-System
- Seil-Durchmesser begrenzt (Reibung im Baum)
- Bei Versagen: gesamtes System fällt aus

**Kosten komplett (inkl. Installation):**
| Bootsgröße | Material | Installation | Gesamt |
|-----------|----------|-------------|--------|
| 30–35 ft | € 500–900 | € 400–800 | € 900–1.700 |
| 35–40 ft | € 700–1.200 | € 600–1.000 | € 1.300–2.200 |
| 40–50 ft | € 1.000–1.800 | € 800–1.500 | € 1.800–3.300 |

#### 6.1.3 Zwei-Leinen-Reefing (Two-Line)

Separate Leinen für Vorliek (Cunningham/Tack) und Achterliek (Clew).
Mehr Kontrolle, zwei Bedienschritte.

**Vorteile:**
- Präzisere Einstellung
- Geringere Reibung pro Leine
- Einfachere Fehlerdiagnose
- Redundanz (eine Leine kann ausfallen)

**Nachteile:**
- Zwei Bedienschritte
- Mehr Leinen im Cockpit
- Erfordert Koordination

### 6.2 In-Mast-Rollreff-Systeme

#### 6.2.1 Seldén In-Mast

Seldén (Schweden) ist der Marktführer für In-Mast-Rollreff-Systeme:

| Modell | Bootsgröße | Mastprofil | Preis (nur Rollsystem) |
|--------|-----------|-----------|----------------------|
| Furlex 50 S | 28–35 ft | 135×90 mm | € 2.500–4.000 |
| Furlex 100 S | 33–42 ft | 155×100 mm | € 3.500–5.500 |
| Furlex 200 S | 40–50 ft | 180×115 mm | € 5.000–8.000 |
| Furlex 300 S | 48–60 ft | 210×140 mm | € 7.000–12.000 |

> ⚠️ **ZU PRÜFEN (Audit):** Produktbezeichnung "Furlex 50 S / 100 S / 200 S / 300 S" — **Furlex** ist Seldéns *Vorsegel*-Rollreffanlage (Rollanlage am Vorstag, Größenbezeichnung nach Vorstag/Drahtlänge), **nicht** die Groß-Rollreffanlage im Mast. Seldéns In-Mast-System sind die *Rollmasten* (Typ RA/RB/RC) mit "Synchronized Main Furling (SMF)". Die hier gelisteten Modellnamen, Mastprofile und Preise für das In-Mast-System sind daher unverifiziert (estimated — unverifiziert). Quelle: seldenmast.com (Furlex = jib/headsail furling; Furling masts / SMF = in-mast mainsail furling).

**Elektrische Option (Seldén E-Motor):**
- Aufpreis: € 3.000–6.000
- Integriert in Masttrommel
- Bedienung: Schalter am Cockpit oder Fernbedienung

#### 6.2.2 Profurl / Facnor

Profurl (heute Teil von Wichard Group, Frankreich):

| Modell | Bootsgröße | Preis |
|--------|-----------|-------|
| FM C320 | 30–38 ft | € 3.000–5.000 |
| FM C420 | 38–48 ft | € 5.000–8.000 |
| FM C580 | 48–65 ft | € 8.000–14.000 |

#### 6.2.3 Wartung In-Mast-Systeme

| Intervall | Maßnahme | Aufwand |
|-----------|---------|--------|
| Wöchentlich | Segel ein-/ausrollen (Mechanismus bewegen) | 5 min |
| Monatlich | Mastnut mit Silikonspray | 15 min |
| Saisonstart | Rollmechanismus prüfen, Lager fetten | 1–2 h |
| Saisonende | Segel bergen, Mechanismus reinigen | 2–3 h |
| Alle 3 Jahre | Professionelle Inspektion Rollmechanismus | € 300–600 |
| Alle 5–8 Jahre | Lager und Dichtungen tauschen | € 500–1.500 |

### 6.3 In-Boom-Rollreff-Systeme

#### 6.3.1 Leisure Furl

Leisure Furl (Neuseeland/USA) ist der weltweit führende Hersteller:

| Modell | Bootsgröße | Baum-Durchmesser | Preis (nur Baum) |
|--------|-----------|-----------------|-----------------|
| LF-100 | 28–35 ft | 180 mm | € 6.000–9.000 |
| LF-200 | 33–42 ft | 210 mm | € 8.000–13.000 |
| LF-300 | 40–50 ft | 250 mm | € 12.000–18.000 |
| LF-400 | 48–60 ft | 300 mm | € 16.000–25.000 |

**Funktion:** Das Segel wird um einen Mandrel (Dorn) im Baum gewickelt.
Der Mandrel wird durch ein Endlos-Fall oder elektrisch gedreht.

#### 6.3.2 Schaefer In-Boom

Schaefer Marine (USA) bietet ein alternatives System:

| Modell | Bootsgröße | Preis |
|--------|-----------|-------|
| SE-500 | 30–38 ft | € 7.000–11.000 |
| SE-600 | 36–45 ft | € 10.000–16.000 |
| SE-700 | 43–55 ft | € 14.000–22.000 |

#### 6.3.3 Bartels In-Boom

Bartels (Deutschland) ist ein europäischer Hersteller mit besonders
robuster Bauweise:

| Modell | Bootsgröße | Preis |
|--------|-----------|-------|
| B-Furl 300 | 28–36 ft | € 5.000–8.000 |
| B-Furl 400 | 34–44 ft | € 7.500–12.000 |
| B-Furl 500 | 42–55 ft | € 11.000–18.000 |

### 6.4 Lazy Jacks, Dutchman und Bergesysteme

#### 6.4.1 Lazy Jacks

Lazy Jacks sind Leinen, die vom Mast (oberes Drittel) schräg zum Baum
geführt werden und eine "Auffangtasche" für das Segel beim Bergen bilden.

**Konfiguration:**
- 2–3 Leinenpaare pro Seite
- Oberer Befestigungspunkt: 60–80 % der Masthöhe
- Unterer Befestigungspunkt: Gleichmäßig am Baum verteilt
- Material: Dyneema oder Polyester, 4–6 mm
- Preis: € 80–250 (Material), € 200–500 (Installation)

**Vorteile:**
- Segel fällt kontrolliert auf den Baum
- Einfaches Bergen ohne Vorschiff-Gang
- Günstig und einfach nachzurüsten

**Nachteile:**
- Segel kann beim Setzen hinter Lazy Jacks hängen
- Optisch nicht optimal
- Können am Segel scheuern (Chafe)

#### 6.4.2 Dutchman-System

Das Dutchman-System verwendet vertikale Leinen, die durch Ösen im
Großsegel geführt werden. Beim Bergen fällt das Segel in kontrollierten
Falten auf den Baum.

**Kosten:** € 300–600 (Material + Installation)

#### 6.4.3 StackPack / Lazy Bag

Ein StackPack (auch Lazy Bag, Sail Pack) ist eine Tasche aus Acryl- oder
Dacrontuch, die am Baum befestigt ist und das geborene Segel aufnimmt.

**Hersteller und Preise:**
| Hersteller | Bootsgröße | Preis |
|-----------|-----------|-------|
| ATN (StackPack) | 25–55 ft | € 400–1.500 |
| UK Sailmakers | 30–50 ft | € 350–1.200 |
| Doyle Sail Cover | 25–60 ft | € 300–1.000 |
| North Sails Lazy Bag | 30–55 ft | € 400–1.400 |

**Vorteile:**
- Schnelles Bergen und Verstauen
- Schutz vor UV und Regen
- Keine separate Persenning nötig
- Sauberes Decksbild

**Nachteile:**
- Zusätzliches Gewicht am Baum (3–8 kg)
- Kann Segeltrimm leicht beeinflussen
- Reißverschlüsse als Verschleißteil
- UV-Degradation des StackPack-Materials

---

## 7. Hersteller

### 7.1 North Sails (3Di-Technologie)

#### 7.1.1 Unternehmen

North Sails ist der weltweit größte Segelhersteller (Hauptsitz: Milford, CT, USA).
Über 30 Lofts weltweit, darunter Deutschland (Strande/Kiel).

#### 7.1.2 Produktlinien für Großsegel

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| 3Di RAW 760 | Carbon HM | Grand Prix | € 8.000–12.000 | € 12.000–18.000 | € 18.000–28.000 |
| 3Di NORDAC | Carbon + Dyneema | Perf. Cruising | € 5.500–8.000 | € 8.000–12.000 | € 12.000–18.000 |
| 3Di NPC | Carbon + Taffeta | Cruising | € 4.000–6.000 | € 6.000–9.000 | € 9.000–14.000 |
| 3Di ENDURE | Dyneema + Taffeta | Langfahrt | € 3.500–5.000 | € 5.000–7.500 | € 7.500–11.000 |
| North Dacron | Dacron Premium | Budget Cruising | € 2.000–3.000 | € 3.000–4.500 | € 4.500–7.000 |

#### 7.1.3 Besonderheiten

- **3Di Design Tool**: Computergestützte Faseroptimierung
- **SailPack**: North Sails' eigenes Bergesystem
- **NorthTracker**: IoT-Sensor für Segelnutzung und Trimm
- **Global Service Network**: Reparatur weltweit möglich
- **Garantie**: 2 Jahre auf Material und Verarbeitung

### 7.2 Elvström Sails (EPEX-Technologie)

#### 7.2.1 Unternehmen

Elvström Sails (Dänemark) wurde vom legendären Olympia-Segler Paul Elvström
gegründet. Bekannt für Innovation und skandinavische Qualität.

#### 7.2.2 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| EPEX Racing | Carbon HM Membran | Regatta | € 7.000–10.000 | € 10.000–15.000 | € 15.000–24.000 |
| EPEX Performance | Carbon + Technora | Perf. Cruising | € 4.500–7.000 | € 7.000–10.000 | € 10.000–16.000 |
| EPEX Cruising | Technora + Dyneema | Cruising | € 3.500–5.500 | € 5.500–8.000 | € 8.000–12.000 |
| EPEX Cruising Plus | Dyneema + Taffeta | Langfahrt | € 3.000–4.500 | € 4.500–6.500 | € 6.500–10.000 |
| Elvström Dacron | Dacron Premium | Budget | € 1.800–2.800 | € 2.800–4.200 | € 4.200–6.500 |

#### 7.2.3 Besonderheiten

- **EPEX-Formtechnik**: Eigene 3D-Formstation in Kolding, Dänemark
- **NFC-Segel-ID**: Jedes Segel trägt einen NFC-Chip mit Herstellungsdaten
- **Furlable EPEX**: Spezielle Rollreff-kompatible EPEX-Version
- **Regatta-Expertise**: Starke Präsenz in olympischen Klassen

### 7.3 Doyle Sails (Stratis-Technologie)

#### 7.3.1 Unternehmen

Doyle Sails (Neuseeland/International) mit Lofts weltweit. Bekannt für
Langfahrt- und Blauwasser-Expertise.

#### 7.3.2 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| Stratis ICE | Carbon Grand-Prix | Regatta | € 7.500–11.000 | € 11.000–16.000 | € 16.000–25.000 |
| Stratis GTi | Carbon + Technora | Performance | € 5.000–7.500 | € 7.500–11.000 | € 11.000–17.000 |
| Stratis Delta | Technora + Dyneema | Cruising | € 3.500–5.500 | € 5.500–8.500 | € 8.500–13.000 |
| Stratis GP | Pentex Membran | Einsteiger-Perf. | € 2.800–4.200 | € 4.200–6.500 | € 6.500–10.000 |
| Doyle Dacron | Dacron Premium | Budget | € 1.700–2.600 | € 2.600–4.000 | € 4.000–6.200 |

#### 7.3.3 Besonderheiten

- **Stratis-Lay-Up**: Patentierte Faserlege-Technik
- **Cableless Construction**: Fasern übernehmen strukturelle Lasten (kein Boltrope)
- **Offshore-Expertise**: Volvo Ocean Race, Vendée Globe
- **UV-optimierte Laminate**: Besonders langlebig in tropischen Revieren

### 7.4 Quantum Sails

#### 7.4.1 Unternehmen

Quantum Sails (USA/International), ursprünglich aus dem America's Cup.
Lofts in über 40 Ländern.

#### 7.4.2 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| Fusion M | Carbon Membran | Grand-Prix | € 7.000–10.500 | € 10.500–15.000 | € 15.000–23.000 |
| Q2 | Pentex/Technora | Performance | € 4.000–6.000 | € 6.000–9.000 | € 9.000–14.000 |
| Q3 | Dacron Premium | Cruising | € 2.200–3.200 | € 3.200–4.800 | € 4.800–7.500 |
| Quantum Dacron | Dacron Standard | Budget | € 1.600–2.400 | € 2.400–3.600 | € 3.600–5.500 |

### 7.5 UK Sailmakers

#### 7.5.1 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| X-Drive | Carbon-Tape auf Dacron | Performance | € 4.500–6.500 | € 6.500–9.500 | € 9.500–15.000 |
| Tape-Drive | Mylar-Tape auf Dacron | Cruiser-Perf. | € 3.000–4.500 | € 4.500–6.500 | € 6.500–10.000 |
| UK Dacron | Dacron Premium | Cruising | € 1.800–2.700 | € 2.700–4.000 | € 4.000–6.200 |

#### 7.5.2 Besonderheiten

- **X-Drive**: Carbon-Tape-Streifen werden auf Dacron-Trägertuch aufgebracht
- Kombination aus Dacron-Handling und Carbon-Formhaltung
- Reparierbar wie Dacron-Segel
- Guter Kompromiss für Performance-Cruiser

### 7.6 OneSails

#### 7.6.1 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| 4T FORTE Racing | Carbon Membran | Regatta | € 6.500–9.500 | € 9.500–14.000 | € 14.000–22.000 |
| 4T FORTE Cruising | Dyneema + Taffeta | Cruising | € 3.500–5.000 | € 5.000–7.500 | € 7.500–12.000 |
| OneSails Dacron | Dacron | Budget | € 1.600–2.400 | € 2.400–3.500 | € 3.500–5.500 |

#### 7.6.2 Besonderheiten

- **4T FORTE**: Vier-Taffeta-Lagen mit eingebetteten Fasern
- Sehr gute Knickfestigkeit (Rollreff-kompatibel)
- Europäische Fertigung (Italien)
- Attraktives Preis-Leistungs-Verhältnis

### 7.7 Rolly Tasker Sails

#### 7.7.1 Unternehmen

Rolly Tasker Sails (Thailand) ist einer der größten OEM-Segelhersteller
(Erstausrüster für viele Werften wie Bavaria, Beneteau, Jeanneau).

#### 7.7.2 Produktlinien

| Produkt | Technologie | Zielgruppe | Preis 35 ft | Preis 42 ft | Preis 50 ft |
|---------|------------|------------|-------------|-------------|-------------|
| RT Performance | Pentex Tri-Radial | Performance | € 2.500–3.800 | € 3.800–5.500 | € 5.500–8.500 |
| RT Cruising | Dacron Premium | Cruising | € 1.400–2.200 | € 2.200–3.300 | € 3.300–5.000 |
| RT Economy | Dacron Standard | Budget/Charter | € 1.000–1.600 | € 1.600–2.400 | € 2.400–3.800 |

#### 7.7.3 Besonderheiten

- Niedrigste Preise im Markt (Fertigung in Thailand)
- OEM für zahlreiche Großserienwerften
- Gute Qualität für den Preis
- Längere Lieferzeiten nach Europa (6–10 Wochen)
- Service-Netzwerk in Europa über Partner

### 7.8 Herstellervergleich — Zusammenfassung

| Hersteller | Stärke | Schwäche | Empfehlung |
|-----------|--------|---------|-----------|
| North Sails | 3Di-Technologie, globales Netzwerk | Hohe Preise, Monopol-Gefühl | Performance-Cruiser mit Budget |
| Elvström | EPEX-Innovation, skandinavische Qualität | Kleineres Netzwerk | Europäische Segler |
| Doyle | Langfahrt-Expertise, Stratis | Weniger Lofts | Blauwasser-Segler |
| Quantum | Breites Sortiment | Weniger innovative Materialien | Allrounder |
| UK Sailmakers | X-Drive (reparierbar + performant) | Nur als Franchise | Performance mit Dacron-Handling |
| OneSails | Preis-Leistung, 4T FORTE | Kleinerer Name | Budget-Performance |
| Rolly Tasker | Günstigste Preise | Kein lokaler Service | Budget, Charter |

---

## 8. Fehlerbild-Atlas

### 8.1 F-16_02-01 — Vorliektau-/Nut-Probleme (Luff Groove Issues)

#### 8.1.1 Beschreibung

Das Vorliektau (Boltrope) oder die Rutscher (Slides/Slugs) verklemmen in
der Mastnut oder auf der Mastschiene. Das Segel lässt sich nicht setzen
oder bergen.

#### 8.1.2 Erscheinungsbild

- Segel bleibt beim Setzen auf halber Höhe stecken
- Segel lässt sich beim Bergen nicht herunterholen
- Sichtbare Beschädigung/Verformung der Slides
- Mastnut-Kanten eingedrückt oder verbogen
- Boltrope ausgefranst oder verdickt

#### 8.1.3 Ursachen

| Ursache | Häufigkeit | Schwere |
|---------|-----------|--------|
| Verschmutzte Mastnut (Salz, Schmutz) | Sehr häufig | Gering |
| Verformte Slides/Slugs | Häufig | Mittel |
| Beschädigte Mastnut (Delle, Grat) | Mittel | Hoch |
| Verdicktes Boltrope (Feuchtigkeit) | Mittel | Mittel |
| Falsche Slide-Größe | Selten | Hoch |
| Korrodierte Mastschiene | Selten | Hoch |

#### 8.1.4 Reparatur und Prävention

- Mastnut regelmäßig mit Süßwasser spülen und Silikonspray behandeln
- Slides alle 2–3 Saisons prüfen und ggf. austauschen
- Mastnut auf Grate prüfen und mit feinem Schleifpapier glätten
- McLube oder ähnliches Gleitmittel verwenden (kein ölbasiertes Schmiermittel)
- Defekte Slides einzeln austauschen (€ 5–15/Stk)
- Bei Schienenbeschädigung: Segelschiene ersetzen (€ 200–800 + Installation)

#### 8.1.5 AYDI-Bewertung

- **Konfidenz**: visual_medium (sichtbar bei guten Fotos)
- **Schweregrad**: WARNUNG bis KRITISCH
- **Empfehlung**: Sofortige Inspektion empfohlen

### 8.2 F-16_02-02 — Achterliek-Flattern (Leech Flutter)

#### 8.2.1 Beschreibung

Das Achterliek des Großsegels flattert unkontrolliert, was ein
charakteristisches "Klatsch"-Geräusch erzeugt. Dies ist eines der
häufigsten Probleme bei Großsegeln.

#### 8.2.2 Erscheinungsbild

- Sichtbares Flattern der Achterliekkante
- Hörbares rhythmisches Klatschen
- Beschleunigte Materialermüdung am Achterliek
- Telltales am Achterliek flattern chaotisch
- Ausgefranste Achterliekkante bei fortgeschrittenem Verschleiß

#### 8.2.3 Ursachen und Behebung

| Ursache | Diagnose | Behebung | Kosten |
|---------|---------|---------|--------|
| Leech Line zu lose | Flattern hört auf bei Anziehen der Leech Line | Leech Line anziehen | € 0 (Trimm) |
| Leech Line gebrochen | Leech Line ohne Funktion | Leech Line ersetzen | € 50–150 |
| Achterliek-Saum aufgetrennt | Sichtbare Naht-Öffnung | Segelmacher: Saum nähen | € 80–200 |
| Profil ausgeweht | Achterliek ist "hohl" geworden | Segelmacher: Achterliek kürzen | € 150–400 |
| Zu viel Twist | Achterliek "einfallen" bei jedem Kurs | Schot/Kicker dichter | € 0 (Trimm) |
| Latten fehlen/gebrochen | Bereich ohne Stützung | Latten ersetzen | € 15–150/Stk |

#### 8.2.4 AYDI-Bewertung

- **Konfidenz**: visual_high (deutlich erkennbar auf Fotos)
- **Schweregrad**: INFO bis WARNUNG
- **Empfehlung**: Trimm prüfen, Leech Line prüfen, ggf. Segelmacher

### 8.3 F-16_02-03 — Lattentaschen-Verschleiß (Batten Pocket Wear)

#### 8.3.1 Beschreibung

Die Lattentaschen zeigen Verschleiß durch mechanische Belastung,
UV-Strahlung oder Scheuern. Die Latten können sich lösen oder
durchscheuern.

#### 8.3.2 Erscheinungsbild

- Aufgescheuerte oder aufgetrennte Nähte an Lattentaschen-Enden
- Durchgescheuertes Material an Lattentaschen-Eingang
- Verfärbung/Versprödung des Lattentaschen-Materials
- Latte steht aus der Tasche hervor
- Velcro-Verschluss hält nicht mehr

#### 8.3.3 Ursachen

- Mechanische Belastung bei Wende/Halse (Latte schlägt gegen Wanten)
- UV-Degradation des Taschen-Materials
- Reibung der Latte in der Tasche bei Twist-Änderungen
- Falscher Latten-Durchmesser (zu dick → dehnt Tasche)
- Übermäßige Lattenspannung

#### 8.3.4 Reparatur

| Reparatur | Aufwand | Kosten |
|-----------|--------|--------|
| Nähte nachbessern (lokal) | Segelmacher, 1–2 h | € 60–120 |
| Lattentaschen-Ende verstärken | Segelmacher, 2–3 h | € 100–200 |
| Lattentasche komplett erneuern | Segelmacher, 3–5 h | € 150–350 |
| Velcro-Verschluss erneuern | Segelmacher, 1 h | € 40–80 |

#### 8.3.5 AYDI-Bewertung

- **Konfidenz**: visual_medium (erkennbar bei guten Detailfotos)
- **Schweregrad**: INFO bis WARNUNG
- **Empfehlung**: Saisonale Inspektion, frühzeitige Reparatur

### 8.4 F-16_02-04 — Cunningham-Öse Ausriss (Cunningham Eyelet Pullout)

#### 8.4.1 Beschreibung

Die Cunningham-Öse reißt aus dem Segel aus oder zeigt Deformierung.
Dies ist ein strukturelles Problem, das sofortige Aufmerksamkeit erfordert.

#### 8.4.2 Erscheinungsbild

- Verformte oder ovale Öse
- Risse im Segeltuch rund um die Öse
- Ausgerissene Verstärkungslagen
- Öse vollständig losgerissen
- Vorliek im Cunningham-Bereich deformiert

#### 8.4.3 Ursachen

| Ursache | Häufigkeit |
|---------|-----------|
| Übermäßige Cunningham-Spannung | Häufig |
| Unzureichende Verstärkung | Mittel |
| Materialermüdung (Alter) | Mittel |
| Plötzliche Belastungsspitzen (Böen) | Selten |
| Korrosion der Metallöse | Selten |

#### 8.4.4 Reparatur

- Segelmacher: Neue Öse mit erweiteter Verstärkung einsetzen
- Kosten: € 120–300
- Zeitraum: 1–3 Tage (Segelmacher)
- Prävention: Cunningham-Spannung reduzieren, Öse regelmäßig prüfen

#### 8.4.5 AYDI-Bewertung

- **Konfidenz**: visual_high (deutlich sichtbar auf Fotos)
- **Schweregrad**: WARNUNG bis KRITISCH
- **Empfehlung**: Sofortige Reparatur empfohlen

### 8.5 F-16_02-05 — Schothorn-Versagen (Clew Failure)

#### 8.5.1 Beschreibung

Das Schothorn ist der am höchsten belastete Punkt des Großsegels
(Kombination aus Schot-, Outhaul- und Reff-Kräften). Versagen kann
zum sofortigen Funktionsverlust des Segels führen.

#### 8.5.2 Erscheinungsbild

- Risse in den Verstärkungslagen rund um das Schothorn
- Verformte oder ovale Schothorn-Öse
- Ablösung der Verstärkungslagen
- Vollständiger Ausriss (Segel nicht mehr kontrollierbar)
- Delamination im Schothorn-Bereich (bei Laminatsegeln)

#### 8.5.3 Ursachen und Belastungen

Typische Belastungen am Schothorn:
| Bootsgröße | Schot-Last (max) | Outhaul-Last | Reff-Last |
|-----------|-----------------|-------------|-----------|
| 30 ft | 300–600 kg | 100–250 kg | 200–400 kg |
| 40 ft | 600–1.200 kg | 200–500 kg | 400–800 kg |
| 50 ft | 1.000–2.000 kg | 400–800 kg | 700–1.400 kg |

#### 8.5.4 Reparatur

- Sofortige Segelbergung bei sichtbaren Rissen
- Segelmacher: Neue Verstärkungslagen, neue Öse
- Kosten: € 200–600 (Reparatur), € 500–1.500 (kompletter Neuaufbau)
- Bei Laminatsegeln oft Totalschaden (nicht reparierbar)

#### 8.5.5 AYDI-Bewertung

- **Konfidenz**: visual_high
- **Schweregrad**: KRITISCH
- **Empfehlung**: Sofortige Segelbergung, Segelmacherinspektion

### 8.6 F-16_02-06 — UV-Achterliek-Schäden (UV Leech Damage)

#### 8.6.1 Beschreibung

UV-Strahlung degradiert das Segelmaterial am Achterliek, da dieser
Bereich bei gerefftem oder geborgenem Segel oft der Sonne ausgesetzt ist.

#### 8.6.2 Erscheinungsbild

- Verfärbung des Achterliek-Bereichs (Vergilbung, Ausbleichen)
- Versprödung des Materials (Knirschen beim Knicken)
- Auflösung der UV-Schutzstreifen
- Fadenzug und Materialablösung
- Achterliek-Saum aufgelöst

#### 8.6.3 Betroffene Materialien (UV-Empfindlichkeit)

| Material | UV-Degradation nach 5 Jahren | Risiko |
|----------|------------------------------|--------|
| Dacron | 5–10 % Festigkeitsverlust | Gering |
| Pentex | 10–15 % | Mäßig |
| Technora | 15–25 % | Hoch |
| Kevlar | 30–50 % | Sehr hoch |
| Carbon | 2–5 % | Gering |
| Dyneema | 5–10 % | Gering |
| Mylar-Folie | 15–30 % | Hoch |

#### 8.6.4 Prävention und Reparatur

- UV-Schutzstreifen anbringen oder erneuern (€ 150–400)
- Persenning/StackPack verwenden
- Segel bergen wenn nicht in Gebrauch
- Achterliek-Saum erneuern lassen (€ 200–500)
- Bei fortgeschrittenem Schaden: Segel ersetzen

#### 8.6.5 AYDI-Bewertung

- **Konfidenz**: visual_medium
- **Schweregrad**: INFO bis WARNUNG
- **Empfehlung**: UV-Schutz prüfen und ggf. erneuern

### 8.7 F-16_02-07 — Laminat-Blasenbildung (Laminate Bubbling)

#### 8.7.1 Beschreibung

Bei Laminatsegeln lösen sich die Schichten voneinander (Delamination),
was als Blasen oder Aufwölbungen sichtbar wird.

#### 8.7.2 Erscheinungsbild

- Luftblasen zwischen den Laminatschichten
- Aufwölbungen, die sich bei Druck bewegen lassen
- Knisternde Geräusche beim Knicken
- Milchige/trübe Stellen im Laminat
- Sichtbare Faserablösung

#### 8.7.3 Ursachen

| Ursache | Häufigkeit | Prävention |
|---------|-----------|-----------|
| UV-Degradation des Klebers | Häufig | UV-Schutz, Persenning |
| Mechanische Ermüdung (Flattern) | Häufig | Korrekt trimmen, kein Flattern |
| Feuchtigkeit im Laminat | Mittel | Segel trocknen, nicht nass verstauen |
| Produktionsfehler (Klebung) | Selten | Garantieanspruch |
| Chemische Einwirkung (Diesel, Säuren) | Selten | Segel schützen |

#### 8.7.4 Reparatur

- Kleine Blasen (<50 mm): Lokale Reparatur mit Laminatflicken (€ 50–150)
- Große Blasen (>50 mm): Nur durch Hersteller reparierbar (€ 200–800)
- Großflächige Delamination: Segel nicht mehr reparierbar (Ersatz)

#### 8.7.5 AYDI-Bewertung

- **Konfidenz**: visual_medium (erkennbar bei guten Detailfotos)
- **Schweregrad**: WARNUNG bis KRITISCH
- **Empfehlung**: Segelmacher konsultieren, Progressionsüberwachung

### 8.8 F-16_02-08 — Reffpunkt-Ausriss (Reef Point Pullout)

#### 8.8.1 Beschreibung

Die Reffpunkte (Reffhals-Öse oder Reff-Schothorn-Öse) reißen unter
Last aus dem Segel aus. Kritisches Sicherheitsproblem.

#### 8.8.2 Erscheinungsbild

- Verformte Reff-Ösen
- Risse rund um Reff-Verstärkungen
- Ausgerissene Reffbändseln-Ösen
- Deformation des Segels im Reffbereich

#### 8.8.3 Ursachen

- Reff-Outhaul zu stark durchgesetzt
- Unzureichende Verstärkung (Herstellerfehler)
- Materialermüdung
- Falsche Reff-Technik (Reff-Outhaul vor Fall)
- Böen-Belastung bei gerefftem Segel

#### 8.8.4 Reparatur

- Neue Verstärkung mit erweiterter Fläche: € 150–400
- Neue Reff-Ösen: € 50–100 pro Öse
- Kompletter Reffbereich neu aufbauen: € 300–800
- Bei Laminatsegeln: oft nicht reparierbar

#### 8.8.5 AYDI-Bewertung

- **Konfidenz**: visual_high
- **Schweregrad**: KRITISCH
- **Empfehlung**: Sofortige Reparatur, Segel nicht gerefft nutzen

### 8.9 F-16_02-09 — Kopfbrett-Deformation (Headboard Deformation)

#### 8.9.1 Beschreibung

Das Kopfbrett (Headboard) verformt sich unter der Fall-Last oder bricht.
Kann zum Verlust des Segels führen.

#### 8.9.2 Erscheinungsbild

- Verbogenes oder verformtes Kopfbrett
- Risse im Kopfbrett-Material
- Lösen des Kopfbretts von den Verstärkungslagen
- Ausgerissene Fall-Öse
- Segel hängt schief am Fall

#### 8.9.3 Ursachen

| Ursache | Häufigkeit |
|---------|-----------|
| Überbelastung (zu viel Fall-Spannung) | Mittel |
| Materialermüdung (Alter) | Mittel |
| Korrosion (Aluminium-Kopfbrett) | Selten |
| Produktionsfehler | Selten |
| Rigg-Schaden (Fall-Block-Versager) | Selten |

#### 8.9.4 Reparatur

- Neues Kopfbrett einsetzen: € 150–400
- Verstärkungslagen erneuern: € 100–250
- Fall-Öse ersetzen: € 50–100
- Segelmacher-Zeitaufwand: 3–6 Stunden

#### 8.9.5 AYDI-Bewertung

- **Konfidenz**: visual_high
- **Schweregrad**: WARNUNG bis KRITISCH
- **Empfehlung**: Sofortige Inspektion, keine Nutzung bei Verformung

### 8.10 F-16_02-10 — In-Mast-Verklemmung (In-Mast Jamming)

#### 8.10.1 Beschreibung

Das In-Mast-Rollreff-Großsegel verklemmt im Mast und lässt sich weder
vollständig ein- noch ausrollen. Eines der häufigsten und kritischsten
Probleme bei In-Mast-Systemen.

#### 8.10.2 Erscheinungsbild

- Segel steckt fest (halb ein- oder ausgerollt)
- Knirschende/quietschende Geräusche beim Rollen
- Ungleichmäßiges Einrollen (Falten sichtbar)
- Motor (bei elektrischem System) blockiert oder überlastet
- Fall-Spannung anomal hoch oder niedrig

#### 8.10.3 Ursachen

| Ursache | Häufigkeit | Sofortmaßnahme |
|---------|-----------|---------------|
| Falsche Fall-Spannung | Sehr häufig | Fall fieren/spannen |
| Achterliek hakt an Versteifung | Häufig | Vorsichtig an Achterliek ziehen |
| Vertikale Latte verklemmt | Häufig | Latte durch Mastöffnung drücken |
| Fremdkörper in Mastnut | Mittel | Mastnut inspizieren |
| Verdrehtes Segel im Mast | Mittel | Segel komplett ausrollen, neu einrollen |
| Rollmechanismus defekt | Selten | Professionelle Hilfe erforderlich |

#### 8.10.4 Notfallverfahren

1. Ruhe bewahren — nicht mit Gewalt rollen
2. Fall-Spannung prüfen und variieren
3. Achterliek-Leech-Line lösen
4. Segel komplett ausrollen (weniger Reibung als einrollen)
5. Wenn ausgerollt: Fall-Spannung korrigieren, langsam einrollen
6. Wenn nichts hilft: Segel oben lassen, unter Motor einlaufen
7. An Land: Rigger/Segelmacher kontaktieren

#### 8.10.5 AYDI-Bewertung

- **Konfidenz**: visual_low (nur im ausgerollten Zustand beurteilbar)
- **Schweregrad**: KRITISCH
- **Empfehlung**: Regelmäßige Wartung, korrekte Bedienung

### 8.11 F-16_02-11 — Gebrochene Latten (Broken Battens)

#### 8.11.1 Beschreibung

Eine oder mehrere Latten sind gebrochen oder gesplittert.

#### 8.11.2 Erscheinungsbild

- Segel hat eine "Delle" oder Knick an der Bruchstelle
- Sichtbare Verformung der Lattentasche
- Latte steht in unnatürlichem Winkel
- Bei CFK-Latten: scharfe Bruchkanten (Verletzungsgefahr!)
- Achterliek hängt an der betroffenen Stelle durch

#### 8.11.3 Ursachen

| Ursache | Material | Häufigkeit |
|---------|----------|-----------|
| Überlast (Starkwind-Halse) | GFK, CFK | Häufig |
| Ermüdung (viele Zyklen) | GFK | Mittel |
| Schlag gegen Wanten/Backstag | CFK | Mittel |
| UV-Degradation | GFK | Selten |
| Falscher Latten-Typ/Dimension | Alle | Selten |

#### 8.11.4 Reparatur

- GFK-Latte ersetzen: € 15–35 + Einbau
- CFK-Latte ersetzen: € 60–150 + Einbau
- Lattentasche prüfen (Beschädigung durch Bruch)
- Ersatzlatten an Bord haben! (1–2 Stück jeder Länge)

#### 8.11.5 AYDI-Bewertung

- **Konfidenz**: visual_high
- **Schweregrad**: INFO bis WARNUNG
- **Empfehlung**: Latte ersetzen, Ursache analysieren

### 8.12 F-16_02-12 — Scheuerstellen an Saling/Achterstag (Chafe at Spreaders/Backstay)

#### 8.12.1 Beschreibung

Das Großsegel scheuert an den Salingen (Spreaders) oder am Achterstag,
was zu lokaler Materialschwächung führt. Besonders kritisch bei
Raumschots- und Vorwindkursen.

#### 8.12.2 Erscheinungsbild

- Aufgescheuertes Segeltuch in Saling-Höhe
- Fadenzug oder Materialablösung
- Dünne Stellen im Segel (gegen Licht sichtbar)
- Abriebspuren auf dem Achterliek
- Bei Laminatsegeln: lokale Delamination

#### 8.12.3 Ursachen

- Baum zu weit gefiert (Raumschots/Vorwind)
- Fehlender Bullenstander (Segel geht über Salingspitze)
- Saling-Polster fehlen oder sind verschlissen
- Achterstag ohne Schutz (Split-Backstag)
- Falsche Running-Backstag-Spannung

#### 8.12.4 Prävention und Reparatur

| Maßnahme | Kosten | Wirksamkeit |
|---------|--------|-------------|
| Salingpolster anbringen | € 30–80 | Hoch |
| Achterliek-Scheuerschutz | € 50–120 | Hoch |
| Bullenstander verwenden | € 30–100 | Sehr hoch |
| Aufgescheuertes Flicken | € 80–250 (Segelmacher) | Mittel |
| Chafe Patches aufnähen | € 100–300 | Hoch |

#### 8.12.5 AYDI-Bewertung

- **Konfidenz**: visual_medium (erkennbar bei Detailfotos)
- **Schweregrad**: WARNUNG
- **Empfehlung**: Scheuerschutz installieren, Segel regelmäßig inspizieren

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Großsegel hat zu wenig Kraft

```
Großsegel hat zu wenig Kraft / Boot geht nicht
├── Wind < 8 kn?
│   ├── JA → Leichtwind-Trimm anwenden
│   │   ├── Outhaul los (30-50 %)
│   │   ├── Cunningham los
│   │   ├── Traveller nach Luv
│   │   ├── Schot leicht (Twist zulassen)
│   │   └── Crew-Gewicht nach Lee (Boot aufrecht halten)
│   └── NEIN → Weiter prüfen
│       ├── Segel alt / ausgeweht?
│       │   ├── JA → Profil visuell prüfen
│       │   │   ├── Draft < 6 %? → Segel ersetzen
│       │   │   ├── Draft-Position > 55 %? → Cunningham kann nicht korrigieren → Segel ersetzen
│       │   │   └── Achterliek flattert unkontrolliert? → Leech Line + Segelmacher
│       │   └── NEIN → Weiter prüfen
│       │       ├── Mast zu stark gebogen?
│       │       │   ├── JA → Achterstag fieren, Wanten prüfen
│       │       │   └── NEIN → Weiter prüfen
│       │       │       ├── Traveller zu weit Lee?
│       │       │       │   ├── JA → Traveller nach Luv
│       │       │       │   └── NEIN → Segel zu flach geschnitten
│       │       │       │       └── → Segelmacher konsultieren
│       │       └── Trimm korrekt? → Segelmacher Profil-Check
```

### 9.2 Entscheidungsbaum: Reffen funktioniert nicht

```
Reffen funktioniert nicht
├── Slab Reefing?
│   ├── JA
│   │   ├── Fall geht nicht runter?
│   │   │   ├── Fall-Stopper klemmt → Stopper lösen
│   │   │   ├── Fall-Winch blockiert → Winch-Mechanismus prüfen
│   │   │   └── Halyard-Lock greift → Lock lösen
│   │   ├── Reffhaken greift nicht?
│   │   │   ├── Fall nicht weit genug gefiert → Mehr Fall fieren
│   │   │   ├── Haken verbogen → Haken ersetzen
│   │   │   └── Öse verformt → Segelmacher
│   │   ├── Reff-Outhaul geht nicht dicht?
│   │   │   ├── Leine blockiert → Umlenkung prüfen, Leine klar machen
│   │   │   ├── Zu viel Reibung → Blöcke schmieren/ersetzen
│   │   │   └── Leine zu dünn → Leine ersetzen (1–2 mm dicker)
│   │   └── Segel hängt unsauber?
│   │       ├── Lazy Jacks fehlen → Lazy Jacks installieren
│   │       └── Reffbändseln nicht gesetzt → Bändseln setzen
│   └── NEIN → In-Mast oder In-Boom? → Siehe 9.5 / 9.4
```

### 9.3 Entscheidungsbaum: Achterliek-Flattern

```
Achterliek flattert
├── Leech Line prüfen
│   ├── Leech Line lose → Anziehen (bis Flattern aufhört, aber NICHT so weit
│   │   dass Achterliek "Haken" bildet)
│   ├── Leech Line gebrochen → Ersetzen (Segelmacher, € 50–150)
│   └── Leech Line unter Spannung, flattert trotzdem
│       ├── Teilbereich flattert?
│       │   ├── Im Bereich einer Latte → Latte prüfen (gebrochen? falsch gespannt?)
│       │   ├── Zwischen Latten → Achterliek ausgeweht → Segelmacher
│       │   └── Am Kopf → Oberlatte prüfen, Kopfbrett-Befestigung prüfen
│       └── Gesamtes Achterliek flattert?
│           ├── Segel generell ausgeweht → Segel ersetzen
│           ├── Zu viel Twist → Schot/Kicker dichter
│           └── Achterliek zu hohl → Segelmacher kann begrenzt korrigieren
```

### 9.4 Entscheidungsbaum: Slide-Blockade

```
Slides/Slugs blockieren
├── Beim Setzen?
│   ├── Bestimmte Stelle am Mast?
│   │   ├── JA → Mastnut an dieser Stelle inspizieren
│   │   │   ├── Delle/Grat → Feilen/schleifen, Silikon
│   │   │   ├── Schiene lose → Schiene nachschrauben
│   │   │   └── Wechsel Nut/Schiene → Adapter prüfen
│   │   └── NEIN (überall schwergängig)
│   │       ├── Verschmutzung → Mastnut reinigen, Gleitmittel
│   │       ├── Slides verschlissen → Slides ersetzen
│   │       ├── Slides falscher Typ → Korrekte Slides bestellen
│   │       └── Boltrope verdickt → Boltrope ersetzen (Segelmacher)
│   └── Battcar blockiert?
│       ├── Lager trocken → Battcar schmieren
│       ├── Battcar verformt → Ersetzen
│       └── Schiene beschädigt → Schiene reparieren/ersetzen
├── Beim Bergen?
│   ├── Sail-Track-Stop in Position? → Entfernen
│   ├── Fall nicht genug gefiert → Mehr Fall fieren
│   └── Lazy Jacks blockieren → Lazy Jacks lösen
```

### 9.5 Entscheidungsbaum: In-Mast-Verklemmung

```
In-Mast-Segel verklemmt
├── Einrollen oder Ausrollen?
│   ├── Einrollen blockiert
│   │   ├── Schritt 1: Fall-Spannung reduzieren (50 mm fieren)
│   │   ├── Schritt 2: Schot und Kicker lösen
│   │   ├── Schritt 3: Leech Line komplett fieren
│   │   ├── Schritt 4: Langsam einrollen, ggf. am Achterliek nachhelfen
│   │   ├── Schritt 5: Wenn blockiert → Fall mehr fieren
│   │   └── Schritt 6: Wenn nichts hilft → Segel komplett ausrollen, inspizieren
│   │       ├── Vertikale Latte quer? → Latte entfernen oder richten
│   │       ├── Segel verdreht? → Komplett ausrollen, Fall kontrolliert neu setzen
│   │       ├── Fremdkörper in Nut? → Mast öffnen (Rigger erforderlich)
│   │       └── Rollmechanismus defekt? → Rigger/Werft kontaktieren
│   └── Ausrollen blockiert
│       ├── Fall zu viel Spannung? → Spannung variieren
│       ├── Segel im Mast verknotet? → Vorsichtig am Segel ziehen
│       ├── Motor/Trommel blockiert? → Manuell rollen (Endlos-Fall)
│       └── Segel gefroren? (Winter) → Mastnut mit warmem Wasser behandeln
├── NOTFALL-PROTOKOLL:
│   ├── Segel bleibt halb ausgerollt und Wind nimmt zu
│   ├── → Motor starten, Bug in den Wind drehen
│   ├── → Schot dicht, Segel so gut wie möglich trimmen
│   ├── → Nächsten Hafen anlaufen
│   └── → Professionelle Hilfe an Land
```

---

## 10. Lebensdauer

### 10.1 Lebensdauer nach Material

| Material | Fahrtensegeln (Saisons) | Regatta (Saisons) | Einflussfaktoren |
|----------|------------------------|-------------------|-----------------|
| Dacron Standard | 5–8 | 3–5 | UV, Reibung, Trimm |
| Dacron Premium | 7–12 | 4–6 | UV, Reibung |
| Pentex | 6–10 | 3–5 | UV, Knicken |
| Technora Laminat | 5–8 | 2–4 | UV, Delamination |
| Kevlar Laminat | 3–5 | 1–3 | UV, Knicken |
| Carbon Laminat | 5–10 | 2–4 | Knicken, Delamination |
| Dyneema Laminat | 5–8 | 3–5 | Creep |
| 3Di NORDAC | 6–10 | 3–5 | Abrasion |
| 3Di ENDURE | 10–15 | – | UV, Abrasion |
| EPEX Cruising | 8–12 | – | UV, Delamination |
| Stratis Delta | 7–11 | – | UV, Delamination |

### 10.2 Degradationsindikatoren

#### 10.2.1 Visuelle Indikatoren

| Indikator | Bedeutung | Restlebensdauer |
|-----------|----------|----------------|
| Verfärbung am Achterliek | UV-Beginn | 70–90 % |
| Leichte Falten bei Nullwind | Profilverlust beginnt | 60–80 % |
| Fadenzug sichtbar | Materialermüdung | 40–60 % |
| Achterliek-Flattern trotz Leech Line | Fortgeschrittener Profilverlust | 30–50 % |
| Transparente Stellen (Dacron) | Harz-Verlust, Gewebe dünn | 20–40 % |
| Delamination sichtbar | Strukturelle Schwächung | 10–30 % |
| Risse an Verstärkungen | Segel am Lebensende | 0–20 % |

#### 10.2.2 Funktionale Indikatoren

| Indikator | Beschreibung | Handlung |
|-----------|-------------|---------|
| Draft > 15 % am Wind | Segel ist "bauchig" geworden | Segelmacher-Check |
| Draft Position > 55 % | Profil zu weit achtern | Segel ersetzen |
| Höheverlust > 5° | Boot zeigt weniger am Wind | Segel ersetzen |
| Geschwindigkeitsverlust > 10 % | Vergleich mit Polartabelle | Segel ersetzen |
| Reffen bringt keine Verbesserung | Profil auch gerefft zu tief | Segel ersetzen |

### 10.3 Inspektionsprotokoll

#### 10.3.1 Saisonstart-Inspektion (jährlich)

| Prüfpunkt | Methode | Dauer |
|-----------|---------|-------|
| Vorliek: Boltrope/Slides | Visuell + manuell | 10 min |
| Achterliek: Saum, Leech Line | Visuell | 5 min |
| Unterliek: Outhaul-Öse, Saum | Visuell | 5 min |
| Ecken: Kopf, Hals, Schothorn | Visuell + manuell | 10 min |
| Reffpunkte: Ösen, Verstärkungen | Visuell + manuell | 10 min |
| Latten: Integrität, Spannung | Manuell | 10 min |
| Lattentaschen: Nähte, Velcro | Visuell | 5 min |
| Segeltuch: UV-Schäden, Risse | Visuell (Gegenlicht) | 10 min |
| Cunningham-Öse | Visuell + manuell | 5 min |
| Nähte: Stichbild, Festigkeit | Visuell + manuell | 10 min |
| UV-Schutzstreifen | Visuell | 5 min |

**Gesamtdauer:** ca. 90 Minuten

#### 10.3.2 Mid-Season-Check (alle 2 Monate)

- Achterliek-Zustand (Flattern, Saum)
- Latten (Bruch, Spannung)
- Scheuerstellen (Salingen, Backstag)
- Reffpunkte (Ösen, Leinen)
- Allgemeiner Zustand (Risse, Fadenzug)

**Gesamtdauer:** ca. 30 Minuten

#### 10.3.3 Saisonende-Inspektion

Wie Saisonstart, plus:
- Segel gewaschen und vollständig getrocknet lagern
- Latten entfernen (reduziert Lattentaschen-Belastung)
- Lose Falten legen (nicht scharf knicken!)
- In trockenem, dunklem Raum lagern
- Segeltasche beschriften (Datum, Zustand, Reparaturbedarf)

### 10.4 Lebensdauerverlängerung

| Maßnahme | Lebensdauer-Effekt | Kosten |
|---------|-------------------|--------|
| UV-Schutzstreifen erneuern | +1–2 Saisons | € 150–400 |
| Persenning/StackPack verwenden | +2–4 Saisons | € 300–1.500 |
| Segel nicht permanent gesetzt | +1–3 Saisons | € 0 |
| Korrekt trimmen (kein Flattern) | +1–2 Saisons | € 0 |
| Segel nach Gebrauch trocknen | +1 Saison | € 0 |
| Professionelle Reinigung (2-jährlich) | +1 Saison | € 100–300 |
| Segelmacher-Inspektion (jährlich) | Frühzeitige Reparatur | € 80–150 |

---

## 11. Kosten

### 11.1 Neusegel-Preise nach Bootsgröße und Kategorie

#### 11.1.1 Segel für 30-Fuß-Yachten (ca. 25 m² Segelfläche)

| Kategorie | Material | Preis (€) | Hersteller-Beispiel |
|-----------|----------|----------|-------------------|
| Budget | Dacron Standard | 1.000–1.800 | Rolly Tasker RT Economy |
| Mittelklasse | Dacron Premium | 1.800–2.800 | North Dacron, Elvström Dacron |
| Performance | Pentex Tri-Radial | 2.500–4.000 | Doyle Stratis GP, Quantum Q2 |
| High Performance | Carbon Membran | 4.000–7.000 | 3Di NPC, EPEX Performance |
| Racing | Carbon HM | 6.000–10.000 | 3Di RAW, Stratis ICE |

#### 11.1.2 Segel für 35-Fuß-Yachten (ca. 35 m² Segelfläche)

| Kategorie | Material | Preis (€) | Hersteller-Beispiel |
|-----------|----------|----------|-------------------|
| Budget | Dacron Standard | 1.400–2.200 | Rolly Tasker RT Economy |
| Mittelklasse | Dacron Premium | 2.200–3.500 | North Dacron, UK Dacron |
| Performance | Pentex/Technora | 3.500–5.500 | UK X-Drive, Quantum Q2 |
| High Performance | Carbon Membran | 5.500–8.500 | 3Di NORDAC, EPEX Performance |
| Racing | Carbon HM | 8.000–12.000 | 3Di RAW, EPEX Racing |

#### 11.1.3 Segel für 40-Fuß-Yachten (ca. 50 m² Segelfläche)

| Kategorie | Material | Preis (€) | Hersteller-Beispiel |
|-----------|----------|----------|-------------------|
| Budget | Dacron Standard | 2.000–3.200 | Rolly Tasker RT Cruising |
| Mittelklasse | Dacron Premium | 3.200–5.000 | North Dacron, Elvström Dacron |
| Performance | Pentex/Technora | 5.000–8.000 | Doyle Stratis Delta, UK X-Drive |
| High Performance | Carbon Membran | 8.000–13.000 | 3Di NORDAC, EPEX Performance |
| Racing | Carbon HM | 12.000–18.000 | 3Di RAW, Stratis ICE |

#### 11.1.4 Segel für 45-Fuß-Yachten (ca. 65 m² Segelfläche)

| Kategorie | Material | Preis (€) | Hersteller-Beispiel |
|-----------|----------|----------|-------------------|
| Budget | Dacron Standard | 2.800–4.200 | Rolly Tasker RT Cruising |
| Mittelklasse | Dacron Premium | 4.200–6.500 | North Dacron, Doyle Dacron |
| Performance | Pentex/Technora | 6.500–10.000 | Quantum Fusion M, Stratis GTi |
| High Performance | Carbon Membran | 10.000–16.000 | 3Di NORDAC, EPEX Performance |
| Racing | Carbon HM | 15.000–24.000 | 3Di RAW, Stratis ICE |

#### 11.1.5 Segel für 50-Fuß-Yachten (ca. 85 m² Segelfläche)

| Kategorie | Material | Preis (€) | Hersteller-Beispiel |
|-----------|----------|----------|-------------------|
| Budget | Dacron Standard | 3.800–5.800 | Rolly Tasker RT Cruising |
| Mittelklasse | Dacron Premium | 5.800–9.000 | North Dacron, UK Dacron |
| Performance | Pentex/Technora | 9.000–14.000 | Doyle Stratis Delta, UK X-Drive |
| High Performance | Carbon Membran | 14.000–22.000 | 3Di NORDAC, EPEX Performance |
| Racing | Carbon HM | 20.000–30.000 | 3Di RAW, Stratis ICE |

### 11.2 Zusatzkosten

#### 11.2.1 Optionen und Upgrades

| Option | Aufpreis | Empfehlung |
|--------|---------|-----------|
| Volllatten (statt Teillatten) | € 300–1.200 | Empfohlen für alle Cruiser |
| Square-Top-Kopf | € 500–2.000 | Performance-Cruiser und Regatta |
| Carbon-Latten (statt GFK) | € 200–800 | Empfohlen für obere Latten |
| Loose Foot | € 0–200 | Geschmackssache |
| UV-Schutzstreifen (Premium) | € 200–500 | Empfohlen in UV-Revieren |
| Reef-Points (3. Reff) | € 200–600 | Empfohlen für Hochseesegeln |
| Cunningham-Öse (verstärkt) | € 50–150 | Empfohlen |
| Segelnummer/Logo | € 100–400 | Optional |
| Dacron-Fenster (Sichtfenster) | € 80–200 | Empfohlen |
| Telltaltes (eingenäht) | € 30–80 | Empfohlen |

#### 11.2.2 Bergesystem-Kosten

| System | Material | Installation | Gesamt |
|--------|---------|-------------|--------|
| Lazy Jacks (einfach) | € 80–200 | € 150–350 | € 230–550 |
| Lazy Jacks (einziehbar) | € 200–500 | € 200–400 | € 400–900 |
| Dutchman-System | € 200–400 | € 150–300 | € 350–700 |
| StackPack/Lazy Bag | € 350–1.200 | € 200–500 | € 550–1.700 |
| In-Mast-Rollreff (nur System) | € 2.500–12.000 | € 1.000–3.000 | € 3.500–15.000 |
| In-Boom-Rollreff (nur Baum) | € 5.000–25.000 | € 1.500–4.000 | € 6.500–29.000 |

### 11.3 Reparaturkosten

| Reparatur | Kosten (€) | Dauer |
|-----------|-----------|-------|
| Naht nachbessern (lokal) | 60–150 | 1–2 h |
| Flicken aufnähen (< 200 mm) | 80–200 | 1–3 h |
| Flicken aufnähen (> 200 mm) | 150–400 | 2–4 h |
| Lattentasche erneuern | 120–350 | 2–4 h |
| Achterliek-Saum erneuern | 200–600 | 4–8 h |
| UV-Schutzstreifen erneuern | 200–500 | 3–6 h |
| Reffpunkt reparieren | 150–400 | 2–4 h |
| Schothorn-Verstärkung erneuern | 200–600 | 3–6 h |
| Kopfbrett ersetzen | 150–400 | 3–5 h |
| Boltrope/Vorliek erneuern | 300–800 | 6–12 h |
| Cunningham-Öse erneuern | 100–250 | 1–3 h |
| Leech Line ersetzen | 50–150 | 1–2 h |
| Slide/Slug ersetzen (pro Stk) | 10–25 | 15 min |

### 11.4 Laufende Kosten (jährlich)

| Posten | Kosten/Jahr (€) | Anmerkung |
|--------|----------------|-----------|
| Inspektion (Segelmacher) | 80–200 | Empfohlen jährlich |
| Reinigung | 50–200 | Professionell alle 2 Jahre |
| Kleinreparaturen | 50–200 | Durchschnitt |
| StackPack/Persenning | 0–50 | Reißverschlüsse, Nähte |
| Gleitmittel (McLube etc.) | 15–30 | Mastnut, Slides |
| Gesamt (Durchschnitt) | 200–600 | Pro Saison |

---

## 12. FAQ

### FAQ 1: Wie oft muss ich mein Großsegel ersetzen?

**Antwort:** Die Lebensdauer hängt stark vom Material und der Nutzung ab.
Ein Dacron-Großsegel hält bei normaler Fahrtenbenutzung (200–400 Stunden/Saison)
typischerweise 6–10 Saisons. Laminatsegel halten 4–8 Saisons, Membransegel
(3Di, EPEX) 6–15 Saisons. Regatta-Nutzung reduziert die Lebensdauer um ca. 40 %.
UV-Exposition und falsche Lagerung sind die größten Lebensdauer-Killer.

### FAQ 2: Volllatten oder Teillatten?

**Antwort:** Für die meisten Fahrtenyachten ab 30 Fuß empfehlen wir Volllatten.
Die Vorteile (besseres Profil, ruhigeres Stehen, längere Lebensdauer) überwiegen
die Nachteile (Mehrgewicht, Mehrkosten). Teillatten sind nur bei kleinen Booten
(<28 ft) oder bei Budget-Beschränkung eine sinnvolle Alternative.

### FAQ 3: Lohnt sich 3Di / EPEX / Stratis für Fahrtensegler?

**Antwort:** Ja, wenn Sie das Budget haben und Performance schätzen. Die
Cruising-Versionen (3Di ENDURE, EPEX Cruising Plus, Stratis Delta) bieten
eine hervorragende Kombination aus Formhaltung und Langlebigkeit. Der
Mehrpreis von 50–100 % gegenüber Dacron Premium amortisiert sich durch
die längere Lebensdauer. Nachteil: Reparaturen sind teurer und oft nur
beim Hersteller möglich.

### FAQ 4: In-Mast oder In-Boom Rollreff?

**Antwort:** In-Mast ist einfacher und bewährter, hat aber 15–25 %
Leistungseinbuße (kein Roach, flacher Schnitt). In-Boom erlaubt Latten
und Roach (nur 5–10 % Leistungseinbuße), ist aber teurer und mechanisch
komplexer. Für Komfort-Cruiser, die vorwiegend unter Motor fahren: In-Mast.
Für Performance-Cruiser, die gern segeln: In-Boom oder Slab Reefing.

### FAQ 5: Was kostet ein Großsegel für meine 40-Fuß-Yacht?

**Antwort:** Abhängig von Material und Hersteller:
- Budget (Dacron Standard): € 2.000–3.200
- Mittelklasse (Dacron Premium): € 3.200–5.000
- Performance (Pentex/Technora): € 5.000–8.000
- High Performance (Carbon Membran): € 8.000–13.000
Dazu kommen ggf. Optionen (Volllatten, UV-Schutz, etc.): € 500–2.000

### FAQ 6: Wie lagere ich mein Großsegel am besten?

**Antwort:** Segel vollständig trocknen lassen (nie nass lagern!). Latten
entfernen. Locker zusammenfalten (nicht scharf knicken, besonders bei
Laminaten). In Segelsack in trockenem, dunklem, temperiertem Raum lagern.
Kein Dachboden (Hitze!), kein Keller (Feuchtigkeit!). Alternativ:
Persenning/StackPack am Baum, wenn UV-Schutz gewährleistet ist.

### FAQ 7: Kann ich mein Großsegel selbst reparieren?

**Antwort:** Kleine Reparaturen (Segelreparaturband für unterwegs, Naht
nachbessern mit Handnähgerät) sind möglich und empfohlen als Notmaßnahme.
Dauerhafte Reparaturen sollten immer vom Segelmacher ausgeführt werden.
Laminat- und Membransegel können nur vom Hersteller repariert werden.

### FAQ 8: Was sind die häufigsten Fehler beim Großsegeltrimm?

**Antwort:** Die fünf häufigsten Fehler:
1. Zu viel Schot (Achterliek zu geschlossen → Boot bremst)
2. Traveller vergessen (steht mittschiffs bei Starkwind → zu viel Krängung)
3. Cunningham nie benutzt (Profil wandert bei Wind nach achtern)
4. Outhaul nie verstellt (Standardposition für alle Bedingungen)
5. Kicker zu lose auf Raumschotkurs (Twist nicht kontrolliert)

### FAQ 9: Woran erkenne ich, dass mein Segel ausgeweht ist?

**Antwort:** Ein ausgewehtes Segel zeigt:
- Profil tiefer als 15 % (Bauch hängt durch)
- Draft-Position hinter 50 % (Bauch zu weit achtern)
- Achterliek flattert trotz angezogener Leech Line
- Horizontale Falten parallel zum Baum (Material gedehnt)
- Transparente/dünne Stellen (gegen Licht sichtbar)
- Höheverlust von >5° gegenüber Neuzustand

### FAQ 10: Wie messe ich mein Segel für eine Neubestellung?

**Antwort:** Folgende Maße werden benötigt:
- P (Vorlieklänge): Mastschiene unten bis Salingspin oben
- E (Unterlieklänge): Mast-Achterkante bis Baum-Ende
- Mastprofil: Breite × Tiefe in mm
- Mastnut-Breite: Innere Nutenbreite in mm
- Baumprofil: Breite × Tiefe in mm
- Slide/Slug-System: Typ und Größe
- Reffpunkte: Anzahl und gewünschte Positionen
Am besten: Altes Segel dem Segelmacher geben.

### FAQ 11: Muss ich bei einem Großsegel für In-Mast-Rollreff auf Leistung verzichten?

**Antwort:** Ja, aber weniger als oft angenommen. Moderne In-Mast-Segel
mit Vertikallatten und optimiertem Schnitt verlieren ca. 10–15 % an Höhe
und ca. 5–10 % an Geschwindigkeit am Wind. Auf Raumschotkursen ist der
Unterschied geringer. Für Fahrtensegler, die Komfort und Sicherheit
priorisieren, ist dieser Verlust akzeptabel.

### FAQ 12: Was ist der Unterschied zwischen Cross-Cut und Tri-Radial?

**Antwort:** Cross-Cut: Horizontale Bahnen, einfachste Fertigung,
niedrigste Kosten, gut für Dacron. Tri-Radial: Bahnen strahlen von den
drei Ecken aus, bessere Faserausrichtung entlang der Lastpfade, geringere
Dehnung, längere Profillhaltung, 20–40 % teurer. Empfehlung: Cross-Cut
für Budget-Dacron, Tri-Radial für Premium-Dacron und Pentex.

### FAQ 13: Wie wichtig ist der UV-Schutzstreifen?

**Antwort:** Sehr wichtig in UV-intensiven Revieren (Mittelmeer, Tropen,
Karibik). Ein UV-Schutzstreifen am Achterliek und Unterliek verlängert
die Segellebensdauer um 1–3 Saisons. Kosten: € 200–500 als Option beim
Neusegel, € 200–500 für nachträgliches Anbringen. Alternativ oder
zusätzlich: Persenning/StackPack.

### FAQ 14: Square-Top — lohnt sich das?

**Antwort:** Square-Top-Segel bieten 10–20 % mehr Segelfläche oben und
besseres Höhelaufen. Lohnt sich für: Performance-Cruiser mit modernem Rigg,
Regatta-orientierte Segler. Lohnt sich NICHT für: In-Mast-Rollreff, ältere
Riggs ohne ausreichende Festigkeit, reine Langfahrt-Yachten.

### FAQ 15: Wie oft sollte ich mein Großsegel waschen?

**Antwort:** Professionelle Reinigung (Segelmacher, Segelwaschdienst) alle
2–3 Saisons. Dazwischen: Süßwasser-Spülung nach Salzwasser. Kein
Hochdruckreiniger (beschädigt Beschichtung)! Keine aggressiven Reiniger.
Spezielle Segelreiniger verwenden (z.B. Sail Kleen, SnappySail).
Kosten: € 50–200 für professionelle Wäsche (abhängig von Segelgröße).

### FAQ 16: Kann ich ein Dacron-Segel auf ein Laminat upgraden?

**Antwort:** Ja, wenn Rigg und Beschläge kompatibel sind. Beim Upgrade
auf Membran/Laminat prüfen: Mastschiene/Slides kompatibel? Battcars nötig?
Kopfbeschlag passend? Fall-Durchmesser? Die Umrüstung auf Volllatten
erfordert ggf. neue Battcars (€ 500–2.000 zusätzlich).

### FAQ 17: Was ist ein Trysegel und brauche ich eines?

**Antwort:** Ein Trysegel (Sturmgroßsegel) ist ein kleines, schweres
Großsegel ohne Baum, das bei Sturmstärke (>40 kn) gesetzt wird. Es wird
direkt an Schot-Punkten am Deck gefahren. Pflicht für Hochsee/Langfahrt
(ISAF/ORC-Vorschrift für Offshore-Regatten). Empfohlen für alle Yachten,
die das Revier verlassen. Kosten: € 400–1.200.

### FAQ 18: Wie beeinflusst die Mastbiegung mein Großsegel?

**Antwort:** Mastbiegung flacht das Großsegel ab (weniger Draft). Ein
flexibler Mast ermöglicht größere Trimmvarianz, erfordert aber ein
Segel mit entsprechender Luff Curve. Zu viel Mastbiegung erzeugt
diagonale Falten vom Achterliek zum Mast ("overbend wrinkles"). Jedes
Segel muss auf den spezifischen Mast abgestimmt sein.

### FAQ 19: Was mache ich, wenn eine Latte bricht?

**Antwort:** Kurzfristig: Segel kann mit gebrochener Latte weitergesegelt
werden (reduzierte Leistung, erhöhter Verschleiß an der Lattentasche).
Langfristig: Latte so schnell wie möglich ersetzen. CFK-Latten-Bruch:
Vorsicht vor scharfen Kanten! Empfehlung: Immer 1–2 Ersatzlatten an Bord.

### FAQ 20: Kann ich mein Großsegel zum Segelmacher bringen oder muss ich den Hersteller kontaktieren?

**Antwort:** Dacron- und konventionelle Laminatsegel: Jeder qualifizierte
Segelmacher kann reparieren. 3Di, EPEX, Stratis: Nur Hersteller-Lofts
können diese Segel reparieren (spezielle Maschinen und Materialien).
UK X-Drive: Von jedem Segelmacher reparierbar (Dacron-Basis).

### FAQ 21: Wie beeinflusst die Segelfläche die Rumpfgeschwindigkeit?

**Antwort:** Die Segelfläche beeinflusst die Geschwindigkeit bis zur
theoretischen Rumpfgeschwindigkeit (1,34 × √LWL in Fuß = Kn). Mehr
Segelfläche erreicht die Rumpfgeschwindigkeit bei weniger Wind.
Überdimensioniertes Segel bringt über Rumpfgeschwindigkeit keinen
Vorteil (außer bei Gleitern/Halbgleitern).

### FAQ 22: Was bedeutet "Roach" genau?

**Antwort:** Roach ist die konvexe Überhöhung des Achterlieks über die
gerade Verbindungslinie Kopf–Schothorn. Wird in Prozent der geraden
Verbindungslinie angegeben. Mehr Roach = mehr Segelfläche = mehr Leistung.
Erfordert Latten zur Stützung. Typisch: 5–25 % je nach Segeltyp.

### FAQ 23: Warum flattert mein Großsegel beim Ankern?

**Antwort:** Vor Anker, Bug im Wind, steht das Großsegel permanent in der
Windabdeckung des Mastes und flattert. Dies beschleunigt den Verschleiß
erheblich. Lösung: Segel bergen, Persenning aufziehen, oder StackPack
schließen. Niemals ein Großsegel unnötig flattern lassen!

### FAQ 24: Welches Großsegel für einen Katamaran?

**Antwort:** Katamarane erzeugen weniger Krängung, aber höhere
Geschwindigkeiten (mehr scheinbarer Wind). Empfehlung:
- Material: Mindestens Dacron Premium, besser Pentex oder Membran
- Schnitt: Flat-Cut für Performance, etwas Bauch für Leichtwind
- Latten: Volllatten empfohlen (Square-Top bei Performance-Kats)
- Reefing: Slab oder In-Boom bevorzugt
- Kein In-Mast (Leistungsverlust bei Kats besonders nachteilig)

### FAQ 25: Wie entsorge ich ein altes Großsegel umweltgerecht?

**Antwort:** Optionen:
1. Upcycling: Segeltaschen, Windschutz, Abdeckungen (Segelmanufakturen)
2. Spende: Segelclubs, Jugendabteilungen, Entwicklungsländer
3. Recycling: Dacron (PET) theoretisch recycelbar, Laminate schwierig
4. Restmüll: Letzter Ausweg, da Segelmaterial nicht biologisch abbaubar
Empfehlung: Upcycling oder Spende bevorzugen.

### FAQ 26: Brauche ich bei einem Rollgroß-Segel Lazy Jacks?

**Antwort:** Bei In-Mast-Rollreff: Nein, Segel wird im Mast geborgen.
Bei In-Boom-Rollreff: Nein, Segel wird im Baum geborgen.
Bei konventionellem Segel mit Slab Reefing: Lazy Jacks sind sehr
empfehlenswert, besonders bei Volllatten-Segeln (Segel fällt
kontrolliert auf den Baum).

### FAQ 27: Wie beeinflusst Salzwasser das Segelmaterial?

**Antwort:** Salzkristalle sind abrasiv und hygrosokopisch (ziehen
Feuchtigkeit an). Salzrückstände auf dem Segel beschleunigen:
- UV-Degradation (Salz als Katalysator)
- Materialermüdung (Abrasion durch Kristalle)
- Schimmelbildung (Feuchtigkeit in Salzkruste)
Prävention: Regelmäßig mit Süßwasser spülen, besonders vor Einlagerung.

---

## 13. Glossar

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|-----------|
| Achterliek | Leech | Hintere Kante des Segels, vom Kopf zum Schothorn |
| Achterstag | Backstay | Stag vom Masttopp nach achtern, stabilisiert den Mast |
| Anstellwinkel | Angle of Attack | Winkel zwischen Segelprofil-Sehne und Windrichtung |
| Bauch | Draft / Camber | Profiltiefe des Segels in Prozent der Sehnenlänge |
| Baum | Boom | Horizontaler Spier am unteren Ende des Großsegels |
| Baumniederholer | Vang / Kicking Strap | System zur Kontrolle der Achterliekspannung |
| Boltrope | Bolt Rope | Liektau, eingenäht in das Vorliek |
| Broadseam | Broadseam | Gekrümmte Naht zur Profilgebung |
| Bullenstander | Preventer | Leine zur Fixierung des Baums (verhindert Patenthalse) |
| Cunningham | Cunningham | Vorliekstrecker, verschiebt Profiltiefe nach vorne |
| Dacron | Dacron | Markenname für Polyester-Segelgewebe |
| Delamination | Delamination | Ablösung der Schichten in Laminatsegeln |
| Druckpunkt | Centre of Effort (CE) | Geometrischer Schwerpunkt der Windkraft im Segel |
| Fieren | Ease / Let out | Leine nachlassen, lockern |
| Großschot | Mainsheet | Hauptleine zur Trimmung des Großsegels |
| Hals | Tack | Untere vordere Ecke des Großsegels |
| Halse | Gybe / Jibe | Kurswechsel mit dem Heck durch den Wind |
| Kopf | Head | Obere Ecke des Großsegels |
| Kopfbrett | Headboard | Verstärkungsplatte am Segelkopf |
| Krängen | Heeling | Seitliche Neigung des Bootes unter Windeinfluss |
| Latte | Batten | Verstärkungsstab im Segel zur Profilstützung |
| Lattentasche | Batten Pocket | Tasche im Segel zur Aufnahme der Latte |
| Leech Line | Leech Line | Dünne Leine im Achterliek-Saum zur Flatter-Kontrolle |
| Lümmelbeschlag | Gooseneck | Gelenk-Beschlag am Mast für den Baumansatz |
| Luff Curve | Luff Curve | Konvexe Krümmung des Vorlieks |
| Luvgierigkeit | Weather Helm | Tendenz des Bootes, in den Wind zu drehen |
| Mast | Mast | Vertikaler Spier, der das Segel trägt |
| Outhaul | Outhaul | Unterliekstrecker, kontrolliert Profiltiefe am Fuß |
| Patenthalse | Accidental Gybe | Unkontrollierte Halse (Sicherheitsrisiko) |
| Profil | Sail Shape / Profile | Querschnittsform des Segels |
| Reffen | Reefing | Reduzierung der Segelfläche bei zunehmendem Wind |
| Roach | Roach | Konvexe Überhöhung des Achterlieks |
| Rutscher | Slide / Slug | Befestigungselement am Vorliek für die Mastschiene |
| Saling | Spreader | Querstab am Mast zur Wantenabspreizung |
| Schothorn | Clew | Untere hintere Ecke des Großsegels |
| Slot-Effekt | Slot Effect | Aerodynamische Wechselwirkung Vorsegel-Großsegel |
| Traveller | Traveller | Schiene zur Querschiffsverstellung des Großschot-Blocks |
| Trimm | Trim | Einstellung des Segels für optimale Leistung |
| Trysegel | Trysail / Storm Trysail | Kleines Sturmsegel, das das Großsegel ersetzt |
| Twist | Twist | Verdrehung des Segelprofils von unten nach oben |
| Unterliek | Foot | Untere Kante des Segels, zwischen Hals und Schothorn |
| Vorliek | Luff | Vordere Kante des Segels, am Mast befestigt |
| Wende | Tack | Kurswechsel mit dem Bug durch den Wind |
| Wanten | Shrouds | Seitliche Drähte/Stagen zur Maststabilisierung |

---

## 14. Schnell-Referenz

### 14.1 Großsegel-Entscheidungsmatrix

```
Welches Großsegel passt zu mir?

Frage 1: Budget?
├── < € 3.000 → Dacron Standard oder Economy → Rolly Tasker, lokaler Segelmacher
├── € 3.000–6.000 → Dacron Premium oder Pentex → North, Elvström, Doyle, UK
├── € 6.000–12.000 → Membran Cruising → 3Di ENDURE/NPC, EPEX Cruising, Stratis Delta
└── > € 12.000 → Membran Performance/Racing → 3Di NORDAC/RAW, EPEX Racing, Stratis ICE

Frage 2: Reefing-System?
├── Slab Reefing → Alle Materialien, alle Typen, beste Performance
├── In-Mast → Nur Dacron/Pentex, kein Roach, flacher Schnitt
└── In-Boom → Alle Materialien, moderate Roach, Volllatten möglich

Frage 3: Priorität?
├── Komfort/Einfachheit → In-Mast oder In-Boom + Dacron/Pentex
├── Langlebigkeit → Dacron Premium oder 3Di ENDURE + Persenning
├── Performance → Membran + Volllatten + Square-Top
└── Budget → Dacron Standard + Cross-Cut + Teillatten
```

### 14.2 Trimm-Kurzanleitung

```
Wind zunehmend? Abflachen!
1. Traveller nach Lee
2. Cunningham anziehen
3. Outhaul dicht
4. Achterstag dicht
5. Immer noch zu viel? → 1. Reff

Wind abnehmend? Füllen!
1. Achterstag fieren
2. Outhaul los
3. Cunningham los
4. Traveller nach Luv
5. Immer noch zu wenig? → Reff ausschütteln
```

### 14.3 Wartungskalender

```
Vor jeder Fahrt:
- Slides/Slugs: Laufen frei?
- Latten: Alle vorhanden?
- Schot, Kicker, Cunningham: Klar?

Monatlich:
- Achterliek: Flattern, Saum
- Scheuerstellen prüfen
- Leech Line: Funktion

Saisonstart:
- Vollinspektion (90 min, siehe 10.3.1)
- Mastnut reinigen + Gleitmittel
- Slides prüfen und ggf. ersetzen

Saisonende:
- Segel waschen + trocknen
- Latten entfernen
- Locker falten, in Segelsack
- Dunkel + trocken lagern
```

### 14.4 Notfall-Kontakte

| Situation | Sofortmaßnahme |
|-----------|---------------|
| Schothorn ausgerissen | Segel sofort bergen, unter Motor fahren |
| Kopfbrett gebrochen | Segel sofort bergen, Trysegel setzen |
| In-Mast verklemmt | Nicht forcieren! Protokoll 9.5 befolgen |
| Latte gebrochen | Weiterfahrt möglich, bald ersetzen |
| Achterliek aufgerissen | Reffen bis unter den Riss, Segelmacher |
| Boltrope gerissen | Segel sofort bergen, Segelmacher |

---

## 15. ANHANG A–H: Fallstudien

### ANHANG A: Bavaria 40 Cruiser — Dacron-Großsegel-Ersatz nach 8 Saisons

#### A.1 Ausgangslage

- **Yacht**: Bavaria 40 Cruiser, Baujahr 2016
- **Revier**: Ostsee, 300–400 Stunden/Saison
- **Altes Segel**: OEM Dacron (Rolly Tasker), Cross-Cut, Teillatten
- **Zustand**: Profil ausgeweht (Draft 16 %, Position 55 %), UV-Schäden am Achterliek,
  2 Latten gebrochen, Schothorn-Verstärkung angerissen

#### A.2 Analyse (AYDI)

- Konfidenz: visual_medium + estimated
- Befund: Segel am Lebensende (geschätzte Restlebensdauer: 0–1 Saison)
- Empfehlung: Ersatz, Upgrade auf Volllatten empfohlen

#### A.3 Entscheidung

Eigentümer entschied sich für:
- North Dacron Premium, Tri-Radial, Volllatten (4 GFK-Latten)
- UV-Schutzstreifen, Cunningham-Öse verstärkt, 2 Reffpunkte
- StackPack (ATN) als Bergesystem

#### A.4 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Segel (North Dacron Premium, 50 m², Tri-Radial, Volllatten) | 4.200 |
| StackPack (ATN) | 650 |
| Battcars (4× Harken, Montage) | 680 |
| Lazy Jacks (einziehbar) | 350 |
| Installation | 400 |
| **Gesamt** | **6.280** |

#### A.5 Ergebnis

- Höheverlust: +4° gegenüber altem Segel
- Geschwindigkeit: +0,5 kn am Wind, +0,3 kn Raumschots
- Handling: Deutlich verbessert (Volllatten, StackPack)
- Erwartete Lebensdauer: 8–10 Saisons

### ANHANG B: Hallberg-Rassy 43 — Upgrade von Dacron auf 3Di ENDURE

#### B.1 Ausgangslage

- **Yacht**: Hallberg-Rassy 43 MkII, Baujahr 2018
- **Revier**: Nordsee, Atlantik (Langfahrt geplant)
- **Altes Segel**: Elvström Dacron Premium, Cross-Cut, Teillatten, 4 Saisons alt
- **Motivation**: Vorbereitung für Atlantiküberquerung, bessere Performance gewünscht

#### B.2 Analyse

- Altes Segel in gutem Zustand (noch 3–5 Saisons Restleben)
- Profilmessungen: Draft 12 %, Position 45 % → akzeptabel
- Upgrade primär aus Performance-Gründen, nicht aus Verschleißgründen

#### B.3 Entscheidung

- North 3Di ENDURE, Volllatten (4 GFK + 1 CFK oben)
- UV-Schutzstreifen Premium, 3 Reffpunkte, Square-Top-Option verworfen (HR 43 Rigg nicht optimiert)
- Bestehendes StackPack weiterverwendet

#### B.4 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Segel (3Di ENDURE, 65 m², Volllatten) | 8.500 |
| CFK-Oberlatte | 120 |
| Battcar-Upgrade (5× Harken) | 850 |
| Vermessung + Anpassung | 300 |
| **Gesamt** | **9.770** |

#### B.5 Ergebnis

- Höheverlust: +3° gegenüber neuem Dacron (signifikant)
- VMG am Wind: +8 % (nach Polare)
- Profilstabilität: Segel behält Form bei 25 kn (Dacron wurde ab 18 kn "bauchig")
- Erwartete Lebensdauer: 12–15 Saisons (bei Langfahrt-Nutzung)
- Altes Segel als Reservesegel an Bord behalten

### ANHANG C: Jeanneau Sun Odyssey 349 — Budget-Großsegel für Charterbetrieb

#### C.1 Ausgangslage

- **Yacht**: Jeanneau SO 349, Baujahr 2019, Charterboot in Kroatien
- **Anforderung**: Robustes, günstiges Segel, einfach zu bedienen
- **Bisheriges Segel**: OEM Dacron (3 Saisons Charter → verschlissen)

#### C.2 Analyse

- Charter-Nutzung: 1.200+ Stunden in 3 Saisons
- UV-Belastung extrem (Kroatien, selten Persenning benutzt)
- Segel stark ausgeweht, UV-Schäden erheblich
- Budget: maximal € 2.000

#### C.3 Entscheidung

- Rolly Tasker RT Cruising, Dacron Premium, Cross-Cut
- UV-Schutzstreifen (beidseitig), 2 Reffpunkte, Teillatten
- Neues StackPack (günstigstes Modell)

#### C.4 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Segel (RT Cruising, 30 m², Cross-Cut) | 1.400 |
| StackPack | 380 |
| Installation (lokal in Kroatien) | 200 |
| **Gesamt** | **1.980** |

#### C.5 Ergebnis

- Gutes Preis-Leistungs-Verhältnis
- Lieferzeit: 8 Wochen ab Bestellung
- Qualität: Gut für Charterboot (robuste Verstärkungen)
- Erwartete Lebensdauer: 4–5 Charter-Saisons (mit Persenning-Disziplin)

### ANHANG D: Contest 42CS — In-Mast-Rollreff Problembehebung

#### D.1 Ausgangslage

- **Yacht**: Contest 42CS, Baujahr 2012, Seldén-Mast mit In-Mast-Rollreff
- **Problem**: Großsegel klemmt regelmäßig beim Einrollen (ca. alle 5. Nutzung)
- **Alter Segel**: OEM In-Mast-Segel, 6 Saisons, Dacron

#### D.2 Diagnose (AYDI)

1. Mastnut gereinigt und inspiziert → leichter Grat bei 4 m Höhe (Ursache 1)
2. Vertikale Latten: 2 von 4 verbogen (Ursache 2)
3. Fall-Spannung: inkonsistent (Bedienfehler) (Ursache 3)
4. Segel-Zustand: Moderate UV-Schäden, Profil akzeptabel

#### D.3 Maßnahmen

| Maßnahme | Kosten (€) |
|---------|-----------|
| Mastnut schleifen und polieren | 250 |
| 4 neue Vertikallatten (GFK) | 60 |
| Fall-Markierungen anbringen | 30 |
| Bedienungseinweisung für Eigner | 0 (im Service) |
| Silikon-Behandlung Mastnut | 25 |
| **Gesamt** | **365** |

#### D.4 Ergebnis

- Verklemmung behoben (nach 2 Saisons kein Vorfall)
- Kosten minimal (kein neues Segel erforderlich)
- Wichtigste Erkenntnis: Fall-Spannung korrekt einstellen ist entscheidend

### ANHANG E: Swan 48 — Racing-Großsegel 3Di RAW

#### E.1 Ausgangslage

- **Yacht**: Nautor Swan 48, Baujahr 2020
- **Einsatz**: ORC-Regatta (Nordsee, Mittelmeer), einige Langstrecken
- **Anforderung**: Maximale Performance, Carbon HM, Square-Top

#### E.2 Entscheidung

- North 3Di RAW 760, Volllatten (5 CFK), Square-Top
- Kein UV-Schutz (Segel wird nach Regatta immer geborgen)
- 2 Reffpunkte, verstärktes Schothorn (Regatta-Belastungen)

#### E.3 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Segel (3Di RAW, 75 m², Carbon HM, Square-Top) | 18.500 |
| CFK-Latten (5×) | 550 |
| Battcars (5× Harken Racing) | 1.200 |
| Vermessung + Design | 500 |
| **Gesamt** | **20.750** |

#### E.4 Ergebnis

- Performance: Exzellent, Boot erreicht ORC-Polare konsistent
- VMG am Wind: +12 % gegenüber altem Laminat-Segel
- Gewicht: 3,5 kg leichter als Vorgänger-Segel
- Erwartete Lebensdauer: 3–4 Regatta-Saisons

### ANHANG F: Catana 47 — Katamaran-Großsegel mit Square-Top

#### F.1 Ausgangslage

- **Yacht**: Catana 47, Baujahr 2017
- **Revier**: Karibik, Pazifik (Langfahrt)
- **Anforderung**: Hohe Performance für Katamaran, UV-beständig

#### F.2 Entscheidung

- Doyle Stratis Delta, Volllatten (5, davon 2 CFK), Square-Top
- Premium UV-Schutzstreifen (beidseitig)
- 3 Reffpunkte (Hochsee-Anforderung)
- StackPack mit UV-Schutz

#### F.3 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Segel (Stratis Delta, 70 m², Square-Top) | 10.500 |
| CFK-Latten (2×) + GFK-Latten (3×) | 380 |
| UV-Schutz Premium (beidseitig) | 550 |
| StackPack UV-Pro | 950 |
| Installation | 450 |
| **Gesamt** | **12.830** |

#### F.4 Ergebnis

- Performance: Hervorragend, Katamaran profitiert stark vom Square-Top
- UV-Schutz: Nach 3 Saisons Karibik noch kein sichtbarer UV-Schaden
- Handling: Square-Top erfordert mehr Aufmerksamkeit beim Bergen
- Erwartete Lebensdauer: 8–10 Saisons (tropische UV-Bedingungen)

### ANHANG G: Dehler 46 — Umbau von Slab auf Single-Line Reefing

#### G.1 Ausgangslage

- **Yacht**: Dehler 46 SQ, Baujahr 2019
- **Problem**: Eigner segelt viel einhand, Slab Reefing umständlich
- **Segel**: 2 Saisons alt, Elvström EPEX Cruising, in gutem Zustand

#### G.2 Maßnahmen

Umbau des bestehenden Segels von 2-Leinen-Reff auf Single-Line-Reff:

| Maßnahme | Kosten (€) |
|---------|-----------|
| Segel-Modifikation (Reffhaken-Ösen, Umlenkungen) | 350 |
| Harken Single-Line Kit (2 Reffpunkte) | 680 |
| Neue Reffleinen (Dyneema, 10 mm, 40 m) | 240 |
| Umlenkblöcke am Mast (2×) | 120 |
| Spinlock Klemmen (2×) | 160 |
| Installation (Rigger, 1 Tag) | 500 |
| **Gesamt** | **2.050** |

#### G.3 Ergebnis

- Reffen jetzt in 45 Sekunden aus dem Cockpit (vorher: 3–5 Minuten)
- Einhandsegeln wesentlich sicherer und komfortabler
- Kein Vorschiff-Gang mehr zum Reffen nötig
- Segel unverändert gut im Profil

### ANHANG H: Beneteau Oceanis 51.1 — In-Boom-Rollreff Nachrüstung

#### H.1 Ausgangslage

- **Yacht**: Beneteau Oceanis 51.1, Baujahr 2020
- **Problem**: Slab Reefing für älteres Eigner-Ehepaar zu anstrengend
- **Anforderung**: Komfortables Reefing, keine Performance-Einbuße

#### H.2 Entscheidung

- Leisure Furl LF-300 In-Boom-System
- Neues Großsegel: UK Sailmakers Tape-Drive (Dacron + Mylar-Tape)
- Spezial-Schnitt für In-Boom (angepasste Lattentaschen)

#### H.3 Kosten

| Posten | Kosten (€) |
|--------|-----------|
| Leisure Furl LF-300 (Baum komplett) | 15.500 |
| Neues Großsegel (UK Tape-Drive, 75 m², In-Boom) | 5.800 |
| Alter Baum Demontage | 400 |
| Neuer Baum Montage + Rigg-Anpassung | 1.200 |
| Elektrischer Antrieb (Harken UniPower) | 3.500 |
| Bedienelemente + Verkabelung | 800 |
| **Gesamt** | **27.200** |

#### H.4 Ergebnis

- Reffen jetzt per Knopfdruck (elektrisch, 30 Sekunden für 1. Reff)
- Performance-Verlust: nur ca. 5–8 % (Latten und moderate Roach möglich)
- Eigner-Zufriedenheit: maximal ("Bestes Investment am Boot")
- Gewicht am Baum: +18 kg (kompensiert durch leichteres Segel)
- Erwartete Systemlebensdauer: 15–20 Jahre (mit Wartung)

---

## 16. ANHANG I–R: Pydantic v2 Modelle

### ANHANG I: MainsailSpec

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class SailMaterial(str, Enum):
    DACRON_STANDARD = "dacron_standard"
    DACRON_PREMIUM = "dacron_premium"
    PENTEX = "pentex"
    TECHNORA = "technora"
    KEVLAR = "kevlar"
    CARBON = "carbon"
    DYNEEMA = "dyneema"
    VECTRAN = "vectran"
    DCF = "dcf"
    THREE_DI_RAW = "3di_raw"
    THREE_DI_NORDAC = "3di_nordac"
    THREE_DI_NPC = "3di_npc"
    THREE_DI_ENDURE = "3di_endure"
    EPEX_RACING = "epex_racing"
    EPEX_PERFORMANCE = "epex_performance"
    EPEX_CRUISING = "epex_cruising"
    STRATIS_ICE = "stratis_ice"
    STRATIS_GTI = "stratis_gti"
    STRATIS_DELTA = "stratis_delta"
    X_DRIVE = "x_drive"
    TAPE_DRIVE = "tape_drive"
    FOUR_T_FORTE = "4t_forte"


class CutType(str, Enum):
    CROSS_CUT = "cross_cut"
    TRI_RADIAL = "tri_radial"
    RADIAL = "radial"
    MEMBRANE = "membrane"
    MOLDED = "molded"


class BattenType(str, Enum):
    NONE = "none"
    PARTIAL = "partial"
    FULL = "full"
    VERTICAL = "vertical"


class ReefingType(str, Enum):
    SLAB_TRADITIONAL = "slab_traditional"
    SLAB_SINGLE_LINE = "slab_single_line"
    SLAB_TWO_LINE = "slab_two_line"
    IN_MAST = "in_mast"
    IN_BOOM = "in_boom"


class MainsailSpec(BaseModel):
    """Spezifikation eines Großsegels mit allen relevanten Parametern."""

    model_config = {"from_attributes": True}

    # Identifikation
    hersteller: str = Field(..., description="Segelhersteller")
    modell: str = Field(..., description="Modellbezeichnung")
    baujahr: Optional[int] = Field(None, description="Baujahr des Segels")
    seriennummer: Optional[str] = Field(None, description="Seriennummer des Segels")

    # Abmessungen (mm)
    p_luff_mm: float = Field(..., description="Vorlieklänge P in mm")
    e_foot_mm: float = Field(..., description="Unterlieklänge E in mm")
    leech_mm: Optional[float] = Field(None, description="Achterlieklänge in mm")
    area_sqm: Optional[float] = Field(None, description="Segelfläche in m²")
    roach_percent: Optional[float] = Field(None, description="Roach in Prozent")
    hqw_mm: Optional[float] = Field(None, description="7/8-Segelbreite in mm")
    tqw_mm: Optional[float] = Field(None, description="3/4-Segelbreite in mm")
    hw_mm: Optional[float] = Field(None, description="1/2-Segelbreite in mm")
    qw_mm: Optional[float] = Field(None, description="1/4-Segelbreite in mm")

    # Material und Konstruktion
    material: SailMaterial = Field(..., description="Segelmaterial")
    cut_type: CutType = Field(..., description="Schnitttyp")
    gewicht_g_per_sqm: Optional[float] = Field(None, description="Tuchgewicht g/m²")

    # Latten
    batten_type: BattenType = Field(..., description="Lattentyp")
    batten_count: int = Field(0, description="Anzahl Latten")
    batten_material: Optional[str] = Field(None, description="Lattenmaterial (GFK/CFK)")

    # Reefing
    reefing_type: ReefingType = Field(..., description="Reefing-System")
    reef_points: int = Field(0, description="Anzahl Reffpunkte")

    # Features
    square_top: bool = Field(False, description="Square-Top / Fathead")
    loose_footed: bool = Field(False, description="Loses Unterliek")
    cunningham: bool = Field(True, description="Cunningham-Öse vorhanden")
    uv_protection: bool = Field(False, description="UV-Schutzstreifen vorhanden")
    leech_line: bool = Field(True, description="Achterlikleine vorhanden")
    window: bool = Field(False, description="Sichtfenster vorhanden")

    # Kompatibilität
    mast_profil_mm: Optional[str] = Field(None, description="Mastprofil Breite×Tiefe")
    mast_nut_mm: Optional[float] = Field(None, description="Mastnut-Breite in mm")
    slide_type: Optional[str] = Field(None, description="Slide/Slug-Typ und Größe")
    boom_profil_mm: Optional[str] = Field(None, description="Baumprofil Breite×Tiefe")
```

### ANHANG J: MainsailTrim

```python
class WindStrength(str, Enum):
    LIGHT = "light"          # 0-8 kn
    MEDIUM = "medium"        # 8-16 kn
    HEAVY = "heavy"          # 16-25 kn
    STORM = "storm"          # 25+ kn


class PointOfSail(str, Enum):
    CLOSE_HAULED = "close_hauled"     # 30-45°
    CLOSE_REACH = "close_reach"       # 45-60°
    BEAM_REACH = "beam_reach"         # 60-90°
    BROAD_REACH = "broad_reach"       # 90-150°
    RUN = "run"                       # 150-180°


class MainsailTrim(BaseModel):
    """Trimmeinstellungen des Großsegels für eine bestimmte Bedingung."""

    model_config = {"from_attributes": True}

    # Bedingungen
    wind_strength: WindStrength = Field(..., description="Windstärke-Bereich")
    point_of_sail: PointOfSail = Field(..., description="Kurs zum Wind")
    wind_speed_kn: Optional[float] = Field(None, description="Tatsächliche Windgeschwindigkeit in kn")

    # Trimmelemente (0.0 = voll lose, 1.0 = voll dicht)
    mainsheet_tension: float = Field(..., ge=0.0, le=1.0, description="Großschot-Spannung")
    traveller_position: float = Field(
        ..., ge=-1.0, le=1.0,
        description="Traveller-Position (-1.0=ganz Lee, 0=Mitte, 1.0=ganz Luv)"
    )
    cunningham_tension: float = Field(0.0, ge=0.0, le=1.0, description="Cunningham-Spannung")
    outhaul_tension: float = Field(..., ge=0.0, le=1.0, description="Outhaul-Spannung")
    vang_tension: float = Field(0.0, ge=0.0, le=1.0, description="Baumniederholer-Spannung")
    backstay_tension: float = Field(0.0, ge=0.0, le=1.0, description="Achterstag-Spannung")

    # Profil-Ergebnis
    draft_percent: Optional[float] = Field(None, description="Resultierende Profiltiefe %")
    draft_position_percent: Optional[float] = Field(None, description="Profilposition vom Vorliek %")
    twist_degrees: Optional[float] = Field(None, description="Twist in Grad")

    # Reefing
    reef_number: int = Field(0, ge=0, le=3, description="Aktives Reff (0=kein Reff)")

    # Anmerkungen
    notes: Optional[str] = Field(None, description="Trim-Anmerkungen (deutsch)")
```

### ANHANG K: MainsailCondition

```python
from datetime import date


class ConditionRating(str, Enum):
    EXCELLENT = "excellent"     # Neuzustand
    GOOD = "good"               # Geringe Gebrauchsspuren
    FAIR = "fair"               # Deutliche Gebrauchsspuren, noch funktional
    POOR = "poor"               # Erheblicher Verschleiß, Leistungseinbuße
    END_OF_LIFE = "end_of_life" # Am Lebensende, Ersatz empfohlen
    DAMAGED = "damaged"         # Beschädigt, nicht einsatzfähig


class MainsailCondition(BaseModel):
    """Zustandsbewertung eines Großsegels."""

    model_config = {"from_attributes": True}

    # Bewertung
    overall_rating: ConditionRating = Field(..., description="Gesamtbewertung")
    inspection_date: date = Field(..., description="Datum der Inspektion")
    inspector: Optional[str] = Field(None, description="Inspektor/Segelmacher")
    estimated_remaining_seasons: Optional[int] = Field(
        None, description="Geschätzte Restlebensdauer in Saisons"
    )

    # Einzelbewertungen (0-100)
    score_luff: int = Field(..., ge=0, le=100, description="Vorliek-Zustand")
    score_leech: int = Field(..., ge=0, le=100, description="Achterliek-Zustand")
    score_foot: int = Field(..., ge=0, le=100, description="Unterliek-Zustand")
    score_head: int = Field(..., ge=0, le=100, description="Kopf/Kopfbrett-Zustand")
    score_tack: int = Field(..., ge=0, le=100, description="Hals-Zustand")
    score_clew: int = Field(..., ge=0, le=100, description="Schothorn-Zustand")
    score_reef_points: int = Field(..., ge=0, le=100, description="Reffpunkte-Zustand")
    score_battens: int = Field(..., ge=0, le=100, description="Latten/Lattentaschen-Zustand")
    score_cloth: int = Field(..., ge=0, le=100, description="Segeltuch-Zustand")
    score_stitching: int = Field(..., ge=0, le=100, description="Nähte-Zustand")
    score_uv_damage: int = Field(..., ge=0, le=100, description="UV-Schaden (100=kein Schaden)")
    score_profile: int = Field(..., ge=0, le=100, description="Profilhaltung")

    # Profilmessungen
    draft_percent: Optional[float] = Field(None, description="Gemessene Profiltiefe %")
    draft_position_percent: Optional[float] = Field(None, description="Profilposition vom Vorliek %")

    # Fehlerbilder
    defects: list[str] = Field(
        default_factory=list,
        description="Liste der identifizierten Fehlerbilder (F-16_02-XX)"
    )

    # Empfehlungen
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )

    # Konfidenz
    confidence: str = Field(
        ...,
        description="Konfidenz-Level: measured, visual_high, visual_medium, visual_low, estimated"
    )
```

### ANHANG L: ReefingSystem

```python
class ReefingDriveType(str, Enum):
    MANUAL_HALYARD = "manual_halyard"
    MANUAL_ENDLESS = "manual_endless"
    ELECTRIC = "electric"
    HYDRAULIC = "hydraulic"


class ReefingSystem(BaseModel):
    """Beschreibung des Reefing-Systems."""

    model_config = {"from_attributes": True}

    # System-Typ
    system_type: ReefingType = Field(..., description="Reefing-Systemtyp")
    hersteller: Optional[str] = Field(None, description="System-Hersteller")
    modell: Optional[str] = Field(None, description="Modellbezeichnung")
    baujahr: Optional[int] = Field(None, description="Installations-Jahr")

    # Konfiguration
    reef_points: int = Field(..., ge=0, le=4, description="Anzahl Reffpunkte")
    drive_type: ReefingDriveType = Field(..., description="Antriebstyp")
    cockpit_operable: bool = Field(True, description="Aus dem Cockpit bedienbar")
    single_line: bool = Field(False, description="Einleinen-System (nur Slab)")

    # In-Mast/In-Boom spezifisch
    mast_profile_mm: Optional[str] = Field(None, description="Mastprofil für In-Mast")
    boom_profile_mm: Optional[str] = Field(None, description="Baumprofil für In-Boom")
    motor_power_w: Optional[int] = Field(None, description="Motor-Leistung (Watt)")

    # Zustand
    condition: Optional[ConditionRating] = Field(None, description="System-Zustand")
    last_service_date: Optional[date] = Field(None, description="Letzter Service")
    service_interval_months: int = Field(12, description="Service-Intervall in Monaten")

    # Kosten
    replacement_cost_eur: Optional[float] = Field(None, description="Austauschkosten in EUR")
    annual_maintenance_cost_eur: Optional[float] = Field(None, description="Jährliche Wartungskosten EUR")
```

### ANHANG M: BattenConfig

```python
class BattenMaterial(str, Enum):
    GFK = "gfk"
    CFK = "cfk"
    HYBRID = "hybrid"
    PVC = "pvc"
    STAINLESS = "stainless"


class BattenConfig(BaseModel):
    """Konfiguration der Segellatten."""

    model_config = {"from_attributes": True}

    # Grundkonfiguration
    batten_type: BattenType = Field(..., description="Lattentyp")
    count: int = Field(..., ge=0, le=8, description="Anzahl Latten")

    # Einzelne Latten (von oben nach unten)
    battens: list["SingleBatten"] = Field(
        default_factory=list,
        description="Einzelne Latten-Spezifikationen"
    )

    # Battcars
    battcar_required: bool = Field(False, description="Battcars erforderlich")
    battcar_hersteller: Optional[str] = Field(None, description="Battcar-Hersteller")
    battcar_modell: Optional[str] = Field(None, description="Battcar-Modell")

    # Zustand
    overall_condition: Optional[ConditionRating] = Field(None, description="Gesamtzustand Latten")


class SingleBatten(BaseModel):
    """Spezifikation einer einzelnen Latte."""

    model_config = {"from_attributes": True}

    position: int = Field(..., ge=1, description="Position von oben (1=oberste)")
    material: BattenMaterial = Field(..., description="Material")
    length_mm: float = Field(..., description="Länge in mm")
    width_mm: Optional[float] = Field(None, description="Breite in mm")
    thickness_mm: Optional[float] = Field(None, description="Dicke in mm")
    full_length: bool = Field(True, description="Volle Segelbreite (Volllatte)")
    compression_system: Optional[str] = Field(None, description="Kompressionssystem")
    condition: Optional[ConditionRating] = Field(None, description="Zustand dieser Latte")
    weight_g: Optional[float] = Field(None, description="Gewicht in Gramm")
    replacement_cost_eur: Optional[float] = Field(None, description="Ersatzkosten EUR")
```

### ANHANG N: MainsailRepair

```python
from datetime import date


class RepairType(str, Enum):
    STITCH = "stitch"              # Naht reparieren
    PATCH = "patch"                # Flicken aufnähen
    BATTEN_POCKET = "batten_pocket"  # Lattentasche erneuern
    LEECH_LINE = "leech_line"      # Achterlikleine ersetzen
    UV_STRIP = "uv_strip"          # UV-Schutzstreifen erneuern
    REEF_POINT = "reef_point"      # Reffpunkt reparieren
    HEADBOARD = "headboard"        # Kopfbrett ersetzen
    CLEW_REINFORCEMENT = "clew_reinforcement"  # Schothorn-Verstärkung
    TACK_REINFORCEMENT = "tack_reinforcement"  # Hals-Verstärkung
    CUNNINGHAM = "cunningham"      # Cunningham-Öse erneuern
    BOLTROPE = "boltrope"          # Vorliektau erneuern
    SLIDE_REPLACEMENT = "slide_replacement"  # Slides ersetzen
    LEECH_RESEW = "leech_resew"    # Achterliek-Saum erneuern
    BATTEN_REPLACEMENT = "batten_replacement"  # Latte ersetzen


class MainsailRepair(BaseModel):
    """Dokumentation einer Großsegel-Reparatur."""

    model_config = {"from_attributes": True}

    # Identifikation
    repair_id: Optional[str] = Field(None, description="Eindeutige Reparatur-ID")
    repair_date: date = Field(..., description="Datum der Reparatur")
    sailmaker: str = Field(..., description="Ausführender Segelmacher")

    # Reparaturdetails
    repair_type: RepairType = Field(..., description="Art der Reparatur")
    location_description: str = Field(
        ..., description="Beschreibung der Reparaturstelle (deutsch)"
    )
    defect_code: Optional[str] = Field(
        None, description="AYDI Fehlerbild-Code (F-16_02-XX)"
    )

    # Umfang
    work_hours: float = Field(..., ge=0, description="Arbeitsstunden")
    material_cost_eur: float = Field(..., ge=0, description="Materialkosten EUR")
    labor_cost_eur: float = Field(..., ge=0, description="Arbeitskosten EUR")
    total_cost_eur: float = Field(..., ge=0, description="Gesamtkosten EUR")

    # Ergebnis
    warranty_months: int = Field(0, description="Garantie auf Reparatur in Monaten")
    notes: Optional[str] = Field(None, description="Anmerkungen (deutsch)")
    before_photo_url: Optional[str] = Field(None, description="Foto vor Reparatur")
    after_photo_url: Optional[str] = Field(None, description="Foto nach Reparatur")
```

### ANHANG O: MainsailOrder

```python
class OrderStatus(str, Enum):
    QUOTE_REQUESTED = "quote_requested"
    QUOTE_RECEIVED = "quote_received"
    ORDERED = "ordered"
    IN_PRODUCTION = "in_production"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    INSTALLED = "installed"


class MainsailOrder(BaseModel):
    """Bestellung eines neuen Großsegels."""

    model_config = {"from_attributes": True}

    # Identifikation
    order_id: Optional[str] = Field(None, description="Bestell-ID")
    order_date: Optional[date] = Field(None, description="Bestelldatum")
    status: OrderStatus = Field(
        OrderStatus.QUOTE_REQUESTED, description="Bestellstatus"
    )

    # Yacht
    yacht_name: str = Field(..., description="Yacht-Name")
    yacht_type: str = Field(..., description="Yacht-Typ (z.B. Bavaria 40)")
    yacht_year: Optional[int] = Field(None, description="Baujahr der Yacht")

    # Segel-Spezifikation
    spec: MainsailSpec = Field(..., description="Segel-Spezifikation")

    # Optionen
    options: list[str] = Field(
        default_factory=list,
        description="Zusätzliche Optionen (deutsch)"
    )

    # Hersteller und Kosten
    sailmaker: str = Field(..., description="Segelhersteller/Loft")
    quote_eur: Optional[float] = Field(None, description="Angebotspreis EUR")
    final_price_eur: Optional[float] = Field(None, description="Endpreis EUR")
    delivery_weeks: Optional[int] = Field(None, description="Lieferzeit in Wochen")

    # Lieferung
    expected_delivery: Optional[date] = Field(None, description="Voraussichtliches Lieferdatum")
    actual_delivery: Optional[date] = Field(None, description="Tatsächliches Lieferdatum")

    # Anmerkungen
    notes: Optional[str] = Field(None, description="Anmerkungen (deutsch)")
```

### ANHANG P: MainsailMeasurements

```python
class MainsailMeasurements(BaseModel):
    """Vermessungsdaten für eine Großsegel-Bestellung oder -Prüfung."""

    model_config = {"from_attributes": True}

    # Datum und Kontext
    measurement_date: date = Field(..., description="Vermessungsdatum")
    measured_by: str = Field(..., description="Vermesser")

    # Mast-Maße (mm)
    mast_height_mm: float = Field(..., description="Masthöhe über Deck")
    p_luff_mm: float = Field(..., description="P-Maß (Vorlieklänge)")
    mast_profile_width_mm: float = Field(..., description="Mastprofil Breite")
    mast_profile_depth_mm: float = Field(..., description="Mastprofil Tiefe")
    mast_groove_width_mm: float = Field(..., description="Mastnut-Breite innen")
    mast_groove_type: str = Field(
        ..., description="Mastnut-Typ (intern/extern/Schiene)"
    )
    mast_bend_mm: Optional[float] = Field(
        None, description="Mastbiegung unter Belastung in mm"
    )
    spreader_height_mm: Optional[float] = Field(
        None, description="Salinghöhe über Deck"
    )
    spreader_sweep_degrees: Optional[float] = Field(
        None, description="Salingwinkel in Grad nach achtern"
    )

    # Baum-Maße (mm)
    e_foot_mm: float = Field(..., description="E-Maß (Unterlieklänge)")
    boom_profile_width_mm: float = Field(..., description="Baumprofil Breite")
    boom_profile_depth_mm: float = Field(..., description="Baumprofil Tiefe")
    boom_groove_width_mm: Optional[float] = Field(
        None, description="Baumnut-Breite (falls vorhanden)"
    )
    boom_above_deck_mm: float = Field(..., description="Baumhöhe über Deck")
    gooseneck_height_mm: float = Field(
        ..., description="Lümmelbeschlag-Höhe über Deck"
    )

    # Bestehende Beschläge
    existing_slide_type: Optional[str] = Field(
        None, description="Bestehender Slide/Slug-Typ"
    )
    existing_slide_count: Optional[int] = Field(
        None, description="Anzahl bestehender Slides"
    )
    existing_battcar_type: Optional[str] = Field(
        None, description="Bestehender Battcar-Typ"
    )
    halyard_diameter_mm: Optional[float] = Field(
        None, description="Fall-Durchmesser"
    )
    halyard_type: Optional[str] = Field(
        None, description="Fall-Typ (Draht/Dyneema/Polyester)"
    )

    # Backstag
    backstay_type: Optional[str] = Field(
        None, description="Backstag-Typ (fest/verstellbar/Split)"
    )
    backstay_clearance_mm: Optional[float] = Field(
        None, description="Backstag-Abstand zum Achterliek"
    )

    # Fotos
    photo_mast_full: Optional[str] = Field(None, description="Foto: Mast komplett")
    photo_mast_groove: Optional[str] = Field(None, description="Foto: Mastnut Detail")
    photo_boom: Optional[str] = Field(None, description="Foto: Baum")
    photo_gooseneck: Optional[str] = Field(None, description="Foto: Lümmelbeschlag")
    photo_existing_sail: Optional[str] = Field(None, description="Foto: Bestehendes Segel")

    # Anmerkungen
    notes: Optional[str] = Field(None, description="Anmerkungen (deutsch)")

    # Konfidenz
    confidence: str = Field(
        "measured",
        description="Konfidenz-Level der Vermessung"
    )
```

### ANHANG Q: VisualMainsailAnalysis

```python
class VisualMainsailAnalysis(BaseModel):
    """Ergebnis einer visuellen Großsegel-Analyse aus Fotos."""

    model_config = {"from_attributes": True}

    # Identifikation
    analysis_id: Optional[str] = Field(None, description="Analyse-ID")
    analysis_date: date = Field(..., description="Analysedatum")
    photo_count: int = Field(..., description="Anzahl analysierter Fotos")

    # Erkanntes Material und Typ
    detected_material: Optional[SailMaterial] = Field(
        None, description="Erkanntes Material (oder None wenn unklar)"
    )
    material_confidence: str = Field(
        ..., description="Konfidenz Material-Erkennung"
    )
    detected_batten_type: Optional[BattenType] = Field(
        None, description="Erkannter Lattentyp"
    )
    detected_reefing_type: Optional[ReefingType] = Field(
        None, description="Erkanntes Reefing-System"
    )

    # Zustandsbewertung
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0-100")
    condition: ConditionRating = Field(..., description="Zustandsbewertung")

    # Erkannte Fehlerbilder
    detected_defects: list[dict] = Field(
        default_factory=list,
        description="Erkannte Fehlerbilder mit Code und Konfidenz"
    )

    # Profil-Schätzung
    estimated_draft_percent: Optional[float] = Field(
        None, description="Geschätzte Profiltiefe %"
    )
    estimated_draft_position: Optional[float] = Field(
        None, description="Geschätzte Profilposition %"
    )
    profile_assessment: Optional[str] = Field(
        None, description="Profil-Beurteilung (deutsch)"
    )

    # Alter-Schätzung
    estimated_age_seasons: Optional[int] = Field(
        None, description="Geschätztes Alter in Saisons"
    )

    # Empfehlungen
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )

    # Konfidenz
    overall_confidence: str = Field(
        ..., description="Gesamt-Konfidenz der Analyse"
    )
    analysis_limitations: list[str] = Field(
        default_factory=list,
        description="Einschränkungen der Analyse (deutsch)"
    )
```

### ANHANG R: MainsailCostEstimate

```python
class CostCategory(str, Enum):
    BUDGET = "budget"
    MIDRANGE = "midrange"
    PERFORMANCE = "performance"
    HIGH_PERFORMANCE = "high_performance"
    RACING = "racing"


class MainsailCostEstimate(BaseModel):
    """Kostenschätzung für ein neues Großsegel."""

    model_config = {"from_attributes": True}

    # Yacht-Daten
    boat_length_ft: float = Field(..., description="Bootslänge in Fuß")
    sail_area_sqm: float = Field(..., description="Geschätzte Segelfläche m²")
    category: CostCategory = Field(..., description="Preiskategorie")

    # Basis-Segel
    base_material: SailMaterial = Field(..., description="Empfohlenes Material")
    base_price_eur_min: float = Field(..., description="Basispreis Minimum EUR")
    base_price_eur_max: float = Field(..., description="Basispreis Maximum EUR")

    # Optionen
    full_battens_eur: Optional[float] = Field(None, description="Aufpreis Volllatten EUR")
    square_top_eur: Optional[float] = Field(None, description="Aufpreis Square-Top EUR")
    carbon_battens_eur: Optional[float] = Field(None, description="Aufpreis CFK-Latten EUR")
    uv_protection_eur: Optional[float] = Field(None, description="Aufpreis UV-Schutz EUR")
    third_reef_eur: Optional[float] = Field(None, description="Aufpreis 3. Reff EUR")
    battcars_eur: Optional[float] = Field(None, description="Kosten Battcars EUR")
    stackpack_eur: Optional[float] = Field(None, description="Kosten StackPack EUR")
    installation_eur: Optional[float] = Field(None, description="Installationskosten EUR")

    # Gesamt
    total_min_eur: float = Field(..., description="Gesamtkosten Minimum EUR")
    total_max_eur: float = Field(..., description="Gesamtkosten Maximum EUR")

    # Empfohlene Hersteller
    recommended_sailmakers: list[str] = Field(
        default_factory=list,
        description="Empfohlene Segelmacher für diese Kategorie"
    )

    # Laufende Kosten
    annual_maintenance_eur: float = Field(
        ..., description="Geschätzte jährliche Wartungskosten EUR"
    )
    expected_lifespan_seasons: int = Field(
        ..., description="Erwartete Lebensdauer in Saisons"
    )
    cost_per_season_eur: Optional[float] = Field(
        None, description="Kosten pro Saison EUR (Kauf + Wartung / Lebensdauer)"
    )

    # Konfidenz
    confidence: str = Field(
        "estimated",
        description="Konfidenz-Level der Kostenschätzung"
    )
    price_date: str = Field(
        ..., description="Stand der Preisangaben (YYYY-MM)"
    )
```

---

*Ende des Dokuments — AYDI Maritime Knowledge Base v2.0*
*Letzte Aktualisierung: April 2026*
*Alle Preisangaben in EUR, Stand April 2026, unverbindlich.*
*Alle technischen Angaben ohne Gewähr — im Zweifelsfall Segelmacher konsultieren.*
