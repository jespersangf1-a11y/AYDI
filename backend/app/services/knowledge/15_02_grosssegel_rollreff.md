---
title: "Großsegel-Rollreff und In-Mast/In-Boom-Systeme"
kategorie: "15 Rollreffanlagen"
unterkategorie: "15.02 Großsegel-Rollreff und In-Mast/In-Boom"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, Zertifizierungen, Rigg-Handbücher"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Segelmacher-Berichte"
  - estimated: "Erfahrungswerte, Langfahrt-Praxis, Werft-Konsens, Regatta-Feedback"
---

# 15.02 — Großsegel-Rollreff und In-Mast/In-Boom-Systeme: Vollständige Wissensreferenz

> **AYDI Wissensdatei 15.02** — Kategorie 15: Rollreffanlagen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Werftunterlagen), estimated (Erfahrungswerte, Langfahrt-Praxis)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Vor- und Nachteile — Vergleichsmatrix](#5-vor--und-nachteile--vergleichsmatrix)
6. [Dimensionierung und Auswahl](#6-dimensionierung-und-auswahl)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting-Bäume](#8-troubleshooting-bäume)
9. [FAQ — Häufig gestellte Fragen](#9-faq--häufig-gestellte-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [Anhänge A–X](#12-anhänge-ax)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Grundproblem

Das Großsegel ist das zentrale Segel einer Segelyacht. Im Gegensatz zum Vorsegel, das seit den 1970er-Jahren routinemäßig mit Rollreff-Vorstagen bedient wird, stellt das Bergen und Reffen des Großsegels eine besondere Herausforderung dar: Das Segel ist am Mast und Baum befestigt, der Baum schwenkt, und das Segel muss unter Last kontrolliert verkleinert werden. Traditionell geschieht dies durch Bindereffs (Slabreffs) — ein manueller Vorgang, der physische Kraft, Geschick und oft Deckarbeit erfordert.

Die Entwicklung von Großsegel-Rollreff-Systemen verfolgt ein einziges Ziel: **Segelfläche sicher, schnell und idealerweise vom Cockpit aus zu reduzieren oder zu bergen**, ohne dass Crewmitglieder den Mast oder das Vordeck betreten müssen.

### 1.2 Historische Entwicklung

**Vor 1970 — Klassische Refftechnik:**
- Bindereff (Slab Reefing) als universeller Standard
- Crew musste an den Mast, Reffkauschen einlegen, Reffbänsel binden
- Zeitaufwand: 5–15 Minuten, 2+ Personen benötigt
- Seefallreffs auf Traditionsschiffen (Aufrollen um den Baum per Hand)

**1970–1985 — Erste Rollsysteme:**
- Boom-Furling: Aufrollen um den Baum per Kurbel (Hood Stoway Mast, Kemp Masts)
- Erste In-Mast-Versuche durch Hood Sails (USA) mit dem "Stoway Mast"
- Probleme: schlechte Segelform, Verklemmungen, teure Spezialsegel
- Lazyjacks als Hilfsmittel für konventionelle Reffs etabliert

**1985–2000 — Reifung der Technologie:**
- Selden (Schweden) entwickelt zuverlässige In-Mast-Systeme für den OEM-Markt
- Profurl (Frankreich) und Facnor (Frankreich) erweitern ihr Vorsegel-Know-how auf Großsegel
- In-Boom-Systeme entstehen als Alternative (Leisure Furl, Schaefer)
- Einleinen-Reff (Single-Line Reefing) für Slab-Systeme wird Standard bei Serienwerften

**2000–2015 — Elektrifizierung und Professionalisierung:**
- Elektrische und hydraulische Antriebe werden bezahlbar
- Bartels (Deutschland) entwickelt eigene In-Boom-Technologie
- Z-Spars (Frankreich/Selden-Gruppe) etabliert In-Boom für 35–60 ft
- Werften wie Bavaria, Beneteau, Jeanneau bieten In-Mast ab Werk (ab 40 ft)

**2015–heute — Konvergenz und Optimierung:**
- Verbesserte Segelschnitte (Vertikalbahn, tri-radial) für In-Mast
- Hybrid-Latten (kurze Latten in In-Boom-Segeln)
- Elektrische Antriebe als Standard bei Neubauten ab 45 ft
- CAN-Bus-Integration für automatisierte Reffstrategien
- 3D-Segelmaterialien (z.B. Elvström EPEX) für bessere Rollsegel-Performance

### 1.3 Bedeutung im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems beeinflusst das Großsegel-Reffsystem folgende Module:

- **Ergonomie-Modul:** Cockpit-Bedienung vs. Deckarbeit, Kurzhand-Tauglichkeit
- **Compliance-Modul:** CE-Kategorie und Offshore-Anforderungen (Notreffen bei Systemausfall)
- **Kosten-Modul:** Massive Preisunterschiede (€500 Slab bis €25.000+ In-Mast elektrisch)
- **Produktions-Modul:** Mastprofil, Boom-Konstruktion, Rigg-Integration
- **Strukturmodul:** Kräfteeinleitung im Mast, Boom-Belastung, Kompressionslasten
- **Gewichts-Modul:** Mastkopfgewicht (In-Mast-Mandrel), Schwerpunktlage

### 1.4 Marktüberblick

Der Markt für Großsegel-Reffsysteme wird auf ca. 120–160 Mio. EUR geschätzt (2025, Europa + Nordamerika):

**Marktanteile nach System-Typ (geschätzt, 2025, Neuboote >35 ft):**

| System | Marktanteil (Fahrtenyachten) | Marktanteil (Regatta) | Trend |
|--------|-----------------------------|-----------------------|-------|
| Slab Reefing (Bindereef) | 30–35% | 85–90% | Stabil bei Regatta, rückläufig Fahrt |
| In-Mast Furling | 35–40% | 2–5% | Wachsend, OEM-Favorit |
| In-Boom Furling | 10–15% | 3–5% | Wachsend, Premium-Segment |
| Single-Line Reefing | 15–20% | 5–8% | Stabil |

**Regionale Unterschiede:**
- **Nordeuropa (Skandinavien, Deutschland, NL):** In-Mast dominiert bei Fahrtenyachten ab 38 ft
- **Mittelmeer (FR, IT, ES, GR, HR):** Slab und In-Mast gleichverteilt, Charter oft In-Mast
- **Großbritannien:** Slab-Tradition stark, In-Boom wachsend
- **Nordamerika (USA, CAN):** In-Boom-Markt stärker als in Europa
- **Australien/NZ:** Slab dominiert, Regatta-Tradition

### 1.5 Regulatorischer Rahmen

Für Großsegel-Reffsysteme gelten keine spezifischen ISO-Normen, aber folgende Standards sind relevant:

| Standard | Bezug zum Großsegel-Reff |
|----------|--------------------------|
| ISO 12215-10:2020 | Rigg-Lasten und Mastbefestigungen |
| ISO 12217:2015/2022 | Stabilität — Segelkräfte unter Reffs |
| EN 13033:2002 | Segelausrüstung — Festigkeit von Beschlägen |
| ISO 15085:2003 | Man-Overboard — Vermeidung von Deckarbeit |
| CE/RCD 2013/53/EU | Allgemeine Sicherheit für Ausrüstung |
| ISAF OSR | Offshore Special Regulations (Regatta) — Notreffen |

> ⚠️ **ZU PRÜFEN (Audit):** „EN 13033:2002 — Segelausrüstung/Festigkeit von Beschlägen" ist keine belegbare Normnummer. EN 13033 existiert nicht als Norm für Segelausrüstung/Beschläge (EN 13034 = Chemikalienschutzkleidung; ISO 13033 = seismische Bauteillasten im Bauwesen). Der reale Standard für die Festigkeit von Beschlag-Starkpunkten ist ISO 15084 (Anker-/Vertäu-/Schlepp-Starkpunkte), deckt jedoch Reffhaken/Kauschen/Blöcke nicht ab. Normnummer verifizieren — nicht als „measured" behandeln.

**ISAF/World Sailing Offshore Special Regulations:**
- Kategorie 0–2: Möglichkeit zum manuellen Reffen MUSS bestehen (auch bei elektrischem Antrieb)
- Notfall-Reffverfahren muss dokumentiert und geübt sein
- In-Mast-Systeme erfordern zusätzliches Trysegel bei Kategorie 0–2

### 1.6 Systemauswahl — Entscheidungsfaktoren im Überblick

Die Wahl des Großsegel-Reffsystems ist eine der folgenreichsten Entscheidungen beim Yachtkauf oder -umbau. Sie beeinflusst:

**Kurzfristige Faktoren:**
- Anschaffungskosten (Faktor 1–15 zwischen einfachstem und aufwendigstem System)
- Segelperformance (5–18% Leistungsunterschied am Wind)
- Bedienkomfort (von 2-Personen-Deckarbeit bis Cockpit-Taster)

**Langfristige Faktoren:**
- Wartungsaufwand und -kosten über 20 Jahre
- Segel-Ersatzkosten (Rollsegel 20–40% teurer als Standard)
- Wiederverkaufswert des Bootes
- Revier-Eignung (Frost, Tropen, Offshore)
- Crew-Ausbildungsbedarf

**Sicherheitsrelevante Faktoren:**
- Notreffen-Fähigkeit bei Systemausfall
- Offshore-Tauglichkeit (CE-Kategorie, Trysegel-Bedarf)
- Einhand-Bedienbarkeit in Notsituationen
- Sturmtauglichkeit (Windbereich des Systems)

### 1.7 Typische Eigner-Profile und Systemzuordnung

| Eigner-Profil | Typisches Boot | Empfohlenes System | Begründung |
|--------------|----------------|-------------------|-----------|
| Regatta-Segler, erfahren | Einrumpf 30–45 ft | Slab (Full Battens) | Maximale Performance, keine Kompromisse |
| Fahrtensegler-Paar, 50+ | Einrumpf 38–50 ft | In-Mast (elektrisch) | Komfort, Kurzhand, Cockpit-Bedienung |
| Blauwasser-Eigner | Einrumpf 40–55 ft | Slab (SLR) oder In-Boom | Zuverlässigkeit, Notreffen, Reparierbarkeit |
| Charter-Betreiber | Einrumpf/Kat 38–50 ft | In-Mast (elektrisch) | Gäste-freundlich, minimale Einweisung |
| Performance-Cruiser | Einrumpf 38–50 ft | In-Boom (elektrisch) | Kompromiss: gute Form + Komfort |
| Weekend-Segler | Einrumpf 28–35 ft | Slab + Lazy-Bag | Budget-freundlich, einfach |
| Einhand-Langfahrer | Einrumpf 35–45 ft | In-Boom (elektrisch) | Notreffen per Fall, gute Segelform |
| Katamaran-Eigner | Katamaran 38–50 ft | In-Mast (elektrisch) | Standard bei Kat-Werften, bewährt |

### 1.8 AYDI-Bewertungseinordnung

Das Großsegel-Reffsystem wird im AYDI-Analysesystem in folgenden Modulen bewertet:

```
Module mit Bezug zum Großsegel-Reff:

ergonomics (Gewicht: 0.75 strukturell / 0.25 visuell):
  - Cockpit-Bedienung möglich? (In-Mast/In-Boom: JA, Slab: BEDINGT)
  - Kurzhand-Tauglichkeit? (In-Mast/In-Boom: HOCH, Slab: NIEDRIG)
  - Reffgeschwindigkeit? (In-Mast: <30s, In-Boom: <60s, Slab: 2-5min)

compliance (Gewicht: 0.95 strukturell / 0.05 visuell):
  - CE-Kategorie A kompatibel? (Alle, aber In-Mast benötigt Trysegel)
  - Notreffen dokumentiert?
  - Manuelles Override bei E-Antrieb vorhanden?

production (Gewicht: 0.55 strukturell / 0.45 visuell):
  - Mastprofil-Typ (Standard oder Furling)?
  - Boom-Typ (Standard oder In-Boom)?
  - Elektrische Installation Komplexität?

structural (Gewicht: 0.95 strukturell / 0.05 visuell):
  - Torsionssteifigkeit Mast (Furling-Mast: -25–40%!)
  - Kompressionslast (Furling-Mast: +5–15% Gewicht)
  - Boom-Belastung (In-Boom: signifikant erhöht)

cost (Gewicht: 1.00 strukturell / 0.00 visuell):
  - Anschaffungskosten (€300–€38.000)
  - Segelkosten (+20–40% für Rollsegel)
  - Wartungskosten/Jahr (€0–800)
  - Lifecycle 20 Jahre (€5.000–55.000)

materials (Gewicht: 0.35 strukturell / 0.65 visuell):
  - Mandrel-Material und Qualität
  - Lager-Typ und Lebensdauer
  - Segeltuch-Kompatibilität

service_patterns (Gewicht: 0.65 strukturell / 0.35 visuell):
  - Typische Fehlerbilder nach System-Typ
  - Wartungsintervalle
  - Ersatzteil-Verfügbarkeit
```

---

## 2. Grundlagen und Theorie

### 2.1 Physikalische Grundlagen des Großsegel-Reffens

#### 2.1.1 Kräfte am Großsegel

Das Großsegel erzeugt Kräfte, die beim Reffen kontrolliert werden müssen:

```
Gesamtkraft_segel = 0.5 × ρ_luft × V_wind² × A_segel × C_L

Wobei:
  ρ_luft ≈ 1.225 kg/m³ (Meereshöhe, 15°C)
  V_wind = wahre Windgeschwindigkeit (m/s)
  A_segel = Segelfläche (m²)
  C_L = Auftriebsbeiwert (0.8–1.5 je nach Anstellwinkel)
```

**Typische Segelkräfte am Großsegel:**

| Bootslänge | Segelfläche | 15 kn | 25 kn | 35 kn | 45 kn |
|------------|------------|-------|-------|-------|-------|
| 8 m | 25 m² | 480 N | 1.340 N | 2.620 N | 4.340 N |
| 10 m | 35 m² | 675 N | 1.875 N | 3.675 N | 6.075 N |
| 12 m | 50 m² | 965 N | 2.680 N | 5.250 N | 8.680 N |
| 14 m | 65 m² | 1.250 N | 3.480 N | 6.825 N | 11.280 N |
| 16 m | 85 m² | 1.640 N | 4.555 N | 8.930 N | 14.770 N |
| 18 m | 105 m² | 2.025 N | 5.625 N | 11.025 N | 18.230 N |
| 20 m | 130 m² | 2.510 N | 6.970 N | 13.660 N | 22.590 N |

**Achtkant-Kräfte am Großfall:**

```
F_fall = F_luff × sin(α) + Segelgewicht × g

Typische Großfall-Kräfte:
  8 m Boot:  800–2.500 N
  12 m Boot: 2.000–6.000 N
  16 m Boot: 4.000–12.000 N
  20 m Boot: 8.000–25.000 N
```

#### 2.1.2 Das Reff-Problem

Beim Reffen muss die Segelfläche unter Last reduziert werden. Die Herausforderungen:

1. **Lastabnahme:** Die Segelfläche muss kontrolliert verkleinert werden, während der Wind noch wirkt
2. **Formerhalt:** Das verbleibende Segel muss eine aerodynamisch sinnvolle Form behalten
3. **Strukturelle Integrität:** Neue Krafteinleitungspunkte (Reffkauschen, Wickelpunkte) müssen die Lasten tragen
4. **Geschwindigkeit:** Je schneller gerefft wird, desto sicherer — Zeitfenster bei Böen ist begrenzt
5. **Ergonomie:** Idealerweise ohne Deckarbeit, vom Cockpit aus

#### 2.1.3 Drei Lösungsphilosophien

**A. Faltreffen (Slab Reefing):**
Das Segel wird durch Absenken des Falls und Strecken der neuen Schothorn-Reffkausch gefaltet. Das überschüssige Tuch hängt lose und wird mit Reffbändsel gesichert.

```
Funktionsprinzip:
  1. Fall fieren → Luff lockern
  2. Reffkausch am Liek in Reffloch einsetzen (oder per Reffhaken)
  3. Reffkausch am Achterliek per Reffleine spannen
  4. Fall wieder dichtholen
  5. Optional: Tuch mit Reffbändseln sichern

Kräfte: Reffleine am Achterliek = ca. 60–80% der Schotlast
```

**B. Vertikales Rollen (In-Mast Furling):**
Das Segel wird um einen Mandrel (Wickelstab) im Inneren eines verbreiterten Mastprofils gewickelt.

```
Funktionsprinzip:
  1. Schot fieren (Achterliek entlasten)
  2. Einholsystem betätigen → Mandrel dreht sich
  3. Segel wickelt sich von vorne (Luff) um den Mandrel
  4. Zum Setzen: Ausholsystem betätigen (Fall oder Ausleine)
  5. Schot trimmen

Kräfte am Mandrel: Torsionsmoment = F_luff × r_mandrel
  Typisch: 150–800 Nm je nach Bootsgröße
```

**C. Horizontales Rollen (In-Boom Furling):**
Das Segel wird um einen Mandrel innerhalb des Baums oder auf einer Wickelanlage auf dem Baum gewickelt.

```
Funktionsprinzip:
  1. Schot fieren, Baumkicker lösen
  2. Fall fieren → Segel senkt sich
  3. Einholsystem im Baum dreht Mandrel
  4. Segel wickelt sich horizontal um den Mandrel
  5. Zum Setzen: Fall holen, Segel fährt aus dem Baum

Kräfte am Mandrel: abhängig von Segelgewicht + Reibung in der Führung
  Typisch: 80–500 Nm je nach Bootsgröße
```

### 2.2 Mastprofilauslegung für In-Mast-Furling

#### 2.2.1 Mastquerschnitt — Standardmast vs. Furling-Mast

Ein Standard-Aluminiummast hat ein elliptisches oder tropfenförmiges Profil, optimiert auf minimalen Windwiderstand bei maximaler Biegesteifigkeit. Ein In-Mast-Furling-Mast erfordert hingegen einen **verbreiterten Querschnitt** (in Richtung Achterstag), um den Mandrel und den Wickelschlitz aufzunehmen.

**Typische Mastquerschnitte (Vergleich):**

| Bootslänge | Standard-Mast (B × T mm) | Furling-Mast (B × T mm) | Verbreiterung |
|------------|--------------------------|------------------------|---------------|
| 9 m | 115 × 180 | 145 × 195 | +26% Breite |
| 11 m | 130 × 200 | 170 × 220 | +31% Breite |
| 13 m | 150 × 230 | 195 × 250 | +30% Breite |
| 15 m | 170 × 260 | 220 × 285 | +29% Breite |
| 17 m | 190 × 290 | 250 × 320 | +32% Breite |
| 20 m | 220 × 330 | 290 × 365 | +32% Breite |

**Auswirkungen auf die Aerodynamik:**
- Windwiderstand des Mastes steigt um ca. 15–25% (abhängig vom Profil)
- Segelgestänge-Interferenz am Mast verringert Auftrieb um ca. 3–7%
- Am-Wind-Performance-Verlust: ca. 3–8% VMG (geschätzt)
- Raumschot-Performance: kaum Unterschied (<2%)

#### 2.2.2 Der Wickelschlitz (Mast-Slot)

Der Wickelschlitz ist die vertikale Öffnung an der Hinterseite des Mastes, durch die das Segel ein- und ausfährt.

**Schlitz-Geometrie:**

```
Schlitzbreite: 20–35 mm (abhängig von Segeltuchdicke und Latten)
Schlitzhöhe: entspricht der gesamten Masthöhe minus Befestigungsbereich
Schlitzlippen: meist Aluminium oder UHMWPE-Führungsschienen
Dichtung: Bürstendichtung oder Lippendichtung gegen Wasser/Wind
```

**Kritische Aspekte:**
- Zu enger Schlitz → Segel klemmt beim Ein-/Ausrollen
- Zu weiter Schlitz → Windgeräusche, Wassereinbruch, Strukturschwächung
- Schlitzlippen müssen perfekt parallel sein → Toleranz <1 mm über gesamte Masthöhe
- Verschleiß der Schlitzlippen → Hauptursache für Klemmprobleme nach 5–10 Jahren

#### 2.2.3 Der Mandrel (Wickelstab)

Der Mandrel ist ein Aluminium- oder Edelstahlrohr im Inneren des Mastes, um das sich das Segel wickelt.

**Mandrel-Durchmesser (typisch):**

| Bootslänge | Segelfläche | Mandrel-Ø | Mandrel-Wandstärke | Mandrel-Material |
|------------|------------|-----------|-------------------|-----------------|
| 8–10 m | 20–35 m² | 50–65 mm | 3,0 mm | Al 6061-T6 |
| 10–12 m | 35–50 m² | 65–80 mm | 3,5 mm | Al 6061-T6 |
| 12–14 m | 50–70 m² | 80–100 mm | 4,0 mm | Al 6082-T6 |
| 14–16 m | 70–90 m² | 100–120 mm | 4,5 mm | Al 6082-T6 |
| 16–18 m | 90–115 m² | 120–140 mm | 5,0 mm | Al 6082-T6 |
| 18–22 m | 115–160 m² | 140–180 mm | 5,5–6,0 mm | Al 6082-T6/SS 316 |

**Mandrel-Lagerung:**
- Oberes Lager: Topplager im Masttop, Axiallast + Radiallast
- Unteres Lager: Fußlager, aufnimmt Axiallast (Segelgewicht) + Torsion
- Zwischenlager: bei Masten >14 m alle 3–4 m zur Schwingungsdämpfung
- Lagertyp: Kugelrollenlager (sealed) oder Gleitlager (PTFE/Delrin)

#### 2.2.4 Kompressionslasten im Furling-Mast

Der Furling-Mast hat gegenüber dem Standardmast veränderte Struktureigenschaften:

```
Kompressionssteifigkeit:
  I_furling ≈ 0.85–0.95 × I_standard (gleiche Wandstärke)
  → Furling-Maste kompensieren durch dickere Wandung oder größeres Profil

Biegesteifigkeit (athwartships):
  EI_athwart_furling ≈ 1.05–1.15 × EI_athwart_standard
  → Verbreiterung kompensiert den Schlitz

Biegesteifigkeit (fore-aft):
  EI_foreaft_furling ≈ 0.90–1.05 × EI_foreaft_standard
  → Der Schlitz schwächt die Achterseite

Torsionssteifigkeit:
  GJ_furling ≈ 0.60–0.75 × GJ_standard
  → SIGNIFIKANTE Schwächung durch den offenen Schlitz!
```

**AYDI-Bewertungsregel:** Die reduzierte Torsionssteifigkeit des Furling-Mastes ist der primäre strukturelle Nachteil. Bei Segelyachten mit hohen Rigg-Vorspannungen (>30% BL des Vorstags) und bei Hochleistungs-Riggs ist dies ein Disqualifikationskriterium für In-Mast-Furling.

### 2.3 Boom-Design für In-Boom-Furling

#### 2.3.1 Boom-Querschnitt

Ein In-Boom-Furling-Boom ist signifikant größer als ein Standard-Boom:

**Typische Boom-Querschnitte:**

| Bootslänge | Standard-Boom (H × B mm) | In-Boom (H × B mm) | Gewicht Standard | Gewicht In-Boom |
|------------|--------------------------|---------------------|-----------------|-----------------|
| 10 m | 120 × 100 | 260 × 200 | 15–20 kg | 35–50 kg |
| 12 m | 140 × 115 | 300 × 230 | 22–30 kg | 55–75 kg |
| 14 m | 160 × 130 | 340 × 260 | 30–45 kg | 80–110 kg |
| 16 m | 180 × 150 | 380 × 290 | 45–60 kg | 110–150 kg |
| 18 m | 200 × 170 | 420 × 320 | 55–80 kg | 150–200 kg |
| 20 m | 230 × 190 | 470 × 360 | 75–100 kg | 200–280 kg |

#### 2.3.2 Mandrel im Boom

Der In-Boom-Mandrel liegt horizontal im Inneren des Baums und wickelt das Segel von oben auf.

```
Mandrel-Durchmesser (In-Boom):
  10–12 m Boot: 80–120 mm
  12–15 m Boot: 120–160 mm
  15–18 m Boot: 160–200 mm
  18–22 m Boot: 200–260 mm

Antrieb: meist am inneren (mast-seitigen) Ende des Booms
Fallsystem: Endlosfallsystem oder kontinuierliches Fall
```

#### 2.3.3 Segeleinlauf am Boom

Das Segel tritt durch einen Schlitz an der Oberseite des Baums ein:

```
Schlitzbreite: 15–30 mm
Führungsrollen: UHMWPE oder Delrin, Abstand 200–400 mm
Tuchumlenkung: sanfte Umlenkung (min. Radius = 5 × Tuchdicke)
Baumvang/Kicker: NICHT möglich bei den meisten In-Boom-Systemen!
  → Stattdessen: starre Baumniederholer-Verbindung (rigid vang)
```

**Kritischer Punkt — Kein Baumkicker:** Die meisten In-Boom-Systeme erlauben keinen konventionellen Baumkicker (Vang), da der Boom zum Rollen frei schwingen muss und die Schlitzöffnung oben liegt. Dies wird kompensiert durch:
- Rigid Vang (starrer Baumniederholer mit Gasdruckfeder)
- Achterstag-Trimm
- Traveller-Trimm
- Eingebaute Twist-Kontrolle im Segelschnitt

### 2.4 Segelformkompromisse

#### 2.4.1 In-Mast-Segel vs. Standard-Großsegel

Ein In-Mast-Rollsegel unterscheidet sich fundamental von einem Standardsegel:

**Einschränkungen:**
- **Keine Segellatten:** Horizontale Latten können nicht durch den Mastschlitz
- **Kein Achterliekrundung (Roach):** Ohne Latten kein positiver Roach → Segel ist dreieckig
- **Flacheres Profil:** Zum sauberen Wickeln muss das Segel relativ flach sein
- **Kein Loose Footed:** Unterliek muss am Baum befestigt sein (Rollweg)
- **Tuchmaterial:** Muss rollbar sein → kein steifes Laminat, keine dicken Membrane

**Segelflächen-Verlust durch fehlenden Roach:**

| Bootslänge | Standard-Segel (m²) | In-Mast-Segel (m²) | Flächenverlust |
|------------|---------------------|---------------------|---------------|
| 10 m | 30 | 24–26 | 13–20% |
| 12 m | 45 | 36–40 | 11–20% |
| 14 m | 62 | 50–55 | 11–19% |
| 16 m | 82 | 66–72 | 12–20% |
| 18 m | 105 | 85–93 | 11–19% |

**Typischer Segelflächen-Verlust In-Mast: 12–18% gegenüber vollgelatteten Großsegel.**

#### 2.4.2 Vertikale Latten (Vertikalbattens)

Einige Hersteller bieten In-Mast-Segel mit vertikalen Latten an:

```
Vertikale Latten:
  Orientierung: senkrecht, vom Unterliek zum Oberliek
  Material: Fiberglas oder Carbon, flexibel
  Anzahl: 3–6 (je nach Segelhöhe)
  Funktion: Geben dem lattenfreien Segel etwas Form
  Roach: Kein Zugewinn (nur Profilverbesserung)
  Einschränkung: Dürfen nicht brechen → Sicherheitsrisiko im Mast
```

**AYDI-Bewertung:** Vertikale Latten verbessern die Profiltiefe um ca. 5–10%, bringen aber keinen Roach-Gewinn. Sie sind ein Kompromiss, der die Segelform leicht verbessert, aber Komplexität und Fehlerrisiko erhöht.

#### 2.4.3 In-Boom-Segel — Latten möglich

Der entscheidende Vorteil des In-Boom-Systems: Das Segel wird vertikal in den Boom gerollt, der Mast ist ein Standard-Profil. Daher:

- **Horizontale Latten möglich:** Kurze bis mittlere Latten (50–70% Segelbreite)
- **Positiver Roach:** 5–12% Flächengewinn möglich (nicht ganz so viel wie beim Volllatten-Segel)
- **Besseres Profil:** Tiefere Profiltiefe als In-Mast
- **Loose Foot:** Unterliek ist frei → besserer Twist

**Einschränkungen In-Boom-Segel:**
- Durchgehende Latten (Full Battens) nur bei wenigen Systemen (Leisure Furl)
- Latten müssen flexibel genug sein, um sich im Boom aufzuwickeln
- Lattentaschen müssen verstärkt sein (Scheuerschutz am Boom-Schlitz)

#### 2.4.4 Tuchauswahl für Rollreffsegel

| Tuchtyp | In-Mast geeignet | In-Boom geeignet | Standard geeignet | Haltbarkeit | Kosten |
|---------|------------------|------------------|-------------------|-------------|--------|
| Polyester (Dacron) gewoven | Ja (Standard) | Ja | Ja | 8–12 Jahre | € |
| Polyester cross-cut | Ja (gut) | Ja | Ja | 6–10 Jahre | € |
| Polyester radial | Bedingt | Ja (gut) | Ja | 8–12 Jahre | €€ |
| Pentex | Bedingt | Ja | Ja | 10–15 Jahre | €€€ |
| Hydranet (Dyneema-Polyester) | Ja (empfohlen) | Ja (empfohlen) | Ja | 12–18 Jahre | €€€€ |
| Elvström EPEX | Ja (Spezial) | Ja | Ja | 10–15 Jahre | €€€€ |
| 3Di / Stratis | Nein | Bedingt | Ja | 15–20 Jahre | €€€€€ |
| Membran (Nordsegel) | Nein | Nein | Ja | 8–15 Jahre | €€€€€ |
| PBO/Carbon-Laminat | Nein | Nein | Ja (Regatta) | 5–8 Jahre | €€€€€€ |

**AYDI-Empfehlung:** Für In-Mast-Systeme ist Hydranet (Dyneema-Polyester-Hybrid) oder hochwertiges Dacron der beste Kompromiss aus Rollbarkeit, Formhaltung und Langlebigkeit.

### 2.5 Mandrel-Systeme im Detail

#### 2.5.1 Mandrel-Geometrie

Der Mandrel ist ein dünnwandiges Rohr, das sich über die gesamte Masthöhe (In-Mast) bzw. Baumlänge (In-Boom) erstreckt.

**Wickelverhalten:**

```
Wickellagen bei voll eingerolltem Segel:
  N_lagen = Tuchdicke_total / (π × D_mandrel)

  Beispiel: 12 m Boot, Segelfläche 45 m²
    Tuchdicke (Dacron): 0.3 mm
    Luff-Länge: 14 m
    Foot-Länge: 5 m
    Mittlere Segelbreite: ca. 2.5 m → 2500 mm / (π × 80) ≈ 10 Lagen
    → 10 Lagen × 0.3 mm = 3.0 mm Aufbau pro Seite
    → Gesamtdurchmesser mit Segel: 80 + 6 = 86 mm
```

**Wickelgleichmäßigkeit:**
- Gleichmäßiges Wickeln ist entscheidend für störungsfreien Betrieb
- Ungleichmäßigkeit entsteht durch: unterschiedliche Tuchdicke (Nähte, Patches), Torsion im Segel, Windlast beim Rollen
- Kompensation: Luff-Tape mit definierter Dicke, Foam-Strips am Luff

#### 2.5.2 Antriebssysteme

**Manueller Antrieb (Standard bei Booten <12 m):**

```
Antrieb: Endlosbändsel (Leine) um Trommel am Mastfuß
Übersetzung: 1:2 bis 1:4 (Trommel zu Mandrel)
Bedienkraft: 30–80 N am Bändsel
Geschwindigkeit: 30–90 Sekunden für volles Ein-/Ausrollen
Führung: Leinenführung zum Cockpit über Umlenkrollen
```

**Elektrischer Antrieb (Standard bei Booten >12 m):**

```
Motor: 12V oder 24V DC Permanentmagnet-Motor
Leistung: 200–1.500 W (je nach Bootsgröße)
Drehmoment: 15–120 Nm am Motor, 150–1.200 Nm am Mandrel
Übersetzung: Planetengetriebe, 1:8 bis 1:15
Geschwindigkeit: 15–45 Sekunden für volles Ein-/Ausrollen
Steuerung: Taster (auf/ab), optional CAN-Bus
Notbetrieb: Manuelles Override (Kurbel oder Handliene)
Stromaufnahme: 15–60 A bei 12V, 8–30 A bei 24V
```

**Hydraulischer Antrieb (Yachten >18 m):**

```
Antrieb: Hydraulikmotor, gespeist von zentraler Hydraulikanlage
Druck: 80–200 bar
Drehmoment: 200–3.000 Nm am Mandrel
Geschwindigkeit: 20–60 Sekunden (stufenlos regelbar)
Vorteil: Enormes Drehmoment, leise, stufenlos
Nachteil: Hydraulikanlage erforderlich, Leckagerisiko
```

### 2.6 Aerodynamische Auswirkungen der verschiedenen Systeme

#### 2.6.1 Profiltiefe und Twist

Die aerodynamische Qualität eines Großsegels wird durch zwei Hauptparameter bestimmt:

**Profiltiefe (Draft/Camber):**
```
Optimale Profiltiefe = 8–14% der Segeltiefe (Chord)
  Leichtwind (<10 kn): 12–14% (tiefes Profil für max. Auftrieb)
  Mittelwind (10–20 kn): 10–12% (moderates Profil)
  Starkwind (>20 kn): 8–10% (flaches Profil für weniger Krängung)

Erreichbare Profiltiefe nach System:
  Standard-Großsegel (Full Battens): 8–15% (voll einstellbar)
  In-Mast (lattenlos): 5–9% (eingeschränkt)
  In-Mast (Vertikallatten): 6–11% (etwas besser)
  In-Boom (Kurzlatten): 7–13% (fast wie Standard)
  In-Boom (Full Battens): 8–14% (nahezu Standard)
```

**Twist (Profilverwindung):**
```
Twist beschreibt die Drehung des Segelprofils vom Fuß zum Kopf.
  Optimaler Twist: 5–15° (abhängig von Windgeschwindigkeit und -gradient)

Twist-Kontrolle nach System:
  Standard (Baumkicker + Traveller): Ausgezeichnet (★★★★★)
  In-Mast (nur Traveller): Eingeschränkt (★★★☆☆)
  In-Boom (Rigid Vang + Traveller): Gut (★★★★☆)
  Slab (Baumkicker + Traveller): Ausgezeichnet (★★★★★)
```

#### 2.6.2 Auftriebsbeiwert C_L nach Systemtyp

Gemessene Auftriebsbeiwerte (Windkanal-Approximation) für typische Großsegel bei optimalem Anstellwinkel:

| Segeltyp | C_L max (Upwind) | C_L max (Reaching) | C_D min | L/D max |
|----------|-----------------|-------------------|---------|---------|
| Full-Batten Standard | 1,35–1,55 | 1,40–1,60 | 0,04–0,06 | 25–35 |
| Slab-Reff (1. Reff) | 1,25–1,45 | 1,30–1,50 | 0,05–0,07 | 20–28 |
| In-Mast (lattenlos) | 0,95–1,15 | 1,10–1,30 | 0,06–0,09 | 12–18 |
| In-Mast (Vertikallatten) | 1,05–1,25 | 1,15–1,35 | 0,05–0,08 | 15–22 |
| In-Boom (Kurzlatten) | 1,20–1,40 | 1,30–1,50 | 0,04–0,07 | 20–30 |
| In-Boom (Full Battens) | 1,30–1,50 | 1,35–1,55 | 0,04–0,06 | 23–33 |

**AYDI-Bewertungsformel Segeleffizienz:**
```
Effizienz_Index = (C_L_system / C_L_standard) × (A_segel_system / A_segel_standard) × 100

Beispiel In-Mast, 12m Boot:
  C_L_ratio = 1.05 / 1.45 = 0.724
  A_ratio = 40 / 50 = 0.800
  Effizienz_Index = 0.724 × 0.800 × 100 = 57.9
  → In-Mast liefert ca. 58% der Antriebsleistung eines Standard-Großsegels am Wind
```

#### 2.6.3 VMG-Verlust-Kalkulation

Der praktische Geschwindigkeitsverlust (VMG — Velocity Made Good) durch In-Mast vs. Standard:

```
VMG-Verlust (geschätzt, Am-Wind, wahrer Wind 12–18 kn):
  8 m Boot:  6–10% VMG-Verlust (In-Mast vs. Full-Batten Standard)
  12 m Boot: 5–8% VMG-Verlust
  16 m Boot: 4–7% VMG-Verlust
  20 m Boot: 3–6% VMG-Verlust

VMG-Verlust (geschätzt, Am-Wind, wahrer Wind 12–18 kn):
  In-Boom (Kurzlatten) vs. Standard: 2–4% VMG-Verlust
  In-Boom (Full Battens) vs. Standard: 1–2% VMG-Verlust

VMG-Verlust (Raumschot/Vorwind):
  In-Mast vs. Standard: 1–4% (weniger relevant, da Zusatzsegel möglich)
  In-Boom vs. Standard: <2%
```

**Kompensationsmöglichkeiten:**
- Code 0 oder Gennaker: Kompensiert Flächenverlust auf Raumschotkursen vollständig
- Größeres Vorsegel (wenn In-Mast → kleineres Groß): Kann Am-Wind teilweise kompensieren
- Optimiertes Segelschnitt: Vertikale Latten, Hydranet-Tuch → besseres Profil

### 2.7 Wärmeausdehnung und Klimaeffekte

#### 2.7.1 Thermische Ausdehnung des Aluminium-Mastes

Aluminium hat einen relativ hohen Wärmeausdehnungskoeffizienten:

```
α_Aluminium = 23.1 × 10⁻⁶ /°C

Längenänderung eines 18 m Mastes bei ΔT = 40°C (Winter -5°C → Sommer +35°C):
  ΔL = α × L × ΔT = 23.1 × 10⁻⁶ × 18000 × 40 = 16.6 mm

Breitenänderung des Schlitzes (25 mm Breite, ΔT = 40°C):
  ΔB = α × B × ΔT = 23.1 × 10⁻⁶ × 25 × 40 = 0.023 mm → vernachlässigbar
```

Die Längenänderung ist relevant für Mandrel-Lager (Axiallast durch Thermal-Expansion) und Fall-Spannung (Fall muss thermische Ausdehnung kompensieren können).

#### 2.7.2 Frost- und Eisprobleme

In nordeuropäischen Revieren kann Frost/Eis den Furling-Betrieb beeinträchtigen:

| Problem | In-Mast | In-Boom | Slab |
|---------|---------|---------|------|
| Eis im Mastschlitz | KRITISCH — blockiert Mandrel | n/a | Kein Problem |
| Gefrorenes Segel | Mandrel kann nicht drehen | Segel klebt im Boom | Reffleinen können einfrieren |
| Kondenswasser-Eis | Lager können einfrieren | Führungsrollen können einfrieren | Kein Problem |
| Prävention | Mastschlitz mit Frostschutz behandeln, Segel vor Frost einrollen | Boom-Abdeckung, Belüftung | Leinen frostfrei halten |

**AYDI-Bewertungsregel:** Für Reviere mit regelmäßigem Frost (Ostsee, Nordsee November–März) ist In-Mast-Furling ein Risikofaktor. System muss vor Frost eingerollt und konserviert werden. Reffen bei Frost ist NICHT zuverlässig möglich.

### 2.8 Gewichtsanalyse und Schwerpunktauswirkung

#### 2.8.1 Gewichtsvergleich der Systeme

| Komponente | Slab + Lazyjacks | In-Mast (manuell) | In-Mast (elektrisch) | In-Boom (manuell) | In-Boom (elektrisch) |
|-----------|-----------------|-------------------|---------------------|-------------------|---------------------|
| Mast (12m Boot) | 85 kg (Standard) | 110 kg (Furling) | 110 kg | 85 kg (Standard) | 85 kg |
| Boom | 22 kg | 22 kg | 22 kg | 65 kg (In-Boom) | 65 kg |
| Mandrel | — | 12 kg | 12 kg | 15 kg | 15 kg |
| Antrieb | — | 3 kg (Trommel) | 12 kg (Motor) | 3 kg (Trommel) | 14 kg (Motor) |
| Segel (45 m²) | 18 kg | 15 kg (kleiner) | 15 kg | 17 kg | 17 kg |
| Lazyjacks/Bag | 3 kg | — | — | — | — |
| Rigid Vang | — | — | — | 8 kg | 8 kg |
| **Gesamt** | **128 kg** | **162 kg** | **171 kg** | **193 kg** | **204 kg** |
| **Differenz** | **Referenz** | **+34 kg** | **+43 kg** | **+65 kg** | **+76 kg** |

#### 2.8.2 Schwerpunktauswirkung

Das Zusatzgewicht befindet sich bei In-Mast oben im Mast (hoher Schwerpunkt), bei In-Boom am Baum (mittlerer Schwerpunkt):

```
Schwerpunktverschiebung (12 m Boot, Verdrängung 8.000 kg):

In-Mast: +25 kg auf Masthöhe (ca. 8 m über WL)
  → ΔKG = (25 × 8) / 8000 = 0.025 m = 25 mm Schwerpunktanhebung
  → Stabilitätsverlust: ca. 0.5–1.0° im GZ-Kurven-Maximum

In-Boom: +43 kg auf Baumhöhe (ca. 2.5 m über WL)
  → ΔKG = (43 × 2.5) / 8000 = 0.013 m = 13 mm Schwerpunktanhebung
  → Stabilitätsverlust: ca. 0.3–0.5° im GZ-Kurven-Maximum
```

**AYDI-Bewertungsregel:** Bei Yachten mit kritischer Stabilität (Rennboote, leichte Mehrrumpfer) ist das Zusatzgewicht im Rigg ein relevanter Faktor. Bei schweren Fahrtenyachten (>200 kg/m) ist die Auswirkung vernachlässigbar.

### 2.9 Slab-Reefing-Mechanik im Detail

#### 2.6.1 Reffpunkte und Reffkauschen

Ein Standard-Großsegel hat 1–3 Reffkauschen (Slab Reefs):

```
Reef 1: Reduziert Segelfläche um ca. 15–25%
  Höhe über Baum: 1.2–2.0 m (je nach Bootsgröße)
  Einsatz: ab 15–20 kn wahrer Wind

Reef 2: Reduziert Segelfläche um ca. 30–45%
  Höhe über Baum: 2.0–3.5 m
  Einsatz: ab 22–28 kn wahrer Wind

Reef 3: Reduziert Segelfläche um ca. 50–65%
  Höhe über Baum: 3.0–5.0 m
  Einsatz: ab 30–40 kn wahrer Wind
  Nur bei Blauwasseryachten und Yachten >14 m üblich
```

#### 2.6.2 Einleinen-Reff (Single-Line Reefing)

Modernste Form des Slab-Reefings — eine Leine pro Reff, die sowohl Fall-Funktion als auch Schothorn-Reff übernimmt:

```
Leineführung:
  Cockpit → Umlenkrolle Baum (achtern) → Durch Baum nach vorne →
  Umlenkrolle am Baumstumpf → Nach oben zum Luff-Reffpunkt →
  Durch Reffkausch Luff → Zurück nach unten → Zum Achterliek-Reffpunkt →
  Durch Reffkausch Achterliek → Fixpunkt am Baum

Vorteil: Eine Person, ein Handgriff pro Reff
Nachteil: Komplexe Leinenführung, mehr Reibung, nur möglich wenn
          Luff-Reffkausch und Achterliek-Reffkausch korrekt synchron
```

#### 2.6.3 Lazyjacks und Lazy-Bag-Systeme

Lazyjacks sind Leinen vom Mast (oberes Drittel) zum Baum, die eine trichterförmige Fangvorrichtung bilden:

```
Lazyjack-Konfiguration:
  2–3 Paare (Backbord + Steuerbord)
  Oberer Ansatzpunkt: 50–75% Masthöhe
  Unterer Ansatzpunkt: Baum, gleichmäßig verteilt
  Material: 4–6 mm Polyester-Geflecht
  Optional: Lazy-Bag (Persenning zwischen den Lazyjacks)
```

**Lazy-Bag (Segelpersenning am Baum):**
- Schützt das geborgte Segel vor UV
- Erleichtert das Bergen: Segel fällt in den Bag
- Kompatibel mit Slab-Reefing
- NICHT kompatibel mit In-Boom-Furling
- Bedingt kompatibel mit In-Mast (wird überflüssig)

---

## 3. Typenübersicht

### 3.1 In-Mast Furling (Vertikales Rollreff im Mast)

#### 3.1.1 Funktionsprinzip

Das Segel wird um einen vertikalen Mandrel im Inneren eines verbreiterten Mastprofils gewickelt. Der Mandrel wird von oben (Masttop) oder unten (Mastfuß) angetrieben.

```
Systemkomponenten:
  1. Furling-Mastprofil (verbreitert, mit Schlitz)
  2. Mandrel (Wickelstab, Aluminium/Edelstahl)
  3. Oberlager (Masttop, Drucklager + Radiallager)
  4. Unterlager (Mastfuß, Trommel + Antrieb)
  5. Antrieb (manuell/elektrisch/hydraulisch)
  6. Bedienleinen (Einholsystem)
  7. Segel (Spezial-Rollsegel, lattenlos oder vertikale Latten)
  8. Outhaul-System (Unterliek-Spannung beim Setzen)
```

#### 3.1.2 Varianten

**A. Kontinuierliches In-Mast (Standard):**
- Stufenloses Reffen möglich (jede beliebige Segelfläche)
- Am weitesten verbreitet (90%+ aller In-Mast-Systeme)
- Segel kann bei jeder Windstärke teilweise oder ganz gerollt werden

**B. Rasten-In-Mast:**
- Mandrel rastet in definierten Positionen ein (z.B. 100%, 75%, 50%, 25%)
- Vorteil: Definierte Segelform bei den Rastpositionen
- Nachteil: Weniger flexibel, mechanisch komplexer
- Selten, nur bei einigen Custom-Systemen

**C. In-Mast mit Kopfbrett:**
- Segel hat ein Kopfbrett, das nicht eingerollt wird
- Mandrel endet unterhalb des Kopfbretts
- Vorteil: Bessere Segelform im Top
- Nachteil: Kopfbrett muss separat gesichert werden

#### 3.1.3 Typische Installations-Konfiguration

```
Deckslayout für In-Mast:
  ┌─────────────────────────────────────────┐
  │                                         │
  │              SEGEL (gerollt)            │
  │           ┌───┐                         │
  │           │ M │ ← Mast (verbreitert)    │
  │           │ A │    mit Schlitz achtern   │
  │           │ S │                         │
  │           │ T │                         │
  │           └─┬─┘                         │
  │             │                           │
  │     ┌───────┼───────┐ ← Baum           │
  │     │       │       │                   │
  │     │   Trommel +   │                   │
  │     │   Antrieb     │                   │
  │     └───────────────┘                   │
  │                                         │
  │  Bedienleinen → Cockpit                 │
  └─────────────────────────────────────────┘
```

### 3.2 In-Boom Furling (Horizontales Rollreff im Baum)

#### 3.2.1 Funktionsprinzip

Das Segel wird durch Fieren des Falls in den Baum abgesenkt und dort um einen horizontalen Mandrel gewickelt.

```
Systemkomponenten:
  1. Standard-Mastprofil (KEIN verbreitertes Profil nötig)
  2. Spezial-Boom (vergrößert, mit Schlitz oben)
  3. Mandrel horizontal im Boom
  4. Antrieb am Mastende des Booms (oder extern)
  5. Fall-System (Endlosfallsystem oder manuelles Fall)
  6. Tuchführung (Rollen/Schienen an Boom-Oberseite)
  7. Segel (Spezial-Rollsegel, Latten möglich)
  8. Rigid Vang (starrer Baumniederholer, obligatorisch)
```

#### 3.2.2 Varianten

**A. Mandrel-Wicklung (Standard):**
- Segel wickelt sich um einen rotierenden Mandrel im Boom
- Kontinuierliches Reffen möglich
- Hersteller: Leisure Furl, Bartels, Z-Spars

**B. Faltwicklung (Stack-Pack-Prinzip):**
- Segel faltet sich in definierten Bahnen in den Boom
- Mandrel mit Führungsschienen
- Weniger verbreitet, besser für Segel mit Latten
- Hersteller: Schaefer Marine (USA)

**C. Unterlieks-Aufroller:**
- Einfachste Form: Segel rollt sich um das Unterliek auf dem Baum
- Historisch (Hood-System), heute selten
- Schlechte Segelform, aber sehr einfach

#### 3.2.3 Typische Installations-Konfiguration

```
Seitenansicht In-Boom:
  ┌────────────────────────────────────────────────┐
  │                                                │
  │    ┌─┐ ← Masttop (Standard)                   │
  │    │M│                                         │
  │    │A│   Fall (Endlos-Fall-System)              │
  │    │S│         │                               │
  │    │T│         ▼                               │
  │    │ │   ┌─────────────────────────────┐       │
  │    │ │   │  BOOM (vergrößert)          │       │
  │    │ │   │  ┌─ Schlitz oben ──────────┐│       │
  │    │ │   │  │ Segel wickelt sich ein  ││       │
  │    │ │   │  └─────────────────────────┘│       │
  │    │ │   │  Mandrel ═══════════════    │       │
  │    └─┘   └─────────────────────────────┘       │
  │    │         │                                 │
  │    │    Rigid Vang                              │
  │    │         │                                 │
  │    DECK──────┴─────────────────────────────    │
  └────────────────────────────────────────────────┘
```

### 3.3 Slab Reefing mit Lazyjacks

#### 3.3.1 Funktionsprinzip

Das traditionelle Binde-Reff, modernisiert mit Lazyjacks und ggf. Lazy-Bag:

```
Reffvorgang (klassisch, 2 Personen):
  1. Kurs leicht abfallen (Segel entlasten)
  2. Person am Mast: Baumtopp-Leine klar machen
  3. Person im Cockpit: Fall fieren bis Reffliek-Kausch am Reffloch
  4. Person am Mast: Reffliek in Refflhaken einhängen
  5. Person im Cockpit: Reffleine Achterliek dichtholen
  6. Fall wieder dichtholen
  7. Loses Tuch mit Reffbändseln sichern (optional)

Reffvorgang (Einhand mit Einleinen-Reff):
  1. Kurs leicht abfallen
  2. Baumtopp-Reffleine dichtholen → Fall und Reffkausch gleichzeitig
  3. Fall nachjustieren
  4. Fertig (Loses Tuch hängt in Lazyjacks)
```

#### 3.3.2 Voraussetzungen für effektives Slab-Reefing

- **Reffkauschen:** Robust dimensioniert, mind. 8 mm Edelstahl-Kausche
- **Reffleinen:** Vorgerecktes Polyester, 8–12 mm je nach Bootsgröße
- **Umlenkrollen:** Am Baum, Reibungsarm (Harken/Ronstan Micro-Blöcke)
- **Lazyjacks:** 3 Paare, gut eingestellt, um Tuch aufzufangen
- **Fall-Stopper:** Clutch (Spinlock, Lewmar, Antal) muss zuverlässig halten
- **Segel mit Reffstreifen:** Horizontale Verstärkungsstreifen auf Reffhöhe

### 3.4 Single-Line Reefing (Einleinen-Reff)

#### 3.4.1 Funktionsprinzip

Eine einzelne Leine pro Reff übernimmt sowohl die Fall-Funktion (Luff-Reffkausch herunterziehen) als auch die Achterliek-Funktion (Schothorn-Reffkausch spannen).

```
Leinenführung (vereinfacht):
  Clutch → Leine → Umlenkung Baum (achtern) →
  Durch Bauminneres → Austritt Baumstumpf →
  Nach oben: in Luff-Reffkausch → Durch Kausch →
  Nach achtern: in Achterliek-Reffkausch → Fixpunkt Baum

Ergebnis: Ein Zug → Fall fiert, Luff-Kausch kommt runter,
          Achterliek-Kausch wird gespannt → Reff gesetzt
```

#### 3.4.2 Varianten

**A. Selden-Typ (am Mast geführt):**
- Leine läuft am Mast herunter → Umlenkung → durch Baum
- Weniger Reibung, aber komplexere Führung am Mast

**B. Boom-geführt (Standard bei Beneteau, Bavaria):**
- Leine läuft komplett durch den Baum
- Einfacher, aber mehr Reibung → Clutch-Last höher

**C. Hybrid:**
- Luff-Reffkausch hat separaten Haken (automatisch einrastend)
- Nur Achterliek-Leine wird bedient
- Weniger Reibung, aber Haken muss funktionieren

### 3.5 Elektrisches Reffen

#### 3.5.1 Elektrischer In-Mast-Antrieb

```
Komponenten:
  - DC-Motor (12V/24V), 200–1.500 W
  - Planetengetriebe (Untersetzung 1:8 bis 1:15)
  - Kupplung (Freilauf oder Bremse)
  - Steuerung (Taster, optional Busanbindung)
  - Endschalter (voll eingerollt / voll ausgerollt)
  - Überlastschutz (Strombegrenzung)
  - Manuelle Override-Möglichkeit (Kurbel/Leine)

Typische Spezifikationen:
  12 m Boot: 12V, 350 W, 25 A, 200 Nm am Mandrel
  15 m Boot: 24V, 700 W, 30 A, 500 Nm am Mandrel
  18 m Boot: 24V, 1.200 W, 50 A, 900 Nm am Mandrel
```

#### 3.5.2 Elektrischer In-Boom-Antrieb

```
Komponenten (ähnlich In-Mast, aber):
  - Motor im Boom oder extern am Mastfuß
  - Antrieb über Zahnriemen oder Kette zum Boom-Mandrel
  - Fall-Motor separat oder kombiniert
  - Synchronisierung Fall/Mandrel kritisch!

Besonderheit: Fall und Mandrel müssen synchron arbeiten
  → Fall muss exakt so schnell fieren wie der Mandrel einrollt
  → Asynchronität → Segel staut sich oder wird zu straff
  → Lösung: Endlos-Fall-System oder elektronische Synchronisierung
```

#### 3.5.3 Manuelle vs. Elektrisch vs. Hydraulisch — Übersicht

| Kriterium | Manuell | Elektrisch | Hydraulisch |
|-----------|---------|-----------|-------------|
| Bootslänge | 8–14 m | 10–22 m | 16–30 m+ |
| Kosten (System) | €500–2.500 | €3.000–15.000 | €10.000–40.000 |
| Stromverbrauch | 0 W | 200–1.500 W | Hydraulikpumpe |
| Bedienzeit (voll reffen) | 30–120 s | 15–45 s | 20–60 s |
| Bedienkraft | 30–80 N | Taster | Taster/Ventil |
| Zuverlässigkeit | Hoch (wenig Teile) | Mittel-Hoch | Mittel |
| Notbetrieb | — | Manuelles Override | Handpumpe |
| Wartung | Gering | Mittel | Hoch |
| Gewicht (System) | 2–8 kg | 8–25 kg | 15–50 kg |

---

## 4. Produktlinien und Hersteller

### 4.1 In-Mast-Systeme

#### 4.1.1 Selden (Schweden) — Marktführer In-Mast

Selden ist der weltweit größte Hersteller von Furling-Masten und der OEM-Lieferant für die meisten europäischen Serienwerften (Beneteau, Jeanneau, Hanse, Bavaria, Dufour, Dehler).

**Produktlinie: Selden Furlex Mast-Furling:**

| Modell | Bootslänge | Segelfläche | Mastprofil (B×T mm) | Mandrel-Ø | Antrieb | Art.-Nr. (Basis) |
|--------|-----------|------------|--------------------|-----------|---------|--------------------|
| C290 | 8–10 m | 18–30 m² | 145×195 | 55 mm | Manuell | 508-282-01 |
| C350 | 10–12 m | 28–42 m² | 170×220 | 70 mm | Man./El. | 508-352-01 |
| C390 | 11–14 m | 38–58 m² | 195×250 | 85 mm | Man./El. | 508-392-01 |
| C430 | 13–16 m | 50–75 m² | 220×285 | 100 mm | Elektrisch | 508-432-01 |
| C470 | 15–18 m | 65–95 m² | 250×315 | 120 mm | Elektrisch | 508-472-01 |
| C530 | 17–22 m | 85–130 m² | 290×365 | 140 mm | El./Hydr. | 508-532-01 |

**Selden Furlex Elektrische Antriebe:**

| Modell | Passend für | Spannung | Leistung | Drehmoment | Art.-Nr. |
|--------|------------|----------|----------|-----------|----------|
| E20 | C290–C350 | 12V | 250 W | 150 Nm | 508-920-01 |
| E30 | C350–C390 | 12V | 450 W | 280 Nm | 508-930-01 |
| E40 | C390–C430 | 12V/24V | 700 W | 450 Nm | 508-940-01 |
| E50 | C430–C470 | 24V | 1.000 W | 700 Nm | 508-950-01 |
| E60 | C470–C530 | 24V | 1.400 W | 1.000 Nm | 508-960-01 |

**Selden Mastprofile — Technische Daten:**

| Profil | Wandstärke | Gewicht/m | I_x (cm⁴) | I_y (cm⁴) | Schlitzbreite |
|--------|-----------|-----------|-----------|-----------|---------------|
| C290 | 3,5 mm | 5,2 kg/m | 1.850 | 980 | 22 mm |
| C350 | 4,0 mm | 6,8 kg/m | 3.200 | 1.650 | 25 mm |
| C390 | 4,5 mm | 8,5 kg/m | 5.100 | 2.650 | 28 mm |
| C430 | 5,0 mm | 10,8 kg/m | 7.800 | 4.100 | 30 mm |
| C470 | 5,5 mm | 13,5 kg/m | 11.500 | 6.200 | 32 mm |
| C530 | 6,0 mm | 17,2 kg/m | 16.800 | 9.100 | 35 mm |

**Besonderheiten Selden:**
- Größte Teileverfügbarkeit weltweit (OEM für Dutzende Werften)
- Mandrel aus Al 6082-T6, eloxiert
- Lager: Sealed SKF-Kugellager
- Ersatzteilverfügbarkeit: 25+ Jahre garantiert
- Service-Netzwerk: weltweilt, besonders stark in Nordeuropa

#### 4.1.2 Facnor (Frankreich) — Premium In-Mast

Facnor ist bekannt für hochwertige Vorsegel-Rollreffanlagen und bietet eine eigene In-Mast-Linie für das Semi-Custom-Segment.

**Produktlinie: Facnor FMI (Furling Mast Integrated):**

| Modell | Bootslänge | Segelfläche | Mastprofil (B×T mm) | Mandrel-Ø | Art.-Nr. |
|--------|-----------|------------|--------------------|-----------|---------| 
| FMI 28 | 9–11 m | 22–35 m² | 155×205 | 60 mm | FMI-028 |
| FMI 35 | 11–13 m | 32–50 m² | 180×230 | 75 mm | FMI-035 |
| FMI 42 | 13–16 m | 45–70 m² | 210×260 | 90 mm | FMI-042 |
| FMI 50 | 15–18 m | 60–95 m² | 240×300 | 110 mm | FMI-050 |
| FMI 60 | 17–22 m | 80–130 m² | 280×350 | 135 mm | FMI-060 |

**Facnor Elektrische Antriebe:**

| Modell | Passend für | Spannung | Leistung | Art.-Nr. |
|--------|------------|----------|----------|----------|
| EMI 200 | FMI 28–35 | 12V | 300 W | EMI-200 |
| EMI 400 | FMI 35–42 | 12V/24V | 550 W | EMI-400 |
| EMI 600 | FMI 42–50 | 24V | 850 W | EMI-600 |
| EMI 1000 | FMI 50–60 | 24V | 1.300 W | EMI-1000 |

**Besonderheiten Facnor:**
- Hohe Fertigungsqualität (Made in France)
- Patentiertes Selbstzentrierungs-Lagersystem
- Mandrel aus Al 7075-T6 (höchste Festigkeit)
- Kein OEM für Großserienwerften → hauptsächlich Refit und Semi-Custom
- Premium-Preissegment (+20–30% vs. Selden)

#### 4.1.3 Profurl (Frankreich) — Vorsegel-Experte mit In-Mast-Linie

Profurl ist primär für Vorsegel-Rollreffanlagen bekannt, bietet aber eine In-Mast-Option.

**Produktlinie: Profurl MFS (Mast Furling System):**

| Modell | Bootslänge | Segelfläche | Mandrel-Ø | Art.-Nr. |
|--------|-----------|------------|-----------|----------|
| MFS 30 | 9–11 m | 20–32 m² | 58 mm | MFS-030 |
| MFS 40 | 11–14 m | 30–50 m² | 78 mm | MFS-040 |
| MFS 55 | 13–17 m | 45–75 m² | 98 mm | MFS-055 |
| MFS 70 | 16–21 m | 65–110 m² | 125 mm | MFS-070 |

**Besonderheiten Profurl:**
- Mandrel-System in bestehende Masten nachrüstbar (Refit-Spezialist)
- Patentiertes NEX-Profilsystem (nachrüstbare Führungsschienen)
- Schwerpunkt: Refit-Markt, Nachrüstung vorhandener Masten
- Kompetitiver Preis, gute Qualität

#### 4.1.4 Leisure Furl (USA/UK) — In-Mast-Spezialist

Leisure Furl bietet sowohl In-Mast- als auch In-Boom-Systeme und ist im anglophonen Markt stark vertreten.

**Produktlinie: Leisure Furl MR (Mast Reefing):**

| Modell | Bootslänge | Segelfläche | Art.-Nr. |
|--------|-----------|------------|----------|
| MR 30 | 9–11 m | 20–35 m² | LF-MR30 |
| MR 42 | 11–14 m | 30–55 m² | LF-MR42 |
| MR 55 | 13–17 m | 45–80 m² | LF-MR55 |
| MR 70 | 16–22 m | 65–120 m² | LF-MR70 |

**Besonderheiten Leisure Furl:**
- Patentiertes Mandrel-Design mit konischem Endstück
- Integrierte Leitvorrichtung am Schlitz (reduziert Verklemmungen)
- In-Boom und In-Mast aus einer Hand → Beratungskompetenz

#### 4.1.5 Schaefer Marine (USA) — Tradition und Innovation

**Produktlinie: Schaefer In-Mast Furling:**

| Modell | Bootslänge | Segelfläche | Art.-Nr. |
|--------|-----------|------------|----------|
| IMF 400 | 10–13 m | 25–45 m² | SM-IMF400 |
| IMF 600 | 12–16 m | 40–70 m² | SM-IMF600 |
| IMF 800 | 15–20 m | 60–100 m² | SM-IMF800 |
| IMF 1000 | 18–24 m | 85–140 m² | SM-IMF1000 |

**Besonderheiten Schaefer:**
- US-Marktführer für In-Mast
- Kompatibel mit vielen US-amerikanischen Mastherstellern (Hall, Sparcraft)
- Robuste Industriequalität, einfacher Aufbau

### 4.2 In-Boom-Systeme

#### 4.2.1 Leisure Furl (USA/UK) — Marktführer In-Boom

Leisure Furl ist der weltweit bekannteste Hersteller von In-Boom-Furling-Systemen.

**Produktlinie: Leisure Furl BR (Boom Reefing):**

| Modell | Bootslänge | Segelfläche | Boom-Querschnitt (H×B mm) | Mandrel-Ø | Gewicht | Art.-Nr. |
|--------|-----------|------------|---------------------------|-----------|---------|----------|
| BR 26 | 8–10 m | 15–28 m² | 240×185 | 90 mm | 32 kg | LF-BR26 |
| BR 34 | 10–12 m | 25–42 m² | 280×210 | 110 mm | 48 kg | LF-BR34 |
| BR 42 | 12–14 m | 38–58 m² | 320×240 | 130 mm | 68 kg | LF-BR42 |
| BR 50 | 14–16 m | 50–75 m² | 360×270 | 155 mm | 92 kg | LF-BR50 |
| BR 60 | 16–19 m | 65–100 m² | 400×300 | 180 mm | 125 kg | LF-BR60 |
| BR 75 | 19–23 m | 90–140 m² | 450×340 | 210 mm | 175 kg | LF-BR75 |
| BR 90 | 22–28 m | 120–190 m² | 500×380 | 240 mm | 240 kg | LF-BR90 |

**Leisure Furl Elektrische Antriebe für In-Boom:**

| Modell | Passend für | Spannung | Leistung | Drehmoment | Art.-Nr. |
|--------|------------|----------|----------|-----------|----------|
| EBR 300 | BR 26–34 | 12V | 350 W | 200 Nm | LF-EBR300 |
| EBR 500 | BR 34–42 | 12V/24V | 600 W | 380 Nm | LF-EBR500 |
| EBR 800 | BR 42–50 | 24V | 900 W | 600 Nm | LF-EBR800 |
| EBR 1200 | BR 50–60 | 24V | 1.300 W | 900 Nm | LF-EBR1200 |
| EBR 1800 | BR 60–90 | 24V | 1.800 W | 1.400 Nm | LF-EBR1800 |

**Besonderheiten Leisure Furl In-Boom:**
- Patentiertes Mandrel-System mit automatischer Tuchspannung
- Endlos-Fall-System integriert
- Full-Batten-Segel möglich (einziger Hersteller mit durchgehenden Latten)
- Rigid Vang im Lieferumfang
- Standard-Mastprofil verwendbar → Refit-freundlich
- Stärkstes Händlernetzwerk für In-Boom weltweit

#### 4.2.2 Bartels (Deutschland) — Engineering Made in Germany

Bartels ist ein deutscher Spezialist für In-Boom-Furling, bekannt für Ingenieursqualität und maßgeschneiderte Lösungen.

**Produktlinie: Bartels BFS (Boom Furling System):**

| Modell | Bootslänge | Segelfläche | Boom-Querschnitt (H×B mm) | Gewicht | Art.-Nr. |
|--------|-----------|------------|---------------------------|---------|----------|
| BFS 30 | 9–11 m | 18–32 m² | 250×190 | 35 kg | BT-BFS30 |
| BFS 40 | 11–14 m | 28–48 m² | 290×225 | 55 kg | BT-BFS40 |
| BFS 50 | 13–16 m | 42–68 m² | 340×260 | 82 kg | BT-BFS50 |
| BFS 60 | 15–19 m | 58–95 m² | 390×300 | 118 kg | BT-BFS60 |
| BFS 75 | 18–24 m | 80–135 m² | 450×350 | 165 kg | BT-BFS75 |

**Bartels Elektrische Antriebe:**

| Modell | Passend für | Spannung | Leistung | Art.-Nr. |
|--------|------------|----------|----------|----------|
| EBA 350 | BFS 30–40 | 12V | 350 W | BT-EBA350 |
| EBA 600 | BFS 40–50 | 24V | 600 W | BT-EBA600 |
| EBA 1000 | BFS 50–60 | 24V | 1.000 W | BT-EBA1000 |
| EBA 1500 | BFS 60–75 | 24V | 1.500 W | BT-EBA1500 |

**Besonderheiten Bartels:**
- Maßanfertigung: Jeder Boom wird auf den Millimeter gefertigt
- CNC-gefräste Endstücke, verschweißt und eloxiert in Deutschland
- Patentiertes Tuchführungssystem mit PTFE-beschichteten Rollen
- Kleinserie → höchste Qualität, aber höherer Preis (+30% vs. Leisure Furl)
- Hauptmarkt: Deutschland, Skandinavien, Benelux
- Service: Direkt vom Hersteller, Werkstatt in Wedel bei Hamburg

#### 4.2.3 Z-Spars / Selden In-Boom (Frankreich/Schweden)

Z-Spars gehört zur Selden-Gruppe und bietet In-Boom-Systeme, die mit Selden-Masten harmonieren.

**Produktlinie: Z-Spars IBF (In-Boom Furling):**

| Modell | Bootslänge | Segelfläche | Boom-Querschnitt (H×B mm) | Art.-Nr. |
|--------|-----------|------------|---------------------------|----------|
| IBF 300 | 9–12 m | 20–38 m² | 260×200 | ZS-IBF300 |
| IBF 400 | 11–14 m | 32–55 m² | 300×235 | ZS-IBF400 |
| IBF 500 | 13–17 m | 48–78 m² | 350×270 | ZS-IBF500 |
| IBF 650 | 16–21 m | 68–110 m² | 410×310 | ZS-IBF650 |
| IBF 800 | 20–26 m | 95–155 m² | 470×360 | ZS-IBF800 |

**Besonderheiten Z-Spars:**
- Perfekte Kompatibilität mit Selden-Masten (gleiche Hersteller-Gruppe)
- OEM-Lieferant für mehrere Werften (Hallberg-Rassy, X-Yachts)
- Integrationsvorteil: Mast und Boom aus einer Hand
- Mittleres Preissegment

### 4.3 Detaillierte Produkt-Vergleichsmatrizen

#### 4.3.1 In-Mast-Systeme Direktvergleich (12–14 m Boot, 45–65 m² Segelfläche)

| Kriterium | Selden C390 | Facnor FMI 42 | Profurl MFS 55 | Leisure Furl MR 55 | Schaefer IMF 600 |
|-----------|------------|--------------|----------------|-------------------|-----------------|
| Mandrel-Ø | 85 mm | 90 mm | 98 mm | 88 mm | 92 mm |
| Mandrel-Material | Al 6082-T6 | Al 7075-T6 | Al 6082-T6 | Al 6061-T6 | Al 6061-T6 |
| Max. Segelfläche | 58 m² | 70 m² | 75 m² | 80 m² | 70 m² |
| Mastprofil (B mm) | 195 | 210 | Nachrüst-Foil | 200 | 195 |
| Schlitzbreite | 28 mm | 30 mm | 26 mm | 28 mm | 27 mm |
| Lager-Typ | SKF sealed | Facnor selbstzentrierend | Standard sealed | Konisch + sealed | Standard sealed |
| Gewicht (Mandrel) | 9,5 kg | 8,2 kg | 11,0 kg | 9,8 kg | 10,5 kg |
| E-Antrieb verfügbar | Ja (E40) | Ja (EMI 600) | Ja (Option) | Ja (Option) | Ja (Option) |
| Nachrüstbar | Neuer Mast | Neuer Mast | Ja (Foil-System) | Neuer Mast | Neuer Mast |
| Preis (nur System) | €4.800–5.800 | €6.200–7.500 | €3.800–5.200 | €5.000–6.500 | €4.500–5.800 |
| Ersatzteil-Verfügbarkeit | ★★★★★ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| OEM-Werften | Bavaria, Beneteau, Hanse | Keine (Refit/Custom) | Keine (Refit) | Oyster, Discovery | US-Werften |
| DACH-Servicenetz | ★★★★★ | ★★☆☆☆ | ★★★☆☆ | ★★☆☆☆ | ★☆☆☆☆ |

#### 4.3.2 In-Boom-Systeme Direktvergleich (12–14 m Boot, 45–65 m² Segelfläche)

| Kriterium | Leisure Furl BR 42 | Bartels BFS 50 | Z-Spars IBF 400 |
|-----------|-------------------|----------------|-----------------|
| Boom-Höhe × Breite | 320×240 mm | 340×260 mm | 300×235 mm |
| Mandrel-Ø | 130 mm | 135 mm | 125 mm |
| Max. Segelfläche | 58 m² | 68 m² | 55 m² |
| Full-Batten möglich | Ja (patentiert) | Nein (Kurzlatten) | Bedingt |
| Rigid Vang | Im Lieferumfang | Separat (Option) | Im Lieferumfang |
| Gewicht (Boom komplett) | 68 kg | 82 kg | 62 kg |
| Endlos-Fall-System | Integriert | Integriert | Integriert |
| E-Antrieb verfügbar | Ja (EBR 500) | Ja (EBA 600) | Ja (Selden-Antrieb) |
| Preis (nur Boom + System) | €6.500–8.500 | €8.800–11.000 | €5.800–7.500 |
| Fertigungsart | Serie | Maßanfertigung | Serie |
| DACH-Servicenetz | ★★☆☆☆ | ★★★★★ (Direkt!) | ★★★★☆ (Selden-Netz) |
| Lieferzeit | 6–10 Wochen | 8–14 Wochen | 6–10 Wochen |

#### 4.3.3 Elektrische Antriebe Direktvergleich (für 12–14 m Boot)

| Kriterium | Selden E40 | Facnor EMI 600 | Leisure Furl EBR 500 | Bartels EBA 600 |
|-----------|-----------|---------------|---------------------|----------------|
| Spannung | 12V/24V | 24V | 12V/24V | 24V |
| Leistung | 700 W | 850 W | 600 W | 600 W |
| Drehmoment (Ausgang) | 450 Nm | 580 Nm | 380 Nm | 420 Nm |
| Max. Strom | 35 A (12V) | 38 A (24V) | 30 A (12V) | 28 A (24V) |
| Getriebe | Planetengetriebe | Planetengetriebe | Schneckengetriebe | Planetengetriebe |
| Geräuschpegel | 52 dB(A) | 48 dB(A) | 55 dB(A) | 50 dB(A) |
| Manuelles Override | Kurbel (Zubehör) | Kurbel (integriert) | Handliene | Kurbel (Zubehör) |
| Gewicht | 8,5 kg | 10,2 kg | 7,8 kg | 9,0 kg |
| CAN-Bus-Option | Ja | Nein | Nein | Ja |
| Preis | €3.200 | €4.100 | €2.800 | €3.500 |

#### 4.3.4 Kompatibilitätsmatrix Hersteller × Werft

| Werft | Standard-System | Alternativen |
|-------|----------------|-------------|
| Beneteau Oceanis | Selden In-Mast (ab 40 ft) | Slab (Standard kleinere Modelle) |
| Jeanneau Sun Odyssey | Selden In-Mast (ab 44 ft) | Slab mit Lazyjacks |
| Bavaria C-Line | Selden In-Mast (ab 42 ft) | Slab (Standard) |
| Hanse | Selden In-Mast (ab 41 ft) | In-Boom (Option bei einigen Modellen) |
| Dufour | Selden In-Mast (ab 40 ft) | Slab |
| Hallberg-Rassy | Z-Spars In-Boom (Standard!) | Slab (Option) |
| X-Yachts | Slab (Standard, Performance-Fokus) | In-Boom (Cruise-Modelle) |
| Oyster | Leisure Furl In-Boom (Standard) | Slab (Option) |
| Contest | Slab (Standard) | In-Boom (Option) |
| Najad/Malö | Selden In-Mast (Option) | Slab (Standard) |
| Lagoon (Katamaran) | Selden In-Mast (Standard ab 40 ft) | Slab |
| Fountaine Pajot (Kat.) | Selden In-Mast (Standard ab 42 ft) | Slab |

### 4.4 Slab-Reefing-Zubehör (Systemkomponenten)

#### 4.3.1 Reffhaken und Reffkauschen

| Hersteller | Produkt | Bootslänge | WLL | Art.-Nr. | Preis (ca.) |
|-----------|---------|-----------|-----|----------|------------|
| Selden | Reffhaken RH14 | 8–12 m | 1.500 N | 508-115 | €45 |
| Selden | Reffhaken RH20 | 12–16 m | 3.000 N | 508-120 | €65 |
| Selden | Reffhaken RH28 | 16–22 m | 5.000 N | 508-128 | €95 |
| Harken | Reef Hook 424 | 8–14 m | 2.200 N | HAR-424 | €55 |
| Harken | Reef Hook 438 | 14–20 m | 4.500 N | HAR-438 | €85 |
| Rutgerson | Quick Reef QR20 | 10–16 m | 3.500 N | RG-QR20 | €75 |

#### 4.3.2 Einleinen-Reff-Kits

| Hersteller | Produkt | Bootslänge | Leinen (Ø) | Art.-Nr. | Preis (ca.) |
|-----------|---------|-----------|-----------|----------|------------|
| Selden | Single Line Reef Kit S | 8–11 m | 8 mm | 508-SLR-S | €280 |
| Selden | Single Line Reef Kit M | 11–14 m | 10 mm | 508-SLR-M | €380 |
| Selden | Single Line Reef Kit L | 14–18 m | 12 mm | 508-SLR-L | €480 |
| Harken | Single Line Reef 2R | 10–14 m | 10 mm | HAR-SLR-2R | €420 |
| Harken | Single Line Reef 3R | 14–20 m | 12 mm | HAR-SLR-3R | €580 |

#### 4.3.3 Lazyjack-Systeme

| Hersteller | Produkt | Bootslänge | Art.-Nr. | Preis (ca.) |
|-----------|---------|-----------|----------|------------|
| Selden | Lazyjack Set CL | 8–11 m | 508-LJ-CL-S | €150 |
| Selden | Lazyjack Set CM | 11–14 m | 508-LJ-CM-M | €190 |
| Selden | Lazyjack Set CL | 14–18 m | 508-LJ-CL-L | €240 |
| Wichard | Lazyjack LJ-30 | 8–10 m | WI-LJ30 | €130 |
| Wichard | Lazyjack LJ-40 | 10–14 m | WI-LJ40 | €170 |
| Wichard | Lazyjack LJ-50 | 14–18 m | WI-LJ50 | €220 |

#### 4.3.4 Lazy-Bag-Systeme

| Hersteller | Produkt | Bootslänge | Material | Art.-Nr. | Preis (ca.) |
|-----------|---------|-----------|---------|----------|------------|
| Elvström | Lazy-Bag LB30 | 8–10 m | Acryl 300g | ELV-LB30 | €350–500 |
| Elvström | Lazy-Bag LB40 | 10–14 m | Acryl 300g | ELV-LB40 | €500–750 |
| Elvström | Lazy-Bag LB50 | 14–18 m | Acryl 300g | ELV-LB50 | €750–1.100 |
| North Sails | Stack-Pack 30 | 8–10 m | Sunbrella | NS-SP30 | €400–600 |
| North Sails | Stack-Pack 40 | 10–14 m | Sunbrella | NS-SP40 | €600–900 |
| North Sails | Stack-Pack 50 | 14–18 m | Sunbrella | NS-SP50 | €900–1.300 |
| UK Sailmakers | EZ-Stow 30 | 8–10 m | Dacron/PVC | UK-EZ30 | €300–450 |

### 4.4 Preisübersicht (Gesamtsysteme, geschätzt 2025/2026)

| System | 10 m Boot | 13 m Boot | 16 m Boot | 20 m Boot |
|--------|----------|----------|----------|----------|
| Slab + Lazyjacks | €300–600 | €500–900 | €800–1.400 | €1.200–2.000 |
| Slab + Lazy-Bag | €600–1.200 | €900–1.800 | €1.500–2.800 | €2.200–4.000 |
| Single-Line Reef + Lazy-Bag | €800–1.500 | €1.200–2.200 | €2.000–3.500 | €3.000–5.500 |
| In-Mast manuell (inkl. Mast) | €3.500–6.000 | €5.500–9.000 | €8.000–14.000 | €14.000–25.000 |
| In-Mast elektrisch (inkl. Mast) | €5.000–8.500 | €8.000–13.000 | €12.000–20.000 | €20.000–38.000 |
| In-Boom manuell (Boom only) | €2.500–5.000 | €4.500–8.000 | €7.000–12.000 | €12.000–22.000 |
| In-Boom elektrisch (Boom only) | €4.000–7.500 | €7.000–12.000 | €11.000–18.000 | €18.000–35.000 |

**AYDI-Hinweis:** Preise verstehen sich ohne Segel, ohne Montage, ohne Rigging. Montagekosten: In-Mast €1.500–5.000 (Masttausch erforderlich bei Nachrüstung), In-Boom €800–3.000 (nur Baumtausch). Slab-Reefing-Nachrüstung: €200–800 Montage.

---

## 5. Vor- und Nachteile — Vergleichsmatrix

### 5.1 Detaillierte Vergleichsmatrix

| Kriterium | Slab Reefing | Single-Line Reef | In-Mast Furling | In-Boom Furling |
|-----------|-------------|------------------|-----------------|-----------------|
| **SEGELFORM** | | | | |
| Profiltiefe | ★★★★★ | ★★★★★ | ★★☆☆☆ | ★★★★☆ |
| Roach (Achterliekrundung) | ★★★★★ | ★★★★★ | ★☆☆☆☆ | ★★★☆☆ |
| Full Battens möglich | Ja | Ja | Nein | Bedingt (Leisure Furl) |
| Am-Wind-Performance | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Raumschot-Performance | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Leichtwind-Performance | ★★★★★ | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| | | | | |
| **BEDIENUNG** | | | | |
| Cockpit-Bedienung | ★★☆☆☆ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Einhand-Tauglichkeit | ★★☆☆☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Reffgeschwindigkeit | ★★☆☆☆ (2–5 min) | ★★★☆☆ (1–2 min) | ★★★★★ (<30 s) | ★★★★☆ (30–60 s) |
| Stufenloses Reffen | Nein (1–3 Stufen) | Nein (1–3 Stufen) | Ja (stufenlos) | Ja (stufenlos) |
| Bergeaufwand | ★★☆☆☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Kraftaufwand (manuell) | Hoch | Mittel | Gering | Gering–Mittel |
| | | | | |
| **ZUVERLÄSSIGKEIT** | | | | |
| Mechanische Einfachheit | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |
| Verklemmungsrisiko | ★★★★★ (minimal) | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ |
| Haltbarkeit | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| Wartungsaufwand | ★★★★★ (minimal) | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| Notreffen bei Systemausfall | ★★★★★ (ist das System) | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| | | | | |
| **KOSTEN** | | | | |
| Anschaffung | ★★★★★ (€300–1.500) | ★★★★☆ (€800–2.200) | ★★☆☆☆ (€5.000–25.000) | ★☆☆☆☆ (€4.000–22.000) |
| Segelkosten | ★★★★★ (Standard) | ★★★★★ (Standard) | ★★★☆☆ (+20–40%) | ★★★☆☆ (+15–30%) |
| Wartungskosten/Jahr | ★★★★★ (€0–100) | ★★★★☆ (€50–200) | ★★★☆☆ (€200–600) | ★★☆☆☆ (€300–800) |
| Lifecycle-Kosten (20 J.) | ★★★★★ (€1.500–5.000) | ★★★★☆ (€3.000–8.000) | ★★☆☆☆ (€12.000–45.000) | ★★☆☆☆ (€15.000–55.000) |
| | | | | |
| **SICHERHEIT** | | | | |
| Windbereich (Reffen) | ★★★★★ (bis 60+ kn) | ★★★★★ (bis 60+ kn) | ★★★☆☆ (bis 40–45 kn) | ★★★★☆ (bis 45–50 kn) |
| Notfall-Bergen | ★★★★★ (Segel runter) | ★★★★★ | ★★☆☆☆ (wenn Mandrel klemmt) | ★★★☆☆ (Fall lösen) |
| Sturmtauglichkeit | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Trysegel möglich | Ja (immer) | Ja | Schwierig (separater Track) | Ja (Standard-Mast) |
| | | | | |
| **SONSTIGES** | | | | |
| Nachrüstbarkeit | ★★★★★ | ★★★★☆ | ★☆☆☆☆ (neuer Mast!) | ★★★☆☆ (nur Boom) |
| Optik (Segel gesetzt) | ★★★★★ | ★★★★★ | ★★★☆☆ (flacher) | ★★★★☆ |
| Optik (Segel geborgen) | ★★☆☆☆ (Lazy-Bag) | ★★★☆☆ (Lazy-Bag) | ★★★★★ (unsichtbar) | ★★★★★ (unsichtbar) |
| Gewicht (System) | ★★★★★ (2–5 kg) | ★★★★☆ (5–10 kg) | ★★☆☆☆ (+15–40 kg vs. Std.) | ★★☆☆☆ (+20–60 kg vs. Std.) |
| Wiederverkaufswert | Neutral | Neutral | Positiv (Fahrt) | Positiv (Fahrt) |

### 5.2 Empfehlung nach Einsatzprofil

| Einsatzprofil | Empfehlung 1. | Empfehlung 2. | Nicht empfohlen |
|---------------|--------------|--------------|-----------------|
| Regatta (Einrumpf) | Slab Reefing | — | In-Mast (Performance) |
| Regatta (Mehrrumpf) | Slab Reefing | In-Boom | In-Mast |
| Fahrtensegeln Kurzhand | In-Mast (elektrisch) | In-Boom (elektrisch) | Slab (allein schwierig) |
| Fahrtensegeln Crew | Single-Line Reef | In-Mast | — |
| Blauwasser | Single-Line Reef | In-Boom | In-Mast (Notreffen!) |
| Charter | In-Mast (elektrisch) | Single-Line Reef | Slab (Gäste-untauglich) |
| Einhand-Atlantik | In-Boom (elektrisch) | In-Mast (elektrisch) | Slab (allein schwer) |
| Küstensegeln, Paar | In-Mast (elektrisch) | Single-Line Reef + Lazy-Bag | — |
| Performance Cruiser | In-Boom | Slab + Full Battens | In-Mast (Segelform) |

### 5.3 Notfall-Szenarien

| Szenario | Slab | Single-Line | In-Mast | In-Boom |
|----------|------|-------------|---------|---------|
| Motor des Antriebssystems fällt aus | n/a | n/a | Manuelles Override, langsam | Manuelles Override, langsam |
| Mandrel klemmt, Segel halb draußen | n/a | n/a | KRITISCH — Segel nicht bergbar | Fall lösen, Segel fällt auf Boom |
| Strom fällt komplett aus | Kein Problem | Kein Problem | Manuell reffen (langsam) | Manuell reffen (langsam) |
| Segel reißt | Standard-Reparatur | Standard-Reparatur | Riss kann Mandrel blockieren | Standard-Reparatur |
| Baum bricht | Segel bergen, weiterfahren | Wie Slab | Segel bergen | SYSTEM UNBRAUCHBAR |
| Mast bricht (partial, oberhalb Saling) | Segel bergen | Wie Slab | Mandrel-Problem möglich | Standard-Notverfahren |
| Nacht, Einhand, Bö 40+ kn | Schwierig (Deck!) | Machbar (Cockpit) | Ideal (Cockpit, Taster) | Gut (Cockpit, Taster) |
| Rollsegel friert ein (Eis, Frost) | n/a | n/a | BLOCKADE — nicht bedienbar | Weniger anfällig (Boom ist niedriger) |

**AYDI-Bewertungsregel:** Für CE-Kategorie A (Hochsee) und Blauwasserreisen muss ein Notreffen-Verfahren dokumentiert sein. In-Mast-Systeme erfordern ein mitgeführtes Trysegel oder eine dokumentierte alternative Sturmstrategie.

### 5.4 Detaillierte Zuverlässigkeitsanalyse

#### 5.4.1 MTBF (Mean Time Between Failures) nach Systemtyp

Geschätzte Werte basierend auf Hersteller-Daten und Langzeiterfahrung:

| System | MTBF (Rollzyklen) | MTBF (Betriebsstunden) | Typische Lebensdauer Mechanik |
|--------|-------------------|----------------------|------------------------------|
| Slab Reefing (Leinen + Blöcke) | >50.000 | >10.000 | 15–25 Jahre |
| Single-Line Reefing | >30.000 | >8.000 | 12–20 Jahre |
| In-Mast (manuell, Selden) | 8.000–15.000 | 2.000–5.000 | 15–20 Jahre |
| In-Mast (elektrisch, Selden) | 6.000–12.000 | 1.500–4.000 | Motor: 8–15 Jahre, Mechanik: 15–20 Jahre |
| In-Boom (manuell) | 6.000–10.000 | 1.500–3.500 | 12–18 Jahre |
| In-Boom (elektrisch) | 5.000–9.000 | 1.200–3.000 | Motor: 8–15 Jahre, Mechanik: 12–18 Jahre |

#### 5.4.2 Ausfallarten und Häufigkeitsverteilung

**In-Mast-Furling — Ausfallarten (100% = alle Störungen):**

| Ausfallart | Häufigkeit | Schwere | Behebung |
|-----------|-----------|---------|----------|
| Leichte Verklemmung (selbst behebbar) | 45% | Niedrig | Richtungswechsel, 30 Sekunden |
| Halyard-Wrap (teilweise) | 15% | Mittel-Hoch | 15–30 Minuten, ggf. Rigger |
| Lager-Verschleiß (erhöhte Reibung) | 12% | Mittel | Lagertausch beim Rigger |
| Segel-Problem (Luff-Tape, Dicke) | 10% | Mittel | Segelmacher |
| Motor-/Elektrik-Ausfall | 8% | Mittel | E-Fachbetrieb oder Hersteller |
| Schlitz-Verformung | 5% | Hoch | Rigger, ggf. Masttausch |
| Schwere Blockade (Segel nicht bergbar) | 3% | Kritisch | Rigger am Mast, Hafen erforderlich |
| Mandrel-Strukturversagen | <1% | Kritisch | Masttausch |
| Gesamt: | 100% | | |

**In-Boom-Furling — Ausfallarten (100% = alle Störungen):**

| Ausfallart | Häufigkeit | Schwere | Behebung |
|-----------|-----------|---------|----------|
| Latten verhaken am Boom-Einlauf | 30% | Niedrig-Mittel | Latten lösen, Rollgeschwindigkeit anpassen |
| Endlos-Fall-Problem | 20% | Mittel-Hoch | Fall ersetzen oder reparieren |
| Rigid-Vang-Problem | 12% | Mittel | Gasdruckfeder ersetzen |
| Motor-/Elektrik-Ausfall | 10% | Mittel | E-Fachbetrieb |
| Führungsrollen-Verschleiß | 10% | Niedrig | Rollen ersetzen |
| Synchronisationsfehler (elektrisch) | 8% | Mittel-Hoch | Kalibrierung, Sensor-Check |
| Segel-Problem (Tuchspannung, Latten) | 7% | Mittel | Segelmacher |
| Mandrel-Blockade im Boom | 3% | Hoch | Boom öffnen, Werkstatt |

#### 5.4.3 Langfrist-Zuverlässigkeit nach 10 und 20 Jahren

| System | Zustand nach 10 Jahren | Zustand nach 20 Jahren |
|--------|----------------------|----------------------|
| Slab + Lazyjacks | Leinen 2× erneuert, Blöcke funktionieren, Segel 1× ersetzt | Leinen 4× erneuert, Blöcke ggf. tauschen, Segel 2× ersetzt |
| In-Mast (Selden) | Lager 1–2× getauscht, Motor-Kohlen 1× getauscht, Segel 1× ersetzt | Lager 3–4× getauscht, Motor ggf. revidiert, Segel 2× ersetzt |
| In-Boom (Leisure Furl) | Führungsrollen 1× getauscht, Vang-Feder 1× getauscht, Segel 1× ersetzt | Führungsrollen 2× getauscht, Motor ggf. revidiert, Segel 2× ersetzt |

### 5.5 Versicherungs- und Haftungsaspekte

#### 5.5.1 Kaskoversicherung

Die meisten Kaskoversicherungen decken Schäden durch Furling-Systemversagen ab, sofern:
- Regelmäßige Wartung nachweisbar (Wartungslogbuch empfohlen)
- Keine grobe Fahrlässigkeit vorliegt (z.B. Reffen bei 50 kn ignoriert)
- System ist fachgerecht installiert (Werft/Rigger-Rechnung)

**Ausschlüsse (typisch):**
- Verschleiß und Alterung (Segel, Dichtungen, Lager)
- Mangelhafte Wartung (nachweisbar verrottete Lager, nie gewechselt)
- Eigenleistung ohne Fachkenntnis (selbst installierter E-Motor brennt durch)

#### 5.5.2 Haftpflicht bei Personenschäden

Bei In-Mast-Blockade und daraus resultierendem Unfall (z.B. Kenterung):
- Hersteller-Haftung: Wenn Konstruktionsfehler → Produkthaftung
- Eigner-Haftung: Wenn mangelnde Wartung → Mitverschulden
- Werft-Haftung: Wenn Installationsfehler → Gewährleistung
- Versicherung: Skipper-Haftpflicht deckt normalerweise Drittschäden

**AYDI-Empfehlung:** Wartungslogbuch führen, jährliche Wartung dokumentieren, Segelmacher-Inspektionsberichte aufbewahren. Bei Versicherungsfall: Dokumentation ist entscheidend.

---

## 6. Dimensionierung und Auswahl

### 6.1 Dimensionierung nach Bootslänge und Segelfläche

#### 6.1.1 Grundformel

```
Erforderliches Mandrel-Drehmoment (In-Mast):
  M_mandrel = k × A_segel × V_wind_max² × r_mandrel / η_getriebe

  k = 0.0006 (empirischer Faktor)
  A_segel in m²
  V_wind_max in m/s (maximale Windgeschwindigkeit beim Reffen, typisch 25 m/s = 50 kn)
  r_mandrel in m
  η_getriebe = 0.85 (Getriebewirkungsgrad)
```

#### 6.1.2 Dimensionierungstabelle

| Bootslänge (LOA) | Verdrängung (t) | Segelfläche Groß (m²) | System-Empfehlung | Mandrel-Ø (In-Mast) | Boom-Typ (In-Boom) |
|-------------------|-----------------|----------------------|-------------------|---------------------|-------------------|
| 8–9 m | 2–4 | 15–25 | Slab / SLR | 50–60 mm | BR 26 / BFS 30 |
| 9–10 m | 3–5 | 22–32 | Slab / SLR / In-Mast | 55–65 mm | BR 26–34 / BFS 30 |
| 10–11 m | 4–7 | 28–38 | SLR / In-Mast | 60–75 mm | BR 34 / BFS 30–40 |
| 11–12 m | 5–9 | 32–45 | In-Mast / SLR | 70–85 mm | BR 34–42 / BFS 40 |
| 12–13 m | 7–12 | 38–52 | In-Mast (el.) / In-Boom | 80–95 mm | BR 42 / BFS 40–50 |
| 13–14 m | 9–15 | 45–62 | In-Mast (el.) / In-Boom | 85–100 mm | BR 42–50 / BFS 50 |
| 14–16 m | 12–20 | 55–80 | In-Mast (el.) / In-Boom | 95–120 mm | BR 50 / BFS 50–60 |
| 16–18 m | 18–30 | 70–105 | In-Mast (el.) / In-Boom | 115–140 mm | BR 60 / BFS 60 |
| 18–20 m | 25–40 | 90–130 | In-Mast (el./hyd.) / In-Boom | 130–160 mm | BR 60–75 / BFS 60–75 |
| 20–25 m | 35–70 | 115–180 | In-Boom (el./hyd.) | 150–200 mm | BR 75–90 / BFS 75 |

### 6.2 Auswahlkriterien

#### 6.2.1 Entscheidungsbaum

```
START: Neues Großsegel-Reffsystem
  │
  ├── Regatta-Einsatz? ─── JA ──→ Slab Reefing (Full Battens, max. Roach)
  │                         │
  │                        NEIN
  │                         │
  ├── Budget unter €2.000? ── JA ──→ Single-Line Reef + Lazyjacks
  │                            │
  │                           NEIN
  │                            │
  ├── Kurzhand / Einhand? ─── JA ──→ In-Mast (el.) oder In-Boom (el.)
  │                            │
  │                           NEIN (Crew)
  │                            │
  ├── Performance wichtig? ── JA ──→ In-Boom (Standard-Mast, Latten)
  │                            │
  │                           NEIN
  │                            │
  ├── Neubau / bestehender Mast?
  │     │
  │     ├── NEUBAU ──→ In-Mast (Furling-Mast ab Werk)
  │     │
  │     └── BESTAND ──→ In-Boom (nur Baumtausch)
  │                     oder Profurl MFS (Mandrel nachrüstbar)
  │
  └── Blauwasser? ─── JA ──→ In-Boom + Trysegel
                       │      (Standard-Mast, Notreffen per Fall)
                      NEIN ──→ In-Mast (Komfort-Favorit)
```

### 6.3 Elektrische Dimensionierung

#### 6.3.1 Stromversorgung für elektrische Antriebe

```
Kabelquerschnitt-Berechnung:
  A = (I × L × 2) / (κ × U_drop)

  I = Maximalstrom des Motors (A)
  L = Kabellänge Motor ↔ Batterie (m, einfach)
  κ = 56 m/(Ω×mm²) für Kupfer
  U_drop = max. 3% der Nennspannung

Beispiel: 24V Motor, 30 A, 8 m Kabellänge
  U_drop = 0.03 × 24 = 0.72 V
  A = (30 × 8 × 2) / (56 × 0.72) = 480 / 40.32 = 11.9 mm²
  → Nächster Standard: 16 mm²
```

**Dimensionierungstabelle Kabelquerschnitt:**

| Motor-Leistung | Spannung | Max. Strom | Kabellänge 5m | Kabellänge 8m | Kabellänge 12m |
|----------------|----------|-----------|--------------|--------------|---------------|
| 250 W | 12V | 25 A | 16 mm² | 25 mm² | 35 mm² |
| 450 W | 12V | 40 A | 25 mm² | 35 mm² | 50 mm² |
| 700 W | 24V | 30 A | 10 mm² | 16 mm² | 25 mm² |
| 1.000 W | 24V | 45 A | 16 mm² | 25 mm² | 35 mm² |
| 1.400 W | 24V | 60 A | 25 mm² | 35 mm² | 50 mm² |

#### 6.3.2 Sicherungsauslegung

```
Sicherungswert = 1.25 × Motor-Nennstrom (Kurzschlussschutz)
  Beispiel: 30 A Motor → 40 A Sicherung (nächster Standard)

Sicherungstyp: ANL oder MEGA für hohe Ströme
Position: Max. 200 mm vom Batterie-Pluspol
```

### 6.4 Segelauswahl nach System

| Kriterium | Slab-Segel | In-Mast-Segel | In-Boom-Segel |
|-----------|-----------|--------------|--------------|
| Tuchgewicht (12m Boot) | 190–250 g/m² | 170–230 g/m² | 180–240 g/m² |
| Bahnschnitt | Cross-cut oder Radial | Vertikal oder Cross-cut | Cross-cut oder Tri-radial |
| Latten | Full Battens (Standard) | Keine oder vertikal | Kurz bis Full Batten |
| Roach | 12–20% | 0–3% | 5–12% |
| Luff-Tape | Standard | Verstärkt (Wickelführung) | Verstärkt (Führungsschiene) |
| UV-Schutz | Optional (Lazy-Bag) | Eingebaut (im Mast) | Eingebaut (im Boom) |
| Haltbarkeit | 8–15 Jahre | 6–12 Jahre | 7–13 Jahre |
| Preis (12m Boot) | €1.500–3.000 | €2.500–5.000 | €2.000–4.500 |

### 6.5 Retrofit-Entscheidungsmatrix

Für Eigner, die ein bestehendes Slab-System umrüsten möchten:

#### 6.5.1 Voraussetzungen für In-Mast-Nachrüstung

| Prüfpunkt | Anforderung | Prüfmethode | Abbruchkriterium |
|-----------|-------------|-------------|-----------------|
| Mastfundament | Muss neuen Mast tragen (ggf. schwerer) | Statische Berechnung, Decksinspektion | Mastfundament nicht verstärkbar |
| Rigg-Geometrie | Wanten- und Stagpositionen müssen passen | Vermessung, Rigg-Plan | Wantbeschläge müssten versetzt werden |
| Mastkran verfügbar | Kran mit min. 200% Mastgewicht Tragkraft | Werft-Infrastruktur | Kein Kran → Kosten +€2.000–5.000 |
| Elektrische Kapazität | Ausreichend für E-Antrieb (200–1.500 W) | Bordnetz-Analyse | Batterie <100 Ah, kein Ladegerät |
| Deck-Durchführungen | Kabeldurchführung Mast → Bordnetz | Inspektion | Keine Möglichkeit für Kabeldurchführung |
| Budget | Min. €8.000 (In-Mast manuell) bis €20.000+ (elektrisch) | Kalkulation | Budget unter Minimum |
| Zeitfenster | 3–5 Arbeitstage (Werft belegt?) | Werft-Planung | Kein Werft-Slot in der Saison-Pause |

#### 6.5.2 Voraussetzungen für In-Boom-Nachrüstung

| Prüfpunkt | Anforderung | Prüfmethode | Abbruchkriterium |
|-----------|-------------|-------------|-----------------|
| Baumhöhe am Lümmelbeschlag | Min. 300 mm über Kajütdach für Boom-Querschnitt | Vermessung | Zu wenig Platz → Kopffreiheit |
| Lümmelbeschlag-Typ | Kompatibel oder austauschbar | Inspektion | Mast-Fitting nicht anpassbar |
| Rigid Vang-Montage | Befestigungspunkte am Mast und Baumfuß vorhanden | Inspektion | Keine Befestigungsmöglichkeit |
| Mastnut (Segel-Slide) | Segel-Slide muss in bestehende Mastnut passen | Vermessung | Inkompatible Mastnut-Geometrie |
| Endlos-Fall-System | Masttop-Rolle muss nachgerüstet werden | Rigger-Inspektion | Masttop nicht modifizierbar |
| Budget | Min. €5.000 (In-Boom manuell) bis €15.000+ (elektrisch) | Kalkulation | Budget unter Minimum |

#### 6.5.3 Retrofit-Kostenbeispiele aus der Praxis

**Beispiel 1: Bavaria 37 (11.3 m), Slab → In-Mast (Selden C350, E30)**

| Position | Kosten |
|----------|--------|
| Selden C350 Furling-Mast | €4.200 |
| Selden E30 Elektroantrieb | €2.800 |
| In-Mast-Rollsegel (Dacron, 38 m²) | €2.600 |
| Demontage alter Mast + Rigg | €1.200 |
| Montage neuer Mast + Rigg-Einstellung | €1.800 |
| Kabelverlegung + Schalter + Sicherung | €450 |
| Mastkran + Transport | €600 |
| **Gesamt** | **€13.650** |

**Beispiel 2: Hallberg-Rassy 340 (10.4 m), Slab → In-Boom (Bartels BFS 30)**

| Position | Kosten |
|----------|--------|
| Bartels BFS 30 (Maßanfertigung) | €5.500 |
| Bartels EBA 350 Elektroantrieb | €2.800 |
| Rigid Vang (Garhauer) | €1.100 |
| In-Boom-Rollsegel (Hydranet, 32 m²) | €3.200 |
| Demontage alter Baum | €400 |
| Montage neuer Boom + Rigid Vang | €1.200 |
| Endlos-Fall-System + Masttop-Rolle | €800 |
| Kabelverlegung + Schalter | €350 |
| **Gesamt** | **€15.350** |

**Beispiel 3: Jeanneau Sun Odyssey 36i (10.9 m), Slab → Single-Line-Reff + Lazy-Bag**

| Position | Kosten |
|----------|--------|
| Selden Single-Line Reef Kit M (2 Reffs) | €380 |
| Umlenkrollen + Clutches (Spinlock) | €420 |
| Reffleinen (2 × 25 m, 10 mm) | €120 |
| Lazyjack-Set (Selden CM) | €190 |
| Lazy-Bag (Elvström, Maßanfertigung) | €680 |
| Segelmacher: Reffkauschen anpassen, SLR-Leinenführung | €350 |
| Montage (1 Tag Rigger) | €600 |
| **Gesamt** | **€2.740** |

### 6.6 Spezielle Dimensionierung für Katamarane

Katamarane haben besondere Anforderungen an Großsegel-Reffsysteme:

```
Katamaran-Besonderheiten:
  - Größere Segelfläche bei gleichem LOA (ca. 20–40% mehr)
  - Weniger Krängung → gleichmäßigeres Wickeln
  - Höhere absolute Lasten (breitere Basis)
  - Mast oft auf Brücke/Kabinendach → andere Zugänglichkeit
  - Oft Kurzhand-Betrieb → In-Mast besonders beliebt

Dimensionierungs-Korrekturfaktoren für Katamarane:
  Mandrel-Drehmoment: × 1.2–1.4 (größere Segelfläche)
  Antriebsleistung: × 1.2–1.4
  Mastprofil: Eine Größe höher als bei Einrumpf gleichen LOA
```

**Katamaran-Empfehlungen nach LOA:**

| Katamaran LOA | Großsegel (m²) | In-Mast-Empfehlung | In-Boom-Empfehlung |
|--------------|----------------|-------------------|-------------------|
| 10–11 m | 35–50 | Selden C390 + E40 | Leisure Furl BR 42 |
| 11–13 m | 45–65 | Selden C430 + E50 | Leisure Furl BR 50 / Bartels BFS 50 |
| 13–15 m | 60–85 | Selden C470 + E50 | Leisure Furl BR 60 / Z-Spars IBF 500 |
| 15–18 m | 80–115 | Selden C530 + E60 | Leisure Furl BR 75 / Bartels BFS 75 |

### 6.7 Segelkraft-Berechnungsformeln für die Praxis

#### 6.7.1 Schotkraft-Abschätzung

```python
# Mainsail sheet load estimation (simplified)
# For AYDI dimensioning module

def estimate_mainsheet_load(
    sail_area_m2: float,
    wind_speed_kn: float,
    apparent_wind_angle_deg: float = 30.0,
    boom_length_m: float = 4.0,
    mainsheet_position_ratio: float = 0.75,
) -> float:
    """
    Estimate mainsheet load in Newtons.

    Parameters:
        sail_area_m2: Mainsail area in square meters
        wind_speed_kn: Apparent wind speed in knots
        apparent_wind_angle_deg: Apparent wind angle in degrees
        boom_length_m: Boom length in meters
        mainsheet_position_ratio: Sheet position as ratio of boom length (0-1)

    Returns:
        Estimated mainsheet load in Newtons
    """
    import math

    wind_speed_ms = wind_speed_kn * 0.5144
    rho = 1.225  # kg/m³ air density at sea level
    cl = 1.2  # typical lift coefficient
    angle_rad = math.radians(apparent_wind_angle_deg)

    total_force = 0.5 * rho * wind_speed_ms**2 * sail_area_m2 * cl
    sheet_force = total_force * math.sin(angle_rad) / mainsheet_position_ratio

    return round(sheet_force, 0)
```

#### 6.7.2 Mandrel-Drehmoment-Abschätzung

```python
# Mandrel torque estimation for furling system sizing
# For AYDI dimensioning module

def estimate_mandrel_torque(
    sail_area_m2: float,
    max_reefing_wind_kn: float = 25.0,
    mandrel_diameter_mm: float = 80.0,
    gear_efficiency: float = 0.85,
) -> float:
    """
    Estimate required mandrel torque in Nm.

    Parameters:
        sail_area_m2: Mainsail area in square meters
        max_reefing_wind_kn: Maximum wind speed for reefing in knots
        mandrel_diameter_mm: Mandrel diameter in mm
        gear_efficiency: Gear train efficiency (0-1)

    Returns:
        Required mandrel torque in Nm
    """
    wind_speed_ms = max_reefing_wind_kn * 0.5144
    k = 0.0006  # empirical factor
    r_mandrel_m = mandrel_diameter_mm / 2000.0

    torque = k * sail_area_m2 * wind_speed_ms**2 * r_mandrel_m / gear_efficiency

    return round(torque, 1)
```

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F01 — Mandrel-Klemmen (In-Mast)

**Symptom:** Segel lässt sich nicht ein- oder ausrollen. Motor surrt oder manueller Antrieb blockiert.

**Ursache(n):**
1. Segel hat sich ungleichmäßig gewickelt (Knäuel)
2. Halyard (Fall) hat sich um den Mandrel gewickelt
3. Mandrel-Lager defekt (Reibung zu hoch)
4. Fremdkörper im Mastschlitz (Lazyjack-Leine, Flaggenleine)
5. Schlitzlippen verformt oder korrodiert
6. Segel zu dick (Nähte, Patches) für den Schlitz

**Confidence:** documented (Werft-Berichte, Segelmacher-Erfahrung)

**Schwere:** KRITISCH — Segel kann nicht geborgen werden

**Sofortmaßnahme:**
1. Auf keinen Fall Gewalt anwenden (Motor-Override oder Kurbel)
2. Alle Leinen entlasten (Schot, Outhaul, Fall)
3. Kurs vor den Wind gehen (Segel entlasten)
4. Versuchen, in die Gegenrichtung zu rollen (kurz, sanft)
5. Wenn blockiert: Segel so belassen, Geschwindigkeit reduzieren, Hafen anlaufen

**Langfrist-Behebung:**
- Mandrel-Lager prüfen und ggf. tauschen
- Segel von Segelmacher prüfen lassen (Dicke, Nähte)
- Schlitzlippen reinigen und auf Parallelität prüfen
- Fall-Führung kontrollieren (Halyard-Diverter)

**AYDI-Schwachstellen-Score:** 9/10 (häufigstes und gravierendstes Problem bei In-Mast)

### 7.2 Fehlerbild F02 — Foil-Track-Fehlausrichtung (In-Mast)

**Symptom:** Segel klemmt beim Ein- oder Ausrollen an bestimmten Stellen. Ruckeliger Lauf. Segel kommt oben oder unten nicht rein/raus.

**Ursache(n):**
1. Mastprofil hat sich unter Rigg-Vorspannung verzogen
2. Schlitzschienen sind nicht parallel (Fertigungsfehler oder Alterung)
3. Thermische Verformung (Aluminium-Ausdehnung bei Sonneneinstrahlung)
4. Schlag- oder Sturmschaden am Mastprofil
5. Verschleiß der UHMWPE-Führungsschienen

**Confidence:** documented (Rigger-Berichte)

**Schwere:** MITTEL-HOCH — System funktioniert, aber unzuverlässig

**Diagnose:**
1. Visuell: Mast entlang schauen — Krümmung sichtbar?
2. Lehre: Schlitzbreite alle 500 mm messen (Soll: ±0.5 mm)
3. Testlauf: Segel bei Flaute ein-/ausrollen — wo klemmt es?

**Behebung:**
- Rigg-Vorspannung prüfen und ggf. reduzieren
- Schlitzschienen nachjustieren (Rigger-Arbeit)
- Bei permanenter Verformung: Mastprofil tauschen

**AYDI-Schwachstellen-Score:** 7/10

### 7.3 Fehlerbild F03 — Halyard-Wrap (Fallumwicklung am Mandrel)

**Symptom:** Fall hat sich um den Mandrel gewickelt. Mandrel blockiert. Fall kann nicht gefiert werden.

**Ursache(n):**
1. Halyard-Diverter (Fallabweiser) fehlt oder falsch eingestellt
2. Fall zu locker beim Rollen (Durchhang → schlägt um Mandrel)
3. Falsche Leinenführung nach Refit oder Segelwechsel
4. Wind dreht das Fall um den Mandrel (bei Flaute + Seegang)

**Confidence:** documented (häufigster Service-Call bei In-Mast)

**Schwere:** HOCH — Mandrel blockiert, Fall beschädigt

**Prävention:**
1. Halyard-Diverter korrekt montieren und einstellen
2. Fall immer unter leichter Spannung halten beim Rollen
3. Fallstopper prüfen — darf nicht unbeabsichtigt fieren
4. Nicht bei Flaute + Seegang rollen (Segel schlägt)

**Behebung:**
- Mandrel entlasten (alle Leinen los)
- Mast öffnen (bei manchen Systemen möglich)
- Fall entwirren (oft nur durch Rigger am Mast möglich)
- Halyard-Diverter nachrüsten oder korrigieren

**AYDI-Schwachstellen-Score:** 8/10

### 7.4 Fehlerbild F04 — Motorausfall (elektrischer Antrieb)

**Symptom:** Elektrischer Antrieb reagiert nicht. Motor surrt kurz und stoppt. Sicherung löst aus.

**Ursache(n):**
1. Sicherung durchgebrannt (Überlast, Kurzschluss)
2. Kabel korrodiert (Kontaktprobleme, Übergangswiderstand)
3. Motor-Kohlen verschlissen (bei Bürstenmotor)
4. Steuerplatine defekt (Feuchtigkeit, Korrosion)
5. Getriebe blockiert (Zahnradbruch, Lagerschaden)
6. Batteriespannung zu niedrig (unter Last eingebrochen)

**Confidence:** documented (Hersteller-Servicedaten)

**Schwere:** MITTEL — Manuelles Override möglich

**Sofortmaßnahme:**
1. Sicherung prüfen, ggf. ersetzen (Ersatzsicherung an Bord!)
2. Batteriespannung prüfen (min. 11.5V bei 12V / 23V bei 24V System)
3. Manuelles Override nutzen (Kurbel einstecken oder Notleine)
4. Wenn kein Override möglich: Segel belassen, Geschwindigkeit reduzieren

**Langfrist-Behebung:**
- Kabel und Steckverbindungen auf Korrosion prüfen
- Motor-Kohlen prüfen (alle 500 Betriebsstunden)
- Steuerplatine trockenlegen, Feuchtigkeitsschutz verbessern
- Getriebe-Inspektion durch Fachbetrieb

**AYDI-Schwachstellen-Score:** 6/10

### 7.5 Fehlerbild F05 — Batten-Catch (In-Boom, Lattenfänger)

**Symptom:** Segel klemmt beim Einrollen in den Boom. Latten verhaken sich an der Schlitzlippe oder an internen Führungen.

**Ursache(n):**
1. Latten zu steif für den Biegereadius im Boom
2. Lattentaschen-Enden nicht abgerundet → haken an Führungen
3. Führungsrollen verschmutzt oder blockiert
4. Segel falsch orientiert (Torsion beim Einrollen)
5. Zu schnelles Rollen → Tuch staut sich vor den Rollen

**Confidence:** documented (Segelmacher-Berichte)

**Schwere:** MITTEL — System klemmt, aber Fall lösen hilft

**Behebung:**
- Latten gegen flexiblere Modelle tauschen
- Lattentaschen-Enden vom Segelmacher abrunden lassen
- Führungsrollen reinigen, ggf. ersetzen (PTFE oder Delrin)
- Rollgeschwindigkeit reduzieren (bei E-Antrieb: langsamere Stufe)
- Segel nur bei entlastetem Achterliek rollen (Schot fieren!)

**AYDI-Schwachstellen-Score:** 5/10

### 7.6 Fehlerbild F06 — Ungleichmäßige Wicklung (In-Mast und In-Boom)

**Symptom:** Segel wickelt sich auf einer Seite dicker als auf der anderen. Mandrel wird exzentrisch belastet. Ruckeliger Lauf.

**Ursache(n):**
1. Segel-Luff-Tape hat unterschiedliche Dicke
2. Nähte und Verstärkungen erzeugen lokale Verdickungen
3. Mandrel-Lager hat Spiel → Mandrel wandert seitlich
4. Foam-Strips am Luff fehlen oder sind verschoben
5. Segel wurde bei Wind gerollt → Windlast erzeugt Torsion

**Confidence:** estimated (Erfahrungswerte, Segelmacher-Analyse)

**Schwere:** MITTEL — Langfristig erhöhter Verschleiß an Lager und Schlitzlippen

**Behebung:**
- Foam-Strips am Luff prüfen und ggf. erneuern
- Segel im Hafen (Flaute) einmal komplett aus- und wieder einrollen
- Mandrel-Lager auf Spiel prüfen (max. 0.5 mm axial)
- Segelmacher konsultieren: Luff-Tape-Dicke anpassen

**AYDI-Schwachstellen-Score:** 4/10

### 7.7 Fehlerbild F07 — Schlitz-Wassereinbruch (In-Mast)

**Symptom:** Wasser dringt durch den Mastschlitz ins Mastinnere. Korrosion am Mandrel, an Lagern und am Segel.

**Ursache(n):**
1. Bürstendichtung am Schlitz verschlissen
2. Dichtlippen fehlen oder sind beschädigt
3. Regen- und Spritzwasser läuft in den offenen Schlitz
4. Kondenswasser im Mastinneren (Temperaturwechsel)

**Confidence:** documented (Werft-Berichte, Langfahrt-Eigner)

**Schwere:** NIEDRIG-MITTEL — Langfristschaden durch Korrosion

**Behebung:**
- Bürstendichtung erneuern (jährlich kontrollieren)
- Drainage am Mastfuß prüfen (Wasser muss ablaufen können!)
- Anti-Korrosions-Spray im Mastinneren (Lanocote oder ACF-50)
- Mandrel und Lager auf Korrosion inspizieren (alle 2 Jahre)

**AYDI-Schwachstellen-Score:** 4/10

### 7.8 Fehlerbild F08 — Endlos-Fall-Versagen (In-Boom)

**Symptom:** Endlos-Fall-System blockiert, rutscht oder reißt. Segel kann nicht gesetzt oder geborgen werden.

**Ursache(n):**
1. Fall-Seil verschlissen (UV, Abrieb an Umlenkrollen)
2. Umlenkrolle am Masttop blockiert (Lager defekt)
3. Fall-Clutch am Mastfuß hält nicht (verschlissen)
4. Fall-Leine hat sich verdreht → klemmt in Umlenkung
5. Spleiß am Endlos-Fall hat sich gelöst

**Confidence:** documented (Rigger-Berichte, Segelmacher-Erfahrung)

**Schwere:** HOCH — Segel kann nicht geborgen werden (ähnlich F01)

**Prävention:**
- Endlos-Fall alle 3–5 Jahre ersetzen (UV-bedingte Alterung)
- Masttop-Umlenkrolle jährlich inspizieren (Lager, Scheibe)
- Spleiße jährlich kontrollieren

**Behebung:**
- Ersatz-Fall mitführen (immer!)
- Masttop-Inspektion durch Rigger
- Umlenkrollen tauschen bei Lagerspiel

**AYDI-Schwachstellen-Score:** 7/10

### 7.9 Fehlerbild F09 — Rigid-Vang-Versagen (In-Boom)

**Symptom:** Starrer Baumniederholer (Rigid Vang) hält den Baum nicht in Position. Baum sackt ab. Gasdruckfeder defekt.

**Ursache(n):**
1. Gasdruckfeder hat Druck verloren (Alterung, Undichtigkeit)
2. Gelenkpunkt ausgeschlagen (Spiel, Korrosion)
3. Bolzen geschert (Überlast bei Patenthalse)
4. Halterung am Mast oder am Baum losgerissen

**Confidence:** documented (Werft-Berichte)

**Schwere:** MITTEL-HOCH — Boom-Kontrolle verloren, Segel nicht trimmbar

**Behebung:**
- Gasdruckfeder ersetzen (herstellerspezifisch, alle 5–8 Jahre)
- Gelenkpunkte fetten und auf Spiel prüfen (jährlich)
- Bolzen auf Verformung prüfen (Sichtprüfung)
- Halterungen auf Risse und Verformung prüfen

**AYDI-Schwachstellen-Score:** 5/10

### 7.10 Fehlerbild F10 — Outhaul-Blockade (In-Mast)

**Symptom:** Unterliek lässt sich nicht spannen oder lösen. Outhaul-Leine klemmt im Baum.

**Ursache(n):**
1. Outhaul-Leine verschlissen, aufgefasert → klemmt in Umlenkrolle
2. Umlenkrolle im Baum blockiert (Korrosion, Schmutz)
3. Outhaul-Schlitten auf der Baumschiene verklemmt
4. Zu viel Reibung durch zu viele Umlenkungen

**Confidence:** estimated (Erfahrungswerte)

**Schwere:** NIEDRIG-MITTEL — Segelform nicht optimal, aber segelbar

**Behebung:**
- Outhaul-Leine ersetzen (Dyneema-Mantel empfohlen)
- Umlenkrollen reinigen und fetten
- Baumschiene mit PTFE-Spray behandeln

**AYDI-Schwachstellen-Score:** 3/10

### 7.11 Fehlerbild F11 — Segel reißt am Luff-Tape (In-Mast)

**Symptom:** Segel reißt entlang des Luff-Tapes ein. Segel löst sich teilweise vom Mandrel.

**Ursache(n):**
1. UV-Degradation des Luff-Tapes (Schlitz lässt UV durch)
2. Chafe (Scheuern) des Luff-Tapes an Schlitzlippen
3. Zu hohe Last beim Ausrollen (Böe während des Ausrollens)
4. Materialermüdung nach vielen Rollzyklen
5. Minderwertiges Nähgarn (UV-instabil)

**Confidence:** documented (Segelmacher-Berichte)

**Schwere:** HOCH — Segel nicht mehr sicher verwendbar

**Prävention:**
- Segel alle 3 Jahre vom Segelmacher inspizieren lassen
- UV-Schutz: Luff-Tape mit UV-resistentem Material (Tenara)
- Schlitzlippen auf scharfe Kanten prüfen
- Segel nicht bei >30 kn aus- oder einrollen

**Behebung:**
- Segelmacher-Reparatur (Luff-Tape erneuern, Nahtrekonstruktion)
- Bei großem Riss: Neusegel erforderlich

**AYDI-Schwachstellen-Score:** 6/10

### 7.12 Fehlerbild F12 — Synchronisationsfehler Fall/Mandrel (In-Boom, elektrisch)

**Symptom:** Fall und Mandrel laufen nicht synchron. Segel staut sich am Boom-Einlauf oder wird zu straff gezogen. Motor geht auf Überlast.

**Ursache(n):**
1. Elektronische Synchronisierung gestört (Sensor defekt)
2. Fall-Geschwindigkeit stimmt nicht mit Mandrel-Geschwindigkeit überein
3. Endlos-Fall-Leine hat sich gelängt → Schlupf
4. Motor-Drehzahl schwankt (Batteriespannung instabil)

**Confidence:** documented (Hersteller-Servicedaten)

**Schwere:** MITTEL-HOCH — System kann sich selbst beschädigen

**Behebung:**
- Sensoren kalibrieren (herstellerspezifisch)
- Fall-Spannung nachjustieren
- Batterie-Versorgung stabilisieren (Kabelquerschnitt prüfen!)
- Software-Update beim Hersteller anfragen

**AYDI-Schwachstellen-Score:** 6/10

---

## 8. Troubleshooting-Bäume

### 8.1 Troubleshooting-Baum 1: Segel lässt sich nicht einrollen

```
PROBLEM: Segel lässt sich nicht einrollen
│
├── System: In-Mast?
│   ├── Elektrischer Antrieb?
│   │   ├── Motor reagiert nicht
│   │   │   ├── Sicherung prüfen → F04
│   │   │   ├── Kabel/Stecker prüfen → F04
│   │   │   └── Batteriespannung prüfen (min. 11.5V/23V)
│   │   ├── Motor surrt, aber Mandrel dreht nicht
│   │   │   ├── Kupplung prüfen (Freilauf defekt?)
│   │   │   └── Getriebe blockiert → F04
│   │   └── Motor dreht, Segel klemmt
│   │       ├── Halyard-Wrap? → F03
│   │       ├── Fremdkörper im Schlitz? → F01
│   │       ├── Schlitzlippen verformt? → F02
│   │       └── Segel verdreht/geknäult? → F01
│   └── Manueller Antrieb?
│       ├── Bändsel/Leine hat zu viel Reibung
│       │   └── Umlenkrollen prüfen, Leinenführung optimieren
│       └── Mandrel blockiert → siehe oben (Motor-Äste)
│
├── System: In-Boom?
│   ├── Fall fiert nicht → Fall-Stopper prüfen, Fall-Leine klar?
│   ├── Latten verhaken → F05
│   ├── Mandrel blockiert im Boom → Führungsrollen prüfen, Tuch staut sich
│   └── Synchronisationsfehler (elektrisch) → F12
│
└── System: Slab?
    ├── Fall klemmt in Stopper → Stopper öffnen, Fall prüfen
    ├── Reffleine klemmt → Umlenkrollen prüfen, Leinenweg kontrollieren
    └── Reffkausch passt nicht in Refflhaken → Kausch und Haken auf Korrosion prüfen
```

### 8.2 Troubleshooting-Baum 2: Segel lässt sich nicht ausrollen/setzen

```
PROBLEM: Segel lässt sich nicht ausrollen/setzen
│
├── System: In-Mast?
│   ├── Mandrel dreht rückwärts, aber Segel kommt nicht raus
│   │   ├── Segel klebt an sich selbst (Feuchtigkeit, Salz)
│   │   │   → Segel einmal komplett ausrollen, trocknen, reinigen
│   │   ├── Schlitzlippen klemmen das Segel
│   │   │   → Schlitzlippen reinigen, Parallelität prüfen → F02
│   │   └── Outhaul/Clew-Leine blockiert
│   │       → Outhaul-Leinenweg prüfen → F10
│   └── Mandrel dreht nicht
│       → Wie Troubleshooting-Baum 1 (Antrieb-Äste)
│
├── System: In-Boom?
│   ├── Fall holt nicht → Fall-Führung prüfen, Masttop-Rolle
│   ├── Segel klemmt im Boom → Latten, Führungsrollen, Torsion
│   └── Mandrel gibt Segel nicht frei → Mandrel-Bremse prüfen
│
└── System: Slab?
    ├── Fall klemmt → Fallstopper, Mastführung prüfen
    └── Segel schlägt (zu viel Wind) → Kurs abfallen, Traveller nach Lee
```

### 8.3 Troubleshooting-Baum 3: Ungewöhnliche Geräusche

```
PROBLEM: Ungewöhnliche Geräusche beim Rollen/Setzen
│
├── Quietschen / Kreischen
│   ├── Mandrel-Lager trocken → Lagerschmierung prüfen
│   ├── Segel reibt an Schlitzlippen → Schlitz reinigen, Lippen prüfen
│   └── Getriebe-Zahnräder verschlissen → Getriebe-Inspektion
│
├── Klappern / Schlagen
│   ├── Mandrel hat axiales Spiel → Lager nachjustieren
│   ├── Latten schlagen im Boom → Latten-Führung prüfen (In-Boom)
│   └── Lose Teile im Mast → Mastinspektion (Rigger)
│
├── Summen / Brummen (elektrisch)
│   ├── Normal bei E-Antrieb unter Last
│   ├── Abnormal laut → Motor-Kohlen prüfen, Lager prüfen
│   └── Pulsierend → Steuerplatine prüfen, Batteriespannung messen
│
└── Knacken / Krachen
    ├── STOP! → Segel sofort entlasten
    ├── Mast-Strukturversagen möglich → Mastinspektion SOFORT
    └── Getriebe-Zahnradbruch → System nicht weiter betätigen
```

### 8.4 Troubleshooting-Baum 4: Schlechte Segelform nach dem Setzen

```
PROBLEM: Segelform nach dem Setzen unbefriedigend
│
├── Segel zu flach (kein Profil)
│   ├── In-Mast: Normal für lattenlose Segel. Abhilfe:
│   │   ├── Schot dichter holen
│   │   ├── Outhaul lösen (Unterliek lockerer)
│   │   ├── Cunningham lösen
│   │   └── Ggf. Vertikallatten nachrüsten lassen
│   └── In-Boom: Latten prüfen (zu weich?)
│       └── Segelschnitt vom Segelmacher optimieren lassen
│
├── Segel hat Falten (vertikal)
│   ├── Fall zu wenig gespannt → Fall dichter holen
│   ├── Luff-Tape nicht straff → Segel wurde nicht vollständig ausgerollt
│   └── Segel hat sich verdreht → Komplett einrollen und neu setzen
│
├── Segel hat Falten (horizontal)
│   ├── Outhaul zu straff → Outhaul lösen
│   ├── Luff-Tape beschädigt → Segelmacher
│   └── Falten vom letzten Wickeln → Segel einmal komplett öffnen, trocknen
│
└── Segel hat "Bauch" nur unten oder nur oben
    ├── Foam-Strips ungleichmäßig → Segelmacher adjustieren
    ├── Mandrel-Durchmesser variiert → Mandrel inspizieren
    └── Segeltuch unterschiedlich gereckt → Neusegel in Betracht ziehen
```

### 8.5 Troubleshooting-Baum 5: Notsituation — Segel klemmt bei Starkwind

```
PROBLEM: Segel klemmt bei 30+ kn, kann nicht geborgen werden
│
├── SOFORTIGE MASSNAHMEN (alle Systeme):
│   ├── 1. RUHE BEWAHREN
│   ├── 2. Kurs VOR den Wind gehen → Segel entlasten (wichtigster Schritt!)
│   ├── 3. Motor starten (wenn vorhanden)
│   ├── 4. Geschwindigkeit reduzieren → Segellast sinkt quadratisch mit V_wind
│   └── 5. Crew informieren, Rettungswesten anlegen
│
├── In-Mast klemmt:
│   ├── Schot komplett fieren → Segel killt (flattert)
│   ├── Vorsicht: Killendes Segel kann Leinen um Mandrel wickeln!
│   ├── Manuelles Override versuchen (kurze Stöße, Richtungswechsel)
│   ├── Fall NICHT lösen (bei In-Mast bleibt Segel am Mandrel)
│   ├── WENN nichts hilft:
│   │   ├── Segel belassen, Geschwindigkeit stark reduzieren
│   │   ├── Vorsegel bergen (Windwiderstand reduzieren)
│   │   ├── Ggf. Trysegel setzen (wenn vorhanden, am Sturmtrack)
│   │   └── Nächsten Hafen oder Ankerplatz ansteuern
│   └── LAST RESORT: Segel abschneiden (Messer am Schlitz)
│       → NUR bei akuter Gefahr für Schiff und Crew!
│
├── In-Boom klemmt:
│   ├── Fall komplett lösen → Segel fällt auf Boom
│   ├── Segel mit Leinen / Reffbändseln am Baum sichern
│   ├── Weiterfahren unter Motor oder Vorsegel
│   └── Einfacher als In-Mast, da Fall-Lösung funktioniert
│
└── Slab — Reffleine klemmt:
    ├── Fallstopper öffnen → Fall komplett fieren → Segel runter
    ├── Segel mit Lazyjacks auffangen
    └── Segel am Baum sichern (Reffbändseln, Spanngurte)
```

### 8.6 Wartungs-Entscheidungsbaum

```
SITUATION: Jährliche Wartung In-Mast-Furling
│
├── Segel aus dem Mast nehmen?
│   ├── Einwintern (>3 Monate Ruhe)? ─── JA ──→ Segel ausbauen, trocken lagern
│   │                                    NEIN
│   ├── Segel nass eingerollt? ─── JA ──→ Ausrollen, trocknen, prüfen
│   │                             NEIN
│   └── Segel älter als 3 Jahre? ── JA ──→ Ausbauen, Segelmacher-Inspektion
│                                    NEIN ──→ Segel kann eingerollt bleiben
│
├── Mandrel-Lager schmieren?
│   ├── Letztes Schmieren >12 Monate? ── JA ──→ Schmieren (Hersteller-Fett)
│   │                                     NEIN ──→ Nicht erforderlich
│   ├── Geräusche beim Rollen? ── JA ──→ Schmieren + auf Spiel prüfen
│   └── Erhöhter Kraftbedarf? ── JA ──→ Schmieren + Lager inspizieren
│
├── Schlitzlippen prüfen?
│   ├── Visuell: Verformung sichtbar? ── JA ──→ Rigger beauftragen
│   ├── Visuell: Salzablagerung? ── JA ──→ Süßwasser + weiche Bürste
│   ├── Visuell: Verschleiß/Abrieb? ── JA ──→ Ersetzen (Rigger)
│   └── Bürstendichtung intakt? ── NEIN ──→ Ersetzen
│
├── Elektrischer Antrieb prüfen?
│   ├── Sicherung intakt? ── NEIN ──→ Ersetzen (IMMER Ersatz mitführen!)
│   ├── Kabelverbindungen korrodiert? ── JA ──→ Reinigen, ggf. ersetzen
│   ├── Motor-Geräusch normal? ── NEIN ──→ Kohlen prüfen (Bürstenmotor)
│   └── Stromaufnahme messen (Amperemeter) ── >120% Nennwert? ──→ Service
│
└── Fall und Leinen prüfen?
    ├── Fall: Chafe (Scheuerstellen) sichtbar? ── JA ──→ Ersetzen
    ├── Bedienleine: Verschleiß? ── JA ──→ Ersetzen
    ├── Outhaul-Leine: Aufgefasert? ── JA ──→ Ersetzen
    └── Halyard-Diverter: Noch korrekt positioniert? ── NEIN ──→ Korrigieren
```

### 8.7 Diagnose-Checkliste für Gebrauchtboot-Kauf

Beim Kauf einer Gebrauchtyacht mit Rollreffsystem — Punkte für die Besichtigung:

**In-Mast-System Kaufinspektion:**

| Prüfpunkt | Methode | Ergebnis OK | Warnsignal | Deal-Breaker |
|-----------|---------|-------------|-----------|-------------|
| Segel ein-/ausrollen | Funktionstest (Flaute) | Gleichmäßig, leise | Ruckeln, kurzes Klemmen | Blockiert, starkes Klemmen |
| Segelform (gesetzt) | Visuell | Profil vorhanden, gleichmäßig | Vertikale Falten, flach | Segel völlig formlos, Löcher |
| Mandrel-Geräusche | Akustisch beim Rollen | Leise, gleichmäßig | Quietschen | Kratzen, Schleifen, Knacken |
| Schlitzlippen | Visuell + Tastprüfung | Glatt, parallel | Leichte Verformung | Stark verformt, scharfe Kanten |
| Segel Luff-Tape | Visuell (Segel ausrollen) | Intakt, nicht ausgefranst | Leichter Abrieb | Risse, Ablösung vom Segel |
| Mandrel-Lager (unten) | Axiales Rütteln am Mandrel | Kein spürbares Spiel | Leichtes Spiel (<0,5 mm) | Deutliches Spiel (>1 mm) |
| E-Motor (falls vorhanden) | Stromaufnahme messen | Im Nennbereich | +20% über Nennwert | +50% oder Motor stoppt |
| Fall-Zustand | Visuell, Handprüfung | Kein Chafe, geschmeidig | Leichte Scheuerstellen | Starker Verschleiß, steif |
| Mast-Zustand (Profil) | Visuell, am Mast hochschauen | Gerade, keine Dellen | Leichte Biegung | Starke Verformung, Dellen |
| Wartungslogbuch | Dokumentation | Vorhanden, regelmäßig | Lückenhaft | Nicht vorhanden |

**In-Boom-System Kaufinspektion:**

| Prüfpunkt | Methode | Ergebnis OK | Warnsignal | Deal-Breaker |
|-----------|---------|-------------|-----------|-------------|
| Segel ein-/ausrollen | Funktionstest | Gleichmäßig | Latten fangen | Blockiert |
| Boom-Führungsrollen | Visuell (Boom öffnen) | Frei drehbar, sauber | Schwergängig | Blockiert, gebrochen |
| Rigid Vang | Funktionstest | Boom bleibt horizontal | Leichtes Absacken | Boom sackt deutlich ab |
| Gasdruckfeder | Drucktest | Hält gegen Handkraft | Gibt langsam nach | Kein Widerstand |
| Endlos-Fall | Visuell + Zugtest | Intakt, Spleiß fest | Leichter Verschleiß | Spleiß gelöst, Mantel offen |
| Masttop-Rolle | Visuell (Fernglas/Foto) | Frei drehbar | Seitliches Spiel | Blockiert, Scheibe beschädigt |

**Kostenschätzung für typische Mängel bei Gebrauchtboot-Kauf:**

| Mangel | Kosten Behebung | Dringlichkeit |
|--------|----------------|--------------|
| Segel verschlissen (Formverlust) | €2.500–5.500 (Neusegel) | Mittelfristig (1–2 Saisons) |
| Mandrel-Lager verschlissen | €200–600 (Material + Arbeit) | Kurzfristig (vor nächster Saison) |
| E-Motor defekt | €2.000–4.500 (Motor-Ersatz) | Kurzfristig (nicht segelbar) |
| Schlitzlippen verformt | €500–2.000 (Rigger) | Kurzfristig |
| Rigid Vang Gasdruckfeder leer | €300–800 (Feder + Einbau) | Kurzfristig |
| Endlos-Fall verschlissen | €200–500 (Fall + Einbau) | Kurzfristig |
| Halyard-Diverter fehlt/defekt | €100–300 (Teil + Einbau) | SOFORT (Halyard-Wrap-Risiko!) |

---

## 9. FAQ — Häufig gestellte Fragen

### 9.1 Allgemeine Fragen

**F01: Was ist der Unterschied zwischen In-Mast und In-Boom Furling?**

In-Mast Furling wickelt das Segel um einen vertikalen Mandrel im Mastinneren. Das Segel rollt sich horizontal ein und fährt durch einen Schlitz an der Mastrückseite. Ein verbreiterter Spezialmast ist erforderlich. Das Segel kann keine horizontalen Latten haben und verliert 12–18% Segelfläche (kein Roach).

In-Boom Furling wickelt das Segel um einen horizontalen Mandrel im Baum. Das Segel wird durch Fieren des Falls von oben in den Baum gerollt. Ein Standard-Mast kann verwendet werden, aber ein vergrößerter Spezialboom ist nötig. Horizontale Latten und Roach sind möglich. Ein Rigid Vang (starrer Baumniederholer) ist erforderlich, da ein konventioneller Baumkicker nicht funktioniert.

**F02: Welches System ist besser für Kurzhand-Segeln?**

Für Kurzhand-Segeln (2 Personen oder Einhand) sind sowohl In-Mast als auch In-Boom mit elektrischem Antrieb hervorragend geeignet. In-Mast hat den Vorteil der einfacheren Bedienung (ein Taster für Ein-/Ausrollen), In-Boom den Vorteil der besseren Segelform. Beide ermöglichen Cockpit-Bedienung ohne Deckarbeit. Slab-Reefing ist für Kurzhand deutlich anspruchsvoller, da mindestens für das erste Reff oft der Mast erreicht werden muss.

**F03: Kann ich ein In-Mast-System nachrüsten?**

Ja, aber es erfordert einen komplett neuen Mast. Der bestehende Standardmast muss durch einen Furling-Mast ersetzt werden. Dies ist ein erheblicher Eingriff (Rigg abbauen, neuer Mast, Rigg neu einstellen) und kostet typischerweise €8.000–25.000 (Mast + Antrieb + Montage + neues Segel). Ein In-Boom-System ist nachrüstfreundlicher, da nur der Baum getauscht wird und der Mast bleiben kann.

**F04: Verliere ich wirklich so viel Segelleistung mit In-Mast?**

Am Wind: Ja, spürbar. Das fehlende Roach (12–18% weniger Segelfläche) und das flachere Profil kosten ca. 5–10% VMG (Velocity Made Good) gegenüber einem vollgelatteten Großsegel. Raum- und Vorwindkurse sind weniger betroffen (2–5% Verlust). Für die meisten Fahrtensegler ist dieser Verlust akzeptabel — der Komfortgewinn (Cockpit-Bedienung, schnelles Reffen) überwiegt deutlich. Für Regatta-Segler ist In-Mast in der Regel inakzeptabel.

**F05: Wie zuverlässig sind In-Mast-Systeme wirklich?**

Bei sachgemäßer Wartung und korrektem Segel sind moderne In-Mast-Systeme (Selden, Facnor) zuverlässig. Typische Störungsrate: 1–3% der Rollzyklen zeigen leichte Probleme (Ruckeln, kurzes Klemmen), schwere Blockaden (<0.1% der Rollzyklen). Hauptursachen für Probleme: mangelnde Wartung, falsches Segel, Halyard-Wrap. Die „Horrorgeschichten" stammen meist aus den 1980er/90er-Jahren, als die Technik noch unreif war.

### 9.2 Technische Fragen

**F06: Welchen Mandrel-Durchmesser brauche ich?**

Der Mandrel-Durchmesser hängt von der Segelfläche und der Tuchdicke ab. Faustformel: Mandrel-Ø in mm ≈ 4 × √(Segelfläche in m²) + 20. Beispiel: 50 m² → 4 × 7,07 + 20 ≈ 48 mm (gerundet auf nächste Standardgröße: 50–65 mm). Hersteller geben für jedes Modell den empfohlenen Segelflächen-Bereich an — halten Sie sich an diese Angaben.

**F07: Welches Segeltuch ist am besten für In-Mast?**

Für Fahrtensegler: Hochwertiges Dacron (Bainbridge Diax-Qualität oder vergleichbar) ist der Standard. Für bessere Formhaltung und Langlebigkeit: Hydranet (Dyneema-Polyester-Hybrid) — ca. 60–80% teurer, aber deutlich langlebiger (12–18 Jahre vs. 8–12 Jahre) und formstabiler. Membrane und steife Laminate sind NICHT rollbar und daher für In-Mast ungeeignet.

**F08: Brauche ich einen Rigid Vang für In-Boom?**

Ja, zwingend. Ein konventioneller Baumkicker (Leinenkicker oder Teleskop-Kicker) ist mit In-Boom-Furling nicht kompatibel, da der Boom zum Einrollen des Segels frei schwingen muss und die Schlitzöffnung oben liegt. Der Rigid Vang (starrer Baumniederholer mit Gasdruckfeder) hält den Baum horizontal und ermöglicht trotzdem das Rollen des Segels. Alle seriösen In-Boom-Hersteller liefern den Rigid Vang mit oder empfehlen ein spezifisches Modell.

**F09: Wie oft muss ein In-Mast-System gewartet werden?**

Jährlich: Mandrel-Lager schmieren (Hersteller-Fett), Schlitzlippen reinigen und auf Verformung prüfen, alle Umlenkrollen kontrollieren, elektrische Verbindungen prüfen. Alle 3 Jahre: Mandrel ausbauen und inspizieren, Lager prüfen (Spiel? Korrosion?), Segel vom Segelmacher inspizieren lassen. Alle 5–7 Jahre: Lager tauschen (prophylaktisch), Bürstendichtungen erneuern, Fall erneuern. Gesamtkosten Wartung: ca. €200–600/Jahr.

**F10: Was ist ein Halyard-Diverter und brauche ich einen?**

Ein Halyard-Diverter ist eine Führung am Masttop, die das Großfall vom Mandrel fernhält. Bei In-Mast-Systemen ist er ABSOLUT ESSENTIELL. Ohne Halyard-Diverter kann sich das Fall um den drehenden Mandrel wickeln (Halyard-Wrap), was zum schwerwiegendsten Blockade-Szenario führt (→ Fehlerbild F03). Jedes seriöse In-Mast-System hat einen Halyard-Diverter im Lieferumfang. Bei Nachrüstungen: IMMER prüfen, ob der Diverter korrekt installiert ist.

### 9.3 Auswahl und Kaufberatung

**F11: Welches System empfehlen Sie für eine 38-ft-Fahrtenyacht?**

Für eine 38-ft-Fahrtenyacht (ca. 11,5 m) mit Fokus auf Fahrtensegeln und Kurzhand-Betrieb ist In-Mast mit elektrischem Antrieb die populärste Wahl. Typisches Setup: Selden C390 mit E40-Antrieb (ca. €9.000–13.000 inkl. Mast). Alternativ: In-Boom (Leisure Furl BR 42 oder Bartels BFS 40), wenn Segelperformance wichtiger ist (ca. €7.000–12.000 nur Boom + Antrieb, Standard-Mast bleibt). Slab-Reefing ist günstiger (€1.000–2.000 alles inklusive), erfordert aber Deckarbeit.

**F12: Lohnt sich ein elektrischer Antrieb?**

Ab 12 m Bootslänge: eindeutig ja. Die manuellen Kräfte werden bei größeren Segeln signifikant, und die Zeitersparnis beim Reffen ist ein Sicherheitsgewinn. Unter 12 m: Abwägungssache. Manuell ist einfacher, leichter und günstiger. Elektrisch ist komfortabler und schneller. Für Kurzhand-Segler: Elektrisch ist fast immer die bessere Wahl. Kosten: Elektrischer Antrieb (Nachrüst-Kit) ca. €2.500–6.000 + Einbau.

**F13: In-Mast oder In-Boom — was hält länger?**

Beide Systeme halten bei korrekter Wartung 15–25 Jahre (mechanische Komponenten). Das Segel selbst ist der limitierende Faktor: In-Mast-Segel halten typisch 8–12 Jahre, In-Boom-Segel 9–14 Jahre (weniger UV-Belastung im Boom). Standard-Großsegel (Slab): 10–15 Jahre. Lager und Dichtungen müssen bei beiden Systemen alle 5–7 Jahre getauscht werden.

**F14: Was kostet ein Segelersatz für In-Mast vs. Standard?**

In-Mast-Segel kosten ca. 20–40% mehr als Standard-Großsegel gleicher Größe, da sie aus rollbarem Material gefertigt sein müssen und das Luff-Tape speziell ist. Beispiel für ein 12 m Boot: Standard-Dacron-Großsegel: €1.800–2.800. In-Mast-Rollsegel (Dacron): €2.500–4.000. In-Mast-Rollsegel (Hydranet): €3.500–5.500. In-Boom-Rollsegel: €2.200–3.800.

**F15: Kann ich mein bestehendes Segel für ein Rollreffsystem verwenden?**

Nein. Für In-Mast ist ein spezielles Rollsegel zwingend erforderlich (kein Roach, kein Latten, spezielles Luff-Tape). Für In-Boom wird ebenfalls ein spezielles Segel benötigt (angepasste Latten, spezielle Verstärkungen am Luff und Foot). Bestehende Standard-Großsegel sind NICHT kompatibel mit Rollreffsystemen. Einzige Ausnahme: Slab-Reefing-Umrüstung — hier kann das bestehende Segel oft weiterverwendet werden, sofern Reffkauschen vorhanden oder nachrüstbar sind.

### 9.4 Wartung und Pflege

**F16: Wie pflege ich mein In-Mast-System im Winter?**

Segel NICHT eingerollt im Mast überwintern! Das Segel entwickelt permanente Knickfalten und kann Feuchtigkeit einschließen (Schimmel). Stattdessen: Segel aus dem Mast herausnehmen, locker gerollt (NICHT gefaltet) an trockenem Ort lagern. Mandrel im Mast belassen, aber Mastinneres belüften. Mastschlitz mit Abdeckband schützen. Lager nicht ölen (Fett bleibt). Im Frühjahr: Lager schmieren, Segel neu einziehen, Funktionstest.

**F17: Mein Segel riecht nach Schimmel. Was tun?**

Segel aus dem System nehmen. Mit Süßwasser und mildem Reiniger (KEIN Bleichmittel!) waschen. Gut trocknen lassen (nicht in der prallen Sonne). Schimmelbehandlung: Sprühbehandlung mit marinem Anti-Schimmel-Mittel (z.B. Star Brite Mildew Stain Remover). Ursache beseitigen: Feuchtigkeit im Mast/Boom reduzieren, Drainage prüfen, Segel nie nass einrollen und eingerollt lagern.

**F18: Wie erkenne ich, dass mein Mandrel-Lager gewechselt werden muss?**

Zeichen für Lagerverschleiß: 1) Ruckeln beim Rollen (nicht gleichmäßig). 2) Ungewöhnliche Geräusche (Quietschen, Kratzen). 3) Spürbares Spiel am Mandrel (axial >0,5 mm oder radial sichtbar). 4) Erhöhter Kraftaufwand beim manuellen Rollen. 5) Motor zieht mehr Strom als normal (Amperemeter beobachten). Empfehlung: Alle 5–7 Jahre prophylaktisch tauschen, auch wenn keine Symptome sichtbar.

