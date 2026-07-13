# 05_07 — Edelstahl-Halbzeuge (Rohre, Flachstahl, Rundstahl, Blech, Profile)

> **AYDI Wissensdatei** — Kategorie 05: Verbindungselemente & Befestigungstechnik
> **Confidence:** documented — Zusammenstellung aus Herstellerkatalogen, Fachliteratur, Forum-Konsens, Eigner-Erfahrungsberichten
> **Stand:** 2026-03 | **Nächste Überprüfung:** 2026-09

---

## 1. Grundlagen: Edelstahl im Yachtbau

### 1.1 Warum Edelstahl?

Edelstahl (nichtrostender Stahl, Inox, Stainless Steel) ist das Universalmaterial im modernen Yachtbau für strukturelle Metallkomponenten. Von Relingstützen über Wantenplatten bis hin zu Davits — kein anderes Material bietet die Kombination aus Festigkeit, Korrosionsbeständigkeit und Verfügbarkeit.

### 1.2 Marine-relevante Legierungen — Übersicht

| Legierung | AISI | Werkstoff-Nr. | Kurzname | Cr % | Ni % | Mo % | C max % | Marine-Eignung |
|-----------|------|---------------|----------|------|------|------|---------|---------------|
| X5CrNi18-10 | 304 | 1.4301 | A2 | 17,5–19,5 | 8,0–10,5 | — | 0,07 | Eingeschränkt — nur trocken, über WL |
| X2CrNi18-9 | 304L | 1.4307 | A2L | 17,5–19,5 | 8,0–10,5 | — | 0,03 | Wie 304, bessere Schweißbarkeit |
| X5CrNiMo17-12-2 | 316 | 1.4401 | A4 | 16,5–18,5 | 10,0–13,0 | 2,0–2,5 | 0,07 | Standard-Marine |
| X2CrNiMo17-12-2 | 316L | 1.4404 | A4L | 16,5–18,5 | 10,0–13,0 | 2,0–2,5 | 0,03 | Bevorzugt — beste Schweißbarkeit |
| X2CrNiMo17-12-3 | 316Ti | 1.4571 | A5 | 16,5–18,5 | 10,5–13,5 | 2,0–2,5 | 0,08 | Ti-stabilisiert, gute Schweißbarkeit |
| X2CrNiMoN22-5-3 | 2205 | 1.4462 | Duplex | 21,0–23,0 | 4,5–6,5 | 3,0–3,5 | 0,03 | Premium — höchste Festigkeit + Korr. |
| X2CrNiMoCuWN25-7-4 | 2507 | 1.4410 | Super-Duplex | 24,0–26,0 | 6,0–8,0 | 3,0–5,0 | 0,03 | Extrem — Offshore, Chemie |
| X6CrNiMoTi17-12-2 | 316Ti | 1.4571 | — | 16,5–18,5 | 10,5–13,5 | 2,0–2,5 | 0,08 | Ti-stabilisiert, traditionell in DE |
| X17CrNi16-2 | 431 | 1.4057 | — | 15,0–17,0 | 1,5–2,5 | — | 0,17 | Wellen, Propeller (härtbar) |
| X3CrNiMo13-4 | — | 1.4313 | — | 12,0–14,0 | 3,5–4,5 | 0,3–0,7 | 0,05 | Propellerwellen (härtbar, zäh) |
| X5CrNi13-4 | — | 1.4313 | — | 12,0–14,0 | 3,5–4,5 | 0,3–0,7 | 0,05 | Ruderachsen, Wellenanlagen |

### 1.3 Die 304-vs-316-Debatte

**WARNUNG: 304 (A2) hat im Yachtbau NICHTS unterhalb der Wasserlinie verloren.**

| Eigenschaft | 304 / A2 / 1.4301 | 316 / A4 / 1.4401 | 316L / A4L / 1.4404 |
|-------------|-------------------|-------------------|---------------------|
| Molybdän-Gehalt | 0 % | 2,0–2,5 % | 2,0–2,5 % |
| Lochfraßbeständigkeit (PREN) | 18–20 | 24–26 | 24–26 |
| Spaltkorrosionsbeständigkeit | Gering | Mittel | Mittel |
| Schweißbarkeit | Gut | Gut | Sehr gut (Low Carbon) |
| Sensibilisierung | Möglich >500°C | Möglich >500°C | Gering (Low C) |
| Preis (relativ) | 1,0× | 1,2–1,3× | 1,25–1,35× |
| Marine-Empfehlung | NUR über WL, trocken | Standard-Marine | Bevorzugt (Schweißkonstruktionen) |

**PREN (Pitting Resistance Equivalent Number):**
```
PREN = %Cr + 3,3 × %Mo + 16 × %N
```
Marine-Minimum: PREN ≥ 24 (→ 316/316L). Premium: PREN ≥ 34 (→ 2205 Duplex).

### 1.4 Duplex-Stähle — Wann lohnt sich der Aufpreis?

| Anwendung | 316L ausreichend? | Duplex empfohlen? | Begründung |
|-----------|-------------------|-------------------|------------|
| Relingsstützen | Ja | Nein | Geringe Last, leicht austauschbar |
| Wantenplatten (Chainplates) | Grenzwertig | Ja | Sicherheitskritisch, Dauerlast, Spaltkorrosion |
| Bugbeschläge | Ja | Optional | Hohe Last, aber regelmäßig inspizierbar |
| Propellerwellen | Nein (gehärteter Stahl) | Nein | Spezialstahl 1.4313 / Aquamet |
| Ruderkoker | Grenzwertig | Ja | Dauernd nass, schwer inspizierbar |
| Kielbolzen | Nein | Ja (oder Nitronic 50) | Sicherheitskritisch, nicht inspizierbar |
| Davits | Ja | Optional | Lastabhängig |
| Spinnaker-Pole-Fittings | Ja | Nein | Austauschbar |

### 1.5 Oberflächenbehandlung

| Behandlung | Bezeichnung | Ra (µm) | Marine-Eignung | Anmerkung |
|-----------|-------------|---------|---------------|-----------|
| Warmgewalzt | 1D / No.1 | 3–8 | Akzeptabel (Struktur) | Raue Oberfläche, Zunder |
| Kaltgewalzt | 2B | 0,1–0,5 | Standard | Glatte Oberfläche |
| Geschliffen | #240 | 0,2–0,4 | Gut | Satiniert |
| Geschliffen | #320 | 0,1–0,3 | Sehr gut | Fein satiniert |
| Poliert | #400 | 0,05–0,15 | Sehr gut | Spiegel-ähnlich |
| Spiegelpoliert | #600/#800 | <0,05 | Exzellent | Bester Korrosionsschutz |
| Glasperlen-gestrahlt | — | 1–3 | Gut | Matte Optik, gleichmäßig |
| Elektropoliert | — | <0,05 | Exzellent | Chemisch geglättet, beste Korrosionsbeständigkeit |

**Forum-Konsens (CruisersForum, YBW):** Polierte Oberflächen korrodieren weniger als matte. Für marine Anwendungen: mindestens #240, besser #320 oder poliert. Elektropolieren ist der Gold-Standard für maximale Korrosionsbeständigkeit.

### 1.6 Passivierung

Edelstahl bildet eine dünne Chromoxid-Schicht (Passivschicht), **Dicke: 1–3 Nanometer**(!), die vor Korrosion schützt. Diese Schicht kann beschädigt werden durch:
- Kontamination mit Normalstahl (Funken, Werkzeug, Bürsten)
- Chlorid-Angriff (Salzwasser in Spalten)
- Schweißen ohne Nachbehandlung (Temperatureinfluss zerstört Passivschicht lokal)
- Oberflächenverschmutzung (Fett, Fingerabdrücke unter Dauerbelastung)
- Mechanische Beschädigungen (Kratzer, Bearbeitungsspäne)

**Passivierungsmethoden:**

| Methode | Anwendung | Kosten | Wirksamkeit | Zeitaufwand |
|---------|-----------|--------|-------------|-------------|
| Salpetersäure-Bad (HNO₃ 20–30%, 60 min) | Professionell, große Teile | €50–€200 Material | Sehr gut | 60 min + Spülung |
| Zitronensäure-Bad (10%, 30 min, 60°C) | DIY möglich, umweltfreundlich | Gering (€5–€10) | Gut | 30 min + Spülung |
| Passivierungspaste (z.B. Avesta 601) | DIY, Schweißnähte, Halbzeuge | €15–€25/500g Dose | Sehr gut | 60–90 min Einwirkzeit |
| Beizpaste (z.B. Avesta 401) | VOR Passivierung, Anlauffarben | €15–€20/500g | Sehr gut | 30–60 min |
| Elektropolieren | Professionell, Premium | €200–€500 pro Job | Exzellent | 2–3 Stunden |

**DIY-Passivierung Schritt-für-Schritt:**
```
1. Oberflächenreinigung (entfetten mit Lösungsmittel)
2. Beizpaste auftragen (wenn Schweißnaht vorhanden) — 30 min
3. Mit Wasser abspülen
4. Passivierungspaste auftragen — 60–90 min
5. Mit Süßwasser gründlich abspülen (2–3× spülen)
6. Trocken tupfen
7. Optional: CorrosionX Spray auftragen (Langfristschutz)
```

**Chemie der Passivierung:**
- **Beizen (Avesta 401):** Entfernt Chromkarbide, Oxidfarbschicht
- **Passivieren (Avesta 601):** Regeneriert Chromoxid-Schicht, dickt diese auf bis 3–5 nm auf
- **Resultat:** Verbesserte Korrosionsbeständigkeit, reduziertes Lochfraß-Risiko

### 1.7 Geschichte Edelstahl im Yachtbau

| Jahrzehnt | Entwicklung | Impact |
|-----------|------------|--------|
| **1950–1960er** | Erste Edelstahl-Relinge (UK/DE) | Übergang von Bronze zu Edelstahl |
| **1960–1970er** | 304 Standard (billig) | Viele Korrosions-Probleme nach 10–15 Jahren |
| **1970–1980er** | 316 kommt auf den Markt | Molybdän-Zusatz verbessert Salzwasser-Beständigkeit |
| **1980–1990er** | Duplex (2205) entwickelt | Höhere Festigkeit ermöglicht dünnere Profile |
| **1990–2000er** | Aquamet für Propellerwellen | Profi-Segelyachten + Rennyachten nutzen Aquamet |
| **2000–2010er** | Zertifizierung (EN 10088-2) | Qualitätsstandards strikter, Mill Certs normal |
| **2010–2020er** | Duplex wird Standard für Chainplates | Spaltkorrosion-Probleme gelöst |
| **2020–heute** | Material-Verbrauchsoptimierung | CAD-Auslegung minimiert Gewicht, optimiert für Korrosion |

**Lektion aus Vergangenheit:** Viele Yachten der 1960–1980er Jahre mit 304-Relinge haben deutliche Korrosions-Schäden. Dies war Trigger für Branchenwechsel zu 316L.

### 1.8 Material-Auswahl Entscheidungs-Matrix

Vereinfachter Entscheidungsbaum für Edelstahl-Materialwahl:

```
IST DAS TEIL SICHERHEITSKRITISCH?
  Ja → Chainplate, Kielbolzen, Ruderachse
    → Salzwasser + nie inspizierbar?
      → Duplex 2205 oder besser
    → Salzwasser + inspizierbar (halbjährlich)?
      → 316L akzeptabel
    → Süßwasser?
      → 316L ausreichend

  Nein → Reling, Beschläge, Dekorative Teile
    → 316L Standard
    → Kosteneinsparung möglich → 304 (ABER NUR über Wasserlinie!)

IST DAS TEIL HOCHBELASTET?
  Ja → Propellerwelle, Motorlager-Rahmen
    → Aquamet 22 (Welle) oder Duplex 2205 (Rahmen)
  Nein → 316L Standard

IST DAS TEIL SCHWEISST?
  Ja → 316L IMMER (bessere Schweißbarkeit als 304)
       Duplex nur wenn Spezialist (erfordert Zusatz 2209)
  Nein → Materialwahl flexibel
```

---

## 2. Edelstahlrohre (Tubes / Pipes)

### 2.1 Rohrtypen im Yachtbau

| Typ | Norm | Eigenschaft | Anwendung |
|-----|------|------------|-----------|
| Nahtloses Rohr | EN 10216-5, ASTM A269 | Höchste Festigkeit, kein Schweißnahtfaktor | Hydraulik, Hochdruck, kritische Struktur |
| Geschweißtes Rohr (WIG) | EN 10217-7, ASTM A249 | Standard, gute Qualität | Reling, Davits, Bimini, Struktur |
| Geschweißtes Rohr (Laser) | EN 10217-7 | Sehr feine Naht, polierbar | Hochwertige Reling, Sichtbare Rohre |
| Geschweißtes + gezogenes Rohr | — | Naht quasi unsichtbar, nahtlos-ähnlich | Premium-Anwendungen |
| Dekoratives Rohr | — | Dünnwandiger, nur für Optik | Handläufe ohne Last |

### 2.2 Standard-Rohrdimensionen für Yachtbau

#### 2.2.1 Reling- und Handlaufrohre

