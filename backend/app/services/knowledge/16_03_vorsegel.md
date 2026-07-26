---
titel: "Vorsegel — Genua, Fock und Sturmfock"
kategorie: "Segel"
unterkategorie: "Vorsegel"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 16_03 — Vorsegel — Genua, Fock und Sturmfock

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Vorsegel-Typen](#2-vorsegel-typen)
3. [Materialien](#3-materialien)
4. [Konstruktion und Schnitt](#4-konstruktion-und-schnitt)
5. [Trimm](#5-trimm)
6. [Furler-Systeme](#6-furler-systeme)
7. [Hersteller-Spezifikationen](#7-hersteller-spezifikationen)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [Vorsegel-Garderobe](#10-vorsegel-garderobe)
11. [Kosten](#11-kosten)
12. [FAQ](#12-faq)
13. [Glossar](#13-glossar)
14. [Schnell-Referenz](#14-schnell-referenz)
15. [ANHANG A–H: Fallstudien](#15-anhang-a-h-fallstudien)
16. [ANHANG I–R: Pydantic v2 Modelle](#16-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einführung

### 1.1 Die Rolle des Vorsegels im Segelplan

Das Vorsegel ist neben dem Großsegel die zweite tragende Komponente des modernen Segelplans.
Bei Slup-getakelten Yachten (dem mit Abstand häufigsten Rigg-Typ bei Fahrtenyachten von 8–16 m)
erzeugt das Vorsegel typischerweise 40–55 % der gesamten Antriebskraft am Wind.
Bei achterlichen Kursen kann dieser Anteil auf 60–70 % steigen, wenn das Großsegel im Windschatten
des Vorsegels steht oder das Vorsegel als Schmetterlings-Konfiguration gefahren wird.

Die Bedeutung des Vorsegels geht jedoch weit über den bloßen Antriebsanteil hinaus:

- **Balancierung des Ruderdrucks:** Ein korrekt getrimmtes Vorsegel reduziert den Wetterdruck
  (Tendenz zum Anluven) und ermöglicht leichtgängiges Steuern.
- **Krängungsminimierung:** Durch präzises Trimmen des Vorsegel-Profils lässt sich die
  Krängung kontrollieren, was Komfort und Sicherheit auf Langfahrt erhöht.
- **Manövrierbarkeit:** Die Fähigkeit, das Vorsegel schnell zu bergen oder zu reffen,
  ist entscheidend für die Handhabung bei zunehmendem Wind.
- **Redundanz:** Bei Ausfall des Großsegels (Riss, Mastbruch oberhalb der Salingkopplung)
  kann allein unter Vorsegel noch kontrolliert gesegelt werden.

### 1.2 Slot-Effekt (Düseneffekt)

Der aerodynamische Slot-Effekt zwischen Vorsegel und Großsegel ist einer der am häufigsten
missverstandenen Aspekte der Segeltheorie. Entgegen der populären Erklärung beschleunigt
der Slot die Strömung auf der Leeseite des Großsegels nicht nach dem Venturi-Prinzip.
Vielmehr bewirkt das Vorsegel eine Umlenkung der Anströmung des Großsegels, wodurch
dieses bei gleichem Anstellwinkel einen höheren Auftrieb erzeugt.

**Messwerte aus Windkanal-Untersuchungen (North Sails, 2019):**

| Konfiguration | Auftriebsbeiwert (Cl) | Widerstandsbeiwert (Cd) | Cl/Cd-Verhältnis |
|---|---|---|---|
| Großsegel allein | 1,28 | 0,14 | 9,1 |
| Fock (100 % LP) + Großsegel | 1,85 | 0,18 | 10,3 |
| Genua 1 (150 % LP) + Großsegel | 2,35 | 0,24 | 9,8 |
| Genua 2 (130 % LP) + Großsegel | 2,15 | 0,21 | 10,2 |

**Optimaler Slot-Abstand:**
Der Abstand zwischen Achterliek des Vorsegels und Leeseite des Großsegels sollte im
oberen Drittel des Segels etwa 10–15 % der Großsegel-Unterliekslänge betragen.
Ein zu enger Slot erzeugt Rückstau und frühe Ablösung am Großsegel.
Ein zu weiter Slot reduziert den Synergieeffekt.

### 1.3 Historische Entwicklung

Die Entwicklung des Vorsegels lässt sich in vier wesentliche Phasen unterteilen:

1. **Vor 1920:** Überlappende Vorsegel waren weitgehend unbekannt. Yachten fuhren
   kleine Klüver und Focks ohne Überlappung. Das Rigg war stark unterteilt (Schoner,
   Kutter mit mehreren Vorsegeln).

2. **1920–1960:** Der schwedische Segler Sven Salén experimentierte 1926 mit überlappenden
   Vorsegeln. Die erste dokumentierte Genua wurde bei der Regatta vor Genua 1927 eingesetzt,
   daher der Name. Die Genua revolutionierte das Regattasegeln und wurde schnell zum Standard.

3. **1960–1990:** Die Einführung von Rollreffsystemen (erste praktische Systeme ab ca. 1970)
   veränderte die Vorsegel-Philosophie grundlegend. Statt einer „Segelgarderobe" mit 4–6
   verschiedenen Vorsegeln konnte eine einzelne, rollbare Genua einen großen Windbereich abdecken.

4. **1990–heute:** Membransegel (3Di, D4, Stratis), selbstwendende Focks mit Schienensystemen,
   Code 0 als Bindeglied zwischen Vorsegel und Spinnaker, sowie computergestützte Schnittdesigns
   (CFD-optimierte Profile) bestimmen die aktuelle Entwicklung.

### 1.4 Terminologie: Vorsegel vs. Fock vs. Genua

In der deutschsprachigen Segelterminologie werden die Begriffe häufig unscharf verwendet:

- **Vorsegel (headsail):** Oberbegriff für jedes Segel, das vor dem Mast gefahren wird.
- **Fock (jib):** Ein Vorsegel ohne Überlappung des Großsegel-Dreiecks (LP/J ≤ 100 %).
- **Genua (genoa):** Ein Vorsegel mit Überlappung (LP/J > 100 %).
- **Klüver (inner jib):** Bei Kutterrigg das innere Vorsegel am Kutterstag.
- **Sturmfock (storm jib):** Schwerwetter-Vorsegel gemäß World Sailing OSR (Offshore Special Regulations), stark reduzierte Fläche.

Dabei ist LP die kürzeste Distanz vom Schothorn (clew) zum Vorliek (luff), und
J die Distanz vom Vorstag-Ansatzpunkt am Deck bis zur Mastmitte auf Deckshöhe.

### 1.5 Bedeutung für die AYDI-Analyse

Im Rahmen der AYDI-Bewertung wird das Vorsegel in mehreren Modulen analysiert:

- **Structural:** Lasten auf Vorstag, Deck-Beschläge, Rollreffanlage
- **Materials:** Segeltuch-Zustand, UV-Schutz, Nähte
- **Production:** Qualität der Verarbeitung (Patches, Verstärkungen, Ösen)
- **Compliance:** Sturmfock-Anforderungen gemäß CE-Kategorie
- **Cost:** Wiederbeschaffungswert, Reparaturkosten
- **Service_patterns:** Typische Verschleißmuster nach Betriebsstunden/Saisons

Jede Bewertung wird mit einem Konfidenzlevel versehen. Visuelle Analyse von Segelfotos
kann „visual_high" erreichen bei klaren Detailaufnahmen, fällt jedoch häufig auf
„visual_medium" oder „visual_low" bei Gesamtaufnahmen unter Segelbedingungen.

---

## 2. Vorsegel-Typen

### 2.1 Genua 1 (Leichtwind-Genua)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 150–155 % |
| Windbereich (TWS) | 4–12 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 48–55 m² |
| Tuchgewicht | 140–180 g/m² (Dacron), 100–140 g/m² (Laminat) |
| Profiltiefe | 14–17 % der Sehnenlänge |
| Position maximale Wölbung | 38–42 % vom Vorliek |

**Beschreibung:**
Die Genua 1 ist das größte Vorsegel in der Garderobe und wird bei leichten Winden eingesetzt.
Ihre große Überlappung erzeugt maximale Segelfläche, erfordert jedoch mehr Aufmerksamkeit
beim Trimm und bei Wenden, da das Segel um die Wanten herumgeführt werden muss.

**Einsatzbedingungen:**
- Idealer Einsatzbereich: flaches Wasser, leichter Wind, Amwind bis Halbwind
- Grenzbereich: Ab 14 kn TWS wird die Genua 1 zur Belastung (Krängung, Ruderdruck)
- Auf Rollreffanlagen: Kann bis auf ca. 120 % LP eingerollt werden, dann Profilqualität nachlassend

**Material-Empfehlungen nach Einsatzprofil:**
- Fahrtensegler (< 500 sm/Jahr): Dacron 170 g/m², Cross-Cut
- Aktiver Fahrtensegler (500–2.000 sm/Jahr): Dacron 160 g/m² oder Pentex-Laminat
- Regatta-/Fahrtensegler: Pentex/Dyneema-Laminat oder 3Di
- Reine Regatta: Carbon-/Aramid-Laminat

**Lebensdauer-Erwartung:**
- Dacron: 5–8 Jahre bei durchschnittlicher Nutzung
- Laminat: 3–5 Jahre
- 3Di/Membran: 6–10 Jahre (abhängig von UV-Exposition)

### 2.2 Genua 2 (Arbeits-Genua)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 130–140 % |
| Windbereich (TWS) | 10–18 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 38–45 m² |
| Tuchgewicht | 180–220 g/m² (Dacron), 140–180 g/m² (Laminat) |
| Profiltiefe | 12–15 % der Sehnenlänge |
| Position maximale Wölbung | 40–45 % vom Vorliek |

**Beschreibung:**
Die Genua 2 ist das Arbeitspferd der Segelgarderobe. Sie deckt den häufigsten Windbereich ab
und bietet den besten Kompromiss zwischen Segelfläche und Handhabbarkeit. Viele Fahrtensegler
mit Rollreffanlage nutzen eine Genua 2 als Standardsegel, das bei Bedarf eingerollt wird.

**Einsatzbedingungen:**
- Idealer Einsatzbereich: mittlerer Wind, alle Kurse am Wind
- Bei 16–18 kn TWS: erstes Reffen sinnvoll (Rollung auf ca. 110 % LP)
- Auf Rollreffanlagen: Gute Rollbarkeit, Profil bleibt bis ca. 100 % LP akzeptabel

**Besonderheiten:**
- Bei Yachten mit nur einem Vorsegel auf Rollreffanlage ist die Genua 2 die häufigste Wahl
- UV-Schutzstreifen am Achterliek und Unterliek sind bei Rollgenuas obligatorisch
- Verstärkungspatches an Schothorn, Kopf und Hals müssen höheren Lasten standhalten als bei Genua 1

### 2.3 Genua 3 (Starkwind-Genua)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 110–125 % |
| Windbereich (TWS) | 15–22 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 32–38 m² |
| Tuchgewicht | 220–280 g/m² (Dacron), 180–220 g/m² (Laminat) |
| Profiltiefe | 10–13 % der Sehnenlänge |
| Position maximale Wölbung | 42–48 % vom Vorliek |

**Beschreibung:**
Die Genua 3 ist ein Starkwind-Segel mit reduzierter Überlappung. Sie wird eingesetzt,
wenn die Genua 2 selbst nach dem Reffen zu viel Fläche bietet. Bei Yachten mit
Rollreffanlagen wird diese Segelgröße häufig durch teilweises Einrollen der Genua 2
ersetzt, allerdings mit Kompromissen im Profil.

**Konstruktive Merkmale:**
- Stärkere Nahtausführung (dreifach genäht, Zickzack + Gerade)
- Verstärkte Liektau-Anbindung
- Breitere Verstärkungspatches (doppelte Fläche gegenüber Genua 1)
- Oft mit Reffpunkten (Cunningham-Ösen) am Vorliek

### 2.4 Genua 4 (Schwerwetter-Genua)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 100–110 % |
| Windbereich (TWS) | 20–28 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 26–32 m² |
| Tuchgewicht | 280–340 g/m² (Dacron) |
| Profiltiefe | 8–11 % der Sehnenlänge |
| Position maximale Wölbung | 45–50 % vom Vorliek |

**Beschreibung:**
Die Genua 4 markiert den Übergangsbereich zwischen Genua und Fock. Mit ihrer geringen
oder marginalen Überlappung ist sie ein ausgesprochenes Starkwind-Segel für erfahrene
Crews, die bei 20+ Knoten noch effizient Höhe laufen wollen.

**Einsatz:**
- Primär bei Langfahrt- und Blauwasser-Seglern
- Bei Kurzstrecken-Fahrten wird dieses Segel selten benötigt (Rollgenua reicht)
- Auf Regatten als „Nummer 4" bezeichnet
- Wird häufig am Vorstag mit Stagreitern gefahren (nicht auf Furler)

### 2.5 Arbeitsfock (Working Jib)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 95–100 % |
| Windbereich (TWS) | 12–25 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 24–30 m² |
| Tuchgewicht | 220–300 g/m² (Dacron) |
| Profiltiefe | 10–14 % der Sehnenlänge |
| Position maximale Wölbung | 40–45 % vom Vorliek |

**Beschreibung:**
Die Arbeitsfock hat keine Überlappung (LP/J ≤ 100 %). Sie ist das klassische Allround-Segel
für Yachten, die ohne Rollreffanlage segeln, oder als Zweitsegel auf einem inneren Vorstag
(Kutterstag) bei Yachten mit Kutterrigg.

**Vorteile gegenüber Genuas:**
- Einfache Wenden: kein Umführen um die Wanten nötig
- Geringere Belastung der Winschen
- Bessere Sicht nach Luv
- Weniger Verschleiß durch Schamfilen an Wanten und Salingen

**Nachteile:**
- Weniger Segelfläche bei Leichtwind
- Weniger effektiver Slot-Effekt
- Geringerer Vortrieb auf Amwind-Kursen bei leichtem Wind

### 2.6 Selbstwendefock (Self-Tacking Jib)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 85–105 % |
| Windbereich (TWS) | 8–22 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 22–30 m² |
| Tuchgewicht | 200–260 g/m² (Dacron), 160–200 g/m² (Laminat) |
| Schienenlänge (Fock-Schiene) | 1.200–2.000 mm (abhängig von Bootsgröße) |
| Schienenbogenradius | Abhängig von Segelschnitt, typisch 800–1.500 mm |

**Beschreibung:**
Die Selbstwendefock läuft auf einer Schiene (Fockschiene, jib track), die quer über das
Vordeck verläuft. Beim Wenden wechselt das Schothorn automatisch die Seite, ohne dass
die Crew eine Schot bedienen muss. Dies ist besonders vorteilhaft für:

- Einhandsegler und Kurzhandcrews
- Segler, die Komfort und einfache Handhabung priorisieren
- Reviere mit häufigen Wenden (Flüsse, enge Buchten)

**Schienensysteme:**

| Hersteller | Modell | Bootsgröße | Preis (EUR) |
|---|---|---|---|
| Harken | Self-Tacking System | 8–12 m | 1.800–3.200 |
| Antal | ST Track System | 10–15 m | 2.200–4.000 |
| Selden | Genua Car + Track | 9–14 m | 1.600–3.500 |
| Frederiksen | Self-Tacking System | 8–13 m | 1.500–2.800 |
| Karver | KST System | 10–18 m | 2.800–5.500 |

**Nachteile:**
- Reduzierte Segelfläche gegenüber Genua (typisch 20–30 % weniger)
- Schiene muss exakt zum Segelschnitt passen
- Eingeschränkte Trimmbarkeit (Holepunkt nur auf der Schiene variabel)
- Kosten für Schienensystem und Einbau

**Integration mit Rollreffanlage:**
Selbstwendefocks können mit Rollreffanlagen kombiniert werden. Dabei ist jedoch darauf
zu achten, dass das Segel beim Rollen das korrekte Profil behält und die Schot nicht
am Leitblock klemmt. Einige Hersteller (insbesondere Beneteau und Jeanneau) bieten
ab Werk aufeinander abgestimmte Systeme an.

### 2.7 Sturmfock (Storm Jib)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 50–65 % |
| Windbereich (TWS) | 28–60+ kn |
| Segelfläche (OSR-Anforderung) | max. 0,05 × H² (H = Vorsegeldreieck-Höhe) |
| Alternativ-Berechnung | ca. 5 % der Vorsegel-Nennfläche |
| Tuchgewicht | 340–450 g/m² (schweres Dacron oder Nylon-Laminat) |
| Farbe (OSR-Empfehlung) | Orange oder Signalfarbe (empfohlen, nicht vorgeschrieben) |

**Anforderungen an Sturmsegel (World Sailing Offshore Special Regulations / OSR):**

Für CE-Kategorie A (Hochsee) und B (Küstengewässer) ist eine Sturmfock vorgeschrieben.
Die Anforderungen umfassen:

1. **Maximale Segelfläche:** Die Sturmfock darf eine Fläche von 0,05 × H² nicht
   überschreiten, wobei H die Höhe des Vorsegeldreiecks in Metern ist.
   Beispiel: H = 14 m → max. Sturmfock-Fläche = 0,05 × 196 = 9,8 m²

2. **Unabhängige Befestigung:** Die Sturmfock muss unabhängig von der Rollreffanlage
   gesetzt werden können. Ein separates Innenstag (Sturmstag, baby stay) oder ein
   Textil-Vorstag mit Stag-Wirbeln ist erforderlich.

3. **Sichtbarkeit:** Die Sturmfock sollte in einer gut sichtbaren Farbe (orange, rot,
   gelb) ausgeführt sein, um die Erkennbarkeit bei schweren Wetterbedingungen zu erhöhen.
   Dies ist eine Empfehlung, keine zwingende Vorschrift.

4. **Verstärkung:** Dreifach genähte Nähte, verstärkte Ecken, Edelstahl-Kauschen
   (nicht Kunststoff), Vorliek mit Draht oder Dyneema-Kern.

5. **Befestigungsmittel an Bord:** Passende Schäkel, Stagreiter oder Karabiner müssen
   an Bord sein und zur Sturmfock passen.

**Einsatz-Empfehlungen:**
- Vor jeder Blauwasser-Reise: Sturmfock probeweise setzen und trimmen
- Stagreiter oder Karabiner regelmäßig auf Gängigkeit prüfen
- Stauraum: trocken, zugänglich, nicht unter schwerer Ausrüstung vergraben
- Sturmfock und Sturmstag als Einheit betrachten und gemeinsam lagern

**Typische Sturmfock-Flächen nach Bootsgröße:**

| Bootsgröße (LOA) | H (typisch) | Max. Sturmfock (m²) |
|---|---|---|
| 8 m (26 ft) | 9,5 m | 4,5 m² |
| 10 m (33 ft) | 12,0 m | 7,2 m² |
| 12 m (40 ft) | 14,0 m | 9,8 m² |
| 14 m (46 ft) | 16,0 m | 12,8 m² |
| 16 m (52 ft) | 17,5 m | 15,3 m² |
| 18 m (59 ft) | 19,0 m | 18,1 m² |

### 2.8 Code 0 / Screecher

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 160–200 % |
| Windbereich (TWS) | 4–16 kn |
| Einsatz-Kurse (TWA) | 60–120° (Amwind-Reaching bis Halbwind) |
| Segelfläche (typisch, 38-Fuß-Yacht) | 60–85 m² |
| Tuchgewicht | 80–140 g/m² (Laminat) |
| Furler-Typ | Top-Down-Furler (Pflicht) |

**Beschreibung:**
Der Code 0 (auch Screecher oder Gennaker auf Furler genannt) ist ein asymmetrisches
Leichtwind-Vorsegel, das den Bereich zwischen traditioneller Genua und Gennaker abdeckt.
Er wird auf einem eigenen Top-Down-Furler gefahren und kann nicht am Standard-Vorstag
befestigt werden.

**Unterschied zum Gennaker:**
- Code 0: flacheres Profil, kann höher am Wind gefahren werden (ab TWA 55–60°)
- Gennaker: tieferes Profil, typisch ab TWA 70–80°, mehr Fläche

**Top-Down-Furler-Systeme für Code 0:**

| Hersteller | Modell | Bootsgröße | Preis (EUR) |
|---|---|---|---|
| Facnor | FX+ 2500/3500 | 10–14 m | 2.800–4.500 |
| Karver | KF4–KF8 | 10–18 m | 3.200–6.800 |
| Ronstan | RF-45/RF-55 | 9–14 m | 2.400–4.200 |
| Selden | CX Furler | 10–15 m | 2.600–4.800 |
| Profurl | Spin 2/3 | 10–16 m | 2.800–5.200 |

**Torque-Seil (Anti-Torsion Rope):**
Das Torque-Seil (Torsionsseil) verbindet Furler-Trommel und Segel-Kopf und erzeugt
die für das Aufrollen notwendige Drehung. Typische Länge: Vorstaglänge + 10 %.
Materialien: Dyneema/Spectra-Kern mit Anti-Torsions-Außengeflecht.
Lebensdauer: 3–5 Jahre bei regelmäßiger Nutzung.

### 2.9 Gennaker

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Windbereich (TWS) | 6–20 kn |
| Einsatz-Kurse (TWA) | 70–160° |
| Segelfläche (typisch, 38-Fuß-Yacht) | 80–120 m² |
| Tuchgewicht | 50–100 g/m² (Nylon, Polyester) |
| Befestigung | Bugspriet oder Bugbeschlag, Tacker oder Furler |

**Beschreibung:**
Der Gennaker ist ein asymmetrischer Spinnaker, der am Bugspriet oder einem festen
Bugbeschlag gefahren wird. Er ersetzt zunehmend den symmetrischen Spinnaker auf
Fahrtenyachten, da er einfacher zu handhaben ist.

**Typen:**
- **A-Gennaker (Full):** Sehr tiefes Profil, maximale Fläche, für Vorwind-Kurse (TWA 120–160°)
- **S-Gennaker (Standard):** Mittleres Profil, Allround (TWA 90–140°)
- **C-Gennaker (Close):** Flaches Profil, für höhere Kurse (TWA 70–110°), ähnlich Code 0

**Handling-Systeme:**
- **Berge-Sock (Snuffer):** Textilschlauch zum kontrollierten Bergen, ab 1.200 EUR
- **Top-Down-Furler:** Komfortabelste Lösung, ab 2.800 EUR
- **Tacker-System (Asymm. Spinnaker-Tacker):** Für Wenden ohne Bergen, ab 800 EUR

### 2.10 Staysail (Kutter-Fock)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis (bezogen auf Kutterstag) | 90–100 % |
| Windbereich (TWS) | 18–35 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 12–18 m² |
| Tuchgewicht | 260–340 g/m² (Dacron) |
| Befestigung | Kutterstag (inner forestay) |

**Beschreibung:**
Das Staysail ist das innere Vorsegel bei einer Kutter-Takelung. Es wird am Kutterstag
(auch Inner Forestay oder Baby Stay) gefahren, das typischerweise 30–40 % der Vorstaglänge
hinter dem Vorstag am Mast ansetzt.

**Einsatz-Szenarien:**
1. **Starkwind-Konfiguration:** Staysail + gerefftes Großsegel bei 25+ kn TWS
2. **Kombi-Konfiguration:** Genua auf Furler + Staysail + Großsegel bei 12–18 kn TWS
3. **Sturm-Konfiguration:** Staysail allein oder Sturmfock am Vorstag + Staysail

**Vorteile des Kutter-Riggs:**
- Hochgradig anpassbare Segelfläche
- Niedrigerer Schwerpunkt der Segelfläche bei Starkwind
- Redundanz bei Vorstag-Versagen
- Bessere Balance bei schweren Wetterbedingungen
- Staysail als selbstwendende Fock auf Kutterstag-Schiene

**Kutterstag-Montage:**
- Festes Kutterstag (Running Backstays erforderlich): 1.500–3.500 EUR
- Abnehmbares Kutterstag (mit Spannschloss): 800–2.000 EUR
- Textile Variante (Dyneema-Kutterstag): 400–1.200 EUR

### 2.11 Yankee

**Technische Daten:**

| Parameter | Wert |
|---|---|
| LP/J-Verhältnis | 90–110 % |
| Windbereich (TWS) | 10–25 kn |
| Segelfläche (typisch, 38-Fuß-Yacht) | 28–35 m² |
| Tuchgewicht | 220–300 g/m² (Dacron) |
| Achterliek-Höhe | ca. 85–90 % der Vorstag-Höhe |

**Beschreibung:**
Der Yankee ist ein hochgeschnittenes Vorsegel mit hohem Schothorn (clew). Das Unterliek
verläuft deutlich über Deckshöhe, was Sicht nach Luv verbessert und Spritzwasser unter
dem Segel durchlässt. Typisch für Langfahrt-Yachten und Kutter-Riggs.

**Vorteile:**
- Hervorragende Sicht nach Lee und Luv
- Weniger Spritzwasser auf Deck
- Gute Kombination mit Staysail (Kutter-Konfiguration)
- Einfachere Wenden (Schot läuft frei über die Wanten)

**Nachteile:**
- Weniger Segelfläche als eine vergleichbare Genua
- Höherer Segelschwerpunkt
- Nicht optimal für Leichtwind (fehlendes Unterliek-Dreieck)

---

## 3. Materialien

### 3.1 Dacron (Polyester-Gewebe)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Dichte | 1,38 g/cm³ |
| Bruchfestigkeit | 400–800 MPa |
| Dehnung bei Bruch | 12–20 % |
| UV-Beständigkeit | Gut (5–10 Jahre ohne nennenswerten Abbau) |
| Feuchtigkeitsaufnahme | < 0,4 % |
| Temperaturbeständigkeit | -40 °C bis +150 °C |
| Preis (Segeltuch) | 15–35 EUR/m² |

**Beschreibung:**
Dacron ist der Handelsname für Polyester-Gewebe (PET) und seit den 1960er-Jahren das
Standard-Material für Fahrtensegel. Es bietet die beste Balance aus Haltbarkeit, UV-
Beständigkeit, Handhabung und Preis.

**Qualitätsstufen:**
- **Standard-Dacron (150–200 g/m²):** Für Charteryachten und Gelegenheitssegler. Webdichte
  gering, schnellere Formverschlechterung. Lebensdauer: 3–5 Jahre.
- **Premium-Dacron (180–280 g/m²):** Dichter gewebt, wärmebehandelt (heat-set), längere
  Formstabilität. Hersteller: Contender (Contender CZ), Dimension Polyant (DP-WB).
  Lebensdauer: 6–10 Jahre.
- **High-Modulus-Dacron (200–340 g/m²):** Maximal verdichtetes Gewebe, mehrfach kalandriert.
  Beste Formstabilität im Dacron-Bereich. Lebensdauer: 8–12 Jahre.

**Pflegeanweisungen:**
- Regelmäßig mit Süßwasser spülen (Salzkristalle schädigen die Fasern)
- Nicht in Waschmaschine waschen
- Schimmelbefall mit mildem Essig-Wasser behandeln (keine Bleiche!)
- Trocken lagern, nicht dauerhaft gefaltet (Knickbrüche)
- UV-Schutz durch Rollgenua-Einrollen oder Persenning

### 3.2 Pentex (High-Modulus-Polyester)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Dehnung (vs. Dacron) | ca. 50 % weniger Dehnung |
| UV-Beständigkeit | Gut bis sehr gut |
| Lebensdauer | 4–7 Jahre |
| Preis (Segeltuch) | 40–70 EUR/m² |
| Einsatz | Fahrtensegel mit höherer Performance |

**Beschreibung:**
Pentex ist ein speziell behandeltes Polyester mit deutlich geringerer Dehnung als
Standard-Dacron. Es bietet einen Kompromiss zwischen der Haltbarkeit von Dacron und
der Performance von Laminaten. Pentex wird häufig als Garn in gewebten oder als
Faser in laminierten Segeln verwendet.

**Typische Einsatzgebiete:**
- Rollgenuas für Performance-Fahrtensegler
- Cross-Cut- und Radial-Schnitte
- Yachten 10–16 m, die mehr Performance als Dacron wollen, aber nicht auf Laminat umsteigen

### 3.3 Technora (Aramid, HT)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Bruchfestigkeit | 3.000 MPa |
| E-Modul | 73 GPa |
| Dehnung bei Bruch | 4,6 % |
| UV-Beständigkeit | Mäßig (3–5 Jahre ohne Schutz) |
| Preis (Segeltuch, Laminat) | 60–120 EUR/m² |

**Beschreibung:**
Technora ist eine hochfeste Aramidfaser (entwickelt von Teijin), die in Segellaminaten
als Verstärkungsfaser eingesetzt wird. Sie bietet höhere Festigkeit und geringere Dehnung
als Dacron bei akzeptabler UV-Beständigkeit. Technora ist UV-beständiger als Kevlar
und wird daher bevorzugt in Segellaminaten verwendet.

**Achtung UV-Degradation:**
Auch Technora leidet unter UV-Strahlung, wenngleich weniger als Kevlar. Segel mit
Technora-Fasern müssen bei Nichtgebrauch geschützt werden (Rollgenua einrollen,
Persenning, UV-Schutzstreifen).

### 3.4 Carbon (Kohlefaser)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Bruchfestigkeit | 3.500–7.000 MPa |
| E-Modul | 230–400 GPa |
| Dehnung bei Bruch | 1,5–2,0 % |
| UV-Beständigkeit | Hervorragend |
| Gewicht | 1,75 g/cm³ |
| Preis (Segeltuch, Laminat) | 120–250 EUR/m² |

**Beschreibung:**
Kohlefaser ist das ultimative Segelmaterial hinsichtlich Festigkeit-zu-Gewicht-Verhältnis
und Dehnungsresistenz. Sie wird in High-Performance-Laminaten und Membransegeln eingesetzt.

**Nachteile:**
- Empfindlich gegen Knickbelastung (Falten = Faserbruch)
- Hoher Preis
- Reparatur aufwendig und teuer
- Erfordert sorgfältige Handhabung (kein hartes Falten, kein Drauftreten)

**Einsatzempfehlung:**
Carbon-Segel sind primär für Regatta-Yachten und Performance-Cruiser sinnvoll,
die bereit sind, den höheren Preis und die eingeschränkte Haltbarkeit in Kauf
zu nehmen. Für reine Fahrtensegel ist Carbon selten die beste Wahl.

### 3.5 Dyneema / Spectra (UHMWPE)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Bruchfestigkeit | 2.500–3.500 MPa |
| E-Modul | 87–170 GPa |
| Dehnung bei Bruch | 2,5–3,5 % |
| UV-Beständigkeit | Gut |
| Feuchtigkeitsaufnahme | 0 % |
| Dichte | 0,97 g/cm³ (leichter als Wasser!) |
| Preis (Segeltuch, Laminat) | 80–160 EUR/m² |

**Beschreibung:**
Dyneema (DSM) und Spectra (Honeywell) sind Handelsbezeichnungen für UHMWPE (Ultra High
Molecular Weight Polyethylene). Diese Faser bietet ein hervorragendes Verhältnis von
Festigkeit zu Gewicht und ist resistent gegen UV-Strahlung, Feuchtigkeit und Chemikalien.

**Besonderheiten:**
- Schwimmt auf Wasser (Dichte < 1,0)
- Kriechverhalten (Creep): Dyneema dehnt sich unter Dauerlast langsam plastisch.
  Neuere Varianten (DM20, SK99) haben deutlich reduziertes Creep-Verhalten.
- Hervorragend für Leichtwind-Laminate und als Verstärkungsfaser in Dacron-Hybridtüchern.

### 3.6 Vectran (LCP)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Bruchfestigkeit | 2.800–3.200 MPa |
| E-Modul | 75–103 GPa |
| Dehnung bei Bruch | 3,3 % |
| UV-Beständigkeit | Schlecht (muss einlaminiert werden) |
| Kriechverhalten | Minimal (besser als Dyneema) |
| Preis (Segeltuch, Laminat) | 70–140 EUR/m² |

**Beschreibung:**
Vectran (Kuraray/Celanese) ist eine flüssigkristalline Polymerfaser (LCP) mit
exzellenter Formstabilität und minimalem Kriechverhalten. Sie wird häufig in
Hochleistungs-Segellaminaten eingesetzt, muss jedoch vor UV-Strahlung geschützt werden.

**Einsatz:**
- Verstärkungsfaser in Laminaten (zwischen Mylar-Folien geschützt)
- Kombination mit Taffeta-Außenschicht als UV-Schutz
- Häufig in Genuas für Performance-Cruiser (12–18 m)

### 3.7 Mylar-Laminate

**Beschreibung:**
Mylar (DuPont-Handelsname für biaxial orientierte PET-Folie) wird als Matrix-Folie in
Segellaminaten verwendet. Die Verstärkungsfasern (Dacron, Pentex, Technora, Carbon,
Dyneema, Vectran) werden zwischen zwei Mylar-Folien einlaminiert.

**Aufbau eines typischen Segellaminats:**
```
Außen:   Taffeta (gewebte Schutzschicht, optional)
         Mylar-Folie (0,02–0,075 mm)
Mitte:   Verstärkungsfasern (orientiert nach Lastpfaden)
         Klebstoff
Innen:   Mylar-Folie (0,02–0,075 mm)
         Taffeta (gewebte Schutzschicht, optional)
```

**Taffeta-Optionen:**
- Kein Taffeta: Leichtester Aufbau, aber empfindlich gegen Abrieb. Für Regatta.
- Einseitiger Taffeta: Kompromiss aus Gewicht und Haltbarkeit. Für Performance-Cruiser.
- Beidseitiger Taffeta: Maximale Haltbarkeit, mehr Gewicht. Für Fahrtensegler.

**Mylar-Folienstärken:**
- 0,5 mil (0,013 mm): Ultra-leicht, nur für Regatta-Laminate
- 0,75 mil (0,019 mm): Leichtwind-Segel, Performance-Cruiser
- 1,0 mil (0,025 mm): Standard für Fahrtensegel-Laminate
- 1,5 mil (0,038 mm): Starkwind-Laminate
- 2,0–3,0 mil (0,050–0,075 mm): Schwerlast-Anwendungen

**Delaminierungs-Risiken:**
- UV-Strahlung degradiert den Klebstoff zwischen Folien und Fasern
- Wiederholtes Knicken (Falten) löst die Laminat-Schichten
- Feuchtigkeitseintritt an Kanten oder Nähten beschleunigt die Delaminierung
- Hitze (> 60 °C) kann den Klebstoff erweichen

### 3.8 Hydra Net / DCF (Dyneema Composite Fabric)

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Gewicht | 30–120 g/m² |
| Dehnung | < 1 % (praktisch dehnungsfrei) |
| UV-Beständigkeit | Sehr gut (Dyneema-Grundmaterial) |
| Wasseraufnahme | 0 % |
| Preis | 150–350 EUR/m² |
| Lebensdauer | 5–8 Jahre (abhängig von Handhabung) |

**Beschreibung:**
DCF (ehemals Cuben Fiber) ist ein ultraleichtes Laminat aus Dyneema-Fasern in einer
Mylar-Matrix. Es wird ohne Weben hergestellt — die Fasern werden in gewünschter
Orientierung zwischen Mylar-Folien laminiert. DCF ist das leichteste verfügbare
Segelmaterial mit exzellenter Formstabilität.

**Einsatz bei Vorsegeln:**
- Primär für Regatta (Offshore-Regatta, Einhandsegler)
- Zunehmend bei Performance-Cruisern für Leichtwind-Genuas
- Code 0 und Gennaker (wo Gewicht kritisch ist)

### 3.9 3Di (North Sails)

**Beschreibung:**
3Di ist North Sails' proprietäres Membran-Segeltuchverfahren. Im Gegensatz zu
traditionellen Laminaten werden die Fasern (Dyneema, Carbon, Technora) in einem
geformten Prozess direkt auf die Segel-Oberfläche aufgebracht.

**Varianten:**

| Variante | Fasern | Einsatz | Preis-Aufschlag vs. Dacron |
|---|---|---|---|
| 3Di Nordac | Polyester | Fahrtensegel, Einsteiger-3Di | +80–120 % |
| 3Di Endurance | Dyneema + Polyester | Langfahrt, Offshore | +120–180 % |
| 3Di 780 | Dyneema + Carbon | Performance-Cruising | +200–280 % |
| 3Di 700 | Carbon | Regatta-Cruising | +280–400 % |
| 3Di Raw | Carbon (dünn) | Reine Regatta | +400–600 % |

**Vorteile:**
- Nahtlose Konstruktion (geringere Leck-Punkte für Delaminierung)
- Exzellente Formstabilität über die gesamte Lebensdauer
- Geringeres Flattern = längere Lebensdauer
- Reparierbar durch North Sails Service-Netzwerk

**Nachteile:**
- Nur über North Sails erhältlich (proprietär)
- Hoher Preis
- Reparatur nur durch autorisierte Lofts sinnvoll
- Mindest-Vorlaufzeit 4–8 Wochen

### 3.10 EPEX (Elvström Sails)

**Beschreibung:**
EPEX ist das proprietäre Segeltuch-System von Elvström Sails (jetzt Teil der Elvström
Sobstad Gruppe). Es verwendet ein patentiertes Polyester-Laminat-Verfahren mit
hoher Formstabilität und guter Haltbarkeit.

**Varianten:**
- **EPEX Polyester:** Einstiegs-Laminat, für Fahrtensegel
- **EPEX Hybrid:** Pentex- und Dyneema-Fasern, für Performance-Cruiser
- **EPEX Carbon:** Carbon-Verstärkung für Regatta-Segel

**Preisbereich:** +50–200 % gegenüber vergleichbarem Dacron-Segel

### 3.11 Stratis (Doyle Sails)

**Beschreibung:**
Stratis ist das proprietäre Membran-Segeltuchverfahren von Doyle Sails. Ähnlich wie 3Di
werden die Fasern in einem geformten Prozess aufgebracht, jedoch mit einer anderen
Fertigungsmethode (flacher Aufbau statt geformter 3D-Prozess).

**Varianten:**
- **Stratis ICE:** Weiße Fasern (Dyneema), dezente Optik, für Fahrtensegler
- **Stratis GTX:** Gemischte Fasern (Dyneema/Technora), Performance-Cruising
- **Stratis D4:** Carbon-Fasern, Regatta

**Vorteil gegenüber 3Di:** Flachere Produktionsform ermöglicht größere Segel-Stücke
ohne Klebestellen.

### 3.12 UV-Schutzstreifen (Sunbrella / Weblon)

**Funktion:**
Der UV-Schutzstreifen wird am Achterliek und Unterliek einer Rollgenua angebracht.
Wenn das Segel eingerollt ist, schützt dieser Streifen das exponierte Segeltuch
vor UV-Strahlung.

**Material:**
- **Sunbrella (Glen Raven):** Acryl-Gewebe, lösung-gefärbt, hervorragende UV-Beständigkeit.
  Standardmaterial. Farben: navy, schwarz, grau, weiß, blau, rot. Preis: 18–35 EUR/lfm.
- **Weblon (Herculite):** Vinyl-beschichtetes Polyester, glatte Oberfläche, etwas
  steifer. Preis: 22–40 EUR/lfm.

**Dimensionierung:**
Die Breite des UV-Schutzstreifens muss so berechnet werden, dass bei vollständig
eingerollter Genua der Streifen das gesamte Segel abdeckt:

```
UV-Streifen-Breite = π × Furler-Trommel-Durchmesser × Anzahl Wicklungen × 0,85
```

> ⚠️ **ZU PRÜFEN (Audit):** Diese vereinfachte Formel widerspricht der detaillierten, mit Rechenbeispiel validierten Berechnung in Abschnitt 4.5 (`UV_breite = π × D_gesamt / 2 × F_sicherheit`, mit `D_gesamt = D_trommel + 2·D_liektau·N`) und liefert um ca. Faktor 5 zu große Werte. Maßgeblich ist Abschnitt 4.5.

**Richtwerte:**

| Segelfläche | UV-Streifen-Breite (Achterliek) | UV-Streifen-Breite (Unterliek) |
|---|---|---|
| bis 25 m² | 200–300 mm | 150–250 mm |
| 25–40 m² | 300–400 mm | 250–350 mm |
| 40–60 m² | 400–550 mm | 350–450 mm |
| über 60 m² | 500–700 mm | 400–550 mm |

**Lebensdauer:**
- Sunbrella: 8–12 Jahre (mediterran), 10–15 Jahre (Nordeuropa)
- Weblon: 6–10 Jahre (mediterran), 8–12 Jahre (Nordeuropa)
- Austausch bei sichtbarer Fadenmüdigkeit, Verfärbung > 50 %, oder Rissbildung

---

## 4. Konstruktion und Schnitt

### 4.1 Cross-Cut (Kreuzschnitt)

**Beschreibung:**
Beim Cross-Cut-Schnitt verlaufen die Tuchbahnen horizontal (parallel zum Unterliek).
Die Kettfäden des Gewebes nehmen die Hauptlasten entlang der Bahnen auf. Dies ist
der einfachste und kostengünstigste Schnitt.

**Vorteile:**
- Günstigste Herstellung (wenig Verschnitt)
- Gut geeignet für gewebte Materialien (Dacron, Pentex)
- Einfache Reparatur (Bahnen-Ersatz)
- Bewährte Technologie seit Jahrzehnten

**Nachteile:**
- Lastverteilung nicht optimal (Bias-Dehnung zwischen den Bahnen)
- Formverlust schneller als bei Radial- oder Membranschnitten
- Bei großen Segeln (> 40 m²) stärkere Profilverformung unter Last

**Empfehlung:**
Cross-Cut ist ideal für Dacron-Fahrtensegel bis 14 m Bootslänge, Charter-Segel
und Budget-bewusste Segler. Für Performance-orientierte Segler ab 12 m Bootslänge
sind Radialschnitte oder Membransegel empfehlenswert.

### 4.2 Radial-Schnitt

**Beschreibung:**
Beim Radialschnitt verlaufen die Tuchbahnen von den drei Ecken des Segels (Kopf,
Schothorn, Hals) sternförmig nach innen. Die Kettfäden folgen damit den Haupt-
Lastpfaden im Segel.

**Varianten:**
- **Tri-Radial:** Bahnen von allen drei Ecken, vollständig radial
- **Bi-Radial:** Radiale Bahnen von Kopf und Schothorn, Cross-Cut im Unterliek-Bereich
- **Radial-Head:** Nur vom Kopf radial, Rest Cross-Cut

**Vorteile:**
- Bessere Lastverteilung als Cross-Cut
- Längere Formstabilität (20–40 % länger als Cross-Cut bei gleichem Material)
- Möglichkeit, verschiedene Tuchgewichte in verschiedenen Zonen einzusetzen

**Nachteile:**
- Höherer Herstellungsaufwand (mehr Verschnitt, komplexere Nähte)
- Teurer als Cross-Cut (+15–30 %)
- Mehr Nähte = mehr potenzielle Schwachstellen

**Empfehlung:**
Tri-Radial ist der Standard für Performance-Fahrtensegel und Regattasegel in
gewebten Materialien. Für Laminate ist der Radialschnitt weniger relevant,
da die Fasern im Laminat bereits orientiert sind.

### 4.3 Membranschnitt

**Beschreibung:**
Membransegel (3Di, Stratis, EPEX) werden nicht aus vorgefertigten Tuchbahnen
zusammengenäht, sondern als ganzes Segel oder in großen Paneelen geformt. Die
Verstärkungsfasern werden individuell entlang der Lastpfade platziert, berechnet
durch Finite-Elemente-Analyse.

**Vorteile:**
- Optimale Faserausrichtung entlang aller Lastpfade
- Keine oder minimale Nähte (Schwachstellenreduktion)
- Beste Formstabilität über die Lebensdauer
- Leichtester Aufbau bei gegebener Festigkeit

**Nachteile:**
- Höchster Preis (+100–500 % vs. Dacron-Cross-Cut)
- Aufwendige Reparatur (Spezial-Lofts erforderlich)
- Empfindlicher gegen mechanische Beschädigung (Knicken, Abrieb)
- Längere Lieferzeiten (4–12 Wochen)

### 4.4 Vorliek-Befestigung

**4.4.1 Liektau (Luff Tape)**

Das Liektau ist ein Tau oder Band, das in eine Nut (Groove) am Vorstag oder in
den Furler-Profil-Kanal eingeführt wird.

**Spezifikationen:**

| Bootsgröße | Liektau-Durchmesser | Typischer Furler |
|---|---|---|
| 8–10 m | 4–6 mm | Furlex 200S, Profurl C290 |
| 10–13 m | 6–8 mm | Furlex 300S, Profurl C350/C420 |
| 13–16 m | 8–10 mm | Furlex 400S, Profurl C480/NEX 7.0 |
| 16–20 m | 10–13 mm | Harken MKIV Unit 2, Profurl NEX 10.0 |
| 20+ m | 13–16 mm | Reckmann, Harken MKIV Unit 3+ |

**Material:**
- Standard: Polyester-Tau mit Kern
- Premium: Dyneema/Spectra-Kern mit Polyester-Mantel
- UV-beständige Ausführung: PVC- oder Teflon-beschichteter Mantel

**4.4.2 Stagreiter (Hanks)**

Stagreiter sind Karabiner-artige Beschläge, die das Vorliek des Segels am Vorstag
befestigen. Sie werden heute primär bei Sturmfock, Staysail und auf älteren Yachten
ohne Furler verwendet.

**Typen:**
- **Piston Hanks (Kolben-Stagreiter):** Federbetätigter Kolben, Standard
- **Snap Hanks (Schnapp-Stagreiter):** Einfacher Federmechanismus
- **Inglefield Clips:** Doppel-Karabiner-System, leichtgängiger

**Material:** Bronze (Standard), Edelstahl 316L (Salzwasser), Kunststoff (Leichtwind)

**Abstände:**
- Standard: 250–350 mm Abstand zwischen Stegreitern
- Starkwind-Segel: 200–250 mm
- Sturmfock: 150–200 mm

**4.4.3 Groove-Systeme (Nutschiene)**

Bei Yachten ohne Rollreffanlage kann ein Groove-System am Vorstag montiert werden.
Das Vorliek wird in eine Nut eingeführt (ähnlich dem Großsegel-Mast-Profil).

**Hersteller:**
- Selden Furlex Groove: 280–600 EUR
- Harken Luff Groove: 350–700 EUR
- Profurl Foil: 300–650 EUR

### 4.5 UV-Streifen-Berechnung und Montage

**Montage-Methoden:**

1. **Aufgenäht:** UV-Streifen wird auf das Achterliek und Unterliek genäht.
   Standardmethode, robust, aber Nähte können UV-geschädigtes Material schwächen.

2. **Eingeklebt:** UV-Streifen wird in eine Tasche eingeklebt und zusätzlich genäht.
   Bessere Kraftübertragung, aufwendiger.

3. **Integriert:** UV-Streifen ist Teil des Segel-Laminats (nur bei Membransegeln).
   Beste Lösung, aber nur bei Neuanfertigung möglich.

**Berechnung der UV-Streifen-Breite (Detail):**

```
Eingangsparameter:
- D_trommel = Durchmesser der Furler-Trommel (mm)
- D_liektau = Durchmesser des Liektaus (mm)
- N = Anzahl der Wicklungen bei voll eingerolltem Segel
- F_sicherheit = 1,15 (15 % Sicherheitszuschlag)

Berechnung:
D_gesamt = D_trommel + (2 × D_liektau × N)
UV_breite = π × D_gesamt / 2 × F_sicherheit

Praxisregel:
UV_breite ≈ D_gesamt × 1,8
```

**Beispielrechnung (38-Fuß-Yacht, Furlex 300S):**
- D_trommel = 80 mm
- D_liektau = 7 mm
- N = 8 Wicklungen (typisch für 130 %-Genua)
- D_gesamt = 80 + (2 × 7 × 8) = 192 mm
- UV_breite = π × 192 / 2 × 1,15 = 347 mm → Empfehlung: 350 mm

### 4.6 Furler-Kompatibilität

Die Kompatibilität zwischen Segel und Rollreffanlage ist entscheidend für die
Funktionalität. Inkompatibilität führt zu:
- Schwergängigem Rollen
- Asymmetrischem Wickelbild
- Vorzeitigem Verschleiß des Liektaus
- Blockieren der Furler-Trommel

**Kompatibilitätsmatrix:**

| Furler-Modell | Max. Vorstag-Ø | Max. Liektau-Ø | Max. Segelfläche | Kopfwirbel-Typ |
|---|---|---|---|---|
| Selden Furlex 200S | 8 mm | 6 mm | 28 m² | Selden Standard |
| Selden Furlex 300S | 10 mm | 8 mm | 45 m² | Selden Standard |
| Selden Furlex 400S | 12 mm | 10 mm | 70 m² | Selden Standard |
| Profurl C290 | 8 mm | 5 mm | 25 m² | Profurl Standard |
| Profurl C350 | 9 mm | 7 mm | 35 m² | Profurl Standard |
| Profurl C420 | 10 mm | 8 mm | 45 m² | Profurl Standard |
| Profurl NEX 7.0 | 12 mm | 9 mm | 55 m² | Profurl NEX |
| Profurl NEX 10.0 | 14 mm | 11 mm | 80 m² | Profurl NEX |
| Harken MKIV Unit 1 | 10 mm | 7 mm | 38 m² | Harken MKIV |
| Harken MKIV Unit 2 | 12 mm | 10 mm | 60 m² | Harken MKIV |
| Harken MKIV Unit 3 | 14 mm | 12 mm | 90 m² | Harken MKIV |

---

## 5. Trimm

### 5.1 Grundlagen des Vorsegel-Trimms

Der korrekte Vorsegel-Trimm ist entscheidend für Geschwindigkeit, Balance und Komfort.
Die vier Hauptparameter sind:

1. **Schot-Spannung (Sheet Tension):** Bestimmt den Twist (Verwindung) und die
   Profiltiefe des Segels.
2. **Holepunkt-Position (Lead Position):** Bestimmt das Verhältnis von Achterliek-
   Spannung zu Unterliek-Spannung.
3. **Fall-Spannung (Halyard Tension):** Bestimmt die Position der maximalen
   Profiltiefe entlang des Vorlieks.
4. **Vorstag-Spannung (Forestay Tension):** Bestimmt den Vorstag-Durchhang und
   damit die Gesamtform des Segels.

### 5.2 Schot-Führung und Holepunkt (Sheet Lead Position)

**Grundregel:**
Der Holepunkt (Genuaschot-Leitblock) muss so positioniert werden, dass die
imaginäre Verlängerung der Schot die Mitte des Vorlieks trifft. Diese Linie
bildet einen Winkel zur Horizontalen, der als „Schot-Winkel" (sheet angle)
bezeichnet wird.

**Optimaler Schot-Winkel:**

| Segel-Typ | Schot-Winkel zur Horizontalen |
|---|---|
| Genua 1 (150 %) | 7–9° |
| Genua 2 (130 %) | 9–11° |
| Genua 3 (115 %) | 10–12° |
| Fock (100 %) | 11–14° |
| Selbstwendefock | 12–15° |
| Sturmfock | 15–20° |

**Holepunkt zu weit vorn:**
- Achterliek zu dicht → Segel „gehakt" (hooking)
- Obere Trimmfäden (Telltales) fallen nach Lee
- Großsegel-Anströmung gestört
- Mehr Krängung, weniger Höhe

**Holepunkt zu weit achtern:**
- Achterliek offen → Segel „twistet" zu stark
- Untere Trimmfäden fallen nach Lee
- Leech-Flutter (Achterliek-Flattern)
- Weniger Vortrieb, offeneres Achterliek

### 5.3 Barber Hauler

**Funktion:**
Der Barber Hauler ist ein zusätzlicher Block-/Taljen-System, das den Schot-
Holepunkt nach innen (Luv-Barber) oder nach außen (Lee-Barber) versetzt.

**Einsatzfälle:**
- **Luv-Barber (Inhaul):** Zieht den Holepunkt nach Luv. Einsatz: Halbwind-
  bis Raumschot-Kurse, um das Achterliek der Genua dichter zu halten.
- **Lee-Barber (Outhaul):** Zieht den Holepunkt nach Lee. Einsatz: bei
  gereffter Genua (teileingerollt), um den Schot-Winkel zu korrigieren.

**Montage-Empfehlungen:**
- Luv-Barber: Block an Schiene oder Decksbeschlag, ca. 300–500 mm achterlich
  des Standard-Holepunkts
- Lee-Barber: Block an der Außenseite des Decksbeschlags, idealerweise auf
  einer kurzen Schiene
- Talje-Verhältnis: 2:1 bis 4:1 (je nach Bootsgröße)
- Klampe oder Stopper für schnelles Belegen/Lösen

### 5.4 Genua-Car-Schiene (Genua Track)

**Positionierung:**
Die Genua-Schiene (jib lead track) wird auf dem Seitendeck montiert und
ermöglicht die Vor-/Achterlich-Verstellung des Holepunkts.

**Schienenlänge-Berechnung:**

```
Schienenlänge = Vorstaglänge × 0,12 bis 0,15
Typisch: 1.000–2.500 mm bei 10–16 m Yachten
```

**Position (Querabstand zur Mittellinie):**

| Bootsgröße | Querabstand (ca.) |
|---|---|
| 8–10 m | 15–20 % der max. Bootsbreite |
| 10–13 m | 18–22 % der max. Bootsbreite |
| 13–16 m | 20–25 % der max. Bootsbreite |

**Schienensysteme und Wagen:**

| Hersteller | System | Bootsgröße | Preis (Schiene + Wagen) |
|---|---|---|---|
| Harken | 27 mm T-Track | 8–11 m | 350–700 EUR |
| Harken | 32 mm T-Track | 11–14 m | 500–1.000 EUR |
| Antal | 30 mm Track | 9–12 m | 300–600 EUR |
| Antal | 40 mm Track | 12–16 m | 500–900 EUR |
| Lewmar | Size 1/2 Track | 8–14 m | 400–800 EUR |
| Frederiksen | 27/30 mm Track | 8–13 m | 280–550 EUR |

### 5.5 Schot-Spannung (Sheet Tension)

**Trimm-Indikatoren:**

1. **Trimmfäden (Telltales):** Die wichtigsten visuellen Trimm-Indikatoren.
   Montage: drei Paare (Luv/Lee) bei 25 %, 50 % und 75 % der Vorliekhöhe.

   **Korrekt getrimmt:** Alle Trimmfäden strömen parallel nach achtern.
   **Zu dicht (übertrimmt):** Lee-Trimmfäden fallen nach unten oder wirbeln.
   **Zu offen (untertrimmt):** Luv-Trimmfäden flattern oder stehen ab.

2. **Achterliek-Form:** Beobachten der Achterliek-Krümmung:
   - Offen (konkav): zu wenig Schot-Spannung oder Holepunkt zu weit achtern
   - Neutral (gerade): optimal für Amwind
   - Geschlossen (konvex): zu viel Schot-Spannung oder Holepunkt zu weit vorn

3. **Achterliek-Trimmfaden:** Ein einzelner Trimmfaden am oberen Achterliek.
   Dieser sollte ca. 50 % der Zeit frei strömen. Wenn er dauerhaft
   hinter dem Achterliek verschwindet, ist das Segel zu dicht.

### 5.6 Fall-Spannung (Halyard Tension)

**Funktion:**
Die Fall-Spannung verschiebt die Position der maximalen Profiltiefe:
- Mehr Spannung → Profil wandert nach vorn (Vorliek glatter)
- Weniger Spannung → Profil wandert nach achtern (Vorliek bauchiger)

**Optimale Profil-Position:**
- Leichtwind (< 8 kn): Maximale Wölbung bei 40–45 % der Sehnenlänge
- Mittelwind (8–15 kn): Maximale Wölbung bei 35–40 %
- Starkwind (> 15 kn): Maximale Wölbung bei 30–35 %

**Visuelle Kontrolle:**
Horizontale Falten parallel zum Vorliek = zu wenig Fall-Spannung (Profil zu weit achtern).
Vertikale Streifen am Vorliek = zu viel Fall-Spannung (Material überdehnt).

**Cunningham:**
Bei Segeln mit Cunningham-Öse (Loch im Vorliek oberhalb des Halsbeschlags)
kann die Vorliek-Spannung unabhängig von der Fall-Spannung erhöht werden.
Dies ist besonders nützlich, wenn das Fall auf Maximum steht und weitere
Vorliek-Straffung gewünscht ist.

### 5.7 Selbstwendefock-Trimm

**Besonderheiten:**
Die Selbstwendefock hat nur einen eingeschränkten Trimmbereich:
- Holepunkt ist auf die Fockschiene begrenzt
- Kein klassischer Luv-/Lee-Barber möglich
- Schot-Spannung ist der primäre Trimmparameter

**Trimm-Sequenz:**

1. **Schienen-Position einstellen:** Der Anschlag auf der Fockschiene bestimmt
   den maximalen Ausholwinkel. Bei zu engem Anschlag dreht das Segel bei
   der Wende nicht vollständig; bei zu weitem Anschlag wird das Segel zu
   offen auf Amwind-Kursen.

2. **Schot-Spannung:** Über eine Trimmschot (Sheet Trimmer) oder einen
   Einzelblock mit Klemme wird die Schot-Spannung eingestellt.

3. **Fallspannung:** Analog zu anderen Vorsegeln.

4. **Baumniederholer (Vang):** Einige Selbstwendefock-Systeme haben einen
   Niederholer am Fockbaum, der das Achterliek kontrolliert.

**Häufige Probleme:**
- Segel wendet nicht sauber → Schienen-Anschlag prüfen, Schot-Länge prüfen
- Segel zu flach auf Raumschot → Fockbaum-Niederholer lösen
- Segel zu bauchig bei Starkwind → Mehr Schot, mehr Fall, Reff erwägen

### 5.8 Code 0 Trimm

**Besonderheiten:**
Der Code 0 wird auf einem Top-Down-Furler gefahren und hat ein sehr empfindliches
Trimmprofil. Fehltrimmung führt schnell zu Kollaps oder Stundenglas-Bildung.

**Trimm-Parameter:**

1. **Schot-Winkel:** Der Code 0 wird mit sehr offenem Schot-Winkel gefahren
   (15–25° zur Mittellinie, abhängig vom Kurs).

2. **Schot-Spannung:** Leichter Zug. Das Achterliek darf leicht offen stehen.
   Zu viel Schot-Spannung erzeugt einen „Haken" im Achterliek, der den
   Luftstrom stört.

3. **Tacker-Position:** Der Tacker-Punkt (Hals-Befestigung am Bugspriet)
   beeinflusst den gesamten Segelschnitt. Variabler Tacker ermöglicht
   Anpassung an verschiedene Windwinkel.

4. **Furler-Spannung:** Das Torque-Seil muss unter leichter Vorspannung
   stehen, um Stundenglas-Bildung beim Bergen zu vermeiden.

**Stundenglas-Vermeidung:**
- Vor dem Einrollen: Kurs so wählen, dass der Code 0 nicht im Windschatten
  des Großsegels steht
- Einroll-Geschwindigkeit: gleichmäßig, nicht ruckartig
- Bei Stundenglas: NICHT weiter rollen! Schot lösen, Segel zum Flattern bringen,
  neu ausrollen, erneut versuchen

### 5.9 Vorstag-Spannung und Durchhang

**Einfluss auf das Segelprofil:**
Ein durchhängendes Vorstag erzeugt ein tieferes Profil (mehr Bauch) im Vorsegel.
Ein straffes Vorstag ergibt ein flacheres Profil.

**Vorstag-Spannung einstellen über:**
- Achterstag-Spannung (primärer Hebel bei Masttop-Rigg)
- Backstag-Spannung (bei Fraktional-Rigg)
- Wantentrimmung (Oberwanten)
- Checkstagen (bei Kutter-Rigg)

**Richtwerte für Vorstag-Durchhang:**

| Windstärke | Erlaubter Durchhang (% der Vorstaglänge) |
|---|---|
| 0–8 kn | 2,0–3,0 % |
| 8–15 kn | 1,0–2,0 % |
| 15–25 kn | 0,5–1,0 % |
| 25+ kn | < 0,5 % |

**Beispiel:** Bei einer Vorstaglänge von 15 m ergibt ein Durchhang von 2 % einen
maximalen Abstand von 300 mm von der Geraden zwischen Masttopp und Bug-Befestigung.

---

## 6. Furler-Systeme

### 6.1 Übersicht und Funktionsprinzip

Rollreffanlagen (Furler) ermöglichen das kontrollierte Ein- und Ausrollen des
Vorsegels. Sie bestehen aus:

1. **Trommel (Drum):** Am Fuß des Vorstags, nimmt die Furler-Leine auf
2. **Profil (Foil):** Umschließt das Vorstag und bietet die Nut für das Liektau
3. **Kopfwirbel (Swivel):** Am Masttopp, ermöglicht die Drehung des Segels
4. **Furler-Leine:** Betätigt die Trommel zum Ein-/Ausrollen

**Funktionsprinzip:**
Beim Ziehen der Furler-Leine dreht sich die Trommel und wickelt das Segel um
das Profil. Die Schot muss dabei kontrolliert gefiert (gelöst) werden, um
gleichmäßiges Aufwickeln zu gewährleisten.

### 6.2 Selden Furlex

**Modellreihe:**

| Modell | Vorstag-Ø | Max. Segelfläche | Boot-LOA | Gewicht | Preis (EUR) |
|---|---|---|---|---|---|
| Furlex 104S | 5 mm | 12 m² | 6–8 m | 2,1 kg | 850–1.100 |
| Furlex 200S | 8 mm | 28 m² | 8–11 m | 4,2 kg | 1.400–1.800 |
| Furlex 200S TD | 8 mm | 28 m² | 8–11 m | 4,5 kg | 1.800–2.200 |
| Furlex 300S | 10 mm | 45 m² | 10–14 m | 6,8 kg | 2.200–2.800 |
| Furlex 300S TD | 10 mm | 45 m² | 10–14 m | 7,2 kg | 2.600–3.200 |
| Furlex 400S | 12 mm | 70 m² | 13–18 m | 11,5 kg | 3.500–4.500 |

**Besonderheiten:**
- „S"-Serie: Aktuelle Serie mit verbessertem Profil und Kugellager
- „TD"-Varianten: Top-Down-Furler für Code 0 / Gennaker
- Profillängen: 1 m oder 2 m Segmente, beliebig kombinierbar
- Werkzeugfreie Montage des Segels (Liektau-Einführung von unten)

**Wartung:**
- Jährlich: Süßwasser-Spülung, Sichtprüfung der Kugellager
- Alle 3 Jahre: Kugellager-Inspektion, ggf. Fett-Nachfüllung
- Alle 5–7 Jahre: Kugellager-Austausch (Ersatzteil: 80–180 EUR)
- Profil-Verbinder: auf Korrosion prüfen, ggf. austauschen

### 6.3 Profurl

**Modellreihe:**

| Modell | Vorstag-Ø | Max. Segelfläche | Boot-LOA | Preis (EUR) |
|---|---|---|---|---|
| C290 | 8 mm | 25 m² | 7–10 m | 1.200–1.600 |
| C350 | 9 mm | 35 m² | 9–12 m | 1.800–2.400 |
| C420 | 10 mm | 45 m² | 11–14 m | 2.400–3.200 |
| C480 | 12 mm | 60 m² | 13–16 m | 3.200–4.200 |
| NEX 5.0 | 10 mm | 40 m² | 10–13 m | 2.800–3.600 |
| NEX 7.0 | 12 mm | 55 m² | 12–16 m | 3.800–4.800 |
| NEX 10.0 | 14 mm | 80 m² | 15–20 m | 5.200–6.800 |
| NEX 15.0 | 16 mm | 120 m² | 18–24 m | 7.500–9.500 |
| Spin 2 | — | 50 m² | 10–14 m | 2.800–3.800 |
| Spin 3 | — | 80 m² | 13–18 m | 3.800–5.200 |

**Besonderheiten:**
- C-Serie: Bewährte Einsteiger-Linie, manuelles System
- NEX-Serie: Hochleistungs-Furler mit integrierten Kugellagern, geringerem
  Drehmoment, längerer Lebensdauer
- Spin-Serie: Top-Down-Furler für asymmetrische Segel

**Wartung:**
- Halbjährlich: Süßwasser-Spülung der Trommel und des Kopfwirbels
- Jährlich: Drehmoment-Test (Segel ausrollen sollte mit < 5 kg Zug möglich sein)
- Alle 3–4 Jahre: Lager-Service, Dichtungs-Austausch
- Profurl-spezifisch: Trommel-Feder (Rückhol-Feder) alle 5 Jahre prüfen

### 6.4 Harken MKIV

**Modellreihe:**

| Modell | Vorstag-Ø | Max. Segelfläche | Boot-LOA | Preis (EUR) |
|---|---|---|---|---|
| MKIV Unit 0 | 6 mm | 18 m² | 6–9 m | 1.100–1.500 |
| MKIV Unit 1 | 10 mm | 38 m² | 9–13 m | 2.400–3.200 |
| MKIV Unit 2 | 12 mm | 60 m² | 12–17 m | 3.800–5.000 |
| MKIV Unit 3 | 14 mm | 90 m² | 16–22 m | 5.500–7.500 |
| MKIV Unit 4 | 16 mm | 130 m² | 20–26 m | 8.000–11.000 |

**Besonderheiten:**
- Bewährtes System mit langer Marktpräsenz
- Robuste Konstruktion, besonders für Blauwasser-Einsatz geeignet
- Aluminium-Profil mit eloxierter Oberfläche
- Einzelnes Torque-Tube-Design (geringere Reibung als Zweiteilige Profile)

**Wartung:**
- Jährlich: Trommel-Inspektion, Furler-Leine auf Verschleiß prüfen
- Alle 2 Jahre: Kopfwirbel-Lager schmieren (Harken-Spezialfett)
- Alle 5 Jahre: Lager-Austausch empfohlen
- Profilverbinder: Schrauben auf Festsitz prüfen (Edelstahl-Klemmschraube)

### 6.5 Facnor FX+ / LS

**Modellreihe:**

| Modell | Typ | Max. Segelfläche | Boot-LOA | Preis (EUR) |
|---|---|---|---|---|
| FX+ 1500 | Genua-Furler | 20 m² | 7–9 m | 1.000–1.400 |
| FX+ 2500 | Genua-Furler | 35 m² | 9–12 m | 1.800–2.400 |
| FX+ 3500 | Genua-Furler | 50 m² | 11–15 m | 2.800–3.600 |
| FX+ 4500 | Genua-Furler | 70 m² | 14–18 m | 3.800–5.000 |
| LS 130 | Code 0 Furler | 30 m² | 8–11 m | 1.800–2.400 |
| LS 170 | Code 0 Furler | 55 m² | 11–15 m | 2.600–3.600 |
| LS 200 | Code 0 Furler | 80 m² | 14–18 m | 3.600–4.800 |

**Besonderheiten:**
- FX+: Kompaktes Design, geringes Gewicht, ideal für Serienyachten
- LS-Serie: Top-Down-Furler mit freilaufendem Torsionsseil
- Integrierter Halyard-Swivel (Kopfwirbel mit Fall-Durchführung)

### 6.6 Karver

**Modellreihe:**

| Modell | Typ | Max. Segelfläche | Preis (EUR) |
|---|---|---|---|
| KF4 | Code 0/Gennaker | 35 m² | 3.200–4.200 |
| KF5 | Code 0/Gennaker | 55 m² | 4.200–5.500 |
| KF6 | Code 0/Gennaker | 80 m² | 5.500–7.000 |
| KF8 | Code 0/Gennaker | 120 m² | 7.000–9.000 |
| KST 12 | Selbstwendefock | 25 m² | 2.800–3.800 |
| KST 16 | Selbstwendefock | 40 m² | 3.800–5.200 |

**Besonderheiten:**
- KF-Serie: Premium-Top-Down-Furler, Rennsport-erprobt
- KST-Serie: Integriertes Selbstwende-System mit Furler
- Kontinuierliches Faserwickel-Profil (keine Segmente)
- Wartungsarm durch versiegelte Kugellager

### 6.7 Ronstan

**Modellreihe:**

| Modell | Typ | Max. Segelfläche | Preis (EUR) |
|---|---|---|---|
| RF-30 | Code 0 Furler | 20 m² | 1.800–2.400 |
| RF-45 | Code 0 Furler | 45 m² | 2.400–3.400 |
| RF-55 | Code 0 Furler | 70 m² | 3.400–4.600 |
| RF-75 | Code 0 Furler | 100 m² | 4.600–6.200 |

**Besonderheiten:**
- Australischer Hersteller mit Schwerpunkt auf Regatta-Systemen
- Leichtbau-Design (Aluminium/Delrin-Hybrid)
- Schnelle Installation und Demontage

### 6.8 Teilrollreffung — Probleme und Lösungen

**Grundproblem:**
Eine Rollgenua, die auf 70–80 % ihrer vollen Fläche eingerollt wird, verliert
ihr optimales Profil. Die Wölbung wandert nach achtern, das Achterliek wird zu
dicht, und die Effizienz sinkt deutlich.

**Lösungsansätze:**

1. **Schaumstoff-Streifen (Luff Pad):** Ein konischer Schaumstoffstreifen wird
   am Vorliek in der unteren Hälfte befestigt. Beim Einrollen erzeugt der
   Schaumstoff eine dicke Rolle im Vorliek-Bereich, die das Profil flacher hält.
   Preis: 50–150 EUR.

2. **Cunningham-Öse:** Ermöglicht zusätzliche Vorliek-Spannung bei gerefftem Segel.

3. **Zweit-Segel-Konzept:** Statt teileingerollter Genua wird eine separate,
   kleinere Fock auf einem Kutterstag oder als Wechselsegel eingesetzt.
   Aufwendiger, aber besseres Segelprofil.

4. **Flattop-Genua:** Spezielle Genua mit geradem Kopf (kein spitzes Dreieck),
   die beim Einrollen ein gleichmäßigeres Wickelbild erzeugt. Nachteil:
   weniger Segelfläche im oberen Bereich.

---

## 7. Hersteller-Spezifikationen

### 7.1 North Sails

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| North NPC | Dacron Cross-Cut | Charter, Einsteiger | Standard |
| North NorDac | 3Di Nordac | Fahrtensegler | +80–120 % |
| North Endurance | 3Di Endurance | Langfahrt, Offshore | +120–180 % |
| North Performance | 3Di 780/700 | Performance-Cruiser | +200–400 % |
| North Racing | 3Di Raw | Reine Regatta | +400–600 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- NPC Dacron: 3.800–4.800 EUR
- 3Di Nordac: 6.500–8.500 EUR
- 3Di Endurance: 8.000–11.000 EUR
- 3Di 780: 12.000–16.000 EUR
- 3Di Raw: 18.000–25.000 EUR

**Lieferzeit:** 4–8 Wochen (Dacron), 6–12 Wochen (3Di)

**Service-Netzwerk:** 75+ Lofts weltweit, Deutschland: Hamburg, Kiel, Tutzing,
Lindau, Berlin, Rostock

### 7.2 Elvström Sails (Elvström Sobstad)

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| Elvström Standard | Dacron Cross-Cut | Charter, Budget | Standard |
| Elvström Cruising | Dacron Radial | Aktiver Fahrtensegler | +20–40 % |
| EPEX Cruising | EPEX Polyester | Performance-Cruiser | +60–100 % |
| EPEX Performance | EPEX Hybrid | Regatta-/Fahrtensegler | +100–160 % |
| EPEX Racing | EPEX Carbon | Reine Regatta | +200–350 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- Standard Dacron: 3.200–4.200 EUR
- Cruising Dacron: 4.000–5.500 EUR
- EPEX Cruising: 5.500–7.500 EUR
- EPEX Performance: 7.500–11.000 EUR
- EPEX Racing: 12.000–18.000 EUR

**Lieferzeit:** 3–6 Wochen (Dacron), 5–10 Wochen (EPEX)

**Stärken:** Gutes Preis-Leistungs-Verhältnis, starke Präsenz in Skandinavien
und Nordeuropa. Deutsche Vertretung: Elvström Sails Deutschland (Kiel).

### 7.3 Doyle Sails

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| Doyle Delta | Dacron Cross-Cut/Radial | Charter, Fahrtensegler | Standard |
| Doyle AP | Dacron/Pentex Radial | Aktiver Segler | +30–50 % |
| Stratis ICE | Dyneema Membran | Performance-Cruiser | +120–180 % |
| Stratis GTX | Dyneema/Technora Membran | Regatta-Cruiser | +180–280 % |
| Stratis D4 | Carbon Membran | Reine Regatta | +300–500 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- Delta Dacron: 3.500–4.500 EUR
- AP Radial: 4.500–6.000 EUR
- Stratis ICE: 8.000–11.000 EUR
- Stratis GTX: 11.000–15.000 EUR
- Stratis D4: 16.000–22.000 EUR

**Lieferzeit:** 3–6 Wochen (Dacron), 6–10 Wochen (Stratis)

**Stärken:** Starke Technologie im Membran-Bereich, gutes internationales Netzwerk.
Deutsche Vertretung: Doyle Sails Germany (verschiedene Standorte).

### 7.4 Quantum Sails

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| Quantum Dacron | Dacron Cross-Cut | Charter, Budget | Standard |
| Quantum Fusion M | Taffeta-Laminat | Fahrtensegler | +40–70 % |
| Quantum iQ | Pentex/Dyneema Laminat | Performance-Cruiser | +80–140 % |
| Quantum Fusion XP | Carbon-Hybrid | Regatta-Cruiser | +150–250 % |
| Quantum Grand Prix | Carbon Membran | Reine Regatta | +300–500 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- Dacron: 3.400–4.400 EUR
- Fusion M: 4.800–6.500 EUR
- iQ: 6.800–9.500 EUR
- Fusion XP: 10.000–14.000 EUR
- Grand Prix: 15.000–22.000 EUR

**Lieferzeit:** 3–5 Wochen (Dacron), 5–8 Wochen (Laminat/Membran)

**Stärken:** Exzellenter Kundenservice, umfangreiche Design-Beratung,
Sail-Care-Programm. Vertretung in Deutschland: Quantum Sails Deutschland.

### 7.5 UK Sailmakers

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| UK Dacron | Dacron Cross-Cut | Fahrtensegler | Standard |
| UK Tape Drive X | Pentex X-Ply | Aktiver Segler | +30–60 % |
| UK Tape Drive HD | Dyneema Tape | Performance-Cruiser | +60–100 % |
| UK Titanium | Carbon Tape-Drive | Regatta | +150–250 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- Dacron: 3.200–4.000 EUR
- Tape Drive X: 4.200–5.500 EUR
- Tape Drive HD: 5.500–7.500 EUR
- Titanium: 9.000–14.000 EUR

**Stärken:** Tape-Drive-Technologie (ausgerichtete Faserbänder) als
eigenständiger Ansatz zwischen gewebtem Tuch und Membransegel.
Besonders gutes Preis-Leistungs-Verhältnis im mittleren Segment.

### 7.6 OneSails

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| OneSails 4T Forte | Dacron | Charter, Fahrtensegler | Standard |
| OneSails 4T Carbon | Carbon Laminat | Performance-Cruiser | +80–140 % |
| OneSails MX5 | Pentex/Dyneema Laminat | Regatta-Cruiser | +100–180 % |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- 4T Forte: 3.000–4.000 EUR
- 4T Carbon: 5.500–8.000 EUR
- MX5: 7.000–10.000 EUR

**Stärken:** Italienisches Design, gutes Preis-Leistungs-Verhältnis,
starke Präsenz im Mittelmeerraum. Deutsche Vertretung vorhanden.

### 7.7 Rolly Tasker Sails

**Produktlinien (Vorsegel):**

| Produktlinie | Material | Zielgruppe | Preis-Niveau |
|---|---|---|---|
| Rolly Tasker Standard | Dacron Cross-Cut | Budget-Segler | -20–30 % vs. EU |
| Rolly Tasker Premium | Dacron Radial | Fahrtensegler | -10–20 % vs. EU |
| Rolly Tasker Performance | Pentex Laminat | Performance | Standard EU-Preis |

**Preise (Genua 2, 130 %, für 38-Fuß-Yacht, ca. 40 m²):**
- Standard Dacron: 2.400–3.200 EUR
- Premium Dacron: 3.000–4.000 EUR
- Performance Pentex: 4.200–5.800 EUR

**Lieferzeit:** 4–8 Wochen (Produktion in Thailand, Versand 2–3 Wochen)

**Stärken:** Günstiger Preis durch Produktion in Thailand, gute Qualität
für den Preis, umfangreiche Erfahrung mit Fahrtensegeln (gegründet 1947).

**Hinweise:**
- Import-Zoll (EU): ca. 6,5 % auf Segel aus Nicht-EU-Ländern
- Versandkosten: 150–400 EUR (je nach Segelgröße)
- Garantie: 3 Jahre (Standardmäßig), Reklamation kann aufwendiger sein

---

## 8. Fehlerbild-Atlas

### F-16_03-01: UV-Schutzstreifen-Versagen

**Schweregrad:** MITTEL bis HOCH (wenn Segeltuch betroffen)
**Häufigkeit:** Sehr häufig (häufigster Defekt bei Rollgenuas)

**Beschreibung:**
Der UV-Schutzstreifen (Sunbrella, Weblon) am Achterliek und/oder Unterliek
einer Rollgenua zeigt Degradation durch UV-Strahlung. Sichtbare Anzeichen
sind Verfärbung, Fadenbrüchigkeit, Rissbildung und Ablösung der Nähte.

**Ursachen:**
1. Natürliche UV-Alterung (Lebensdauer 8–15 Jahre je nach Revier)
2. Zu schmaler UV-Streifen (Segel nicht vollständig abgedeckt)
3. Minderwertiges UV-Schutz-Material
4. Segel dauerhaft ausgerollt (auch bei Nichtgebrauch)
5. Nähfaden-Degradation durch UV vor Stoffdegradation

**Visuelle Indikatoren (für AYDI Vision-Analyse):**
- Verfärbung: dunkle Farben werden blass, weiß wird gelblich
- Fadenmüdigkeit: einzelne Fäden stehen ab, fransiges Gewebe
- Nahtlösung: UV-Streifen löst sich vom Segel
- Rissbildung: Längsrisse entlang der Kettrichtung
- Durchsichtigkeit: Material wird transparent (fortgeschrittener Schaden)

**Konfidenz-Einschätzung:**
- Foto-Detailaufnahme (< 50 cm): visual_high
- Foto-Gesamtsegel (2–5 m): visual_medium
- Foto unter Segel/in Fahrt: visual_low

**Reparatur-Optionen:**
1. UV-Streifen erneuern (Segelmacher): 400–1.200 EUR (je nach Segelgröße)
2. UV-Streifen und angrenzende Bahnen erneuern: 800–2.000 EUR
3. UV-Schutz-Spray als Überbrückung (3M, Star Brite): 20–40 EUR/Dose
   (Haltbarkeit: 6–12 Monate, nur Notlösung)

**Präventive Maßnahmen:**
- Segel bei Nichtgebrauch immer vollständig einrollen
- UV-Streifen-Zustand jährlich prüfen (insbesondere Nähte)
- Rechtzeitig austauschen (bevor das darunterliegende Segeltuch geschädigt wird)
- Breitere UV-Streifen wählen als Mindestberechnung (+15–20 %)

### F-16_03-02: Vorliek-Bandablösung (Luff Tape Separation)

**Schweregrad:** HOCH (kann zu Segelverlust führen)
**Häufigkeit:** Mittel

**Beschreibung:**
Das Liektau (Vorliekband) löst sich vom Segeltuch. Dies kann am Kopf, am Hals
oder in der Mitte des Vorlieks auftreten.

**Ursachen:**
1. Alterung der Naht-/Klebeverbindung
2. Überlastung (zu viel Fall-Spannung bei Starkwind)
3. Mangelhafte Verarbeitung (zu wenig Nähte, falscher Faden)
4. UV-Degradation des Nahtfadens
5. Wiederholtes Knicken im Bereich der Liektau-Befestigung

**Visuelle Indikatoren:**
- Spalt zwischen Liektau und Segeltuch
- Aufstehende Nähte
- Faltenbildung parallel zum Vorliek (nicht durch Trimmfehler erklärbar)
- Liektau rutscht im Furler-Profil

**Sofortmaßnahme:**
- Segel bergen! Weiterfahren kann zu vollständiger Ablösung und
  Segelverlust führen.
- Provisorische Reparatur: Segeltape (Insignia) + Schäkel-Sicherung

**Reparatur:**
1. Liektau-Neunaht beim Segelmacher: 500–1.500 EUR
2. Vorliek-Erneuerung (neues Liektau + Naht): 800–2.500 EUR
3. Bei fortgeschrittenem Schaden: Neusegel erforderlich

### F-16_03-03: Achterliek-Drahtbruch (Leech Wire Break)

**Schweregrad:** MITTEL
**Häufigkeit:** Mittel

**Beschreibung:**
Der Achterliek-Draht (leech wire) oder die Achterliek-Leine bricht oder
löst sich. Das Achterliek flattert unkontrolliert (leech flutter),
was zu schnellem Verschleiß des Achterlieks führt.

**Ursachen:**
1. Materialermüdung durch Vibrationen (Flattern)
2. Korrosion (bei Stahldraht)
3. UV-Degradation (bei Textil-Achterliek-Leinen)
4. Beschädigung beim Bergen/Falten
5. Überlastung (Klemme blockiert, Draht wird bei Böe überlastet)

**Visuelle Indikatoren:**
- Dauerhaftes Achterliek-Flattern, auch bei korrektem Trimm
- Drahtende ragt aus dem Achterliek-Saum heraus
- Achterliek-Saum aufgeplatzt
- Wellenförmige Verformung des Achterlieks

**Reparatur:**
1. Achterliek-Leine/-Draht erneuern: 200–500 EUR beim Segelmacher
2. Achterliek-Saum reparieren und Draht ersetzen: 300–800 EUR
3. Provisorisch: Achterliek-Leine durch externen Block führen und
   mit Klemme sichern (nur Notlösung)

### F-16_03-04: Schothorn-Verschleiß (Clew Wear)

**Schweregrad:** MITTEL bis HOCH
**Häufigkeit:** Häufig

**Beschreibung:**
Das Schothorn (clew) ist der am stärksten belastete Punkt des Vorsegels.
Verschleiß zeigt sich in Form von Ausfransungen, Patch-Ablösung oder
Verformung der Kausch/Öse.

**Ursachen:**
1. Mechanische Belastung (Schotzug, 300–2.000 kg je nach Segel/Wind)
2. Schamfilen an der Reling, Wanten oder Salingen beim Wenden
3. UV-Degradation des Schothorn-Patches
4. Wiederholtes Anschlagen des Schothorns an Deck-Beschläge
5. Korrosion der Schothorn-Öse (bei Nicht-Edelstahl)

**Visuelle Indikatoren:**
- Abriebspuren am Schothorn-Patch
- Aufstehende oder gebrochene Nähte
- Verformung oder Rissbildung der Öse/Kausch
- Verfärbung (Rost) der Metalteile
- Ausdünnung des Segeltuchs um das Schothorn

**Reparatur:**
1. Schothorn-Patch erneuern: 300–800 EUR
2. Öse/Kausch austauschen: 100–300 EUR
3. Schothorn-Bereich komplett erneuern: 500–1.500 EUR

### F-16_03-05: Wanten-Schamfilen bei Überlappung (Shroud Chafe)

**Schweregrad:** MITTEL
**Häufigkeit:** Sehr häufig bei Genuas > 120 % LP

**Beschreibung:**
Bei Genuas mit Überlappung scheuert (schamfilt) das Segel bei Wenden an
den Wanten und Salingen. Dies erzeugt Abriebstellen, die das Segeltuch
schwächen und zu Rissen führen können.

**Ursachen:**
1. Konstruktionsbedingter Kontakt (große Genua + enge Wantenbasis)
2. Fehlende oder abgenutzte Schamfilschutze an Wanten/Salingen
3. Falscher Holepunkt (Segel zu dicht → mehr Kontakt)
4. Windverhältnisse (bei Starkwind mehr Druck → intensiverer Kontakt)

**Visuelle Indikatoren:**
- Glänzende Abriebstellen auf dem Segeltuch
- Kreisförmige Scheuerstellen (Wanten-Querschnitt)
- Längliche Scheuerstellen (Salingen-Kontakt)
- Verfärbung des Segeltuchs an Kontaktstellen
- Faserbrüche im Laminate (bei Laminatsegeln sichtbar)

**Reparatur:**
1. Scheuerschutz-Patches aufnähen: 150–400 EUR
2. Schamfil-geschädigte Bahnen ersetzen: 400–1.200 EUR
3. Wanten-Schamfilschutze (Leeder-Covers) installieren: 50–150 EUR/Stück

**Prävention:**
- Wanten-Überzüge (Leeder-Covers, Sailman TurtleSkin): 40–120 EUR/Stück
- Salingen-Schutzkappen: 20–50 EUR/Stück
- Korrekte Saling-Ausrichtung prüfen (Spitzen nach achtern gerichtet)
- Holepunkt weiter achtern setzen (offeneres Achterliek, weniger Kontakt)

### F-16_03-06: Ungleichmäßiges Rollen (Poor Furling)

**Schweregrad:** MITTEL
**Häufigkeit:** Häufig

**Beschreibung:**
Das Segel rollt sich nicht gleichmäßig auf die Furler-Trommel. Es bilden
sich Wulste, Falten oder das Segel „schlägt aus" (loose wrap).

**Ursachen:**
1. Defekte oder schwergängige Kugellager im Kopfwirbel oder der Trommel
2. Liektau-Durchmesser passt nicht zum Furler-Profil
3. Ungleichmäßige Schot-Spannung beim Einrollen
4. Fehlender oder beschädigter Luff-Pad (Schaumstoff-Streifen)
5. Verbogenes oder falsch montiertes Furler-Profil
6. Verformtes Vorstag (Korrosion, mechanischer Schaden)

**Visuelle Indikatoren:**
- Sichtbare Falten oder Wulste im aufgerollten Segel
- Segel steht an einzelnen Stellen ab
- Asymmetrische Wicklung (eine Seite dicker als andere)
- UV-Schutzstreifen nicht durchgängig sichtbar

**Reparatur:**
1. Furler-Service (Kugellager, Trommel): 200–600 EUR
2. Liektau-Anpassung: 150–400 EUR
3. Luff-Pad erneuern: 80–200 EUR
4. Furler-Profil richten oder ersetzen: 300–1.500 EUR

### F-16_03-07: Kopfbeschlag-Ausriss (Tack Thimble Pullout)

**Schweregrad:** HOCH bis KRITISCH
**Häufigkeit:** Selten, aber gefährlich

**Beschreibung:**
Der Halsbeschlag (Tack Fitting) oder die Hals-Kausch reißt aus dem
Segeltuch. Das Segel kann unkontrolliert flattern und sich vom
Furler lösen.

**Ursachen:**
1. Überlastung (Starkwind, Böen, blockierte Schot)
2. Materialermüdung der Nähte und Patches
3. Mangelhafte Verarbeitung (zu wenig Verstärkung)
4. Korrosion der Kausch oder des Schäkels
5. Falscher Anschlagwinkel der Schot (Kausch unter seitlicher Last)

**Visuelle Indikatoren:**
- Verformung des Halsbeschlags
- Aufstehende Nähte im Hals-Bereich
- Rissbildung im Segeltuch um die Kausch
- Korrosion sichtbar am Metall

**Sofortmaßnahme:**
- Segel sofort bergen!
- Provisorische Befestigung mit Textil-Schäkel oder Dyneema-Leine
  durch das nächsthöhere Stagreiterloch (nur Nottransfer zum Hafen)

**Reparatur:**
1. Hals-Patch und Kausch erneuern: 300–800 EUR
2. Hals-Bereich komplett erneuern (neuer Patch, neue Naht): 500–1.500 EUR
3. Bei strukturellem Schaden am Vorliek: Neusegel erforderlich

### F-16_03-08: Laminat-Delaminierung (Laminate Delamination)

**Schweregrad:** MITTEL bis HOCH
**Häufigkeit:** Häufig bei Laminatsegeln > 5 Jahre

**Beschreibung:**
Die Schichten eines Laminatsegels (Mylar-Folie, Fasern, Taffeta) lösen
sich voneinander. Sichtbar als Blasen, Falten oder milchige Verfärbung.

**Ursachen:**
1. UV-Degradation des Klebstoffs
2. Wiederholtes Knicken/Falten des Segels
3. Feuchtigkeitseintritt (besonders an Nähten und Kanten)
4. Hitzeeinwirkung (> 60 °C, z.B. in der Sonne auf Deck liegend)
5. Materialermüdung (natürliche Alterung)
6. Chemische Einwirkung (Reinigungsmittel, Diesel, Hydrauliköl)

**Visuelle Indikatoren:**
- Blasenbildung zwischen den Laminatschichten
- Milchige oder trübe Verfärbung (Klebstoff versagt)
- Knistergeräusche beim Biegen des Segels
- Wellenbildung im Segeltuch (Schichten bewegen sich unabhängig)
- Taffeta löst sich vom Laminatkern

**Konfidenz-Einschätzung (AYDI Vision):**
- Detailaufnahme mit Seitenlicht: visual_high
- Foto unter normalen Lichtverhältnissen: visual_medium
- Foto des gesetzten Segels: visual_low bis visual_insufficient

**Reparatur:**
1. Lokale Delaminierung: Patch-Reparatur mit speziellem Laminat-Kleber
   und Heißpresse. 200–600 EUR pro Stelle.
2. Großflächige Delaminierung: Bahnen-Ersatz. 500–2.000 EUR.
3. Fortgeschrittene Delaminierung: Neusegel (wirtschaftlicher als Reparatur)

### F-16_03-09: Selbstwendefock-Schienenblockade (Self-Tacking Track Jam)

**Schweregrad:** MITTEL (kann in kritischen Situationen HOCH sein)
**Häufigkeit:** Mittel

**Beschreibung:**
Der Schlitten (car/traveller) auf der Selbstwende-Schiene blockiert oder
bewegt sich schwergängig. Das Segel wendet nicht oder nur teilweise.

**Ursachen:**
1. Korrosion der Schiene (besonders bei Aluminium-Schienen)
2. Salzkristalle in der Schienennut
3. Verformte Schiene (mechanische Beschädigung, z.B. Treten)
4. Defekte Kugellager oder Rollen im Wagen
5. Falsche Schot-Führung (Schot verhakt sich)
6. Fremdkörper in der Schienennut (Blätter, Tau-Enden)

**Visuelle Indikatoren:**
- Sichtbare Korrosion auf der Schiene
- Schlitten steht schief auf der Schiene
- Schot liegt nicht sauber im Block
- Verformung der Schienenenden

**Reparatur:**
1. Reinigung und Schmierung: 50–100 EUR (Eigenleistung möglich)
2. Schlittenaustausch: 200–500 EUR
3. Schienenaustausch: 500–1.500 EUR (inkl. Montage)
4. Kugellager-Service: 100–300 EUR

**Prävention:**
- Monatlich: Schiene mit Süßwasser spülen
- Vierteljährlich: Schlitten-Lauf prüfen, ggf. Teflon-Spray
- Jährlich: Schiene demontieren, reinigen, auf Korrosion prüfen
- Nach jeder Saison: Schlitten-Lager prüfen und fetten

### F-16_03-10: Code-0-Torsionsseil-Versagen (Code 0 Torque Rope Failure)

**Schweregrad:** HOCH
**Häufigkeit:** Mittel (bei älteren Systemen häufiger)

**Beschreibung:**
Das Torsionsseil (torque rope/anti-torsion cable) des Code 0 Top-Down-Furlers
versagt. Das Segel lässt sich nicht mehr einrollen oder bildet beim
Einrollen ein Stundenglas.

**Ursachen:**
1. UV-Degradation des Torque-Seils (Mantel und/oder Kern)
2. Mechanischer Verschleiß (Reibung am Vorliek oder Furler-Beschlägen)
3. Falsche Torsionsseil-Länge (zu lang = nicht genug Drehmoment,
   zu kurz = Überlastung)
4. Korrosion der Seilenden-Beschläge (Pressungen, Kauschen)
5. Alterung (Creep bei Dyneema-Kern)
6. Beschädigung durch Einklemmen

**Visuelle Indikatoren:**
- Sichtbare Beschädigung des Torsionsseil-Mantels
- Aufgedrehte oder verformte Abschnitte
- Segel lässt sich nur schwer oder gar nicht einrollen
- Stundenglas-Bildung beim Einrollen (oberes und unteres Drittel rollt,
  Mitte nicht)

**Sofortmaßnahme:**
- Segel über Lee-Schot-Fieren und Halsen bergen
- NICHT weiter versuchen, einzurollen (Gefahr der Verschlimmierung)
- Ggf. Segel per Bergesock oder manuelles Einwickeln sichern

**Reparatur:**
1. Torsionsseil-Austausch: 300–800 EUR (Material) + 200–500 EUR (Arbeit)
2. Furler-Komplett-Service: 500–1.500 EUR
3. Bei Beschlagschaden: Furler-Kopf/Trommel ersetzen: 800–2.500 EUR

### F-16_03-11: Sturmfock-Befestigungsversagen (Storm Jib Attachment Failure)

**Schweregrad:** KRITISCH (lebensbedrohliche Situation bei Sturm)
**Häufigkeit:** Selten (aber Konsequenzen schwerwiegend)

**Beschreibung:**
Die Befestigung der Sturmfock am Sturmstag oder am Vorstag versagt.
Dies kann Stagreiter-Bruch, Schäkel-Versagen, Stag-Befestigungs-Bruch
oder Hals-/Kopf-Ausriss umfassen.

**Ursachen:**
1. Korrosion der Stagreiter oder Schäkel (fehlende regelmäßige Inspektion)
2. Falsche Dimensionierung (zu schwache Beschläge)
3. Ungeeignetes Material (Edelstahl 304 statt 316L)
4. Sturmstag nicht korrekt gespannt oder befestigt
5. Mangelhafte Nähte/Verstärkungen am Segel (Hals, Kopf)
6. Fehlende Probe-Montage (Sturmfock wurde nie probeweise gesetzt)

**Visuelle Indikatoren:**
- Korrosion an Stegreitern oder Schäkeln (Rost, Lochfraß)
- Risse in Kunststoff-Teilen der Befestigung
- Verformung der Stag-Endverbindungen
- Spiel in der Stag-Befestigung (Wackeln, Klappern)

**Sofortmaßnahmen (auf See):**
- Alternative Befestigung vorbereiten (Dyneema-Leine, Textil-Schäkel)
- Sturmfock ggf. direkt am Vorstag mit Textil-Befestigungen sichern
- Unter Motor/Bare Poles weitermachen bis zur sicheren Befestigung

**Reparatur/Prävention:**
1. Alle Beschläge ersetzen: 100–400 EUR
2. Sturmstag erneuern: 300–1.000 EUR
3. Halbjährliche Inspektion ALLER Sturmfock-Beschläge (Checkliste erstellen)
4. Probe-Montage vor jeder Saison (mindestens 1× im Hafen setzen)

### F-16_03-12: Nähte-Versagen bei Starkwind (Headsail Stitch Failure)

**Schweregrad:** HOCH bis KRITISCH
**Häufigkeit:** Mittel (steigt exponentiell mit Segelalter)

**Beschreibung:**
Nähte im Vorsegel versagen unter Last. Dies kann Bahn-zu-Bahn-Nähte,
Patch-Nähte, Liektau-Nähte oder UV-Streifen-Nähte betreffen.

**Ursachen:**
1. UV-Degradation des Nähfadens (häufigste Ursache!)
2. Mechanische Überlastung (Böen, blockierte Schot)
3. Scheuerverschleiß (Naht an Wanten, Salingen)
4. Materialermüdung (wiederholtes Dehnen/Entspannen)
5. Falscher Nähfaden (nicht UV-stabilisiert, zu dünn)
6. Mangelhafte Verarbeitung (Fadenzug zu locker, zu wenig Stiche/cm)

**Visuelle Indikatoren:**
- Aufstehende Nahtfäden
- Sichtbarer Spalt zwischen Bahnen
- Nahtlinie verfärbt (UV-degradierter Faden wird bräunlich/rötlich)
- Segeltuch wölbt sich entlang der Nahtlinie
- Bei Gegenlicht: Nadellöcher sichtbar (Fäden bereits gebrochen)

**Konfidenz-Einschätzung (AYDI Vision):**
- Detailaufnahme Naht (< 30 cm): visual_high
- Gesamtsegel-Foto mit sichtbarem Nahtproblem: visual_medium
- Foto gesetztes Segel mit sichtbarem Riss: visual_high (Riss) / visual_low (Ursache)

**Reparatur:**
1. Einzelne Naht erneuern: 100–400 EUR/lfm
2. Patch + Naht erneuern: 200–800 EUR pro Stelle
3. Mehrere Bahnen-Nähte erneuern: 500–2.000 EUR
4. Komplettes Segel nachnähen (Overhaul): 1.000–3.000 EUR

**Prävention:**
- Jährliche Nahtinspektion (besonders UV-exponierte Nähte)
- Nähfaden-Test: Faden zwischen Daumen und Zeigefinger reiben.
  Wenn Fäden abbrechen → Naht-Erneuerung fällig
- UV-Schutzstreifen schützt auch die darunterliegenden Nähte

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Ungleichmäßiges Rollen

```
Problem: Vorsegel rollt ungleichmäßig auf den Furler

├── Rollt das Segel überhaupt?
│   ├── NEIN
│   │   ├── Furler-Trommel blockiert?
│   │   │   ├── JA → Trommel-Kugellager defekt oder Fremdkörper in Trommel
│   │   │   │       → Aktion: Trommel demontieren, reinigen, Lager prüfen/tauschen
│   │   │   └── NEIN → Kopfwirbel blockiert?
│   │   │       ├── JA → Kopfwirbel-Lager defekt
│   │   │       │       → Aktion: Kopfwirbel-Service, Lager tauschen
│   │   │       └── NEIN → Furler-Leine verhakt oder zu kurz?
│   │   │           → Aktion: Leinenführung prüfen, Länge kontrollieren
│   │   │
│   └── JA, aber ungleichmäßig
│       ├── Wulst im oberen Drittel?
│       │   ├── JA → Zu viel Fall-Spannung ODER Liektau zu dünn für Profil oben
│       │   │       → Aktion: Fall etwas fieren, Liektau-Durchmesser prüfen
│       │   └── NEIN
│       ├── Wulst im unteren Drittel?
│       │   ├── JA → Fehlender Luff-Pad ODER Schot-Spannung beim Rollen ungleichmäßig
│       │   │       → Aktion: Luff-Pad installieren, Schot kontrolliert fieren
│       │   └── NEIN
│       ├── Segel schlägt auf einer Seite aus?
│       │   ├── JA → Wind-Einfluss ODER Profil-Verbinder locker
│       │   │       → Aktion: Bei wenig Wind rollen, Profilverbinder prüfen
│       │   └── NEIN
│       └── Segel rollt sich schief (Torsion)?
│           ├── JA → Kopfwirbel oder Trommel nicht fluchtend montiert
│           │       → Aktion: Furler-Ausrichtung prüfen (Vorstag-Spannung)
│           └── NEIN → Allgemeiner Verschleiß → Furler-Komplett-Service
```

### 9.2 Entscheidungsbaum: Zu viel Bauch (Belly) im Vorsegel

```
Problem: Vorsegel hat zu viel Profiltiefe (Bauch)

├── Tritt das Problem bei allen Windstärken auf?
│   ├── JA → Permanente Segelverformung
│   │   ├── Dacron-Segel > 5 Jahre?
│   │   │   ├── JA → Natürliche Tuchermüdung. Profil ist dauerhaft verformt.
│   │   │   │       → Aktion: Segel vom Segelmacher nachmessen lassen.
│   │   │   │         Ggf. nachschneiden (re-cut) oder Neusegel.
│   │   │   └── NEIN → Herstellungsfehler oder falscher Schnitt
│   │   │       → Aktion: Reklamation beim Segelmacher/Hersteller
│   │   └── Laminat-Segel?
│   │       ├── Delaminierung vorhanden?
│   │       │   ├── JA → Laminat versagt, Fasern tragen nicht mehr
│   │       │   │       → Aktion: Reparatur oder Neusegel
│   │       │   └── NEIN → Falsche Faser-Orientierung oder -Menge
│   │       │       → Aktion: Hersteller kontaktieren
│   │
│   └── NEIN → Trimm-Problem oder Vorstag-Durchhang
│       ├── Vorstag durchgehangen?
│       │   ├── JA → Zu wenig Achterstag-/Backstag-Spannung
│       │   │       → Aktion: Achterstag dichter, Wantentrimm prüfen
│       │   └── NEIN
│       ├── Fall-Spannung zu gering?
│       │   ├── JA → Profil wandert nach achtern → mehr Bauch
│       │   │       → Aktion: Fall durchsetzen, Cunningham nutzen
│       │   └── NEIN
│       ├── Holepunkt zu weit vorn?
│       │   ├── JA → Achterliek zu dicht → Profil zu tief
│       │   │       → Aktion: Holepunkt nach achtern versetzen
│       │   └── NEIN
│       └── Schot zu dicht?
│           ├── JA → Gesamtes Segel zu tief getrimmt
│           │       → Aktion: Schot fieren, Trimmfäden beobachten
│           └── NEIN → Weitere Diagnose durch Segelmacher empfohlen
```

### 9.3 Entscheidungsbaum: Achterliek-Flattern (Leech Flutter)

```
Problem: Achterliek flattert unkontrolliert

├── Achterliek-Draht/-Leine intakt?
│   ├── NEIN → Draht/Leine gebrochen (siehe F-16_03-03)
│   │   → Aktion: Achterliek-Draht/-Leine erneuern lassen
│   └── JA
│       ├── Achterliek-Leine korrekt gespannt?
│       │   ├── NEIN → Leine zu locker oder Klemme defekt
│       │   │   → Aktion: Leine nachspannen (nicht zu viel — Haken vermeiden!)
│       │   └── JA
│       ├── Holepunkt-Position korrekt?
│       │   ├── NEIN → Holepunkt zu weit achtern → oberes Achterliek offen
│       │   │   → Aktion: Holepunkt nach vorn versetzen
│       │   └── JA
│       ├── Segel-Material ermüdet?
│       │   ├── JA → Segeltuch in der Achterliek-Zone ausgedehnt
│       │   │   → Aktion: Achterliek nachschneiden lassen (Segelmacher)
│       │   └── NEIN
│       └── Windverhältnisse? (wechselhaft, böig)
│           ├── JA → Natürliches Flattern bei unstetigem Wind
│           │   → Aktion: Normal, Achterliek-Leine leicht anziehen
│           └── NEIN → Segelschnitt prüfen lassen (Segelmacher)
```

### 9.4 Entscheidungsbaum: Selbstwendefock wendet nicht sauber

```
Problem: Selbstwendefock wendet nicht oder nur teilweise

├── Blockiert der Schlitten auf der Schiene?
│   ├── JA → Siehe F-16_03-09 (Schienenblockade)
│   └── NEIN
│       ├── Wendet das Segel auf eine Seite, aber nicht auf die andere?
│       │   ├── JA → Asymmetrisches Problem
│       │   │   ├── Schiene verbogen oder asymmetrisch montiert?
│       │   │   │   → Aktion: Schienen-Ausrichtung prüfen (Wasserwaage, Schnur)
│       │   │   ├── Schot-Länge ungleich?
│       │   │   │   → Aktion: Schot-Länge auf beiden Seiten abmessen
│       │   │   └── Block oder Beschlag auf einer Seite beschädigt?
│       │   │       → Aktion: Alle Beschläge auf beiden Seiten vergleichen
│       │   └── NEIN → Segel wendet auf keiner Seite
│       │       ├── Schot zu lang?
│       │       │   ├── JA → Segel flattet durch, bevor Schot Zug aufnimmt
│       │       │   │   → Aktion: Schot kürzen oder Stopper anpassen
│       │       │   └── NEIN
│       │       ├── Schienen-Anschlag zu eng?
│       │       │   ├── JA → Schlitten erreicht nicht die neue Seite
│       │       │   │   → Aktion: Anschlag-Position vergrößern
│       │       │   └── NEIN
│       │       ├── Fockbaum (falls vorhanden) klemmt?
│       │       │   ├── JA → Fockbaum-Gelenk reinigen, schmieren
│       │       │   │   → Aktion: Fockbaum-Beschläge warten
│       │       │   └── NEIN
│       │       └── Wendegeschwindigkeit zu langsam?
│       │           → Aktion: Schnellere Wende fahren (mehr Schwung)
│       │             oder Segelschnitt prüfen (zu schwerer Stoff?)
```

### 9.5 Entscheidungsbaum: Code 0 Stundenglas-Bildung (Hourglassing)

```
Problem: Code 0 bildet beim Einrollen ein Stundenglas

├── Tritt das Problem beim Einrollen auf?
│   ├── JA
│   │   ├── Torque-Seil korrekt vorgespannt?
│   │   │   ├── NEIN → Zu wenig Vorspannung → nicht genug Drehmoment
│   │   │   │   → Aktion: Torque-Seil nachspannen (Hersteller-Vorgabe beachten)
│   │   │   └── JA
│   │   ├── Schot unter Spannung während des Einrollens?
│   │   │   ├── JA → Zu viel Schot-Spannung verhindert gleichmäßiges Rollen
│   │   │   │   → Aktion: Schot kontrolliert fieren, nur leichten Zug belassen
│   │   │   └── NEIN
│   │   ├── Wind im Segel während des Einrollens?
│   │   │   ├── JA → Segel steht unter Druck → ungleichmäßiges Rollen
│   │   │   │   → Aktion: Kurs ändern (Vorwind, Segel im Lee des Großsegels),
│   │   │   │     DANN einrollen
│   │   │   └── NEIN
│   │   ├── Torque-Seil beschädigt?
│   │   │   ├── JA → Siehe F-16_03-10 (Torque Rope Failure)
│   │   │   └── NEIN
│   │   └── Furler-Trommel schwergängig?
│   │       ├── JA → Lager-Problem → Service erforderlich
│   │       └── NEIN → Segelschnitt ggf. nicht optimal für Furler →
│   │                  Hersteller/Segelmacher konsultieren
│   │
│   └── NEIN → Stundenglas liegt vor (bereits entstanden)
│       └── SOFORTMASSNAHME:
│           1. NICHT weiter rollen!
│           2. Schot vollständig lösen
│           3. Segel komplett ausrollen lassen (ggf. Fall fieren)
│           4. Stundenglas löst sich durch Flattern
│           5. Erneuter Einroll-Versuch mit korrekter Technik
│           6. Falls nicht lösbar: Segel bergen (Fall lösen) und
│              manuell einwickeln (2 Personen)
```

---

## 10. Vorsegel-Garderobe

### 10.1 Garderobe-Empfehlungen nach Seglerprofil

**Profil A: Wochenendsegler, Binnenrevier (See, Fluss)**
| Segel | Empfehlung | Material | Budget (38 ft) |
|---|---|---|---|
| Rollgenua (130 %) | Pflicht | Dacron | 3.500–5.000 EUR |
| Sturmfock | Optional (nicht CE-pflichtig Kat. C/D) | Dacron | 800–1.500 EUR |
| **Gesamt** | | | **4.300–6.500 EUR** |

**Profil B: Aktiver Küstensegler, Ostsee/Nordsee**
| Segel | Empfehlung | Material | Budget (38 ft) |
|---|---|---|---|
| Rollgenua (135 %) | Pflicht | Dacron Premium/Pentex | 4.000–6.500 EUR |
| Sturmfock | Pflicht (CE Kat. A/B) | Dacron schwer | 1.200–2.000 EUR |
| Code 0 | Empfohlen | Laminat | 3.500–6.000 EUR |
| **Gesamt** | | | **8.700–14.500 EUR** |

**Profil C: Langfahrtsegler, Blauwasser**
| Segel | Empfehlung | Material | Budget (38 ft) |
|---|---|---|---|
| Rollgenua (130 %) | Pflicht | Dacron Premium | 4.500–7.000 EUR |
| Staysail (Kutterstag) | Dringend empfohlen | Dacron schwer | 2.000–3.500 EUR |
| Sturmfock | Pflicht | Dacron schwer, orange | 1.500–2.500 EUR |
| Gennaker/Code 0 | Empfohlen | Nylon/Laminat | 3.000–6.000 EUR |
| Ersatz-Genua (leicht, faltbar) | Empfohlen | Dacron | 3.000–4.500 EUR |
| **Gesamt** | | | **14.000–23.500 EUR** |

**Profil D: Regattasegler**
| Segel | Empfehlung | Material | Budget (38 ft) |
|---|---|---|---|
| Genua 1 (150 %) | Pflicht | Laminat/3Di | 6.000–15.000 EUR |
| Genua 2 (130 %) | Pflicht | Laminat/3Di | 5.500–12.000 EUR |
| Genua 3 (115 %) | Empfohlen | Laminat | 4.500–10.000 EUR |
| Fock (100 %) | Empfohlen | Laminat | 3.500–8.000 EUR |
| Sturmfock | Pflicht (ORC/IRC) | Dacron schwer | 1.500–2.500 EUR |
| Code 0 | Pflicht | Laminat | 5.000–10.000 EUR |
| Gennaker | Pflicht | Nylon | 3.000–6.000 EUR |
| **Gesamt** | | | **29.000–63.500 EUR** |

### 10.2 Garderobe nach Bootsklasse

**Fahrtensegelyacht 8–10 m (26–33 ft):**
- Minimum: 1 Rollgenua + 1 Sturmfock = 3.000–5.000 EUR
- Empfohlen: + Code 0 = 5.500–9.000 EUR
- Optimal: + Staysail = 7.000–12.000 EUR

**Fahrtensegelyacht 10–13 m (33–43 ft):**
- Minimum: 1 Rollgenua + 1 Sturmfock = 5.000–8.000 EUR
- Empfohlen: + Code 0 + Staysail = 10.000–18.000 EUR
- Optimal: + Ersatz-Genua = 13.000–22.000 EUR

**Fahrtensegelyacht 13–16 m (43–52 ft):**
- Minimum: 1 Rollgenua + 1 Sturmfock = 7.000–12.000 EUR
- Empfohlen: + Code 0 + Staysail = 15.000–25.000 EUR
- Optimal: + Ersatz-Genua + Gennaker = 22.000–38.000 EUR

**Fahrtensegelyacht 16–20 m (52–65 ft):**
- Minimum: 1 Rollgenua + 1 Sturmfock = 10.000–18.000 EUR
- Empfohlen: + Code 0 + Staysail = 22.000–38.000 EUR
- Optimal: + Ersatz-Genua + Gennaker + Yankee = 35.000–60.000 EUR

---

## 11. Kosten

### 11.1 Neusegel-Preise (Dacron, Cross-Cut)

| Bootsgröße | Genua 2 (130 %) | Fock (100 %) | Sturmfock | Code 0 |
|---|---|---|---|---|
| 8 m (26 ft) | 1.800–2.800 EUR | 1.200–2.000 EUR | 600–1.000 EUR | 2.000–3.500 EUR |
| 10 m (33 ft) | 2.500–3.800 EUR | 1.800–2.800 EUR | 800–1.400 EUR | 2.800–4.500 EUR |
| 12 m (40 ft) | 3.500–5.500 EUR | 2.500–4.000 EUR | 1.200–2.000 EUR | 3.800–6.000 EUR |
| 14 m (46 ft) | 5.000–7.500 EUR | 3.500–5.500 EUR | 1.500–2.500 EUR | 5.000–8.000 EUR |
| 16 m (52 ft) | 7.000–10.000 EUR | 5.000–7.500 EUR | 2.000–3.500 EUR | 7.000–11.000 EUR |
| 18 m (59 ft) | 9.000–14.000 EUR | 6.500–10.000 EUR | 2.500–4.000 EUR | 9.000–15.000 EUR |
| 20 m (65 ft) | 12.000–18.000 EUR | 8.000–13.000 EUR | 3.000–5.000 EUR | 12.000–20.000 EUR |

### 11.2 Material-Aufpreise (vs. Dacron Cross-Cut)

| Material / Schnitt | Aufpreis |
|---|---|
| Dacron Radial / Tri-Radial | +15–30 % |
| Pentex Cross-Cut | +30–50 % |
| Pentex Radial | +50–80 % |
| Technora-Laminat | +80–150 % |
| Dyneema-Laminat | +100–180 % |
| Vectran-Laminat | +80–140 % |
| Carbon-Laminat | +150–300 % |
| 3Di Nordac | +80–120 % |
| 3Di Endurance | +120–180 % |
| 3Di 780 | +200–280 % |
| Stratis ICE | +120–180 % |
| Stratis GTX | +180–280 % |
| EPEX Cruising | +60–100 % |
| DCF / Cuben Fiber | +200–400 % |

### 11.3 Reparaturkosten

| Reparatur | Preisbereich |
|---|---|
| UV-Streifen erneuern (Achterliek) | 400–1.200 EUR |
| UV-Streifen erneuern (Achterliek + Unterliek) | 700–2.000 EUR |
| Naht erneuern (einzelne Bahn, bis 3 m) | 100–400 EUR |
| Naht erneuern (Komplett-Overhaul) | 1.000–3.000 EUR |
| Liektau-Erneuerung | 500–1.500 EUR |
| Achterliek-Draht ersetzen | 200–500 EUR |
| Schothorn-Patch erneuern | 300–800 EUR |
| Hals-/Kopfpatch erneuern | 300–800 EUR |
| Riss-Reparatur (klein, < 30 cm) | 100–300 EUR |
| Riss-Reparatur (groß, > 30 cm) | 300–1.000 EUR |
| Bahnen-Ersatz (einzelne Bahn) | 300–800 EUR |
| Laminat-Delaminierungs-Reparatur (lokal) | 200–600 EUR |
| Segel-Reinigung (professionell) | 150–400 EUR |
| Segel-Vermessung (komplett) | 100–250 EUR |
| Kauschen/Ösen erneuern (pro Stück) | 30–80 EUR |
| Stagreiter ersetzen (komplett) | 100–300 EUR |

### 11.4 Wartungskosten (jährlich)

| Maßnahme | Kosten | Empfehlung |
|---|---|---|
| Segel-Inspektion (Segelmacher) | 100–250 EUR | Jährlich |
| Furler-Service (Kugellager, Schmierung) | 200–500 EUR | Alle 2–3 Jahre |
| Furler-Lager-Austausch | 300–800 EUR | Alle 5–7 Jahre |
| Schot-Erneuerung | 100–400 EUR | Alle 3–5 Jahre |
| Trimmfäden ersetzen | 20–50 EUR | Jährlich |
| Segel-Reinigung (DIY) | 20–50 EUR | 1–2× pro Saison |
| Segel-Imprägnierung | 50–150 EUR | Alle 3–5 Jahre |

### 11.5 Lifecycle-Kosten (10-Jahres-Betrachtung, 38 ft)

| Szenario | Anschaffung | Wartung (10 J.) | Reparaturen | Ersatz | Gesamt (10 J.) |
|---|---|---|---|---|---|
| Budget (1 Dacron-Rollgenua) | 3.800 EUR | 2.500 EUR | 1.500 EUR | 3.800 EUR | 11.600 EUR |
| Standard (Dacron Genua + Sturmfock) | 5.500 EUR | 3.500 EUR | 2.000 EUR | 4.000 EUR | 15.000 EUR |
| Performance (Pentex + Code 0 + Sturmfock) | 12.000 EUR | 5.000 EUR | 3.000 EUR | 8.000 EUR | 28.000 EUR |
| Premium (3Di + Code 0 + Staysail + Sturmfock) | 22.000 EUR | 6.000 EUR | 3.500 EUR | 12.000 EUR | 43.500 EUR |
| Regatta (volle Garderobe, Laminat) | 40.000 EUR | 8.000 EUR | 5.000 EUR | 25.000 EUR | 78.000 EUR |

---

## 12. FAQ

### Allgemeine Fragen

**F1: Was ist der Unterschied zwischen einer Fock und einer Genua?**
Eine Fock hat ein LP/J-Verhältnis von ≤ 100 % (keine Überlappung mit dem Großsegel-Dreieck).
Eine Genua hat ein LP/J-Verhältnis von > 100 % (Überlappung). LP ist die kürzeste Distanz
vom Schothorn zum Vorliek, J ist die Distanz vom Vorstag-Fußpunkt zum Mast auf Deckshöhe.
Je größer die Überlappung, desto mehr Segelfläche, aber auch desto schwieriger die Handhabung
bei Wenden und bei zunehmendem Wind.

**F2: Brauche ich eine Sturmfock?**
Für CE-Kategorie A (Hochsee) und B (Küstengewässer) ist eine Sturmfock vorgeschrieben
(World Sailing OSR). Für Kategorie C und D ist sie empfohlen, aber nicht zwingend. Für jede
Blauwasser-Reise ist sie unverzichtbar. Die Sturmfock muss unabhängig von der Rollreffanlage
gesetzt werden können — eine teileingerollte Rollgenua ist KEIN Ersatz für eine Sturmfock.

**F3: Wie lange hält ein Dacron-Vorsegel?**
Bei durchschnittlicher Nutzung (500–1.000 sm/Jahr, korrekte Pflege, UV-Schutz) hält ein
Premium-Dacron-Vorsegel 6–10 Jahre. Standard-Dacron: 4–6 Jahre. Entscheidende Faktoren:
UV-Exposition (Mittelmeer vs. Nordeuropa), Windstärken, Pflegedisziplin. Ein Segel, das
dauerhaft ausgerollt am Vorstag steht, altert 2–3× schneller als ein geschütztes Segel.

**F4: Rollgenua oder Wechselsegel — was ist besser?**
Rollgenuas sind komfortabler und schneller zu bedienen. Wechselsegel (mehrere Segel,
die bei Bedarf gewechselt werden) bieten ein optimales Profil für jeden Windbereich.
Für Fahrtensegler ist die Rollgenua der Standard. Für Regattasegler und Langfahrtsegler
ist eine Kombination aus Rollgenua und zusätzlichen Wechselsegeln (Staysail, Sturmfock)
optimal.

**F5: Was kostet ein Vorsegel für meine Yacht?**
Richtwert für ein Dacron-Vorsegel (Cross-Cut, 130 % Genua): ca. 80–120 EUR pro m²
Segelfläche. Für eine 38-Fuß-Yacht (ca. 40 m² Genua-Fläche): 3.500–5.000 EUR (Dacron).
Laminat-Segel: +50–300 % Aufschlag. 3Di/Stratis: +100–500 % Aufschlag.

**F6: Kann ich mein Vorsegel waschen?**
Ja, aber nur mit Süßwasser und mildem Segelreiniger. KEINE Bleichmittel, keine
Waschmaschine, keinen Hochdruckreiniger. Segel flach auslegen, einweichen, mit
weicher Bürste schrubben, gründlich spülen, vollständig trocknen lassen. Professionelle
Reinigung beim Segelmacher: 150–400 EUR.

**F7: Was sind Trimmfäden und wie lese ich sie?**
Trimmfäden (Telltales) sind kurze Wollfäden oder Bänder, die am Vorliek des
Vorsegels angebracht sind (typisch: 3 Paare auf Luv- und Leeseite bei 25 %, 50 %
und 75 % der Vorliekhöhe). Sie zeigen die Strömung am Segel an:
- Beide strömen: korrekt getrimmt
- Luv-Faden steht/flattert: zu offen (untergetrimmt) → dichter holen oder abfallen
- Lee-Faden fällt/wirbelt: zu dicht (übertrimmt) → fieren oder anluven

**F8: Was ist ein Code 0 und brauche ich einen?**
Ein Code 0 (auch Screecher) ist ein großes, flaches Leichtwind-Vorsegel, das auf
einem Top-Down-Furler gefahren wird. Es schließt die Lücke zwischen Genua und
Gennaker (TWA 55–120°, TWS 4–16 kn). Für aktive Segler, die in Leichtwind-Revieren
segeln, ist ein Code 0 eine ausgezeichnete Ergänzung. Kosten: Segel 3.000–8.000 EUR
+ Furler 2.400–5.500 EUR.

### Material-Fragen

**F9: Dacron oder Laminat — was ist für Fahrtensegler besser?**
Für die meisten Fahrtensegler ist Dacron die bessere Wahl: langlebiger, reparaturfreundlicher,
UV-beständiger, günstiger. Laminat lohnt sich für Segler, die regelmäßig segeln (> 1.500 sm/Jahr),
Performance schätzen und bereit sind, das Segel sorgfältig zu behandeln (kein Knicken, UV-Schutz).

**F10: Was ist 3Di und lohnt sich das für Fahrtensegler?**
3Di ist North Sails' proprietäres Membransegel-System. Für Fahrtensegler gibt es die
Variante 3Di Nordac (Polyester-basiert) und 3Di Endurance (Dyneema-basiert). Diese
bieten bessere Formstabilität als Dacron bei vergleichbarer Haltbarkeit. Preis: +80–180 %
vs. Dacron. Lohnt sich für ambitionierte Fahrtensegler ab 12 m Bootslänge.

**F11: Ist Pentex ein guter Kompromiss zwischen Dacron und Laminat?**
Ja. Pentex (High-Modulus-Polyester) bietet ca. 50 % weniger Dehnung als Standard-Dacron
bei vergleichbarer UV-Beständigkeit und Haltbarkeit. Preis: +30–50 % vs. Dacron. Ideal
für Fahrtensegler, die etwas mehr Performance wollen, ohne auf Laminat umzusteigen.

**F12: Wie erkenne ich, ob mein Laminatsegel delaminiert?**
Anzeichen: Blasenbildung, milchige Verfärbung, Knistergeräusche beim Biegen, sichtbare
Trennung der Schichten. Test: Segel gegen Licht halten — bei Delaminierung sind die
Schichten als separate Lagen erkennbar. Im Frühstadium: Segelmacher konsultieren.
Fortgeschrittene Delaminierung: Neusegel wahrscheinlich wirtschaftlicher.

### Furler-Fragen

**F13: Wie oft muss ich meine Rollreffanlage warten?**
Jährlich: Süßwasser-Spülung, Sichtprüfung. Alle 2–3 Jahre: Professioneller Service
(Kugellager prüfen, schmieren). Alle 5–7 Jahre: Kugellager-Austausch. Bei Schwergängigkeit
oder Geräuschen: sofortiger Service. Kosten: 200–800 EUR pro Service.

**F14: Welcher Furler passt zu meiner Yacht?**
Die Furler-Größe richtet sich nach: Vorstag-Durchmesser, maximaler Segelfläche und
Bootslänge. Siehe Kompatibilitätsmatrix in Abschnitt 4.6. Bei Unsicherheit: Hersteller-
Beratung oder Rigger konsultieren. Falsche Dimensionierung führt zu Schwergängigkeit,
Verschleiß und im schlimmsten Fall zu Versagen.

**F15: Kann ich meine Rollgenua bei Starkwind eingerollt lassen?**
Nein — nicht vollständig. Eine teileingerollte Rollgenua hat ein schlechtes Profil und
belastet den Furler und das Rigg ungleichmäßig. Bei Starkwind (> 25 kn): Genua vollständig
einrollen und ggf. Sturmfock oder Staysail setzen. Eine dauerhaft halb eingerollte
Genua ist eine der häufigsten Ursachen für Furler-Versagen.

### Trimm-Fragen

**F16: Wie finde ich den richtigen Holepunkt?**
Ausgangspunkt: Die imaginäre Verlängerung der Schot vom Schothorn zum Holepunkt sollte
die Mitte des Vorlieks treffen. Dann Trimmfäden beobachten: Wenn obere und untere
Trimmfäden gleichzeitig reagieren (beim Anluven zuerst Luv-Fäden kippen), ist der
Holepunkt korrekt. Obere kippen zuerst → Holepunkt zu weit vorn. Untere kippen zuerst
→ Holepunkt zu weit achtern.

**F17: Was tun, wenn die Genua bei Wenden an den Wanten hängenbleibt?**
1. Schot rechtzeitig lösen (Winsch-Griff bereithalten)
2. Holepunkt etwas weiter achtern setzen (offeneres Achterliek)
3. Salingen-Schutzkappen und Wantenüberzüge installieren
4. Bei häufigem Problem: kleineres Vorsegel (weniger Überlappung) erwägen
5. Ggf. Barber-Hauler installieren für variablere Schot-Führung

**F18: Mein Segel hat einen „Haken" im Achterliek — was tun?**
Ein Haken (hook) im Achterliek bedeutet, dass die Luft an der Hinterkante des Segels
nach Luv umgelenkt wird. Ursachen: Achterliek-Leine zu straff, Holepunkt zu weit vorn,
oder Schot zu dicht. Lösung: Achterliek-Leine lösen, Holepunkt achterlicher, Schot fieren.
Bei permanentem Haken: Segelmacher konsultieren (Achterliek nachschneiden).

**F19: Wie stelle ich das Vorstag korrekt ein?**
Vorstag-Spannung wird primär über das Achterstag (Masttop-Rigg) oder Backstag
(Fraktional-Rigg) kontrolliert. Bei mehr Wind: mehr Achterstag-Spannung = strafferes
Vorstag = flacheres Segel. Die Faustregel: Das Vorstag sollte bei Amwind-Kurs und
normalem Wind keinen sichtbaren Durchhang von mehr als 1–2 % der Länge haben.

### Pflege-Fragen

**F20: Wie lagere ich mein Vorsegel über den Winter?**
1. Gründlich mit Süßwasser spülen (Salz entfernen)
2. Vollständig trocknen (nicht feucht einlagern → Schimmel!)
3. Locker rollen (nicht falten — Knickbrüche vermeiden)
4. In trockenem, belüftetem Raum lagern (kein feuchter Keller)
5. Nicht in direktem Sonnenlicht lagern (UV-Schutz)
6. Segel-Tasche verwenden (atmungsaktiv, nicht luftdicht)
7. Motten- und Nagetierschutz bedenken

**F21: Kann ich einen UV-Schutzstreifen selbst erneuern?**
Theoretisch ja, aber es erfordert eine industrielle Nähmaschine mit Zickzack-Funktion
und Erfahrung im Segelnähen. Für Hobby-Segler nicht empfohlen — die Nähte müssen
erhebliche Lasten aushalten. Empfehlung: Segelmacher beauftragen (400–1.200 EUR).
DIY-Preis (Material): 100–200 EUR.

**F22: Wie entferne ich Schimmel vom Segel?**
1. Segel trocken auslegen
2. Schimmel mit weicher Bürste abbürsten (Atemschutz tragen!)
3. Lösung aus 1 Teil weißem Essig + 3 Teilen Wasser aufsprühen
4. 30 Minuten einwirken lassen
5. Mit weicher Bürste schrubben
6. Gründlich mit Süßwasser spülen
7. Vollständig trocknen
8. Bei hartnäckigem Schimmel: Spezialreiniger (Star Brite Sail Cleaner)
KEIN Bleichmittel — schädigt Nähfäden und Beschichtungen!

### Spezial-Fragen

**F23: Was ist ein selbstwendendes Fock-System und wann lohnt es sich?**
Ein selbstwendendes System verwendet eine Querschiene auf dem Vordeck, über die das
Schothorn bei der Wende automatisch die Seite wechselt. Lohnt sich für: Einhandsegler,
Kurzhandcrews (2 Personen), häufiges Wenden (Flüsse, enge Reviere), Komfort-orientierte
Segler. Nachteile: kleinere Segelfläche, eingeschränkte Trimmbarkeit, Kosten für
Schienensystem (1.500–5.500 EUR).

**F24: Kann ich eine Genua auf einem Kutterstag fahren?**
Nein, auf dem Kutterstag wird typischerweise ein Staysail (Kutter-Fock) oder eine
kleine Fock gefahren (LP/J 90–100 % bezogen auf das Kutterstag). Eine Genua mit
Überlappung ist für das Kutterstag nicht vorgesehen — sie wird am Vorstag gefahren.

**F25: Was ist der Unterschied zwischen Code 0 und Gennaker?**
Code 0: Flacheres Profil, kann höher am Wind gefahren werden (ab TWA 55–60°), wird
auf Top-Down-Furler gefahren, kleinere Fläche. Gennaker: Tieferes Profil, typisch ab
TWA 70–80°, wird in Bergesock oder auf Furler gefahren, größere Fläche. Der Code 0
ist ein „Reaching-Segel", der Gennaker ein „Raumschot-Segel".

**F26: Was bedeuten die Prozentangaben bei Genuas (z.B. 135 %)?**
Die Prozentzahl gibt das LP/J-Verhältnis an: LP (Lot Perpendicular) = kürzeste Distanz
vom Schothorn zum Vorliek; J = Vordreiecks-Basis (Vorstag-Fußpunkt bis Mast auf Deckshöhe).
135 % bedeutet: Das Segel überlappt das Großsegel-Dreieck um 35 % der J-Strecke.
Eine „100 %-Fock" hat keine Überlappung.

**F27: Wie viele Seemeilen hält mein Segel?**
Grobe Richtwerte: Dacron: 15.000–30.000 sm, Laminat: 8.000–15.000 sm,
3Di/Membran: 20.000–40.000 sm. Diese Werte variieren stark je nach Pflege,
Windverhältnissen, UV-Exposition und Segelprofil. Ein gut gepflegtes Dacron-Segel
auf einer Langfahrt-Yacht kann 50.000+ sm erreichen.

---

## 13. Glossar

| Begriff | Erklärung |
|---|---|
| **Achterliek** (leech) | Hintere Kante des Segels, von Kopf zu Schothorn |
| **Achterliek-Draht** (leech wire) | Dünner Draht oder Leine im Achterliek-Saum zur Formkontrolle |
| **Arbeitsfock** (working jib) | Fock ohne Überlappung (LP/J ≤ 100 %) für mittlere Windstärken |
| **Barber Hauler** | Zusätzliche Schot-Umlenkung zur Änderung des Holepunkts quer zum Boot |
| **Bias** (Schräge) | Diagonale Richtung im Gewebe (45° zu Kette/Schuss), maximal dehnbar |
| **Blister** (Gennaker) | Raumschot-Segel, asymmetrisch, am Bugspriet gefahren |
| **Code 0** (Screecher) | Flaches Leichtwind-Vorsegel auf Top-Down-Furler, TWA 55–120° |
| **Cross-Cut** | Segelschnitt mit horizontal verlaufenden Tuchbahnen |
| **Cunningham** | Öse oder Strecker am Vorliek zur Kontrolle der Profiltiefe-Position |
| **Dacron** | Handelsname für Polyester-Segeltuch (PET-Gewebe) |
| **DCF** (Dyneema Composite Fabric) | Ultraleichtes Laminat aus Dyneema-Fasern in Mylar-Matrix |
| **Delaminierung** | Trennung der Schichten in einem Laminatsegel |
| **Dyneema** (UHMWPE) | Hochfeste Polyethylen-Faser (DSM), leichter als Wasser |
| **Fock** (jib) | Vorsegel ohne Überlappung (LP/J ≤ 100 %) |
| **Fockschiene** (jib track) | Querschiene auf dem Vordeck für selbstwendende Fock |
| **Furler** | Rollreffanlage zum Ein- und Ausrollen des Vorsegels |
| **Furler-Trommel** (drum) | Unteres Bauteil der Rollreffanlage, nimmt die Furler-Leine auf |
| **Genua** (genoa) | Vorsegel mit Überlappung (LP/J > 100 %) |
| **Genua-Schiene** (genua track) | Längsschiene auf dem Seitendeck für den Genua-Holepunkt |
| **Hals** (tack) | Untere vordere Ecke des Segels (Verbindung Vorliek/Unterliek) |
| **Holepunkt** (sheet lead) | Position des Schot-Leitblocks auf der Genua-Schiene |
| **Kausch** (thimble) | Metallöse zum Schutz der Segel-Ecken vor Schamfilschäden |
| **Kopf** (head) | Obere Ecke des Segels, Befestigung am Fall |
| **Kopfwirbel** (swivel) | Drehbares Verbindungsstück am Masttopp des Furlers |
| **Kutterstag** (inner forestay) | Inneres Vorstag bei Kutter-Takelung |
| **Liektau** (luff tape/rope) | Tau oder Band am Vorliek, wird in die Furler-Nut eingeführt |
| **LP** (Lot Perpendicular) | Kürzeste Distanz vom Schothorn zum Vorliek |
| **Luff Pad** | Schaumstoff-Streifen am Vorliek zur Verbesserung des Rollprofils |
| **Mylar** | PET-Folie, Matrix-Material in Segellaminaten |
| **Pentex** | Hochmodul-Polyester-Faser mit reduzierter Dehnung |
| **Profiltiefe** (camber depth) | Maximale Wölbung des Segelprofils, in % der Sehnenlänge |
| **Radial-Schnitt** | Segelschnitt mit sternförmig von den Ecken verlaufenden Bahnen |
| **Schamfilen** (chafe) | Abrieb durch Reibung an Wanten, Salingen oder anderen Teilen |
| **Schothorn** (clew) | Hintere untere Ecke des Segels, Befestigung der Schot |
| **Selbstwendefock** (self-tacking jib) | Fock mit automatischem Seitenwechsel über Querschiene |
| **Slot-Effekt** | Aerodynamische Wechselwirkung zwischen Vorsegel und Großsegel |
| **Staysail** | Inneres Vorsegel bei Kutter-Takelung, am Kutterstag gefahren |
| **Sturmfock** (storm jib) | Schwerwetter-Vorsegel, stark reduzierte Fläche, OSR-Anforderung |
| **Taffeta** | Gewebte Schutzschicht auf der Außenseite eines Laminatsegels |
| **Technora** | Hochfeste Aramidfaser (Teijin), UV-beständiger als Kevlar |
| **Torque-Seil** (torque rope) | Anti-Torsions-Seil für Top-Down-Furler (Code 0, Gennaker) |
| **Trimmfäden** (telltales) | Wollfäden am Vorliek zur Anzeige der Strömungsrichtung |
| **Twist** | Verwindung des Segels (Änderung des Anstellwinkels von unten nach oben) |
| **Unterliek** (foot) | Untere Kante des Segels, von Hals zu Schothorn |
| **UV-Schutzstreifen** (UV strip) | Schutzstreifen aus Sunbrella/Weblon am Achterliek der Rollgenua |
| **Vectran** (LCP) | Flüssigkristalline Polymerfaser, geringes Creep, UV-empfindlich |
| **Vorliek** (luff) | Vordere Kante des Segels, am Vorstag befestigt |
| **Vorstag** (forestay) | Draht oder Stange vom Masttopp zum Bug |
| **Yankee** | Hochgeschnittenes Vorsegel mit hohem Schothorn, gute Sicht |

---

## 14. Schnell-Referenz

### 14.1 Windbereich-Übersicht (TWS in Knoten)

```
         0    4    8   12   16   20   24   28   32   36   40+
         |    |    |    |    |    |    |    |    |    |    |
Code 0   |====|====|====|====|                              
Genua 1  |    |====|====|====|                              
Genua 2  |         |====|====|====|                         
Genua 3  |              |====|====|====|                    
Genua 4  |                   |====|====|====|               
Fock     |              |====|====|====|====|               
Staysail |                        |====|====|====|====|     
Sturmfock|                             |====|====|====|====|
Gennaker |         |====|====|====|====|                    
```

### 14.2 LP/J-Verhältnis Übersicht

```
Sturmfock      50–65 %   ██
Selbstwendefock 85–105 % ████
Fock           95–100 %  ████
Genua 4       100–110 %  █████
Genua 3       110–125 %  █████
Genua 2       130–140 %  ██████
Genua 1       150–155 %  ███████
Code 0        160–200 %  █████████
```

### 14.3 Material-Vergleich Kurzübersicht

| Material | Dehnung | UV | Haltbarkeit | Preis | Empfehlung |
|---|---|---|---|---|---|
| Dacron | ★★☆☆ | ★★★★ | ★★★★ | ★★★★ | Fahrtensegler |
| Pentex | ★★★☆ | ★★★★ | ★★★☆ | ★★★☆ | Aktive Segler |
| Technora | ★★★★ | ★★★☆ | ★★★☆ | ★★☆☆ | Perf.-Cruiser |
| Carbon | ★★★★★ | ★★★★★ | ★★☆☆ | ★☆☆☆ | Regatta |
| Dyneema | ★★★★ | ★★★★ | ★★★☆ | ★★☆☆ | Perf.-Cruiser |
| Vectran | ★★★★ | ★★☆☆ | ★★★☆ | ★★☆☆ | Laminat-Kern |
| 3Di | ★★★★★ | ★★★★ | ★★★★ | ★☆☆☆ | Ambitionierte |
| DCF | ★★★★★ | ★★★★ | ★★★☆ | ★☆☆☆ | Ultra-Leicht |

### 14.4 Trimm-Checkliste (Am-Wind-Kurs)

```
1. □ Vorstag-Spannung: Achterstag/Backstag entsprechend Windstärke
2. □ Fall-Spannung: Keine horizontalen Falten am Vorliek
3. □ Holepunkt: Alle 3 Trimmfaden-Paare reagieren gleichzeitig
4. □ Schot-Spannung: Oberer Achterliek-Trimmfaden strömt 50 % der Zeit
5. □ Achterliek-Leine: Kein Haken, leichtes Flattern akzeptabel
6. □ Barber Hauler: Nur bei Bedarf (Halbwind-/Raumschotkurse)
7. □ Slot-Abstand: 10–15 % des Großsegel-Unterlieks im oberen Bereich
```

### 14.5 Furler-Wartungs-Intervalle

```
Monatlich:     Sichtprüfung, Süßwasser-Spülung (Salzwasser-Revier)
Vierteljährlich: Drehmoment-Test (≤ 5 kg Zug zum Ausrollen)
Halbjährlich:  Profil-Verbinder prüfen, Furler-Leine auf Verschleiß prüfen
Jährlich:      Kopfwirbel-Inspektion, Schot-Zustand, Trimmfäden erneuern
Alle 2–3 J.:   Professioneller Furler-Service (Kugellager, Schmierung)
Alle 5–7 J.:   Kugellager-Austausch, Profil auf Korrosion/Verformung prüfen
```

---

## 15. ANHANG A–H: Fallstudien

### ANHANG A: Rollgenua-Ausfall auf Atlantik-Überquerung

**Yacht:** Bavaria 40 Cruiser (Baujahr 2012), 12,35 m LOA
**Vorsegel:** Dacron Genua 2 (135 %), Baujahr 2018, Furlex 300S
**Revier:** Atlantik-Überquerung, Las Palmas → Barbados (November 2023)

**Ereignis:**
Am Tag 8 der Überquerung (Position ca. 22°N 32°W) bei 18–22 kn TWS und TWA 120°
versagte der UV-Schutzstreifen am oberen Drittel des Achterlieks. Die darunterliegenden
Nähte waren durch UV-Degradation bereits geschwächt. Beim nächsten Rollversuch riss
eine Bahn-zu-Bahn-Naht auf ca. 1,5 m Länge.

**Sofortmaßnahme:**
Genua wurde vollständig eingerollt und mit zusätzlichen Schot-Wicklungen gesichert.
Staysail am Kutterstag gesetzt (8,5 m² Segelfläche). Geschwindigkeit reduzierte sich
von 7,2 auf 5,8 kn.

**Provisorische Reparatur (auf See):**
- Genua bei ruhigem Wetter (12 kn) teilweise ausgerollt
- Riss mit Insignia-Tape (beidseitig) und Segelnadel/gewachstem Faden repariert
- Genua danach nur bei < 15 kn eingesetzt

**Kosten der Reparatur in Barbados:**
- Professionelle Naht-Reparatur: 450 USD
- UV-Streifen-Erneuerung (komplett): 800 USD
- Gesamt: 1.250 USD

**Lehren:**
1. UV-Streifen vor Blauwasser-Reisen professionell inspizieren lassen
2. Staysail/Sturmfock als unabhängiges Backup unverzichtbar
3. Segel-Reparaturset an Bord: Insignia-Tape, Segelnadeln, gewachster Faden, Ahle

### ANHANG B: Selbstwendefock-Nachrüstung auf Hallberg-Rassy 372

**Yacht:** Hallberg-Rassy 372 (Baujahr 2005), 11,18 m LOA
**Vorher:** Genua 2 (135 %) auf Furlex 300S, Schot über Winschen
**Nachher:** Selbstwendefock (95 %) auf Furlex 300S + Harken Self-Tacking System

**Motivation:**
Eignerpaar (beide 65+), segelt zu zweit, häufig in skandinavischen Schären mit
vielen Wenden. Die Genua-Wenden erforderten beide Personen (eine am Steuer, eine
an den Winschen). Ziel: Einhand-fähige Wenden.

**Maßnahmen:**
1. Neue Selbstwendefock (95 % LP/J) bei Elvström bestellt: 3.800 EUR (Dacron)
2. Harken Self-Tacking Schiene (1.600 mm): 2.200 EUR
3. Montage (Yachtwerft, inkl. Deck-Verstärkung): 1.800 EUR
4. Zusätzliches Fall für Genua (optional, bei Leichtwind): 350 EUR
5. Genua als Zweit-Segel behalten (Leichtwind, Langstrecke)
6. Gesamt: 8.150 EUR

**Ergebnis:**
- Wenden: von 45–60 Sekunden auf < 10 Sekunden (komplett selbsttätig)
- Geschwindigkeitsverlust vs. 135 %-Genua: ca. 0,3–0,5 kn bei 8–12 kn TWS
- Eignerzufriedenheit: sehr hoch, segelt jetzt häufiger einhand

**Nachteile (beobachtet):**
- Bei < 6 kn TWS deutlich weniger Vortrieb als mit Genua
- Schiene erfordert regelmäßige Wartung (Salzwasser-Revier)
- Segel wendet bei < 4 kn TWS manchmal nicht sauber (zu wenig Druck)

### ANHANG C: Code-0-Stundenglas auf Regatta

**Yacht:** X-Yachts Xp 44 (Baujahr 2016), 13,29 m LOA
**Vorsegel:** Code 0, 75 m², North Sails 3Di 780, Facnor FX+ 3500 Furler
**Revier:** Kieler Woche 2024, Offshore-Wettfahrt

**Ereignis:**
Bei TWS 14 kn und TWA 85° wurde der Code 0 zum Bergen eingerollt. Die Schot
wurde zu schnell gefiert, wodurch das Segel in eine Stundenglas-Formation geriet.
Das obere und untere Drittel waren eingerollt, die Mitte blähte sich auf.

**Sofortmaßnahme:**
1. Einrollen gestoppt
2. Schot vollständig gelöst
3. Kurs geändert (Vorwind, Code 0 im Lee des Großsegels)
4. Fall um 50 cm gefiert → Segel begann zu flattern
5. Stundenglas löste sich nach ca. 30 Sekunden
6. Erneuter Einrollversuch: kontrolliert, Schot unter leichtem Zug → erfolgreich

**Ursachenanalyse:**
- Torque-Seil war korrekt gespannt
- Ursache: zu schnelles Schot-Fieren → ungleichmäßige Windbelastung → Stundenglas
- Crew-Fehler, kein Material-Problem

**Lehren:**
1. Code 0 immer kontrolliert einrollen (Schot unter leichtem Zug)
2. Kurs vor dem Bergen anpassen (Vorwind oder Segel im Großsegel-Schatten)
3. Bei Stundenglas: NICHT weiterrollen, sondern komplett ausrollen und neu versuchen
4. Regatta-Training sollte Code-0-Bergen unter verschiedenen Bedingungen einschließen

### ANHANG D: Laminat-Genua-Delaminierung nach 4 Jahren

**Yacht:** Beneteau Oceanis 51.1 (Baujahr 2019), 15,38 m LOA
**Vorsegel:** Pentex/Dyneema-Laminat Genua (130 %), Quantum Fusion M, Baujahr 2020
**Revier:** Mittelmeer (Kroatien), ganzjährig am Mast

**Entdeckung:**
Bei der Herbst-Inspektion 2024 wurden großflächige Delaminierungen im oberen
Drittel des Segels festgestellt. Milchige Verfärbung auf ca. 3 m² Fläche,
Blasenbildung an mehreren Stellen.

**Ursachenanalyse:**
1. Segel wurde ganzjährig am Vorstag belassen (auch im Sommer bei Nichtgebrauch)
2. Furler nicht vollständig eingerollt (Segel teilweise exponiert)
3. UV-Schutzstreifen zu schmal (280 mm statt empfohlener 380 mm)
4. Mittelmeer-Sonne: extrem hohe UV-Belastung (2.500+ Sonnenstunden/Jahr)
5. Klebstoff-Degradation durch UV → Delaminierung

**Reparatur-Versuch:**
Lokale Reparatur durch Quantum-Service-Partner in Split (Kroatien).
Kosten: 1.800 EUR. Ergebnis: Delaminierung setzte sich innerhalb von 6 Monaten fort.

**Endlösung:**
Neusegel bestellt: Quantum Fusion M mit breiterem UV-Streifen (420 mm) und
beidseitigem Taffeta. Kosten: 7.200 EUR.

**Lehren:**
1. Laminatsegel im Mittelmeer MÜSSEN adäquaten UV-Schutz haben
2. UV-Streifen-Breite großzügig kalkulieren (+20 % über Minimum)
3. Segel bei längerem Nichtgebrauch (> 2 Wochen) vollständig einrollen
4. Für ganzjährige Mittelmeer-Nutzung: Dacron oder 3Di Endurance erwägen

### ANHANG E: Sturmfock-Einsatz im Biskaya-Sturm

**Yacht:** Hallberg-Rassy 412 (Baujahr 2017), 12,65 m LOA
**Vorsegel:** Sturmfock, 6,8 m², schweres Dacron (380 g/m²), orange
**Revier:** Golf von Biskaya, November 2024, Passage La Coruña → La Rochelle

**Ereignis:**
Frontdurchgang mit Windstärken 9–10 Beaufort (45–55 kn), signifikante Wellenhöhe 6–8 m.
Dauer: 18 Stunden.

**Vorgehensweise:**
1. Bei 30 kn (zunehmend): Rollgenua komplett eingerollt, Staysail gesetzt
2. Bei 38 kn: Staysail geborgen, Sturmstag (abnehmbares Kutterstag) installiert
3. Sturmfock am Sturmstag mit Piston-Hanks befestigt und gesetzt
4. Konfiguration: Sturmfock + 3. Reff im Großsegel
5. Bei 48 kn: Großsegel komplett geborgen, nur Sturmfock
6. Kurs: 30° vom Wind (Halbwind), Geschwindigkeit 4–5 kn, kontrollierbar

**Beobachtungen:**
- Sturmfock hielt allen Belastungen stand
- Kauschen und Stagreiter zeigten nach 18 Stunden keine Abnutzung
- Steuerung war mit Sturmfock allein kontrollierbar (leichter Ruderdruck)
- Sichtbarkeit der orangefarbenen Sturmfock für Handelsschiffe: gut

**Lehren:**
1. Sturmfock MUSS vor der Reise probeweise gesetzt werden (inkl. Sturmstag)
2. Alle Beschläge (Stagreiter, Schäkel, Kauschen) vorher inspizieren
3. Sturmstag-Installation unter kontrollierten Bedingungen üben
4. Orange Farbe hat sich bei Sichtverhältnissen < 500 m bewährt
5. Sturmfock-Schoten vorher bereitliegen lassen (separate Schoten!)

### ANHANG F: Genua-Schamfilen an Salingen

**Yacht:** Jeanneau Sun Odyssey 449 (Baujahr 2018), 13,75 m LOA
**Vorsegel:** Rollgenua 135 %, Dacron Cross-Cut, Profurl C420
**Revier:** Ostsee (Dänische Südsee), Sommersaison

**Problem:**
Nach 3 Saisons zeigten sich deutliche Scheuerstellen auf der Genua, ca. 1,8 m oberhalb
des Unterlieks, in einer Linie, die dem Kontakt mit den Salingen bei der Wende entspricht.
Das Segeltuch war an diesen Stellen auf ca. 50 % der Ursprungsdicke abgescheuert.

**Ursachenanalyse:**
1. Salingen-Spitzen waren nicht mit Schutzkappen versehen
2. Keine Wanten-Überzüge (Leeder-Covers) installiert
3. Genua mit 135 % Überlappung scheuert bei jeder Wende an den Salingen
4. Eignerin wendete häufig (Dänische Südsee: enge Reviere) → hohe Kontakthäufigkeit

**Reparatur:**
1. Scheuerschutz-Patches (beide Seiten) aufgenäht: 320 EUR
2. Salingen-Schutzkappen installiert: 45 EUR
3. Wanten-Überzüge (Leeder-Covers, 4 Stück): 180 EUR
4. Gesamt: 545 EUR

**Langfristige Lösung (empfohlen):**
Wechsel auf Genua mit 120 % Überlappung oder Selbstwendefock (95 %) für den
Schären-Einsatz, Genua nur für Langstrecken-Segeln.

### ANHANG G: Furler-Versagen durch Lagerschaden

**Yacht:** Bavaria Cruiser 37 (Baujahr 2014), 11,30 m LOA
**Furler:** Selden Furlex 300S (Baujahr 2014, original)
**Vorsegel:** Dacron Genua 130 %, 38 m²
**Revier:** Mittelmeer (Griechenland), Chartereinsatz

**Problem:**
Furler ließ sich nicht mehr einrollen. Crew versuchte mit Kraft, die Furler-Leine
durchzuziehen. Ergebnis: Furler-Leine riss, Genua blieb ausgerollt.

**Ursachenanalyse:**
1. Kopfwirbel-Kugellager durch Salzwasser-Korrosion zerstört
2. Letzter Furler-Service: nie (10 Jahre ohne Wartung!)
3. Charterbetrieb: keine regelmäßige Wartung durch wechselnde Crews
4. Kugellager blockiert → Furler-Trommel dreht nicht → Leine reißt

**Sofortmaßnahme (auf See):**
- Genua mit Hilfe einer zweiten Leine (als Furler-Ersatz um das Vorstag gewickelt)
  notdürftig eingerollt und mit Segel-Stoppern gesichert
- Unter Motor in den nächsten Hafen (Lefkas)

**Reparatur:**
1. Kopfwirbel-Kugellager ersetzt: 140 EUR (Ersatzteil)
2. Trommel-Kugellager ersetzt: 95 EUR (Ersatzteil)
3. Neue Furler-Leine: 85 EUR
4. Arbeit (Rigger, 4 Stunden): 320 EUR
5. Gesamt: 640 EUR

**Lehren:**
1. Furler-Wartung ist NICHT optional — auch im Charterbetrieb
2. Alle 2–3 Jahre professioneller Service (200–500 EUR spart tausende)
3. Bei Schwergängigkeit: SOFORT Service, nicht mit Kraft weiterdrehen!
4. Charteryachten: Furler-Service in den Wartungsplan aufnehmen

### ANHANG H: Übergang von Dacron zu 3Di Endurance

**Yacht:** Swan 48 (Baujahr 2010), 14,78 m LOA
**Alt-Segel:** Dacron Tri-Radial Genua (130 %), Elvström, 6 Jahre alt
**Neu-Segel:** 3Di Endurance Genua (130 %), North Sails
**Revier:** Ostsee + Mittelmeer (Sommer Kroatien, Winter Kiel)

**Motivation:**
- Dacron-Genua hatte nach 6 Jahren deutlich an Form verloren (Bauch bei > 12 kn)
- Eigner wollte bessere Performance ohne Kompromisse bei der Haltbarkeit
- 3Di Endurance als „bester Kompromiss" für aktiven Fahrtensegler empfohlen

**Investition:**
- 3Di Endurance Genua (130 %, ca. 52 m²): 11.800 EUR
- Neue UV-Schutzlösung (3Di-integriert): im Preis enthalten
- Neue Schoten (Dyneema-Kern, 14 mm): 280 EUR
- Genua-Trimmberatung (North Sails Kiel, 2 Stunden an Bord): 350 EUR
- Gesamt: 12.430 EUR

**Ergebnis nach 2 Saisons:**
- Geschwindigkeitsgewinn: +0,3–0,5 kn bei 10–15 kn TWS (Amwind)
- Formstabilität: nach 2 Saisons keine messbare Profilveränderung
- Handling: leichter als Dacron (geringeres Gewicht)
- UV-Beständigkeit: bisher keine sichtbare Degradation
- Eignerzufriedenheit: sehr hoch

**Vergleich Dacron vs. 3Di Endurance (Eigner-Einschätzung):**

| Kriterium | Dacron (alt) | 3Di Endurance (neu) |
|---|---|---|
| Performance | ★★★☆☆ | ★★★★☆ |
| Formstabilität | ★★★☆☆ | ★★★★★ |
| Handhabung | ★★★★☆ | ★★★★★ |
| UV-Beständigkeit | ★★★★☆ | ★★★★☆ |
| Preis | ★★★★☆ | ★★☆☆☆ |
| Gesamt | ★★★☆☆ | ★★★★☆ |

---

## 16. ANHANG I–R: Pydantic v2 Modelle

### ANHANG I: HeadsailSpec

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class HeadsailType(str, Enum):
    GENUA_1 = "genua_1"
    GENUA_2 = "genua_2"
    GENUA_3 = "genua_3"
    GENUA_4 = "genua_4"
    WORKING_JIB = "working_jib"
    SELF_TACKING_JIB = "self_tacking_jib"
    STORM_JIB = "storm_jib"
    CODE_0 = "code_0"
    GENNAKER = "gennaker"
    STAYSAIL = "staysail"
    YANKEE = "yankee"


class SailMaterial(str, Enum):
    DACRON = "dacron"
    PENTEX = "pentex"
    TECHNORA = "technora"
    CARBON = "carbon"
    DYNEEMA = "dyneema"
    VECTRAN = "vectran"
    MYLAR_LAMINATE = "mylar_laminate"
    DCF = "dcf"
    THREE_DI = "3di"
    EPEX = "epex"
    STRATIS = "stratis"
    NYLON = "nylon"


class SailCut(str, Enum):
    CROSS_CUT = "cross_cut"
    RADIAL = "radial"
    TRI_RADIAL = "tri_radial"
    BI_RADIAL = "bi_radial"
    MEMBRANE = "membrane"


class HeadsailSpec(BaseModel):
    model_config = {"from_attributes": True}

    headsail_type: HeadsailType
    lp_j_ratio_percent: float = Field(
        ..., ge=40.0, le=220.0,
        description="LP/J-Verhältnis in Prozent"
    )
    sail_area_m2: float = Field(
        ..., gt=0.0,
        description="Segelfläche in Quadratmetern"
    )
    luff_length_mm: float = Field(
        ..., gt=0.0,
        description="Vorliek-Länge in mm"
    )
    leech_length_mm: float = Field(
        ..., gt=0.0,
        description="Achterliek-Länge in mm"
    )
    foot_length_mm: float = Field(
        ..., gt=0.0,
        description="Unterliek-Länge in mm"
    )
    material: SailMaterial
    cut: SailCut
    cloth_weight_gsm: float = Field(
        ..., gt=0.0,
        description="Tuchgewicht in g/m²"
    )
    manufacturer: Optional[str] = None
    model_name: Optional[str] = None
    year_built: Optional[int] = Field(
        None, ge=1950, le=2030,
        description="Baujahr des Segels"
    )
    uv_strip_present: bool = Field(
        default=False,
        description="UV-Schutzstreifen vorhanden"
    )
    uv_strip_width_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Breite des UV-Schutzstreifens in mm"
    )
    furler_compatible: bool = Field(
        default=True,
        description="Für Rollreffanlage ausgelegt"
    )
    luff_tape_diameter_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Liektau-Durchmesser in mm"
    )
    tws_min_kn: float = Field(
        ..., ge=0.0,
        description="Minimale wahre Windgeschwindigkeit in Knoten"
    )
    tws_max_kn: float = Field(
        ..., gt=0.0,
        description="Maximale wahre Windgeschwindigkeit in Knoten"
    )
    camber_depth_percent: Optional[float] = Field(
        None, ge=0.0, le=30.0,
        description="Profiltiefe in Prozent der Sehnenlänge"
    )
    camber_position_percent: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Position maximale Wölbung in Prozent vom Vorliek"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Kaufpreis in EUR"
    )
```

### ANHANG J: HeadsailTrim

```python
class HeadsailTrim(BaseModel):
    model_config = {"from_attributes": True}

    headsail_type: HeadsailType
    tws_kn: float = Field(
        ..., ge=0.0,
        description="Wahre Windgeschwindigkeit in Knoten"
    )
    twa_deg: float = Field(
        ..., ge=0.0, le=180.0,
        description="Wahrer Windwinkel in Grad"
    )
    sheet_lead_position_mm: Optional[float] = Field(
        None,
        description="Holepunkt-Position in mm ab Vorderkante Schiene"
    )
    sheet_angle_deg: Optional[float] = Field(
        None, ge=0.0, le=30.0,
        description="Schot-Winkel zur Horizontalen in Grad"
    )
    halyard_tension: str = Field(
        ...,
        description="Fall-Spannung: 'locker', 'mittel', 'fest', 'max'"
    )
    sheet_tension: str = Field(
        ...,
        description="Schot-Spannung: 'locker', 'mittel', 'fest', 'max'"
    )
    leech_line_tension: str = Field(
        default="mittel",
        description="Achterliek-Leinen-Spannung: 'locker', 'mittel', 'fest'"
    )
    barber_hauler_active: bool = Field(
        default=False,
        description="Barber Hauler in Verwendung"
    )
    barber_hauler_direction: Optional[str] = Field(
        None,
        description="'inhaul' oder 'outhaul'"
    )
    cunningham_active: bool = Field(
        default=False,
        description="Cunningham in Verwendung"
    )
    forestay_sag_percent: Optional[float] = Field(
        None, ge=0.0, le=5.0,
        description="Vorstag-Durchhang in Prozent der Vorstaglänge"
    )
    telltale_upper_streaming: bool = Field(
        default=True,
        description="Obere Trimmfäden strömen korrekt"
    )
    telltale_middle_streaming: bool = Field(
        default=True,
        description="Mittlere Trimmfäden strömen korrekt"
    )
    telltale_lower_streaming: bool = Field(
        default=True,
        description="Untere Trimmfäden strömen korrekt"
    )
    leech_telltale_streaming_percent: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Prozent der Zeit, in der Achterliek-Trimmfaden strömt"
    )
    notes: Optional[str] = None
```

### ANHANG K: HeadsailCondition

```python
class ConditionRating(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    UNUSABLE = "unusable"


class HeadsailCondition(BaseModel):
    model_config = {"from_attributes": True}

    overall_condition: ConditionRating
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    estimated_remaining_life_nm: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Restlebensdauer in Seemeilen"
    )
    cloth_condition: ConditionRating
    cloth_notes: Optional[str] = None
    stitching_condition: ConditionRating
    stitching_notes: Optional[str] = None
    uv_strip_condition: Optional[ConditionRating] = None
    uv_strip_notes: Optional[str] = None
    hardware_condition: ConditionRating = Field(
        ...,
        description="Zustand von Kauschen, Ösen, Stegreitern"
    )
    hardware_notes: Optional[str] = None
    luff_tape_condition: ConditionRating
    luff_tape_notes: Optional[str] = None
    leech_wire_condition: Optional[ConditionRating] = None
    leech_wire_notes: Optional[str] = None
    patches_condition: ConditionRating = Field(
        ...,
        description="Zustand der Verstärkungspatches (Kopf, Hals, Schothorn)"
    )
    patches_notes: Optional[str] = None
    delamination_present: bool = Field(
        default=False,
        description="Delaminierung vorhanden (nur Laminatsegel)"
    )
    delamination_area_m2: Optional[float] = Field(
        None, ge=0.0,
        description="Fläche der Delaminierung in m²"
    )
    chafe_damage_present: bool = Field(
        default=False,
        description="Schamfilschäden vorhanden"
    )
    chafe_locations: Optional[list[str]] = None
    repair_recommended: bool = Field(
        default=False,
        description="Reparatur empfohlen"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Reparaturkosten in EUR"
    )
    replacement_recommended: bool = Field(
        default=False,
        description="Austausch empfohlen"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzter Wiederbeschaffungswert in EUR"
    )
    confidence_level: str = Field(
        ...,
        description="Konfidenzlevel: 'measured', 'visual_high', 'visual_medium', 'visual_low', 'estimated'"
    )
    inspection_date: Optional[str] = None
    inspector_notes: Optional[str] = None
```

### ANHANG L: UVStripStatus

```python
class UVStripMaterial(str, Enum):
    SUNBRELLA = "sunbrella"
    WEBLON = "weblon"
    OTHER = "other"
    UNKNOWN = "unknown"


class UVStripStatus(BaseModel):
    model_config = {"from_attributes": True}

    material: UVStripMaterial
    color: Optional[str] = Field(
        None,
        description="Farbe des UV-Streifens (z.B. 'navy', 'schwarz', 'grau')"
    )
    width_leech_mm: float = Field(
        ..., ge=0.0,
        description="Breite am Achterliek in mm"
    )
    width_foot_mm: float = Field(
        ..., ge=0.0,
        description="Breite am Unterliek in mm"
    )
    width_required_mm: float = Field(
        ..., ge=0.0,
        description="Erforderliche Mindestbreite in mm (berechnet)"
    )
    coverage_adequate: bool = Field(
        ...,
        description="Abdeckung ausreichend (breiter als erforderlich)"
    )
    condition: ConditionRating
    uv_degradation_visible: bool = Field(
        default=False,
        description="Sichtbare UV-Degradation"
    )
    stitching_intact: bool = Field(
        default=True,
        description="Nähte intakt"
    )
    fading_percent: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Geschätzter Farbverlust in Prozent"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Austauschkosten in EUR"
    )
    confidence_level: str = Field(
        ...,
        description="Konfidenzlevel der Bewertung"
    )
```

### ANHANG M: FurlerCompatibility

```python
class FurlerBrand(str, Enum):
    SELDEN = "selden"
    PROFURL = "profurl"
    HARKEN = "harken"
    FACNOR = "facnor"
    KARVER = "karver"
    RONSTAN = "ronstan"
    RECKMANN = "reckmann"
    OTHER = "other"


class FurlerType(str, Enum):
    GENUA_FURLER = "genua_furler"
    TOP_DOWN_FURLER = "top_down_furler"
    CODE_0_FURLER = "code_0_furler"


class FurlerCompatibility(BaseModel):
    model_config = {"from_attributes": True}

    furler_brand: FurlerBrand
    furler_model: str = Field(
        ...,
        description="Modellbezeichnung (z.B. 'Furlex 300S', 'NEX 7.0')"
    )
    furler_type: FurlerType
    max_forestay_diameter_mm: float = Field(
        ..., gt=0.0,
        description="Maximaler Vorstag-Durchmesser in mm"
    )
    max_luff_tape_diameter_mm: float = Field(
        ..., gt=0.0,
        description="Maximaler Liektau-Durchmesser in mm"
    )
    max_sail_area_m2: float = Field(
        ..., gt=0.0,
        description="Maximale Segelfläche in m²"
    )
    min_boat_loa_m: Optional[float] = Field(
        None, gt=0.0,
        description="Minimale Bootslänge in m"
    )
    max_boat_loa_m: Optional[float] = Field(
        None, gt=0.0,
        description="Maximale Bootslänge in m"
    )
    swivel_type: str = Field(
        ...,
        description="Kopfwirbel-Typ"
    )
    compatible_with_sail: bool = Field(
        ...,
        description="Kompatibel mit dem aktuellen Segel"
    )
    compatibility_issues: Optional[list[str]] = Field(
        None,
        description="Liste von Kompatibilitätsproblemen"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Preis der Furler-Anlage in EUR"
    )
    weight_kg: Optional[float] = Field(
        None, gt=0.0,
        description="Gewicht der Furler-Anlage in kg"
    )
    service_interval_years: Optional[float] = Field(
        None, gt=0.0,
        description="Empfohlenes Service-Intervall in Jahren"
    )
    bearing_replacement_interval_years: Optional[float] = Field(
        None, gt=0.0,
        description="Empfohlenes Kugellager-Austausch-Intervall in Jahren"
    )
```

### ANHANG N: HeadsailWardrobe

```python
class SailingProfile(str, Enum):
    WEEKEND_INLAND = "weekend_inland"
    COASTAL_ACTIVE = "coastal_active"
    BLUEWATER = "bluewater"
    REGATTA = "regatta"
    PERFORMANCE_CRUISER = "performance_cruiser"


class HeadsailWardrobe(BaseModel):
    model_config = {"from_attributes": True}

    boat_loa_m: float = Field(
        ..., gt=0.0,
        description="Bootslänge über Alles in m"
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp (z.B. 'Fahrtensegelyacht', 'Regattayacht')"
    )
    sailing_profile: SailingProfile
    ce_category: str = Field(
        ...,
        description="CE-Kategorie: 'A', 'B', 'C', 'D'"
    )
    rig_type: str = Field(
        default="sloop",
        description="Rigg-Typ: 'sloop', 'cutter', 'ketch', 'schooner'"
    )
    has_furler: bool = Field(
        default=True,
        description="Rollreffanlage vorhanden"
    )
    has_inner_forestay: bool = Field(
        default=False,
        description="Kutterstag vorhanden"
    )
    has_bowsprit: bool = Field(
        default=False,
        description="Bugspriet vorhanden"
    )
    sails: list[HeadsailSpec] = Field(
        ...,
        description="Liste der Vorsegel in der Garderobe"
    )
    total_investment_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Gesamtinvestition Vorsegel-Garderobe in EUR"
    )
    recommended_additions: Optional[list[str]] = Field(
        None,
        description="Empfohlene Ergänzungen"
    )
    wardrobe_rating: str = Field(
        ...,
        description="Bewertung: 'minimal', 'standard', 'empfohlen', 'optimal', 'premium'"
    )
    notes: Optional[str] = None
```

### ANHANG O: HeadsailRepair

```python
class RepairType(str, Enum):
    UV_STRIP_RENEWAL = "uv_strip_renewal"
    STITCH_REPAIR = "stitch_repair"
    STITCH_OVERHAUL = "stitch_overhaul"
    LUFF_TAPE_REPAIR = "luff_tape_repair"
    LEECH_WIRE_REPLACEMENT = "leech_wire_replacement"
    CLEW_PATCH_REPAIR = "clew_patch_repair"
    HEAD_PATCH_REPAIR = "head_patch_repair"
    TACK_PATCH_REPAIR = "tack_patch_repair"
    TEAR_REPAIR_SMALL = "tear_repair_small"
    TEAR_REPAIR_LARGE = "tear_repair_large"
    PANEL_REPLACEMENT = "panel_replacement"
    DELAMINATION_REPAIR = "delamination_repair"
    CHAFE_PATCH = "chafe_patch"
    THIMBLE_REPLACEMENT = "thimble_replacement"
    HANK_REPLACEMENT = "hank_replacement"
    CLEANING = "cleaning"
    REPROOFING = "reproofing"


class RepairUrgency(str, Enum):
    IMMEDIATE = "immediate"
    BEFORE_NEXT_SAIL = "before_next_sail"
    WITHIN_MONTH = "within_month"
    NEXT_WINTER_SERVICE = "next_winter_service"
    MONITOR = "monitor"


class HeadsailRepair(BaseModel):
    model_config = {"from_attributes": True}

    repair_type: RepairType
    urgency: RepairUrgency
    description_de: str = Field(
        ...,
        description="Beschreibung der Reparatur auf Deutsch"
    )
    affected_area: str = Field(
        ...,
        description="Betroffener Bereich (z.B. 'Achterliek oben', 'Schothorn', 'Vorliek Mitte')"
    )
    estimated_cost_min_eur: float = Field(
        ..., ge=0.0,
        description="Minimale geschätzte Kosten in EUR"
    )
    estimated_cost_max_eur: float = Field(
        ..., ge=0.0,
        description="Maximale geschätzte Kosten in EUR"
    )
    diy_possible: bool = Field(
        default=False,
        description="Eigenreparatur möglich"
    )
    diy_difficulty: Optional[str] = Field(
        None,
        description="Schwierigkeitsgrad DIY: 'einfach', 'mittel', 'schwer', 'nicht_empfohlen'"
    )
    professional_required: bool = Field(
        default=True,
        description="Professionelle Reparatur empfohlen/erforderlich"
    )
    estimated_duration_hours: Optional[float] = Field(
        None, gt=0.0,
        description="Geschätzte Reparaturdauer in Stunden"
    )
    related_fault_pattern: Optional[str] = Field(
        None,
        description="Zugehöriges Fehlerbild (z.B. 'F-16_03-01')"
    )
    sail_age_factor: Optional[str] = Field(
        None,
        description="Einfluss des Segelalters auf die Reparatur-Entscheidung"
    )
    confidence_level: str = Field(
        ...,
        description="Konfidenzlevel der Kostenschätzung"
    )
```

### ANHANG P: HeadsailMeasurements

```python
class HeadsailMeasurements(BaseModel):
    model_config = {"from_attributes": True}

    # Grundmaße
    luff_length_mm: float = Field(
        ..., gt=0.0,
        description="Vorliek-Länge (Hals bis Kopf) in mm"
    )
    leech_length_mm: float = Field(
        ..., gt=0.0,
        description="Achterliek-Länge (Kopf bis Schothorn) in mm"
    )
    foot_length_mm: float = Field(
        ..., gt=0.0,
        description="Unterliek-Länge (Hals bis Schothorn) in mm"
    )
    lp_mm: float = Field(
        ..., gt=0.0,
        description="LP (Lot Perpendicular): kürzeste Distanz Schothorn–Vorliek in mm"
    )
    j_mm: float = Field(
        ..., gt=0.0,
        description="J: Vordreiecks-Basis (Vorstag-Fuß bis Mast auf Deck) in mm"
    )
    lp_j_ratio_percent: Optional[float] = Field(
        None,
        description="LP/J-Verhältnis in Prozent (berechnet)"
    )

    # Halbhöhenmaße
    half_width_mm: Optional[float] = Field(
        None, gt=0.0,
        description="Halbhöhenbreite in mm"
    )
    three_quarter_width_mm: Optional[float] = Field(
        None, gt=0.0,
        description="Dreiviertel-Höhenbreite in mm"
    )
    quarter_width_mm: Optional[float] = Field(
        None, gt=0.0,
        description="Viertelhöhenbreite in mm"
    )

    # Profil
    max_camber_depth_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Maximale Profiltiefe in mm"
    )
    max_camber_position_percent: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Position der max. Profiltiefe in % vom Vorliek"
    )

    # Liektau
    luff_tape_diameter_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Liektau-Durchmesser in mm"
    )
    luff_tape_type: Optional[str] = Field(
        None,
        description="Liektau-Typ: 'tau', 'band', 'boltrope', 'tape'"
    )

    # UV-Schutz
    uv_strip_width_leech_mm: Optional[float] = Field(
        None, ge=0.0,
        description="UV-Streifen-Breite Achterliek in mm"
    )
    uv_strip_width_foot_mm: Optional[float] = Field(
        None, ge=0.0,
        description="UV-Streifen-Breite Unterliek in mm"
    )

    # Gewicht und Fläche
    sail_area_m2: Optional[float] = Field(
        None, gt=0.0,
        description="Segelfläche in m² (berechnet oder gemessen)"
    )
    sail_weight_kg: Optional[float] = Field(
        None, gt=0.0,
        description="Segelgewicht in kg"
    )

    # Methodik
    measurement_method: str = Field(
        default="manual",
        description="Messmethode: 'manual', 'laser', 'photogrammetry', 'cad'"
    )
    confidence_level: str = Field(
        default="measured",
        description="Konfidenzlevel: 'measured', 'estimated', 'visual_high'"
    )
    measurement_date: Optional[str] = None
    measured_by: Optional[str] = None
    notes: Optional[str] = None
```

### ANHANG Q: HeadsailFaultPattern

```python
class FaultSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class HeadsailFaultPattern(BaseModel):
    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        description="Fehlerbild-ID (z.B. 'F-16_03-01')"
    )
    fault_name_de: str = Field(
        ...,
        description="Fehlerbild-Name auf Deutsch"
    )
    fault_name_en: str = Field(
        ...,
        description="Fehlerbild-Name auf Englisch"
    )
    severity: FaultSeverity
    frequency: str = Field(
        ...,
        description="Häufigkeit: 'sehr_haeufig', 'haeufig', 'mittel', 'selten'"
    )
    description_de: str = Field(
        ...,
        description="Ausführliche Beschreibung auf Deutsch"
    )
    causes: list[str] = Field(
        ...,
        description="Liste der möglichen Ursachen"
    )
    visual_indicators: list[str] = Field(
        ...,
        description="Liste visueller Indikatoren für AYDI Vision"
    )
    visual_confidence: str = Field(
        ...,
        description="Erwartetes Konfidenzlevel bei visueller Analyse"
    )
    immediate_action_de: Optional[str] = Field(
        None,
        description="Sofortmaßnahme auf Deutsch"
    )
    repair_options: list[dict] = Field(
        ...,
        description="Reparatur-Optionen mit Beschreibung und Kosten"
    )
    prevention_measures: list[str] = Field(
        ...,
        description="Präventive Maßnahmen"
    )
    related_faults: Optional[list[str]] = Field(
        None,
        description="Verwandte Fehlerbilder (IDs)"
    )
    affected_sail_types: list[HeadsailType] = Field(
        ...,
        description="Betroffene Segeltypen"
    )
    affected_materials: Optional[list[SailMaterial]] = Field(
        None,
        description="Besonders betroffene Materialien"
    )
```

### ANHANG R: HeadsailAnalysisResult

```python
class HeadsailAnalysisResult(BaseModel):
    model_config = {"from_attributes": True}

    # Identifikation
    yacht_id: Optional[str] = None
    analysis_id: str = Field(
        ...,
        description="Eindeutige Analyse-ID"
    )
    analysis_date: str = Field(
        ...,
        description="Datum der Analyse (ISO 8601)"
    )
    analysis_level: str = Field(
        ...,
        description="'level_1' (Schnellanalyse) oder 'level_2' (Profi)"
    )

    # Segel-Daten
    headsail_spec: Optional[HeadsailSpec] = None
    headsail_measurements: Optional[HeadsailMeasurements] = None
    headsail_condition: Optional[HeadsailCondition] = None
    uv_strip_status: Optional[UVStripStatus] = None
    furler_compatibility: Optional[FurlerCompatibility] = None
    wardrobe_context: Optional[HeadsailWardrobe] = None

    # Befunde
    fault_patterns_found: list[HeadsailFaultPattern] = Field(
        default_factory=list,
        description="Erkannte Fehlerbilder"
    )
    repairs_recommended: list[HeadsailRepair] = Field(
        default_factory=list,
        description="Empfohlene Reparaturen"
    )

    # Bewertung
    overall_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Gesamtbewertung (0–100)"
    )
    structural_score: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Strukturelle Bewertung (0–100)"
    )
    material_score: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Material-Bewertung (0–100)"
    )
    trim_score: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Trimm-Bewertung (0–100, nur bei Fotos unter Segel)"
    )

    # Kosten
    estimated_repair_cost_total_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Gesamte geschätzte Reparaturkosten in EUR"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzter Wiederbeschaffungswert in EUR"
    )
    repair_vs_replace_recommendation: Optional[str] = Field(
        None,
        description="Empfehlung: 'repair', 'replace', 'monitor', 'nicht_beurteilbar'"
    )

    # Konfidenz
    overall_confidence: str = Field(
        ...,
        description="Gesamt-Konfidenzlevel"
    )
    data_sources: list[str] = Field(
        ...,
        description="Datenquellen: 'structured', 'visual', 'text'"
    )
    pipeline_versions: dict = Field(
        default_factory=dict,
        description="Versionen der verwendeten Analyse-Pipelines"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen und Hinweise"
    )
    suggestions_de: list[str] = Field(
        default_factory=list,
        description="Verbesserungsvorschläge auf Deutsch"
    )
```

---

**Ende des Dokuments — AYDI Maritime Knowledge Base v2.0**
**Letzte Aktualisierung: April 2026**
**Nächste planmäßige Aktualisierung: Oktober 2026**
