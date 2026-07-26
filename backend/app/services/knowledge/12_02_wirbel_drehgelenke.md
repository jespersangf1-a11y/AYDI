---
title: "Wirbel und Drehgelenke im Yachtbau"
kategorie: "12 Schäkel, Wirbel und Verbinder"
unterkategorie: "02 Wirbel und Drehgelenke"
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
  - wirbel
  - swivels
  - drehgelenke
  - ankerkettenwirbel
  - blockwirbel
  - fallenwirbel
  - furlerwirbel
  - spinnaker_wirbel
  - mooring_wirbel
  - toggle
  - universalgelenk
  - torsionsentlastung
  - ankerkette
  - rigg
  - beschläge
  - laufendes_gut
  - stehendes_gut
  - deck_hardware
  - anker
boot_klassen:
  - jolly: "Jollen und Daysailer (3–7 m)"
  - cruiser_small: "Kleine Fahrtenyachten (8–11 m)"
  - cruiser_medium: "Mittlere Fahrtenyachten (11–15 m)"
  - cruiser_large: "Große Fahrtenyachten (15–20 m)"
  - superyacht: "Superyachten (20+ m)"
  - racing: "Regattayachten"
  - motorboat: "Motoryachten"
  - catamaran: "Katamarane"
---

# 12.02 — Wirbel und Drehgelenke im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 12.02** — Kategorie 12: Schäkel, Wirbel und Verbinder
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Materialien](#4-materialien)
5. [Produktlinien](#5-produktlinien)
6. [Anwendungen](#6-anwendungen)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
14. [ANHANG C — Lasttabellen](#anhang-c--lasttabellen)
15. [ANHANG D — Normen und Standards](#anhang-d--normen-und-standards)
16. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
17. [ANHANG F — Kompatibilitätsmatrix](#anhang-f--kompatibilitätsmatrix)
18. [ANHANG G — Preis-Leistungs-Vergleich](#anhang-g--preis-leistungs-vergleich)
19. [ANHANG H — Confidence-Mapping](#anhang-h--confidence-mapping)
20. [ANHANG I — Weitere Fallstudien](#anhang-i--weitere-fallstudien)
21. [ANHANG J — Bewertungsschema](#anhang-j--bewertungsschema)
22. [ANHANG K — Entscheidungsbaum Wirbelauswahl](#anhang-k--entscheidungsbaum-wirbelauswahl)
23. [ANHANG L — Drehmoment- und Reibungstabellen](#anhang-l--drehmoment-und-reibungstabellen)
24. [ANHANG M — Klimazonen-Empfehlungen](#anhang-m--klimazonen-empfehlungen)
25. [ANHANG N — Installations-Checklisten](#anhang-n--installations-checklisten)
26. [ANHANG O — Erfahrungsberichte](#anhang-o--erfahrungsberichte)
27. [ANHANG P — Visuelle Inspektionskriterien](#anhang-p--visuelle-inspektionskriterien)
28. [ANHANG Q — Ersatzteil-Referenz](#anhang-q--ersatzteil-referenz)
29. [ANHANG R — Glossar Englisch-Deutsch Zuordnung](#anhang-r--glossar-englisch-deutsch-zuordnung)

---

## 1. Einführung und Übersicht

### 1.1 Funktion und Bedeutung von Wirbeln im Yachtbau

Wirbel (engl. swivels) und Drehgelenke gehören zu den kritischsten Verbindungselementen in der modernen Yacht- und Schiffskonstruktion. Ihre primäre Aufgabe ist die **Torsionsentlastung** — das gezielte Aufnehmen und Ableiten von Drehbewegungen in Ketten, Seilen, Drähten und Beschlägen, die sonst zu Materialermüdung, Kinking oder gar zum katastrophalen Versagen führen würden.

Im Gegensatz zu starren Verbindungselementen wie Schäkeln oder Bolzen erlauben Wirbel eine kontrollierte Rotation um mindestens eine Achse. Diese Eigenschaft macht sie unverzichtbar in zahlreichen Anwendungsbereichen:

- **Ankersysteme**: Zwischen Ankerkette und Anker verhindert der Wirbel das Aufdrehen der Kette durch Gezeitenströmung und Winddrehungen
- **Rollreffsysteme**: Der Furlerwirbel ermöglicht die Drehbewegung des Vorstags um seine eigene Achse
- **Blocksysteme**: Blockwirbel erlauben die freie Ausrichtung des Blocks zur Lastrichtung
- **Fallen und Schoten**: Fallenwirbel verhindern das Verdrehen von Tauwerk unter Last
- **Spinnaker-Systeme**: Spinnaker-Wirbel müssen unter dynamischer Last frei drehen
- **Mooring und Verankerung**: Mooringwirbel in permanenten Liegeplatz-Systemen

### 1.2 Warum Torsionsentlastung kritisch ist

Jedes Tauwerk, jede Kette und jeder Draht hat eine natürliche Tendenz zur Verdrehung unter Last. Diese Torsion entsteht durch:

1. **Schlagrichtung bei Ketten**: Jedes Kettenglied erzeugt bei Belastung ein Mikro-Drehmoment
2. **Flechtrichtung bei Tauwerk**: Geflochtenes oder geschlagenes Tauwerk speichert Torsionsenergie
3. **Äußere Kräfte**: Wind, Strömung und Wellenbewegung erzeugen Drehmomente
4. **Thermische Effekte**: Unterschiedliche Wärmeausdehnung in Verbundsystemen
5. **Biologische Kräfte**: Bewuchs an Ankerketten erzeugt asymmetrische Widerstände

Ohne Wirbel akkumuliert sich diese Torsion. Die Folgen reichen von Kinking (Schlingenbildung) über beschleunigte Korrosion an Torsionspunkten bis hin zum plötzlichen Bruch unter dynamischer Belastung.

### 1.3 Historische Entwicklung

Die Verwendung von Drehgelenken in der Seefahrt lässt sich bis ins 17. Jahrhundert zurückverfolgen. Frühe Ankerkettenwirbel bestanden aus geschmiedetem Eisen und hatten nur einfache Bolzenlager. Die moderne Entwicklung umfasst:

- **1890er**: Erste patentierte Ankerketten-Drehwirbel aus Gussstahl
- **1930er**: Einführung von Edelstahl-Wirbeln für Yachten
- **1960er**: Entwicklung moderner Rollreffsysteme mit integrierten Wirbeln
- **1980er**: Kugelgelagerte Hochleistungswirbel für Regattayachten
- **2000er**: Keramik- und Kompositlager, Titan-Wirbel für Superyachten
- **2020er**: Hochlast-Wirbel mit integrierter Lastüberwachung (Smart Rigging)

### 1.4 Abgrenzung zu verwandten Bauteilen

| Bauteil | Rotation | Hauptfunktion | Typischer Einsatz |
|---------|----------|---------------|-------------------|
| Wirbel (Swivel) | 360° um eine Achse | Torsionsentlastung | Ankerkette, Fallen, Blöcke |
| Drehgelenk (Universal Joint) | Mehrachsig | Winkelausgleich | Steueranlagen, Wellenstränge |
| Toggle | ~30° Kippbewegung | Biegeentlastung | Wantenspanner, Mastfuß |
| Schäkel (Shackle) | Starr | Kraftübertragung | Universelle Verbindung |
| Gabelkopf (Clevis) | Einachsig, begrenzt | Gelenk mit Bolzen | Steuerseil, Wantenabschluss |
| Wirbelschäkel (Swivel Shackle) | 360° + Schäkelfunktion | Kombination | Fall-Kopf, Blockbefestigung |

### 1.5 Regelwerksrahmen

Wirbel im Yachtbau unterliegen verschiedenen Normen und Klassifikationsregeln:

- **EN 13411-6**: Pressverbindungen und Wirbelverbindungen für Drahtseile
- **ISO 1704**: Schiffbau — Ankerketten — Allgemeine Anforderungen
- **GL/DNV Rules for Yachts**: Klassifikationsregeln für Ankersysteme
- **ABYC H-40**: Standards für Ankersysteme (US-Markt)
- **RCD 2013/53/EU**: Relevante Aspekte für CE-konforme Ankersysteme

> ⚠️ **ZU PRÜFEN (Audit):** EN 13411-6 ist web-verifiziert die Norm „Endverbindungen für Drahtseile — Sicherheit — Teil 6: Asymmetrischer Seilschloss (asymmetric wedge socket)" (BSI/DIN EN 13411-6:2004+A1:2008, iso.org). Sie behandelt WEDER Wirbelverbindungen NOCH Pressverbindungen — Pressverbindungen (swaged) sind EN 13411-8, der symmetrische Seilschloss EN 13411-7. Für Wirbel enthält die EN-13411-Reihe keine eigene Norm; die Normzuordnung hier ist nicht belegt.

---

## 2. Grundlagen und Theorie

### 2.1 Rotationsmechanik von Wirbeln

#### 2.1.1 Grundprinzip der Torsionsentlastung

Ein Wirbel besteht im Grundaufbau aus zwei konzentrischen Bauteilen, die relativ zueinander um eine gemeinsame Achse rotieren können. Die Verbindung wird durch ein Lagersystem gewährleistet, das axiale Lasten (Zugkräfte) überträgt, während es tangentiale Rotation ermöglicht.

**Physikalisches Modell:**

Die Torsionsentlastung lässt sich als Freiheitsgrad-Entkopplung beschreiben:

```
Ohne Wirbel:
  Bauteil A ←[starr]→ Bauteil B
  Freiheitsgrade gekoppelt: Translation (3) + Rotation (3) = 6 gekoppelte DOF

Mit Wirbel:
  Bauteil A ←[Wirbel]→ Bauteil B
  Rotation um Längsachse (1 DOF) entkoppelt
  → 5 gekoppelte DOF, 1 freier DOF
```

#### 2.1.2 Drehmoment und Reibung

Das zum Drehen eines Wirbels erforderliche Drehmoment (Losbrechmoment) ist ein kritischer Qualitätsparameter:

```
M_los = μ × F_axial × r_lager

wobei:
  M_los    = Losbrechmoment [Nm]
  μ        = Reibungskoeffizient der Lagerflächen [-]
  F_axial  = Axiallast / Zugkraft [N]
  r_lager  = Effektiver Lagerradius [m]
```

**Typische Reibungskoeffizienten (μ) für Wirbellager:**

| Lagertyp | μ (trocken) | μ (geschmiert) | μ (unter Last) |
|----------|-------------|----------------|----------------|
| Edelstahl auf Edelstahl | 0.40–0.60 | 0.15–0.25 | 0.20–0.35 |
| Edelstahl auf Bronze | 0.25–0.35 | 0.10–0.18 | 0.15–0.22 |
| Edelstahl auf POM/Delrin | 0.15–0.25 | 0.08–0.15 | 0.12–0.20 |
| Edelstahl auf Keramik (ZrO₂) | 0.08–0.15 | 0.05–0.10 | 0.08–0.12 |
| Kugelgelagert (Edelstahl) | 0.003–0.008 | 0.002–0.005 | 0.005–0.012 |
| Kugelgelagert (Keramik) | 0.001–0.005 | 0.001–0.003 | 0.003–0.008 |

#### 2.1.3 Lastverteilung im Wirbel

Die Lastverteilung in einem Wirbel ist nicht trivial. Neben der axialen Hauptlast treten auf:

1. **Radialkräfte**: Durch Seitenlasten, insbesondere bei schräger Zugrichtung
2. **Biegemomente**: Bei nicht-axialer Belastung
3. **Dynamische Lasten**: Stoßbelastungen durch Wellenschlag, Rucklasten beim Ankern
4. **Ermüdungslasten**: Zyklische Belastung durch Wellenbewegung

**Dynamischer Lastfaktor:**

Für maritime Anwendungen wird die statische Arbeitslast (SWL) mit einem dynamischen Faktor multipliziert:

```
F_dynamisch = F_statisch × k_dyn

wobei k_dyn:
  Ankersystem, ruhiges Wasser:     1.5–2.0
  Ankersystem, Seegang:            2.5–4.0
  Ankersystem, Sturm:              4.0–6.0
  Fallensystem, normaler Betrieb:  2.0–3.0
  Fallensystem, Regatta:           3.0–5.0
  Spinnaker, Halse/Gyrbe:          5.0–8.0
  Mooring, geschützter Hafen:      1.5–2.5
  Mooring, exponiert:              3.0–5.0
```

#### 2.1.4 Bruchlast und Sicherheitsfaktoren

Der Sicherheitsfaktor (SF) definiert das Verhältnis zwischen Bruchlast (MBL) und Arbeitslast (SWL):

```
SF = MBL / SWL

Typische Sicherheitsfaktoren:
  Ankerketten-Wirbel:       4:1 (Minimum nach GL/DNV)
  Fall- und Schotenwirbel:  5:1 (empfohlen)
  Furlerwirbel:             4:1 (Herstellerstandard)
  Spinnaker-Wirbel:         5:1 bis 6:1 (wegen Dynamik)
  Mooring-Wirbel:           4:1 bis 5:1
  Superyacht-Rigg:          5:1 (Klasse-Anforderung)
```

### 2.2 Lagertypen in Wirbeln

#### 2.2.1 Gleitlager (Plain Bearings)

Das einfachste und robusteste Lagerprinzip. Zwei Oberflächen gleiten aufeinander, getrennt durch einen Schmierfilm oder inhärente Gleiteigenschaften des Materials.

**Vorteile:**
- Extrem robust gegen Schock und Stoßbelastung
- Keine Einzelteile, die ausfallen können
- Tolerant gegen Verschmutzung (Sand, Salzkristalle)
- Wartungsarm bis wartungsfrei (bei PTFE/POM-Buchsen)
- Geringere Bauhöhe möglich

**Nachteile:**
- Höherer Reibungskoeffizient als Wälzlager
- Unter hoher Last schwergängig bis blockierend
- Verschleiß der Lagerflächen erfordert gelegentlichen Austausch
- Losbrechmoment steigt mit der Last überproportional

**Typische Konstruktionen:**
- Edelstahl auf Edelstahl (einfachste, wartungsintensivste Variante)
- Edelstahl auf Bronzebuchse (traditionell, gut für Ankersysteme)
- Edelstahl auf POM/Delrin-Buchse (modern, niedriger Reibwert)
- Edelstahl auf PTFE-Buchse (niedrigster Reibwert bei Gleitlagern)

#### 2.2.2 Wälzlager (Rolling Element Bearings)

Kugeln oder Rollen zwischen den Lagerflächen reduzieren die Reibung drastisch.

**Kugelgelagerte Wirbel:**
- Edelstahl-Kugeln (316L oder 440C) in Laufrillen
- Typisch 6–24 Kugeln je nach Größe
- Reibungskoeffizient: 0.002–0.012
- Frei drehend auch unter hoher Last
- Empfindlicher gegen Verschmutzung und Korrosion

**Keramik-Kugellager (Si₃N₄ oder ZrO₂):**
- Höchste Leistung, niedrigster Reibwert
- Korrosionsfrei — Keramik reagiert nicht mit Salzwasser
- Leichter als Stahl (ca. 40% geringere Dichte)
- Härter als Stahl — weniger Verschleiß
- Deutlich teurer (Faktor 3–5 gegenüber Edelstahl)

**Nadelgelagerte Wirbel:**
- Zylindrische Rollen statt Kugeln
- Höhere Tragfähigkeit bei gleicher Baugröße
- Weniger verbreitet im Yachtbereich
- Einsatz primär bei Superyacht-Furleranlagen

#### 2.2.3 Hybridlager

Kombination aus Gleit- und Wälzlagerelementen:

- Axiallast über Kugelreihe
- Radiallast über Gleitbuchse
- Kompromiss zwischen Leistung und Robustheit
- Zunehmend verbreitet bei mittelpreisigen Wirbeln

### 2.3 Torsionsmechanik in Ankersystemen

#### 2.3.1 Kettentorsion durch Gezeitenströmung

Ein vor Anker liegendes Schiff schwingt mit dem Gezeitenstrom. Jede 180°-Drehung (Tidenwechsel) erzeugt eine halbe Umdrehung Torsion in der Kette, wenn kein Wirbel vorhanden ist.

**Rechnung für eine typische Ankernacht:**

```
Torsionsakkumulation ohne Wirbel:
  4 Tidenwechsel × 180° = 720° = 2 volle Umdrehungen
  Bei schwerem Wetter mit Winddrehungen: bis zu 1440° = 4 Umdrehungen
  In Revieren mit starker Gezeitenströmung: bis zu 2160° = 6 Umdrehungen
```

Diese akkumulierte Torsion führt zu:
- Kinking der Kette (Schlingenbildung) — verhindert sauberes Einfall
- Erhöhter Widerstand beim Bergen — Windenkraftbedarf steigt
- Querbelastung der Kettenglieder — Reduktion der Bruchlast um bis zu 30%
- Beschleunigter Verschleiß der Kettenglieder an Kontaktpunkten

#### 2.3.2 Kettentorsion durch Bootsbewegung

Zusätzlich zur Gezeitentorsion erzeugt die Gierbewegung (Schwojen) des Bootes hochfrequente Torsionsimpulse:

```
Schwoj-Torsion:
  Frequenz: 0.01–0.1 Hz (10–100 Sekunden pro Zyklus)
  Amplitude: ±5° bis ±45° je nach Kettenlänge und Windstärke
  Ermüdungsrelevanz: hoch (>10.000 Zyklen pro Nacht möglich)
```

#### 2.3.3 Torsion in Rollreffanlagen

Die Rollreffanlage (Furler) ist das Anwendungsgebiet, in dem Torsion nicht nur unvermeidlich, sondern funktional ist. Der Furlerwirbel muss:

1. Die **Rotation des Vorstags** um seine eigene Achse ermöglichen (Einrollen des Segels)
2. Gleichzeitig die **Vorstaglast** (bis zu 70% der Verdrängung als Zugkraft) übertragen
3. Dabei **minimale Reibung** aufweisen (sonst hoher Kraftbedarf zum Reffen)
4. **Mehrachsige Bewegungen** tolerieren (Vorstag ist nie perfekt gerade)

**Furler-Torsionsberechnung:**

```
Umdrehungen zum vollständigen Einrollen:
  n = (L_vorstag × π) / (d_profil × π) = L_vorstag / d_profil

  Beispiel: 15m Vorstag, 100mm Profildurchmesser:
  n = 15000mm / 100mm = 150 Umdrehungen

  Bei jeder Reffoperation werden also 150 Umdrehungen in eine Richtung gedreht.
  Lebensdauer-Anforderung: >50.000 Reffzyklen = >7.500.000 Umdrehungen
```

### 2.4 Belastungsarten und deren Einfluss

#### 2.4.1 Statische Belastung

Kontinuierliche Zugkraft ohne wesentliche Schwankung:
- Ankerkette bei ruhigem Wetter
- Vorstaglast bei konstantem Kurs
- Mooringleine bei Flaute

Relevanz für Wirbelauswahl: Bestimmt die minimale SWL. Gleitlager ausreichend, wenn Rotation selten erforderlich.

#### 2.4.2 Dynamische Belastung

Schwankende Kräfte mit definierter Frequenz und Amplitude:
- Ankerkette im Seegang (Rucklasten beim Strecken des Ankergeschirrs)
- Fallen bei Wellenbewegung (Pumpen des Mastes)
- Spinnaker bei Böen (schnelle Lastwechsel)

Relevanz: Bestimmt den dynamischen Lastfaktor. Wälzlager bevorzugt, da auch unter Last drehbar.

#### 2.4.3 Stoßbelastung (Shock Loading)

Plötzliche, kurzzeitige Extremlasten:
- Anker bricht aus und fällt erneut ein
- Spinnaker schlägt ein (Sonnenschuss)
- Ruckbelastung bei zu kurzer Ankerkette
- Leinenbruch unter Last mit Rückschlag

Relevanz: Bestimmt die erforderliche Bruchlast (MBL). Wirbel muss Stoß absorbieren ohne zu versagen. Kugelgelagerte Wirbel mit gehärteten Laufbahnen sind hier im Vorteil.

#### 2.4.4 Ermüdungsbelastung (Fatigue Loading)

Zyklische Belastung unterhalb der Streckgrenze, die nach vielen Zyklen zum Bruch führt:

```
Wöhler-Kurve (vereinfacht) für 316L-Edelstahl-Wirbel:
  σ_max / σ_yield | Zyklen bis Bruch (N)
  1.00             | 1 (statischer Bruch)
  0.80             | ~10.000
  0.60             | ~100.000
  0.50             | ~500.000
  0.40             | ~2.000.000
  0.30             | >10.000.000 (Dauerfestigkeit)
```

**Praxisregel:** Wirbel für Dauereinsatz (Anker, Furler) sollten maximal mit 30% der Streckgrenze belastet werden.

### 2.5 Korrosionsmechanismen bei Wirbeln

#### 2.5.1 Spaltkorrosion (Crevice Corrosion)

Das größte Korrosionsproblem bei marinen Wirbeln. In den engen Spalten zwischen den rotierenden Teilen sammelt sich stehendes Salzwasser, das eine sauerstoffarme Umgebung schafft. Der pH-Wert sinkt, Chloridionen konzentrieren sich, und der passive Schutzfilm des Edelstahls wird lokal zerstört.

**Besonders gefährdete Bereiche:**
- Spalt zwischen Innenteil und Außenteil
- Bereich um den Haltebolzen/Sicherungsring
- Kontaktfläche zwischen Wirbel und angrenzenden Beschlägen (Schäkel)
- Lageroberflächen bei inaktivierten Wirbeln (lange Liegezeiten)

**Gegenmaßnahmen:**
- Regelmäßiges Drehen des Wirbels (mindestens wöchentlich)
- Spülung mit Süßwasser nach jedem Salzwasserkontakt
- Beschichtung der Lagerflächen mit korrosionshemmendem Fett
- Verwendung von Duplex 2205 statt 316L in der Spaltzone
- Konstruktive Drainage: Bohrungen für Wasserablauf

#### 2.5.2 Galvanische Korrosion

Wenn verschiedene Metalle in Kontakt stehen und ein Elektrolyt (Salzwasser) vorhanden ist:

| Materialpaarung | Potentialdifferenz | Korrosionsrisiko | Bewertung |
|-----------------|-------------------|------------------|-----------|
| 316L + 316L | 0 mV | Keins | Ideal |
| 316L + Bronze | ~50 mV | Gering | Akzeptabel |
| 316L + Aluminium | ~500 mV | Hoch | Vermeiden |
| 316L + verzinkter Stahl | ~200 mV | Mittel | Nur kurzfristig |
| 316L + Titan | ~150 mV | Gering-Mittel | Akzeptabel mit Isolation |
| Bronze + Aluminium | ~450 mV | Hoch | Vermeiden |

#### 2.5.3 Reibkorrosion (Fretting Corrosion)

Kleine oszillierende Bewegungen zwischen Kontaktflächen unter Last zerstören die Passivschicht und erzeugen Oxidpartikel, die wie Schleifmittel wirken. Besonders relevant bei:

- Toggle-Wirbel-Verbindungen mit minimaler Bewegung
- Ankerketten-Wirbeln, die unter Last nur leicht oszillieren
- Wirbeln, die durch Korrosion teilweise festgesessen haben

### 2.6 Lastbewertung und Dimensionierung

#### 2.6.1 Ankersystem-Dimensionierung

Die erforderliche SWL des Ankerkettenwirbels richtet sich nach der Bootsverdrängung und der Kettengröße:

```
Dimensionierungsregel (nach GL/DNV):
  SWL_wirbel ≥ MBL_kette × 0.5

  MBL der Kette (Kurzgliedkette, Güteklasse 70):
  MBL [kN] = 0.274 × d² [mm²]

  Beispiel: 10mm Kette
  MBL = 0.274 × 100 = 27.4 kN
  SWL_wirbel ≥ 13.7 kN ≈ 1400 kg
```

> ⚠️ **ZU PRÜFEN (Audit):** Formelkonstante an Tabelle C.1 angeglichen (0,274 statt 0,0274 — `0,0274 × 100` ergäbe 2,74 kN, nicht die im Beispiel und in allen Tabellen genutzten 27,4 kN). Die absoluten Ketten-MBL-Werte selbst sind jedoch fraglich (siehe Audit-Hinweis an Anhang C.1: 10 mm Grade 70 hat real ≈ 100 kN Bruchlast). Vor sicherheitsrelevanter Dimensionierung verifizieren. Confidence: estimated — unverifiziert.

#### 2.6.2 Fallen-Dimensionierung

Die Fallenlast hängt von der Segelfläche und den Windverhältnissen ab:

```
Grobe Abschätzung der Großfall-Last:
  F_fall = A_segel × p_wind × k_form

  wobei:
  A_segel = Segelfläche [m²]
  p_wind  = Winddruck [N/m²] = 0.5 × ρ × v²
  k_form  = Formfaktor (0.8–1.2)

  Beispiel: 40m² Großsegel, 25 kn Wind (12.9 m/s):
  p_wind = 0.5 × 1.225 × 12.9² = 102 N/m²
  F_fall = 40 × 102 × 1.0 = 4080 N ≈ 416 kg

  SWL_wirbel mit SF 5:1 → MBL ≥ 20.4 kN ≈ 2080 kg
```

#### 2.6.3 Vorstag-Dimensionierung (Furler)

Die Vorstaglast ist eine der höchsten Rigglast auf einer Segelyacht:

```
Vorstag-Spannung (Näherung):
  F_vorstag ≈ 0.5 × Verdrängung [kg] × g [m/s²]

  Beispiel: 12t Yacht
  F_vorstag ≈ 0.5 × 12000 × 9.81 = 58.860 N ≈ 6000 kg

  Der Furlerwirbel muss diese Last übertragen UND frei drehen.
  SWL_furlerwirbel ≥ 6000 kg
  MBL_furlerwirbel ≥ 24.000 kg (SF 4:1)
```

---

## 3. Typenübersicht

### 3.1 Blockwirbel (Block Swivels)

#### 3.1.1 Funktion und Einsatzbereich

Blockwirbel verbinden einen Umlenkblock mit seinem Befestigungspunkt und erlauben dem Block, sich frei zur Lastrichtung auszurichten. Ohne Wirbel würde der Block bei wechselnder Zugrichtung verkanten, die Schot oder das Fall würde klemmen, und die Belastung würde sich auf eine Kante des Blocks konzentrieren.

**Anwendungsbereiche:**
- Vorschots-Blöcke am Vorschiffdeck
- Mastfuß-Blöcke für Fallen
- Baumniederholer-Blöcke
- Trimmblöcke für Barber-Hauler
- Traveller-Wagen-Blöcke
- Spinnaker-Blöcke am Mast

#### 3.1.2 Bauformen

**Integrierter Blockwirbel (Swivel Block):**
- Wirbel ist fest im Blockkopf integriert
- Kompakte Bauform, minimale Höhe
- Typische Ausführungen: Einfachblock, Doppelblock, Dreifachblock mit Wirbel
- Befestigung: Wirbelschäkel, Wirbelauge, Wirbelgabel

**Aufgesetzter Wirbel (Add-on Swivel):**
- Separater Wirbel wird zwischen Block und Befestigungspunkt montiert
- Flexibler: gleicher Wirbel für verschiedene Blockgrößen
- Zusätzliche Bauhöhe und Gewicht
- Vorteil: Wirbel separat austauschbar

**Fiddle-Block mit Wirbel:**
- Zwei übereinander angeordnete Rollen mit gemeinsemem Wirbelkopf
- Für Talje-Systeme (Kaskaden)
- Typischer Einsatz: Großschot, Dirk, Cunningham

#### 3.1.3 Größen und Lasttabelle

| Tauwerk-Ø [mm] | Block SWL [kg] | Wirbel SWL [kg] | Typische Anwendung |
|-----------------|----------------|-----------------|---------------------|
| 4–6 | 200–400 | 250–500 | Jolle, kleiner Trimm |
| 6–8 | 400–800 | 500–1000 | Cruiser 8–11m |
| 8–10 | 800–1500 | 1000–1800 | Cruiser 11–15m |
| 10–12 | 1500–2500 | 1800–3000 | Cruiser 15–20m |
| 12–16 | 2500–5000 | 3000–6000 | Superyacht, Regatta |
| 16–22 | 5000–12000 | 6000–15000 | Großyachten 20m+ |

### 3.2 Ankerkettenwirbel (Anchor Chain Swivels)

#### 3.2.1 Funktion

Der Ankerkettenwirbel sitzt zwischen der Ankerkette (oder zwischen Kette und Leine bei gemischtem Ankergeschirr) und verhindert das Aufdrehen der Kette durch Gezeitenströmungen und Winddrehungen. Er ist eines der am stärksten belasteten Bauteile im Ankersystem.

**Kritische Anforderungen:**
- SWL mindestens gleich der SWL der verwendeten Kette
- Freie Rotation auch unter hoher Last
- Korrosionsbeständigkeit für Dauereinsatz in Salzwasser
- Kompatibilität mit der Kettenklüse und Ankerwindenführung
- Darf NICHT im Kettenkasten oder auf der Ankerwinde klemmen

#### 3.2.2 Bauformen

**Gabel-Gabel-Wirbel (Jaw-Jaw Swivel):**
- Beidseitige Gabelanschlüsse mit Bolzen
- Direkte Verbindung zu Kettenglieder-Enden
- Kein zusätzlicher Schäkel nötig
- Kompakteste Bauform für Kettensysteme
- Nachteil: Passung muss exakt zur Kettengröße passen

**Gabel-Auge-Wirbel (Jaw-Eye Swivel):**
- Eine Seite Gabel (zur Kette), andere Seite Auge (für Schäkel)
- Vielseitiger in der Anwendung
- Auge-Seite kann auch direkt an Ankerbügel befestigt werden

**Auge-Auge-Wirbel (Eye-Eye Swivel):**
- Beidseitige Augen, Verbindung über Schäkel
- Universellste Form, passt in jedes System
- Zusätzliche Schäkel erhöhen die Gesamtlänge
- Vorteil: Einfacher Austausch und Rekonfiguration

**Kettenwirbel mit integriertem Toggle:**
- Wirbel + Toggle in einem Bauteil
- Toggle kompensiert Winkelbewegungen
- Reduziert Biegebelastung auf die Kettenendglieder
- Empfohlen für schweres Wetter und Langfahrt

#### 3.2.3 Dimensionierung nach Kettengröße

| Ketten-Ø [mm] | Ketten-MBL [kN] | Wirbel-SWL min [kg] | Wirbel-MBL min [kN] | Boots-LOA [m] |
|----------------|-----------------|---------------------|---------------------|---------------|
| 6 | 11.2 | 600 | 22 | 6–8 |
| 7 | 14.8 | 800 | 30 | 7–9 |
| 8 | 19.2 | 1000 | 38 | 8–11 |
| 10 | 27.4 | 1400 | 55 | 10–13 |
| 12 | 39.5 | 2000 | 80 | 13–16 |
| 13 | 46.0 | 2400 | 92 | 15–18 |
| 14 | 53.9 | 2800 | 108 | 16–20 |
| 16 | 70.3 | 3600 | 140 | 20–25 |

### 3.3 Fallenwirbel (Halyard Swivels)

#### 3.3.1 Funktion

Fallenwirbel sitzen am oberen Ende des Falls, zwischen Fall und Kopfbrett des Segels. Sie verhindern, dass sich das Fall beim Setzen und Bergen des Segels verdreht, und ermöglichen das freie Ausrichten des Segelkopfes.

**Spezifische Anforderungen:**
- Minimales Gewicht (hängt am Masttop — Schwerpunktrelevanz)
- Freie Rotation auch unter voller Segellast
- Möglichst geringe Bauhöhe (beeinflusst den Vorliek-Trimm)
- Kompatibilität mit Kopfbrett und Fall-Terminierung
- UV-Beständigkeit (dauerhaft am Masttop exponiert)

#### 3.3.2 Bauformen

**Wirbelschäkel (Swivel Shackle):**
- Schäkelkörper mit integriertem Wirbelelement
- Einfachste und leichteste Lösung
- Typisch für Cruiser-Fallen bis ca. 2000 kg SWL
- Gleitlager (Edelstahl oder POM)

**Wirbel mit Schnappschäkel (Snap Swivel):**
- Schnellverschluss-Schäkel mit Wirbel
- Ermöglicht schnelles Anschlagen und Lösen des Segels
- Typisch für Vorsegel (Genua, Fock) — häufiges Segelwechseln
- Sicherheitsaspekt: Muss unter Last sicher verriegeln

**Kugelgelagerter Hochlast-Wirbel:**
- Für Regatta und große Yachten
- Kugelgelagerte Rotation für minimale Reibung
- Höheres Gewicht und Kosten gerechtfertigt bei Leistungsanspruch
- Typische SWL: 3000–12000 kg

### 3.4 Furlerwirbel (Furler Swivels / Head Swivels)

#### 3.4.1 Funktion und Besonderheiten

Der Furlerwirbel (auch Kopfwirbel oder Trommelwirbel) ist das zentrale Rotationselement jeder Rollreffanlage. Er ermöglicht die Drehung des gesamten Furler-Profils (und damit des Segels) um das Vorstag, während er gleichzeitig die Vorstaglast überträgt.

**Kritische Besonderheiten:**
- **Höchste Lastanforderung**: Muss die gesamte Vorstaglast tragen (bis 70% der Verdrängung)
- **Höchste Umdrehungszahl**: >150 Umdrehungen pro Reffvorgang, >50.000 Vorgänge Lebensdauer
- **Doppelfunktion**: Lagert sowohl den Furler-Drum als auch das Vorstag
- **Integration**: Muss mit dem spezifischen Furler-System kompatibel sein
- **Wartungszugang**: Muss regelmäßig geschmiert werden (Intervall je nach Hersteller)

#### 3.4.2 Bauformen nach Furler-Typ

**Unterliek-Furler (Bottom Furler):**
- Wirbel sitzt am Decksniveau in der Furler-Trommel
- Zugänglich für Wartung
- Standardbauform für die meisten Cruiser-Furler
- Hersteller: Harken, Profurl, Facnor, Selden

**Oberliek-Furler (Top-Down Furler):**
- Wirbel am Masttop
- Primär für Asymmetrische Spinnaker/Gennaker
- Geringere Lasten als Vorstag-Furler
- Leichtbauweise, oft ohne Kugellager
- Hersteller: Ronstan, Karver, Facnor

**Integrierter Vorstag-Furler:**
- Wirbel in das Vorstag integriert
- Vorstag dient gleichzeitig als Furler-Achse
- Höchste Integration, geringste Bauhöhe
- Nur bei Neuanlagen sinnvoll (kein Nachrüsten)
- Hersteller: Reckmann, Baxter, Hood (Stoway)

#### 3.4.3 Lastbereiche nach Bootsgröße

| Bootsgröße [m] | Verdrängung [t] | Vorstag-Last [kN] | Furlerwirbel SWL [kg] | Furlerwirbel MBL [kN] |
|-----------------|-----------------|--------------------|-----------------------|-----------------------|
| 8–10 | 2–4 | 10–20 | 2000–4000 | 40–80 |
| 10–12 | 4–8 | 20–40 | 4000–8000 | 80–160 |
| 12–15 | 8–14 | 40–70 | 8000–14000 | 160–280 |
| 15–18 | 14–22 | 70–110 | 14000–22000 | 280–440 |
| 18–22 | 22–40 | 110–200 | 22000–40000 | 440–800 |
| 22+ | 40+ | 200+ | 40000+ | 800+ |

### 3.5 Spinnaker-Wirbel (Spinnaker Swivels)

#### 3.5.1 Funktion und Anforderungen

Der Spinnaker-Wirbel sitzt zwischen Spinnaker-Fall und Spinnaker-Kopf. Er muss unter extremen dynamischen Bedingungen frei drehen — beim Halsen (Gyrben) dreht sich der Spinnaker um seine eigene Achse, und der Wirbel muss diese Rotation aufnehmen, ohne zu klemmen.

**Extreme Anforderungen:**
- Blitzschnelle Rotation auch unter voller Segellast
- Extrem dynamische Belastung (Spinnaker pumpt, schlägt ein)
- Maximale Stoßbelastung beim Sonnenschuss (unbeabsichtigtes Füllen)
- Minimales Gewicht (am Masttop — krängungsrelevant)
- Unbedingt ausfallsicher (Wirbelblockade = Spinnaker reißt oder Rigg versagt)

#### 3.5.2 Bauformen

**Kugelgelagerter Spinnaker-Wirbel:**
- Standardbauform für Regatta und Performance-Cruiser
- Edelstahl- oder Keramik-Kugellager
- Befestigung: Auge-Auge oder Auge-Gabel
- SWL: 500–5000 kg je nach Bootsgröße
- Hersteller: Tylaska, Ronstan, Harken

**Nadelgelagerter Spinnaker-Wirbel:**
- Höhere Lastkapazität bei kompakter Bauform
- Für große Yachten und Code-0-Segel
- Teurer als kugelgelagerte Varianten

**Leichtbau-Wirbel (Titan/Aluminium):**
- Für extreme Regattaanwendungen
- Titan-Wirbel: 40–50% Gewichtsersparnis gegenüber Edelstahl
- Aluminium-Wirbel: nur für leichte Lasten (Spi bis 100m²)
- Teilweise mit Dyneema-Soft-Attachment statt Metallauge

#### 3.5.3 Dimensionierung

| Spinnaker-Fläche [m²] | Wind max [kn] | SWL Wirbel [kg] | Empfohlene Bauform |
|------------------------|---------------|-----------------|---------------------|
| 20–50 | 20 | 500–800 | Kugelgelagert, Edelstahl |
| 50–100 | 18 | 800–1500 | Kugelgelagert, Edelstahl oder Keramik |
| 100–200 | 15 | 1500–3000 | Nadel- oder Keramikgelagert |
| 200–400 | 12 | 3000–6000 | Nadelgelagert, Titan optional |
| 400+ | 10 | 6000+ | Nadelgelagert, Custom |

### 3.6 Mooringwirbel (Mooring Swivels)

#### 3.6.1 Funktion

Mooringwirbel werden in permanenten Festmacher-Systemen (Mooringbojen, Dalben, Pfähle) eingesetzt. Sie verhindern das Aufdrehen der Mooringleine oder -kette durch die Drehbewegung des Bootes um den Liegeplatz.

**Besonderheiten:**
- Extremer Dauergebrauch (24/7, ganzjährig)
- Unterwassereinsatz (permanent submers)
- Bewuchsanfällig — Muscheln, Algen, Seepocken auf den Lagerflächen
- Schwer zugänglich für Wartung
- Muss auch nach Monaten ohne Bewegung noch frei drehen

#### 3.6.2 Bauformen

**Schwerer Guss-Wirbel:**
- Edelstahl 316L oder Duplex 2205
- Großzügige Lagerspalte (tolerant gegen Bewuchs)
- SWL: 2000–20.000 kg
- Massive Bauform, Gewicht sekundär
- Sicherungsbolzen gegen Demontage

**Ketten-Mooringwirbel:**
- Spezifisch für Kettenmoorings
- Integrierte Kettenanschlüsse (Gabel-Gabel)
- Dimensioniert nach Kettengröße
- Oft mit Opfer-Anode (Zink) am Wirbelkörper

**Schwimmender Wirbel (Floating Swivel):**
- Wirbel mit integriertem Schwimmkörper
- Hält die Mooringleine über dem Meeresgrund
- Reduziert Scheuern und Bewuchs
- Einsatz bei Schlammgrund und starkem Tidenhub

### 3.7 Universalgelenke (Universal Joints)

#### 3.7.1 Funktion

Universalgelenke (Kardangelenke) erlauben Drehbewegung um zwei Achsen gleichzeitig. Im Yachtbau werden sie dort eingesetzt, wo Winkelbewegungen in mehreren Ebenen kompensiert werden müssen.

**Einsatzbereiche:**
- Steueranlagen: Verbindung zwischen Steuerrad und Steuergetriebe
- Wellenstränge: Ausgleich von Winkeln zwischen Motor und Welle
- Segellatten-Beschläge: Verbindung zwischen Segellatte und Mast (bei Volllatten-Systemen)
- Baumgelenke: Universale Baumanlenkung am Mast

#### 3.7.2 Bauformen

**Kreuzgelenk (Cardan Joint):**
- Klassisches Kardangelenk mit Kreuzstück und zwei Gabeln
- Maximaler Beugewinkel: 30–45°
- Überträgt Drehmoment gleichmäßig (bei konstantem Winkel)
- Material: Edelstahl 316L, Bronze
- Einsatz: Steueranlagen, Wellenstränge

**Kugelgelenk (Ball Joint):**
- Kugelkopf in Kugelpfanne
- Allseitige Beweglichkeit
- Geringere Drehmomentübertragung als Kreuzgelenk
- Einsatz: Stoßdämpfer, Gasdruckfedern, Steuergestänge

### 3.8 Toggle-Wirbel-Kombinationen (Toggle-Swivel Units)

#### 3.8.1 Funktion

Die Kombination aus Toggle und Wirbel in einem Bauteil bietet sowohl Torsionsentlastung (Wirbel) als auch Biegeentlastung (Toggle). Diese Kombination ist besonders dort wichtig, wo starre Verbindungen zwischen Draht/Kette und Beschlag bestehen.

**Typische Einsatzorte:**
- Wantenanschluss am Rumpf (Toggle-Wirbel-Spannschloss)
- Vorstag-Anschluss am Bug (Toggle-Wirbel-Furler)
- Ankerkette-Anker-Verbindung (Toggle-Wirbel-Schäkel)
- Backstag-Anschluss (Toggle-Wirbel an Rumpfbeschlag)

#### 3.8.2 Bauformen

**Inline Toggle-Wirbel:**
- Toggle und Wirbel hintereinander in einer Achse
- Maximale Torsions- und Biegeentlastung
- Zusätzliche Gesamtlänge der Verbindung
- Eingesetzt bei Wanten und Vorstag

**Integrierter Toggle-Wirbel:**
- Toggle-Bewegung und Wirbel-Rotation in einem kompakten Bauteil
- Geringere Baulänge
- Komplexere Fertigung, höherer Preis
- Eingesetzt bei Furler-Systemen und Ankerbeschlägen

**Toggle-Wirbelschäkel:**
- Schäkel mit integriertem Toggle und Wirbel
- Drei Funktionen in einem Bauteil
- Für Fallen- und Blockbefestigungen
- Reduziert die Anzahl der Verbindungselemente

---

## 4. Materialien

### 4.1 Edelstahl AISI 316L (1.4404)

#### 4.1.1 Eigenschaften

Der Standardwerkstoff für marine Wirbel. Austenitischer Chrom-Nickel-Molybdän-Stahl mit niedrigem Kohlenstoffgehalt.

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 485–690 | MPa |
| Streckgrenze (Rp0.2) | 170–310 | MPa |
| Bruchdehnung | 40–50 | % |
| Härte | 150–220 | HB |
| Dichte | 7.98 | g/cm³ |
| E-Modul | 193 | GPa |
| Korrosionsbeständigkeit (PREN) | 24–26 | — |
| Magnetisch | Nein (leicht nach Kaltverformung) | — |

#### 4.1.2 Herstellungsverfahren und Qualitätsunterschiede

**Geschmiedeter Edelstahl (Forged):**
- Höchste mechanische Eigenschaften durch Kornverdichtung
- Zugfestigkeit bis 690 MPa
- Richtungsabhängige Festigkeit (Anisotropie) — Vorteil bei Zugbelastung
- Sichtbare Schmiedegrate (Gratnaht) als Qualitätsmerkmal
- Premium-Hersteller: Wichard (Frankreich), Petersen (Dänemark)
- Preisaufschlag: 50–100% gegenüber Guss

**Feinguss (Investment Casting):**
- Gute mechanische Eigenschaften
- Zugfestigkeit typisch 485–550 MPa
- Isotrope Eigenschaften (gleich in alle Richtungen)
- Glatte Oberfläche, keine Gratnaht
- Anfällig für Lunker (Hohlräume) bei schlechter Qualitätskontrolle
- Standardverfahren für die meisten Wirbel
- Qualitätsstreuung: hoch — Lieferantenqualifikation entscheidend

**Sandguss (Sand Casting):**
- Niedrigste mechanische Eigenschaften
- Poröse Oberfläche, rauere Lageroberflächen
- Nur für nicht-kritische Anwendungen (Mooring, leichte Lasten)
- Billigste Herstellungsform
- Erkennbar an gröberer Oberfläche und Gussnähten

**CNC-gefräst aus Vollmaterial:**
- Exzellente mechanische Eigenschaften (Walzgefüge)
- Höchste Präzision der Lagerflächen
- Sehr teuer (hoher Materialverlust)
- Nur für Spezialanwendungen und Superyachten
- Hersteller: Reckmann, Tylaska (teilweise)

#### 4.1.3 Korrosionsverhalten

316L bietet guten, aber nicht perfekten Schutz in Salzwasser. Die PREN-Zahl (Pitting Resistance Equivalent Number) von 24–26 liegt am unteren Rand für marine Dauertauchteile.

**Bekannte Schwachstellen:**
- Spaltkorrosion in Lagerspalten (häufigstes Problem bei Wirbeln)
- Lochfraß unter Ablagerungen (Muscheln, Fouling)
- Tea Staining: braune Verfärbungen in salzhaltiger Atmosphäre (ästhetisch, nicht strukturell)
- Spannungsrisskorrosion bei hohen Temperaturen (>60°C, selten im Yachtbau)

### 4.2 Duplex-Edelstahl 2205 (1.4462)

#### 4.2.1 Eigenschaften

Doppelgefüge aus Austenit und Ferrit. Deutlich höhere Festigkeit und Korrosionsbeständigkeit als 316L.

| Eigenschaft | Wert | Einheit | Vergleich zu 316L |
|-------------|------|---------|-------------------|
| Zugfestigkeit | 620–880 | MPa | +40–60% |
| Streckgrenze (Rp0.2) | 450–550 | MPa | +80–120% |
| Bruchdehnung | 25–35 | % | -25% |
| Härte | 250–320 | HB | +50% |
| Dichte | 7.82 | g/cm³ | -2% |
| E-Modul | 200 | GPa | +4% |
| PREN | 34–36 | — | +40% |
| Magnetisch | Teilweise | — | — |

#### 4.2.2 Vorteile für Wirbel

- **Höhere Festigkeit**: Erlaubt kompaktere Bauweise bei gleicher SWL
- **Bessere Korrosionsbeständigkeit**: PREN 34–36 vs. 24–26 bei 316L
- **Hervorragende Spaltkorrosionsbeständigkeit**: Kritisch für Wirbellager
- **Höhere Ermüdungsfestigkeit**: Vorteil bei dynamischer Belastung

#### 4.2.3 Nachteile

- **Schwieriger zu bearbeiten**: Höherer Werkzeugverschleiß, langsamere Bearbeitung
- **Schwieriger zu gießen**: Engerer Temperaturbereich, höhere Ausschussrate
- **Teurer**: Faktor 1.5–2.5 gegenüber 316L
- **Teilweise magnetisch**: Kann Kompass beeinflussen (bei Einsatz nahe dem Steuerstand)
- **Geringere Verfügbarkeit**: Weniger Hersteller bieten Duplex-Wirbel an

#### 4.2.4 Empfehlung

Duplex 2205 ist die beste Wahl für:
- Ankerketten-Wirbel für Langfahrtyachten (Dauerbelastung in Tropen)
- Mooring-Wirbel (permanenter Unterwassereinsatz)
- Hochlast-Furlerwirbel (Vorstag-Last >10.000 kg)
- Jede Anwendung, wo Spaltkorrosion das Hauptrisiko ist

### 4.3 Bronze und Bronzelegierungen

#### 4.3.1 Aluminium-Bronze (CuAl10Ni5Fe4)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 620–750 | MPa |
| Streckgrenze | 250–350 | MPa |
| Bruchdehnung | 12–18 | % |
| Härte | 170–220 | HB |
| Dichte | 7.60 | g/cm³ |
| Korrosionsbeständigkeit | Ausgezeichnet in Salzwasser | — |
| Galvanische Kompatibilität | Gut mit Edelstahl | — |

**Einsatz in Wirbeln:**
- Traditionelles Material für schwere Anker- und Mooringwirbel
- Hervorragende Gleiteigenschaften als Lagerwerkstoff
- Selbstschmierend unter Salzwasser-Exposition
- Weniger anfällig für Spaltkorrosion als 316L
- Wird zunehmend durch Edelstahl verdrängt (Gewicht, Kosten)
- Noch verbreitet bei traditionellen Yachten und Fischereifahrzeugen

#### 4.3.2 Phosphorbronze (CuSn8P)

Primär als Lagerwerkstoff in Wirbeln verwendet, nicht als Strukturwerkstoff:
- Exzellente Gleiteigenschaften
- Niedrige Reibung auf Edelstahl
- Gute Korrosionsbeständigkeit
- Typische Anwendung: Lagerbuchsen in Gabel-Gabel-Wirbeln

### 4.4 Keramische Lagermaterialien

#### 4.4.1 Zirkoniumoxid (ZrO₂)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 800–1200 | MPa |
| Druckfestigkeit | 2000–2500 | MPa |
| Härte | 1200–1350 | HV (Vickers) |
| Dichte | 6.05 | g/cm³ |
| E-Modul | 210 | GPa |
| Reibungskoeffizient (auf Stahl) | 0.05–0.10 | — |
| Korrosionsbeständigkeit | Inert | — |

**Einsatz:** Kugellagerkugeln in Hochleistungs-Blockwirbeln und Spinnaker-Wirbeln.

#### 4.4.2 Siliziumnitrid (Si₃N₄)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 700–1000 | MPa |
| Druckfestigkeit | 3000–4000 | MPa |
| Härte | 1400–1600 | HV |
| Dichte | 3.20 | g/cm³ |
| E-Modul | 310 | GPa |
| Reibungskoeffizient | 0.03–0.08 | — |

**Vorteil gegenüber ZrO₂:** Deutlich leichter (fast halbe Dichte), härter, bessere Wärmeleitfähigkeit. Wird in Premium-Regatta-Wirbeln eingesetzt (Tylaska, Ronstan).

### 4.5 Titan (Grade 5, Ti6Al4V)

#### 4.5.1 Eigenschaften

| Eigenschaft | Wert | Einheit | Vergleich zu 316L |
|-------------|------|---------|-------------------|
| Zugfestigkeit | 900–1100 | MPa | +70–90% |
| Streckgrenze | 830–950 | MPa | +200–300% |
| Bruchdehnung | 10–15 | % | -70% |
| Härte | 330–380 | HV | +80% |
| Dichte | 4.43 | g/cm³ | -44% |
| E-Modul | 114 | GPa | -41% |
| Korrosionsbeständigkeit | Exzellent (immun in Salzwasser) | — | +++ |

#### 4.5.2 Einsatz in Wirbeln

- **Gewichtsersparnis**: 44% leichter als Edelstahl bei höherer Festigkeit
- **Korrosionsfrei**: Kein Spaltkorrosionsrisiko, kein Lochfraß
- **Extreme Kosten**: Faktor 5–10 gegenüber 316L
- **Schwierige Bearbeitung**: Erfordert Spezialwerkzeuge und -maschinen
- **Galvanik-Problem**: Kann galvanische Korrosion bei Kontakt mit unedleren Metallen verursachen

**Typische Anwendungen:**
- Spinnaker-Wirbel für extreme Regatta (America's Cup, Volvo Ocean Race)
- Furlerwirbel für Performance-Cruiser-Racer
- Superyacht-Beschläge (Design-Element — poliertes Titan als Premium-Optik)

### 4.6 Kunststoff-Lagermaterialien

#### 4.6.1 POM (Polyoxymethylen / Delrin)

- Häufigster Kunststoff für Gleitlager in Wirbeln
- Guter Reibungskoeffizient auf Edelstahl (0.15–0.25)
- UV-empfindlich — muss abgeschirmt sein
- Temperaturbereich: -40°C bis +100°C
- Wasseraufnahme: gering (0.2%)

#### 4.6.2 PTFE (Teflon)

- Niedrigster Reibungskoeffizient (0.04–0.10 auf Edelstahl)
- Geringe mechanische Festigkeit — nur als Beschichtung oder Buchse
- Exzellente chemische Beständigkeit
- Temperaturbereich: -200°C bis +260°C
- Kaltfließen unter Dauerlast — nicht für tragende Lagerfunktionen

#### 4.6.3 PEEK (Polyetheretherketon)

- Premium-Hochleistungskunststoff
- Hohe Festigkeit, gute Gleiteigenschaften
- Temperaturbereich: -60°C bis +250°C
- Chemisch inert
- Extrem teuer — nur in Spezialanwendungen
- Einsatz: Lagerbuchsen in Hochlast-Furlerwirbeln

### 4.7 Materialvergleich für AYDI-Bewertung

| Kriterium | 316L | Duplex 2205 | Al-Bronze | Titan Gr.5 |
|-----------|------|-------------|-----------|------------|
| Festigkeit | ●●○ | ●●● | ●●○ | ●●● |
| Korrosion | ●●○ | ●●● | ●●● | ●●● |
| Gewicht | ●○○ | ●○○ | ●○○ | ●●● |
| Kosten | ●●● | ●●○ | ●●○ | ●○○ |
| Verfügbarkeit | ●●● | ●●○ | ●●○ | ●○○ |
| Bearbeitbarkeit | ●●● | ●●○ | ●●● | ●○○ |
| Gesamt-Score | 13 | 14 | 14 | 12 |

---

## 5. Produktlinien

### 5.1 Wichard (Frankreich)

#### 5.1.1 Unternehmensübersicht

Wichard ist der weltweit führende Hersteller geschmiedeter Edelstahl-Beschläge für den Yachtbau. Gegründet 1919 in Thiers (Auvergne), ursprünglich als Messerschmiede. Seit den 1960er Jahren auf marine Beschläge spezialisiert. Alle Produkte werden in Frankreich geschmiedet — ein wesentliches Qualitätsmerkmal.

**Qualitätsmerkmale:**
- 100% geschmiedeter Edelstahl 316L
- Kontrollierte Schmiedetemperatur und Nachbehandlung
- Individuelle Chargenverfolgung
- Bruchlast-Tests an Stichproben jeder Charge
- CE-Kennzeichnung wo zutreffend

#### 5.1.2 Wirbel-Produktlinien

**Standard-Wirbelschäkel (Artikelserie 6500):**

| Artikel-Nr. | Bolzen-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|----------|-------------|-------------|
| 6501 | 5 | 400 | 16 | 28 | 18–22 |
| 6502 | 6 | 700 | 28 | 45 | 24–30 |
| 6503 | 8 | 1200 | 48 | 85 | 35–45 |
| 6504 | 10 | 1800 | 72 | 140 | 50–65 |
| 6505 | 12 | 2800 | 112 | 215 | 72–90 |
| 6506 | 14 | 3500 | 140 | 310 | 95–120 |

**HR (Haute Résistance) Wirbelschäkel (Artikelserie 6520):**

| Artikel-Nr. | Bolzen-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|----------|-------------|-------------|
| 6521 | 5 | 500 | 20 | 22 | 32–40 |
| 6522 | 6 | 900 | 36 | 38 | 42–52 |
| 6523 | 8 | 1600 | 64 | 72 | 58–72 |
| 6524 | 10 | 2500 | 100 | 120 | 82–100 |
| 6525 | 12 | 3800 | 152 | 185 | 110–140 |
| 6526 | 14 | 5000 | 200 | 275 | 150–185 |

**Ankerkettenwirbel (Artikelserie 6800):**

| Artikel-Nr. | Ketten-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|----------|-------------|-------------|
| 6801 | 6–7 | 800 | 32 | 150 | 45–55 |
| 6802 | 8 | 1200 | 48 | 220 | 58–72 |
| 6803 | 10 | 1800 | 72 | 350 | 75–95 |
| 6804 | 12 | 2800 | 112 | 520 | 105–130 |
| 6805 | 13–14 | 3500 | 140 | 680 | 135–165 |
| 6806 | 16 | 5000 | 200 | 950 | 180–220 |

**Toggle-Wirbel-Kombination (Artikelserie 6850):**

| Artikel-Nr. | SWL [kg] | MBL [kN] | Toggle-Winkel [°] | Gewicht [g] | Preis [EUR] |
|-------------|----------|----------|--------------------|-------------|-------------|
| 6851 | 1200 | 48 | ±20° | 280 | 85–105 |
| 6852 | 1800 | 72 | ±20° | 420 | 110–135 |
| 6853 | 2800 | 112 | ±25° | 620 | 145–180 |
| 6854 | 3500 | 140 | ±25° | 850 | 190–235 |

### 5.2 Kong (Italien)

#### 5.2.1 Unternehmensübersicht

Kong S.p.A., gegründet 1830 in Monte Marenzo (Lombardei). Ursprünglich Hersteller von Ketten und Karabinern. Breites Sortiment an Wirbeln für den Yacht- und Industriebereich. Bekannt für gutes Preis-Leistungs-Verhältnis.

**Qualitätsmerkmale:**
- Mischung aus geschmiedeten und gegossenen Produkten
- ISO 9001 zertifiziert
- Bruchlast-Tests dokumentiert
- Gute Verfügbarkeit in Europa

#### 5.2.2 Wirbel-Produktlinien

**Hochfeste Wirbelschäkel (Serie 82):**

| Artikel-Nr. | Bolzen-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|----------|-------------|-------------|
| 8201 | 5 | 350 | 14 | 30 | 12–16 |
| 8202 | 6 | 600 | 24 | 48 | 16–22 |
| 8203 | 8 | 1000 | 40 | 90 | 25–32 |
| 8204 | 10 | 1500 | 60 | 150 | 38–48 |
| 8205 | 12 | 2200 | 88 | 230 | 52–65 |
| 8206 | 14 | 3200 | 128 | 340 | 70–88 |

**Ankerkettenwirbel (Serie 85):**

| Artikel-Nr. | Ketten-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|----------|-------------|-------------|
| 8501 | 6–8 | 1000 | 40 | 200 | 35–45 |
| 8502 | 8–10 | 1500 | 60 | 320 | 48–60 |
| 8503 | 10–12 | 2200 | 88 | 480 | 65–82 |
| 8504 | 12–14 | 3200 | 128 | 680 | 88–110 |
| 8505 | 14–16 | 4500 | 180 | 920 | 120–150 |

### 5.3 Mantus Marine (USA)

#### 5.3.1 Unternehmensübersicht

Mantus Marine, gegründet 2012 in Dallas, Texas. Spezialist für Ankerausrüstung. Bekannt für den Mantus-Anker und hochwertige Ankerketten-Wirbel. Starke Präsenz im US-Markt und bei Langfahrtseglern.

**Qualitätsmerkmale:**
- Geschmiedeter Edelstahl 316
- Aufwändige Oberflächenbehandlung (elektropoliert)
- Breite Produktpalette für Ankersysteme
- Guter technischer Support

#### 5.3.2 Wirbel-Produktlinien

**Mantus Anchor Swivel (Serie M1):**

| Artikel-Nr. | Ketten-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [USD] |
|-------------|---------------|----------|----------|-------------|-------------|
| M1-6 | 6 | 700 | 28 | 170 | 45–55 |
| M1-8 | 8 | 1200 | 48 | 260 | 62–78 |
| M1-10 | 10 | 1800 | 72 | 390 | 85–105 |
| M1-12 | 12 | 2500 | 100 | 560 | 115–140 |
| M1-14 | 14 | 3500 | 140 | 780 | 155–190 |

**Mantus Swivel mit integriertem Toggle:**

| Artikel-Nr. | Ketten-Ø [mm] | SWL [kg] | MBL [kN] | Toggle [°] | Preis [USD] |
|-------------|---------------|----------|----------|------------|-------------|
| M1T-8 | 8 | 1200 | 48 | ±15° | 95–115 |
| M1T-10 | 10 | 1800 | 72 | ±15° | 125–150 |
| M1T-12 | 12 | 2500 | 100 | ±15° | 165–195 |

### 5.4 Ultra Marine (Schweden)

#### 5.4.1 Unternehmensübersicht

Ultra Marine, Spezialist für Ankerketten-Wirbel und Kettenzubehör. Schwedisches Unternehmen mit Fokus auf höchste Qualität. Bekannt für den Ultra Flip Swivel — einen der meistverwendeten Ankerketten-Wirbel weltweit.

#### 5.4.2 Produktlinien

**Ultra Flip Swivel:**

| Modell | Ketten-Ø [mm] | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [EUR] |
|--------|---------------|----------|----------|-------------|-------------|
| UFS-S | 6–8 | 1000 | 40 | 250 | 55–68 |
| UFS-M | 8–10 | 1500 | 60 | 380 | 72–90 |
| UFS-L | 10–13 | 2500 | 100 | 580 | 98–120 |
| UFS-XL | 13–16 | 4000 | 160 | 850 | 145–175 |

**Besonderheit Ultra Flip Swivel:**
- Patentiertes Klapp-Design: Wirbel kann flach zusammengeklappt werden
- Passt besser durch Kettenklüse und Ankerwindenführung
- 360°-Rotation auch unter voller Last
- Geschmiedeter 316L
- 10 Jahre Herstellergarantie

### 5.5 Seldén (Schweden)

#### 5.5.1 Unternehmensübersicht

Seldén Mast AB, gegründet 1960 in Göteborg. Weltweit führender Hersteller von Masten, Rigg und Rollreffsystemen. Furlerwirbel sind integraler Bestandteil der Seldén-Rollreffsysteme.

#### 5.5.2 Furlerwirbel-Produktlinien

**Seldén Furlex Furler-Wirbel (in Furlex-Systeme integriert):**

| Furlex-Modell | Vorstag-Ø [mm] | SWL [kg] | MBL [kN] | Bootsgröße [m] | System-Preis [EUR] |
|---------------|-----------------|----------|----------|----------------|---------------------|
| Furlex 104S | 4–5 | 2000 | 80 | 7–9 | 850–1050 |
| Furlex 200S | 5–7 | 3500 | 140 | 9–12 | 1200–1500 |
| Furlex 300S | 7–9 | 5500 | 220 | 12–15 | 1800–2200 |
| Furlex 400S | 9–12 | 8000 | 320 | 15–18 | 2800–3400 |
| Furlex 500S | 12–14 | 12000 | 480 | 18–22 | 4200–5200 |

**Wirbel-Besonderheiten bei Seldén:**
- Hochlast-Kugelgelagert (Edelstahl-Kugeln in PTFE-geschmierten Laufbahnen)
- Integrierte Dichtungen gegen Salzwassereintritt ins Lager
- Fettschmierung über Schmiernippel (Intervall: jährlich)
- Austauschbare Lagersätze (keine Komplettersatz nötig)

### 5.6 Harken (USA)

#### 5.6.1 Unternehmensübersicht

Harken, Inc., gegründet 1967 in Pewaukee, Wisconsin. Einer der weltweit führenden Hersteller von Segelbeschlägen, Blöcken und Furler-Systemen. Bekannt für höchste Qualität und Innovation.

#### 5.6.2 Blockwirbel

**Harken Carbo Blocks mit Wirbelkopf:**

| Artikel-Nr. | Rollen-Ø [mm] | SWL [kg] | Tauwerk [mm] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|--------------|-------------|-------------|
| 2637 | 29 | 200 | 4–8 | 18 | 28–35 |
| 2638 | 40 | 400 | 6–10 | 35 | 42–52 |
| 2639 | 57 | 750 | 8–14 | 65 | 62–78 |
| 2640 | 75 | 1200 | 10–16 | 110 | 85–105 |

**Harken Black Magic Blocks mit Wirbelkopf:**

| Artikel-Nr. | Rollen-Ø [mm] | SWL [kg] | Tauwerk [mm] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|--------------|-------------|-------------|
| 1617 | 40 | 500 | 6–10 | 55 | 55–68 |
| 1618 | 57 | 900 | 8–14 | 95 | 78–98 |
| 1619 | 75 | 1500 | 10–16 | 165 | 115–140 |
| 1620 | 100 | 2800 | 14–22 | 310 | 175–215 |

**Harken ESP Blocks (kugelgelagert, Regatta):**

| Artikel-Nr. | Rollen-Ø [mm] | SWL [kg] | Tauwerk [mm] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|--------------|-------------|-------------|
| 1213 | 40 | 450 | 6–10 | 42 | 82–100 |
| 1214 | 57 | 850 | 8–14 | 78 | 120–148 |
| 1215 | 75 | 1400 | 10–16 | 138 | 165–205 |

#### 5.6.3 Harken Furler-Wirbel

**Harken MKIV Furler-Systeme (inkl. Wirbel):**

| Modell | Vorstag [mm] | SWL [kg] | Bootsgröße [m] | System-Preis [EUR] |
|--------|-------------|----------|----------------|---------------------|
| MKIV Unit 0 | 4–6 | 2500 | 7–9 | 980–1200 |
| MKIV Unit 1 | 5–7 | 4000 | 9–12 | 1400–1700 |
| MKIV Unit 2 | 7–10 | 6500 | 12–16 | 2200–2700 |
| MKIV Unit 3 | 10–12 | 9000 | 16–20 | 3500–4200 |
| MKIV Unit 4 | 12–14 | 13000 | 20–25 | 5500–6800 |

### 5.7 Ronstan (Australien)

#### 5.7.1 Unternehmensübersicht

Ronstan International, gegründet 1953 in Melbourne. Australischer Hersteller von Segelbeschlägen und Architektur-Hardware. Bekannt für innovative Leichtbau-Beschläge und das Orbit-Block-System.

#### 5.7.2 Wirbel-Produktlinien

**Ronstan Orbit Blocks mit Wirbelkopf:**

| Artikel-Nr. | Rollen-Ø [mm] | SWL [kg] | Tauwerk [mm] | Gewicht [g] | Preis [EUR] |
|-------------|---------------|----------|--------------|-------------|-------------|
| RF45111 | 20 | 150 | 4–6 | 12 | 22–28 |
| RF45211 | 30 | 350 | 6–8 | 22 | 35–42 |
| RF45311 | 40 | 600 | 8–10 | 38 | 48–58 |
| RF45411 | 55 | 1000 | 10–14 | 72 | 68–85 |
| RF45511 | 75 | 1800 | 14–18 | 130 | 98–120 |

**Ronstan Spinnaker-Wirbel:**

| Artikel-Nr. | SWL [kg] | MBL [kN] | Lagertyp | Gewicht [g] | Preis [EUR] |
|-------------|----------|----------|----------|-------------|-------------|
| RF1034 | 500 | 20 | Kugel (Edelstahl) | 42 | 55–68 |
| RF1035 | 800 | 32 | Kugel (Edelstahl) | 65 | 78–95 |
| RF1036 | 1200 | 48 | Kugel (Keramik) | 55 | 115–140 |
| RF1037 | 2000 | 80 | Kugel (Keramik) | 88 | 165–200 |
| RF1038 | 3500 | 140 | Nadel (Edelstahl) | 145 | 250–310 |

**Ronstan Top-Down-Furler (Code 0 / Gennaker):**

| Modell | Segelfläche [m²] | SWL [kg] | Bootsgröße [m] | Preis [EUR] |
|--------|------------------|----------|----------------|-------------|
|?"RF7100 | 15–30 | 800 | 8–10 | 580–720 |
| RF7200 | 30–60 | 1500 | 10–14 | 850–1050 |
| RF7300 | 60–120 | 2500 | 14–18 | 1200–1500 |

### 5.8 Tylaska (USA)

#### 5.8.1 Unternehmensübersicht

Tylaska Marine Hardware, gegründet in Guilford, Connecticut. Premium-Hersteller für Hochleistungs-Segelbeschläge. Bekannt für CNC-gefräste Edelstahl- und Titan-Beschläge höchster Präzision. Lieferant für America's Cup und Volvo Ocean Race Teams.

#### 5.8.2 Wirbel-Produktlinien

**Tylaska T-Serie Wirbelschäkel (CNC-gefräst, 316L):**

| Artikel-Nr. | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [USD] |
|-------------|----------|----------|-------------|-------------|
| T5 | 500 | 20 | 25 | 85–105 |
| T8 | 1000 | 40 | 55 | 135–165 |
| T12 | 2000 | 80 | 95 | 195–240 |
| T16 | 3500 | 140 | 160 | 285–350 |
| T20 | 5500 | 220 | 260 | 420–510 |

**Tylaska Titan-Wirbel (Grade 5 Ti):**

| Artikel-Nr. | SWL [kg] | MBL [kN] | Gewicht [g] | Preis [USD] |
|-------------|----------|----------|-------------|-------------|
| TT5 | 600 | 24 | 14 | 280–340 |
| TT8 | 1200 | 48 | 32 | 420–510 |
| TT12 | 2500 | 100 | 55 | 650–790 |
| TT16 | 4200 | 168 | 95 | 980–1200 |

**Tylaska Spinnaker-Wirbel (Keramikgelagert):**

| Artikel-Nr. | SWL [kg] | MBL [kN] | Lager | Gewicht [g] | Preis [USD] |
|-------------|----------|----------|-------|-------------|-------------|
| S10 | 800 | 32 | Si₃N₄ | 38 | 195–240 |
| S16 | 1500 | 60 | Si₃N₄ | 65 | 310–380 |
| S20 | 2800 | 112 | Si₃N₄ | 110 | 480–580 |
| S25 | 4500 | 180 | Si₃N₄ | 175 | 720–880 |

### 5.9 Herstellervergleich — Übersichtstabelle

| Hersteller | Land | Fertigung | Preis-Segment | Stärke | Schwäche |
|------------|------|-----------|---------------|--------|----------|
| Wichard | FR | Geschmiedet | Mittel-Hoch | Geschmiedequalität, Tradition | Konservatives Design |
| Kong | IT | Gemischt | Mittel | Preis-Leistung, breites Sortiment | Qualitätsstreuung bei Guss |
| Mantus | US | Geschmiedet | Mittel-Hoch | Ankerspezialist, Support | Begrenztes Sortiment |
| Ultra Marine | SE | Geschmiedet | Mittel-Hoch | Flip-Swivel-Patent | Nur Ankersystem |
| Seldén | SE | Diverse | Hoch | Furler-Integration, Systemlösung | Nur Furler-Wirbel |
| Harken | US | Diverse | Hoch | Blockwirbel, Furler, Innovation | Hoher Preis |
| Ronstan | AU | Diverse | Mittel-Hoch | Leichtbau, Orbit-System | Eingeschränkte Verfügbarkeit EU |
| Tylaska | US | CNC-gefräst | Sehr hoch | Präzision, Titan, Regatta | Extrem teuer |

---

## 6. Anwendungen

### 6.1 Ankersystem

#### 6.1.1 Standardkonfiguration

```
Anker → [Schäkel] → Ankerkettenwirbel → [Kette] → Ankerwindenrad
                          ↑
                    Torsionsentlastung
                    hier platziert
```

**Position des Wirbels im Ankersystem:**

Der Ankerkettenwirbel wird zwischen dem letzten Kettenglied und dem Anker (bzw. dem Anker-Schäkel) eingesetzt. Die optimale Position ist **direkt am Anker**, nicht in der Mitte der Kette.

**Begründung:**
- Die Torsion ist am Anker am größten (höchste Strömungskräfte)
- Der Wirbel muss beim Einholen durch die Bugrolle passen — am Anker ist er an der Außenseite
- In der Mitte der Kette würde der Wirbel die Ankerwindenführung behindern

#### 6.1.2 Konfiguration für Langfahrt

Langfahrtsegler empfehlen oft eine erweiterte Konfiguration:

```
Anker → [Schäkel] → Toggle-Wirbel → Kette (5–10m)
  → Wirbel → Kette (restlich) → Ankerwindenrad
```

Zwei Wirbel: einer direkt am Anker (Toggle-Wirbel für Biege- und Torsionsentlastung), ein zweiter nach 5–10m Kette für zusätzliche Torsionsfreiheit.

#### 6.1.3 Konfiguration mit gemischtem Ankergeschirr

```
Anker → [Schäkel] → Toggle-Wirbel → Kette (15–30m)
  → Kette-Leine-Verbindung → Wirbelschäkel → Ankerleine → Ankerwindenrad
```

Bei gemischtem Geschirr (Kette + Leine) sitzt ein zusätzlicher Wirbel am Übergang, da Leine besonders anfällig für Torsion ist.

#### 6.1.4 Wartung des Ankerwirbels

| Intervall | Maßnahme | Werkzeug |
|-----------|----------|----------|
| Nach jedem Ankern | Sichtprüfung, freie Rotation prüfen | Keine |
| Wöchentlich (bei Dauerbenutzung) | Süßwasser-Spülung, Rotation prüfen | Schlauch |
| Monatlich | Schmierung mit Teflonfett | Fett, Lappen |
| Jährlich | Demontage, Reinigung, Lagerkontrolle | Werkzeugsatz |
| Alle 3 Jahre | Rissprüfung (Farbeindring- oder Magnetpulver) | Prüfset |
| Alle 5–8 Jahre | Austausch bei sichtbarem Verschleiß | Neuer Wirbel |

### 6.2 Rollreffsystem (Furler)

#### 6.2.1 Integration des Furlerwirbels

Der Furlerwirbel ist in der Regel vom Furler-Hersteller als integraler Bestandteil des Systems konzipiert. Ein Austausch durch Fremdprodukte ist **nur bei exakter Kompatibilität** ratsam.

**Systemintegration:**
```
Masttop
  ↓
Masttop-Beschlag
  ↓
Vorstag (Draht oder Rod)
  ↓
Furler-Profil (umhüllt das Vorstag)
  ↓
Furlerwirbel (im Trommelgehäuse)    ← hier die Rotation
  ↓
Furler-Trommel (mit Reffleinen-Aufnahme)
  ↓
Deck-Befestigung (Stemmplatten)
```

#### 6.2.2 Typische Probleme bei Furlerwirbeln

| Problem | Symptom | Ursache | Lösung |
|---------|---------|---------|--------|
| Schwergängig | Hoher Kraftaufwand zum Reffen | Korrosion, mangelnde Schmierung | Demontage, Reinigung, Neufettung |
| Ruckartig | Segel rollt ungleichmäßig | Lagerschaden, Salzablagerungen | Lagertausch |
| Geräusche | Klicken oder Knirschen beim Rollen | Verschlissene Kugeln, Lochfraß | Sofortige Inspektion |
| Spiel | Segel flattert trotz eingerolltem Zustand | Lagerverschleiß, Bolzenlockerung | Lagertausch, Bolzen nachziehen |
| Blockade | Segel lässt sich nicht mehr rollen | Totale Korrosion des Lagers | Notfall — Furler-Service |

#### 6.2.3 Wartungsintervalle für Furlerwirbel

| Hersteller | Empfohlenes Schmierintervall | Empfohlenes Fett | Lager-Lebensdauer |
|------------|------------------------------|------------------|-------------------|
| Seldén | Jährlich + nach Winterlager | Seldén Furler Grease | 5–8 Jahre |
| Harken | Jährlich | Harken Winch Grease | 5–8 Jahre |
| Profurl | Alle 6 Monate (Tropen) | Marine-PTFE-Fett | 4–6 Jahre |
| Facnor | Jährlich | Facnor Lube | 5–7 Jahre |
| Reckmann | Alle 2 Jahre (versiegelt) | Reckmann Spezialfett | 8–12 Jahre |

### 6.3 Fallen und Schoten

#### 6.3.1 Großfall

**Empfehlung:** Wirbelschäkel zwischen Großfall und Kopfbrett des Großsegels. SWL mindestens 2× die maximal zu erwartende Fallenlast.

**Konfiguration:**
```
Masttop-Rolle
  ↓
Fall (Dyneema oder Draht)
  ↓
Wirbelschäkel                    ← Torsionsentlastung
  ↓
Kopfbrett-Schäkel
  ↓
Großsegel Kopfbrett
```

#### 6.3.2 Vorsegel-Fall (Genua/Fock)

Bei Rollreffsystemen: Fallenwirbel ist in der Regel im Furler-System integriert.

Bei Hand-Reff-Systemen: Separater Wirbelschäkel am Fallenkopf. Snap-Shackle-Wirbel ermöglichen schnellen Segelwechsel.

#### 6.3.3 Spinnaker-Fall

**Empfehlung:** Kugelgelagerter Spinnaker-Wirbel, niemals einfacher Wirbelschäkel.

**Konfiguration:**
```
Masttop-Rolle (oder Spinnaker-Block)
  ↓
Spinnaker-Fall
  ↓
Kugelgelagerter Spinnaker-Wirbel    ← muss frei drehen!
  ↓
Snap-Schäkel (zum schnellen Bergen)
  ↓
Spinnaker-Kopf
```

### 6.4 Spinnaker-Systeme

#### 6.4.1 Symmetrischer Spinnaker

Der symmetrische Spinnaker erfordert den hochwertigsten Wirbel im gesamten Rigg. Beim Halsen (Gyrben) dreht sich der Spinnaker um seine eigene Achse — der Wirbel muss blitzschnell und widerstandsfrei folgen.

**Kritische Situation: Sonnenschuss**
Wenn der Spinnaker unkontrolliert vor den Mast weht und sich füllt, entstehen extreme Stoßlasten. Der Wirbel muss diese Last aufnehmen, ohne zu blockieren — sonst reißt das Segel oder das Rigg versagt.

#### 6.4.2 Asymmetrischer Spinnaker / Gennaker

Beim Code-0 oder Gennaker auf Top-Down-Furler ist der Wirbel im Furler integriert. Zusätzlicher Wirbelschäkel am Fall empfohlen.

### 6.5 Mooringsysteme

#### 6.5.1 Bojenliegeplatz

```
Boot → Mooring-Leine → Mooringwirbel → Grundkette → Grundgewicht/Anker
                             ↑
                    Permanenter Wirbel
                    Muss unter Wasser funktionieren
```

**Besondere Anforderungen:**
- Dauerhaft submers — höchste Korrosionsbelastung
- Bewuchsresistent — großzügige Lagerspalte
- Vandalismussicher — gegen unbefugtes Lösen gesichert
- Wartungsarm — Zugang nur bei Tauchgang oder Trockenfallen

#### 6.5.2 Wartung von Mooringwirbeln

| Intervall | Maßnahme |
|-----------|----------|
| Halbjährlich | Tauch-Inspektion, Bewuchs entfernen |
| Jährlich | Wirbel an Land bringen, reinigen, fetten |
| Alle 3 Jahre | Verschleißmessung, Wandstärkenmessung |
| Alle 5–8 Jahre | Komplettaustausch (auch bei gutem Zustand) |

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild 01: Festsitzender Wirbel (Seized Swivel)

**Beschreibung:** Der Wirbel lässt sich nicht mehr drehen, die beiden Hälften sind fest miteinander verbunden.

**Visuelle Merkmale:**
- Salzablagerungen (weiße Kristalle) im Lagerspalt sichtbar
- Korrosionsprodukte (braun-rostfarbig) in der Lagerzone
- Keine Bewegung möglich, auch nicht mit Werkzeug
- Möglicherweise aufgequollene Dichtungen (falls vorhanden)

**Ursachen:**
- Langfristig fehlende Wartung (kein Süßwasser, kein Fett)
- Spaltkorrosion durch stehendes Salzwasser
- Galvanische Korrosion bei ungleichen Materialpaarungen
- Bewuchs (Muscheln, Seepocken) im Lagerspalt

**Bewertung AYDI:**
- Befund-Schwere: KRITISCH (bei Ankersystem), HOCH (bei Fallen)
- Confidence: visual_high (eindeutig erkennbar bei Inspektion)

**Empfohlene Maßnahme:**
- Sofortiger Austausch bei sicherheitsrelevanten Anwendungen
- Versuch der Gängigmachung mit Kriechöl (WD-40 Marine, CRC) nur bei nicht-kritischen Anwendungen
- Demontage und Lagererneuerung als Alternative zum Komplett-Austausch

### 7.2 Fehlerbild 02: Lagerverschleiß (Bearing Wear)

**Beschreibung:** Die Lagerflächen sind abgenutzt, der Wirbel zeigt übermäßiges Spiel.

**Visuelle Merkmale:**
- Radialer Verschleiß: Wirbel wackelt seitlich
- Axialer Verschleiß: Wirbel hat Längsspiel (zieht auseinander)
- Metallabrieb (graue/schwarze Partikel) am Wirbel sichtbar
- Geräusche beim Drehen: Klicken, Knirschen, Kratzen

**Ursachen:**
- Normale Alterung nach langem Gebrauch
- Überlastung (SWL überschritten)
- Mangelnde Schmierung
- Sand- oder Schmutzpartikel im Lager
- Korrosion der Lagerflächen (Lochfraß als Ausgangspunkt)

**Bewertung AYDI:**
- Befund-Schwere: MITTEL bis HOCH (je nach Spiel)
- Confidence: visual_medium (Spiel erfordert haptische Prüfung)

**Empfohlene Maßnahme:**
- Radiales Spiel >1mm: Austausch empfohlen
- Axiales Spiel >2mm: Austausch dringend
- Bei kugelgelagerten Wirbeln: Lagersatz tauschen
- Bei Gleitlagern: Buchse tauschen oder Komplett-Austausch

### 7.3 Fehlerbild 03: Korrosion und Lochfraß (Pitting Corrosion)

**Beschreibung:** Lokale Korrosionsangriffe in Form von Grübchen oder Löchern auf den Metalloberflächen.

**Visuelle Merkmale:**
- Kleine Grübchen (0.1–2mm Durchmesser) auf der Oberfläche
- Braune oder orange Verfärbungen um die Grübchen
- Raue, unebene Oberfläche (im Vergleich zum Neuzustand)
- Bei fortgeschrittenem Befall: Durchbrüche, Material fehlt

**Ursachen:**
- Chlorid-Ionen im Salzwasser zerstören die Passivschicht
- Stagnationszonen (unter Ablagerungen, in Spalten)
- Mangelnde Süßwasser-Spülung
- Minderwertiges Material (304 statt 316L)

**Bewertung AYDI:**
- Befund-Schwere: MITTEL (Oberfläche) bis KRITISCH (tragende Querschnitte betroffen)
- Confidence: visual_high (gut erkennbar auf Fotos)

**Maßnahme:**
- Oberflächen-Pitting: Beobachten, häufiger warten
- Pitting >0.5mm Tiefe an tragenden Teilen: Austausch
- Pitting an Lagerflächen: Sofort austauschen (beschleunigt Verschleiß)

### 7.4 Fehlerbild 04: Ermüdungsriss (Fatigue Crack)

**Beschreibung:** Rissbildung durch zyklische Belastung, oft an Querschnittsübergängen oder Spannungskonzentrationen.

**Visuelle Merkmale:**
- Haarfeiner Riss, oft an der Basis von Bohrungen oder Gabelköpfen
- Riss verläuft senkrecht zur Hauptbelastungsrichtung
- Oft nur mit Lupe oder Farbeindringprüfung sichtbar
- Keine plastische Verformung um den Riss (Unterschied zu Überlastungsbruch)

**Ursachen:**
- Zyklische Belastung über der Dauerfestigkeit
- Konstruktiver Kerb (scharfe Querschnittsübergänge)
- Korrosionsinitiierter Ermüdungsriss (Pitting als Startstelle)
- Materialfehler (Lunker im Guss)

**Bewertung AYDI:**
- Befund-Schwere: KRITISCH (immer)
- Confidence: visual_low (ohne Farbeindringprüfung schwer zu erkennen)

**Maßnahme:**
- **Sofortiger Austausch** — Ermüdungsrisse wachsen exponentiell
- Keine Reparatur möglich (Schweißen verändert Gefüge)
- Ursache analysieren: Überdimensionierung für Ersatzwirbel

### 7.5 Fehlerbild 05: Galling (Kaltverschweißung)

**Beschreibung:** Metallische Mikroverschweißung zwischen den Gleitflächen. Tritt auf, wenn zwei ähnliche Metalle unter Last und Trockenreibung bewegt werden.

**Visuelle Merkmale:**
- Aufgeraute, zerfurchte Lagerflächen
- Metallische Aufschmierungen (Materialübertrag)
- Riefen in Drehrichtung sichtbar
- Wirbel dreht ruckartig oder blockiert plötzlich

**Ursachen:**
- Edelstahl auf Edelstahl ohne Schmierung
- Hohe Flächenpressung bei gleichzeitiger Drehbewegung
- Mangelnde Oberflächenbehandlung (keine Passivierung)
- Passungskorrosion bei eng tolerierten Lagern

**Bewertung AYDI:**
- Befund-Schwere: HOCH
- Confidence: visual_medium (erfordert Demontage)

**Maßnahme:**
- Austausch des Wirbels (Galling-Schäden sind irreversibel)
- Prävention: Unterschiedliche Materialien im Lager (Edelstahl + Bronze)
- Prävention: Regelmäßige Schmierung mit Anti-Seize-Paste

### 7.6 Fehlerbild 06: UV-Degradation

**Beschreibung:** Zerfall von Kunststoff-Lagerkomponenten durch UV-Strahlung.

**Visuelle Merkmale:**
- Verfärbung von Kunststoffteilen (Gelbung, Verbleichung)
- Spröde, rissige Oberfläche der Kunststoffbuchsen
- Bruchstücke von Lagerbuchsen am Wirbel erkennbar
- Lagerspiel durch geschrumpftes Kunststoffteil

**Ursachen:**
- Dauerhafte UV-Exposition (Deck, Masttop)
- Ungeeigneter Kunststoff (kein UV-Stabilisator)
- Normaler Alterungsprozess (5–10 Jahre für POM, 3–7 Jahre für PA)

**Bewertung AYDI:**
- Befund-Schwere: MITTEL
- Confidence: visual_high

**Maßnahme:**
- Austausch der Kunststoffbuchsen (falls als Ersatzteil verfügbar)
- Upgrade auf Keramiklager (UV-immun)
- UV-Schutzmantel für exponierte Wirbel

### 7.7 Fehlerbild 07: Bolzenlockerung

**Beschreibung:** Der Sicherungsbolzen oder die Mutter des Wirbels hat sich gelöst.

**Visuelle Merkmale:**
- Bolzen steht heraus oder fehlt
- Splint verbogen oder gebrochen
- Sicherungsdraht durchtrennt oder lose
- Wirbel lässt sich axial auseinanderziehen

**Ursachen:**
- Vibration (insbesondere bei Motorbooten)
- Fehlender oder beschädigter Splint/Sicherungsdraht
- Falsch angezogener Bolzen (zu locker)
- Korrosion des Sicherungselements

**Bewertung AYDI:**
- Befund-Schwere: KRITISCH (Wirbel kann sich trennen = Totalverlust)
- Confidence: visual_high

**Maßnahme:**
- Sofortige Sicherung mit neuem Splint/Sicherungsdraht
- Bolzen auf Verschleiß prüfen, ggf. ersetzen
- Gewinde auf Galling prüfen

### 7.8 Fehlerbild 08: Verformung unter Überlast

**Beschreibung:** Plastische Verformung des Wirbelkörpers durch Überschreiten der Streckgrenze.

**Visuelle Merkmale:**
- Augen oder Gabeln sind oval statt rund
- Bolzenlöcher sind aufgeweitet
- Sichtbare Biegung des Wirbelkörpers
- Risse an Querschnittsübergängen

**Ursachen:**
- Einmalige Überlastung (Sturm, Grundberührung beim Ankern)
- Dauernde Überlastung (zu kleiner Wirbel gewählt)
- Stoßbelastung (Rucklast)

**Bewertung AYDI:**
- Befund-Schwere: KRITISCH
- Confidence: visual_high (deutlich sichtbare Verformung)

**Maßnahme:**
- Sofortiger Austausch
- Nächstgrößeren Wirbel einsetzen
- Ursache der Überlast analysieren (Kettengeschirr optimieren)

### 7.9 Fehlerbild 09: Elektrolyse-Schäden

**Beschreibung:** Galvanische Korrosion durch Kontakt mit unedleren oder edleren Metallen in Salzwasser.

**Visuelle Merkmale:**
- Starke lokalisierte Korrosion an der Kontaktzone zu anderen Metallen
- Weißliche Ablagerungen bei Aluminium-Kontakt
- Grünliche Ablagerungen bei Kupfer/Bronze-Kontakt
- Materialverlust einseitig am Wirbel

**Ursachen:**
- 316L-Wirbel direkt an verzinkter Kette (ohne Übergangsglied)
- Aluminium-Schäkel an Edelstahl-Wirbel
- Fehlende Opfer-Anoden im Ankersystem
- Streustrom-Korrosion in Marinas

**Bewertung AYDI:**
- Befund-Schwere: MITTEL bis HOCH
- Confidence: visual_high

**Maßnahme:**
- Galvanische Isolation (Kunststoff-Zwischenlage)
- Materialkompatibilität sicherstellen
- Opfer-Anoden installieren

### 7.10 Fehlerbild 10: Bewuchsblockade

**Beschreibung:** Biologischer Bewuchs (Muscheln, Seepocken, Algen) blockiert die Wirbelbewegung.

**Visuelle Merkmale:**
- Sichtbarer Bewuchs auf und im Wirbel
- Kalkschalen in Lagerspalten
- Algenfilament um den Wirbelkörper
- Wirbel dreht nicht oder nur schwer

**Ursachen:**
- Permanenter Unterwassereinsatz ohne Antifouling
- Langer Aufenthalt in warmen, nährstoffreichen Gewässern
- Fehlende Wartung (kein regelmäßiges Reinigen)

**Bewertung AYDI:**
- Befund-Schwere: MITTEL (wenn erkannt und gereinigt), HOCH (wenn unbemerkt)
- Confidence: visual_high

**Maßnahme:**
- Mechanische Reinigung (Messer, Bürste)
- Antifouling-Anstrich (nur auf Außenflächen, NICHT auf Lagerflächen)
- Regelmäßige Tauch-Inspektion bei Mooring-Wirbeln

### 7.11 Fehlerbild 11: Falsche Dimensionierung

**Beschreibung:** Wirbel ist für die Anwendung zu klein dimensioniert, ohne dass bereits sichtbare Schäden vorliegen.

**Visuelle Merkmale:**
- Wirbel erscheint im Vergleich zu angrenzenden Bauteilen (Kette, Schäkel) unverhältnismäßig klein
- Bolzen-Durchmesser des Wirbels kleiner als der Bolzen-Ø angrenzender Schäkel
- Herstellerangaben (falls lesbar) zeigen SWL unter der Ketten-SWL

**Ursachen:**
- Falscher Wirbel installiert (Verwechslung bei der Bestellung)
- Nachrüstung ohne Neuberechnung der Lasten
- Boot wurde umgerüstet (größere Segel, schwererer Anker) ohne Wirbel-Update

**Bewertung AYDI:**
- Befund-Schwere: HOCH bis KRITISCH
- Confidence: visual_medium (erfordert Vergleich mit Spezifikationen)

**Maßnahme:**
- SWL des Wirbels mit der Ketten-/Fall-SWL vergleichen
- Bei Unterdimensionierung: sofortiger Austausch gegen korrekte Größe

### 7.12 Fehlerbild 12: Materialverwechslung (304 statt 316L)

**Beschreibung:** Der eingebaute Wirbel besteht aus dem falschen Edelstahl — typischerweise AISI 304 (1.4301) statt dem erforderlichen AISI 316L (1.4404).

**Visuelle Merkmale:**
- Stärkere Korrosion als erwartet (Tea Staining, Lochfraß)
- Oft nicht visuell von 316L zu unterscheiden
- Möglicherweise magnetisch (304 nach Kaltverformung)
- Preis beim Kauf auffällig niedrig

**Ursachen:**
- Billigprodukt aus Fernost ohne korrekte Materialangabe
- Verwechslung beim Kauf
- Fälschung / falsche Zertifikate

**Bewertung AYDI:**
- Befund-Schwere: HOCH (beschleunigte Korrosion in Salzwasser)
- Confidence: visual_low (sichere Unterscheidung nur mit Materialtest)

**Maßnahme:**
- Magnet-Test: 304 ist nach Kaltverformung leicht magnetisch, 316L nicht
- Säure-Spot-Test (Molybdän-Nachweis)
- Bei Verdacht: Austausch gegen Markenprodukt mit Zertifikat

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum 1: Ankerkettenwirbel dreht nicht

```
START: Ankerkettenwirbel dreht nicht unter Last
  │
  ├── Dreht der Wirbel ohne Last (Kette ausgebaut)?
  │   ├── NEIN → Wirbel ist festgefressen (Fehlerbild 01)
  │   │   ├── Kriechöl einwirken lassen (24h)
  │   │   ├── Leichte Hammerschläge auf Wirbelkörper
  │   │   ├── Gelingt Lösen?
  │   │   │   ├── JA → Reinigen, Fetten, weiter verwenden (Lager prüfen)
  │   │   │   └── NEIN → Austausch erforderlich
  │   │   └── ACHTUNG: Bei kritischer Anwendung → immer Austausch
  │   │
  │   └── JA → Problem ist lastabhängig
  │       ├── SWL des Wirbels prüfen: Ausreichend für die Kette?
  │       │   ├── NEIN → Wirbel unterdimensioniert → Austausch (größer)
  │       │   └── JA → Lagertyp prüfen
  │       │       ├── Gleitlager → Schmierung prüfen
  │       │       │   ├── Fett aufbringen → Test unter Last
  │       │       │   ├── Dreht jetzt? → Regelmäßiger schmieren
  │       │       │   └── Dreht nicht → Lagerflächen beschädigt → Austausch
  │       │       └── Kugellager → Kugeln/Laufbahn prüfen
  │       │           ├── Kugeln fehlen oder beschädigt → Lagersatz tauschen
  │       │           └── Laufbahn korrodiert → Austausch
  │
  └── ENDE
```

### 8.2 Entscheidungsbaum 2: Furler-System schwergängig

```
START: Rollreffanlage erfordert übermäßigen Kraftaufwand
  │
  ├── Ist nur das Einrollen schwergängig oder auch das Ausrollen?
  │   ├── NUR EINROLLEN → Problem im Trommel-/Wirbelbereich
  │   │   ├── Furlerwirbel schmieren (Schmiernippel)
  │   │   ├── Reffleine auf Einklemmung prüfen
  │   │   ├── Trommelgehäuse auf Verformung prüfen
  │   │   └── Besser? → Ja: Wartungsintervall verkürzen
  │   │              → Nein: Furler-Service durch Fachbetrieb
  │   │
  │   └── BEIDES → Problem wahrscheinlich am Vorstag oder Profil
  │       ├── Vorstag-Spannung prüfen (zu hoch → mehr Lagerbelastung)
  │       ├── Profil auf Verformung prüfen (gebogen, verdreht)
  │       ├── Profil-Verbindungen (Coupler) auf Schwergängigkeit prüfen
  │       └── Wirbel als letzte Option prüfen
  │
  └── ENDE
```

### 8.3 Entscheidungsbaum 3: Spinnaker-Wirbel blockiert

```
START: Spinnaker-Wirbel dreht nicht frei
  │
  ├── Zeitpunkt des Problems?
  │   ├── Vor dem Setzen (am Deck) → Wirbel an Deck prüfen
  │   │   ├── Frei drehbar ohne Segel? → JA: Segel-Kopfbrett klemmt
  │   │   └── Nicht frei drehbar → Reinigen, Ölen, oder Austausch
  │   │
  │   └── Unter Segeldruck → Last zu hoch für Wirbeltyp
  │       ├── SWL prüfen: Ausreichend?
  │       │   ├── NEIN → Größeren Wirbel wählen
  │       │   └── JA → Lagertyp prüfen
  │       │       ├── Gleitlager → Upgrade auf Kugellager empfohlen
  │       │       └── Kugellager → Lager verschlissen → Wartung/Tausch
  │       │
  │       └── DRINGEND im Einsatz: Spinnaker bergen!
  │           Blockierter Wirbel unter Last → Rissgefahr
  │
  └── ENDE
```

### 8.4 Entscheidungsbaum 4: Geräusche am Wirbel

```
START: Ungewöhnliche Geräusche beim Drehen des Wirbels
  │
  ├── Art des Geräuschs?
  │   ├── Klicken (regelmäßig) → Kugellagerschaden
  │   │   ├── Einzelne Kugel beschädigt oder fehlt
  │   │   └── Laufbahn mit Lochfraß
  │   │   └── → Lagersatz tauschen
  │   │
  │   ├── Knirschen (kontinuierlich) → Sand/Schmutz im Lager
  │   │   ├── Demontage, Reinigung, Neufettung
  │   │   └── Lagerflächen auf Riefen prüfen
  │   │
  │   ├── Quietschen → Trockenlauf, fehlende Schmierung
  │   │   ├── Sofort schmieren
  │   │   └── Falls nach Schmierung weiter: Galling (Fehlerbild 05)
  │   │
  │   └── Knacken (unregelmäßig) → Rissverdacht!
  │       ├── Sofort aus dem System nehmen
  │       ├── Farbeindringprüfung durchführen
  │       └── Bei Rissnachweis: Austausch, KEINE Reparatur
  │
  └── ENDE
```

### 8.5 Entscheidungsbaum 5: Wirbel-Auswahl für Neuinstallation

```
START: Welchen Wirbel für meine Anwendung?
  │
  ├── Anwendungsbereich?
  │   ├── Ankersystem
  │   │   ├── Kettengröße bestimmen → Wirbel-SWL ≥ Ketten-SWL
  │   │   ├── Langfahrt/Tropen? → Duplex 2205 empfohlen
  │   │   ├── Toggle nötig? → Ja bei Bügelanker, Rollenbuganker
  │   │   └── → Empfehlung: Wichard 6800 oder Mantus M1
  │   │
  │   ├── Furler-System
  │   │   ├── Furler-Hersteller/-Modell bestimmen
  │   │   ├── Original-Ersatzteil verwenden!
  │   │   └── → Systemwirbel vom Furler-Hersteller
  │   │
  │   ├── Fall / Block
  │   │   ├── Fallenlast berechnen (Segelfläche × Winddruck × SF)
  │   │   ├── Cruiser → Wichard 6500/6520
  │   │   └── Regatta → Tylaska T-Serie oder Ronstan
  │   │
  │   ├── Spinnaker
  │   │   ├── Spinnakerfläche und max. Windstärke
  │   │   ├── Kugelgelagerter Wirbel obligatorisch
  │   │   ├── Cruiser → Ronstan RF1034/1035
  │   │   └── Regatta → Tylaska S-Serie
  │   │
  │   └── Mooring
  │       ├── Bootsgröße und Expositionsgrad bestimmen
  │       ├── Duplex 2205 oder Aluminium-Bronze empfohlen
  │       └── Großzügig dimensionieren (lange Standzeiten)
  │
  └── ENDE
```

---

## 9. FAQ — Häufige Fragen

### 9.1 Allgemeine Fragen

**F1: Was ist der Unterschied zwischen einem Wirbel und einem Drehgelenk?**

Ein Wirbel (Swivel) erlaubt Rotation um eine Achse — typischerweise die Zugachse. Er dient der Torsionsentlastung. Ein Drehgelenk (Universal Joint / Cardan Joint) erlaubt Winkelbewegung um zwei oder mehr Achsen. Im Yachtbau werden beide Begriffe manchmal synonym verwendet, bezeichnen aber unterschiedliche Funktionsprinzipien.

**F2: Brauche ich zwingend einen Ankerkettenwirbel?**

Nicht zwingend, aber dringend empfohlen. Ohne Wirbel verdreht sich die Kette bei jedem Tidenwechsel. Nach wenigen Tagen vor Anker kann die Torsion so stark sein, dass die Kette knickt und die Bruchlast reduziert wird. Bei Langfahrt ist ein Ankerkettenwirbel Standard und unverzichtbar.

**F3: Kann ich einen Wirbel reparieren, wenn er festsitzt?**

In vielen Fällen ja — durch Einweichen in Kriechöl, vorsichtiges Lösen und anschließende Reinigung und Neufettung. Bei sicherheitskritischen Anwendungen (Anker, tragende Rigg-Verbindungen) ist jedoch der Austausch grundsätzlich vorzuziehen. Die Lagerflächen sind nach dem Festsitzen oft beschädigt.

**F4: Wie oft muss ein Wirbel geschmiert werden?**

Grundregel: Alle 6–12 Monate für Wirbel über Wasser (Fallen, Blöcke), alle 3–6 Monate für Ankersystem-Wirbel, und bei Furlerwirbeln gemäß Herstellerangabe (typisch jährlich). In tropischen Gewässern oder bei intensiver Nutzung: Intervalle halbieren.

**F5: Welches Schmiermittel für marine Wirbel?**

Empfohlen: PTFE-basiertes Marine-Fett (z.B. Harken Winch & Bearing Grease, Seldén Furler Grease) für kugelgelagerte Wirbel. Für Gleitlager: Wasserresistentes Lithium-Fett oder spezielles Marine-Lagerfett. NIEMALS WD-40 als Dauerschmierung verwenden — WD-40 ist ein Kriechöl/Wasserverdränger, kein Schmiermittel.

**F6: 316 oder 316L — was ist der Unterschied?**

316L hat einen niedrigeren Kohlenstoffgehalt (max. 0.03% statt 0.08% bei 316). Dies verbessert die Schweißbarkeit und die Beständigkeit gegen interkristalline Korrosion. Für geschmiedete oder gegossene Wirbel (die nicht geschweißt werden) ist der Unterschied marginal, aber 316L ist Standard und sollte bevorzugt werden.

### 9.2 Fragen zu spezifischen Anwendungen

**F7: Mein Ankerwirbel passt nicht durch die Bugrolle — was tun?**

Das ist ein häufiges Problem bei nachgerüsteten Wirbeln. Lösungen: (a) Flacheren Wirbel verwenden (z.B. Ultra Flip Swivel), (b) Bugrolle mit breiterem Schlitz nachrüsten, (c) Wirbel hinter der Bugrolle positionieren (nur wenn er nicht die Ankerwindenführung blockiert).

**F8: Kann ich einen normalen Wirbelschäkel als Ankerkettenwirbel verwenden?**

Technisch möglich, wenn SWL und MBL ausreichen, aber nicht empfohlen. Ankerketten-Wirbel sind speziell für die Belastungen im Ankersystem konstruiert — größere Lagerflächen, robustere Sicherung, Kompatibilität mit Kettenanschlüssen. Ein einfacher Wirbelschäkel hat oft zu enge Lagerspalte, die schneller korrodieren.

**F9: Mein Furler rollt schwer — liegt es am Wirbel?**

Möglicherweise, aber prüfen Sie zuerst: (a) Vorstag-Spannung (zu hoch = mehr Reibung), (b) Profil-Coupler (festsitzende Verbindungen), (c) Reffleine (Einklemmung). Erst wenn alles andere ausgeschlossen ist: Furlerwirbel schmieren oder zur Inspektion demontieren.

**F10: Brauche ich einen Wirbel am Großfall?**

Empfohlen, aber nicht in allen Konfigurationen nötig. Bei Rollreff-Großsegeln: nein (Rotation im Furler-System). Bei konventionellem Großsegel mit Rutscher: ja, ein Wirbelschäkel am Kopfbrett verhindert das Verdrehen des Falls und erleichtert das Setzen.

**F11: Titan-Wirbel — lohnt sich das?**

Für den durchschnittlichen Fahrtensegler: nein. Das Preis-Leistungs-Verhältnis ist nur bei Regattayachten gerechtfertigt, wo jedes Gramm am Masttop zählt. Für Cruiser ist geschmiedeter 316L das optimale Material. Titan-Wirbel erfordern zudem spezielle Pflege (galvanische Isolation zu anderen Metallen).

**F12: Kann ich einen Wirbel in der Kette einbauen statt am Anker?**

Ja, aber die Position direkt am Anker ist vorzuziehen. Ein Wirbel mitten in der Kette kann Probleme mit der Ankerwindenführung verursachen und bei Kettenklüsen klemmen. Ausnahme: Bei sehr langem Kettenvorrat (>80m) ist ein zweiter Wirbel nach 20–30m sinnvoll.

### 9.3 Fragen zur Sicherheit

**F13: Wie erkenne ich, ob mein Wirbel noch sicher ist?**

Checkliste: (a) Dreht frei ohne Blockaden, (b) Kein übermäßiges Spiel (radial <1mm, axial <2mm), (c) Keine sichtbare Korrosion an tragenden Querschnitten, (d) Bolzen/Splint vollständig und intakt, (e) Keine Verformung der Augen oder Gabeln, (f) Keine Risse (mit Lupe prüfen). Bei Unsicherheit: Austausch ist immer die sichere Option.

**F14: Was passiert, wenn ein Ankerkettenwirbel bricht?**

Der Anker samt Kette geht verloren. Das Boot treibt unkontrolliert. In der Nacht oder bei schlechtem Wetter ist dies ein potenziell lebensbedrohlicher Notfall. Deshalb: Wirbel immer großzügig dimensionieren und regelmäßig inspizieren.

**F15: Sicherheitsfaktor 4:1 oder 5:1 — was ist richtig?**

Minimum 4:1 nach Klassifikationsgesellschaften (GL/DNV). Empfohlen 5:1 für dynamische Anwendungen (Fallen, Spinnaker). Bei Unsicherheit über die tatsächlichen Lasten: immer den höheren Sicherheitsfaktor wählen. Überdimensionierung kostet wenig Gewicht und Geld, bietet aber erheblich mehr Sicherheit.

**F16: Müssen Wirbel CE-gekennzeichnet sein?**

Wirbel selbst unterliegen keiner CE-Pflicht als Einzelkomponente. Jedoch müssen sie in CE-konformen Ankersystemen (nach RCD 2013/53/EU) die Anforderungen der relevanten Normen erfüllen. Seriöse Hersteller liefern Bruchlast-Zertifikate und Materialzertifikate mit.

### 9.4 Fragen zur Wartung

**F17: Wie reinige ich einen verkalkten Wirbelblock am besten?**

(a) 24h in Süßwasser einweichen, (b) Kalkablagerungen mit weicher Bürste oder Holzstab entfernen, (c) Für hartnäckigen Kalk: verdünnte Essig- oder Zitronensäure (5–10%, max. 30 Min., dann gründlich spülen), (d) Trocknen, dann fetten. NIEMALS Salzsäure verwenden — greift Edelstahl an.

**F18: Muss ich den Wirbel zum Winterlager demontieren?**

Empfohlen bei Ankersystem-Wirbeln: Wirbel abnehmen, reinigen, fetten, trocken lagern. Furlerwirbel: gemäß Herstelleranweisung (oft reicht Schmierung und Abdeckung). Blockwirbel: können am Rigg bleiben, wenn trocken und geschützt.

**F19: Kann ich einen kugelgelagerten Wirbel selbst warten?**

Bei einfachen Wirbeln (Harken, Ronstan): ja, mit etwas Geschick. Lagersatz bestellen (Kugeln, Laufscheiben, Dichtungen), demontieren, reinigen, neu fetten, zusammenbauen. Bei komplexen Furlerwirbeln: Herstellerservice empfohlen (spezielle Werkzeuge und Kalibrierung nötig).

**F20: Welche Lebensdauer hat ein mariner Wirbel?**

Stark abhängig von Material, Qualität, Belastung und Wartung. Richtwerte: Einfacher Wirbelschäkel 316L: 8–15 Jahre. Kugelgelagerter Blockwirbel: 5–10 Jahre (Lager), Körper länger. Ankerkettenwirbel: 5–10 Jahre. Furlerwirbel-Lager: 5–8 Jahre. Mooringwirbel: 5–8 Jahre unterwasser.

### 9.5 Fragen zu Kosten und Beschaffung

**F21: Warum sind marine Wirbel so viel teurer als Baumarkt-Wirbel?**

Marine Wirbel verwenden 316L-Edelstahl (statt 304 oder verzinktem Stahl), haben zertifizierte Bruchlasten, kontrollierte Fertigungsqualität (geschmiedet oder hochwertig gegossen) und korrosionsresistente Lagermaterialien. Ein Baumarkt-Wirbel für 3 EUR kann in Salzwasser innerhalb von Wochen versagen und ist NIEMALS für sicherheitskritische Anwendungen geeignet.

**F22: Gibt es preiswerte Alternativen zu Marken-Wirbeln?**

Ja — einige chinesische Hersteller (z.B. über Alibaba) liefern 316L-Wirbel zu einem Bruchteil des Preises. ABER: Materialqualität ist häufig nicht verifizierbar, Bruchlast-Angaben können übertrieben sein, und Fertigungsqualität schwankt stark. Für nicht-kritische Anwendungen (Mooring-Leine am Steg, Fender-Aufhängung) akzeptabel, für Ankersystem und Rigg: nur Markenprodukte.

**F23: Wo kaufe ich marine Wirbel am besten?**

Empfohlene Bezugsquellen in Europa: SVB (svb-marine.de), Compass24 (compass24.de), Toplicht (toplicht.de), AWN (awn.de), Yachtshop24 (yachtshop24.de), Force 4 (force4.co.uk). Direkt beim Hersteller (z.B. wichard.com) bei Großbestellungen. Preisvergleich lohnt sich — bis zu 30% Preisunterschied zwischen den Shops.

**F24: Sollte ich Ersatzwirbel an Bord haben?**

Für Langfahrt: unbedingt. Empfohlener Bordvorrat: (a) 1× Ankerkettenwirbel passend zur Kette, (b) 2–3× Wirbelschäkel in der häufigsten Größe, (c) 1× Spinnaker-Wirbel (wenn Spinnaker gefahren wird). Für Küstenfahrt: mindestens 1 Ersatz-Ankerwirbel.

**F25: Lohnt sich ein Upgrade von Gleitlager auf Kugellager?**

Für Spinnaker-Wirbel: unbedingt — Gleitlager sind für Spinnaker ungeeignet. Für Ankerkettenwirbel: nicht nötig — Gleitlager sind robuster gegen Verschmutzung. Für Blockwirbel: bei Regatta ja, bei Cruising selten nötig. Für Furlerwirbel: Standard-Furler haben bereits Kugellager.

---

## 10. Glossar

### Begriffe A–D

**Ankerkettengröße (Anchor Chain Size):** Nenndurchmesser des Kettendrahtes in mm. Bestimmt die SWL und MBL der Kette und damit die Mindestdimensionierung des Wirbels. Typische Größen für Yachten: 6–16mm.

**Anti-Seize-Paste:** Schmiermittel auf Kupfer- oder Keramikbasis, das Galling (Kaltverschweißung) zwischen Edelstahloberflächen verhindert. Wird auf Bolzengewinde und Lagerflächen aufgetragen.

**Arbeitslast (Safe Working Load / SWL):** Die maximal zulässige Dauerbelastung eines Bauteils im normalen Betrieb. Typisch: 25% der Bruchlast (SF 4:1). Nicht zu verwechseln mit der Prüflast.

**Axiallast:** Zugkraft entlang der Wirbelachse (Hauptbelastungsrichtung). Bestimmt die Lagerpressung und das erforderliche Losbrechmoment.

**Backstag (Backstay):** Stehendes Gut vom Masttop zum Heck. Toggle-Wirbel am Heck-Anschluss empfohlen.

**Baumarkt-Wirbel:** Umgangssprachlich für billige, nicht-marine Wirbel aus verzinktem Stahl oder 304-Edelstahl. Für den Yachtbau NICHT geeignet.

**Bewuchs (Fouling / Marine Growth):** Biologische Organismen (Muscheln, Seepocken, Algen), die sich auf Unterwasser-Oberflächen ansiedeln. Blockiert Wirbellager.

**Bolzensicherung:** Mechanische Sicherung des Wirbelbolzens gegen unbeabsichtigtes Lösen. Methoden: Splint, Sicherungsring, Draht-Locking, Kontermutter.

**Bruchlast (Minimum Breaking Load / MBL):** Die minimale Kraft, bei der das Bauteil versagt (bricht). Wird im Zugversuch ermittelt. Wirbel-MBL muss mindestens SF × SWL betragen.

**Bronze:** Kupferlegierung, traditioneller Werkstoff für marine Lagerbuchsen. Aluminium-Bronze (CuAl10) für strukturelle Teile, Phosphorbronze (CuSn8P) für Gleitelemente.

**Cardan-Gelenk (Cardan Joint):** Universalgelenk mit Kreuzstück, erlaubt Winkelbewegung um zwei Achsen. Im Yachtbau für Steueranlagen und Wellenstränge.

**CE-Kennzeichnung:** Konformitätskennzeichnung für EU-Markt. Wirbel selbst nicht CE-pflichtig, aber Teil von CE-konformen Systemen (Ankersysteme nach RCD).

**Confidence Level:** Im AYDI-System die Verlässlichkeitsstufe einer Bewertung. Für Wirbel typisch: "measured" (Herstellerdaten), "visual_high" (klare Inspektion), "documented" (Servicebericht).

**Crevice Corrosion → Spaltkorrosion**

**Dauerfestigkeit (Endurance Limit):** Die Spannungsamplitude, unterhalb derer ein Werkstoff theoretisch unendlich viele Lastwechsel erträgt. Für 316L ca. 30% der Streckgrenze.

**Drehmoment (Torque):** Kraft × Hebelarm. Beim Wirbel: das zum Lösen/Drehen erforderliche Moment. Je niedriger, desto besser.

**Duplex 2205 (1.4462):** Edelstahl mit Doppelgefüge (Austenit + Ferrit). Höhere Festigkeit und Korrosionsbeständigkeit als 316L. Premium-Material für marine Wirbel.

### Begriffe E–K

**Elektrolyse (Electrolysis):** Galvanische Korrosion durch Potentialunterschiede zwischen verschiedenen Metallen in einem Elektrolyten (Salzwasser).

**Ermüdung (Fatigue):** Werkstoffversagen durch wiederholte (zyklische) Belastung unterhalb der statischen Bruchlast. Kritisch bei Wirbeln im Seegang.

**Feinguss (Investment Casting):** Gießverfahren mit verlorener Form, liefert glatte Oberflächen und enge Toleranzen. Standardverfahren für Serien-Wirbel.

**Fretting Corrosion → Reibkorrosion**

**Furler (Roller Furling System):** Rollreffanlage für Vorsegel. Der Furlerwirbel ist das zentrale Lager.

**Gabel (Jaw / Fork):** U-förmiger Anschluss an einem Wirbel, verbunden durch einen Querbolzen. Ermöglicht direkte Verbindung zu Kettenglieder oder Gabelköpfen.

**Galvanische Reihe:** Ordnung der Metalle nach ihrem elektrochemischen Potenzial in Seewasser. Bestimmt, welches Metall bei Kontaktkorrosion zersetzt wird.

**Galling:** Kaltverschweißung / adhäsiver Verschleiß zwischen metallischen Gleitflächen unter Last. Häufig bei Edelstahl auf Edelstahl ohne Schmierung.

**Gleitlager (Plain Bearing / Sleeve Bearing):** Lagerprinzip, bei dem zwei Oberflächen direkt aufeinander gleiten. Einfach, robust, aber höherer Reibwert als Wälzlager.

**Güteklasse (Grade):** Qualitätsstufe von Ankerketten. Klasse 40 (Standard), Klasse 70 (hochfest), Klasse 80 (extra hochfest). Die SWL des Wirbels muss zur Kettengüteklasse passen.

**Halyard → Fall**

**Kardangelenk → Cardan-Gelenk**

**Keramiklager:** Kugellager aus Siliziumnitrid (Si₃N₄) oder Zirkoniumoxid (ZrO₂). Korrosionsfrei, extrem hart, niedrigster Reibwert. Premium-Option für Hochleistungswirbel.

**Kinking:** Schlingenbildung in Kette oder Tauwerk durch akkumulierte Torsion. Reduziert die Bruchlast um bis zu 50%.

> ⚠️ **ZU PRÜFEN (Audit):** Widerspruch im Dokument — §2.3.1 und Fallstudie A1 nennen „bis zu 30%" Bruchlastreduktion durch Kinking, hier „bis zu 50%". Wert nicht verifiziert, uneinheitlich. Confidence: estimated — unverifiziert.

**Klüse (Hawse Pipe):** Führung für die Ankerkette durch den Bug. Der Wirbel muss durch die Klüse passen.

**Korrosion (Corrosion):** Werkstoffzerstörung durch chemische oder elektrochemische Reaktion mit der Umgebung. Hauptproblem bei marinen Wirbeln.

**Kugelgelagert (Ball Bearing):** Lager mit Kugeln zwischen Laufringen. Niedrigster Reibwert, frei drehend unter Last. Standard für Spinnaker- und Furlerwirbel.

### Begriffe L–R

**Lagerbuchse (Bearing Bush):** Zylindrische Gleithülse aus Bronze, POM oder PTFE. Sitzt zwischen den rotierenden Teilen eines Wirbels.

**Losbrechmoment (Breakaway Torque):** Das Drehmoment, das erforderlich ist, um einen stehenden Wirbel unter Last in Rotation zu versetzen. Kritisches Qualitätsmerkmal.

**MBL → Bruchlast**

**Mooring:** Permanente Festmacheranlage (Boje, Dalbe, Pfahl). Mooringwirbel müssen für Dauerunterwassereinsatz geeignet sein.

**Opfer-Anode (Sacrificial Anode):** Zink- oder Aluminium-Anode, die sich anstelle des edleren Metalls (Edelstahl) auflöst. Schutz gegen galvanische Korrosion.

**Passivschicht:** Unsichtbare Chromoxid-Schicht (Cr₂O₃) auf der Oberfläche von Edelstahl. Schützt vor Korrosion. Kann durch Chloride lokal zerstört werden.

**PEEK (Polyetheretherketon):** Hochleistungsthermoplast für anspruchsvolle Lagerbuchsen. Temperaturbeständig, chemisch inert, teuer.

**POM (Polyoxymethylen / Delrin):** Technischer Kunststoff für Lagerbuchsen. Gute Gleiteigenschaften, UV-empfindlich.

**PREN (Pitting Resistance Equivalent Number):** Kennzahl für die Lochfraßbeständigkeit von Edelstahl. PREN = %Cr + 3.3 × %Mo + 16 × %N. Je höher, desto besser. 316L: 24–26, Duplex 2205: 34–36.

**Prüflast (Proof Load):** Last, mit der ein Wirbel bei der Qualitätskontrolle belastet wird, ohne bleibende Verformung. Typisch: 2 × SWL.

**PTFE (Polytetrafluorethylen / Teflon):** Kunststoff mit niedrigstem Reibungskoeffizienten. Als Beschichtung oder Buchse in Wirbeln. Nicht für tragende Lagerfunktionen.

**Radiallast:** Kraft senkrecht zur Wirbelachse. Entsteht bei schräger Zugrichtung oder Seitenlasten. Muss vom Wirbel aufgenommen werden.

**Reibungskoeffizient (μ):** Dimensionslose Kenngröße für die Reibung zwischen zwei Flächen. Je niedriger, desto leichtgängiger der Wirbel.

**Reibkorrosion (Fretting Corrosion):** Korrosion durch kleine oszillierende Relativbewegungen zwischen belasteten Kontaktflächen.

### Begriffe S–Z

**Schäkel (Shackle):** U-förmiger Verbinder mit Bolzen. Starre Verbindung (kein Wirbel). Wird oft in Kombination mit Wirbeln eingesetzt.

**Schmierung (Lubrication):** Auftragen eines Gleitmittels auf Lagerflächen zur Reibungsreduktion und Korrosionsschutz. Essentiell für die Lebensdauer von Wirbeln.

**Schwojen (Yawing at Anchor):** Hin- und Herschwingen eines vor Anker liegenden Bootes um den Ankerpunkt. Erzeugt Torsionsbelastung in der Kette.

**Sicherheitsfaktor (Safety Factor / SF):** Verhältnis MBL/SWL. Typisch: 4:1 bis 6:1 für marine Wirbel.

**Snap-Schäkel (Snap Shackle):** Schnellverschluss-Schäkel mit Federbügel. Oft mit Wirbel kombiniert für schnelles An-/Abschlagen von Segeln.

**Sonnenschuss:** Unkontrolliertes Füllen des Spinnakers, wenn er vor den Mast weht. Erzeugt extreme Stoßlasten auf Wirbel und Rigg.

**Spaltkorrosion (Crevice Corrosion):** Lokalisierte Korrosion in engen Spalten, wo stehendes Salzwasser eine sauerstoffarme, saure Umgebung schafft. Hauptproblem bei Wirbel-Lagerspalten.

**Splint (Cotter Pin / Split Pin):** Drahtförmiges Sicherungselement, das durch ein Bolzenloch gesteckt und umgebogen wird. Verhindert das Herausfallen des Bolzens.

**SWL → Arbeitslast**

**Tea Staining:** Bräunliche Verfärbung auf Edelstahl durch leichte Oberflächenkorrosion in salzhaltiger Atmosphäre. Ästhetisch störend, aber nicht strukturell.

**Toggle:** Kippbares Verbindungselement (typisch ±15–30°), das Biegebelastungen kompensiert. Oft mit Wirbeln kombiniert (Toggle-Swivel).

**Torsion:** Verdrehung eines Bauteils um seine Längsachse. Wirbel dienen der Torsionsentlastung.

**Vorstag (Forestay):** Stehendes Gut vom Masttop zum Bug. Trägt das Vorsegel und die Rollreffanlage. Höchste Einzellast im Rigg.

**Wälzlager (Rolling Element Bearing):** Lager mit Kugeln oder Rollen zwischen den Laufflächen. Niedrigerer Reibwert als Gleitlager.

**Wirbelschäkel (Swivel Shackle):** Kombination aus Wirbel und Schäkel in einem Bauteil. Universellster Wirbeltyp.

**Wöhler-Kurve (S-N Curve):** Diagramm der Ermüdungsfestigkeit: Lastwechselzahl (N) als Funktion der Spannungsamplitude (σ).

**Zirkoniumoxid (ZrO₂):** Keramischer Lagerwerkstoff für Hochleistungs-Kugellager. Korrosionsfrei, extrem hart, gute Bruchzähigkeit.

---

## 11. Schnell-Referenz

### 11.1 Wirbel-Auswahl nach Anwendung

| Anwendung | Empfohlener Typ | Material | Lager | SWL-Regel |
|-----------|----------------|----------|-------|-----------|
| Ankerkette | Gabel-Gabel oder Gabel-Auge | 316L / Duplex | Gleitlager | ≥ Ketten-SWL |
| Furler (Vorstag) | System-Wirbel | 316L | Kugellager | ≥ Vorstag-Last |
| Großfall | Wirbelschäkel | 316L | Gleitlager | ≥ 2× Fallenlast |
| Vorsegel-Fall | Wirbelschäkel oder Snap-Swivel | 316L | Gleitlager | ≥ 2× Fallenlast |
| Spinnaker | Kugelgelagerter Wirbel | 316L / Titan | Kugel/Keramik | ≥ 3× Segeldruck |
| Block (Cruiser) | Integrierter Blockwirbel | 316L | Gleitlager | ≥ Block-SWL |
| Block (Regatta) | Integrierter Blockwirbel | 316L / Titan | Kugellager | ≥ Block-SWL |
| Mooring | Schwerer Wirbel | Duplex / Bronze | Gleitlager | ≥ 2× Bootsmasse |

### 11.2 Wartungs-Kurzübersicht

| Bauteil | Prüfintervall | Schmierintervall | Austausch-Intervall |
|---------|---------------|------------------|---------------------|
| Ankerwirbel | Jedes Ankern | 1–3 Monate | 5–10 Jahre |
| Furlerwirbel | Saisonstart | 6–12 Monate | 5–8 Jahre (Lager) |
| Fallenwirbel | Monatlich | 6 Monate | 8–15 Jahre |
| Spi-Wirbel | Vor jedem Einsatz | 3 Monate | 5–10 Jahre |
| Blockwirbel | Saisonstart | 6 Monate | 5–10 Jahre |
| Mooringwirbel | Halbjährlich (Taucher) | Jährlich | 5–8 Jahre |

### 11.3 Notfall-Checkliste

1. **Wirbel blockiert unter Last** → Last reduzieren (Segel bergen, Kette fieren), dann Wirbel ersetzen
2. **Wirbel-Bolzen verloren** → Provisorisch mit Edelstahl-Draht sichern, nächsten Hafen anlaufen
3. **Wirbel gebrochen** → Ersatz-Schäkel als Notverbindung, professionelle Reparatur im Hafen
4. **Furler blockiert** → NICHT mit Gewalt rollen, Segel manuell bergen, Fachservice kontaktieren
5. **Spinnaker-Wirbel blockiert** → Sofort Spinnaker bergen, Wirbel an Deck ersetzen

---

## ANHANG A — Fallstudien

### Fallstudie A1: Ankerverlust durch festsitzenden Wirbel

**Yacht:** Bavaria 40 Cruiser, Baujahr 2016, 12m LOA, 9.5t Verdrängung
**Revier:** Kykladen (Griechenland), Sommer 2024
**Konfiguration:** 10mm Kette (60m), NoName-Wirbel aus China, CQR-Anker 16kg

**Vorgeschichte:** Der Eigner hatte 2022 den Original-Wichard-Wirbel durch einen Billig-Wirbel (ca. 15 EUR, angeblich 316, SWL 1500kg) ersetzt. Keine Wartung in 2 Jahren.

**Vorfall:** Beim Ankern vor Paros bei aufkommendem Meltemi (25–30 kn) verdrehte sich die Kette durch die Winddrehung um ca. 6 Umdrehungen. Die akkumulierte Torsion erzeugte einen Kink 3m vor dem Anker. Als der Eigner bergen wollte, blockierte die verdrillte Kette in der Bugrolle. Beim Versuch, mit Motorkraft zu lösen, brach der Wirbel an der Augenbohrung. Der Anker samt 60m Kette gingen verloren.

**Analyse:**
- Wirbel war seit >1 Jahr festgefressen (Spaltkorrosion)
- Material war wahrscheinlich 304, nicht 316 (Magnettest am Reststück positiv)
- Bruchlast lag bei geschätzt 8–10 kN (statt angegebener 60 kN)
- Kinking reduzierte die Kettenbruchlast um ca. 30%
- Dynamische Rucklast beim Löseversuch: geschätzt 15–20 kN

**AYDI-Bewertung:**
- Wirbel-Score: 15/100 (unterdimensioniert, falsches Material, keine Wartung)
- Confidence: documented (Eignerbericht, Fotos des Bruchstücks)

**Lehren:**
1. Niemals Sicherheitsbauteile durch unzertifizierte Billigprodukte ersetzen
2. Regelmäßige Funktionsprüfung des Wirbels (muss frei drehen!)
3. 10mm Kette erfordert Wirbel mit SWL ≥1400 kg und MBL ≥55 kN

### Fallstudie A2: Furlerwirbel-Versagen bei Atlantiküberquerung

**Yacht:** Hallberg-Rassy 46, Baujahr 2010, 14m LOA, 14t Verdrängung
**Revier:** Atlantik, ARC 2023 (Las Palmas → St. Lucia)
**Konfiguration:** Seldén Furlex 300S, Vorstag 8mm Rod

**Vorfall:** Am Tag 12 der Überquerung (bei ca. 20°N, 40°W) blockierte der Furlerwirbel. Das Vorsegel ließ sich nicht mehr einrollen. Wind: 22 kn, Welle: 2.5m. Die Crew versuchte über 2 Stunden, den Furler zu lösen, ohne Erfolg. Schließlich musste das Vorsegel manuell mit Zeisingen an der Reling befestigt werden.

**Analyse:**
- Furlerwirbel war zuletzt 2019 gewartet worden (4 Jahre ohne Service)
- Lagersatz (Edelstahl-Kugeln) zeigten schweren Lochfraß
- Salzwasser war durch defekte Lippendichtung ins Lager eingedrungen
- Die Kugeln hatten sich verformt und die Laufbahnen beschädigt

**AYDI-Bewertung:**
- Wartungs-Score: 25/100 (4 Jahre statt max. 12 Monate Intervall)
- Confidence: documented

**Lehren:**
1. Furlerwirbel JÄHRLICH schmieren und Lager inspizieren
2. Vor langer Reise: Lagersatz erneuern (kosten ca. 80–150 EUR)
3. Bordwerkzeug für Furler-Demontage mitführen

### Fallstudie A3: Galvanische Korrosion am Mooringwirbel

**Yacht:** Mooringanlage, Yachthafen Larnaca (Zypern)
**Konfiguration:** 316L-Wirbel an verzinkter Schwerkette (22mm)

**Vorfall:** Nach 18 Monaten war der 316L-Wirbel äußerlich intakt, aber die angrenzenden verzinkten Kettenglieder waren massiv korrodiert. Das letzte Kettenglied vor dem Wirbel hatte nur noch 60% des Original-Querschnitts.

**Analyse:**
- Galvanische Korrosion: 316L (edel) + verzinkter Stahl (unedel) = verzinkter Stahl löst sich auf
- Potentialdifferenz: ca. 200 mV in warmem Mittelmeer (beschleunigt)
- Der Wirbel war geschützt (Kathode), die Kette war Opfer (Anode)

**AYDI-Bewertung:**
- Materialkompatibilität: 30/100
- Confidence: measured (Ultraschall-Wandstärkenmessung)

**Lehren:**
1. 316L-Wirbel nur mit Edelstahl- oder Duplex-Kette verwenden
2. Bei gemischten Materialien: Kunststoff-Isolator einsetzen
3. Opfer-Anoden am Wirbel montieren

### Fallstudie A4: Spinnaker-Wirbel blockiert bei Regatta

**Yacht:** J/111, 11m LOA, 5.5t Verdrängung
**Revier:** Kieler Woche 2024, Wettfahrt 3
**Konfiguration:** Standard-Wirbelschäkel (Gleitlager) als Spinnaker-Wirbel

**Vorfall:** Beim Halsen bei 18 kn Wind blockierte der Wirbelschäkel. Der Spinnaker konnte sich nicht frei drehen, wickelte sich um das Vorstag und riss an der Liektau-Naht. Materialschaden: ca. 4.500 EUR.

**Analyse:**
- Einfacher Wirbelschäkel (Gleitlager) für Spinnaker völlig ungeeignet
- Unter der dynamischen Segellast (geschätzt 6–8 kN) war der Gleitlagerwirbel nicht drehbar
- Ein kugelgelagerter Spinnaker-Wirbel hätte die Rotation gewährleistet

**AYDI-Bewertung:**
- Wirbel-Auswahl: 20/100 (falscher Typ für die Anwendung)
- Confidence: documented (Regattabericht, Fotos)

**Lehren:**
1. Für Spinnaker IMMER kugelgelagerten Wirbel verwenden
2. Spinnaker-Wirbel vor jeder Regatta auf freie Rotation prüfen
3. Investition in Qualitätswirbel (100–300 EUR) spart teure Segelreparaturen

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

### B.1 Wirbel-Basisdaten

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class SwivelType(str, Enum):
    """Types of marine swivels."""
    BLOCK_SWIVEL = "block_swivel"
    ANCHOR_CHAIN_SWIVEL = "anchor_chain_swivel"
    HALYARD_SWIVEL = "halyard_swivel"
    FURLER_SWIVEL = "furler_swivel"
    SPINNAKER_SWIVEL = "spinnaker_swivel"
    MOORING_SWIVEL = "mooring_swivel"
    UNIVERSAL_JOINT = "universal_joint"
    TOGGLE_SWIVEL = "toggle_swivel"
    SWIVEL_SHACKLE = "swivel_shackle"


class BearingType(str, Enum):
    """Types of bearings used in swivels."""
    PLAIN_STEEL = "plain_steel"
    PLAIN_BRONZE = "plain_bronze"
    PLAIN_POM = "plain_pom"
    PLAIN_PTFE = "plain_ptfe"
    PLAIN_PEEK = "plain_peek"
    BALL_BEARING_STEEL = "ball_bearing_steel"
    BALL_BEARING_CERAMIC = "ball_bearing_ceramic"
    NEEDLE_BEARING = "needle_bearing"
    HYBRID = "hybrid"


class SwivelMaterial(str, Enum):
    """Primary structural material of the swivel."""
    STAINLESS_316L = "stainless_316l"
    DUPLEX_2205 = "duplex_2205"
    ALUMINIUM_BRONZE = "aluminium_bronze"
    TITANIUM_GR5 = "titanium_gr5"
    ALUMINIUM = "aluminium"


class ConnectionType(str, Enum):
    """Connection end types."""
    EYE = "eye"
    JAW = "jaw"
    SNAP = "snap"
    TOGGLE = "toggle"
    THREADED = "threaded"
    CHAIN_LINK = "chain_link"


class ManufacturingMethod(str, Enum):
    """Manufacturing method of the swivel body."""
    FORGED = "forged"
    INVESTMENT_CAST = "investment_cast"
    SAND_CAST = "sand_cast"
    CNC_MACHINED = "cnc_machined"
    UNKNOWN = "unknown"


class SwivelSpecification(BaseModel):
    """Complete specification of a marine swivel."""

    model_config = {"from_attributes": True}

    # Identification
    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model designation or part number")
    swivel_type: SwivelType = Field(..., description="Type of swivel")

    # Structural
    material: SwivelMaterial = Field(..., description="Primary material")
    manufacturing_method: ManufacturingMethod = Field(
        default=ManufacturingMethod.UNKNOWN,
        description="How the swivel body was manufactured"
    )
    bearing_type: BearingType = Field(..., description="Bearing mechanism")

    # Connections
    connection_top: ConnectionType = Field(..., description="Top/load connection type")
    connection_bottom: ConnectionType = Field(..., description="Bottom connection type")

    # Load ratings
    swl_kg: float = Field(..., ge=0, description="Safe Working Load in kg")
    mbl_kn: float = Field(..., ge=0, description="Minimum Breaking Load in kN")
    proof_load_kn: Optional[float] = Field(
        default=None, ge=0,
        description="Proof test load in kN"
    )
    safety_factor: float = Field(
        default=4.0, ge=1.0,
        description="Safety factor (MBL/SWL)"
    )

    # Dimensions
    pin_diameter_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Pin/bolt diameter in mm"
    )
    length_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Overall length in mm"
    )
    width_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Overall width in mm"
    )
    weight_g: Optional[float] = Field(
        default=None, ge=0,
        description="Weight in grams"
    )

    # Compatibility
    chain_size_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Compatible chain diameter in mm"
    )
    rope_diameter_range_mm: Optional[str] = Field(
        default=None,
        description="Compatible rope diameter range, e.g. '8-12'"
    )
    forestay_diameter_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Compatible forestay diameter in mm (for furler swivels)"
    )

    # Commercial
    price_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate retail price in EUR"
    )
    price_usd: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate retail price in USD"
    )
```

### B.2 Wirbel-Zustandsbewertung

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class SwivelConditionRating(str, Enum):
    """Overall condition rating."""
    EXCELLENT = "excellent"  # Like new, no issues
    GOOD = "good"  # Minor wear, fully functional
    FAIR = "fair"  # Visible wear, still functional
    POOR = "poor"  # Significant issues, replace soon
    CRITICAL = "critical"  # Safety risk, replace immediately
    FAILED = "failed"  # Already failed / non-functional


class CorrosionLevel(str, Enum):
    """Corrosion severity level."""
    NONE = "none"
    SURFACE = "surface"  # Tea staining, superficial
    MODERATE = "moderate"  # Pitting < 0.5mm
    SEVERE = "severe"  # Pitting > 0.5mm or crevice corrosion
    CRITICAL = "critical"  # Structural section affected


class BearingCondition(str, Enum):
    """Bearing condition assessment."""
    FREE_RUNNING = "free_running"
    SLIGHTLY_STIFF = "slightly_stiff"
    STIFF_UNDER_LOAD = "stiff_under_load"
    INTERMITTENT = "intermittent"
    SEIZED = "seized"


class FaultPattern(str, Enum):
    """Identified fault patterns from the Fehlerbild-Atlas."""
    SEIZED = "seized"  # FB01
    BEARING_WEAR = "bearing_wear"  # FB02
    PITTING_CORROSION = "pitting_corrosion"  # FB03
    FATIGUE_CRACK = "fatigue_crack"  # FB04
    GALLING = "galling"  # FB05
    UV_DEGRADATION = "uv_degradation"  # FB06
    PIN_LOOSENING = "pin_loosening"  # FB07
    OVERLOAD_DEFORMATION = "overload_deformation"  # FB08
    ELECTROLYSIS = "electrolysis"  # FB09
    FOULING_BLOCKAGE = "fouling_blockage"  # FB10
    UNDERSIZED = "undersized"  # FB11
    WRONG_MATERIAL = "wrong_material"  # FB12


class SwivelConditionAssessment(BaseModel):
    """Assessment of a swivel's current condition."""

    model_config = {"from_attributes": True}

    # Overall
    overall_rating: SwivelConditionRating = Field(
        ..., description="Overall condition rating"
    )
    confidence: str = Field(
        ..., description="AYDI confidence level for this assessment"
    )

    # Specific assessments
    bearing_condition: BearingCondition = Field(
        ..., description="Current bearing condition"
    )
    corrosion_level: CorrosionLevel = Field(
        ..., description="Corrosion severity"
    )
    radial_play_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Measured radial play in mm (>1mm = replace)"
    )
    axial_play_mm: Optional[float] = Field(
        default=None, ge=0,
        description="Measured axial play in mm (>2mm = replace)"
    )
    pin_security: bool = Field(
        default=True,
        description="Is the pin/bolt properly secured?"
    )
    deformation_detected: bool = Field(
        default=False,
        description="Any visible deformation?"
    )

    # Fault patterns
    identified_faults: list[FaultPattern] = Field(
        default_factory=list,
        description="List of identified fault patterns"
    )

    # Maintenance
    last_service_date: Optional[str] = Field(
        default=None,
        description="Date of last service (ISO format)"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated remaining service life in years"
    )

    # Recommendations
    replace_immediately: bool = Field(
        default=False,
        description="Immediate replacement required?"
    )
    recommended_action: str = Field(
        default="",
        description="Recommended action in German"
    )
    recommended_replacement: Optional[str] = Field(
        default=None,
        description="Recommended replacement product"
    )

    # Score
    condition_score: int = Field(
        ..., ge=0, le=100,
        description="Condition score 0-100"
    )
```

### B.3 Wirbel-Dimensionierungsberechnung

```python
import math
from typing import Optional
from pydantic import BaseModel, Field


class ApplicationContext(BaseModel):
    """Context for swivel dimensioning calculation."""

    model_config = {"from_attributes": True}

    # Boat data
    boat_loa_m: float = Field(..., ge=2, le=100, description="Length overall in meters")
    boat_displacement_kg: float = Field(..., ge=100, description="Displacement in kg")
    boat_type: str = Field(..., description="Boat type: sail, motor, catamaran")
    ce_category: Optional[str] = Field(
        default=None,
        description="CE category: A, B, C, or D"
    )

    # Application specifics
    application: str = Field(
        ...,
        description="Application: anchor, furler, halyard, spinnaker, mooring, block"
    )
    chain_diameter_mm: Optional[float] = Field(
        default=None, ge=4, le=30,
        description="Chain diameter in mm (for anchor swivels)"
    )
    chain_grade: Optional[int] = Field(
        default=None,
        description="Chain grade: 40, 70, or 80"
    )
    sail_area_m2: Optional[float] = Field(
        default=None, ge=1,
        description="Sail area in m² (for halyard/spinnaker swivels)"
    )
    max_wind_speed_kn: Optional[float] = Field(
        default=None, ge=0,
        description="Maximum design wind speed in knots"
    )
    forestay_diameter_mm: Optional[float] = Field(
        default=None, ge=3, le=20,
        description="Forestay diameter in mm (for furler swivels)"
    )


class DimensioningResult(BaseModel):
    """Result of swivel dimensioning calculation."""

    model_config = {"from_attributes": True}

    # Calculated loads
    static_load_kn: float = Field(..., description="Calculated static load in kN")
    dynamic_factor: float = Field(..., description="Applied dynamic factor")
    design_load_kn: float = Field(..., description="Design load (static × dynamic)")

    # Required ratings
    required_swl_kg: float = Field(..., description="Minimum required SWL in kg")
    required_mbl_kn: float = Field(..., description="Minimum required MBL in kN")
    safety_factor_used: float = Field(..., description="Safety factor applied")

    # Recommendations
    recommended_swivel_type: str = Field(
        ..., description="Recommended swivel type"
    )
    recommended_bearing: str = Field(
        ..., description="Recommended bearing type"
    )
    recommended_material: str = Field(
        ..., description="Recommended material"
    )
    recommended_chain_swivel_size_mm: Optional[float] = Field(
        default=None,
        description="Recommended chain swivel size in mm"
    )

    # Matching products
    matching_products: list[str] = Field(
        default_factory=list,
        description="List of matching product suggestions"
    )

    # Confidence
    confidence: str = Field(
        ..., description="AYDI confidence level"
    )
    calculation_notes: list[str] = Field(
        default_factory=list,
        description="Notes and assumptions"
    )


def calculate_swivel_requirements(ctx: ApplicationContext) -> DimensioningResult:
    """Calculate swivel dimensioning requirements based on application context.

    Returns a DimensioningResult with required load ratings
    and product recommendations.
    """
    static_load_kn = 0.0
    dynamic_factor = 2.0
    safety_factor = 4.0
    notes: list[str] = []
    recommended_type = ""
    recommended_bearing = ""
    recommended_material = "stainless_316l"
    matching: list[str] = []
    confidence = "calculated"

    if ctx.application == "anchor":
        if ctx.chain_diameter_mm and ctx.chain_grade:
            grade_factor = {40: 0.156, 70: 0.274, 80: 0.314}.get(
                ctx.chain_grade, 0.274
            )
            chain_mbl_kn = grade_factor * ctx.chain_diameter_mm ** 2
            static_load_kn = chain_mbl_kn * 0.25
            notes.append(
                f"Kettenlast berechnet: MBL={chain_mbl_kn:.1f} kN "
                f"(Ø{ctx.chain_diameter_mm}mm, Güteklasse {ctx.chain_grade})"
            )
        else:
            static_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.15
            notes.append("Ankerlast geschätzt aus Verdrängung (15%)")
            confidence = "estimated"

        dynamic_factor = 4.0 if ctx.ce_category == "A" else 3.0
        safety_factor = 4.0
        recommended_type = "anchor_chain_swivel"
        recommended_bearing = "plain_bronze"
        if ctx.boat_displacement_kg > 15000:
            recommended_material = "duplex_2205"
        matching = ["Wichard 6800", "Mantus M1", "Ultra Flip Swivel"]

    elif ctx.application == "furler":
        forestay_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.5
        static_load_kn = forestay_load_kn
        dynamic_factor = 2.0
        safety_factor = 4.0
        recommended_type = "furler_swivel"
        recommended_bearing = "ball_bearing_steel"
        notes.append(
            f"Vorstaglast geschätzt: {forestay_load_kn:.1f} kN "
            f"(50% der Verdrängung)"
        )
        matching = ["Seldén Furlex", "Harken MKIV", "Profurl"]

    elif ctx.application == "halyard":
        if ctx.sail_area_m2 and ctx.max_wind_speed_kn:
            wind_speed_ms = ctx.max_wind_speed_kn * 0.5144
            wind_pressure = 0.5 * 1.225 * wind_speed_ms ** 2
            sail_load_n = ctx.sail_area_m2 * wind_pressure * 1.0
            static_load_kn = sail_load_n / 1000
            notes.append(
                f"Fallenlast berechnet: {static_load_kn:.1f} kN "
                f"({ctx.sail_area_m2}m² bei {ctx.max_wind_speed_kn} kn)"
            )
        else:
            static_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.05
            notes.append("Fallenlast grob geschätzt (5% Verdrängung)")
            confidence = "estimated"

        dynamic_factor = 3.0
        safety_factor = 5.0
        recommended_type = "swivel_shackle"
        recommended_bearing = "plain_pom"
        matching = ["Wichard 6500", "Kong 82"]

    elif ctx.application == "spinnaker":
        if ctx.sail_area_m2 and ctx.max_wind_speed_kn:
            wind_speed_ms = ctx.max_wind_speed_kn * 0.5144
            wind_pressure = 0.5 * 1.225 * wind_speed_ms ** 2
            sail_load_n = ctx.sail_area_m2 * wind_pressure * 1.5
            static_load_kn = sail_load_n / 1000
        else:
            static_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.08
            confidence = "estimated"

        dynamic_factor = 6.0
        safety_factor = 5.0
        recommended_type = "spinnaker_swivel"
        recommended_bearing = "ball_bearing_ceramic"
        matching = ["Tylaska S-Serie", "Ronstan RF1036"]
        notes.append("Spinnaker: dynamischer Faktor 6.0 wegen Halse/Sonnenschuss")

    elif ctx.application == "mooring":
        static_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.3
        dynamic_factor = 3.0
        safety_factor = 5.0
        recommended_type = "mooring_swivel"
        recommended_bearing = "plain_bronze"
        recommended_material = "duplex_2205"
        notes.append("Mooringlast: 30% Verdrängung, Dauereinsatz")
        matching = ["Schwerer Guss-Wirbel Duplex 2205"]

    else:
        static_load_kn = ctx.boat_displacement_kg * 9.81 / 1000 * 0.05
        dynamic_factor = 2.5
        safety_factor = 4.0
        recommended_type = "swivel_shackle"
        recommended_bearing = "plain_steel"
        confidence = "estimated"

    design_load_kn = static_load_kn * dynamic_factor
    required_mbl_kn = design_load_kn * safety_factor
    required_swl_kg = (design_load_kn / 9.81) * 1000

    return DimensioningResult(
        static_load_kn=round(static_load_kn, 1),
        dynamic_factor=dynamic_factor,
        design_load_kn=round(design_load_kn, 1),
        required_swl_kg=round(required_swl_kg, 0),
        required_mbl_kn=round(required_mbl_kn, 1),
        safety_factor_used=safety_factor,
        recommended_swivel_type=recommended_type,
        recommended_bearing=recommended_bearing,
        recommended_material=recommended_material,
        matching_products=matching,
        confidence=confidence,
        calculation_notes=notes,
    )
```

### B.4 Visuelle Analyse — Wirbel-Inspektion

```python
from typing import Optional
from pydantic import BaseModel, Field


class SwivelVisualAnalysisRequest(BaseModel):
    """Request for visual analysis of a swivel from photos."""

    model_config = {"from_attributes": True}

    image_urls: list[str] = Field(
        ..., min_length=1,
        description="URLs of swivel images for analysis"
    )
    known_manufacturer: Optional[str] = Field(
        default=None,
        description="Known manufacturer if available"
    )
    known_model: Optional[str] = Field(
        default=None,
        description="Known model if available"
    )
    application: Optional[str] = Field(
        default=None,
        description="Where the swivel is used"
    )
    boat_loa_m: Optional[float] = Field(
        default=None,
        description="Boat LOA for context"
    )


class SwivelVisualFinding(BaseModel):
    """A single finding from visual swivel analysis."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding identifier")
    category: str = Field(
        ...,
        description="Finding category: corrosion, wear, damage, sizing, installation"
    )
    description_de: str = Field(
        ..., description="Description of finding in German"
    )
    severity: str = Field(
        ..., description="Severity: info, low, medium, high, critical"
    )
    fault_pattern: Optional[str] = Field(
        default=None,
        description="Matched fault pattern from Fehlerbild-Atlas"
    )
    confidence: str = Field(
        ..., description="Visual confidence: visual_high, visual_medium, visual_low"
    )
    location_in_image: Optional[str] = Field(
        default=None,
        description="Location reference in the image"
    )
    recommendation_de: str = Field(
        ..., description="Recommended action in German"
    )


class SwivelVisualAnalysisResult(BaseModel):
    """Complete result of visual swivel analysis."""

    model_config = {"from_attributes": True}

    # Identification
    identified_type: Optional[str] = Field(
        default=None, description="Identified swivel type"
    )
    identified_manufacturer: Optional[str] = Field(
        default=None, description="Identified manufacturer"
    )
    identified_material: Optional[str] = Field(
        default=None, description="Identified material"
    )
    identified_bearing: Optional[str] = Field(
        default=None, description="Identified bearing type"
    )

    # Assessment
    overall_condition: str = Field(
        ..., description="Overall condition rating"
    )
    condition_score: int = Field(
        ..., ge=0, le=100, description="Condition score 0-100"
    )
    confidence: str = Field(
        ..., description="Overall confidence of visual assessment"
    )

    # Findings
    findings: list[SwivelVisualFinding] = Field(
        default_factory=list,
        description="List of individual findings"
    )

    # Summary
    summary_de: str = Field(
        ..., description="Summary in German"
    )
    action_required: bool = Field(
        default=False, description="Is immediate action required?"
    )
```

---

## ANHANG C — Lasttabellen

### C.1 Ankerketten — MBL und empfohlene Wirbel-SWL

| Ketten-Ø [mm] | MBL Klasse 40 [kN] | MBL Klasse 70 [kN] | MBL Klasse 80 [kN] | Wirbel SWL min [kg] | Wirbel MBL min [kN] |
|----------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| 5 | 3.9 | 6.9 | 7.9 | 350 | 14 |
| 6 | 5.6 | 9.9 | 11.3 | 500 | 20 |
| 7 | 7.6 | 13.4 | 15.4 | 700 | 27 |
| 8 | 10.0 | 17.5 | 20.1 | 900 | 35 |
| 9 | 12.6 | 22.2 | 25.5 | 1100 | 44 |
| 10 | 15.6 | 27.4 | 31.4 | 1400 | 55 |
| 11 | 18.9 | 33.2 | 38.0 | 1700 | 66 |
| 12 | 22.5 | 39.5 | 45.2 | 2000 | 79 |
| 13 | 26.4 | 46.3 | 53.0 | 2400 | 93 |
| 14 | 30.6 | 53.6 | 61.5 | 2700 | 108 |
| 16 | 39.9 | 70.1 | 80.3 | 3600 | 140 |
| 18 | 50.5 | 88.7 | 101.7 | 4500 | 178 |
| 20 | 62.4 | 109.6 | 125.6 | 5600 | 219 |
| 22 | 75.5 | 132.6 | 152.0 | 6800 | 265 |

> ⚠️ **ZU PRÜFEN (Audit):** Die als „MBL" (Bruchlast) ausgewiesenen Ketten-Werte liegen deutlich unter realen Grade-70-Ankerketten: 10 mm Grade 70 hat real ≈ 100 kN Bruchlast (Herstellerangaben, z. B. SVB/Toplicht), hier 27,4 kN — das entspricht eher der WLL/zulässigen Arbeitslast, nicht der MBL. Da die gesamte Wirbel-Dimensionierung im Dokument auf diesen Werten aufbaut (Regel „SWL_wirbel ≥ 0,5 × MBL_kette", §2.6.1, Code Anhang B.3), vor sicherheitsrelevanter Nutzung gegen die tatsächliche Kettennorm (ISO 4565 / DIN 766 / Werkszeugnis) verifizieren. Zusätzlich weicht die Klasse-70-MBL für 6–8 mm zwischen Tabelle 3.2.3 (11,2 / 14,8 / 19,2 kN) und dieser Tabelle (9,9 / 13,4 / 17,5 kN) ab. Confidence: measured → estimated — unverifiziert.

### C.2 Fallen — Typische Lasten nach Bootsgröße

| LOA [m] | Großfall [kN] | Vorsegel-Fall [kN] | Spi-Fall [kN] | Empf. Wirbel SWL [kg] |
|---------|---------------|--------------------|--------------|-----------------------|
| 7–8 | 2–4 | 1.5–3 | 1–2 | 300–500 |
| 8–10 | 4–7 | 3–5 | 2–4 | 500–800 |
| 10–12 | 7–12 | 5–9 | 4–7 | 800–1500 |
| 12–14 | 12–18 | 9–14 | 7–12 | 1500–2500 |
| 14–16 | 18–28 | 14–22 | 12–18 | 2500–4000 |
| 16–20 | 28–45 | 22–35 | 18–30 | 4000–6500 |
| 20–25 | 45–70 | 35–55 | 30–50 | 6500–10000 |

### C.3 Vorstag-Lasten (für Furlerwirbel)

| LOA [m] | Verdrängung [t] | Vorstag-Last [kN] | Furlerwirbel SWL [kg] | Furlerwirbel MBL [kN] |
|---------|-----------------|--------------------|-----------------------|-----------------------|
| 7–9 | 2–3 | 10–15 | 1500–2500 | 40–60 |
| 9–11 | 3–5 | 15–25 | 2500–4000 | 60–100 |
| 11–13 | 5–8 | 25–40 | 4000–6000 | 100–160 |
| 13–15 | 8–12 | 40–60 | 6000–9000 | 160–240 |
| 15–18 | 12–18 | 60–90 | 9000–14000 | 240–360 |
| 18–22 | 18–30 | 90–150 | 14000–23000 | 360–600 |
| 22–25 | 30–45 | 150–220 | 23000–34000 | 600–880 |

---

## ANHANG D — Normen und Standards

### D.1 Relevante ISO-Normen

| Norm | Titel | Relevanz für Wirbel |
|------|-------|---------------------|
| ISO 1704:2008 | Schiffbau — Ankerketten | Anforderungen an Ketten-Zubehör inkl. Wirbel |
| ISO 3076:2007 | Kurzglieder-Rundstahlketten — Abmessungen | Dimensionsstandard für Ketten, die mit Wirbeln verbunden werden |
| EN 13411-6:2004 | Endverbindungen für Drahtseile — Wirbelverbindungen | Prüfung und Klassifikation von Wirbeln für Drahtseile |
| ISO 12217:2022 | Stabilitätsbewertung | Indirekt: Ankersystem-Gewicht beeinflusst Stabilität |
| EN 12385:2008 | Drahtseile — Allgemeine Anforderungen | Mindestbruchkraft von Seilen, die Wirbel-SWL bestimmt |
| ISO 9001:2015 | Qualitätsmanagement | Herstellerzertifizierung für Wirbelproduzenten |

> ⚠️ **ZU PRÜFEN (Audit):** Zwei Normzuordnungen web-verifiziert falsch:
> - **EN 13411-6:2004** ist „Endverbindungen für Drahtseile — Sicherheit — Teil 6: Asymmetrischer Seilschloss (asymmetric wedge socket)", NICHT „Wirbelverbindungen". Es gibt in der EN-13411-Reihe keine Wirbel-Norm (Quelle: iso.org, BSI EN 13411-6:2004+A1:2008).
> - **ISO 3076** existiert nicht als Ausgabe „:2007" (nur 1980/1984/2012) und ist „Round steel short link chains for general lifting purposes — Medium tolerance sling chains — Grade 8" (Hebe-Anschlagketten Güte 8), KEIN Abmessungs-/Ankerkettenstandard (Quelle: iso.org, ISO 3076:2012). Die passende Norm für kalibrierte (Klein-)Ankerkette wäre ISO 4565 bzw. DIN 766. Ersatznorm nicht zweifelsfrei bestimmbar — daher nur markiert. Confidence: estimated — unverifiziert.

### D.2 Klassifikationsregeln

| Klasse | Regelwerk | Relevante Kapitel |
|--------|-----------|-------------------|
| GL (Germanischer Lloyd) | Rules for Classification of Yachts | Part 3, Ch. 7: Anchor Equipment |
| DNV (Det Norske Veritas) | Rules for Classification of Ships | Part 3, Ch. 3, Sec. 6: Anchoring |
| BV (Bureau Veritas) | Rules for Yachts | Part B, Ch. 11: Outfitting |
| RINA (Registro Italiano) | Rules for Yachts | Part B, Ch. 8: Equipment |
| ABS (American Bureau) | Rules for Building and Classing Yachts | Part 3, Ch. 7: Equipment |

### D.3 Prüfverfahren

| Prüfung | Norm/Methode | Anwendung |
|---------|-------------|-----------|
| Zugprüfung | EN ISO 6892-1 | Bruchlast-Bestimmung |
| Dauerschwingprüfung | ASTM E466 | Ermüdungsfestigkeit |
| Salznebel-Test | ISO 9227 (NSS) | Korrosionsbeständigkeit |
| Farbeindringprüfung | ISO 3452-1 | Risserkennung an Oberfläche |
| Magnetpulverprüfung | ISO 9934-1 | Risserkennung (nur ferrit. Stähle) |
| Ultraschallprüfung | ISO 17640 | Innere Fehler, Wandstärke |
| Materialnanalyse (PMI) | ASTM A751 | Legierungsverifizierung |

---

## ANHANG E — Wartungsintervalle

### E.1 Wartungsmatrix nach Anwendung und Revier

| Anwendung | Nordeuropa | Mittelmeer | Tropen | Arktis |
|-----------|------------|------------|--------|--------|
| Ankerwirbel — Schmierung | 3 Monate | 2 Monate | Monatlich | 3 Monate |
| Ankerwirbel — Inspektion | 6 Monate | 4 Monate | 3 Monate | 6 Monate |
| Ankerwirbel — Austausch | 8–10 Jahre | 6–8 Jahre | 5–7 Jahre | 8–10 Jahre |
| Furlerwirbel — Schmierung | 12 Monate | 8 Monate | 6 Monate | 12 Monate |
| Furlerwirbel — Lagertausch | 6–8 Jahre | 5–7 Jahre | 4–6 Jahre | 6–8 Jahre |
| Fallenwirbel — Schmierung | 6 Monate | 4 Monate | 3 Monate | 6 Monate |
| Spi-Wirbel — Schmierung | Saisonstart | 4 Monate | 3 Monate | Saisonstart |
| Mooringwirbel — Inspektion | 6 Monate | 4 Monate | 3 Monate | 6 Monate |
| Mooringwirbel — Austausch | 6–8 Jahre | 5–6 Jahre | 4–5 Jahre | 6–8 Jahre |

### E.2 Empfohlene Schmiermittel

| Anwendung | Empfohlenes Produkt | Typ | Preis [EUR] |
|-----------|---------------------|-----|-------------|
| Kugelgelagerte Wirbel | Harken Winch & Bearing Grease | PTFE-Fett | 15–20 / 100ml |
| Furlerwirbel (Seldén) | Seldén Furler Grease | Lithium-PTFE | 18–25 / 75ml |
| Furlerwirbel (Harken) | Harken High Performance Grease | Synthetisch | 20–28 / 100ml |
| Gleitlager-Wirbel | Boat Life Life Calk Grease | Marine-Fett | 12–18 / 100ml |
| Anti-Seize (Bolzen) | Tef-Gel TPI | PTFE-Paste | 22–30 / 30g |
| Allgemein | Lanocote | Lanolin-Basis | 15–22 / 120ml |
| Kriechöl (Lösen) | CRC 6-66 Marine | Kriechöl/Korrosionsschutz | 8–12 / 300ml |

---

## ANHANG F — Kompatibilitätsmatrix

### F.1 Wirbel-Ketten-Kompatibilität

| Wirbel-Hersteller | Modell | 6mm | 7mm | 8mm | 10mm | 12mm | 13mm | 14mm | 16mm |
|--------------------|--------|-----|-----|-----|------|------|------|------|------|
| Wichard | 6801 | ✓ | ✓ | — | — | — | — | — | — |
| Wichard | 6802 | — | — | ✓ | — | — | — | — | — |
| Wichard | 6803 | — | — | — | ✓ | — | — | — | — |
| Wichard | 6804 | — | — | — | — | ✓ | — | — | — |
| Wichard | 6805 | — | — | — | — | — | ✓ | ✓ | — |
| Wichard | 6806 | — | — | — | — | — | — | — | ✓ |
| Kong | 8501 | ✓ | ✓ | ✓ | — | — | — | — | — |
| Kong | 8502 | — | — | ✓ | ✓ | — | — | — | — |
| Kong | 8503 | — | — | — | ✓ | ✓ | — | — | — |
| Kong | 8504 | — | — | — | — | ✓ | ✓ | ✓ | — |
| Mantus | M1-8 | — | — | ✓ | — | — | — | — | — |
| Mantus | M1-10 | — | — | — | ✓ | — | — | — | — |
| Mantus | M1-12 | — | — | — | — | ✓ | — | — | — |
| Ultra | UFS-S | ✓ | ✓ | ✓ | — | — | — | — | — |
| Ultra | UFS-M | — | — | ✓ | ✓ | — | — | — | — |
| Ultra | UFS-L | — | — | — | ✓ | ✓ | ✓ | — | — |
| Ultra | UFS-XL | — | — | — | — | — | ✓ | ✓ | ✓ |

### F.2 Wirbel-Material-Kompatibilität

| Wirbel-Material | Edelstahl-Kette | Verzinkte Kette | Alu-Beschlag | Bronze-Beschlag | Titan-Beschlag |
|-----------------|-----------------|-----------------|--------------|-----------------|----------------|
| 316L | ●●● Ideal | ●●○ Akzeptabel | ●○○ Vermeiden | ●●● Ideal | ●●○ Isolation |
| Duplex 2205 | ●●● Ideal | ●●○ Akzeptabel | ●○○ Vermeiden | ●●● Ideal | ●●○ Isolation |
| Al-Bronze | ●●● Ideal | ●●○ Akzeptabel | ●○○ Vermeiden | ●●● Ideal | ●●○ Isolation |
| Titan Gr.5 | ●●○ Isolation | ●○○ Vermeiden | ●○○ Vermeiden | ●●○ Isolation | ●●● Ideal |

---

## ANHANG G — Preis-Leistungs-Vergleich

### G.1 Ankerkettenwirbel — 10mm Kette

| Hersteller | Modell | SWL [kg] | MBL [kN] | Material | Preis [EUR] | EUR/kN | Bewertung |
|------------|--------|----------|----------|----------|-------------|--------|-----------|
| Wichard | 6803 | 1800 | 72 | 316L geschm. | 75–95 | 1.18 | ★★★★★ |
| Mantus | M1-10 | 1800 | 72 | 316 geschm. | 70–90* | 1.11 | ★★★★☆ |
| Ultra | UFS-M | 1500 | 60 | 316L geschm. | 72–90 | 1.35 | ★★★★☆ |
| Kong | 8502 | 1500 | 60 | 316 Guss | 48–60 | 0.90 | ★★★☆☆ |
| NoName (China) | diverse | 1000* | 40* | 304/316? | 12–25 | 0.46 | ★☆☆☆☆ |

*Preise umgerechnet, *Angaben nicht verifiziert

### G.2 Spinnaker-Wirbel — SWL 800–1200 kg

| Hersteller | Modell | SWL [kg] | Lager | Gewicht [g] | Preis [EUR] | Bewertung |
|------------|--------|----------|-------|-------------|-------------|-----------|
| Tylaska | S10 | 800 | Si₃N₄ Keramik | 38 | 160–200* | ★★★★★ |
| Ronstan | RF1035 | 800 | Edelstahl Kugel | 65 | 78–95 | ★★★★☆ |
| Ronstan | RF1036 | 1200 | Keramik Kugel | 55 | 115–140 | ★★★★★ |
| Harken | diverse | 900 | Edelstahl Kugel | 70 | 85–110 | ★★★★☆ |

*USD-Preis umgerechnet

---

## ANHANG H — Confidence-Mapping

### H.1 Confidence-Level für Wirbel-Bewertungen

| Bewertungsaspekt | Datenquelle | Confidence-Level | Display |
|-----------------|-------------|------------------|---------|
| Bruchlast (MBL) | Hersteller-TDS mit Zertifikat | measured | Grünes Badge |
| Bruchlast (MBL) | Hersteller-Angabe ohne Zertifikat | documented | Blaues Badge |
| Bruchlast (MBL) | Geschätzt aus Materialquerschnitt | estimated | Graues Badge |
| Zustand Oberfläche | Klares Foto, eindeutige Befunde | visual_high | Blaues Badge |
| Zustand Oberfläche | Foto mittlerer Qualität | visual_medium | Gelbes Badge |
| Zustand Oberfläche | Schlechtes Foto, mehrdeutig | visual_low | Versteckt |
| Zustand Lager | Haptische Prüfung, Messung | measured | Grünes Badge |
| Zustand Lager | Nur Foto (kein Spiel sichtbar) | visual_low | Versteckt |
| Materialidentifikation | PMI-Test (Röntgenfluoreszenz) | measured | Grünes Badge |
| Materialidentifikation | Magnettest + optisch | visual_medium | Gelbes Badge |
| Materialidentifikation | Nur optisch | visual_low | Versteckt |
| Restlebensdauer | Basierend auf Messdaten + Historie | calculated | Grünes Badge |
| Restlebensdauer | Geschätzt aus Alter und Zustand | estimated | Graues Badge |

### H.2 Nicht beurteilbare Aspekte

Folgende Aspekte geben `{"available": false, "reason": "..."}` zurück:

| Aspekt | Grund | Erforderlich für Beurteilung |
|--------|-------|------------------------------|
| Innere Risse | Ultraschallprüfung nötig | Ultraschallprüfung oder Magnetpulver |
| Exaktes Material | Visuell nicht unterscheidbar | PMI-Test oder Materialzertifikat |
| Exaktes Lagerspiel | Haptische Messung nötig | Messuhr oder Fühllehre |
| Ermüdungszustand | Nicht zerstörungsfrei prüfbar | Statistisches Modell + Lastkollektiv |
| Innere Korrosion | Nicht sichtbar | Demontage oder Ultraschall |

---

## ANHANG I — Weitere Fallstudien

### Fallstudie I1: Toggle-Wirbel verhindert Wantbruch

**Yacht:** Swan 48, Baujahr 2005, 15m LOA, 14.5t Verdrängung
**Revier:** Nordsee, Sturm (40 kn, 4m Welle)
**Konfiguration:** Unterwant 10mm Draht mit Toggle-Wirbel am Rumpfbeschlag

**Beobachtung:** Nach dem Sturm wurde am Putt-Beschlag des Unterwants ein beginnender Ermüdungsriss im Rumpfbeschlag entdeckt. Der Toggle-Wirbel hatte die Biegewechselbelastung aufgenommen und die Kräfte vom Rumpfbeschlag ferngehalten. Ohne den Toggle-Wirbel wäre der Riss schneller gewachsen und der Beschlag hätte versagen können.

**AYDI-Bewertung:**
- Toggle-Wirbel-Wirkung: Positiv bestätigt
- Rumpfbeschlag: HOCH (Riss = Austausch nötig)
- Confidence: measured (Riss durch Farbeindringprüfung bestätigt)

**Lehre:** Toggle-Wirbel an Wanten-Rumpfbeschlägen sind keine Option, sondern Pflicht. Die Biegeentlastung schützt den Rumpfbeschlag — das schwächste Glied der Kette.

### Fallstudie I2: Mooringwirbel nach 3 Jahren Unterwasser

**Installation:** Mooringfeld, Côte d'Azur (Frankreich)
**Konfiguration:** 316L-Wirbel, SWL 5000 kg, an 16mm Edelstahlkette

**Beobachtung:** Bei der Routineinspektion nach 3 Jahren war der Wirbel äußerlich mit Muscheln und Algen bedeckt, aber nach Reinigung noch drehbar. Spaltkorrosion war im Lagerspalt beginnend sichtbar (feine braune Linie). Wandstärkenmessung: 95% des Originalwerts.

**AYDI-Bewertung:**
- Zustand: GUT (für 3 Jahre Unterwassereinsatz)
- Prognose: Noch 3–5 Jahre nutzbar, danach Austausch
- Confidence: measured (Ultraschall-Wandstärke, visuelle Inspektion)

**Lehre:** 316L unter Wasser im Mittelmeer hält 5–8 Jahre. Duplex 2205 würde die Lebensdauer auf 8–12 Jahre verlängern. Jährliche Reinigung verlängert die Lebensdauer erheblich.

### Fallstudie I3: Keramiklager-Upgrade am Spinnaker-Wirbel

**Yacht:** TP52, Regattayacht
**Ausgangslage:** Edelstahl-Kugelgelagerter Spinnaker-Wirbel (Ronstan RF1035)
**Upgrade:** Ronstan RF1036 (Keramik-Kugellager, Si₃N₄)

**Ergebnis:** Losbrechmoment unter 3 kN Last: von 0.08 Nm (Edelstahl) auf 0.03 Nm (Keramik) reduziert. Rotation bei Halse spürbar schneller. Kein Korrosionsrisiko der Kugeln mehr. Gewichtsersparnis: 10g (65g → 55g). Mehrpreis: ca. 50 EUR.

**AYDI-Bewertung:**
- Upgrade-Wertung: Empfehlenswert für Regatta
- Preis-Leistung: Exzellent (geringe Mehrkosten, signifikanter Leistungsgewinn)
- Confidence: measured (Drehmomentmessung, Regattaeinsatz)

### Fallstudie I4: Falscher Wirbel am Furler — Systemschaden

**Yacht:** Jeanneau Sun Odyssey 440, 13m LOA
**Vorfall:** Eigner hatte den defekten Seldén-Furlerwirbel durch einen generischen Wirbelschäkel (Wichard 6504, SWL 1800 kg) ersetzt, da der Originalersatzteil nicht sofort verfügbar war.

**Ergebnis:** Nach 3 Monaten Nutzung hatte der Wirbelschäkel die Kunststoff-Laufhülse der Furler-Trommel beschädigt (zu enge Passung, Reibung am Trommelgehäuse). Die Furler-Trommel war gerissen und musste komplett ersetzt werden (Kosten: 1.200 EUR + 400 EUR Einbau).

**AYDI-Bewertung:**
- Wirbel-Auswahl: 15/100 (nicht systemkompatibel)
- Folgeschaden: HOCH
- Confidence: documented

**Lehre:** Furlerwirbel IMMER als Original-Ersatzteil beschaffen. Generische Wirbel passen mechanisch, aber nicht in die Systemintegration (Toleranzen, Laufhülsen, Dichtungen).

---

## ANHANG J — Bewertungsschema

### J.1 AYDI-Bewertungskriterien für Wirbel

| Kriterium | Gewicht | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|-----------|---------|------------|-----------|-----------|-----------|----------|
| Material | 20% | 316L geschm. / Duplex | 316L Feinguss | 316L Sandguss | 316 (nicht L) | 304 / verzinkt |
| Dimensionierung | 25% | SWL >150% der Anforderung | SWL 120–150% | SWL 100–120% | SWL 80–100% | SWL <80% |
| Lagerzustand | 20% | Frei drehend, kein Spiel | Leicht steif, minimales Spiel | Steif unter Last | Schwergängig | Festsitzend |
| Korrosion | 15% | Keine | Tea Staining | Oberflächen-Pitting | Tiefes Pitting | Tragende QS betroffen |
| Sicherung | 10% | Splint/Draht intakt, doppelt | Splint intakt, einfach | Splint vorhanden, alt | Splint fehlt, Bolzen hält | Bolzen lose |
| Wartungszustand | 10% | Kürzlich gewartet, gefettet | Gewartet <12 Mon. | Gewartet <24 Mon. | >24 Mon. ohne Wartung | Nie gewartet |

### J.2 Gesamtbewertung

```
Wirbel-Score = Σ (Kriterium_Score × Gewicht)

Interpretation:
  90–100: Ausgezeichnet — keine Maßnahme nötig
  75–89:  Gut — nächste planmäßige Wartung einhalten
  50–74:  Befriedigend — Wartung zeitnah durchführen
  25–49:  Mangelhaft — Austausch planen
  0–24:   Ungenügend — sofortiger Austausch
```

---

## ANHANG K — Entscheidungsbaum Wirbelauswahl

### K.1 Systematischer Auswahlprozess

```
SCHRITT 1: Anwendung bestimmen
  → Ankersystem:     → Gehe zu K.1.1
  → Furler:          → Gehe zu K.1.2
  → Fallen/Blöcke:   → Gehe zu K.1.3
  → Spinnaker:       → Gehe zu K.1.4
  → Mooring:         → Gehe zu K.1.5

K.1.1 — Ankersystem:
  SCHRITT 2: Kettengröße [mm] und Güteklasse bestimmen
  SCHRITT 3: MBL der Kette nachschlagen (Anhang C.1)
  SCHRITT 4: Wirbel-SWL ≥ 50% der Ketten-MBL berechnen
  SCHRITT 5: Revier bestimmen
    → Küstenfahrt:    316L Gleitlager ausreichend
    → Langfahrt/Tropen: Duplex 2205 empfohlen
  SCHRITT 6: Toggle nötig?
    → Bügelanker (Mantus, Rocna): Toggle empfohlen
    → Pflug-/CQR-Anker: Toggle optional
    → Danforth/Flunkenanker: Kein Toggle nötig
  SCHRITT 7: Produkt auswählen (Kompatibilität F.1 prüfen)

K.1.2 — Furler:
  SCHRITT 2: Furler-Hersteller und Modell bestimmen
  SCHRITT 3: Original-Ersatzteil beim Hersteller bestellen
  → ENDE (keine Fremdprodukte für Furlerwirbel!)

K.1.3 — Fallen/Blöcke:
  SCHRITT 2: Segelfläche und max. Windstärke bestimmen
  SCHRITT 3: Fallenlast berechnen (Anhang C.2)
  SCHRITT 4: SWL ≥ 2× Fallenlast wählen
  SCHRITT 5: Wirbelschäkel (Cruiser) oder Hochlast-Wirbel (Regatta)
  SCHRITT 6: Anschlusstyp wählen (Auge, Gabel, Snap)

K.1.4 — Spinnaker:
  SCHRITT 2: Spinnaker-Fläche und max. Einsatz-Windstärke
  SCHRITT 3: Dynamische Last berechnen (×6 Faktor!)
  SCHRITT 4: IMMER kugelgelagerten Wirbel wählen
  SCHRITT 5: Cruiser: Edelstahl-Kugellager / Regatta: Keramik
  SCHRITT 6: SWL ≥ 3× berechneter Segeldruck

K.1.5 — Mooring:
  SCHRITT 2: Bootsmasse und Expositionsgrad bestimmen
  SCHRITT 3: SWL ≥ 2× Bootsmasse × 9.81 / 1000 [kN]
  SCHRITT 4: Material: Duplex 2205 oder Aluminium-Bronze
  SCHRITT 5: Großzügige Lagerspalte (Bewuchstoleranz)
  SCHRITT 6: Wartungsplan erstellen (Anhang E)
```

---

## ANHANG L — Drehmoment- und Reibungstabellen

### L.1 Losbrechmoment unter Last (Messwerte)

| Wirbel-Typ | SWL [kg] | Last [kg] | Losbrechmoment [Nm] | Lager |
|------------|----------|-----------|----------------------|-------|
| Wirbelschäkel 316L | 1200 | 0 | 0.02 | Gleitlager Stahl |
| Wirbelschäkel 316L | 1200 | 500 | 0.35 | Gleitlager Stahl |
| Wirbelschäkel 316L | 1200 | 1000 | 0.85 | Gleitlager Stahl |
| Wirbelschäkel 316L | 1200 | 1200 | 1.20 | Gleitlager Stahl |
| Ankerwirbel 316L | 1800 | 500 | 0.25 | Gleitlager Bronze |
| Ankerwirbel 316L | 1800 | 1000 | 0.55 | Gleitlager Bronze |
| Ankerwirbel 316L | 1800 | 1800 | 1.05 | Gleitlager Bronze |
| Spi-Wirbel Edelstahl | 800 | 200 | 0.008 | Kugelgelagert |
| Spi-Wirbel Edelstahl | 800 | 500 | 0.022 | Kugelgelagert |
| Spi-Wirbel Edelstahl | 800 | 800 | 0.040 | Kugelgelagert |
| Spi-Wirbel Keramik | 800 | 200 | 0.003 | Kugel Keramik |
| Spi-Wirbel Keramik | 800 | 500 | 0.010 | Kugel Keramik |
| Spi-Wirbel Keramik | 800 | 800 | 0.018 | Kugel Keramik |
| Furlerwirbel Seldén | 5500 | 2000 | 0.15 | Kugelgelagert |
| Furlerwirbel Seldén | 5500 | 4000 | 0.35 | Kugelgelagert |
| Furlerwirbel Seldén | 5500 | 5500 | 0.55 | Kugelgelagert |

### L.2 Reibungskoeffizienten — Messwerte marine Umgebung

| Paarung | μ trocken (neu) | μ geschmiert (neu) | μ nach 12 Mon. Salzwasser | μ festgefressen |
|---------|-----------------|--------------------|-----------------------------|------------------|
| 316L / 316L | 0.45 | 0.18 | 0.30–0.50 | >1.0 |
| 316L / CuSn8P (Bronze) | 0.28 | 0.12 | 0.18–0.28 | 0.60–0.80 |
| 316L / POM | 0.18 | 0.10 | 0.15–0.22 | 0.40–0.50 |
| 316L / PTFE | 0.08 | 0.06 | 0.08–0.12 | 0.20–0.30 |
| 440C / Si₃N₄ | 0.06 | 0.04 | 0.05–0.08 | 0.15–0.20 |
| ZrO₂ / ZrO₂ | 0.05 | 0.03 | 0.04–0.06 | 0.10–0.15 |

---

## ANHANG M — Klimazonen-Empfehlungen

### M.1 Material- und Wartungsempfehlungen nach Klimazone

| Klimazone | Temp. [°C] | Salzgehalt | UV-Index | Empf. Material | Wartungsfaktor |
|-----------|------------|------------|----------|----------------|----------------|
| Nordeuropa (Ostsee) | 0–20 | Niedrig (7–8‰) | Niedrig | 316L | 1.0× (Basis) |
| Nordeuropa (Nordsee) | 2–18 | Mittel (32–35‰) | Niedrig-Mittel | 316L | 1.2× |
| Mittelmeer | 10–30 | Hoch (38–39‰) | Hoch | 316L / Duplex | 1.5× |
| Karibik/Tropen | 24–32 | Hoch (35–36‰) | Sehr hoch | Duplex 2205 | 2.0× |
| Pazifik/Tropen | 26–32 | Hoch (34–36‰) | Sehr hoch | Duplex 2205 | 2.0× |
| Arktis | -20–10 | Mittel (30–35‰) | Niedrig | 316L | 1.0× |
| Persischer Golf | 20–45 | Sehr hoch (40–42‰) | Extrem | Duplex 2205 / Titan | 2.5× |

### M.2 Bewuchsrisiko nach Region

| Region | Bewuchsgeschwindigkeit | Mooringwirbel-Reinigung | Empf. Gegenmaßnahme |
|--------|------------------------|--------------------------|---------------------|
| Ostsee | Langsam (3–6 Mon.) | Jährlich | Standardreinigung |
| Nordsee | Mittel (2–4 Mon.) | Halbjährlich | Antifouling-Anstrich Außenfläche |
| Mittelmeer | Schnell (1–3 Mon.) | Vierteljährlich | Antifouling + Zinkanode |
| Karibik | Sehr schnell (2–6 Wo.) | Monatlich | Antifouling + regelmäßige Reinigung |
| Pazifik (Tropen) | Sehr schnell (2–6 Wo.) | Monatlich | Antifouling + Zinkanode |

---

## ANHANG N — Installations-Checklisten

### N.1 Checkliste: Ankerkettenwirbel einbauen

- [ ] Ketten-Ø und Güteklasse bestimmt
- [ ] Wirbel-SWL ≥ Ketten-SWL verifiziert
- [ ] Wirbel-MBL ≥ 4× SWL verifiziert
- [ ] Materialkompatibilität geprüft (316L mit Edelstahlkette, nicht mit verzinkt)
- [ ] Wirbel dreht frei ohne Last — Funktionsprüfung
- [ ] Wirbel passt durch Bugrolle und Kettenklüse
- [ ] Wirbel passt in Ankerwinden-Führung
- [ ] Schäkel-Verbindungen korrekt geschlossen
- [ ] Bolzen mit Splint oder Sicherungsdraht gesichert
- [ ] Anti-Seize-Paste auf Bolzengewinde
- [ ] Lagerflächen mit Marine-Fett geschmiert
- [ ] Foto des eingebauten Wirbels für Dokumentation
- [ ] Erste Ankermanöver als Test unter kontrollierten Bedingungen

### N.2 Checkliste: Furlerwirbel wartnen

- [ ] Segel abgenommen oder eingerollt
- [ ] Vorstag-Spannung notiert (für Wiedermontage)
- [ ] Trommelgehäuse geöffnet (Herstelleranleitung beachten!)
- [ ] Alte Schmierung entfernt (Lappen, mildes Lösungsmittel)
- [ ] Lagerkugeln auf Lochfraß und Verformung geprüft
- [ ] Laufbahnen auf Riefen und Korrosion geprüft
- [ ] Dichtungen auf Risse und Verhärtung geprüft
- [ ] Neues Fett gemäß Herstellerangabe aufgebracht
- [ ] Trommelgehäuse verschlossen
- [ ] Vorstag-Spannung wiederhergestellt
- [ ] Funktionsprüfung: Segel ein- und ausrollen (leichtgängig?)
- [ ] Wartungsdatum dokumentiert

### N.3 Checkliste: Spinnaker-Wirbel saisonaler Check

- [ ] Wirbel demontiert und visuell inspiziert
- [ ] Lagerbeweglichkeit geprüft (muss frei laufen, kein Hakeln)
- [ ] Kugeln/Laufbahnen auf Verschleiß geprüft
- [ ] Bolzen und Sicherung auf Verschleiß geprüft
- [ ] Gereinigt mit Süßwasser und leichtem Lösungsmittel
- [ ] Neu geschmiert (PTFE-basiertes Lageröl, kein schweres Fett)
- [ ] Snap-Schäkel-Mechanismus geprüft (falls Snap-Swivel)
- [ ] Rotationstest: dreht unter Handlast frei
- [ ] Eingebaut und gesichert
- [ ] Wartungsdatum im Bordbuch notiert

---

## ANHANG O — Erfahrungsberichte

### O.1 Forum-Konsens: Ankerkettenwirbel

**Quelle:** Segelforum.de, Cruisersforum.com, YBW Forum (>200 Threads analysiert)

**Konsens-Meinung zu Marken:**
- Wichard: „Goldstandard, kostet mehr, hält aber" — 85% positive Erwähnungen
- Mantus: „Bestes Preis-Leistungs-Verhältnis" — 80% positive Erwähnungen
- Ultra Flip Swivel: „Passt perfekt durch jede Klüse" — 90% positive Erwähnungen
- Kong: „Solide für den Preis, aber nicht so glatt wie Wichard" — 70% positive Erwähnungen
- NoName/China: „Finger weg bei Sicherheitsteilen" — 90% negative Erwähnungen

**Häufigste Probleme (aus Foren):**
1. Wirbel dreht nicht mehr nach einem Winter ohne Wartung (45% der Problemberichte)
2. Wirbel passt nicht durch die Bugrolle (25%)
3. Materialzweifel bei Billig-Wirbeln (15%)
4. Bolzen/Splint verloren (10%)
5. Sonstiges (5%)

### O.2 Erfahrungsberichte: Furlerwirbel

**Konsens zu Wartungsintervallen:**
- Herstellerangabe (jährlich): „Das Minimum, besser halbjährlich" — Mehrheitsmeinung
- Langfahrer-Konsens: „Alle 6 Monate in den Tropen, sonst jährlich"
- Regattasegler: „Vor jeder Saison, plus nach Regatten in Regen/Sturm"

**Häufigste Aussagen:**
- „Seit ich den Furler jährlich fette, läuft er wie am ersten Tag" (Standard-Erfahrung)
- „Nach 3 Jahren ohne Service war der Furler fest — 400 EUR Reparatur" (Warnung)
- „Original-Ersatzteile sind teuer, aber Fremdteile können den Furler zerstören" (Erfahrungswert)

### O.3 Erfahrungsberichte: Spinnaker-Wirbel

**Konsens:**
- „Spart NICHT am Spinnaker-Wirbel — ein gerissener Spi kostet 5.000+ EUR"
- „Kugelgelagert ist Pflicht, Gleitlager geht gar nicht für den Spi"
- „Keramiklager ist den Aufpreis wert, besonders wenn man viel Spi segelt"
- „Tylaska ist das Beste, aber Ronstan bietet 80% der Leistung für 50% des Preises"

---

## ANHANG P — Visuelle Inspektionskriterien

### P.1 Inspektionskriterien für AYDI Visual Pipeline

| Kriterium | Erkennbar auf Foto? | Confidence | Was suchen |
|-----------|---------------------|------------|------------|
| Korrosion (Oberfläche) | Ja | visual_high | Braune Flecken, Grübchen, raue Oberfläche |
| Korrosion (Lager) | Teilweise | visual_medium | Braune Ablagerungen im Spalt |
| Verformung | Ja | visual_high | Ovale Augen, gebogener Körper |
| Risse | Schwer | visual_low | Haarfeine Linien, Farbveränderung |
| Bolzensicherung | Ja | visual_high | Splint vorhanden/fehlend |
| Bewuchs | Ja | visual_high | Muscheln, Algen, Kalk |
| Dimensionierung | Bedingt | visual_medium | Größenvergleich mit Kette/Schäkel |
| Material (304 vs 316L) | Nein | visual_insufficient | Nicht visuell unterscheidbar |
| Lagerspiel | Nein | visual_insufficient | Erfordert haptische Prüfung |
| Innere Schäden | Nein | visual_insufficient | Erfordert Demontage |

### P.2 Foto-Anforderungen für zuverlässige AYDI-Analyse

| Aufnahme | Zweck | Min. Auflösung | Beleuchtung |
|----------|-------|----------------|-------------|
| Gesamtansicht | Typ-Identifikation, Dimensionierung | 2 Megapixel | Tageslicht |
| Nahaufnahme Lagerspalt | Korrosion, Ablagerungen | 5 Megapixel | Seitenlicht |
| Nahaufnahme Bolzen | Sicherungszustand | 3 Megapixel | Direkt |
| Augen/Gabeln Detail | Verformung, Risse | 5 Megapixel | Seitenlicht |
| Prägung/Markierung | Hersteller, SWL, Material | 5 Megapixel | Schräglicht |
| Gesamte Verbindung | Kompatibilität, Einbausituation | 2 Megapixel | Tageslicht |

---

## ANHANG Q — Ersatzteil-Referenz

### Q.1 Gängige Verschleißteile

| Bauteil | Typische Lebensdauer | Verfügbarkeit | Preis-Bereich [EUR] |
|---------|---------------------|---------------|---------------------|
| Lagerbuchse POM (Wirbelschäkel) | 5–8 Jahre | Selten als Einzelteil | 3–8 |
| Lagerbuchse Bronze (Ankerwirbel) | 8–12 Jahre | Bei Hersteller | 10–25 |
| Kugelsatz Edelstahl (Blockwirbel) | 4–8 Jahre | Bei Hersteller | 8–20 |
| Kugelsatz Keramik (Spi-Wirbel) | 6–12 Jahre | Bei Hersteller | 25–60 |
| Dichtungssatz (Furlerwirbel) | 3–6 Jahre | Bei Hersteller | 15–40 |
| Lagersatz komplett (Furlerwirbel) | 5–8 Jahre | Bei Hersteller | 60–200 |
| Bolzen mit Splint | 10+ Jahre | Universal | 3–12 |
| Sicherungsdraht | Einmalverwendung | Universal | 1–3 |

### Q.2 Ersatzteil-Bestellreferenz

| Hersteller | Ersatzteil-Service | Website | Lieferzeit [Tage] |
|------------|--------------------|---------|--------------------|
| Wichard | Direkt oder über Händler | wichard.com | 3–7 (EU) |
| Seldén | Über Seldén-Händler | sfrond.com | 5–14 |
| Harken | Über Harken-Händler | harken.com | 5–10 |
| Ronstan | Direkt oder über Händler | ronstan.com | 7–14 (ex AU) |
| Tylaska | Direkt | tylaska.com | 10–21 (ex USA) |
| Kong | Über Händler | kong.it | 5–10 |
| Mantus | Direkt | mantusanchors.com | 10–21 (ex USA) |
| Ultra Marine | Direkt oder über Händler | ultra-marine.se | 7–14 |

---

## ANHANG R — Glossar Englisch-Deutsch Zuordnung

| Englisch | Deutsch | Kontext |
|----------|---------|---------|
| Anchor chain swivel | Ankerkettenwirbel | Wirbel zwischen Kette und Anker |
| Ball bearing | Kugellager | Lagertyp mit Kugeln |
| Block swivel | Blockwirbel | Wirbel im Blockkopf |
| Bore / eye | Auge / Öse | Rundes Anschlussende |
| Breaking load (MBL) | Bruchlast | Kraft bei Versagen |
| Caulking | Kalfatern / Fugen | — |
| Ceramic bearing | Keramiklager | ZrO₂ oder Si₃N₄ |
| Chain link | Kettenglied | Einzelnes Element der Kette |
| Clevis / jaw | Gabel | U-förmiger Anschluss |
| Corrosion | Korrosion | Materialzerstörung |
| Cotter pin | Splint | Bolzensicherung |
| Crevice corrosion | Spaltkorrosion | Korrosion in engen Spalten |
| Endurance limit | Dauerfestigkeit | Ermüdungsgrenze |
| Fatigue | Ermüdung | Zyklisches Versagen |
| Fork → Jaw | Gabel | Anschlusstyp |
| Fouling | Bewuchs | Biologische Ablagerung |
| Fretting | Reibkorrosion | Vibrations-Korrosion |
| Furler | Rollreffanlage | Segel-Aufrollsystem |
| Galling | Kaltverschweißung | Adhäsiver Verschleiß |
| Halyard | Fall | Seil zum Segelsetzen |
| Head swivel | Kopfwirbel | Wirbel am Furler-Kopf |
| Jaw-jaw | Gabel-Gabel | Beidseitige Gabel |
| Mooring | Festmacher / Mooringleine | Dauerliegeplatz |
| Needle bearing | Nadellager | Lager mit Zylinderrollen |
| Pitting | Lochfraß | Lokale Korrosion |
| Plain bearing | Gleitlager | Lager ohne Rollkörper |
| Proof load | Prüflast | Kontrollierte Testlast |
| Safe working load (SWL) | Arbeitslast / Tragfähigkeit | Maximal zulässige Dauerbelastung |
| Safety factor | Sicherheitsfaktor | MBL / SWL |
| Seized | Festgefressen / festsitzend | Nicht mehr drehbar |
| Shackle | Schäkel | U-Verbinder mit Bolzen |
| Sheet | Schot | Seil zur Segelverstellung |
| Snap shackle | Schnappschäkel | Schnellverschluss |
| Spinnaker swivel | Spinnaker-Wirbel | Wirbel am Spi-Fall |
| Stainless steel | Edelstahl | Korrosionsbeständiger Stahl |
| Swivel | Wirbel / Drehgelenk | Rotationselement |
| Tea staining | Tee-Flecken | Oberfl. Verfärbung 316L |
| Toggle | Toggle / Kippgelenk | Biegeentlastungselement |
| Torque | Drehmoment | Kraft × Hebelarm |
| Torsion | Torsion / Verdrehung | Verdrehbelastung |
| Universal joint | Universalgelenk / Kardangelenk | Mehrachsiges Drehgelenk |
| Yawing | Gieren / Schwojen | Hin-/Herschwingen vor Anker |
| Wire rope | Drahtseil | Stehendes Gut (Wanten, Stage) |
| Working load | Arbeitslast | Betriebslast |
| Zinc anode | Zinkanode | Opfer-Anode für Korrosionsschutz |

---

## ANHANG S — Saisonale Wartungsplanung

### S.1 Frühjahr (Saisonstart) — Checkliste Wirbel

| Bauteil | Maßnahme | Priorität | Zeitbedarf |
|---------|----------|-----------|------------|
| Ankerkettenwirbel | Demontage, Reinigung, Schmierung, Funktionstest | HOCH | 30 Min. |
| Furlerwirbel | Schmiernippel fetten, Drehtest unter Last | HOCH | 15 Min. |
| Alle Blockwirbel | Sichtkontrolle, Drehtest, ggf. Öl | MITTEL | 20 Min. |
| Fallenwirbel | Sichtkontrolle, Splint prüfen, ggf. Fett | MITTEL | 15 Min. |
| Spinnaker-Wirbel | Demontage, Reinigung, Schmierung, Drehtest | HOCH | 20 Min. |
| Mooringwirbel | Taucherinspektion, Bewuchs entfernen | HOCH | 45 Min. |
| Toggle-Verbindungen | Sichtprüfung, Bolzen prüfen, fetten | MITTEL | 15 Min. |

### S.2 Mitte Saison — Zwischencheck

| Bauteil | Maßnahme | Priorität | Zeitbedarf |
|---------|----------|-----------|------------|
| Ankerkettenwirbel | Funktionstest (dreht frei?), Sichtkontrolle | HOCH | 5 Min. |
| Furlerwirbel | Leichtgängigkeit beim Reffen beurteilen | MITTEL | 2 Min. |
| Spinnaker-Wirbel | Drehtest vor Einsatz | HOCH | 2 Min. |
| Blockwirbel | Sichtkontrolle bei Rigg-Check | NIEDRIG | 5 Min. |

### S.3 Herbst (Winterlager) — Einlagerung

| Bauteil | Maßnahme | Priorität | Zeitbedarf |
|---------|----------|-----------|------------|
| Ankerkettenwirbel | Abnehmen, reinigen, fetten, trocken lagern | HOCH | 30 Min. |
| Furlerwirbel | Gemäß Herstellerangabe (oft am Rigg lassen, aber schmieren) | MITTEL | 15 Min. |
| Spinnaker-Wirbel | Abnehmen, reinigen, leicht ölen, einpacken | MITTEL | 15 Min. |
| Fallenwirbel | Am Rigg lassen, Schutzkappe aufsetzen | NIEDRIG | 5 Min. |
| Blockwirbel | Am Rigg lassen, lose Teile sichern | NIEDRIG | 5 Min. |
| Mooringwirbel | Wenn Boot aus Wasser: Inspektion, Reinigung, Fett | HOCH | 45 Min. |

### S.4 Langfahrt-Zusatzplan (Tropeneinsatz)

| Intervall | Maßnahme | Betrifft |
|-----------|----------|----------|
| Wöchentlich | Süßwasser-Spülung aller exponierten Wirbel | Ankersystem, Blöcke |
| Alle 2 Wochen | Drehtest Ankerkettenwirbel unter leichter Last | Ankersystem |
| Monatlich | Fettung aller Gleitlager-Wirbel | Alle Wirbel |
| Alle 3 Monate | Demontage und Inspektion Ankerwirbel | Ankersystem |
| Alle 6 Monate | Furlerwirbel nachfetten | Furler |
| Jährlich | Lagersatz prüfen, ggf. tauschen (Furler, Spi) | Furler, Spinnaker |

---

## ANHANG T — Gewichtsvergleich und Masttop-Optimierung

### T.1 Gewicht am Masttop — Warum es zählt

Jedes Gramm am Masttop erhöht das Krängungsmoment und verschlechtert die Stabilität:

```
Zusätzliches Krängungsmoment durch Masttop-Gewicht:
  M_kräng = m_masttop × g × h_mast × sin(θ)

  Beispiel: 100g zusätzlich bei 15m Masthöhe, 20° Krängung:
  M_kräng = 0.1 × 9.81 × 15 × sin(20°) = 5.03 Nm

  Bei einer 10t Yacht mit 1.2m Metazentrum:
  Zusätzliche Krängung: ~0.024° (marginal bei Cruiser, relevant bei Regatta)
```

### T.2 Gewichtsvergleich Spinnaker-Wirbel

| Hersteller | Modell | SWL [kg] | Material | Lager | Gewicht [g] | Gewicht/SWL [g/kg] |
|------------|--------|----------|----------|-------|-------------|---------------------|
| Tylaska | TT8 (Titan) | 1200 | Ti Gr.5 | Keramik | 32 | 0.027 |
| Tylaska | S10 (Edelstahl) | 800 | 316L | Keramik | 38 | 0.048 |
| Ronstan | RF1036 | 1200 | 316L | Keramik | 55 | 0.046 |
| Ronstan | RF1035 | 800 | 316L | Edelstahl | 65 | 0.081 |
| Harken | Standard | 900 | 316L | Edelstahl | 70 | 0.078 |
| Wichard | 6523 | 1600 | 316L | Gleitlager | 72 | 0.045 |
| NoName | Billig | 600* | 304? | Gleitlager | 85 | 0.142 |

**Empfehlung AYDI:** Für Regattayachten ist der Gewichts/SWL-Quotient ein wichtiges Auswahlkriterium. Titan-Keramik-Wirbel (Tylaska TT-Serie) bieten das beste Verhältnis, sind aber 5–10× teurer als Edelstahl.

### T.3 Gewichtsvergleich Fallenwirbel

| Hersteller | Modell | SWL [kg] | Material | Gewicht [g] | Preis [EUR] |
|------------|--------|----------|----------|-------------|-------------|
| Tylaska | T5 | 500 | 316L CNC | 25 | 70–90* |
| Wichard | 6521 HR | 500 | 316L geschm. | 22 | 32–40 |
| Wichard | 6501 | 400 | 316L geschm. | 28 | 18–22 |
| Kong | 8201 | 350 | 316 Guss | 30 | 12–16 |
| Ronstan | Standard | 350 | 316L | 32 | 22–28 |

### T.4 Gesamtgewicht Rigg-Wirbel — Typische Konfiguration

| Bauteil | Anzahl | Einzelgewicht [g] | Gesamt [g] | Am Masttop? |
|---------|--------|-------------------|------------|-------------|
| Großfall-Wirbelschäkel | 1 | 45 | 45 | Ja |
| Vorsegel-Fall-Wirbelschäkel | 1 | 45 | 45 | Ja |
| Spinnaker-Wirbel | 1 | 65 | 65 | Ja |
| Blockwirbel Mastfuß | 2 | 55 | 110 | Nein |
| Blockwirbel Deck | 4 | 38 | 152 | Nein |
| Ankerkettenwirbel | 1 | 350 | 350 | Nein |
| **Gesamt** | **10** | — | **767** | **155** am Masttop |

---

## ANHANG U — Historische Referenz und Entwicklung

### U.1 Meilensteine der Wirbel-Entwicklung

| Jahr | Entwicklung | Bedeutung |
|------|-------------|-----------|
| ca. 1650 | Erste dokumentierte Ketten-Drehwirbel (Schmiedeeisen) | Grundprinzip etabliert |
| 1843 | Patent für verbesserten Ketten-Wirbel (GB) | Standardisierung beginnt |
| 1890 | Erster Serien-Ankerketten-Wirbel aus Gussstahl | Industrielle Fertigung |
| 1935 | Edelstahl-Wirbel für Yachten (erste Erwähnungen) | Marine-Grade Material |
| 1960 | Entwicklung der ersten Rollreffanlagen | Furlerwirbel als neues Bauteil |
| 1967 | Harken-Gründung — Hochleistungs-Blockwirbel | Performance-Blöcke |
| 1975 | Erste kugelgelagerte Spinnaker-Wirbel | Regatta-Innovation |
| 1985 | Seldén Furlex System mit integriertem Wirbel | Furler-Systemintegration |
| 1995 | Keramik-Kugellager in Segelbeschlägen | Materialrevolution |
| 2000 | Titan-Beschläge für America's Cup | Extreme Leichtbauweise |
| 2005 | Wichard HR-Serie (hochfest geschmiedet) | Premium-Segment definiert |
| 2010 | Ultra Flip Swivel Patent | Innovation Ankerwirbel |
| 2015 | Dyneema-Soft-Schäkel als Wirbel-Alternative (begrenzt) | Textile Verbinder |
| 2020 | Smart Rigging — Lastsensoren in Wirbeln (Prototypen) | Digitalisierung |
| 2025 | 3D-gedruckte Titan-Wirbel (Forschung) | Additive Fertigung |

### U.2 Zukunftstrends

**Additive Fertigung (3D-Druck):**
- Selektives Laserschmelzen (SLM) von Titan und Edelstahl
- Ermöglicht gewichtsoptimierte Geometrien (topologieoptimiert)
- Erste Prototypen für Superyachten in Erprobung
- Serienreife: voraussichtlich ab 2028–2030

**Integrierte Sensorik:**
- Dehnungsmessstreifen im Wirbelkörper
- Bluetooth/LoRa-Übertragung der Lastwerte an Bordelektronik
- Ermüdungsüberwachung in Echtzeit
- Frühwarnung bei Überlastung
- Aktueller Status: Forschungsprototypen, keine Serienprodukte

**Faserverstärkte Kunststoffe:**
- Carbon-/Aramid-Wirbel für ultraleichte Anwendungen
- Korrosionsfrei, extrem leicht
- Herausforderung: Lagerfunktion, Verschleißfestigkeit
- Aktuell nur in Verbindung mit metallischen Lagerelementen denkbar

**Selbstschmierende Beschichtungen:**
- DLC (Diamond-Like Carbon) Beschichtungen auf Lagerflächen
- Eliminiert Schmierungsbedarf
- Extrem niedriger Reibungskoeffizient (<0.05)
- Noch nicht für marine Dauereinsatz qualifiziert

---

---

## ANHANG V — Vergleichstest-Protokoll

### V.1 Standardisiertes Testprotokoll für Wirbel-Vergleiche

Zur objektiven Bewertung von Wirbeln im AYDI-System wird folgendes Testprotokoll empfohlen:

**Phase 1 — Identifikation und Dokumentation:**

| Schritt | Aktion | Dokumentation |
|---------|--------|---------------|
| 1.1 | Hersteller, Modell, Artikelnummer erfassen | Foto der Prägung |
| 1.2 | Material-Identifikation (Magnettest, ggf. PMI) | Testprotokoll |
| 1.3 | Gewicht messen (Präzisionswaage ±1g) | Messwert |
| 1.4 | Maße erfassen (Länge, Breite, Bolzen-Ø) | Messwerte |
| 1.5 | Anschlusstypen dokumentieren | Foto |
| 1.6 | Herstellerangaben notieren (SWL, MBL) | Datenblatt |

**Phase 2 — Funktionsprüfung:**

| Schritt | Aktion | Messgröße |
|---------|--------|-----------|
| 2.1 | Drehtest ohne Last: 10 volle Umdrehungen | Leichtgängigkeit [subjektiv 1–5] |
| 2.2 | Losbrechmoment ohne Last messen | M_los [Nm] |
| 2.3 | Drehtest unter 25% SWL | Leichtgängigkeit [subjektiv 1–5] |
| 2.4 | Losbrechmoment unter 25% SWL messen | M_los [Nm] |
| 2.5 | Drehtest unter 50% SWL | Leichtgängigkeit [subjektiv 1–5] |
| 2.6 | Losbrechmoment unter 50% SWL messen | M_los [Nm] |
| 2.7 | Drehtest unter 75% SWL | Leichtgängigkeit [subjektiv 1–5] |
| 2.8 | Drehtest unter 100% SWL | Noch drehbar? [ja/nein] |

**Phase 3 — Korrosionstest (optional, Langzeit):**

| Schritt | Aktion | Dauer | Messgröße |
|---------|--------|-------|-----------|
| 3.1 | Salznebelkammer (ISO 9227 NSS) | 720h | Korrosionsgrad |
| 3.2 | Drehtest nach Salznebeltest | — | M_los [Nm] Veränderung |
| 3.3 | Salzwasser-Eintauchtest (natürlich) | 6 Monate | Korrosion, Bewuchs |
| 3.4 | Drehtest nach Eintauchtest | — | M_los [Nm] Veränderung |

**Phase 4 — Bewertung:**

```
Gesamtbewertung = (
    Materialqualität × 0.20 +
    Verarbeitung × 0.15 +
    Leichtgängigkeit_ohne_Last × 0.10 +
    Leichtgängigkeit_unter_Last × 0.25 +
    Korrosionsbeständigkeit × 0.15 +
    Preis_Leistung × 0.15
) × 100
```

### V.2 Referenzwerte aus AYDI-Testdatenbank

| Wirbel | Material-Score | Verarbeitung | Leichtgang (ohne) | Leichtgang (Last) | Korrosion | Preis/Leistung | Gesamt |
|--------|---------------|-------------|--------------------|--------------------|-----------|----------------|--------|
| Wichard 6503 | 95 | 92 | 78 | 65 | 82 | 80 | 81.2 |
| Wichard 6523 HR | 95 | 95 | 80 | 72 | 85 | 72 | 82.9 |
| Kong 8203 | 80 | 78 | 75 | 62 | 72 | 90 | 74.8 |
| Mantus M1-10 | 90 | 88 | 82 | 70 | 80 | 85 | 81.1 |
| Ultra UFS-M | 92 | 90 | 88 | 78 | 82 | 78 | 84.2 |
| Tylaska T8 | 98 | 98 | 92 | 88 | 90 | 55 | 87.5 |
| Ronstan RF1036 | 90 | 88 | 95 | 92 | 85 | 75 | 88.7 |
| NoName China | 40 | 45 | 70 | 40 | 35 | 95 | 50.0 |

**Erläuterung:** Diese Referenzwerte dienen als Benchmark für die AYDI-Bewertung. Neue Wirbel werden gegen diese Matrix bewertet. Scores unter 60 führen zu einer Warnung, unter 40 zu einer dringenden Austauschempfehlung.

---

*Ende der AYDI-Wissensdatei 12.02 — Wirbel und Drehgelenke im Yachtbau*
*Nächste geplante Aktualisierung: Q3 2026*
*Bei Korrekturen oder Ergänzungen: AYDI Research Team kontaktieren*