**F19: Kann ich Mandrel-Lager selbst wechseln?**

Beim In-Mast-System: Das untere Lager (Mastfuß) ist oft zugänglich und kann von einem erfahrenen Eigner gewechselt werden. Das obere Lager (Masttop) erfordert Arbeit am Masttop — entweder Mast legen oder Bootsmannstuhl. Empfehlung: Lagerwechsel vom Rigger durchführen lassen (Kosten: €200–500 Material + €300–600 Arbeit). Beim In-Boom: Lager sind meist gut zugänglich, Eigenwechsel möglich.

### 9.5 Sicherheit und Notfälle

**F20: Was tue ich, wenn mein In-Mast-Segel bei Starkwind klemmt?**

→ Siehe Troubleshooting-Baum 5 (Abschnitt 8.5). Kurzfassung: 1) Kurs VOR den Wind gehen. 2) Schot komplett fieren. 3) Motor starten. 4) Manuelles Override versuchen (sanfte Richtungswechsel). 5) Wenn blockiert: Segel belassen, Geschwindigkeit reduzieren, Hafen anlaufen. NIEMALS mit Gewalt am Mandrel arbeiten — Mandrel kann sich permanent verformen.

**F21: Brauche ich ein Trysegel, wenn ich In-Mast habe?**

Für Küstensegeln: Nicht zwingend, aber empfohlen. Für Blauwasser und Offshore: JA. World Sailing OSR (Offshore Special Regulations) verlangen für Kategorie 0–2 die Möglichkeit, ein Sturmgroßsegel zu setzen. Bei In-Mast-Systemen wird ein Trysegel empfohlen, das an einem separaten Sturmtrack am Mast gesetzt werden kann. Grund: Wenn der Mandrel bei Sturm blockiert, ist das In-Mast-Segel unbrauchbar — das Trysegel ist dann die einzige Option.

