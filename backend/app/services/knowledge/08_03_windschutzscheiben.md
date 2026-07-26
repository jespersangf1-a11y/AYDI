# 08.03 — Windschutzscheiben und Frontfenster im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 08.03** — Kategorie 8: Fenster, Luken und Öffnungen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen, Klassifikationsregeln), documented (Hersteller-Kataloge, Werftunterlagen, Surveyor-Erfahrungen), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien](#2-zukunftstechnologien)
3. [Best Practices nach Revier](#3-best-practices-nach-revier)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle (WindshieldSpec, WindshieldCondition, WindshieldSystemAssessment)](#6-pydantic-modelle)
7. [Grundlagen](#7-grundlagen)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Definition und Abgrenzung

**Windschutzscheiben** (engl. windshields, windscreens) und **Frontfenster** (engl. front windows) sind die vorderen Verglasungselemente des Steuerhauses, der Flybridge oder des Helms einer Motor- oder Segelyacht. Sie unterscheiden sich fundamental von Seitenfenstern (→ 08.02 Bullaugen) und Decksluken (→ 08.01) durch:

1. **Strukturelle Funktion** — Windschutzscheiben sind tragende Elemente der Aufbaustruktur, besonders bei rahmenlosen Designs
2. **Extreme Belastung** — Frontale Wellenbelastung (Slamming), Windlast bei hohen Geschwindigkeiten, Spritzwasser, Regen, Hagel
3. **Sicherheitskritische Sichtfunktion** — Klare Sicht für den Schiffsführer unter allen Wetterbedingungen ist navigatorisch essentiell
4. **Komplexe Geometrie** — Häufig gebogen (single-curved oder compound-curved), geneigte Einbaulage, große Flächen

| Begriff | Definition | Typische Anwendung |
|---------|-----------|-------------------|
| **Windschutzscheibe** (Windshield/Windscreen) | Frontale Verglasung vor dem Steuerstand | Motoryacht, Pilothouse, Flybridge |
| **Frontfenster** (Front Window) | Festverglaste Frontscheibe ohne Öffnungsmechanismus | Moderne Motoryachten, Superyachten |
| **Wrap-around Windscreen** | Durchgehende Verglasung von Front bis Seite | Sportboote, Express Cruiser |
| **Pilothouse-Verglasung** | Steuerhaus-Frontscheiben bei Segelyachten | Decksalon-Yachten, Pilothouse-Segler |
| **Flybridge-Windschutz** (Flybridge Screen) | Frontscheibe der oberen Steuerposition | Flybridge-Motoryachten |
| **Center-Console-Windschutz** | T-Top oder Rahmenwindschutz bei offenen Booten | Center Consoles, Walkarounds |
| **Helm-Station-Verglasung** | Verglasung um den Hauptsteuerstand | Alle Bootstypen mit geschlossenem Helm |

### 1.2 Abgrenzung zu anderen Wissensdateien

- **08.01 Decksluken**: Horizontale Öffnungen im Deck — andere Belastungsrichtung, andere Normanforderungen
- **08.02 Bullaugen und Seitenfenster**: Seitliche Verglasung — geringere Frontbelastung, kleinere Flächen
- **02.01–02.08 Dichtstoffe**: Klebstoffe für Structural Glazing werden hier referenziert, Detailwissen in Kat. 02

### 1.3 Historischer Kontext

Die Entwicklung der Yacht-Windschutzscheibe spiegelt den Wandel im Yachtdesign:

**1950er–1970er:** Flache Einscheiben-Windschutzscheiben aus gehärtetem Glas in Aluminiumrahmen mit Gummidichtungen. Schiebefenster für Belüftung. Sicht und Dichtheit oft mangelhaft. Typische Dicke: 4–6 mm ESG.

**1980er–1990er:** Aufkommen gebogener Scheiben durch Fortschritte in der Glasbearbeitung. Erste Verklebungstechnologien (Sikaflex). Getönte Scheiben werden populär. Polycarbonat für Sportboote. Typische Dicke: 6–8 mm ESG oder 10–12 mm PMMA.

**2000er–2010er:** Structural Glazing revolutioniert das Yachtdesign — rahmenlose, verklebte Panorama-Windschutzscheiben. Verbundsicherheitsglas (VSG) wird Standard bei Premium-Yachten. Beheizte Scheiben für nordische Märkte. Wischer-Systeme werden leistungsfähiger (Pantograph-Wischer). Typische Dicke: 8–12 mm VSG.

**2020er:** Vollflächige Panorama-Verglasungen, elektrochromes Glas, integrierte Displays (HUD-Projektionen), akustische Laminate, High-Performance-Beschichtungen (Low-E, hydrophob). Superyachten mit >15 m² zusammenhängender Frontscheibe. Typische Dicke: 12–25 mm VSG je nach Fläche.

### 1.4 Regulatorischer Rahmen — ISO 12216:2020

#### 1.4.1 Anwendung auf Windschutzscheiben

Die **ISO 12216:2020** ("Small craft — Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements") gilt vollumfänglich für Windschutzscheiben von Booten bis 24 m Rumpflänge. Windschutzscheiben fallen unter die Kategorie **"Windows"** und werden nach Position klassifiziert.

**Positionsklassifizierung für Windschutzscheiben:**

| Position | ISO-Klasse | Beschreibung | Bemessungsdruck-Faktor k_LOC |
|----------|-----------|-------------|------------------------------|
| Frontscheibe, aufrecht (>60° zur Horizontalen) | Position 1A | Höchste Belastung — direkter Wellenaufprall | 1.2 |
| Frontscheibe, geneigt (30°–60° zur Horizontalen) | Position 1B | Hohe Belastung — reduzierter Aufprallwinkel | 1.0 |
| Frontscheibe, stark geneigt (<30° zur Horizontalen) | Position 2 | Mittlere Belastung — Scheibe eher horizontal | 0.8 |
| Seitliche Wrap-around-Bereiche | Position 2 | Seitliche Belastung, geringer als frontal | 0.6 |
| Flybridge-Frontscheibe | Position 2–3 | Höher über Wasserlinie, weniger Wellenbelastung | 0.5–0.8 |

#### 1.4.2 Bemessungsdruck-Berechnung

Der Bemessungsdruck für Windschutzscheiben berechnet sich nach ISO 12216 wie folgt:

```
P_design = k_DC × k_LOC × k_AR × P_base

wobei:
  k_DC   = Designkategorie-Faktor
           Kat. A = 1.00, Kat. B = 0.80, Kat. C = 0.50, Kat. D = 0.25
  k_LOC  = Positionsfaktor (siehe Tabelle oben)
  k_AR   = Seitenverhältnis-Faktor (abhängig von b/a, kurze/lange Seite)
  P_base = Basisdrück (abhängig von Bootslänge und Geschwindigkeit)
```

**Basisdruck P_base nach Bootslänge (vereinfacht):**

| Bootslänge (m) | P_base Verdränger (kPa) | P_base Gleiter >25 kn (kPa) | P_base Gleiter >40 kn (kPa) |
|-----------------|------------------------|-----------------------------|-----------------------------|
| 8 | 3.0 | 5.0 | 8.0 |
| 10 | 3.5 | 5.5 | 9.0 |
| 12 | 4.0 | 6.0 | 10.0 |
| 15 | 5.0 | 7.5 | 12.0 |
| 18 | 6.0 | 9.0 | 14.0 |
| 20 | 6.5 | 10.0 | 16.0 |
| 24 | 7.5 | 12.0 | 18.0 |

**Beispielrechnung:** Eine 15 m Motoryacht (Gleiter, 30 kn), CE Kat. B, Frontscheibe aufrecht:

```
P_design = 0.80 × 1.2 × 1.0 × 7.5 = 7.2 kPa
```

Dies entspricht einer Flächenlast von ca. 720 kg/m² — erheblich mehr als bei Seitenfenstern.

> Confidence: `measured` (ISO 12216:2020, Annex A + B)

#### 1.4.3 Scheibendicke nach ISO 12216

**Für Sicherheitsglas (ESG/VSG) in Windschutzscheiben:**

```
t_min = k_shape × a × √(P_design / σ_allow)

wobei:
  t_min   = Mindestdicke in mm
  k_shape = Formfaktor (0.028 für b/a=1.0, 0.022 für b/a=0.5, 0.018 für b/a=0.3)
  a       = kurze Scheibenseite in mm
  σ_allow = zulässige Spannung (ESG: 35 MPa, VSG: 28 MPa, Float: 10 MPa)
```

**Praxis-Mindestdicken für Windschutzscheiben nach Bootslänge und Typ:**

| Bootslänge (m) | Verdränger ESG (mm) | Verdränger VSG (mm) | Gleiter >25 kn ESG (mm) | Gleiter >25 kn VSG (mm) |
|-----------------|--------------------|--------------------|------------------------|------------------------|
| 8–10 | 6 | 8 (4+4) | 8 | 10 (5+5) |
| 10–12 | 8 | 10 (5+5) | 10 | 12 (6+6) |
| 12–15 | 8 | 12 (6+6) | 10 | 14 (6+0.76+6) |
| 15–18 | 10 | 14 (6+0.76+6) | 12 | 16 (8+0.76+8) |
| 18–24 | 12 | 16 (8+0.76+8) | 14 | 19 (8+1.52+8) |

> Confidence: `measured` (ISO 12216:2020, Annex A) / `estimated` (Praxiswerte für Gleiter)

#### 1.4.4 Prüfanforderungen für Windschutzscheiben

ISO 12216 schreibt folgende Prüfungen vor:

1. **Wasserdichtigkeitsprüfung**: Berieselungstest mit 2,5 l/min pro Meter Dichtungslänge für 5 Minuten. Kein Wasser darf in den Innenraum gelangen.
2. **Festigkeitsprüfung**: 1.5 × P_design für 5 Minuten ohne bleibende Verformung. Maximale Durchbiegung ≤1/80 der kurzen Scheibenseite.
3. **Bruchprüfung**: 3.5 × P_design (Glas) bzw. 4.0 × P_design (Kunststoff) ohne Versagen.
4. **Stoßprüfung (Impact Test)**: 1 kg Stahlkugel aus 1.5 m Fallhöhe (Position 1) bzw. 1.0 m (Position 2/3) — kein Durchschlag.
5. **Verklebungsprüfung (Structural Glazing)**: Abzugsprüfung ≥1.5 × P_design auf der Klebfläche.
6. **UV-Alterung**: 2.000 Stunden Xenon-Bogenlampe, danach erneute Festigkeitsprüfung ≥90% des Ausgangswerts.

### 1.5 ISO 21005:2018 — Structural Glazing

Die **ISO 21005:2018** ("Small craft — Windows, portlights and hatches — Structural glazing") ist besonders relevant für Windschutzscheiben, da moderne Designs nahezu ausschließlich auf Structural Glazing setzen.

> ⚠️ **ZU PRÜFEN (Audit):** Normnummer/Scope nicht belegbar. ISO 21005:2018 ist tatsächlich "Ships and marine technology — Thermally toughened safety glass panes for windows and side scuttles" (Glasscheiben-Spezifikation), NICHT "Small craft — … — Structural glazing". Ein dedizierter ISO-Standard für Structural Glazing an Kleinbooten ließ sich nicht verifizieren (Klebe-/Verklebungsanforderungen ergeben sich i.d.R. aus ISO 12216 bzw. Klassenregeln). Die in diesem Abschnitt unter der Bezeichnung "ISO 21005" genannten Grenzwerte (SF ≥ 6, ≥15 mm Klebflächenbreite, Scherfestigkeit, UV-/Salzsprühdauer) sind daher normseitig unbelegt und zu verifizieren. Quelle: iso.org/standard/69966.html.

#### 1.5.1 Anwendungsbereich

- Fest verklebte Scheiben ohne mechanische Halterung (Schrauben, Klemmen)
- Typisch für Windschutzscheiben ab Baujahr ~2005
- Kombination mit mechanischer Sicherung (Retainer) für CE Kat. A/B empfohlen

#### 1.5.2 Klebstoffanforderungen

| Parameter | Anforderung ISO 21005 | Bemerkung |
|-----------|----------------------|-----------|
| Klebflächenbreite | ≥15 mm, typisch 20–40 mm | Abhängig von Scheibengewicht und Bemessungsdruck |
| Klebstoff-Scherfestigkeit | ≥2.0 MPa (nach Alterung) | Muss über gesamte Lebensdauer erreicht werden |
| UV-Beständigkeit | 3.000 h Xenon-Alterung | Festigkeit nach Alterung ≥90% |
| Salzsprühnebel | 1.000 h (ISO 9227) | Keine Delamination, keine Festigkeitsabnahme >10% |
| Temperaturbereich | -30°C bis +80°C (Klebfuge) | +80°C wird bei schwarzen Rahmen im Mittelmeer erreicht |
| Primer-Kompatibilität | Primer für Glas UND Rahmen nötig | Falsche Primer = häufigste Fehlerursache |

#### 1.5.3 Marine-Klebstoffe für Windschutzscheiben-Verklebung

| Produkt | Hersteller | Typ | Shore A | Scherfestigkeit (MPa) | Empfohlen für |
|---------|-----------|-----|---------|----------------------|---------------|
| **Sikaflex-295 UV** | Sika | 1K-PU | 40 | 2.0 | Standard, universell |
| **Sikaflex-296** | Sika | 1K-PU | 50 | 2.5 | Schwere Scheiben, Hochleistung |
| **Sikaflex-265** | Sika | 1K-PU | 40 | 2.0 | Kfz-Technik, marine adaptiert |
| **Simson ISR 70-03** | Bostik/Den Braven | 2K-PU | 55 | 4.0 | Superyacht-Standard |
| **Simson ISR 70-05** | Bostik/Den Braven | 2K-PU | 65 | 5.0 | Hochfest, steif |
| **3M 550 FC** | 3M | 1K-PU | 45 | 2.2 | Schnelle Aushärtung (24h) |
| **3M 590** | 3M | 1K-Silikon | 25 | 1.2 | Glas auf Glas, Doppelverglasung |
| **Dow Corning 795** | Dow | Silikon | 30 | 1.4 | Glas auf Aluminium |
| **Dow DOWSIL 993** | Dow | 2K-Silikon | 35 | 1.4 | Architektur-Structural-Glazing, marine adaptiert |

**Primer-System für Sikaflex-295 UV (häufigste Kombination):**

| Substrat | Primer | Trockenzeit | Bemerkung |
|----------|--------|-------------|-----------|
| Glas (ESG/VSG) | Sika Primer-206 G+P | 30 min | PFLICHT — ohne Primer haftet PU nicht auf Glas |
| Aluminium (eloxiert) | Sika Primer-206 G+P | 30 min | Nach Anschleifen mit K120 |
| Aluminium (pulverbeschichtet) | Sika Primer-209 D | 30 min | Abhängig vom Pulverbeschichtungstyp — Verträglichkeitstest! |
| GFK/Gelcoat | Sika Primer-206 G+P | 30 min | Oberfläche anschleifen, Lösemittel-fettfrei |
| Edelstahl 316L | Sika Primer-206 G+P | 30 min | Nach Anschleifen mit K80 |
| Acrylglas (PMMA) | Sika Primer-215 | 120 min | VORSICHT: Nur 215, andere Primer greifen PMMA an |
| Polycarbonat | Sika Primer-215 | 120 min | VORSICHT: Primer-Verträglichkeit prüfen |

> Confidence: `estimated — unverifiziert` (Sika TDS SDP025-SDP209; ISO-21005-Bezug fehlerhaft — reale ISO 21005 = thermisch vorgespannte Glasscheiben, nicht Structural Glazing; siehe Audit-Hinweis in §1.5)

### 1.6 ISO 3903:2020 — Scheibenwischer

Die **ISO 3903:2020** ("Ships and marine technology — Windscreen wipers") regelt Scheibenwischer-Systeme für die Schifffahrt:

> ⚠️ **ZU PRÜFEN (Audit):** Normnummer/Scope/Jahr nicht belegbar. ISO 3903 ist tatsächlich "Ships and marine technology — Ships' ordinary rectangular windows" (aktuelle Ausgabe 2012, keine Ausgabe 2020) und behandelt rechteckige Schiffsfenster, NICHT Scheibenwischer. Ein spezifischer ISO-Standard für marine Scheibenwischer ließ sich nicht verifizieren (Anforderungen stammen i.d.R. aus Klassenregeln/Marinespezifikationen). Die folgenden Wischer-Kennwerte sind fachlich plausibel, aber nicht normbelegt. Quelle: iso.org/standard/54518.html.

#### 1.6.1 Anforderungen

| Parameter | Anforderung | Anmerkung |
|-----------|-------------|-----------|
| Wischfeld | ≥80% der Scheibenfläche je Wischerarm | Für Hauptsteuerstand |
| Wischfrequenz | Normal: 20–45 Zyklen/min, Schnell: 45–65 Zyklen/min | Stufenlos einstellbar empfohlen |
| Betriebsdruck | Wischarmdruck 3–8 N/m Wischblattlänge | Zu wenig = ungenügend, zu viel = Kratzgefahr |
| Waschanlage | Frischwasser-Sprühdüsen empfohlen | Salzentfernung essentiell |
| Betriebstemperatur | -25°C bis +55°C | Arktis/Tropenbereich |
| Salzwasserbeständigkeit | 500 h Salzsprühnebel (ISO 9227) | Motor, Getriebe, Arme, Blätter |
| Lebensdauer Motor | ≥10.000 Betriebsstunden | Scheibenwischerblätter: 6–12 Monate |

#### 1.6.2 Wischer-Typen

| Typ | Beschreibung | Wischfeld | Einsatzbereich |
|-----|-------------|-----------|----------------|
| **Pendelwischer** (Swing Arm) | Einzelner Arm, Pendelbewegung 60°–120° | Segmentförmig | Kleine Boote, einzelne Scheiben |
| **Pantograph-Wischer** (Pantograph) | Parallelogramm-Mechanismus, vertikale Auf-Ab-Bewegung | Nahezu rechteckig | Superyachten, Brückenfenster, große Flächen |
| **Doppelarm-Wischer** (Twin Arm) | Zwei gegenläufige Arme | Breites Feld | Motoryachten mit breiter Frontscheibe |
| **Verdeckter Wischer** (Concealed) | Arm verschwindet unter Scheibenunterkante | Wie Pendelwischer | Premium-Yachten (Ästhetik) |

### 1.7 ABYC Standards (USA)

Die **American Boat and Yacht Council** definiert in den Standards relevante Anforderungen:

- **ABYC H-25 (Windshields and Windows):** Festigkeit, Sichtfeld, Verzerrungsfreiheit. Scheibenverzerrung ≤1 Dioptrie bei Blickrichtung voraus. Lichtdurchlässigkeit ≥70% für klare Scheiben, ≥50% für getönte.
- **ABYC A-22 (Fire Protection):** Windschutzscheiben in der Nähe von Motorräumen müssen Brandausbreitungsprüfung bestehen. VSG mit feuerhemmender Zwischenschicht empfohlen.
- **ABYC H-2 (Ventilation):** Öffnende Windschutzscheiben tragen zur Belüftung des Steuerhauses bei — Querlüftungsquerschnitt mind. 0,02 m² pro Person am Helm.

### 1.8 SOLAS — Feuerwiderstandsklassen für Windschutzscheiben

Für Yachten >24 m (Superyachten) und gewerblich genutzte Fahrzeuge gelten die **SOLAS-Anforderungen** (International Convention for the Safety of Life at Sea):

| Klasse | Feuerwiderstand | Typische Anwendung | Glasaufbau |
|--------|----------------|-------------------|-----------|
| **A-0** | 60 min Tragfähigkeit, 0 min Isolierung | Steuerhaus-Schott (Mindeststandard) | VSG mit intumeszenter Zwischenschicht |
| **A-15** | 60 min Trag., 15 min Isolierung | Maschinenraum-Grenzflächen | VSG mit Brandschutzbeschichtung |
| **A-30** | 60 min Trag., 30 min Isolierung | Hochrisiko-Bereiche | Spezial-VSG (Pilkington Pyrostop) |
| **A-60** | 60 min Trag., 60 min Isolierung | Höchste Anforderung | Brandschutzglas mehrteilig |
| **B-0** | 30 min Tragfähigkeit | Innere Trennwände | ESG oder VSG Standard |

**SOLAS-zertifizierte Glashersteller für Windschutzscheiben:**

| Hersteller | Produkt | Klasse | Max. Größe (mm) |
|-----------|---------|--------|-----------------|
| **Pilkington** (UK) | Pyrostop | A-0 bis A-60 | 2.500 × 1.500 |
| **Schott** (DE) | Pyran S | A-0 bis A-30 | 2.000 × 1.200 |
| **Vetrotech** (CH/Saint-Gobain) | Contraflam | A-0 bis A-60 | 3.000 × 1.800 |
| **AGC** (BE) | Pyrobel | A-0 bis A-30 | 2.200 × 1.400 |

> Confidence: `measured` (SOLAS Ch. II-2, IMO FTP Code)

### 1.9 Klassifikationsgesellschaften — Windschutzscheiben-Bemessung

Für Yachten >24 m oder unter Klasse gelten erweiterte Anforderungen der Klassifikationsgesellschaften:

#### 1.9.1 Lloyd's Register (LR)

**LR SSC Rules (Special Service Craft)** — Windschutzscheiben-Anforderungen:

```
Bemessungsdruck (LR):
  P_design = 0.035 × V² × cos(α) × k_height

wobei:
  V       = Dienstgeschwindigkeit in Knoten
  α       = Neigungswinkel der Scheibe zur Vertikalen
  k_height = Höhenfaktor (1.0 bei h=2m über WL, 0.7 bei h=5m)
```

**Mindestdicken nach LR (VSG):**

| V (kn) | Scheibenfläche <0.5 m² | 0.5–1.0 m² | 1.0–2.0 m² | >2.0 m² |
|--------|------------------------|------------|------------|---------|
| 10 | 10 mm | 12 mm | 14 mm | 16 mm |
| 20 | 12 mm | 14 mm | 16 mm | 19 mm |
| 30 | 14 mm | 16 mm | 19 mm | 22 mm |
| 40 | 16 mm | 19 mm | 22 mm | 25 mm |

#### 1.9.2 DNV (Det Norske Veritas)

**DNV Pt.3 Ch.3 — Yacht/HSC Rules:**

DNV verwendet einen ähnlichen Ansatz, ergänzt um dynamische Lastfälle:

- **Slamming-Zuschlag** für Gleiter-Yachten: +30% auf den Basisdruck bei V/√L > 3.0
- **Grünwasser-Lastfall**: Wasserdruckhöhe h_green = 0.36 × L × k_pos, Druck P = ρ × g × h_green
- **Mindest-Klebflächenbreite**: ≥25 mm für strukturell verklebte Windschutzscheiben (strenger als ISO 21005)
- **Rahmenscantlings**: Mindest-Wandstärke Aluminiumrahmen = 5 mm (vs. 3 mm bei ISO 12216)

#### 1.9.3 Bureau Veritas (BV)

**BV NR 500/NR 217:**

- Spezifische Stoßbelastungsfaktoren für Hochgeschwindigkeitsyachten (>30 kn): P_impact = 1.5 × P_static
- Anforderung an **Splitterschutzfolie** (anti-spall film) auf der Innenseite bei V > 25 kn
- Vorschrift zur **Sicherheitsleiste** (retention bar) als Backup bei VSG-Versagen

#### 1.9.4 RINA (Registro Italiano Navale)

- Weit verbreitet bei italienischen Superyachtwerften (Azimut, Benetti, Sanlorenzo, Ferretti)
- Eigene Scheibendicken-Tabellen, tendenziell konservativ (≈LR + 10%)
- Besondere Anforderung an **Beschlagsfreiheit**: Beheizte Scheiben oder Entfeuchtungssystem vorgeschrieben für Kat. A/B

> Confidence: `measured` (LR SSC Rules 2023, DNV Pt.3 Ch.3, BV NR 500, RINA Rules for Yachts)

### 1.10 CE/RCD 2013/53/EU — Spezifische Anforderungen an Windschutzscheiben

Die **EU Recreational Craft Directive** verlangt für Windschutzscheiben:

**Anhang I, Abschnitt 3.4 (Schutz vor Wassereinbruch):**
- Windschutzscheiben müssen der deklarierten Designkategorie entsprechend wasserdicht sein
- Öffnende Windschutzscheiben müssen im geschlossenen Zustand den Dichtungstest bestehen
- Bei Schiebe-Windschutzscheiben: Drainagebahn für eingedrungenes Wasser vorgeschrieben

**Anhang I, Abschnitt 5.2 (Sicherheit):**
- Sicherheitsverglasung Pflicht (ESG oder VSG) — Floatglas ist NICHT zulässig für Windschutzscheiben
- VSG bevorzugt: Bei Bruch bleibt die Scheibe im Rahmen (keine scharfen Splitter im Cockpit)
- ESG zulässig, aber: zerfällt bei Bruch in kleine Würfel — vollständiger Sichtverlust

**Anhang I, Abschnitt 5.7 (Sichtbarkeit):**
- Windschutzscheibe darf die Sicht des Schiffsführers nicht unzulässig einschränken
- Maximale optische Verzerrung: ≤1 Dioptrie
- Lichtdurchlässigkeit bei klaren Scheiben: ≥70% (gemäß ECE R43 / ISO 3917)
- Spiegelungen und Doppelbilder sind auf ein Minimum zu reduzieren (VSG mit PVB-Folie: <0.5 Dioptrie Doppelbild)

> Confidence: `measured` (RCD 2013/53/EU Anhang I, ECE R43)

---

## 2. Zukunftstechnologien

### 2.1 Head-Up-Display (HUD) Windschutzscheiben

**Funktionsprinzip:** Projektoreinheit unter dem Armaturenbrett projiziert navigationsrelevante Daten (Kurs, Geschwindigkeit, Tiefe, AIS-Ziele) auf die Windschutzscheibe. Die Information erscheint im Sichtfeld des Schiffsführers, ohne den Blick von der See abzuwenden.

**Stand der Technik:**
- **Garmin** bietet HUD-Projektoren für den Nachrüstmarkt (Garmin GHC 50 mit HUD-Funktion in Entwicklung)
- **Raymarine** testet integrierte HUD-Systeme für Motoryacht-Helme
- **Superyacht-Segment**: Custom-Lösungen von **Trend Marine** mit laminierter HUD-Folie in der VSG-Zwischenschicht

**Technische Anforderungen an HUD-Windschutzscheiben:**
- Spezielle PVB-Folie mit Keilprofil (0.5° Keil) zur Vermeidung von Doppelbildern
- Hohe Reflexionseffizienz der Innenscheibe (mindestens 20% bei 550 nm)
- Scheibe darf nicht zu stark geneigt sein (optimal 25°–45° zur Vertikalen)
- Kosten: ca. 3.000–8.000 EUR Aufpreis gegenüber Standard-VSG

> Confidence: `estimated` (Technologie aus Automotive adaptiert, marine Serienprodukte in Entwicklung)

### 2.2 Elektrochromes Glas für Windschutzscheiben

**Anwendung speziell für Windschutzscheiben:**
- Blendschutz bei Tiefstand der Sonne (morgens/abends) durch selektive Abdunklung
- Automatische Steuerung per Lichtsensor möglich
- Partielles Dimmen (Gradient-Schaltung) — oberer Bereich dunkel, unterer klar

**Hersteller mit mariner Zulassung:**

| Hersteller | Produkt | Schaltzeit (s) | T_vis hell (%) | T_vis dunkel (%) | Marine-Erfahrung |
|-----------|---------|----------------|----------------|-------------------|-----------------|
| **View Inc.** | View Dynamic Glass | 8–12 | 62 | 1 | Superyachten, Einzelanfertigung |
| **SageGlass** (Saint-Gobain) | SageGlass Marine | 10–15 | 60 | 3 | Zertifiziert für Marine |
| **Gentex** (USA) | dimmable Marine | 3–5 | 50 | 5 | Automotive/Avionik, Marine-Prototyp |
| **Gauzy** (Israel) | LCG Marine (PDLC) | <1 | 75 | <1 (opak) | Privatsphäre, nicht für Blendschutz |

**Einschränkungen für Windschutzscheiben:**
- COLREG-Konformität: Abgedunkelte Windschutzscheiben dürfen die Erkennung von Navigationslichtern nicht beeinträchtigen — maximale Abdunklung auf T_vis ≥30% begrenzt empfohlen
- Stromausfall: Fail-State muss "transparent" sein (Sicherheitsanforderung)
- Kosten: 1.500–3.000 EUR/m² (vs. 200–500 EUR/m² für Standard-VSG)

### 2.3 Beheizte Windschutzscheiben — Erweiterte Technologien

**Nächste Generation:**
- **Infrarot-reflektierende Beschichtung** (Low-E) kombiniert mit Heizfunktion: reduziert Wärmeeintrag im Sommer, heizt im Winter
- **Selektive Beheizung**: Nur der Wischerbereich wird beheizt (Energieeffizienz)
- **Transparente Heizschicht** auf Basis von Silber-Nanodraht-Netzwerken (CNT/AgNW): gleichmäßigere Erwärmung als Heizdraht, keine sichtbaren Drähte

**Entwicklungsstatus:**
- Heizdraht-Technologie: ausgereift, Serienprodukt (Speich, Trend Marine)
- ITO-Beschichtung: verfügbar, aber teuer (600–1.200 EUR/m² Aufpreis)
- AgNW-Netzwerk: Labor/Prototyp, noch nicht marine-zertifiziert

### 2.4 Selbstreinigende Beschichtungen

**Hydrophobe Beschichtungen** (Lotus-Effekt) für Windschutzscheiben:

| Produkt | Hersteller | Typ | Standzeit | Wasserabperlwinkel | Preis (EUR/m²) |
|---------|-----------|-----|-----------|-------------------|---------------|
| **Aquapel** | PGW (Pilkington) | Fluorpolymer | 6–12 Monate | >110° | 30–50 |
| **Rain-X Marine** | ITW | Siloxan | 3–6 Monate | >100° | 15–25 |
| **Nanolex Si3D Marine** | Nanolex (DE) | SiO₂ Keramik | 12–24 Monate | >115° | 50–80 |
| **Gtechniq Marine Crystal Serum** | Gtechniq (UK) | SiO₂/TiO₂ | 24–36 Monate | >120° | 80–120 |
| **CeRam-Kote Marine** | Freecom (USA) | Keramik | 36+ Monate | >115° | 100–150 |

**Vorteile für Windschutzscheiben:**
- Reduziert Wischerbedarf bei leichtem Regen drastisch (ab 15 kn Fahrt kein Wischer nötig)
- Salzwasser perlt ab, reduziert Salzflecken
- Erleichtert Insektenentfernung

**Photokatalytische Beschichtung** (TiO₂):
- Baut organische Verschmutzung durch UV-Licht ab
- Pilkington Activ: Serienprodukt, aber nicht explizit für marine Windschutzscheiben zertifiziert
- Einschränkung: Funktioniert nur bei UV-Einstrahlung — keine Wirkung bei bewölktem Himmel

### 2.5 Verbundscheiben mit integrierter Antenne

Moderne Yachten integrieren zunehmend Antennen in die VSG-Windschutzscheibe:
- **GPS-Antenne**: Transparente leitfähige Schicht als Patch-Antenne
- **DVB-T/WiFi**: Antennenstruktur in der PVB-Zwischenschicht
- **5G/LTE**: Frequenzselektive Oberfläche (FSS) als Antennenelement
- Hersteller: **AGC** (Automotive-Technologie, marine Adaption), **Saint-Gobain Sekurit**

> Confidence: `estimated` (Technologien aus Automotive, marine Serienreife teilweise noch ausstehend)

---

## 3. Best Practices nach Revier

### 3.1 Mittelmeer (Sommer/Ganzjahr)

**Hauptprobleme:** Extreme UV-Belastung (UV-Index 9–11 im Sommer), Sonnenblendung bei West-/Ost-Kurs, Oberflächentemperatur Windschutzscheibe >80°C (dunkle Rahmen >95°C), Insekten in Marinas

**Empfehlungen:**

- **Getönte Scheiben** obligatorisch: Grau- oder Bronze-Tönung mit T_vis 55–65%. Grüntönung ungeeignet (verfälscht Farben von Bojen/Lichtern).
- **Solar-Control-Beschichtung** (Low-E auf Position 2 der VSG): Reduziert g-Wert von 0.78 auf 0.45, senkt Innentemperatur um 5–8°C.
- **Helle Rahmenfarben**: Silber, Weiß oder helles Grau. Schwarze Rahmen erreichen >95°C → Klebfugentemperatur übersteigt Dauerbelastbarkeit von Sikaflex-295 UV (max. 90°C kurzzeitig).
- **Wischer mit Frischwasseranlage**: Salzspritzer müssen sofort abgespült werden — eingetrocknetes Salz ätzt Glasoberfläche und zerstört Hydrophob-Beschichtung.
- **Sonnenschutz innen**: Rollos oder Jalousien für Liegezeiten — UV-Belastung der PVB-Folie in VSG reduzieren (Vergilbung nach 5–8 Jahren ohne Schutz).
- **Beheizte Scheiben**: Nicht nötig (außer für Überführungen im Winter).

**Typische Probleme im Mittelmeer:**
- PVB-Delaminierung an den Kanten durch UV + Feuchtigkeit → Scheibentausch nötig
- Klebfugenversagen durch Überhitzung → Rahmendesign mit Hinterlüftung wählen
- Glaskorrosion (Alkali-Auslaugung) bei minderwertigen Scheiben → nur Markenglas verwenden

**Bevorzugte Hersteller:** Trend Marine (Custom), Bohamet (gebogenes ESG/VSG), Nautiglass (Holland, gutes Preis-Leistungs-Verhältnis)

### 3.2 Nordeuropa / Ostsee / Nordsee / Ärmelkanal

**Hauptprobleme:** Beschlag/Kondensation (ΔT innen/außen bis 25°C), Eisbildung, schwerer Seegang (Beaufort 7–9), kurze Tage im Winter (Sichtbarkeit), Regen

**Empfehlungen:**

- **Beheizte Scheiben** obligatorisch für Ganzjahresboote: Heizdraht (150–250 W/m²) oder ITO-Beschichtung. Mindestens Frontscheibe im Hauptsichtfeld des Rudergängers.
- **Klare Scheiben** (T_vis ≥80%): Maximale Lichtdurchlässigkeit für kurze Wintertage. Keine dunkle Tönung — reduziert Erkennung von Navigationszeichen bei Dämmerung.
- **Entfeuchtungssystem**: Warmluftstrom auf die Scheibeninnenseite (Defogger) zusätzlich zur Scheibenheizung. Mindest-Luftvolumenstrom: 50 m³/h pro Frontscheibe.
- **Robuste Wischer**: Pantograph-Wischer für große Scheiben (Speich, Exalto). Pendelwischer mit ≥500 mm Armlänge für Motoryachten bis 15 m.
- **Doppelverglasung** empfohlen: Reduziert Kondensation drastisch. U-Wert von 5.8 W/(m²·K) (Einscheibe) auf 2.8 W/(m²·K) (Doppel) oder 1.4 W/(m²·K) (Dreifach mit Edelgas).
- **Rahmendichtungen**: EPDM (nicht Neopren — wird unter -10°C spröde). Silikon für arktische Bedingungen.

**Typische Probleme in Nordeuropa:**
- Kondensation führt zu Schimmelbildung in der Rahmendichtung
- Eisbildung blockiert Wischersysteme → Heizung muss vor Wischerbetrieb aktiviert werden
- Salzsprühnebel korrodiert Wischer-Motoren → nur 316L-Edelstahl-Komponenten

**Bevorzugte Hersteller:** Trend Marine (beheizte Systeme), Speich (Wischer + beheizte Scheiben), Exalto (Wischer), Vetus (Standardware)

### 3.3 Tropen / Blauwasser / Offshore

**Hauptprobleme:** Extreme UV (UV-Index 12+), Squalls mit Hagel, Ferndiagnose/Ersatzteilbeschaffung, Salzbelastung 24/7, Biostoffe (Algen, Vogelkot)

**Empfehlungen:**

- **VSG statt ESG**: Bei Bruch durch Gegenstand (fliegendes Teil bei Squall) bleibt VSG im Rahmen — ESG zerfällt sofort, vollständiger Sichtverlust.
- **Splitterschutzfolie** (Anti-Spall) auf VSG-Innenseite: Bei extremem Einschlag hält die Folie Glassplitter zurück.
- **Solartönung**: T_vis 50–60%, Solar Heat Rejection >60%. Reduziert UV-Eintrag um 99% (mit UV-absorbierender PVB-Folie).
- **Hydrophobe Beschichtung**: Langzeitbeschichtung (Gtechniq/Nanolex) — Salzwasser perlt ab, reduziert Reinigungsaufwand.
- **Ersatzscheibe an Bord**: Für Langfahrt-Yachten >40 ft empfohlen — Polycarbonate-Notscheibe (3–5 mm PC, zugeschnitten auf die größte Frontscheibe) mit Edelstahl-Schrauben und EPDM-Dichtmasse.
- **Wischerblätter als Verschleißteil**: 2 Sätze Ersatzblätter pro Wischer an Bord (Silikon-Blätter halten 2× länger als Gummi in UV).

**Bevorzugte Hersteller:** Trend Marine (Qualität), Freeman Marine (SOLAS-rated, robust), Roca (Wischer, robust)

### 3.4 Hochbreiten / Arktis / Antarktis

**Hauptprobleme:** Extreme Kälte (-40°C und darunter), Eisschlag auf Scheiben, Schneelast, Vereisung der Wischer, Polarfinsternis (dauerhafte Dunkelheit)

**Empfehlungen:**

- **Beheizte Scheiben obligatorisch**: Mindestens 300 W/m², besser 400 W/m². Heizung muss bei -40°C funktionieren.
- **VSG mit Sicherheitsfolie**: Spezial-PVB für Tieftemperatur (PVB bleibt flexibel bis -45°C, Standard-PVB wird spröde unter -20°C).
- **Silikon-Rahmendichtungen**: EPDM wird unter -30°C hart. Silikon funktioniert bis -60°C.
- **Wischer mit Heizelement**: Beheizte Wischerarme verhindern Festfrieren. Speich SWF-Serie mit integrierter Armheizung.
- **Doppel- oder Dreifachverglasung Pflicht**: U-Wert ≤1.5 W/(m²·K). Edelgas-Füllung (Argon/Krypton) für maximale Isolation.
- **Sturmblende (Storm Screen)**: Massive Aluminiumblende zum Vorsetzen bei schwerem Eisgang — schützt Glasscheibe vor mechanischem Eisschlag.

**Bevorzugte Hersteller:** Trend Marine (Expeditionsyachten), Freeman Marine (Ice-Class), Speich (Heizwischer)

> Confidence: `documented` (Erfahrungsberichte von Langfahrt-/Expeditionsyachten, Surveyor-Konsens, Hersteller-Empfehlungen)

---

## 4. Regional Sourcing

### 4.1 Europa

| Land | Anbieter | Spezialisierung | Lieferzeit | Bemerkung |
|------|---------|----------------|------------|-----------|
| UK | **Trend Marine** (Romsey) | Custom Windschutzscheiben, beheizt, Superyacht | 6–12 Wochen | Marktführer Yacht-Windschutzscheiben |
| UK | **Freeman Marine** (Agentur EU) | SOLAS-rated, Ice-Class | 8–16 Wochen | US-Fertigung, EU-Vertrieb |
| IT | **Speich** (Brescia) | Wischer + beheizte Scheiben | 4–8 Wochen | Breit verfügbar |
| IT | **Besenzoni** (Sarnico) | Premium-Scheiben, Sliding-Systeme | 6–10 Wochen | Superyacht-Segment |
| IT | **Osculati** (Mailand) | Standardware, Wischer, Scheiben | 1–3 Wochen | Budget/Retail |
| PL | **Bohamet** (Gdynia) | Gebogenes ESG/VSG, Custom | 4–8 Wochen | Gutes Preis-Leistungs-Verhältnis |
| NL | **Nautiglass** (Urk) | Yacht-Windschutzscheiben, gebogen | 4–8 Wochen | Holländische Werften |
| NL | **Vetus** (Schiedam) | Scheiben, Wischer, Standardware | 2–4 Wochen | Breites Sortiment |
| NL | **Exalto** (Almere) | Premium-Wischer, Scheibenwischer-Systeme | 2–6 Wochen | OEM für viele Werften |
| DE | **Hempel** (Lübeck) | Superyacht-Windschutzscheiben | 8–12 Wochen | Custom, Brandschutzglas |
| FR | **Euracryl** (La Rochelle) | Gebogenes Acrylglas (PMMA) | 4–8 Wochen | Spezialität: curved acrylic |
| ES | **Roca** (Barcelona) | Wischer-Systeme, marine Antriebe | 3–6 Wochen | Robust, bewährt |
| UK | **Lewmar** (Havant) | Standardscheiben, Luken, Fenster | 2–4 Wochen | Eher Luken als Windschutzscheiben |

### 4.2 Nordamerika

| Anbieter | Standort | Spezialisierung | Bemerkung |
|---------|---------|----------------|-----------|
| **Freeman Marine** | Gold Beach, OR | Custom Windschutzscheiben, SOLAS, Ice-Class | Premium, US-Marktführer |
| **Aritex** (US-Vertrieb) | Fort Lauderdale, FL | Superyacht-Windschutzscheiben | OEM für viele US-Werften |
| **Marine Window Mfg.** | Largo, FL | Standard-Windschutzscheiben, Ersatz | Mittleres Preissegment |
| **Taylor Made** | Gloversville, NY | Standard-Windschutzscheiben, OEM | Breit verfügbar, Budget bis Mittel |
| **Webasto** (Marine Div.) | Fenton, MI | Schiebedächer, Windschutzscheiben | Automotive-Qualität, marine adaptiert |

### 4.3 Asien / Rest der Welt

| Anbieter | Standort | Spezialisierung | Bemerkung |
|---------|---------|----------------|-----------|
| **Aritex** | Ningbo, China | Superyacht-Zulieferer, gebogenes Glas | CE-zertifiziert, wachsende Qualität |
| **Linyi Safety Glass** | Linyi, China | OEM Sicherheitsglas | Budget, Qualitätskontrolle nötig |
| **Asahi Glass (AGC)** | Tokyo, Japan | Premium-Floatglas, Spezialbeschichtungen | Automotive-Technologie |
| **Fuyao Glass** | Fuqing, China | Gebogenes VSG, OEM | Großer Automotive-Hersteller, marine Einstieg |

> Confidence: `documented` (Händler-Websites, Werftlisten, Marine-Fachhandel, Messen Boot Düsseldorf/METS)

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei dient dem AYDI-Analysemotor als Referenz für:

1. **Zustandsbewertung** von Windschutzscheiben und Frontfenstern (Pipeline A + B)
   - Visuelle Erkennung von Glasschäden (Risse, Kratzer, Delaminierung, Vergilbung)
   - Bewertung der Klebfuge (Ablösung, Rissbildung, UV-Degradation)
   - Beurteilung des Wischersystems (Verschleiß, Funktion, Abdeckung)
   - Prüfung der Scheibenheizung (Funktion, Gleichmäßigkeit)
   - Compliance-Check gegen ISO 12216, ISO 21005, ISO 3903

2. **Designbewertung** bei Neubauprojekten (Pipeline A)
   - Scheibentyp und -dicke für gegebene Bootslänge, Geschwindigkeit und CE-Kategorie
   - Rahmendesign und Materialauswahl
   - Wischer-System-Dimensionierung
   - Klebstoffauswahl und Klebflächenberechnung
   - Sichtfeld-Analyse und Ergonomie

3. **Kostenschätzung** (Pipeline A)
   - Neueinbau und Ersatz von Windschutzscheiben
   - Wischer-System-Kosten
   - Beheizung und Beschichtung
   - Material- und Arbeitskosten nach Bootslänge und Typ

4. **Wartungsplanung** (Pipeline C)
   - Intervalle für Wischerblatt-Wechsel, Dichtungsprüfung, Beschichtungserneuerung
   - Lebensdauer von VSG-Scheiben (PVB-Alterung)
   - Typische Schadensbilder und deren Ursachen

5. **Visuelle Analyse** (Pipeline B)
   - Referenzdaten für die Erkennung von Herstellern und Serien anhand von Fotos
   - Schadenskatalog mit Referenzbildern (Confidence-Stufen)
   - Geometrische Merkmale (flach/gebogen, Neigungswinkel, Rahmentyp)

---

## 6. Pydantic-Modelle

### 6.1 Enums

```python
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field


class WindshieldGlassType(str, Enum):
    """Glastyp der Windschutzscheibe."""
    TEMPERED_CLEAR = "tempered_clear"                 # ESG klar (Einscheibensicherheitsglas)
    TEMPERED_TINTED = "tempered_tinted"               # ESG getönt (Grau/Bronze/Grün)
    LAMINATED_CLEAR = "laminated_clear"               # VSG klar (Verbundsicherheitsglas)
    LAMINATED_TINTED = "laminated_tinted"             # VSG getönt
    LAMINATED_ACOUSTIC = "laminated_acoustic"         # VSG akustisch (Schallschutz-PVB)
    LAMINATED_SOLAR_CONTROL = "laminated_solar_control"  # VSG mit Solar-Control-Beschichtung
    LAMINATED_FIRE_RATED = "laminated_fire_rated"     # VSG brandschutzklassifiziert (SOLAS)
    ACRYLIC_CLEAR = "acrylic_clear"                   # Acrylglas (PMMA) klar
    ACRYLIC_TINTED = "acrylic_tinted"                 # Acrylglas getönt
    POLYCARBONATE_CLEAR = "polycarbonate_clear"       # Polycarbonat klar
    POLYCARBONATE_TINTED = "polycarbonate_tinted"     # Polycarbonat getönt
    DOUBLE_GLAZED_CLEAR = "double_glazed_clear"       # Isolierglas klar (Doppelverglasung)
    DOUBLE_GLAZED_TINTED = "double_glazed_tinted"     # Isolierglas getönt
    TRIPLE_GLAZED = "triple_glazed"                   # Dreifachverglasung
    ELECTROCHROMIC = "electrochromic"                 # Elektrochromes Glas (Smart Glass)


class WindshieldShape(str, Enum):
    """Geometrische Form der Windschutzscheibe."""
    FLAT = "flat"                                     # Planscheibe (flach)
    SINGLE_CURVED = "single_curved"                   # Einfach gebogen (Zylinder-Segment)
    COMPOUND_CURVED = "compound_curved"               # Mehrfach gebogen (Sphärisches Segment)
    WRAP_AROUND = "wrap_around"                       # Umlaufend gebogen (Front + Seite)
    V_SHAPED = "v_shaped"                             # V-förmig (zwei Flachscheiben im Winkel)
    RAKED = "raked"                                   # Stark geneigt (>30° zur Vertikalen)
    REVERSE_RAKED = "reverse_raked"                   # Nach vorne geneigt (selten, Retrodesign)


class WindshieldFrameMaterial(str, Enum):
    """Rahmenmaterial der Windschutzscheibe."""
    ALUMINUM_ANODIZED = "aluminum_anodized"           # Eloxiertes Aluminium
    ALUMINUM_PAINTED = "aluminum_painted"             # Lackiertes Aluminium
    ALUMINUM_POWDER_COATED = "aluminum_powder_coated" # Pulverbeschichtetes Aluminium
    STAINLESS_316L = "stainless_316l"                 # Edelstahl 316L (Marine Grade)
    STAINLESS_DUPLEX = "stainless_duplex"             # Duplex-Edelstahl (Superyacht)
    GRP_COMPOSITE = "grp_composite"                   # GFK/Composite (in Aufbau integriert)
    CARBON_COMPOSITE = "carbon_composite"             # CFK (Leichtbau, Racing)
    FRAMELESS = "frameless"                           # Rahmenlos (Structural Glazing only)
    BRONZE = "bronze"                                 # Bronze (klassische Yachten)


class WindshieldMountType(str, Enum):
    """Montage-/Befestigungstyp der Windschutzscheibe."""
    STRUCTURAL_GLAZING = "structural_glazing"         # Strukturell verklebt (ISO 21005)
    MECHANICAL_GASKET = "mechanical_gasket"            # Mechanisch mit Gummidichtung
    MECHANICAL_CLAMP = "mechanical_clamp"              # Mechanisch mit Klemmleiste
    BOLT_ON_FRAME = "bolt_on_frame"                    # Verschraubter Rahmen
    BONDED_PLUS_MECHANICAL = "bonded_plus_mechanical"  # Verklebt + mechanische Sicherung
    CHANNEL_MOUNT = "channel_mount"                    # Eingeschobene Scheibe in U-Profil


class WindshieldOpeningType(str, Enum):
    """Öffnungsmechanismus (falls vorhanden)."""
    FIXED = "fixed"                                   # Fest, nicht öffnend
    SLIDING_HORIZONTAL = "sliding_horizontal"         # Horizontal schiebend
    SLIDING_VERTICAL = "sliding_vertical"             # Vertikal schiebend (Drop-Down)
    TILTING_TOP = "tilting_top"                        # Oben kippend
    TILTING_BOTTOM = "tilting_bottom"                  # Unten kippend
    FOLDING = "folding"                               # Zusammenklappbar (Center Consoles)
    REMOVABLE = "removable"                           # Abnehmbar
    POWER_SLIDING = "power_sliding"                   # Elektrisch schiebend
    POWER_TILTING = "power_tilting"                    # Elektrisch kippend


class WiperType(str, Enum):
    """Wischer-Typ."""
    SWING_ARM = "swing_arm"                           # Pendelwischer (Standard)
    PANTOGRAPH = "pantograph"                         # Pantograph-Wischer
    TWIN_ARM = "twin_arm"                             # Doppelarm-Wischer
    CONCEALED = "concealed"                           # Verdeckter Wischer
    NONE = "none"                                     # Kein Wischer


class WiperBladeType(str, Enum):
    """Wischerblatt-Typ."""
    RUBBER_STANDARD = "rubber_standard"               # Standard-Gummi
    SILICONE = "silicone"                             # Silikon (UV-beständiger)
    FLAT_BEAM = "flat_beam"                           # Flachbalken (aerodynamisch)
    HEATED = "heated"                                 # Beheizt (Anti-Eis)


class HeatingType(str, Enum):
    """Beheizungstyp der Windschutzscheibe."""
    NONE = "none"                                     # Keine Beheizung
    WIRE_HEATED = "wire_heated"                       # Heizdraht-Matrix
    ITO_COATED = "ito_coated"                         # ITO-Beschichtung (transparente Heizschicht)
    HOT_AIR_DEFOG = "hot_air_defog"                   # Warmluft-Entbeschlagung (Defogger)
    COMBINED_WIRE_DEFOG = "combined_wire_defog"       # Heizdraht + Warmluft


class WindshieldLocation(str, Enum):
    """Position der Windschutzscheibe auf dem Boot."""
    HELM_MAIN = "helm_main"                           # Hauptsteuerstand Frontscheibe
    HELM_PORT = "helm_port"                           # Hauptsteuerstand Backbord
    HELM_STARBOARD = "helm_starboard"                 # Hauptsteuerstand Steuerbord
    HELM_WRAP_PORT = "helm_wrap_port"                 # Wrap-around Backbord
    HELM_WRAP_STARBOARD = "helm_wrap_starboard"       # Wrap-around Steuerbord
    FLYBRIDGE_MAIN = "flybridge_main"                 # Flybridge Frontscheibe
    FLYBRIDGE_PORT = "flybridge_port"                 # Flybridge Backbord
    FLYBRIDGE_STARBOARD = "flybridge_starboard"       # Flybridge Steuerbord
    PILOTHOUSE_MAIN = "pilothouse_main"               # Decksalon/Pilothouse Front
    PILOTHOUSE_PORT = "pilothouse_port"               # Decksalon Backbord
    PILOTHOUSE_STARBOARD = "pilothouse_starboard"     # Decksalon Steuerbord
    CENTER_CONSOLE = "center_console"                 # Center Console Windschutz
    AFT_HELM = "aft_helm"                             # Achtersteuerstand


class CECategory(str, Enum):
    """CE Design-Kategorie."""
    A = "A"  # Hochsee
    B = "B"  # Offshore
    C = "C"  # Küstennah
    D = "D"  # Geschützt


class ConfidenceLevel(str, Enum):
    """Confidence-Level für AYDI-Bewertungen."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"
```

### 6.2 WindshieldSpec

```python
class WindshieldSpec(BaseModel):
    """Vollständige Spezifikation einer einzelnen Windschutzscheibe.

    Dient als Input für die AYDI-Analyse-Engine (Pipeline A).
    Alle Maße in mm, Gewichte in kg, Preise in EUR.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(
        ...,
        description="Windschutzscheiben-Hersteller (z.B. 'Trend Marine', 'Bohamet', 'Nautiglass')"
    )
    series: Optional[str] = Field(
        None,
        description="Hersteller-Serie (z.B. 'TM1000', 'Panorama', 'ClearView')"
    )
    model_number: Optional[str] = Field(
        None,
        description="Hersteller-Modellnummer"
    )
    part_number: Optional[str] = Field(
        None,
        description="OEM-Teilenummer"
    )

    # Geometrie
    shape: WindshieldShape = Field(
        WindshieldShape.FLAT,
        description="Geometrische Form"
    )
    width_mm: float = Field(
        ...,
        ge=200, le=6000,
        description="Breite der Scheibe in mm (horizontale Erstreckung)"
    )
    height_mm: float = Field(
        ...,
        ge=150, le=2500,
        description="Höhe der Scheibe in mm (vertikale Erstreckung)"
    )
    thickness_mm: float = Field(
        ...,
        ge=3.0, le=50.0,
        description="Gesamt-Scheibendicke in mm (bei VSG: Summe aller Schichten)"
    )
    curvature_radius_mm: Optional[float] = Field(
        None,
        ge=500,
        description="Biegeradius bei gebogenen Scheiben in mm (None = flach)"
    )
    rake_angle_deg: float = Field(
        0.0,
        ge=-15.0, le=75.0,
        description="Neigungswinkel zur Vertikalen in Grad (0 = senkrecht, 45 = stark geneigt)"
    )
    corner_radius_mm: float = Field(
        0.0,
        ge=0.0, le=200.0,
        description="Eckenradius der Scheibe in mm (0 = scharfe Ecke)"
    )
    area_m2: Optional[float] = Field(
        None,
        ge=0.01, le=20.0,
        description="Scheibenfläche in m² (berechnet oder gemessen)"
    )

    # Glasaufbau
    glass_type: WindshieldGlassType = Field(
        WindshieldGlassType.LAMINATED_CLEAR,
        description="Glastyp / Scheibenaufbau"
    )
    outer_pane_mm: Optional[float] = Field(
        None,
        ge=2.0, le=25.0,
        description="Dicke Außenscheibe in mm (bei VSG/Isolierglas)"
    )
    inner_pane_mm: Optional[float] = Field(
        None,
        ge=2.0, le=25.0,
        description="Dicke Innenscheibe in mm (bei VSG/Isolierglas)"
    )
    interlayer_mm: Optional[float] = Field(
        None,
        ge=0.38, le=4.0,
        description="Dicke Zwischenschicht in mm (PVB: 0.38/0.76/1.14/1.52)"
    )
    interlayer_type: Optional[str] = Field(
        None,
        description="Typ der Zwischenschicht (z.B. 'PVB', 'EVA', 'SGP', 'Acoustic PVB')"
    )
    light_transmission_pct: Optional[float] = Field(
        None,
        ge=1.0, le=95.0,
        description="Lichttransmission T_vis in % (70+ = klar, 50-70 = leicht getönt, <50 = dunkel)"
    )
    uv_rejection_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="UV-Abweisung in % (typisch 95-99% bei VSG mit PVB)"
    )
    solar_heat_gain: Optional[float] = Field(
        None,
        ge=0.0, le=1.0,
        description="Gesamtenergiedurchlassgrad g-Wert (0.0-1.0, niedriger = weniger Wärme)"
    )
    u_value: Optional[float] = Field(
        None,
        ge=0.5, le=6.0,
        description="Wärmedurchgangskoeffizient U in W/(m²·K)"
    )
    tint_color: Optional[str] = Field(
        None,
        description="Tönungsfarbe (z.B. 'grey', 'bronze', 'green', 'blue', 'clear')"
    )

    # Rahmen
    frame_material: WindshieldFrameMaterial = Field(
        WindshieldFrameMaterial.ALUMINUM_ANODIZED,
        description="Rahmenmaterial"
    )
    frame_width_mm: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Sichtbare Rahmenbreite in mm (0 = rahmenlos)"
    )
    frame_depth_mm: Optional[float] = Field(
        None,
        ge=0.0, le=80.0,
        description="Rahmentiefe (Einbautiefe) in mm"
    )
    frame_finish: Optional[str] = Field(
        None,
        description="Rahmenoberfläche (z.B. 'satin_anodized', 'black_powder_coated', 'polished')"
    )

    # Montage
    mount_type: WindshieldMountType = Field(
        WindshieldMountType.STRUCTURAL_GLAZING,
        description="Montageart"
    )
    adhesive_product: Optional[str] = Field(
        None,
        description="Klebstoff-Produkt (z.B. 'Sikaflex-295 UV', 'Simson ISR 70-03')"
    )
    bond_width_mm: Optional[float] = Field(
        None,
        ge=5.0, le=80.0,
        description="Klebflächenbreite in mm"
    )
    mechanical_retention: Optional[bool] = Field(
        None,
        description="Mechanische Rückhaltesicherung vorhanden (zusätzlich zur Verklebung)"
    )

    # Öffnungsmechanismus
    opening_type: WindshieldOpeningType = Field(
        WindshieldOpeningType.FIXED,
        description="Öffnungsmechanismus"
    )
    opening_width_mm: Optional[float] = Field(
        None,
        description="Öffnungsbreite in mm (bei Schiebe-/Kipp-Windschutzscheiben)"
    )
    opening_height_mm: Optional[float] = Field(
        None,
        description="Öffnungshöhe in mm"
    )

    # Beheizung
    heating_type: HeatingType = Field(
        HeatingType.NONE,
        description="Beheizungstyp"
    )
    heating_power_w: Optional[float] = Field(
        None,
        ge=0.0, le=5000.0,
        description="Heizleistung in Watt (gesamt pro Scheibe)"
    )
    heating_voltage: Optional[int] = Field(
        None,
        description="Heizspannung in Volt (typisch 12, 24, 110, 230)"
    )

    # Wischer
    wiper_type: WiperType = Field(
        WiperType.NONE,
        description="Wischer-Typ"
    )
    wiper_manufacturer: Optional[str] = Field(
        None,
        description="Wischer-Hersteller (z.B. 'Speich', 'Exalto', 'Roca', 'Vetus')"
    )
    wiper_model: Optional[str] = Field(
        None,
        description="Wischer-Modell"
    )
    wiper_arm_length_mm: Optional[float] = Field(
        None,
        ge=200, le=1000,
        description="Wischerarm-Länge in mm"
    )
    wiper_blade_length_mm: Optional[float] = Field(
        None,
        ge=250, le=800,
        description="Wischerblatt-Länge in mm"
    )
    wiper_blade_type: Optional[WiperBladeType] = Field(
        None,
        description="Wischerblatt-Typ"
    )
    wiper_coverage_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Wischer-Abdeckung in % der Scheibenfläche"
    )
    washer_system: Optional[bool] = Field(
        None,
        description="Scheibenwaschanlage vorhanden"
    )

    # Beschichtung
    hydrophobic_coating: Optional[bool] = Field(
        None,
        description="Hydrophobe Beschichtung vorhanden"
    )
    hydrophobic_product: Optional[str] = Field(
        None,
        description="Hydrophob-Produkt (z.B. 'Nanolex Si3D Marine', 'Rain-X Marine')"
    )
    anti_reflective_coating: Optional[bool] = Field(
        None,
        description="Antireflexbeschichtung vorhanden"
    )
    low_e_coating: Optional[bool] = Field(
        None,
        description="Low-E-Beschichtung vorhanden (Wärmedämmung)"
    )

    # Position
    location: WindshieldLocation = Field(
        WindshieldLocation.HELM_MAIN,
        description="Position auf dem Boot"
    )
    height_above_wl_mm: Optional[float] = Field(
        None,
        ge=500, le=15000,
        description="Unterkante Scheibe über Konstruktionswasserlinie in mm"
    )
    iso_position_class: Optional[str] = Field(
        None,
        description="ISO 12216 Positionsklasse (z.B. '1A', '1B', '2', '3')"
    )

    # Gewicht und Preis
    weight_kg: Optional[float] = Field(
        None,
        ge=0.5, le=500.0,
        description="Gewicht der Scheibe inkl. Rahmen in kg"
    )
    price_eur: Optional[float] = Field(
        None,
        ge=50, le=100000,
        description="Preis in EUR (Scheibe + Rahmen, ohne Einbau)"
    )
    installation_cost_eur: Optional[float] = Field(
        None,
        ge=50, le=50000,
        description="Einbaukosten in EUR"
    )

    # CE/Norm
    ce_category: Optional[CECategory] = Field(
        None,
        description="CE-Designkategorie für die das Fenster zugelassen ist"
    )
    iso_12216_compliant: Optional[bool] = Field(
        None,
        description="Konformität mit ISO 12216:2020"
    )
    iso_21005_compliant: Optional[bool] = Field(
        None,
        description="Konformität mit ISO 21005:2018 (Structural Glazing)"
    )
    solas_fire_rating: Optional[str] = Field(
        None,
        description="SOLAS-Brandschutzklasse (z.B. 'A-0', 'A-15', 'A-30', 'A-60', None)"
    )
    classification_society: Optional[str] = Field(
        None,
        description="Klassifikationsgesellschaft (z.B. 'LR', 'DNV', 'BV', 'RINA', None)"
    )
```

### 6.3 WindshieldCondition

```python
class WindshieldCondition(BaseModel):
    """Zustandsbeurteilung einer einzelnen verbauten Windschutzscheibe.

    Wird von Pipeline A (Inspektion) und Pipeline B (Foto-Analyse) befüllt.
    Jeder Zustandswert hat ein eigenes Confidence-Feld.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    windshield_id: str = Field(
        ...,
        description="Eindeutige ID der Windschutzscheibe im Boot (z.B. 'helm_main', 'flybridge_center')"
    )
    boat_manufacturer: Optional[str] = Field(
        None,
        description="Bootshersteller"
    )
    boat_model: Optional[str] = Field(
        None,
        description="Bootsmodell"
    )
    boat_year: Optional[int] = Field(
        None,
        description="Baujahr"
    )
    windshield_manufacturer: Optional[str] = Field(
        None,
        description="Windschutzscheiben-Hersteller (erkannt oder dokumentiert)"
    )
    windshield_age_years: Optional[float] = Field(
        None,
        ge=0.0, le=60.0,
        description="Alter der Windschutzscheibe in Jahren (falls bekannt)"
    )
    location: WindshieldLocation = Field(
        WindshieldLocation.HELM_MAIN,
        description="Position auf dem Boot"
    )

    # Glasschäden
    glass_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Gesamtbewertung Glasscheibe (0=defekt, 100=neuwertig)"
    )
    glass_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Glasbewertung"
    )
    cracks_present: Optional[bool] = Field(
        None,
        description="Risse in der Scheibe vorhanden"
    )
    crack_type: Optional[str] = Field(
        None,
        description="Risstyp (z.B. 'star', 'bull_eye', 'edge_crack', 'stress_crack', 'thermal_crack')"
    )
    crack_length_mm: Optional[float] = Field(
        None,
        ge=0.0,
        description="Maximale Risslänge in mm"
    )
    scratches_severity: Optional[str] = Field(
        None,
        description="Kratzer-Schweregrad: 'none', 'light' (Polierbar), 'medium' (Sichtbar), 'heavy' (Sichtbeeinträchtigend)"
    )
    delamination_present: Optional[bool] = Field(
        None,
        description="Delaminierung der VSG-Zwischenschicht vorhanden"
    )
    delamination_area_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Delaminierte Fläche in % der Gesamtscheibenfläche"
    )
    delamination_location: Optional[str] = Field(
        None,
        description="Position der Delaminierung (z.B. 'edge', 'center', 'corner', 'widespread')"
    )
    yellowing_present: Optional[bool] = Field(
        None,
        description="Vergilbung der PVB-Folie (bei VSG) oder des Acrylglases"
    )
    yellowing_severity: Optional[str] = Field(
        None,
        description="Vergilbungsgrad: 'none', 'slight', 'moderate', 'severe'"
    )
    haze_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Trübung (Haze) in % (0 = klar, >5% = sichtbar, >15% = beeinträchtigend)"
    )
    stress_marks_visible: Optional[bool] = Field(
        None,
        description="Spannungsdoppelbrechung sichtbar (bei ESG unter Polfilter)"
    )
    chips_count: Optional[int] = Field(
        None,
        ge=0,
        description="Anzahl Muschelausbrüche (Chips) an den Kanten"
    )
    optical_distortion: Optional[str] = Field(
        None,
        description="Optische Verzerrung: 'none', 'slight', 'moderate', 'severe'"
    )

    # Klebfuge / Montage
    bond_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Bewertung Klebfuge / Montage (0=versagt, 100=neuwertig)"
    )
    bond_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Montagebewertung"
    )
    bond_separation: Optional[bool] = Field(
        None,
        description="Klebfugen-Ablösung vorhanden"
    )
    bond_separation_length_mm: Optional[float] = Field(
        None,
        ge=0.0,
        description="Länge der Klebfugen-Ablösung in mm"
    )
    bond_cracking: Optional[bool] = Field(
        None,
        description="Risse in der Klebfuge (UV-Degradation)"
    )
    bond_discoloration: Optional[bool] = Field(
        None,
        description="Verfärbung der Klebfuge (Vergilbung, Kreidung)"
    )
    water_ingress: Optional[bool] = Field(
        None,
        description="Wassereinbruch an der Scheibe festgestellt"
    )
    water_ingress_location: Optional[str] = Field(
        None,
        description="Position des Wassereinbruchs (z.B. 'top_edge', 'bottom_edge', 'corner', 'frame_joint')"
    )

    # Rahmen
    frame_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Bewertung Rahmen (0=versagt, 100=neuwertig)"
    )
    frame_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Rahmenbewertung"
    )
    frame_corrosion: Optional[str] = Field(
        None,
        description="Korrosion am Rahmen: 'none', 'surface' (Oberflächenkorrosion), 'pitting' (Lochfraß), 'structural' (Tragfähigkeit beeinträchtigt)"
    )
    frame_seal_condition: Optional[str] = Field(
        None,
        description="Zustand der Rahmendichtung: 'good', 'hardened', 'cracked', 'missing', 'compressed'"
    )
    frame_fastener_condition: Optional[str] = Field(
        None,
        description="Zustand der Befestigungselemente: 'good', 'corroded', 'loose', 'missing'"
    )

    # Wischer
    wiper_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Bewertung Wischer-System (0=defekt, 100=neuwertig)"
    )
    wiper_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Wischerbewertung"
    )
    wiper_blade_condition: Optional[str] = Field(
        None,
        description="Zustand Wischerblatt: 'good', 'streaking', 'chattering', 'torn', 'missing'"
    )
    wiper_motor_functional: Optional[bool] = Field(
        None,
        description="Wischermotor funktionsfähig"
    )
    wiper_arm_corrosion: Optional[str] = Field(
        None,
        description="Korrosion am Wischerarm: 'none', 'surface', 'pitting', 'structural'"
    )
    washer_functional: Optional[bool] = Field(
        None,
        description="Scheibenwaschanlage funktionsfähig"
    )
    wiper_coverage_adequate: Optional[bool] = Field(
        None,
        description="Wischerabdeckung ausreichend (≥80% der Scheibenfläche)"
    )

    # Beheizung
    heating_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Bewertung Scheibenheizung (0=defekt, 100=neuwertig, None=nicht vorhanden)"
    )
    heating_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Heizungsbewertung"
    )
    heating_functional: Optional[bool] = Field(
        None,
        description="Scheibenheizung funktionsfähig"
    )
    heating_uniform: Optional[bool] = Field(
        None,
        description="Heizverteilung gleichmäßig (keine kalten Stellen)"
    )
    heating_wire_visible: Optional[bool] = Field(
        None,
        description="Heizdrähte sichtbar (Ästhetik-Problem)"
    )

    # Gesamtbewertung
    overall_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Gesamtbewertung der Windschutzscheibe (0=Sofortersatz, 100=neuwertig)"
    )
    overall_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Gesamtbewertung"
    )
    action_required: Optional[str] = Field(
        None,
        description="Handlungsempfehlung: 'none', 'monitor', 'repair', 'replace_soon', 'replace_immediately'"
    )
    findings: List[str] = Field(
        default_factory=list,
        description="Liste aller Befunde als Freitext"
    )
    suggestions: List[str] = Field(
        default_factory=list,
        description="Liste aller Verbesserungsvorschläge"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None,
        ge=0.0,
        description="Geschätzte Kosten für Scheibentausch in EUR (Material + Arbeit)"
    )
```

### 6.4 WindshieldSystemAssessment

```python
class WindshieldSystemAssessment(BaseModel):
    """Gesamtbewertung des Windschutzscheiben-Systems eines Bootes.

    Aggregiert alle Einzelscheiben-Bewertungen und prüft Systemaspekte
    (Normkonformität, Sichtfeld-Analyse, Wischer-Abdeckung, Beheizung).
    """
    model_config = {"from_attributes": True}

    # Boot-Identifikation
    boat_manufacturer: str = Field(..., description="Bootshersteller")
    boat_model: str = Field(..., description="Bootsmodell")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    boat_length_mm: Optional[float] = Field(None, description="Bootslänge (LOA) in mm")
    boat_class: str = Field(
        "production_motorboat",
        description="Bootsklasse: production_sailboat, semicustom_cruiser, "
                    "custom_yacht, superyacht, production_motorboat, center_console"
    )
    ce_category: CECategory = Field(
        CECategory.C,
        description="CE-Designkategorie des Bootes"
    )
    max_speed_kn: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Maximale Geschwindigkeit in Knoten"
    )

    # Einzelscheiben
    windshield_count: int = Field(0, description="Gesamtanzahl Windschutzscheiben/Frontfenster")
    windshields: List[WindshieldCondition] = Field(
        default_factory=list,
        description="Liste aller bewerteten Einzelscheiben"
    )

    # Normkonformität
    iso_12216_compliant: Optional[bool] = Field(
        None,
        description="Gesamtsystem konform mit ISO 12216:2020"
    )
    iso_12216_findings: List[str] = Field(
        default_factory=list,
        description="Einzelbefunde ISO 12216"
    )
    iso_21005_compliant: Optional[bool] = Field(
        None,
        description="Structural Glazing konform mit ISO 21005:2018"
    )
    iso_21005_findings: List[str] = Field(
        default_factory=list,
        description="Einzelbefunde ISO 21005"
    )
    iso_3903_compliant: Optional[bool] = Field(
        None,
        description="Wischer-System konform mit ISO 3903:2020"
    )
    iso_3903_findings: List[str] = Field(
        default_factory=list,
        description="Einzelbefunde ISO 3903"
    )

    # Sichtfeld-Analyse
    visibility_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Sichtfeld-Bewertung (0=stark eingeschränkt, 100=hervorragend)"
    )
    visibility_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Sichtfeldbewertung"
    )
    blind_spots_identified: List[str] = Field(
        default_factory=list,
        description="Identifizierte tote Winkel (z.B. 'A-pillar port', 'wiper park position')"
    )
    forward_visibility_deg: Optional[float] = Field(
        None,
        ge=0.0, le=360.0,
        description="Horizontales Sichtfeld nach vorn in Grad"
    )

    # Wischer-System-Analyse
    wiper_system_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Gesamtbewertung Wischer-System"
    )
    wiper_total_coverage_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Gesamte Wischerabdeckung aller Frontscheiben in %"
    )
    wiper_system_findings: List[str] = Field(
        default_factory=list,
        description="Befunde zum Wischer-System"
    )

    # Beheizung
    heating_system_present: Optional[bool] = Field(
        None,
        description="Scheibenheizung im Boot vorhanden"
    )
    heating_coverage_pct: Optional[float] = Field(
        None,
        ge=0.0, le=100.0,
        description="Anteil beheizter Frontscheiben in %"
    )
    heating_total_power_w: Optional[float] = Field(
        None,
        ge=0.0,
        description="Gesamte Heizleistung aller Scheiben in Watt"
    )
    heating_adequate: Optional[bool] = Field(
        None,
        description="Heizleistung ausreichend für das Revier"
    )

    # Gesamtbewertung
    overall_score: Optional[int] = Field(
        None,
        ge=0, le=100,
        description="Gesamtbewertung des Windschutzscheiben-Systems"
    )
    overall_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence-Level der Gesamtbewertung"
    )
    critical_findings: List[str] = Field(
        default_factory=list,
        description="Kritische Befunde (sofortiger Handlungsbedarf)"
    )
    recommendations: List[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
    estimated_total_cost_eur: Optional[float] = Field(
        None,
        ge=0.0,
        description="Geschätzte Gesamtkosten für alle Maßnahmen in EUR"
    )

    # AYDI-Meta
    analysis_timestamp: Optional[str] = Field(
        None,
        description="Zeitstempel der Analyse (ISO 8601)"
    )
    analyzer_version: Optional[str] = Field(
        None,
        description="Version des AYDI-Analysators"
    )
    data_sources: List[str] = Field(
        default_factory=list,
        description="Datenquellen der Analyse (z.B. 'pipeline_a_cad', 'pipeline_b_photo', 'pipeline_c_report')"
    )
```

> Confidence: `measured` (Pydantic v2 Syntax, AYDI-Konventionen)

---

## 7. Grundlagen

### 7.1 Flache vs. Gebogene Windschutzscheiben

#### 7.1.1 Flache Windschutzscheiben (Flat Windshields)

**Konstruktion:** Planscheiben, entweder als Einzelscheibe oder als V-Konfiguration (zwei Flachscheiben im Winkel zueinander). Einfachste und kostengünstigste Variante.

**Vorteile:**
- Niedrigste Kosten: Standardglas, keine Biegekosten
- Keine optische Verzerrung durch Biegung
- Einfacher Austausch — Ersatzscheiben überall lieferbar
- Wischer arbeiten auf Flachscheiben gleichmäßiger
- V-Konfiguration reduziert Spiegelungen und Blendung

**Nachteile:**
- Ästhetisch weniger modern
- Kein aerodynamischer Vorteil
- Seitliche Sicht nur durch separate Seitenscheiben
- Spiegelungen bei aufrechten Flachscheiben (Armaturenbrett spiegelt sich in der Scheibe)

**Typische Anwendung:**
- Arbeitstrawler, Fischer-Boote, klassische Motoryachten
- Segelyacht-Pilothouse (Tradition)
- Center Consoles (als Klappscheibe)
- Budget-Sportboote

**Glas-Spezifikationen Flachscheibe:**

| Parameter | Wert | Bemerkung |
|-----------|------|-----------|
| Material | ESG oder VSG | ESG günstiger, VSG sicherer |
| Dicke (Standardboot 8–12 m) | 6–10 mm | Abhängig von Fläche und CE-Kategorie |
| Dicke (Yacht 12–24 m) | 8–16 mm | VSG empfohlen |
| Toleranz | ±0.5 mm Dicke, ±1 mm Kantenlänge | Standard-Glastoleranzen |
| Kantenbearbeitung | Geschliffen (KGS) oder poliert (KPO) | Poliert für sichtbare Kanten |
| Bohrungen (für Befestigung) | Durchmesser ≥3× Glasdicke | Mindestabstand Bohrung-Kante: 2× Glasdicke |
| Preis Flachscheibe ESG (EUR/m²) | 120–250 | 6–10 mm, klar |
| Preis Flachscheibe VSG (EUR/m²) | 200–450 | 6+0.76+6 mm, klar |

#### 7.1.2 Einfach Gebogene Windschutzscheiben (Single-Curved)

**Konstruktion:** Zylindrisches Segment — die Scheibe ist in einer Achse gebogen. Kann in ESG oder VSG gefertigt werden. Die Biegung erfolgt thermisch (bei ESG: gleichzeitig mit der Vorspannung, bei VSG: Biegung der Einzelscheiben vor der Lamination).

**Herstellungsprozess:**
1. Floatglas auf Maß zuschneiden
2. Kanten schleifen
3. Erhitzen auf ~620°C (Erweichungstemperatur)
4. Über Biegeform biegen (Schwerkraftbiegen oder Pressbiegen)
5. Bei ESG: Schnelles Abkühlen (Vorspannen) — bei VSG: Langsames Abkühlen, dann mit PVB-Folie laminieren

**Typische Biegeradien:**

| Anwendung | Biegeradius (mm) | Bemerkung |
|-----------|-----------------|-----------|
| Leichte Biegung (optisch nahezu flach) | >3.000 | Spannungsarm, günstig |
| Standard-Yacht-Windschutzscheibe | 1.500–3.000 | Standardproduktion |
| Stark gebogen (Panorama) | 800–1.500 | Aufwendiger, teurer |
| Extrem gebogen (Wrap-around) | 500–800 | Nur bei Spezialherstellern (Bohamet, Trend Marine) |
| Untergrenze (Mindestradius ESG) | ~350 mm bei 6 mm Dicke | Glasdicken-abhängig |

**Preise gebogenes Glas (Aufpreis gegenüber Flachscheibe):**

| Biegeradius (mm) | Aufpreis ESG | Aufpreis VSG |
|-----------------|-------------|-------------|
| >3.000 | +30–50% | +30–50% |
| 1.500–3.000 | +50–80% | +50–80% |
| 800–1.500 | +80–120% | +100–150% |
| 500–800 | +120–200% | +150–250% |

**Hersteller gebogenes Glas:**

| Hersteller | Standort | Min. Radius (mm) | Max. Größe (mm) | Bemerkung |
|-----------|---------|-----------------|----------------|-----------|
| **Bohamet** | Gdynia, Polen | 400 (ESG), 600 (VSG) | 3.200 × 2.000 | Spezialist, gutes P/L |
| **Trend Marine** | Romsey, UK | 500 | 4.000 × 2.500 | Marktführer, Premium |
| **Nautiglass** | Urk, NL | 600 | 2.800 × 1.800 | Holländische Werften |
| **Pilkington Marine** | Lathom, UK | 350 (ESG) | 3.500 × 2.200 | Weltkonzern, Standardware |
| **AGC Interpane** | Plattling, DE | 500 | 3.000 × 2.000 | Industriequalität |
| **Glaston** (Biegemaschinen) | Tampere, FI | — | — | Maschinenhersteller, nicht Glaslieferant |

> Confidence: `measured` (Hersteller-Datenblätter, EN 12150 ESG, ISO 12543 VSG)

#### 7.1.3 Mehrfach Gebogene Windschutzscheiben (Compound-Curved)

**Konstruktion:** Sphärisches Segment — die Scheibe ist in zwei Achsen gebogen. Deutlich aufwendiger in der Herstellung, da das Glas über eine dreidimensionale Form gebogen werden muss. Nur möglich mit Schwerkraftbiegen (Gravity Bending) oder Pressbiegen.

**Einschränkungen:**
- Nur VSG möglich (ESG-Vorspannung ist bei compound curves nicht gleichmäßig durchführbar)
- Hohe optische Verzerrung möglich — kritisch für Navigationssicht
- Jede Scheibe ist eine Einzelanfertigung (kundenspezifische Form)
- Biegeform (Mold) muss für jede Scheibengeometrie neu erstellt werden: 3.000–15.000 EUR Werkzeugkosten
- Lieferzeit: 8–16 Wochen (inkl. Formbau)

**Typische Anwendung:**
- Superyachten (>24 m) mit Design-Priorität
- Moderne Express-Cruiser
- Luxus-Sportboote

**Preise compound-curved:**

| Scheibenfläche (m²) | Preis pro Scheibe (EUR) | Werkzeugkosten (EUR) | Bemerkung |
|---------------------|------------------------|---------------------|-----------|
| 0.5–1.0 | 1.500–4.000 | 3.000–5.000 | Inkl. VSG, ohne Rahmen |
| 1.0–2.0 | 3.000–8.000 | 5.000–10.000 | |
| 2.0–4.0 | 6.000–15.000 | 8.000–15.000 | Superyacht-Segment |
| >4.0 | 12.000–40.000 | 10.000–25.000 | Einzelstück, Premium |

**Hersteller compound-curved:**

| Hersteller | Standort | Spezialisierung | Lieferzeit |
|-----------|---------|----------------|------------|
| **Trend Marine** | Romsey, UK | Marktführer für compound-curved Yacht-Windschutzscheiben | 10–16 Wochen |
| **Bohamet** | Gdynia, PL | Starke Compound-Curve-Fähigkeit, konkurrenzfähige Preise | 8–14 Wochen |
| **Hempel** | Lübeck, DE | Superyacht-Segment, Brandschutzglas | 12–20 Wochen |
| **Freeman Marine** | Gold Beach, OR, USA | SOLAS-zertifiziert, Ice-Class | 12–20 Wochen |

> Confidence: `measured` (Hersteller-Kataloge), `estimated` (Preise sind Richtwerte, projektabhängig)

### 7.2 Glastypen im Detail

#### 7.2.1 Einscheibensicherheitsglas (ESG / Tempered Glass)

**Herstellung:** Floatglas wird auf ~620°C erhitzt und schnell mit Luft abgekühlt (gehärtet). Dadurch entsteht eine Druckspannung in der Oberfläche (80–120 MPa) und eine Zugspannung im Kern. Die Oberfläche ist ca. 4–5× fester als normales Floatglas.

**Eigenschaften für Windschutzscheiben:**

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Biegefestigkeit | 120–150 MPa | vs. 30–40 MPa Floatglas |
| Zul. Spannung (ISO 12216) | 35 MPa | Sicherheitsfaktor ~3.5 |
| Thermische Beständigkeit | ΔT ≤200°C | vs. 40°C bei Floatglas |
| Bruchverhalten | Zerfällt in kleine, stumpfe Würfel | Keine großen scharfen Splitter |
| Nachbearbeitung nach Härtung | NICHT möglich | Bohren, Schleifen = Zerstörung |
| Kantenfestigkeit | Kritisch — Kantendefekte lösen Spontanbruch aus | Schleifen VOR Härtung |
| Nickel-Sulfid-Einschlüsse | Spontanbruch-Risiko 1:10.000 | Heat-Soak-Test (HST) reduziert auf 1:100.000 |

> ⚠️ **ZU PRÜFEN (Audit):** 1:10.000 (ohne HST) bzw. 1:100.000 (mit HST) widerspricht den Anhängen. In "Alterungsmechanismus 3", Fehlerbild FB-WS-08 und der Bewertungsmatrix steht durchgängig: ohne HST 1:500, mit HST 1:10.000. Publizierte NiS-Spontanbruchhäufigkeiten streuen stark; keine Richtung ist zweifelsfrei belegbar. Diese Rate daher als `estimated — unverifiziert` behandeln, nicht als `measured`, bis vereinheitlicht.

**Vorteile für Windschutzscheiben:**
- Hohe Festigkeit bei geringer Dicke
- Kostengünstig (30–50% günstiger als VSG gleicher Dicke)
- Gute Temperaturbeständigkeit (wichtig bei beheizten Scheiben)
- Kratzfester als Kunststoffscheiben

**Nachteile für Windschutzscheiben:**
- **Totalausfall bei Bruch**: Scheibe zerfällt vollständig → sofortiger Sichtverlust
- **Kein Splitterschutz**: Glaswürfel fliegen durch den gesamten Steuerbereich
- **Spontanbruch-Risiko** durch Nickel-Sulfid-Einschlüsse (NiS): Ohne Heat-Soak-Test (HST nach EN 14179) besteht ein statistisches Risiko, dass die Scheibe ohne äußere Einwirkung bricht
- **Nicht reparabel**: Jeder Riss/Chip ist ein Komplettausfall

**AYDI-Empfehlung:** ESG nur für Boote ≤10 m in CE Kat. C/D akzeptabel. Ab 12 m und/oder CE Kat. A/B → VSG empfohlen.

> Confidence: `measured` (EN 12150-1, ISO 12216:2020)

#### 7.2.2 Verbundsicherheitsglas (VSG / Laminated Safety Glass)

**Herstellung:** Zwei oder mehr Glasscheiben werden mit einer Zwischenschicht (typisch PVB = Polyvinylbutyral, EVA = Ethylenvinylacetat, oder SGP = SentryGlas Plus) unter Hitze und Druck im Autoklav verbunden.

**Aufbau einer typischen Yacht-Windschutzscheibe VSG:**

```
Außenseite (See-Seite)
  ├── Äußere Glasscheibe (ESG oder Float, 5–10 mm)
  ├── PVB-Folie (0.76–1.52 mm)
  └── Innere Glasscheibe (ESG oder Float, 5–10 mm)
Innenseite (Helm-Seite)
```

**Zwischenschicht-Typen:**

| Typ | Material | Dicke (mm) | Eigenschaften | Preis-Aufschlag |
|-----|---------|-----------|--------------|-----------------|
| **Standard-PVB** | Polyvinylbutyral (Saflex/Trosifol) | 0.38/0.76/1.14/1.52 | UV-Schutz 99%, Splitterbindung | Basis |
| **Acoustic PVB** | PVB mit Schalldämmkern (Saflex Acoustic, Trosifol SC) | 0.76/1.52 | Schalldämmung +3–5 dB | +20–40% |
| **EVA** | Ethylenvinylacetat | 0.38/0.76 | Keine Autoklav-Prozess nötig, einfacher | -10% |
| **SGP** (SentryGlas Plus) | Ionoplast-Polymer (Kuraray) | 0.89/1.52/2.28 | 5× steifer als PVB, 100× reißfester | +60–100% |
| **Brandschutz-Interlayer** | Intumeszent (Pilkington Pyrostop) | 1.5–15.0 | Schäumt bei Feuer auf, Isolation | +200–400% |

**Vorteile für Windschutzscheiben (AYDI-Referenz):**
- **Splitterbindung**: Bei Bruch bleibt die Scheibe im Rahmen, Splitter haften an der Folie
- **Resttragfähigkeit**: Gebrochene VSG-Scheibe hält noch zusammen — Notbetrieb möglich
- **UV-Schutz**: PVB blockiert 99% der UV-Strahlung (schützt Interieur und Besatzung)
- **Schalldämmung**: Bessere Akustik als ESG (besonders mit Acoustic PVB: bis 5 dB Verbesserung)
- **Anpassbar**: Tönungsfolien, Heizdrähte, Beschichtungen können in die Zwischenschicht integriert werden
- **SOLAS-Fähig**: Brandschutzglas nur als VSG möglich

**Nachteile:**
- Teurer als ESG (50–100% Aufpreis)
- Schwerer (zwei Scheiben + Folie)
- PVB-Alterung: Vergilbung nach 10–20 Jahren (abhängig von UV-Belastung)
- PVB-Delaminierung an den Kanten bei mangelhafter Kantenversiegelung + Feuchtigkeit
- Reparatur: Kein Austausch der Zwischenschicht — Scheibe komplett tauschen

**AYDI-Empfehlung:** VSG ist der **Goldstandard** für Yacht-Windschutzscheiben ab 10 m Bootslänge. Bei Superyachten (>24 m) ist VSG obligatorisch (Klasse + SOLAS). Bei CE Kat. A/B: VSG mit SGP-Zwischenschicht empfohlen (höhere Resttragfähigkeit).

> Confidence: `measured` (EN 14449, ISO 12543-1/2/3/4/5/6, Hersteller-TDS Saflex/Trosifol/Kuraray)

#### 7.2.3 Floatglas (Ungehärtet)

**NICHT ZULÄSSIG für Windschutzscheiben** nach ISO 12216 und RCD 2013/53/EU. Floatglas bricht in große, messerscharfe Splitter — tödliche Verletzungsgefahr bei Bruch.

Ausnahme: Floatglas als Bestandteil von VSG (innere oder äußere Scheibe kann Float sein, die PVB-Folie hält die Splitter zurück). Bei hoher Belastung (CE Kat. A/B, Gleiter) sollten beide Scheiben ESG sein (ESG+PVB+ESG = sicherste Konfiguration).

#### 7.2.4 Acrylglas (PMMA)

**Anwendung:** Ältere Sportboote, Center Consoles, Schiebe-Windschutzscheiben, Klapp-Windschutzscheiben.

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 1.19 g/cm³ | ~50% von Glas |
| Biegefestigkeit | 70–80 MPa | Gut, aber unter ESG |
| E-Modul | 2.7–3.2 GPa | Deutlich weicher als Glas (70 GPa) |
| Lichtdurchlässigkeit | 92% (klar) | Besser als Glas (89%) |
| Kratzfestigkeit | Gering | Politur möglich, aber empfindlich |
| UV-Beständigkeit | Gut (30+ Jahre outdoor) | Bessere UV-Beständigkeit als PC |
| Temperaturbeständigkeit | Max. 80°C Dauertemperatur | VORSICHT: Windschutzscheiben können >80°C erreichen! |
| Chemische Beständigkeit | Empfindlich gegen Lösemittel | Kein Aceton, kein Alkohol auf PMMA! |
| Preis (klar, 10 mm) | 80–150 EUR/m² | Günstiger als VSG |
| Bruchverhalten | Splitter (nicht würfelig wie ESG) | Weniger gefährlich als Float, aber nicht sicher |

**AYDI-Empfehlung:** PMMA nur für Klapp-Windschutzscheiben auf Center Consoles akzeptabel (CE Kat. C/D, V ≤25 kn). Für geschlossene Steuerhäuser → VSG bevorzugen.

**Hersteller PMMA-Scheiben:**

| Hersteller | Produkt | Typ | Bemerkung |
|-----------|---------|-----|-----------|
| **Euracryl** | Marine-Acryl | Gegossenes PMMA | Spezialist für gebogene marine PMMA-Scheiben |
| **Röhm/Evonik** | Plexiglas GS / Plexiglas XT | Gegossen / Extrudiert | GS = höhere Qualität, XT = günstiger |
| **Lucite/Mitsubishi** | Perspex | Gegossenes PMMA | UK-Marke, gleichwertig |

#### 7.2.5 Polycarbonat (PC / Lexan / Makrolon)

**Anwendung:** Racing-Boote, militärische Boote, Arbeitsboote, Notfall-Ersatzscheiben.

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 1.20 g/cm³ | ~50% von Glas |
| Schlagfestigkeit | 250× Glas, 30× PMMA | Nahezu unzerbrechlich |
| Biegefestigkeit | 60–70 MPa | Etwas unter PMMA |
| Lichtdurchlässigkeit | 88% (klar) | Leicht unter PMMA |
| Kratzfestigkeit | Sehr gering ohne Beschichtung | Hard-Coat nötig (z.B. MR10E von Makrolon) |
| UV-Beständigkeit | Schlecht ohne Beschichtung | Vergilbt nach 2–5 Jahren ohne UV-Schutz |
| Temperaturbeständigkeit | Max. 130°C | Besser als PMMA |
| Preis (klar, 10 mm, hard-coated) | 150–300 EUR/m² | Teurer als PMMA |

**AYDI-Empfehlung:** PC als Notfall-Ersatzscheibe an Bord (3–5 mm, zugeschnitten) für Langfahrt. Als dauerhafte Windschutzscheibe nur mit Hartbeschichtung beidseitig und UV-Schutz.

> Confidence: `measured` (Materialdatenblätter Evonik/Covestro, ISO 12216)

### 7.3 Structural Bonding — Verklebungstechnik im Detail

#### 7.3.1 Prinzip

Structural Glazing (auch: Direct Glazing) bedeutet, dass die Scheibe ausschließlich durch einen elastischen Klebstoff im Rahmen oder direkt auf der Aufbaustruktur gehalten wird — ohne mechanische Befestigung (Schrauben, Klemmen, Gummiprofil).

**Vorteile:**
- Rahmenlose oder schmale Rahmen → modernes Design
- Gleichmäßige Lastverteilung auf die gesamte Klebfläche
- Keine Spannungskonzentration an Schraubpunkten
- Vibrationsdämpfung (elastischer Klebstoff absorbiert Motorvibrationen)
- Wasserdicht ohne zusätzliche Dichtung

**Risiken:**
- Klebstoff ist die EINZIGE Verbindung → Versagen = Scheibenverlust
- UV-Degradation der Klebfuge bei exponierten Kanten
- Temperaturempfindlichkeit (Klebstoff-Festigkeit sinkt bei hoher Temperatur)
- Falsche Primer-Auswahl = adhäsives Versagen (häufigster Fehler!)
- Kontamination der Klebfläche = Versagen (Fett, Feuchtigkeit, Staub)

#### 7.3.2 Klebfugenberechnung

Die erforderliche Klebflächenbreite berechnet sich nach ISO 21005:

```
w_bond = P_design × A_panel / (2 × (L_h + L_v) × σ_allow_adhesive × SF)

wobei:
  w_bond            = Klebflächenbreite in mm
  P_design          = Bemessungsdruck in kPa (aus ISO 12216)
  A_panel           = Scheibenfläche in m²
  L_h               = Horizontale Klebfugenlänge in m
  L_v               = Vertikale Klebfugenlänge in m
  σ_allow_adhesive  = Zul. Scherfestigkeit des Klebstoffs in kPa (nach Alterung!)
  SF                = Sicherheitsfaktor (ISO 21005: SF ≥ 6)
```

**Beispielrechnung:** Frontscheibe 1200 mm × 800 mm (0.96 m²), P_design = 7.2 kPa, Sikaflex-295 UV (σ = 2000 kPa):

```
w_bond = 7200 × 0.96 / (2 × (1.2 + 0.8) × 2000000 × 6)
w_bond = 6912 / (48000000)
w_bond ≈ 0.000144 m ≈ 0.14 mm → Rechnerisch minimal!
```

**Aber:** ISO 21005 schreibt ein **Minimum von 15 mm** vor (unabhängig von der Berechnung). In der Praxis werden **20–40 mm** verwendet, da:
- Fertigungstoleranzen ausgeglichen werden
- Kriechverformung über die Lebensdauer berücksichtigt wird
- Windlasten (dynamisch) zusätzlich zum Wasserdruck wirken
- Sicherheitsreserve für Alterung der Klebfuge

#### 7.3.3 Verarbeitungshinweise Structural Glazing

**Vorbereitung (kritischste Phase):**

1. **Reinigung Rahmen:**
   - Schleifen mit K120–K180 (Aluminium) oder K80–K120 (Edelstahl)
   - Reinigen mit Sika Reiniger-205 (Lösemittel, fettlösend)
   - Trocknen lassen (min. 10 min)
   - Primer auftragen (dünn, gleichmäßig, keine Pfützen)
   - Primer-Ablüftzeit einhalten (Sika-206 G+P: 30 min bei 23°C, 50% rH)

2. **Reinigung Glasscheibe:**
   - Klebfläche mit Sika Reiniger-205 reinigen (Handschuh-Pflicht!)
   - Primer Sika-206 G+P auftragen
   - Ablüftzeit: 30 min

3. **Klebstoff-Auftrag:**
   - Raupendurchmesser: ca. 1.5× Fugenbreite (Kompression beim Einsetzen)
   - Dreiecksraupe oder Rundraupe — KEINE Punkte (Lufteinschlüsse!)
   - Verarbeitungszeit Sikaflex-295 UV: ca. 30 min bei 23°C
   - Scheibe einsetzen und gleichmäßig andrücken
   - Fixierung mit Klebeband oder Saugnäpfen während Aushärtung (min. 24h)

4. **Aushärtung:**
   - Sikaflex-295 UV: Durchhärtung ca. 3 mm/24h bei 23°C, 50% rH
   - Bei 20 mm Fugenbreite: volle Festigkeit nach ca. 7 Tagen
   - Kein Boot-Einsatz vor vollständiger Durchhärtung!
   - Temperatur während Aushärtung: min. 10°C, max. 35°C

**Häufigste Fehler bei Structural Glazing (AYDI-Bewertungskriterien):**

| Fehler | Auswirkung | Erkennung |
|--------|-----------|-----------|
| Falscher/fehlender Primer | Adhäsionsversagen (Klebstoff löst sich vom Substrat) | Scheibe lässt sich von Hand anheben |
| Kontamination der Klebfläche | Lokales Versagen der Klebfuge | Blasen, Ablösung an Stellen |
| Zu geringe Klebflächenbreite | Strukturversagen unter Last | Scheibe bewegt sich bei Fingerdruck am Rand |
| Zu dünne Klebfuge | Keine Elastizität, Risse bei Temperaturwechsel | Risse in der Klebfuge sichtbar |
| Lufteinschlüsse in Klebfuge | Schwachstellen, Wassereinbruch | Blasen sichtbar durch Scheibe |
| Unvollständige Aushärtung | Plastische Verformung, Versagen | Klebstoff weich, verformbar |
| UV-Exposition der Klebfuge | Degradation, Versprödung | Verfärbung, Kreidung, Risse |

> Confidence: `measured` (Sika TDS/ADS, ISO 21005:2018, Werft-Verarbeitungsrichtlinien)

### 7.4 Beheizte Windschutzscheiben

#### 7.4.1 Heizdraht-Technologie

**Prinzip:** Dünne Metalldrähte (Wolfram, Nichrom, oder versilberter Kupferdraht, Ø 0.02–0.05 mm) werden in die PVB-Zwischenschicht eines VSG eingebettet. Die Drähte bilden ein Gitter mit ca. 15–25 mm Drahtabstand. Elektrischer Strom (12V, 24V oder 230V) erwärmt die Drähte durch Widerstandsheizung.

**Technische Daten:**

| Parameter | Wert | Bemerkung |
|-----------|------|-----------|
| Drahtdurchmesser | 0.02–0.05 mm | Nahezu unsichtbar bei <0.03 mm |
| Drahtabstand | 15–25 mm | Engerer Abstand = gleichmäßigere Heizung |
| Heizleistung | 150–400 W/m² | 150 = leichter Anti-Beschlag, 400 = Eisfreihaltung |
| Aufheizzeit (0°C → 20°C Oberfläche) | 3–8 min bei 300 W/m² | Abhängig von Außentemperatur |
| Stromaufnahme (24V, 1 m² bei 300 W/m²) | 12.5 A | Erhebliche Belastung der Bordelektrik |
| Gleichmäßigkeit | ±3°C über die Fläche | Bei guter Drahtverteilung |
| Lebensdauer | 15–25 Jahre | Drahtbruch nach Spannungsrissen im Glas |
| Sichtbarkeit | Bei direkter Sicht sichtbar, bei Polarisationsbrille deutlich | Ästhetischer Nachteil bei dicken Drähten |

**Hersteller beheizter Windschutzscheiben:**

| Hersteller | Produkt-Serie | Spannung | Leistung (W/m²) | Preis (EUR/m², Aufpreis) |
|-----------|--------------|---------|-----------------|--------------------------|
| **Trend Marine** | TM ClearView Heated | 12/24/230V | 200–400 | 400–800 |
| **Speich** | S.400 / S.500 Heated | 12/24V | 150–300 | 300–600 |
| **Hempel** | Marine Heated Glass | 24/110/230V | 200–400 | 500–1.000 |
| **Bohamet** | Heated Series | 12/24V | 150–350 | 250–500 |
| **Nautiglass** | NautiHeat | 24V | 200–300 | 300–500 |

#### 7.4.2 ITO-Beschichtung (Indium-Zinn-Oxid)

**Prinzip:** Transparente, elektrisch leitfähige Metalloxid-Beschichtung (In₂O₃:SnO₂) wird auf die Glasoberfläche per Magnetron-Sputtering aufgebracht. Gleichmäßige Flächenheizung ohne sichtbare Drähte.

| Parameter | Wert | Bemerkung |
|-----------|------|-----------|
| Beschichtungsdicke | 100–300 nm | Unsichtbar |
| Flächenwiderstand | 5–20 Ω/□ | Einstellbar durch Schichtdicke |
| Heizleistung | 100–300 W/m² | Geringer als Heizdraht |
| Lichtdurchlässigkeit | -5–10% vs. unbeschichtetes Glas | Leicht reduziert |
| Gleichmäßigkeit | ±1°C | Deutlich besser als Heizdraht |
| Sichtbarkeit | Keine Drähte sichtbar | Premium-Optik |
| Kosten (Aufpreis) | 600–1.200 EUR/m² | 2–3× teurer als Heizdraht |
| Haltbarkeit | Beschichtung auf Position 3 (VSG-Innenseite) | Geschützt vor mechanischer Beschädigung |

**ITO-Positionen in der Scheibe:**

```
Außenseite
  ├── Äußere Glasscheibe (Pos. 1 = außen, Pos. 2 = innen)
  ├── PVB-Folie
  └── Innere Glasscheibe (Pos. 3 = außen/ITO-Seite, Pos. 4 = Raumseite)
Innenseite
```

ITO auf Position 3 ist geschützt und beheizt primär die PVB-Folie, was die thermische Spannung im Glas minimiert.

> Confidence: `measured` (Hersteller-TDS Trend Marine, Speich, Pilkington)

#### 7.4.3 Warmluft-Entbeschlagung (Defogger / Demister)

**Prinzip:** Warme, trockene Luft wird über Schlitzdüsen an der Scheibenunterkante auf die Innenseite der Windschutzscheibe geblasen. Verhindert Beschlag (Kondensation) und unterstützt die Scheibenheizung.

**System-Dimensionierung:**

| Parameter | Empfehlung | Quelle |
|-----------|-----------|--------|
| Luftvolumenstrom | 50–80 m³/h pro m Scheibenbreite | Erfahrungswert, Webasto-Richtlinie |
| Austrittstemperatur | 40–60°C | Zu heiß → thermischer Schock, zu kalt → unwirksam |
| Austrittsgeschwindigkeit | 3–6 m/s | Geringer als Kfz (Geräusch!) |
| Düsenbreite | 10–15 mm Schlitzweite | Über gesamte Scheibenbreite |
| Abstand Düse → Scheibe | 30–60 mm | Optimal für Strömungsanlage |

**Typische Systeme:**

| Hersteller | Produkt | Leistung | Typ | Preis (EUR) |
|-----------|---------|---------|-----|------------|
| **Webasto** | BlueCool D Defrost | 2–5 kW | Warmluft aus Klimaanlage | 800–2.500 |
| **Eberspächer** | Airtronic D4/D5 | 4–5 kW | Diesel-Luftheizung mit Defrostkanal | 1.200–2.000 |
| **Vetus** | DEHW024A | 2.4 kW | Elektrischer Heizlüfter (24V) | 350–600 |
| **Dometic** | Tempered Air | 1.5–3 kW | AC/Heiz-Kombisystem | 1.000–3.000 |

> Confidence: `documented` (Hersteller-Empfehlungen, Werft-Installationsrichtlinien)

### 7.5 Scheibenwischer-Systeme

#### 7.5.1 Pendelwischer (Swing Arm / Pendulum Wiper)

**Funktionsprinzip:** Ein elektromotorisch angetriebener Arm pendelt in einem Winkel von 60°–120° über die Scheibe. Einfachste und verbreitetste Bauform für Yachten bis 15 m.

**Komponenten:**
1. **Motor**: 12V oder 24V DC, 30–80 W, Schneckengetriebe
2. **Antriebswelle**: Durchführung durch die Aufbauwand (wasserdichte Stopfbuchse)
3. **Wischerarm**: Edelstahl 316L oder schwarz beschichtetes Aluminium
4. **Wischerblatt**: Gummi oder Silikon, Flachbalken oder konventionell
5. **Steuerung**: 1–2 Geschwindigkeiten + Intervall

**Hersteller Pendelwischer:**

| Hersteller | Serie | Motor-Typ | Armlänge (mm) | Blattlänge (mm) | Preis (EUR) |
|-----------|-------|----------|--------------|-----------------|------------|
| **Exalto** | HD (Heavy Duty) | 12/24V, 60W | 305–610 | 400–700 | 350–800 |
| **Exalto** | 215 BD | 12/24V, 40W | 280–500 | 350–600 | 250–500 |
| **Speich** | S.100 | 12/24V, 40W | 250–450 | 300–500 | 200–450 |
| **Speich** | S.200 | 12/24V, 60W | 350–610 | 450–700 | 300–600 |
| **Roca** | W10/W12 | 12/24V, 30W | 250–400 | 300–500 | 150–350 |
| **Roca** | W25 | 12/24V, 60W | 305–610 | 400–700 | 250–550 |
| **Vetus** | RW Range | 12/24V, 40W | 280–508 | 350–600 | 200–500 |
| **Lewmar** | Standard | 12V, 30W | 250–400 | 300–500 | 180–400 |

**Ersatzblätter (häufig benötigtes Verschleißteil):**

| Blatt-Typ | Material | Standzeit (Monate) | Preis (EUR) | Kompatibilität |
|----------|---------|-------------------|------------|----------------|
| Standard Gummi | Naturkautschuk | 6–12 | 15–35 | Universal, 9×3 mm Profil |
| Silikon | Silikonelastomer | 12–24 | 25–55 | Universal, UV-beständiger |
| Flachbalken (Flat Beam) | Gummi + Federstahl | 12–18 | 30–60 | Herstellerspezifisch |

#### 7.5.2 Pantograph-Wischer

**Funktionsprinzip:** Parallelogramm-Mechanismus — der Wischerarm wird vertikal auf und ab geführt (nicht pendelnd). Das Wischerblatt wischt ein nahezu rechteckiges Feld ab. Ideal für große, breite Windschutzscheiben.

**Vorteile gegenüber Pendelwischer:**
- Nahezu rechteckiges Wischfeld → höhere Abdeckung (>90% vs. 70–80% beim Pendelwischer)
- Gleichmäßigerer Anpressdruck über die Blattlänge
- Ästhetisch unauffälliger (kein seitlicher Schwenkbereich nötig)
- Beidseitig einfahrbar (Parkposition am Scheibenrand)

**Nachteile:**
- 3–5× teurer als Pendelwischer
- Komplexere Mechanik (Verschleißteile: Parallelogrammgelenke)
- Größerer Einbauraum hinter der Scheibe
- Schwierigere Nachrüstung

**Hersteller Pantograph-Wischer:**

| Hersteller | Serie | Wischfeldbreite (mm) | Motor | Preis (EUR) |
|-----------|-------|---------------------|-------|------------|
| **Exalto** | 1700 Series | 500–1.500 | 24V, 80–120W | 1.500–4.000 |
| **Speich** | S.400 / S.500 | 600–1.800 | 12/24V, 60–100W | 1.200–3.500 |
| **Roca** | W38 Pantograph | 500–1.200 | 24V, 80W | 800–2.500 |
| **Doga** (FR) | PantoDoga | 600–1.500 | 24V, 100W | 1.000–3.000 |
| **Hepworth** (UK) | Clearview | 400–2.000 | 24/110/230V | 2.000–8.000 |

#### 7.5.3 Wischer-Dimensionierung

**Faustformel für Armlänge:**

```
Arm_length ≈ 0.6 × Scheibenhöhe (mm)
Blade_length ≈ Arm_length + 50–100 mm (Blatt überragt Arm leicht)
```

**Wischfeld-Abdeckung nach ISO 3903:**

| Position | Mindest-Abdeckung | Empfehlung |
|----------|------------------|-----------|
| Hauptsteuerstand, direkt vor Rudergänger | ≥80% der Scheibe | ≥90% |
| Neben-Steuerstand (Flybridge) | ≥70% | ≥80% |
| Seitliche Scheiben | Nicht vorgeschrieben | Empfohlen bei Regenwetter-Revieren |

> Confidence: `estimated — unverifiziert` (Hersteller-Kataloge; ISO-3903-Bezug fehlerhaft — reale ISO 3903 = rechteckige Schiffsfenster, nicht Scheibenwischer; siehe Audit-Hinweis in §1.6)

### 7.6 Öffnende und Schiebende Windschutzscheiben

#### 7.6.1 Horizontal-Schiebescheiben (Sliding Windshields)

**Anwendung:** Belüftung des Steuerhauses, Kommunikation mit Vorschiff-Crew, Zugang zum Vordeck.

**Konstruktionstypen:**

| Typ | Beschreibung | Vorteile | Nachteile |
|-----|-------------|---------|----------|
| **Einzel-Schiebescheibe** | Eine Scheibe gleitet horizontal hinter die andere | Einfach, bewährt | Nur 50% Öffnung |
| **Doppel-Schiebescheibe** | Zwei Scheiben gleiten gegeneinander | 50–66% Öffnung | Mittelpfosten nötig |
| **Taschenschieber** | Scheibe gleitet in eine Tasche in der Aufbauwand | 100% Öffnung | Aufwändig, teuer |
| **Elektrisch** | Motorisch angetriebenes Gleiten | Komfort | Kosten, Ausfallrisiko |

**Führungsschienen:**
- Material: Eloxiertes Aluminium oder Edelstahl 316L
- Profil: U-Profil mit UHMW-PE- oder Teflon-Gleitleisten
- Dichtung: Bürstendichtung (Schleifdichtung) + Lippendichtung am Rand
- Drainage: Entwässerungsöffnungen in der unteren Schiene obligatorisch

**Hersteller Schiebe-Windschutzscheiben:**

| Hersteller | Serie | Typ | Preis-Range (EUR) |
|-----------|-------|-----|------------------|
| **Trend Marine** | ClearView Sliding | Horizontal, manuell/elektrisch | 2.000–8.000 |
| **Besenzoni** | P-Series Sliding | Elektrisch, Superyacht | 4.000–15.000 |
| **Webasto** | SunSlider Marine | Elektrisch, aus Automotive | 1.500–5.000 |
| **Taylor Made** | Sliding Windshield | Manuell, Standardware | 800–2.500 |

#### 7.6.2 Klapp-Windschutzscheiben (Folding Windshields)

**Anwendung:** Center Consoles, Walkarounds, Sportfischer. Die gesamte Windschutzscheibe klappt nach vorne oder hinten.

**Konstruktion:**
- Scharnier am unteren Rand (Klappen nach vorne) oder am oberen Rand (Klappen nach hinten)
- Material: PMMA oder PC (leichter als Glas, da gesamte Scheibe bewegt wird)
- Gasdruckfedern oder Verriegelungen halten die Scheibe in aufrechter Position
- Dichtung: EPDM-Kompressionsdichtung am Rahmen

**AYDI-Hinweis:** Klapp-Windschutzscheiben sind NICHT für CE Kat. A/B geeignet (Wassereinbruchsrisiko bei versehentlichem Öffnen). Nur Kat. C/D.

#### 7.6.3 Kipp-Windschutzscheiben (Tilting Windows)

**Anwendung:** Belüftungsöffnung am oberen Rand der Windschutzscheibe. Die Scheibe kippt oben nach innen oder außen.

- Kipp nach außen: Regenabweisend, aber Spritzwassergefahr
- Kipp nach innen: Besser bei Regen, aber reduziert Kopffreiheit

**Typische Öffnungsmaße:**
- Kippwinkel: 15–30°
- Öffnungsspalt: 80–200 mm
- Gasdruckfeder für kontrollierten Öffnungsvorgang

### 7.7 Entbeschlagung und Demisting — Systemvergleich

| Methode | Wirksamkeit | Energiebedarf | Kosten (EUR) | Empfohlen für |
|---------|------------|--------------|-------------|---------------|
| Beheizte Scheibe (Heizdraht) | Sehr hoch | 150–400 W/m² | 300–800/Scheibe | Kat. A/B, Ganzjahr |
| Beheizte Scheibe (ITO) | Sehr hoch | 100–300 W/m² | 600–1.200/Scheibe | Premium, Superyacht |
| Warmluft-Defogger | Hoch | 1.500–5.000 W gesamt | 350–2.500 | Alle Bootstypen |
| Klimaanlage (Trockene Luft) | Mittel | Teil der AC-Leistung | In AC integriert | Tropen, Mittelmeer |
| Anti-Beschlag-Folie (innen) | Gering | 0 W | 20–50/Scheibe | Nachrüstung, Budget |
| Chemisches Anti-Fog-Spray | Gering | 0 W | 10–20/Dose | Kurzfristige Lösung |
| Doppelverglasung | Hoch (verhindert Beschlag) | 0 W | +200–500/Scheibe | Langfristig beste Lösung |
| Lüftungsklappe in Scheibe | Mittel | 0 W | 100–300 | Segelyachten, Trawler |

**AYDI-Empfehlung nach Bootsklasse:**

| Bootsklasse | Empfehlung | Bemerkung |
|-------------|-----------|-----------|
| Sportboot ≤10 m, Kat. C/D | Warmluft-Defogger | Günstig, ausreichend |
| Motoryacht 10–15 m, Kat. B/C | Beheizte Scheibe + Defogger | Standard für Nordeuropa |
| Motoryacht 15–24 m, Kat. A/B | Doppelverglasung + Heizdraht + Defogger | Maximale Zuverlässigkeit |
| Superyacht >24 m | Doppelverglasung + ITO + Klimaanlage-Defrost | Luxusstandard |
| Segelyacht Pilothouse | Defogger + optional Heizdraht | Energiebudget begrenzt |

> Confidence: `documented` (Hersteller-Vergleich, Werftpraxis, Surveyor-Erfahrung)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Trend Marine Products Ltd. (UK) — Marktführer

**Standort:** Romsey, Hampshire, UK
**Gegründet:** 1982
**Website:** www.trendmarine.com
**Spezialisierung:** Custom-Windschutzscheiben und -Fenster für Yachten, Superyachten und kommerzielle Schiffe

**Produktportfolio:**

| Produktlinie | Beschreibung | Typische Bootslänge | Preis-Range (EUR/Scheibe) |
|-------------|-------------|--------------------|-----------------------------|
| **TM ClearView** | Standard-Windschutzscheiben, flach und gebogen | 8–20 m | 800–5.000 |
| **TM ClearView Heated** | Beheizte Windschutzscheiben (Heizdraht/ITO) | 10–24 m | 1.500–8.000 |
| **TM Panorama** | Große Panorama-Frontscheiben, compound-curved | 15–40 m | 3.000–25.000 |
| **TM Sliding** | Schiebe-Windschutzscheiben, manuell/elektrisch | 10–30 m | 2.000–12.000 |
| **TM Superyacht** | Custom-Verglasungen für Superyachten >24 m | 24–100+ m | 5.000–80.000 |
| **TM Fire-Rated** | SOLAS-konforme Brandschutzscheiben | 24+ m (gewerblich) | 8.000–40.000 |

**Stärken:**
- Eigene Glasbiegerei (single-curved + compound-curved bis 4 m × 2.5 m)
- Integrierte Heizsysteme (Heizdraht + ITO)
- SOLAS-Zertifizierung (Lloyd's, DNV, BV, RINA zugelassen)
- Eigene Wischer-Integration (Kooperation mit Exalto/Speich)
- OEM-Lieferant für Princess, Sunseeker, Fairline, Oyster, Discovery

**Referenz-OEM-Partnerschaften:**

| Werft | Bootstyp | Trend Marine Produkt |
|-------|---------|---------------------|
| **Sunseeker** | Manhattan/Predator Range | TM ClearView gebogen, beheizt |
| **Princess Yachts** | V-Class, F-Class, Y-Class | TM Panorama, beheizt |
| **Fairline** | Targa/Squadron | TM ClearView |
| **Oyster Yachts** | 565/675/745/885 | TM Pilothouse-Verglasung |
| **Discovery Yachts** | 57/58 | TM ClearView Heated |
| **Nordhavn** | 41/43/47/56/60 (Trawler) | TM ClearView Heated |

**Lieferzeit:** 6–12 Wochen (Standard), 12–16 Wochen (Compound-Curved/SOLAS)

> Confidence: `documented` (Trend Marine Katalog 2025, Werft-Referenzen)

### 8.2 Speich S.r.l. (Italien)

**Standort:** Brescia, Lombardei, Italien
**Gegründet:** 1957
**Website:** www.speich-italy.com
**Spezialisierung:** Scheibenwischer-Systeme und beheizte Fenster/Windschutzscheiben

**Produktportfolio — Wischer:**

| Serie | Typ | Motor | Armlänge (mm) | Preis (EUR) |
|-------|-----|-------|--------------|------------|
| **S.100** | Pendelwischer, Economy | 12V, 30W | 250–450 | 180–350 |
| **S.200** | Pendelwischer, Standard | 12/24V, 50W | 305–610 | 280–550 |
| **S.300** | Pendelwischer, Heavy Duty | 24V, 80W | 400–700 | 400–800 |
| **S.400** | Pantograph, Standard | 24V, 80W | 400–1.200 | 1.000–2.500 |
| **S.500** | Pantograph, Heavy Duty | 24/110V, 120W | 600–1.800 | 2.000–5.000 |
| **S.SWF** | Beheizte Arme | 24V | 305–610 | +200–400 Aufpreis |

**Produktportfolio — Beheizte Scheiben:**

| Produkt | Beschreibung | Spannung | Leistung |
|---------|-------------|---------|---------|
| **Speich Heated Glass** | Heizdraht in VSG | 12/24V | 150–350 W/m² |
| **Speich Heated + Wiper** | Komplettsystem Scheibe + Wischer | 24V | 200–300 W/m² |

**Stärken:**
- Integrierte Wischer-Scheiben-Systeme (alles aus einer Hand)
- 65+ Jahre Erfahrung im Marine-Segment
- Breites Händlernetz in Europa
- OEM für viele italienische Werften (Ferretti, Azimut, Cranchi, Sessa)

**Schwächen:**
- Begrenzte Compound-Curve-Fähigkeit
- Weniger Erfahrung im Superyacht-Segment (>30 m) als Trend Marine
- Dokumentation manchmal nur auf Italienisch

**Lieferzeit:** 4–8 Wochen (Standard), 8–12 Wochen (Custom)

### 8.3 Bohamet Sp. z o.o. (Polen)

**Standort:** Gdynia, Pommern, Polen
**Gegründet:** 1990
**Website:** www.bohamet.com
**Spezialisierung:** Gebogenes gehärtetes und laminiertes Glas für Yachten und kommerzielle Schiffe

**Produktportfolio:**

| Produkt | Glastyp | Min. Radius (mm) | Max. Größe (mm) | Preis-Range (EUR/m²) |
|---------|---------|-----------------|----------------|----------------------|
| **Bohamet ESG Curved** | Einscheibensicherheitsglas, gebogen | 400 | 3.200 × 2.000 | 250–600 |
| **Bohamet VSG Curved** | Verbundsicherheitsglas, gebogen | 600 | 2.800 × 1.800 | 400–1.000 |
| **Bohamet VSG Heated** | VSG gebogen mit Heizdraht | 600 | 2.500 × 1.500 | 600–1.500 |
| **Bohamet Flat ESG/VSG** | Flach, ESG oder VSG | — | 3.600 × 2.400 | 150–500 |
| **Bohamet IGU** | Isolierglas (Doppelverglasung) | 800 | 2.200 × 1.400 | 500–1.200 |

**Stärken:**
- Hervorragendes Preis-Leistungs-Verhältnis (30–40% günstiger als UK-Hersteller)
- Moderne Produktionsanlage (Glaston-Biegeofen, neueste Generation)
- CE-zertifiziert, EN 12150 (ESG), EN 14449 (VSG)
- Flexibel bei Kleinstückzahlen (ab 1 Stück Sonderanfertigung)
- Export in >30 Länder, starke Präsenz auf METS Amsterdam

**Schwächen:**
- Kein SOLAS-zertifiziertes Brandschutzglas
- Weniger Erfahrung mit Compound-Curves als Trend Marine
- Wischer-Systeme werden nicht angeboten (nur Scheiben)

**OEM-Referenzen:** Galeon (PL), Delphia (PL), Sunreef (PL), diverse skandinavische Werften

**Lieferzeit:** 4–8 Wochen (Standard), 6–14 Wochen (Compound-Curved)

### 8.4 Nautiglass B.V. (Niederlande)

**Standort:** Urk, Flevoland, Niederlande
**Gegründet:** 1995
**Website:** www.nautiglass.nl
**Spezialisierung:** Yacht-Windschutzscheiben und marine Verglasung, Fokus auf holländische und skandinavische Werften

**Produktportfolio:**

| Produkt | Beschreibung | Preis-Range (EUR/m²) |
|---------|-------------|----------------------|
| **NautiClear** | Flache ESG/VSG-Windschutzscheiben | 200–500 |
| **NautiCurve** | Gebogene Windschutzscheiben (single-curved) | 350–800 |
| **NautiHeat** | Beheizte Windschutzscheiben (Heizdraht, 24V) | 500–1.000 |
| **NautiSafe** | VSG mit SGP-Zwischenschicht (hochfest) | 600–1.200 |
| **NautiDuo** | Doppelverglasung (Isolierglas) | 500–1.000 |

**OEM-Referenzen:** Linssen (NL), Aquanaut (NL), Super Lauwersmeer (NL), Jetten (NL), verschiedene skandinavische Werften

**Lieferzeit:** 4–8 Wochen

### 8.5 Hempel Glas GmbH (Deutschland)

**Standort:** Lübeck, Schleswig-Holstein, Deutschland
**Gegründet:** 1946
**Website:** www.hempel-glas.de
**Spezialisierung:** Superyacht-Verglasungen, Brandschutzglas, marine Spezialverglasungen

**Produktportfolio:**

| Produkt | Beschreibung | Zertifizierung | Preis-Range (EUR/m²) |
|---------|-------------|---------------|----------------------|
| **Hempel Marine VSG** | Standard VSG für Yachten | ISO 12216 | 400–800 |
| **Hempel Marine Heated** | Beheizte Superyacht-Scheiben | ISO 12216 + Klasse | 800–2.000 |
| **Hempel Pyro Marine** | SOLAS-Brandschutzglas A-0 bis A-60 | SOLAS, MED-Rad | 1.500–5.000 |
| **Hempel Marine IGU** | Doppelverglasung für Yachten | ISO 12216 | 600–1.500 |
| **Hempel Marine Acoustic** | Schallschutz-VSG mit Acoustic PVB | ISO 12216 | 600–1.200 |

**Stärken:**
- Eines der wenigen Unternehmen mit SOLAS-zertifiziertem Brandschutzglas für Yachten
- Eigene Glasbiegerei (bis 3.5 m × 2 m)
- MED-Rad-Zertifizierung (Marine Equipment Directive)
- Erfahrung mit deutschen Superyacht-Werften (Lürssen, Blohm+Voss, Nobiskrug, Abeking & Rasmussen)

**Lieferzeit:** 8–12 Wochen (Standard), 12–20 Wochen (SOLAS/Custom)

### 8.6 Euracryl SARL (Frankreich)

**Standort:** La Rochelle, Charente-Maritime, Frankreich
**Gegründet:** 1988
**Website:** www.euracryl.fr
**Spezialisierung:** Gebogenes Acrylglas (PMMA) für Yachten — Windschutzscheiben und Hardtops

**Produktportfolio:**

| Produkt | Material | Min. Radius (mm) | Max. Größe (mm) | Preis-Range (EUR/m²) |
|---------|---------|-----------------|----------------|----------------------|
| **Euracryl Marine Flat** | PMMA GS/XT | — | 3.000 × 2.000 | 100–250 |
| **Euracryl Marine Curved** | PMMA thermogeformt | 300 | 2.500 × 1.500 | 200–600 |
| **Euracryl Marine Tinted** | PMMA getönt (Grau/Bronze) | 300 | 2.500 × 1.500 | 250–700 |

**Stärken:**
- Spezialist für gebogenes Acrylglas im Marine-Segment
- Leicht (50% des Gewichts von Glas) — wichtig für Center Consoles und Sportboote
- OEM für Bénéteau, Jeanneau (sportliche Modelle)
- Thermoformung ermöglicht komplexere Formen als Glasbiegen

**Schwächen:**
- PMMA ist kratzempfindlicher als Glas
- Temperaturlimit 80°C — problematisch bei dunklen Rahmen in Tropen
- Nicht für CE Kat. A/B Hochleistungsboote empfohlen
- Keine Heizdraht-Integration möglich (Schmelzgefahr)

**Lieferzeit:** 4–8 Wochen

### 8.7 Exalto BV (Niederlande)

**Standort:** Almere, Flevoland, Niederlande
**Gegründet:** 1969
**Website:** www.exalto.nl
**Spezialisierung:** Premium-Scheibenwischer-Systeme für Yachten und kommerzielle Schiffe

**Produktportfolio — Wischer-Systeme:**

| Serie | Typ | Armlänge (mm) | Besonderheit | Preis (EUR) |
|-------|-----|--------------|-------------|------------|
| **215 BD** | Pendelwischer, Standard | 280–508 | Bewährt, preiswert | 250–500 |
| **215 BD+** | Pendelwischer, verdeckt | 280–508 | Arm verschwindet unter Unterkante | 350–650 |
| **HD** | Pendelwischer, Heavy Duty | 305–610 | Für raue Bedingungen | 400–800 |
| **1700** | Pantograph | 500–1.500 | Professionell, Superyacht | 1.500–4.000 |
| **1700 HD** | Pantograph, Heavy Duty | 600–1.800 | Offshore/Fischerei | 2.500–6.000 |

**Zubehör:**

| Produkt | Beschreibung | Preis (EUR) |
|---------|-------------|------------|
| **Exalto Washer Kit** | Scheibenwaschanlage (Tank + Pumpe + Düsen) | 150–350 |
| **Exalto Wiper Control** | Elektronische Steuerung (Intervall, 2 Geschw.) | 120–250 |
| **Exalto Heated Arm** | Beheizte Wischerarme (24V) | 200–400 Aufpreis |

**Stärken:**
- Holländische Ingenieursqualität
- OEM für viele europäische Werften
- Breites Ersatzteilprogramm (Blätter, Arme, Motoren einzeln lieferbar)
- Gutes Preis-Leistungs-Verhältnis

### 8.8 Roca Industry S.A. (Spanien)

**Standort:** Barcelona, Spanien (Marine-Division)
**Website:** www.rfroca.com
**Spezialisierung:** Scheibenwischer, marine Antriebssysteme

**Produktportfolio:**

| Serie | Typ | Motor | Preis (EUR) |
|-------|-----|-------|------------|
| **W10** | Pendelwischer, Compact | 12V, 25W | 120–280 |
| **W12** | Pendelwischer, Standard | 12V, 35W | 150–350 |
| **W25** | Pendelwischer, Heavy Duty | 12/24V, 60W | 250–550 |
| **W38** | Pantograph | 24V, 80W | 800–2.500 |

**Stärken:** Robuste, einfache Konstruktion, bewährt in Fischerei und Arbeitsbooten, günstiger als Exalto/Speich.

### 8.9 Vetus B.V. (Niederlande)

**Standort:** Schiedam, Südholland, Niederlande
**Website:** www.vetus.com
**Spezialisierung:** Umfassendes Sortiment an marine Hardware, darunter Scheibenwischer und Windschutzscheiben

**Wischer-Produktportfolio:**

| Serie | Typ | Armlänge (mm) | Motor | Preis (EUR) |
|-------|-----|--------------|-------|------------|
| **RW** | Pendelwischer, Standard | 280–508 | 12/24V, 40W | 200–450 |
| **RWAV** | Pendelwischer + Waschanlage | 280–508 | 12/24V, 40W | 300–600 |
| **DINSD** | Pendelwischer, Parallelmontage | 280–400 | 12V, 30W | 180–350 |

**Windschutzscheiben:**

| Produkt | Beschreibung | Preis (EUR) |
|---------|-------------|------------|
| **Vetus Flat Glass** | Flache ESG-Scheiben, Standardmaße | 200–600 |
| **Vetus Curved Glass** | Einfach gebogene ESG-Scheiben | 400–1.000 |

**Stärken:** Breites Sortiment, extrem gutes Händlernetz weltweit, Ersatzteile überall verfügbar. Schwäche: Keine Custom-Lösungen, kein Superyacht-Segment.

### 8.10 Lewmar Ltd. (UK)

**Standort:** Havant, Hampshire, UK
**Website:** www.lewmar.com
**Spezialisierung:** Luken, Bullaugen, Fenster, Beschläge — Windschutzscheiben sind ein Neben-Segment

Lewmar bietet Standard-Windschutzscheiben primär für Segelyacht-Pilothouse-Anwendungen und kleinere Motoryachten. Nicht vergleichbar mit Trend Marine im Custom-Segment.

### 8.11 Freeman Marine Equipment Inc. (USA)

**Standort:** Gold Beach, Oregon, USA
**Gegründet:** 1973
**Website:** www.freemanmarine.com
**Spezialisierung:** SOLAS-zertifizierte Windschutzscheiben, Türen und Luken für Superyachten, kommerzielle Schiffe und Marineschiffe

**Produktportfolio:**

| Produkt | Beschreibung | Zertifizierung | Preis-Range (EUR) |
|---------|-------------|---------------|-------------------|
| **FM Windshield** | Custom-Windschutzscheiben (flach/gebogen) | ABS, USCG, SOLAS | 3.000–30.000 |
| **FM Fire-Rated** | Brandschutzglas A-0 bis A-60 | SOLAS, USCG | 8.000–50.000 |
| **FM Ice-Class** | Windschutzscheiben für Eisfahrt | DNV ICE-1A | 5.000–40.000 |
| **FM Ballistic** | Ballistische Schutzscheiben | NIJ Level III | 10.000–80.000 |

**Stärken:**
- Höchste Zertifizierungsdichte (SOLAS, USCG, ABS, DNV, LR, BV)
- Einziger Hersteller mit ballistischen Schutzscheiben für Yachten (Sicherheitsyachten)
- Ice-Class-Erfahrung (Expeditionsyachten)
- Qualität: US Navy Contractor

**Schwächen:**
- Premium-Preissegment (2–3× europäische Hersteller)
- Lange Lieferzeiten (12–20 Wochen)
- Versand aus USA → Zoll, Logistik

### 8.12 Besenzoni S.p.A. (Italien)

**Standort:** Sarnico, Lombardei, Italien
**Gegründet:** 1967
**Website:** www.besenzoni.it
**Spezialisierung:** Premium-Yacht-Ausstattung: Gangways, Krane, Fenster, Schiebe-Systeme

**Windschutzscheiben-Segment:**

| Produkt | Beschreibung | Preis-Range (EUR) |
|---------|-------------|-------------------|
| **P.600 / P.700 Sliding** | Elektrische Schiebe-Windschutzscheiben | 4.000–15.000 |
| **P.800 Panorama** | Elektrische Panorama-Schiebescheiben (Superyacht) | 10.000–40.000 |
| **P.500 Tilting** | Elektrisch kippende Frontscheiben | 3.000–10.000 |

**Stärken:** Premium-Segment, OEM für Azimut, Ferretti, Riva. Elektrische Antriebe mit Soft-Close und Einklemmschutz.

> Confidence: `documented` (Hersteller-Kataloge 2024/2025, METS Amsterdam 2025, Boot Düsseldorf 2026)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Motoryacht — Hauptsteuerstand (Lower Helm)

**Typische Konfiguration (12–20 m Motoryacht):**

| Parameter | Typisch Verdränger (Trawler) | Typisch Gleiter (Sportboot) |
|-----------|-------------------------------|-------------------------------|
| Scheibenanzahl | 3–5 (Front) + 2–4 (Seite) | 1–3 (Front, Wrap-around) |
| Form | Flach oder leicht gebogen (V-Form) | Stark gebogen (Wrap-around) |
| Neigung (Rake) | 5–15° | 25–45° |
| Glastyp | VSG 10–14 mm | VSG 10–16 mm |
| Wischer | 2–3 Pendelwischer (S.200/Exalto 215) | 1–2 Pendelwischer (versteckt) |
| Heizung | Heizdraht + Defogger (Nordeuropa) | Defogger (meist ausreichend) |
| Öffnung | 1 Schiebescheibe (Center) | Selten (alles fest verklebt) |
| Preis Verglasungssystem (EUR) | 5.000–15.000 | 8.000–25.000 |

**Dimensionierungs-Faustregeln für Motoryacht-Windschutzscheiben:**

| Bootslänge (m) | Gesamtbreite Frontscheibe (mm) | Höhe (mm) | Empfohlene Dicke VSG (mm) |
|-----------------|-------------------------------|-----------|--------------------------|
| 8–10 | 2.000–2.800 | 500–700 | 8–10 (4+0.76+4) |
| 10–12 | 2.500–3.200 | 600–800 | 10–12 (5+0.76+5) |
| 12–15 | 3.000–4.000 | 700–1.000 | 12–14 (6+0.76+6) |
| 15–18 | 3.500–5.000 | 800–1.200 | 14–16 (6+1.52+6) |
| 18–24 | 4.000–6.000 | 900–1.400 | 16–19 (8+1.52+8) |

**Typische Probleme (AYDI-Bewertungskatalog):**

| Problem | Häufigkeit | Ursache | Maßnahme | Kosten (EUR) |
|---------|-----------|--------|---------|-------------|
| PVB-Delaminierung (Kante) | Häufig (>10 Jahre) | UV + Feuchtigkeit | Scheibentausch | 2.000–8.000 |
| Klebfugenversagen | Mittel | UV-Degradation, Temperaturschwankung | Neu verkleben | 500–2.000 |
| Wischer-Motorausfall | Häufig (>5 Jahre) | Salzkorrosion | Motor tauschen | 200–600 |
| Wischerblatt-Streaking | Sehr häufig (>1 Jahr) | Verschleiß | Blatt tauschen | 20–50 |
| Kondensation zwischen VSG-Scheiben | Selten | Herstellungsfehler / Kantendichtungsversagen | Scheibentausch | 2.000–8.000 |
| Kratzer (Wischerfeld) | Häufig (>3 Jahre) | Salzpartikel unter Wischerblatt | Polieren oder Tausch | 100 (Polieren), 2.000+ (Tausch) |
| Riss (Steinschlag/Thermospannung) | Selten | Mechanischer Schlag, Temperaturdifferenz | Scheibentausch | 2.000–8.000 |
| Heizdrahtausfall | Selten (>10 Jahre) | Drahtbruch | Scheibentausch | 3.000–10.000 |

### 9.2 Pilothouse-Segelyacht (Decksalon)

**Typische Konfiguration (40–60 ft Pilothouse-Segler):**

| Parameter | Typisch |
|-----------|---------|
| Scheibenanzahl | 3–7 (Front) + 4–8 (Seite) |
| Form | Flach (Tradition) oder leicht gebogen (modern) |
| Neigung (Rake) | 10–25° |
| Glastyp | VSG 8–12 mm (Kat. A/B), ESG 6–10 mm (Kat. C) |
| Wischer | 1–2 Pendelwischer (klein, 250–400 mm Arm) |
| Heizung | Defogger (Standard), Heizdraht (optional) |
| Öffnung | 1–2 Kipp-Fenster oben, ggf. 1 Schiebescheibe |
| Preis Verglasungssystem (EUR) | 4.000–12.000 |

**Besonderheiten Pilothouse-Segelyacht:**
- Scheibenfläche muss groß genug für Segelsicht nach vorne und seitlich (Vorsegel, Trimm)
- Blendung durch tiefstehende Sonne ist das Hauptproblem — getönte Scheiben oder Innenrollos
- Heeling (Krängung): Bei 25° Krängung verändert sich der Blickwinkel durch die Scheibe erheblich → Wrap-around-Verglasung bevorzugt
- Energiebudget begrenzt (Segelyacht) → Scheibenheizung nur bei ausreichender Batterie-/Generator-Kapazität
- Gewicht: Oberer Teil des Bootes → CG-relevant. VSG statt Dreifach-Verglasung bevorzugen

**Hersteller für Pilothouse-Segelyachten:**

| Bootsmarke | OEM-Lieferant Windschutzscheiben | Bemerkung |
|-----------|--------------------------------|-----------|
| **Hallberg-Rassy** (SE) | Trend Marine / eigene Fertigung | Premium, beheizt für skandinavische Gewässer |
| **Oyster** (UK) | Trend Marine | Custom für jedes Modell |
| **Discovery** (UK) | Trend Marine | Beheizt, Bluewater-Spezifikation |
| **Moody** (UK/DE) | Nautiglass / Trend Marine | Decksalon-Serie |
| **Bénéteau** (FR) | Euracryl (PMMA) / Bohamet (VSG) | OEM-Großserien |
| **Jeanneau** (FR) | Euracryl / Bohamet | Sun Odyssey DS, Yachts-Serie |
| **Garcia** (FR) | Trend Marine | Aluminium-Blauwasser-Yachten |

### 9.3 Center Console / Walkaround

**Typische Konfiguration (20–40 ft Center Console):**

| Parameter | Typisch |
|-----------|---------|
| Scheibenanzahl | 1 (einteilig, Wrap-around) oder 2–3 (flach) |
| Form | Flach (klappbar) oder gebogen (fest) |
| Neigung (Rake) | 15–30° |
| Material | PMMA 8–12 mm (Klappscheibe) oder ESG 6–8 mm (fest) |
| Wischer | 0–1 (oft keiner bei offenen Booten) |
| Heizung | Keine |
| Öffnung | Klappbar (gesamte Scheibe) oder fest |
| Preis Verglasungssystem (EUR) | 500–3.000 |

**Besonderheiten:**
- Hauptexposition: Spritzwasser, Salz, UV
- Scheibe muss leicht sein (PMMA oder PC, nicht Glas)
- Klappbare Windschutzscheiben müssen gegen unbeabsichtigtes Öffnen gesichert sein
- Kein geschlossenes Steuerhaus → keine Beschlagproblematik
- Edelstahl-Rahmen (316L) bevorzugt (Salzwasser)

### 9.4 Flybridge

**Typische Konfiguration (Flybridge-Motoryacht 14–24 m):**

| Parameter | Typisch |
|-----------|---------|
| Scheibenanzahl | 1–3 (Front) |
| Form | Flach oder leicht gebogen |
| Neigung (Rake) | 10–25° |
| Glastyp | ESG 6–8 mm (Standardboot), VSG 8–10 mm (Premium) |
| Wischer | 0–1 Pendelwischer (optional) |
| Heizung | Keine (Flybridge wird bei Kälte nicht genutzt) |
| Öffnung | Oft klappbar oder abnehmbar |
| Preis Verglasungssystem (EUR) | 1.000–5.000 |

**Besonderheiten:**
- Höher über Wasserlinie → geringere Wellenbelastung (ISO 12216 Position 2–3)
- Wind- und UV-Exposition hoch
- Gewicht minimieren (CG-empfindlich: Flybridge ist höchster Punkt)
- Spritzwasserschutz wichtiger als Wellenwiderstand
- Häufig nachgerüstet: Hardtop + Windschutzscheibe wird oft nach Kauf ergänzt

### 9.5 Superyacht (>24 m)

**Typische Konfiguration (30–60 m Motoryacht):**

| Parameter | Typisch |
|-----------|---------|
| Scheibenanzahl | 5–12 (Front, Brücke) + 8–20 (Seite) |
| Form | Compound-curved (Design-Priorität) |
| Glastyp | VSG 16–25 mm, oft mit SGP-Zwischenschicht |
| Beschichtung | Solar-Control Low-E, Acoustic PVB |
| Wischer | 2–4 Pantograph-Wischer |
| Heizung | ITO + Warmluft-Defrost (Kombination) |
| Öffnung | Elektrische Schiebescheiben (Besenzoni P.800) |
| Brandschutz | SOLAS A-0 (Brückenfenster), A-15/A-30 (Maschinenraum-Grenze) |
| Preis Verglasungssystem (EUR) | 50.000–500.000+ |

**Besonderheiten Superyacht:**
- Jede Scheibe ist eine Einzelanfertigung
- Klasse-Zertifizierung (LR/DNV/BV/RINA) obligatorisch
- Biegeformen (Molds) werden für jedes Boot neu gebaut → erhebliche Werkzeugkosten
- Akustik: Acoustic-PVB in allen Brückenfenstern (Maschinengeräusch-Isolation)
- Privatsphäre: Getönte Scheiben oder Elektrochromes Glas (insbesondere Owner-Deck)
- Integration mit Brücken-Elektronik: Heizung, Wischer, Sonnenschutz → zentrale Gebäudesteuerung (z.B. Lutron, Crestron)
- Gewicht einer einzelnen Superyacht-Frontscheibe: 50–300 kg → Kran für Einbau nötig
- Wartung: Regelmäßige Inspektion der Klebfugen (jährlich, durch Surveyor)
- Ersatzbeschaffung: 3–6 Monate Lieferzeit für Compound-Curved-Scheiben → Notscheibe (flach, temporär) an Bord empfohlen

**Typische Superyacht-Windschutzscheiben-Konfiguration (Beispiel 40 m MY):**

| Position | Anzahl | Maße je Scheibe (mm) | Glasaufbau | Beschichtung | Heizung |
|----------|--------|---------------------|-----------|-------------|---------|
| Brücke Front Center | 1 | 2.500 × 1.200 | VSG 19 mm (8+1.52+8, SGP) | Solar-Control Low-E | ITO |
| Brücke Front Port/Stbd | 2 | 1.800 × 1.200 | VSG 16 mm (6+1.52+6) | Solar-Control | ITO |
| Brücke Wrap Port/Stbd | 2 | 1.200 × 1.200 | VSG 14 mm (6+0.76+6) | Low-E | Heizdraht |
| Brücke Schiebefenster | 2 | 800 × 1.000 | VSG 12 mm (5+0.76+5) | Klar | Defogger |
| Owner-Deck Front | 3 | 2.200 × 1.400 | VSG 19 mm + Electrochromic | Solar-Control + EC | ITO |

**Geschätzte Kosten dieses Systems:**

| Posten | Kosten (EUR) |
|--------|-------------|
| Glasscheiben (10 Stück) | 80.000–150.000 |
| Biegeformen/Werkzeuge | 30.000–60.000 |
| Rahmen (Aluminium, pulverbeschichtet) | 20.000–40.000 |
| Wischer-System (4× Pantograph Exalto 1700) | 8.000–16.000 |
| Scheibenheizung (ITO + Heizdraht) | 15.000–30.000 |
| Defogger-System | 5.000–10.000 |
| Elektrochromes Glas (3 Scheiben Owner-Deck) | 25.000–50.000 |
| Montage (Werft, 2–3 Wochen) | 15.000–30.000 |
| **Gesamt** | **198.000–386.000** |

> Confidence: `estimated` (Superyacht-Projektpreise sind stark projektabhängig, Richtwerte basierend auf Werft-Erfahrung und Hersteller-Angaben)

---

*Ende der ersten ~2000 Zeilen — Wissensdatei 08.03 Windschutzscheiben und Frontfenster*
*Weiterführende Abschnitte (Schadenskatalog, Wartungsintervalle, FAQ, Glossar, Expertenstimmen) in späterer Erweiterung*

---

## Technische Referenz & Berechnungen

### Glasdickenberechnung nach ISO 12216

Die Mindestglasdicke für Windschutzscheiben auf Yachten wird gemäß ISO 12216:2020 berechnet. Die Norm unterscheidet zwischen vorgespanntem Einscheibensicherheitsglas (ESG), Verbundsicherheitsglas (VSG) und thermisch vorgespanntem Glas (TVG).

#### Grundformel (vereinfacht)

```
t_min = k × a × √(P_design / σ_zul)
```

| Variable | Bedeutung | Einheit |
|----------|-----------|---------|
| t_min | Mindest-Glasdicke | mm |
| k | Formfaktor (abhängig vom Seitenverhältnis a/b) | dimensionslos |
| a | kürzere Seite der Scheibe | mm |
| P_design | Design-Druck (aus Fahrtgebiet + Geschwindigkeit) | kPa |
| σ_zul | zulässige Biegezugspannung des Glases | MPa |

#### Design-Druck nach CE-Kategorie und Geschwindigkeit

| CE-Kategorie | Basis-Druck P_base (kPa) | Geschwindigkeitszuschlag |
|--------------|---------------------------|--------------------------|
| A (Ozean) | 8,0 | + 0,5 × v² / 1000 (v in kn) |
| B (Offshore) | 6,0 | + 0,5 × v² / 1000 |
| C (Küste) | 4,5 | + 0,5 × v² / 1000 |
| D (Binnengewässer) | 3,0 | + 0,3 × v² / 1000 |

Für Motoryachten mit v > 20 kn ist der Fahrtwind-Druck oft dimensionierend:

```
P_wind = 0,5 × ρ_luft × v² = 0,5 × 1,225 × (v × 0,5144)²
```

Bei 30 kn: P_wind ≈ 0,5 × 1,225 × 15,43² ≈ 146 Pa ≈ 0,146 kPa (zusätzlich zum Wellendruck)

#### Zulässige Biegezugspannung

| Glastyp | σ_zul (MPa) | Sicherheitsfaktor |
|---------|-------------|-------------------|
| ESG (Einscheiben-Sicherheit) | 120 | 3,5 |
| TVG (teilvorgespannt) | 70 | 3,5 |
| VSG mit ESG-Lagen | 100 (pro Lage) | 3,5 |
| VSG mit TVG-Lagen | 60 (pro Lage) | 3,5 |
| Float (ungespannt) | 45 | 4,0 |

> ⚠️ **ZU PRÜFEN (Audit):** Diese Tabelle bezeichnet 120 / 70 / 100 / 60 / 45 MPa als "Zulässige Biegezugspannung" (σ_zul). Im Haupttext (§1.4.3 und §7.2.1) ist die zulässige Spannung σ_allow dagegen mit ESG 35 / VSG 28 / Float 10 MPa angegeben. 120/70/45 MPa sind physikalisch die charakteristischen Bruchfestigkeiten (vgl. EN 16612), NICHT die zulässigen Spannungen (= charakteristische Festigkeit ÷ Sicherheitsfaktor ~3,5). Wer 120 MPa direkt in die Dickenformel t_min = k·a·√(P/σ_zul) einsetzt, unterdimensioniert die Scheibe um ca. Faktor 1,8 — sicherheitskritisch. Konvention (charakteristisch vs. zulässig) vor Nutzung eindeutig festlegen; bis dahin nicht als `measured` verwenden.

#### Praxistabelle: Empfohlene Glasdicken nach Scheibengröße

| Scheibenfläche (mm × mm) | CE-Kat A/B ESG | CE-Kat A/B VSG | CE-Kat C/D ESG | CE-Kat C/D VSG |
|---------------------------|----------------|----------------|----------------|----------------|
| 400 × 300 | 6 mm | 2×4 mm (8,76) | 5 mm | 2×3 mm (6,76) |
| 600 × 400 | 8 mm | 2×5 mm (10,76) | 6 mm | 2×4 mm (8,76) |
| 800 × 500 | 10 mm | 2×5 mm (10,76) | 8 mm | 2×4 mm (8,76) |
| 1000 × 600 | 12 mm | 2×6 mm (12,76) | 10 mm | 2×5 mm (10,76) |
| 1200 × 700 | 15 mm | 2×8 mm (16,76) | 12 mm | 2×6 mm (12,76) |
| 1500 × 800 | 19 mm | 2×10 mm (20,76) | 15 mm | 2×8 mm (16,76) |

> Die Werte in Klammern bei VSG bezeichnen die Gesamtdicke inkl. PVB-Folie (0,76 mm Standard).

#### Formfaktor k nach Seitenverhältnis

| a/b | k (eingespannt, 4 Seiten) | k (2 Seiten eingespannt) |
|-----|---------------------------|--------------------------|
| 1,0 | 0,0138 | 0,0625 |
| 1,5 | 0,0220 | 0,0625 |
| 2,0 | 0,0277 | 0,0625 |
| 3,0 | 0,0323 | 0,0625 |
| ∞ | 0,0333 | 0,0625 |

### Verklebungsbreite (Structural Glazing)

Die Klebefugenbreite ist entscheidend für die Übertragung von Wind- und Wellenlasten:

```
b_min = P_design × a / (2 × σ_kleber_zul)
```

| Parameter | Wert |
|-----------|------|
| σ_kleber_zul (Sikaflex 295 UV) | 0,8 MPa (Zugfestigkeit) |
| σ_kleber_zul (Sikaflex 552) | 1,0 MPa |
| σ_kleber_zul (3M VHB 4991) | 0,4 MPa (nur Sekundär) |
| σ_kleber_zul (Dow 795) | 0,14 MPa (Dauerlast) |

#### Praxiswerte Klebefugenbreite

| Scheibengröße (mm) | CE-Kat A/B | CE-Kat C/D | Minimum |
|---------------------|------------|------------|---------|
| 400 × 300 | 15 mm | 12 mm | 10 mm |
| 600 × 400 | 20 mm | 15 mm | 12 mm |
| 800 × 500 | 25 mm | 20 mm | 15 mm |
| 1000 × 600 | 30 mm | 25 mm | 20 mm |
| 1200 × 700 | 35 mm | 30 mm | 25 mm |
| 1500 × 800 | 45 mm | 35 mm | 30 mm |

Klebefugendicke: 6–12 mm (optimal 8–10 mm für Spannungsausgleich).

### Wischer-Geometrie und Wischfeld

#### Wischertypen und Wischfeldberechnung

**Pendelwischer (Standard):**
```
Wischfeld = (π × L²_wisch / 2) × (α / 180°)
```
- L_wisch: Wischblattlänge (mm)
- α: Pendelwinkel (typisch 70–110°)

**Pantograph-Wischer (Parallelwischer):**
```
Wischfeld ≈ L_arm × L_wisch × sin(α)
```
- L_arm: Armauslage (mm)
- L_wisch: Wischblattlänge (mm)
- α: Schwenkwinkel (typisch 60–90°)

#### Empfohlene Wischergrößen

| Scheibenbreite (mm) | Scheibenhöhe (mm) | Wischertyp | Wischblatt (mm) | Abdeckung |
|----------------------|-------------------|------------|-----------------|-----------|
| 400–600 | 300–400 | Pendel | 350–450 | ≥ 85% |
| 600–800 | 400–500 | Pendel | 450–550 | ≥ 80% |
| 800–1000 | 500–600 | Pantograph | 500–650 | ≥ 80% |
| 1000–1200 | 600–700 | Pantograph | 600–750 | ≥ 75% |
| 1200–1500 | 700–900 | Pantograph | 700–900 | ≥ 75% |

Wischgeschwindigkeit: 1. Stufe 30–45 Doppelhübe/min, 2. Stufe 50–70 Doppelhübe/min.

#### Waschdüsen-Positionierung

- Abstand Düse–Scheibe: 20–50 mm
- Sprühwinkel: 60–90° zur Scheibe
- Durchfluss pro Düse: 80–150 ml/min
- Tankapazität Scheibenwaschanlage: 2–5 Liter (Süßwasser + Reiniger 1:10)

---

## Einbau-/Austausch-Anleitung

### Strukturelle Verklebung — Vollständiges Verfahren

Die folgende Anleitung beschreibt den vollständigen Prozess einer Structural-Glazing-Verklebung für Yacht-Windschutzscheiben gemäß Herstellerangaben (Sika, Dow) und gängiger Werftpraxis.

#### Phase 1: Vorbereitung (Tag 1)

**Schritt 1 — Umgebungsbedingungen prüfen**
- Lufttemperatur: 15–30 °C (ideal 20–25 °C)
- Relative Luftfeuchte: 40–70% (wichtig für Aushärtung)
- Kein Regen, kein direktes Sonnenlicht auf Klebefläche
- Substrattemperatur: mindestens 5 °C über Taupunkt
- Wind: < 15 km/h (Staubkontamination)

**Schritt 2 — Altscheibe entfernen (bei Austausch)**
- Schneidedraht (Ø 0,6–0,8 mm) oder oszillierendes Messer verwenden
- Von unten nach oben schneiden, Scheibe mit Saugheber sichern
- Restkleber mit Cuttermesser + Spachtel entfernen (max. 1 mm stehenlassen)
- Flansch auf Beschädigungen prüfen — Korrosion behandeln

**Schritt 3 — Flansch vorbereiten**
- Reinigung 1: Grobreinigung mit Isopropanol (IPA) oder Sika Remover 208
- Trocknen lassen: 10 min
- Reinigung 2: Feinreinigung mit Sika Aktivator 205 (bei Aluminium) oder Sika Aktivator 100 (bei GFK)
- Auftragsmethode: fusselfreies Tuch, in eine Richtung wischen, nicht zurück
- Flash-off-Zeit: 10–30 min (temperaturabhängig)

**Schritt 4 — Primer auf Flansch**
- Sika Primer 206 G+P (für lackiertes Metall, GFK)
- Oder: Sika Primer 209 D (für Aluminium blank)
- Dünn auftragen mit Pinsel oder Filzapplikator
- Schichtdicke: 5–15 μm (transparent bis leicht gelblich)
- Mindest-Ablüftzeit: 30 min bei 23 °C
- Maximale offene Zeit nach Primer: 8 Stunden (danach erneut primern)

#### Phase 2: Glasvorbereitung

**Schritt 5 — Glaskante vorbereiten**
- Keramikrand (bei ESG/VSG mit Siebdruck): keine weitere Behandlung nötig
- Blanke Glaskante: Reinigung mit IPA, dann Sika Primer 210 T
- Flash-off: 10 min
- Abkleben: Klebefläche mit Malerkrepp definieren (Fugenbreite markieren)

**Schritt 6 — Primer auf Glas**
- Sika Primer 210 T (für Glas und Keramikrand)
- Auftrag: dünn, gleichmäßig, mit fusselfreiem Filz
- Ablüftzeit: 10 min bei 23 °C
- Maximale offene Zeit: 2 Stunden

#### Phase 3: Verklebung

**Schritt 7 — Kleber auftragen**
- Kartusche: Sika 295 UV (1-K PU, schwarz, UV-beständig) oder Sikaflex 252 (für Innenanwendung)
- Kartuschengröße: 300 ml oder 600 ml
- Düse: Dreiecksdüse passend zur Fugenbreite (z. B. 12 × 10 mm)
- Auftrag auf Flansch (nicht auf Glas bei großen Scheiben)
- Raupe gleichmäßig ohne Unterbrechungen auftragen
- Keine Lufteinschlüsse — Kartusche gleichmäßig führen

**Schritt 8 — Scheibe einsetzen**
- Saugheber mit mindestens 2 Köpfen verwenden (4 bei > 1 m²)
- Scheibe in einem Zug positionieren — Nachkorrektur nur innerhalb 10 min
- Gleichmäßig andrücken — Fugendicke mit Abstandshaltern (Distanzklötze) sichern
- Distanzklötze: 6–10 mm PE oder Silikon, alle 300 mm
- Überschüssigen Kleber sofort mit Spachtel + Sika Remover 208 entfernen

**Schritt 9 — Fixierung während Aushärtung**
- Klebeband (Packaging-Tape) zur Lagesicherung
- Keine mechanische Belastung für mindestens 24 h
- Bei großen Scheiben: temporäre Stützen oder Schraubklemmen

#### Phase 4: Aushärtung

**Schritt 10 — Aushärteparameter**

| Kleber | Hautbildungszeit | Durchhärtung/mm/24h | Volle Festigkeit |
|--------|-----------------|---------------------|------------------|
| Sikaflex 295 UV | 45–90 min | 3–4 mm | 7 Tage |
| Sikaflex 252 | 30–60 min | 3–4 mm | 5–7 Tage |
| Sikaflex 552 | 20–40 min | 4–5 mm | 5 Tage |
| Dow 795 (Silikon) | 15–30 min | 2–3 mm | 14–21 Tage |

- Aushärtung benötigt Luftfeuchtigkeit (1-K PU: feuchtigkeitshärtend)
- Bei trockener Luft (<30% rH): Aushärtung mit feuchtem Tuch über Fuge beschleunigen
- Boot nicht bewegen/kranen für mindestens 48–72 h
- Keine Vibrationen (Motorlauf, Schleifarbeiten in Nähe) für 24 h

#### Phase 5: Qualitätskontrolle

**Schritt 11 — Sichtprüfung (nach 24 h)**
- Klebefuge durchgehend geschlossen
- Keine Luftblasen sichtbar
- Scheibe in korrekter Position (± 2 mm)
- Distanzklötze nicht verschoben
- Oberfläche sauber, kein Kleberrückstand

**Schritt 12 — Funktionsprüfung (nach 7 Tagen)**
- Wassertest: Schlauch auf Scheibe, 15 min bei 2 bar
- Wischer-Funktionstest
- Visuell auf Undichtigkeit prüfen (innen)
- Dokumentation: Foto, Datum, Kleber-Charge, Verarbeiter

### Werkzeug- und Materialliste

| Werkzeug/Material | Spezifikation | Ca. Kosten (EUR) |
|--------------------|---------------|-------------------|
| Saugheber (Doppel) | 80 kg Tragkraft | 120–250 |
| Schneidedraht-Set | Edelstahl Ø 0,6 mm, 25 m + Griffe | 30–60 |
| Sika Primer 206 G+P | 250 ml | 35–50 |
| Sika Primer 210 T | 250 ml | 30–45 |
| Sika Aktivator 205 | 250 ml | 25–40 |
| Sikaflex 295 UV | 600 ml Kartusche | 25–40 |
| Kartuschenpistole (Druckluft) | 310/600 ml | 80–200 |
| Dreiecksdüsen-Set | 6/8/10/12 mm | 15–25 |
| Distanzklötze PE | 6/8/10 mm, 100 Stück | 10–20 |
| Fusselfreie Tücher | 100 Stück | 15–25 |
| Malerkrepp 19 mm | 4 Rollen | 10–15 |
| Sika Remover 208 | 1 Liter | 20–35 |

> **Sicherheitshinweis:** Primer und Aktivatoren sind lösemittelhaltig — Schutzbrille, Nitrilhandschuhe, gute Belüftung. Sicherheitsdatenblätter beachten.

---

## Lebensdauer und Alterungsmechanismen

### Lebensdauer-Übersicht

| Komponente | Erwartete Lebensdauer | Beeinflussende Faktoren |
|------------|----------------------|------------------------|
| VSG-Glasscheibe | 20–30+ Jahre | UV-Exposition, mechanische Belastung |
| ESG-Glasscheibe | 25–40+ Jahre | Kantenbeschädigung, Nickel-Sulfid-Einschlüsse |
| PVB-Zwischenschicht (VSG) | 15–25 Jahre | UV, Feuchtigkeit, Temperatur |
| SentryGlas-Zwischenschicht | 25–35 Jahre | Deutlich UV-beständiger als PVB |
| Strukturelle Verklebung (PU) | 15–20 Jahre | UV, Salz, mechanische Dauerlast |
| Strukturelle Verklebung (Silikon) | 20–30 Jahre | Höhere UV-Beständigkeit |
| Gummidichtung (EPDM) | 8–15 Jahre | UV, Ozon, mechanische Beanspruchung |
| Scheibenwischer-Gummi | 1–2 Jahre | UV, Salzwasser, mechanischer Abrieb |
| Wischermotor | 5–10 Jahre | Salzkorrosion, Betriebsstunden |
| Wischerarm (Edelstahl 316L) | 15–25 Jahre | Spaltkorrosion, mechanische Beanspruchung |
| Scheibenheizung (Heizdraht) | 10–20 Jahre | Thermische Zyklen, Korrosion |
| Scheibenheizung (ITO-Beschichtung) | 15–25 Jahre | Abrieb, UV |
| Rahmendichtung (Silikon) | 10–15 Jahre | UV, Bewegung, Reinigungsmittel |
| Elektrochromes Glas | 10–15 Jahre | Schaltzyklenzahl (typ. 50.000+) |

### Alterungsmechanismus 1: UV-Degradation der Verklebung

**Prozess:** UV-Strahlung spaltet Polymerketten im PU-Kleber. Oberfläche vergilbt, wird spröde, Mikrorisse entstehen. Wasser dringt über Mikrorisse ein und beschleunigt den Abbau.

**Zeitverlauf:**
- 0–5 Jahre: Keine sichtbaren Veränderungen, volle Festigkeit
- 5–10 Jahre: Leichte Oberflächenvergilbung, Elastizität -10–15%
- 10–15 Jahre: Sichtbare Versprödung, Elastizität -20–30%, erste Mikrorisse
- 15–20 Jahre: Deutliche Rissbildung, Festigkeit -30–50%, Austausch empfohlen
- 20+ Jahre: Kritischer Zustand, Versagen möglich

**Prävention:** UV-beständigen Kleber verwenden (Sikaflex 295 UV), Fuge mit UV-Schutzband abdecken, regelmäßig inspizieren.

### Alterungsmechanismus 2: PVB-Delamination

**Prozess:** Feuchtigkeit dringt über die Glaskanten in die PVB-Folie ein. PVB nimmt Wasser auf (hygroskopisch), quillt, verliert Haftung zum Glas. Sichtbar als milchige Trübung oder Blasenbildung am Scheibenrand.

**Zeitverlauf:**
- 0–10 Jahre: Keine Veränderung bei korrekter Kantenversiegelung
- 10–15 Jahre: Erste Randtrübung möglich (2–5 mm vom Rand)
- 15–20 Jahre: Trübung breitet sich aus (5–15 mm), erste Blasen
- 20–25 Jahre: Großflächige Delamination, Scheibenaustausch nötig

**Prävention:** Polysulfid- oder Silikon-Kantenversiegelung, SentryGlas statt PVB für kritische Positionen, Scheiben nicht vollständig mit Wasser umspülen.

### Alterungsmechanismus 3: Nickel-Sulfid-Einschlüsse (ESG)

**Prozess:** Mikroskopische NiS-Einschlüsse im Float-Glas durchlaufen nach dem Vorspannen eine langsame Phasenumwandlung (α → β). Die Volumenzunahme (~4%) erzeugt Spannungen, die zum spontanen Bruch führen können.

**Statistik:** Betrifft ca. 1 von 500 ESG-Scheiben, meist innerhalb der ersten 5 Jahre.

**Prävention:** Heat-Soak-Test (HST) nach EN 14179: Scheiben 2 h bei 290 °C halten. Reduziert Ausfallwahrscheinlichkeit auf 1:10.000. Für Yacht-Windschutzscheiben empfohlen.

### Alterungsmechanismus 4: Korrosion der Scheibenheizung

**Heizdraht-Systeme:** Wolframdrähte (Ø 20–50 μm) in der PVB-Schicht. Korrosion beginnt an Kontaktstellen zum Rand. Symptom: einzelne Heizlinien fallen aus, ungleichmäßige Erwärmung.

**ITO-Beschichtung:** Indium-Zinn-Oxid als transparente Leitschicht. Degradation durch mechanischen Abrieb (Wischer!) und Feuchtigkeit. Symptom: Fleckige Erwärmung, steigende Stromaufnahme.

### Wartungsintervalle

| Komponente | Intervall | Maßnahme |
|------------|-----------|----------|
| Glasscheibe | 6 Monate | Sichtprüfung auf Kratzer, Chips, Risse |
| Verklebung | 12 Monate | Sichtprüfung Fuge auf Risse, Ablösung |
| Verklebung | 5 Jahre | Haftungsprüfung (Drucktest mit Seifenwasser) |
| Dichtungen | 12 Monate | Sichtprüfung, Silikonspray |
| Wischergummi | 6 Monate | Prüfung auf Schlieren, ggf. tauschen |
| Wischermotor | 12 Monate | Funktionsprüfung, Stromaufnahme messen |
| Wischerarm | 12 Monate | Andruck prüfen (typisch 200–400 g/cm) |
| Scheibenheizung | 12 Monate | Funktionsprüfung, Wärmebild |
| Waschanlage | 6 Monate | Düsen prüfen, Tank auffüllen |

---

## Fehlerbild-Atlas

### Fehlerbild FB-WS-01: Haarlinienriss (Spannungsriss)

- **Erscheinung:** Feiner, meist geradliniger Riss ohne erkennbaren Einschlagpunkt, oft vom Scheibenrand ausgehend
- **Ursache:** Thermische Spannungen, ungleichmäßige Erwärmung (Scheibenheizung defekt, partieller Sonnenschatten), oder Einbauspannung durch zu enge Rahmung
- **Häufigkeit:** Mittel (ca. 8% aller Windschutzscheiben-Schäden)
- **Betroffene Bootsklassen:** Alle, besonders bei dunklen Rahmen in tropischen Gewässern
- **Risikobewertung:** 60/100 — Riss kann wachsen, Scheibe muss beobachtet werden
- **Sofortmaßnahme:** Rissende mit Glasbohrer (Ø 3 mm) aufbohren, um Ausbreitung zu stoppen
- **Langfrist-Lösung:** Scheibentausch innerhalb 3–6 Monaten planen
- **Erkennungsmethode_visuell:** Bei seitlicher Beleuchtung oder mit Polarisationsfilter gut sichtbar
- **Verwechslungsgefahr:** Kann mit Kratzer verwechselt werden — Riss fühlt sich auf beiden Seiten an
- **Confidence:** `visual_high` (bei klarem Foto eindeutig identifizierbar)
- **AYDI-Score-Auswirkung:** Compliance -15, Structural -10
- **Reparaturkosten:** 800–3.000 EUR (Scheibentausch je nach Größe)
- **Präventionsempfehlung:** Scheibenheizung gleichmäßig auslegen, Einbautoleranzen einhalten

### Fehlerbild FB-WS-02: Steinschlag / Impact-Krater

- **Erscheinung:** Sternförmiger oder kreisförmiger Einschlag (Ø 5–30 mm) mit weißlichem Kern, oft mit radialen Rissen
- **Ursache:** Aufprall von Gegenständen (Winde, Schäkel bei Segelmanövern, angeschwemmtes Material)
- **Häufigkeit:** Hoch bei Segelbooten (ca. 15% aller Schäden), niedrig bei Motoryachten mit Hardtop
- **Betroffene Bootsklassen:** Segelyachten (Großschot, Fallen), Sportboote (Trailer-Transport)
- **Risikobewertung:** 45/100 (VSG: Scheibe bleibt intakt) bis 85/100 (ESG: Totalbruch möglich)
- **Sofortmaßnahme:** Bei VSG: Steinschlagreparatur mit UV-Harz innerhalb 48 h (wenn < 20 mm)
- **Langfrist-Lösung:** Scheibentausch bei Rissbildung > 50 mm oder > 3 Einschläge
- **Erkennungsmethode_visuell:** Deutlich sichtbar, Kamera-Makro empfohlen für Rissausbreitung
- **Verwechslungsgefahr:** Keine — eindeutiges Fehlerbild
- **Confidence:** `visual_high`
- **AYDI-Score-Auswirkung:** Structural -5 bis -20 (je nach Schwere), Compliance -5
- **Reparaturkosten:** 150–350 EUR (Harzfüllung) oder 800–3.000 EUR (Austausch)
- **Präventionsempfehlung:** Schutznetz über Winschen, Windschutzfolie beim Trailern

### Fehlerbild FB-WS-03: PVB-Delamination (Randtrübung)

- **Erscheinung:** Milchig-weiße Trübung am Scheibenrand (3–30 mm breit), teils blasig, breitet sich über Jahre aus
- **Ursache:** Feuchtigkeitseintritt über unversiegelte oder beschädigte Glaskante in die PVB-Zwischenschicht
- **Häufigkeit:** Hoch bei Scheiben > 12 Jahre (ca. 20% aller VSG-Scheiben)
- **Betroffene Bootsklassen:** Alle mit VSG-Verglasung, besonders in tropischen Revieren
- **Risikobewertung:** 30/100 (Anfangsstadium, < 10 mm) bis 65/100 (> 30 mm, strukturelle Schwächung)
- **Sofortmaßnahme:** Kantenversiegelung erneuern, Wasserexposition minimieren
- **Langfrist-Lösung:** Scheibentausch, neue Scheibe mit Polysulfid-Kantenversiegelung
- **Erkennungsmethode_visuell:** Bei Durchlicht deutlich, bei Auflicht subtiler
- **Verwechslungsgefahr:** Kann mit interner Verschmutzung oder Kondensat verwechselt werden
- **Confidence:** `visual_medium` (Foto muss Randbereich in Durchlicht zeigen)
- **AYDI-Score-Auswirkung:** Materials -15, Emotional -10 (ästhetisch störend)
- **Reparaturkosten:** 1.200–4.000 EUR (nur Austausch möglich)
- **Präventionsempfehlung:** SentryGlas statt PVB, Polysulfid-Kantenversiegelung ab Werk

### Fehlerbild FB-WS-04: Verklebungsablösung (Bonding Failure)

- **Erscheinung:** Sichtbarer Spalt zwischen Glas und Rahmen, Scheibe lässt sich leicht eindrücken, Wasser dringt ein
- **Ursache:** UV-Alterung des Klebers, falsche Primer-Anwendung bei Montage, Substrat-Inkompatibilität
- **Häufigkeit:** Mittel (ca. 10% nach 15+ Jahren), häufiger bei DIY-Montagen
- **Betroffene Bootsklassen:** Alle, besonders bei nachgerüsteten Scheiben
- **Risikobewertung:** 85/100 — Sicherheitskritisch, Scheibe kann sich bei Seegang lösen
- **Sofortmaßnahme:** Temporäre Sicherung mit Klebeband oder Leisten, Boot nicht in raues Wasser
- **Langfrist-Lösung:** Scheibe vollständig entfernen, Flansch reinigen, Neuverklebung nach Protokoll
- **Erkennungsmethode_visuell:** Drucktest (Scheibe von außen drücken, auf Bewegung achten)
- **Verwechslungsgefahr:** Dichtungsverlust (Silikon) vs. Verklebungsverlust (strukturell) — kritisch unterscheiden
- **Confidence:** `visual_medium` (visuell oft erst bei fortgeschrittenem Stadium erkennbar)
- **AYDI-Score-Auswirkung:** Structural -30, Compliance -25, Safety KRITISCH
- **Reparaturkosten:** 1.500–6.000 EUR (Neuverklebung inkl. Material und Arbeit)
- **Präventionsempfehlung:** Professionelle Erstmontage, 5-Jahres-Inspektionsintervall

### Fehlerbild FB-WS-05: Wischerschlieren (Streaking)

- **Erscheinung:** Schlierenförmige Wasserrückstände nach Wischerbetrieb, unregelmäßiges Wischbild
- **Ursache:** Verschlissenes Wischergummi, Salzkristalle auf Scheibe, falsche Wischeranpressung
- **Häufigkeit:** Sehr hoch (ca. 40% aller Boote nach 1 Saison)
- **Betroffene Bootsklassen:** Alle
- **Risikobewertung:** 25/100 — Sichtbehinderung, besonders nachts und bei Gegenlicht
- **Sofortmaßnahme:** Scheibe mit Süßwasser reinigen, Wischergummi mit Essigwasser abwischen
- **Langfrist-Lösung:** Wischergummi tauschen (alle 1–2 Saisons)
- **Erkennungsmethode_visuell:** Bei Regen oder Wischertest sofort sichtbar
- **Verwechslungsgefahr:** Keine
- **Confidence:** `visual_high`
- **AYDI-Score-Auswirkung:** Ergonomics -5, Service_patterns +5 (Wartungsstau-Indikator)
- **Reparaturkosten:** 30–120 EUR (Gummi-Ersatz) oder 80–300 EUR (inkl. Montage)
- **Präventionsempfehlung:** Wischergummi vor Winterlager mit Glycerin einreiben

### Fehlerbild FB-WS-06: Kratzspuren im Sichtfeld

- **Erscheinung:** Parallele oder kreisförmige feine Kratzer, besonders bei Gegenlicht/Sonneneinstrahlung sichtbar
- **Ursache:** Wischerbetrieb auf trockener/sandiger Scheibe, aggressive Reinigungsmittel, Scheuerschwamm
- **Häufigkeit:** Hoch (ca. 25% aller Scheiben > 5 Jahre)
- **Betroffene Bootsklassen:** Alle, besonders Küsten- und Flussboote (Sand/Staub)
- **Risikobewertung:** 20/100 (leichte Kratzer) bis 50/100 (tiefe Kratzer mit Blendwirkung)
- **Sofortmaßnahme:** Cerium-Oxid-Politur (nur bei leichten Kratzern auf ESG wirksam)
- **Langfrist-Lösung:** Scheibentausch bei tiefen Kratzern, Schutzfolie nach Erneuerung
- **Erkennungsmethode_visuell:** Foto bei schrägem Lichteinfall, idealerweise mit Gegenlichtquelle
- **Verwechslungsgefahr:** Ablagerungen (abwischbar) vs. Kratzer (permanent)
- **Confidence:** `visual_medium` (abhängig von Lichtverhältnissen auf dem Foto)
- **AYDI-Score-Auswirkung:** Emotional -10, Ergonomics -5 (Blendung)
- **Reparaturkosten:** 80–200 EUR (Politur) oder 800–3.000 EUR (Austausch)
- **Präventionsempfehlung:** Immer Süßwasser vorsprühen, nur Mikrofaser oder Fensterleder verwenden

### Fehlerbild FB-WS-07: Beschlagsbildung zwischen VSG-Lagen

- **Erscheinung:** Permanenter Beschlag/Nebel zwischen den Glaslagen, nicht abwischbar, oft fleckig
- **Ursache:** PVB-Degradation mit Feuchtigkeitseintritt, Übergang von Delamination
- **Häufigkeit:** Gering (ca. 5% aller VSG, meist > 15 Jahre alt)
- **Betroffene Bootsklassen:** Alle mit VSG
- **Risikobewertung:** 40/100 (Sichtbehinderung, kein unmittelbares Sicherheitsrisiko)
- **Sofortmaßnahme:** Keine Sofortmaßnahme möglich — irreversibel
- **Langfrist-Lösung:** Scheibentausch erforderlich
- **Erkennungsmethode_visuell:** Unterscheidung von Oberflächenbeschlag: Tuch-Test (innen/außen sauber → internes Problem)
- **Verwechslungsgefahr:** Innerer Beschlag (Kondensat) — dieser verschwindet bei Belüftung/Heizung
- **Confidence:** `visual_medium`
- **AYDI-Score-Auswirkung:** Materials -20, Emotional -15, Ergonomics -10
- **Reparaturkosten:** 1.200–4.000 EUR (nur Austausch)
- **Präventionsempfehlung:** SentryGlas-Zwischenschicht, Kantenversiegelung

### Fehlerbild FB-WS-08: Spontanbruch ESG (Nickel-Sulfid)

- **Erscheinung:** Scheibe zerfällt vollständig in kleine, stumpfe Krümel, kein Einschlagpunkt erkennbar
- **Ursache:** Nickel-Sulfid-Einschluss (NiS) mit Phasenumwandlung, auch ohne äußere Einwirkung
- **Häufigkeit:** Selten (1:500 bei Standard-ESG, 1:10.000 nach HST)
- **Betroffene Bootsklassen:** Alle mit ESG-Verglasung (ohne VSG-Schutz)
- **Risikobewertung:** 95/100 — Sofortiger Totalverlust der Scheibe, Sicherheitsrisiko bei Seegang
- **Sofortmaßnahme:** Öffnung mit Plane/Folie verschließen, sicheren Hafen anlaufen
- **Langfrist-Lösung:** Ersatz durch VSG oder ESG mit HST-Prüfung (EN 14179)
- **Erkennungsmethode_visuell:** Unverwechselbar — vollständig zerbrochene Scheibe in kleine Stücke
- **Verwechslungsgefahr:** Mechanischer Bruch (hat sichtbaren Einschlagpunkt mit Sternmuster)
- **Confidence:** `visual_high`
- **AYDI-Score-Auswirkung:** Structural -50, Compliance -40, Safety KRITISCH
- **Reparaturkosten:** 1.500–5.000 EUR (Notfall-Ersatz, höher wegen Dringlichkeit)
- **Präventionsempfehlung:** VSG statt reines ESG, oder ESG nur mit HST-Prüfung einsetzen

### Fehlerbild FB-WS-09: Rahmenkorrosion (Aluminium-Pitting)

- **Erscheinung:** Weiße, pulverige Ablagerungen auf Aluminiumrahmen, Lochfraß-Vertiefungen
- **Ursache:** Galvanische Korrosion (Kontakt Al mit Edelstahl ohne Isolation), Salzwasser, beschädigte Beschichtung
- **Häufigkeit:** Mittel-hoch (ca. 15% aller Alu-Rahmen > 8 Jahre)
- **Betroffene Bootsklassen:** Alle mit Aluminiumrahmen, besonders Salzwasserreviere
- **Risikobewertung:** 55/100 — Schwächt Rahmenstruktur, kann Klebehaftung beeinträchtigen
- **Sofortmaßnahme:** Korrosion mechanisch entfernen (Scotch-Brite), Konversionsschicht auftragen
- **Langfrist-Lösung:** Rahmen sandstrahlen, neu pulverbeschichten, galvanische Trennung sicherstellen
- **Erkennungsmethode_visuell:** Weiße Flecken auf dunklem Rahmen gut sichtbar
- **Verwechslungsgefahr:** Salzablagerung (abwaschbar) vs. Korrosion (in Oberfläche eingefressen)
- **Confidence:** `visual_high`
- **AYDI-Score-Auswirkung:** Materials -15, Structural -10
- **Reparaturkosten:** 500–2.000 EUR (lokale Behandlung) oder 3.000–8.000 EUR (Rahmenaustausch)
- **Präventionsempfehlung:** EPDM-Isolation zwischen verschiedenen Metallen, regelmäßiges Süßwasserspülen

### Fehlerbild FB-WS-10: UV-Vergilbung der Zwischenschicht

- **Erscheinung:** Gelbliche bis bräunliche Verfärbung der gesamten Scheibe, gleichmäßig oder zoniert
- **Ursache:** UV-Degradation der PVB-Folie, besonders bei älterem PVB ohne UV-Stabilisatoren
- **Häufigkeit:** Mittel (ca. 12% aller VSG > 10 Jahre, häufiger in tropischen Revieren)
- **Betroffene Bootsklassen:** Alle mit VSG, besonders bei horizontaler Einbaulage (Deckscheiben)
- **Risikobewertung:** 25/100 — Ästhetisches Problem, leichte Sichtbeeinträchtigung
- **Sofortmaßnahme:** Keine Sofortmaßnahme möglich — irreversibel
- **Langfrist-Lösung:** Scheibentausch mit UV-stabilisiertem PVB oder SentryGlas
- **Erkennungsmethode_visuell:** Vergleich mit Referenz-Weißwert, am besten gegen weißen Hintergrund
- **Verwechslungsgefahr:** Getöntes Glas (Fabrikton, gleichmäßig) vs. Vergilbung (ungleichmäßig, fortschreitend)
- **Confidence:** `visual_medium` (Kameraweißabgleich kann täuschen)
- **AYDI-Score-Auswirkung:** Emotional -15, Materials -10
- **Reparaturkosten:** 1.200–4.000 EUR (nur Austausch)
- **Präventionsempfehlung:** SentryGlas oder UV-stabilisiertes PVB spezifizieren

### Fehlerbild FB-WS-11: Undichte Scheibenrahmen-Dichtung

- **Erscheinung:** Wassertropfen oder -spuren an der Innenseite des Rahmens, nasse Polster/Instrumente
- **Ursache:** Alterung der EPDM-/Silikon-Dichtung, thermische Verformung, mechanische Belastung
- **Häufigkeit:** Hoch (ca. 20% aller Boote > 7 Jahre)
- **Betroffene Bootsklassen:** Alle, besonders bei Gummi-Profil-Dichtungen (ältere Bauweise)
- **Risikobewertung:** 50/100 — Wasserschaden an Elektronik und Polstern, Schimmelgefahr
- **Sofortmaßnahme:** Dichtung von außen mit Sikaflex 291i oder Captain Tolley's Creeping Crack Cure abdichten
- **Langfrist-Lösung:** Dichtung komplett erneuern, ggf. auf Verklebung umrüsten
- **Erkennungsmethode_visuell:** Wasserflecken innen, Kalkränder am Rahmen
- **Verwechslungsgefahr:** Kondenswasser (gleichmäßig, temperaturabhängig) vs. Leckage (lokalisiert, windrichtungsabhängig)
- **Confidence:** `visual_medium` (Leckage nicht immer auf Foto sichtbar, Wassertest nötig)
- **AYDI-Score-Auswirkung:** Compliance -10, Structural -5, Service_patterns +10 (Wartungsstau)
- **Reparaturkosten:** 200–800 EUR (Nachdichtung) oder 1.000–3.000 EUR (Dichtungserneuerung)
- **Präventionsempfehlung:** Jährliche Wassertests, Dichtungen mit Silikonspray pflegen

### Fehlerbild FB-WS-12: Wischermotor-Blockade / Geräusche

- **Erscheinung:** Wischer bewegt sich nicht, bewegt sich ruckartig, oder erzeugt laute Schleif-/Knarzgeräusche
- **Ursache:** Salzkorrosion im Getriebe, Lagerverschleiß, Wassereinbruch ins Motorgehäuse, festsitzende Parkposition
- **Häufigkeit:** Mittel (ca. 10% aller Boote > 5 Jahre, höher bei ungeschützten Montagen)
- **Betroffene Bootsklassen:** Alle, besonders offene Steuerstandkonfigurationen
- **Risikobewertung:** 40/100 — Sicherheitsrelevant bei Schlechtwetter (eingeschränkte Sicht)
- **Sofortmaßnahme:** Sicherung prüfen, Motor entkoppeln und manuell drehen, WD-40 Marine
- **Langfrist-Lösung:** Motor zerlegen und warten oder ersetzen, korrosionsgeschütztes Modell wählen
- **Erkennungsmethode_visuell:** Visuelle Inspektion begrenzt — Funktionstest nötig
- **Verwechslungsgefahr:** Elektrischer Defekt (Sicherung, Schalter) vs. mechanischer Defekt (Motor, Getriebe)
- **Confidence:** `visual_low` (Funktionstest erforderlich, visuell kaum diagnostizierbar)
- **AYDI-Score-Auswirkung:** Ergonomics -10, Compliance -5
- **Reparaturkosten:** 100–300 EUR (Wartung) oder 400–1.200 EUR (Motor-Ersatz)
- **Präventionsempfehlung:** Motor jährlich schmieren, bei Nichtgebrauch entriegeln, Schutzkappe montieren

---

## Fehlerbehebungs-Leitfaden

### Problem 1: Scheibe beschlägt von innen trotz Heizung

**Symptom:** Sichtbare Kondensation auf der Innenseite, Heizung läuft, aber Beschlag bleibt.

**Diagnose-Ablauf:**
1. Heizleistung messen: Stromaufnahme am Heizkreis prüfen (Soll: lt. Herstellerangabe, typ. 2–8 A bei 12 V)
2. Oberflächentemperatur messen: Infrarot-Thermometer, Soll: 5–15 °C über Umgebungstemperatur
3. Verteilung prüfen: Gleichmäßig warm oder kalte Zonen?
4. Lüftung prüfen: Defogger-Düsen frei? Lüfter funktionsfähig?

**Ursache & Lösung:**

| Befund | Ursache | Maßnahme |
|--------|---------|----------|
| Stromaufnahme = 0 | Sicherung, Kabel, Schalter | Elektrik prüfen, Sicherung tauschen |
| Stromaufnahme normal, gleichmäßig kalt | Heizelement defekt (Drahtbruch) | Scheibentausch (Heizdraht nicht reparabel) |
| Kalte Zonen | Teilausfall Heizdraht | Bei < 20% Fläche tolerierbar, sonst Tausch |
| Scheibe warm, aber Beschlag bleibt | Belüftung unzureichend | Defogger-Düsen reinigen, Lüfter prüfen |
| Beschlag nur am Rand | Rahmenbrücke (Kältebrücke) | Thermische Trennung verbessern |

**Kosten:** 50–200 EUR (Elektrik/Lüftung) bis 2.000–5.000 EUR (Scheibentausch mit Heizung)

### Problem 2: Wasser dringt bei Fahrt ein, aber nicht im Hafen

**Symptom:** Undichtigkeit nur bei Fahrtgeschwindigkeit > 15 kn, insbesondere bei Gegenwind/Welle.

**Diagnose-Ablauf:**
1. Position der Leckage genau bestimmen (trockene Papiertücher entlang des Rahmens)
2. Wassertest mit Schlauch: von unten nach oben, sektor für Sektor
3. Klebefuge/Dichtung an der Leckstelle visuell inspizieren
4. Scheibenbeweglichkeit unter Druck prüfen

**Ursache & Lösung:**

| Befund | Ursache | Maßnahme |
|--------|---------|----------|
| Leckage am oberen Rand | Ablauflöcher in Rahmenschiene verstopft | Reinigen (Draht Ø 2 mm) |
| Leckage seitlich | Dichtungsschrumpfung an Ecken | Nachdichtung mit Sikaflex 291i |
| Leckage mittig unten | Klebefuge hat Hohlstelle | Neuverklebung dieses Abschnitts |
| Scheibe bewegt sich | Verklebung partiell gelöst | Sofort-Maßnahme: Sicherung, dann Neuverklebung |

**Kosten:** 150–500 EUR (Nachdichtung) bis 2.000–6.000 EUR (Neuverklebung)

### Problem 3: Scheibe vibriert / brummt bei bestimmter Drehzahl

**Symptom:** Resonanzgeräusch der Windschutzscheibe bei bestimmter Motordrehzahl oder Geschwindigkeit.

**Diagnose-Ablauf:**
1. Drehzahl-Bereich des Brummens eingrenzen (typisch: 1.800–2.400 U/min)
2. Prüfen ob Geräusch von Scheibe oder Rahmen kommt (Finger auf Scheibe legen)
3. Verklebungszustand prüfen — Scheibe darf sich nicht frei bewegen
4. Montagebolzen des Rahmens auf Festsitz prüfen

**Ursache & Lösung:**

| Befund | Ursache | Maßnahme |
|--------|---------|----------|
| Scheibe schwingt frei | Verklebung teilweise gelöst | Neuverklebung |
| Rahmen klappert | Lose Rahmenverschraubung | Bolzen nachziehen (Drehmoment lt. Werft) |
| Resonanz trotz fester Verklebung | Eigenfrequenz der Scheibe im Anregungsbereich | Schwingungsdämpfer (Butyl-Pads) auf Scheibe kleben |
| Geräusch nur bei Wind | Aerodynamische Anregung | Spoiler/Windabweiser montieren |

**Kosten:** 50–200 EUR (Dämpfer/Nachziehen) bis 1.500–4.000 EUR (Neuverklebung/Umbau)

### Problem 4: Wischer hinterlässt Kratzer auf neuer Scheibe

**Symptom:** Neue Scheibe zeigt nach wenigen Betriebsstunden feine Kratzer im Wischfeld.

**Diagnose-Ablauf:**
1. Wischergummi auf eingebettete Partikel prüfen (Lupe)
2. Wischerarm-Andruck messen (Federwaage: Soll 200–400 g/cm Wischblattlänge)
3. Scheibenbeschichtung prüfen (hydrophob? antistatisch?)
4. Waschwasser-Qualität prüfen (Sand, Salzkristalle?)

**Ursache & Lösung:**

| Befund | Ursache | Maßnahme |
|--------|---------|----------|
| Partikel im Gummi | Salzablagerung, Sand | Gummi reinigen oder tauschen, Scheibe vorwaschen |
| Andruck zu hoch | Federspannung falsch | Arm justieren oder tauschen |
| Andruck zu niedrig | Gummi springt und schleift | Arm justieren |
| Beschichtung empfindlich | Weiche Hydrophob-Beschichtung | Wischer nur mit Wassersprühung betreiben |

**Kosten:** 30–120 EUR (Gummi-Tausch) bis 200–500 EUR (Arm-Tausch + Justage)

### Problem 5: Elektrochromes Glas schaltet nicht mehr / fleckig

**Symptom:** Elektrochromes Glas verdunkelt sich nicht gleichmäßig, bleibt in Teilbereichen hell oder dunkel.

**Diagnose-Ablauf:**
1. Steuergerät prüfen: Spannung am Ausgang messen (Soll: 0,8–1,2 V DC im Schaltbetrieb)
2. Kontaktierung der Scheibe prüfen: Anschlussklemmen auf Korrosion
3. Temperatur beachten: Elektrochromes Glas schaltet langsam < 10 °C
4. Zyklen-Zähler abfragen (falls vorhanden)

**Ursache & Lösung:**

| Befund | Ursache | Maßnahme |
|--------|---------|----------|
| Keine Spannung am Glas | Steuergerät defekt oder Kabelbruch | Elektrik reparieren |
| Spannung vorhanden, keine Reaktion | EC-Schicht degradiert (>50.000 Zyklen) | Scheibentausch |
| Fleckige Schaltung | Lokale Delamination der EC-Schicht | Nicht reparabel, Scheibentausch |
| Sehr langsames Schalten | Niedrige Temperatur oder Alterung | Bei Kälte: normal; bei >15°C: Alterung → Tausch planen |

**Kosten:** 100–400 EUR (Elektrik) oder 5.000–15.000 EUR (EC-Scheibentausch)

---

## FAQ — Häufig gestellte Fragen

### WS-001: Welches Glas ist für Yacht-Windschutzscheiben am sichersten?
**Antwort:** Verbundsicherheitsglas (VSG) ist der Sicherheitsstandard für maritime Windschutzscheiben. Bei Bruch bleiben die Fragmente an der PVB-/SentryGlas-Folie haften, die Scheibe bleibt im Rahmen. ESG zerfällt in kleine stumpfe Stücke — sicherer als Float, aber die Öffnung ist sofort ungeschützt. Für CE-Kategorie A/B wird VSG empfohlen.
**Confidence:** `measured` (ISO 12216 / Herstellerangaben)

### WS-002: Wie dick muss meine Windschutzscheibe sein?
**Antwort:** Die Mindestdicke hängt von Scheibengröße, CE-Kategorie und Glastyp ab. Faustregel: 6–8 mm ESG für kleine Scheiben (< 0,25 m²) in CE-Kat C/D, 10–15 mm ESG oder 2×5–2×8 mm VSG für große Scheiben (> 0,5 m²) in CE-Kat A/B. Exakte Berechnung nach ISO 12216 — siehe Abschnitt "Technische Referenz".
**Confidence:** `calculated`

### WS-003: Kann ich eine ESG-Scheibe durch VSG ersetzen?
**Antwort:** Ja, grundsätzlich immer möglich und empfehlenswert. Beachten: VSG ist bei gleicher Festigkeit dicker und schwerer. Rahmen muss ggf. angepasst werden. Wischer-Andruck ggf. nachjustieren. Kosten: ca. 30–50% Aufpreis gegenüber ESG.
**Confidence:** `benchmark`

### WS-004: Wie oft müssen Scheibenwischer-Gummis getauscht werden?
**Antwort:** Alle 1–2 Saisons bei regelmäßiger Nutzung. Anzeichen für Wechsel: Schlieren, Quietschen, unvollständiges Wischbild. Wichtig: Wischer vor Saisonende reinigen und mit Glycerin-Tuch abwischen. Im Winterlager Wischerarm von Scheibe abheben.
**Confidence:** `benchmark`

### WS-005: Was kostet ein Windschutzscheiben-Austausch?
**Antwort:** Stark abhängig von Scheibengröße, Glastyp und Einbausituation. Richtwerte: Segelboot (35-Fuß, eine Scheibe): 800–2.000 EUR. Motoryacht (40-Fuß, Panorama): 3.000–8.000 EUR. Superyacht (20m+, gebogene VSG): 8.000–25.000+ EUR pro Scheibe. Montage jeweils 500–2.000 EUR zusätzlich.
**Confidence:** `estimated`

### WS-006: Darf ich Scheiben selbst verkleben?
**Antwort:** Technisch möglich, aber nur empfohlen für erfahrene Bootseigner mit geeignetem Werkzeug. Fehlerhafte Verklebung ist sicherheitskritisch — bei Seegang kann sich die Scheibe lösen. Für CE-zertifizierte Boote muss die Verklebung fachmännisch dokumentiert werden. Empfehlung: Verklebung durch zertifizierte Werft.
**Confidence:** `benchmark`

### WS-007: Was ist der Unterschied zwischen PVB und SentryGlas?
**Antwort:** PVB (Polyvinylbutyral) ist der Standard-Zwischenschichtfilm für VSG. SentryGlas (Kuraray/Trosifol) ist 5× steifer und 100× reißfester, UV-beständiger und weniger feuchtigkeitsempfindlich. Nachteil: ca. 40–60% teurer. Empfehlung: SentryGlas für alle Scheiben > 0,5 m² und CE-Kat A/B.
**Confidence:** `measured` (Herstellerdaten Kuraray)

### WS-008: Muss meine Windschutzscheibe einen CE-Stempel haben?
**Antwort:** Die Scheibe selbst braucht keinen CE-Stempel, aber sie muss den Anforderungen der CE-Zertifizierung des Bootes entsprechen (ISO 12216). Bei Austausch muss die neue Scheibe mindestens die gleiche Spezifikation erfüllen. Dokumentation (Glasdicke, Typ, Hersteller) für die CE-Akte aufbewahren.
**Confidence:** `measured` (EU-Richtlinie 2013/53/EU)

### WS-009: Wie reinige ich Yacht-Windschutzscheiben richtig?
**Antwort:** Süßwasser + mildes Reinigungsmittel (pH-neutral). Mikrofasertuch oder Fensterleder. Niemals: Scheuermittel, Küchenschwamm, Zeitungspapier. Salzablagerungen zuerst einweichen (5 min). Hydrophobe Beschichtung danach erneuern (Rain-X Marine oder Gtechniq Marine). Wischer nicht auf trockener Scheibe betreiben.
**Confidence:** `benchmark`

### WS-010: Kann ich eine gebogene Scheibe durch eine flache ersetzen?
**Antwort:** Nein, nicht empfohlen. Gebogene Scheiben sind aerodynamisch und strukturell in den Rumpf integriert. Eine flache Scheibe passt nicht in den vorhandenen Rahmen und verändert die Windlasten. Gebogene Ersatzscheiben müssen nach der Originalform gefertigt werden (Biegelehre oder 3D-Scan). Lieferzeit: 4–8 Wochen.
**Confidence:** `benchmark`

### WS-011: Wie funktioniert eine Scheibenheizung auf dem Boot?
**Antwort:** Zwei Systeme: 1) Heizdrähte (Wolfram, Ø 20–50 μm) in der VSG-Zwischenschicht — widerstandsbeheizt mit 12/24 V. 2) ITO-Beschichtung (Indium-Zinn-Oxid) als transparente Leitschicht auf der Glasoberfläche — gleichmäßigere Erwärmung aber empfindlicher gegen Wischerabrieb. Leistung: typisch 200–500 W/m².
**Confidence:** `measured`

### WS-012: Was bedeutet "Structural Glazing" genau?
**Antwort:** Die Scheibe wird direkt auf den Rumpf/Aufbau geklebt, ohne mechanischen Rahmen. Der Kleber (Sikaflex 295 UV oder vergleichbar) überträgt alle Lasten. Vorteile: flächenbündige Optik, weniger Gewicht, bessere Abdichtung. Nachteil: Austausch aufwändiger. Standard bei modernen Yachten ab ca. 2005.
**Confidence:** `measured`

### WS-013: Wie lange dauert ein Scheibenaustausch?
**Antwort:** Vorbereitung + Altscheibe entfernen: 2–4 h. Flanschreinigung + Primer: 2–3 h. Verklebung: 1–2 h. Aushärtung: 7 Tage (Boot nicht bewegen für 48–72 h). Gesamt: 1 Arbeitstag plus 7 Tage Aushärtung. Bei Superyachten: 2–3 Tage Arbeit plus Aushärtung.
**Confidence:** `benchmark`

### WS-014: Meine Scheibe hat einen kleinen Steinschlag — muss ich sie tauschen?
**Antwort:** Bei VSG: Steinschlagreparatur mit UV-Harz möglich, wenn Einschlag < 20 mm Durchmesser und > 100 mm vom Rand entfernt. Kosten: 150–350 EUR. Bei ESG: Keine Reparatur möglich, jeder Einschlag schwächt die gesamte Scheibe — Austausch nötig. Bei > 3 Reparaturen pro Scheibe: Austausch empfohlen.
**Confidence:** `benchmark`

### WS-015: Welchen Kleber soll ich für die Verklebung verwenden?
**Antwort:** Standard: Sikaflex 295 UV (1-K PU, UV-beständig, schwarz, Shore A 40). Alternative: Sikaflex 552 (schneller aushärtend) oder Dow 795 (Silikon, höhere UV-Beständigkeit aber geringere Festigkeit). Für DIY: Niemals Baumarkt-Silikon verwenden — nur zugelassene Marine-Kleber mit dokumentierter Haftung auf Glas und Substrat.
**Confidence:** `measured` (Sika Technical Data Sheets)

### WS-016: Kann ich eine Scheibenheizung nachrüsten?
**Antwort:** Ja, zwei Optionen: 1) Heizfolie auf Bestandsscheibe kleben (einfach, 200–500 EUR, Optik eingeschränkt). 2) Neue VSG-Scheibe mit integriertem Heizdraht fertigen lassen (1.500–4.000 EUR, optisch perfekt). Stromanschluss: 12/24 V, 15–30 A pro Scheibe. Kabelquerschnitt und Sicherung entsprechend dimensionieren.
**Confidence:** `benchmark`

