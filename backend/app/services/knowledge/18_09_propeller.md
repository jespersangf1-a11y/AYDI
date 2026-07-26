---
titel: "Propeller — Typen, Dimensionierung und Optimierung"
kategorie: "Motoren und Antrieb"
unterkategorie: "Propeller"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_09 — Propeller — Typen, Dimensionierung und Optimierung

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Propeller-Grundlagen](#2-propeller-grundlagen)
3. [Festpropeller](#3-festpropeller)
4. [Faltpropeller](#4-faltpropeller)
5. [Verstellpropeller (Feathering)](#5-verstellpropeller-feathering)
6. [Saildrive-Propeller](#6-saildrive-propeller)
7. [Propeller-Materialien](#7-propeller-materialien)
8. [Dimensionierung und Auslegung](#8-dimensionierung-und-auslegung)
9. [Kavitation](#9-kavitation)
10. [Propeller-Balance und Vibration](#10-propeller-balance-und-vibration)
11. [Propeller-Schutz und Antifouling](#11-propeller-schutz-und-antifouling)
12. [Hersteller und Marktübersicht](#12-hersteller-und-marktübersicht)
13. [Fehlerbild-Atlas](#13-fehlerbild-atlas)
14. [Troubleshooting](#14-troubleshooting)
15. [FAQ](#15-faq)
16. [Glossar](#16-glossar)
17. [Schnell-Referenz](#17-schnell-referenz)
18. [ANHANG A–H: Fallstudien](#18-anhang-ah-fallstudien)
19. [ANHANG I–R: Pydantic v2 Datenmodelle](#19-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Die Bedeutung des Propellers im Antriebssystem

Der Propeller ist das zentrale Bindeglied zwischen Motor und Wasser — er wandelt
die Drehbewegung der Motorwelle in Schub (Thrust) um. Ein perfekt gewarteter Motor
mit einem falsch dimensionierten oder beschädigten Propeller liefert bestenfalls
60–70 % der möglichen Leistung. Die Propellerwahl beeinflusst:

- **Geschwindigkeit**: Ein optimal abgestimmter Propeller nutzt die verfügbare
  Motorleistung maximal aus. Die Differenz zwischen gutem und schlechtem Propeller
  beträgt 15–25 % bei der Höchstgeschwindigkeit.
- **Kraftstoffverbrauch**: Falsche Propellerdimensionierung kann den
  Kraftstoffverbrauch um 20–40 % erhöhen.
- **Motordrehzahl**: Der Propeller bestimmt die Drehzahl, bei der der Motor
  unter Volllast arbeitet (Prop Curve). Ein falsch ausgelegter Propeller führt
  zu Über- oder Unterdrehzahl.
- **Motorlebensdauer**: Ein zu großer Propeller (overpropping) erzwingt dauerhaft
  hohe Drehmomente bei niedrigen Drehzahlen — Motorschaden droht.
- **Fahrverhalten**: Manövrierbarkeit, Rückwärtsfahrt, Seitenversatz, Vibrationen
  — alles hängt vom Propeller ab.
- **Segelperformance** (Segelyachten): Ein unter Segeln mitdrehender Festpropeller
  erzeugt erheblichen Widerstand. Falt- und Feathering-Propeller lösen dieses Problem.

**Marktstatistik 2025:**
- Weltmarkt Marine-Propeller (Sportschifffahrt): ~450 Mio. EUR
- Durchschnittlich werden 12–15 % aller Propeller bei der Jahresinspektion als
  reparaturbedürftig eingestuft
- Falt- und Feathering-Propeller machen bei Segelyachten >35 Fuß mittlerweile
  ~65 % der Neuinstallationen aus
- Der Trend geht zu hocheffizienten Propellern mit computergeneriertem Blattprofil

### 1.2 Geschichte des Marine-Propellers

Die Entwicklung des Schiffspropellers ist eine faszinierende Ingenieursgeschichte:

- **1770**: James Watt experimentiert mit propellerähnlichen Wasserrädern
- **1827**: Josef Ressel (Österreich) testet den ersten Schraubenpropeller
  am Schiff „Civetta" im Hafen von Triest
- **1836**: John Ericsson (Schweden/USA) und Francis Pettit Smith (England)
  melden unabhängig Schraubenpropeller-Patente an
- **1843**: SS Great Britain — erstes großes eisernes Schraubenschiff
- **1845**: Berühmter „Tug of War" zwischen HMS Rattler (Schraube) und
  HMS Alecto (Schaufelrad) — Schraube gewinnt eindeutig
- **1880er**: Kavitationsforschung beginnt (Osborne Reynolds, William Froude)
- **1900–1920**: Systematische Propellerforschung (Taylor, Troost, Wageningen)
- **1930er**: Erste Faltpropeller für Segelyachten
- **1937**: Wageningen B-Serie — Systematische Propeller-Testreihe, die bis
  heute die Grundlage der Propellerauslegung bildet
- **1950er**: Martec (später Flexofold) entwickelt moderne Faltpropeller
- **1970er**: Max-Prop (Italien) revolutioniert den Feathering-Propeller-Markt
- **1980er**: Computersimulation (CFD) beginnt, Propellerdesign zu verändern
- **1990er**: Gori (Dänemark) führt 2-Gang-Faltpropeller ein
- **2000er**: Kiwiprop (Neuseeland) — selbstanpassender Autopropeller
- **2010er**: 3D-gedruckte Propeller im Prototypenstadium
- **2020er**: CFD-optimierte Composite-Propeller, E-Antrieb-spezifische Designs

### 1.3 Propellertypen im Überblick

| Typ | Einsatz | Segelwiderstand | Rückwärts | Preis (EUR) |
|-----|---------|:---:|:---:|:---:|
| Festpropeller 2-Blatt | Segelyacht (Motor selten) | Hoch | Mäßig | 200–800 |
| Festpropeller 3-Blatt | Motor- & Segelyacht | Hoch | Gut | 300–1.500 |
| Festpropeller 4-Blatt | Motoryacht, Verdränger | Hoch | Sehr gut | 500–2.500 |
| Faltpropeller 2-Blatt | Segelyacht (Cruising) | Sehr gering | Mäßig–Gut | 800–2.500 |
| Faltpropeller 3-Blatt | Segelyacht (Cruising/Performance) | Sehr gering | Gut | 1.200–3.500 |
| Feathering 2-Blatt | Segelyacht | Minimal | Gut | 1.500–3.000 |
| Feathering 3-Blatt | Segelyacht (Premium) | Minimal | Sehr gut | 2.000–4.500 |
| Verstellpropeller (CPP) | Motoryacht >15 m | – | Variabel | 5.000–25.000+ |

### 1.4 Relevanz im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems beeinflusst der Propeller folgende Module:

- **Kosten-Modul**: Propeller sind ein signifikanter Kostenfaktor (300–5.000+ EUR)
- **Performance-Modul**: Propellerwahl bestimmt Geschwindigkeit, Verbrauch, Reichweite
- **Compliance-Modul**: CE-Konformität erfordert korrekte Motor-Propeller-Abstimmung
- **Service-Modul**: Propellerwartung ist Teil des jährlichen Wartungsplans
- **Strukturell-Modul**: Propellervibrationen beeinflussen Wellenanlage und Rumpf

---
---

## 2. Propeller-Grundlagen

### 2.1 Funktionsprinzip — Wie erzeugt ein Propeller Schub?

Ein Propeller funktioniert wie ein rotierendes Tragflächenprofil im Wasser.
Jedes Propellerblatt ist ein hydrodynamisches Profil (Airfoil/Hydrofoil),
das durch seine Drehung eine Druckdifferenz zwischen Saug- (Vorderseite)
und Druckseite (Rückseite) erzeugt. Diese Druckdifferenz resultiert in
einer Kraft senkrecht zur Blattfläche, deren Komponente in Fahrtrichtung
den Schub (Thrust) darstellt.

**Grundlegende Physik:**

```
Thrust (T) = Druckdifferenz × Blattfläche × Anzahl Blätter × cos(Anstellwinkel)
```

Vereinfacht nach der Impulstheorie (Rankine-Froude):

```
T = ṁ × Δv = ρ × A × V × (V_exit - V_entry)

wobei:
  ṁ = Massenstrom [kg/s]
  Δv = Geschwindigkeitsänderung des Wassers [m/s]
  ρ = Wasserdichte [kg/m³] (Süßwasser ~1.000, Seewasser ~1.025)
  A = Propellerkreisfläche [m²]
  V = Anströmgeschwindigkeit [m/s]
```

### 2.2 Die fünf Kernparameter eines Propellers

#### 2.2.1 Durchmesser (Diameter, D)

Der Durchmesser ist der Kreisdurchmesser, den die Blattspitzen beschreiben.
Er ist der wichtigste Parameter für den Schub.

**Physikalische Bedeutung:**
- Thrust steigt proportional zu D⁴ (bei konstanter Drehzahl)
- Drehmoment steigt proportional zu D⁵
- Ein größerer Propeller bewegt mehr Wasser bei niedrigerer Geschwindigkeit
  → höherer Wirkungsgrad

**Typische Durchmesser nach Bootsgröße:**

| Bootslänge (m) | Motorleistung (PS) | Propellerdurchmesser (mm) |
|:---:|:---:|:---:|
| 7–9 | 10–25 | 250–350 |
| 9–11 | 20–40 | 300–400 |
| 11–13 | 30–55 | 350–450 |
| 13–15 | 40–75 | 400–500 |
| 15–18 | 55–120 | 450–600 |
| 18–22 | 100–250 | 550–750 |
| 22–30 | 200–600 | 700–1.000 |

**Begrenzende Faktoren:**
- Abstand Blattspitze → Rumpf: mindestens 15 % des Durchmessers (besser 20 %)
- Eintauchtiefe: Blattspitze muss bei jeder Lage vollständig eingetaucht sein
- Stevenrohr/Saildrive-Gehäuse: limitiert maximalen Durchmesser
- Bei Segelyachten: Propelleröffnung im Ruder oder Skeg

#### 2.2.2 Steigung (Pitch, P)

Die Steigung ist die theoretische Vorwärtsbewegung pro Umdrehung — analog
zur Ganghöhe einer Schraube.

**Physikalische Bedeutung:**
- Gemessen in Zoll oder Millimetern
- Pitch = theoretischer Vorschub pro Umdrehung in einem festen Medium
- Hoher Pitch = „hoher Gang" — mehr Geschwindigkeit bei gleicher Drehzahl
- Niedriger Pitch = „niedriger Gang" — mehr Schubkraft bei gleicher Drehzahl

**Pitch-Ratio (P/D):**

```
Pitch-Ratio = Steigung / Durchmesser

Typische Werte:
  Verdränger (Motorboot): 0,8–1,0
  Halbgleiter: 1,0–1,4
  Gleiter: 1,4–2,2
  Segelyacht: 0,6–1,0
```

**Pitch-Änderungen und ihre Wirkung:**

| Änderung | Auswirkung auf Drehzahl | Auswirkung auf Geschwindigkeit |
|----------|:---:|:---:|
| +1" Pitch | −150 bis −200 U/min | +1–2 kn (wenn Motor nicht überlastet) |
| −1" Pitch | +150 bis +200 U/min | −1–2 kn (Motor dreht freier) |
| +2" Pitch | −300 bis −400 U/min | Überladung → Motor schaden |
| −2" Pitch | +300 bis +400 U/min | Motor überdreht → Verschleiß |

#### 2.2.3 Blattflächenverhältnis (Blade Area Ratio, BAR)

Das Blattflächenverhältnis ist das Verhältnis der Gesamtblattfläche
zur Propellerkreisfläche.

```
BAR = (Anzahl Blätter × Einzelblattfläche) / (π/4 × D²)

Typische Werte:
  2-Blatt Segelyacht: 0,30–0,40
  3-Blatt Cruiser: 0,45–0,55
  3-Blatt Motoryacht: 0,50–0,65
  4-Blatt Verdränger: 0,55–0,70
  Hochleistung: 0,70–0,85
```

**Bedeutung:**
- Höheres BAR → mehr Schub bei gleicher Drehzahl, aber mehr Widerstand
- Höheres BAR → geringere Kavitationsneigung (Kraft verteilt sich auf mehr Fläche)
- Niedrigeres BAR → höherer Wirkungsgrad (weniger Reibung), aber Kavitationsrisiko

#### 2.2.4 Rake (Blattneigung)

Rake ist der Winkel, um den die Blätter aus der Propellerebene nach
hinten (positiver Rake) oder vorn (negativer Rake) geneigt sind.

**Typische Werte:**
- Standard-Propeller: 0°–15° positiver Rake
- Hochleistungspropeller: 15°–25° positiver Rake
- Tunnelheck-Propeller: 0°–5° oder negativer Rake

**Auswirkungen:**
- Positiver Rake: bessere Kavitationseigenschaften, Propeller „zieht" sich
  aus dem Kavitationsbereich, geringere Druckimpulse auf den Rumpf
- Negativer Rake: kompaktere Bauweise, weniger Biegemoment am Blatt
- Mehr Rake erhöht die Biegebelastung der Blätter

#### 2.2.5 Skew (Blattverwindung)

Skew beschreibt die Sichelform der Blätter — die Verdrehung der Blattvorderkante
gegenüber der radialen Linie.

**Typische Werte:**
- Standard: 0°–15°
- Moderate Skew: 15°–30°
- High Skew: 30°–90° (U-Boot-Propeller, Superyachten)

**Auswirkungen:**
- Höherer Skew → weniger Vibrationen (Blätter treten graduell in Störungszonen ein)
- Höherer Skew → geringere Druckpulsationen auf den Rumpf
- Höherer Skew → leiser
- Nachteil: reduzierter Wirkungsgrad, teurer in der Fertigung

### 2.3 Cup (Blattlippenprofil)

Cup ist eine leichte Aufwärtskrümmung der Blatthinterkante. Es wirkt wie eine
virtuelle Pitch-Erhöhung und verbessert das Kavitationsverhalten.

**Typische Cup-Höhe:** 0,5–3 mm

**Auswirkungen:**
- Cup wirkt wie +1" bis +2" Pitch am Blattaustritt
- Verbessert das Greifen des Propellers bei Belüftung (belüfteter Propeller
  „verliert" weniger Schub)
- Verzögert den Kavitationsbeginn am Blattaustritt
- Leicht erhöhter Widerstand im Leerlauf/unter Segeln

**Cup vs. Pitch-Erhöhung:**
Cup bietet ähnliche Effekte wie eine Pitch-Erhöhung, aber ohne die Nachteile
des erhöhten Drehmoments bei niedrigen Geschwindigkeiten. Es ist quasi ein
„kostenloser" halber Zoll Pitch — besonders wirksam bei Gleiterbooten.

### 2.4 Slip — Theorie vs. Realität

Slip ist die Differenz zwischen der theoretischen Vorwärtsbewegung (Pitch × Drehzahl)
und der tatsächlichen Geschwindigkeit durch das Wasser.

```
Slip (%) = ((Pitch × RPM) − (Geschwindigkeit × 1.852/60)) / (Pitch × RPM) × 100

Beispiel:
  Pitch = 12" = 304,8 mm
  RPM = 2.500
  Geschwindigkeit = 6,5 kn

  Theoretischer Vorschub = 304,8 mm × 2.500 / 60 = 12.700 mm/s = 24,7 kn
  Slip = (24,7 − 6,5) / 24,7 × 100 = 73,7 %
```

**Achtung:** Dieser „simple Slip" ist bei Verdrängerfahrt normal hoch!

**Typische Slip-Werte:**

| Bootstyp | Normaler Slip (%) |
|----------|:---:|
| Gleiter (bei Gleitfahrt) | 5–15 |
| Halbgleiter | 15–30 |
| Verdränger (Motorboot) | 30–50 |
| Segelyacht (unter Motor) | 40–60 |
| Schwerer Verdränger | 50–70 |

**Interpretation:**
- Slip < 10 %: Propeller zu klein oder zu wenig Pitch (Motor überdreht)
- Slip 10–20 %: Optimal für Gleiter in Gleitfahrt
- Slip 20–40 %: Normal für Verdränger und Segelyachten
- Slip > 50 %: Propeller möglicherweise falsch dimensioniert oder verschmutzt
- Plötzliche Slip-Erhöhung: Bewuchsproblem, Propellerschaden, Getriebeproblem

### 2.5 Propellerwirkungsgrad (Efficiency)

Der Propellerwirkungsgrad η (Eta) beschreibt, wie viel der zugeführten
Wellenleistung in Schub umgewandelt wird.

```
η = (Schubkraft × Bootgeschwindigkeit) / (Wellenleistung)
η = T × V_s / (2π × n × Q)

wobei:
  T = Schub [N]
  V_s = Bootsgeschwindigkeit [m/s]
  n = Drehzahl [1/s]
  Q = Drehmoment [Nm]
```

**Typische Wirkungsgrade:**

| Propellertyp | η (Open Water) | η (Behind Hull) |
|-------------|:---:|:---:|
| Festpropeller (optimal) | 55–65 % | 45–55 % |
| Festpropeller (Standard) | 45–55 % | 35–45 % |
| Faltpropeller (angetrieben) | 50–60 % | 40–50 % |
| Feathering-Propeller | 55–65 % | 45–55 % |
| Verstellpropeller (CPP) | 50–60 % | 40–50 % |

**Wirkungsgradverluste:**
- Hinter dem Rumpf (Wake-Einfluss): −5 bis −15 %
- Bewuchs: −5 bis −30 % (je nach Stärke)
- Beschädigung: −5 bis −20 %
- Kavitation: −5 bis −40 %
- Fehlausrichtung: −5 bis −15 %

### 2.6 Drehrichtung und Seitenversatz

**Drehrichtung:**
- Standard: Rechts drehend (clockwise von achtern gesehen, Vorwärtsfahrt)
- Links drehend: Typisch für Backbord-Motor bei Doppelanlagen
- Bei Doppelanlagen: gegenläufig (counter-rotating) für besseres Geradeauslaufverhalten

**Seitenversatz (Propellereffekt):**
Ein Propeller erzeugt neben dem Vorschub auch einen seitlichen Druck:

```
Rechts drehend → Vorwärtsfahrt → Heck geht nach Steuerbord
Rechts drehend → Rückwärtsfahrt → Heck geht nach Backbord (stärker!)
```

**Einflussfaktoren auf den Seitenversatz:**
- Blattanzahl: Weniger Blätter → mehr Seitenversatz
- Drehzahl: Höher → mehr Seitenversatz
- Geschwindigkeit: Gering → Seitenversatz dominanter
- Propellerposition: Asymmetrischer Abstand zum Rumpf verstärkt Effekt

### 2.7 Propellerkoeffizienten

Für die systematische Propellerauslegung werden dimensionslose Koeffizienten verwendet:

**Schubbeiwert K_T:**
```
K_T = T / (ρ × n² × D⁴)
```

**Drehmomentenbeiwert K_Q:**
```
K_Q = Q / (ρ × n² × D⁵)
```

**Fortschrittsgrad J:**
```
J = V_a / (n × D)

wobei:
  V_a = Anströmgeschwindigkeit am Propeller [m/s]
  n = Drehzahl [1/s]
  D = Durchmesser [m]
```

**Wirkungsgrad aus Koeffizienten:**
```
η = (J / (2π)) × (K_T / K_Q)
```

Diese Koeffizienten sind die Grundlage der Wageningen B-Serie-Diagramme
und aller modernen CFD-Propellerberechnungen.

---
---

## 3. Festpropeller

### 3.1 Grundprinzip

Festpropeller (fixed-pitch propeller, FPP) haben starre, nicht verstellbare Blätter.
Die Blätter sind entweder aus einem Stück gegossen oder als einzelne Blätter
in eine Nabe geschraubt/gepresst. Sie sind die einfachste, robusteste und
preisgünstigste Propellerform.

**Vorteile:**
- Einfachster Aufbau — keine beweglichen Teile
- Höchste Zuverlässigkeit (nichts kann klemmen oder versagen)
- Günstigster Preis
- Leicht reparierbar (Blätter können gerichtet werden)
- Optimaler Wirkungsgrad bei genau einem Betriebspunkt

**Nachteile:**
- Hoher Widerstand unter Segeln (bei Segelyachten)
- Nicht anpassbar an verschiedene Betriebsbedingungen
- Kompromiss zwischen Vorwärts- und Rückwärtsleistung
- Wirkungsgrad sinkt schnell bei abweichenden Betriebsbedingungen

### 3.2 Zwei-Blatt-Festpropeller

Der 2-Blatt-Propeller war lange Zeit der Standard für Segelyachten mit
Wellenantrieb. Heute wird er zunehmend von Falt- und Feathering-Propellern
verdrängt, ist aber bei kleinen Booten (<10 m) und als Budgetlösung
noch verbreitet.

**Eigenschaften:**
- Niedrigstes BAR (0,30–0,40) → geringster Widerstand unter Segeln
- Kann hinter dem Kiel oder Skeg „versteckt" werden (Blätter vertikal)
- Höchster Wirkungsgrad bei niedrigem Schub
- Neigt bei hoher Last zu Kavitation (wenig Blattfläche)
- Starke Vibrationen bei bestimmten Drehzahlen (Resonanz)
- Schlechte Rückwärtsleistung

**Typische Anwendung:**
- Segelyachten 6–10 m mit Wellenantrieb
- Langfahrt-Segelyachten (Budgetlösung)
- Beiboote mit Innenbordmotor

**Produkte und Preise:**

| Hersteller | Modell | Material | Größe (") | Preis (EUR) |
|------------|--------|----------|:---------:|:-----------:|
| Michigan Wheel | Sailor | Manganbronze | 10–16 | 180–450 |
| Vetus | Type 2 | Manganbronze | 10–18 | 200–550 |
| Bruntons | AutoProp 2-Blade | Ni-Al-Bronze | 12–20 | 1.800–3.200 |

### 3.3 Drei-Blatt-Festpropeller

Der 3-Blatt-Propeller ist der universelle Standard — sowohl für Motor-
als auch für Segelyachten. Er bietet den besten Kompromiss zwischen
Schub, Laufruhe und Wirkungsgrad.

**Eigenschaften:**
- BAR typisch 0,45–0,55
- Deutlich ruhigerer Lauf als 2-Blatt (120°-Symmetrie)
- Gutes Rückwärtsverhalten
- Moderate Kavitationsneigung
- Guter Kompromiss Vorwärts/Rückwärts
- Höherer Widerstand unter Segeln als 2-Blatt

**Typische Anwendung:**
- Segelyachten >10 m mit vorrangig Motornutzung
- Motoryachten 7–15 m (Verdränger und Halbgleiter)
- Arbeitsboote, Fischerboote

**Produkte und Preise:**

| Hersteller | Modell | Material | Größe (") | Preis (EUR) |
|------------|--------|----------|:---------:|:-----------:|
| Michigan Wheel | Match | Manganbronze | 10–20 | 250–850 |
| Vetus | Type 3 | Manganbronze | 10–22 | 300–1.100 |
| Flexofold | — (auch Festpropeller) | Ni-Al-Bronze | 12–22 | 350–950 |
| Bruntons | Varifold 3 | Ni-Al-Bronze | 12–24 | 400–1.200 |
| Sole Diesel | OEM 3-Blatt | Manganbronze | 12–18 | 280–650 |

### 3.4 Vier-Blatt-Festpropeller

4-Blatt-Propeller werden primär bei Motoryachten eingesetzt, wo maximaler
Schub, Laufruhe und gutes Rückwärtsverhalten wichtiger sind als der
Segelwiderstand.

**Eigenschaften:**
- BAR typisch 0,55–0,70
- Sehr ruhiger Lauf (90°-Symmetrie)
- Exzellentes Rückwärtsverhalten
- Geringe Kavitationsneigung
- Höchster Schub bei niedrigen Drehzahlen
- Geringerer Spitzenwirkungsgrad als 3-Blatt
- Nicht sinnvoll für Segelyachten (zu viel Widerstand)

**Typische Anwendung:**
- Motoryachten >12 m (Verdränger)
- Trawler und Langfahrt-Motorboote
- Schwere Verdränger mit niedrigtourigen Motoren
- Doppelmotoranlagen (Manövrierfähigkeit)

**Produkte und Preise:**

| Hersteller | Modell | Material | Größe (") | Preis (EUR) |
|------------|--------|----------|:---------:|:-----------:|
| Michigan Wheel | Dyna Quad | Ni-Al-Bronze | 14–28 | 800–2.500 |
| Vetus | Type 4 | Manganbronze | 14–24 | 650–1.800 |
| Bruntons | SiComp 4 | Composite | 14–22 | 1.200–2.200 |
| Ewol (PL) | Custom 4-Blatt | Manganbronze | 16–30 | 900–2.800 |

### 3.5 Material-Varianten bei Festpropellern

#### 3.5.1 Manganbronze (Standard)

- Zusammensetzung: Cu 55–60 %, Zn 38–42 %, Mn 1–2 %, Fe/Al <1 %
- Günstig, gut gießbar, ausreichend für die meisten Anwendungen
- **Nachteil**: Anfällig für Entzinkung (dezincification) in Seewasser
- **Nachteil**: Weicher als Ni-Al-Bronze → schnellere Erosion
- Lebensdauer mit Anodenschutz: 10–20 Jahre
- Ohne Anodenschutz: 3–8 Jahre (je nach Gewässer)

#### 3.5.2 Nickel-Aluminium-Bronze (Ni-Al-Bronze, NAB)

- Zusammensetzung: Cu 79–82 %, Al 8,5–10,5 %, Ni 4–5,5 %, Fe 3–5 %, Mn 0,5–1,5 %
- Deutlich korrosionsbeständiger als Manganbronze
- Härter und erosionsbeständiger
- Weniger anfällig für galvanische Korrosion
- **Standard für hochwertige Propeller** ab ~14" Durchmesser
- Lebensdauer: 20–40+ Jahre
- Preis: ~50–80 % teurer als Manganbronze

#### 3.5.3 Edelstahl (316L / Duplex)

- Edelstahl-Propeller bieten höchste Festigkeit und Verschleißbeständigkeit
- AISI 316L: Standard-Marine-Edelstahl, gut für Süß- und Brackwasser
- Duplex 2205: Deutlich besser für Seewasser (höhere Lochfraßbeständigkeit)
- **Vorteil**: Dünnere Blätter möglich → höherer Wirkungsgrad
- **Nachteil**: Spaltkorrosion möglich (bei 316L in stagnierendem Seewasser)
- **Nachteil**: Nicht reparierbar durch einfaches Richten (muss geschweißt werden)
- Preis: ~100–150 % teurer als Manganbronze

#### 3.5.4 Composite (GFK/CFK)

- Glasfaser- oder Kohlefaserverstärkter Kunststoff mit Edelstahl-Nabe
- Extrem leicht → weniger Wellenbelastung, weniger Vibrationen
- Federnde Blätter absorbieren Stöße (Grundberührung, Treibgut)
- **Vorteil**: Bei Grundberührung brechen die Blätter statt der Welle
- **Vorteil**: Kein galvanisches Korrosionsproblem
- **Nachteil**: Nicht reparierbar bei Bruch
- **Nachteil**: Geringere Erosionsbeständigkeit bei Sand/Sediment
- Hersteller: Flexofold, Bruntons (SiComp), Torqeedo
- Preis: Vergleichbar mit Ni-Al-Bronze

---
---

## 4. Faltpropeller

### 4.1 Grundprinzip

Faltpropeller (folding propeller) haben bewegliche Blätter, die sich unter
Segeln zusammenfalten und so den Wasserwiderstand drastisch reduzieren.
Beim Einschalten des Motors öffnen sich die Blätter durch die Fliehkraft
und den Wasserdruck.

**Funktionsweise:**
1. **Motor an, Vorwärtsgang**: Blätter öffnen sich durch Fliehkraft und
   Wasserströmung. Arretierung hält sie in Arbeitsposition.
2. **Motor aus, unter Segeln**: Blätter falten sich zusammen (Federkraft
   oder Strömungskraft). Minimaler Strömungswiderstand.
3. **Rückwärtsgang**: Blätter öffnen sich in die entgegengesetzte Richtung.
   Bei älteren Designs oft problematisch.

**Widerstandsreduktion unter Segeln:**

| Propellertyp | C_d (Widerstandsbeiwert) | Widerstand bei 6 kn (N) |
|-------------|:---:|:---:|
| 3-Blatt Festpropeller | 0,40–0,50 | 120–180 |
| 2-Blatt Festpropeller (vertikal) | 0,25–0,35 | 70–120 |
| Faltpropeller (gefaltet) | 0,02–0,05 | 5–15 |
| Feathering-Propeller | 0,03–0,06 | 8–20 |

→ Ein Faltpropeller reduziert den Propellerwiderstand unter Segeln um 85–95 %.

### 4.2 Faltpropeller-Typen

#### 4.2.1 Einfache Faltpropeller (2-Blatt)

Die klassische Form — zwei Blätter, die sich in der Nabe nach
hinten zusammenfalten.

**Mechanismus:**
- Blätter sind über Bolzen in der Nabe gelagert
- Öffnung durch Fliehkraft bei Motordrehzahl
- Schließung durch Federkraft oder Strömung
- Kein aktiver Mechanismus — rein passiv

**Einschränkungen:**
- Öffnungswinkel oft nicht voll 180°
- Rückwärtsbetrieb: Blätter öffnen sich oft nicht vollständig
- Bei niedrigen Drehzahlen (Ladegenerator) falten die Blätter
  nicht immer sauber auf

#### 4.2.2 Geared Faltpropeller (Zahnrad-gesteuert)

Moderne Faltpropeller verwenden ein Zahnradsystem in der Nabe,
das alle Blätter synchron öffnet und eine definierte Blattposition
in Vorwärts- und Rückwärtsfahrt garantiert.

**Mechanismus:**
- Zahnräder (Gears) in der Nabe verbinden alle Blätter
- Rotation der Welle → Zahnräder drehen die Blätter synchron auf
- Vorwärts: Blätter stehen im optimalen Angriffswinkel
- Rückwärts: Zahnräder drehen die Blätter in die
  entgegengesetzte Position → voller Rückwärtsschub

**Vorteile gegenüber einfachem Faltpropeller:**
- 100 % Rückwärtsleistung (vs. 50–70 % bei einfachen)
- Gleichmäßiges Öffnen → weniger Vibrationen beim Start
- Definierte Blattposition → höherer Wirkungsgrad
- Besseres Ansprechverhalten bei niedrigen Drehzahlen

### 4.3 Flexofold (Dänemark)

Flexofold ist der Marktführer für Faltpropeller im Segelyachtbereich und
wurde 2005 in Dänemark gegründet. Das Unternehmen hat den Markt mit
dem ersten vollständig zahnradgesteuerten Faltpropeller revolutioniert.

**Technologie:**
- Patentiertes Zahnrad-Faltsystem (Geared Folding)
- Blätter öffnen synchron und schließen symmetrisch
- 100 % Rückwärtsleistung (einzigartiges Merkmal bei Faltpropellern)
- Composite-Optionen für Gewichtsreduzierung

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Flexofold 2-Blade | 2 | Welle | 13–22 | 980–2.200 |
| Flexofold 3-Blade | 3 | Welle | 14–24 | 1.350–2.800 |
| Flexofold 2-Blade SD | 2 | Saildrive | 13–20 | 1.050–2.350 |
| Flexofold 3-Blade SD | 3 | Saildrive | 14–22 | 1.450–2.950 |
| Flexofold Composite 2 | 2 | Welle/SD | 14–19 | 1.250–2.100 |
| Flexofold Composite 3 | 3 | Welle/SD | 15–21 | 1.650–2.700 |

**Materialien:**
- Standard: Ni-Al-Bronze (NAB)
- Composite: Glasfaser-verstärkter Kunststoff mit Bronze-Nabe
- Edelstahl-Bolzen und -Zahnräder in der Nabe

**Wartung:**
- Alle 2–3 Jahre: Nabe öffnen, Zahnräder inspizieren, fetten
- Empfohlenes Fett: Flexofold Original Grease oder Marine-Lithiumfett
- Anoden: Alle 1–2 Jahre (Flexofold-eigene Anode auf der Nabe)
- Kein Wintereinlagern der Nabe nötig — Fett schützt ausreichend

**Erfahrungswerte:**
- Wirkungsgrad unter Motor: 92–96 % eines vergleichbaren Festpropellers
- Widerstandsreduktion unter Segeln: 88–94 %
- Lebensdauer Zahnräder: 10.000+ Betriebsstunden
- Häufigstes Problem: Fett verbraucht → Zahnräder laufen schwer → Blätter
  öffnen verzögert

### 4.4 Volvo Penta Folding Propeller

Volvo Penta bietet als OEM-Zulieferer für ihre Saildrive-Systeme (SD110/SD130/SD150)
eigene Faltpropeller an.

**Produktlinie:**

| Modell | Blätter | Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------|:---------:|:-----------:|
| Volvo 2-Blade Folding | 2 | S-Drive | 15–19 | 850–1.400 |
| Volvo 3-Blade Folding | 3 | S-Drive | 16–20 | 1.200–1.900 |

**Besonderheiten:**
- Optimiert für Volvo Saildrive-Systeme
- Einfaches Falt-Design ohne Zahnradsteuerung (ältere Modelle)
- Neuere Modelle (ab 2018) mit verbessertem Faltsystem
- Nur für Volvo Saildrives passend — proprietäre Nabenverbindung

**Kritik:**
- Rückwärtsleistung bei älteren 2-Blatt-Modellen nur 50–65 %
- Preis-Leistung schlechter als Flexofold
- OEM-Bindung (nur Volvo-Händler)
- Wirkungsgrad etwas geringer als bei spezialisierten Herstellern

### 4.5 Gori (Dänemark)

Gori ist ein dänischer Hersteller, der seit den 1980er Jahren Faltpropeller
und verstellbare Propeller für Segelyachten produziert. Bekannt für den
patentierten 2-Gang-Mechanismus.

**Technologie:**
- Patentierter 2-Gang-Faltpropeller: „Low Speed" und „High Speed" Pitch
- Blätter haben zwei definierte Öffnungswinkel
- Rückwärtsfahrt mit optimiertem Blattwinkel
- Overdrive-Position für höhere Geschwindigkeiten bei reduzierter Last

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Gori 2-Blade | 2 | Welle | 12–18 | 850–1.600 |
| Gori 3-Blade | 3 | Welle | 13–22 | 1.200–2.400 |
| Gori 2-Blade SD | 2 | Saildrive | 13–18 | 950–1.750 |
| Gori 3-Blade SD | 3 | Saildrive | 14–20 | 1.350–2.600 |

**Besonderheiten:**
- 2-Gang-System einzigartig am Markt
- Dänische Fertigung, hohe Qualität
- Langfristig bewährt (>40 Jahre am Markt)
- Guter technischer Support

**Einschränkung:**
- 2-Gang-Umschaltung nicht bei allen Modellen zuverlässig
- Komplexerer Mechanismus als Flexofold → mehr Wartung
- Gori-spezifische Anoden erforderlich

### 4.6 Faltpropeller — Vergleichsmatrix

| Kriterium | Flexofold | Volvo Folding | Gori |
|-----------|:---------:|:------------:|:----:|
| Vorwärts-Wirkungsgrad | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Rückwärts-Leistung | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Falt-Widerstand | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Zuverlässigkeit | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Preis-Leistung | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Wartungsaufwand | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Saildrive-Kompatibilität | ★★★★★ | ★★★★★ (nur Volvo) | ★★★★☆ |
| Verfügbarkeit Ersatzteile | ★★★★☆ | ★★★★★ | ★★★☆☆ |

---
---

## 5. Verstellpropeller (Feathering)

### 5.1 Grundprinzip

Feathering-Propeller (Verstellpropeller) können ihre Blattstellung aktiv
oder passiv verändern. Im Gegensatz zu Faltpropellern, die sich zusammenklappen,
drehen Feathering-Propeller ihre Blätter so, dass die Blattvorderkante
in die Strömungsrichtung zeigt — ähnlich einer Windfahne.

**Vergleich Falten vs. Feathering:**

| Eigenschaft | Faltpropeller | Feathering-Propeller |
|------------|:---:|:---:|
| Blattbewegung | Klappen nach hinten | Drehen um Blattachse |
| Unter Segeln | Blätter zusammengeklappt | Blätter in Strömungsrichtung |
| Widerstand unter Segeln | Minimal (Nabe + gefaltete Blätter) | Minimal (Blätter als „Messer") |
| Vorwärts-Wirkungsgrad | 90–96 % eines Festpropellers | 95–102 % eines Festpropellers |
| Rückwärts-Wirkungsgrad | 70–100 % (je nach Typ) | 85–100 % |
| Mechanische Komplexität | Mittel | Hoch |
| Preis | EUR 800–3.000 | EUR 1.500–5.000 |

### 5.2 Max-Prop (Italien)

Max-Prop ist der Pionier und Marktführer bei Feathering-Propellern für
Segelyachten. Seit 1974 in Mailand (Italien) produziert, hat Max-Prop
den Standard für Feathering-Propeller gesetzt.

**Technologie:**
- Patentiertes internes Getriebe (Kegelräder/Bevel Gears)
- Blätter werden beim Umschalten Vorwärts/Rückwärts durch das Getriebe
  in die optimale Position gedreht
- Unter Segeln: Wasser drückt die Blätter in die Feathering-Position
- Pitch wird werksseitig eingestellt (verschiedene Pitch-Ringe verfügbar)

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Max-Prop Easy | 2 | Welle | 12–18 | 1.500–2.500 |
| Max-Prop Classic | 2 | Welle | 12–24 | 1.800–3.200 |
| Max-Prop Easy 3 | 3 | Welle | 14–22 | 2.200–3.500 |
| Max-Prop Classic 3 | 3 | Welle | 14–24 | 2.500–4.000 |
| Max-Prop Easy SD | 2 | Saildrive | 13–19 | 1.700–2.700 |
| Max-Prop Easy 3 SD | 3 | Saildrive | 14–20 | 2.400–3.700 |
| Max-Prop Whisper | 3 | Welle/SD | 14–22 | 2.800–4.500 |

**Modellunterschiede:**
- **Easy**: Vereinfachtes Getriebe, niedrigerer Preis, etwas weniger Pitch-Optionen
- **Classic**: Volles Getriebesystem, maximale Pitch-Verstellung, für anspruchsvolle Eigner
- **Whisper**: Neuestes Modell mit optimiertem Blattprofil für weniger Geräusch und Vibration

**Wartung:**
- Alle 1–2 Jahre: Blätter auf Leichtgängigkeit prüfen
- Alle 3–5 Jahre: Nabe öffnen, Kegelräder inspizieren, fetten
- Empfohlenes Fett: Max-Prop Original Grease (wasserfestes Spezialfett)
- Zinkanode auf der Nabe: jährlich prüfen/ersetzen

**Erfahrungswerte:**
- Wirkungsgrad Vorwärts: 95–100 % eines Festpropellers
- Wirkungsgrad Rückwärts: 90–95 %
- Lebensdauer: 25+ Jahre bei korrekter Wartung
- Häufigstes Problem: Korrosion der Kegelräder nach >10 Jahren ohne Wartung

### 5.3 Variprop (Deutschland)

Variprop ist ein deutscher Hersteller aus Kiel, der hochwertige Feathering-Propeller
für anspruchsvolle Segelyachten produziert.

**Technologie:**
- Blätter drehen sich um ihre eigene Achse (echte Pitch-Verstellung)
- Pitch kann vom Eigner selbst angepasst werden (ohne Tauchen!)
- Markierung auf der Nabe zeigt aktuelle Pitch-Position
- Patentiertes Verriegelungssystem hält Blätter in Position

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Variprop 2B | 2 | Welle | 12–19 | 1.600–2.800 |
| Variprop 3B | 3 | Welle | 14–22 | 2.200–3.800 |
| Variprop 4B | 4 | Welle | 16–24 | 3.000–5.000 |
| Variprop SD | 2/3 | Saildrive | 14–20 | 2.000–3.500 |
| Variprop GP | 3 | Welle | 15–26 | 2.800–4.500 |

**Besonderheiten:**
- „Made in Germany" — Fertigung in Kiel
- Pitch-Verstellung ohne Tauchen (einzigartiges Merkmal)
- 4-Blatt-Option für Motoryachten/Motorsegler
- Guter technischer Support direkt vom Hersteller

**Wartung:**
- Jährlich: Blattbeweglichkeit prüfen
- Alle 2–3 Jahre: Nabe öffnen, Lager prüfen
- Zinkanode: jährlich ersetzen

### 5.4 Autoprop (UK — Bruntons)

Der Autoprop von Bruntons (Colchester, England) ist ein einzigartiges Konzept:
ein selbstanpassender Propeller, dessen Blätter sich automatisch auf den
optimalen Pitch einstellen.

**Technologie:**
- Blätter sind frei drehbar in der Nabe gelagert
- Hydrodynamische Kräfte und Fliehkraft stellen den Pitch automatisch ein
- Bei hoher Last (Anlegen, Gegenwind): Blätter stellen sich steiler → mehr Schub
- Bei geringer Last (Freifahrt): Blätter stellen sich flacher → mehr Geschwindigkeit
- Unter Segeln: Blätter feathern automatisch

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Autoprop H5 | 3 | Welle | 14–24 | 2.200–3.800 |
| Autoprop H6 | 3 | Welle (Schwerlast) | 16–30 | 2.800–5.500 |
| Autoprop H5 SD | 3 | Saildrive | 14–20 | 2.400–3.600 |

**Besonderheiten:**
- Einziger wirklich selbstanpassender Propeller am Markt
- Ideal für wechselnde Betriebsbedingungen (Tidenstrom, Wind, Gewicht)
- Keine Pitch-Einstellung nötig — Propeller passt sich selbst an
- Patentierte Technologie seit >25 Jahren bewährt

**Einschränkungen:**
- Blätter bewegen sich ständig → mechanischer Verschleiß
- Kann bei sehr niedrigen Drehzahlen „flattern"
- Höherer Preis als viele Konkurrenten
- Reparatur nur durch autorisierte Bruntons-Werkstätten

### 5.5 Kiwiprop (Neuseeland)

Kiwiprop ist ein neuseeländischer Hersteller, der einen innovativen
Feathering-Propeller mit einfacher, robuster Mechanik anbietet.

**Technologie:**
- Blätter werden durch Fliehkraft und Wasserdruck positioniert
- Einfaches mechanisches System ohne Zahnräder
- Pitch-Verstellung durch austauschbare Pitch-Scheiben
- Robuste Konstruktion für Langfahrt-Segelyachten

**Produktlinie:**

| Modell | Blätter | Welle/Saildrive | Größe (") | Preis (EUR) |
|--------|:-------:|-----------------|:---------:|:-----------:|
| Kiwiprop Standard | 3 | Welle | 14–20 | 1.800–2.800 |
| Kiwiprop SD | 3 | Saildrive | 14–19 | 2.000–3.000 |
| Kiwiprop DP | 3 | Welle (Dual Pitch) | 15–22 | 2.200–3.200 |

**Besonderheiten:**
- Einfache, wartungsarme Mechanik
- Bewährt bei Langfahrt-Seglern (Südsee, Weltumsegelung)
- Kompetenter Support aus Neuseeland
- Gutes Preis-Leistungs-Verhältnis

### 5.6 Feathering-Propeller — Vergleichsmatrix

| Kriterium | Max-Prop | Variprop | Autoprop | Kiwiprop |
|-----------|:--------:|:--------:|:--------:|:--------:|
| Vorwärts-Wirkungsgrad | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Rückwärts-Leistung | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Feathering-Qualität | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Selbstanpassung | ★★☆☆☆ | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| Zuverlässigkeit | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★★ |
| Wartungsaufwand | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| Preis-Leistung | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| Verfügbarkeit Europa | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Pitch-Verstellbarkeit | ★★★★☆ | ★★★★★ | ★★★★★ (auto) | ★★★☆☆ |

---
---

## 6. Saildrive-Propeller

### 6.1 Spezifische Anforderungen

Saildrive-Propeller unterscheiden sich von Wellenpropellern in mehreren
entscheidenden Punkten:

**Mechanische Unterschiede:**
- Saildrive-Abtrieb hat eine kürzere Welle mit Splines (Keilwellenprofil)
- Die Nabe muss zum jeweiligen Saildrive-System passen (Volvo, Yanmar, ZF)
- Der Abstand Propeller ↔ Saildrive-Gehäuse ist kritisch (Kavitation!)
- Maximaler Durchmesser wird durch Saildrive-Gehäuse und Rumpfform begrenzt

**Saildrive-Systeme und Propellerkompatibilität:**

| Saildrive | Hersteller | Leistung (PS) | Max. Prop-Ø (") | Spline |
|-----------|-----------|:---:|:---:|:---:|
| SD110 | Volvo Penta | 10–30 | 17 | Volvo Spline |
| SD130 | Volvo Penta | 30–55 | 19 | Volvo Spline |
| SD150 | Volvo Penta | 55–110 | 21 | Volvo Spline |
| SD20 | Yanmar | 15–30 | 16 | Yanmar Spline |
| SD50 | Yanmar | 30–75 | 19 | Yanmar Spline |
| SD60 | Yanmar | 45–100 | 21 | Yanmar Spline |
| Sail Drive 80 | ZF Marine | 30–80 | 19 | ZF Spline |
| Sail Drive 150 | ZF Marine | 80–150 | 22 | ZF Spline |

### 6.2 Anodenschutz bei Saildrive

Saildrive-Systeme sind besonders korrosionsgefährdet, da verschiedene Metalle
(Aluminium-Gehäuse, Bronze-Propeller, Edelstahl-Welle) in direktem Kontakt
stehen und im Seewasser einen galvanischen Kreislauf bilden.

**Anodensystem:**
- **Propeller-Anode**: Ring- oder Zinkkegel auf der Propellernabe
- **Saildrive-Anode**: Zinkanode am Saildrive-Gehäuse (oft 2 Stück)
- **Rumpf-Anode**: Separate Zinkanode am Rumpf in der Nähe des Saildrives

**Kritische Regel:** Saildrive-Anoden müssen MINDESTENS jährlich geprüft
und bei >50 % Verbrauch ersetzt werden. Bei Aluminium-Saildrives (Volvo SD110/130)
ist Unterlassung der Anodenwartung die häufigste Ursache für Saildrive-Totalschaden!

**Anoden-Verbrauchsraten (typisch):**

| Gewässertyp | Verbrauchsrate | Prüfintervall |
|------------|:---:|:---:|
| Süßwasser | 5–15 % pro Jahr | Jährlich |
| Brackwasser | 20–40 % pro Jahr | Halbjährlich |
| Seewasser (gemäßigt) | 30–50 % pro Jahr | Halbjährlich |
| Seewasser (tropisch) | 40–70 % pro Jahr | Quartalsweise |
| Marina mit Fehlströmen | 50–100 % pro Jahr | Quartalsweise |

### 6.3 Saildrive-spezifische Propellerprobleme

**Problem 1: Kavitation durch Saildrive-Gehäuse**
Das Saildrive-Gehäuse erzeugt eine Wirbelzone, die den Propeller ungleichmäßig
anströmt. Dies kann zu:
- Erhöhter Kavitation an einzelnen Blättern
- Vibrationen bei bestimmten Drehzahlen
- Vorzeitigem Blattverschleiß

**Lösung:** Propeller mit ausreichendem Abstand zum Gehäuse wählen.
Faustregel: Blattspitze → Gehäuse mindestens 15 % des Durchmessers.

**Problem 2: Elektrolyse durch Landstrom**
Landstromanschluss ohne galvanischen Isolator erzeugt Fehlströme,
die Saildrive und Propeller angreifen.

**Lösung:** Galvanischer Isolator (Galvanic Isolator) am Landstromkabel
installieren. Kosten: 150–400 EUR. Spart potenziell 5.000+ EUR Schaden.

**Problem 3: Propellerpassung**
Verschiedene Saildrive-Systeme haben unterschiedliche Spline-Profile.
Ein falsch passender Propeller kann:
- Spiel auf der Welle entwickeln → Vibrationen
- Die Splines beschädigen
- Im schlimmsten Fall abfallen

**Lösung:** Immer den exakten Spline-Typ des Saildrives prüfen und
Propeller mit korrektem Adapter bestellen.

---
---

## 7. Propeller-Materialien

### 7.1 Übersicht und Vergleich

| Material | Dichte (g/cm³) | Zugfestigkeit (MPa) | Seewasser-Beständigkeit | Preis-Faktor |
|----------|:---:|:---:|:---:|:---:|
| Manganbronze | 8,3 | 350–450 | Mäßig | 1,0× |
| Ni-Al-Bronze | 7,6 | 550–700 | Sehr gut | 1,5–1,8× |
| Edelstahl 316L | 8,0 | 480–620 | Gut (Spaltkorrosion!) | 2,0–2,5× |
| Duplex 2205 | 7,8 | 620–880 | Ausgezeichnet | 2,5–3,5× |
| GFK-Composite | 1,6–1,8 | 200–400 | Ausgezeichnet | 1,5–2,0× |
| CFK-Composite | 1,4–1,6 | 400–700 | Ausgezeichnet | 3,0–5,0× |

### 7.2 Manganbronze — Detail

**Zusammensetzung (EN 1982 / UNS C86500):**
- Kupfer (Cu): 55–60 %
- Zink (Zn): 36–42 %
- Mangan (Mn): 0,5–3,0 %
- Eisen (Fe): 0,5–2,0 %
- Aluminium (Al): 0–1,5 %

**Physikalische Eigenschaften:**
- Dichte: 8,3 g/cm³
- Zugfestigkeit: 350–450 MPa
- Streckgrenze: 180–250 MPa
- Bruchdehnung: 15–25 %
- Härte: 120–170 HB
- E-Modul: 100 GPa

**Korrosionsverhalten in Seewasser:**
Manganbronze ist das preiswerteste Propellermaterial, hat aber einen
entscheidenden Schwachpunkt: **Entzinkung (Dezincification)**.

Bei Entzinkung wird selektiv das Zink aus der Legierung gelöst, was eine
schwammige, kupferfarbene Schicht zurücklässt. Diese Schicht hat nur noch
~20 % der ursprünglichen Festigkeit. Der Propeller kann ohne äußere
Anzeichen von innen her zerstört werden.

**Risikofaktoren für Entzinkung:**
- Warmes Seewasser (>25 °C)
- Stehende oder langsam fließende Gewässer
- Fehlender Anodenschutz
- Fehlströme durch Landstromanschluss
- Benachbarte Edelstahl-Teile ohne galvanische Trennung

**Schutzmaßnahmen:**
1. Zinkanode auf der Propellerwelle (Wellenanode)
2. Galvanischer Isolator bei Landstromanschluss
3. Regelmäßige Inspektion (Klopftest: hohler Klang = Entzinkung)
4. Antifouling-Beschichtung des Propellers

### 7.3 Nickel-Aluminium-Bronze (NAB) — Detail

**Zusammensetzung (EN 1982 CC333G / UNS C95800):**
- Kupfer (Cu): 79–82 %
- Aluminium (Al): 8,5–10,5 %
- Nickel (Ni): 4–5,5 %
- Eisen (Fe): 3–5 %
- Mangan (Mn): 0,5–1,5 %

**Physikalische Eigenschaften:**
- Dichte: 7,6 g/cm³ (leichter als Manganbronze!)
- Zugfestigkeit: 550–700 MPa
- Streckgrenze: 250–350 MPa
- Bruchdehnung: 12–18 %
- Härte: 150–220 HB
- E-Modul: 120 GPa

**Korrosionsverhalten:**
Ni-Al-Bronze bildet eine schützende Oxidschicht (Al₂O₃), die den
Propeller passiviert. Diese Schicht regeneriert sich nach Beschädigung
selbständig. Daher:

- **Keine Entzinkung** (kein Zink in der Legierung)
- **Ausgezeichnete Erosionsbeständigkeit** (hart, zäh)
- **Geringe galvanische Aktivität** (ähnlich wie Edelstahl)
- **Selbstheilende Oberfläche**

**Empfehlung:** Ni-Al-Bronze ist das optimale Material für Marine-Propeller
in Seewasser. Der Mehrpreis gegenüber Manganbronze amortisiert sich
durch die deutlich längere Lebensdauer.

### 7.4 Edelstahl — Detail

#### 7.4.1 AISI 316L

**Zusammensetzung:**
- Eisen (Fe): Basis
- Chrom (Cr): 16–18 %
- Nickel (Ni): 10–14 %
- Molybdän (Mo): 2–3 %
- Kohlenstoff (C): <0,03 % (L = Low Carbon)

**Propeller-Anwendung:**
316L wird für hochbelastete Propeller verwendet, wenn dünne Blattprofile
gewünscht sind (höherer Wirkungsgrad) oder wenn extreme Festigkeit nötig ist.

**Probleme in Seewasser:**
- **Spaltkorrosion**: In Spalten (Nabe, Keilnut) kann 316L anfällig sein
- **Lochfraß (Pitting)**: In warmem, stagniertem Seewasser möglich
- **Galvanische Korrosion**: 316L ist „edler" als Bronze → korrodiert
  weniger, kann aber benachbarte Bronze-Teile angreifen

#### 7.4.2 Duplex 2205

**Zusammensetzung:**
- Eisen (Fe): Basis
- Chrom (Cr): 21–23 %
- Nickel (Ni): 4,5–6,5 %
- Molybdän (Mo): 2,5–3,5 %
- Stickstoff (N): 0,14–0,20 %

**Vorteile gegenüber 316L:**
- Doppelte Streckgrenze (620 vs. 300 MPa)
- Deutlich bessere Beständigkeit gegen Spalt- und Lochfraßkorrosion
- Bessere Erosionsbeständigkeit
- PREN (Pitting Resistance Equivalent Number) >35 (316L: ~25)

**Empfehlung:** Duplex 2205 ist das beste Edelstahl-Material für
Marine-Propeller, aber auch das teuerste.

### 7.5 Composite-Materialien — Detail

#### 7.5.1 GFK-Propeller (Glasfaser)

**Aufbau:**
- Blätter: E-Glas oder S-Glas in Epoxid- oder Vinylester-Matrix
- Nabe: Ni-Al-Bronze oder Edelstahl (Composite-Nabe nicht ausreichend fest)
- Blatt-Naben-Verbindung: Eingegossene Metallhülsen oder Bolzenverbindung

**Vorteile:**
- Gewichtsersparnis: 50–60 % gegenüber Bronze
- Keine galvanische Korrosion der Blätter
- Dämpfungswirkung: Absorbs Vibrationen und Stöße
- Bei Grundberührung: Blatt bricht → Welle und Getriebe geschützt

**Nachteile:**
- Geringere Erosionsbeständigkeit (Sandkörner, Sediment)
- Nicht reparierbar bei Bruch (Blatt muss ersetzt werden)
- Geringere Steifigkeit → Blattverformung unter Last
- Bewuchsneigung höher als bei glattem Metall

#### 7.5.2 CFK-Propeller (Kohlefaser)

**Aufbau:**
- Blätter: Hochmodul-Carbonfaser in Epoxid-Matrix
- Nabe: Edelstahl oder Titan
- Fertigung: Autoclave-Verfahren oder Prepreg

**Vorteile gegenüber GFK:**
- Höhere Steifigkeit (weniger Blattverformung)
- Noch leichter (70 % Gewichtsersparnis gegenüber Bronze)
- Bessere Ermüdungsfestigkeit

**Nachteile:**
- Sehr hoher Preis (3–5× Bronze)
- Empfindlich gegen Stoßbelastung (Delamination)
- Nur für spezielle Anwendungen (Regatta, E-Antrieb)

### 7.6 Materialauswahl nach Anwendung

| Anwendung | Empfohlenes Material | Begründung |
|----------|---------------------|-----------|
| Segelyacht 8–12 m (Budget) | Manganbronze | Preis, ausreichend bei Anodenschutz |
| Segelyacht 12–18 m | Ni-Al-Bronze | Beste Korrosionsbeständigkeit, Langlebigkeit |
| Segelyacht >18 m | Ni-Al-Bronze oder Duplex | Premium-Qualität, Langlebigkeit |
| Motoryacht <15 m | Manganbronze oder Ni-Al-Bronze | Je nach Budget und Revier |
| Motoryacht >15 m | Ni-Al-Bronze | Standard für hochwertige Motoryachten |
| Hochleistungs-Segler | Duplex 2205 oder CFK | Dünne Profile, hohe Festigkeit |
| E-Antrieb | GFK oder CFK Composite | Leicht, keine Korrosion, vibrationsdämpfend |
| Langfahrt-Yacht | Ni-Al-Bronze | Selbstheilend, robust, weltweit reparierbar |
| Regatta | CFK oder Duplex 2205 | Leicht, dünn, hocheffizient |

---
---

## 8. Dimensionierung und Auslegung

### 8.1 Grundlagen der Propellerdimensionierung

Die korrekte Propellerdimensionierung ist der Schlüssel zu einem effizienten
Antriebssystem. Ein falsch dimensionierter Propeller kann:

- Den Motor überlasten (overpropping) → Kurbelwellenlager-Schaden
- Den Motor unterladen (underpropping) → Überdrehzahl, Ventiltrieb-Verschleiß
- Die Höchstgeschwindigkeit um 15–25 % reduzieren
- Den Kraftstoffverbrauch um 20–40 % erhöhen
- Kavitationsschäden verursachen

**Die drei Kernfragen der Dimensionierung:**
1. **Welcher Durchmesser?** → Maximal groß, begrenzt durch Einbauraum
2. **Welche Steigung (Pitch)?** → So, dass der Motor seine Nenndrehzahl
   bei Volllast erreicht
3. **Wie viele Blätter?** → Abhängig von Bootstyp und Einsatz

### 8.2 Engine-Power-Matching

Der Propeller muss so dimensioniert werden, dass der Motor bei Volllast
seine Nenndrehzahl (WOT RPM = Wide Open Throttle RPM) erreichen kann.

**Warum ist das wichtig?**
- Zu viel Pitch/Durchmesser: Motor kann Nenndrehzahl nicht erreichen
  → dauerhafte Überlastung → erhöhter Verschleiß → Motorschaden
- Zu wenig Pitch/Durchmesser: Motor überdreht die Nenndrehzahl
  → erhöhter Verschleiß → Motorschaden
- Optimaler Punkt: Motor erreicht Nenndrehzahl ±3 %

**Faustregel Leistungs-Zuordnung:**

```
Propellerleistung [kW] = Motorleistung × Getriebewirkungsgrad × Wellenleitung-Wirkungsgrad

Typisch:
  Getriebewirkungsgrad: 0,93–0,97 (mechanisch), 0,85–0,93 (Saildrive)
  Wellenleitungswirkungsgrad: 0,95–0,98 (kurze Welle), 0,90–0,95 (lange Welle)

Beispiel: 55 PS Motor, Saildrive
  Propellerleistung = 55 × 0,90 × 1,0 = 49,5 PS am Propeller
```

### 8.3 Bp-δ Diagramm (Leistungskoeffizient-Methode)

Das Bp-δ-Diagramm ist die klassische Methode zur Propellerdimensionierung,
basierend auf der Wageningen B-Serie.

**Definition der Variablen:**

```
Bp = (N × √P_D) / V_a^2.5

δ = (N × D) / V_a

wobei:
  N = Drehzahl [U/min]
  P_D = Wellenleistung (Delivered Power) [PS]
  V_a = Anströmgeschwindigkeit am Propeller [kn]
  D = Propellerdurchmesser [ft]
```

**Vorgehensweise:**
1. Berechne V_a aus der Designgeschwindigkeit und dem Nachstromfaktor (wake fraction)
2. Berechne Bp aus N, P_D und V_a
3. Gehe mit Bp in das Bp-δ-Diagramm (für gewählte Blattanzahl und BAR)
4. Lese δ und η_o (Open-Water-Wirkungsgrad) ab
5. Berechne D aus δ
6. Prüfe, ob D in den Einbauraum passt
7. Wenn nicht: begrenze D und wiederhole mit höherem Bp (höhere Drehzahl)

**Vereinfachte Formel für Segelyachten:**

```
D (Zoll) ≈ K × ⁴√(SHP / RPM²)

K-Werte:
  2-Blatt: K ≈ 290–310
  3-Blatt: K ≈ 270–290
  4-Blatt: K ≈ 250–270
```

**Vereinfachte Formel für Motoryachten (Verdränger):**

```
D (Zoll) ≈ 15,5 × ⁴√(SHP / RPM²) × Korrekturfaktor

Korrekturfaktoren:
  Einwellendampfer: 1,00
  Doppelwellen: 0,95
  Halbgleiter: 0,90
  Gleiter: 0,85
```

### 8.4 Slip Calculation — Praxisanleitung

Die Slip-Berechnung ist die einfachste Methode, um zu prüfen, ob ein
Propeller korrekt dimensioniert ist.

**Schritt 1: Daten sammeln**
```
Pitch (P): vom Propeller ablesen oder Datenblatt [Zoll]
RPM (n): Motordrehzahl bei Volllast [U/min]
Untersetzung (i): Getriebe-Untersetzungsverhältnis
Geschwindigkeit (V_s): GPS-Geschwindigkeit über Grund [kn]
```

**Schritt 2: Propellerdrehzahl berechnen**
```
Propeller-RPM = Motor-RPM / Untersetzung
```

**Schritt 3: Theoretische Geschwindigkeit berechnen**
```
V_theo [kn] = (Propeller-RPM × Pitch [Zoll] × 60) / (12 × 6.076)

vereinfacht:
V_theo [kn] = (Propeller-RPM × Pitch [Zoll]) / 1.215,2
```

**Schritt 4: Slip berechnen**
```
Slip (%) = (V_theo − V_s) / V_theo × 100
```

**Beispiel:**
```
Motor: Yanmar 4JH57, 57 PS, 3.400 U/min max
Getriebe: Saildrive SD50, i = 2,64
Propeller: 3-Blatt, 16" × 11" (Durchmesser × Pitch)
GPS-Geschwindigkeit bei Vollgas: 7,2 kn

Propeller-RPM = 3.400 / 2,64 = 1.288 U/min
V_theo = (1.288 × 11) / 1.215,2 = 11,66 kn
Slip = (11,66 − 7,2) / 11,66 × 100 = 38,3 %

→ 38 % Slip bei einer Segelyacht (10t, 13m) ist normal.
```

### 8.5 Pitch-Optimierung

Wenn der Motor seine Nenndrehzahl nicht erreicht oder überdreht,
muss der Pitch angepasst werden:

**Motor erreicht Nenndrehzahl nicht (overpropped):**
- Symptom: Motor erreicht max. 85–95 % der Nenndrehzahl
- Ursache: Pitch zu hoch oder Durchmesser zu groß
- Lösung: Pitch um 1–2 Zoll reduzieren
- Alternativ: Blätter kürzen (Durchmesser reduzieren) — nur durch Fachmann!

**Motor überdreht (underpropped):**
- Symptom: Motor erreicht >103 % der Nenndrehzahl
- Ursache: Pitch zu niedrig oder Durchmesser zu klein
- Lösung: Pitch um 1–2 Zoll erhöhen
- Alternativ: Propeller mit größerem Durchmesser wählen

**Pitch-Änderung Faustregel:**
```
+1" Pitch ≈ −150 bis −200 U/min (bei 14–18" Propeller)
−1" Pitch ≈ +150 bis +200 U/min

Bei kleinen Propellern (10–13"): Änderung stärker
Bei großen Propellern (20–28"): Änderung geringer
```

### 8.6 Dimensionierungsbeispiele

#### Beispiel 1: Segelyacht Bavaria 38 Cruiser

**Daten:**
- LOA: 11,7 m, Verdrängung: 8.200 kg
- Motor: Volvo D2-40, 40 PS, 3.600 U/min
- Saildrive: SD130, Untersetzung 2,15:1
- Rumpfgeschwindigkeit: V_hull = 1,34 × √LWL = 1,34 × √10,0 = 4,24 kn × 1,5 = 6,4 kn
- Ziel-Motorgeschwindigkeit: 6,5–7,0 kn

**Berechnung:**
```
Propeller-RPM = 3.600 / 2,15 = 1.674
Verfügbare Leistung am Propeller = 40 × 0,90 = 36 PS
Empfohlener Durchmesser (3-Blatt): ≈ 16"
Empfohlener Pitch: ≈ 10–11"
```

**Ergebnis:** Flexofold 3-Blatt, 16" × 11" oder Max-Prop 3-Blatt 16"
mit mittlerem Pitch-Ring.

#### Beispiel 2: Motoryacht Linssen Grand Sturdy 40.0

**Daten:**
- LOA: 12,85 m, Verdrängung: 13.500 kg (Vollbeladung)
- Motor: Volvo D3-110, 110 PS, 3.200 U/min
- Getriebe: MS25S, Untersetzung 2,63:1
- Wellenantrieb, S-Antrieb
- Ziel-Motorgeschwindigkeit: 9,0 kn

**Berechnung:**
```
Propeller-RPM = 3.200 / 2,63 = 1.217
Verfügbare Leistung = 110 × 0,95 × 0,96 = 100 PS
Empfohlener Durchmesser (3-Blatt): ≈ 20"
Empfohlener Pitch: ≈ 14–15"
```

**Ergebnis:** Michigan Wheel Match 3-Blatt, 20" × 14" in Ni-Al-Bronze.

#### Beispiel 3: Segelyacht Hallberg-Rassy 48

**Daten:**
- LOA: 14,98 m, Verdrängung: 17.500 kg
- Motor: Volvo D3-150, 150 PS, 3.000 U/min
- Saildrive: SD150, Untersetzung 2,27:1
- Ziel-Motorgeschwindigkeit: 8,5 kn

**Berechnung:**
```
Propeller-RPM = 3.000 / 2,27 = 1.321
Verfügbare Leistung = 150 × 0,90 = 135 PS
Empfohlener Durchmesser (3-Blatt): ≈ 20"
Empfohlener Pitch: ≈ 14"
```

**Ergebnis:** Max-Prop Whisper 3-Blatt 20" oder Variprop 3B 20".

### 8.7 Untersetzungsverhältnis und Propellerdrehzahl

Das Getriebe-Untersetzungsverhältnis verbindet Motordrehzahl und
Propellerdrehzahl. Die optimale Propellerdrehzahl hängt vom Bootstyp ab:

**Optimale Propellerdrehzahl nach Bootstyp:**

| Bootstyp | Optimale Prop-RPM | Untersetzung bei 3.000 Motor-RPM |
|----------|:---:|:---:|
| Schwerer Verdränger | 400–700 | 4:1 bis 7:1 |
| Leichter Verdränger | 700–1.000 | 3:1 bis 4:1 |
| Segelyacht | 1.000–1.500 | 2:1 bis 3:1 |
| Halbgleiter | 1.200–1.800 | 1,5:1 bis 2,5:1 |
| Gleiter | 1.500–3.000 | 1:1 bis 2:1 |

**Faustregel:** Niedrigere Propellerdrehzahl + größerer Propeller =
höherer Wirkungsgrad. Begrenzt durch Einbauraum und Kavitation.

---
---

## 9. Kavitation

### 9.1 Was ist Kavitation?

Kavitation ist die Bildung und der Zusammenfall von Dampfblasen in einer
Flüssigkeit aufgrund lokaler Druckabsenkung unter den Dampfdruck.

**Physik:**
Bei ausreichend hoher Strömungsgeschwindigkeit auf der Saugseite
(Vorderseite) des Propellerblatts sinkt der lokale Druck unter den
Dampfdruck des Wassers (~2,3 kPa bei 20 °C). Es bilden sich Dampfblasen.
Wenn diese Blasen in Zonen höheren Drucks gelangen, kollabieren sie
schlagartig — der sogenannte **Kavitationsschlag** (Implosion).

**Kavitationsschlag:**
- Lokaler Druck beim Kollaps: bis zu 1.500 MPa (!)
- Temperatur im Blasenzentrum: bis zu 5.000 °C
- Dauer: Mikrosekunden
- Wiederholungsrate: Tausende pro Sekunde an einer Stelle

Diese enormen Kräfte erodieren das Blattmaterial und können einen
Propeller innerhalb weniger Stunden schwer beschädigen.

### 9.2 Kavitationstypen

#### 9.2.1 Blattkavitation (Sheet Cavitation)

Die häufigste Form. Bildet sich als zusammenhängendes Dampffeld
auf der Saugseite des Blatts, beginnend an der Vorderkante.

**Ursachen:**
- Zu hohe Blattbelastung (zu wenig Blattfläche für die Leistung)
- Zu hohe Anstellwinkel (falscher Pitch bei der Geschwindigkeit)
- Scharfe Vorderkante (nach Reparatur oder Beschädigung)

#### 9.2.2 Spitzenkavitation (Tip Vortex Cavitation)

Kavitationsfäden, die von den Blattspitzen ausgehen und spiralförmig
hinter dem Propeller verlaufen.

**Ursachen:**
- Hohe Druckdifferenz zwischen Saug- und Druckseite an der Blattspitze
- Zu kleiner Propeller für die Leistung
- Zu geringer Tipabstand zum Rumpf

#### 9.2.3 Blasenkavitation (Bubble Cavitation)

Einzelne Dampfblasen, die an Oberflächenrauhigkeiten oder
Korrosionsstellen entstehen.

**Ursachen:**
- Raue Oberfläche (Bewuchs, Korrosion, schlechte Reparatur)
- Lokale Druckspitzen durch Geometriefehler
- Verschmutzung der Vorderkante

#### 9.2.4 Wurzelkavitation (Hub Vortex Cavitation)

Kavitation an der Blattwurzel, wo das Blatt in die Nabe übergeht.

**Ursachen:**
- Ungünstiger Übergangsradius Blatt → Nabe
- Zu enge Blattstellungen (hohes BAR)
- Strömungsablösung an der Nabenwölbung

### 9.3 Kavitationserkennung

**Akustische Erkennung:**
- Leichte Kavitation: Leises Zischen oder „Sprudeln"
- Mittlere Kavitation: Deutliches Knistern, „Kies in der Trommel"
- Starke Kavitation: Lautes Hämmern, Vibrationen spürbar
- Intervall-Kavitation: Rhythmisches Klopfen (1× pro Blattumlauf =
  hinterer Stevenbereich stört die Strömung)

**Visuelle Erkennung (Pipeline B — AYDI):**
- Weißes, schäumendes Wasser hinter dem Propeller bei niedrigen Drehzahlen
  → Kavitation (normalerweise sieht man erst bei höheren Drehzahlen Blasen)
- Propellerblätter mit mattem, rauem Bereich (Erosion)
- Kleine Krater und Löcher an der Saugseite (nach Trockenstellen)
- „Spongy" Oberfläche bei starker Erosion

**Instrumentelle Erkennung:**
- Vibrationssensor an der Welle oder am Stevenrohr
- Hydrophone (Unterwassermikrofon)
- Bei modernen Motoren: Drehzahlschwankungen unter Last

### 9.4 Kavitationsvermeidung

**Design-Maßnahmen:**
1. **Ausreichende Blattfläche (BAR)**: Keller-Kriterium verwenden
2. **Optimales Blattprofil**: Abgerundete Vorderkante, NACA-Profil
3. **Moderate Blattbelastung**: Nicht zu wenige Blätter für die Leistung
4. **Genügend Abstand zum Rumpf**: ≥15 % des Durchmessers
5. **Skew**: Reduziert periodische Kavitation in der Nachlaufzone
6. **Cup**: Verzögert Kavitationsbeginn an der Hinterkante

**Betriebsmaßnahmen:**
1. **Propeller sauber halten**: Bewuchs erhöht Kavitationsneigung drastisch
2. **Nicht dauerhaft Vollgas fahren**: 80–85 % Leistung = deutlich weniger Kavitation
3. **Langsam beschleunigen**: Schnelles Gasgeben erzeugt kurzzeitige Kavitation
4. **Trim optimieren**: Korrekter Trimm verbessert die Anströmung

**Keller-Kriterium (vereinfacht):**
```
BAR_min = (1,3 + 0,3 × Z) × T / ((p_0 − p_v) × D²)

wobei:
  Z = Anzahl Blätter
  T = Schub [N]
  p_0 = Umgebungsdruck am Propeller [Pa]
  p_v = Dampfdruck des Wassers [Pa]
  D = Durchmesser [m]
```

Wenn BAR < BAR_min → Kavitationsgefahr!

---
---

## 10. Propeller-Balance und Vibration

### 10.1 Statische Balance

Ein statisch ungewuchteter Propeller hat eine ungleichmäßige Massenverteilung.
Das schwerere Blatt erzeugt bei Drehung eine Zentrifugalkraft, die
den gesamten Antriebsstrang in Vibration versetzt.

**Prüfmethode (Bordmittel):**
1. Propeller horizontal auf einen runden Stab (Besenstiel) legen
2. Blatt markieren, das nach unten dreht
3. Wiederholen — immer dasselbe Blatt → Unwucht vorhanden
4. Material am schweren Blatt entfernen oder am leichten Blatt hinzufügen

**Toleranzen:**
- ISO 484 Klasse S: ≤0,5 g × cm pro kg Propellergewicht (Präzision)
- ISO 484 Klasse I: ≤1,0 g × cm pro kg (Standard)
- ISO 484 Klasse II: ≤2,0 g × cm pro kg (Wirtschaftlich)
- ISO 484 Klasse III: ≤4,0 g × cm pro kg (Grob)

### 10.2 Dynamische Balance

Dynamische Unwucht tritt auf, wenn die Massenverteilung zwar statisch
ausgeglichen ist, aber die Schwerpunkte der einzelnen Blätter nicht in
einer Ebene liegen. Dynamische Unwucht erzeugt ein Kippmoment.

**Erkennung:**
- Vibrationen, die mit der Drehzahl zunehmen (proportional zu RPM²)
- Vibrationen auch bei niedrigen Drehzahlen spürbar
- Frequenz der Vibration = Propeller-RPM / 60

**Prüfmethode:**
Dynamische Balance kann nur auf einer Auswuchtmaschine geprüft werden.
Kosten: 80–200 EUR bei einer Propellerwerkstatt.

### 10.3 Pitch-Balance

Pitch-Balance bedeutet, dass alle Blätter exakt den gleichen Pitch haben.
Unterschiedliche Pitch-Werte erzeugen unterschiedliche Schubkräfte pro Blatt
→ Vibration und reduzierter Wirkungsgrad.

**Ursachen für Pitch-Unbalance:**
- Herstellungstoleranz (bei Guss-Propellern: ±0,5–1°)
- Verbogenes Blatt (Grundberührung)
- Ungleichmäßige Erosion oder Reparatur

**Prüfmethode:**
- Pitch-Block und Messvorrichtung (Fachbetrieb)
- Kosten: 50–150 EUR für Pitch-Messung und -Korrektur

**Toleranzen:**
- Maximum ±1 % Pitch-Abweichung zwischen Blättern
- Bei 12" Pitch: max ±0,12" = ±3 mm Abweichung

### 10.4 Vibrationsursachen am Propeller

| Nr. | Ursache | Frequenz | Schwere |
|:---:|---------|---------|:---:|
| 1 | Statische Unwucht | 1× Prop-RPM | Mittel |
| 2 | Dynamische Unwucht | 1× Prop-RPM | Mittel |
| 3 | Pitch-Unbalance | 1× Prop-RPM | Gering–Mittel |
| 4 | Verbogenes Blatt | 1× Prop-RPM | Hoch |
| 5 | Fehlendes Blatt | 1× Prop-RPM | Kritisch |
| 6 | Kavitation (periodisch) | Z × Prop-RPM | Mittel–Hoch |
| 7 | Welle verbogen | 1× Prop-RPM | Hoch |
| 8 | Fehlausrichtung Motor/Welle | 1× und 2× Prop-RPM | Hoch |
| 9 | Propeller locker auf Welle | Variabel (Klappern) | Kritisch |
| 10 | Ruderturbulenz | Unregelmäßig | Gering |

### 10.5 Vibrations-Diagnose Praxis

**Schritt 1: Vibrationscharakter bestimmen**
- Konstant: Unwucht, Verformung, Fehlausrichtung
- Drehzahlabhängig: Stärker = Unwucht (∝ RPM²)
- Belastungsabhängig: Stärker unter Last = Kavitation, Blattbeschädigung
- Intermittierend: Lose Teile, Bewuchs

**Schritt 2: Frequenzanalyse**
- 1× Prop-RPM: Propellerproblem (Unwucht, Verformung)
- 1× Motor-RPM: Motorproblem (Zündung, Lager)
- Z × Prop-RPM: Kavitation oder Nachlaufstörung (Z = Blattanzahl)

**Schritt 3: Visuelle Inspektion**
- Propeller tauchen und inspizieren (Taucher oder Bootshebeanlage)
- Blätter auf Verformung, Erosion, Bewuchs prüfen
- Wellendurchführung auf Leckage prüfen
- Motorlager prüfen (Gummi-Verformung?)

---
---

## 11. Propeller-Schutz und Antifouling

### 11.1 Anodenschutz (Kathodischer Schutz)

Der Propeller ist eines der am stärksten korrosionsgefährdeten Bauteile
am Boot, da er ständig in Seewasser getaucht ist und aus einem anderen
Metall besteht als Welle, Stevenrohr und Rumpfbeschläge.

**Galvanische Spannungsreihe (marine, vereinfacht):**

| Material | Potential (V vs. Ag/AgCl) |
|----------|:---:|
| Zink | −1,05 |
| Aluminium (Marine) | −0,87 |
| Stahl (unlegiert) | −0,60 bis −0,71 |
| Manganbronze | −0,30 bis −0,37 |
| Ni-Al-Bronze | −0,26 bis −0,32 |
| Edelstahl 316L (passiv) | −0,05 bis −0,10 |
| Titan | +0,06 |
| Graphit/CFK | +0,20 bis +0,30 |

**Anodenmaterial-Auswahl:**

| Gewässertyp | Anodenmaterial |
|------------|:---:|
| Seewasser | Zink |
| Brackwasser | Zink oder Aluminium |
| Süßwasser | Magnesium |

**Anodentypen für Propeller:**

| Typ | Position | Funktion |
|-----|---------|---------|
| Wellenanode (Shaft Anode) | Auf der Propellerwelle | Schützt Welle + Propeller |
| Propeller-Zinkkegel | Auf der Propellernabe (hinter) | Schützt Propeller direkt |
| Rumpfanode | Am Rumpf nahe Propeller | Allgemeiner Schutz |
| Saildrive-Anode | Am Saildrive-Gehäuse | Schützt Saildrive + Propeller |

**Dimensionierung:**
- Faustregel: 1 kg Zink pro 50 m² benetzter Oberfläche pro Jahr (Seewasser)
- Für einen typischen Segelyacht-Propeller (16"): 0,5–1,0 kg Zink p.a.
- Anode muss metallischen Kontakt zum geschützten Teil haben!

### 11.2 Propeller-Antifouling

Bewuchs auf dem Propeller reduziert den Wirkungsgrad drastisch:

**Wirkungsgradeinbußen durch Bewuchs:**

| Bewuchsgrad | Beschreibung | Wirkungsgradeinbuße |
|------------|-------------|:---:|
| Stufe 0 | Sauber, glatt | 0 % |
| Stufe 1 | Leichter Schleimfilm | 2–5 % |
| Stufe 2 | Algenfilm, kleine Muscheln | 5–15 % |
| Stufe 3 | Dichter Bewuchs, Seepocken | 15–30 % |
| Stufe 4 | Starker Bewuchs, Muschelbänke | 30–50 % |

**Antifouling-Produkte für Propeller:**

| Produkt | Hersteller | Typ | Haltbarkeit | Preis (EUR) |
|---------|-----------|-----|:-----------:|:-----------:|
| Prop-Gold | International | Spezialbeschichtung | 12–18 Monate | 35–55 (Kit) |
| Trilux 33 | International | Propeller-Antifouling | 6–12 Monate | 25–40 (0,375 l) |
| Prop-O-Drev | Hempel | Primer + Antifouling | 12 Monate | 40–65 (Kit) |
| Velox Plus | Marlin | Antifouling | 12 Monate | 30–50 |
| Mille Xtra | Hempel | Universal (auch Propeller) | 6–12 Monate | 20–35 (0,375 l) |
| PropSpeed | PropSpeed (NZ) | Foul-Release Beschichtung | 18–24 Monate | 180–350 (Kit) |

**Anwendungsregeln:**
1. Propeller IMMER zuerst mit Primer behandeln (spezifisch für das Metall!)
2. Normales Rumpf-Antifouling NICHT auf den Propeller auftragen (andere Chemie!)
3. Propeller-Antifouling enthält i.d.R. kein Kupfer (Kupfer greift Bronze an)
4. Zink-basierte oder PTFE-basierte Antifoulings sind für Propeller geeignet
5. Foul-Release-Beschichtungen (PropSpeed) funktionieren am besten bei Booten,
   die regelmäßig bewegt werden

**PropSpeed — Foul-Release-System:**

PropSpeed (Neuseeland) ist der Marktführer bei Foul-Release-Beschichtungen
für Propeller und Unterwasserbauteile.

- **Funktionsprinzip**: Silikonbasierte, ultraglatte Beschichtung. Bewuchs
  kann sich nicht festsetzen und wird bei Fahrt abgespült.
- **Anwendung**: 1× Etching Primer + 2× Clear Coat → 3-Schicht-System
- **Haltbarkeit**: 18–24 Monate (herstellergarantiert)
- **Preis**: 180–350 EUR (für 1 Propeller + Saildrive/Stevenrohr)
- **Vorteil**: Kein Biozid, umweltfreundlich, wirkt auf allen Metallen
- **Nachteil**: Hoher Preis, empfindlich gegen mechanische Beschädigung

### 11.3 Linenschneider (Rope Cutter)

Linenschneider schützen den Propeller vor Beschädigung durch Leinen,
Netze und Treibgut, die sich um Welle und Propeller wickeln können.

**Funktionsprinzip:**
Ein rotierendes Messer (auf der Welle) und ein feststehendes Gegenmesser
(am Stevenrohr oder P-Bracket) schneiden Leinen und Netzreste, bevor
sie sich um die Welle wickeln können.

**Produkte:**

| Hersteller | Modell | Wellengrößen | Preis (EUR) |
|------------|--------|:---:|:-----------:|
| Spurs (UK) | Spurs Line Cutter | 25–60 mm | 350–650 |
| ShaftCutter (NL) | ShaftCutter | 25–50 mm | 280–550 |
| Stripper (AU) | Prop Protector | 25–50 mm | 300–600 |
| Volvo Penta | Rope Cutter Kit | SD-spezifisch | 250–400 |

**Installation:**
- Rotierendes Element fest auf der Welle montiert
- Feststehendes Element am Stevenrohr oder P-Bracket
- Spalt zwischen rotierend/feststehend: 0,5–1 mm
- Regelmäßig auf Verschleiß prüfen (Schneidkanten)

### 11.4 Propeller-Abdeckungen (Prop Sock / Prop Cover)

Für Langzeitliegeplätze oder Winterlager ist eine Propellerabdeckung
eine einfache und effektive Schutzmaßnahme.

**Typen:**
- **Prop Sock**: Neopren-Überzug, der über den Propeller gezogen wird.
  Schützt vor Bewuchs im Hafenbecken. Preis: 40–80 EUR
- **Prop Bag**: Wasserdichter Beutel mit Desinfektionslösung.
  Tötet Bewuchs ab und verhindert Neuansiedlung. Preis: 60–120 EUR

---
---

## 12. Hersteller und Marktübersicht

### 12.1 Flexofold (Dänemark)

**Unternehmensprofil:**
- Gründung: 2005
- Sitz: Søborg, Dänemark
- Spezialisierung: Zahnrad-Faltpropeller
- Marktanteil (geschätzt): 25–30 % (Faltpropeller-Segment)
- Website: flexofold.com

**Stärken:**
- Marktführer bei Faltpropellern mit 100 % Rückwärtsleistung
- Breites Größensortiment (13"–24")
- Composite-Optionen verfügbar
- Guter weltweiter Vertrieb

**Schwächen:**
- Keine Feathering-Option
- Zahnrad-Mechanismus erfordert regelmäßiges Fetten
- Premium-Preis

**Preisübersicht (EUR, 2025/26):**
- 2-Blatt Welle: 980–2.200
- 3-Blatt Welle: 1.350–2.800
- 2-Blatt Saildrive: 1.050–2.350
- 3-Blatt Saildrive: 1.450–2.950
- Composite-Varianten: +200–500 EUR
- Ersatzblätter: 180–350 EUR pro Blatt

### 12.2 Gori (Dänemark)

**Unternehmensprofil:**
- Gründung: 1965
- Sitz: Fredericia, Dänemark
- Spezialisierung: Faltpropeller mit 2-Gang-Mechanismus
- Marktanteil (geschätzt): 15–20 % (Faltpropeller-Segment)
- Website: gfrpropeller.dk

**Stärken:**
- Einzigartiger 2-Gang-Mechanismus
- Über 50 Jahre Erfahrung
- Hohe Fertigungsqualität (dänische Produktion)
- Gutes Rückwärtsverhalten

**Schwächen:**
- Komplexerer Mechanismus als Flexofold
- Begrenztere Größenauswahl
- 2-Gang-Umschaltung nicht immer zuverlässig

**Preisübersicht (EUR, 2025/26):**
- 2-Blatt Welle: 850–1.600
- 3-Blatt Welle: 1.200–2.400
- 2-Blatt Saildrive: 950–1.750
- 3-Blatt Saildrive: 1.350–2.600
- Ersatzblätter: 150–300 EUR pro Blatt
- Wartungskit (Fett, O-Ringe): 40–60 EUR

### 12.3 Max-Prop (Italien)

**Unternehmensprofil:**
- Gründung: 1974
- Sitz: Mailand, Italien
- Spezialisierung: Feathering-Propeller (Kegelrad-System)
- Marktanteil (geschätzt): 30–35 % (Feathering-Segment)
- Website: max-prop.com

**Stärken:**
- Über 50 Jahre Marktpräsenz — der „Klassiker"
- Hervorragender Vorwärts- UND Rückwärtswirkungsgrad
- Bewährtes Kegelrad-System
- Breites Größensortiment
- Neues Modell „Whisper" für reduzierte Geräusche

**Schwächen:**
- Hoher Preis
- Kegelräder können bei Wartungsmangel korrodieren
- Pitch-Verstellung erfordert Tauchen (außer bei Easy-Modell mit Pitch-Ring)

**Preisübersicht (EUR, 2025/26):**
- Easy 2-Blatt: 1.500–2.500
- Classic 2-Blatt: 1.800–3.200
- Easy 3-Blatt: 2.200–3.500
- Classic 3-Blatt: 2.500–4.000
- Whisper 3-Blatt: 2.800–4.500
- Saildrive-Varianten: +200–400 EUR
- Pitch-Ring: 80–150 EUR
- Wartungskit: 60–90 EUR

### 12.4 Variprop (Deutschland)

**Unternehmensprofil:**
- Gründung: 1998
- Sitz: Kiel, Deutschland
- Spezialisierung: Feathering-Propeller mit externer Pitch-Verstellung
- Marktanteil (geschätzt): 10–15 % (Feathering-Segment, Nordeuropa)
- Website: variprop.de

**Stärken:**
- „Made in Germany" — Kieler Fertigung
- Pitch-Verstellung OHNE Tauchen (einzigartig!)
- 4-Blatt-Option für Motorsegler
- Direkter Herstellerkontakt und Support

**Schwächen:**
- Kleinerer Betrieb → begrenzte weltweite Verfügbarkeit
- Höherer Preis als Max-Prop (bei vergleichbarer Leistung)
- Weniger Langzeiterfahrung als Max-Prop

**Preisübersicht (EUR, 2025/26):**
- 2-Blatt: 1.600–2.800
- 3-Blatt: 2.200–3.800
- 4-Blatt: 3.000–5.000
- Saildrive-Varianten: 2.000–3.500
- GP-Modell: 2.800–4.500
- Ersatzblätter: 250–450 EUR pro Blatt

### 12.5 Bruntons Autoprop (UK)

**Unternehmensprofil:**
- Gründung: 1906 (Bruntons Propellers)
- Sitz: Colchester, England
- Spezialisierung: Selbstanpassende Propeller (Autoprop)
- Marktanteil (geschätzt): 8–12 % (Feathering-Segment)
- Website: bruntons-propellers.com

**Stärken:**
- Einziger wirklich selbstanpassender Propeller
- Ideal für wechselnde Bedingungen (Langfahrt, Gezeiten)
- Über 100 Jahre Propellererfahrung
- Guter technischer Support

**Schwächen:**
- Höherer mechanischer Verschleiß (Blätter bewegen sich ständig)
- Kann bei niedrigen Drehzahlen flattern
- Reparatur nur durch autorisierte Werkstätten
- Höherer Preis

**Preisübersicht (EUR, 2025/26):**
- H5 (Standard): 2.200–3.800
- H6 (Schwerlast): 2.800–5.500
- H5 Saildrive: 2.400–3.600
- Ersatzblätter: 350–600 EUR pro Blatt
- Wartungskit: 80–120 EUR

### 12.6 Volvo Penta (Schweden)

**Propeller-Angebot:**
Volvo Penta bietet als OEM-Zulieferer Propeller für ihre eigenen
Saildrive- und Sterndrive-Systeme an.

**Produktbereiche:**
- Faltpropeller für Saildrives (SD110, SD130, SD150)
- Festpropeller für Saildrives
- Duo-Prop (gegenläufige Doppelpropeller) für Sterndrive
- IPS-Propeller für IPS-Antriebe

**Preisübersicht (EUR, 2025/26):**
- 2-Blatt Folding SD: 850–1.400
- 3-Blatt Folding SD: 1.200–1.900
- 3-Blatt Fest SD: 350–800
- Duo-Prop Set (Sterndrive): 1.200–2.800
- IPS-Propeller Set: 2.500–5.500

### 12.7 Michigan Wheel (USA)

**Unternehmensprofil:**
- Gründung: 1903
- Sitz: Grand Rapids, Michigan, USA
- Spezialisierung: Festpropeller für alle Anwendungen
- Marktanteil (geschätzt): 20–25 % (Festpropeller-Segment, Nordamerika)
- Website: miwheel.com

**Stärken:**
- Über 120 Jahre Propellerproduktion
- Breitestes Sortiment an Festpropellern
- Gutes Preis-Leistungs-Verhältnis
- Eigene Gießerei und Qualitätskontrolle

**Schwächen:**
- Primär auf Nordamerika fokussiert
- Keine Falt-/Feathering-Propeller im Sortiment
- Verfügbarkeit in Europa über Importeure

**Preisübersicht (EUR, 2025/26):**
- 2-Blatt Bronze (Sailor): 180–450
- 3-Blatt Bronze (Match): 250–850
- 4-Blatt Bronze (Dyna Quad): 800–2.500
- 3-Blatt Ni-Al-Bronze: 400–1.200
- Custom-Propeller: ab 1.500 EUR

### 12.8 Weitere Hersteller

| Hersteller | Land | Spezialisierung | Preisklasse (EUR) |
|------------|------|----------------|:-----------:|
| Ewol | Polen | Festpropeller (Custom) | 400–3.000 |
| Vetus | Niederlande | Festpropeller (OEM) | 200–1.500 |
| SPW (Side Power) | Norwegen | Bugstrahlruder-Propeller | 200–800 |
| Sole Diesel | Spanien | OEM-Propeller | 250–900 |
| Torqeedo | Deutschland | E-Antriebs-Propeller | 150–1.200 |
| Quick (QMT) | Italien | Bugstrahlruder-Propeller | 180–700 |
| Piranha | Kanada | Composite-Propeller | 100–400 |
| Acme | USA | Hochleistungs-Festpropeller | 400–1.500 |

---
---

## 13. Fehlerbild-Atlas

### 13.1 Übersicht Fehlermuster

| Nr. | Fehlerbild | Dringlichkeit | Häufigkeit |
|:---:|---------|:---:|:---:|
| F-18_09-01 | Kavitationsschäden an Propellerblättern | Hoch | Häufig |
| F-18_09-02 | Elektrolyse / galvanische Korrosion | Hoch | Häufig |
| F-18_09-03 | Verbogenes Blatt | Mittel–Hoch | Häufig |
| F-18_09-04 | Verlorenes Blatt | Kritisch | Selten |
| F-18_09-05 | Vibration durch Propeller | Mittel | Häufig |
| F-18_09-06 | Bewuchsproblem (Fouling) | Mittel | Sehr häufig |
| F-18_09-07 | Zinkerosion / Anodenverschleiß | Mittel | Häufig |
| F-18_09-08 | Pitch-Fehlanpassung (Überlastung/Unterlastung) | Mittel | Häufig |
| F-18_09-09 | Wellenbohrungsverschleiß (Shaft Hole Wear) | Hoch | Mittel |
| F-18_09-10 | Antifouling-Versagen am Propeller | Gering–Mittel | Häufig |
| F-18_09-11 | Faltmechanismus-Blockade | Mittel | Mittel |
| F-18_09-12 | Linenschneider-Versagen | Mittel | Selten |

---

### F-18_09-01 — Kavitationsschäden an Propellerblättern

**Symptom:** Blattoberfläche zeigt raue, poröse Bereiche, kleine Krater
(Pitting) oder großflächige Erosion. Typisch an der Saugseite (Vorderseite),
besonders an den Blattspitzen und der Vorderkante.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Propeller zu klein für die Motorleistung (BAR zu gering) | 25 % |
| 2 | Pitch zu hoch → Blattüberlastung | 20 % |
| 3 | Zu geringer Abstand Blattspitze → Rumpf | 15 % |
| 4 | Raue Propelleroberfläche (Bewuchs, alte Beschichtung) | 15 % |
| 5 | Propeller beschädigt/verbogen → asymmetrische Anströmung | 10 % |
| 6 | Dauerbetrieb auf Volllast | 8 % |
| 7 | Luft ansaugend (Propeller zu nah an Wasserlinie) | 5 % |
| 8 | Strömungsstörung durch Saildrive-Gehäuse/Stevenrohr | 2 % |

**Sofortmaßnahmen:**
1. Drehzahl reduzieren (80 % Last = deutlich weniger Kavitation)
2. Propeller auf Beschädigungen prüfen (Taucher)
3. Bewuchs entfernen
4. Trim des Bootes optimieren

**Langfristmaßnahmen:**
- Propeller durch Fachbetrieb prüfen und polieren
- Bei schwerem Kavitationsschaden: Propeller ersetzen
- Ggf. Propeller mit höherem BAR (mehr Blätter/Fläche) wählen
- Regelmäßiges Polieren der Propelleroberfläche

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Matte, raue Flecken auf sonst glatter Blattoberfläche
- Kleine Krater (0,5–3 mm) in Gruppen
- Scharfkantige Erosion an der Vorderkante
- In schweren Fällen: Durchbruch des Materials

---

### F-18_09-02 — Elektrolyse / Galvanische Korrosion

**Symptom:** Propellermaterial löst sich auf — rosa/kupferfarbene Flecken
auf Manganbronze (Entzinkung), weiße Ablagerungen auf Aluminium,
allgemeine Materialabnahme. Anoden ungewöhnlich schnell aufgebraucht.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Fehlende oder verbrauchte Opferanoden | 30 % |
| 2 | Fehlströme durch Landstromanschluss (ohne Galv. Isolator) | 25 % |
| 3 | Galvanische Korrosion durch benachbarte edle Metalle | 15 % |
| 4 | Fehlender metallischer Kontakt Anode → Propeller | 10 % |
| 5 | Falsches Anodenmaterial für das Gewässer | 8 % |
| 6 | Fehlströme von benachbarten Booten in der Marina | 7 % |
| 7 | Defekter Landstrom-Trenntrafo | 3 % |
| 8 | Edelstahl-Propeller neben Bronze-Beschlägen | 2 % |

**Sofortmaßnahmen:**
1. Alle Anoden prüfen und ersetzen
2. Landstromanschluss trennen → beobachten ob Korrosion stoppt
3. Galvanischen Isolator installieren (falls nicht vorhanden)
4. Metallischen Kontakt Anode → geschütztes Teil prüfen

**Langfristmaßnahmen:**
- Galvanischen Isolator am Landstromkabel installieren
- Isolationstransformator (Trenntrafo) erwägen
- Regelmäßige Anodeninspektion (halbjährlich in Seewasser)
- Referenzelektrode installieren für Messung des Schutzpotentials
- Auf Ni-Al-Bronze umsteigen (korrosionsbeständiger als Manganbronze)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Rosa/kupferfarbene Bereiche auf Bronze-Propeller (Entzinkung)
- Raue, poröse Oberfläche
- Anoden stark oder vollständig verbraucht
- Weiße Ablagerungen (Zinkoxid) um Anodenbereiche
- Materialverlust an den Blattkanten

---

### F-18_09-03 — Verbogenes Blatt

**Symptom:** Vibrationen, die mit der Drehzahl zunehmen.
Ein oder mehrere Blätter sind sichtbar verbogen (geknickt, verdreht
oder aufgebogen).

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Grundberührung (Fels, Sand, Kette) | 40 % |
| 2 | Treibgut-Einschlag (Holz, Plastik) | 25 % |
| 3 | Leinenwickler (Leine um Propeller gewickelt) | 15 % |
| 4 | Eisschlag (Winterbetrieb) | 8 % |
| 5 | Transport-/Slip-Schaden | 7 % |
| 6 | Materialermüdung (altes Blatt) | 5 % |

**Sofortmaßnahmen:**
1. Drehzahl reduzieren auf Minimum
2. Vibrationsintensität beobachten
3. Bei starker Vibration: Motor stoppen, Propeller tauchen und inspizieren
4. Wenn nur Blattspitze verbogen: vorsichtig weiterfahren möglich

**Langfristmaßnahmen:**
- Propeller durch Fachbetrieb richten lassen (Cold Straightening)
- Pitch-Messung und Neuauswuchtung nach dem Richten
- Bei starker Verformung: Blatt ersetzen (bei Falt-/Feathering)
  oder gesamten Propeller ersetzen
- Linenschneider installieren (präventiv)
- Tiefenkarte des Reviers studieren

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Deutliche Biegung/Knick an einem oder mehreren Blättern
- Verdrehung des Blatts gegenüber der Normalposition
- Aufgebogene Blattspitze(n)
- Kratzspuren oder Riefen auf der Blattoberfläche

---

### F-18_09-04 — Verlorenes Blatt

**Symptom:** Extreme Vibrationen, der Motor läuft ungleichmäßig, deutlicher
Leistungsverlust. Möglicherweise Schäden an Wellenanlage und Motorlager.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Materialermüdung (Riss an der Blattwurzel) | 30 % |
| 2 | Schwere Kavitationserosion (Blatt durchgefressen) | 20 % |
| 3 | Elektrolyse-Schaden (Material so geschwächt, dass Blatt abbricht) | 20 % |
| 4 | Schwerer Einschlag (Fels, Metallgegenstand) | 15 % |
| 5 | Lockere Blattbefestigung (bei Falt-/Feathering-Propellern) | 10 % |
| 6 | Fertigungsfehler (Gusslunker an der Blattwurzel) | 5 % |

**Sofortmaßnahmen:**
1. Motor SOFORT stoppen!
2. Unter Segeln oder mit Schleppboot in den Hafen
3. NICHT versuchen, mit fehlendem Blatt zu fahren (Schaden an Welle/Getriebe!)
4. Taucher beauftragen: restliche Blätter prüfen

**Langfristmaßnahmen:**
- Propeller komplett ersetzen
- Wellenanlage inspizieren (Lager, Stopfbuchse, Getriebeflansch)
- Motorlager prüfen (Gummi kann durch Vibration gerissen sein)
- Ursache klären: Korrosion? Kavitation? Materialfehler?

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Propeller mit offensichtlich fehlendem Blatt
- Bruchstelle an der Nabe: glatt = Ermüdung, rau = Sprödbruch
- Evtl. restliche Blätter angerissen → AUCH ERSETZEN
- Materialverfärbung an der Bruchstelle (rosa = Entzinkung)

---

### F-18_09-05 — Vibration durch Propeller

**Symptom:** Vibrationen, die mit der Motordrehzahl korrelieren.
Spürbar in Rumpf, Steuerstand und/oder Salon. Können drehzahlabhängig
oder belastungsabhängig sein.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Statische Unwucht (ungleichmäßig bewachsen oder erodiert) | 25 % |
| 2 | Verbogenes Blatt (siehe F-18_09-03) | 20 % |
| 3 | Pitch-Unbalance (Blätter haben unterschiedlichen Pitch) | 15 % |
| 4 | Propeller locker auf der Welle | 10 % |
| 5 | Fehlausrichtung Motor ↔ Welle | 10 % |
| 6 | Kavitation (periodisch, bei bestimmten Drehzahlen) | 8 % |
| 7 | Welle verbogen | 7 % |
| 8 | Stevenrohrlager verschlissen | 5 % |

**Sofortmaßnahmen:**
1. Drehzahl variieren — ändert sich die Vibration?
2. Vorwärts vs. Rückwärts — unterschiedlich?
3. Unter Last vs. im Leerlauf — belastungsabhängig?
4. Propeller tauchen und visuell inspizieren

**Langfristmaßnahmen:**
- Propeller abnehmen, reinigen, statisch und dynamisch auswuchten
- Pitch aller Blätter messen und korrigieren
- Wellenausrichtung prüfen (Laser-Alignment)
- Stevenrohrlager und Wellendichtung prüfen/ersetzen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Ungleichmäßiger Bewuchs auf verschiedenen Blättern
- Sichtbare Verformung einzelner Blätter
- Verschlissene oder ausgefranste Blattkanten
- Spiel auf der Welle (Propeller „wackelt")

---

### F-18_09-06 — Bewuchsproblem (Fouling)

**Symptom:** Gradueller Leistungsverlust, Motor muss höhere Drehzahlen
fahren für gleiche Geschwindigkeit, erhöhter Kraftstoffverbrauch.
Bei starkem Bewuchs: Motor überhitzt (Kühlwassereinlass bewachsen).

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Kein oder abgelaufenes Propeller-Antifouling | 40 % |
| 2 | Falsches Antifouling (Rumpf-AF auf Propeller aufgetragen) | 15 % |
| 3 | Boot steht lange still (Marina-Lieger) | 20 % |
| 4 | Warmes Wasser (Mittelmeer, Tropen) | 10 % |
| 5 | Anode bewachsen → galvanische Korrosion fördert Bewuchs | 8 % |
| 6 | Propelleroberfläche rau (Erosion, alte Beschichtung) | 7 % |

**Sofortmaßnahmen:**
1. Taucher beauftragen: Propeller reinigen
2. Wenn möglich: Boot aus dem Wasser nehmen
3. Propeller mit Bürste und Schwamm reinigen (kein Hochdruckreiniger
   auf Propeller-Antifouling!)

**Langfristmaßnahmen:**
- Propeller-spezifisches Antifouling auftragen (PropSpeed, Trilux 33, Prop-Gold)
- Regelmäßiges Taucherputzen (monatlich in Warmwasser-Revieren)
- Bei Dauerlieger: PropSpeed-Beschichtung erwägen (18–24 Monate)
- Boot regelmäßig bewegen (Bewuchs wird bei Fahrt teilweise abgespült)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Grüne/braune Algenbeläge auf Propellerblättern
- Seepocken (weiße, kegelförmige Kalkgehäuse)
- Muscheln (Mytilus, Crassostrea)
- Schlauchförmige Kalkröhren (Serpuliden)

---

### F-18_09-07 — Zinkerosion / Anodenverschleiß

**Symptom:** Opferanoden am Propeller, Welle oder Saildrive sind vorzeitig
aufgebraucht. Möglicherweise bereits Korrosionsschäden am geschützten Metall.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Fehlströme durch Landstrom (ohne Galv. Isolator) | 30 % |
| 2 | Fehlströme von benachbarten Booten in der Marina | 20 % |
| 3 | Warmes Seewasser (Tropen, Mittelmeer Sommer) | 15 % |
| 4 | Anode zu klein dimensioniert | 12 % |
| 5 | Schlechter metallischer Kontakt Anode → geschütztes Teil | 10 % |
| 6 | Benachbarte edle Materialien (Graphit, Edelstahl) | 8 % |
| 7 | Falsches Anodenmaterial für das Gewässer | 5 % |

**Sofortmaßnahmen:**
1. Alle Anoden prüfen und bei >50 % Verbrauch ersetzen
2. Metallischen Kontakt prüfen (kein Antifouling zwischen Anode und Metall!)
3. Galvanischen Isolator prüfen/installieren

**Langfristmaßnahmen:**
- Galvanischen Isolator installieren (150–400 EUR → spart tausende EUR Schaden)
- Anodengrößen erhöhen (im Zweifel: lieber zu viel als zu wenig)
- Halbjährliche Anodeninspektion einplanen
- Referenzelektrode installieren (Schutzpotential messen: Ziel −0,85 bis −1,05 V)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Anoden stark oder vollständig verbraucht (nur noch Befestigungsschraube)
- Weiße/graue Korrosionsprodukte um Anodenbereiche
- Rosa Verfärbung auf Bronze-Teilen (Entzinkung hat begonnen)
- Lochfraß an Edelstahl-Teilen nahe der Anoden

---

### F-18_09-08 — Pitch-Fehlanpassung (Überlastung/Unterlastung)

**Symptom:** Motor erreicht seine Nenndrehzahl nicht (overpropped)
oder überdreht die Nenndrehzahl (underpropped). Erhöhter Kraftstoff-
verbrauch, reduzierte Lebensdauer.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Propeller ab Werk falsch spezifiziert | 25 % |
| 2 | Boot schwerer als vom Hersteller angegeben | 20 % |
| 3 | Unterwasserschiff bewachsen (erhöht den Widerstand) | 20 % |
| 4 | Propeller bei Reparatur falsch eingestellt | 10 % |
| 5 | Motor hat an Leistung verloren (Verschleiß) | 10 % |
| 6 | Falsches Getriebe-Untersetzungsverhältnis | 8 % |
| 7 | Veränderte Betriebsbedingungen (z.B. höhere Beladung) | 7 % |

**Sofortmaßnahmen:**
1. Motor-RPM bei Volllast messen (GPS-Geschwindigkeit notieren)
2. Vergleich mit Nenndrehzahl des Motors (Datenblatt)
3. Slip berechnen (siehe Abschnitt 8.4)

**Langfristmaßnahmen:**
- Pitch anpassen lassen (Festpropeller: durch Fachbetrieb biegen)
- Bei Feathering-Propellern: Pitch-Ring oder -Scheibe wechseln
- Ggf. neuen Propeller mit korrektem Pitch beschaffen
- Unterwasserschiff reinigen und Widerstand reduzieren

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Keine direkten visuellen Anzeichen am Propeller
- Aber: schwarzer Rauch bei Überlastung (Motor)
- Hoher Kraftstoffverbrauch (Logbuch-Vergleich)

---

### F-18_09-09 — Wellenbohrungsverschleiß (Shaft Hole Wear)

**Symptom:** Propeller hat Spiel auf der Welle, klapperndes Geräusch
bei Drehrichtungswechsel, Vibration, die sich bei Drehrichtungswechsel
verschlimmert.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Normaler Verschleiß nach 10.000+ Betriebsstunden | 30 % |
| 2 | Propeller nicht richtig angezogen (Mutter lose) | 25 % |
| 3 | Keilnut ausgeschlagen | 20 % |
| 4 | Korrosion in der Nabenbohrung | 15 % |
| 5 | Propeller-Material zu weich für die Beanspruchung | 10 % |

**Sofortmaßnahmen:**
1. Propellermutter nachziehen und sichern (Split-Pin / Selbstsicherungsmutter)
2. Spiel prüfen (radial und axial)
3. Bei starkem Spiel: nicht auf hoher Drehzahl fahren

**Langfristmaßnahmen:**
- Nabenbohrung aufbohren und neue Wellenpassung einpressen
- Keilnut erneuern
- Propeller durch Fachbetrieb überholen lassen
- Bei starkem Verschleiß: neuen Propeller beschaffen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Propeller „wackelt" sichtbar auf der Welle
- Glänzende Verschleißspuren in der Nabenbohrung
- Ausgeschlagene Keilnut (beim ausgebauten Propeller)
- Rostspuren/Korrosion in der Bohrung

---

### F-18_09-10 — Antifouling-Versagen am Propeller

**Symptom:** Propeller-Antifouling löst sich ab, blättert ab oder bietet
keinen Schutz mehr gegen Bewuchs. Bewuchs bildet sich trotz kürzlich
aufgetragenem Antifouling.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Falsches Antifouling (Rumpf-AF statt Propeller-AF) | 30 % |
| 2 | Primer nicht aufgetragen oder falscher Primer | 25 % |
| 3 | Propelleroberfläche nicht korrekt vorbereitet | 20 % |
| 4 | Antifouling abgelaufen (Haltbarkeit überschritten) | 10 % |
| 5 | Mechanische Beschädigung (Taucher, Grundberührung) | 8 % |
| 6 | Inkompatibles Antifouling-System (alte + neue Schicht) | 7 % |

**Sofortmaßnahmen:**
1. Propeller manuell reinigen (Taucher oder Slip)
2. Altes Antifouling komplett entfernen (Schleifpapier, Abbeizer)
3. Neuauftrag mit korrektem System

**Langfristmaßnahmen:**
- Propeller-spezifisches Antifouling-System verwenden (Primer + Antifouling)
- PropSpeed erwägen (biozidfreie Foul-Release-Beschichtung)
- Herstelleranweisungen genau befolgen (Schichtdicke, Trocknungszeiten)
- Propeller vor dem Auftrag mit Aceton/Lösungsmittel entfetten

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Abblätternde Beschichtungsreste auf dem Propeller
- Teilweiser Bewuchs (dort, wo AF abgeblättert ist)
- Blasenbildung unter der Beschichtung
- Unterschiedliche Farben/Schichten sichtbar (altes + neues AF)

---

### F-18_09-11 — Faltmechanismus-Blockade

**Symptom:** Propellerblätter öffnen sich nicht oder nicht vollständig
beim Einschalten des Motors. Deutlicher Leistungsverlust, ungleichmäßiger
Lauf. Oder: Blätter falten sich nicht zusammen unter Segeln → erhöhter
Widerstand.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Bewuchs im Faltmechanismus (Seepocken in Gelenken) | 30 % |
| 2 | Fett verbraucht (Zahnräder/Lager trocken) | 25 % |
| 3 | Korrosion in den Blattlagern | 20 % |
| 4 | Fremdkörper im Mechanismus (Leinenrest, Steinchen) | 10 % |
| 5 | Defekte Feder (bei federbelasteten Faltpropellern) | 8 % |
| 6 | Zahnrad-Verschleiß oder -Bruch | 5 % |
| 7 | Blatt-Bolzen korrodiert oder festgefressen | 2 % |

**Sofortmaßnahmen:**
1. Motor mehrmals aus und ein → Fliehkraft löst manchmal Blockade
2. Rückwärtsgang → Vorwärtsgang → Rückwärts → Blätter „aufbrechen"
3. Taucher: Blätter manuell bewegen, Bewuchs entfernen
4. Wenn Blätter nicht falten: unter Segeln manuell zusammenklappen (Taucher)

**Langfristmaßnahmen:**
- Propeller aus dem Wasser nehmen, komplett zerlegen, reinigen, fetten
- Alle Lager und Zahnräder inspizieren
- Defekte Teile ersetzen (Lager, Federn, Zahnräder)
- Regelmäßige Wartung einplanen (alle 2–3 Jahre öffnen und fetten)
- PropSpeed oder Antifouling auf den Faltmechanismus auftragen

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Blätter stehen in einer ungewöhnlichen Position
- Bewuchs konzentriert in den Gelenkbereichen
- Korrosionsprodukte (grün, weiß) an den Lagerstellen
- Blätter asymmetrisch geöffnet (ein Blatt mehr als das andere)

---

### F-18_09-12 — Linenschneider-Versagen

**Symptom:** Leine wickelt sich trotz installiertem Linenschneider um
Welle und/oder Propeller. Linenschneider beschädigt oder unwirksam.

**Mögliche Ursachen:**

| Nr. | Ursache | Wahrscheinlichkeit |
|:---:|---|:---:|
| 1 | Schneidkanten verschlissen/stumpf | 30 % |
| 2 | Spalt zwischen rotierend/feststehend zu groß | 25 % |
| 3 | Dickere Leine als vom Schneider ausgelegt | 15 % |
| 4 | Rotierendes Element hat sich gelöst/verschoben | 12 % |
| 5 | Netzreste (dehnbar, rutschen durch den Schneider) | 10 % |
| 6 | Feststehendes Element korrodiert/abgefallen | 8 % |

**Sofortmaßnahmen:**
1. Motor SOFORT stoppen!
2. NICHT versuchen, mit gewickelter Leine weiterzufahren
3. Taucher: Leine freiräumen (Messer mitnehmen!)
4. Linenschneider auf Beschädigung prüfen

**Langfristmaßnahmen:**
- Schneidkanten nachschleifen oder Schneider ersetzen
- Spalt auf 0,5–1 mm einstellen
- Befestigung mit Loctite sichern
- Regelmäßige Inspektion (jährlich bei Slip)

**Visuelle Erkennungsmerkmale (Pipeline B):**
- Leine/Netz um Welle oder Propeller gewickelt
- Abgerundete, stumpfe Schneidkanten
- Großer Spalt zwischen Messern (>2 mm)
- Korrosion oder Bewuchs am Schneidemechanismus

---
---

## 14. Troubleshooting

### 14.1 Motor überhitzt trotz neuem Impeller

**Problem:** Kühlwassertemperatur steigt trotz kürzlich gewechseltem Impeller.

**Diagnostik:**
1. Propeller unter Wasser inspizieren → Bewuchs auf Propeller und
   Seewassereinlass?
2. Seewasserfilter prüfen → verstopft durch Seegras/Plastik?
3. Seewasserauslass prüfen → Seepocken können den Auspuff-Kühler
   verstopfen
4. Kühlwasserschlauch zur Auspuffanlage prüfen → geknickt?
5. Thermostat prüfen → klemmt geschlossen?

**Lösung:** In 30 % der Fälle ist nicht der Motor, sondern ein bewachsener
Propeller die indirekte Ursache: Der Motor muss auf höherer Drehzahl
laufen, um den Leistungsverlust durch Bewuchs zu kompensieren → Überhitzung.

### 14.2 Boot wird langsamer — Propeller oder Rumpf?

**Problem:** Boot erreicht nicht mehr die gewohnte Geschwindigkeit.

**Diagnostik:**
1. Motor-RPM bei Volllast messen
   - RPM wie früher, aber Boot langsamer → **Propellerproblem** (Bewuchs, Erosion)
   - RPM niedriger als früher, Boot langsamer → **Rumpfproblem** (Bewuchs, Gewicht)
   - RPM höher als früher, Boot langsamer → **Motor hat Leistung verloren**
2. Propeller tauchen und inspizieren
3. Unterwasserschiff tauchen und inspizieren
4. Motorparameter prüfen (Öldruck, Temperatur, Abgasfarbe)

### 14.3 Starke Vibrationen nach Propellerwechsel

**Problem:** Nach dem Einbau eines neuen Propellers treten Vibrationen auf.

**Diagnostik:**
1. Propellermutter korrekt angezogen? (Drehmoment nach Hersteller)
2. Keilnut vorhanden und unbeschädigt?
3. Propeller für die richtige Wellen-/Saildrivepassung?
4. Drehrichtung korrekt? (rechts/links — von achtern gesehen)
5. Propeller statisch ausgewuchtet? (Neuer Propeller ≠ ausgewuchtet!)
6. Neuer Pitch stimmt mit altem Pitch überein?

**Lösung:** In 40 % der Fälle ist der neue Propeller nicht korrekt
ausgewuchtet oder hat einen leicht anderen Pitch als der alte.

### 14.4 Faltpropeller öffnet nicht beim ersten Motorstart

**Problem:** Nach dem Segelsetzen will der Motor den Faltpropeller
nicht sofort öffnen.

**Diagnostik:**
1. Drehzahl hoch genug? (Mindestens 1.500 Motor-RPM für ~30 Sekunden)
2. Vorwärtsgang eingelegt? (Rückwärts kann bei einigen Modellen Probleme machen)
3. Bewuchs im Faltmechanismus?
4. Mechanismus gefettet? (Wann war die letzte Wartung?)

**Lösung:** In 80 % der Fälle hilft: Vorwärtsgang einlegen, Gas geben,
5–10 Sekunden warten. Wenn nicht: Rückwärtsgang, kurz Gas, dann
Vorwärtsgang. Bei Gori: auf „High Speed" umschalten, dann normal weiterfahren.

### 14.5 Seitenversatz beim Rückwärtsfahren extrem stark

**Problem:** Beim Rückwärtsfahren zieht das Boot extrem nach einer Seite.

**Diagnostik:**
1. Propeller-Typ prüfen: 2-Blatt Festpropeller → stärkster Seitenversatz
2. Ruder steht gerade oder ist festgestellt?
3. Strömungsverhältnisse (Wind, Strom)?
4. Propeller beschädigt? (asymmetrischer Schub)

**Lösung:** 2-Blatt-Festpropeller haben den stärksten Seitenversatz.
Abhilfe: 3-Blatt-Propeller (120°-Symmetrie reduziert Seitenversatz).
Faltpropeller mit Zahnradsteuerung (Flexofold) bieten auch rückwärts
symmetrischen Schub.

---
---

## 15. FAQ

### 15.1 Allgemeine Fragen

**F: Welcher Propellertyp ist für meine Segelyacht am besten?**
A: Für Segelyachten, die regelmäßig segeln und den Motor nur zum Manövrieren
und bei Flaute nutzen, empfehlen wir einen Falt- oder Feathering-Propeller.
Faltpropeller (Flexofold, Gori) sind etwas günstiger und einfacher in der
Wartung. Feathering-Propeller (Max-Prop, Variprop) bieten etwas höheren
Wirkungsgrad unter Motor und bessere Rückwärtsleistung. Für Motorsegler
und Yachten, die häufig motoren, ist ein guter Festpropeller die
wirtschaftlichste Lösung.

**F: Wie oft sollte ein Propeller gewartet werden?**
A: Festpropeller: jährliche Sichtprüfung, Reinigung, Anodentausch. Alle
5 Jahre: Auswuchten und Pitch-Kontrolle. Faltpropeller: alle 2–3 Jahre
öffnen, reinigen, fetten. Feathering-Propeller: alle 3–5 Jahre öffnen,
Kegelräder inspizieren, fetten. Generell: Antifouling jährlich erneuern,
Anoden jährlich prüfen.

**F: Kann ich den Propeller selbst wechseln?**
A: Ja, wenn das Boot an Land steht und Sie das richtige Werkzeug haben.
Benötigt wird: Propellerabzieher, Drehmomentschlüssel, Keilnut-Werkzeug,
ggf. Impactschrauber. ACHTUNG: Propeller-Mutter muss mit korrektem
Drehmoment angezogen werden (Herstellerangabe beachten!). Split-Pin
nicht vergessen!

**F: Was kostet ein guter Propeller für eine 12-Meter-Segelyacht?**
A: Budget (Festpropeller 3-Blatt Manganbronze): 350–600 EUR.
Mittelklasse (Faltpropeller Flexofold/Gori): 1.200–2.200 EUR.
Premium (Feathering Max-Prop/Variprop): 2.200–3.500 EUR.
Dazu kommen Einbau (~200–400 EUR) und Antifouling (~50–100 EUR).

**F: Wie erkenne ich, ob mein Propeller die richtige Größe hat?**
A: Messen Sie die Motor-RPM bei Volllast (GPS-Geschwindigkeit dabei notieren).
Vergleichen Sie mit der Nenndrehzahl laut Motorhersteller. Wenn die RPM
innerhalb von ±3 % liegen, ist der Propeller korrekt dimensioniert.
Wenn der Motor die Nenndrehzahl nicht erreicht: Propeller zu groß/zu viel
Pitch. Wenn der Motor überdreht: Propeller zu klein/zu wenig Pitch.

### 15.2 Material-Fragen

**F: Manganbronze oder Ni-Al-Bronze — was lohnt sich?**
A: Für Boote, die dauerhaft im Seewasser liegen: Ni-Al-Bronze lohnt sich
fast immer. Die Mehrkosten (50–80 %) werden durch die 2–3-fach längere
Lebensdauer und die bessere Korrosionsbeständigkeit mehr als ausgeglichen.
Für Trailer-Boote, die nach dem Törn herausgenommen werden: Manganbronze
ist ausreichend.

**F: Sind Composite-Propeller gut?**
A: Composite-Propeller (GFK, CFK) sind eine gute Wahl für leichte Boote,
E-Antriebe und Situationen, wo Grundberührung wahrscheinlich ist (das
Blatt bricht statt die Welle). Für schwere Verdränger und hohe Lasten
sind Metallpropeller besser geeignet (steifer, erosionsbeständiger).

**F: Kann ich einen Edelstahl-Propeller auf meine Bronze-Welle montieren?**
A: Ja, aber mit Vorsicht! Edelstahl ist „edler" als Bronze in der galvanischen
Spannungsreihe. Die Bronze-Welle wird schneller korrodieren. Lösung:
ausreichende Opferanoden UND galvanischen Isolator verwenden. Alternativ:
Edelstahl-Welle (empfohlen bei Edelstahl-Propeller).

**F: Warum ist mein Manganbronze-Propeller rosa geworden?**
A: Rosa Verfärbung auf Manganbronze ist ein Zeichen für **Entzinkung**
(Dezincification). Das Zink wird aus der Legierung gelöst, es bleibt
nur das Kupfer zurück. Der Propeller hat in diesen Bereichen nur noch
~20 % seiner ursprünglichen Festigkeit. DRINGEND: Propeller durch
Fachmann prüfen lassen. Opferanoden kontrollieren und ggf. auf
Ni-Al-Bronze umsteigen.

### 15.3 Dimensionierung und Performance

**F: Mein Motor erreicht die Nenndrehzahl nicht — was tun?**
A: Motor ist „overpropped" (zu viel Widerstand). Lösungen in Reihenfolge:
1. Unterwasserschiff reinigen (Bewuchs?)
2. Propeller reinigen und polieren
3. Pitch um 1" reduzieren lassen
4. Falls nichts hilft: kleineren Propeller wählen

**F: Mein Motor überdreht — was tun?**
A: Motor ist „underpropped" (zu wenig Widerstand). Lösungen:
1. Pitch um 1" erhöhen lassen
2. Propeller mit größerem Durchmesser wählen (wenn Platz vorhanden)
3. Mehr Blätter wählen (2-Blatt → 3-Blatt)

**F: Wie viel schneller werde ich mit einem neuen Propeller?**
A: Die typische Verbesserung beim Wechsel von einem schlecht dimensionierten
oder verschlissenen Festpropeller auf einen optimal dimensionierten
Falt- oder Feathering-Propeller beträgt:
- Unter Motor: +0,5–1,5 kn bei gleicher Drehzahl
- Unter Segeln: +0,3–1,0 kn durch reduzierten Propellerwiderstand
- Kraftstoffverbrauch: −10–25 % bei gleicher Geschwindigkeit

**F: Welchen Einfluss hat die Blattanzahl?**
A: Mehr Blätter = ruhigerer Lauf, mehr Schub bei niedrigen Drehzahlen,
weniger Kavitation, ABER: niedrigerer Spitzenwirkungsgrad und mehr
Widerstand. Weniger Blätter = höherer Wirkungsgrad, weniger Widerstand,
ABER: mehr Vibration und weniger Schub bei niedrigen Drehzahlen.
Segelyacht: 2–3 Blätter. Motoryacht: 3–4 Blätter.

**F: Was ist besser — großer Durchmesser oder hoher Pitch?**
A: Im Zweifelsfall: größerer Durchmesser bei niedrigerem Pitch. Ein
größerer Propeller, der langsamer dreht, hat einen höheren Wirkungsgrad
als ein kleinerer, der schneller dreht. Begrenzend ist der verfügbare
Einbauraum.

### 15.4 Wartung und Schutz

**F: Kann ich normales Rumpf-Antifouling auf den Propeller auftragen?**
A: NEIN! Normales Rumpf-Antifouling enthält Kupfer (Kupferoxid, Kupfer-
Thiocyanat), das Bronze-Propeller angreift und Korrosion verursacht.
Verwenden Sie IMMER propeller-spezifisches Antifouling (Trilux 33,
Prop-Gold, Velox Plus) oder Foul-Release-Beschichtung (PropSpeed).

**F: Wie oft sollten die Anoden gewechselt werden?**
A: Faustregel: Anode wechseln, wenn >50 % des Materials verbraucht sind.
In Seewasser typisch: jährlich. In Brackwasser: alle 6–12 Monate. In
Süßwasser: alle 1–2 Jahre. ACHTUNG: Wenn eine Anode innerhalb von
3 Monaten >50 % verliert, gibt es ein Problem (Fehlströme?).

**F: Muss ich den Propeller im Winter abnehmen?**
A: Nicht zwingend, aber empfehlenswert bei Kran-/Slip-Aufenthalt.
Vorteile: bessere Inspektion, Reinigung, Antifouling-Auftrag, Anodentausch.
Bei Faltpropellern: Mechanismus reinigen und fetten. Bei im Wasser
liegenden Booten (Winterliegeplatz): Prop Sock oder PropSpeed verwenden.

**F: Was tun bei Grundberührung?**
A: 1. Motor SOFORT stoppen. 2. Propeller tauchen und inspizieren (Taucher).
3. Bei sichtbarer Beschädigung: vorsichtig unter Motor in den nächsten
Hafen fahren (niedrige Drehzahl, Vibrationen beobachten). 4. An Land:
Propeller abnehmen, Wellenanlage prüfen, Propeller richten oder ersetzen.
NIEMALS eine Grundberührung ignorieren — auch unsichtbare Schäden
(Haarrisse, leichte Verformung) können zu späteren Problemen führen.

### 15.5 Saildrive-spezifische Fragen

**F: Passt jeder Propeller auf meinen Saildrive?**
A: NEIN! Saildrives haben herstellerspezifische Spline-Profile (Volvo,
Yanmar, ZF). Sie benötigen entweder einen Propeller mit dem richtigen
Spline oder einen Universalpropeller mit passendem Adapter. Flexofold,
Max-Prop und Variprop bieten Adapter für alle gängigen Saildrives an.

**F: Mein Saildrive-Gehäuse korrodiert — liegt das am Propeller?**
A: Möglicherweise! Ein zu „edler" Propeller (Edelstahl) auf einem
Aluminium-Saildrive kann galvanische Korrosion am Saildrive verursachen.
Lösung: Ausreichende Opferanoden + galvanischer Isolator. Besser: Bronze-
oder Ni-Al-Bronze-Propeller verwenden (geringerer galvanischer Unterschied).

**F: Brauche ich einen galvanischen Isolator?**
A: JA, wenn Ihr Boot einen Landstromanschluss hat und einen Saildrive
oder Bronze-Propeller besitzt. Ein galvanischer Isolator kostet 150–400 EUR
und kann Schäden von 5.000–15.000 EUR verhindern. Es gibt keinen guten
Grund, keinen zu haben.

### 15.6 Spezielle Anwendungen

**F: Welcher Propeller für Elektroantrieb?**
A: E-Antriebe haben ein anderes Drehzahl-/Drehmoment-Profil als Diesel.
E-Motoren liefern volles Drehmoment ab 0 U/min und drehen typisch bis
1.500–3.000 U/min. Empfohlen: Composite-Propeller (leicht, keine
Korrosion) oder Ni-Al-Bronze mit niedrigem Pitch und großem Durchmesser.
Speziell: Torqeedo bietet optimierte Propeller für ihre Antriebe.

**F: Propeller für Motorsegler — Falt oder Fest?**
A: Motorsegler verbringen typisch 40–60 % der Zeit unter Motor. Hier ist
ein hochwertiger 3-Blatt-Festpropeller oft die bessere Wahl als ein
Faltpropeller, da der Wirkungsgrad unter Motor höher ist und das Boot
häufiger unter Motor fährt. Wenn Segelleistung kritisch ist: Feathering-
Propeller (Max-Prop, Variprop) bieten den besten Kompromiss.

**F: Kann ich meinen 2-Blatt-Propeller durch einen 3-Blatt ersetzen?**
A: Ja, aber beachten: 3-Blatt-Propeller benötigen ~10 % weniger Durchmesser
und ~10 % weniger Pitch für die gleiche Schubkraft. Der Einbauraum
(Propelleröffnung, Saildrive-Gehäuse) muss ausreichen. Ein 3-Blatt läuft
ruhiger, hat bessere Rückwärtsleistung, aber etwas höheren Widerstand
unter Segeln.

**F: Wie messe ich den Pitch meines Propellers?**
A: Professionelle Methode: Pitch-Block und Messuhr (Propellerwerkstatt).
Behelfsmethode: Propellerblatt auf ein flaches Brett legen, Anstellwinkel
bei 0,7 × Radius (Referenzposition) messen. Pitch = tan(Winkel) × 2π × r.
Oder: Hersteller-Markierung auf der Nabe ablesen (Durchmesser × Pitch,
z.B. „16 × 11" = 16" Durchmesser, 11" Pitch).

**F: Was bedeutet RH und LH?**
A: RH = Right Hand (rechts drehend, Standardrichtung für Einzelpropeller-
Boote). LH = Left Hand (links drehend, typisch für Backbord-Motor bei
Doppelanlage). Von achtern betrachtet: RH dreht im Uhrzeigersinn bei
Vorwärtsfahrt.

---
---

## 16. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Autoprop** | Selbstanpassender Propeller der Firma Bruntons, dessen Blätter sich automatisch auf den optimalen Pitch einstellen |
| **BAR (Blade Area Ratio)** | Blattflächenverhältnis — Verhältnis der Gesamtblattfläche zur Propellerkreisfläche (π/4 × D²) |
| **Belüftung (Ventilation)** | Eintritt von Luft (nicht Dampf!) in den Propellerbereich. Ursache: Propeller zu nah an der Wasseroberfläche oder Lufteintritt über den Stevenrohrbereich |
| **Blattprofil** | Querschnittform des Propellerblatts — bestimmt Auftrieb und Widerstand. Typisch: NACA-Profile |
| **Blattspitze (Tip)** | Äußerstes Ende des Propellerblatts — höchste Umfangsgeschwindigkeit, Kavitationsanfälligster Bereich |
| **Blattwurzel (Root)** | Bereich, wo das Blatt in die Nabe übergeht — höchste mechanische Belastung |
| **Bp-δ-Diagramm** | Standarddiagramm für die Propellerauslegung auf Basis der Wageningen B-Serie. Bp = Leistungskoeffizient, δ = Durchmesserkoeffizient |
| **Cavitation** | Siehe Kavitation |
| **Composite-Propeller** | Propeller mit Blättern aus GFK (Glasfaser) oder CFK (Kohlefaser) — leicht, korrosionsfrei, bei Stoß brechend statt verbiegend |
| **CPP (Controllable Pitch Propeller)** | Verstellpropeller, dessen Blattsteigung während der Fahrt hydraulisch verstellt werden kann |
| **Cup** | Leichte Aufwärtskrümmung der Blatthinterkante — wirkt wie eine virtuelle Pitch-Erhöhung, verbessert Kavitationsverhalten |
| **Dezincification** | Entzinkung — selektive Korrosion, bei der Zink aus Manganbronze gelöst wird. Verbleibende schwammige Kupferschicht hat nur ~20 % der Festigkeit |
| **Druckseite** | Rückseite (konvexe Seite) des Propellerblatts — höherer Druck als auf der Saugseite |
| **Duplex-Stahl** | Spezielle Edelstahl-Legierung (z.B. 2205) mit austentisch-ferritischem Gefüge — hervorragende Korrosionsbeständigkeit |
| **Duo-Prop** | Volvo-Penta-System mit zwei gegenläufigen Propellern auf einer Achse (Sterndrive/IPS) |
| **Faltpropeller (Folding Propeller)** | Propeller, dessen Blätter sich unter Segeln zusammenfalten, um den Widerstand zu minimieren |
| **Feathering-Propeller** | Propeller, dessen Blätter sich unter Segeln in Strömungsrichtung drehen (wie eine Windfahne), um den Widerstand zu minimieren |
| **Festpropeller (Fixed-Pitch Propeller, FPP)** | Propeller mit starren, nicht verstellbaren Blättern |
| **Fortschrittsgrad J** | Dimensionsloser Koeffizient J = V_a / (n × D), beschreibt die Betriebsbedingung des Propellers |
| **Foul-Release** | Beschichtungstechnologie, bei der die Oberfläche so glatt ist, dass Bewuchs sich nicht festsetzen kann (z.B. PropSpeed) |
| **Galvanischer Isolator** | Elektronisches Bauteil im Landstromkabel, das galvanische Fehlströme blockiert, aber den Schutzleiter für den Fehlerstrom aufrechterhält |
| **Geared Folding** | Faltpropeller mit Zahnradsteuerung (z.B. Flexofold) — synchrones Öffnen und Schließen aller Blätter |
| **Hub** | Nabe des Propellers — der zentrale Körper, an dem die Blätter befestigt sind |
| **IPS (Inboard Performance System)** | Volvo-Penta-Antriebssystem mit nach vorn gerichteten, gegenläufigen Doppelpropellern unter dem Rumpf |
| **ISO 484** | Internationale Norm für Propellerherstellung — definiert Toleranzklassen (S, I, II, III) |
| **K_Q (Drehmomentenbeiwert)** | Dimensionsloser Koeffizient K_Q = Q / (ρ × n² × D⁵) |
| **K_T (Schubbeiwert)** | Dimensionsloser Koeffizient K_T = T / (ρ × n² × D⁴) |
| **Kavitation** | Bildung und Zusammenfall von Dampfblasen in Wasser aufgrund lokaler Druckabsenkung unter den Dampfdruck. Zerstört Propellerblätter |
| **Keilnut (Keyway)** | Längsnut in der Propellernabe und auf der Welle, in die ein Keil (Key) eingesetzt wird, um Drehmoment zu übertragen |
| **Linenschneider (Rope Cutter)** | Schneidvorrichtung auf der Propellerwelle, die Leinen und Netze zerschneidet, bevor sie sich um die Welle wickeln |
| **Manganbronze** | Kupfer-Zink-Legierung (Cu 55–60 %, Zn 36–42 %) — preisgünstiges Standard-Propellermaterial |
| **Nachstromfaktor (Wake Fraction, w)** | Maß für die Strömungsverlangsamung hinter dem Rumpf: V_a = V_s × (1 − w). Typisch: 0,15–0,30 |
| **NAB** | Nickel-Aluminium-Bronze — korrosionsbeständige Kupfer-Aluminium-Legierung für hochwertige Propeller |
| **Ni-Al-Bronze** | Siehe NAB |
| **Overpropping** | Zustand, in dem der Propeller zu viel Widerstand bietet → Motor kann Nenndrehzahl nicht erreichen |
| **P/D Ratio (Pitch-Ratio)** | Verhältnis Steigung/Durchmesser — Maß für die „Steilheit" des Propellers |
| **Pitch (Steigung)** | Theoretische Vorwärtsbewegung des Propellers pro Umdrehung in einem festen Medium (in Zoll oder mm) |
| **PREN** | Pitting Resistance Equivalent Number — Maß für die Lochfraßbeständigkeit von Edelstahl. Höher = besser |
| **Prop Curve** | Leistungskurve, die beschreibt, wie viel Leistung der Propeller bei jeder Drehzahl aufnimmt |
| **PropSpeed** | Foul-Release-Beschichtungssystem aus Neuseeland für Propeller und Unterwasserbauteile |
| **Rake** | Winkel, um den die Propellerblätter aus der Propellerebene nach hinten geneigt sind |
| **Saildrive** | Antriebssystem für Segelyachten, bei dem Motor und Getriebe direkt durch den Rumpf nach unten ragen |
| **Saugseite** | Vorderseite (konkave Seite) des Propellerblatts — niedrigerer Druck als auf der Druckseite |
| **Schub (Thrust)** | Kraft, die der Propeller in Vorwärtsrichtung erzeugt [N] |
| **Seitenversatz (Prop Walk)** | Seitliche Kraft des Propellers, die das Heck zur Seite drückt — besonders stark bei Rückwärtsfahrt |
| **Skew** | Sichelförmige Verdrehung der Blätter — reduziert Vibrationen und Druckpulsationen |
| **Slip** | Differenz zwischen theoretischer (Pitch × RPM) und tatsächlicher Geschwindigkeit, in Prozent |
| **Spline** | Keilwellenprofil auf der Saildrive-/Getriebewelle zur Drehmomentübertragung auf den Propeller |
| **Underpropping** | Zustand, in dem der Propeller zu wenig Widerstand bietet → Motor überdreht die Nenndrehzahl |
| **Wageningen B-Serie** | Systematische Propeller-Testreihe (MARIN, Niederlande), die seit 1937 die Grundlage der Propellerauslegung bildet |
| **Wellenanode (Shaft Anode)** | Opferanode, die um die Propellerwelle geklemmt wird, um Welle und Propeller vor galvanischer Korrosion zu schützen |
| **WOT RPM** | Wide Open Throttle RPM — Motordrehzahl bei Vollgas unter Last |

---
---

## 17. Schnell-Referenz

### 17.1 Propellertyp-Entscheidungsbaum

```
Bootstyp?
├── Segelyacht
│   ├── Budget < 1.000 EUR
│   │   └── Festpropeller 2-/3-Blatt Manganbronze
│   ├── Häufig Segeln (>60 %)
│   │   ├── Wert auf einfache Wartung
│   │   │   └── Faltpropeller (Flexofold, Gori)
│   │   └── Wert auf max. Wirkungsgrad
│   │       └── Feathering (Max-Prop, Variprop)
│   ├── Häufig Motor (>40 %)
│   │   └── Feathering (Max-Prop, Variprop, Autoprop)
│   └── Langfahrt / Weltumsegelung
│       └── Feathering Ni-Al-Bronze (Max-Prop Classic, Kiwiprop)
├── Motoryacht (Verdränger)
│   ├── < 15 m
│   │   └── 3-Blatt Festpropeller Ni-Al-Bronze
│   └── > 15 m
│       └── 4-Blatt Festpropeller Ni-Al-Bronze oder CPP
├── Motorsegler
│   ├── Viel Segeln
│   │   └── Feathering (Max-Prop, Variprop)
│   └── Viel Motor
│       └── 3-Blatt Festpropeller oder Feathering
└── Elektroantrieb
    └── Composite-Propeller oder Torqeedo-spezifisch
```

### 17.2 Wartungsintervalle Kurzübersicht

| Maßnahme | Festpropeller | Faltpropeller | Feathering |
|----------|:---:|:---:|:---:|
| Sichtprüfung (Taucher) | Jährlich | Jährlich | Jährlich |
| Anoden prüfen/ersetzen | Jährlich | Jährlich | Jährlich |
| Antifouling erneuern | Jährlich | Jährlich | Jährlich |
| Polieren | Alle 2–3 Jahre | Alle 2–3 Jahre | Alle 2–3 Jahre |
| Mechanismus warten | – | Alle 2–3 Jahre | Alle 3–5 Jahre |
| Auswuchten/Pitch prüfen | Alle 5 Jahre | Alle 5 Jahre | Alle 5 Jahre |

### 17.3 Troubleshooting Schnellreferenz

| Problem | Erste Prüfung | Wahrscheinlichste Ursache |
|---------|--------------|--------------------------|
| Motor erreicht Nenndrehzahl nicht | Unterwasserschiff sauber? | Bewuchs am Rumpf/Propeller |
| Motor überdreht | Propeller beschädigt? | Blatt verbogen oder fehlt |
| Starke Vibrationen | Propeller tauchen | Verbogenes Blatt, Unwucht |
| Leistungsverlust graduell | Propeller ansehen | Bewuchs, Erosion |
| Leistungsverlust plötzlich | Propeller tauchen | Leine, Blattbruch |
| Seitenversatz extrem | 2-Blatt-Propeller? | Normaler Prop-Effekt |
| Faltprop öffnet nicht | Gas geben, warten | Bewuchs im Mechanismus |
| Anoden schnell verbraucht | Galv. Isolator vorhanden? | Fehlströme Landstrom |

### 17.4 Propeller-Checkliste für Jahresinspektion

```
□ 1. Propellerblätter auf Beschädigung prüfen (Risse, Kerben, Verformung)
□ 2. Oberfläche auf Kavitationserosion prüfen (raue Stellen, Krater)
□ 3. Oberfläche auf Korrosion prüfen (rosa = Entzinkung!)
□ 4. Bewuchs entfernen (Bürste, Schaber, KEIN Hochdruckreiniger auf AF!)
□ 5. Blattkanten auf Schärfe prüfen (erodierte Kanten = Wirkungsgradeinbuße)
□ 6. Propellermutter prüfen (fest? Split-Pin vorhanden?)
□ 7. Wellenanode prüfen und ggf. ersetzen
□ 8. Propeller-Zinkkegel prüfen und ggf. ersetzen
□ 9. Saildrive-Anoden prüfen und ggf. ersetzen
□ 10. Bei Faltpropellern: Mechanismus auf Leichtgängigkeit prüfen
□ 11. Antifouling-Zustand prüfen — erneuern?
□ 12. Linenschneider auf Verschleiß prüfen (Schneidkanten scharf?)
□ 13. Wellenspiel prüfen (radial und axial)
□ 14. Propellerwelle auf Korrosion/Riefen prüfen
□ 15. Stevenrohr-Dichtung auf Leckage prüfen
```

---
---

## 18. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Bavaria 38 — Faltpropeller vs. Festpropeller

**Boot:** Bavaria 38 Cruiser, Baujahr 2018
**Motor:** Volvo D2-40, 40 PS, Saildrive SD130
**Revier:** Ostsee, Deutschland/Dänemark/Schweden

**Ausgangssituation:**
Der Eigner segelte jährlich 2.500 sm, davon ca. 600 sm unter Motor.
Der originale 3-Blatt-Festpropeller (Volvo 16" × 10" Manganbronze) war
nach 6 Jahren deutlich erodiert und verursachte Vibrationen.

**Maßnahme:**
Wechsel auf Flexofold 3-Blatt Saildrive, 16" × 11", Ni-Al-Bronze.
Kosten: Propeller 2.150 EUR + Einbau 250 EUR + PropSpeed 220 EUR = 2.620 EUR total.

**Ergebnisse:**
- Geschwindigkeit unter Motor bei 2.800 U/min: 6,4 kn → 6,8 kn (+0,4 kn)
- Geschwindigkeit unter Segeln bei 5 kn Wind: +0,2–0,4 kn durch reduzierten Widerstand
- Motor erreicht Nenndrehzahl: 3.580 U/min (Ziel: 3.600 ±3 %) → perfekt
- Rückwärtsleistung: deutlich besser als Festpropeller (Hafenmanöver einfacher)
- Kraftstoffverbrauch: −15 % bei gleicher Geschwindigkeit unter Motor

**Amortisation:** Bei 300 Motorstunden/Jahr und −15 % Diesel: ~80 EUR/Jahr
Ersparnis. Amortisation des Propellers (vs. neuer Festpropeller 500 EUR):
(2.620 − 500) / 80 = 26 Jahre über Diesel. Aber: Der wahre Wert liegt
in der Segelleistung (+0,3 kn = ~5 % mehr VMG).

---

### ANHANG B — Fallstudie: Hallberg-Rassy 43 — Max-Prop vs. Autoprop

**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2014
**Motor:** Volvo D2-75, 75 PS, Saildrive SD150
**Revier:** Mittelmeer (Langfahrt: Spanien → Kanarische Inseln → Karibik)

**Ausgangssituation:**
Für eine geplante Atlantiküberquerung musste der originale Volvo
2-Blatt-Faltpropeller ersetzt werden. Die Rückwärtsleistung war
unzureichend für enge Marinas in der Karibik.

**Option 1:** Max-Prop Whisper 3-Blatt, 19" — 3.800 EUR
**Option 2:** Bruntons Autoprop H5, 19" — 3.200 EUR

**Entscheidung:** Der Eigner installierte den Max-Prop Whisper.

**Ergebnisse nach 12.000 sm:**
- Motorgeschwindigkeit bei 2.500 U/min: 7,2 kn (zuvor 6,5 kn mit Faltpropeller)
- Rückwärtsleistung: exzellent, volle Manövrierfähigkeit in engen Marinas
- Segelperformance: +0,3 kn gegenüber altem 2-Blatt-Faltpropeller
- Kraftstoffverbrauch: −18 % bei Marschfahrt (6,5 kn)
- Wartung nach 12.000 sm: Nabe geöffnet, Kegelräder OK, neu gefettet (1h Arbeit)

**Fazit:** Der Max-Prop Whisper überzeugte besonders durch die leise
Laufkultur und die hervorragende Rückwärtsleistung. Die Investition von
3.800 EUR hat sich durch Kraftstoffeinsparung und erhöhten Segelkomfort
gelohnt.

---

### ANHANG C — Fallstudie: Jeanneau Sun Odyssey 440 — Kavitationsschaden

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2020
**Motor:** Yanmar 4JH57, 57 PS, Saildrive SD50
**Propeller:** 3-Blatt Festpropeller, 15" × 11", Manganbronze (OEM)
**Revier:** Kroatien, Adria

**Situation:**
Nach 3 Saisons (800 Motorstunden) zeigte der Propeller deutliche
Kavitationserosion an den Blattvorderkanten. Motor erreichte die
Nenndrehzahl nur noch bei 3.100 U/min (Soll: 3.400 ±100).

**Diagnose:**
- Propelleroberfläche stark bewachsen (nur jährlich gereinigt)
- Bewuchs erhöhte Oberflächenrauheit → verstärkte Kavitation
- Erosion reduzierte Blattfläche → Motor wurde overpropped
- Saildrive-Anoden waren zu 80 % verbraucht → zusätzliche Korrosion

**Maßnahme:**
1. Propeller durch Fachbetrieb repariert (Erosionsstellen aufgeschweißt, poliert)
2. Pitch von 11" auf 10,5" reduziert (bessere Drehzahlabstimmung)
3. PropSpeed-Beschichtung aufgetragen
4. Alle Anoden erneuert
5. Galvanischer Isolator installiert (fehlte!)

**Kosten:** Reparatur 380 EUR + PropSpeed 220 EUR + Anoden 65 EUR +
Galv. Isolator 280 EUR + Arbeit 200 EUR = 1.145 EUR

**Ergebnis nach 1 Saison:**
- Motor erreicht 3.380 U/min bei Volllast → korrekt
- Keine Kavitationsgeräusche mehr
- PropSpeed hält Propeller bewuchsfrei
- Anoden-Verbrauch normalisiert (30 % nach 12 Monaten statt 80 %)

---

### ANHANG D — Fallstudie: Bénéteau Océanis 46.1 — Elektrolyse-Totalschaden

**Boot:** Bénéteau Océanis 46.1, Baujahr 2021
**Motor:** Yanmar 4JH80, 80 PS, Saildrive SD60
**Propeller:** Volvo 3-Blatt Faltpropeller, 18" × 12"
**Revier:** Griechenland, Athen (Marina Alimos)

**Situation:**
Nach nur 2 Jahren (400 Motorstunden) war der Aluminium-Saildrive
schwer korrodiert. Propellernabe zeigte weiße Korrosionsablagerungen,
Saildrive-Gehäuse hatte mehrere Lochfraß-Stellen.

**Diagnose:**
- Kein galvanischer Isolator installiert (ab Werft fehlend!)
- Marina hatte Fehlstrom-Probleme (benachbarte Stahl-Motoryacht)
- Saildrive-Anoden waren nach 6 Monaten vollständig verbraucht
- Eigner hatte Anoden nicht geprüft (Unwissenheit)

**Reparatur:**
1. Saildrive-Gehäuse komplett ersetzt (Yanmar OEM)
2. Alle Anoden erneuert
3. Galvanischer Isolator installiert (Diodentyp)
4. Fehlstrom-Messung in der Marina veranlasst
5. Propeller poliert und Antifouling erneuert

**Kosten:**
- Saildrive-Gehäuse: 4.800 EUR
- Einbau + Dichtungen: 1.200 EUR
- Galvanischer Isolator: 320 EUR
- Anoden + Antifouling: 180 EUR
- **Gesamt: 6.500 EUR**

**Lerneffekt:** Ein galvanischer Isolator (320 EUR) hätte 6.180 EUR
Schaden verhindert! JEDES Boot mit Landstromanschluss braucht einen!

---

### ANHANG E — Fallstudie: Oyster 485 — Langfahrt-Propellerwahl

**Boot:** Oyster 485, Baujahr 2016
**Motor:** Yanmar 4JH110, 110 PS, Saildrive SD60
**Revier:** Weltumsegelung (Atlantik, Pazifik, Indischer Ozean)

**Ausgangssituation:**
Vor der Weltumsegelung stand die Frage: Welcher Propeller hält 3 Jahre
und 40.000 sm ohne Zugang zu spezialisierten Werkstätten?

**Evaluierte Optionen:**
1. Max-Prop Classic 3-Blatt Ni-Al-Bronze (3.500 EUR)
2. Flexofold 3-Blatt Ni-Al-Bronze (2.600 EUR)
3. Kiwiprop 3-Blatt (2.400 EUR)
4. Bruntons Autoprop H5 (3.200 EUR)

**Entscheidung:** Max-Prop Classic 3-Blatt — Begründung:
- Bewährteste Technik für Langfahrt (50 Jahre Erfahrung)
- Ersatzteile weltweit verfügbar
- Mechanismus sehr robust (Kegelräder halten 25+ Jahre)
- Vollwertiger Rückwärtsgang (wichtig in Korallenriffen)
- Ni-Al-Bronze-Blätter: korrosionsbeständig, reparierbar

**Ergebnis nach 38.000 sm (2,5 Jahre):**
- Keine mechanischen Probleme
- 1× Grundberührung (Korallenriff, Fidschi): Blattspitze leicht verbogen
  → durch Taucher vor Ort gerichtet (provisorisch, hielt bis zum nächsten
  Werftaufenthalt in Neuseeland)
- 2× Nabe geöffnet und gefettet (Panama, Neuseeland)
- PropSpeed-Beschichtung alle 12 Monate erneuert (4× total)
- Motor-RPM über die gesamte Reise stabil: 2.900 ±50 U/min bei Volllast

---

### ANHANG F — Fallstudie: Linssen Grand Sturdy 40.0 — Propellerwechsel

**Boot:** Linssen Grand Sturdy 40.0 AC, Baujahr 2012
**Motor:** Vetus Deutz DT64, 60 PS, Wellenantrieb
**Propeller:** 3-Blatt Festpropeller, 18" × 14", Manganbronze (OEM)
**Revier:** Niederländische Binnengewässer und Nordsee-Küste

**Ausgangssituation:**
Motor erreichte nur noch 2.600 U/min bei Volllast (Soll: 3.000 U/min).
Geschwindigkeit max. 7,2 kn (Soll: 8,5 kn). Hoher Kraftstoffverbrauch.

**Diagnose:**
1. Propeller: Manganbronze mit deutlicher Entzinkung (rosa Verfärbung)
2. Wellenanlage: Stevenrohrlager verschlissen (Spiel 0,8 mm statt max 0,3 mm)
3. Unterwasserschiff: leichter Bewuchs
4. Motor: Leistung OK (Kompressionstest bestanden)

**Maßnahme:**
1. Neuer Propeller: Michigan Wheel Match 3-Blatt, 18" × 13", Ni-Al-Bronze
   (1" weniger Pitch wegen leichter Überladung durch Ausrüstung)
2. Stevenrohrlager erneuert
3. Wellenanode und Rumpfanoden erneuert
4. Unterwasserschiff gereinigt und neu beschichtet

**Kosten:**
- Propeller (Michigan Wheel Ni-Al-Bronze): 680 EUR
- Stevenrohrlager: 350 EUR
- Anoden: 85 EUR
- Antifouling (Rumpf + Propeller): 280 EUR
- Arbeit (Slip, Montage): 850 EUR
- **Gesamt: 2.245 EUR**

**Ergebnis:**
- Motor-RPM bei Volllast: 3.020 U/min → perfekt
- Geschwindigkeit: 8,3 kn → fast wie Soll
- Kraftstoffverbrauch: −22 % bei Marschfahrt (7,5 kn)
- Vibrationen: deutlich reduziert
- Amortisation Diesel-Ersparnis: ~1,5 Jahre

---

### ANHANG G — Fallstudie: Contest 42 — Propeller-Vibration nach Osmose-Reparatur

**Boot:** Contest 42, Baujahr 2005
**Motor:** Volvo D2-55, 55 PS, Wellenantrieb
**Propeller:** Max-Prop 3-Blatt, 17" (seit 2010)
**Revier:** Nordsee, Niederlande

**Situation:**
Nach einer umfangreichen Osmose-Reparatur (Unterwasserschiff komplett
erneuert) traten starke Vibrationen bei Motorbetrieb auf.
Propeller war nicht angetastet worden.

**Diagnose:**
1. Motorausrichtung: 0,35 mm Abweichung (nach Osmose-Reparatur)
2. Stevenrohr: leicht versetzt (Rumpfverformung durch Osmose-Reparatur: 2 mm)
3. Propeller: Max-Prop mechanisch einwandfrei, aber Pitch-Einstellung
   stimmte nicht mehr (Boot war 500 kg schwerer durch Osmose-Epoxid-Schichten!)

**Maßnahme:**
1. Motor-Laser-Alignment (0,35 mm → 0,05 mm)
2. Stevenrohr-Buchse erneuert und zentriert
3. Max-Prop Pitch-Ring von „Medium" auf „Low" gewechselt

**Kosten:**
- Motor-Alignment: 450 EUR
- Stevenrohr-Buchse: 280 EUR
- Pitch-Ring (Max-Prop): 120 EUR
- Arbeit (Slip): 400 EUR
- **Gesamt: 1.250 EUR**

**Ergebnis:**
- Vibrationen: komplett verschwunden
- Motor-RPM bei Volllast: 3.400 U/min (vorher: 3.050 U/min → overpropped!)
- Geschwindigkeit: 7,0 kn (vorher: 6,2 kn)
- Lerneffekt: Nach JEDER Rumpfarbeit → Motorausrichtung UND Propeller-Pitch prüfen!

---

### ANHANG H — Fallstudie: Hanse 508 — Composite-Propeller am E-Motor

**Boot:** Hanse 508 (Retrofit), Baujahr 2019
**Original-Motor:** Volvo D3-150, 150 PS (entfernt)
**Neuer Antrieb:** Oceanvolt ServoProp 25 kW + 40 kWh LiFePO4-Batterie
**Propeller:** Oceanvolt Composite 3-Blatt, 19", CFK-Blätter, Edelstahl-Nabe
**Revier:** Ostsee, Dänemark

**Ausgangssituation:**
Im Rahmen eines umfangreichen E-Motor-Retrofits musste ein neuer
Propeller gewählt werden, der zum E-Antrieb passt.

**Warum Composite?**
- E-Motor wiegt 45 kg (statt 280 kg Diesel) → Boot leichter
- Leichter Propeller (1,8 kg statt 8 kg Bronze) → weniger Trägheit
- Keine galvanische Korrosion (CFK + Edelstahl + Aluminium-Saildrive)
- Hoher Wirkungsgrad bei niedrigen Drehzahlen (E-Motor-optimiert)

**Ergebnisse nach 2 Saisons (3.000 sm):**
- Motorgeschwindigkeit bei 100 % Leistung: 7,5 kn
- Motorgeschwindigkeit bei 50 % Leistung: 6,2 kn (Marschfahrt)
- Reichweite bei 50 %: 42 sm (nur Batterie, kein Generator)
- Keine Korrosionsprobleme (CFK ist galvanisch neutral)
- Propeller: kein Verschleiß, keine Erosion nach 2 Jahren

**Einschränkung:**
- 1× leichte Grundberührung: keine Beschädigung (CFK ist elastisch)
- Bewuchs etwas stärker als bei Bronze (rauere Oberfläche)
  → Lösung: PropSpeed-Beschichtung

---
---

## 19. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — PropellerType Enum

```python
from enum import Enum


class PropellerType(str, Enum):
    """Propellertyp-Klassifikation."""
    FIXED_2_BLADE = "fixed_2_blade"
    FIXED_3_BLADE = "fixed_3_blade"
    FIXED_4_BLADE = "fixed_4_blade"
    FIXED_5_BLADE = "fixed_5_blade"
    FOLDING_2_BLADE = "folding_2_blade"
    FOLDING_3_BLADE = "folding_3_blade"
    FEATHERING_2_BLADE = "feathering_2_blade"
    FEATHERING_3_BLADE = "feathering_3_blade"
    FEATHERING_4_BLADE = "feathering_4_blade"
    AUTOPROP = "autoprop"
    CPP = "controllable_pitch"
    COMPOSITE_2_BLADE = "composite_2_blade"
    COMPOSITE_3_BLADE = "composite_3_blade"
    DUO_PROP = "duo_prop"
    UNKNOWN = "unknown"
```

---

### ANHANG J — PropellerMaterial und DriveType Enums

```python
class PropellerMaterial(str, Enum):
    """Propeller-Werkstoff."""
    MANGANESE_BRONZE = "manganese_bronze"
    NI_AL_BRONZE = "ni_al_bronze"
    STAINLESS_316L = "stainless_316l"
    STAINLESS_DUPLEX = "stainless_duplex"
    GFK_COMPOSITE = "gfk_composite"
    CFK_COMPOSITE = "cfk_composite"
    ALUMINIUM = "aluminium"
    UNKNOWN = "unknown"


class DriveType(str, Enum):
    """Antriebstyp / Wellenanlage."""
    SHAFT_DRIVE = "shaft_drive"
    SAILDRIVE_VOLVO = "saildrive_volvo"
    SAILDRIVE_YANMAR = "saildrive_yanmar"
    SAILDRIVE_ZF = "saildrive_zf"
    STERNDRIVE = "sterndrive"
    IPS = "ips"
    OUTBOARD = "outboard"
    POD_DRIVE = "pod_drive"
    ELECTRIC_DIRECT = "electric_direct"
    UNKNOWN = "unknown"


class PropellerCondition(str, Enum):
    """Zustandsbewertung Propeller."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class CavitationType(str, Enum):
    """Kavitationstyp."""
    NONE = "none"
    SHEET = "sheet_cavitation"
    TIP_VORTEX = "tip_vortex"
    BUBBLE = "bubble_cavitation"
    HUB_VORTEX = "hub_vortex"
    MULTIPLE = "multiple_types"
    UNKNOWN = "unknown"


class FoulingLevel(str, Enum):
    """Bewuchsgrad."""
    CLEAN = "clean"
    LIGHT_SLIME = "light_slime"
    ALGAE_LIGHT_BARNACLES = "algae_light_barnacles"
    HEAVY_BARNACLES = "heavy_barnacles"
    SEVERE_FOULING = "severe_fouling"
    UNKNOWN = "unknown"


class FailureSeverity(str, Enum):
    """Schweregrad eines Fehlers/Befunds."""
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
```

---

### ANHANG K — PropellerSpec (Basis-Datenmodell)

```python
from pydantic import BaseModel, Field
from typing import Optional


class PropellerSpec(BaseModel):
    """
    Spezifikation eines Marine-Propellers.
    Enthält alle relevanten physikalischen und technischen Daten.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Hersteller (z.B. 'Flexofold', 'Max-Prop')")
    model_name: str = Field(..., description="Modellbezeichnung")
    serial_number: Optional[str] = Field(None, description="Seriennummer")
    year_of_manufacture: Optional[int] = Field(None, ge=1900, le=2100, description="Baujahr")

    # Typ und Material
    propeller_type: PropellerType = Field(..., description="Propellertyp")
    material: PropellerMaterial = Field(..., description="Werkstoff")
    blade_count: int = Field(..., ge=2, le=7, description="Blattanzahl")

    # Geometrie
    diameter_mm: float = Field(..., gt=0, description="Durchmesser [mm]")
    diameter_inch: Optional[float] = Field(None, gt=0, description="Durchmesser [Zoll]")
    pitch_mm: float = Field(..., gt=0, description="Steigung [mm]")
    pitch_inch: Optional[float] = Field(None, gt=0, description="Steigung [Zoll]")
    pitch_ratio: Optional[float] = Field(
        None, gt=0, le=3.0,
        description="Steigungsverhältnis P/D"
    )
    blade_area_ratio: Optional[float] = Field(
        None, gt=0, le=1.5,
        description="Blattflächenverhältnis (BAR)"
    )
    rake_degrees: Optional[float] = Field(
        None, ge=-30, le=45,
        description="Blattneigung (Rake) [°]"
    )
    skew_degrees: Optional[float] = Field(
        None, ge=0, le=90,
        description="Blattverwindung (Skew) [°]"
    )
    cup_mm: Optional[float] = Field(
        None, ge=0, le=10,
        description="Cup-Höhe an der Hinterkante [mm]"
    )

    # Antrieb
    drive_type: DriveType = Field(..., description="Antriebstyp")
    shaft_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Wellendurchmesser [mm]"
    )
    rotation: str = Field(
        "RH",
        pattern="^(RH|LH)$",
        description="Drehrichtung: RH (rechts) oder LH (links)"
    )

    # Gewicht
    weight_kg: Optional[float] = Field(
        None, gt=0,
        description="Gewicht [kg]"
    )

    # Preis
    price_eur: Optional[float] = Field(
        None, ge=0,
        description="Listenpreis [EUR]"
    )
```

---

### ANHANG L — PropellerConditionAssessment

```python
class PropellerConditionAssessment(BaseModel):
    """
    Zustandsbewertung eines Propellers — kombiniert visuelle und
    strukturelle Analyse.
    """
    model_config = {"from_attributes": True}

    propeller_id: str = Field(..., description="Propeller-Referenz-ID")
    assessment_date: str = Field(..., description="Bewertungsdatum (ISO 8601)")

    # Zustand
    overall_condition: PropellerCondition = Field(
        ..., description="Gesamtzustand"
    )
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung (0–100)"
    )

    # Kavitation
    cavitation_type: CavitationType = Field(
        CavitationType.NONE,
        description="Identifizierter Kavitationstyp"
    )
    cavitation_severity: FailureSeverity = Field(
        FailureSeverity.INFO,
        description="Schwere der Kavitationsschäden"
    )
    cavitation_area_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Betroffene Blattfläche [%]"
    )

    # Korrosion
    corrosion_detected: bool = Field(
        False, description="Korrosion festgestellt?"
    )
    dezincification_detected: bool = Field(
        False, description="Entzinkung festgestellt?"
    )
    electrolysis_detected: bool = Field(
        False, description="Elektrolyse-Schäden festgestellt?"
    )

    # Mechanik (Falt/Feathering)
    mechanism_functional: Optional[bool] = Field(
        None, description="Mechanismus funktioniert? (None = Festpropeller)"
    )
    mechanism_notes: Optional[str] = Field(
        None, description="Anmerkungen zum Mechanismus"
    )

    # Bewuchs
    fouling_level: FoulingLevel = Field(
        FoulingLevel.UNKNOWN,
        description="Bewuchsgrad"
    )
    antifouling_condition: Optional[str] = Field(
        None, description="Zustand der Antifouling-Beschichtung"
    )

    # Blätter
    blade_damage: list[str] = Field(
        default_factory=list,
        description="Liste der Blattschäden (z.B. 'Blatt 1: Spitze verbogen')"
    )
    blade_balance_ok: Optional[bool] = Field(
        None, description="Statische Balance OK?"
    )
    pitch_balance_ok: Optional[bool] = Field(
        None, description="Pitch-Balance OK?"
    )

    # Anoden
    anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Verbleibende Anoden-Kapazität [%]"
    )
    anode_replacement_needed: bool = Field(
        False, description="Anodenwechsel erforderlich?"
    )

    # Wellenpassung
    shaft_fit_ok: Optional[bool] = Field(
        None, description="Passung auf der Welle OK?"
    )
    shaft_play_mm: Optional[float] = Field(
        None, ge=0,
        description="Spiel auf der Welle [mm]"
    )

    # Befunde und Empfehlungen
    findings: list[str] = Field(
        default_factory=list,
        description="Befunde (Deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (Deutsch)"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe der Bewertung"
    )
    data_sources: list[str] = Field(
        default_factory=list,
        description="Verwendete Datenquellen (structured, visual, text)"
    )
```

---

### ANHANG M — PropellerDimensioning

```python
class PropellerDimensioning(BaseModel):
    """
    Berechnung der optimalen Propellerdimensionierung für ein Boot.
    """
    model_config = {"from_attributes": True}

    # Eingabedaten Boot
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: str = Field(
        ..., description="Bootstyp (sailboat, motorboat, motorsailer)"
    )
    loa_m: float = Field(..., gt=0, description="Länge über Alles [m]")
    lwl_m: float = Field(..., gt=0, description="Wasserlinienlänge [m]")
    displacement_kg: float = Field(
        ..., gt=0, description="Verdrängung [kg]"
    )
    hull_speed_kn: Optional[float] = Field(
        None, gt=0,
        description="Rumpfgeschwindigkeit [kn]"
    )
    target_speed_kn: float = Field(
        ..., gt=0,
        description="Ziel-Motorgeschwindigkeit [kn]"
    )

    # Eingabedaten Motor
    engine_power_hp: float = Field(
        ..., gt=0, description="Motorleistung [PS]"
    )
    engine_rpm_rated: float = Field(
        ..., gt=0, description="Motor-Nenndrehzahl [U/min]"
    )
    gear_ratio: float = Field(
        ..., gt=0, description="Getriebe-Untersetzungsverhältnis"
    )
    gear_efficiency: float = Field(
        0.95, gt=0, le=1.0,
        description="Getriebe-Wirkungsgrad"
    )
    shaft_efficiency: float = Field(
        0.97, gt=0, le=1.0,
        description="Wellenleitung-Wirkungsgrad"
    )
    drive_type: DriveType = Field(
        ..., description="Antriebstyp"
    )

    # Eingabedaten Einbauraum
    max_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Maximaler Propellerdurchmesser [mm] (Einbauraum)"
    )
    tip_clearance_min_percent: float = Field(
        15.0, ge=0, le=50,
        description="Minimaler Tipabstand [% des Durchmessers]"
    )

    # Berechnungsergebnisse
    propeller_rpm: Optional[float] = Field(
        None, gt=0,
        description="Berechnete Propellerdrehzahl [U/min]"
    )
    power_at_propeller_hp: Optional[float] = Field(
        None, gt=0,
        description="Leistung am Propeller [PS]"
    )
    recommended_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Empfohlener Durchmesser [mm]"
    )
    recommended_pitch_mm: Optional[float] = Field(
        None, gt=0,
        description="Empfohlene Steigung [mm]"
    )
    recommended_blade_count: Optional[int] = Field(
        None, ge=2, le=5,
        description="Empfohlene Blattanzahl"
    )
    recommended_bar: Optional[float] = Field(
        None, gt=0, le=1.5,
        description="Empfohlenes BAR"
    )
    estimated_slip_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Geschätzter Slip [%]"
    )
    estimated_efficiency: Optional[float] = Field(
        None, ge=0, le=1.0,
        description="Geschätzter Propellerwirkungsgrad η"
    )

    # Empfehlungen
    recommended_propellers: list[str] = Field(
        default_factory=list,
        description="Empfohlene Propellermodelle"
    )
    notes: list[str] = Field(
        default_factory=list,
        description="Hinweise zur Dimensionierung"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe der Berechnung"
    )
    calculation_method: str = Field(
        "simplified",
        description="Berechnungsmethode (simplified, bp_delta, cfd)"
    )
```

---

### ANHANG N — PropellerSlipAnalysis

```python
class PropellerSlipAnalysis(BaseModel):
    """
    Slip-Berechnung und -Bewertung für einen installierten Propeller.
    """
    model_config = {"from_attributes": True}

    # Eingabedaten
    propeller_pitch_inch: float = Field(
        ..., gt=0, description="Propeller-Pitch [Zoll]"
    )
    engine_rpm_measured: float = Field(
        ..., gt=0, description="Gemessene Motor-RPM bei Volllast"
    )
    engine_rpm_rated: float = Field(
        ..., gt=0, description="Motor-Nenndrehzahl (WOT RPM)"
    )
    gear_ratio: float = Field(
        ..., gt=0, description="Getriebe-Untersetzungsverhältnis"
    )
    boat_speed_kn: float = Field(
        ..., gt=0, description="GPS-Geschwindigkeit bei Volllast [kn]"
    )

    # Berechnungsergebnisse
    propeller_rpm: float = Field(
        ..., gt=0, description="Propellerdrehzahl [U/min]"
    )
    theoretical_speed_kn: float = Field(
        ..., gt=0, description="Theoretische Geschwindigkeit [kn]"
    )
    slip_percent: float = Field(
        ..., ge=0, le=100,
        description="Berechneter Slip [%]"
    )
    rpm_deviation_percent: float = Field(
        ..., description="RPM-Abweichung von Nenndrehzahl [%]"
    )

    # Bewertung
    slip_assessment: str = Field(
        ..., description="Bewertung des Slip-Werts"
    )
    rpm_assessment: str = Field(
        ..., description="Bewertung der RPM-Abweichung"
    )
    is_overpropped: bool = Field(
        ..., description="Motor overpropped? (RPM < Nenn −3 %)"
    )
    is_underpropped: bool = Field(
        ..., description="Motor underpropped? (RPM > Nenn +3 %)"
    )

    # Empfehlungen
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen zur Optimierung"
    )
    suggested_pitch_change_inch: Optional[float] = Field(
        None,
        description="Empfohlene Pitch-Änderung [Zoll] (positiv = erhöhen)"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

---

### ANHANG O — CavitationAssessment

```python
class CavitationAssessment(BaseModel):
    """
    Bewertung des Kavitationsrisikos und identifizierter Kavitationsschäden.
    """
    model_config = {"from_attributes": True}

    propeller_id: str = Field(..., description="Propeller-Referenz-ID")
    assessment_date: str = Field(..., description="Bewertungsdatum (ISO 8601)")

    # Kavitationstyp
    cavitation_types: list[CavitationType] = Field(
        default_factory=list,
        description="Identifizierte Kavitationstypen"
    )
    primary_cavitation_type: CavitationType = Field(
        CavitationType.NONE,
        description="Hauptkavitationstyp"
    )

    # Schweregrad
    severity: FailureSeverity = Field(
        FailureSeverity.INFO,
        description="Gesamtschwere"
    )
    erosion_depth_mm: Optional[float] = Field(
        None, ge=0,
        description="Maximale Erosionstiefe [mm]"
    )
    affected_area_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Betroffene Blattfläche [%]"
    )
    affected_blades: list[int] = Field(
        default_factory=list,
        description="Betroffene Blätter (Nummern)"
    )

    # Risikoberechnung (Keller-Kriterium)
    bar_minimum_required: Optional[float] = Field(
        None, gt=0,
        description="Mindest-BAR nach Keller-Kriterium"
    )
    bar_actual: Optional[float] = Field(
        None, gt=0,
        description="Tatsächliches BAR"
    )
    cavitation_risk: str = Field(
        "unknown",
        description="Kavitationsrisiko: low, medium, high, critical"
    )

    # Befunde und Empfehlungen
    findings: list[str] = Field(
        default_factory=list,
        description="Befunde (Deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (Deutsch)"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Reparaturkosten [EUR]"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
    data_sources: list[str] = Field(
        default_factory=list,
        description="Datenquellen"
    )
```

---

### ANHANG P — AnodeAssessment

```python
class AnodeAssessment(BaseModel):
    """
    Bewertung des Anodenschutzsystems am Propeller und der Wellenanlage.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    boat_id: Optional[str] = Field(None, description="Boot-ID")
    assessment_date: str = Field(..., description="Bewertungsdatum (ISO 8601)")

    # Anoden-Inventar
    shaft_anode_present: bool = Field(..., description="Wellenanode vorhanden?")
    shaft_anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Wellenanode Restkapazität [%]"
    )
    prop_anode_present: bool = Field(
        ..., description="Propeller-Anode vorhanden?"
    )
    prop_anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Propeller-Anode Restkapazität [%]"
    )
    saildrive_anode_present: Optional[bool] = Field(
        None, description="Saildrive-Anode vorhanden? (None = kein Saildrive)"
    )
    saildrive_anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Saildrive-Anode Restkapazität [%]"
    )
    hull_anode_count: int = Field(
        0, ge=0,
        description="Anzahl Rumpfanoden"
    )

    # Galvanische Isolation
    galvanic_isolator_present: bool = Field(
        ..., description="Galvanischer Isolator vorhanden?"
    )
    shore_power_connection: bool = Field(
        ..., description="Landstromanschluss vorhanden?"
    )
    stray_current_risk: str = Field(
        "unknown",
        description="Fehlstrom-Risiko: low, medium, high, unknown"
    )

    # Bewertung
    overall_protection_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtschutz-Bewertung (0–100)"
    )
    protection_adequate: bool = Field(
        ..., description="Anodenschutz ausreichend?"
    )

    # Befunde und Empfehlungen
    findings: list[str] = Field(
        default_factory=list,
        description="Befunde (Deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (Deutsch)"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Kosten für Anodenwechsel [EUR]"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

---

### ANHANG Q — PropellerMaintenanceSchedule

```python
class MaintenanceAction(BaseModel):
    """Einzelne Wartungsmaßnahme."""
    model_config = {"from_attributes": True}

    action_id: str = Field(..., description="Maßnahmen-ID")
    description_de: str = Field(..., description="Beschreibung (Deutsch)")
    interval_months: int = Field(
        ..., gt=0, description="Intervall [Monate]"
    )
    interval_hours: Optional[int] = Field(
        None, gt=0, description="Intervall [Betriebsstunden]"
    )
    estimated_duration_hours: float = Field(
        ..., gt=0, description="Geschätzte Dauer [h]"
    )
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Kosten [EUR]"
    )
    requires_haul_out: bool = Field(
        ..., description="Erfordert Slip/Kran?"
    )
    diy_possible: bool = Field(
        ..., description="Selbst durchführbar?"
    )
    priority: FailureSeverity = Field(
        ..., description="Priorität"
    )
    last_performed: Optional[str] = Field(
        None, description="Zuletzt durchgeführt (ISO 8601)"
    )
    next_due: Optional[str] = Field(
        None, description="Nächster Termin (ISO 8601)"
    )


class PropellerMaintenanceSchedule(BaseModel):
    """
    Wartungsplan für einen Propeller und die zugehörige Wellenanlage.
    """
    model_config = {"from_attributes": True}

    propeller_id: str = Field(..., description="Propeller-Referenz-ID")
    propeller_type: PropellerType = Field(
        ..., description="Propellertyp"
    )
    propeller_age_years: Optional[float] = Field(
        None, ge=0,
        description="Alter des Propellers [Jahre]"
    )
    operating_hours: Optional[float] = Field(
        None, ge=0,
        description="Betriebsstunden (Motor)"
    )

    # Wartungsmaßnahmen
    actions: list[MaintenanceAction] = Field(
        default_factory=list,
        description="Wartungsmaßnahmen"
    )

    # Zusammenfassung
    total_annual_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte jährliche Wartungskosten [EUR]"
    )
    next_action_due: Optional[str] = Field(
        None, description="Nächste fällige Maßnahme"
    )
    overdue_actions: list[str] = Field(
        default_factory=list,
        description="Überfällige Maßnahmen"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
```

---

### ANHANG R — PropellerAnalysis (Orchestrierungs-Modell)

```python
class PropellerAnalysis(BaseModel):
    """
    Orchestrierungs-Modell für die Gesamtanalyse eines Marine-Propellers.
    Kombiniert alle Teilanalysen zu einem Gesamtergebnis.
    """
    model_config = {"from_attributes": True}

    analysis_id: str = Field(..., description="Analyse-ID")
    propeller_id: str = Field(..., description="Propeller-ID")
    boat_id: Optional[str] = Field(None, description="Boot-ID")
    analysis_date: str = Field(..., description="Analysedatum (ISO 8601)")
    analysis_level: str = Field(
        ..., description="Analyselevel: quick (Level 1) oder professional (Level 2)"
    )

    # Teilanalysen
    propeller_spec: Optional[PropellerSpec] = Field(
        None, description="Propellerspezifikation"
    )
    condition_assessment: Optional[PropellerConditionAssessment] = Field(
        None, description="Zustandsbewertung"
    )
    dimensioning: Optional[PropellerDimensioning] = Field(
        None, description="Dimensionierungsberechnung"
    )
    slip_analysis: Optional[PropellerSlipAnalysis] = Field(
        None, description="Slip-Analyse"
    )
    cavitation_assessment: Optional[CavitationAssessment] = Field(
        None, description="Kavitations-Bewertung"
    )
    anode_assessment: Optional[AnodeAssessment] = Field(
        None, description="Anodenschutz-Bewertung"
    )
    maintenance_schedule: Optional[PropellerMaintenanceSchedule] = Field(
        None, description="Wartungsplan"
    )

    # Gesamtergebnis
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Propeller (0–100)"
    )
    overall_condition: PropellerCondition = Field(
        ..., description="Gesamtzustand"
    )

    # Gewichtete Teilbewertungen
    sub_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (z.B. {'condition': 85, 'dimensioning': 72})"
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
        description="Sofortige Kosten für notwendige Maßnahmen [EUR]"
    )
    estimated_annual_maintenance_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte jährliche Wartungskosten [EUR]"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Ersatzkosten bei Totalschaden [EUR]"
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