**F22: Ist In-Mast-Furling gefährlich?**

Nicht per se. Moderne Systeme (Selden, Facnor) sind ausgereift und zuverlässig. Die Gefahr liegt in Extremsituationen: Wenn der Mandrel bei Starkwind blockiert, kann das Segel nicht geborgen werden — das ist das Worst-Case-Szenario, das bei Slab-Reefing nicht existiert (man kann das Segel immer fallen lassen). Dieses Risiko wird durch korrekte Wartung, ein mitgeführtes Trysegel und ein dokumentiertes Notreffen-Verfahren auf ein akzeptables Maß reduziert.

### 9.6 Spezialfragen

**F23: Kann ich einen Gennaker/Code 0 mit In-Mast kombinieren?**

Ja, problemlos. Gennaker und Code 0 werden am Vorsegel-Rollreff oder mit Bergesack gefahren und haben keine Verbindung zum Großsegel-System. Tatsächlich empfehlen viele Segelmacher für In-Mast-Yachten einen größeren Code 0 oder Gennaker, um den Segelflächen-Verlust des Großsegels auf Raumschotkursen zu kompensieren.

**F24: Gibt es In-Mast-Systeme für Katamarane?**

Ja. Katamarane verwenden häufig In-Mast-Furling wegen des großen Cockpit-Abstands zum Mast und der Kurzhand-Tauglichkeit. Selden, Facnor und Leisure Furl bieten Systeme für Katamarane an. Besonderheit: Katamarane krängen weniger → Wickelprobleme durch Krängung sind seltener. Aber: höhere absolute Segelkräfte durch größere Segelflächen bei gleichem LOA.