### WS-017: Was ist der Vorteil einer hydrophoben Beschichtung?
**Antwort:** Wasser perlt bei > 30 kn ohne Wischer ab, verbesserte Nachtsicht (weniger Lichtbrechung durch Tropfen), leichtere Reinigung, reduzierter Wischerverschleiß. Haltbarkeit: Spray-Beschichtung 3–6 Monate, professionelle Nano-Beschichtung 2–3 Jahre. Kosten: 30–80 EUR (Spray) oder 200–500 EUR (professionell pro Scheibe).
**Confidence:** `benchmark`

### WS-018: Wie verhindere ich Beschlagen der Windschutzscheibe?
**Antwort:** Kombination aus: 1) Scheibenheizung (innenseitig), 2) Defogger-Gebläse (warme Luft auf Scheibe), 3) Belüftung (Querlüftung im Steuerhaus), 4) Anti-Beschlag-Spray (temporär, 2–4 Wochen wirksam). Bei Neubauten: Zwangsbelüftung am Scheibenfuß einplanen (Schlitzdüsen, 30–50 mm breit).
**Confidence:** `benchmark`

### WS-019: Meine Scheibe hat eine gelbliche Verfärbung — was tun?
**Antwort:** Wenn Verfärbung nicht abwischbar: PVB-Alterung (UV-Degradation). Irreversibel, nur Scheibentausch möglich. Prävention: SentryGlas oder UV-stabilisiertes PVB verwenden. Sonnenschutz (Persenning) bei Nichtgebrauch reduziert UV-Belastung um 80–90%.
**Confidence:** `visual_medium`

