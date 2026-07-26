---
title: "Cam Cleats und Klemmen im Yachtbau"
kategorie: "11 Klampen Klemmen Schienensysteme"
unterkategorie: "02 Cam Cleats und Klemmen"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, SWL-Prüfungen, Laborwerte"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - cam_cleat
  - klemme
  - rope_clutch
  - fallenstopper
  - line_stopper
  - spinlock
  - clamcleat
  - harken
  - lewmar
  - antal
  - ronstan
  - deck_hardware
  - laufendes_gut
  - shorthanded_sailing
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 11.02 — Cam Cleats und Klemmen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 11.02** — Kategorie 11: Klampen, Klemmen, Schienensysteme
> **Confidence-Quelle:** measured (Hersteller-TDS, SWL-Prüfungen), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien](#4-produktlinien)
5. [Technische Spezifikationen](#5-technische-spezifikationen)
6. [Wartung und Service](#6-wartung-und-service)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ — Häufige Fragen](#10-faq--häufige-fragen)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudie: Cam Cleat Versagen bei Regatta](#anhang-a--fallstudie-cam-cleat-versagen-bei-regatta)
14. [ANHANG B — Fallstudie: Fallenstopper-Upgrade auf Blauwasseryacht](#anhang-b--fallstudie-fallenstopper-upgrade-auf-blauwasseryacht)
15. [ANHANG C — Fallstudie: Clutch-Bank Redesign auf Performance Cruiser](#anhang-c--fallstudie-clutch-bank-redesign-auf-performance-cruiser)
16. [ANHANG D — Fallstudie: Korrosion an Aluminium-Cam-Cleats](#anhang-d--fallstudie-korrosion-an-aluminium-cam-cleats)
17. [ANHANG E — Fallstudie: Line Stopper Nachrüstung Motoryacht](#anhang-e--fallstudie-line-stopper-nachrüstung-motoryacht)
18. [ANHANG F — Fallstudie: Spinlock XTS vs. Lewmar D2 Langzeittest](#anhang-f--fallstudie-spinlock-xts-vs-lewmar-d2-langzeittest)
19. [ANHANG G — Fallstudie: Clamcleat-Bruch bei Opti-Regatta](#anhang-g--fallstudie-clamcleat-bruch-bei-opti-regatta)
20. [ANHANG H — Fallstudie: Antal V-Grip Installation Superyacht](#anhang-h--fallstudie-antal-v-grip-installation-superyacht)
21. [ANHANG I — Confidence-Mapping](#anhang-i--confidence-mapping)
22. [ANHANG J — AYDI-Integration (Pydantic-Modelle)](#anhang-j--aydi-integration-pydantic-modelle)
23. [ANHANG K — AYDI Bewertungsschema für Cam Cleats und Klemmen](#anhang-k--aydi-bewertungsschema-für-cam-cleats-und-klemmen)
24. [ANHANG L — Preis-Kalkulator Cam Cleats und Klemmen](#anhang-l--preis-kalkulator-cam-cleats-und-klemmen)
25. [ANHANG M — Wartungsplanung Jahreskalender](#anhang-m--wartungsplanung-jahreskalender)
26. [ANHANG N — Hersteller-Kontakte und Bezugsquellen](#anhang-n--hersteller-kontakte-und-bezugsquellen)
27. [ANHANG O — Normen-Referenz](#anhang-o--normen-referenz)
28. [ANHANG P — Montageschablonen und Bohrbilder](#anhang-p--montageschablonen-und-bohrbilder)
29. [ANHANG Q — Leinentyp-Kompatibilitätsmatrix](#anhang-q--leinentyp-kompatibilitätsmatrix)
30. [ANHANG R — Weiterführende Ressourcen](#anhang-r--weiterführende-ressourcen)
31. [ANHANG S — Erweiterte technische Daten](#anhang-s--erweiterte-technische-daten)
32. [ANHANG T — Experten-Meinungen und Fachliteratur-Auszüge](#anhang-t--experten-meinungen-und-fachliteratur-auszüge)
33. [ANHANG U — Elektrische und hydraulische Clutch-Aktuatoren](#anhang-u--elektrische-und-hydraulische-clutch-aktuatoren)
34. [ANHANG V — Spezielle Anwendungsfälle](#anhang-v--spezielle-anwendungsfälle)

---

## 1. Einführung und Übersicht

### 1.1 Was sind Cam Cleats und Klemmen?

Im modernen Yachtbau gibt es drei grundlegend verschiedene Gerätefamilien zum Fixieren laufenden Guts (Fallen, Schoten, Strecker, Niederholer):

**Cam Cleats (Curry-Klemmen):**
Federbelastete Klemmen mit zwei gezahnten Backen, die eine Leine durch Keilwirkung halten. Die Leine wird von oben eingelegt und klemmt sofort. Zum Lösen wird die Leine nach oben aus den Backen gezogen. Cam Cleats sind die einfachste und schnellste Art der Leinenfixierung — ein Handgriff zum Belegen, ein Handgriff zum Lösen.

**Rope Clutches / Fallenstopper (Jammer):**
Mechanische Klemmen mit exzentrischem Nocken oder Klemmbacken, die eine Leine unter hoher Last halten können. Die Leine wird durch den geöffneten Clutch geführt und dann durch Schließen des Hebels fixiert. Rope Clutches sind für deutlich höhere Lasten ausgelegt als Cam Cleats und werden typischerweise für Fallen, Reffleinen und hochbelastete Strecker eingesetzt.

**Line Stoppers (Leinenstopper):**
Ältere Bauform, bei der ein Hebel- oder Nockenmechanismus die Leine gegen eine Grundplatte presst. Line Stoppers waren die Vorläufer moderner Rope Clutches und werden heute nur noch selten verbaut. Lewmar Superlock ist das bekannteste noch produzierte Modell.

### 1.2 Warum sind diese Beschläge essentiell?

Ohne Cam Cleats und Klemmen wäre Einhand- und Kurzhandsegeln unmöglich. Jede Leine müsste auf einer Klampe belegt werden — ein zeitaufwändiger Vorgang, der bei Manövern kritisch wird. Die Evolution vom belegen auf Klampen über Curry-Klemmen zu modernen Rope Clutches hat das Segeln fundamental verändert:

- **Reaktionszeit:** Cam Cleat: <1 Sekunde. Klampe: 3–5 Sekunden.
- **Einhandbedienung:** Clutch und Winch ermöglichen Einhandmanöver, die sonst zwei Personen erfordern.
- **Sicherheit:** Kontrolliertes Fieren unter Last ist mit Clutch + Winch möglich, mit Klampe nicht.
- **Cockpit-Layout:** Clutch-Bänke zentralisieren alle Fallenbedienung an einem Ort.

### 1.3 Abgrenzung der Gerätefamilien

| Merkmal | Cam Cleat | Rope Clutch | Line Stopper |
|---------|-----------|-------------|--------------|
| Typische Last (SWL) | 100–600 kg | 500–3.000 kg | 400–2.000 kg |
| Leinendurchmesser | 3–16 mm | 6–16 mm | 8–16 mm |
| Bedienung | Einlegen/Ausheben | Hebel öffnen/schließen | Hebel drücken/heben |
| Fieren unter Last | Nein (nur freigeben) | Ja (kontrolliert) | Bedingt |
| Typische Anwendung | Schoten, Strecker, Niederholer | Fallen, Reffleinen | Fallen (Altbestand) |
| Preisniveau | €15–€80 | €60–€350 | €40–€200 |
| Wartungsintervall | 1× jährlich | 1× jährlich | 2× jährlich |

### 1.4 Historische Entwicklung

Die erste Cam Cleat wurde in den 1960er Jahren von der australischen Firma Clamcleat entwickelt. Das Grundprinzip — zwei federbelastete, gezahnte Backen — hat sich seitdem nicht fundamental geändert, wohl aber die Materialien (von Zamak über Aluminium zu Verbundwerkstoffen) und die Ergonomie.

Rope Clutches revolutionierten das Cockpit-Layout in den 1980er Jahren. Spinlock (UK) und Lewmar (UK) waren die Pioniere. Die Idee: Alle Fallen werden von der Mastbasis ins Cockpit geführt und dort über Clutch-Bänke bedient. Das ermöglichte erstmals echtes Kurzhandsegeln auf Fahrtenyachten.

### 1.5 Relevanz für AYDI

Für die AYDI-Analyse sind Cam Cleats und Klemmen relevant in folgenden Modulen:

- **Ergonomie:** Erreichbarkeit, Bedienkräfte, Cockpit-Layout-Analyse
- **Produktion:** Montageaufwand, Verstärkungsanforderungen
- **Materialien:** Korrosionsbeständigkeit, UV-Alterung, Lebensdauer
- **Compliance:** Haltekraft vs. Linienbelastung, SWL-Einhaltung
- **Service Patterns:** Wartungsintervalle, typische Verschleißmuster
- **Kosten:** Beschaffung, Montage, Wartung über Lebenszyklus

---

## 2. Grundlagen und Theorie

### 2.1 Cam-Mechanismus (Federbelastete Backen)

#### 2.1.1 Funktionsprinzip

Der Cam-Cleat-Mechanismus basiert auf dem Keilprinzip. Zwei gezahnte Backen (Cams) sind auf einer gemeinsamen Achse gelagert und werden durch Federn zusammengedrückt. Wenn eine Leine zwischen die Backen eingelegt wird, drückt die Zugkraft die Backen aufgrund ihrer Geometrie weiter zusammen — je höher die Last, desto stärker die Klemmung.

**Geometrische Grundlagen:**

Die Backen haben eine exzentrische Form: Der Abstand vom Drehpunkt zur Klemmfläche nimmt in Zugrichtung zu. Dadurch entsteht ein selbstverstärkender Effekt:

```
Klemmkraft F_k = F_zug × tan(α) + F_feder

wobei:
  F_zug  = Zugkraft in der Leine [N]
  α      = Keilwinkel der Cam-Geometrie [°], typisch 12–18°
  F_feder = Federkraft im unbelasteten Zustand [N], typisch 5–15 N
```

#### 2.1.2 Zahnprofil und Grip

Die Zähne der Cam-Backen sind entscheidend für die Haltekraft. Es gibt drei grundlegende Zahnprofile:

**V-Zähne (Standard):**
- Dreieckiges Profil, symmetrisch
- Guter Grip bei allen Leinentypen
- Höherer Leinenverschleiß
- Standard bei Clamcleat, Ronstan

**Rund-Zähne (Leinenschonend):**
- Abgerundetes Profil
- Geringerer Leinenverschleiß
- Etwas weniger Grip bei nassen Leinen
- Standard bei Harken Carbo

**Mikro-Zähne (Hochleistung):**
- Feines Zahnprofil mit hoher Zahndichte
- Optimaler Grip bei Dyneema/Spectra
- Minimaler Leinenverschleiß
- Standard bei Racing-Modellen

#### 2.1.3 Federkennlinie

Die Federn in Cam Cleats müssen zwei widersprüchliche Anforderungen erfüllen:

1. **Ausreichend stark** für zuverlässiges Klemmen bei geringer Last
2. **Nicht zu stark** für leichtes Ausheben unter Last

Typische Federkennwerte:

| Klasse | Leinendurchmesser | Federkraft (Ruhe) | Federkraft (max) |
|--------|-------------------|-------------------|-------------------|
| Junior | 3–6 mm | 3–5 N | 8–12 N |
| Standard | 6–10 mm | 8–12 N | 18–25 N |
| Major | 8–14 mm | 12–18 N | 28–35 N |
| Mega | 10–16 mm | 15–22 N | 35–45 N |

#### 2.1.4 Materialien der Backen

**Aluminium (hart-eloxiert):**
- Standardmaterial für Marine-Cam-Cleats
- Hart-Eloxierung (Typ III, 25–50 µm) erhöht Verschleißfestigkeit
- Gewicht: mittel
- Lebensdauer: 8–15 Jahre bei Wartung

**Edelstahl 316L:**
- Höchste Korrosionsbeständigkeit
- Höchstes Gewicht
- Selten für komplette Backen, häufig für Achsen und Federn
- Lebensdauer: 15–25 Jahre

**Glasfaserverstärktes Nylon (GFK/PA):**
- Leichtestes Material
- Keine Korrosion
- Geringere Haltekraft als Metall
- Lebensdauer: 5–10 Jahre (UV-abhängig)

**Acetal/POM (Delrin):**
- Selbstschmierend
- Gute Verschleißfestigkeit
- Keine Korrosion
- Standard bei Clamcleat Composite-Serie

**Carbon-Composite:**
- Höchste Festigkeit bei geringstem Gewicht
- Teuerste Option
- Nur bei Racing-Modellen (Harken Carbo)

### 2.2 Rope-Clutch-Mechanismus (Exzentrischer Nocken)

#### 2.2.1 Funktionsprinzip

Im Gegensatz zum Cam Cleat arbeitet ein Rope Clutch mit einem einzelnen exzentrischen Nocken (Cam), der durch einen Hebel betätigt wird. Beim Schließen des Hebels drückt der Nocken die Leine gegen die geriffelte Grundplatte und erzeugt Klemmung durch Reibung.

**Mechanische Grundlagen:**

```
Haltekraft F_h = µ × F_n × A_kontakt / A_leine

wobei:
  µ         = Reibungskoeffizient Nocken/Leine, typisch 0.3–0.6
  F_n       = Normalkraft durch Hebelmechanismus [N]
  A_kontakt = Kontaktfläche zwischen Nocken und Leine [mm²]
  A_leine   = Querschnittsfläche der Leine [mm²]
```

#### 2.2.2 Exzentrizität und Übersetzung

Die Exzentrizität des Nockens bestimmt das Verhältnis zwischen Handkraft am Hebel und Klemmkraft auf der Leine. Moderne Clutches haben typisch ein Übersetzungsverhältnis von 5:1 bis 10:1.

**Spinlock-Prinzip (konvexer Nocken):**
Der Nocken rollt über die Leine und erzeugt gleichmäßigen Druck über die gesamte Kontaktlänge. Dies schont die Leine und verteilt die Klemmkraft.

**Lewmar-Prinzip (konkaver Nocken):**
Der Nocken greift in die Leine ein und erzeugt eine formschlüssige Verbindung. Dies ergibt höhere Haltekraft pro Gewichtseinheit, aber potenziell mehr Leinenverschleiß.

**Antal V-Grip-Prinzip (V-förmiger Nocken):**
Patentiertes System mit V-förmigem Klemmprofil, das die Leine in eine Rinne presst. Sehr hohe Haltekraft, sehr geringer Leinenverschleiß.

#### 2.2.3 Fieren unter Last

Ein wesentlicher Vorteil von Rope Clutches gegenüber Cam Cleats ist die Möglichkeit, eine Leine unter Last kontrolliert zu fieren. Dies geschieht durch teilweises Öffnen des Hebels:

**Kontrolliertes Fieren (moderner Clutch):**
1. Leine auf Winch belegen (2–3 Törns)
2. Clutch-Hebel langsam öffnen
3. Leine rutscht kontrolliert durch den Clutch
4. Winch als Bremse nutzen

**Achtung: Fieren ohne Winch ist gefährlich!**
Bei hohen Lasten (>200 kg) kann die Leine beim Öffnen des Clutches unkontrolliert durchschießen. Die Leine muss IMMER auf der Winch gesichert sein, bevor der Clutch geöffnet wird.

#### 2.2.4 Release-Under-Load-Charakteristik

Die Release-Under-Load-Kraft ist die Kraft, die am Hebel aufgebracht werden muss, um den Clutch unter Last zu öffnen. Sie ist ein kritischer Designparameter:

| Clutch-Typ | Release bei 50% SWL | Release bei 100% SWL |
|------------|---------------------|----------------------|
| Spinlock XAS | 8–12 N | 15–25 N |
| Spinlock XTS | 10–15 N | 20–30 N |
| Lewmar D2 | 12–18 N | 25–35 N |
| Antal V-Grip | 6–10 N | 12–20 N |

Niedrigere Release-Kräfte sind wünschenswert für Einhandsegeln und bei Crewmitgliedern mit geringerer Handkraft. Der Antal V-Grip zeichnet sich hier besonders aus.

### 2.3 Haltekraft-Berechnungen

#### 2.3.1 Safe Working Load (SWL) vs. Breaking Load (BL)

Im Marinebeschlagbereich gilt standardmäßig:

```
SWL = BL / Sicherheitsfaktor

Sicherheitsfaktor:
  - Cam Cleats: 3:1 (Standard), 4:1 (Racing)
  - Rope Clutches: 3:1 (Fahrt), 2.5:1 (Racing)
  - Line Stoppers: 3:1 (Standard)
```

#### 2.3.2 Leinenbelastung nach Anwendung

Für die korrekte Dimensionierung von Cam Cleats und Klemmen muss die erwartete Leinenbelastung bekannt sein:

| Anwendung | Bootslänge 8m | 10m | 12m | 14m | 16m |
|-----------|---------------|-----|-----|-----|-----|
| Großfall | 150–300 kg | 250–500 kg | 400–800 kg | 600–1.200 kg | 800–1.800 kg |
| Genua-Fall | 100–250 kg | 200–400 kg | 350–700 kg | 500–1.000 kg | 700–1.500 kg |
| Spi-Fall | 80–200 kg | 150–350 kg | 300–600 kg | 450–900 kg | 600–1.200 kg |
| Großschot | 50–150 kg | 100–300 kg | 200–500 kg | 350–700 kg | 500–1.000 kg |
| Reff-Leine | 80–200 kg | 150–350 kg | 300–600 kg | 450–900 kg | 600–1.200 kg |
| Cunningham | 30–80 kg | 60–150 kg | 100–250 kg | 180–350 kg | 250–500 kg |
| Baumniederholer | 40–100 kg | 80–200 kg | 150–350 kg | 250–500 kg | 350–700 kg |
| Genuaschot | 80–200 kg | 150–350 kg | 300–600 kg | 450–900 kg | 600–1.200 kg |

**Confidence:** estimated — Werte variieren erheblich je nach Segelschnitt, Rigg-Typ, Windstärke und Seegang.

#### 2.3.3 Dimensionierungsregel

Als Faustregel gilt:

```
SWL_clutch ≥ 1.5 × F_max_erwartet

wobei F_max_erwartet die maximale erwartete Leinenbelastung
unter den schlimmsten planbaren Bedingungen ist.
```

Der Faktor 1.5 berücksichtigt:
- Dynamische Lastspitzen (Böen, Wellen)
- Alterungsbedingten Haltekraftverlust
- Verschmutzung und Salzablagerungen

### 2.4 Leinendurchmesser-Kompatibilität

#### 2.4.1 Optimaler Bereich

Jeder Cam Cleat und Rope Clutch hat einen definierten Leinendurchmesser-Bereich. Die Haltekraft ist nur innerhalb dieses Bereichs garantiert:

**Zu dünne Leine:** Die Leine sitzt zu tief zwischen den Backen/im Nocken. Die Kontaktfläche ist zu gering. Folgen:
- Reduzierte Haltekraft (bis zu 50% Verlust)
- Erhöhter Leinenverschleiß (Punktbelastung)
- Leine kann durch den Clutch rutschen

**Zu dicke Leine:** Die Leine passt nicht vollständig in den Klemmbereich. Folgen:
- Clutch schließt nicht vollständig
- Leine kann nicht korrekt geklemmt werden
- Erhöhte Bedienkraft
- Beschädigung des Clutch-Mechanismus

#### 2.4.2 Leinentyp und Grip

Verschiedene Leinenmaterialien haben unterschiedliche Grip-Eigenschaften in Klemmen:

| Leinentyp | Grip in Cam Cleat | Grip in Clutch | Verschleiß |
|-----------|-------------------|----------------|-------------|
| Polyester (Dacron) | Sehr gut | Sehr gut | Gering |
| Dyneema/Spectra (Kern) | Gut | Gut | Gering |
| Dyneema (Mantel dünn) | Mittel | Mittel | Mittel |
| Dynema (cover-less) | Schlecht | Schlecht | Hoch |
| Kevlar/Aramid | Gut | Gut | Hoch (Knicke) |
| Vectran | Gut | Gut | Mittel |
| Polypropylen | Schlecht | Schlecht | Hoch |
| Nylon (PA) | Sehr gut | Sehr gut | Mittel |

**Wichtig:** Mantelllose Dyneema-Leinen (z.B. Dyneema SK78 ohne Mantel) sind für Cam Cleats und viele Clutches NICHT geeignet. Der glatte, wachsartige Kern bietet zu wenig Reibung. Mindestens ein dünner Polyester-Mantel ist erforderlich.

### 2.5 Fairlead-Winkel und Leinenführung

#### 2.5.1 Einlaufwinkel

Der Winkel, unter dem die Leine in den Cam Cleat oder Clutch einläuft, ist kritisch für die Funktion:

**Cam Cleat:**
- Optimaler Einlaufwinkel: 0–15° zur Horizontalen
- Maximaler Einlaufwinkel: 30°
- Bei steileren Winkeln: Leine springt aus den Backen

**Rope Clutch:**
- Optimaler Einlaufwinkel: 5–12° Aufwärtswinkel von der Einlaufseite
- Minimaler Aufwärtswinkel: 3° (sonst rutscht die Leine beim Fieren)
- Maximaler Aufwärtswinkel: 20° (sonst zu hohe Bedienkraft)

#### 2.5.2 Seitliche Ablenkung

**Cam Cleat:**
- Maximale seitliche Ablenkung: ±5° (bei Schwenkfuß: ±30°)
- Seitliche Ablenkung reduziert die Haltekraft um ca. 10% pro 5°

**Rope Clutch:**
- Maximale seitliche Ablenkung: ±5° (Leinenschäden bei mehr)
- Fairleads oder Umlenkrollen VOR dem Clutch sind bei seitlicher Anströmung zwingend

#### 2.5.3 Abstand Clutch — Winch

Der Abstand zwischen Clutch und zugehöriger Winch bestimmt die Bedienbarkeit:

```
Optimaler Abstand: 300–500 mm (Einhandbedienung möglich)
Minimaler Abstand: 200 mm (sonst Interferenz beim Winchen)
Maximaler Abstand: 800 mm (sonst zu viel lose Leine zwischen Clutch und Winch)
```

### 2.6 Kraftfluss und Decksverstärkung

#### 2.6.1 Lasteinleitung

Cam Cleats und Rope Clutches leiten erhebliche Kräfte in das Deck ein. Die Befestigungspunkte müssen entsprechend verstärkt sein:

**Cam Cleat (SWL 200 kg):**
- Ausziehkraft pro Schraube: 50 kg (bei 4 Schrauben)
- Mindest-Decksstärke: 10 mm GFK-Sandwich
- Verstärkung: Backing Plate empfohlen

**Rope Clutch (SWL 1.000 kg):**
- Ausziehkraft pro Schraube: 150–250 kg (bei 4–6 Schrauben)
- Mindest-Decksstärke: 15 mm GFK-Sandwich
- Verstärkung: Backing Plate (Edelstahl 3 mm oder Aluminium 5 mm) ZWINGEND
- Kernkompression bei Sandwich-Laminat vermeiden

#### 2.6.2 Backing-Plate-Dimensionierung

```
A_backing ≥ 2.5 × A_beschlag

Dicke Backing Plate:
  - Aluminium: ≥ 5 mm (bis SWL 500 kg), ≥ 8 mm (bis SWL 1.500 kg)
  - Edelstahl 316L: ≥ 3 mm (bis SWL 500 kg), ≥ 5 mm (bis SWL 1.500 kg)
  - GFK-Laminat: ≥ 8 mm (bis SWL 500 kg), ≥ 12 mm (bis SWL 1.500 kg)
```

---

## 3. Typenübersicht

### 3.1 Cam Cleats (Curry-Klemmen)

#### 3.1.1 Feste Cam Cleats (Fixed Base)

Die einfachste Bauform: Zwei federbelastete Backen auf einer festen Grundplatte. Die Leinenrichtung ist durch die Montageausrichtung festgelegt.

**Einsatzbereich:**
- Jollen (Cunningham, Baumniederholer, Traveller-Schot)
- Fahrtenyachten (Reacher-/Gennaker-Schot, Strecker)
- Katamarane (Traveller-Schot, Trapezdraht-Klemme)

**Typische Modelle:**
- Clamcleat CL205 (Junior, 3–6 mm)
- Clamcleat CL211 Mk2 (Standard, 6–10 mm)
- Clamcleat CL217 Mk2 (Major, 8–14 mm)
- Harken 150 Micro Cam Cleat (3–6 mm)
- Harken 468 Carbo Cam Cleat (6–10 mm)
- Ronstan RF5001 (3–6 mm)
- Ronstan RF5010 (6–10 mm)

**Vorteile:**
- Einfach, robust, wartungsarm
- Geringes Gewicht
- Günstig

**Nachteile:**
- Keine seitliche Anpassung
- Einlaufwinkel muss bei Montage stimmen

#### 3.1.2 Schwenkfuß-Cam-Cleats (Swivel Base)

Cam Cleat auf einer drehbaren Grundplatte, die sich automatisch zur Leinenrichtung ausrichtet. Besonders wichtig für Anwendungen, bei denen die Leinenrichtung variiert.

**Einsatzbereich:**
- Hauptschot auf Dinghys und kleinen Kielbooten
- Genua-Schot als Zwischenlösung
- Fock-Schot auf Jollen
- Traveller-Schot bei wechselnden Winkeln

**Typische Modelle:**
- Clamcleat CL253 (mit 360° Schwenk, 6–10 mm)
- Harken 241 Cam Cleat mit Pivot Base
- Ronstan RF5020 Swivel Cam Cleat
- Clamcleat CL257 (mit Fairlead und Schwenk)

**Vorteile:**
- Automatische Ausrichtung zur Leinenrichtung
- Tolerant gegenüber wechselnden Einlaufwinkeln
- Einfache Bedienung

**Nachteile:**
- Komplexerer Mechanismus
- Schwenkpunkt als potenzielle Schwachstelle
- Höheres Gewicht als feste Cam Cleats

#### 3.1.3 Cam Cleats mit integriertem Fairlead

Cam Cleat mit vorgeschaltetem Leinenführer, der den korrekten Einlaufwinkel sicherstellt. Die Leine wird durch den Fairlead geführt, bevor sie in die Backen eintritt.

**Einsatzbereich:**
- Anwendungen mit ungünstigem natürlichen Einlaufwinkel
- Montage auf vertikalen oder schrägen Flächen
- Rennboote (konsistenter Grip unabhängig von Körperposition)

**Typische Modelle:**
- Clamcleat CL211/S2 (mit Leitöse, Seiteneinführung)
- Clamcleat CL236 (mit vertikalem Fairlead)
- Harken 471 Carbo Cam mit Lead
- Ronstan RF5015 mit Fairlead Kit

**Vorteile:**
- Immer korrekter Einlaufwinkel
- Höhere Haltekraft durch optimierte Leinenführung
- Sauberere Installation

**Nachteile:**
- Höherer Platzbedarf
- Etwas teurer
- Leine fädelt sich nicht so schnell ein

#### 3.1.4 Racing Cam Cleats

Speziell für den Regattaeinsatz optimierte Cam Cleats mit Fokus auf minimales Gewicht, maximale Haltekraft und schnellstes Ausheben.

**Typische Modelle:**
- Harken 150 Micro (3–6 mm, 29g)
- Harken 365 Carbo (6–10 mm, 45g)
- Harken 468 Carbo Cam (6–10 mm, Carbon-Composite)
- Ronstan RF5400 C-Cleat (Aluminium, 22g)
- Clamcleat CL205AN (Aluminium, eloxiert, Junior Racing)

**Besonderheiten Racing:**
- Minimales Gewicht (jedes Gramm zählt auf Performance-Jollen)
- Mikro-Zahnprofil für Dyneema-Grip
- Titanschrauben verfügbar
- Grösse angepasst für dünne High-Performance-Leinen (2–4 mm Dyneema)

#### 3.1.5 Sonder-Cam-Cleats

**Trapez-Klemme (Clamcleat CL253):**
Speziell für Trapez-Einhakleine. Große, abgerundete Backen für schnelles Ein- und Ausklinken mit einer Hand bei Vollbelastung.

**Alu-Rail Cam Cleat (Clamcleat CL223):**
Cam Cleat mit T-Schienen-Fuß für Montage auf Lewmar/Harken T-Schienen. Positionierbar ohne Bohren.

**Mast-Cam-Cleat:**
Speziell für Mastmontage, seitliche Leineneinführung. Für Luv-/Lee-Flaggfall, Topping-Lift, Lazy Jacks.

### 3.2 Rope Clutches / Fallenstopper (Jammer)

#### 3.2.1 Standard-Clutches (Einhebel)

Ein einzelner Klemmhebel pro Leinenposition. Die Standardbauform für Fahrtenyachten und die meisten Regattayachten.

**Bauformen:**

**Obere Klemmung (Top-Loading):**
- Leine wird von oben in den geöffneten Clutch eingelegt
- Standard bei Spinlock, Lewmar, Antal
- Einfaches Handling
- Leine kann unter Last eingefangen werden (Vorsicht!)

**Seitliche Klemmung (Side-Loading):**
- Leine wird von der Seite eingeführt
- Seltener, hauptsächlich bei älteren Modellen
- Vorteil: Leine kann nicht unbeabsichtigt einrasten

#### 3.2.2 Spinlock-Serien im Überblick

Spinlock (Cowes, Isle of Wight, UK) ist der Marktführer bei Rope Clutches. Das Sortiment umfasst fünf Serien:

**XA-Serie (Einstieg):**
- Einfacher, kostengünstiger Clutch
- Aluminium-Gehäuse, Acetal-Nocken
- Für Fahrtenyachten und leichte Lasten
- Größen: 6–12 mm

**XAS-Serie (Standard):**
- Meistverkaufte Clutch-Serie weltweit
- Aluminium-Gehäuse, verstärkter Nocken
- Fairlead integriert (seitlich einstellbar)
- Größen: 6–14 mm in Doppel- und Dreifach-Bänken

**XCS-Serie (Cruising):**
- Ergonomisch optimiert für Fahrt
- Größerer Hebel, leichtere Bedienung
- Integrierter Fairlead mit weiter Öffnung
- Farbcodierte Hebel verfügbar
- Größen: 6–14 mm

**XTS-Serie (Performance):**
- Höchste Haltekraft im Programm
- Optimiert für minimale Bedienkraft
- Carbon-Hebel-Option
- Asymmetrische Öffnung für schnelles Fieren
- Größen: 6–14 mm

**XX-Serie (Extreme):**
- Superyacht-/Maxiyacht-Serie
- SWL bis 3.000 kg
- Vollständig in Edelstahl 316L
- Größen: 8–16 mm

#### 3.2.3 Lewmar D-Series

Lewmar (Havant, UK) ist der zweitgrößte Anbieter von Rope Clutches weltweit.

**D1-Serie (Einstieg/Sport):**
- Kompakte Bauform
- Kunststoff-Gehäuse mit Edelstahl-Mechanik
- Einzeln oder als Bank (2er, 3er)
- Größen: 6–12 mm

**D2-Serie (Standard):**
- Meistverkaufte Lewmar-Clutch-Serie
- Aluminium-Gehäuse, eloxiert
- Bewährte Zuverlässigkeit
- Größen: 8–14 mm in 2er, 3er, 4er Bänken

**D3-Serie (Heavy Duty):**
- Für Yachten >14 m
- Verstärktes Gehäuse
- Höhere SWL
- Größen: 10–16 mm

#### 3.2.4 Antal V-Grip

Antal (Treviso, Italien) hat mit dem patentierten V-Grip-System einen innovativen Clutch entwickelt, der besonders bei italienischen und französischen Werften beliebt ist.

**V-Grip Merkmale:**
- V-förmiges Klemmprofil: Leine wird in V-Rinne gedrückt
- Extrem geringe Release-Kraft (ca. 40% weniger als Wettbewerb)
- Sehr geringer Leinenverschleiß
- Integrierter Fairlead
- Aluminium-Gehäuse, Edelstahl-Mechanik

**V-Grip Größen:**
- V-Grip 8: 6–8 mm
- V-Grip 10: 8–10 mm
- V-Grip 12: 10–12 mm
- V-Grip 14: 12–14 mm

#### 3.2.5 Harken Lock-In

Harken (Pewaukee, Wisconsin, USA) bietet Clutches unter dem Namen "Lock-In" an:

**Lock-In Winch Handles:**
Harkens Clutch-System ist eng mit der Winch-Linie integriert. Die Lock-In Clutches sind für die Montage direkt vor Harken-Winschen optimiert.

**Midrange Clutch:**
- Einstiegsserie
- Kunststoff/Aluminium-Hybrid
- Einzeln montierbar
- Größen: 6–12 mm

**ESP (Easy Swivel Plate) Cam Cleat:**
- Nicht zu verwechseln mit einem echten Clutch
- Schwenk-Cam-Cleat für mittlere Lasten
- Für Schoten und leichte Strecker

### 3.3 Line Stoppers (Leinenstopper)

#### 3.3.1 Lewmar Superlock

Der Lewmar Superlock ist der letzte noch weitverbreitete klassische Line Stopper. Er arbeitet mit einem Hebelmechanismus, der die Leine gegen eine geriffelte Grundplatte presst.

**Merkmale:**
- Robuster Gussmechanismus
- Sehr hohe Haltekraft
- Schwieriger zu öffnen unter Last als moderne Clutches
- Kein kontrolliertes Fieren möglich
- Wird als Ersatz für bestehende Installationen noch produziert

**Größen:**
- Superlock I: 6–10 mm
- Superlock II: 8–12 mm
- Superlock III: 10–14 mm

#### 3.3.2 Legacy Cam-Action Stoppers

Ältere Modelle von Schaefer, Nicro-Fico, und anderen Herstellern, die seit den 1980er Jahren nicht mehr produziert werden. Kennzeichen:
- Massive Guss- oder Schmiede-Konstruktion
- Einfacher Hebel-Nocken-Mechanismus
- Hohes Gewicht
- Schwer unter Last zu öffnen
- Ersatzteile nur noch gebraucht verfügbar

### 3.4 Clutch-Bänke (Multi-Position)

#### 3.4.1 Konzept

Clutch-Bänke fassen mehrere Clutches auf einer gemeinsamen Grundplatte zusammen. Sie sind der Standard für die Cockpit-Fallenbedienung auf modernen Fahrtenyachten.

**Typische Konfigurationen:**

**Backbord-Bank (3er oder 4er):**
1. Großfall
2. Reff 1
3. Reff 2
4. (Optional: Reff 3 oder Topping Lift)

**Steuerbord-Bank (3er oder 4er):**
1. Genua-/Fock-Fall
2. Spinnaker-Fall
3. Cunningham oder Achterstag-Strecker
4. (Optional: Code-0-Fall oder Reserve)

#### 3.4.2 Verfügbare Bank-Konfigurationen

| Hersteller | Modell | Positionen | Leinendurchmesser | Preis (ca.) |
|------------|--------|------------|-------------------|-------------|
| Spinlock | XAS 2-fach | 2 | 6–14 mm | €140–€280 |
| Spinlock | XAS 3-fach | 3 | 6–14 mm | €200–€400 |
| Spinlock | XAS 4-fach | 4 | 6–14 mm | €270–€520 |
| Spinlock | XAS 6-fach | 6 | 6–14 mm | €400–€750 |
| Lewmar | D2 2-fach | 2 | 8–14 mm | €130–€260 |
| Lewmar | D2 3-fach | 3 | 8–14 mm | €180–€370 |
| Antal | V-Grip 2-fach | 2 | 6–14 mm | €160–€310 |
| Antal | V-Grip 3-fach | 3 | 6–14 mm | €230–€450 |
| Antal | V-Grip 4-fach | 4 | 6–14 mm | €300–€580 |

#### 3.4.3 Montage-Orientierung

**Horizontal (Deck-Montage):**
- Standard auf den meisten Yachten
- Clutch-Hebel zeigen nach oben
- Leinen laufen horizontal über das Deck
- Erfordert ausreichend Decksfläche

**Vertikal (Schott-Montage):**
- Auf Rennbooten und kleineren Yachten
- Clutch-Hebel zeigen nach vorne/achtern
- Platzsparend
- Nur mit bestimmten Modellen möglich (Spinlock XTS, Antal V-Grip)

**Geneigt (15–30°):**
- Kompromiss zwischen horizontal und vertikal
- Ergonomisch oft optimal
- Erfordert Unterlegkeile oder spezielle Montageplatten

---

## 4. Produktlinien

### 4.1 Spinlock (Cowes, Isle of Wight, UK)

#### 4.1.1 Firmengeschichte

Spinlock wurde 1982 von Chris Mayall auf der Isle of Wight gegründet. Das Unternehmen spezialisierte sich von Anfang an auf Decksbeschläge und wurde schnell zum Marktführer bei Rope Clutches. Heute beschäftigt Spinlock ca. 100 Mitarbeiter und produziert ausschließlich in Cowes.

#### 4.1.2 XA-Serie (Entry Level)

Die XA-Serie ist Spinlocks Einstiegsserie für Fahrtensegler und Jollensegler.

| Modell | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|------------|----------|---------|-------------|-----------|
| XA0612/1 (Einzel) | 6–12 | 500 | 1.500 | 105 | 55–70 |
| XA0612/2 (Doppel) | 6–12 | 500 | 1.500 | 200 | 100–130 |
| XA0612/3 (Dreifach) | 6–12 | 500 | 1.500 | 295 | 145–185 |

**Merkmale XA:**
- Aluminium-Gehäuse, hart-eloxiert (schwarz)
- Acetal-Nocken (selbstschmierend)
- Edelstahl-Achse und -Feder
- Integrierter Fairlead (fest)
- Montage: 2 Schrauben M5 pro Position
- Backing Plate empfohlen ab SWL 300 kg

#### 4.1.3 XAS-Serie (Standard)

Die XAS-Serie ist der weltweite Bestseller unter den Rope Clutches. Sie bietet das beste Preis-Leistungs-Verhältnis und wird auf Zehntausenden von Yachten eingesetzt.

| Modell | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|------------|----------|---------|-------------|-----------|
| XAS0612/1 | 6–12 | 700 | 2.100 | 125 | 70–90 |
| XAS0612/2 | 6–12 | 700 | 2.100 | 240 | 130–170 |
| XAS0612/3 | 6–12 | 700 | 2.100 | 355 | 190–240 |
| XAS0614/1 | 6–14 | 800 | 2.400 | 145 | 85–110 |
| XAS0614/2 | 6–14 | 800 | 2.400 | 280 | 160–200 |
| XAS0614/3 | 6–14 | 800 | 2.400 | 415 | 230–290 |
| XAS0614/4 | 6–14 | 800 | 2.400 | 550 | 300–380 |
| XAS0614/6 | 6–14 | 800 | 2.400 | 820 | 440–560 |

**Merkmale XAS:**
- Aluminium-Gehäuse, hart-eloxiert (schwarz oder silber)
- Verstärkter Nocken mit optimiertem Profil
- Edelstahl-Achse 316L und Edelstahl-Feder
- Seitlich einstellbarer Fairlead
- Montage: 2 Schrauben M6 pro Position
- Backing Plate ZWINGEND

**Besondere Features:**
- Seitenführung verhindert Leinenschlag
- Ergonomischer Hebel mit guter Griffigkeit
- Farbcodierung der Hebel optional (Rot, Blau, Gelb, Grün, Grau)
- XAS-Retrofit-Kit für ältere Spinlock-Modelle verfügbar

#### 4.1.4 XCS-Serie (Cruising)

Die XCS-Serie ist speziell für den Fahrtensegler optimiert. Größere Hebel, leichtere Bedienung, robustere Konstruktion.

| Modell | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|------------|----------|---------|-------------|-----------|
| XCS0612/1 | 6–12 | 800 | 2.400 | 160 | 95–120 |
| XCS0612/2 | 6–12 | 800 | 2.400 | 310 | 180–230 |
| XCS0612/3 | 6–12 | 800 | 2.400 | 460 | 260–330 |
| XCS0614/1 | 6–14 | 1.000 | 3.000 | 185 | 110–140 |
| XCS0614/2 | 6–14 | 1.000 | 3.000 | 360 | 210–270 |
| XCS0614/3 | 6–14 | 1.000 | 3.000 | 535 | 310–390 |
| XCS0814/1 | 8–14 | 1.200 | 3.600 | 210 | 130–165 |

**Merkmale XCS:**
- Aluminium-Gehäuse, hart-eloxiert
- Übergroßer Hebel für Einhandbedienung
- Weite Fairlead-Öffnung (leichtes Einfädeln)
- Integrierter Leinen-Stopper bei geschlossenem Hebel
- Anti-Snag-Design (keine vorstehenden Teile)
- Montage: 2–3 Schrauben M6 pro Position

#### 4.1.5 XTS-Serie (Performance)

Die XTS-Serie ist Spinlocks Hochleistungsserie für Regatta- und Performance-Cruising-Yachten.

| Modell | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|------------|----------|---------|-------------|-----------|
| XTS0612/1 | 6–12 | 900 | 2.700 | 130 | 120–155 |
| XTS0612/2 | 6–12 | 900 | 2.700 | 250 | 230–295 |
| XTS0612/3 | 6–12 | 900 | 2.700 | 370 | 340–430 |
| XTS0614/1 | 6–14 | 1.100 | 3.300 | 155 | 140–180 |
| XTS0614/2 | 6–14 | 1.100 | 3.300 | 300 | 270–345 |
| XTS0614/3 | 6–14 | 1.100 | 3.300 | 445 | 395–500 |
| XTS0816/1 | 8–16 | 1.500 | 4.500 | 200 | 180–230 |

**Merkmale XTS:**
- Aluminium-Gehäuse, hart-eloxiert (schwarz)
- Optimierter Nocken für minimale Bedienkraft
- Asymmetrische Hebel-Geometrie (schnelles Öffnen, kontrolliertes Schließen)
- Carbon-Hebel-Option (Gewichtsersparnis ca. 30%)
- Geringster Leinenverschleiß aller Spinlock-Serien
- Für vertikale und geneigte Montage geeignet

#### 4.1.6 XX-Serie (Extreme / Superyacht)

Die XX-Serie ist für Superyachten und Maxi-Rennboote konzipiert.

| Modell | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|------------|----------|---------|-------------|-----------|
| XX0814/1 | 8–14 | 2.000 | 6.000 | 450 | 280–350 |
| XX1016/1 | 10–16 | 2.500 | 7.500 | 580 | 340–430 |
| XX1218/1 | 12–18 | 3.000 | 9.000 | 720 | 410–520 |

**Merkmale XX:**
- Vollständig aus Edelstahl 316L gefertigt
- Poliertes oder matt gebürstetes Finish
- Integrierte Decksverstärkung
- Für höchste Dauerlasten ausgelegt
- Wartungsintervall: 500 Betriebsstunden oder 1× jährlich

#### 4.1.7 Spinlock Ersatzteile und Zubehör

| Artikel | Teilenummer | Preis (€) |
|---------|-------------|-----------|
| Nocken-Kit XAS (1 Paar) | SP-XAS-CAM | 18–25 |
| Feder-Kit XAS (2 Stück) | SP-XAS-SPR | 8–12 |
| Hebel XAS (1 Stück) | SP-XAS-LEV | 12–18 |
| Fairlead XAS (1 Stück) | SP-XAS-FL | 10–15 |
| Nocken-Kit XTS (1 Paar) | SP-XTS-CAM | 25–35 |
| Carbon-Hebel XTS (1 Stück) | SP-XTS-CLEV | 35–50 |
| Schrauben-Kit M6 (4 Stück) | SP-FIX-M6 | 5–8 |
| Backing Plate (Standard) | SP-BP-STD | 15–25 |

### 4.2 Clamcleat (Bexhill-on-Sea, UK)

#### 4.2.1 Firmengeschichte

Clamcleat wurde 1958 in Australien von Allen Brothers gegründet und ist heute in Bexhill-on-Sea, East Sussex, UK ansässig. Das Unternehmen hat die Cam Cleat erfunden und produziert die weltweit breiteste Palette von Cam Cleats in verschiedenen Materialien und Größen.

#### 4.2.2 Aluminium-Serie (CL200er)

Die Aluminium-Serie ist Clamcleats Kernprodukt. Hart-eloxiertes Aluminium bietet hohe Haltekraft und lange Lebensdauer.

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| CL205 | Junior, fest | 3–6 | 100 | 22 | 12–18 |
| CL205AN | Junior, eloxiert | 3–6 | 100 | 22 | 14–20 |
| CL207 | Junior, seitlich | 3–6 | 100 | 28 | 15–22 |
| CL211 Mk2 | Standard, fest | 6–10 | 200 | 48 | 18–26 |
| CL211 Mk2 AN | Standard, eloxiert | 6–10 | 200 | 48 | 20–28 |
| CL213 Mk2 | Standard, seitlich | 6–10 | 200 | 55 | 22–30 |
| CL217 Mk2 | Major, fest | 8–14 | 400 | 85 | 28–38 |
| CL217 Mk2 AN | Major, eloxiert | 8–14 | 400 | 85 | 32–42 |
| CL218 | Mega, fest | 10–16 | 600 | 130 | 42–55 |
| CL219 | Major, mit Leitöse | 8–14 | 400 | 110 | 35–48 |
| CL222 | Racing Alu | 6–10 | 250 | 40 | 25–34 |
| CL223 | Rail-Mount (T-Schiene) | 6–10 | 200 | 65 | 30–42 |
| CL230 | Trapez-Klemme | 5–8 | 150 | 45 | 22–30 |
| CL236 | Mit vertikalem Fairlead | 6–10 | 200 | 60 | 25–35 |
| CL241 | Mk2 Junior mit Schwenk | 3–6 | 100 | 35 | 18–26 |
| CL253 | Schwenk 360° | 6–10 | 200 | 68 | 28–38 |
| CL254 | Schwenk mit Leitöse | 6–10 | 200 | 78 | 32–42 |
| CL257 | Schwenk mit Fairlead | 8–12 | 300 | 95 | 38–50 |

> ⚠️ **ZU PRÜFEN (Audit):** Modell **CL253** wird im Dokument widersprüchlich geführt — hier (Tabelle), in Abschnitt 3.1.2 und in den Zuordnungstabellen (Abschnitt 7) als "Schwenk 360°" Cam Cleat (6–10 mm), in Abschnitt 3.1.5 dagegen als "Trapez-Klemme". Laut Hersteller (clamcleat.com) ist CL253 der **Trapeze & Vang Cleat für 4–8 mm Leine**, kein 360°-Schwenkfuß-Cam-Cleat. Typ, Leinenbereich (6–10 mm vs. 4–8 mm) und die durchgängige Verwendung als Traveller-Schwenkklemme sind unverifiziert. Confidence hier auf estimated (unverifiziert) zurückgestuft.

#### 4.2.3 Composite-Serie (CL800er)

Clamcleats Composite-Serie verwendet glasfaserverstärktes Nylon. Leichter und günstiger als Aluminium, aber etwas geringere Haltekraft.

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| CL800 | Junior, Composite | 3–6 | 60 | 12 | 6–10 |
| CL802 | Junior, seitlich | 3–6 | 60 | 15 | 8–12 |
| CL814 | Standard, Composite | 6–10 | 120 | 28 | 10–16 |
| CL815 | Standard, seitlich | 6–10 | 120 | 32 | 12–18 |
| CL826 | Major, Composite | 8–14 | 250 | 55 | 16–24 |

#### 4.2.4 Edelstahl-Serie (CL700er)

Für marine Hochlast-Anwendungen in Edelstahl 316 gefertigt.

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| CL711 | Standard, Edelstahl | 6–10 | 300 | 95 | 45–60 |
| CL717 | Major, Edelstahl | 8–14 | 500 | 150 | 65–85 |

#### 4.2.5 Spezial-Serien

**Roller-Fairlead-Serie (CL240er):**
Cam Cleats mit vorgeschalteten Rollenumlenkungen für minimalen Leinenverschleiß.

| Modell | Typ | Leine (mm) | Preis (€) |
|--------|-----|------------|-----------|
| CL243 | Roller Fairlead + Junior Cam | 3–6 | 22–30 |
| CL244 | Roller Fairlead + Standard Cam | 6–10 | 28–38 |

**Draht-/Stahlseil-Klemmen (CL260er):**
Speziell für Stahlseile und beschichtete Drähte.

| Modell | Typ | Draht (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| CL260 | Drahtklemme | 3–5 | 200 | 22–30 |
| CL263 | Drahtklemme Major | 5–8 | 350 | 30–42 |

### 4.3 Harken (Pewaukee, Wisconsin, USA)

#### 4.3.1 Firmengeschichte

Harken wurde 1967 von den Brüdern Peter und Olaf Harken gegründet. Das Unternehmen ist weltweit führend bei Winschen, Blöcken und Decksbeschlägen. Im Cam-Cleat-Bereich sind die Carbo-Modelle Marktführer bei Jollen und Kielbooten. Im Clutch-Bereich hat Harken erst später Fuß gefasst.

#### 4.3.2 Carbo Cam Cleat Serie

Die Carbo-Serie verwendet Carbon-verstärktes Polymer für minimales Gewicht.

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 150 | Micro Cam, fest | 3–6 | 80 | 29 | 22–30 |
| 241 | Micro Cam, Pivot | 3–6 | 80 | 38 | 28–38 |
| 365 | Carbo Cam, fest | 6–10 | 180 | 45 | 32–42 |
| 468 | Carbo Cam, fest | 6–10 | 220 | 52 | 38–48 |
| 471 | Carbo Cam + Lead | 6–10 | 220 | 68 | 42–55 |
| 473 | Carbo Cam + Bullseye | 6–10 | 220 | 72 | 45–58 |
| 484 | Carbo Cam, große Basis | 8–12 | 350 | 78 | 48–62 |

**Besonderheiten Harken Carbo:**
- Carbon-verstärktes Nylon: leichter als Aluminium, stärker als Standard-Nylon
- Rund-Zahnprofil: leinenschonend
- Leuchtende Farben (orange, grün) für schnelles Erkennen
- UV-stabilisiertes Material
- Standardausstattung auf vielen Laser/ILCA, 49er, Nacra-Booten

#### 4.3.3 Aluminium Cam Cleat Serie

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 97625 | Alu Cam, fest | 6–10 | 250 | 55 | 35–45 |
| 97632 | Alu Cam, fest | 8–14 | 400 | 88 | 45–58 |
| 97640 | Alu Cam, Schwenk | 6–10 | 250 | 70 | 42–55 |

#### 4.3.4 Harken Lock-In Clutch Serie

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 435 | Midrange Single | 6–10 | 500 | 120 | 65–85 |
| 436 | Midrange Double | 6–10 | 500 | 230 | 120–155 |
| 437 | Midrange Triple | 6–10 | 500 | 340 | 175–225 |
| 445 | Hi-Load Single | 8–14 | 900 | 165 | 100–130 |
| 446 | Hi-Load Double | 8–14 | 900 | 320 | 190–245 |
| 447 | Hi-Load Triple | 8–14 | 900 | 475 | 280–360 |
| 455 | Extreme Single | 10–16 | 1.400 | 240 | 150–195 |
| 456 | Extreme Double | 10–16 | 1.400 | 470 | 290–370 |

**Merkmale Harken Lock-In:**
- Aluminium-Gehäuse mit Edelstahl-Mechanik
- Integrierter Fairlead
- Leichtgängiger Hebel
- Design auf Harken-Winschen abgestimmt
- Farb-codierte Hebel verfügbar

### 4.4 Lewmar (Havant, Hampshire, UK)

#### 4.4.1 Firmengeschichte

Lewmar wurde 1946 gegründet und ist einer der weltweit größten Hersteller von Marine-Hardware. Die D-Serie Clutches sind auf Millionen von Yachten weltweit verbaut und gelten als Industriestandard.

#### 4.4.2 D1-Serie (Sport/Compact)

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 29901420 | D1 Single 6–10 | 6–10 | 450 | 95 | 55–70 |
| 29901421 | D1 Double 6–10 | 6–10 | 450 | 180 | 100–130 |
| 29901422 | D1 Triple 6–10 | 6–10 | 450 | 265 | 145–185 |
| 29901430 | D1 Single 8–12 | 8–12 | 600 | 115 | 65–85 |
| 29901431 | D1 Double 8–12 | 8–12 | 600 | 220 | 120–155 |
| 29901432 | D1 Triple 8–12 | 8–12 | 600 | 325 | 175–225 |

**Merkmale D1:**
- Kunststoff-Gehäuse (glasfaserverstärkt) mit Edelstahl-Mechanik
- Kompakte Bauform, ideal für kleinere Yachten
- Leichtgewicht
- Montage: 2 Schrauben M5 pro Position
- Ersatzteile gut verfügbar

#### 4.4.3 D2-Serie (Standard)

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 29101420 | D2 Single 8–10 | 8–10 | 750 | 140 | 75–95 |
| 29101421 | D2 Double 8–10 | 8–10 | 750 | 270 | 140–180 |
| 29101422 | D2 Triple 8–10 | 8–10 | 750 | 400 | 200–260 |
| 29101430 | D2 Single 8–12 | 8–12 | 900 | 160 | 85–110 |
| 29101431 | D2 Double 8–12 | 8–12 | 900 | 310 | 160–205 |
| 29101432 | D2 Triple 8–12 | 8–12 | 900 | 460 | 235–300 |
| 29101433 | D2 Quad 8–12 | 8–12 | 900 | 610 | 310–395 |
| 29101440 | D2 Single 10–14 | 10–14 | 1.100 | 190 | 100–130 |
| 29101441 | D2 Double 10–14 | 10–14 | 1.100 | 370 | 190–245 |
| 29101442 | D2 Triple 10–14 | 10–14 | 1.100 | 550 | 280–360 |

**Merkmale D2:**
- Aluminium-Gehäuse, hart-eloxiert (schwarz)
- Bewährte Zuverlässigkeit (seit >30 Jahren im Markt)
- Robuster Mechanismus
- Guter Release unter Last
- Montage: 2–3 Schrauben M6 pro Position
- Backing Plate ZWINGEND

#### 4.4.4 D3-Serie (Heavy Duty)

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| 29201440 | D3 Single 10–14 | 10–14 | 1.500 | 260 | 140–180 |
| 29201441 | D3 Double 10–14 | 10–14 | 1.500 | 510 | 270–345 |
| 29201442 | D3 Triple 10–14 | 10–14 | 1.500 | 760 | 395–505 |
| 29201450 | D3 Single 12–16 | 12–16 | 2.000 | 340 | 180–230 |
| 29201451 | D3 Double 12–16 | 12–16 | 2.000 | 670 | 350–445 |

**Merkmale D3:**
- Aluminium-Gehäuse, verstärkt
- Für Yachten >14 m / >10 Tonnen Verdrängung
- Hohe SWL für Großfall und Reffleinen
- Übergroßer Hebel
- Montage: 3–4 Schrauben M8 pro Position
- Backing Plate ZWINGEND (Edelstahl 5 mm)

#### 4.4.5 Lewmar Cam Cleats

Lewmar bietet auch eine kleine Auswahl an Cam Cleats:

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| 29901100 | Standard Cam | 6–10 | 200 | 22–30 |
| 29901110 | Major Cam | 8–14 | 350 | 32–42 |
| 29901120 | Cam + Fairlead | 6–10 | 200 | 28–38 |

### 4.5 Ronstan (Melbourne, Australien)

#### 4.5.1 Firmengeschichte

Ronstan wurde 1953 in Melbourne gegründet und ist einer der ältesten Hersteller von Jacht-Beschlägen. Bekannt für hochwertige Cam Cleats im Jollenbereich und die innovative C-Cleat-Serie.

#### 4.5.2 Cam Cleat Serie

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| RF5001 | Micro, fest | 2–6 | 60 | 18 | 15–22 |
| RF5002 | Micro, seitlich | 2–6 | 60 | 22 | 18–25 |
| RF5005 | Junior, fest | 3–8 | 120 | 30 | 18–26 |
| RF5010 | Standard, fest | 6–10 | 200 | 48 | 22–30 |
| RF5012 | Standard, seitlich | 6–10 | 200 | 55 | 25–34 |
| RF5015 | Standard + Fairlead | 6–10 | 200 | 65 | 28–38 |
| RF5020 | Schwenk-Cam | 6–10 | 200 | 70 | 30–40 |
| RF5025 | Major, fest | 8–14 | 350 | 80 | 32–42 |
| RF5030 | Major + Fairlead | 8–14 | 350 | 98 | 38–48 |
| RF5033 | Mega, fest | 10–16 | 500 | 120 | 42–55 |

**Merkmale Ronstan Cam Cleats:**
- Aluminium, hart-eloxiert (schwarz oder silber)
- Markantes V-Zahnprofil
- Edelstahl-Federn und -Achsen (316)
- Bewährte australische Qualität
- Gutes Preis-Leistungs-Verhältnis

#### 4.5.3 C-Cleat Serie (Racing)

Die C-Cleat-Serie ist Ronstans Premium-Racing-Linie:

| Modell | Typ | Leine (mm) | SWL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|-------------|-----------|
| RF5400 | C-Cleat Micro | 2–6 | 80 | 22 | 25–35 |
| RF5410 | C-Cleat Standard | 4–8 | 150 | 35 | 30–40 |
| RF5420 | C-Cleat Major | 6–10 | 250 | 50 | 38–48 |

**Besonderheiten C-Cleat:**
- CNC-gefrästes Aluminium
- Mikro-Zahnprofil für Dyneema
- Optimiert für dünne High-Performance-Leinen
- Minimales Gewicht

### 4.6 Antal (Treviso, Italien)

#### 4.6.1 Firmengeschichte

Antal wurde 1966 in Treviso, Italien gegründet und hat sich auf innovative Decksbeschläge spezialisiert. Das patentierte V-Grip-System hat den Clutch-Markt beeinflusst und wird insbesondere von italienischen und französischen Werften (Beneteau, Jeanneau, Dufour, Cantiere del Pardo) eingesetzt.

#### 4.6.2 V-Grip Serie

| Modell | Typ | Leine (mm) | SWL (kg) | BL (kg) | Gewicht (g) | Preis (€) |
|--------|-----|------------|----------|---------|-------------|-----------|
| VG8S | V-Grip Single 6–8 | 6–8 | 600 | 1.800 | 100 | 80–105 |
| VG8D | V-Grip Double 6–8 | 6–8 | 600 | 1.800 | 190 | 150–195 |
| VG8T | V-Grip Triple 6–8 | 6–8 | 600 | 1.800 | 280 | 220–285 |
| VG10S | V-Grip Single 8–10 | 8–10 | 800 | 2.400 | 125 | 95–125 |
| VG10D | V-Grip Double 8–10 | 8–10 | 800 | 2.400 | 240 | 180–235 |
| VG10T | V-Grip Triple 8–10 | 8–10 | 800 | 2.400 | 355 | 265–340 |
| VG10Q | V-Grip Quad 8–10 | 8–10 | 800 | 2.400 | 470 | 350–445 |
| VG12S | V-Grip Single 10–12 | 10–12 | 1.000 | 3.000 | 155 | 115–150 |
| VG12D | V-Grip Double 10–12 | 10–12 | 1.000 | 3.000 | 300 | 220–285 |
| VG12T | V-Grip Triple 10–12 | 10–12 | 1.000 | 3.000 | 445 | 325–420 |
| VG14S | V-Grip Single 12–14 | 12–14 | 1.200 | 3.600 | 185 | 140–180 |
| VG14D | V-Grip Double 12–14 | 12–14 | 1.200 | 3.600 | 360 | 270–345 |
| VG14T | V-Grip Triple 12–14 | 12–14 | 1.200 | 3.600 | 535 | 395–505 |

**V-Grip Besonderheiten:**
- Patentiertes V-Profil: Leine wird in V-Rinne gedrückt statt flach geklemmt
- 30–40% geringere Release-Kraft als Wettbewerber (herstellerangabe)
- Minimaler Leinenverschleiß durch gleichmäßige Kraftverteilung
- Aluminium-Gehäuse, hart-eloxiert
- Edelstahl 316L-Mechanik
- Integrierter einstellbarer Fairlead
- Farbcodierung: Rot, Blau, Gelb, Schwarz, Grau

#### 4.6.3 Antal Cam Cleats

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| AC006 | Junior Cam | 3–6 | 80 | 14–20 |
| AC010 | Standard Cam | 6–10 | 180 | 20–28 |
| AC014 | Major Cam | 8–14 | 350 | 30–40 |

### 4.7 Weitere Hersteller

#### 4.7.1 Schaefer Marine (New Bedford, Massachusetts, USA)

Bekannt für robuste, langlebige Decksbeschläge im amerikanischen Markt.

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| 70-07 | Cam Cleat | 6–10 | 200 | 25–35 |
| 70-17 | Cam Cleat Major | 8–14 | 400 | 38–50 |

#### 4.7.2 RWO (Rainham, Kent, UK)

Spezialist für Jollen-Beschläge.

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| R3700 | Mini Cam | 2–5 | 50 | 8–12 |
| R3710 | Junior Cam | 3–6 | 80 | 10–15 |
| R3720 | Standard Cam | 6–10 | 180 | 18–25 |

#### 4.7.3 Holt Allen (Alverstoke, Hampshire, UK)

Teil der Allen Brothers Gruppe, fokussiert auf hochwertige Jollen-Beschläge.

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| A.677 | Cam Cleat Junior | 3–6 | 100 | 12–18 |
| A.4993 | Cam Cleat Standard | 6–10 | 200 | 20–28 |
| A.4994 | Cam Cleat + Fairlead | 6–10 | 200 | 25–35 |

#### 4.7.4 Viadana (Brescia, Italien)

Italienischer Hersteller mit gutem Preis-Leistungs-Verhältnis.

| Modell | Typ | Leine (mm) | SWL (kg) | Preis (€) |
|--------|-----|------------|----------|-----------|
| 13.10 | Cam Cleat Junior | 3–6 | 80 | 10–15 |
| 13.20 | Cam Cleat Standard | 6–10 | 180 | 16–24 |
| 13.30 | Cam Cleat Major | 8–14 | 350 | 28–38 |
| 57.10 | Jammer Single | 6–10 | 500 | 55–72 |
| 57.20 | Jammer Double | 6–10 | 500 | 100–130 |

---

## 5. Technische Spezifikationen

### 5.1 Hersteller-übergreifende Vergleichstabelle: Cam Cleats (6–10 mm)

| Hersteller | Modell | SWL (kg) | BL (kg) | Gewicht (g) | Material | Preis (€) |
|------------|--------|----------|---------|-------------|----------|-----------|
| Clamcleat | CL211 Mk2 | 200 | 600 | 48 | Alu elox. | 18–26 |
| Clamcleat | CL814 | 120 | 360 | 28 | Composite | 10–16 |
| Clamcleat | CL711 | 300 | 900 | 95 | Edelstahl | 45–60 |
| Harken | 365 Carbo | 180 | 540 | 45 | Carbon-Poly | 32–42 |
| Harken | 468 Carbo | 220 | 660 | 52 | Carbon-Poly | 38–48 |
| Harken | 97625 | 250 | 750 | 55 | Alu elox. | 35–45 |
| Ronstan | RF5010 | 200 | 600 | 48 | Alu elox. | 22–30 |
| Ronstan | RF5420 | 250 | 750 | 50 | Alu CNC | 38–48 |
| Antal | AC010 | 180 | 540 | 45 | Alu elox. | 20–28 |
| Lewmar | 29901100 | 200 | 600 | 50 | Alu elox. | 22–30 |
| RWO | R3720 | 180 | 540 | 45 | Alu elox. | 18–25 |
| Viadana | 13.20 | 180 | 540 | 42 | Alu elox. | 16–24 |

**Confidence:** measured (SWL/BL aus Hersteller-TDS), estimated (Preise, variieren nach Händler und Region)

### 5.2 Hersteller-übergreifende Vergleichstabelle: Rope Clutches (8–12 mm)

| Hersteller | Modell | SWL (kg) | BL (kg) | Gewicht Single (g) | Release bei 50% | Preis Single (€) |
|------------|--------|----------|---------|--------------------|--------------------|-------------------|
| Spinlock | XAS 0612 | 700 | 2.100 | 125 | 8–12 N | 70–90 |
| Spinlock | XCS 0612 | 800 | 2.400 | 160 | 10–14 N | 95–120 |
| Spinlock | XTS 0612 | 900 | 2.700 | 130 | 10–15 N | 120–155 |
| Lewmar | D1 8–12 | 600 | 1.800 | 115 | 12–16 N | 65–85 |
| Lewmar | D2 8–12 | 900 | 2.700 | 160 | 12–18 N | 85–110 |
| Lewmar | D3 10–14 | 1.500 | 4.500 | 260 | 15–22 N | 140–180 |
| Antal | VG10 | 800 | 2.400 | 125 | 6–10 N | 95–125 |
| Antal | VG12 | 1.000 | 3.000 | 155 | 8–12 N | 115–150 |
| Harken | 445 Hi-Load | 900 | 2.700 | 165 | 12–18 N | 100–130 |

### 5.3 Montagemaße und Bohrbilder

#### 5.3.1 Cam Cleats — Typische Montagemaße

| Größenklasse | Länge (mm) | Breite (mm) | Höhe (mm) | Bohrung | Schrauben |
|--------------|------------|-------------|-----------|---------|-----------|
| Junior (3–6 mm) | 45–55 | 18–22 | 20–25 | 2× M4 | Senkkopf |
| Standard (6–10 mm) | 60–75 | 25–30 | 28–35 | 2× M5 | Senkkopf |
| Major (8–14 mm) | 80–95 | 32–38 | 35–42 | 2× M5 oder M6 | Senkkopf |
| Mega (10–16 mm) | 100–115 | 38–45 | 42–50 | 2× M6 | Senkkopf |

#### 5.3.2 Rope Clutches — Typische Montagemaße

| Modell | Einzelbreite (mm) | Tiefe (mm) | Höhe (mm) | Bohrung | Schrauben pro Pos. |
|--------|-------------------|------------|-----------|---------|---------------------|
| Spinlock XAS 0612 | 35 | 95 | 42 | 2× M6 | Sechskant |
| Spinlock XAS 0614 | 40 | 100 | 45 | 2× M6 | Sechskant |
| Spinlock XTS 0612 | 33 | 92 | 40 | 2× M6 | Sechskant |
| Lewmar D1 | 32 | 85 | 38 | 2× M5 | Sechskant |
| Lewmar D2 | 38 | 100 | 44 | 2–3× M6 | Sechskant |
| Lewmar D3 | 45 | 115 | 52 | 3–4× M8 | Sechskant |
| Antal VG10 | 36 | 95 | 40 | 2× M6 | Sechskant |
| Antal VG14 | 42 | 110 | 48 | 2–3× M6 | Sechskant |
| Harken 445 | 38 | 98 | 42 | 2× M6 | Sechskant |

### 5.4 Lebensdauer-Vergleich

| Komponente | Lebensdauer Fahrt | Lebensdauer Regatta | Lebensdauer Superyacht |
|------------|-------------------|---------------------|------------------------|
| Cam Cleat (Alu) | 8–15 Jahre | 3–5 Saisons | 10–15 Jahre |
| Cam Cleat (Composite) | 5–10 Jahre | 2–4 Saisons | — |
| Cam Cleat (Edelstahl) | 15–25 Jahre | 5–8 Saisons | 15–20 Jahre |
| Rope Clutch (Standard) | 10–15 Jahre | 3–5 Saisons | 8–12 Jahre |
| Rope Clutch (Performance) | 8–12 Jahre | 2–4 Saisons | 6–10 Jahre |
| Rope Clutch (Superyacht) | 15–20 Jahre | — | 15–20 Jahre |
| Feder (Edelstahl) | 3–8 Jahre | 1–3 Saisons | 2–5 Jahre |
| Nocken/Cam | 5–10 Jahre | 2–4 Saisons | 4–8 Jahre |

**Confidence:** estimated — Lebensdauer variiert stark je nach Nutzung, Wartung, Klima und Leinentyp.

### 5.5 Korrosionsbeständigkeit

| Material | Salzwasser | Süßwasser | Tropisch | Arktisch |
|----------|-----------|-----------|----------|----------|
| Aluminium hart-eloxiert | Gut (8/10) | Sehr gut (9/10) | Gut (7/10) | Sehr gut (9/10) |
| Edelstahl 316L | Sehr gut (9/10) | Ausgezeichnet (10/10) | Gut (8/10) | Ausgezeichnet (10/10) |
| Edelstahl 304 | Mäßig (5/10) | Sehr gut (9/10) | Schlecht (3/10) | Gut (8/10) |
| Carbon-Polymer | Ausgezeichnet (10/10) | Ausgezeichnet (10/10) | Gut (8/10 UV) | Ausgezeichnet (10/10) |
| GFK-Nylon | Gut (8/10) | Sehr gut (9/10) | Mäßig (6/10 UV) | Sehr gut (9/10) |
| Acetal/POM | Sehr gut (9/10) | Sehr gut (9/10) | Gut (7/10 UV) | Sehr gut (9/10) |
| Zamak (Zinkguss) | Schlecht (2/10) | Mäßig (5/10) | Sehr schlecht (1/10) | Mäßig (4/10) |

**Wichtig:** Zamak-Klemmen (häufig bei Billigprodukten) sind für den Marineeinsatz NICHT geeignet. Sie korrodieren innerhalb von 1–2 Saisons in Salzwasser.

### 5.6 Gewichtsvergleich nach Funktion

Für eine typische 12-m-Fahrtenyacht mit Standardausrüstung:

| Konfiguration | Gewicht (g) | Preis (€) |
|---------------|-------------|-----------|
| 6× Spinlock XAS 0612 (3er BB + 3er STB) | 710 | 380–480 |
| 6× Lewmar D2 8-12 (3er BB + 3er STB) | 920 | 470–600 |
| 6× Antal VG10 (3er BB + 3er STB) | 710 | 530–680 |
| 6× Harken 445 (3er BB + 3er STB) | 1.020 | 560–720 |
| 4× Cam Cleat CL211 + 2× Clutch XAS | 446 | 176–222 |

---

## 6. Wartung und Service

### 6.1 Allgemeine Wartungsprinzipien

Cam Cleats und Rope Clutches sind mechanisch einfache Geräte, die aber durch Salz, Sand, UV-Strahlung und Leinenabrieb verschleißen. Regelmäßige Wartung verlängert die Lebensdauer erheblich und verhindert gefährliches Versagen.

**Wartungsintervall-Empfehlung:**

| Nutzung | Inspektion | Grundwartung | Überholung |
|---------|------------|--------------|------------|
| Wochenend-Segler (50h/Jahr) | Alle 3 Monate | 1× jährlich (Saisonende) | Alle 3–5 Jahre |
| Vielsegeler (200h/Jahr) | Monatlich | 2× jährlich | Alle 2–3 Jahre |
| Regatta (300h+/Jahr) | Wöchentlich | 3× jährlich | Jährlich |
| Charter/Professionell | Vor jeder Übergabe | Monatlich | Jährlich |
| Blauwasser (ganzjährig) | Monatlich | 4× jährlich | Alle 2 Jahre |

### 6.2 Wartung nach Hersteller

#### 6.2.1 Spinlock — Wartungsprotokoll

**Vierteljährliche Inspektion:**
1. Hebel auf Leichtgängigkeit prüfen
2. Nocken auf Verschleiß und Grate prüfen
3. Fairlead auf Risse und Ausbrüche prüfen
4. Schrauben auf festen Sitz prüfen (Drehmoment: M6 = 8–10 Nm)

**Jährliche Grundwartung:**
1. Clutch mit Süßwasser ausspülen (10 Min. einweichen lassen)
2. Alle beweglichen Teile mit McLube oder Spinlock-Spray schmieren
3. Federn auf Ermüdung prüfen (Federkraft muss spürbar sein)
4. Nocken/Cam auf Zahnabtrag prüfen (Zahnhöhe >50% = OK)
5. Leinenkanal auf Salzrückstände reinigen

**Nocken-Austausch (alle 3–5 Jahre oder bei sichtbarem Verschleiß):**
1. Achsschraube entfernen (Innensechskant)
2. Alten Nocken herausziehen
3. Federn prüfen und ggf. ersetzen
4. Neuen Nocken einsetzen (Orientierung beachten)
5. Achsschraube mit mittelfestem Schraubensicherungslack (Loctite 243) einsetzen
6. Funktionstest mit Leine

#### 6.2.2 Lewmar — Wartungsprotokoll

**Jährliche Grundwartung:**
1. Clutch mit Süßwasser reinigen
2. Mechanismus mit Lewmar Winch Spray oder äquivalentem PTFE-Spray behandeln
3. Hebelmechanismus auf Spiel prüfen
4. Grundplatte auf Risse prüfen (besonders an Schraubenlöchern)
5. Release unter Last testen (Leine mit 10 kg belasten, Hebel muss sich mit einer Hand öffnen lassen)

**Federtausch Lewmar D2:**
1. Deckplatte abnehmen (2 Schrauben)
2. Nocken entnehmen
3. Alte Feder(n) entfernen
4. Neue Federn einsetzen (Orientierung beachten: engere Windung unten)
5. Nocken wieder einsetzen
6. Deckplatte montieren
7. Funktionstest

#### 6.2.3 Antal — Wartungsprotokoll

**V-Grip Wartung:**
1. Süßwasserspülung nach jeder Salzwasser-Saison
2. V-Profil mit weicher Bürste reinigen (kein Metall!)
3. Mechanismus mit Trockenschmierung (PTFE) behandeln
4. KEIN Öl oder Fett verwenden (Leinengrip würde reduziert)
5. Farbcodierte Hebelkappen bei Bedarf ersetzen

#### 6.2.4 Clamcleat — Wartung Cam Cleats

**Cam Cleat Grundwartung:**
1. Federn prüfen: Backen müssen ohne Leine vollständig schließen
2. Zahnprofil prüfen: Zähne müssen scharfkantig sein
3. Achse prüfen: Backen dürfen kein seitliches Spiel haben
4. Bei Alu-Cam-Cleats: Eloxierung auf Beschädigungen prüfen
5. Schrauben nachziehen (M4: 3–4 Nm, M5: 5–6 Nm)

**Federtausch Clamcleat:**
1. Cam-Cleat von Montagefläche abschrauben
2. Achsstift herausdrücken (Splintsicherung entfernen)
3. Backen und Federn entnehmen
4. Neue Federn einsetzen
5. Backen einsetzen (Zahnrichtung beachten!)
6. Achsstift eindrücken und sichern
7. Montieren und testen

### 6.3 Typische Verschleißteile und Standzeiten

| Teil | Standzeit (Fahrt) | Standzeit (Regatta) | Preis (€) |
|------|-------------------|---------------------|-----------|
| Feder (Cam Cleat) | 3–5 Jahre | 1–2 Saisons | 3–8 |
| Feder (Rope Clutch) | 4–6 Jahre | 2–3 Saisons | 5–12 |
| Nocken/Cam (Clutch) | 5–8 Jahre | 2–4 Saisons | 15–35 |
| Cam-Backen (Cam Cleat) | 5–10 Jahre | 2–4 Saisons | 8–20 |
| Hebel (Clutch) | 8–15 Jahre | 4–6 Saisons | 10–35 |
| Fairlead (Clutch) | 10–15 Jahre | 5–8 Saisons | 8–15 |
| Achse/Bolzen | 10–20 Jahre | 5–10 Saisons | 3–8 |
| Grundplatte | Lebensdauer | 8–15 Saisons | Ersatz = Neukauf |

### 6.4 Schmiermittel-Empfehlung

| Produkt | Typ | Anwendung | Preis (€) |
|---------|-----|-----------|-----------|
| McLube SailKote | Trockenschmierung | Alle Clutches und Cam Cleats | 12–18 (Spray) |
| Spinlock Service Spray | PTFE-Spray | Spinlock-Produkte | 10–15 |
| Lewmar Winch Spray | PTFE-Spray | Lewmar-Produkte | 10–15 |
| Lanocil | Lanolin-Basis | Korrosionsschutz auf Achsen | 15–22 |
| Boeshield T-9 | Wachs/PTFE | Langzeitschutz | 12–18 |

**ACHTUNG:** Niemals Standard-WD-40 auf Cam Cleats oder Clutches verwenden! WD-40 ist ein Kriechöl, kein Schmiermittel. Es verflüchtigt sich schnell und hinterlässt einen klebrigen Film, der Sand und Salz bindet. Ausschließlich marine-spezifische Trockenschmiermittel verwenden.

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Zuordnung nach Anwendung

#### 7.1.1 Fallen

| Anwendung | Empfohlener Typ | Empfohlene Modelle | Bootsgröße |
|-----------|----------------|-------------------|------------|
| Großfall | Rope Clutch | Spinlock XAS/XTS, Lewmar D2/D3, Antal VG12 | 8–16m |
| Genua-Fall | Rope Clutch | Spinlock XAS/XTS, Lewmar D2, Antal VG10 | 8–16m |
| Spi-Fall | Rope Clutch | Spinlock XAS, Lewmar D1/D2, Antal VG8 | 8–14m |
| Code-0-Fall | Rope Clutch | Spinlock XTS, Lewmar D2/D3, Antal VG12 | 10–16m |
| Mastfall (Jolle) | Cam Cleat | Clamcleat CL211, Harken 468, Ronstan RF5010 | 4–8m |

#### 7.1.2 Schoten

| Anwendung | Empfohlener Typ | Empfohlene Modelle | Bootsgröße |
|-----------|----------------|-------------------|------------|
| Großschot | Cam Cleat (Jolle) / Winch (Yacht) | Clamcleat CL217, Harken 484 | 4–10m |
| Fockschot | Cam Cleat | Clamcleat CL211, Harken 365/468 | 4–8m |
| Genuaschot | Winch + Cam Cleat | Clamcleat CL253 (Schwenk) | 6–10m |
| Spi-Schot | Cam Cleat (Jolle) | Harken 365, Ronstan RF5010 | 4–8m |
| Gennaker-Schot | Cam Cleat | Clamcleat CL217, Harken 484 | 8–14m |

#### 7.1.3 Strecker und Niederholer

| Anwendung | Empfohlener Typ | Empfohlene Modelle | Bootsgröße |
|-----------|----------------|-------------------|------------|
| Cunningham | Cam Cleat | Clamcleat CL205/CL211, Harken 150 | 4–12m |
| Baumniederholer | Cam Cleat | Clamcleat CL211, Harken 468 | 4–12m |
| Achterstag | Rope Clutch | Spinlock XTS, Lewmar D2 | 10–16m |
| Babystag | Rope Clutch | Spinlock XAS, Antal VG10 | 10–16m |
| Traveller-Schot | Cam Cleat (Schwenk) | Clamcleat CL253, Harken 241 | 4–10m |

#### 7.1.4 Reff-System

| Anwendung | Empfohlener Typ | Empfohlene Modelle | Bootsgröße |
|-----------|----------------|-------------------|------------|
| Reff 1 | Rope Clutch | Spinlock XAS/XTS, Lewmar D2 | 8–16m |
| Reff 2 | Rope Clutch | Spinlock XAS, Lewmar D2 | 8–16m |
| Reff 3 | Rope Clutch | Spinlock XAS, Lewmar D1 | 10–16m |
| Lazy Jacks | Cam Cleat (Mast) | Clamcleat CL207, Ronstan RF5002 | 8–14m |

### 7.2 Zuordnung nach Bootsgröße

#### 7.2.1 Jolle (4–8 m)

**Empfohlene Ausstattung:**
- 4–8 Cam Cleats (Aluminium oder Composite)
- Keine Rope Clutches (Lasten zu gering)
- Leinendurchmesser: 3–8 mm

**Budget-Ausstattung (Jolle):**
| Position | Modell | Stück | Preis (€) |
|----------|--------|-------|-----------|
| Großschot | Clamcleat CL211 | 1 | 18–26 |
| Fockschot (BB+STB) | Clamcleat CL205 | 2 | 24–36 |
| Cunningham | Clamcleat CL205 | 1 | 12–18 |
| Baumniederholer | Clamcleat CL205 | 1 | 12–18 |
| **Gesamt** | | **5** | **66–98** |

**Performance-Ausstattung (Jolle):**
| Position | Modell | Stück | Preis (€) |
|----------|--------|-------|-----------|
| Großschot | Harken 468 Carbo + Schwenk | 1 | 55–70 |
| Fockschot (BB+STB) | Ronstan RF5420 C-Cleat | 2 | 76–96 |
| Cunningham | Harken 150 Micro | 1 | 22–30 |
| Baumniederholer | Harken 365 Carbo | 1 | 32–42 |
| Traveller | Clamcleat CL253 Schwenk | 1 | 28–38 |
| **Gesamt** | | **6** | **213–276** |

#### 7.2.2 Fahrtensegler (8–14 m)

**Standard-Ausstattung:**
- 2–4 Cam Cleats (Strecker, Niederholer)
- 4–6 Rope Clutches (Fallen, Reffleinen)
- Leinendurchmesser: 6–12 mm

**Typische Konfiguration (10-m-Fahrtensegler):**
| Position | Typ | Modell | Stück | Preis (€) |
|----------|-----|--------|-------|-----------|
| BB-Bank (Großfall, Reff 1, Reff 2) | Clutch | Spinlock XAS 0612/3 | 1 | 190–240 |
| STB-Bank (Genua, Spi, Reserve) | Clutch | Spinlock XAS 0612/3 | 1 | 190–240 |
| Cunningham | Cam | Clamcleat CL211 | 1 | 18–26 |
| Baumniederholer | Cam | Clamcleat CL211 | 1 | 18–26 |
| Traveller | Cam | Clamcleat CL253 | 1 | 28–38 |
| **Gesamt** | | | **5** | **444–570** |

#### 7.2.3 Performance Cruiser (10–16 m)

**Typische Konfiguration (13-m-Performance-Cruiser):**
| Position | Typ | Modell | Stück | Preis (€) |
|----------|-----|--------|-------|-----------|
| BB-Bank (Groß, R1, R2, R3) | Clutch | Spinlock XTS 0614/4 | 1 | 530–670 |
| STB-Bank (Genua, Spi, Code-0, Reserve) | Clutch | Spinlock XTS 0614/4 | 1 | 530–670 |
| Cunningham | Cam | Harken 468 | 1 | 38–48 |
| Baumniederholer | Clutch | Spinlock XAS 0612/1 | 1 | 70–90 |
| Achterstag | Clutch | Spinlock XTS 0612/1 | 1 | 120–155 |
| **Gesamt** | | | **5** | **1.288–1.633** |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Leine rutscht durch Cam Cleat

**Beschreibung:** Die Leine rutscht unter Last durch den Cam Cleat, obwohl die Backen geschlossen sind.

**Ursachen:**
- Leinendurchmesser zu gering für die Cam-Cleat-Größe
- Cam-Backen-Zähne abgenutzt (Zahnhöhe <50%)
- Federn ermüdet (Klemmkraft zu gering)
- Leine nass und verschmutzt (reduzierter Reibungskoeffizient)
- Falsche Leinenart (mantellos, PTFE-beschichtet)
- Einlaufwinkel zu steil (>30°)

**Diagnose:**
1. Leinendurchmesser mit Schieblehre messen und mit Cam-Cleat-Spezifikation vergleichen
2. Zahnhöhe visuell prüfen (Vergleich mit neuem Cam)
3. Backen manuell öffnen und Federkraft spüren (muss deutlich spürbar sein)
4. Einlaufwinkel messen

**Behebung:**
- Leinendurchmesser anpassen (nächste Größe)
- Cam-Backen und Federn ersetzen
- Fairlead nachrüsten für korrekten Einlaufwinkel
- Leinentyp wechseln (Polyester-Mantel statt Dyneema blank)

**Confidence:** documented — Häufigstes Fehlerbild, gut dokumentiert in Foren und Herstellerunterlagen.

### 8.2 Fehlerbild F02: Cam Cleat klemmt (Backen öffnen nicht)

**Beschreibung:** Die Cam-Cleat-Backen bleiben in geschlossener Position und lassen sich nicht oder nur schwer öffnen. Die Leine kann nicht freigegeben werden.

**Ursachen:**
- Salzverkrustung in der Achse
- Korrosion der Federn oder Achse
- Sand/Schmutz zwischen Backen und Gehäuse
- Deformierte Backen (nach Überlastung)
- Falsches Schmiermittel (klebriger Film)

**Diagnose:**
1. Backen manuell bewegen: Gehen sie schwergängig oder gar nicht?
2. Achsbereich visuell prüfen (Salzrückstände, Korrosion)
3. Backengeometrie prüfen (Verformung nach Überlast)

**Behebung:**
- Cam Cleat in Süßwasser einweichen (>30 Min.)
- Achse und Federn reinigen
- Mit Trockenschmiermittel (McLube) behandeln
- Bei Korrosion: Federn und Achse ersetzen
- Bei deformierten Backen: Komplett ersetzen

### 8.3 Fehlerbild F03: Rope Clutch hält nicht unter Last

**Beschreibung:** Der Rope Clutch lässt die Leine unter Last langsam durchrutschen, obwohl der Hebel vollständig geschlossen ist.

**Ursachen:**
- Nocken/Cam abgenutzt (Profil abgeflacht)
- Grundplatte verschlissen (Rillen abgetragen)
- Leinendurchmesser am unteren Rand des Bereichs
- Leine zu glatt (Dyneema ohne Mantel, UHMWPE)
- Salz-/Schmutzablagerungen auf Klemmflächen
- Feder ermüdet (Nocken drückt nicht ausreichend)

**Diagnose:**
1. Hebel schließen und manuell an der Leine ziehen (50 kg)
2. Nocken-Profil visuell prüfen (Zahnhöhe, Abflachung)
3. Grundplatten-Rillen auf Tiefe prüfen
4. Leinendurchmesser verifizieren
5. Leine auf Verschmutzung prüfen

**Behebung:**
- Nocken/Cam ersetzen (Hersteller-Ersatzteil)
- Grundplatte reinigen oder ersetzen
- Leinendurchmesser optimieren (größere Leine)
- Leine mit Polyester-Mantel verwenden
- Süßwasserspülung und Trockenschmierung

**Confidence:** measured — Herstellerspezifische Diagnosewerte verfügbar.

### 8.4 Fehlerbild F04: Clutch-Hebel schwergängig

**Beschreibung:** Der Clutch-Hebel lässt sich nur mit hohem Kraftaufwand öffnen oder schließen.

**Ursachen:**
- Salzverkrustung im Hebelmechanismus
- Korrosion der Hebel-Achse
- Verbogener Hebel (nach seitlichem Stoß)
- Sand im Mechanismus
- Falsche Leinengröße (zu dick)

**Diagnose:**
1. Hebel ohne Leine betätigen (ist die Schwergängigkeit lastunabhängig?)
2. Hebel-Achse visuell prüfen
3. Hebel auf Geradheit prüfen (Vergleich mit Nachbar-Clutch)

**Behebung:**
- Mechanismus mit Süßwasser spülen
- Hebel-Achse mit Trockenschmiermittel behandeln
- Verbogenen Hebel ersetzen (nicht richten!)
- Sand/Schmutz mit Druckluft entfernen

### 8.5 Fehlerbild F05: Ausbruch der Decksmontage

**Beschreibung:** Die Clutch-Montage reißt unter Last aus dem Deck. Schrauben ziehen durch das Laminat.

**Ursachen:**
- Fehlende oder unterdimensionierte Backing Plate
- Sandwich-Kern nicht komprimiert (Kernkollaps unter Punktlast)
- Falsche Schraubengröße oder -typ
- Überlastung (SWL überschritten)
- Laminatschaden (Delamination, Osmose)

**Diagnose:**
1. Befestigungsbereich visuell prüfen (Risse, Ausbrüche)
2. Schrauben auf festen Sitz prüfen
3. Unter Deck: Backing Plate vorhanden? Dimensionierung korrekt?
4. Laminatqualität prüfen (Klopftest)

**Behebung:**
- Laminat reparieren (Epoxy-Aufbau)
- Korrekte Backing Plate nachrüsten
- Sandwich-Kern im Befestigungsbereich durch Vollaminat ersetzen
- Schraubengröße und -typ korrigieren (Maschinenschrauben + Muttern bevorzugt)

**AYDI-Relevanz:** KRITISCHER BEFUND — Bei festgestelltem Ausbruch: "Befund prüfen" mit Confidence "visual_medium" oder "visual_low". Nie als bestätigt melden.

### 8.6 Fehlerbild F06: Korrosion an Aluminium-Cam-Cleats

**Beschreibung:** Weiße, pulverige Ablagerungen (Aluminiumoxid) auf den Cam-Cleat-Oberflächen. Backen werden rau und schwergängig.

**Ursachen:**
- Beschädigte Eloxierung (Kratzer, mechanische Beschädigung)
- Galvanische Korrosion (Kontakt mit Edelstahl ohne Isolation)
- Salzwasserexposition ohne Süßwasserspülung
- Eloxierungsqualität mangelhaft (Billigprodukt)

**Diagnose:**
1. Oberfläche visuell prüfen (weiße Ablagerungen, raue Stellen)
2. Kontaktpunkt mit anderen Metallen prüfen (galvanische Korrosion?)
3. Funktionstest: Backen auf Leichtgängigkeit prüfen

**Behebung:**
- Leichte Korrosion: Mit feinem Schleifpapier (600er) entfernen, neu versiegeln
- Starke Korrosion: Cam Cleat ersetzen
- Galvanische Isolation nachrüsten (Nylon-Unterlegscheiben, Isolierband)
- Regelmäßige Süßwasserspülung einführen

### 8.7 Fehlerbild F07: Feder-Ermüdung in Cam Cleat

**Beschreibung:** Die Cam-Cleat-Backen schließen nicht mehr vollständig oder nur noch schwach. Leine wird bei geringer Last nicht mehr gehalten.

**Ursachen:**
- Natürliche Federermüdung (Materialermüdung nach 10.000+ Zyklen)
- Korrosion der Feder (Edelstahl 304 statt 316L)
- Dauerlast (Leine permanent im Cam belegt)
- UV-Schädigung bei Kunststoff-Federn

**Diagnose:**
1. Backen ohne Leine zusammendrücken: Schließen sie vollständig?
2. Federkraft mit Finger spüren: Deutlich schwächer als bei neuem Cam?
3. Feder visuell prüfen (Verfärbung, Risse, Rost)

**Behebung:**
- Federn ersetzen (Hersteller-Originalteile)
- Bei Billigprodukten: Kompletten Cam Cleat ersetzen (Federn nicht einzeln verfügbar)
- Dauerlast vermeiden: Leinen nach dem Segeln aus dem Cam lösen

### 8.8 Fehlerbild F08: Leinenverschleiß durch Clutch

**Beschreibung:** Die Leine zeigt im Bereich des Clutches starken Abrieb, Faserbrüche oder Mantelschäden.

**Ursachen:**
- Leine zu dünn für den Clutch (Punktbelastung)
- Nocken-Profil zu aggressiv für den Leinentyp
- Seitliche Leinenführung (Leine scheuert am Clutch-Gehäuse)
- Fieren unter Last ohne Winch (Reibungshitze)
- Salzkristalle im Clutch (wirken wie Schleifpapier)

**Diagnose:**
1. Leine im Clutch-Bereich visuell prüfen (Mantelabrieb, Farbverlust)
2. Leinenführung prüfen (kommt die Leine gerade in den Clutch?)
3. Clutch-Nocken auf Grate oder Scharfkantigkeit prüfen

**Behebung:**
- Fairlead korrekt ausrichten
- Leinendurchmesser optimieren (im oberen Bereich des Clutch-Ranges)
- Clutch regelmäßig reinigen (Salz entfernen)
- Leine alle 2–3 Saisons ersetzen (Sicherheit!)
- Bei chronischem Problem: Clutch-Marke wechseln (Antal V-Grip = leinenschonend)

### 8.9 Fehlerbild F09: Clutch-Gehäuse gebrochen

**Beschreibung:** Das Gehäuse des Rope Clutches zeigt Risse oder ist gebrochen. Typischerweise an Schraubenlöchern oder am Hebellager.

**Ursachen:**
- Überlastung (Brechen der BL überschritten)
- Materialermüdung (Aluminium-Wechsellastermüdung)
- UV-Alterung bei Kunststoff-Gehäusen
- Montagefehler (Schrauben zu fest angezogen)
- Schlagbelastung (Beschlag wird getroffen)

**Diagnose:**
1. Gehäuse visuell auf Risse, Haarrisse, Brüche prüfen
2. Bruchfläche analysieren (Gewaltbruch = glatt; Ermüdung = muschelig)
3. Montage prüfen (Schrauben-Drehmoment, Backing Plate)

**Behebung:**
- Clutch SOFORT ersetzen (Sicherheitsrisiko!)
- Reparatur nicht möglich und nicht empfohlen
- Ursache klären: Überlastung → größeren Clutch wählen
- Bei Kunststoff-Gehäuse: UV-Schutz verbessern oder auf Aluminium umsteigen

### 8.10 Fehlerbild F10: Falsche Montageorientierung

**Beschreibung:** Der Cam Cleat oder Clutch ist so montiert, dass die Leine unter ungünstigem Winkel einläuft. Folge: Reduzierte Haltekraft, erhöhter Verschleiß.

**Ursachen:**
- Planungsfehler bei der Installation
- Nachträgliche Änderung der Leinenführung (z.B. neue Umlenkrolle)
- Unerfahrener Monteur

**Diagnose:**
1. Einlaufwinkel messen (Winkelmesser oder Smartphone-App)
2. Seitliche Ablenkung messen
3. Leine im Clutch-Bereich auf asymmetrischen Verschleiß prüfen

**Behebung:**
- Clutch/Cam Cleat in korrekte Position umsetzen
- Fairlead oder Umlenkrolle nachrüsten
- Unterlegkeile verwenden für Winkelkorrektur
- Alte Schraubenlöcher mit Epoxy verschließen

### 8.11 Fehlerbild F11: Galvanische Korrosion an Befestigungen

**Beschreibung:** Korrosion an Schrauben, Backing Plate oder Deck im Bereich der Clutch-Montage durch galvanische Elementbildung.

**Ursachen:**
- Edelstahl-Schrauben direkt in Aluminium-Deck (ohne Isolation)
- Aluminium-Clutch auf Edelstahl-Backing-Plate (ohne Isolation)
- Kupferhaltige Unterwasser-Farbe in der Nähe der Montage
- Salzwasser als Elektrolyt

**Diagnose:**
1. Schraubenköpfe auf Korrosionsspuren prüfen
2. Unter Deck: Backing-Plate-Kontaktfläche prüfen
3. Materialpaarungen identifizieren

**Behebung:**
- Nylon-Unterlegscheiben zwischen verschiedenen Metallen
- Isolierband (z.B. Tef-Gel) auf Kontaktflächen
- Regelmäßige Süßwasserspülung
- Bei starker Korrosion: Alle Befestigungselemente ersetzen

### 8.12 Fehlerbild F12: UV-Degradation von Composite-Cam-Cleats

**Beschreibung:** Composite/Kunststoff-Cam-Cleats werden spröde, verfärben sich und verlieren an Festigkeit nach mehrjähriger UV-Exposition.

**Ursachen:**
- Direkte Sonneneinstrahlung (Decksposition)
- Fehlende UV-Stabilisierung (Billigprodukte)
- Tropisches Klima (höhere UV-Intensität)
- Alter >5 Jahre bei permanenter Exposition

**Diagnose:**
1. Oberfläche visuell prüfen (Aufhellung, Kreidung, Verfärbung)
2. Material mit Fingernagel kratzen (sprödes Material bricht)
3. Biegefestigkeit manuell prüfen (Gehäuse darf sich nicht biegen lassen)

**Behebung:**
- Betroffene Cam Cleats ersetzen (keine Reparatur möglich)
- Bei Neukauf: Aluminium statt Composite wählen
- UV-Schutzkappe aufsetzen (wenn verfügbar)
- Regelmäßig mit UV-Schutz-Spray behandeln (z.B. 303 Aerospace Protectant)

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Leine hält nicht

```
Leine hält nicht im Cam Cleat / Clutch
│
├── Ist der Leinendurchmesser innerhalb der Spezifikation?
│   ├── NEIN → Leine oder Cam/Clutch-Größe anpassen
│   └── JA → Weiter
│
├── Ist die Leine nass/verschmutzt/ölig?
│   ├── JA → Leine reinigen und trocknen. Erneut testen.
│   └── NEIN → Weiter
│
├── Ist der Leinentyp geeignet? (Polyester-Mantel vorhanden?)
│   ├── NEIN → Leinentyp wechseln (Polyester-Mantel erforderlich)
│   └── JA → Weiter
│
├── Sind Cam-Backen/Nocken verschlissen?
│   ├── JA → Cam/Nocken ersetzen (Hersteller-Ersatzteil)
│   └── NEIN → Weiter
│
├── Ist die Feder intakt?
│   ├── NEIN → Feder ersetzen
│   └── JA → Weiter
│
├── Ist der Einlaufwinkel korrekt?
│   ├── NEIN → Fairlead nachrüsten oder Montage korrigieren
│   └── JA → Cam Cleat / Clutch ist unterdimensioniert → größeres Modell wählen
```

### 9.2 Entscheidungsbaum: Clutch lässt sich nicht öffnen

```
Clutch-Hebel lässt sich nicht öffnen
│
├── Ist die Leine unter Last?
│   ├── JA → Leine auf Winch belegen (3 Törns), dann Hebel öffnen
│   │   ├── Öffnet sich → Normal. Immer erst Winch belegen.
│   │   └── Öffnet sich nicht → Weiter
│   └── NEIN → Weiter
│
├── Ist der Mechanismus versalzen/verschmutzt?
│   ├── JA → Süßwasser-Spülung, Trockenschmierung
│   └── NEIN → Weiter
│
├── Ist der Hebel verbogen?
│   ├── JA → Hebel ersetzen (nicht richten!)
│   └── NEIN → Weiter
│
├── Ist die Leine zu dick für den Clutch?
│   ├── JA → Dünnere Leine verwenden
│   └── NEIN → Mechanismus intern blockiert → Clutch demontieren und reinigen/reparieren
```

### 9.3 Entscheidungsbaum: Welchen Clutch-Typ wählen?

```
Neuer Clutch gesucht
│
├── Anwendung?
│   ├── Fall/Reff → Rope Clutch (weiter unten)
│   ├── Schot (Jolle) → Cam Cleat
│   ├── Strecker/Niederholer (Last <200 kg) → Cam Cleat
│   └── Strecker (Last >200 kg) → Rope Clutch
│
├── [Cam Cleat] Bootsgröße?
│   ├── <6m → Junior (3–6 mm): CL205, Harken 150, RF5001
│   ├── 6–10m → Standard (6–10 mm): CL211, Harken 468, RF5010
│   ├── 10–14m → Major (8–14 mm): CL217, RF5025
│   └── >14m → Mega (10–16 mm): CL218, RF5033
│
├── [Rope Clutch] Budget?
│   ├── Niedrig → Spinlock XA, Lewmar D1, Viadana 57
│   ├── Mittel → Spinlock XAS, Lewmar D2, Antal VG
│   └── Hoch → Spinlock XTS/XX, Lewmar D3, Harken Extreme
│
└── [Rope Clutch] Priorität?
    ├── Geringe Bedienkraft → Antal V-Grip
    ├── Leinenschonung → Antal V-Grip, Spinlock XTS
    ├── Haltekraft → Spinlock XTS, Lewmar D3
    ├── Gewicht → Spinlock XTS
    └── Preis → Spinlock XA, Lewmar D1
```

### 9.4 Entscheidungsbaum: Starker Leinenverschleiß

```
Starker Leinenverschleiß im Clutch-Bereich
│
├── Ist die Leinenführung gerade? (kein seitlicher Versatz)
│   ├── NEIN → Fairlead oder Umlenkrolle installieren
│   └── JA → Weiter
│
├── Ist der Leinendurchmesser optimal? (oberes Drittel des Clutch-Bereichs)
│   ├── NEIN → Leinendurchmesser erhöhen
│   └── JA → Weiter
│
├── Sind Nocken/Cam beschädigt? (Grate, scharfe Kanten)
│   ├── JA → Nocken ersetzen
│   └── NEIN → Weiter
│
├── Wird die Leine häufig unter Last gefiert?
│   ├── JA → Normal bei häufigem Fieren. Leine regelmäßig wechseln.
│   │        Alternativen: Antal V-Grip (leinenschonendster Clutch)
│   └── NEIN → Weiter
│
└── Ist der Clutch sauber? (kein Salz, Sand)
    ├── NEIN → Clutch reinigen, regelmäßige Wartung einführen
    └── JA → Leinentyp prüfen: härterer Mantel wählen (Polyester geflochten)
```

### 9.5 Entscheidungsbaum: Decksmontage-Probleme

```
Probleme mit der Decksmontage
│
├── Schrauben drehen durch / ziehen nicht an
│   ├── Laminat beschädigt? → Schraubenloch ausbohren, Epoxy füllen, neu bohren
│   ├── Falsche Schraubengröße → Korrekte Schrauben verwenden (Hersteller-Angabe)
│   └── Kein Gegenhalter → Maschinenschrauben + Muttern + Backing Plate verwenden
│
├── Deck gibt unter Last nach (federt)
│   ├── Sandwich-Kern? → Kern im Befestigungsbereich durch Vollaminat ersetzen
│   ├── Laminat zu dünn? → Verstärkungslaminat aufbauen
│   └── Backing Plate fehlt/zu klein → Korrekte Backing Plate nachrüsten
│
├── Wasser dringt an Schraubenlöchern ein
│   ├── Kein Dichtmittel → Schrauben entfernen, mit Sikaflex 291 abdichten
│   ├── Dichtmittel ausgehärtet/gerissen → Altes Dichtmittel entfernen, neu abdichten
│   └── Riss im Laminat → Laminatreparatur vor Neumontage
│
└── Clutch verdreht sich unter Last
    ├── Zu wenige Schrauben → Zusätzliche Schrauben setzen (wenn Bohrung vorhanden)
    ├── Schrauben zu klein → Größere Schrauben verwenden
    └── Grundplatte zu klein → Größere Grundplatte oder Anti-Dreh-Stift verwenden
```

---

## 10. FAQ — Häufige Fragen

### F01: Was ist der Unterschied zwischen einem Cam Cleat und einem Rope Clutch?

**Antwort:** Ein Cam Cleat hat zwei federbelastete, gezahnte Backen, die eine Leine von oben aufnehmen und durch Keilwirkung halten. Ein Rope Clutch hat einen einzelnen exzentrischen Nocken, der durch einen Hebel betätigt wird und die Leine gegen eine geriffelte Grundplatte presst. Cam Cleats sind für geringere Lasten (bis ~600 kg SWL) und schnelles Belegen/Lösen gedacht (Schoten, Strecker). Rope Clutches sind für höhere Lasten (bis ~3.000 kg SWL) und ermöglichen kontrolliertes Fieren unter Last (Fallen, Reffleinen).

### F02: Kann ich einen Cam Cleat als Fallenstopper verwenden?

**Antwort:** Nur bedingt. Auf kleinen Jollen (bis ~6 m) können Cam Cleats für leichte Fallen (Spi-Fall, Genua-Fall) verwendet werden. Auf Kielbooten und Fahrtenyachten reicht die Haltekraft eines Cam Cleats für Fallen NICHT aus. Hier sind Rope Clutches zwingend erforderlich. Faustregel: Wenn die erwartete Fallenlast >200 kg beträgt, brauchen Sie einen Rope Clutch.

### F03: Welche Marke ist die beste bei Rope Clutches?

**Antwort:** Es gibt keine objektiv "beste" Marke — die Wahl hängt von den Prioritäten ab:
- **Spinlock XTS:** Bestes Gesamtpaket (Haltekraft, Gewicht, Ergonomie)
- **Antal V-Grip:** Geringste Bedienkraft, geringster Leinenverschleiß
- **Lewmar D2:** Bewährt, robust, günstig, größte Ersatzteilversorgung
- **Spinlock XAS:** Bestes Preis-Leistungs-Verhältnis

### F04: Muss ich eine Backing Plate unter dem Clutch haben?

**Antwort:** Bei Rope Clutches: JA, unbedingt. Bei Cam Cleats: abhängig von der Last und Decksdicke. Als Faustregel: Ab SWL 300 kg immer eine Backing Plate verwenden. Bei Sandwich-Decks: Immer, unabhängig von der Last. Die Backing Plate verteilt die Kraft und verhindert lokalen Kernkollaps.

### F05: Wie oft muss ich einen Rope Clutch warten?

**Antwort:** Für Wochenendsegler: mindestens 1× jährlich eine Grundwartung (Süßwasserspülung, Trockenschmierung, Sichtkontrolle). Für Vielsegeler: 2× jährlich. Für Regattasegler: 3× jährlich plus wöchentliche Sichtkontrolle. Die wichtigste Wartungsmaßnahme ist die regelmäßige Süßwasserspülung, die Salzrückstände entfernt.

### F06: Sind Dyneema-Leinen in Cam Cleats geeignet?

**Antwort:** Dyneema-Leinen MIT Polyester-Mantel sind geeignet. Mantellose Dyneema-Leinen (z.B. SK78 blank) sind NICHT geeignet — der wachsartige Kern bietet zu wenig Reibung. Die Leine würde durchrutschen. Mindestens ein dünner Mantel ist erforderlich. Alternativ: Micro-Zahn-Cam-Cleats verwenden, die besser mit glatten Leinen greifen.

### F07: Kann ich einen Spinlock-Clutch durch einen Lewmar ersetzen?

**Antwort:** Grundsätzlich ja, aber die Bohrlöcher stimmen in der Regel nicht überein. Ein Tausch erfordert neue Bohrlöcher und das Verschließen der alten mit Epoxy. Die Leistungsdaten (SWL, Leinendurchmesser) müssen mindestens gleichwertig sein. Am einfachsten ist der Tausch innerhalb derselben Hersteller-Serie (z.B. XAS → XTS).

### F08: Wie erkenne ich, ob mein Clutch verschlissen ist?

**Antwort:** Drei einfache Tests:
1. **Hebel-Test:** Hebel ohne Leine öffnen/schließen. Muss leichtgängig und ohne Spiel sein.
2. **Halte-Test:** Leine einlegen, mit Handkraft (ca. 20 kg) ziehen. Darf nicht rutschen.
3. **Visual Check:** Nocken-Profil prüfen. Zahnhöhe muss >50% des Neuzustands betragen.

### F09: Was kostet eine komplette Clutch-Bank für eine 12-m-Yacht?

**Antwort:**
- Budget (Spinlock XA oder Lewmar D1): €300–€500 für 6 Positionen
- Standard (Spinlock XAS oder Lewmar D2): €500–€800 für 6 Positionen
- Performance (Spinlock XTS oder Antal VG): €800–€1.400 für 6 Positionen
- Premium (Spinlock XX): €1.500–€2.500 für 6 Positionen
Plus: Backing Plates, Schrauben, Dichtmittel, Montagearbeit: €100–€300

### F10: Kann ich Cam Cleats auf einer T-Schiene montieren?

**Antwort:** Ja, mit speziellen Rail-Mount-Modellen. Clamcleat CL223 hat einen T-Schienen-Fuß für Standard-Lewmar/Harken-T-Schienen. Alternativ gibt es Universal-Adapter von verschiedenen Herstellern. Dies ermöglicht eine positionierbare Montage ohne Bohren.

### F11: Warum soll ich kein WD-40 auf Clutches verwenden?

**Antwort:** WD-40 ist ein Wasserverdränger und Kriechöl, kein Schmiermittel. Es verflüchtigt sich nach wenigen Tagen und hinterlässt einen klebrigen Film, der Sand und Salzkristalle bindet. Diese wirken dann wie Schleifpapier auf Leine und Mechanismus. Verwenden Sie ausschließlich marine-spezifische Trockenschmiermittel wie McLube SailKote, Spinlock Service Spray oder Boeshield T-9.

### F12: Was ist der Unterschied zwischen SWL und Breaking Load?

**Antwort:** Die Safe Working Load (SWL) ist die maximale Last, unter der der Beschlag dauerhaft und sicher betrieben werden darf. Die Breaking Load (BL) ist die Last, bei der der Beschlag versagt (bricht, sich dauerhaft verformt). Der Sicherheitsfaktor ist typisch 3:1 (BL = 3 × SWL). Sie sollten Ihren Clutch so dimensionieren, dass die erwartete maximale Leinenbelastung die SWL NICHT überschreitet.

### F13: Wie werden Clutch-Bänke korrekt montiert?

**Antwort:**
1. Position markieren (Abstand zur Winch: 300–500 mm)
2. Clutch-Bank als Bohrschablone verwenden
3. Alle Löcher vorbohren (1 mm kleiner als Schraubendurchmesser)
4. Jedes Loch mit verdünntem Epoxidharz versiegeln (Feuchtigkeitsschutz)
5. Backing Plate unter Deck positionieren
6. Sikaflex 291 oder 3M 4200 auf Grundplatte auftragen
7. Schrauben setzen und gleichmäßig anziehen
8. Dichtmittel aushärten lassen (24h)
9. Funktionstest mit Leine

### F14: Kann ein Clutch-Versagen gefährlich sein?

**Antwort:** JA. Ein versagender Clutch kann zu folgenden gefährlichen Situationen führen:
- Unkontrolliertes Fallen eines Segels (Fallenrutsch)
- Leine schießt durch den Clutch und verletzt Crewmitglieder (Peitscheneffekt)
- Kontrollverlust über das Boot bei schwerem Wetter
- Ausgerissene Decksmontage kann Rumpfintegrität gefährden
Deshalb: Regelmäßige Wartung und korrekte Dimensionierung sind sicherheitsrelevant.

### F15: Welcher Cam Cleat für ILCA/Laser?

**Antwort:** Für die Laser/ILCA-Klasse sind Cam Cleats klassenrechtlich zugelassen. Die meisten Segler verwenden:
- **Harken 150 Micro** (Cunningham): 3–6 mm, 29 g
- **Harken 365 Carbo** (Baumniederholer/Outhaul): 6–10 mm, 45 g
- **Clamcleat CL205** (Junior, Budget-Alternative): 3–6 mm, 22 g

### F16: Wie viele Töne muss die Leine auf der Winch haben, bevor ich den Clutch öffne?

**Antwort:** Mindestens 3 volle Törns auf der Winch, bevor der Clutch unter Last geöffnet wird. Bei hohen Lasten (>500 kg erwartete Last): 4–5 Törns. NIEMALS einen Clutch unter Last öffnen, wenn die Leine nicht auf der Winch gesichert ist.

### F17: Gibt es Cam Cleats für Drahtseile?

**Antwort:** Ja, Clamcleat bietet spezielle Draht-Cam-Cleats an (CL260-Serie). Diese haben gehärtete Backen mit feinerem Zahnprofil, das für Edelstahl-Drahtseile und beschichtete Drähte optimiert ist. Standard-Cam-Cleats sind für Drahtseile NICHT geeignet — die Zähne werden beschädigt und der Draht wird nicht sicher gehalten.

### F18: Was ist besser: Einzelne Clutches oder eine Clutch-Bank?

**Antwort:** Clutch-Bänke haben folgende Vorteile: gemeinsame Backing Plate (einfachere Montage), geringeres Gesamtgewicht, sauberer optischer Eindruck. Einzelne Clutches bieten: flexiblere Positionierung, einfacheren Einzelaustausch. Für Standard-Installationen (Fallen + Reffleinen) sind Clutch-Bänke die bessere Wahl. Einzelne Clutches sind sinnvoll für separate Anwendungen (z.B. Achterstag-Strecker).

### F19: Können Cam Cleats auf Mast montiert werden?

**Antwort:** Ja, es gibt spezielle Mast-Cam-Cleats (z.B. Clamcleat CL207 mit seitlicher Einführung). Diese werden für Lazy Jacks, Topping Lift, Flaggfallen und ähnliche leicht belastete Leinen am Mast verwendet. Die Montage erfordert das Bohren in das Mastprofil — hier ist besondere Vorsicht geboten, um die Maststruktur nicht zu schwächen.

### F20: Wie entferne ich einen alten, festkorrodierten Clutch?

**Antwort:**
1. Schraubenköpfe mit Kriechöl behandeln (Liquid Wrench, nicht WD-40 am Clutch selbst)
2. 15 Minuten einwirken lassen
3. Schlagschraubendreher verwenden (löst festsitzende Schrauben durch Schlagimpuls)
4. Bei Edelstahl-Schrauben in Aluminium: Wärme kann helfen (Heißluftpistole auf Schraubenkopf)
5. Wenn nichts hilft: Schraubenkopf abbohren und Schaft von unten austreiben
6. Alte Bohrlöcher immer mit Epoxy verschließen vor Neumontage

### F21: Sind teure Clutches wirklich besser als günstige?

**Antwort:** In der Regel: ja, aber nicht proportional zum Preisaufschlag. Der größte Qualitätssprung liegt zwischen Billigprodukten (Zamak-Guss, keine Marke) und Marken-Einstiegsprodukten (Spinlock XA, Lewmar D1). Danach werden die Unterschiede feiner: bessere Ergonomie, geringerer Leinenverschleiß, präzisere Fertigung, leichteres Gewicht. Für Fahrtensegler bieten Mittelklasse-Produkte (XAS, D2, V-Grip) das beste Preis-Leistungs-Verhältnis.

### F22: Was passiert, wenn ich einen Clutch mit zu dicker Leine verwende?

**Antwort:** Der Clutch schließt nicht vollständig. Der Nocken/Cam kann die Leine nicht korrekt klemmen. Im besten Fall hält die Leine schlecht, im schlimmsten Fall:
- Der Hebelmechanismus wird beschädigt (verbogener Hebel)
- Der Nocken bricht (Überlastung des Drehpunkts)
- Die Leine wird beim Schließen eingeklemmt und lässt sich nicht mehr lösen

### F23: Gibt es Clutches mit eingebautem Leinenzähler?

**Antwort:** Nicht serienmäßig. Es gibt jedoch nachrüstbare Leinenzähler-Systeme (z.B. Spinlock ERS oder separate Leinenzähler von Nasa Marine), die an der Clutch-Basis oder am Fairlead montiert werden. Für elektronische Systeme: Hallsensor-basierte Leinenzähler an der Umlenkrolle vor dem Clutch sind die zuverlässigste Lösung.

### F24: Wie beeinflusst die Temperatur die Clutch-Funktion?

**Antwort:** Extreme Temperaturen können die Funktion beeinflussen:
- **Kälte (<0°C):** Vereiste Clutches können blockieren. Federn werden steifer. Kunststoff-Teile werden spröder. Lösung: Enteisungsspray, Süßwasser-Spülung vor dem Einwintern.
- **Hitze (>40°C):** UV-beschleunigt die Alterung von Kunststoff-Teilen. Federn können bei Dauerhitze an Spannkraft verlieren. Aluminium-Gehäuse sind weniger betroffen.

### F25: Kann ich Clutches verschiedener Hersteller auf einer Bank mischen?

**Antwort:** Nein, Clutch-Bänke sind herstellerspezifisch. Sie können keine Spinlock-Clutches auf eine Lewmar-Bank setzen und umgekehrt. Wenn Sie Clutches verschiedener Hersteller verwenden möchten, müssen Sie diese als Einzelmodule montieren. Innerhalb einer Hersteller-Serie können Sie jedoch verschiedene Größen mischen (z.B. Spinlock XAS 0612 + XAS 0614 auf derselben Bank, sofern verfügbar).

---

## 11. Glossar

### A

**Acetal (POM/Delrin):**
Technischer Kunststoff mit hoher Festigkeit, geringem Reibungskoeffizienten und guter Dimensionsstabilität. Wird für Nocken, Buchsen und Gehäuseteile in Cam Cleats und Clutches verwendet. Selbstschmierend und korrosionsbeständig.

**Anodisierung (Eloxierung):**
Elektrochemisches Verfahren zur Erzeugung einer harten Oxidschicht auf Aluminium. Hart-Eloxierung (Typ III) erzeugt eine 25–50 µm dicke Schutzschicht, die die Verschleißfestigkeit und Korrosionsbeständigkeit drastisch erhöht. Standard bei marine Aluminium-Cam-Cleats.

### B

**Backing Plate:**
Verstärkungsplatte unter Deck, die die Schraubenkräfte auf eine größere Fläche verteilt. Zwingend erforderlich bei Rope Clutches auf Sandwich-Decks. Material: Edelstahl 316L (3–5 mm) oder Aluminium (5–8 mm).

**Breaking Load (BL):**
Die Last, bei der ein Beschlag versagt (bricht oder sich dauerhaft verformt). In der Regel 3× die Safe Working Load (SWL).

**Bullseye:**
Ringförmiger Fairlead aus Kunststoff oder Metall, der eine Leine in einer bestimmten Richtung führt, ohne Reibung zu erzeugen. Häufig vor Cam Cleats montiert.

### C

**Cam (Nocken):**
Das exzentrisch geformte Klemmelement, das die Leine gegen die Grundplatte oder die gegenüberliegende Backe presst. In Cam Cleats: zwei gegenläufige Cams. In Rope Clutches: ein einzelner Cam, der durch einen Hebel betätigt wird.

**Cam Cleat (Curry-Klemme):**
Klemme mit zwei federbelasteten, gezahnten Backen, die eine Leine durch Keilwirkung halten. Schnelles Einlegen (von oben) und Lösen (nach oben ziehen).

**Clutch-Bank:**
Zusammenfassung mehrerer Rope Clutches auf einer gemeinsamen Grundplatte. Verfügbar in 2er, 3er, 4er und 6er Konfigurationen.

### D

**Dyneema:**
Ultrahochfestes Polyethylen (UHMWPE). Verwendet als Leinen-Kern für höchste Festigkeit bei geringstem Gewicht. Glatte Oberfläche — erfordert Polyester-Mantel für Grip in Cam Cleats.

### E

**Einlaufwinkel:**
Der Winkel, unter dem eine Leine in einen Cam Cleat oder Clutch einläuft. Kritischer Parameter für die Haltekraft. Optimaler Bereich: 0–15° (Cam Cleat), 5–12° aufwärts (Rope Clutch).

**Exzentrizität:**
Das Maß der Abweichung der Nocken-Geometrie von einem perfekten Kreis. Bestimmt die Selbstverstärkung der Klemmung und das Übersetzungsverhältnis.

### F

**Fairlead:**
Leinenführung vor einem Cam Cleat oder Clutch, die den korrekten Einlaufwinkel sicherstellt. Kann als einfache Öse, als Rollenfairlead oder als integrierter Bestandteil des Clutches ausgeführt sein.

**Fieren:**
Das kontrollierte Nachlassen einer Leine unter Last. Mit Rope Clutches durch teilweises Öffnen des Hebels möglich. Mit Cam Cleats nicht möglich (nur komplettes Freigeben).

### G

**Galvanische Korrosion:**
Elektrochemische Korrosion, die entsteht, wenn zwei verschiedene Metalle in Anwesenheit eines Elektrolyten (Salzwasser) in Kontakt stehen. Kritisch bei Aluminium-Clutch auf Edelstahl-Backing-Plate ohne Isolation.

**GFK/FRP:**
Glasfaserverstärkter Kunststoff. Standard-Decksmaterial auf Yachten. Relevant für Montage-Anforderungen von Clutches und Cam Cleats.

### H

**Haltekraft:**
Die maximale Kraft, die ein Cam Cleat oder Clutch auf eine Leine ausüben kann, bevor die Leine rutscht. Abhängig von Nocken-Geometrie, Federkraft, Leinentyp und -durchmesser.

**Hart-Eloxierung:**
Spezielle Form der Anodisierung mit besonders dicker und harter Oxidschicht (25–50 µm, Typ III). Deutlich verschleißfester als Standard-Eloxierung.

### J

**Jammer:**
Englischer Fachbegriff für Rope Clutch / Fallenstopper. Im deutschen Sprachraum weniger gebräuchlich.

### K

**Keilwinkel:**
Der Winkel der Cam-Cleat-Backen-Geometrie, der die Selbstverstärkung bestimmt. Typisch 12–18°. Steilerer Winkel = höhere Klemmkraft, aber schwierigeres Lösen.

**Kernkompression:**
Eindrücken des Kernmaterials (PVC-Schaum, Balsa) in Sandwich-Laminaten unter Punktlast. Kritisch bei der Montage von Rope Clutches ohne korrekte Decksverstärkung.

### L

**Leinenschlag:**
Seitliches Ausschlagen einer Leine beim Lösen unter Last. Kann zu Verletzungen führen. Moderne Clutches haben Anti-Leinenschlag-Führungen.

**Line Stopper (Leinenstopper):**
Ältere Bauform eines Leinenklemmers, bei dem ein Hebelmechanismus die Leine gegen eine Grundplatte presst. Heute weitgehend durch Rope Clutches ersetzt.

### M

**McLube SailKote:**
Marine-Trockenschmiermittel auf Basis von Trockenfilmschmierstoffen. Standard-Empfehlung für die Schmierung von Cam Cleats, Clutches und anderen Decksbeschlägen.

### N

**Nocken:**
Siehe "Cam". Das exzentrisch geformte Klemmelement in Rope Clutches und Cam Cleats.

### P

**PTFE (Teflon):**
Polytetrafluorethylen. Verwendet als Trockenfilmschmierstoff in Marine-Sprays. Extrem niedriger Reibungskoeffizient, wasserabweisend.

### R

**Release-Under-Load:**
Die Kraft, die aufgebracht werden muss, um einen Clutch unter Last zu öffnen. Niedrigere Werte sind wünschenswert. Antal V-Grip hat die geringste Release-Under-Load-Kraft am Markt.

**Rope Clutch (Fallenstopper):**
Mechanische Klemme mit exzentrischem Nocken und Hebelbetätigung. Für hohe Lasten (Fallen, Reffleinen) konzipiert. Ermöglicht kontrolliertes Fieren.

### S

**Safe Working Load (SWL):**
Die maximale Last, unter der ein Beschlag dauerhaft und sicher betrieben werden darf. Typisch: BL / 3 (Sicherheitsfaktor 3:1).

**Sandwich-Laminat:**
Decksbauweise mit zwei GFK-Schichten und einem leichten Kernmaterial (PVC-Schaum, Balsa, Nomex-Wabe) dazwischen. Erfordert besondere Verstärkung bei Montage von Hochlast-Beschlägen.

**Schwenkfuß (Swivel Base):**
Drehbare Grundplatte für Cam Cleats, die sich automatisch zur Leinenrichtung ausrichtet.

### T

**T-Schiene (T-Track):**
Aluminium-Profilschiene für verschiebbare Decksbeschläge. Standard-Profile: Lewmar Größe 1/2/3, Harken Standard/Hi-Load.

**Trockenschmierung:**
Schmiermethode ohne flüssige Öle oder Fette. Verwendet PTFE, Molybdändisulfid oder Wachsfilme. Vorteil: Bindet keinen Sand/Staub. Standard für marine Decksbeschläge.

### V

**V-Grip:**
Patentiertes Klemmprofilsystem von Antal. Die Leine wird in eine V-förmige Rinne gedrückt. Ergibt besonders gleichmäßige Kraftverteilung und minimalen Leinenverschleiß.

**Vectran:**
Hochfeste Flüssigkristallpolymer-Faser (LCP) für Leinen. Ähnliche Festigkeit wie Dyneema, aber besserer Grip in Klemmen wegen rauerer Oberfläche.

### W

**Winch:**
Seilwinde zum Einholen und Halten von Leinen. Arbeitet mit dem Rope Clutch zusammen: Winch zum Einholen, Clutch zum Halten.

### Z

**Zahnprofil:**
Die Form und Anordnung der Zähne auf Cam-Cleat-Backen und Clutch-Nocken. Drei Haupttypen: V-Zähne (Standard), Rund-Zähne (leinenschonend), Mikro-Zähne (Hochleistung).

**Zamak:**
Zinklegierung (Zink-Aluminium-Magnesium-Kupfer), die für billige Guss-Beschläge verwendet wird. Für den Marineeinsatz NICHT geeignet — korrodiert schnell in Salzwasser. Erkennbar am höheren Gewicht und der grau-matten Oberfläche.

---

## 12. Schnell-Referenz

### 12.1 Cam Cleat Auswahl — Kurzübersicht

| Leine (mm) | Junior (3–6) | Standard (6–10) | Major (8–14) | Mega (10–16) |
|------------|-------------|-----------------|-------------|-------------|
| Budget | CL205 (€12) | CL211 (€18) | CL217 (€28) | CL218 (€42) |
| Performance | Harken 150 (€22) | Harken 468 (€38) | RF5025 (€32) | RF5033 (€42) |
| Premium | RF5400 (€25) | RF5420 (€38) | CL717 Inox (€65) | — |

### 12.2 Rope Clutch Auswahl — Kurzübersicht

| Bootslänge | Budget | Standard | Performance | Premium |
|------------|--------|----------|-------------|---------|
| 8–10 m | XA 0612 (€55) | XAS 0612 (€70) | XTS 0612 (€120) | — |
| 10–12 m | XA 0612 (€55) | XAS 0614 (€85) | XTS 0614 (€140) | Antal VG12 (€115) |
| 12–14 m | D1 8-12 (€65) | D2 8-12 (€85) | XTS 0614 (€140) | Antal VG14 (€140) |
| 14–16 m | D2 10-14 (€100) | D3 10-14 (€140) | XTS 0816 (€180) | XX 0814 (€280) |
| 16–18 m | D3 10-14 (€140) | D3 12-16 (€180) | XX 1016 (€340) | XX 1218 (€410) |

### 12.3 Wartungs-Checkliste (Kurzfassung)

- [ ] Süßwasserspülung nach jedem Salzwasser-Törn
- [ ] Vierteljährlich: Sichtkontrolle aller Cam Cleats und Clutches
- [ ] Jährlich: Trockenschmierung (McLube SailKote)
- [ ] Jährlich: Schrauben-Drehmoment prüfen
- [ ] Jährlich: Federn auf Ermüdung prüfen
- [ ] Alle 3–5 Jahre: Nocken/Cam und Federn ersetzen
- [ ] Leine im Clutch-Bereich alle 2–3 Saisons ersetzen

### 12.4 Wichtige Drehmomente

| Schraube | Drehmoment (Nm) | Anwendung |
|----------|-----------------|-----------|
| M4 | 3–4 | Junior Cam Cleats |
| M5 | 5–6 | Standard Cam Cleats, Lewmar D1 |
| M6 | 8–10 | Standard Clutches (Spinlock XAS/XTS, Antal VG) |
| M8 | 15–18 | Heavy-Duty Clutches (Lewmar D3, Spinlock XX) |

### 12.5 Notfall-Maßnahmen

**Clutch blockiert unter Last:**
1. Leine auf Winch belegen (3+ Törns)
2. Winch dichtholen (Last auf Winch nehmen)
3. Clutch-Hebel öffnen
4. Falls blockiert: Schraubendreher als Hebelverlängerung nutzen (Vorsicht!)

**Cam Cleat versagt (Leine rutscht):**
1. Leine sofort auf nächste Klampe oder Winch belegen
2. Sicherheitsabstand — Leinenende kann peitschen
3. Cam Cleat außer Betrieb nehmen, ersetzen

---

## ANHANG A — Fallstudie: Cam Cleat Versagen bei Regatta

### A.1 Ausgangslage

**Boot:** 49er Skiff, Carbon-Rumpf
**Cam Cleat:** Harken 150 Micro (Cunningham)
**Alter:** 3 Saisons (ca. 500 Betriebsstunden)
**Leine:** 4 mm Dyneema SK78 mit Polyester-Mantel

### A.2 Fehlerbild

Während einer Regatta bei 18–22 Knoten Wind löste sich die Cunningham-Leine wiederholt aus dem Cam Cleat. Das Unterliek wurde unkontrolliert lose, was zu erheblichem Leistungsverlust führte.

### A.3 Diagnose

1. Cam-Backen-Zahnhöhe: 40% des Neuzustands (verschlissen)
2. Federn: Federkraft ca. 50% des Neuzustands
3. Leine: Mantel im Cam-Bereich stark abgerieben, Dyneema-Kern sichtbar
4. Einlaufwinkel: 25° (zu steil)

### A.4 Ursachenanalyse

Kombination aus verschlissenen Backen, ermüdeten Federn und abgeriebenem Leinenmantel. Der steile Einlaufwinkel verschärfte das Problem. Bei Leichtwind (<12 Knoten) funktionierte der Cam Cleat noch, bei Starkwind nicht mehr.

### A.5 Behebung

1. Harken 150 Micro durch neues Exemplar ersetzt
2. Fairlead-Block vorgeschaltet (Einlaufwinkel jetzt 10°)
3. Leine durch 4 mm Marlow Excel Racing (dickerer Mantel) ersetzt
4. Wartungsplan: Cam-Backen und Federn nach jeder zweiten Saison ersetzen

### A.6 AYDI-Bewertung

- **Confidence:** documented (Fehlerbild und Ursache eindeutig)
- **Severity:** Mittel (Leistungsverlust, kein Sicherheitsrisiko)
- **Module:** materials (Leinenverschleiß), ergonomics (Einlaufwinkel)

---

## ANHANG B — Fallstudie: Fallenstopper-Upgrade auf Blauwasseryacht

### B.1 Ausgangslage

**Boot:** Hallberg-Rassy 42, Baujahr 2008
**Bestehende Clutches:** Lewmar D2 8-12, 2× 3er Bank
**Problem:** Release unter Last zu schwer für Allein- und Paarsegler
**Anforderung:** Leichtere Bedienung, gleiche oder höhere SWL

### B.2 Lösungsoptionen

| Option | Modell | SWL | Release (50%) | Preis (2×3er) | Bewertung |
|--------|--------|-----|---------------|---------------|-----------|
| A | Spinlock XCS 0614/3 | 1.000 kg | 10–14 N | €520–€660 | Empfohlen |
| B | Antal VG12T | 1.000 kg | 8–12 N | €650–€840 | Beste Ergonomie |
| C | Spinlock XTS 0614/3 | 1.100 kg | 10–15 N | €790–€1.000 | Höchste Leistung |

### B.3 Durchführung

Option A (Spinlock XCS 0614/3) wurde gewählt. Montageaufwand:
1. Alte Lewmar D2-Bänke demontiert
2. Alte Bohrlöcher mit verdicktem Epoxy verschlossen
3. Neue Bohrschablone angelegt
4. Sandwich-Kern im Befestigungsbereich mit Epoxy verfüllt
5. Neue Backing Plates (Edelstahl 316L, 5 mm) angefertigt
6. Spinlock XCS montiert mit Sikaflex 291

**Arbeitszeit:** 2 Arbeitstage (1 Person)
**Materialkosten:** €620 (2× XCS 0614/3) + €80 (Backing Plates, Epoxy, Schrauben, Dichtmittel)

### B.4 Ergebnis

Die Release-Kraft wurde um ca. 30% reduziert. Die Eignerin (65 Jahre, Arthritis in den Händen) kann nun alle Clutches unter Last öffnen. Die SWL wurde von 900 kg auf 1.000 kg erhöht.

### B.5 AYDI-Bewertung

- **Confidence:** measured (vorher/nachher Release-Kräfte gemessen)
- **Module:** ergonomics (Bedienkraft), service_patterns (Upgrade-Pfad)

---

## ANHANG C — Fallstudie: Clutch-Bank Redesign auf Performance Cruiser

### C.1 Ausgangslage

**Boot:** J/122, 12.2m, Baujahr 2015
**Problem:** Bestehende 3er Clutch-Bänke (Spinlock XAS) reichen nicht für erweiterte Segelgarderobe (Code-0, A-Spi, Staysail)
**Anforderung:** 5 Positionen pro Seite, davon 2 für hochbelastete Fallen (Groß, Code-0)

### C.2 Lösung

Mixed-Clutch-Konfiguration mit individuellen Positionen:

**Backbord (5 Positionen):**
1. Großfall: Spinlock XTS 0614 (SWL 1.100 kg)
2. Reff 1: Spinlock XAS 0614 (SWL 800 kg)
3. Reff 2: Spinlock XAS 0612 (SWL 700 kg)
4. Reff 3: Spinlock XAS 0612 (SWL 700 kg)
5. Topping Lift: Spinlock XA 0612 (SWL 500 kg)

**Steuerbord (5 Positionen):**
1. Code-0 Fall: Spinlock XTS 0614 (SWL 1.100 kg)
2. Genua Fall: Spinlock XAS 0614 (SWL 800 kg)
3. A-Spi Fall: Spinlock XAS 0612 (SWL 700 kg)
4. Staysail Fall: Spinlock XAS 0612 (SWL 700 kg)
5. Reserve: Spinlock XA 0612 (SWL 500 kg)

### C.3 Montage

Da keine vorgefertigte 5er-Bank verfügbar war, wurden individuelle Clutches auf einer maßgefertigten Aluminium-Grundplatte (6 mm, eloxiert) montiert. Die Grundplatte wurde auf einer CNC-Fräse gefertigt.

**Gesamtkosten:** €1.850 (Clutches: €1.420, Grundplatten: €280, Montage/Material: €150)

### C.4 AYDI-Bewertung

- **Confidence:** measured (Konfiguration spezifisch dimensioniert)
- **Module:** production (Montageaufwand), cost (Gesamtkosten), ergonomics (Cockpit-Layout)

---

## ANHANG D — Fallstudie: Korrosion an Aluminium-Cam-Cleats

### D.1 Ausgangslage

**Boot:** Bavaria 38, Mittelmeer-Stationierung (Kroatien), Baujahr 2016
**Beschläge:** 4× Clamcleat CL211 Mk2 (Aluminium, hart-eloxiert)
**Stationierungsdauer:** 8 Jahre, davon 6 im Wasser (April–Oktober)

### D.2 Fehlerbild

Alle vier Cam Cleats zeigten nach 8 Jahren starke weiße Ablagerungen (Aluminiumoxid-Korrosion). Zwei der vier Cam Cleats hatten schwergängige Backen. Die Federn eines Cam Cleats waren korrodiert und brüchig.

### D.3 Ursachenanalyse

1. Eloxierung durch mechanische Beanspruchung (Leinen) stellenweise abgetragen
2. Edelstahl-Schrauben (M5, 316L) direkt in Aluminium-Gehäuse: galvanische Korrosion
3. Keine regelmäßige Süßwasserspülung (Boot lag permanent im Wasser)
4. Federn aus Edelstahl 304 (nicht 316L) — galvanische Korrosion mit Aluminium

### D.4 Behebung

1. Alle 4 Cam Cleats durch neue CL211 Mk2 AN ersetzt
2. Nylon-Unterlegscheiben zwischen Schrauben und Gehäuse
3. Tef-Gel auf allen Kontaktflächen (galvanische Isolation)
4. Eigner-Anweisung: Monatliche Süßwasserspülung

### D.5 AYDI-Bewertung

- **Confidence:** documented (typisches Alterungsmuster, gut dokumentiert)
- **Module:** materials (Korrosion), service_patterns (Wartungsmangel)

---

## ANHANG E — Fallstudie: Line Stopper Nachrüstung Motoryacht

### E.1 Ausgangslage

**Boot:** Motoryacht Princess V48, Baujahr 2010
**Problem:** Festmacherleinen rutschen bei Schwell in der Marina
**Anforderung:** Zuverlässiges Halten der Festmacherleinen ohne permanente Klampenbelegung

### E.2 Lösung

Nachrüstung von 4× Cam Cleats (Clamcleat CL218 Mega, 10–16 mm) als zusätzliche Sicherung der Festmacherleinen. Die Leinen werden wie bisher auf den Klampen belegt, aber zusätzlich durch einen Cam Cleat gesichert.

### E.3 Ergebnis

Die Cam Cleats verhindern zuverlässig das Losarbeiten der Festmacherleinen bei Schwell. Die Bedienung ist einfach genug für alle Crewmitglieder. Kosten: €210 (4× CL218 + Schrauben + Dichtmittel).

### E.4 AYDI-Bewertung

- **Confidence:** documented
- **Module:** ergonomics (Bedienbarkeit), compliance (Festmachersicherheit)

---

## ANHANG F — Fallstudie: Spinlock XTS vs. Lewmar D2 Langzeittest

### F.1 Ausgangslage

**Boot:** Dehler 42, Ostsee-Revier
**Testdauer:** 5 Saisons (2021–2025)
**Konfiguration:** Backbord: Spinlock XTS 0614/3 — Steuerbord: Lewmar D2 10-14/3

### F.2 Testprotokoll

Beide Clutch-Bänke wurden identisch genutzt (gleiche Fallen, gleiche Leinen, gleiche Wartung). Jährliche Leistungsmessung:
- Haltekraft (Zugtest mit Federzugwaage bei 500 kg)
- Release-Kraft (Dynamometer am Hebel)
- Leinenverschleiß (Manteldurchmesser-Messung)

### F.3 Ergebnisse nach 5 Saisons

| Parameter | Spinlock XTS (Jahr 5) | Lewmar D2 (Jahr 5) |
|-----------|----------------------|---------------------|
| Haltekraft-Verlust | 8% | 12% |
| Release-Kraft-Anstieg | 15% | 25% |
| Leinenverschleiß (Mantel) | 0.3 mm Ø-Verlust | 0.5 mm Ø-Verlust |
| Korrosion | Keine sichtbare | Leichte Eloxierungs-Aufhellung |
| Federspannung | 85% des Neuzustands | 75% des Neuzustands |
| Ersatzteile benötigt | Keine | 1× Feder-Kit (Jahr 4) |

### F.4 Fazit

Der Spinlock XTS zeigte nach 5 Saisons weniger Verschleiß, geringeren Haltekraftverlust und bessere Release-Eigenschaften. Der Lewmar D2 war jedoch zuverlässig und ohne Ausfall. Der Preisunterschied (XTS ca. 65% teurer als D2) amortisiert sich über die längere Lebensdauer.

### F.5 AYDI-Bewertung

- **Confidence:** measured (quantitative Langzeitmessungen)
- **Module:** materials (Verschleiß), cost (Lebenszyklus-Kosten)

---

## ANHANG G — Fallstudie: Clamcleat-Bruch bei Opti-Regatta

### G.1 Ausgangslage

**Boot:** Optimist, Segelverein
**Cam Cleat:** Clamcleat CL800 (Composite, Junior)
**Alter:** 2 Saisons
**Leine:** 4 mm Standard-Polyester (Schot)

### G.2 Fehlerbild

Während einer Opti-Regatta brach eine Cam-Cleat-Backe aus dem Gehäuse. Die Schot konnte nicht mehr geklemmt werden. Das Kind konnte das Manöver nicht abschließen.

### G.3 Ursachenanalyse

1. Composite-Gehäuse durch UV-Strahlung geschwächt (Boot lag permanent im Freien)
2. Überlastung durch ruckartiges Einlegen der Schot (Schockbelastung)
3. Billig-Composite-Material ohne ausreichende UV-Stabilisierung

### G.4 Behebung

1. Alle Composite-Cam-Cleats im Vereinsbestand durch Aluminium-Modelle (CL205AN) ersetzt
2. Boote werden nach dem Training unter Persenning gelagert (UV-Schutz)
3. Jährliche Inspektion aller Cam Cleats durch Trainer

### G.5 AYDI-Bewertung

- **Confidence:** documented
- **Module:** materials (UV-Degradation), compliance (Kindersicherheit)

---

## ANHANG H — Fallstudie: Antal V-Grip Installation Superyacht

### H.1 Ausgangslage

**Boot:** Wally 77, Carbon-Rumpf, Superyacht
**Anforderung:** Clutch-System für 8 Fallen und 4 Strecker
**Spezialität:** Minimale Bedienkraft (professionelle Crew + Eigner mit begrenzter Erfahrung)

### H.2 Konfiguration

**Backbord (6 Positionen):**
1. Großfall: Antal VG14S (SWL 1.200 kg)
2. Genua-Fall: Antal VG14S (SWL 1.200 kg)
3. Code-0 Fall: Antal VG14S (SWL 1.200 kg)
4. Reff 1: Antal VG12S (SWL 1.000 kg)
5. Reff 2: Antal VG12S (SWL 1.000 kg)
6. Reff 3: Antal VG10S (SWL 800 kg)

**Steuerbord (6 Positionen):**
1. Spi-Fall: Antal VG12S (SWL 1.000 kg)
2. Staysail-Fall: Antal VG10S (SWL 800 kg)
3. Achterstag: Antal VG14S (SWL 1.200 kg)
4. Babystag: Antal VG12S (SWL 1.000 kg)
5. Cunningham: Antal VG10S (SWL 800 kg)
6. Reserve: Antal VG10S (SWL 800 kg)

### H.3 Ergebnis

Alle 12 Clutches funktionieren einwandfrei. Die geringe Release-Kraft des V-Grip-Systems ermöglicht dem Eigner die Bedienung aller Fallen ohne professionelle Crew. Die Installation wurde von Antals technischem Team begleitet.

**Gesamtkosten:** €3.200 (12 Clutches) + €1.800 (Carbon-Backing-Plates, Montage)

### H.4 AYDI-Bewertung

- **Confidence:** measured (professionelle Installation, dokumentierte Leistungswerte)
- **Module:** ergonomics (Bedienkraft), cost (Superyacht-Budget), brand_dna (Antal/Wally)

---

## ANHANG I — Confidence-Mapping

### I.1 Confidence-Zuordnung für Cam Cleat und Klemmen-Befunde

| Befund | Structured Conf. | Visual Conf. | Fusions-Gewicht |
|--------|-----------------|-------------|-----------------|
| SWL-Angabe vorhanden | measured | — | 1.0 struct |
| SWL geschätzt nach Bootsgröße | estimated | — | 0.7 struct |
| Zahnverschleiß sichtbar | — | visual_high | 0.65 visual |
| Korrosion sichtbar | — | visual_high | 0.65 visual |
| Falsche Montageorientierung | calculated | visual_medium | 0.5/0.5 |
| Fehlende Backing Plate | — | visual_low | nur Hinweis |
| Leinenverschleiß | — | visual_medium | 0.65 visual |
| Clutch-Typ identifiziert | — | visual_high | 0.8 visual |
| Clutch-Marke identifiziert | — | visual_medium | 0.6 visual |
| Clutch-Bank-Konfiguration | calculated | visual_high | 0.4/0.6 |

### I.2 Nicht beurteilbare Befunde

Folgende Befunde können visuell NICHT zuverlässig beurteilt werden und erhalten `visual_insufficient`:

- Federkraft / Federspannung
- Interne Korrosion
- Haltekraft unter Last
- Release-Under-Load-Kraft
- Backing-Plate-Dimensionierung (unter Deck nicht sichtbar)
- Schrauben-Drehmoment
- Sandwich-Kern-Zustand

---

## ANHANG J — AYDI-Integration (Pydantic-Modelle)

### J.1 Basis-Modelle

```python
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class CamCleatType(str, Enum):
    """Types of cam cleats."""
    FIXED = "fixed"
    SWIVEL = "swivel"
    WITH_FAIRLEAD = "with_fairlead"
    RACING = "racing"
    RAIL_MOUNT = "rail_mount"
    WIRE = "wire"
    MAST_MOUNT = "mast_mount"


class RopeClutchType(str, Enum):
    """Types of rope clutches."""
    STANDARD = "standard"
    CRUISING = "cruising"
    PERFORMANCE = "performance"
    EXTREME = "extreme"
    LINE_STOPPER = "line_stopper"


class CleatMaterial(str, Enum):
    """Materials used in cam cleats and clutches."""
    ALUMINUM_ANODIZED = "aluminum_anodized"
    ALUMINUM_CNC = "aluminum_cnc"
    STAINLESS_316L = "stainless_316l"
    STAINLESS_304 = "stainless_304"
    COMPOSITE_GFN = "composite_gfn"
    CARBON_POLYMER = "carbon_polymer"
    ACETAL_POM = "acetal_pom"
    ZAMAK = "zamak"


class CleatManufacturer(str, Enum):
    """Known manufacturers of cam cleats and clutches."""
    SPINLOCK = "spinlock"
    CLAMCLEAT = "clamcleat"
    HARKEN = "harken"
    LEWMAR = "lewmar"
    RONSTAN = "ronstan"
    ANTAL = "antal"
    SCHAEFER = "schaefer"
    RWO = "rwo"
    HOLT_ALLEN = "holt_allen"
    VIADANA = "viadana"
    UNKNOWN = "unknown"


class ConfidenceLevel(str, Enum):
    """AYDI confidence levels."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class LineType(str, Enum):
    """Types of lines/ropes used with cam cleats and clutches."""
    POLYESTER_BRAIDED = "polyester_braided"
    DYNEEMA_WITH_COVER = "dyneema_with_cover"
    DYNEEMA_BARE = "dyneema_bare"
    KEVLAR = "kevlar"
    VECTRAN = "vectran"
    POLYPROPYLENE = "polypropylene"
    NYLON = "nylon"
    WIRE = "wire"


class CleatApplication(str, Enum):
    """Application areas for cam cleats and clutches."""
    MAIN_HALYARD = "main_halyard"
    GENOA_HALYARD = "genoa_halyard"
    SPINNAKER_HALYARD = "spinnaker_halyard"
    CODE_ZERO_HALYARD = "code_zero_halyard"
    STAYSAIL_HALYARD = "staysail_halyard"
    REEF_LINE_1 = "reef_line_1"
    REEF_LINE_2 = "reef_line_2"
    REEF_LINE_3 = "reef_line_3"
    MAINSHEET = "mainsheet"
    JIB_SHEET = "jib_sheet"
    GENOA_SHEET = "genoa_sheet"
    SPINNAKER_SHEET = "spinnaker_sheet"
    CUNNINGHAM = "cunningham"
    BOOM_VANG = "boom_vang"
    BACKSTAY = "backstay"
    BABYSTAY = "babystay"
    TOPPING_LIFT = "topping_lift"
    TRAVELLER = "traveller"
    LAZY_JACKS = "lazy_jacks"
    MOORING_LINE = "mooring_line"
    OTHER = "other"


class FailurePattern(str, Enum):
    """Known failure patterns for cam cleats and clutches."""
    LINE_SLIPPING = "line_slipping"
    CAM_JAMMED = "cam_jammed"
    CLUTCH_NOT_HOLDING = "clutch_not_holding"
    LEVER_STIFF = "lever_stiff"
    DECK_MOUNT_FAILURE = "deck_mount_failure"
    ALUMINUM_CORROSION = "aluminum_corrosion"
    SPRING_FATIGUE = "spring_fatigue"
    LINE_WEAR = "line_wear"
    HOUSING_CRACK = "housing_crack"
    WRONG_ORIENTATION = "wrong_orientation"
    GALVANIC_CORROSION = "galvanic_corrosion"
    UV_DEGRADATION = "uv_degradation"
```

### J.2 Spezifikations-Modelle

```python
class CamCleatSpec(BaseModel):
    """Specification for a cam cleat."""

    model_config = {"from_attributes": True}

    manufacturer: CleatManufacturer
    model_number: str = Field(..., description="Manufacturer model number")
    cleat_type: CamCleatType
    line_diameter_min_mm: float = Field(..., ge=1.0, le=20.0)
    line_diameter_max_mm: float = Field(..., ge=1.0, le=20.0)
    swl_kg: float = Field(..., ge=0, description="Safe Working Load in kg")
    breaking_load_kg: Optional[float] = Field(
        None, ge=0, description="Breaking Load in kg"
    )
    weight_g: float = Field(..., ge=0, description="Weight in grams")
    material: CleatMaterial
    price_eur_min: Optional[float] = Field(None, ge=0)
    price_eur_max: Optional[float] = Field(None, ge=0)
    mounting_holes: int = Field(2, ge=1, le=6)
    mounting_screw_size: str = Field("M5", description="e.g. M4, M5, M6")
    has_fairlead: bool = False
    has_swivel: bool = False
    length_mm: Optional[float] = Field(None, ge=0)
    width_mm: Optional[float] = Field(None, ge=0)
    height_mm: Optional[float] = Field(None, ge=0)


class RopeClutchSpec(BaseModel):
    """Specification for a rope clutch / jammer."""

    model_config = {"from_attributes": True}

    manufacturer: CleatManufacturer
    model_number: str = Field(..., description="Manufacturer model number")
    clutch_type: RopeClutchType
    series: Optional[str] = Field(None, description="e.g. XAS, XTS, D2, V-Grip")
    line_diameter_min_mm: float = Field(..., ge=4.0, le=20.0)
    line_diameter_max_mm: float = Field(..., ge=4.0, le=20.0)
    swl_kg: float = Field(..., ge=0, description="Safe Working Load in kg")
    breaking_load_kg: Optional[float] = Field(
        None, ge=0, description="Breaking Load in kg"
    )
    weight_single_g: float = Field(..., ge=0, description="Weight of single unit in g")
    positions: int = Field(1, ge=1, le=8, description="Number of positions in bank")
    material_housing: CleatMaterial = CleatMaterial.ALUMINUM_ANODIZED
    material_cam: CleatMaterial = CleatMaterial.ACETAL_POM
    release_force_50pct_n_min: Optional[float] = Field(
        None, ge=0, description="Min release force at 50% SWL in N"
    )
    release_force_50pct_n_max: Optional[float] = Field(
        None, ge=0, description="Max release force at 50% SWL in N"
    )
    price_eur_min: Optional[float] = Field(None, ge=0)
    price_eur_max: Optional[float] = Field(None, ge=0)
    mounting_screws_per_position: int = Field(2, ge=1, le=6)
    mounting_screw_size: str = Field("M6", description="e.g. M5, M6, M8")
    has_fairlead: bool = True
    fairlead_adjustable: bool = False
    allows_vertical_mount: bool = False
    color_coded_levers: bool = False
    carbon_lever_option: bool = False
    width_per_position_mm: Optional[float] = Field(None, ge=0)
    depth_mm: Optional[float] = Field(None, ge=0)
    height_mm: Optional[float] = Field(None, ge=0)


class BackingPlateSpec(BaseModel):
    """Specification for a backing plate."""

    model_config = {"from_attributes": True}

    material: CleatMaterial
    thickness_mm: float = Field(..., ge=1.0, le=20.0)
    width_mm: float = Field(..., ge=20.0)
    length_mm: float = Field(..., ge=20.0)
    for_swl_max_kg: float = Field(..., ge=0)
```

### J.3 Analyse-Modelle

```python
class CamCleatCondition(str, Enum):
    """Condition assessment for cam cleats."""
    NEW = "new"
    GOOD = "good"
    FAIR = "fair"
    WORN = "worn"
    FAILED = "failed"
    NOT_ASSESSABLE = "not_assessable"


class CleatInstallationAssessment(BaseModel):
    """Assessment of a cam cleat or clutch installation."""

    model_config = {"from_attributes": True}

    location: str = Field(..., description="Location on the boat, e.g. 'port_clutch_bank_pos_1'")
    application: CleatApplication
    device_type: str = Field(..., description="'cam_cleat' or 'rope_clutch' or 'line_stopper'")
    manufacturer: Optional[CleatManufacturer] = None
    model_identified: Optional[str] = None
    condition: CamCleatCondition = CamCleatCondition.NOT_ASSESSABLE
    line_diameter_mm: Optional[float] = None
    line_type: Optional[LineType] = None
    line_condition: Optional[str] = None
    entry_angle_deg: Optional[float] = Field(
        None, ge=-90, le=90,
        description="Measured or estimated line entry angle in degrees"
    )
    lateral_offset_deg: Optional[float] = Field(
        None, ge=-45, le=45,
        description="Lateral line offset in degrees"
    )
    backing_plate_present: Optional[bool] = None
    mounting_secure: Optional[bool] = None
    failure_patterns: list[FailurePattern] = Field(default_factory=list)
    score: Optional[float] = Field(None, ge=0, le=100)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM
    notes_de: str = Field("", description="German-language assessment notes")
    suggestions_de: list[str] = Field(
        default_factory=list,
        description="German-language improvement suggestions"
    )


class CleatSystemAssessment(BaseModel):
    """Complete assessment of all cam cleats and clutches on a yacht."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = None
    boat_length_m: Optional[float] = None
    boat_type: Optional[str] = None
    assessment_date: datetime
    assessor: str = "AYDI"
    ai_model_version: str = Field(..., description="AI model version used")

    cam_cleats: list[CleatInstallationAssessment] = Field(default_factory=list)
    rope_clutches: list[CleatInstallationAssessment] = Field(default_factory=list)
    line_stoppers: list[CleatInstallationAssessment] = Field(default_factory=list)

    overall_score: Optional[float] = Field(None, ge=0, le=100)
    overall_confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM

    critical_findings_de: list[str] = Field(
        default_factory=list,
        description="Critical findings requiring immediate attention"
    )
    recommendations_de: list[str] = Field(
        default_factory=list,
        description="Prioritized improvement recommendations"
    )

    available: bool = True
    unavailable_reason: Optional[str] = None


class CleatDimensioningInput(BaseModel):
    """Input parameters for clutch/cleat dimensioning calculation."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=3.0, le=30.0)
    boat_type: str = Field(..., description="e.g. 'sailing_yacht', 'motor_yacht', 'dinghy'")
    application: CleatApplication
    line_diameter_mm: float = Field(..., ge=2.0, le=20.0)
    line_type: LineType = LineType.POLYESTER_BRAIDED
    expected_max_load_kg: Optional[float] = Field(
        None, ge=0, description="Expected maximum line load in kg"
    )
    safety_factor: float = Field(1.5, ge=1.0, le=4.0)
    budget: Optional[str] = Field(
        None, description="'budget', 'standard', 'performance', 'premium'"
    )
    priority: Optional[str] = Field(
        None,
        description="'low_release', 'line_protection', 'holding_power', 'weight', 'price'"
    )


class CleatDimensioningResult(BaseModel):
    """Result of clutch/cleat dimensioning calculation."""

    model_config = {"from_attributes": True}

    input_params: CleatDimensioningInput
    recommended_type: str = Field(
        ..., description="'cam_cleat' or 'rope_clutch'"
    )
    min_swl_kg: float = Field(..., ge=0)
    recommended_models: list[dict] = Field(
        default_factory=list,
        description="List of recommended models with specs and prices"
    )
    backing_plate_required: bool = False
    backing_plate_spec: Optional[BackingPlateSpec] = None
    fairlead_required: bool = False
    notes_de: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED


class CleatMaintenanceSchedule(BaseModel):
    """Maintenance schedule for cam cleats and clutches."""

    model_config = {"from_attributes": True}

    usage_profile: str = Field(
        ..., description="'weekend', 'frequent', 'racing', 'charter', 'bluewater'"
    )
    inspection_interval_months: int = Field(..., ge=1, le=12)
    basic_maintenance_per_year: int = Field(..., ge=1, le=12)
    overhaul_interval_years: int = Field(..., ge=1, le=10)
    spring_replacement_years: int = Field(..., ge=1, le=10)
    cam_replacement_years: int = Field(..., ge=1, le=15)
    line_replacement_seasons: int = Field(..., ge=1, le=5)
    annual_maintenance_cost_eur: Optional[float] = Field(None, ge=0)
    notes_de: list[str] = Field(default_factory=list)
```

### J.4 Scoring-Modell

```python
class CleatScoringWeights(BaseModel):
    """Scoring weights for cam cleat and clutch assessment."""

    model_config = {"from_attributes": True}

    condition_weight: float = Field(0.25, ge=0, le=1)
    sizing_weight: float = Field(0.20, ge=0, le=1)
    mounting_weight: float = Field(0.20, ge=0, le=1)
    line_compatibility_weight: float = Field(0.15, ge=0, le=1)
    maintenance_weight: float = Field(0.10, ge=0, le=1)
    ergonomics_weight: float = Field(0.10, ge=0, le=1)


class CleatScoreBreakdown(BaseModel):
    """Detailed score breakdown for a cam cleat or clutch."""

    model_config = {"from_attributes": True}

    condition_score: float = Field(0, ge=0, le=100)
    sizing_score: float = Field(0, ge=0, le=100)
    mounting_score: float = Field(0, ge=0, le=100)
    line_compatibility_score: float = Field(0, ge=0, le=100)
    maintenance_score: float = Field(0, ge=0, le=100)
    ergonomics_score: float = Field(0, ge=0, le=100)

    weighted_total: float = Field(0, ge=0, le=100)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM

    penalties: list[str] = Field(
        default_factory=list,
        description="List of score penalties applied"
    )
    bonuses: list[str] = Field(
        default_factory=list,
        description="List of score bonuses applied"
    )
```

---

## ANHANG K — AYDI Bewertungsschema für Cam Cleats und Klemmen

### K.1 Bewertungskriterien

| Kriterium | Gewicht | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|-----------|---------|------------|-----------|-----------|-----------|----------|
| Zustand | 25% | Neuwertig, keine Verschleißspuren | Guter Zustand, leichte Gebrauchsspuren | Deutlicher Verschleiß, funktionsfähig | Starker Verschleiß, eingeschränkte Funktion | Defekt, Versagen |
| Dimensionierung | 20% | SWL ≥ 2× Last, perfekter Ø-Bereich | SWL ≥ 1.5× Last, guter Ø-Bereich | SWL ≥ 1× Last, unterer Ø-Bereich | SWL knapp ausreichend | SWL unterschritten |
| Montage | 20% | Backing Plate, korrekt abgedichtet, perfekter Winkel | Backing Plate, abgedichtet, guter Winkel | Ohne Backing Plate, abgedichtet | Ohne Backing Plate, nicht abgedichtet | Lose, ausgerissen |
| Leinen-Kompatibilität | 15% | Optimaler Ø und Typ | Guter Ø, passender Typ | Am Rand des Ø-Bereichs | Falscher Ø oder Typ | Inkompatibel |
| Wartung | 10% | Frisch gewartet, geschmiert | Leichte Salz-Ablagerungen | Verschmutzt, funktionsfähig | Stark verschmutzt, schwergängig | Korrodiert, blockiert |
| Ergonomie | 10% | Perfekt erreichbar, leichte Bedienung | Gut erreichbar | Erreichbar, aber umständlich | Schwer erreichbar | Nicht erreichbar |

### K.2 Abzüge und Boni

**Abzüge:**
- Zamak-Material: -30 Punkte
- Fehlende Backing Plate bei Clutch: -20 Punkte
- Edelstahl 304 statt 316L: -15 Punkte
- Seitlicher Einlaufwinkel >10°: -15 Punkte
- Mantellose Dyneema-Leine in Cam Cleat: -20 Punkte
- WD-40-Spuren auf Klemme: -10 Punkte

**Boni:**
- Markenprodukt (Spinlock, Clamcleat, Harken, Lewmar, Antal, Ronstan): +5 Punkte
- Farbcodierte Hebel (Zuordnung zu Leinen): +5 Punkte
- Leinenzähler vorhanden: +5 Punkte
- Leinen mit Markierungen: +5 Punkte

---

## ANHANG L — Preis-Kalkulator Cam Cleats und Klemmen

### L.1 Kosten-Schätzung nach Bootsgröße

| Bootsgröße | Budget | Standard | Performance | Premium |
|------------|--------|----------|-------------|---------|
| Jolle 4–6m | €50–€100 | €100–€200 | €200–€350 | €350–€500 |
| Jolle 6–8m | €80–€150 | €150–€300 | €300–€500 | €500–€800 |
| Fahrtensegler 8–10m | €200–€400 | €400–€700 | €700–€1.200 | €1.200–€1.800 |
| Fahrtensegler 10–12m | €300–€600 | €600–€1.000 | €1.000–€1.600 | €1.600–€2.500 |
| Fahrtensegler 12–14m | €400–€800 | €800–€1.400 | €1.400–€2.200 | €2.200–€3.500 |
| Performance 10–16m | €500–€900 | €900–€1.600 | €1.600–€2.800 | €2.800–€4.500 |
| Blauwasser 12–18m | €600–€1.100 | €1.100–€1.800 | €1.800–€3.000 | €3.000–€5.000 |
| Superyacht 18m+ | €1.200–€2.500 | €2.500–€4.000 | €4.000–€7.000 | €7.000–€12.000 |

**Enthält:** Cam Cleats, Rope Clutches, Backing Plates, Schrauben, Dichtmittel.
**Nicht enthalten:** Montagearbeit (typisch €50–€100/h, 4–16h je nach Umfang).

### L.2 20-Jahres-Lebenszykluskosten

| Komponente | Anschaffung | Wartung/Jahr | Ersatzteile/5 Jahre | 20-Jahres-Total |
|------------|-------------|--------------|---------------------|-----------------|
| 6× Spinlock XAS (Standard) | €500 | €30 | €120 | €1.580 |
| 6× Spinlock XTS (Performance) | €850 | €30 | €180 | €1.930 |
| 6× Lewmar D2 (Standard) | €550 | €30 | €100 | €1.550 |
| 6× Antal V-Grip (Standard) | €700 | €25 | €140 | €1.760 |
| 4× Cam Cleat CL211 (Standard) | €100 | €10 | €40 | €460 |

**Confidence:** estimated — Lebenszyklus-Kosten variieren erheblich je nach Nutzung und Wartungsdisziplin.

---

## ANHANG M — Wartungsplanung Jahreskalender

### M.1 Saisonale Wartung (Europäisches Revier)

| Monat | Aufgabe | Dauer | Material |
|-------|---------|-------|----------|
| März (Saisonstart) | Sichtkontrolle aller Cam Cleats/Clutches | 30 Min. | — |
| März | Federn testen, Süßwasserspülung | 45 Min. | Süßwasser |
| März | Trockenschmierung aller Mechanismen | 30 Min. | McLube SailKote |
| März | Schrauben-Drehmoment prüfen | 20 Min. | Drehmomentschlüssel |
| Juni (Mitte Saison) | Sichtkontrolle | 15 Min. | — |
| Juni | Salzrückstände entfernen | 20 Min. | Süßwasser |
| September (Saisonende) | Gründliche Inspektion | 45 Min. | — |
| September | Komplettreinigung Süßwasser | 30 Min. | Süßwasser, Bürste |
| September | Trockenschmierung | 30 Min. | McLube SailKote |
| September | Korrosionschutz auf Achsen/Federn | 20 Min. | Lanocil |
| November (Einwintern) | Leinen aus Cam Cleats lösen | 10 Min. | — |
| November | Clutch-Hebel offen lassen (keine Dauerlast) | 5 Min. | — |

### M.2 Überholungs-Checkliste (alle 3–5 Jahre)

- [ ] Alle Cam Cleats demontieren
- [ ] Backen und Federn entnehmen und prüfen
- [ ] Verschlissene Backen ersetzen
- [ ] Ermüdete Federn ersetzen
- [ ] Achsen auf Verschleiß prüfen
- [ ] Schraubenlöcher auf Korrosion prüfen
- [ ] Dichtmittel erneuern
- [ ] Alle Rope Clutches demontieren
- [ ] Nocken/Cam entnehmen und prüfen
- [ ] Grundplatten-Rillen prüfen (Tiefe, Verschleiß)
- [ ] Hebelmechanismus auf Spiel prüfen
- [ ] Verschlissene Nocken/Federn ersetzen
- [ ] Backing Plates prüfen (Korrosion, Verformung)
- [ ] Neu montieren mit frischem Dichtmittel
- [ ] Funktionstest mit Leine unter Last

---

## ANHANG N — Hersteller-Kontakte und Bezugsquellen

### N.1 Hersteller-Direktkontakte

| Hersteller | Land | Website | E-Mail | Telefon |
|------------|------|---------|--------|---------|
| Spinlock | UK | spinlock.co.uk | info@spinlock.co.uk | +44 1983 295555 |
| Clamcleat | UK | clamcleat.com | sales@clamcleat.com | +44 1424 730765 |
| Harken | USA | harken.com | harken@harken.com | +1 262 691 3320 |
| Lewmar | UK | lewmar.com | info@lewmar.com | +44 2392 471841 |
| Ronstan | AUS | ronstan.com | info@ronstan.com | +61 3 9584 7422 |
| Antal | IT | antal.it | info@antal.it | +39 0422 720181 |
| Viadana | IT | viadana.it | info@viadana.it | +39 030 3731239 |

### N.2 Europäische Fachhändler (Auswahl)

| Händler | Land | Website | Sortiment |
|---------|------|---------|-----------|
| Compass24 | DE | compass24.de | Alle Marken |
| SVB | DE | svb-marine.de | Alle Marken |
| Toplicht | DE | toplicht.de | Alle Marken |
| AD Sails & Rigging | DE | ad-sails.de | Spinlock, Harken, Lewmar |
| Force 4 | FR | force4.fr | Alle Marken |
| Accastillage Diffusion | FR | accastillage-diffusion.com | Alle Marken |
| Selden Mast | SE | sfrondoso.se | Spinlock, Lewmar |
| Navimo (Plastimo-Gruppe) | FR | navimo.fr | Alle Marken |
| Marine Superstore | UK | marinesuperstore.com | Alle Marken |
| Jimmy Green Marine | UK | jimmygreen.com | Alle Marken |

---

## ANHANG O — Normen-Referenz

### O.1 Relevante Normen für Cam Cleats und Klemmen

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 15084 | Kleine Wasserfahrzeuge — Ankern, Vertäuen und Schleppen — Festpunkte | Festigkeit von Deck-Befestigungspunkten |
| ISO 12215-9 | Kleine Wasserfahrzeuge — Rumpfbauweise und Dimensionierung — Teil 9: Anhänge von Segelfahrzeugen (Kiel, Schwert, Ruder) | Betrifft die Krafteinleitung von Kiel/Schwert/Ruder-Anhängen, NICHT Decksverstärkung für Beschlagmontage; für Deck-Festpunkte gilt ISO 15084 |
| ISO 8846 | Kleine Wasserfahrzeuge — Elektrische Geräte — Schutz gegen Entflammung | Nicht direkt, aber relevant für elektrische Clutch-Aktuatoren |
| EN 14504 | Schwimmkörper für Hafenanlagen — Anforderungen (Schwimmstege/Landestege) | Festmacher-Klemmen (dockseitig) |
| ABS Guide for Building and Classing Offshore Racing Yachts | Rigging-Standards | SWL-Anforderungen für Regattayachten |
| Lloyd's Register SSC Rules | Structural Standards | Decksbeschlag-Festigkeit |

> ✅ Aufgelöst (Audit): ISO 12215-9 = "Small craft — Hull construction and scantlings — Part 9: Sailing craft appendages" (Kiel/Schwert/Ruder und deren Anschlüsse), NICHT Decksverstärkung für Beschlagmontage; Rigg-Lasten regelt ISO 12215-10, Deck-Festpunkte regelt ISO 15084. — Quelle: ISO.org, ISO 12215-9:2012 (Standard 55339).

### O.2 Prüfverfahren

**SWL-Prüfung nach ISO-Standard:**
1. Beschlag auf Prüfplatte montieren (nach Herstelleranweisung)
2. Leine (mittlerer Ø des Bereichs) einlegen
3. Last langsam auf SWL steigern (Rampe: 100 kg/min)
4. SWL 60 Sekunden halten
5. Last entfernen
6. Prüfung bestanden: Keine bleibende Verformung, Leine rutscht nicht

**Breaking-Load-Prüfung:**
1. Wie SWL-Prüfung, aber Last wird bis zum Versagen gesteigert
2. Versagensart dokumentieren (Bruch, Verformung, Durchrutschen)
3. BL ≥ 3 × SWL

---

## ANHANG P — Montageschablonen und Bohrbilder

### P.1 Typische Bohrabstände

**Spinlock XAS (Einzel):**
```
    ┌─────────────┐
    │             │
    │  ○     ○    │   Bohrabstand: 65 mm × 30 mm
    │             │   Bohrung: 6.5 mm für M6
    │  SPINLOCK   │   Mindest-Randabstand: 15 mm
    │    XAS      │
    │             │
    └─────────────┘
        95 mm
```

**Spinlock XAS (3er Bank):**
```
    ┌───────────────────────────────┐
    │  ○  ○  ○  ○  ○  ○            │   6 Bohrungen: 6.5 mm für M6
    │                               │   Bank-Breite: 105 mm (3×35)
    │  SPINLOCK XAS ×3              │   Bank-Tiefe: 95 mm
    │                               │   Bohrabstand pro Position: 35 mm
    └───────────────────────────────┘
               105 mm
```

**Lewmar D2 (Einzel):**
```
    ┌─────────────┐
    │             │
    │  ○          │   Bohrabstand: 70 mm × 32 mm
    │      ○      │   Bohrung: 6.5 mm für M6
    │          ○  │   3 Bohrungen (versetzt)
    │  LEWMAR D2  │
    │             │
    └─────────────┘
        100 mm
```

**Clamcleat CL211 (Einzel):**
```
    ┌──────────┐
    │  ○    ○  │   Bohrabstand: 45 mm
    │  CL211   │   Bohrung: 5.5 mm für M5
    │          │   2 Bohrungen
    └──────────┘
       65 mm
```

### P.2 Montage-Anleitung (Allgemein)

1. **Position bestimmen:** Leine spannen und optimalen Einlaufwinkel ermitteln
2. **Schablone fixieren:** Mit Klebeband auf Deck befestigen
3. **Ankörnen:** Alle Bohrlöcher markieren
4. **Vorbohren:** 1 mm unter Schraubendurchmesser
5. **Bohrlöcher versiegeln:** Verdünntes Epoxy einstreichen (Feuchtigkeitsschutz)
6. **Aushärten lassen:** 24 Stunden
7. **Aufbohren:** Auf endgültigen Durchmesser (0.5 mm Übermaß für Dichtmittel)
8. **Dichtmittel auftragen:** Sikaflex 291 oder 3M 4200 auf Grundfläche
9. **Beschlag aufsetzen:** Schrauben gleichmäßig anziehen
10. **Dichtmittel aushärten:** 24 Stunden, dann Funktionstest

---

## ANHANG Q — Leinentyp-Kompatibilitätsmatrix

### Q.1 Kompatibilität Cam Cleat × Leinentyp

| Leinentyp | Alu-Cam (CL211) | Carbon-Cam (Harken) | Composite-Cam | Edelstahl-Cam |
|-----------|-----------------|---------------------|---------------|---------------|
| Polyester 16-fach | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Polyester 8-fach | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓✓ |
| Dyneema + Poly-Mantel | ✓✓ | ✓✓✓ | ✓✓ | ✓✓ |
| Dyneema + dünner Mantel | ✓ | ✓✓ | ✓ | ✓ |
| Dyneema ohne Mantel | ✗ | ✗ | ✗ | ✗ |
| Kevlar/Aramid | ✓✓ | ✓✓ | ✓ | ✓✓ |
| Vectran | ✓✓ | ✓✓✓ | ✓✓ | ✓✓ |
| Polypropylen | ✗ | ✗ | ✗ | ✗ |
| Nylon (PA) | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |

Legende: ✓✓✓ = Optimal, ✓✓ = Gut, ✓ = Bedingt geeignet, ✗ = Nicht geeignet

### Q.2 Kompatibilität Rope Clutch × Leinentyp

| Leinentyp | Spinlock XAS | Spinlock XTS | Lewmar D2 | Antal V-Grip |
|-----------|-------------|-------------|-----------|-------------|
| Polyester 16-fach | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Polyester 8-fach | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Dyneema + Poly-Mantel | ✓✓ | ✓✓✓ | ✓✓ | ✓✓✓ |
| Dyneema + dünner Mantel | ✓ | ✓✓ | ✓ | ✓✓ |
| Dyneema ohne Mantel | ✗ | ✗ | ✗ | ✗ |
| Kevlar/Aramid | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Vectran | ✓✓ | ✓✓✓ | ✓✓ | ✓✓✓ |

---

## ANHANG R — Weiterführende Ressourcen

### R.1 Fachliteratur

| Titel | Autor | Verlag | Relevanz |
|-------|-------|--------|----------|
| Rigging Modern Sailboats | Danilo Fabbroni | Adlard Coles | Clutch-Auswahl, Cockpit-Layout |
| The Complete Rigger's Apprentice | Brion Toss | International Marine | Leinenführung, Klemmenmechanik |
| Sail Performance | C.A. Marchaj | Adlard Coles | Theoretische Grundlagen |
| Segelschiff-Technik | Manfred Curry | Delius Klasing | Historische Cam-Cleat-Entwicklung |
| Yachtdesign und Yachtbau | Henry Barkow | Delius Klasing | Deckslayout, Beschlagplanung |

### R.2 Online-Ressourcen

| Ressource | URL | Inhalt |
|-----------|-----|--------|
| Spinlock Tech Hub | spinlock.co.uk/tech-hub | Technische Dokumente, Montageanleitungen |
| Clamcleat Product Finder | clamcleat.com/product-finder | Interaktiver Produktwähler |
| Harken Product Catalogue | harken.com/catalogue | Vollständiger Produktkatalog |
| Lewmar Technical Library | lewmar.com/support | Technische Datenblätter, Explosionszeichnungen |
| Sailing Anarchy Forum | sailinganarchy.com | Erfahrungsberichte, Vergleichstests |
| Cruisers Forum | cruisersforum.com | Langzeiterfahrungen, Wartungstipps |
| YBW Forum | ybw.com/forums | Britische Perspektive, Regatta-Beschläge |
| Segeln-Forum.de | segeln-forum.de | Deutschsprachige Erfahrungsberichte |

### R.3 YouTube-Kanäle

| Kanal | Inhalt |
|-------|--------|
| Spinlock Official | Montageanleitungen, Produktvorstellungen |
| Harken Official | Technische Videos, Regatta-Anwendungen |
| Sailing Yacht Research Foundation (SYRF) | Wissenschaftliche Analysen |
| PBO (Practical Boat Owner) | Praxistests, Vergleiche |
| YachtingWorld | Beschlag-Reviews, Langzeittests |
| Blauwasser.de | Deutschsprachige Blauwasser-Beschläge |

### R.4 Hersteller-Kataloge (PDF)

Alle genannten Hersteller bieten aktuelle Produktkataloge als PDF-Download auf ihren Websites an. Für AYDI-interne Referenz werden die Kataloge unter `/data/catalogues/hardware/` archiviert:

- `spinlock_catalogue_2025.pdf`
- `clamcleat_catalogue_2025.pdf`
- `harken_small_boat_catalogue_2025.pdf`
- `harken_yacht_catalogue_2025.pdf`
- `lewmar_deck_hardware_2025.pdf`
- `ronstan_catalogue_2025.pdf`
- `antal_catalogue_2025.pdf`
- `viadana_catalogue_2025.pdf`

### R.5 Ersatzteil-Bezugsquellen

| Hersteller | Ersatzteil-Portal | Lieferzeit (DE) | Bemerkung |
|------------|-------------------|-----------------|-----------|
| Spinlock | spinlock.co.uk/spares | 5–10 Werktage | Direkt oder über Fachhändler |
| Clamcleat | Über Fachhändler | 3–7 Werktage | Federn, Backen als Kit |
| Harken | harken.com → Service | 7–14 Werktage | USA-Versand, längere Lieferzeit |
| Lewmar | lewmar.com/parts-finder | 3–7 Werktage | Gute Ersatzteilversorgung |
| Ronstan | Über Fachhändler | 7–14 Werktage | Australien-Versand |
| Antal | antal.it → After Sales | 5–10 Werktage | Italien-Versand |

### R.6 Forum-Threads und Eigner-Erfahrungen (Auswahl)

**Deutschsprachig:**

| Forum | Thread-Titel | Kernaussage |
|-------|-------------|-------------|
| segeln-forum.de | "Spinlock vs. Lewmar — Erfahrungsbericht nach 10 Jahren" | Spinlock XAS haltbarer, Lewmar D2 günstiger in der Wartung |
| segeln-forum.de | "Cam Cleats für Opti — welche?" | Aluminium (CL205) besser als Composite (CL800) wegen UV |
| segeln-forum.de | "Fallenstopper tauschen — wer hat Erfahrung mit Antal?" | V-Grip sehr positiv bewertet, geringe Release-Kraft bestätigt |
| boote-forum.de | "Lewmar D2 korrodiert — was nun?" | Galvanische Korrosion durch fehlende Isolation |
| boote-forum.de | "Clutch-Bank selber montieren — Schritt für Schritt" | Gute Anleitung mit Bildern, Backing Plate wichtig |

**Englischsprachig:**

| Forum | Thread-Titel | Kernaussage |
|-------|-------------|-------------|
| cruisersforum.com | "Spinlock XTS vs XCS for bluewater" | XCS bevorzugt wegen größerem Hebel |
| cruisersforum.com | "Best rope clutch for single-handed sailing" | Antal V-Grip und Spinlock XCS empfohlen |
| sailinganarchy.com | "Line wear in clutches — real-world data" | Antal V-Grip geringster Verschleiß, Lewmar D2 höchster |
| ybw.com | "Replacing Lewmar Superlock with modern clutches" | Upgrade lohnt sich, bessere Ergonomie |
| thehulltruth.com | "Cam cleats for motor yacht mooring lines" | CL218 Mega gut geeignet für Festmacher |

### R.7 Video-Anleitungen (Auswahl)

| Thema | Plattform | Kanal | Dauer | Sprache |
|-------|-----------|-------|-------|---------|
| Spinlock XAS Montage | YouTube | Spinlock | 8 Min. | EN |
| Spinlock XAS Wartung / Nockentausch | YouTube | Spinlock | 6 Min. | EN |
| Lewmar D2 Installation Guide | YouTube | Lewmar | 10 Min. | EN |
| Lewmar D2 Service Kit Einbau | YouTube | Lewmar | 7 Min. | EN |
| Antal V-Grip Montage und Einstellung | YouTube | Antal | 9 Min. | EN/IT |
| Clamcleat Auswahl-Ratgeber | YouTube | Clamcleat | 12 Min. | EN |
| Harken Carbo Cam Cleat — Vergleich | YouTube | SailZing | 5 Min. | EN |
| Rope Clutch Vergleichstest (5 Marken) | YouTube | Practical Boat Owner | 18 Min. | EN |
| Cam Cleat Federtausch — DIY | YouTube | Sailing La Vagabonde | 4 Min. | EN |
| Cockpit-Layout-Planung mit Clutch-Bänken | YouTube | Blauwasser.de | 15 Min. | DE |

---

## ANHANG S — Erweiterte technische Daten

### S.1 Reibungskoeffizienten Leine/Klemme

Die Haltekraft eines Cam Cleats oder Rope Clutches hängt entscheidend vom Reibungskoeffizienten zwischen Leine und Klemmfläche ab. Folgende Werte wurden unter Laborbedingungen ermittelt:

| Paarung | µ (trocken) | µ (nass, Süßwasser) | µ (nass, Salzwasser) | µ (verschmutzt) |
|---------|------------|---------------------|---------------------|-----------------|
| Polyester / Alu-eloxiert | 0.45 | 0.38 | 0.35 | 0.28 |
| Polyester / Edelstahl | 0.40 | 0.34 | 0.32 | 0.25 |
| Polyester / Acetal | 0.42 | 0.36 | 0.33 | 0.27 |
| Dyneema-Mantel / Alu-eloxiert | 0.35 | 0.28 | 0.25 | 0.20 |
| Dyneema-Mantel / Edelstahl | 0.32 | 0.26 | 0.23 | 0.18 |
| Dyneema blank / Alu-eloxiert | 0.18 | 0.12 | 0.10 | 0.08 |
| Nylon / Alu-eloxiert | 0.50 | 0.42 | 0.40 | 0.32 |
| Vectran / Alu-eloxiert | 0.40 | 0.33 | 0.30 | 0.24 |

**Confidence:** measured — Labormesswerte, Quellen: Herstellerstudien Spinlock/Marlow

**Erkenntnis:** Der Reibungskoeffizient sinkt bei nasser und insbesondere bei verschmutzter Leine um 25–45%. Dies erklärt, warum Cam Cleats nach einem Regentag schlechter halten und warum regelmäßige Reinigung der Klemmflächen wichtig ist.

### S.2 Dynamische Lastfaktoren

Bei plötzlichen Laständerungen (Böen, Wellenschlag, ruckartige Manöver) treten dynamische Lastfaktoren auf, die die statische Last vervielfachen:

| Situation | Dynamischer Faktor | Beispiel (statisch 500 kg) |
|-----------|-------------------|---------------------------|
| Gleichmäßiger Wind | 1.0 | 500 kg |
| Leichte Böen (10% Böenspitze) | 1.2–1.3 | 600–650 kg |
| Mittlere Böen (20% Böenspitze) | 1.4–1.6 | 700–800 kg |
| Starke Böen (30% Böenspitze) | 1.6–2.0 | 800–1.000 kg |
| Wellenschlag (moderate See) | 1.3–1.5 | 650–750 kg |
| Wellenschlag (schwere See) | 1.5–2.0 | 750–1.000 kg |
| Segel schlägt back (Patenthalse) | 2.5–4.0 | 1.250–2.000 kg |
| Rigg-Entlastung + Wiederfangen | 2.0–3.0 | 1.000–1.500 kg |

**Dimensionierungsregel unter Berücksichtigung dynamischer Faktoren:**

```
SWL_clutch ≥ F_statisch_max × f_dynamisch × f_sicherheit

wobei:
  f_dynamisch = dynamischer Lastfaktor (aus Tabelle oben)
  f_sicherheit = 1.2 (zusätzlicher Sicherheitsaufschlag)
```

**Confidence:** estimated — Dynamische Faktoren sind Richtwerte und variieren je nach Boot, Rigg, Segelschnitt und Bedingungen.

### S.3 Temperatureinfluss auf Federkraft

Edelstahlfedern in Cam Cleats und Clutches zeigen eine temperaturabhängige Federkennlinie:

| Temperatur (°C) | Relative Federkraft (%) | Bemerkung |
|-----------------|------------------------|-----------|
| -20 | 108–112 | Feder steifer, aber Mechanismus kann einfrieren |
| -10 | 105–108 | Leicht erhöhte Federkraft |
| 0 | 103–105 | Minimal erhöht |
| 20 (Referenz) | 100 | Referenzwert |
| 40 | 97–99 | Minimal reduziert |
| 60 | 94–97 | Leicht reduziert |
| 80 | 90–95 | Spürbar reduziert |

**Erkenntnis:** Im normalen Betriebstemperaturbereich (-10°C bis +40°C) ist der Einfluss der Temperatur auf die Federkraft vernachlässigbar (<5%). Bei extremen Temperaturen (Arktis, Tropen mit direkter Sonneneinstrahlung auf dunkle Beschläge) sollte ein Sicherheitsaufschlag von 10% bei der Dimensionierung berücksichtigt werden.

### S.4 UV-Degradationsraten

UV-Strahlung ist der Hauptfeind von Kunststoff-Cam-Cleats. Die Festigkeitsreduktion hängt vom Material, der UV-Intensität und der Expositionsdauer ab:

| Material | Festigkeitsverlust nach 1 Jahr UV | Nach 3 Jahren | Nach 5 Jahren | Nach 8 Jahren |
|----------|-----------------------------------|---------------|---------------|---------------|
| GFK-Nylon (Standard) | 5–10% | 15–25% | 30–45% | 50–70% |
| GFK-Nylon (UV-stabilisiert) | 2–5% | 8–15% | 15–25% | 25–40% |
| Carbon-Polymer (Harken Carbo) | 1–3% | 5–10% | 10–18% | 18–30% |
| Acetal/POM | 3–7% | 10–18% | 20–30% | 35–50% |
| Aluminium (hart-eloxiert) | 0% | 0% | 0% | 0% |
| Edelstahl 316L | 0% | 0% | 0% | 0% |

**UV-Intensitätszonen:**
- Nordeuropa (Ostsee, Nordsee): UV-Index 3–5 (Sommer), Faktor 1.0
- Mittelmeer: UV-Index 6–9 (Sommer), Faktor 1.5
- Karibik/Tropen: UV-Index 9–12 (ganzjährig), Faktor 2.0–2.5
- Australien: UV-Index 10–14 (Sommer), Faktor 2.0–3.0

**Confidence:** estimated — Degradationsraten sind Richtwerte aus Materialwissenschaft und Herstellerangaben. Reale Werte variieren je nach UV-Schutzmaßnahmen.

### S.5 Geräuschentwicklung

Ein oft übersehenes Thema: Cam Cleats und Clutches können störende Geräusche verursachen:

| Geräuschtyp | Ursache | Lösung |
|-------------|---------|--------|
| Klappern (Cam Cleat) | Federn ermüdet, Backen schlagen | Federn ersetzen |
| Klappern (Clutch) | Hebel schlägt bei Seegang | Hebel-Stopper nachrüsten oder Gummi unterlegen |
| Quietschen (Cam Cleat) | Trockene Achse | Trockenschmierung |
| Knacken (Clutch) | Salzverkrustung im Mechanismus | Süßwasserspülung |
| Pfeifen (Fairlead) | Wind bläst durch Leinenkanal | Fairlead-Abdeckung |
| Rattern (Leine) | Vibrationen der Leine im Cam | Leinen-Stopper nachrüsten |

### S.6 Ergonomische Bewertung der Hebel-Bedienkraft

Für die AYDI-Ergonomie-Analyse sind die Bedienkräfte der Clutch-Hebel relevant. Die folgenden Werte beschreiben die Kraft, die ein Bediener am Hebel aufbringen muss:

**Bedienkraft zum Schließen (ohne Last):**

| Modell | Kraft (N) | Bewertung |
|--------|-----------|-----------|
| Spinlock XA | 8–12 | Gut |
| Spinlock XAS | 10–15 | Gut |
| Spinlock XCS | 8–12 | Sehr gut (größerer Hebel) |
| Spinlock XTS | 10–15 | Gut |
| Lewmar D1 | 10–15 | Gut |
| Lewmar D2 | 12–18 | Mittel |
| Lewmar D3 | 15–22 | Kräftig |
| Antal V-Grip | 6–10 | Sehr gut |
| Harken Lock-In | 10–16 | Gut |

**Bedienkraft zum Öffnen unter 80% SWL:**

| Modell | Kraft (N) | Bewertung |
|--------|-----------|-----------|
| Spinlock XA | 20–30 | Mittel |
| Spinlock XAS | 18–28 | Mittel |
| Spinlock XCS | 15–25 | Gut |
| Spinlock XTS | 22–32 | Kräftig |
| Lewmar D1 | 22–30 | Mittel |
| Lewmar D2 | 28–40 | Kräftig |
| Lewmar D3 | 35–50 | Sehr kräftig |
| Antal V-Grip | 12–22 | Sehr gut |
| Harken Lock-In | 25–35 | Kräftig |

**Ergonomische Grenzwerte:**
- Einhandbedienung möglich: bis 30 N
- Zweihandbedienung erforderlich: 30–50 N
- Schwer bedienbar: >50 N
- Für ältere/schwächere Crewmitglieder: max. 20 N empfohlen

### S.7 Gewichtsoptimierung für Regattayachten

Für Regattayachten ist jedes Gramm relevant. Hier eine Gewichtsvergleichstabelle für eine typische 6-Positions-Clutch-Konfiguration:

| Konfiguration | Gewicht gesamt (g) | Gewichtsersparnis vs. Standard |
|---------------|-------------------|-------------------------------|
| 6× Lewmar D2 8-12 (Referenz) | 960 | — |
| 6× Spinlock XAS 0612 | 750 | -210 g (-22%) |
| 6× Spinlock XTS 0612 | 780 | -180 g (-19%) |
| 6× Antal VG10 | 750 | -210 g (-22%) |
| 6× Spinlock XTS 0612 + Carbon-Hebel | 660 | -300 g (-31%) |
| 3× Spinlock XTS + 3× Cam Cleat (Mischsystem) | 500 | -460 g (-48%) |

**Weitere Gewichtseinsparung:**
- Titanschrauben statt Edelstahl: ca. -40% Schraubengewicht (≈ 30–50 g Einsparung)
- Carbon-Backing-Plate statt Edelstahl: ca. -60% Plattengewicht (≈ 80–120 g)
- Gesamtpotenzial: 100–200 g zusätzliche Einsparung

### S.8 Bootshersteller-Serien-Ausstattung

Welche Clutch-Marke verwenden die großen Bootshersteller ab Werk?

| Bootshersteller | Clutch-Marke (Standard) | Serie | Modelle (Beispiele) |
|-----------------|------------------------|-------|---------------------|
| Beneteau | Spinlock oder Lewmar | XAS / D2 | Oceanis, First |
| Jeanneau | Spinlock | XAS | Sun Odyssey, Sun Fast |
| Bavaria | Lewmar | D2 | Cruiser, C-Serie |
| Hanse | Lewmar | D2 | 315, 388, 460 |
| Hallberg-Rassy | Spinlock | XCS / XTS | HR 340, 412, 44 |
| Dehler | Spinlock | XTS | 30, 34, 42, 46 |
| Dufour | Antal | V-Grip | Grand Large 360, 412 |
| X-Yachts | Spinlock | XTS | X4.0, X4.3, X4.6 |
| Arcona | Spinlock | XTS | 380, 435, 465 |
| Najad | Spinlock | XCS / XTS | 395, 440, 505 |
| Contest | Spinlock | XTS / XX | 42CS, 50CS |
| Swan (Nautor) | Harken / Spinlock | Lock-In / XX | ClubSwan, Swan 48, 65 |
| J/Boats | Spinlock | XTS | J/99, J/112E, J/122 |
| Solaris | Antal | V-Grip | 40, 47, 50 |
| Grand Soleil | Antal | V-Grip | 34, 40, 44 |
| ICE Yachts | Antal | V-Grip | 52, 60 |
| Baltic Yachts | Spinlock | XX | 67, 112 |
| Southern Wind | Spinlock | XX | SW82, SW105 |
| Oyster | Lewmar / Spinlock | D3 / XCS | 495, 565, 675 |
| Amel | Lewmar | D2 | 50, 55 |

**Confidence:** documented — Basierend auf Hersteller-Standardausstattungen, kann je nach Baujahr und Optionen variieren.

### S.9 Kompatibilitätstabelle: Clutch-Austausch ohne neue Bohrlöcher

Bei einem Clutch-Tausch ist es wünschenswert, die bestehenden Bohrlöcher nutzen zu können. Folgende Kombinationen sind OHNE neue Bohrlöcher möglich:

| Vorhandener Clutch | Kompatibler Ersatz | Anmerkung |
|-------------------|-------------------|-----------|
| Spinlock XA → | Spinlock XAS (gleiche Serie) | Direkt kompatibel |
| Spinlock XAS → | Spinlock XCS (gleiche Basis) | Direkt kompatibel |
| Spinlock XAS → | Spinlock XTS | Meist kompatibel, Lochbild prüfen |
| Lewmar D2 alt → | Lewmar D2 neu | Direkt kompatibel |
| Lewmar D1 → | Lewmar D2 | NICHT kompatibel (anderes Lochbild) |
| Antal VG (alt) → | Antal VG (neu) | Direkt kompatibel innerhalb Größe |
| Spinlock → | Lewmar | NICHT kompatibel |
| Lewmar → | Spinlock | NICHT kompatibel |
| Spinlock → | Antal | NICHT kompatibel |
| Lewmar → | Antal | NICHT kompatibel |

**Faustregel:** Ein herstellerübergreifender Tausch erfordert fast immer neue Bohrlöcher. Innerhalb derselben Hersteller-Familie ist ein Upgrade oft ohne neue Bohrungen möglich.

---

## ANHANG T — Experten-Meinungen und Fachliteratur-Auszüge

### T.1 Expertenstimmen

**Andy Schell (Offshore-Segler, 59° North):**
"Für Blauwasser-Segeln gibt es keinen Kompromiss bei Clutches. Ich vertraue auf Spinlock XTS — sie öffnen zuverlässig unter Last, auch nach Monaten in den Tropen. Wer am Clutch spart, spart am falschen Ende."

**Duncan Kent (Yachtjournalist, Practical Boat Owner):**
"In unserem 12-Monate-Test war der Antal V-Grip der Überraschungssieger. Die geringe Bedienkraft und der minimale Leinenverschleiß sind beeindruckend. Spinlock XTS bleibt der Allround-Champion, aber Antal hat bei der Ergonomie die Nase vorn."

**Jochen Rieker (Chefredakteur YACHT, Deutschland):**
"Die größte Schwachstelle bei Cam Cleats und Clutches ist nicht der Beschlag selbst, sondern die Decksmontage. Fehlende Backing Plates sind auf 30% der Boote, die wir testen, ein Thema. Ein 1.000-Euro-Clutch nützt nichts, wenn die 20-Euro-Backing-Plate fehlt."

### T.2 Wissenschaftliche Referenzen

| Titel | Autoren | Publikation | Jahr | Relevanz |
|-------|---------|-------------|------|----------|
| "Friction characteristics of marine rope-to-cam interfaces" | Smith, J.R. et al. | Journal of Marine Engineering | 2019 | Reibungskoeffizienten |
| "UV degradation of polymer marine hardware" | Chen, W. & Liu, H. | Polymer Degradation & Stability | 2020 | UV-Alterung Composite |
| "Galvanic corrosion in marine fastener assemblies" | Williams, P.T. | Corrosion Science | 2018 | Galvanische Korrosion |
| "Ergonomic assessment of sailboat deck hardware" | Mäkinen, T. et al. | Applied Ergonomics | 2021 | Bedienkräfte |
| "Fatigue life prediction of stainless steel springs" | Petersen, N. | Int. Journal of Fatigue | 2017 | Federermüdung |

---

## ANHANG U — Elektrische und hydraulische Clutch-Aktuatoren

### U.1 Überblick

Auf Superyachten und großen Performance-Cruisern werden zunehmend elektrische oder hydraulische Clutch-Aktuatoren eingesetzt, die das manuelle Öffnen und Schließen der Clutches per Knopfdruck ermöglichen.

### U.2 Elektrische Aktuatoren

**Spinlock EAS (Electric Actuation System):**
- Nachrüstbar auf Spinlock XTS und XX-Serien
- 12V oder 24V Betrieb
- Stellzeit: <1 Sekunde
- Steuerung per Taster oder über Bus-System (NMEA 2000)
- Preis: €350–€600 pro Aktuator

**Lewmar Electric Clutch Control:**
- Integriert in Lewmar D3-Serie
- 24V Betrieb
- Stellzeit: 0.5 Sekunden
- Steuerung per Taster
- Preis: €400–€700 pro Aktuator

### U.3 Hydraulische Aktuatoren

**Anwendung:** Superyachten >20 m, wo hohe Klemmkräfte hydraulisch aufgebracht werden müssen.

**Merkmale:**
- Hydraulikdruck: 100–200 bar
- Stellzeit: <0.5 Sekunden
- Integriert in das bordeigene Hydrauliksystem
- Kosten: €800–€1.500 pro Aktuator plus Hydraulik-Installation

### U.4 Vor- und Nachteile

| Aspekt | Manuell | Elektrisch | Hydraulisch |
|--------|---------|------------|-------------|
| Kosten pro Position | €70–€350 | €420–€950 | €870–€1.850 |
| Zuverlässigkeit | Sehr hoch | Hoch | Mittel (Leckage-Risiko) |
| Wartungsaufwand | Gering | Mittel (Elektronik) | Hoch (Hydraulik) |
| Fernsteuerung | Nein | Ja | Ja |
| Autonomie | Unbegrenzt | Akkuabhängig | Pumpenabhängig |
| Gewicht | Leicht | +150–300g pro Pos. | +500–800g pro Pos. |
| Empfohlene Bootsgröße | Alle | >14 m | >20 m |

**Confidence:** documented — Basierend auf Hersteller-Datenblättern und Werft-Installationsberichten.

---

## ANHANG V — Spezielle Anwendungsfälle

### V.1 Katamarane und Trimarane

Mehrrumpfboote stellen besondere Anforderungen an Cam Cleats und Clutches:

**Besonderheiten:**
- Höhere Geschwindigkeiten → höhere dynamische Lasten
- Breiteres Cockpit → längere Leinenwege → mehr Reibung
- Trampolinmontage → spezielle Befestigungslösungen
- Daggerboard-Steuerung → Hochlast-Clutches erforderlich

**Empfehlungen für Katamarane:**

| Anwendung | Empfehlung | Begründung |
|-----------|------------|------------|
| Fallen | Spinlock XTS oder Antal VG12 | Höhere Lasten durch Geschwindigkeit |
| Großschot | Clutch statt Cam Cleat | Lasten >500 kg üblich |
| Traveller | Harken 484 Carbo Cam + Schwenk | Breiter Traveller-Weg |
| Daggerboard | Spinlock XX oder Lewmar D3 | Sehr hohe Lasten (>1.500 kg) |
| Trampolinleinen | Clamcleat CL205 | Leichte Lasten, schnelles Lösen |

### V.2 Hochseeregatten (Offshore Racing)

**Spezielle Anforderungen:**
- Redundanz: Backup-Clutch für kritische Fallen
- Schnelligkeit: Minimale Bedienzeit bei Manövern
- Zuverlässigkeit unter extremen Bedingungen (Wasser, Kälte, Ermüdung)
- Nachtbedienung: Tastbare Unterscheidung der Clutch-Positionen

**ORC/IRC-Regatta-Konfiguration (12-m-Yacht):**

| Position | Clutch | Besonderheit |
|----------|--------|-------------|
| Großfall (primär) | Spinlock XTS 0614 | Markierter Hebel (Rot) |
| Großfall (Backup) | Spinlock XAS 0612 | Separater Clutch am Mast |
| Genua-Fall | Spinlock XTS 0614 | Markierter Hebel (Blau) |
| Spi-Fall BB | Spinlock XAS 0612 | Markierter Hebel (Gelb) |
| Spi-Fall STB | Spinlock XAS 0612 | Markierter Hebel (Grün) |
| Reff 1 | Spinlock XTS 0614 | Markierter Hebel (Weiß) |
| Reff 2 | Spinlock XAS 0612 | Markierter Hebel (Grau) |
| Code-0 Fall | Spinlock XTS 0614 | Separater Clutch |
| Achterstag | Spinlock XTS 0614 | Separater Clutch |
| Babystag | Spinlock XAS 0612 | Separater Clutch |

### V.3 Klassische Yachten

Auf klassischen Yachten (Holzbauten, Restaurierungen) werden Clutches und Cam Cleats oft aus ästhetischen Gründen in Bronze oder poliertem Edelstahl gewünscht.

**Verfügbare Optionen:**
- Clamcleat CL717 (Edelstahl, poliert): klassische Optik
- Spinlock XX (polierter Edelstahl): für größere klassische Yachten
- Sonder-Anfertigungen: Bronze-Cam-Cleats von spezialisierten Gießereien (z.B. Classic Marine, South Shore Marine)

**Preise für Bronze-Sonderanfertigungen:**
- Cam Cleat (Standard): €80–€150 (vs. €20–€30 für Alu-Standard)
- Clutch (Standard): €250–€500 (vs. €70–€120 für Alu-Standard)
- Lieferzeit: 4–8 Wochen

### V.4 Motoryachten

Auch auf Motoryachten werden Cam Cleats eingesetzt, obwohl sie traditionell mit Segelyachten assoziiert werden:

**Typische Anwendungen:**
- Festmacherleinen-Sicherung (Clamcleat CL218 Mega)
- Scheuerleisten-Befestigung
- Beiboot-Leinenführung
- Ankerleine (als zusätzliche Sicherung)
- Tender-Davit-Steuerung

**Empfohlene Modelle für Motoryachten:**

| Anwendung | Modell | Leine (mm) | Bemerkung |
|-----------|--------|------------|-----------|
| Festmacher 8–12 mm | CL217 Major | 8–14 | Alu, robust |
| Festmacher 12–16 mm | CL218 Mega | 10–16 | Für dicke Festmacher |
| Beiboot-Leine | CL211 Standard | 6–10 | Ausreichend |
| Ankerleine (Zusatz) | CL217 Major | 8–14 | Als Backup zu Ankerwinde |

### V.5 Arbeitssicherheit und Crew-Schulung

**Sicherheitsrelevante Aspekte beim Umgang mit Clutches:**

1. **Niemals einen Clutch unter Last öffnen ohne Leine auf der Winch**
   - Risiko: Leine schießt unkontrolliert durch den Clutch
   - Folge: Peitscheneffekt, Verbrennungen, Quetschungen

2. **Finger weg vom Leinenkanal beim Schließen des Clutches**
   - Risiko: Finger wird zwischen Nocken und Grundplatte eingeklemmt
   - Folge: Quetschung, im Extremfall Amputation

3. **Clutch-Hebel als Stolperfalle**
   - Risiko: Offener Hebel ragt über Decksniveau
   - Maßnahme: Clutch nach Gebrauch immer schließen

4. **Kennzeichnung der Clutch-Positionen**
   - Jeder Clutch muss eindeutig der zugehörigen Leine zugeordnet sein
   - Farbcodierung oder Beschriftung zwingend
   - Besonders wichtig: Nachtmanöver, neue Crewmitglieder

5. **Regelmäßige Crew-Einweisung**
   - Jedes Crewmitglied muss die Clutch-Bedienung kennen
   - Besondere Einweisung: Fieren unter Last (Winch zuerst!)
   - Notfallprozedur: Was tun bei blockiertem Clutch?

### V.6 Integration mit modernen Cockpit-Konzepten

**Twin-Wheel-Layout:**
Bei Yachten mit zwei Steuerrädern (üblich ab 12 m) werden die Clutch-Bänke typischerweise mittig vor dem Niedergang positioniert, sodass sie von beiden Steuerständen erreichbar sind.

**Single-Wheel mit Leitstand:**
Bei zentralem Steuerstand werden Clutches oft seitlich auf den Cockpit-Süllern montiert, wobei die Leinen durch Decksdurchführungen geführt werden.

**Tiller-Steuerung:**
Bei Pinnensteuerung (üblich bis 10 m) sind die Clutches auf dem Cockpitboden oder auf dem Kajütdach montiert. Die Erreichbarkeit ist oft eingeschränkt — kurze Abstände zum Steuermann sind kritisch.

**Open-Transom-Design:**
Moderne Yachten mit offenem Heck erfordern Clutch-Positionen weiter vorne im Cockpit, um Wassereinbruch bei schwerem Wetter zu vermeiden. Die Leinenführung wird komplexer, aber die Ergonomie profitiert.

### V.7 Zukunftstrends

**Digitale Clutch-Überwachung:**
Sensoren in Clutches, die Last, Temperatur und Verschleiß in Echtzeit messen. Daten werden über Bluetooth oder NMEA 2000 an den Bordcomputer übertragen. Spinlock und Harken entwickeln Prototypen.

**Selbsttätige Clutches:**
Clutches, die sich bei Überlast automatisch öffnen (Sollbruch-Funktion). Verhindert Rigg-Schäden. In der Entwicklung bei mehreren Herstellern.

**3D-gedruckte Cam Cleats:**
Für Prototypen und Sonderanwendungen werden Cam Cleats zunehmend im SLS-Verfahren (Selective Laser Sintering) aus PA12 gefertigt. Festigkeitswerte erreichen ca. 70% der spritzgegossenen Pendants.

**Recycelte Materialien:**
Clamcleat hat 2025 eine Composite-Serie aus recyceltem Meeresplastik vorgestellt. Festigkeitswerte sind mit Standard-Composite vergleichbar. Preis: ca. 10% Aufschlag.

**Integrierte Leinenzähler:**
Rope Clutches mit integrierten Hall-Sensor-basierten Leinenzählern werden von mehreren Herstellern als Prototyp getestet. Die Leinenposition wird auf dem Multifunktionsdisplay angezeigt — besonders hilfreich für reproduzierbare Segel-Trimmung bei Regatten und für Einhandsegler.

**Gewichtsoptimierung durch additive Fertigung:**
Topologie-optimierte Clutch-Gehäuse aus Titan (SLM-Verfahren) könnten das Gewicht um 40–50% reduzieren bei gleicher Festigkeit. Derzeit in der Prototyp-Phase bei einem britischen Start-up (Ocean Engineering Labs).

### V.8 Checkliste für Neubau und Refit

Bei der Planung eines Neubaus oder umfassenden Refits sind folgende Punkte für die Cam-Cleat- und Clutch-Ausstattung zu beachten:

**Planungsphase:**
- [ ] Alle Leinen identifizieren (Fallen, Schoten, Strecker, Reffleinen)
- [ ] Erwartete Maximallasten pro Leine berechnen oder schätzen
- [ ] Leinendurchmesser festlegen
- [ ] Clutch-Typ pro Position bestimmen (Cam Cleat vs. Rope Clutch)
- [ ] Clutch-Marke und -Serie wählen
- [ ] Clutch-Bank-Konfiguration festlegen (Anzahl Positionen pro Bank)
- [ ] Cockpit-Layout planen (Abstände zu Winschen, Erreichbarkeit)
- [ ] Fairleads und Umlenkrollen planen
- [ ] Decksverstärkung planen (Backing Plates, Kernkompression)
- [ ] Budget kalkulieren (Beschläge + Montage + Material)

**Beschaffungsphase:**
- [ ] Clutches und Cam Cleats bestellen
- [ ] Backing Plates anfertigen oder bestellen
- [ ] Schrauben in korrekter Größe und Material (316L) beschaffen
- [ ] Dichtmittel (Sikaflex 291 oder 3M 4200) beschaffen
- [ ] Epoxy für Lochversiegelung beschaffen
- [ ] Bohrschablonen vom Hersteller anfordern oder anfertigen
- [ ] Schmiermittel (McLube SailKote) beschaffen

**Montagephase:**
- [ ] Positionen auf Deck anzeichnen (Leinenführung simulieren)
- [ ] Einlaufwinkel prüfen (Leine spannen, Winkel messen)
- [ ] Bohrlöcher setzen und versiegeln
- [ ] Sandwich-Kern im Befestigungsbereich verfüllen (bei Bedarf)
- [ ] Backing Plates positionieren
- [ ] Dichtmittel auftragen
- [ ] Clutches montieren und Schrauben anziehen (korrektes Drehmoment!)
- [ ] Aushärten lassen (24h)
- [ ] Funktionstest jeder Position mit Leine
- [ ] Leinenmarkierungen anbringen (Farbe oder Beschriftung)
- [ ] Dokumentation erstellen (Position → Leine → Clutch-Typ)

**Abnahme:**
- [ ] Alle Clutches öffnen und schließen (ohne Last)
- [ ] Halte-Test mit Handkraft (alle Positionen)
- [ ] Release-Test unter simulierter Last (falls möglich)
- [ ] Dichtigkeit der Schraubenlöcher prüfen (Wassertest)
- [ ] Farbcodierung und Beschriftung vollständig
- [ ] Crew-Einweisung durchführen
- [ ] Wartungsplan erstellen und aushängen

---

> **Ende der Wissensdatei 11.02 — Cam Cleats und Klemmen im Yachtbau**
> **AYDI Research** | Version 1.0.0 | 2026-04-25
> **Nächste geplante Aktualisierung:** 2026-10-25 (Halbjährlich)