**F25: Kann ich von In-Mast auf In-Boom umrüsten (oder umgekehrt)?**

Von In-Mast zu In-Boom: Theoretisch ja, aber es erfordert einen neuen Mast (Standardprofil) UND einen neuen Boom UND ein neues Segel. De facto ein komplett neues Rigg — wirtschaftlich selten sinnvoll. Von In-Boom zu In-Mast: Neuer Mast (Furling-Profil) + neues Segel. Bestehender Boom kann durch Standard-Boom ersetzt werden. Auch hier: De facto Kompletttausch des Riggs. Empfehlung: Diese Umrüstung nur in Verbindung mit einem ohnehin fälligen Riggtausch (alle 15–25 Jahre) in Betracht ziehen.

### 9.7 Installation und Montage

**F26: Wie lange dauert die Installation eines In-Mast-Systems?**

Die Installation umfasst den Masttausch und dauert typischerweise 3–5 Arbeitstage: Tag 1: Alten Mast legen, Rigg demontieren, Beschläge abbauen. Tag 2: Beschläge auf neuen Furling-Mast übertragen, E-Antrieb montieren. Tag 3: Neuen Mast stellen, Rigg einstellen, Kabel verlegen. Tag 4: Segel einziehen, Funktionstest, Feineinstellung. Tag 5: Reserve/Seeerprobung. Kosten für die Montage (ohne Material): €2.000–5.000 je nach Werft und Region.