### WS-020: Kann ich Tönungsfolie auf die Windschutzscheibe kleben?
**Antwort:** Grundsätzlich ja, aber: 1) Lichttransmission muss ≥ 70% bleiben (Nachtfahrt, behördliche Vorschriften). 2) Folie nicht auf Scheibenheizung kleben (Blasenbildung). 3) Wischfeld freilassen oder wischerbeständige Folie verwenden. 4) Folie auf der Innenseite anbringen. Kosten: 100–400 EUR pro Scheibe.
**Confidence:** `benchmark`

### WS-021: Wie finde ich den richtigen Ersatzscheiben-Hersteller?
**Antwort:** Erstausrüster-Kontakt über die Werft (Beneteau → Saint-Gobain, Bavaria → Pilkington). Alternativ: spezialisierte Boots-Glaser (Maritim-Glas, Boatglass, Glasermeister mit Schiffserfahrung). Für gebogene Scheiben: Biegelehre oder Schablone vom Original anfertigen. Lieferzeit Standard: 2–4 Wochen, gebogen: 4–8 Wochen.
**Confidence:** `benchmark`

### WS-022: Was passiert bei einem Scheibenschaden auf See?
**Antwort:** Sofortmaßnahmen: 1) Öffnung mit stabiler Folie (Segeltuch, Plane) verschließen und mit Klebeband sichern. 2) Geschwindigkeit reduzieren, Seegang meiden. 3) Sicheren Hafen anlaufen. Notfall-Kit an Bord empfohlen: Folie 2 × 2 m, Panzer-Tape, Kabelbinder. Bei VSG-Scheibe: Scheibe bleibt im Rahmen, provisorische Reparatur oft nicht nötig.
**Confidence:** `benchmark`

