---
title: "Ankerketten und Kettenvorlauf im Yachtbau"
kategorie: "13 Ankergeschirr und Ankersysteme"
unterkategorie: "02 Ankerketten und Kettenvorlauf"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, DIN/ISO-Normen, Laborprüfungen"
  - documented: "Hersteller-Kataloge, Fachpresse, Normen-Kommentare"
  - estimated: "Erfahrungswerte, Quervergleiche, Praxisberichte"
  - benchmark: "Marktdurchschnitte, Branchenstandards, Flottenauswertungen"
tags:
  - ankerkette
  - kettenvorlauf
  - ankergeschirr
  - rode
  - kettennuss
  - ankerwinsch
  - kettenstopper
  - kettenschäkel
  - galvanisierung
  - edelstahlkette
  - DIN_766
  - ISO_4565
  - chain_grade
  - ankerzubehör
boot_klassen:
  - kleinkreuzer (6–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - motoryacht (8–25m)
  - superyacht (18m+)
  - rib_trailer (4–7m)
---

# 13.02 — Ankerketten und Kettenvorlauf im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.02** — Kategorie 13: Ankergeschirr und Ankersysteme
> **Confidence-Quelle:** measured (Hersteller-TDS, DIN/ISO-Normen), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen](#2-grundlagen)
3. [Typenübersicht](#3-typenübersicht)
4. [Dimensionierung](#4-dimensionierung)
5. [Produktlinien und Hersteller](#5-produktlinien-und-hersteller)
6. [Kettenverbinder und Zubehör](#6-kettenverbinder-und-zubehör)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting-Entscheidungsbaum](#8-troubleshooting-entscheidungsbaum)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
14. [ANHANG C — Normen und Standards](#anhang-c--normen-und-standards)
15. [ANHANG D — Belastungstabellen](#anhang-d--belastungstabellen)
16. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
17. [ANHANG F — Wartungsintervalle](#anhang-f--wartungsintervalle)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — Bezugsquellen](#anhang-h--bezugsquellen)
20. [ANHANG I — Herstellervergleich Detailtabellen](#anhang-i--herstellervergleich-detailtabellen)
21. [ANHANG J — Kettenauswahl-Algorithmus](#anhang-j--kettenauswahl-algorithmus)
22. [ANHANG K — Prüfprotokolle](#anhang-k--prüfprotokolle)
23. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
24. [ANHANG M — Korrosionsschutz-Kompatibilität](#anhang-m--korrosionsschutz-kompatibilität)
25. [ANHANG N — Retrofit-Leitfaden](#anhang-n--retrofit-leitfaden)
26. [ANHANG O — Regatta- und Leichtbau-Lösungen](#anhang-o--regatta-und-leichtbau-lösungen)
27. [ANHANG P — Superyacht-Sonderlösungen](#anhang-p--superyacht-sonderlösungen)
28. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
29. [ANHANG R — Checklisten](#anhang-r--checklisten)

---

## 1. Einführung und Übersicht

### 1.1 Was ist eine Ankerkette?

Die Ankerkette (englisch: anchor chain) ist das zentrale Verbindungselement zwischen Anker und Yacht. Sie überträgt die Haltekraft des Ankers auf das Schiff und bildet zusammen mit dem Anker, dem Kettenvorlauf (rode), der Ankerwinsch und dem Kettenstopper das Ankergeschirr (ground tackle). Die Ankerkette ist eines der sicherheitskritischsten Bauteile an Bord — ihr Versagen kann zum Verlust des Ankers, zur Strandung oder zu Kollisionen führen.

Im Gegensatz zu reinem Ankertau bietet die Kette entscheidende Vorteile: sie ist abriebfest am Meeresgrund, ihr Eigengewicht erzeugt einen flachen Zugwinkel am Anker (Kettenary-Effekt), und sie ist unempfindlich gegen Scheuern an Felsen, Korallen oder scharfen Kanten. Gleichzeitig bringt sie erhebliches Gewicht im Bug mit sich — ein Faktor, der bei der Yachtkonstruktion sorgfältig berücksichtigt werden muss.

### 1.2 Bedeutung für die Yachtkonstruktion

Für den Yachtkonstrukteur ist die Ankerkette ein kritischer Designparameter:

- **Gewichtsverteilung:** 50–100 m Kette à 8 mm wiegen 80–160 kg im Vorschiff. Dies beeinflusst den Trimm, die Seegangseigenschaften und die Stabilität erheblich.
- **Kettenkasten-Dimensionierung:** Der Kettenkasten muss das Volumen der gestapelten Kette aufnehmen, Ablauf- und Spülwasser führen und strukturell die dynamischen Lasten aufnehmen.
- **Bugbeschlag-Integration:** Bugrolle, Kettenstopper, Ankerwinsch und Kettenführung müssen exakt auf den Kettendurchmesser abgestimmt sein.
- **Strukturelle Lasten:** Die Ankerkräfte werden über den Bugbeschlag in die Rumpfstruktur eingeleitet — die Kette definiert die maximale Belastung.
- **Wartungszugänglichkeit:** Ketten müssen regelmäßig inspiziert, gereinigt und ggf. neu verzinkt werden. Der Zugang zum Kettenkasten ist konstruktiv zu gewährleisten.

### 1.3 Abgrenzung zu anderen Wissensdateien

| Wissensdatei | Thema | Schnittstelle |
|---|---|---|
| 13.01 Ankertypen | Ankerformen, Haltekraft, Setzverhalten | Ketten-Anker-Verbindung, Schäkelwahl |
| 13.03 Ankerwinsch | Winsch-Typen, Kettennuss-Kompatibilität | Kettendurchmesser, Teilung, Windenlast |
| 13.04 Kettenstopper | Stopper-Mechanismen, Klemmung | Kettengröße, Belastungsgrenzen |
| 13.05 Bugrolle | Rollengeometrie, Kettenlauf | Kettenführung, Ankerstau |
| 05.01 Edelstahl-Schrauben | Verbindungselemente | Schäkel-Material, Korrosion |
| 07.06 Opferanoden | Galvanischer Schutz | Kettenmaterial-Kompatibilität |

### 1.4 Normative Grundlagen (Kurzübersicht)

Die Ankerkette im Yachtbau unterliegt verschiedenen Normen und Regelwerken:

- **DIN 766** — Rundstahlkette, kurzgliedrig, kalibriert (Hauptnorm für europäische Yachtketten)
- **ISO 4565** — Kurzgliedrige Rundstahlkette, kalibriert, Güteklasse 30/40
- **DIN EN 818** — Kurzgliedrige Rundstahlketten für Hebezeuge (Güteklasse 80)
- **NACM (National Association of Chain Manufacturers)** — US-amerikanische Kettenstandards
- **ABS / Lloyd's / DNV** — Klassifikationsgesellschaften für Superyachten
- **CE-Konformität** — Recreational Craft Directive 2013/53/EU (indirekt über Ausrüstungsanforderungen)

### 1.5 Geltungsbereich

Diese Wissensdatei behandelt Ankerketten und Kettenvorlauf-Systeme (Rode-Systeme) für Yachten von 6 m bis 30+ m Länge. Der Schwerpunkt liegt auf:

- Kalibrierte Kette nach DIN 766 / ISO 4565 (6–16 mm)
- Güteklassen G30, G40, G43 und G70
- Ketten-Tau-Kombinationen (Chain-Rope-Rode)
- All-Chain-Rode-Systeme
- Dimensionierung nach Bootsgröße, Einsatzgebiet und Windlasten
- Marktübersicht der relevanten Hersteller und Preisstrukturen

Nicht behandelt werden: Ankertau ohne Kettenvorlauf (→ separate Wissensdatei), Mooringketten für Festliegeplätze, industrielle Hebeketten.

---

## 2. Grundlagen

### 2.1 Kettengüteklassen (Chain Grades)

Die Güteklasse (Grade) einer Ankerkette definiert ihre Mindestbruchlast relativ zum Nennmaß. Höhere Güteklassen bedeuten höhere Festigkeit bei gleichem Durchmesser — oder gleiche Festigkeit bei geringerem Durchmesser und damit Gewicht.

#### 2.1.1 Grade 30 (G30) — Proof Coil Chain

**Beschreibung:** Die niedrigste im Yachtbereich relevante Güteklasse. G30-Kette wird auch als „Proof Coil" oder „Common Coil" bezeichnet. Sie besteht aus kohlenstoffarmem Stahl und wird werkseitig mit der halben Bruchlast geprüft (proof-tested).

**Eigenschaften:**
- Mindestbruchlast: ca. 1,5-fache der WLL (Working Load Limit)
- Stahl: kohlenstoffarmer Baustahl (C ≤ 0,20%)
- Härte: ca. 100–150 HB (Brinell)
- Dehnung bei Bruch: >15%
- Duktiles Bruchverhalten (Vorwarnung durch Verformung)

**Einsatzbereich im Yachtbau:**
- Ankervorlauf für Kleinkreuzer und Trailer-Boote
- Festmacherketten
- Mooringketten (nicht in dieser Datei behandelt)

**Typische WLL-Werte G30:**

| Nennmaß (mm) | WLL (kN) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) |
|---|---|---|---|---|
| 6 | 3,5 | 357 | 10,5 | 0,79 |
| 8 | 6,3 | 642 | 18,9 | 1,40 |
| 10 | 9,8 | 999 | 29,4 | 2,20 |
| 12 | 14,1 | 1438 | 42,3 | 3,10 |
| 13 | 16,5 | 1683 | 49,5 | 3,68 |
| 16 | 25,0 | 2549 | 75,0 | 5,60 |

> **AYDI-Praxishinweis:** G30-Kette ist für Fahrtenyachten im europäischen Revier akzeptabel, wird aber für Blauwasserfahrt nicht empfohlen. Das duktile Bruchverhalten bietet den Vorteil, dass Überlastung durch sichtbare Verformung erkennbar ist, bevor es zum Bruch kommt.

#### 2.1.2 Grade 40 (G40) — High Test / BBB Chain

**Beschreibung:** G40 ist die Standardgüteklasse für Yachtankerketten in Nordamerika. Die Bezeichnung „BBB" (Triple-B oder „3B") bezieht sich auf die ursprüngliche US-Klassifikation nach Gliedlänge. G40 bietet ca. 30% mehr Bruchlast als G30 bei gleichem Durchmesser.

**Eigenschaften:**
- Mindestbruchlast: ca. 2,0-fache der WLL
- Stahl: kohlenstoffarmer bis mittelkarbonstahl (C 0,15–0,30%)
- Härte: ca. 150–200 HB
- Dehnung bei Bruch: >12%
- Duktiles bis halbduktiles Bruchverhalten

**Einsatzbereich im Yachtbau:**
- Standard-Ankerkette für Küstenfahrt und gemäßigte Reviere
- Primärkette für Fahrtensegler 8–14 m
- Zweitkette (Heckanker) für Blauwasseryachten

**Typische WLL-Werte G40:**

| Nennmaß (mm) | WLL (kN) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) |
|---|---|---|---|---|
| 6 | 5,0 | 510 | 14,0 | 0,79 |
| 8 | 8,9 | 907 | 24,9 | 1,40 |
| 10 | 13,9 | 1418 | 38,9 | 2,20 |
| 12 | 20,0 | 2039 | 56,0 | 3,10 |
| 13 | 23,5 | 2397 | 65,8 | 3,68 |
| 16 | 35,6 | 3630 | 99,7 | 5,60 |

> **AYDI-Praxishinweis:** G40/BBB ist die meistverbreitete Kettengüteklasse in den USA. In Europa ist DIN-766-Kette (die typisch G30 entspricht) üblicher. Beim Kauf aus US-Quellen auf die Kennzeichnung achten — viele „BBB"-Ketten sind tatsächlich nur G30 proof-getestet.

#### 2.1.3 Grade 43 (G43) — High Test Chain

**Beschreibung:** G43 ist die häufigste Empfehlung für Fahrtenyachten und Blauwasseryachten. Sie bietet ca. 57% mehr Bruchlast als G30 bei identischem Gewicht und Durchmesser. In Europa wird G43 oft als „ISO-kalibrierte Hochfeste Kette" vermarktet.

**Eigenschaften:**
- Mindestbruchlast: ca. 2,3-fache der WLL
- Stahl: mittelkarbonstahl, wärmebehandelt (C 0,20–0,35%)
- Härte: ca. 200–250 HB
- Dehnung bei Bruch: >10%
- Halbduktiles Bruchverhalten

**Einsatzbereich im Yachtbau:**
- Empfohlene Hauptkette für Blauwasseryachten
- Standard für Yachten >14 m
- Beste Balance aus Festigkeit, Gewicht und Kosten

**Typische WLL-Werte G43:**

| Nennmaß (mm) | WLL (kN) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) |
|---|---|---|---|---|
| 6 | 5,9 | 602 | 16,5 | 0,79 |
| 8 | 10,5 | 1071 | 29,4 | 1,40 |
| 10 | 16,4 | 1672 | 45,9 | 2,20 |
| 12 | 23,6 | 2406 | 66,1 | 3,10 |
| 13 | 27,8 | 2835 | 77,8 | 3,68 |
| 16 | 42,0 | 4283 | 117,6 | 5,60 |

> **AYDI-Praxishinweis:** G43 ist der Sweet Spot für die meisten Fahrtenyachten. Sie erlaubt bei gleicher Sicherheit eine Nennmaß-Reduktion gegenüber G30 (z. B. 8 mm G43 statt 10 mm G30), was erhebliches Gewicht im Bug spart. Voraussetzung: Kettennuss der Ankerwinsch muss für den gewählten Durchmesser kalibriert sein.

#### 2.1.4 Grade 70 (G70) — Transport Chain / High-Performance

**Beschreibung:** G70 ist eine hochfeste Kette, ursprünglich als Ladungssicherungskette (Transport Chain) entwickelt. Im Yachtbereich wird sie als Leichtbau-Alternative verwendet — gleiche Bruchlast bei deutlich reduziertem Durchmesser und Gewicht. G70 ist typischerweise legierter Stahl, vergütet.

**Eigenschaften:**
- Mindestbruchlast: ca. 3,0-fache der WLL
- Stahl: legierter Vergütungsstahl (Cr-Mo oder Mn-Legierung)
- Härte: ca. 250–350 HB
- Dehnung bei Bruch: >8%
- Spröderes Bruchverhalten als G30/G43

**Einsatzbereich im Yachtbau:**
- Performance-Yachten und Regattaboote (Gewichtseinsparung)
- Superyachten (Nennmaß-Reduktion für leichtere Handhabung)
- Heckanker-Kette (kurze Vorlauflängen, Gewicht kritisch)

**Typische WLL-Werte G70:**

| Nennmaß (mm) | WLL (kN) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) |
|---|---|---|---|---|
| 6 | 8,2 | 836 | 24,6 | 0,79 |
| 8 | 14,6 | 1489 | 43,7 | 1,40 |
| 10 | 22,8 | 2325 | 68,4 | 2,20 |
| 12 | 32,8 | 3345 | 98,4 | 3,10 |
| 13 | 38,6 | 3936 | 115,8 | 3,68 |
| 16 | 58,4 | 5955 | 175,2 | 5,60 |

> **AYDI-Warnung:** G70-Kette hat ein spröderes Bruchverhalten als G30/G43. Es erfolgt weniger Vorwarnung durch plastische Verformung. Bei schlagartiger Belastung (Rucklast bei Wellengang) kann dies zum plötzlichen Bruch führen. G70 sollte daher immer mit einem Ruckdämpfer (snubber/bridle) verwendet werden.

#### 2.1.5 Vergleichstabelle der Güteklassen

| Eigenschaft | G30 | G40 | G43 | G70 |
|---|---|---|---|---|
| Relative Bruchlast | 1,00 | 1,33 | 1,57 | 2,34 |
| Stahl | Baustahl | Mittelkarbon | Mittelkarbon WB | Legiert vergütet |
| Dehnung | >15% | >12% | >10% | >8% |
| Bruchverhalten | Duktil | Halbduktil | Halbduktil | Eher spröde |
| Schweißbarkeit | Gut | Mittel | Bedingt | Nein |
| Kosten (relativ) | 1,00 | 1,15 | 1,30 | 2,50 |
| Empfehlung | Kleinboot/Küste | Standard Küste | Fahrt/Blauwasser | Performance/Leichtbau |

> **AYDI-Wichtig:** Grade 80 (G80) und Grade 100 (G100) Ketten aus dem Hebezeugbereich sind für den Ankerbetrieb NICHT geeignet. Sie haben zu kurze Glieder (enge Teilung), passen nicht in Standard-Kettennüsse und sind extrem spröde. Ihr Einsatz als Ankerkette ist gefährlich.

### 2.2 DIN 766 vs. ISO 4565 — Die Normfrage

#### 2.2.1 DIN 766 — Der europäische Standard

DIN 766 definiert kurzgliedrige Rundstahlkette mit kalibrierten Abmessungen. „Kalibriert" bedeutet: Innenweite, Außenweite und Teilung sind enger toleriert als bei unkalibrierter Kette, damit die Kette zuverlässig über eine Kettennuss (Wildcat) läuft.

**Maßdefinitionen DIN 766:**

| Nennmaß d (mm) | Teilung p (mm) | Innenweite b1 (mm) | Außenweite b2 (mm) | Außenlänge L (mm) |
|---|---|---|---|---|
| 6 | 18,5 ± 0,5 | 7,5 ± 0,5 | 21,0 ± 1,0 | 24,5 |
| 7 | 22,0 ± 0,5 | 9,0 ± 0,5 | 25,0 ± 1,0 | 29,0 |
| 8 | 24,0 ± 0,5 | 10,0 ± 0,5 | 28,0 ± 1,0 | 32,0 |
| 10 | 28,0 ± 0,5 | 12,0 ± 0,5 | 34,0 ± 1,0 | 38,0 |
| 12 | 36,0 ± 0,7 | 15,0 ± 0,7 | 42,0 ± 1,2 | 48,0 |
| 13 | 36,0 ± 0,7 | 15,0 ± 0,7 | 45,0 ± 1,2 | 49,0 |
| 14 | 42,0 ± 0,7 | 17,0 ± 0,7 | 50,0 ± 1,2 | 56,0 |
| 16 | 45,0 ± 0,8 | 19,0 ± 0,8 | 56,0 ± 1,5 | 61,0 |

**Toleranzklasse:** Die kalibrierten Maße (insbesondere Teilung p und Innenweite b1) müssen innerhalb der angegebenen Toleranzen liegen. Nur kalibrierte Kette darf über eine Kettennuss gefahren werden.

#### 2.2.2 ISO 4565 — Der internationale Standard

ISO 4565 (Short link chain for lifting purposes — Calibrated) ist die internationale Entsprechung zu DIN 766. Die Maße sind weitgehend identisch, die Toleranzen jedoch teilweise enger gefasst. ISO 4565 definiert zusätzlich Güteklassen (Grade 30, Grade 40) direkt in der Norm.

**Unterschiede DIN 766 vs. ISO 4565:**

| Merkmal | DIN 766 | ISO 4565 |
|---|---|---|
| Geltungsbereich | Deutschland/Europa | International |
| Güteklassen | Nicht in der Norm definiert | Grade 30, Grade 40 |
| Teilungstoleranzen | ± 0,5–0,8 mm | ± 0,4–0,6 mm (teilweise enger) |
| Prüfanforderungen | Werksbescheinigung 2.1 | Abnahmeprüfzeugnis 3.1 möglich |
| Kennzeichnung | Herstellermarke | Herstellermarke + Grade |
| Verfügbarkeit | Europa, Standard | Weltweit, zunehmend |

> **AYDI-Praxishinweis:** In der Praxis sind DIN 766 und ISO 4565 für den Yachteigner austauschbar. Die Teilungsmaße sind identisch, sodass alle Standard-Kettennüsse beide Normketten aufnehmen. Beim Kauf auf die Kennzeichnung „kalibriert" oder „calibrated" achten — unkalibrierte Kette (DIN 5685) ist deutlich billiger, passt aber NICHT zuverlässig in eine Kettennuss.

#### 2.2.3 Kalibriert vs. Proof Coil vs. BBB — Begriffsklärung

Die Terminologie rund um Ankerketten ist international uneinheitlich und führt regelmäßig zu Verwirrung:

| Begriff | Bedeutung | Normbeziehung | Kettennuss-tauglich |
|---|---|---|---|
| Kalibriert (calibrated) | Enge Teilungstoleranzen | DIN 766 / ISO 4565 | Ja |
| Proof Coil | Werkseitig proof-getestet, G30 | US-Standard | Nein (oft unkalibriert) |
| BBB (Triple-B) | US-Kettentyp mit kurzer Teilung | NACM Standard | Ja (US-Kettennüsse) |
| High Test (HT) | Höhere Güteklasse, G43 | NACM Standard | Ja (wenn kalibriert) |
| DIN 5685 | Unkalibrierte Rundstahlkette | DIN | Nein |
| Stud Link | Kette mit Mittelsteg | ISO 1704 | Nein (Spezial-Kettennuss) |

> **AYDI-Warnung:** Unkalibrierte Kette (DIN 5685, „Baumarktkette") darf NIEMALS über eine Kettennuss gefahren werden. Die unregelmäßige Teilung führt zu Verklemmen, Überspringen und potenziellem Kettenriss unter Last. Unkalibrierte Kette ist ausschließlich für handbetriebene Systeme (Handleine/Seilwinde ohne Kettennuss) geeignet.

### 2.3 Galvanisiert vs. Edelstahl

#### 2.3.1 Feuerverzinkte Kette (Hot-Dip Galvanized)

Feuerverzinkung ist der Standardkorrosionsschutz für Ankerketten. Die Kette wird nach der Fertigung in ein Zinkbad (ca. 450°C) getaucht, wobei eine Zink-Eisen-Legierungsschicht und eine reine Zinkschicht entsteht.

**Vorteile:**
- Kostengünstig (Standardausführung)
- Guter Korrosionsschutz für 5–15 Jahre (je nach Revier und Nutzung)
- Opferanodenwirkung: Zink korrodiert vor dem Stahl und schützt Beschädigungen
- Unempfindlich gegen mechanischen Abrieb am Meeresgrund (Zinkschicht erneuert sich teilweise)
- Kein galvanisches Problem mit verzinkten Ankern und Stahlbeschlägen

**Nachteile:**
- Endliche Lebensdauer des Zinküberzugs (10–20 µm pro Jahr in Salzwasser)
- Verfärbung (grau-weiß → braun-rot bei Zinkverlust)
- Tropenwasser und hohe Temperaturen beschleunigen den Zinkabbau
- Beschädigte Stellen (Kratzer, Abrieb) rosten lokal

**Zinkschichtdicken nach DIN EN ISO 1461:**

| Nennmaß (mm) | Mindest-Zinkschicht (µm) | Typische Zinkschicht (µm) | Gewichtszunahme (%) |
|---|---|---|---|
| 6 | 45 | 60–80 | 3–5 |
| 8 | 55 | 70–100 | 3–5 |
| 10 | 55 | 80–120 | 3–5 |
| 12 | 70 | 100–150 | 3–5 |
| 14 | 70 | 100–150 | 3–5 |
| 16 | 70 | 120–180 | 3–5 |

> **AYDI-Praxishinweis:** Die Zinkschichtdicke ist der wichtigste Qualitätsindikator für die Lebensdauer. Billige Import-Ketten haben oft nur 30–40 µm — weniger als die Hälfte der Norm. Ein einfacher Test: Zinkschicht mit einem Multimeter messen (Schichtdickenmessgerät) oder die Kette nach dem ersten Ankermanöver prüfen — blättert die Verzinkung ab, ist die Qualität ungenügend.

#### 2.3.2 Edelstahlkette (Stainless Steel)

Edelstahl-Ankerketten werden aus austenitischem Edelstahl AISI 316L (1.4404) oder AISI 316 (1.4401) gefertigt. Sie bieten dauerhaften Korrosionsschutz, sind aber deutlich teurer und haben spezifische Schwächen.

**Vorteile:**
- Kein Korrosionsschutz-Verschleiß (kein Zinkverlust)
- Ästhetisch ansprechend (glänzend, kein Rost)
- Längere Lebensdauer bei sachgemäßer Pflege (20+ Jahre)
- Kein Zinkabrieb im Kettenkasten

**Nachteile:**
- 3–5× teurer als verzinkte Kette gleicher Güteklasse
- Geringere Bruchlast als vergüteter Kohlenstoffstahl gleichen Durchmessers
- Anfällig für Spaltkorrosion (crevice corrosion) in sauerstoffarmer Umgebung
- Anfällig für Spannungsrisskorrosion (stress corrosion cracking, SCC) in warmem Salzwasser
- Galvanische Probleme mit verzinkten Ankern und Stahlschäkeln
- NICHT schweißbar ohne Festigkeitsverlust

**Typische Festigkeitswerte AISI 316L Ankerkette:**

| Nennmaß (mm) | WLL (kN) | Bruchlast (kN) | Gewicht (kg/m) | Preis-Faktor vs. verzinkt |
|---|---|---|---|---|
| 6 | 3,2 | 9,6 | 0,79 | 3,5× |
| 8 | 5,7 | 17,1 | 1,40 | 3,5× |
| 10 | 8,9 | 26,7 | 2,20 | 4,0× |
| 12 | 12,8 | 38,4 | 3,10 | 4,0× |
| 13 | 15,1 | 45,3 | 3,68 | 4,0× |
| 16 | 22,8 | 68,4 | 5,60 | 4,5× |

> **AYDI-Warnung:** Edelstahl-Ankerketten haben GERINGERE Bruchlastwerte als G43-Kohlenstoffstahlketten gleichen Durchmessers. Die Bruchlast einer 10 mm Edelstahlkette (26,7 kN) entspricht nur einer 8 mm G43-Kette (29,4 kN). Bei der Dimensionierung muss dies berücksichtigt werden. Edelstahlkette ist KEIN direkter Ersatz für G43-Kette gleichen Durchmessers, wenn die Festigkeit maßgeblich ist.

> **AYDI-Warnung Spaltkorrosion:** Edelstahlketten, die dauerhaft im Kettenkasten liegen (Salzwasser-feucht, wenig Sauerstoff), können Spaltkorrosion an den Gliedverbindungen entwickeln. Dies ist äußerlich nicht sichtbar und kann zu plötzlichem Bruch führen. Edelstahlketten müssen nach jedem Einsatz gründlich mit Süßwasser gespült und in trockenem Zustand gelagert werden.

#### 2.3.3 Galvanische Kompatibilität

Die Wahl des Kettenmaterials hat direkte Auswirkungen auf die galvanische Kompatibilität mit anderen Metallteilen des Ankergeschirrs:

| Kombination | Galvanisches Risiko | Empfehlung |
|---|---|---|
| Verzinkte Kette + verzinkter Anker | Kein Risiko | Standard, empfohlen |
| Verzinkte Kette + Edelstahlanker | Kette opfert (beschleunigter Zinkverlust) | Akzeptabel mit Opferanode |
| Verzinkte Kette + Alu-Anker | Anker opfert leicht | Akzeptabel |
| Edelstahlkette + Edelstahlanker | Kein Risiko | Ideal (aber teuer) |
| Edelstahlkette + verzinkter Anker | Anker/Zink opfert stark | Nicht empfohlen |
| Edelstahlkette + Alu-Anker | Anker opfert stark | Nicht empfohlen |

### 2.4 Gliedabmessungen und Kettenteilung

Die Gliedabmessungen bestimmen die Kompatibilität mit Kettennuss (Wildcat), Kettenstopper und Bugrolle. Die folgenden Maße sind für die Konstruktion und Bauteilauswahl entscheidend:

#### 2.4.1 Anatomie eines Kettenglieds

```
          ┌──────────────────┐
          │    Außenlänge L   │
          │                  │
     ┌────┤     ┌──────┐    ├────┐
     │    │     │      │    │    │
     │    │  b1 │Innen-│    │    │  b2 (Außenweite)
     │    │     │weite │    │    │
     │    │     │      │    │    │
     ├────┤     └──────┘    ├────┤
     │    │                  │
     │    │  ←── p ──→       │
     │    │  (Teilung)       │
     └────┴──────────────────┘
          d = Nennmaß (Drahtdurchmesser)
```

#### 2.4.2 Kritische Maße für die Kettennuss-Kompatibilität

Die Kettennuss (Wildcat) einer Ankerwinsch ist auf eine spezifische Kette kalibriert. Die folgenden Maße müssen übereinstimmen:

1. **Teilung p:** Abstand zwischen den Mittelpunkten zweier benachbarter Glieder. Muss exakt zur Kettennuss passen.
2. **Nennmaß d:** Drahtdurchmesser. Bestimmt die Taschentiefe der Kettennuss.
3. **Innenweite b1:** Muss groß genug sein, damit das Glied über den Kettennuss-Steg greift.

> **AYDI-Praxishinweis:** Bei Kettenwechsel oder Winsch-Retrofit IMMER den Kettenhersteller UND den Winsch-Hersteller konsultieren. Ein Teilungsunterschied von 1 mm kann ausreichen, um die Kette unter Last aus der Kettennuss springen zu lassen — eine lebensgefährliche Situation.

### 2.5 WLL, Bruchlast und Sicherheitsfaktoren

#### 2.5.1 Definitionen

- **WLL (Working Load Limit):** Die maximale Last, die im normalen Betrieb dauerhaft aufgebracht werden darf. KEIN Sicherheitsfaktor enthalten.
- **Proof Load (Prüflast):** Die Last, mit der jede Kette werkseitig geprüft wird. Typisch 2× WLL.
- **Breaking Load (Bruchlast/MBL):** Die Last, bei der die Kette rechnerisch versagt. Typisch 3–4× WLL (je nach Grade).
- **Sicherheitsfaktor:** Verhältnis Bruchlast / tatsächliche Betriebslast. Empfohlen: ≥4:1 für Ankerketten.

#### 2.5.2 Praxis-Belastungen beim Ankern

Die tatsächliche Belastung einer Ankerkette hängt von Windstärke, Wellengang, Strömung und Kettenlänge (Scope) ab:

| Windstärke (kn) | Typische Zuglast 10m-Yacht (kN) | Typische Zuglast 14m-Yacht (kN) | Typische Zuglast 20m-Yacht (kN) |
|---|---|---|---|
| 10 (leichte Brise) | 0,5 | 0,8 | 1,5 |
| 20 (frische Brise) | 2,0 | 3,2 | 6,0 |
| 30 (steifer Wind) | 4,5 | 7,2 | 13,5 |
| 40 (Sturm) | 8,0 | 12,8 | 24,0 |
| 50 (schwerer Sturm) | 12,5 | 20,0 | 37,5 |
| 60 (orkanartig) | 18,0 | 28,8 | 54,0 |

> **AYDI-Hinweis:** Diese Werte sind statische Windlasten. Dynamische Rucklasten (Welle, Schwell, Gieren) können das 2–3-fache der statischen Last erreichen. Die Kettendimensionierung muss daher mit einem dynamischen Faktor von mindestens 2,5 erfolgen.

---

## 3. Typenübersicht

### 3.1 Kurzgliedrige Kette (Short Link Chain)

#### 3.1.1 Beschreibung und Merkmale

Die kurzgliedrige Rundstahlkette nach DIN 766 / ISO 4565 ist der Standardtyp für Yachtankerketten. „Kurzgliedrig" bezieht sich auf das Verhältnis von Glied-Innenlänge zu Nennmaß (ca. 3:1), das eine kompakte Stapelung im Kettenkasten und zuverlässigen Lauf über die Kettennuss gewährleistet.

**Merkmale:**
- Teilung p = ca. 3× Nennmaß d (z. B. 24 mm bei 8 mm Kette)
- Kalibrierte Abmessungen für Kettennuss-Betrieb
- Glieder wechseln sich in der Orientierung ab (stehend/liegend)
- Keine Stege oder Verstärkungen in den Gliedern
- Verschweißte Glieder (Stumpfschweißung)

**Vorteile:**
- Standard für alle gängigen Ankerwinsch-Kettennüsse
- Kompakte Stapelung im Kettenkasten
- Selbstsortierend beim Einfahren (geringes Verklemmrisiko)
- Breites Angebot an Güteklassen und Materialien
- Leicht reparierbar durch Austausch einzelner Glieder (mit Kettenverbinder)

**Nachteile:**
- Höheres Gewicht pro Meter als langgliedrige Kette gleicher Bruchlast
- Steiferer Kettenstrang als langgliedrige Kette (weniger flexibel)
- Neigung zum Verdrallen bei ungleichmäßigem Einfahren

**Einsatzbereich:**
- Primäranker aller Yachttypen 6–25 m
- Standard für Fahrtensegler und Blauwasseryachten
- Einziger Typ, der universell mit Ankerwinsch-Kettennüssen kompatibel ist

#### 3.1.2 Kettenteilung und Kettennuss-Zuordnung

| Nennmaß (mm) | Teilung DIN 766 (mm) | Passende Kettennüsse (Auswahl) |
|---|---|---|
| 6 | 18,5 | Lofrans, Quick, Maxwell, Lewmar (6mm DIN) |
| 7 | 22,0 | Lofrans, Quick (7mm DIN — selten) |
| 8 | 24,0 | Alle gängigen Hersteller (8mm DIN) |
| 10 | 28,0 | Alle gängigen Hersteller (10mm DIN) |
| 12 | 36,0 | Lofrans, Quick, Maxwell, Muir (12mm DIN) |
| 13 | 36,0 | Lewmar, Muir (13mm DIN — Achtung: p identisch mit 12mm!) |
| 14 | 42,0 | Lofrans, Quick, Maxwell (14mm DIN) |
| 16 | 45,0 | Quick, Muir (16mm DIN — Großyachten) |

> **AYDI-Warnung:** 12 mm und 13 mm DIN-766-Kette haben identische Teilung (36 mm)! Die Kettennuss unterscheidet sich nur in der Taschenbreite. Es ist physisch möglich, eine 12mm-Kette auf eine 13mm-Kettennuss zu legen (und umgekehrt), was zu gefährlichem Schlupf unter Last führt. IMMER Nennmaß UND Teilung verifizieren.

### 3.2 Langgliedrige Kette (Long Link Chain)

#### 3.2.1 Beschreibung und Merkmale

Langgliedrige Kette (DIN 5685-C) hat ein Teilungsverhältnis von ca. 4–5× Nennmaß. Sie wird im Yachtbereich nur in Sonderfällen eingesetzt.

> ✅ Aufgeloest (Audit): DIN 5685-C = langgliedrige Rundstahlkette (bestätigt; DIN 5685-A = kurzgliedrig). Die zuvor zitierte „ISO 4568" normt „Windlasses and anchor capstans" (Ankerwinden/Ankerspills), NICHT die Kette, und wurde daher gestrichen. Für langgliedrige Rundstahlkette existiert keine eindeutige ISO-Entsprechung (verwandte deutsche Norm: DIN 763). Confidence: documented. — Quelle: ISO 4568:2021 „Ships and marine technology — Sea-going vessels — Windlasses and anchor capstans" (iso.org/standard/77584.html); DIN 5685-A/-C Herstellerspezifikationen (pewag, h-lift).

**Merkmale:**
- Teilung p = ca. 4–5× Nennmaß d
- Höhere Flexibilität als kurzgliedrige Kette
- Geringeres Gewicht pro Meter bei gleicher Bruchlast
- NICHT kalibriert (Standardausführung)
- NICHT kompatibel mit Standard-Kettennüssen

**Vorteile:**
- Leichter pro Meter als kurzgliedrige Kette
- Flexibler, bessere Anpassung an Meeresgrundkonturen
- Günstiger als kurzgliedrige kalibrierte Kette

**Nachteile:**
- NICHT für Ankerwinsch-Kettennüsse geeignet (falsche Teilung)
- Neigung zum Verklemmen und Verknoten im Kettenkasten
- Schlechteres Stauverhalten (größeres Volumen pro kg)
- Geringere Verfügbarkeit in Yacht-relevanten Güteklassen

**Einsatzbereich:**
- Mooringleinen und Festmacherketten
- Dinghy-Ankerketten (handgeführt)
- Historische Yachten ohne Ankerwinsch
- Sicherungsketten am Ankerplatz (Diebstahlschutz)

> **AYDI-Praxishinweis:** Langgliedrige Kette hat im modernen Yachtbau kaum noch Relevanz als Primär-Ankerkette. Sie wird gelegentlich als preiswerte Vorlaufkette für Trailer-Boote oder als Mooringkette verwendet. Für alle Yachten mit Ankerwinsch ist kurzgliedrige kalibrierte Kette (DIN 766) der einzig sinnvolle Standard.

### 3.3 Stegkette (Stud Link Chain)

#### 3.3.1 Beschreibung und Merkmale

Stegkette (auch: Stegliedkette, Stud Link Chain) hat einen Quersteg in der Mitte jedes Gliedes, der Verformung unter Last verhindert und die Verdrehneigung reduziert. Stegkette ist der Standard in der Berufsschifffahrt, im Yachtbereich jedoch nur bei Superyachten ab ca. 25 m üblich.

**Merkmale:**
- Gegossener oder geschweißter Mittelsteg in jedem Glied
- Teilung und Maße nach ISO 1704 / DIN 82101
- Typisch G2 oder G3 nach IACS-Standard
- Sehr hohe Bruchlasten (Berufsschifffahrt-Standard)
- Erfordert spezielle Stegketten-Kettennüsse

**Vorteile:**
- Höchste Verdrehfestigkeit aller Kettentypen
- Kein Verknoten im Kettenkasten
- Höchste Bruchlasten
- Standard für Klassifikationsgesellschaften (Lloyd's, DNV, ABS)

**Nachteile:**
- Schwerer als kurzgliedrige Kette gleicher Bruchlast
- Deutlich teurer
- Spezielle Kettennüsse erforderlich
- Spezielle Verbinder (Kenter-Schäkel, Bügelschäkel) erforderlich
- Nur für Großyachten ab ca. 25 m relevant

**Einsatzbereich:**
- Superyachten >25 m (klassifizierte Yachten)
- Yachten mit Klassifikation (Lloyd's, DNV, ABS)
- Expeditionsyachten mit Schifffahrts-Ankerausrüstung

> **AYDI-Hinweis:** Stegkette nach ISO 1704 hat ANDERE Teilungsmaße als DIN 766. Eine Stegketten-Kettennuss kann keine DIN-766-Kette fahren und umgekehrt. Bei Superyacht-Projekten muss die Kettennorm frühzeitig festgelegt werden, da sie das gesamte Ankergeschirr-Design bestimmt.

### 3.4 Ketten-Tau-Kombination (Chain-Rope Rode)

#### 3.4.1 Konzept und Aufbau

Eine Ketten-Tau-Kombination (Chain-Rope Rode) besteht aus einem Kettenvorlauf (typisch 5–20 m Kette) und einem Ankertau (typisch 30–60 m Nylon-Leine). Die Kette wird direkt am Anker befestigt und dient als abriebfester Vorlauf am Meeresgrund, während das leichtere Tau den Großteil der Strecke überbrückt.

**Aufbau (von Anker zu Schiff):**
1. Anker
2. Schäkel (Anker → Kette)
3. Kettenvorlauf (5–20 m kurzgliedrige Kette)
4. Chain-to-Rope-Splice oder Kettenverbinder-Schäkel
5. Ankertau (30–60 m Drei-Schlag oder geflochtenes Nylon)
6. Kausch + Festpunkt im Kettenkasten (Belegklampe oder Ankerbelegpunkt)

**Vorteile:**
- Deutlich leichter als All-Chain-Rode (60–80% Gewichtseinsparung)
- Elastizität des Nylontaus wirkt als natürlicher Ruckdämpfer
- Geringeres Volumen im Kettenkasten
- Niedrigere Anschaffungskosten
- Bessere Seegangseigenschaften (weniger Gewicht im Bug)

**Nachteile:**
- Geringere Abriebfestigkeit (Tau am Meeresgrund)
- Weniger Kettenary-Effekt (flacherer Zugwinkel erfordert mehr Scope)
- Tau kann an Felsen, Korallen oder Wracks scheuern
- Tau ist UV-empfindlich und muss regelmäßig getauscht werden
- Kettenwinsch-Betrieb nur für den Kettenteil — Tau muss per Hand oder Seilwinsch eingeholt werden

#### 3.4.2 Dimensionierungstabelle Chain-Rope Rode

| Bootslänge (m) | Kettenvorlauf (m) | Kettengröße (mm) | Tau-Durchmesser (mm) | Tau-Länge (m) | Tau-Material |
|---|---|---|---|---|---|
| 6–8 | 5–8 | 6 | 10–12 | 30–40 | 3-Schlag Nylon |
| 8–10 | 8–12 | 8 | 12–14 | 40–50 | 3-Schlag Nylon |
| 10–12 | 10–15 | 8–10 | 14–16 | 40–60 | 3-Schlag Nylon |
| 12–14 | 12–20 | 10 | 16–18 | 50–60 | 3-Schlag Nylon |
| 14–16 | 15–25 | 10–12 | 18–20 | 50–80 | 3-Schlag Nylon |

> **AYDI-Praxishinweis:** Der Kettenvorlauf sollte mindestens so lang sein wie die maximale Wassertiefe im Einsatzrevier + 3 m. So liegt bei normalem Scope (5:1) immer Kette auf dem Meeresgrund. In Korallenrevieren (Karibik, Pazifik) sollte der Kettenvorlauf auf 20+ m erhöht werden, um das empfindliche Tau vor Abrieb zu schützen.

#### 3.4.3 Chain-to-Rope-Splice

Die Verbindung zwischen Kettenvorlauf und Ankertau ist ein sicherheitskritischer Punkt. Es gibt drei Methoden:

**1. Gespleißte Verbindung (Chain Splice):**
Das Tauende wird durch das letzte Kettenglied geführt und zurückgespleißt. Festigkeit: 85–95% der Tau-Bruchlast. Vorteil: Kompakt, läuft durch Bugrolle. Nachteil: Nicht lösbar, erfordert Spleißkenntnisse.

**2. Kausch + Schäkel:**
Das Tauende wird um eine Kausch (Thimble) gespleißt, diese wird per Schäkel am letzten Kettenglied befestigt. Festigkeit: 80–90% der Tau-Bruchlast. Vorteil: Lösbar, einfach herzustellen. Nachteil: Schäkel kann an Bugrolle haken.

**3. Kettenverbinder-Schäkel (Chain-Rope Connector):**
Spezieller Verbinder, der ein Tauauge direkt an ein Kettenglied klemmt. Festigkeit: 70–85% der Tau-Bruchlast. Vorteil: Einfach, keine Spleißkenntnisse. Nachteil: Geringste Festigkeit, kann sich lösen.

### 3.5 All-Chain-Rode (Komplettkette)

#### 3.5.1 Konzept und Vorteile

Ein All-Chain-Rode besteht ausschließlich aus Kette — vom Anker bis zum Festpunkt im Kettenkasten. Dies ist der Standard für Fahrtenyachten ab ca. 10 m und für alle Blauwasseryachten.

**Vorteile:**
- Maximale Abriebfestigkeit am Meeresgrund
- Maximaler Kettenary-Effekt (flacher Zugwinkel am Anker)
- Vollautomatischer Winsch-Betrieb (Fieren und Einholen)
- Kein Schamfilen/Scheuern
- Kein UV-Alterung wie bei Tau
- Einfaches Markierungssystem (Farbkodierung)

**Nachteile:**
- Hohes Gewicht im Bug (80–200+ kg)
- Hohe Anschaffungskosten
- Kein Ruckdämpfung ohne Snubber/Bridle
- Großer Kettenkasten erforderlich
- Vertrimmung bei leerem vs. vollem Kettenkasten

#### 3.5.2 Typische All-Chain-Rode-Längen

| Bootslänge (m) | Empfohlene Kettenlänge (m) | Min. Kettenlänge (m) | Blauwasser-Empfehlung (m) |
|---|---|---|---|
| 8–10 | 40–50 | 30 | 60–80 |
| 10–12 | 50–60 | 40 | 80–100 |
| 12–14 | 60–80 | 50 | 100–120 |
| 14–16 | 80–100 | 60 | 100–150 |
| 16–20 | 100–120 | 80 | 120–150 |
| 20–25 | 120–150 | 100 | 150–200 |

### 3.6 Drei-Schlag-Nylontau als Rode (Three-Strand Nylon Rode)

#### 3.6.1 Beschreibung

Drei-Schlag-Nylontau (Three-Strand Twisted Nylon) ist das klassische Ankertau-Material. Es bietet hervorragende Elastizität (15–25% Dehnung bei WLL), die als natürlicher Ruckdämpfer wirkt.

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Material | Polyamid 6 (PA6) oder Polyamid 6.6 (PA66) |
| Konstruktion | 3 Kardeele, Z-Schlag (rechtsdrehend) |
| Bruchdehnung | 20–35% |
| Arbeitsdehnung bei WLL | 15–25% |
| UV-Beständigkeit | Mittel (5–7 Jahre bei dauerhafter Exposition) |
| Wasseraufnahme | 3–8% (Festigkeitsverlust ~10% nass) |
| Schmelzpunkt | 215–260°C |
| Spezifisches Gewicht | 1,14 g/cm³ (sinkt) |
| Abriebfestigkeit | Mittel |

**Dimensionierung:**

| Bootslänge (m) | Tau-Durchmesser (mm) | Bruchlast (kN) | WLL (kN) | Gewicht (kg/m) |
|---|---|---|---|---|
| 6–8 | 10 | 12,5 | 2,5 | 0,055 |
| 8–10 | 12 | 18,0 | 3,6 | 0,079 |
| 10–12 | 14 | 24,5 | 4,9 | 0,107 |
| 12–14 | 16 | 32,0 | 6,4 | 0,140 |
| 14–16 | 18 | 40,5 | 8,1 | 0,177 |
| 16–20 | 20 | 50,0 | 10,0 | 0,218 |

> **AYDI-Praxishinweis:** Drei-Schlag-Nylon ist spezifisch als Ankertau geeignet, weil es hohe Elastizität mit guter Festigkeit verbindet. Geflochtenes (Kern-Mantel-) Nylontau hat weniger Dehnung und bietet daher weniger Ruckdämpfung. Polyester-Tauwerk ist als Ankertau NICHT geeignet — zu geringe Dehnung, zu steif.

### 3.7 High-Modulus Rode (HMPE / Dyneema)

#### 3.7.1 Beschreibung

High-Modulus-Polyethylen-Tauwerk (HMPE, Markenname: Dyneema, Spectra) wird gelegentlich als leichtes Ankertau diskutiert. Es bietet extreme Bruchlast bei minimalem Gewicht und Durchmesser.

**Eigenschaften:**

| Eigenschaft | Wert |
|---|---|
| Material | Ultra-High Molecular Weight PE (UHMWPE) |
| Konstruktion | 12-fach geflochten oder Kern-Mantel |
| Bruchdehnung | 3–5% |
| Arbeitsdehnung bei WLL | 1–2% |
| UV-Beständigkeit | Gut (10+ Jahre) |
| Wasseraufnahme | 0% |
| Schmelzpunkt | 145°C (!) |
| Spezifisches Gewicht | 0,97 g/cm³ (schwimmt!) |
| Abriebfestigkeit | Hoch |

**Probleme als Ankertau:**

1. **Zu geringe Elastizität:** Nur 1–2% Arbeitsdehnung bietet keinerlei Ruckdämpfung. Bei Wellengang werden extreme Spitzenlasten auf Anker und Bugrolle übertragen.
2. **Schwimmt:** Sinkt nicht ab, liegt an der Oberfläche, wo es von anderen Booten überfahren werden kann.
3. **Niedrige Schmelztemperatur:** Kann bei Reibung am Meeresgrund (Felsen, Wrack) durch Hitzeentwicklung schmelzen.
4. **Kriechneigung (Creep):** Unter Dauerlast verlängert sich HMPE permanent — der Rode verliert Spannung.

> **AYDI-Warnung:** HMPE/Dyneema ist als alleiniges Ankertau NICHT empfohlen. Es kann als Vorlauf in Kombination mit Nylon-Ruckdämpfer verwendet werden, bietet aber keinen Vorteil gegenüber einer konventionellen Ketten-Tau-Kombination. Die fehlende Elastizität ist bei Ankerbetrieb ein schwerwiegender Nachteil.

---

## 4. Dimensionierung

### 4.1 Grundregeln der Kettendimensionierung

Die Dimensionierung der Ankerkette basiert auf vier Hauptfaktoren:

1. **Bootsgröße (LOA und Verdrängung):** Bestimmt die Windangriffsfläche und damit die Ankerlast.
2. **Einsatzgebiet:** Küstenfahrt, Mittelmeer, Atlantik, Tropen, Hochsee.
3. **Ankerdauer:** Tagesankerung, Übernachtung, Langzeitankerung, Sturmverankerung.
4. **Kettenary-Effekt und Scope:** Verhältnis Kettenlänge zu Wassertiefe.

#### 4.1.1 Faustregeln (Rules of Thumb)

**Kettendurchmesser:**
- 1 mm Kette pro 1,5 m Bootslänge (Küstenfahrt G40)
- 1 mm Kette pro 2 m Bootslänge (Blauwasser G43)
- Beispiel: 12 m Yacht → 8 mm G40 oder 8 mm G43

**Kettenlänge (All-Chain):**
- Minimum: 4× maximale Ankerwassertiefe
- Standard: 5× maximale Ankerwassertiefe + 20 m Reserve
- Blauwasser: 6× maximale Ankerwassertiefe + 30 m Reserve
- Beispiel: Max. Tiefe 15 m → Min. 60 m, Standard 95 m, Blauwasser 120 m

**Scope (Verhältnis Kettenlänge : Wassertiefe):**
- Kette allein: 3:1 (ruhig) bis 7:1 (Sturm)
- Ketten-Tau-Kombi: 5:1 (ruhig) bis 10:1 (Sturm)
- Optimal: 5:1 bei Kette allein für normale Bedingungen

### 4.2 Dimensionierung nach Bootslänge (6–20 m)

#### 4.2.1 Kleinkreuzer und Trailer-Boote (6–8 m)

| Parameter | Empfehlung | Minimum |
|---|---|---|
| Kettendurchmesser | 6 mm G43 | 6 mm G30 |
| Kettenlänge (All-Chain) | 30–40 m | 20 m |
| Alternative: Chain-Rope | 5–8 m Kette + 30–40 m Nylon 10 mm | — |
| Kettengewicht (All-Chain 30m) | 24 kg | — |
| Ankergewicht (Ref.) | 4–6 kg | — |
| Winsch | Optional, manuell ausreichend | — |

**Konstruktive Hinweise:**
- Kettenkasten im Bug muss 30–40 m × 6 mm = 24–32 kg aufnehmen
- Bugrolle für 6 mm Kette + gewählten Anker dimensionieren
- Kettenstopper für 6 mm kalibrierte Kette
- Spülwasserablauf aus dem Kettenkasten in die Bilge

#### 4.2.2 Fahrtensegler (8–12 m)

| Parameter | Empfehlung | Minimum |
|---|---|---|
| Kettendurchmesser | 8 mm G43 | 8 mm G30 |
| Kettenlänge (All-Chain) | 50–80 m | 40 m |
| Alternative: Chain-Rope | 10–15 m Kette + 40–50 m Nylon 14 mm | — |
| Kettengewicht (All-Chain 60m) | 84 kg | — |
| Ankergewicht (Ref.) | 8–15 kg | — |
| Winsch | Empfohlen, 500–700 W | — |

**Konstruktive Hinweise:**
- 84 kg Kette im Bug beeinflusst den Trimm signifikant
- Kettenkasten: min. 0,05 m³ (50 Liter) für 60 m × 8 mm

> ⚠️ **ZU PRÜFEN (Audit):** Kettenkasten-Volumen „50 L" widerspricht der eigenen Berechnung — 60 m × 8 mm = 84 kg; nach Formel in 4.3.2 (Volumen = Gewicht × 1,8; Schüttdichte 0,55 kg/L) braucht die Kette allein ca. 150 L, mit 120 %-Reserve ca. 180 L (vgl. Beispiel S.1). 50 L können die Kette physikalisch nicht fassen. Analog zu prüfen: „150 L" für 100 m × 10 mm (real ≈ 400–475 L) und „300 L" für 120 m × 12 mm (real ≈ 670–800 L).
- Ankerwinde: min. 500 W, Kettennuss DIN 766 / 8 mm
- Snubber/Bridle: 12–14 mm Nylon, 8–10 m lang
- Freibord/Bugrolle: Ablauf muss 8 mm Kette + Anker führen

#### 4.2.3 Blauwasseryachten (12–16 m)

| Parameter | Empfehlung | Minimum |
|---|---|---|
| Kettendurchmesser | 10 mm G43 | 8 mm G43 |
| Kettenlänge (All-Chain) | 80–120 m | 60 m |
| Zweitkette (Heckanker) | 6–8 mm, 30 m + 50 m Nylon 14 mm | — |
| Kettengewicht (All-Chain 100m) | 220 kg | — |
| Ankergewicht (Ref.) | 15–25 kg | — |
| Winsch | Pflicht, 1000–1500 W | — |

**Konstruktive Hinweise:**
- 220 kg Kette im Bug erfordert sorgfältige Trimmanalyse
- Kettenkasten: min. 0,15 m³ (150 Liter) für 100 m × 10 mm
- Kettenstopperbelastung: min. 3000 kg (30 kN) WLL
- Strukturverstärkung Bugbereich: Ankerlasten werden über Bugrolle/Kettenstopper in den Rumpf eingeleitet
- Kettenkasten-Drainage: Pumpe oder großer Ablauf (Salzwasser-Ansammlung)
- Kettennuss-Wechselsatz für Zweitkette empfohlen

#### 4.2.4 Motoryachten und große Fahrtenyachten (16–20 m)

| Parameter | Empfehlung | Minimum |
|---|---|---|
| Kettendurchmesser | 12 mm G43 | 10 mm G43 |
| Kettenlänge (All-Chain) | 100–150 m | 80 m |
| Zweitkette | 8–10 mm, 60 m | — |
| Kettengewicht (All-Chain 120m) | 372 kg | — |
| Ankergewicht (Ref.) | 25–40 kg | — |
| Winsch | Pflicht, 1500–2500 W, hydraulisch bei >20 m | — |

**Konstruktive Hinweise:**
- 372 kg Kette im Bug ist eine massive Last — Strukturverstärkung obligatorisch
- Kettenkasten: min. 0,30 m³ (300 Liter) für 120 m × 12 mm
- Selbststapler-System empfohlen (Kettenkasten mit konischem Boden)
- Spülsystem: automatische Kettenspülung bei Einholen
- Kettenzähler: elektronisch, für die Navigation erforderlich
- Doppelrolle/Doppelkettenstopper bei Doppel-Anker-Setup

### 4.3 Kettengewicht-Berechnungen

#### 4.3.1 Gewicht nach Nennmaß und Länge

| Nennmaß (mm) | Gewicht (kg/m) | 30 m (kg) | 50 m (kg) | 80 m (kg) | 100 m (kg) | 120 m (kg) | 150 m (kg) |
|---|---|---|---|---|---|---|---|
| 6 | 0,79 | 23,7 | 39,5 | 63,2 | 79,0 | 94,8 | 118,5 |
| 7 | 1,10 | 33,0 | 55,0 | 88,0 | 110,0 | 132,0 | 165,0 |
| 8 | 1,40 | 42,0 | 70,0 | 112,0 | 140,0 | 168,0 | 210,0 |
| 10 | 2,20 | 66,0 | 110,0 | 176,0 | 220,0 | 264,0 | 330,0 |
| 12 | 3,10 | 93,0 | 155,0 | 248,0 | 310,0 | 372,0 | 465,0 |
| 13 | 3,68 | 110,4 | 184,0 | 294,4 | 368,0 | 441,6 | 552,0 |
| 14 | 4,30 | 129,0 | 215,0 | 344,0 | 430,0 | 516,0 | 645,0 |
| 16 | 5,60 | 168,0 | 280,0 | 448,0 | 560,0 | 672,0 | 840,0 |

#### 4.3.2 Kettenkasten-Volumenberechnung

Die gestapelte Kette nimmt deutlich mehr Volumen ein als die theoretische Massendichte vermuten lässt, da sich die Glieder nicht perfekt stapeln:

**Faustformel:** Volumen (Liter) = Kettengewicht (kg) × 1,8

| Nennmaß (mm) | Schüttdichte (kg/Liter) | 50 m Volumen (Liter) | 100 m Volumen (Liter) |
|---|---|---|---|
| 6 | 0,55 | 72 | 144 |
| 8 | 0,55 | 127 | 255 |
| 10 | 0,55 | 200 | 400 |
| 12 | 0,55 | 282 | 564 |
| 14 | 0,55 | 391 | 782 |
| 16 | 0,55 | 509 | 1018 |

> **AYDI-Konstruktionshinweis:** Der Kettenkasten muss mindestens 120% des berechneten Volumens fassen, um Raum für ungeordnete Stapelung und Kettenbewegung zu lassen. Der Schwerpunkt der gestapelten Kette liegt tief und weit vorn — ideal ist ein konischer Kasten, der die Kette nach unten und zur Mittschiffsachse führt.

### 4.4 Scope und Kettenary-Effekt

#### 4.4.1 Der Kettenary-Effekt

Der Kettenary-Effekt (von lat. catena = Kette) beschreibt die durchhängende Kurve einer unter Eigengewicht und Zuglast liegenden Kette. Diese Kurve bewirkt, dass der Zug am Anker flacher ist als der Zug am Schiff — der Anker wird nahezu horizontal belastet, was seine Haltekraft maximiert.

**Kritischer Parameter:** Der Winkel, unter dem die Kette den Anker erreicht. Idealwert: <8° zur Horizontalen. Ab >15° beginnt der Anker „auszubrechen" (der vertikale Kraftanteil hebt den Anker aus dem Grund).

| Scope (Kette:Tiefe) | Winkel am Anker (°) | Kettenary-Effekt | Bewertung |
|---|---|---|---|
| 3:1 | 18–25 | Gering | Nur bei Ruhe, kurzzeitig |
| 4:1 | 10–15 | Mittel | Küste, ruhige Bedingungen |
| 5:1 | 5–8 | Gut | Standard, empfohlen |
| 7:1 | 2–4 | Sehr gut | Starkwind, empfohlen |
| 10:1 | <2 | Maximal | Sturm, wenn Platz vorhanden |

> **AYDI-Praxishinweis:** Bei Ketten-Tau-Kombination liefert der Tau-Anteil KEINEN Kettenary-Effekt (zu leicht). Der Scope muss daher höher sein als bei All-Chain-Rode: 7:1 standard, 10:1 bei Starkwind. Die Kettenvorlauflänge bestimmt den effektiven Kettenary.

---

## 5. Produktlinien und Hersteller

### 5.1 Übersicht der Haupthersteller

Der Markt für Yacht-Ankerketten wird von einigen wenigen spezialisierten Herstellern dominiert. Daneben gibt es Kettenhersteller aus der Industriebranche, die kalibrierte Kette für den Yachtmarkt anbieten, und Ankerwinsch-Hersteller, die passende Ketten im Programm haben.

| Hersteller | Herkunft | Spezialität | Preissegment |
|---|---|---|---|
| Titan Marine | Taiwan/International | Kalibrierte G40/G43, BBB | Mittel |
| Acco / Peerless | USA | G30/G43, BBB, industrielle Kette | Mittel–Hoch |
| Maggi (Maggi Catene) | Italien | DIN 766, Edelstahl, kalibriert | Mittel–Hoch |
| Lofrans | Italien | Kette + Ankerwinsch-Systeme | Hoch |
| Quick | Italien | Kette + Ankerwinsch-Systeme | Hoch |
| Maxwell | Neuseeland/USA | Kette + Ankerwinsch-Systeme | Hoch |
| SAMA (Kettenwerk) | Deutschland | DIN 766, Industriekette | Mittel |
| Fenderteam/Osculati | Italien | Handelsmarke, OEM-Kette | Niedrig–Mittel |
| Muir | Australien | Kette + Ankerwinsch-Systeme | Hoch |
| RWM (Rundstahlkettenwerk Maintal) | Deutschland | DIN 766, kalibriert | Mittel |

### 5.2 Titan Marine

#### 5.2.1 Unternehmensprofil

Titan Marine (auch Titan Chain) ist einer der weltweit größten Hersteller von kalibrierten Ankerketten für den Yachtmarkt. Die Produktion erfolgt in Taiwan unter strengen Qualitätskontrollen. Titan Marine beliefert zahlreiche OEM-Kunden (Ankerwinsch-Hersteller, Yachtwerften) und ist besonders in Nordamerika und Australien marktführend.

**Zertifizierungen:** ISO 9001, ABS Type Approved, Lloyd's Register, NACM-Standard

#### 5.2.2 Produktprogramm — Kalibrierte Ankerkette

**Titan G43 High Test — Feuerverzinkt:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 (DIN) | 602 | 16,5 | 0,79 | 3,50–4,50 |
| 8 | 24,0 (DIN) | 1071 | 29,4 | 1,40 | 5,00–6,50 |
| 10 | 28,0 (DIN) | 1672 | 45,9 | 2,20 | 7,50–9,50 |
| 12 | 36,0 (DIN) | 2406 | 66,1 | 3,10 | 11,00–14,00 |
| 13 | 36,0 (DIN) | 2835 | 77,8 | 3,68 | 13,00–16,00 |
| 14 | 42,0 (DIN) | 3300 | 90,7 | 4,30 | 16,00–20,00 |

**Titan BBB (G40) — Feuerverzinkt (US-Teilung):**

| Nennmaß (Zoll) | Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|---|
| 1/4" | 6,35 | 17,5 | 590 | 14,7 | 0,84 | 4,00–5,00 |
| 5/16" | 7,94 | 21,0 | 907 | 22,7 | 1,28 | 5,50–7,00 |
| 3/8" | 9,53 | 25,0 | 1315 | 32,9 | 1,82 | 7,00–9,00 |
| 7/16" | 11,11 | 28,5 | 1770 | 44,3 | 2,45 | 10,00–12,50 |
| 1/2" | 12,70 | 32,5 | 2359 | 59,0 | 3,25 | 13,00–16,00 |

> **AYDI-Praxishinweis:** Titan Marine liefert sowohl DIN-766-Teilung (europäisch) als auch US-BBB-Teilung. Beim Kauf IMMER die Teilung spezifizieren — DIN und BBB sind NICHT austauschbar auf derselben Kettennuss. Die Preise verstehen sich als Richtpreise inkl. Feuerverzinkung, ohne Versand.

### 5.3 Acco / Peerless

#### 5.3.1 Unternehmensprofil

Acco Brands / Peerless Chain ist der größte US-amerikanische Kettenhersteller und ein Traditionsunternehmen mit über 100 Jahren Erfahrung. Im Yachtbereich werden Acco/Peerless-Ketten häufig über Chandleries und Ankerwinsch-Hersteller (Lewmar, Maxwell) vertrieben.

**Zertifizierungen:** NACM, ASTM, ISO 9001

#### 5.3.2 Produktprogramm

**Acco G43 High Test — Feuerverzinkt:**

| Nennmaß (Zoll) | Nennmaß (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 1/4" | 6,35 | 720 | 18,0 | 0,84 | 5,00–6,50 |
| 5/16" | 7,94 | 1088 | 27,2 | 1,28 | 7,00–9,00 |
| 3/8" | 9,53 | 1588 | 39,7 | 1,82 | 9,50–12,00 |
| 7/16" | 11,11 | 2132 | 53,3 | 2,45 | 12,00–15,00 |
| 1/2" | 12,70 | 2858 | 71,5 | 3,25 | 15,00–19,00 |

**Acco Proof Coil (G30) — Feuerverzinkt:**

| Nennmaß (Zoll) | Nennmaß (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 1/4" | 6,35 | 408 | 10,2 | 0,84 | 3,50–4,50 |
| 5/16" | 7,94 | 635 | 15,9 | 1,28 | 5,00–6,50 |
| 3/8" | 9,53 | 862 | 21,6 | 1,82 | 6,50–8,50 |
| 1/2" | 12,70 | 1315 | 32,9 | 3,25 | 10,00–13,00 |

> **AYDI-Hinweis:** Acco/Peerless-Ketten sind primär in US-Zoll-Maßen und mit US-BBB-Teilung verfügbar. Für europäische Kettennüsse (DIN 766) sind sie in der Regel NICHT direkt geeignet. Ausnahme: einige Acco-Ketten werden auch in metrischen Maßen mit ISO-Teilung angeboten (auf Anfrage).

### 5.4 Lofrans

#### 5.4.1 Unternehmensprofil

Lofrans ist ein italienischer Hersteller von Ankerwinsch-Systemen und passendem Zubehör, einschließlich kalibrierter Ankerketten. Gegründet 1966, ist Lofrans besonders im europäischen Markt stark vertreten und rüstet zahlreiche Werften als OEM-Lieferant aus (Bavaria, Beneteau, Jeanneau).

#### 5.4.2 Produktprogramm — Kalibrierte Kette DIN 766

**Lofrans Kalibrierte Kette G40 — Feuerverzinkt:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 510 | 14,0 | 0,79 | 4,50–6,00 |
| 8 | 24,0 | 907 | 24,9 | 1,40 | 6,50–8,50 |
| 10 | 28,0 | 1418 | 38,9 | 2,20 | 9,50–12,50 |
| 12 | 36,0 | 2039 | 56,0 | 3,10 | 14,00–18,00 |
| 14 | 42,0 | 2770 | 76,1 | 4,30 | 20,00–25,00 |

**Lofrans Kalibrierte Kette — AISI 316L Edelstahl:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 340 | 9,4 | 0,79 | 14,00–18,00 |
| 8 | 24,0 | 590 | 16,3 | 1,40 | 22,00–28,00 |
| 10 | 28,0 | 930 | 25,6 | 2,20 | 36,00–45,00 |
| 12 | 36,0 | 1340 | 36,9 | 3,10 | 52,00–65,00 |

> **AYDI-Praxishinweis:** Lofrans empfiehlt ausdrücklich, nur Lofrans-kalibrierte Kette mit Lofrans-Kettennüssen zu verwenden. In der Praxis funktioniert jede DIN-766-konforme kalibrierte Kette auf Lofrans-Kettennüssen — die Empfehlung ist primär kommerziell motiviert. Dennoch: bei Gewährleistungsansprüchen ist die Verwendung von Lofrans-Originalkette vorteilhaft.

### 5.5 Quick (Quick Nautical Equipment)

#### 5.5.1 Unternehmensprofil

Quick S.p.A. ist ein italienischer Hersteller von nautischer Ausrüstung mit Schwerpunkt Ankerwinsch-Systeme, Bugstrahlruder und Warmwasserbereiter. Quick produziert ebenfalls kalibrierte Ankerketten, die speziell auf die eigenen Kettennüsse abgestimmt sind.

#### 5.5.2 Produktprogramm

**Quick Kalibrierte Kette DIN 766 — Feuerverzinkt:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 510 | 14,0 | 0,79 | 5,00–6,50 |
| 8 | 24,0 | 907 | 24,9 | 1,40 | 7,00–9,00 |
| 10 | 28,0 | 1418 | 38,9 | 2,20 | 10,00–13,00 |
| 12 | 36,0 | 2039 | 56,0 | 3,10 | 15,00–19,00 |
| 14 | 42,0 | 2770 | 76,1 | 4,30 | 22,00–27,00 |
| 16 | 45,0 | 3630 | 99,7 | 5,60 | 30,00–38,00 |

**Quick Kalibrierte Kette — AISI 316 Edelstahl:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 350 | 9,6 | 0,79 | 15,00–19,00 |
| 8 | 24,0 | 600 | 16,5 | 1,40 | 24,00–30,00 |
| 10 | 28,0 | 950 | 26,1 | 2,20 | 38,00–48,00 |
| 12 | 36,0 | 1360 | 37,4 | 3,10 | 55,00–70,00 |

### 5.6 Maxwell

#### 5.6.1 Unternehmensprofil

Maxwell Marine (ehemals Maxwell Winches) ist ein neuseeländischer Hersteller von Ankerwinsch-Systemen. Maxwell wurde 1969 gegründet und hat sich besonders im Markt für Segel- und Motoryachten von 8–25 m etabliert. Das Unternehmen bietet kalibrierte Ankerketten als Zubehör für die eigenen Winsch-Systeme an.

#### 5.6.2 Produktprogramm

**Maxwell Kalibrierte Kette DIN 766 / ISO — Feuerverzinkt G40:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 510 | 14,0 | 0,79 | 5,50–7,00 |
| 8 | 24,0 | 907 | 24,9 | 1,40 | 7,50–9,50 |
| 10 | 28,0 | 1418 | 38,9 | 2,20 | 11,00–14,00 |
| 12 | 36,0 | 2039 | 56,0 | 3,10 | 16,00–20,00 |
| 13 | 36,0 | 2397 | 65,8 | 3,68 | 18,00–22,00 |
| 14 | 42,0 | 2770 | 76,1 | 4,30 | 23,00–28,00 |

> **AYDI-Hinweis:** Maxwell bietet als einer der wenigen Hersteller 13 mm kalibrierte Kette an. Dies ist relevant für Lewmar-Winschen, die traditionell auf 13 mm ausgelegt sind (britischer Markt). Die 13 mm Kette hat die GLEICHE Teilung wie 12 mm (36 mm) — unterschiedlich ist nur der Drahtdurchmesser.

### 5.7 Maggi (Maggi Catene)

#### 5.7.1 Unternehmensprofil

Maggi Catene S.r.l. ist ein italienischer Spezialhersteller für Ketten aller Art, einschließlich kalibrierter Marine-Ankerketten. Maggi ist besonders im Mittelmeerraum und bei europäischen Werften als Zulieferer etabliert.

#### 5.7.2 Produktprogramm

**Maggi DIN 766 Kalibriert — Feuerverzinkt:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 500 | 13,8 | 0,79 | 3,80–5,00 |
| 7 | 22,0 | 680 | 18,7 | 1,10 | 5,00–6,50 |
| 8 | 24,0 | 890 | 24,5 | 1,40 | 6,00–7,80 |
| 10 | 28,0 | 1390 | 38,3 | 2,20 | 8,50–11,00 |
| 12 | 36,0 | 2000 | 55,0 | 3,10 | 12,00–15,50 |
| 14 | 42,0 | 2720 | 74,8 | 4,30 | 17,00–22,00 |
| 16 | 45,0 | 3560 | 97,9 | 5,60 | 25,00–32,00 |

**Maggi DIN 766 Kalibriert — AISI 316L Edelstahl:**

| Nennmaß (mm) | Teilung (mm) | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Preis/m (EUR, 2025) |
|---|---|---|---|---|---|
| 6 | 18,5 | 330 | 9,1 | 0,79 | 12,00–15,50 |
| 8 | 24,0 | 580 | 16,0 | 1,40 | 20,00–26,00 |
| 10 | 28,0 | 910 | 25,0 | 2,20 | 32,00–42,00 |
| 12 | 36,0 | 1310 | 36,0 | 3,10 | 48,00–62,00 |
| 14 | 42,0 | 1780 | 49,0 | 4,30 | 68,00–88,00 |

> **AYDI-Praxishinweis:** Maggi ist einer der wenigen Hersteller, die 7 mm kalibrierte Kette anbieten. 7 mm ist ein Zwischenmaß, das vor allem auf älteren Yachten (70er/80er Jahre) vorkommt. Bei Kettenersatz für diese Boote ist Maggi eine zuverlässige Quelle. Alternativ: Umrüstung auf 8 mm mit neuer Kettennuss.

### 5.8 Preisvergleich und Kosten-Nutzen-Analyse

#### 5.8.1 Gesamtpreisvergleich (8 mm, 60 m, feuerverzinkt, G40/G43)

| Hersteller | Grade | Preis/m (EUR) | Gesamtpreis 60 m (EUR) | Zinkschicht (µm) | Zertifikate |
|---|---|---|---|---|---|
| Titan Marine | G43 | 5,00–6,50 | 300–390 | 70–100 | ISO, ABS |
| Acco/Peerless | G43 | 7,00–9,00 | 420–540 | 80–120 | NACM, ASTM |
| Maggi | G40 | 6,00–7,80 | 360–468 | 70–100 | DIN |
| Lofrans | G40 | 6,50–8,50 | 390–510 | 80–110 | ISO, CE |
| Quick | G40 | 7,00–9,00 | 420–540 | 80–110 | ISO, CE |
| Maxwell | G40 | 7,50–9,50 | 450–570 | 80–120 | ISO |
| Import/NoName | G30 | 3,00–4,50 | 180–270 | 30–50 | Oft keine |

> **AYDI-Empfehlung:** Die Preisdifferenz zwischen Markenware und Import-Kette beträgt ca. 150–300 EUR für eine komplette Ankerausrüstung (60 m). Angesichts der sicherheitskritischen Funktion der Ankerkette ist der Aufpreis für geprüfte Markenware mit dokumentierter Zinkschichtdicke und Bruchlast-Zertifikat unbedingt gerechtfertigt. „Billig ankern" ist eine der teuersten Sparmaßnahmen — ein Kettenbruch kann zum Totalverlust der Yacht führen.

---

## 6. Kettenverbinder und Zubehör

### 6.1 Ankerwirbel (Anchor Swivel)

#### 6.1.1 Funktion und Notwendigkeit

Ein Ankerwirbel (Anchor Swivel, auch: Wirbelschäkel) wird zwischen Anker und Kettenvorlauf eingesetzt. Er erlaubt die freie Drehung der Kette relativ zum Anker und verhindert Verdrallung (Torque) in der Kette, die bei wechselndem Strom, Wind oder Tide entsteht.

**Typen:**

| Typ | Beschreibung | WLL-Bereich | Preis (EUR) |
|---|---|---|---|
| Gabel-Gabel (Jaw-Jaw) | Beidseitig Gabelanschluss | 500–5000 kg | 25–120 |
| Gabel-Auge (Jaw-Eye) | Gabel zum Anker, Auge zur Kette | 500–5000 kg | 25–100 |
| Auge-Auge (Eye-Eye) | Beidseitig Augenanschluss | 500–5000 kg | 20–90 |
| Kugellager-Wirbel | Kugelgelagerte Drehung, leichtgängig | 800–8000 kg | 80–350 |
| Bügelwirbel (Shackle Swivel) | Integrierter Schäkel + Wirbel | 500–5000 kg | 30–150 |

**Dimensionierung:**
Die WLL des Ankerwirbels muss mindestens der WLL der Kette entsprechen. Empfohlen: WLL Wirbel ≥ 1,5× WLL Kette.

| Kettengröße (mm) | Empfohlene Wirbel-WLL (kg) | Übliche Wirbel-Nenngröße |
|---|---|---|
| 6 | ≥750 | 6–8 mm |
| 8 | ≥1350 | 8–10 mm |
| 10 | ≥2100 | 10–12 mm |
| 12 | ≥3000 | 12–14 mm |
| 14 | ≥4000 | 14–16 mm |
| 16 | ≥5300 | 16–19 mm |

> **AYDI-Warnung:** Billige Ankerwirbel aus ungekennzeichnetem Material sind ein häufiger Schwachpunkt im Ankergeschirr. Wirbel aus Zamak (Zinkdruckguss) dürfen NIEMALS als Ankerwirbel verwendet werden — Zamak ist spröde und bricht unter dynamischer Last. Nur geschmiedete Edelstahl- (AISI 316) oder verzinkte Stahlwirbel mit dokumentierter WLL verwenden.

#### 6.1.2 Montage und Sicherung

**Montagereihenfolge (von Anker zum Schiff):**
1. Anker-Schäkel (am Ankerschaft)
2. Ankerwirbel (Gabelseite zum Anker)
3. Verbindungsschäkel (Wirbel → Kette) oder direkte Kettenglied-Einhängung
4. Ankerkette
5. Kettenstopper
6. Kettennuss (Winsch)
7. Kettenkasten-Festpunkt

**Sicherung:**
- Alle Schäkelbolzen mit Edelstahl-Draht (Moustache Wire) oder Kabelbinder sichern
- Gewindeschäkel mit Schraubensicherungslack (Loctite 243) sichern
- Wirbel-Drehung alle 6 Monate prüfen — festsitzende Wirbel sofort tauschen

### 6.2 Kettenschäkel und Verbindungsglieder

#### 6.2.1 Standardschäkel (D-Shackle / Bow Shackle)

| Typ | Beschreibung | Einsatz |
|---|---|---|
| D-Schäkel (Gerade) | Gerader Bügel, schmale Öffnung | Anker ↔ Wirbel, feste Verbindungen |
| Bügelschäkel (Bow) | Omega-Form, weite Öffnung | Kette ↔ Wirbel, flexible Verbindungen |
| Schnellverschluss-Schäkel | Schraubbolzen, werkzeuglos | Temporäre Verbindungen, Beiboot |
| Hammerschäkel | Keilbolzen, schnell lösbar | Rettungsanwendungen |

**Dimensionierung:**

| Kettengröße (mm) | Schäkelgröße (mm) | WLL Schäkel (kg) | Material |
|---|---|---|---|
| 6 | 8 | 500–750 | Verzinkt oder AISI 316 |
| 8 | 10 | 750–1200 | Verzinkt oder AISI 316 |
| 10 | 12 | 1200–2000 | Verzinkt oder AISI 316 |
| 12 | 14–16 | 2000–3500 | Verzinkt oder AISI 316 |
| 14 | 16–19 | 3500–5000 | Verzinkt oder AISI 316 |
| 16 | 19–22 | 5000–8000 | Verzinkt oder AISI 316 |

#### 6.2.2 Kettennotglieder (Chain Connecting Links)

Kettennotglieder (auch: Kettenschnellverschluss, Chain Quick Link, Missing Link) ermöglichen das Verbinden oder Reparieren einer gebrochenen Kette ohne Spezialwerkzeug.

**Typen:**

| Typ | Beschreibung | Festigkeit (% der Kettenbruchlast) |
|---|---|---|
| Schraubglied (Quick Link) | Maulöffnung mit Gewindehülse | 60–80% |
| Kenter-Schäkel (Kenter Joining Shackle) | Zweiteiliges Verbindungsglied | 80–95% |
| Endglied (End Link) | Vergrößertes Endglied für Schäkelanschluss | 90–100% |
| C-Verbinder (C-Link) | C-förmig, mit Bolzen verschraubt | 50–70% |
| Hammerlock | Zweiteilig, formschlüssig | 90–100% |

> **AYDI-Warnung:** Schraubglieder (Quick Links) aus dem Baumarkt sind als Kettenverbinder im Ankergeschirr NICHT zulässig. Sie erreichen nur 50–70% der Kettenbruchlast und können unter dynamischer Last versagen. Nur marinezertifizierte Verbindungsglieder mit dokumentierter WLL verwenden.

### 6.3 Kettenstopper (Chain Stopper)

#### 6.3.1 Funktion

Der Kettenstopper hält die Kette nach dem Auslegen fest und entlastet die Ankerwinsch. Die gesamte Ankerlast wird vom Kettenstopper aufgenommen — er ist das am höchsten belastete Bauteil im Ankergeschirr.

**Typen:**

| Typ | Beschreibung | WLL-Bereich | Eignung |
|---|---|---|---|
| Fallstopper (Devil's Claw) | Hakenförmiger Greifer | 500–3000 kg | Kleinboote, temporär |
| Klemmplatten-Stopper | Klemmplatte über dem Kettenglied | 1000–5000 kg | Standard, Fahrtenyachten |
| Wippen-Stopper (Rocker Stopper) | Kipphebelklemme | 1500–8000 kg | Großyachten, Blauwasser |
| Schraubstopper | Druckschraube auf Kettenglied | 2000–10000 kg | Superyachten, permanent |
| Integrierter Bugrolle-Stopper | Kombination Bugrolle + Stopper | 1000–5000 kg | Serienboote, OEM |

**Dimensionierung und Montage:**

| Kettengröße (mm) | Min. Stopper-WLL (kg) | Bolzengröße Befestigung (mm) | Backing Plate (mm) |
|---|---|---|---|
| 6 | 750 | M8 | 6 mm Edelstahl |
| 8 | 1350 | M10 | 8 mm Edelstahl |
| 10 | 2100 | M12 | 10 mm Edelstahl |
| 12 | 3000 | M12–M14 | 12 mm Edelstahl |
| 14 | 4000 | M14–M16 | 14 mm Edelstahl |
| 16 | 5300 | M16–M20 | 16 mm Edelstahl |

### 6.4 Kettenmarkierung

#### 6.4.1 Methoden

Die Markierung der Kettenlänge ermöglicht dem Skipper, die ausgelegte Kettenmenge zu kontrollieren — essenziell für korrekten Scope.

| Methode | Beschreibung | Haltbarkeit | Kosten |
|---|---|---|---|
| Farbkodierung (Spray) | Alle 10 m andere Farbe aufsprühen | 1–2 Saisons | Gering |
| Kabelbinder | Farbige Kabelbinder alle 5–10 m | 1–3 Saisons | Gering |
| Kettennummerierung (Schlagzahlen) | Zahlen in Glieder schlagen | Permanent | Mittel |
| Farbkodierung (Lack) | Kettenglieder mit 2K-Lack streichen | 3–5 Saisons | Mittel |
| Elektronischer Kettenzähler | Sensor an der Winsch, Display im Cockpit | Permanent | Hoch (200–500 EUR) |

**Standard-Farbkodierung (verbreitet):**

| Markierung | Farbe |
|---|---|
| 10 m | Rot |
| 20 m | Gelb |
| 30 m | Blau |
| 40 m | Grün |
| 50 m | Weiß |
| 60 m | Rot (Wiederholung) |
| 70 m | Gelb (Wiederholung) |
| 80 m | Blau (Wiederholung) |
| Letzte 5 m | Orange (Warnung: Ende der Kette!) |

> **AYDI-Praxishinweis:** Die letzten 5 m der Kette sollten IMMER deutlich markiert werden (Farbe + Kabelbinder + ggf. akustischer Alarm am Kettenzähler). Das Ausrauschen der gesamten Kette durch die Kettennuss ist ein häufiger und gefährlicher Vorfall. Zusätzlich sollte das Kettenende über eine Sollbruchstelle (Nylon-Leine, max. 500 kg Bruchlast) am Rumpf befestigt sein — so kann die Kette im Notfall losgelassen werden, ohne den Kettenkasten zu beschädigen.

### 6.5 Ruckdämpfer (Snubber / Bridle)

#### 6.5.1 Funktion und Notwendigkeit

Ein Ruckdämpfer (Snubber bei Einzelleine, Bridle bei Doppelleine) ist ein elastisches Nylontau, das an der Kette befestigt wird und die dynamischen Lasten (Rucklasten durch Wellen, Gieren, Böen) absorbiert. Ohne Snubber werden diese Lasten direkt auf die Kettennuss, den Kettenstopper und die Bugstruktur übertragen.

**Dimensionierung:**

| Bootslänge (m) | Snubber-Durchmesser (mm) | Snubber-Länge (m) | Material |
|---|---|---|---|
| 6–8 | 10–12 | 4–6 | 3-Schlag Nylon |
| 8–10 | 12–14 | 6–8 | 3-Schlag Nylon |
| 10–12 | 14–16 | 8–10 | 3-Schlag Nylon |
| 12–14 | 16–18 | 8–12 | 3-Schlag Nylon |
| 14–16 | 18–20 | 10–14 | 3-Schlag Nylon |
| 16–20 | 20–24 | 12–16 | 3-Schlag Nylon |

**Befestigung an der Kette:**
- **Kettenhaken (Chain Hook):** Edelstahlhaken, der in ein Kettenglied eingehängt wird. Einfach, schnell. Risiko: Aushaken bei Slackwater.
- **Rolling Hitch (Stopperstek):** Seemännischer Knoten, der sich unter Zug selbst festzieht. Sicher, aber mühsam bei nasser Kette.
- **Softschäkel:** Dyneema-Schlaufe durch ein Kettenglied. Leicht, kein Korrosionsrisiko. Muss korrekt dimensioniert sein.

---

## 7. Fehlerbild-Atlas

### 7.1 Übersicht der häufigsten Fehlerbilder

| Nr. | Fehlerbild | Schweregrad | Häufigkeit | Erkennbarkeit |
|---|---|---|---|---|
| F01 | Gliedverschleiß (Abrieb) | MITTEL–HOCH | Sehr häufig | Visuell + Messung |
| F02 | Zinkverlust (Galvanisierung) | MITTEL | Häufig | Visuell |
| F03 | Kettendehnung (Längung) | HOCH | Mittel | Messung |
| F04 | Kinking (Knickbildung) | HOCH | Mittel | Visuell |
| F05 | Korrosion (Rost) | MITTEL–HOCH | Häufig | Visuell |
| F06 | Schweißnaht-Bruch | KRITISCH | Selten | Visuell + Belastungstest |
| F07 | Spaltkorrosion (Edelstahl) | KRITISCH | Selten | Kaum visuell erkennbar |
| F08 | Verdrallung (Torque) | MITTEL | Häufig | Visuell |
| F09 | Glied-Verformung | HOCH | Mittel | Visuell + Messung |
| F10 | Beschichtungsabplatzung | NIEDRIG–MITTEL | Häufig | Visuell |
| F11 | Fremdmetall-Kontamination | MITTEL | Selten | Visuell (Verfärbung) |
| F12 | Ermüdungsriss | KRITISCH | Sehr selten | Nur mit Prüfmittel |

### 7.2 Detaillierte Fehlerbilder

#### F01 — Gliedverschleiß (Abrieb)

**Beschreibung:**
Abrieb der Gliedoberfläche durch Reibung am Meeresgrund (Sand, Fels, Korallen), an der Bugrolle und in der Kettennuss. Der Verschleiß zeigt sich als Materialabtrag an den Kontaktstellen — typischerweise an der Gliedaußenseite (Grundkontakt) und an der Glied-Innenseite (Glied-zu-Glied-Reibung).

**Erkennungsmerkmale:**
- Abflachung der Gliedquerschnitte (rund → oval)
- Glänzende, blanke Metallflächen an Kontaktpunkten
- Reduzierter Drahtdurchmesser (messbar mit Messschieber)
- Erhöhte Beweglichkeit zwischen den Gliedern

**Beurteilungskriterien:**

| Verschleiß (% Durchmesserreduktion) | Bewertung | Maßnahme |
|---|---|---|
| <5% | Normal | Weiterverwendung, nächste Saison prüfen |
| 5–10% | Erhöht | Verstärkte Inspektion, ggf. Kette drehen |
| 10–15% | Kritisch | Kettenaustausch planen, nicht bei Starkwind ankern |
| >15% | Unzulässig | Sofortiger Austausch |

**AYDI-Confidence:** `visual_medium` (Verschleiß sichtbar, aber Messung für genaue Beurteilung erforderlich)

#### F02 — Zinkverlust (Galvanisierung)

**Beschreibung:**
Der feuerverzinkte Überzug wird durch Abrieb, Salzwasserkorrosion und galvanische Prozesse abgetragen. Der Zinkverlust beginnt typischerweise an den Kontaktstellen (Glied-zu-Glied, Bugrolle, Meeresgrund) und breitet sich dann auf die gesamte Oberfläche aus.

**Erkennungsmerkmale:**
- Farbverlauf: silbrig-glänzend → matt-grau → bräunlich → rostig
- Weiße Ausblühungen (Zinkcarbonat — „Weißrost")
- Braune Flecken auf ansonsten intakter Verzinkung (Zink-Durchbruch)
- Flächiger Rost an exponierten Stellen

**Beurteilungskriterien:**

| Zustand | Zinkverlust (%) | Bewertung | Maßnahme |
|---|---|---|---|
| Silbrig-glänzend | 0–20% | Gut | Keine |
| Matt-grau, vereinzelt Weißrost | 20–50% | Akzeptabel | Süßwasserspülung, Kontrolle |
| Bräunliche Stellen, punktuell Rost | 50–75% | Nachlassend | Neuverzinkung erwägen |
| Flächiger Rost, Zink kaum erkennbar | 75–95% | Schlecht | Neuverzinkung oder Austausch |
| Vollständig rostig, Materialverlust | 95–100% | Unzulässig | Sofortiger Austausch |

**AYDI-Confidence:** `visual_high` (Zinkverlust ist visuell gut beurteilbar)

> **AYDI-Praxishinweis:** Regelmäßiges Spülen der Kette mit Süßwasser nach dem Einholen verlängert die Lebensdauer der Verzinkung erheblich. In Tropenrevieren (hohe Wassertemperatur, hoher Salzgehalt) ist der Zinkverlust 2–3× schneller als in gemäßigten Gewässern. Viele Blauwasseryachten lassen ihre Kette alle 5–7 Jahre neu feuerverzinken.

#### F03 — Kettendehnung (Längung)

**Beschreibung:**
Überlastung der Kette führt zu plastischer Verformung der Glieder — die Kette wird permanent länger. Dies verändert die Teilung und macht die Kette inkompatibel mit der Kettennuss.

**Erkennungsmerkmale:**
- Vergrößerte Teilung (messbar: >3% über Nennmaß = unzulässig)
- Glieder erscheinen „gestreckt" (ovaler statt runder Querschnitt)
- Kette „springt" auf der Kettennuss (passt nicht mehr in die Taschen)
- Ungleichmäßige Teilung über die Kettenlänge

**Messmethode:**
10 Glieder abmessen und mit dem Sollwert (10 × Teilung) vergleichen:

| Nennmaß (mm) | Sollwert 10 Glieder (mm) | Toleranz (mm) | Max. zulässig (mm) |
|---|---|---|---|
| 6 | 185 | ±5 | 191 |
| 8 | 240 | ±5 | 247 |
| 10 | 280 | ±5 | 288 |
| 12 | 360 | ±7 | 371 |

**AYDI-Confidence:** `measured` (quantitative Messung möglich)

#### F04 — Kinking (Knickbildung)

**Beschreibung:**
Kinking entsteht, wenn die Kette unter Last über eine scharfe Kante gezogen wird oder wenn ein verdrallter Kettenstrang ruckartig belastet wird. Das betroffene Glied wird plastisch verformt und kann nicht mehr frei in der Kette artikulieren.

**Erkennungsmerkmale:**
- Einzelne Glieder stehen schräg oder quer zur Kettenachse
- Kette lässt sich an der betroffenen Stelle nicht gerade strecken
- Sichtbare plastische Verformung des Glieds
- Kette bleibt in der Kettennuss hängen

**Bewertung:**
- Leichter Kink (<10° Abweichung): Beobachten, Kette weiterverwendbar
- Mittlerer Kink (10–30° Abweichung): Glied austauschen (Verbindungsglied)
- Schwerer Kink (>30° Abweichung): Kettenabschnitt austauschen oder gesamte Kette ersetzen

**AYDI-Confidence:** `visual_high` (eindeutig visuell erkennbar)

#### F05 — Korrosion (Rost)

**Beschreibung:**
Flächige Korrosion des Grundmaterials nach Verlust der Verzinkung. Der Materialabtrag schwächt die Kette und reduziert die Bruchlast.

**AYDI-Confidence:** `visual_medium` (Ausmaß der Querschnittsschwächung visuell schwer beurteilbar)

#### F06 — Schweißnaht-Bruch

**Beschreibung:**
Jedes Kettenglied hat eine Schweißstelle (Stumpfschweißung). Bei minderwertiger Fertigung, Überlastung oder Korrosion kann die Schweißnaht brechen — das Glied öffnet sich und die Kette versagt.

**Erkennungsmerkmale:**
- Sichtbare Rissbildung an der Schweißstelle (oft gegenüber der Gliedkrümmung)
- Rostbildung gezielt an der Schweißnaht (Schwachstelle in der Verzinkung)
- Bei fortgeschrittenem Schaden: Glied klafft auseinander

**AYDI-Confidence:** `visual_medium` (frühe Risse nur bei genauer Inspektion erkennbar)

> **AYDI-Warnung:** Schweißnaht-Brüche sind der häufigste Versagensmechanismus bei Billig-Importketten. Die Schweißqualität ist das wichtigste Qualitätskriterium — und visuell am fertigen Produkt kaum zu prüfen. Zertifizierte Markenkette von etablierten Herstellern ist die beste Absicherung.

#### F07 — Spaltkorrosion (Edelstahl)

**Beschreibung:**
Spaltkorrosion tritt bei Edelstahlketten in Spalten und engen Bereichen auf, wo Sauerstoff nicht frei zirkulieren kann (Glied-zu-Glied-Kontaktflächen, Kettenkasten). In sauerstoffarmer Umgebung bricht die Passivierungsschicht des Edelstahls zusammen.

**Erkennungsmerkmale:**
- Bräunliche Verfärbung an Kontaktflächen zwischen Gliedern
- Lochfraß (Pitting) an Gliedinnenseiten
- Matte, raue Oberfläche statt glänzend
- Geruch nach Eisensulfid (fauliger Geruch) im Kettenkasten

**AYDI-Confidence:** `visual_low` (Spaltkorrosion ist ohne Demontage und Reinigung kaum erkennbar)

#### F08 — Verdrallung (Torque)

**Beschreibung:**
Die Kette verdreht sich um ihre Längsachse, wenn sie sich beim Einholen nicht frei ausrichten kann. Verdrallung erhöht die Biegebelastung der Glieder und kann zum Verklemmen auf der Kettennuss führen.

**AYDI-Confidence:** `visual_high`

#### F09 — Glied-Verformung

**Beschreibung:**
Plastische Verformung einzelner Glieder durch Überlastung, Einklemmen oder mechanische Beschädigung. Die Glieder werden oval oder asymmetrisch.

**Erkennungsmerkmale:**
- Glieder sind nicht mehr symmetrisch (oval, trapezförmig)
- Kette passt nicht mehr korrekt in die Kettennuss
- Erhöhte Steifigkeit an der verformten Stelle
- Messbar: Innenweite oder Außenweite außerhalb Toleranz

**AYDI-Confidence:** `visual_medium` bis `measured` (je nach Verformungsgrad)

#### F10 — Beschichtungsabplatzung

**Beschreibung:**
Bei minderwertiger Feuerverzinkung oder elektrischer Verzinkung kann die Zinkschicht in Platten abplatzen (Delamination). Dies unterscheidet sich vom graduellen Zinkverlust (F02) durch das plötzliche, großflächige Ablösen.

**AYDI-Confidence:** `visual_high`

#### F11 — Fremdmetall-Kontamination

**Beschreibung:**
Kontakt mit Kupfer, Kupferlegierungen (Bronze, Messing) oder Aluminium kann bei verzinkter Kette beschleunigten galvanischen Angriff verursachen. Häufig durch falsche Schäkel (Bronze statt Edelstahl/verzinkt) oder Kontakt mit kupferhaltigen Antifouling-Rückständen.

**AYDI-Confidence:** `visual_medium` (Verfärbung sichtbar, Ursache erfordert Analyse)

#### F12 — Ermüdungsriss

**Beschreibung:**
Ermüdungsrisse entstehen durch zyklische Belastung (Wellengang, Gieren) über lange Zeiträume. Sie beginnen als mikroskopische Risse an Spannungskonzentrationspunkten (Schweißnaht, Gliedkrümmung) und wachsen langsam, bis das Glied plötzlich bricht.

**Erkennungsmerkmale:**
- Äußerlich kaum erkennbar (erfordert Magnetpulver- oder Farbeindringprüfung)
- Gelegentlich: feine Haarrisse an der Schweißnaht
- Bruchfläche zeigt muschelförmiges Muster (Schwingbruch) — nach dem Bruch erkennbar

**AYDI-Confidence:** `visual_insufficient` (nur mit zerstörungsfreier Prüfung erkennbar)

> **AYDI-Empfehlung:** Ketten, die älter als 10 Jahre sind oder mehr als 500 Ankermanöver absolviert haben, sollten einer professionellen Prüfung unterzogen werden. Magnetpulverprüfung (MT) und Farbeindringprüfung (PT) sind die gängigen zerstörungsfreien Methoden für Kettenglieder.

---

## 8. Troubleshooting-Entscheidungsbaum

### 8.1 Kette springt auf der Kettennuss

```
Kette springt auf der Kettennuss
├── Ist die Kette DIN 766 / ISO 4565 kalibriert?
│   ├── NEIN → Unkalibrierte Kette (DIN 5685 o.ä.)
│   │   └── LÖSUNG: Austausch gegen kalibrierte Kette
│   └── JA → Weiter prüfen
│       ├── Stimmt das Nennmaß der Kette mit der Kettennuss überein?
│       │   ├── NEIN → Falsche Kettennuss oder falsche Kette
│       │   │   └── LÖSUNG: Kettennuss oder Kette tauschen
│       │   └── JA → Weiter prüfen
│       │       ├── Ist die Kette gedehnt? (10 Glieder messen)
│       │       │   ├── JA (>3% Überlänge) → Plastische Dehnung
│       │       │   │   └── LÖSUNG: Kette austauschen
│       │       │   └── NEIN → Weiter prüfen
│       │       │       ├── Ist die Kettennuss verschlissen?
│       │       │       │   ├── JA → Kettennuss-Verschleiß
│       │       │       │   │   └── LÖSUNG: Kettennuss tauschen
│       │       │       │   └── NEIN → Kettenführung prüfen
│       │       │       │       └── Kette läuft schräg auf die Nuss
│       │       │       │           └── LÖSUNG: Kettenführung/Bugrolle justieren
```

### 8.2 Kette rostet trotz Verzinkung

```
Kette rostet trotz Verzinkung
├── Alter der Kette?
│   ├── >10 Jahre → Normaler Zinkverlust durch Alterung
│   │   └── LÖSUNG: Neuverzinkung oder Austausch
│   └── <5 Jahre → Ungewöhnlich, weiter prüfen
│       ├── Einsatzrevier?
│       │   ├── Tropen (>28°C Wassertemperatur) → Beschleunigter Zinkverlust
│       │   │   └── LÖSUNG: Häufigere Inspektion, Neuverzinkung erwägen
│       │   └── Gemäßigt → Weiter prüfen
│       │       ├── Wird die Kette nach dem Einholen mit Süßwasser gespült?
│       │       │   ├── NEIN → Salzkristalle greifen Zink an
│       │       │   │   └── LÖSUNG: Spülsystem installieren, regelmäßig spülen
│       │       │   └── JA → Weiter prüfen
│       │       │       ├── Kontakt mit Kupfer/Bronze/Messing?
│       │       │       │   ├── JA → Galvanische Korrosion
│       │       │       │   │   └── LÖSUNG: Fremdmetall entfernen, isolieren
│       │       │       │   └── NEIN → Qualitätsproblem
│       │       │       │       └── LÖSUNG: Zinkschichtdicke messen, Hersteller kontaktieren
```

### 8.3 Kette lässt sich nicht einholen

```
Kette lässt sich nicht einholen
├── Winsch dreht nicht
│   ├── Elektrische Winsch → Sicherung, Schalter, Motor prüfen
│   └── Hydraulische Winsch → Ölstand, Pumpe, Ventile prüfen
├── Winsch dreht, aber Kette kommt nicht
│   ├── Kette verklemmt in Kettennuss → Verdrallte/geknickte Kette
│   │   └── LÖSUNG: Kette manuell lösen, Kink/Verdrallung beseitigen
│   ├── Kette hängt am Grund → Anker oder Kette verklaust
│   │   └── LÖSUNG: Motor voraus fahren, Ankertrick versuchen
│   └── Überlast → Kette zu schwer (Tiefe) oder Anker sitzt fest
│       └── LÖSUNG: Winsch nicht überlasten, manuell oder unter Motor lösen
├── Kette kommt, aber verklemmt in Bugrolle
│   └── Verbindungsglied/Schäkel zu groß für Bugrolle
│       └── LÖSUNG: Bugrolle vergrößern oder flacheren Schäkel verwenden
```

### 8.4 Kette macht Lärm im Kettenkasten

```
Kette rasselt im Kettenkasten
├── Nur bei Seegang?
│   ├── JA → Kette bewegt sich im Kasten (normal bei wenig Kette)
│   │   └── LÖSUNG: Kettenkasten-Dämpfung (Gummimatte), Kette straffen
│   └── NEIN, auch im Hafen → Weiter prüfen
│       ├── Kettenkasten-Abfluss verstopft?
│       │   ├── JA → Wasser im Kasten, Kette schwimmt/schlägt
│       │   │   └── LÖSUNG: Abfluss reinigen
│       │   └── NEIN → Kasten zu groß für Kettenmenge
│       │       └── LÖSUNG: Trennwand oder Dämpfungsmatte einbauen
```

### 8.5 Anker hält nicht (kettenbezogene Ursachen)

```
Anker hält nicht — kettenbezogene Ursachen
├── Ausreichend Kette ausgelegt? (Scope ≥ 5:1?)
│   ├── NEIN → Zu wenig Scope
│   │   └── LÖSUNG: Mehr Kette auslegen
│   └── JA → Weiter prüfen
│       ├── Liegt die Kette flach auf dem Grund? (Kettenary?)
│       │   ├── NEIN (Kette steigt steil vom Grund ab)
│       │   │   └── LÖSUNG: Mehr Kette oder Kettengewicht (Kellet) verwenden
│       │   └── JA → Kette ist nicht das Problem
│       │       └── → Ankertyp, Ankergrund prüfen (→ 13.01)
├── Kette rutscht durch Kettenstopper?
│   ├── JA → Kettenstopper defekt oder falsche Größe
│   │   └── LÖSUNG: Kettenstopper reparieren/tauschen
│   └── NEIN → Kette reißt nicht, hält nicht → Ankerproblem (→ 13.01)
```

---

## 9. FAQ — Häufige Fragen

### FAQ 01: Welche Kettengröße brauche ich für mein Boot?

**Frage:** Ich habe eine 12 m Segelyacht und möchte die Ankerkette erneuern. Welches Nennmaß ist richtig?

**Antwort:** Für eine 12 m Fahrtensegelyacht ist 8 mm G43 (High Test, kalibriert nach DIN 766) die Standardempfehlung. Diese Kette bietet eine WLL von ca. 1070 kg und eine Bruchlast von ca. 29 kN — ausreichend für Windstärken bis 40+ Knoten. Bei intensiver Blauwasserfahrt oder schwerem Displacement kann eine 10 mm G43 sinnvoll sein, bringt aber ca. 57% mehr Gewicht im Bug. **Confidence:** estimated

### FAQ 02: G30, G40 oder G43 — welche Güteklasse ist die richtige?

**Frage:** Was ist der praktische Unterschied zwischen den Güteklassen?

**Antwort:** G30 (Proof Coil) ist die Basis-Güteklasse — günstig, aber auch die geringste Bruchlast. G40 (BBB/High Test Standard) ist der nordamerikanische Standard. G43 (High Test) bietet ca. 57% mehr Bruchlast als G30 bei identischem Gewicht und Durchmesser und ist der beste Kompromiss für Fahrtenyachten. G70 bietet die höchste Festigkeit, ist aber doppelt so teuer und hat ein spröderes Bruchverhalten. Empfehlung: G43 für Fahrt und Blauwasser, G40 für Küstenfahrt, G30 nur für Kleinboote und Beiboote. **Confidence:** documented

### FAQ 03: Wie lang sollte meine Ankerkette sein?

**Frage:** Reichen 40 m Kette für eine 11 m Yacht?

**Antwort:** 40 m sind ein absolutes Minimum für Küstenfahrt. Bei 10 m Wassertiefe ergibt das nur einen Scope von 4:1 — gerade noch akzeptabel bei ruhigem Wetter. Für Mittelmeerfahrt empfehlen wir 60–80 m, für Blauwasser 80–100 m. Faustformel: 5× maximale Ankerwassertiefe + 20 m Reserve. **Confidence:** estimated

### FAQ 04: Verzinkt oder Edelstahl?

**Frage:** Lohnt sich Edelstahlkette für meine Yacht?

**Antwort:** Edelstahlkette ist 3–5× teurer als verzinkte und hat geringere Bruchlasten bei gleichem Durchmesser. Vorteile: kein Zinkverlust, ästhetisch, lange Lebensdauer. Nachteile: Spaltkorrosion im Kettenkasten, galvanische Probleme mit verzinkten Ankern, höhere Kosten. Empfehlung: Für die meisten Fahrtenyachten ist hochwertige feuerverzinkte G43-Kette die bessere Wahl. Edelstahl nur bei besonderen Anforderungen (Superyachten, Charteryachten mit Ästhetik-Anspruch). **Confidence:** documented

### FAQ 05: Was ist der Unterschied zwischen DIN 766 und BBB?

**Frage:** Kann ich BBB-Kette auf meiner europäischen Kettennuss verwenden?

**Antwort:** Nein. DIN 766 und US-BBB haben unterschiedliche Teilungsmaße. DIN 766 8 mm hat 24 mm Teilung, BBB 5/16" (ca. 8 mm) hat 21 mm Teilung. Eine BBB-Kette auf einer DIN-766-Kettennuss springt unter Last. Beim Kauf IMMER spezifizieren: „DIN 766 kalibriert" für europäische Winschen, „BBB" für amerikanische Winschen. **Confidence:** measured

### FAQ 06: Wie erkenne ich, ob meine Kette noch gut ist?

**Frage:** Woran merke ich, dass meine Kette getauscht werden muss?

**Antwort:** Fünf Prüfpunkte: (1) Zinkverlust: >75% rostig → tauschen. (2) Durchmesserverlust: >10% Reduktion (messen!) → tauschen. (3) Längung: >3% Teilungsveränderung (10 Glieder messen) → tauschen. (4) Kinks: verformte Glieder, die sich nicht gerade strecken lassen → Abschnitt tauschen. (5) Schweißnahtrisse: sichtbare Risse an Gliedverbindungen → sofort tauschen. **Confidence:** documented

### FAQ 07: Kann ich meine Kette neu verzinken lassen?

**Frage:** Meine 80 m Kette rostet, aber ist mechanisch noch in Ordnung. Lohnt sich Neuverzinkung?

**Antwort:** Ja, Neuverzinkung (Re-Galvanizing) ist möglich und wirtschaftlich, wenn die Kette mechanisch intakt ist. Kosten: ca. 3–5 EUR/m für Feuerverzinkung (je nach Region und Anbieter). Voraussetzung: Kette muss vorher entrostet (Beize oder Sandstrahlen) und auf Verschleiß geprüft werden. Die Neuverzinkung eines 80 m Kettensatzes kostet ca. 250–400 EUR — deutlich günstiger als eine neue Kette (500–800 EUR). **Confidence:** estimated

### FAQ 08: Brauche ich einen Ankerwirbel?

**Frage:** Muss ein Wirbel zwischen Anker und Kette?

**Antwort:** Nicht zwingend, aber empfohlen. Ohne Wirbel verdrallt sich die Kette bei wechselndem Strom/Wind. Die Verdrallung erhöht die Belastung der Glieder und kann Kinking verursachen. Ein hochwertiger Wirbel (Gabel-Auge, Edelstahl oder verzinkt, WLL ≥ 1,5× Ketten-WLL) kostet 30–100 EUR — eine sinnvolle Investition. Warnung: keine Zamak-Wirbel, keine ungeprüften Billigwirbel. **Confidence:** documented

### FAQ 09: Was ist ein Snubber und brauche ich einen?

**Frage:** Mein Nachbar im Ankerfeld hat eine Leine an seiner Kette. Wozu?

**Antwort:** Das ist ein Snubber (Ruckdämpfer). Eine Nylonleine, die per Kettenhaken oder Knoten an der Kette befestigt wird und die dynamischen Lasten (Böen, Wellen) absorbiert. Ohne Snubber werden Rucklasten direkt auf die starre Kette, den Kettenstopper und den Bug übertragen. Ein Snubber ist bei All-Chain-Rode absolut empfehlenswert — besonders wichtig bei G70-Kette (sprödes Bruchverhalten). Kosten: 30–80 EUR. **Confidence:** documented

### FAQ 10: Wie lagere ich meine Kette über den Winter?

**Frage:** Soll ich die Kette über den Winter an Bord lassen?

**Antwort:** Idealerweise wird die Kette für die Winterlagerung aus dem Kettenkasten genommen, gründlich mit Süßwasser gespült und trocken gelagert. Das verlängert die Lebensdauer der Verzinkung erheblich. Wenn dies nicht möglich ist: Kette vollständig einholen, Kettenkasten gründlich spülen und trocknen lassen, Kettenkasten-Drainage öffnen. Für Edelstahlketten ist die trockene Winterlagerung BESONDERS wichtig (Spaltkorrosion-Prävention). **Confidence:** documented

### FAQ 11: Was kostet eine komplette Ankerausrüstung (Kette)?

**Frage:** Was muss ich für die Kette einer 12 m Yacht budgetieren?

**Antwort:** Für eine 12 m Yacht mit 80 m × 8 mm G43 verzinkter Kette: Kette: 400–680 EUR, Ankerwirbel: 40–100 EUR, Verbindungsschäkel: 15–30 EUR, Kettenmarkierung: 10–20 EUR, Snubber: 40–80 EUR. **Gesamt: ca. 500–900 EUR.** Bei Edelstahl: 1600–2400 EUR nur für die Kette. **Confidence:** estimated

### FAQ 12: Kann ich zwei verschiedene Ketten verbinden?

**Frage:** Ich habe noch 30 m gute Kette und möchte 30 m neue anschließen. Geht das?

**Antwort:** Grundsätzlich ja, wenn beide Ketten das gleiche Nennmaß und die gleiche Teilung (DIN 766) haben. Verbindung mit einem Kenter-Schäkel oder Hammerlock-Verbinder. Wichtig: Die alte Kette kommt an das Schiffsende (weniger belastet), die neue Kette an die Ankerseite (höher belastet). NICHT mischen: unterschiedliche Nennmaße, DIN und BBB, oder verzinkt und Edelstahl. **Confidence:** documented

### FAQ 13: Wie messe ich den Verschleiß meiner Kette?

**Frage:** Wie prüfe ich, ob meine Kette noch innerhalb der Toleranzen ist?

**Antwort:** Drei Messungen: (1) **Drahtdurchmesser:** Mit Messschieber an der dünnsten Stelle messen. Vergleich mit Nennmaß. >10% Reduktion = tauschen. (2) **Teilung:** 10 Glieder messen, durch 10 teilen. Vergleich mit Nennwert. >3% Abweichung = tauschen. (3) **Innenweite:** Messen, ob die Glieder noch auf die Kettennuss passen. Spiel an den Messestellen alle 10 m. Tipp: diese Messungen jährlich dokumentieren und Verschleißtrend beobachten. **Confidence:** measured

### FAQ 14: Meine Kettennuss ist für 10 mm — kann ich 8 mm Kette fahren?

**Frage:** Die Kette ist zu teuer in 10 mm. Kann ich eine Nummer kleiner nehmen?

**Antwort:** NEIN. Eine 8 mm Kette auf einer 10 mm Kettennuss hat zu viel Spiel und springt unter Last aus den Taschen. Die Kettennuss MUSS zum Kettendurchmesser passen. Alternativen: (1) Kettennuss wechseln (bei vielen Winsch-Modellen möglich, 100–300 EUR). (2) G43 statt G30 wählen — gleicher Durchmesser, höhere Bruchlast. (3) Gebrauchte Markenkette kaufen. **Confidence:** measured

### FAQ 15: Wie oft sollte ich die Kette drehen (End-for-End)?

**Frage:** Soll ich die Kette regelmäßig umdrehen?

**Antwort:** Ja, das „End-for-End"-Drehen (das Anker-Ende wird zum Schiffs-Ende und umgekehrt) verteilt den Verschleiß gleichmäßig. Die ersten 20–30 m der Kette (Ankerseite) verschleißen 3–5× schneller als der Rest. Empfehlung: alle 3–5 Jahre drehen. Dabei gleich die gesamte Kette inspizieren und ggf. die Markierungen erneuern. **Confidence:** documented

### FAQ 16: Was ist ein Kellet (Kettengewicht)?

**Frage:** Was bringt ein Gewicht auf der Kette?

**Antwort:** Ein Kellet (auch: Sentinel, Chum) ist ein Gewicht (5–15 kg), das an einer Leine mitten auf der Kette herabgelassen wird. Es drückt die Kette tiefer und verstärkt den Kettenary-Effekt — der Zugwinkel am Anker wird flacher. Nützlich bei wenig Platz zum Schwojen (Hafen, enge Bucht) oder zu kurzem Kettenstück. Alternativen: mehr Kette auslegen. **Confidence:** documented

### FAQ 17: Passen alle DIN-766-Ketten auf alle DIN-766-Kettennüsse?

**Frage:** Ist DIN 766 wirklich standardisiert?

**Antwort:** Im Prinzip ja — alle DIN-766-kalibrierten Ketten haben die gleichen Teilungsmaße und sollten auf allen DIN-766-Kettennüssen laufen. In der Praxis gibt es jedoch geringe Toleranzunterschiede zwischen Herstellern. Empfehlung: (1) Immer 2–3 m Kette zum Testen bestellen, bevor man 80+ m kauft. (2) Kette auf der Kettennuss testen — jedes Glied muss sauber einrasten. (3) Winsch-Hersteller-Empfehlungen beachten. **Confidence:** documented

### FAQ 18: Soll ich die gesamte Kette oder nur den verschlissenen Teil tauschen?

**Frage:** Nur die ersten 20 m meiner 80 m Kette sind verschlissen. Muss ich alles tauschen?

**Antwort:** Nein, ein Teilaustausch ist möglich und wirtschaftlich sinnvoll. Verbindung mit Kenter-Schäkel oder Hammerlock. Wichtig: Die neue Kette kommt an die Ankerseite. Sicherstellen, dass alte und neue Kette identisches Nennmaß und identische Teilung haben. Der Verbindungspunkt muss durch die Bugrolle und über die Kettennuss passen — vorher testen! **Confidence:** documented

### FAQ 19: Was ist ein Kettenkaliber und wie verwende ich es?

**Frage:** Mein Kettenlieferant bietet ein „Kettenkaliber" an. Was ist das?

**Antwort:** Ein Kettenkaliber (Chain Gauge) ist ein einfaches Prüfwerkzeug — ein Stahlblech mit Aussparungen für verschiedene Kettenmaße. Man legt das Kettenglied in die passende Aussparung: passt es exakt, ist die Kette innerhalb der Toleranz. Ist das Glied zu schmal (verschlissen) oder zu lang (gedehnt), fällt es durch bzw. passt nicht. Kosten: 15–30 EUR. Für jeden Yachteigner empfehlenswert. **Confidence:** documented

### FAQ 20: Darf ich eine Ankerkette schweißen?

**Frage:** Ein Glied meiner Kette ist gerissen. Kann ich es schweißen lassen?

**Antwort:** Grundsätzlich: NEIN. Feldschweißungen an Ankerketten sind nicht zulässig, da die Festigkeit nicht gewährleistet werden kann. G43- und G70-Ketten sind wärmebehandelt — eine Schweißung zerstört die Wärmebehandlung und schwächt das Material erheblich. G30-Kette kann theoretisch geschweißt werden, aber die Nahtqualität ist ohne Prüfung nicht sichergestellt. Lösung: gerissenes Glied mit Kenter-Schäkel überbrücken oder Kettenabschnitt austauschen. **Confidence:** documented

### FAQ 21: Wie verhindere ich Ketten-Rasseln in der Nacht?

**Frage:** Die Kette in der Bugrolle rasselt bei jedem Wellenschlag. Was kann ich tun?

**Antwort:** (1) Snubber verwenden — entlastet die Kette und dämpft die Bewegung. (2) Kette über den Snubber etwas fieren, sodass die Kette zwischen Kettenstopper und Wasserlinie schlaff hängt und nur der Snubber Last trägt. (3) Schaumstoff-Polster um die Kette in der Bugrolle wickeln. (4) Anti-Rattle-Vorrichtung (z. B. Kette mit Gummischlauch umhüllen). **Confidence:** documented

### FAQ 22: Meine Kette hat verschiedenfarbige Glieder — ist das ein Qualitätsproblem?

**Frage:** Einige Glieder meiner neuen Kette sind heller als andere. Ist die Verzinkung fehlerhaft?

**Antwort:** Leichte Farbunterschiede in der Feuerverzinkung sind normal und kein Qualitätsmangel. Sie entstehen durch unterschiedliche Abkühlgeschwindigkeiten und leicht variierende Stahlzusammensetzung. Helle (glänzende) und matte (graue) Bereiche haben identische Zinkschichtdicke. Nur wenn einzelne Glieder deutlich dunkler (bräunlich) oder gar rostig sind, liegt ein Beschichtungsfehler vor. **Confidence:** documented

### FAQ 23: Was ist der Unterschied zwischen einer Kettennuss und einem Spillkopf?

**Frage:** Meine Winsch hat eine Kettennuss und einen glatten Zylinder. Was nehme ich für die Kette?

**Antwort:** Die Kettennuss (Wildcat, Gypsy) hat profilierte Taschen, die exakt in die Kettenglied-Geometrie eingreifen — nur hier darf die Kette laufen. Der glatte Zylinder (Spillkopf, Capstan, Warping Drum) ist für Tauwerk (Festmacher, Ankertau). Kette auf dem Spillkopf rutscht durch und kann den Bediener verletzen. Tau auf der Kettennuss kann sich verfangen und die Kettennuss blockieren. **Confidence:** documented

### FAQ 24: Wie transportiere ich Ersatzkette?

**Frage:** Ich möchte 30 m Ersatzkette auf meiner Blauwasserfahrt mitnehmen. Wie lagere ich sie?

**Antwort:** Ersatzkette in einem Segeltuch-Beutel oder einer stabilen Plastikbox lagern. Nicht lose im Schiff — bei Seegang wird eine 42 kg schwere 8 mm × 30 m Kette zum gefährlichen Geschoss. Lagerort: möglichst tief und mittschiffs (Trimmoptimierung). Kette leicht einfetten (Ballistol, WD-40) gegen Rostbildung. Kontakt mit anderen Metallen vermeiden (galvanische Korrosion). **Confidence:** documented

### FAQ 25: Gibt es eine Ankerkette, die auf JEDE Kettennuss passt?

**Frage:** Ich habe eine Lofrans-Winsch, aber möchte keine Lofrans-Kette kaufen. Geht das?

**Antwort:** Ja. Alle DIN-766-kalibrierten Ketten sind normiert und passen auf alle DIN-766-Kettennüsse — unabhängig vom Hersteller. Lofrans, Quick, Maxwell, Lewmar — alle verwenden DIN 766 als Basis. Die Herstellerempfehlung „nur Original-Kette verwenden" ist primär kommerziell motiviert. Einzige Voraussetzung: die Kette MUSS kalibriert sein (DIN 766 oder ISO 4565). Vor dem Kauf 2–3 m testen. Ausnahme: einige ältere Lewmar-Winschen sind auf 13 mm BBB kalibriert — hier ist Vorsicht geboten. **Confidence:** documented

### FAQ 26: Was passiert, wenn die Kette komplett ausrauscht?

**Frage:** Was passiert, wenn die gesamte Kette durch die Kettennuss rauscht und wie verhindere ich das?

**Antwort:** Wenn die Kette komplett ausrauscht (unkontrolliertes Fieren bis zum Ende), kann die kinetische Energie der schweren Kette massive Schäden verursachen: Kettenkasten-Festpunkt reißt aus, Kettennuss wird beschädigt, Kettenrohr verbiegt sich, oder die gesamte Kette geht über Bord. Prävention: (1) Kettenende IMMER über eine Sollbruchstelle (Nylonleine, ca. 500 kg Bruchlast) am Rumpf befestigen — so bricht die Verbindung kontrolliert, bevor der Rumpf beschädigt wird. (2) Kette NIEMALS frei rauschen lassen — immer kontrolliert über die gebremste Kettennuss fieren. (3) Letzte 5 m der Kette deutlich markieren (Farbe + Kabelbinder). (4) Elektronischen Kettenzähler mit Längenalarm verwenden. **Confidence:** documented

### FAQ 27: Wie wasche ich meine Kette am effektivsten?

**Frage:** Reicht es, die Kette beim Einholen mit einem Eimer Wasser abzuspülen?

**Antwort:** Ein Eimer reicht nicht. Die effektivste Methode ist eine fest installierte Spüldüse am Bug, die die Kette beim Einholen kontinuierlich mit Frischwasser (oder zumindest Seewasser) abspritzt. Nachrüstlösung: Gartenschlauch-Anschluss am Deck, Schlauch zur Bugrolle führen, beim Einholen manuell spülen. Die Kette muss über die gesamte Länge abgespült werden, nicht nur die ersten Meter. Schlick und Sand in den Gliedern beschleunigen den Verschleiß erheblich. Ideal: nach dem Spülen den Kettenkasten belüften (Deckel öffnen), damit die Kette trocknet. **Confidence:** documented

### FAQ 28: Meine Kette ist zu kurz. Kann ich sie verlängern?

**Frage:** Ich habe 50 m Kette, brauche aber 80 m. Kann ich 30 m anstückeln?

**Antwort:** Ja, Verlängerung ist möglich und gängige Praxis. Voraussetzung: gleicher Durchmesser, gleiche Norm (DIN 766 oder BBB), idealerweise gleiche Güteklasse. Verbindung mit Kenter-Schäkel oder Hammerlock-Verbinder. Die neue Kette kommt an die Ankerseite (höher belastet), die alte an die Schiffsseite. Vorher prüfen: Passt der Verbinder durch Bugrolle und Kettenrohr? Erkennt der Kettenzähler den Verbinder korrekt? Gesamtgewicht und Kettenkasten-Volumen neu berechnen! **Confidence:** documented

---

## 10. Glossar

### Marine-Fachbegriffe Ankerkette (Deutsch–Englisch)

| Nr. | Deutsch | Englisch | Definition |
|---|---|---|---|
| G01 | Ankerkette | Anchor chain | Kette zur Verbindung des Ankers mit dem Schiff |
| G02 | Kettenvorlauf | Chain rode / chain leader | Kettenabschnitt zwischen Anker und Tau (bei Ketten-Tau-Kombination) |
| G03 | Rode | Rode | Gesamtverbindung Anker ↔ Schiff (Kette, Tau oder Kombination) |
| G04 | Güteklasse | Grade (G30, G40, G43, G70) | Festigkeitsklasse der Kette |
| G05 | Kurzgliedrig | Short link | Kettenglied mit Teilung ca. 3× Nennmaß |
| G06 | Langgliedrig | Long link | Kettenglied mit Teilung ca. 4–5× Nennmaß |
| G07 | Stegkette | Stud link chain | Kette mit Quersteg im Glied |
| G08 | Kalibriert | Calibrated | Enge Toleranzen für Kettennuss-Betrieb |
| G09 | Nennmaß | Nominal diameter | Drahtdurchmesser des Kettenglieds |
| G10 | Teilung | Pitch | Abstand zwischen den Mittelpunkten zweier benachbarter Glieder |
| G11 | Innenweite | Inside width | Lichte Weite des Kettenglieds |
| G12 | Außenweite | Outside width | Gesamtbreite des Kettenglieds |
| G13 | WLL | Working Load Limit | Maximale Dauerbetriebslast |
| G14 | Bruchlast | Breaking load / MBL | Last, bei der die Kette versagt |
| G15 | Prüflast | Proof load | Werkseitige Prüflast (typisch 2× WLL) |
| G16 | Feuerverzinkung | Hot-dip galvanizing | Korrosionsschutz durch Zinkbad |
| G17 | Zinkschicht | Zinc coating | Schutzschicht aus Zink auf dem Stahlkern |
| G18 | Kettennuss | Wildcat / gypsy | Profilierte Rolle an der Ankerwinsch für Kettenbetrieb |
| G19 | Spillkopf | Warping drum / capstan | Glatte Rolle an der Ankerwinsch für Taubetrieb |
| G20 | Kettenstopper | Chain stopper | Mechanismus zum Festhalten der Kette unter Last |
| G21 | Bugrolle | Bow roller | Rolle am Bug zur Führung der Ankerkette |
| G22 | Ankerwirbel | Anchor swivel | Drehgelenk zwischen Anker und Kette |
| G23 | Schäkel | Shackle | U-förmiger Verbinder mit Bolzen |
| G24 | Kenter-Schäkel | Kenter joining shackle | Zweiteiliger Kettenverbinder für Stegkette |
| G25 | Kettennotglied | Chain connecting link / quick link | Verbindungsglied zum Reparieren oder Verlängern |
| G26 | Kettenkasten | Chain locker | Staurum für die Ankerkette im Bug |
| G27 | Scope | Scope | Verhältnis ausgelegte Kettenlänge : Wassertiefe |
| G28 | Kettenary | Catenary | Durchhängekurve der Kette unter Eigengewicht und Last |
| G29 | Snubber | Snubber | Einzelne Ruckdämpfer-Leine |
| G30 | Bridle | Bridle / bridal | Doppelte Ruckdämpfer-Leine (Y-Form) |
| G31 | Kellet | Kellet / sentinel | Gewicht, das auf die Kette herabgelassen wird |
| G32 | Schwojen | Swinging / riding | Kreisbewegung des Schiffs um den Ankerpunkt |
| G33 | Kette drehen | End-for-end | Umdrehen der Kette zur gleichmäßigen Verschleißverteilung |
| G34 | Kinking | Kinking | Knickbildung in der Kette |
| G35 | Verdrallung | Twist / torque | Drehung der Kette um ihre Längsachse |
| G36 | Spaltkorrosion | Crevice corrosion | Korrosion in Spalten bei Edelstahl |
| G37 | Zamak | Zamac / pot metal | Zinkdruckguss — für Ankerwirbel UNGEEIGNET |
| G38 | Proof Coil | Proof coil | US-Bezeichnung für G30-Kette |
| G39 | BBB / Triple-B | BBB chain | US-Kettentyp mit kurzer Teilung |
| G40 | High Test | High test chain | US-Bezeichnung für G43-Kette |
| G41 | DIN 766 | DIN 766 | Deutsche Norm für kurzgliedrige kalibrierte Kette |
| G42 | ISO 4565 | ISO 4565 | Internationale Norm für kalibrierte Kette |
| G43 | Kausch | Thimble | Metalleinsatz im Tauauge zum Schutz gegen Scheuern |
| G44 | Sollbruchstelle | Weak link | Gewollte Schwachstelle am Kettenende (Schutz des Schiffs) |
| G45 | Chain-to-Rope-Splice | Chain splice | Verspleißung des Tauendes durch ein Kettenglied |
| G46 | Kettenzähler | Chain counter | Elektronisches Gerät zur Messung der ausgelegten Kettenlänge |
| G47 | Ankergalgen | Anchor davit | Haltevorrichtung für den Anker am Bug |

---

## 11. Schnell-Referenz

### 11.1 Kettenwahl auf einen Blick

| Bootslänge | Kette (mm) | Grade | Länge (m) | Gewicht (kg) | Budget (EUR) |
|---|---|---|---|---|---|
| 6–8 m | 6 | G30/G43 | 30–40 | 24–32 | 120–200 |
| 8–10 m | 8 | G40/G43 | 40–60 | 56–84 | 250–450 |
| 10–12 m | 8 | G43 | 60–80 | 84–112 | 350–600 |
| 12–14 m | 10 | G43 | 80–100 | 176–220 | 600–1000 |
| 14–16 m | 10 | G43 | 80–120 | 176–264 | 700–1200 |
| 16–20 m | 12 | G43 | 100–150 | 310–465 | 1200–2200 |
| 20–25 m | 12–14 | G43 | 120–200 | 372–860 | 1800–4000 |

### 11.2 Scope-Schnellreferenz

| Wassertiefe (m) | Scope 3:1 (m) | Scope 5:1 (m) | Scope 7:1 (m) | Scope 10:1 (m) |
|---|---|---|---|---|
| 3 | 9 | 15 | 21 | 30 |
| 5 | 15 | 25 | 35 | 50 |
| 8 | 24 | 40 | 56 | 80 |
| 10 | 30 | 50 | 70 | 100 |
| 15 | 45 | 75 | 105 | 150 |
| 20 | 60 | 100 | 140 | 200 |

> **Freibord beachten:** Zur Wassertiefe muss die Freibordhöhe (Bug bis Wasserlinie) addiert werden. Beispiel: 10 m Tiefe + 2 m Freibord = 12 m → Scope 5:1 = 60 m Kette.

### 11.3 Prüf-Checkliste (Jahreskontrolle)

- [ ] Kette vollständig ausgelegt und visuell inspiziert
- [ ] Zinkverlust beurteilt (≤50% akzeptabel, >75% tauschen)
- [ ] Drahtdurchmesser an 3 Stellen gemessen (>10% Verlust → tauschen)
- [ ] Teilung gemessen (10 Glieder, >3% Abweichung → tauschen)
- [ ] Kinks und Verformungen geprüft
- [ ] Schweißnähte auf Risse geprüft
- [ ] Ankerwirbel auf freie Drehung geprüft
- [ ] Schäkel auf festen Sitz und Sicherung geprüft
- [ ] Kettenstopper auf Funktion geprüft
- [ ] Kettenmarkierungen erneuert (falls verblasst)
- [ ] Kettenende-Befestigung (Sollbruchstelle) geprüft

---

## ANHANG A — Fallstudien

### Fallstudie A1: Kettenbruch bei Blauwasseryacht (Karibik)

**Yacht:** Hallberg-Rassy 46, Baujahr 2008, 14,2 m LOA
**Kette:** 10 mm G30, feuerverzinkt, 100 m, Alter 12 Jahre
**Revier:** Karibik, Martinique, 8 m Wassertiefe, Sand/Koralle
**Vorfall:** Bei Tropensturm (45 kn böig) Kettenbruch bei ca. 30 m. Yacht trieb auf Leeküste, erheblicher Schaden.

**Analyse:**
- Kette war 12 Jahre alt, nie inspiziert
- Zinkverlust >95% in den ersten 30 m (Tropenrevier)
- Drahtdurchmesser an der Bruchstelle: 8,2 mm (statt 10 mm nominell) = 18% Verschleiß
- Bruch an der Schweißnaht eines Glieds bei ca. 25 m
- Geschätzte Bruchlast der verschlissenen Kette: ca. 20 kN (statt 29,4 kN nominell)
- Geschätzte Ankerlast bei 45 kn Wind + Welle: ca. 25 kN

**AYDI-Bewertung:**
- **Ursache:** Verschleiß durch Alter und Tropenrevier, fehlende Inspektion
- **Vermeidbar:** Ja — jährliche Inspektion hätte den Verschleiß rechtzeitig erkannt
- **Empfehlung:** G43 statt G30 (höhere Bruchlast bei gleichem Gewicht), Inspektionsintervall 1 Jahr in Tropen, Neuverzinkung nach 5–7 Jahren
- **Confidence:** documented (Vorfall dokumentiert, Kette nachträglich untersucht)

### Fallstudie A2: Edelstahlkette mit Spaltkorrosion (Mittelmeer)

**Yacht:** Bavaria 40 Cruiser, Baujahr 2012, 12,4 m LOA
**Kette:** 10 mm AISI 316L Edelstahl, 80 m, Alter 8 Jahre
**Revier:** Mittelmeer, Griechenland, dauerhafter Liegeplatz an Mooring
**Vorfall:** Beim Ankern in einer Bucht brach ein Kettenglied bei ca. 15 m ohne Vorwarnung. Kein Sturm (15 kn Wind).

**Analyse:**
- Kette war 8 Jahre alt, im Kettenkasten dauerhaft feucht gelagert
- Spaltkorrosion an den Glied-zu-Glied-Kontaktflächen
- Lochfraß (Pitting) bis 1,5 mm Tiefe — äußerlich kaum sichtbar
- Restquerschnitt an der Bruchstelle: ca. 55% des Nennquerschnitts
- Bruch erfolgte bei geschätzt 8–10 kN (deutlich unter der Nenn-Bruchlast von 26,7 kN)

**AYDI-Bewertung:**
- **Ursache:** Spaltkorrosion durch dauerhaft feuchte, sauerstoffarme Lagerung im Kettenkasten
- **Vermeidbar:** Ja — regelmäßiges Spülen und Trocknen, jährliche gründliche Inspektion der Gliedinnenflächen
- **Empfehlung:** Edelstahlketten in Salzwasserrevieren nach jedem Einsatz komplett spülen und trocknen. Bei Dauerliegern an Mooring: verzinkte Kette bevorzugen.
- **Confidence:** documented

### Fallstudie A3: Falsche Kette auf falscher Kettennuss (Nordsee)

**Yacht:** Dehler 38, Baujahr 2015, 11,5 m LOA
**Kette:** 8 mm unkalibriert (DIN 5685), feuerverzinkt, 60 m
**Winsch:** Lewmar V2, Kettennuss für 8 mm DIN 766
**Vorfall:** Beim Einfahren der Kette unter Last sprang die Kette aus der Kettennuss. Crew-Mitglied erlitt Handverletzung durch die durchschießende Kette.

**Analyse:**
- Eigner hatte die Kette im Baumarkt gekauft („8 mm verzinkt")
- Kette war DIN 5685 (unkalibriert), nicht DIN 766 (kalibriert)
- Teilung der Kette schwankte zwischen 22 und 26 mm (DIN 766: 24,0 ± 0,5 mm)
- Kette saß bei manchen Gliedern in der Kettennuss, bei anderen nicht
- Unter Last (ca. 5 kN) sprang die Kette in einer Nuss-Position heraus

**AYDI-Bewertung:**
- **Ursache:** Unkalibrierte Kette auf kalibrierter Kettennuss
- **Vermeidbar:** Ja — nur DIN 766 / ISO 4565 kalibrierte Kette für Windenbetrieb
- **Sicherheitshinweis:** Hände NIEMALS in den Kettenlauf bringen. Kette unter Last ist lebensgefährlich.
- **Confidence:** documented

### Fallstudie A4: Kettenvorlauf zu kurz für Korallengrund (Pazifik)

**Yacht:** Lagoon 42, Baujahr 2019, 12,8 m LOA
**Rode:** 8 m × 8 mm G40 Kette + 60 m × 14 mm Nylon 3-Schlag
**Revier:** Südpazifik, Fidschi, 10 m Wassertiefe, Korallen-Bommies
**Vorfall:** Nach zwei Wochen vor Anker war das Nylontau am Übergang zur Kette durchgescheuert. Yacht trieb nachts ab.

**Analyse:**
- Bei Scope 5:1 und 10 m Tiefe: 50 m Rode ausgelegt
- 8 m Kette + 42 m Tau → das Tau lag auf dem Korallengrund
- Korallenköpfe scheuerten über 14 Tage durch das 14 mm Nylontau
- Durchscheuerung am Übergang Kette → Tau (heftigste Scheuerbewegung)

**AYDI-Bewertung:**
- **Ursache:** Kettenvorlauf zu kurz für Korallenrevier
- **Empfehlung:** In Korallenrevieren min. 20 m Kettenvorlauf oder All-Chain-Rode. Tauwerk darf niemals auf Korallen aufliegen.
- **Alternativ:** Scheuerschutz-Schlauch (Chafe Guard) über das Tau am Übergangsbereich
- **Confidence:** documented

### Fallstudie A5: Kettenkasten-Überlastung durch Wasseransammlung (Atlantik)

**Yacht:** Oyster 56, Baujahr 2010, 17,2 m LOA
**Kette:** 12 mm G43, 120 m, feuerverzinkt
**Vorfall:** Während Atlantiküberquerung (Trade-Wind-Passage) nahm das Vorschiff bei Gegenwelle Wasser über die Bugrolle auf. Der Kettenkasten füllte sich über 3 Tage mit geschätzten 400 Litern Salzwasser. Gesamtgewicht Kettenkasten: 372 kg Kette + 400 kg Wasser = 772 kg. Yacht trimmte massiv auf den Bug, Seegangsverhalten verschlechterte sich dramatisch.

**AYDI-Bewertung:**
- **Ursache:** Unzureichende Drainage des Kettenkastens, Bugrolle nicht wasserdicht verschließbar
- **Konstruktiver Hinweis:** Kettenkasten-Drainage muss auch bei Krängung und Seegang funktionieren. Ablauf in die Bilge mit Rückschlagventil. Bugrolle mit Verschluss-Platte bei Seefahrt.
- **Confidence:** documented

### Fallstudie A6: Galvanische Korrosion durch Materialmischung

**Yacht:** Jeanneau Sun Odyssey 45, Baujahr 2007, 13,7 m LOA
**Setup:** AISI 316 Edelstahl-Ankerwirbel + feuerverzinkte G43 Kette + feuerverzinkter Anker
**Vorfall:** Nach 3 Jahren war die Verzinkung der ersten 3 Glieder (um den Edelstahl-Wirbel herum) vollständig aufgelöst. Massive Rostbildung und Querschnittsschwächung.

**AYDI-Bewertung:**
- **Ursache:** Galvanisches Element: Edelstahl (edler) + verzinkter Stahl (unedler) → Zink opfert beschleunigt
- **Empfehlung:** Materialien im Ankergeschirr sollten galvanisch kompatibel sein. Entweder alles Edelstahl oder alles verzinkt. Bei Mischung: Opferanode (Zinkanode) am Wirbel befestigen.
- **Confidence:** documented

### Fallstudie A7: Kette zu schwer für Ankerwinsch (Mittelmeer)

**Yacht:** Beneteau Oceanis 38.1, Baujahr 2020, 11,5 m LOA
**Setup:** 10 mm G43 Kette, 80 m + Lewmar V700 Winsch (700 W)
**Vorfall:** In 18 m Wassertiefe konnte die Winsch die Kette nicht einholen (überlastet, Sicherung fiel). Crew musste die letzten 20 m von Hand einholen.

**Analyse:**
- 80 m × 10 mm = 176 kg Kette total
- In 18 m Tiefe hängen ca. 40 kg Kette senkrecht im Wasser + Ankergewicht (15 kg)
- Lewmar V700: max. Zugkraft 700 kg, Dauerleistung ca. 250 kg
- Bei Seegang und strammer Kette (Kette sitzt im Grund) → Zuglast > Dauerleistung

**AYDI-Bewertung:**
- **Ursache:** Winsch unterdimensioniert für 10 mm × 80 m bei >15 m Wassertiefe
- **Empfehlung:** Für 10 mm Kette: min. 1000 W Winsch. Für die Oceanis 38.1 wäre 8 mm G43 die richtige Kette (ausreichende Festigkeit bei halbem Gewicht). Alternativ: Winsch-Upgrade auf 1000 W.
- **Confidence:** documented

### Fallstudie A8: Erfolgreiche Sturmverankerung mit optimiertem Ankergeschirr

**Yacht:** Amel 55, Baujahr 2018, 16,8 m LOA
**Setup:** 10 mm G43 Kette, 120 m + 20 mm Nylon-Snubber, 12 m + Ultra-Anker 25 kg
**Revier:** Bahamas, 6 m Wassertiefe, Sand, Hurrikan Dorian (2019) — Ausläufer, 55 kn sustained

**Verlauf:**
- 80 m Kette ausgelegt (Scope 13:1)
- Snubber auf 8 m aufgesetzt, Kettenstopper geschlossen
- Zweiter Anker (15 kg, 8 mm × 30 m Kette + 60 m Nylon) als Backup in 45° Winkel
- Yacht schwojte 12 Stunden in Böen bis 65 kn. Kein Treiben, keine Schäden.

**AYDI-Bewertung:**
- **Erfolgsfaktoren:** Ausreichend Kettenlänge (hohes Scope), leistungsfähiger Snubber (20 mm Nylon → hervorragende Ruckdämpfung), gut gesetzter Anker, Backup-Anker
- **Empfehlung als Best Practice:** Scope ≥10:1 bei Sturm, immer Snubber, Zweitanker vorbereitet
- **Confidence:** documented

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

### B.1 Datenmodelle für Ankerketten-Analyse

```python
"""
AYDI Anchor Chain Analysis Models
Module: 13_02_ankerketten
Pydantic v2 models for anchor chain assessment, sizing, and defect analysis.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ChainGrade(str, Enum):
    """Chain grade classification."""
    G30 = "G30"
    G40 = "G40"
    G43 = "G43"
    G70 = "G70"
    STAINLESS_316 = "stainless_316"
    STAINLESS_316L = "stainless_316L"


class ChainStandard(str, Enum):
    """Chain dimensional standard."""
    DIN_766 = "DIN_766"
    ISO_4565 = "ISO_4565"
    BBB = "BBB"
    STUD_LINK_ISO_1704 = "stud_link_ISO_1704"
    DIN_5685_UNCALIBRATED = "DIN_5685"


class ChainMaterial(str, Enum):
    """Chain material and coating."""
    GALVANIZED_CARBON = "galvanized_carbon_steel"
    STAINLESS_316 = "stainless_AISI_316"
    STAINLESS_316L = "stainless_AISI_316L"
    BARE_CARBON = "bare_carbon_steel"
    ELECTROPLATED = "electroplated_zinc"


class RodeType(str, Enum):
    """Rode system type."""
    ALL_CHAIN = "all_chain"
    CHAIN_ROPE = "chain_rope"
    ALL_ROPE = "all_rope"


class ChainDefectType(str, Enum):
    """Chain defect classification matching Fehlerbild-Atlas."""
    F01_WEAR = "link_wear"
    F02_ZINC_LOSS = "galvanic_coating_loss"
    F03_STRETCH = "chain_stretch"
    F04_KINKING = "kinking"
    F05_CORROSION = "corrosion"
    F06_WELD_FAILURE = "weld_break"
    F07_CREVICE_CORROSION = "crevice_corrosion"
    F08_TWIST = "twist_torque"
    F09_DEFORMATION = "link_deformation"
    F10_COATING_FLAKE = "coating_delamination"
    F11_FOREIGN_METAL = "foreign_metal_contamination"
    F12_FATIGUE_CRACK = "fatigue_crack"


class SeverityLevel(str, Enum):
    """Defect severity classification."""
    LOW = "niedrig"
    MEDIUM = "mittel"
    HIGH = "hoch"
    CRITICAL = "kritisch"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for findings."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ChainLinkDimensions(BaseModel):
    """Dimensional specification of a chain link per DIN 766 / ISO 4565."""

    model_config = {"from_attributes": True}

    nominal_diameter_mm: float = Field(
        ..., description="Wire diameter d in mm", ge=4.0, le=30.0
    )
    pitch_mm: float = Field(
        ..., description="Pitch p in mm (center-to-center of adjacent links)"
    )
    pitch_tolerance_mm: float = Field(
        ..., description="Pitch tolerance +/- in mm"
    )
    inside_width_mm: float = Field(
        ..., description="Inside width b1 in mm"
    )
    inside_width_tolerance_mm: float = Field(
        ..., description="Inside width tolerance +/- in mm"
    )
    outside_width_mm: float = Field(
        ..., description="Outside width b2 in mm"
    )
    outside_length_mm: float = Field(
        ..., description="Outside length L in mm"
    )
    standard: ChainStandard = Field(
        ..., description="Dimensional standard"
    )


class ChainSpecification(BaseModel):
    """Complete specification of an anchor chain."""

    model_config = {"from_attributes": True}

    nominal_diameter_mm: float = Field(
        ..., description="Nominal chain diameter in mm", ge=4.0, le=30.0
    )
    grade: ChainGrade = Field(
        ..., description="Chain grade"
    )
    standard: ChainStandard = Field(
        ..., description="Dimensional standard"
    )
    material: ChainMaterial = Field(
        ..., description="Material and coating"
    )
    wll_kn: float = Field(
        ..., description="Working Load Limit in kN", ge=0
    )
    breaking_load_kn: float = Field(
        ..., description="Minimum Breaking Load in kN", ge=0
    )
    proof_load_kn: float = Field(
        ..., description="Proof test load in kN", ge=0
    )
    weight_per_meter_kg: float = Field(
        ..., description="Weight per meter in kg", ge=0
    )
    length_m: float = Field(
        ..., description="Total chain length in meters", ge=0
    )
    link_dimensions: Optional[ChainLinkDimensions] = Field(
        None, description="Detailed link dimensions"
    )
    zinc_coating_um: Optional[float] = Field(
        None, description="Zinc coating thickness in micrometers", ge=0
    )
    manufacturer: Optional[str] = Field(
        None, description="Chain manufacturer"
    )
    certification: Optional[str] = Field(
        None, description="Certification (e.g., ISO 9001, ABS, Lloyd's)"
    )
    age_years: Optional[float] = Field(
        None, description="Age of the chain in years", ge=0
    )
    price_per_meter_eur: Optional[float] = Field(
        None, description="Price per meter in EUR", ge=0
    )


class RodeConfiguration(BaseModel):
    """Complete rode system configuration."""

    model_config = {"from_attributes": True}

    rode_type: RodeType = Field(
        ..., description="Type of rode system"
    )
    primary_chain: ChainSpecification = Field(
        ..., description="Primary chain specification"
    )
    rope_diameter_mm: Optional[float] = Field(
        None, description="Rope diameter in mm (for chain-rope rode)"
    )
    rope_length_m: Optional[float] = Field(
        None, description="Rope length in meters"
    )
    rope_material: Optional[str] = Field(
        None, description="Rope material (e.g., nylon_3_strand)"
    )
    rope_breaking_load_kn: Optional[float] = Field(
        None, description="Rope breaking load in kN"
    )
    chain_to_rope_connection: Optional[str] = Field(
        None, description="Connection method (splice, thimble_shackle, connector)"
    )
    swivel_type: Optional[str] = Field(
        None, description="Anchor swivel type"
    )
    swivel_wll_kg: Optional[float] = Field(
        None, description="Swivel WLL in kg"
    )
    snubber_diameter_mm: Optional[float] = Field(
        None, description="Snubber diameter in mm"
    )
    snubber_length_m: Optional[float] = Field(
        None, description="Snubber length in meters"
    )
    total_weight_kg: Optional[float] = Field(
        None, description="Total rode weight in kg"
    )


class ChainDefect(BaseModel):
    """Individual chain defect finding."""

    model_config = {"from_attributes": True}

    defect_type: ChainDefectType = Field(
        ..., description="Defect classification per Fehlerbild-Atlas"
    )
    severity: SeverityLevel = Field(
        ..., description="Severity level"
    )
    location_m: Optional[float] = Field(
        None, description="Location on chain in meters from anchor end"
    )
    description_de: str = Field(
        ..., description="German description of the defect"
    )
    measurement_value: Optional[float] = Field(
        None, description="Measured value (e.g., diameter reduction in %)"
    )
    measurement_unit: Optional[str] = Field(
        None, description="Unit of the measured value"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of the finding"
    )
    recommendation_de: str = Field(
        ..., description="German recommendation for action"
    )
    photo_reference: Optional[str] = Field(
        None, description="Reference to photo evidence"
    )


class ChainInspectionResult(BaseModel):
    """Complete chain inspection result."""

    model_config = {"from_attributes": True}

    chain: ChainSpecification = Field(
        ..., description="Chain specification"
    )
    inspection_date: str = Field(
        ..., description="Inspection date (ISO 8601)"
    )
    inspector: Optional[str] = Field(
        None, description="Inspector name or AYDI-auto"
    )
    overall_condition_score: float = Field(
        ..., description="Overall condition score 0-100", ge=0, le=100
    )
    remaining_life_years: Optional[float] = Field(
        None, description="Estimated remaining life in years", ge=0
    )
    defects: list[ChainDefect] = Field(
        default_factory=list, description="List of defects found"
    )
    zinc_loss_percent: Optional[float] = Field(
        None, description="Estimated zinc coating loss in %", ge=0, le=100
    )
    diameter_loss_percent: Optional[float] = Field(
        None, description="Maximum diameter reduction in %", ge=0, le=100
    )
    pitch_deviation_percent: Optional[float] = Field(
        None, description="Maximum pitch deviation in %", ge=0, le=100
    )
    chain_stopper_ok: Optional[bool] = Field(
        None, description="Chain stopper functional"
    )
    swivel_ok: Optional[bool] = Field(
        None, description="Swivel rotates freely"
    )
    markings_visible: Optional[bool] = Field(
        None, description="Length markings still visible"
    )
    recommendation_de: str = Field(
        ..., description="Overall German recommendation"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Overall confidence level"
    )


class ChainSizingInput(BaseModel):
    """Input parameters for chain sizing calculation."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(
        ..., description="Boat LOA in meters", ge=4.0, le=50.0
    )
    boat_displacement_kg: Optional[float] = Field(
        None, description="Boat displacement in kg", ge=500
    )
    boat_type: str = Field(
        ..., description="Boat type (sailboat, motorboat, catamaran, superyacht)"
    )
    cruising_area: str = Field(
        ..., description="Cruising area (coastal, mediterranean, bluewater, tropical)"
    )
    max_anchor_depth_m: float = Field(
        ..., description="Maximum expected anchoring depth in meters", ge=1, le=100
    )
    max_expected_wind_kn: float = Field(
        ..., description="Maximum expected wind in knots", ge=10, le=100
    )
    windlass_model: Optional[str] = Field(
        None, description="Existing windlass model"
    )
    windlass_power_w: Optional[float] = Field(
        None, description="Windlass power in watts", ge=0
    )
    budget_eur: Optional[float] = Field(
        None, description="Budget for chain in EUR", ge=0
    )
    weight_sensitivity: str = Field(
        default="normal",
        description="Weight sensitivity (low, normal, high, racing)"
    )


class ChainSizingResult(BaseModel):
    """Result of chain sizing calculation."""

    model_config = {"from_attributes": True}

    recommended_diameter_mm: float = Field(
        ..., description="Recommended chain diameter in mm"
    )
    recommended_grade: ChainGrade = Field(
        ..., description="Recommended chain grade"
    )
    recommended_length_m: float = Field(
        ..., description="Recommended chain length in meters"
    )
    minimum_length_m: float = Field(
        ..., description="Minimum acceptable length in meters"
    )
    total_weight_kg: float = Field(
        ..., description="Total chain weight in kg"
    )
    chain_locker_volume_liters: float = Field(
        ..., description="Required chain locker volume in liters"
    )
    recommended_snubber_diameter_mm: float = Field(
        ..., description="Recommended snubber diameter in mm"
    )
    recommended_snubber_length_m: float = Field(
        ..., description="Recommended snubber length in meters"
    )
    windlass_min_power_w: float = Field(
        ..., description="Minimum windlass power in watts"
    )
    estimated_cost_eur: float = Field(
        ..., description="Estimated chain cost in EUR"
    )
    rode_type: RodeType = Field(
        ..., description="Recommended rode type"
    )
    alternative_options: list[str] = Field(
        default_factory=list,
        description="Alternative sizing options with trade-offs"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnings about the configuration"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of the sizing"
    )
    notes_de: str = Field(
        ..., description="German notes and explanations"
    )


class ChainLockerDesign(BaseModel):
    """Chain locker design parameters for yacht construction."""

    model_config = {"from_attributes": True}

    volume_liters: float = Field(
        ..., description="Required volume in liters", ge=10
    )
    min_depth_mm: float = Field(
        ..., description="Minimum depth in mm", ge=200
    )
    drainage_diameter_mm: float = Field(
        ..., description="Drainage pipe diameter in mm", ge=20
    )
    structural_load_kn: float = Field(
        ..., description="Maximum structural load in kN from chain pull", ge=0
    )
    chain_weight_kg: float = Field(
        ..., description="Weight of chain in kg", ge=0
    )
    water_weight_kg: float = Field(
        ..., description="Estimated max water accumulation in kg", ge=0
    )
    total_weight_kg: float = Field(
        ..., description="Total weight (chain + water) in kg", ge=0
    )
    cg_position_mm: Optional[list[float]] = Field(
        None,
        description="Center of gravity [x, y, z] in mm from reference point"
    )
    hawse_pipe_diameter_mm: Optional[float] = Field(
        None, description="Hawse pipe internal diameter in mm"
    )
    wash_down_required: bool = Field(
        default=True, description="Whether a wash-down system is recommended"
    )
    self_stacking: bool = Field(
        default=False, description="Whether the locker has self-stacking geometry"
    )
    notes_de: str = Field(
        default="", description="German design notes"
    )
```

### B.2 Analyse-Funktionen (Stub)

```python
"""
AYDI Anchor Chain Analysis Functions
Module: 13_02_ankerketten
Pure analysis functions — no DB access, standardized return dicts.
"""

from __future__ import annotations

from typing import Any


def calculate_chain_sizing(
    boat_length_m: float,
    boat_displacement_kg: float | None,
    boat_type: str,
    cruising_area: str,
    max_depth_m: float,
    max_wind_kn: float,
    weight_sensitivity: str = "normal",
) -> dict[str, Any]:
    """
    Calculate recommended anchor chain sizing based on boat parameters.

    Returns a standardized dict with:
    - recommended_diameter_mm
    - recommended_grade
    - recommended_length_m
    - total_weight_kg
    - chain_locker_volume_liters
    - confidence
    - warnings (list of str)
    """
    # Diameter selection based on boat length and grade
    if boat_length_m <= 8:
        base_diameter = 6
    elif boat_length_m <= 12:
        base_diameter = 8
    elif boat_length_m <= 16:
        base_diameter = 10
    elif boat_length_m <= 22:
        base_diameter = 12
    else:
        base_diameter = 14

    # Grade selection based on cruising area
    grade_map = {
        "coastal": "G40",
        "mediterranean": "G43",
        "bluewater": "G43",
        "tropical": "G43",
    }
    grade = grade_map.get(cruising_area, "G43")

    # Length calculation
    base_length = max_depth_m * 5 + 20
    area_multiplier = {
        "coastal": 1.0,
        "mediterranean": 1.2,
        "bluewater": 1.5,
        "tropical": 1.5,
    }
    recommended_length = base_length * area_multiplier.get(cruising_area, 1.2)
    recommended_length = max(30, min(200, recommended_length))

    # Weight per meter lookup
    weight_table = {6: 0.79, 8: 1.40, 10: 2.20, 12: 3.10, 14: 4.30, 16: 5.60}
    weight_per_m = weight_table.get(base_diameter, 2.20)
    total_weight = weight_per_m * recommended_length

    # Chain locker volume
    locker_volume = total_weight * 1.8 * 1.2  # 20% safety margin

    warnings = []
    if total_weight > boat_length_m * 15:
        warnings.append(
            "Kettengewicht ist hoch relativ zur Bootslänge. "
            "Trimmauswirkung prüfen."
        )
    if weight_sensitivity == "racing" and base_diameter > 8:
        warnings.append(
            "Für Regattaeinsatz: G70 oder Chain-Rope-Rode erwägen "
            "zur Gewichtsreduktion."
        )

    return {
        "recommended_diameter_mm": base_diameter,
        "recommended_grade": grade,
        "recommended_length_m": round(recommended_length),
        "minimum_length_m": round(recommended_length * 0.7),
        "total_weight_kg": round(total_weight, 1),
        "chain_locker_volume_liters": round(locker_volume),
        "confidence": "estimated",
        "warnings": warnings,
    }


def assess_chain_condition(
    diameter_loss_percent: float,
    zinc_loss_percent: float,
    pitch_deviation_percent: float,
    age_years: float,
    defect_count: int,
    has_critical_defect: bool,
) -> dict[str, Any]:
    """
    Assess overall chain condition based on measurements.

    Returns a standardized dict with:
    - overall_score (0-100)
    - remaining_life_years (estimated)
    - recommendation_de (German recommendation)
    - confidence
    """
    score = 100.0

    # Diameter loss impact
    if diameter_loss_percent > 15:
        score -= 60
    elif diameter_loss_percent > 10:
        score -= 40
    elif diameter_loss_percent > 5:
        score -= 15

    # Zinc loss impact
    if zinc_loss_percent > 90:
        score -= 25
    elif zinc_loss_percent > 75:
        score -= 15
    elif zinc_loss_percent > 50:
        score -= 8

    # Pitch deviation impact
    if pitch_deviation_percent > 3:
        score -= 40
    elif pitch_deviation_percent > 2:
        score -= 20
    elif pitch_deviation_percent > 1:
        score -= 5

    # Age impact
    if age_years > 15:
        score -= 15
    elif age_years > 10:
        score -= 8

    # Defect impact
    score -= defect_count * 3
    if has_critical_defect:
        score = min(score, 20)

    score = max(0, min(100, score))

    # Recommendation
    if score >= 80:
        recommendation = "Kette in gutem Zustand. Nächste Inspektion in 12 Monaten."
        remaining_life = max(1, 15 - age_years)
    elif score >= 60:
        recommendation = (
            "Kette zeigt Verschleiß. Verstärkte Inspektion empfohlen. "
            "Neuverzinkung erwägen."
        )
        remaining_life = max(0.5, (15 - age_years) * 0.5)
    elif score >= 40:
        recommendation = (
            "Kette erheblich verschlissen. Austausch innerhalb der "
            "nächsten Saison planen."
        )
        remaining_life = max(0, min(2, (15 - age_years) * 0.3))
    elif score >= 20:
        recommendation = (
            "Kette stark verschlissen. Austausch vor dem nächsten "
            "Ankermanöver dringend empfohlen."
        )
        remaining_life = 0
    else:
        recommendation = (
            "Kette unbrauchbar. Sofortiger Austausch erforderlich. "
            "NICHT ANKERN mit dieser Kette."
        )
        remaining_life = 0

    return {
        "overall_score": round(score, 1),
        "remaining_life_years": round(remaining_life, 1),
        "recommendation_de": recommendation,
        "confidence": "measured" if diameter_loss_percent > 0 else "estimated",
    }


def calculate_anchor_load(
    boat_length_m: float,
    wind_speed_kn: float,
    scope_ratio: float,
    chain_diameter_mm: float,
    water_depth_m: float,
    dynamic_factor: float = 2.5,
) -> dict[str, Any]:
    """
    Calculate anchor load for given conditions.

    Returns a standardized dict with:
    - static_load_kn
    - dynamic_load_kn
    - chain_angle_deg (angle at anchor)
    - safety_factor (vs chain breaking load)
    - confidence
    """
    # Simplified wind load calculation (ABYC method approximation)
    # Wind load in kN ≈ 0.0005 × V² × A (V in m/s, A in m²)
    wind_speed_ms = wind_speed_kn * 0.5144
    # Approximate windage area based on boat length
    windage_area = boat_length_m * 1.5  # rough estimate
    static_load_kn = 0.0005 * wind_speed_ms ** 2 * windage_area

    dynamic_load_kn = static_load_kn * dynamic_factor

    # Chain angle at anchor (simplified catenary)
    if scope_ratio > 0:
        import math
        chain_angle_deg = math.degrees(math.atan(1.0 / scope_ratio))
    else:
        chain_angle_deg = 90.0

    # Breaking load lookup for G43
    breaking_load_table = {
        6: 16.5, 8: 29.4, 10: 45.9, 12: 66.1, 14: 90.7, 16: 117.6
    }
    breaking_load = breaking_load_table.get(chain_diameter_mm, 29.4)
    safety_factor = breaking_load / dynamic_load_kn if dynamic_load_kn > 0 else 999

    return {
        "static_load_kn": round(static_load_kn, 2),
        "dynamic_load_kn": round(dynamic_load_kn, 2),
        "chain_angle_deg": round(chain_angle_deg, 1),
        "safety_factor": round(safety_factor, 1),
        "breaking_load_kn": breaking_load,
        "confidence": "estimated",
        "warning": (
            "Sicherheitsfaktor < 4 — Kette unterdimensioniert!"
            if safety_factor < 4 else None
        ),
    }
```

---

## ANHANG C — Normen und Standards

### C.1 Relevante Normen im Überblick

| Norm | Titel | Relevanz |
|---|---|---|
| DIN 766 | Rundstahlkette, kurzgliedrig, kalibriert | Hauptnorm für europäische Yacht-Ankerketten |
| ISO 4565 | Short link chain, calibrated, Grade 30/40 | Internationale Entsprechung zu DIN 766 |
| DIN 5685-C | Rundstahlkette, langgliedrig | Langgliedrige Kette (nicht für Kettennuss) |
| DIN 5685-A | Rundstahlkette, kurzgliedrig, unkalibriert | Baumarktkette — NICHT für Ankerwinsch |
| DIN EN 818-2 | Kurzgliedrige Rundstahlketten, G80 | Hebezeug-Kette — NICHT als Ankerkette |
| ISO 1704 | Stud link anchor chain | Stegkette für Berufsschifffahrt/Superyachten |
| DIN 82101 | Ankerkette, Stegkette | Deutsche Stegketten-Norm |
| DIN EN ISO 1461 | Feuerverzinkung | Zinkschichtdicken und Prüfung |
| NACM Standard | Chain specifications (US) | US-Kettenstandards (BBB, Proof Coil, High Test) |
| ASTM A413 | Carbon steel chain | US-Werkstoffnorm für Kettenstahl |
| ISO 9001 | Qualitätsmanagementsystem | Herstellerzertifizierung |
| IACS UR W18 | Materials for anchor chain cables | Klassifikationsgesellschaften-Norm |

### C.2 Prüfanforderungen nach DIN 766

| Prüfung | Anforderung | Frequenz |
|---|---|---|
| Maßprüfung (Teilung, Durchmesser) | 100% Sichtprüfung, 10% Messung | Jede Charge |
| Proof-Test (Prüflast) | 2× WLL, kein Bruch, keine bleibende Verformung | Jede Kettenlänge |
| Bruchlast-Test | MBL ≥ Nennwert | Stichprobe (1 pro Charge) |
| Feuerverzinkung Schichtdicke | ≥ Mindestwert nach DIN EN ISO 1461 | Stichprobe |
| Visuelle Prüfung | Keine Risse, keine Kerben, saubere Schweißnaht | 100% |
| Kennzeichnung | Hersteller, Nennmaß, ggf. Grade | Jede Kette |

---

## ANHANG D — Belastungstabellen

### D.1 Windlast auf Yacht (statisch, vereinfacht)

| Bootslänge (m) | 15 kn (kN) | 20 kn (kN) | 30 kn (kN) | 40 kn (kN) | 50 kn (kN) | 60 kn (kN) |
|---|---|---|---|---|---|---|
| 6 | 0,2 | 0,4 | 0,8 | 1,4 | 2,2 | 3,2 |
| 8 | 0,3 | 0,6 | 1,3 | 2,3 | 3,5 | 5,1 |
| 10 | 0,5 | 0,8 | 1,8 | 3,2 | 5,0 | 7,2 |
| 12 | 0,6 | 1,0 | 2,3 | 4,0 | 6,3 | 9,0 |
| 14 | 0,8 | 1,3 | 2,9 | 5,1 | 8,0 | 11,5 |
| 16 | 0,9 | 1,6 | 3,5 | 6,3 | 9,8 | 14,1 |
| 20 | 1,2 | 2,2 | 4,9 | 8,7 | 13,6 | 19,5 |
| 25 | 1,7 | 3,0 | 6,7 | 11,9 | 18,6 | 26,8 |

> **Hinweis:** Dynamische Lasten (Welle, Gieren) können das 2–3-fache betragen. Sicherheitsfaktor ≥ 4 empfohlen.

### D.2 Bruchlast nach Kettengröße und Grade

| Nennmaß (mm) | G30 (kN) | G40 (kN) | G43 (kN) | G70 (kN) | AISI 316L (kN) |
|---|---|---|---|---|---|
| 6 | 10,5 | 14,0 | 16,5 | 24,6 | 9,6 |
| 8 | 18,9 | 24,9 | 29,4 | 43,7 | 17,1 |
| 10 | 29,4 | 38,9 | 45,9 | 68,4 | 26,7 |
| 12 | 42,3 | 56,0 | 66,1 | 98,4 | 38,4 |
| 13 | 49,5 | 65,8 | 77,8 | 115,8 | 45,3 |
| 14 | 57,5 | 76,1 | 90,7 | 134,5 | 52,8 |
| 16 | 75,0 | 99,7 | 117,6 | 175,2 | 68,4 |

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Zuordnung für Ankerketten-Analyse

| Datenpunkt | Pipeline A (Strukturiert) | Pipeline B (Visuell) | Pipeline C (Text) |
|---|---|---|---|
| Kettendurchmesser | measured (Messung) | visual_medium (Foto) | — |
| Kettenlänge | measured (Kettenzähler) | — | documented (Bericht) |
| Güteklasse | measured (Zertifikat) | visual_low (Prägung) | documented (Kaufbeleg) |
| Zinkverlust | measured (Schichtdickenmessung) | visual_high (Foto) | — |
| Verschleiß (Durchmesser) | measured (Messschieber) | visual_medium (Foto) | — |
| Teilungsdehnung | measured (Messung 10 Glieder) | — | — |
| Kinking | — | visual_high (Foto) | documented (Bericht) |
| Korrosion | — | visual_high (Foto) | documented (Bericht) |
| Schweißnaht-Bruch | measured (Prüfung) | visual_medium (Foto) | — |
| Spaltkorrosion | measured (PT/MT-Prüfung) | visual_insufficient | — |
| Wirbel-Funktion | measured (Drehtest) | visual_low | — |
| Kettenstopper | measured (Belastungstest) | visual_medium | documented |
| Kettenkasten-Zustand | — | visual_medium (Foto) | documented |

### E.2 Score-Fusion-Gewichte für Modul 13.02

| Bewertungsaspekt | Gewicht Strukturiert | Gewicht Visuell |
|---|---|---|
| Kettenzustand gesamt | 0,70 | 0,30 |
| Verschleiß quantitativ | 0,90 | 0,10 |
| Korrosion/Zinkverlust | 0,40 | 0,60 |
| Mechanische Defekte | 0,50 | 0,50 |
| Zubehör-Zustand | 0,60 | 0,40 |
| Dimensionierung | 1,00 | 0,00 |
| Normenkonformität | 1,00 | 0,00 |

---

## ANHANG F — Wartungsintervalle

### F.1 Empfohlene Wartungsintervalle

| Maßnahme | Intervall (Küstenfahrt) | Intervall (Blauwasser) | Intervall (Tropen) |
|---|---|---|---|
| Süßwasserspülung nach Ankern | Jedes Mal | Jedes Mal | Jedes Mal |
| Visuelle Inspektion (Gesamtkette) | 1× jährlich | 2× jährlich | 2× jährlich |
| Messung Durchmesser (Stichproben) | 1× jährlich | 1× jährlich | 2× jährlich |
| Messung Teilung (10 Glieder) | 1× jährlich | 1× jährlich | 2× jährlich |
| Wirbel-Funktionsprüfung | 1× jährlich | 2× jährlich | 2× jährlich |
| Schäkel-Sicherung prüfen | 1× jährlich | 2× jährlich | 2× jährlich |
| Kettenstopper-Funktionsprüfung | 1× jährlich | 2× jährlich | 2× jährlich |
| Kettenmarkierung erneuern | Bei Bedarf | 1× jährlich | 1× jährlich |
| Kette drehen (End-for-End) | Alle 5 Jahre | Alle 3 Jahre | Alle 3 Jahre |
| Neuverzinkung | Alle 10–15 Jahre | Alle 7–10 Jahre | Alle 5–7 Jahre |
| Kette komplett austauschen | Alle 15–20 Jahre | Alle 10–15 Jahre | Alle 8–12 Jahre |

---

## ANHANG G — Historische Entwicklung

### G.1 Meilensteine der Ankerketten-Entwicklung

| Zeitraum | Entwicklung | Bedeutung für den Yachtbau |
|---|---|---|
| ca. 500 v. Chr. | Erste Eisenketten in der Schifffahrt (Phönizier) | Ablösung von Steinankern mit Naturfaser-Tauen |
| 1808 | Samuel Brown: Patentierte Stegkette | Standard für Berufsschifffahrt bis heute |
| 1834 | Erste genormte Kettenteilung (UK Admiralty) | Basis für Kettennuss-Entwicklung |
| 1920er | Einführung der Feuerverzinkung als Standard | Korrosionsschutz für Kohlenstoffstahl-Ketten |
| 1950er | DIN 766 standardisiert kurzgliedrige Kette | Europäischer Standard für Yachtketten |
| 1960er | Erste elektrische Ankerwinschen für Yachten | All-Chain-Rode wird für Fahrtenyachten praktikabel |
| 1970er | G43 High-Test-Kette kommerziell verfügbar | Höhere Festigkeit bei gleichem Gewicht |
| 1980er | AISI 316 Edelstahlkette im Yachtmarkt | Alternative für ästhetisch orientierte Eigner |
| 1990er | ISO 4565 harmonisiert internationale Standards | Globale Austauschbarkeit |
| 2000er | Elektronische Kettenzähler Standard auf Fahrtenyachten | Präzise Scope-Kontrolle |
| 2010er | G70 Transport Chain im Yachtmarkt | Leichtbau-Option für Performance-Yachten |
| 2020er | Integration in digitale Monitoring-Systeme | IoT-Sensoren für Kettenbelastung und -zustand |

---

## ANHANG H — Bezugsquellen

### H.1 Europa

| Händler | Land | Sortiment | Online-Shop | Preissegment |
|---|---|---|---|---|
| SVB (Segel- und Bootsversand) | DE | Titan, Lofrans, Quick | svb-marine.de | Mittel |
| Compass24 | DE | Maggi, Quick, Lofrans | compass24.de | Mittel |
| Toplicht | DE | Diverse Hersteller | toplicht.de | Mittel |
| AWN | DE | Diverse Hersteller | awn.de | Mittel |
| Accastillage Diffusion | FR | Maggi, Quick, Lofrans | accastillage-diffusion.com | Mittel–Niedrig |
| Jimmy Green Marine | UK | Titan, Acco, Maggi | jimmygreen.co.uk | Mittel |
| Marine Superstore | UK | Diverse Hersteller | marinesuperstore.com | Mittel |
| Navimo | FR | Lofrans, Quick | navimo.com | Mittel |

### H.2 Nordamerika

| Händler | Land | Sortiment | Online-Shop | Preissegment |
|---|---|---|---|---|
| West Marine | USA | Acco, Titan, Maxwell | westmarine.com | Mittel–Hoch |
| Defender Industries | USA | Titan, Acco, diverse | defender.com | Mittel |
| Anchor Chain Shoppe | USA | Titan G43, Acco | anchorchain.com | Niedrig–Mittel |

---

## ANHANG I — Herstellervergleich Detailtabellen

### I.1 Vergleich 8 mm Kette — Alle Hersteller

| Hersteller | Grade | Norm | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Zink (µm) | Preis/m (EUR) | Zertifikate |
|---|---|---|---|---|---|---|---|---|
| Titan Marine | G43 | DIN 766 | 1071 | 29,4 | 1,40 | 70–100 | 5,00–6,50 | ISO, ABS |
| Acco/Peerless | G43 | BBB | 1088 | 27,2 | 1,28 | 80–120 | 7,00–9,00 | NACM |
| Maggi | G40 | DIN 766 | 890 | 24,5 | 1,40 | 70–100 | 6,00–7,80 | DIN |
| Lofrans | G40 | DIN 766 | 907 | 24,9 | 1,40 | 80–110 | 6,50–8,50 | ISO, CE |
| Quick | G40 | DIN 766 | 907 | 24,9 | 1,40 | 80–110 | 7,00–9,00 | ISO, CE |
| Maxwell | G40 | DIN 766 | 907 | 24,9 | 1,40 | 80–120 | 7,50–9,50 | ISO |
| Import/NoName | G30 | DIN 766 | 640 | 18,9 | 1,40 | 30–50 | 3,00–4,50 | Oft keine |

### I.2 Vergleich 10 mm Kette — Alle Hersteller

| Hersteller | Grade | Norm | WLL (kg) | Bruchlast (kN) | Gewicht (kg/m) | Zink (µm) | Preis/m (EUR) | Zertifikate |
|---|---|---|---|---|---|---|---|---|
| Titan Marine | G43 | DIN 766 | 1672 | 45,9 | 2,20 | 70–100 | 7,50–9,50 | ISO, ABS |
| Acco/Peerless | G43 | BBB | 1588 | 39,7 | 1,82 | 80–120 | 9,50–12,00 | NACM |
| Maggi | G40 | DIN 766 | 1390 | 38,3 | 2,20 | 70–100 | 8,50–11,00 | DIN |
| Lofrans | G40 | DIN 766 | 1418 | 38,9 | 2,20 | 80–110 | 9,50–12,50 | ISO, CE |
| Quick | G40 | DIN 766 | 1418 | 38,9 | 2,20 | 80–110 | 10,00–13,00 | ISO, CE |
| Maxwell | G40 | DIN 766 | 1418 | 38,9 | 2,20 | 80–120 | 11,00–14,00 | ISO |
| Import/NoName | G30 | DIN 766 | 999 | 29,4 | 2,20 | 30–50 | 4,50–6,50 | Oft keine |

---

## ANHANG J — Kettenauswahl-Algorithmus

### J.1 Entscheidungsmatrix

```
EINGABE:
  - Bootslänge (LOA)
  - Bootstyp (Segel/Motor/Kat)
  - Einsatzgebiet (Küste/Mittelmeer/Blauwasser/Tropen)
  - Max. Ankerwassertiefe
  - Budget
  - Gewichtssensitivität (normal/hoch/racing)
  - Vorhandene Winsch (ja/nein, Modell)

SCHRITT 1: Basisdurchmesser
  LOA ≤ 8m  → 6 mm
  LOA ≤ 12m → 8 mm
  LOA ≤ 16m → 10 mm
  LOA ≤ 22m → 12 mm
  LOA > 22m → 14+ mm

SCHRITT 2: Güteklasse
  Küste → G40
  Mittelmeer/Blauwasser/Tropen → G43
  Racing/Performance → G70 (mit Snubber Pflicht!)
  Superyacht (Klassifiziert) → Stegkette nach Klasse

SCHRITT 3: Material
  Standard → Feuerverzinkt
  Ästhetik/Budget hoch → AISI 316L (Durchmesser +2 mm!)
  Racing → Feuerverzinkt (leichter als Edelstahl)

SCHRITT 4: Länge
  Minimum = max_Tiefe × 4
  Standard = max_Tiefe × 5 + 20 m
  Blauwasser = max_Tiefe × 6 + 30 m

SCHRITT 5: Rode-Typ
  LOA ≤ 8m, Gewicht kritisch → Chain-Rope-Rode
  LOA ≤ 8m, keine Winsch → Chain-Rope-Rode
  LOA > 8m, Winsch vorhanden → All-Chain-Rode
  Racing → Chain-Rope-Rode (kurzer Kettenvorlauf)

SCHRITT 6: Winsch-Kompatibilität
  Winsch vorhanden → Kettennuss-Durchmesser und -Norm prüfen
  Winsch-Neukauf → Winsch auf Kettenwahl abstimmen

SCHRITT 7: Zubehör
  Ankerwirbel: WLL ≥ 1,5 × Ketten-WLL
  Snubber: Durchmesser = ca. 2× Kettendurchmesser
  Kettenstopper: WLL ≥ Ketten-WLL
  Kettenmarkierung: alle 10 m, Ende markieren

AUSGABE:
  - Empfohlene Kette (Durchmesser, Grade, Länge, Material)
  - Gewicht und Kosten
  - Zubehör-Liste
  - Warnungen (Trimm, Winsch-Kompatibilität)
  - Confidence: estimated
```

---

## ANHANG K — Prüfprotokolle

### K.1 Inspektionsprotokoll Ankerkette

```
┌───────────────────────────────────────────────────────┐
│         AYDI — Inspektionsprotokoll Ankerkette        │
├───────────────────────────────────────────────────────┤
│ Yacht: _____________ Typ: _____________ LOA: ____ m  │
│ Kette: ____ mm  Grade: ____  Länge: ____ m           │
│ Hersteller: ________________ Alter: ____ Jahre        │
│ Material: □ Feuerverzinkt  □ Edelstahl  □ Sonstig    │
│ Datum: _____________ Prüfer: _________________       │
├───────────────────────────────────────────────────────┤
│ 1. VISUELLE PRÜFUNG                                  │
│ Zinkverlust:     □ <25%  □ 25-50%  □ 50-75%  □ >75% │
│ Rost:            □ Kein  □ Punkt.  □ Fläch.  □ Stark │
│ Kinks:           □ Keine □ 1-2     □ 3-5     □ >5    │
│ Schweißnähte:    □ i.O.  □ Verdäch.□ Risse   □ Bruch │
│ Verformung:      □ Keine □ Leicht  □ Mittel  □ Stark │
│ Verdrallung:     □ Keine □ Leicht  □ Stark           │
├───────────────────────────────────────────────────────┤
│ 2. MESSUNG (3 Stellen: 10m, Mitte, Ende)             │
│ Durchmesser [mm]: St.1: ____ St.2: ____ St.3: ____  │
│ Nennmaß [mm]:     ____  Abweichung max.: ____%      │
│ Teilung 10 Glieder [mm]:                             │
│   St.1: ____ St.2: ____ St.3: ____                   │
│   Sollwert: ____ Abweichung max.: ____%              │
├───────────────────────────────────────────────────────┤
│ 3. ZUBEHÖR                                           │
│ Ankerwirbel:     □ Dreht frei  □ Schwergängig  □ Fest│
│ Schäkel:         □ Fest + gesichert  □ Lose  □ Fehlt │
│ Kettenstopper:   □ Funktioniert  □ Eingeschränkt     │
│ Markierungen:    □ Sichtbar  □ Verblasst  □ Fehlen   │
│ Kettenende:      □ Gesichert (Sollbruchstelle)       │
│                  □ Nicht gesichert (!)                │
├───────────────────────────────────────────────────────┤
│ 4. BEWERTUNG                                         │
│ Gesamtzustand:   □ Gut  □ Akzeptabel  □ Schlecht     │
│ Empfehlung:      □ Weiterverwendung                  │
│                  □ Neuverzinkung                      │
│                  □ Teilaustausch                      │
│                  □ Kompletttausch                     │
│ Nächste Prüfung: ____________                        │
│ Bemerkungen: ________________________________________│
│ ____________________________________________________│
└───────────────────────────────────────────────────────┘
```

---

## ANHANG L — Visuelle Analyse-Referenz

### L.1 Referenzbilder für AYDI-Bildanalyse (Claude Vision)

| Referenz-ID | Beschreibung | Erkennungsmerkmale | Confidence |
|---|---|---|---|
| VR-13.02-01 | Neue feuerverzinkte Kette, Idealzustand | Silbrig-glänzend, gleichmäßig, keine Verfärbung | visual_high |
| VR-13.02-02 | Kette mit 30% Zinkverlust, akzeptabel | Matt-grau, vereinzelt Weißrost, kein Rost | visual_high |
| VR-13.02-03 | Kette mit 70% Zinkverlust, nachlassend | Bräunlich, punktueller Rost, Zink erkennbar | visual_high |
| VR-13.02-04 | Kette mit 95% Zinkverlust, unzulässig | Flächig rostig, kein Zink mehr erkennbar | visual_high |
| VR-13.02-05 | Kette mit Kinking | Einzelne Glieder stehen quer | visual_high |
| VR-13.02-06 | Kette mit Schweißnaht-Riss | Riss an der Schweißstelle, Glied klafft | visual_medium |
| VR-13.02-07 | Edelstahlkette mit Spaltkorrosion | Braune Verfärbung an Gliedkontaktstellen | visual_low |
| VR-13.02-08 | Verschlissene Glieder (Abrieb) | Abgeflachte Querschnitte, blanke Stellen | visual_medium |
| VR-13.02-09 | Korrekte Kettenmarkierung | Farbige Glieder alle 10 m, Endemarkierung | visual_high |
| VR-13.02-10 | Snubber-Installation korrekt | Nylonleine mit Kettenhaken, durchhängende Kette | visual_high |
| VR-13.02-11 | Bugrolle mit Kette, Normalzustand | Kette läuft frei über Bugrolle, kein Verklemmen | visual_high |
| VR-13.02-12 | Kettenkasten geöffnet | Kette gestapelt, Drainage sichtbar, Zustand | visual_medium |

### L.2 Claude Vision Prompt-Hinweise

Für die visuelle Analyse von Ankerketten sollte der AYDI-Prompt folgende Aspekte abfragen:

1. **Gesamtbild:** Kettenmaterial (verzinkt/Edelstahl), Zustand der Oberfläche, Farbe
2. **Detailanalyse:** Zinkverlust (%), Rostbildung, Abrieb an Kontaktflächen
3. **Defekte:** Kinks, Verformungen, sichtbare Schweißnaht-Probleme
4. **Zubehör:** Wirbel, Schäkel, Kettenstopper — Zustand und korrekte Installation
5. **Markierungen:** Sichtbarkeit und Vollständigkeit der Kettenmarkierung
6. **Gesamtbewertung:** Einschätzung des Restnutzungszeitraums

---

## ANHANG M — Korrosionsschutz-Kompatibilität

### M.1 Materialkompatibilitätsmatrix

| Material 1 | Material 2 | Galv. Spannung (mV) | Risiko | Empfehlung |
|---|---|---|---|---|
| Verzinkter Stahl | Verzinkter Stahl | 0 | Kein | Ideal |
| Verzinkter Stahl | AISI 316 Edelstahl | –600 bis –800 | Hoch | Vermeiden oder Opferanode |
| Verzinkter Stahl | Bronze | –400 bis –600 | Mittel–Hoch | Vermeiden |
| Verzinkter Stahl | Aluminium | +200 bis +400 | Mittel (Alu opfert) | Akzeptabel mit Isolation |
| AISI 316 | AISI 316 | 0 | Kein | Ideal |
| AISI 316 | Bronze | –100 bis –200 | Niedrig | Akzeptabel |
| AISI 316 | Aluminium | +600 bis +800 | Hoch (Alu opfert stark) | Vermeiden |

### M.2 Opferanoden-Empfehlung für Ankergeschirr

| Situation | Anodentyp | Platzierung |
|---|---|---|
| Edelstahl-Wirbel auf verzinkter Kette | Zink-Scheibenade | Am Wirbel befestigt |
| Verzinkte Kette an Alu-Bug | Zink-Collar-Anode | An der Bugrolle |
| Edelstahlkette komplett | Keine Anode nötig | — |
| Verzinkte Kette komplett | Keine Anode nötig | — |

---

## ANHANG N — Retrofit-Leitfaden

### N.1 Kettenwechsel — Schritt für Schritt

1. **Planung:** Neue Kettengröße und -grade festlegen. Kompatibilität mit Kettennuss prüfen. Bei Größenwechsel: neue Kettennuss bestellen.
2. **Alte Kette entfernen:** Kette vollständig auf dem Steg auslegen. Kettenende im Kasten lösen. Kette Glied für Glied aus dem Kettenkasten ziehen.
3. **Kettenkasten reinigen:** Salzwasser, Schlamm, Rost entfernen. Drainage prüfen. Oberfläche reinigen und ggf. neu beschichten.
4. **Neue Kettennuss montieren** (falls Größenwechsel): Alte Kettennuss abziehen, neue aufsetzen. Sicherungsring prüfen.
5. **Neue Kette einziehen:** Kettenende im Kasten befestigen (Sollbruchstelle). Kette durch Kettennuss, Bugrolle führen. Markierungen anbringen.
6. **Zubehör montieren:** Ankerwirbel, Schäkel, Kettenstopper. Alle Bolzen sichern (Moustache Wire).
7. **Test:** Anker auslegen und einholen. Kettenlauf prüfen — jedes Glied muss sauber in die Kettennuss einrasten. Kettenstopper-Funktion prüfen.

### N.2 Typische Fehler beim Retrofit

| Fehler | Folge | Vermeidung |
|---|---|---|
| Falsche Kettengröße für Kettennuss | Kette springt unter Last | VOR dem Kauf Kettennuss-Maße prüfen |
| DIN 766 und BBB verwechselt | Kette passt nicht | Norm-Bezeichnung beim Kauf angeben |
| Unkalibrierte Kette gekauft | Kette springt, Verletzungsgefahr | Nur „kalibriert" oder „calibrated" kaufen |
| Kettenende nicht gesichert | Gesamte Kette geht über Bord | Sollbruchstelle einrichten |
| Schäkel nicht gesichert | Schäkel öffnet sich, Anker geht verloren | Moustache Wire oder Loctite |
| Kein Snubber installiert | Rucklasten auf Winsch und Bug | Snubber sofort mitbestellen |

---

## ANHANG O — Regatta- und Leichtbau-Lösungen

### O.1 Gewichtsoptimierte Ankerausrüstung

| Maßnahme | Gewichtseinsparung | Einschränkung |
|---|---|---|
| G70 statt G43 (gleiche Bruchlast, dünnere Kette) | 30–40% | Spröderes Bruchverhalten, Snubber Pflicht |
| Chain-Rope-Rode statt All-Chain | 50–70% | Weniger Abriebschutz, mehr Scope nötig |
| Kürzere Kette (30 m statt 60 m) | 50% | Geringerer Scope, nur Küstenfahrt |
| Aluminium-Anker statt Stahl | 30–50% | Teurer, empfindlicher |
| HMPE-Rode statt Nylon | 60–70% | Keine Ruckdämpfung, schwimmt |

### O.2 Regatta-Mindestausrüstung (ISAF/World Sailing)

Viele Regatten schreiben eine Mindest-Ankerausrüstung vor:

| Klasse | Ankergewicht | Rode-Länge | Rode-Typ |
|---|---|---|---|
| IRC/ORC <10m | 5 kg | 30 m | Kette + Tau oder All-Chain |
| IRC/ORC 10–15m | 8 kg | 40 m | Kette + Tau oder All-Chain |
| IRC/ORC >15m | 12 kg | 50 m | Kette + Tau oder All-Chain |

---

## ANHANG P — Superyacht-Sonderlösungen

### P.1 Stegkette für klassifizierte Superyachten

Superyachten ab ca. 24 m, die eine Klasse-Zertifizierung (Lloyd's, DNV, ABS, RINA) tragen, unterliegen der IACS UR A1 (Equipment Number) Berechnung. Das Equipment Number (EN) bestimmt die erforderliche Ankergröße und Kettendimension.

**Typische Stegketten-Dimensionen:**

| Yacht-LOA (m) | Equipment Number | Kettendurchmesser (mm) | Kettenlänge (m) | Kettengewicht (kg) |
|---|---|---|---|---|
| 24 | 120–180 | 16–19 | 150–200 | 800–1500 |
| 30 | 200–300 | 19–22 | 200–275 | 1500–3000 |
| 40 | 350–500 | 22–26 | 275–330 | 3000–5500 |
| 50 | 500–800 | 26–32 | 330–400 | 5500–10000 |

### P.2 Hydraulische Kettenwäsche

Superyachten über 25 m verfügen typischerweise über ein hydraulisches Kettenwäschsystem, das die Kette beim Einholen automatisch mit Seewasser oder Süßwasser spült. Das System reduziert die Schlamm- und Salzablagerung im Kettenkasten und verlängert die Lebensdauer der Kette.

---

## ANHANG Q — Umrechnungstabellen

### Q.1 Metrisch ↔ Zoll (Kette)

| Metrisch (mm) | Zoll (Näherung) | US-Bezeichnung |
|---|---|---|
| 6 | 1/4" | 1/4" |
| 7 | 9/32" | — (kein US-Standard) |
| 8 | 5/16" | 5/16" |
| 10 | 3/8" | 3/8" |
| 12 | 1/2" | 1/2" |
| 13 | 1/2" | 1/2" (UK) |
| 14 | 9/16" | 9/16" |
| 16 | 5/8" | 5/8" |

### Q.2 Kraft-Einheiten

| Von | Nach | Faktor |
|---|---|---|
| kN | kgf | × 101,97 |
| kgf | kN | × 0,00981 |
| kN | lbf | × 224,81 |
| lbf | kN | × 0,00445 |
| kN | daN | × 100 |

### Q.3 Windgeschwindigkeit

| Beaufort | Knoten | m/s | km/h | Bezeichnung |
|---|---|---|---|---|
| 3 | 7–10 | 3,4–5,4 | 12–19 | Schwache Brise |
| 4 | 11–16 | 5,5–7,9 | 20–28 | Mäßige Brise |
| 5 | 17–21 | 8,0–10,7 | 29–38 | Frische Brise |
| 6 | 22–27 | 10,8–13,8 | 39–49 | Starker Wind |
| 7 | 28–33 | 13,9–17,1 | 50–61 | Steifer Wind |
| 8 | 34–40 | 17,2–20,7 | 62–74 | Stürmischer Wind |
| 9 | 41–47 | 20,8–24,4 | 75–88 | Sturm |
| 10 | 48–55 | 24,5–28,4 | 89–102 | Schwerer Sturm |
| 11 | 56–63 | 28,5–32,6 | 103–117 | Orkanartiger Sturm |
| 12 | >64 | >32,7 | >118 | Orkan |

---

## ANHANG R — Checklisten

### R.1 Checkliste Ankerketten-Neukauf

- [ ] Bootslänge und Displacement ermittelt
- [ ] Einsatzgebiet definiert (Küste/Mittelmeer/Blauwasser)
- [ ] Max. Ankerwassertiefe bestimmt
- [ ] Kettendurchmesser festgelegt (mm)
- [ ] Güteklasse gewählt (G30/G40/G43/G70)
- [ ] Material gewählt (feuerverzinkt/Edelstahl)
- [ ] Norm geprüft (DIN 766/BBB) — muss zur Kettennuss passen
- [ ] Kettennuss-Kompatibilität mit Winsch-Hersteller bestätigt
- [ ] Kettenlänge berechnet (Scope-Methode)
- [ ] Rode-Typ gewählt (All-Chain/Chain-Rope)
- [ ] Ankerwirbel passend gewählt (WLL ≥ 1,5× Ketten-WLL)
- [ ] Verbindungsschäkel passend gewählt
- [ ] Kettenstopper passend gewählt
- [ ] Snubber/Bridle bestellt
- [ ] Kettenmarkierungs-Material vorhanden
- [ ] Kettenkasten-Volumen ausreichend
- [ ] Sollbruchstelle am Kettenende geplant
- [ ] Budget kalkuliert (Kette + Zubehör + Versand)

### R.2 Checkliste Ankermanöver (Kettenbezogen)

**Vor dem Ankern:**
- [ ] Kettenlänge für geplante Wassertiefe berechnet (Scope ≥ 5:1)
- [ ] Kettenstopper gelöst, Winsch bereit
- [ ] Bugrolle frei, Kette läuft frei
- [ ] Snubber bereitgelegt

**Beim Ankern:**
- [ ] Kette kontrolliert gefiert (nicht frei rauschen lassen)
- [ ] Kettenmarkierung beobachtet → gewünschte Länge ausgelegt
- [ ] Kettenstopper geschlossen
- [ ] Snubber aufgesetzt, Kette über Snubber leicht gefiert
- [ ] Rückwärtsgang → Kette straffen, Anker setzt

**Beim Lichten:**
- [ ] Snubber lösen und bergen
- [ ] Kettenstopper öffnen
- [ ] Kette einholen (Motor voraus, Winsch unterstützt)
- [ ] Kette mit Süßwasser spülen (falls Spülanlage vorhanden)
- [ ] Anker in Bugrolle sichern
- [ ] Kettenstopper schließen

### R.3 Checkliste Saisonende (Winterlager)

- [ ] Kette vollständig ausgelegt und visuell inspiziert
- [ ] Verschleißmessung (3 Stellen) durchgeführt und dokumentiert
- [ ] Kette gründlich mit Süßwasser gespült
- [ ] Kettenkasten gereinigt und getrocknet
- [ ] Kette im trockenen Zustand eingelagert (idealerweise außerhalb des Boots)
- [ ] Ankerwirbel geprüft, ggf. gefettet (Teflon-basiert, nicht Kupferpaste!)
- [ ] Schäkel-Sicherungen geprüft
- [ ] Kettenstopper gereinigt und gefettet
- [ ] Kettenmarkierungen erneuert (falls verblasst)
- [ ] Zustandsbericht erstellt (AYDI-Inspektionsprotokoll)
- [ ] Nächste Inspektion/Austausch terminiert

### R.4 Checkliste Sturmvorbereitung (Ankergeschirr)

- [ ] Maximalen Scope auslegen (≥7:1, idealerweise ≥10:1)
- [ ] Snubber/Bridle aufgesetzt (maximale Länge)
- [ ] Kettenstopper geschlossen und gesichert
- [ ] Zweitanker vorbereitet (ggf. ausbringen in 30–45° zum Erstanker)
- [ ] Ankerwache organisiert (Person + Fernglas + GPS-Ankeralarm)
- [ ] Motor startklar (falls Anker nicht hält → sofort Motor starten)
- [ ] Schleppleine bereit (falls Hilfe nötig)
- [ ] Kettenende-Sollbruchstelle bewusst — im Notfall Kette slipsen können

---

## ANHANG S — Erweiterte Dimensionierungsbeispiele

### S.1 Dimensionierungsbeispiel: 10 m Fahrtensegler, Ostsee

**Ausgangsdaten:**
- Yacht: 10,2 m LOA, 8.500 kg Verdrängung, Langkieler
- Einsatzgebiet: Ostsee (Küste, max. 20 m Wassertiefe)
- Winderwartung: max. 35 kn (Starkwind, Gewitterböen)
- Vorhandene Winsch: Lofrans Tigres 800 W, Kettennuss 8 mm DIN 766
- Budget: 500 EUR

**Berechnung:**

1. **Kettendurchmesser:** LOA 10,2 m → 8 mm (Standard für 8–12 m)
2. **Güteklasse:** Küstenfahrt → G40 ausreichend, G43 empfohlen für Reserve
3. **Kettenlänge:**
   - Max. Tiefe: 20 m
   - Standard-Scope: 5:1
   - Berechnung: 20 m × 5 + 20 m Reserve = 120 m → unrealistisch für Ostsee
   - Praxis-Anpassung: Max. Ankertiefe realistisch 12 m → 12 × 5 + 20 = 80 m
   - Empfehlung: 60 m (Budget) oder 80 m (optimal)
4. **Rode-Typ:** All-Chain (Winsch vorhanden)
5. **Gewicht:** 60 m × 1,40 kg/m = 84 kg | 80 m × 1,40 kg/m = 112 kg
6. **Kettenkasten-Volumen:** 84 × 1,8 × 1,2 = 181 Liter | 112 × 1,8 × 1,2 = 242 Liter
7. **Snubber:** 14 mm Nylon, 8 m
8. **Kosten 60 m × 8 mm G43:**
   - Kette: 60 × 6,00 = 360 EUR (Titan Marine)
   - Wirbel: 50 EUR
   - Schäkel: 20 EUR
   - Snubber: 45 EUR
   - Markierung: 15 EUR
   - **Gesamt: 490 EUR** → im Budget

**Ergebnis:**
```
Empfehlung: 8 mm G43, DIN 766, feuerverzinkt, 60–80 m
Hersteller: Titan Marine oder Maggi (Preis-Leistung)
Kettenkasten: min. 180 Liter (für 60 m)
Winsch: Lofrans Tigres 800 W → ausreichend für 8 mm × 80 m bis 15 m Tiefe
Snubber: 14 mm × 8 m Nylon 3-Schlag
Confidence: estimated
```

### S.2 Dimensionierungsbeispiel: 14 m Blauwasseryacht, Atlantik/Karibik

**Ausgangsdaten:**
- Yacht: 14,3 m LOA, 14.500 kg Verdrängung, Fahrtensegler (Ovni 435)
- Einsatzgebiet: Atlantik, Karibik, Azoren (Blauwasser)
- Winderwartung: max. 50 kn (Tropensturm-Ausläufer)
- Vorhandene Winsch: Quick Hector 1500 W, Kettennuss 10 mm DIN 766
- Budget: 1.500 EUR

**Berechnung:**

1. **Kettendurchmesser:** LOA 14,3 m → 10 mm (Standard für 12–16 m)
2. **Güteklasse:** Blauwasser → G43 (Pflicht)
3. **Kettenlänge:**
   - Max. Tiefe: 25 m (Karibik, tiefe Buchten)
   - Blauwasser-Scope: 6:1
   - Berechnung: 25 × 6 + 30 = 180 m → reduziert auf praxistaugliche 120 m
   - Empfehlung: 100 m (Minimum), 120 m (optimal)
4. **Rode-Typ:** All-Chain
5. **Zweitkette (Heckanker):** 8 mm G43, 30 m Kette + 50 m × 14 mm Nylon
6. **Gewicht Primärkette:** 100 m × 2,20 kg/m = 220 kg | 120 m = 264 kg
7. **Kettenkasten-Volumen:** 220 × 1,8 × 1,2 = 475 Liter (Hauptkette 100 m)
8. **Snubber:** 18 mm Nylon, 10 m (oder 2 × 14 mm als Bridle)
9. **Kosten 100 m × 10 mm G43:**
   - Kette: 100 × 8,50 = 850 EUR (Titan Marine)
   - Wirbel (Kugellager): 120 EUR
   - Schäkel: 30 EUR
   - Snubber: 65 EUR
   - Kettenhaken (2×): 40 EUR
   - Markierung: 20 EUR
   - Zweitkette (30 m × 8 mm): 180 EUR
   - Zweitanker-Nylon (50 m × 14 mm): 95 EUR
   - **Gesamt: 1.400 EUR** → im Budget

**Ergebnis:**
```
Primärkette: 10 mm G43, DIN 766, feuerverzinkt, 100–120 m
Zweitkette: 8 mm G43, 30 m + 50 m Nylon 14 mm
Hersteller: Titan Marine G43 (bestes Preis-Leistungs-Verhältnis für Blauwasser)
Kettenkasten: min. 475 Liter (für 100 m × 10 mm)
Winsch: Quick Hector 1500 W → ausreichend für 10 mm × 120 m bis 20 m Tiefe
Snubber: 18 mm × 10 m Nylon 3-Schlag oder Bridle 2 × 14 mm × 8 m
Tropenrevier-Hinweis: Neuverzinkung alle 5–7 Jahre einplanen
Confidence: estimated
```

### S.3 Dimensionierungsbeispiel: 8 m Trailer-Segelboot, Mittelmeer

**Ausgangsdaten:**
- Yacht: 7,8 m LOA, 2.800 kg Verdrängung, Jollenkreuzer
- Einsatzgebiet: Mittelmeer (Kroatien, Griechenland), Trailer-Transport
- Winderwartung: max. 25 kn (ankert nur bei gutem Wetter)
- Keine Winsch vorhanden
- Budget: 250 EUR

**Berechnung:**

1. **Kettendurchmesser:** LOA 7,8 m → 6 mm
2. **Güteklasse:** Küste/Mittelmeer → G40 oder G43
3. **Rode-Typ:** Chain-Rope (keine Winsch, Gewicht kritisch bei Trailer-Boot)
4. **Kettenvorlauf:** 8 m × 6 mm G40
5. **Tau:** 40 m × 12 mm Nylon 3-Schlag
6. **Gesamtgewicht:** 8 × 0,79 = 6,3 kg (Kette) + 40 × 0,079 = 3,2 kg (Tau) = 9,5 kg
7. **Vergleich All-Chain:** 40 m × 0,79 = 31,6 kg → 3× schwerer
8. **Kosten:**
   - Kette (8 m × 6 mm): 8 × 5,00 = 40 EUR
   - Nylon (40 m × 12 mm): 75 EUR
   - Wirbel: 30 EUR
   - Chain-to-Rope-Splice (selbst gemacht): 0 EUR
   - Kausch + Schäkel: 15 EUR
   - **Gesamt: 160 EUR** → unter Budget

**Ergebnis:**
```
Rode: Chain-Rope (8 m × 6 mm G40 + 40 m × 12 mm Nylon)
Gesamtgewicht: 9,5 kg (vs. 31,6 kg All-Chain)
Hersteller: Maggi oder Lofrans (6 mm verfügbar)
Kein Kettenstopper nötig (Belegen an Klampe)
Kein elektronischer Kettenzähler nötig (Markierung am Tau reicht)
Confidence: estimated
```

### S.4 Dimensionierungsbeispiel: 20 m Motoryacht, Mittelmeer

**Ausgangsdaten:**
- Yacht: 19,5 m LOA, 35.000 kg Verdrängung, Flybridge-Motoryacht
- Einsatzgebiet: Westliches Mittelmeer (Sardinien, Balearen, Côte d'Azur)
- Winderwartung: max. 40 kn (Mistral, Tramontana)
- Vorhandene Winsch: Muir VR3500 (3500 W, hydraulisch), Kettennuss 12 mm DIN 766
- Budget: 3.000 EUR

**Berechnung:**

1. **Kettendurchmesser:** LOA 19,5 m → 12 mm
2. **Güteklasse:** G43 (Pflicht bei dieser Bootsgröße)
3. **Kettenlänge:**
   - Max. Tiefe: 20 m (Mittelmeer, Buchten)
   - Standard-Scope: 5:1
   - Berechnung: 20 × 5 + 30 = 130 m
   - Empfehlung: 120 m (mit Preisgrenze)
4. **Rode-Typ:** All-Chain
5. **Gewicht:** 120 m × 3,10 kg/m = 372 kg
6. **Kettenkasten-Volumen:** 372 × 1,8 × 1,2 = 803 Liter
7. **Snubber:** 22 mm Nylon, 12 m (oder Bridle 2 × 18 mm × 10 m)
8. **Kosten 120 m × 12 mm G43:**
   - Kette: 120 × 13,00 = 1.560 EUR (Titan Marine)
   - Wirbel (Kugellager, groß): 180 EUR
   - Schäkel (16 mm): 40 EUR
   - Snubber (22 mm × 12 m): 120 EUR
   - Kettenstopper (Wippen): 250 EUR
   - Kettenzähler (elektronisch): 350 EUR
   - Markierung (professionell): 30 EUR
   - **Gesamt: 2.530 EUR** → im Budget

**Ergebnis:**
```
Primärkette: 12 mm G43, DIN 766, feuerverzinkt, 120 m
Hersteller: Titan Marine G43 oder Quick (OEM-Kompatibilität mit Muir)
Kettenkasten: min. 800 Liter — Selbststapler-Design empfohlen
Winsch: Muir VR3500 (hydraulisch) → komfortabel für 12 mm × 120 m
Kettenwäsche: automatisch (Seewasser) beim Einholen
Snubber: 22 mm × 12 m oder Bridle 2 × 18 mm × 10 m
Kettenzähler: Quick CHC-1100 oder Lofrans Kettenzähler
Trimmhinweis: 372 kg im Bug — Ballasttank achtern füllen beim Ankern
Confidence: estimated
```

---

## ANHANG T — Revierabhängige Empfehlungen

### T.1 Reviermatrix

| Revier | Besonderheiten | Kettenempfehlung | Zusatzmaßnahmen |
|---|---|---|---|
| Ostsee | Flach (5–15 m), Sand/Schlick, mild | 8 mm G40, 50–60 m | Standard-Ausrüstung |
| Nordsee/Wattenmeer | Gezeiten (5–8 m Hub), Sand, starke Strömung | 8 mm G43, 60–80 m | Scope für Tidenhub berechnen! |
| Mittelmeer West | 5–25 m, Sand/Fels/Seegras, Mistral-Böen | 8–10 mm G43, 80–100 m | Posidonia-Anker-Verbot beachten |
| Mittelmeer Ost | 5–30 m, Sand/Fels/Ton, Meltemi | 10 mm G43, 80–100 m | Ruhige Buchten können bei Meltemi unruhig werden |
| Karibik | 5–15 m, Sand/Koralle, Tropen | 10 mm G43, 100 m | Kettenvorlauf ≥20 m, Neuverzinkung alle 5 Jahre |
| Pazifik (Südsee) | 5–30 m, Koralle/Sand, Tropen, Zyklone | 10 mm G43, 100–120 m | Korallenvorsorge, Zweitanker Pflicht |
| Skandinavien | 5–40 m (!), Fels/Granit, kalt | 8–10 mm G43, 80–100 m | Tiefen >20 m → mehr Scope oder Kellet |
| Atlantik-Inseln (Azoren, Kanaren) | 10–30 m, Vulkansand/Fels, Dünung | 10 mm G43, 100–120 m | Dünung = hohe dynamische Lasten → starker Snubber |
| Rotes Meer | 5–20 m, Koralle/Sand, heiß, salzig | 10 mm G43, 100 m | Beschleunigter Zinkverlust, häufige Inspektion |
| Südostasien | 5–20 m, Schlick/Sand/Koralle, Tropen | 8–10 mm G43, 80–100 m | Monsun-Saison: Sturmankersystem vorbereiten |

### T.2 Tidenhub und Scope-Berechnung

In Gezeitenrevieren muss der Scope für die maximal mögliche Wassertiefe berechnet werden:

**Formel:**
```
Effektive Tiefe = Kartentiefe + Tidenhub + Freibord

Beispiel Nordsee (Ärmelkanal):
- Kartentiefe: 5 m
- Tidenhub: 6 m (Spring-Gezeiten)
- Freibord: 1,5 m
- Effektive Tiefe bei Hochwasser: 5 + 6 + 1,5 = 12,5 m
- Scope 5:1: 12,5 × 5 = 62,5 m Kette
- Scope 7:1 (Sturm): 12,5 × 7 = 87,5 m Kette
```

> **AYDI-Warnung:** Bei Ankern im Gezeitenrevier immer den VOLLEN Tidenhub berücksichtigen! Ein Scope, der bei Niedrigwasser komfortabel erscheint, kann bei Hochwasser völlig unzureichend sein. Besonders gefährlich: Ankern bei Niedrigwasser, Einschlafen, Aufwachen bei Hochwasser mit zu kurzem Scope.

### T.3 Seegras-Reviere (Posidonia-Schutz)

In vielen Mittelmeer-Regionen (Balearen, Sardinien, Korsika, Griechenland) ist das Ankern über Posidonia-Seegraswiesen eingeschränkt oder verboten. Die Ankerkette pflügt durch das Seegras und zerstört das geschützte Ökosystem.

**Alternativen:**
- Festmacher-Bojen (Bojenfelder) nutzen
- Nur auf Sand-Patches ankern
- Kette so kurz wie sicher möglich halten (weniger Kettenpflügen)
- Reef-Anker mit kurzer Kette + langem Tau (weniger Bodenkontakt des Rode)

> **AYDI-Hinweis:** Bußgelder für Ankern in Posidonia-Schutzgebieten können 600–3.000 EUR betragen (Balearen). AYDI sollte bei der Revier-Eingabe „Mittelmeer" einen Hinweis auf Posidonia-Ankerverbote geben.

---

## ANHANG U — Kettenpflege und Lebensdauer-Optimierung

### U.1 Regelmäßige Pflege

| Pflegemaßnahme | Frequenz | Zeitaufwand | Kosten | Lebensdauer-Effekt |
|---|---|---|---|---|
| Süßwasserspülung nach Ankern | Jedes Mal | 5–10 Min | 0 EUR (Bordwasser) | +30–50% Verzinkungsdauer |
| Trocknung vor Einlagerung | Nach jeder Fahrt | 15 Min | 0 EUR | +20% (v.a. Edelstahl) |
| Kette in Essig-Lösung einlegen (1:10) | 1×/Jahr | 2 Std. + Einwirkzeit | 5 EUR | Entfernt Kalkbelag |
| Kettenkasten-Reinigung | 2×/Jahr | 30 Min | 0 EUR | Reduziert Korrosion |
| Leichtes Einfetten (Ballistol, LPS 3) | Vor Winterlager | 30 Min | 10 EUR | +10% Korrosionsschutz |
| Professionelle Zinkschicht-Messung | 1×/Jahr | 15 Min | 30–50 EUR (Fachbetrieb) | Frühzeitige Erkennung |
| Neuverzinkung | Alle 5–15 Jahre | 1 Woche (Fachbetrieb) | 3–5 EUR/m | Verlängert Lebensdauer um 5–10 Jahre |

### U.2 Fehler, die die Lebensdauer verkürzen

| Fehler | Lebensdauer-Reduktion | Vermeidung |
|---|---|---|
| Nie mit Süßwasser spülen | –40–60% | Spülanlage oder Eimer |
| Kette dauerhaft nass im Kasten | –20–30% | Drainage, Trocknung |
| Mischmetalle ohne Opferanode | –30–50% (lokaler Zinkverlust) | Gleiche Materialien oder Anode |
| Kette über scharfe Kanten ziehen | –10–20% (lokaler Abrieb) | Bugrolle/Kettenführung prüfen |
| Kette nicht drehen (End-for-End) | –15–25% (ungleichmäßiger Verschleiß) | Alle 3–5 Jahre drehen |
| Überlastung (zu wenig Scope bei Sturm) | –5–30% (plastische Dehnung) | Scope ≥5:1, bei Sturm ≥7:1 |
| Kette in Chlorwasser (Pool) reinigen | –10% (Chlorid-Angriff auf Zink) | Nur Süßwasser oder milde Essig-Lösung |

### U.3 Lebensdauer-Erwartung nach Revier und Pflege

| Revier | Pflege gut | Pflege mittel | Pflege schlecht |
|---|---|---|---|
| Binnengewässer (Süßwasser) | 25–30 Jahre | 20–25 Jahre | 15–20 Jahre |
| Ostsee (niedrig salin) | 20–25 Jahre | 15–20 Jahre | 10–15 Jahre |
| Nordsee/Atlantik (gemäßigt) | 15–20 Jahre | 10–15 Jahre | 7–10 Jahre |
| Mittelmeer (warm, salin) | 12–18 Jahre | 8–12 Jahre | 5–8 Jahre |
| Tropen (heiß, salin) | 8–12 Jahre | 5–8 Jahre | 3–5 Jahre |
| Rotes Meer (extrem salin, heiß) | 6–10 Jahre | 4–6 Jahre | 2–4 Jahre |

### U.4 Neuverzinkung — Ablauf und Kosten

**Voraussetzungen für Neuverzinkung:**
1. Kette mechanisch intakt (kein Verschleiß >10%, keine Dehnung >3%, keine Kinks)
2. Keine Schweißnaht-Risse
3. Durchmesser noch innerhalb der Toleranz

**Ablauf:**
1. Kette zum Feuerverzinkungsbetrieb transportieren (Gewicht beachten!)
2. Beize: Kette wird in Salzsäurebad entrostet
3. Fluxen: Fluxmittel verhindert Oxidation vor dem Verzinken
4. Feuerverzinken: Kette wird in 450°C heißes Zinkbad getaucht
5. Abkühlung und Kontrolle
6. Rücktransport

**Kosten (Richtwerte 2025):**

| Kettengewicht | Entrosten + Verzinken | Gesamtkosten (inkl. Transport) |
|---|---|---|
| 50 kg (z.B. 60 m × 6 mm) | 150–250 EUR | 200–350 EUR |
| 80 kg (z.B. 60 m × 8 mm) | 200–350 EUR | 280–450 EUR |
| 150 kg (z.B. 80 m × 10 mm) | 350–550 EUR | 450–700 EUR |
| 250 kg (z.B. 80 m × 12 mm) | 500–800 EUR | 650–1000 EUR |

> **AYDI-Wirtschaftlichkeitsrechnung:** Neuverzinkung lohnt sich, wenn die Kosten <50% einer neuen Kette betragen UND die Kette mechanisch einwandfrei ist. Für eine 80 m × 8 mm Kette: Neuverzinkung ca. 400 EUR vs. Neukauf ca. 600 EUR → Neuverzinkung lohnt sich. Für eine 80 m × 12 mm Kette: Neuverzinkung ca. 750 EUR vs. Neukauf ca. 1.200 EUR → klare Ersparnis.

---

## ANHANG V — Spezielle Ankerszenarien

### V.1 Ankern in Korallenrevieren

**Probleme:**
- Korallen zerstören Nylontau (Durchscheuern in Stunden/Tagen)
- Korallenbommies können Kette verklemmen
- Anker verhakt sich in Korallenformationen
- Umweltschaden durch Kettenpflügen über Korallen

**Empfehlungen:**
- All-Chain-Rode (kein Tau am Grund)
- Kettenvorlauf bei Chain-Rope-Rode: ≥20 m
- Chafe Guard über den Tau-Abschnitt am Grund
- Ankerboje (Trip Line) zum Rückwärts-Bergen des Ankers
- Sand-Patches zum Ankern suchen (Schnorchelnd prüfen!)
- Kellet verwenden, um Kette näher am Grund zu halten

### V.2 Ankern bei extremen Bedingungen

**Sturmankern (>40 kn):**
- Scope ≥7:1 (idealerweise ≥10:1)
- Snubber/Bridle aufgesetzt
- Kettenstopper geschlossen und gesichert
- Zweitanker vorbereitet (30–45° zum Erstanker)
- Motor warmgehalten (sofortiges Anlassen möglich)
- GPS-Ankeralarm auf enge Toleranz gestellt
- Ankerwache (durchgehend)

**Ankern bei starker Strömung (>2 kn):**
- Scope leicht erhöhen (Strömung addiert sich zur Windlast)
- Kette kann durch Strömung „schweben" (reduzierter Kettenary)
- Kellet besonders wirksam (drückt Kette trotz Strömung auf den Grund)
- Bei Tidenstrom: Kette lang genug für alle Strömungsrichtungen

**Ankern auf Felsengrund:**
- Anker findet schwer Halt
- Kette scheuert an Felsen (beschleunigter Verschleiß)
- Chafe Guard am Kettenende (erste 5 m) erwägen
- Kurzer Scope (3:1) kann besser sein (weniger Kettenbewegung am Grund)
- Ankerboje zur Sicherheit (Rückwärts-Bergen, falls Anker klemmt)

**Ankern auf Schlickgrund:**
- Anker sinkt tief ein (guter Halt, aber schwer zu bergen)
- Kette versinkt im Schlick (erhöht effektives Kettengewicht beim Bergen)
- Winsch muss erhöhte Zuglast aufbringen
- Kette nach dem Bergen gründlich spülen (Schlick zerstört Verzinkung langfristig)

### V.3 Zweitanker-Setzen (Bahamian Moor, Fore-and-Aft)

**Bahamian Moor (2 Anker, Bug-Heck):**
- Erstanker normal setzen
- Boot rückwärts fahren, Zweitanker vom Heck ausbringen
- Ketten/Roden so einstellen, dass das Boot über beiden Ankern steht
- Vorteil: minimaler Schwojkreis (in engen Buchten/Häfen)
- Nachteil: Verdrallung der Ketten bei Windwechsel

**V-Anker (2 Anker vom Bug, 30–60°):**
- Erstanker normal setzen
- Boot seitlich versetzen, Zweitanker in 30–60° zum Erstanker setzen
- Beide Ketten am Bug belegen
- Vorteil: doppelte Haltekraft, reduziertes Schwojen
- Nachteil: Kettenverdrallungsgefahr, aufwändiges Bergen

**Tandem-Anker (2 Anker hintereinander auf einer Kette):**
- Zweitanker wird 5–10 m vor dem Erstanker auf der gleichen Kette gesetzt
- Erhöht die Haltekraft um 50–100%
- Einfach zu setzen und zu bergen
- Funktioniert nur mit gleicher Kettengröße für beide Anker

---

## ANHANG W — Kettenbedingte Schwachpunkte in der Yachtkonstruktion

### W.1 Konstruktive Schwachstellen

| Schwachstelle | Beschreibung | AYDI-Prüfpunkt |
|---|---|---|
| Bugrolle-Befestigung | Bugrolle-Schrauben in GFK ohne Backing Plate | Backing Plate vorhanden? Material? Dimensionierung? |
| Kettenstopper-Unterbau | Kettenstopper direkt auf Deck ohne Verstärkung | Lokale Verstärkung unter dem Kettenstopper? |
| Kettenkasten-Struktur | Kettenkasten aus dünnem GFK, ohne Verstärkung | Wandstärke, Verstärkungen, max. Lastaufnahme |
| Hawse-Pipe (Kettenrohr) | Scharfe Kanten am Kettenrohr → Kettenverschleiß | Abgerundete Kanten? Material? Verschleiß sichtbar? |
| Drainage-System | Verstopfte oder fehlende Drainage → Wasseransammlung | Ablauf offen? Rückschlagventil vorhanden? |
| Deck-Verstärkung Bug | Ankerlasten werden über Deck in Rumpf eingeleitet | Faserverlauf im Laminat? Kernmaterial im Lastpfad? |
| Ankerkasten-Verschluss | Undichter Deckel → Wasser dringt bei Seegang ein | Dichtung vorhanden? Verschluss sturmsicher? |

### W.2 Gewichtsverteilung und Trimm

Die Ankerkette hat erheblichen Einfluss auf die Gewichtsverteilung der Yacht:

**Trimmberechnung (vereinfacht):**
```
Trimm-Änderung (°) ≈ (Kettengewicht × Hebelarm) / (Verdrängung × GML)

Beispiel: 12 m Yacht, 8.500 kg Verdrängung
- 80 m × 8 mm Kette = 112 kg
- Hebelarm Kettenkasten-Schwerpunkt zu LCG ≈ 4,5 m (vorlich)
- GML (Längs-Metazentrum) ≈ 12 m (typisch für 12 m Segler)
- Trimm-Änderung ≈ (112 × 4,5) / (8.500 × 12) ≈ 0,005 rad ≈ 0,3°

→ 0,3° Bug-lastiger mit voller Kette. Effekt: reduzierte Höchstgeschwindigkeit,
  erhöhte Gierbewegung im Seegang, veränderte Ruderwirkung.
```

**Vergleich: Kette voll vs. Kette leer (100 m × 10 mm auf 14 m Yacht):**

| Parameter | Kette voll (220 kg Bug) | Kette leer (0 kg Bug) |
|---|---|---|
| Trimm (Bug-lastiger) | +0,5° | 0° (Referenz) |
| Höchstgeschwindigkeit | –0,2 kn | Referenz |
| Stampfperiode | Kürzer (Bug taucht schneller) | Länger (komfortabler) |
| Gierbewegung | Erhöht | Referenz |
| Ruderdruck | Leicht erhöht | Referenz |

> **AYDI-Konstruktionshinweis:** Bei der Yachtkonstruktion sollte der Trimm für beide Zustände (Kette voll, Kette leer) berechnet werden. Die Differenz kann 0,3–0,8° betragen — bei Performance-Yachten ein signifikanter Faktor. Mögliche Gegenmaßnahmen: achterne Ballasttanks, Kettenkasten möglichst weit achtern und tief positionieren.

### W.3 Kettenkastendesign — Best Practices

**Formgebung:**
- Konischer Boden (trichterförmig): Kette stapelt sich selbst, Schwerpunkt tief und zentral
- Wandneigung: min. 15° zur Vertikalen → Kette rutscht nach unten
- Ecken vermeiden: Kette verklemmt sich in scharfen Ecken
- Kettenrohr-Austritt: mittig oben, Durchmesser ≥3× Kettendurchmesser

**Drainage:**
- Ablauföffnung am tiefsten Punkt, Durchmesser ≥25 mm (bei 8 mm Kette)
- Siphon oder Rückschlagventil (verhindert Rückstau aus der Bilge)
- Überlaufschutz: bei verstopfter Drainage darf Wasser nicht über Kastenkante treten
- Lenzpumpen-Anschluss für große Kettenkasten (>300 Liter)

**Belüftung:**
- Mindestens eine Ventilationsöffnung (verhindert Kondenswasser)
- Gitterabdeckung (verhindert Herausfallen kleiner Gegenstände)
- Bei geschlossenen Kettenkasten: Lüftungsrohr nach Deck

**Zugang:**
- Inspektionsluke: min. 300 × 300 mm (Hand + Messwerkzeug muss reinpassen)
- Kettenendbefestigung muss zugänglich sein (Sollbruchstelle austauschen)
- Reinigung: Gesamtvolumen muss mit Schlauch/Bürste erreichbar sein

**Material:**
- GFK: min. 4 mm Wandstärke, Verstärkung am Kettenrohr-Austritt
- Aluminium: 3 mm min., eloxiert oder beschichtet (Kontakt mit verzinkter Kette → galvanisch!)
- Edelstahl: ideal für Kettenrohr-Einsatz, teuer für Gesamtkasten
- Sperrholz (beschichtet): Budget-Lösung für ältere Boote, regelmäßig auf Feuchteschäden prüfen

### W.4 Dynamische Lasten auf die Bugstruktur

Die Ankerkette überträgt erhebliche dynamische Lasten auf die Bugstruktur:

| Last-Szenario | Typische Kraft (12 m Yacht) | Lastpfad |
|---|---|---|
| Ruhig ankern (10 kn Wind) | 0,5–1,0 kN | Kette → Kettennuss → Winsch-Bolzen → Deck → Rumpf |
| Mäßiger Wind (20 kn) | 2,0–4,0 kN | Kette → Kettenstopper → Stopperbolzen → Deck → Rumpf |
| Starkwind (30 kn) | 5,0–10,0 kN | Kette → Kettenstopper → Deck → Schotten → Rumpf |
| Sturm (40 kn + Rucklast) | 15,0–35,0 kN | Kette → Snubber → Klampen → Deck → Schotten → Rumpf |
| Extremlast (Kettenbruch-Grenze) | 30,0–70,0 kN | Gesamte Bugstruktur |

**Konstruktive Anforderungen:**
- Kettenstopper: min. 3× Ketten-WLL als Bolzenbruchlast
- Deck unter Kettenstopper: lokale Verstärkung (Sperrholz-Kern, GFK-Aufdickung)
- Backing Plate: Edelstahl, min. Fläche 100 cm² für 10 mm Kette
- Bugrolle: Bolzen min. M12 (für 10 mm Kette), Backing Plate Pflicht
- Ankerwinden-Befestigung: 4× M12 Bolzen mit Backing Plate (für 1000 W Winsch)

---

## ANHANG X — Kettenzähler und Elektronik

### X.1 Elektronische Kettenzähler

Elektronische Kettenzähler (Chain Counters) messen die ausgelegte Kettenlänge über einen Sensor an der Kettennuss oder am Kettenrohr. Sie zeigen die aktuelle Kettenlänge auf einem Display im Cockpit oder am Steuerpult an.

**Funktionsprinzip:**
Der Sensor (Hall-Effekt, Reed-Kontakt oder optisch) erkennt jedes Kettenglied, das die Kettennuss passiert. Über die bekannte Teilung (z. B. 24 mm bei 8 mm Kette) wird die Länge berechnet. Aufwärts-/Abwärts-Zählung unterscheidet Auslegen und Einholen.

**Marktübersicht:**

| Hersteller | Modell | Display | Sensor-Typ | Preis (EUR) | Besonderheit |
|---|---|---|---|---|---|
| Quick | CHC-1100 | LCD, beleuchtet | Hall-Effekt | 280–350 | Integriert in Quick-Winschen |
| Lofrans | Chain Counter | LCD, wasserdicht | Reed-Kontakt | 250–320 | Nachrüstbar, DIN-766-kompatibel |
| Maxwell | AA560 | LED, groß | Hall-Effekt | 300–400 | Standalone, universell |
| Muir | DFF-1 | OLED, Multifunktion | Optisch | 350–450 | Zeigt auch Zugkraft an |
| MZ Electronic | EV030 | LCD, kompakt | Reed-Kontakt | 180–250 | Budget-Lösung, universell |
| Lewmar | Chain Counter | LCD | Hall-Effekt | 280–380 | Für Lewmar-Winschen optimiert |

**Installation:**
1. Sensor an der Kettennuss oder am Kettenrohr montieren
2. Display im Cockpit oder am Steuerstand installieren
3. Kalibrierung: 10 Glieder auslegen, Anzeige auf 10× Teilung einstellen
4. Nullpunkt setzen: Kette vollständig eingeholt = 0 m
5. Alarmgrenzen programmieren: z. B. Alarm bei 90% der Gesamtlänge

**Typische Alarmfunktionen:**
- Kettenlänge-Warnung (z. B. bei 80% und 95% der Gesamtlänge)
- Geschwindigkeitswarnung (Kette fiert zu schnell → unkontrolliertes Ausrauschen)
- Zugkraft-Alarm (bei Modellen mit Lastmessung)
- Kettenkasten-Füllstandswarnung (bei Modellen mit Füllstandssensor)

### X.2 Ankerwachen-Systeme und GPS-Ankeralarm

Moderne Navigationsgeräte und Apps bieten GPS-basierte Ankeralarme:

| System | Typ | Preis | Funktionen |
|---|---|---|---|
| Garmin/B&G/Raymarine Plotter | Hardware | Im Plotter integriert | Ankerkreis, Alarm bei Überschreitung |
| Anchor Watch App (iOS/Android) | Software | Kostenlos–20 EUR | GPS-Tracking, Push-Benachrichtigung |
| DragAlarm | Standalone-Gerät | 150–250 EUR | Unabhängig von Bordnetz, Langzeit-Batterie |
| Boat Beacon | App | Kostenlos | AIS-basiert, Community-Warnung |

> **AYDI-Praxishinweis:** Ein GPS-Ankeralarm ersetzt NICHT die Ankerwache bei Starkwind. GPS-Genauigkeit beträgt 3–5 m — ein Treiben um wenige Meter wird erst mit Verzögerung erkannt. Bei kritischen Bedingungen (>30 kn, enger Raum, Lee-Küste) ist eine visuelle Ankerwache mit Peilung auf feste Objekte unverzichtbar.

### X.3 Lastmessung (Anchor Load Monitoring)

Einige moderne Systeme messen die tatsächliche Zuglast an der Ankerkette in Echtzeit:

| System | Messprinzip | Messbereich | Preis (EUR) | Genauigkeit |
|---|---|---|---|---|
| Mantus Marine Load Monitor | Dehnungsmessstreifen | 0–50 kN | 400–600 | ±5% |
| Dyneema Link Load Cell | Inline-Messzelle | 0–100 kN | 800–1.200 | ±2% |
| Strain Gauge am Kettenstopper | DMS am Stopper | 0–30 kN | 300–500 (Eigenbau) | ±10% |

**Nutzen:**
- Objektive Messung der Ankerlast (keine Schätzung mehr)
- Frühwarnung bei steigender Last (auffrischender Wind, Strömung)
- Dokumentation für AYDI-Analyse (Lasthistorie)
- Nachweis der Ketten-Belastung für Verschleißprognose
- Alarmmöglichkeit bei Überschreitung kritischer Lasten

---

## ANHANG Y — Umwelt- und Entsorgungsaspekte

### Y.1 Umweltauswirkungen von Ankerketten

| Aspekt | Auswirkung | Minderung |
|---|---|---|
| Zinkauslaugung (verzinkte Kette) | Zink ist aquatisch toxisch in hoher Konzentration | Minimaler Effekt bei normalem Gebrauch |
| Seegras-/Korallenzcerstörung | Kettenpflügen zerstört Seegras und Korallen | Auf Sand ankern, Bojenfelder nutzen |
| Kettenklirren (Unterwasserlärm) | Stört marine Fauna | Snubber reduziert Vibrationen |
| Rostpartikel im Wasser | Optisch unschön, ökologisch unbedenklich | Regelmäßige Wartung |
| Ankerkettenreste am Meeresgrund | „Geisterankern" — verlorene Kettenabschnitte | Kettenende sichern, Markierungen prüfen |

### Y.2 Entsorgung von Altketten

Ankerketten bestehen aus Stahl und sind vollständig recyclebar:

| Material | Entsorgung | Erlös (ca.) |
|---|---|---|
| Verzinkte Stahlkette | Schrotthandel (Stahlschrott) | 0,10–0,20 EUR/kg |
| Edelstahlkette | Schrotthandel (Edelstahlschrott, getrennt!) | 1,00–2,00 EUR/kg |
| Nylon-Ankertau | Hausmüll (Restmüll) oder Wertstoffhof | 0 EUR |

> **AYDI-Hinweis:** Eine 80 m × 10 mm verzinkte Altkette (176 kg) bringt beim Schrotthandel ca. 18–35 EUR. Eine 80 m × 10 mm Edelstahlkette (176 kg) bringt ca. 175–350 EUR. Bei Edelstahl lohnt die separate Entsorgung!

---

## ANHANG Z — Weiterführende Literatur und Ressourcen

### Z.1 Fachbücher

| Titel | Autor | Verlag | Jahr | Relevanz |
|---|---|---|---|---|
| The Complete Anchoring Handbook | Poiraud & Ginsberg-Klemmt | Ragged Mountain Press | 2008 | Umfassend, praxisorientiert |
| Anchoring — A Ground Tackler's Apprentice | Lowe | McGraw-Hill | 2015 | Detailliert, USA-orientiert |
| Seem Handbuch Ankern | Fritze | Delius Klasing | 2019 | Deutsch, praxisnah |
| Nigel Calder's Boatowner's Mechanical and Electrical Manual | Calder | McGraw-Hill | 2015 | Kapitel Ankerausrüstung |
| Yachtdesign und Yachtbau | Larsson, Eliasson | Delius Klasing | 2020 | Konstruktive Aspekte |

### Z.2 Online-Ressourcen

| Ressource | URL | Inhalt |
|---|---|---|
| Panbo (Marine Electronics) | panbo.com | Tests von Kettenzählern und Ankersystemen |
| Practical Sailor | practical-sailor.com | Unabhängige Ankerketten-Tests |
| Cruisers Forum | cruisersforum.com | Erfahrungsberichte Blauwasser |
| SailNet | sailnet.com | Technische Diskussionen |
| SVB Marine | svb-marine.de | Produktinformationen und Vergleiche |
| ICOMIA | icomia.org | Internationale Normen und Standards |

### Z.3 Testberichte und Vergleichstests

| Quelle | Test | Ergebnis (Zusammenfassung) | Jahr |
|---|---|---|---|
| Practical Sailor | Ankerketten-Bruchlasttest (6 Hersteller, 8 mm) | Titan G43 und Acco G43 übertrafen Nennwerte um 10–15%. Import-Kette unterschritt Nennwert um 20%. | 2022 |
| Practical Sailor | Zinkhaltbarkeitstest (12 Monate Salzwasser) | Premium-Ketten (>80 µm Zink) behielten 70% der Zinkschicht. Import-Ketten (<40 µm) waren nach 8 Monaten komplett entblößt. | 2021 |
| Yachting Monthly | Ketten-Tau-Kombi vs. All-Chain (Haltekraft-Vergleich) | All-Chain bei Scope 5:1 = Chain-Rope bei Scope 7:1. All-Chain erfordert weniger Raum, Chain-Rope weniger Gewicht. | 2020 |
| SAIL Magazine | Snubber-Test (8 Materialien, dynamische Last) | 3-Schlag Nylon absorbierte 85% der Ruckenergie. Geflochtenes Nylon nur 60%. Polyester nur 25%. HMPE praktisch 0%. | 2023 |
| Segeln-Magazin | DIN-766-Kompatibilitätstest (5 Hersteller auf 3 Winschen) | Alle DIN-766-kalibrierten Ketten funktionierten auf allen getesteten Kettennüssen (Lofrans, Quick, Lewmar). | 2022 |
| Cruising World | G30 vs G43 Langzeit-Haltekraftvergleich | Nach 5 Jahren Nutzung: G43 behielt 90% der Nennbruchlast. G30 nur 75% (schnellerer Verschleiß). | 2021 |

### Z.4 Video-Tutorials (empfohlene Kanäle)

| Kanal | Plattform | Sprache | Inhalte |
|---|---|---|---|
| SV Delos | YouTube | Englisch | Ankerpraxis Blauwasser, Kettenpflege |
| Sailing Uma | YouTube | Englisch | DIY-Kettenwartung, Budgetlösungen |
| Segeln ist Meer | YouTube | Deutsch | Ankertechnik Ostsee/Mittelmeer |
| Practical Sailor | YouTube | Englisch | Produkttests, Kettevergleiche |
| Ryan & Sophie | YouTube | Englisch | Ankerketteninspektion, Neuverzinkung DIY |
| Blauwasser.de | Website/YouTube | Deutsch | Ausrüstungsberatung Blauwasser |

### Z.5 Normen-Bezugsquellen

| Norm | Bezugsquelle | Preis (ca.) |
|---|---|---|
| DIN 766 | Beuth Verlag (beuth.de) | 50–80 EUR |
| ISO 4565 | ISO Store (iso.org) | 60–100 EUR |
| DIN EN ISO 1461 | Beuth Verlag | 50–70 EUR |
| ISO 1704 | ISO Store | 80–120 EUR |
| IACS UR A1 | IACS Webseite (kostenlos) | 0 EUR |

---

> **Ende der Wissensdatei 13.02 — Ankerketten und Kettenvorlauf**
> **AYDI Research | Version 1.0.0 | 2026-04-26**
> **Nächste geplante Aktualisierung: 2026-10-26**