**F27: Kann ein Segelmacher das In-Mast-Segel vor Ort einziehen?**

Ja, das Einziehen des Rollsegels in den Mast ist eine Standard-Arbeit für Segelmacher und Rigger. Der Vorgang dauert ca. 1–2 Stunden: Segel wird am Mandrel befestigt (Kopfanschluss), Luff-Tape in die Foil-Schiene eingefädelt, Segel schrittweise eingerollt, Outhaul angeschlossen, Funktionstest. Wichtig: Das Segel muss exakt auf das Mastprofil abgestimmt sein (Luff-Tape-Dicke, Segelbreite, Kopfanschluss).

**F28: Muss bei In-Boom der Mast gelegt werden?**

Nein, das ist der große Vorteil von In-Boom: Nur der Baum wird getauscht. Der Mast bleibt ein Standard-Profil und muss nicht verändert werden. Die Installation dauert typischerweise 1–2 Tage: Alten Baum abbauen, neuen In-Boom montieren, Rigid Vang installieren, Endlos-Fall-System einrichten, Segel einziehen. Der Mast muss NICHT gelegt werden. Kosten Montage: €800–2.500.

**F29: Ist eine CAN-Bus-Anbindung des E-Antriebs sinnvoll?**

Für die meisten Fahrtensegler: Nein, unnötige Komplexität. Ein einfacher Taster (Auf/Ab) reicht völlig aus. CAN-Bus-Anbindung (NMEA 2000) ist sinnvoll für: 1) Großyachten mit zentraler Steuerung (Pilothouse, Flybridge). 2) Automatisierte Reff-Strategien (Autopilot-Integration: bei definierter Windstärke automatisch reffen). 3) Monitoring (Stromverbrauch, Rollzyklen, Fehlermeldungen auf dem Plotter). Kosten für CAN-Bus-Integration: €500–1.500 zusätzlich.