### WS-023: Beeinflusst die Windschutzscheibe die Radarreflexion?
**Antwort:** Ja, metallbeschichtete Scheiben (Wärmeschutz, Scheibenheizung mit ITO) können Radarstrahlen reflektieren oder absorbieren. Bei ARPA/Radar-Mast hinter der Windschutzscheibe: Radar-transparentes Glas spezifizieren oder Radarantenne außerhalb des Scheibensektors positionieren. Heizdraht-Systeme beeinflussen Radar weniger als ITO-Beschichtungen.
**Confidence:** `benchmark`

### WS-024: Welche Garantie gibt es auf Yacht-Windschutzscheiben?
**Antwort:** Üblich: 2 Jahre Herstellergarantie auf Glasfehler (Blasen, Einschlüsse, Delamination). 5–10 Jahre auf Spontanbruch (bei HST-geprüftem ESG). Verklebung: 2–5 Jahre Werft-Garantie. Wischer: 1–2 Jahre. SentryGlas-Hersteller geben teils 10 Jahre auf Delaminationsfreiheit. Garantie erlischt bei unsachgemäßer Reinigung/Pflege.
**Confidence:** `benchmark`

### WS-025: Wie beeinflusst die Windschutzscheibe den Wiederverkaufswert?
**Antwort:** Erheblich. Trübe, verkratzte oder delaminierte Scheiben reduzieren den subjektiven Wert um 5.000–15.000 EUR bei Yachten > 40 Fuß. Neue Scheiben vor dem Verkauf amortisieren sich fast immer. AYDI-Score-Auswirkung: Emotional ±20 Punkte, Materials ±15 Punkte. Tipp: Scheibenzustand in Yacht-Survey immer dokumentieren lassen.
**Confidence:** `estimated`

