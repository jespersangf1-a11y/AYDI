---
titel: "Abgasanlagen — Nassauspuff, Trockenauspuff und Mischkrümmer"
kategorie: "Motoren und Antrieb"
unterkategorie: "Abgasanlage"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_06 — Abgasanlagen — Nassauspuff, Trockenauspuff und Mischkrümmer

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Nassauspuff-System (Wet Exhaust)](#2-nassauspuff-system-wet-exhaust)
3. [Trockenauspuff-System (Dry Exhaust)](#3-trockenauspuff-system-dry-exhaust)
4. [Mischkrümmer / Injection Elbow](#4-mischkrümmer--injection-elbow)
5. [Wassersammler / Waterlock](#5-wassersammler--waterlock)
6. [Schalldämpfer (Muffler)](#6-schalldämpfer-muffler)
7. [Auspuffschläuche und Leitungen](#7-auspuffschläuche-und-leitungen)
8. [Anti-Siphon-Ventil](#8-anti-siphon-ventil)
9. [Schwanenhals (Swan Neck)](#9-schwanenhals-swan-neck)
10. [Auspuff-Auslass (Transom / Hull Fitting)](#10-auspuff-auslass-transom--hull-fitting)
11. [Hydrolock-Prävention](#11-hydrolock-prävention)
12. [Systemauslegung und Dimensionierung](#12-systemauslegung-und-dimensionierung)
13. [Wartung und Inspektion](#13-wartung-und-inspektion)
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

### 1.1 Warum die Abgasanlage das kritischste System am Marine-Diesel ist

Die Abgasanlage eines Marine-Dieselmotors ist gleichzeitig das am meisten
unterschätzte und das gefährlichste System an Bord. Kein anderes System
vereint so viele Risiken in sich:

- **Kohlenmonoxid (CO)**: Ein undichter Mischkrümmer oder ein gebrochener
  Auspuffschlauch kann tödliche CO-Konzentrationen im Innenraum erzeugen.
  CO ist geruch-, farb- und geschmacklos. Jährlich sterben Bootsfahrer an
  CO-Vergiftungen, die auf defekte Abgasanlagen zurückzuführen sind.
- **Hydrolock**: Wasser, das durch die Abgasanlage zurück in die Zylinder
  gelangt, zerstört den Motor sofort und irreparabel. Kolben, Pleuel,
  Kurbelwelle — Totalschaden in Millisekunden.
- **Feuer**: Ein trockener Abgasabschnitt ohne Wassereinspritzung erreicht
  400–600 °C. Berührt er brennbares Material (Holz, GFK, Isolierung),
  entsteht ein Bootsbrand.
- **Korrosion**: Die Kombination aus heißen Abgasen, Salzwasser und
  Schwefelsäure-Kondensation greift jedes Material an. Gusseisen-
  Mischkrümmer korrodieren von innen, unsichtbar von außen.

**Statistik:**
- ~30 % aller Marine-Diesel-Ausfälle hängen mit der Abgasanlage zusammen
- Der Mischkrümmer ist das Bauteil mit der höchsten Ausfallrate am Marine-Diesel
- ~65 % aller Mischkrümmer-Ausfälle werden erst erkannt, wenn bereits
  Wasser in den Motor gelangt ist
- Geschätzte jährliche Schadenssumme allein durch Mischkrümmer-Versagen:
  >50 Mio. EUR in Europa

### 1.2 Grundprinzip: Nassauspuff vs. Trockenauspuff

In der Sportschifffahrt dominiert das Nassauspuff-System (Wet Exhaust).
Das Prinzip: Kühlwasser, das bereits den Motor durchlaufen hat, wird in
den Abgasstrom eingespritzt. Dadurch wird:

1. Das Abgas von ~400–600 °C auf ~50–70 °C gekühlt
2. Die gesamte Abgasleitung kann aus flexiblem Gummischlauch bestehen
3. Keine Hochtemperatur-Isolierung notwendig
4. Schalldämpfung durch Wasser im Gasstrom

**Nassauspuff (>95 % aller Sportboote <20 m):**
```
Motor → Mischkrümmer (Wassereinspritzung) → Auspuffschlauch →
Wassersammler/Waterlock → Schwanenhals → Auspuffschlauch →
Transom-Auslass → über Bord
```

**Trockenauspuff (<5 % der Sportboote, häufig bei Yachten >20 m):**
```
Motor → Trockener Krümmer → Isoliertes Metallrohr → Schalldämpfer →
Isoliertes Metallrohr → Schornstein/Seitenauslass → über Bord
```

### 1.3 Historische Entwicklung

Die Geschichte der marinen Abgastechnik ist eine Abfolge von
Materialverbesserungen und Sicherheitserkenntnissen:

- **1930er–1950er**: Trockenauspuff als Standard. Schwere Gussrohre,
  asbesthaltige Isolierung, ständige Brandgefahr.
- **1960er**: Einführung des Nassauspuffs durch Volvo Penta und andere.
  Erste Gusseisen-Mischkrümmer mit Wassermantel.
- **1970er**: Verbreitung des Nassauspuff-Systems in der Sportschifffahrt.
  Erste standardisierte Schalldämpfer (Vetus, Centek).
- **1980er**: Erkenntnis, dass Gusseisen-Mischkrümmer eine begrenzte
  Lebensdauer haben. Erste Edelstahl-Alternativen.
- **1990er**: Waterlock-Systeme werden Standard. Anti-Siphon-Ventile
  empfohlen. Erste Fälle von CO-Vergiftungen werden systematisch erfasst.
- **2000er**: NiCu-Legierungen (Nickel-Kupfer) für Mischkrümmer.
  Verbesserte Auspuffschlauch-Materialien.
- **2010er**: ISO 8846 und ISO 9094 verschärfen Anforderungen an
  Abgasanlagen. CO-Detektoren werden empfohlen.
- **2020er**: Einige Hersteller bieten Edelstahl-316L-Mischkrümmer als
  Standard. Intelligente Überwachungssysteme (Temperatur, Durchfluss).

### 1.4 Relevante Normen und Vorschriften

| Norm | Inhalt | Relevanz |
|------|--------|----------|
| ISO 9094 (2015) | Brandschutz | Abstände Abgasleitung zu brennbarem Material |
| ISO 8469 (2021) | Kraftstoffschläuche | Schlauchqualität, indirekt Abgas relevant |
| ISO 13363 (2016) | Nassauspuff-Systeme | Dimensionierung, Materialanforderungen |
| ISO 11105 (1997) | Belüftung Motorraum | CO-Vermeidung, Abgasführung |
| ABYC P-1 | Abgassysteme | US-Standard, strenger als ISO |
| EN 50291-2 | CO-Detektoren | Empfohlen in bewohnten Räumen |
| CE RCD 2013/53/EU | Gesamtzertifizierung | Abgasanlage Teil der CE-Konformität |

### 1.5 Die Abgasanlage im AYDI-Analysesystem

Die AYDI-Analyse bewertet die Abgasanlage als Subsystem der
Motor-/Antriebsbewertung mit folgenden Schwerpunkten:

- **Strukturelle Analyse (Pipeline A)**: Alter, Material, Dimensionierung,
  Komponentenspezifikation, bekannte Schwachstellen des Motormodells
- **Visuelle Analyse (Pipeline B)**: Korrosionsspuren, Verfärbungen,
  Rissbildung, Schlauchzustand, Schellen, Auslass-Zustand
- **Text-Analyse (Pipeline C)**: Wartungsberichte, Surveyor-Befunde,
  Herstellerrückrufe, Versicherungsschäden

**Konfidenz-Besonderheit Abgasanlage:**
Der Mischkrümmer korrodiert primär von innen. Eine äußerlich makellose
Oberfläche sagt nichts über den Innenzustand. Daher wird die visuelle
Konfidenz für Mischkrümmer auf maximal `visual_medium` begrenzt, mit dem
Hinweis: "Innere Korrosion nicht visuell beurteilbar — Endoskopie oder
Demontage empfohlen."

---
---

## 2. Nassauspuff-System (Wet Exhaust)

### 2.1 Funktionsprinzip im Detail

Das Nassauspuff-System nutzt das bereits erwärmte Motorkühlwasser
(bei Seewasser-gekühlten Motoren) oder den Seewasserkreislauf
(bei Zweikreis-Kühlsystemen), um die Abgase zu kühlen. Der Prozess
verläuft in folgenden Schritten:

**Schritt 1 — Abgaserzeugung:**
Der Diesel verbrennt Kraftstoff bei ~1.800–2.200 °C im Zylinder.
Die Abgase verlassen den Zylinderkopf mit ~400–600 °C und gelangen
in den Abgaskrümmer.

**Schritt 2 — Wassereinspritzung am Mischkrümmer:**
Am Injection Elbow (Mischkrümmer) wird Kühlwasser — typisch 15–40 Liter
pro Minute je nach Motorgröße — in den Abgasstrom eingespritzt. Das Wasser
verdampft teilweise, kühlt die Gase auf ~50–70 °C und erzeugt ein
Wasser-Dampf-Abgas-Gemisch.

**Schritt 3 — Transport durch Auspuffschlauch:**
Das gekühlte Gemisch fließt durch einen flexiblen Auspuffschlauch
(typisch 75–150 mm Durchmesser) zum Wassersammler.

**Schritt 4 — Wassersammler / Waterlock:**
Im Wassersammler trennt sich das Wasser teilweise vom Gas. Der
Waterlock verhindert, dass Wasser bei Rückstau (Welle, Wind, Gegenmotor)
zurück zum Motor fließt.

**Schritt 5 — Schwanenhals:**
Der Schwanenhals (ein invertiertes U-Rohr) führt die Leitung auf
einen Hochpunkt über der maximalen Wasserlinie. Dies ist die primäre
Barriere gegen Wasserrückfluss.

**Schritt 6 — Abführung zum Auslass:**
Vom Schwanenhals fällt das Gemisch zum Transom-Auslass oder
Seitenauslass, wo es über Bord geleitet wird.

### 2.2 Systemkomponenten-Übersicht

| Komponente | Funktion | Typisches Material | Lebensdauer |
|------------|----------|-------------------|-------------|
| Mischkrümmer | Wassereinspritzung | Gusseisen, Edelstahl, NiCu | 4–15 Jahre |
| Steigleitung | Motor → Mischkrümmer | Edelstahl, Gusseisen | Motorlebensdauer |
| Auspuffschlauch | Flexible Verbindung | Gummi/EPDM, verstärkt | 5–8 Jahre |
| Wassersammler | Wasser-/Gas-Trennung | Kunststoff, GFK, Edelstahl | 10–20 Jahre |
| Schwanenhals | Rückflusssicherung | Gummi, GFK, Edelstahl | 8–15 Jahre |
| Anti-Siphon-Ventil | Siphon-Schutz | Kunststoff, Bronze | 3–8 Jahre |
| Transom-Auslass | Austritt über Bord | Edelstahl 316, Bronze | 15–25 Jahre |
| Schlauchschellen | Verbindungssicherung | Edelstahl 316 | 5–10 Jahre |
| Schalldämpfer | Geräuschreduktion | GFK, Kunststoff, Edelstahl | 10–15 Jahre |

### 2.3 Dimensionierungsregeln

Die korrekte Dimensionierung der Nassauspuffanlage ist entscheidend.
Zu enge Leitungen erzeugen Gegendruck, der den Motor schädigt und
Leistung kostet. Zu weite Leitungen verlangsamen den Durchfluss, was
zu Ablagerungen und unzureichender Kühlung führt.

**Schlauch-Innendurchmesser nach Motorleistung:**

| Motorleistung (PS) | Mindest-ID Schlauch (mm) | Empfohlen (mm) |
|--------------------|--------------------------|----------------|
| 10–20 | 38 | 45 |
| 20–40 | 45 | 50 |
| 40–75 | 50 | 60 |
| 75–120 | 60 | 75 |
| 120–200 | 75 | 90 |
| 200–350 | 90 | 100 |
| 350–500 | 100 | 120 |
| 500–800 | 120 | 150 |

**Maximaler Gegendruck:**
- Saugmotor: max. 50 mbar (500 mm Wassersäule)
- Turbomotor: max. 40 mbar (400 mm Wassersäule)
- Gegendruck >60 mbar: Leistungsverlust >5 %, erhöhte Abgastemperatur

**Berechnung des Gegendrucks:**
```
Gegendruck (mbar) = Reibungsverlust + Höhendifferenz + Schalldämpfer
Reibungsverlust ≈ (Schlauchlänge / Schlauchdurchmesser) × Faktor × Durchfluss²
Höhendifferenz = Δh (m) × 100 (mbar/m) [nur für Wassersäule im Schlauch]
Schalldämpfer ≈ 5–15 mbar (herstellerabhängig)
```

### 2.4 Kritische Steigungen und Gefälle

Die Auspuffleitung muss ein kontinuierliches Gefälle vom Motor zum
Auslass aufweisen. Jede Senke bildet einen Wasseransammelpunkt, der:

- Gegendruck erhöht
- Bei Motorabschaltung Wasser staut
- Korrosion beschleunigt
- Bei Frost Eisschaden verursacht

**Mindestgefälle:**
- Horizontale Abschnitte: min. 10 mm/m Gefälle zum Auslass
- Vom Schwanenhals zum Auslass: min. 15 mm/m Gefälle
- Keine Senken zwischen Wassersammler und Auslass

**Maximale Steigung Motor → Schwanenhals:**
- Die Steigleitung vom Motor zum Schwanenhals-Hochpunkt darf
  nicht mehr als 45° gegenüber der Horizontalen betragen
- Empfohlen: 20–30° Steigung
- Länge der Steigleitung: max. 3 m bis zum Schwanenhals

### 2.5 Nassauspuff bei Segelyachten: Besonderheiten

Segelyachten stellen besondere Anforderungen an die Abgasanlage:

- **Krängung**: Bei 20–25° Krängung ändert sich der Wasserstand im
  Auspuffsystem. Der Auslass kann unter Wasser geraten. Der Schwanenhals
  muss für den gekrängten Zustand dimensioniert sein.
- **Heckwelle**: Bei schwerer See oder Surfen kann die Heckwelle den
  Auspuffauslass überfluten. Das System muss so dimensioniert sein,
  dass kurzzeitige Überflutung toleriert wird.
- **Niedriger Freibord achtern**: Viele Segelyachten haben einen niedrigen
  Freibord am Heck. Der Auspuffauslass liegt oft nur 150–300 mm über
  der Wasserlinie. Das erhöht das Risiko des Wasserrückflusses.
- **Seltener Motorbetrieb**: Wenn der Motor selten läuft, trocknet die
  Abgasanlage zwischen den Einsätzen aus — und dann wieder Salzwasser.
  Dieses Nass-Trocken-Wechseln beschleunigt die Korrosion.
- **Motorposition tief in der Bilge**: Bei vielen Segelyachten sitzt
  der Motor sehr tief, manchmal unter der Wasserlinie. Das macht
  die Abgasführung nach oben zum Schwanenhals besonders kritisch.

### 2.6 Nassauspuff bei Motoryachten: Besonderheiten

Motoryachten haben andere Herausforderungen:

- **Höhere Leistung = mehr Abgas**: Zwei 300-PS-Motoren produzieren
  erheblich mehr Abgas und Kühlwasser als ein 40-PS-Segelyacht-Diesel.
  Die Dimensionierung muss entsprechend größer sein.
- **Twin-Engine-Installationen**: Zwei separate Abgassysteme, die sich
  oft den Platz teilen. Keine Querverbindung zwischen den Systemen.
- **Flybridge / Oberdeck**: Abgase müssen so geführt werden, dass sie
  nicht in den Flybridge-Bereich gelangen. CO-Risiko.
- **Generator**: Zusätzliches Abgassystem für den Generator, oft
  vergessen bei der Wartung.
- **Planing-Boote**: Bei hoher Geschwindigkeit ändert sich der Trimm
  erheblich. Der Schwanenhals-Hochpunkt muss für alle Trimmlagen
  über der Wasserlinie bleiben.

---
---

## 3. Trockenauspuff-System (Dry Exhaust)

### 3.1 Funktionsprinzip

Beim Trockenauspuff wird kein Kühlwasser in den Abgasstrom eingespritzt.
Die Abgase bleiben trocken und heiß — typisch 350–500 °C am Austritt.
Dies erfordert:

- Hochtemperaturbeständige Rohre (Edelstahl, Stahl mit Keramikbeschichtung)
- Umfangreiche Wärmeisolierung aller Rohrabschnitte
- Mindestabstände zu brennbaren Materialien (gem. ISO 9094: 200 mm zu
  Holz, 150 mm zu GFK ohne Isolierung)
- Trockene Schalldämpfer (reaktiv oder absorptiv)
- Vertikalen oder seitlichen Auslass (nie unter der Wasserlinie)

### 3.2 Einsatzbereiche

Der Trockenauspuff ist Standard bei:

- **Motoryachten >20 m / Superyachten**: Eleganter Schornstein,
  Abgase werden hoch über Deck geleitet. Kein Kühlwasser-Gestank.
- **Fischkutter und Arbeitsboote**: Robuste Systeme, die jahrzehnte-
  lang halten. Weniger korrosionsanfällig als Nassauspuff.
- **Motorboote mit Hochleistungsmotoren >800 PS**: Der Kühlwasserbedarf
  eines Nassauspuffs wäre bei diesen Leistungen extrem hoch.
- **Stahlboote**: Oft werksseitig mit Trockenauspuff, da die Rohrführung
  in Stahl einfacher und die Brandgefahr geringer ist.
- **Nachtrüstung bei wiederholtem Nassauspuff-Versagen**: Manche Eigner
  konvertieren nach dem dritten Mischkrümmer-Schaden auf Trockenauspuff.

### 3.3 Komponenten des Trockenauspuffs

| Komponente | Material | Temperaturbereiche |
|------------|----------|-------------------|
| Auspuffkrümmer | Gusseisen, Edelstahl 310S/316Ti | 400–650 °C |
| Kompensator (Faltenbalg) | Edelstahl 321/316Ti | 300–550 °C |
| Auspuffrohr | Edelstahl 316L/310S, Stahl verzinkt | 250–500 °C |
| Isolierung | Keramikfaser, Steinwolle (maritim) | Bis 1.000 °C |
| Isolierung Ummantelung | Aluminium-Blech, Edelstahl | Oberflächentemp. <60 °C |
| Trockener Schalldämpfer | Edelstahl mit Absorptionsfüllung | 300–500 °C |
| Regenwasserkappe | Edelstahl 316L | Umgebung |
| Decksdurchführung | Edelstahl mit Hitze-Isolation | 200–400 °C |

### 3.4 Isolierungsanforderungen

Die Isolierung eines Trockenauspuffs ist lebens- und schiffskritisch.
Eine unzureichende Isolierung hat schon zahlreiche Bootsbrände verursacht.

**Isolierungsmindestdicken (gem. ISO 9094 / ABYC P-1):**

| Abgastemperatur | Mindest-Isolierdicke | Ergebnis Oberfläche |
|-----------------|---------------------|---------------------|
| 200–300 °C | 25 mm Keramikfaser | <60 °C |
| 300–400 °C | 40 mm Keramikfaser | <60 °C |
| 400–500 °C | 50 mm Keramikfaser | <60 °C |
| 500–600 °C | 75 mm Keramikfaser | <60 °C |

**Ziel**: Die Oberflächentemperatur der Isolierung darf nirgends 60 °C
überschreiten (Berührungsschutz) und muss mindestens 200 mm Abstand zu
brennbaren Materialien einhalten, auch mit Isolierung.

**Isolierungsmaterialien im Vergleich:**

| Material | Temp.-Bereich | Vor-/Nachteile |
|----------|--------------|----------------|
| Keramikfaser-Matte | Bis 1.260 °C | Leicht, flexibel, kein Wasser-Sauger |
| Steinwolle (maritim) | Bis 750 °C | Preiswert, schwerer, saugt Feuchtigkeit |
| Kalziumsilikat-Platte | Bis 1.000 °C | Formstabil, für starre Ummantelungen |
| Aerogel-Matte | Bis 650 °C | Sehr dünn bei hoher Isolierwirkung, teuer |
| Asbest (historisch) | Bis 1.500 °C | VERBOTEN seit 2005, bei Altbooten prüfen |

### 3.5 Schalldämpfung im Trockensystem

Trockene Schalldämpfer arbeiten nach zwei Prinzipien:

**Absorptionsschalldämpfer:**
- Schallenergie wird durch poröses Material (Glasfaser, Edelstahlwolle) absorbiert
- Wirksam bei mittleren und hohen Frequenzen (>500 Hz)
- Einfacher Aufbau: perforiertes Innenrohr + Absorptionsmaterial + Außenmantel
- Wartung: Absorptionsmaterial erneuern alle 5–10 Jahre
- Typische Dämpfung: 15–25 dB(A)

**Reaktionsschalldämpfer (Reflexion):**
- Schallwellen werden durch Querschnittsänderungen und Kammern reflektiert
- Wirksam bei niedrigen Frequenzen (<500 Hz) — dem typischen Diesel-Brummen
- Komplexerer Aufbau: Mehrkammer-System mit definierten Volumina
- Wartungsfrei, aber größer und schwerer
- Typische Dämpfung: 20–35 dB(A)

**Kombinationsschalldämpfer:**
- Vereinen beide Prinzipien
- Breitbandige Dämpfung: 25–40 dB(A)
- Eingesetzt bei Superyachten mit hohen Komfortanforderungen

### 3.6 Decksdurchführung und Schornstein

Bei Yachten mit Trockenauspuff muss die Abgasleitung durch das Deck
nach oben geführt werden. Kritische Punkte:

- **Decksdurchführung**: Muss hitzebeständig und wasserdicht sein.
  Spezielle Manschetten aus Silikon/PTFE mit Edelstahlkragen.
- **Schornstein**: Sollte mindestens 500 mm über dem höchsten begehbaren
  Deck enden, um CO-Gefährdung zu minimieren.
- **Regenwasserkappe**: Verhindert Wassereindrung in den Trockenauspuff.
  Muss den Abgasstrom nicht blockieren (Gegendruck).
- **Funkenfänger**: Bei Holzbooten oder in Naturschutzgebieten
  vorgeschrieben. Edelstahlnetz im Schornsteinkopf.

### 3.7 Abgasrückführung (EGR) bei Marine-Diesel

Einige moderne Marine-Diesel (ab EU Stage V / EPA Tier 4) verwenden
Abgasrückführung (Exhaust Gas Recirculation, EGR) zur NOx-Reduktion.
Dies hat Auswirkungen auf die Abgasanlage:

- **EGR-Kühler**: Zusätzlicher Wärmetauscher im Abgasstrom, der einen
  Teil der Abgase kühlt und in den Ansaugtrakt zurückführt
- **Erhöhte Korrosion**: Rückgeführte Abgase erhöhen den
  Schwefelsäure-Kondensationsanteil → aggressiverer Angriff auf Mischkrümmer
- **Rußpartikel**: EGR erhöht die Rußbelastung im Abgas →
  schnellere Ablagerungen in Schläuchen und Wassersammler
- **Wartungsintensität**: EGR-Ventil und EGR-Kühler als zusätzliche
  Wartungspunkte → verkürzte Inspektionsintervalle für Abgasanlage

**Betroffene Motoren (Sportschifffahrt):**
- Volvo Penta D3/D4/D6 (neuere Generationen)
- MAN V8/V12 Marine
- Cummins QSB/QSC (neuere Generationen)
- Hinweis: Die meisten Segelyacht-Motoren <100 PS sind (noch) NICHT
  mit EGR ausgestattet

### 3.8 Konversion Nassauspuff → Trockenauspuff

In manchen Fällen lohnt sich die Umrüstung:

**Vorteile der Konversion:**
- Keine Mischkrümmer-Korrosion mehr
- Kein Hydrolock-Risiko
- Längere Lebensdauer des Gesamtsystems
- Bessere Motoreffizienz (weniger Gegendruck)
- Kein Kühlwasser im Abgas (sauberer Auslass)

**Nachteile der Konversion:**
- Hohe Kosten (5.000–15.000 EUR je nach Installation)
- Brandschutz-Isolierung erforderlich
- Mehr Wärmeabstrahlung im Motorraum
- Höherer Geräuschpegel ohne spezielle Schalldämpfer
- Platz für Rohre und Isolierung notwendig
- Decksdurchbruch nötig (Leck-Risiko)

**Wann es sich lohnt:**
- Gusseisen-Mischkrümmer bereits 2× oder öfter ersetzt
- Motor hat noch >5.000 Stunden Restlebensdauer
- Stahlboot (einfachere Rohrführung)
- Eigentümer behält das Boot langfristig (>10 Jahre)

---
---

## 4. Mischkrümmer / Injection Elbow

### 4.1 Warum der Mischkrümmer DAS kritischste Bauteil am Marine-Diesel ist

Der Mischkrümmer (engl. Mixing Elbow, Injection Elbow, Exhaust Elbow)
ist der Punkt, an dem heißes Abgas und kühles Seewasser aufeinandertreffen.
Diese Kombination macht ihn zum Bauteil mit der höchsten Beanspruchung
und der kürzesten Lebensdauer am gesamten Motor:

- **Thermische Belastung**: 400–600 °C Abgas trifft auf 15–30 °C Seewasser
- **Chemische Belastung**: Schwefelsäure-Kondensation, Salzwasser-Korrosion
- **Erosion**: Sandpartikel im Kühlwasser schleifen die Innenwände
- **Thermal Cycling**: Bei jedem Start/Stopp massive Temperaturwechsel
- **Galvanische Korrosion**: Verschiedene Metalle im Kontakt mit Salzwasser

**Lebensdauer nach Material:**

| Material | Mittlere Lebensdauer | Bestfall | Schlechtfall |
|----------|---------------------|----------|-------------|
| Gusseisen | 5–8 Jahre | 12 Jahre | 3 Jahre |
| Edelstahl 316L | 10–15 Jahre | 20+ Jahre | 7 Jahre |
| NiCu-Legierung (Ni-Resist) | 12–20 Jahre | 25+ Jahre | 8 Jahre |
| Bronze | 8–12 Jahre | 15 Jahre | 5 Jahre |

### 4.2 Aufbau und Funktion

Der Mischkrümmer ist ein Guss- oder Schweißteil, das folgende Aufgaben
gleichzeitig erfüllt:

1. **Abgassammlung**: Nimmt die Abgase aus dem Motorauspuffkrümmer auf
2. **Wassereinspritzung**: Leitet Kühlwasser in den Abgasstrom ein
3. **Umlenkung**: Lenkt den kombinierten Strom nach unten/hinten
4. **Mischung**: Sorgt für gleichmäßige Vermischung von Wasser und Abgas

**Typischer Aufbau:**
```
Motorseite:
├── Flansch zum Motorauspuffkrümmer (trocken, heiß)
├── Wassereinlass (¾"–1½" Anschluss vom Kühlwassersystem)
├── Mischzone (Wasser trifft Abgas, ~90° Umlenkung)
└── Auslass zum Auspuffschlauch (nass, gekühlt)
```

### 4.3 Materialien im Detail

#### 4.3.1 Gusseisen (klassisch)

Der traditionelle Werkstoff für Mischkrümmer:

- **Hersteller**: Volvo Penta, Yanmar, Perkins — alle OEM-Krümmer bis
  ~2015 waren Gusseisen
- **Vorteile**: Preiswert (150–400 EUR), gute Gießbarkeit, bewährte Form
- **Nachteile**: Korrodiert von innen durch Salzwasser und Schwefelsäure,
  Durchrostung nicht von außen erkennbar, manchmal plötzliches Versagen
- **Typische Lebensdauer**: 1.500–3.000 Betriebsstunden / 5–8 Jahre
- **Versagensmechanismus**: Interne Rostschichten wachsen, verengen den
  Wasserkanal, reduzieren die Kühlung, beschleunigen die Korrosion →
  Durchrostung → Wasser in den Motor

**Inspektion Gusseisen-Krümmer:**
- Äußerlich: Rostspuren, Verfärbungen, Rissbildung, weiße Salzablagerungen
- Klopftest: Dumpfer Klang = Wandstärke noch OK; hohl/dünn = Abtrag
- Endoskopie: Kamera durch den Auspuffschlauch-Anschluss
- Drucktest: Wasserkanal unter Druck setzen, auf Leckage prüfen
- Gewichtsvergleich: Stark korrodierter Krümmer ist leichter als Neuteil

#### 4.3.2 Edelstahl 316L

Die moderne Alternative für Hochleistungs- und Langzeit-Installationen:

- **Hersteller**: Vetus, Barr Marine, Osco (Aftermarket), manche OEM
- **Legierung**: AISI 316L (1.4404) mit niedrigem Kohlenstoffgehalt
  - Cr: 16–18 %, Mo: 2–3 %, Ni: 10–14 %, C: <0.03 %
- **Vorteile**: Korrosionsbeständig, langlebig, visuell inspizierbar
  (blanke Oberfläche zeigt Verfärbungen sofort)
- **Nachteile**: Teurer (500–1.200 EUR), empfindlich gegen Spaltkorrosion,
  Chlorid-induzierte Spannungsrisskorrosion bei >60 °C möglich
- **Typische Lebensdauer**: 3.000–6.000 Betriebsstunden / 10–15 Jahre
- **Wartung**: Jährliche Inspektion auf Verfärbungen, Rissbildung, Spaltkorrosion
  an Flanschverbindungen

**Achtung**: Nicht jeder "Edelstahl"-Krümmer ist 316L. Billige
Nachbauten verwenden 304 (1.4301), das in Salzwasser deutlich schneller
korrodiert. Immer Werkszertifikat oder Materialnummer prüfen.

#### 4.3.3 NiCu-Legierung (Ni-Resist / Monel-ähnlich)

Die Premium-Option für maximale Lebensdauer:

- **Hersteller**: Volvo Penta (neuere Modelle), Yanmar (Premium-Linie)
- **Legierung**: Nickel-Kupfer-Gusseisen (Ni-Resist Typ D2 oder ähnlich)
  - Ni: 18–22 %, Cu: 5–7 %, Cr: 1,5–2,5 %, Rest Fe
- **Vorteile**: Hervorragende Salzwasserbeständigkeit, thermisch stabil,
  keine Spannungsrisskorrosion, nahezu galvanisch neutral in Seewasser
- **Nachteile**: Sehr teuer (800–2.500 EUR), schwerer, weniger Anbieter
- **Typische Lebensdauer**: 5.000–10.000 Betriebsstunden / 12–20 Jahre
- **Einsatz**: Empfohlen für Fahrtenyachten, Charterboote, tropische Gewässer

#### 4.3.4 Bronze (Sonderfälle)

Selten, aber bei einigen älteren Motoren und Spezialanwendungen:

- **Einsatz**: Ältere Lehman-Ford-Motoren, einige Perkins-Marinisierungen
- **Legierung**: Aluminiumbronze oder Nickelbronze
- **Vorteile**: Gute Seewasserbeständigkeit, natürliches Antifouling
- **Nachteile**: Enthärtung (Entzinkung bei Messingteilen), teuer, schwer
- **Lebensdauer**: 3.000–5.000 Stunden / 8–12 Jahre

### 4.4 OEM vs. Aftermarket: Qualitätsunterschiede

**Volvo Penta Genuine Mischkrümmer:**
- Genaue Passung garantiert
- Material: Gusseisen (ältere Modelle) oder NiCu (neuere Modelle)
- Preis: 400–2.000 EUR je nach Motor
- Garantie: 24 Monate / 1.000 Betriebsstunden
- Volvo Penta Teilenummern:
  - D1-30: 3580918 (Gusseisen), 22898216 (NiCu)
  - D2-40/55/75: 22840507
  - MD2040: 3583608
  - D4/D6: 3589907 / 21469181
  - 2003: 3580918

**Aftermarket-Alternativen (Beispiele):**

| Hersteller | Material | Passend für | Preis (ca.) |
|------------|----------|-------------|-------------|
| Barr Marine | Gusseisen/Edelstahl | Volvo, Yanmar, Perkins, Lehman | 250–800 EUR |
| Osco | Edelstahl 316L | Volvo, Yanmar, Westerbeke | 400–1.000 EUR |
| Vetus | Edelstahl 316L | Universal-Anschlüsse | 350–900 EUR |
| Centek | Edelstahl 316L | Volvo, Yanmar, Universal | 350–950 EUR |
| MarineLine | Beschichtetes Gusseisen | Volvo, Yanmar | 200–500 EUR |

**Qualitätsrisiken Aftermarket:**
- Ungenaue Passform → Dichtungsprobleme → Abgasleck → CO-Gefahr
- Minderwertiges Material (304 statt 316L) → frühe Korrosion
- Fehlende Wasserkanal-Optimierung → ungleichmäßige Kühlung → Hotspots
- Keine Dichtsätze mitgeliefert → Wiederverwendung alter Dichtungen
- Mangelnde CE-Dokumentation → Problem bei Versicherungsschäden

### 4.5 Mischkrümmer-Wartung und Inspektion

**Jährliche Inspektion (Empfohlen):**

1. Äußere Sichtprüfung auf Rost, Verfärbungen, Risse, Wasseraustritt
2. Schlauchschellen am Ein- und Ausgang prüfen (Festigkeit, Rost)
3. Kühlwasserfluss kontrollieren: Tritt Wasser gleichmäßig am Auslass aus?
4. Abgastemperatur messen: Infrarot-Thermometer am Krümmer-Ausgang.
   >80 °C = Kühlungsproblem. >100 °C = sofort Motor stoppen, untersuchen.
5. Abgas optisch prüfen: Normales Nassauspuff-Abgas ist durchsichtig bis
   leicht weiß. Blaues Abgas = Ölverbrennung. Schwarzes Abgas = unvollständige
   Verbrennung.

**Alle 500 Betriebsstunden / alle 3 Jahre (je nachdem, was zuerst):**

1. Mischkrümmer demontieren und inspizieren
2. Innenraum auf Korrosionsabtrag prüfen (Messschieber: Wandstärke)
3. Wasserkanäle auf Verstopfung prüfen (Durchspülen mit Essigwasser)
4. Zink-Anode im Kühlwassersystem erneuern (falls vorhanden)
5. Dichtungen und O-Ringe erneuern
6. Bei >30 % Wandstärkenverlust: sofort ersetzen

**Kritische Verschleißgrenze:**
- Gusseisen: Wandstärke <3 mm an dünnster Stelle → Ersatz
- Edelstahl 316L: Wandstärke <1,5 mm → Ersatz
- NiCu: Wandstärke <2 mm → Ersatz

### 4.6 Mischkrümmer-Tausch: Anleitung

Der Tausch eines Mischkrümmers ist eine typische DIY-Arbeit für
versierte Bootseigner. Zeitaufwand: 2–4 Stunden.

**Werkzeug und Material:**
- Ringschlüssel / Steckschlüssel passend (typisch 13, 16, 19 mm)
- Neuer Mischkrümmer mit Dichtsatz
- Neue Schlauchschellen Edelstahl 316 (T-Bolt-Schellen bevorzugt)
- Hochtemperatur-Dichtmasse (z. B. Permatex Ultra Copper)
- Auffangwanne (Kühlwasser wird auslaufen)
- Drahtbürste, WD-40 für festsitzende Schrauben
- Optional: Drehmomentschlüssel für Flanschschrauben

**Vorgehensweise:**
1. Motor kalt. Seewasserventil schließen.
2. Kühlwasserschlauch am Mischkrümmer lösen (Wasser auffangen)
3. Auspuffschlauch vom Mischkrümmer lösen
4. Befestigungsschrauben/-muttern am Motorflansch lösen
   (Vorsicht: oft festgerostet, WD-40 vorher einwirken lassen)
5. Alten Mischkrümmer abnehmen
6. Flanschfläche am Motor reinigen (Drahtbürste, kein Schaber der kratzt)
7. Neue Dichtung auflegen (NIEMALS alte Dichtung wiederverwenden)
8. Neuen Mischkrümmer montieren, Schrauben über Kreuz anziehen
   (Drehmoment gem. Herstellerangabe, typisch 25–35 Nm)
9. Kühlwasserschlauch anschließen, neue T-Bolt-Schelle
10. Auspuffschlauch anschließen, neue Schelle
11. Seewasserventil öffnen
12. Motor starten, auf Lecks prüfen (Wasser + Abgas)
13. Probelauf 15 min, dabei Temperatur überwachen

---
---

## 5. Wassersammler / Waterlock

### 5.1 Funktionsprinzip

Der Wassersammler (engl. Waterlock, Water Separator) ist ein Behälter im
Nassauspuff-System, der zwei entscheidende Aufgaben erfüllt:

1. **Wasserabscheidung**: Trennt einen Teil des Kühlwassers vom Abgasstrom,
   damit nicht die gesamte Wassermenge durch den Schwanenhals gedrückt
   werden muss.
2. **Rückflussbarriere**: Das stehende Wasser im Behälter bildet eine
   Barriere, die verhindert, dass Abgase oder Wasser zurück zum Motor
   fließen, wenn der Motor steht.

**Funktionsweise:**
```
Einlass (von Motor/Mischkrümmer) → Abgas+Wasser strömen ein
├── Wasser setzt sich durch Schwerkraft ab (sammelt sich unten)
├── Abgas steigt nach oben zum Auslass
└── Bei nächstem Motorstart: Wasser wird durch Gasdruck ausgetrieben
Auslass (zum Schwanenhals/Auslass) → gekühltes Abgas + etwas Wasser
```

### 5.2 Dimensionierung

Der Wassersammler muss groß genug sein, um das gesamte Wasser aufzunehmen,
das sich im System befindet, wenn der Motor abstellt. Andernfalls fließt
das Wasser zurück zum Motor (Hydrolock-Gefahr).

**Faustformel für das Mindestvolumen:**
```
V_waterlock (Liter) = Volumen der Auspuffleitung Motor→Waterlock (Liter)
                     + 1 Liter Sicherheitsreserve je 30 PS
                     + Nachlauf-Volumen (Kühlwasser, das nach Motorstopp nachläuft)
```

**Praxis-Empfehlungen:**

| Motorleistung | Mindest-Waterlock-Volumen | Empfohlenes Volumen |
|--------------|--------------------------|---------------------|
| 10–30 PS | 3 Liter | 4–5 Liter |
| 30–75 PS | 5 Liter | 8–10 Liter |
| 75–150 PS | 10 Liter | 12–15 Liter |
| 150–300 PS | 15 Liter | 20–25 Liter |
| 300–500 PS | 25 Liter | 30–40 Liter |

### 5.3 Hersteller und Modelle

#### 5.3.1 Vetus

Der Marktführer für marine Waterlock-Systeme:

| Modell | Volumen | Anschlüsse | Geeignet für | Preis (ca.) |
|--------|---------|-----------|-------------|-------------|
| NLPH40 | 4,3 L | 40 mm | 10–30 PS | 80 EUR |
| NLPH50 | 7,5 L | 50 mm | 20–55 PS | 110 EUR |
| NLPH60 | 10 L | 60 mm | 40–75 PS | 130 EUR |
| NLPH75 | 14 L | 75 mm | 60–120 PS | 160 EUR |
| NLPH90 | 22 L | 90 mm | 100–200 PS | 210 EUR |
| NLP90 | 35 L | 90 mm | 150–350 PS | 280 EUR |
| NLP100 | 50 L | 100 mm | 250–500 PS | 380 EUR |

**Vetus-Besonderheit**: Die NLPH-Serie hat eine integrierte
Hubkammer (Lift Muffler), die gleichzeitig als Schalldämpfer und
Wassersammler fungiert. Die NLP-Serie ist nur Wassersammler.

#### 5.3.2 Centek Industries

US-Hersteller mit patentierten Vernalift-Systemen:

| Modell | Volumen | Anschlüsse | Geeignet für | Preis (ca.) |
|--------|---------|-----------|-------------|-------------|
| Vernalift 1000 | 3,8 L | 38 mm | 10–25 PS | 120 EUR |
| Vernalift 1500 | 5,7 L | 50 mm | 20–50 PS | 150 EUR |
| Vernalift 2000 | 11 L | 63 mm | 40–100 PS | 200 EUR |
| Vernalift 3000 | 19 L | 75 mm | 75–200 PS | 280 EUR |
| Vernalift 4000 | 30 L | 90 mm | 150–400 PS | 380 EUR |
| Vernalift GRP | 45 L | 100 mm | 300–600 PS | 500 EUR |

**Centek-Besonderheit**: Glasfaser-verstärkter Kunststoff (GRP),
leichter und korrosionsbeständiger als Edelstahl.

#### 5.3.3 Kunststoff-Wassersammler (Custom / Bootsbau)

Viele Bootswerften fertigen eigene Wassersammler aus GFK oder
Polyethylen. Qualität variiert stark:

- **Gut**: Ausreichend dimensioniert, glatte Innenflächen, stabile
  Schlauchanschlüsse, Ablassventil am Tiefpunkt
- **Mangelhaft**: Zu klein, scharfe Kanten innen (Ablagerungsfallen),
  schlecht zugänglich, kein Ablassventil

### 5.4 Einbau-Richtlinien

- **Position**: So tief wie möglich, aber über der Bilgenwasserlinie
- **Zugänglichkeit**: Muss für Reinigung und Inspektion erreichbar sein
- **Befestigung**: Stabil montiert — der volle Wassersammler wiegt
  erheblich (10 L Wasser = 10 kg + Eigengewicht)
- **Ablassventil**: Am tiefsten Punkt ein Ablasshahn oder -stopfen
  für Winterentleerung und Reinigung
- **Mindestabstand zum Motor**: 300 mm (Wärmeschutz)
- **Schläuche**: Einlass oben, Auslass ebenfalls oben oder seitlich oben.
  Niemals Auslass unter dem Einlass.

### 5.5 Wartung

- **Jährlich**: Innenraum inspizieren, Ablagerungen entfernen
  (Rußschlämme, Salzablagerungen, Biomasse)
- **Alle 2 Jahre**: Schlauchschellen ersetzen, Schlauchsitz prüfen
- **Alle 5 Jahre**: Kunststoff-Wassersammler auf Rissbildung prüfen
  (UV-Degradation auch im Motorraum möglich durch Belüftungsöffnungen)
- **Winterlager**: Komplett entleeren (Frostschaden). Ablassventil öffnen.
- **Nach Salzwassersaison**: Durchspülen mit Süßwasser empfohlen

---
---

## 6. Schalldämpfer (Muffler)

### 6.1 Schalldämpfung im Nassauspuff

Die Schalldämpfung im Nassauspuff-System ist einfacher als im
Trockenauspuff, da das Wasser selbst bereits erheblich dämpft.
Dennoch sind spezielle Schalldämpfer bei den meisten Installationen
Standard — und bei Yachten mit Komfortanspruch unverzichtbar.

**Geräuschquellen im Nassauspuff:**
- Motorauspuff-Pulsation (tieffrequent, 50–200 Hz)
- Turbolader-Pfeifen (hochfrequent, 2.000–8.000 Hz)
- Wasser-Gurgeln im Schlauch (breitbandig, 100–2.000 Hz)
- Auslass-Spritzen/Plätschern (breitbandig, 200–5.000 Hz)

### 6.2 Nassauspuff-Schalldämpfer-Typen

#### 6.2.1 Lift Muffler (Hubschalldämpfer)

Der Lift Muffler kombiniert Schalldämpfung mit der Waterlock-Funktion.
Das Abgas/Wasser-Gemisch wird in einem vertikalen Behälter gesammelt,
das Wasser setzt sich unten ab, und das gedämpfte Abgas steigt nach
oben zum Auslass.

**Vorteile:**
- Kompakt: Zwei Funktionen in einem Bauteil
- Gute Tiefton-Dämpfung durch Volumenexpansion
- Standard-Lösung für Segelyachten und kleine Motorboote

**Nachteile:**
- Begrenzte Dämpfung bei hohen Frequenzen
- Bei Überdimensionierung zu viel stehendes Wasser (Gewicht, Hydrolock-Risiko)

**Typische Produkte:**
- Vetus NLPH-Serie (40–90 mm)
- Centek Vernalift-Serie
- Halyard Marine Waterlock-Muffler

#### 6.2.2 Resonanzschalldämpfer

Speziell abgestimmte Kammern, die bestimmte Frequenzen auslöschen:

- **Helmholtz-Resonator**: Kammer mit definiertem Halsquerschnitt,
  abgestimmt auf die Motordrehzahl-Grundfrequenz
- **Viertelwellen-Resonator**: Seitenkanal mit Länge λ/4 der zu
  dämpfenden Frequenz
- **Einsatz**: Ergänzend zum Lift Muffler bei Motorbooten mit
  besonders störendem Tiefton

#### 6.2.3 Inline-Schalldämpfer

Rohrförmige Schalldämpfer, die in die Auspuffleitung eingesetzt werden:

**Vetus Produkte:**
| Modell | Durchmesser | Dämpfung | Einsatz |
|--------|------------|----------|---------|
| DEMPMP40 | 40 mm | ~10 dB(A) | Zusätzliche Dämpfung |
| DEMPMP50 | 50 mm | ~10 dB(A) | Zusätzliche Dämpfung |
| DEMPMP75 | 75 mm | ~12 dB(A) | Zusätzliche Dämpfung |
| DEMPMP90 | 90 mm | ~12 dB(A) | Zusätzliche Dämpfung |

### 6.3 Schalldämpfer-Dimensionierung

**Schalldämpfer-Volumen:**
```
V_muffler ≥ 10 × V_zylinder_gesamt × (n / 60)
```
Wobei: V_zylinder_gesamt = Hubraum, n = typische Betriebsdrehzahl

**Praxis**: Ein 2-Liter-Diesel bei 2.500 U/min benötigt:
```
V_muffler ≥ 10 × 2,0 × (2500 / 60) = 833 Liter/min Volumenverarbeitung
→ Mindest-Schalldämpfervolumen: ~8–10 Liter
```

**Akustische Zielwerte:**

| Boot-Typ | Zielwert am Auslass | Zielwert im Salon |
|----------|--------------------|--------------------|
| Segelyacht (Hilfsmotor) | <75 dB(A) | <65 dB(A) |
| Motorboot (Verdränger) | <80 dB(A) | <70 dB(A) |
| Motorboot (Gleiter) | <85 dB(A) | <75 dB(A) |
| Motoryacht (Komfort) | <70 dB(A) | <60 dB(A) |
| Superyacht | <65 dB(A) | <55 dB(A) |

### 6.4 Einbauregeln für Schalldämpfer

- Schalldämpfer so nah wie möglich am Motor installieren
  (je näher die Schallquelle, desto effektiver die Dämpfung)
- Schalldämpfer horizontal oder mit leichtem Gefälle zum Auslass montieren
- Niemals als tiefsten Punkt im System einbauen (Wasseransammlung)
- Ausreichend befestigen (Gewicht + Vibrationen)
- Mindestens 30 cm Schlauch zwischen Motor und Schalldämpfer (Entkopplung)
- Bei Twin-Installationen: separate Schalldämpfer pro Motor, keine
  gemeinsamen Dämpfer (Rückstrom-Risiko)

---
---

## 7. Auspuffschläuche und Leitungen

### 7.1 Anforderungen an Nassauspuff-Schläuche

Nassauspuff-Schläuche müssen extremen Bedingungen standhalten:

- **Temperatur**: Dauerhaft 70 °C, kurzzeitig bis 100 °C
  (bei Kühlwasser-Ausfall auch höher)
- **Chemische Belastung**: Salzwasser, Schwefelsäure-Kondensat, Abgase
- **Mechanische Belastung**: Eigengewicht (mit Wasser gefüllt), Vibrationen,
  Biegeradien
- **UV-Beständigkeit**: Auch im Motorraum relevant (Belüftungsöffnungen)
- **Biegeradius**: Muss Biegeradien von 2–4 × Durchmesser tolerieren
  ohne Knicken

### 7.2 Schlauchtypen und Materialien

#### 7.2.1 Nassauspuff-Schlauch (Standard)

- **Material**: EPDM-Gummi, drahtverformt oder gewebeverstärkt
- **Temperaturbereich**: −30 °C bis +100 °C (dauerhaft max. 70 °C)
- **Kennzeichnung**: SAE J2006 R2 (US) oder ISO 13363 (EU)
- **Farbe**: Schwarz (Standard), Blau (einige Hersteller für Nassauspuff)

**Führende Hersteller:**

| Hersteller | Serie | Temp.-Bereich | Durchmesser | Preis/m |
|------------|-------|---------------|-------------|---------|
| Shields Rubber | 250 Series | Bis 100 °C | 38–152 mm | 25–80 EUR |
| Trident Marine | 200 Series | Bis 100 °C | 38–152 mm | 20–70 EUR |
| Vetus | DHWS | Bis 100 °C | 40–152 mm | 30–90 EUR |
| Buck Algonquin | Standard | Bis 100 °C | 38–127 mm | 20–60 EUR |
| Novaflex | 5700 | Bis 120 °C | 50–200 mm | 35–100 EUR |

#### 7.2.2 Hochtemperatur-Nassauspuff-Schlauch

Für den Abschnitt direkt nach dem Mischkrümmer, wo Temperaturen
kurzzeitig >100 °C erreichen können:

- **Material**: Silikon-verstärkter EPDM oder Viton
- **Temperaturbereich**: Bis 150–200 °C
- **Einsatz**: Zwischen Mischkrümmer und erstem Waterlock
  (typisch 30–50 cm Länge)
- **Hersteller**: Trident 252 Series, Shields HT, Vetus DHTW

#### 7.2.3 Auspuffschlauch mit Drahtspirale

Für Abschnitte, die Stützung gegen Zusammendrücken benötigen:

- **Material**: EPDM mit eingebetteter Stahldrahtspirale
- **Einsatz**: Vertikale Abschnitte, enge Räume, lange horizontale
  Strecken
- **Vorteil**: Knickt nicht, behält Querschnitt auch bei Biegung
- **Nachteil**: Weniger flexibel, schwerer, teurer
- **Hersteller**: Shields 274 Series, Trident 200/XHD

### 7.3 Schlauchverbindungen und Schellen

**T-Bolt-Schellen (Empfohlen):**
- Edelstahl 316 Bügel mit T-Schrauben
- Gleichmäßige Druckverteilung über gesamten Umfang
- Drehmoment: 6–8 Nm (nicht überdrehen!)
- Hersteller: ABA, Breeze, Vetus, Awab
- Preis: 8–15 EUR pro Schelle

**Standard-Schneckengetriebe-Schellen (Nicht empfohlen):**
- Ungleichmäßige Druckverteilung
- Schraubenkopf kann den Schlauch einschneiden
- Einige Versicherungen akzeptieren sie im Abgassystem nicht mehr
- Nur als Notlösung verwenden

**Doppelschellen:**
- An jeder Verbindung werden zwei Schellen direkt nebeneinander
  montiert (Redundanz)
- ABYC-Standard: Doppelschellen an allen Nassauspuff-Verbindungen
  unter der Wasserlinie
- Empfehlung AYDI: Doppelschellen an ALLEN Nassauspuff-Verbindungen

### 7.4 Lebensdauer und Austauschintervalle

**Empfohlene Austauschintervalle:**

| Schlauchtyp | Austauschintervall | Anzeichen für Verschleiß |
|-------------|-------------------|--------------------------|
| Standard EPDM | 5–8 Jahre | Risse, Härte, Quellungen |
| Hochtemperatur | 4–6 Jahre | Verhärtung, Verfärbung |
| Drahtspirale | 7–10 Jahre | Rost an Spirale, Weichwerden |

**Inspektions-Checkliste Auspuffschläuche:**

1. **Äußere Oberfläche**: Risse, Blasen, Quellungen, Verfärbungen?
2. **Flexibilität**: Schlauch leicht zusammendrücken — hart = alt
3. **Innenseite**: Wenn zugänglich: glatt oder aufgeraut/erodiert?
4. **Schellen**: Fest? Rostig? Eingeschnitten?
5. **Anschlüsse**: Fester Sitz? Feuchtigkeit unter Schelle = Leck
6. **Biegungen**: Knickstellen? Zu enger Radius?
7. **Durchhängen**: Schlauch hängt durch = Wasseransammlung = Gegendruck
8. **Geruch**: Abgasgeruch im Motorraum = undichte Stelle

### 7.5 Schlauchverlegung

**Regeln für die korrekte Verlegung:**

- Mindest-Biegeradius: 2 × Schlauchdurchmesser (besser 4 ×)
- Keine S-Kurven oder Senken (Wasseransammlung)
- Kontinuierliches Gefälle zum Auslass (min. 10 mm/m)
- Ausreichende Stützung bei horizontalen Strecken (Schlauchhalter
  alle 50–80 cm)
- Mindestabstand zu heißen Oberflächen: 50 mm (auch mit Nassauspuff)
- Keine Metallschrauben oder scharfe Kanten in Kontakt mit Schlauch
- Genügend Spiel für Motorbewegungen auf Gummilagern (50–100 mm)

---
---

## 8. Anti-Siphon-Ventil

### 8.1 Das Siphon-Problem

Ein oft übersehenes, aber potenziell motorenzerstörendes Problem:
Der Siphon-Effekt im Kühlwassersystem.

**Wie der Siphon entsteht:**

Wenn der Kühlwasseranschluss am Mischkrümmer (wo das Wasser eingespritzt
wird) unter der Wasserlinie liegt, kann nach dem Abstellen des Motors
ein Siphon entstehen:

```
Meeresniveau ─────────────────────────────────
                                              │
                  Kühlwasserschlauch           │ Wasserdruck
                  ┌───────────────────┐        │
Seewasserventil ──┘                   └── Mischkrümmer → Motor
(unter WL)                                    (unter WL)
```

Der Wasserdruck auf dem Seewassereinlass treibt kontinuierlich Wasser
durch das System — auch wenn die Kühlwasserpumpe nicht läuft. Das Wasser
fließt durch den Mischkrümmer in den Auspuffschlauch, füllt den
Wassersammler, steigt zum Schwanenhals, und wenn es nicht rechtzeitig
über Bord abfließen kann, drückt es zurück in den Motor.

**Besonders gefährlich:**
- Bei Segelyachten mit tiefem Motor (Einlass UND Mischkrümmer unter WL)
- Bei motorlosen Überführungsfahrten (Motor aus, Seewasserventil offen)
- Bei Liegeplätzen mit Strömung/Wellen (Druckschwankungen)
- Über Nacht oder bei längerem Liegen

### 8.2 Funktionsprinzip des Anti-Siphon-Ventils

Das Anti-Siphon-Ventil (auch: Siphon-Brecher, Vacuum Breaker) ist ein
einfaches, aber lebensrettendes Bauteil. Es wird am höchsten Punkt der
Kühlwasserleitung zwischen Seewasserpumpe und Mischkrümmer installiert.

**Funktionsweise:**
- **Motor läuft**: Kühlwasserpumpe erzeugt Druck → Ventil schließt →
  normaler Kühlwasserfluss
- **Motor steht**: Kein Pumpendruck → Ventil öffnet → Luft strömt ein →
  Siphon wird gebrochen → Wasser fließt zurück zum Seewasserventil,
  nicht zum Motor

**Aufbau (typisch):**
```
Kühlwasserleitung ──┤ ├── Kühlwasserleitung (weiter zum Mischkrümmer)
                    │V│
                    │e│ ← Membrane oder Kugel
                    │n│
                    │t│
                    │i│ ← Entlüftungsöffnung (nach oben, Auffangbehälter)
                    │l│
                    └─┘
```

### 8.3 Einbauposition

- **Höhe**: Mindestens 300 mm über der maximalen Wasserlinie
  (einschließlich Krängung bei Segelbooten)
- **ABYC-Anforderung**: 350 mm über Wasserlinie
- **Position in der Leitung**: Zwischen Impeller-Pumpe und Mischkrümmer,
  am höchsten Punkt der Kühlwasserleitung
- **Entlüftung**: Das Ventil gibt beim Öffnen etwas Wasser ab. Ein
  Auffangschlauch zum Bilgenbereich oder ein kleiner Auffangbehälter
  ist empfohlen.

### 8.4 Hersteller und Modelle

| Hersteller | Modell | Anschluss | Preis | Besonderheit |
|------------|--------|-----------|-------|-------------|
| Vetus | NASBV 13–38 | 13–38 mm | 25–50 EUR | Membrane, wartungsarm |
| Volvo Penta | 3588236 | ¾"–1" | 40–70 EUR | OEM, Kugel-Typ |
| Yanmar | 128397-49530 | ¾" | 35–55 EUR | OEM |
| Jabsco | 29295 Serie | 13–38 mm | 20–40 EUR | Membrane, verbreitet |
| Groco | SVS Serie | ¾"–1½" | 60–100 EUR | Bronze, robust |

### 8.5 Wartung und häufige Probleme

**Wartungsintervall: Jährlich**

1. Ventil ausbauen (2 Schlauchschellen lösen)
2. Membrane/Kugel auf Verkalkung, Salzkristalle, Risse prüfen
3. Sitz reinigen (Essigwasser über Nacht einweichen bei Kalkbefall)
4. Entlüftungsöffnung auf Freiheit prüfen (Salzkristalle, Spinnennetze)
5. Membrane/Kugel bei Verschleiß ersetzen (Ersatzteilset ~10–20 EUR)
6. Funktion prüfen: Wasser durch Ventil gießen → muss stoppen und
   belüften, wenn kein Druck anliegt

**Häufige Probleme:**

- **Membrane verhärtet**: UV, Salz, Alter → öffnet nicht mehr →
  Siphon-Schutz verloren → Motor gefährdet
- **Membrane eingerissen**: → undicht bei laufendem Motor →
  Kühlwasser spritzt in Motorraum
- **Kalkverkrustung**: In Gebieten mit kalkhaltigem Wasser verkrustet
  der Ventilsitz → öffnet/schließt nicht sauber
- **Falsche Einbauhöhe**: Unter der Wasserlinie eingebaut = wirkungslos
- **Fehlende Entlüftung**: Auffangschlauch verstopft → Ventil kann
  nicht belüften → Siphon-Schutz verloren

### 8.6 Alternativen zum Anti-Siphon-Ventil

**Lösung 1 — Schwanenhals in der Kühlwasserleitung:**
Statt eines Ventils wird die Kühlwasserleitung selbst als Schwanenhals
über die Wasserlinie geführt. Einfach, aber platzintensiv und
Strömungswiderstand.

**Lösung 2 — Seewasserventil immer schließen:**
Disziplinierter Bootseigner schließt das Seewasserventil nach jedem
Motorbetrieb. In der Praxis wird dies oft vergessen. Keine zuverlässige
Lösung.

**Lösung 3 — Elektrisch gesteuertes Seewasserventil:**
Öffnet nur wenn der Motor läuft (über Öldruckschalter oder Zündung).
Teuer, aber zuverlässig. Einige Motoryachten ab Werk so ausgestattet.

**Empfehlung AYDI**: Anti-Siphon-Ventil ist Pflicht. Zusätzlich
Seewasserventil bei längerem Liegen schließen.

---
---

## 9. Schwanenhals (Swan Neck)

### 9.1 Funktion und Bedeutung

Der Schwanenhals ist ein invertiertes U-Rohr in der Auspuffleitung,
das den höchsten Punkt des Nassauspuff-Systems bildet. Er ist die
primäre physikalische Barriere gegen Wasserrückfluss in den Motor.

**Warum der Schwanenhals lebensrettend ist:**

Wenn Wellen den Auspuffauslass überfluten, Rückstau vom Wind entsteht
oder das Boot stark krängt, versucht Seewasser, durch den Auspuff in
den Motor zu gelangen. Der Schwanenhals zwingt dieses Wasser, zunächst
einen Hochpunkt zu überwinden — was unter normalen Umständen nicht möglich ist.

### 9.2 Mindesthöhe über Wasserlinie

Die Höhe des Schwanenhals-Scheitelpunkts über der Wasserlinie ist
der wichtigste Auslegungsparameter. Zu niedrig = kein Schutz.

**Berechnung der Mindesthöhe:**

```
h_min = h_WL + h_Welle + h_Krängung + h_Sicherheit

h_WL = 300 mm (Mindesthöhe über statischer Wasserlinie)
h_Welle = 0,7 × max. Wellenhöhe am Heck (Erfahrungswert)
h_Krängung = sin(Krängungswinkel) × horizontaler Abstand WL→Auslass
h_Sicherheit = 100 mm
```

**Praxis-Mindesthöhen:**

| Boot-Typ | Mindesthöhe über WL | Empfohlen |
|----------|--------------------|-----------| 
| Segelyacht <10 m | 350 mm | 500 mm |
| Segelyacht 10–15 m | 450 mm | 600 mm |
| Motorboot Verdränger | 300 mm | 450 mm |
| Motorboot Gleiter | 400 mm | 550 mm |
| Motoryacht >15 m | 350 mm | 500 mm |

**CE-Kategorie-Zuschläge:**
- Kategorie A (Ozean): +200 mm
- Kategorie B (Offshore): +100 mm
- Kategorie C (Küste): Standard
- Kategorie D (Geschützt): Standard

### 9.3 Konstruktionsformen

**Fester Schwanenhals (GFK oder Edelstahl):**
- Laminiertes GFK-Rohr, fix montiert
- Vorteil: Stabil, definierte Geometrie
- Nachteil: Nicht flexibel, aufwendige Installation

**Flexibler Schwanenhals (Auspuffschlauch):**
- Der Auspuffschlauch selbst wird in einem Bogen nach oben geführt
  und mit Halterungen fixiert
- Vorteil: Einfach, kostengünstig, flexibel
- Nachteil: Schlauch kann sich mit der Zeit setzen → Höhe nimmt ab

**Vetus-Schwanenhals-Fittings:**
- Spezielle Formstücke aus GFK oder Edelstahl
- Modelle: LTSV 40–100 mm
- Definierte Umlenkung mit integrierter Abtropfschale
- Preis: 60–200 EUR

### 9.4 Einbauregeln

1. **Scheitelpunkt**: Muss der höchste Punkt der gesamten Auspuffleitung sein
2. **Position**: So nah wie möglich am Auspuffauslass (kurzer Weg bergab)
3. **Gefälle nach dem Scheitelpunkt**: Min. 15 mm/m kontinuierlich zum Auslass
4. **Keine zweiten Tiefpunkte**: Zwischen Schwanenhals und Auslass darf
   keine Senke entstehen (Wasseransammlung)
5. **Steigung vor dem Scheitelpunkt**: Vom Wassersammler zum Schwanenhals
   max. 3 m Steiglänge, max. 45° Neigung
6. **Entwässerung**: Am Scheitel-Innenpunkt bildet sich Kondenswasser.
   Ein kleines Entwässerungsloch (3 mm) kann hier helfen.
7. **Halterung**: Stabile Befestigung am höchsten Punkt — der schwere,
   wassergefüllte Schlauch zieht nach unten.

### 9.5 Schwanenhals bei Segelschiffen: Krängungsberechnung

Bei einer Segelyacht, die 25° krängt, ändert sich die effektive Höhe des
Schwanenhalses über der Wasserlinie erheblich:

**Beispielrechnung:**
```
Boot: 12 m Segelyacht, Breite 3,8 m
Schwanenhals: 1,2 m achterlich der Mittschiffs, 0,3 m unter Deck
Deckshöhe über WL: 0,5 m
Schwanenhals-Scheitelpunkt: 0,5 + 0,3 m über WL = 0,8 m (aufrecht)

Bei 25° Krängung:
Seitliche Verschiebung des Auslass-Punktes unter WL:
Δh = sin(25°) × halbe Bootsbreite = 0,42 × 1,9 m = 0,80 m
→ Der Auspuffauslass liegt fast auf Wasserlinie!

Effektive Schwanenhals-Höhe (Leeseite):
h_eff = 0,8 m − 0,80 m = ~0 m → KRITISCH
```

**Lösung**: Schwanenhals-Höhe muss für den gekrängten Zustand ausgelegt sein.
Bei einer 12-m-Segelyacht: Scheitelpunkt mindestens 1,0 m über WL.

---
---

## 10. Auspuff-Auslass (Transom / Hull Fitting)

### 10.1 Auslass-Positionen

Es gibt drei grundsätzliche Positionen für den Auspuffauslass:

**Heck-Auslass (Transom Fitting):**
- Die häufigste Lösung bei Motorbooten und vielen Segelyachten
- Vorteil: Kurze Leitung, gutes Gefälle, einfache Installation
- Nachteil: Bei achterlichem Wellengang Überflutungsgefahr

**Seiten-Auslass (Hull Side Fitting):**
- Bei Segelyachten mit Langkiel oder Heckspiegel ohne Platz
- Vorteil: Weniger Überflutung von achtern
- Nachteil: Krängung bringt Leseiten-Auslass unter Wasser

**Unterwasser-Auslass (Below Waterline):**
- Selten bei Nassauspuff, häufiger bei Generatoren
- Vorteil: Unsichtbar, kein Spritzen auf Heck
- Nachteil: Permanenter Gegendruck durch Wassersäule, Rückflussgefahr

### 10.2 Transom-Fittings

| Hersteller | Modell | Material | Durchmesser | Preis |
|------------|--------|----------|-------------|-------|
| Vetus | TRC Serie | Edelstahl 316L | 40–100 mm | 35–120 EUR |
| Vetus | TRANSOM Serie | Edelstahl 316L mit Klappe | 40–100 mm | 50–150 EUR |
| Centek | Gooseneck | GFK | 50–100 mm | 60–130 EUR |
| Groco | HSC Serie | Bronze | 38–76 mm | 80–200 EUR |
| Yachticon | Standard | Edelstahl 316 | 38–90 mm | 30–90 EUR |

### 10.3 Design-Überlegungen

**Rückschlagklappe am Auslass:**
- Eine federbelastete Klappe verhindert Wassereindrung bei Liegeplatzbedingungen
- Muss leicht genug öffnen, um keinen nennenswerten Gegendruck zu erzeugen
- Korrodiert im Salzwasser → regelmäßig auf Gängigkeit prüfen
- Nicht als alleinigen Rückflussschutz verwenden (Schwanenhals + Anti-Siphon
  bleiben primäre Sicherungen)

**Spritzschutz:**
- Wasser, das am Auslass austritt, kann Flecken auf dem Rumpf/Heck verursachen
  (Ruß + Salzwasser = braune/schwarze Streifen)
- Lösung: Auslass-Fitting mit Ablaufrinne oder nach unten gerichtetem Winkel
- Manche Eigner installieren ein Ablauf-Blech unter dem Auslass

**Mindestdurchmesser Auslass:**
- Mindestens gleicher Durchmesser wie Auspuffschlauch
- Nie kleiner als Schlauch-ID (Engstelle = Gegendruck)
- Verjüngung am Auslass = häufigster Installationsfehler

### 10.4 Abgasgestank am Heck vermeiden

Ein klassisches Problem: Die Abgase sammeln sich im Cockpit oder auf
der Badeplattform. Ursachen und Lösungen:

- **Auslass zu hoch**: Abgase treffen Cockpit. → Auslass möglichst
  niedrig am Transom positionieren.
- **Auslass zu nah an Cockpit**: → Mindestens 300 mm unterhalb der
  Cockpitbodenöffnung.
- **Wind von achtern**: → Nicht vermeidbar, aber CO-Detektor im Cockpit
  empfohlen.
- **Abgasfahne am Rumpf**: → Auslass nach unten abgewinkelt, damit
  Abgas/Wasser direkt ins Wasser fällt.
- **Twin-Installationen**: Beide Auslässe auf gleicher Höhe, symmetrisch.

---
---

## 11. Hydrolock-Prävention

### 11.1 Was ist Hydrolock?

Hydrolock (Wasserschlag) tritt auf, wenn Wasser in einen oder mehrere
Zylinder des Motors gelangt und der Kolben beim Kompressionsvorgang
auf die inkompressible Flüssigkeit trifft. Da Wasser sich nicht
komprimieren lässt (im Gegensatz zu Luft/Abgas), treten extreme Kräfte
auf, die den Motor sofort und irreparabel zerstören:

**Typische Schäden durch Hydrolock:**
- Verbogene Pleuelstangen (häufigster Schaden)
- Gebrochene Kolben
- Gerissene Zylinderkopfdichtung
- Beschädigte Kurbelwelle (Lagerschäden)
- Risse im Motorblock
- Schaden am Anlasser (wenn Motor bei Hydrolock gestartet wird)

**Kosten eines Hydrolock-Schadens:**
- Mindestens: Zylinderkopfdichtung + Pleuel = 2.000–5.000 EUR
- Typisch: Motorrevision = 5.000–15.000 EUR
- Häufig: Motoraustausch = 8.000–30.000 EUR
- Die Versicherung zahlt nur, wenn die Abgasanlage nicht offensichtlich
  mangelhaft war (Wartungsnachweise!)

### 11.2 Ursachen für Wasser im Motor über die Abgasanlage

**Ursache 1 — Fehlender oder defekter Wassersammler:**
Ohne Wassersammler fließt nach dem Motorstopp das gesamte Wasser aus
der Auspuffleitung zurück zum Motor.

**Ursache 2 — Siphon-Effekt (fehlende Anti-Siphon):**
Seewasser wird kontinuierlich durch den Mischkrümmer in den Auspuff
gedrückt → Wassersammler läuft über → Wasser zum Motor.

**Ursache 3 — Schwanenhals zu niedrig:**
Wellenschlag am Heck drückt Wasser durch den Auslass → überwindet den
zu niedrigen Schwanenhals → Wasser zum Motor.

**Ursache 4 — Motor bei Rückenwind/Welle abstellen:**
Achterliche Welle drückt Wasser in den Auslass. Gleichzeitig steht
der Motor → kein Gegendruck durch Abgas → Wasser fließt ungehindert
zum Motor.

**Ursache 5 — Langer Anlassvorgang ohne Zündung:**
Beim Orgeln des Anlassers (Motor startet nicht) pumpt die Kühlwasserpumpe
Wasser durch den Mischkrümmer, aber es gibt keinen Abgasdruck, der es
durch das System drückt → Wasser sammelt sich im Krümmer → fließt in
den Auspuffkrümmer des Motors → in die Zylinder.

**Ursache 6 — Mischkrümmer-Durchrostung:**
Wasser tropft durch korrodierten Mischkrümmer direkt in den Auspuffkrümmer
des Motors → sammelt sich → bei nächstem Start → Hydrolock.

### 11.3 Präventionsmaßnahmen (Checkliste)

| Maßnahme | Priorität | Kosten | Wirksamkeit |
|----------|-----------|--------|-------------|
| Korrekt dimensionierter Wassersammler | KRITISCH | 100–400 EUR | Sehr hoch |
| Anti-Siphon-Ventil, korrekt installiert | KRITISCH | 25–100 EUR | Hoch |
| Schwanenhals auf korrekter Höhe | KRITISCH | 50–200 EUR | Sehr hoch |
| Mischkrümmer regelmäßig inspizieren | HOCH | 0 EUR (Eigenleistung) | Hoch |
| Seewasserventil bei Nicht-Betrieb schließen | HOCH | 0 EUR | Hoch |
| Auspuffschlauch-Zustand prüfen | HOCH | 0 EUR | Mittel |
| Rückschlagklappe am Auslass | MITTEL | 30–80 EUR | Mittel |
| Abgas-Temperaturüberwachung | MITTEL | 50–200 EUR | Mittel |
| CO-Detektor im Motorraum | HOCH | 30–80 EUR | CO-Schutz |

### 11.4 Notfallmaßnahme: Wasser im Motor entdeckt

Wenn der Verdacht besteht, dass Wasser in die Zylinder gelangt ist:

1. **NICHT den Anlasser betätigen!** Das verschlimmert den Schaden.
2. Glühkerzen oder Injektoren entfernen (alle Zylinder öffnen)
3. Motor von Hand durchdrehen (Kurbel oder Schwungrad)
   - Dreht leicht → wahrscheinlich kein Hydrolock-Schaden
   - Dreht nicht oder mit Widerstand → Wasser ist in Zylindern
4. Wenn Wasser gefunden: Motor mit offenen Zylindern durchdrehen
   (Anlasser kurz betätigen, Wasser wird herausgedrückt)
5. Ölstand prüfen: Milchiges Öl = Wasser im Ölkreislauf → Öl sofort wechseln
6. Zylinder mit etwas Motoröl benetzen (Rostschutz)
7. Motor erst starten, wenn alle Zylinder trocken und Ölwechsel erfolgt
8. Ursache der Wassereindrung BEHEBEN vor erneutem Motorbetrieb

### 11.5 Hydrolock-Statistiken und Versicherungsdaten

Hydrolock ist kein seltenes Ereignis. Versicherungsdaten und
Branchenerhebungen zeigen:

**Häufigkeit:**
- ~2–3 % aller versicherten Motorboote erleben innerhalb von 10 Jahren
  einen Hydrolock-Vorfall
- Bei Segelyachten mit Hilfsmotor: ~1,5 % in 10 Jahren
- In tropischen Gewässern mit starkem Tidenhub: bis zu 5 % in 10 Jahren
- Höchste Inzidenz: Boote >15 Jahre mit Original-Gusseisen-Mischkrümmer

**Schadensverteilung bei Hydrolock:**

| Schadensgrad | Anteil | Typische Kosten |
|-------------|--------|----------------|
| Leicht (nur Wasser, kein Start) | 25 % | 200–500 EUR |
| Mittel (Zylinderkopfdichtung) | 30 % | 1.500–3.000 EUR |
| Schwer (Pleuel, Kolben) | 30 % | 3.000–8.000 EUR |
| Totalschaden (Block gerissen) | 15 % | 8.000–30.000 EUR |

**Häufigste Ursachenverteilung:**

| Ursache | Anteil |
|---------|--------|
| Siphon-Rückfluss (fehlendes/defektes Anti-Siphon-Ventil) | 35 % |
| Mischkrümmer-Durchrostung | 25 % |
| Wellenschlag am Heck (Schwanenhals zu niedrig) | 20 % |
| Wassersammler-Überlauf (zu klein dimensioniert) | 10 % |
| Langer Anlassvorgang ohne Motorstart | 7 % |
| Sonstige (Auspuffschlauch-Versagen, Auslass-Überflutung) | 3 % |

### 11.6 Hydrolock-Erkennung bei der Kaufinspektion (Pre-Purchase Survey)

Bei einer Kaufinspektion sollte gezielt auf Hydrolock-Spuren geprüft werden:

**Indirekte Anzeichen eines früheren Hydrolock-Ereignisses:**

1. **Ölanalyse**: Erhöhter Wassergehalt im Motoröl (>0,1 %) deutet
   auf aktuelle oder frühere Wassereindrung hin
2. **Motoröl-Farbe**: Gräulich-milchiges Öl oder Emulsionsspuren am
   Öleinfülldeckel = Wasser war im System
3. **Kompressionstest**: Deutlich unterschiedliche Kompressionswerte
   zwischen den Zylindern können auf Pleuel-Verbiegung hindeuten
4. **Motor durchdrehen**: Von Hand — ungleichmäßiger Widerstand?
5. **Auspuffkrümmer inspizieren**: Weiße Salzablagerungen im
   Inneren des Motor-Auspuffkrümmers (nicht Mischkrümmer) deuten
   auf Wassereindrung in die Zylinder hin
6. **Injektorsitze**: Korrosionsspuren an den Injektorsitzen =
   Wasser war in den Zylindern

**AYDI-Flagging bei Kaufinspektion:**
Wenn die AYDI-Analyse bei einem Gebrauchtboot feststellt, dass
Anti-Siphon-Ventil fehlt UND Mischkrümmer >5 Jahre alt (Gusseisen) UND
Wassersammler unterdimensioniert: automatischer Warnhinweis
"Erhöhtes Hydrolock-Risiko — Motorölanalyse und Kompressionstest empfohlen."

### 11.7 Elektronische Hydrolock-Prävention

Moderne Ansätze zur automatisierten Hydrolock-Prävention:

**Wasserstandssensor im Auspuffkrümmer:**
- Ein Feuchtigkeitssensor im Motor-Auspuffkrümmer erkennt Wasser,
  bevor es die Zylinder erreicht
- Akustischer Alarm + Motorstopp-Relais
- Hersteller: Einige Spezialanbieter, noch kein Massenmarkt-Produkt
- Kosten: 150–300 EUR

**Abgastemperatur-basierte Erkennung:**
- Wenn die Abgastemperatur nach dem Mischkrümmer plötzlich unter
  die Kühlwassertemperatur fällt (statt darüber = normales Nassauspuff),
  deutet das auf massiven Wassereintritt hin
- Kann über NMEA2000-Netzwerk mit Motorsteuerung verbunden werden

**Kühlwasserdurchfluss-Überwachung:**
- Durchflusssensor in der Kühlwasserleitung
- Bei Null-Durchfluss bei laufendem Motor → Alarm → Motor stoppen
- Verhindert indirekt Hydrolock, weil Kühlwasserausfall erkannt wird
  (und damit auch defekte Impeller, die zu Überhitzung führen)
- Hersteller: Aqualarm, WaterWitch
- Kosten: 100–250 EUR

---
---

## 12. Systemauslegung und Dimensionierung

### 12.1 Gesamtsystem-Design

Die Auslegung einer Nassauspuffanlage erfordert die Abstimmung aller
Komponenten aufeinander. Ein falsch dimensioniertes Einzelteil kann
das gesamte System kompromittieren.

**Systemparameter und Abhängigkeiten:**

```
Motorleistung (PS/kW)
├── Bestimmt: Abgasmenge (m³/min)
├── Bestimmt: Kühlwassermenge (L/min)
├── Bestimmt: Mischkrümmer-Größe
├── Bestimmt: Schlauch-Innendurchmesser
├── Bestimmt: Wassersammler-Volumen
├── Bestimmt: Schalldämpfer-Volumen
└── Bestimmt: Auslass-Durchmesser

Installation (Bootslayout)
├── Bestimmt: Schlauchlänge → Gegendruck
├── Bestimmt: Höhendifferenz → Schwanenhals-Höhe
├── Bestimmt: Biegungen → Zusätzlicher Gegendruck
├── Bestimmt: Auslass-Position → Rückstau-Risiko
└── Bestimmt: Zugänglichkeit → Wartbarkeit
```

### 12.2 Gegendruck-Berechnung (vollständig)

Der Gesamtgegendruck des Abgassystems darf die Herstellerangabe nicht
überschreiten. Typisch: 40–50 mbar für die meisten Marine-Diesel.

**Gegendruckkomponenten:**

| Komponente | Typischer Druckverlust |
|------------|----------------------|
| Mischkrümmer | 3–8 mbar |
| Auspuffschlauch (pro Meter) | 0,5–2 mbar/m |
| 90°-Bogen | 3–5 mbar |
| 45°-Bogen | 1,5–3 mbar |
| Wassersammler/Waterlock | 3–8 mbar |
| Schalldämpfer (Lift Muffler) | 5–15 mbar |
| Schwanenhals | 2–5 mbar |
| Transom-Auslass | 1–3 mbar |
| Rückschlagklappe am Auslass | 2–5 mbar |

**Beispielrechnung für eine 40-PS-Segelyacht:**
```
Mischkrümmer:           5 mbar
Schlauch 2 m:           2 mbar
90°-Bogen (1×):         4 mbar
Wassersammler:          5 mbar
Schwanenhals:           3 mbar
Schlauch 1,5 m:         1,5 mbar
Auslass:                2 mbar
────────────────────────────────
Gesamt:                 22,5 mbar ← unter 50 mbar → OK
```

### 12.3 Kühlwasserbedarf

Die Menge an Kühlwasser, die durch den Mischkrümmer eingespritzt wird,
bestimmt die Kühlung der Abgase und damit die thermische Belastung
aller nachfolgenden Komponenten.

**Faustregel Kühlwasserbedarf:**
```
Q_kühlwasser (L/min) ≈ 0,05 × P_motor (PS) + 5
```

**Tabelle Kühlwasserbedarf:**

| Motorleistung | Kühlwasser min. | Empfohlen |
|--------------|----------------|-----------|
| 20 PS | 6 L/min | 8 L/min |
| 40 PS | 7 L/min | 10 L/min |
| 75 PS | 9 L/min | 12 L/min |
| 120 PS | 11 L/min | 15 L/min |
| 200 PS | 15 L/min | 20 L/min |
| 350 PS | 22 L/min | 30 L/min |

**Konsequenz bei zu wenig Kühlwasser:**
- Abgastemperatur nach Mischkrümmer steigt über 70 °C
- Auspuffschlauch wird thermisch überbelastet
- Schlauch erweicht, verformt sich, wird undicht
- Im Extremfall: Schlauch schmilzt oder entzündet sich

### 12.4 Twin-Engine-Installationen

Bei Zweimotor-Anlagen gelten besondere Regeln:

- **Getrennte Systeme**: Jeder Motor hat sein eigenes, vollständig
  getrenntes Abgassystem. Keine Querverbindungen.
- **Grund**: Wenn ein Motor läuft und der andere steht, würden Abgase
  durch die Querverbindung in den stehenden Motor gedrückt.
- **Separate Auslässe**: Idealerweise zwei getrennte Transom-Fittings.
  Mindestabstand 200 mm.
- **Symmetrie**: Beide Systeme möglichst symmetrisch ausgelegt
  (gleiche Längen, gleiche Höhen).
- **Generator**: Der Generator hat immer ein eigenes System, komplett
  getrennt von den Hauptmotoren.

### 12.5 Generator-Abgasanlage

Der Bordgenerator wird bei der Abgasanlagenplanung oft vergessen,
hat aber die gleichen Risiken wie der Hauptmotor:

- **Gleiche Komponenten**: Mischkrümmer, Schlauch, Wassersammler,
  Schwanenhals, Auslass — alles notwendig.
- **Besonderheit**: Generator läuft oft im Hafen (Landstrom-Alternative).
  CO-Emissionen in Hafennähe → Vergiftungsgefahr für Nachbarboote.
- **Besonderheit**: Generator läuft oft nachts (Klimaanlage).
  CO-Leck → schlafende Crew bemerkt nichts.
- **Dimensionierung**: Typisch 4–15 kW Generator = kleine Abgasanlage,
  aber gleiche Sorgfalt bei der Installation.
- **CO-Detektor**: Im Schlafbereich PFLICHT wenn Generator an Bord.

### 12.6 Motorspezifische Abgasanlagen-Konfigurationen

Die korrekte Konfiguration der Abgasanlage hängt stark vom Motortyp ab.
Die folgenden Konfigurationen sind werksseitig empfohlen:

#### 12.6.1 Volvo Penta D1-30 / D1-20

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | 22898216 (NiCu, ab 2015) |
| Schlauch-ID | 50 mm |
| Max. Gegendruck | 50 mbar |
| Kühlwasserbedarf | ~8 L/min |
| Waterlock empfohlen | Vetus NLPH50 oder Centek 1500 |
| Schwanenhals-Höhe min. | 400 mm über WL |
| Anti-Siphon | Volvo 3588236 oder Vetus NASBV19 |
| Besonderheit | Saildrive-Installation: Motor sehr tief → Schwanenhals besonders wichtig |

#### 12.6.2 Volvo Penta D2-40 / D2-55 / D2-75

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | 22840507 (Gusseisen) |
| Schlauch-ID | 60 mm (D2-40), 75 mm (D2-55/75) |
| Max. Gegendruck | 45 mbar (D2-55/75 Turbo) |
| Kühlwasserbedarf | ~10–15 L/min |
| Waterlock empfohlen | Vetus NLPH60–75 oder Centek 2000–3000 |
| Schwanenhals-Höhe min. | 450 mm über WL |
| Anti-Siphon | Volvo 3588236 oder Vetus NASBV25 |
| Besonderheit | D2-75 hat Turbolader → empfindlicher gegen Gegendruck |

#### 12.6.3 Yanmar 3YM20 / 3YM30

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | 128990-13520 (Gusseisen) |
| Schlauch-ID | 50–60 mm |
| Max. Gegendruck | 50 mbar |
| Kühlwasserbedarf | ~8–10 L/min |
| Waterlock empfohlen | Vetus NLPH50 oder Centek 1500 |
| Schwanenhals-Höhe min. | 400 mm über WL |
| Anti-Siphon | Yanmar 128397-49530 oder Vetus NASBV19 |
| Besonderheit | Kompakter Motorraum, Mischkrümmer oft schwer zugänglich |

#### 12.6.4 Yanmar 4JH5E / 4JH4-TE

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | 129671-13560 (4JH5E) / 129472-13560 (4JH4-TE) |
| Schlauch-ID | 60–75 mm |
| Max. Gegendruck | 45 mbar (Turbo-Versionen) |
| Kühlwasserbedarf | ~12–15 L/min |
| Waterlock empfohlen | Vetus NLPH75 oder Centek 3000 |
| Schwanenhals-Höhe min. | 450 mm über WL |
| Anti-Siphon | Yanmar OEM oder Vetus NASBV25 |
| Besonderheit | 4JH4-TE: Turbolader → Ölüberwachung, Gegendruck kritisch |

#### 12.6.5 Perkins M35 / M92B

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | 3586779 (M35) / 131616340 (M92B) |
| Schlauch-ID | 50 mm (M35), 75 mm (M92B) |
| Max. Gegendruck | 50 mbar (M35), 40 mbar (M92B Turbo) |
| Kühlwasserbedarf | ~8 L/min (M35), ~12 L/min (M92B) |
| Waterlock empfohlen | Vetus NLPH50 (M35), NLPH75 (M92B) |
| Besonderheit | Ältere Perkins-Motoren: Mischkrümmer oft werksspezifisch marinisiert |

#### 12.6.6 Nanni N4.38 / N4.50 / N4.80

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | Nanni OEM (Gusseisen), herstellerspezifisch |
| Schlauch-ID | 50–75 mm |
| Max. Gegendruck | 45–50 mbar |
| Kühlwasserbedarf | ~10–15 L/min |
| Besonderheit | Nanni marinisiert Kubota-Motoren; Aftermarket-Krümmer selten verfügbar. Bei Nanni immer OEM-Teil verwenden oder exakte Maße nehmen und Sonderanfertigung bestellen. |

#### 12.6.7 Beta Marine 25 / 43 / 60

| Parameter | Wert |
|-----------|------|
| Mischkrümmer | Beta OEM (Gusseisen), basierend auf Kubota |
| Schlauch-ID | 50–60 mm |
| Max. Gegendruck | 50 mbar |
| Kühlwasserbedarf | ~8–12 L/min |
| Besonderheit | Beta Marine verwendet Kubota-Blöcke mit eigener Marinisierung. Barr Marine bietet Aftermarket-Edelstahl für einige Modelle. Beta hat guten technischen Support. |

### 12.7 Typische Installationsfehler

Die folgenden Fehler werden bei Bootskäufen und Surveys am häufigsten
gefunden:

| Rang | Fehler | Häufigkeit | Gefährdung |
|------|--------|-----------|------------|
| 1 | Auspuffschlauch zu alt (>10 Jahre) | Sehr häufig | CO, Wassereinbruch |
| 2 | Anti-Siphon-Ventil fehlt oder defekt | Häufig | Hydrolock |
| 3 | Schwanenhals zu niedrig | Häufig | Hydrolock |
| 4 | Mischkrümmer nie inspiziert | Sehr häufig | Hydrolock, CO |
| 5 | Schlauchschellen minderwertig (Schneckengetriebe statt T-Bolt) | Häufig | Undichtigkeit |
| 6 | Auspuffschlauch hat Senke | Mäßig häufig | Gegendruck, Korrosion |
| 7 | Wassersammler zu klein | Mäßig häufig | Hydrolock |
| 8 | Kein CO-Detektor an Bord | Häufig | Lebensgefahr |
| 9 | Transom-Fitting aus Edelstahl 304 statt 316L | Mäßig häufig | Korrosion |
| 10 | Generator-Abgasanlage ignoriert | Häufig | CO, Hydrolock |

### 12.8 AYDI-Scoring-Kriterien für die Abgasanlage

Die AYDI-Analyse bewertet die Abgasanlage mit einem Punktesystem
von 0–100. Die Gewichtung der Einzelkomponenten:

| Komponente | Gewichtung | Begründung |
|------------|-----------|------------|
| Mischkrümmer (Zustand + Material + Alter) | 30 % | Höchstes Ausfallrisiko |
| Anti-Siphon + Wassersammler + Schwanenhals | 25 % | Hydrolock-Prävention |
| Auspuffschläuche + Schellen | 20 % | CO-Risiko, Dichtigkeit |
| CO-Sicherheitsmaßnahmen (Detektoren) | 10 % | Personensicherheit |
| Auslass + Dimensionierung + Gegendruck | 10 % | Motorseitiger Schutz |
| Dokumentation + Wartungsnachweise | 5 % | Wartungszustand |

**Scoring-Abzüge (Beispiele):**

| Befund | Abzug |
|--------|-------|
| Mischkrümmer Gusseisen >8 Jahre ohne Inspektion | −30 Punkte |
| Anti-Siphon-Ventil fehlt komplett | −25 Punkte |
| Kein CO-Detektor an Bord | −15 Punkte |
| Auspuffschlauch >8 Jahre | −15 Punkte |
| Schwanenhals <300 mm über WL | −20 Punkte |
| Wassersammler fehlt | −25 Punkte |
| Schellen nicht Edelstahl 316 | −5 Punkte |
| Keine Wartungsdokumentation | −5 Punkte |

---
---

## 13. Wartung und Inspektion

### 13.1 Wartungsplan Abgasanlage

#### Jährliche Wartung / Saisonstart

| Prüfpunkt | Aktion | Werkzeug |
|-----------|--------|----------|
| Mischkrümmer | Sichtprüfung außen: Rost, Risse, Verfärbungen | Taschenlampe |
| Kühlwasserfluss | Motor starten, Wasseraustritt am Auslass prüfen | Sicht |
| Abgastemperatur | IR-Thermometer am Mischkrümmer-Ausgang | IR-Thermometer |
| Auspuffschläuche | Sichtprüfung: Risse, Härte, Quellungen | Sicht, Hand |
| Schlauchschellen | Festigkeit, Rost, Sitz | Schraubendreher |
| Anti-Siphon-Ventil | Funktion prüfen, Membrane inspizieren | Schraubendreher |
| Wassersammler | Innenraum inspizieren, Ablagerungen entfernen | Taschenlampe |
| Schwanenhals | Höhe über WL prüfen, Halterung prüfen | Maßband |
| Auslass-Fitting | Klappe auf Gängigkeit prüfen, Zustand | Sicht, Hand |
| CO-Detektor | Funktion testen, Batterie prüfen | Testknopf |
| Abgas-Geruch | Motorraum bei laufendem Motor: Riecht es nach Abgas? | Nase |

#### Alle 500 Betriebsstunden / alle 3 Jahre

| Prüfpunkt | Aktion | Werkzeug |
|-----------|--------|----------|
| Mischkrümmer | Demontieren, Innenzustand prüfen, Wandstärke messen | Messschieber |
| Wasserkanäle | Durchspülen, auf Verstopfung prüfen | Wasserschlauch |
| Zink-Anoden | Im Kühlsystem erneuern | Schlüssel |
| Dichtungen | Alle Dichtungen am Mischkrümmer erneuern | Dichtsatz |
| Auspuffschläuche | Innenzustand prüfen (Erosion) | Taschenlampe |

#### Alle 2.000 Betriebsstunden / alle 8 Jahre

| Prüfpunkt | Aktion |
|-----------|--------|
| Auspuffschläuche | Komplett ersetzen |
| Schlauchschellen | Alle ersetzen (T-Bolt Edelstahl 316) |
| Wassersammler | Gründlich reinigen oder ersetzen |
| Anti-Siphon-Ventil | Komplett ersetzen |
| Mischkrümmer (Gusseisen) | Ersetzen (unabhängig vom Zustand) |

### 13.2 Winterlager-Maßnahmen

Die Abgasanlage muss für das Winterlager vorbereitet werden,
insbesondere bei Frostgefahr:

1. **Wassersammler entleeren**: Ablassventil öffnen, komplett leeren
2. **Auspuffschläuche entleeren**: Am tiefsten Punkt lösen, Wasser ablaufen
   lassen (wenn möglich)
3. **Frostschutzmittel**: Ungiftiges Propylenglykol (NICHT Ethylenglykol!)
   durch das Kühlsystem und damit auch durch den Mischkrümmer spülen
4. **Anti-Siphon-Ventil**: Offen lassen für Belüftung
5. **Auslass-Klappe**: Leicht geöffnet lassen für Belüftung
6. **Motor mit offenen Auspuffventilen**: Manche Mechaniker empfehlen,
   den Motor mit leicht geöffneten Dekompressionsventilen zu überwintern,
   damit eventuell kondensierendes Wasser in den Zylindern keinen
   Schaden anrichten kann

### 13.3 Inbetriebnahme nach Winterlager

1. Alle Schlauchverbindungen auf festen Sitz prüfen
2. Ablassventil am Wassersammler schließen
3. Anti-Siphon-Ventil auf Funktion prüfen
4. Seewasserventil öffnen
5. Motor starten — sofort prüfen:
   - Kommt Kühlwasser am Auslass?
   - Abgastemperatur normal (<70 °C nach Mischkrümmer)?
   - Abgasgeruch im Motorraum?
   - Undichte Stellen?
6. 15 Minuten Probelauf, dann nochmals alle Verbindungen prüfen

### 13.4 Dokumentation

Jede Wartung an der Abgasanlage sollte dokumentiert werden:

- Datum, Betriebsstunden
- Geprüfte Komponenten und Befund
- Ersetzene Teile mit Hersteller und Teilenummer
- Fotos des Mischkrümmer-Innenzustands (bei Demontage)
- Nächster empfohlener Wartungszeitpunkt
- Name des Durchführenden

**Warum wichtig:**
- Versicherungsfälle: Nachweis ordnungsgemäßer Wartung
- Bootskauf/-verkauf: Wartungshistorie der Abgasanlage ist wertrelevant
- AYDI-Analyse: Wartungsdokumentation fließt in Pipeline C (Text-Analyse) ein

### 13.5 Abgastemperatur-Überwachung

Die kontinuierliche Überwachung der Abgastemperatur ist eine der
effektivsten Frühwarnsysteme für Probleme in der Abgasanlage und
im Kühlsystem.

**Messpunkte und Normalwerte:**

| Messpunkt | Normalbereich | Warnung | Alarm |
|-----------|--------------|---------|-------|
| Abgaskrümmer (vor Mischkrümmer) | 350–550 °C | >600 °C | >650 °C |
| Nach Mischkrümmer (Nassauspuff) | 45–70 °C | >80 °C | >100 °C |
| Am Wassersammler-Eingang | 40–65 °C | >75 °C | >90 °C |
| Am Auspuffauslass | 35–55 °C | >65 °C | >80 °C |
| Trockenauspuff am Schalldämpfer | 250–450 °C | >500 °C | >550 °C |
| Trockenauspuff Isolierung außen | 30–55 °C | >60 °C | >70 °C |

**Überwachungssysteme:**

| System | Hersteller | Sensoren | Display | Preis |
|--------|------------|----------|---------|-------|
| EGT-Anzeige analog | VDO, Faria | 1× Typ-K Thermoelement | Rundanzeige | 80–150 EUR |
| EGT-Anzeige digital | ScanGauge, Maretron | 1–4× Typ-K | LCD/OLED | 150–400 EUR |
| NMEA2000 EGT-Sensor | Maretron, Actisense | 1× pro Kanal | MFD-Display | 200–350 EUR |
| CAN-Bus Integration | Volvo Penta EVC | OEM-Sensoren | Volvo-Display | Ab Werk |
| Alarm-only | Diverse | Bimetall oder PTC | Akustisch/LED | 30–80 EUR |

**Empfehlung AYDI:**
- Minimum: Infrarot-Thermometer bei jeder Inspektion anwenden
- Empfohlen: Fest installierter EGT-Sensor nach dem Mischkrümmer
  mit Alarm bei >80 °C
- Optimal: NMEA2000-Integration mit Logging und Trend-Analyse

### 13.6 Impeller-Verschleiß und Auswirkung auf die Abgasanlage

Der Impeller der Seewasser-Kühlpumpe hat direkte Auswirkung auf die
Abgasanlage, da er das Kühlwasser fördert, das im Mischkrümmer
eingespritzt wird. Ein verschlissener Impeller = weniger Kühlwasser =
heißere Abgase = thermische Überlastung der Abgasanlage.

**Impeller-Verschleiß-Stufen und Auswirkungen:**

| Verschleißgrad | Fördermenge (% Soll) | Abgastemp. nach Mischkrümmer | Auswirkung |
|---------------|---------------------|------------------------------|------------|
| Neu | 100 % | 45–55 °C | Optimal |
| Leicht verschlissen | 80–90 % | 55–65 °C | Akzeptabel |
| Mäßig verschlissen | 60–80 % | 65–80 °C | Grenzwertig |
| Stark verschlissen | 40–60 % | 80–100 °C | KRITISCH — Schlauch gefährdet |
| Defekt (Flügel abgerissen) | <40 % | >100 °C | NOTFALL — Motor sofort stoppen |

**Impeller-Wechselintervalle:**

| Einsatz | Intervall |
|---------|----------|
| Segelyacht (<300 h/Jahr) | Jährlich zum Saisonstart |
| Motorboot (300–600 h/Jahr) | Alle 400 Betriebsstunden |
| Charter/Vielfahrer (>600 h/Jahr) | Alle 300 Betriebsstunden |
| Immer: | Ersatz-Impeller + Dichtung an Bord mitführen! |

**Impeller-Hersteller und Qualität:**

| Hersteller | Qualität | Besonderheiten | Preis (typisch) |
|------------|---------|----------------|----------------|
| Jabsco/Xylem | OEM-Qualität | Originalausstatter vieler Motorenhersteller | 25–60 EUR |
| Johnson (SPX Flow) | OEM-Qualität | Alternative OEM-Pumpen | 25–55 EUR |
| Oberdorfer | Gut | US-Hersteller, robust | 20–45 EUR |
| Jabsco Profile H | Premium | Hart-Neopren, längere Lebensdauer | 35–70 EUR |
| Aftermarket Asien | Variabel | Günstig, aber Qualität schwankt | 10–25 EUR |

### 13.7 Korrosionsschutz im Kühlwassersystem

Die Korrosion des Mischkrümmers und anderer Abgaskomponenten wird
maßgeblich durch den Zustand des Kühlwassersystems beeinflusst.

**Zink-Anoden im Kühlsystem:**
Viele Motoren haben Opfer-Zinkanoden im Seewasserkreislauf (am
Wärmetauscher, manchmal am Motorblock). Diese Anoden schützen den
Mischkrümmer vor galvanischer Korrosion.

- **Wechselintervall**: Jährlich oder wenn >50 % aufgelöst
- **Achtung**: Fehlende oder aufgebrauchte Zinkanoden beschleunigen
  die Mischkrümmer-Korrosion erheblich
- **Typische Zink-Anode am Wärmetauscher**: Bleistiftform, Ø 10–14 mm,
  Länge 40–60 mm, Preis 5–15 EUR

**Interne Reinigung des Kühlwasserkreislaufs:**
Alle 2–3 Jahre empfohlen, um Kalk-, Salz- und Korrosionsablagerungen zu
entfernen, die den Kühlwasserdurchfluss im Mischkrümmer reduzieren.

- Spüllösung: Biologisch abbaubarer Marine-Entkalker
  (z. B. Barnacle Buster, Rydlyme Marine)
- Alternativ: 10 % Essig-Wasser-Lösung, 2–4 Stunden zirkulieren
- NICHT: Salzsäure oder aggressive Industrieentkalker (greifen
  Gummiteile und Dichtungen an)
- Ablauf: Seewassereinlass in Eimer mit Spüllösung umlenken,
  Motor 30 min bei Leerlauf laufen lassen, dann mit Frischwasser spülen

### 13.8 Ersatzteil-Bevorratung an Bord

Für Fahrtenyachten und Langfahrer empfohlene Abgas-Ersatzteile an Bord:

| Teil | Priorität | Gewicht/Größe | Preis |
|------|----------|--------------|-------|
| Impeller + Dichtung | PFLICHT | Minimal | 30–60 EUR |
| Auspuffschlauch (1 m, passend) | HOCH | ~1–2 kg | 30–80 EUR |
| T-Bolt-Schellen (4 Stück, passend) | HOCH | Minimal | 40–60 EUR |
| Anti-Siphon-Ventil-Membrane | HOCH | Minimal | 10–20 EUR |
| Hochtemperatur-Dichtmasse (Permatex) | MITTEL | 1 Tube | 12 EUR |
| Dichtung Mischkrümmer-Flansch | MITTEL | Minimal | 15–40 EUR |
| Mischkrümmer (komplett) | LANGFAHRT | 3–8 kg | 300–1.200 EUR |
| Schlauchschellen Sortiment | MITTEL | Minimal | 30 EUR |

**Hinweis für Langfahrer:**
Ab dem Mittelmeer ostwärts, in der Karibik und in Südostasien sind
Ersatzteile für Mischkrümmer oft nicht oder nur mit wochenlanger
Lieferzeit erhältlich. Auf Langfahrt einen Ersatz-Mischkrümmer
mitführen ist eine kluge Investition.

---
---

## 14. Fehlerbild-Atlas

### Fehlerbild 14.1 — Mischkrümmer-Durchrostung (von innen)

**Beschreibung:**
Der Gusseisen-Mischkrümmer korrodiert von der Innenseite durch die
permanente Einwirkung von Salzwasser und Schwefelsäure-Kondensat. Die
Korrosion ist von außen nicht sichtbar, bis der Durchbruch erfolgt.

**Symptome:**
- Zunächst keine äußeren Anzeichen
- Später: Rostspuren an der Außenseite, besonders an Schweißnähten
- Kühlwasser tropft am Mischkrümmer (Durchrostung Wasserkanal → Abgaskanal)
- Weiße Dampfwolken am Auslass (mehr als normal)
- Im Extremfall: Wasser fließt durch Krümmer direkt in Auspuffkrümmer/Zylinder

**Ursachen:**
- Normaler Alterungsprozess bei Gusseisen (4–8 Jahre Nutzung)
- Beschleunigt durch: Salzwasser, wenig Betrieb (Nass-Trocken-Zyklen),
  fehlende Zink-Anoden im Kühlsystem, schwefelhaltiger Kraftstoff
- Unzureichender Kühlwasserdurchfluss (Impeller verschlissen)

**Schweregrad:** KRITISCH

**Reparatur:**
- Sofortiger Austausch des Mischkrümmers (keine Reparatur möglich)
- Material-Upgrade empfohlen: Edelstahl 316L oder NiCu statt Gusseisen
- Kühlwassersystem prüfen (Impeller, Thermostat, Wärmetauscher)
- Kosten: 300–2.500 EUR (Material) + 200–400 EUR (Einbau)

**AYDI-Bewertung:**
- Konfidenz: `visual_medium` (Innenzustand nicht visuell beurteilbar)
- Empfehlung: Bei Gusseisen-Krümmer >5 Jahre: "Endoskopie oder Demontage empfohlen"

---

### Fehlerbild 14.2 — Auspuffschlauch-Versagen

**Beschreibung:**
Der Nassauspuff-Schlauch altert durch Temperatur, Chemikalien und
UV-Einstrahlung. Das Gummi/EPDM wird spröde, rissig oder quillt auf.
Im schlimmsten Fall reißt der Schlauch und Abgase (inkl. CO) treten
in den Motorraum aus.

**Symptome:**
- Abgasgeruch im Motorraum
- Sichtbare Risse, Blasen oder Quellungen am Schlauch
- Schlauch ist hart und unflexibel (drücken → kein Nachgeben)
- Wasser-/Abgasaustritt an Schellen oder Rissstellen
- Schwarze Rußspuren an umliegenden Bauteilen

**Ursachen:**
- Alterung (>5–8 Jahre)
- Thermische Überlastung (Kühlwasserausfall → heißes Abgas → Schlauch schmilzt)
- Chemische Degradation (Kraftstoff, Öl auf dem Schlauch)
- UV-Einwirkung (auch im Motorraum über Lüftungsöffnungen)
- Minderwertiges Schlauchmaterial (nicht SAE J2006 R2 zertifiziert)

**Schweregrad:** HOCH (CO-Gefahr, Wassereinbruch)

**Reparatur:**
- Schlauch komplett ersetzen (Reparatur nicht empfohlen)
- Immer mit neuen T-Bolt-Schellen (Edelstahl 316)
- Ursache der Überhitzung beheben (falls thermisch bedingt)
- Kosten: 80–300 EUR (Schlauch) + 50–150 EUR (Schellen) + 100–300 EUR (Einbau)

---

### Fehlerbild 14.3 — Wassersammler-Überlauf

**Beschreibung:**
Der Wassersammler/Waterlock ist zu klein dimensioniert oder das System
fördert mehr Wasser zurück, als der Sammler aufnehmen kann. Wasser
fließt vom Wassersammler zurück zum Motor.

**Symptome:**
- Wasser im Auspuffkrümmer des Motors (bei Inspektion nach Motorstopp)
- Milchiges Motoröl (Wasser im Ölkreislauf)
- Schwerer Motorstart nach längerer Standzeit
- Wassersammler ist nach Motorstopp randvoll (Inspektion)

**Ursachen:**
- Wassersammler-Volumen zu klein für die Anlage
- Fehlender Anti-Siphon-Ventil → Siphon-Effekt füllt Sammler
- Auspuffleitung zwischen Motor und Sammler zu lang (zu viel Wasservolumen)
- Schwanenhals-Höhe zu niedrig → Rückstau bei Wellen
- Defekte Rückschlagklappe am Auslass

**Schweregrad:** KRITISCH (Hydrolock-Gefahr)

**Reparatur:**
- Wassersammler durch größeres Modell ersetzen
- Anti-Siphon-Ventil installieren oder reparieren
- Schwanenhals-Höhe erhöhen
- System-Gesamtkonzept überprüfen
- Kosten: 100–400 EUR (Wassersammler) + Systemanpassung

---

### Fehlerbild 14.4 — Siphon-Rückfluss

**Beschreibung:**
Durch den Siphon-Effekt fließt nach Motorstillstand kontinuierlich
Seewasser durch das Kühlsystem und den Mischkrümmer in die Abgasanlage,
überläuft den Wassersammler und gelangt in den Motor.

**Symptome:**
- Wasserstand im Wassersammler steigt nach Motorstopp
  (beobachten über 10–30 Minuten)
- Motor orgelnd, aber nicht startend nach längerem Liegen
- Wasser am Auspuffauslass, obwohl Motor nicht läuft
- Milchiges Öl

**Ursachen:**
- Fehlendes Anti-Siphon-Ventil
- Defektes Anti-Siphon-Ventil (Membrane verhärtet, verkrustet)
- Anti-Siphon-Ventil unter Wasserlinie montiert
- Seewasserventil nicht geschlossen bei Nicht-Betrieb

**Schweregrad:** KRITISCH (Hydrolock-Gefahr)

**Reparatur:**
- Anti-Siphon-Ventil einbauen oder ersetzen
- Korrekte Einbauhöhe sicherstellen (>300 mm über WL)
- Membrane/Kugel erneuern
- Kosten: 25–100 EUR + Einbau

---

### Fehlerbild 14.5 — Kohlenstoff-Ablagerung (Verrußung)

**Beschreibung:**
Im Auspuffsystem lagern sich Rußpartikel, Verbrennungsrückstände und
Ölreste ab. Dies verengt den Querschnitt, erhöht den Gegendruck und
kann die Motorleistung erheblich reduzieren.

**Symptome:**
- Leistungsverlust des Motors (besonders unter Last)
- Schwarzer Auspuff (mehr Ruß als normal)
- Erhöhte Abgastemperatur (Gegendruck → schlechtere Verbrennung)
- Motor läuft unrund bei höherer Drehzahl
- Bei Inspektion: Schwarze, teerartige Ablagerungen in Schlauch und Sammler

**Ursachen:**
- Motor wird dauerhaft unter Last betrieben (<40 % Nenndrehzahl)
  → "Wet Stacking" / Verglasung
- Injektoren verschlissen (schlechte Zerstäubung → Rußbildung)
- Luftfilter verstopft (zu fettes Gemisch)
- Turbolader defekt (reduzierte Ladeluft)
- Schlechter Kraftstoff (hoher Schwefelgehalt)

**Schweregrad:** MITTEL–HOCH

**Reparatur:**
- Abgassystem reinigen (Schläuche, Wassersammler, Schalldämpfer)
- Motor regelmäßig unter Volllast fahren (15–20 Minuten)
  → "Italian Tune-up"
- Injektoren prüfen/warten
- Luftfilter tauschen
- Kosten: Reinigung 200–500 EUR, Injektoren 400–1.200 EUR

---

### Fehlerbild 14.6 — Abgasleck mit CO-Gefahr

**Beschreibung:**
Kohlenmonoxid (CO) tritt an einer undichten Stelle im Abgassystem aus
und kann in bewohnbare Räume gelangen. CO ist geruch-, farb- und
geschmacklos und kann tödlich sein.

**Symptome:**
- CO-Detektor schlägt Alarm
- Kopfschmerzen, Übelkeit, Schwindel bei Crew (SOFORT Motorraum lüften!)
- Abgasgeruch im Motorraum (andere Abgasbestandteile riechen)
- Rußspuren an Schlauchverbindungen, Schellen, Mischkrümmer
- Verfärbungen an umliegenden Bauteilen

**Ursachen:**
- Gerissener oder gealterte Auspuffschlauch
- Lose Schlauchschellen
- Defekte Dichtung am Mischkrümmer
- Riss im Mischkrümmer
- Undichter Wassersammler
- Lose Flanschverbindung Motor → Auspuffkrümmer

**Schweregrad:** LEBENSBEDROHLICH

**Sofortmaßnahmen:**
1. Motor abstellen
2. Alle Räume lüften (Luken, Fenster öffnen)
3. Betroffene Personen an frische Luft
4. Bei Symptomen: Rettungsdienst/Seenotrettung alarmieren
5. Motor NICHT starten bis Leck gefunden und behoben

**Reparatur:**
- Undichte Stelle finden und beheben
- Gesamtes System prüfen (wo ein Leck ist, sind oft weitere)
- CO-Detektor in allen bewohnten Räumen nachrüsten
- Kosten: abhängig von Ursache, 50–2.500 EUR

---

### Fehlerbild 14.7 — Turbo-Öl im Abgas

**Beschreibung:**
Bei verschlissenem Turbolader gelangt Schmieröl aus den Turbolager-
Dichtungen in den Abgasstrom. Das Öl verschmutzt das gesamte Auspuffsystem
und kann den Auspuffschlauch chemisch angreifen.

**Symptome:**
- Blauer/grauer Rauch am Auspuff (besonders bei Last)
- Öliger Film im Wassersammler und an den Auspuffschläuchen
- Ölflecken auf dem Wasser hinter dem Auspuffauslass
- Erhöhter Ölverbrauch des Motors
- Nachlaufen/Überdrehen des Motors nach Abstellen
  (Öl im Ansaugtrakt verbrennt = Diesel Runaway)

**Ursachen:**
- Turbolager verschlissen (Spiel zu groß → Öl tritt an Dichtungen aus)
- Ölablaufleitung vom Turbo verstopft (Staudruck → Öl drückt durch Dichtungen)
- Zu hoher Kurbelgehäusedruck (verstopfte Kurbelgehäuseentlüftung)

**Schweregrad:** HOCH

**Reparatur:**
- Turbolader überholen oder ersetzen
- Ölablaufleitung reinigen
- Kurbelgehäuseentlüftung prüfen
- Auspuffsystem reinigen (Öl-Ruß-Schlämme entfernen)
- Kosten: Turbo-Überholung 800–2.500 EUR, Turbo neu 1.500–5.000 EUR

---

### Fehlerbild 14.8 — Wet Stacking (Nassverbrennung)

**Beschreibung:**
Wenn ein Dieselmotor dauerhaft unter zu geringer Last betrieben wird
(typisch <40 % Nenndrehzahl), verbrennt der Kraftstoff nicht vollständig.
Unverbrannter Diesel und Ruß kondensieren im Auspuffsystem und bilden
teerartige Ablagerungen. Im Extremfall tropft flüssiger Kraftstoff aus
dem Auspuff.

**Symptome:**
- Schwarzer, teerhaltiger Tropf am Auspuffauslass
- Intensiver Dieselgeruch aus dem Auspuff
- Motor raucht schwarz, besonders bei Gasstößen
- Leistungsverlust
- Auspuffschläuche innen beschichtet mit klebriger, schwarzer Masse

**Ursachen:**
- Dauerhafter Betrieb unter 40 % Last (typisch: Segelyacht-Motoren)
- Überdimensionierter Motor für das Einsatzprofil
- Generator unter Mindestlast betrieben (ohne Lastbank)

**Schweregrad:** MITTEL

**Reparatur:**
- Motor unter Last fahren: 1 Stunde bei 75–85 % Nenndrehzahl verbrennt
  Ablagerungen ("Italian Tune-up")
- Bei extremem Wet Stacking: Abgassystem reinigen
- Langfristig: Motor bei Fahrt regelmäßig belasten
- Generator: Lastbank installieren oder Mindestlast sicherstellen
- Kosten: 0 EUR (Betriebsweise anpassen) bis 500 EUR (Systemreinigung)

---

### Fehlerbild 14.9 — Transom-Fitting-Korrosion

**Beschreibung:**
Der Auspuffauslass am Heck (Transom Fitting) korrodiert durch die
permanente Einwirkung von Salzwasser, Abgaskondensaten und
galvanische Ströme.

**Symptome:**
- Rostspuren rund um den Auslass (am Heck/Transom)
- Rückschlagklappe klemmt (öffnet oder schließt nicht)
- Schlauchverbindung am Auslass locker oder undicht
- Verfärbung des Rumpfes um den Auslass (Ruß + Korrosion)
- Bei fortgeschrittener Korrosion: Wassereindrung durch den Auslass

**Ursachen:**
- Minderwertiges Material (Edelstahl 304 statt 316, verzinkter Stahl)
- Galvanische Korrosion (falsches Metall in Kontakt mit Rumpfbeschlag)
- Fehlende Isolierung zwischen Auslass und Rumpf (bei Stahlbooten)
- Kein regelmäßiges Spülen mit Süßwasser nach Salzwasserbetrieb

**Schweregrad:** MITTEL–HOCH

**Reparatur:**
- Transom-Fitting ersetzen (Edelstahl 316L oder Bronze)
- Korrekte Dichtung mit Sikaflex 291/291i
- Isolierung gegen galvanische Korrosion (Kunststoff-Unterlegscheiben)
- Kosten: 50–200 EUR (Fitting) + 100–300 EUR (Einbau/Abdichtung)

---

### Fehlerbild 14.10 — Schalldämpfer-Zersetzung

**Beschreibung:**
Der Schalldämpfer/Lift Muffler zersetzt sich durch chemische und
thermische Belastung. Kunststoff-Schalldämpfer können reißen,
GFK-Schalldämpfer delaminieren.

**Symptome:**
- Erhöhter Geräuschpegel des Auspuffs (plötzlich lauter)
- Wasseraustritt am Schalldämpfer (Riss)
- Abgasgeruch trotz intakter Schläuche
- Bei Inspektion: Risse, Verformungen, Ablösungen im Schalldämpfer

**Ursachen:**
- Thermische Überlastung (Kühlwasserausfall → heißes Abgas zerstört Kunststoff)
- UV-Degradation (Kunststoff-Schalldämpfer im Lichteinfall)
- Chemische Zersetzung (Schwefelsäure-Kondensat)
- Alter (>10–15 Jahre)
- Mechanische Beschädigung (Schlag, Vibration, Befestigung gerissen)

**Schweregrad:** MITTEL

**Reparatur:**
- Schalldämpfer ersetzen (keine Reparatur möglich)
- Ursache der Überhitzung beheben
- Kosten: 80–400 EUR + Einbau

---

### Fehlerbild 14.11 — Anti-Siphon-Ventil klemmt

**Beschreibung:**
Das Anti-Siphon-Ventil öffnet oder schließt nicht korrekt. Entweder
fehlt der Siphon-Schutz (Ventil öffnet nicht) oder es leckt bei
laufendem Motor (Ventil schließt nicht).

**Symptome (Ventil schließt nicht):**
- Kühlwasser spritzt aus dem Ventil bei laufendem Motor
- Wasserflecken unter/neben dem Ventil
- Motorraum feucht

**Symptome (Ventil öffnet nicht):**
- Nicht direkt sichtbar — stille Gefahr!
- Wasserstand im Wassersammler steigt nach Motorstopp
  (nur durch Beobachtung erkennbar)
- Im schlimmsten Fall: Hydrolock nach Liegezeit

**Ursachen:**
- Membrane verhärtet/verkalkt (Salz, Alter)
- Kugel im Sitz festgeklebt (Kalk, Salz, Biomasse)
- Entlüftungsöffnung verstopft (Salzkristalle, Schmutz, Insekten)
- Falsches Ventil (für Süßwasser statt Seewasser)

**Schweregrad:** HOCH (Motor-Zerstörungspotenzial)

**Reparatur:**
- Ventil reinigen (Essigwasser, Entkalkung)
- Membrane ersetzen (Ersatzteilset 10–20 EUR)
- Bei wiederkehrendem Problem: Ventil komplett ersetzen (25–100 EUR)
- Einbauhöhe kontrollieren (>300 mm über WL)

---

### Fehlerbild 14.12 — Wasser in den Zylindern (Hydrolock-Folge)

**Beschreibung:**
Wasser ist durch die Abgasanlage in die Zylinder des Motors gelangt.
Im schlimmsten Fall wurde der Anlasser betätigt und Hydrolock hat
mechanische Schäden verursacht.

**Symptome:**
- Motor dreht nicht oder nur schwer (Anlasser summt, Motor rührt sich nicht)
- Motor startet nicht (Kompression fehlt)
- Wasser tritt an Glühkerzen/Injektoren aus (wenn entfernt)
- Milchiges Motoröl (Wasser-Emulsion)
- Bei schwerem Hydrolock: Metallgeräusche, verbogene Teile sichtbar

**Ursachen:**
- Alle Ursachen aus Fehlerbild 14.3, 14.4 (Wassersammler-Überlauf,
  Siphon-Rückfluss)
- Mischkrümmer-Durchrostung (14.1)
- Wellenschlag am Heck bei niedrigem Schwanenhals
- Langer Anlassvorgang ohne Motorstart (Kühlwasser ohne Abgasgegendruck)

**Schweregrad:** KRITISCH (Motorenzerstörung)

**Erstmaßnahmen:**
1. NICHT weiter anlassen!
2. Glühkerzen/Injektoren entfernen
3. Von Hand durchdrehen (frei oder blockiert?)
4. Wasser aus Zylindern entfernen
5. Motoröl sofort wechseln (wenn milchig)
6. Zylinder mit Öl benetzen (Korrosionsschutz)
7. Fachwerkstatt für Schadensbeurteilung

**Kosten:**
- Glück gehabt (nur Wasser, kein Start): 200–500 EUR (Öl, Dichtungen)
- Zylinderkopfdichtung beschädigt: 1.500–3.000 EUR
- Pleuel verbogen: 3.000–8.000 EUR (Motorrevision)
- Totalschaden: 8.000–30.000 EUR (Motortausch)

---
---

## 15. Troubleshooting

### 15.1 Überhitzte Abgase (Temperatur >80 °C nach Mischkrümmer)

**Mögliche Ursachen und Prüfschritte:**

| Schritt | Prüfung | Ergebnis → Maßnahme |
|---------|---------|---------------------|
| 1 | Kühlwasseraustritt am Auspuffauslass prüfen | Kein/wenig Wasser → Weiter Schritt 2 |
| 2 | Impeller der Seewasserpumpe prüfen | Beschädigt/verschlissen → Impeller tauschen |
| 3 | Seewasserfilter prüfen | Verstopft → Reinigen |
| 4 | Seewasserventil prüfen | Geschlossen/klemmt → Öffnen/warten |
| 5 | Thermostat prüfen (bei Zweikreis) | Klemmt geschlossen → Thermostat tauschen |
| 6 | Wasserkanal im Mischkrümmer prüfen | Verstopft (Kalk, Salz, Korrosion) → Reinigen oder Krümmer tauschen |
| 7 | Kühlwasserschläuche auf Knick prüfen | Geknickt → Korrigieren |
| 8 | Abgas-Gegendruck messen | >50 mbar → System auf Verstopfung prüfen |

### 15.2 Wasseraustritt am Mischkrümmer

**Mögliche Ursachen und Prüfschritte:**

| Schritt | Prüfung | Ergebnis → Maßnahme |
|---------|---------|---------------------|
| 1 | Außenseite trocknen und beobachten: Wo tritt Wasser aus? | Flansch → Schritt 2, Gehäuse → Schritt 3, Schlauch → Schritt 4 |
| 2 | Flansch-Dichtung prüfen | Leck am Flansch → Schrauben nachziehen oder Dichtung ersetzen |
| 3 | Gehäuse auf Durchrostung prüfen | Durchrostung → Mischkrümmer sofort ersetzen |
| 4 | Schlauchschelle prüfen | Lose → Nachziehen/ersetzen |
| 5 | Kühlwasseranschluss prüfen | O-Ring defekt → O-Ring ersetzen |

### 15.3 Abgasgeruch im Innenraum

**ACHTUNG: Potenziell lebensbedrohlich! Sofort handeln.**

| Schritt | Prüfung | Ergebnis → Maßnahme |
|---------|---------|---------------------|
| 1 | CO-Detektor prüfen (falls vorhanden) | Alarm → Motor aus, Lüften, Personen an frische Luft |
| 2 | Motorraum öffnen und riechen (bei laufendem Motor) | Abgasgeruch im Motorraum → Weiter Schritt 3 |
| 3 | Alle Schlauchverbindungen visuell prüfen | Lose/rissig/feucht → Schlauch/Schelle ersetzen |
| 4 | Mischkrümmer-Flansch prüfen | Rußspuren am Flansch → Dichtung ersetzen, Schrauben prüfen |
| 5 | Abgasschlauch auf Risse prüfen (Taschenlampe + Rauchtest) | Riss → Schlauch ersetzen |
| 6 | Abgasgeruch vom Auslass, nicht vom Motorraum? | Ja → Rückstrom über Cockpit-Öffnungen. Ventilation prüfen |

### 15.4 Motor raucht schwarz

**Mögliche Ursachen im Abgassystem:**

| Schritt | Prüfung | Ergebnis → Maßnahme |
|---------|---------|---------------------|
| 1 | Abgas-Gegendruck messen | Zu hoch → Abgassystem auf Verstopfung prüfen |
| 2 | Wassersammler inspizieren | Voller Ruß → Reinigen |
| 3 | Schalldämpfer inspizieren | Verstopft → Reinigen oder ersetzen |
| 4 | Auspuffschlauch inspizieren | Innen verengt durch Ablagerungen → Ersetzen |
| 5 | Motor unter Last fahren (15 min bei 75 % Drehzahl) | Besserung → Wet Stacking war Ursache |

### 15.5 Ungewöhnliche Geräusche aus dem Auspuff

| Geräusch | Mögliche Ursache | Maßnahme |
|----------|-----------------|----------|
| Gurgeln/Blubbern (normal bei Nassauspuff) | Normaler Wassertransport | Keine Maßnahme, wenn gleichmäßig |
| Klopfen/Hämmern | Wasser schlägt gegen Schlauch/Sammler | Befestigung prüfen, Gegendruck prüfen |
| Zischen | Abgasleck (heißes Gas tritt aus) | Sofort prüfen, CO-Gefahr |
| Pfeifen | Verengung im System | Schlauchquerschnitte prüfen |
| Lautes Brummen (neu) | Schalldämpfer defekt | Schalldämpfer inspizieren/ersetzen |
| Metallisches Klappern | Rückschlagklappe lose | Auslass-Fitting prüfen |
| Stoßweises Spucken | Ungleichmäßiger Kühlwasserfluss | Impeller prüfen |

---
---

## 16. FAQ

### 16.1 Grundlagen

**F: Wie oft muss ein Mischkrümmer getauscht werden?**
A: Gusseisen: alle 5–8 Jahre oder 1.500–3.000 Betriebsstunden, je nachdem
was zuerst erreicht wird. Edelstahl 316L: alle 10–15 Jahre. NiCu-Legierung:
alle 12–20 Jahre. Entscheidend ist die regelmäßige Inspektion — ein gut
gepflegter Gusseisen-Krümmer kann 10 Jahre halten, ein vernachlässigter
Edelstahl-Krümmer 5 Jahre versagen.

**F: Kann man einen Gusseisen-Mischkrümmer durch einen Edelstahl-Krümmer ersetzen?**
A: Ja, sofern die Anschlussmaße identisch sind. Aftermarket-Hersteller wie
Osco, Barr Marine und Centek bieten 316L-Ersatzkrümmer für die meisten
gängigen Motortypen an. Die Investition ist höher (500–1.200 vs. 200–400 EUR),
aber die Lebensdauer verdoppelt bis verdreifacht sich.

**F: Was passiert, wenn ich mit defektem Mischkrümmer weiterfahre?**
A: Im besten Fall: Motor überhitzt, weil Kühlwasser im Krümmer austritt
statt ihn zu kühlen. Im schlimmsten Fall: Wasser fließt durch den defekten
Krümmer in die Zylinder und verursacht Hydrolock. Beides ist teuer.
Weiterfahren ist NICHT empfehlenswert.

**F: Ist ein Nassauspuff oder ein Trockenauspuff besser?**
A: Kommt auf das Boot an. Für Sportboote <20 m ist der Nassauspuff Standard,
weil er einfacher, leiser und platzsparender ist. Der Trockenauspuff ist
besser für Boote >20 m, Arbeitsboote und Stahlboote, weil er langlebiger ist
und kein Hydrolock-Risiko birgt. Die Wahl hängt von Boot, Budget und
Nutzungsprofil ab.

### 16.2 Installation

**F: Wie hoch muss der Schwanenhals über der Wasserlinie sein?**
A: Mindestens 300 mm über der statischen Wasserlinie. Bei Segelyachten muss
die Krängung einberechnet werden — bei 25° Krängung kann die effektive Höhe
um bis zu 800 mm sinken. Empfohlene Mindesthöhen: Segelyacht 500–600 mm,
Motorboot 400–550 mm über Wasserlinie (statisch, aufrecht).

**F: Brauche ich ein Anti-Siphon-Ventil?**
A: Ja, wenn der Kühlwassereinlass am Mischkrümmer unter oder nahe der
Wasserlinie liegt — und das ist bei >90 % aller Boote der Fall. Das Ventil
kostet 25–100 EUR und kann einen Motorschaden im fünfstelligen Bereich
verhindern. Es gibt keinen vernünftigen Grund, darauf zu verzichten.

**F: Können zwei Motoren ein gemeinsames Abgassystem nutzen?**
A: Nein, auf keinen Fall. Wenn ein Motor läuft und der andere steht, würden
Abgase durch die Querverbindung in den stehenden Motor gedrückt — und mit
ihnen Wasser. Jeder Motor braucht sein eigenes, vollständig getrenntes
Abgassystem. Dasselbe gilt für den Generator.

**F: Welcher Auspuffschlauch-Durchmesser für meinen Motor?**
A: Faustregel: Motorhersteller-Angabe verwenden. Wenn nicht verfügbar:
40 PS = 50–60 mm, 75 PS = 60–75 mm, 120 PS = 75–90 mm, 200 PS = 90–100 mm,
350 PS = 100–120 mm. Nie kleiner als der Anschluss am Mischkrümmer.

**F: Darf der Auspuffschlauch eine Senke haben?**
A: Nein. Jede Senke ist ein Wasseransammlungspunkt, der Gegendruck erzeugt,
Korrosion fördert und bei Frost platzen kann. Die Leitung muss ein
kontinuierliches Gefälle zum Auslass haben (mindestens 10 mm/m).

### 16.3 Wartung

**F: Wie erkenne ich, ob mein Mischkrümmer noch in Ordnung ist?**
A: Äußere Anzeichen: Rost, Verfärbungen, Wasseraustritt, weiße Salzkristalle.
Aber: Die gefährliche Korrosion findet INNEN statt. Der einzige sichere Weg
ist die Demontage und Innenkontrolle alle 3 Jahre (Gusseisen) oder 5 Jahre
(Edelstahl). Endoskopie durch den Schlauch ist eine Alternative.

**F: Wie oft müssen Auspuffschläuche ersetzt werden?**
A: Standard-EPDM-Schläuche: alle 5–8 Jahre. Hochtemperaturschläuche:
alle 4–6 Jahre. Drahtspiral-Schläuche: alle 7–10 Jahre. Unabhängig vom
Alter ersetzen, wenn: Risse, Verhärtung, Quellungen oder Verfärbungen
sichtbar sind.

**F: Mein Anti-Siphon-Ventil spritzt bei laufendem Motor. Normal?**
A: Ein leichtes Tropfen ist normal — das Ventil lässt konstruktionsbedingt
etwas Wasser durch, wenn es schließt. Spritzen unter Druck deutet auf eine
defekte Membrane hin. Ersetzen (10–20 EUR für Membrane, 25–100 EUR für
das gesamte Ventil).

**F: Was ist die richtige Vorgehensweise bei der Winterlagerung?**
A: Wassersammler entleeren. Frostschutzmittel (Propylenglykol, ungiftig)
durch das Kühlsystem spülen. Anti-Siphon-Ventil offen lassen. Bei extremem
Frost: Auspuffschlauch am tiefsten Punkt lösen und Wasser ablaufen lassen.

**F: Warum tropft schwarze Flüssigkeit aus meinem Auspuff?**
A: Wet Stacking — der Motor wird dauerhaft unter zu geringer Last betrieben.
Unverbrannter Diesel und Ruß kondensieren im Auspuffsystem. Lösung: Motor
regelmäßig 15–30 Minuten bei 75–85 % Last fahren. Wenn das nicht hilft:
Injektoren und Luftfilter prüfen.

### 16.4 Sicherheit

**F: Wie gefährlich ist CO aus der Abgasanlage wirklich?**
A: Sehr. CO-Konzentrationen ab 100 ppm verursachen Kopfschmerzen und Übelkeit.
Ab 400 ppm innerhalb von 1–2 Stunden Bewusstlosigkeit. Ab 1.600 ppm innerhalb
von 20 Minuten Tod. Ein defekter Mischkrümmer oder gerissener Auspuffschlauch
kann im geschlossenen Motorraum Konzentrationen >1.000 ppm erzeugen, die dann
durch Kabinenlüftung in bewohnte Räume gelangen. CO-Detektoren in allen
Schlaf- und Aufenthaltsräumen sind PFLICHT.

**F: Können Abgase in den Cockpit gelangen?**
A: Ja, besonders bei achterlichem Wind. Der Auspuffauslass am Heck bläst
die Abgase nach oben, wo sie vom Wind in den Cockpit getrieben werden.
Bei Generatorbetrieb im Hafen ein besonders hohes Risiko. CO-Detektoren
im Cockpit werden von der ABYC und vielen Versicherungen empfohlen.

**F: Ist der Geruch am Auspuff gefährlich?**
A: Der typische Dieselabgas-Geruch (Stickoxide, unverbrannte Kohlenwasserstoffe)
ist unangenehm, aber das eigentlich gefährliche CO ist geruchlos. Man kann
CO-vergiftet werden, ohne den Auspuff zu riechen. Deshalb sind CO-Detektoren
wichtig — die Nase allein schützt nicht.

**F: Was tun, wenn der CO-Detektor im Hafen alarmiert?**
A: 1. Motor und Generator sofort abstellen. 2. Alle Räume lüften (Luken,
Fenster). 3. Boot verlassen, an frische Luft. 4. Nachbarboote informieren
(deren Generator kann die Ursache sein). 5. Abgasanlage vor nächstem
Motorbetrieb vollständig inspizieren.

### 16.5 Spezialfragen

**F: Kann ich den Auspuffauslass unter die Wasserlinie legen?**
A: Prinzipiell ja, wird bei einigen Generatoren und sehr leisen Installationen
gemacht. Aber: Der permanente Gegendruck durch die Wassersäule belastet den
Motor und erhöht den Kraftstoffverbrauch. Außerdem muss das System absolut
dicht sein, da bei Motorstillstand Wasser durch den Auslass einströmt. Nur
mit spezieller Ventiltechnik und professioneller Installation.

**F: Warum hat mein Boot zwei Auspuffauslässe auf einer Seite?**
A: Wahrscheinlich: Hauptmotor + Generator. Oder bei älteren Installationen:
Nassauspuff + Dry-Stack für Notfälle. Jedes System muss separat gewartet werden.

**F: Ist ein Edelstahl-Mischkrümmer immer besser als Gusseisen?**
A: Nicht immer. Edelstahl 316L hat eine Schwäche: Chlorid-induzierte
Spannungsrisskorrosion bei Temperaturen >60 °C. Am Mischkrümmer können
lokale Temperaturen diese Grenze überschreiten, besonders bei Kühlwasserausfall.
NiCu-Legierungen sind in dieser Hinsicht überlegen. Für die meisten
Anwendungen ist 316L dennoch die beste Wahl — die Lebensdauer ist deutlich
länger als bei Gusseisen.

**F: Was kostet eine komplette Nassauspuff-Anlage?**
A: Für einen typischen 40-PS-Segelyacht-Diesel (Volvo Penta, Yanmar):
Mischkrümmer (Edelstahl): 500–800 EUR, Auspuffschlauch (3 m): 120–250 EUR,
Wassersammler/Lift Muffler: 100–200 EUR, Anti-Siphon-Ventil: 30–50 EUR,
Schellen und Kleinteile: 50–100 EUR, Transom-Auslass: 40–100 EUR.
Gesamt: 840–1.500 EUR Material. Einbau durch Werft: zusätzlich 500–1.500 EUR.

**F: Wie prüfe ich den Abgas-Gegendruck?**
A: Mit einem U-Rohr-Manometer (einfach, 20 EUR) oder einem digitalen
Differenzdruckmesser (100–200 EUR). Messport: Am Mischkrümmer-Ausgang oder
am Schlauchanschluss des Mischkrümmers. Motor auf Nenndrehzahl bringen.
Wert ablesen. Maximal: 40 mbar (Turbo) bzw. 50 mbar (Sauger). Werte >30 mbar
deuten auf Teilverstopfung hin.

**F: Kann ein Rußpartikelfilter (DPF) in der Marine nachgerüstet werden?**
A: In der Theorie ja, in der Praxis sehr aufwendig und teuer. DPF-Systeme
benötigen regelmäßige Regeneration (hohe Abgastemperatur >600 °C), die
im Nassauspuff nicht erreichbar ist. Einige Superyachten >24 m haben
Trockenauspuff-Systeme mit DPF, aber für die Sportschifffahrt ist das
aktuell nicht praktikabel.

**F: Mein Gusseisen-Krümmer ist erst 2 Jahre alt und schon rostig. Normal?**
A: Oberflächenrost an Gusseisen ist normal und unvermeidlich. Entscheidend
ist der Innenzustand. Äußerer Rost allein ist kein Grund zum Tausch.
Aber: Wenn Rostflecken an Stellen auftreten, die mit dem Kühlwasserkanal
korrespondieren, deutet das auf Durchrostung von innen hin → Demontage
und Inspektion.

**F: Warum empfiehlt mein Motorhersteller Gusseisen, wenn Edelstahl besser ist?**
A: Kosten und Haftung. Gusseisen-Krümmer kosten den Hersteller in der
Produktion ein Drittel des Edelstahl-Preises. Außerdem garantiert der
Hersteller nur seine eigenen Teile — Edelstahl-Aftermarket-Krümmer werden
nicht unterstützt. Die OEM-Empfehlung ist wirtschaftlich motiviert, nicht
technisch optimal.

**F: Taugt eine Keramikbeschichtung im Mischkrümmer etwas?**
A: Keramikbeschichtungen (z. B. Cerakote C-Series) können die Lebensdauer
von Gusseisen-Krümmern verlängern, indem sie die Innenfläche vor Korrosion
schützen. Aber: Die Beschichtung muss den thermischen Zyklen standhalten
und kann abplatzen. Die Beschichtung kostet 150–300 EUR und verlängert die
Lebensdauer um geschätzte 20–40 %. Ob das wirtschaftlich ist, hängt vom
Einzelfall ab. Im Vergleich zu einem Edelstahl-Krümmer ist es keine bessere
Lösung.

**F: Wie finde ich heraus, welchen Mischkrümmer mein Motor braucht?**
A: 1. Motortyp und Seriennummer identifizieren (Typenschild am Motor).
2. Herstellerkatalog konsultieren (Volvo Penta: VODIA, Yanmar: YETS).
3. Aftermarket-Hersteller-Website: Motor eingeben → passende Teile werden
angezeigt (z. B. osco.com, barrmarine.com). 4. Im Zweifelsfall: Alten
Krümmer demontieren und Anschlussmaße messen (Flanschdurchmesser,
Schraubenabstand, Wasseranschluss-Größe).

**F: Mein Boot hat keinen Wassersammler — ist das ein Problem?**
A: Ja, definitiv. Ohne Wassersammler fließt nach dem Motorstopp das gesamte
Wasser aus der Auspuffleitung zurück zum Motor. Je nach Installation und
Schwanenhals-Höhe kann das ausreichen, um die Zylinder zu füllen. Einen
Wassersammler nachzurüsten kostet 100–400 EUR und ist eine der wichtigsten
Sicherheitsinvestitionen an der Abgasanlage.

**F: Welches Frostschutzmittel für die Abgasanlage?**
A: Propylenglykol (PG), ungiftig, lebensmittelecht. NICHT Ethylenglykol
(EG, Autofrostschutz), das giftig ist und die Umwelt belastet. Konzentration:
-30 °C Schutz = ca. 50 % PG-Wasser-Gemisch. Nach der Winterpause das
System gründlich mit Frischwasser spülen, bevor der Motor normal betrieben wird.

**F: Können Abgase den GFK-Rumpf beschädigen?**
A: Ja, wenn heiße Abgase direkt auf GFK treffen. GFK beginnt ab ~120 °C zu
erweichen. Im Nassauspuff liegt die Temperatur bei ~50–70 °C, das ist unkritisch.
Aber: Bei Kühlwasserausfall steigen die Temperaturen auf 400–600 °C — dann ist
der GFK-Rumpf in unmittelbarer Gefahr. Genügend Abstand und Hitzeschilde sind
Pflicht.

**F: Mein Auspuff-Auslass liegt nur 100 mm über der Wasserlinie. Reicht das?**
A: Grenzwertig. Bei jeder Welle, jedem Manöver, jeder Gewichtsverlagerung
kann der Auslass unter Wasser kommen. Empfohlen: Mindestens 200 mm statisch,
besser 300 mm. Wenn baulich nicht änderbar: Rückschlagklappe am Auslass UND
korrekt dimensionierter Schwanenhals sind Pflicht. CO-Detektor im Cockpit
ebenfalls.

**F: Sind flexible oder starre Schwanenhalse besser?**
A: Beide haben Vor- und Nachteile. Starre Schwanenhalse (GFK, Edelstahl)
haben eine definierte, unveränderliche Höhe — der Scheitelpunkt bleibt
immer dort, wo er sein soll. Flexible Schwanenhalse (Schlauch in Bogenform)
können sich mit der Zeit setzen und an Höhe verlieren. Empfehlung: Starre
Schwanenhalse für Boote, die viel segeln (Kräfte auf dem Schlauch). Flexible
Schwanenhalse für einfache Installationen, aber mit stabiler Halterung.

### 16.6 Motorspezifische Fragen

**F: Mein Volvo Penta 2003 hat den originalen Mischkrümmer von 1990. Ist das gefährlich?**
A: Ja, extrem. Ein 35 Jahre alter Gusseisen-Mischkrümmer ist weit über seine
Lebensdauer hinaus. Auch wenn er äußerlich "noch OK" aussieht, ist die
interne Korrosion mit an Sicherheit grenzender Wahrscheinlichkeit weit
fortgeschritten. Sofortiger Austausch empfohlen, idealerweise gegen einen
Edelstahl-316L-Krümmer (z. B. Osco VV-80918, ~500 EUR). Die Kosten stehen
in keinem Verhältnis zum Risiko eines Hydrolock-Schadens (5.000–15.000 EUR).

**F: Mein Yanmar 3YM20 verbraucht plötzlich mehr Kühlwasser. Hängt das mit der Abgasanlage zusammen?**
A: Ja, möglicherweise. Wenn der Mischkrümmer intern korrodiert ist, kann
Kühlwasser auf der Abgasseite austreten, statt korrekt in den Abgasstrom
eingespritzt zu werden. Das ist ein Frühwarnzeichen für Mischkrümmer-Versagen.
Weitere Möglichkeit: Defekte Zink-Anode im Wärmetauscher → beschleunigte
Korrosion. Sofortige Inspektion von Mischkrümmer und Kühlsystem empfohlen.

**F: Passen Volvo Penta D2-40 und D2-55 Mischkrümmer untereinander?**
A: Ja, die D2-40, D2-55 und D2-75 teilen sich den gleichen Mischkrümmer
(Volvo PN 22840507). Die Motoren basieren auf dem gleichen Block, nur
Einspritzung und Turbolader unterscheiden sich. Das gilt auch für
Aftermarket-Krümmer von Osco, Barr Marine und Centek.

**F: Mein Perkins 4.108 hat Ölflecken am Mischkrümmer. Was bedeutet das?**
A: Der Perkins 4.108 ist berühmt-berüchtigt für undichte Auspuff-
Krümmerdichtungen. Ölflecken am Mischkrümmer deuten auf eine undichte
Krümmerdichtung zwischen Motorblock und Auspuffkrümmer hin — das Öl kommt
nicht vom Kühlsystem, sondern vom Motor selbst. Dichtungssatz tauschen
(30–50 EUR), Schrauben auf Drehmoment prüfen. Wenn die Dichtung
wiederholt undicht wird: Planheit der Flanschflächen prüfen (verzogen?).

**F: Sind die neuen Volvo Penta D1/D2-Krümmer (NiCu) wirklich besser?**
A: Ja, deutlich. Volvo hat ab ca. 2015 bei der D1/D2-Serie auf
Nickel-Kupfer-Gusseisen umgestellt. Diese Krümmer sind erheblich
korrosionsbeständiger als die alten Gusseisen-Krümmer. Lebensdauer:
12–20 Jahre statt 5–8 Jahre. Der Mehrpreis (ca. 200–400 EUR) gegenüber
Aftermarket-Gusseisen amortisiert sich durch die längere Lebensdauer.

**F: Mein Generator-Auspuff stinkt, obwohl der Motor OK ist. Warum?**
A: Häufigste Ursache: Wet Stacking am Generator. Generatoren laufen oft
unter Mindestlast (nur Kühlschrank und ein paar Lichter), was zu
unvollständiger Verbrennung führt. Lösung: Klimaanlage, Warmwasserboiler
oder elektrische Heizkassette während des Generatorbetriebs einschalten,
um die Last zu erhöhen. Mindestens 30–40 % der Nennleistung anstreben.

### 16.7 Kosten und Wirtschaftlichkeit

**F: Lohnt sich ein jährlicher Abgas-Check?**
A: Absolut. Ein jährlicher Check dauert 30–60 Minuten (Eigenleistung)
oder kostet 100–200 EUR (Werft). Er kann Mischkrümmer-Durchrostung
(Schaden: 5.000–30.000 EUR), CO-Vergiftung (unbezahlbar) und
Auspuffschlauch-Versagen (Schaden: 500–5.000 EUR) verhindern. Das
Kosten-Nutzen-Verhältnis ist extrem.

**F: Was kostet eine komplette Abgasanlagen-Überholung?**
A: Für eine typische Segelyacht mit 40-PS-Diesel:
- Mischkrümmer Edelstahl 316L: 500–800 EUR
- Auspuffschlauch komplett (3 m): 120–250 EUR
- Wassersammler neu: 100–200 EUR
- Anti-Siphon-Ventil neu: 30–50 EUR
- Schellen, Dichtungen, Kleinteile: 80–150 EUR
- Transom-Fitting: 40–100 EUR
- Arbeitszeit Werft: 600–1.200 EUR
- **Gesamt: 1.470–2.750 EUR**

Für eine Motoryacht mit 2× 300 PS: Verdoppeln bis Verdreifachen der
Materialkosten, Arbeitszeit 1.000–2.500 EUR. Gesamt: 4.000–8.000 EUR.

**F: Mein Surveyor sagt, die Abgasanlage ist "acceptable". Reicht das?**
A: "Acceptable" beim Surveyor bedeutet: "Funktioniert aktuell, keine
unmittelbare Gefahr." Es bedeutet NICHT: "Braucht keine Aufmerksamkeit."
Wenn der Surveyor Einschränkungen notiert hat (z. B. "elbow showing age",
"hoses hardening"), sollten Sie diese Punkte vor der nächsten Saison
adressieren. Ein Surveyor inspiziert die Abgasanlage oft nur oberflächlich
— eine dedizierte Abgas-Inspektion durch einen Motor-Fachmann ist
gründlicher.

**F: Übernimmt die Kaskoversicherung Schäden durch defekte Abgasanlage?**
A: Das hängt von der Police und der Schadensursache ab. Grundsätzlich:
- **Plötzliches, unvorhergesehenes Ereignis** (z. B. Hydrolock durch
  Welleneinschlag trotz korrekt gewarteter Anlage): In der Regel gedeckt.
- **Verschleiß** (z. B. Mischkrümmer-Korrosion nach 10 Jahren ohne Inspektion):
  In der Regel NICHT gedeckt.
- **Folgeschaden** (z. B. Motor durch Hydrolock zerstört wegen defektem
  Mischkrümmer): Gedeckt, wenn der Versicherungsnehmer seiner
  Wartungspflicht nachgekommen ist. Wartungsnachweise AUFBEWAHREN.
- **CO-Vergiftung**: Personenschäden sind über die Haftpflicht gedeckt.

### 16.8 Umwelt und Emissionen

**F: Gelten Emissionsvorschriften für meine Yacht?**
A: Für den Motor selbst: Ja, ab Werk muss er der jeweiligen Emissionsstufe
entsprechen (EU Stage IIIA/V, EPA Tier 3). Für die Abgasanlage: Es gibt
keine spezifischen Nachrüst-Emissionsvorschriften für Sportboote <24 m.
Aber: In einigen Binnengewässern und Naturschutzgebieten gelten lokale
Emissionsbeschränkungen (z. B. Bodensee, Schweizer Seen).

**F: Kann ich die Abgase ins Wasser leiten statt in die Luft?**
A: Beim Nassauspuff werden die Abgase über den Auspuffauslass
zusammen mit dem Kühlwasser über Bord geleitet — also teilweise ins
Wasser. Das ist Standard und akzeptiert. Ein Unterwasser-Auslass, bei dem
die Abgase direkt unter der Wasserlinie ausgestoßen werden, ist bei
Generatoren möglich, erfordert aber spezielle Ventiltechnik und ist
technisch anspruchsvoller.

**F: Schadet das Kühlwasser-Abgas-Gemisch dem Meer?**
A: Der Umwelteinfluss ist gering. Das Kühlwasser ist Seewasser, das
lediglich erwärmt wurde. Die Abgase enthalten CO₂, NOx und kleine Mengen
Ruß — ähnlich dem Abgas an Land. Bei gut gewarteten Motoren mit
vollständiger Verbrennung ist die Umweltbelastung minimal. Problematisch
wird es nur bei Wet Stacking (unverbrannter Diesel ins Wasser) oder
Ölverlust durch defekten Turbolader.

---
---

## 17. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Abgasgegendruck** | Druckwiderstand, den das Abgassystem dem Abgasstrom des Motors entgegensetzt. Gemessen in mbar oder mm Wassersäule. Zu hoher Gegendruck = Leistungsverlust, Überhitzung. |
| **Abgaskrümmer (Motor)** | Das am Zylinderkopf montierte Gussteil, das die Abgase aller Zylinder sammelt. NICHT zu verwechseln mit dem Mischkrümmer. |
| **Abgastemperatur (EGT)** | Exhaust Gas Temperature. Am Zylinderkopf: 400–650 °C. Nach Mischkrümmer (Nassauspuff): 50–70 °C. Messbar mit Pyrometer oder IR-Thermometer. |
| **Anti-Siphon-Ventil** | Ventil, das den Siphon-Effekt in der Kühlwasserleitung unterbricht und verhindert, dass Seewasser durch den Mischkrümmer in den Motor fließt. Auch: Vacuum Breaker, Siphon-Brecher. |
| **ABYC P-1** | US-Standard des American Boat and Yacht Council für Abgassysteme. Strenger als ISO-Normen in einigen Punkten. |
| **CE-Kategorie** | Designkategorie nach EU Recreational Craft Directive: A (Ozean), B (Offshore), C (Küste), D (Geschützt). Bestimmt Anforderungen an Schwanenhals-Höhe u.a. |
| **Centek** | US-Hersteller von Abgaskomponenten (Vernalift-Schalldämpfer, Mischkrümmer). |
| **CO (Kohlenmonoxid)** | Farb-, geruch- und geschmackloses Gas. Entsteht bei unvollständiger Verbrennung. Ab 100 ppm gesundheitsschädlich, ab 1.600 ppm tödlich. |
| **CO-Detektor** | Elektronischer Warnmelder für Kohlenmonoxid. Nach EN 50291-2 zertifizierte Geräte für den maritimen Einsatz empfohlen. |
| **Decksdurchführung** | Stelle, an der die Trockenauspuffleitung durch das Deck nach oben geführt wird. Muss hitzebeständig und wasserdicht sein. |
| **EPDM** | Ethylen-Propylen-Dien-Monomer-Kautschuk. Standardmaterial für Nassauspuffschläuche. Temperaturbeständig bis ~100 °C. |
| **Faltenbalg (Kompensator)** | Flexibles Edelstahl-Verbindungsstück im Trockenauspuff, das thermische Ausdehnung und Motorvibrationen aufnimmt. |
| **Frostschutzmittel** | Für die Abgasanlage: Propylenglykol (ungiftig). NICHT Ethylenglykol (Autofrostschutz, giftig). |
| **Funkenfänger** | Edelstahlnetz im Schornsteinkopf eines Trockenauspuffs, das Funken abfängt. Vorgeschrieben bei Holzbooten und in Naturschutzgebieten. |
| **Gegendruck** | Siehe Abgasgegendruck. |
| **GFK/FRP** | Glasfaserverstärkter Kunststoff / Fibre Reinforced Plastic. Material für Wassersammler und Schalldämpfer. Erweicht ab ~120 °C. |
| **Gusseisen** | Traditionelles Material für Mischkrümmer. Preiswert, aber korrosionsanfällig in Salzwasser. Lebensdauer: 5–8 Jahre. |
| **Helmholtz-Resonator** | Akustischer Schalldämpfer: Kammer mit definiertem Halsquerschnitt, abgestimmt auf eine bestimmte Frequenz. |
| **Hydrolock** | Wasserschlag im Zylinder. Wasser gelangt in den Zylinder und wird vom Kolben komprimiert → extreme Kräfte → mechanische Zerstörung (Pleuel, Kolben, Kurbelwelle). |
| **Impeller** | Gummiflügelrad der Seewasser-Kühlpumpe. Fördert das Kühlwasser durch den Mischkrümmer. Verschleißteil (1–2 Jahre). |
| **Injection Elbow** | Englisch für Mischkrümmer. Der Punkt, an dem Kühlwasser in den Abgasstrom eingespritzt wird. |
| **ISO 13363** | Internationale Norm für Nassauspuff-Systeme (Schläuche) in Sportbooten. |
| **ISO 9094** | Internationale Norm für Brandschutz auf Sportbooten. Relevant für Mindestabstände und Isolierung. |
| **Italian Tune-up** | Umgangssprachlich: Motor unter Volllast fahren, um Ablagerungen zu verbrennen. Bei Wet Stacking empfohlen. |
| **Keramikfaser** | Hochtemperatur-Isoliermaterial für Trockenauspuff. Bis 1.260 °C beständig. |
| **Krängung** | Seitliche Neigung eines Bootes. Bei Segelyachten typisch 15–25°. Beeinflusst die effektive Schwanenhals-Höhe erheblich. |
| **Kühlwassermantel** | Hohlraum im Mischkrümmer, durch den Kühlwasser fließt, bevor es in den Abgasstrom eingespritzt wird. |
| **Lift Muffler** | Schalldämpfer/Wassersammler-Kombination. Das Wasser wird durch den Abgasdruck nach oben "geliftet". Standard bei Segelyachten. |
| **Mischkrümmer** | Das Bauteil, an dem Kühlwasser in den Abgasstrom eingespritzt wird. Kritischstes Verschleißteil am Marine-Diesel. |
| **Mischzone** | Bereich im Mischkrümmer, wo heißes Abgas und kühles Wasser aufeinandertreffen. Höchste thermische/chemische Belastung. |
| **Monel** | Nickel-Kupfer-Legierung (65 % Ni, 33 % Cu). Ähnlich wie Ni-Resist, aber geschmiedet statt gegossen. Extrem korrosionsbeständig. |
| **Nassauspuff (Wet Exhaust)** | Abgassystem, bei dem Kühlwasser in den Abgasstrom eingespritzt wird. Standard bei >95 % der Sportboote. |
| **Ni-Resist** | Nickel-Kupfer-Gusseisen-Legierung für Mischkrümmer. Hochkorrosionsbeständig. Premium-Material. |
| **NiCu** | Abkürzung für Nickel-Kupfer-Legierung. Siehe Ni-Resist. |
| **Propylenglykol** | Ungiftiges Frostschutzmittel für marine Kühlsysteme. Im Gegensatz zu Ethylenglykol umwelt- und lebensmittelverträglich. |
| **Pyrometer** | Temperaturmessgerät für hohe Temperaturen. Kontaktlos (Infrarot) oder mit Thermoelement. Für Abgastemperaturmessung. |
| **Rückschlagklappe** | Federbelastete Klappe am Auspuffauslass, die Wassereindrung bei Wellengang verhindert. Zusätzliche Sicherung, nicht alleiniger Schutz. |
| **SAE J2006 R2** | US-Standard für marine Auspuffschläuche. Definiert Materialanforderungen und Temperaturbeständigkeit. |
| **Schalldämpfer (Muffler)** | Bauteil zur Reduzierung des Abgasgeräuschs. Im Nassauspuff: Lift Muffler, Waterlock. Im Trockenauspuff: Absorptions- oder Reaktionsschalldämpfer. |
| **Schwanenhals (Swan Neck)** | Invertiertes U-Rohr im Nassauspuff, das den höchsten Punkt bildet. Primäre Barriere gegen Wasserrückfluss in den Motor. |
| **Schwefelsäure-Kondensat** | Entsteht, wenn schwefelhaltiges Abgas unter den Taupunkt abkühlt. Greift Gusseisen und selbst Edelstahl an. |
| **Seewasserventil** | Absperrhahn am Rumpfdurchlass, durch den Kühlwasser angesaugt wird. Sollte bei Nicht-Betrieb geschlossen werden. |
| **Siphon-Effekt** | Physikalischer Effekt: Wasser fließt durch einen höherliegenden Punkt aufgrund von Druckunterschieden. Im Kühlsystem → Wasser fließt auch ohne Pumpe. |
| **Spannungsrisskorrosion** | Korrosionsform, die bei Edelstahl in Chlorid-Umgebung bei erhöhter Temperatur auftritt. Rissbildung ohne äußere mechanische Last. |
| **T-Bolt-Schelle** | Hochwertige Schlauchschelle mit T-förmigen Schrauben. Gleichmäßige Druckverteilung, Standard für Nassauspuff-Verbindungen. |
| **Transom-Fitting** | Auspuffauslass-Beschlag am Heck (Transom) des Bootes. Edelstahl 316L oder Bronze. |
| **Trockenauspuff (Dry Exhaust)** | Abgassystem ohne Wassereinspritzung. Heißes Abgas, isolierte Metallrohre, Schornstein. Standard bei Booten >20 m und Arbeitsschiffen. |
| **Turbolader** | Abgasturbolader: nutzt Abgasenergie zur Verdichtung der Ansaugluft. Relevant für Abgasanlage: höherer Abgasstrom, empfindlicher gegen Gegendruck. |
| **Vacuum Breaker** | Englisch für Anti-Siphon-Ventil. |
| **Vernalift** | Patentierter Schalldämpfer/Wassersammler von Centek Industries. |
| **Vetus** | Niederländischer Hersteller von Marine-Komponenten. Marktführer bei Abgaskomponenten (Schalldämpfer, Wassersammler, Schläuche, Anti-Siphon-Ventile). |
| **Waterlock** | Englisch für Wassersammler. Behälter im Nassauspuff, der Wasser abscheidet und als Rückflussbarriere dient. |
| **Wassersammler** | Deutsch für Waterlock. Siehe dort. |
| **Wet Stacking** | Nassverbrennung: Unvollständige Verbrennung bei Dieselmotoren unter zu geringer Last. Teerartige Ablagerungen im Auspuffsystem. |
| **Zink-Anode** | Opferanode im Kühlwassersystem, die galvanische Korrosion am Mischkrümmer und Wärmetauscher verzögert. Verschleißteil. |

---
---

## 18. Schnell-Referenz

### 18.1 Mischkrümmer-Austausch nach Motortyp

| Motor | OEM-Teilenummer | Material OEM | Aftermarket (316L) | Preis OEM | Preis Aftermarket |
|-------|----------------|-------------|-------------------|-----------|-------------------|
| Volvo Penta 2003 | 3580918 | Gusseisen | Osco VV-80918 | ~350 EUR | ~500 EUR |
| Volvo Penta D1-30 | 22898216 | NiCu | Barr VP1-30 | ~650 EUR | ~550 EUR |
| Volvo Penta D2-40 | 22840507 | Gusseisen | Osco VV-40507 | ~450 EUR | ~600 EUR |
| Volvo Penta D2-75 | 22840507 | Gusseisen | Osco VV-40507 | ~450 EUR | ~600 EUR |
| Volvo Penta D4-260 | 3589907 | NiCu | Barr VP4-260 | ~1.200 EUR | ~950 EUR |
| Volvo Penta D6-370 | 21469181 | NiCu | Barr VP6-370 | ~1.800 EUR | ~1.400 EUR |
| Yanmar 3YM20 | 128990-13520 | Gusseisen | Osco YA-13520 | ~300 EUR | ~450 EUR |
| Yanmar 3YM30 | 128990-13520 | Gusseisen | Osco YA-13520 | ~300 EUR | ~450 EUR |
| Yanmar 4JH5E | 129671-13560 | Gusseisen | Osco YA-13560 | ~400 EUR | ~550 EUR |
| Yanmar 4JH4-TE | 129472-13560 | Gusseisen | Barr YA-4JH4 | ~380 EUR | ~500 EUR |
| Yanmar 6LP-STE | 119773-13501 | Gusseisen | Osco YA-13501 | ~550 EUR | ~700 EUR |
| Perkins M35 | 3586779 | Gusseisen | Barr PE-M35 | ~280 EUR | ~400 EUR |
| Perkins M92B | 131616340 | Gusseisen | Barr PE-M92 | ~350 EUR | ~500 EUR |
| Nanni N4.50 | 970312174 | Gusseisen | — | ~420 EUR | — |
| Bukh DV36 | 033D3516 | Gusseisen | — | ~380 EUR | — |
| Beta Marine 43 | 209-63990 | Gusseisen | Barr BM-43 | ~300 EUR | ~450 EUR |

### 18.2 Abgas-Systemdiagnose auf einen Blick

| Symptom | Wahrscheinliche Ursache | Sofortmaßnahme |
|---------|------------------------|----------------|
| Kein Wasser am Auslass | Impeller defekt, Seewasserventil zu | Motor STOPPEN, Impeller prüfen |
| Wenig Wasser am Auslass | Impeller verschlissen, Filter verstopft | Motor stoppen, Kühlsystem prüfen |
| Abgas >80 °C nach Mischkrümmer | Kühlungsproblem | Motor stoppen, System prüfen |
| Wasser am Mischkrümmer | Durchrostung, lose Schelle | Motor stoppen, inspizieren |
| Abgasgeruch im Motorraum | Schlauch defekt, Schelle lose | CO-Gefahr! Motor stoppen, lüften |
| Schwarzer Rauch | Wet Stacking, Injektoren, Verstopfung | Unter Last fahren, ggf. Werft |
| Blauer Rauch | Turbo-Öl, Zylinderverschleiß | Ölstand prüfen, Werft |
| Weißer Rauch (exzessiv) | Wasser in Zylindern, Mischkrümmer defekt | Motor stoppen, Mischkrümmer prüfen |
| Motor startet nicht nach Liegen | Wasser in Zylindern (Hydrolock) | NICHT weiter anlassen! Injektoren öffnen |
| Tropft schwarz am Auslass | Wet Stacking | Unter Last fahren |
| Auspuff deutlich lauter | Schalldämpfer defekt | Inspizieren, ggf. ersetzen |

### 18.3 Wartungsintervalle Abgasanlage

| Komponente | Inspektion | Austausch |
|------------|-----------|----------|
| Mischkrümmer (Gusseisen) | Jährlich + alle 500 h | 5–8 Jahre / 1.500–3.000 h |
| Mischkrümmer (Edelstahl 316L) | Jährlich + alle 1.000 h | 10–15 Jahre / 3.000–6.000 h |
| Mischkrümmer (NiCu) | Jährlich + alle 1.000 h | 12–20 Jahre / 5.000–10.000 h |
| Auspuffschlauch | Jährlich | 5–8 Jahre |
| Schlauchschellen | Jährlich | Bei Inspektion, alle 5 Jahre |
| Wassersammler | Jährlich | 10–15 Jahre |
| Schalldämpfer | Alle 2 Jahre | 10–15 Jahre |
| Anti-Siphon-Ventil (Membrane) | Jährlich | 3–5 Jahre |
| Anti-Siphon-Ventil (komplett) | Jährlich | 5–8 Jahre |
| Transom-Fitting | Jährlich | 15–25 Jahre |
| CO-Detektor | Monatlich (Testknopf) | 5–7 Jahre (Sensoren altern) |

---
---

## 19. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Mischkrümmer-Durchrostung bei Volvo Penta 2003

**Boot:** Bavaria 32, Baujahr 2004, Volvo Penta 2003 (28 PS)
**Liegeplatz:** Ostsee (Brackwasser)
**Betriebsstunden:** 1.850 h
**Alter Mischkrümmer:** 11 Jahre, Original-Gusseisen (Volvo PN 3580918)

**Befund:**
Bei der Saisonvorbereitung 2015 bemerkte der Eigner einen leichten
Wasserfleck am Mischkrümmer. Der Krümmer wurde demontiert. Inneninspektion
zeigte massive Korrosion im Wasserkanal — die Wandstärke war an der
dünnsten Stelle auf 1,2 mm reduziert (original: 8 mm). An einer Stelle
war ein Haarriss sichtbar, durch den minimal Wasser austrat.

**Kritisch:** Der Eigner hatte das Boot zwei Wochen zuvor an einem windigen
Wochenende im Hafen liegen lassen — mit offenem Seewasserventil und OHNE
Anti-Siphon-Ventil. Bei der Rückkehr war der Motorölstand erhöht und das
Öl milchig. Es war bereits Wasser über den Siphon-Effekt durch den
angerissenen Krümmer in den Motor gelangt.

**Maßnahmen:**
1. Sofortiger Ölwechsel (2×) mit Spülung
2. Glühkerzen entfernt, Motor durchgedreht → kein Widerstand (Glück gehabt)
3. Mischkrümmer ersetzt: Osco Edelstahl 316L (~500 EUR)
4. Anti-Siphon-Ventil nachgerüstet: Vetus NASBV19 (~35 EUR)
5. Auspuffschlauch ebenfalls ersetzt (10 Jahre alt, verhärtet)
6. Gesamtkosten: ~850 EUR (Teile) + 300 EUR (Werft) = 1.150 EUR

**Lehre:** Regelmäßige Inspektion des Mischkrümmers und Installation
eines Anti-Siphon-Ventils hätten den Motorschaden verhindert. Der Eigner
hatte "Glück im Unglück" — 2 Wochen länger, und es wäre Hydrolock gewesen.

---

### ANHANG B — Fallstudie: Hydrolock durch fehlenden Wassersammler

**Boot:** Dehler 34, Baujahr 1999, Volvo Penta MD2030 (29 PS)
**Liegeplatz:** Mittelmeer (Kroatien)
**Betriebsstunden:** 2.400 h

**Befund:**
Beim Motorstart nach zweiwöchiger Hafenliegezeit dreht der Anlasser
den Motor nicht. Mechaniker findet Wasser in den Zylindern 2 und 3.
Pleuelstange Zylinder 2 ist verbogen. Motorblock hat Haarriss an Zylinder 3.

**Ursache:**
Die Werft hatte bei einer früheren Reparatur den defekten Wassersammler
entfernt und durch ein einfaches Schlauchstück ersetzt — "provisorisch",
was dann 3 Jahre so blieb. Ohne Wassersammler konnte das Wasser nach
Motorstillstand ungehindert vom Schwanenhals zurück zum Motor fließen.
Ein Anti-Siphon-Ventil war nicht verbaut. Der Schwanenhals war nur
200 mm über der Wasserlinie — bei Wellen im Hafen reichte das nicht.

**Kosten des Schadens:**
- Motorrevision: nicht möglich (Block gerissen)
- Motortausch (gebrauchter Volvo MD2030): 4.500 EUR
- Einbau: 2.500 EUR
- Neues Abgassystem komplett: 900 EUR
- Gesamt: 7.900 EUR

**Lehre:** Ein Wassersammler für 150 EUR hätte den Totalschaden verhindert.
"Provisorien" in der Abgasanlage sind NIEMALS akzeptabel.

---

### ANHANG C — Fallstudie: CO-Vergiftung durch gerissenen Auspuffschlauch

**Boot:** Jeanneau Sun Odyssey 42, Baujahr 2008, Yanmar 4JH4-TE (54 PS)
**Liegeplatz:** Atlantik (Kanarische Inseln)
**Betriebsstunden:** 3.100 h

**Befund:**
Während einer Überführungsfahrt bei Motorbetrieb klagt die Crew über
Kopfschmerzen und Übelkeit. Der Skipper vermutet Seekrankheit und
fährt weiter. Erst als ein Crewmitglied ohnmächtig wird, stoppt er
den Motor und öffnet alle Luken. Nachträglich wird ein CO-Wert von
380 ppm im Salon gemessen (Schwellenwert: 50 ppm).

**Ursache:**
Der Nassauspuffschlauch (12 Jahre alt, nie ersetzt) hatte einen
10 cm langen Riss an einer Biegestelle. Abgase einschließlich CO
traten in den Motorraum aus und gelangten über die Motorraum-
Belüftung in den Salon. Ein CO-Detektor war nicht an Bord.

**Maßnahmen:**
1. Auspuffschlauch komplett ersetzt (neuer Shields 250, 90 mm)
2. Alle Schlauchschellen ersetzt (T-Bolt Edelstahl 316)
3. CO-Detektoren in Salon, Achterkajüte und Vorschiff installiert
4. Jährliche Schlauchinspektion in Wartungsplan aufgenommen

**Lehre:** Auspuffschläuche müssen alle 5–8 Jahre präventiv ersetzt
werden. CO-Detektoren in allen bewohnten Räumen retten Leben.
CO-Vergiftungssymptome ähneln der Seekrankheit — eine tückische Verwechslung.

---

### ANHANG D — Fallstudie: Wet Stacking bei Segelyacht-Motor

**Boot:** Hallberg-Rassy 36, Baujahr 2011, Volvo Penta D2-55 (55 PS)
**Liegeplatz:** Nordsee (Cuxhaven)
**Betriebsstunden:** 1.200 h (in 10 Jahren)

**Befund:**
Motor verliert zunehmend Leistung, raucht schwarz, tropft teerartige
Substanz am Auspuffauslass. Mechaniker findet bei Inspektion:
Wassersammler zu 40 % mit schwarzem Schlamm gefüllt, Auspuffschlauch
innen beschichtet mit teerartiger Masse, Schalldämpfer-Wirkung reduziert.

**Ursache:**
Die Eigner segeln viel und nutzen den Motor nur zum Ein-/Auslaufen
und bei Flaute — typisch 15–30 Minuten bei 1.500–2.000 U/min
(30–40 % Last). In 10 Jahren wurde der Motor nie über 2.500 U/min
gefahren. Der typische "Sonntagssegler"-Motor.

**Maßnahmen:**
1. Wassersammler gereinigt
2. Auspuffschlauch ersetzt (innen zu stark verengt)
3. Motor 2 Stunden bei 3.000 U/min (75 % Last) gefahren
4. Injektoren geprüft (leicht verrußt → gereinigt)
5. Empfehlung: Bei jeder Fahrt mindestens 20 Minuten bei >70 % Last

**Kosten:** 450 EUR (Schlauch + Reinigung + Arbeit)

**Lehre:** Segelyacht-Motoren leiden chronisch unter Unterlast.
Regelmäßiges "Ausfahren" ist keine Motorquälerei, sondern
notwendige Pflege.

---

### ANHANG E — Fallstudie: Galvanische Korrosion am Transom-Fitting

**Boot:** Beneteau Oceanis 38, Baujahr 2015, Yanmar 3YM30 (29 PS)
**Liegeplatz:** Mittelmeer (Marina Alicante, Spanien)

**Befund:**
Nach 5 Jahren zeigt das Transom-Fitting massive Korrosion — deutlich
stärker als bei Nachbarbooten gleichen Alters. Die Rückschlagklappe
ist festkorrodiert. Rund um das Fitting ist die Gelcoat verfärbt.

**Ursache:**
Das Fitting war aus Edelstahl 304 (nicht 316L). In direkter Nähe befand
sich ein Aluminium-Badeplattform-Beschlag. Die Kombination Edelstahl +
Aluminium in Salzwasser = galvanische Korrosion des unedleren Metalls
(Aluminium zuerst, dann beschleunigter Angriff auf den Edelstahl durch
Kontaktkorrosion). Das 304er-Material war dem aggressiven mediterranen
Salzwasser nicht gewachsen.

**Maßnahmen:**
1. Fitting ersetzt durch Edelstahl 316L (Vetus TRC90)
2. Kunststoff-Isolierscheiben zwischen Fitting und Alu-Beschlag
3. Neue Dichtung mit Sikaflex 291i
4. Jährliche Kontrolle empfohlen

**Kosten:** 180 EUR (Fitting + Dichtmittel) + 200 EUR (Einbau Werft)

**Lehre:** Im Salzwasser nur Edelstahl 316L oder Bronze. Galvanische
Korrosion durch Materialtrennung (Kunststoff-Unterlegscheiben) verhindern.

---

### ANHANG F — Fallstudie: Anti-Siphon-Ventil vergessen — Beinahe-Hydrolock

**Boot:** Moody 38, Baujahr 2007, Volvo Penta D2-40 (40 PS)
**Liegeplatz:** Englischer Kanal (Solent)

**Befund:**
Der Eigner bemerkt nach einer Woche im Hafen (Seewasserventil offen,
Motor nicht betrieben), dass der Wasserstand im Wassersammler deutlich
höher ist als nach dem letzten Motorstopp. Er entleert den Wassersammler
(ca. 3 Liter Seewasser) und untersucht das System.

**Ursache:**
Das Anti-Siphon-Ventil (Vetus NASBV, Baujahr 2007) war noch das Original.
Die Membrane war verhärtet und öffnete nicht mehr. Der Siphon-Effekt
hatte über eine Woche kontinuierlich Seewasser durch den Mischkrümmer
in den Wassersammler gedrückt. Der Wassersammler war fast voll — noch
ein Tag, und das Wasser wäre übergelaufen und in den Motor geflossen.

**Maßnahmen:**
1. Anti-Siphon-Ventil-Membrane ersetzt (Vetus Ersatzteilset ~15 EUR)
2. Seewasserventil-Disziplin: Ab jetzt bei jedem Verlassen geschlossen
3. Hinweisschild am Zündschlüssel: "Seewasserventil prüfen!"

**Kosten:** 15 EUR (Membrane) — Ersparnis: potenziell >10.000 EUR Motorschaden

**Lehre:** Das Anti-Siphon-Ventil ist ein 25-EUR-Teil mit
10.000-EUR-Schadenspotenzial. Jährliche Wartung ist Pflicht.

---

### ANHANG G — Fallstudie: Trockenauspuff-Konversion auf Stahlsegelyacht

**Boot:** Reinke S11, Stahlsegelyacht 11 m, Baujahr 1998, Nanni N4.50 (50 PS)
**Liegeplatz:** Binnenwasserstraßen + Nordsee

**Befund:**
Der Eigner hatte in 15 Jahren drei Gusseisen-Mischkrümmer verschlissen
und entschied sich für die Konversion auf Trockenauspuff. Das Stahlboot
bot ideale Voraussetzungen: Schweißbare Rohrführung, kein GFK als
Brandrisiko, vorhandener Platz für Decksdurchführung.

**Umsetzung:**
1. Trockener Edelstahl-Auspuffkrümmer (Sonderanfertigung): 800 EUR
2. Edelstahl-Auspuffrohr (3 m, 60 mm, 316L): 350 EUR
3. Kompensator (Edelstahl-Faltenbalg): 180 EUR
4. Trockener Absorptionsschalldämpfer: 450 EUR
5. Keramikfaser-Isolierung (50 mm, Alu-Ummantelung): 300 EUR
6. Decksdurchführung mit Regenwasserkappe: 250 EUR
7. Arbeitszeit (Eigenleistung + Schweißer): 1.500 EUR
8. **Gesamt: 3.830 EUR**

**Ergebnis nach 8 Jahren:**
- Kein einziger Auspuff-Defekt
- Motor läuft effizienter (weniger Gegendruck)
- Kein Hydrolock-Risiko mehr
- Geräuschpegel höher als vorher → zusätzlicher Inline-Schalldämpfer
  nachgerüstet (150 EUR)
- Motorraum etwas wärmer → zusätzliche Belüftung eingebaut

**Lehre:** Auf Stahlbooten ist die Trockenauspuff-Konversion eine
hervorragende Langzeitlösung. Die Investition amortisiert sich nach
2–3 Mischkrümmer-Intervallen.

---

### ANHANG H — Fallstudie: Doppelmotorige Abgasanlage auf Motoryacht

**Boot:** Princess V45, Baujahr 2012, 2× Volvo Penta D6-370 (2× 370 PS)
**Liegeplatz:** Côte d'Azur (Marina Port Vauban, Antibes)
**Betriebsstunden:** 1.800 h (Backbord), 1.750 h (Steuerbord)

**Befund:**
Bei der jährlichen Inspektion wird am Steuerbord-Motor ein Mischkrümmer
mit beginnender Korrosion an den Wasserkanälen festgestellt. Der
Backbord-Krümmer ist noch in Ordnung, aber gleichen Alters.

**Entscheidung:** Beide Mischkrümmer gleichzeitig tauschen (gleiche
Belastung → gleicher Verschleiß → der andere wird bald folgen).

**Maßnahmen:**
1. 2× Volvo Penta OEM Mischkrümmer NiCu (PN 21469181): 2× 1.800 EUR
2. 2× Dichtsätze: 2× 45 EUR
3. 2× Auspuffschlauch-Sektionen (90 mm, Shields HT): 2× 180 EUR
4. 4× T-Bolt-Schellen (90 mm): 4× 12 EUR
5. 2× Anti-Siphon-Ventil-Membranen: 2× 18 EUR
6. Arbeitszeit Werft (2× Motor zugänglich machen, Tausch, Test): 1.200 EUR
7. **Gesamt: 5.354 EUR**

**Zusätzlich durchgeführt:**
- Generator-Abgasanlage inspiziert (OK, Onan 9 kW, 5 Jahre alt)
- CO-Detektoren in Salon, Schlafkajüte und Flybridge überprüft
- Wassersammler gereinigt (beide)
- Impeller gewechselt (beide Motoren + Generator)

**Lehre:** Bei Doppelmotoranlagen immer beide Seiten gleich warten.
Ein einzelner Krümmer-Tausch spart kurzfristig, kostet aber doppelt
Werftzeit, wenn der zweite 6 Monate später fällt.

### ANHANG H2 — Fallstudie: Generator-CO-Vergiftung im Hafen

**Boot:** Fairline Targa 38, Baujahr 2013, Generator Onan MDKBJ 7,5 kW
**Liegeplatz:** Marina di Ragusa, Sizilien
**Vorfall:** August 2023

**Befund:**
Ein Chartergast wird bewusstlos in der Achterkajüte aufgefunden. Der
Generator lief über Nacht für die Klimaanlage. Die Crew auf dem
Nachbarboot bemerkte den ungewöhnlichen Auspuffgeruch und alarmierte
den Hafenmeister.

**Ursache:**
Der Generator-Auspuffschlauch (8 Jahre alt, nie ersetzt) hatte einen
5 cm langen Riss an einer Biegestelle. Der Generator-Auslass war am
Heck platziert — in Lee des Nachbarbootes, direkt unter der eigenen
Heckkajüte. Der Wind drückte die Abgase (inkl. CO) nach oben in die
geöffnete Achterluke. Kein CO-Detektor an Bord.

**Folgen:**
- Crewmitglied: Krankenhausaufenthalt, 3 Tage, CO-Vergiftung mittleren Grades
- Charterfirma: Betriebsverbot bis zur Nachrüstung aller Boote
- Kosten: Krankenhauskosten, Charterausfall, Nachrüstung = >15.000 EUR

**Maßnahmen (gesamte Charterflotte):**
1. Alle Generator-Auspuffschläuche ersetzt
2. CO-Detektoren in allen Kabinen und im Cockpit nachgerüstet
3. Generator-Abgasanlage in den jährlichen Wartungsplan aufgenommen
4. Checkliste für Chartergäste: "Generator nur bei geschlossenen
   achteren Luken betreiben"

**Lehre:** Der Generator wird bei der Abgasanlagen-Wartung systematisch
vergessen. Er hat die gleichen Risiken wie der Hauptmotor — und
läuft oft nachts, wenn die Crew schläft. CO-Detektoren in allen
Schlafräumen sind lebensrettend.

---

### ANHANG H3 — Fallstudie: Falsch dimensionierter Wassersammler auf Neuboot

**Boot:** Hanse 388, Baujahr 2022, Yanmar 4JH5E (45 PS)
**Liegeplatz:** Nordsee (Bremerhaven)

**Befund:**
Beim ersten Wintercheck nach der Auslieferung fällt dem Eigner auf,
dass der Wasserstand im Wassersammler nach Motorstopp ungewöhnlich
hoch steht — fast bis zum Auslassanschluss. Bei der Messung ergibt
sich: Der Wassersammler hat nur 4 Liter Volumen. Für einen 45-PS-Motor
mit 2,5 m Auspuffleitung zum Wassersammler ist ein Mindestvolumen von
8–10 Litern erforderlich.

**Ursache:**
Die Werft hatte einen preiswerten Standard-Wassersammler eingebaut,
der für Motoren bis 25 PS dimensioniert war. Bei dem optionalen
größeren Motor (4JH5E statt Standard-3YM20) wurde der Wassersammler
nicht angepasst.

**Risiko:**
Bei jeder Motorabschaltung lief mehr Wasser in den Wassersammler
zurück, als dieser fassen konnte. Nur der Schwanenhals (korrekt
dimensioniert) verhinderte bisher den Rückfluss zum Motor. Bei Wellengang
im Hafen oder bei Fahrt wäre der Schwanenhals allein nicht ausreichend.

**Maßnahmen:**
1. Wassersammler ersetzt durch Vetus NLPH75 (14 L, passend)
2. Werft kontaktiert → Garantieanspruch bestätigt → Kostenübernahme
3. Anti-Siphon-Ventil zusätzlich eingebaut (fehlte ebenfalls)

**Kosten:** 160 EUR (Wassersammler) + 35 EUR (Anti-Siphon) + 250 EUR (Einbau)
= 445 EUR (von Werft übernommen)

**Lehre:** Auch bei Neubooten die Abgasanlage kritisch prüfen. Werften
optimieren auf Kosten, nicht auf Sicherheit. Besonders bei optionalen
Motorupgrades werden periphere Systeme nicht immer angepasst.

---

### ANHANG H4 — Fallstudie: Thermische Schlauchzerstörung durch Impeller-Versagen

**Boot:** Najad 355, Baujahr 2005, Volvo Penta D2-55 (55 PS)
**Liegeplatz:** Schweden (Westküste, Marstrand)

**Befund:**
Während einer Fahrt bei mäßigem Seegang bemerkt der Eigner plötzlich
intensiven Gummigeruch im Cockpit und schwarzen Rauch aus dem Motorraum.
Motor wird sofort gestoppt. Bei der Inspektion: Der Auspuffschlauch
direkt hinter dem Mischkrümmer ist auf 15 cm Länge geschmolzen und
deformiert. Wasser und Abgas treten aus. Der GFK-Boden des Motorraums
zeigt Brandspuren.

**Ursache:**
Der Impeller der Seewasserpumpe hatte 3 Flügel verloren. Die verbliebenen
Flügel förderten nur noch ~30 % des Soll-Kühlwassers. Die Abgastemperatur
nach dem Mischkrümmer stieg auf >150 °C (statt normal 50–70 °C).
Der Standard-EPDM-Schlauch (rated bis 100 °C) hielt dieser Temperatur
nicht stand und schmolz/verformte sich.

**Verschärfend:**
Die abgerissenen Impeller-Flügel hatten sich im Wärmetauscher verfangen
und den Kühlwasserdurchfluss zusätzlich eingeschränkt.

**Maßnahmen:**
1. Impeller ersetzt (28 EUR)
2. Impeller-Bruchstücke aus Wärmetauscher entfernt
3. Auspuffschlauch komplett ersetzt (1,5 m Shields 252 HT direkt nach
   Mischkrümmer + 2 m Standard für den Rest)
4. EGT-Alarm (80 °C Schwelle) nach Mischkrümmer installiert
5. GFK-Boden im Brandbereich repariert

**Kosten:** 450 EUR (Teile) + 600 EUR (Werft) = 1.050 EUR

**Lehre:** Impeller-Versagen → Kühlwasserausfall → Abgas überhitzt →
Schlauchzerstörung → Brandgefahr. Die Kette ist schnell. Ein
Abgastemperatur-Alarm nach dem Mischkrümmer (80 °C Schwelle) hätte
den Eigner 10 Minuten früher gewarnt und den Schaden begrenzt.

---
---

## 20. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — ExhaustSystemType (Enum)

```python
from enum import Enum


class ExhaustSystemType(str, Enum):
    """Typ des Abgassystems."""
    WET = "wet"                    # Nassauspuff
    DRY = "dry"                    # Trockenauspuff
    SEMI_DRY = "semi_dry"         # Halbtrockenes System (selten)
    UNKNOWN = "unknown"            # Unbekannt
```

### ANHANG J — MixingElbowMaterial (Enum)

```python
class MixingElbowMaterial(str, Enum):
    """Material des Mischkrümmers."""
    CAST_IRON = "cast_iron"                  # Gusseisen
    STAINLESS_316L = "stainless_316l"        # Edelstahl 316L
    STAINLESS_316TI = "stainless_316ti"      # Edelstahl 316Ti
    NICU = "nicu"                            # Nickel-Kupfer (Ni-Resist)
    BRONZE = "bronze"                        # Bronze
    COATED_CAST_IRON = "coated_cast_iron"    # Beschichtetes Gusseisen
    UNKNOWN = "unknown"                      # Unbekannt
```

### ANHANG K — ExhaustComponentCondition (Enum)

```python
class ExhaustComponentCondition(str, Enum):
    """Zustandsbewertung einer Abgaskomponente."""
    EXCELLENT = "excellent"      # Ausgezeichnet — neuwertig
    GOOD = "good"                # Gut — normaler Verschleiß
    FAIR = "fair"                # Befriedigend — Verschleiß sichtbar
    POOR = "poor"                # Schlecht — Austausch empfohlen
    CRITICAL = "critical"        # Kritisch — sofortiger Austausch nötig
    FAILED = "failed"            # Ausgefallen — nicht funktionsfähig
    NOT_INSPECTED = "not_inspected"  # Nicht inspiziert
```

### ANHANG L — MixingElbowSpec (Spezifikation)

```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class MixingElbowSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung eines Mischkrümmers (Injection Elbow).
    Das kritischste Verschleißteil am Marine-Diesel.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    engine_model: str = Field(
        ..., description="Motormodell (z.B. 'Volvo Penta D2-40')"
    )
    oem_part_number: Optional[str] = Field(
        None, description="OEM-Teilenummer (z.B. '22840507')"
    )
    aftermarket_part_number: Optional[str] = Field(
        None, description="Aftermarket-Teilenummer, falls nicht OEM"
    )
    manufacturer: str = Field(
        ..., description="Hersteller (z.B. 'Volvo Penta', 'Osco', 'Barr Marine')"
    )

    # Material und Alter
    material: MixingElbowMaterial = Field(
        ..., description="Material des Mischkrümmers"
    )
    installation_date: Optional[date] = Field(
        None, description="Einbaudatum"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    operating_hours_since_install: Optional[int] = Field(
        None, ge=0, description="Betriebsstunden seit Einbau"
    )

    # Zustand
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    wall_thickness_mm: Optional[float] = Field(
        None, ge=0, le=20,
        description="Gemessene minimale Wandstärke in mm"
    )
    wall_thickness_original_mm: Optional[float] = Field(
        None, ge=0, le=20,
        description="Originale Wandstärke in mm"
    )
    wall_thickness_loss_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Wandstärkenverlust in Prozent"
    )
    internal_corrosion: Optional[str] = Field(
        None, description="Beschreibung der internen Korrosion"
    )
    external_corrosion: Optional[str] = Field(
        None, description="Beschreibung der externen Korrosion"
    )
    water_channel_blocked: Optional[bool] = Field(
        None, description="Wasserkanal verstopft?"
    )
    cracks_detected: Optional[bool] = Field(
        None, description="Risse erkannt?"
    )
    leak_detected: Optional[bool] = Field(
        None, description="Leckage erkannt?"
    )

    # Empfehlung
    remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    remaining_life_hours: Optional[int] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer in Betriebsstunden"
    )
    replacement_recommended: bool = Field(
        ..., description="Austausch empfohlen?"
    )
    replacement_urgency: Optional[str] = Field(
        None, description="Dringlichkeit: 'immediate', 'next_season', 'planned'"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Austauschkosten (Material + Arbeit) in EUR"
    )

    # Konfidenz
    confidence: str = Field(
        ..., description="Konfidenzstufe (measured, visual_high, visual_medium, estimated)"
    )
    inspection_method: Optional[str] = Field(
        None, description="Inspektionsmethode (visual_external, visual_internal, endoscopy, removal, pressure_test)"
    )
```

### ANHANG M — WaterlockSpec (Wassersammler)

```python
class WaterlockSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung eines Wassersammlers (Waterlock).
    """
    model_config = {"from_attributes": True}

    manufacturer: Optional[str] = Field(
        None, description="Hersteller (z.B. 'Vetus', 'Centek')"
    )
    model: Optional[str] = Field(
        None, description="Modellbezeichnung (z.B. 'NLPH75')"
    )
    material: Optional[str] = Field(
        None, description="Material (z.B. 'kunststoff', 'gfk', 'edelstahl')"
    )
    volume_liters: Optional[float] = Field(
        None, ge=0, le=100,
        description="Nennvolumen in Litern"
    )
    required_volume_liters: Optional[float] = Field(
        None, ge=0, le=100,
        description="Berechnetes Mindestvolumen in Litern"
    )
    volume_adequate: Optional[bool] = Field(
        None, description="Volumen ausreichend dimensioniert?"
    )
    connection_diameter_mm: Optional[int] = Field(
        None, ge=20, le=200,
        description="Anschlussdurchmesser in mm"
    )
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    drain_valve_present: Optional[bool] = Field(
        None, description="Ablassventil vorhanden?"
    )
    drain_valve_functional: Optional[bool] = Field(
        None, description="Ablassventil funktionsfähig?"
    )
    sediment_level: Optional[str] = Field(
        None, description="Ablagerungsgrad: 'clean', 'light', 'moderate', 'heavy'"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    replacement_recommended: bool = Field(
        ..., description="Austausch empfohlen?"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG N — AntiSiphonValveSpec

```python
class AntiSiphonValveSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung eines Anti-Siphon-Ventils.
    """
    model_config = {"from_attributes": True}

    present: bool = Field(
        ..., description="Anti-Siphon-Ventil vorhanden?"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller"
    )
    model: Optional[str] = Field(
        None, description="Modellbezeichnung"
    )
    connection_diameter_mm: Optional[int] = Field(
        None, ge=10, le=50,
        description="Anschlussdurchmesser in mm"
    )
    height_above_waterline_mm: Optional[int] = Field(
        None,
        description="Einbauhöhe über Wasserlinie in mm"
    )
    height_adequate: Optional[bool] = Field(
        None, description="Einbauhöhe ausreichend (>300 mm über WL)?"
    )
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    membrane_condition: Optional[str] = Field(
        None, description="Membrane-Zustand: 'good', 'hardened', 'cracked', 'missing'"
    )
    vent_clear: Optional[bool] = Field(
        None, description="Entlüftungsöffnung frei?"
    )
    functional_test_passed: Optional[bool] = Field(
        None, description="Funktionsprüfung bestanden?"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    replacement_recommended: bool = Field(
        ..., description="Austausch/Wartung empfohlen?"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG O — SwanNeckSpec

```python
class SwanNeckSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung des Schwanenhalses.
    """
    model_config = {"from_attributes": True}

    present: bool = Field(
        ..., description="Schwanenhals vorhanden?"
    )
    type: Optional[str] = Field(
        None, description="Typ: 'rigid_grp', 'rigid_stainless', 'flexible_hose', 'vetus_fitting'"
    )
    apex_height_above_wl_mm: Optional[int] = Field(
        None,
        description="Scheitelpunkthöhe über statischer Wasserlinie in mm"
    )
    required_height_mm: Optional[int] = Field(
        None,
        description="Berechnete Mindesthöhe über WL in mm"
    )
    height_adequate: Optional[bool] = Field(
        None, description="Höhe ausreichend?"
    )
    heel_angle_considered: Optional[float] = Field(
        None, ge=0, le=45,
        description="Berücksichtigter Krängungswinkel in Grad (Segelboote)"
    )
    effective_height_at_heel_mm: Optional[int] = Field(
        None,
        description="Effektive Höhe bei Krängung in mm"
    )
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    continuous_fall_to_outlet: Optional[bool] = Field(
        None, description="Kontinuierliches Gefälle zum Auslass?"
    )
    support_adequate: Optional[bool] = Field(
        None, description="Halterung ausreichend?"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG P — ExhaustHoseSpec

```python
class ExhaustHoseSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung der Auspuffschläuche.
    """
    model_config = {"from_attributes": True}

    sections: list[dict] = Field(
        default_factory=list,
        description="Liste der Schlauchabschnitte mit Position, Länge, Zustand"
    )
    total_length_m: Optional[float] = Field(
        None, ge=0, le=20,
        description="Gesamtlänge aller Schläuche in Metern"
    )
    inner_diameter_mm: Optional[int] = Field(
        None, ge=20, le=200,
        description="Innendurchmesser in mm"
    )
    required_diameter_mm: Optional[int] = Field(
        None, ge=20, le=200,
        description="Berechneter Mindest-Innendurchmesser in mm"
    )
    diameter_adequate: Optional[bool] = Field(
        None, description="Durchmesser ausreichend?"
    )
    material: Optional[str] = Field(
        None, description="Material (z.B. 'epdm', 'epdm_ht', 'epdm_wire')"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller (z.B. 'Shields', 'Trident', 'Vetus')"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    cracks_present: Optional[bool] = Field(
        None, description="Risse vorhanden?"
    )
    hardened: Optional[bool] = Field(
        None, description="Schlauch verhärtet?"
    )
    swelling: Optional[bool] = Field(
        None, description="Quellungen vorhanden?"
    )
    clamps_condition: Optional[str] = Field(
        None, description="Schellen-Zustand: 'good', 'corroded', 'loose', 'wrong_type'"
    )
    clamp_type: Optional[str] = Field(
        None, description="Schellen-Typ: 't_bolt_316', 'worm_drive', 'spring'"
    )
    double_clamped: Optional[bool] = Field(
        None, description="Doppelschellen an Verbindungen?"
    )
    sag_present: Optional[bool] = Field(
        None, description="Durchhängen vorhanden? (Wasseransammlung)"
    )
    continuous_fall: Optional[bool] = Field(
        None, description="Kontinuierliches Gefälle zum Auslass?"
    )
    replacement_recommended: bool = Field(
        ..., description="Austausch empfohlen?"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Austauschkosten in EUR"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG Q — ExhaustOutletSpec

```python
class ExhaustOutletSpec(BaseModel):
    """
    Spezifikation und Zustandsbewertung des Auspuffauslasses.
    """
    model_config = {"from_attributes": True}

    position: str = Field(
        ..., description="Position: 'transom', 'hull_side', 'below_waterline', 'stack'"
    )
    material: Optional[str] = Field(
        None, description="Material (z.B. 'stainless_316l', 'bronze', 'grp')"
    )
    diameter_mm: Optional[int] = Field(
        None, ge=20, le=200,
        description="Durchmesser in mm"
    )
    height_above_wl_mm: Optional[int] = Field(
        None,
        description="Höhe über Wasserlinie in mm (negativ = unter WL)"
    )
    flap_valve_present: Optional[bool] = Field(
        None, description="Rückschlagklappe vorhanden?"
    )
    flap_valve_functional: Optional[bool] = Field(
        None, description="Rückschlagklappe funktionsfähig?"
    )
    condition: ExhaustComponentCondition = Field(
        ..., description="Zustandsbewertung"
    )
    corrosion_level: Optional[str] = Field(
        None, description="Korrosionsgrad: 'none', 'surface', 'moderate', 'severe'"
    )
    hull_seal_condition: Optional[str] = Field(
        None, description="Dichtungszustand zum Rumpf: 'good', 'fair', 'poor'"
    )
    replacement_recommended: bool = Field(
        ..., description="Austausch empfohlen?"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

### ANHANG R — ExhaustSystemAnalysis (Orchestrierungs-Modell)

```python
class ExhaustSystemAnalysis(BaseModel):
    """
    Orchestrierungs-Modell für die Gesamtanalyse einer marinen Abgasanlage.
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

    # System-Typ
    exhaust_system_type: ExhaustSystemType = Field(
        ..., description="Typ des Abgassystems"
    )
    engine_power_ps: Optional[int] = Field(
        None, ge=0,
        description="Motorleistung in PS"
    )
    engine_model: Optional[str] = Field(
        None, description="Motormodell"
    )

    # Teilanalysen
    mixing_elbow: Optional[MixingElbowSpec] = Field(
        None, description="Mischkrümmer-Bewertung"
    )
    waterlock: Optional[WaterlockSpec] = Field(
        None, description="Wassersammler-Bewertung"
    )
    anti_siphon_valve: Optional[AntiSiphonValveSpec] = Field(
        None, description="Anti-Siphon-Ventil-Bewertung"
    )
    swan_neck: Optional[SwanNeckSpec] = Field(
        None, description="Schwanenhals-Bewertung"
    )
    exhaust_hose: Optional[ExhaustHoseSpec] = Field(
        None, description="Auspuffschlauch-Bewertung"
    )
    exhaust_outlet: Optional[ExhaustOutletSpec] = Field(
        None, description="Auspuffauslass-Bewertung"
    )

    # Hydrolock-Risiko
    hydrolock_risk_level: Optional[str] = Field(
        None, description="Hydrolock-Risiko: 'low', 'medium', 'high', 'critical'"
    )
    hydrolock_risk_factors: list[str] = Field(
        default_factory=list,
        description="Identifizierte Hydrolock-Risikofaktoren"
    )

    # CO-Risiko
    co_risk_level: Optional[str] = Field(
        None, description="CO-Risiko: 'low', 'medium', 'high', 'critical'"
    )
    co_risk_factors: list[str] = Field(
        default_factory=list,
        description="Identifizierte CO-Risikofaktoren"
    )
    co_detector_present: Optional[bool] = Field(
        None, description="CO-Detektor(en) an Bord?"
    )

    # Gegendruck
    backpressure_estimated_mbar: Optional[float] = Field(
        None, ge=0,
        description="Geschätzter Abgasgegendruck in mbar"
    )
    backpressure_max_mbar: Optional[float] = Field(
        None, ge=0,
        description="Maximaler zulässiger Gegendruck in mbar"
    )
    backpressure_acceptable: Optional[bool] = Field(
        None, description="Gegendruck innerhalb der Grenzen?"
    )

    # Gesamtergebnis
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Abgasanlage (0–100)"
    )
    overall_condition: ExhaustComponentCondition = Field(
        ..., description="Gesamt-Zustandsbewertung"
    )

    # Gewichtete Teilbewertungen
    sub_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (z.B. {'mixing_elbow': 45, 'waterlock': 85})"
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
    estimated_annual_maintenance_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte jährliche Wartungskosten"
    )
    estimated_5year_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte 5-Jahres-Kosten (Wartung + absehbarer Austausch)"
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
    limitations: list[str] = Field(
        default_factory=list,
        description="Einschränkungen der Analyse (z.B. 'Mischkrümmer-Innenzustand nicht beurteilbar')"
    )
```