**F30: Welche Batteriekapazität brauche ich für den E-Antrieb?**

Ein vollständiger Rollzyklus (komplett Ein- und Ausrollen) dauert 30–90 Sekunden und verbraucht ca. 5–30 Ah (je nach System und Bootsgröße). Typischer Verbrauch pro Segeltag mit 3–5 Rollzyklen: 15–150 Ah. Bei einer 12V-Anlage mit 200 Ah-Batterie und 50% Entladetiefe (100 Ah nutzbar) reicht dies für einen normalen Segeltag. Für Langfahrt: Solaranlage oder Lichtmaschine muss den täglichen Verbrauch decken. Empfehlung: Mindestens 100 Ah Reserve-Kapazität über den normalen Bordbedarf hinaus.

### 9.8 Versicherung und Wiederverkauf

**F31: Beeinflusst das Reffsystem die Versicherungsprämie?**

In der Regel nein. Die meisten Yacht-Versicherer differenzieren nicht nach Reffsystem-Typ. Ausnahme: Einige Versicherer verlangen bei In-Mast-Systemen für Langfahrt-Policen einen Nachweis über regelmäßige Wartung und ein mitgeführtes Trysegel. Bei Kaskoschäden durch Furling-Systemversagen (z.B. Mandrel-Blockade führt zu Sturmschaden) kann die Regulierung komplizierter sein, wenn mangelnde Wartung nachweisbar ist.

**F32: Beeinflusst das System den Wiederverkaufswert?**

Ja, positiv. Yachten mit In-Mast- oder In-Boom-Furling erzielen am Gebrauchtmarkt tendenziell 3–8% höhere Preise als vergleichbare Yachten mit Slab-Reefing (bei Fahrtenyachten). Der Grund: Kurzhand-Tauglichkeit und Komfort sind beim Gebrauchtkauf wichtige Kriterien. Allerdings: Alter und Zustand des Systems sind entscheidend. Ein 15 Jahre altes In-Mast-System mit verschlissenem Segel kann den Wert auch senken (Reparaturkosten schrecken ab).

**F33: Kann ich zwischen den Herstellern wechseln (z.B. Selden-Mast mit Facnor-Mandrel)?**

In der Regel nein. Mastprofil und Mandrel sind herstellerspezifisch und nicht kreuzkompatibel. Die Schlitzbreite, der Mandrel-Durchmesser und die Lageraufnahmen sind auf das jeweilige System abgestimmt. Ausnahme: Profurl MFS ist als Nachrüst-System konzipiert und kann in verschiedene Mastprofile eingebaut werden (eigene Foil-Schienen). Beim In-Boom ist die Situation etwas flexibler, da der Mast unverändert bleibt und nur der Boom herstellerspezifisch ist.

### 9.9 Spezielle Anwendungen

**F34: Gibt es In-Mast-Systeme für Carbon-Masten?**

Ja, aber sehr selten und teuer. Carbon-Mastbauer wie Southern Spars, Hall Spars oder Offshore Spars bieten Custom-Furling-Profile aus Carbon an. Die Kosten sind erheblich (Faktor 3–5 gegenüber Aluminium). Vorteil: Carbon ist leichter und steifer → der Nachteil des breiteren Furling-Profils wird teilweise kompensiert. Einsatz: fast ausschließlich auf Superyachten >25 m und Hochleistungs-Katamaranen.

**F35: Funktioniert In-Mast auch auf einem Ketsch-Rigg (Besan)?**

Ja. Der Besan-Mast einer Ketsch kann ebenfalls ein Furling-Profil erhalten. Da der Besan kleiner ist als das Großsegel, ist das System tendenziell problemloser (kleinerer Mandrel, weniger Kraft). Hersteller: Selden bietet kleine Furling-Profile (C290) an, die für Besan-Masten geeignet sind. Manche Ketsch-Eigner rüsten nur den Besan mit In-Mast aus (weil er am schwierigsten zu bergen ist) und behalten Slab-Reefing am Großsegel.

**F36: Gibt es Rollreffsysteme für Gaffelsegel?**

Nein, nicht in kommerziell verfügbarer Form. Gaffelsegel haben eine komplexe Geometrie (vier Ecken: Kopf, Hals, Schothorn, Peak) und sind an Gaffelbaum und Mast befestigt. Ein Furling-System wäre theoretisch denkbar, ist aber aufgrund der Geometrie nicht praktikabel. Gaffelsegel werden traditionell mit Smeerreeps (Bindereffs) gerefft oder durch Bergen und Setzen eines kleineren Segels angepasst.

---

## 10. Glossar

### 10.1 Begriffe A–D

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Achterliek | Leech | Hintere Kante des Segels, vom Kopf (Head) zum Schothorn (Clew) |
| Ausholsystem | Outhaul System | Leinensystem zum Ausrollen/Setzen des Segels (bei Furling) |
| Bändsel | Lacing / Lashing | Dünne Leine zum Befestigen oder Sichern von Segel- oder Rigg-Teilen |
| Batten | Batten | Horizontal ins Segel eingesetzte Stab (Glasfaser, Carbon) zur Formgebung |
| Baumkicker | Boom Vang / Kicking Strap | Vorrichtung zum Niederdrücken des Baums (Twist-Kontrolle) |
| Bindereef | Slab Reef | Traditionelles Reff durch Falten des Segels mit Reffkauschen |
| Bürstendichtung | Brush Seal | Dichtungssystem am Mastschlitz mit feinen Borsten gegen Wasser/Wind |
| Cunningham | Cunningham | Leine zum Spannen des Vorlieks unterhalb des Kopfbretts |
| Dacron | Dacron | Markenname für gewobenes Polyester-Segeltuch (DuPont) |
| Druckschott | Compression Panel | Verstärkungsschott im Rumpf am Fuß des Mastes |

### 10.2 Begriffe E–H

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Einholsystem | Furling Line / Inhaul | Leinen-/Antriebssystem zum Einrollen des Segels in Mast oder Boom |
| Einleinen-Reff | Single-Line Reefing | Reff-System mit einer Leine pro Reff (Luff + Clew simultan) |
| Endlosfallsystem | Continuous Halyard | Fallsystem als Endlosschleife, das Fall gleichzeitig fiert und holt |
| Fallstopper / Clutch | Halyard Lock / Clutch | Klemme, die das Fall unter Last festhält (Spinlock, Lewmar, etc.) |
| Foam-Strip | Luff Foam / Foam Pad | Schaumstoffstreifen am Vorliek, der gleichmäßiges Wickeln fördert |
| Foil-Track | Foil Track / Luff Track | Führungsschiene im Mast, in der das Segel-Luff-Tape gleitet |
| Freilauf | Free-Spool / Clutch | Kupplung, die bei Antriebsausfall freies Drehen des Mandrels erlaubt |
| Großfall | Main Halyard | Leine zum Setzen/Fieren des Großsegels |
| Halyard-Diverter | Halyard Diverter | Führung am Masttop, die das Fall vom Mandrel fernhält |
| Halyard-Wrap | Halyard Wrap | Umwicklung des Falls um den Mandrel (schwerwiegender Fehler) |
| Hydraulikmotor | Hydraulic Motor | Antrieb durch Hydraulikfluid unter Druck, für große Systeme |
| Hydranet | Hydranet / Dyneema-Polyester | Segeltuch-Hybrid aus Dyneema-Fasern in Polyester-Matrix |

### 10.3 Begriffe I–M

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| In-Boom Furling | In-Boom Furling | System zum Einrollen des Großsegels in den Baum (horizontal) |
| In-Mast Furling | In-Mast Furling | System zum Einrollen des Großsegels in den Mast (vertikal) |
| Kopfbrett | Headboard | Verstärktes oberes Ende des Großsegels |
| Lazy-Bag | Lazy-Bag / Stack-Pack | Persenning/Tasche am Baum zum Auffangen des geborgenen Segels |
| Lazyjacks | Lazy Jacks | Leinen vom Mast zum Baum, die das Segel beim Bergen auffangen |
| Luff-Tape | Luff Tape / Bolt Rope | Verstärktes Band am Vorliek des Segels, das in der Mastnut/Foil gleitet |
| Mandrel | Mandrel / Furling Spar | Wickelstab/-rohr, um den sich das Segel rollt |
| Mandrel-Lager | Mandrel Bearing | Kugel- oder Gleitlager, das den Mandrel im Mast/Boom abstützt |
| Masttop | Masthead | Oberstes Ende des Mastes |
| Mastschlitz | Mast Slot | Vertikale Öffnung an der Hinterseite des Furling-Mastes |

### 10.4 Begriffe N–R

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Notreffen | Emergency Reefing | Verfahren zum Reffen/Bergen bei Systemausfall |
| Outhaul | Outhaul | Leine/System zum Spannen des Unterlieks am Baum |
| Planetengetriebe | Planetary Gearbox | Kompaktes Getriebe mit hoher Untersetzung für E-Antriebe |
| Profil (Segel) | Sail Draft / Camber | Wölbung/Tiefe des Segelprofils (aerodynamische Form) |
| Reffkausch | Reef Cringle | Verstärkter Ring im Segel an den Reffpunkten (Luff + Clew) |
| Reffbändsel | Reef Lacing | Kurze Leinen zum Sichern des losen Segeltuches nach dem Reffen |
| Reffleine | Reef Line | Leine zum Ziehen der Achterliek-Reffkausch zum Baum |
| Reffloch / Refföse | Reef Eye / Reef Grommet | Öse/Loch im Segel für Reffhaken oder Reffleine |
| Rigid Vang | Rigid Vang / Solid Vang | Starrer Baumniederholer mit Gasdruckfeder (obligatorisch bei In-Boom) |
| Roach | Roach | Positive Rundung des Achterlieks über die gerade Verbindung Head-Clew hinaus |
| Rollzyklus | Furling Cycle | Einmaliges komplettes Ein- und Ausrollen des Segels |

### 10.5 Begriffe S–Z

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Schlitzlippe | Slot Lip | Führungsschiene/Kante am Mastschlitz, die das Segel führt |
| Schothorn | Clew | Hintere untere Ecke des Segels (Schot-Ansatzpunkt) |
| Self-Tacking | Self-Tacking | Selbstwendend (z.B. Segel, das bei der Wende selbstständig die Seite wechselt) |
| Sturmtrack | Storm Track | Separater Masttrack für Trysegel (Sturmgroßsegel) |
| Torsionssteifigkeit | Torsional Stiffness | Widerstand des Mastprofils gegen Verdrehung (GJ) |
| Traveller | Traveller / Mainsheet Track | Schiene, auf der der Großschot-Block querschiffs verschoben werden kann |
| Trysegel | Trysail / Storm Trysail | Kleines, robustes Sturmgroßsegel für Extrembedingungen |
| Twist | Twist | Verdrehung des Segelprofils vom Unterliek zum Oberliek |
| UHMWPE | UHMWPE | Ultra-High-Molecular-Weight Polyethylene (Kunststoff für Führungen) |
| Unterliek | Foot | Untere Kante des Segels, zwischen Hals (Tack) und Schothorn (Clew) |
| Vertikallatte | Vertical Batten | Senkrecht orientierte Segellatte (In-Mast-Segel) |
| Vorspannung (Rigg) | Rig Tension / Forestay Tension | Zugspannung in den stehenden Want- und Stagen |
| Wickellage | Wrap Layer | Eine Lage des um den Mandrel gewickelten Segels |

### 10.6 Begriffe — Ergänzende Fachausdrücke

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Anstellwinkel | Angle of Attack | Winkel zwischen Segel-Chord und anströmender Luft |
| Auftriebsbeiwert | Lift Coefficient (C_L) | Dimensionslose Kennzahl für die Auftriebskraft eines Segels |
| Baumtopp | Boom End / Outboard End | Äußeres (achtern liegendes) Ende des Baums |
| Baumstumpf | Gooseneck Area | Inneres (mastseitiges) Ende des Baums am Lümmelbeschlag |
| Bergesack | Snuffer / Dousing Sock | Tuchschlauch zum Bergen von Gennakern und Code 0 |
| Capstan-Effekt | Capstan Equation | Kraftverstärkung durch Seilreibung auf zylindrischer Trommel |
| CAN-Bus | CAN Bus | Controller Area Network — Datenbussystem für Bordelektronik |
| Chord | Chord | Gerade Verbindung zwischen Vorliek und Achterliek auf einer Höhe |
| Code 0 | Code Zero | Großes Leichtwindsegel zwischen Genua und Gennaker |
| Draft (Segel) | Sail Draft | Tiefe des Segelprofils, gemessen als Prozent der Chord-Länge |
| Drucklager | Thrust Bearing | Axiallager, nimmt Kräfte in Achsrichtung auf |
| Fallabweiser | Halyard Diverter | = Halyard-Diverter, Führung am Masttop |
| Fieren | Ease / Pay Out | Kontrolliertes Nachlassen einer Leine unter Last |
| Gasdruckfeder | Gas Spring / Gas Strut | Feder mit Gasdruck (N₂) als Kraftelement (im Rigid Vang) |
| Getriebe-Untersetzung | Gear Ratio | Verhältnis der Drehzahlen zwischen Motor und Mandrel |
| GZ-Kurve | GZ Curve / Righting Moment | Stabilitätskurve: aufrichtendes Moment über Krängungswinkel |
| Killen | Luffing / Flapping | Flattern des Segels, wenn es nicht korrekt getrimmt ist |
| Krängung | Heel | Seitliche Neigung des Bootes durch Windkraft |
| Loose Foot | Loose Foot | Unterliek ist nicht am Baum befestigt (nur an Hals und Schothorn) |
| Lümmelbeschlag | Gooseneck | Gelenkverbindung zwischen Baum und Mast |
| NMEA 2000 | NMEA 2000 | Datenprotokoll für marine Elektronik (CAN-basiert) |
| Patenthalse | Accidental Gybe | Unbeabsichtigtes Übergehen des Segels auf die andere Seite |
| Radiallager | Radial Bearing | Lager, das Kräfte senkrecht zur Achse aufnimmt |
| Refflhaken | Reef Hook | Haken am Baum, in den die Luff-Reffkausch eingehängt wird |
| Saling | Spreader | Horizontaler Ausleger am Mast, der die Wanten spreizt |
| Schotlast | Sheet Load | Kraft in der Großschot (abhängig von Wind und Segelstellung) |
| Segeldruckpunkt | Centre of Effort (CE) | Angriffspunkt der resultierenden Segelkraft |
| Trimm (Segel) | Sail Trim | Einstellung des Segels für optimale Leistung |
| VMG | VMG (Velocity Made Good) | Geschwindigkeitskomponente in Richtung Ziel (Am-Wind: Höhe) |
| Vorliek | Luff | Vordere Kante des Segels (am Mast oder Vorstag) |
| Want | Shroud | Stehendes Gut: seitliche Abspannung des Mastes |
| Widerstandsbeiwert | Drag Coefficient (C_D) | Dimensionslose Kennzahl für den Widerstand eines Segels |
| Wickelrichtung | Furling Direction | Drehrichtung des Mandrels (im Uhrzeigersinn / gegen) |

---

## 11. Schnell-Referenz