---

## Glossar

| Nr. | Begriff | Definition |
|-----|---------|------------|
| 1 | **Anlauffarben** | Verfärbung von Edelstahl durch Überhitzung beim Schweißen — Indikator für beschädigte Passivschicht |
| 2 | **Autoklave** | Druckbehälter zum Laminieren von VSG unter Hitze (120–140 °C) und Druck (10–14 bar) |
| 3 | **Biegelehre** | Metallform, über die Flachglas bei 600–700 °C gebogen wird, um die gewünschte Krümmung zu erhalten |
| 4 | **Butyl** | Synthetischer Kautschuk, verwendet als Vorverklebung und Dampfsperre in der Isolierglasproduktion |
| 5 | **CE-Kategorie** | Einteilung (A–D) nach EU-Richtlinie 2013/53/EU für den Seebereich, in dem ein Boot betrieben werden darf |
| 6 | **Defogger** | System zur Entfeuchtung der Scheibeninnenseite durch Warmluft oder Heizung |
| 7 | **Distanzklotz** | Abstandshalter (PE, Silikon, 6–12 mm) zwischen Glas und Rahmen zur Einhaltung der Klebefugendicke |
| 8 | **Doppelkrümmung** | Scheibe mit Biegung in zwei Achsen gleichzeitig (Sphärisch) — aufwändigste Fertigungsform |
| 9 | **Dreiecksdüse** | Kartuschenaufsatz, der eine dreieckige Kleberraupe formt für optimale Fugenform |
| 10 | **EPDM** | Ethylen-Propylen-Dien-Monomer — Dichtungsgummi mit guter UV- und Ozonbeständigkeit |
| 11 | **ESG** | Einscheibensicherheitsglas — thermisch vorgespanntes Glas, zerfällt bei Bruch in kleine stumpfe Krümel |
| 12 | **Flash-off-Zeit** | Mindest-Wartezeit nach Primer-Auftrag, bis Lösemittel vollständig verdampft ist |
| 13 | **Float-Glas** | Standard-Flachglas, auf flüssigem Zinn hergestellt — Ausgangsmaterial für ESG und VSG |
| 14 | **Formfaktor (k)** | Dimensionsloser Faktor in der Glasdickenberechnung, abhängig vom Seitenverhältnis der Scheibe |
| 15 | **Galvanische Korrosion** | Elektrochemische Korrosion bei Kontakt unterschiedlicher Metalle in Salzwasser-Umgebung |
| 16 | **Heat-Soak-Test (HST)** | Prüfverfahren (EN 14179) zur Reduzierung des Spontanbruchrisikos bei ESG durch NiS-Einschlüsse |
| 17 | **Hydrophobe Beschichtung** | Wasserabweisende Oberflächenbehandlung (Nano-Beschichtung), Kontaktwinkel > 110° |
| 18 | **ISO 12216** | Internationale Norm für Fenster, Bullaugen, Luken und Lichtschächte auf Wasserfahrzeugen |
| 19 | **ITO-Beschichtung** | Indium-Zinn-Oxid — transparente, elektrisch leitfähige Schicht für Scheibenheizung oder Sonnenschutz |
| 20 | **Kantenversiegelung** | Versiegelung der VSG-Glaskante zum Schutz der PVB-Zwischenschicht vor Feuchtigkeitseintritt |
| 21 | **Klebefugenbreite** | Breite der strukturellen Verklebung zwischen Glas und Rahmen/Rumpf (typisch 15–45 mm) |
| 22 | **Klebefugendicke** | Dicke der Kleberschicht (typisch 6–12 mm, optimal 8–10 mm) |
| 23 | **Kompaktwischer** | Kurzer, einteiliger Scheibenwischer ohne Parallelogrammführung — für kleine Scheiben |
| 24 | **Krümelbruch** | Bruchmuster von ESG — Scheibe zerfällt in viele kleine, stumpfkantige Fragmente |
| 25 | **Laminierung** | Verbindung von zwei oder mehr Glasscheiben mit Zwischenschicht (PVB, SentryGlas) unter Hitze und Druck |
| 26 | **Nickel-Sulfid-Einschluss (NiS)** | Mikroskopische Verunreinigung im Float-Glas, kann Spontanbruch bei ESG verursachen |
| 27 | **Pantograph-Wischer** | Parallelogramm-Scheibenwischer, der das Wischblatt parallel zur Scheibe führt — größeres Wischfeld |
| 28 | **Pendelwischer** | Standard-Scheibenwischer mit kreissegmentförmigem Wischfeld |
| 29 | **Polysulfid** | Elastischer Dichtstoff für Kantenversiegelung von VSG — hohe Feuchtigkeitssperre |
| 30 | **Primer** | Haftvermittler, der vor dem Kleber auf Substrat (Glas, Metall, GFK) aufgetragen wird |
| 31 | **PVB** | Polyvinylbutyral — Standard-Zwischenschichtfolie für VSG, 0,38 oder 0,76 mm Dicke |
| 32 | **R-Wert** | Biegeradius einer gebogenen Scheibe (mm) — kleinerer R = stärkere Krümmung |
| 33 | **Scheibenwascheranlage** | Pumpe + Düsen + Tank zur Reinigung der Windschutzscheibe während der Fahrt |
| 34 | **SentryGlas** | Hochleistungs-Zwischenschichtfolie (Kuraray/Trosifol) — steifer, reißfester und UV-beständiger als PVB |
| 35 | **Shore-Härte** | Maß für die Härte von Elastomeren (Kleber, Dichtungen) — Shore A 30–50 typisch für Marine-Kleber |
| 36 | **Siebdruck (Keramikrand)** | Aufgebrannter, opaker Keramikrand auf Glasscheiben, schützt Kleber vor UV und verdeckt Klebefuge |
| 37 | **Structural Glazing** | Rahmenloses Einbauverfahren, bei dem die Scheibe direkt auf den Aufbau geklebt wird |
| 38 | **Thermische Vorspannung** | Verfahren zur Herstellung von ESG: Glas auf 620–680 °C erhitzt, dann schnell abgekühlt |
| 39 | **TVG** | Teilvorgespanntes Glas — zwischen Float und ESG, bricht in größere Stücke als ESG |
| 40 | **Vorspannung** | Eigenspannung im Glas durch thermische oder chemische Behandlung — erhöht die Biegefestigkeit |
| 41 | **VSG** | Verbundsicherheitsglas — zwei oder mehr Glasscheiben mit PVB/SentryGlas-Zwischenschicht |
| 42 | **Wischerfeld** | Fläche der Scheibe, die vom Wischblatt erreicht wird — Soll: ≥ 75–85% der Scheibenfläche |