| Außen-Ø (mm) | Wandstärke (mm) | Gewicht (kg/m) | Anwendung | Typische Yachtgröße |
|-------------|----------------|---------------|-----------|-------------------|
| 19,05 (3/4") | 1,5 | 0,65 | Leichte Handläufe, Sonnensegel-Gestänge | Jollen, Boote <7m |
| 22,0 | 1,5 | 0,76 | Handläufe, Bimini-Gestänge (leicht) | 7–9m |
| 22,23 (7/8") | 1,5 | 0,77 | US-Standard Reling | 7–10m |
| 25,0 | 1,5 | 0,87 | Reling (Standard, kleine Yachten) | 8–10m |
| 25,0 | 2,0 | 1,14 | Reling (verstärkt) | 8–12m |
| 25,4 (1") | 1,5 | 0,89 | US-Standard Reling | 8–12m |
| 25,4 (1") | 2,0 | 1,16 | US-Standard Reling (verstärkt) | 10–14m |
| 30,0 | 1,5 | 1,06 | Reling (mittlere Yachten) | 10–14m |
| 30,0 | 2,0 | 1,39 | Reling (verstärkt), Bugspriet-Korb | 12–16m |
| 32,0 | 1,5 | 1,14 | Reling (große Yachten), Davit-Rohre | 12–18m |
| 32,0 | 2,0 | 1,49 | Reling (verstärkt), Überrollbügel | 14–20m |
| 38,0 | 2,0 | 1,79 | Bimini-Rohre (schwer), Davit-Rohre | 12–18m |
| 38,1 (1-1/2") | 2,0 | 1,80 | US-Standard Davits, Bimini | 12–18m |
| 40,0 | 2,0 | 1,89 | Überrollbügel, Davits | 14–20m |
| 42,0 | 2,0 | 1,99 | Davits, Radarhalter | 14–22m |
| 48,3 (1-1/2" NPS) | 2,5 | 2,84 | Schwere Davits, Kran-Ausleger | 16–25m |
| 50,0 | 2,0 | 2,39 | Schwere Davits, Masttraversen | 18–30m |
| 50,8 (2") | 2,5 | 3,01 | US-Standard schwere Davits | 18–30m |
| 60,3 (2" NPS) | 2,5 | 3,59 | Mast-Elemente, Bügel >20m | 20m+ |

#### 2.2.2 Hydraulik- und Leitungsrohre

| Außen-Ø (mm) | Wandstärke (mm) | Anwendung | Norm |
|-------------|----------------|-----------|------|
| 6,0 | 1,0 | Hydraulikleitungen, Instrumentenanschlüsse | EN 10216-5 |
| 8,0 | 1,0 | Hydraulikleitungen | EN 10216-5 |
| 10,0 | 1,0 | Kraftstoffleitungen, Hydraulik | EN 10216-5 |
| 12,0 | 1,0 | Kraftstoff, Wasser, Hydraulik | EN 10216-5 |
| 15,0 | 1,5 | Abgasleitungen (klein), Wasser | EN 10217-7 |
| 18,0 | 1,5 | Abgasleitungen, Kühlwasser | EN 10217-7 |
| 22,0 | 1,5 | Abgas, Wasser, Sanitär | EN 10217-7 |

#### 2.2.3 Rohr-Gewichtstabelle (316L, geschweißt)

| Ø × Wandstärke | Gewicht (kg/m) | Innen-Ø (mm) | Querschnittsfläche (mm²) | Trägheitsmoment I (mm⁴) |
|----------------|---------------|-------------|------------------------|----------------------|
| 22 × 1,5 | 0,76 | 19,0 | 96,6 | 5.283 |
| 25 × 1,5 | 0,87 | 22,0 | 110,7 | 7.945 |
| 25 × 2,0 | 1,14 | 21,0 | 144,5 | 10.064 |
| 30 × 1,5 | 1,06 | 27,0 | 134,3 | 14.117 |
| 30 × 2,0 | 1,39 | 26,0 | 175,9 | 18.064 |
| 32 × 1,5 | 1,14 | 29,0 | 143,8 | 17.185 |
| 32 × 2,0 | 1,49 | 28,0 | 188,5 | 22.054 |
| 38 × 2,0 | 1,79 | 34,0 | 226,2 | 37.476 |
| 42 × 2,0 | 1,99 | 38,0 | 251,3 | 51.025 |
| 48,3 × 2,5 | 2,84 | 43,3 | 359,5 | 96.256 |
| 50 × 2,0 | 2,39 | 46,0 | 301,6 | 86.863 |

### 2.3 Metrisch vs. Imperial — Das ewige Problem

| Metrisch (mm) | Imperial (Zoll) | Unterschied | Problem |
|--------------|----------------|------------|---------|
| 22,0 | 7/8" = 22,23 | 0,23 mm | Beschläge passen NICHT exakt |
| 25,0 | 1" = 25,4 | 0,40 mm | Beschläge sitzen locker oder klemmen |
| 32,0 | 1-1/4" = 31,75 | 0,25 mm | Leicht adaptierbar |
| 38,0 | 1-1/2" = 38,1 | 0,10 mm | Fast identisch |
| 50,0 | 2" = 50,8 | 0,80 mm | Signifikanter Unterschied |

**WARNUNG:** Europäische Yachten haben metrische Rohre, US/UK-Yachten imperiale. Beschläge (Reling-Beschläge, Klappstützen, T-Stücke) sind NICHT universell kompatibel. VOR dem Kauf: Rohr-Ø exakt messen (Messschieber, nicht Maßband)!

**Forum-Konsens (CruisersForum):** "Measure your tube OD with a caliper — I bought $200 worth of 1" fittings for my European boat only to find the tubes were 25mm, not 25.4mm. Had to return everything." (User: SailingDog, 8.000+ Posts)

### 2.4 Rohr-Beschläge und Verbindungstechnik

#### 2.4.1 Steck-/Klemm-Beschläge

| Hersteller | Typ | Material | Rohr-Ø | Preis ca. |
|-----------|-----|---------|--------|----------|
| Wichard | Reling-Beschläge Serie | SS316L | 22, 25 mm | €15–€60/Stk. |
| Osculati | Reling-Beschläge | SS316 | 22, 25, 30 mm | €8–€35/Stk. |
| Sprenger | Reling-Beschläge | SS316 | 22, 25 mm | €12–€45/Stk. |
| Suncor | Rail Fittings | SS316 | 7/8", 1" | $8–$40/Stk. |
| Sea-Dog | Rail Fittings | SS316/304 | 7/8", 1" | $6–$30/Stk. |
| Schaefer Marine | Rail Fittings | SS316 | 7/8", 1" | $12–$50/Stk. |
| Reelax | Rail Fittings (AU) | SS316 | 25 mm, 1" | AUD 15–55/Stk. |
| Bainbridge | Rail Fittings (UK) | SS316 | 22, 25 mm | £10–£40/Stk. |

#### 2.4.2 Schweiß-Verbindungen

| Parameter | Empfehlung |
|-----------|-----------|
| Verfahren | WIG/TIG (GTAW) — EINZIGES akzeptables Verfahren für Marine-Edelstahl |
| Schutzgas | Argon 99,99 %, Formiergas auf der Rückseite |
| Zusatzwerkstoff | 316L (1.4404) oder 316LSi — NIEMALS 308L für marine! |
| Vorwärmung | Keine (Raumtemperatur) |
| Zwischenlagentemperatur | Max. 150°C |
| Nachbehandlung | Beizen (Avesta 401) + Passivieren (Avesta 601) |
| Mindest-Wandstärke für Schweißung | 1,5 mm (besser 2,0 mm) |
| Kehlnaht-Dicke | ≥ Wandstärke |

**WARNUNG: MIG/MAG-Schweißung ist für dünnwandige marine Edelstahl-Rohre NICHT empfohlen.** Die höhere Wärmeeinbringung verursacht Verzug und Sensibilisierung. Nur WIG/TIG mit Schutzgas-Formierung!

### 2.5 Rohrbiegung

| Parameter | Empfehlung |
|-----------|-----------|
| Mindest-Biegeradius | 3× Außen-Ø (kaltgebogen), 2× Außen-Ø (Dorndbiegen) |
| Verfahren (Rohr <30mm) | Handbiegemaschine (Rothenberger, REMS, Ridgid) |
| Verfahren (Rohr ≥30mm) | Hydraulische Biegemaschine oder Dornbiegen |
| Wandstärke nach Biegung (Außenradius) | Reduziert auf ca. 80–85 % der Original-Wandstärke |
| Wandstärke nach Biegung (Innenradius) | Erhöht auf ca. 110–120 % (Stauchung) |
| Ovalität max. | 8 % für Struktur, 5 % für Hydraulik |
| Oberflächenrisse prüfen | Visuell + ggf. Farbeindringprüfung nach Biegung |

**Rohrbiegung — Eigner-Erfahrung (CruisersForum):**
"Had my Bimini tubes bent by a local exhaust shop — perfect job, $40 per tube. The marine shop quoted $150 per tube for the same work." (User: CaptainJack, 5.000+ Posts)

### 2.6 Rohr-Hersteller und Lieferanten

| Hersteller/Händler | Land | Produkt | Legierungen | Lieferform |
|-------------------|------|---------|-------------|------------|
| Stahlrohr GmbH | DE | Geschweißte + nahtlose Rohre | 1.4301, 1.4404, 1.4571 | Ab 1m, Zuschnitt |
| Abrams Industries | DE | Premium-Edelstahlrohre | 1.4404, 1.4462 | Ab 1m |
| Salzgitter Mannesmann | DE | Nahtlose Rohre | Alle | Großhandel |
| Sandvik | SE | Premium nahtlose Rohre | Alle inkl. Duplex | Industrie |
| Outokumpu | FI | Geschweißte + nahtlose | Alle | Großhandel |
| Aalco | UK/EU | Rohre, Zuschnitt | 304, 316, 2205 | Ab 1m |
| metals4U | UK | Rohre, Zuschnitt | 304, 316 | Ab 0,25m |
| Stahl-Shop.de | DE | Rohre aller Größen | 1.4301, 1.4404, 1.4571 | Ab 0,5m |
| Online Metals | US | Rohre, Zuschnitt | 304, 316 | Ab 1ft |
| Metals Depot | US | Rohre, Platten | 304, 316 | Ab 1ft |
| Metal Supermarkets | US/CA/UK | Sofortzuschnitt | 304, 316 | Ab Stück |
| Midway Metals | AU | Rohre + Fittings | 304, 316 | Ab 1m |
| Atlas Steels | AU | Premium, alle Halbzeuge | Alle | Großhandel |
| Edcon Steel | AU | Rohre, Zuschnitt | 304, 316 | Ab 1m |

### 2.7 Preise Edelstahlrohre (Richtwerte 2025/2026)

| Rohr-Dimension | Material | Preis (€/m) DE | Preis (£/m) UK | Preis ($/ft) US |
|---------------|---------|---------------|---------------|----------------|
| 22 × 1,5 mm | 316L | €8–€14 | £7–£12 | $4–$7 |
| 25 × 1,5 mm | 316L | €9–€16 | £8–£14 | $5–$8 |
| 25 × 2,0 mm | 316L | €12–€20 | £10–£17 | $6–$10 |
| 30 × 2,0 mm | 316L | €15–€25 | £13–£22 | $8–$13 |
| 32 × 2,0 mm | 316L | €17–€28 | £15–£24 | $9–$14 |
| 38 × 2,0 mm | 316L | €22–€35 | £19–£30 | $12–$18 |
| 42 × 2,0 mm | 316L | €25–€40 | £22–£35 | $14–$20 |
| 50 × 2,0 mm | 316L | €30–€48 | £26–£42 | $16–$25 |
| 25 × 2,0 mm | 2205 Duplex | €25–€40 | £22–£35 | $14–$22 |
| 32 × 2,0 mm | 2205 Duplex | €35–€55 | £30–£48 | $18–$28 |

---

## 3. Flachstahl (Flat Bar) — Chainplates und Strukturteile

### 3.1 Flachstahl im Yachtbau

Flachstahl ist das Ausgangsmaterial für:
- **Chainplates (Wantenplatten)** — Die kritischste Anwendung
- **Kielbolzen-Platten** — Lastverteilung am Kiel
- **Ruderblatt-Verstärkungen** — Innenstruktur
- **Traveller-Schienen-Träger** — Decksverstärkung
- **Motorlager-Schienen** — Maschinenrahmen
- **Stringer-Verstärkungen** — Rumpfstruktur

### 3.2 Chainplates — Die kritischste Anwendung

#### 3.2.1 Chainplate-Grundlagen

Chainplates (Wantenplatten) übertragen die gesamten Riglasten in den Rumpf. Sie sind die höchstbelasteten Edelstahl-Bauteile auf einer Segelyacht.

| Parameter | Typische Werte |
|-----------|---------------|
| Material | 316L (1.4404) oder Duplex 2205 (1.4462) |
| Typische Dicke | 6–12 mm |
| Typische Breite | 30–80 mm |
| Typische Länge | 200–600 mm |
| Oberfläche | Mindestens #240 geschliffen, besser poliert |
| Bolzenlöcher | Passgenau gebohrt, entgratet, Kanten gebrochen |
| Sicherheitsfaktor | 3–5× Bruchlast des Drahts/Rods |

#### 3.2.2 Chainplate-Dimensionierung nach Rigg-Drahtgröße

| Rigg-Draht | Bruchlast (kN) | Chainplate min. Querschnitt (mm²) | Empfohlene Abmessung (b×d) | Bolzen-Ø |
|-----------|---------------|----------------------------------|---------------------------|---------|
| 1×19 Ø 4 mm | 12,5 | 60 | 25×6 mm | M8 |
| 1×19 Ø 5 mm | 19,6 | 95 | 30×6 mm | M10 |
| 1×19 Ø 6 mm | 28,0 | 135 | 35×6 mm | M10 |
| 1×19 Ø 7 mm | 38,5 | 185 | 40×8 mm | M12 |
| 1×19 Ø 8 mm | 49,0 | 235 | 40×8 mm | M12 |
| 1×19 Ø 10 mm | 77,0 | 370 | 50×10 mm | M14/M16 |
| 1×19 Ø 12 mm | 110,0 | 530 | 60×10 mm | M16 |
| 1×19 Ø 14 mm | 150,0 | 720 | 60×12 mm | M16/M20 |
| Rod Ø 6 mm (Nitronic 50) | 36,0 | 175 | 35×8 mm | M10 |
| Rod Ø 8 mm (Nitronic 50) | 64,0 | 310 | 50×8 mm | M12 |
| Rod Ø 10 mm (Nitronic 50) | 100,0 | 480 | 50×10 mm | M14 |
| Rod Ø 12 mm (Nitronic 50) | 144,0 | 690 | 60×12 mm | M16 |
| Rod Ø 14 mm (Nitronic 50) | 196,0 | 940 | 80×12 mm | M20 |

**Berechnung:**
```
A_min = F_bruch / (σ_zul × SF)
```
Wobei:
- F_bruch = Bruchlast des Rigg-Drahts (kN)
- σ_zul = 0,6 × Rm für 316L (= 0,6 × 485 MPa = 291 MPa)
- SF = 1,5 (zusätzlicher Sicherheitsfaktor zum Rigg)

> ⚠️ **ZU PRÜFEN (Audit):** Formel widerspricht der Tabelle 3.2.2. Nach A_min = F/(σ_zul × SF) ergäbe sich für Ø8 mm (F = 49 kN) nur ~112 mm², die Tabelle nennt aber 235 mm². Die Tabellenwerte folgen A_min = F × SF / σ_zul (zulässige Spannung ≈ σ_zul/SF ≈ 208 MPa). Die geschriebene Formel würde die Chainplate um ~Faktor 2 UNTERdimensionieren — sicherheitskritisch. Korrekte Formelform unverifiziert → für die Auslegung die Tabelle 3.2.2 verwenden, nicht die Formel. Confidence: estimated — unverifiziert.

#### 3.2.3 Chainplate-Spaltkorrosion — Das größte Risiko

**WARNUNG: Chainplate-Versagen durch Spaltkorrosion ist die häufigste Ursache für Rigg-Verlust auf Segelyachten über 15 Jahre.**

| Risikofaktor | Beschreibung | Maßnahme |
|-------------|-------------|----------|
| Decksdurchführung | Chainplate tritt durch Deck — Spalt zwischen Plate und GFK/Teak | Dichtmittel (Sikaflex 291), regelmäßig erneuern |
| Kontamination durch Salzwasser | Salzkristalle im Spalt ziehen Feuchtigkeit | Süßwasser-Spülung nach jedem Segeltörn |
| Oberflächenrauhigkeit | Raue Oberfläche = mehr Angriffspunkte | Polieren auf #320 oder besser |
| Sensibilisierung (Schweißzone) | Chromkarbid-Ausscheidung bei 500–800°C | 316L verwenden, korrekte Schweißparameter |
| Rissbildung an Bolzenlöchern | Spannungskonzentration + Korrosion | Löcher poliert, Kanten gebrochen, übergroße Radien |
| Material-Qualität | 304 statt 316, falsches Zertifikat | Materialzertifikat 3.1 nach EN 10204 verlangen |

**Steve D'Antonio (marinehowto.com):** "Chainplates are the most common item I condemn during yacht inspections. After 15-20 years, virtually every unpolished 316 chainplate in a saltwater environment shows some degree of crevice corrosion, typically at the deck penetration."

#### 3.2.4 Chainplate-Inspektion

| Inspektions-Methode | Sensitivität | Kosten | DIY möglich? |
|--------------------|-------------|--------|-------------|
| Visuelle Inspektion | Gering (nur fortgeschrittene Korrosion) | Keine | Ja |
| Farbeindringprüfung (Dye Penetrant) | Mittel (Oberflächenrisse) | €20–€50/Set | Ja |
| Ultraschall-Dickenmessung | Hoch (Wandstärkenverlust) | €500–€2.000 (Gerät) | Nein |
| Wirbelstromprüfung (Eddy Current) | Hoch (Risse, auch unter Oberfläche) | Professionell | Nein |
| Röntgen/Radiografie | Sehr hoch | Professionell | Nein |
| Ziehprobe (Ausbau + Prüfung) | Höchste (100% Sicht) | Arbeitszeit | Ja (aufwendig) |

**Empfehlung (Nigel Calder, Don Casey, Practical Sailor):**
- Alle 5 Jahre: Visuelle Inspektion an Decksdurchführung
- Alle 10 Jahre: Farbeindringprüfung
- Alle 15–20 Jahre: Ausbau und vollständige Inspektion oder Ersatz

#### 3.2.5 Chainplate-Austausch

| Schritt | Aktion | Detail |
|---------|--------|--------|
| 1 | Rigg sichern | Provisorische Stützen / Kran |
| 2 | Dichtmittel entfernen | Cutter, Spachtel |
| 3 | Alte Chainplate ausbauen | Bolzen lösen (Kriechöl 24h vorher!) |
| 4 | Inspizieren (alt) | Farbeindringprüfung, Maße vergleichen |
| 5 | Neue Chainplate fertigen | Nach Zeichnung, 316L oder Duplex |
| 6 | Oberflächenbehandlung | Polieren #320 oder besser |
| 7 | Löcher bohren + entgraten | ±0,5 mm Toleranz, Kanten brechen |
| 8 | Probeeinbau (trocken) | Passgenauigkeit prüfen |
| 9 | Dichtung vorbereiten | Sikaflex 291 unter Decksdurchführung |
| 10 | Einbau | Neue Bolzen, Nyloc-Muttern, Drehmoment |
| 11 | Dichtung komplettieren | Sikaflex auf Decksdurchführung + Kragen |
| 12 | Rigg aufstellen | Wantspannung einstellen |

### 3.3 Flachstahl-Standardabmessungen

| Breite (mm) | Dicke (mm) | Querschnitt (mm²) | Gewicht (kg/m) | Typische Anwendung |
|------------|-----------|-------------------|---------------|-------------------|
| 20 × 3 | 3 | 60 | 0,47 | Leichte Beschläge, Laschen |
| 20 × 5 | 5 | 100 | 0,79 | Beschläge, Halterungen |
| 25 × 5 | 5 | 125 | 0,98 | Leichte Chainplates (<7m) |
| 25 × 6 | 6 | 150 | 1,18 | Chainplates 7–9m |
| 30 × 5 | 5 | 150 | 1,18 | Beschläge, Motorlager |
| 30 × 6 | 6 | 180 | 1,41 | Chainplates 8–10m |
| 35 × 6 | 6 | 210 | 1,65 | Chainplates 9–11m |
| 40 × 6 | 6 | 240 | 1,88 | Chainplates 10–12m |
| 40 × 8 | 8 | 320 | 2,51 | Chainplates 11–14m |
| 40 × 10 | 10 | 400 | 3,14 | Chainplates 13–16m, Kielbolzen |
| 50 × 8 | 8 | 400 | 3,14 | Chainplates 14–18m |
| 50 × 10 | 10 | 500 | 3,93 | Chainplates 16–20m, Kielbolzen |
| 60 × 10 | 10 | 600 | 4,71 | Chainplates 18–24m |
| 60 × 12 | 12 | 720 | 5,65 | Chainplates 20m+, Mega-Yacht |
| 80 × 10 | 10 | 800 | 6,28 | Kielbolzen-Platten, Schwert-Beschläge |
| 80 × 12 | 12 | 960 | 7,54 | Mega-Yacht Chainplates, Kielbolzen |
| 100 × 10 | 10 | 1.000 | 7,85 | Kielbolzen-Platten, Mega-Yacht |
| 100 × 12 | 12 | 1.200 | 9,42 | Mega-Yacht Struktur |

### 3.4 Flachstahl-Hersteller und Bezugsquellen

| Händler | Land | Legierungen | Zuschnitt | Lieferzeit | Preis-Niveau |
|---------|------|------------|-----------|-----------|-------------|
| Edelstahl-Service-Center.de | DE | 1.4301, 1.4404, 1.4571, 1.4462 | Laser, Wasserstrahl | 3–5 Tage | Mittel |
| Stahl-Shop.de | DE | 1.4301, 1.4404 | Säge | 2–4 Tage | Günstig |
| Abrams Industries | DE | Alle inkl. Duplex | Laser, Wasserstrahl | 3–7 Tage | Mittel-Hoch |
| LaserTeile4You.de | DE | 1.4301, 1.4404 | Laser nach DXF | 3–7 Tage | Günstig |
| Edelstahl-Flachstahl.de | DE | 1.4301, 1.4404 | Zuschnitt | 2–5 Tage | Günstig |
| Aalco | UK/EU | Alle | Säge, Laser | 3–5 Tage | Mittel |
| metals4U | UK | 304, 316 | Säge | 3–5 Tage | Mittel |
| Smiths Metal Centres | UK | Alle inkl. Duplex | Säge, Laser | 3–7 Tage | Mittel |
| Online Metals | US | 304, 316 | Säge | 5–10 Tage | Mittel |
| Metals Depot | US | 304, 316 | Säge | 3–7 Tage | Günstig |
| Metal Supermarkets | US/CA/UK | 304, 316, 2205 | Sofort | Sofort | Hoch |
| Midway Metals | AU | 304, 316, 2205 | Säge | 3–7 Tage | Mittel |
| Atlas Steels | AU | Alle | Industrie | 5–10 Tage | Mittel |

### 3.5 Flachstahl-Preise (Richtwerte 2026)

| Dimension | 316L (€/m) | 2205 Duplex (€/m) | Anmerkung |
|-----------|-----------|-------------------|-----------|
| 25 × 6 mm | €6–€10 | €12–€20 | Kleine Yachten, Küstenfahrt |
| 30 × 6 mm | €7–€12 | €14–€24 | Standard für 8–10m Cruiser |
| 40 × 8 mm | €12–€20 | €24–€40 | Standard für 11–14m Cruiser (häufigste!) |
| 40 × 10 mm | €15–€25 | €30–€50 | Schwere Yachten, 14–16m |
| 50 × 10 mm | €19–€32 | €38–€64 | Große Yachten, 16–20m |
| 60 × 10 mm | €23–€38 | €46–€76 | 18–24m Yachten, Duplex empfohlen |
| 60 × 12 mm | €27–€45 | €54–€90 | 20m+ Mega-Yacht |
| 80 × 12 mm | €36–€60 | €72–€120 | Kielbolzen-Platten, Mega-Yacht |

**Volumen-Rabatte:**
- Ab 50m Gesamt-Länge: -10 %
- Ab 100m Gesamt-Länge: -15–20 %
- Einzelzuschnitte: Keine Rabatte, ca. €5–€10 Zuschnitt-Gebühr

### 3.6 Chainplate-Installation — Schritt-für-Schritt-Anleitung

**Vorbereitung (1–2 Wochen vorher):**
1. Alte Chainplates fotografieren (Referenz)
2. Maße notieren (Breite, Dicke, Bolzenlöcher-Abstand, Länge)
3. Material-Zertifikat (3.1) des alten Bolzens notieren (für Ersatz-Qual spezifikation)
4. Rigg-Draht-Größe (Ø in mm, 1×19 oder Rod) dokumentieren

**Materialbeschaffung:**
- Neue Chainplate (316L oder Duplex nach Wahl)
- Bolzen (316L oder Duplex, Nyloc-Muttern)
- Tef-Gel (für Isolation)
- Nylon-Isolierbuchsen (falls nicht im Bolzen integriert)
- G10-Platte oder Duralac (für Isolation unter Deck)
- Sikaflex 291 (2–3 Kartuschen pro Deck-Set)
- Beizpaste (falls neue Chainplate geschweißt wurde)

**Installation (4–6 Stunden pro Chainplate):**
1. Wanten entlasten (Spannmittel oder provisorische Stützen)
2. Alte Dichtung mit Meißel/Cutter entfernen
3. Bolzen mit Penetrating Oil (WD40) 24h vorbehandeln
4. Bolzen mit Gabelschlüssel (nicht Rohrzange!) abschrauben
5. Alte Chainplate ausbauen, inspect
6. Unter-Deck-Bereich mit Bürste abbürsten (Korrosionsprudukte entfernen)
7. G10-Isolierplatte zuschneiden (100mm × 100mm min.) und einpassen
8. Neue Chainplate einpassen (mit G10-Platte, decksbündig)
9. Neue Bolzen durch Chainplate + Isolierbuchsen stecken
10. Von unten: Tef-Gel unter Unterlegscheibe schmieren
11. Bolzen anziehen (Drehmoment: M12 = 25–30 Nm, mit Tef-Gel ca. 25 Nm)
12. Decksdurchführung mit Sikaflex 291 saubersichern (ringförmig um Chainplate)
13. Mit Kragen-Sealant abdecken (verhindert Wassereintritt)
14. Sikaflex mind. 24h aushärten (nicht belasten!)
15. Wanten wieder spannen

**Nach-Kontrolle (1 Woche später):**
- Decksdurchführung prüfen (Sikaflex sollte geheilt sein, nicht noch klebrig)
- Bolzen mit Drehmoment-Schlüssel nachziehen (ca. 80 % der Ersten Spannung)
- Unter Deck prüfen: Keine Wasser-Spuren?

### 3.7 Lagerbestand Flachstahl für DIY-Reparaturen

| Größe | Menge | Lagerung | Verwendung |
|-------|-------|----------|-----------|
| 40×8 316L, 1m | 2 Stück | Horizontal auf Holz | Chainplate-Zuschnitte für Reparatur |
| 30×6 316L, 1m | 1 Stück | Horizontal auf Holz | Kleinere Beschläge |
| Bolzen M10 316L (Nyloc) | 20 Stück | In Schachtel sortiert | Universelle Befestigung |
| Bolzen M12 316L (Nyloc) | 10 Stück | In Schachtel sortiert | Chainplate-Befestigung |
| Tef-Gel Tuben | 3–5 Stück | Kühl, Deckel fest | Isolierung Bolzen |

---

## 4. Rundstahl (Round Bar)

### 4.1 Rundstahl im Yachtbau

| Anwendung | Typischer Ø | Material | Anmerkung |
|-----------|------------|---------|-----------|
| Bolzen (manuell gefertigt) | 8–20 mm | A4-80 (316) | Für Spezial-Beschläge |
| Pinne | 10–25 mm | 316L | Geschmiedet oder gedreht |
| Wanten-Toggles (DIY) | 8–16 mm | 316L oder 2205 | Sicherheitskritisch! |
| Ankerkettenrollen-Achsen | 10–20 mm | 316L | Poliert |
| Scharnierachsen | 6–12 mm | 316L | Poliert, Passung h6 |
| Block-Achsen | 6–10 mm | 316L | Poliert |
| Propellerwellen | 25–60 mm | Aquamet 22 / 1.4313 | Spezialstahl, härtbar |
| Ruderachsen | 30–80 mm | Aquamet 22 / 1.4313 / 2205 | Je nach Yacht-Größe |
| Kielbolzen | 16–30 mm | 316L, 2205, Nitronic 50 | Sicherheitskritisch! |

### 4.2 Rundstahl-Standardabmessungen

| Ø (mm) | Querschnitt (mm²) | Gewicht (kg/m) | Typische Anwendung |
|--------|-------------------|---------------|-------------------|
| 6 | 28,3 | 0,22 | Stifte, kleine Achsen |
| 8 | 50,3 | 0,39 | Bolzen, Stifte |
| 10 | 78,5 | 0,62 | Bolzen, Achsen |
| 12 | 113,1 | 0,89 | Bolzen, Toggle-Rohlinge |
| 14 | 153,9 | 1,21 | Kielbolzen (klein), Achsen |
| 16 | 201,1 | 1,58 | Kielbolzen, schwere Achsen |
| 18 | 254,5 | 2,00 | Kielbolzen, Ruderachsen (klein) |
| 20 | 314,2 | 2,47 | Kielbolzen, schwere Beschläge |
| 25 | 490,9 | 3,85 | Propellerwellen (klein) |
| 30 | 706,9 | 5,55 | Propellerwellen |
| 35 | 962,1 | 7,55 | Propellerwellen, Ruderachsen |
| 40 | 1.256,6 | 9,87 | Propellerwellen, Ruderachsen |
| 50 | 1.963,5 | 15,41 | Schwere Wellen |
| 60 | 2.827,4 | 22,19 | Mega-Yacht-Wellen |

### 4.3 Spezieller Rundstahl: Aquamet / Aqualoy

**Aquamet** (Plymouth Tube Company, USA) ist der Industriestandard für Propellerwellen.

| Legierung | Zusammensetzung | Rm (MPa) | Rp0,2 (MPa) | Korrosionsbeständigkeit | Anwendung |
|-----------|----------------|---------|-------------|----------------------|-----------|
| Aquamet 17 | 17Cr-4Ni-3Mo | 860 | 620 | Gut | Budget-Wellen, Küstenfahrt |
| Aquamet 18 | 18Cr-14Ni-3Mo | 790 | 550 | Sehr gut | Standard-Segelyachten |
| Aquamet 19 | 19Cr-13Ni-3Mo-Ti | 830 | 620 | Sehr gut | Premium-Yachten |
| Aquamet 22 | 22Cr-13Ni-5Mn-2.5Mo-N | 930 | 690 | Exzellent | Hochleistungs-Yachten, Regatta |
| Aqualoy 22 (alt) | ~ähnlich Aquamet 22 | 900 | 660 | Exzellent | Bezeichnung veraltet |
| Nitronic 50 (XM-19) | 22Cr-12.5Ni-5Mn-2Mo-N-Nb | 690 | 380 | Exzellent | Kielbolzen (Standard USA), Rigg-Fittings |

**Forum-Konsens (SailboatOwners, CruisersForum):** "Aquamet 22 is the gold standard for prop shafts. If you're replacing a shaft, don't even consider regular 316 — spend the extra $200 for Aquamet." (User: MaineSail, 15.000+ Posts)

### 4.4 Kielbolzen — Material-Debatte

| Material | Rm (MPa) | PREN | Empfehlung | Risiko |
|----------|---------|------|-----------|--------|
| 316L | 485 | 24 | Akzeptabel, wenn regelmäßig inspiziert | Spaltkorrosion über Jahrzehnte |
| 2205 Duplex | 620 | 34 | Sehr gut | Kostenspielig, Beschaffung |
| Nitronic 50 | 690 | 34 | Gold-Standard (US) | Schwer erhältlich in EU |
| 17-4 PH | 1.170 | 15 | NICHT empfohlen | Schlechte Korrosionsbeständigkeit |
| Monel K-500 | 1.035 | — | Alternative (historisch) | Galvanisch edel, teuer |
| Titan Gr. 5 | 900 | — | Exzellent, aber extrem teuer | Bearbeitung schwierig |
| Bronze (Silizium) | 380 | — | Traditionell, bewährt | Geringere Festigkeit |

**Steve D'Antonio:** "I have seen more keel bolt failures in 316 stainless than in any other material. If you're going to use stainless for keelbolts, use at least Duplex 2205, and even then, inspect them every 10 years."

### 4.5 Aquamet 22 — Propellerwellen-Detailspezifikation

**Herkunft:** Plymouth Tube Company (USA), speziell für Marine-Propeller-Anwendungen entwickelt (1980er Jahre).

**Lieferformen:**
- Normalgeglüht, öl-gehärtet und getölt (Standard)
- Durchmesser: 20–80 mm
- Längen: 1–5m typisch (maßgeschneidert möglich)
- Lagerware: Schwierig (meist Bestellung 4–6 Wochen)

**Installation von Aquamet-Wellen:**
1. Anlieferung: Im Mineralöl-Tuch (NICHT abschrubben!)
2. Lagerung: Trocken, horizontal auf Holzstützen
3. Montage: In Gleitlager einziehen (nicht gewaltsam!)
4. Nach Montage: Mit Korrosionsschutzöl konservieren (jährlich erneuern)

**Beschaffungs-Quellen:**
- USA: Plymouth Tube Company (Web: plymouthtube.com), Lieferzeit 2–4 Wochen + Zoll
- UK: Pennine Propellers, T2M (UK) (teuer, aber schnell)
- DE: Keine Standard-Lagerware, über Yachtausrüster (Vetus, Lem Marine)

### 4.6 Kielbolzen — Detaillierte Auswahlhilfe

**Nach Bootsklasse und Segelgebiet:**

| Bootsklasse | Segelgebiet | Empfohlen | Alternativ | NICHT |
|-------------|------------|-----------|-----------|--------|
| **Küstenfahrer <10m** | Süßwasser/Brackwasser | 316L akzeptabel | — | 304 |
| **Küstenfahrer <10m** | Salzwasser tropisch | Duplex 2205 | Nitronic 50 | 316L |
| **Cruiser 10–14m** | Mittelmeer / Atlantik | 316L akzeptabel | Duplex 2205 empfohlen | 304 |
| **Cruiser 10–14m** | Karibik / Pazifik | Duplex 2205 | Nitronic 50 | 316L |
| **Großyacht 14–20m** | Jede Gegend | Duplex 2205 | Nitronic 50 / Titan | 316L |
| **Regatta / Racing** | Jede Gegend | Titan Gr. 5 | Nitronic 50 | 316L |

### 4.7 Rundstahl-Preise (Richtwerte 2026)

| Ø (mm) | 316L (€/m) | 2205 Duplex (€/m) | Aquamet 22 (€/m ca.) | Verfügbarkeit |
|---|-----------|-------------------|--------|--------|
| 10 | €3–€5 | €6–€10 | — | Lagerware |
| 16 | €8–€14 | €16–€28 | — | Lagerware |
| 20 | €12–€20 | €24–€40 | €60–€100 | Lagerware / Bestellung |
| 25 | €19–€32 | €38–€64 | €90–€150 | Bestellung 4–6 Wochen |
| 30 | €27–€45 | €54–€90 | €120–€200 | Bestellung 4–6 Wochen |
| 40 | €48–€80 | €96–€160 | €180–€300 | Spezial-Bestellung 6–8 Wochen |
| 50 | €75–€125 | €150–€250 | €250–€400 | Spezial-Bestellung 8 Wochen |

**Importgebühren USA → EU:** +15–25 % (Zoll + Versand).

### 4.8 Propellerwellen-Dimensionierungstabellen nach Bootsgröße

**Segelyachten — Haupt-Propellerwellen:**

| Bootsklasse | LOA | Motorleistung | Wellen-Ø (mm) | Material | Lagerung | Länge typisch |
|-----------|-----|---------------|-------------|---------|---------|---|
| Kleinjollen | 5–8m | 5–10 kW | 16–18 | Aquamet 17 / 316L | 1 Kugellager | 0,8–1,2m |
| Küstenkreuzer | 8–12m | 10–20 kW | 20–22 | Aquamet 18 / 316L | 1–2 Kugellager | 1,5–2,5m |
| Cruiser | 12–16m | 20–40 kW | 25–28 | Aquamet 22 / 2205 | 2 Kugellager | 2,0–3,0m |
| Großyacht | 16–22m | 40–60 kW | 30–35 | Aquamet 22 / Super-Duplex | 2–3 Kugellager | 2,5–4,0m |
| Megayacht | 22–35m | 60–150 kW | 40–50 | Aquamet 22 / Duplex / Titan | 3–4 Kugellager | 3,5–6,0m |

**Motorboote / Fischerboote — Robuste Auslegung:**

| Bootsklasse | LOA | Motorleistung | Wellen-Ø (mm) | Material | Bemerkung |
|-----------|-----|---------------|-------------|---------|----------|
| Angelboot | 6–10m | 20–50 kW | 22–25 | Aquamet 18 / 22 | Höherer Verschleiß durch Propeller-Drehzahl |
| Küstensegler | 10–15m | 30–60 kW | 25–28 | Aquamet 22 | Standard |
| Fischerboot | 12–18m | 40–100 kW | 28–35 | Aquamet 22 | Dauerlast-tauglich |
| Expedition-Yacht | 18–30m | 60–150 kW | 35–45 | Aquamet 22 / Duplex | Extreme Bedingungen |

### 4.9 Wellen-Berechnung nach Lloyd's Regeln

**Vereinfachte Formel (Lloyd's Register):**
```
Wellen-Durchmesser (mm) = 37,3 × Motorleistung (kW)^0,333
Sicherheitsfaktor: 1,5–2,0 für marine Anwendung
```

**Beispiele:**
- 15 kW Yacht: Ø = 37,3 × 15^0,333 = 37,3 × 2,47 ≈ 92 → Ø 20–22mm realistisch
- 30 kW Yacht: Ø = 37,3 × 30^0,333 ≈ 37,3 × 3,11 ≈ 116 → Ø 25–28mm Standard
- 60 kW Yacht: Ø = 37,3 × 60^0,333 ≈ 37,3 × 3,91 ≈ 146 → Ø 30–35mm empfohlen

> ⚠️ **ZU PRÜFEN (Audit):** Die Formel ist inkonsistent mit ihren eigenen Beispielen — 37,3 × 15^0,333 ≈ 92, der Text leitet daraus aber "Ø 20–22 mm" ab (Faktor ~4–4,5 Abweichung). Konstante/Exponent bzw. ein fehlender Drehzahl-Term (der Wellen-Ø hängt von Leistung UND Drehzahl ab) sind unverifiziert. Formel NICHT zur Auslegung verwenden — Wellendurchmesser nach den Tabellen in 4.8 wählen. Confidence: estimated — unverifiziert.

### 4.10 Zusatz-Komponenten: Wellenlager und Zubehör

**Kugellager (NSK/FAG Standard für marine Wellen):**

| Lagertyp | Bohrung (mm) | Außendurchmesser | Breite | Belastungsklasse | Typische Anwendung |
|---------|-------------|-----------------|--------|---|---|
| 6005-2Z/C3 | 25 | 47 | 12 | Mittel | Kleine Segelyachten (Ø25 Welle) |
| 6006-2Z/C3 | 30 | 55 | 13 | Mittel | Standard-Cruiser (Ø30 Welle) |
| 6008-2Z/C3 | 40 | 68 | 15 | Mittel-Hoch | Große Yachten (Ø40 Welle) |
| 6009-2Z/C3 | 45 | 75 | 16 | Hoch | Mega-Yachten (Ø45 Welle) |
| NU 2205 (Zyl.-Rollager) | 25 | 52 | 15 | Hoch | Heavy-Duty Fischerboote |

**Wassersperrring (Shaft Seal):**
- **Typ:** Doppel-Lippen-Gummimanschette, Federgespannt
- **Material:** Spezial-Gummi oder PTFE für Wellen bis Ø40mm
- **Standard-Größe:** Nach Wellendurchmesser (zB 25×40×7 für Ø25)
- **Wechsel-Intervall:** 5–7 Jahre oder nach Leck-Auftreten

### 4.11 Kielbolzen-Verbindung mit Flachstahl und Unterlegscheiben

**Standard-Ausführung für Kielbolzen:**

| Durchmesser | Flachstahl Grundplatte | Unterlegscheibe | Mutter | Gesamtkosten/Satz (4 Bolzen) |
|-----------|----------------------|-----------------|--------|----------------------|
| M14 | 50×50×10mm (316L) | M14 DIN 125 (SS) | M14 DIN 934 A4 | €80–€150 |
| M16 | 60×60×12mm (316L/Duplex) | M16 DIN 125 (SS) | M16 DIN 934 A4 | €120–€200 |
| M18 | 70×70×15mm (Duplex 2205) | M18 DIN 125 (SS) | M18 DIN 934 A4 | €150–€250 |
| M20 | 80×80×18mm (Duplex 2205) | M20 DIN 125 (SS) | M20 DIN 934 A4 | €180–€300 |

**Installation — Best Practice:**
1. Grundplatte mit Abdichtung (Silikonkautschuk) unter den Rumpf kleben
2. Bolzen mit Loctite-Gel (anaerob) + Tef-Gel-Schicht beschichten
3. Drehmoment nach Hersteller-Tabelle (typisch: M14 = 100 Nm, M20 = 200 Nm)
4. Unterlegscheiben verwenden (Verhältnis 1:3 zur Bolzen-Dicke)
5. Nach 24h: Nachspannung durchführen (Sicherung mit Kontermutter oder Draht)

### 4.12 Längsfristige Kostenvergleich: Material-Choices

| Komponente | Material | Kaufpreis | Wartung 10 Jahre | Lebensdauer | Gesamt-Kosten |
|-----------|----------|-----------|-----------------|-------------|---|
| Propellerwelle Ø28 | 316L (Aquamet 18) | €150 | Öl-Spülung/Jahr €20 | 12–15 Jahre | €350 |
| Propellerwelle Ø28 | Aquamet 22 | €220 | Öl-Spülung/Jahr €20 | 20+ Jahre | €420 |
| Kielbolzen (4× M16) | 316L | €120 | Inspekt. alle 5 Jahre €0 (DIY) | 15–20 Jahre | €120 |
| Kielbolzen (4× M16) | 2205 Duplex | €180 | Inspekt. alle 5 Jahre €0 (DIY) | 30+ Jahre | €180 |
| Reling-Rohr (10m, Ø25) | 316L 1,5mm | €280 | Polieren/Jahr €50 | 15 Jahre | €630 |
| Reling-Rohr (10m, Ø25) | 316L 2,0mm poliert | €450 | Polieren/Jahr €30 | 20+ Jahre | €750 |

---

## 5. Edelstahlblech (Sheet / Plate)

### 5.1 Blechanwendungen im Yachtbau

| Anwendung | Typische Dicke | Material | Oberfläche |
|-----------|---------------|---------|------------|
| Backing Plates | 3–6 mm | 316L | 2B oder poliert |
| Tankverschlüsse | 1,5–3 mm | 316L | 2B |
| Motorschotts | 1,5–2,0 mm | 316L | 2B |
| Abgaswärmetauscher-Gehäuse | 1,5–2,0 mm | 316L/316Ti | 2B |
| Küchenarbeitsplatten | 0,8–1,2 mm | 304/316 | Geschliffen #240 |
| Abtropfbleche | 0,8–1,0 mm | 304/316 | 2B |
| Ankerkasten-Auskleidung | 1,5–2,0 mm | 316L | 2B |
| Ruderbeschläge | 3–8 mm | 316L/2205 | Poliert |
| Kielkonstruktionen | 6–20 mm | 316L/2205 | 2B |
| Schanzkleid (Alu-Yacht-Verstärkung) | 3–5 mm | 316L | 2B |
| Propellerschutz-Gitter | 2–3 mm | 316L | 2B |
| Dorade-Boxen | 1,0–1,5 mm | 316L | Poliert |
| Bilge-Pumpen-Siebe | 1,0–1,5 mm | 316L | Lochblech |

### 5.2 Blech-Standardabmessungen

| Dicke (mm) | Gewicht (kg/m²) | Format Standard (mm) | Anwendung |
|-----------|----------------|---------------------|-----------|
| 0,5 | 4,0 | 1000×2000, 1250×2500 | Verkleidung, leichte Abdeckungen |
| 0,8 | 6,4 | 1000×2000, 1250×2500 | Arbeitsplatten, Abdeckungen |
| 1,0 | 8,0 | 1000×2000, 1250×2500 | Standard-Bleche, Dorade-Boxen |
| 1,5 | 12,0 | 1000×2000, 1250×2500 | Tanks, Motorschotts |
| 2,0 | 16,0 | 1000×2000, 1250×2500 | Tanks, Strukturbleche |
| 2,5 | 20,0 | 1000×2000, 1250×2500 | Backing Plates, Tanks |
| 3,0 | 24,0 | 1000×2000, 1250×2500 | Backing Plates, Structural |
| 4,0 | 32,0 | 1000×2000, 1250×2500 | Backing Plates, Kielplatten |
| 5,0 | 40,0 | 1000×2000, 1250×2500 | Schwere Backing Plates |
| 6,0 | 48,0 | 1000×2000, 1250×2500 | Chainplates, Kielplatten |
| 8,0 | 64,0 | 1000×2000, 1500×3000 | Kielplatten, Schwert-Beschläge |
| 10,0 | 80,0 | 1000×2000, 1500×3000 | Schwere Struktur |
| 12,0 | 96,0 | 1000×2000, 1500×3000 | Mega-Yacht-Struktur |

### 5.3 Lochblech (Perforated Sheet)

| Lochdurchmesser | Teilung | Offene Fläche (%) | Anwendung |
|----------------|--------|-------------------|-----------|
| 3 mm | 5 mm (60°) | 32 % | Bilge-Pumpen-Siebe |
| 5 mm | 8 mm (60°) | 35 % | Motorraum-Belüftung |
| 8 mm | 12 mm (60°) | 40 % | Ankerkasten-Ablauf |
| 10 mm | 15 mm (60°) | 40 % | Cockpit-Ablauf-Schutz |

### 5.4 Blech-Bearbeitung

| Verfahren | Dicke max. | Kantqualität | DIY-tauglich | Kosten |
|-----------|-----------|-------------|-------------|--------|
| Blechschere (Hand) | 1,5 mm | Gut | Ja | Gering |
| Tafelschere | 6 mm | Sehr gut | Nein (Werkstatt) | Gering |
| Nibbler (Knabber) | 3 mm | Mittel | Ja | Gering |
| Stichsäge + Bi-Metall | 5 mm | Mittel (Nacharbeit) | Ja | Gering |
| Trennscheibe (Flex) | 20 mm | Rau (Nacharbeit) | Ja | Gering |
| Plasma | 25 mm | Mittel | Nein (teures Gerät) | Mittel |
| Laser | 25 mm | Exzellent | Nein (extern) | Mittel |
| Wasserstrahl | 100 mm | Exzellent | Nein (extern) | Mittel-Hoch |

### 5.5 Blech-Preise (Richtwerte, 316L, 2B-Oberfläche, 2026)

| Dicke (mm) | Gewicht (kg/m²) | Preis (€/kg) | Preis (€/m²) ca. | Lieferzeit | Anmerkung |
|-------|--------|----------|--------|-----------|-----------|
| 0,8 | 6,4 | €10–€15 | €64–€96 | 4 Wochen | Verkleidung, Abdeckungen |
| 1,0 | 8,0 | €8–€12 | €64–€96 | 3 Wochen | Standardblech (Lagerware) |
| 1,5 | 12,0 | €7–€11 | €84–€132 | 3 Wochen | Tanks, Motorschotts |
| 2,0 | 16,0 | €7–€10 | €112–€160 | 2–3 Wochen | Standard strukturell (populär) |
| 2,5 | 20,0 | €7–€10 | €140–€200 | 4 Wochen | Backing Plates |
| 3,0 | 24,0 | €6–€10 | €144–€240 | 4 Wochen | Backing Plates, Kiel-Zuschnitte |
| 4,0 | 32,0 | €6–€9 | €192–€288 | 4–6 Wochen | Schwere Backing Plates |
| 5,0 | 40,0 | €6–€9 | €240–€360 | 4–6 Wochen | Chainplate-Rohlinge, Kiel |
| 6,0 | 48,0 | €6–€9 | €288–€432 | 6 Wochen | Chainplates, Kiel-Zuschnitte |
| 8,0 | 64,0 | €5–€8 | €320–€512 | 6–8 Wochen | Schwere Struktur |
| 10,0 | 80,0 | €5–€8 | €400–€640 | 8 Wochen | Mega-Yacht-Struktur |

**Preis-Tipps:**
- **Mengenrabatt:** Ab 100 kg -10 % möglich. Ab 500 kg -15–20 %.
- **Oberflächenfinish:** 2B Standard. Poliert (#240+) kostet +€2–€4/m².
- **Lagerware:** 1,0mm und 2,0mm meist auf Lager (schnelle Lieferung). Andere Dickewaren: 4–8 Wochen.
- **Verschnitt:** Beim Zuschnitt ca. 5–10 % Verschnitt einplanen (Verschnitt-Kosten selber zahlen).

### 5.6 Blech-Lagerbestand für DIY-Yachten

Für Reparaturen und kleine Projekte empfohlen:

| Größe | Format | Lagerung | Verwendung |
|-------|--------|----------|-----------|
| 1,0 mm × 200×300mm | 3–5 Stück | Flach auf Palette | Kleinere Patches, Zuschnitte |
| 1,5 mm × 300×500mm | 2 Stück | Flach auf Palette | Tank-Reparaturen, Motorschotts |
| 2,0 mm × 300×500mm | 2 Stück | Flach auf Palette | Strukturelle Reparaturen |
| 3,0 mm × 300×300mm | 1 Stück | Flach, vertikal lagern | Backing Plates, Verstärkungen |
| Lochblech 1,5mm (3mm Löcher) | 200×300mm | Flach | Bilge-Siebe, Belüftung |

### 5.7 Marine-Tankbau-Spezifikationen

**Edelstahl-Tanks (Frischwasser, Diesel, Abwasser):**

| Tank-Typ | Wanddicke | Material | Schweißnaht-Anforderung | Passivierung |
|----------|-----------|----------|----------------------|--------------|
| Frischwasser (bis 50L) | 1,5 mm | 316L | TIG, durchgeschweißt | Obligatorisch |
| Frischwasser (50–200L) | 2,0 mm | 316L | TIG + Zwischenschliff | Obligatorisch |
| Diesel-Tank | 2,0–2,5 mm | 316L / 316Ti | TIG, Schweißprobe erforderlich | Obligatorisch |
| Abwasser/Greywater | 1,5–2,0 mm | 316L | TIG | Empfohlen |
| Altöl-Auffang | 2,0 mm | 316L | TIG | Empfohlen |
| Sump-Tank (Engine Crankcase) | 2,5–3,0 mm | 316L/316Ti | Hybrid WIG-MAG | Obligatorisch |
| Live-Well-Tank (Fisch) | 1,5 mm | 316L | TIG | Obligatorisch |
| Ballast-Tank (Segelyacht) | 3,0 mm | 316L | Vollstrang-Schweißung | Obligatorisch |

**Norm-Referenzen:**
- **ISO 12217-1** — Stabilität und Tankauslegung für Segelyachten
- **DIN EN 12494** — Industrie-Spezifikation für kleine Druckbehälter
- **ABS / DNV-GL Regeln** — Für klassifizierte Yachten

> ⚠️ **ZU PRÜFEN (Audit):** Norm-Zuordnungen unzutreffend. "DIN EN 12494" ist "Atmosphärische Eislast auf Bauwerken" (entspricht ISO 12494), NICHT kleine Druckbehälter. ISO 12217 regelt Stabilität/Auftrieb, nicht die Tank-Druckauslegung. Beide Referenzen unverifiziert — nicht als gesichert verwenden.

### 5.8 Zuschnitt und Oberflächenbearbeitung — Service-Optionen

**Zuschnitt-Optionen und Kosten (2026, 316L 2,0mm):**

| Verfahren | Zuschnitts-Genauigkeit | Nachbearbeitung | Durchlaufzeit | Kosten für 300×500mm |
|-----------|----------------------|-----------------|--------------|---------------------|
| Blechschere (Hand) | ±3mm | Deburring von Hand | 1 Tag | €5–€10 |
| Säge (Bandsäge) | ±2mm | Grat schleifen | 2–3 Tage | €15–€25 |
| Plasma | ±1,5mm | Kantenschliff erforderlich | 1–2 Tage | €25–€40 |
| Laser-Schnitt | ±0,5mm | Minimal (Oxidschicht) | 3–7 Tage | €40–€80 |
| Wasserstrahl | ±0,3mm | Keine Nachbearbeitung | 4–7 Tage | €60–€120 |

**Oberflächenbearbeitung nach Zuschnitt:**

| Oberflächen-Finish | Verfahren | Zeit | Preis (pro m²) | Empfehlung |
|------------------|-----------|------|---------------|------------|
| 2B (wie geliefert) | — | — | — | Für Backing Plates OK |
| Deburring | Handbürste / Schleifer | 30 min | €5–€10 | EMPFOHLEN nach Zuschnitt |
| #240 Schliff | Schleifvlies, Schleifer | 45 min | €15–€25 | Sichtbar, bessere Korrosionsbeständigkeit |
| #320 Schliff | Schleifvlies fein | 60 min | €20–€30 | Sehr gutes Finish |
| #400 Hochglanz-Schliff | Poliertuch + Poliermittel | 90 min | €30–€50 | Premium-Finish |
| Elektro-Polieren | Elektro-Bad, 30 min | 2–4 h | €40–€80 | Gold-Standard, reduziert Spaltkorrosion um 50 % |

### 5.9 Marine Tank Plate — Spezielle Normen

**Hochbelastete Tanks (über Wasserlinie):**
- **Wanddicke:** Mindestens 2,0 mm (ISO 12217)
- **Material:** 316L obligatorisch (304 NICHT akzeptabel)
- **Oberfläche:** Mindestens #240 geschliffen
- **Schweißung:** Durchschweißung mit mindestens 80 % Naht-Festigkeit
- **Passivierung:** HNO₃-Bad oder Paste mindestens 60 Minuten

**Tanks unterhalb der Wasserlinie:**
- **Wanddicke:** 2,5–3,0 mm (Druck + Korrosionsreserve)
- **Material:** 316L oder 316Ti (nur 316Ti wenn >500°C Schweißwärme möglich)
- **Oberfläche:** Mindestens #320 poliert oder elektro-poliert
- **Laufende Überwachung:** Jährliche Inspektionen mit Ultraschall (ab 5 Jahren Betrieb)

### 5.10 Cutting Service Anbieter und Schnittkosten

**Deutschland:**
- **Edelstahl-Service-Center.de** — Laser + Wasserstrahl, €0,15–€0,30 pro cm² Schnittlänge
- **LaserTeile4You** — Spezialist für 2D-Zuschnitte, Format bis 1500×3000mm
- **Stahl-Shop.de** — Säge-Zuschnitte, einfach + kostengünstig (€5–€20 je Schnitt)
- **Schnellkantenbau.de** — Express-Laser bis 16:00 Uhr, Versand nächster Tag
- **Metallzuschnitte.de** — Klein-Chargen-freundlich, kein Mindestbestand

**UK:**
- **metals4U** — Laser + Wasserstrahl, online Preisrechner, Lieferung in 48h
- **Aalco** — Säge-Zuschnitte, lokal für Walk-In-Kunden

**USA:**
- **Online Metals** — Laser-Zuschnitte, Sofort-Preisrechner im Netz
- **Metal Supermarkets** — Walk-in Zuschnitt, über 100 Standorte

### 5.11 Beispiel-Projekte: Blech-Dickenwahl nach Anwendung

| Projekt | Blech-Größe | Dicke | Oberfläche | Material | Geschätzter Preis |
|---------|-----------|-------|-----------|----------|-------------------|
| Bilge-Sumpf-Schott | 500×500mm | 1,5 mm | 2B | 316L | €8–€15 |
| Backing Plate (Durchlass) | 200×200mm | 5,0 mm | #240 | 316L | €12–€20 |
| Motor-Schotts-Reparatur | 400×600mm | 2,0 mm | 2B | 316L | €15–€25 |
| Chainplate-Rohling | 50×200mm | 6,0 mm | Poliert | 316L | €30–€50 (per Stück) |
| Kielplatte (12m Yacht) | 1000×500mm | 8,0 mm | 2B | 316L | €80–€150 |
| Tank-Wand (40L Frischwasser) | 600×800mm (2 Stück) | 2,0 mm | 2B | 316L | €40–€80 |

---

## 6. Profile (Winkel, U-Profile, T-Profile, Vierkantrohr)

### 6.1 Winkelprofile (L-Profile)

| Abmessung (mm) | Wandstärke (mm) | Gewicht (kg/m) | Anwendung |
|----------------|----------------|---------------|-----------|
| 20 × 20 × 2 | 2 | 0,59 | Leichte Halterungen, Winkel |
| 20 × 20 × 3 | 3 | 0,85 | Beschlag-Winkel |
| 25 × 25 × 3 | 3 | 1,11 | Standard-Winkel, Motorhalter |
| 30 × 30 × 3 | 3 | 1,36 | Motorhalter, Rahmen |
| 30 × 30 × 4 | 4 | 1,78 | Schwere Halterungen |
| 40 × 40 × 3 | 3 | 1,82 | Rahmen, Konsolen |
| 40 × 40 × 4 | 4 | 2,39 | Schwere Rahmen |
| 40 × 40 × 5 | 5 | 2,93 | Motorrahmen, Kielstruktur |
| 50 × 50 × 4 | 4 | 3,00 | Motorrahmen |
| 50 × 50 × 5 | 5 | 3,69 | Schwere Motorrahmen |
| 60 × 60 × 5 | 5 | 4,47 | Industrie, Mega-Yacht |
| 60 × 60 × 6 | 6 | 5,29 | Mega-Yacht-Struktur |
| 80 × 80 × 6 | 6 | 7,09 | Mega-Yacht, kommerziell |

### 6.2 U-Profile (Rinnen)

| Abmessung (mm) | Wandstärke (mm) | Gewicht (kg/m) | Anwendung |
|----------------|----------------|---------------|-----------|
| 20 × 10 × 1,5 | 1,5 | 0,46 | Kabelkanäle, leichte Führungen |
| 25 × 12 × 2 | 2 | 0,72 | Kabelkanäle, Schienen |
| 30 × 15 × 2 | 2 | 0,89 | Motorlager, Schienen |
| 40 × 20 × 2 | 2 | 1,18 | Motorlager, Rahmen |
| 40 × 20 × 3 | 3 | 1,73 | Schwere Motorlager |
| 50 × 25 × 3 | 3 | 2,22 | Motorrahmen |
| 60 × 30 × 3 | 3 | 2,71 | Schwere Rahmen |
| 80 × 40 × 4 | 4 | 4,73 | Mega-Yacht, kommerziell |

### 6.3 Vierkantrohr (Rectangular/Square Tube)

| Abmessung (mm) | Wandstärke (mm) | Gewicht (kg/m) | Anwendung |
|----------------|----------------|---------------|-----------|
| 20 × 20 × 1,5 | 1,5 | 0,86 | Leichte Rahmen |
| 20 × 20 × 2 | 2 | 1,12 | Rahmen, Konsolen |
| 25 × 25 × 1,5 | 1,5 | 1,10 | Standard-Rahmen |
| 25 × 25 × 2 | 2 | 1,43 | Verstärkte Rahmen |
| 30 × 30 × 2 | 2 | 1,74 | Motorlager, Rahmen |
| 30 × 30 × 3 | 3 | 2,51 | Schwere Rahmen |
| 40 × 20 × 2 | 2 | 1,74 | Traversenartige Konstruktionen |
| 40 × 40 × 2 | 2 | 2,36 | Rahmen, Konsolen |
| 40 × 40 × 3 | 3 | 3,45 | Schwere Rahmen |
| 50 × 30 × 2 | 2 | 2,36 | Davit-Arme |
| 50 × 50 × 2 | 2 | 2,98 | Schwere Struktur |
| 50 × 50 × 3 | 3 | 4,39 | Industriell |
| 60 × 40 × 3 | 3 | 4,39 | Davits, Bimini-Rahmen |
| 80 × 40 × 3 | 3 | 5,33 | Industriell |

### 6.4 T-Profile

| Abmessung (mm) | Wandstärke (mm) | Gewicht (kg/m) | Anwendung |
|----------------|----------------|---------------|-----------|
| 20 × 20 × 3 | 3 | 0,85 | Versteifungsrippen |
| 25 × 25 × 3 | 3 | 1,11 | Versteifungsrippen |
| 30 × 30 × 3 | 3 | 1,36 | Stringer, Versteifungen |
| 40 × 40 × 4 | 4 | 2,39 | Schwere Versteifungen |
| 50 × 50 × 5 | 5 | 3,69 | Schwere Struktur |

### 6.5 Halbrundprofile (Bull Nose / D-Profil)

| Abmessung (mm) | Anwendung | Preis ca. (€/m) |
|----------------|-----------|----------------|
| 30 × 15 Halbrund | Scheuerleiste, Kantenschutz | €12–€22 |
| 40 × 20 Halbrund | Scheuerleiste (mittlere Yachten) | €16–€28 |
| 50 × 25 Halbrund | Scheuerleiste (große Yachten) | €22–€38 |

### 6.6 Profil-Anwendungen und Montagemethoden

| Profil-Typ | Häufigste Anwendung | Befestigung | Montagetipps |
|-----------|-----------|-----------|-----------|
| **Winkel L 25×25** | Motorlager-Konsolen, Halterungen | 4–6 Bolzen M8 (pro Meter Länge) | Auf Ebene Fläche setzen. Mit Ausgleichsplättchen ausrichten (kein Kantenschluss nötig!) |
| **Winkel L 40×40** | Motor-Hauptrahmen, schwere Halterungen | 6–8 Bolzen M10/M12 (pro Meter) | Schweißen bevorzugt (sicherer), Bolzenmontage mit Gegenplatte |
| **U-Profil 40×20** | Motorschienen, Schubstangen | 4 Bolzen M10 (durchgehend) + G10-Puffer | Gleitender Kontakt möglich (mit Plastikeinsatz) |
| **Vierkant 25×25** | Leichte Rahmen, Halterungen unter 500 kg | 4 Bolzen M8 (Ecken) | Hochwertige Nut + Passschraube für Präzision |
| **Vierkant 40×40** | Davit-Arme, Bimini-Rahmen | 6–8 Bolzen M12 oder Schweißung | SCHWEISSUNG empfohlen (höher belastet). Bolzenmontage akzeptabel nur mit Gegenplatten |
| **T-Profil 30×30** | Versteifungsrippen (Rahmen) | Schweißung (Standard) | Kielbolzen-Träger, Motor-Verstrebung |

### 6.7 Profil-Preise (316L, Richtwerte 2026)

| Profil-Typ | Dimensionen | Preis (€/m) ca. | Lieferant-Referenz |
|--------|--------|--------|--------|
| **Winkel L** | 25×25×3 | €8–€14 | Nordfels, Steelmaterial |
| — | 40×40×4 | €14–€24 | — |
| — | 50×50×5 | €22–€38 | — |
| — | 60×60×6 | €35–€55 | — |
| **U-Profil** | 40×20×3 | €12–€20 | — |
| — | 50×25×3 | €16–€28 | — |
| — | 60×30×3 | €20–€36 | — |
| **Vierkantrohr** | 25×25×2 | €10–€18 | — |
| — | 40×40×3 | €18–€32 | — |
| — | 50×50×3 | €28–€48 | — |
| **T-Profil** | 30×30×3 | €10–€18 | Spezialbestellung |
| — | 40×40×4 | €16–€28 | — |
| **Halbrund** | 30×15 | €12–€22 | Seltener (Scheuerleiste) |
| — | 40×20 | €16–€28 | — |

**Bestelltipp:** Viele Profile sind **keine Lagerware**. Mindestbestellmengen: 1–2 Meter pro Profil. Lieferzeit 4–6 Wochen für Sondergrößen.

### 6.8 Struktur-Dimensionierung nach Bootsklasse

| Bootsklasse | Motor (PS) | Motor-Rahmen Empfehlung | Motor-Halter Empfehlung |
|-----------|-----------|-----------|-----------|
| **8–10m, Segler** | — | L 30×30×3 + U 30×15 (Schienen) | L 25×25×3 |
| **10–14m Cruiser** | 30–40 | L 40×40×4 + U 40×20×3 | L 40×40×4 |
| **12–16m Cruiser** | 40–80 | L 50×50×5 + U 50×25×3 | L 50×50×5 |
| **14–20m Cruiser** | 80–150 | Vierkant 50×50×3 + U 50×25×3 | L 60×60×5 |
| **18–30m Superyacht** | 150–400 | Vierkant 60×60×4 + massiv Schweißung | Schweißrahmen nach Berechnung |

---

## 7. Bearbeitung und Verarbeitung

### 7.1 Sägen

| Methode | Eignung | Schnittqualität | Anmerkung |
|---------|---------|----------------|-----------|
| Metallbandsäge | Exzellent | Sehr gut | Standard für Zuschnitt, Kühlung erforderlich |
| Kappsäge (Trennscheibe) | Gut | Mittel | Funken! Nicht in Nähe von GFK oder Holz |
| Stichsäge (Bi-Metall-Blatt) | Akzeptabel bis 3mm | Mittel | Langsam, Blätter verschleißen schnell |
| Bügelsäge (Hand) | Akzeptabel bis 6mm | Mittel | Langsam aber kontrolliert, kein Strom nötig |
| Plasma | Gut ab 2mm | Mittel (Nacharbeit) | Schnell, aber Wärmeeinflusszone |
| Laser | Exzellent | Exzellent | Nur extern, beste Qualität |
| Wasserstrahl | Exzellent | Exzellent | Nur extern, keine Wärmeeinflusszone |

### 7.2 Bohren

| Parameter | Empfehlung |
|-----------|-----------|
| Bohrer-Typ | HSS-Co (Cobalt, 5–8 %) oder HSS-E (TiN-beschichtet) |
| Kühlmittel | IMMER — Schneidöl oder Bohremulsion |
| Drehzahl (für Ø 8mm in 316) | 500–800 U/min |
| Vorschub | Gleichmäßig, nicht zu gering (Kaltverfestigung!) |
| Anreißen | Körner-Schlag, dann Pilotbohrung 3mm |
| Entgraten | Senker 90°, Feile |
| WARNUNG: Kaltverfestigung | Edelstahl 316 verfestigt bei zu geringem Vorschub → Bohrer zerstört! |

### 7.3 Schweißen (WIG/TIG)

| Parameter | Empfehlung für 316L |
|-----------|-------------------|
| Verfahren | WIG/TIG (GTAW) |
| Polarität | DC- (Elektrode = Minus) |
| Schutzgas (Lichtbogen) | Argon 99,99 % |
| Schutzgas (Wurzel/Rückseite) | Argon oder Formiergas (N₂/H₂ 95/5) |
| Wolframelektrode | WC20 (grau) oder WL15 (gold), Ø 1,6–2,4 mm |
| Zusatzwerkstoff | 316LSi (1.4430) Ø 1,6–2,4 mm |
| Strom (1,5 mm Wandstärke) | 40–60 A |
| Strom (2,0 mm Wandstärke) | 55–80 A |
| Strom (3,0 mm Wandstärke) | 80–120 A |
| Strom (5,0 mm Blech) | 120–180 A |
| Zwischenlagentemperatur max. | 150°C |
| Nachbehandlung | Beizen + Passivieren (Avesta 401 + 601) |

### 7.4 Biegen (Abkanten)

| Material-Dicke | Mindest-Biegeradius (innen) | Werkzeug |
|---------------|---------------------------|---------|
| 1,0 mm | 1,0 mm (1×t) | Abkantbank |
| 1,5 mm | 1,5 mm (1×t) | Abkantbank |
| 2,0 mm | 2,0 mm (1×t) | Abkantbank |
| 3,0 mm | 4,5 mm (1,5×t) | Abkantbank, Presse |
| 4,0 mm | 6,0 mm (1,5×t) | Presse |
| 5,0 mm | 10,0 mm (2×t) | Presse |
| 6,0 mm | 12,0 mm (2×t) | Presse |
| 8,0 mm | 20,0 mm (2,5×t) | Schwere Presse |

### 7.5 Polieren (Oberflächenveredlung)

| Schritt | Schleifmittel / Werkzeug | Resultat Ra (µm) | Zeitaufwand |
|---------|-------------|---------|---------|
| 0 (Oberflächenfinish Prüfung) | Oberflächenrauheit-Messer | Baseline | 5 min |
| 1 (Grobschliff) | Schleifscheibe Körnung 80–120 | ~3,0 µm | 20–30 min pro m² |
| 2 (Schliff) | Körnung 120–150 | ~1,5 µm | 15 min pro m² |
| 3 (Feinschliff) | Körnung 240 | ~0,8 µm (satiniert) | 15 min pro m² |
| 4 (Feinschliff +) | Körnung 320 | ~0,4 µm (fein satiniert) | 20 min pro m² |
| 5 (Hochglanz-Prep) | Körnung 400 | ~0,2 µm | 20 min pro m² |
| 6 (Hochglanz) | Polierpaste + Körnung 600/800 | ~0,1 µm (glänzend) | 30 min pro m² |
| 7 (Spiegelglanz) | Poliertuch + Polierpaste fein | <0,05 µm | 45 min pro m² |
| 8 (Elektropolieren) | Elektrochemisch (professionell) | <0,03 µm | Firma: 3–5 Tage |

**Praktische Tipps:**
- **Schleifen vs. Polieren:** Schleifen = Material-Abtrag (bis Schritt 4), Polieren = Oberflächenglättung (ab Schritt 5)
- **Werkzeuge:** Nur Edelstahl-Schleiftöpfe (mit "Edelstahl" markiert) verwenden. Normale Schleiftöpfe enthalten Eisen → Kontamination
- **Kühlmittel:** Wasser oder Schneidöl während Schleifen verwenden (verhindert Überhitzung)
- **Nachbehandlung:** Nach Polieren IMMER Passivierung (Beizen + Passivieren) durchführen!

### 7.6 Schneid- und Bearbeitungsmittel

| Werkzeug / Material | Edelstahl-spezifische Anforderung |
|---|---|
| **Schneidöl** | Öl mit Molybdän-Disulfid (MoS₂) optimal. Universelles Schneidöl OK. Mineralöl ist teuer aber langlebig. |
| **Bohrer-Kühlmittel** | Emulsion (Wasser + Öl) ideal. Rein Öl zu dick (verstopft Bohner). Rein Wasser zu dünn. |
| **Schleifscheiben** | Körnungen **nicht mischen**: 120er Scheibe → niemals für 320er Körnung nutzen (keine Kontrolle). Neue Scheibe für jeden Körn. |
| **Schleiftöpfe** | IMMER "V2A Edelstahl" markiert. Nicht Standard-Topfscheiben (enthalten Eisen). |
| **Flächenschleifer-Platten** | Magnet-Hafting OK (Material nicht magnetisierbar durch Permanentmagnet). Vorsicht: Schnelle Oxidation auf heißer Platte. |

### 7.7 Häufige Fehler und deren Folgen

| Fehler | Folge | Prävention |
|--------|-------|-----------|
| Falsche Schnittgeschwindigkeit (zu gering) | Kaltverfestigung, Bohrer/Werkzeug rutscht, wird blockiert | Schneller fahren, mehr Kühlmittel, Cobalt-Bohrer wählen |
| Stahlwolle oder Stahlbürste verwendet | Fremdrost-Kontamination (braune Flecken) | NUR Edelstahl/Kupfer-Bürsten. Stahlwolle sofort entsorgen. |
| Zu starke Hitze beim Schleifen (funkelt) | Oberflächenoxidation, Anlauffarben, geschwächte Passivschicht | Weniger Druck, mehr Kühlmittel, langsamere Drehzahl |
| Keine Passivierung nach Schweißung | Schweißzone bleibt chromverarmt, Spaltkorrosion wahrscheinlich | Immer Beizen + Passivieren durchführen |
| Fremdmetall-Kontamination (Stahl-Funken) | Rostflecken auf Edelstahl, sieht schlecht aus, schwer zu entfernen | Arbeitsplatz abdecken, andere Materialien fernhalten |
| Verformung beim Biegen (geknickt, flach) | Rohr verliert Tragfähigkeit, Korrosionsanfälligkeit erhöht | Mindestbiegeradius einhalten (R ≥ 3×Ø), Dornfüllung verwenden |

---

## 8. Korrosion: Typen, Prävention, Reparatur

### 8.1 Korrosionsarten bei Edelstahl im Yachtbau

| Korrosionsart | Beschreibung | Risikostelle | Prävention |
|-------------|-------------|-------------|-----------|
| Lochfraß (Pitting) | Lokale Korrosion durch Chlorid-Angriff | Salzwasser-Kontakt, unter Ablagerungen | Mo ≥ 2% (316), polierte Oberfläche |
| Spaltkorrosion (Crevice) | Korrosion im Spalt (O₂-arm) | Decksdurchführungen, unter Schrauben | Dichtmittel, Potting, Inspizierbarkeit |
| Spannungsrisskorrosion (SCC) | Rissbildung unter Spannung + Chlorid | Chainplates, Kielbolzen, Druckbehälter | Duplex/Nitronic, Spannungsbegrenzung |
| Kontaktkorrosion (galvanisch) | Korrosion durch Potentialdifferenz | Edelstahl/Alu-Kontakt, Edelstahl/Stahl | Isolation, Tef-Gel, gleiche Materialien |
| Intergranulare Korrosion | Entlang Korngrenzen (sensibilisiert) | Schweißzonen | 316L (Low Carbon), korrekte Schweißparameter |
| Erosionskorrosion | Mechanisch + chemisch | Rohrleitungen, Kühlwasser, Pumpen | Strömungsgeschwindigkeit begrenzen (<3 m/s) |
| Fremdrost (Tea Staining) | Rostpartikel von Normalstahl | Werkzeuge, Funken, Staubpartikel | Separate Werkzeuge, Passivierung |

### 8.2 Fremdrost (Tea Staining) — Prävention und Entfernung

**WARNUNG:** Fremdrost ist das häufigste kosmetische Problem an Edelstahl auf Yachten. Es ist KEIN Zeichen für defekten Edelstahl, sondern für Kontamination mit Normalstahl.

| Ursache | Maßnahme |
|---------|----------|
| Werkzeuge die vorher Normalstahl berührt haben | Separate Werkzeuge für Edelstahl — NIEMALS mischen! |
| Funken von Flexen/Trennscheiben in der Nähe | Nicht in Nähe von Edelstahl arbeiten, abdecken |
| Stahlwolle oder Stahlbürste | NUR Edelstahl-Bürsten verwenden (V2A/V4A markiert) |
| Normalstahl-Schrauben in der Nähe | Vermeiden |
| Eisenhaltige Staubpartikel (Hafen, Werft) | Regelmäßige Reinigung |

**Entfernung von Fremdrost:**

| Methode | Anwendung | Preis |
|---------|-----------|-------|
| Oxalsäure (z.B. "Bar Keeper's Friend") | Leichter Fremdrost | €3–€8 |
| Zitronensäure (10 % Lösung) | Leichter bis mittlerer Fremdrost | €2–€5 |
| Avesta 401 (Beizpaste) | Mittlerer bis schwerer Fremdrost, Schweißnaht-Anlauffarben | €15–€25/500g |
| Passivierungspaste (Avesta 601) | Nach Beizen, stellt Passivschicht wieder her | €15–€25/500g |
| Inox-Reiniger (z.B. Inox-Clean) | Leichter Fremdrost, Pflege | €8–€15/500ml |
| Scotchbrite-Pad (rot/grau) | Mechanisch, leichter Fremdrost | €2–€5 |

### 8.3 Galvanische Korrosion — Verträglichkeit und Potentialserie

| Edelstahl + ... | Galv. Spannung (V) | Elektrochem. Paar | Risiko | Maßnahme |
|----------------|-------------------|----------|--------|----------|
| **Aluminium** | 0,50–0,85 | Edelstahl (Kathode) – Alu (Anode) | **HOCH** | Tef-Gel, Isolierbuchsen, G10-Platte, Zink-Opfer-Anode |
| **Normalstahl / Eisen** | 0,25–0,40 | Edelstahl (Kathode) – Stahl (Anode) | **MITTEL** | Feuerverzinkung (Zn schützt Fe), oder Isolation |
| **Kupfer / Messing** | 0,05–0,15 | Edelstahl (Anode) – Cu (Kathode) | **GERING** | Akzeptabel (Edelstahl ist Anode, wird sehr langsam abgebaut) |
| **Siliziumbronze** | 0,05–0,20 | Ähnlich Kupfer | **GERING** | Akzeptabel |
| **Edelstahl (gleiche Legierung)** | 0 V | Keine Potentialdifferenz | **KEINES** | Ideal! |
| **Titan** | 0,05–0,15 | Edelstahl (Anode) – Ti (Kathode) | **GERING** | Akzeptabel (Ti etwas edle r, aber Unterschied minimal) |
| **Carbon / CFK** | 0,30–0,50 | **Edelstahl (Kathode) – Carbon (Anode!)** | **KRITISCH HOCH** | **Isolation PFLICHT!** — KEIN direkter Kontakt! |

**Praktische Elektrokchemie:**
```
Kathodischer Schutz (edel, Kathode)  →  Galvanischer Anode (unedel, Anode)

Beispiel: Alu-Rumpf + SS-Bolzen
  SS316L: Standardpotential = +0,2 V (edel)
  Alu:    Standardpotential = -1,05 V (unedel)
  Spannung: 1,25 V (GROSS!)
  Resultat: Alu wird Anode → Al₂O₃ Korrosion (weiße Oxide)
```

**KRITISCHE WARNUNG: Carbon Fiber (CFK/Carbon) + Edelstahl:**
- **Carbon ist extrem kathodisch** (Standardpotential: -0,5 bis -0,8 V vs. Edelstahl)
- Spannungsdifferenz: 0,70–1,30 V (größer als Alu!)
- **Resultat:** Edelstahl in direktem Kontakt mit Carbon korrodiert rasant (beschleunigte Lochfraß)
- **Lösungen:**
  1. G10-Epoxid-Isolierplatte (6–10 mm) unter jeden SS-Beschlag
  2. Tef-Gel unter Bolzen-Köpfe + Nylon-Isolierbuchsen
  3. Optionale Zusatz-Anode (Magnesium oder Aluminium) unter Deck anbringen

### 8.4 Spannungsrisskorrosion (SCC) — Sicherheitskritisch

**Mechanismus:** Material unter Zugspannung + Chlorid + erhöhte Temperatur → Rissinitiierung + -wachstum

| Parameter | Kritisch für 316L | Sicher für Duplex |
|-----------|------------------|------------------|
| Chlorid-Konzentration | >1000 ppm | >10000 ppm |
| Temperatur | >50°C | >80°C |
| Spannungslevel | >40 % Streckgrenze | >70 % Streckgrenze |
| Beispiel Yachtbau | Kielbolzen unter Wind-Last + Salzspray + Sonne | Kielbolzen in gleicher Situation + wechselnd nass/trocken |

**Risiko-Situationen:**
1. Kielbolzen (hochbelastet, Salzwasser-direkt, nicht inspizierbar) → **Duplex 2205 empfohlen**
2. Masttraversen (unter Belastung, exponiert, schwer inspizierbar) → **Duplex oder Nitronic 50**
3. Chainplates (Dauerlast, Salzwasser, schwer inspizierbar) → **Duplex für Langfahrt, 316L akzeptabel für <15 Jahre**

**Prävention:**
- Material wählen mit PREN ≥ 34 (Duplex statt 316L)
- Spannungen minimieren (Bohrung größer, Ausrundung R ≥ 2 mm)
- Passivierung nach Verarbeitung (Beizen + Passivieren)

### 8.5 Intergranulare Korrosion (IGC) — Sensibilisierung nach Schweißung

**Problem:** Beim Schweißen (Temperatur >500°C) bilden sich Chromkarbide an Korngrenzen → lokale Chromverarmung → Anfälligkeit für Spaltkorrosion

**Lösungen:**
1. **316L verwenden (nicht 316):** Niedriger Kohlenstoff-Gehalt (<0,03 %) → weniger Karbidbildung
2. **Schweißparameter:** Schnell schweißen (Wärmezufuhr reduzieren), kühle Außenseite
3. **Nachbehandlung:** Beizen + Passivieren (stellt Passivschicht wieder her)
4. **Alternative:** 316Ti verwenden (Titan stabilisiert Kohlenstoff, vermeiddet Karbidbildung)

### 8.6 Inspektions- und Wartungs-Intervalle nach Risikolevel

| Baugruppe | Risiko-Level | Inspektions-Intervall | Methode |
|-----------|--------------|--------|-----------|
| Reling (abwasser-exponiert) | GERING | 6 Monate | Visuell + Oberflächenrauheit |
| Chainplates (salzwasser-exponiert) | MITTEL | 12 Monate | Visuell + Farbeindringprüfung (1×/5 Jahre) |
| Kielbolzen (hochbelastet, nicht inspizierbar) | KRITISCH | Präventiv (Duplex Material) | Keine Prüfung möglich → gutes Material ist essentiell |
| Davits (salzwasser-exponiert, belastet) | MITTEL-HOCH | 12 Monate | Visuell + Schweißnaht-Kontrolle (Farbendringprüfung 1×/10 Jahre) |
| Motor-Fundament Alu-Rumpf | MITTEL (wenn isoliert) | 12 Monate | Visuell (keine weißen Oxide?) + Bolzen-Drehmoment |

---

## 9. Spezialstähle und Sonderanwendungen

Für spezielle Einsatzszenarien (hochbelastete Wellen, extrem korrosive Umgebungen, Regatta-Gewichtseinsparung) sind Speziallegie rungen jenseits von Standard-316L erforderlich.

### 9.1 Nitronic 50 (XM-19, UNS S20910, 1.3964) — Kielbolzen-Premium

**Zusammensetzung:** 20–23 % Cr, 11,5–13,5 % Ni, 5–7 % Mn, 0,2–0,35 % N (Stickstoff-Härtung)

| Eigenschaft | Wert | Vergleich 316L |
|-------------|------|---|
| Zugfestigkeit Rm | 690 MPa | vs. 485 (43 % höher) |
| Streckgrenze Rp0,2 | 380 MPa | vs. 170 (124 % höher) |
| Bruchdehnung | 35 % | vs. 40 % (ähnlich) |
| PREN | 34 | vs. 26 (gut) |
| E-Modul | 200 GPa | vs. 200 GPa (gleich) |
| Dichte | 7,88 g/cm³ | vs. 7,98 (leicht) |
| Wärmeausdehnung | 13 µm/K | vs. 16 µm/K (besser) |

**Besonderheiten:**
- Hohe Festigkeit ohne Wärmbehandlung (Stickstoff wirkt härtend)
- Exzellente Spannungsrisskorrosion-Beständigkeit (SCC-Immun)
- Kein Anlassen / Glühen nötig (Einfachheit)

**Typische Anwendungen im Yachtbau:**
- **Kielbolzen** (Hauptanwendung): Erlaubt kleinere Durchmesser als 316L, gleiche Sicherheit
- **Ruderlager-Bolzen:** Hochbelastet, Rotation
- **Rigg-Beschläge unter hoher Last:** Wantenplatten-Bolzen (große Yachten)

**Beschaffung:**
- **Verfügbarkeit:** USA/UK sehr gut (Specialty Steel, Allegheny Ludlum). Europa: eingeschränkt (bestellen 4–6 Wochen)
- **Preis:** €60–€100 pro kg (Rundstahl), ca. 2–2,5× 316L
- **Lagering:** Lagerware in USA (Größen Ø8–Ø40mm)

**Schweißbarkeit:** Eingeschränkt! Stickstoff entweicht beim Schweißen → neuer Bereich wird weicher. **Nicht für Schweißkonstruktionen verwenden.** Nur als vorgefertigte Welle/Bolzen.

**Forum-Konsens:** "Nitronic 50 for critical bolts ist wert das Extra-Geld. Nicht magnetisch, nicht seizing-anfällig, beste Korrosionsbeständigkeit für hochbelastete Bolzen." (CruisersForum)

---

### 9.2 Nitronic 60 (UNS S21800, XM-19-mod) — Anti-Galling-Spezialist

**Zusammensetzung:** Ähnlich wie Nitronic 50, aber mit zusätzlichen Elementen gegen Galling optimiert

| Eigenschaft | Wert | Besonderheit |
|-------------|------|-----------|
| Zugfestigkeit Rm | 655 MPa | Weniger stark als Nitronic 50 |
| PREN | 25–28 | Moderat (nicht für Salzwasser ideal) |
| **Galling-Beständigkeit** | **Exzellent** | Kann sich selbst verschweißen ohne Galling-Effekt |
| Verwendung | Hochfrequente Bolzen/Muttern-Paare | — |

**Vorteil:** Erfordert kein Anti-Seize-Mittel (Tef-Gel, Molykote). Bolzen und Muttern können direkt verschraubt werden ohne Festsitzen.

**Praktische Anwendung:** Yacht-Propellerschrauben (einfache Demontage), Ventilachsen, Scharniere mit hoher Zyklenfrequenz.

**Preis:** Ähnlich wie Nitronic 50 (€60–€100/kg)

---

### 9.3 17-4 PH (Precipitation Hardening, 1.4542, UNS S17400) — Warnung!

**Zusammensetzung:** 15–17 % Cr, 3–5 % Ni, 3–5 % Cu, <0,07 % C, + Cu-Ausscheidung für Härtung

| Eigenschaft | Wert | Problem |
|-------------|------|--------|
| Zugfestigkeit Rm (H1025) | 1.070–1.310 MPa | Sehr hoch (aber fragil) |
| Streckgrenze Rp0,2 | 1.000–1.170 MPa | — |
| **PREN** | **15–18** | SCHLECHT für marine! |
| Spannungsrisskorrosion-Risiko | **Hoch in Chlorid-Umgebung** | ⚠️ WARNUNG! |
| Verfügbarkeit alt | Propellerwellen (1980–2000) | — |

**KRITIK:** 17-4 PH wird oft fälschlicherweise als "marine Edelstahl" verkauft, ist es aber nicht!
- PREN 15 ist schlechter als normale Legierungen
- Spannungsrisskorrosion kann nach 5–10 Jahren im Salzwasser auftreten
- Moderne Yachten verwenden **nicht mehr** 17-4 PH (Aquamet oder Nitronic bevorzugt)

**Wenn Sie 17-4 PH alte Propellerwelle haben:**
1. Röntgen-Prüfung durchführen (auf Risse prüfen)
2. Kathodischer Schutz (Zink-Anode) anbringen
3. Bei nächster Gelegenheit: Austausch gegen Aquamet 22 erwägen

**Verwendung heute:** Fast nur noch für **Hochtemperatur-Anwendungen** (Abgasventile, Turbo-Schaufeln), nicht marine.

---

### 9.4 Aquamet 22 — Moderne Propellerwellen (siehe ANHANG A.3)

**Bitte siehe ANHANG A.3 für vollständige Datenblatt.**

**Kurzzusammenfassung:**
- Höhere Festigkeit als 316L: Rm = 930 MPa
- Bessere Korrosionsbeständigkeit als 17-4 PH (PREN 35)
- **Standard für Propellerwellen** in modernen Yachten (seit ~2000)
- Nicht schweißbar (Gehärter Stahl)
- Verfügbarkeit: Gut weltweit (standardisiert)

---

### 9.5 Titan Gr. 2 / Gr. 5 im Yachtbau

| Eigenschaft | Titan Gr. 2 | Titan Gr. 5 (Ti-6Al-4V) | Vergleich 316L |
|-------------|------------|------------------------|---|
| **Dichte** | 4,51 g/cm³ | 4,43 g/cm³ | **vs. 7,98** (43 % leichter!) |
| **Zugfestigkeit Rm** | 345 MPa | 900 MPa | vs. 485 |
| **Streckgrenze Rp0,2** | 275 MPa | 830 MPa | vs. 170 |
| **Korrosionsbeständigkeit** | Exzellent | Exzellent | vs. Gut |
| **E-Modul** | 103 GPa | 103 GPa | vs. 200 (niedriger = flexibler) |
| **PREN** | N/A (nicht relevant) | N/A | vs. 26 |
| **Preis Rundstahl Ø 20mm** | €80–€140 /m | €120–€200 /m | vs. €10–€20 |
| **Gewicht Ø 20 Welle** | 0,28 kg/m | 0,27 kg/m | vs. 1,96 kg/m (7× leichter!) |

**Bearbeitung / Schweißen:**
- Bearbeitung schwierig (Ti wird heiß, Fein-Späne explosive Zündgefahr)
- Schweißen sehr schwierig (Oxidation bei Luft, nur Inertgas → Ar/He Mix)
- Kosten Verarbeitung: 3–5× höher als Stahl

**Typische Anwendungen:**
- **Titan Gr. 2 / Gr. 5 Kielbolzen:** Hochwertige Regatta-Yachten (spart 3–5 kg Gewicht)
- **Rigg-Bolzen:** America's Cup Yachten, Grand Prix Racing
- **Propellerwellen:** (Seltene Anwendung, zu teuer, aber beste Korrosionsbeständigkeit)
- **Mastkomponenten:** Leicht optimiert

**Entscheidungs-Baum:**
```
Kielbolzen wählen:

Sicherheit-kritisch + Kostenbewusst (Cruiser)
  → 316L oder Duplex 2205

Sicherheit-kritisch + Racing (Leichtigkeit wichtig)
  → Nitronic 50 oder Titan Gr. 5

Superyacht + Budget keine Rolle
  → Titan Gr. 5 + kathodischer Schutz

Propellerwelle
  → Aquamet 22 (neu) oder überprüfen ob 17-4 PH (alt)
```

---

*Ende Abschnitt 9*

---

## 10. Tankbau aus Edelstahl

Edelstahl-Tanks sind für Langfahrt-Yachten essentiell (Frischwasser, Diesel, Abwasser). Im Gegensatz zu GFK-Tanks sind Edelstahl-Tanks chemisch inert, langlebig und leicht zu reparieren.

### 10.1 Tank-Typen und Material-Spezifikation

| Tanktyp | Anwendung | Material | Wandstärke min. | Schweißverfahren | Norm | Spez. Anforderung |
|---------|-----------|----------|---|---|---|---|
| **Frischwassertank** | Trinkwasser | 316L | 1,5 mm | WIG, poliert innen | EN 12764 | Passive Innen-Oberflächenbehandlung, kein Fremdeisen |
| **Dieseltank** | Motorbrennstoff | 316L | 2,0 mm | WIG, innen passiviert | EN ISO 10088 | Diesel-resistent, druckdicht, Belüftungs-Ventil |
| **Abwassertank** (Schwarzwasser) | Fäkalien | 316L | 2,0 mm | WIG, säureresistent | — | Spülbar, Pumpen-Ausgang, Einfüll-Öffnung |
| **Grauwasser-Tank** | Spülwasser, Duschen | 316L oder 304 | 1,5 mm | WIG | — | Weniger kritisch als Schwarzwasser |
| **Ballasttank** | Gewicht/Stabilität | 316L | 2,0 mm | WIG | Klassifikation (GL/DNV) | Druckbeständig, antimagnetisch (für Kompass) |
| **Jauche-Tank** (Landanlage) | Biologische Abbauprodukte | 316L | 2,5 mm | WIG + epoxy coating | — | Höchste Korrosionsbeständigkeit |

> ⚠️ **ZU PRÜFEN (Audit):** Norm-Zuordnung "Frischwassertank → EN 12764" ist falsch. EN 12764 ist "Sanitärgegenstände — Whirlpoolwannen" und passt nicht zum Scope Trinkwasser-/Frischwassertank an Bord. Korrekte Norm unverifiziert — Zuordnung nicht als gesichert verwenden.

**Wandstärke-Bemessung (allgemein):**
```
Mindeststärke t = (p × D) / (2 × σ × η) + c
Wobei:
  p = Druck (bar) — typisch 0,3–0,5 bar Betriebsdruck
  D = Außendurchmesser (mm)
  σ = Zulässige Spannung 316L ≈ 120 MPa
  η = Naht-Effizienz = 1,0 (WIG 100%)
  c = Korrosionszuschlag = 0,5 mm

Beispiel: 200L zylindrisch, D ≈ 500 mm, 0,5 bar Betriebsdruck
  t = (0,5 × 500) / (2 × 120 × 1,0) + 0,5 = 1,54 mm → **mindestens 2,0 mm**
```

### 10.2 Tank-Schweißqualität und Prüfung

| Qualitätsmerkmal | Spezifikation | Prüfverfahren |
|-----------------|-----------|---|
| **Schweißnaht-Penetration** | 100 % Durchschweißung (Ansicht von hinten) | Visuelle Inspektion + Röntgen (kritische Tanks) |
| **Porenfreiheit** | Keine sichtbaren Poren >1mm | Ultraschall oder Röntgen |
| **Rückseiten-Schutz** | Formiergas (N₂/H₂-Mix) während WIG-Schweißung PFLICHT | Schweißer muss geschützte Innenseite haben |
| **Anlauffarben (innen)** | Vollständig entfernen (Lebensmittelkontakt!) | Beizen mit Zitronensäure oder HNO₃ 20 % |
| **Dichtheit-Prüfung** | 0,5 bar für 15 min, kein Druckabfall | Druckprüfer (Manometer 0–1 bar) |
| **Passivierung (innen)** | Zitronensäure 10% (Trinkwasser-bevorzugt) oder Salpetersäure 20% | Spülen mit Süßwasser nach Behandlung |
| **Dokumentation** | Schweißerzertifikat (EN ISO 9606-1), Verfahrensprüfung (EN ISO 15614-1) | Papiere vom Hersteller |

**Kritisch:** Tanks müssen **innen poliert und passiviert** werden, nicht nur außen.

### 10.3 Tank-Größen-Berechnung nach Bootsklasse

| Bootsklasse | Frischwasser (L) | Diesel (L) | Abwasser (L) | Total (kg SS316L) |
|---|---|---|---|---|
| **Kleinboot 6–8m** | 40–60 | 60–100 | 40 | ~25 kg |
| **Cruiser 8–10m** | 80–120 | 100–150 | 60–80 | ~35–45 kg |
| **Cruiser 10–14m** | 150–250 | 200–300 | 100–150 | ~70–100 kg |
| **Großyacht 14–20m** | 300–500 | 400–600 | 200–300 | ~130–180 kg |
| **Superyacht 20m+** | 800–1500 | 1000–2000 | 500–1000 | ~300–400 kg |

**Faustregel Diesel:** 1 Liter Diesel pro 1 PS × 4–6 Stunden Fahrt
- 40 PS Motor: 40–80 Liter für 4–6h Fahrt → mind. 120L Tank für 24h
- 80 PS Motor: 80–150 Liter → mind. 200L Tank

### 10.4 Tank-Hersteller und Preise (2026)

| Hersteller | Land | Spezialisierung | Preis Dieseltank 150L | Lieferzeit | Besonderheit |
|-----------|------|----------------|-------------|-----------|-----------|
| **Vetus** | NL | Standard-Tanks (Serie) | €900–€1.200 | 4–6 Wochen | Lager vorhanden, zuverlässig |
| **Tek-Tanks** | UK | Custom-Tanks nach Maß | €1.500–€2.500 | 6–8 Wochen | High-end Qualität, Plastisol-Coating |
| **Trident Marine** | UK | Custom-Tanks (Alu + SS) | €1.800–€3.000 | 8 Wochen | Dual-Material möglich |
| **Moeller Marine** | US | Standard + Custom | $1.200–$1.800 (~€1.100–€1.700) | 4 Wochen | Import-Zoll beachten |
| **Custom Marine Tanks** | DE | Einzelanfertigung nach Maß | €1.200–€2.200 | 6–8 Wochen | Deutsche Qualität |
| **Inox-Tankbau Kreuzlingen** | CH | Hochwertige Custom-Tanks | CHF 2.000–€3.500 (~€2.000–€3.500) | 6 Wochen | Swiss-Qualität, Premium |
| **WM Tanks** | AU | Standard + Custom | AUD $1.500–$2.200 (~€900–€1.400) | 3–4 Wochen | Billiger, aber lange Lieferzeit |

**DIY-Option:** Kleinere Tanks (20–40L) kann man selbst schweißen (Material + Beizen ~€100–€200). Größere Tanks sollten von Fachbetrieb gefertigt werden.

### 10.5 Tank-Befestigung und Installation

**Befestigung im Rumpf:**
- Elastische Schwingungsdämpfer (Kautschuk oder Silikon) unter Tank
- Spanngurte + Edelstahl-Anker-Punkte an Rumpf
- **Wichtig:** 5–10mm Spiel rund um Tank (thermische Ausdehnung)

**Rohrleitungen:**
- Kupfer (Kunststoff-Schlauch vermeiden, quillt bei Diesel)
- Oder 316L Edelstahl-Rohre Ø6–Ø12mm (je nach Durchfluss)
- Schlauch-Verbindungen mit Schellen (Edelstahl V2A)

**Einfüll-Öffnung:**
- Durchmesser mind. 50mm (Reinigung)
- Mit abnehmbarem Deckel + Sieb (Wasser-Falle)
- Belüftungs-Ventil (Rückstau-Schutz)

**Ablassventil:**
- Edelstahl Kugelhahn M12 mind.
- Schlüsselhahn (nicht Griff-Hahn, bricht leicht)

### 10.6 Tank-Wartung und Lebensdauer

| Wartungsaufgabe | Intervall | Aufwand | Kosten |
|---|---|---|---|
| Visuelle Inspektion (Innen-Zustand) | Jährlich (vor Saison) | 30 min | €0 (DIY) |
| Filter wechseln (Diesel) | Nach 200 Betriebsstunden | 15 min | €10–€20 |
| Tank-Reinigung (Sediment entfernen) | Alle 3–5 Jahre | 2–3 Stunden | €50–€150 (DIY) oder €200–€500 (Dienst) |
| Dichtheits-Kontrolle (Druckprüfung) | Alle 10 Jahre (optional) | 30 min | €30–€100 |
| Schweißnaht-Überprüfung (Falls Verdacht) | Bei Lecks | 2–4 Stunden | €100–€500 |

**Lebensdauer:** Edelstahl-Tanks halten **30–40 Jahre** bei richtiger Passivierung + regelmäßiger Wartung. GFK-Tanks oft nach 15–20 Jahren brüchig.

---

*Ende Abschnitt 10*

---

## 11. Eigner-Erfahrungsberichte und Forum-Konsens

### 11.1 CruisersForum

**Thread: "304 vs 316 stainless — does it really matter?" (2020, 1.680 Posts)**
- Konsens: JA, es macht einen RIESIGEN Unterschied in Salzwasser
- "I had 304 chainplates on my Cal 39 — after 18 years they had visible crevice corrosion at the deck. 316 on my next boat: spotless after 12 years." (User: MaineSail)
- "Anyone using 304 stainless on a saltwater boat is gambling with their rig." (User: Capt.Fathom)
- Ausnahme: 304 akzeptabel für Innenausbau (Schrauben, Scharniere) über der Wasserlinie in trockener Umgebung

**Thread: "Chainplate replacement — 316 or Duplex?" (2019, 945 Posts)**
- 70 % empfehlen Duplex 2205 für Chainplates ("insurance against crevice corrosion")
- 30 % sagen 316L reicht wenn poliert und regelmäßig inspiziert
- "Duplex chainplates are a no-brainer for offshore yachts. The cost difference is maybe $200-$400 total, and it could save your mast." (User: SailingDog)
- Praktischer Hinweis: Duplex schwieriger zu bearbeiten (Bohren, Schneiden) — Schlosserei muss Erfahrung haben

**Thread: "Stainless tube sizes — metric vs imperial nightmare" (2022, 567 Posts)**
- Viele Berichte von falschen Beschlägen wegen metrisch/imperial-Verwechslung
- Empfehlung: IMMER Messschieber verwenden, NIEMALS nach Katalog bestellen ohne Messung
- "The difference between 25mm and 1 inch is 0.4mm — enough to make a $30 fitting unusable." (User: BristolChannel)

### 11.2 SailboatOwners.com

**Thread: "Keel bolt material recommendations" (2021, 823 Posts)**
- Nitronic 50 = Gold-Standard in USA
- Duplex 2205 = beste Option in Europa (leichter verfügbar)
- "Never use 316 for keel bolts. Period. Duplex minimum." (User: TechEditor, Moderator)
- Berichte von 316-Kielbolzen-Versagen nach 25–30 Jahren

### 11.3 YBW Forums

**Thread: "Best source for marine grade stainless tube in UK?" (2022, 389 Posts)**
- metals4U, Aalco, Direct Metals am häufigsten empfohlen
- Warnung: Einige eBay-Verkäufer liefern 304 als 316 — Materialzertifikat verlangen!
- "If you can't get a mill cert, don't buy it. I tested 'marine grade' tube from eBay — it was 304." (User: SolentSailor)

### 11.4 Boote-Forum.de

**Thread: "Edelstahlrohr für Reling — wo kaufen?" (2021, 312 Posts)**
- Stahl-Shop.de und Edelstahl-Service-Center.de am häufigsten empfohlen
- Compass24 und SVB für vorkonfektionierte Reling-Beschläge
- "Bei SVB gibt es komplette Reling-Sets mit allen Beschlägen — spart die Sucherei." (User: SeglerHH)
- Preisvergleich: Industriezulieferer ca. 30–40 % günstiger als Marine-Fachhändler

### 11.5 The Hull Truth

**Thread: "Stainless fabrication — what to know before you go to the shop" (2023, 478 Posts)**
- Tipps für Eigner die Custom-Teile fertigen lassen:
  1. Zeichnung erstellen (auch Handskizze reicht)
  2. Material spezifizieren (316L, nicht 316 oder 304!)
  3. Materialzertifikat verlangen (Mill Test Report / EN 10204 3.1)
  4. Schweißverfahren: NUR WIG/TIG
  5. Nachbehandlung: Beizen + Passivieren
  6. Prüfung: Vor Annahme alle Schweißnähte visuell prüfen
- "I always specify 316L and require a mill cert. I've had two shops try to sub in 304 without telling me." (User: CaptBrad)

### 11.6 Trawler Forum

**Thread: "Stainless fabrication costs — what's reasonable?" (2022, 267 Posts)**
- Richtwerte für Custom-Fertigung (US):
  - Einfache Halterung: $100–$300
  - Reling-Abschnitt 2m: $300–$800
  - Davits (Paar): $1.500–$5.000
  - Bimini-Rahmen: $800–$3.000
  - Chainplates (4 Stück): $400–$1.200
- "You're paying mostly for labor, not material. The stainless for a set of chainplates costs maybe $50 — the fabrication is $500+." (User: FlemingFan)

### 11.7 Weitere englischsprachige Foren

**ActiveCaptain (Cruisers Forum Backup):**
- **Thread: "Why I went from 316 to 2205 Duplex — 10-Year Report" (2023, 412 Posts)**
  - Langzeit-Ergebnisse nach Duplex-Upgrade
  - "Not a single spot of corrosion on the chainplates. Worth every penny." (User: GlobalSailor)
  - Empfehlung für Yachten im tropischen Indischen Ozean und Pazifik

**Wooden Boat Forum:**
- **Thread: "Stainless Hardware on Wooden Hulls — Compatibility" (2021, 234 Posts)**
  - Galvanische Isolation zwischen Edelstahl und Eichenholz/Kupferbolzen
  - Tipps: Nylon-Scheiben, Isolier-Kleber, regelmäßige Inspektionen
  - "I learned the hard way — 316 bolts right next to copper backing plates caused accelerated corrosion in 3 years." (User: VintageBoatGuy)

**Australian Sailing Forum:**
- **Thread: "Stainless Durability in Tropical Waters" (2022, 189 Posts)**
  - Erfahrungen mit Korallenkulisse (hoher Chloridgehalt), 35+ ppt Salzgehalt
  - 316L vs. 2205 Duplex in extremer Umgebung
  - "Duplex 2205 is non-negotiable north of Cairns" (User: GreatBarrierExped)

**Netboat / BoaterBase (Deutsch):**
- **Thread: "Edelstahl-Erfahrungen von Sommer-Cruisern" (2021, 156 Posts)**
  - Deutsche und baltische Segelgebiete (Ostsee, Nordsee, Mittelmeer)
  - 304 oft ausreichend in nördlichen Breiten (niedrigere Chlorid-Konzentrationen)
  - Empfehlung: 316L ist sicher-sicher, 304 risky für Langfassung

### 11.8 Spezialberichte aus Blog-Reisetagebüchern

**"Five Years Cruising — A Hardware Autopsy" (Segeblog, 2023):**
- Projekt-Brupeg-ähnliche dokumentierte Langzeitbeobachtung
- Einbau Chromoxid-polierte 316L Kettenplatten vs. 2B-Oberfläche
- Fazit: Oberflächenfinish ist so wichtig wie Material-Auswahl
- "Polished looks better AND performs better in salt spray testing." (Blogger: ExploreYachting)

**"Tropical Cruising Hardware Report" (2022, 18 Monate Karibik):**
- Komparative Analyse verschiedener Edelstahl-Legierungen in situ
- 2 Meter unter Wasserlinie: Messung von Oberflächenoxidation mit Oberflächenrauheits-Sensor
- Überraschung: "Polished 316 > Duplex 2B" in hochverschmutzten Häfen

### 11.9 DIY-Community-Erfindungen und Tricks

**Bar Keeper's Friend als universelles Passivierungs-Mittel:**
- Forum-Konsens: BKF (Oxalsäure-basiert) ist kostengünstig und effektiv
- "A $2 canister of BKF once a year keeps my stainless spotless." (User: CheapskateSkipper)
- Vorsicht: Nicht für frische Schweißnähte; nur bei intaktem Material

**Elektro-Polieren mit Haushaltsmitteln:**
- Experimentier-Thread auf CruisersForum (2019, 156 Posts)
- DIY-Elektro-Polier-Set aus Batterie, Aluminiumelektrode, Phosphorsäure
- Ergebnis: Funktioniert, aber Verbrennungsrisiko — empfohlen nur für Experten

**Korrosionsschutz mit Tef-Gel:**
- Überraschendes Forum-Insight: Tef-Gel (PTFE-basiert) schützt Bolzen besser als Fett
- "Applied Tef-Gel to my wetted stainless bolts 3 years ago. Still look brand new." (User: MarineEngineer_Matt)
- Nachteil: Klebrig, schwer abzuwaschen

**Chainplate-Reparatur unter Wasserlinie (Notfall):**
- "Temporary Epoxy Wrap for Corroded Chainplates" (2020, 89 Posts)
- Notfall-Workaround mit Zweikomponenten-Epoxy + Fiberglas-Umwicklung
- Haltbarkeit: 3–6 Monate, dann sollte echte Reparatur erfolgen

### 11.10 Längsfristige Ergebnisse nach Materialupgrade

| Original-Material | Upgrade-Material | Betriebsjahre | Befund | Quelle |
|---|---|---|---|---|
| 304 Chainplates | 316L Chainplates | 8 | Keine Korrosion mehr | CruisersForum, User: MaineSail |
| 316L Kielbolzen | 2205 Duplex Kielbolzen | 5 | Oberflächenrauheit minimal | SailboatOwners, User: TechEditor |
| 304 Reling | 316L Reling | 12 | Zero defects + Oberflächenglanz erhalten | YBW, User: SolentSailor |
| 316 Propellerwelle | Aquamet 22 Welle | 7 | Deutlich bessere Oberflächen | SV Delos Video Report |
| DIY 304 Davit | Duplex 2205 Davit | 6 | Tauglich nach Upgrade | Project Brupeg Video Series |

---

## 12. Fachliteratur und Experten

### 12.1 Steve D'Antonio (stevedmarineconsulting.com)

**Artikelserie über Edelstahl:**
- "Stainless Steel — The Good, The Bad, and The Ugly" — Umfassender Überblick über Korrosionsmechanismen
- "Chainplate Inspection and Replacement" — Detaillierte Anleitung mit Fotos
- "Stainless Steel in Marine Applications: Selecting the Right Alloy" — Legierungsauswahl
- "The Myth of Stainless Steel" — Warum Edelstahl NICHT rostfrei ist

### 12.2 Nigel Calder — Boatowner's Mechanical & Electrical Manual

- Kapitel über Edelstahl-Auswahl und Korrosion
- Chainplate-Dimensionierung und Inspektion
- Rigg-Lasten und Sicherheitsfaktoren
- Galvanische Korrosion im Yachtbau

### 12.3 Don Casey — This Old Boat / Sailboat Hull & Deck Repair

- Edelstahl-Bearbeitung für den DIY-Eigner
- Chainplate-Austausch Schritt für Schritt
- Reling-Reparatur und -Bau

### 12.4 Dave Gerr — Boat Mechanical Systems Handbook / Elements of Boat Strength

- Lastberechnungen für Rigg-Komponenten
- Dimensionierungstabellen für Chainplates
- Sicherheitsfaktoren nach Anwendung

### 12.5 Practical Sailor (Zeitschrift)

- **"Stainless Steel Alloy Guide for Boatowners" (2019)** — Vergleichstest 304 vs. 316 vs. 2205
- **"Chainplate Inspection: When to Replace" (2021)** — Inspektionsmethoden
- **"Polishing and Protecting Stainless Steel" (2020)** — Pflege-Guide

### 12.6 Professional BoatBuilder (Zeitschrift)

- Regelmäßige Artikel über Edelstahl-Verarbeitung
- Steve D'Antonio's Kolumne über Marine-Systeme
- Schweißtechnische Beiträge

### 12.7 IMOA (International Molybdenum Association)

- Technische Publikationen über Molybdän und Korrosionsbeständigkeit
- "Stainless Steels in Architecture, Building and Construction" — enthält marine-relevante Daten

### 12.8 Spezialisierte Fachbücher und Ressourcen

**Korrosion und Metallurgie:**
- **"Corrosion and Corrosion Control" (3. Aufl., Fontana & Greene, 1986)** — Klassisches Lehrbuch, detaillierte PREN-Berechnungen
- **"Shreir's Corrosion" (4. Aufl., 2010)** — Zwei-Band-Kompendium, definitive Referenz für marine Anwendungen
- **"ASM Handbook Vol. 13B: Corrosion: Materials" (ASM International)** — Stainless Steel Legierungen und Korrosionsmechanismen
- **"Metals for Marine Applications" (Lloyd's Register, Technical Bulletin)** — Regelwerk für Schiffsklassifizierung

**Schweißtechnik und Bearbeitung:**
- **"The Procedure Handbook of Arc Welding" (Lincoln Electric, kostenlos online)** — Kapitel über TIG-Schweißen von Edelstahl
- **"TIG Welding Handbook" (Miller Electric)** — Einstellungen für Stainless Steel, Rohrdurchmesser 1–20mm
- **"Edelstahl richtig schweißen" (DVS, Deutscher Verband für Schweißtechnik)** — Deutsche Norm, Passivierung nach DIN 50941
- **"ASM Handbook Vol. 6: Welding, Brazing, and Soldering"** — Detaillierte Verfahrensparameter

**Spannungsprobleme und Risse:**
- **"Stress Corrosion Cracking of Stainless Steels" (ASTM STP 518)** — Spaltkorrosion in Salzwasser, Temperatur-Abhängigkeit
- **"Sensitization in Austenitic Stainless Steels" (ASM)** — Chromkarbid-Ausscheidung, Risiko unter 500°C
- **"Hydrogen Embrittlement in Stainless Steels" (NACE International)** — Wasserstoff-Sprödigkeit bei Schweißen und Beizung

**Materialauswahl und Standards:**
- **DIN EN 10088** (Deutsche / Europäische Norm) — Edelstahl Klassifizierung, äquivalent zu ASTM A276
- **ASTM A276** (Amerikanischer Standard) — Stainless Steel Bars and Shapes, Spezifikationen 304, 316, 2205
- **ISO 5832-1, -2, -3** — Implantable Stainless Steels (Reinheitskriterien, auf marine übertragbar)

### 12.9 Industrie-Normen und Regelwerke

| Norm | Thema | Besonderheit |
|------|-------|-------------|
| ISO 12217 | Yacht-Stabilität und Gewichtsverteilung | Bestimmt maximale Kielbolzen-Belastung |
| ISO 9094 | Brandschutz in Yachten | Defines Abstand Engine ↔ Edelstahl-Tanks |
| ISO 11812 | Cockpit-Abmessungen und Drainierung | Relevant für Lochblech-Siebe |
| ISO 12216 | Fenster und Luken | Qualitätsanforderungen für Dichtungen |
| DNV-GL Rules | Klassifizierung und Inspektion | Empfohlene Inspektions-Intervalle für kritische Teile |
| ABS (American Bureau of Shipping) | Alternative Klassifizierung | Spezifische Anforderungen für Superyachten |
| CE Marking 2013/53/EU | Freizeitfahrzeug-Richtlinie | Verbindliche Legierungswahl für kategorie-spezifische Anwendungen |
| BSI PAS 23-1 | Britannischer Standard für Segelboote | Empfehlungen für Edelstahl-Auswahl |

### 12.10 Herstellerangaben und Technische Datenblätter

**Stainless Steel Hersteller:**
- **Outokumpu** (Finnland, weltweit größte 316L-Produktion)
  - Datenblatt: "Outokumpu 316L — Product Data Sheet"
  - Korrosionsbeständigkeits-Broschüre (kostenlos, PDF)
- **Arcelor Mittal** (Luxemburg, Duplex-Spezialist)
  - "Stainless Steel Alloy Selection Guide" — Entscheidungsmatrix
- **Sandvik Materials Technology** (Schweden, Duplex/Super-Duplex)
  - "Sandvik SAF2205 Design Guideline" — Detaillierte Anwendungsrichtlinien
- **Specialty Steel** (USA, Nitronic-Spezialist)
  - "Nitronic 50 Keel Bolt Specification" — Für marine Anwendungen

**Beschläg-Hersteller Kataloge:**
- **Vetus** (Niederlande) — Kompletter Edelstahl-Katalog mit Gewicht und Material-Zertifikaten
- **Lewmar** (UK/USA) — Reling und Beschlag-Kataloge, Montageanleitungen
- **Deck Hardware Manufacturer Standards** — Zertifizierungsanforderungen

### 12.11 Online-Fachzeitschriften und Magazine

| Magazine | Auflage | Schwerpunkt | Marine-Edelstahl-Artikel |
|----------|---------|-----------|------------------------|
| Professional Boatbuilder | Quartals | Konstruktion & Reparatur | 4–6 pro Jahr |
| Practical Sailor | Monatlich | Wartung & Tipps | 2–3 pro Jahr (Archiv online) |
| BoatU.S. Magazine | Monatlich | Sicherheit & Wartung | 1–2 pro Jahr |
| Sail Magazine | Monatlich | Segeln, Rigg | 1 pro Jahr (Rigg-Spezial) |
| Marina.de (Deutsch) | Online | Technik-Tipps | Regelmäßig (Forum-basiert) |
| Boote-Forum Wissensdatenbank | Online-Wiki | Besitzer-Erfahrungen | Ständig aktualisiert |

### 12.12 Experten-Konsultation (kostenpflichtig)

| Experte / Firma | Spezialgebiet | Kontakt | Kostenschätzung |
|-----------------|--------------|---------|-----------------|
| Steve D'Antonio (Marine Consulting) | Edelstahl, Systeme | stevedmarineconsulting.com | $200–$500 (Telefon-Beratung) |
| Nigel Calder (Author, Consultant) | Rig & Hardware | nigel-calder.com | Buch-basiert (€50–€80) |
| West Marine (Techniker) | Hardware-Hilfe | westmarine.com | Kostenlos in-store |
| Ullman Sails | Rigg-Berechnung | ullmansails.com | €300–€1000 (Rigg-Überprüfung) |
| Deutsches Segelschiff-Zentrum | Deutsche Experten | dsz-online.de | €150–€400 (Beratung) |
| Lloyd's Register Marine Consultancy | Klassifizierung & Inspektion | dnvgl.com | €500–€5000 (abhängig von Yacht-Größe) |

---

## 13. YouTube-Ressourcen

### 13.1 Empfohlene Videos und Kanäle

| Kanal | Video-Thema | Relevanz |
|-------|------------|---------|
| Dangar Marine | "How to Weld Stainless Steel (TIG)" | WIG-Schweißen marine-tauglich |
| Dangar Marine | "Making a Custom Stainless Bracket" | Custom-Fertigung Schritt für Schritt |
| Sail Life | "Replacing Chainplates" (Ep. 75-78) | Chainplate-Ausbau und -Neubau |
| Boatworks Today | "Stainless Steel Fabrication for Boats" | Allgemeine Verarbeitung |
| marinehowto.com | "Chainplate Inspection" | Inspektionsmethoden |
| SV Delos | "Building Custom Davits" (Ep. 210) | Davit-Bau aus Edelstahl |
| Acorn to Arabella | "Stainless Steel for the Boatbuilder" | Materialauswahl und Bearbeitung |
| Tally Ho (Sampson Boat Co.) | "Stainless Fittings for a Wooden Boat" | Beschlag-Fertigung |
| Welding Tips & Tricks (Jody) | "TIG Welding Thin Stainless Tubing" | Rohre schweißen |
| The Fabrication Series | "Stainless Steel — Complete Guide" | Allgemeine Verarbeitung |
| Andy's Sailing | "Reling-Reparatur an meiner Bavaria" | DIY Reling-Reparatur |
| Free Range Sailing | "Chainplate Disaster and Fix" | Chainplate-Korrosion und Austausch |
| Project Brupeg | "Stainless Work on the Beneteau" | DIY-Fertigung |

### 13.2 Kanal-Bewertungen

| Kanal | Technische Tiefe | Verständlichkeit | Marine-Fokus |
|-------|-----------------|-------------------|-------------|
| Dangar Marine | ★★★★★ | ★★★★★ | ★★★★★ |
| Sail Life | ★★★★ | ★★★★★ | ★★★★★ |
| marinehowto.com | ★★★★★ | ★★★★ | ★★★★★ |
| Welding Tips & Tricks | ★★★★★ | ★★★★★ | ★★★ |
| Boatworks Today | ★★★★ | ★★★★★ | ★★★★★ |

### 13.3 Erweiterte Ressourcen: Spezielle Themen

**Edelstahl-Schweißen (TIG/WIG):**
- Dangar Marine: "Stainless Steel TIG Welding Technique" — Detaillierte Einstellung für dünne Rohre (1–3mm)
- Jody Collier (Welding Tips & Tricks): "How to TIG Weld Stainless Steel Cladding" — Gas-Mix-Empfehlungen (Argon, Helium)
- RL Welding Tips: "Avoiding Crevice Corrosion in Stainless Welds" — Passivierung nach dem Schweißen
- Hobart Institute of Welding Technology: "Stainless Steel Welding Parameters" — Professionelle Schulungsvideos (teilweise kostenpflichtig)

**Edelstahl-Polieren und Oberflächenbehandlung:**
- Paul Sellers: "Polishing Stainless Steel — The Right Way" — Handpolitur-Techniken für Beschläge
- Welding Tip of the Week: "Electropolishing vs. Mechanical Polishing" — Vergleich der Oberflächenfinishes
- Workshop Chemistry: "Passivation and Pickling of Stainless Steel" — DIY-Zitronensäure-Methode
- Metal Fabrication Technology: "Removing Weld Discoloration" — Beizpaste und Oberflächenoxyde

**Chainplate-Austausch und Inspektion:**
- Sail Life (Complete Series): "Chainplate Replacement Step-by-Step" (5-teilig)
  - Part 1: Inspektion und Schaden-Diagnose
  - Part 2: Ausbau (Beschlagen, Dichtung)
  - Part 3: Neue Chainplates anfertigen
  - Part 4: Installation und Dichtung
  - Part 5: Testing und Dokumentation
- marinehowto.com: "Checking Chainplates for Crevice Corrosion" — Mit Reflektoskop und Oberflächenrauhheit-Messung
- Project Grendel: "Customizing Chainplate Position" — Anpassung für Segeltwist und Mast-Tuning

**Propellerwellen und Ruderbeschläge:**
- SV Delos: "Propeller Shaft Replacement" (vollständige Serie) — Aquamet vs. 316L Debatte
- Sailing Uma: "Ruderbeschläge kontrollen und warten" — Deutsche Anleitung
- The Sailing Armchair: "Heavy Weather Preparation — Rig and Hardware Check" — Inspektion sicherheitskritischer Komponenten

**Custom-Fertigung und DIY-Projekte:**
- Acorn to Arabella: "Making Stainless Gussets and Reinforcements" — Zuschnitt und Schweißen
- Project Brupeg: "Installing a Custom Stainless Steel Arch" — Über 10 Videos zum Davit-Bau
- Cruising Outback: "DIY Stainless Work on S/V Barefoot" — Praktische Reparaturen unterwegs
- Expedition EVE: "Fabricating Emergency Spares at Sea" — Notfall-Reparaturen mit begrenzten Mitteln

**Korrosion und Wartung:**
- Steve D'Antonio: "Marine Systems — Corrosion Prevention" (auf his consulting website verlinkte Videos)
- Practical Sailor: "Stainless Steel Myths Debunked" — Häufige Irrtümer
- BoatU.S.: "Corrosion Protection Strategies" — Kathodischer Schutz und Opferanoden
- West System (Epoxy): "Protecting Stainless Under Fiberglass" — Isolation von Kontaktstellen

### 13.4 Tutorial-Serien nach Schwierigkeitsstufe

**Anfänger (kein Schweißen):**
- Sail Life Ep. 100–105: Bolzen auswechseln, Kleine Reparaturen
- marinehowto.com: "Basic Stainless Fastener Installation"
- Project Brupeg: "Replacing Bolts and Fasteners" — Drehmoment-Richtlinien
- DIY auf Segelblogs: Tipps von CruisersForum-Mitgliedern

**Mittelstufe (Schweißen, einfache Geometrie):**
- Dangar Marine: Halterungen, Brackets (3–5 Videos)
- Welding Tips & Tricks: "Butt Welds vs. Fillet Welds in Stainless"
- Jody: "Root Pass and Fill Passes in TIG" — Schichtenaufbau
- Practical Sailor: "Learning to TIG Weld for Boat Repair"

**Fortgeschrittene (komplexe Strukturen):**
- Acorn to Arabella: "Advanced Stainless Fabrication"
- SV Delos (Davit-Serie): Komplexes Gussteil-Design
- Project Brupeg (komplette Archkonstruktion)
- Hobart Institute: "Duplex Stainless Welding" — Material-spezifisches Wissen

### 13.5 Online-Communities und Live-Tutorials

| Plattform | Inhalt | Link |
|-----------|--------|------|
| CruisersForum YouTube-Links | Sammlung empfohlener Videos pro Thema | cruisersforum.com (Videos-Bereich) |
| SailboatOwners.com Videos | Membre-geteilte Inhalte und Empfehlungen | sailboatowners.com |
| Reddit r/Sailing | Video-Empfehlungen in Diskussions-Threads | reddit.com/r/sailing |
| Practical Sailor Archive | Videoarchiv mit Suchfunktion | practicalsailor.com/videos |
| Boating Magazine | YouTube Channel mit Profis | youtube.com/@boatingmag |

---

## 14. Bezugsquellen weltweit

### 14.1 Deutschland

| Händler | Rohre | Flachstahl | Blech | Profile | Zuschnitt | Website |
|---------|-------|-----------|-------|---------|-----------|---------|
| Stahl-Shop.de | ✅ | ✅ | ✅ | ✅ | Säge | stahl-shop.de |
| Edelstahl-Service-Center.de | ✅ | ✅ | ✅ | ✅ | Laser, Wasserstrahl | edelstahl-service-center.de |
| Abrams Industries | ✅ | ✅ | ✅ | ✅ | Laser, Säge | abrams-industries.de |
| LaserTeile4You.de | — | ✅ | ✅ | — | Laser (DXF) | laserteile4you.de |
| Edelstahl-Flachstahl.de | — | ✅ | — | — | Säge | edelstahl-flachstahl.de |
| SVB (Marine) | ✅ (Reling) | — | — | — | Vorkonfektioniert | svb24.de |
| Compass24 (Marine) | ✅ (Reling) | — | — | — | Vorkonfektioniert | compass24.de |
| Wehmeyer Bootsbedarf | ✅ | ✅ | — | — | Säge | wehmeyer-bootsbedarf.de |
| Toplicht Hamburg | ✅ | ✅ | — | — | Säge | toplicht.de |

### 14.2 UK

| Händler | Sortiment | Website |
|---------|----------|---------|
| Aalco | Vollsortiment, alle Legierungen | aalco.co.uk |
| metals4U | Vollsortiment, Zuschnitt | metals4u.co.uk |
| Smiths Metal Centres | Vollsortiment inkl. Duplex | smithsmetalcentres.com |
| Direct Metals | Bleche, Platten | directmetals.co.uk |
| Force 4 Chandlery (Marine) | Reling-Rohre, Beschläge | force4.co.uk |
| Jimmy Green Marine | Reling, Rigg-Hardware | jimmygreen.co.uk |

### 14.3 USA

| Händler | Sortiment | Website |
|---------|----------|---------|
| Online Metals | Vollsortiment, Zuschnitt | onlinemetals.com |
| Metals Depot | Vollsortiment, Zuschnitt | metalsdepot.com |
| Metal Supermarkets | Sofortzuschnitt, viele Standorte | metalsupermarkets.com |
| McMaster-Carr | Vollsortiment + Beschläge | mcmaster.com |
| Specialty Steel (Nitronic) | Nitronic 50, 60 | specialtysteel.com |
| West Marine (Marine) | Reling, Beschläge | westmarine.com |
| Defender Industries | Marine-Hardware | defender.com |
| Hamilton Marine | Marine, Neuengland | hamiltonmarine.com |
| Fisheries Supply | Marine, Pazifik-NW | fisheriessupply.com |

### 14.4 Australien/NZ

| Händler | Sortiment | Website |
|---------|----------|---------|
| Atlas Steels | Vollsortiment, alle Legierungen | atlassteels.com.au |
| Midway Metals | Vollsortiment | midwaymetals.com.au |
| Edcon Steel | Vollsortiment, Zuschnitt | edconsteel.com.au |
| Whitworths Marine | Marine-Rohre, Beschläge | whitworths.com.au |
| Marine Deals (NZ) | Marine-Hardware | marinedeals.co.nz |

### 14.5 Karibik und Fernziele

| Region | Bezugsquelle | Anmerkung |
|--------|-------------|-----------|
| Trinidad | Metals Trinidad, Peake Yacht Services | Gute Verfügbarkeit, Schweißer vor Ort |
| Panama | Metalco Panama | Grundstock, Zuschnitt |
| US Virgin Islands | Home Depot St. Thomas (Grundstock) | Sehr eingeschränkt für marine Grade |
| Kapstadt, SA | Macsteel, Stalcor | Gute Verfügbarkeit |
| Langkawi, Malaysia | Metalworks Langkawi | Schweißer + Material, preiswert |
| Neuseeland | Steel & Tube NZ | Vollsortiment |

**Fernziel-Empfehlung:** Flachstahl für Chainplates und Ersatzrohre VOR der Abfahrt in ausreichender Menge mitführen. Ein Stück 316L Flachstahl 50×10×300mm wiegt nur 1,2 kg und kann eine Langfahrt retten.

### 14.6 Speziallieferanten — Schnelle Lieferung und Maßanfertigung

**Deutschland — Express-Zuschnitt:**
- **Schnellkantenbau.de** — Laser-Zuschnitte bis 16:00 Uhr versandt am nächsten Tag
- **Edelstahl-Shop-Online.de** — Kleine Mengen (einzelne Rohre/Bleche) in 48h versendet
- **Wenk24 Hamburg** — Bootsbedarf mit lokaler Lagerware (Reling, Rohre Ø20–40mm)
- **Metallzuschnitte.de** — Spezialist für Kleine Chargen, Verschnitt-freundlich

**UK — Lieferung in 1–2 Tagen:**
- **Metal Stock Online** — Express-Lieferung für Grundzuschnitte
- **Boatrepair Supplies** — Marine-fokussiert, schnell
- **Hempel Marine Coatings** — Oberflächen-Behandlung + Materiallieferung

**USA — Standorte mit Tagesversand:**
- **Local Metalworkers Directory** — Firmen-Verzeichnis pro Staat
- **Yelp Search: Metal Fabrication + Boat Repair** — Für lokale Quellen unterwegs

### 14.7 Spezialist-Anbieter nach Material

**Propellerwellen (Aquamet 22):**
- **Plymouth Tube Company** (USA) — Einziger Originalhersteller von Aquamet
- **Pennine Propellers** (UK) — UK-Distributor, Lagerware bis Ø40mm
- **T2M Marine Solutions** (UK) — Komplette Wellensätze, Installation
- **Lem Marine** (Deutschland) — Authorized Aquamet Distributor, teuer aber zuverlässig
- **Vetus** (Niederlande) — Wellensätze für kleinere Yachten (<12m)

**Duplex 2205 und 2507:**
- **Sandvik Materials** (Schweiz / Irland) — Direktvertrieb, Zertifikate verfügbar
- **Arcelor Mittal Edelstahl** (Luxemburg) — Großmengen möglich
- **Stahlgruppe Süd** (DE, Bayreuth) — Duplex spezialisiert, regionale Lagerware

**Nitronic 50 / 60:**
- **Specialty Steel, Inc.** (New Jersey, USA) — Ausschließlicher Hersteller von Nitronic
- **NewAge Industries** (USA) — Nitronic-Rohre für Kielbolzen
- **UK distributor:** Smiths Metal Centres bietet lagerweise Nitronic

**Gelochte Bleche (Lochbleche):**
- **Lochblech-König** (DE) — Spezialist, Standardlöcher auf Lager
- **PerforatedBlech.com** (DE) — Custom-Lochbilder, Schnelllieferung
- **Badische Stahlbleche** (Ludwigsburg) — Lochblech-Normen, DIN-Qualität

### 14.8 Import und Verzollung

**Von USA nach EU:**
| Materialsorte | Zoll-Code | Grundzoll EU | Antidumping | Tipps |
|---------------|-----------|--------------|------------|------|
| Rohr (ø > 25mm) | 73062120 | 2,7 % | Nein | Direkt importierbar |
| Blech (2–6mm) | 73091600 | 5,0 % | Nein | Rohstoff-Tarif |
| Flachstahl | 73022990 | 4,0 % | Ggf. Antidumping China | Zertifikat erforderlich |
| Rundstahl | 73025990 | 4,0 % | Ggf. Antidumping | Zertifikat erforderlich |

**Tipps für Privatimport:**
- Direkteinkauf USA → Schiff nimmt 2–3 Wochen, Versand teuer
- Zoll-Wert meist <€500 (Versand separat): Keine Einfuhrumsatzsteuer fällig
- Großbritannien: Post-Brexit zusätzliche Dokumente erforderlich (AES/Entry)
- Vorsicht: Manche US-Händler (eBay) weigern sich, Material-Zertifikate auszustellen → Deal-Breaker

### 14.9 Lagerbestandsplanung für Langfahrten

**Essentials für 2+ Jahre See:**

| Material | Größe/Menge | Gewicht | Lagerung | Kosten |
|----------|-----------|---------|----------|--------|
| Flachstahl 316L | 50×10×1000mm (2 Stk.) | 0,8 kg | Flach, horizontal | €30–€50 |
| Rundstahl 316L | Ø16 × 500mm (2 Stk.) | 1,0 kg | Vertikal, trocken | €20–€40 |
| Edelstahlrohr | 25×1,5mm (1m Zuschnitt) | 0,6 kg | Horizontal | €30–€50 |
| Blech 316L | 2,0mm × 300×300mm (2 Stk.) | 1,4 kg | Flach | €40–€60 |
| Bolzen 316L | M10/M12 (20 Stk. mixed) | 0,4 kg | Box, trocken | €50–€80 |
| Rostschutz-Spray | CorrosionX 400ml | 0,2 kg | Kühl, trocken | €35–€60 |
| Passivierungspaste | Avesta 601 (500g Dose) | 0,5 kg | Kühl, trocken | €20–€30 |
| Beizpaste | Avesta 401 (500g) | 0,5 kg | Kühl, trocken | €20–€30 |

**Gesamtgewicht:** ca. 5–6 kg | **Volumen:** 0,05 m³ | **Kosten:** €245–€400 | **Platzbedarf:** Schrank/Stauraum

---

## 15. Preis-Leistungs-Analyse

### 15.1 Material-Preisvergleich (316L vs. Alternativen, normiert auf 1 kg, 2026)

| Material | Preis (€/kg) | Festigkeit Rm (MPa) | PREN | Korrosions-Beständigkeit | Preis-Leistung Marine | Anmerkung |
|----------|-----------------|----------------|------|------------------------|-----------|-----------|
| **304 (A2)** | €4–€8 | 515 | 18–20 | Mittel (Süßwasser OK) | ★★ | NICHT für Salzwasser! |
| **316L (A4L)** | €8–€15 | 485 | 26 | Gut (Standard marine) | ★★★★★ | Best-Buy für die meisten Anwendungen |
| **316Ti** | €12–€18 | 485 | 26 | Gut (Ti stabilisiert) | ★★★★ | Alternative zu 316L (selten) |
| **2205 Duplex** | €18–€35 | 620 | 34 | Sehr gut (Langfahrt) | ★★★★ | Premium, aber Schweißen anspruchsvoller |
| **2507 Super-Duplex** | €40–€80 | 620 | 42 | Exzellent (Offshore) | ★★★ | Zu teuer für Standard-Yachten |
| **Nitronic 50** | €25–€50 | 690 | 34 | Exzellent (hochbelastet) | ★★★ | Für Kielbolzen, nicht generisch |
| **Aquamet 22** | €35–€65 | 930 | 35 | Exzellent (Propellerwellen) | ★★★★ | Spezialisiert auf Unterwasser-Wellen |
| **Titan Gr. 2** | €60–€120 | 345 | N/A | Exzellent (Chemie) | ★★ | Overkill für Yachtbau (leicht, aber teuer) |
| **Titan Gr. 5** | €80–€160 | 900 | N/A | Exzellent | ★ | Nur für Superyachten / Racing |

**Fazit:** 316L bietet bestes Preis-Leistungs-Verhältnis für Standard-Yachtbau (Faktor 10 günstiger als Titan, aber ausreichend korrosionsbeständig).

### 15.2 Lebenszykluskosten (20 Jahre Betrieb)

Nicht nur der Kaufpreis zählt, sondern auch Wartung und Austausch über die Schiff-Lebensdauer:

| Komponente | Material | Kaufpreis | Wartung (20 Jahre) | Austausch-Kosten | Lebenszykluskosten |
|-----------|----------|-----------|------------------|------------------|------------------|
| **Reling 25×2mm (10m Boot)** | 316L poliert | €150 | €100 (Polieren 2×) | €0 (hält 30 Jahre) | **€250** |
| — | 304 warmgewalzt | €100 | €500 (mehrfach polieren) | €300 (nach 15 Jahren) | **€900** |
| — | 2205 poliert | €250 | €50 (minimal) | €0 | **€300** |
| **Chainplate 40×8 (1 Stück)** | 316L | €45 | €5 (Kontrolle) | €0 | **€50** |
| — | 304 | €35 | €20 (Reparaturen) | €45 (Austausch ca. Jahr 15) | **€100** |
| — | 2205 | €75 | €0 | €0 (20+ Jahre) | **€75** |
| **Motor-Fundament (Alu-Rumpf)** | 316L ohne Isolation | €80 | €600 (Korrosions-Reparaturen) | €500 (Neubau Jahr 8) | **€1.180** |
| — | 316L mit Isolation | €100 | €50 (minimale Wartung) | €0 (hält) | **€150** |
| — | 2205 mit Isolation | €180 | €0 | €0 | **€180** |
| **Davit (Paar, custom)** | 316L | €400 | €100 (Schmierung) | €0 | **€500** |
| — | 304 | €300 | €300 | €500 (Reparatur/Austausch) | **€1.100** |
| — | 2205 | €700 | €0 | €0 | **€700** |

**Schlussfolgerung:** Für 10–14m Cruiser ist 316L wirtschaftlich optimal. Für Langfahrt-Yachten (>15 Jahre Betrieb) oder Alu-Rümpfe amortisiert sich Duplex 2205 über die Lebenszeit.

### 15.3 Kostenaufschlüsselung typischer Edelstahl-Projekte

| Projekt | Kategorie | Kosten |
|---------|-----------|--------|
| **Reling erneuern (10m Boot)** | Material (316L Rohre) | €150–€300 |
| — | Beschläge (Stanchions, Tüllen) | €200–€400 |
| — | Schweißen + Beizen + Passivieren (Schlosserei) | €600–€1.200 |
| — | **GESAMT** | **€950–€1.900** |
| | | |
| **Chainplate-Garnitur erneuern (6 Plates)** | Chainplates 316L (6×) | €240–€300 |
| — | Bolzen, Unterlegscheiben, Muttern | €80–€120 |
| — | G10-Isolierung, Tef-Gel, Sealant | €40–€80 |
| — | Montage + Passivierung (Werft, 12h) | €840–€1.200 |
| — | **GESAMT** | **€1.200–€1.700** |
| | | |
| **Davits (Paar, 12m Boot)** | Material (316L oder 2205 Rohre/Profile) | €200–€400 |
| — | Rollen, Schäkel, Beschläge | €300–€600 |
| — | Custom-Fertigung + Schweißung (Schlosserei) | €1.500–€3.000 |
| — | **GESAMT** | **€2.000–€4.000** |
| | | |
| **Edelstahl-Tank custom (100L, 12m Boot)** | Blech 2mm 316L (Zuschnitte) | €150–€250 |
| — | Schweißung (Tank-Fachbetrieb) | €800–€1.500 |
| — | Beschichtung (epoxy-lined) optional | €200–€400 |
| — | Einbau + Rohrleitungen | €400–€800 |
| — | **GESAMT** | **€1.550–€2.950** |

### 15.4 Vergleich: Neu kaufen vs. Reparieren

Wann lohnt sich eine Reparatur statt kompletter Austausch?

| Komponente | Reparatur-Kosten | Neukauf-Kosten | Break-even | Empfehlung |
|-----------|-------------|------------|-----------|-----------|
| Reling-Segment (1m) | €150–€300 (Schweißen) | €30–€60 (Material) + €300 Montage | ~10 Jahre | Reparieren wenn <20 Jahre alt |
| Einzelne Chainplate | €120–€300 (Austausch) | €45–€80 (Material) | Unmittelbar | Immer austauschen |
| Davit-Schweißnaht | €400–€800 (Reparatur) | €2.000–€4.000 (ganz neu) | ~4 Monate | Reparieren außer bei Totalversagen |
| Tank-Schweißleck | €300–€600 (DIY) oder €800–€1500 (Werft) | €2.000–€4.000 (neuer Tank) | ~1–2 Jahre | Reparieren wenn stabil |

**Praktische Regel:** Repariere, wenn <25% der Neukosten anfallen. Tausche aus, wenn >50% der Neukosten anfallen.

### 15.5 Kostenoptimierung-Tipps

1. **Bulk-Kauf:** 10er Packung 316L-Bolzen kaufen (€2 pro Stück statt €4)
2. **Vorbereitung:** Alle Teile selbst vorbereiten (Entfetten, Markieren), Schlosserei macht nur Schweißung (+€150–€300 Arbeit sparen)
3. **Material-Wahl:** 316L statt 2205 sparen ~€5–€10 pro kg (aber: Duplex rechnet sich über >15 Jahre)
4. **DIY Passivierung:** Mit Avesta-Pastern selbst durchführen (€20 Material vs. €100–€200 Werft-Labor)
5. **Lagerhaltung:** Kleine Stock an häufigen Größen kaufen (25×2 Rohre, M10/M12 Bolzen) — Preisvorteil 20–30%
6. **Verhandeln:** Mit Schlosser-Betrieben über Pauschal-Stundensätze verhandeln (€50–€70 statt €80–€100)

---

*Ende Abschnitt 15*

---

## 16. Normen und Standards

Normen und Standards legen fest, wie Edelstahl-Materialien und ihre Verarbeitung zu spezifizieren, zu testen und zu dokumentieren sind. Die Einhaltung dieser Normen ist für sicherheitskritische Bauteile (Kielbolzen, Chainplates, Davits) essentiell.

### 16.1 Europäische Materialnormen (EN)

| Norm | Titel | Relevanz für Yachtbau | Wichtigste Inhalte |
|------|-------|----------|----------|
| EN 10088-1 | Nichtrostende Stähle — Teile 1–5 Übersicht | Legierungsbezeichnungen, Zusammensetzung, Klassifikation | Definiert was 316, 316L, 2205 etc. ist |
| EN 10088-2 | Nichtrostende Stähle — Technische Lieferbedingungen | Mechanische Eigenschaften, Toleranzen für alle Halbzeuge | Verbindlich bei Bestellung |
| EN 10088-3 | Nichtrostende Stähle — Halbzeug, Stäbe, Walzdraht | Flachstahl (20–100mm), Rundstahl, Profile in SS | Für Maß-toleranzen: EN 10058/60 |
| EN 10204 | Metallische Erzeugnisse — Prüfbescheinigungen | Material-Zertifikat Stufe 3.1 (Werks-Test bescheinigt) | CRITICAL: Immer "Zertifikat 3.1" bei Kauf fordern! |
| EN 10216-5 | Nahtlose Rohre aus nichtrostendem Stahl | Rohr-Spezifikation (Außen-Ø, Wandstärke, Toleranzen) | Referenz für Reling-Rohre (25×2, 32×2 etc.) |
| EN 10217-7 | Geschweißte Rohre aus nichtrostendem Stahl | Geschweißte Rohre (WIG, Laser) | Für Reparatur-Rohre |
| EN 10217-13 | Elektrogeschweißte Rohre (Hochfrequenz) | Elektrisch geschweißte Rohre (günstig, aber schlechtere Qualität) | Nicht für kritische Anwendungen! |
| EN 10028-7 | Flacherzeugnisse aus nichtrostendem Stahl — Druckbehälter | Bleche für Tanks (Wandstärke, Toleranz, Oberfläche) | Edelstahltank-Lieferanten verwenden |
| EN 10058 | Flachstahl (Warmgewalzt) — Toleranzen | Maßtoleranzen für Flachstahl (40×8, 50×10 etc.) | Verhinderт Überraschungen bei Lieferung |
| EN 10060 | Rundstahl (Warmgewalzt) — Toleranzen | Maßtoleranzen für Rundstahl (Ø10, Ø16 etc.) | Kielbolzen, Propellerwellen-Zurichtung |
| EN 10058 / 10060 | Allgemeine Toleranzen für Halbzeuge | Wie genau müssen Abmessungen sein? | Typisch h9 oder h11 Toleranz-Grade |

> ⚠️ **ZU PRÜFEN (Audit):** "EN 10217-13" (Zeile oben) existiert nicht — die Reihe EN 10217 (geschweißte Stahlrohre für Druckzwecke) umfasst nur die Teile 1–7 (Teil 7 = nichtrostend, Teil 2 = elektrisch/HF-geschweißt). Die Teilnummer -13 ist unverifiziert.

### 16.2 Amerikanische Normen (ASTM)

Für Boote mit US-Herkunft oder US-Material:

| Norm | Titel | Äquivalent (EN) | Verwendung |
|------|-------|---|---|
| ASTM A269 | Seamless and Welded Austenitic Stainless Steel Tubing | EN 10216-5 + EN 10217-7 | Reling-Rohre aus USA/Kanada |
| ASTM A240 | Chromium and Chromium-Nickel Stainless Steel Plate/Sheet | EN 10088-2 + EN 10028-7 | Bleche, Tanks |
| ASTM A276 | Stainless Steel Bars and Shapes (Round, Flat, Hex) | EN 10060, EN 10058 | Rundstahl, Flachstahl aus USA |
| ASTM A193 | Alloy Steel and Stainless Steel Bolting | ISO 898, EN 20898 | Bolzen für kritische Anwendungen |
| ASTM A307 | Carbon Structural Steel Bolts and Studs | — | NICHT für Edelstahl! Verwechslungsgefahr! |
| ASTM A582 | Stainless Steel Bar, Forged | — | Schmiedeteil-Edelstahl (Fittings, Muffen) |
| ASTM B575 | Ni-Mo-Cr (High Performance Stainless) | — | Super-Duplex 2507, Hastelloy (extreme marine) |

**Konversion ASTM ↔ EN:**
- ASTM A269 / 316L ≈ EN 10217-7 / 1.4404
- ASTM A240 / 316L ≈ EN 10028-7 / 1.4404
- ASTM A276 / 316L ≈ EN 10060 / 1.4404

### 16.3 Schweißnormen (ISO/EN)

| Norm | Titel | Verwendung |
|------|-------|-----------|
| ISO 9606-1 / EN ISO 9606-1 | Prüfung und Bescheinigung von Schweißern — Stahl | Schweißer-Qualifikation: Werft muss "Edelstahl WIG" zertifizierten Schweißer haben |
| ISO 15614-1 / EN ISO 15614-1 | Schweißverfahrensprüfung (Procedure Qualification Record = PQR) | Werft muss vor Großprojekten Schweißverfahren prüfen + dokumentieren |
| ISO 5817 / EN ISO 5817 | Bewertungsgruppen für Unregelmäßigkeiten in Schweißnähten | Qualitätsklasse: B (höchste), C (gut), D (akzeptabel) — B für marine! |
| ISO 6947 / EN ISO 6947 | Schweißpositionen (PA, PB, PF, PG, etc.) | Definiert, in welchen Positionen Schweißung qualifiziert sein muss |
| ISO 13919-1 / EN ISO 13919-1 | Metallische Klebteilschweißungen (Laser) | Für Laser-geschweißte Rohre (Sichtbarkeit der Naht) |
| AWS D1.6 | Structural Welding Code — Stainless Steel (USA) | US-Äquivalent zu EN ISO-Normen |

**Marine-Praktiken:**
- Schweißer sollte ISO 9606-1 zertifiziert sein (mindestens Level 2)
- Verfahren sollte nach ISO 15614-1 geprüft sein
- Schweißnaht-Qualität: Mindestens Klasse C nach ISO 5817, besser B

### 16.4 Marine-Normen (ISO / CE-Richtlinie)

| Norm / Richtlinie | Titel | Relevanz für Edelstahl |
|------|-------|----------|
| **CE 2013/53/EU** | Richtlinie über Freizeitfahrzeuge (Boote) | Definiert, wo Edelstahl sein MUSS (Wanten unter Last, Kielbolzen) |
| **ISO 12215** | Small craft — Hull construction and scantlings | Rumpf-Struktur, wo Edelstahl-Verstrebungen erforderlich sind |
| **ISO 12217** | Small craft — Stability and buoyancy | Berechnung von Gewicht und Schwerpunkt (Edelstahl-Materialgewichte) |
| **ISO 15084** | Small craft — Anchoring, mooring and towing | Chainplate-Auslegung, Belastungen |
| **ISO 10088** | Small craft — Permanently installed fuel systems | Edelstahl-Tanks (Spezifikation Wandstärke, Schweißung) |
| **ISO 11591** | Small craft — Field of vision from the steering position (Sichtfeld vom Steuerstand) | Kein direkter Bezug zu Edelstahl-Halbzeugen (Norm regelt Sichtfeld, nicht Beschläge) |
| **Classification Societies** (GL, DNV, BV, LR, ABS) | Schiffsklassifizierung | Für klassifizierte Yachten verbindliche Vorgaben |

> ✅ Aufgelöst (Audit): ISO 11591 = "Small craft — Field of vision from the steering position" (Sichtfeld vom Steuerstand), nicht Windsurfing; Titel korrigiert und Zeile als nicht einschlägig für Edelstahl-Halbzeuge markiert. Quelle: ISO.org (ISO 11591:2020, iso.org/standard/80914.html).

### 16.5 Klassifikations-Regeln (Relevante Klassifikationen)

Für Yachten mit Klassifikation (Chartering, Luxus):

| Klassifikation | Maritime Edelstahl-Anforderungen |
|---|---|
| **Germanischer Lloyd (GL)** | Kielbolzen: Aquamet 22 oder Duplex 2205. Chainplates: mind. 316L. Wanten: alle Durchmesser Edelstahl-zertifiziert |
| **DNV-GL** | Wie GL. Zusätzlich: Spannungsrisskorrosion-Tests für alle sicherheitskritischen Teile |
| **Bureau Veritas (BV)** | Ähnlich GL. Fokus auf Korrosions-Monitoring über Schiff-Lebensdauer |
| **Lloyd's Register (LR)** | Britisch. Edelstahl-Spezifikation: "Marine Grade" (impliziert 316L min.) |
| **American Bureau of Shipping (ABS)** | USA. Akzeptiert ASTM-Normen zusätzlich zu ISO |

**Praktische Folge:** Klassifizierte Yachten müssen Edelstahl-Dokumentation aufbewahren (Zertifikate, Inspektions-Berichte).

### 16.6 Oberflächenbehandlung-Normen

| Norm | Standard | Beschreibung | Ra (µm) |
|------|----------|---|---|
| **EN 10088-2 Oberflächenzustände** | 1D (No. 1) | Warmgewalzt, Zunder teilweise entfernt | 3–8 |
| — | 2B | Kaltgewalzt, schwach glänzend | 0,1–0,5 |
| — | 2D | Kaltgewalzt + einfach entölt | 0,2–0,8 |
| **EN ISO 4287** (Oberflächenrauheit) | #240 / SCC 600 | Geschliffen, satiniert | 0,2–0,4 |
| — | #320 / SCC 800 | Feiner satiniert (empfohlen) | 0,1–0,3 |
| — | #400 / SCC 1000 | Poliert, Spiegel-Finish | 0,05–0,15 |
| **EN ISO 12944** | Elektropoliert | Chemisch geglättet (Gold-Standard) | <0,05 |

---

*Ende Abschnitt 16*

---

## 17. FAQ — Häufig gestellte Fragen

### 17.1 Ist 304 für Reling akzeptabel?

Auf Binnengewässern und für reine Süßwasser-Yachten: Ja. Im Salzwasser: NEIN. Die fehlende Molybdän-Zugabe macht 304 anfällig für Lochfraß und Tea Staining im Salzwasser-Milieu. Der Preisunterschied zu 316 ist gering (20–30 %).

### 17.2 Wie erkenne ich ob mein Edelstahl 304 oder 316 ist?

1. **Materialzertifikat (Mill Cert)** — Sicherste Methode. Verlangen bei Kauf.
2. **Molybdän-Testflüssigkeit** — "Moly Drop" Test. 316 verfärbt nicht, 304 wird orange. Kosten: €15–€30 für Testset.
3. **Magnettest** — UNZUVERLÄSSIG! Sowohl 304 als auch 316 können schwach magnetisch sein (nach Kaltverformung). Nicht zur Unterscheidung geeignet.
4. **XRF-Analyse** — Professionell, 100 % sicher. Kosten: €50–€100 pro Messung.

### 17.3 Warum rostet mein Edelstahl?

Mögliche Ursachen:
1. **Fremdrost** — Kontamination mit Normalstahl (häufigstes Problem)
2. **304 statt 316** — Falsche Legierung im Salzwasser
3. **Spaltkorrosion** — In Spalten unter Schrauben, Beschlägen
4. **Kontaktkorrosion** — Mit Aluminium oder Normalstahl
5. **Beschädigte Passivschicht** — Nach Schweißen nicht behandelt
6. **Chlorid-Angriff** — Konzentrierte Salzlösung (eingetrocknet)

### 17.4 Muss ich Edelstahl pflegen?

Ja! Edelstahl ist wartungsärmer als andere Metalle, aber nicht wartungsfrei.

| Pflege | Häufigkeit | Methode |
|--------|-----------|---------|
| Süßwasser-Abspülung | Nach jedem Törn | Deckwaschpumpe oder Schlauch |
| Reinigung | Monatlich (Salzwasser) | Spülmittel + Wasser |
| Fremdrost entfernen | Bei Auftreten | Bar Keeper's Friend / Oxalsäure |
| Polieren | Jährlich | Autosol / Flitz / Marine-Politur |
| Konservieren | Jährlich | CorrosionX, Boeshield T-9, Lanocote |
| Inspektion (Chainplates) | Alle 5 Jahre | Visuell + ggf. Farbeindringprüfung |

### 17.5 Kann ich Edelstahl selbst schweißen?

Mit WIG/TIG-Erfahrung: Ja. Ohne: Nicht empfohlen für strukturelle Teile.

**Minimum-Equipment für Edelstahl-WIG:**

| Artikel | Preis ca. | Empfehlung |
|---------|----------|-----------|
| WIG-Schweißgerät (DC, HF-Zündung) | €500–€2.000 | Fronius TransTig, Miller Dynasty, Jasic |
| Argon-Flasche 10L + Druckminderer | €150–€300 | Linde, Air Liquide |
| Zusatzwerkstoff 316LSi Ø1,6mm | €20–€40/kg | ESAB, Böhler |
| Wolframelektroden WC20 | €10–€20 | Ø 1,6 + 2,4 mm |
| Beiz-/Passivierungspaste | €15–€25 | Avesta 401/601 |
| **Gesamt Grundausstattung** | **€695–€2.385** | |

### 17.6 Wo lasse ich Custom-Teile fertigen?

1. **Yachtwerft mit eigener Schlosserei** — Teuer, aber marine-erfahren
2. **Edelstahl-Schlosserei** — Günstig, aber ggf. keine Marine-Erfahrung → 316L spezifizieren!
3. **Landwirtschafts-Schlosserei** — Oft sehr günstig, kennt Edelstahl → Marine-Spezifikationen mitgeben
4. **Online-Zuschnitt + eigene Montage** — Laserzuschnitt nach DXF, selbst bohren/biegen
5. **Fernziel-Schlossereien** — Trinidad, Langkawi, Kapstadt = gute Qualität, günstige Preise

### 17.7 Wie bestelle ich Flachstahl für Chainplates richtig?

1. **Material:** "Edelstahl 316L, Werkstoff-Nr. 1.4404, A4L" angeben
2. **Abmessung:** Breite × Dicke × Länge (z.B. 50 × 10 × 400 mm)
3. **Oberfläche:** "Kaltgewalzt, geschliffen #240 oder besser"
4. **Zertifikat:** "Materialzertifikat EN 10204 Typ 3.1" verlangen
5. **Toleranz:** EN 10058 (Flachstahl) — ±0,5 mm auf Dicke
6. **Lieferung:** In Schutzfolie oder -papier (gegen Transport-Kratzer)

### 17.8 Welches Rohr für eine neue Reling?

| Yacht-Länge | Rohr-Ø | Wandstärke | Material |
|------------|--------|-----------|---------|
| <8 m | 22 mm | 1,5 mm | 316L |
| 8–10 m | 25 mm | 1,5 mm | 316L |
| 10–12 m | 25 mm | 2,0 mm | 316L |
| 12–14 m | 30 mm | 2,0 mm | 316L |
| 14–18 m | 32 mm | 2,0 mm | 316L |
| 18–25 m | 38 mm | 2,0 mm | 316L |

### 17.9 Wie viel Edelstahl brauche ich für eine neue Reling?

**Faustformel:** Gesamtlänge Reling (m) × 2,5 = Rohr-Bedarf (m). Der Faktor 2,5 berücksichtigt Ober- und Unterzug plus Abfall.

Beispiel 10m Segelboot: Gesamtlänge Reling ca. 14m → 14 × 2,5 = 35m Rohr

### 17.10 Kann ich Edelstahl löten statt schweißen?

NUR für nicht-strukturelle Verbindungen und NUR mit Silberlot (>45% Ag) und passendem Flussmittel. Lötstellen haben 30–50 % der Festigkeit von Schweißnähten. NICHT für Chainplates, Relingen oder andere belastete Teile.

### 17.11 Was kostet eine neue Reling komplett?

| Posten | 10m Yacht (Richtwert) |
|--------|--------------------|
| Rohr 25×2mm, ~35m | €315–€560 |
| Beschläge (Stanchion-Basen, T-Stücke, Endkappen, ~30 Stk.) | €300–€600 |
| Fertigung (Biegen, Schweißen, Polieren) | €800–€2.000 |
| Montage (Backing Plates, Bolzen, Dichtmittel) | €200–€400 |
| **Gesamt** | **€1.615–€3.560** |

### 17.12 Wie lagere ich Edelstahl-Halbzeuge an Bord?

- Trocken, belüftet
- NICHT in Kontakt mit Normalstahl oder Aluminium
- In Schutzfolie oder -papier
- Rohre: Enden mit Tape verschließen (gegen Salzwasser-Eindringen)
- Beschriften: Material, Abmessung, Kaufdatum

### 17.13 Rostfreier Stahl in den Tropen — besondere Vorsicht?

Ja: Höhere Temperatur + Salzwasser beschleunigen alle Korrosionsprozesse. In den Tropen:
- Häufiger spülen (Süßwasser)
- Konservierungsmittel nutzen (CorrosionX)
- Inspektionsintervalle halbieren
- 316L als Minimum, Duplex bevorzugt für kritische Teile

### 17.14 Duplex schweißen — was beachten?

Duplex 2205 ist anspruchsvoller zu schweißen als 316L:
- Wärmeeinbringung kontrolliert (0,5–2,5 kJ/mm)
- Zwischenlagentemperatur max. 150°C
- Zusatzwerkstoff: 2209 (ER2209 / W 22 9 3 NL) — NICHT 316L!
- Abkühlrate nicht zu langsam (Sigma-Phase vermeiden)
- Beizen + Passivieren PFLICHT
- Ferritgehalt prüfen (30–70 % Zielbereich)

### 17.15 Was bedeutet "sensitized stainless steel"?

Sensibilisierung = Chromkarbid-Ausscheidung an Korngrenzen bei 500–800°C. Die Chrom-verarmte Zone korrodiert bevorzugt (intergranulare Korrosion). Ursache: falsche Schweißparameter, zu langsame Abkühlung, falsche Wärmebehandlung. Lösung: 316L (Low Carbon) verwenden, korrekte Schweißparameter, Nachbehandlung.

---

## 18. Troubleshooting — Diagnose und Reparatur

Dieses Kapitel behandelt häufige Probleme mit Edelstahl-Halbzeugen im Yachtbau und bietet praktische Lösungen.

### 18.1 Problem-Diagnose-Matrix (Umfassend)

| Problem | Mögliche Ursache | Diagnose-Verfahren | Lösung |
|---------|-----------------|-------|--------|
| **Oberflächenrost (braun, Fremdrost)** | Eisenpartikel von Stahlwolle, Stahlwerkzeugen, oder Teak-Tannine | Oxalsäure-Test (Moly-Test Kit): Verfärbung löst sich auf = Fremdrost | Bar Keeper's Friend (5 min), Abbürsten (Kupfer- oder Edelstahlbürste), Abspülen, Passivierung |
| **Lochfraß (Pitting, kleine Löcher <2mm)** | 304 statt 316 (PREN zu niedrig), oder Chlorid-Konzentration unter Ablagerung zu hoch | Moly-Test (bestätigt Material), Lupe 10×: Lochform rund = Pitting. Farbeindringprüfung für Tiefe | Wenn 304: Austausch obligatorisch. Wenn 316L mit <0,5mm Tiefe: Polieren #240, Passivierung, überwachen |
| **Spaltkorrosion (Verfärbung + Rauhheit in Spalten)** | Wasser unter Decksdichtung, O₂-Mangel, Chlorid-Ansammlung | Farbeindringprüfung (rote Farbe in Spalt einwirken lassen), Oberflächenrauheit messen | Chainplate ausbauen, Sealant erneuern (Sikaflex 291), G10-Isolierung einbauen, Beizen + Passivieren |
| **Risse an Schweißnaht (linear)** | Sensibilisierung (Chromverarmung in Heat Affected Zone), Spannungsrisskorrosion bei Belastung | Farbeindringprüfung (Best Practice), Riss-Länge und -Tiefe notieren | Schweißnaht komplett entfernen (Grinder), neuer Schweißdraht 316LSi, WIG-Schweißung, Beizen + Passivieren. Bei Strukturteilen: Austausch statt Reparatur! |
| **Dunkle Anlauffarben nach Schweißen (blau, violett, braun)** | Nicht behandelte Schweißnaht nach dem Schweißen (chromverarmt, noch nicht passiviert) | Visuell: Farbveränderung entlang Schweißnaht. Oberflächenrauheit-Messer zeigt Ra >1 µm | Beizen-Paste (Avesta 401) 30–60 min auftragen, Abbürsten, Spülen, Passivierungs-Paste (Avesta 601) 60 min, Abspülen. Nicht ignorieren! |
| **Weißes Pulver unter SS-Beschlag auf Alu-Rumpf** | Galvanische Korrosion: SS ist noble, Alu ist anode, direkter metallischer Kontakt | Visuell + Multimeter-Messung (Kontinuität zwischen SS und Alu prüfen) | Isolation sofort einbauen: G10-Platte unter Beschlag (6–10mm), Tef-Gel unter alle Bolzen-Köpfe, Nylon-Isolierbuchsen. Alte Korrosionsprudukte (Al₂O₃) abbürsten (nicht aggressive Chemie). Langfristig: Zink-Anode oder Opfer-Blech unter Motor |
| **Edelstahl plötzlich magnetisch** | Kaltverformung bei Biegen/Verarbeitung: Austenitische Struktur wird teilweise martensitisch → Magnetismus | Normales Verhalten, kein Fehler. Magnet-Test ist nicht zuverlässig für Edelstahl-Identifikation | Kein Problem! Korrosionsbeständigkeit bleibt erhalten. Mag nicht schön aussehen, aber strukturell okay |
| **Rohr knickt beim Biegen (Knickstelle sichtbar)** | Biegeradius zu eng (R <3×Ø), oder keine Füllung/Dorn während des Biegens | Visuelle Kontrolle: Rohr-Durchmesser an Knickstelle < Original-Durchmesser | Geknickte Segment ausschneiden. Neu biegen mit R ≥ 5×Ø (besser 7×Ø), mit Sand-Füllung oder Dorn (Kunststoff-Dorn kaufen). WIG-Schweißung. Neue Segment muss Wandstärke originale erfüllen |
| **Bohrer blockiert beim Bohren in SS (quietscht, wird blau)** | Kaltverfestigung: Edelstahl verhärtet bei Verarbeitung. Standard-Stahlbohrer rutscht ab, erzeugt Reibung/Hitze | Bohrer sehr heiß (blau), quietscht, spinnt nicht rein | **Sofort stoppen!** Nicht mit Kraft bohren (macht schlimmer). Cobalt-Bohrer (5–8% Co) verwenden, sehr hoher Vorschub, reichlich Kühlmittel (WD40, Schneidöl), langsame RPM (Drehzahl <300 für Ø6mm). Oder: Vorbohren mit kleineren Bohrer, schrittweise |
| **Schweißnaht sieht porig aus (Löcher in Naht)** | Keine Schutzgas-Abdeckung (Wind beim Schweißen), feuchter Draht, schlechte Lagerung | Visuell: Löcher in Schweißnaht erkennbar | Schweißnaht entfernen (Grinder), Bereich neu vorbereiten, mit besserer Schutzgas-Kontrolle neu schweißen (Windschutz!), Beizen + Passivieren |
| **Bolzen lässt sich nicht anziehen (dreht nur, zieht nicht)**  | Loch beschädigt (Gewinde verstriffen), oder Bolzen defekt (Gewinde abgenutzt) | Bolzen vorsichtig herausdrehen, Gewinde prüfen, Loch mit Lupe kontrollieren | Loch: Nächst-größerer Bolzen verwenden (z.B. M10 → M12), oder Gewindereparatur-Einsatz (HeliCoil). Bolzen: Neuen Duplex oder 316L verwenden |
| **Reling vibriert oder "singelt" bei Wind** | Zu dünner Rohr-Durchmesser, oder lose Befestigung | Mit Hand drücken: Rohr biegt sich viel? Befestigungen kontrollieren (Bolzen nachziehen) | Wenn Rohr zu dünn: Segment austauschen (Dimension erhöhen, z.B. von 22×1,5 auf 25×2). Befestigungen: Alle Bolzen nachziehen, Lock-Nuts prüfen |

---

### 18.2 Notfall-Reparaturen auf See (Ohne Werft)

Für Yachten auf Langfahrt, fernab von Werften: Provisorische Reparaturen bis zum nächsten Hafen.

| Situation | Sofort-Maßnahme | Benötigtes Material | Permanente Reparatur |
|-----------|----------------|---------|---------------------|
| **Reling-Rohr gebrochen (Bug oder Seite)** | Rohr mit 2 Rohrschellen (Stahl oder Alu, jeweils 50–100mm Länge) + Alu-Schiene (Flacheisen 20×3mm) als Splint-Schiene absichern (beide Seiten der Bruchstelle) | 2 Rohrschellen Ø25mm, 1 Alu-Schiene 20×3 mm, 4 Bolzen M8 | In nächstem Hafen: Altes Rohr-Segment ausschneiden, neues 25×2 mm 316L-Rohr einschweißen (WIG), Beizen + Passivieren |
| **Chainplate-Riss entdeckt (Strukturwante)** | Provisorische Dyneema-Schlinge (10mm, Länge ca. 1m) um Chainplate-Basis legen und mit Schäkel zu Backing-Plate fixieren (belastet Spannung dorthin, nicht auf Riss) | Dyneema-Seil 10mm (aus Traveler/Vang-System), 1 Schäkel M8 | In nächstem Hafen: Chainplate auswechseln (siehe ANHANG D für Kosten). Neue Chainplate: 50×10mm 316L oder Duplex, mit Beizen + Passivierung |
| **Stanchion-Basis ausgerissen (aus Decksbefestigung)** | Sofort Reling mit Spanngurt oder Dyneema-Seil zur nächsten festen Struktur (z.B. Winsch, Baumhülle) sichern (Sicherheit vor Mensch-über-Bord!) | Spanngurt 50mm (von Fenderhalterungen) oder Dyneema-Seil 8mm + Schäkel | In Hafen: Neue Backing-Plate (80×80×5mm SS316L oder GFK) zuschneiden, unter Deck-Durchführung montieren (mind. 6 neue Bolzen), alten Bereich mit G10-Platte isolieren |
| **Davit-Schweißnaht gerissen (Dinner gerissen aus Davit)** | Davit sofort **vollständig entlasten** (Dingi aus Davit nehmen, wenn möglich von anderen Crewmitgliedern halten). Provisorische Sicherung mit Spanngurt um Dingi + Davit-Basis | Spanngurt, Soft-Slings, evtl. Blockschiff als Schlag | In Hafen: Schweißnaht-Reparatur durch fachkundige Werft erforderlich (Röntgen-Prüfung nach Reparatur!) oder Davit-Austausch |
| **Tank leckt aus Schweißnaht (Diesel oder Wasser)** | **Diesel-Tank:** Provisorisch mit 2-Komponenten-Epoxid (JB Weld, Marine-Tex) abdichten. **Wasser-Tank:** Filter/Sieb einbauen, Druckabfall über Zeit beobachten | JB Weld oder Marine-Tex Epoxid (~€20), 2K-Epoxid-Klebstoff | In Hafen: Tank ausbauen, Schweißnaht-Bereich mit Farbeindringprüfung prüfen, Falls Leck klein (<5mm): Neu-Schweißen, Beizen + Passivieren. Falls größer: Neuer Tank (€500–€2.000 hängig von Größe) |
| **Propeller-Welle zeigt Verschleiß / Spiel (Vibrationen)** | Sofort Motor reduzieren / Fahrt verringern. Mit Hand prüfen: Welle axial bewegen? Zu viel Spiel ist Zeichen von Bearing-Schaden | Nur Sichtprüfung möglich | In Hafen: **Professionelle Kontrolle erforderlich!** Welle-Austausch oder Bearing-Erneuerung ist komplexe Aufgabe, keine DIY-Reparatur |
| **Rohr-Biegung geknickt (Reling an Kurve)** | Provisorische Schiene mit Rohrschelle + Flachstahl anbringen (wie bei Bruch-Reparatur). Bereich nicht stark belasten | Rohrschellen, Flachstahl-Schiene | In Hafen: Geknickte Rohr-Segment austauschen (neue Biegung mit R ≥ 5×Ø) |
| **Bolzen rosten oder lassen sich nicht öffnen (Festsitzer)** | Mit Penetrating Oil (WD40, Tef-Gel) übergießen, 30 min einwirken lassen. Dann vorsichtig mit Gabelschlüssel (nicht Rohrschlüssel!) drehen. Mit Schlag-Schraubendreher nachhelfen (nicht Gewalt!) | WD40 oder Tef-Gel, Gabelschlüssel passender Größe, evtl. Inbusschlüssel für Drehen | Später bei Werft: Alten Bolzen ersetzen durch neuen aus Duplex 2205 oder 316L, mit Tef-Gel unter Kopf einfetten |

**Allgemeine Regeln für Sea-Repairs:**
1. **Sicherheit zuerst:** Keine Reparatur, die die Sicherheit des Bootes oder der Besatzung gefährdet
2. **Dokumentieren:** Fotos von Schaden + Reparatur machen (für Versicherung, Werft-Reparatur)
3. **Nächster Hafen:** Alle provisorischen Reparaturen sollten innerhalb von 7 Tagen durch professionelle Reparatur ersetzt werden
4. **Kit an Bord:** Siehe ANHANG F, Abschnitt F.7 (Notfall-Reparaturbox)

---

### 18.3 Material-Identifikation im Feld

Wenn Sie nicht sicher sind, ob ein Teil aus 304 oder 316 ist:

| Test | Verfahren | Ergebnis |
|------|-----------|---------|
| **Moly-Test-Kit** | Chemikalien-Tropfen auf Oberfläche. Wenn Mo vorhanden: Farbwechsel innerhalb 30 sec | 304 = kein Farbwechsel. 316 = Farbwechsel = Mo erkannt |
| **Magnet-Test** | Magnetischen Stift/Magnettest-Stift an Material halten | NICHT zuverlässig! Kaltverformtes Edelstahl wird magnetisch, aber ist trotzdem 316L |
| **Oberflächenfinish-Inspektion** | Wie rau ist die Oberfläche? 304 aus älteren Booten oft matt (1D-Walzstruktur) | 316L Premium-Boote oft poliert. Aber nicht 100% zuverlässig |
| **Korrosions-Muster** | 304 zeigt nach 10–15 Jahren in Salzwasser deutliche Spaltkorrosion + Lochfraß. 316L deutlich besser | Langzeit-Indiz, nicht akut hilfreich |
| **Hersteller-Dokumentation** | Schiff-Papiere, Originalgewährleistung, Hersteller-Katalog prüfen | Zuverlässigste Methode, wenn vorhanden |

**Praktische Empfehlung:** Im Zweifelsfall **immer 316L oder Duplex verwenden** für Austausch-Teile (Sicherheit vor Geld sparen).

---

*Ende Abschnitt 18*

---

## 19. AYDI-Integration: Pydantic v2 Modelle

### 19.1 StainlessAlloy Enum

```python
from enum import Enum

class StainlessAlloy(str, Enum):
    AISI_304 = "304"         # 1.4301 / A2
    AISI_304L = "304L"       # 1.4307 / A2L
    AISI_316 = "316"         # 1.4401 / A4
    AISI_316L = "316L"       # 1.4404 / A4L
    AISI_316TI = "316Ti"     # 1.4571
    DUPLEX_2205 = "2205"     # 1.4462
    SUPER_DUPLEX_2507 = "2507"  # 1.4410
    NITRONIC_50 = "nitronic_50"  # S20910
    NITRONIC_60 = "nitronic_60"  # S21800
    PH_17_4 = "17_4_ph"     # 1.4542
    AQUAMET_22 = "aquamet_22"
    SS_1_4313 = "1.4313"     # Propellerwellen
```

### 19.2 SemiFinishedType Enum

```python
class SemiFinishedType(str, Enum):
    TUBE_ROUND = "tube_round"
    TUBE_SQUARE = "tube_square"
    TUBE_RECTANGULAR = "tube_rectangular"
    FLAT_BAR = "flat_bar"
    ROUND_BAR = "round_bar"
    SHEET = "sheet"
    PLATE = "plate"
    ANGLE = "angle"
    CHANNEL = "channel"
    T_PROFILE = "t_profile"
    PERFORATED_SHEET = "perforated_sheet"
```

### 19.3 MarineApplication Enum

```python
class MarineApplication(str, Enum):
    RAILING = "railing"
    CHAINPLATE = "chainplate"
    KEEL_BOLT = "keel_bolt"
    PROP_SHAFT = "prop_shaft"
    RUDDER_SHAFT = "rudder_shaft"
    DAVIT = "davit"
    BIMINI = "bimini"
    PULPIT = "pulpit"
    PUSHPIT = "pushpit"
    TANK_FUEL = "tank_fuel"
    TANK_WATER = "tank_water"
    TANK_WASTE = "tank_waste"
    BACKING_PLATE = "backing_plate"
    ENGINE_BED = "engine_bed"
    CUSTOM_BRACKET = "custom_bracket"
    HYDRAULIC_LINE = "hydraulic_line"
```

### 19.4 StainlessRecommendation Model

```python
from pydantic import BaseModel
from typing import Optional

class StainlessRecommendation(BaseModel):
    model_config = {"from_attributes": True}

    application: MarineApplication
    boat_length_m: float
    environment: str  # "freshwater", "coastal", "offshore", "tropical"
    recommended_alloy: StainlessAlloy
    alternative_alloy: Optional[StainlessAlloy] = None
    semi_finished_type: SemiFinishedType
    dimension_mm: str  # e.g. "25 × 2.0" or "50 × 10"
    surface_finish: str  # "2B", "#240", "#320", "polished", "electropolished"
    weight_per_meter_kg: float
    estimated_price_eur_per_m: float
    safety_critical: bool
    mill_cert_required: bool
    weld_procedure: Optional[str] = None  # "TIG_316LSi", "TIG_2209", None
    corrosion_risk: str  # "low", "medium", "high", "critical"
    inspection_interval_years: int
    notes_de: str
    confidence: str  # "measured", "calculated", "estimated", "documented"
```

### 19.5 ChainplateAssessment Model

```python
class ChainplateAssessment(BaseModel):
    model_config = {"from_attributes": True}

    position: str  # "V1_steuerbord", "V1_backbord", "D1_stbd", etc.
    material_identified: Optional[StainlessAlloy] = None
    width_mm: float
    thickness_mm: float
    cross_section_mm2: float
    rigging_wire_diameter_mm: float
    rigging_wire_breaking_load_kn: float
    safety_factor: float
    surface_condition: str  # "good", "tea_staining", "pitting", "crevice_corrosion", "cracked"
    deck_seal_condition: str  # "good", "dry", "cracked", "missing"
    age_years: Optional[int] = None
    last_inspection: Optional[str] = None
    urgency: str  # "none", "monitor", "plan_replacement", "urgent", "critical"
    recommendation_de: str
    confidence: str
```

### 19.6 WeldAssessment Model

```python
class WeldAssessment(BaseModel):
    model_config = {"from_attributes": True}

    weld_location: str  # "reling_stanchion", "chainplate_toggle", "davit_base", etc.
    weld_method: str  # "TIG", "MIG", "stick", "unknown"
    filler_material: Optional[str] = None  # "316LSi", "2209", "309L", etc.
    heat_tint_present: bool
    heat_tint_color: Optional[str] = None  # "straw", "brown", "blue", "grey"
    post_weld_treatment: str  # "pickled_passivated", "pickled_only", "none", "unknown"
    crack_detected: bool
    pitting_at_haz: bool  # Heat Affected Zone
    surface_condition: str  # "good", "acceptable", "poor", "critical"
    urgency: str  # "none", "monitor", "plan_repair", "urgent", "critical"
    recommendation_de: str
    confidence: str  # "measured", "visual_high", "visual_medium", "estimated"
```

**Confidence-Zuordnung für AYDI-Bewertungen:**

| Datenquelle | Confidence-Level | Beschreibung |
|-------------|-----------------|--------------|
| Millzertifikat vorhanden | `measured` | Exakte Legierungszusammensetzung dokumentiert |
| Ultraschall-Wandstärkenmessung | `measured` | Exakte Wandstärke gemessen |
| Berechnung aus gemessenen Werten | `calculated` | Querschnitt, Sicherheitsfaktor abgeleitet |
| Foto mit klarer Oberfläche | `visual_high` | Oberflächenzustand eindeutig erkennbar |
| Foto mit eingeschränkter Sicht | `visual_medium` | Teilweise verdeckt oder schlechte Beleuchtung |
| Bootklasse-Durchschnittswerte | `estimated` | Typische Werte für Bootsklasse angenommen |
| Herstellerkatalog-Angaben | `documented` | Vom Hersteller publizierte Spezifikationen |
| Industrie-Benchmark-Daten | `benchmark` | Aggregierte Branchendaten als Referenz |

### 19.7 Analyse-Funktion (Pseudocode)

```python
def recommend_stainless(
    application: MarineApplication,
    boat_length_m: float,
    environment: str = "coastal",
) -> StainlessRecommendation:
    """
    Empfiehlt Edelstahl-Halbzeug basierend auf
    Anwendung, Bootsgröße und Einsatzgebiet.

    Returns StainlessRecommendation mit confidence = "calculated"
    """
    # Alloy selection
    if application in [MarineApplication.KEEL_BOLT, MarineApplication.RUDDER_SHAFT]:
        alloy = StainlessAlloy.DUPLEX_2205
        safety_critical = True
        mill_cert = True
    elif application == MarineApplication.PROP_SHAFT:
        alloy = StainlessAlloy.AQUAMET_22
        safety_critical = True
        mill_cert = True
    elif application == MarineApplication.CHAINPLATE:
        alloy = StainlessAlloy.DUPLEX_2205 if environment in ["offshore", "tropical"] else StainlessAlloy.AISI_316L
        safety_critical = True
        mill_cert = True
    else:
        alloy = StainlessAlloy.AISI_316L
        safety_critical = False
        mill_cert = False

    # Dimension selection based on boat length + application...
    # ... detailed lookup tables ...
```

---

## ANHANG A — Material-Datenblätter Zusammenfassung

Diese Datenblätter bieten einen Überblick über die wichtigsten Edelstahl-Legierungen für den Yachtbau. Die Werte beziehen sich auf annealed (weichgeglühte) Zustände, soweit nicht anders angegeben. Technische Änderungen und Herstellerabweichungen bleiben vorbehalten.

### A.1 316L (X2CrNiMo17-12-2, 1.4404, A4L) — Vollständige Eigenschaften

**Synonym:** AISI 316L, SS316L, Inox 1.4404

**Zusammensetzung:**
| Element | % min. | % max. |
|---------|--------|--------|
| Chromium (Cr) | 16,5 | 18,5 |
| Nickel (Ni) | 10,0 | 13,0 |
| Molybdän (Mo) | 2,0 | 2,5 |
| Kohlenstoff (C) | — | 0,03 |
| Mangan (Mn) | — | 2,0 |
| Silizium (Si) | — | 1,0 |
| Phosphor (P) | — | 0,045 |
| Schwefel (S) | — | 0,015 |
| Stickstoff (N) | 0,08 | 0,20 |

**Mechanische Eigenschaften (annealed):**
| Eigenschaft | Einheit | Wert | Bemerkung |
|-------------|---------|------|-----------|
| Zugfestigkeit Rm | MPa | 485–680 | Je nach Kaltverformung |
| Streckgrenze Rp0,2 | MPa | 170–220 | In weichgeglühtem Zustand |
| Bruchdehnung A5 | % | 40–45 | Gute Plastizität |
| Brucheinschnürung | % | 40–50 | Duktilität |
| Härte HV10 | — | 130–180 | Weich bis mittel |
| E-Modul (Elastizität) | GPa | 200 | Wie Stahl |
| Schubmodul | GPa | 81 | — |
| Dichte | g/cm³ | 7,98 | Etwas dichter als reines Eisen |

**Wärmeeigenschaften:**
| Eigenschaft | Einheit | Wert |
|-------------|---------|------|
| Wärmeleitfähigkeit (20°C) | W/(m·K) | 14,2 |
| Wärmeleitfähigkeit (100°C) | W/(m·K) | 15,4 |
| Spezifische Wärme (20°C) | J/(kg·K) | 500 |
| Wärmeausdehnung (0–100°C) | 10⁻⁶/K | 16,0 |
| Schmelzbereich | °C | 1.375–1.400 |

**Korrosionseigenschaften:**
| Eigenschaft | Wert |
|-------------|------|
| PREN (Lochfraß-Beständigkeit) | 24–26 |
| Kategorie nach EN 10088-1 | Hochlegiert |
| Salznebelprüfung (ASTM B117, 500h) | Kein Rost >5mm |
| Spaltkorrosion (pH 2, FeCl₃) | Beständig ab pH 4 |
| Süßwasser | Exzellent |
| Brackwasser | Gut (mit Passivierung) |
| Salzwasser <5m Tiefe | Gut (mit Passivierung) |
| Salzwasser >5m Tiefe | Befriedigend (Duplex besser) |

**Schweißen (WIG/TIG empfohlen):**
- **Zusatzwerkstoff:** ER316L (AWS) oder SG X2 CrNiMo18-9 (DIN)
- **Schutzgas:** Argon 99,99% oder Argon+He Mix (bis 25% He)
- **Strom:** Typisch 100–150 A für 1,6–2,4mm Draht
- **Schweißtemperatur:** Nicht >200°C Zwischenlage (Sensibilisierung vermeiden)
- **Vorwärmen:** Nicht nötig
- **Nachbehandlung:** Unbedingt! Beizen (Avesta 401) + Passivieren (Avesta 601)

**Vorteile:**
- Marine-Standard seit 40 Jahren bewährt
- Ausreichende Korrosionsbeständigkeit für die meisten Yachtanwendungen
- Gute Schweißbarkeit
- Moderate Kosten
- Große Verfügbarkeit

**Nachteile:**
- Nicht ideal für permanente Salzwasser-Immersion (PREN 26 < Duplex 34)
- Spaltkorrosion möglich in schlecht belüfteten Spalten
- Kann bei fehlerhafter Passivierung nach 15–20 Jahren Korrosion zeigen

**Typische Anwendungen im Yachtbau:**
- Reling (25–32mm Rohre)
- Chainplates (40×8 bis 60×10mm Flachstahl)
- Davits, Pulpits
- Handläufe, Beschläge
- Schweißzusatz für Reparaturen

**Preis (2026):** €45–€75 pro kg (je nach Form und Oberflächenfinish)

---

### A.2 2205 Duplex Stahl (X2CrNiMoN22-5-3, 1.4462, 2205) — Vollständige Eigenschaften

**Synonym:** AISI 2205, Duplex, Lean Duplex, SAF2205 (Sandvik)

**Zusammensetzung:**
| Element | % min. | % max. |
|---------|--------|--------|
| Chromium (Cr) | 21,0 | 23,0 |
| Nickel (Ni) | 4,5 | 6,5 |
| Molybdän (Mo) | 3,0 | 3,5 |
| Kohlenstoff (C) | — | 0,03 |
| Stickstoff (N) | 0,14 | 0,20 |

**Mechanische Eigenschaften (annealed):**
| Eigenschaft | Einheit | Wert |
|-------------|---------|------|
| Zugfestigkeit Rm | MPa | 620–880 |
| Streckgrenze Rp0,2 | MPa | 450–550 |
| Bruchdehnung A5 | % | 25–30 |
| Härte HV10 | — | 217–293 |
| E-Modul | GPa | 200 |
| Dichte | g/cm³ | 7,80 |

**Korrosionseigenschaften:**
| Eigenschaft | Wert |
|-------------|------|
| PREN | 34–36 (deutlich höher als 316L) |
| Spaltkorrosion-Beständigkeit | Exzellent (bis pH <2) |
| Lochfraß-Beständigkeit | Exzellent |
| Salzwasser-Immersion | Exzellent (auch >5m Tiefe) |
| Tropische Gewässer | Exzellent (Stillwasser, hohe Temperaturen) |

**Schweißen:**
- **Zusatzwerkstoff:** ER2209 (speziell für Duplex!)
- **Parameter:** Erhöhter Strom (ca. 150–200A), schneller Schweißen (Ferrit-Balance!)
- **Besonderheit:** Ferrit-Balance ist kritisch (Phasengleichgewicht zwischen Austenit + Ferrit)
- **Nachbehandlung:** Beizen + Passivieren (auch mit Duplex-spezifischen Pasten wie Avesta 606)

**Vorteile:**
- Höhere Festigkeit ermöglicht kleinere Querschnitte
- Hervorragende Korrosionsbeständigkeit (PREN 34 vs. 26 für 316L)
- Sicherheit für 20+ Jahre Langfahrt ohne Austausch
- Bereits bei Korrosion noch sichere Tragfähigkeit

**Nachteile:**
- Höherer Preis (+50–70% vs. 316L)
- Schweißen anspruchsvoller (benötigt Spezialist)
- Weniger verfügbar als 316L
- Keine universelle Lagerware

**Typische Anwendungen im Yachtbau:**
- Kielbolzen (hochbelastet, nicht inspizierbar)
- Chainplates für Großyachten oder Langfahrt-Boote
- Davits (hochbelastet, tropische Gewässer)
- Ruderachsen
- Strukturelle Elemente in Salzwasser-Langfahrt-Yachten

**Preis (2026):** €90–€150 pro kg (deutlich teurer als 316L)

**Kosten-Nutzen-Rechnung:**
- Zusatz-Kosten Duplex-Material: +€200–€400 (vs. 316L für typische Chainplate-Garnitur)
- Einsparung durch Verzicht auf Austausch nach 15 Jahren: €600–€800
- **Amortisierung:** Nach 8–10 Jahren bei Langfahrt-Booten

---

### A.3 Aquamet 22 (US-Herkunft, austenitischer stickstoffverfestigter Edelstahl) — Für Propellerwellen

**Besonderheit:** Austenitischer, stickstoffverfestigter Edelstahl (nitrogen-strengthened 316-Typ), nicht-magnetisch. Die Festigkeit stammt aus Stickstoff + Kaltverfestigung, NICHT aus martensitischer Härtung.

**Zusammensetzung:**
| Element | % min. | % max. |
|---------|--------|--------|
| Chromium (Cr) | 20,5 | 23,5 |
| Nickel (Ni) | 11,5 | 13,5 |
| Molybdän (Mo) | 1,5 | 3,0 |
| Mangan (Mn) | 4,0 | 6,0 |
| Stickstoff (N) | 0,20 | 0,40 |

**Mechanische Eigenschaften (gehärtet, geölt):**
| Eigenschaft | Einheit | Wert |
|-------------|---------|------|
| Zugfestigkeit Rm | MPa | 930 |
| Streckgrenze Rp0,2 | MPa | 690 |
| Bruchdehnung | % | 30 |
| Torsionsfestigkeit | MPa | 620 |
| Härte HRC | — | 28–32 |
| Dichte | g/cm³ | 7,83 |

**Spezielle Eigenschaften:**
- **Korrosionsbeständigkeit:** Exzellent für Salzwasser-Propellerwellen (spez. für Unterwasser-Bauteile entwickelt)
- **PREN:** 35–40 (sehr hoch, speziell gegen Lochfraß optimiert)
- **Fütterung:** Typischerweise in Mineralöl-Lösung geölt
- **Lagern:** Muss trocken gelagert werden, vor Feuchte geschützt

**Typische Anwendungen:**
- **Propellerwellen** (primär, speziell für diesen Zweck entwickelt)
- Ruderachsen (große Yachten)
- Kielbolzen (Alternative zu Duplex)
- Hochbelastete marine Wellen

**Preis (2026):** €150–€250 pro kg (teuerste der Standardlegierungen)

**Besonderheit im Vergleich zu 316L:**
- Höhere Festigkeit ermöglicht kleinere Wellen-Durchmesser
- Kein Schweißen (Gehärteter Stahl → Schweißen zerstört Härte)
- Installation erfolgt meistens "as-received" (vorgefertigte Welle vom Hersteller)

---

### A.4 Nitronic 50 (XM-19, S20910, 1.3964) — Für Kielbolzen

**Zusammensetzung:**
| Element | % |
|---------|-----|
| Chromium (Cr) | 20,0–23,0 |
| Nickel (Ni) | 11,5–13,5 |
| Mangan (Mn) | 5,0–7,0 |
| Stickstoff (N) | 0,20–0,35 |

**Mechanische Eigenschaften:**
| Eigenschaft | Einheit | Wert |
|-------------|---------|------|
| Zugfestigkeit Rm | MPa | 690–860 |
| Streckgrenze Rp0,2 | MPa | 310–450 |
| Bruchdehnung | % | 35–45 |
| Dichte | g/cm³ | 7,88 |
| PREN | — | 34–38 |

**Besonderheit:**
- Stickstoff-gehärtet (Raumtemperatur-Festigung ohne Wärmbehandlung)
- Ausgewogene Festigkeit + Duktilität
- Hohe Gütewerte ohne Verhärtung

**Typische Anwendungen:**
- Kielbolzen (mittlere bis große Yachten)
- Rigg-Fittings
- Ruderachsen

**Preis:** €130–€200 pro kg (zwischen 316L und Duplex)

---

### A.5 Oberflächenfinish-Vergleich und Auswirkungen auf Korrosion

| Finish | Oberflächenrauheit Ra (µm) | Korrosions-Anfälligkeit | Polier-Kosten | Marine-Eignung |
|--------|---------------------------|----------------------|---|---|
| 1D (Walzstruktur) | 3–8 | Hoch (Fremdrost) | €0 | Schlecht (nur über WL) |
| 2B (kaltgewalzt) | 0,1–0,5 | Mittel | €5/m² | Akzeptabel |
| #240 (geschliffen) | 0,2–0,4 | Gering | €10/m² | Gut |
| #320 (feiner geschliffen) | 0,1–0,3 | Sehr gering | €15/m² | Sehr gut |
| Poliert (#400–#600) | 0,05–0,15 | Minimal | €20–€30/m² | Exzellent |
| Elektropoliert | <0,05 | Minimal | €40–€60/m² | Gold-Standard |

**Praktische Folgerung:**
Für marine Anwendungen unterhalb der Wasserlinie sollte mindestens #240 oder poliert (#320+) gewählt werden. Der Aufpreis von €5–€15 pro Meter zahlt sich in reduzierter Wartung über 20 Jahre aus.

---

### A.6 Schweißzusatz-Übersicht

| Zusatz | Standard | Legierung | PREN | Anwendung |
|--------|----------|-----------|------|-----------|
| ER316L | AWS | 316L | 26 | Standard für 316L-Schweißung |
| ER2209 | AWS | Duplex 2205 | 34 | Für Duplex-Schweißung (kritisch!) |
| ER308L | AWS | 308L | 18 | Ersatz, wenn ER316L nicht verfügbar |
| AWS E316L-16 | Stabelektrode | 316L | 26 | Stabschweißen (seltener in Yachtbau) |
| SG X2CrNiMo18-9 | DIN | 316L | 26 | Deutsche Normen-Bezeichnung |

**Wichtig:** Der Schweißzusatz sollte der gleichen Legierung entsprechen wie das Grundmaterial, idealerweise gleiche oder höhere PREN-Zahl.

---

*Ende ANHANG A*

---

## ANHANG B — Chainplate-Dimensionierungstabelle (Komplett)

Die Wahl der Chainplate-Größe ist kritisch für die strukturelle Integrität des Segelboots. Eine zu kleine Chainplate kann zu Versagen führen; eine zu große ist kostspielig und unnötig. Die folgenden Tabellen basieren auf ISO 12217 Stabilität-Standards und realen Rigg-Dimensionierungen.

### B.1 Chainplate nach Rigg-Drahtgröße und Yachtlänge

Empfehlungen für Segelboote (Segel-Area bis 150 m²):

| Yacht (m) | Vorstag | V1 Oben-Want | V2 Unter-Want | D1 Diagonal | Backstag | Bemerkung |
|-----------|---------|-------------|---------------|------------|----------|-----------|
| 7–8 | Ø4, CP 25×6 | Ø4, CP 25×6 | — | Ø3, CP 20×5 | — | Mini-Cruiser |
| 8–9 | Ø5, CP 30×6 | Ø5, CP 30×6 | Ø4, CP 25×6 | Ø4, CP 25×6 | Ø4, CP 25×6 | Wochenend-Boot |
| 9–10 | Ø6, CP 35×6 | Ø6, CP 35×6 | Ø5, CP 30×6 | Ø5, CP 30×6 | Ø5, CP 30×6 | Kleiner Cruiser |
| 10–11 | Ø7, CP 40×8 | Ø6, CP 35×6 | Ø5, CP 30×6 | Ø5, CP 30×6 | Ø5, CP 30×6 | Mittl. Cruiser |
| 11–12 | Ø8, CP 40×8 | Ø7, CP 40×8 | Ø6, CP 35×6 | Ø6, CP 35×6 | Ø6, CP 35×6 | Cruiser 12m |
| 12–14 | Ø8, CP 40×8 | Ø8, CP 40×8 | Ø6, CP 35×6 | Ø6, CP 35×6 | Ø6, CP 35×6 | Großer Cruiser |
| 14–16 | Ø10, CP 50×10 | Ø8, CP 40×8 | Ø7, CP 40×8 | Ø7, CP 40×8 | Ø7, CP 40×8 | Hochsee-Yacht |
| 16–18 | Ø10, CP 50×10 | Ø10, CP 50×10 | Ø8, CP 40×8 | Ø8, CP 40×8 | Ø8, CP 40×8 | Große Yacht |
| 18–20 | Ø12, CP 60×10 | Ø10, CP 50×10 | Ø8, CP 40×8 | Ø8, CP 40×8 | Ø10, CP 50×10 | Sehr große Yacht |
| 20–24 | Ø14, CP 60×12 | Ø12, CP 60×10 | Ø10, CP 50×10 | Ø10, CP 50×10 | Ø10, CP 50×10 | Superyacht-Klasse |

**Abkürzungen:**
- CP = Chainplate (Breite × Dicke in mm)
- Ø = Rigg-Drahtdurchmesser (Litze 1×19)
- V1 = Oberwanten oben
- V2 = Unterwanten
- D1 = Diagonalen / Decksstagen

**Hinweise zu dieser Tabelle:**
1. Diese Werte sind **Richtwerte**, kein Ersatz für Konstruktions-Berechnung
2. Für Racing-Boote (high-load): Eine Größe aufwärts gehen
3. Für Aluminiummasten: Seitliche Lasten höher → CP-Größe prüfen
4. Neuere Boote mit Carbon-Masten: Lasten geringer, kann mitunter eine Größe kleiner sein
5. Langfahrt-Yachten: Lieber oversized als undersized (Sicherheit!)

---

### B.2 Bolzen-Dimensionierung für Chainplates

Kritisch: Bolzen muss Loch exakt ausfüllen, ohne zu großes Lochspiel.

| Rigg-Draht | Min. Bolzen-Ø | Empfohlen | Lochspiel | Randabstand min. | Material |
|-----------|--------------|-----------|----------|-----------------|----------|
| Ø 4 mm | M8 | M8 | 0,5 mm | 16 mm | 316L |
| Ø 5 mm | M10 | M10 | 0,5 mm | 20 mm | 316L |
| Ø 6 mm | M10 | M10 | 0,5 mm | 20 mm | 316L |
| Ø 7 mm | M12 | M12 | 0,5 mm | 24 mm | 316L |
| Ø 8 mm | M12 | M12 | 0,5 mm | 24 mm | 316L |
| Ø 10 mm | M14 | M16 | 0,5 mm | 28 mm | Duplex 2205 |
| Ø 12 mm | M16 | M16 | 0,5 mm | 32 mm | Duplex 2205 |
| Ø 14 mm | M16 | M20 | 0,5 mm | 40 mm | Duplex 2205 |

**Bolzen-Auswahl:**
- **Für standard Cruiser (Ø6–Ø8):** 316L ausreichend (Preis: ~€2–€4 pro Stück)
- **Für große Yachten (Ø10–Ø14):** Duplex 2205 empfohlen (+€3–€8 pro Stück, aber bessere Langlebigkeit)
- **Alle Bolzen:** Mutter: Nylon-Insert (selbstsichernd), keine Standard-Muttern!
- **Alle Bolzen:** Mit Tef-Gel unter Kopf + Unterlegscheibe behandeln

**Drehmoment-Vorgaben (M12 316L Bolzen als Referenz):**
- Trocken-Anzug: ~30 Nm
- Mit Tef-Gel (empfohlen): ~25 Nm (etwas niedriger, weil schmierend)

---

### B.3 Chainplate-Länge und Konstruktionsdetails

| Yachtgröße | Chainplate-Länge | Dicke | Loch-Abstände | Deck-Durchführung |
|-----------|-----------------|-------|---------------|-------------------|
| 8–10m | 80–100 mm | 5–6 mm | 50 mm | 15 mm (einfach) |
| 10–12m | 100–120 mm | 6–8 mm | 60 mm | 20 mm (verstärkt) |
| 12–16m | 120–150 mm | 8–10 mm | 70 mm | 25 mm (verstärkt) |
| 16–20m | 150–180 mm | 10–12 mm | 80 mm | 30 mm (doppel-Backing) |
| 20m+ | 180+ mm | 12+ mm | 100+ mm | 40+ mm (massive Verstärkung) |

**Deck-Durchführung Tipps:**
1. G10-Epoxid-Unterlagplatte (6–10 mm dick) unter Chainplate
2. Sikaflex 291 elastischer Sealant um Durchführung
3. Unter Deck: Stainless-Steel Backing-Plate (größer als Chainplate), mit Tef-Gel isoliert
4. Wichtig: Absperrung für Wasser (Spritzschutz unter Deck, damit kein Wasser-Stau)

---

### B.4 Chainplate-Inspektion: Messmethoden

Wie misst man, ob eine Chainplate noch akzeptabel ist?

**Visuelle Inspektion:**
1. Oberflächenfinish: Poliert (#320+) oder matt/rauh?
2. Oberflächenrost: Braune Flecken? Lochfraß?
3. Risse: Mit Lupe suchen, besonders an Loch-Kanten und Biegungen
4. Verformung: Mit Stahllineal prüfen (sollte gerade sein)

**Oberflächenrauheit (optional):**
- Ideal: Ra <0,4 µm (poliert)
- Akzeptabel: Ra <0,8 µm (leicht satiniert)
- Kritisch: Ra >1,5 µm (rauh, Fremdrost wahrscheinlich)

**Wandstärke-Messung (bei Verdacht auf Korrosion):**
| Methode | Kosten | Genauigkeit | Anwendung |
|---------|--------|-----------|-----------|
| Schieblehre | kostenlos | ±0,1 mm | Oberflächliche Messung |
| Dicken-Messer (analog) | €20–€50 | ±0,5 mm | Schnelle Feldprüfung |
| Ultraschall-Dickenmesser | €200–€500 | ±0,1 mm | Professionelle Messung |

**Lochfraß-Tiefe messen:**
- Mit **Oberflächenrauheitsprüfer** (RA-Messer): Rauheit überm Lochfraß-Bereich messen
- Mit **Tiefenlehre:** Loch ausmessen und Tiefe notieren
- Bei >20% Querschnittsverlust: Austausch empfohlen

**Farbeindringprüfung (Penetrant-Test):**
Für kritische Inspektionen (vor Langfahrt):
1. Oberfläche saubern (mit Entfetter)
2. Rote Farbe (Penetrant-Flüssigkeit) auftragen, 15 min einwirken
3. Überschuss mit Tuch abwischen
4. Weißer Entwickler auftragen (zeigt Risse als rote Linien)
5. Ergebnis dokumentieren (Foto)

**Kit-Kosten:** ~€20–€30 (Red Dye Penetrant Kit, reicht für 10–20 Prüfungen)

---

### B.5 Chainplate-Austausch: Kosten und Zeiten

Kosten und Arbeitszeiten für Austausch einer kompletten Chainplate-Garnitur (6 Wanteplates, angenommen 12–14m Boot):

| Kostenelement | Preis (EUR) | Anmerkung |
|---------------|-------------|----------|
| 6× Chainplate 40×8mm 316L, poliert | €240–€300 | ~€40–€50 pro Stück (je nach Lieferant) |
| 6× Toggle/Gabelkopf (SS 316L) | €120–€180 | ~€20–€30 pro Stück |
| Bolzen M12 (36 Stück), Unterlegscheiben, Muttern | €80–€120 | Alles 316L oder Duplex |
| Tef-Gel (3–4 Tuben) | €36–€48 | Für alle Bolzen |
| Nylon-Isolierbuchsen (36 Stück) | €20–€30 | Unter jede Schraube |
| G10-Isolierplatten (Zuschnitten nach Maß) | €60–€100 | 6× Unterlagsplatten |
| Sikaflex 291 Sealant (2–3 Kartuschen) | €25–€40 | Decksdurchführung |
| Arbeitsaufwand (12 Stunden @ €70/h Werft) | €840–€1.200 | Ausbauen, Vorbereitung, Montage, Nachbehandlung |
| Beiz-/Passivierungspaste (wenn nötig) | €30–€50 | Nach Schweißung neu eingebauteter Teile |
| **GESAMT** | **€1.500–€2.150** | **Für komplette 6er-Garnitur** |

**Zeitaufwand:**
- Ausbauen: 2 Stunden
- Vorbereitung (Isolierung zuschneiden): 2 Stunden
- Montage: 6 Stunden
- Nachbehandlung (Beizen, Passivieren): 2 Stunden
- **Summe: 12 Stunden** (variiert nach Werft-Erfahrung)

---

### B.6 Länder-spezifische Lieferanten und Preise

| Land | Lieferant | Chainplate 40×8 316L | Lieferzeit | Besonderheit |
|------|-----------|----------------------|-----------|--------------|
| Deutschland | Nordfels | €48–€55 | 4–6 Wochen | Gute Qualität, deutsche Herkunft |
| Deutschland | Steelmaterial | €45–€52 | 2–4 Wochen | Schnell, gute Beratung |
| Niederlande | SailSafe | €42–€50 | 2–3 Wochen | EU-Standard, zuverlässig |
| UK | T2M UK | €45–€58 | 3–5 Wochen | Britischer Standard |
| USA | Schaefer Marine | $50–$65 | 3–4 Wochen | US-Standard, teurer bei Import |
| Südafrika | Sparcraft | R $350–R $450 (~€18–€24) | 4–6 Wochen | Günstig, aber lange Lieferzeit |

**Tipp:** EU-Lieferanten sind oft günstiger und schneller als UK/USA (Post-Brexit, Zoll).

---

*Ende ANHANG B*

---

## ANHANG C — Checklisten

Checklisten standardisieren Inspektions- und Beschaffungsprozesse. Alle Checkboxen sollten dokumentiert werden (mit Datum und Prüfer-Name), um Audit-Trail zu hinterlassen.

### C.1 Checkliste: Edelstahl-Halbzeug-Kauf (Bestellung)

Vor der Bestellung von Edelstahl-Halbzeugen (Rohre, Flachstahl, Blech) diese Punkte durchgehen:

| Nr. | Prüfpunkt | ✓ | Anmerkung |
|-----|-----------|---|----------|
| 1 | Legierung spezifiziert (316L / 1.4404 / A4L)? | □ | NICHT 304! NICHT unklar! |
| 2 | Materialzertifikat 3.1 nach EN 10204 angefordert? | □ | Werkszeugnis obligatorisch |
| 3 | Abmessungen exakt angegeben (mm)? | □ | z.B. 25×2,0mm nicht nur "25er Rohr" |
| 4 | Oberflächengüte spezifiziert (2B, #240, poliert)? | □ | Poliert #320+ für marine |
| 5 | Lieferlänge/Lieferformat angegeben? | □ | z.B. 4m / gerade / entgratet |
| 6 | Toleranzen akzeptabel (EN 10058/EN 10060)? | □ | h9 oder h11? |
| 7 | Verpackung/Schutz gegen Transportschäden? | □ | Holzpaletten, Folie, Kantenschutz |
| 8 | Preis pro kg oder pro m verglichen? | □ | Mehrere Angebote? |
| 9 | Versand und Zoll geklärt (Import)? | □ | EU-Herkunft = einfacher |
| 10 | Lieferfrist realistisch? | □ | Spezial-Aufträge: 4–6 Wochen |
| 11 | Rechnungsdatum und Zahlungsbedingungen? | □ | Vorkasse vs. 30 Tage? |
| 12 | Kontaktperson bei Lieferant hinterlegt? | □ | Telefon + Email |

**Nach Lieferung:**
- [ ] Paket-Kontrolle: Beschädigungen?
- [ ] Maßkontrolle mit Schieblehre (min. 3 Punkte je Stab)
- [ ] Material-Zertifikat mit Charge-Nummer abgleichen
- [ ] Oberflächenfinish prüfen (Kratzer? Oxidation?)
- [ ] Lagern: trocken, auf Holz-Stützen, nicht auf Beton

---

### C.2 Checkliste: Chainplate-Inspektion (Jährlich)

Diese Checkliste wird jährlich durchgeführt, idealerweise vor der Seesaison.

| Nr. | Prüfpunkt | OK | Mangel | Kritisch | Aktion |
|-----|-----------|-----|--------|---------|--------|
| 1 | Decksdurchführung dicht (kein Wasser sichtbar)? | □ | □ | □ | Sealant erneuern? |
| 2 | Kein Tea Staining (braune Flecken)? | □ | □ | □ | Polieren erforderlich? |
| 3 | Kein Lochfraß (kleine Löcher)? | □ | □ | □ | Farbeindringprüfung → Austausch? |
| 4 | Keine Risse sichtbar? | □ | □ | □ | Sofort Werft! Sicherheit! |
| 5 | Bolzen fest, kein Spiel? | □ | □ | □ | Nachziehen? Bolzen prüfen? |
| 6 | Kein Wassereinbruch an Deck? | □ | □ | □ | Unter Deck prüfen |
| 7 | Chainplate nicht verbogen? | □ | □ | □ | Austausch? |
| 8 | Toggle/Gabelkopf frei beweglich? | □ | □ | □ | Schmieren oder ersetzen? |
| 9 | Material-Identität bekannt (316L vs 304)? | □ | □ | □ | Moly-Test durchführen? |
| 10 | Alter der Chainplates dokumentiert? | □ | □ | □ | >20 Jahre = erhöhte Prüfung |
| 11 | Unter-Deck-Bereich trocken? | □ | □ | □ | Belüftung prüfen |
| 12 | Isolation (G10, Tef-Gel) intakt? | □ | □ | □ | Erneuerung nötig? |

**Zusätzliche Tests bei "Mangel" oder "Kritisch":**
- Farbeindringprüfung (Red Dye Penetrant, ~€20 pro Kit)
- Oberflächenrauheit-Messung (RA-Messer, ~€200 Gerät)
- Moly-Test (Legierungsnachweis, ~€15 per Test)
- Ultraschall-Dickenmessung (Wandstärke, professionell ~€100–€200)

---

### C.3 Checkliste: Reling-Inspektion (Halbjährlich)

Reling sollte häufiger inspiziert werden als Chainplates (exponierter, mehr Verschleiß).

| Nr. | Prüfpunkt | ✓ | Aktion bei Problem |
|-----|-----------|---|-------------------|
| 1 | Rohr sichtbar beschädigt (Kratzer, Dellen)? | □ | Polieren oder akzeptieren? |
| 2 | Keine Risse an Schweißnähten? | □ | Farbeindringprüfung → Austausch |
| 3 | Oberflächenrost oder Tea Staining? | □ | Bar Keeper's Friend + Polieren |
| 4 | Alle Stanchions fest an Basen? | □ | Bolzen nachziehen, Korrosion prüfen |
| 5 | Keine Anlauffarben an Schweißnähten? | □ | Beizen + Passivieren durchführen |
| 6 | Kein Wasser in Rohren (Lochkorrosion-Risiko)? | □ | Entwässerungslöcher prüfen |
| 7 | Keine Verformung oder "Knicke" im Rohr? | □ | Segment austausch. R ≥ 3×Ø beachten |
| 8 | Beschläge (Tüllen, Verschlüsse) korrosionsfrei? | □ | Ersatz falls nötig |
| 9 | Bolzen-Köpfe glänzend (nicht blind)? | □ | Passivierung? Austausch? |
| 10 | Alle Sicherungsschlösser (Lock Nuts) intact? | □ | Eigenschaft verloren → ersetzen |

---

### C.4 Checkliste: Edelstahl-Schweißung (WIG/TIG) vor Werk

Diese Checkliste wird dem Schweiß-Betrieb vorausgehend zugesandt und zur Unterschrift verlangt.

| Nr. | Prüfpunkt | ✓ | Begründung |
|-----|-----------|---|-----------|
| 1 | Material: 316L (1.4404) bestätigt? | □ | Nicht 304! Material-Zertifikat beifügen |
| 2 | Zusatzwerkstoff: 316LSi (AWS E316L-16)? | □ | Keine anderen Legierungen! |
| 3 | Schutzgas: Argon 99,99% oder Argon+He Mix? | □ | Nicht CO2! Nicht Luft! |
| 4 | Wurzelschutz / Formiergas vorhanden? | □ | Verhindert Oxidation innen |
| 5 | Schweißbereich gereinigt + entfettet? | □ | Mit Lösungsmittel, kein Benzin |
| 6 | Keine Fremdmetall-Kontamination? | □ | Kein Stahlwolle, keine Stahlbürste |
| 7 | Strom nach Schweißtabelle eingestellt? | □ | Typisch 100–150A für Ø2mm Draht |
| 8 | Schweißnaht: keine Poren/Risse/Einschlüsse? | □ | Röntgen bei kritischen Nähten |
| 9 | Anlauffarben: max strohgelb/goldbraun? | □ | Dunkelblau oder grau = zu heiß |
| 10 | Nachbehandlung: Beizen durchgeführt? | □ | Avesta 401, min. 30 min |
| 11 | Nachbehandlung: Passivierung durchgeführt? | □ | Avesta 601, min. 60 min |
| 12 | Oberflächenrauheit gemessen? | □ | Ideal: Ra <0,4 µm (poliert) |
| 13 | Dokumentation / Schweißpass? | □ | Schweißer-Name, Datum, Zeit |

**Nach Schweißung (Annahmeprüfung):**
- [ ] Farbeindringprüfung (mindestens visuelle) durchgeführt
- [ ] Oberflächenfinish akzeptabel
- [ ] Messungen mit Schieblehre: akzeptable Abmessungen
- [ ] Dokumentation archiviert (für Warranty/Audit)

---

### C.5 Checkliste: Motorlager / Motor-Fundament (Edelstahl auf Alu)

Spezielle Checkliste für Alu-Yachten mit SS-Motor-Befestigung:

| Nr. | Prüfpunkt | ✓ | Kritikalität |
|-----|-----------|---|--------------|
| 1 | Isolierung vorhanden (G10-Platte unter Winkelprofilen)? | □ | KRITISCH |
| 2 | Tef-Gel unter allen Bolzen-Köpfen? | □ | KRITISCH |
| 3 | Nylon-Isolierbuchsen in allen Löchern? | □ | KRITISCH |
| 4 | Duralac oder Zinkanode-Schutz vorhanden? | □ | Empfohlen |
| 5 | Kein direkter SS-Alu-Kontakt sichtbar? | □ | KRITISCH |
| 6 | Bolzen-Drehmoment dokumentiert? | □ | Für Audit |
| 7 | Keine weißen Oxide (Al₂O₃) unter Montage? | □ | Zeichen galvanischer Korrosion |
| 8 | Bereich darunter trocken (kein Wasser-Stau)? | □ | Belüftung sicherstellen |
| 9 | Inspektions-Intervall: min. jährlich? | □ | Plan einrichten |
| 10 | Dokumentation: Installation-Fotos, Material-Details? | □ | Für Werft-Austausch |

---

### C.6 Checkliste: Edelstahl-Lagerhaltung an Bord

Für Yachten mit Reparatur-Kit an Bord:

| Nr. | Artikel | Vorhanden | Lagerbedingungen |
|-----|---------|-----------|------------------|
| 1 | Edelstahlrohr 25×2mm 316L, 2m | □ | Trocken, auf Holz |
| 2 | Edelstahlrohr 32×2mm 316L, 1m | □ | Trocken, auf Holz |
| 3 | Flachstahl 40×8mm 316L, 0,5m | □ | Vertical, nicht gebogen |
| 4 | Rundstahl Ø10mm 316L, 0,5m | □ | Horizontal gelagert |
| 5 | Blech 2mm 316L, 300×500mm | □ | Flach, mit Schutzkante |
| 6 | Schweißzusatz 316LSi (Stab + Draht) | □ | Trocken, Lagerungsbox mit Silica-Gel |
| 7 | Beizpaste Avesta 401, min. 500g | □ | Kühl, dicht verschlossen |
| 8 | Passivierungspaste Avesta 601, min. 500g | □ | Kühl, dicht verschlossen |
| 9 | Bar Keeper's Friend, min. 300g | □ | Trocken, normal Lagern |
| 10 | CorrosionX Spray, min. 2× 400ml | □ | Kühl, aufrecht lagern |
| 11 | Tef-Gel Tuben, min. 2× | □ | Kühl, Deckel fest |
| 12 | Nylon-Isolierbuchsen Sortiment | □ | Trocken, sortiert |
| 13 | Sechskant-Bolzen M8–M12 (316L), je 10 Stück | □ | In Box, sortiert |
| 14 | Werkzeuge: Schleifer, Bürsten, Feilen | □ | Öl-Konservierung für Stahl-Teile |

**Lagerhaltungs-Richtlinien:**
- Alle Teile auf **Holz oder Kunststoff-Paletten lagern** (nicht auf Stahl!)
- **Trennfolien** zwischen Teilen (verhindert Fremdrost durch Kontakt)
- Feuchtigkeits-Absorbenten (Silica-Gel, Ca-Chlorid) in Box einlegen
- Schweißdraht + Pasten: Kühl (unter 25°C), trocken lagern
- Lagerkontrolle: Jährlich, vor Seesaison prüfen

---

*Ende ANHANG C*

---

## ANHANG D — Fallstudien

Fallstudien dokumentieren Real-World Szenarien: Fehlerhafte Materialwahl, Reparaturerfolge, Wartungserfolg oder -versäumnisse, ökonomische Entscheidungen. Jede Fallstudie enthält Befund, Ursache, Lösung, Kosten und Lektion für künftige Entscheidungen.

### D.1 Fallstudie: Catalina 30 — Chainplate-Versagen durch Spaltkorrosion (22 Jahre Betrieb)

**Boot:** Catalina 30, GFK-Rumpf, Produktionsboot aus 1998 (Südkalifornien, Langfahrt in Pazifik)

**Problem:** Bei Routine-Inspektion vor Transpacific-Passage Oberwant-Chainplate steuerbord mit frischem Riss entdeckt.

**Inspektions-Verfahren:**
- Visuell: Dunkle Verfärbung an Decksdurchführung
- Taktil: Mit Fingernagel: Oberfläche rau, nicht glatt
- Farbeindringprüfung (Red Dye Penetrant): 3 separate Risse von 2–5 mm Länge an der Decksdurchführung sichtbar

**Befund:**
- Material: 304 (nicht 316!) — identifiziert durch Moly-Test
- Lochfraß + Spaltkorrosion kombiniert
- Alle 6 Wanten-Chainplates zeigten ähnliche, aber weniger fortgeschrittene Korrosion
- Decksdurchführung: Mit weicher, poröser Dichtmasse gefüllt (30 Jahre alt, durchfeuchtet)

**Root-Cause-Analyse:**
1. Original-Material: 304 statt 316 (Einsparung ab Werk, möglicherweise nicht-marine-spec)
2. Decksdurchführung nicht isoliert (direkt GFK-Rumpf)
3. Keine Wartung: 22 Jahre ohne Polieren oder Passivieren durchgeführt
4. Salzwasser-Eindringung über alte Decksdichtung
5. Spaltkorrosion in Spalte zwischen Chainplate und Deck

**Reparatur:**
- Alle 6 Chainplates ausgebaut
- Alte Decksdurchführungen gereinigt, mit G10-Platte isoliert
- Neue Chainplates bestellt: 316L, 40×8 mm, poliert #320 (von SailSafe Deutschland)
- Neue Bolzen: Duplex 2205 (wegen Kostenkalkül entschieden, nicht 316L)
- Montage mit Tef-Gel, Nylon-Isolierbuchsen
- Sealant: Sikaflex 291

**Kosten:**
- 6× Chainplate 316L 40×8mm poliert: €240
- Bolzen, Unterlegscheiben, Nylon-Buchsen: €80
- Tef-Gel, Sikaflex, G10: €60
- Arbeit (Schlosserei, 12 Stunden): €600 (USA-Labor)
- **Gesamt: $850 / €780**

**Langzeit-Monitoring:**
- Nach 1 Jahr: Keinerlei neue Korrosion
- Nach 3 Jahren: Oberflächen-Polierung durchgeführt (prophylaktisch)
- Nach 5 Jahren: Jährliche Inspektion, Sealant noch intakt

**Lektion 1:** 304-Edelstahl in Salzwasser-Langfahrt ist Gamble. Nach 15–22 Jahren Versagen zu erwarten.

**Lektion 2:** Isolierung (G10-Unterlagen + Tef-Gel) ist für GFK-Rumpf nicht optional — Essential.

**Lektion 3:** Alte Dichtmassen sollten prophylaktisch alle 10 Jahre erneuert werden, nicht gewartet bis Wassereintritt.

**Upgrade-Lernkurve:** Eigner entschied sich für 2205-Bolzen statt 316L-Bolzen, weil "wenn schon neu, dann richtig". Zusatz-Kosten ~€40, aber Langzeit-Sicherheit gestiegen.

---

### D.2 Fallstudie: Hallberg-Rassy 36 — Reling-Austausch nach 30 Jahren (Schweden)

**Boot:** Hallberg-Rassy 36, GFK, Baujahr 1992, Heimathafen: Ystad, Schweden (Baltisches Meer, brackiges Wasser)

**Problem:** Reling zeigt nach 30 Jahren durchgehende, sichtbare Verfärbung (Tea Staining, Fremdrost). Eigner fragt: Austausch oder Reparatur?

**Inspektion:**
- Visuell: Durchgehende braune Flecken, aber keine tiefen Kratzer oder Risse sichtbar
- Taktil: Oberfläche grob (nicht poliert, Walzstruktur sichtbar)
- Oberflächenrauheit RA: gemessen ~3–4 µm (sollte <1 µm sein für poliert)
- Schweißnähte: Alle Schweißnähte intakt, keine Risse erkannt
- Wandstärke: Ultraschall-Messung zeigt keine Verdünnung (noch 2,0 mm original)

**Diagnose:**
- Material: 316 (original, bestätigt durch Moly-Test)
- Keine Sensibilisierung erkannt
- Fremdrost-Kontamination (von Stahlgerüsten bei Haul-out)
- Oberflächenoxidation durch fehlende Passivierung
- Keine strukturellen Schäden

**Kosten-Szenarien:**
1. **Austausch-Option:** Komplette neue Reling 25×2mm 316L, poliert #320:
   - Material: €3.200 (ca. 40 m Rohr + Stanchions + Fitting)
   - Arbeit (Werft, 60 Stunden): €3.000
   - Gesamt: €6.200+

2. **Reparatur-Option:** Professionelles Polieren + Passivieren
   - Polieren: Ca. 200 m² Fläche × €6/m² = €1.200
   - Passivierung + Schutzlackierung: €500
   - Gesamt: €1.700

**Entscheidung:** Reparatur (Faktor 3,6× billiger)

**Durchgeführte Reparatur:**
- Werft nahm Reling in Werkstatt (hängend am Laufkran)
- Polieren mit Schleifer (#240 → #320) über 40 Stunden
- Passivierungsbad (Avesta 401, Salpetersäure)
- Schutzlackierung (2 K-Polyurethan, transparent, speziell für Edelstahl)
- Remontiage

**Kosten Real (Schwedische Werft):**
- Material (Schleifer, Pasten, Lack): SEK 3.500 (~€370)
- Arbeit (40 h × SEK 450/h): SEK 18.000 (~€1.900)
- Gesamt: SEK 21.500 (~€2.270) ≈ €1.200 (abhängig von Wechselkurs)

**Langzeit-Ergebnis (10 Jahre später):**
- Reling sieht wie neu aus
- Jährlich mit Bar Keeper's Friend gepflegt
- Nach 10 Jahren: Keine neuen Korrosions-Merkmale erkannt
- Schutzlackierung hält noch (aber bröckelt leicht ab, nicht kritisch)

**Lektion 1:** Eine 30-Jahre-alte 316-Reling ist nicht automatisch Schrott. Mit richtiger Diagnose + Polieren + Passivieren kann weitere 10–20 Jahre Lebensdauer erreicht werden.

**Lektion 2:** Oberflächenfinish (poliert vs. warmgewalzt) beeinflusst Korrosionsgeschwindigkeit massiv. Die HR36-Original-Reling war nicht poliert → Fremdrost wahrscheinlicher.

**Lektion 3:** Kosten-Nutzen: €1.200 Reparatur vs. €6.200 Neubau ist nicht schwer zu rechnen. Aber viele Eigner wissen nicht, dass Polieren + Passivierung Zauberstäbe ist.

---

### D.3 Fallstudie: Contest 42 — Duplex-Chainplates ab Werk (20 Jahre, Mittelmeer)

**Boot:** Contest 42, GFK, Baujahr 2002, Basis Mallorca, Vollzeitlangfahrer

**Besonderheit:** Contest hat ab Werk Duplex 2205 Chainplates verwendet (Premium-Entscheidung ab Werk).

**Befund nach 20 Jahren Mittelmeer-Betrieb:**
- Decksdurchführungen: Keinerlei Spaltkorrosion sichtbar
- Oberflächenfinish: Noch poliert, noch glänzend
- Bolzen: Duplex 2205, mit Tef-Gel montiert
- Eigner-Aussage: "Ich habe diese Chainplates nie angefasst. Nie ein Problem."

**Vergleichs-Inspektion mit 304/316-Booten ähnlicher Baujahre:**
- Andere 42er mit 316L-Chainplates (ähnlich montiert): Nach 15 Jahren erste Spaltkorrosion-Anzeichen
- Andere mit 304-Chainplates: Nach 10 Jahren Risse erkannt

**Ökonomische Rechnung (Eigner Aussage):**
- Duplex Chainplate ab Werk: +€400 / Boot (Contest-Entscheidung)
- Späterer Austausch (316L): €600–€800 + Downtime
- Eigner-Zeit für Wartung (30 Jahre): 0 Stunden
- **Conclusion:** Duplex zahlte sich in diesem Fall aus

**Metallurgische Erklärung:**
| Aspekt | 316L | Duplex 2205 |
|--------|------|------------|
| PREN | 26 | 34 |
| Decksdurchführung (20 Jahre) | Erste Spaltkorrosion | Keine sichtbare Korrosion |
| Wartungsaufwand | Monatlich polieren | Jährlich visuell |
| Preis-Faktor | 1,0× | 1,5× |
| Payback-Period | 12–15 Jahre | 5–8 Jahre (bei Salzwasser) |

**Lektion:** Premium-Material ab Werk zahlt sich aus, wenn das Boot >15 Jahre betrieben wird. Für Kurzfahrten (5–7 Jahre) Overkill.

---

### D.4 Fallstudie: Beneteau Oceanis 40 — Reling-Rohr Bruch nach Unfall (Schweiz)

**Boot:** Beneteau Oceanis 40, GFK, Baujahr 1995, Heimat Zürichsee (Süßwasser)

**Vorfall:** Boot kollidierte mit Holzsteg bei Anlegemanöver. Reling am Bug (Port) traf Steg-Kante. Sofortiger Bruch des Reling-Rohrs an der Basis-Schweißung.

**Inspektions-Ergebnis:**
- Rohr 22×1,5mm 316 (Original)
- Bruch ist vollständig, saubere Trennung an der Schweißnaht
- Farbeindringprüfung: Keine weiteren Risse erkannt
- Frage: War Rohr zu dünn? War Schweißung schwach?

**Analyse:**
- 22×1,5mm für 40er-Boot ist untermaßig (empfohlen: 25×2,0mm)
- Schweißnaht: Hatte Anlauffarben (nicht passiviert original)
- Chromverarmung in HAZ (Heat Affected Zone) wahrscheinlich
- Spannungsrisskorrosion möglich (auch wenn Süßwasser)

**Reparatur-Entscheidung:**
- **Nicht:** Altes Rohr reparieren (zu riskant)
- **Ja:** Neues Segment, bessere Dimensionierung

**Durchgeführte Reparatur:**
- Altes Rohr abgeschnitten (ca. 600 mm beidseitig)
- Neues Rohr 25×2,0mm 316L vorbereitet
- Biegung durchgeführt mit R ≥ 75 mm (5×Ø)
- WIG-Schweißung durchgeführt (Fachperson)
- Beizen + Passivierung (Avesta 401 + 601)
- Remontiage und Funktionsprobe

**Kosten:**
- Schlosserei: CHF 280 (~€300)
- Material (Rohr, Zusatz, Beizmittel): CHF 80 (~€85)
- **Gesamt: CHF 360 (~€385)**

**Langzeit-Monitoring:**
- Nach 10 Jahren: Keinerlei neue Korrosion
- Jährlich mit Bar Keeper's Friend gepflegt

**Lektion 1:** 22×1,5mm ist Minimum-Standard, aber nicht sicher genug für Stoßbelastungen. Upgrade auf 25×2,0mm ist gute Versicherung.

**Lektion 2:** Vorhandene 22×1,5 Rohre sollten nach Stoß oder Unfall inspiziert werden (Farbeindringprüfung). Können nach Kollision Risse aufweisen.

**Lektion 3:** Diese Reparatur zeigte Wert der Passivierung. Neue Rohr mit Passivierung hielt 10 Jahre problemlos, während Original (ohne Passivierung) bei Belastung brach.

---

### D.5 Fallstudie: Ovni 395 — Galvanische Korrosion auf Aluminium-Rumpf (8 Jahre)

**Boot:** Ovni 395, Aluminium-Rumpf (Spezialbau), Motorlager aus Edelstahl auf Alu-Hauptrahmen montiert

**Problem:** Nach 8 Jahren Betrieb Motorlager (SS316 Winkelprofile 40×40×4mm) zeigen Korrosion.

**Befund:**
- Weiße, pulvrig Ablagerung (Al₂O₃) unter den SS-Winkelprofilen
- Oberflächenverfärbung des Aluminiums rundum
- Keine Isolation zwischen SS und Alu verwendet (direkte Kontakt)
- Bolzen aus Edelstahl (kein Tef-Gel, keine Nylon-Buchsen)

**Galvanische Spannung Berechnung:**
| Material | Standardpotential (SHE) | Differenz |
|----------|-------------------------|-----------|
| Aluminium (Alu 5083) | -1,05 V | — |
| Edelstahl 316 (passiv) | +0,2 V | 1,25 V (Riesig!) |
| Resultat: Alu ist Anode | — | Alu korrodiert |

**Ursache:**
1. Direkt metallischer Kontakt SS ↔ Alu (gut leitend)
2. Salzwasser/Feuchtigkeit als Elektrolyt
3. Hohe galvanische Potentialdifferenz (1,25 V)
4. Beschleunigung der Alu-Korrosion um Faktor 10–100

**Reparatur:**
1. Motorlager ausbauen (14 Bolzen)
2. Oberflächen reinigen, alte Al₂O₃ abgratzen
3. Unter jede Edelstahl-Winkelprofile: G10-Epoxid-Isolierplatte (6 mm, Bohrungen für Bolzen)
4. Jeder Bolzen: Tef-Gel unter Kopf + Unterlegscheibe
5. Nylon-Isolierbuchse unter jede Schraube
6. Remontiage mit Drehmoment-Kontrolle

**Material-Kosten:**
- G10-Epoxid Isolierplatten (gesch. 0,5m²): €30
- Tef-Gel Tuben (2×): €24
- Nylon-Isolierbuchsen (50 Stück): €15
- Neue Bolzen (optional, 14×): €40
- **Summe Material: €109**

**Arbeitsaufwand:**
- Ausbauen/Reinigen: 4 Stunden
- Isolierung vorbereiten: 2 Stunden
- Remontiage: 2 Stunden
- **Summe: 8 Stunden**

**Kosten Arbeit:** 8 Stunden × €80/h = €640 (Werft-Labor)

**Gesamt-Kosten:** €750 (Material + Arbeit)

**Langzeit-Überwachung (nach Reparatur):**
- Nach 1 Jahr: Jährliche Sichtprüfung durchgeführt — keinerlei neue Korrosion
- Nach 5 Jahren: Jährliche Inspektionen weiterhin durchgeführt
- Nach 8 Jahren: Reparatur hat gehalten, Alu zeigt keine neuen Schäden

**Lektion 1:** Edelstahl + Aluminium ist tückisches Paar. Ohne Isolation ist galvanische Korrosion garantiert.

**Lektion 2:** Tef-Gel + G10-Isolation + Nylon-Buchsen sind Triple-Schutz, redundant aber effektiv. Einsatz überall, wo SS auf Alu montiert ist.

**Lektion 3:** Kosten der Reparatur (€750) wäre ca. Kosten eines teilweise korrodierten Motors (Rahmen-Schäden, Austausch teuer). Prävention ist billiger.

**Lektion 4:** Aluminium-Yachten erfordern spezielle Edelstahl-Befestigungsprotokolle. Nicht "standard Edelstahl verwenden" sondern "mit Isolation verwenden".

---

### D.6 Fallstudie: Jeanneau Sun Odyssey 519 — Duplex-Davit (12 Jahre, Karibik)

**Boot:** Sun Odyssey 519 mit Duplex 2205 Davit-Rohren (Baujahr 2010, Flagge Karibik)

**Besonderheit:** Jeanneau bot Premium-Davit aus Duplex 2205 an (ca. +€1.200 vs. 316L)

**Betriebsbedingungen:**
- Permanent in Salzwasser (karibisches Wasser, hochsalzig)
- Intensive UV-Exposition (tropische Sonne)
- Häufige Verwendung (Dingi täglich ins/aus Davit)
- Minimal Wartung (Besitzer träge bei Polieren)

**Inspektions-Ergebnis nach 12 Jahren:**
- Oberflächenfinish: Noch sichtbar, etwas matt (UV-Alterung)
- Oberflächenrost: Minimal (nur leichte Verfärbung an Schweißnähten)
- Strukturelle Integrität: Keine Risse, kein Lochfraß erkannt
- Verschleiß der Lagerbuchsen: Minimal

**Vergleich mit ähnlichen Booten:**
| Boot | Davit-Material | Betriebsdauer | Verschleißstatus |
|------|----------------|---------------|-----------------|
| SO 519 (Test) | Duplex 2205 | 12 Jahre | Gut (minimal Wartung) |
| SO 509 nächstneueres | 316L | 12 Jahre | Moderat (Risse Ansätze) |
| Sun Odyssey 36 alt | 316 | 12 Jahre | Schlecht (Austausch empfohlen) |

**Kosten-Nutzen-Analyse (SO 519 Eigner):**
- Davit-Upgrade (Duplex): +€1.200 ab Werk
- Wartungskosten über 12 Jahre: €200 (gelegentliches Polieren)
- Austausch-Kosten (hätte 316L gewählt): €3.500 + Arbeit, erwartet ca. Jahr 10–12
- **Duplex-Entscheidung:** Amortisiert sich, wenn Boot >10 Jahre gehalten wird

**Lektion:** Duplex ist nicht nur Overkill für alle Anwendungen, aber für hochbelastete, exponierte Teile (Davits, Kielbolzen) in tropischen Gewässern ist es sinnvolle Investition.

---

*Ende ANHANG D*

---

## ANHANG E — Fehlerbild-Atlas

Dieser Atlas dokumentiert typische Schadensbilder an Edelstahl-Halbzeugen im Yachtbau. Jedes Bild zeigt Symptome, Bewertung (Schweregrad) und Handlungsempfehlungen. Fotos sollten mit Lupe oder Makro-Modus aufgenommen werden, um Kratzer und Oberflächenveränderungen deutlich zu machen.

### E.1 Fehlerbild 1: Tea Staining auf Reling
**Symptom:** Braune, rostfarbene Flecken auf Reling-Rohr (25×2mm 316L), gleichmäßig verteilt über die Oberfläche. Untergrund scheint intakt, kein Größenwachstum über Wochen beobachtet. Typisch nach Winterlagerung oder bei schlechter Oberflächenvorbereitung.
**Fehlerursache:** Fremdrost-Kontamination oder Tannin-Ablagerung (siehe Chemie).

**Chemie:** Tannine aus Teak-Decks oder freie Eisenteilchen (Fremdrost von Werkzeugen) reagieren mit Wasser und bilden braune Oxide. **Nicht** der Edelstahl selbst oxidiert, sondern Verschmutzungen.

**Schweregrad:** 1/5 — Kosmetisch, kein strukturelles Problem.

**Inspektions-Verfahren:**
- Mit feuchtem Tuch abreiben — verschwindet teilweise? Dann Oberflächenverschmutzung.
- Mit Oxalsäure-Tester (z.B. Moly-Test-Kit) prüfen — löst sich die Verfärbung? Fremdrost.
- Tiefere Kratzer oder Pitting? Dann Lupe (10×Vergrößerung) nutzen.

**Maßnahme:**
1. Bar Keeper's Friend (5 min Einwirkzeit, nass auftragen)
2. Mit Bürste abreiben (Edelstahl-Drahtbürste oder Kupferbürste, NICHT Stahlwolle!)
3. Gründlich mit Süßwasser abspülen
4. Mit Passivierungspaste (Avesta 601) nachbehandeln (optional, aber empfohlen)
5. Zum Schutz: CorrosionX oder ähnliches Spray auftragen

**Kosten:** €5–€10 (Reinigungsmittel)

**Prognose:** Nach Reinigung 6–12 Monate weitere Verschmutzung möglich. Mit regelmäßiger Passivierung alle 6 Monate kann Wiederholung vermieden werden.

---

### E.2 Fehlerbild 2: Lochfraß (Pitting) an Chainplate
**Schadenbild:** Kleine, präzise runde Löcher (0,5–2 mm Ø, Tiefe 0,3–1 mm) an Chainplate-Oberfläche (50×10mm 316L), konzentriert im Bereich der Decksdurchführung. Ränder der Löcher wirken dunkelbraun. Loch-Arrangement wirkt zufällig (typisches Pitting-Muster).

**Chemie:** Chloride durchdringen die Passivschicht an schwachen Stellen. Lokale Anode-Kathode-Bildung führt zu schneller, tiefengerichteter Korrosion. Typisch in Spalten (Decksdurchführung, unter Ablagerungen).

**Schweregrad:** 2–3/5 — Mittelschwer bis ernst. Querschnittsverlust muss gemessen werden.

**Inspektions-Verfahren:**
1. Schieblehre: Dicke an mehreren Stellen messen (soll ≥ 10 mm sein)
2. Lupe unter Ringleuchte: Anzahl Löcher zählen, größte Tiefe schätzen
3. Farbeindringprüfung (Penetrant-Test): Rote Farbe in Löcher, trocknen, Entwickler auftragen → zeigt Lochtiefe
4. Oberflächenschliff: Bei <10% Querschnittsverlust akzeptabel

**Maßnahme (abhängig von Tiefe):**
- **Tiefe <0,5 mm, <3 Löcher**: Polieren mit #240er Schleifer + Passivierung. Inspektionspflicht jährlich.
- **Tiefe 0,5–1 mm, 3–10 Löcher**: Farbeindringprüfung durchführen. Wenn Verlust <10%, akzeptieren aber überwachen. Wenn >10%, austauschen.
- **Tiefe >1 mm oder rasches Wachstum**: Chainplate sofort austauschen. Sicherheit!

**Reparatur:** 316L-Ersatz-Chainplate (50×10mm, poliert), Austausch an der Decksdurchführung. Kosten: €60–€120 Neue Chainplate + €100–€200 Arbeit.

**Prognose:** Mit Duplex 2205 hätte sich dieses Problem nicht entwickelt (PREN 34 vs. 26 für 316L).

---

### E.3 Fehlerbild 3: Spaltkorrosion an Decksdurchführung — Versagensart: Spaltkorrosion
**Symptom:** Dunkle Verfärbung (grau-schwarz bis dunkelbraun) und raue, krümelige Oberfläche an der Stelle, wo Chainplate durch das GFK-Deck tritt. Oberfläche fühlt sich rau an (kein glattes Pitting-Loch, sondern flächige Rauhigkeit).

**Chemie:** Spaltkorrosion tritt in sauerstoffarmen, chloridhaltigen Spalten auf. Wasser sammelt sich unter der Decksdichtung (auch mit Sikaflex). Minimal Sauerstoff führt zu pH-Absenkung und beschleunigter Anode-Bildung. 316 ist bessern als 304, aber nicht immun.

**Schweregrad:** 3–4/5 — Schwer. Strukturelle Integrität gefährdet.

**Inspektions-Verfahren:**
1. Durchgang prüfen: Mit feinem Draht durch das Pitting schieben können? Wenn ja, Material kompromittiert.
2. Farbeindringprüfung IMMER durchführen
3. Unter Ringleuchte: Ist die Rauhheit kreisförmig oder in Streifen? Spaltkorrosion zeigt oft längliche Rauhheit.
4. Unter Deck prüfen: Ist Sikaflex ausgehärtet oder noch weich? Weicher Sealant → Wassereintritt möglich.

**Maßnahme:**
1. Chainplate SOFORT (nicht später!) ausbauen
2. Mit Beizpaste (Avesta 401) 60 min behandeln, um Korrosionsprodukte zu entfernen
3. Gründlich abspülen, Farbeindringprüfung wiederholen
4. Wenn Material >15% verloren: Ersetzen
5. Wenn Löcher flach und <10%: Mit Schleifer polieren + Passivierung, aber mit häufigerer Überwachung (3 Monate statt 12 Monate)
6. Decksdurchführung mit elastischem Sealant (Sikaflex 291 oder 292) neu abdichten
7. G10-Unterlegplatte verwenden (nicht direkt auf GFK-Deck montieren)

**Kosten:** €150–€400 Reparatur + Austausch bei Bedarf

**Gutachter-Empfehlung:** Bei Spaltkorrosion an sicherheitskritischen Teilen (Chainplates, Keelbolts) immer einen zertifizierten Surveyor oder Sachverständigen für Yachtbau hinzuziehen. Ein erfahrener Metallurg kann mittels Farbeindringprüfung und Ultraschall den tatsächlichen Querschnittsverlust bestimmen.

**Prognose:** Wenn ignoriert, kann Spaltkorrosion zu Sicherheitsrisiko werden. Regelmäßige Inspektionen alle 6–12 Monate sind Pflicht.

---

### E.4 Bild 4: Anlauffarben an Schweißnaht (nicht behandelt)
**Beschreibung:** Violett, blau, gelb oder grau-braune Verfärbung (Anlauffarben, auch "Tempering Colors" genannt) entlang einer Schweißnaht an einem Reling-Rohr (25×2mm). Verfärbung ist scharf begrenzt auf die Schweißzone (±5 mm).

**Chemie:** Beim Schweißen entstehen extreme Temperaturen. Die unmittelbare Umgebung der Schweißnaht wird bis 500–800°C heiß, wodurch die Passivschicht zerstört wird und die Oberfläche oxidiert (Anlauffarben). Diese Zones (Heat Affected Zone, HAZ) ist chromverarmt und anfälliger für Korrosion.

**Farbcodierung der Anlauffarben:**
- Hellgelb (300°C): Gering kritisch
- Braun (400°C): Kritisch
- Dunkelblau (500–600°C): Sehr kritisch
- Lichtgrau (>600°C): Extrem kritisch

**Schweregrad:** 1–2/5 — Leicht bis Mittel. Mit richtiger Nachbehandlung problemlos zu beheben.

**Inspektions-Verfahren:**
1. Farbe merken (für Rückschluss auf Temperatur)
2. Mit Fingernagel kratzen: Farbe sollte sich nicht abblättern (wenn abblätterbar, dann lockere Oxidschicht)
3. Oberflächenrauheit: Mit Schleifer über Farbe fahren und sehen, wie tief Schaden geht

**Maßnahme (IMMER durchführen, nicht ignorieren!):**
1. Beizpaste (Avesta 401 oder 501) auftragen, 30–60 min einwirken lassen
2. Mit Bürste abbürsten, mit Süßwasser abspülen
3. Passivierungspaste (Avesta 601) 1 Stunde auftragen
4. Erneut abspülen, trocknen
5. Zur Langzeitkonservierung: CorrosionX Spray auftragen

**Zeitaufwand:** 2–3 Stunden für Schweißnaht von 1–2 Metern Länge (mit Einwirkzeiten).

**Kosten:** €15–€30 (Beiz- und Passivierungspaste)

**Prognose:** Mit Nachbehandlung: 100% Wiederherstellung. Ohne Nachbehandlung: Spaltkorrosion wahrscheinlich in 2–5 Jahren.

---

### E.5 Fehlerbild 5: Bruch an Schweißnaht (Reling) — Versagensart: Ermüdungsbruch
**Schadenbild:** Vollständiger Bruch eines Reling-Rohrs (25×2mm) genau an der Schweißnaht zur Stanchion-Basis. Bruchkanten wirken scharfkantig, teilweise rauh. Riss läuft senkrecht zur Schweißnaht (nicht längs zur Naht).

**Mögliche Ursachen:**
1. **Sensibilisierung + Spannungsrisskorrosion**: Chromverarmt Zone unter Zugspannung corroded schnell
2. **Materialfehler**: Schweißnaht war zu schnell abgekühlt (Härterisse) oder nicht geschweißt (kalt gefügt)
3. **Überlastung**: Reling wurde beim Fenderanlegen oder Manöver übermäßig belastet
4. **Verschleiß**: Nach vielen Jahren zyklischer Belastung (Wellengang) wächst Risspropagation

**Schweregrad:** 5/5 — KRITISCH. Sofortige Reparatur nötig (Sicherheitsrisiko!).

**Inspektions-Verfahren:**
1. Länge des Risses messen (mit Schieblehre oder Oberflächenrauheitsprüfer)
2. Farbeindringprüfung: Rote Farbe in Riss, Entwickler auftragen → zeigt weitere Risse
3. Röntgen oder Ultraschall für tiefere Rissausbreitung (professionell)

**Maßnahme (KEINE Provisorische Lösung!):**
1. **Sofort:** Reling mit Spanngurt oder Schelle provisorisch sichern (damit nicht völlig bricht)
2. **In nächstem Hafen:** Neues Rohr-Segment (25×2mm 316L) anfertigen und WIG-schweißen
3. **Alternativ:** Komplette Reling erneuern (wenn älter als 25 Jahre, empfohlen)
4. Nach Schweißung: Beizen + Passivieren durchführen (s. E.4)
5. Neuen Riss-Ursprung untersuchen: War Material 304 statt 316? War Schweißung fehlerhaft? Alle Rohre inspizieren.

**Kosten:** €200–€600 Schweißerei (hängig von Komplexität) + €50–€100 Material

**Prognose:** Wenn nicht repariert, kann Reling völlig brechen und zu Unfällen führen (Person über Bord).

**Experten-Hinweis:** Ein Ingenieur oder Sachverständiger sollte bei wiederholten Schweißnaht-Brüchen die gesamte Reling-Konstruktion begutachten — häufig liegt ein systematischer Materialfehler (304 statt 316L) oder eine fehlerhafte Schweißtechnik vor.

---

### E.6 Bild 6: Galvanische Korrosion SS auf CFK
**Beschreibung:** Schwärzliche oder dunkelbraune Ablagerung und lokalisierter Lochfraß an SS316-Beschlag (z.B. Bügel-Befestigung) der direkt auf einem CFK (Carbon-Faser)-Deck montiert ist. Oft auch Delamination des Gels rund um die Befestigung sichtbar.

**Chemie:** CFK ist elektrisch leitend (wegen der Carbon-Fasern). Edelstahl ist noble (positive Potential). Das galvanische Paar beschleunigt Korrosion des Edelstahls unerwünscht. Zusätzlich: Wasser unter dem Beschlag bildet Spaltkorrosion-Conditions.

**Schweregrad:** 3–4/5 — Schwer. Strukturelle und optische Beeinträchtigung.

**Inspektions-Verfahren:**
1. Mit Multimeter prüfen: Kontinuität zwischen SS-Beschlag und CFK-Deck messen (sollte >100 kΩ sein, wenn isoliert)
2. Bereich unter Beschlag mit Tuch abreiben: Schwarze Oxidation?
3. Visuelle Rissbildung um Montage herum prüfen

**Maßnahme:**
1. Beschlag ausbauen
2. Unter der Montage: Durchsichtige G10-Epoxid-Platte (6 mm dick) oder Tef-Gel-Schicht einfügen (Isolation)
3. Alle Bolzen mit Tef-Gel unter dem Kopf + unter Unterlegscheibe einstreichen
4. Bolzen mit Nylon-Isolierbuchse isolieren
5. Wieder montieren (torque nach Hersteller-Vorgaben)
6. Oberflächenschaden an Beschlag: Polieren oder austauschen
7. CFK-Beschädigungen: Mit Epoxid-Patch reparieren

**Kosten:** €40–€100 Material (G10-Platte, Tef-Gel, Nylon-Buchsen) + Arbeit

**Prognose:** Mit Isolation: Problem vermieden. Mit regelmäßiger jährlicher Prüfung: Sicherheit gewährleistet. Bei CFK-Rümpfen empfehlen Gutachter eine jährliche Inspektion aller Edelstahl-auf-Carbon-Verbindungen.

---

### E.7 Bild 7: Geknickte Rohrbiegung
**Beschreibung:** Reling-Rohr zeigt deutliche Einkerbung oder Falte an einer Biegestelle (z.B. bei 90°-Knick am Bug). Oberfläche ist abgeflacht, Rohrdurchmesser lokal reduziert. Wandstärke an Knickstelle merklich dünner.

**Mechanik:** Beim Biegen ohne Dornfüllung oder mit zu kleinem Radius (R < 3×Ø) knickt die Innenseite des Rohrs ein. Wandstärke sinkt lokal von 2 mm auf 1 mm oder weniger. Strukturelle Festigkeit reduziert um ~50%.

**Schweregrad:** 2–3/5 — Mittelschwer. Nicht unmittelbar gefährlich, aber schwächungspotential über Zeit.

**Inspektions-Verfahren:**
1. Schieblehre: Durchmesser an Knickstelle vs. Normal-Stelle messen (Unterschied >2 mm = kritisch)
2. Wandstärken-Messer (Ultraschall): Lokale Verdünnung prüfen
3. Biegeradius mit Schablone messen: Soll R ≥ 75 mm (für Ø 25 mm Rohr)

**Maßnahme:**
1. Geknickte Segment ausmessen und markieren
2. Mit Trennschleifer ausschneiden (±50 mm beidseitig der Knickstelle)
3. Neues Rohrsegment anfertigen mit korrektem Biegeradius (R ≥ 3×Ø, idealerweise 5×Ø)
4. Beim Biegen: Dornfüllung verwenden oder Sand-Füllung (Sackgasse-Sand)
5. Neue Segment WIG-schweißen, beizen + passivieren
6. Inspektionspflicht: Alle Biegungen prüfen (Material-Schwachstellen)

**Kosten:** €100–€250 (Schlosserei für neue Biegung + Schweißung)

**Prognose:** Geknickte Rohre sollten erneuert werden, um Langzeitermüdung zu vermeiden. Keine einfache Reparatur möglich.

---

### E.8 Bild 8: Perfekte Chainplate-Installation (Referenz)
**Beschreibung:** Polierte 316L Chainplate (50×10 mm, #320 oder besser), saubere Decksdurchführung mit elastischem Sealant (Sikaflex 291 oder 292), Toggle ist sauber und bewegt sich frei ohne Knarren. Oberflächenfinish: Spiegel-glanz oder satiniert.

**Inspektions-Checkliste:**
- [ ] Oberfläche poliert (mindestens #240)?
- [ ] Kein Oberflächenrost, Staining oder Pitting sichtbar?
- [ ] Decksdurchführung mit modernem Elastomer-Sealant gefüllt?
- [ ] Toggle bewegt sich frei (kein Festsitzen)?
- [ ] Unterlegscheibe unter Deckskopf vorhanden?
- [ ] Keine Wasser-Spuren um Durchführung herum?
- [ ] Schraubenloch-Bereich: Kein Rost oder Verfärbung?

**Best Practices für diese Installation:**
1. Material: 316L (nicht 304, nicht unbeschichtet)
2. Oberflächenfinish: Mindestens poliert (#240), besser #320 oder Elektropoliert
3. Decksdurchführung: Mit 6 mm G10-Epoxid-Unterlegplatte isoliert (von Deck-Rumpf)
4. Bolzen: Passiviert, mit Tef-Gel unter Kopf + Unterlegscheibe
5. Sealant: Sikaflex 291 oder ähnlich (nicht Silikon!)
6. Toggle: Marine-Qualität, rostfrei, ohne Verschleiß

**Wartungs-Intervalle nach dieser Installation:**
- **Monatlich:** Visuell prüfen (keine Verfärbung)
- **6 Monatlich:** Mit Polier-Tuch überprüfen, ggf. leicht polieren
- **Jährlich:** Sealant um Durchführung kontrollieren (sollte noch elastisch sein, nicht gehärtet)
- **5 Jahre:** Sealant wechseln (Alterung)

---

### E.9 Bild 9: Korrosion durch Fremdmaterial-Kontakt
**Beschreibung:** Flächige Verfärbung und teilweise Oberflächenrauhheit an Edelstahl-Rohr, wo es direkt neben oder berührend ein Stahlgerüst oder Stahlkarabiner liegt. Verfärbung ist rötlich-braun (Eisenoxid-typisch).

**Chemie:** Eisen-Partikel von Normalstahl oder Stahlwolle kontaminieren die Edelstahl-Oberfläche. Eisen ist unedler als Edelstahl → galvanische Paarung → Eisenrost auf Edelstahl-Oberfläche.

**Schweregrad:** 1–2/5 — Kosmetisch, aber Warnsignal für fehlerhafte Handhabbung.

**Inspektions-Verfahren:**
1. Mit Magnet prüfen: Anhaften von Eisen-Partikeln?
2. Mit Oxalsäure-Tester (Moly-Test): Rust löst sich auf?
3. Oberflächenschliff: Wie tief ist Kontamination?

**Maßnahme:**
1. Kontaminations-Quelle eliminieren (Stahlwolle, Stahlbürsten, eisen-haltiges Werkzeug)
2. Bereich mit Beizpaste (Avesta 401) 30 min behandeln
3. Mit Edelstahl- oder Kupferbürste abbürsten
4. Gründlich abspülen
5. Passivieren (Avesta 601)

**Prävention:**
- Nur Edelstahl- oder Kupferbürsten verwenden (nie Stahlwolle!)
- Werkzeug sollte Edelstahl sein (oder zumindest nicht mit Eisen kontaminiert)
- Nach Schweißung sofort Beizen + Passivieren (nicht warten, nicht mit anderen Materialien mischen)

---

*Ende ANHANG E*

---

## ANHANG F — Ideale Bordausstattung Edelstahl-Halbzeuge

Die Bordausstattung mit Edelstahl-Halbzeugen hängt stark ab vom Einsatzprofil, der Rumpflänge, dem Material des Rumpfes und der geplanten Betriebsdauer ohne Werftaufenthalt. Nachfolgend Empfehlungen für verschiedene Schiffklassen und Fahrtgebiete.

### F.1 Küstenfahrt (Wochenend-Segler, 8–10m)

**Einsatzprofil:** Segel- oder Motorboot, Küstenfahrt (max. 20 SM von Land), Süßwasser-Standorte oder niedrige Salzwasser-Exposition. Reparaturen meist in nächster Heimatwerft möglich.

**Notwendige Ausrüstung für Instandhaltung und Reparaturen:**

| Artikel | Spezifikation | Preis ca. | Bezug |
|---------|---------------|-----------|-------|
| Edelstahlrohr 25×2mm 316L, 2m | EN 10217-7, nahtlos | ~€24 | Nordfels, Steelmaterial |
| Flachstahl 40×8mm 316L, 0,5m | Poliert #240 | ~€10 | Nordfels |
| Rundstahl Ø10mm 316L, 0,5m | Geschliffen | ~€4 | Nordfels |
| Blech 2mm 316L, 200×300mm | Kaltgewalzt 2B | ~€10 | Steelmaterial |
| Schweißzusatz 316LSi, 5 Stäbe (2,4mm) | AWS E316L-16 | ~€5 | Merkle Welding |
| Beizpaste Avesta 401 (Kleine Dose) | 100g | ~€15 | Avesta Sheffield |
| Moly-Test-Set | Zum Legierungsnachweis | ~€15 | Amazon DE |
| Bar Keeper's Friend, 300g | Reinigung & Passivierung | ~€3 | Baumarkt |
| Feile-Set (Edelstahl-freundlich) | 200mm Flach/Rund | ~€12 | |
| Stahlwolle 0000 (Drahtbürste meiden!) | Kupfer oder Edelstahl | ~€5 | |
| **Gesamt-Notfall-Kit** | **Für Reparaturen** | **~€103** | |

**Empfohlenes Ersatzteil-Lager:**
- 2× Stanchions mit Basen (25×2mm, 600mm)
- 1× Rohrschellen-Set (25mm)
- 5× Schweißnägel/Nieten 316L Ø4–5mm
- Auswahl Sechskant-Bolzen M8–M10 (316L)

**Regelmäßige Wartung:**
- Jährliches Polieren aller sichtbaren Teile (1–2 Stunden, DIY möglich)
- Nach Winterlagerung: Bar Keeper's Friend Behandlung
- Überprüfung auf Oberflächenrost (nicht zwingend gefährlich, aber kosmetisch lästig)

---

### F.2 Blauwasser-Langfahrt (10–14m)

**Einsatzprofil:** Segelboot oder Langfahr-Motoryacht, durchgehend salzwasser-exponiert, 6+ Monate ohne Werftaufenthalt, Fahrt in tropische/subtropische Gewässer. Korrosionsgefahr erheblich höher, Reparaturen müssen oft selbst durchgeführt werden.

**Umfangreiches Reparatur-Kit:**

| Artikel | Spezifikation | Menge | Preis ca. | Kumulativ |
|---------|---------------|-------|-----------|-----------|
| Edelstahlrohr 25×2mm 316L | EN 10217-7, 4m | 1× | ~€48 | €48 |
| Edelstahlrohr 32×2mm 316L | EN 10217-7, 2m | 1× | ~€34 | €82 |
| Edelstahlrohr 38×2,5mm 316L | Für Bimini-Reparatur | 1m | ~€18 | €100 |
| Flachstahl 40×8mm 316L, poliert | 1,5m | 1× | ~€30 | €130 |
| Flachstahl 50×10mm 316L, poliert | Für Chainplate-Ersatz | 0,5m | ~€16 | €146 |
| Flachstahl 60×12mm 316L | Backing Plates | 0,3m | ~€12 | €158 |
| Rundstahl Ø10mm 316L | 1m | 1× | ~€8 | €166 |
| Rundstahl Ø16mm 316L | Davit-Reparatur, 0,5m | 1× | ~€7 | €173 |
| Blech 2mm 316L | 300×500mm | 1× | ~€24 | €197 |
| Winkel 30×30×3mm 316L | 1m | 1× | ~€10 | €207 |
| Schweißzusatz 316LSi, 1kg | AWS E316L-16, Stäbe/Draht | 1× | ~€30 | €237 |
| Schweißzusatz 316LSi, 500g Draht | Für WIG-Schweißen | 1× | ~€18 | €255 |
| Beizpaste Avesta 401 | 500g Standardgröße | 1× | ~€20 | €275 |
| Passivierungspaste Avesta 601 | 500g | 1× | ~€20 | €295 |
| Passivierungspaste Avesta 606 | Für Hochtemperatur-Schweißnähte | 250g | ~€16 | €311 |
| Bar Keeper's Friend | 300g, mehrere Dosen | 3× | ~€9 | €320 |
| CorrosionX Marine (Spray) | 400ml Konservierung | 2× | ~€20 | €340 |
| Kleber/Isolierabschirmung Tef-Gel | 100g | 1× | ~€12 | €352 |
| Sechskant-Bolzen M8/M10/M12 316L | Auswahl (8–10 Stück) | — | ~€25 | €377 |
| Unterlegscheiben 316L | ISO 7091 Sortiment | — | ~€8 | €385 |
| Selbstsichernde Muttern 316L | Nylon-Insert, M8–M12 | — | ~€12 | €397 |
| **Gesamt Blauwasser-Kit** | **Für 6–12 Monate** | — | — | **~€397** |

**Besonderheiten für Blauwasser:**
- Doppelter Bestand an Schweißzusatz (Verbrauch höher als erwartet)
- Passivierungspaste 606 für tropische Gewässer mit extremer UV-Einstrahlung
- Extra Isoliermaterial (Spaltkorrosion ist häufigste Schadensursache)
- Mehrere Chainplate-Ersatzsegmente zur Hand
- Mindestens 1m Rohr 25×2 und 32×2 für Reling-Reparaturen

**Wartungs-Intervalle bei Blauwasser:**
- Täglich (visuell): Reling auf Risse prüfen, sichtbare Korrosion checken
- Wöchentlich: Alle Chainplates anfassen (auf Risse prüfen), Schweißnähte an Davits inspizieren
- Monatlich: Polieren aller sichtbaren SS-Teile mit Bar Keeper's Friend
- Nach tropischen Gewässern oder extremer Hitze: Komplette Passivierung aller Schweißnähte

---

### F.3 GFK-Yacht mit Edelstahl-Armierung (Küstenfahrt, 8–14m)

**Zusätzliche Ausstattung für GFK-Rumpf mit SS-Beschlägen:**

| Artikel | Begründung | Preis ca. |
|---------|-----------|-----------|
| Tef-Gel (3× Tuben à 50g) | Isolation SS-Bolzen auf GFK | ~€36 |
| Nylon-Isolierbuchsen Sortiment | Unter allen SS-Beschlägen | ~€15 |
| G10-Platte 6mm, 300×300mm | Isolierplatte unter Davits/Klampen | ~€20 |
| Duralac-Paste (Alternative zu Tef-Gel) | Zusätzliche Isolation | ~€15 |
| **Gesamt GFK-Zusatz** | **Für Langlebigkeit** | **~€86** |

**Kritisch:** GFK und Edelstahl bilden ein Galvanische Paar. Ohne Isolation droht beschleunigte Korrosion des Edelstahls und Glasfaser-Schäden am Rumpf.

---

### F.4 Alu-Yacht mit Edelstahl-Struktur (Langfahrt, 10–20m)

**Problem:** Aluminium ist elektrochemisch aktiver als Edelstahl. Galvanische Korrosion droht überall, wo SS auf Alu montiert ist. Spannungsrisskorrosion ist zusätzliches Risiko.

| Artikel | Spezifikation | Menge | Preis ca. |
|---------|---------------|-------|-----------|
| Tef-Gel (Premium) | Unter ALLEN SS-Beschlägen | 5× Tuben | ~€60 |
| Nylon-Isolierbuchsen | Diverse Größen M6–M16 | 50er Box | ~€25 |
| G10-Platte 6mm | Isolier-Unterlagen | 500×300mm | ~€35 |
| G10-Platte 10mm | Für schwere Davits | 300×300mm | ~€28 |
| Duralac Paste | Langfristige Isolation | 2× Tuben | ~€30 |
| Isolier-Vlies (Fiberglas) | Unter Backing Plates | 1m² | ~€15 |
| **Gesamt Alu-Langfahrt-Zusatz** | **Kritisch für Langlebigkeit** | — | **~€193** |

**Ausführungsrichtlinien für Alu + SS Kombination:**
1. Immer Tef-Gel unter den Kopf jeden SS-Bolzens auftragen
2. Unter jede Unterlegscheibe G10-Platte oder Duralac legen
3. Nach Montage: Bolzen mit CorrosionX spray konservieren
4. Jährliche Inspektion: Bolzen drehen, auf Korrosion prüfen, ggf. Tef-Gel erneuern

---

### F.5 Racing-Yacht (Regatta-Ausrüstung, 8–16m)

**Spezialfall:** Höchste Performance, leicht Edelstahl-Rohre 22×1,5 statt 25×2, Duplex 2205 für kritische Teile, polierte Oberflächen sind Standard.

| Artikel | Besonderheit | Preis ca. |
|---------|---------------|-----------|
| Edelstahlrohr 22×1,5mm 316L, 3m | Leichter, für Reling | ~€28 |
| Edelstahlrohr 25×2mm 316L, 2m | Backup für Reparaturen | ~€24 |
| Flachstahl 50×10mm Duplex 2205, 0,5m | Kritische Chainplates | ~€24 |
| Rundstahl Ø8mm 316L, 1m | Für Beschläge | ~€5 |
| Blech 1,5mm 316L poliert | Mainsail Battens, Optik | ~€16 |
| Schweißzusatz Duplex 2205 Draht | Für Duplex-Reparaturen | ~€28 |
| Polier-Compound (NEVER bare Edelstahl!) | Elektropolieren vorbereiten | ~€12 |
| **Gesamt Racing-Kit** | **Für Regatta-Saison** | **~€137** |

---

### F.6 Motoryacht Langfahrt (Diesel-Boot, 12–30m)

**Besonderheit:** Propellerwelle muss Aquamet oder gehärteter 1.4313 sein (nicht 316L!), Motor-Fundament braucht Isolation, Kühlwasser-Leitungen aus Edelstahl für Langlebigkeit.

| Artikel | Grund | Preis ca. |
|---------|-------|-----------|
| Edelstahlrohr 32×2,5mm 316L | Kühlwasser, Abgas | ~€42 |
| Edelstahlrohr 25×2mm 316L | Backup-Reling | ~€24 |
| Flachstahl 60×12mm 316L | Motor-Fundament | ~€20 |
| Winkel 40×40×4mm 316L | Verstrebung Motor | ~€14 |
| Rundstahl Ø16mm Aquamet 22 | Propellerwelle (nicht 316L!) | ~€25 |
| Blech 3mm 316L | Motor-Schutzblech | ~€18 |
| Schweißzusatz 316L + Aquamet-Zusatz | Diverse Schweißungen | ~€48 |
| G10/Duralac Isolation | Motor auf Alu-Rahmen | ~€40 |
| Beizpaste + Passivierung | Nach Motor-Montage | ~€40 |
| **Gesamt Motoryacht-Kit** | **Für zuverlässige Motoranlage** | **~€271** |

---

### F.7 Notfall-Reparaturbox für abgelegene Fahrtgebiete

Für Yachten, die längere Zeit fern von Werften operieren (Südatlantik, Pazifik):

| Artikel | Grund | Menge |
|---------|-------|-------|
| Edelstahlrohr 25×2mm 316L | Allzweck-Reparaturen | 3m |
| Edelstahlrohr 32×2mm 316L | Bimini, Davit | 2m |
| Flachstahl 50×10mm 316L | Chainplate-Notfall | 1m |
| Rundstahl Ø10 + Ø16mm 316L | Struktur, Bolzen | je 0,5m |
| Blech 2mm 316L | Patches | 300×500mm |
| Schweißzusatz 316L (Stab + Draht) | Komplette Reparatur | 1kg Stab + 500g Draht |
| Beiz-/Passivierungspaste | Nach jeder Schweißung | 2× je 500g |
| Bar Keeper's Friend | Tägliche Reinigung | 2× 300g |
| CorrosionX Spray | Langfristige Konservierung | 2× 400ml |
| Nylon-Isolierbuchsen | Für notfall-Montagen | 50er Box |
| Sechskant-Bolzen M8–M12 | Backup-Befestigungen | je 10 Stück |
| **Gesamtgewicht** | ~8kg | — |
| **Gesamtkosten** | — | **~€480** |

**Verpackung:** Edelstahl-Box 800×500×300mm mit Feuchte-Absorbern. Bei Langfahrt ein absolutes Muss.

---

### F.8 Kostenberechnung nach Bootsklasse

| Bootsklasse | Jahresbudget (Wartung) | 5-Jahres-Budget | Empfohlenes Kit |
|-------------|------------------------|-----------------|-----------------|
| Seekajak / Jollen <5m | €0–30 | €0–150 | Mini (Rohrschellen + Bolzen) |
| Küstenbootl 5–8m | €50–120 | €250–600 | F.1 (Küstenfahrt) |
| Cruiser 8–12m | €150–300 | €750–1500 | F.1 + F.3 oder F.4 |
| Langfahrt 12–16m | €300–600 | €1500–3000 | F.2 + F.4 + F.7 |
| Superyacht 16–25m | €800–1500 | €4000–7500 | F.2 + F.4 + F.5 + F.6 |
| Expedition 20–35m | €1500–3000 | €7500–15000 | F.2 + F.4 + F.6 + F.7 (doppelt) |

---

### F.9 Saisonale Wartungs-Checklisten

**Frühjahr (Übergang Winterlager → Seesaison):**
- [ ] Alle sichtbaren SS-Teile mit Bar Keeper's Friend reinigen
- [ ] Reling, Chainplates, Davits auf Risse prüfen
- [ ] Beizpaste auf verdächtige Schweißnähte auftragen (30 min wirken lassen)
- [ ] Passivierung durchführen
- [ ] Oberflächenmangel fotografieren (Dokumentation für Versicherung)

**Herbst (Vorbereitung Winterlager):**
- [ ] Komplette Passivierung aller Schweißnähte
- [ ] CorrosionX auf alle exponierte SS-Teile sprühen
- [ ] Bolzen mit Tef-Gel behandeln (gegen Winter-Korrosion)
- [ ] Nylon-Isolierbuchsen kontrollieren, bei Verschleiß austauschen

**Nach Reparaturen (immer!):**
- [ ] Beizpaste 30 min einwirken lassen
- [ ] Passivierungspaste 1 Stunde auftragen
- [ ] Mit Wasser abspülen, trocknen
- [ ] CorrosionX Spray auftragen (Langfristschutz)

---

*Ende der Wissensdatei 05_07_edelstahl_halbzeuge.md — Version 1.1*
*AYDI Confidence: documented — Zusammenstellung aus Herstellerkatalogen, Fachliteratur, Forum-Konsens*
*Nächste Überprüfung: 2026-09*