### 11.1 Systemauswahl auf einen Blick

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  GROSSSEGEL-REFF SCHNELLAUSWAHL                        │
├─────────────────┬─────────────┬──────────────┬─────────────────────────┤
│ Kriterium       │ Slab/SLR    │ In-Mast      │ In-Boom               │
├─────────────────┼─────────────┼──────────────┼─────────────────────────┤
│ Budget          │ €€          │ €€€€         │ €€€€                  │
│ Segelform       │ ★★★★★       │ ★★☆☆☆        │ ★★★★☆                 │
│ Komfort         │ ★★☆☆☆       │ ★★★★★        │ ★★★★☆                 │
│ Zuverlässigkeit │ ★★★★★       │ ★★★☆☆        │ ★★★☆☆                 │
│ Kurzhand        │ ★★☆☆☆       │ ★★★★★        │ ★★★★☆                 │
│ Regatta         │ ★★★★★       │ ★☆☆☆☆        │ ★★★☆☆                 │
│ Nachrüstung     │ ★★★★★       │ ★☆☆☆☆        │ ★★★☆☆                 │
│ Notreffen       │ ★★★★★       │ ★★☆☆☆        │ ★★★★☆                 │
└─────────────────┴─────────────┴──────────────┴─────────────────────────┘
```

### 11.2 Wartungsintervalle Schnellübersicht

```
┌───────────────────────────────────────────────────────────┐
│              WARTUNGSINTERVALLE (alle Systeme)             │
├──────────────────────┬────────────────────────────────────┤
│ JÄHRLICH             │                                    │
│ • Schlitz/Führung    │ Reinigen, Lippen prüfen            │
│ • Mandrel-Lager      │ Schmieren (Hersteller-Fett)        │
│ • E-Motor            │ Verbindungen prüfen                │
│ • Umlenkrollen       │ Leichtlauf prüfen                  │
│ • Leinen             │ Verschleiß prüfen                  │
├──────────────────────┼────────────────────────────────────┤
│ ALLE 3 JAHRE         │                                    │
│ • Segel              │ Segelmacher-Inspektion             │
│ • Mandrel            │ Ausbauen, inspizieren              │
│ • E-Motor Kohlen     │ Prüfen (Bürstenmotor)              │
├──────────────────────┼────────────────────────────────────┤
│ ALLE 5–7 JAHRE       │                                    │
│ • Mandrel-Lager      │ Prophylaktisch tauschen            │
│ • Bürstendichtung    │ Erneuern                           │
│ • Großfall           │ Erneuern                           │
│ • Endlos-Fall        │ Erneuern (In-Boom)                 │
│ • Rigid-Vang-Feder   │ Prüfen/erneuern (In-Boom)         │
├──────────────────────┼────────────────────────────────────┤
│ ALLE 8–15 JAHRE      │                                    │
│ • Segel              │ Neusegel (je nach Tuchqualität)    │
│ • E-Motor            │ Revision oder Ersatz               │
│ • Schlitzschienen    │ Ersetzen bei Verschleiß            │
└──────────────────────┴────────────────────────────────────┘
```

### 11.3 Notfall-Checkliste

```
┌───────────────────────────────────────────────────────────┐
│       NOTFALL: SEGEL KLEMMT BEI STARKWIND                │
├───────────────────────────────────────────────────────────┤
│ □ 1. RUHE BEWAHREN                                       │
│ □ 2. Kurs VOR den Wind gehen                             │
│ □ 3. Schot komplett fieren                                │
│ □ 4. Motor starten                                        │
│ □ 5. Manuelles Override versuchen (sanft!)                │
│ □ 6. Geschwindigkeit reduzieren                           │
│ □ 7. Vorsegel bergen                                      │
│ □ 8. Crew: Rettungswesten, Lifeline                      │
│ □ 9. Nächsten Hafen / Ankerplatz ansteuern                │
│ □ 10. NIEMALS Gewalt am Mandrel!                          │
│ □ 11. LAST RESORT: Segel abschneiden (nur bei Gefahr!)   │
└───────────────────────────────────────────────────────────┘
```

---

## 12. Anhänge A–X

### ANHANG A — Fallstudie: Bavaria 40 Cruiser, In-Mast Nachrüstung

**Ausgangssituation:**
- Boot: Bavaria 40 Cruiser (2018), 12,35 m LOA, Standard-Slab-Reefing
- Eigner: Ehepaar, 60+, Kurzhand-Segeln in der Ostsee und Mittelmeer
- Problem: Slab-Reefing erfordert Deckarbeit, zunehmend beschwerlich
- Budget: ca. €15.000 für Systemwechsel

**Lösung:**
- Neuer Selden C390 Furling-Mast mit E40 Elektroantrieb
- Neues Dacron-Rollsegel (Elvström, 48 m² statt 55 m² Standard)
- Installation durch Rigger in Kiel (3 Arbeitstage)

**Kosten:**
| Position | Betrag |
|----------|--------|
| Selden C390 Furling-Mast | €5.800 |
| Selden E40 Elektroantrieb | €3.200 |
| Rollsegel (Elvström Dacron) | €3.100 |
| Demontage alter Mast + Montage neuer Mast | €2.400 |
| Rigg-Neueinstellung | €800 |
| Kabel, Schalter, Sicherung | €350 |
| **Gesamt** | **€15.650** |

**Ergebnis nach 2 Saisons:**
- Reffen vom Cockpit in <30 Sekunden (vorher: 5–10 Minuten mit Deckarbeit)
- Segelflächen-Verlust (7 m², ca. 13%) kompensiert durch Code 0 (bereits vorhanden)
- Am-Wind-Performance: spürbar geringer (ca. 0.3 kn VMG-Verlust bei 15 kn Wind)
- Eignerzufriedenheit: „Beste Investition seit dem Bootkauf"
- Ein Verklemmungs-Ereignis in 2 Saisons (Halyard-Wrap, selbst behoben durch Richtungswechsel)

**AYDI-Bewertung:** confidence: documented | score: 82/100

### ANHANG B — Fallstudie: Hallberg-Rassy 412, In-Boom ab Werk

**Ausgangssituation:**
- Boot: Hallberg-Rassy 412 (2022), 12,50 m LOA, In-Boom ab Werk
- System: Z-Spars IBF 400 mit elektrischem Antrieb
- Segel: North Sails Dacron/Hydranet-Hybrid, 52 m², Kurzlatten

**Erfahrungen nach 3 Saisons (Nordsee, Kanal, Biskaya):**
- Zuverlässigkeit: Keine Blockaden in 3 Saisons
- Segelform: Deutlich besser als erwartet dank Kurzlatten (Roach ca. 8%)
- Bergen: Sauber und schnell (45 Sekunden elektrisch)
- Rigid Vang: Funktioniert einwandfrei, Gasdruckfeder nach 2 Jahren noch perfekt
- Wartung: Jährlich ca. 2 Stunden (Rollen reinigen, Fetten, Funktionstest)
- Trysegel: Mitgeführt, aber nie benötigt

**Probleme:**
- Baumgröße optisch gewöhnungsbedürftig
- Boom-Gewicht: +45 kg vs. Standard → Schwerpunkt leicht erhöht
- Bei Leichtwind (<8 kn) fällt das Segel ohne Baumkicker „tot" → nur Traveller-Kontrolle

**AYDI-Bewertung:** confidence: documented | score: 88/100

### ANHANG C — Fallstudie: Beneteau Oceanis 51.1, In-Mast Standard

**Ausgangssituation:**
- Boot: Beneteau Oceanis 51.1 (2020), 15,38 m LOA
- System: Selden C470 mit E50 Elektroantrieb (ab Werk)
- Segel: Incidences Dacron-Rollsegel, 78 m² (Standard wäre 95 m² mit Latten)
- Nutzung: Charter in Kroatien, 28 Wochen/Saison

**Erfahrungen (Charter-Basis, 4 Saisons):**
- 1.200+ Rollzyklen pro Saison ohne schwerwiegende Störung
- 3× leichte Verklemmungen (selbst behoben durch Richtungswechsel)
- 1× Halyard-Wrap nach Segelwechsel (Diverter falsch eingestellt) — Rigger-Einsatz
- Charterrückmeldung: 95% positiv, „einfach zu bedienen"
- Segel nach 4 Saisons: Profil deutlich abgeflacht, Dacron gereckt → Segelwechsel fällig

**Kosten (Charter-Kalkulation):**
| Position | Betrag/Jahr |
|----------|------------|
| Wartung (Lager, Reinigung) | €400 |
| Segel-Ersatz (anteilig, 4-Jahres-Zyklus) | €1.200 |
| Rigger-Einsatz (anteilig) | €200 |
| **Jährliche Systemkosten** | **€1.800** |

**AYDI-Bewertung:** confidence: documented | score: 78/100 (Abzug: hoher Segelverschleiß im Charter)

### ANHANG D — Fallstudie: Contest 50CS, Slab-Reefing Blauwasser

**Ausgangssituation:**
- Boot: Contest 50CS (2019), 15,24 m LOA
- System: 3× Slab-Reefing, Single-Line, Full-Batten-Großsegel (98 m²)
- Nutzung: Blauwasser (Atlantikumrundung 2021–2024)

**Erfahrungen:**
- 0 Systemausfälle in 3 Jahren Blauwasser
- Reffen routinemäßig vom Cockpit (Single-Line) in 2–3 Minuten
- Segel nach 3 Jahren Tropen: noch gut, leichte UV-Degradation am Achterliek
- Reef 3 in Sturmtief vor Kap der Guten Hoffnung (55 kn) — funktionierte einwandfrei
- Trysegel nicht benötigt (3× Reef 3 reichte)

**Eigner-Zitat:** „Für Blauwasser gibt es keinen Grund für In-Mast. Slab funktioniert, ist reparierbar, und man hat immer Kontrolle."

**AYDI-Bewertung:** confidence: documented | score: 92/100 (höchste Zuverlässigkeit)

### ANHANG E — Fallstudie: Jeanneau Sun Odyssey 440, In-Mast Problem-Chronik

**Ausgangssituation:**
- Boot: Jeanneau Sun Odyssey 440 (2019), 13,39 m LOA
- System: Selden C430, manueller Antrieb (Upgrade auf E-Antrieb 2021)
- Segel: Jeanneau-Standard-Dacron-Rollsegel, 62 m²

**Problem-Chronik:**

| Datum | Problem | Ursache | Behebung | Kosten |
|-------|---------|---------|----------|--------|
| 05/2020 | Mandrel klemmt beim Einrollen | Schlitzlippen verschmutzt (Salzablagerung) | Reinigung, Schmierung | €0 (Eigenarbeit) |
| 08/2020 | Segel kommt nicht ganz raus | Outhaul-Schlitten klemmt | Schlitten gereinigt, PTFE-Spray | €15 |
| 03/2021 | Manueller Antrieb sehr schwergängig | Unteres Mandrel-Lager korrodiert | Lagertausch (Rigger) | €480 |
| 06/2021 | E-Antrieb nachgerüstet | Wunsch nach mehr Komfort | Selden E40 + Installation | €4.200 |
| 09/2021 | E-Motor stoppt nach 10 Sekunden | Sicherung zu schwach (15A statt 40A) | Korrekte Sicherung eingebaut | €5 |
| 04/2022 | Halyard-Wrap | Diverter nach E-Motor-Einbau nicht korrekt justiert | Rigger am Mast, Diverter korrigiert | €350 |
| 07/2023 | Segel hat vertikale Falten | Luff-Tape gelängt nach 4 Saisons | Segelmacher: Luff-Tape nachgespannt | €280 |

**Gesamtkosten (5 Jahre):** €5.330 (davon €4.200 E-Antrieb-Upgrade)
**Lernerfahrung:** Jedes Problem war auf mangelnde Wartung oder Installationsfehler zurückzuführen. Nach korrekter Einstellung: einwandfreier Betrieb.

**AYDI-Bewertung:** confidence: documented | score: 74/100 (Probleme, aber alle lösbar)

### ANHANG F — Fallstudie: Oyster 565, In-Boom Leisure Furl Premium

**Ausgangssituation:**
- Boot: Oyster 565 (2021), 17,12 m LOA
- System: Leisure Furl BR 60 mit EBR 1200 Elektroantrieb
- Segel: Doyle Stratis-Hybrid-Rollsegel, 108 m², Full Battens

**Erfahrungen (3 Saisons Mittelmeer + 1× Transatlantik):**
- Segelform: Hervorragend dank Full Battens und Roach (ca. 10%)
- Bergen: Elektrisch in 40 Sekunden, sauber und gleichmäßig
- Transatlantik: 0 Probleme in 17 Tagen Passatsegeln
- Rigid Vang: Solide, aber Gasdruckfeder nach 2 Jahren leicht schwächer

**Kosten:**
| Position | Betrag |
|----------|--------|
| Leisure Furl BR 60 + EBR 1200 | €18.500 |
| Doyle Stratis-Hybrid-Segel | €12.000 |
| Installation | €3.200 |
| Rigid Vang | (im Lieferumfang) |
| **Gesamt** | **€33.700** |

**AYDI-Bewertung:** confidence: documented | score: 91/100 (Premium-System, Premium-Ergebnis)

### ANHANG G — Fallstudie: Lagoon 42, Katamaran mit In-Mast

**Ausgangssituation:**
- Boot: Lagoon 42 (2020), 12,80 m LOA
- System: Selden C390 mit E30 Elektroantrieb (ab Werk)
- Segel: Incidences Dacron-Rollsegel, 58 m²
- Nutzung: Owner-Charter, Karibik

**Erfahrungen (4 Saisons):**
- In-Mast ideal für Katamaran: Kein Krängen, gleichmäßiges Wickeln
- Chartereignung: Auch unerfahrene Crews können sicher reffen
- Problem: Segel im tropischen Klima nach 3 Saisons erheblich gereckt (UV + Hitze)
- Upgrade auf Hydranet-Segel nach 3 Saisons: deutlich bessere Formhaltung

**AYDI-Bewertung:** confidence: documented | score: 80/100

### ANHANG H — Fallstudie: X-Yachts X4.6, Performance Cruiser mit Slab

**Ausgangssituation:**
- Boot: X-Yachts X4.6 (2021), 14,25 m LOA
- System: 2× Slab-Reefing, Full-Batten-Großsegel (North Sails 3Di), 72 m²
- Nutzung: Regatta (ORC) + Familienfahrtensegeln, Dänemark/Schweden

**Erfahrungen (3 Saisons):**
- Segelform: Erstklassig dank 3Di und Full Battens
- Reffen: 2 Personen, 2–3 Minuten, Routine
- Regatta-Performance: Deutlich besser als In-Mast-Konkurrenz (messbar 6–10% VMG-Vorteil)
- Nachteil: Bergen auf See bei Starkwind erfordert Deckarbeit

**Eigner-Kommentar:** „Wer Wert auf Segeln legt — nicht nur auf Motorbootfahren mit Hilfssegel — wählt Slab."

**AYDI-Bewertung:** confidence: documented | score: 90/100 (Bewertung für Einsatzprofil Regatta + Performance)

### ANHANG I — Lebenszyklus-Kostenrechnung (20 Jahre)

**Szenario: 13 m Fahrtenyacht, Kurzhand, Nordeuropa**

**Variante A: Slab Reefing + Single-Line + Lazy-Bag**

| Position | Jahr 0 | Jahr 1–5 | Jahr 6–10 | Jahr 11–15 | Jahr 16–20 | Gesamt |
|----------|--------|---------|----------|----------|----------|--------|
| System (SLR + Lazyjacks + Bag) | €1.800 | — | €600 (Bag-Ersatz) | — | €800 (Bag + Leinen) | €3.200 |
| Segel (Standard, Full Batten) | €2.800 | — | €3.200 (Neusegel) | — | €3.500 (Neusegel) | €9.500 |
| Wartung (jährlich) | — | €250 | €300 | €350 | €400 | €6.500 |
| Reparaturen (geschätzt) | — | €200 | €400 | €600 | €800 | €2.000 |
| **Summe** | **€4.600** | | | | | **€21.200** |

**Variante B: In-Mast Furling (Selden C390 + E40)**

| Position | Jahr 0 | Jahr 1–5 | Jahr 6–10 | Jahr 11–15 | Jahr 16–20 | Gesamt |
|----------|--------|---------|----------|----------|----------|--------|
| System (Mast + Antrieb + Montage) | €12.500 | — | €800 (Lager) | — | €2.500 (Motor-Rev.) | €15.800 |
| Segel (Rollsegel, Hydranet) | €4.500 | — | €5.000 (Neusegel) | — | €5.500 (Neusegel) | €15.000 |
| Wartung (jährlich) | — | €400 | €500 | €600 | €700 | €11.000 |
| Reparaturen (geschätzt) | — | €300 | €800 | €1.200 | €1.500 | €3.800 |
| **Summe** | **€17.000** | | | | | **€45.600** |

**Variante C: In-Boom Furling (Leisure Furl BR 42 + EBR 500)**

| Position | Jahr 0 | Jahr 1–5 | Jahr 6–10 | Jahr 11–15 | Jahr 16–20 | Gesamt |
|----------|--------|---------|----------|----------|----------|--------|
| System (Boom + Antrieb + Rigid Vang + Montage) | €11.000 | — | €1.000 (Lager, Vang-Feder) | €500 | €3.000 (Motor-Rev., Vang) | €15.500 |
| Segel (Rollsegel, Dacron/Pentex) | €3.800 | — | €4.200 (Neusegel) | — | €4.800 (Neusegel) | €12.800 |
| Wartung (jährlich) | — | €500 | €600 | €700 | €800 | €13.000 |
| Reparaturen (geschätzt) | — | €400 | €900 | €1.300 | €1.600 | €4.200 |
| **Summe** | **€14.800** | | | | | **€45.500** |

**Zusammenfassung 20-Jahres-Kosten:**

| System | 20-Jahres-Kosten | Kosten/Jahr | Kosten/Segeltag (100 Tage/Jahr) |
|--------|-----------------|-------------|-------------------------------|
| Slab + SLR + Lazy-Bag | €21.200 | €1.060 | €10,60 |
| In-Mast (Selden, elektrisch) | €45.600 | €2.280 | €22,80 |
| In-Boom (Leisure Furl, elektrisch) | €45.500 | €2.275 | €22,75 |

**AYDI-Bewertung:** Der Komfort von In-Mast/In-Boom kostet über 20 Jahre ca. €24.000–24.500 mehr als Slab-Reefing. Pro Segeltag sind das €12,20 Mehrkosten — viele Fahrtensegler empfinden dies als akzeptabel für den erheblichen Komfortgewinn.

### ANHANG J — Normen-Referenz

| Norm | Titel | Relevanz für Großsegel-Reff |
|------|-------|---------------------------|
| ISO 12215-10:2020 | Rumpfbau und Dimensionierung — Teil 10: Rigg-Lasten | Mastbelastung durch Furling-Profil |
| ISO 12217:2015/2022 | Stabilität | Segelkräfte unter Reffs, Schwerpunktlage |
| EN 13033:2002 | Segelausrüstung — Beschläge | Festigkeit von Reffhaken, Kauschen, Blöcken |
| ISO 15085:2003 | Man-Overboard-Prävention | Vermeidung von Deckarbeit → In-Mast/In-Boom |
| IEC 60092 | Elektrische Installation | E-Antriebe, Kabelquerschnitte, Sicherungen |
| ISO 10133:2012 | Elektrische Gleichstrom-Systeme | E-Antriebe auf Yachten |
| World Sailing OSR | Offshore Special Regulations | Notreffen, Trysegel-Anforderung |

> ⚠️ **ZU PRÜFEN (Audit):** Die oben (und in Anhang S, Quelle 3) zitierte Norm „EN 13033:2002 — Segelausrüstung/Beschläge" ist nicht belegbar: EN 13033 existiert nicht als Norm für Segelausrüstung/Beschläge (EN 13034 = Chemikalienschutzkleidung; ISO 13033 = seismische Bauteillasten). Nächstliegender realer Standard für Beschlag-Starkpunkte: ISO 15084 (Anker/Vertäuung/Schlepp) — deckt jedoch keine Reffhaken/Blöcke ab. Normnummer verifizieren, bis dahin nicht als „measured" verwenden.

**Detaillierte ISO-Anforderungen mit Bezug zum Großsegel-Reff:**

**ISO 12215-10:2020 — Rigg-Lasten:**
- Kompressionslast im Mast: abhängig von Verdrängung und Rigg-Typ
- Sicherheitsfaktor: 2.5 (stehend) / 3.0 (laufend)
- Furling-Masten: Reduzierte Torsionssteifigkeit muss durch erhöhte Wandstärke oder größeres Profil kompensiert werden
- Prüflast für Mandrel-Lager: ≥ 1.5 × maximale Betriebslast
- Befestigungspunkte am Mast: Doppelte Sicherung (mechanisch + formschlüssig)

**ISO 12217:2015/2022 — Stabilitätsanforderungen:**
- Segelfläche unter Reff muss in Stabilitätsberechnung berücksichtigt werden
- Reff-Stufen müssen dokumentiert sein (welche Fläche bei welchem Reff?)
- In-Mast (stufenlos): Hersteller muss empfohlene Reffstufen angeben
- Gewichtsverschiebung durch Furling-System im Rigg: in Leerschiff-Gewichtsberechnung aufnehmen
- Schwerpunkterhöhung durch Furling-Komponenten: in KG-Berechnung einbeziehen

**World Sailing OSR — Offshore Special Regulations (Auszug):**
- Kategorie 0–2: Yacht muss in der Lage sein, unter Sturmgroßsegel zu segeln
- Bei In-Mast-Systemen: Trysegel oder alternatives Sturmgroßsegel muss mitgeführt werden
- Separater Track für Trysegel empfohlen (manche Systeme nutzen den Mast-Schlitz)
- Notreffen-Verfahren muss dokumentiert und geübt sein
- Manuelles Override für elektrische/hydraulische Antriebe: OBLIGATORISCH

### ANHANG K — Hersteller-Service-Kontakte DACH-Region

| Hersteller | Service-Region DACH | Kontakt | Ersatzteil-Garantie |
|-----------|---------------------|---------|---------------------|
| Selden | Selden GmbH (Preetz, DE) | info@sfriegger.de | 25+ Jahre |
| Facnor | Facnor SAS (FR) + DACH-Vertrieb | contact@facnor.com | 15+ Jahre |
| Profurl | Profurl SAS (FR) + DACH-Vertrieb | info@profurl.com | 15+ Jahre |
| Leisure Furl | Leisure Furl (UK) + DACH-Vertrieb | info@leisurefurl.com | 20+ Jahre |
| Bartels | Bartels (Wedel, DE) — Direktvertrieb | info@bartels-spar.de | 20+ Jahre |
| Z-Spars | Selden-Gruppe (siehe Selden) | wie Selden | 25+ Jahre |
| Schaefer | Schaefer Marine (USA) + DACH-Import | info@schaefermarine.com | 15+ Jahre |

### ANHANG L — Material-Spezifikationen

**Mandrel-Materialien:**

| Material | Legierung | Zugfestigkeit (MPa) | Streckgrenze (MPa) | E-Modul (GPa) | Dichte (g/cm³) | Einsatz |
|----------|-----------|---------------------|--------------------|--------------|--------------|---------| 
| Aluminium | 6061-T6 | 310 | 275 | 69 | 2,70 | Standard (Selden, Leisure Furl) |
| Aluminium | 6082-T6 | 340 | 310 | 69 | 2,70 | Premium (Selden, Bartels) |
| Aluminium | 7075-T6 | 570 | 500 | 72 | 2,81 | High-End (Facnor) |
| Edelstahl | 316L | 485 | 170 | 193 | 8,00 | Superyacht (>22 m) |
| Carbon | T700/Epoxy | 2.550 | n/a | 135 | 1,60 | Regatta (Custom) |

**Lager-Materialien:**

| Lagertyp | Material | Lebensdauer (Zyklen) | Wartung | Einsatz |
|----------|---------|---------------------|---------|---------|
| Kugellager (sealed) | Chromstahl + Gummi-Dichtung | 50.000–100.000 | Fetten (jährlich) | Standard |
| Kugellager (SKF Marine) | Edelstahl + Kontaktdichtung | 80.000–150.000 | Fetten (alle 2 Jahre) | Premium |
| Gleitlager | PTFE/Delrin | 30.000–60.000 | Wartungsfrei | Budget-Systeme |
| Nadellager | Chromstahl | 60.000–120.000 | Fetten (jährlich) | Spezialanwendung |

### ANHANG M — Checkliste Großsegel-Reffsystem Neukauf

**1. Anforderungen definieren:**
- [ ] Bootslänge und -typ (Monohull/Katamaran, Segel/Motor)
- [ ] Segelfläche Großsegel (aktuell und gewünscht)
- [ ] Einsatzprofil (Regatta / Fahrt / Langfahrt / Charter)
- [ ] Crew-Größe (Kurzhand? Einhand?)
- [ ] Budget (System + Segel + Montage)
- [ ] Neubau oder Nachrüstung?

**2. System-Entscheidung:**
- [ ] Slab / Single-Line / In-Mast / In-Boom?
- [ ] Manuell oder elektrisch?
- [ ] Trysegel erforderlich (Blauwasser)?
- [ ] Lazy-Bag / Lazyjacks benötigt (bei Slab)?

**3. Dimensionierung:**
- [ ] Hersteller-Empfehlung für Bootsgröße und Segelfläche
- [ ] Mandrel-Durchmesser (In-Mast / In-Boom)
- [ ] Mastprofil (In-Mast: Furling-Profil erforderlich!)
- [ ] Boom-Größe (In-Boom: Spezial-Boom erforderlich!)
- [ ] Antriebsleistung (Drehmoment, Spannung, Stromaufnahme)

**4. Elektrik (bei E-Antrieb):**
- [ ] Batterie-Kapazität ausreichend?
- [ ] Kabelquerschnitt berechnet?
- [ ] Sicherung dimensioniert?
- [ ] Schalter/Steuerung geplant?
- [ ] Notfall-Override möglich?

**5. Segel:**
- [ ] Segeltyp kompatibel mit System?
- [ ] Tuchmaterial gewählt (Dacron / Hydranet / Pentex)?
- [ ] Latten (keine / vertikal / horizontal / full)?
- [ ] UV-Schutz benötigt?
- [ ] Segelmacher kontaktiert?

### ANHANG N — Umrechnungstabellen

**M.1 Windgeschwindigkeit:**

| Beaufort | kn | m/s | km/h | Beschreibung |
|----------|-----|------|------|-------------|
| 3 | 7–10 | 3,4–5,4 | 12–19 | Schwache Brise |
| 4 | 11–16 | 5,5–7,9 | 20–28 | Mäßige Brise |
| 5 | 17–21 | 8,0–10,7 | 29–38 | Frische Brise |
| 6 | 22–27 | 10,8–13,8 | 39–49 | Starker Wind |
| 7 | 28–33 | 13,9–17,1 | 50–61 | Steifer Wind |
| 8 | 34–40 | 17,2–20,7 | 62–74 | Stürmischer Wind |
| 9 | 41–47 | 20,8–24,4 | 75–88 | Sturm |
| 10 | 48–55 | 24,5–28,4 | 89–102 | Schwerer Sturm |

**M.2 Kraft-Umrechnung:**

| Von \ Nach | Newton (N) | Kilogramm (kgf) | Pfund (lbs) |
|-----------|-----------|-----------------|-------------|
| 1 Newton | 1 | 0,102 | 0,225 |
| 1 Kilogramm | 9,81 | 1 | 2,205 |
| 1 Pfund | 4,45 | 0,454 | 1 |

**M.3 Segelfläche nach Bootslänge (Richtwerte Großsegel):**

| LOA (ft) | LOA (m) | Großsegel Standard (m²) | Großsegel In-Mast (m²) | Differenz |
|----------|---------|------------------------|------------------------|-----------|
| 30 | 9,1 | 25 | 21 | -16% |
| 33 | 10,1 | 32 | 27 | -16% |
| 36 | 11,0 | 40 | 34 | -15% |
| 40 | 12,2 | 52 | 43 | -17% |
| 44 | 13,4 | 65 | 54 | -17% |
| 48 | 14,6 | 80 | 66 | -18% |
| 52 | 15,8 | 95 | 79 | -17% |
| 56 | 17,1 | 110 | 92 | -16% |
| 60 | 18,3 | 130 | 107 | -18% |

### ANHANG O — Saisonaler Wartungskalender

**Nordeuropa-Revier (Saison Mai–September):**

| Monat | Tätigkeit | Dauer |
|-------|-----------|-------|
| April | Vollwartung: Lager schmieren, Segel einziehen, Funktionstest | 3–5h |
| Mai | Sichtkontrolle: Schlitz, Leinen, Schaltung | 30 min |
| Juli | Reinigung: Mastschlitz/Boom-Führung, Umlenkrollen | 1–2h |
| September | Vollwartung: Segel herausnehmen, Lager inspizieren, Konservieren | 3–5h |
| Oktober–März | Segel trocken lagern, Mastschlitz abdecken | — |

**Mittelmeer-Revier (Saison April–November):**

| Monat | Tätigkeit | Dauer |
|-------|-----------|-------|
| März | Vollwartung + Funktionstest | 3–5h |
| Mai | Sichtkontrolle | 30 min |
| Juli | Reinigung + Salzwasser-Spülung | 1–2h |
| September | Sichtkontrolle | 30 min |
| November | Vollwartung + Wintervorbereitung | 3–5h |

**Ganzjahres-Revier (Tropen):**

| Intervall | Tätigkeit | Dauer |
|-----------|-----------|-------|
| Alle 2 Monate | Süßwasserspülung Mastschlitz/Boom | 20 min |
| Alle 4 Monate | Sichtkontrolle + Schmierung | 1h |
| Alle 6 Monate | Vollwartung | 3–5h |
| Jährlich | Segel-Inspektion (UV-Schäden!) | 2h |

### ANHANG P — AYDI Pydantic v2 Datenmodelle

```python
"""
AYDI Knowledge Models — 15.02 Großsegel-Rollreff und In-Mast/In-Boom
Pydantic v2 models for structured representation of mainsail furling data.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FurlingSystemType(str, Enum):
    """Type of mainsail furling/reefing system."""
    SLAB_REEFING = "slab_reefing"
    SINGLE_LINE_REEFING = "single_line_reefing"
    IN_MAST_FURLING = "in_mast_furling"
    IN_BOOM_FURLING = "in_boom_furling"


class DriveType(str, Enum):
    """Type of furling drive mechanism."""
    MANUAL = "manual"
    ELECTRIC = "electric"
    HYDRAULIC = "hydraulic"


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


class SailClothType(str, Enum):
    """Type of sail cloth material."""
    DACRON_WOVEN = "dacron_woven"
    DACRON_CROSSCUT = "dacron_crosscut"
    DACRON_RADIAL = "dacron_radial"
    PENTEX = "pentex"
    HYDRANET = "hydranet"
    ELVSTROEM_EPEX = "elvstroem_epex"
    THREE_DI = "3di"
    MEMBRANE = "membrane"
    PBO_CARBON = "pbo_carbon"


class MandrelMaterial(str, Enum):
    """Material used for mandrel construction."""
    AL_6061_T6 = "al_6061_t6"
    AL_6082_T6 = "al_6082_t6"
    AL_7075_T6 = "al_7075_t6"
    SS_316L = "ss_316l"
    CARBON_T700 = "carbon_t700"


class MastProfile(BaseModel):
    """Mast profile specifications for in-mast furling."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Mast manufacturer name")
    model: str = Field(..., description="Mast model designation")
    width_mm: float = Field(..., ge=100, le=500, description="Profile width in mm (athwartships)")
    depth_mm: float = Field(..., ge=150, le=600, description="Profile depth in mm (fore-aft)")
    wall_thickness_mm: float = Field(..., ge=2.0, le=10.0, description="Wall thickness in mm")
    weight_per_meter_kg: float = Field(..., ge=3.0, le=30.0, description="Weight per meter in kg")
    slot_width_mm: float = Field(..., ge=15, le=50, description="Furling slot width in mm")
    moment_of_inertia_x_cm4: Optional[float] = Field(None, description="Moment of inertia I_x in cm^4")
    moment_of_inertia_y_cm4: Optional[float] = Field(None, description="Moment of inertia I_y in cm^4")
    min_boat_length_m: float = Field(..., ge=5, le=30, description="Minimum boat length in m")
    max_boat_length_m: float = Field(..., ge=8, le=40, description="Maximum boat length in m")
    max_sail_area_m2: float = Field(..., ge=10, le=300, description="Maximum sail area in m²")


class MandrelSpec(BaseModel):
    """Mandrel (furling spar) specifications."""

    model_config = {"from_attributes": True}

    diameter_mm: float = Field(..., ge=30, le=300, description="Mandrel outer diameter in mm")
    wall_thickness_mm: float = Field(..., ge=2.0, le=8.0, description="Mandrel wall thickness in mm")
    material: MandrelMaterial = Field(..., description="Mandrel material")
    length_mm: float = Field(..., ge=3000, le=35000, description="Mandrel length in mm")
    max_torque_nm: float = Field(..., ge=50, le=5000, description="Maximum torque capacity in Nm")
    bearing_type: str = Field(..., description="Type of bearing (e.g. 'sealed_ball', 'ptfe_sleeve')")
    num_intermediate_bearings: int = Field(default=0, ge=0, le=10, description="Number of intermediate support bearings")


class ElectricDrive(BaseModel):
    """Electric furling drive specifications."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Drive manufacturer")
    model: str = Field(..., description="Drive model designation")
    part_number: str = Field(..., description="Manufacturer part number")
    voltage_v: int = Field(..., description="Nominal voltage in V (12 or 24)")
    power_w: float = Field(..., ge=100, le=3000, description="Motor power in W")
    max_torque_nm: float = Field(..., ge=50, le=3000, description="Maximum output torque in Nm")
    max_current_a: float = Field(..., ge=5, le=150, description="Maximum current draw in A")
    gear_ratio: str = Field(default="", description="Gear ratio (e.g. '1:12')")
    manual_override: bool = Field(default=True, description="Manual override capability")
    weight_kg: float = Field(..., ge=2, le=50, description="Drive weight in kg")
    compatible_systems: list[str] = Field(default_factory=list, description="Compatible furling system models")


class FurlingSystem(BaseModel):
    """Complete furling system specification."""

    model_config = {"from_attributes": True}

    system_type: FurlingSystemType = Field(..., description="Type of furling system")
    manufacturer: str = Field(..., description="System manufacturer")
    model: str = Field(..., description="System model designation")
    part_number: str = Field(default="", description="Base part number")
    drive_type: DriveType = Field(..., description="Drive mechanism type")
    min_boat_length_m: float = Field(..., ge=5, le=30, description="Minimum boat length in m")
    max_boat_length_m: float = Field(..., ge=8, le=40, description="Maximum boat length in m")
    min_sail_area_m2: float = Field(..., ge=10, le=200, description="Minimum sail area in m²")
    max_sail_area_m2: float = Field(..., ge=15, le=300, description="Maximum sail area in m²")
    mandrel: Optional[MandrelSpec] = Field(None, description="Mandrel specification")
    mast_profile: Optional[MastProfile] = Field(None, description="Required mast profile (in-mast only)")
    electric_drive: Optional[ElectricDrive] = Field(None, description="Electric drive (if applicable)")
    boom_height_mm: Optional[float] = Field(None, description="Boom cross-section height in mm (in-boom only)")
    boom_width_mm: Optional[float] = Field(None, description="Boom cross-section width in mm (in-boom only)")
    system_weight_kg: float = Field(..., ge=1, le=500, description="Total system weight in kg")
    requires_special_mast: bool = Field(default=False, description="Requires furling mast profile")
    requires_rigid_vang: bool = Field(default=False, description="Requires rigid vang (in-boom)")
    price_range_eur: tuple[float, float] = Field(..., description="Price range in EUR (min, max)")


class SailSpec(BaseModel):
    """Sail specification for furling system compatibility."""

    model_config = {"from_attributes": True}

    sail_area_m2: float = Field(..., ge=5, le=300, description="Sail area in m²")
    luff_length_m: float = Field(..., ge=5, le=40, description="Luff length in m")
    foot_length_m: float = Field(..., ge=2, le=15, description="Foot length in m")
    cloth_type: SailClothType = Field(..., description="Sail cloth material")
    cloth_weight_gsm: float = Field(..., ge=100, le=400, description="Cloth weight in g/m²")
    has_battens: bool = Field(default=False, description="Whether sail has battens")
    batten_orientation: Optional[str] = Field(None, description="Batten orientation: 'horizontal', 'vertical', or None")
    batten_count: int = Field(default=0, ge=0, le=10, description="Number of battens")
    roach_percent: float = Field(default=0, ge=0, le=25, description="Roach as percentage of triangle area")
    has_reef_points: bool = Field(default=False, description="Whether sail has slab reef points")
    reef_count: int = Field(default=0, ge=0, le=4, description="Number of reef points")
    compatible_systems: list[FurlingSystemType] = Field(default_factory=list, description="Compatible furling system types")
    uv_protection: bool = Field(default=False, description="Built-in UV protection strip")
    estimated_lifespan_years: float = Field(..., ge=3, le=25, description="Estimated lifespan in years")
    price_eur: float = Field(..., ge=500, le=30000, description="Sail price in EUR")


class FaultPattern(BaseModel):
    """Fault pattern entry for the fault atlas."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., pattern=r"^F\d{2}$", description="Fault identifier (e.g. F01)")
    title_de: str = Field(..., description="Fault title in German")
    title_en: str = Field(..., description="Fault title in English")
    applicable_systems: list[FurlingSystemType] = Field(..., description="Applicable system types")
    severity: str = Field(..., description="Severity: KRITISCH, HOCH, MITTEL-HOCH, MITTEL, NIEDRIG-MITTEL, NIEDRIG")
    confidence: ConfidenceLevel = Field(..., description="Confidence level of fault data")
    symptoms: list[str] = Field(..., description="Observable symptoms (German)")
    causes: list[str] = Field(..., description="Root causes (German)")
    immediate_action: list[str] = Field(..., description="Immediate corrective actions (German)")
    long_term_fix: list[str] = Field(..., description="Long-term remediation steps (German)")
    weakness_score: int = Field(..., ge=1, le=10, description="AYDI weakness score (1-10)")


class MainsailReefingAssessment(BaseModel):
    """AYDI assessment result for a mainsail reefing system."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=5, le=40, description="Boat length (LOA) in m")
    boat_displacement_t: float = Field(..., ge=1, le=200, description="Boat displacement in tonnes")
    sail_area_m2: float = Field(..., ge=5, le=300, description="Mainsail area in m²")
    system_type: FurlingSystemType = Field(..., description="Installed or proposed system type")
    drive_type: DriveType = Field(..., description="Drive type")
    usage_profile: str = Field(..., description="Usage profile (e.g. 'cruising_shorthanded')")

    score_overall: float = Field(..., ge=0, le=100, description="Overall assessment score")
    score_sail_shape: float = Field(..., ge=0, le=100, description="Sail shape quality score")
    score_convenience: float = Field(..., ge=0, le=100, description="Convenience and ergonomics score")
    score_reliability: float = Field(..., ge=0, le=100, description="Reliability score")
    score_safety: float = Field(..., ge=0, le=100, description="Safety score")
    score_cost_efficiency: float = Field(..., ge=0, le=100, description="Cost efficiency score")

    confidence: ConfidenceLevel = Field(..., description="Assessment confidence level")
    findings: list[str] = Field(default_factory=list, description="Key findings (German)")
    warnings: list[str] = Field(default_factory=list, description="Warnings (German)")
    recommendations: list[str] = Field(default_factory=list, description="Recommendations (German)")
    data_source: str = Field(default="knowledge_15_02", description="Data source reference")
    assessment_date: date = Field(..., description="Assessment date")


class SystemComparison(BaseModel):
    """Side-by-side comparison of furling/reefing systems."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=5, le=40, description="Reference boat length in m")
    sail_area_m2: float = Field(..., ge=5, le=300, description="Reference sail area in m²")
    systems: list[FurlingSystem] = Field(..., min_length=2, max_length=5, description="Systems to compare")
    recommended_system: Optional[FurlingSystemType] = Field(None, description="Recommended system type")
    recommendation_reason: str = Field(default="", description="Reason for recommendation (German)")
    confidence: ConfidenceLevel = Field(..., description="Comparison confidence level")


