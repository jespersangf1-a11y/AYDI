---
title: "Verbinder Wartung und Troubleshooting"
kategorie: "12 Schäkel, Wirbel und Verbinder"
unterkategorie: "05 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Wartungsanleitungen, Laborprüfungen, Verschleißmessungen"
  - documented: "Hersteller-Kataloge, Rigger-Handbücher, Fachliteratur"
  - estimated: "Erfahrungswerte, Quervergleiche, Praxisberichte"
  - benchmark: "Branchenstandards, Versicherungsstatistiken, Havarieberichte"
tags:
  - wartung
  - maintenance
  - troubleshooting
  - schäkel
  - wirbel
  - verbinder
  - bolzen
  - splinte
  - schnappschäkel
  - korrosion
  - verschleiß
  - inspektion
  - schmierung
  - rigg
  - sicherheit
  - lebensdauer
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 12.05 — Verbinder Wartung und Troubleshooting: Vollständige Wissensreferenz

> **AYDI Wissensdatei 12.05** — Kategorie 12: Schäkel, Wirbel und Verbinder
> **Confidence-Quelle:** measured (Hersteller-TDS, Verschleißmessungen), documented (Wartungshandbücher, Rigger-Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Wartungsintervalle](#3-wartungsintervalle)
4. [Schritt-für-Schritt Wartung](#4-schritt-für-schritt-wartung)
5. [Schmiermittel und Korrosionsschutz](#5-schmiermittel-und-korrosionsschutz)
6. [Verschleißerkennung und Austauschkriterien](#6-verschleißerkennung-und-austauschkriterien)
7. [Anlagen-spezifische Wartung](#7-anlagen-spezifische-wartung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting-Entscheidungsbäume](#9-troubleshooting-entscheidungsbäume)
10. [FAQ — Häufige Fragen](#10-faq--häufige-fragen)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
14. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
15. [ANHANG C — Inspektions-Checklisten](#anhang-c--inspektions-checklisten)
16. [ANHANG D — Verschleißgrenztabellen](#anhang-d--verschleißgrenztabellen)
17. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
18. [ANHANG F — Werkzeuglisten](#anhang-f--werkzeuglisten)
19. [ANHANG G — Herstellerspezifische Wartungsvorgaben](#anhang-g--herstellerspezifische-wartungsvorgaben)
20. [ANHANG H — Schmierplan-Vorlagen](#anhang-h--schmierplan-vorlagen)
21. [ANHANG I — Korrosions-Referenztabellen](#anhang-i--korrosions-referenztabellen)
22. [ANHANG J — Ersatzteil-Referenz](#anhang-j--ersatzteil-referenz)
23. [ANHANG K — Dokumentationsvorlagen](#anhang-k--dokumentationsvorlagen)
24. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
25. [ANHANG M — Notfall-Reparaturverfahren](#anhang-m--notfall-reparaturverfahren)
26. [ANHANG N — Saisonale Wartungskalender](#anhang-n--saisonale-wartungskalender)
27. [ANHANG O — Schulungsunterlagen](#anhang-o--schulungsunterlagen)
28. [ANHANG P — Wirtschaftlichkeitsbetrachtung](#anhang-p--wirtschaftlichkeitsbetrachtung)
29. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
30. [ANHANG R — Prüfprotokolle](#anhang-r--prüfprotokolle)

---

## 1. Einführung und Übersicht

### 1.1 Warum Verbinderwartung sicherheitskritisch ist

Verbinder — Schäkel, Wirbel, Bolzen, Schnappschäkel und Toggles — sind die schwächsten Glieder in jeder Kette von Rigg- und Decksbeschlägen. Ein einzelner versagender Verbinder kann zum Mastbruch, zum Verlust der Segelkontrolle oder zum Durchgehen einer Ankerkette führen. Statistiken der Versicherungswirtschaft zeigen, dass 23–31% aller riggbezogenen Schadensfälle auf versagende oder unzureichend gewartete Verbinder zurückzuführen sind.

**Kernprinzip:** Verbinder sind Verschleißteile mit definierter Lebensdauer — keine "fit and forget"-Komponenten. Jeder Verbinder an Bord muss einem dokumentierten Wartungs- und Inspektionsplan unterliegen.

### 1.2 Schadensstatistik und Unfallursachen

| Schadensursache | Anteil | Vermeidbarkeit durch Wartung |
|----------------|--------|------------------------------|
| Korrosion (alle Typen) | 35% | 85% vermeidbar |
| Materialermüdung | 25% | 70% vermeidbar (rechtzeitige Inspektion) |
| Mechanischer Verschleiß | 20% | 90% vermeidbar |
| Überlastung | 12% | 40% vermeidbar (Dimensionierung) |
| Montagefehler | 8% | 95% vermeidbar |

> **Confidence: documented** — Basierend auf Auswertungen von Pantaenius, Allianz Global, MAIB-Reports 2018–2025

### 1.3 Geltungsbereich dieser Wissensdatei

Diese Datei deckt die Wartung und das Troubleshooting folgender Verbindertypen ab:

- **Schäkel** (D-Schäkel, Bügelschäkel, Wirbelschäkel, Langgliedschäkel)
- **Wirbel** (Gabel-Gabel, Gabel-Auge, Auge-Auge, Kugellager-Wirbel)
- **Bolzen und Splinte** (Bolzen, Splinte, Schnellverschlussbolzen, Federstecker)
- **Schnappschäkel** (Standard, Hochlast, Spinnaker-Schnappschäkel)
- **Toggles** (Gabelköpfe, Wantenspanner-Toggles)
- **Soft-Schäkel** (Dyneema-Verbinder)

### 1.4 Abgrenzung zu anderen Wissensdateien

| Thema | Wissensdatei |
|-------|-------------|
| Grundlagen, Typen, Auswahl | 12_01_schaekel_grundlagen.md |
| Wirbel und Drehgelenke | 12_02_wirbel_drehgelenke.md |
| Bolzen und Splinte | 12_03_bolzen_splinte.md |
| Schnappschäkel | 12_04_schnappschaekel.md |
| **Wartung und Troubleshooting (alle)** | **12_05_verbinder_wartung.md (diese Datei)** |

### 1.5 Sicherheitshinweise

> **WARNUNG:** Arbeiten am stehenden Gut und an lasttragenden Verbindern dürfen nur bei entlastetem Rigg durchgeführt werden. Niemals unter Last Bolzen entfernen oder Schäkel öffnen. Bei Unsicherheit einen zertifizierten Rigger hinzuziehen.

> **WARNUNG:** Beschädigte oder über die Verschleißgrenzen hinaus abgenutzte Verbinder müssen sofort ausgetauscht werden. Provisorische Reparaturen sind nur als Notmaßnahme auf See zulässig und müssen bei nächster Gelegenheit durch fachgerechten Austausch ersetzt werden.

---

## 2. Grundlagen und Theorie

### 2.1 Versagensmechanismen bei Verbindern

Verbinder unterliegen einem komplexen Zusammenspiel verschiedener Degradationsmechanismen, die einzeln oder in Kombination zum Versagen führen können. Das Verständnis dieser Mechanismen ist die Grundlage jeder sinnvollen Wartungsstrategie.

### 2.2 Korrosion

#### 2.2.1 Allgemeine Korrosion (Flächenkorrosion)

Gleichmäßiger Materialabtrag über die gesamte Oberfläche. Bei hochwertigem Edelstahl 316L in Salzwasser beträgt die Rate typischerweise <0,01 mm/Jahr. Erkennbar an matter, gleichmäßig aufgerauter Oberfläche. In der Regel nicht kritisch bei Marinequalität, aber ein Indikator für unzureichende Passivierung.

**Einflussfaktoren:**
- Legierungsqualität (316L vs. 304 vs. Duplex)
- Salzgehalt des Wassers
- Temperatur (tropische Gewässer beschleunigen um Faktor 2–3)
- pH-Wert (Industriehafen vs. offene See)
- Dauer der Benetzung

#### 2.2.2 Spaltkorrosion (Crevice Corrosion)

Die gefährlichste Korrosionsform bei Verbindern. Tritt in engen Spalten auf — zwischen Schäkelbolzen und -körper, unter Wirbellagern, unter Ablagerungen. Im Spalt wird der Sauerstoff verbraucht, der pH-Wert sinkt, Chlorid-Ionen konzentrieren sich. Die resultierende aggressive Lösung greift die Passivschicht des Edelstahls an.

**Kritische Stellen bei Verbindern:**
- Schäkelbolzen-Bohrung (häufigste Schadensstelle)
- Wirbelgehäuse-Inneres
- Toggle-Gabelschlitze
- Unter festsitzenden Salzablagerungen
- Unter Teflonbuchsen ohne Drainage

**Prävention:**
- Regelmäßiges Süßwasserspülen (mindestens monatlich, nach jeder Salzwasserexposition)
- Anti-Seize-Compound auf Bolzen (Tef-Gel, Lanocote)
- Regelmäßiges Lösen und Reinigen von Bolzenverbindungen
- Vermeidung von Totzonen ohne Wasserablauf

#### 2.2.3 Galvanische Korrosion (Kontaktkorrosion)

Tritt auf, wenn zwei verschiedene Metalle in einem Elektrolyten (Salzwasser) in Kontakt stehen. Das unedlere Metall (Anode) wird beschleunigt aufgelöst. Besonders problematisch bei gemischten Beschlagsystemen.

**Galvanische Reihe (marine, relevant für Verbinder):**

| Material | Potenzial (mV vs. SCE) | Risiko |
|----------|------------------------|--------|
| Titan | -50 bis +50 | Sehr edel (Kathode) |
| Edelstahl 316L (passiv) | -100 bis 0 | Edel |
| Monel | -150 bis -100 | Edel |
| Bronze | -300 bis -200 | Mittel |
| Edelstahl 316L (aktiv/Spalt) | -500 bis -350 | Unedles Verhalten! |
| Aluminium | -800 bis -600 | Unedles Verhalten |
| Zink | -1050 bis -950 | Opferanode |

**Kritische Kombinationen bei Verbindern:**
- Edelstahlschäkel an Aluminiummast → Aluminium wird aufgelöst
- Bronzeblock mit Edelstahlachse → normalerweise unkritisch (Potentialdifferenz gering)
- Edelstahlschäkel an verzinkter Kette → Zink wird beschleunigt aufgelöst
- Titanschäkel an Edelstahlbeschlag → Edelstahl kann leiden

**Prävention:**
- Galvanische Isolation (Tef-Gel, Kunststoffbuchsen, Duralac)
- Materialgleichheit anstreben
- Potentialdifferenz <200 mV einhalten
- Opferanoden in kritischen Bereichen

#### 2.2.4 Spannungsrisskorrosion (Stress Corrosion Cracking, SCC)

Kombination aus mechanischer Zugspannung, korrosivem Medium und empfindlichem Material. Führt zu plötzlichem Sprödbruch ohne Vorwarnung. Bei Edelstahl 316L ab Temperaturen >50°C in chloridhaltiger Umgebung relevant. Duplex-Stähle (z.B. SAF 2205) sind deutlich resistenter.

**Risikoerhöhende Faktoren:**
- Hohe statische Last (stehendes Gut)
- Tropische Gewässer (Temperatur + Salzgehalt)
- Kaltverformung (erhöht Eigenspannungen)
- Schweißnähte ohne Spannungsarmglühen
- Oberflächenbeschädigungen (Kerben, Kratzer)

**Erkennungsmerkmale:**
- Verästelte, intergranuläre Risse (nur unter Mikroskop sichtbar)
- Keine sichtbare plastische Verformung vor dem Bruch
- Bruchfläche spröd, oft mit Anlauffarben
- Häufig an Bolzenbohrungen und Radienübergängen

**Prävention:**
- Materialwahl: Duplex oder geschmiedetes 316L bevorzugen
- Regelmäßige NDT-Prüfung (Farbeindringprüfung alle 3–5 Jahre)
- Vermeidung von Überbelastung
- Süßwasserspülung nach jedem Einsatz in tropischen Gewässern

#### 2.2.5 Lochfraß (Pitting Corrosion)

Lokaler, stark konzentrierter Korrosionsangriff, der kleine, tiefe Löcher erzeugt. Beginnt an Schwachstellen der Passivschicht (Einschlüsse, mechanische Beschädigungen). Besonders tückisch, da die Oberfläche weitgehend intakt erscheint, während das Material lokal massiv geschwächt ist.

**Erkennungsmerkmale:**
- Kleine, scharf begrenzte Vertiefungen (0,1–2 mm Durchmesser)
- Oft unter Ablagerungen oder Biofilmen verborgen
- Rostbraune Verfärbungen als Indikator
- Querschnittsminderung kann erheblich sein

### 2.3 Materialermüdung (Fatigue)

#### 2.3.1 Grundlagen der Ermüdung

Verbinder unterliegen zyklischen Belastungen: Wellenschlag, Böen, Manöver, Schwojkreis am Ankerplatz. Auch bei Spannungen weit unterhalb der statischen Festigkeit können nach ausreichend vielen Lastzyklen Ermüdungsrisse entstehen.

**Wöhler-Kurve — typische Zyklenzahlen bis Versagen (Edelstahl 316L geschmiedet):**

| Belastung (% der Bruchlast) | Zyklen bis Rissinitiierung | Zyklen bis Bruch |
|------------------------------|---------------------------|-------------------|
| 80% | 1.000 | 5.000 |
| 60% | 10.000 | 50.000 |
| 40% | 100.000 | 500.000 |
| 30% | 500.000 | 2.000.000 |
| 20% | >2.000.000 | >10.000.000 |
| <15% (Dauerfestigkeit) | ∞ | ∞ |

> **Confidence: measured** — Basierend auf Wichard-Prüfdaten und DIN 50100

#### 2.3.2 Ermüdungskritische Stellen bei Verbindern

- **Schäkelbolzen-Bohrung:** Spannungskonzentrationsfaktor Kt = 2,5–3,5
- **Toggle-Gabelradien:** Kt = 2,0–4,0 je nach Radiusausführung
- **Wirbelachsen:** Kt = 1,8–2,5
- **Schnappschäkel-Nasen:** Kt = 3,0–5,0 (besonders kritisch)
- **Schweißnähte:** Kt = 1,5–4,0 je nach Qualität

#### 2.3.3 Einflussfaktoren auf die Ermüdungslebensdauer

- **Oberflächenzustand:** Kratzer, Korrosionsnarben reduzieren die Lebensdauer um 30–70%
- **Mittelspannung:** Hohe statische Vorlast (Rigspannung) verkürzt die Lebensdauer
- **Korrosion:** Salzwasser-Korrosionsermüdung senkt die Dauerfestigkeit um 50–80%
- **Temperatur:** Erhöhte Temperatur beschleunigt Risswachstum
- **Frequenz:** Niederfrequente Zyklen (Seegang) sind schädlicher als hochfrequente

### 2.4 Galling (Fressen, Kaltverschweißen)

Galling ist ein adhäsiver Verschleißmechanismus, der bei Edelstahl besonders häufig auftritt. Zwei Edelstahloberflächen unter Druck und Relativbewegung verschweißen lokal kallt miteinander. Das Ergebnis sind festsitzende Bolzen, zerstörte Gewinde und blockierte Wirbel.

**Galling-Risiko nach Materialpaarung:**

| Paarung | Galling-Risiko | Prävention |
|---------|---------------|------------|
| 316L / 316L | Sehr hoch | Anti-Seize zwingend |
| 316L / Bronze | Niedrig | Schmierfett ausreichend |
| 316L / Titan | Mittel | Anti-Seize empfohlen |
| Duplex / 316L | Hoch | Anti-Seize zwingend |
| 316L / Nitronic 60 | Sehr niedrig | Minimalschmierung |

**Prävention:**
- Anti-Seize-Compound bei jeder Montage
- Langsames, gleichmäßiges Anziehen
- Saubere, trockene Oberflächen vor Anti-Seize-Auftrag
- Unterschiedliche Härten der Kontaktpartner bevorzugen

### 2.5 UV-Degradation

Betrifft primär Soft-Schäkel (Dyneema/UHMWPE), aber auch Kunststoffkomponenten von Schnappschäkeln (Federn, Buchsen, Schutzkappen).

**UV-Degradation bei Dyneema-Soft-Schäkeln:**
- Festigkeitsverlust: ca. 2–5% pro 1000 Stunden direkte UV-Exposition
- Äußerliche Zeichen: Vergrauung, Aufspleißen der Oberfläche, Versteifung
- Lebensdauer bei ungeschützter Decksmontage: 2–4 Jahre (Mittelmeer)
- Lebensdauer bei geschützter Montage (im Mast, unter Lazy Bag): 5–8 Jahre

**Kunststoffkomponenten:**
- Nylon-Buchsen: Versprödung nach 3–5 Jahren UV-Exposition
- POM-Federn in Schnappschäkeln: Festigkeitsverlust 15–30% nach 5 Jahren
- Polycarbonat-Schutzkappen: Vergilbung und Sprödbruch nach 3–5 Jahren

### 2.6 Abrasiver Verschleiß

Mechanischer Materialabtrag durch Reibung, Scheuern und Partikeleinwirkung. Besonders relevant an:

- **Schäkelbolzen in Bohrungen:** Ovalisierung durch wechselnde Belastungsrichtung
- **Wirbellagerflächen:** Abrieb durch Sand/Salzkristalle in den Lagerspalten
- **Schnappschäkel-Nasen:** Abrieb durch wiederholtes Einrasten
- **Toggle-Bolzen:** Abrieb durch Schwenkbewegungen unter Last

**Verschleißraten (typisch, marine Bedingung):**

| Bauteil | Verschleißrate | Austauschgrenze |
|---------|---------------|-----------------|
| Schäkelbolzen (Ø 8mm) | 0,02–0,05 mm/Jahr | 5% Durchmesserreduktion (Ø 7,6mm) |
| Wirbelachse (Ø 10mm) | 0,03–0,08 mm/Jahr | 5% Reduktion (Ø 9,5mm) |
| Toggle-Bolzen (Ø 12mm) | 0,02–0,06 mm/Jahr | 5% Reduktion (Ø 11,4mm) |
| Schnappschäkel-Nase | 0,05–0,15 mm/Jahr | Sichtbare Verformung, kein sicheres Einrasten |

> **Confidence: estimated** — Zusammengestellt aus Rigger-Praxisberichten und Hersteller-Empfehlungen

---

## 3. Wartungsintervalle

### 3.1 Allgemeine Wartungsphilosophie

Die Wartung von Verbindern folgt einem abgestuften System aus routinemäßigen Sichtprüfungen, periodischen Detailinspektionen und zustandsabhängigen Eingriffen. Jeder Verbinder an Bord muss einem dieser Zyklen zugeordnet sein.

**Wartungsstufen:**

| Stufe | Bezeichnung | Umfang | Wer |
|-------|------------|--------|-----|
| W1 | Sichtprüfung | Augenschein, Funktionstest | Skipper |
| W2 | Detailinspektion | Demontage, Reinigung, Messung | Skipper/Eigner |
| W3 | Fachinspektion | NDT, kalibrierte Messung | Rigger/Surveyor |
| W4 | Generalüberholung | Kompletttausch, Dokumentation | Rigger/Werft |

### 3.2 Wartungsintervalle nach Verbindertyp

#### 3.2.1 Schäkel (D-Schäkel, Bügelschäkel)

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Sichtprüfung | Monatlich während Saison | Bolzensitz, Sicherung, Verformung, Korrosion |
| W2 Bolzeninspektion | Jährlich (Saisonende) | Bolzen lösen, reinigen, messen, Anti-Seize neu |
| W2 Bolzenbohrung | Jährlich | Auf Ovalisierung und Spaltkorrosion prüfen |
| W3 Farbeindringprüfung | Alle 5 Jahre (stehendes Gut) | Risssuche an Bolzenbohrung und Bügel |
| W3 Dimensionsprüfung | Alle 3 Jahre | Kalibrierte Messung aller kritischen Maße |
| W4 Kompletttausch | Nach 10–15 Jahren | Altersbedingt, unabhängig vom Zustand |

**Sonderbedingungen für verkürzte Intervalle:**
- Tropische Gewässer: alle Intervalle × 0,7
- Regattaeinsatz: alle Intervalle × 0,5
- Charterboote: alle Intervalle × 0,5
- Blauwasseryachten: W2 halbjährlich

#### 3.2.2 Wirbel (Drehgelenke)

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Funktionsprüfung | Monatlich | Drehgängigkeit, Spiel, Geräusche |
| W2 Schmierung | Alle 6 Monate | Demontage wenn möglich, Lager reinigen, schmieren |
| W2 Lagerinspektion | Jährlich | Lagerflächen auf Abrieb, Pitting, Galling prüfen |
| W3 Spiel-Messung | Alle 2 Jahre | Axiales und radiales Lagerspiel kalibriert messen |
| W3 NDT-Prüfung | Alle 5 Jahre | Farbeindringprüfung an Gabelaugen und Achse |
| W4 Kompletttausch | Nach 8–12 Jahre | Je nach Belastung und Zustand |

**Sonderbedingungen:**
- Ankerketten-Wirbel: W2 Schmierung alle 3 Monate
- Masttop-Wirbel: W2 jährlich (mit Mastlegung)
- Kugellager-Wirbel: W2 Schmierung alle 3 Monate bei Regattaeinsatz

#### 3.2.3 Bolzen und Splinte

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Splint-Kontrolle | Monatlich | Alle Splinte/Federstecker auf Sitz und Zustand |
| W1 Tape-Kontrolle | Wöchentlich (Regatta) | Abdecktape auf Segel- und Personenschutz |
| W2 Bolzenmessung | Jährlich | Bolzendurchmesser an 3 Stellen messen |
| W2 Bolzensitz | Jährlich | Bolzen lösen, Bohrung inspizieren, reinigen |
| W2 Splint-Tausch | Jährlich | Alle Federstecker und Splinte erneuern |
| W3 Bolzenmessung kalibriert | Alle 3 Jahre | Mikrometer-Messung, Protokoll |
| W4 Kompletttausch | Nach 8–12 Jahren | Alle Bolzen und zugehörige Splinte |

**Kritische Hinweise:**
- Splinte sind Einmalteile — nach jedem Entfernen ersetzen
- Federstecker dürfen maximal 3× wiederverwendet werden
- Bolzen mit sichtbarer Riefen- oder Rillenbildung sofort ersetzen

#### 3.2.4 Schnappschäkel

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Funktionstest | Wöchentlich während Saison | Einrasten/Ausrasten, Federkraft subjektiv |
| W1 Sichtprüfung | Monatlich | Verformung, Korrosion, Nasenabrieb |
| W2 Federprüfung | Saisonstart und -ende | Feder ausbauen, Zustand prüfen, Federkraft vergleichen |
| W2 Naseninspektion | Halbjährlich | Nase auf Abrieb, Verformung, Risse prüfen |
| W2 Schmierung | Alle 3 Monate | Federachse und Raststelle schmieren (Teflon-Spray) |
| W3 Federkraftmessung | Jährlich (Regatta) | Kraftmessgerät, Vergleich mit Neuzustand |
| W4 Kompletttausch | Nach 5–8 Jahren | Kürzere Lebensdauer als Standardschäkel |

**Sonderbedingungen:**
- Spinnaker-Schnappschäkel: W1 vor jeder Regatta, W2 monatlich
- Gennaker-Schnappschäkel: W2 nach jeder Saison
- Großsegel-Kopfbrett-Schnappschäkel: W2 halbjährlich

#### 3.2.5 Toggles (Gabelköpfe)

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Sichtprüfung | Monatlich | Risse in Gabel, Bolzensitz, Verformung |
| W2 Bolzeninspektion | Jährlich | Bolzen lösen, Lagerflächen prüfen |
| W2 Gabelöffnung messen | Jährlich | Aufweitung der Gabel als Ermüdungsindikator |
| W3 Farbeindringprüfung | Alle 3 Jahre | Risssuche an Gabelradien (höchste Belastung) |
| W4 Kompletttausch | Nach 10–15 Jahren | Altersbedingt |

**Kritische Hinweise:**
- Toggle-Gabeln mit sichtbaren Rissen sofort ersetzen — Bruchgefahr!
- Aufgeweitete Gabelöffnung (>1mm über Nennmaß) deutet auf Überlastung hin
- Toggle-Bolzen müssen frei schwenken — festsitzende Bolzen erzeugen Biegemomente im Wantterminal

#### 3.2.6 Soft-Schäkel (Dyneema)

| Wartung | Intervall | Beschreibung |
|---------|-----------|-------------|
| W1 Sichtprüfung | Wöchentlich | Aufrieb, Verfärbung, Verformung des Knotens |
| W2 Detailprüfung | Monatlich | Faserbrüche zählen, Knotensitz prüfen |
| W2 Durchmesser messen | Vierteljährlich | Durchmesserreduktion durch Abrieb |
| W2 UV-Beurteilung | Halbjährlich | Vergrauung, Oberflächenverhärtung bewerten |
| W3 Reißprüfung | Keine Feldprüfung möglich | Im Zweifel ersetzen |
| W4 Tausch | Nach 2–4 Jahren (Deck) | Je nach UV-Exposition |

### 3.3 Wartungsintervalle nach Hersteller

#### 3.3.1 Wichard

Wichard gibt in seinen technischen Dokumentationen folgende Wartungsintervalle vor:

| Produkt | Wichard-Empfehlung | AYDI-Empfehlung | Abweichung |
|---------|-------------------|-----------------|-----------|
| HR-Schäkel | Jährliche Inspektion | Jährlich + monatl. Sichtprüfung | Ergänzt um W1 |
| Selbstverriegelnde Schäkel | Halbjährliche Funktionsprüfung | Vierteljährlich | Häufiger (Sicherheit) |
| Wirbel (alle Typen) | Jährliche Schmierung | Halbjährlich | Häufiger (Salzwasser) |
| Schnappschäkel | Saisonale Inspektion | Monatlich W1, saisonal W2 | Ergänzt um W1 |
| Toggles | 5-jährliche NDT | 3-jährlich | Häufiger (Ermüdung) |

> **Confidence: documented** — Wichard Technical Documentation 2024, ergänzt durch AYDI-Erfahrungswerte

#### 3.3.2 Tylaska

| Produkt | Tylaska-Empfehlung | AYDI-Empfehlung | Abweichung |
|---------|-------------------|-----------------|-----------|
| T-Schäkel (alle) | Jährliche Inspektion | Jährlich + monatl. Sichtprüfung | Ergänzt um W1 |
| Schnappschäkel (T-Serie) | Saisonale Wartung, Federtausch | Vierteljährlich, Federtausch alle 2 Jahre | Spezifischer |
| Trigger-Release | Halbjährliche Inspektion | Vierteljährlich | Häufiger (Sicherheitsbauteil) |
| Toggle-Systeme | Jährliche Inspektion | Jährlich + Rissmonitoring | Ergänzt |

> **Confidence: documented** — Tylaska Marine Hardware Technical Bulletins

#### 3.3.3 Harken

| Produkt | Harken-Empfehlung | AYDI-Empfehlung | Abweichung |
|---------|-------------------|-----------------|-----------|
| Snap Shackle (Standard) | Saisonale Inspektion | Monatlich W1, saisonal W2 | Ergänzt um W1 |
| Snap Shackle (Hi-Load) | Halbjährliche Inspektion | Vierteljährlich | Häufiger |
| Unit Blocks mit Schäkel | Jährlich | Jährlich + Schmierung halbjährlich | Ergänzt |
| Battcar-Schäkel | Saisonale Inspektion | Vor jeder Regatta | Häufiger |

> **Confidence: documented** — Harken Maintenance Guides

#### 3.3.4 Ronstan

| Produkt | Ronstan-Empfehlung | AYDI-Empfehlung | Abweichung |
|---------|-------------------|-----------------|-----------|
| Orbit-Blöcke (Schäkelachse) | Jährlich | Jährlich + Sichtprüfung monatlich | Ergänzt |
| Schäkel (Standardlinie) | Jährlich | Jährlich + monatliche Sichtprüfung | Ergänzt |
| Wirbel | Halbjährliche Schmierung | Halbjährlich | Übereinstimmend |
| Serie 55 Snap Shackle | Saisonale Wartung | Vierteljährlich | Häufiger |

> **Confidence: documented** — Ronstan Technical Information Sheets

### 3.4 Wartungsintervalle nach Bootsklasse

#### 3.4.1 Jolle (4–8m)

Jollen haben weniger Verbinder, diese sind aber oft stärker belastet (Gewichtsoptimierung) und häufiger gewechselter Witterung ausgesetzt (Slipwagen, offenes Cockpit).

| Verbindergruppe | W1 | W2 | W3 | W4 |
|----------------|----|----|----|----|
| Wantschäkel | Monatlich | Saisonstart/-ende | Alle 5 Jahre | 10 Jahre |
| Trapezschäkel | Wöchentlich | Monatlich | Jährlich | 3 Jahre |
| Spinnaker-Snap | Vor jedem Segeln | Monatlich | Jährlich | 3 Jahre |
| Ruder-/Schwertbolzen | Monatlich | Saisonal | Alle 3 Jahre | 8 Jahre |

#### 3.4.2 Fahrtensegler (8–14m)

| Verbindergruppe | W1 | W2 | W3 | W4 |
|----------------|----|----|----|----|
| Stehendes Gut (Schäkel, Toggles) | Monatlich | Jährlich | Alle 5 Jahre | 12 Jahre |
| Laufendes Gut (Fallenschäkel) | Wöchentlich | Halbjährlich | Alle 3 Jahre | 8 Jahre |
| Ankerverbinder | Monatlich | Halbjährlich | Alle 3 Jahre | 10 Jahre |
| Decksbeschlag-Bolzen | Monatlich | Jährlich | Alle 5 Jahre | 15 Jahre |

#### 3.4.3 Blauwasseryacht (12–18m)

Erhöhte Anforderungen durch Dauereinsatz, tropische Gewässer, fehlende Werftinfrastruktur unterwegs.

| Verbindergruppe | W1 | W2 | W3 | W4 |
|----------------|----|----|----|----|
| Stehendes Gut | Wöchentlich | Halbjährlich | Alle 3 Jahre | 10 Jahre |
| Laufendes Gut | Wöchentlich | Vierteljährlich | Alle 2 Jahre | 5 Jahre |
| Ankerverbinder | Wöchentlich | Vierteljährlich | Jährlich | 8 Jahre |
| Sturmfock-/Trysegel-Schäkel | Monatlich | Halbjährlich | Jährlich | 8 Jahre |
| Rettungsinsel-Befestigung | Monatlich | Jährlich | Jährlich | Gemäß Hersteller |

#### 3.4.4 Regattayacht (8–20m)

Höchste Anforderungen durch extreme Belastungen, gewichtsoptimierte Bauteile, Hochlast-Schnappschäkel.

| Verbindergruppe | W1 | W2 | W3 | W4 |
|----------------|----|----|----|----|
| Stehendes Gut | Vor jeder Regatta | Nach jeder Saison | Jährlich | 5–8 Jahre |
| Laufendes Gut | Vor jeder Regatta | Monatlich | Halbjährlich | 3–5 Jahre |
| Spinnaker-System | Vor jedem Einsatz | Wöchentlich | Monatlich | 2–3 Jahre |
| Soft-Schäkel | Vor jeder Regatta | Monatlich | — | 1–2 Jahre |
| Trapez/Ausreitsystem | Vor jedem Segeln | Wöchentlich | Monatlich | 2 Jahre |

#### 3.4.5 Superyacht (18m+)

| Verbindergruppe | W1 | W2 | W3 | W4 |
|----------------|----|----|----|----|
| Stehendes Gut | Wöchentlich (Crew) | Vierteljährlich | Jährlich (Surveyor) | 10 Jahre |
| Laufendes Gut | Wöchentlich (Crew) | Monatlich | Halbjährlich | 5 Jahre |
| Ankersystem | Vor/nach jeder Nutzung | Monatlich | Halbjährlich | 8 Jahre |
| Kran-/Davit-Verbinder | Vor jeder Nutzung | Monatlich | Vierteljährlich (Surveyor) | 5 Jahre |
| Tender-Lift-Verbinder | Vor jeder Nutzung | Wöchentlich | Monatlich | 3 Jahre |

---

## 4. Schritt-für-Schritt Wartung

### 4.1 Allgemeine Vorbereitung

**Vor jeder Wartungsarbeit an Verbindern:**

1. **Rigg entlasten:** Fall/Schot fieren, Wantenspanner lösen, Ankerkette auf Klampe/Poller sichern
2. **Ersatzteile bereitlegen:** Neue Splinte, Federstecker, Anti-Seize, Schmiermittel
3. **Werkzeug zusammenstellen:** Gabelschlüssel passend, Dorn, Hammer (Kunststoff/Messing), Messschieber, Lupe (10×), Kamera
4. **Dokumentation vorbereiten:** Inspektionsprotokoll, Fotos vorher, Messwerte-Tabelle
5. **Sicherung:** Bei Arbeiten in der Höhe: Bosunsstuhl, Sicherungsleine, Werkzeugtasche

### 4.2 Schäkelbolzen-Inspektion und -Messung

**Dauer:** 10–15 Minuten pro Schäkel | **Werkzeug:** Messschieber (0,02mm), Lupe 10×, Tef-Gel, neue Splinte

**Schritt 1 — Fotodokumentation (Vorzustand)**
- Schäkel im eingebauten Zustand fotografieren
- Position, Orientierung, Zustand der Sicherung dokumentieren
- Beschriftung/Markierung notieren

**Schritt 2 — Sicherung entfernen**
- Federstecker: Mit Spitzzange Schenkel zusammendrücken, herausziehen
- Splint: Schenkel geradebiegen, herausziehen, NICHT wiederverwenden
- Drahtwicklung: Aufschneiden, entfernen
- Selbstsichernd (Wichard HR): Innensechskant lösen (meist 3mm oder 4mm)

**Schritt 3 — Bolzen lösen**
- Bolzen mit Dorn von der Gewindenseite her austreiben
- Festsitzende Bolzen: Kriechöl (WD-40, Caramba) einwirken lassen (30 Min)
- NIEMALS mit Stahlhammer direkt auf Bolzen schlagen → Materialschäden
- Bei extremem Festsitzen: Bolzen von hinten mit Messingdorn austreiben
- Dokumentieren, wenn Bolzen festsaß → Indikator für Korrosion/Galling

**Schritt 4 — Reinigung**
- Bolzen und Bohrung mit Süßwasser und Bürste (Nylon, NICHT Stahl!) reinigen
- Alte Anti-Seize-Reste mit Lösungsmittel (Isopropanol) entfernen
- Oberflächen trocknen lassen
- Bei hartnäckigen Ablagerungen: Essiglösung (5%) einweichen, dann spülen

**Schritt 5 — Bolzenmessung**
- Durchmesser an drei Stellen messen: Kopf, Mitte, Gewinde/Ende
- An jeder Stelle in zwei Achsen messen (0° und 90°)
- Werte protokollieren und mit Nennmaß vergleichen
- Ovalität berechnen: Differenz der beiden Achsen

**Auswertung Bolzenmessung:**

| Befund | Bewertung | Maßnahme |
|--------|-----------|----------|
| Ø-Reduktion <2% | In Ordnung | Weiter verwenden |
| Ø-Reduktion 2–5% | Beobachten | Inspektionsintervall halbieren |
| Ø-Reduktion >5% | Ersetzen | Bolzen sofort tauschen |
| Ovalität >0,1mm | Beobachten | Ursache analysieren |
| Ovalität >0,3mm | Ersetzen | Bolzen tauschen, Bohrung prüfen |
| Riefen/Rillen sichtbar | Bewerten | >0,1mm Tiefe → tauschen |
| Pitting/Lochfraß | Ersetzen | Sofort tauschen |
| Risse (Lupe) | Ersetzen | Sofort tauschen, Schäkelkörper prüfen |

**Schritt 6 — Bohrungsinspektion**
- Mit LED-Taschenlampe in Bohrung leuchten
- Auf Spaltkorrosion (rotbraune Verfärbung) achten
- Ovalisierung der Bohrung messen (schwierig → Lehrdorn verwenden)
- Bei Korrosion in der Bohrung: Schäkelkörper ersetzen

**Schritt 7 — Anti-Seize auftragen**
- Tef-Gel oder Lanocote dünn auf Bolzenschaft auftragen
- Gewinde einstreichen
- Bohrungsinnenrand dünn benetzen
- NICHT zu viel — überschüssiges Material sammelt Schmutz

**Schritt 8 — Zusammenbau**
- Bolzen einsetzen, Gewinde handfest anziehen
- Sicherung einbauen:
  - Neuen Splint einsetzen, Schenkel umbiegen (mindestens 90°)
  - Neuen Federstecker einsetzen
  - Selbstsichernd: Innensechskant festziehen, Loctite 243 optional
- Korrekte Orientierung prüfen: Bolzen so einsetzen, dass Kopf/Sicherung nicht an Segeln/Tauwerk scheuert

**Schritt 9 — Dokumentation**
- Messwerte protokollieren
- Foto Nachzustand
- Nächsten Inspektionstermin vermerken
- Auffälligkeiten im Wartungslog eintragen

### 4.3 Wirbel-Lagerservice

**Dauer:** 20–40 Minuten pro Wirbel | **Werkzeug:** Schraubenzieher/Innensechskant, Reinigungsmittel, Schmierfett (marine), Messschieber

**Schritt 1 — Demontage (wenn möglich)**
- Nicht alle Wirbel sind zerlegbar — Bauart identifizieren
  - Zerlegbar: Wichard, Ronstan (die meisten Modelle)
  - Teilzerlegbar: Seldén, Harken (nur Achse)
  - Nicht zerlegbar: einige Billigmodelle → nur äußerlich reinigen/schmieren
- Sicherungsschraube/Sprengring entfernen
- Achse vorsichtig herausziehen
- Alle Teile beschriften (oben/unten, Einbaurichtung)

**Schritt 2 — Reinigung**
- Alle Teile in Süßwasser einweichen (30 Minuten)
- Lagerflächen mit weicher Bürste und Spülmittel reinigen
- Salzkristalle und Ablagerungen vollständig entfernen
- Gehäuseinneres mit Wattestäbchen/Lappen reinigen
- Bei Kugellagerwirbeln: Lager NICHT mit Druckluft ausblasen (zerstört Dichtungen)

**Schritt 3 — Inspektion der Lagerflächen**
- Gleitflächen auf Riefen, Galling-Spuren, Pitting prüfen
- Kugellager auf Rauigkeit prüfen (von Hand drehen)
- Achse auf Abrieb und Risse prüfen
- Gabelaugen auf Aufweitung und Risse prüfen
- Sprengring/Sicherung auf Verformung prüfen

**Auswertung Wirbelinspektion:**

| Befund | Bewertung | Maßnahme |
|--------|-----------|----------|
| Leichtgängig, keine Spuren | In Ordnung | Schmieren, zusammenbauen |
| Leichte Rauigkeit | Normal | Glätten (Scotch-Brite), schmieren |
| Deutliche Galling-Spuren | Grenzwertig | Glätten, Anti-Seize, Intervall halbieren |
| Tiefe Riefen (>0,1mm) | Ersetzen | Wirbel tauschen |
| Kugellager rau/blockiert | Ersetzen | Lager oder Wirbel komplett tauschen |
| Pitting in Lagerfläche | Ersetzen | Wirbel tauschen |
| Risse (Gabelauge, Achse) | Sofort ersetzen | Sicherheitsrelevant! |
| Axialspiel >0,5mm | Beobachten | Ursache: Verschleiß oder Montage |
| Axialspiel >1,0mm | Ersetzen | Tragfähigkeit reduziert |

**Schritt 4 — Schmierung**
- Gleitlager: Marine-Schmierfett (z.B. Harken Winch Grease) dünn auftragen
- Kugellager: Spezialfett für Kugellager, Menge gemäß Herstellerangabe
- Achse: Anti-Seize auf Gewinde und Sicherungsschraube
- NICHT schmieren: Freilaufende Drahtseilterminals → Fett sammelt Wasser in Litzenhohlräumen

**Schritt 5 — Zusammenbau und Funktionstest**
- Teile in korrekter Reihenfolge zusammenbauen
- Sicherung (Sprengring, Schraube) einsetzen
- Drehgängigkeit prüfen: Wirbel muss unter leichtem Zug frei drehen
- Axialspiel prüfen: maximal gemäß Herstellerangabe
- Funktionstest: am eingebauten System 10× durchdrehen

### 4.4 Splint- und Federstecker-Austausch

**Dauer:** 5 Minuten pro Splint | **Werkzeug:** Spitzzange, Seitenschneider, neue Splinte/Federstecker

**Grundregeln:**
- Splinte (Biegesplinte): IMMER ersetzen — sind Einmalteile
- Federstecker (R-Clips): können 2–3× wiederverwendet werden, wenn keine Verformung
- Korrekte Größe verwenden: Splint-Ø = Bolzenbohrung minus 0,5mm Spiel
- Splintlänge: Schenkel nach Umbiegen mindestens 1× Bolzendurchmesser umgreifen
- Material: Edelstahl 316L — KEIN Messing, kein verzinkter Stahl im Salzwasser

**Verfahren Splint-Tausch:**
1. Alten Splint mit Seitenschneider kürzen (wenn Schenkel stark umgebogen)
2. Schenkel mit Spitzzange geradebiegen
3. Splint herausziehen
4. Bohrung reinigen (Dorn oder dünner Draht)
5. Neuen Splint einsetzen
6. Schenkel um Bolzen biegen: mindestens 90°, besser 180°
7. Enden mit Tape/Schrumpfschlauch abdecken (Segel-/Hautschutz)
8. Sicherstellen: Splint darf sich nicht selbsttätig lösen können

**Federstecker-Prüfung:**
- Federweg prüfen: muss satt einrasten
- Schenkel auf Verbiegung prüfen
- Rost/Korrosion → sofort tauschen
- Locker sitzende Federstecker → nächste Größe verwenden oder durch Splint ersetzen

### 4.5 Schnappschäkel-Federtausch

**Dauer:** 15–30 Minuten | **Werkzeug:** Innensechskant-Set, Feinmechanik-Schraubenzieher, Ersatzfeder, Teflon-Spray

**Schritt 1 — Bauart identifizieren**
- Harken: Federachse durch Splint gesichert, Feder auf Achse aufgeschoben
- Tylaska: Versenkte Innensechskantschraube, Feder und Plunger-System
- Wichard: Schraube am Nasenfuß, Blattfeder oder Spiralfeder
- Ronstan: Ähnlich Harken, Splint-gesichert

**Schritt 2 — Demontage**
- Schnappschäkel NICHT unter Last demontieren
- Sicherung entfernen (Splint, Schraube)
- Federachse/Federelement vorsichtig herausziehen
- ACHTUNG: Feder steht unter Spannung — Schutzbrille tragen!
- Teile in Reihenfolge ablegen und fotografieren

**Schritt 3 — Inspektion**
- Feder: Auf Ermüdung, Bruch, Korrosion, Verformung prüfen
- Federachse: Auf Abrieb, Verformung, Korrosion prüfen
- Nase: Auf Abrieb, Verformung, Risse prüfen (kritisch!)
- Gehäuse: Federaufnahme auf Verschleiß, Korrosion prüfen
- Rastpunkt: Rastfläche auf Abrieb prüfen

**Schritt 4 — Federtausch**
- Originale Ersatzfeder des Herstellers verwenden — Federkraft ist spezifiziert!
- KEINE Universal-Federn → Federkraft muss zum Modell passen
- Neue Feder einsetzen (Einbaurichtung beachten)
- Federachse einschieben
- Sicherung anbringen (neuer Splint oder Schraube + Loctite 243)

**Schritt 5 — Funktionstest**
- Nase muss satt und hörbar einrasten
- Nase muss sich mit einer Hand gegen die Feder öffnen lassen
- Unter simulierter Last (Hand) darf die Nase nicht aufspringen
- 20× Auf-/Zumachen → gleichmäßige Funktion
- Vergleich mit neuem Schnappschäkel: ähnliche Federkraft?

**Schritt 6 — Schmierung und Abschluss**
- Federachse dünn mit Teflon-Spray einsprühen
- KEIN Fett auf Raststelle → sammelt Schmutz, behindert Einrasten
- Nase und Kontaktflächen: trocken lassen oder nur Teflon-Spray
- Bewegliche Teile: nur Teflon-Spray (kein Öl, kein Fett)

### 4.6 Toggle-Inspektion auf Ermüdungsrisse

**Dauer:** 15–20 Minuten pro Toggle | **Werkzeug:** Lupe 10×, ggf. Farbeindringmittel-Set (PT), LED-Taschenlampe, Messschieber

**Warum Toggles besonders ermüdungskritisch sind:**

Toggles nehmen die Wechselbiegebelastung aus dem Rigg auf und überführen sie in eine saubere axiale Belastung des Wantterminals. Die Gabelradien sind dabei extremen Spannungskonzentrationen ausgesetzt (Kt = 2,0–4,0). Ermüdungsrisse an Toggles sind eine der häufigsten Ursachen für Riggversagen bei Yachten >10m.

**Schritt 1 — Visuelle Inspektion (W1/W2)**
- Toggle unter heller Beleuchtung (LED) inspizieren
- Mit Lupe (10×) alle Radienübergänge absuchen
- Typische Rissstartpunkte:
  - Innenseite der Gabelradien (häufigster Rissort)
  - Bohrungsrand
  - Übergang Gabel → Schaft
- Verfärbungen (Roststreifen aus Riss heraus) beachten
- Verformungen der Gabel (Aufweitung, Verdrehung)

**Schritt 2 — Dimensionskontrolle**
- Gabelöffnungsweite messen und mit Nennmaß vergleichen
- Aufweitung >0,5mm → genauer untersuchen
- Aufweitung >1,0mm → Toggle ersetzen (Überlastungsindikator)
- Bolzendurchmesser messen (Verschleiß)
- Gabelschlitzbreite messen (Aufweitung)

**Schritt 3 — Farbeindringprüfung (W3)**
- Nur bei Verdacht oder nach Plan (alle 3–5 Jahre)
- Oberfläche mit Reiniger vorbereiten (Cleaner aus PT-Set)
- Eindringmittel (rot) auftragen, 15–30 Minuten einwirken lassen
- Überschuss abwischen
- Entwickler (weiß) aufsprühen
- Risse zeigen sich als rote Linien im weißen Entwickler
- Dokumentieren und fotografieren

**Bewertung von Farbeindringprüfungen an Toggles:**

| Befund | Bewertung | Maßnahme |
|--------|-----------|----------|
| Keine Anzeigen | In Ordnung | Nächster Plan-Termin |
| Lineare Anzeige <3mm | Grenzwertig | Rigger konsultieren, Intervall auf 1 Jahr |
| Lineare Anzeige >3mm | Ersetzen | Toggle sofort tauschen |
| Mehrere Anzeigen | Ersetzen | Sofort tauschen, Rigg-Check empfehlen |
| Rundliche Anzeigen | Pitting | Beobachten, Anti-Korrosion verstärken |

### 4.7 Wartung von Wantenspanner-Verbindungen

**Dauer:** 30–45 Minuten pro Wantenspanner | **Werkzeug:** Gabelschlüssel (2 Stück passend), Messschieber, Anti-Seize, Splinte

**Schritt 1 — Rigg entlasten**
- Fall oder Backstag gegenüber nutzen, um Want zu entlasten
- Alternativ: Bei Mastlegung komplett entspannen
- NIEMALS Wantenspanner unter voller Rigspannung öffnen

**Schritt 2 — Sicherungen entfernen**
- Splinte an Spannschraube entfernen
- Kontermuttern lösen (wenn vorhanden)
- Tape/Schutz entfernen

**Schritt 3 — Wantenspanner öffnen**
- Spannschraube langsam ausdrehen (Umdrehungen zählen!)
- Gewinde auf Galling-Spuren prüfen
- Gabelköpfe/Terminals von Spannschraube trennen

**Schritt 4 — Inspektion aller Verbindungspunkte**
- Gabelbolzen oben und unten: Messung, Sichtprüfung
- Toggle (unten): Rissprüfung gemäß 4.6
- T-Terminal oder Gabelkopf: Auf Risse am Übergang zum Drahtseil
- Gewinde: Auf Verschleiß, Galling, Korrosion
- Mastbeschlag: Bolzen, Buchsen, Auge

**Schritt 5 — Reinigung und Schmierung**
- Alle Gewinde reinigen (Drahtbürste aus Bronze)
- Anti-Seize auf alle Gewinde auftragen (Tef-Gel)
- Bolzen: Anti-Seize dünn auf Schaft
- Toggle: Anti-Seize auf Bolzen
- KEIN Fett/Öl auf offene Gewinde → sammelt Schmutz

**Schritt 6 — Zusammenbau**
- In umgekehrter Reihenfolge zusammenbauen
- Wantenspanner auf dokumentierte Umdrehungszahl zurückdrehen
- Neue Splinte einsetzen
- Kontermuttern sichern
- Tape/Schutz erneuern

### 4.8 Ankerketten-Verbinder Wartung

**Dauer:** 20–30 Minuten | **Werkzeug:** Drahtbürste, Messschieber, Ankerketten-Wirbelschlüssel, Schmierfett

**Spezielle Anforderungen:**
- Ankerketten-Verbinder unterliegen extremer Belastung: dynamische Ankerlasten, Kettenschloss-Blockierung, Abrieb durch Ankerwinde
- Salzwasserexposition ist permanent, Süßwasserspülung oft schwierig
- Sicherheitsrelevant: Verlust des Ankers = Sicherheitsrisiko

**Schritt 1 — Kette fieren, Verbinder zugänglich machen**
- Ankerkette so weit fieren, dass Wirbelschäkel / Kettenverbinder sichtbar
- Kette auf Deck sichern (nicht nur auf Windenbremsband verlassen)

**Schritt 2 — Sichtinspektion**
- Wirbelschäkel: Bolzensitz, Sicherung, Verformung
- Kettenwirbel: Drehgängigkeit, Spiel, Korrosion
- Ketten-Anker-Schäkel: Bolzen, Sicherung
- Ketten-Vorläufer-Verbindung: Schäkel, Spleiß

**Schritt 3 — Reinigung**
- Mit Süßwasser und Drahtbürste (Bronze bei Edelstahl, Stahl bei verzinkter Kette)
- Salzablagerungen vollständig entfernen
- Besonders in Gewindegängen und Spalten

**Schritt 4 — Messung und Inspektion**
- Bolzendurchmesser messen
- Bügelöffnung messen (Aufweitung)
- Gewindegängigkeit prüfen (Bolzen muss sich lösen lassen)
- Wirbel auf Leichtgängigkeit prüfen

**Schritt 5 — Schmierung und Zusammenbau**
- Bolzengewinde mit Anti-Seize einstreichen
- Wirbellagerflächen mit Marine-Fett schmieren
- Bolzen handfest + Sicherung (Draht oder Splint)
- Wirbelschäkel-Bolzen: Drahtwicklung erneuern

---

## 5. Schmiermittel und Korrosionsschutz

### 5.1 Übersicht der Schmiermittel und Schutzpasten

#### 5.1.1 Anti-Seize-Compounds (Montagepaste)

Anti-Seize-Compounds verhindern Galling, Festfressen und galvanische Korrosion an Gewindeverbindungen und Bolzen. Sie sind KEIN Schmiermittel im klassischen Sinne, sondern Montagehilfen und Korrosionsschutz.

**Tef-Gel (Fluoropolymer-basiert):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | PTFE (Teflon) in Gelform |
| Temperaturbereich | -40°C bis +260°C |
| Galvanische Isolation | Ja (hervorragend) |
| Wasserbeständigkeit | Ausgezeichnet |
| Galling-Schutz | Ausgezeichnet |
| Anwendung | Edelstahl/Edelstahl, Edelstahl/Aluminium, Gewinde |
| Auftrag | Dünn mit Finger oder Pinsel |
| Ergiebigkeit | 30g-Tube reicht für 50+ Schäkel |
| Nachteile | Teuer (~€15/30g), nicht für Hochlast-Gleitlager |

> **Confidence: measured** — Herstellerdatenblatt Tef-Gel/Tef-Gel HD, Praxistests

**Lanocote (Lanolin-basiert):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | Wasserfreies Lanolin |
| Temperaturbereich | -20°C bis +150°C |
| Galvanische Isolation | Gut |
| Wasserbeständigkeit | Sehr gut (natürlich wasserabweisend) |
| Galling-Schutz | Gut |
| Anwendung | Universal-Korrosionsschutz, Bolzen, Gewinde, Schlösser |
| Auftrag | Dünn mit Finger, Pinsel oder Lappen |
| Ergiebigkeit | 120g-Dose für eine komplette Yacht |
| Nachteile | Zieht Staub an, nicht für hohe Temperaturen |

**Duralac (Chromat-basiert):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | Bariumchromat in Bindemittel |
| Temperaturbereich | -30°C bis +200°C |
| Galvanische Isolation | Ausgezeichnet (Hauptzweck) |
| Wasserbeständigkeit | Ausgezeichnet |
| Galling-Schutz | Gut |
| Anwendung | Primär für Aluminium/Edelstahl-Kontaktstellen |
| Auftrag | Dünn mit Pinsel |
| Ergiebigkeit | 125ml für 30+ Verbindungen |
| Nachteile | Grüne Farbe, enthält Chromat (Gesundheitsschutz!) |

> **WARNUNG:** Duralac enthält Bariumchromat — Handschuhe und Augenschutz tragen, nicht einatmen. In einigen Ländern eingeschränkt erhältlich.

**Vergleich und Empfehlung:**

| Anwendung | Empfehlung 1. Wahl | Alternative |
|-----------|-------------------|-------------|
| Edelstahl/Edelstahl-Gewinde | Tef-Gel | Lanocote |
| Edelstahl/Aluminium | Duralac oder Tef-Gel | Lanocote |
| Bolzen in Bohrungen | Tef-Gel | Lanocote |
| Wantenspanner-Gewinde | Tef-Gel HD | Tef-Gel Standard |
| Allg. Korrosionsschutz | Lanocote | Tef-Gel |
| Ankerketten-Verbinder | Lanocote | Marine-Fett |
| Notfall/provisorisch | Vaseline | Kriechöl (temporär) |

#### 5.1.2 Schmierfette (Lager, Wirbel)

**Marine-Schmierfett (z.B. Harken Winch Grease):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | Lithium-Komplex + PTFE |
| Temperaturbereich | -30°C bis +180°C |
| Wasserbeständigkeit | Ausgezeichnet (NLGI 2) |
| Salzwasserbeständigkeit | Ausgezeichnet |
| Anwendung | Wirbel-Gleitlager, Rollenlager, Winschgetriebe |
| Nachteile | Sammelt Schmutz, muss regelmäßig erneuert werden |

**Kugellager-Fett (für Kugellager-Wirbel):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | Synthetisch (PAO) + Lithium-Komplex |
| Temperaturbereich | -40°C bis +200°C |
| Wasserbeständigkeit | Ausgezeichnet |
| Anwendung | Geschlossene Kugellager (Wirbel, Blöcke) |
| Nachteile | Teuer, spezielle Anwendung |

#### 5.1.3 Sprühschmierstoffe

**Teflon-Spray (PTFE):**

| Eigenschaft | Wert |
|-------------|------|
| Basis | PTFE-Partikel in Lösungsmittel |
| Anwendung | Schnappschäkel-Mechanik, Reißverschlüsse, leichte Schmierung |
| Vorteile | Trocken nach Verdampfung, sammelt keinen Schmutz |
| Nachteile | Kurzlebig, muss häufig erneuert werden |
| Intervall | Alle 2–4 Wochen bei Einsatz |

**Silikon-Spray:**

| Eigenschaft | Wert |
|-------------|------|
| Basis | Silikonöl in Lösungsmittel |
| Anwendung | Dichtungen, Reißverschlüsse, NICHT für belastete Teile |
| Vorteile | Wasserabweisend, materialschonend |
| Nachteile | Keine Lastschmierung, kontaminiert Klebeflächen |
| WARNUNG | NIEMALS auf Flächen anwenden, die später geklebt oder lackiert werden! |

### 5.2 Wann NICHT schmieren

Es gibt Situationen, in denen Schmierung kontraproduktiv oder sogar gefährlich ist:

| Situation | Begründung | Stattdessen |
|-----------|------------|-------------|
| Drahtseilterminals (Presshülsen) | Fett zieht Wasser in Litzenhohlräume → Innenkorrosion | Trocken lassen, Wachs außen |
| Dyneema/Soft-Schäkel | Kontaminiert Fasern, kann Schlupf verursachen | Trocken lassen |
| Schnappschäkel-Raststelle | Fett/Öl sammelt Schmutz, behindert sicheres Einrasten | Nur Teflon-Spray |
| Festsitzende Bolzen (Erstlösung) | Fett auf Oberfläche hilft nicht | Kriechöl in Spalt, einwirken lassen |
| Segel-berührende Flächen | Fett/Öl macht Flecken auf Segeln | Tef-Gel (trocken) oder gar nichts |
| Aluminium-Oberflächen für Klebung | Fett verhindert Haftung | Reinigung mit Aceton |

### 5.3 Galvanische Isolation

#### 5.3.1 Warum galvanische Isolation bei Verbindern wichtig ist

Bei gemischten Metallkombinationen (z.B. Edelstahlschäkel auf Aluminiumbeschlag) entsteht ohne galvanische Isolation eine galvanische Zelle. Das unedlere Metall wird beschleunigt korrodiert. Bei Verbindern führt dies zu:
- Materialverlust am Beschlag (Aluminium)
- Festsitzen des Bolzens durch Korrosionsprodukte
- Querschnittsminderung und Tragfähigkeitsverlust

#### 5.3.2 Methoden der galvanischen Isolation

**Chemische Isolation (Pasten/Compounds):**
- Tef-Gel: Bildet PTFE-Barriere zwischen den Metallen
- Duralac: Bildet Chromat-Barriere (aktiver Korrosionsschutz)
- Lanocote: Bildet Lanolin-Barriere (passiver Schutz)

**Mechanische Isolation (Buchsen/Unterlagen):**
- Nylon-Buchsen: In Bolzenbohrungen bei Alu/Edelstahl-Kontakt
- PTFE-Scheiben: Zwischen Schäkel und Beschlagauge
- Delrin-Buchsen: In Wirbelgehäusen (Ronstan, Harken)
- Schrumpfschlauch: Provisorische Isolation im Notfall

**Elektrische Isolation (Komplett):**
- Titanium-Schäkel an Aluminiummast → MUSS isoliert werden
- Carbon-Mast mit Edelstahlbeschlag → galvanische Isolation zwingend
- GFK-Buchsen bei Carbon/Metall-Kontakt

### 5.4 Korrosionsschutz-Strategien nach Einsatzgebiet

| Einsatzgebiet | Strategie | Intervall |
|---------------|-----------|-----------|
| Ostsee/Nordsee | Anti-Seize + jährliche Wartung | Standard |
| Mittelmeer | Anti-Seize + halbjährliche Wartung | ×0,8 |
| Tropen/Karibik | Anti-Seize + vierteljährliche Wartung + Süßwasser | ×0,5 |
| Hochsee/Blauwasser | Anti-Seize + monatliche Sichtprüfung | ×0,5 |
| Trockenliegend (Winter) | Lanocote + Abdeckung | Vor Einwinterung |
| Dauerliegeplatz (Wasser) | Anti-Seize + monatliche Prüfung | ×0,7 |

### 5.5 Schmiermittel-Verträglichkeitsmatrix

| | Tef-Gel | Lanocote | Duralac | Marine-Fett | Teflon-Spray | Silikon |
|---|---------|----------|---------|-------------|-------------|---------|
| Tef-Gel | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ |
| Lanocote | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Duralac | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Marine-Fett | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ |
| Teflon-Spray | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Silikon | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |

> **Hinweis:** ✗ bedeutet "nicht mischen" — altes Mittel vollständig entfernen vor Wechsel. Duralac ist grundsätzlich nicht mit anderen Mitteln mischbar. Silikon darf nicht mit Fett oder Tef-Gel gemischt werden.

---

## 6. Verschleißerkennung und Austauschkriterien

### 6.1 Messmethoden

#### 6.1.1 Bolzendurchmesser-Messung

**Werkzeug:** Bügelmessschraube (Mikrometer) 0–25mm, Genauigkeit 0,01mm. Alternativ: Messschieber mit Genauigkeit 0,02mm.

**Messpunkte pro Bolzen:**
- Position 1: 5mm hinter Bolzenkopf
- Position 2: Mitte des Bolzens
- Position 3: 5mm vor Gewindeanfang
- An jeder Position: Messung in 0° und 90° (Ovalität)

**Messprotokoll-Schema:**

```
Bolzen-ID: WS_Stb_Unt_01 (Wantenspanner Steuerbord Unterwant 01)
Nennmaß: 10,00 mm
Messdatum: 2026-04-26
Messmittel: Bügelmessschraube Mitutoyo 0-25mm, Kalibrierung 2026-01

Position | 0° | 90° | Ovalität | Reduktion
---------|------|------|----------|----------
Kopf     | 9,95 | 9,96 | 0,01     | 0,5%
Mitte    | 9,88 | 9,92 | 0,04     | 1,2%
Gewinde  | 9,90 | 9,91 | 0,01     | 1,0%

Bewertung: In Ordnung (max. Reduktion 1,2% < 5%)
Nächste Messung: 2027-04-26
```

#### 6.1.2 Bohrungsmessung

**Werkzeug:** Innenmessschraube, Lehrdorn (go/no-go), oder Teleskop-Innentaster + Messschieber

**Verfahren:**
1. Bohrung reinigen und trocknen
2. An drei Positionen messen: Eingang, Mitte, Ausgang
3. In zwei Achsen messen: Lastrichtung und 90° dazu
4. Mit Nennmaß vergleichen (Herstellerangabe oder Bolzendurchmesser + 0,1mm)

**Go/No-Go-Lehrdorn:**
- GO-Seite (Nennmaß): muss einführbar sein → Bohrung nicht zukorrodiert
- NO-GO-Seite (Nennmaß + 5%): darf NICHT einführbar sein → Bohrung nicht aufgeweitet

#### 6.1.3 Risssuche

**Visuelle Inspektion (Lupe 10×):**
- Effektiv für oberflächliche Risse >0,5mm Länge
- Gute Beleuchtung essenziell (LED-Taschenlampe im spitzen Winkel)
- Besonders an Spannungskonzentrationen suchen (Radien, Bohrungsränder)

**Farbeindringprüfung (Penetrant Testing, PT):**
- Findet Risse ab ca. 0,1mm Länge
- Kostengünstig, kann vom geschulten Eigner durchgeführt werden
- PT-Set: Reiniger, Eindringmittel (rot), Entwickler (weiß) — ca. €25–40
- Einwirkzeit: 15–30 Minuten (Herstellerangabe beachten)
- Dokumentation durch Foto zwingend

**Magnetische Rissprüfung (MT):**
- NUR für ferromagnetische Werkstoffe (Stahl, NICHT Edelstahl 316L!)
- Für austenitischen Edelstahl nicht geeignet
- Relevant nur bei verzinkten Kettenverbindern

**Ultraschallprüfung (UT):**
- Für dickwandige Bauteile (>5mm)
- Findet Innenrisse und Materialfehler
- Erfordert Fachpersonal (UT Stufe 2)
- Für Standard-Verbinder selten erforderlich

#### 6.1.4 Visuelle Indikatoren

| Indikator | Bedeutung | Dringlichkeit |
|-----------|-----------|---------------|
| Roststreifen aus Bolzenbohrung | Spaltkorrosion aktiv | HOCH — sofort inspizieren |
| Rostpunkte auf Oberfläche | Lochfraß | MITTEL — W2 einplanen |
| Matte Oberfläche gleichmäßig | Normale Passivierung | NIEDRIG — normal |
| Glänzende Reibspuren | Abrasiver Verschleiß | MITTEL — messen |
| Bläuliche Anlauffarben | Überhitzung (Reibung) | HOCH — Galling-Prüfung |
| Schwarze Verfärbung (Edelstahl) | Schwefelbad/biologisch | MITTEL — reinigen und schützen |
| Grünspan | Kupfer/Bronze-Korrosion | NIEDRIG — kosmetisch |
| Weiße Kristalle | Aluminium-Korrosion | HOCH — galvanische Korrosion! |
| Dunkelbraune Ablagerungen | Crevice Corrosion Produkte | HOCH — sofort inspizieren |
| Risse (auch haarfein) | Ermüdung oder SCC | KRITISCH — sofort ersetzen |
| Verformung (Aufweitung) | Überlastung | HOCH — Ursache klären |
| Geräusche (Knarzen, Knacken) | Reibung, lockere Teile | MITTEL — inspizieren |

### 6.2 Austauschkriterien (Go/No-Go)

#### 6.2.1 Universelle Austauschgrenzen

| Kriterium | Grenzwert | Quelle |
|-----------|-----------|--------|
| Bolzendurchmesser-Reduktion | >5% vom Nennmaß | Rigger-Standard, Herstellerempfehlung |
| Bohrungsdurchmesser-Zunahme | >5% vom Nennmaß | Rigger-Standard |
| Ovalität (Bolzen oder Bohrung) | >0,3mm | AYDI-Empfehlung |
| Risstiefe (PT/UT bestätigt) | >0,1mm | Sofort ersetzen |
| Gabelaufweitung (Toggle) | >1,0mm über Nennmaß | Rigger-Standard |
| Oberflächenpitting-Dichte | >5 Pits/cm² mit Ø >0,5mm | AYDI-Empfehlung |
| Federbruch (Schnappschäkel) | Jeder Bruch | Sofort ersetzen |
| Federkraft-Reduktion | >30% gegenüber Neuzustand | Herstellerempfehlung |
| Soft-Schäkel Durchmesserreduktion | >10% | Herstellerempfehlung |
| Korrosionstiefe | >10% der Wandstärke | DIN/EN-Standard |
| Galling-Fläche | >25% der Kontaktfläche | AYDI-Empfehlung |
| Alter (stehendes Gut) | >15 Jahre | Versicherungs-Standard |
| Alter (laufendes Gut) | >10 Jahre | Versicherungs-Standard |
| Alter (Soft-Schäkel) | >4 Jahre (Deck, UV) | Herstellerempfehlung |

> **Confidence: measured/documented** — Zusammengestellt aus Herstellervorgaben (Wichard, Tylaska, Seldén), Rigger-Standards, DIN-Normen

#### 6.2.2 Herstellerspezifische Austauschkriterien

**Wichard HR-Schäkel:**
- Bolzenbohrung: Austausch bei >0,2mm Ovalisierung
- Bügel: Austausch bei sichtbarer Verformung oder Riss
- Selbstsicherungsmechanismus: Austausch bei Funktionsverlust
- Maximales Alter: 15 Jahre (Empfehlung)

**Tylaska T-Serie Schnappschäkel:**
- Federkraft: Austausch unter 70% des Neuwerts
- Nase: Austausch bei >0,5mm Abrieb an der Rastkante
- Gehäuse: Austausch bei sichtbarer Verformung
- Feder: Austausch alle 2 Jahre oder bei jedem Federbruch
- Maximales Alter: 8 Jahre

**Harken Snap Shackle:**
- Federachse: Austausch bei sichtbarem Abrieb
- Nase: Austausch bei Funktionsstörung (kein sicheres Einrasten)
- Gehäuse: Austausch bei Riss oder Verformung
- Feder: Austausch bei nachlassender Kraft
- Maximales Alter: 8 Jahre

**Ronstan Wirbel:**
- Lagerspiel axial: >0,8mm → Austausch
- Lagerspiel radial: >0,3mm → Austausch
- Drehwiderstand: spürbar rau → Service oder Austausch
- Gabelaugen: Riss → soforter Austausch
- Maximales Alter: 12 Jahre

### 6.3 Dokumentation von Verschleißbefunden

Jeder Verschleißbefund muss dokumentiert werden — für das Wartungslog, für Versicherungszwecke und für die AYDI-Zustandsbewertung.

**Mindestdokumentation pro Befund:**
1. Datum und Uhrzeit
2. Verbinder-Identifikation (Position, Typ, Hersteller, Alter)
3. Art des Befundes (Verschleiß, Korrosion, Riss, Verformung)
4. Messwerte (wenn zutreffend)
5. Foto(s) mit Maßstab
6. Bewertung (OK / Beobachten / Ersetzen)
7. Durchgeführte Maßnahme
8. Nächster Inspektionstermin
9. Name des Prüfers

---

## 7. Anlagen-spezifische Wartung

### 7.1 Stehendes Gut (Rigging)

Das stehende Gut trägt die höchsten statischen Lasten an Bord und unterliegt gleichzeitig dauernder Wechselbelastung durch Seegang und Windböen. Verbinder im stehenden Gut sind die kritischste Verbindergruppe.

**Besonderheiten:**
- Hohe statische Vorlast (Riggspannung)
- Zusätzliche dynamische Lasten (Seegang, Böen)
- Schwer zugänglich (Masttop, Saling, Bugspriet)
- Salzwasser-Exposition permanent
- Ermüdung ist der dominante Versagensmechanismus

**Spezifische Wartungsmaßnahmen:**
- Toggle-Rissinspektion bei jeder Mastlegung
- T-Terminal-Inspektion: Übergang Draht/Terminal besonders beachten
- Wantenspanner-Gewinde: Anti-Seize zwingend, jährlich erneuern
- Masttop-Verbinder: Inspektion nur bei Mastlegung oder Bosunstuhl
- Vorstag-Schäkel: Besonders belastet (Segeldruck + Vorstag-Spannung)

**Empfohlene Zusatzmaßnahmen:**
- Farbeindringprüfung aller Toggles und Terminals alle 5 Jahre
- Bolzenmessung aller Rigg-Verbinder jährlich
- Dokumentation in Rigg-Logbuch mit Fotos
- Rigg-Check durch zertifizierten Rigger vor Blauwasser-Reise

### 7.2 Laufendes Gut (Running Rigging)

Verbinder im laufenden Gut (Fallen, Schoten, Niederholer) unterliegen häufigerer Bewegung und geringerer statischer Last, aber höherem Abriebverschleiß.

**Besonderheiten:**
- Häufiges Öffnen/Schließen (Schnappschäkel)
- Abrieb durch Tauwerk-Kontakt
- UV-Exposition (Decksmontage)
- Geringere statische Last, aber hohe dynamische Spitzen
- Leichtere Bauweise → geringere Reserven

**Spezifische Wartungsmaßnahmen:**
- Schnappschäkel: Wöchentlicher Funktionstest, vierteljährliche Federprüfung
- Fallenschäkel: Monatliche Sichtprüfung auf Abrieb am Mast-Einlauf
- Schotenblöcke-Schäkel: Monatliche Drehgängigkeitsprüfung
- Soft-Schäkel: Wöchentliche Sichtprüfung, monatlicher Durchmesser-Check

### 7.3 Ankersystem

Ankerketten-Verbinder sind permanent Salzwasser ausgesetzt und unterliegen hohen dynamischen Lasten (Schwojen, Wellenschlag, Ankermanöver).

**Besonderheiten:**
- Permanente Salzwasser-Immersion
- Hohe dynamische Lasten (Ankerschock)
- Mechanischer Abrieb (Ankerwinde, Kettennuss, Meeresgrund)
- Schwer zugänglich während des Ankerns
- Sicherheitskritisch: Ankerverlust = Strandungsgefahr

**Spezifische Wartungsmaßnahmen:**
- Wirbelschäkel Anker/Kette: Vierteljährliche Inspektion und Schmierung
- Ketten-Vorläufer-Verbindung: Halbjährliche Inspektion
- Ankerwirbel: Vierteljährliche Schmierung, jährliche Demontage
- Kettenstopper-Bolzen: Monatliche Prüfung
- Ankerwinden-Kettenführung: Auf Abrieb der Kette durch Fehlausrichtung prüfen

### 7.4 Spinnaker-/Gennaker-System

Spinnaker- und Gennaker-Verbinder unterliegen den höchsten dynamischen Belastungen und müssen unter Last sicher auslösbar sein.

**Besonderheiten:**
- Extreme dynamische Lasten (Böen in leichtem Segel)
- Muss unter Last auslösbar sein (Schnappschäkel, Trigger-Release)
- Sicherheitsrelevant: Unkontrolliertes Segel = Kenterrisiko
- Häufiges Setzen/Bergen → hoher Betätigungsverschleiß
- Salzwasser-Spray und UV-Exposition

**Spezifische Wartungsmaßnahmen:**
- Spinnaker-Schnappschäkel: Funktionstest vor jedem Einsatz
- Barberholer-Schnappschäkel: Monatliche Inspektion
- Spi-Fall-Wirbelschäkel: Halbjährliche Schmierung
- Trigger-Release-Systeme: Vierteljährliche Revision
- Top-Schäkel (Kopfbrett): Jährliche Inspektion und Messung

### 7.5 Davit- und Kransysteme (Superyacht)

Verbinder an Davit- und Kransystemen unterliegen besonderen Anforderungen, da sie Lasten über Personen und Wasser heben (Tender, Jet-Ski, Beiboot). Viele Flag-State-Administrationen schreiben jährliche Inspektionen durch zugelassene Surveyor vor.

**Besonderheiten:**
- Personengefährdung beim Heben (Tender mit Crew)
- Dynamische Lasten durch Seegang während des Hebevorgangs
- Salzwasser-Spritzwasser und UV-Exposition
- Behördliche Prüfpflicht (MCA, RINA, Lloyd's)
- Dokumentation für ISM-Code und Flaggenstaat erforderlich

**Spezifische Wartungsmaßnahmen:**
- Alle Schäkel und Bolzen: Vierteljährliche W2-Inspektion
- Jährliche W3-Inspektion durch zugelassenen Surveyor
- SWL-Markierung an jedem Verbinder muss lesbar sein
- Ersatz ausschließlich durch zertifizierte Bauteile (mit Zertifikat)
- Prüfprotokoll nach jeder Inspektion (behördliche Aufbewahrungspflicht 5 Jahre)
- Probelast-Test nach jedem Verbindertausch (1,25× SWL)

**Behördliche Anforderungen (Auswahl):**
- MCA (UK): MGN 332 (M+F) — LOLER-Regelwerk, jährliche Prüfung aller Hebevorrichtungen durch eine befähigte Person
- BG Verkehr (DE): See-Berufsgenossenschaft-Vorschriften
- RINA (IT): Regolamento per la classificazione delle navi
- DNV: Rules for Classification — Lifting Appliances

### 7.6 Sicherheitsausrüstung

Verbinder an Sicherheitsausrüstung (Rettungsinsel-Befestigung, Lifebelts, Sicherheitsleinen) müssen den höchsten Wartungsstandards genügen.

**Spezifische Anforderungen:**
- Rettungsinsel-Halteband: Schäkel jährlich inspizieren, Sicherung prüfen
- Lifeline-Verbinder: Monatliche Sichtprüfung, jährliche Messung
- Lifebelt-Karabiner: Vor jeder Nutzung Funktionstest
- Jack-Line-Schäkel: Saisonstart Inspektion, nach 5 Jahren tauschen
- MOB-Rettungsmittel-Befestigung: Monatliche Sichtprüfung

---

## 8. Fehlerbild-Atlas

### Fehlerbild W-01: Bolzenbruch durch Spaltkorrosion

**Beschreibung:** Schäkelbolzen bricht im Bereich der Bohrung. Bruchfläche zeigt Korrosionsprodukte (rotbraun), reduzierter Restquerschnitt. Häufig bei Bolzen, die über Jahre nicht gelöst wurden.

**Typische Anzeichen:**
- Roststreifen am Bohrungsaustritt (vor dem Bruch)
- Festsitzender Bolzen (der nie gelöst wurde)
- Bolzen lässt sich bei Demontage nur mit Gewalt lösen
- Sichtbare Querschnittsreduktion im Bohrungsbereich

**Ursache:** Spaltkorrosion in der Bohrung hat den Bolzenquerschnitt über Jahre reduziert. Der verbleibende Querschnitt reichte für die Betriebslast nicht mehr aus → Gewaltbruch.

**Betroffene Verbinder:** D-Schäkel, Bügelschäkel, Toggle-Bolzen, Wantenspanner-Bolzen

**Vermeidung:**
- Jährlich Bolzen lösen, reinigen, Anti-Seize erneuern
- Regelmäßige Bolzenmessung (Ø-Reduktion?)
- Süßwasserspülung nach Salzwasserkontakt

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: KRITISCH
- Häufigkeit: HÄUFIG (Top-3 Versagensursache)

### Fehlerbild W-02: Wirbel-Blockade durch Galling

**Beschreibung:** Wirbel lässt sich nicht mehr drehen. Beim Versuch, ihn zu lösen, verkanten die Lagerflächen und verschweißen kalt. Das Want/Fall kann sich nicht mehr frei ausrichten → Biegebelastung im Terminal.

**Typische Anzeichen:**
- Wirbel dreht sich nicht mehr frei
- Metallisch glänzende, aufgeraute Kontaktflächen
- Bläuliche Anlauffarben an den Lagerflächen
- Geräusche (Knirschen) bei erzwungener Drehung

**Ursache:** Edelstahl-auf-Edelstahl-Kontakt ohne ausreichende Schmierung. Salzwasser hat restliches Fett ausgewaschen. Korrosionsprodukte haben den Lagerspalt verengt.

**Betroffene Verbinder:** Alle Wirbel-Typen, besonders Gabel-Gabel und Gabel-Auge

**Vermeidung:**
- Halbjährliche Schmierung mit Marine-Fett
- Vierteljährlich Drehgängigkeit prüfen und betätigen
- Anti-Seize auf Achse bei Montage

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH
- Häufigkeit: HÄUFIG

### Fehlerbild W-03: Toggle-Ermüdungsbruch

**Beschreibung:** Toggle bricht an der Innenseite des Gabelradius. Der Bruch erfolgt ohne Vorwarnung (kein sichtbarer plastischer Verformungshinweis). Die Bruchfläche zeigt typisches Ermüdungsmuster: glatte Schwingbruchfläche mit Rastlinien und kleine, raue Restbruchfläche.

**Typische Anzeichen (vor dem Bruch):**
- Haarfeine Risse an der Innenseite des Gabelradius (nur mit Lupe/PT sichtbar)
- Roststreifen aus Riss heraus
- Leichte Verfärbung an der Rissstelle

**Ursache:** Zyklische Biegebelastung hat an der Spannungskonzentration (Gabelradius) einen Ermüdungsriss initiiert. Der Riss ist über Monate/Jahre gewachsen, bis der Restquerschnitt für die Betriebslast nicht mehr ausreichte.

**Betroffene Verbinder:** Toggles an Unterwanten (höchste Wechsellast), Vorstag-Toggle, Achterstag-Toggle

**Vermeidung:**
- Farbeindringprüfung aller Toggles alle 3–5 Jahre
- Toggle-Gabeln visuell bei jeder Wartung inspizieren (Lupe)
- Toggles nach 10–15 Jahren altersbedingt tauschen
- Korrekte Dimensionierung (Sicherheitsfaktor ≥4:1)

**AYDI-Bewertung:**
- Confidence: measured
- Schweregrad: KRITISCH
- Häufigkeit: MITTEL (aber katastrophale Folgen)

### Fehlerbild W-04: Schnappschäkel öffnet unter Last

**Beschreibung:** Schnappschäkel öffnet sich unter Betriebslast unkontrolliert. Segel/Fall geht verloren. Kann durch Federmüdigkeit, Nasenabrieb oder Verformung des Gehäuses verursacht werden.

**Typische Anzeichen:**
- Feder fühlt sich "weich" an im Vergleich zu neuem Schäkel
- Nase rastet nur noch knapp ein
- Nase lässt sich ungewöhnlich leicht öffnen
- Gehäuse zeigt leichte Verformung

**Ursache:** Federmüdigkeit (häufigste), Nasenabrieb an der Rastkante, Verformung des Gehäuses durch Querlast, oder Kombination aller drei.

**Betroffene Verbinder:** Alle Schnappschäkel, besonders Spinnaker- und Gennaker-Schäkel

**Vermeidung:**
- Federtausch alle 2–3 Jahre
- Vierteljährliche Federprüfung (subjektive Kraft)
- Jährliche Federkraftmessung (Regatta)
- Nase auf Abrieb prüfen

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH
- Häufigkeit: HÄUFIG

### Fehlerbild W-05: Splint-Versagen und Bolzenverlust

**Beschreibung:** Splint oder Federstecker versagt, Bolzen arbeitet sich heraus, Verbindung löst sich. Kann bei allen bolzengesicherten Verbindungen auftreten.

**Typische Anzeichen:**
- Verlorener/gebrochener Splint (oft erst beim Versagen bemerkt)
- Federstecker herausgefallen
- Bolzen teilweise herausgewandert
- Bolzen komplett verloren → Verbindung getrennt

**Ursache:** Korrodierter Splint, ermüdeter Federstecker, vibrationsbedingtes Herauswandern, ungenügendes Umbiegen der Splintschenkel.

**Betroffene Verbinder:** Alle bolzengesicherten Verbindungen

**Vermeidung:**
- Monatliche Sichtprüfung aller Splinte und Federstecker
- Jährlicher Tausch aller Splinte
- Splinte korrekt umbiegen (≥90°)
- Federstecker maximal 3× wiederverwenden
- Edelstahl 316L für Splinte (kein Messing, kein verzinkter Stahl)

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH (abhängig von Position)
- Häufigkeit: HÄUFIG

### Fehlerbild W-06: Galvanische Korrosion an Mischmetall-Verbindung

**Beschreibung:** An der Kontaktstelle zwischen zwei unterschiedlichen Metallen zeigt sich beschleunigte Korrosion am unedleren Partner. Typisch: Edelstahlschäkel auf Aluminium-Mastbeschlag → Aluminium wird weiß und porös.

**Typische Anzeichen:**
- Weiße, pulvrige Ablagerungen (Aluminium)
- Rotbraune Verfärbung (Stahl/Eisen)
- Grünspan (Kupfer/Bronze)
- Materialverlust am unedleren Partner
- Bolzen festsitzend durch Korrosionsprodukte

**Ursache:** Potentialdifferenz zwischen Metallen erzeugt galvanische Zelle in Salzwasser. Das unedlere Metall (Anode) opfert sich.

**Betroffene Verbinder:** Alle Mischmetall-Verbindungen, besonders Edelstahl/Aluminium

**Vermeidung:**
- Galvanische Isolation (Tef-Gel, Duralac, Nylon-Buchsen)
- Materialgleichheit anstreben
- Regelmäßige Inspektion der Kontaktstellen
- Opferanoden in kritischen Bereichen

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: MITTEL bis HOCH
- Häufigkeit: HÄUFIG

### Fehlerbild W-07: Soft-Schäkel UV-Degradation

**Beschreibung:** Soft-Schäkel (Dyneema) verliert Festigkeit durch UV-Strahlung. Oberfläche vergraut, wird spröde und fasert auf. Kann zum Bruch unter Betriebslast führen.

**Typische Anzeichen:**
- Deutliche Vergrauung gegenüber Neuzustand
- Oberfläche fühlt sich rau und spröde an
- Einzelne Fasern stehen ab (Aufrieb)
- Durchmesser hat abgenommen (Querschnittsverlust)
- Knoten sitzt lockerer als im Neuzustand

**Ursache:** UV-Strahlung bricht die Polymerketten des UHMWPE (Dyneema). Der Prozess ist kumulativ und irreversibel. Tropische Sonne beschleunigt den Prozess um Faktor 2–3.

**Betroffene Verbinder:** Alle Soft-Schäkel in UV-exponierter Position

**Vermeidung:**
- UV-Schutzüberzüge verwenden
- Soft-Schäkel nach 2–4 Jahren tauschen (je nach UV-Exposition)
- Bei Nichtgebrauch abdecken oder entfernen
- Farbige Dyneema-Hüllen bieten leichten UV-Schutz

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH
- Häufigkeit: HÄUFIG (bei Soft-Schäkeln auf Deck)

### Fehlerbild W-08: Wantenspanner-Gewinde festgefressen (Galling)

**Beschreibung:** Wantenspanner-Gewinde (Spannschraube) lässt sich nicht mehr drehen. Beim Versuch, ihn mit Gewalt zu lösen, fressen die Gewindeflanken und der Spanner wird unbrauchbar.

**Typische Anzeichen:**
- Spanner lässt sich trotz gelöster Kontermutter nicht drehen
- Metallische Geräusche (Knirschen) bei Drehversuch
- Sichtbare Galling-Spuren am Gewinde
- Gewindegänge sind aufgeworfen

**Ursache:** Edelstahl-auf-Edelstahl-Gewinde ohne Anti-Seize. Salzwassereintritt hat die Restschmierung ausgewaschen. Korrosionsprodukte haben das Gewinde blockiert.

**Betroffene Verbinder:** Wantenspanner (Turnbuckles), Spannschrauben allgemein

**Vermeidung:**
- Anti-Seize (Tef-Gel) bei jeder Montage und jährlich erneuern
- Wantenspanner mindestens jährlich bewegen (eindrehen/ausdrehen)
- Gewinde vor dem Zusammenbau reinigen
- Bronze- oder Nitronic-60-Spannschrauben verwenden (weniger Galling-anfällig)

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH
- Häufigkeit: SEHR HÄUFIG (Top-Wartungsproblem)

### Fehlerbild W-09: Schäkel-Überlastungsverformung

**Beschreibung:** Schäkelbügel ist sichtbar aufgebogen, Bolzenbohrung ovalisiert. Tritt nach einmaliger Überlastung (Sturmschaden, Grundberührung mit Anker) oder schleichend durch Dauerlast über der Auslegung auf.

**Typische Anzeichen:**
- Bügel steht erkennbar offen (Spalt zwischen Bolzenkopf und Bügel)
- Bolzen lässt sich leichter als normal lösen (Bohrung aufgeweitet)
- Bügel zeigt Verformung in Lastrichtung
- Bolzen zeigt Biegung

**Ursache:** Betriebslast hat die Streckgrenze des Materials überschritten. Einmalige Überlastung oder kumulative Plastizierung durch dauerhaft zu hohe Arbeitslast.

**Betroffene Verbinder:** Unterdimensionierte Schäkel, Schäkel am Ankersystem, Schäkel an Abschleppverbindungen

**Vermeidung:**
- Korrekte Dimensionierung (Sicherheitsfaktor ≥4:1 bzgl. Bruchlast)
- Jährliche Sichtprüfung auf Verformung
- Nach Sturm/Notmanöver alle belasteten Schäkel inspizieren
- Nie den nächstkleineren Schäkel verwenden ("passt schon")

**AYDI-Bewertung:**
- Confidence: measured
- Schweregrad: KRITISCH
- Häufigkeit: MITTEL

### Fehlerbild W-10: Wirbelachse abgeschert

**Beschreibung:** Die Achse eines Wirbels ist abgeschert. Die beiden Hälften (Gabel oben/unten) sind getrennt. Die Bruchfläche zeigt entweder Ermüdung (glatt + rau) oder Gewaltbruch (vollständig rau mit Verformung).

**Typische Anzeichen (vor dem Bruch):**
- Wirbel hat übermäßiges Spiel
- Metallische Geräusche
- Sichtbare Risse an der Achse (Farbeindringprüfung)

**Ursache:** Ermüdung der Achse (häufigste), Überlastung, oder Korrosion + Ermüdung.

**Betroffene Verbinder:** Wirbel am stehenden Gut, Ankerwirbel, Masthead-Wirbel

**Vermeidung:**
- Regelmäßige Inspektion des Achsspiels
- NDT-Prüfung alle 5 Jahre
- Altersbedingter Tausch nach 8–12 Jahren
- Korrekte Dimensionierung

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: KRITISCH
- Häufigkeit: SELTEN (aber katastrophale Folgen)

### Fehlerbild W-11: Ankerwirbel-Blockade durch Muschelbewuchs

**Beschreibung:** Ankerketten-Wirbel ist durch Muschel-/Seepockenbewuchs blockiert. Die Kette kann sich beim Schwojkreis nicht frei drehen → Kette verknäult sich, Ankerhaltkraft sinkt.

**Typische Anzeichen:**
- Wirbel dreht sich nicht frei
- Sichtbarer Bewuchs auf Wirbel
- Kette verdreht sich beim Schwojen
- Erhöhte Spannung in der Kette bei Wind-/Strömungswechsel

**Ursache:** Biologischer Bewuchs in warmem Wasser (>15°C), besonders bei langer Liegezeit am selben Ankerplatz.

**Betroffene Verbinder:** Ankerwirbel, Kettenverbinder

**Vermeidung:**
- Regelmäßiges Einholen und Reinigen (alle 2–4 Wochen in tropischen Gewässern)
- Anti-Fouling-Anstrich auf Wirbel (Kupfer-basiert)
- Wirbel vierteljährlich demontieren und reinigen

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: MITTEL
- Häufigkeit: HÄUFIG (tropische/subtropische Gewässer)

### Fehlerbild W-12: Falsche Schäkel-Sicherung (Montagefehler)

**Beschreibung:** Schäkelbolzen ist nicht korrekt gesichert: Splint fehlt, Federstecker falsch eingesetzt, Selbstsicherung nicht angezogen, Drahtwicklung gelöst. Kann zur Lösung des Bolzens und Verbindungstrennung führen.

**Typische Anzeichen:**
- Fehlender oder gebrochener Splint
- Lose Federstecker
- Offene Selbstsicherungsschraube (Wichard HR)
- Fehlende Drahtwicklung (Ankerschäkel)
- Bolzen steht teilweise heraus

**Ursache:** Unachtsamkeit bei der Montage, fehlende Ersatz-Splinte, Unkenntnis der korrekten Sicherungsmethode, oder Splint/Federstecker wurde bei letzter Wartung vergessen.

**Betroffene Verbinder:** Alle bolzengesicherten Verbinder

**Vermeidung:**
- Checkliste bei jeder Montage verwenden
- Ausreichend Ersatz-Splinte an Bord
- Wartungsprotokoll führen (Punkt "Sicherung geprüft")
- Gegenseitige Kontrolle (Vier-Augen-Prinzip bei kritischen Verbindungen)

**AYDI-Bewertung:**
- Confidence: documented
- Schweregrad: HOCH
- Häufigkeit: HÄUFIG (häufigster Montagefehler)

---

## 9. Troubleshooting-Entscheidungsbäume

### Entscheidungsbaum T-01: Festsitzender Bolzen

```
Bolzen lässt sich nicht lösen
├── Kriechöl auftragen, 30 Min einwirken
│   ├── Bolzen löst sich → Spaltkorrosion war Ursache
│   │   ├── Bolzen reinigen, messen
│   │   ├── Wenn Ø-Reduktion <5% → Anti-Seize, weiter verwenden
│   │   └── Wenn Ø-Reduktion ≥5% → Bolzen ersetzen
│   └── Bolzen löst sich NICHT
│       ├── Erwärmen (Heißluft, max. 200°C, NICHT am Segel/Tauwerk!)
│       │   ├── Bolzen löst sich → wie oben weiter
│       │   └── Bolzen löst sich NICHT
│       │       ├── Austreiben mit Messingdorn + Hammer
│       │       │   ├── Bolzen löst sich → stark korrodiert, ERSETZEN
│       │       │   └── Bolzen bricht → Galling → Schäkel KOMPLETT ersetzen
│       │       └── Falls kein Zugang für Dorn:
│       │           └── Rigger/Werft einschalten
│       └── NIEMALS: Stahlhammer direkt auf Edelstahlbolzen!
└── Bei Wantenspanner-Gewinde: NICHT mit Rohrzange!
    └── Passenden Gabelschlüssel verwenden oder Rigger rufen
```

### Entscheidungsbaum T-02: Wirbel dreht nicht

```
Wirbel dreht sich nicht frei
├── Reinigung versuchen (Süßwasser + Spülmittel)
│   ├── Dreht nach Reinigung → Salzablagerungen/leichter Bewuchs
│   │   └── Schmieren und weiter verwenden, Intervall verkürzen
│   └── Dreht NICHT nach Reinigung
│       ├── Wirbel zerlegbar?
│       │   ├── JA → Demontieren
│       │   │   ├── Lagerflächen inspizieren
│       │   │   ├── Galling (glänzende, aufgeraute Flächen)?
│       │   │   │   ├── Leicht → Glätten (Scotch-Brite), Anti-Seize, weiter
│       │   │   │   └── Stark → Wirbel ersetzen
│       │   │   ├── Korrosion in Lagerspalt?
│       │   │   │   ├── Oberflächlich → Reinigen, schmieren
│       │   │   │   └── Tiefgehend/Pitting → Wirbel ersetzen
│       │   │   └── Kugellager defekt?
│       │   │       ├── Ersatzlager verfügbar → Lager tauschen
│       │   │       └── Kein Ersatz → Wirbel komplett tauschen
│       │   └── NEIN → Kriechöl + vorsichtig bewegen
│       │       ├── Löst sich → Schmieren, weiter verwenden, Intervall verkürzen
│       │       └── Löst sich NICHT → Wirbel ersetzen
│       └── Blockade durch Bewuchs? (Ankerwirbel)
│           └── Mechanisch entfernen, reinigen, schmieren
```

### Entscheidungsbaum T-03: Schnappschäkel rastet nicht ein

```
Schnappschäkel rastet nicht sicher ein
├── Nase prüfen: Abrieb sichtbar?
│   ├── JA, Rastkante abgenutzt
│   │   ├── Abrieb >0,5mm → Schnappschäkel ersetzen
│   │   └── Abrieb <0,5mm → Feder prüfen (unten)
│   └── NEIN, Nase sieht gut aus
│       ├── Feder prüfen: Federkraft ausreichend?
│       │   ├── Feder weich/gebrochen → Feder ersetzen (Originalteil!)
│       │   ├── Feder OK → Gehäuse prüfen
│       │   │   ├── Gehäuse verformt → Schnappschäkel ersetzen
│       │   │   └── Gehäuse OK → Verschmutzung?
│       │   │       ├── JA → Reinigen, Teflon-Spray, testen
│       │   │       └── NEIN → Zusammenbaufehler? Korrekt montiert?
│       │   └── Federkraft nicht beurteilbar → Vergleich mit Neuem
│       └── Nase blockiert / klemmt
│           ├── Korrosion an Achse → Reinigen, schmieren
│           ├── Fremdkörper → Entfernen
│           └── Verformung → Schnappschäkel ersetzen
```

### Entscheidungsbaum T-04: Korrosion an Verbinder entdeckt

```
Korrosion an Verbinder entdeckt
├── Art der Korrosion bestimmen:
│   ├── Gleichmäßig matt → Normale Passivierungsänderung
│   │   └── Kein Handlungsbedarf, beobachten
│   ├── Einzelne Punkte (Pitting)
│   │   ├── <5 Pits/cm², <0,5mm Tiefe → Beobachten, Korrosionsschutz
│   │   └── >5 Pits/cm² oder >0,5mm → Verbinder ersetzen
│   ├── In Spalt/Bohrung (Crevice)
│   │   ├── Bolzen lösen, Bohrung inspizieren
│   │   ├── Oberflächlich → Reinigen, Anti-Seize, Intervall halbieren
│   │   └── Tiefgehend (>10% Wandstärke) → Verbinder ersetzen
│   ├── An Materialkontakt (galvanisch)
│   │   ├── Materialien identifizieren
│   │   ├── Isolation nachrüsten (Tef-Gel, Buchse)
│   │   ├── Betroffenes Teil: Querschnitt noch ausreichend?
│   │   │   ├── JA → Isolieren und weiter verwenden
│   │   │   └── NEIN → Ersetzen + Isolation
│   │   └── Ursache der fehlenden Isolation beheben
│   └── Risse (SCC verdacht)
│       ├── SOFORT aus dem Einsatz nehmen
│       ├── NDT-Prüfung (PT oder UT)
│       ├── Riss bestätigt → Ersetzen + Materialupgrade erwägen (Duplex)
│       └── Kein Riss → Oberfläche behandeln, Intervall verkürzen
└── Dokumentieren! (Foto, Position, Art, Maßnahme)
```

### Entscheidungsbaum T-05: Verdacht auf Ermüdungsriss

```
Verdacht auf Ermüdungsriss (visuelle Anomalie, Geräusch, Alter)
├── Verbinder sofort entlasten (wenn möglich)
├── Visuelle Inspektion mit 10× Lupe
│   ├── Riss sichtbar
│   │   ├── SOFORT ersetzen
│   │   ├── Keine provisorische Reparatur — Rissgröße nimmt exponentiell zu
│   │   └── Gesamtes Rigg prüfen lassen (gleiche Generation?)
│   ├── Kein Riss sichtbar, aber Verdacht bleibt
│   │   ├── Farbeindringprüfung durchführen
│   │   │   ├── Anzeige gefunden → Ersetzen
│   │   │   └── Keine Anzeige → Verbinder kann weiter verwendet werden
│   │   │       └── Inspektionsintervall auf 1 Jahr verkürzen
│   │   └── Keine PT-Möglichkeit → im Zweifel ersetzen
│   └── Geräusch, aber kein Sichtbefund
│       ├── Ursache des Geräuschs suchen (lose Teile? Reibung?)
│       ├── Wenn Ursache unklar → PT oder Surveyor
│       └── Wenn Ursache gefunden (z.B. loser Splint) → beheben
└── Blauwasser/Offshore: Im Zweifel IMMER ersetzen
```

---

## 10. FAQ — Häufige Fragen

### F-01: Wie oft muss ich die Verbinder meiner Yacht warten?

**Antwort:** Das hängt von Bootstyp, Einsatzgebiet und Verbindertyp ab. Als Faustregel: Monatliche Sichtprüfung (W1) aller zugänglichen Verbinder während der Saison, jährliche Detailinspektion (W2) bei der Einwinterung, und alle 3–5 Jahre eine Fachinspektion (W3) durch einen Rigger. Für Blauwasseryachten und Regattaboote gelten verkürzte Intervalle. Die genauen Intervalle finden Sie in Kapitel 3.

> **Confidence: documented**

### F-02: Welches Anti-Seize soll ich für Edelstahl-Schäkel verwenden?

**Antwort:** Tef-Gel ist die beste Wahl für Edelstahl-auf-Edelstahl-Verbindungen im Salzwasser. Es bietet hervorragenden Galling-Schutz und galvanische Isolation. Lanocote ist eine gute, preiswertere Alternative für den allgemeinen Korrosionsschutz. Für Edelstahl-auf-Aluminium-Verbindungen ist Duralac oder Tef-Gel zu empfehlen. Details in Kapitel 5.

> **Confidence: measured**

### F-03: Mein Wantenspanner lässt sich nicht drehen — was tun?

**Antwort:** NICHT mit Gewalt versuchen! Kriechöl (WD-40, Caramba) an beiden Gewindeenden auftragen und mindestens 30 Minuten einwirken lassen. Dann mit zwei passenden Gabelschlüsseln (gegenhalten!) vorsichtig versuchen. Wenn das nicht hilft, erwärmen (Heißluftfön, max. 200°C) und erneut versuchen. Wenn auch das scheitert, muss ein Rigger den Spanner eventuell absägen. Ursache ist fast immer fehlendes Anti-Seize — bei der Neumontage unbedingt Tef-Gel verwenden. Siehe Entscheidungsbaum T-01.

> **Confidence: documented**

### F-04: Wann muss ich einen Schäkel ersetzen?

**Antwort:** Sofort ersetzen bei: Rissen (jeder Art), Bolzendurchmesser-Reduktion >5%, Bohrungsovalisierung >5%, sichtbarer Verformung des Bügels, starkem Pitting (>5 Pits/cm² >0,5mm), oder wenn der Schäkel älter als 15 Jahre ist (stehendes Gut) bzw. 10 Jahre (laufendes Gut). Details in Kapitel 6.2.

> **Confidence: measured/documented**

### F-05: Wie erkenne ich Spaltkorrosion an einem Schäkelbolzen?

**Antwort:** Typische Anzeichen sind: Rostbraune Streifen am Bohrungsaustritt, Bolzen lässt sich schwer lösen (obwohl er das sollte), und beim Lösen zeigen sich rotbraune Korrosionsprodukte. Im fortgeschrittenen Stadium ist der Bolzen sichtbar dünner im Bohrungsbereich. Prävention: Jährlich Bolzen lösen, reinigen und Anti-Seize erneuern. Siehe Kapitel 2.2.2 und Fehlerbild W-01.

> **Confidence: documented**

### F-06: Sind Soft-Schäkel eine gute Alternative zu Stahlschäkeln?

**Antwort:** Soft-Schäkel (Dyneema) bieten Vorteile bei Gewicht (80% leichter), Segel- und Personenschutz (kein Schlag bei Halse), und Korrosionsfreiheit. Nachteile sind UV-Empfindlichkeit (Lebensdauer 2–4 Jahre auf Deck), Abrieb-Anfälligkeit und die Notwendigkeit korrekter Knoten. Für laufendes Gut und Segelverbindungen sind sie oft die bessere Wahl. Für stehendes Gut und Ankerverbindungen sind Stahlschäkel vorzuziehen. Wartung: Wöchentliche Sichtprüfung auf Abrieb und UV-Schäden.

> **Confidence: documented**

### F-07: Kann ich einen gebrochenen Schnappschäkel-Feder provisorisch reparieren?

**Antwort:** Nein, nicht sinnvoll. Ohne intakte Feder rastet die Nase nicht sicher ein. Provisorisch kann man den Schnappschäkel durch einen D-Schäkel mit Bolzen und Splint ersetzen. Auf keinen Fall einen Schnappschäkel mit defekter Feder weiterverwenden — die Nase kann unter Last aufspringen. Ersatzfedern vom Hersteller kosten €5–15 und sollten an Bord vorrätig sein.

> **Confidence: documented**

### F-08: Muss ich bei der Einwinterung die Verbinder besonders behandeln?

**Antwort:** Ja. Bei der Einwinterung empfehlen wir: (1) Alle zugänglichen Verbinder mit Süßwasser spülen und trocknen, (2) Schäkelbolzen lösen, reinigen, messen und Anti-Seize erneuern, (3) Wirbel schmieren, (4) Schnappschäkel-Federn prüfen, (5) Alle Splinte und Federstecker inspizieren und bei Bedarf tauschen, (6) Korrosionsschutz (Lanocote) auf alle exponierten Verbinder auftragen, (7) Alle Befunde dokumentieren und Wartungsbedarf für die nächste Saison notieren.

> **Confidence: documented**

### F-09: Wie prüfe ich einen Toggle auf Ermüdungsrisse?

**Antwort:** Visuelle Inspektion mit 10× Lupe bei guter Beleuchtung (LED im spitzen Winkel). Fokus auf die Innenseite der Gabelradien — dort entstehen Ermüdungsrisse zuerst. Auf haarfeine Linien und Roststreifen achten. Für eine zuverlässigere Prüfung: Farbeindringprüfung (PT) durchführen — PT-Sets kosten ca. €25–40 und können vom geschulten Eigner selbst angewendet werden. Detaillierte Anleitung in Kapitel 4.6.

> **Confidence: documented**

### F-10: Welches Schmierfett ist für Wirbel geeignet?

**Antwort:** Marine-Schmierfett auf Lithium-Komplex-Basis mit PTFE-Zusatz (z.B. Harken Winch Grease, Lewmar Winch Grease). Kein normales Autofett — dieses ist nicht salzwasserbeständig. Für Kugellager-Wirbel: synthetisches Kugellager-Fett. KEIN Silikon-Spray für belastete Lager. Details in Kapitel 5.1.2.

> **Confidence: documented**

### F-11: Wie lange halten Rigg-Verbinder?

**Antwort:** Richtwerte für die Lebensdauer (gut gewartet, gemäßigtes Klima): Schäkel stehendes Gut 10–15 Jahre, Schäkel laufendes Gut 8–10 Jahre, Wirbel 8–12 Jahre, Toggles 10–15 Jahre, Schnappschäkel 5–8 Jahre, Soft-Schäkel 2–4 Jahre (Deck). In tropischen Gewässern verkürzen sich diese Werte um 30–50%. Bei Regattaeinsatz um 40–60%. Diese Werte gelten unabhängig vom optischen Zustand — auch ein optisch einwandfreier Verbinder kann durch innere Ermüdung geschwächt sein.

> **Confidence: estimated**

### F-12: Darf ich Edelstahl-Verbinder mit einer Stahldrahtbürste reinigen?

**Antwort:** NEIN! Eine Stahldrahtbürste hinterlässt Eisenpartikel auf der Edelstahloberfläche, die als Korrosionskeime wirken und Rostflecken verursachen ("Fremdrost"). Verwenden Sie ausschließlich Nylonbürsten, Bronzedrahtbürsten oder Edelstahl-Drahtbürsten (die aus dem gleichen Material wie der zu reinigende Verbinder bestehen). Für verzinkte Ketten und Stahl-Verbinder ist eine Stahldrahtbürste dagegen in Ordnung.

> **Confidence: measured**

### F-13: Was kostet ein kompletter Verbinder-Service am Rigg?

**Antwort:** Orientierungswerte (Fahrtensegler 10–14m, Stand 2026):
- Eigener Service (Material): €50–100 (Anti-Seize, Splinte, Schmiermittel)
- Rigger-Inspektion W3: €400–800 (halber Tag, ohne Mastlegung)
- Rigger-Inspektion W3 mit Mastlegung: €1.200–2.500 (inkl. Kran)
- Kompletttausch alle Rigg-Verbinder: €2.000–5.000 (Material + Arbeit)
- Zum Vergleich: Riggversagen durch mangelhafte Verbinder: €15.000–50.000+ Schaden

> **Confidence: estimated** — Marktpreise 2026, regionale Unterschiede möglich

### F-14: Mein Ankerschäkel dreht sich mit — wie verhindere ich das?

**Antwort:** Ein sich drehender Ankerschäkel bedeutet, dass der Bolzen nicht festsitzt und sich unter Last lösen kann. Maßnahmen: (1) Bolzen mit Drahtwicklung (Mousing Wire) aus 316L-Draht sichern, (2) Bolzen mit Loctite 243 (mittelfest) sichern, (3) Einen selbstsichernden Schäkel verwenden (z.B. Wichard HR), (4) Bolzen so einsetzen, dass die Gewindepartie am Kettenglieder anliegt (verhindert Abschrauben durch Kettenbewegung).

> **Confidence: documented**

### F-15: Kann ich einen verformten Schäkel wieder geradbiegen?

**Antwort:** NEIN! Ein verformter Schäkel hat seine Streckgrenze überschritten. Das Material ist plastisch verformt und durch Kaltverfestigung versprödet. Rückbiegen würde die Versprödung verstärken und zum Bruch führen. Verformte Schäkel sofort ersetzen. Die Ursache der Überlastung muss analysiert werden — ggf. größeren Schäkel wählen.

> **Confidence: measured**

### F-16: Wie transportiere und lagere ich Ersatzverbinder korrekt?

**Antwort:** Verbinder in trockener, verschlossener Box aufbewahren. Gewinde und Bolzen dünn mit Lanocote/Tef-Gel einstreichen. Verschiedene Metalle getrennt lagern (galvanische Korrosion auch im Trockenen möglich durch Kondenswasser). Soft-Schäkel UV-geschützt aufbewahren. Beschriftung mit Typ, Größe und Kaufdatum. Auf Blauwasseryachten: kompletten Satz Ersatzverbinder für alle kritischen Positionen mitführen.

> **Confidence: documented**

### F-17: Soll ich Splinte oder Federstecker verwenden?

**Antwort:** Für sicherheitskritische Verbindungen (stehendes Gut, Ankerkette) sind Splinte (Biegesplinte) vorzuziehen — sie können sich nicht selbsttätig lösen. Federstecker (R-Clips) sind für weniger kritische, häufig zu lösende Verbindungen akzeptabel (laufendes Gut, Decksbeschläge). In der Superyacht- und Offshore-Praxis werden zunehmend selbstsichernde Systeme (Wichard HR, Schnellverschlussbolzen) verwendet.

> **Confidence: documented**

### F-18: Mein Wirbel macht Geräusche — ist das gefährlich?

**Antwort:** Kommt auf das Geräusch an: (1) Leises Klicken bei Drehung → Kugellager, normal, (2) Knirschen → Sand/Salz in Lagerspalt, reinigen und schmieren, (3) Knarzen unter Last → Galling beginnt, sofort demontieren und schmieren, (4) Metallisches Knacken → potentiell gefährlich, könnte Riss sein. Bei Geräusch (3) oder (4): Wirbel entlasten und inspizieren. Im Zweifel Rigger konsultieren.

> **Confidence: documented**

### F-19: Wie sichere ich Verbinder gegen Diebstahl?

**Antwort:** Diebstahl von Verbindern ist leider ein reales Problem, besonders bei hochwertigen Titanschäkeln und Tylaska-Schnappschäkeln. Maßnahmen: (1) Bolzen mit Loctite 271 (hochfest) sichern — kann nur mit Wärme gelöst werden, (2) Nicht-Standard-Sicherungen verwenden (Torx statt Innensechskant), (3) Markierung/Gravur mit Bootsname, (4) Versicherung über Yachtkaskoversicherung, (5) Bei Langzeitliegeplatz: wertvolle Beschläge demontieren.

> **Confidence: documented**

### F-20: Wie dokumentiere ich Verbinder-Wartung für den Surveyor?

**Antwort:** Ein gutes Wartungslog enthält für jeden Verbinder: (1) Position und Identifikation, (2) Typ, Hersteller, Modell, Größe, (3) Einbaudatum und Kaufbeleg, (4) Wartungshistorie mit Datum, Befund, Maßnahme, (5) Messwerte (Bolzendurchmesser, Verschleißmaße), (6) Fotos (mindestens jährlich), (7) Nächster Inspektionstermin. Surveyor akzeptieren zunehmend digitale Dokumentation. Die AYDI-Plattform kann diese Dokumentation automatisch verwalten.

> **Confidence: documented**

### F-21: Was ist der Unterschied zwischen Tef-Gel und Tef-Gel HD?

**Antwort:** Tef-Gel Standard ist ein dünnflüssiges Gel für allgemeine Anti-Seize-Anwendungen (Bolzen, leichte Gewinde). Tef-Gel HD (Heavy Duty) ist dickflüssiger und für größere Gewinde (Wantenspanner, Kielbolzen) und höhere Belastungen optimiert. Für Standard-Schäkelbolzen reicht Tef-Gel Standard. Für Wantenspanner und große Bolzen empfehlen wir Tef-Gel HD.

> **Confidence: measured**

### F-22: Wie entsorge ich ausgetauschte Edelstahl-Verbinder korrekt?

**Antwort:** Edelstahl ist zu 100% recycelbar und hat einen Materialwert. Ausgetauschte Verbinder können beim Schrotthändler (Edelstahl-Fraktion) abgegeben werden. NICHT in den Hausmüll. Verbinder mit Korrosionsschutzpasten (Duralac enthält Chromat!) als Sondermüll behandeln oder vor Abgabe reinigen. Alte Soft-Schäkel können im Restmüll entsorgt werden (Dyneema ist Polyethylen).

> **Confidence: documented**

### F-23: Kann ich Verbinder verschiedener Hersteller mischen?

**Antwort:** Grundsätzlich ja, solange (1) das Material identisch ist (alles 316L oder alles Titan — nicht mischen ohne Isolation), (2) die Dimensionen zueinander passen (Bolzendurchmesser, Gabelweite, Bohrungsabstand), und (3) die Tragfähigkeit des schwächsten Gliedes die Anforderung erfüllt. In der Praxis bewährt es sich, pro System (z.B. stehendes Gut) einen Hersteller zu verwenden — das erleichtert Ersatzteilbeschaffung und Wartung.

> **Confidence: documented**

### F-24: Wie prüfe ich die Tragfähigkeit eines gebrauchten Verbinders?

**Antwort:** Eine zuverlässige Tragfähigkeitsprüfung ist nur durch einen Zugversuch (destruktiv) oder eine kalibierte Belastungsprüfung (Prüfstand) möglich. Im Feld beschränkt sich die Beurteilung auf: (1) Visuelle Inspektion (Verformung, Risse, Korrosion), (2) Dimensionskontrolle (Querschnittsreduktion <5%?), (3) NDT (Farbeindringprüfung für Risse). Im Zweifel gilt: ersetzen. Ein neuer Schäkel kostet €5–50, ein Riggversagen €15.000+.

> **Confidence: documented**

### F-25: Was sind die häufigsten Fehler bei der Verbinder-Wartung?

**Antwort:** Die Top-10 Fehler:
1. Bolzen nie lösen ("war ja alles OK letzes Jahr")
2. Kein Anti-Seize verwenden
3. Alte Splinte wiederverwenden
4. Stahldrahtbürste auf Edelstahl
5. Falsches Schmiermittel (Autofett statt Marine-Fett)
6. Wantenspanner nie bewegen
7. Schnappschäkel-Federn nie prüfen
8. Soft-Schäkel als "wartungsfrei" betrachten
9. Mischmetalle ohne galvanische Isolation
10. Keine Dokumentation führen

> **Confidence: documented**

---

## 11. Glossar

### A

**Abrasion (Abrieb):** Mechanischer Materialabtrag durch Reibung zweier Oberflächen. Bei Verbindern relevant an Bolzen, Lagerflächen und Schnappschäkel-Nasen.

**Anti-Fouling:** Bewuchsverhindernder Anstrich. Bei Ankerketten-Wirbeln kann Anti-Fouling den Bewuchs reduzieren, der zur Wirbelblockade führt.

**Anti-Seize (Montagepaste):** Compound auf PTFE-, Lanolin- oder Metallbasis, der Galling und Korrosion an Gewindeverbindungen verhindert. Nicht zu verwechseln mit Schmierfett.

**Austenitisch:** Kristallstruktur von Edelstahl 316L. Nicht magnetisch. Anfällig für Spannungsrisskorrosion bei hohen Temperaturen in Chlorid-Umgebung.

### B

**Bolzenbohrung:** Die Durchgangsbohrung im Schäkelkörper, Toggle oder Beschlagauge, durch die der Verbindungsbolzen geführt wird. Kritische Stelle für Spaltkorrosion und Ermüdungsrissinitiierung.

**Bügelmessschraube (Mikrometer):** Präzisionsmessinstrument zur Bestimmung von Außenmaßen mit einer Genauigkeit von 0,01mm. Unverzichtbar für die Bolzenverschleißmessung.

**Bügelschäkel (Bow Shackle):** Schäkelform mit weiter, bogenförmiger Öffnung. Auch Omega-Schäkel genannt. Erlaubt mehrere Anschlagpunkte.

### C

**CE-Kennzeichnung:** Konformitätskennzeichnung für Produkte im europäischen Wirtschaftsraum. Für Yachtverbinder relevant durch die Maschinenrichtlinie und die Freizeitbootrichtlinie.

**Crevice Corrosion:** Siehe Spaltkorrosion.

### D

**D-Schäkel (Dee Shackle):** Schäkelform in D-Form. Der am häufigsten verwendete Schäkeltyp. Kompakt, hohe Tragfähigkeit bei axialer Belastung.

**Dauerfestigkeit:** Belastungsgrenze, unterhalb derer ein Werkstoff theoretisch unendlich viele Lastzyklen übersteht. Für Edelstahl 316L geschmiedet bei ca. 15% der Bruchlast.

**Duralac:** Handelsname für eine Montage- und Isolierpaste auf Bariumchromat-Basis (Spezifikation DTD 369B). Bietet hervorragende galvanische Isolation zwischen Aluminium und Edelstahl.

**Duplex-Stahl:** Edelstahl mit gemischter austenitisch-ferritischer Struktur (z.B. SAF 2205). Höhere Festigkeit und bessere Korrosionsbeständigkeit als 316L. Zunehmend im Superyacht-Rigging.

**Dyneema:** Markenname für Ultra-High-Molecular-Weight-Polyethylene (UHMWPE) Fasern der Firma DSM. Basis für Soft-Schäkel und Hightech-Tauwerk.

### E

**Ermüdung (Fatigue):** Werkstoffversagen durch zyklische (wechselnde) Belastung unterhalb der statischen Festigkeit. Beginnt mit Mikrorissbildung an Spannungskonzentrationen.

**Ermüdungsriss:** Riss, der durch zyklische Belastung entstanden ist. Typisches Erscheinungsbild: glatte Schwingbruchfläche mit Rastlinien (Beachmarks) und raue Restbruchfläche.

### F

**Farbeindringprüfung (PT, Penetrant Testing):** Zerstörungsfreie Prüfmethode zum Nachweis von Oberflächenrissen. Eindringmittel (rot) dringt in Risse ein und wird durch weißen Entwickler sichtbar gemacht.

**Federstecker (R-Clip, Beta Pin):** Federnd vorgespannter Sicherungsstift für Bolzenverbindungen. Schneller zu montieren als Biegesplinte, aber weniger sicher (kann sich durch Vibration lösen).

**Fressen:** Siehe Galling.

### G

**Gabelkopf (Clevis):** U-förmiges Bauteil mit Querbohrung zur Aufnahme eines Bolzens. Grundelement von Toggles und Wantenspannern.

**Galling (Fressen, Kaltverschweißen):** Adhäsiver Verschleißmechanismus, bei dem zwei metallische Oberflächen unter Druck und Relativbewegung lokal kaltverschweißen. Besonders problematisch bei Edelstahl/Edelstahl-Paarungen.

**Galvanische Korrosion:** Beschleunigte Korrosion des unedleren Metalls in einer elektrochemischen Zelle, die durch den Kontakt zweier verschiedener Metalle in einem Elektrolyten (Salzwasser) entsteht.

**Go/No-Go-Lehrdorn:** Prüfwerkzeug mit zwei kalibrierten Durchmessern. Der "Go"-Teil muss in die Bohrung passen, der "No-Go"-Teil darf nicht passen. Einfache Methode zur Bohrungsverschleißprüfung.

### H

**Hochlast-Schnappschäkel (Hi-Load Snap Shackle):** Schnappschäkel für hohe Lasten, z.B. Spinnaker-Systeme. Robustere Bauweise, stärkere Feder, präziserer Rastmechanismus als Standard-Schnappschäkel.

### I

**Inspektion:** Systematische Prüfung eines Bauteils auf Zustand, Funktion und Sicherheit. Abgestuft in visuelle Inspektion (W1), Detailinspektion (W2) und Fachinspektion (W3).

### K

**Kaltverschweißen:** Siehe Galling.

**Korrosionsermüdung:** Zusammenwirken von Korrosion und Ermüdung. Die Wechselwirkung ist überproportional — die Kombination ist deutlich schädlicher als die Summe der Einzeleffekte.

**Korrosionsprodukte:** Durch Korrosion gebildete Verbindungen (Oxide, Hydroxide, Salze). Bei Edelstahl: rotbraun (Eisenoxid), bei Aluminium: weiß (Aluminiumoxid), bei Kupfer/Bronze: grün (Kupfercarbonat).

**Kriechöl (Penetrating Oil):** Niedrigviskoses Öl mit hohem Kriechvermögen. Dringt in enge Spalte und Gewindegänge ein. Verwendung zum Lösen festsitzender Bolzen (WD-40, Caramba, Kroil).

### L

**Lanocote:** Handelsname für ein Korrosionsschutzmittel auf Lanolin-Basis (Wollwachs). Natürlich wasserabweisend, gute Kriechfähigkeit, universeller Korrosionsschutz für marine Anwendungen.

**Lastzyklen:** Anzahl der Belastungswechsel, denen ein Bauteil ausgesetzt wird. Entscheidend für die Ermüdungslebensdauer. Im Rigg: 10.000–1.000.000 Zyklen pro Jahr je nach Position.

**Lehrdorn:** Kalibriertes Prüfwerkzeug zur Messung von Bohrungs-Innendurchmessern. Für Verbinder: Go/No-Go-Lehrdorn zur Verschleißprüfung.

**Lochfraß (Pitting):** Lokale Korrosionsform, bei der kleine, tiefe Löcher in der Metalloberfläche entstehen. Beginnt an Schwachstellen der Passivschicht.

### M

**Messschieber (Caliper):** Messinstrument zur Bestimmung von Außen-, Innen- und Tiefenmaßen. Für Verbinderwartung: digitaler Messschieber mit 0,02mm Genauigkeit.

**Mikrometer:** Siehe Bügelmessschraube.

**Mousing Wire (Sicherungsdraht):** Dünner Edelstahldraht (0,8–1,2mm), der durch Bolzenbohrung und um Schäkelbügel gewickelt wird, um den Bolzen gegen Herausdrehen zu sichern. Standard bei Ankerketten-Verbindern.

### N

**NDT (Non-Destructive Testing, Zerstörungsfreie Prüfung):** Oberbegriff für Prüfverfahren, die ein Bauteil nicht beschädigen. Bei Verbindern relevant: Farbeindringprüfung (PT), Magnetpulverprüfung (MT), Ultraschallprüfung (UT).

**Nitronic 60:** Austenitischer Edelstahl (UNS S21800) mit hervorragender Galling-Resistenz. Wird für Bolzen und Buchsen verwendet, die gegen Edelstahl 316L laufen.

### O

**Ovalität (Ovality):** Abweichung einer Bohrung oder eines Bolzens von der idealen Kreisform. Gemessen als Differenz zwischen größtem und kleinstem Durchmesser. Bei Verbindern: >0,3mm = Austauschgrenze.

### P

**Passivschicht:** Dünne, transparente Chromoxidschicht (3–5nm) auf Edelstahloberflächen. Schützt das darunterliegende Metall vor Korrosion. Kann durch Beschädigung, Spaltbedingungen oder Chloride zerstört werden.

**Pitting:** Siehe Lochfraß.

**PT (Penetrant Testing):** Siehe Farbeindringprüfung.

### R

**Rastlinien (Beach Marks):** Konzentrische Linien auf Ermüdungsbruchflächen, die den Fortschritt des Risswachstums über die Zeit markieren. Diagnostisches Merkmal für Ermüdungsversagen.

### S

**SCC (Stress Corrosion Cracking):** Siehe Spannungsrisskorrosion.

**Schnappschäkel (Snap Shackle):** Schäkel mit federbelasteter Nase, die ohne Werkzeug geöffnet werden kann. Für schnelles Setzen/Bergen von Segeln. Sicherheitskritisch: Nase muss unter Last zuverlässig einrasten.

**Soft-Schäkel:** Verbinder aus hochfestem Fasergewebe (Dyneema/UHMWPE). Leicht, korrosionsfrei, segel- und personenschonend. Begrenzte Lebensdauer durch UV und Abrieb.

**Spaltkorrosion (Crevice Corrosion):** Korrosionsform, die in engen Spalten auftritt (Bolzen/Bohrung, unter Ablagerungen). Im Spalt verarmt der Sauerstoff, Chloride konzentrieren sich, pH sinkt → aggressive Korrosionsbedingungen.

**Spannungskonzentration (Stress Concentration):** Lokale Erhöhung der mechanischen Spannung an geometrischen Übergängen (Bohrungsrand, Kerbgrund, Radius). Beschrieben durch den Faktor Kt. Typische Werte bei Verbindern: 2,0–5,0.

**Spannungsrisskorrosion (SCC):** Rissbildung durch Zusammenwirken von Zugspannung, korrosivem Medium und empfindlichem Material. Bei Edelstahl 316L relevant in heißen, chloridhaltigen Umgebungen (>50°C).

**Splint (Cotter Pin, Split Pin):** Drahtförmiges Sicherungselement aus weichem Edelstahl. Wird durch Querbohrung im Bolzen geführt und umgebogen. Einmal-Bauteil — nach Entfernen IMMER ersetzen.

### T

**Tef-Gel:** Handelsname für eine Anti-Seize- und Korrosionsschutzpaste auf PTFE-Basis (Fluoropolymer). Standard in der Marine-Industrie für Edelstahl/Edelstahl- und Edelstahl/Aluminium-Verbindungen.

**Toggle:** Gabelförmiges Zwischenstück zwischen Wantterminal und Wantenspanner/Mastbeschlag. Ermöglicht winklige Ausrichtung und verhindert Biegebelastung des Terminals. Ermüdungskritisches Bauteil.

### U

**UHMWPE (Ultra-High-Molecular-Weight Polyethylene):** Hochmolekulares Polyethylen, Grundmaterial für Dyneema und Spectra. Extrem zugfest, chemisch beständig, aber UV-empfindlich.

**Ultraschallprüfung (UT):** NDT-Verfahren, bei dem Ultraschallwellen durch das Material geschickt werden. Reflektionen an Rissen und Fehlstellen werden detektiert. Für dickwandige Verbinder (>5mm) geeignet.

### V

**Verschleißgrenze:** Maximaler zulässiger Materialverlust, ab dem ein Bauteil ersetzt werden muss. Bei Verbindern typisch: 5% Querschnittsreduktion.

### W

**Wantenspanner (Turnbuckle, Rigging Screw):** Verstellbare Spannvorrichtung im stehenden Gut. Gewinde müssen regelmäßig mit Anti-Seize behandelt werden, um Galling zu verhindern.

**Wöhler-Kurve (S-N Curve):** Diagramm, das die ertragbare Lastamplitude über der Anzahl der Lastzyklen darstellt. Grundlage für die Ermüdungsbeurteilung von Verbindern.

### Z

**Zerstörungsfreie Prüfung:** Siehe NDT.

---

## 12. Schnell-Referenz

### Wartungs-Kurzanleitung

| Was | Wann | Wie | Womit |
|-----|------|-----|-------|
| Sichtprüfung alle Verbinder | Monatlich | Augenschein + Funktionstest | Lupe 10×, LED-Lampe |
| Bolzen lösen und reinigen | Jährlich | Ausbauen, messen, Anti-Seize | Messschieber, Tef-Gel |
| Wirbel schmieren | Alle 6 Monate | Demontieren, reinigen, fetten | Marine-Fett |
| Splinte erneuern | Jährlich | Alle Splinte tauschen | Neue 316L-Splinte |
| Schnappschäkel-Feder | Saisonal | Federkraft prüfen | Vergleich mit Neuem |
| Toggle-Rissprüfung | Alle 3–5 Jahre | Farbeindringprüfung | PT-Set |
| Soft-Schäkel UV-Check | Wöchentlich | Sichtprüfung Oberfläche | Vergleich mit Neuem |

### Austausch-Kurzreferenz

| Verbinder | Ersetzen wenn... |
|-----------|------------------|
| Schäkel | Ø-Reduktion >5%, Risse, Verformung, >15 Jahre |
| Wirbel | Axialspiel >1mm, Galling tief, Riss, >12 Jahre |
| Bolzen | Ø-Reduktion >5%, Ovalität >0,3mm, Riefen >0,1mm |
| Splint | IMMER nach Entfernen ersetzen |
| Federstecker | Verformung, Korrosion, oder nach 3× Gebrauch |
| Schnappschäkel | Feder defekt, Nase abgenutzt, >8 Jahre |
| Toggle | Riss (jeder!), Gabelaufweitung >1mm, >15 Jahre |
| Soft-Schäkel | UV-Degradation sichtbar, Ø-Reduktion >10%, >4 Jahre |

### Anti-Seize Kurzreferenz

| Material-Paarung | Produkt | Auftrag |
|-----------------|---------|---------|
| Edelstahl/Edelstahl | Tef-Gel | Dünn auf Bolzen/Gewinde |
| Edelstahl/Aluminium | Duralac oder Tef-Gel | Dünn auf Kontaktflächen |
| Edelstahl/Bronze | Lanocote | Dünn auf Kontaktflächen |
| Gewinde allgemein | Tef-Gel | In Gewindegänge |
| Allg. Korrosionsschutz | Lanocote | Dünn auf alle Oberflächen |

### Notfall-Kurzreferenz

| Problem | Sofortmaßnahme |
|---------|---------------|
| Bolzen gebrochen | Ersatzschäkel/-bolzen, zur Not Soft-Schäkel |
| Schnappschäkel öffnet | Durch D-Schäkel + Splint ersetzen |
| Toggle gerissen | Sofort Rigg entlasten! Notfall-Toggle oder Soft-Verbindung |
| Wirbel blockiert | Kriechöl, NICHT mit Gewalt drehen |
| Splint verloren | Sofort neuen einsetzen, zur Not Kabelbinder (temporär!) |

---

## ANHANG A — Fallstudien

### Fallstudie A-1: Riggversagen durch korrodierten Vorstag-Toggle

**Yacht:** Bavaria 40 Cruiser, BJ 2012, Ostsee
**Schadensjahr:** 2024
**Situation:** Beim Aufkreuzen in 25 kn Wind bricht der Vorstag-Toggle. Vorstag fällt, Mast steht nur noch auf Wanten. Kein Personenschaden.

**Befund:** Toggle war seit Werftauslieferung 2012 nie inspiziert worden (12 Jahre). Ermüdungsriss an der Innenseite des Gabelradius, durch Spaltkorrosion beschleunigt. Riss war von außen als feiner Roststreifen erkennbar — wurde vom Eigner als "normaler Rost" abgetan.

**Ursache:** Fehlende Wartung (nie W2 oder W3 durchgeführt). Toggle-Radien waren ab Werk scharf (kleiner Radius = hohe Spannungskonzentration). Kombination aus Korrosionsermüdung und ungünstiger Geometrie.

**Schaden:** Toggle €45, Vorstag mit Terminal €800, Bergung und Reparatur €4.500, Saison-Ausfall €3.000 (geschätzt). Gesamt: ca. €8.345.

**Lehre:** Jährliche Toggle-Inspektion (W2) und 5-jährliche PT-Prüfung (W3) hätte den Riss frühzeitig erkannt. Kostenpunkt der Prävention: €50/Jahr (Eigenwartung) oder €200/5 Jahre (Rigger-PT).

**AYDI-Bewertung:** Confidence: documented (Surveyor-Bericht, Fotos)

### Fallstudie A-2: Spinnaker-Verlust durch ermüdete Schnappschäkel-Feder

**Yacht:** J/109, Regattaeinsatz, Nordsee
**Schadensjahr:** 2025
**Situation:** Beim Halsen in 18 kn Wind öffnet sich der Spinnaker-Schnappschäkel am Spi-Fall. Spinnaker geht ins Wasser, wird unter dem Boot durchgezogen und reißt.

**Befund:** Schnappschäkel (Tylaska T12) war 6 Jahre alt. Die Feder hatte nur noch ca. 40% der Originalfederkraft. Die Nase rastete zwar noch ein, aber die Haltekraft reichte bei der dynamischen Belastung der Halse nicht aus.

**Ursache:** Keine regelmäßige Federprüfung. Tylaska empfiehlt Federtausch alle 2 Jahre bei Regattaeinsatz.

**Schaden:** Schnappschäkel €120, Spinnaker €4.800, Reparatur Bugkorb €600. Gesamt: ca. €5.520.

**Lehre:** Vierteljährliche Federprüfung (Vergleich mit neuem Schäkel) und 2-jährlicher Federtausch (€15/Feder). Gesamtkosten Prävention: ca. €30/Jahr.

**AYDI-Bewertung:** Confidence: documented (Regattateam-Bericht)

### Fallstudie A-3: Ankerverlust durch galvanische Korrosion

**Yacht:** Hallberg-Rassy 372, Langfahrt, Karibik
**Schadensjahr:** 2023
**Situation:** Beim Ankeraufholen bricht die Ketten-Anker-Verbindung. Der Anker (Delta 20kg) geht mit 5m Kette auf 12m Tiefe verloren.

**Befund:** Der Schäkel (verzinkter Stahl) zwischen Edelstahlkette und Edelstahlanker war durch galvanische Korrosion massiv geschwächt. Die Zinkschicht war vollständig aufgelöst, der darunterliegende Stahl war stark korrodiert. Wandstärkenreduktion >60%.

**Ursache:** Verzinkter Schäkel in Kontakt mit Edelstahl → galvanische Zelle. In tropischem Salzwasser (28°C) extrem beschleunigt. Keine galvanische Isolation, keine regelmäßige Inspektion.

**Schaden:** Anker €280, Kette 5m €150, Taucheinsatz (erfolglos) €200, neuer Anker + Kette + Schäkel €500. Gesamt: ca. €1.130.

**Lehre:** Ankerschäkel MUSS aus dem gleichen Material wie die Kette sein (Edelstahl 316L) oder durch galvanische Isolation geschützt werden. In tropischen Gewässern vierteljährliche Inspektion.

**AYDI-Bewertung:** Confidence: documented (Eigner-Bericht, Fotos)

### Fallstudie A-4: Mastbruch durch festgefressenen Wirbel

**Yacht:** Swan 48, Mittelmeer-Regatta
**Schadensjahr:** 2024
**Situation:** Bei Kursänderung unter Spi bricht der Mast auf Salinghöhe. Ursache: Das Vorstag konnte einem seitlichen Zug nicht folgen, weil der Masttop-Wirbel festgefressen war (Galling). Die resultierende Querlast auf das Terminal führte zum Terminalbruch, der Mast knickte.

**Befund:** Wirbel (12 Jahre alt) war nie geschmiert worden. Edelstahl-auf-Edelstahl-Lagerflächen komplett verschweißt (Galling). Wirbel ließ sich auch mit Werkzeug nicht mehr drehen.

**Ursache:** Fehlende Schmierung über 12 Jahre. Kein Anti-Seize bei der Installation. Salzwasser hat jegliche Restschmierung ausgewaschen.

**Schaden:** Mast, Rigg, Segel, Elektronik: ca. €85.000. Bergung: €8.000. Saisonausfall: €15.000. Gesamt: ca. €108.000.

**Lehre:** Halbjährliche Wirbelschmierung (€5 Fett + 20 Min Arbeit pro Jahr) hätte diesen Totalschaden verhindert.

**AYDI-Bewertung:** Confidence: documented (Surveyor-Bericht, Versicherungsakte)

### Fallstudie A-5: Wantenspanner-Blockade durch fehlendes Anti-Seize

**Yacht:** Beneteau Oceanis 45, Charteryacht, Griechenland
**Schadensjahr:** 2025
**Situation:** Bei der Rigg-Inspektion vor der Saison lässt sich kein einziger Wantenspanner drehen. Alle 8 Spanner sind festgefressen. Rigg-Tuning unmöglich, Yacht nicht einsatzfähig.

**Befund:** Wantenspanner (7 Jahre alt) wurden bei der Erstmontage ohne Anti-Seize eingebaut und seitdem nie bewegt. Alle Gewinde zeigen Galling. 6 von 8 Spannern konnten durch Wärme + Kriechöl gelöst werden, 2 mussten abgesägt werden.

**Ursache:** Werft hat bei Erstmontage kein Anti-Seize verwendet. Charterbetrieb hat keine regelmäßige Rigg-Wartung durchgeführt.

**Schaden:** 2 neue Wantenspanner: €600, Rigger-Arbeit (2 Tage): €1.600, Saisonstart-Verzögerung: €2.000 (entgangene Charter). Gesamt: ca. €4.200.

**Lehre:** Tef-Gel bei Erstmontage + jährliches Bewegen der Spanner. Kosten: €15 Tef-Gel + 30 Min/Jahr.

**AYDI-Bewertung:** Confidence: documented (Charter-Management-Bericht)

### Fallstudie A-6: Soft-Schäkel Bruch durch UV-Degradation

**Yacht:** Dehler 38, Performance Cruiser, Mittelmeer
**Schadensjahr:** 2024
**Situation:** Beim Bergen des Gennakers bricht der Soft-Schäkel am Kopfbrett. Gennaker geht ins Wasser, wird durch die Bugwelle überspült, Boot segelt über den Gennaker.

**Befund:** Soft-Schäkel (Marlow Dyneema SK78, 5mm) war 4 Jahre alt und permanent UV-exponiert am Kopfbrett des Gennakers montiert. Oberfläche stark vergraut, Fasern deutlich aufgerieben, Durchmesser um 15% reduziert. Bruchlast war auf geschätzte 30–40% des Neuwerts gesunken.

**Ursache:** UV-Degradation über 4 Jahre in Mittelmeer-Sonne (>2000 UV-Stunden/Jahr). Keine regelmäßige Inspektion.

**Schaden:** Gennaker: €3.200, Soft-Schäkel: €12, Reparatur Gennaker: unwirtschaftlich → Neukauf. Gesamt: ca. €3.212.

**Lehre:** Soft-Schäkel am Kopfbrett alle 2 Jahre tauschen (€12). UV-Schutzüberzug verwenden. Wöchentliche Sichtprüfung.

**AYDI-Bewertung:** Confidence: documented (Eigner-Bericht, Fotos)

### Fallstudie A-7: Systematischer Verbinder-Service rettet Blauwasser-Reise

**Yacht:** Amel 55, Blauwasser, Weltumsegelung
**Zeitraum:** 2022–2025
**Situation:** Eigner führt systematisches Wartungsprogramm durch (angelehnt an AYDI-Empfehlungen). Während der 3-jährigen Weltumsegelung kein einziger Verbinder-bezogener Ausfall.

**Wartungsprogramm:**
- Monatliche W1-Sichtprüfung aller 147 dokumentierten Verbinder
- Vierteljährliche W2-Inspektion (Bolzen lösen, messen, schmieren)
- Jährliche W3-Inspektion (PT an Toggles und Terminals)
- Alle Soft-Schäkel nach 2 Jahren getauscht
- Schnappschäkel-Federn nach 2 Jahren getauscht
- Komplettes Wartungslog mit Fotos und Messwerten

**Befunde während der Reise:**
- 3 Bolzen vorzeitig getauscht (Ø-Reduktion 3–4% durch tropische Bedingungen)
- 1 Toggle vorzeitig getauscht (PT-Anzeige nach 2 Jahren in Tropen)
- 2 Wirbel vorzeitig getauscht (Spiel >0,5mm)
- 8 Soft-Schäkel getauscht (UV-Degradation)
- 4 Schnappschäkel-Federn getauscht

**Kosten des Wartungsprogramms:** ca. €400/Jahr (Material) + ca. 40 Stunden/Jahr (Eignerarbeit).

**Lehre:** Systematische Wartung funktioniert. Die Investition steht in keinem Verhältnis zu den potenziellen Schadenskosten.

**AYDI-Bewertung:** Confidence: documented (Eigner-Logbuch, 3 Jahre Daten)

### Fallstudie A-8: Kran-Schäkel-Versagen bei Tender-Lift

**Yacht:** Superyacht 35m, Mittelmeer
**Schadensjahr:** 2024
**Situation:** Beim Heben des 800kg-Tenders bricht ein Schäkel am Krangeschirr. Tender fällt aus 2m Höhe auf Deck, erheblicher Sachschaden, Crew-Mitglied leicht verletzt.

**Befund:** Schäkel (8mm D-Schäkel, WLL 1.000 kg) war korrekt dimensioniert. Aber: Der Bolzen wies starken Lochfraß auf (Pitting), der die tragende Querschnittsfläche um geschätzte 40% reduziert hatte. Der Schäkel war 8 Jahre alt und wurde nie inspiziert (W2 nie durchgeführt).

**Ursache:** Fehlende Wartung trotz sicherheitskritischer Anwendung (Personengefährdung). Kran-/Hebegeräte-Verbinder unterliegen eigentlich jährlicher Prüfpflicht.

**Schaden:** Tender-Reparatur: €35.000, Deck-Reparatur: €12.000, Personenschaden (ärztl. Behandlung): €2.000, Surveyor/Behörde: €5.000. Gesamt: ca. €54.000.

**Lehre:** Kran- und Hebegeschirr-Verbinder müssen vierteljährlich inspiziert und jährlich durch Fachpersonal geprüft werden. Bei Superyachten ist dies oft behördlich vorgeschrieben (Flag State).

**AYDI-Bewertung:** Confidence: documented (ISM-Audit-Bericht, Surveyor-Report)

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Connector Maintenance Models — Pydantic v2
File: backend/app/models/connector_maintenance.py

These models represent the data structures for connector maintenance
tracking, inspection records, and wear measurement within the AYDI platform.
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ConnectorType(str, Enum):
    """Types of marine connectors."""
    D_SHACKLE = "d_shackle"
    BOW_SHACKLE = "bow_shackle"
    SWIVEL_SHACKLE = "swivel_shackle"
    SNAP_SHACKLE = "snap_shackle"
    SOFT_SHACKLE = "soft_shackle"
    SWIVEL = "swivel"
    TOGGLE = "toggle"
    PIN = "pin"
    CLEVIS_PIN = "clevis_pin"
    TURNBUCKLE = "turnbuckle"


class ConnectorLocation(str, Enum):
    """Location categories for connectors on a yacht."""
    STANDING_RIGGING = "standing_rigging"
    RUNNING_RIGGING = "running_rigging"
    ANCHOR_SYSTEM = "anchor_system"
    SPINNAKER_SYSTEM = "spinnaker_system"
    SAFETY_EQUIPMENT = "safety_equipment"
    CRANE_LIFTING = "crane_lifting"
    DECK_HARDWARE = "deck_hardware"


class MaintenanceLevel(str, Enum):
    """Maintenance inspection levels."""
    W1_VISUAL = "w1_visual"
    W2_DETAIL = "w2_detail"
    W3_EXPERT = "w3_expert"
    W4_OVERHAUL = "w4_overhaul"


class ConditionRating(str, Enum):
    """Condition assessment ratings."""
    GOOD = "good"
    MONITOR = "monitor"
    REPLACE_SOON = "replace_soon"
    REPLACE_IMMEDIATELY = "replace_immediately"
    CONDEMNED = "condemned"


class CorrosionType(str, Enum):
    """Types of corrosion found on connectors."""
    NONE = "none"
    GENERAL = "general"
    PITTING = "pitting"
    CREVICE = "crevice"
    GALVANIC = "galvanic"
    SCC = "stress_corrosion_cracking"
    INTERGRANULAR = "intergranular"


class FailureMode(str, Enum):
    """Connector failure modes."""
    CORROSION = "corrosion"
    FATIGUE = "fatigue"
    OVERLOAD = "overload"
    GALLING = "galling"
    UV_DEGRADATION = "uv_degradation"
    ABRASION = "abrasion"
    SPRING_FAILURE = "spring_failure"
    PIN_LOSS = "pin_loss"
    ASSEMBLY_ERROR = "assembly_error"


class ConfidenceLevel(str, Enum):
    """Confidence levels for assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ConnectorIdentification(BaseModel):
    """Unique identification of a connector on a yacht."""

    model_config = {"from_attributes": True}

    connector_id: str = Field(
        ...,
        description="Unique identifier, e.g., 'WS_STB_UNT_01'",
        examples=["WS_STB_UNT_01", "SNAP_SPI_FALL_01"],
    )
    connector_type: ConnectorType
    location: ConnectorLocation
    position_description: str = Field(
        ...,
        description="Human-readable position description in German",
        examples=["Steuerbord Unterwant, Toggle unten"],
    )
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    material: str = Field(
        default="316L",
        description="Material designation",
    )
    nominal_diameter_mm: Optional[float] = None
    wll_kg: Optional[float] = Field(
        None,
        description="Working Load Limit in kg",
    )
    breaking_load_kg: Optional[float] = Field(
        None,
        description="Minimum Breaking Load in kg",
    )
    install_date: Optional[date] = None
    purchase_receipt: Optional[str] = None


class PinMeasurement(BaseModel):
    """Measurement record for a pin/bolt diameter check."""

    model_config = {"from_attributes": True}

    position: str = Field(
        ...,
        description="Measurement position: 'head', 'center', 'thread'",
    )
    diameter_0deg_mm: float = Field(
        ...,
        ge=0,
        description="Diameter measurement at 0 degrees",
    )
    diameter_90deg_mm: float = Field(
        ...,
        ge=0,
        description="Diameter measurement at 90 degrees",
    )

    @property
    def ovality_mm(self) -> float:
        """Calculate ovality as difference between axes."""
        return abs(self.diameter_0deg_mm - self.diameter_90deg_mm)

    @property
    def min_diameter_mm(self) -> float:
        """Return minimum measured diameter."""
        return min(self.diameter_0deg_mm, self.diameter_90deg_mm)


class WearAssessment(BaseModel):
    """Assessment of wear on a connector component."""

    model_config = {"from_attributes": True}

    component: str = Field(
        ...,
        description="Component assessed: 'pin', 'bore', 'body', 'fork', 'spring', 'nose'",
    )
    nominal_dimension_mm: float
    measured_dimension_mm: float
    reduction_percent: float = Field(
        ...,
        ge=0,
        description="Percentage reduction from nominal",
    )
    ovality_mm: Optional[float] = None
    condition: ConditionRating
    notes: Optional[str] = None


class CorrosionFinding(BaseModel):
    """Documentation of a corrosion finding."""

    model_config = {"from_attributes": True}

    corrosion_type: CorrosionType
    location_on_connector: str = Field(
        ...,
        description="Where on the connector corrosion was found",
    )
    severity: str = Field(
        ...,
        description="Severity: 'light', 'moderate', 'severe'",
    )
    depth_mm: Optional[float] = None
    area_percent: Optional[float] = Field(
        None,
        description="Percentage of surface affected",
    )
    photo_reference: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM


class InspectionRecord(BaseModel):
    """Complete inspection record for a connector."""

    model_config = {"from_attributes": True}

    inspection_id: str = Field(
        ...,
        description="Unique inspection identifier",
    )
    connector: ConnectorIdentification
    inspection_date: datetime
    maintenance_level: MaintenanceLevel
    inspector_name: str
    inspector_qualification: Optional[str] = None

    # Measurements
    pin_measurements: list[PinMeasurement] = Field(default_factory=list)
    wear_assessments: list[WearAssessment] = Field(default_factory=list)
    corrosion_findings: list[CorrosionFinding] = Field(default_factory=list)

    # Overall assessment
    overall_condition: ConditionRating
    lubrication_applied: Optional[str] = Field(
        None,
        description="Lubricant/anti-seize applied, e.g., 'Tef-Gel'",
    )
    pins_replaced: bool = False
    split_pins_replaced: bool = False
    spring_replaced: bool = False

    # Documentation
    photos: list[str] = Field(
        default_factory=list,
        description="List of photo file references",
    )
    notes: Optional[str] = None
    next_inspection_date: Optional[date] = None
    next_inspection_level: Optional[MaintenanceLevel] = None

    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class MaintenanceSchedule(BaseModel):
    """Maintenance schedule for a set of connectors."""

    model_config = {"from_attributes": True}

    yacht_id: str
    yacht_name: str
    boat_class: str
    sailing_area: str = Field(
        ...,
        description="Primary sailing area for interval adjustment",
    )
    connectors: list[ConnectorIdentification] = Field(default_factory=list)
    inspection_history: list[InspectionRecord] = Field(default_factory=list)

    # Schedule adjustments
    tropical_factor: float = Field(
        default=1.0,
        ge=0.3,
        le=1.0,
        description="Interval multiplier for tropical conditions (0.5 = half intervals)",
    )
    racing_factor: float = Field(
        default=1.0,
        ge=0.3,
        le=1.0,
        description="Interval multiplier for racing use",
    )
    charter_factor: float = Field(
        default=1.0,
        ge=0.3,
        le=1.0,
        description="Interval multiplier for charter use",
    )


class ConnectorFailureReport(BaseModel):
    """Report of a connector failure for pattern analysis."""

    model_config = {"from_attributes": True}

    report_id: str
    connector: ConnectorIdentification
    failure_date: datetime
    failure_mode: FailureMode
    failure_description: str
    consequences: str
    damage_cost_eur: Optional[float] = None
    root_cause_analysis: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    photos: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class ConnectorMaintenanceAnalysis(BaseModel):
    """AYDI analysis result for connector maintenance assessment."""

    model_config = {"from_attributes": True}

    yacht_id: str
    analysis_date: datetime
    total_connectors: int
    inspected_connectors: int
    overdue_inspections: int

    # Condition summary
    condition_good: int = 0
    condition_monitor: int = 0
    condition_replace_soon: int = 0
    condition_replace_immediately: int = 0
    condition_condemned: int = 0

    # Risk assessment
    overall_risk_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall risk score (0=safe, 100=critical)",
    )
    risk_factors: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)

    # Estimated costs
    immediate_replacement_cost_eur: Optional[float] = None
    annual_maintenance_cost_eur: Optional[float] = None
    deferred_risk_cost_eur: Optional[float] = Field(
        None,
        description="Estimated cost if maintenance is deferred",
    )

    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED
    data_completeness_percent: float = Field(
        ...,
        ge=0,
        le=100,
        description="How complete the underlying data is",
    )


class LubricantRecommendation(BaseModel):
    """Lubricant recommendation for a specific application."""

    model_config = {"from_attributes": True}

    application: str
    material_pairing: str
    recommended_product: str
    alternative_product: Optional[str] = None
    application_method: str
    reapplication_interval_months: int
    warnings: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class WearLimitTable(BaseModel):
    """Wear limit reference for a connector type."""

    model_config = {"from_attributes": True}

    connector_type: ConnectorType
    component: str
    nominal_dimension_mm: float
    monitor_threshold_percent: float = Field(
        default=2.0,
        description="Percent reduction triggering monitoring",
    )
    replace_threshold_percent: float = Field(
        default=5.0,
        description="Percent reduction requiring replacement",
    )
    max_ovality_mm: float = Field(
        default=0.3,
        description="Maximum allowed ovality",
    )
    max_age_years: Optional[int] = None
    source: str = Field(
        ...,
        description="Source of the limit values",
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
```

---

## ANHANG C — Inspektions-Checklisten

### Checkliste C-1: Monatliche Sichtprüfung (W1) — Alle Verbinder

```
AYDI Inspektions-Checkliste W1 — Monatliche Sichtprüfung
=========================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________ Wetter: ____________

STEHENDES GUT
□ Vorstag-Toggle: Sichtbare Risse? ___  Bolzensitz? ___
□ Achterstag-Toggle: Sichtbare Risse? ___  Bolzensitz? ___
□ Oberwant Bb: Toggle, Schäkel, Splinte OK? ___
□ Oberwant Stb: Toggle, Schäkel, Splinte OK? ___
□ Unterwant Bb: Toggle, Schäkel, Splinte OK? ___
□ Unterwant Stb: Toggle, Schäkel, Splinte OK? ___
□ Wantenspanner (alle): Splinte vorhanden? ___
□ Mastbeschläge (soweit sichtbar): Bolzen fest? ___

LAUFENDES GUT
□ Großfall-Schäkel: Bolzensitz, Sicherung? ___
□ Vorsegel-Fallenschäkel: Bolzensitz, Sicherung? ___
□ Spi-Fall-Schnappschäkel: Einrasten OK? ___
□ Großschot-Blöcke: Schäkel, Achsen OK? ___
□ Vorschot-Blöcke: Schäkel, Achsen OK? ___

ANKERSYSTEM
□ Anker-Ketten-Schäkel: Bolzen fest, Sicherung? ___
□ Kettenwirbel: Dreht frei? ___
□ Kettenstopper: Bolzen fest? ___

SICHERHEITSAUSRÜSTUNG
□ Lifeline-Verbinder: Zustand OK? ___
□ Rettungsinsel-Halteband: Schäkel OK? ___

BEFUNDE:
_____________________________________________
_____________________________________________

NÄCHSTE PRÜFUNG: ____________
```

### Checkliste C-2: Jährliche Detailinspektion (W2) — Schäkel

```
AYDI Inspektions-Checkliste W2 — Jährliche Schäkelinspektion
=============================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________ Messmittel: _________ (Kalibrierung: _______)

Schäkel-ID: _____________ Position: _____________
Hersteller: _____________ Modell: ______________
Nennmaß Bolzen: ______mm  Alter: ______ Jahre

BOLZEN-DEMONTAGE
□ Sicherung entfernt (Typ: __________)
□ Bolzen gelöst (Leichtgängig / Schwer / Festsitzend)
□ Falls festsitzend: Methode: _______________

BOLZEN-INSPEKTION
□ Korrosion: Keine / Leicht / Mittel / Schwer
□ Galling-Spuren: Keine / Leicht / Schwer
□ Riefen/Rillen: Keine / <0,1mm / >0,1mm
□ Pitting: Keine / Vereinzelt / Häufig
□ Risse: Keine / Verdacht / Sichtbar

BOLZEN-MESSUNG
Position | 0°      | 90°     | Ovalität | Reduktion
Kopf     | ____mm  | ____mm  | ____mm   | ____%
Mitte    | ____mm  | ____mm  | ____mm   | ____%
Gewinde  | ____mm  | ____mm  | ____mm   | ____%

BOHRUNG-INSPEKTION
□ Spaltkorrosion: Keine / Leicht / Schwer
□ Ovalisierung: Nicht messbar / Messbar: ____mm
□ Verfärbungen: Keine / Rostbraun / Andere: _______

SCHÄKELKÖRPER
□ Verformung: Keine / Leicht / Deutlich → ERSETZEN
□ Korrosion: Keine / Leicht / Mittel / Schwer
□ Risse: Keine / Verdacht → PT empfohlen

ZUSAMMENBAU
□ Anti-Seize aufgetragen (Produkt: ___________)
□ Bolzen eingesetzt
□ Neue Sicherung eingesetzt (Typ: ___________)
□ Korrekte Orientierung geprüft

BEWERTUNG: □ OK  □ Beobachten  □ Ersetzen
NÄCHSTE INSPEKTION: ____________ Stufe: W__
BEMERKUNGEN: ___________________________________
```

### Checkliste C-3: Schnappschäkel Saisonale Wartung (W2)

```
AYDI Inspektions-Checkliste W2 — Schnappschäkel
================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

Schnappschäkel-ID: _______ Position: _____________
Hersteller: _____________ Modell: ______________
Alter: ______ Jahre

FUNKTIONSTEST (VOR DEMONTAGE)
□ Nase rastet ein: Sicher / Unsicher / Nicht
□ Federkraft subjektiv: Kräftig / Normal / Schwach / Keine
□ Öffnen mit einer Hand: Ja / Nein (blockiert)
□ Geräusche: Keine / Klicken / Knirschen

DEMONTAGE
□ Federachse/Schraube entfernt
□ Feder ausgebaut (VORSICHT: Spannung!)
□ Alle Teile fotografiert

INSPEKTION
□ Feder: OK / Ermüdet / Gebrochen / Korrodiert
□ Nase (Rastkante): OK / Leichter Abrieb / Stark abgenutzt
□ Federachse: OK / Abrieb / Korrosion
□ Gehäuse: OK / Verformung / Riss
□ Rastpunkt (Gehäuse): OK / Abgenutzt

MESSUNG (falls zutreffend)
Nasen-Rastkante Abrieb: ____mm
Federkraft (Kraftmesser): ____N (Neuwert: ____N = ___%)

ZUSAMMENBAU
□ Feder: Alte weiterverwendet / Neue eingesetzt
□ Schmierung: Teflon-Spray auf Achse
□ Sicherung: Eingesetzt (Typ: ___________)
□ Funktionstest: 20× Auf/Zu → OK / Auffällig

BEWERTUNG: □ OK  □ Beobachten  □ Feder tauschen  □ Ersetzen
NÄCHSTE INSPEKTION: ____________
```

---

## ANHANG D — Verschleißgrenztabellen

### Tabelle D-1: Bolzen-Verschleißgrenzen nach Durchmesser

| Nenn-Ø (mm) | Monitor ab (mm) | Ersetzen ab (mm) | Max. Ovalität (mm) |
|-------------|----------------|-------------------|---------------------|
| 5,0 | 4,90 (2%) | 4,75 (5%) | 0,15 |
| 6,0 | 5,88 (2%) | 5,70 (5%) | 0,20 |
| 8,0 | 7,84 (2%) | 7,60 (5%) | 0,25 |
| 10,0 | 9,80 (2%) | 9,50 (5%) | 0,30 |
| 12,0 | 11,76 (2%) | 11,40 (5%) | 0,30 |
| 14,0 | 13,72 (2%) | 13,30 (5%) | 0,35 |
| 16,0 | 15,68 (2%) | 15,20 (5%) | 0,40 |
| 19,0 | 18,62 (2%) | 18,05 (5%) | 0,45 |
| 22,0 | 21,56 (2%) | 20,90 (5%) | 0,50 |
| 25,0 | 24,50 (2%) | 23,75 (5%) | 0,55 |

> **Confidence: documented** — Basierend auf Rigger-Standards und Hersteller-Empfehlungen (Wichard, Seldén, Navtec)

### Tabelle D-2: Schäkelkörper-Verschleißgrenzen

| Bauteil | Monitor-Schwelle | Austausch-Schwelle |
|---------|-----------------|-------------------|
| Bügelweite (Aufweitung) | +0,5mm über Nennmaß | +1,0mm über Nennmaß |
| Bügelquerschnitt (Abrieb) | -3% Querschnitt | -5% Querschnitt |
| Bohrung (Aufweitung) | +3% über Nennmaß | +5% über Nennmaß |
| Pitting-Tiefe | >0,2mm | >0,5mm oder >5 Pits/cm² |
| Risstiefe (PT) | Jeder Riss | Jeder Riss = Austausch |

### Tabelle D-3: Wirbel-Verschleißgrenzen

| Parameter | Monitor | Austausch |
|-----------|---------|----------|
| Axialspiel | >0,5mm | >1,0mm (>0,8mm bei Ronstan) |
| Radialspiel | >0,2mm | >0,3mm |
| Achsdurchmesser-Reduktion | >2% | >5% |
| Lagerflächen-Rauigkeit | Spürbar | Riefen >0,1mm oder Galling |
| Kugellager-Lauf | Leicht rau | Rau, blockiert, Geräusche |
| Gabelauge-Aufweitung | >0,3mm | >0,5mm |

### Tabelle D-4: Toggle-Verschleißgrenzen

| Parameter | Monitor | Austausch |
|-----------|---------|----------|
| Gabelöffnung-Aufweitung | >0,5mm | >1,0mm |
| Gabelradius-Riss (PT) | Jede Anzeige <3mm | Jede Anzeige ≥3mm |
| Bolzendurchmesser-Reduktion | >2% | >5% |
| Gabelschenkel-Verdrehung | Sichtbar | Jede messbare Verdrehung |
| Schaft-Durchmesser-Reduktion | >2% | >5% |

### Tabelle D-5: Schnappschäkel-Verschleißgrenzen

| Parameter | Monitor | Austausch |
|-----------|---------|----------|
| Federkraft (vs. Neuwert) | <80% | <70% |
| Nasen-Rastkante Abrieb | >0,2mm | >0,5mm |
| Federachsen-Durchmesser | >2% Reduktion | >5% Reduktion |
| Gehäuse-Verformung | Sichtbar | Jede messbare Verformung |
| Feder gebrochen | — | Sofort ersetzen |

### Tabelle D-6: Soft-Schäkel Verschleißgrenzen

| Parameter | Monitor | Austausch |
|-----------|---------|----------|
| Durchmesser-Reduktion | >5% | >10% |
| UV-Vergrauung | Deutlich sichtbar | Stark + Oberflächenverhärtung |
| Faserbrüche | Einzelne Fasern | Mehrere Faserstränge |
| Knoten-Festigkeit | Knoten lockert sich | Knoten rutscht unter Last |
| Alter (UV-exponiert) | >2 Jahre | >4 Jahre |
| Alter (UV-geschützt) | >4 Jahre | >8 Jahre |

---

## ANHANG E — Confidence-Mapping

### Confidence-Zuordnung für Wartungsbefunde

| Befundtyp | Methode | Confidence |
|-----------|---------|-----------|
| Bolzenmessung (Mikrometer) | Kalibrierte Messung | measured |
| Bolzenmessung (Messschieber) | Kalibrierte Messung | measured |
| Bohrungsmessung (Lehrdorn) | Go/No-Go | measured |
| Risssuche (PT) | NDT-Verfahren | measured |
| Risssuche (visuell, 10× Lupe) | Sichtprüfung | visual_high |
| Risssuche (Augenschein) | Sichtprüfung | visual_medium |
| Korrosionsbewertung (visuell) | Sichtprüfung | visual_medium |
| Federkraft (Kraftmesser) | Messung | measured |
| Federkraft (subjektiv) | Handprüfung | estimated |
| Verschleißrate (berechnet) | Aus Messwerten | calculated |
| Lebensdauerprognose | Aus Verschleißrate | estimated |
| Herstellerangabe Intervall | Dokumentation | documented |
| AYDI-Empfehlung Intervall | Erfahrungswerte | estimated |
| Schadensursache (Bruchfläche) | Fachanalyse | measured |
| Schadensursache (Vermutung) | Erfahrung | estimated |

---

## ANHANG F — Werkzeuglisten

### Werkzeug-Grundausstattung für Verbinder-Wartung

| Werkzeug | Spezifikation | Verwendung | Ca. Preis |
|----------|--------------|------------|-----------|
| Digitaler Messschieber | 0–150mm, 0,02mm | Bolzen/Bohrungsmessung | €25–50 |
| Bügelmessschraube | 0–25mm, 0,01mm | Präzise Bolzenmessung | €30–60 |
| Lupe | 10× Vergrößerung | Risssuche, Korrosionsbeurteilung | €10–20 |
| LED-Taschenlampe | >200 Lumen, fokussierbar | Beleuchtung Spalte/Bohrungen | €15–30 |
| Spitzzange | Gerade, 150mm | Federstecker, Splinte | €15–25 |
| Seitenschneider | 150mm | Splinte, Drahtwicklung | €15–25 |
| Gabelschlüssel-Satz | 8–22mm | Wantenspanner, Bolzen | €30–50 |
| Innensechskant-Satz | 2–10mm | Wichard HR, div. Schrauben | €10–20 |
| Dorn (Messing) | Ø 5, 8, 10mm | Bolzen austreiben | €15–25 |
| Hammer (Kunststoff) | 300g | Bolzen austreiben | €15–25 |
| Nylonbürste | Hart, 30mm | Reinigung Edelstahl | €5–10 |
| Bronzedrahtbürste | 30mm | Reinigung Edelstahl | €8–12 |
| PT-Set (Farbeindringprüfung) | Reiniger, Eindringm., Entwickler | Risssuche | €25–40 |
| Kamera/Smartphone | Mit Makrofunktion | Dokumentation | vorhanden |

**Gesamtkosten Grundausstattung:** ca. €220–370

### Zusatzausstattung für Profis/Blauwasser

| Werkzeug | Spezifikation | Verwendung | Ca. Preis |
|----------|--------------|------------|-----------|
| Kraftmessgerät (Federwaage) | 0–50 N | Schnappschäkel-Federkraft | €25–40 |
| Go/No-Go Lehrdorn-Satz | Ø 6, 8, 10, 12mm | Bohrungsprüfung | €80–120 |
| Drehmomentschlüssel | 5–50 Nm | Bolzen definiert anziehen | €50–80 |
| Endoskop (USB) | Ø 5mm, 1m Länge | Inspektion unzugänglicher Stellen | €30–60 |
| Dickenmessgerät (Ultraschall) | 0,8–200mm | Wandstärkenmessung | €200–400 |

---

## ANHANG G — Herstellerspezifische Wartungsvorgaben

### G-1: Wichard — Wartungsvorgaben Zusammenfassung

| Produkt | Wartungsvorgabe | Quelle |
|---------|----------------|--------|
| HR-Schäkel (selbstsichernd) | Jährliche Inspektion, Innensechskant prüfen, Anti-Seize | Wichard Tech Doc |
| Schnappschäkel (2677 Serie) | Saisonal: Feder prüfen, Nase inspizieren | Wichard Tech Doc |
| Wirbel (Gabel-Gabel) | Jährlich: Schmierung, Lagerflächen prüfen | Wichard Tech Doc |
| Wirbel (mit Kugellager) | Halbjährlich: Drehgängigkeit, Schmierung | Wichard Tech Doc |
| Toggle-Systeme | 5-jährlich: NDT (PT empfohlen) | Wichard Tech Doc |
| Soft-Schäkel (Dyneema) | Vor jeder Nutzung: Sichtprüfung UV/Abrieb | Wichard Tech Doc |

### G-2: Tylaska — Wartungsvorgaben Zusammenfassung

| Produkt | Wartungsvorgabe | Quelle |
|---------|----------------|--------|
| T5/T8/T12 Snap Shackle | Saisonal: Komplett zerlegen, Feder prüfen/tauschen | Tylaska Tech Bulletin |
| T-Serie Trigger Release | Halbjährlich: Trigger-Mechanismus prüfen | Tylaska Tech Bulletin |
| Racing Snap Shackle | Monatlich: Funktionstest, vierteljährlich: Service | Tylaska Tech Bulletin |
| Ersatzfedern | Tausch empfohlen: alle 2 Jahre (Regatta), 3 Jahre (Fahrt) | Tylaska Tech Bulletin |

### G-3: Harken — Wartungsvorgaben Zusammenfassung

| Produkt | Wartungsvorgabe | Quelle |
|---------|----------------|--------|
| Snap Shackle (Standard) | Saisonal: Inspektion, Schmierung (Harken McLube) | Harken Maintenance Guide |
| Snap Shackle (Hi-Load) | Halbjährlich: Demontage, Inspektion, Schmierung | Harken Maintenance Guide |
| Block-Schäkel-Verbindungen | Jährlich: Achse und Schäkel prüfen, schmieren | Harken Maintenance Guide |
| Battcar-Schäkel | Saisonal: Auf Abrieb am Mast-Schlitten prüfen | Harken Maintenance Guide |

### G-4: Ronstan — Wartungsvorgaben Zusammenfassung

| Produkt | Wartungsvorgabe | Quelle |
|---------|----------------|--------|
| Orbit-Blöcke (Schäkelachse) | Jährlich: Achse und Schäkel prüfen | Ronstan Tech Info |
| Wirbel (alle Modelle) | Halbjährlich: Schmierung, Drehgängigkeit | Ronstan Tech Info |
| Serie 55 Snap Shackle | Saisonal: Demontage, Feder prüfen, schmieren | Ronstan Tech Info |
| Schäkel (Standardlinie) | Jährlich: Bolzen lösen, Anti-Seize erneuern | Ronstan Tech Info |

---

## ANHANG H — Schmierplan-Vorlagen

### Schmierplan — Fahrtensegler (8–14m)

```
AYDI Schmierplan — Fahrtensegler
=================================
Yacht: _________________ Saison: _____________

QUARTAL 1 (SAISONSTART, z.B. April)
□ Alle Wantenspanner: Gewinde mit Tef-Gel
□ Alle Toggle-Bolzen: Anti-Seize erneuern
□ Alle Rigg-Schäkel: Bolzen Anti-Seize
□ Ankerwirbel: Marine-Fett auf Lager
□ Ankerschäkel: Anti-Seize auf Bolzen
□ Schnappschäkel (alle): Teflon-Spray auf Achse
□ Wirbel (alle): Marine-Fett auf Lagerflächen

QUARTAL 2 (MITTE SAISON, z.B. Juli)
□ Wirbel: Drehgängigkeit prüfen, bei Bedarf nachschmieren
□ Ankerwirbel: Nachschmieren
□ Schnappschäkel: Teflon-Spray nachsprühen

QUARTAL 3 (SAISONENDE, z.B. Oktober)
□ Wie Quartal 1 — vollständiger Service
□ Zusätzlich: Lanocote auf alle exponierten Verbinder (Winterschutz)

QUARTAL 4 (WINTERLAGER)
□ Keine Schmierung erforderlich (Schutz aus Q3 wirkt)
□ Bei Hallenlagerung: Belüftung sicherstellen (Kondensation!)

Datum Q1: ___________ Prüfer: ___________
Datum Q2: ___________ Prüfer: ___________
Datum Q3: ___________ Prüfer: ___________
```

---

## ANHANG I — Korrosions-Referenztabellen

### Tabelle I-1: Korrosionsraten verschiedener Materialien in Meerwasser

| Material | Allgemeine Korrosion (mm/Jahr) | Pitting-Risiko | SCC-Risiko |
|----------|-------------------------------|----------------|-----------|
| Edelstahl 316L (passiv) | <0,01 | Mittel | Niedrig (<50°C) |
| Edelstahl 316L (aktiv/Spalt) | 0,1–1,0 | Hoch | Mittel |
| Edelstahl 304 | 0,01–0,05 | Hoch | Mittel |
| Duplex SAF 2205 | <0,005 | Sehr niedrig | Sehr niedrig |
| Titan Gr.2/Gr.5 | <0,001 | Extrem niedrig | Extrem niedrig |
| Bronze (CuSn8) | 0,02–0,05 | Niedrig | Niedrig |
| Aluminium 6082 | 0,05–0,15 | Mittel | Niedrig |
| Stahl verzinkt | 0,05–0,15 (Zink) | Mittel | Niedrig |
| Stahl unbehandelt | 0,1–0,5 | Hoch | Niedrig |

> **Confidence: measured** — Basierend auf Laborwerten und Langzeitstudien (DNV, NACE, Outokumpu)

### Tabelle I-2: Galvanische Verträglichkeit — Praxismatrix

| | Edelst. 316L | Titan | Bronze | Alu | Stahl verz. |
|---|---|---|---|---|---|
| Edelst. 316L | ✓ | ⚠ | ✓ | ✗ | ⚠ |
| Titan | ⚠ | ✓ | ⚠ | ✗✗ | ✗ |
| Bronze | ✓ | ⚠ | ✓ | ✗ | ⚠ |
| Alu | ✗ | ✗✗ | ✗ | ✓ | ⚠ |
| Stahl verz. | ⚠ | ✗ | ⚠ | ⚠ | ✓ |

Legende: ✓ = kompatibel, ⚠ = Isolation empfohlen, ✗ = Isolation erforderlich, ✗✗ = Kombination vermeiden

---

## ANHANG J — Ersatzteil-Referenz

### Empfohlene Ersatzteile an Bord — Fahrtensegler (8–14m)

| Teil | Menge | Größe | Ca. Preis |
|------|-------|-------|-----------|
| D-Schäkel 316L | 4 | 2× Rigg-Größe, 2× Deck-Größe | €20 |
| Bügelschäkel 316L | 2 | Anker-Größe | €15 |
| Schnappschäkel | 1 | Spi-Fall-Größe | €40 |
| Schnappschäkel-Ersatzfeder | 2 | Passend zu verbauten Modellen | €20 |
| Wirbel | 1 | Rigg-Größe | €40 |
| Bolzen (Sortiment) | 10 | Ø 6, 8, 10mm | €15 |
| Splinte 316L | 20 | Sortiment passend | €8 |
| Federstecker 316L | 20 | Sortiment passend | €10 |
| Soft-Schäkel | 4 | 2× Schotenblöcke, 2× Segel | €20 |
| Tef-Gel | 1 Tube 30g | — | €15 |
| Lanocote | 1 Dose 120g | — | €20 |
| Marine-Fett | 1 Tube 100g | — | €12 |
| Teflon-Spray | 1 Dose 200ml | — | €8 |

**Gesamtkosten Ersatzteilbox:** ca. €243

### Empfohlene Ersatzteile — Blauwasseryacht (12–18m)

Grundausstattung wie Fahrtensegler, zusätzlich:

| Teil | Menge | Begründung | Ca. Preis |
|------|-------|-----------|-----------|
| Toggle (Rigg-Größe) | 2 | Kein Ersatz unterwegs beschaffbar | €80 |
| Wantenspanner | 1 | Reserve für Notfall-Reparatur | €120 |
| Schnappschäkel-Set (mit Federn) | 2 | Verschiedene Größen | €100 |
| D-Schäkel (groß, Anker) | 4 | Ankersystem-Reserve | €30 |
| PT-Set (Farbeindringprüfung) | 1 | Risssuche unterwegs | €30 |
| Ersatz-Kugellager (Wirbel) | 2 | Falls Wirbel zerlegbar | €25 |
| Mousing Wire 316L | 10m | Ankerschäkel-Sicherung | €8 |
| Loctite 243 (mittelfest) | 1 Tube | Schraubensicherung | €10 |

**Zusatzkosten Blauwasser:** ca. €403

---

## ANHANG K — Dokumentationsvorlagen

### Vorlage K-1: Verbinder-Bestandsliste

```
AYDI Verbinder-Bestandsliste
==============================
Yacht: _________________ Typ: _________________ BJ: _______

Nr | Position | Typ | Hersteller | Modell | Ø/Größe | Material | Einbau | Letzter Service
---|----------|-----|-----------|--------|---------|----------|--------|----------------
01 | Vorstag Toggle unten | Toggle | Seldén | — | Ø12 | 316L | 2020 | 2025-10
02 | Vorstag Schäkel oben | D-Schäkel | Wichard | HR 10mm | Ø10 | 316L | 2022 | 2025-10
03 | ...

Gesamtanzahl Verbinder: _______
Letzte Aktualisierung: _______
```

### Vorlage K-2: Wartungslog (pro Verbinder)

```
AYDI Wartungslog — Verbinder
==============================
Verbinder-ID: ______________ Position: ______________

Datum | Stufe | Befund | Maßnahme | Messwerte | Prüfer | Nächster Termin
------|-------|--------|----------|-----------|--------|---------------
2025-04 | W1 | OK | — | — | JS | 2025-05
2025-10 | W2 | Bolzen Ø 9,92mm | Anti-Seize, Splint neu | Ø 9,92/9,94 | JS | 2026-04
...
```

---

## ANHANG L — Visuelle Analyse-Referenz

### AYDI Visual Pipeline — Verbinder-Wartungsbefunde

Die AYDI Visual Pipeline (Pipeline B) kann Wartungsbefunde an Verbindern aus Fotos erkennen. Die folgenden Referenzbilder und Beschreibungen dienen als Trainingsdaten und Validierungsreferenz.

**Erkennbare Befunde und Confidence-Level:**

| Befund | Confidence bei gutem Foto | Confidence bei mittlerem Foto | Mindest-Anforderung |
|--------|--------------------------|------------------------------|---------------------|
| Fehlender Splint | visual_high | visual_medium | Verbinder erkennbar |
| Sichtbare Korrosion (allgemein) | visual_high | visual_medium | Oberfläche erkennbar |
| Pitting (grob) | visual_medium | visual_low | Nahaufnahme |
| Verformung (deutlich) | visual_high | visual_medium | Gesamtansicht |
| UV-Degradation (Soft-Schäkel) | visual_medium | visual_low | Vergleichsbild |
| Galling-Spuren | visual_low | visual_insufficient | Makro-Nahaufnahme |
| Risse | visual_low | visual_insufficient | Nur grobe Risse |
| Bolzenverschleiß (Messung) | visual_insufficient | visual_insufficient | Nicht visuell möglich |

> **Hinweis:** Für präzise Verschleißmessung (Bolzendurchmesser, Ovalität) ist die visuelle Analyse grundsätzlich nicht geeignet. Diese erfordert Pipeline A (measured) mit kalibrierten Messmitteln.

**Foto-Anforderungen für visuelle Wartungsanalyse:**
- Auflösung: mindestens 12 MP
- Beleuchtung: Tageslicht oder LED, kein Blitz (Reflexionen verfälschen)
- Winkel: Senkrecht zur Oberfläche + 45°-Ansicht
- Maßstab: Referenzobjekt im Bild (Münze, Lineal)
- Fokus: Scharf auf die zu beurteilende Oberfläche

---

## ANHANG M — Notfall-Reparaturverfahren

### M-1: Provisorischer Ersatz eines gebrochenen Schäkels auf See

**Situation:** Schäkelbruch am laufenden Gut (z.B. Fallenschäkel), kein Ersatzschäkel an Bord.

**Provisorische Lösung:**
1. Soft-Schäkel aus Reserveleine (Dyneema) spleißen/knoten
2. Alternativ: Tau-Anbindung mit Palstek (nur für laufendes Gut)
3. Drahtwicklung als provisorische Verbindung (nur Notfall!)

**WARNUNG:** Provisorische Verbindungen sind NICHT für stehendes Gut geeignet!

### M-2: Toggle-Bruch auf See — Notmaßnahme

**Situation:** Toggle am Wantterminal gebrochen, Rigg gefährdet.

**Sofortmaßnahmen:**
1. Sofort Kurs ändern, betroffenes Want entlasten (Halse/Wende)
2. Fall oder Reservestag als Ersatzwant einsetzen
3. Wenn Toggle-Bolzen noch intakt: Drahtwicklung als provisorische Verbindung
4. Wenn komplett gebrochen: Dyneema-Soft-Schäkel als provisorischer Ersatz
5. Geschwindigkeit und Segelfläche reduzieren
6. Nächsten Hafen anlaufen

**WARNUNG:** Eine provisorische Toggle-Reparatur ist NUR als Seenotmaßnahme akzeptabel. Im nächsten Hafen MUSS ein fachgerechter Ersatz erfolgen.

### M-3: Schnappschäkel ohne Federkraft auf See

**Situation:** Schnappschäkel-Feder gebrochen, Spi-Fall-Schäkel funktionslos.

**Sofortmaßnahme:**
1. Schnappschäkel durch D-Schäkel + Splint ersetzen (immer an Bord!)
2. Alternativ: Soft-Schäkel als Ersatz
3. Schnappschäkel NICHT mit defekter Feder weiternutzen

---

## ANHANG N — Saisonale Wartungskalender

### Wartungskalender — Nordeuropa (Ostsee/Nordsee)

| Monat | Aktivitäten |
|-------|-------------|
| März | Aufrüsten: Alle Verbinder W2-Inspektion, Anti-Seize erneuern, Splinte tauschen |
| April | Saisonstart: W1 alle Verbinder, Wirbel schmieren |
| Mai | W1 Routine |
| Juni | W1 Routine, Schnappschäkel Teflon-Spray |
| Juli | W1 Routine, Ankerwirbel nachschmieren |
| August | W1 Routine |
| September | W1 Routine, Schnappschäkel Teflon-Spray |
| Oktober | Abrüsten: Alle Verbinder W2-Inspektion, Lanocote Winterschutz |
| November–Februar | Winterlager: W3-Inspektionen, NDT bei Bedarf, Ersatzteile beschaffen |

### Wartungskalender — Tropen/Karibik (Ganzjahres-Betrieb, verschärft)

| Monat | Aktivitäten |
|-------|-------------|
| Januar | W2 Komplett: Alle Verbinder, Anti-Seize erneuern, Wirbel schmieren |
| Februar | W1, Ankerwirbel auf Bewuchs prüfen |
| März | W1, Schnappschäkel Teflon-Spray |
| April | W2: Ankerverbinder, Wirbel nachschmieren, Soft-Schäkel UV-Check |
| Mai | W1, Regenzeit: Süßwasserspülung nutzen |
| Juni | W1, Schnappschäkel Teflon-Spray |
| Juli | W2 Komplett: Wie Januar, Soft-Schäkel kritisch bewerten |
| August | W1, Hurrikan-Saison: Alle Verbinder vor Sturmsicherung prüfen |
| September | W1, nach Sturmereignis: Sonderinspektion aller belasteten Verbinder |
| Oktober | W2: Ankerverbinder, Wirbel nachschmieren |
| November | W1, Schnappschäkel Teflon-Spray |
| Dezember | W1, Jahresabschluss-Bewertung, Ersatzteile auffüllen |

> **Hinweis:** In tropischen Gewässern sind alle Verschleiß- und Korrosionsprozesse um Faktor 2–3 beschleunigt. Die verkürzte Intervalle sind sicherheitsrelevant und nicht optional.

### Wartungskalender — Mittelmeer (Ganzjahres-Betrieb)

| Quartal | Aktivitäten |
|---------|-------------|
| Q1 (Jan–Mär) | W2 alle Verbinder, Wirbel schmieren, Splinte tauschen, Schnappschäkel-Federn prüfen |
| Q2 (Apr–Jun) | W1 monatlich, Schnappschäkel Teflon-Spray, Ankerwirbel schmieren |
| Q3 (Jul–Sep) | W1 monatlich, Wirbel nachschmieren, Soft-Schäkel UV-Check |
| Q4 (Okt–Dez) | W2 alle Verbinder (Hauptwartung), W3 nach Plan, Ersatzteile auffüllen |

---

## ANHANG O — Schulungsunterlagen

### O-1: Kompetenzanforderungen für Verbinderwartung

| Kompetenz | W1 (Skipper) | W2 (Eigner) | W3 (Rigger) |
|-----------|-------------|-------------|-------------|
| Sichtprüfung Verbinder | ✓ erforderlich | ✓ | ✓ |
| Bolzenmessung (Messschieber) | — | ✓ erforderlich | ✓ |
| Farbeindringprüfung (PT) | — | Optional (Schulung) | ✓ erforderlich |
| NDT-Prüfung (UT) | — | — | ✓ (UT Stufe 2) |
| Kraftmessung (Federwaage) | — | ✓ optional | ✓ |
| Dokumentation | ✓ (Basis) | ✓ (Detail) | ✓ (Formal) |
| Bewertung/Freigabe | Sichtbefunde | Verschleißbefunde | Alle Befunde |

### O-2: Schulungsmodule

**Modul 1: Verbinder-Grundlagen (2 Stunden)**
- Verbindertypen und ihre Funktion
- Materialien und ihre Eigenschaften
- Belastungen und Sicherheitsfaktoren
- Warum Wartung lebenswichtig ist
- Praktische Übung: Verbindertypen identifizieren

**Modul 2: Praktische Wartung (4 Stunden)**
- Werkzeuge und ihre korrekte Verwendung
- Bolzendemontage und -messung (Praxis)
- Anti-Seize korrekt auftragen (Praxis)
- Splinte und Federstecker wechseln (Praxis)
- Schnappschäkel-Feder tauschen (Praxis)
- Wirbel-Service (Praxis)
- Dokumentation führen

**Modul 3: Fehlersuche und Bewertung (3 Stunden)**
- Korrosionsarten erkennen (Bildmaterial + Praxisproben)
- Verschleißgrenzen verstehen und anwenden
- Farbeindringprüfung durchführen (Praxis)
- Entscheidungsbäume anwenden
- Wann zum Rigger / Surveyor überweisen

**Modul 4: Dokumentation und AYDI-System (1 Stunde)**
- Wartungslog führen
- Fotos korrekt anfertigen
- AYDI-Plattform für Verbinder-Tracking nutzen
- Inspektionsplanung und Terminerinnerungen

### O-3: Typische Fehler bei der Erstausbildung

1. **Bolzen zu fest anziehen:** Schäkelbolzen = handfest + Sicherung, KEIN Drehmoment
2. **Stahldrahtbürste auf Edelstahl:** Verursacht Fremdrost
3. **Alten Splint wiederverwenden:** Splinte sind Einmalteile
4. **Zu viel Fett:** Überschuss sammelt Schmutz und Salz
5. **Wantenspanner unter Last öffnen:** Lebensgefahr!
6. **Silikon statt Anti-Seize:** Silikon ist kein Galling-Schutz
7. **"Sieht gut aus" = "Ist gut":** Viele Schäden sind nicht sichtbar (Innenkorrosion, Ermüdung)

---

## ANHANG P — Wirtschaftlichkeitsbetrachtung

### P-1: Kosten-Nutzen-Analyse der Verbinderwartung

**Szenario: Fahrtensegler 12m, 15 Jahre Nutzung**

| Posten | Ohne Wartung | Mit Wartungsprogramm |
|--------|-------------|---------------------|
| Jährliche Wartungskosten (Material) | €0 | €80/Jahr = €1.200 |
| Jährliche Wartungskosten (Zeit, €40/h) | €0 | 8h/Jahr = €320/Jahr = €4.800 |
| Schaden durch Verbinder-Versagen (Erwartungswert) | €2.500/5 Jahre = €7.500 | €500/15 Jahre = €500 |
| Rigg-Kompletttausch (vorgezogen durch fehlende Wartung) | €15.000 nach 10 Jahren | €15.000 nach 15 Jahren |
| **Gesamtkosten 15 Jahre** | **€22.500** | **€21.500** |

**Ergebnis:** Selbst bei konservativer Betrachtung ist ein Wartungsprogramm wirtschaftlicher. Bei Berücksichtigung von Sicherheit, Saisonausfall und Werterhalt der Yacht ist der Vorteil deutlich größer.

### P-2: Return on Investment — Wartung

| Investition | ROI |
|------------|-----|
| 30g Tef-Gel (€15) | Verhindert Galling → potentiell €500–5.000 Schaden |
| 20 Splinte (€8) | Verhindert Bolzenverlust → potentiell €1.000–50.000 |
| PT-Set (€30) | Erkennt Ermüdungsriss → potentiell €5.000–100.000 |
| 8h Eigenarbeit/Jahr | Verhindert durchschnittlich €500/Jahr Schadenserwartung |

---

## ANHANG Q — Umrechnungstabellen

### Q-1: Last-Umrechnungen

| Von | Nach | Faktor |
|-----|------|--------|
| kg | kN | ×0,00981 |
| kN | kg | ×101,97 |
| kg | lbs | ×2,2046 |
| lbs | kg | ×0,4536 |
| kN | lbs | ×224,81 |
| Tonnen (metrisch) | kN | ×9,81 |

### Q-2: Längen-Umrechnungen

| Von | Nach | Faktor |
|-----|------|--------|
| mm | inch | ×0,03937 |
| inch | mm | ×25,4 |
| m | feet | ×3,2808 |
| feet | m | ×0,3048 |

### Q-3: Schäkelgrößen — Metrisch/Imperial Zuordnung

| Metrisch (Bolzen-Ø) | Imperial (Bolzen-Ø) | Typische WLL (kg) |
|---------------------|---------------------|-------------------|
| 5mm | 3/16" | 200–350 |
| 6mm | 1/4" | 400–600 |
| 8mm | 5/16" | 700–1.200 |
| 10mm | 3/8" | 1.200–2.000 |
| 12mm | 1/2" | 2.000–3.500 |
| 14mm | 9/16" | 3.000–4.500 |
| 16mm | 5/8" | 4.000–6.500 |
| 19mm | 3/4" | 6.500–10.000 |
| 22mm | 7/8" | 9.000–14.000 |
| 25mm | 1" | 12.000–20.000 |

### Q-4: Drehmoment-Umrechnungen

| Von | Nach | Faktor |
|-----|------|--------|
| Nm | ft-lbs | ×0,7376 |
| ft-lbs | Nm | ×1,3558 |
| Nm | in-lbs | ×8,851 |

---

## ANHANG R — Prüfprotokolle

### Prüfprotokoll R-1: Rigg-Verbinder Komplett-Inspektion

```
AYDI Prüfprotokoll — Rigg-Verbinder Komplett-Inspektion (W2/W3)
================================================================
Yacht: _________________ Typ: __________ BJ: ______
Eigner: ________________ Liegeplatz: ______________
Datum: _________________ Prüfer: __________________
Qualifikation: _________ Nächste Prüfung: __________

MESSMITTEL
Messschieber: ______________ Kalibrierung: ____________
Mikrometer: _______________ Kalibrierung: ____________
PT-Set: ___________________ Charge/Ablauf: ___________

PRÜFUMFANG
□ Stehendes Gut komplett (__ Verbinder)
□ Laufendes Gut komplett (__ Verbinder)
□ Ankersystem (__ Verbinder)
□ Decksbeschläge (__ Verbinder)
□ Sicherheitsausrüstung (__ Verbinder)
Gesamtanzahl geprüfter Verbinder: ____

ZUSAMMENFASSUNG BEFUNDE
Verbinder in Ordnung: ____
Verbinder "Beobachten": ____
Verbinder "Bald ersetzen": ____
Verbinder "Sofort ersetzen": ____

SOFORTMASSNAHMEN ERFORDERLICH:
□ Nein
□ Ja: ___________________________________________

EMPFEHLUNGEN:
_________________________________________________
_________________________________________________
_________________________________________________

Unterschrift Prüfer: ______________ Datum: ________
Unterschrift Eigner: ______________ Datum: ________
```

### Prüfprotokoll R-2: Farbeindringprüfung (PT) — Toggle

```
AYDI Prüfprotokoll — Farbeindringprüfung Toggle
=================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________ Qualifikation: _____________

PT-SYSTEM
Hersteller: ____________ Typ: ______________
Reiniger: ______________ Charge: ___________
Eindringmittel: ________ Charge: ___________
Entwickler: ____________ Charge: ___________
Temperatur (Oberfläche): ____°C (zulässig: 10–50°C)

PRÜFOBJEKT
Toggle-ID: _____________ Position: _____________
Hersteller: ____________ Material: _____________
Alter: ______ Jahre

PRÜFDURCHFÜHRUNG
□ Oberfläche gereinigt (Reiniger, trocknen: ____ Min)
□ Eindringmittel aufgetragen (Einwirkzeit: ____ Min)
□ Überschuss entfernt (Methode: ____________)
□ Entwickler aufgetragen (Entwicklungszeit: ____ Min)

BEFUND
□ Keine Anzeigen
□ Anzeigen gefunden:
  Anzeige 1: Typ: ________ Länge: ____mm Position: __________
  Anzeige 2: Typ: ________ Länge: ____mm Position: __________
  Anzeige 3: Typ: ________ Länge: ____mm Position: __________

FOTOS
□ Foto vor PT: Nr. _______
□ Foto nach Entwicklung: Nr. _______
□ Detail-Fotos Anzeigen: Nr. _______

BEWERTUNG
□ Keine relevanten Anzeigen — Toggle kann weiter verwendet werden
□ Anzeigen gefunden — Toggle ersetzen
□ Anzeigen grenzwertig — Nachprüfung in _____ Monaten

NÄCHSTE PT-PRÜFUNG: ____________

Unterschrift: ______________ Datum: ________
```

### Prüfprotokoll R-3: Schnappschäkel-Federkraftmessung

```
AYDI Prüfprotokoll — Schnappschäkel Federkraft
================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

PRÜFMITTEL
Kraftmessgerät: _________ Kalibrierung: _________
Messbereich: 0–___N Genauigkeit: ±___N

MESSUNG
Schäkel-ID | Hersteller | Modell | Alter | Gemessen (N) | Neuwert (N) | Verhältnis
-----------|-----------|--------|-------|-------------|-------------|----------
           |           |        |       |             |             |
           |           |        |       |             |             |
           |           |        |       |             |             |

BEWERTUNG
□ Alle Federn >80% → OK
□ Federn 70–80% → Beobachten: _______
□ Federn <70% → Ersetzen: _______
□ Federn defekt → Ersetzt: _______

Unterschrift: ______________ Datum: ________
```

---

### Prüfprotokoll R-4: Wirbel-Lagerinspektion

```
AYDI Prüfprotokoll — Wirbel-Lagerinspektion (W2)
===================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

PRÜFOBJEKT
Wirbel-ID: _____________ Position: _____________
Hersteller: ____________ Modell: ______________
Typ: □ Gleitlager  □ Kugellager  □ Nadellager
Material: _____________ Alter: ______ Jahre
Zerlegbar: □ Ja  □ Teilweise  □ Nein

VOR-DEMONTAGE-PRÜFUNG
Drehgängigkeit: □ Frei  □ Schwergängig  □ Blockiert
Geräusche: □ Keine  □ Klicken  □ Knirschen  □ Knarzen
Axialspiel (geschätzt): □ Keins  □ Gering  □ Deutlich
Korrosion außen: □ Keine  □ Leicht  □ Mittel  □ Schwer

DEMONTAGE (falls zerlegbar)
□ Sicherung entfernt (Typ: ____________)
□ Achse herausgezogen
□ Alle Teile nummeriert/fotografiert
□ Lagerschalen/Kugeln entnommen

LAGERFLÄCHEN-INSPEKTION
Obere Lagerfläche:
  Zustand: □ Gut  □ Rau  □ Galling  □ Pitting  □ Risse
  Riefen: □ Keine  □ Leicht (<0,1mm)  □ Tief (>0,1mm)

Untere Lagerfläche:
  Zustand: □ Gut  □ Rau  □ Galling  □ Pitting  □ Risse
  Riefen: □ Keine  □ Leicht (<0,1mm)  □ Tief (>0,1mm)

Achse:
  Zustand: □ Gut  □ Abrieb  □ Korrosion  □ Risse
  Durchmesser: Nenn ____mm  Gemessen ____mm  Reduktion ____%

Kugellager (falls zutreffend):
  Lauf: □ Glatt  □ Leicht rau  □ Rau  □ Blockiert
  Spiel: □ Normal  □ Erhöht  □ Übermäßig

MESSUNG
Axialspiel: ____mm (Grenzwert: 1,0mm)
Radialspiel: ____mm (Grenzwert: 0,3mm)
Gabelauge Weite: Nenn ____mm  Gemessen ____mm

SCHMIERUNG
□ Alte Schmierung entfernt
□ Neue Schmierung aufgetragen (Produkt: _____________)
□ Menge: □ Dünn  □ Normal  □ Reichlich
□ Anti-Seize auf Achse/Gewinde (Produkt: _____________)

ZUSAMMENBAU
□ Korrekte Reihenfolge
□ Sicherung eingesetzt (Typ: ____________)
□ Drehgängigkeit nach Zusammenbau: □ Frei  □ Schwergängig

BEWERTUNG
□ In Ordnung — nächste Inspektion: ____________
□ Beobachten — verkürzte Inspektion: ____________
□ Lager/Achse tauschen — Termin: ____________
□ Wirbel komplett ersetzen — sofort / bis: ____________

BEMERKUNGEN:
_________________________________________________
_________________________________________________

Unterschrift: ______________ Datum: ________
```

### Prüfprotokoll R-5: Ankersystem-Verbinder Inspektion

```
AYDI Prüfprotokoll — Ankersystem-Verbinder (W2)
=================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

ANKER-KETTEN-SCHÄKEL
Typ: __________________ Größe: ____mm  Material: ________
Bolzensicherung: □ Drahtwicklung  □ Splint  □ Selbstsichernd
Bolzen-Zustand: □ OK  □ Korrodiert  □ Festsitzend
Bolzen-Ø: Nenn ____mm  Gemessen ____mm
Bügel-Zustand: □ OK  □ Verformt  □ Korrodiert
Drahtwicklung: □ OK  □ Lose  □ Gebrochen  □ Fehlend
Bewertung: □ OK  □ Ersetzen

KETTENWIRBEL
Typ: __________________ Hersteller: ______________
Drehgängigkeit: □ Frei  □ Schwergängig  □ Blockiert
Bewuchs: □ Kein  □ Leicht  □ Stark (entfernt: □)
Korrosion: □ Keine  □ Leicht  □ Mittel  □ Schwer
Schmierung durchgeführt: □ Ja (Produkt: ___________)  □ Nein
Bewertung: □ OK  □ Schmieren  □ Ersetzen

KETTENSTOPPER-BOLZEN
Bolzen-Zustand: □ OK  □ Verschlissen  □ Korrodiert
Sicherung: □ OK  □ Fehlt  □ Defekt
Funktion: □ Hält sicher  □ Rutscht  □ Klemmt
Bewertung: □ OK  □ Ersetzen

KETTEN-VORLÄUFER-VERBINDUNG
Schäkel-Zustand: □ OK  □ Verschlissen  □ Korrodiert
Vorläufer-Spleiß: □ OK  □ Aufgegangen  □ Gescheuert
Bewertung: □ OK  □ Ersetzen

GESAMTBEWERTUNG ANKERSYSTEM
□ Alle Verbinder in Ordnung
□ Einzelne Verbinder zu ersetzen: _______________
□ Komplettrevision empfohlen

Nächste Inspektion: ____________
Unterschrift: ______________ Datum: ________
```

### Prüfprotokoll R-6: Sicherheitsausrüstung-Verbinder

```
AYDI Prüfprotokoll — Sicherheitsausrüstung-Verbinder
======================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

RETTUNGSINSEL-BEFESTIGUNG
Halteband-Schäkel: □ OK  □ Korrodiert  □ Lose  □ Fehlt
Auslösemechanismus (Hydrostatic Release): □ OK  □ Abgelaufen
Ablaufdatum HRU: ____________
Befestigungspunkt an Deck: □ OK  □ Beschädigt
Bewertung: □ OK  □ Maßnahme: _______________

LIFELINE-VERBINDER
Lifeline-Spanner Bb: □ OK  □ Lose  □ Korrodiert
Lifeline-Spanner Stb: □ OK  □ Lose  □ Korrodiert
Lifeline-Schäkel Bb (Anzahl: __): □ Alle OK  □ Defekt: ___
Lifeline-Schäkel Stb (Anzahl: __): □ Alle OK  □ Defekt: ___
Lifeline-Draht/Dyneema: □ OK  □ Beschädigt
Stanchion-Basis-Bolzen: □ Alle fest  □ Lose: ___
Bewertung: □ OK  □ Maßnahme: _______________

JACK-LINE-BEFESTIGUNG
Bug-Schäkel: □ OK  □ Korrodiert  □ Lose
Heck-Schäkel: □ OK  □ Korrodiert  □ Lose
Jack-Line-Gurtband: □ OK  □ Verschlissen  □ UV-Schaden
Bewertung: □ OK  □ Maßnahme: _______________

SICHERHEITSLEINEN-KARABINER
Karabiner 1: □ Schließt sicher  □ Schwergängig  □ Defekt
Karabiner 2: □ Schließt sicher  □ Schwergängig  □ Defekt
Karabiner 3: □ Schließt sicher  □ Schwergängig  □ Defekt
Gurtband/Leine: □ OK  □ Verschlissen  □ UV-Schaden
Bewertung: □ OK  □ Maßnahme: _______________

MOB-RETTUNGSMITTEL
Rettungsring-Halter: □ OK  □ Beschädigt
Rettungsring-Leine-Schäkel: □ OK  □ Korrodiert
MOB-Leuchte-Befestigung: □ OK  □ Lose
Bewertung: □ OK  □ Maßnahme: _______________

GESAMTBEWERTUNG SICHERHEITSAUSRÜSTUNG
□ Alle Verbinder in Ordnung
□ Maßnahmen erforderlich: _______________
□ Sicherheitskritische Mängel: _______________

Nächste Inspektion: ____________
Unterschrift: ______________ Datum: ________
```

### Prüfprotokoll R-7: Soft-Schäkel Zustandsbewertung

```
AYDI Prüfprotokoll — Soft-Schäkel Zustandsbewertung
=====================================================
Yacht: _________________ Datum: _____________
Prüfer: ________________

Soft-Schäkel-ID: ________ Position: _____________
Material: □ Dyneema SK78  □ Dyneema SK99  □ Andere: _______
Hersteller: _____________ Durchmesser (Nenn): ____mm
Einbaudatum: ____________ Alter: ____ Monate
UV-Exposition: □ Permanent (Deck)  □ Teilweise  □ Geschützt (Mast)

VISUELLE INSPEKTION
Farbe: □ Original  □ Leicht vergraut  □ Stark vergraut  □ Weiß/bleich
Oberfläche: □ Glatt  □ Leicht aufgeraut  □ Deutlich aufgefasert
Flexibilität: □ Geschmeidig  □ Leicht steif  □ Steif  □ Spröde
Faserbrüche: □ Keine  □ Einzelne (<5)  □ Mehrere (5–20)  □ Viele (>20)
Abriebstellen: □ Keine  □ Leicht  □ Deutlich (Kerbe)
Knoten: □ Fest  □ Noch fest  □ Lockert sich

MESSUNG
Durchmesser gemessen (3 Stellen):
  Stelle 1: ____mm  Stelle 2: ____mm  Stelle 3: ____mm
  Minimum: ____mm  Reduktion: ____%
  (Grenzwert: >10% = ersetzen)

UV-DEGRADATIONS-SCORE (0–10)
□ 0–2: Neuwertig, keine sichtbare Degradation
□ 3–4: Leichte Vergrauung, Fasern intakt
□ 5–6: Deutliche Vergrauung, vereinzelte Faserbrüche
□ 7–8: Starke Vergrauung, aufgeraute Oberfläche, Steifigkeit
□ 9–10: Schwere Degradation, spröde, Bruchgefahr → ERSETZEN

UV-Score: ____/10

BEWERTUNG
□ In Ordnung — weiter verwenden
□ Beobachten — Inspektionsintervall: ____ Wochen
□ Bald ersetzen — innerhalb ____ Wochen
□ Sofort ersetzen — Bruchgefahr

BEMERKUNGEN:
_________________________________________________

Unterschrift: ______________ Datum: ________
```

### Prüfprotokoll R-8: Jahresabschluss Verbinder-Gesamtbewertung

```
AYDI Prüfprotokoll — Jahresabschluss Verbinder
=================================================
Yacht: _________________ Typ: __________ BJ: ______
Eigner: ________________ Datum: _____________
Prüfer: ________________ Qualifikation: _____________

ZUSAMMENFASSUNG DES JAHRES

Gesamtanzahl Verbinder an Bord: ____
Davon inspiziert (W2 oder höher): ____ (____ %)
Davon mit W3 (Fachinspektion): ____ (____ %)

ZUSTANDSÜBERSICHT
Verbinder "In Ordnung": ____ (____ %)
Verbinder "Beobachten": ____ (____ %)
Verbinder "Bald ersetzen": ____ (____ %)
Verbinder "Sofort ersetzen": ____ (____ %)
Verbinder ersetzt in diesem Jahr: ____

GETAUSCHTE VERBINDER (dieses Jahr)
Nr | Position | Alt (Typ/Alter) | Neu (Typ) | Grund | Kosten
---|----------|----------------|-----------|-------|-------
   |          |                |           |       |
   |          |                |           |       |
   |          |                |           |       |

VERBRAUCHTE MATERIALIEN
Anti-Seize (Produkt/Menge): _________________________
Schmierfett (Produkt/Menge): ________________________
Splinte verbraucht: ____ Stück
Federstecker verbraucht: ____ Stück

KOSTEN-ZUSAMMENFASSUNG
Materialkosten: €______
Arbeitskosten (extern): €______
Eigenarbeit (geschätzt ____ Stunden à €___): €______
Gesamtkosten Verbinderwartung: €______

AUFFÄLLIGKEITEN / TRENDS
□ Keine besonderen Auffälligkeiten
□ Korrosion zunehmend → Gebiet: ___________
□ Verschleiß überdurchschnittlich → Position: ___________
□ Altersbedingte Tausch-Welle anstehend → Wann: ___________

PLAN FÜR NÄCHSTES JAHR
□ Routine-Wartung fortführen
□ W3-Inspektionen geplant für: _______________
□ Tausch geplant für: _______________
□ Rigg-Check durch Rigger: □ Ja (Termin: _______)  □ Nein
□ Ersatzteile nachbestellen: _______________

GESAMTBEWERTUNG VERBINDER-ZUSTAND DER YACHT
□ Sehr gut — alle Verbinder in einwandfreiem Zustand
□ Gut — einzelne Beobachtungspunkte, keine Sicherheitsbedenken
□ Befriedigend — einzelne Verbinder bald fällig zum Tausch
□ Mangelhaft — mehrere Verbinder überfällig, Sicherheitsrisiko
□ Ungenügend — sofortige Maßnahmen erforderlich

Gesamtscore (AYDI, 0–100): ____

UNTERSCHRIFTEN
Prüfer: _________________ Datum: _________
Eigner: _________________ Datum: _________
```

---

> **Ende der Wissensdatei 12.05 — Verbinder Wartung und Troubleshooting**
> **AYDI Research — Version 1.0.0 — 2026-04-26**
> **Nächste geplante Überarbeitung: 2026-10-26**