---

## Schnell-Referenz

### Entscheidungsbaum: Glastyp-Auswahl

```
Neubau oder Ersatz?
├── CE-Kat A/B (Ozean/Offshore)?
│   ├── Scheibenfläche > 0,5 m² → VSG mit SentryGlas + Heizung
│   ├── Scheibenfläche 0,25–0,5 m² → VSG mit PVB oder ESG (HST)
│   └── Scheibenfläche < 0,25 m² → ESG (HST) ausreichend
├── CE-Kat C/D (Küste/Binnen)?
│   ├── Scheibenfläche > 0,5 m² → VSG mit PVB
│   ├── Scheibenfläche 0,25–0,5 m² → ESG (HST empfohlen)
│   └── Scheibenfläche < 0,25 m² → ESG Standard
└── Superyacht (> 24m)?
    └── Immer VSG mit SentryGlas + HST + Heizung + hydrophobe Beschichtung
```

### Checkliste: Scheibenaustausch

- [ ] Scheibengröße exakt vermessen (± 1 mm)
- [ ] Glastyp und -dicke nach ISO 12216 bestimmen
- [ ] Biegeform vorhanden? (bei gebogenen Scheiben)
- [ ] Rahmenzustand prüfen (Korrosion, Verformung)
- [ ] Richtige Primer + Kleber beschaffen (Substrat-kompatibel)
- [ ] Wetterfenster: 7 Tage ohne Regen/Sturm nach Verklebung
- [ ] Saugheber vorhanden (Tragkraft ≥ 1,5× Scheibengewicht)
- [ ] Schutzausrüstung: Handschuhe, Brille, Belüftung
- [ ] Abnahme dokumentieren: Foto, Klebercharge, Datum
- [ ] Wassertest nach 7 Tagen

