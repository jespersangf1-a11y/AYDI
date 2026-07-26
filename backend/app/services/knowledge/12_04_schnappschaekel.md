---
title: "Schnappschäkel und Karabiner im Yachtbau"
kategorie: "12 Schäkel, Wirbel und Verbinder"
unterkategorie: "04 Schnappschäkel und Karabiner"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen, CE-Zertifikate"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - schnappschäkel
  - snap_shackle
  - karabiner
  - carabiner
  - trigger_schäkel
  - spinnaker_schäkel
  - tylaska
  - wichard
  - harken
  - ronstan
  - quick_release
  - sicherheitsleine
  - safety_tether
  - jackline
  - laufendes_gut
  - deck_hardware
  - rigg
  - beschläge
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 12.04 — Schnappschäkel und Karabiner im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 12.04** — Kategorie 12: Schäkel, Wirbel und Verbinder
> **Confidence-Quelle:** measured (Hersteller-TDS, CE-Prüfzeugnisse), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#5-produktlinien-und-hersteller)
5. [Anwendungen](#6-anwendungen)
6. [Sicherheitsaspekte](#7-sicherheitsaspekte)
7. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
8. [Troubleshooting-Entscheidungsbaum](#9-troubleshooting-entscheidungsbaum)
9. [FAQ — Häufige Fragen](#10-faq--häufige-fragen)
10. [Glossar](#11-glossar)
11. [Schnell-Referenz](#12-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
14. [ANHANG C — Normen und Standards](#anhang-c--normen-und-standards)
15. [ANHANG D — Lasttabellen](#anhang-d--lasttabellen)
16. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
17. [ANHANG F — Wartungsintervalle](#anhang-f--wartungsintervalle)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — Bezugsquellen](#anhang-h--bezugsquellen)
20. [ANHANG I — Herstellervergleich Detailtabellen](#anhang-i--herstellervergleich-detailtabellen)
21. [ANHANG J — Schnappschäkel-Auswahl-Algorithmus](#anhang-j--schnappschäkel-auswahl-algorithmus)
22. [ANHANG K — Prüfprotokolle](#anhang-k--prüfprotokolle)
23. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
24. [ANHANG M — Korrosionsschutz und Pflege](#anhang-m--korrosionsschutz-und-pflege)
25. [ANHANG N — Retrofit-Leitfaden](#anhang-n--retrofit-leitfaden)
26. [ANHANG O — Regatta-Spezifikationen](#anhang-o--regatta-spezifikationen)
27. [ANHANG P — Superyacht-Sonderlösungen](#anhang-p--superyacht-sonderlösungen)
28. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
29. [ANHANG R — Checklisten](#anhang-r--checklisten)

---

## 1. Einführung und Übersicht

### 1.1 Was sind Schnappschäkel und Karabiner?

Schnappschäkel (englisch: snap shackles) und Karabiner (englisch: carabiners) sind schnelllösbare Verbindungselemente im Rigg- und Deckssystem von Yachten. Im Unterschied zu konventionellen Schäkeln, deren Bolzen geschraubt oder gesteckt wird, besitzen Schnappschäkel einen federbelasteten Auslösemechanismus (Trigger), der ein Öffnen und Schließen mit einer Hand und unter Sekundenbruchteilen ermöglicht.

Diese Eigenschaft macht Schnappschäkel unverzichtbar für alle Anwendungen, bei denen:

- **Schnelles Lösen unter Last** gefordert ist (Spinnaker-Bergen, Notfall-Slippage)
- **Einhändige Bedienung** notwendig ist (Arbeiten am Vorschiff, Sicherheitsleinen)
- **Häufiges An- und Abschlagen** erfolgt (Fallen wechseln, Segel tauschen)
- **Schnelligkeit** über maximale Bruchlast geht (Regattaeinsatz)

Ein Schnappschäkel besteht aus vier Grundelementen:

- **Körper (Body)**: Der Hauptrahmen, der die Last zwischen Auge und Bügel überträgt
- **Bügel (Shackle Bow)**: Der bewegliche Teil, der durch den Trigger geöffnet und durch die Feder geschlossen wird
- **Auslösemechanismus (Trigger)**: Hebel, Kolben oder Druckknopf zum Öffnen
- **Feder (Spring)**: Hält den Bügel im geschlossenen Zustand unter Spannung

### 1.2 Warum Schnappschäkel existieren — Funktionale Notwendigkeit

Im traditionellen Segelbetrieb wurden alle Verbindungen mit geschraubten D-Schäkeln oder Bügelschäkeln hergestellt. Das Lösen eines geschraubten Schäkels erfordert:

- Beide Hände (eine hält den Bügel, die andere dreht den Bolzen)
- Ein Werkzeug (Schäkelöffner, Zange oder Marlspieker)
- Zeit (15–60 Sekunden je nach Zustand und Korrosion)
- Vollständige Entlastung der Verbindung

Im modernen Segelsport gibt es jedoch zahlreiche Situationen, in denen diese Voraussetzungen nicht gegeben sind:

**Spinnaker-Bergen bei auffrischendem Wind:**
Der Spinnaker muss in weniger als 10 Sekunden vom Fall gelöst werden. Der Vorschiffs-Crewmember arbeitet auf einem schaukelnden, nassen Deck, hält sich mit einer Hand fest und muss mit der anderen das Fall lösen. Ein geschraubter Schäkel wäre hier nicht nur langsam, sondern lebensgefährlich.

**Sicherheitsleine (Safety Tether):**
Wenn ein Crewmitglied über Bord geht oder eine Notsituation das sofortige Lösen der Sicherheitsleine erfordert, kann ein geschraubter Schäkel tödlich sein. ISO 12401 schreibt vor, dass Sicherheitsleinen innerhalb von 5 Sekunden mit einer Hand lösbar sein müssen.

**Regattabetrieb:**
Beim Spinnaker-Set oder -Wechsel zählt jede Sekunde. Professionelle Crews führen Sets in unter 15 Sekunden durch — nur möglich mit Schnappschäkeln an allen relevanten Verbindungspunkten.

### 1.3 Abgrenzung: Schnappschäkel vs. Karabiner

Obwohl beide Typen schnelllösbar sind, unterscheiden sie sich fundamental:

| Eigenschaft | Schnappschäkel | Karabiner |
|-------------|----------------|-----------|
| Primärfunktion | Verbindung unter Last lösen | Verbindung herstellen und sichern |
| Öffnungsrichtung | Bügel öffnet nach außen/unten | Gate öffnet nach innen |
| Lastrichtung | Axial (Auge → Bügel) | Axial (Längsachse) |
| Bedienung unter Last | Ja (Hauptzweck) | Bedingt (je nach Typ) |
| Typische Anwendung | Fallen, Spinnaker, Sheets | Sicherheitsleinen, Jacklines, Lazy Jacks |
| Sicherheitsmechanismus | Optional (Sicherungsstift) | Schraubverschluss oder Auto-Lock |
| Preisbereich (EUR) | 15–250 | 8–80 |

### 1.4 Bedeutung im Yacht-System

Auf einer modernen 12-Meter-Fahrtenyacht befinden sich typischerweise 8–20 Schnappschäkel und 4–10 Karabiner. Auf einer Regattayacht gleicher Größe können es 15–40 Schnappschäkel und 6–15 Karabiner sein.

| Bootsklasse | Schnappschäkel | Karabiner | Kostenbereich (EUR) |
|-------------|---------------|-----------|---------------------|
| Jolle (4–8m) | 2–6 | 0–2 | 30–200 |
| Fahrtensegler (8–14m) | 8–20 | 4–10 | 200–1.200 |
| Performance Cruiser (10–16m) | 12–25 | 6–12 | 400–2.000 |
| Blauwasseryacht (12–18m) | 10–18 | 8–16 | 350–1.800 |
| Regattayacht (8–20m) | 15–40 | 6–15 | 600–5.000 |
| Motoryacht (8–25m) | 2–8 | 2–6 | 80–500 |
| Superyacht (18m+) | 20–60+ | 10–30 | 1.500–15.000+ |

### 1.5 Kritische Sicherheitsrelevanz

Schnappschäkel sind in vielen Anwendungen sicherheitskritisch. Ein unbeabsichtigtes Öffnen unter Last kann zu:

- **Personenschäden**: Peitschende Fallen, herabfallende Beschläge, unkontrolliert schlagende Segel
- **Materialschäden**: Riggversagen durch schlagartige Lastumverteilung, Segelverlust
- **Situationsverschlechterung**: Verlust der Segelkontrolle bei schwerem Wetter
- **Lebensgefahr**: Versagen der Sicherheitsleine bei Überbordgehen

Deshalb muss die Auswahl, Installation und Wartung von Schnappschäkeln mit höchster Sorgfalt erfolgen.

---

## 2. Grundlagen und Theorie

### 2.1 Auslösemechanismen im Detail

Der Auslösemechanismus (Trigger) ist das definierende Merkmal eines Schnappschäkels. Er bestimmt die Bedienbarkeit, Sicherheit und Zuverlässigkeit des gesamten Beschlags.

#### 2.1.1 Trigger-Hebel (Lever Trigger)

Der klassische Schnappschäkel-Auslösemechanismus. Ein beweglicher Hebel am Körper des Schäkels wird gegen die Federspannung gedrückt und gibt den Bügel frei.

**Funktionsprinzip:**
1. Im geschlossenen Zustand hält die Feder den Bügel gegen einen Anschlag im Körper
2. Der Trigger-Hebel ist mit dem Bügel-Verriegelungsmechanismus verbunden
3. Drücken des Hebels zieht den Verriegelungsstift zurück
4. Die im Bügel gespeicherte Energie (durch die Last) drückt den Bügel auf
5. Der Bügel schwingt um seinen Drehpunkt nach außen

**Vorteile:**
- Intuitive Bedienung
- Mit Handschuhen bedienbar
- Große Kontaktfläche für den Finger
- Bewährtes Design seit Jahrzehnten

**Nachteile:**
- Kann durch Leinen oder Segel unbeabsichtigt ausgelöst werden
- Hebel kann bei Stoss oder Schlag brechen
- Verschmutzungsempfindlich (Salzkristalle blockieren Mechanismus)

#### 2.1.2 Plunger-Pin (Kolbenbolzen)

Ein federbelasteter Kolbenbolzen wird axial gegen die Federkraft gedrückt und gibt den Bügel frei.

**Funktionsprinzip:**
1. Der Kolbenbolzen ragt im geschlossenen Zustand in eine Bohrung im Bügel
2. Drücken des Kolbens gegen die Feder zieht den Bolzen aus der Bügelbohrung
3. Der Bügel wird frei und öffnet sich durch die Lastspannung

**Vorteile:**
- Kompaktere Bauform als Trigger-Hebel
- Geringere Gefahr des unbeabsichtigten Öffnens
- Besser gegen Verschmutzung geschützt (kleinere Öffnungen)

**Nachteile:**
- Schwieriger mit Handschuhen zu bedienen
- Kleinere Kontaktfläche
- Höhere Federkräfte bei größeren Modellen

#### 2.1.3 Triplebar-Trigger (Wichard-System)

Das von Wichard patentierte Triplebar-System verwendet drei ineinandergreifende Hebelelemente, die ein unbeabsichtigtes Öffnen nahezu ausschließen.

**Funktionsprinzip:**
1. Drei separate Hebelsegmente müssen in der richtigen Reihenfolge betätigt werden
2. Erst wenn alle drei Segmente ausgerichtet sind, wird der Bügel freigegeben
3. Die Wahrscheinlichkeit einer unbeabsichtigten Auslösung durch eine Leine oder einen Stoß ist extrem gering

**Vorteile:**
- Höchste Sicherheit gegen unbeabsichtigtes Öffnen
- Bewusste Auslösung erforderlich
- Auch unter hoher Last bedienbar

**Nachteile:**
- Komplexerer Mechanismus
- Teurer als Standard-Trigger
- Lernkurve bei Erstanwendung

#### 2.1.4 Karabiner-Gate (Federtor)

Bei Karabinern wird ein federbelastetes Tor (Gate) gegen die Feder eingedrückt, um das Einführen einer Leine oder eines Auges zu ermöglichen.

**Funktionsprinzip:**
1. Das Gate ist an einem Ende drehbar gelagert
2. Eine Feder drückt das Gate in die geschlossene Position
3. Eindrücken des Gates gegen die Feder öffnet den Karabiner
4. Nach Einführen des Verbindungselements schließt die Feder das Gate automatisch

**Varianten:**
- **Straight Gate**: Gerades Gate, einfachste Bauform
- **Bent Gate**: Gebogenes Gate, erleichtert das Einhängen
- **Wire Gate**: Draht-Gate, leichter, weniger vereisungsanfällig
- **Auto-Lock Gate**: Automatisch verriegelndes Gate (Twist-Lock, Tri-Lock)
- **Screw Gate**: Schraubverschluss über dem Gate

### 2.2 Lastverhalten unter dynamischen Bedingungen

Schnappschäkel unterliegen im Yachteinsatz extremen dynamischen Belastungen, die sich fundamental von statischen Testbedingungen unterscheiden.

#### 2.2.1 Statische vs. dynamische Belastung

**Statische Bruchlast (Breaking Load / BL):**
Die maximale Last, bei der der Schäkel unter langsam steigender, gleichmäßiger Belastung versagt. Dies ist der Wert, der in Herstellerdatenblättern angegeben wird.

**Sichere Arbeitslast (Safe Working Load / SWL):**
Die maximale Last für den regulären Betrieb. Typischerweise:
- SWL = BL / 4 (Standardfaktor für marine Beschläge)
- SWL = BL / 5 (bei sicherheitskritischen Anwendungen wie Safety Tether)
- SWL = BL / 3 (nur bei Regattaeinsatz mit häufiger Inspektion)

**Dynamische Belastung im Yachteinsatz:**
Im realen Einsatz wirken Stoßlasten (Shock Loads), die ein Vielfaches der statischen Last betragen können:

| Belastungssituation | Lastfaktor (× statische Last) |
|---------------------|-------------------------------|
| Ruhiges Segeln, gleichmäßiger Wind | 1,0–1,5 |
| Böen in Küstengewässern | 1,5–2,5 |
| Spinnaker-Füllung nach Kollaps | 2,0–4,0 |
| Segel schlägt im Sturm | 3,0–6,0 |
| Plötzliches Stoppen einer laufenden Leine | 4,0–8,0 |
| Fall einer Person in Safety Tether | 5,0–12,0 |
| Ankerkette bei Sturm mit kurzer Kette | 3,0–10,0 |

#### 2.2.2 Ermüdungsbelastung (Fatigue)

Schnappschäkel unterliegen zyklischer Belastung. Die Lebensdauer wird nicht nur durch die maximale Last, sondern durch die Anzahl der Lastzyklen bestimmt.

**Wöhler-Kurve für marine Edelstahlbeschläge (316L, geschmiedet):**

| Lastamplitude (% BL) | Zyklen bis Versagen |
|-----------------------|--------------------|
| 80% | ~1.000 |
| 60% | ~10.000 |
| 40% | ~100.000 |
| 25% | ~1.000.000 |
| 15% | ~10.000.000 (Dauerfestigkeit) |

**Konsequenz für die Praxis:**
Ein Spinnaker-Fall-Schnappschäkel auf einer aktiven Regattayacht erfährt typischerweise 200–500 Lastzyklen pro Saison (Sets, Bergen, Böen). Bei einer Lastamplitude von 30–40% BL ergibt sich eine theoretische Lebensdauer von 200–500 Saisons — sofern keine Korrosion, keine Stoßlasten über 60% BL und keine Materialfehler vorliegen.

In der Praxis begrenzen jedoch Korrosion, Verschmutzung und mechanischer Verschleiß die Lebensdauer auf 5–15 Jahre bei normaler Nutzung und 2–5 Jahre bei intensivem Regattaeinsatz.

#### 2.2.3 Lastverteilung im Schnappschäkel

Die Lastverteilung innerhalb eines Schnappschäkels ist nicht gleichmäßig:

**Kritische Belastungspunkte:**
1. **Bügel-Drehpunkt (Pivot Point)**: Höchste Belastung, da hier die gesamte Last als Scherkraft wirkt
2. **Verriegelungspunkt (Latch Point)**: Zweithöchste Belastung, hält den Bügel geschlossen
3. **Auge (Eye)**: Zugbelastung, verteilt sich auf die Materialquerschnittsfläche
4. **Triggermechanismus**: Geringe direkte Last, aber mechanische Beanspruchung durch Betätigung

**Spannungsspitzen bei Fehlbelastung:**
- Querlast auf den Bügel: Spannungskonzentration am Drehpunkt × 2–3
- Seitliche Last auf das Auge: Biegemoment im Schaftbereich
- Torsion durch verdrehte Leine: Ungleichmäßige Lastverteilung

### 2.3 Unbeabsichtigtes Öffnen — Ursachen und Prävention

Das unbeabsichtigte Öffnen (Accidental Opening) ist das zentrale Sicherheitsproblem bei Schnappschäkeln.

#### 2.3.1 Ursachen für unbeabsichtigtes Öffnen

**Mechanische Auslösung durch Leinen:**
Lose Leinen, Sheets oder Fallen können sich um den Trigger wickeln und diesen bei Zugbelastung auslösen. Dies ist die häufigste Ursache für unbeabsichtigtes Öffnen.

**Anschlagen gegen Beschläge:**
Bei Seegang kann der Schnappschäkel gegen Winschen, Klampen oder andere Beschläge schlagen. Der Stoßimpuls kann den Trigger auslösen, besonders bei verschlissenen Federn.

**Vibration:**
Hochfrequente Vibrationen (Motor, Rigg-Schwingungen) können bei ermüdeten Federn den Trigger sukzessive lösen.

**Federermüdung:**
Die Trigger-Feder verliert über die Zeit ihre Spannung. Ein neuer Schnappschäkel erfordert typischerweise 2–4 kg Fingerkraft zum Öffnen. Nach 3–5 Jahren kann diese Kraft auf 0,5–1 kg sinken — unzureichend, um unbeabsichtigtes Öffnen zu verhindern.

**Korrosion des Mechanismus:**
Salzkristalle und Korrosion können den Mechanismus blockieren oder die Feder schwächen. Paradoxerweise kann ein korrodierter Schnappschäkel sowohl schwergängig als auch unsicher sein — der Trigger bewegt sich nicht mehr gleichmäßig und kann in einer Zwischenposition verharren.

#### 2.3.2 Präventionsmaßnahmen

**Sicherungsstift (Safety Pin):**
Ein kleiner Stift oder Splint, der durch den Trigger gesteckt wird und dessen Betätigung verhindert. Standard bei Fallen-Schäkeln an Masten.

**Whipping/Tape:**
Der Trigger wird mit einem dünnen Bändsel oder Segelmacher-Tape umwickelt. Bietet Schutz gegen unbeabsichtigtes Auslösen durch Leinen, kann aber im Notfall schnell entfernt werden.

**Korrekte Ausrichtung:**
Der Schnappschäkel wird so montiert, dass der Trigger von Leinen und Beschlägen weg zeigt. Grundregel: Trigger nach oben oder vom Segel weg.

**Regelmäßige Wartung:**
- Süßwasserspülung nach jedem Segeltag
- Ölen des Mechanismus alle 4–6 Wochen (Teflon- oder Silikonöl)
- Prüfung der Federspannung saisonal
- Austausch bei nachlassender Federspannung

**Einsatz von Anti-Snag-Designs:**
Moderne Schnappschäkel (z.B. Tylaska) haben versenkte Trigger, die von Leinen nicht erreicht werden können.

### 2.4 Materialien

#### 2.4.1 Edelstahl 316L (Marine-Standard)

- **Zusammensetzung**: Fe-Cr18-Ni10-Mo2, niedrig Kohlenstoff (L = Low Carbon)
- **Bruchfestigkeit**: 500–700 MPa
- **Streckgrenze**: 200–300 MPa
- **Korrosionsbeständigkeit**: Ausgezeichnet in Salzwasser, PREN ≥ 24
- **Magnetisch**: Nein (austenitisch)
- **Verarbeitung**: Geschmiedet (höchste Festigkeit), gegossen, CNC-gefräst

**Wichtig für AYDI-Analyse:**
Gegossene 316L-Schäkel haben 20–40% geringere Festigkeit als geschmiedete. Die Angabe „Edelstahl" ohne Spezifikation der Legierung und Herstellungsart ist unzureichend für eine Sicherheitsbewertung.

#### 2.4.2 Titan (Grade 5 / Ti-6Al-4V)

- **Zusammensetzung**: Ti-90, Al-6, V-4
- **Bruchfestigkeit**: 900–1.100 MPa
- **Streckgrenze**: 800–900 MPa
- **Korrosionsbeständigkeit**: Hervorragend, PREN > 40
- **Gewicht**: 56% von Edelstahl bei höherer Festigkeit
- **Preis**: 5–10× Edelstahl

Wird bei High-Performance-Regattayachten und Superyachten eingesetzt. Tylaska bietet die umfangreichste Titan-Produktlinie.

#### 2.4.3 Hochfester Edelstahl (17-4 PH, Custom 455)

- **Bruchfestigkeit**: 1.000–1.300 MPa
- **Streckgrenze**: 900–1.100 MPa
- **Korrosionsbeständigkeit**: Gut, aber geringer als 316L
- **Magnetisch**: Ja (martensitisch/ausgehärtet)

Wird für Hochlast-Trigger und Bolzen verwendet, wo maximale Festigkeit bei kleinem Querschnitt erforderlich ist.

#### 2.4.4 Bronze (Phosphorbronze, Aluminiumbronze)

- **Bruchfestigkeit**: 400–700 MPa (je nach Legierung)
- **Korrosionsbeständigkeit**: Sehr gut in Salzwasser
- **Einsatz**: Historische Beschläge, einige Spezialanwendungen
- **Nachteil**: Schwerer als Edelstahl, aufwendigere Fertigung

### 2.5 Fertigungsverfahren und Qualitätsmerkmale

#### 2.5.1 Schmieden (Forging)

Höchstes Qualitätsniveau. Das Metall wird unter hohem Druck in eine Form gepresst. Die Kornstruktur folgt der Bauteilgeometrie, was maximale Festigkeit ergibt.

**Erkennungsmerkmale:**
- Gratlinien (Trennlinien der Schmiedeform) sichtbar
- Gleichmäßige Oberfläche
- Hohe Maßgenauigkeit
- Keine Lunker oder Poren

**Hersteller mit geschmiedeten Schnappschäkeln:**
Wichard (alle Modelle), Tylaska (alle Modelle), Harken (Hochlast-Modelle)

#### 2.5.2 Feinguss (Investment Casting)

Gutes Qualitätsniveau. Wachsmodell wird mit Keramik ummantelt, ausgeschmolzen und mit Metall gefüllt.

**Erkennungsmerkmale:**
- Glatte Oberfläche (keine Gratlinien)
- Komplexere Geometrien möglich
- Potenzielle innere Lunker (nur durch Röntgen erkennbar)

**Hersteller mit gegossenen Schnappschäkeln:**
Ronstan (Standard-Modelle), diverse asiatische Hersteller

#### 2.5.3 CNC-Bearbeitung (Machined)

Aus Vollmaterial gefräst. Höchste Maßgenauigkeit, aber Kornstruktur wird durchschnitten.

**Erkennungsmerkmale:**
- Frässpuren (bei günstigen Modellen sichtbar)
- Scharfe Kanten (müssen verrundet sein)
- Gleichmäßige Wandstärke

**Hersteller mit CNC-Schnappschäkeln:**
Tylaska (Titan-Modelle), diverse Spezialanbieter

### 2.6 Normen und Prüfverfahren

#### 2.6.1 Relevante Normen

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 12401:2009 | Deck safety harness and safety line | Sicherheitsleinen-Karabiner |
| ISO 9227 | Salt spray test | Korrosionsbeständigkeit |
| EN 362:2004 | Connectors for PPE against falls | Karabiner für Sicherheitsausrüstung |
| EN 12275 | Mountaineering connectors | Basis für marine Karabiner |
| ISAF OSR | Offshore Special Regulations | Regatta-Sicherheitsanforderungen |
| DNV-GL Rules | Classification society rules | Superyacht-Zertifizierung |

#### 2.6.2 Prüfverfahren

**Bruchlast-Prüfung (Breaking Load Test):**
Langsam steigende axiale Zugbelastung bis zum Versagen. Prüfgeschwindigkeit: 10–50 mm/min. Ergebnis: Bruchlast in kN.

**Proof-Load-Prüfung:**
Jeder Schäkel wird mit 50% der Bruchlast belastet und auf plastische Verformung geprüft. Bei Verformung: Ausschuss.

**Trigger-Funktionsprüfung:**
- Öffnung unter Last: Trigger muss bei SWL betätigbar sein
- Öffnungskraft: 15–50 N (handhabbar mit einer Hand)
- Schließkraft der Feder: Muss Gate/Bügel sicher schließen
- Zyklentest: 10.000 Öffnungs-/Schließzyklen ohne Funktionsverlust

**Salzsprühtest (Salt Spray Test nach ISO 9227):**
- 500 Stunden: Minimale Anforderung für marine Beschläge
- 1.000 Stunden: Hochwertige Beschläge
- 2.000+ Stunden: Premium-Qualität (Tylaska, Wichard geschmiedet)

---

## 3. Typenübersicht

### 3.1 Standard-Schnappschäkel (Standard Snap Shackle)

Der Grundtyp aller Schnappschäkel. Besteht aus einem festen Auge (Eye) am oberen Ende und einem federbelasteten Bügel am unteren Ende mit Trigger-Auslösung.

**Konstruktionsmerkmale:**
- Festes, gestanztes oder geschmiedetes Auge
- Bügel mit Drehpunkt auf einer Seite
- Trigger-Hebel oder Plunger-Pin
- Interne Spiralfeder oder Blattfeder

**Typische Abmessungen und Lasten:**

| Nenngröße | Gesamtlänge (mm) | Bügelweite (mm) | BL (kN) | SWL (kN) | Gewicht (g) |
|-----------|-------------------|-----------------|---------|----------|-------------|
| Mini (30mm) | 50–55 | 10–12 | 4–6 | 1,0–1,5 | 15–25 |
| Klein (50mm) | 70–80 | 14–16 | 8–12 | 2,0–3,0 | 40–60 |
| Mittel (70mm) | 90–100 | 18–22 | 15–25 | 3,8–6,3 | 80–120 |
| Groß (90mm) | 110–130 | 22–28 | 25–40 | 6,3–10,0 | 130–200 |
| XL (120mm) | 140–160 | 28–35 | 40–70 | 10,0–17,5 | 200–350 |

**Anwendungen:**
- Fallen (Großsegel, Genua, Fock)
- Spinnaker-Fall (oberes Ende)
- Leichte Befestigungspunkte
- Beiboot-Hebegeschirr

**Vorteile:**
- Einfacher, bewährter Mechanismus
- Günstigster Schnappschäkeltyp
- Breite Verfügbarkeit in allen Größen

**Nachteile:**
- Festes Auge kann Torsion in die Verbindung einleiten
- Keine Drehbewegung möglich
- Trigger teilweise exponiert

### 3.2 Wirbel-Schnappschäkel (Swivel Snap Shackle)

Ein Schnappschäkel mit integriertem Wirbel (Swivel) zwischen Auge und Körper. Der Wirbel ermöglicht eine 360°-Drehung und verhindert Torsion in der Verbindungskette.

**Konstruktionsmerkmale:**
- Kugelgelagerter oder gleitgelagerter Wirbel
- Wirbel zwischen Auge und Schäkelkörper
- Gleicher Trigger-Mechanismus wie Standard-Schnappschäkel
- Wirbel-Lastübertragung als zusätzliches potenzielles Versagenselement

**Typische Abmessungen und Lasten:**

| Nenngröße | Gesamtlänge (mm) | BL (kN) | SWL (kN) | Gewicht (g) |
|-----------|-------------------|---------|----------|-------------|
| Klein (50mm) | 85–95 | 6–10 | 1,5–2,5 | 50–75 |
| Mittel (70mm) | 105–120 | 12–22 | 3,0–5,5 | 100–150 |
| Groß (90mm) | 130–150 | 22–35 | 5,5–8,8 | 160–240 |
| XL (120mm) | 160–190 | 35–60 | 8,8–15,0 | 250–400 |

**Wichtig:** Die Bruchlast eines Wirbel-Schnappschäkels wird durch das schwächste Element bestimmt — Wirbel oder Schäkelkörper. Typischerweise ist der Wirbel der limitierende Faktor (10–20% geringere BL als der Schäkelkörper allein).

**Anwendungen:**
- Spinnaker-Fall (oberes Ende) — verhindert Verdrillung
- Ankerwirbel-Verbindung
- Trapezhaken-Verbindung
- Alle Anwendungen mit Rotationstendenz

### 3.3 Festaugen-Schnappschäkel (Fixed Eye Snap Shackle)

Ein Schnappschäkel mit besonders großem, verstärktem festem Auge, das für direkte Bolzenverbindung an Beschlägen ausgelegt ist.

**Konstruktionsmerkmale:**
- Übergroßes, gestanztes oder geschmiedetes Auge
- Auge mit Bohrung für Bolzen oder Stift
- Keine Drehbewegung möglich
- Maximale Lastübertragung durch direkte Bolzenverbindung

**Typische Abmessungen und Lasten:**

| Nenngröße | Gesamtlänge (mm) | Augenbohrung (mm) | BL (kN) | SWL (kN) |
|-----------|-------------------|--------------------|---------|----------|
| Klein | 65–75 | 6–8 | 10–15 | 2,5–3,8 |
| Mittel | 85–100 | 8–10 | 18–30 | 4,5–7,5 |
| Groß | 110–130 | 10–13 | 30–50 | 7,5–12,5 |
| XL | 140–170 | 13–16 | 50–80 | 12,5–20,0 |

**Anwendungen:**
- Mastbeschläge für Fallen
- Baum-Niederholer (Vang)
- Cunningham
- Direkte Montage an Augbolzen oder Beschlagplatten

### 3.4 Plunger-Pin-Schnappschäkel (Plunger Pin Snap Shackle)

Ein Schnappschäkel, bei dem der Auslösemechanismus ein federbelasteter Kolbenbolzen (Plunger Pin) ist statt eines Trigger-Hebels.

**Konstruktionsmerkmale:**
- Kolbenbolzen statt Trigger-Hebel
- Bolzen wird axial gegen die Feder gedrückt
- Kompaktere Bauform
- Geringere Anfälligkeit für unbeabsichtigtes Öffnen

**Typische Abmessungen und Lasten:**

| Nenngröße | Gesamtlänge (mm) | BL (kN) | SWL (kN) | Gewicht (g) |
|-----------|-------------------|---------|----------|-------------|
| Mini | 40–50 | 3–5 | 0,8–1,3 | 12–20 |
| Klein | 55–70 | 6–10 | 1,5–2,5 | 30–50 |
| Mittel | 75–90 | 10–18 | 2,5–4,5 | 60–100 |
| Groß | 95–120 | 18–30 | 4,5–7,5 | 100–170 |

**Anwendungen:**
- Spinnaker-Tack (Buganschluss)
- Leichte Fallen
- Segel-Cunningham
- Lazy Jacks
- Anwendungen, bei denen die Gefahr des unbeabsichtigten Öffnens besonders hoch ist

### 3.5 Trigger-Schnappschäkel (Trigger Release Snap Shackle)

Hochleistungs-Schnappschäkel mit speziellem Auslösemechanismus, der auch unter extrem hoher Last betätigt werden kann. Typisch für Regatta- und Superyacht-Einsatz.

**Konstruktionsmerkmale:**
- Mechanisch vorteilhafter Trigger-Mechanismus (Hebelübersetzung)
- Trigger-Kraft bleibt auch unter hoher Last moderat (< 40 N)
- Oft mit Anti-Snag-Design (versenkter Trigger)
- Premium-Materialien und -Verarbeitung

**Designprinzip:**
Bei konventionellen Schnappschäkeln steigt die erforderliche Trigger-Kraft mit der Last, da der Trigger gegen die Reibung im Verriegelungsmechanismus arbeiten muss. Bei Trigger-Release-Designs wird die Last durch eine spezielle Geometrie vom Trigger entkoppelt — die Auslösekraft bleibt unabhängig von der Schäkellast nahezu konstant.

**Typische Abmessungen und Lasten:**

| Nenngröße | Gesamtlänge (mm) | BL (kN) | SWL (kN) | Trigger-Kraft (N) |
|-----------|-------------------|---------|----------|--------------------|
| Klein | 70–85 | 12–18 | 3,0–4,5 | 15–25 |
| Mittel | 90–110 | 20–35 | 5,0–8,8 | 20–35 |
| Groß | 115–140 | 35–60 | 8,8–15,0 | 25–40 |
| XL | 145–180 | 60–100 | 15,0–25,0 | 30–45 |

**Hersteller:**
Tylaska (T-Serie), Wichard (Triplebar), Harken (Reflex)

**Anwendungen:**
- Spinnaker-Fall auf Regattayachten
- Asymmetric Spinnaker Tack
- Hochlast-Fallen auf Superyachten
- Alle Anwendungen, bei denen Lösen unter hoher Last erforderlich ist

### 3.6 Karabiner ohne Verriegelung (Non-Locking Carabiner)

Einfache Karabiner mit Federgate, ohne zusätzlichen Verriegelungsmechanismus.

**Konstruktionsmerkmale:**
- Aluminium oder Edelstahl
- Federbelastetes Gate
- Keine Verriegelung — Gate kann jederzeit geöffnet werden
- Leichte Bauform

**Typische Abmessungen und Lasten:**

| Material | Größe | BL Längsachse (kN) | BL Querachse (kN) | BL Gate offen (kN) | Gewicht (g) |
|----------|-------|---------------------|---------------------|---------------------|-------------|
| Aluminium | 60mm | 15–22 | 5–7 | 5–8 | 25–40 |
| Aluminium | 80mm | 22–30 | 7–10 | 8–12 | 40–60 |
| Edelstahl | 60mm | 25–35 | 8–12 | 10–15 | 50–80 |
| Edelstahl | 80mm | 35–50 | 12–18 | 15–22 | 80–130 |

**WARNUNG:** Non-Locking-Karabiner sind NICHT für sicherheitskritische Anwendungen (Safety Tether, Jackline) zugelassen. ISO 12401 schreibt für Sicherheitsleinen selbstverriegelnde Karabiner vor.

**Anwendungen:**
- Lazy Jacks
- Sonnensegel-Befestigung
- Werkzeugsicherung
- Provisorische Verbindungen
- Beiboot-Befestigung (nicht tragend)

### 3.7 Karabiner mit Verriegelung (Locking Carabiner)

Karabiner mit zusätzlichem Verriegelungsmechanismus, der das Gate gegen unbeabsichtigtes Öffnen sichert.

#### 3.7.1 Schraubkarabiner (Screw-Lock)

- Schraubhülse über dem Gate, die manuell zugedreht werden muss
- Sicherste Verriegelung, aber erfordert bewusste Handlung
- Kann sich durch Vibration lockern (Gegenmaßnahme: Tape)

#### 3.7.2 Twist-Lock-Karabiner (Auto-Lock)

- Federhülse, die automatisch verriegelt
- Zum Öffnen: Hülse drehen und Gate drücken
- Schneller als Schraubkarabiner
- Kann durch Vereisung oder Verschmutzung blockieren

#### 3.7.3 Tri-Lock-Karabiner

- Dreifach-Verriegelung: Hülse heben, drehen, Gate drücken
- Höchste Sicherheit gegen unbeabsichtigtes Öffnen
- Standard für ISO-12401-konforme Sicherheitsleinen

**Typische Abmessungen und Lasten (Edelstahl, Locking):**

| Verriegelung | Größe | BL (kN) | Gate-Open BL (kN) | Gewicht (g) |
|--------------|-------|---------|---------------------|-------------|
| Screw-Lock | 70mm | 30–45 | 10–15 | 90–140 |
| Screw-Lock | 90mm | 45–65 | 15–22 | 140–200 |
| Twist-Lock | 70mm | 28–42 | 10–14 | 95–145 |
| Twist-Lock | 90mm | 42–60 | 14–20 | 145–210 |
| Tri-Lock | 80mm | 35–50 | 12–18 | 120–170 |
| Tri-Lock | 100mm | 50–70 | 18–25 | 170–250 |

**Anwendungen:**
- Safety Tether / Sicherheitsleinen (ISO 12401)
- Jackline-Verbindung
- MOB-Ausrüstung (Mann über Bord)
- Persönliche Sicherheitsausrüstung
- Rettungsinsel-Befestigung (einige Typen)

### 3.8 Tylaska Schnappschäkel

Tylaska (USA, Rhode Island) ist der Maßstab für High-Performance-Schnappschäkel im Regatta- und Superyacht-Bereich. Die T-Serie kombiniert minimale Baugröße mit maximaler Bruchlast und einem patentierten Anti-Snag-Trigger.

**Designphilosophie:**
- Trigger-Kraft unabhängig von der Last (Load-Independent Trigger)
- Versenkter Trigger verhindert unbeabsichtigtes Öffnen durch Leinen
- Geschmiedeter 17-4 PH Edelstahl für Trigger-Komponenten
- 316L geschmiedeter Körper
- Austauschbare Federn und Trigger-Komponenten

**Besondere Merkmale:**
- Alle Modelle einzeln proof-load-getestet
- Seriennummer auf jedem Schäkel
- Lebenslange Garantie auf den Körper
- Ersatzteil-Service für alle Komponenten

**Modellübersicht:**

| Modell | BL (kN) | SWL (kN) | Länge (mm) | Gewicht (g) | Primäranwendung |
|--------|---------|----------|------------|-------------|-----------------|
| T5 | 5,3 | 1,3 | 57 | 28 | Leichte Fallen, Cunningham |
| T8 | 8,9 | 2,2 | 70 | 48 | Spinnaker-Tack, Fallen (Jollen, Sportboote) |
| T12 | 13,3 | 3,3 | 83 | 85 | Spinnaker-Fall, Fallen (Fahrtenyachten) |
| T20 | 22,2 | 5,6 | 102 | 142 | Hochlast-Fallen, Spinnaker (große Yachten) |
| T30 | 31,1 | 7,8 | 121 | 227 | Superyacht-Fallen, extreme Lasten |
| T50 | 53,4 | 13,4 | 152 | 454 | Superyacht-Spezialanwendungen |

### 3.9 Soft-Attachment-Schnappschäkel

Schnappschäkel, bei denen das obere Auge durch eine Soft-Verbindung (Dyneema-Schlaufe, Textil-Loop) ersetzt ist. Dies reduziert das Gewicht erheblich und ermöglicht eine flexible Befestigung.

**Konstruktionsmerkmale:**
- Schäkelkörper ohne festes Auge
- Bohrung oder Slot für Dyneema-Schlaufe
- Dyneema-Schlaufe (SK78 oder SK99) als Verbindungselement
- Gewichtsersparnis: 20–40% gegenüber Vollmetall

**Vorteile:**
- Deutlich leichter
- Flexiblere Montage
- Geringere Schwungmasse (weniger Verletzungsgefahr)
- Kein Metallkontakt mit Segel oder Beschlag

**Nachteile:**
- Dyneema altert (UV, Abrieb)
- Schlaufe muss regelmäßig geprüft und getauscht werden (alle 1–3 Saisons)
- Geringere Bruchlast als Vollmetall-Auge
- Nicht für Dauerlast geeignet

**Typische Abmessungen und Lasten:**

| Nenngröße | BL Schäkelkörper (kN) | BL mit Dyneema (kN) | Gewicht Komplett (g) |
|-----------|------------------------|----------------------|----------------------|
| Klein | 8–12 | 6–10 | 20–35 |
| Mittel | 15–25 | 12–20 | 40–70 |
| Groß | 25–40 | 20–35 | 70–120 |

**Anwendungen:**
- Regattayachten (Gewichtsoptimierung)
- Spinnaker-Ausrüstung
- Gennaker-Tack
- Alle Anwendungen, bei denen Gewicht kritisch ist

---

## 4. Produktlinien und Hersteller

### 4.1 Wichard (Frankreich)

Wichard ist der führende europäische Hersteller von geschmiedeten Edelstahl-Beschlägen für den Yachtbereich. Seit 1919 in Thiers (Auvergne) ansässig, produziert Wichard ausschließlich in Frankreich.

**Markenphilosophie:**
- Alle Produkte geschmiedet (kein Guss)
- Ausschließlich 316L Edelstahl (HR = Haute Résistance = hochfest)
- Patentiertes Triplebar-Sicherheitssystem
- Lebenslange Garantie bei bestimmungsgemäßem Einsatz

#### 4.1.1 Wichard Schnappschäkel

**Wichard Standard Snap Shackle (Série 2670/2671/2672):**

| Artikelnr. | Typ | BL (daN) | Länge (mm) | Bolzen (mm) | Gewicht (g) | Preis (EUR) |
|------------|-----|----------|------------|-------------|-------------|-------------|
| 2670 | Standard, festes Auge | 500 | 52 | 5 | 22 | 18–25 |
| 2671 | Standard, festes Auge | 800 | 66 | 6 | 42 | 22–30 |
| 2672 | Standard, festes Auge | 1.200 | 78 | 8 | 72 | 28–38 |
| 2673 | Standard, festes Auge | 2.000 | 96 | 10 | 135 | 42–55 |
| 2674 | Standard, festes Auge | 3.000 | 116 | 12 | 220 | 65–85 |

**Wichard Wirbel-Schnappschäkel (Série 2473/2474/2475):**

| Artikelnr. | Typ | BL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|-----|----------|------------|-------------|-------------|
| 2473 | Swivel Snap | 500 | 68 | 32 | 28–38 |
| 2474 | Swivel Snap | 800 | 82 | 58 | 35–48 |
| 2475 | Swivel Snap | 1.200 | 98 | 98 | 45–60 |
| 2476 | Swivel Snap | 2.000 | 118 | 170 | 62–80 |
| 2477 | Swivel Snap | 3.000 | 142 | 280 | 85–110 |

**Wichard Triplebar-Schnappschäkel (Série 2995/2996/2997):**

| Artikelnr. | Typ | BL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|-----|----------|------------|-------------|-------------|
| 2995 | Triplebar, festes Auge | 800 | 70 | 48 | 35–48 |
| 2996 | Triplebar, festes Auge | 1.200 | 84 | 82 | 45–60 |
| 2997 | Triplebar, festes Auge | 2.000 | 102 | 148 | 58–75 |
| 2998 | Triplebar, festes Auge | 3.000 | 122 | 240 | 78–100 |

**Wichard Sicherheits-Karabiner (Série 2480/2481):**

| Artikelnr. | Typ | BL (daN) | Öffnung (mm) | Gewicht (g) | Preis (EUR) |
|------------|-----|----------|--------------|-------------|-------------|
| 2480 | HR Screw-Lock | 2.500 | 17 | 95 | 28–38 |
| 2481 | HR Screw-Lock | 2.500 | 22 | 120 | 32–42 |
| 2482 | HR Auto-Lock | 2.500 | 17 | 105 | 35–48 |
| 2483 | HR Auto-Lock | 2.500 | 22 | 130 | 40–52 |
| 2484 | HR Tri-Lock | 2.500 | 17 | 110 | 42–55 |

**Wichard Safety Tether Karabiner (ISO 12401):**

| Artikelnr. | Typ | Norm | BL (daN) | Gewicht (g) | Preis (EUR) |
|------------|-----|------|----------|-------------|-------------|
| 2490 | Safety Tether, Screw | ISO 12401 | 1.500 | 115 | 35–45 |
| 2491 | Safety Tether, Auto | ISO 12401 | 1.500 | 125 | 42–55 |
| 2493 | Overboard Release | ISO 12401 | 1.500 | 140 | 48–62 |

### 4.2 Tylaska (USA)

Tylaska Marine Hardware wurde 1991 in Bristol, Rhode Island, gegründet und ist der Maßstab für High-Performance-Schnappschäkel. Jedes Produkt wird in den USA gefertigt und einzeln getestet.

**Markenphilosophie:**
- Load-Independent Trigger — Auslösekraft unabhängig von der Last
- Anti-Snag-Design — versenkter Trigger
- Jeder Schäkel einzeln proof-load-getestet und serialisiert
- Austauschbare Verschleißteile
- Lebenslange Garantie auf den Körper

#### 4.2.1 Tylaska T-Serie (Standard Edelstahl)

**T5 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 5,3 kN (1.200 lbs) |
| SWL | 1,3 kN (300 lbs) |
| Gesamtlänge | 57 mm |
| Bügelöffnung | 11 mm |
| Gewicht | 28 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 12–18 N |
| Preis (EUR) | 65–85 |
| Primäranwendung | Cunningham, leichte Fallen, Spinnaker-Sheets (Jollen) |

**T8 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 8,9 kN (2.000 lbs) |
| SWL | 2,2 kN (500 lbs) |
| Gesamtlänge | 70 mm |
| Bügelöffnung | 13 mm |
| Gewicht | 48 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 15–22 N |
| Preis (EUR) | 85–110 |
| Primäranwendung | Spinnaker-Fall (Jollen/Sportboote), Fallen (< 10m Yachten) |

**T12 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 13,3 kN (3.000 lbs) |
| SWL | 3,3 kN (750 lbs) |
| Gesamtlänge | 83 mm |
| Bügelöffnung | 16 mm |
| Gewicht | 85 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 18–28 N |
| Preis (EUR) | 110–145 |
| Primäranwendung | Spinnaker-Fall (Fahrtenyachten 10–14m), Fallen, Niederholer |

**T20 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 22,2 kN (5.000 lbs) |
| SWL | 5,6 kN (1.250 lbs) |
| Gesamtlänge | 102 mm |
| Bügelöffnung | 19 mm |
| Gewicht | 142 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 22–32 N |
| Preis (EUR) | 155–195 |
| Primäranwendung | Spinnaker-Fall (große Yachten 14–20m), Hochlast-Fallen |

**T30 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 31,1 kN (7.000 lbs) |
| SWL | 7,8 kN (1.750 lbs) |
| Gesamtlänge | 121 mm |
| Bügelöffnung | 22 mm |
| Gewicht | 227 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 25–38 N |
| Preis (EUR) | 210–265 |
| Primäranwendung | Superyacht-Fallen, extreme Lasten, Regattayachten 20m+ |

**T50 Snap Shackle:**

| Eigenschaft | Wert |
|-------------|------|
| Bruchlast (BL) | 53,4 kN (12.000 lbs) |
| SWL | 13,4 kN (3.000 lbs) |
| Gesamtlänge | 152 mm |
| Bügelöffnung | 28 mm |
| Gewicht | 454 g |
| Material Körper | 316L geschmiedet |
| Material Trigger | 17-4 PH |
| Trigger-Kraft | 30–42 N |
| Preis (EUR) | 320–400 |
| Primäranwendung | Superyacht-Spezialanwendungen, extreme Lasten |

#### 4.2.2 Tylaska T-Serie Titan

Die Titan-Varianten der T-Serie bieten identische Bruchlasten bei ca. 45% weniger Gewicht.

| Modell | BL (kN) | Gewicht (g) | Gewichtersparnis | Preis (EUR) |
|--------|---------|-------------|------------------|-------------|
| T5 Ti | 5,3 | 16 | 43% | 180–230 |
| T8 Ti | 8,9 | 28 | 42% | 240–300 |
| T12 Ti | 13,3 | 50 | 41% | 310–390 |
| T20 Ti | 22,2 | 82 | 42% | 420–530 |
| T30 Ti | 31,1 | 132 | 42% | 580–720 |

#### 4.2.3 Tylaska Swivel-Varianten

Alle T-Modelle sind auch als Swivel-Variante (S-Suffix) erhältlich:

| Modell | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|--------|---------|------------|-------------|-------------|
| T8-S | 8,9 | 88 | 62 | 115–145 |
| T12-S | 13,3 | 102 | 108 | 145–185 |
| T20-S | 22,2 | 124 | 178 | 195–245 |
| T30-S | 31,1 | 146 | 290 | 265–330 |

### 4.3 Harken (USA/Italien)

Harken, gegründet 1967 in Pewaukee, Wisconsin, ist einer der weltweit führenden Hersteller von Segelzubehör. Die Schnappschäkel werden im italienischen Werk in Limena gefertigt.

**Markenphilosophie:**
- Integration in das Harken-Deckssystem (Blöcke, Winschen, Beschläge)
- Breite Produktpalette von Jolle bis Superyacht
- Gutes Preis-Leistungs-Verhältnis im mittleren Segment

#### 4.3.1 Harken Snap Shackles

**Harken Standard Snap Shackle:**

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| 097 | 4,4 | 48 | 17 | 15–22 |
| 098 | 6,7 | 60 | 28 | 18–26 |
| 099 | 11,1 | 72 | 53 | 25–35 |
| 2100 | 17,8 | 89 | 91 | 35–48 |
| 2101 | 26,7 | 108 | 156 | 52–68 |
| 2102 | 40,0 | 130 | 258 | 75–95 |

**Harken Swivel Snap Shackle:**

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| 2108 | 6,7 | 78 | 38 | 28–38 |
| 2109 | 11,1 | 92 | 72 | 35–48 |
| 2110 | 17,8 | 112 | 118 | 48–62 |
| 2111 | 26,7 | 132 | 196 | 68–85 |

**Harken Reflex Snap Shackle (Hochleistung):**

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Trigger-Kraft (N) | Preis (EUR) |
|------------|---------|------------|-------------|---------------------|-------------|
| 2150 | 11,1 | 76 | 62 | 15–25 | 55–72 |
| 2151 | 17,8 | 94 | 108 | 18–28 | 72–92 |
| 2152 | 26,7 | 114 | 175 | 22–32 | 95–120 |
| 2153 | 40,0 | 138 | 285 | 25–38 | 128–160 |

### 4.4 Ronstan (Australien)

Ronstan, gegründet 1953 in Melbourne, bietet ein breites Sortiment an Decksbeschlägen mit ausgezeichnetem Preis-Leistungs-Verhältnis. Die Produktion erfolgt teilweise in Asien nach australischer Qualitätskontrolle.

#### 4.4.1 Ronstan Snap Shackles

**Ronstan Standard Snap Shackle (Serie RF):**

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| RF6200 | 3,5 | 42 | 12 | 10–15 |
| RF6210 | 5,6 | 55 | 22 | 14–20 |
| RF6220 | 8,9 | 68 | 38 | 18–26 |
| RF6230 | 13,3 | 82 | 65 | 25–35 |
| RF6240 | 20,0 | 98 | 108 | 35–48 |
| RF6250 | 31,1 | 118 | 180 | 52–68 |

**Ronstan Swivel Snap Shackle:**

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| RF6310 | 5,6 | 72 | 32 | 22–30 |
| RF6320 | 8,9 | 88 | 52 | 28–38 |
| RF6330 | 13,3 | 105 | 88 | 38–50 |
| RF6340 | 20,0 | 122 | 142 | 50–65 |

### 4.5 Kong (Italien)

Kong, gegründet 1830 in Lecco (Lombardei), ist einer der ältesten Beschläge-Hersteller weltweit. Ursprünglich auf Bergsteiger-Ausrüstung spezialisiert, bietet Kong eine umfangreiche Marine-Karabiner-Linie.

#### 4.5.1 Kong Marine Karabiner

**Kong Locking Carabiner (Marine Serie):**

| Artikelnr. | Typ | BL (kN) | Öffnung (mm) | Gewicht (g) | Preis (EUR) |
|------------|-----|---------|--------------|-------------|-------------|
| 541.L | Screw-Lock, oval | 25 | 18 | 85 | 18–25 |
| 542.L | Screw-Lock, D-Form | 30 | 20 | 100 | 22–30 |
| 543.L | Screw-Lock, HMS | 28 | 22 | 110 | 25–35 |
| 551.A | Auto-Lock, oval | 25 | 18 | 92 | 25–32 |
| 552.A | Auto-Lock, D-Form | 30 | 20 | 108 | 28–38 |
| 561.T | Tri-Lock, oval | 25 | 18 | 98 | 30–40 |
| 562.T | Tri-Lock, D-Form | 30 | 20 | 115 | 35–45 |

**Kong Safety Tether Carabiner (ISO 12401):**

| Artikelnr. | Norm | BL (kN) | Öffnung (mm) | Gewicht (g) | Preis (EUR) |
|------------|------|---------|--------------|-------------|-------------|
| 580.ISO | ISO 12401 | 15 | 20 | 130 | 35–45 |
| 581.ISO | ISO 12401, mit Indikator | 15 | 20 | 138 | 42–52 |

### 4.6 Allen Brothers (UK)

Allen Brothers, gegründet 1956 in Essex (England), ist spezialisiert auf Jollen- und Sportboot-Beschläge. Die Schnappschäkel sind funktional und preislich im Einstiegsbereich positioniert.

#### 4.6.1 Allen Snap Shackles

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| A4055 | 2,5 | 38 | 8 | 6–10 |
| A4056 | 4,0 | 50 | 15 | 9–14 |
| A4058 | 6,5 | 62 | 28 | 12–18 |
| A4060 | 9,0 | 75 | 45 | 18–25 |
| A4062 | 13,0 | 88 | 72 | 25–35 |

**Besonderheit Allen Brothers:**
- Gutes Preis-Leistungs-Verhältnis für den Jollenbereich
- Nyloneinsätze im Trigger zur Geräuschreduktion
- Kompakte Bauform
- Nicht für Hochlast-Anwendungen oder Fahrtenyachten geeignet

### 4.7 Selden (Schweden)

Selden Mast AB, gegründet 1960 in Göteborg, ist primär Masthersteller, bietet aber auch ein umfassendes Sortiment an Decksbeschlägen und Rigg-Komponenten.

#### 4.7.1 Selden Snap Shackles

| Artikelnr. | BL (kN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|------------|---------|------------|-------------|-------------|
| 528-021 | 4,5 | 50 | 18 | 14–20 |
| 528-031 | 7,5 | 64 | 32 | 18–26 |
| 528-041 | 12,0 | 78 | 58 | 25–35 |
| 528-051 | 18,0 | 95 | 98 | 38–50 |
| 528-061 | 28,0 | 115 | 165 | 55–72 |

**Besonderheit Selden:**
- Optimiert für Selden-Rigg-Systeme
- Passende Dimensionen für Selden-Fallen und -Beschläge
- Gute Integration in das Selden-Gesamtsystem

### 4.8 Herstellervergleich — Zusammenfassung

| Hersteller | Stärke | Schwäche | Zielgruppe | Preissegment |
|------------|--------|----------|------------|--------------|
| Wichard | Geschmiedet, Triplebar-Sicherheit | Schwerer als Tylaska | Fahrtensegler, Blauwasser | Mittel–Hoch |
| Tylaska | Höchste Leistung, Anti-Snag | Teuer | Regatta, Superyacht | Hoch–Premium |
| Harken | Breites Sortiment, Integration | Kein Alleinstellungsmerkmal | Alle Bereiche | Mittel |
| Ronstan | Preis-Leistung | Teilweise Guss | Fahrtensegler, Budget | Niedrig–Mittel |
| Kong | Karabiner-Expertise, CE-Zertifiziert | Wenig Schnappschäkel | Safety Tether | Mittel |
| Allen Brothers | Jollen-Spezialist, günstig | Begrenzte Größen | Jollen, Sportboote | Niedrig |
| Selden | Systemintegration | Kleines Sortiment | Selden-System-Nutzer | Mittel |

---

## 5. Anwendungen

### 5.1 Spinnaker-Fall (Spinnaker Halyard)

Die wichtigste Anwendung für Schnappschäkel. Das Spinnaker-Fall muss unter Last gelöst werden können, wenn der Spinnaker geborgen wird.

#### 5.1.1 Anforderungen

- **Schnelles Lösen unter Last**: Das Fall muss in < 2 Sekunden trennbar sein
- **Einhändige Bedienung**: Der Vorschiffs-Crewmember hält sich mit einer Hand fest
- **Sichere Verriegelung**: Der Schäkel darf sich während des Segelns nicht unbeabsichtigt öffnen
- **Drehfreiheit**: Wirbel-Schnappschäkel bevorzugt, um Verdrillung zu vermeiden
- **Korrekter Lastbereich**: SWL > maximale Falllast bei Starkwind

#### 5.1.2 Lastberechnung Spinnaker-Fall

Die Falllast am Spinnaker hängt von der Segelfläche, dem Winddruck und dynamischen Faktoren ab:

**Statische Falllast (vereinfacht):**
```
F_halyard = F_wind × sin(α) × dynamic_factor
F_wind = 0,5 × ρ × v² × A × Cd
```
Wobei:
- ρ = 1,225 kg/m³ (Luftdichte)
- v = Windgeschwindigkeit (m/s)
- A = Segelfläche (m²)
- Cd = Widerstandsbeiwert (~1,2 für Spinnaker)
- α = Ausfallwinkel
- dynamic_factor = 2,0–4,0 (Böen, Füllung)

**Typische Spinnaker-Falllasten:**

| Bootsklasse | Spinnakerfläche (m²) | Falllast 12 kn (kN) | Falllast 20 kn (kN) | Dynamisch max (kN) | Empfohlener Schäkel SWL (kN) |
|-------------|----------------------|----------------------|----------------------|---------------------|-------------------------------|
| Jolle (6m) | 15–25 | 0,3–0,5 | 0,8–1,4 | 2,0–4,0 | 1,5–2,0 |
| Fahrtensegler (10m) | 40–60 | 0,8–1,2 | 2,0–3,2 | 5,0–8,0 | 3,0–4,0 |
| Performance (13m) | 80–120 | 1,5–2,4 | 4,0–6,5 | 10,0–16,0 | 5,0–7,0 |
| Große Yacht (16m) | 120–180 | 2,4–3,6 | 6,0–10,0 | 15,0–25,0 | 7,0–10,0 |
| Superyacht (22m) | 200–350 | 4,0–7,0 | 10,0–18,0 | 25,0–45,0 | 12,0–18,0 |

#### 5.1.3 Empfohlene Schnappschäkel für Spinnaker-Fall

| Bootsklasse | Budget | Mittelklasse | Premium |
|-------------|--------|--------------|---------|
| Jolle (6m) | Allen A4056 | Ronstan RF6210 | Tylaska T5 |
| Fahrtensegler (10m) | Ronstan RF6230 | Wichard 2672 | Tylaska T12 |
| Performance (13m) | Harken 2100 | Wichard 2997 (Triplebar) | Tylaska T20 |
| Große Yacht (16m) | Harken 2101 | Wichard 2998 (Triplebar) | Tylaska T30 |
| Superyacht (22m) | — | Wichard 2674 | Tylaska T50 |

### 5.2 Asymmetrischer Spinnaker — Tack-Verbindung

Der asymmetrische Spinnaker (Gennaker) wird am Tack (Bugbeschlag oder Bugspriet) mit einem Schnappschäkel befestigt. Das schnelle Lösen ermöglicht ein kontrolliertes Bergen durch Aufziehen des Segels am Fall bei gleichzeitigem Lösen des Tacks.

#### 5.2.1 Anforderungen

- **Lösen unter voller Segeldrucklast**: Die Tacklast ist typischerweise 50–70% der Falllast
- **Einhändige Bedienung am Bugspriet**: Unsicherer Arbeitsplatz, oft nass
- **Kompakte Bauform**: Begrenzter Platz am Bugbeschlag
- **Anti-Snag**: Leinen vom Vorsegel können den Trigger berühren

#### 5.2.2 Typische Tacklasten

| Bootsklasse | Gennakerfläche (m²) | Tacklast 15 kn (kN) | Dynamisch max (kN) | Empf. SWL (kN) |
|-------------|---------------------|----------------------|---------------------|-----------------|
| Jolle/Sport (6m) | 15–30 | 0,5–1,0 | 1,5–3,0 | 1,5–2,0 |
| Fahrtensegler (10m) | 35–55 | 1,0–1,8 | 3,0–6,0 | 2,5–3,5 |
| Performance (13m) | 60–100 | 1,8–3,0 | 5,5–10,0 | 4,0–5,5 |
| Große Yacht (16m) | 100–160 | 3,0–5,0 | 9,0–16,0 | 6,0–8,0 |

### 5.3 Quick-Release Fallen (Schnelllösbare Fallen)

Auf modernen Fahrtenyachten und Regattayachten werden auch Großsegel- und Genuafallen mit Schnappschäkeln am Kopf ausgestattet, um einen schnellen Segelwechsel zu ermöglichen.

#### 5.3.1 Anforderungen

- **Lösen unter moderater Last**: Fall wird vor dem Lösen gefiert, Restlast 5–15% BL
- **Sichere Verriegelung**: Fall darf sich während Wochen oder Monaten nicht unbeabsichtigt lösen
- **Korrosionsbeständigkeit**: Fall-Schnappschäkel am Masttop sind der Witterung permanent ausgesetzt
- **Kompatibilität**: Muss zum Falldurchmesser und zum Kopfbrett-Auge des Segels passen

#### 5.3.2 Empfohlene Konfiguration

| Segeltyp | Schäkelposition | Empfohlener Typ | Sicherung |
|----------|-----------------|-----------------|-----------|
| Großsegel | Masttop-Fall → Kopfbrett | Festaugen-Snap, Sicherungsstift | Pin + Tape |
| Genua/Fock | Masttop-Fall → Kopfbrett | Standard-Snap oder Festaugen | Pin + Tape |
| Spinnaker | Masttop-Fall → Kopfbrett | Wirbel-Snap oder Trigger-Release | Nur Trigger |
| Code 0 | Masttop-Fall → Kopfbrett | Wirbel-Snap | Pin bei Langfahrt |

### 5.4 Sicherheitsleine (Safety Tether)

Die Sicherheitsleine verbindet das Sicherheitsgeschirr (Harness) des Crewmitglieds mit der Jackline oder einem festen Punkt an Deck. Die Karabiner an beiden Enden der Leine sind lebenswichtige Ausrüstung.

#### 5.4.1 Anforderungen nach ISO 12401

- **Bruchlast**: Mindestens 15 kN (1.500 daN) in Längsrichtung
- **Verriegelung**: Selbstverriegelnder Mechanismus (Auto-Lock oder Screw-Lock), mindestens 2-Schritt-Öffnung
- **Einhändige Bedienbarkeit**: Muss mit einer Hand und mit nassen Handschuhen bedienbar sein
- **Gate-Öffnung**: Mindestens 15 mm für Standard-Jacklines, 20 mm empfohlen
- **Lösbarkeit unter Last**: Muss auch bei 1 kN Last einhändig lösbar sein
- **Kennzeichnung**: CE-Kennzeichnung, Herstellerangabe, Bruchlast, Prüfnorm

#### 5.4.2 Konfiguration Safety Tether

Eine Standard-Sicherheitsleine besteht aus:

1. **Schiff-seitiger Karabiner (Ship End)**: Tri-Lock oder Auto-Lock, Öffnung ≥ 20 mm für Jackline-Gurtband
2. **Leine (Tether)**: 1,0 m oder 2,0 m elastisches Gurtband oder Dyneema-Kernmantel
3. **Körper-seitiger Karabiner (Body End)**: Tri-Lock oder Auto-Lock, Öffnung ≥ 15 mm für Harness-D-Ring
4. **Optional: Kurz-Strop**: 1,0 m Leine mit zusätzlichem Karabiner für cockpitnahe Sicherung

#### 5.4.3 Empfohlene Karabiner für Safety Tether

| Hersteller | Modell | Norm | BL (kN) | Öffnung (mm) | Preis (EUR) |
|------------|--------|------|---------|--------------|-------------|
| Wichard | 2490 | ISO 12401 | 15 | 20 | 35–45 |
| Wichard | 2493 (Overboard) | ISO 12401 | 15 | 22 | 48–62 |
| Kong | 580.ISO | ISO 12401 | 15 | 20 | 35–45 |
| Spinlock | Deckware | ISO 12401 | 15 | 23 | 42–55 |
| Gibb | Safety Hook | ISO 12401 | 15 | 20 | 30–42 |

### 5.5 Jackline-Befestigung

Jacklines (Sicherheitsleinen, die längs über das Deck gespannt werden) werden an Bug und Heck mit Schnappschäkeln oder Karabinern befestigt.

#### 5.5.1 Anforderungen

- **Dauerbelastung**: Jacklines stehen unter moderater Vorspannung
- **Stoßlast bei Sturz**: Bis zu 12 kN bei Sturz einer Person
- **Korrosionsbeständigkeit**: Permanent der Witterung ausgesetzt
- **Schnelle Montage/Demontage**: Jacklines werden oft nur bei Bedarf aufgebaut

#### 5.5.2 Empfohlene Befestigung

| Befestigungsart | Beschreibung | SWL (kN) | Empfehlung |
|----------------|--------------|----------|------------|
| D-Schäkel an Augbolzen | Klassisch, sicher, langsam | 8–15 | Dauermontage |
| Snap Shackle an Augbolzen | Schnell auf-/abzubauen | 5–10 | Temporäre Montage |
| Karabiner an Augbolzen | Schnell, einhändig | 6–12 | Temporäre Montage |
| Textil-Loop an Klampe | Notlösung, nicht ideal | 3–8 | Nur Notfall |

### 5.6 Weitere Anwendungen

#### 5.6.1 Baumniederholer (Vang)

- Schnappschäkel zwischen Baumfuß und Niederholer-Beschlag
- Ermöglicht schnelles An-/Abschlagen des Niederholers
- Typisch: Festaugen-Snap, BL 10–25 kN

#### 5.6.2 Cunningham

- Schnappschäkel am Cunningham-Strop
- Schnelles Wechseln zwischen verschiedenen Segeln
- Typisch: Klein (T5/T8 Größe), BL 5–10 kN

#### 5.6.3 Lazy Jacks

- Karabiner oder kleine Schnappschäkel an den Lazy-Jack-Leinen
- Ermöglicht Entfernen bei Spinnaker-Einsatz
- Typisch: Non-Locking Karabiner oder Plunger-Pin Snap

#### 5.6.4 Beiboot-Befestigung

- Schnappschäkel an der Schleppleine des Beiboots
- Schnelles Lösen bei Hafeneinfahrt oder Notfall
- Typisch: Wirbel-Snap, BL 10–20 kN

---

## 6. Sicherheitsaspekte

### 6.1 Unbeabsichtigtes Öffnen unter Last

Das unbeabsichtigte Öffnen (Accidental Release) ist das schwerwiegendste Sicherheitsproblem bei Schnappschäkeln. Die Konsequenzen reichen von Segelschäden bis zu lebensbedrohlichen Situationen.

#### 6.1.1 Dokumentierte Unfallszenarien

**Szenario 1 — Spinnaker-Verlust durch Sheet-Kontakt:**
Eine lose Spinnaker-Sheet wickelt sich beim Bergen um den Trigger des Fall-Schnappschäkels. Die Zugbewegung der Sheet löst den Trigger aus, das Segel fliegt unkontrolliert davon. Risiko: Segelverlust (Wert 3.000–15.000 EUR), Verletzung durch peitschendes Fall.

**Szenario 2 — Genua-Fall löst sich bei Starkwind:**
Vibration und Schlagen des Segels bei 30+ Knoten lösen einen verschlissenen Schnappschäkel am Genua-Fall. Die 30+ m² Genua schlägt unkontrolliert. Risiko: Riggschäden, Personenverletzung.

**Szenario 3 — Safety Tether versagt:**
Ein nicht-verriegelnder Karabiner (Non-Locking) wird irrtümlich als Safety Tether eingesetzt. Bei einer Welle öffnet sich das Gate durch Kontakt mit der Jackline. Die Person geht über Bord ohne Sicherung. Risiko: Tod.

#### 6.1.2 Prävention

**Konstruktive Maßnahmen:**
- Anti-Snag-Design (Tylaska, Wichard Triplebar)
- Versenkter Trigger (nicht von Leinen erreichbar)
- Ausreichende Federspannung (Prüfung: > 2 kg Fingerkraft zum Öffnen)
- Sicherungsstift bei Fallen

**Organisatorische Maßnahmen:**
- Regelmäßige Inspektion aller Schnappschäkel (alle 3 Monate oder 50 Segeltage)
- Wartungsprotokoll mit Federkraft-Messung
- Schulung der Crew über korrektes Einhängen
- Klare Markierung: Welcher Schäkel für welche Anwendung

**Regulatorische Maßnahmen:**
- Nur ISO-12401-konforme Karabiner für Safety Tether
- Keine Non-Locking-Karabiner für sicherheitskritische Anwendungen
- ISAF/World Sailing OSR: Vorgeschriebene Spezifikationen für Regatta

### 6.2 Sicherheitsleine — Anforderungen nach ISO 12401

ISO 12401:2009 „Small craft — Deck safety harness and safety line — Safety harness and safety line for use on recreational craft" definiert die Anforderungen an Sicherheitsgeschirre und -leinen.

#### 6.2.1 Anforderungen an Karabiner (Hooks)

| Anforderung | Spezifikation |
|-------------|--------------|
| Bruchlast Längsrichtung | ≥ 15 kN |
| Bruchlast Querrichtung | ≥ 10 kN (wenn konstruktionsbedingt möglich) |
| Bruchlast Gate offen | ≥ 7 kN |
| Verriegelung | Mindestens 2-Stufen-Öffnung (Drehen + Drücken oder Schrauben + Drücken) |
| Öffnung | ≥ 15 mm (empfohlen: ≥ 20 mm für Jackline-Gurtband) |
| Einhändige Bedienung | Muss mit einer Hand und nassen Handschuhen bedienbar sein |
| Lösen unter 1 kN Last | Muss einhändig möglich sein |
| Salzsprühtest | ≥ 500 Stunden ohne Funktionsverlust |
| Zyklentest | 10.000 Zyklen ohne Versagen |
| Kennzeichnung | CE, Hersteller, BL, Norm, Produktionsdatum oder -charge |

#### 6.2.2 Kritische Hinweise

- **NIEMALS** einen Non-Locking-Karabiner als Safety Tether verwenden
- **NIEMALS** einen Schnappschäkel als Safety Tether verwenden (Trigger kann sich lösen)
- Karabiner alle 5 Jahre oder nach einem Sturz tauschen
- Beschädigte oder korrodierte Karabiner sofort ersetzen
- Karabiner-Gate muss sich selbstständig und vollständig schließen

### 6.3 Prüfprotokolle für den Bordbetrieb

#### 6.3.1 Saisonale Prüfung (vor jeder Saison)

**Schnappschäkel:**
1. Sichtprüfung auf Risse, Verformung, Korrosion
2. Funktionsprüfung Trigger: Öffnen und Schließen, Federspannung subjektiv bewerten
3. Bügelspiel prüfen: Darf nicht wackeln oder klemmen
4. Verriegelung prüfen: Bügel muss vollständig einrasten
5. Auge/Wirbel prüfen: Keine Risse, kein übermäßiges Spiel

**Karabiner:**
1. Gate-Funktion: Muss von selbst vollständig schließen
2. Verriegelung: Screw-Lock festziehen, Auto-Lock/Tri-Lock prüfen
3. Gate-Feder: Ausreichende Schließkraft
4. Oberfläche: Keine Risse, keine tiefe Korrosion
5. Kennzeichnung: Lesbar, Ablaufdatum prüfen (falls vorhanden)

#### 6.3.2 Monatliche Sichtprüfung (während der Saison)

- Alle Schnappschäkel und Karabiner visuell auf Beschädigungen prüfen
- Trigger-Funktion stichprobenartig testen
- Fallen-Schnappschäkel am Masttop: Bei Mastinspektion gesondert prüfen
- Sicherheitsleinen-Karabiner: Vor jeder Nachtfahrt oder Starkwind-Situation prüfen

### 6.4 Austauschkriterien

Ein Schnappschäkel oder Karabiner muss SOFORT ausgetauscht werden, wenn:

| Befund | Dringlichkeit | Begründung |
|--------|--------------|------------|
| Sichtbare Risse | SOFORT | Versagen unmittelbar bevorstehend |
| Plastische Verformung | SOFORT | Überlastung erfolgt, Restfestigkeit unbekannt |
| Trigger klemmt oder hakt | VOR NÄCHSTEM EINSATZ | Funktion nicht gewährleistet |
| Federspannung < 1 kg | VOR NÄCHSTEM EINSATZ | Unbeabsichtigtes Öffnen möglich |
| Gate schließt nicht vollständig | SOFORT | Keine Verbindungssicherheit |
| Tiefe Lochfraß-Korrosion (Pitting) | VOR NÄCHSTEM EINSATZ | Festigkeitsreduktion unklar |
| Bügel hat seitliches Spiel > 1 mm | Saisonende | Verschleiß am Drehpunkt |
| Wirbel dreht nicht mehr frei | BALD | Torsionsbelastung auf Fall/Segel |
| Alter > 10 Jahre (Fahrt) | Saisonbeginn | Materialermüdung |
| Alter > 5 Jahre (Regatta-intensiv) | Saisonbeginn | Materialermüdung |

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F-SS-01: Trigger-Mechanismus-Versagen

**Beschreibung:**
Der Trigger-Hebel oder -Kolben lässt sich nicht mehr betätigen oder kehrt nach Betätigung nicht in die Ausgangsposition zurück.

**Visuelle Merkmale:**
- Trigger-Hebel steht in Zwischenposition
- Sichtbare Salzkristalle im Trigger-Mechanismus
- Rost oder grüne Patina (bei Bronzefedern) im Mechanismusbereich
- Verbogener oder gebrochener Trigger-Hebel

**Ursachen:**
- Korrosion durch mangelnde Wartung (keine Süßwasserspülung)
- Mechanische Beschädigung durch Stoß
- Fremdkörper (Sand, Fasern) im Mechanismus
- Ermüdungsbruch des Trigger-Hebels

**Auswirkung:**
- Schäkel kann nicht geöffnet werden → Bergen unmöglich
- ODER: Schäkel schließt nicht sicher → Sicherheitsrisiko

**Behebung:**
1. Soaking in Süßwasser (12–24 Stunden)
2. Mechanismus mit Druckluft ausblasen
3. Teflon-Spray oder Silikon-Öl applizieren
4. Bei Bruch: Austausch des gesamten Schäkels

**AYDI-Confidence:** visual_medium (Trigger-Position sichtbar, aber Ursache nicht immer erkennbar)

### 7.2 Fehlerbild F-SS-02: Federermüdung (Spring Fatigue)

**Beschreibung:**
Die Trigger- oder Bügelfeder hat ihre Spannung verloren. Der Bügel schließt nicht mehr mit ausreichender Kraft oder der Trigger kehrt nicht vollständig zurück.

**Visuelle Merkmale:**
- Bügel schließt langsam oder unvollständig
- Trigger-Hebel bewegt sich „weich" ohne definierten Widerstand
- Bei geöffnetem Schäkel: Feder hat sichtbare Verformung oder Verfärbung

**Ursachen:**
- Alterung (Spannungsrelaxation über Zeit)
- Temperatureinfluss (hohe Temperaturen beschleunigen Relaxation)
- Korrosion der Feder (Festigkeitsverlust)
- Überdehnung durch unsachgemäße Handhabung

**Auswirkung:**
- Unbeabsichtigtes Öffnen unter Last → Segelversagen, Sicherheitsrisiko
- Bügel schließt nicht vollständig → Verbindung nicht gesichert

**Behebung:**
1. Feder tauschen (bei Tylaska: Ersatzteile verfügbar)
2. Bei nicht-servicebaren Schäkeln: Komplettaustausch
3. Präventiv: Federspannung jährlich prüfen

**AYDI-Confidence:** visual_low (Federzustand nur bei geöffnetem Schäkel oder durch Funktionstest erkennbar)

### 7.3 Fehlerbild F-SS-03: Unbeabsichtigtes Öffnen (Accidental Opening)

**Beschreibung:**
Der Schnappschäkel öffnet sich ohne manuelle Betätigung des Triggers während des Betriebs.

**Visuelle Merkmale:**
- Geöffneter Bügel unter Last
- Verlorenes Segel oder Fall
- Spuren von Leinen-Kontakt am Trigger (Abriebspuren)

**Ursachen:**
- Leine/Sheet wickelt sich um Trigger
- Stoß gegen Beschlag löst Trigger aus
- Federermüdung (F-SS-02 als Vorstufe)
- Falsche Montageausrichtung (Trigger zur Leine)
- Vibration bei Motorfahrt oder Rigg-Schwingung

**Auswirkung:**
- KRITISCH: Segelverlust, Riggschäden, Personengefährdung
- Abhängig von der Anwendung: von ärgerlich bis lebensbedrohlich

**Behebung:**
1. Sofortige Ursachenanalyse
2. Schäkel ersetzen oder Sicherungsmaßnahme implementieren
3. Montageausrichtung prüfen (Trigger weg von Leinen)
4. Anti-Snag-Schäkel einsetzen (Tylaska, Wichard Triplebar)
5. Sicherungsstift verwenden bei nicht-schnelllösbaren Anwendungen

**AYDI-Confidence:** documented (wenn Vorfall berichtet wird), visual_insufficient (nachträgliche Analyse schwierig)

### 7.4 Fehlerbild F-SS-04: Bolzenverschleiß am Drehpunkt (Pivot Pin Wear)

**Beschreibung:**
Der Bolzen, um den der Bügel schwenkt, verschleißt durch die zyklische Belastung und entwickelt Spiel.

**Visuelle Merkmale:**
- Seitliches Spiel des Bügels (> 0,5 mm)
- Bügel steht nicht mehr parallel zum Körper
- Sichtbarer Materialabrieb am Bolzen oder an der Bohrung

**Ursachen:**
- Normaler Verschleiß bei hoher Zyklenbelastung
- Korrosion am Bolzen (Reibkorrosion / Fretting)
- Überlastung (Verformung des Bolzens)
- Sand oder Partikel im Drehpunkt

**Auswirkung:**
- Reduzierte Bruchlast (Bolzen ist potenzielle Bruchstelle)
- Schlechte Verriegelung (Bügel rastet nicht sauber ein)
- Erhöhte Gefahr des unbeabsichtigten Öffnens

**Behebung:**
1. Bolzen tauschen (bei servicebaren Modellen)
2. Bei nicht-servicebaren Modellen: Komplettaustausch
3. Präventiv: Drehpunkt regelmäßig schmieren

**AYDI-Confidence:** visual_medium (Spiel durch Foto schwer zu erkennen, aber Fehlstellung des Bügels sichtbar)

### 7.5 Fehlerbild F-SS-05: Korrosion am Schäkelkörper (Body Corrosion)

**Beschreibung:**
Korrosionserscheinungen am Körper des Schnappschäkels, die die strukturelle Integrität beeinträchtigen.

**Visuelle Merkmale:**
- Lochfraß (Pitting): Kleine, tiefe Löcher in der Oberfläche
- Spaltkorrosion: Korrosion in Spalten zwischen Bügel und Körper
- Allgemeine Oberflächenkorrosion: Matte, raue Oberfläche
- Rost-Spuren (bei unzureichendem Edelstahl oder fremdem Metallkontakt)

**Ursachen:**
- Kontaktkorrosion (galvanisches Element mit Aluminium oder Stahl)
- Chlorid-Konzentration (unzureichende Spülung)
- Minderwertiges Material (nicht 316L oder unterdimensioniert)
- Spaltkorrosion durch eingeschlossene Feuchtigkeit

**Auswirkung:**
- Festigkeitsreduktion: Pitting kann lokale Spannungsspitzen erzeugen
- Bei tiefem Pitting: 20–50% Festigkeitsverlust möglich
- Trigger-Blockade durch Korrosionsprodukte

**Behebung:**
1. Leichte Korrosion: Reinigen, passivieren (Zitronensäure oder Oxalsäure)
2. Mittlere Korrosion: Mechanisch reinigen (Scotch-Brite, KEIN Stahlwolle), passivieren
3. Tiefe Korrosion / Pitting > 0,5 mm: Austausch
4. Präventiv: Süßwasserspülung, Kontaktkorrosion vermeiden

**AYDI-Confidence:** visual_high (Korrosion ist visuell gut erkennbar)

### 7.6 Fehlerbild F-SS-06: Bügelverformung (Bow Deformation)

**Beschreibung:**
Der Bügel des Schnappschäkels ist plastisch verformt, sodass er nicht mehr korrekt schließt oder die Lastübertragung beeinträchtigt ist.

**Visuelle Merkmale:**
- Bügel steht im geschlossenen Zustand nicht bündig am Körper
- Sichtbare Biegung oder Verformung des Bügels
- Spalt zwischen Bügel und Körper im geschlossenen Zustand

**Ursachen:**
- Überlastung (Last > SWL, insbesondere Stoßlasten)
- Seitliche Belastung (Querlast auf den Bügel)
- Mechanische Beschädigung (Schlag, Fall auf Deck)

**Auswirkung:**
- SOFORTIGER AUSTAUSCH: Verformung zeigt Überlastung an
- Restfestigkeit nicht bestimmbar
- Verriegelung nicht mehr sicher

**Behebung:**
1. Sofortiger Austausch — KEIN Richten oder Nachbiegen
2. Ursachenanalyse: Warum wurde der Schäkel überlastet?
3. Dimensionierung prüfen: Größeren Schäkel einsetzen

**AYDI-Confidence:** visual_high (Verformung ist visuell gut erkennbar)

### 7.7 Fehlerbild F-SS-07: Wirbel-Blockade (Swivel Seizure)

**Beschreibung:**
Der Wirbel eines Wirbel-Schnappschäkels dreht nicht mehr frei oder ist vollständig blockiert.

**Visuelle Merkmale:**
- Wirbel dreht sich nicht oder nur schwergängig
- Sichtbare Korrosion am Wirbel-Interface
- Verdrehte Leine am Fall (Folge des blockierten Wirbels)

**Ursachen:**
- Korrosion im Wirbelgelenk
- Salzkristalle im Wirbel
- Überlastung (Verformung der Wirbelkomponenten)
- Fremdkörper im Wirbel

**Auswirkung:**
- Torsion wird auf Fall und Segel übertragen → Segelform-Verschlechterung
- Falldraht kann sich verdrillen → Drahtbruch
- Erhöhte Last auf den Schäkelkörper durch Torsionsmoment

**Behebung:**
1. Soaking in Süßwasser + WD-40 oder Penetrationsöl
2. Wirbel vorsichtig hin- und herdrehen
3. Mit Teflon-Spray oder Silikon-Öl schmieren
4. Bei dauerhafter Blockade: Austausch

**AYDI-Confidence:** visual_medium (verdrehte Leine als Indikator sichtbar)

### 7.8 Fehlerbild F-SS-08: Gate-Feder-Versagen bei Karabinern (Gate Spring Failure)

**Beschreibung:**
Die Gate-Feder eines Karabiners hat versagt — das Gate schließt nicht mehr selbstständig oder bleibt in halb-offener Position.

**Visuelle Merkmale:**
- Gate steht offen oder halb offen
- Gate schließt nur bei Schwerkraftunterstützung (Gate nach unten)
- Sichtbare Korrosion an der Feder oder am Feder-Sitz

**Ursachen:**
- Federermüdung
- Korrosion der Feder
- Mechanische Beschädigung (verbogenes Gate)
- Sand oder Salzkristalle im Feder-Mechanismus

**Auswirkung:**
- KRITISCH bei Safety Tether: Keine Verbindungssicherheit
- Gate-offene Bruchlast ist 50–70% geringer als Gate-geschlossen
- Unbeabsichtigtes Aushängen möglich

**Behebung:**
1. SOFORTIGER AUSTAUSCH bei sicherheitskritischer Anwendung
2. Reinigung und Schmierung kann temporär helfen
3. Feder-Tausch nur bei dafür vorgesehenen Modellen

**AYDI-Confidence:** visual_high (offenes Gate ist eindeutig erkennbar)

### 7.9 Fehlerbild F-SS-09: Verriegelungs-Versagen bei Karabinern (Lock Mechanism Failure)

**Beschreibung:**
Der Verriegelungsmechanismus (Screw-Lock, Auto-Lock, Tri-Lock) funktioniert nicht mehr korrekt.

**Visuelle Merkmale:**
- Schraubhülse dreht nicht oder lässt sich nicht festziehen
- Auto-Lock-Hülse rastet nicht ein
- Tri-Lock-Hülse dreht oder hebt nicht
- Sichtbare Korrosion oder Verformung am Verriegelungsmechanismus

**Ursachen:**
- Korrosion (Salzkristalle im Gewinde)
- Cross-Threading (Gewinde übergedreht)
- Mechanische Beschädigung
- Materialabrieb

**Auswirkung:**
- Karabiner funktioniert nur noch als Non-Locking → Sicherheitsrisiko
- Bei Safety Tether: Nicht mehr ISO-12401-konform → SOFORTIGER AUSTAUSCH

**Behebung:**
1. Reinigung mit Süßwasser und Bürste
2. Schmierung des Gewindes (NICHT Fett, sondern Teflon-Spray)
3. Bei Cross-Threading: Austausch
4. Bei Korrosion im Gewinde: Zitronensäure-Bad, dann Teflon-Spray

**AYDI-Confidence:** visual_medium (Verriegelungszustand oft schwer per Foto zu beurteilen)

### 7.10 Fehlerbild F-SS-10: Dyneema-Degradation bei Soft-Attachment

**Beschreibung:**
Die Dyneema-Schlaufe eines Soft-Attachment-Schnappschäkels zeigt Alterungserscheinungen.

**Visuelle Merkmale:**
- Verfärbung (UV-Degradation: Grau → Weiß, raue Oberfläche)
- Ausfasern der Schlaufe
- Sichtbare Abriebstellen (Chafe)
- Reduzierter Durchmesser an Belastungspunkten

**Ursachen:**
- UV-Strahlung (primärer Alterungsfaktor)
- Mechanischer Abrieb (Kontakt mit Beschlägen)
- Chemische Einflüsse (Dieselkraftstoff, Reinigungsmittel)
- Überlastung (Kreechverformung / Creep)

**Auswirkung:**
- Festigkeitsverlust: 10–50% je nach Schädigung
- Plötzliches Versagen ohne Vorwarnung möglich

**Behebung:**
1. Regelmäßiger Austausch der Schlaufe (alle 1–3 Saisons, je nach Exposition)
2. Vor Saisonbeginn: Durchmesser-Messung (> 10% Reduktion → tauschen)
3. Bei sichtbarer Beschädigung: Sofortiger Austausch

**AYDI-Confidence:** visual_high (Faserveränderungen visuell gut erkennbar)

### 7.11 Fehlerbild F-SS-11: Galvanische Korrosion durch Materialpaarung

**Beschreibung:**
Kontaktkorrosion zwischen dem Schnappschäkel (Edelstahl 316L) und einem benachbarten Bauteil aus einem anderen Metall.

**Visuelle Merkmale:**
- Verfärbung am Kontaktbereich
- Rost-Spuren an Edelstahl (durch Eisenkontakt = Fremdrost)
- Weiße Ablagerungen (Aluminium-Korrosion)
- Materialabtrag am unedleren Partner

**Ursachen:**
- Aluminium-Beschlag in direktem Kontakt mit Edelstahl-Schäkel
- Verzinkter Stahl (Ankerkette) in Kontakt mit Edelstahl
- Kupfer/Messing-Beschlag neben Edelstahl (weniger kritisch)

**Auswirkung:**
- Beschleunigter Korrosionsangriff am unedleren Metall
- Fremdrost am Edelstahl (optisch, nicht strukturell)
- Bei Aluminium: Kann zu schnellem Materialversagen führen

**Behebung:**
1. Isolierscheibe (Nylon, PTFE) zwischen die Metalle einsetzen
2. Materialpaarung ändern (gleiche Legierung verwenden)
3. Schutzanstrich auf unedlerem Partner

**AYDI-Confidence:** visual_high (Korrosionsspuren visuell gut erkennbar)

### 7.12 Fehlerbild F-SS-12: Falsche Dimensionierung (Undersized Shackle)

**Beschreibung:**
Ein Schnappschäkel ist für seine Anwendung unterdimensioniert — die SWL ist geringer als die tatsächliche Betriebslast.

**Visuelle Merkmale:**
- Optisch kleiner Schäkel an großer Leine/Fall
- Bügelöffnung passt knapp oder gar nicht zur Leine
- Anzeichen von Überlastung: leichte Verformung, Verschleiß am Drehpunkt

**Ursachen:**
- Falsche Berechnung der Betriebslast
- Austausch durch „was gerade da war"
- Upgrade des Segels ohne Upgrade des Schäkels
- Verwendung eines Standard-Schäkels für eine Hochlast-Anwendung

**Auswirkung:**
- Vorzeitiger Verschleiß
- Erhöhte Gefahr des plötzlichen Versagens
- Kein Sicherheitsfaktor vorhanden

**Behebung:**
1. Lastberechnung durchführen (siehe Abschnitt 5)
2. Korrekten Schäkel gemäß SWL-Tabelle auswählen
3. Nächstgrößeren Schäkel verwenden, wenn Berechnung unsicher

**AYDI-Confidence:** visual_medium (Größenverhältnis visuell einschätzbar), measured (wenn Schäkel-Daten und Lastdaten bekannt)

---

## 8. Troubleshooting-Entscheidungsbaum

### 8.1 Entscheidungsbaum 1: Schnappschäkel lässt sich nicht öffnen

```
START: Schnappschäkel lässt sich nicht öffnen
│
├─ Trigger-Hebel/Kolben bewegt sich gar nicht?
│  ├─ JA → Korrosion oder Fremdkörper im Mechanismus
│  │       → Süßwasser-Soaking 12h, dann WD-40 und vorsichtig bewegen
│  │       → Falls weiterhin blockiert: Schäkel unter Last setzen 
│  │          und erneut versuchen (Last kann Reibung reduzieren)
│  │       → Falls immer noch blockiert: Leine kappen und Schäkel ersetzen
│  │
│  └─ NEIN → Trigger bewegt sich teilweise?
│            ├─ JA → Feder blockiert oder gebrochen
│            │       → Mechanismus reinigen und schmieren
│            │       → Feder prüfen (falls sichtbar)
│            │       → Nach Reinigung: Trigger muss vollständig durchgehen
│            │       → Falls nicht: Austausch
│            │
│            └─ NEIN → Trigger bewegt sich voll, Bügel öffnet nicht
│                      → Verriegelungspunkt korrodiert oder verklemmt
│                      → Last komplett entfernen
│                      → Bügel mit Werkzeug vorsichtig aufhebeln
│                      → Schäkel ersetzen (Verriegelung nicht mehr vertrauenswürdig)
```

### 8.2 Entscheidungsbaum 2: Schnappschäkel öffnet sich unbeabsichtigt

```
START: Schnappschäkel hat sich unbeabsichtigt geöffnet
│
├─ Ist die Feder noch intakt (Bügel schnappt zurück)?
│  ├─ JA → Trigger wurde extern ausgelöst
│  │       → Prüfe: Leinen in der Nähe des Triggers?
│  │       │ ├─ JA → Montageausrichtung ändern (Trigger weg von Leinen)
│  │       │ │       → Anti-Snag-Schäkel einsetzen (Tylaska, Wichard Triplebar)
│  │       │ │       → Sicherungsstift verwenden (wenn Schnelllösung nicht benötigt)
│  │       │ └─ NEIN → Stoß oder Vibration als Ursache
│  │       │           → Schäkel gegen Anschlagen sichern (Polster, Positionsänderung)
│  │       │           → Sicherungsstift verwenden
│  │
│  └─ NEIN → Feder ermüdet oder gebrochen
│            → Feder tauschen (Tylaska: Ersatzteile verfügbar)
│            → Bei anderen Herstellern: Komplettaustausch
│            → Präventiv: Federspannung jährlich prüfen
```

### 8.3 Entscheidungsbaum 3: Karabiner-Gate schließt nicht

```
START: Karabiner-Gate schließt nicht selbstständig
│
├─ Gate bewegt sich frei (kein Widerstand)?
│  ├─ JA → Feder gebrochen oder ausgefallen
│  │       → SOFORTIGER AUSTAUSCH (keine Reparatur möglich)
│  │       → Temporär: Karabiner mit Tape sichern (NUR Notfall)
│  │
│  └─ NEIN → Gate klemmt in offener Position?
│            ├─ JA → Korrosion oder Fremdkörper
│            │       → Süßwasser + Bürste, dann Teflon-Spray
│            │       → Gate mehrfach betätigen
│            │       → Falls Gate danach frei schließt: OK, aber engmaschig prüfen
│            │       → Falls Gate weiterhin klemmt: Austausch
│            │
│            └─ NEIN → Gate schließt teilweise
│                      → Verformung des Gates oder der Nase
│                      → Austausch (Gate-Verformung = Überlastung)
```

### 8.4 Entscheidungsbaum 4: Welchen Schnappschäkel brauche ich?

```
START: Schnappschäkelauswahl
│
├─ Anwendung: Safety Tether / Sicherheitsleine?
│  └─ JA → KEINEN Schnappschäkel! → Locking Carabiner nach ISO 12401
│
├─ Anwendung: Spinnaker-Fall oder Tack?
│  ├─ Regatta?
│  │  ├─ JA → Tylaska T-Serie (Load-Independent Trigger)
│  │  └─ NEIN → Wichard Triplebar oder Harken Reflex
│  │
│  └─ Wirbel benötigt?
│     ├─ JA → Swivel-Variante (T-S oder Wichard Swivel)
│     └─ NEIN → Standard mit festem Auge
│
├─ Anwendung: Großsegel/Genua-Fall?
│  └─ Standard Snap Shackle mit Sicherungsstift
│     → Dimensionierung nach Falllast-Tabelle (Abschnitt 5)
│
├─ Anwendung: Niederholer/Cunningham?
│  └─ Festaugen-Snap oder Plunger-Pin
│     → Kleine Bauform bevorzugt (T5/T8 Klasse)
│
└─ Anwendung: Lazy Jacks / leichte Befestigung?
   └─ Plunger-Pin Snap oder Non-Locking Karabiner
      → Geringste Bruchlast-Anforderung
```

### 8.5 Entscheidungsbaum 5: Korrosion am Schnappschäkel

```
START: Korrosion am Schnappschäkel festgestellt
│
├─ Art der Korrosion?
│  ├─ Oberflächenkorrosion (matte, raue Oberfläche)
│  │  └─ Reinigen (Scotch-Brite, KEIN Stahlwolle)
│  │     → Passivieren (Zitronensäure 10%, 30 min einwirken)
│  │     → Spülen und trocknen
│  │     → OK, weiter verwenden, häufiger prüfen
│  │
│  ├─ Lochfraß (Pitting, kleine tiefe Löcher)
│  │  ├─ Pitting < 0,3 mm Tiefe
│  │  │  └─ Reinigen, passivieren, engmaschig überwachen
│  │  │     → Austausch bei nächster Gelegenheit planen
│  │  │
│  │  └─ Pitting ≥ 0,3 mm Tiefe
│  │     └─ SOFORTIGER AUSTAUSCH
│  │        → Festigkeitsverlust nicht kalkulierbar
│  │
│  ├─ Spaltkorrosion (im Spalt Bügel/Körper)
│  │  └─ Spalt reinigen (Zahnarzt-Sonde oder dünner Draht)
│  │     → Teflon-Spray in den Spalt
│  │     → Regelmäßig wiederholen
│  │     → Bei fortgeschrittener Spaltkorrosion: Austausch
│  │
│  └─ Fremdrost (orangebraun, von externem Eisenkontakt)
│     └─ Reinigen (Oxalsäure oder Bar Keepers Friend)
│        → Kontaktquelle identifizieren und eliminieren
│        → Kein Strukturproblem, nur optisch
```

---

## 9. FAQ — Häufige Fragen

### F01: Was ist der Unterschied zwischen einem Schnappschäkel und einem normalen D-Schäkel?

**Antwort:** Ein D-Schäkel wird mit einem Schraubbolzen verschlossen und erfordert zum Öffnen ein Werkzeug und beide Hände. Ein Schnappschäkel hat einen federbelasteten Trigger-Mechanismus, der ein Öffnen mit einer Hand in Sekundenbruchteilen ermöglicht — auch unter Last. Dafür hat ein D-Schäkel bei gleicher Größe eine höhere Bruchlast (kein Mechanismus als Schwachstelle) und ist sicherer gegen unbeabsichtigtes Öffnen. Regel: D-Schäkel für permanente Verbindungen, Schnappschäkel für häufig gelöste Verbindungen.

### F02: Kann ich einen Schnappschäkel als Sicherheitsleine-Karabiner verwenden?

**Antwort:** NEIN, NIEMALS. Schnappschäkel können sich unbeabsichtigt öffnen (Leinenkontakt, Stoß, Vibration). ISO 12401 schreibt selbstverriegelnde Karabiner mit mindestens 2-Stufen-Öffnung vor. Nur Karabiner mit der Kennzeichnung „ISO 12401" oder „EN 362" dürfen als Sicherheitsleine-Karabiner eingesetzt werden.

### F03: Wie oft muss ich meine Schnappschäkel warten?

**Antwort:** Mindestens: Süßwasserspülung nach jedem Segeltag in Salzwasser. Schmierung (Teflon- oder Silikonöl) alle 4–6 Wochen während der Saison. Vollständige Inspektion (Federspannung, Verschleiß, Korrosion) vor jeder Saison. Fallen-Schnappschäkel am Masttop bei jeder Mastinspektion. Professionelle Yachten/Regatta: monatliche Funktionsprüfung aller Schäkel.

### F04: Welche Bruchlast brauche ich für mein Spinnaker-Fall?

**Antwort:** Faustregel: SWL des Schnappschäkels ≥ erwartete Maximallast unter dynamischen Bedingungen. Für eine 12m-Fahrtenyacht mit 60m² Spinnaker bedeutet das: Maximallast dynamisch ca. 8–10 kN, SWL ≥ 4–5 kN, Bruchlast ≥ 16–20 kN. Empfehlung: Tylaska T12 (BL 13,3 kN) oder T20 (BL 22,2 kN) bzw. Wichard 2672 (BL 12 kN) oder 2673 (BL 20 kN).

> ⚠️ **ZU PRÜFEN (Audit):** Diese Antwort fordert selbst SWL ≥ 4–5 kN und BL ≥ 16–20 kN, empfiehlt dann aber u.a. Tylaska T12 (SWL 3,3 kN / BL 13,3 kN) und Wichard 2672 (SWL 3,0 kN / BL 12 kN) — beide liegen UNTER der hier genannten Mindest-SWL und Mindest-BL für dieses last-/sicherheitskritische Spinnakerfall. Nur T20 (BL 22,2 kN) und Wichard 2673 (BL 20 kN) erfüllen die Anforderung; Dimensionierung vor Verwendung verifizieren.

### F05: Sind Titan-Schnappschäkel den Aufpreis wert?

**Antwort:** Für Fahrtensegler: Nein, der Mehrpreis (Faktor 3–4) rechtfertigt die Gewichtsersparnis (ca. 40%) nicht. Für Regattasegler auf Yachten > 10m: Ja, wenn das Mastgewicht optimiert wird — jedes Gramm am Masttop beeinflusst die Stabilität. Für Superyachten: Ja, weil die Korrosionsbeständigkeit von Titan überlegen ist und die Kosten im Gesamtbudget marginal sind.

### F06: Wichard oder Tylaska — was ist besser?

**Antwort:** Beide sind Premium-Hersteller. Wichard bietet das Triplebar-Sicherheitssystem und ist in Europa besser verfügbar. Tylaska bietet den Load-Independent Trigger (Auslösekraft unabhängig von der Last) und das Anti-Snag-Design. Für Regatta: Tylaska. Für Fahrt und Blauwasser: Wichard (Triplebar-Sicherheit). Für Superyacht: Beide geeignet, Tylaska T30/T50 für extreme Lasten.

### F07: Was bedeutet „Anti-Snag-Design"?

**Antwort:** Der Trigger ist so konstruiert, dass Leinen, Segel oder andere Gegenstände nicht versehentlich den Trigger berühren und auslösen können. Tylaska erreicht dies durch einen versenkten Trigger, der nur durch gezielten Fingerdruck erreichbar ist. Wichard nutzt das Triplebar-System, das drei Hebelsegmente erfordert.

### F08: Mein Schnappschäkel klemmt — was tun?

**Antwort:** 1) Schäkel 12–24 Stunden in Süßwasser einlegen. 2) Mechanismus mit WD-40 oder Penetrationsöl besprühen. 3) Trigger vorsichtig bewegen — NICHT mit Gewalt! 4) Mechanismus mit Druckluft ausblasen. 5) Mit Teflon-Spray schmieren. Falls der Schäkel weiterhin klemmt: Austausch. Ein klemmender Schäkel ist ein Sicherheitsrisiko in beide Richtungen — er kann entweder nicht geöffnet werden oder schließt nicht sicher.

### F09: Kann ich den Trigger oder die Feder eines Schnappschäkels selbst tauschen?

**Antwort:** Bei Tylaska: Ja, Ersatzteile sind verfügbar und der Austausch ist mit einfachem Werkzeug möglich. Bei Wichard: Begrenzt, einige Modelle haben austauschbare Federn. Bei Harken, Ronstan, anderen: In der Regel nicht vorgesehen — Komplettaustausch. Grundsätzlich gilt: Wenn der Schäkelkörper beschädigt oder korrodiert ist, bringt ein Federtausch nichts — Komplettersatz nötig.

### F10: Wie lagere ich Schnappschäkel über den Winter?

**Antwort:** 1) Gründlich mit Süßwasser spülen und trocknen lassen. 2) Mechanismus mit Teflon-Spray schmieren. 3) Trigger mehrfach betätigen, um Schmiermittel zu verteilen. 4) Trocken und luftig lagern (NICHT in einer luftdichten Tüte — Restfeuchtigkeit führt zu Korrosion). 5) Vor Saisonbeginn: Funktionsprüfung aller Schäkel.

### F11: Darf ich WD-40 für marine Schnappschäkel verwenden?

**Antwort:** WD-40 ist als Penetrationsöl zum Lösen korrodierter Mechanismen geeignet. Als Dauerschmierung ist es NICHT geeignet — WD-40 verdunstet und hinterlässt keinen Schutzfilm. Für die Dauerschmierung: Teflon-Spray (PTFE), Silikonöl oder spezielle Marine-Schmiermittel (z.B. Harken McLube, Ronstan Spray). KEIN Fett (zieht Schmutz an und blockiert den Mechanismus).

### F12: Was ist der Unterschied zwischen SWL und BL?

**Antwort:** BL (Breaking Load / Bruchlast) ist die Last, bei der der Schäkel unter statischer Prüfung versagt. SWL (Safe Working Load / sichere Arbeitslast) ist die maximal zulässige Last im regulären Betrieb. SWL = BL / Sicherheitsfaktor. Für marine Beschläge: Sicherheitsfaktor 4 (Standard), 5 (sicherheitskritisch), 3 (Regatta mit häufiger Inspektion). Beispiel: BL 20 kN, Sicherheitsfaktor 4 → SWL 5 kN.

### F13: Kann ich einen Aluminium-Karabiner an einer Edelstahl-Jackline verwenden?

**Antwort:** Technisch ja, aber mit Vorsicht. Aluminium ist unedler als Edelstahl — in Salzwasser entsteht ein galvanisches Element, das den Aluminium-Karabiner beschleunigt korrodiert. Empfehlung: Edelstahl-Karabiner an Edelstahl-Jacklines. Aluminium-Karabiner nur auf Süßwasseryachten oder bei intensiver Pflege (Spülung nach jedem Einsatz).

### F14: Woran erkenne ich einen hochwertigen Schnappschäkel?

**Antwort:** Qualitätsmerkmale: 1) Geschmiedet statt gegossen (Gratlinien als Indikator). 2) Klare Materialangabe (316L, nicht nur „Edelstahl"). 3) Bruchlast auf dem Schäkel eingeprägt oder gelasert. 4) Herstellermarke und Artikelnummer. 5) Gleichmäßige Oberfläche ohne Lunker oder Poren. 6) Trigger bewegt sich definiert und mit ausreichendem Widerstand. 7) Bügel rastet hörbar und fühlbar ein. 8) Kein seitliches Spiel am Bügel.

### F15: Wie viele Schnappschäkel brauche ich für meine Yacht?

**Antwort:** Abhängig von der Besegelung und dem Nutzungsprofil. Mindestausrüstung für eine 10m-Fahrtenyacht: 2× Fallen-Schäkel (Groß, Genua), 1× Spinnaker-Fall (wenn vorhanden), 1× Spinnaker-Tack, 2× Cunningham/Niederholer. Plus 4–8 Karabiner für Sicherheitsleinen (2 pro Crewmitglied). Plus 2–4 Reserve-Schnappschäkel. Gesamt: 8–15 Schnappschäkel, 4–8 Sicherheitskarabiner.

### F16: Ist der Preisunterschied zwischen Tylaska T12 und Ronstan RF6230 gerechtfertigt?

**Antwort:** Beide haben ähnliche Bruchlasten (ca. 13 kN). Der Tylaska T12 (110–145 EUR) kostet 4–5× so viel wie der Ronstan RF6230 (25–35 EUR). Die Unterschiede: Tylaska ist geschmiedet (Ronstan teilweise gegossen), hat den Anti-Snag-Trigger, wird einzeln proof-load-getestet und hat austauschbare Verschleißteile. Für Regatta: Tylaska ist die klar bessere Wahl. Für Fahrt bei moderater Nutzung: Ronstan ist ausreichend, wenn regelmäßig inspiziert wird.

### F17: Kann Kälte meinen Schnappschäkel blockieren?

**Antwort:** Ja. In Gefriertemperaturen kann Wasser im Mechanismus gefrieren und den Trigger blockieren. Prävention: Vor Frostperioden Mechanismus mit wasserverdrängendem Schmiermittel behandeln (WD-40, dann Teflon-Spray). Enteisen: Warmes (nicht heißes!) Süßwasser über den Mechanismus gießen. NICHT mit Gewalt am Trigger ziehen — Bruchgefahr.

### F18: Darf ich einen Schnappschäkel mit der Flex aufschneiden, wenn er klemmt?

**Antwort:** Im Notfall: Ja, wenn das Segel oder Fall sofort geborgen werden muss und keine andere Möglichkeit besteht. ACHTUNG: Splittergefahr, Metallstaub, und der Schäkel steht unter Last — IMMER Schutzbrille. Besser: Leine oberhalb des Schäkels kappen (schneller, sicherer) und den Schäkel später am Boden entfernen.

### F19: Was bedeutet „daN" als Einheit bei Wichard?

**Antwort:** daN = Dekanewton = 10 Newton ≈ 1 kg Gewichtskraft. Wichard gibt die Bruchlast traditionell in daN an (französische Konvention). Umrechnung: 100 daN = 1 kN = ca. 100 kg Gewichtskraft. Beispiel: Wichard 2672 mit 1.200 daN = 12 kN = Bruchlast ca. 1.200 kg.

### F20: Warum haben manche Schnappschäkel zwei Augen (Bügel und Auge)?

**Antwort:** Das obere Auge (Eye) ist die Befestigung am Fall oder Beschlag — es nimmt die Zuglast auf. Der untere Bügel (Bow) ist das öffenbare Element, in das die Leine oder das Segelauge eingehängt wird. Die Last wird vom Bügel durch den Verriegelungsmechanismus und den Drehpunkt in den Körper und dann über das Auge in das Fall übertragen.

### F21: Gibt es Schnappschäkel aus Kunststoff?

**Antwort:** Ja, für Anwendungen mit sehr geringer Last (z.B. Flaggenleinen, Sonnensegel, Persenning-Befestigung). Kunststoff-Schnappschäkel (POM/Delrin oder Nylon) haben typisch eine Bruchlast von 0,5–2 kN und sind NICHT für sicherheitskritische oder strukturelle Anwendungen geeignet. Vorteil: Keine Korrosion, kein Kratzer auf Gelcoat, sehr günstig.

### F22: Wie befestige ich einen Schnappschäkel richtig am Fall?

**Antwort:** Drei Methoden: 1) Verspleißt: Die Fallschlaufe wird durch das Schäkelauge gespleißt (Brummel-Spleiß oder Augspleiß). Stärkste Verbindung, aber nicht schnell lösbar. 2) Schäkel-in-Schäkel: Ein D-Schäkel verbindet Fall-Auge und Schnappschäkel-Auge. Einfach, aber zusätzliches Verbindungselement. 3) Soft-Attachment: Dyneema-Loop durch Schäkelauge und Fall-Auge. Leicht, aber Dyneema altert.

### F23: Mein Wirbel-Schnappschäkel quietscht — ist das ein Problem?

**Antwort:** Quietschen zeigt Trockenreibung im Wirbel an — er ist nicht ausreichend geschmiert. Kurzfristig kein Sicherheitsproblem, aber erhöhter Verschleiß. Behebung: Teflon-Spray oder Silikonöl in den Wirbel einbringen, dann mehrfach drehen. Wenn das Quietschen nach Schmierung wiederkehrt: Wirbel prüfen, möglicherweise ist die Lagerfläche korrodiert.

### F24: Was ist der Unterschied zwischen „Snap Shackle" und „Piston Hank"?

**Antwort:** Ein Piston Hank (Kolbenkarabiner) ist ein spezieller Karabiner für die Befestigung von Vorsegeln am Vorstag. Er hat einen federbelasteten Kolben, der über das Vorstag schnappt. Ein Snap Shackle ist ein allgemeiner Schnellverschluss für Fallen, Sheets und andere Verbindungen. Beide haben einen Federmechanismus, aber völlig unterschiedliche Anwendungen und Konstruktionen.

### F25: Kann ich Schnappschäkel verschiedener Hersteller an derselben Yacht mischen?

**Antwort:** Ja, technisch kein Problem. Allerdings erschwert ein Mischbestand die Ersatzteilhaltung und Wartung. Empfehlung: Ein Primärhersteller für alle Schnappschäkel (z.B. Wichard oder Tylaska), ein Primärhersteller für alle Sicherheitskarabiner (z.B. Wichard oder Kong). Reserve-Schnappschäkel in den 2–3 am häufigsten verwendeten Größen mitführen.

---

## 10. Glossar

### A

**Accidental Opening (Unbeabsichtigtes Öffnen)**
Das Öffnen eines Schnappschäkels ohne manuelle Betätigung des Triggers, verursacht durch Leinenkontakt, Stoß, Vibration oder Federermüdung. Das zentrale Sicherheitsproblem bei Schnappschäkeln.

**Allen Key (Inbusschlüssel)**
Sechskant-Stiftschlüssel, benötigt für einige Schnappschäkel-Wartungsarbeiten (Federtausch bei Tylaska).

**Anti-Snag-Design**
Konstruktionsprinzip, bei dem der Trigger so versenkt oder geschützt ist, dass er nicht durch Leinen, Segel oder zufälligen Kontakt ausgelöst werden kann.

**Auto-Lock**
Selbstverriegelnder Karabiner-Verschlussmechanismus. Das Gate verriegelt automatisch nach dem Schließen. Zum Öffnen: Hülse drehen und Gate drücken.

### B

**Bow (Bügel)**
Der bewegliche Teil des Schnappschäkels, der durch den Trigger geöffnet wird und in den die Leine oder das Auge eingehängt wird.

**Breaking Load / BL (Bruchlast)**
Die maximale Last in kN oder daN, bei der ein Beschlag unter statischer Prüfung versagt. Nicht identisch mit der sicheren Arbeitslast.

### C

**Carabiner / Karabiner**
Schnellverschluss mit federbelastetem Gate. In der Marine-Anwendung primär für Sicherheitsleinen (Safety Tether) und leichte Befestigungen.

**CE-Kennzeichnung**
Europäische Konformitätskennzeichnung, die die Einhaltung relevanter EU-Richtlinien bestätigt.

**Chafe (Scheuern)**
Mechanischer Abrieb an Leinen, Dyneema-Schlaufen oder Beschlägen durch wiederholten Kontakt.

**Creep (Kriechen)**
Langsame plastische Verformung unter Dauerlast, relevant für Dyneema-Schlaufen an Soft-Attachment-Schnappschäkeln.

### D

**daN (Dekanewton)**
10 Newton ≈ 1 kg Gewichtskraft. Von Wichard und anderen französischen Herstellern als Einheit für die Bruchlast verwendet.

**Dyneema**
Ultra-hochmolekulares Polyethylen (UHMWPE), Markenname von DSM. Verwendet für Soft-Attachment-Schlaufen an Schnappschäkeln. Extrem hohe Zugfestigkeit bei geringem Gewicht, aber empfindlich gegen UV und Hitze.

### E

**Eye (Auge)**
Die geschlossene Öse am oberen Ende eines Schnappschäkels, die die Verbindung zum Fall, Beschlag oder Wirbel herstellt.

### F

**Fatigue (Ermüdung)**
Materialversagen durch wiederholte zyklische Belastung unterhalb der statischen Bruchlast. Kritisch bei Federn und Bolzen im Trigger-Mechanismus.

**Fixed Eye (Festes Auge)**
Ein nicht-drehbares, fest mit dem Schäkelkörper verbundenes Auge. Im Gegensatz zum Wirbel-Auge.

**Forging (Schmieden)**
Umformverfahren, bei dem Metall unter hohem Druck in eine Form gepresst wird. Ergibt die höchste Festigkeit bei Schnappschäkeln.

**Fretting (Reibkorrosion)**
Korrosion an Kontaktflächen, die unter Last geringfügig gegeneinander bewegt werden. Typisch am Bügel-Drehpunkt.

### G

**Galvanic Corrosion (Galvanische Korrosion)**
Beschleunigte Korrosion durch elektrochemische Reaktion zwischen zwei unterschiedlichen Metallen in einem Elektrolyten (Salzwasser).

**Gate (Tor)**
Der bewegliche Verschlussteil eines Karabiners. Wird durch eine Feder in der geschlossenen Position gehalten.

### H

**HMS-Karabiner**
Birnenförmiger Karabiner (Halbmastwurf-Sicherung), ursprünglich aus dem Bergsport. In der Marine für Sicherheitsleinen mit breitem Gate.

### I

**Investment Casting (Feinguss)**
Gießverfahren mit Wachsausschmelzmodell. Ermöglicht komplexe Geometrien, aber geringere Festigkeit als Schmieden.

**ISO 12401**
Internationale Norm für Sicherheitsgeschirre und -leinen auf Sportbooten. Definiert Anforderungen an Karabiner für Safety Tether.

### J

**Jackline (Strecktau / Sicherheitsleine)**
Leine oder Gurtband, das längs über das Deck gespannt wird und als Ankerpunkt für Safety Tether dient.

### K

**kN (Kilonewton)**
1.000 Newton ≈ 100 kg Gewichtskraft. Standardeinheit für Bruchlasten und Arbeitslasten im Marine-Bereich.

### L

**Latch Point (Verriegelungspunkt)**
Der Punkt, an dem der Bügel im geschlossenen Zustand am Schäkelkörper einrastet. Zweithöchste Belastung im Schäkel.

**Load-Independent Trigger**
Trigger-Mechanismus (Tylaska-Patent), bei dem die zum Auslösen erforderliche Kraft unabhängig von der am Schäkel anliegenden Last ist.

**Locking Carabiner (Verriegelnder Karabiner)**
Karabiner mit zusätzlichem Verriegelungsmechanismus (Screw-Lock, Auto-Lock, Tri-Lock), der das Gate gegen unbeabsichtigtes Öffnen sichert.

### M

**Marine Grade (Marine-Qualität)**
Informelle Bezeichnung für Materialien und Beschläge, die für den Einsatz in Salzwasserumgebung geeignet sind. Keine normierte Definition.

### N

**Non-Locking Carabiner**
Karabiner ohne Verriegelungsmechanismus. NICHT für sicherheitskritische Anwendungen (Safety Tether) zugelassen.

### O

**OSR (Offshore Special Regulations)**
Sicherheitsvorschriften von World Sailing (ehemals ISAF) für Hochsee-Regatten. Definieren Mindestanforderungen an Sicherheitsausrüstung.

### P

**Piston Hank (Kolbenkarabiner)**
Spezieller Karabiner für die Befestigung von Vorsegeln am Vorstag. Nicht mit Schnappschäkeln zu verwechseln.

**Pivot Point (Drehpunkt)**
Der Punkt, um den der Bügel des Schnappschäkels schwenkt. Höchste Belastung im Schäkel (Scherkraft).

**Plunger Pin (Kolbenbolzen)**
Federbelasteter Bolzen als Auslösemechanismus bei Plunger-Pin-Schnappschäkeln.

**Proof Load (Prüflast)**
Last, mit der jeder Schäkel vor der Auslieferung belastet wird, um sicherzustellen, dass keine plastische Verformung auftritt. Typisch: 50% BL.

**PREN (Pitting Resistance Equivalent Number)**
Kennzahl für die Lochfraß-Beständigkeit von Edelstahl. PREN = %Cr + 3,3 × %Mo + 16 × %N. 316L hat PREN ≈ 24.

### R

**Reflex Snap Shackle**
Harken-Bezeichnung für ihre Hochleistungs-Schnappschäkel mit optimiertem Trigger-Mechanismus.

### S

**Safety Tether (Sicherheitsleine)**
Leine mit Karabinern an beiden Enden, die das Sicherheitsgeschirr (Harness) einer Person mit der Jackline oder einem festen Deckspunkt verbindet.

**Screw-Lock (Schraubverschluss)**
Verriegelungsmechanismus bei Karabinern, bei dem eine Schraubhülse manuell über das Gate gedreht wird.

**Shock Load (Stoßlast)**
Plötzlich auftretende Last, die ein Vielfaches der statischen Last betragen kann. Typisch bei Spinnaker-Füllung, Fallsturz in Safety Tether.

**Snap Shackle (Schnappschäkel)**
Schnelllösbarer Schäkel mit federbelastetem Trigger-Mechanismus.

**Soft-Attachment**
Verbindungstechnik, bei der das metallische Auge eines Schnappschäkels durch eine textile Schlaufe (Dyneema) ersetzt wird.

**Spring (Feder)**
Elastisches Element, das den Bügel (bei Schnappschäkeln) oder das Gate (bei Karabinern) in der geschlossenen Position hält.

**Swivel (Wirbel)**
Drehgelenk zwischen Auge und Schäkelkörper, das 360°-Rotation ermöglicht und Torsion verhindert.

**SWL (Safe Working Load / Sichere Arbeitslast)**
Maximale Last für den regulären Betrieb. SWL = BL / Sicherheitsfaktor.

### T

**Tack (Hals)**
Der untere vordere Punkt eines Segels. Bei Spinnaker und Gennaker oft mit Schnappschäkel am Bugbeschlag befestigt.

**Tri-Lock**
Dreifach-Verriegelungsmechanismus bei Karabinern: Hülse heben, drehen, Gate drücken. Höchste Sicherheit.

**Trigger**
Der Auslösemechanismus eines Schnappschäkels — Hebel, Kolben oder Druckknopf.

**Triplebar**
Patentiertes Wichard-Sicherheitssystem mit drei ineinandergreifenden Hebelsegmenten.

**Tylaska**
US-amerikanischer Hersteller von High-Performance-Schnappschäkeln (Bristol, Rhode Island).

### U

**UHMWPE (Ultra High Molecular Weight Polyethylene)**
Werkstoff für Hochleistungsfasern (Dyneema, Spectra). Verwendet für Soft-Attachment-Schlaufen.

### W

**Whipping (Bändsel)**
Umwicklung mit dünnem Garn oder Tape zum Schutz des Triggers gegen unbeabsichtigtes Auslösen.

**Wichard**
Französischer Hersteller geschmiedeter Edelstahl-Beschläge (Thiers, Auvergne). Seit 1919.

**Wire Gate (Draht-Gate)**
Karabiner-Gate aus Draht statt massivem Metall. Leichter und weniger vereisungsanfällig.

**Wöhler-Kurve (S-N Curve)**
Diagramm, das die Anzahl der Lastzyklen bis zum Versagen in Abhängigkeit von der Lastamplitude darstellt.

---

## 11. Schnell-Referenz

### 11.1 Schnappschäkel-Auswahl nach Anwendung

| Anwendung | Empfohlener Typ | Mindest-SWL | Empfohlene Marken |
|-----------|-----------------|-------------|-------------------|
| Spinnaker-Fall (Jolle) | Standard Snap | 1,5 kN | Allen, Ronstan |
| Spinnaker-Fall (Fahrt 10m) | Swivel Snap / Trigger Release | 3,0 kN | Wichard, Tylaska T12 |
| Spinnaker-Fall (Regatta 13m) | Trigger Release Swivel | 5,0 kN | Tylaska T20-S |
| Spinnaker-Tack | Standard/Plunger Snap | 2,0 kN | Wichard, Harken |
| Gennaker-Tack | Standard Snap | 2,5 kN | Wichard, Tylaska T8/T12 |
| Großsegel-Fall | Fixed Eye Snap + Pin | 4,0 kN | Wichard, Harken |
| Genua-Fall | Standard Snap + Pin | 3,0 kN | Wichard, Harken |
| Niederholer/Vang | Fixed Eye Snap | 3,0 kN | Wichard, Ronstan |
| Cunningham | Plunger Pin Snap | 1,5 kN | Tylaska T5, Allen |
| Lazy Jacks | Non-Lock Karabiner | 1,0 kN | Kong, Ronstan |
| Safety Tether | Locking Carabiner ISO 12401 | ISO 12401 | Wichard, Kong |
| Jackline-Befestigung | D-Schäkel oder Snap | 5,0 kN | Wichard |
| Beiboot-Schleppleine | Swivel Snap | 3,0 kN | Wichard, Ronstan |

### 11.2 Schnappschäkel-Mindestgrößen nach Bootsklasse

| Bootsklasse | Fallen-Schäkel SWL (kN) | Spinnaker-Schäkel SWL (kN) | Safety Karabiner |
|-------------|--------------------------|----------------------------|------------------|
| Jolle (4–8m) | 1,0–2,0 | 1,5–2,5 | ISO 12401 |
| Fahrtensegler (8–14m) | 2,5–4,0 | 3,0–5,0 | ISO 12401 |
| Performance (10–16m) | 3,5–6,0 | 5,0–8,0 | ISO 12401 |
| Blauwasser (12–18m) | 3,0–5,0 | 4,0–7,0 | ISO 12401 |
| Regatta (8–20m) | 3,0–8,0 | 4,0–10,0 | ISO 12401 |
| Superyacht (18m+) | 6,0–15,0 | 8,0–20,0 | ISO 12401 |

### 11.3 Wartungsintervalle

| Maßnahme | Intervall | Hinweis |
|----------|-----------|---------|
| Süßwasserspülung | Nach jedem Salz-Segeltag | Alle beweglichen Teile |
| Schmierung (Teflon/Silikon) | Alle 4–6 Wochen (Saison) | Trigger, Wirbel, Gate |
| Sichtprüfung | Monatlich (Saison) | Risse, Korrosion, Verformung |
| Funktionstest | Monatlich (Saison) | Trigger, Feder, Gate |
| Vollinspektion | Saisonbeginn | Federspannung, Verschleiß, BL |
| Masttop-Fallen-Schäkel | Bei Mastinspektion | Fallen-Schäkel, Wirbel |
| Safety Tether Karabiner | Vor jeder Nachtfahrt/Starkwind | Gate, Lock, Funktion |
| Austausch (Fahrt) | Alle 8–10 Jahre | Oder bei Befund |
| Austausch (Regatta) | Alle 3–5 Jahre | Oder bei Befund |
| Dyneema-Schlaufe (Soft-Att.) | Alle 1–3 Saisons | UV, Abrieb prüfen |

---

## ANHANG A — Fallstudien

### Fallstudie A1: Spinnaker-Verlust bei Langstreckenregatta — Trigger-Auslösung durch Sheet

**Yacht:** 12m One-Design-Regattayacht, Baujahr 2020
**Revier:** Nordsee, Langstreckenregatta, 25–30 kn Wind
**Schnappschäkel:** Standard-Snap (nicht Tylaska, nicht Triplebar), BL 15 kN
**Vorfall:** Beim Spinnaker-Bergen wickelte sich die losgehende Spinnaker-Sheet um den Trigger des Fall-Schnappschäkels. Der Zug der Sheet löste den Trigger aus. Der 80m² Spinnaker löste sich vom Fall und flog ins Wasser.
**Schaden:** Spinnaker (Wert 4.500 EUR) konnte geborgen werden, aber mit Rissen. Reparaturkosten: 1.200 EUR. Zeitverlust im Rennen: 45 Minuten.
**Ursachenanalyse:**
- Schnappschäkel ohne Anti-Snag-Design
- Trigger-Ausrichtung zur Sheet-Seite
- Keine Sicherung des Triggers (kein Pin, kein Tape)
- Crew-Training: Vorschiffs-Mann hätte Sheet klarer führen müssen
**Maßnahmen:**
1. Austausch gegen Tylaska T12 (Anti-Snag-Trigger)
2. Montageausrichtung: Trigger immer nach Lee (weg von den Sheets)
3. Crew-Briefing: Sheet-Handling beim Bergen

**AYDI-Relevanz:** Pipeline B (Visual) — Schnappschäkeltyp und Montageausrichtung können auf Deckfotos bewertet werden. Confidence: visual_medium.

### Fallstudie A2: Genua-Fall löst sich bei Nachtfahrt

**Yacht:** 14m Fahrtenyacht, Baujahr 2012
**Revier:** Biskaya, Nachtfahrt, 28 kn Wind, 3m Welle
**Schnappschäkel:** Wichard Standard 2672, BL 12 kN, 8 Jahre alt
**Vorfall:** Um 03:00 Uhr löste sich das Genua-Fall am Masttop. Die 28m² Genua schlug unkontrolliert. Zwei Crewmitglieder wurden geweckt und benötigten 20 Minuten, um die Genua zu sichern.
**Schaden:** Genua-Vorliek gerissen (Reparatur: 600 EUR), Salingleder beschädigt (150 EUR). Kein Personenschaden.
**Ursachenanalyse:**
- Schäkel war 8 Jahre alt, nie gewartet
- Federspannung stark reduziert (< 0,5 kg Auslösekraft)
- Vibration des Falls am Masttop + Rigg-Schwingung löste Trigger aus
- Kein Sicherungsstift verwendet
**Maßnahmen:**
1. Alle Fallen-Schnappschäkel erneuert (Wichard Triplebar 2996)
2. Sicherungsstifte an allen Fallen-Schäkeln
3. Wartungsintervall eingeführt: jährliche Inspektion Masttop

**AYDI-Relevanz:** Pipeline A (Structured) — Alter und Wartungszustand als Risikofaktor. Pipeline C (Text) — Service-Report dokumentiert Vorfall. Confidence: documented.

### Fallstudie A3: Safety Tether Karabiner öffnet sich — MOB-Situation

**Yacht:** 11m Fahrtenyacht, Baujahr 2015
**Revier:** Englischer Kanal, Nachtfahrt, 22 kn Wind, 2m Welle
**Karabiner:** Non-Locking Karabiner (NICHT ISO 12401), aus dem Bergsport
**Vorfall:** Rudergänger wurde von einer Welle erfasst und gegen die Reling geworfen. Der Karabiner seiner Sicherheitsleine öffnete sich durch den Kontakt mit dem Relingstrang. Der Rudergänger wurde über Bord gespült. Die Crew konnte ihn nach 12 Minuten bergen.
**Schaden:** Hypothermie-Behandlung im Krankenhaus, emotionales Trauma bei der gesamten Crew.
**Ursachenanalyse:**
- Non-Locking-Karabiner: Gate öffnete sich durch Kontakt mit Relingstrang
- Karabiner war nicht ISO-12401-konform
- Crew war nicht über die Unterschiede zwischen Bergsport- und Marine-Karabinern informiert
**Maßnahmen:**
1. Alle Karabiner durch ISO-12401-konforme Modelle ersetzt (Wichard 2491, Auto-Lock)
2. Crew-Briefing über Sicherheitsleinen-Anforderungen
3. Regelmäßige Übung von MOB-Manövern

**AYDI-Relevanz:** Pipeline C (Text) — MOB-Bericht. Pipeline A — Karabiner-Typ als kritischer Sicherheitsparameter. Confidence: documented.

### Fallstudie A4: Tylaska T5 — Federtausch nach 4 Saisons Regatta

**Yacht:** 8m Sportboot/Sportskeelboat, Regatta-intensiv (60+ Regatta-Tage/Saison)
**Schnappschäkel:** Tylaska T5, BL 5,3 kN, am Cunningham
**Vorfall:** Bei der saisonalen Inspektion wurde festgestellt, dass die Trigger-Feder nur noch ca. 0,5 kg Widerstand bot (Neuzustand: 1,5–2 kg).
**Schaden:** Kein Vorfall, präventive Erkennung.
**Maßnahme:** Feder getauscht (Tylaska Replacement Spring Kit, ca. 15 EUR). Trigger-Funktion danach wie neu.
**Erkenntnis:** Tylaska-Schäkel sind servicefreundlich. Feder-Austausch als routinemäßige Wartung alle 3–5 Saisons bei intensiver Nutzung.

**AYDI-Relevanz:** Pipeline A — Wartungsintervall-Empfehlung. Confidence: measured.

### Fallstudie A5: Galvanische Korrosion — Edelstahl-Schnappschäkel an Aluminium-Mastbeschlag

**Yacht:** 10m Fahrtenyacht, Aluminium-Mast
**Schnappschäkel:** Standard 316L Edelstahl, direkt an Aluminium-Mastbeschlag montiert
**Zeitraum:** 3 Saisons
**Befund:** Starke Korrosion am Aluminium-Mastbeschlag rund um den Schäkel-Kontaktbereich. Weiße Aluminiumoxid-Ablagerungen, Materialabtrag am Aluminium.
**Ursachenanalyse:** Galvanisches Element 316L Edelstahl ↔ Aluminium in Salzwasser. Edelstahl ist deutlich edler als Aluminium → beschleunigter Abtrag am Aluminium.
**Maßnahmen:**
1. Isolierscheibe (Nylon) zwischen Schäkel und Mastbeschlag
2. Regelmäßige Inspektion des Aluminium-Beschlags
3. Teflon-Beschichtung auf dem Aluminium-Beschlag

**AYDI-Relevanz:** Pipeline B (Visual) — Korrosionsspuren visuell erkennbar. Confidence: visual_high.

### Fallstudie A6: Wirbel-Schnappschäkel blockiert — Spinnaker-Verdrillung

**Yacht:** 13m Cruiser-Racer, Baujahr 2018
**Schnappschäkel:** Wichard Swivel Snap 2475, BL 12 kN, am Spinnaker-Fall
**Vorfall:** Während einer Regatta drehte sich der Wirbel nicht mehr frei. Das Spinnaker-Fall verdrillte sich und der Spinnaker konnte nicht sauber gefüllt werden. Beim Bergeversuch verdrehte sich das Fall weiter und der Spinnaker wickelte sich um das Vorstag.
**Schaden:** Spinnaker-Beschädigung (Reparatur 800 EUR), Zeitverlust 30 Minuten.
**Ursachenanalyse:**
- Wirbel war seit 2 Jahren nicht geschmiert worden
- Salzkristalle im Wirbelgelenk
- Keine Wartung nach Winterlager (Schäkel trocken eingelagert ohne vorherige Schmierung)
**Maßnahmen:**
1. Wirbel demontiert, gereinigt, geschmiert
2. Wartungsplan: Wirbel alle 4 Wochen mit Teflon-Spray schmieren
3. Vor Einwinterung: Wirbel gründlich schmieren

**AYDI-Relevanz:** Pipeline B (Visual) — Verdrehtes Fall als Indikator sichtbar. Confidence: visual_medium.

### Fallstudie A7: Soft-Attachment-Versagen — Dyneema-Schlaufe bricht

**Yacht:** 11m Regattayacht, Sportboot-Klasse
**Schnappschäkel:** Soft-Attachment Snap Shackle, BL 10 kN, am Gennaker-Tack
**Vorfall:** Bei einem Gennaker-Set riss die Dyneema-Schlaufe des Soft-Attachment-Schnappschäkels. Der Gennaker-Tack löste sich und der Gennaker flog unkontrolliert.
**Schaden:** Gennaker-Riss (Reparatur 500 EUR), kein Personenschaden.
**Ursachenanalyse:**
- Dyneema-Schlaufe war 4 Saisons alt und hatte sichtbare UV-Degradation
- Schlaufe zeigte Verfärbung (weiß statt gelb) und Ausfaserung
- Keine Inspektion der Schlaufe durchgeführt
**Maßnahmen:**
1. Alle Dyneema-Schlaufen erneuert
2. Austausch-Intervall: Jede Saison für Regatta, alle 2 Saisons für Fahrt
3. UV-Schutz: Schlaufen nach Gebrauch abdecken

**AYDI-Relevanz:** Pipeline B (Visual) — UV-Degradation der Dyneema visuell erkennbar. Confidence: visual_high.

### Fallstudie A8: Karabiner-Gate-Versagen im Winterlager

**Yacht:** 15m Blauwasseryacht, Winterlager in Mittelmeer-Marina
**Karabiner:** Wichard 2490 Safety Tether Karabiner, ISO 12401, 6 Jahre alt
**Befund:** Bei der saisonalen Inspektion schließt das Gate nicht mehr selbstständig. Gate-Feder ist gebrochen.
**Ursachenanalyse:**
- Gate-Feder aus Edelstahldraht, 6 Jahre alt
- Kombination aus Salzwasser-Exposition und Alterung
- Keine Winterlager-Schmierung durchgeführt
**Maßnahmen:**
1. Sofortiger Austausch beider Safety Tether Karabiner
2. Ersatzkarabiner an Bord als Reserve
3. Winterlager-Checkliste: Alle Karabiner schmieren und Funktion prüfen

**AYDI-Relevanz:** Pipeline A — Alter als Risikofaktor für Safety Tether. Confidence: measured.

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

### B.1 Schnappschäkel-Datenmodell

```python
"""
AYDI Snap Shackle and Carabiner Data Models
Module: 12_04_snap_shackle_carabiner
"""

from enum import Enum
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


class SnapShackleType(str, Enum):
    """Snap shackle type classification."""
    STANDARD = "standard"
    SWIVEL = "swivel"
    FIXED_EYE = "fixed_eye"
    PLUNGER_PIN = "plunger_pin"
    TRIGGER_RELEASE = "trigger_release"
    SOFT_ATTACHMENT = "soft_attachment"


class CarabinerType(str, Enum):
    """Carabiner type classification."""
    NON_LOCKING = "non_locking"
    SCREW_LOCK = "screw_lock"
    AUTO_LOCK = "auto_lock"
    TRI_LOCK = "tri_lock"


class TriggerMechanism(str, Enum):
    """Trigger mechanism type."""
    LEVER = "lever"
    PLUNGER = "plunger"
    TRIPLEBAR = "triplebar"
    GATE_SPRING = "gate_spring"
    GATE_WIRE = "gate_wire"


class Material(str, Enum):
    """Material classification for snap shackles."""
    STAINLESS_316L = "316l"
    STAINLESS_17_4PH = "17_4ph"
    TITANIUM_GR5 = "ti_gr5"
    BRONZE = "bronze"
    ALUMINUM = "aluminum"
    POM = "pom"


class Manufacturer(str, Enum):
    """Snap shackle manufacturer."""
    WICHARD = "wichard"
    TYLASKA = "tylaska"
    HARKEN = "harken"
    RONSTAN = "ronstan"
    KONG = "kong"
    ALLEN = "allen_brothers"
    SELDEN = "selden"
    OTHER = "other"


class Application(str, Enum):
    """Snap shackle application area."""
    SPINNAKER_HALYARD = "spinnaker_halyard"
    SPINNAKER_TACK = "spinnaker_tack"
    GENNAKER_TACK = "gennaker_tack"
    MAIN_HALYARD = "main_halyard"
    GENOA_HALYARD = "genoa_halyard"
    CUNNINGHAM = "cunningham"
    VANG = "vang"
    LAZY_JACKS = "lazy_jacks"
    SAFETY_TETHER = "safety_tether"
    JACKLINE = "jackline"
    DINGHY_TOWLINE = "dinghy_towline"
    OTHER = "other"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SnapShackleSpec(BaseModel):
    """Technical specification for a snap shackle."""

    model_config = {"from_attributes": True}

    manufacturer: Manufacturer
    model_name: str = Field(..., description="Model name/number, e.g. 'T12', '2672'")
    part_number: Optional[str] = Field(None, description="Manufacturer part number")
    shackle_type: SnapShackleType
    trigger_mechanism: TriggerMechanism

    # Materials
    body_material: Material
    trigger_material: Optional[Material] = None
    spring_material: Optional[str] = None

    # Dimensions (mm)
    overall_length_mm: float = Field(..., ge=20, le=300)
    bow_opening_mm: Optional[float] = Field(None, ge=5, le=50)
    eye_bore_mm: Optional[float] = Field(None, ge=3, le=25)
    pin_diameter_mm: Optional[float] = Field(None, ge=3, le=20)

    # Load ratings (kN)
    breaking_load_kn: float = Field(..., ge=0.5, le=200)
    safe_working_load_kn: float = Field(..., ge=0.1, le=50)
    safety_factor: float = Field(default=4.0, ge=2.0, le=10.0)

    # Trigger
    trigger_force_n: Optional[float] = Field(None, ge=5, le=100, description="Force required to operate trigger (N)")
    load_independent_trigger: bool = Field(default=False)
    anti_snag_design: bool = Field(default=False)

    # Weight
    weight_g: float = Field(..., ge=5, le=1000)

    # Pricing
    price_eur_min: Optional[float] = Field(None, ge=1, le=2000)
    price_eur_max: Optional[float] = Field(None, ge=1, le=2000)

    # Manufacturing
    forged: bool = Field(default=False)
    proof_load_tested: bool = Field(default=False)
    serialized: bool = Field(default=False)

    # Certification
    ce_marked: bool = Field(default=False)
    iso_12401: bool = Field(default=False)


class CarabinerSpec(BaseModel):
    """Technical specification for a marine carabiner."""

    model_config = {"from_attributes": True}

    manufacturer: Manufacturer
    model_name: str
    part_number: Optional[str] = None
    carabiner_type: CarabinerType

    # Materials
    body_material: Material
    gate_material: Optional[Material] = None

    # Dimensions (mm)
    overall_length_mm: float = Field(..., ge=40, le=200)
    gate_opening_mm: float = Field(..., ge=10, le=40)

    # Load ratings (kN)
    breaking_load_major_axis_kn: float = Field(..., ge=5, le=100)
    breaking_load_minor_axis_kn: Optional[float] = Field(None, ge=2, le=50)
    breaking_load_gate_open_kn: Optional[float] = Field(None, ge=2, le=50)

    # Weight
    weight_g: float = Field(..., ge=20, le=500)

    # Pricing
    price_eur_min: Optional[float] = Field(None, ge=1, le=500)
    price_eur_max: Optional[float] = Field(None, ge=1, le=500)

    # Certification
    ce_marked: bool = Field(default=False)
    iso_12401: bool = Field(default=False)
    en_362: bool = Field(default=False)

    # Cycle test
    cycle_test_count: Optional[int] = Field(None, ge=0, le=100000)
    salt_spray_hours: Optional[int] = Field(None, ge=0, le=5000)


class SnapShackleCondition(BaseModel):
    """Assessment of a snap shackle's condition."""

    model_config = {"from_attributes": True}

    shackle_id: Optional[str] = None
    location: str = Field(..., description="Location on yacht, e.g. 'main_halyard_masthead'")
    application: Application

    # Identification
    manufacturer: Optional[Manufacturer] = None
    model_name: Optional[str] = None
    estimated_age_years: Optional[float] = None
    installation_date: Optional[date] = None

    # Condition assessment (0-100 scale)
    overall_score: float = Field(..., ge=0, le=100)
    body_condition_score: float = Field(..., ge=0, le=100)
    trigger_condition_score: float = Field(..., ge=0, le=100)
    spring_condition_score: float = Field(..., ge=0, le=100)
    corrosion_score: float = Field(..., ge=0, le=100, description="100 = no corrosion, 0 = severe")
    swivel_condition_score: Optional[float] = Field(None, ge=0, le=100)

    # Specific findings
    trigger_functional: bool = Field(default=True)
    spring_adequate: bool = Field(default=True)
    accidental_opening_risk: str = Field(default="low", pattern="^(low|medium|high|critical)$")
    bow_deformation: bool = Field(default=False)
    pitting_depth_mm: Optional[float] = Field(None, ge=0, le=5)
    lateral_play_mm: Optional[float] = Field(None, ge=0, le=5)

    # Recommendation
    action_required: str = Field(
        default="none",
        pattern="^(none|monitor|service|replace_soon|replace_immediately)$"
    )
    replacement_urgency: Optional[str] = Field(
        None,
        pattern="^(not_required|next_season|before_next_trip|immediately)$"
    )
    notes: Optional[str] = None

    # AYDI confidence
    confidence: ConfidenceLevel
    assessment_method: str = Field(
        default="visual",
        pattern="^(visual|measured|documented|estimated)$"
    )


class SafetyTetherAssessment(BaseModel):
    """Assessment of a safety tether system (tether + carabiners)."""

    model_config = {"from_attributes": True}

    # Tether identification
    tether_id: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    tether_length_m: Optional[float] = Field(None, ge=0.5, le=3.0)

    # Carabiner assessment — ship end
    ship_end_carabiner_type: Optional[CarabinerType] = None
    ship_end_iso_12401: bool = Field(default=False)
    ship_end_gate_functional: bool = Field(default=True)
    ship_end_lock_functional: bool = Field(default=True)
    ship_end_condition_score: float = Field(default=100, ge=0, le=100)

    # Carabiner assessment — body end
    body_end_carabiner_type: Optional[CarabinerType] = None
    body_end_iso_12401: bool = Field(default=False)
    body_end_gate_functional: bool = Field(default=True)
    body_end_lock_functional: bool = Field(default=True)
    body_end_condition_score: float = Field(default=100, ge=0, le=100)

    # Tether line assessment
    tether_material: Optional[str] = None
    tether_condition_score: float = Field(default=100, ge=0, le=100)
    uv_degradation_visible: bool = Field(default=False)
    chafe_visible: bool = Field(default=False)
    stitching_intact: bool = Field(default=True)

    # Overall compliance
    iso_12401_compliant: bool = Field(default=False)
    overall_score: float = Field(..., ge=0, le=100)
    safety_critical_finding: bool = Field(default=False)
    action_required: str = Field(
        default="none",
        pattern="^(none|monitor|service|replace_soon|replace_immediately)$"
    )
    notes: Optional[str] = None

    # AYDI confidence
    confidence: ConfidenceLevel


class SnapShackleLoadCalculation(BaseModel):
    """Load calculation for snap shackle selection."""

    model_config = {"from_attributes": True}

    application: Application
    boat_class: str = Field(..., description="Boat class, e.g. 'fahrtensegler_12m'")
    boat_length_m: float = Field(..., ge=3, le=50)

    # Sail data
    sail_area_m2: Optional[float] = Field(None, ge=1, le=500)
    sail_type: Optional[str] = None

    # Load calculation
    static_load_kn: Optional[float] = Field(None, ge=0, le=100)
    dynamic_factor: float = Field(default=3.0, ge=1.0, le=12.0)
    max_dynamic_load_kn: Optional[float] = Field(None, ge=0, le=500)

    # Required shackle specs
    required_swl_kn: Optional[float] = Field(None, ge=0, le=100)
    required_bl_kn: Optional[float] = Field(None, ge=0, le=400)
    safety_factor: float = Field(default=4.0, ge=2.0, le=10.0)

    # Recommendations
    recommended_shackles: list[str] = Field(default_factory=list)
    notes: Optional[str] = None

    # AYDI confidence
    confidence: ConfidenceLevel


class SnapShackleFaultPattern(BaseModel):
    """Fault pattern for snap shackle analysis."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., pattern="^F-SS-\\d{2}$")
    fault_name_de: str
    fault_name_en: str
    severity: str = Field(..., pattern="^(info|warning|critical|safety_critical)$")

    # Visual detection
    visual_detectability: ConfidenceLevel
    visual_indicators: list[str] = Field(default_factory=list)

    # Causes
    causes: list[str] = Field(default_factory=list)

    # Impact
    impact_description: str
    safety_impact: bool = Field(default=False)

    # Remediation
    immediate_action: Optional[str] = None
    long_term_action: Optional[str] = None
    replacement_required: bool = Field(default=False)

    # AYDI mapping
    aydi_module: str = Field(default="materials")
    aydi_zone: Optional[str] = None
```

### B.2 Analyse-Funktionen

```python
"""
AYDI Snap Shackle Analysis Functions
Module: 12_04_snap_shackle_analysis
"""

from typing import Optional


def calculate_halyard_load(
    sail_area_m2: float,
    wind_speed_kn: float,
    dynamic_factor: float = 3.0,
    drag_coefficient: float = 1.2,
    halyard_angle_deg: float = 15.0,
) -> dict:
    """
    Calculate halyard load for snap shackle sizing.

    Args:
        sail_area_m2: Sail area in square meters.
        wind_speed_kn: Wind speed in knots.
        dynamic_factor: Dynamic load multiplier (2.0-4.0 for spinnaker).
        drag_coefficient: Aerodynamic drag coefficient.
        halyard_angle_deg: Halyard angle from vertical in degrees.

    Returns:
        Dictionary with static and dynamic load values in kN.
    """
    import math

    air_density = 1.225  # kg/m³
    wind_speed_ms = wind_speed_kn * 0.5144  # knots to m/s

    # Static wind force
    wind_force_n = 0.5 * air_density * wind_speed_ms**2 * sail_area_m2 * drag_coefficient

    # Halyard component (vertical)
    halyard_angle_rad = math.radians(halyard_angle_deg)
    halyard_load_n = wind_force_n * math.sin(halyard_angle_rad)

    # Dynamic load
    dynamic_load_n = halyard_load_n * dynamic_factor

    return {
        "wind_force_kn": round(wind_force_n / 1000, 2),
        "static_halyard_load_kn": round(halyard_load_n / 1000, 2),
        "dynamic_halyard_load_kn": round(dynamic_load_n / 1000, 2),
        "required_swl_kn": round(dynamic_load_n / 1000, 2),
        "required_bl_kn_sf4": round(dynamic_load_n / 1000 * 4, 2),
        "required_bl_kn_sf5": round(dynamic_load_n / 1000 * 5, 2),
        "confidence": "calculated",
    }


def select_snap_shackle(
    application: str,
    required_swl_kn: float,
    boat_class: str,
    prefer_manufacturer: Optional[str] = None,
    swivel_required: bool = False,
    anti_snag_required: bool = False,
    budget: str = "mid",
) -> dict:
    """
    Select appropriate snap shackle based on requirements.

    Args:
        application: Application type (e.g., 'spinnaker_halyard').
        required_swl_kn: Required safe working load in kN.
        boat_class: Boat class identifier.
        prefer_manufacturer: Preferred manufacturer.
        swivel_required: Whether a swivel is needed.
        anti_snag_required: Whether anti-snag design is needed.
        budget: Budget level ('low', 'mid', 'high', 'premium').

    Returns:
        Dictionary with recommended shackle(s) and reasoning.
    """
    if application == "safety_tether":
        return {
            "recommendation": "USE LOCKING CARABINER, NOT SNAP SHACKLE",
            "type": "locking_carabiner",
            "requirement": "ISO 12401 certified",
            "suggested_models": [
                {"manufacturer": "wichard", "model": "2491", "type": "auto_lock"},
                {"manufacturer": "kong", "model": "580.ISO", "type": "iso_12401"},
            ],
            "confidence": "measured",
        }

    # Snap shackle database (simplified)
    shackle_db = [
        {"mfr": "allen", "model": "A4055", "swl": 0.6, "bl": 2.5, "type": "standard", "budget": "low", "swivel": False, "anti_snag": False, "price_min": 6},
        {"mfr": "allen", "model": "A4058", "swl": 1.6, "bl": 6.5, "type": "standard", "budget": "low", "swivel": False, "anti_snag": False, "price_min": 12},
        {"mfr": "ronstan", "model": "RF6220", "swl": 2.2, "bl": 8.9, "type": "standard", "budget": "low", "swivel": False, "anti_snag": False, "price_min": 18},
        {"mfr": "ronstan", "model": "RF6230", "swl": 3.3, "bl": 13.3, "type": "standard", "budget": "low", "swivel": False, "anti_snag": False, "price_min": 25},
        {"mfr": "ronstan", "model": "RF6320", "swl": 2.2, "bl": 8.9, "type": "swivel", "budget": "low", "swivel": True, "anti_snag": False, "price_min": 28},
        {"mfr": "harken", "model": "099", "swl": 2.8, "bl": 11.1, "type": "standard", "budget": "mid", "swivel": False, "anti_snag": False, "price_min": 25},
        {"mfr": "harken", "model": "2100", "swl": 4.5, "bl": 17.8, "type": "standard", "budget": "mid", "swivel": False, "anti_snag": False, "price_min": 35},
        {"mfr": "harken", "model": "2110", "swl": 4.5, "bl": 17.8, "type": "swivel", "budget": "mid", "swivel": True, "anti_snag": False, "price_min": 48},
        {"mfr": "harken", "model": "2151", "swl": 4.5, "bl": 17.8, "type": "trigger_release", "budget": "mid", "swivel": False, "anti_snag": False, "price_min": 72},
        {"mfr": "wichard", "model": "2672", "swl": 3.0, "bl": 12.0, "type": "standard", "budget": "mid", "swivel": False, "anti_snag": False, "price_min": 28},
        {"mfr": "wichard", "model": "2673", "swl": 5.0, "bl": 20.0, "type": "standard", "budget": "mid", "swivel": False, "anti_snag": False, "price_min": 42},
        {"mfr": "wichard", "model": "2996", "swl": 3.0, "bl": 12.0, "type": "trigger_release", "budget": "high", "swivel": False, "anti_snag": True, "price_min": 45},
        {"mfr": "wichard", "model": "2997", "swl": 5.0, "bl": 20.0, "type": "trigger_release", "budget": "high", "swivel": False, "anti_snag": True, "price_min": 58},
        {"mfr": "tylaska", "model": "T8", "swl": 2.2, "bl": 8.9, "type": "trigger_release", "budget": "high", "swivel": False, "anti_snag": True, "price_min": 85},
        {"mfr": "tylaska", "model": "T12", "swl": 3.3, "bl": 13.3, "type": "trigger_release", "budget": "premium", "swivel": False, "anti_snag": True, "price_min": 110},
        {"mfr": "tylaska", "model": "T12-S", "swl": 3.3, "bl": 13.3, "type": "trigger_release", "budget": "premium", "swivel": True, "anti_snag": True, "price_min": 145},
        {"mfr": "tylaska", "model": "T20", "swl": 5.6, "bl": 22.2, "type": "trigger_release", "budget": "premium", "swivel": False, "anti_snag": True, "price_min": 155},
        {"mfr": "tylaska", "model": "T20-S", "swl": 5.6, "bl": 22.2, "type": "trigger_release", "budget": "premium", "swivel": True, "anti_snag": True, "price_min": 195},
        {"mfr": "tylaska", "model": "T30", "swl": 7.8, "bl": 31.1, "type": "trigger_release", "budget": "premium", "swivel": False, "anti_snag": True, "price_min": 210},
    ]

    budget_map = {"low": ["low"], "mid": ["low", "mid"], "high": ["low", "mid", "high"], "premium": ["low", "mid", "high", "premium"]}
    allowed_budgets = budget_map.get(budget, ["low", "mid", "high", "premium"])

    candidates = [
        s for s in shackle_db
        if s["swl"] >= required_swl_kn
        and s["budget"] in allowed_budgets
        and (not swivel_required or s["swivel"])
        and (not anti_snag_required or s["anti_snag"])
        and (prefer_manufacturer is None or s["mfr"] == prefer_manufacturer)
    ]

    if not candidates:
        # Fallback: relax manufacturer preference
        candidates = [
            s for s in shackle_db
            if s["swl"] >= required_swl_kn
            and s["budget"] in allowed_budgets
            and (not swivel_required or s["swivel"])
            and (not anti_snag_required or s["anti_snag"])
        ]

    # Sort by SWL (closest match first), then by price
    candidates.sort(key=lambda s: (s["swl"], s["price_min"]))

    return {
        "application": application,
        "required_swl_kn": required_swl_kn,
        "boat_class": boat_class,
        "recommended": candidates[:3] if candidates else [],
        "alternatives": candidates[3:6] if len(candidates) > 3 else [],
        "note": "Alle Empfehlungen basieren auf SWL-Anforderung und Budget-Klasse.",
        "confidence": "calculated" if candidates else "estimated",
    }


def assess_snap_shackle_condition(
    trigger_functional: bool,
    spring_adequate: bool,
    bow_deformation: bool,
    pitting_depth_mm: float,
    lateral_play_mm: float,
    age_years: float,
    usage_intensity: str = "moderate",
    application: str = "general",
) -> dict:
    """
    Assess the condition of a snap shackle and recommend action.

    Args:
        trigger_functional: Whether the trigger operates correctly.
        spring_adequate: Whether the spring has adequate tension.
        bow_deformation: Whether the bow shows plastic deformation.
        pitting_depth_mm: Depth of pitting corrosion in mm.
        lateral_play_mm: Lateral play of the bow in mm.
        age_years: Age of the shackle in years.
        usage_intensity: Usage level ('light', 'moderate', 'intensive', 'racing').
        application: Application type for severity assessment.

    Returns:
        Dictionary with condition scores and recommendations.
    """
    score = 100.0

    # Immediate disqualifiers
    if bow_deformation:
        return {
            "overall_score": 0,
            "action": "replace_immediately",
            "reason": "Plastische Verformung des Bügels — Überlastung. Restfestigkeit nicht bestimmbar.",
            "safety_critical": True,
            "confidence": "visual_high",
        }

    if not trigger_functional:
        return {
            "overall_score": 10,
            "action": "replace_immediately",
            "reason": "Trigger-Mechanismus funktionsuntüchtig. Schäkel kann nicht geöffnet oder nicht sicher geschlossen werden.",
            "safety_critical": True,
            "confidence": "measured",
        }

    # Pitting deductions
    if pitting_depth_mm >= 0.5:
        score -= 60
    elif pitting_depth_mm >= 0.3:
        score -= 35
    elif pitting_depth_mm >= 0.1:
        score -= 15

    # Spring deductions
    if not spring_adequate:
        score -= 40

    # Lateral play deductions
    if lateral_play_mm >= 1.5:
        score -= 30
    elif lateral_play_mm >= 1.0:
        score -= 15
    elif lateral_play_mm >= 0.5:
        score -= 5

    # Age deductions
    age_limits = {
        "light": 15,
        "moderate": 10,
        "intensive": 7,
        "racing": 4,
    }
    age_limit = age_limits.get(usage_intensity, 10)
    if age_years > age_limit:
        score -= 20
    elif age_years > age_limit * 0.7:
        score -= 10

    score = max(0, score)

    # Determine action
    if score >= 80:
        action = "none"
    elif score >= 60:
        action = "monitor"
    elif score >= 40:
        action = "service"
    elif score >= 20:
        action = "replace_soon"
    else:
        action = "replace_immediately"

    # Safety critical check
    safety_critical = (
        application in ["safety_tether", "spinnaker_halyard"]
        and score < 60
    )

    return {
        "overall_score": round(score),
        "action": action,
        "safety_critical": safety_critical,
        "detail_scores": {
            "trigger": 100 if trigger_functional else 10,
            "spring": 60 if not spring_adequate else 100,
            "corrosion": max(0, 100 - pitting_depth_mm * 200),
            "mechanical_wear": max(0, 100 - lateral_play_mm * 40),
            "age": max(0, 100 - (age_years / age_limit) * 50),
        },
        "confidence": "measured",
    }
```

### B.3 Visuelle Analyse-Prompts

```python
"""
AYDI Visual Analysis Prompts for Snap Shackles and Carabiners
Module: 12_04_visual_prompts
"""

SNAP_SHACKLE_VISUAL_PROMPT = """
Analysiere das Bild eines Schnappschäkels oder Karabiners auf einer Yacht.

Bewerte folgende Aspekte:

1. **Identifikation**:
   - Hersteller (Wichard, Tylaska, Harken, Ronstan, Kong, Allen, Selden, unbekannt)
   - Typ (Standard Snap, Swivel Snap, Fixed Eye, Plunger Pin, Trigger Release, Karabiner)
   - Geschätzte Größe (Länge in mm)
   - Material (Edelstahl, Titan, Aluminium, Kunststoff)

2. **Zustandsbewertung**:
   - Korrosion: keine / leicht / mittel / stark / kritisch
   - Pitting (Lochfraß): ja / nein / nicht beurteilbar
   - Verformung: ja / nein / nicht beurteilbar
   - Trigger-Position: geschlossen / teilweise offen / offen / nicht beurteilbar
   - Gate-Position (Karabiner): geschlossen / offen / nicht beurteilbar

3. **Montage**:
   - Anwendung (Fallen, Spinnaker, Safety Tether, etc.)
   - Montageausrichtung (Trigger-Richtung relativ zu Leinen)
   - Sicherungsstift vorhanden: ja / nein / nicht erkennbar
   - Korrekte Dimensionierung: ja / nein / nicht beurteilbar

4. **Sicherheitsbewertung**:
   - Non-Locking Karabiner als Safety Tether? KRITISCH
   - Schnappschäkel als Safety Tether? KRITISCH
   - Trigger exponiert zu Leinen? WARNUNG
   - Sichtbare Risse oder Brüche? KRITISCH

Antworte in strukturiertem Format mit Confidence-Level für jeden Aspekt.
Wenn ein Aspekt nicht beurteilbar ist, antworte "nicht beurteilbar" mit Begründung.
"""

SNAP_SHACKLE_CONDITION_PROMPT = """
Bewerte den Zustand des abgebildeten Schnappschäkels oder Karabiners.

Fokus auf:
- Korrosionsgrad (0-100, wobei 100 = keine Korrosion)
- Mechanische Beschädigung (Risse, Verformung, Abrieb)
- Trigger/Gate-Funktion (Position, offensichtliche Defekte)
- Allgemeiner Wartungszustand

Für jeden Befund:
- Beschreibung auf Deutsch
- Schweregrad (info / warnung / kritisch / sicherheitskritisch)
- Empfehlung (weiter verwenden / überwachen / bald ersetzen / sofort ersetzen)
- Confidence-Level (visual_high / visual_medium / visual_low / visual_insufficient)

Wenn der Schnappschäkel/Karabiner nicht ausreichend sichtbar ist: 
Antworte "nicht beurteilbar" und erkläre warum.
"""
```

---

## ANHANG C — Normen und Standards

### C.1 Relevante Normen für Schnappschäkel und Karabiner

| Norm | Ausgabe | Titel | Relevanz |
|------|---------|-------|----------|
| ISO 12401 | 2009 | Small craft — Deck safety harness and safety line | Sicherheitsleinen-Karabiner, Mindest-BL 15 kN |
| ISO 9227 | 2017 | Corrosion tests in artificial atmospheres — Salt spray tests | Korrosionsprüfung, 500–2000 h |
| EN 362 | 2004 | PPE against falls from a height — Connectors | Karabiner für persönliche Schutzausrüstung |
| EN 12275 | 2013 | Mountaineering equipment — Connectors | Basis-Norm für Karabiner (Bergsport-Herkunft) |
| ISAF/WS OSR | 2024 | Offshore Special Regulations | Regatta-Sicherheitsanforderungen |
| DNV-GL | div. | Rules for Classification | Superyacht-Zertifizierung |
| RCD 2013/53/EU | 2013 | Recreational Craft Directive | EU-Konformität für Sportboote |
| ISO 15085 | 2003 | Man-overboard prevention and recovery | Reling, Sicherheitsausrüstung |
| ASTM F1774 | 2020 | Standard Specification for Climbing and Mountaineering Carabiners | US-Norm für Kletterkarabiner (Basis für marine Karabiner; NICHT für Schnappschäkel) |

### C.2 ISO 12401 im Detail

**Anwendungsbereich:**
Sicherheitsgeschirre und -leinen für den Einsatz auf Sportbooten. Gilt für alle Karabiner, die als Teil einer Sicherheitsleine (Safety Tether) eingesetzt werden.

**Wesentliche Anforderungen an Karabiner:**

1. **Bruchlasten:**
   - Längsrichtung (Major Axis): ≥ 15 kN
   - Querrichtung (Minor Axis): ≥ 10 kN (wenn konstruktionsbedingt belastbar)
   - Gate offen: ≥ 7 kN

2. **Verriegelung:**
   - Mindestens 2-Stufen-Öffnung (z.B. drehen + drücken)
   - Gate muss selbsttätig schließen
   - Verriegelung muss selbsttätig einrasten (Auto-Lock) oder manuell gesichert werden (Screw-Lock)

3. **Bedienbarkeit:**
   - Einhändige Bedienung mit nassen Handschuhen
   - Lösbar unter 1 kN Last
   - Gate-Öffnung ≥ 15 mm

4. **Dauerhaftigkeit:**
   - 10.000 Öffnungs-/Schließzyklen ohne Funktionsverlust
   - 500 Stunden Salzsprühtest ohne Funktionsverlust

5. **Kennzeichnung:**
   - CE-Zeichen
   - Hersteller
   - Bruchlast
   - Prüfnorm (ISO 12401)
   - Produktionsdatum oder -charge

---

## ANHANG D — Lasttabellen

### D.1 Spinnaker-Fall-Lasten nach Bootsgröße

| LOA (m) | Spi-Fläche (m²) | 10 kn (kN) | 15 kn (kN) | 20 kn (kN) | 25 kn (kN) | Dynamisch max (kN) | Empf. BL (kN) |
|---------|------------------|------------|------------|------------|------------|---------------------|---------------|
| 6 | 18 | 0,2 | 0,4 | 0,7 | 1,1 | 3,3 | 13 |
| 8 | 30 | 0,3 | 0,6 | 1,1 | 1,8 | 5,4 | 22 |
| 10 | 50 | 0,4 | 1,0 | 1,9 | 2,9 | 8,7 | 35 |
| 12 | 75 | 0,7 | 1,5 | 2,8 | 4,4 | 13,2 | 53 |
| 14 | 100 | 0,9 | 2,0 | 3,7 | 5,8 | 17,4 | 70 |
| 16 | 135 | 1,2 | 2,8 | 5,0 | 7,8 | 23,4 | 94 |
| 18 | 170 | 1,5 | 3,5 | 6,3 | 9,8 | 29,4 | 118 |
| 20 | 210 | 1,9 | 4,3 | 7,7 | 12,1 | 36,3 | 145 |

*Annahmen: Cd=1,2, α=15°, Dynamik-Faktor 3,0, Sicherheitsfaktor 4,0*

### D.2 Tack-Lasten (Gennaker/Asymmetrischer Spinnaker)

| LOA (m) | Gennaker-Fläche (m²) | 15 kn (kN) | 20 kn (kN) | Dynamisch max (kN) | Empf. BL (kN) |
|---------|----------------------|------------|------------|---------------------|---------------|
| 8 | 25 | 0,5 | 0,9 | 2,7 | 11 |
| 10 | 40 | 0,8 | 1,5 | 4,5 | 18 |
| 12 | 60 | 1,2 | 2,2 | 6,6 | 26 |
| 14 | 85 | 1,7 | 3,1 | 9,3 | 37 |
| 16 | 115 | 2,4 | 4,2 | 12,6 | 50 |

*Annahmen: Cd=1,1, Tack-Anteil 60% der Falllast, Dynamik-Faktor 3,0, SF 4,0*

### D.3 Safety Tether — Sturzlasten

| Szenario | Sturzhöhe (m) | Person (kg) | Stoßlast (kN) | Anmerkung |
|----------|--------------|-------------|----------------|-----------|
| Stolpern auf Deck | 0,3 | 80 | 2–4 | Elastischer Tether |
| Fall von Sitzbank | 0,5 | 80 | 3–6 | Elastischer Tether |
| Fall über Reling | 1,0 | 80 | 5–10 | Tether-Länge limitiert |
| Überbordfallen (2m Tether) | 2,0 | 80 | 8–15 | Extremfall |
| Überbordfallen + Welle | 2,0+ | 80 | 10–20 | Absolute Grenze |

*ISO 12401 fordert 15 kN BL — deckt auch Extremszenarien ab.*

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Level für Schnappschäkel-Analyse

| Parameter | Pipeline A (Structured) | Pipeline B (Visual) | Pipeline C (Text) |
|-----------|------------------------|--------------------|--------------------|
| Schäkel-Identifikation (Hersteller, Typ) | measured | visual_medium | documented |
| Bruchlast (BL, SWL) | measured (Datenblatt) | visual_low (Schätzung) | documented (Bericht) |
| Trigger-Funktion | measured (Test) | visual_low | documented |
| Korrosionszustand | — | visual_high | documented |
| Bügelverformung | measured (Messung) | visual_high | documented |
| Federspannung | measured (Kraftmessung) | visual_insufficient | — |
| Montageausrichtung | — | visual_medium | — |
| Alter/Nutzungsdauer | measured (Log) | visual_low | documented |
| Dyneema-Zustand | — | visual_high | — |
| Galvanische Korrosion | — | visual_high | documented |
| Dimensionierung | calculated | visual_medium | — |
| ISO-12401-Konformität | measured (Zertifikat) | visual_low (Kennzeichnung) | documented |

### E.2 Score-Fusion-Gewichte (Modul: Materials — Schnappschäkel)

| Aspekt | Structured Weight | Visual Weight |
|--------|-------------------|---------------|
| Materialidentifikation | 0,40 | 0,60 |
| Korrosionszustand | 0,20 | 0,80 |
| Mechanische Integrität | 0,70 | 0,30 |
| Montage/Installation | 0,30 | 0,70 |
| Dimensionierung | 0,90 | 0,10 |
| Sicherheitskonformität | 0,95 | 0,05 |

---

## ANHANG F — Wartungsintervalle

### F.1 Detaillierte Wartungsmatrix

| Komponente | Tägliche Pflege | Monatlich | Saisonal | Alle 2 Jahre | Alle 5 Jahre |
|------------|-----------------|-----------|----------|--------------|--------------|
| Schnappschäkel Körper | Süßwasserspülung | Sichtprüfung | Detailinspektion | — | Austausch prüfen |
| Trigger-Mechanismus | — | Funktionstest | Schmierung, Federkraft | — | — |
| Feder | — | — | Federspannung prüfen | Feder tauschen (Regatta) | Feder tauschen (Fahrt) |
| Wirbel | — | Drehbarkeit prüfen | Schmierung | — | — |
| Bügel-Drehpunkt | — | — | Spiel prüfen, schmieren | — | — |
| Safety Karabiner Gate | — | Schließfunktion | Vollinspektion | — | Austausch |
| Safety Karabiner Lock | — | Verriegelung prüfen | Schmierung | — | — |
| Dyneema-Schlaufe | Sichtprüfung UV | Durchmesser messen | — | Austausch (Fahrt) | — |
| Sicherungsstifte | — | Vorhandensein prüfen | Zustand prüfen | Tauschen | — |

### F.2 Schmiermittel-Empfehlungen

| Schmiermittel | Anwendung | Intervall | Markenbeispiele |
|---------------|-----------|-----------|-----------------|
| Teflon-Spray (PTFE) | Trigger, Gate, Wirbel | 4–6 Wochen | McLube (Harken), Ronstan Spray |
| Silikonöl | Trigger-Mechanismus | 4–6 Wochen | Jeder marine Silikonöl-Hersteller |
| WD-40 | Nur zum Lösen korrodierter Teile | Bei Bedarf | WD-40 (KEINE Dauerschmierung!) |
| Marine-Fett | NICHT für Schnappschäkel | — | — (zieht Schmutz an) |
| Vaseline | NICHT für Schnappschäkel | — | — (wird klebrig, blockiert) |

---

## ANHANG G — Historische Entwicklung

### G.1 Zeitleiste der Schnappschäkel-Entwicklung

**1920er–1940er: Erste Schnappschäkel**
Die ersten federbelasteten Schnellverschlüsse im maritimen Bereich waren einfache Federkarabiner, die aus der Pferdegeschirr-Herstellung übernommen wurden. Keine standardisierten Lasten, häufiges Versagen.

**1950er–1960er: Marine-spezifische Designs**
Mit dem Aufkommen des Hochsee-Rennsegels (z.B. Fastnet Race, Sydney-Hobart) wuchs der Bedarf an schnelllösbaren, hochfesten Verbindungen. Erste marine-spezifische Schnappschäkel aus rostfreiem Stahl erschienen.

**1970er–1980er: Standardisierung und Massenproduktion**
Wichard (Frankreich) etablierte das geschmiedete Schnappschäkel-Design als Standard. Die ersten ISO-Normen für marine Sicherheitsausrüstung wurden entwickelt. Harken und Ronstan begannen mit eigenen Produktlinien.

**1991: Gründung Tylaska**
Michael Tylaska gründete Tylaska Marine Hardware und entwickelte den patentierten Load-Independent Trigger. Dies revolutionierte den Hochleistungs-Schnappschäkel-Markt.

**2000er: Soft-Attachment und Gewichtsoptimierung**
Mit dem Aufkommen von Dyneema und anderen UHMWPE-Fasern wurden Soft-Attachment-Designs möglich. Regattayachten sparten signifikantes Gewicht am Masttop.

**2009: ISO 12401 veröffentlicht**
Die Norm für Sicherheitsgeschirre und -leinen definierte klare Anforderungen an Karabiner für Safety Tether. Non-Locking-Karabiner wurden für diese Anwendung ausgeschlossen.

**2010er–2020er: Titan und CNC-Fertigung**
Tylaska und andere Hersteller boten Titan-Varianten an. CNC-Bearbeitung ermöglichte komplexere und leichtere Designs. Anti-Snag-Features wurden zum Standard im Premium-Segment.

---

## ANHANG H — Bezugsquellen

### H.1 Bezugsquellen Deutschland

| Händler | Sortiment | Stärke | Website |
|---------|-----------|--------|---------|
| Compass24 | Wichard, Harken, Ronstan | Breites Sortiment, schnell | compass24.de |
| SVB | Wichard, Harken, Kong | Guter Preis, Blauwasser-Fokus | svb-marine.de |
| Toplicht | Wichard, Harken, Ronstan, Selden | Umfassend, Beratung | toplicht.de |
| AWN | Wichard, Harken | Standard-Sortiment | awn.de |
| Segelladen | Wichard, Harken, Tylaska (auf Anfrage) | Fachberatung | segelladen.de |
| Schäkel-Express | Diverse | Spezialist für Verbinder | schaekel-express.de |

### H.2 Bezugsquellen International

| Händler | Land | Spezialität | Website |
|---------|------|-------------|---------|
| Tylaska Direct | USA | Tylaska Komplettlinie | tylaska.com |
| Rig-Rite | UK | Hochleistungsbeschläge | rig-rite.co.uk |
| Nautos | Italien | Harken, diverse | nautos-usa.com |
| Marine Mega Store | Australien | Ronstan | marinemegastore.com.au |
| Accastillage Diffusion | Frankreich | Wichard, Facnor | accastillage-diffusion.com |

---

## ANHANG I — Herstellervergleich Detailtabellen

### I.1 Vergleich: 13 kN Klasse (alle Hersteller)

| Eigenschaft | Tylaska T12 | Wichard 2672 | Harken 2100 | Ronstan RF6230 | Selden 528-041 |
|-------------|-------------|--------------|-------------|----------------|----------------|
| BL (kN) | 13,3 | 12,0 | 17,8 | 13,3 | 12,0 |
| SWL (kN) | 3,3 | 3,0 | 4,5 | 3,3 | 3,0 |
| Länge (mm) | 83 | 78 | 89 | 82 | 78 |
| Gewicht (g) | 85 | 72 | 91 | 65 | 58 |
| Trigger-Typ | Load-Independent | Standard | Standard | Standard | Standard |
| Anti-Snag | Ja | Nein | Nein | Nein | Nein |
| Geschmiedet | Ja | Ja | Teilweise | Nein (Guss) | Teilweise |
| Proof-Load-Test | Jeder Stück | Stichprobe | Stichprobe | Stichprobe | Stichprobe |
| Serialisiert | Ja | Nein | Nein | Nein | Nein |
| Ersatzteile | Ja | Begrenzt | Nein | Nein | Nein |
| Preis (EUR) | 110–145 | 28–38 | 35–48 | 25–35 | 25–35 |
| Preis/kN BL | 8,3–10,9 | 2,3–3,2 | 2,0–2,7 | 1,9–2,6 | 2,1–2,9 |

### I.2 Vergleich: Safety Tether Karabiner (ISO 12401)

| Eigenschaft | Wichard 2490 | Wichard 2491 | Wichard 2493 | Kong 580.ISO | Kong 581.ISO |
|-------------|--------------|--------------|--------------|--------------|--------------|
| Verriegelung | Screw | Auto | Auto + Overboard | Tri-Lock | Tri-Lock + Indikator |
| BL (kN) | 15 | 15 | 15 | 15 | 15 |
| Öffnung (mm) | 20 | 20 | 22 | 20 | 20 |
| Gewicht (g) | 115 | 125 | 140 | 130 | 138 |
| Material | 316L HR | 316L HR | 316L HR | 316L | 316L |
| CE | Ja | Ja | Ja | Ja | Ja |
| ISO 12401 | Ja | Ja | Ja | Ja | Ja |
| Preis (EUR) | 35–45 | 42–55 | 48–62 | 35–45 | 42–52 |
| Besonderheit | — | Schneller als Screw | Overboard-Release | Standard | Verschleißindikator |

---

## ANHANG J — Schnappschäkel-Auswahl-Algorithmus

### J.1 Entscheidungslogik

```
EINGABE:
  - Anwendung (application)
  - Bootslänge (LOA) in Metern
  - Bootstyp (sail/motor)
  - Segelfläche (falls relevant)
  - Nutzungsprofil (fahrt/regatta/charter)
  - Budget (niedrig/mittel/hoch/premium)

SCHRITT 1: Safety Check
  IF application == safety_tether:
    RETURN "Kein Schnappschäkel! Locking Carabiner nach ISO 12401 erforderlich."

SCHRITT 2: Lastberechnung
  IF sail_area provided:
    load = calculate_halyard_load(sail_area, max_wind_speed, dynamic_factor)
  ELSE:
    load = estimate_from_boat_class(LOA, boat_type)
  
  required_SWL = load.dynamic_max
  required_BL = required_SWL × safety_factor

SCHRITT 3: Typ-Auswahl
  IF application in [spinnaker_halyard, spinnaker_tack]:
    IF regatta: type = trigger_release
    ELSE: type = standard OR triplebar
    IF application == spinnaker_halyard:
      swivel = RECOMMENDED
  ELIF application in [main_halyard, genoa_halyard]:
    type = standard OR fixed_eye
    security_pin = REQUIRED
  ELIF application in [cunningham, vang]:
    type = plunger_pin OR standard
  ELIF application == lazy_jacks:
    type = non_locking_carabiner OR plunger_pin

SCHRITT 4: Hersteller-Empfehlung
  FILTER shackle_database BY (SWL >= required_SWL, type, budget)
  SORT BY (best_match_SWL, quality_score, price)
  RETURN top_3_recommendations
```

---

## ANHANG K — Prüfprotokolle

### K.1 Prüfprotokoll: Saisonale Schnappschäkel-Inspektion

```
═══════════════════════════════════════════════════════════
PRÜFPROTOKOLL — SCHNAPPSCHÄKEL-INSPEKTION
═══════════════════════════════════════════════════════════

Yacht: _________________________  Datum: _______________
Prüfer: ________________________  Saison: ______________

Für jeden Schnappschäkel:

Nr. | Position | Hersteller/Modell | BL (kN) | Alter
----+----------+-------------------+---------+-------
    |          |                   |         |

Prüfpunkte (✓ = OK, ✗ = Mangel, ? = nicht beurteilbar):

[ ] Sichtprüfung Körper (Risse, Verformung)
[ ] Korrosion (keine / leicht / mittel / stark)
[ ] Pitting (keine / < 0,3mm / ≥ 0,3mm)
[ ] Trigger-Funktion (öffnet und schließt sauber)
[ ] Federspannung (subjektiv: gut / nachlassend / unzureichend)
[ ] Bügel-Einrastung (hörbar, fühlbar, vollständig)
[ ] Bügel seitliches Spiel (< 0,5mm / 0,5-1mm / > 1mm)
[ ] Wirbel-Funktion (frei / schwergängig / blockiert)
[ ] Auge (Risse, Verformung, Korrosion)
[ ] Sicherungsstift (vorhanden / fehlt / n.a.)
[ ] Dyneema-Schlaufe (Zustand, Durchmesser)

Bewertung: □ Einsatzfähig  □ Einschränkung  □ Ersetzen

Anmerkungen:
______________________________________________________________
______________________________________________________________

═══════════════════════════════════════════════════════════
```

### K.2 Prüfprotokoll: Safety Tether Inspektion

```
═══════════════════════════════════════════════════════════
PRÜFPROTOKOLL — SAFETY TETHER
═══════════════════════════════════════════════════════════

Yacht: _________________________  Datum: _______________
Prüfer: ________________________  Saison: ______________

Tether Nr: ____  Hersteller: ____________  Modell: ____________
Alter: _______ Jahre  ISO 12401 Kennzeichnung: □ Ja  □ Nein

KARABINER SCHIFF-SEITE:
  Typ: □ Screw-Lock  □ Auto-Lock  □ Tri-Lock  □ Non-Lock (KRITISCH!)
  [ ] Gate schließt selbstständig und vollständig
  [ ] Verriegelung funktioniert einwandfrei
  [ ] Öffnung ≥ 15mm für Jackline
  [ ] Keine Korrosion am Mechanismus
  [ ] Keine Risse oder Verformung
  [ ] CE / ISO Kennzeichnung lesbar

KARABINER KÖRPER-SEITE:
  Typ: □ Screw-Lock  □ Auto-Lock  □ Tri-Lock  □ Non-Lock (KRITISCH!)
  [ ] Gate schließt selbstständig und vollständig
  [ ] Verriegelung funktioniert einwandfrei
  [ ] Öffnung ≥ 15mm für Harness-D-Ring
  [ ] Keine Korrosion am Mechanismus
  [ ] Keine Risse oder Verformung
  [ ] CE / ISO Kennzeichnung lesbar

LEINE:
  [ ] Keine sichtbare UV-Degradation
  [ ] Kein Abrieb (Chafe)
  [ ] Nähte intakt
  [ ] Elastik-Funktion (falls elastisch)
  [ ] Korrekte Länge (1,0m oder 2,0m)

GESAMTBEWERTUNG:
  □ Einsatzfähig (ISO 12401 konform)
  □ Einschränkung (spezifizieren: ___________________________)
  □ SOFORT ERSETZEN (Grund: ________________________________)

═══════════════════════════════════════════════════════════
```

---

## ANHANG L — Visuelle Analyse-Referenz

### L.1 Referenzbilder-Beschreibungen für AYDI Visual Pipeline

| Referenz-ID | Beschreibung | Zustand | Erwartete Erkennung |
|-------------|-------------|---------|---------------------|
| SS-REF-001 | Neuer Tylaska T12, Standard, Edelstahl | Neuwertig | Hersteller: Tylaska, Typ: Trigger Release, Zustand: 100 |
| SS-REF-002 | Wichard 2672, 5 Jahre, leichte Korrosion | Gut | Hersteller: Wichard, Typ: Standard, Korrosion: leicht |
| SS-REF-003 | Unbekannter Snap, starke Korrosion, Pitting | Schlecht | Korrosion: stark, Pitting: ja, Empfehlung: ersetzen |
| SS-REF-004 | Snap Shackle mit verformtem Bügel | Kritisch | Verformung: ja, Empfehlung: sofort ersetzen |
| SS-REF-005 | Safety Karabiner, Non-Locking | Sicherheitskritisch | Non-Locking als Safety: KRITISCH |
| SS-REF-006 | Wichard Triplebar, geschlossen, am Spi-Fall | Gut | Typ: Triplebar, Anwendung: Spinnaker-Fall |
| SS-REF-007 | Dyneema Soft-Attachment, UV-degradiert | Mäßig | Dyneema-UV: sichtbar, Empfehlung: bald ersetzen |
| SS-REF-008 | Galvanische Korrosion, Edelstahl auf Alu | Warnung | Kontaktkorrosion erkannt, Empfehlung: Isolation |

### L.2 Visuelle Erkennungsmerkmale nach Hersteller

| Hersteller | Erkennungsmerkmal | AYDI Visual Confidence |
|------------|-------------------|----------------------|
| Wichard | „W" Logo, HR-Prägung, Gratlinien (geschmiedet) | visual_high |
| Tylaska | „T" Logo, Seriennummer, versenkter Trigger | visual_high |
| Harken | „H" Logo, Artikelnummer auf Körper | visual_medium |
| Ronstan | „R" Logo, RF-Nummer auf Körper | visual_medium |
| Kong | Kong-Schriftzug, Alpennummer | visual_high |
| Allen | „A" Nummer, kompakte Bauform | visual_medium |
| Selden | Selden-Schriftzug, 528-Nummer | visual_medium |
| Unbekannt | Kein Logo, keine Nummer | visual_low |

---

## ANHANG M — Korrosionsschutz und Pflege

### M.1 Korrosionsschutzmaßnahmen

| Maßnahme | Beschreibung | Frequenz | Effektivität |
|----------|-------------|----------|--------------|
| Süßwasserspülung | Salzkristalle auswaschen | Nach jedem Salzwasser-Tag | Hoch |
| Teflon-Spray | Schützender PTFE-Film auf Mechanismus | 4–6 Wochen | Hoch |
| Silikonöl | Schmierende Schutzschicht | 4–6 Wochen | Mittel-Hoch |
| Passivierung | Zitronensäure-Behandlung der Edelstahloberfläche | Saisonal | Mittel |
| Isolierung | Nylon/PTFE-Scheibe zwischen verschiedenen Metallen | Einmalig (Installation) | Hoch |
| Schutzabdeckung | UV- und Witterungsschutz bei Nichtgebrauch | Permanent | Mittel |
| Winterlager-Behandlung | Gründliche Reinigung, Schmierung, trockene Lagerung | Jährlich | Hoch |

### M.2 Reinigungsmittel

| Mittel | Anwendung | Vorsicht |
|--------|-----------|----------|
| Süßwasser | Tägliche Spülung | — |
| Zitronensäure 10% | Passivierung, leichte Korrosion | 30 min einwirken, gründlich spülen |
| Oxalsäure (Bar Keepers Friend) | Fremdrost entfernen | Handschuhe, gut spülen |
| Phosphorsäure | Stärkere Korrosion | Vorsicht bei empfindlichen Teilen |
| Scotch-Brite (fein) | Mechanische Reinigung | KEIN Stahlwolle (Fremdrost-Quelle!) |
| Essig (5%) | Leichte Kalkablagerungen | Für Edelstahl unbedenklich |

---

## ANHANG N — Retrofit-Leitfaden

### N.1 Aufrüstung Standard → Anti-Snag

**Situation:** Bestehende Standard-Schnappschäkel sollen gegen Anti-Snag-Modelle getauscht werden (nach Vorfall oder präventiv).

**Vorgehen:**
1. Alle Schnappschäkel inventarisieren (Position, Typ, BL, Alter)
2. Lastanforderung pro Position bestimmen
3. Ersatzschäkel auswählen (Tylaska T-Serie oder Wichard Triplebar)
4. Kompatibilität prüfen (Augenbohrung, Falldurchmesser, Platz)
5. Austausch durchführen (Saisonbeginn empfohlen)
6. Alte Schäkel dokumentieren und entsorgen (nicht wiederverwenden)

**Budget-Schätzung (10m Fahrtenyacht, 8 Schnappschäkel):**
- Standard → Wichard Triplebar: 250–450 EUR
- Standard → Tylaska T-Serie: 600–1.000 EUR

### N.2 Aufrüstung Non-Locking → ISO 12401 Safety Karabiner

**Situation:** Bestehende Sicherheitsleinen mit Non-Locking-Karabinern sollen ISO-konform nachgerüstet werden.

**Vorgehen:**
1. SOFORT alle Non-Locking-Karabiner an Sicherheitsleinen ersetzen
2. ISO-12401-konforme Karabiner beschaffen (Wichard 2490/2491 oder Kong 580.ISO)
3. Sicherheitsleinen auf Zustand prüfen (ggf. komplett tauschen)
4. Crew briefen: Unterschied Non-Locking vs. Locking erklären

**Budget-Schätzung (4 Sicherheitsleinen komplett):**
- Nur Karabiner tauschen: 200–350 EUR
- Komplette Sicherheitsleinen mit ISO-Karabinern: 350–600 EUR

---

## ANHANG O — Regatta-Spezifikationen

### O.1 World Sailing OSR Anforderungen

**Kategorie 0–2 (Hochsee-Regatten):**
- Safety Tether: ISO-12401-konforme Karabiner, mind. 1 pro Crewmitglied
- Jacklines: Gurtband oder Edelstahldraht, beidseitig befestigt
- Sicherheitsgeschirr: Integriert oder separat, ISO 12401

**Regatta-spezifische Schnappschäkel-Anforderungen:**
- Keine spezifische Norm für Schnappschäkel an Fallen/Segeln
- Empfehlung: BL ≥ 3× maximale Betriebslast
- Spinnaker-Fall-Schnappschäkel: Trigger muss unter SWL betätigbar sein

### O.2 One-Design-Klassenregeln

Viele One-Design-Klassen spezifizieren maximale Schnappschäkel-Gewichte oder beschränken den Einsatz:

| Klasse | Regelung | Typische Lösung |
|--------|----------|-----------------|
| J/70 | Keine spezifische Beschränkung | Tylaska T5/T8 oder Allen |
| Melges 24 | Gewichtslimit Mast | Tylaska Titan oder Soft-Attachment |
| SB20 | Klassenregel definiert Beschläge | Allen oder Ronstan |
| TP52 | Keine Beschränkung | Tylaska T12/T20 Titan |
| IMOCA 60 | Keine Beschränkung, Gewicht kritisch | Tylaska Titan, Soft-Attachment |

---

## ANHANG P — Superyacht-Sonderlösungen

### P.1 Anforderungen Superyachten (18m+)

Superyachten stellen besondere Anforderungen an Schnappschäkel:

**Lastanforderungen:**
- Segelflächen 200–1.000+ m²
- Falllasten 30–200+ kN
- Standardbeschläge reichen oft nicht aus

**Ästhetische Anforderungen:**
- Polierte Oberfläche (Mirror Finish)
- Keine sichtbaren Gratlinien
- Farblich abgestimmte Beschläge (eloxiert oder beschichtet)

**Typische Lösungen:**

| Anwendung | Standardlösung | Superyacht-Lösung |
|-----------|---------------|-------------------|
| Spinnaker-Fall | Tylaska T30 | Tylaska T50, Sonderfertigung |
| Großsegel-Fall | Wichard 2674 | Hydraulische Fallen-Klemme |
| Safety Tether | Wichard 2491 | Custom ISO-12401 Karabiner |
| Decksbeschläge | Standard-Snap | CNC-gefräste Sonderanfertigung |

### P.2 Zertifizierungsanforderungen

Superyachten über 24m LOA unterliegen den Klassifikationsregeln (Lloyd's, DNV-GL, Bureau Veritas). Schnappschäkel und Karabiner müssen:

- Vom Hersteller mit Prüfzeugnissen geliefert werden
- In der Klassifikationszeichnung dokumentiert sein
- Regelmäßig durch den Klasse-Surveyor inspiziert werden

---

## ANHANG Q — Umrechnungstabellen

### Q.1 Krafteinheiten

| Von | Nach | Faktor |
|-----|------|--------|
| kN | daN | × 100 |
| kN | kgf | × 101,97 |
| kN | lbf | × 224,81 |
| daN | kN | × 0,01 |
| daN | kgf | × 1,0197 |
| lbf | kN | × 0,004448 |
| kgf | kN | × 0,009807 |

### Q.2 Windgeschwindigkeit

| Beaufort | kn | m/s | km/h | Bezeichnung |
|----------|----|-----|------|-------------|
| 1 | 1–3 | 0,3–1,5 | 1–5 | Leiser Zug |
| 2 | 4–6 | 1,6–3,3 | 6–11 | Leichte Brise |
| 3 | 7–10 | 3,4–5,4 | 12–19 | Schwache Brise |
| 4 | 11–16 | 5,5–7,9 | 20–28 | Mäßige Brise |
| 5 | 17–21 | 8,0–10,7 | 29–38 | Frische Brise |
| 6 | 22–27 | 10,8–13,8 | 39–49 | Starker Wind |
| 7 | 28–33 | 13,9–17,1 | 50–61 | Steifer Wind |
| 8 | 34–40 | 17,2–20,7 | 62–74 | Stürmischer Wind |

### Q.3 Längen und Dimensionen

| Von | Nach | Faktor |
|-----|------|--------|
| mm | inch | × 0,03937 |
| inch | mm | × 25,4 |
| m | ft | × 3,281 |
| ft | m | × 0,3048 |

---

## ANHANG R — Checklisten

### R.1 Checkliste: Neukauf Schnappschäkel

- [ ] Anwendung definiert (Spinnaker, Fall, Niederholer, etc.)
- [ ] Lastberechnung durchgeführt (SWL, BL bestimmt)
- [ ] Sicherheitsfaktor festgelegt (4 Standard, 5 sicherheitskritisch, 3 Regatta)
- [ ] Typ ausgewählt (Standard, Swivel, Fixed Eye, Trigger Release, Plunger)
- [ ] Anti-Snag-Anforderung geprüft
- [ ] Wirbel-Anforderung geprüft (Spinnaker-Fall: empfohlen)
- [ ] Kompatibilität mit Fall/Leine geprüft (Durchmesser, Auge)
- [ ] Kompatibilität mit Beschlag geprüft (Bolzenbohrung, Platz)
- [ ] Material bestätigt (316L geschmiedet für Standard, Titan optional für Regatta)
- [ ] Hersteller gewählt (Qualitätsniveau und Budget)
- [ ] Reserveschäkel mitbestellt (1–2 gleiche Größe)
- [ ] Schmiermittel mitbestellt (Teflon-Spray)

### R.2 Checkliste: Neukauf Safety Tether

- [ ] ISO 12401 Konformität bestätigt
- [ ] Karabiner-Typ: Locking (Screw, Auto, oder Tri-Lock)
- [ ] BL ≥ 15 kN bestätigt
- [ ] Gate-Öffnung ≥ 15 mm (≥ 20 mm für breite Jacklines)
- [ ] Einhändige Bedienung mit nassen Handschuhen getestet
- [ ] Leinenlänge gewählt (1,0 m oder 2,0 m)
- [ ] Elastik oder nicht-elastik gewählt
- [ ] CE-Kennzeichnung vorhanden
- [ ] Anzahl bestimmt (min. 1 pro Crewmitglied + 1 Reserve)
- [ ] Jackline-Kompatibilität geprüft

### R.3 Checkliste: Saisonbeginn — Alle Schnappschäkel und Karabiner

- [ ] Alle Schnappschäkel inventarisiert und mit Prüfprotokoll abgeglichen
- [ ] Sichtprüfung aller Schäkel auf Risse, Verformung, Korrosion
- [ ] Trigger-Funktionstest aller Schnappschäkel
- [ ] Federspannung subjektiv bewertet (jeder Schäkel)
- [ ] Bügelspiel geprüft (jeder Schäkel)
- [ ] Wirbel-Drehbarkeit geprüft (Wirbel-Schäkel)
- [ ] Alle Sicherungsstifte vorhanden und intakt
- [ ] Dyneema-Schlaufen (Soft-Attachment) auf UV und Abrieb geprüft
- [ ] Safety Tether komplett geprüft (Gate, Lock, Leine)
- [ ] Alle Schäkel und Karabiner geschmiert
- [ ] Ersatzteile an Bord (Reserve-Schäkel, Federn, Sicherungsstifte)
- [ ] Prüfprotokoll ausgefüllt und archiviert

### R.4 Checkliste: Vor Starkwind / Nachtfahrt

- [ ] Alle Fallen-Schnappschäkel gesichert (Pin oder Tape)
- [ ] Safety Tether für jedes Crewmitglied bereitgelegt
- [ ] Safety Tether Karabiner Funktionstest (Gate, Lock)
- [ ] Jacklines aufgebaut und befestigt
- [ ] Spinnaker-Schnappschäkel geprüft (falls Spi steht)
- [ ] Reserve-Schnappschäkel griffbereit

### R.5 Checkliste: Winterlager / Saisonende

- [ ] Alle Schnappschäkel und Karabiner demontiert (wo möglich)
- [ ] Gründliche Süßwasserspülung aller Teile
- [ ] Trocknen lassen (24h Lufttrocknung)
- [ ] Mechanismen mit Teflon-Spray schmieren
- [ ] Trigger/Gates mehrfach betätigen (Schmiermittel verteilen)
- [ ] Dyneema-Schlaufen abnehmen und trocken lagern
- [ ] Safety Tether komplett, trocken lagern
- [ ] Zustandsbericht erstellen (was muss vor nächster Saison getauscht werden?)
- [ ] Ersatzteile bestellen (Federn, Schäkel, Karabiner)
- [ ] Prüfprotokoll archivieren

### R.6 Checkliste: Regatta-Vorbereitung — Schnappschäkel

- [ ] Alle Spinnaker-/Gennaker-Schnappschäkel Funktionstest unter Handlast
- [ ] Trigger-Kraft subjektiv: alle > 1,5 kg Fingerkraft
- [ ] Anti-Snag-Schäkel an allen kritischen Positionen (Spi-Fall, Spi-Tack)
- [ ] Backup-Schnappschäkel in Cockpit-Tasche (2 Stück, passende Größen)
- [ ] Ersatzfedern an Bord (Tylaska: 2 Stück pro Größe)
- [ ] Schäkelöffner / Marlspieker griffbereit
- [ ] Sicherungsband (Segelmacher-Tape) griffbereit
- [ ] Alle Wirbel-Schäkel drehen frei (kein Quietschen, kein Klemmen)
- [ ] Soft-Attachment-Schlaufen: Durchmesser und UV-Zustand OK
- [ ] Crew-Briefing: Wer löst welchen Schäkel beim Bergen?
- [ ] Crew-Briefing: Notfall-Prozedur bei Schnappschäkel-Versagen

### R.7 Checkliste: Blauwasser-Vorbereitung — Schnappschäkel und Sicherheit

- [ ] Alle Schnappschäkel durch neue oder gründlich geprüfte ersetzt
- [ ] Doppelte Anzahl Reserve-Schnappschäkel an Bord (jede verwendete Größe)
- [ ] Safety Tether: 2 pro Crewmitglied (1 aktiv, 1 Reserve)
- [ ] Jackline-Material geprüft (Alter < 5 Jahre, Zustand einwandfrei)
- [ ] Jackline-Befestigungspunkte geprüft (Augbolzen, Belastbarkeit)
- [ ] Alle Safety Karabiner ISO 12401 konform
- [ ] Ersatz-Safety-Karabiner an Bord (2 Stück)
- [ ] Schmiermittel-Vorrat an Bord (Teflon-Spray: 2 Dosen, Silikonöl: 1 Flasche)
- [ ] Wartungswerkzeug an Bord (Inbusschlüssel für Tylaska, Scotch-Brite, Zitronensäure)
- [ ] Crew-Briefing: Safety Tether Handhabung, Jackline-Einhängepunkte
- [ ] Crew-Briefing: MOB-Prozedur mit Safety Tether
- [ ] Notfall-Schneidwerkzeug an Bord (für Leinenkappeung bei blockiertem Schäkel)

### R.8 Checkliste: Charter-Übernahme — Schnappschäkel und Sicherheit

- [ ] Alle vorhandenen Schnappschäkel identifiziert und Zustand bewertet
- [ ] Fallen-Schnappschäkel: Trigger-Funktion getestet
- [ ] Spinnaker-Equipment (falls vorhanden): Schnappschäkel-Zustand
- [ ] Safety Tether: Vorhanden? ISO 12401? Karabiner-Typ?
- [ ] Jacklines: Vorhanden? Zustand? Befestigungspunkte?
- [ ] Wenn Safety Tether fehlt oder mangelhaft: EIGENE mitbringen
- [ ] Wenn Schnappschäkel erkennbar mangelhaft: Charter-Basis informieren
- [ ] Reserveteile der Charter-Basis erfragen

---

## ANHANG S — Weiterführende Berechnungen

### S.1 Dynamischer Lastfaktor — Detailberechnung

Der dynamische Lastfaktor (Dynamic Amplification Factor, DAF) für Schnappschäkel hängt von der Art der Lastaufbringung ab:

**Plötzliche Volllast (Spinnaker füllt nach Kollaps):**
```
DAF = 1 + √(1 + 2 × h/δ_st)
```
wobei:
- h = "Fallhöhe" der Last (Segel fällt und füllt sich)
- δ_st = statische Dehnung der Verbindungskette (Fall + Schäkel)

**Harmonische Schwingung (Rigg-Vibration):**
```
DAF = 1 / √((1 - r²)² + (2 × ζ × r)²)
```
wobei:
- r = Frequenzverhältnis (Erregerfrequenz / Eigenfrequenz)
- ζ = Dämpfungsverhältnis (0,02–0,05 für Edelstahl)

**Impuls-Last (Stoß gegen Beschlag):**
```
F_impact = m × v / Δt
```
wobei:
- m = Masse des schlagenden Teils
- v = Aufprallgeschwindigkeit
- Δt = Kontaktdauer (0,001–0,01 s für Metall-auf-Metall)

### S.2 Federkraft-Berechnung für Trigger

Die erforderliche Mindest-Federkraft für einen Schnappschäkel-Trigger:

**Gegen unbeabsichtigtes Öffnen durch Vibration:**
```
F_spring > m_trigger × a_max × SF_spring
```
wobei:
- m_trigger = Masse des Trigger-Hebels
- a_max = maximale Beschleunigung (Vibration, Seegang)
- SF_spring = Sicherheitsfaktor Feder (typisch: 3–5)

**Typische Werte:**
| Schäkelgröße | Trigger-Masse (g) | Max. Beschleunigung (g) | Min. Federkraft (N) |
|--------------|-------------------|-------------------------|---------------------|
| Mini (T5) | 3–5 | 5–10 | 1,5–5 |
| Klein (T8) | 5–8 | 5–10 | 2,5–8 |
| Mittel (T12) | 8–15 | 5–8 | 4–12 |
| Groß (T20) | 15–25 | 3–6 | 5–15 |
| XL (T30) | 25–40 | 3–5 | 8–20 |

### S.3 Lebensdauer-Abschätzung

**Ermüdungslebensdauer (Zyklen):**
```
N = (S_e / S_a)^b
```
wobei:
- N = Anzahl Zyklen bis Versagen
- S_e = Dauerfestigkeit (Endurance Limit) des Materials
- S_a = Spannungsamplitude
- b = Materialexponent (3–5 für Edelstahl)

**Korrosions-bedingte Lebensdauer:**
Die Kombination aus Ermüdung und Korrosion (Corrosion Fatigue) reduziert die Lebensdauer signifikant:
- In Salzwasser: Lebensdauer ca. 30–50% der Luft-Lebensdauer
- Mit Spaltkorrosion: Weitere Reduktion um 20–40%
- Mit Pitting: Pitting-Tiefe wirkt als Kerbfaktor (Kt = 1 + 2×√(a/ρ))

**Praktische Konsequenz:**
Die theoretische Ermüdungslebensdauer eines Schnappschäkels in Salzwasser beträgt nur 15–30% der Herstellerangabe (die auf Luftprüfungen basiert). Deshalb sind die empfohlenen Austauschintervalle (5–10 Jahre Fahrt, 3–5 Jahre Regatta) konservativ und sollten eingehalten werden.

### S.4 Galvanische Spannungsreihe — Relevante Paarungen

| Material 1 | Material 2 | Spannungsdifferenz (mV) | Korrosionsrisiko |
|------------|------------|------------------------|------------------|
| 316L Edelstahl | Aluminium 6061 | ~500–700 | HOCH — Alu korrodiert |
| 316L Edelstahl | Verzinkter Stahl | ~300–500 | MITTEL — Zink korrodiert |
| 316L Edelstahl | Bronze | ~50–150 | GERING |
| 316L Edelstahl | Titan | ~100–200 | GERING — Edelstahl korrodiert leicht |
| Titan | Aluminium | ~600–800 | SEHR HOCH — Alu korrodiert |

**Regel für Schnappschäkel:**
- Edelstahl-Schnappschäkel an Edelstahl-Beschlag: OK
- Edelstahl-Schnappschäkel an Bronze-Beschlag: OK
- Edelstahl-Schnappschäkel an Aluminium-Beschlag: NUR mit Isolation
- Titan-Schnappschäkel an Aluminium-Beschlag: NUR mit Isolation

---

## ANHANG T — Typische Fehler bei der Schnappschäkel-Auswahl

### T.1 Die 10 häufigsten Fehler

**Fehler 1: Non-Locking-Karabiner als Safety Tether**
Konsequenz: Lebensgefahr. Gate kann sich durch Kontakt mit Jackline oder Reling öffnen.
Lösung: Nur ISO-12401-konforme Locking-Karabiner verwenden.

**Fehler 2: Schnappschäkel nicht gewartet**
Konsequenz: Federermüdung, Korrosion, unbeabsichtigtes Öffnen.
Lösung: Wartungsplan gemäß Anhang F einhalten.

**Fehler 3: Unterdimensionierung**
Konsequenz: Vorzeitiges Versagen, insbesondere bei dynamischen Lasten.
Lösung: Lastberechnung gemäß Abschnitt 5 und Anhang D durchführen.

**Fehler 4: Trigger zur Leinenseite montiert**
Konsequenz: Leine kann Trigger auslösen.
Lösung: Trigger immer von Leinen und Segeln weg ausrichten.

**Fehler 5: Kein Sicherungsstift bei Dauer-Fallen**
Konsequenz: Unbeabsichtigtes Öffnen bei Vibration oder Schlag.
Lösung: Sicherungsstift oder Tape bei Großsegel- und Genua-Fall.

**Fehler 6: Billig-Schäkel an sicherheitskritischer Position**
Konsequenz: Unbekannte Materialqualität, kein Proof-Load-Test, Versagensrisiko.
Lösung: Nur Markenhersteller (Wichard, Tylaska, Harken, Ronstan) verwenden.

**Fehler 7: Alter nicht beachtet**
Konsequenz: Ermüdungsversagen nach 10+ Jahren ohne Austausch.
Lösung: Austauschintervalle einhalten (Anhang F).

**Fehler 8: Falsche Schmierung (Fett statt Teflon)**
Konsequenz: Fett zieht Schmutz an und blockiert den Trigger-Mechanismus.
Lösung: Nur Teflon-Spray oder Silikonöl verwenden.

**Fehler 9: Galvanische Paarung ignoriert**
Konsequenz: Beschleunigte Korrosion, insbesondere bei Aluminium-Beschlägen.
Lösung: Isolierscheibe verwenden, gleiche Materialien bevorzugen.

**Fehler 10: Dyneema-Schlaufe nicht getauscht**
Konsequenz: UV-Degradation führt zu plötzlichem Versagen.
Lösung: Dyneema alle 1–3 Saisons tauschen, regelmäßig inspizieren.

---

*Ende der AYDI-Wissensdatei 12.04 — Schnappschäkel und Karabiner im Yachtbau*
*Version 1.0.0 — 2026-04-26 — AYDI Research*
*Nächste geplante Revision: 2026-10-01*