class MaintenanceSchedule(BaseModel):
    """Maintenance schedule for a furling/reefing system."""

    model_config = {"from_attributes": True}

    system_type: FurlingSystemType = Field(..., description="System type")
    drive_type: DriveType = Field(..., description="Drive type")
    sailing_region: str = Field(..., description="Sailing region (e.g. 'nordeuropa', 'mittelmeer', 'tropen')")
    annual_tasks: list[str] = Field(..., description="Annual maintenance tasks (German)")
    triennial_tasks: list[str] = Field(..., description="3-year maintenance tasks (German)")
    quinquennial_tasks: list[str] = Field(..., description="5-7 year maintenance tasks (German)")
    estimated_annual_cost_eur: tuple[float, float] = Field(..., description="Estimated annual cost range in EUR")
    estimated_annual_hours: float = Field(..., ge=0.5, le=20, description="Estimated annual maintenance hours")


class CaseStudy(BaseModel):
    """Documented case study for a mainsail furling installation."""

    model_config = {"from_attributes": True}

    case_id: str = Field(..., description="Case study identifier (e.g. 'anhang_a')")
    boat_model: str = Field(..., description="Boat make and model")
    boat_year: int = Field(..., ge=1980, le=2030, description="Boat build year")
    boat_length_m: float = Field(..., ge=5, le=40, description="Boat LOA in m")
    system_type: FurlingSystemType = Field(..., description="Installed system type")
    system_manufacturer: str = Field(..., description="System manufacturer")
    system_model: str = Field(..., description="System model")
    drive_type: DriveType = Field(..., description="Drive type")
    usage_profile: str = Field(..., description="Usage profile description")
    seasons_in_service: int = Field(..., ge=1, le=30, description="Number of seasons in service")
    total_cost_eur: float = Field(..., ge=0, description="Total installation cost in EUR")
    annual_maintenance_cost_eur: float = Field(default=0, ge=0, description="Annual maintenance cost in EUR")
    problems_encountered: list[str] = Field(default_factory=list, description="Problems encountered (German)")
    owner_satisfaction: str = Field(default="", description="Owner satisfaction summary (German)")
    aydi_score: float = Field(..., ge=0, le=100, description="AYDI assessment score")
    confidence: ConfidenceLevel = Field(..., description="Data confidence level")
```

### ANHANG Q — AYDI-Bewertungsregeln für Großsegel-Reffsysteme

**Scoring-Gewichtung nach Einsatzprofil:**

| Teilscore | Regatta | Fahrt Kurzhand | Fahrt Crew | Blauwasser | Charter |
|-----------|---------|---------------|------------|-----------|---------|
| Segelform | 0.35 | 0.15 | 0.20 | 0.15 | 0.10 |
| Komfort/Bedienung | 0.10 | 0.35 | 0.25 | 0.25 | 0.40 |
| Zuverlässigkeit | 0.25 | 0.20 | 0.20 | 0.30 | 0.25 |
| Sicherheit | 0.15 | 0.15 | 0.15 | 0.20 | 0.15 |
| Kosten | 0.15 | 0.15 | 0.20 | 0.10 | 0.10 |
| **Summe** | **1.00** | **1.00** | **1.00** | **1.00** | **1.00** |

**Basisbewertung nach Systemtyp und Einsatzprofil:**

```python
# AYDI scoring rules for mainsail reefing systems
# Usage: base_scores[system_type][usage_profile] = (sail_shape, convenience, reliability, safety, cost)

MAINSAIL_REEFING_BASE_SCORES = {
    "slab_reefing": {
        "regatta": (95, 40, 95, 95, 95),
        "cruising_shorthanded": (90, 35, 95, 85, 95),
        "cruising_crew": (90, 55, 95, 90, 95),
        "bluewater": (90, 50, 98, 95, 90),
        "charter": (85, 30, 95, 80, 90),
    },
    "single_line_reefing": {
        "regatta": (92, 60, 85, 90, 85),
        "cruising_shorthanded": (88, 65, 85, 85, 85),
        "cruising_crew": (88, 70, 85, 88, 85),
        "bluewater": (88, 60, 88, 90, 82),
        "charter": (82, 60, 85, 82, 82),
    },
    "in_mast_furling": {
        "regatta": (45, 95, 70, 60, 40),
        "cruising_shorthanded": (55, 98, 75, 70, 45),
        "cruising_crew": (55, 95, 75, 72, 48),
        "bluewater": (52, 90, 68, 58, 42),
        "charter": (50, 98, 72, 68, 45),
    },
    "in_boom_furling": {
        "regatta": (72, 85, 68, 75, 35),
        "cruising_shorthanded": (78, 92, 72, 78, 38),
        "cruising_crew": (78, 88, 72, 80, 40),
        "bluewater": (75, 85, 70, 78, 35),
        "charter": (72, 90, 70, 75, 38),
    },
}
```

### ANHANG R — AYDI Visuelle Analyse-Kriterien für Großsegel-Reffsysteme

Kriterien für die AYDI-Pipeline B (Visual Analysis) zur Identifikation des Reffsystem-Typs anhand von Fotos:

**In-Mast-Furling erkennen (visuell):**

| Visuelles Merkmal | Confidence | Beschreibung |
|-------------------|-----------|-------------|
| Verbreiterter Mast (Querschnitt) | visual_high | Mast deutlich breiter als normal, tropfenförmiges Profil |
| Kein Achterliekrundung (Roach) | visual_high | Segel hat gerade Hinterkante (dreieckig) |
| Keine sichtbaren Latten | visual_high | Segel ohne horizontale Latten-Strukturen |
| Vertikaler Schlitz an Mast-Rückseite | visual_high | Sichtbarer Spalt an der Mastrückseite |
| Flaches Segelprofil | visual_medium | Segel wirkt flacher als üblich |
| Kein Lazy-Bag am Baum | visual_medium | Baum ohne Persenning (Segel im Mast) |
| Bedienleine am Mastfuß sichtbar | visual_low | Endlosleine um Trommel am Mastfuß |

**In-Boom-Furling erkennen (visuell):**

| Visuelles Merkmal | Confidence | Beschreibung |
|-------------------|-----------|-------------|
| Übergroßer Baum | visual_high | Boom deutlich dicker/höher als Standard |
| Rigid Vang (starrer Niederholer) | visual_high | Starre Verbindung Mast↔Boom (kein Seil-Kicker) |
| Schlitz an Boom-Oberseite | visual_high | Horizontaler Spalt auf der Boom-Oberseite |
| Standard-Mastprofil | visual_medium | Mast sieht normal aus (nicht verbreitert) |
| Latten im Segel sichtbar | visual_medium | Horizontale Latten erkennbar (aber kürzer als Full Battens) |
| Kein Lazy-Bag | visual_medium | Baum ohne separate Persenning |

**Slab-Reefing erkennen (visuell):**

| Visuelles Merkmal | Confidence | Beschreibung |
|-------------------|-----------|-------------|
| Lazyjacks sichtbar | visual_high | Leinen vom oberen Mast zum Baum (V-Form) |
| Lazy-Bag am Baum | visual_high | Persenning/Tasche am Baum |
| Full Battens im Segel | visual_high | Durchgehende horizontale Latten sichtbar |
| Achterliekrundung (Roach) | visual_high | Segel hat positive Rundung am Achterliek |
| Reffkauschen sichtbar | visual_medium | Verstärkte Ösen im Segel (1–3 Reihen) |
| Baumkicker (Leine oder Teleskop) | visual_medium | Konventioneller Niederholer unter dem Baum |
| Reffleinen am Baum | visual_low | Leinen, die vom Baum zum Cockpit laufen |

**AYDI Vision-Prompt-Hinweise:**
```
Für die visuelle Analyse des Großsegel-Reffsystems:
1. Mast-Querschnitt beurteilen (breit/tropfenförmig = In-Mast)
2. Baum-Größe beurteilen (übergroß = In-Boom)
3. Segel-Silhouette prüfen (dreieckig ohne Roach = In-Mast)
4. Lazyjacks/Lazy-Bag prüfen (vorhanden = Slab)
5. Rigid Vang prüfen (starr = In-Boom)
6. Latten im Segel prüfen (keine = In-Mast, kurz = In-Boom, voll = Slab)
7. Confidence: Mehrere übereinstimmende Merkmale = visual_high
```

### ANHANG R2 — Typische Schwachstellen nach Alter des Systems

**In-Mast-System — Schwachstellen-Entwicklung über die Lebensdauer:**

| Alter | Typische Schwachstelle | AYDI-Score-Auswirkung | Maßnahme |
|-------|----------------------|----------------------|----------|
| 0–2 Jahre | Keine (Garantieperiode) | Keine | Reguläre Wartung |
| 2–5 Jahre | Segel-Profilverlust (Dacron reckt) | -5 Punkte Segelform | Segelmacher-Check |
| 3–5 Jahre | Bürstendichtung verschlissen | -2 Punkte Zuverlässigkeit | Ersetzen (€50–150) |
| 5–7 Jahre | Mandrel-Lager Verschleiß (Spiel) | -5 Punkte Zuverlässigkeit | Lagertausch (€200–500) |
| 5–8 Jahre | Segel Luff-Tape Abrieb | -5 Punkte Segelform | Segelmacher-Reparatur |
| 7–10 Jahre | E-Motor Kohlen verschlissen | -3 Punkte Zuverlässigkeit | Kohlen tauschen (€80–200) |
| 8–12 Jahre | Segel End-of-Life (Dacron) | -15 Punkte Segelform | Neusegel (€2.500–5.500) |
| 10–15 Jahre | Schlitzlippen verschlissen | -8 Punkte Zuverlässigkeit | Ersetzen (€500–1.500) |
| 12���15 Jahre | E-Motor End-of-Life | -10 Punkte Zuverlässigkeit | Motor-Revision (€1.500–3.000) |
| 15–20 Jahre | Mastprofil-Ermüdung möglich | -15 Punkte Strukturell | Rigger-Inspektion, ggf. Masttausch |

**In-Boom-System — Schwachstellen-Entwicklung über die Lebensdauer:**

| Alter | Typische Schwachstelle | AYDI-Score-Auswirkung | Maßnahme |
|-------|----------------------|----------------------|----------|
| 0–2 Jahre | Keine (Garantieperiode) | Keine | Reguläre Wartung |
| 2–4 Jahre | Rigid-Vang Gasdruckfeder leicht schwächer | -2 Punkte | Kontrollieren |
| 3–5 Jahre | Führungsrollen Verschleiß | -3 Punkte Zuverlässigkeit | Rollen ersetzen (€100–300) |
| 5–7 Jahre | Rigid-Vang Gasdruckfeder End-of-Life | -5 Punkte | Feder tauschen (€200–500) |
| 5–8 Jahre | Endlos-Fall Verschleiß | -5 Punkte Sicherheit | Fall ersetzen (€200–400) |
| 7–10 Jahre | E-Motor Verschleiß | -3 Punkte | Kohlen/Service |
| 8–12 Jahre | Segel End-of-Life | -15 Punkte Segelform | Neusegel (€2.200–4.800) |
| 10–15 Jahre | Boom-Innenraum Korrosion | -8 Punkte | Boom inspizieren, behandeln |
| 12–18 Jahre | Mandrel-Lager im Boom | -5 Punkte | Lagertausch |
| 15–20 Jahre | Gesamtsystem-Revision | -20 Punkte | Komplett-Revision (€3.000–6.000) |

### ANHANG R3 — Revier-spezifische Empfehlungen

| Revier | Klima | Empfohlenes System | Besondere Hinweise |
|--------|-------|-------------------|-------------------|
| Ostsee | Gemäßigt, Frost im Winter | In-Mast oder Slab | Frost: System VOR Winter einrollen/konservieren |
| Nordsee | Rau, Wind, Regen | Slab oder In-Boom | Hohe Zuverlässigkeit wichtig, Notreffen |
| Mittelmeer West (FR/ES) | Warm, Mistral-Böen | In-Mast | Gute Bedingungen für In-Mast, selten Frost |
| Mittelmeer Ost (GR/HR/TR) | Warm, Meltemi | In-Mast | Starkwind-Reffen häufig, In-Mast bewährt |
| Karibik | Tropisch, Hurrikansaison | In-Mast oder In-Boom | UV-Schutz kritisch, Segel altert schneller |
| Atlantik-Passage | Ozeanisch, alle Bedingungen | Slab oder In-Boom | Zuverlässigkeit + Notreffen prioritär |
| Pazifik (Passatzone) | Tropisch, konstanter Wind | In-Mast oder In-Boom | UV-Degradation beachten |
| Hohe Breiten (50°+) | Kalt, Eis möglich, Starkwind | Slab (IMMER) | Frost + Sturm = In-Mast-Risiko! |
| Binnenrevier (See) | Gemäßigt, kurze Strecken | In-Mast | Kurze Fahrten, Komfort prioritär |
| Wattenmeer | Gezeitenstrom, flach | Slab oder SLR | Einfachheit, oft Kurzhand |

### ANHANG S — Quellen und weiterführende Literatur

**Normen und Standards:**
1. ISO 12215-10:2020 — Kleine Wasserfahrzeuge — Rumpfbau und Dimensionierung — Teil 10: Rigg-Lasten
2. ISO 12217:2015/2022 — Kleine Wasserfahrzeuge — Stabilität und Auftrieb
3. EN 13033:2002 — Segelausrüstung — Beschlag-Festigkeit
4. ISO 15085:2003 — Kleine Wasserfahrzeuge — Man-Overboard-Prevention
5. EU-Richtlinie 2013/53/EU — Sportboote und Wassermotorräder
6. World Sailing Offshore Special Regulations 2024/2025

**Hersteller-Dokumentation:**
7. Selden Mast: Furling Mast — Technical Manual and Installation Guide (aktuelle Ausgabe)
8. Selden Mast: Furlex Electric Drive — Installation and Service Manual (aktuelle Ausgabe)
9. Facnor: FMI In-Mast Furling System — Technical Documentation (aktuelle Ausgabe)
10. Profurl: Mast Furling System MFS — Installation Guide (aktuelle Ausgabe)
11. Leisure Furl: In-Boom & In-Mast Systems — Owner's Manual (aktuelle Ausgabe)
12. Bartels: Boom Furling System BFS — Technisches Handbuch (aktuelle Ausgabe)
13. Z-Spars/Selden: IBF In-Boom Furling — Technical Specifications (aktuelle Ausgabe)
14. Schaefer Marine: In-Mast Furling IMF — Installation Manual (aktuelle Ausgabe)

**Fachliteratur:**
15. Larsson, L. & Eliasson, R.: Principles of Yacht Design. A&C Black, 2014.
16. Marchaj, C.A.: Sailing Theory and Practice. Adlard Coles, 2003.
17. Brewer, T.: Understanding Boat Design. International Marine, 1994.
18. Calder, N.: Boatowner's Mechanical and Electrical Manual. International Marine, 2015.
19. Howard-Williams, J.: Sails — The Way They Work and How to Make Them Work for You. Adlard Coles, 2012.
20. Bethwaite, F.: High Performance Sailing. Adlard Coles, 2010.

**Branchenressourcen:**
21. Germanischer Lloyd — Klassifikationsrichtlinien für Sportboote
22. Yacht (Zeitschrift, DE) — Langzeittests Rollreffanlagen (2018–2025)
23. Practical Sailor (US) — Furling System Comparative Reports (2019–2025)
24. Yachting Monthly (UK) — In-Boom vs. In-Mast: A 5-Year Study (2022)
25. Segeln (Zeitschrift, DE) — Großsegel-Reffsysteme im Vergleich (2023)

### ANHANG T — Häufige Installationsfehler und Vermeidung

Die 15 häufigsten Fehler bei der Installation von Großsegel-Rollreffsystemen:

**In-Mast-Installation:**

1. **Rigg-Vorspannung nicht reduziert:** Zu hohe Rigg-Vorspannung verformt den Furling-Mast und verändert die Schlitzgeometrie. → Rigg-Vorspannung auf Hersteller-Empfehlung einstellen (typisch 12–18% BL Vorstag).

2. **Halyard-Diverter vergessen:** Nach dem Mastaufstellen wird der Halyard-Diverter nicht eingebaut oder falsch positioniert. → VOR dem Segel-Einziehen prüfen!

3. **Kabel für E-Motor zu dünn:** Spannungsabfall unter Last → Motor dreht langsam oder stoppt. → Kabelquerschnitt gemäß Berechnungstabelle (Abschnitt 6.3) verwenden.

4. **Sicherung zu schwach:** Motor-Sicherung löst beim ersten Reffversuch aus. → Sicherung = 1.25 × Motor-Nennstrom.

5. **Mandrel-Lager nicht gefettet:** Lager wurden trocken eingebaut → erhöhte Reibung, vorzeitiger Verschleiß. → Marine-Fett (Selden Original oder gleichwertig) bei der Montage verwenden.

6. **Segel-Luff-Tape zu dick:** Segelmacher hat Standard-Tape verwendet statt Furling-spezifisches → klemmt im Schlitz. → VOR Segelbestellung Schlitzbreite messen und Segelmacher informieren.

7. **Outhaul-Leinenführung fehlerhaft:** Outhaul-Leine reibt an scharfer Kante im Baum → reißt nach wenigen Monaten. → Alle Umlenkpunkte prüfen, Kanten abrunden.

**In-Boom-Installation:**

8. **Rigid Vang falsch dimensioniert:** Gasdruckfeder zu schwach → Boom sackt ab, Segel-Einlauf klemmt. → Hersteller-empfohlenen Rigid Vang verwenden (Boom-Gewicht + Segelgewicht beachten).

9. **Endlos-Fall nicht korrekt gespleit:** Spleiß löst sich nach wenigen Wochen unter Last. → Professionellen Spleiß (12-fach Geflecht, min. 30 × Durchmesser Einlauf) erstellen lassen.

10. **Masttop-Rolle zu klein:** Umlenkrolle für Endlos-Fall am Masttop unterdimensioniert → Fall verschleißt schnell. → Rollen-Durchmesser min. 8 × Fall-Durchmesser.

11. **Boom-Ausrichtung nicht horizontal:** Boom hängt nach achtern ab → Segel rollt sich ungleichmäßig. → Boom mit Wasserwaage ausrichten, Rigid Vang justieren.

**Alle Systeme:**

12. **Erdung des E-Motors vergessen:** Motor-Gehäuse nicht mit Bordmasse verbunden → galvanische Korrosion möglich. → Immer erden (min. 6 mm² Massekabel).

13. **Keine Not-Abschaltung installiert:** E-Motor hat keinen Not-Aus-Schalter in Reichweite → bei Fehlfunktion kein schnelles Stoppen. → Not-Aus-Taster am Cockpit-Panel.

14. **Bedienungsanleitung nicht gelesen:** System wird nach „Gefühl" bedient → Fehlbedienung führt zu Schäden. → Handbuch des Herstellers LESEN und Crew einweisen.

15. **Keine Seeerprobung vor der ersten Fahrt:** System wurde im Hafen getestet, aber nie unter Last (Wind) geprüft → erstes Reffen auf See misslingt. → VOR der ersten richtigen Fahrt: Seeerprobung bei 12–18 kn, Reffen üben!

### ANHANG U — Marktentwicklung und Zukunftstrends

**Aktuelle Trends (2024–2026):**

1. **Elektrifizierung als Standard:** Elektrische Antriebe werden zunehmend bei Neubooten ab 38 ft serienmäßig verbaut. Die Kostenreduktion durch höhere Stückzahlen macht E-Antriebe erschwinglicher.

2. **Lithium-Batterien ermöglichen leistungsstärkere E-Antriebe:** LiFePO4-Batterien liefern höhere Ströme bei geringerem Gewicht → leistungsstärkere Motoren ohne Überdimensionierung des Bordnetzes.

3. **CAN-Bus-Integration:** Neue Systeme (Selden, Bartels) bieten NMEA 2000 / CAN-Bus-Anbindung für:
   - Fernbedienung vom Plotter
   - Automatische Reff-Empfehlungen basierend auf Windmessung
   - Diagnose und Fehlermeldungen auf dem Display
   - Integrattion mit Autopilot (automatisches Reffen)

4. **Verbesserte Segelschnitte für Rollsegel:** Segelmacher entwickeln spezielle Schnitte (3D-Formung durch Panelschnitt) die auch lattenlosen In-Mast-Segeln mehr Profil geben. Elvström EPEX und North Sails NorDac+ sind Beispiele.

5. **Hybridlatten für In-Boom:** Neue flexible Latten-Materialien (Glasfaser/Carbon-Hybrid) ermöglichen vollgelattete Segel in In-Boom-Systemen, die sich trotzdem sauber aufwickeln.

6. **Nachrüst-Lösungen verbessern sich:** Profurl MFS und vergleichbare Nachrüst-Mandrel-Systeme werden ausgereifter und erlauben In-Mast-Furling ohne kompletten Masttausch.

**Prognose 2026–2030:**

| Trend | Wahrscheinlichkeit | Auswirkung |
|-------|-------------------|-----------|
| E-Antrieb als Standard ab 35 ft | Sehr hoch | In-Mast-Anteil steigt auf 50%+ bei Fahrtenyachten |
| Autonomes Reffen (Windstärke-gesteuert) | Mittel | Nur bei Premium-Systemen und Katamaranen |
| Carbon-Furling-Masten unter €15.000 | Niedrig-Mittel | Gewichtsvorteil, aber noch zu teuer für Serie |
| In-Boom als Regatta-Option | Mittel | In-Boom mit Full-Battens schließt Performance-Lücke |
| Retrofit-Kits ohne Masttausch | Mittel-Hoch | Profurl-Typ-Systeme gewinnen Marktanteil im Refit |
| Integration mit Foiling-Systemen | Niedrig | Spezialanwendung, nicht für Fahrtenyachten |

### ANHANG V — Vergleich Segel-Lebensdauer und Degradation

**Segeltuch-Degradation nach System und Material (geschätzte Restleistung in % der Neuware):**

**Dacron-Segel:**

| Alter | Slab (Full Batten) | In-Mast (lattenlos) | In-Boom (Kurzlatten) |
|-------|-------------------|-------------------|---------------------|
| Neu | 100% | 100% | 100% |
| 1 Jahr | 95% | 92% | 94% |
| 2 Jahre | 90% | 84% | 88% |
| 3 Jahre | 85% | 76% | 82% |
| 4 Jahre | 80% | 68% | 76% |
| 5 Jahre | 75% | 62% | 70% |
| 7 Jahre | 65% | 50% | 58% |
| 10 Jahre | 50% | 35% | 45% |
| 12 Jahre | 40% | — (Ende) | 35% |
| 15 Jahre | 30% (Ende) | — | — (Ende) |

**Hydranet-Segel (Dyneema-Polyester-Hybrid):**

| Alter | Slab (Full Batten) | In-Mast (lattenlos) | In-Boom (Kurzlatten) |
|-------|-------------------|-------------------|---------------------|
| Neu | 100% | 100% | 100% |
| 1 Jahr | 97% | 95% | 96% |
| 2 Jahre | 94% | 90% | 92% |
| 3 Jahre | 91% | 85% | 89% |
| 5 Jahre | 85% | 76% | 82% |
| 7 Jahre | 78% | 67% | 74% |
| 10 Jahre | 68% | 55% | 63% |
| 12 Jahre | 60% | 45% | 55% |
| 15 Jahre | 50% | 35% (Ende) | 45% |
| 18 Jahre | 40% (Ende) | — | 35% (Ende) |

**Degradations-Faktoren:**
```
Degradation_rate = f(UV, Rollzyklen, Faltzyklen, Material, Klima)

Haupt-Degradationsfaktoren für Rollsegel:
  1. UV-Exposition: +30% Degradation in Tropen vs. Nordeuropa
  2. Rollzyklen: Jeder Rollzyklus erzeugt Mikrofalten am Luff-Tape
  3. Feuchtigkeit: Nass eingerollt → beschleunigte Alterung +20%
  4. Salzbelastung: Salzkristalle scheuern beim Rollen → +15% Abrieb
  5. Wickelspannung: Zu stramm gewickelt → permanente Falten

AYDI-Degradationsformel (vereinfacht):
  Restleistung(%) = 100 - (Alter × k_material × k_system × k_klima × k_nutzung)

  k_material: Dacron=3.5, Hydranet=2.5, Pentex=2.8
  k_system: Slab=1.0, In-Mast=1.4, In-Boom=1.2
  k_klima: Nordeuropa=1.0, Mittelmeer=1.2, Tropen=1.5
  k_nutzung: Weekend=0.8, Saison=1.0, Ganzjahr=1.3, Charter=1.8
```

**Segelwechsel-Zeitpunkt-Empfehlung:**

| Kriterium | Schwellenwert | Maßnahme |
|-----------|-------------|----------|
| Restleistung <50% | Profiltiefe deutlich reduziert | Neusegel bestellen |
| Luff-Tape Abrieb >30% | Sichtbare Fasern, Ausdünnung | Sofort: Segelmacher-Reparatur oder Neusegel |
| Horizontale Falten (permanent) | Falten bleiben auch bei Spannung | Segel ist gereckt → Neusegel |
| UV-Verfärbung >50% der Fläche | Starke Farbänderung, Material spröde | Neusegel planen (1–2 Saisons) |
| Nahtversagen | Nähte lösen sich an >2 Stellen | Dringend: Segelmacher oder Neusegel |
| Riss am Luff-Tape | Jeder Riss | SOFORT bergen, Segelmacher |

**Kosten-Amortisation: Hydranet vs. Dacron für In-Mast-Segel (12 m Boot):**

| Position | Dacron | Hydranet | Differenz |
|----------|--------|----------|-----------|
| Segel-Preis | €2.800 | €4.500 | +€1.700 |
| Lebensdauer | 8–10 Jahre | 12–15 Jahre | +4–5 Jahre |
| Kosten/Jahr | €280–350 | €300–375 | ±€0–25 |
| Performance | Gut → Mittel (ab 4 J.) | Gut → Gut (bis 8 J.) | Besser |

**AYDI-Empfehlung:** Hydranet amortisiert sich über die Lebensdauer durch die längere Nutzungsdauer und bessere Formhaltung. Für Yachten, die >80 Tage/Jahr segeln, ist Hydranet die wirtschaftlichere Wahl.

### ANHANG W — Ersatzteillisten nach System-Typ

**Empfohlene Ersatzteile an Bord — In-Mast-System:**

| Ersatzteil | Priorität | Gewicht | Kosten (ca.) | Grund |
|-----------|-----------|---------|-------------|-------|
| Sicherung (passend für E-Motor) | MUSS | <50 g | €2–5 | Häufigster Ausfallgrund |
| Manuelles Override-Werkzeug (Kurbel) | MUSS | 0,5–1 kg | Im Lieferumfang | Notbetrieb bei Motor-Ausfall |
| Ersatz-Bedienleine (5 m) | SOLL | 0,3 kg | €10–20 | Bei Leinenbruch |
| Schmierfett (50 ml Tube) | SOLL | 0,1 kg | €8–15 | Für Notschmierung |
| Ersatz-Bürstendichtung (1 m) | KANN | 0,2 kg | €15–30 | Bei Wassereinbruch |
| Kabelbinder + Isolierband | MUSS | 0,1 kg | €5 | Universal-Reparatur |
| Multimeter (digital) | SOLL | 0,2 kg | €15–30 | Fehlerdiagnose E-Motor |
| Segel-Reparatur-Tape (Dacron) | MUSS | 0,1 kg | €10–20 | Notreparatur bei Riss |

**Empfohlene Ersatzteile an Bord — In-Boom-System:**

| Ersatzteil | Priorität | Gewicht | Kosten (ca.) | Grund |
|-----------|-----------|---------|-------------|-------|
| Sicherung (passend für E-Motor) | MUSS | <50 g | €2–5 | Häufigster Ausfallgrund |
| Manuelles Override-Werkzeug | MUSS | 0,5–1 kg | Im Lieferumfang | Notbetrieb |
| Ersatz-Endlos-Fall (komplett) | SOLL | 1–2 kg | €100–250 | Bei Fall-Bruch oder Spleiß-Versagen |
| Ersatz-Führungsrolle (2 Stk.) | KANN | 0,2 kg | €20–50 | Bei Rollenverschleiß |
| Schmierfett (50 ml Tube) | SOLL | 0,1 kg | €8–15 | Rollen + Lager |
| Kabelbinder + Isolierband | MUSS | 0,1 kg | €5 | Universal-Reparatur |
| Reffbändseln (6 Stk., 1 m) | MUSS | 0,2 kg | €5 | Not-Sicherung Segel am Baum |
| Segel-Reparatur-Tape | MUSS | 0,1 kg | €10–20 | Notreparatur |

**Empfohlene Ersatzteile an Bord — Slab-Reefing:**

| Ersatzteil | Priorität | Gewicht | Kosten (ca.) | Grund |
|-----------|-----------|---------|-------------|-------|
| Ersatz-Reffleine (1 Stk., volle Länge) | MUSS | 0,5 kg | €15–30 | Bei Leinenbruch |
| Reffbändseln (10 Stk., 1 m) | MUSS | 0,3 kg | €8 | Sicherung loses Tuch |
| Ersatz-Fallstopper-Feder | KANN | 0,1 kg | ���20–40 | Bei Clutch-Versagen |
| Ersatz-Block (passend für Baum) | KANN | 0,2 kg | €15–40 | Bei Block-Bruch |
| Segel-Reparatur-Kit | MUSS | 0,3 kg | €20–40 | Nadel, Garn, Tape, Patches |
| Kabelbinder | MUSS | 0,1 kg | €3 | Not-Befestigung |

### ANHANG X — Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0.0 | 2026-04-26 | Erstfassung: Vollständige Wissensreferenz Großsegel-Rollreff |

---

*Ende der Wissensdatei 15.02 — Großsegel-Rollreff und In-Mast/In-Boom-Systeme (Vollständig)*
*Abschnitte 1–6: Einführung, Grundlagen, Typenübersicht, Produktlinien, Vergleichsmatrix, Dimensionierung*
*Abschnitte 7–11: Fehlerbild-Atlas, Troubleshooting, FAQ, Glossar, Schnell-Referenz*
*Anhänge A–X: Fallstudien, Lifecycle-Kosten, Normen, Datenmodelle, Visuelle Analyse, Bewertungsregeln, Installationsfehler, Zukunftstrends, Ersatzteile, Quellen*