### Kosten-Schnellübersicht (EUR)

| Position | Segelboot 35' | Motoryacht 42' | Motoryacht 55' | Superyacht 24m+ |
|----------|--------------|----------------|----------------|-----------------|
| ESG-Scheibe (1 Stk.) | 300–800 | 500–1.500 | 800–2.500 | 1.500–5.000 |
| VSG-Scheibe (1 Stk.) | 500–1.200 | 800–2.500 | 1.200–4.000 | 2.500–10.000 |
| VSG + SentryGlas (1 Stk.) | 700–1.800 | 1.200–3.500 | 1.800–6.000 | 4.000–15.000 |
| Montage (Verklebung) | 500–1.000 | 800–1.500 | 1.000–2.500 | 2.000–5.000 |
| Wischersystem komplett | 300–800 | 500–1.500 | 800–3.000 | 2.000–8.000 |
| Scheibenheizung | 400–1.000 | 600–1.800 | 1.000–3.000 | 2.000–8.000 |

---

## Notfall-Ressourcen

### Notfall-Kontakte für Scheibenprobleme auf See

| Situation | Maßnahme | Kontakt |
|-----------|----------|---------|
| Totalbruch auf See | Öffnung abdichten, Hafen anlaufen | MRCC/Küstenwache (UKW Kanal 16) |
| Leckage bei Sturm | Innen abdichten, Kurs ändern | — |
| Scheibe lose | Geschwindigkeit reduzieren, sichern | Nächste Werft per Funk/Telefon |

