---
titel: "Marine-Diesel — Grundlagen und Funktionsprinzip"
kategorie: "Motoren und Antrieb"
unterkategorie: "Marine-Diesel Grundlagen"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_01 — Marine-Diesel — Grundlagen und Funktionsprinzip

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Viertakt-Diesel Funktionsprinzip](#2-viertakt-diesel-funktionsprinzip)
3. [Marinisierung — Vom Industriemotor zum Schiffsantrieb](#3-marinisierung--vom-industriemotor-zum-schiffsantrieb)
4. [Leistungskurven und Drehmoment](#4-leistungskurven-und-drehmoment)
5. [Hubraum, Zylinder und Verdichtung](#5-hubraum-zylinder-und-verdichtung)
6. [Einspritzsysteme — Common-Rail vs. mechanisch](#6-einspritzsysteme--common-rail-vs-mechanisch)
7. [Turbolader und Saugmotoren](#7-turbolader-und-saugmotoren)
8. [Motorlagerung und Ausrichtung](#8-motorlagerung-und-ausrichtung)
9. [Betriebsstunden als Verschleißindikator](#9-betriebsstunden-als-verschleißindikator)
10. [Motormanagement und Diagnose](#10-motormanagement-und-diagnose)
11. [Emissionsvorschriften](#11-emissionsvorschriften)
12. [Motorauswahl nach Bootsgröße und -typ](#12-motorauswahl-nach-bootsgröße-und--typ)
13. [Hersteller und Modellübersicht](#13-hersteller-und-modellübersicht)
14. [Fehlerbild-Atlas](#14-fehlerbild-atlas)
15. [Troubleshooting](#15-troubleshooting)
16. [FAQ](#16-faq)
17. [Glossar](#17-glossar)
18. [Schnell-Referenz](#18-schnell-referenz)
19. [ANHANG A–H: Fallstudien](#19-anhang-ah-fallstudien)
20. [ANHANG I–R: Pydantic v2 Datenmodelle](#20-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Warum der Dieselmotor den maritimen Antrieb dominiert

Der Dieselmotor ist seit über einem Jahrhundert die vorherrschende
Antriebsquelle für Wasserfahrzeuge aller Größenklassen — vom 6-Meter-Fischerboot
bis zum Mega-Containerschiff. In der Sportschifffahrt und im Yachtbau hat der
Dieselmotor den Benzinmotor nahezu vollständig verdrängt, und das aus
guten Gründen:

- **Sicherheit**: Diesel ist nicht explosiv. Benzindämpfe in Bilgen sind eine
  der häufigsten Ursachen für Bootsexplosionen. Dieselkraftstoff entzündet
  sich erst ab ~55 °C Flammpunkt (Benzin: −20 °C).
- **Zuverlässigkeit**: Dieselmotoren haben keine Zündanlage (Kerzen, Verteiler,
  Zündspulen), die versagen kann. Die Selbstzündung durch Verdichtung
  eliminiert eine komplette Fehlerquelle.
- **Effizienz**: Dieselmotoren arbeiten mit 35–45 % thermischem Wirkungsgrad,
  Benzinmotoren nur mit 25–35 %. Das bedeutet 20–30 % weniger
  Kraftstoffverbrauch bei gleicher Leistung.
- **Drehmoment**: Dieselmotoren liefern hohes Drehmoment bei niedrigen
  Drehzahlen — ideal für den Propellerantrieb, der maximale Effizienz
  bei 1.500–3.000 U/min erreicht.
- **Langlebigkeit**: Marine-Diesel sind für 6.000–20.000 Betriebsstunden
  ausgelegt. Bei sachgemäßer Wartung erreichen viele Motoren 10.000+
  Stunden ohne Grundüberholung.

**Marktstatistik 2025:**
- >95 % aller Segelyachten >8 m haben Dieselantrieb
- >90 % aller Motorboote >7 m fahren mit Diesel
- Elektrische/hybride Antriebe wachsen, haben aber erst ~3 % Marktanteil
- Außenbord-Diesel wachsen im Segment 150–300 PS (OXE, Cox, Yanmar)

### 1.2 Geschichte des Marine-Diesels

Die Entwicklung des Dieselmotors für maritime Anwendungen verlief in
markanten Phasen:

- **1893**: Rudolf Diesel patentiert den Selbstzündungsmotor
- **1903**: Erstes dieselmotorbetriebenes Schiff (Petit Pierre, Frankreich)
- **1912**: MS Selandia — erstes ozeangehendes Motorschiff mit Diesel
- **1930er**: Erste Marine-Diesel für Yachten (schwer, laut, unzuverlässig)
- **1950er**: Perkins, BMC und Volvo Penta beginnen mit marinisierten
  Automobilmotoren — leichter, erschwinglicher
- **1960er**: Yanmar entwickelt kompakte Marine-Diesel speziell für Yachten
- **1970er**: Ölkrise treibt Dieselisierung der Freizeitschifffahrt
- **1980er**: Turbolader in Marine-Diesel, Saildrive-Systeme von Volvo Penta
- **1990er**: Elektronische Einspritzung beginnt bei größeren Motoren
- **2000er**: Common-Rail-Dieselmotoren werden Standard ab 100 PS
- **2010er**: EU Stage IIIA/IV Emissionsvorschriften erzwingen Abgasnachbehandlung
- **2020er**: EU Stage V, hybride Ergänzungssysteme, erste elektrische Alternativen

### 1.3 Diesel vs. Benzin im maritimen Einsatz

| Merkmal | Marine-Diesel | Marine-Benzin |
|---------|:---:|:---:|
| Flammpunkt | 55 °C | −20 °C |
| Explosionsgefahr | Minimal | Hoch |
| Spezifischer Verbrauch | 200–240 g/kWh | 280–350 g/kWh |
| Thermischer Wirkungsgrad | 35–45 % | 25–35 % |
| Typische Lebensdauer | 6.000–20.000 h | 1.500–3.000 h |
| Gewicht/PS | 3–6 kg/PS | 1,5–3 kg/PS |
| Anschaffungspreis | Höher | Niedriger |
| Wartungskosten/h | 3–8 EUR | 5–12 EUR |
| Drehmoment bei Nenndrehzahl | Sehr hoch | Mittel |
| Max. Drehzahl | 2.400–4.200 U/min | 4.000–6.000 U/min |
| Zündanlage | Keine (Selbstzündung) | Erforderlich |
| Hauptmarkt | >7 m Einbau | <7 m Außenborder |

### 1.4 Einsatzprofile und Belastungscharakteristik

Marine-Diesel werden in unterschiedlichen Regimen betrieben:

**Segelboote (Hilfsantrieb):**
- Typisch 100–400 Betriebsstunden/Jahr
- Belastung: 30–60 % der Nennleistung
- Häufiges An/Aus, kurze Laufzeiten
- Hauptrisiko: Unterlast → Verglasung der Zylinder

**Motoryachten (Hauptantrieb):**
- Typisch 200–800 Betriebsstunden/Jahr
- Belastung: 50–80 % der Nennleistung
- Längere Laufzeiten, gleichmäßigere Belastung
- Hauptrisiko: Überhitzung bei Verdrängerfahrt im Sommer

**Verdränger/Trawler:**
- Typisch 500–1.500 Betriebsstunden/Jahr
- Belastung: 60–75 % der Nennleistung
- Lange, gleichmäßige Laufzeiten — ideal für Dieselmotoren
- Hauptrisiko: Kraftstoffverschmutzung bei großen Tanks

**Charter/Beruflich:**
- Typisch 1.000–3.000 Betriebsstunden/Jahr
- Belastung: variabel, oft Volllast
- Höchste Anforderungen an Zuverlässigkeit
- Hauptrisiko: Wartungsstau durch Betreiberwechsel

### 1.5 Begriffliche Grundlagen

In der Marine-Diesel-Welt werden spezifische Begriffe verwendet, die
sich teilweise vom Automobil-Sprachgebrauch unterscheiden:

- **PS / HP / kW**: 1 PS = 0,7355 kW. Marine-Leistungsangaben nach
  ISO 8665 (mit Getriebe und Lüfter, ohne Auspuff-Gegendruck).
- **Nenndrehzahl**: Die Drehzahl bei Nennleistung (Vollgas unter Last).
- **Leerlaufdrehzahl**: Typisch 600–900 U/min.
- **Propellerkurve**: Leistungsbedarf des Propellers steigt mit der
  dritten Potenz der Drehzahl (P ∝ n³).
- **Betriebsstunden**: Primärer Verschleißindikator, analog zu km beim Auto.
  1 Betriebsstunde ≈ 50 km Autofahrt.
- **Marinisierung**: Anpassung eines Industriemotors für den Schiffseinsatz.
- **Saildrive**: Alternative zum Wellenantrieb bei Segelyachten, Motor
  treibt direkt ein unterwasserliegendes Getriebe an.

---
---

## 2. Viertakt-Diesel Funktionsprinzip

### 2.1 Die vier Arbeitstakte

Der Marine-Viertaktdiesel arbeitet nach dem gleichen Grundprinzip wie
sein terrestrisches Pendant, jedoch mit marine-spezifischen Anpassungen:

**Takt 1 — Ansaugen (0°–180° Kurbelwinkel)**
- Kolben bewegt sich vom oberen Totpunkt (OT) zum unteren Totpunkt (UT)
- Einlassventil öffnet, Frischluft wird angesaugt
- Bei Saugmotoren: Atmosphärendruck (~1 bar)
- Bei Turbomotoren: Ladedruck (1,5–2,5 bar absolut)
- Einlassventil schließt nach UT (Nachladung)
- Marine-Besonderheit: Ansaugluft aus dem Maschinenraum, daher
  ausreichende Belüftung kritisch (min. 0,05 m² freie Fläche)

**Takt 2 — Verdichten (180°–360° Kurbelwinkel)**
- Kolben bewegt sich von UT nach OT
- Beide Ventile geschlossen
- Luft wird auf 1/15 bis 1/23 des Ausgangsvolumens komprimiert
- Verdichtungsverhältnis Marine-Diesel: 15:1 bis 23:1
- Temperatur steigt auf 700–900 °C
- Druck steigt auf 30–50 bar
- Marine-Besonderheit: Höhere Verdichtung als PKW-Diesel üblich,
  da zuverlässige Kaltstartfähigkeit in feuchter Umgebung kritisch

**Takt 3 — Verbrennen/Arbeiten (360°–540° Kurbelwinkel)**
- Kurz vor OT: Kraftstoffeinspritzung (ca. 10–20° vor OT)
- Kraftstoff zündet durch Hitze und Druck (Selbstzündung)
- Verbrennungsdruck steigt auf 60–180 bar (je nach Motor)
- Kolben wird nach UT gedrückt — Arbeitstakt
- Energieumwandlung: chemisch → thermisch → mechanisch
- Marine-Besonderheit: Einspritzcharakteristik ist auf konstante
  Drehzahl unter Propellerlast optimiert, nicht auf Beschleunigung

**Takt 4 — Ausstoßen (540°–720° Kurbelwinkel)**
- Auslassventil öffnet kurz vor UT
- Kolben drückt Abgase aus dem Zylinder
- Abgastemperatur: 350–550 °C (Volllast)
- Bei Turbomotoren: Abgase treiben Turbinenrad an
- Marine-Besonderheit: Abgase werden nach der Turbine/dem Krümmer
  mit Kühlwasser gemischt (Nassauspuff) → Temperatur sinkt auf
  50–70 °C → Gummischlauch als Auspuffleitung möglich

### 2.2 Ventilsteuerung und Nockenwelle

Marine-Diesel verwenden in der Regel OHV- (Overhead Valve) oder
OHC-Ventilsteuerung (Overhead Cam):

**OHV (Stoßstangen-Ventilsteuerung):**
- Nockenwelle im Motorblock
- Stößel → Stoßstange → Kipphebel → Ventil
- Robust, wartungsfreundlich
- Typisch bei: Yanmar JH/YM, Beta Marine, Nanni, Vetus
- Ventilspiel einstellbar mit Fühlerlehre

**OHC (Obenliegende Nockenwelle):**
- Nockenwelle im Zylinderkopf, Antrieb über Kette oder Zahnriemen
- Direkter Ventilantrieb, weniger bewegte Teile
- Leiser, höhere Drehzahlen möglich
- Typisch bei: Volvo Penta D-Serie, modernen Yanmar 4LV
- Zahnriemenwechsel: kritischer Wartungspunkt

**Ventilspiel — Marine-Richtwerte:**

| Motor-Typ | Einlass (kalt) | Auslass (kalt) |
|-----------|:---:|:---:|
| Yanmar 3JH (OHV) | 0,20 mm | 0,20 mm |
| Yanmar 4JH (OHV) | 0,20 mm | 0,20 mm |
| Yanmar 4LV (OHC) | 0,15 mm | 0,25 mm |
| Volvo Penta D1 (OHV) | 0,20 mm | 0,20 mm |
| Volvo Penta D2 (OHC) | 0,20 mm | 0,35 mm |
| Beta Marine 25 (OHV) | 0,15 mm | 0,15 mm |
| Nanni N3.21 (OHV) | 0,20 mm | 0,20 mm |
| Sole Mini-29 (OHV) | 0,20 mm | 0,20 mm |

**Wichtig:** Ventilspiel immer bei kaltem Motor einstellen (< 40 °C).
Falsches Ventilspiel ist eine der häufigsten vermeidbaren Fehlerursachen
bei Marine-Diesel.

### 2.3 Kraftstoffsystem — Überblick

Der Kraftstoffweg in einem Marine-Diesel:

```
Tank → Absperrhahn → Vorfilter/Wasserabscheider (Racor, Separ)
  → Förderpumpe (mechanisch oder elektrisch)
  → Feinfilter (am Motor)
  → Hochdruck-Einspritzpumpe (oder Common-Rail-Pumpe)
  → Einspritzdüsen → Zylinder

Rücklauf: Düsen → Rücklaufleitung → Tank
```

**Kraftstoff-Spezifikation:**
- Marine-Diesel verwendet EN 590 Diesel (gleich wie PKW)
- Cetanzahl: min. 45, besser >50
- Schwefelgehalt: max. 10 ppm (EU seit 2009)
- Biodiesel-Anteil: max. 7 % (B7) — Problematik bei Lagerung
- Winterdiesel: CFPP −20 °C (wichtig für Winterlager mit Kraftstoff)

**Häufige Kraftstoffprobleme im Marinebetrieb:**

1. **Dieselpest** (Mikrobiologische Kontamination)
   - Bakterien und Pilze wachsen an der Wasser-Diesel-Grenzschicht
   - Schwarz-braune Schlammbildung, verstopfte Filter
   - Prävention: Wasser regelmäßig ablassen, Biozid (Grotamar 82)
   - Kosten bei Befall: 500–3.000 EUR (Tankreinigung)

2. **Wasseransammlung**
   - Kondensation in teilgefüllten Tanks
   - Undichte Tankdeckel, defekte Belüftung
   - Prävention: Tanks möglichst voll halten
   - Erkennung: Racor-Wasserabscheider mit Schauglas

3. **Alterung/Oxidation**
   - Diesel wird nach 6–12 Monaten instabil
   - Paraffin-Ausflockung, Harzbildung
   - Prävention: Kraftstoffstabilisator (z. B. Sta-bil Marine)
   - Umwälzung: mindestens alle 6 Monate Motor laufen lassen

### 2.4 Schmierung — Öl als Lebensversicherung

Das Schmiersystem eines Marine-Diesels ist kritischer als bei PKW,
da der Motor häufig unter Last startet und unter widrigen Bedingungen
(Feuchtigkeit, Salzluft, lange Standzeiten) arbeitet.

**Ölkreislauf:**
```
Ölwanne → Ölpumpe (Zahnradpumpe, mechanisch angetrieben)
  → Ölfilter → Ölkühler (Wasser-Öl-Wärmetauscher)
  → Hauptölkanal → Kurbelwellenlager → Pleuellager
  → Nockenwellenlager → Kipphebel/Ventilführungen
  → Rücklauf in Ölwanne
```

**Öl-Spezifikationen für Marine-Diesel:**

| Anwendung | API-Klasse | ACEA-Klasse | Viskosität |
|-----------|:---:|:---:|:---:|
| Saugmotor, gemäßigtes Klima | CI-4 oder CK-4 | E7 | 15W-40 |
| Saugmotor, tropisches Klima | CI-4 oder CK-4 | E7 | 15W-40 oder 20W-50 |
| Turbomotor | CK-4 | E9 | 15W-40 |
| Moderner Common-Rail | CK-4 oder FA-4 | C5 | 5W-30 oder 10W-40 |
| Winterlager / Kaltwasser | CI-4 | E7 | 10W-40 |

**Ölwechselintervalle Marine:**

| Motorhersteller | Intervall (Stunden) | Intervall (Zeit) |
|-----------------|:---:|:---:|
| Yanmar | 150–250 h | 1× jährlich |
| Volvo Penta | 200 h | 1× jährlich |
| Beta Marine | 200 h | 1× jährlich |
| Nanni | 200 h | 1× jährlich |
| Vetus | 150 h | 1× jährlich |
| Sole | 200 h | 1× jährlich |
| Baudouin | 250 h | 1× jährlich |
| Caterpillar | 250–500 h | 1× jährlich |

**Ölverbrauch — Richtwerte:**
- Neuer Motor: 0,1–0,5 g/kWh
- Eingelaufen (500+ h): 0,2–0,8 g/kWh
- Grenzwert: >1,5 g/kWh → Ursachenforschung
- >3,0 g/kWh → Motor muss überholt werden

### 2.5 Arbeitsspiel — Zusammenwirken aller Systeme

Ein vollständiges Arbeitsspiel (720° Kurbelwinkel) erfordert das
präzise Zusammenwirken von:

1. **Mechanik**: Kolben, Pleuel, Kurbelwelle, Schwungrad
2. **Kraftstoff**: Einspritzung zur richtigen Zeit, richtige Menge
3. **Luft**: Ausreichend Frischluft, ggf. verdichtet (Turbo)
4. **Kühlung**: Motortemperatur im Fenster 75–95 °C
5. **Schmierung**: Öldruck > 1,5 bar im Leerlauf, > 3 bar unter Last
6. **Abgas**: Freier Abfluss, korrekter Gegendruck

Versagt ein System, leidet der gesamte Motor. Die häufigste
Ausfallursache bei Marine-Diesel ist nicht mechanisches Versagen,
sondern **Vernachlässigung eines Hilfssystems** — insbesondere
Kühlung und Kraftstoff.

---
---

## 3. Marinisierung — Vom Industriemotor zum Schiffsantrieb

### 3.1 Was bedeutet Marinisierung?

Die meisten Marine-Diesel basieren auf Industriemotoren (Traktor,
Generator, Baumaschine), die für den Marineeinsatz angepasst werden.
Nur wenige Hersteller (Yanmar, Nanni) entwickeln Motoren primär für
den Marineeinsatz.

Die Marinisierung umfasst sechs Kernsysteme:

1. **Kühlsystem**: Umstellung auf Seewasser-/Frischwasserkühlung
2. **Auspuffsystem**: Nassauspuff statt Trockenanlage
3. **Lichtmaschine**: Größere Lichtmaschine für Bordnetz
4. **Getriebe**: Marine-Wendegetriebe statt Fahrzeuggetriebe
5. **Motorlagerung**: Flexible Lagerung für Vibrationsdämpfung
6. **Korrosionsschutz**: Opferanoden, marinisierte Oberflächen

### 3.2 Kühlsystem — Rohwasserkühlung und Wärmetauscher

Das Kühlsystem ist die wichtigste Marinisierungskomponente und
die häufigste Ausfallursache bei Marine-Diesel.

**Einkreis-Kühlung (Rohwasser direkt):**
- Seewasser fließt direkt durch den Motorblock
- Nur noch bei sehr alten Motoren oder einfachen Arbeitsbooten
- Vorteil: Einfach, günstig
- Nachteil: Korrosion, Salzablagerungen, keine Thermostatregelung
- Betriebstemperatur: 45–60 °C (zu kalt für effizienten Betrieb)

**Zweikreis-Kühlung (Wärmetauscher) — Standard seit 1990er:**

```
Primärkreis (geschlossen):
  Frischwasser + Frostschutz → Wasserpumpe (mechanisch)
  → Motorblock → Zylinderkopf → Thermostat
  → Wärmetauscher → zurück zur Pumpe

Sekundärkreis (offen):
  Seewasser → Seeventil → Seewasserfilter (Sieb)
  → Impellerpumpe (Gummilaufrad)
  → Wärmetauscher → Ölkühler → Ladeluftkühler (Turbo)
  → Abgaskrümmer/Mischkammer → Nassauspuff → über Bord
```

**Primärkreis-Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| Kühlmittel | 50 % Ethylenglykol + 50 % destilliertes Wasser |
| Frostschutz bis | −37 °C (50/50 Mischung) |
| Siedepunkt (unter Druck) | ~125 °C |
| Systemdruck | 0,5–1,0 bar |
| Thermostat-Öffnung | 71–82 °C (herstellerabhängig) |
| Betriebstemperatur | 75–95 °C |
| Alarmtemperatur | 100–105 °C |
| Volumen Primärkreis | 3–15 Liter (je nach Motor) |
| Kühlmittelwechsel | Alle 2 Jahre oder 500 h |

**Impellerpumpe — Das Herz der Seewasserkühlung:**

Die Impellerpumpe ist das verschleißanfälligste Bauteil im Marine-Diesel.
Ein Gummi-Impeller (Flügelrad) fördert Seewasser durch den Kühlkreis.

| Parameter | Richtwert |
|-----------|-----------|
| Lebensdauer Impeller | 300–600 h oder 2 Jahre |
| Wechselintervall | Jährlich (Empfehlung AYDI) |
| Ersatzimpeller an Bord | Mindestens 1, besser 2 |
| Materialien | Neopren (Standard), Nitril (höhere Temperatur) |
| Trockenlauf-Toleranz | Max. 30 Sekunden (dann Schaden!) |
| Typische Hersteller | Jabsco, Johnson, Sherwood, Oberdorfer |
| Preis Impeller | 25–80 EUR |
| Preis Pumpe komplett | 180–650 EUR |

**Wärmetauscher-Typen:**

| Typ | Beschreibung | Einsatz |
|-----|-------------|---------|
| Rohrbündel | Seewasser durch Rohre, Kühlmittel außen | Standard bei kleinen Motoren |
| Plattenwärmetauscher | Gestapelte Platten, gegenläufig | Kompakt, hohe Effizienz |
| Rohr-in-Rohr | Zwei konzentrische Rohre | Ölkühler, Ladeluftkühler |

**Häufige Kühlsystemprobleme:**

| Problem | Häufigkeit | Ursache |
|---------|:---:|---------|
| Impeller defekt | 30 % | Alterung, Trockenlauf |
| Seewasserfilter verstopft | 20 % | Algen, Muscheln, Plastik |
| Thermostat defekt | 15 % | Alterung, Korrosion |
| Wärmetauscher verkalkt | 10 % | Kalkablagerung (Süßwasser) |
| Wärmetauscher korrodiert | 8 % | Opferanoden nicht getauscht |
| Kühlmittelverlust | 7 % | Undichte Schläuche, Deckel |
| Impellerflügel im System | 5 % | Impellerbruch, Teile verstopfen Kanäle |
| Zinkanode aufgelöst | 5 % | Galvanische Korrosion |

### 3.3 Nassauspuff-System (Wet Exhaust)

Das Nassauspuff-System ist eine marine-spezifische Lösung:
Heiße Abgase werden mit dem Kühlwasser-Rücklauf gemischt und
durch einen Gummischlauch über Bord geleitet.

**Komponenten:**

```
Abgaskrümmer (Guss oder Edelstahl, wassergekühlt)
  → Mischkammer / Wassereinspritzwinkel
  → Nassauspuff-Schlauch (hitzebeständiger Gummi, 90 mm–150 mm)
  → Wassersammelkasten (Waterlock / Muffler)
  → Schwanenhalsbogen (höher als Wasserlinie!)
  → Anti-Siphon-Ventil
  → Borddurchlass (Seeventil oder offenes Rohr)
```

**Kritische Auslegungsregeln:**

1. **Schwanenhals**: Scheitelpunkt mindestens 300 mm über Wasserlinie
   bei maximaler Krängung
2. **Anti-Siphon-Ventil**: Verhindert Seewasser-Rückfluss in den Motor
   bei Stillstand. Position: höchster Punkt im System
3. **Steigung**: Auspuffschlauch muss durchgehend nach achtern/unten
   führen — keine Tiefpunkte, wo Wasser stehen bleibt
4. **Wassersammelkasten**: Volumen ≥ 2× Seewassermenge zwischen
   Impellerpumpe und Mischkammer
5. **Abgaskrümmer-Kühlung**: Krümmertemperatur max. 250 °C an der
   Außenfläche, Wassertemperatur am Krümmerausgang 60–80 °C

**Auspuffkrümmer-Lebensdauer:**

| Material | Lebensdauer | Preis |
|----------|:---:|:---:|
| Grauguss, wassergekühlt | 5–15 Jahre | 300–800 EUR |
| Edelstahl 316L | 15–25+ Jahre | 800–2.500 EUR |
| Aluminium (Volvo Penta) | 3–8 Jahre | 400–1.200 EUR |

**Volvo Penta Aluminium-Krümmer** sind berüchtigt für frühzeitigen
Ausfall durch Innere Korrosion. AYDI empfiehlt: Nach 5 Jahren
jährlich visuell und per Druckprüfung kontrollieren.

### 3.4 Lichtmaschine (Marine Alternator)

Marine-Lichtmaschinen unterscheiden sich von Kfz-Lichtmaschinen:

| Parameter | Kfz | Marine |
|-----------|:---:|:---:|
| Ausgangsleistung | 80–180 A | 50–200 A |
| Auslegung | Kurze Volllast | Dauerleistung |
| Korrosionsschutz | Minimal | Tropikalisiert, lackiert |
| Spannungsregler | Intern, einfach | Extern, mehrstufig möglich |
| Riemenantrieb | Keilrippenriemen | Keilriemen oder Keilrippenriemen |
| Betriebstemperatur | Umgebungsluft | Maschinenraum 50–70 °C |

**Ladetechnik-Stufen:**

| Stufe | Spannung (12 V) | Spannung (24 V) | Zweck |
|-------|:---:|:---:|---------|
| Bulk | 14,2–14,8 V | 28,4–29,6 V | Schnellladen bis 80 % |
| Absorption | 14,2–14,4 V | 28,4–28,8 V | Vollladen auf ~95 % |
| Float | 13,2–13,6 V | 26,4–27,2 V | Erhaltungsladen |

**Empfehlung AYDI:** Externer Mehrstufen-Regler (z. B. Balmar MC-614,
Sterling PDAR, Mastervolt Alpha Pro III) für optimale Batterieladung.
Die meisten internen Regler laden nur bis ~80 % und überkochen bei
langer Fahrt die Batterie.

**Wichtige Hersteller Marine-Lichtmaschinen:**

| Hersteller | Leistungsbereich | Besonderheit | Preis |
|------------|:---:|---|:---:|
| Balmar (USA) | 60–200 A | Premium, externe Regler | 800–2.500 EUR |
| Mastervolt | 80–175 A | Integrierte Ladetechnik | 900–2.200 EUR |
| Valeo Marine | 60–150 A | OEM bei vielen Herstellern | 400–1.200 EUR |
| Bosch Marine | 65–150 A | Standardqualität | 350–900 EUR |
| Prestolite | 80–200 A | Hochleistung, US-Markt | 700–1.800 EUR |

### 3.5 Marine-Wendegetriebe (Gearbox)

Das Marine-Wendegetriebe übersetzt die Motordrehzahl auf die
Propellerdrehzahl und ermöglicht Vorwärts-/Rückwärtsfahrt.

**Getriebearten:**

| Typ | Beschreibung | Einsatz |
|-----|-------------|---------|
| Mechanisch (Lamelle) | Handschaltung über Bowdenzug | Segelboote <15 m |
| Hydraulisch | Öldruckbetätigung | Motoryachten >12 m |
| Saildrive | Motor-Getriebe-Einheit mit Unterwasserantrieb | Segelboote (Volvo, Yanmar) |

**Typische Untersetzungsverhältnisse:**

| Bootstyp | Untersetzung | Propellerdrehzahl |
|----------|:---:|:---:|
| Segelboot 8–10 m | 2,14:1 – 2,62:1 | 900–1.400 U/min |
| Segelboot 11–14 m | 2,21:1 – 3,06:1 | 800–1.200 U/min |
| Motorboot Gleiter | 1,50:1 – 2,00:1 | 1.500–2.800 U/min |
| Motoryacht Verdränger | 2,50:1 – 3,50:1 | 700–1.100 U/min |
| Trawler | 3,00:1 – 4,00:1 | 500–900 U/min |

**Wichtige Getriebe-Hersteller:**

| Hersteller | Leistungsbereich | Typische Einsätze | Preis |
|------------|:---:|---|:---:|
| ZF Marine | 10–2.000 PS | Alle Bootstypen | 1.500–25.000 EUR |
| Hurth (ZF) | 10–200 PS | Segelboote, kleine Motorboote | 1.200–4.000 EUR |
| PRM (Newage) | 10–300 PS | Preisbewusste Eigner | 800–5.000 EUR |
| Technodrive | 10–250 PS | Mittelklasse | 1.000–4.500 EUR |
| Volvo Penta (Saildrive) | 10–80 PS | Segelyachten | 3.000–8.000 EUR |
| Yanmar (Saildrive) | 15–75 PS | Segelyachten | 2.800–7.500 EUR |

**Getriebeöl — Spezifikationen:**

| Hersteller | Empfohlenes Öl | Wechselintervall |
|------------|---|:---:|
| ZF Marine | ZF Marine Transmission Oil (ATF) | 500 h oder 2 Jahre |
| Hurth | ATF Dexron III oder ZF Marine | 500 h oder 2 Jahre |
| PRM | ATF Dexron III | 500 h oder 2 Jahre |
| Volvo Penta Saildrive | Volvo Penta 75W-90 Synthetic | 200 h oder 1 Jahr |
| Yanmar Saildrive | SAE 90 GL-4 | 200 h oder 1 Jahr |

### 3.6 Saildrive vs. Wellenantrieb

**Saildrive:**
- Motor-Getriebe-Einheit, Propeller direkt unter dem Motor
- Vorteil: Kein Wellenlager, keine Stopfbuchse, weniger Vibrationen
- Nachteil: Teurer, Manschette ist Verschleißteil (10 Jahre Lebensdauer),
  Wartung aufwändiger
- Hersteller: Volvo Penta (S-Drive 120/130/150), Yanmar (SD20–SD60)
- Manschettenwechsel: ca. 1.500–3.500 EUR (Material + Arbeit)

**Wellenantrieb:**
- Klassisch: Motor → Getriebe → Propellerwelle → Stopfbuchse → Propeller
- Vorteil: Günstiger, bewährt, einfach zu warten
- Nachteil: Wellenlager, Stopfbuchse, Motorausrichtung kritisch
- Typisch bei: Motorbooten, Trawlern, größeren Segelyachten

**Entscheidungshilfe:**

| Kriterium | Saildrive | Wellenantrieb |
|-----------|:---:|:---:|
| Installation | Einfacher (Werft) | Komplexer |
| Vibration | Geringer | Höher (wenn schlecht ausgerichtet) |
| Effizienz | ~3 % besser (keine Wellenlager) | Standard |
| Wartungskosten/Jahr | 200–400 EUR | 100–250 EUR |
| Manschette/Stopfbuchse | 10 Jahre / 1.500–3.500 EUR | Jährlich nachziehen / 50–200 EUR |
| Reparatur auf See | Schwierig | Einfacher |
| Maximalleistung | ~80 PS (Saildrive-Limit) | Unbegrenzt |

---
---

## 4. Leistungskurven und Drehmoment

### 4.1 Die Propellerkurve — Fundamentale Beziehung

Die wichtigste Kurve im Marine-Dieselbetrieb ist die Propellerkurve.
Sie beschreibt den Leistungsbedarf des Propellers in Abhängigkeit
von der Drehzahl:

```
P_prop = k × n³

P_prop = benötigte Leistung (kW)
k = Propellerkonstante (abhängig von Durchmesser, Steigung, Bootsform)
n = Drehzahl (U/min)
```

**Praktische Bedeutung:**
- Doppelte Drehzahl = 8× Leistungsbedarf
- 10 % mehr Drehzahl = 33 % mehr Leistungsbedarf
- Ein bewachsener Rumpf erhöht k um 10–30 % → Motor erreicht
  Nenndrehzahl nicht mehr

### 4.2 Motorleistungskurven — Typische Verläufe

**Drehmoment-Verlauf Marine-Diesel:**

| Drehzahlbereich | Drehmoment | Verhalten |
|:---:|:---:|---------|
| Leerlauf (600–900) | 30–50 % | Steigend |
| 1.000–1.500 U/min | 70–90 % | Starker Anstieg |
| 1.500–2.500 U/min | 90–100 % | Plateau (maximales Drehmoment) |
| 2.500–3.000 U/min | 85–95 % | Leicht fallend |
| >3.000 U/min | 75–85 % | Deutlich fallend |

**Maximales Drehmoment typischer Marine-Diesel:**

| Motor | Leistung | Max. Drehmoment | bei Drehzahl |
|-------|:---:|:---:|:---:|
| Yanmar 1GM10 | 9 PS / 6,6 kW | 19,6 Nm | 2.200 U/min |
| Yanmar 3JH40 | 40 PS / 29 kW | 88 Nm | 2.500 U/min |
| Yanmar 4JH80 | 80 PS / 59 kW | 175 Nm | 2.500 U/min |
| Volvo Penta D1-20 | 19 PS / 14 kW | 46 Nm | 2.200 U/min |
| Volvo Penta D2-40 | 38 PS / 28 kW | 93 Nm | 2.200 U/min |
| Volvo Penta D2-75 | 75 PS / 55 kW | 171 Nm | 2.500 U/min |
| Beta Marine 25 | 23 PS / 17 kW | 55 Nm | 2.400 U/min |
| Beta Marine 50 | 50 PS / 37 kW | 119 Nm | 2.400 U/min |
| Nanni N3.21 | 21 PS / 15 kW | 50 Nm | 2.200 U/min |
| Nanni N4.60 | 60 PS / 44 kW | 142 Nm | 2.400 U/min |
| Sole Mini-29 | 27 PS / 20 kW | 64 Nm | 2.200 U/min |
| Sole Mini-55 | 52 PS / 38 kW | 125 Nm | 2.400 U/min |

### 4.3 Leistungsmessung — ISO 8665

Die Nennleistung eines Marine-Diesels wird nach ISO 8665 angegeben:

- Mit montiertem Getriebe (Verlust ~3–5 %)
- Mit Lichtmaschine und Wasserpumpe
- Ohne Auspuff-Gegendruck
- Bei 25 °C Ansauglufttemperatur, 100 kPa Luftdruck
- Kraftstoff nach ISO 8178 (Referenzkraftstoff)

**Leistungskorrekturfaktoren:**

| Bedingung | Korrektur |
|-----------|:---:|
| Pro 10 °C über 25 °C Ansaugluft | −2 % |
| Pro 1.000 m Höhe über NN | −3 % |
| Verschmutzter Luftfilter | −3 bis −8 % |
| Alter Motor (5.000+ h) | −5 bis −15 % |
| Biologisch verschmutzter Kraftstoff | −5 bis −20 % |

### 4.4 Betriebspunkte und Motorbelastung

**Empfohlene Dauerleistung:**

| Einsatz | Dauer-% der Nennleistung | Nenndrehzahl-% |
|---------|:---:|:---:|
| Dauerbetrieb (Langfahrt) | 60–75 % | 80–87 % |
| Marschfahrt | 50–65 % | 75–82 % |
| Manövrieren | 20–40 % | 50–70 % |
| Laden (Generator) | 50–70 % | 75–85 % |
| Maximal (kurzzeitig) | 100 % | 100 % |
| Überlast (NICHT empfohlen) | >100 % | >100 % |

**Goldene Regel:** Marine-Diesel bei 75–80 % der Nenndrehzahl
betreiben. Dies optimiert Lebensdauer, Verbrauch und Emissionen.

### 4.5 Spezifischer Kraftstoffverbrauch (SFC)

| Motortyp | SFC bei Nennleistung | SFC optimal (60-75 %) |
|----------|:---:|:---:|
| Saugmotor, mechanisch | 230–260 g/kWh | 220–240 g/kWh |
| Saugmotor, Common-Rail | 215–240 g/kWh | 200–220 g/kWh |
| Turbomotor, mechanisch | 210–240 g/kWh | 195–220 g/kWh |
| Turbomotor, Common-Rail | 195–220 g/kWh | 185–205 g/kWh |

**Praxis-Verbrauchsrechnung:**
```
Verbrauch [l/h] = Leistung [kW] × SFC [g/kWh] / Diesel-Dichte [~830 g/l]

Beispiel: 40 kW Motor bei 75 % Last (30 kW), SFC 230 g/kWh
  → 30 × 230 / 830 = 8,3 l/h

Tagesverbrauch bei 8 h Fahrt: 66,4 Liter
Kosten bei 1,85 EUR/l: 123 EUR/Tag
Reichweite mit 300 l Tank: ~36 h / ~290 sm bei 8 kn
```

---
---

## 5. Hubraum, Zylinder und Verdichtung

### 5.1 Hubräume im Überblick

Marine-Diesel decken einen enormen Hubraumbereich ab:

| Leistungsklasse | Hubraum | Zylinder | Typische Motoren |
|:---:|:---:|:---:|---|
| 8–15 PS | 300–500 cm³ | 1 | Yanmar 1GM10, Vetus M2.06 |
| 15–30 PS | 500–1.100 cm³ | 2 | Yanmar 2YM20, Volvo D1-20, Beta 20 |
| 25–45 PS | 800–1.600 cm³ | 2–3 | Yanmar 3JH40, Volvo D1-30, Nanni N3.30 |
| 40–60 PS | 1.200–2.200 cm³ | 3–4 | Yanmar 3JH57, Volvo D2-50, Beta 50 |
| 55–80 PS | 1.600–2.500 cm³ | 4 | Yanmar 4JH80, Volvo D2-75, Sole Mini-62 |
| 75–150 PS | 2.000–4.000 cm³ | 4 | Yanmar 4LV150, Volvo D3-150 |
| 100–300 PS | 3.000–6.000 cm³ | 4–6 | Volvo D4-300, Yanmar 6LY |
| 200–500 PS | 5.000–10.000 cm³ | 6 | Volvo D6-480, Cat C7.1 |
| 400–1.000 PS | 8.000–18.000 cm³ | 6–8 | Cat C12.9, Baudouin 12M26 |

### 5.2 Zylinderanordnungen

| Anordnung | Zylinderzahl | Vorteile | Nachteile | Marine-Einsatz |
|-----------|:---:|---|---|---|
| Reihe | 1–6 | Einfach, kompakt | Vibriert bei 1–3 Zylindern | Am häufigsten |
| V-Form | 6, 8 | Kurz, hohe Leistung | Breiter, komplexer | >300 PS |
| Gegenläufer (Boxer) | 2 | Vibrationsarm | Breit, selten | Beta Marine (selten) |

### 5.3 Verdichtungsverhältnis

Das Verdichtungsverhältnis bestimmt:
- Thermischen Wirkungsgrad (höher = effizienter)
- Verbrennungsdruck (höher = mehr Belastung)
- Kaltstartverhalten (höher = besserer Kaltstart)
- Laufruhe (höher = härtere Verbrennung)

**Typische Verdichtungsverhältnisse:**

| Motortyp | Verdichtung | Besonderheit |
|----------|:---:|---------|
| Marine-Saugmotor (alt) | 18:1 – 20:1 | Robust, einfach |
| Marine-Saugmotor (modern) | 20:1 – 23:1 | Besserer Wirkungsgrad |
| Marine-Turbodiesel | 15:1 – 18:1 | Niedrigere Verdichtung da Ladedruck |
| Marine-Common-Rail | 16:1 – 18:1 | Elektronisch optimiert |
| PKW-Diesel (Vergleich) | 14:1 – 17:1 | Niedrig wegen Emissionen |

### 5.4 Bohrung und Hub

**Bohrung/Hub-Verhältnis:**

| Typ | Verhältnis B/H | Eigenschaft | Marine-Einsatz |
|-----|:---:|---------|---------|
| Kurzhuber | >1,0 | Hohe Drehzahl, weniger Drehmoment | Schnelle Motorboote |
| Quadratisch | ~1,0 | Ausgewogen | Allround |
| Langhuber | <1,0 | Hohes Drehmoment, niedrige Drehzahl | Verdränger, Segelboote |

**Beispiele:**

| Motor | Bohrung | Hub | B/H | Typ |
|-------|:---:|:---:|:---:|:---:|
| Yanmar 3JH40 | 88 mm | 90 mm | 0,98 | Quadratisch |
| Yanmar 4JH80 | 84 mm | 90 mm | 0,93 | Leicht Langhub |
| Volvo Penta D1-20 | 76 mm | 80 mm | 0,95 | Quadratisch |
| Volvo Penta D2-75 | 84 mm | 90 mm | 0,93 | Leicht Langhub |
| Beta Marine 25 | 78 mm | 84,5 mm | 0,92 | Leicht Langhub |
| Nanni N3.21 | 76 mm | 80 mm | 0,95 | Quadratisch |
| Sole Mini-29 | 80 mm | 82 mm | 0,98 | Quadratisch |
| Cat C7.1 | 105 mm | 135 mm | 0,78 | Langhub |
| Baudouin 6M26 | 150 mm | 150 mm | 1,00 | Quadratisch |

### 5.5 Kolben und Kolbenringe

**Kolbenbauformen im Marine-Diesel:**

| Typ | Material | Einsatz |
|-----|----------|---------|
| Aluminium-Legierung | AlSi12Cu | Standard bis 100 PS |
| Aluminium mit Eiseneinlage | AlSi + Fe Ring | Mittlere Motoren |
| Stahl-Kolben | Vergütungsstahl | Großmotoren >300 PS |

**Kolbenringe — Anordnung (typisch 3 Ringe):**

1. **Kompressionsring 1** (oben): Dichtet Verbrennungsdruck ab.
   Material: Chrom-beschichteter Stahl
2. **Kompressionsring 2** (Mitte): Zusätzliche Abdichtung + Ölabstreifung.
   Material: Stahl oder Guss
3. **Ölabstreifring** (unten): Reguliert den Ölfilm auf der Zylinderwand.
   Material: Federstahl mit Chromfläche

**Verschleißgrenzen:**

| Parameter | Neuwert | Verschleißgrenze |
|-----------|:---:|:---:|
| Kolbenringspalt (Stoßspiel) | 0,20–0,35 mm | 1,0–1,5 mm |
| Kolbenringaxialspiel | 0,04–0,08 mm | 0,15–0,20 mm |
| Zylinderverschleiß | 0 | 0,1–0,15 mm/1.000 h |
| Kolbenspiel | 0,05–0,10 mm | 0,20–0,30 mm |

---
---

## 6. Einspritzsysteme — Common-Rail vs. mechanisch

### 6.1 Mechanische Einspritzung — Bewährt und robust

Die mechanische Einspritzung verwendet eine vom Motor angetriebene
Einspritzpumpe, die den Kraftstoff unter hohem Druck zu den
Einspritzdüsen fördert.

**Reiheneinspritzpumpe (typisch bei älteren Motoren):**
- Eine Pumpe pro Zylinder, in Reihe angeordnet
- Antrieb über Nockenwelle
- Förderbeginn mechanisch eingestellt
- Drücke: 150–400 bar
- Hersteller: Bosch, Zexel, Denso

**Verteilereinspritzpumpe (typisch bei kleinen Motoren):**
- Eine Pumpe für alle Zylinder
- Verteiler rotiert und teilt den Kraftstoff zu
- Kompakter, leichter, günstiger
- Drücke: 150–350 bar
- Hersteller: Bosch VE, Denso, Delphi/CAV

**Vorteile mechanischer Einspritzung:**
- Kein Elektronikbedarf (kein Strom zum Laufen nach dem Start)
- Reparatur mit Bordmitteln möglich
- Ersatzteile weltweit verfügbar
- Bewährt über Jahrzehnte
- Kein Software-Update nötig

**Nachteile:**
- Höherer Kraftstoffverbrauch (5–15 % gegenüber Common-Rail)
- Höhere Emissionen
- Rauerer Lauf (Nageln)
- Einspritzcharakteristik nicht variabel
- Einstellarbeiten erfordern Erfahrung und Spezialwerkzeug

### 6.2 Common-Rail — Moderne Einspritztechnik

Common-Rail (CR) trennt Druckerzeugung und Einspritzung:
Eine Hochdruckpumpe erzeugt konstant hohen Druck in einer
gemeinsamen Leitung (Rail), die Einspritzdüsen (Injektoren)
werden elektronisch angesteuert.

**Funktionsweise:**

```
Förderpumpe → Hochdruckpumpe → Rail (Druckspeicher)
                                  ↓
  ECU (Motorsteuergerät) → steuert Injektoren
                                  ↓
  Injektor öffnet → Kraftstoff in Zylinder
  (mehrere Einspritzungen pro Arbeitstakt möglich)
```

**Einspritzdrücke Common-Rail:**

| Generation | Druck (bar) | Einführung | Marine-Einsatz |
|:---:|:---:|:---:|---|
| CR 1 | 1.350 | ~2003 | Volvo D3/D4, Yanmar BY |
| CR 2 | 1.600–1.800 | ~2008 | Volvo D4/D6 neu, Cat C7.1 |
| CR 3 | 2.000–2.200 | ~2013 | Volvo D8/D13, MAN |
| CR 4 | 2.500 | ~2018 | Große Motoren >500 PS |

**Einspritzmuster Common-Rail:**

| Phase | Zeitpunkt | Menge | Zweck |
|-------|:---:|:---:|---------|
| Voreinspritzung 1 | −20° KW | 1–2 mg | Vorwärmung, Geräuschreduktion |
| Voreinspritzung 2 | −10° KW | 2–3 mg | Druckaufbau, sanftere Zündung |
| Haupteinspritzung | −5° bis +15° KW | 20–60 mg | Leistungserzeugung |
| Nacheinspritzung 1 | +15° KW | 2–5 mg | Nachbrenner, Rußabbau |
| Nacheinspritzung 2 | +40° KW | 1–3 mg | DPF-Regeneration (falls vorhanden) |

**Vorteile Common-Rail:**
- 5–15 % weniger Kraftstoffverbrauch
- Deutlich leiser (kein Nageln)
- Niedrigere Emissionen (EU Stage V möglich)
- Variable Einspritzung nach Betriebspunkt
- Diagnose über OBD / CAN-Bus
- Einfacherer Einbau (keine mechanische Einspritzpumpe)

**Nachteile:**
- Abhängig von funktionierender Elektronik
- Höhere Empfindlichkeit gegenüber Kraftstoffqualität
- Injektoren teuer (400–1.200 EUR/Stück)
- Hochdruckpumpe teuer (1.500–4.000 EUR)
- Reparatur nur durch autorisierte Werkstatt
- Software-Updates nur beim Händler
- Kraftstoff-Filtration muss <5 µm sein (statt 10–30 µm bei mechanisch)

### 6.3 Vergleich Einspritzsysteme — Zusammenfassung

| Kriterium | Mechanisch | Common-Rail |
|-----------|:---:|:---:|
| Verbrauch | Basis | −5 bis −15 % |
| Emissionen | EU Stage IIIA max. | EU Stage V möglich |
| Geräusch | Lauter (Nageln) | Deutlich leiser |
| Zuverlässigkeit | Sehr hoch | Hoch |
| Reparierbarkeit vor Ort | Gut | Eingeschränkt |
| Kraftstoffqualität | Tolerant | Empfindlich |
| Anschaffungspreis | Basis | +15–25 % |
| Wartungskosten | Niedrig | Mittel–Hoch |
| Lebensdauer Injektoren | 5.000–10.000 h | 3.000–6.000 h |
| Elektronikbedarf | Minimal | Voll |
| Diagnosemöglichkeit | Manuell | CAN-Bus / OBD |

### 6.4 Glühkerzen und Kaltstarthilfe

Marine-Diesel benötigen bei niedrigen Temperaturen eine Kaltstarthilfe.
Im Gegensatz zu PKW-Diesel ist die Vorglühzeit bei Marine-Diesel
länger und die Bedingungen (Feuchtigkeit, Kälte) extremer.

**Glühkerzen-Typen:**

| Typ | Aufheizzeit | Nachglühzeit | Einsatz |
|-----|:---:|:---:|---------|
| Metall (Standard) | 10–30 s | 30–120 s | Yanmar, Beta, Nanni |
| Keramik (SiN) | 3–7 s | 120–300 s | Volvo Penta (neuere) |
| Stabglühkerze | 5–15 s | 60–180 s | Sole, Vetus |

**Kaltstartverhalten nach Temperatur:**

| Temperatur | Vorglühzeit | Startverhalten |
|:---:|:---:|---------|
| >20 °C | 5–10 s | Sofortstart |
| 10–20 °C | 10–15 s | Normaler Start |
| 0–10 °C | 15–25 s | Verlängertes Vorglühen |
| −10 bis 0 °C | 25–45 s | Mehrfaches Vorglühen |
| < −10 °C | 30–60 s | Standheizung/Blockheizung empfohlen |

**Empfehlung AYDI:** Bei Winterlager in kalten Regionen:
Motorvorwärmer (Calix, Defa) installieren. Kosten: 150–400 EUR.
Schont den Motor massiv beim Kaltstart.

---
---

## 7. Turbolader und Saugmotoren

### 7.1 Saugmotor (Naturally Aspirated)

Der Saugmotor bezieht seine Verbrennungsluft allein aus dem
Umgebungsdruck. Er ist die einfachere und robustere Bauart.

**Vorteile Saugmotor:**
- Einfacher Aufbau, weniger Bauteile
- Sofortige Gasannahme (kein Turboloch)
- Günstiger in Anschaffung und Wartung
- Höhere Verdichtung möglich
- Längere Lebensdauer (typisch 8.000–15.000 h)
- Geringere thermische Belastung
- Ideal für Segelboote (kurze Lasten, häufiges An/Aus)

**Nachteile:**
- Geringere spezifische Leistung (PS/Liter)
- Höheres Gewicht pro PS
- Höherer Verbrauch pro PS
- Leistungsverlust in warmer/feuchter Luft

**Typische Saugmotoren im Yachtbau:**

| Motor | Zylinder | Hubraum | Leistung | Gewicht |
|-------|:---:|:---:|:---:|:---:|
| Yanmar 1GM10 | 1 | 330 cm³ | 9 PS | 42 kg |
| Yanmar 2YM20 | 2 | 570 cm³ | 20 PS | 78 kg |
| Yanmar 3JH40 | 3 | 1.642 cm³ | 40 PS | 150 kg |
| Yanmar 4JH57 | 4 | 2.190 cm³ | 57 PS | 210 kg |
| Volvo Penta D1-13 | 2 | 570 cm³ | 12 PS | 79 kg |
| Volvo Penta D1-30 | 3 | 854 cm³ | 28 PS | 120 kg |
| Volvo Penta D2-40 | 4 | 1.131 cm³ | 38 PS | 157 kg |
| Beta Marine 14 | 2 | 570 cm³ | 14 PS | 75 kg |
| Beta Marine 25 | 3 | 854 cm³ | 23 PS | 108 kg |
| Beta Marine 38 | 3 | 1.131 cm³ | 38 PS | 135 kg |
| Nanni N2.14 | 2 | 570 cm³ | 14 PS | 80 kg |
| Nanni N3.21 | 3 | 854 cm³ | 21 PS | 115 kg |
| Sole Mini-17 | 2 | 616 cm³ | 16 PS | 85 kg |
| Sole Mini-29 | 3 | 1.028 cm³ | 27 PS | 125 kg |
| Vetus M2.06 | 1 | 395 cm³ | 6 PS | 52 kg |
| Vetus M3.28 | 3 | 854 cm³ | 28 PS | 122 kg |

### 7.2 Turbodiesel

Der Turbolader nutzt die Energie der Abgase, um die Ansaugluft
zu verdichten und damit die Zylinderfüllung zu erhöhen.

**Turbolader-Funktion:**

```
Abgase (350–550 °C, 0,5–2 bar Überdruck)
  → Turbinenrad (100.000–250.000 U/min)
  → gemeinsame Welle
  → Verdichterrad
  → Ladeluft (1,5–2,5 bar absolut, 80–150 °C)
  → Ladeluftkühler (Luft-Luft oder Wasser-Luft)
  → Ansaugkrümmer (40–60 °C nach Kühlung)
```

**Vorteile Turbolader:**
- 30–50 % mehr Leistung aus gleichem Hubraum
- Bessere spezifische Leistung (PS/kg)
- Niedrigerer spezifischer Verbrauch
- Höheres Drehmoment bei niedrigen Drehzahlen
- Besseres Höhenverhalten (kompensiert Luftdruckabfall)

**Nachteile:**
- Turboloch bei schneller Lastannahme (0,5–2 s Verzögerung)
- Höhere thermische Belastung des Motors
- Turbolager ist Verschleißteil (Lebensdauer 3.000–8.000 h)
- Empfindlich gegen Ölmangel und verschmutztes Öl
- Nachlaufzeit nach Volllast beachten (1–2 Min. Leerlauf!)
- Teurer in der Wartung

**Turbolader-Hersteller im Marine-Bereich:**

| Hersteller | Einsatz | Typische Motoren |
|------------|---------|-----------------|
| Garrett (Honeywell) | Kleine/mittlere Motoren | Yanmar, Nanni, Sole |
| BorgWarner (3K) | Mittlere Motoren | Volvo Penta D3/D4 |
| IHI (Ishikawajima) | Yanmar-Motoren | Yanmar 4LV, 6LY |
| Holset (Cummins) | Große Motoren | Cummins QSB/QSC |
| MAN | Großmotoren | MAN D0836/D2876 |
| ABB | Superyacht-Motoren | Cat, MTU |

### 7.3 Ladeluftkühler

Der Ladeluftkühler (Intercooler) kühlt die vom Turbo verdichtete
Luft ab, bevor sie in den Motor gelangt:

- **Luft-Wasser-Kühler** (Marine-Standard): Kompakt, mit Seewasser gekühlt
- **Luft-Luft-Kühler**: Selten im Marineeinsatz (zu groß)

| Parameter | Ohne LLK | Mit LLK |
|-----------|:---:|:---:|
| Ladelufttemperatur | 120–180 °C | 40–60 °C |
| Zylinderfüllung | +30 % ggü. Sauger | +40–50 % ggü. Sauger |
| Leistungsgewinn durch LLK | Basis | +8–15 % |
| NOx-Emissionen | Höher | Niedriger |
| Thermische Belastung Motor | Höher | Geringer |

### 7.4 Turbo-Pflege und Lebensdauer

**Turbolader-Wartung:**

| Maßnahme | Intervall | Kosten |
|----------|:---:|:---:|
| Ölwechsel (verlängertes Intervall vermeiden!) | Wie Motor | inkl. |
| Ladeluftschläuche prüfen | 200 h / jährlich | 0 EUR |
| Ladeluftschläuche wechseln | 2.000 h / 5 Jahre | 50–200 EUR |
| Turbolager prüfen (Radialspiel) | 1.000 h / 3 Jahre | 50 EUR |
| Turbolader überholen | 3.000–6.000 h | 800–2.500 EUR |
| Turbolader ersetzen | Bei Versagen | 1.500–5.000 EUR |

**Turbo-Killer — Was den Turbolader zerstört:**

1. **Heißabstellen**: Motor unter Volllast abstellen → Restöl verkokt
   in den Lagern. Immer 1–2 Minuten Leerlauf vor dem Abstellen!
2. **Ölmangel**: Bereits 5 Sekunden ohne Öl beschädigt die Lager
3. **Verschmutztes Öl**: Ölwechselintervall überschritten
4. **Fremdkörper im Ansaugsystem**: Defekter Luftfilter
5. **Überdrehzahl**: Defektes Wastegate

---
---

## 8. Motorlagerung und Ausrichtung

### 8.1 Flexible Motorlagerung (Flexible Mounts)

Marine-Diesel werden auf elastischen Motorlagern montiert, um
Vibrationen vom Bootskörper zu entkoppeln.

**Motorlager-Typen:**

| Typ | Beschreibung | Einsatz | Preis/Stück |
|-----|-------------|---------|:---:|
| Standard-Gummilager | Vulkanisierte Gummi-Metall-Verbindung | Segelboote, leichte Motorboote | 30–80 EUR |
| Progressive Lager | Weich im Leerlauf, härter unter Last | Motoryachten | 50–120 EUR |
| Vetus Flex-Mount | Speziell für Vetus-Motoren | Vetus-Einbauten | 60–150 EUR |
| R&D Marine Flex | Hochwertig, lange Lebensdauer | Alle Motorgrößen | 80–200 EUR |
| Polyflex-Lager | Polyurethan statt Gummi | Leistungsmotoren | 100–250 EUR |
| Hydraulik-Lager | Flüssigkeitsgefüllt | Superyachten | 200–500 EUR |

**Motorlagerung — Konstruktionsprinzipien:**

1. **Vier-Punkt-Lagerung**: Standard bei den meisten Einbauten
2. **Lastverteilung**: Vorderlager tragen ~60 % (Schwungradseite),
   Hinterlager ~40 %
3. **Maximale Durchbiegung**: 3–5 mm unter Last (Shore-Härte 40–60)
4. **Lebensdauer**: 3.000–6.000 h oder 5–10 Jahre
5. **Kontrollintervall**: Jährlich visuell, alle 3 Jahre messen

**Anzeichen für verschlissene Motorlager:**
- Erhöhte Vibration im Boot
- Motor „wandert" auf dem Fundament
- Risse im Gummi sichtbar
- Ungleichmäßige Lagerbelastung (Motor steht schief)
- Ausrichtungsprobleme mit Propellerwelle

### 8.2 Motorausrichtung (Engine Alignment)

Die Ausrichtung (Alignment) des Motors zur Propellerwelle ist eine
der kritischsten Arbeiten bei der Motorinstallation und -wartung.

**Warum Ausrichtung so wichtig ist:**
- Fehlausrichtung > 0,1 mm → erhöhter Verschleiß an Kupplung und
  Wellenlagern
- Fehlausrichtung > 0,3 mm → deutliche Vibrationen, höherer Geräuschpegel
- Fehlausrichtung > 0,5 mm → Schäden an Getriebe, Stopfbuchse, Wellenanlage
  innerhalb von 100–500 h
- Fehlausrichtung > 1,0 mm → sofortige Schäden möglich

**Ausrichtungs-Arten:**

| Art | Beschreibung | Toleranz |
|-----|-------------|:---:|
| Angulare Fehlausrichtung | Winkelversatz zwischen Motor- und Wellenflansch | <0,05 mm/25 mm |
| Parallele Fehlausrichtung | Versatz der Wellenachsen zueinander | <0,1 mm |
| Axiale Position | Abstand zwischen Flanschen | 3–5 mm (herstellerspezifisch) |

**Ausrichtung prüfen — Methode mit Fühlerlehre:**

1. Motor abstellen, abkühlen lassen
2. Kupplungsflansche trennen (Schrauben lösen)
3. Flansche zusammenführen (ohne Schrauben)
4. Fühlerlehre an 4 Positionen (12, 3, 6, 9 Uhr) zwischen die Flansche
5. Differenz max. 0,05 mm bei 100 mm Flanschdurchmesser
6. Welle um 90° drehen und erneut messen
7. Bei Abweichung: Motorlager-Stellschrauben justieren

**Ausrichtung muss geprüft werden:**
- Nach Motoreinbau / Motorlagererwechsel
- Jährlich beim Winterlager (Boot an Land)
- Nach Grundberührung
- Bei neuen Vibrationen oder Geräuschen
- Nach Rumpfarbeiten (Osmosebehandlung, Kielung)

### 8.3 Motorfundament

Das Motorfundament überträgt die Motorlasten auf den Bootsrumpf.

**Materialien:**

| Material | Einsatz | Vorteile | Nachteile |
|----------|---------|----------|-----------|
| GFK-Laminat | Serienboote | Integral mit Rumpf, leicht | Delamination möglich |
| Stahlträger | Stahlboote | Fest, justierbar | Korrosion |
| Alu-Träger | Aluboote | Leicht, korrosionsbeständig | Elektrolyse-Risiko |
| Holz + GFK | Ältere GFK-Boote | Einfach zu bauen | Fäulnis bei Wassereinbruch |
| Epoxi/GFK-Composite | Hochwertige Yachten | Steif, leicht, langlebig | Teuer |

**Fundament-Anforderungen:**
- Steifigkeit > 3× Motorgewicht pro mm Durchbiegung
- Keine Resonanz mit Motorschwingungen
- Entwässerung der Bilge muss möglich bleiben
- Zugang zu Motorfüßen muss gewährleistet sein

---
---

## 9. Betriebsstunden als Verschleißindikator

### 9.1 Betriebsstunden — Der „Kilometerzähler" des Motors

Betriebsstunden sind der wichtigste Einzelindikator für den
Zustand eines Marine-Diesels.

**Umrechnungsfaktor zum Auto:**
- 1 Betriebsstunde ≈ 50 km Autofahrt (Durchschnitt)
- 1 Betriebsstunde ≈ 30 km unter Last (Volllast-Äquivalent)
- 5.000 Betriebsstunden ≈ 250.000 km Auto

### 9.2 Lebenserwartung nach Motortyp

| Motortyp | Bis Grundüberholung | Bis Austausch | Beispiele |
|----------|:---:|:---:|---|
| Saugmotor, mech. Einspritzung | 8.000–15.000 h | 15.000–25.000 h | Yanmar 3JH, Beta 25 |
| Saugmotor, Common-Rail | 6.000–12.000 h | 12.000–20.000 h | Yanmar 4JH-CR, Volvo D2 |
| Turbo, mech. Einspritzung | 6.000–10.000 h | 10.000–18.000 h | Ältere Volvo TMD |
| Turbo, Common-Rail | 5.000–8.000 h | 8.000–15.000 h | Volvo D3/D4, Cat C7.1 |
| Großmotor (>300 PS) | 10.000–20.000 h | 25.000–40.000 h | Cat C12.9, Baudouin |

### 9.3 Wartungsintervalle nach Betriebsstunden

**Standard-Wartungsplan Marine-Diesel:**

| Intervall | Maßnahmen |
|:---:|---------|
| 50 h (Einlauf) | Ölwechsel, Filter, Ventilspiel, Schrauben nachziehen |
| 100 h | Impeller prüfen, Riemenspannung, Kraftstofffilter |
| 200 h | Ölwechsel + Filter, Kraftstoff-Vorfilter |
| 500 h | Kühlmittel prüfen/ergänzen, Ventilspiel, Turbo-Kontrolle |
| 1.000 h | Große Inspektion: alle Filter, Kühlsystem spülen, Injektoren prüfen |
| 2.000 h | Impellerpumpe komplett, Thermostat, Zahnriemen (OHC) |
| 3.000 h | Injektoren überholen/tauschen, Turbo prüfen |
| 5.000 h | Motor-Grundinspektion: Kompression, Verschleiß, Lager |
| 8.000–10.000 h | Grundüberholung erwägen |

### 9.4 Betriebsstunden bei Gebrauchtkauf

**Bewertungstabelle für Gebrauchtmotoren:**

| Betriebsstunden | Zustandsklasse | Preisabschlag | Bemerkung |
|:---:|:---:|:---:|---------|
| 0–500 | Neuwertig | 0–10 % | Einlaufphase abgeschlossen |
| 500–2.000 | Sehr gut | 10–25 % | Bestes Lebensalter |
| 2.000–5.000 | Gut | 25–45 % | Normaler Verschleiß |
| 5.000–8.000 | Akzeptabel | 45–65 % | Erste größere Wartungen fällig |
| 8.000–12.000 | Grenzwertig | 65–80 % | Überholung wahrscheinlich |
| >12.000 | Überholungsbedürftig | 80–95 % | Nur mit Motorhistorie kaufen |

**Achtung:** Betriebsstundenzähler können manipuliert werden!
Folgende Indizien zeigen den wahren Zustand:

- Kompressionsmessung (>25 bar bei Saugmotor, <20 bar = Verschleiß)
- Ölanalyse (Metallabrieb zeigt tatsächlichen Verschleiß)
- Rostentwicklung am Abgaskrümmer
- Zustand der Anodenschrauben
- Optischer Zustand von Schläuchen und Kabeln
- Logbücher und Wartungsnachweise
- Zustand der Motorlager (Gummi-Alterung)

### 9.5 Betriebsstundenzähler — Einbau und Typen

| Typ | Funktion | Preis |
|-----|----------|:---:|
| Mechanisch (Hobbs-Meter) | Zählt bei laufendem Motor | 20–50 EUR |
| Elektrisch (Induktiv) | Zählt Motorumdrehungen | 30–80 EUR |
| Digital (GPS-gekoppelt) | Zählt + zeigt Motorparameter | 50–200 EUR |
| CAN-Bus (integriert) | Im Motormanagement integriert | Serienmäßig bei CR-Motoren |

---
---

## 10. Motormanagement und Diagnose

### 10.1 CAN-Bus im Marine-Diesel

Der CAN-Bus (Controller Area Network) ist das Standardprotokoll
für die Kommunikation zwischen elektronischen Steuergeräten
auf modernen Booten.

**CAN-Bus-Varianten im Marineeinsatz:**

| Protokoll | Standard | Einsatz |
|-----------|---------|---------|
| NMEA 2000 | IEC 61162-3 | Navigationsinstrumente, Displays |
| J1939 | SAE J1939 | Motor-Diagnose, Motorsteuerung |
| CANopen | CiA 301 | Industrielle Automation (selten Marine) |
| Proprietär | Herstellerspezifisch | Volvo EVC, Yanmar YEDI |

### 10.2 J1939 — Der Motor-Diagnosestandard

SAE J1939 ist der Industriestandard für die Kommunikation mit
Dieselmotoren. Alle modernen Marine-Diesel mit elektronischer
Einspritzung verwenden J1939.

**Wichtige J1939 Parameter Groups (PGN):**

| PGN | Parameter | Einheit |
|:---:|---------|---------|
| 61444 | Motordrehzahl | U/min |
| 65262 | Kühlmitteltemperatur | °C |
| 65263 | Öldruck | kPa |
| 65270 | Ansauglufttemperatur | °C |
| 65253 | Betriebsstunden | h |
| 65271 | Kraftstofftemperatur | °C |
| 65266 | Kraftstoffverbrauch | l/h |
| 65269 | Batteriesspannung | V |
| 65276 | Ladeluftdruck | kPa |
| 65279 | Abgastemperatur | °C |
| 65226 | Aktive Fehlercodes (DTC) | Code |
| 65227 | Gespeicherte Fehlercodes | Code |

### 10.3 Motorüberwachung — Alarmsysteme

**Standard-Motoralarme:**

| Parameter | Warnstufe | Alarmstufe | Abschaltstufe |
|-----------|:---:|:---:|:---:|
| Kühlmitteltemperatur | 95 °C | 100 °C | 105 °C |
| Öldruck (Leerlauf) | 1,2 bar | 0,8 bar | 0,5 bar |
| Öldruck (Nenndrehzahl) | 2,5 bar | 2,0 bar | 1,5 bar |
| Ladelufttemperatur | 60 °C | 70 °C | 80 °C |
| Abgastemperatur | 500 °C | 550 °C | 600 °C |
| Kühlmittelstand | Niedrig | — | — |
| Motordrehzahl (Über) | 3.600 U/min | 3.800 U/min | 4.000 U/min |

**AYDI empfiehlt:** Auch bei Motoren ohne elektronische Überwachung
nachträgliche Installation von:
- Kühlmittel-Temperaturalarm (30 EUR)
- Öldruck-Schalter (20 EUR)
- Auspufftemperatur-Sensor (50 EUR)
- Summermodul für alle drei Alarme (40 EUR)
- Gesamtkosten: ca. 150–250 EUR inkl. Einbau

### 10.4 Diagnose-Tools

**Herstellerspezifische Diagnose:**

| Hersteller | Diagnose-Tool | Kosten |
|------------|--------------|:---:|
| Volvo Penta | VODIA5 | ~5.000 EUR (nur Händler) |
| Yanmar | YEDI (Yanmar Engine Diagnostic Interface) | ~3.000 EUR |
| Caterpillar | CAT ET (Electronic Technician) | ~4.000 EUR |
| Cummins | INSITE | ~3.500 EUR |
| Nanni | Texa Marine | ~2.500 EUR |

**Universelle Diagnose-Tools:**

| Tool | Protokoll | Preis | Eignung |
|------|----------|:---:|---------|
| Actisense NGW-1 | NMEA 2000 ↔ J1939 | 300 EUR | Gateway für Displays |
| Maretron DSM250 | J1939 / NMEA 2000 | 900 EUR | Multifunktionsdisplay |
| Yacht Devices YDEG-04 | J1939 → NMEA 2000 | 150 EUR | Motorgateway |
| Noland Engineering | J1939 generisch | 200 EUR | Basisdiagnose |

### 10.5 Fernüberwachung und IoT

Moderne Marine-Diesel können über Mobilfunk/Satellit fernüberwacht werden:

| System | Hersteller | Funktionen | Kosten |
|--------|-----------|-----------|:---:|
| Volvo Penta Connect | Volvo Penta | Motor-Daten, Geofencing, Alarme | 500 EUR + 200 EUR/Jahr |
| Yanmar Remote Monitoring | Yanmar | Betriebsdaten, Fehlercodes | 400 EUR + 150 EUR/Jahr |
| Siren Marine | Unabhängig | GPS, Motor, Bilge, Batterie | 600 EUR + 250 EUR/Jahr |
| Yacht Sentinel | Unabhängig | Umfassend, eigene SIM | 800 EUR + 180 EUR/Jahr |
| Glomex ZigBoat | Unabhängig | GSM-basiert, einfach | 350 EUR + 120 EUR/Jahr |

---
---

## 11. Emissionsvorschriften

### 11.1 Überblick Emissionsregime

Drei wesentliche Regulierungsrahmen betreffen Marine-Diesel in der
Sportschifffahrt und kleinen Berufsschifffahrt:

| Regulierung | Geltungsbereich | Anwendung |
|-------------|----------------|-----------|
| EU Stage V (EU 2016/1628) | Europa | Ab 2019–2020, alle neuen Motoren 19–560 kW |
| EPA Tier 3 (40 CFR Part 1042) | USA | Ab 2014, alle neuen Motoren <600 kW |
| IMO Tier III (MARPOL Annex VI) | International | Ab 2016, Schiffe >500 GT in NECAs |

### 11.2 EU Stage V — Details

Die EU Stage V Verordnung (EU 2016/1628) ist seit 2019–2020 die
maßgebliche Emissionsnorm für neue Marine-Diesel in Europa.

**Grenzwerte EU Stage V (Inland Waterway / Recreational Craft):**

| Parameter | Grenzwert (19–37 kW) | Grenzwert (37–56 kW) | Grenzwert (56–130 kW) | Grenzwert (130–560 kW) |
|-----------|:---:|:---:|:---:|:---:|
| CO | 5,0 g/kWh | 5,0 g/kWh | 5,0 g/kWh | 3,5 g/kWh |
| HC + NOx | 7,5 g/kWh | 4,7 g/kWh | 5,4 g/kWh | 5,4 g/kWh |
| PM | 0,40 g/kWh | 0,015 g/kWh | 0,015 g/kWh | 0,015 g/kWh |
| PN | — | 1×10¹² | 1×10¹² | 1×10¹² |

**Technische Konsequenzen EU Stage V:**

| Maßnahme | Ab Leistung | Beschreibung |
|----------|:---:|---------|
| Common-Rail-Einspritzung | ~19 kW | Präzise Kraftstoffdosierung |
| Abgasrückführung (AGR) | ~37 kW | Reduziert NOx durch gekühltes Abgas |
| Dieselpartikelfilter (DPF) | ~37 kW | Fängt Rußpartikel auf |
| Dieseloxidationskatalysator (DOC) | ~37 kW | Oxidiert CO und HC |
| SCR (Selektive katalytische Reduktion) | ~130 kW | AdBlue/DEF reduziert NOx |

**Problematik für Bootseigner:**
- DPF-Regeneration erfordert hohe Abgastemperaturen (>400 °C)
- Bei Segelbooten (niedrige Last, kurze Laufzeiten) kann DPF nicht
  regenerieren → Verstopfung → teure Reinigung (500–1.500 EUR)
- SCR benötigt AdBlue-Tank und -Dosierung → Platz, Gewicht, Kosten
- Nachrüstung an Bestandsmotoren NICHT erforderlich

### 11.3 EPA Tier 3 — US-Vorschriften

EPA Tier 3 gilt für alle neuen Marine-Diesel unter 600 kW, die
in den USA verkauft oder betrieben werden.

**Grenzwerte EPA Tier 3 (Recreation Marine Diesel):**

| Parameter | Grenzwert (alle Leistungsklassen) |
|-----------|:---:|
| HC + NOx | 7,5 g/kWh (gewichtet) |
| CO | 5,0 g/kWh |
| PM | 0,40 g/kWh |

**Wesentliche Unterschiede zu EU Stage V:**
- Keine PN-Grenzwerte (Partikelanzahl)
- Generell weniger streng, insbesondere bei PM
- Kein DPF erforderlich für die meisten Leistungsklassen
- Kein SCR erforderlich unter 600 kW

### 11.4 IMO Tier III

IMO Tier III betrifft primär die kommerzielle Schifffahrt, ist aber
relevant für größere Motoryachten (>500 GT) in NOx Emission Control
Areas (NECAs).

**NOx-Grenzwerte IMO Tier III:**

| Drehzahl (n) | Grenzwert |
|:---:|:---:|
| n < 130 U/min | 3,4 g/kWh |
| 130 ≤ n < 2.000 U/min | 9 × n^(−0,2) g/kWh |
| n ≥ 2.000 U/min | 2,0 g/kWh |

### 11.5 Praxistipps Emissionen

**Für Bootseigner:**
1. Bestandsmotoren genießen Bestandsschutz — keine Nachrüstpflicht
2. EU Stage V Motoren sind 5.000–15.000 EUR teurer als Vorgänger
3. DPF-Motoren brauchen regelmäßige Volllastphasen (min. 30 Min.)
4. AdBlue/DEF gefriert bei −11 °C → beheizter Tank nötig
5. Wartungskosten steigen durch Abgasnachbehandlung um 20–40 %

**AYDI-Empfehlung für Segelboote <75 PS:**
Wenn möglich, EU Stage IIIA Motor wählen (Restbestände, gebrauchte
Motorisierungen). Einfacher, zuverlässiger, günstiger im Unterhalt.
Stage V Motoren sind technisch überdimensioniert für den typischen
Segelboot-Einsatz (200–400 h/Jahr, niedrige Last).

---
---

## 12. Motorauswahl nach Bootsgröße und -typ

### 12.1 Leistungsbedarf — Faustregeln

**Segelboote (Hilfsmotor):**

| Bootslänge | Verdrängung | Empfohlene Leistung | Typische Motoren |
|:---:|:---:|:---:|---|
| 6–8 m | 1–3 t | 8–15 PS | Yanmar 1GM10, Volvo D1-13 |
| 8–10 m | 3–6 t | 15–25 PS | Yanmar 2YM20, Beta 20, Nanni N2.14 |
| 10–12 m | 5–10 t | 25–40 PS | Yanmar 3JH40, Volvo D1-30, Sole Mini-29 |
| 12–14 m | 8–15 t | 40–60 PS | Yanmar 4JH57, Volvo D2-50, Beta 50 |
| 14–16 m | 12–22 t | 55–80 PS | Yanmar 4JH80, Volvo D2-75 |
| 16–18 m | 18–30 t | 75–120 PS | Yanmar 4LV80–150, Volvo D3-110 |
| 18–22 m | 25–50 t | 100–200 PS | Volvo D3-150/D4-180, Cat C2.2 |

**Motorboote (Gleiter):**

| Bootslänge | Verdrängung | Empfohlene Leistung | Typische Motoren |
|:---:|:---:|:---:|---|
| 6–8 m | 1–2,5 t | 100–200 PS | Yanmar 4LV, Volvo D3 |
| 8–10 m | 2–4 t | 200–350 PS | Volvo D4/D6, Yanmar 6LY |
| 10–13 m | 4–8 t | 300–600 PS | Volvo D6/D8, Cat C7.1 |
| 13–16 m | 6–12 t | 2× 250–500 PS | 2× Volvo D6, 2× Cat C7.1 |
| 16–20 m | 10–25 t | 2× 400–800 PS | 2× Volvo D8/D11, 2× Cat C12.9 |

**Motoryachten (Verdränger/Halbgleiter):**

| Bootslänge | Verdrängung | Empfohlene Leistung | Typische Motoren |
|:---:|:---:|:---:|---|
| 8–10 m | 4–8 t | 40–80 PS | Yanmar 4JH, Beta 50, Sole Mini-55 |
| 10–13 m | 8–15 t | 75–150 PS | Yanmar 4LV, Volvo D3, Nanni N4 |
| 13–16 m | 12–25 t | 120–250 PS | Volvo D4, Cat C4.4, Baudouin 4W105 |
| 16–20 m | 20–45 t | 2× 150–300 PS | 2× Volvo D4, 2× Baudouin |
| 20–24 m | 35–80 t | 2× 250–500 PS | 2× Volvo D6, 2× Cat C7.1 |

### 12.2 Motorauswahl-Checkliste

**Schritt 1 — Leistungsbedarf ermitteln:**
```
P_min = V_max³ × Verdrängung / C_p

P_min = Mindestleistung (kW)
V_max = gewünschte Maximalgeschwindigkeit (m/s)
Verdrängung = Verdrängung (kg)
C_p = Propulsionskoeffizient (500–800 für Verdränger, 200–400 für Gleiter)
```

**Schritt 2 — Einbaumaße prüfen:**

| Motor | Länge | Breite | Höhe |
|-------|:---:|:---:|:---:|
| Yanmar 1GM10 | 394 mm | 365 mm | 488 mm |
| Yanmar 3JH40 | 624 mm | 484 mm | 620 mm |
| Yanmar 4JH80 | 756 mm | 484 mm | 645 mm |
| Volvo Penta D1-20 | 595 mm | 420 mm | 550 mm |
| Volvo Penta D2-75 | 785 mm | 540 mm | 625 mm |
| Beta Marine 25 | 572 mm | 440 mm | 534 mm |
| Nanni N3.21 | 585 mm | 420 mm | 560 mm |
| Sole Mini-29 | 620 mm | 450 mm | 560 mm |

**Schritt 3 — Gewicht berücksichtigen:**
- Motor + Getriebe + Kühlwasser + Öl = Einbaugewicht
- Position beeinflusst Trimm und Stabilität
- Gewicht über Kojen/Salon: Einfluss auf Schwerpunkt prüfen

**Schritt 4 — Serviceinfrastruktur:**

| Hersteller | Servicenetz Europa | Servicenetz weltweit | Ersatzteil-Verfügbarkeit |
|------------|:---:|:---:|:---:|
| Volvo Penta | Sehr gut (★★★★★) | Sehr gut (★★★★★) | Sehr gut |
| Yanmar | Sehr gut (★★★★★) | Gut (★★★★) | Sehr gut |
| Beta Marine | Gut (★★★★) | Mäßig (★★★) | Gut |
| Nanni | Gut (★★★★) | Mäßig (★★★) | Gut |
| Sole | Gut (★★★★) | Mäßig (★★★) | Gut |
| Vetus | Gut (★★★★) | Mäßig (★★★) | Gut |
| Baudouin | Gut (★★★★) | Gut (★★★★) | Gut |
| Caterpillar | Sehr gut (★★★★★) | Sehr gut (★★★★★) | Sehr gut |

### 12.3 Preisübersicht Marine-Diesel (Stand 2025/26)

**Segelboot-Motoren (Saildrive oder Wellenantrieb):**

| Motor | Leistung | Preis (ohne Saildrive) | Preis (mit Saildrive) |
|-------|:---:|:---:|:---:|
| Yanmar 1GM10 | 9 PS | 3.800 EUR | — |
| Yanmar 2YM20 | 20 PS | 6.200 EUR | — |
| Yanmar 3JH40 | 40 PS | 10.500 EUR | 14.500 EUR |
| Yanmar 4JH57 | 57 PS | 14.800 EUR | 19.200 EUR |
| Yanmar 4JH80 | 80 PS | 18.500 EUR | 23.500 EUR |
| Volvo D1-20 | 19 PS | 6.800 EUR | 11.200 EUR |
| Volvo D1-30 | 28 PS | 8.500 EUR | 13.500 EUR |
| Volvo D2-40 | 38 PS | 11.200 EUR | 16.000 EUR |
| Volvo D2-50 | 47 PS | 13.500 EUR | 18.800 EUR |
| Volvo D2-75 | 75 PS | 18.000 EUR | 24.500 EUR |
| Beta Marine 14 | 14 PS | 4.200 EUR | — |
| Beta Marine 25 | 23 PS | 5.800 EUR | — |
| Beta Marine 38 | 38 PS | 8.500 EUR | — |
| Beta Marine 50 | 50 PS | 11.000 EUR | — |
| Nanni N2.14 | 14 PS | 5.200 EUR | — |
| Nanni N3.21 | 21 PS | 7.200 EUR | — |
| Nanni N4.60 | 60 PS | 15.500 EUR | — |
| Sole Mini-17 | 16 PS | 4.800 EUR | — |
| Sole Mini-29 | 27 PS | 6.800 EUR | — |
| Sole Mini-55 | 52 PS | 12.500 EUR | — |
| Vetus M2.06 | 6 PS | 3.200 EUR | — |
| Vetus M3.28 | 28 PS | 7.500 EUR | — |
| Vetus M4.35 | 33 PS | 9.200 EUR | — |

**Motoryacht-Motoren (höhere Leistungsklasse):**

| Motor | Leistung | Preis |
|-------|:---:|:---:|
| Yanmar 4LV150 | 150 PS | 28.000 EUR |
| Yanmar 4LV195 | 195 PS | 32.000 EUR |
| Yanmar 4LV250 | 250 PS | 38.000 EUR |
| Yanmar 6LY400 | 400 PS | 55.000 EUR |
| Yanmar 6LY440 | 440 PS | 62.000 EUR |
| Volvo D3-110 | 110 PS | 22.000 EUR |
| Volvo D3-150 | 150 PS | 28.000 EUR |
| Volvo D4-225 | 225 PS | 42.000 EUR |
| Volvo D4-300 | 300 PS | 52.000 EUR |
| Volvo D6-380 | 380 PS | 68.000 EUR |
| Volvo D6-480 | 480 PS | 82.000 EUR |
| Cat C4.4 | 168 PS | 35.000 EUR |
| Cat C7.1 | 425 PS | 75.000 EUR |
| Cat C7.1 | 507 PS | 88.000 EUR |
| Baudouin 4W105S | 160 PS | 28.000 EUR |
| Baudouin 6W105S | 240 PS | 38.000 EUR |
| Baudouin 6M26 | 500 PS | 72.000 EUR |

---
---

## 13. Hersteller und Modellübersicht

### 13.1 Yanmar — Der Segelbootmotor-Spezialist

**Unternehmen:**
- Gründung: 1912, Osaka, Japan
- Marine-Dieselproduktion seit 1933
- Weltweit führend im Segment Segelboot-Diesel (geschätzt >50 % Marktanteil)
- Eigene Marine-Motorentwicklung (nicht nur marinisierte Industriemotoren)

**Aktuelle Motorenreihen:**

| Reihe | Leistung | Zylinder | Einspritzung | Haupteinsatz |
|-------|:---:|:---:|:---:|---|
| 1GM10 | 9 PS | 1 | Mechanisch | Kleine Segelboote |
| 2YM20 | 20 PS | 2 | Mechanisch | Segelboote 8–9 m |
| 3JH40 | 40 PS | 3 | Common-Rail | Segelboote 10–12 m |
| 4JH57 | 57 PS | 4 | Common-Rail | Segelboote 12–14 m |
| 4JH80 | 80 PS | 4 | Common-Rail | Segelboote 14–17 m |
| 4JH110 | 110 PS | 4 | Common-Rail | Segelboote 16–20 m |
| 4LV150 | 150 PS | 4 | Common-Rail | Motorboote, Yachten |
| 4LV195 | 195 PS | 4 | Common-Rail | Motorboote, Yachten |
| 4LV250 | 250 PS | 4 | Common-Rail | Motorboote, Yachten |
| 6LY400 | 400 PS | 6 | Common-Rail | Schnelle Yachten |
| 6LY440 | 440 PS | 6 | Common-Rail | Schnelle Yachten |

**Stärken:** Kompakt, leicht, leise, sehr gute Ersatzteilverfügbarkeit,
bewährte Technik, gute Saildrive-Integration (SD20/SD25/SD40/SD50/SD60).

**Schwächen:** Premium-Preis, proprietäre Teile, YEDI-Diagnose nur beim Händler.

### 13.2 Volvo Penta — Der Allrounder

**Unternehmen:**
- Gründung: 1907, Göteborg, Schweden
- Teil der Volvo Group
- Marktführer im Sterndrive-Segment (Aquamatic)
- Starke Position bei Saildrives und Motoryacht-Motoren

**Aktuelle Motorenreihen:**

| Reihe | Leistung | Zylinder | Einspritzung | Haupteinsatz |
|-------|:---:|:---:|:---:|---|
| D1-13/20 | 12–19 PS | 2 | Mechanisch | Kleine Segelboote |
| D1-30 | 28 PS | 3 | Mechanisch | Segelboote 9–11 m |
| D2-40/50 | 38–47 PS | 4 | Mechanisch | Segelboote 10–13 m |
| D2-60/75 | 60–75 PS | 4 | Common-Rail | Segelboote 12–16 m |
| D3-110/150 | 110–150 PS | 4 | Common-Rail | Motorsegel, Motoryachten |
| D4-180/225/300 | 180–300 PS | 4 | Common-Rail | Motoryachten |
| D6-310/380/480 | 310–480 PS | 6 | Common-Rail | Schnelle Yachten |
| D8-510/600 | 510–600 PS | 8 | Common-Rail | Großyachten |

**Stärken:** Weltweites Servicenetz, EVC-System (Electronic Vessel Control),
Aquamatic-Antrieb, IPS-Pod-Antrieb, gute Integration.

**Schwächen:** Teuer (Ersatzteile bis 40 % über Drittanbietern),
Aluminium-Abgaskrümmer (frühzeitige Korrosion), proprietäres EVC-System,
VODIA-Diagnose nur beim Händler.

### 13.3 Beta Marine — Der britische Geheimtipp

**Unternehmen:**
- Gründung: 1987, Gloucester, England
- Marinisiert Kubota-Industriemotoren
- Bekannt für Qualität und fairen Preis
- Starke Fangemeinde in UK, wachsend in Europa

**Aktuelle Motorenreihen:**

| Modell | Leistung | Zylinder | Basis-Motor | Preis |
|--------|:---:|:---:|---|:---:|
| Beta 14 | 14 PS | 2 | Kubota Z482 | 4.200 EUR |
| Beta 20 | 20 PS | 3 | Kubota D722 | 5.200 EUR |
| Beta 25 | 23 PS | 3 | Kubota D902 | 5.800 EUR |
| Beta 30 | 28 PS | 3 | Kubota D1105 | 6.800 EUR |
| Beta 38 | 38 PS | 3 | Kubota V1505 | 8.500 EUR |
| Beta 43 | 42 PS | 4 | Kubota V1505-T | 9.800 EUR |
| Beta 50 | 50 PS | 4 | Kubota V2003-T | 11.000 EUR |
| Beta 60 | 60 PS | 4 | Kubota V2607-T | 13.500 EUR |
| Beta 75 | 75 PS | 4 | Kubota V3307-T | 16.000 EUR |
| Beta 90 | 90 PS | 4 | Kubota V3800-T | 19.000 EUR |
| Beta 115 | 115 PS | 4 | Kubota V3800-TIE | 24.000 EUR |
| Beta 150 | 150 PS | 4 | Kubota V3800-TIEF | 30.000 EUR |

**Stärken:** Gutes Preis-Leistungs-Verhältnis, Kubota-Basismotoren weltweit
erhältlich, gute Zugänglichkeit beim Einbau, solide Marinisierung.

**Schwächen:** Kein eigenes Saildrive, Servicenetz außerhalb UK dünn,
bei größeren Motoren erreicht Kubota-Basis ihre Grenzen.

### 13.4 Nanni — Der französische Marinisierungsspezialist

**Unternehmen:**
- Gründung: 1952, Marseille, Frankreich
- Marinisiert Kubota- und John-Deere-Motoren
- Stark im Mittelmeerraum, wachsend international

**Aktuelle Motorenreihen:**

| Modell | Leistung | Basis | Preis |
|--------|:---:|---|:---:|
| N2.10 | 10 PS | Kubota Z482 | 4.500 EUR |
| N2.14 | 14 PS | Kubota D722 | 5.200 EUR |
| N3.21 | 21 PS | Kubota D902 | 7.200 EUR |
| N3.30 | 30 PS | Kubota D1305 | 9.500 EUR |
| N4.40 | 40 PS | Kubota V2003 | 12.000 EUR |
| N4.50 | 50 PS | Kubota V2203-T | 14.500 EUR |
| N4.60 | 60 PS | Kubota V2607-T | 15.500 EUR |
| N4.80 | 80 PS | Kubota V3800-T | 20.000 EUR |
| N4.100 | 100 PS | John Deere 4045 | 25.000 EUR |
| N4.115 | 115 PS | John Deere 4045 | 28.000 EUR |

**Stärken:** Solide Marinisierung, guter Service in Südeuropa,
kompaktes Design.

**Schwächen:** Begrenzte Händlerdichte in Nordeuropa, proprietäre Teile.

### 13.5 Weitere wichtige Hersteller

**Vetus (Niederlande):**
- Marinisiert Mitsubishi-Motoren
- Breites Zubehörsortiment (Auspuff, Filter, Lichtmaschine)
- Preis: 3.200–22.000 EUR (6–120 PS)
- Vorteil: Komplettes System aus einer Hand

**Sole (Spanien):**
- Marinisiert Mitsubishi-Motoren
- Starke Präsenz in Südeuropa
- Preis: 4.800–45.000 EUR (16–300 PS)
- Vorteil: Robuste Motoren, guter Service in Spanien/Frankreich

**Baudouin (Frankreich):**
- Eigene Motorentwicklung (seit 1918)
- Seit 2009 Teil der Weichai-Gruppe (China)
- Schwerpunkt: 100–1.200 PS
- Preis: 28.000–180.000 EUR
- Vorteil: Preis-Leistung bei großen Motoren

**Caterpillar (USA):**
- Weltmarktführer bei Großmotoren
- Marine-Segment über Cat Marine Power
- Schwerpunkt: 100–6.000 PS
- Preis: 35.000–500.000+ EUR
- Vorteil: Weltweit beste Serviceinfrastruktur

---
---

## 14. Fehlerbild-Atlas

### 14.1 Übersicht Fehlermuster

| Nr. | Fehlerbild | Dringlichkeit | Häufigkeit |
|:---:|---------|:---:|:---:|
| F-18_01-01 | Motor springt nicht an | Hoch | Sehr häufig |
| F-18_01-02 | Motor geht unter Last aus | Hoch | Häufig |
| F-18_01-03 | Überhitzung | Kritisch | Häufig |
| F-18_01-04 | Schwarzer Rauch (Qualm) | Mittel | Häufig |
| F-18_01-05 | Weißer Rauch | Mittel–Hoch | Mittel |
| F-18_01-06 | Blauer Rauch | Mittel | Mittel |
| F-18_01-07 | Niedriger Öldruck | Kritisch | Mittel |
| F-18_01-08 | Abnormale Vibrationen | Mittel | Häufig |
| F-18_01-09 | Kraftstoff im Öl | Hoch | Selten |
| F-18_01-10 | Wasser im Öl | Kritisch | Selten |
| F-18_01-11 | Dieselnageln/Klopfen | Mittel | Mittel |
| F-18_01-12 | Motor erreicht Nenndrehzahl nicht | Mittel | Häufig |

---

### F-18_01-01 — Motor springt nicht an

**Symptom**: Starter dreht, Motor zündet nicht oder zündet kurz
und geht sofort wieder aus.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Kraftstoff-Absperrhahn geschlossen | 25 % |
| 2 | Luft im Kraftstoffsystem | 20 % |
| 3 | Kraftstofffilter verstopft / Dieselpest | 15 % |
| 4 | Glühkerzen defekt (bei Kälte) | 12 % |
| 5 | Batterie zu schwach (Starter dreht zu langsam) | 10 % |
| 6 | Motorstop-Zug gezogen / Abstellmagnet aktiv | 8 % |
| 7 | Wasser im Kraftstoff | 5 % |
| 8 | Injektoren defekt / verkohlt | 3 % |
| 9 | Kompression zu niedrig (Verschleiß) | 2 % |

**Sofortmaßnahmen:**
1. Kraftstoff-Absperrhahn prüfen — offen?
2. Motorstop-Zug und Gashebel prüfen
3. Batteriespannung prüfen (>12,0 V unter Last)
4. Glühkerzen vorglühen (15–30 Sekunden)
5. Racor-Vorfilter prüfen — Wasser ablassen
6. Kraftstoffsystem entlüften (Entlüftungsschraube)
7. Kraftstofffilter wechseln (Ersatzfilter immer an Bord!)
8. Startpilot NUR als letzte Maßnahme (Motorschaden möglich!)

**Langfristmaßnahmen:**
- Kraftstoffsystem regelmäßig entlüften
- Racor-Vorfilter mit Schauglas installieren
- Batterie im Winter laden oder abklemmen
- Kraftstoff stabilisieren (Sta-bil Marine)
- Glühkerzen alle 3.000 h wechseln

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Starter dreht hörbar, aber kein Auspuffrauch
- Kraftstofflache unter dem Motor (undichtes System)
- Verschmutzter/schwarzer Vorfilter sichtbar
- Korrodierte Batterieklemmen

---

### F-18_01-02 — Motor geht unter Last aus

**Symptom**: Motor läuft im Leerlauf, stirbt aber ab, wenn
Gang eingelegt oder Gas gegeben wird.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Kraftstoffzufuhr unzureichend (Filter, Leitung) | 30 % |
| 2 | Luft im Kraftstoffsystem (undichte Saugleitung) | 25 % |
| 3 | Propeller blockiert (Leine, Netz, Plastiktüte) | 15 % |
| 4 | Förderpumpe schwach | 10 % |
| 5 | Tank leer (Saugstutzen über Kraftstoffspiegel) | 8 % |
| 6 | Einspritzdüsen verschlissen | 7 % |
| 7 | Turbolader-Schaden (bei Turbomotor) | 3 % |
| 8 | Motorsteuergerät-Fehler (bei CR-Motor) | 2 % |

**Sofortmaßnahmen:**
1. Zurück in den Leerlauf, Motor stabil?
2. Kraftstoffstand prüfen
3. Vorfilter auf Luftblasen prüfen
4. Kraftstofffilter wechseln
5. Bei Propellerblockade: Motor AUS, tauchen und freiräumen
6. Kraftstoffsystem entlüften

**Langfristmaßnahmen:**
- Kraftstoffleitungen auf Undichtigkeit prüfen (Saugseite!)
- Doppeltes Kraftstofffilter-System installieren (Umschaltbar)
- Linenschneider am Propeller installieren
- Tankinhaltsmesser installieren/kalibrieren

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Luftblasen im durchsichtigen Kraftstoffschlauch
- Nasse/ölige Stellen an Kraftstoff-Verschraubungen
- Verschmutzter Kraftstofffilter
- Leine/Netz am Propeller (Unterwasserfoto)

---

### F-18_01-03 — Überhitzung

**Symptom**: Kühlmitteltemperatur steigt über 95 °C, Alarm löst aus.
Eventuell Dampfentwicklung.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Impeller defekt / Flügel abgebrochen | 30 % |
| 2 | Seewasserfilter verstopft (Algen, Plastik) | 20 % |
| 3 | Seeventil geschlossen oder verstopft | 12 % |
| 4 | Thermostat klemmt geschlossen | 10 % |
| 5 | Kühlmittel zu wenig (Leck im Primärkreis) | 8 % |
| 6 | Wärmetauscher verkalkt / verstopft | 7 % |
| 7 | Keilriemen/Antrieb Kühlwasserpumpe gerissen | 5 % |
| 8 | Auspuff-Rückstau (verstopfter Wassersammelkasten) | 4 % |
| 9 | Überlast (bewachsener Rumpf, falsche Propellersteigung) | 2 % |
| 10 | Zylinderkopfdichtung defekt | 2 % |

**Sofortmaßnahmen:**
1. Last reduzieren — Drehzahl auf Leerlauf
2. Seewasserfilter prüfen und reinigen
3. Seeventil prüfen — offen?
4. Seewasser-Austritt am Auspuff prüfen (fließt Wasser?)
5. Wenn kein Seewasser: Motor SOFORT abstellen!
6. Motor abkühlen lassen (15–20 Minuten)
7. Kühlmittelstand prüfen (Vorsicht: unter Druck!)
8. Impeller prüfen und ggf. wechseln

**Langfristmaßnahmen:**
- Impeller jährlich wechseln (Ersatz immer an Bord!)
- Seewasserfilter halbjährlich reinigen
- Wärmetauscher alle 3–5 Jahre reinigen lassen
- Opferanoden im Kühlsystem jährlich prüfen
- Auspuffkrümmer auf Innere Korrosion prüfen (Volvo!)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Dampf aus Motorraum
- Lack/Farbe verfärbt an heißen Stellen
- Aufgequollene Kühlschläuche
- Kein Wasserstrahl am Auspuff-Ausgang
- Zerstörter Impeller bei Demontage

---

### F-18_01-04 — Schwarzer Rauch (Qualm)

**Symptom**: Dichter schwarzer oder dunkelgrauer Rauch aus dem Auspuff,
besonders unter Last.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Luftfilter verschmutzt / verstopft | 25 % |
| 2 | Motorüberlastung (falscher Propeller, bewachsener Rumpf) | 20 % |
| 3 | Einspritzdüsen verschlissen (tropfen statt sprühen) | 18 % |
| 4 | Turbolader defekt (bei Turbomotor) | 12 % |
| 5 | Einspritzpumpe falsch eingestellt | 10 % |
| 6 | Ventilspiel falsch | 8 % |
| 7 | Kompression niedrig (Verschleiß) | 5 % |
| 8 | Ladeluftkühler verstopft | 2 % |

**Sofortmaßnahmen:**
1. Last reduzieren — weniger schwarzer Rauch?
2. Luftfilter prüfen / reinigen
3. Wenn nur unter Volllast: Propeller prüfen lassen
4. Turbomotor: Ladeluftschläuche auf Risse prüfen

**Langfristmaßnahmen:**
- Luftfilter regelmäßig reinigen/wechseln
- Einspritzdüsen alle 2.000–3.000 h prüfen lassen
- Ventilspiel alle 500 h einstellen
- Propellerdimensionierung überprüfen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Rußablagerungen um Auspuffausgang
- Schwarze Flecken auf Badeplattform/Spiegel
- Verschmutzter Luftfilter sichtbar
- Rissige Ladeluftschläuche

---

### F-18_01-05 — Weißer Rauch

**Symptom**: Weißer oder hellgrauer Rauch aus dem Auspuff, oft
mit süßlichem Geruch.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Motor noch kalt (normal bei Kaltstart, <3 Min.) | 30 % |
| 2 | Zylinderkopfdichtung undicht (Kühlmittel in Verbrennungsraum) | 25 % |
| 3 | Falscher Einspritzzeitpunkt (zu spät) | 15 % |
| 4 | Wasser im Kraftstoff | 12 % |
| 5 | Glühkerze defekt (einzelner Zylinder zündet nicht) | 10 % |
| 6 | Zylinderkopf gerissen | 5 % |
| 7 | Kompression zu niedrig | 3 % |

**Sofortmaßnahmen:**
1. Abwarten: Verschwindet der Rauch nach 3–5 Minuten Laufzeit?
2. Wenn weiterhin weißer Rauch: Kühlmittelstand prüfen (sinkt er?)
3. Auspuffkondensat auffangen — riecht nach Kühlmittel? → KZD defekt!
4. Ölmessstab ziehen: milchig-braune Emulsion = Wasser im Öl → STOP!

**Langfristmaßnahmen:**
- Kühlmittelstand bei kaltem Motor regelmäßig prüfen
- Ölfarbe bei jedem Ölwechsel begutachten
- Kompressionsmessung bei Verdacht auf KZD-Schaden
- Druckprüfung Kühlsystem (0,5 bar, 15 Minuten halten)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Dichter weißer Rauch auch bei warmem Motor
- Kühlmittel-Flecken unter Zylinderkopf
- Milchige Emulsion auf Ölmessstab
- Kühlmittelstand sinkt ohne sichtbares Leck

---

### F-18_01-06 — Blauer Rauch

**Symptom**: Bläulicher Rauch, besonders beim Starten und bei
Lastwechsel. Ölverbrauch erhöht.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Ventilschaftdichtungen verschlissen | 35 % |
| 2 | Kolbenringe verschlissen | 25 % |
| 3 | Turbolager verschlissen (Öl in Ladeluft) | 15 % |
| 4 | Zu viel Öl eingefüllt | 10 % |
| 5 | Kurbelgehäuseentlüftung verstopft | 8 % |
| 6 | Zylinderlaufbuchsen verschlissen | 5 % |
| 7 | Ventilführungen ausgeschlagen | 2 % |

**Sofortmaßnahmen:**
1. Ölstand prüfen — zu viel? Auf Markierung bringen
2. Kurbelgehäuseentlüftung prüfen (verstopft?)
3. Wenn nur beim Kaltstart: Ventilschaftdichtungen (weniger kritisch)
4. Wenn permanent: Ölverbrauch messen (pro 10 h)

**Langfristmaßnahmen:**
- Ventilschaftdichtungen erneuern (500–1.500 EUR)
- Kompressionstest: unter 20 bar → Kolbenringe prüfen
- Turbolager prüfen: Axialspiel > 0,15 mm → Turbo überholen
- Bei hohem Ölverbrauch (>1,5 g/kWh): Motor überholen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Bläulicher Dunst im Auspuff
- Ölfilm um Auspuffausgang
- Ölspuren am Turbolader-Ausgang
- Nasser/öliger Luftfilter

---

### F-18_01-07 — Niedriger Öldruck

**Symptom**: Öldruck-Warnanzeige leuchtet, Druckmesser zeigt
<1,5 bar im Leerlauf oder <3 bar unter Last.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Ölstand zu niedrig | 30 % |
| 2 | Falsches Öl (zu dünn für Betriebstemperatur) | 15 % |
| 3 | Ölfilter verstopft (Bypass öffnet) | 12 % |
| 4 | Öldrucksensor/Schalter defekt | 12 % |
| 5 | Ölpumpe verschlissen | 10 % |
| 6 | Kurbelwellenlager verschlissen | 8 % |
| 7 | Ölkühler undicht (intern) | 5 % |
| 8 | Überdruckventil klemmt offen | 5 % |
| 9 | Kraftstoff im Öl (Verdünnung) | 3 % |

**Sofortmaßnahmen:**
1. Motor SOFORT auf Leerlauf oder ABSTELLEN!
2. Ölstand prüfen — nachfüllen wenn nötig
3. Ölfarbe/-konsistenz prüfen (dünn = Kraftstoff drin, milchig = Wasser)
4. Öldrucksensor prüfen (mechanisches Manometer anschließen)
5. Wenn Öl OK und Druck wirklich niedrig: Motor NICHT starten!

**Langfristmaßnahmen:**
- Regelmäßige Ölstandskontrolle (alle 20 h oder wöchentlich)
- Korrekte Ölviskosität verwenden
- Ölfilter bei jedem Ölwechsel tauschen
- Ölanalyse alle 500 h (zeigt Lagerverschleiß früh an)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Ölwarnanzeige am Instrumentenpanel
- Ölverlust unter dem Motor / in der Bilge
- Ungewöhnliche Motorgeräusche (Klopfen, Rasseln)

---

### F-18_01-08 — Abnormale Vibrationen

**Symptom**: Ungewöhnliche Vibrationen, die vorher nicht vorhanden
waren. Kann drehzahlabhängig oder lastabhängig sein.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Propeller beschädigt (verbogen, abgebrochen) | 25 % |
| 2 | Motorlager verschlissen | 20 % |
| 3 | Motor-Wellenausrichtung defekt | 15 % |
| 4 | Leine/Netz am Propeller/Welle | 10 % |
| 5 | Ein Zylinder arbeitet nicht (Injektor, Ventil) | 10 % |
| 6 | Kupplung verschlissen (Getriebe) | 8 % |
| 7 | Schwungradschrauben locker | 5 % |
| 8 | Kardanwelle unwuchtig (bei V-Antrieb) | 4 % |
| 9 | Propellerwelle verbogen | 3 % |

**Sofortmaßnahmen:**
1. Drehzahl variieren — Vibration drehzahlabhängig?
2. Leerlauf ohne Gang: Vibration weg? → Propeller/Welle
3. Leerlauf mit Gang: Vibration? → Getriebe/Kupplung
4. Bestimmte Drehzahl: Resonanz → Motorlager

**Langfristmaßnahmen:**
- Propeller jährlich kontrollieren (visuell + dynamisch wuchten)
- Motorlager alle 3 Jahre prüfen und ggf. erneuern
- Ausrichtung bei jedem Winterlager prüfen
- Propellerwelle auf Rundlauf prüfen lassen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Beschädigter Propeller (Kerben, verbogene Blätter)
- Rissige/verformte Motorlager
- Motor steht schief auf dem Fundament
- Leine um Propeller/Welle gewickelt

---

### F-18_01-09 — Kraftstoff im Öl

**Symptom**: Ölstand steigt, Öl riecht nach Diesel, Öl ist
ungewöhnlich dünn.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Einspritzdüse undicht (tropft in Brennraum bei Stillstand) | 40 % |
| 2 | Einspritzpumpe — interne Undichtigkeit | 25 % |
| 3 | Hochdruck-Leitung undicht (Kraftstoff läuft in Motor) | 15 % |
| 4 | Übermäßiger Leerlaufbetrieb (unvollständige Verbrennung) | 10 % |
| 5 | Kolbenringe verschlissen + kalter Betrieb | 10 % |

**Sofortmaßnahmen:**
1. Motor abstellen
2. Ölstand prüfen — über MAX-Markierung?
3. Ölprobe entnehmen — Diesel-Geruch?
4. Sofortiger Ölwechsel erforderlich
5. Motor nur kurz laufen lassen zur Kontrolle

**Langfristmaßnahmen:**
- Injektoren prüfen und überholen/tauschen
- Einspritzpumpe prüfen lassen
- Motor nicht lange im Leerlauf laufen (max. 5 Min.)
- Regelmäßige Ölanalyse

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Ölstand über MAX am Messstab
- Öl riecht nach Diesel
- Öl ungewöhnlich dünn und klar
- Kraftstoffspuren an Injektoren/Leitungen

---

### F-18_01-10 — Wasser im Öl

**Symptom**: Milchig-braune Emulsion auf Ölmessstab,
Mayonnaise-artige Ablagerungen unter Ventildeckel.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Zylinderkopfdichtung defekt (Kühlwasser → Öl) | 35 % |
| 2 | Ölkühler undicht (intern, Seewasser → Öl) | 25 % |
| 3 | Kondensation (kurze Laufzeiten, kaltes Klima) | 20 % |
| 4 | Zylinderkopf gerissen | 10 % |
| 5 | Motorblock gerissen | 5 % |
| 6 | Wärmetauscher-Leck (intern) | 5 % |

**Sofortmaßnahmen:**
1. Motor SOFORT abstellen! Wasser im Öl zerstört Lager!
2. Menge beurteilen: dünner Film = Kondensation, dicke Emulsion = Leck
3. Kühlmittelstand prüfen (sinkt er?) → Internes Leck
4. Nicht weiterfahren! Abschleppen lassen.

**Langfristmaßnahmen:**
- Druckprüfung Kühlsystem (zeigt KZD-/Rissleck)
- Ölkühler auf Dichtigkeit prüfen (extern)
- Ölanalyse: Glykol-Nachweis = Kühlmittelleck
- Motor erst nach Reparatur und komplettem Ölwechsel starten

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Milchig-braune Emulsion am Ölmessstab
- Mayonnaise unter Ventildeckel / Öleinfülldeckel
- Kühlmittelstand sinkt ohne sichtbares Leck
- Ölig-trübes Kühlmittel im Ausgleichsbehälter

---

### F-18_01-11 — Dieselnageln/Klopfen

**Symptom**: Metallisches Klopfen/Nageln, besonders im
Leerlauf und bei niedriger Last.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Falscher Einspritzzeitpunkt (zu früh) | 25 % |
| 2 | Kalter Motor (normal bei Kaltstart) | 20 % |
| 3 | Schlechte Kraftstoffqualität (niedrige Cetanzahl) | 18 % |
| 4 | Einspritzdüse defekt (schlechte Zerstäubung) | 15 % |
| 5 | Kolbenbolzen ausgeschlagen | 8 % |
| 6 | Pleuellager verschlissen | 7 % |
| 7 | Ventilspiel zu groß | 5 % |
| 8 | Turbolader-Schaden | 2 % |

**Sofortmaßnahmen:**
1. Motor warm laufen lassen — verschwindet das Klopfen?
2. Kraftstoffqualität prüfen (Tankstelle wechseln)
3. Ventilspiel prüfen und einstellen
4. Einzelne Zylinder isolieren (Einspritzleitung lösen)

**Langfristmaßnahmen:**
- Einspritzdüsen prüfen und ggf. austauschen
- Einspritzzeitpunkt kontrollieren (Werkstatt)
- Hochwertige Kraftstoffadditive verwenden (Cetanbooster)
- Lagerspiel messen bei Verdacht auf Lagerverschleiß

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Motorblock vibriert ungleichmäßig
- Metallisches Klappern hörbar bei geöffnetem Motorraum
- Eventuelle Ölundichtigkeit an Pleuellagern

---

### F-18_01-12 — Motor erreicht Nenndrehzahl nicht

**Symptom**: Motor kommt unter Last nicht auf die spezifizierte
Nenndrehzahl. Typisch: 200–500 U/min zu wenig.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Bewachsener Rumpf / Propeller | 25 % |
| 2 | Falsche Propellersteigung (zu steil) | 15 % |
| 3 | Kraftstoffzufuhr unzureichend | 15 % |
| 4 | Luftfilter verschmutzt | 10 % |
| 5 | Turbolader-Schaden / Ladedruckverlust | 8 % |
| 6 | Gaszug klemmt (Vollgas nicht erreicht) | 7 % |
| 7 | Motor verschlissen (Kompression niedrig) | 7 % |
| 8 | Einspritzdüsen verschlissen | 5 % |
| 9 | Auspuff-Gegendruck zu hoch | 4 % |
| 10 | Motorbremse/Decompression aktiv | 2 % |
| 11 | Motorsteuergerät begrenzt (Fehlermodus) | 2 % |

**Sofortmaßnahmen:**
1. Gashebel voll durchdrücken — mechanisch am Anschlag?
2. Drehzahlmesser am Motor: Nenndrehzahl ohne Gang erreicht?
   Ja → Rumpf/Propeller. Nein → Motor.
3. Luftfilter prüfen
4. Kraftstofffilter prüfen
5. Turbo: Ladeluftschläuche auf Risse/Undichtigkeit

**Langfristmaßnahmen:**
- Rumpf alle 1–2 Jahre reinigen und Antifouling erneuern
- Propellerdimensionierung vom Fachmann prüfen lassen
- Kraftstoffsystem systematisch warten
- Kompressionsmessung bei Motorverschleiß-Verdacht

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Bewachsener Rumpf / Propeller (Unterwasser-Fotos)
- Schwarzer Auspuffrauch (Überlastung)
- Durchhängende Ladeluftschläuche
- Gaszugeinstellung sichtbar falsch

---
---

## 15. Troubleshooting

### 15.1 Entscheidungsbaum 1: Motor springt nicht an

```
Motor springt nicht an
├── Starter dreht?
│   ├── NEIN
│   │   ├── Batteriespannung < 12,0 V?
│   │   │   ├── JA → Batterie laden / ersetzen
│   │   │   └── NEIN → Starterrelais prüfen → Magnetschalter → Starter
│   │   ├── Sicherung / Motorstop-Schalter?
│   │   │   ├── JA → Sicherung / Schalter prüfen
│   │   │   └── NEIN → Zündschloss / Verdrahtung
│   │   └── Neutralschalter am Getriebe?
│   │       └── JA → Getriebe in Neutral, Schalter prüfen
│   └── JA → Starter dreht normal?
│       ├── NEIN (dreht langsam)
│       │   └── Batterie schwach → laden / Kabel prüfen
│       └── JA (dreht normal, keine Zündung)
│           ├── Kraftstoff vorhanden?
│           │   ├── NEIN → Tanken, Absperrhahn öffnen
│           │   └── JA → Kraftstoffsystem entlüften
│           ├── Kraftstofffilter verstopft?
│           │   └── JA → Filter wechseln
│           ├── Glühkerzen funktionieren?
│           │   └── NEIN → Glühkerzen tauschen
│           ├── Luft im Kraftstoffsystem?
│           │   └── JA → Entlüften (Schraube am Feinfilter)
│           └── Kompression vorhanden?
│               └── NEIN → Werkstatt (Ventile, Kolbenringe)
```

### 15.2 Entscheidungsbaum 2: Motor überhitzt

```
Motor überhitzt (Temperatur > 95 °C)
├── Seewasser-Austritt am Auspuff prüfen
│   ├── KEIN Wasser → Seewassersystem defekt
│   │   ├── Seeventil geschlossen? → Öffnen!
│   │   ├── Seewasserfilter verstopft? → Reinigen!
│   │   ├── Impeller defekt? → Wechseln!
│   │   │   └── Impellerflügel im System? → Wärmetauscher öffnen, Teile entfernen
│   │   └── Seewasserpumpe undicht? → Reparieren
│   └── Normaler Wasserfluss → Primärkreis prüfen
│       ├── Kühlmittelstand OK?
│       │   ├── NEIN → Nachfüllen, Leck suchen
│       │   └── JA → Thermostat prüfen
│       │       ├── Thermostat öffnet nicht → Thermostat tauschen
│       │       └── Thermostat OK → Wärmetauscher verkalkt/verstopft
│       │           └── Wärmetauscher reinigen / ersetzen
│       └── Motor überlastet?
│           ├── JA → Drehzahl reduzieren, Rumpf/Propeller prüfen
│           └── NEIN → Zylinderkopfdichtung prüfen (Drucktest)
```

### 15.3 Entscheidungsbaum 3: Rauchfarbe analysieren

```
Auspuffrauch abnormal
├── Farbe?
│   ├── SCHWARZ → Unvollständige Verbrennung
│   │   ├── Luftfilter prüfen → verstopft? → Reinigen/Wechseln
│   │   ├── Turbolader prüfen → Ladedruck OK?
│   │   │   ├── NEIN → Turbo reparieren
│   │   │   └── JA → Einspritzdüsen prüfen
│   │   ├── Motor überlastet? → Propeller/Rumpf
│   │   └── Ventilspiel → Einstellen
│   ├── WEISS → Unverbrannter Kraftstoff oder Kühlmittel
│   │   ├── Motor kalt? → Normal, abwarten
│   │   ├── Kühlmittelstand sinkt? → KZD defekt → Werkstatt
│   │   ├── Einspritzzeitpunkt → Prüfen/Einstellen
│   │   └── Wasser im Kraftstoff → Vorfilter/Abscheider
│   └── BLAU → Motoröl verbrennt
│       ├── Ölstand zu hoch? → Korrigieren
│       ├── Nur beim Kaltstart? → Ventilschaftdichtungen
│       ├── Permanent? → Kolbenringe / Turbolager
│       └── Ölverbrauch messen → >1,5 g/kWh? → Motor überholen
```

### 15.4 Entscheidungsbaum 4: Abnormale Motorgeräusche

```
Ungewöhnliche Motorgeräusche
├── Geräuschtyp?
│   ├── Metallisches Klopfen (niederfrequent)
│   │   ├── Drehzahlabhängig? → Lager (Pleuel, Hauptlager)
│   │   │   └── SOFORT Motor abstellen → Werkstatt!
│   │   └── Lastabhängig? → Einspritzung prüfen
│   ├── Klappern (hochfrequent)
│   │   ├── Im Zylinderkopfbereich → Ventilspiel prüfen
│   │   ├── Am Antriebsriemen → Riemenspannung prüfen
│   │   └── Am Getriebe → Getriebeöl prüfen
│   ├── Quietschen/Pfeifen
│   │   ├── Keilriemen → Spannen oder tauschen
│   │   ├── Turbolader → Lager prüfen
│   │   └── Lichtmaschine → Lager prüfen
│   └── Rauschen/Zischen
│       ├── Ladeluftsystem → Schläuche auf Undichtigkeit
│       ├── Auspuffsystem → Undichtigkeit am Krümmer
│       └── Seewasserintake → Luft im System
```

### 15.5 Entscheidungsbaum 5: Ölanomalie analysieren

```
Ölproblem erkannt
├── Art des Problems?
│   ├── Ölstand steigt
│   │   ├── Diesel-Geruch im Öl → F-18_01-09 (Kraftstoff im Öl)
│   │   ├── Milchig/schaumig → F-18_01-10 (Wasser im Öl)
│   │   └── Seewasser-Geruch → Ölkühler undicht → Werkstatt
│   ├── Ölstand sinkt schnell
│   │   ├── Äußeres Leck sichtbar? → Dichtung/Schlauch erneuern
│   │   ├── Kein Leck sichtbar → Ölverbrauch messen
│   │   │   ├── >1,5 g/kWh → Kolbenringe/Ventilschaftdichtungen
│   │   │   └── <1,5 g/kWh → Normal, regelmäßig nachfüllen
│   │   └── Blauer Rauch? → F-18_01-06 (Ölverbrennung)
│   ├── Öldruck niedrig → F-18_01-07 (Niedriger Öldruck)
│   └── Öl ungewöhnlich dunkel/verbrannt
│       ├── Ölwechselintervall überschritten → Ölwechsel durchführen
│       ├── Motor überlastet/überhitzt → Ursache beheben
│       └── Rußeintrag (Diesel) → Luftfilter, Einspritzung prüfen
```

---
---

## 16. FAQ

### Allgemeine Fragen

**F: Wie viele Betriebsstunden sind „zu viel" für einen Marine-Diesel?**

A: Es gibt keine absolute Grenze — der Zustand hängt stark von
Wartung und Betriebsbedingungen ab. Als Faustregel: Ein gut gewarteter
Saugmotor mit mechanischer Einspritzung kann 10.000–15.000 h ohne
Grundüberholung laufen. Common-Rail-Motoren typischerweise
6.000–10.000 h. Entscheidend sind Kompressionswerte, Ölanalyse
und Wartungshistorie — nicht die bloße Stundenzahl.

**F: Kann ich mein Boot mit Heizöl (HEL) betanken?**

A: Technisch ja — Marine-Diesel können Heizöl verbrennen. In
Deutschland ist dies jedoch seit 2009 für Sportboote auf
Bundeswasserstraßen verboten (Energiesteuergesetz). In einigen
europäischen Ländern (z. B. Frankreich: „Gazole non routier",
Irland: „Green Diesel") gibt es steuerbegünstigten Schiffsdiesel.
Informieren Sie sich vor Ort über die lokalen Bestimmungen.

**F: Wie lange kann ein Marine-Diesel im Leerlauf laufen?**

A: Möglichst kurz! Längerer Leerlauf (>15–30 Minuten) führt bei
Marine-Diesel zu:
- Verglasung der Zylinder (Ölfilm auf der Zylinderwand verkokt nicht)
- Rußaufbau, besonders bei Turbomotoren
- Unvollständige Verbrennung → Kraftstoff im Öl
- DPF kann nicht regenerieren
- Empfehlung: Wenn der Motor nur für Batterieladung läuft, mindestens
  40 % Last erzeugen (z. B. durch Kühltruhe, Boiler, E-Herd).

**F: Muss ich den Motor warmlaufen lassen?**

A: Ja, aber richtig. Empfehlung:
1. Starten, 1–2 Minuten Leerlauf
2. Langsam Gang einlegen und mit 1.200–1.500 U/min losfahren
3. Erst nach 5–10 Minuten (Kühlwasser >60 °C) auf Reisedrehzahl gehen
4. NIEMALS kalten Motor mit Volllast belasten!

**F: Was ist wichtiger — Öl oder Kühlmittel?**

A: Beides ist gleichermaßen kritisch. Ohne Öl hat der Motor
maximal 30–60 Sekunden, bevor die Lager fressen. Ohne Kühlung
hat der Motor 3–5 Minuten, bevor die Zylinderkopfdichtung versagt.
Beides muss vor jeder Fahrt kontrolliert werden.

**F: Wie lagere ich meinen Motor für den Winter ein?**

A: Winter-Einlagerung in 10 Schritten:
1. Motor warmlaufen lassen
2. Ölwechsel bei warmem Motor (mit Filter)
3. Kühlmittel auf Frostschutz prüfen (−37 °C)
4. Seewassersystem mit Frostschutz oder Druckluft entleeren
5. Impeller ausbauen (oder zumindest entlasten)
6. Kraftstofftank volltanken + Biozid hinzufügen
7. Kraftstofffilter wechseln
8. Luftfilter reinigen/wechseln
9. Anode(n) prüfen und ggf. tauschen
10. Motor konservieren (WD-40 oder spezifisches Korrosionsschutzöl
    in den Luftfilter sprühen, Zylinder über Einspritzdüsen ölen)

**F: Kann ich Bio-Diesel (B100) verwenden?**

A: NEIN — die meisten Marine-Diesel-Hersteller lassen maximal B7
(7 % Biodieselanteil) zu. Höhere Biodieselanteile verursachen:
- Dichtungsquellung (insbesondere bei älteren Motoren)
- Beschleunigte Dieselpest (biologische Kontamination)
- Verstopfte Injektoren
- Probleme mit dem DPF
- Garantieverlust!

**F: Wie oft muss ich den Impeller wechseln?**

A: AYDI-Empfehlung: Jährlich, vor Saisonbeginn. Selbst wenn der
Impeller optisch noch gut aussieht, verliert er nach 12–18 Monaten
seine Elastizität. Ein Impellerversagen auf See führt innerhalb von
Minuten zur Überhitzung. Kosten: 25–80 EUR für den Impeller + 30 Min.
Arbeit. Billigkeit Versicherung gegen Motorschaden (5.000–20.000 EUR).

**F: Was kostet ein neuer Motor inklusive Einbau?**

A: Grobe Richtwerte für Segelboote:
- 15–25 PS: 8.000–14.000 EUR (Motor + Einbau)
- 25–45 PS: 12.000–20.000 EUR
- 45–75 PS: 18.000–30.000 EUR
- 75–110 PS: 25.000–40.000 EUR
Dazu kommen ggf.: neuer Saildrive/Stopfbuchse, Propeller,
Schaltung, Instrumentierung. Der Einbau dauert typischerweise
3–7 Werktage und kostet 3.000–8.000 EUR Arbeitszeit.

### Kraftstoff-Fragen

**F: Wie erkenne ich Dieselpest?**

A: Anzeichen:
- Verstopfte Kraftstofffilter (häufiger Filterwechsel nötig)
- Schwarzer/brauner Schleim im Vorfilter
- Motor stottert unter Last
- Kraftstoff riecht faulig/modrig
- Dunkle Flocken oder Gel im Kraftstoff
Test: Dieselpest-Testkit (z. B. FUELSTAT) ca. 30 EUR.
Bestätigt die Kontamination → Tankreinigung erforderlich.

**F: Wie lagere ich Kraftstoff im Tank über den Winter?**

A: Tank VOLL füllen (reduziert Kondensation). Biozid hinzufügen
(z. B. Grotamar 82, 1 ml/10 Liter). Kraftstoffstabilisator
(z. B. Sta-bil Marine, 10 ml/10 Liter). Nach 6 Monaten Standzeit
den ersten Kraftstofffilter nach 5–10 Betriebsstunden wechseln.

**F: Mein Vorfilter zeigt Wasser — was tun?**

A: Sofort das Wasser über den Ablasshahn unten am Vorfilter
(Racor, Separ) ablassen. Ursachen: Kondensation im Tank,
undichter Tankdeckel, verunreinigter Kraftstoff. Wenn häufig
Wasser auftritt: Tank auf Undichtigkeit prüfen lassen.

### Einspritzung und Kraftstoffsystem

**F: Wie entlüfte ich das Kraftstoffsystem?**

A: Vorgehensweise (mechanische Einspritzung):
1. Absperrhahn öffnen
2. Entlüftungsschraube am Kraftstoff-Feinfilter öffnen
3. Handpumpe (falls vorhanden) betätigen oder Elektropumpe einschalten
4. Warten, bis blasenfreier Kraftstoff austritt
5. Entlüftungsschraube schließen (nicht zu fest! 5 Nm)
6. Vorgang an der Einspritzpumpe wiederholen
7. Bei hartnäckiger Luft: Einspritzleitungen an den Düsen lösen,
   Starter betätigen bis Kraftstoff austritt, Leitungen wieder festziehen

**F: Wie erkenne ich defekte Einspritzdüsen?**

A: Symptome:
- Unrunder Motorlauf
- Schwarzer Rauch (einzelner Zylinder)
- Dieselnageln/Klopfen
- Kraftstoff im Öl (Injektor tropft im Stillstand)
Test: Einspritzleitungen einzeln lösen und Motor laufen lassen.
Zylinderabschaltung: Wenn beim Lösen einer Leitung KEINE
Drehzahländerung eintritt, arbeitet dieser Zylinder nicht → Injektor
oder Kompression defekt.

**F: Was kostet eine Injektorüberholung?**

A: Mechanische Düse: 80–150 EUR/Stück (Prüfstand + neue Düse).
Common-Rail-Injektor: 300–800 EUR/Stück (Austauschteile).
CR-Injektor Neukauf: 400–1.200 EUR/Stück.
Empfehlung: Immer alle Injektoren gleichzeitig überholen/tauschen.

### Kühlung

**F: Welches Kühlmittel soll ich verwenden?**

A: Immer das vom Motorhersteller empfohlene Kühlmittel.
Allgemein: 50/50 Mischung aus Ethylenglykol-Konzentrat (OAT oder
Si-OAT) und destilliertem/demineralisiertem Wasser. KEIN
Leitungswasser (Kalkablagerung)! KEIN Mischen verschiedener
Kühlmittel-Typen (OAT ≠ Si-OAT ≠ IAT)!

**F: Wie oft muss der Wärmetauscher gereinigt werden?**

A: Seewasserseitig: Alle 3–5 Jahre oder bei nachlassender
Kühlleistung. Primärseitig: Beim Kühlmittelwechsel alle 2 Jahre
spülen. In Gebieten mit kalkhaltigem Wasser oder starkem
Muschelwachstum: häufiger.

**F: Mein Seewasser-Austritt am Auspuff ist schwach — was tun?**

A: Reihenfolge prüfen:
1. Seewasserfilter → reinigen
2. Seeventil → ganz offen?
3. Impeller → Flügel vollständig?
4. Seewasserleitungen → Knick? Verstopfung?
5. Wärmetauscher → verstopft?
6. Auspuff-Wassermantel → Kalkablagerung?

### Getriebe und Antrieb

**F: Mein Saildrive-Öl ist milchig — wie schlimm ist das?**

A: SEHR schlimm! Milchiges Öl im Saildrive bedeutet Wassereinbruch
durch die Manschette oder eine Dichtung. Sofort:
1. Boot AUS DEM WASSER nehmen
2. Saildrive öffnen, Wasser ablassen
3. Manschette/Dichtungen prüfen und ersetzen
4. Lager und Zahnräder auf Korrosion prüfen
5. Kosten: 1.500–5.000 EUR je nach Schaden

**F: Welche Getriebeöl-Temperatur ist normal?**

A: Normal: 60–90 °C. Warnung: >100 °C. Kritisch: >120 °C.
Ursachen für Überhitzung: zu wenig Getriebeöl, verschlissene
Kupplung, blockierter Propeller, falsches Öl.

**F: Wie höre ich ein defektes Getriebe?**

A: Anzeichen:
- Ratschen/Rasseln beim Einlegen des Ganges
- Schleifen im Vorwärts- oder Rückwärtsgang
- Vibrationen nur im Gang, nicht im Leerlauf
- Gang rutscht (Drehzahl steigt, Boot wird nicht schneller)
- Getriebeöl metallisch glänzend (Abrieb)

### Emissionen und Vorschriften

**F: Muss ich meinen alten Motor nachrüsten?**

A: Nein — Bestandsmotoren genießen Bestandsschutz. EU Stage V
gilt nur für Motoren, die erstmals in Verkehr gebracht werden.
Ausnahme: Einige Binnengewässer (z. B. Bodensee) haben eigene
Vorschriften, die auch Bestandsmotoren betreffen können.

**F: Was bedeutet der blaue Umweltaufkleber?**

A: In Deutschland gibt es (Stand 2026) keine generelle
Umweltzone für Sportboote. Einige Reviere (Bodensee, Berliner
Gewässer) verlangen spezifische Motorenstandards. Informieren
Sie sich beim lokalen Wasserschifffahrtsamt.

**F: Braucht mein Boot eine Abgasuntersuchung?**

A: Für Sportboote in der EU: Nein, keine regelmäßige
Abgasuntersuchung. Der Motor muss bei Erstinverkehrbringen
die geltende Emissionsnorm erfüllen. Für gewerbliche Fahrzeuge
können je nach Flaggenstaat Prüfpflichten bestehen.

### Kosten und Wirtschaftlichkeit

**F: Was kostet der Betrieb pro Stunde?**

A: Grobe Richtwerte (Segelboot-Hilfsmotor 30–50 PS):
- Kraftstoff: 5–10 EUR/h (bei 60–75 % Last)
- Öl/Filter (umgelegt): 1–2 EUR/h
- Impeller/Riemen (umgelegt): 0,50–1 EUR/h
- Wartung/Werkstatt (umgelegt): 2–5 EUR/h
- Rücklage für Reparaturen: 3–8 EUR/h
- **Gesamt: 12–26 EUR/h**

Für Motoryachten (200–400 PS): 40–100 EUR/h.

**F: Lohnt sich ein Motortausch oder besser eine Überholung?**

A: Faustregeln:
- Kosten Grundüberholung < 50 % Neumotor → Überholung
- Kosten Grundüberholung > 60 % Neumotor → Neuer Motor
- Motor > 20 Jahre → Neuer Motor (bessere Teileversorgung)
- Boot wird nur noch 5 Jahre genutzt → Überholung
- Boot wird langfristig gehalten → Neuer Motor

**Typische Kosten Grundüberholung:**

| Umfang | Maßnahmen | Kosten |
|--------|----------|:---:|
| Klein | KZD, Ventile, Dichtungen, Kolbenringe | 2.500–5.000 EUR |
| Mittel | + Laufbuchsen, Kolben, Turbo-Überholung | 5.000–10.000 EUR |
| Groß | + Kurbelwelle schleifen, Lager, Nockenwelle | 8.000–18.000 EUR |

---
---

## 17. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Absperrhahn** | Ventil in der Kraftstoffleitung zwischen Tank und Motor |
| **AGR (Abgasrückführung)** | System zur NOx-Reduktion, leitet gekühlte Abgase zurück in den Ansaugtrakt |
| **Alignment** | Ausrichtung der Motorwelle zur Propellerwelle |
| **Anti-Siphon-Ventil** | Ventil im Auspuffsystem, verhindert Seewasser-Rückfluss in den Motor |
| **Betriebsstunde (Bh)** | Maßeinheit für die Laufzeit des Motors, primärer Verschleißindikator |
| **Bilge** | Tiefster Punkt im Bootsinneren, wo sich Wasser sammelt |
| **CAN-Bus** | Controller Area Network — digitaler Kommunikationsstandard für Steuergeräte |
| **Cetanzahl** | Maß für die Zündwilligkeit von Diesel (höher = besser, min. 45) |
| **Common-Rail (CR)** | Einspritzsystem mit gemeinsamer Hochdruckleitung und elektronischen Injektoren |
| **Dampfdruck** | Druck, bei dem eine Flüssigkeit zu verdampfen beginnt |
| **Dieselpest** | Mikrobiologische Kontamination des Kraftstoffs (Bakterien/Pilze) |
| **DPF (Dieselpartikelfilter)** | Filter im Abgasstrang, der Rußpartikel auffängt |
| **ECU (Engine Control Unit)** | Motorsteuergerät — elektronisches Gehirn des Motors |
| **Einspritzdüse/Injektor** | Bauteil, das Kraftstoff unter hohem Druck in den Zylinder einspritzt |
| **EU Stage V** | Aktuelle Emissionsnorm für neue Motoren in der EU (seit 2019) |
| **Förderpumpe** | Niederdruckpumpe, die Kraftstoff vom Tank zum Motor fördert |
| **Getriebe (Marine)** | Wendegetriebe mit Untersetzung — ermöglicht Vorwärts/Rückwärts/Neutral |
| **Glühkerze** | Elektrisches Heizelement zur Unterstützung des Kaltstarts |
| **Hochdruckpumpe** | Erzeugt den hohen Einspritzdruck (Common-Rail: bis 2.500 bar) |
| **Hubraum** | Gesamtvolumen aller Zylinder (Kolbenhub × Kolbenfläche × Zylinderanzahl) |
| **Impeller** | Gummi-Flügelrad in der Seewasserpumpe — DAS Verschleißteil am Marine-Diesel |
| **ISO 8665** | Norm zur Leistungsmessung von Schiffsmotoren |
| **J1939** | SAE-Standard für die Motorkommunikation via CAN-Bus |
| **Kolbenring** | Dichtring am Kolben — dichtet Verbrennungsraum ab und reguliert Ölfilm |
| **Kompression** | Verdichtungsdruck im Zylinder — Maß für den mechanischen Zustand |
| **Kurbelgehäuseentlüftung** | System zur Abführung von Blowby-Gasen aus dem Motorinneren |
| **KZD (Zylinderkopfdichtung)** | Dichtung zwischen Zylinderkopf und Motorblock |
| **Ladeluft** | Vom Turbolader verdichtete Ansaugluft |
| **Ladeluftkühler (LLK)** | Wärmetauscher zur Kühlung der Ladeluft nach dem Turbolader |
| **Marinisierung** | Anpassung eines Industrie-/Fahrzeugmotors für den Schiffseinsatz |
| **Nassauspuff** | Marine-Auspuffsystem mit Wasserkühlung (Seewasser + Abgas gemischt) |
| **NMEA 2000** | Digitaler Datenbus-Standard für maritime Elektronik |
| **OT/UT** | Oberer/Unterer Totpunkt — Endstellungen des Kolbens |
| **Propellerkurve** | Leistungsbedarf des Propellers als Funktion der Drehzahl (P ∝ n³) |
| **Racor** | Markenname für weit verbreitete Kraftstoff-Vorfilter/Wasserabscheider |
| **Rail** | Hochdruck-Kraftstoffleitung im Common-Rail-System |
| **Saildrive** | Motor-Getriebe-Einheit mit Unterwasserantrieb (Alternative zur Welle) |
| **SCR** | Selektive katalytische Reduktion — NOx-Reduktion mit Harnstofflösung (AdBlue) |
| **Schwanenhals** | S-förmiger Bogen im Auspuffsystem über der Wasserlinie |
| **Seewasserfilter** | Siebfilter am Seeventil, fängt Algen/Muscheln/Plastik ab |
| **SFC** | Spezifischer Kraftstoffverbrauch (g/kWh) |
| **Stopfbuchse** | Wellendurchführung durch den Rumpf — dichtet Propellerwelle ab |
| **Thermostat** | Regelt die Kühlmitteltemperatur (öffnet bei 71–82 °C) |
| **Turbolader** | Abgasturbinengetriebener Verdichter für die Ansaugluft |
| **Verdichtungsverhältnis** | Verhältnis Gesamtzylindervolumen / Kompressionsvolumen |
| **Wärmetauscher** | Überträgt Wärme vom Primärkreis (Kühlmittel) an den Sekundärkreis (Seewasser) |
| **Wassersammelkasten** | Schalldämpfer und Wassersammler im Nassauspuff (Waterlock) |
| **Wendegetriebe** | Getriebe mit Vorwärts-/Rückwärtskupplung und Untersetzung |
| **Zinkanode** | Opferanode im Kühlsystem zum Schutz vor galvanischer Korrosion |

---
---

## 18. Schnell-Referenz

### 18.1 Öl-Spezifikationen Schnellwahl

| Motor | Empfohlenes Öl | Menge |
|-------|---|:---:|
| Yanmar 1GM10 | 15W-40 CI-4 | 1,0 L |
| Yanmar 3JH40 | 15W-40 CI-4/CK-4 | 3,5 L |
| Yanmar 4JH80 | 15W-40 CK-4 | 5,2 L |
| Volvo D1-20 | 15W-40 CI-4 | 2,8 L |
| Volvo D2-40 | 15W-40 CI-4 | 4,5 L |
| Volvo D2-75 | 15W-40 CK-4 | 6,0 L |
| Beta 25 | 15W-40 CI-4 | 2,5 L |
| Beta 50 | 15W-40 CK-4 | 5,0 L |
| Nanni N3.21 | 15W-40 CI-4 | 2,8 L |
| Sole Mini-29 | 15W-40 CI-4 | 3,2 L |

### 18.2 Filter Schnellwahl

| Motor | Ölfilter | Kraftstofffilter | Luftfilter |
|-------|---------|-----------------|-----------|
| Yanmar 3JH40 | 129150-35170 | 129574-55711 | 128270-12540 |
| Yanmar 4JH80 | 129150-35170 | 129574-55711 | 128270-12540 |
| Volvo D1-20 | 861473 | 3581078 | 3809924 |
| Volvo D2-75 | 861473 | 3581078 | 3809924 |
| Beta 25 | HH150-32094 | HH166-43560 | — (extern) |
| Nanni N3.21 | HH150-32094 | HH166-43560 | — (extern) |

### 18.3 Impeller Schnellwahl

| Motor | Impeller-Teilenummer | Jabsco-Äquivalent | Preis |
|-------|---------------------|:---:|:---:|
| Yanmar 1GM/2YM/3JH | 128990-42200 | 22405-0001 | 25–40 EUR |
| Yanmar 4JH | 129470-42532 | 17937-0001 | 35–55 EUR |
| Volvo D1/D2 | 3586496 | 22405-0001 | 30–45 EUR |
| Beta 14–38 | 211-60004 | 1210-0001 | 25–40 EUR |
| Nanni N2/N3 | 970307632 | 22405-0001 | 28–42 EUR |

### 18.4 Drehmoment-Richtwerte

| Schraube | Drehmoment |
|----------|:---:|
| Zylinderkopf (M10) | 50–65 Nm |
| Zylinderkopf (M12) | 80–100 Nm |
| Pleuelschrauben | 30–45 Nm |
| Schwungradschrauben | 45–65 Nm |
| Einspritzdüsen-Halter | 20–30 Nm |
| Glühkerzen | 15–25 Nm |
| Ölfilter (Patronenfilter) | Handfest + ¾ Umdrehung |
| Motorlager-Schrauben | 25–40 Nm |
| Kupplungsflansch | 35–50 Nm |
| Getriebe-Einfüllschraube | 15–20 Nm |

### 18.5 Notfall-Referenz

**Motor springt nicht an — 5-Minuten-Check:**
1. ☐ Kraftstoff-Absperrhahn OFFEN?
2. ☐ Motorstop-Zug NICHT gezogen?
3. ☐ Gashebel auf START/LEERLAUF?
4. ☐ Getriebe in NEUTRAL?
5. ☐ Batteriespannung > 12,0 V?
6. ☐ Glühkerzen 15–30 Sekunden vorglühen?
7. ☐ Racor-Vorfilter: kein Wasser, nicht verschmutzt?
8. ☐ Kraftstoffsystem entlüftet?

**Überhitzungsalarm — Sofortprotokoll:**
1. ☐ Drehzahl auf LEERLAUF
2. ☐ Seewasseraustritt am Auspuff prüfen — fließt Wasser?
3. ☐ NEIN → Motor SOFORT ABSTELLEN
4. ☐ Seewasserfilter reinigen
5. ☐ Seeventil ganz offen?
6. ☐ Impeller wechseln (Ersatz an Bord!)
7. ☐ Motor 15 Min. abkühlen lassen
8. ☐ Kühlmittelstand prüfen (VORSICHT: Druck!)

**Öldruckalarm — Sofortprotokoll:**
1. ☐ Motor SOFORT auf LEERLAUF oder ABSTELLEN
2. ☐ Ölstand prüfen — unter MIN? → Nachfüllen
3. ☐ Ölfarbe: milchig = Wasser → MOTOR AUS!
4. ☐ Ölfarbe: dünn/Dieselgeruch = Kraftstoff → Motor AUS, Ölwechsel
5. ☐ Mechanisches Öldruckmessgerät anschließen zur Gegenprüfung

---
---

## 19. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Bavaria 37 Cruiser — Impellerversagen auf Langfahrt

**Boot:** Bavaria 37 Cruiser, Baujahr 2018
**Motor:** Volvo Penta D2-40, 38 PS, Saildrive 130
**Betriebsstunden:** 1.850 h
**Revier:** Ägäis, August, 35 °C Wassertemperatur

**Situation:**
Während einer Überfahrt von Kos nach Astypalea (42 sm) fiel nach
3 Stunden unter Maschine der Kühlwasser-Alarm aus. Der Eigner
bemerkte zunächst keinen Seewasserstrahl am Auspuff und stellte
den Motor ab. Temperaturanzeige: 102 °C.

**Diagnose:**
- Impeller komplett zerfallen (3 von 6 Flügeln abgerissen)
- Impellerflügel im Wärmetauscher gefangen
- Ursache: Impeller war 3 Jahre alt (letzter Wechsel bei 900 h)
- Heißes Seewasser (35 °C) beschleunigte Alterung

**Reparatur:**
1. 20 Minuten abkühlen lassen
2. Impeller gewechselt (Ersatz an Bord!)
3. Wärmetauscher geöffnet: 2 Flügelstücke entfernt
4. Seewasserfilter gereinigt (1 Flügelstück)
5. Motor gestartet: normale Temperatur 82 °C

**Kosten:** Impeller 35 EUR (an Bord), Eigenarbeit
**Lerneffekt:** Impeller JÄHRLICH wechseln, besonders im warmen Revier!

---

### ANHANG B — Fallstudie: Hallberg-Rassy 40 — Dieselpest nach Winterlager

**Boot:** Hallberg-Rassy 40, Baujahr 2014
**Motor:** Volvo Penta D2-75, 75 PS
**Betriebsstunden:** 2.100 h
**Revier:** Ostsee/Dänische Gewässer

**Situation:**
Nach 6-monatigem Winterlager (Oktober–April) lief der Motor beim
Saisonstart zunächst normal. Nach 2 Stunden unter Maschine begann
er zu stottern und blieb unter Last stehen. Neustart möglich, aber
Motor starb nach 10–15 Minuten erneut ab.

**Diagnose:**
- Kraftstofffilter (Racor) braun-schwarz verfärbt und verstopft
- Wasserabscheider: 50 ml Wasser aufgefangen
- Tankprobe: schwarz-braune Flocken, fauliger Geruch
- FUELSTAT-Test: Positive Kontamination (HUM-Bug)
- Tank war über den Winter nur halb voll (Kondensation!)

**Reparatur:**
1. Tank komplett leer pumpen (350 Liter kontaminierter Diesel)
2. Tank mit Dieselreiniger (ADERCO 2055G) gespült
3. Tank mechanisch gereinigt (Zugang über Inspektionsluke)
4. Neuer Kraftstoff + Biozid (Grotamar 82)
5. Alle Kraftstofffilter gewechselt (Racor + Motorfilter)
6. Kraftstoffleitungen gespült
7. Motor: 2 Stunden Probelauf unter Last

**Kosten:** Tank-Reinigung + Kraftstoff + Filter = 1.850 EUR
**Lerneffekt:** Tank IMMER voll über den Winter, Biozid verwenden!

---

### ANHANG C — Fallstudie: Jeanneau Sun Odyssey 440 — Auspuffkrümmer-Korrosion

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2019
**Motor:** Yanmar 4JH57, 57 PS, Saildrive SD50
**Betriebsstunden:** 1.200 h
**Revier:** Mittelmeer, Frankreich/Korsika

**Situation:**
Bei der jährlichen Inspektion entdeckte die Werft Kühlwasseraustritt
am Übergang Abgaskrümmer → Mischkammer. Keine Überhitzung bisher,
da das Leck klein war und extern austrat (nicht in den Motor).

**Diagnose:**
- Edelstahl-Bellows am Übergang Krümmer/Mischkammer korrodiert
- Innere Korrosion an der Mischkammer
- Ursache: Zinkanode im Kühlsystem seit Auslieferung nicht getauscht
- Galvanische Korrosion zwischen verschiedenen Metallen

**Reparatur:**
1. Auspuffkrümmer + Mischkammer komplett erneuert (Yanmar OEM)
2. Alle Zinkanoden im Kühlsystem getauscht
3. Kühlmittel komplett gewechselt
4. Wartungsplan erstellt: Anoden jährlich prüfen

**Kosten:** Krümmer + Mischkammer + Arbeit = 2.800 EUR
**Lerneffekt:** Zinkanoden im Kühlsystem JÄHRLICH prüfen!

---

### ANHANG D — Fallstudie: Bénéteau Océanis 46.1 — Common-Rail-Diagnose

**Boot:** Bénéteau Océanis 46.1, Baujahr 2022
**Motor:** Yanmar 4JH80, 80 PS, Common-Rail
**Betriebsstunden:** 650 h
**Revier:** Karibik (Transatlantik)

**Situation:**
Während der Atlantiküberquerung meldete das Motormanagement
„Check Engine" und reduzierte die Leistung auf ~60 % (Limp-Mode).
Motor lief, aber nur bei max. 2.200 U/min (statt 3.400 U/min).

**Diagnose (per YEDI-Ferndiagnose über Satellit):**
- Fehlercode: P0088 — Rail-Druck zu hoch
- Ursache: Druckregelventil am Rail verschmutzt (Paraffin-Ablagerung)
- Kraftstoffprobe: CFPP-Wert −2 °C (karibischer Diesel ohne
  Winteradditive ist paraffinhaltiger)

**Reparatur:**
1. Druckregelventil gereinigt (Bordmittel: Diesel + feine Bürste)
2. Rail-Druck-Sensor kalibriert (YEDI-Reset über Satellit!)
3. Kraftstofffilter gewechselt (beide Stufen)
4. Kraftstoffadditive hinzugefügt (CFPP-Verbesserer)
5. Fehlercode gelöscht → Motor normal

**Kosten:** Filter 45 EUR, Additiv 15 EUR, Ferndiagnose 200 EUR
**Lerneffekt:** In den Tropen: Kraftstoffqualität kritisch überwachen,
immer CFPP-Verbesserer mitführen. Common-Rail-Motoren sind
empfindlicher als mechanische Einspritzung.

---

### ANHANG E — Fallstudie: Grand Banks 42 — Motorausrichtung nach Osmose-Reparatur

**Boot:** Grand Banks 42 Classic, Baujahr 1998
**Motor:** 2× Caterpillar 3126 (420 PS gesamt)
**Betriebsstunden:** 5.800 h (Steuerbord), 5.650 h (Backbord)
**Revier:** Nordsee, Niederlande

**Situation:**
Nach umfangreicher Osmose-Behandlung (komplettes Laminat-Abschleifen
und Neuaufbau mit Epoxid) traten bei beiden Motoren starke Vibrationen
auf. Der Eigner fuhr 3 Monate mit den Vibrationen, bevor er eine
Werft aufsuchte.

**Diagnose:**
- Motorausrichtung beider Motoren außerhalb der Toleranz
- Steuerbord: 0,45 mm angulare Abweichung
- Backbord: 0,32 mm angulare + 0,25 mm parallele Abweichung
- Ursache: Rumpfform hatte sich durch Osmose-Reparatur minimal
  verändert (~1–2 mm am Motorfundament)
- Zusatzschaden durch 3 Monate Fahrt: verschlissene Stopfbuchsen-
  Packungen, angelaufene Getriebeflanschen

**Reparatur:**
1. Beide Motoren komplett neu ausgerichtet (Laser-Alignment)
2. Motorlager geprüft (OK, aber Steuerbord vorn leicht komprimiert)
3. Stopfbuchsen-Packungen erneuert (beide Wellen)
4. Getriebeflansche plan geschliffen

**Kosten:** Alignment + Stopfbuchsen + Flansch = 4.200 EUR
**Lerneffekt:** Nach JEDER Rumpfarbeit Motorausrichtung prüfen!

---

### ANHANG F — Fallstudie: Dehler 38 — Verglasung durch Unterlast

**Boot:** Dehler 38, Baujahr 2020
**Motor:** Volvo Penta D1-30, 28 PS, Saildrive 130
**Betriebsstunden:** 380 h
**Revier:** Mittelmeer, Griechenland

**Situation:**
Der Eigner nutzte den Motor fast ausschließlich zum Batterieladen
(Ankerliegen, 2–3 Stunden täglich im Leerlauf). Nach 2 Saisons
schwarzer Rauch beim Gas geben, unrunder Lauf, erhöhter Ölverbrauch.

**Diagnose:**
- Zylinder verglast (Ölfilm auf der Zylinderwand verkokt nicht
  bei Unterlast → Oberfläche wird spiegelglatt)
- Kolbenringe können nicht mehr dichten
- Kompression: Zyl. 1: 22 bar, Zyl. 2: 18 bar, Zyl. 3: 20 bar
  (Soll: 28–30 bar)
- Zusätzlich: Einspritzdüsen verrusst

**Reparatur:**
1. Zylinder gehont (Oberfläche aufgerauht)
2. Neue Kolbenringe eingesetzt
3. Einspritzdüsen überholt (neue Düseneinsätze)
4. Ventilschaftdichtungen erneuert
5. Komplett neues Öl, alle Filter

**Kosten:** Motorüberholung (teil) + Arbeit = 4.800 EUR
**Lerneffekt:** Motor NIE im Leerlauf zum Laden betreiben!
Mindestens 40 % Last (Heizpatrone im Boiler, Kühlschrank auf
Maximum, elektrischer Kochplatte). Besser: 1 h unter Maschine
fahren als 3 h Leerlauf.

---

### ANHANG G — Fallstudie: Lagoon 450 F — Turbolader-Schaden

**Boot:** Lagoon 450 F, Baujahr 2017
**Motor:** 2× Yanmar 4JH-CR 57 PS (Vorgänger 4JH57)
**Betriebsstunden:** 3.200 h (Backbord, Schaden), 3.100 h (Steuerbord)
**Revier:** Karibik (Charter-Katamaran)

**Situation:**
Im Charter-Betrieb meldete der Backbord-Motor plötzlich Leistungsverlust
und starken schwarzen Rauch. Turbo-Pfeifgeräusch ungewöhnlich laut.
Motor wurde bei 60 % Last weiter betrieben (Charter-Crew ohne
technische Kenntnisse).

**Diagnose:**
- Turbolager verschlissen (Axialspiel 0,35 mm, Soll max. 0,15 mm)
- Öl im Ladeluftschlauch und Ansaugkrümmer
- Ursache: Ölwechselintervall überschritten (letzte 800 h ohne
  Ölwechsel im Charter-Betrieb)
- Weiterfahrt unter Last → Turbolader komplett blockiert
- Sekundärschaden: verschmutzter Ladeluftkühler

**Reparatur:**
1. Turbolader ersetzt (kein Austausch möglich bei dem Schaden)
2. Ladeluftkühler gereinigt
3. Ansaugkrümmer gereinigt
4. Ölwechsel mit Premium-Öl + neuer Filter
5. 2 h Probelauf unter steigender Last

**Kosten:** Turbo + Arbeit + Teile = 3.800 EUR
**Lerneffekt:** Charter-Motoren brauchen STRIKTERE Wartungsintervalle
(Ölwechsel alle 100–150 h, nicht 200 h). Turbo-Motoren verzeihen
kein altes Öl!

---

### ANHANG H — Fallstudie: Motorentausch Yanmar 3GM → 3JH40

**Boot:** Nordship 35 DS, Baujahr 2005
**Alter Motor:** Yanmar 3GM30F, 27 PS, mechanisch, 7.200 h
**Neuer Motor:** Yanmar 3JH40, 40 PS, Common-Rail
**Revier:** Ostsee, Dänemark

**Ausgangslage:**
Der Yanmar 3GM30F lief seit 20 Jahren zuverlässig, zeigte aber
zunehmende Verschleißerscheinungen: Kompression niedrig (22 bar avg.),
Ölverbrauch 1,8 g/kWh, Rauchentwicklung. Eine Grundüberholung
wäre auf ca. 5.500 EUR geschätzt worden.

**Entscheidung für Neuen Motor:**
- Überholung: 5.500 EUR, aber weiterhin alter Motor (Ersatzteile
  auslaufend, keine Elektronik, lauter)
- Neuer Motor: 14.500 EUR (Motor + Saildrive SD25) + 4.500 EUR Einbau
- Mehrkosten: 13.500 EUR, aber: neuer Motor, volle Garantie,
  leiser, sparsamer, Stage V konform, 40 PS statt 27 PS

**Einbau-Details:**
1. Alter Motor + Saildrive ausgebaut (1 Tag)
2. Motorfundament angepasst (neuer Motor schmaler, aber länger)
3. Neue Motorlager montiert
4. Neuer Saildrive SD25 installiert (Rumpföffnung passt)
5. Neuer Propeller (Flexofold 3-Blatt, 15 × 11)
6. Neue Gaszüge, Schaltung, Instrumentierung
7. CAN-Bus-Anbindung an Navigationssystem
8. Probefahrt und Propelleranpassung

**Gesamtkosten:**
| Position | Kosten |
|----------|:---:|
| Motor Yanmar 3JH40 | 10.500 EUR |
| Saildrive SD25 | 4.000 EUR |
| Propeller Flexofold | 1.800 EUR |
| Instrumentierung | 650 EUR |
| Schaltung/Gaszüge | 450 EUR |
| Einbau (5 Werktage) | 4.500 EUR |
| Diverse (Schläuche, Kabel, Halter) | 600 EUR |
| **Gesamt** | **22.500 EUR** |

**Ergebnis:**
- 48 % mehr Leistung (27 → 40 PS)
- 15 % weniger Verbrauch
- Deutlich leiser (Common-Rail + neue Motorlager)
- Volle Herstellergarantie (3 Jahre)
- Moderne Diagnose über CAN-Bus

---
---

## 20. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — MarineDieselSpec

```python
"""
Pydantic v2 Datenmodelle für die Marine-Diesel-Analyse.
Alle Modelle verwenden model_config = {"from_attributes": True}.
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class EngineType(str, Enum):
    """Motortyp-Klassifikation."""
    NATURALLY_ASPIRATED = "naturally_aspirated"
    TURBOCHARGED = "turbocharged"
    TURBOCHARGED_INTERCOOLED = "turbocharged_intercooled"
    SUPERCHARGED = "supercharged"


class InjectionType(str, Enum):
    """Einspritzsystem-Klassifikation."""
    MECHANICAL_INLINE = "mechanical_inline"
    MECHANICAL_DISTRIBUTOR = "mechanical_distributor"
    COMMON_RAIL_GEN1 = "common_rail_gen1"
    COMMON_RAIL_GEN2 = "common_rail_gen2"
    COMMON_RAIL_GEN3 = "common_rail_gen3"
    UNIT_INJECTOR = "unit_injector"


class DriveType(str, Enum):
    """Antriebsart-Klassifikation."""
    SHAFT_DRIVE = "shaft_drive"
    SAILDRIVE = "saildrive"
    STERNDRIVE = "sterndrive"
    IPS_POD = "ips_pod"
    OUTBOARD = "outboard"
    WATERJET = "waterjet"


class EmissionStandard(str, Enum):
    """Emissionsnorm-Klassifikation."""
    PRE_REGULATION = "pre_regulation"
    EU_STAGE_IIIA = "eu_stage_iiia"
    EU_STAGE_IIIB = "eu_stage_iiib"
    EU_STAGE_IV = "eu_stage_iv"
    EU_STAGE_V = "eu_stage_v"
    EPA_TIER_2 = "epa_tier_2"
    EPA_TIER_3 = "epa_tier_3"
    IMO_TIER_II = "imo_tier_ii"
    IMO_TIER_III = "imo_tier_iii"


class CylinderArrangement(str, Enum):
    """Zylinderanordnung."""
    INLINE = "inline"
    V_TYPE = "v_type"
    BOXER = "boxer"


class CoolingSystem(str, Enum):
    """Kühlsystem-Typ."""
    RAW_WATER_DIRECT = "raw_water_direct"
    HEAT_EXCHANGER = "heat_exchanger"
    KEEL_COOLING = "keel_cooling"


class MarineDieselSpec(BaseModel):
    """Spezifikation eines Marine-Dieselmotors."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model_name: str = Field(..., description="Modellbezeichnung")
    engine_type: EngineType
    injection_type: InjectionType
    emission_standard: EmissionStandard
    drive_types: list[DriveType] = Field(
        default_factory=list,
        description="Kompatible Antriebsarten"
    )

    power_ps: float = Field(..., ge=1, le=5000, description="Leistung in PS")
    power_kw: float = Field(..., ge=0.7, le=3700, description="Leistung in kW")
    rated_rpm: int = Field(..., ge=1000, le=5000, description="Nenndrehzahl in U/min")

    cylinders: int = Field(..., ge=1, le=16, description="Zylinderanzahl")
    cylinder_arrangement: CylinderArrangement
    displacement_cc: int = Field(..., ge=100, le=50000, description="Hubraum in cm³")
    bore_mm: float = Field(..., ge=50, le=250, description="Bohrung in mm")
    stroke_mm: float = Field(..., ge=50, le=250, description="Hub in mm")
    compression_ratio: float = Field(
        ..., ge=12, le=25,
        description="Verdichtungsverhältnis"
    )

    max_torque_nm: float = Field(..., ge=5, le=10000, description="Max. Drehmoment in Nm")
    max_torque_rpm: int = Field(..., ge=800, le=4000, description="Drehzahl bei max. Drehmoment")

    weight_dry_kg: float = Field(..., ge=20, le=10000, description="Trockengewicht in kg")
    length_mm: float = Field(..., ge=200, le=5000, description="Länge in mm")
    width_mm: float = Field(..., ge=200, le=3000, description="Breite in mm")
    height_mm: float = Field(..., ge=200, le=3000, description="Höhe in mm")

    cooling_system: CoolingSystem = Field(
        default=CoolingSystem.HEAT_EXCHANGER,
        description="Kühlsystem-Typ"
    )
    oil_capacity_l: float = Field(..., ge=0.3, le=100, description="Ölinhalt in Litern")
    coolant_capacity_l: Optional[float] = Field(None, description="Kühlmittelinhalt in Litern")

    fuel_consumption_full_lph: float = Field(
        ..., ge=0.5, le=500,
        description="Kraftstoffverbrauch bei Volllast in l/h"
    )
    fuel_consumption_cruise_lph: Optional[float] = Field(
        None, description="Kraftstoffverbrauch bei Marschfahrt in l/h"
    )

    price_eur: Optional[float] = Field(None, ge=0, description="Preis in EUR")
    production_start_year: Optional[int] = Field(None, description="Produktionsbeginn")
    production_end_year: Optional[int] = Field(None, description="Produktionsende (None = aktuell)")

    aydi_rating: Optional[float] = Field(
        None, ge=0, le=10,
        description="AYDI-Gesamtbewertung (0–10)"
    )
```

### ANHANG J — EngineCondition

```python
class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class OilCondition(str, Enum):
    """Ölzustand."""
    CLEAN = "clean"
    NORMAL = "normal"
    DARK = "dark"
    DILUTED_FUEL = "diluted_fuel"
    EMULSIFIED_WATER = "emulsified_water"
    METALLIC_PARTICLES = "metallic_particles"


class EngineCondition(BaseModel):
    """Zustandsbewertung eines Marine-Dieselmotors."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Eindeutige Motor-ID")
    manufacturer: str = Field(..., description="Hersteller")
    model_name: str = Field(..., description="Modellbezeichnung")

    operating_hours: float = Field(..., ge=0, description="Betriebsstunden")
    age_years: float = Field(..., ge=0, description="Alter in Jahren")

    overall_condition: ConditionRating
    confidence: str = Field(
        ..., description="Konfidenzstufe der Bewertung"
    )

    compression_bar: Optional[list[float]] = Field(
        None, description="Kompressionswerte pro Zylinder in bar"
    )
    compression_deviation_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Max. Abweichung zwischen Zylindern in %"
    )
    oil_pressure_idle_bar: Optional[float] = Field(
        None, description="Öldruck im Leerlauf in bar"
    )
    oil_pressure_rated_bar: Optional[float] = Field(
        None, description="Öldruck bei Nenndrehzahl in bar"
    )
    oil_condition: Optional[OilCondition] = Field(
        None, description="Ölzustand"
    )
    oil_consumption_g_kwh: Optional[float] = Field(
        None, ge=0,
        description="Ölverbrauch in g/kWh"
    )

    coolant_temp_operating_c: Optional[float] = Field(
        None, description="Betriebstemperatur Kühlmittel in °C"
    )
    exhaust_temp_c: Optional[float] = Field(
        None, description="Abgastemperatur in °C"
    )
    smoke_color: Optional[str] = Field(
        None, description="Rauchfarbe: none, white, gray, black, blue"
    )

    rated_rpm_achieved: Optional[bool] = Field(
        None, description="Nenndrehzahl unter Last erreichbar?"
    )
    actual_max_rpm: Optional[int] = Field(
        None, description="Tatsächlich erreichte Maximaldrehzahl"
    )

    estimated_remaining_hours: Optional[float] = Field(
        None, description="Geschätzte Restlebensdauer in Stunden"
    )
    estimated_overhaul_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Überholungskosten in EUR"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )
```

### ANHANG K — CoolingSystemAssessment

```python
class ImpellerCondition(str, Enum):
    """Impeller-Zustand."""
    NEW = "new"
    GOOD = "good"
    WORN = "worn"
    DAMAGED = "damaged"
    DESTROYED = "destroyed"
    UNKNOWN = "unknown"


class CoolingSystemAssessment(BaseModel):
    """Bewertung des Kühlsystems."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Motor-ID")
    cooling_type: CoolingSystem

    # Impeller
    impeller_condition: ImpellerCondition
    impeller_age_months: Optional[int] = Field(
        None, ge=0, description="Impelleralter in Monaten"
    )
    impeller_hours_since_change: Optional[float] = Field(
        None, ge=0, description="Betriebsstunden seit Impellerwechsel"
    )

    # Wärmetauscher
    heat_exchanger_condition: ConditionRating
    heat_exchanger_last_cleaned: Optional[str] = Field(
        None, description="Letztes Reinigungsdatum (ISO 8601)"
    )

    # Anoden
    zinc_anode_condition_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Zinkanode Restzustand in % (100 = neu)"
    )

    # Thermostat
    thermostat_opening_temp_c: Optional[float] = Field(
        None, description="Thermostat-Öffnungstemperatur in °C"
    )
    thermostat_functional: Optional[bool] = Field(
        None, description="Thermostat funktioniert korrekt"
    )

    # Kühlmittel
    coolant_freeze_protection_c: Optional[float] = Field(
        None, description="Frostschutz bis (°C)"
    )
    coolant_age_months: Optional[int] = Field(
        None, ge=0, description="Kühlmittelalter in Monaten"
    )

    # Auspuffkrümmer
    exhaust_manifold_condition: ConditionRating
    exhaust_manifold_material: Optional[str] = Field(
        None, description="Material (Guss, Edelstahl, Aluminium)"
    )
    exhaust_manifold_age_years: Optional[float] = Field(
        None, ge=0, description="Krümmeralter in Jahren"
    )

    # Bewertung
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Kühlsystem-Gesamtbewertung (0–100)"
    )
    risk_level: str = Field(
        ..., description="Risikostufe: low, medium, high, critical"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
```

### ANHANG L — FuelSystemAssessment

```python
class FuelContamination(str, Enum):
    """Kraftstoff-Kontaminationsgrad."""
    CLEAN = "clean"
    MINOR = "minor"
    MODERATE = "moderate"
    SEVERE = "severe"
    CRITICAL = "critical"


class FuelSystemAssessment(BaseModel):
    """Bewertung des Kraftstoffsystems."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Motor-ID")
    injection_type: InjectionType

    # Tank
    tank_capacity_l: float = Field(..., ge=10, le=10000, description="Tankvolumen in Litern")
    fuel_age_months: Optional[int] = Field(
        None, ge=0, description="Kraftstoffalter in Monaten"
    )
    water_in_fuel: Optional[bool] = Field(
        None, description="Wasser im Kraftstoff vorhanden?"
    )
    contamination_level: FuelContamination

    # Filter
    prefilter_type: Optional[str] = Field(
        None, description="Vorfilter-Typ (Racor, Separ, etc.)"
    )
    prefilter_age_hours: Optional[float] = Field(
        None, ge=0, description="Betriebsstunden seit Filterwechsel"
    )
    engine_filter_age_hours: Optional[float] = Field(
        None, ge=0, description="Motorfilter-Alter in Stunden"
    )

    # Injektoren
    injector_condition: ConditionRating
    injector_hours: Optional[float] = Field(
        None, ge=0, description="Injektor-Betriebsstunden"
    )
    injection_pressure_bar: Optional[float] = Field(
        None, description="Einspritzdruck in bar"
    )

    # Bewertung
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Kraftstoffsystem-Gesamtbewertung (0–100)"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
```

### ANHANG M — EngineAlignment

```python
class AlignmentStatus(str, Enum):
    """Ausrichtungsstatus."""
    WITHIN_TOLERANCE = "within_tolerance"
    MARGINAL = "marginal"
    OUT_OF_TOLERANCE = "out_of_tolerance"
    CRITICAL = "critical"
    NOT_MEASURED = "not_measured"


class EngineAlignment(BaseModel):
    """Motorausrichtungs-Messung."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Motor-ID")
    drive_type: DriveType

    # Angulare Ausrichtung
    angular_deviation_mm: Optional[float] = Field(
        None, ge=0,
        description="Angulare Abweichung in mm"
    )
    angular_measurement_diameter_mm: Optional[float] = Field(
        None, description="Messdurchmesser in mm"
    )

    # Parallele Ausrichtung
    parallel_deviation_mm: Optional[float] = Field(
        None, ge=0,
        description="Parallele Abweichung in mm"
    )

    # Axiale Position
    flange_gap_mm: Optional[float] = Field(
        None, description="Flanschabstand in mm"
    )

    # Motorlager
    mount_condition: ConditionRating
    mount_age_years: Optional[float] = Field(
        None, ge=0, description="Motorlager-Alter in Jahren"
    )
    mount_type: Optional[str] = Field(
        None, description="Lagertyp"
    )

    # Bewertung
    alignment_status: AlignmentStatus
    vibration_level: Optional[str] = Field(
        None, description="Vibrationsniveau: low, medium, high"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
```

### ANHANG N — EngineSelection

```python
class BoatType(str, Enum):
    """Bootstyp für die Motorauswahl."""
    SAILBOAT_MONOHULL = "sailboat_monohull"
    SAILBOAT_CATAMARAN = "sailboat_catamaran"
    SAILBOAT_TRIMARAN = "sailboat_trimaran"
    MOTORBOAT_PLANING = "motorboat_planing"
    MOTORBOAT_SEMI_PLANING = "motorboat_semi_planing"
    MOTORBOAT_DISPLACEMENT = "motorboat_displacement"
    TRAWLER = "trawler"
    MOTORYACHT = "motoryacht"
    WORKBOAT = "workboat"


class EngineSelection(BaseModel):
    """Motorauswahl-Empfehlung."""
    model_config = {"from_attributes": True}

    boat_type: BoatType
    boat_length_m: float = Field(..., ge=4, le=50, description="Bootslänge in m")
    displacement_kg: float = Field(..., ge=500, le=200000, description="Verdrängung in kg")
    desired_speed_kn: Optional[float] = Field(
        None, ge=2, le=50, description="Gewünschte Geschwindigkeit in kn"
    )

    # Berechnete Werte
    required_power_kw: float = Field(
        ..., ge=1, le=5000,
        description="Benötigte Leistung in kW"
    )
    required_power_ps: float = Field(
        ..., ge=1.4, le=6800,
        description="Benötigte Leistung in PS"
    )

    # Einbaumaße
    max_engine_length_mm: Optional[float] = Field(
        None, description="Max. Motorlänge in mm"
    )
    max_engine_width_mm: Optional[float] = Field(
        None, description="Max. Motorbreite in mm"
    )
    max_engine_height_mm: Optional[float] = Field(
        None, description="Max. Motorhöhe in mm"
    )
    max_engine_weight_kg: Optional[float] = Field(
        None, description="Max. Motorgewicht in kg"
    )

    # Präferenzen
    preferred_manufacturers: list[str] = Field(
        default_factory=list,
        description="Bevorzugte Hersteller"
    )
    preferred_drive_type: Optional[DriveType] = Field(
        None, description="Bevorzugte Antriebsart"
    )
    budget_eur: Optional[float] = Field(
        None, ge=0, description="Budget in EUR"
    )

    # Empfehlungen
    recommended_engines: list[str] = Field(
        default_factory=list,
        description="Empfohlene Motormodelle"
    )
    rationale: str = Field(
        ..., description="Begründung der Empfehlung"
    )

    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG O — MaintenanceSchedule

```python
class MaintenanceInterval(str, Enum):
    """Wartungsintervall-Klassifikation."""
    HOURS_50 = "50h"
    HOURS_100 = "100h"
    HOURS_200 = "200h"
    HOURS_500 = "500h"
    HOURS_1000 = "1000h"
    HOURS_2000 = "2000h"
    HOURS_3000 = "3000h"
    HOURS_5000 = "5000h"
    ANNUAL = "annual"
    BIANNUAL = "biannual"
    SEASONAL = "seasonal"


class MaintenanceTask(BaseModel):
    """Einzelne Wartungsaufgabe."""
    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Aufgaben-ID")
    description_de: str = Field(..., description="Beschreibung (Deutsch)")
    interval: MaintenanceInterval
    interval_hours: Optional[int] = Field(
        None, ge=0, description="Intervall in Betriebsstunden"
    )
    interval_months: Optional[int] = Field(
        None, ge=0, description="Intervall in Monaten"
    )

    estimated_time_minutes: int = Field(
        ..., ge=5, le=1440,
        description="Geschätzte Arbeitszeit in Minuten"
    )
    difficulty: str = Field(
        ..., description="Schwierigkeit: easy, medium, hard, professional"
    )
    parts_cost_eur: float = Field(
        ..., ge=0, description="Materialkosten in EUR"
    )
    labor_cost_eur: Optional[float] = Field(
        None, ge=0, description="Arbeitskosten Werkstatt in EUR"
    )

    parts_required: list[str] = Field(
        default_factory=list,
        description="Benötigte Teile"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Benötigtes Werkzeug"
    )

    is_owner_doable: bool = Field(
        True, description="Vom Eigner selbst durchführbar?"
    )
    safety_critical: bool = Field(
        False, description="Sicherheitsrelevant?"
    )


class MaintenanceSchedule(BaseModel):
    """Wartungsplan für einen Marine-Diesel."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Motor-ID")
    manufacturer: str = Field(..., description="Hersteller")
    model_name: str = Field(..., description="Modell")
    current_hours: float = Field(..., ge=0, description="Aktuelle Betriebsstunden")

    tasks: list[MaintenanceTask] = Field(
        default_factory=list,
        description="Liste aller Wartungsaufgaben"
    )

    next_service_hours: float = Field(
        ..., ge=0, description="Nächster Service bei Stunden"
    )
    next_service_tasks: list[str] = Field(
        default_factory=list,
        description="Aufgaben beim nächsten Service"
    )
    estimated_annual_maintenance_eur: float = Field(
        ..., ge=0,
        description="Geschätzte jährliche Wartungskosten in EUR"
    )
```

### ANHANG P — EngineFailure

```python
class FailureSeverity(str, Enum):
    """Fehlerschwere."""
    MINOR = "minor"
    MODERATE = "moderate"
    MAJOR = "major"
    CRITICAL = "critical"


class FailureCategory(str, Enum):
    """Fehlerkategorie."""
    FUEL_SYSTEM = "fuel_system"
    COOLING_SYSTEM = "cooling_system"
    LUBRICATION = "lubrication"
    INJECTION = "injection"
    TURBOCHARGER = "turbocharger"
    ELECTRICAL = "electrical"
    MECHANICAL = "mechanical"
    EXHAUST = "exhaust"
    ALIGNMENT = "alignment"
    VIBRATION = "vibration"


class EngineFailure(BaseModel):
    """Fehlerdokumentation Marine-Diesel."""
    model_config = {"from_attributes": True}

    failure_id: str = Field(..., description="Fehler-ID (z.B. F-18_01-03)")
    title_de: str = Field(..., description="Fehlertitel (Deutsch)")
    symptom_de: str = Field(..., description="Symptombeschreibung (Deutsch)")

    category: FailureCategory
    severity: FailureSeverity

    causes: list[dict] = Field(
        default_factory=list,
        description="Liste der Ursachen mit Wahrscheinlichkeit"
    )
    immediate_actions: list[str] = Field(
        default_factory=list,
        description="Sofortmaßnahmen"
    )
    long_term_actions: list[str] = Field(
        default_factory=list,
        description="Langfristmaßnahmen"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visuelle Erkennungsmerkmale (Pipeline B)"
    )

    estimated_repair_cost_eur_min: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten (Minimum)"
    )
    estimated_repair_cost_eur_max: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten (Maximum)"
    )
    downtime_days: Optional[int] = Field(
        None, ge=0, description="Erwartete Ausfallzeit in Tagen"
    )

    affected_engines: list[str] = Field(
        default_factory=list,
        description="Besonders betroffene Motormodelle"
    )
    prevention_tips: list[str] = Field(
        default_factory=list,
        description="Präventionshinweise"
    )
```

### ANHANG Q — EngineDiagnostics (CAN-Bus)

```python
class DiagnosticParameter(BaseModel):
    """Einzelner Diagnoseparameter."""
    model_config = {"from_attributes": True}

    pgn: int = Field(..., description="J1939 Parameter Group Number")
    parameter_name: str = Field(..., description="Parametername")
    value: float = Field(..., description="Messwert")
    unit: str = Field(..., description="Einheit")
    min_normal: Optional[float] = Field(None, description="Normalbereich Minimum")
    max_normal: Optional[float] = Field(None, description="Normalbereich Maximum")
    is_alarm: bool = Field(False, description="Alarmzustand?")
    is_warning: bool = Field(False, description="Warnzustand?")


class FaultCode(BaseModel):
    """Motorsteuergeräte-Fehlercode."""
    model_config = {"from_attributes": True}

    code: str = Field(..., description="Fehlercode (z.B. P0088)")
    description_de: str = Field(..., description="Fehlerbeschreibung (Deutsch)")
    severity: FailureSeverity
    is_active: bool = Field(..., description="Aktiver Fehler?")
    occurrence_count: int = Field(
        ..., ge=1, description="Anzahl Auftritte"
    )
    first_occurrence_hours: Optional[float] = Field(
        None, description="Betriebsstunden beim ersten Auftreten"
    )
    recommended_action_de: str = Field(
        ..., description="Empfohlene Maßnahme (Deutsch)"
    )


class EngineDiagnostics(BaseModel):
    """CAN-Bus-Diagnose-Auswertung."""
    model_config = {"from_attributes": True}

    engine_id: str = Field(..., description="Motor-ID")
    manufacturer: str = Field(..., description="Hersteller")
    model_name: str = Field(..., description="Modell")
    protocol: str = Field(
        ..., description="Kommunikationsprotokoll (J1939, NMEA 2000, proprietär)"
    )
    timestamp: str = Field(..., description="Zeitstempel (ISO 8601)")

    operating_hours: float = Field(..., ge=0, description="Betriebsstunden")
    parameters: list[DiagnosticParameter] = Field(
        default_factory=list,
        description="Diagnoseparameter"
    )
    fault_codes: list[FaultCode] = Field(
        default_factory=list,
        description="Fehlercodes"
    )

    overall_health_score: float = Field(
        ..., ge=0, le=100,
        description="Motor-Gesundheitsbewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe der Bewertung"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
```

### ANHANG R — MarineDieselAnalysis (Orchestrierungs-Modell)

```python
class MarineDieselAnalysis(BaseModel):
    """
    Orchestrierungs-Modell für die Gesamtanalyse eines Marine-Dieselmotors.
    Kombiniert alle Teilanalysen zu einem Gesamtergebnis.
    """
    model_config = {"from_attributes": True}

    analysis_id: str = Field(..., description="Analyse-ID")
    engine_id: str = Field(..., description="Motor-ID")
    boat_id: Optional[str] = Field(None, description="Boot-ID")
    analysis_date: str = Field(..., description="Analysedatum (ISO 8601)")
    analysis_level: str = Field(
        ..., description="Analyselevel: quick (Level 1) oder professional (Level 2)"
    )

    # Teilanalysen
    engine_spec: Optional[MarineDieselSpec] = Field(
        None, description="Motorspezifikation"
    )
    engine_condition: Optional[EngineCondition] = Field(
        None, description="Motorzustand"
    )
    cooling_assessment: Optional[CoolingSystemAssessment] = Field(
        None, description="Kühlsystem-Bewertung"
    )
    fuel_assessment: Optional[FuelSystemAssessment] = Field(
        None, description="Kraftstoffsystem-Bewertung"
    )
    alignment: Optional[EngineAlignment] = Field(
        None, description="Ausrichtungs-Bewertung"
    )
    maintenance: Optional[MaintenanceSchedule] = Field(
        None, description="Wartungsplan"
    )
    diagnostics: Optional[EngineDiagnostics] = Field(
        None, description="CAN-Bus-Diagnose"
    )

    # Gesamtergebnis
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Motor (0–100)"
    )
    overall_condition: ConditionRating

    # Gewichtete Teilbewertungen
    sub_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (z.B. {'cooling': 85, 'fuel': 72})"
    )

    # Zusammenfassung
    summary_de: str = Field(
        ..., description="Zusammenfassung in Deutsch"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde"
    )
    all_findings: list[str] = Field(
        default_factory=list,
        description="Alle Befunde"
    )
    all_recommendations: list[str] = Field(
        default_factory=list,
        description="Alle Empfehlungen"
    )

    # Kostenschätzung
    estimated_immediate_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Sofortige Kosten für notwendige Maßnahmen"
    )
    estimated_annual_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte jährliche Unterhaltskosten"
    )
    estimated_5year_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte 5-Jahres-Kosten"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Gesamt-Konfidenzstufe"
    )
    data_sources: list[str] = Field(
        default_factory=list,
        description="Verwendete Datenquellen (structured, visual, text)"
    )
    model_version: str = Field(
        ..., description="AYDI-Modellversion"
    )
```