### Notfall-Reparatur-Kit (empfohlener Bordvorrat)

| Material | Menge | Kosten (EUR) |
|----------|-------|--------------|
| Folie (PVC, 0,5 mm, transparent) | 2 × 2 m | 15–25 |
| Panzer-Tape (wasserfest) | 2 Rollen à 50 m | 15–25 |
| Kabelbinder 300 mm | 20 Stück | 5–10 |
| Sikaflex 291i (Dichtmasse) | 1 Kartusche 300 ml | 15–25 |
| Handkartuschenpistole | 1 Stück | 10–20 |
| Schutzbrille + Handschuhe | je 1 | 10–15 |
| **Gesamt** | — | **70–120** |

### Wichtige Hersteller-Hotlines

| Hersteller | Produkt | Telefon / Web |
|------------|---------|---------------|
| Sika Deutschland | Kleber, Primer | +49 711 8009-0 / sika.de |
| Exalto (Vetus) | Wischersysteme | +31 78 618 8100 / vetus.com |
| Saint-Gobain Sekurit | Marine-Glas | +49 241 516-0 / saint-gobain-sekurit.com |
| Pilkington Marine | Marine-Glas | +44 1744 692000 / pilkington.com |
| Hella Marine | Wischermotoren | +64 9 415 8294 / hellamarine.com |
| Lewmar | Wischer + Luken | +44 145 253 3700 / lewmar.com |

---

## ANHANG A: Normen und Regelwerke — Vollständige Referenzliste

| Norm | Titel | Relevanz für Windschutzscheiben |
|------|-------|-------------------------------|
| ISO 12216:2020 | Fenster, Bullaugen, Luken, Deckel — Festigkeitsanforderungen | Glasdicke, Rahmenbelastung, Prüfverfahren |
| ISO 12217-1:2022 | Stabilitätsbewertung — Teil 1: Nicht-Segelboote | Gewichtsverteilung durch Verglasung |
| ISO 12217-2:2022 | Stabilitätsbewertung — Teil 2: Segelboote | dto. |
| ISO 11812:2020 | Cockpits — Wasserdichtheit | Übergangsbereich Scheibe/Cockpit |
| ISO 9094:2015 | Brandschutz | Brandverhalten Glastyp, Fluchtweg durch Scheibe |
| ISO 15085:2003 | Mann-über-Bord-Schutz | Scheibenanordnung als Absturzsicherung |
| EN 12150 | Thermisch vorgespanntes ESG | Herstellungs- und Prüfstandard |
| EN 14449 | Verbundsicherheitsglas (VSG) | Herstellungs- und Prüfstandard |
| EN 14179 | Heat-Soak-Test für ESG | Prüfverfahren NiS-Spontanbruch |
| EN 572 | Basisglaserzeugnisse (Float) | Ausgangsmaterial-Spezifikation |
| EU 2013/53/EU | Sportboot-Richtlinie | CE-Zertifizierung, Design-Kategorien |

## ANHANG B: Kleber-Vergleichsmatrix

| Eigenschaft | Sikaflex 295 UV | Sikaflex 252 | Sikaflex 552 | Dow 795 | Dow 983 |
|-------------|----------------|--------------|--------------|---------|---------|
| Basis | 1-K PU | 1-K PU | 1-K PU | Silikon | Silikon |
| Farbe | Schwarz | Schwarz/Weiß | Schwarz | Versch. | Schwarz |
| Shore A (ausgehärtet) | 40 | 40 | 50 | 25 | 35 |
| Zugfestigkeit (MPa) | 2,0 | 3,0 | 6,0 | 1,4 | 2,0 |
| Bruchdehnung (%) | 400 | 350 | 250 | 500 | 400 |
| UV-Beständigkeit | Sehr gut | Gut | Gut | Hervorragend | Hervorragend |
| Hautbildung (min) | 45–90 | 30–60 | 20–40 | 15–30 | 15–30 |
| Durchhärtung (mm/24h) | 3–4 | 3–4 | 4–5 | 2–3 | 3–4 |
| Temperaturbereich (°C) | -40 bis +90 | -40 bis +100 | -40 bis +100 | -50 bis +150 | -50 bis +150 |
| Haupteinsatz | Marine-Standard | Universal | Schnellverklebung | Marine-Dichtung | Structural Glazing |

## ANHANG C: Glasgewicht-Tabelle

| Glastyp | Dicke (mm) | Gewicht (kg/m²) |
|---------|-----------|-----------------|
| ESG | 5 | 12,5 |
| ESG | 6 | 15,0 |
| ESG | 8 | 20,0 |
| ESG | 10 | 25,0 |
| ESG | 12 | 30,0 |
| ESG | 15 | 37,5 |
| ESG | 19 | 47,5 |
| VSG 2×4 (8,76) | 8,76 | 21,9 |
| VSG 2×5 (10,76) | 10,76 | 26,9 |
| VSG 2×6 (12,76) | 12,76 | 31,9 |
| VSG 2×8 (16,76) | 16,76 | 41,9 |
| VSG 2×10 (20,76) | 20,76 | 51,9 |

> Glasdichte: 2,5 kg/dm³. PVB-Folie (0,76 mm) ≈ 0,8 kg/m². Gewicht gerundet.

## ANHANG D: Wischer-Spezifikationstabelle

| Modell | Typ | Wischblatt (mm) | Drehmoment (Nm) | Strom 12V (A) | Schutzart | Preis (EUR) |
|--------|-----|----------------|-----------------|---------------|-----------|-------------|
| Exalto HD 215 | Pendel | 280–510 | 6 | 3–5 | IP65 | 250–400 |
| Exalto 1700 | Pantograph | 400–750 | 10 | 5–8 | IP67 | 500–900 |
| Exalto 1800 | Pantograph | 500–900 | 15 | 8–12 | IP67 | 800–1.400 |
| Roca W25 | Pendel | 300–500 | 5 | 3–5 | IP55 | 150–300 |
| Roca W38 | Pantograph | 400–650 | 8 | 5–8 | IP65 | 400–700 |
| Hella Marine HMD | Pendel | 250–450 | 4 | 2–4 | IP56 | 200–350 |
| Lewmar Omega | Pantograph | 350–600 | 8 | 4–7 | IP67 | 450–800 |
| Speich S.200 | Pantograph | 500–1000 | 20 | 10–15 | IP68 | 1.200–2.500 |

## ANHANG E: Primer-Kompatibilitätsmatrix

| Substrat | Primer Glas-Seite | Primer Substrat-Seite | Aktivator |
|----------|-------------------|----------------------|-----------|
| Aluminium (blank) | Sika Primer 210 T | Sika Primer 209 D | Sika Aktivator 205 |
| Aluminium (pulverbeschichtet) | Sika Primer 210 T | Sika Primer 206 G+P | Sika Aktivator 205 |
| GFK/Gelcoat | Sika Primer 210 T | Sika Primer 206 G+P | Sika Aktivator 205 |
| Edelstahl 316L | Sika Primer 210 T | Sika Primer 206 G+P | Sika Aktivator 205 |
| Carbon/CFK | Sika Primer 210 T | Sika Primer 206 G+P | Sika Aktivator 100 |
| Lackiertes Holz | Sika Primer 210 T | Sika Primer 206 G+P | Sika Aktivator 205 |
| Teak (unbehandelt) | — | Nicht empfohlen (Öl) | — |

> **Hinweis:** Vor jeder Verklebung Haftungstest (Cross-Cut + Peel-Test) am tatsächlichen Substrat durchführen.

## ANHANG F: Fallstudien

### Fallstudie 1: Spontanbruch Frontscheibe — Bavaria 40 Cruiser (2018)

- **Yacht:** Bavaria 40 Cruiser, Baujahr 2014, Mittelmeer (Griechenland)
- **Vorfall:** Spontanbruch der ESG-Frontscheibe bei Hafenliegen, keine äußere Einwirkung
- **Ursache:** Nickel-Sulfid-Einschluss (NiS), bestätigt durch Bruchbild-Analyse
- **Folge:** Scheibe zerbröselt, Cockpit offen, kein Personenschaden (Boot war unbesetzt)
- **Maßnahme:** Notabdichtung durch Marina, Ersatzscheibe VSG (2×5 mm) mit HST-Prüfung
- **Kosten:** 2.400 EUR (Scheibe) + 900 EUR (Montage) + 350 EUR (Notmaßnahme) = 3.650 EUR
- **Dauer:** 6 Wochen Lieferzeit für gebogene VSG-Scheibe
- **Lehre:** ESG ohne HST-Prüfung vermeiden, VSG als Standard empfehlen
- **AYDI-Bewertung:** Structural 25/100, Materials 30/100, Compliance 40/100
- **Confidence:** `documented`
- **Relevanz für Analyse:** Bootsklasse Production Sailboat — Risikofaktor ESG ohne HST

### Fallstudie 2: Delamination Panorama-Windschutzscheibe — Princess V58 (2020)

- **Yacht:** Princess V58, Baujahr 2011, Karibik (BVI, ganzjährig)
- **Vorfall:** Fortschreitende PVB-Delamination an allen 5 Frontscheiben (VSG 2×6 mm)
- **Ursache:** Fehlende Kantenversiegelung ab Werk, tropische Feuchtigkeit (>80% rH), hohe UV-Belastung
- **Folge:** Trübung 15–40 mm vom Rand, Sichtbehinderung, ästhetisch inakzeptabel
- **Maßnahme:** Alle 5 Scheiben durch VSG mit SentryGlas und Polysulfid-Kantenversiegelung ersetzt
- **Kosten:** 5 × 3.200 EUR (Scheiben) + 4.500 EUR (Montage) = 20.500 EUR
- **Dauer:** 8 Wochen (Lieferung ab UK, Montage 4 Tage)
- **Lehre:** In tropischen Revieren: SentryGlas + Kantenversiegelung zwingend spezifizieren
- **AYDI-Bewertung:** Materials 35/100, Emotional 30/100, Service_patterns 40/100
- **Confidence:** `documented`
- **Relevanz für Analyse:** Semi-Custom Motoryacht — PVB ungeeignet für tropische Dauerliegeplätze

### Fallstudie 3: Verklebungsversagen bei Hochgeschwindigkeit — Fairline Targa 43 (2019)

- **Yacht:** Fairline Targa 43, Baujahr 2016, Nordsee (NL)
- **Vorfall:** Frontscheibe löste sich bei 32 kn Fahrt in Welle teilweise vom Rahmen
- **Ursache:** DIY-Nachverklebung mit falschem Primer (Silikonbasis statt PU-kompatibel)
- **Folge:** Scheibe kippte nach innen, Wassereinbruch, Steuermann leicht verletzt (Schnittwunde)
- **Maßnahme:** Professionelle Neuverklebung durch Werft, Primer-Kompatibilität getestet
- **Kosten:** 1.800 EUR (Neuverklebung) + 400 EUR (Primer/Kleber) = 2.200 EUR
- **Dauer:** 2 Tage Arbeit + 7 Tage Aushärtung
- **Lehre:** DIY-Verklebung nur mit korrekter Primer-Kombination, Substrat-Test vorher durchführen
- **AYDI-Bewertung:** Structural 15/100, Compliance 20/100, Safety KRITISCH
- **Confidence:** `documented`
- **Relevanz für Analyse:** Semi-Custom Motoryacht — Primer-Inkompatibilität als häufiger Fehler

### Fallstudie 4: Scheibenheizung Totalausfall — Hallberg-Rassy 412 (2021)

- **Yacht:** Hallberg-Rassy 412, Baujahr 2008, Nordsee/Ostsee
- **Vorfall:** Scheibenheizung fällt komplett aus bei Novemberfahrt — Scheibe beschlägt permanent
- **Ursache:** Korrosion der Heizdraht-Anschlussklemmen unter der Rahmendichtung
- **Folge:** Kein Personenschaden, aber stark eingeschränkte Sicht bei 4 °C und Nebel
- **Maßnahme:** Anschlussklemmen freigelegt, gereinigt, mit Marine-Steckern neu angeschlossen
- **Kosten:** 350 EUR (Arbeit) + 80 EUR (Material) = 430 EUR
- **Dauer:** 4 Stunden
- **Lehre:** Heizungs-Anschlussklemmen bei jährlicher Wartung auf Korrosion prüfen
- **AYDI-Bewertung:** Ergonomics 55/100 (Sicht eingeschränkt), Service_patterns 60/100
- **Confidence:** `documented`
- **Relevanz für Analyse:** Production Sailboat — Heizungsanschlüsse als Schwachstelle bei Nordeuroparevieren

### Fallstudie 5: Wischer-Kratzer auf Neuscheibe — Azimut 55 (2022)

- **Yacht:** Azimut 55, Baujahr 2020, Adria (Kroatien)
- **Vorfall:** Neue Frontscheibe (12.000 EUR) nach 3 Monaten mit Kratzspuren im Wischfeld
- **Ursache:** Wischer auf trockener, sandbelegter Scheibe bei Bora-Wind betrieben
- **Folge:** Parallele Kratzer im Fahrersichtfeld, Blendung bei Gegenlicht
- **Maßnahme:** Cerium-Oxid-Politur (teilweise Verbesserung), Schutzfolien-Auftrag
- **Kosten:** 450 EUR (Politur + Folie), Scheibenwert gemindert
- **Dauer:** 1 Tag
- **Lehre:** Wischer niemals auf trockener Scheibe betreiben, Waschanlage immer vorsprühen
- **AYDI-Bewertung:** Emotional 45/100, Ergonomics 60/100 (Blendung)
- **Confidence:** `documented`
- **Relevanz für Analyse:** Semi-Custom Motoryacht — Bedienungsfehler als häufigste Ursache für Kratzer

### Fallstudie 6: Elektrochromes Glas — Fleckenbildung — Sunseeker 76 Yacht (2023)

- **Yacht:** Sunseeker 76 Yacht, Baujahr 2019, Côte d'Azur
- **Vorfall:** Elektrochromes Panorama-Glas (Owner-Deck) schaltet fleckig nach 4 Jahren
- **Ursache:** Lokale Delamination der EC-Schicht durch thermische Zyklen (Sonneneinstrahlung + Klimaanlage)
- **Folge:** Ungleichmäßige Tönung, einige Bereiche bleiben permanent dunkel
- **Maßnahme:** Alle 3 EC-Scheiben getauscht (Sage Glass, neue Generation)
- **Kosten:** 3 × 14.000 EUR (Scheiben) + 8.000 EUR (Montage) = 50.000 EUR
- **Dauer:** 12 Wochen Lieferung, 1 Woche Montage
- **Lehre:** EC-Glas-Garantiebedingungen prüfen, thermische Belastung durch Sonnenschutz reduzieren
- **AYDI-Bewertung:** Materials 30/100, Emotional 25/100, Cost 20/100
- **Confidence:** `documented`
- **Relevanz für Analyse:** Superyacht — EC-Glas als Premiumfeature mit hohem Ausfallrisiko

### Fallstudie 7: Panoramascheibe — Rahmenkorrosion — Beneteau Oceanis 51.1 (2022)

- **Yacht:** Beneteau Oceanis 51.1, Baujahr 2017, Ostsee
- **Vorfall:** Weiße Korrosionsflecken auf dem Aluminium-Scheibenrahmen, Dichtungsverlust
- **Ursache:** Galvanische Korrosion: Edelstahl-Schrauben ohne EPDM-Unterlegscheiben im Alu-Rahmen
- **Folge:** Wassereinbruch bei Regen, Polsterschäden am Kartentisch
- **Maßnahme:** Rahmen demontiert, sandgestrahlt, pulverbeschichtet, EPDM-Isolation, Neuverklebung
- **Kosten:** 4.200 EUR (Gesamtpaket inkl. Neuverklebung der Scheibe)
- **Dauer:** 2 Wochen (Rahmen-Aufarbeitung in Werkstatt + Einbau)
- **Lehre:** Galvanische Trennung zwischen Alu und Edelstahl immer sicherstellen
- **AYDI-Bewertung:** Materials 40/100, Structural 50/100, Compliance 55/100
- **Confidence:** `documented`
- **Relevanz für Analyse:** Production Sailboat — Galvanische Korrosion als systematisches Problem bei Serienbooten

### Fallstudie 8: Notfall-Scheibenverlust auf See — Contest 50CS (2021)

- **Yacht:** Contest 50CS, Baujahr 2015, Biskaya-Überquerung
- **Vorfall:** Frontwelle bei Bf 8 trifft Frontscheibe, ESG zerspringt (keine NiS — mechanischer Impact)
- **Ursache:** Schäkel der Genua löste sich bei Patenthalse und traf Scheibe
- **Folge:** Öffnung 800 × 500 mm, massiver Wassereinbruch ins Steuerhaus
- **Maßnahme:** Sofort: Segeltuch + Panzer-Tape + Schraubzwingen. Nächster Hafen: La Coruña (18 h Fahrt)
- **Kosten:** Notmaßnahme 150 EUR + Ersatzscheibe VSG 2.800 EUR + Montage 1.200 EUR = 4.150 EUR
- **Dauer:** Notmaßnahme 30 min, Ersatzscheibe 4 Wochen Lieferzeit vor Ort
- **Lehre:** 1) Notfall-Kit immer an Bord. 2) VSG statt ESG für Hochsee. 3) Schäkel sichern (Mousings)
- **AYDI-Bewertung:** Structural 20/100, Compliance 30/100, Safety KRITISCH
- **Confidence:** `documented`
- **Relevanz für Analyse:** Semi-Custom Sailboat — ESG-Einsatz bei Hochsee-Yachten kritisch hinterfragen

## ANHANG G: Reinigungsmittel-Kompatibilität

| Reinigungsmittel | ESG | VSG | ITO-Heizung | Hydrophobe Beschichtung | Rahmen (Alu) | Rahmen (Edelstahl) |
|------------------|-----|-----|-------------|--------------------------|--------------|-------------------|
| Süßwasser + Spülmittel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Essigwasser (5%) | ✓ | ✓ | ✓ | ⚠ (löst Beschichtung) | ✓ | ✓ |
| Isopropanol (IPA) | ✓ | ✓ | ✓ | ✗ (entfernt Beschichtung) | ✓ | ✓ |
| Aceton | ✓ | ⚠ (PVB-Kante!) | ✓ | ✗ | ⚠ (Lack!) | ✓ |
| Scheuermilch | ✗ (Kratzer) | ✗ | ✗ | ✗ | ✗ | ⚠ |
| Salzsäure | ✗ | ✗ | ✗ | ✗ | ✗ (Korrosion!) | ✗ |
| Marine-Glasreiniger | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Rain-X / Nano-Versiegelung | ✓ | ✓ | ⚠ (nicht auf ITO-Seite) | — (ist Ersatz) | — | — |

> ✓ = unbedenklich, ⚠ = eingeschränkt/vorsichtig, ✗ = nicht verwenden

## ANHANG H: Temperatur-Einsatzbereiche

| Komponente | Min (°C) | Max (°C) | Kritisch |
|------------|----------|----------|----------|
| ESG-Scheibe | -60 | +300 | Thermischer Schock > 150 °C Differenz |
| VSG (PVB) | -40 | +70 | PVB wird weich > 70 °C (Trübung) |
| VSG (SentryGlas) | -40 | +80 | Steifer als PVB bei Hitze |
| Sikaflex 295 UV | -40 | +90 | Dauerhaft max. 90 °C |
| Dow 795 (Silikon) | -50 | +150 | Höchste Temperaturbeständigkeit |
| EPDM-Dichtung | -50 | +120 | Gute Temperaturbeständigkeit |
| Wischermotor | -20 | +60 | Motorschutz bei Überhitzung |
| ITO-Beschichtung | -40 | +200 | Stabil, Degradation nur mechanisch |
| Elektrochromes Glas | -10 | +60 | Schaltet langsam < 0 °C |

## ANHANG I: Checkliste jährliche Scheibeninspektion

1. [ ] Glasoberfläche: Kratzer, Chips, Risse?
2. [ ] Klebefuge: Risse, Ablösung, Verfärbung?
3. [ ] Rahmenzustand: Korrosion, Verformung, lose Bolzen?
4. [ ] Dichtungen: Risse, Verhärtung, Ablösung?
5. [ ] Wischergummi: Schlieren-Test durchführen
6. [ ] Wischerarm: Andruck prüfen (Federwaage)
7. [ ] Wischermotor: Geschwindigkeitsstufen, Parkposition
8. [ ] Scheibenheizung: Funktionstest, gleichmäßige Erwärmung
9. [ ] Defogger: Luftstrom an Scheibenfuß prüfen
10. [ ] Waschanlage: Düsen, Pumpe, Tankfüllstand
11. [ ] Wassertest: Schlauch 15 min bei 2 bar, Leckage innen prüfen
12. [ ] Dokumentation: Befunde, Fotos, Datum, nächster Termin

## ANHANG J: Maßeinheiten und Umrechnungen

| Von | Nach | Faktor |
|-----|------|--------|
| Zoll (inch) | mm | × 25,4 |
| Fuß (feet) | mm | × 304,8 |
| PSI | kPa | × 6,895 |
| bar | kPa | × 100 |
| kn (Knoten) | m/s | × 0,5144 |
| Beaufort | kn (Mittel) | Tabelle (Bf4=16kn, Bf6=27kn, Bf8=40kn) |
| °F | °C | (°F - 32) × 5/9 |
| lb/ft² | kg/m² | × 4,882 |

## ANHANG K: Abkürzungsverzeichnis

| Abkürzung | Bedeutung |
|-----------|-----------|
| BF | Beaufort (Windstärke) |
| CE | Conformité Européenne |
| CFK | Carbonfaserverstärkter Kunststoff |
| EC | Elektrochrom |
| EPDM | Ethylen-Propylen-Dien-Monomer |
| ESG | Einscheibensicherheitsglas |
| GFK | Glasfaserverstärkter Kunststoff |
| HST | Heat-Soak-Test |
| IPA | Isopropylalkohol |
| ISO | International Organization for Standardization |
| ITO | Indium-Zinn-Oxid |
| NiS | Nickel-Sulfid |
| PE | Polyethylen |
| PU | Polyurethan |
| PVB | Polyvinylbutyral |
| TVG | Teilvorgespanntes Glas |
| UV | Ultraviolett |
| VSG | Verbundsicherheitsglas |
| WS | Windschutzscheibe |

## ANHANG L: AYDI-Bewertungsmatrix für Windschutzscheiben

| Kriterium | Gewichtung | Score 90–100 | Score 60–89 | Score 30–59 | Score 0–29 |
|-----------|-----------|-------------|-------------|-------------|------------|
| Glastyp | 15% | VSG + SentryGlas + HST | VSG + PVB | ESG mit HST | ESG ohne HST / Float |
| Glasdicke (vs. ISO) | 20% | ≥ 120% der Norm | 100–119% | 80–99% | < 80% |
| Verklebung | 20% | Structural Glazing, < 5 Jahre | SG, 5–15 Jahre, intakt | SG > 15 Jahre oder Gummi | Beschädigt / lose |
| Wischersystem | 10% | Pantograph, ≥ 80% Feld | Pendel, ≥ 80% | Pendel, < 80% | Defekt / fehlend |
| Scheibenheizung | 10% | ITO oder Heizdraht, funktionstüchtig | Vorhanden, Teilausfall | Nachrüstfolie | Keine / defekt |
| Zustand Oberfläche | 15% | Kratzer-/rissfrei | Leichte Kratzer | Sichtbare Kratzer/Chips | Risse / Delamination |
| Rahmenzustand | 10% | Korrosionsfrei, dicht | Leichte Korrosion | Fortgeschrittene Korrosion | Strukturell geschwächt |

## ANHANG M: Lieferzeiten-Übersicht

| Scheibentyp | Standard (Wochen) | Express (Wochen) | Aufpreis Express |
|-------------|-------------------|-------------------|-----------------|
| ESG flach | 1–2 | 3–5 Tage | +30–50% |
| ESG gebogen | 3–5 | 1–2 | +50–80% |
| VSG flach | 2–3 | 1 | +30–50% |
| VSG gebogen | 4–6 | 2–3 | +50–80% |
| VSG + SentryGlas | 4–8 | 2–4 | +40–60% |
| VSG + SentryGlas gebogen | 6–10 | 3–5 | +50–80% |
| EC-Glas | 10–16 | 6–8 | +60–100% |

## ANHANG N: Versicherungsrelevante Informationen

- Windschutzscheiben-Schäden fallen unter Kaskoversicherung (Voll- oder Teilkasko)
- Selbstbeteiligung: typisch 500–2.500 EUR (je nach Police)
- Steinschlag-Reparatur (< 20 mm): oft ohne Selbstbeteiligung abgedeckt
- Spontanbruch (NiS): als versicherter Sachschaden anerkannt
- Verklebungsverlust durch Alterung: meist nicht versichert (Verschleiß)
- Dokumentation erforderlich: Fotos, Schadensbericht, Werft-Rechnung
- Bei Totalschaden auf See: Havarier-Kommissar einschalten (bei Wert > 5.000 EUR)

## ANHANG O: Umwelt- und Entsorgungshinweise

| Material | Entsorgung | Hinweis |
|----------|-----------|---------|
| ESG-Bruchstücke | Altglas (weiß) oder Bauschutt | Nicht über Hausmüll |
| VSG-Scheibe | Sondermüll (PVB-Folie) | Spezialisierter Entsorger |
| PU-Kleber (ausgehärtet) | Restmüll | Nicht wassergefährdend nach Aushärtung |
| PU-Kleber (flüssig) | Sondermüll | Wassergefährdend, nicht in Gewässer |
| Primer / Aktivator | Sondermüll | Lösemittelhaltig, Altlösemittel-Sammlung |
| EPDM-Dichtungen | Restmüll oder Gummi-Recycling | — |
| ITO-beschichtetes Glas | Sondermüll (Indium-Rückgewinnung) | Wertvoller Rohstoff |

## ANHANG P: Saisonale Pflege-Empfehlungen

### Frühjahrsinbetriebnahme (März–April)
1. Persenning entfernen, Scheibe mit Süßwasser abwaschen
2. Klebefuge auf Winterschäden inspizieren (Frost-Risse)
3. Wischergummi prüfen, ggf. tauschen
4. Scheibenheizung Funktionstest
5. Waschanlage befüllen, Düsen prüfen
6. Hydrophobe Beschichtung erneuern

### Saisonmitte (Juli–August)
1. Salzablagerungen regelmäßig abwaschen (mindestens wöchentlich)
2. Wischergummi auf Ablagerungen prüfen
3. UV-Belastung reduzieren: Sonnenschutz bei Liegezeiten > 2 Tage

### Herbsteinwinterung (Oktober–November)
1. Gründliche Reinigung aller Scheiben
2. Wischergummis reinigen, mit Glycerin behandeln
3. Wischerarme von Scheibe abheben (Gummischutz)
4. Persenning so aufspannen, dass Scheiben belüftet bleiben
5. Waschanlage entleeren (Frostschutz!)
6. Heizungsanschlüsse mit Korrosionsschutz behandeln

## ANHANG Q: Digitale Integration — AYDI-Analyse-Parameter

```python
# AYDI Windschutzscheiben-Analyse Parameter
WINDSCREEN_ANALYSIS_PARAMS = {
    "module": "structural",
    "sub_module": "windscreen",
    "zones": ["helm_station", "salon_forward", "owner_deck"],
    "visual_analysis_prompts": [
        "windscreen_condition",
        "windscreen_bonding",
        "windscreen_wiper_coverage",
        "windscreen_frame_corrosion",
        "windscreen_delamination"
    ],
    "scoring_weights": {
        "glass_type": 0.15,
        "glass_thickness_compliance": 0.20,
        "bonding_condition": 0.20,
        "wiper_system": 0.10,
        "heating_system": 0.10,
        "surface_condition": 0.15,
        "frame_condition": 0.10
    },
    "confidence_mapping": {
        "measured": ["glass_thickness", "glass_type", "frame_material"],
        "visual_high": ["surface_scratches", "delamination", "frame_corrosion"],
        "visual_medium": ["bonding_condition", "wiper_coverage"],
        "estimated": ["remaining_lifetime", "replacement_cost"]
    },
    "skip_conditions": [
        {"condition": "no_photos_and_no_specs", "reason": "Keine Daten für Windschutzscheiben-Analyse verfügbar"},
        {"condition": "boat_class_unknown", "reason": "Bootsklasse unbekannt — Bewertungsmaßstab fehlt"}
    ]
}
```

## ANHANG R: Änderungshistorie

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | 2025-01-15 | Erstversion: Grundlagen, Materialien, Bootsklassen | AYDI-Team |
| 1.1 | 2025-03-01 | Erweiterung: Kostentabellen, Superyacht-Fallstudien | AYDI-Team |
| 2.0 | 2026-04-25 | Erweiterung: Technische Referenz, Einbauanleitung, Fehlerbild-Atlas, FAQ, Glossar, Schnell-Referenz, Notfall-Ressourcen, Anhänge A–R | AYDI-Team |

---

*Ende der Wissensdatei 08.03 — Windschutzscheiben und Frontfenster — Vollständige Fassung*
*Confidence: `benchmark` für Praxiswerte, `measured` für Normdaten, `estimated` für Kostenangaben*
