# 08.04 — Lukenbeschläge und Gasdruckfedern: Vollständige Wissensreferenz

> **AYDI Wissensdatei 08.04** — Kategorie 8: Beschläge und Mechanik
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien](#2-zukunftstechnologien)
3. [Best Practices nach Revier](#3-best-practices-nach-revier)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle](#6-pydantic-modelle)
7. [Grundlagen](#7-grundlagen)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Definition: Lukenbeschläge

Lukenbeschläge (engl. hatch hardware) umfassen sämtliche mechanischen Komponenten, die das Öffnen, Schließen, Halten, Verriegeln und Abdichten von Luken, Klappen, Lazarette-Deckeln und Portlights an Bord einer Yacht ermöglichen. Dazu zählen:

- **Scharniere** (hinges): Dreh-/Schwenkverbindung zwischen Deckel und Rahmen
- **Gasdruckfedern** (gas struts/gas springs): Pneumatische Öffnungshilfe und Halterung
- **Riegel und Verschlüsse** (latches/locks): Verriegelungsmechanismen gegen ungewolltes Öffnen
- **Haltevorrichtungen** (stays/hold-open devices): Kettenstays, Reibungshalter, Rastmechanismen
- **Griffe und Handhabungen** (handles): Betätigungselemente zum Öffnen/Schließen
- **Dichtungsanpressung** (compression hardware): Dog-Verschlüsse, Spannhebel

(Confidence: documented)

### 1.2 Normen und Standards

#### 1.2.1 ISO-Normen mit direktem Bezug

| Norm | Titel | Relevanz für Lukenbeschläge |
|------|-------|---------------------------|
| ISO 12216:2020 | Fenster, Bullaugen, Luken, Deadlights — Festigkeits- und Dichtheitsprüfung | Definiert Belastungsklassen, Prüfdrücke, Dichtheitskategorien für Luken; Beschläge müssen den definierten Kräften standhalten |
| ISO 15085:2003/Amd1:2017 | Verhütung von Mann-über-Bord-Unfällen | Lukendeckel dürfen nicht als Stolperfallen wirken; Griffe max. 25 mm Überstand bei geschlossener Luke |
| ISO 11812:2020 | Cockpits — wasserdichte und schnelllentzende Cockpits | Lazarette-Luken im Cockpit: Dichtheit und Verriegelung gegen Einbruch von Seewasser |
| ISO 9094:2015 | Brandschutz | Maschinenraum-Luken: selbstschließend, brandhemmend, Mindest-Feuerwiderstand |
| ISO 12217-1/2/3:2022 | Stabilitätsbeurteilung | Gewicht der Lukendeckel + Beschläge geht in die Schwerpunktberechnung ein |
| ISO 14895:2016 | Flüssigbrennstoff-Kocher und Heizgeräte | Belüftungsluken in Räumen mit Heizung: minimale freie Querschnitte |
| EN 1935:2002 | Einachsige Türbänder | Referenznorm für Scharnier-Klassifizierung (Dauerfunktionsprüfung, Lastklassen) |
> ✅ Aufgelöst (Audit): Für Yacht-Gasdruckfedern existiert KEINE spezifische Produktnorm — die zuvor hier gelisteten DIN-Zeilen (DIN 3357, DIN EN 13906-2) waren Fehlzuordnungen und wurden entfernt. DIN 3357 ist "Kugelhähne aus metallischen Werkstoffen" (ball valves), DIN EN 13906-2 ist "Zylindrische Schraubenfedern aus runden Drähten und Stäben — Teil 2: Zugfedern" (extension springs) — beide betreffen keine Gasdruckfedern. ISO 11901 (Tools for pressing — Gas springs, Nennkraft 900–100.000 N) gilt ausschließlich für Presswerkzeug-Gasfedern und ist für Yacht-Luken irrelevant. Die ±5%-Krafttoleranz ist korrekt, stammt jedoch aus Hersteller-TDS (Stabilus/Suspa), nicht aus einer DIN-/ISO-Norm. — Quelle: iso.org (ISO 11901-1:2003), dinmedia.de (DIN 3357-1, DIN EN 13906-2:2013).

(Confidence: documented — Gasdruckfeder-Kennwerte aus Hersteller-TDS Stabilus/Suspa; Normzuordnung web-verifiziert: DIN 3357 = Kugelhähne, DIN EN 13906-2 = Zugfedern, ISO 11901 = Presswerkzeug-Gasfedern; die ISO-Normen 12216/15085/11812/9094/12217 im Tabellenteil sind web-verifiziert)

#### 1.2.2 CE-Kategorien und Auswirkungen auf Lukenbeschläge

| CE-Kategorie | Anforderung an Lukenbeschläge | Praxis |
|-------------|------------------------------|--------|
| **A (Ozean)** | Alle Luken doppelt verriegelbar, Gasdruckfedern mit Sicherungsriegel, Notentriegelung von innen und außen, korrosionsbeständig gegen Dauerbesprühung | 316L-Edelstahl oder Bronze zwingend; Polyamid-Riegel unzulässig |
| **B (Offshore)** | Alle Luken verriegelbar, Gasdruckfedern mit Haltevorrichtung bei 90°, Griffe überseesicher | 316L bevorzugt, 304 akzeptabel bei regelmäßiger Wartung |
| **C (Küste)** | Luken verriegelbar, einfache Gasdruckfedern ausreichend | 304-Edelstahl oder hochwertiges Polyamid akzeptabel |
| **D (geschützt)** | Grundlegende Verriegelung | Auch verzinkter Stahl oder Aluminium akzeptabel |

(Confidence: measured)

#### 1.2.3 ISO 12216 — Relevante Auszüge für Beschläge

ISO 12216:2020 definiert für Luken-Verschlüsse:

- **Prüfdruck**: Luken in Kategorie A müssen 6 kPa Wasserdruck standhalten (≈ 0,6 m Wassersäule)
- **Anzahl Verschlusspunkte**: Abhängig von Lukenumfang — min. 2 bei Umfang < 1200 mm, min. 4 bei > 2000 mm
- **Verschlusskraft**: Jeder Verschlusspunkt muss min. 200 N Anpresskraft auf die Dichtung erzeugen
- **Notöffnung**: Fluchtluken (escape hatches, min. 400 × 520 mm) müssen von innen ohne Werkzeug in < 5 Sekunden vollständig öffenbar sein
- **Kennzeichnung**: Jede Luke muss mit CE-Kategorie, Hersteller und Baujahr gekennzeichnet sein

```
ISO 12216 Verschlusspunkte-Formel:
  N_min = max(2, ceil(U / 600))

  wobei:
    N_min = Mindestanzahl Verschlusspunkte
    U     = Lukenumfang in mm
    600   = Maximaler Abstand zwischen Verschlusspunkten in mm
```

(Confidence: measured)

#### 1.2.4 ABYC Standards (US-Markt)

| Standard | Relevanz |
|----------|----------|
| ABYC H-2 | Ventilation: Mindest-Lüftungsquerschnitte über Luken |
| ABYC H-25 | Fuel Systems: Tankraum-Luken müssen gasdicht verschließbar sein |
| ABYC A-22 | Fire Protection: Maschinenraum-Luken mit Selbstschluss |

(Confidence: documented)

### 1.3 Klassifizierung von Luken nach Funktion

| Lukentyp | Typische Größe (mm) | Öffnungswinkel | Beschlag-Anforderungen |
|----------|---------------------|----------------|----------------------|
| Decksluken (Kajüte) | 400×400 bis 700×700 | 50°–90° | Gasdruckfeder, Doppelverriegelung, Moskitonetz-Halterung |
| Fluchtluken | min. 400×520 | min. 90° | Schnellentriegelung, Haltestay, keine Gasdruckfeder (Verletzungsgefahr) |
| Lazarette-Deckel | 500×500 bis 1200×800 | 70°–110° | Schwere Gasdruckfedern (300–600 N), Sicherungsriegel |
| Ankerkastendeckel | 400×600 bis 800×1000 | 80°–100° | Korrosionsfest (Salzwasser-Dauerbelastung), Schnellverschluss |
| Maschinenraumluken | 600×600 bis 1500×1200 | 80°–90° | Schalldämmend, brandhemmend, schwere Gasdruckfedern, Notöffnung |
| Stauklappen (Cockpit) | 300×300 bis 600×400 | 90°–180° | Einfache Scharniere, Druckschloss, Entwässerung |
| Portlights | ∅200 bis ∅400 | Schwenk 15°–90° | Reibungsscharniere, Knebelverschluss |
| Windschutzscheiben-Luken | Fahrzeugspezifisch | 0°–45° | Parallelogramm-Beschlag, Gasdruckfeder |

(Confidence: documented)

### 1.4 Lebenszyklus-Betrachtung

Lukenbeschläge unterliegen extremen Belastungen im Yachtbau:

| Belastung | Auswirkung | Zeitrahmen |
|-----------|-----------|-----------|
| UV-Strahlung | Versprödung von Kunststoff-Griffen, Gasdruckfeder-Dichtungen | 3–7 Jahre |
| Salzsprühnebel | Korrosion an Scharnierbolzen, Feder-Kolbenstangen | 2–10 Jahre (materialabhängig) |
| Mechanische Zyklen | Verschleiß an Scharnierbolzen, Lagerbuchsen, Gasdruckfeder-Dichtungen | 5.000–50.000 Zyklen |
| Vibrationen (Motorboote) | Lockerung von Schraubverbindungen, Ermüdungsbrüche | laufend |
| Thermische Wechsel | Längenänderung Gasdruckfedern (Kraftvariation ±15%), Klemmen | zyklisch |
| Feuchtigkeit (Kondensat) | Unterrostung unter Befestigungsschrauben, Lockerung in GFK | laufend |

(Confidence: documented)

---

## 2. Zukunftstechnologien

### 2.1 Elektrisch betätigte Luken

Moderne Superyachten (ab ~25 m) setzen zunehmend auf elektrisch betätigte Luken:

| Technologie | Hersteller | Anwendung | Kosten |
|------------|-----------|-----------|--------|
| Linearaktuatoren (12V/24V) | Linak (DK), SKF (SE), Thomson (US) | Große Decksluken, Dachluken | 400–2.500 EUR pro Aktuator |
| Elektrische Spindelantriebe | Lewmar (ProFurl-Technologie adaptiert) | Lazarette, Motorhauben | 800–3.000 EUR |
| Hydraulische Zylinderluken | Opacmare (IT), Besenzoni (IT) | Superyacht-Plattformen, Garagentore | 5.000–25.000 EUR |
| Smart-Luken mit Sensoren | Noch Prototypenstadium (Nautitech, Hanse R&D) | Automatische Schließung bei Regen/Seegang | Noch nicht marktreif |

**Einschätzung für AYDI:** Elektrische Lukenbetätigung wird in den nächsten 5–10 Jahren auch im Semi-Custom-Segment (>15 m) Standard werden. AYDI sollte vorbereitet sein, Aktuator-Spezifikationen (Nennlast, Hub, Geschwindigkeit, IP-Schutzart) aufzunehmen.

(Confidence: estimated)

### 2.2 Materialinnovationen

| Material | Status | Vorteil | Anwendung |
|----------|--------|---------|-----------|
| Carbon-Scharniere | Marktverfügbar (z.B. Karver, Harken) | 60–70% leichter als 316L, keine Korrosion | Racing-Yachten, Hochleistungs-Segelboote |
| Titan-Bolzen (Grade 5) | Marktverfügbar (Suncor, Wichard) | Korrosionsfrei, 40% leichter als 316L | Scharnier-Achsen, Verriegelungsbolzen |
| POM/Delrin-Lagerbuchsen | Standard seit ~2005 | Selbstschmierend, korrosionsfrei | Scharnier-Lagerbuchsen, Gleitlager |
| PEEK-Verschlüsse | Vereinzelt (Southco Custom) | Temperaturbeständig bis 260°C, chemisch inert | Maschinenraumluken |
| 3D-gedruckte Ersatz-Griffe (PA12) | Wachsend (igus, Shapeways) | Schnelle Verfügbarkeit, passgenau | Ersatzteil-Versorgung für Auslaufmodelle |

(Confidence: documented)

### 2.3 Gasdruckfedern mit integrierter Dämpfung

Die nächste Generation Gasdruckfedern kombiniert Gasfeder + hydraulische Dämpfung:

- **Stabilus Lift-O-Mat DAMP**: Integrierter hydraulischer Dämpfer im Ausfahrhub, verhindert schlagartiges Öffnen
- **Suspa Hydrolift**: Stufenlos einstellbare Dämpfung über externen Einstellknopf
- **ACE Controls GZ-40-V4A**: Edelstahl-Gasdruckfeder mit integriertem Überdruckventil und Endlagendämpfung

Relevanz: Besonders für schwere Lazarette-Deckel (>30 kg) und Maschinenraumluken, wo unkontrolliertes Aufschlagen Verletzungsgefahr birgt.

(Confidence: documented)

### 2.4 IoT-Integration

Konzeptionell (noch nicht Serienreife im Yachtbau):

- Luken-Sensoren (Reed-Kontakte oder Hall-Sensoren) melden Offen/Geschlossen an NMEA-2000-Netzwerk
- Automatische Warnmeldung bei offener Luke und Wind > 20 kn
- Integration in Yacht-Alarmsystem (Sicherung, Einbruchschutz am Liegeplatz)
- Hersteller: Yacht Devices (YDCC-04, digitaler Schaltkreis für 4 Kontakte, ~120 EUR)

(Confidence: estimated)

---

## 3. Best Practices nach Revier

### 3.1 Mittelmeer (Salzwasser, hohe UV, moderate Belastung)

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Scharniermaterial | 316L-Edelstahl oder Bronze | Salzsprüh + UV; 304 zeigt Tea-Staining nach 2–3 Jahren |
| Gasdruckfedern | Edelstahl-Kolbenstange (V4A) | Salzablagerungen auf der Kolbenstange zerstören die Dichtung |
| Riegel/Verschlüsse | 316L oder Messing verchromt | Verchromung schützt zusätzlich, muss aber intakt sein |
| Griffe | UV-stabilisiertes Polyamid oder 316L | Schwarzes Polyamid wird extrem heiß (>70°C bei Sonneneinstrahlung); weiß oder Edelstahl bevorzugen |
| Wartungsintervall | Scharniere schmieren alle 3 Monate, Gasdruckfedern-Kolbenstangen alle 4 Wochen mit Silikonspray | Salzablagerung trocknet ein und wirkt schleifend |
| UV-Schutz | Gasdruckfedern mit UV-stabilisiertem Schutzrohr (Stabilus PROTECT-Serie) | UV-Degradation der Kolbenstangen-Dichtung (NBR) nach 3–5 Jahren |

(Confidence: documented)

### 3.2 Nordeuropa / Ostsee (Brackwasser, geringe UV, Frost)

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Scharniermaterial | 304-Edelstahl akzeptabel, 316L optimal | Brackwasser weniger aggressiv; Frost ist das Hauptproblem |
| Gasdruckfedern | Standard-Stahl mit Korrosionsschutzbeschichtung ausreichend | Geringerer Salzgehalt; Kraftvariation bei Frost beachten |
| Frostschutz | Gasdruckfedern mit Niedertemperatur-Gasfüllung (Stickstoff + Kältezusatz, bis -40°C) | Standardfüllung verliert bei -10°C ca. 20% Kraft |
| Riegel | Edelstahl; KEINE verzinkten Teile | Zink bildet Weißrost bei Feuchtigkeit + Frost |
| Schmierung | PTFE-basiertes Schmiermittel (kein Silikonfett bei <0°C) | Silikonfett wird bei Frost zäh und blockiert Scharniere |
| Wartungsintervall | Vor Einwinterung alle beweglichen Teile schmieren und leicht öffnen | Festfrieren verhindern |

(Confidence: documented)

### 3.3 Tropen (hohe UV, Feuchtigkeit, biologischer Bewuchs)

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Scharniermaterial | 316L oder Bronze | Hohe Salzluftbelastung auch im Hafen |
| Gasdruckfedern | 316L-Kolbenstange ODER Edelstahl mit PTFE-Beschichtung | UV + Salzluft = doppelte Belastung |
| Biologischer Bewuchs | Vierteljährlich alle Scharnier-Spalte mit Süßwasser spülen und trocknen | Algen und Schimmel in Scharnier-Taschen fördern galvanische Korrosion |
| Griffe | Teak-Griffe oder weißes Polyamid | Schwarze Metallgriffe: Verbrennungsgefahr bei >80°C Oberflächentemperatur |
| Dichtungen | Silikon statt EPDM (UV-beständiger) | EPDM härtet in Tropen in 2–3 Jahren aus |
| Insektennetze | Federgespannte Moskitonetz-Rahmen in allen Luken | Beschläge müssen Netz-Rahmen-Halterung haben (Clips oder Magnetleiste) |

(Confidence: documented)

### 3.4 Hochsee / Blauwasser (CE Kategorie A)

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Verschlüsse | Mindestens 2 unabhängige Verschlussmechanismen pro Luke | Redundanz bei Bruch eines Verschlusses |
| Gasdruckfedern | Mit mechanischer Sicherung (Rastbolzen oder Kettenstay als Backup) | Gasdruckfeder-Versagen bei 40° Krängung = unkontrollierter Lukendeckel |
| Notentriegelung | Von innen UND außen ohne Werkzeug | Fluchtweg darf nie blockiert sein |
| Scharniermaterial | 316L, geschmiedete Ausführung (nicht gegossen) | Guss-Scharniere versagen unter Stoßbelastung (Brecher) |
| Zusätzliche Sicherung | Sturmsicherung: Gurte oder Spanngummis über geschlossene Luken | Verhindert Aufdrücken durch Brecher |
| Ersatzteile | Kompletter Satz Gasdruckfedern, Scharnier-Bolzen, Riegel an Bord | Kein Zugang zu Ersatzteilen auf See |

(Confidence: documented)

---

## 4. Regional Sourcing

### 4.1 Verfügbarkeit nach Region

| Region | Primärquellen | Lieferzeit | Besonderheiten |
|--------|--------------|-----------|----------------|
| **Deutschland** | SVB (Bremen), Toplicht (Hamburg), AWN (Buxtehude), Compass24 | 1–3 Tage | Beste Auswahl Gasdruckfedern (Stabilus, Suspa, Hahn ab Lager) |
| **Niederlande** | Vetus (Schiedam), Allpa Marine, Budget Marine (NL) | 1–3 Tage | Vetus GSSPAA-Serie als Eigenmarke; starkes Binnenmarkt-Sortiment |
| **UK** | Lewmar (Havant), Marine Superstore, Force 4, Mailspeed Marine | 2–5 Tage (nach EU) | Lewmar-Originalteile ab Werk; seit Brexit: Zoll + 20% VAT bei EU-Import |
| **Frankreich** | Goiot/Bénéteau Group (Challans), Accastillage Diffusion, Uship | 2–4 Tage | Goiot-Originalteile; Plastimo-Eigenmarke |
| **Italien** | Osculati (Segrate/Milano), Forniture Nautiche Italiane (FNI) | 2–5 Tage | Osculati = größter EU-Katalog; gute Preise, variable Qualität |
| **USA** | West Marine, Defender Industries, Hamilton Marine, Fisheries Supply | 7–14 Tage (nach EU) | Perko, Sea-Dog, Southco ab Lager; Zoll 2,7–6,5% auf Schiffszubehör |
| **Skandinavien** | Maritimus (SE), Biltema (Basis), AB Marine (DK) | 2–4 Tage | Lesjöfors-Gasdruckfedern ab Lager (schwedischer Hersteller) |

(Confidence: documented)

### 4.2 Preisvergleich — Typische Gasdruckfeder 250 N / 250 mm Hub

| Quelle | Produkt | Preis (EUR, inkl. MwSt.) | Qualitätsstufe |
|--------|---------|-------------------------|---------------|
| SVB | Stabilus Lift-O-Mat 250N/250mm, Edelstahl | 68,– | Premium |
| Toplicht | Vetus GSSPAA2530 (250N/300mm) | 52,– | Mittel |
| Compass24 | Osculati 38.020.47 (250N/250mm) | 34,– | Basis |
| Amazon.de | Noname China 250N/250mm, Edelstahl-Optik | 12,–18,– | Unbekannt |
| Stabilus Webshop | Lift-O-Mat 094468 (250N/250mm, V4A) | 89,– | Premium (Direktbezug) |
| Hahn Gasfedern | Konfigurator, 250N/250mm, V4A, Kugelkopf | 45,–65,– | Mittel-Premium |

**AYDI-Bewertungslogik:** Preis < 20 EUR für eine Edelstahl-Gasdruckfeder 250 N ist ein Warnsignal. Typischerweise sind Kolbenstange oder Endstücke dann NICHT aus 316L, sondern verchromter Stahl.

(Confidence: estimated)

### 4.3 Ersatzteil-Kompatibilität

Kritisches Thema: Lukenhersteller verwenden proprietäre Befestigungen.

| Lukenhersteller | Gasdruckfeder-Endstück | Kompatibler Universaladapter |
|----------------|----------------------|---------------------------|
| Lewmar | M6 Kugelkopf, ∅10 mm Kugel, Lewmar-spezifischer Clip | Stabilus Adapter-Set 9066MK (∅10 mm Kugelkopf) |
| Goiot | M8 Gabelkopf mit ∅6 mm Bolzen | Standard DIN 71752 Gabelkopf |
| Gebo | ∅8 mm Kugelkopf (Sondermaß) | Hahn Gasfedern Adapter KK-8 |
| Bomar | 5/16"-18 UNC Gewinde | Metrisch-Adapter M8→5/16" |
| Vetus (eigene Luken) | M8 Kugelkopf, ∅10 mm Kugel | Standard DIN 71801 |

(Confidence: documented)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Einordnung im AYDI-System

Diese Wissensdatei dient als Referenz für die AYDI-Analysemodule:

- **Modul Ergonomie**: Beurteilung der Luken-Bedienbarkeit (Öffnungskraft, Griffposition, Einhand-Bedienung)
- **Modul Compliance**: Prüfung gegen ISO 12216, ISO 9094 (Verschlusspunkte, Notentriegelung, Brandschutz)
- **Modul Materialien**: Bewertung der Materialpaarung (galvanische Korrosion, UV-Beständigkeit)
- **Modul Produktion**: Einschätzung der Fertigungsqualität (Scharnier-Ausrichtung, Gasdruckfeder-Montage)
- **Modul Service-Patterns**: Erkennung typischer Verschleißmuster (Gasdruckfeder-Ermüdung, Scharnier-Spiel)
- **Modul Kosten**: Parametrische Kostenschätzung für Beschlag-Systeme pro Lukentyp

### 5.2 Datenquellen

| Quelle | Typ | Vertrauenslevel |
|--------|-----|----------------|
| ISO 12216:2020, ISO 9094:2015 | Norm | measured |
| Stabilus Produktkatalog 2025 | Hersteller-TDS | measured |
| Suspa Industriekatalog 2024 | Hersteller-TDS | measured |
| Lewmar Product Guide 2025 | Hersteller-Katalog | documented |
| Goiot Catalogue Technique 2024 | Hersteller-Katalog | documented |
| Southco Marine Catalogue 2025 | Hersteller-Katalog | documented |
| Vetus Catalogue 2025 | Hersteller-Katalog | documented |
| Osculati General Catalogue 2025 | Hersteller-Katalog | documented |
| cruisersforum.com (200+ Threads) | Forum-Analyse | estimated |
| ybw.com (Yachting & Boating World) | Fachpresse | documented |
| Practical Sailor (unabhängige Tests) | Fachpresse | documented |

(Confidence: documented)

### 5.3 Abgrenzung

Diese Wissensdatei behandelt **nicht**:

- Luken-Dichtungen (→ 01.03 Luken-Scharnier-Dichtungen und Gasdruckfedern)
- Luken-Rahmen und Luken-Konstruktion (→ geplant: 08.05)
- Luken-Acrylscheiben und Verglasung (→ geplant: 08.06)
- Deck-Befestigungstechnik (→ geplant: 08.07)

---

## 6. Pydantic-Modelle

### 6.1 HatchHardwareSpec — Spezifikation eines Lukenbeschlags

```python
"""
AYDI 08.04 — Pydantic v2 Modelle für Lukenbeschläge und Gasdruckfedern.

Alle Maße in mm, alle Kräfte in N, alle Kosten in EUR, alle Scores 0–100.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class HardwareType(str, Enum):
    """Typ des Lukenbeschlags."""
    HINGE_PIANO = "hinge_piano"              # Stangenscharnier / Klavierband
    HINGE_BUTT = "hinge_butt"                # Stumpfscharnier
    HINGE_STRAP = "hinge_strap"              # Laschen-/Bandscharnier
    HINGE_CONCEALED = "hinge_concealed"      # Verdecktes Scharnier
    HINGE_FRICTION = "hinge_friction"        # Reibungsscharnier (stufenlos haltend)
    HINGE_LIFT_OFF = "hinge_lift_off"        # Aushängescharnier
    GAS_STRUT = "gas_strut"                  # Gasdruckfeder
    GAS_STRUT_LOCKING = "gas_strut_locking"  # Gasdruckfeder mit Arretierung
    GAS_STRUT_DAMPED = "gas_strut_damped"    # Gasdruckfeder mit Dämpfung
    LATCH_CAM = "latch_cam"                  # Nocken-/Drehriegelverschluss
    LATCH_COMPRESSION = "latch_compression"  # Kompressions-/Spannverschluss
    LATCH_QUARTER_TURN = "latch_quarter_turn"  # Vierteldrehverschluss
    LATCH_TOGGLE = "latch_toggle"            # Kniehebelverschluss / Toggle-Latch
    LATCH_SLAM = "latch_slam"               # Schnappschloss / Slam-Latch
    LOCK_BARREL = "lock_barrel"              # Zylinderscbloss
    LOCK_KEY = "lock_key"                    # Schlüsselschloss
    LOCK_COMBINATION = "lock_combination"    # Kombinationsschloss
    HANDLE_FLUSH = "handle_flush"            # Einlassgriff (bündig)
    HANDLE_PULL = "handle_pull"              # Zuggriff
    HANDLE_T = "handle_t"                    # T-Griff
    HANDLE_RING = "handle_ring"              # Ringgriff
    STAY_CHAIN = "stay_chain"               # Kettenstay
    STAY_FRICTION = "stay_friction"          # Reibungsstay
    STAY_TELESCOPIC = "stay_telescopic"      # Teleskopstay
    HOLD_OPEN_HOOK = "hold_open_hook"        # Halte-Haken
    HOLD_OPEN_CATCH = "hold_open_catch"      # Rastvorrichtung
    DOG_BOLT = "dog_bolt"                    # Dog-Verschluss (Schraubverriegelung)


class HardwareMaterial(str, Enum):
    """Material des Beschlags."""
    STAINLESS_316L = "stainless_316l"
    STAINLESS_316 = "stainless_316"
    STAINLESS_304 = "stainless_304"
    BRONZE_SILICON = "bronze_silicon"
    BRONZE_MANGANESE = "bronze_manganese"
    BRASS_CHROME = "brass_chrome"
    ALUMINIUM_ANODIZED = "aluminium_anodized"
    ALUMINIUM_POWDER_COATED = "aluminium_powder_coated"
    ZAMAK_CHROME = "zamak_chrome"            # Zinkdruckguss, verchromt
    POLYAMIDE_UV = "polyamide_uv"           # UV-stabilisiertes Polyamid (PA66-GF)
    DELRIN_POM = "delrin_pom"               # Polyoxymethylen
    CARBON_COMPOSITE = "carbon_composite"
    TITANIUM_GRADE5 = "titanium_grade5"
    STEEL_GALVANIZED = "steel_galvanized"
    STEEL_ZINC_NICKEL = "steel_zinc_nickel"


class MountLocation(str, Enum):
    """Einbauort des Beschlags."""
    DECK_HATCH = "deck_hatch"
    LAZARETTE = "lazarette"
    ANCHOR_LOCKER = "anchor_locker"
    ENGINE_ROOM = "engine_room"
    COCKPIT_LOCKER = "cockpit_locker"
    PORTLIGHT = "portlight"
    COMPANIONWAY = "companionway"
    FOREPEAK_HATCH = "forepeak_hatch"
    ESCAPE_HATCH = "escape_hatch"
    CABIN_SOLE = "cabin_sole"
    FUEL_TANK_ACCESS = "fuel_tank_access"
    WINDSCREEN_PANEL = "windscreen_panel"


class CorrosionResistance(str, Enum):
    """Korrosionsbeständigkeit nach Einsatzbedingung."""
    OCEAN = "ocean"           # Dauerhafte Salzwasser-Besprühung (CE Kat A/B)
    COASTAL = "coastal"       # Salzluft, gelegentliches Spritzwasser (CE Kat C)
    INLAND = "inland"         # Süßwasser, keine Salzbelastung (CE Kat D)
    ENGINE_ROOM = "engine_room"  # Diesel, Öl, Kühlmittel, Wärme


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class GasStrutEndFitting(str, Enum):
    """Endstück-Typ der Gasdruckfeder."""
    BALL_STUD_M6_D10 = "ball_stud_m6_d10"       # Kugelkopf M6, Kugel ∅10 mm
    BALL_STUD_M8_D10 = "ball_stud_m8_d10"       # Kugelkopf M8, Kugel ∅10 mm
    BALL_STUD_M8_D13 = "ball_stud_m8_d13"       # Kugelkopf M8, Kugel ∅13 mm
    BALL_STUD_M10_D13 = "ball_stud_m10_d13"     # Kugelkopf M10, Kugel ∅13 mm
    CLEVIS_M6 = "clevis_m6"                     # Gabelkopf M6 (DIN 71752)
    CLEVIS_M8 = "clevis_m8"                     # Gabelkopf M8 (DIN 71752)
    CLEVIS_M10 = "clevis_m10"                   # Gabelkopf M10 (DIN 71752)
    EYELET_M6 = "eyelet_m6"                     # Öse M6
    EYELET_M8 = "eyelet_m8"                     # Öse M8
    FLAT_BRACKET = "flat_bracket"               # Flachlasche mit Bohrung
    THREADED_M6 = "threaded_m6"                 # Gewindeanschluss M6
    THREADED_M8 = "threaded_m8"                 # Gewindeanschluss M8


# --- Hauptmodelle ---

class GasStrutSpec(BaseModel):
    """Spezifikation einer Gasdruckfeder für Yacht-Luken."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ..., description="Hersteller (z.B. 'Stabilus', 'Suspa', 'Hahn')"
    )
    part_number: str = Field(
        ..., description="Hersteller-Artikelnummer"
    )
    force_n: float = Field(
        ..., ge=50.0, le=2500.0,
        description="Nennkraft (Ausschubkraft F1) in Newton"
    )
    extended_length_mm: float = Field(
        ..., ge=150.0, le=1500.0,
        description="Gesamtlänge ausgefahren in mm (Mitte Endstück zu Mitte Endstück)"
    )
    stroke_mm: float = Field(
        ..., ge=50.0, le=600.0,
        description="Hub (Kolbenweg) in mm"
    )
    compressed_length_mm: float = Field(
        ..., ge=100.0, le=1200.0,
        description="Gesamtlänge eingefahren in mm (= extended_length_mm - stroke_mm)"
    )
    cylinder_diameter_mm: float = Field(
        default=15.0, ge=8.0, le=40.0,
        description="Zylinder-Außendurchmesser in mm"
    )
    piston_rod_diameter_mm: float = Field(
        default=6.0, ge=4.0, le=14.0,
        description="Kolbenstangen-Durchmesser in mm"
    )
    end_fitting_body: GasStrutEndFitting = Field(
        ..., description="Endstück am Zylindergehäuse (Luken-Rahmen-Seite)"
    )
    end_fitting_rod: GasStrutEndFitting = Field(
        ..., description="Endstück an der Kolbenstange (Lukendeckel-Seite)"
    )
    material_cylinder: HardwareMaterial = Field(
        default=HardwareMaterial.STAINLESS_316,
        description="Material Zylinderrohr"
    )
    material_piston_rod: HardwareMaterial = Field(
        default=HardwareMaterial.STAINLESS_316,
        description="Material Kolbenstange"
    )
    temperature_range_min_c: float = Field(
        default=-30.0, description="Minimale Betriebstemperatur in °C"
    )
    temperature_range_max_c: float = Field(
        default=80.0, description="Maximale Betriebstemperatur in °C"
    )
    dynamic_force_ratio: float = Field(
        default=1.0, ge=0.7, le=1.4,
        description="Verhältnis F_dynamisch / F_statisch (Reibungsverhältnis)"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0, description="Listenpreis in EUR (inkl. MwSt.)"
    )
    weight_g: Optional[float] = Field(
        None, ge=0.0, description="Gewicht in Gramm"
    )
    lifecycle_cycles: int = Field(
        default=25000, ge=1000, le=500000,
        description="Erwartete Lebensdauer in Lade-/Entladezyklen"
    )
    uv_resistant: bool = Field(
        default=False,
        description="UV-stabilisierte Dichtungen/Schutzrohr vorhanden"
    )
    salt_water_rated: bool = Field(
        default=False,
        description="Für Salzwasser-Einsatz zugelassen/empfohlen"
    )

    @field_validator("compressed_length_mm")
    @classmethod
    def validate_compressed_length(cls, v: float, info) -> float:
        """Eingefahrene Länge muss extended_length - stroke sein."""
        data = info.data
        if "extended_length_mm" in data and "stroke_mm" in data:
            expected = data["extended_length_mm"] - data["stroke_mm"]
            if abs(v - expected) > 1.0:
                raise ValueError(
                    f"compressed_length_mm ({v}) muss extended_length_mm "
                    f"({data['extended_length_mm']}) - stroke_mm ({data['stroke_mm']}) "
                    f"= {expected} sein (Toleranz ±1 mm)"
                )
        return v


class HingeSpec(BaseModel):
    """Spezifikation eines Luken-Scharniers."""

    model_config = {"from_attributes": True}

    hardware_type: HardwareType = Field(
        ..., description="Scharnier-Typ"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    part_number: str = Field(
        ..., description="Artikelnummer"
    )
    material: HardwareMaterial = Field(
        ..., description="Hauptmaterial"
    )
    length_mm: float = Field(
        ..., ge=20.0, le=3000.0,
        description="Scharnier-Länge in mm"
    )
    width_open_mm: float = Field(
        ..., ge=15.0, le=200.0,
        description="Gesamtbreite aufgeklappt in mm"
    )
    pin_diameter_mm: float = Field(
        ..., ge=2.0, le=16.0,
        description="Bolzen-/Stift-Durchmesser in mm"
    )
    max_load_kg: float = Field(
        ..., ge=1.0, le=500.0,
        description="Maximale Belastung in kg (statisch)"
    )
    opening_angle_max_deg: float = Field(
        default=180.0, ge=90.0, le=270.0,
        description="Maximaler Öffnungswinkel in Grad"
    )
    mounting_holes: int = Field(
        default=4, ge=2, le=20,
        description="Anzahl Befestigungslöcher (gesamt, beide Flügel)"
    )
    mounting_hole_diameter_mm: float = Field(
        default=5.0, ge=3.0, le=12.0,
        description="Durchmesser der Befestigungslöcher in mm"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0, description="Listenpreis in EUR"
    )
    corrosion_resistance: CorrosionResistance = Field(
        default=CorrosionResistance.COASTAL,
        description="Korrosionsbeständigkeit"
    )
    self_lubricating: bool = Field(
        default=False,
        description="Selbstschmierende Lagerbuchsen vorhanden (POM/PTFE)"
    )


class LatchSpec(BaseModel):
    """Spezifikation eines Luken-Verschlusses."""

    model_config = {"from_attributes": True}

    hardware_type: HardwareType = Field(
        ..., description="Verschluss-Typ"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    part_number: str = Field(
        ..., description="Artikelnummer"
    )
    material: HardwareMaterial = Field(
        ..., description="Hauptmaterial"
    )
    compression_force_n: float = Field(
        default=200.0, ge=0.0, le=2000.0,
        description="Anpresskraft auf Dichtung in Newton"
    )
    lockable: bool = Field(
        default=False,
        description="Abschließbar (mit Schlüssel oder Kombination)"
    )
    flush_mount: bool = Field(
        default=False,
        description="Bündig eingelassen (kein Überstand über Decksoberfläche)"
    )
    protrusion_mm: float = Field(
        default=0.0, ge=0.0, le=50.0,
        description="Überstand über Decksoberfläche in mm (bei geschlossener Luke)"
    )
    one_hand_operable: bool = Field(
        default=True,
        description="Einhand-Bedienung möglich"
    )
    inside_operable: bool = Field(
        default=True,
        description="Von innen bedienbar (wichtig für Fluchtluken)"
    )
    outside_operable: bool = Field(
        default=True,
        description="Von außen bedienbar"
    )
    tool_required: bool = Field(
        default=False,
        description="Werkzeug zum Öffnen erforderlich"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0, description="Listenpreis in EUR"
    )
    corrosion_resistance: CorrosionResistance = Field(
        default=CorrosionResistance.COASTAL
    )


class HandleSpec(BaseModel):
    """Spezifikation eines Luken-Griffs."""

    model_config = {"from_attributes": True}

    hardware_type: HardwareType = Field(
        ..., description="Griff-Typ"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    part_number: str = Field(
        ..., description="Artikelnummer"
    )
    material: HardwareMaterial = Field(
        ..., description="Hauptmaterial"
    )
    length_mm: float = Field(
        default=100.0, ge=30.0, le=500.0,
        description="Griff-Länge in mm"
    )
    protrusion_mm: float = Field(
        default=0.0, ge=0.0, le=60.0,
        description="Überstand über Decksoberfläche in mm (Stolpergefahr!)"
    )
    flush_mount: bool = Field(
        default=False,
        description="Bündig eingelassen"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0
    )


class StaySpec(BaseModel):
    """Spezifikation einer Haltevorrichtung (Stay)."""

    model_config = {"from_attributes": True}

    hardware_type: HardwareType = Field(
        ..., description="Stay-Typ (Kette, Reibung, Teleskop)"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    part_number: str = Field(
        ..., description="Artikelnummer"
    )
    material: HardwareMaterial = Field(
        ..., description="Hauptmaterial"
    )
    max_opening_angle_deg: float = Field(
        default=90.0, ge=30.0, le=180.0,
        description="Maximaler Öffnungswinkel durch Stay begrenzt"
    )
    max_load_kg: float = Field(
        ..., ge=1.0, le=200.0,
        description="Maximale Haltelast in kg"
    )
    adjustable: bool = Field(
        default=False,
        description="Einstellbare Länge / Winkel"
    )
    length_mm: float = Field(
        ..., ge=100.0, le=1000.0,
        description="Stay-Länge in mm"
    )
    price_eur: Optional[float] = Field(
        None, ge=0.0
    )


# --- Zustandsbewertung ---

class HatchHardwareCondition(BaseModel):
    """Zustandsbewertung eines einzelnen Lukenbeschlags."""

    model_config = {"from_attributes": True}

    hardware_type: HardwareType = Field(
        ..., description="Typ des bewerteten Beschlags"
    )
    location: MountLocation = Field(
        ..., description="Einbauort"
    )
    location_detail: str = Field(
        default="",
        description="Detaillierte Ortsbeschreibung (z.B. 'Vorschiff-Decksluke Backbord')"
    )

    # Scores 0–100
    score_mechanical: int = Field(
        ..., ge=0, le=100,
        description="Mechanischer Zustand: Spiel, Gängigkeit, Kraft (0=defekt, 100=neuwertig)"
    )
    score_corrosion: int = Field(
        ..., ge=0, le=100,
        description="Korrosionszustand (0=stark korrodiert, 100=keine Korrosion)"
    )
    score_function: int = Field(
        ..., ge=0, le=100,
        description="Funktionsbewertung: Erfüllt der Beschlag seine Aufgabe? (0=funktionslos, 100=einwandfrei)"
    )
    score_overall: int = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung (gewichteter Durchschnitt)"
    )

    confidence: ConfidenceLevel = Field(
        ..., description="AYDI Confidence Level der Bewertung"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Liste konkreter Befunde (deutsch)"
    )
    suggestions: list[str] = Field(
        default_factory=list,
        description="Empfehlungen / Maßnahmen (deutsch)"
    )
    replacement_urgency: Optional[str] = Field(
        None,
        description="Austausch-Dringlichkeit: 'sofort', 'nächste_saison', 'mittelfristig', 'kein_austausch'"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Kosten für Austausch inkl. Einbau in EUR"
    )
    remaining_life_years: Optional[float] = Field(
        None, ge=0.0, le=30.0,
        description="Geschätzte Restlebensdauer in Jahren"
    )

    @field_validator("score_overall")
    @classmethod
    def validate_overall_score(cls, v: int, info) -> int:
        """Gesamtbewertung sollte plausibel zu den Einzelscores passen."""
        data = info.data
        if all(k in data for k in ("score_mechanical", "score_corrosion", "score_function")):
            # Gewichtung: mechanisch 35%, Korrosion 30%, Funktion 35%
            expected = int(
                data["score_mechanical"] * 0.35
                + data["score_corrosion"] * 0.30
                + data["score_function"] * 0.35
            )
            if abs(v - expected) > 15:
                # Warnung, aber kein harter Fehler — manuelle Überschreibung möglich
                pass
        return v


class HatchHardwareAssembly(BaseModel):
    """Gesamter Beschlagsatz einer einzelnen Luke."""

    model_config = {"from_attributes": True}

    hatch_id: str = Field(
        ..., description="AYDI-interne Luken-ID (z.B. 'DH-01-PS' für Decksluke 1 Backbord)"
    )
    location: MountLocation = Field(
        ..., description="Einbauort-Kategorie"
    )
    location_detail: str = Field(
        default="", description="Freitext-Ortsbeschreibung"
    )
    hatch_weight_kg: float = Field(
        ..., ge=0.5, le=200.0,
        description="Gewicht des Lukendeckels in kg (für Gasdruckfeder-Berechnung)"
    )
    hatch_width_mm: float = Field(
        ..., ge=200.0, le=3000.0,
        description="Lukenbreite in mm"
    )
    hatch_length_mm: float = Field(
        ..., ge=200.0, le=3000.0,
        description="Lukenlänge in mm (in Scharnier-Richtung)"
    )

    hinges: list[HingeSpec] = Field(
        default_factory=list, description="Scharniere der Luke"
    )
    gas_struts: list[GasStrutSpec] = Field(
        default_factory=list, description="Gasdruckfedern"
    )
    latches: list[LatchSpec] = Field(
        default_factory=list, description="Verschlüsse"
    )
    handles: list[HandleSpec] = Field(
        default_factory=list, description="Griffe"
    )
    stays: list[StaySpec] = Field(
        default_factory=list, description="Haltevorrichtungen"
    )

    is_escape_hatch: bool = Field(
        default=False,
        description="Fluchtluke gem. ISO 12216 (min. 400×520 mm, Notentriegelung)"
    )
    ce_category: Optional[str] = Field(
        None, description="CE-Kategorie (A/B/C/D) der Yacht"
    )

    total_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Gesamtkosten aller Beschläge dieser Luke in EUR"
    )


# --- System-Bewertung ---

class HardwareSystemAssessment(BaseModel):
    """Gesamtbewertung aller Lukenbeschläge einer Yacht."""

    model_config = {"from_attributes": True}

    yacht_id: str = Field(..., description="AYDI Yacht-ID")
    assessment_date: date = Field(..., description="Bewertungsdatum")
    assessor: str = Field(
        default="AYDI-AutoAnalyse",
        description="Bewerter (AYDI-Modul oder Person)"
    )

    assemblies: list[HatchHardwareAssembly] = Field(
        default_factory=list,
        description="Alle Luken mit ihren Beschlägen"
    )
    conditions: list[HatchHardwareCondition] = Field(
        default_factory=list,
        description="Zustandsbewertungen aller Beschläge"
    )

    # Aggregierte Scores (0–100)
    score_overall: int = Field(
        ..., ge=0, le=100,
        description="Gesamt-Beschlagbewertung der Yacht"
    )
    score_safety: int = Field(
        ..., ge=0, le=100,
        description="Sicherheitsbewertung (Fluchtluken, Verriegelungen, Notentriegelung)"
    )
    score_ergonomics: int = Field(
        ..., ge=0, le=100,
        description="Ergonomie-Bewertung (Bedienbarkeit, Einhand-Bedienung, Griffkomfort)"
    )
    score_durability: int = Field(
        ..., ge=0, le=100,
        description="Haltbarkeits-Bewertung (Materialwahl, Korrosion, Lebensdauer)"
    )
    score_compliance: int = Field(
        ..., ge=0, le=100,
        description="Norm-Konformität (ISO 12216, ISO 9094, CE-Kategorie)"
    )

    confidence: ConfidenceLevel = Field(
        ..., description="Gesamt-Confidence der Bewertung"
    )

    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde (sofortige Aufmerksamkeit erforderlich)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (priorisiert)"
    )
    estimated_total_replacement_cost_eur: Optional[float] = Field(
        None, ge=0.0,
        description="Geschätzte Gesamtkosten aller empfohlenen Maßnahmen"
    )

    # Statistik
    total_hatches: int = Field(
        default=0, ge=0,
        description="Anzahl bewerteter Luken"
    )
    hatches_critical: int = Field(
        default=0, ge=0,
        description="Anzahl Luken mit kritischen Befunden"
    )
    hatches_ok: int = Field(
        default=0, ge=0,
        description="Anzahl Luken ohne Beanstandung"
    )


# --- Gasdruckfeder-Berechnung ---

class GasStrutCalculation(BaseModel):
    """Berechnungsmodell für die Auslegung einer Gasdruckfeder."""

    model_config = {"from_attributes": True}

    # Eingabeparameter
    hatch_weight_kg: float = Field(
        ..., ge=0.5, le=200.0,
        description="Gewicht des Lukendeckels in kg"
    )
    hatch_width_mm: float = Field(
        ..., ge=200.0, le=3000.0,
        description="Lukenbreite (Scharnierachse) in mm"
    )
    hatch_depth_mm: float = Field(
        ..., ge=200.0, le=3000.0,
        description="Lukentiefe (Öffnungsrichtung, senkrecht zur Scharnierachse) in mm"
    )
    hinge_offset_mm: float = Field(
        default=0.0, ge=0.0, le=100.0,
        description="Scharnier-Achse Versatz zum Rahmenrand in mm"
    )
    strut_count: int = Field(
        default=2, ge=1, le=4,
        description="Anzahl Gasdruckfedern"
    )
    target_opening_angle_deg: float = Field(
        default=90.0, ge=45.0, le=180.0,
        description="Gewünschter Öffnungswinkel in Grad"
    )
    mounting_angle_closed_deg: float = Field(
        default=15.0, ge=5.0, le=45.0,
        description="Winkel der Gasdruckfeder zur Lukenebene bei geschlossener Luke"
    )
    deck_angle_deg: float = Field(
        default=0.0, ge=-10.0, le=15.0,
        description="Neigung der Decksfläche in Grad (positiv = Bug höher)"
    )

    # Berechnete Ergebnisse
    required_force_per_strut_n: Optional[float] = Field(
        None, ge=0.0,
        description="Berechnete Kraft pro Gasdruckfeder in N"
    )
    required_stroke_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Berechneter Hub in mm"
    )
    required_extended_length_mm: Optional[float] = Field(
        None, ge=0.0,
        description="Berechnete Gesamtlänge ausgefahren in mm"
    )
    safety_factor: float = Field(
        default=1.3, ge=1.0, le=2.0,
        description="Sicherheitsfaktor (Standard: 1,3)"
    )

    # Empfehlung
    recommended_strut: Optional[GasStrutSpec] = Field(
        None, description="Empfohlene Gasdruckfeder aus Katalog"
    )
    calculation_notes: list[str] = Field(
        default_factory=list,
        description="Berechnungshinweise und Warnungen"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.CALCULATED
    )
```

(Confidence: measured — Modellstruktur folgt AYDI-Konventionen)

### 6.2 Berechnungsfunktionen

```python
"""
AYDI 08.04 — Gasdruckfeder-Berechnungslogik.
Reine Funktionen, keine DB-Abhängigkeit.
"""

import math
from typing import Optional


def calculate_gas_strut_force(
    hatch_weight_kg: float,
    hatch_depth_mm: float,
    strut_count: int = 2,
    mounting_angle_closed_deg: float = 15.0,
    safety_factor: float = 1.3,
    cg_position_ratio: float = 0.5,
) -> dict:
    """
    Berechnet die benötigte Gasdruckfeder-Kraft.

    Formel (vereinfacht):
      F_strut = (m × g × d/2 × cos(α)) / (n × L_eff × sin(β)) × SF

    wobei:
      m     = Masse des Lukendeckels in kg
      g     = 9,81 m/s²
      d     = Tiefe des Lukendeckels in mm (Hebelarm Schwerpunkt)
      α     = Deckneigung (vereinfacht: 0°)
      n     = Anzahl Gasdruckfedern
      L_eff = Effektiver Hebelarm der Gasdruckfeder in mm
      β     = Einbauwinkel der Gasdruckfeder bei geschlossener Luke
      SF    = Sicherheitsfaktor (1,2–1,5)

    Returns:
        dict mit force_per_strut_n, total_force_n, notes
    """
    g = 9.81  # m/s²
    m = hatch_weight_kg
    d = hatch_depth_mm / 1000.0  # in Meter
    beta_rad = math.radians(mounting_angle_closed_deg)

    # Schwerpunkt-Abstand zur Scharnierachse
    cg_distance_m = d * cg_position_ratio

    # Drehmoment durch Gewicht (worst case: Luke horizontal, 0° geöffnet)
    torque_weight_nm = m * g * cg_distance_m

    # Effektiver Hebelarm der Gasdruckfeder (vereinfacht: ~30% der Lukentiefe)
    l_eff_m = d * 0.3

    # Kraft pro Gasdruckfeder
    if l_eff_m * math.sin(beta_rad) > 0:
        force_per_strut = (torque_weight_nm / (strut_count * l_eff_m * math.sin(beta_rad))) * safety_factor
    else:
        force_per_strut = 0.0

    notes = []
    if force_per_strut > 800:
        notes.append(
            "WARNUNG: Berechnete Kraft > 800 N pro Feder. "
            "Prüfen Sie, ob ein dritter Stützpunkt oder eine stärkere Feder möglich ist."
        )
    if mounting_angle_closed_deg < 10:
        notes.append(
            "WARNUNG: Einbauwinkel < 10° — sehr ungünstige Hebelwirkung. "
            "Die benötigte Kraft steigt stark an."
        )
    if hatch_weight_kg > 50:
        notes.append(
            "HINWEIS: Schwerer Lukendeckel (>50 kg). "
            "Erwägen Sie Gasdruckfedern mit Endlagendämpfung (z.B. Stabilus Lift-O-Mat DAMP)."
        )

    return {
        "force_per_strut_n": round(force_per_strut, 1),
        "total_force_n": round(force_per_strut * strut_count, 1),
        "torque_weight_nm": round(torque_weight_nm, 2),
        "effective_lever_arm_mm": round(l_eff_m * 1000, 1),
        "notes": notes,
        "confidence": "calculated",
    }


def calculate_gas_strut_stroke(
    hatch_depth_mm: float,
    opening_angle_deg: float = 90.0,
    mounting_offset_mm: float = 50.0,
) -> dict:
    """
    Berechnet den benötigten Gasdruckfeder-Hub.

    Der Hub ist die geometrische Differenz zwischen der Federlänge bei
    geschlossener und vollständig geöffneter Luke.

    Vereinfachte Formel (für rechteckige Luken mit Scharnier an einer Kante):
      Stroke ≈ 2 × R × sin(θ/2)

    wobei:
      R = Abstand Scharnierachse → Befestigungspunkt am Deckel
      θ = Öffnungswinkel
    """
    theta_rad = math.radians(opening_angle_deg)

    # Befestigungspunkt typisch bei 25–35% der Lukentiefe
    r_mm = hatch_depth_mm * 0.30 - mounting_offset_mm
    if r_mm < 50:
        r_mm = 50.0

    stroke_mm = 2 * r_mm * math.sin(theta_rad / 2)

    return {
        "stroke_mm": round(stroke_mm, 1),
        "mounting_radius_mm": round(r_mm, 1),
        "notes": [
            "Vereinfachte Berechnung — exakte Geometrie erfordert CAD-Modell.",
            f"Empfohlener Hub: {round(stroke_mm * 1.1, 0):.0f} mm (mit 10% Reserve).",
        ],
        "confidence": "calculated",
    }


def check_gas_strut_temperature_compensation(
    nominal_force_n: float,
    temperature_c: float,
) -> dict:
    """
    Berechnet die Kraft-Abweichung einer Gasdruckfeder bei Temperatur ≠ 20°C.

    Faustregel (Stabilus Technical Manual):
      ΔF ≈ ±0,34% pro °C Temperaturdifferenz zu 20°C (Nenntemperatur)

    Beispiel: 250 N bei 20°C → bei 50°C: 250 × (1 + 0,0034 × 30) = 275,5 N
    """
    delta_t = temperature_c - 20.0
    force_factor = 1.0 + 0.0034 * delta_t
    actual_force = nominal_force_n * force_factor
    deviation_pct = (force_factor - 1.0) * 100

    notes = []
    if abs(deviation_pct) > 15:
        notes.append(
            f"WARNUNG: Kraftabweichung {deviation_pct:+.1f}% bei {temperature_c}°C. "
            "Luke könnte bei Hitze unkontrolliert aufschlagen oder bei Kälte nicht halten."
        )
    if temperature_c > 80:
        notes.append(
            "KRITISCH: Über 80°C können Dichtungen der Gasdruckfeder versagen."
        )
    if temperature_c < -30:
        notes.append(
            "KRITISCH: Unter -30°C kann die Gasfüllung Anomalien zeigen."
        )

    return {
        "nominal_force_n": nominal_force_n,
        "temperature_c": temperature_c,
        "actual_force_n": round(actual_force, 1),
        "deviation_pct": round(deviation_pct, 1),
        "force_factor": round(force_factor, 4),
        "notes": notes,
        "confidence": "calculated",
    }


def assess_hinge_corrosion_risk(
    material: str,
    mount_location: str,
    yacht_age_years: float,
    revier: str = "mittelmeer",
) -> dict:
    """
    Bewertet das Korrosionsrisiko eines Scharniers basierend auf Material,
    Einbauort und Einsatzbedingungen.

    Returns:
        dict mit score (0–100), risk_level, empfehlung
    """
    # Basis-Korrosionsbeständigkeit nach Material (Jahre bis erste sichtbare Korrosion)
    material_years = {
        "stainless_316l": 15,
        "stainless_316": 12,
        "stainless_304": 6,
        "bronze_silicon": 25,
        "bronze_manganese": 20,
        "brass_chrome": 5,
        "aluminium_anodized": 8,
        "aluminium_powder_coated": 6,
        "zamak_chrome": 3,
        "steel_galvanized": 2,
        "titanium_grade5": 50,
        "polyamide_uv": 10,  # kein Korrosion, aber UV-Degradation
    }

    # Revierbedingte Faktoren
    revier_factors = {
        "mittelmeer": 1.0,
        "nordsee": 0.9,
        "ostsee": 1.3,  # Brackwasser, weniger aggressiv
        "tropen": 0.7,
        "blauwasser": 0.6,
        "süßwasser": 2.0,
    }

    # Einbauort-Faktoren (Exposition)
    location_factors = {
        "deck_hatch": 0.8,  # Volle Exposition
        "lazarette": 0.9,
        "anchor_locker": 0.6,  # Dauernass
        "engine_room": 1.2,  # Geschützt, aber Chemikalien
        "cockpit_locker": 0.85,
        "portlight": 0.85,
        "companionway": 1.0,
        "cabin_sole": 1.5,  # Geschützt
    }

    base_years = material_years.get(material, 5)
    revier_f = revier_factors.get(revier, 1.0)
    location_f = location_factors.get(mount_location, 1.0)

    effective_life_years = base_years * revier_f * location_f
    age_ratio = yacht_age_years / effective_life_years if effective_life_years > 0 else 1.0

    # Score berechnen (0 = stark korrodiert, 100 = neuwertig)
    if age_ratio < 0.3:
        score = 95
        risk = "minimal"
    elif age_ratio < 0.6:
        score = 80
        risk = "gering"
    elif age_ratio < 0.8:
        score = 60
        risk = "mittel"
    elif age_ratio < 1.0:
        score = 40
        risk = "erhöht"
    elif age_ratio < 1.5:
        score = 20
        risk = "hoch"
    else:
        score = 5
        risk = "kritisch"

    remaining_years = max(0.0, effective_life_years - yacht_age_years)

    empfehlung = []
    if risk in ("hoch", "kritisch"):
        empfehlung.append(
            f"Scharnier aus {material} am {mount_location} sollte kurzfristig ersetzt werden."
        )
    if material == "stainless_304" and mount_location in ("deck_hatch", "anchor_locker"):
        empfehlung.append(
            "Upgrade auf 316L dringend empfohlen — 304 ist für diese Exposition nicht ausreichend."
        )

    return {
        "score": score,
        "risk_level": risk,
        "effective_life_years": round(effective_life_years, 1),
        "remaining_life_years": round(remaining_years, 1),
        "age_ratio": round(age_ratio, 2),
        "empfehlung": empfehlung,
        "confidence": "calculated",
    }
```

(Confidence: calculated — Formeln basieren auf Stabilus Technical Manual und Industriestandards)

---

## 7. Grundlagen

### 7.1 Gasdruckfedern (Gas Springs / Gas Struts)

#### 7.1.1 Funktionsprinzip

Eine Gasdruckfeder ist ein pneumatisch-mechanisches Federelement:

```
Aufbau einer Gasdruckfeder:
                                                    
  ┌─────────────────────────────────────────────────────┐
  │ Zylinderrohr (Druckbehälter)                        │
  │  ┌─────────────────────────────────────────────────┐│
  │  │ Stickstoff (N₂) unter Druck (50–200 bar)       ││
  │  │                                                 ││
  │  │    ┌─────┐                                      ││
  │  │    │Kolben│═══════════Kolbenstange═══════════►   ││
  │  │    └─────┘                                      ││
  │  │                                                 ││
  │  │ Ölkammer (Dämpfung, ~5–15 ml)                  ││
  │  └─────────────────────────────────────────────────┘│
  │                                                     │
  │  Endstück (Gabelkopf/Kugelkopf)      Endstück      │
  └─────────────────────────────────────────────────────┘
     ▲ Zylinder-Seite                  ▲ Stangen-Seite
     (am Rahmen befestigt)             (am Deckel befestigt)
```

**Physik:**
- Der Gasdruck wirkt auf die Querschnittsfläche der Kolbenstange
- **Ausschubkraft F1** = Gasdruck × Kolbenstangen-Querschnittsfläche
- F1 = p × A = p × (π/4 × d²)
- Beispiel: p = 150 bar, d = 8 mm → F1 = 150 × 10⁵ × π/4 × (0,008)² ≈ 754 N

**Kraft-Weg-Diagramm:**
```
Kraft (N)
  ▲
  │
F2├─────────────────────────────────┐  F2 = Endkraft (max.)
  │                              ╱  │
  │                           ╱     │  Progressionsbereich
  │                        ╱        │  (letzte 10–15% des Hubs)
  │                     ╱           │
F1├──────────────────╱──────────────┤  F1 = Ausschubkraft (Nennkraft)
  │                                 │
  │  Linearer Bereich               │
  │  (80–85% des Hubs)              │
  │                                 │
  └─────────────────────────────────┴──► Hub (mm)
  0                              Stroke
```

**Wichtige Kraftwerte:**
| Bezeichnung | Symbol | Definition | Typischer Wert |
|------------|--------|-----------|----------------|
| Ausschubkraft | F1 | Kraft bei 5 mm ausgefahren | Nennkraft (z.B. 250 N) |
| Reibungskraft | FR | F_dyn - F_stat | 5–15% von F1 |
| Endkraft | F2 | Kraft bei vollem Auszug | F1 × 1,05–1,30 |
| Einfahrkraft | F3 | Kraft zum Zusammendrücken | F1 + FR |
| Dynamische Kraft | F_dyn | Kraft bei Bewegung | F1 + FR/2 |

(Confidence: measured — Stabilus Technical Manual)

#### 7.1.2 Gasdruckfeder-Typen im Yachtbau

| Typ | Beschreibung | Einsatz | Preis (EUR) |
|-----|-------------|---------|-------------|
| **Standard-Zugfeder** | Drückt aus, zieht nicht | Decksluken, Lazarette | 15–90 |
| **Blockierbare Gasfeder** | Arretierbar in beliebiger Position (Freigabe per Knopf/Seilzug) | Motorraumluken, einstellbare Positionen | 40–180 |
| **Edelstahl V4A** | Kolbenstange + Zylinder aus 316/316L | Alle Salzwasser-Anwendungen | 50–150 |
| **Beschichtete Feder** | Stahl mit Zink-Nickel oder Epoxid-Beschichtung | Budget-Option für Süßwasser | 12–35 |
| **Edelstahl mit Endlagendämpfung** | Hydraulische Dämpfung in letzten 10–20 mm | Schwere Lazarette (>25 kg Deckel) | 80–200 |
| **Edelstahl mit PTFE-Kolbenstange** | PTFE-Beschichtung reduziert Reibung und Korrosion | Premium-Yachten | 100–250 |

(Confidence: documented)

#### 7.1.3 Gasdruckfeder-Dimensionierung — Schritt für Schritt

**Schritt 1: Lukendeckel-Gewicht bestimmen**
```
Typische Deckelgewichte:
  - Lewmar Low Profile 40 (397×527 mm):     3,2 kg
  - Lewmar Low Profile 60 (597×597 mm):     5,8 kg
  - Lewmar Ocean 60 (616×616 mm):           7,5 kg
  - Goiot Cristal 42 (420×420 mm):           3,0 kg
  - Lazarette-Deckel GFK 600×800 mm:        12–18 kg
  - Lazarette-Deckel Teak/GFK 800×1000 mm:  25–40 kg
  - Maschinenraum-Luke 1000×1200 mm:        40–80 kg
```

**Schritt 2: Erforderliche Kraft berechnen**
```
F_erforderlich = (m × g × d/2) / (n × L_eff × sin(α)) × SF

Beispiel: Lazarette-Deckel, 25 kg, 800 mm tief, 2 Federn, 15° Einbauwinkel
  F = (25 × 9,81 × 0,4) / (2 × 0,24 × sin(15°)) × 1,3
  F = 98,1 / (2 × 0,24 × 0,2588) × 1,3
  F = 98,1 / 0,1242 × 1,3
  F = 789,9 × 1,3
  F ≈ 1027 N pro Feder → ZU HOCH!

  Lösung: Einbauwinkel auf 25° erhöhen:
  F = 98,1 / (2 × 0,24 × sin(25°)) × 1,3
  F = 98,1 / (2 × 0,24 × 0,4226) × 1,3
  F = 98,1 / 0,2029 × 1,3
  F = 483,5 × 1,3
  F ≈ 629 N pro Feder → Realistisch (z.B. Stabilus Lift-O-Mat 630N)
```

**Schritt 3: Hub bestimmen**
```
Stroke ≈ 2 × R × sin(θ/2)

R = Abstand Befestigungspunkt → Scharnierachse (typisch 200–350 mm)
θ = Öffnungswinkel (typisch 80°–100°)

Beispiel: R = 250 mm, θ = 90°
  Stroke = 2 × 250 × sin(45°) = 500 × 0,7071 = 354 mm
  → Nächste Standard-Hublänge: 350 mm oder 400 mm wählen
```

**Schritt 4: Einbaulänge berechnen**
```
L_eingebaut = Stroke + Zylinderlänge + Endstück-Überstand
L_eingebaut ≈ Stroke × 2,3 bis 2,6 (Faustregel)

Beispiel: Stroke 350 mm → L_eingebaut ≈ 805–910 mm
```

**Schritt 5: Einbaugeometrie prüfen**
- Gasdruckfeder muss bei geschlossener Luke min. 15° Winkel zum Deckel haben
- Kolbenstange IMMER nach unten montieren (damit Öl an der Dichtung bleibt)
- Befestigungspunkte müssen in Spant/Versteifung liegen, nicht in ungestütztem GFK

(Confidence: calculated)

#### 7.1.4 Montage-Regeln (Non-Negotiable)

| Regel | Begründung |
|-------|-----------|
| Kolbenstange IMMER nach unten | Öl schmiert Dichtung; sonst trocknet die Dichtung aus und die Feder verliert innerhalb von 6–12 Monaten Kraft |
| Min. 15° Einbauwinkel bei geschlossener Luke | Unter 15° wird der Hebel so ungünstig, dass die benötigte Federkraft extrem steigt |
| Beide Federn gleichzeitig tauschen | Unterschiedliche Alterung = asymmetrische Kraft = Luke klemmt oder springt auf |
| Endstücke müssen frei schwenken können | Biegemomente auf die Kolbenstange führen zu Undichtigkeit und Bruch |
| Seitenversatz vermeiden | Luke und Federn müssen in einer Ebene liegen; Querbelastung = vorzeitiger Verschleiß |
| Befestigungspunkte verstärken | Kugelkopf-Aufnahme trägt die volle Federkraft konzentriert auf einen Punkt — min. 3 mm GFK/Sperrholz |

(Confidence: documented)

#### 7.1.5 Typische Ausfallmechanismen von Gasdruckfedern

| Ausfallbild | Ursache | Zeitrahmen | Lösung |
|------------|---------|-----------|--------|
| Nachlassende Kraft (Luke hält nicht mehr) | Gasverlust durch Dichtungsverschleiß | 3–8 Jahre | Austausch (nicht reparierbar) |
| Ruckartiges Ausfahren | Kolbenstangen-Korrosion (Pitting) beschädigt Dichtlippe | 2–5 Jahre (Salzwasser, Stahl-Kolbenstange) | Austausch, auf V4A upgraden |
| Feder komplett kraftlos | Gasverlust durch Dichtungsversagen (UV, Alter) | 5–12 Jahre | Austausch |
| Ölverlust (sichtbar an der Kolbenstange) | Dichtung defekt, Überkopf-Montage | 1–5 Jahre | Austausch + korrekte Montage |
| Endstück abgebrochen | Materialermüdung (Zamak-Guss), Überbelastung | 3–10 Jahre | Austausch + auf geschmiedete Endstücke upgraden |
| Luke springt unkontrolliert auf | Feder zu stark (falsches Modell oder Temperaturanstieg bei Hitze) | sofort oder saisonal | Kraft prüfen, ggf. schwächere Feder montieren |
| Luke schließt nicht vollständig | Feder zu stark bei geschlossener Position | sofort | Geometrie prüfen, ggf. Befestigungspunkt versetzen |

(Confidence: documented)

### 7.2 Scharniere (Hinges)

#### 7.2.1 Scharnier-Typen im Yachtbau

**7.2.1.1 Stangenscharnier / Klavierband (Piano Hinge)**

```
Querschnitt:
        ┌──────┐   ┌──────┐
        │      │   │      │
   ─────┤ Flügel│──●│Flügel├─────
        │  A   │ ↑ │  B   │
        │      │Stift     │
        └──────┘   └──────┘

● = Durchgehender Scharnierstift
```

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L, 304, Messing, Aluminium |
| Breite aufgeklappt | 30–100 mm |
| Stift-∅ | 3,2–6,4 mm |
| Stärke | 0,8–2,5 mm (Blatt) |
| Lieferbar als | Stangenmeter (bis 3660 mm), zugeschnitten |
| Vorteil | Gleichmäßige Lastverteilung, kostengünstig, einfach zu kürzen |
| Nachteil | Viele Befestigungspunkte nötig, schwer zu ersetzen wenn einlaminiert |
| Typischer Einsatz | Lazarette-Deckel, Stauklappen, Cockpit-Sitzpolster-Deckel |
| Preise (316L) | 15–30 EUR/m (Standard), 40–70 EUR/m (schwere Ausführung) |

**Hersteller & Artikel:**
- Suncor S0721-0100 (316L, 50×1,2 mm offen, Stift 3,2 mm, lose Stiftversion): 22 EUR/m
- Osculati 38.659.00 (316L, 40×1,0 mm): 18 EUR/m
- Sea-Dog 201580 (304, 50×1,5 mm): 15 EUR/m
- Perko 0726DP0STS (316, 60×1,5 mm, vorgebohrt alle 50 mm): 35 EUR/m

(Confidence: documented)

**7.2.1.2 Stumpfscharnier (Butt Hinge)**

```
Draufsicht:
  ┌──────────────┐
  │  ○   ○   ○  │  ← Befestigungslöcher
  │              │
  ├──────●───────┤  ← Scharnierachse
  │              │
  │  ○   ○   ○  │
  └──────────────┘
```

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L, Bronze (Silizium oder Mangan), Messing verchromt |
| Größen | 38×38 mm bis 100×100 mm (Einzelblatt) |
| Stift-∅ | 4–8 mm |
| Stärke | 1,5–3,0 mm |
| Vorteil | Kompakt, robuster Stift, austauschbar |
| Nachteil | Punktuelle Belastung der Befestigungslöcher |
| Typischer Einsatz | Decksluken (paarweise), Maschinenraumluken, schwere Klappen |
| Preise (316L) | 8–35 EUR/Stück (je nach Größe) |

**Hersteller & Artikel:**
- Suncor S3413-0400 (316L, 102×76 mm, 4-Loch, Stift 6,3 mm): 28 EUR
- Osculati 38.830.04 (316L, 100×75 mm, verstärkt): 22 EUR
- Sea-Dog 204560 (304, 63×50 mm): 9 EUR
- Perko 1293DP0CHR (Messing verchromt, 76×63 mm): 18 EUR

(Confidence: documented)

**7.2.1.3 Bandscharnier / Laschenscharnier (Strap Hinge)**

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L, Bronze, geschmiedeter Edelstahl |
| Größen | 150–400 mm Gesamtlänge |
| Stift-∅ | 6–10 mm |
| Vorteil | Langer Hebelarm = weniger Befestigungspunkte, sehr hohe Belastbarkeit |
| Nachteil | Sichtbar, schwerer, teurer |
| Typischer Einsatz | Schwere Luken, Motorraumluken, traditionelle Yachten |
| Preise (316L) | 35–120 EUR/Stück |

**Hersteller & Artikel:**
- Suncor S3827-0600 (316L, 152 mm, T-Strap): 45 EUR
- Osculati 38.845.02 (316L, 200 mm, verstärkt): 38 EUR
- Perko 1248DP0STS (316, 254 mm): 55 EUR

(Confidence: documented)

**7.2.1.4 Verdecktes Scharnier (Concealed Hinge)**

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L, Alu-Druckguss, Messing |
| Größen | 50–120 mm Einbaubreite |
| Vorteil | Nicht sichtbar bei geschlossener Luke, ästhetisch, kein Stolperrisiko |
| Nachteil | Komplexe Montage, aufwendiger Austausch, geringere Belastbarkeit |
| Typischer Einsatz | Innenluken (Kabinensole), hochwertige Yachten, Portlight-Rahmenscharniere |
| Preise | 25–80 EUR/Stück |

**Hersteller & Artikel:**
- Southco C5-21 (316L, einstellbar, max. 12 kg pro Scharnier): 45 EUR
- Sugatsune HG-CHA-10 (Marine-grade, max. 15 kg): 52 EUR
- Osculati 38.930.00 (Zamak verchromt, verdeckt, max. 8 kg): 18 EUR

(Confidence: documented)

**7.2.1.5 Reibungsscharnier (Friction Hinge / Torque Hinge)**

```
Funktionsprinzip:
  ┌──────────────────────┐
  │  Feder-Scheiben       │
  │  erzeugen Reibung     │
  │  an der Achse →       │
  │  Luke hält in         │
  │  jeder Position       │
  └──────────────────────┘
```

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L mit PTFE/POM-Buchsen, Federstahl |
| Drehmoment | 0,5–8,0 Nm (einstellbar oder fest) |
| Vorteil | Hält Luke stufenlos in jeder Position, keine Gasdruckfeder nötig |
| Nachteil | Begrenzte Belastung (typisch < 10 kg), Drehmoment lässt mit der Zeit nach |
| Typischer Einsatz | Portlights, leichte Decksluken, Schranktüren |
| Preise | 15–60 EUR/Stück |

**Hersteller & Artikel:**
- Southco E6-10-301-50 (316L, 3,0 Nm, max. 90°): 35 EUR
- Southco E6-10-501-50 (316L, 5,0 Nm, max. 90°): 42 EUR
- Reell HT-4102-117 (Marine-Serie, 2,5 Nm, einstellbar): 48 EUR
- Lewmar 89100054 (Reibungsscharnier für Size 40 Portlight): 32 EUR

(Confidence: documented)

**7.2.1.6 Aushängescharnier (Lift-Off Hinge)**

| Eigenschaft | Wert |
|------------|------|
| Materialien | 316L, Bronze |
| Vorteil | Luke komplett abnehmbar, Wartungszugang |
| Nachteil | Sicherungsbolzen nötig gegen unbeabsichtigtes Aushängen |
| Typischer Einsatz | Maschinenraumluken (Wartung), Ausrüstungsluken |
| Preise (316L) | 20–50 EUR/Stück |

**Hersteller & Artikel:**
- Suncor S3816-0500 (316L, 127×76 mm, linkshand/rechtshand): 32 EUR
- Osculati 38.840.01 (316L, 100×62 mm): 22 EUR
- Sea-Dog 204600 (304, 89×51 mm): 12 EUR

(Confidence: documented)

#### 7.2.2 Scharnier-Materialvergleich für Yachten

| Material | Zugfestigkeit (MPa) | Korrosion (Salzwasser) | Gewicht (rel.) | Preis (rel.) | Empfehlung |
|----------|---------------------|----------------------|----------------|-------------|------------|
| 316L Edelstahl | 485–560 | Sehr gut (PREN 24) | 1,0 | 1,0 | Standard für Seewasser |
| 316 Edelstahl | 515–620 | Gut (PREN 24) | 1,0 | 0,95 | Akzeptabel; 316L bevorzugt wegen niedrigerem C |
| 304 Edelstahl | 515–620 | Mittel (PREN 18) | 1,0 | 0,65 | Nur Süßwasser/Ostsee; Salzwasser: Tea-Staining nach 2–4 Jahren |
| Silizium-Bronze | 475–690 | Ausgezeichnet | 1,07 | 1,8 | Traditionelle Yachten; beste Korrosionsbeständigkeit |
| Messing verchromt | 340–400 | Mäßig (Entzinkung!) | 1,07 | 0,7 | Nur Innenbereich; Entzinkung ab Bj. 3–5 bei Salzluft |
| Alu eloxiert | 240–310 | Gut (wenn Eloxierung intakt) | 0,34 | 0,5 | Leichtbau; NICHT zusammen mit Edelstahl (galvanisch) |
| Titan Grade 5 | 830–1100 | Perfekt (PREN >40) | 0,57 | 5,0 | Racing/Superyachten; keine galvanischen Probleme |

**PREN** = Pitting Resistance Equivalent Number = %Cr + 3,3×%Mo + 16×%N

(Confidence: measured)

#### 7.2.3 Galvanische Korrosion bei Scharnier-Materialpaarungen

**Spannungsreihe im Seewasser (Auszug):**
```
Aktiv (anodisch, korrodiert zuerst)
  │ Zink / verzinkter Stahl     -1,03 V
  │ Aluminium                    -0,76 V
  │ Stahl (unbehandelt)          -0,60 V
  │ Blei                         -0,55 V
  │ Messing                      -0,30 V
  │ Bronze (Silizium)            -0,26 V
  │ Kupfer                       -0,36 V
  │ Edelstahl 304 (passiv)       -0,08 V
  │ Edelstahl 316 (passiv)       -0,05 V
  │ Titan                        -0,05 V
  │ Graphit / Carbon             +0,25 V
  ▼
Edel (kathodisch, geschützt)
```

**Kritische Kombinationen im Lukenbau:**

| Kombination | ΔV | Risiko | Praxis-Beispiel |
|------------|-----|--------|----------------|
| Edelstahl-Scharnier + Alu-Lukenrahmen | ~0,7 V | HOCH | Lewmar-Luke in Alu-Deckshaus — Isolierung zwingend! |
| Bronze-Scharnier + Alu-Aufbau | ~0,5 V | HOCH | Traditionelle Bronze-Beschläge auf Alu-Yacht |
| 316L-Schrauben + 304-Scharnier | ~0,03 V | Minimal | Akzeptabel, gleiches Grundmaterial |
| Edelstahl + Teak-Unterlage | ~0,0 V | Keines | Teak isoliert galvanisch (organisch) |
| Edelstahl + Carbon-Lukendeckel | ~0,3 V | MITTEL | Carbon ist kathodisch; Edelstahl korrodiert beschleunigt |

**Gegenmaßnahmen:**
1. Kunststoff-Unterlegscheiben (POM, PTFE, Nylon) als Isolation
2. Teflonhülsen in Befestigungslöchern
3. Gleiches Material für alle metallischen Kontaktflächen
4. Duralac oder Tef-Gel auf Kontaktflächen (galvanischer Inhibitor)

(Confidence: measured)

### 7.3 Verschlüsse und Riegel (Latches and Locks)

#### 7.3.1 Verschluss-Typen

**7.3.1.1 Nocken-Riegel / Cam Latch**

Der am weitesten verbreitete Luken-Verschluss im Yachtbau.

```
Funktionsprinzip (Querschnitt):

    Geöffnet:                    Geschlossen:
    
    ┌──────Luke──────┐           ┌──────Luke──────┐
    │     ╱──╲       │           │    ╱────╲      │
    │    ╱ Cam╲      │           │   ╱ Cam  ╲─────┤ ← Cam drückt auf
    │   ╱      ╲     │           │  ╱        ╲    │    Lukenrahmen
    │  ●        │    │           │  ●─────────╲───┤
    ├──Achse────┤    │           ├──Achse─────────┤
    │           │    │           │           Rahmen│
    └───────────┘    │           └─────────────────┘
                 Griff dreht                Dichtung komprimiert
                 Cam nach oben              durch Cam-Kontur
```

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 100–400 N (abhängig von Cam-Kontur und Hebelarm) |
| Materialien | 316L, Bronze, Polyamid |
| Abschließbar | Optional (mit Schloss-Einsatz) |
| Einhand-Bedienung | Ja |
| Bündig | Optional (Flush-Mount-Versionen) |
| Typischer Einsatz | Decksluken (Lewmar, Goiot, Gebo), Lazarette, Cockpit-Luken |

**Hersteller & Artikel:**
- Lewmar 89400066 (Cam-Latch für Size 40–70, 316L): 38 EUR
- Lewmar 89400090 (Cam-Latch für Ocean-Serie, 316L): 45 EUR
- Southco M1-43-31 (Flush-Cam-Latch, 316L, abschließbar): 52 EUR
- Perko 1092DP0CHR (Cam-Latch, Messing verchromt): 22 EUR

(Confidence: documented)

**7.3.1.2 Kompressionsverschluss (Compression Latch)**

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 200–800 N (durch Drehbewegung erzeugt) |
| Materialien | 316L, glasfaserverstärktes Polyamid |
| Merkmal | Zieht Luke aktiv zum Rahmen (im Gegensatz zu Cam, der drückt) |
| Abschließbar | Häufig integriert |
| Typischer Einsatz | Maschinenraumluken, Lazarette mit hoher Dichtungsanforderung |

**Hersteller & Artikel:**
- Southco E3-5-31 (316L, Compression Latch, 500 N Anpresskraft): 65 EUR
- Southco E5-10-301-40 (316L, Mini-Compression, bündig, abschließbar): 48 EUR
- Perko 0931DP0CHR (Compression, Messing verchromt, abschließbar): 35 EUR

(Confidence: documented)

**7.3.1.3 Vierteldrehverschluss (Quarter-Turn Latch)**

```
Funktionsprinzip:
  90°-Drehung eines Riegels verriegelt/entriegelt die Luke.
  
  Offen:    Geschlossen:
  ──        │
  │         │
  │         ──
```

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 50–300 N |
| Materialien | 316L, Zamak verchromt, Polyamid |
| Merkmal | Schnelles Öffnen/Schließen, eine Vierteldrehung |
| Bündig | Fast immer (Flush-Mount Standard) |
| Typischer Einsatz | Stauklappen, Instrumententafel-Abdeckungen, kleine Luken |

**Hersteller & Artikel:**
- Southco 62-10-25 (316L, Flush Quarter-Turn, ∅22 mm Ausschnitt): 18 EUR
- Southco 62-10-35 (316L, Flush Quarter-Turn, abschließbar): 28 EUR
- Perko 1092DP0STS (316, Quarter-Turn mit Schlüssel): 32 EUR
- Osculati 38.180.00 (Zamak verchromt, Quarter-Turn): 8 EUR
- Sea-Dog 221840 (316L, Quarter-Turn, ∅25 mm): 15 EUR

(Confidence: documented)

**7.3.1.4 Kniehebelverschluss / Toggle Latch (Spannverschluss)**

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 300–2000 N (durch Kniehebel-Übersetzung) |
| Materialien | 316L, verzinkter Stahl |
| Merkmal | Höchste Anpresskraft aller Verschlusstypen; einstellbar über Gegenhalter |
| Typischer Einsatz | Maschinenraumluken, Tankzugangsluken, CE Kat A Seeluken |

**Hersteller & Artikel:**
- Southco 40-11-101-20 (316L, verstellbar, 600 N): 42 EUR
- De Sta Co 323 (316, Toggle Latch, Industrieausführung, 1800 N): 65 EUR
- Osculati 38.170.01 (316L, einstellbar, 400 N): 25 EUR

(Confidence: documented)

**7.3.1.5 Schnappschloss / Slam Latch**

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 50–200 N |
| Materialien | 316L, Polyamid |
| Merkmal | Federbelastet, schnappt beim Schließen automatisch ein |
| Typischer Einsatz | Cockpit-Staufächer, Bordküchen-Klappen |

**Hersteller & Artikel:**
- Southco C2-32-15 (316L, Push-to-Close, bündig): 22 EUR
- Sea-Dog 221910 (316L, Slam-Latch, federgespannt): 18 EUR
- Perko 0960DP0STS (316, Slam-Latch): 15 EUR

(Confidence: documented)

#### 7.3.2 Dog-Verschlüsse (Dog Bolts)

Dog-Verschlüsse sind Schraubverschlüsse, die den Lukendeckel gegen den Dichtungsrahmen pressen. Sie sind typisch für schwere, wasserdichte Luken (Maschinenraum, Blauwasser).

| Eigenschaft | Wert |
|------------|------|
| Anpresskraft | 500–3000 N pro Dog |
| Materialien | 316L, Bronze |
| Typische Anzahl pro Luke | 4–8 (abhängig von Lukengröße und CE-Kategorie) |
| Typischer Einsatz | Schwere Decksluken, Maschinenraumluken, Watertight-Doors |

**Berechnung Anzahl Dogs:**
```
N_dogs = max(4, ceil(U / 400))

U = Lukenumfang in mm
400 mm = empfohlener Maximalabstand zwischen Dogs

Beispiel: Luke 800×1000 mm → U = 3600 mm → N = ceil(3600/400) = 9 Dogs
```

**Hersteller & Artikel:**
- Freeman Marine (Custom Dog-Bolts für Superyachten): auf Anfrage
- New Found Metals 01-130 (Bronze Dog, ∅16 mm Bolzen): 85 EUR
- Osculati 38.196.00 (316L, Dog-Bolt, M10): 18 EUR

(Confidence: documented)

#### 7.3.3 Schlösser (Locks)

| Typ | Materialien | Anwendung | Preise | Hersteller/Artikel |
|-----|------------|-----------|--------|-------------------|
| Zylinderschloss (Barrel Lock) | 316L, Messing verchromt | Lazarette, Ankerkästen | 15–45 EUR | Perko 0927DP0STS, Southco E3-5-31 |
| Schlüsselschloss (Key Lock) | 316L, Messing | Maschinenraum, Tankluken | 25–80 EUR | Southco E5-10-301-50, Perko 0927DP0CHR |
| Kombinationsschloss | Zamak, 316L | Charter-Yachten, Beiboottaschen | 20–60 EUR | Sea-Dog 221830, Osculati 38.137.00 |
| Push-Button-Lock | 316L, Polyamid | Innenluken, Schranktüren | 10–35 EUR | Southco 93-10-301, Sugatsune MC-32 |

**Sicherheitshinweis:** Schlösser an Fluchtluken (escape hatches) dürfen NIEMALS die Notentriegelung von innen blockieren. ISO 12216 verlangt: Von innen immer ohne Schlüssel und Werkzeug öffenbar.

(Confidence: measured)

### 7.4 Griffe und Handhabungen (Handles)

#### 7.4.1 Grifftypen

| Typ | Beschreibung | Überstand (mm) | Stolpergefahr | Anwendung |
|-----|-------------|---------------|-------------|-----------|
| Einlassgriff (Flush Pull) | Bündig in Lukendeckel eingelassen | 0 | Keine | Decksluken, Cockpit — Standard |
| Zuggriff (Pull Handle) | Bügel auf Lukenoberfläche | 15–40 | JA (ISO 15085!) | Innenluken, geschützte Bereiche |
| T-Griff | T-förmiger Dreh-/Zuggriff | 20–50 | JA | Maschinenraumluken (geschraubt) |
| Ringgriff (Ring Pull) | Versenkbarer Ring | 0 (versenkt) – 25 (ausgeklappt) | Gering | Lazarette, Staufächer |
| Muldengriff | Muldenförmige Vertiefung im Deckel | 0 (vertieft) | Keine | Cockpit-Luken, hochwertige Yachten |

**ISO 15085 Relevanz:** Griffe auf begehbaren Decksflächen dürfen max. 25 mm über die Oberfläche ragen, um Stolpergefahr zu minimieren. Einlassgriffe (0 mm) sind bevorzugt.

**Hersteller & Artikel:**
- Lewmar 89400080 (Flush Pull für Low Profile + Ocean-Luken, 316L): 28 EUR
- Southco M5-92-301-8 (Flush Pull, 316L, 76×57 mm Einbau): 22 EUR
- Osculati 38.150.01 (Ring Pull, 316L, ∅55 mm): 12 EUR
- Perko 1232DP0STS (Flush Pull, 316, 89×64 mm): 18 EUR
- Sea-Dog 221560 (Ring Pull, 316L, versenkbar): 15 EUR

(Confidence: documented)

### 7.5 Haltevorrichtungen (Stays / Hold-Open Devices)

#### 7.5.1 Kettenstays

```
Funktionsprinzip:
                    Luke (geöffnet)
                   ╱
                  ╱
                 ╱  ← Kette begrenzt
                ╱      Öffnungswinkel
               ╱
    ──────────●──────────
              Deck
```

| Eigenschaft | Wert |
|------------|------|
| Material | 316L Kette + 316L Endplatten |
| Kettenglied | 4–6 mm Drahtstärke |
| Vorteil | Robust, einfach, keine mechanische Ermüdung |
| Nachteil | Keine Stufenlose Einstellung, klappert bei Seegang |
| Anwendung | Lazarette, Ankerkästen, einfache Decksluken |
| Preise | 10–30 EUR |

**Hersteller & Artikel:**
- Osculati 38.700.00 (316L, Kette 5 mm × 300 mm, mit Schraubplatten): 18 EUR
- Sea-Dog 321860 (316L, Kettenstay 350 mm): 15 EUR

(Confidence: documented)

#### 7.5.2 Reibungsstays (Friction Stays / Lid Stays)

| Eigenschaft | Wert |
|------------|------|
| Material | 316L Arme + Federstahl/PTFE-Reibelement |
| Haltekraft | 3–20 kg (je nach Modell) |
| Vorteil | Hält Luke stufenlos in jeder Position |
| Nachteil | Haltekraft lässt nach (PTFE-Verschleiß); begrenzte Lebensdauer 5.000–15.000 Zyklen |
| Anwendung | Decksluken, Motorraumluken (als Backup zu Gasdruckfeder) |
| Preise | 20–60 EUR |

**Hersteller & Artikel:**
- Lewmar 14998001 (Friction Stay für Size 40/44, 316L, 5 kg): 35 EUR
- Lewmar 14998002 (Friction Stay für Size 50/54, 316L, 8 kg): 42 EUR
- Osculati 38.695.00 (Reibungsstay, 316L, 250 mm, 10 kg): 28 EUR

(Confidence: documented)

#### 7.5.3 Teleskopstays

| Eigenschaft | Wert |
|------------|------|
| Material | 316L Rohre, POM-Gleitbuchsen |
| Vorteil | Einstellbare Öffnungsweite, robust |
| Nachteil | Teurer, schwerer, sperriger als Gasdruckfeder |
| Anwendung | Schwere Maschinenraumluken (als Backup oder Haupthalter) |
| Preise | 40–120 EUR |

**Hersteller & Artikel:**
- Vetus STAYLONG (Teleskopstay, 316L, 300–500 mm einstellbar): 65 EUR
- Osculati 38.696.30 (Teleskopstay, 316L, 280–450 mm): 45 EUR

(Confidence: documented)

### 7.6 Kraftberechnungen — Zusammenfassung

#### 7.6.1 Gasdruckfeder-Kraft (detailliert)

```python
# Erweiterte Berechnungsfunktion mit Winkelabhängigkeit

def gas_strut_force_detailed(
    mass_kg: float,          # Deckelmasse
    depth_mm: float,         # Lukentiefe (Öffnungsrichtung)
    angle_open_deg: float,   # Gewünschter Öffnungswinkel
    pivot_to_strut_mm: float,  # Abstand Scharnier → Feder-Befestigung am Rahmen
    lid_strut_attach_mm: float,  # Abstand Scharnier → Feder-Befestigung am Deckel
    n_struts: int = 2,
    safety_factor: float = 1.3,
) -> dict:
    """
    Berechnet die benötigte Gasdruckfeder-Kraft unter Berücksichtigung
    der exakten Einbaugeometrie.
    
    Drehmoment-Gleichgewicht um Scharnierachse:
      M_gewicht = M_feder
      m × g × (d/2) × cos(φ) = n × F × r₁ × sin(α)
    
    wobei:
      φ = aktueller Lukenwinkel
      r₁ = Abstand Scharnier → Feder-Befestigungspunkt am Deckel
      α = Winkel der Feder zum Deckel
    """
    import math
    g = 9.81
    
    # Worst case: Lukenwinkel = 0° (geschlossen, cos(0) = 1)
    m_weight = mass_kg * g * (depth_mm / 1000 / 2)  # Nm
    
    # Effektiver Hebelarm der Feder
    r1 = lid_strut_attach_mm / 1000  # m
    
    # Winkel der Feder bei geschlossener Luke (geometrisch)
    alpha_rad = math.atan2(pivot_to_strut_mm, lid_strut_attach_mm)
    
    force = m_weight / (n_struts * r1 * math.sin(alpha_rad)) * safety_factor
    
    return {
        "force_per_strut_n": round(force, 0),
        "total_force_n": round(force * n_struts, 0),
        "lever_arm_weight_mm": depth_mm / 2,
        "lever_arm_strut_mm": round(r1 * math.sin(alpha_rad) * 1000, 1),
        "strut_angle_deg": round(math.degrees(alpha_rad), 1),
    }
```

#### 7.6.2 Schnellreferenz: Kraft nach Lukengewicht

| Deckelgewicht (kg) | 2 Federn, 15° Winkel (N/Feder) | 2 Federn, 25° Winkel (N/Feder) | 2 Federn, 35° Winkel (N/Feder) |
|--------------------|-------------------------------|-------------------------------|-------------------------------|
| 3 | 95 | 57 | 41 |
| 5 | 159 | 96 | 69 |
| 8 | 254 | 153 | 110 |
| 10 | 318 | 191 | 137 |
| 15 | 477 | 287 | 206 |
| 20 | 636 | 383 | 275 |
| 25 | 795 | 479 | 344 |
| 30 | 954 | 574 | 412 |
| 40 | 1272 | 766 | 550 |
| 50 | 1590 | 957 | 687 |

**Lesehinweis:** 15° Einbauwinkel ist typisch für nachgerüstete Gasdruckfedern mit wenig Platz. 25° ist der Standardwert für gute Geometrie. 35° ist optimal, erfordert aber ausreichend Tiefe unter dem Deck.

(Confidence: calculated)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Lewmar (Havant, UK) — Luken-Zubehör und Griffe

**Unternehmensprofil:**
- Gegründet: 1946
- Hauptsitz: Havant, Hampshire, UK
- Spezialität: Luken, Portlights, Winschen, Steuerungssysteme
- Marktposition: Globaler Marktführer für Yacht-Luken (geschätzt 40–50% Marktanteil bei Serienyachten)

**Lukenprogramm (für Beschlag-Zuordnung):**

| Serie | Typ | Größen | Merkmale |
|-------|-----|--------|----------|
| Low Profile | Decksluke | Size 10–70 | Flaches Profil (22–27 mm), Acryl, integrierter Cam-Latch |
| Ocean | Decksluke | Size 00–70 | Höheres Profil, robuster, CE Kat A |
| Flush | Decksluke | Size 40–70 | Bündig mit Deck, Teak-Inlay möglich |
| Medium Profile | Decksluke | Size 40–70 | Mittleres Profil, gutes Preis-Leistungs-Verhältnis |
| Portlights | Portlight | Size 1–7 | Feststehend oder öffnend, Reibungsscharnier |

**Beschlag-Sortiment:**

| Kategorie | Artikel | Artikelnummer | Preis (EUR) | Beschreibung |
|-----------|---------|---------------|-------------|-------------|
| Gasdruckfeder | Standard 120N, 250mm | 89500100 | 45 | 304 Edelstahl, Kugelkopf ∅10mm |
| Gasdruckfeder | Standard 200N, 305mm | 89500200 | 52 | 304 Edelstahl, Kugelkopf ∅10mm |
| Gasdruckfeder | Standard 300N, 355mm | 89500300 | 58 | 304 Edelstahl, Kugelkopf ∅10mm |
| Gasdruckfeder | Heavy-Duty 500N, 400mm | 89500500 | 78 | 316L Edelstahl, Kugelkopf ∅13mm |
| Cam-Latch | Low Profile Handle | 89400066 | 38 | 316L, für Size 40–70 |
| Cam-Latch | Ocean Handle | 89400090 | 45 | 316L, für Ocean-Serie |
| Flush Pull | Einlassgriff LP | 89400080 | 28 | 316L, 76×57mm Einbau |
| Reibungsscharnier | Friction Stay S40 | 14998001 | 35 | 316L, 5 kg Haltekraft |
| Reibungsscharnier | Friction Stay S54 | 14998002 | 42 | 316L, 8 kg Haltekraft |
| Ersatzfeder | Luken-Aufstellfeder | 89500101 | 12 | Ersatz-Torsionsfeder für Aufstellmechanismus |
| Moskitonetz | Flyscreen für Size 40 | 39940030 | 68 | Magnetischer Rahmen, Clip-Befestigung |
| Moskitonetz | Flyscreen für Size 60 | 39960030 | 78 | Magnetischer Rahmen, Clip-Befestigung |

**Zuordnung Lewmar-Luke → Gasdruckfeder:**

| Lukenmodell | Empfohlene Gasdruckfeder | Kraft (N) | Hub (mm) | Einbaulänge (mm) |
|------------|------------------------|-----------|----------|-----------------|
| Low Profile 40 | 89500100 | 120 | 180 | 432 |
| Low Profile 54 | 89500100 | 120 | 180 | 432 |
| Low Profile 60 | 89500200 | 200 | 250 | 584 |
| Low Profile 70 | 89500200 | 200 | 250 | 584 |
| Ocean 40 | 89500200 | 200 | 250 | 584 |
| Ocean 54 | 89500200 | 200 | 250 | 584 |
| Ocean 60 | 89500300 | 300 | 305 | 712 |
| Ocean 70 | 89500300 | 300 | 305 | 712 |

(Confidence: documented)

### 8.2 Goiot / Bénéteau Group (Challans, Frankreich) — Lukenbeschläge

**Unternehmensprofil:**
- Marke der Bénéteau-Gruppe (OEM für Bénéteau, Jeanneau, Lagoon, Prestige)
- Spezialität: Luken, Portlights, Schiebedächer
- Marktposition: Zweitgrößter Lukenhersteller weltweit (OEM-dominiert)

**Beschlag-Sortiment:**

| Kategorie | Artikel | Artikelnummer | Preis (EUR) | Beschreibung |
|-----------|---------|---------------|-------------|-------------|
| Gasdruckfeder | Cristal 20 | GAS-CR20 | 38 | 100N, 200mm Hub, Gabelkopf M8 |
| Gasdruckfeder | Cristal 42 | GAS-CR42 | 45 | 150N, 250mm Hub, Gabelkopf M8 |
| Gasdruckfeder | Opal 42 | GAS-OP42 | 52 | 200N, 280mm Hub, Gabelkopf M8 |
| Cam-Latch | Cristal-Griff | 32120 | 32 | Polyamid, UV-stabilisiert, weiß |
| Cam-Latch | Opal-Griff | 32240 | 42 | 316L + Polyamid-Einlage |
| Scharnier | Cristal Integral-Scharnier | 31100 | (OEM, nicht einzeln) | Im Lukenrahmen integriert |
| Verriegelung | Zusätzlicher Sicherheitsriegel | 32500 | 28 | Für CE Kat A/B Nachrüstung |
| Moskitonetz | Moustiquaire Cristal 42 | 39042 | 55 | Federgespannter Rahmen |

**Hinweis Goiot:** Goiot-Luken verwenden proprietäre Endstücke (Gabelkopf M8 mit ∅6 mm Bolzen). Universelle Kugelkopf-Gasdruckfedern passen NICHT ohne Adapter.

(Confidence: documented)

### 8.3 Suspa (Altdorf bei Nürnberg, Deutschland) — Gasdruckfedern

**Unternehmensprofil:**
- Gegründet: 1951
- Hauptsitz: Altdorf bei Nürnberg, Bayern
- Spezialität: Gasdruckfedern, Dämpfer, Verstellsysteme
- Marktposition: Einer der weltweit größten Gasdruckfeder-Hersteller (Automobilindustrie + Industrie)
- Marine-Relevanz: Standard-Industriefedern werden im Yachtbau eingesetzt; keine dedizierte Marine-Linie, aber V4A-Optionen im Konfigurator

**Produktprogramm (marine-relevant):**

| Serie | Typ | Kraftbereich | Hub | Material | Preis (EUR) |
|-------|-----|-------------|-----|----------|------------|
| Liftline C16-06 | Standard | 50–500 N | 60–300 mm | Stahl + Chromstange | 12–35 |
| Liftline C16-08 | Standard, schwer | 200–1200 N | 80–500 mm | Stahl + Chromstange | 18–55 |
| Liftline C16-V4A | Edelstahl | 50–800 N | 60–400 mm | 316 Zylinder + V4A Stange | 45–120 |
| Hydrolift HL-03 | Gedämpft | 100–600 N | 80–350 mm | Stahl oder V4A | 65–180 |
| Lockline LL-04 | Blockierbar | 150–1000 N | 100–500 mm | Stahl oder V4A | 55–200 |

**Konfigurator-Optionen:**
- Online-Konfigurator: suspa.com/konfigurator
- Endstücke: Kugelkopf (∅8, ∅10, ∅13 mm), Gabelkopf (M6, M8, M10), Öse, Gewinde
- Oberflächenbehandlung: Standard (Lack), Zink-Nickel, Chrom, Edelstahl V4A
- Temperaturbereich: Standard (-30°C bis +80°C), Niedertemperatur (bis -40°C), Hochtemperatur (bis +120°C)

**Technische Daten Liftline C16-V4A (marine-empfohlen):**

| Parameter | Wert |
|-----------|------|
| Zylinder-∅ | 15 mm |
| Kolbenstangen-∅ | 6 mm |
| Nennkraft-Toleranz | ±5% bei 20°C |
| Temperaturdrift | ±0,34%/°C |
| Lebensdauer | ≥50.000 Zyklen (garantiert) |
| Betriebstemperatur | -30°C bis +80°C |
| Gasfüllung | Stickstoff (N₂), ölgedämpft |
| Korrosionsbeständigkeit | Salzsprühtest DIN EN ISO 9227: >1000 h (V4A) |

(Confidence: measured — Suspa TDS)

### 8.4 Stabilus (Koblenz, Deutschland) — Lift-O-Mat

**Unternehmensprofil:**
- Gegründet: 1934
- Hauptsitz: Koblenz, Rheinland-Pfalz
- Spezialität: Gasdruckfedern (Erfinder der modernen Gasdruckfeder, 1953)
- Börsennotiert: XETRA (STM)
- Marktposition: Weltmarktführer Gasdruckfedern (2,5 Mrd. Stück/Jahr über alle Branchen)
- Marine-Relevanz: Lift-O-Mat ist die bekannteste Marke im Yachtbereich; verfügbar über SVB, Toplicht, West Marine

**Produktprogramm Lift-O-Mat (marine-relevant):**

| Artikelnummer | Kraft (N) | Hub (mm) | Einbaulänge (mm) | Endstück | Material | Preis (EUR) |
|--------------|-----------|----------|-----------------|----------|----------|------------|
| 082388 | 100 | 80 | 215 | Kugelkopf ∅10/M6 | Stahl + Cr | 22 |
| 084040 | 150 | 120 | 310 | Kugelkopf ∅10/M6 | Stahl + Cr | 25 |
| 084844 | 200 | 160 | 400 | Kugelkopf ∅10/M8 | Stahl + Cr | 28 |
| 085569 | 250 | 200 | 485 | Kugelkopf ∅10/M8 | Stahl + Cr | 32 |
| 086590 | 300 | 250 | 590 | Kugelkopf ∅10/M8 | Stahl + Cr | 35 |
| 094468 | 250 | 250 | 580 | Kugelkopf ∅10/M8 | V4A Edelstahl | 89 |
| 094472 | 350 | 300 | 690 | Kugelkopf ∅10/M8 | V4A Edelstahl | 98 |
| 094488 | 500 | 350 | 810 | Kugelkopf ∅13/M10 | V4A Edelstahl | 115 |
| 094501 | 750 | 400 | 930 | Kugelkopf ∅13/M10 | V4A Edelstahl | 135 |
| 094515 | 1000 | 400 | 940 | Gabelkopf M10 | V4A Edelstahl | 155 |

**Lift-O-Mat DAMP (mit Endlagendämpfung):**

| Artikelnummer | Kraft (N) | Hub (mm) | Dämpfung | Material | Preis (EUR) |
|--------------|-----------|----------|---------|----------|------------|
| 096200 | 300 | 250 | 10 mm Endlage | V4A | 125 |
| 096220 | 500 | 350 | 15 mm Endlage | V4A | 145 |
| 096240 | 750 | 400 | 20 mm Endlage | V4A | 168 |

**Technische Daten Lift-O-Mat (V4A-Serie):**

| Parameter | Wert |
|-----------|------|
| Zylinder-∅ | 15 mm (bis 500 N), 19 mm (über 500 N) |
| Kolbenstangen-∅ | 6 mm (bis 300 N), 8 mm (bis 750 N), 10 mm (ab 1000 N) |
| Nennkraft-Toleranz | ±5% bei 20°C |
| Temperaturdrift | +0,34%/°C (bei Erwärmung steigt Kraft) |
| Lebensdauer | ≥50.000 Zyklen (bei Nennbedingungen) |
| Gasfüllung | N₂ + Öl (5–15 ml) |
| Einbaulage | Kolbenstange nach unten (empfohlen) — bei Über-Kopf-Montage Lebensdauer ≈ 50% |
| Korrosionsbeständigkeit (V4A) | Salzsprühtest >1500 h (DIN EN ISO 9227) |
| Gewicht (V4A, 250N/250mm) | ~210 g |

**Zubehör (Stabilus):**

| Artikel | Artikelnummer | Preis (EUR) | Beschreibung |
|---------|---------------|-------------|-------------|
| Kugelkopf-Aufnahme | 9066MK | 8 | Clip-Aufnahme für ∅10 mm Kugel, 316L |
| Kugelkopf-Aufnahme | 9067MK | 10 | Clip-Aufnahme für ∅13 mm Kugel, 316L |
| Kugelkopf-Bolzen | 9065MK | 6 | Kugelkopf-Bolzen M8, ∅10 mm Kugel, 316L |
| Gabelkopf-Aufnahme | 9070MK | 12 | Gabelkopf M8, 316L |
| Schutzrohr | PROTECT-250 | 15 | UV-Schutzrohr, PA6, 250 mm |

(Confidence: measured — Stabilus Katalog 2025)

### 8.5 Hahn Gasfedern (Langenfeld, Deutschland) — Konfigurator-Spezialist

**Unternehmensprofil:**
- Gegründet: 1963
- Hauptsitz: Langenfeld, NRW
- Spezialität: Gasdruckfedern nach Maß (Online-Konfigurator)
- Marktposition: Mittelständler, stark in Kleinserie und Einzelfertigung
- Marine-Relevanz: Beliebter Ersatzquelle für Yacht-Eigner, da der Konfigurator Einzelstücke in Edelstahl ermöglicht

**Konfigurator (hahn-gasfedern.de/konfigurator):**

Konfigurierbare Parameter:
```
1. Kraft: 50 N bis 2500 N (in 10 N-Schritten)
2. Hub: 50 mm bis 600 mm (in 1 mm-Schritten)
3. Zylinder-∅: 15 mm (Standard), 19 mm (schwer), 25 mm (Industrie)
4. Kolbenstangen-∅: 6 mm (Standard), 8 mm (schwer), 10 mm (Industrie)
5. Endstück Seite A: Kugelkopf (∅8/10/13 mm), Gabelkopf (M6/M8/M10), Öse, Gewinde
6. Endstück Seite B: Kugelkopf (∅8/10/13 mm), Gabelkopf (M6/M8/M10), Öse, Gewinde
7. Material: Stahl lackiert, Stahl Zink-Nickel, Edelstahl V2A, Edelstahl V4A
8. Temperaturbereich: Standard (-30 bis +80°C), Kälte (-40°C), Hitze (+120°C)
```

**Typische Konfigurationen für Yachtbau:**

| Anwendung | Kraft | Hub | Material | Endstücke | Preis (EUR) |
|-----------|-------|-----|----------|-----------|------------|
| Lewmar Low Profile 40 Ersatz | 120 N | 180 mm | V4A | Kugelkopf ∅10/M6 bds. | 48 |
| Lewmar Ocean 60 Ersatz | 300 N | 305 mm | V4A | Kugelkopf ∅10/M8 bds. | 62 |
| Lazarette-Deckel 600×800 | 400 N | 300 mm | V4A | Kugelkopf ∅13/M8 bds. | 68 |
| Lazarette-Deckel 800×1000 | 600 N | 350 mm | V4A | Gabelkopf M10 bds. | 78 |
| Maschinenraum-Luke | 800 N | 400 mm | V4A | Gabelkopf M10 bds. | 92 |

**Lieferzeit:** 5–8 Werktage (Einzelfertigung), 2–3 Werktage (Standard-V4A ab Lager)

(Confidence: documented — Hahn Gasfedern Webshop 2025)

### 8.6 Bansbach (Bettenhausen/Kassel, Deutschland) — Industrie + Marine

**Unternehmensprofil:**
- Gegründet: 1919
- Hauptsitz: Bettenhausen (Kassel), Hessen
- Spezialität: Gasdruckfedern, Dämpfer, Drehzahlregler
- Marktposition: Traditionsunternehmen, stark in Industrie; Marine als Nebenmarkt

**Marine-relevantes Programm:**

| Serie | Typ | Kraftbereich | Hub | Material | Preis (EUR) |
|-------|-----|-------------|-----|----------|------------|
| Easy-Lift EL-14 | Standard | 50–500 N | 50–300 mm | Stahl + Cr | 14–38 |
| Easy-Lift EL-18 | Schwer | 200–1500 N | 80–500 mm | Stahl + Cr | 22–65 |
| Easy-Lift EL-V4A | Edelstahl | 50–800 N | 50–400 mm | V4A komplett | 42–110 |
| Block-O-Lift | Blockierbar | 100–1000 N | 80–400 mm | Stahl oder V4A | 45–165 |
| H-Lift | Gedämpft | 100–600 N | 80–350 mm | Stahl oder V4A | 55–150 |

**Besonderheit:** Bansbach bietet eine „Marine-Empfehlung" in ihrem Onlineshop: vorselektierte Federn in V4A mit Kugelkopf-Endstücken.

(Confidence: documented)

### 8.7 Lesjöfors (Herrljunga, Schweden) — Skandinavischer Spezialist

**Unternehmensprofil:**
- Gegründet: 1852
- Hauptsitz: Herrljunga, Schweden
- Spezialität: Federn aller Art (Druck-, Zug-, Gas-, Blattfedern)
- Marktposition: Größter Federnhersteller Skandinaviens
- Marine-Relevanz: Verbreitet in skandinavischen Werften (Hallberg-Rassy, Najad, Arcona)

**Marine-Programm:**

| Serie | Typ | Kraftbereich | Material | Besonderheit |
|-------|-----|-------------|----------|-------------|
| GF-800 | Standard Marine | 80–600 N | V2A oder V4A | Vorselektiert für skandinavische OEM-Luken |
| GF-1200 | Heavy Marine | 300–1200 N | V4A | Für Lazarette und Motorluken |
| GF-BLOCK | Blockierbar | 150–800 N | V4A | Freigabe per Seilzug |

**Preise:** 35–95 EUR (V4A Marine-Serie), ab Lager in Schweden, Lieferzeit nach Deutschland 3–5 Werktage.

(Confidence: documented)

### 8.8 Vetus (Schiedam, Niederlande) — GSSPAA-Serie

**Unternehmensprofil:**
- Gegründet: 1951
- Hauptsitz: Schiedam, Niederlande
- Spezialität: Marine-Zubehör (Motoren, Luken, Lüfter, Sanitär, Elektrik)
- Marktposition: Einer der größten Marine-Zubehör-Kataloge weltweit

**GSSPAA-Gasdruckfeder-Programm (Eigenmarke):**

| Artikelnummer | Kraft (N) | Hub (mm) | Einbaulänge (mm) | Endstück | Material | Preis (EUR) |
|--------------|-----------|----------|-----------------|----------|----------|------------|
| GSSPAA1020 | 100 | 200 | 480 | Kugelkopf ∅10/M8 | 316 | 38 |
| GSSPAA1525 | 150 | 250 | 585 | Kugelkopf ∅10/M8 | 316 | 42 |
| GSSPAA2025 | 200 | 250 | 585 | Kugelkopf ∅10/M8 | 316 | 45 |
| GSSPAA2530 | 250 | 300 | 695 | Kugelkopf ∅10/M8 | 316 | 48 |
| GSSPAA3530 | 350 | 300 | 695 | Kugelkopf ∅10/M8 | 316 | 52 |
| GSSPAA5035 | 500 | 350 | 810 | Kugelkopf ∅13/M10 | 316 | 62 |
| GSSPAA7540 | 750 | 400 | 930 | Kugelkopf ∅13/M10 | 316 | 78 |

**GSSPAA Zubehör:**

| Artikel | Artikelnummer | Preis (EUR) |
|---------|---------------|-------------|
| Kugelkopf-Aufnahme ∅10 mm | GSSPAAC10 | 6 |
| Kugelkopf-Aufnahme ∅13 mm | GSSPAAC13 | 8 |
| Kugelkopf-Bolzen M8/∅10 mm | GSSPAAB10 | 5 |
| Kugelkopf-Bolzen M10/∅13 mm | GSSPAAB13 | 7 |
| Montageplatte (Paar) | GSSPAAMP | 12 |

**Vorteil Vetus:** Alle GSSPAA-Federn sind standardmäßig aus 316-Edelstahl und für Salzwasser-Einsatz spezifiziert. Endstücke sind universell und kompatibel mit den meisten Lewmar-, Goiot- und Gebo-Luken (mit Standard-Kugelkopf-Aufnahmen).

(Confidence: documented — Vetus Catalogue 2025)

### 8.9 Osculati (Segrate/Milano, Italien) — Breitestes Sortiment

**Unternehmensprofil:**
- Gegründet: 1958
- Hauptsitz: Segrate (Mailand), Italien
- Spezialität: Marine-Zubehör (größter Katalog Europas, >50.000 Artikel)
- Marktposition: Preis-Leistungs-Führer; breites Sortiment, variable Qualität

**Lukenbeschlag-Sortiment (Auszug):**

| Kategorie | Artikelnummer | Beschreibung | Material | Preis (EUR) |
|-----------|---------------|-------------|----------|------------|
| Gasdruckfeder | 38.020.30 | 150N/250mm, Kugelkopf ∅10 | 316 | 28 |
| Gasdruckfeder | 38.020.47 | 250N/250mm, Kugelkopf ∅10 | 316 | 34 |
| Gasdruckfeder | 38.020.55 | 350N/300mm, Kugelkopf ∅10 | 316 | 38 |
| Gasdruckfeder | 38.020.68 | 500N/350mm, Kugelkopf ∅13 | 316 | 48 |
| Scharnier (Piano) | 38.659.00 | Klavierband, 316L, 40×1,0mm/m | 316L | 18/m |
| Scharnier (Butt) | 38.830.04 | Stumpf, 100×75mm, verstärkt | 316L | 22 |
| Scharnier (Strap) | 38.845.02 | Band, 200mm, verstärkt | 316L | 38 |
| Scharnier (Lift-Off) | 38.840.01 | Aushänge, 100×62mm | 316L | 22 |
| Scharnier (Concealed) | 38.930.00 | Verdeckt, max. 8 kg | Zamak Cr | 18 |
| Verschluss (QT) | 38.180.00 | Quarter-Turn, bündig | Zamak Cr | 8 |
| Verschluss (Toggle) | 38.170.01 | Spannverschluss, einstellbar | 316L | 25 |
| Stay (Kette) | 38.700.00 | Kettenstay, 5mm × 300mm | 316L | 18 |
| Stay (Reibung) | 38.695.00 | Reibungsstay, 250mm, 10 kg | 316L | 28 |
| Stay (Teleskop) | 38.696.30 | Teleskop, 280–450mm | 316L | 45 |
| Griff (Ring) | 38.150.01 | Ringgriff, versenkbar, ∅55mm | 316L | 12 |
| Griff (Flush) | 38.151.20 | Einlassgriff, 80×60mm | 316L | 15 |
| Dog-Bolt | 38.196.00 | Dog-Verschluss M10 | 316L | 18 |

**Qualitätshinweis (AYDI-Bewertung):**
- Osculati 316L-Artikel: Tatsächlich 316L, gute Qualität (regelmäßig geprüft durch unabhängige Tests in Practical Sailor)
- Osculati Zamak-Artikel: Akzeptabel für geschützte Innenbereiche; Verchromung platzt bei Salzwasser-Exposition nach 1–3 Jahren
- Osculati Gasdruckfedern: Zugekauft von verschiedenen Herstellern; Qualität schwankt chargenweise. Kolbenstange ist 316, nicht garantiert 316L

(Confidence: documented)

### 8.10 Plastimo (Lorient, Frankreich) — Marine-Sicherheitsausstattung

**Lukenbeschlag-Sortiment (begrenzt):**

| Kategorie | Artikelnummer | Beschreibung | Material | Preis (EUR) |
|-----------|---------------|-------------|----------|------------|
| Gasdruckfeder | 63576 | 200N/250mm, Kugelkopf ∅10 | 304 | 32 |
| Gasdruckfeder | 63577 | 300N/300mm, Kugelkopf ∅10 | 304 | 38 |
| Einlassgriff | 16580 | Flush Pull, 90×60mm | 316L | 22 |

**Hinweis:** Plastimo ist kein Beschlag-Spezialist. Die Gasdruckfedern sind OEM (wahrscheinlich Suspa/Bansbach). Für Plastimo-Luken (z.B. Plastimo Offshore-Luken) empfiehlt sich der Einsatz von Stabilus- oder Vetus-Ersatzfedern.

(Confidence: estimated)

### 8.11 Suncor Stainless (Plymouth, MA, USA) — Edelstahl-Scharniere

**Unternehmensprofil:**
- Hauptsitz: Plymouth, Massachusetts, USA
- Spezialität: 316L-Edelstahl-Beschläge für Marine-Anwendungen
- Marktposition: US-Marktführer für Edelstahl-Marine-Beschläge; in EU über Fachhändler verfügbar

**Scharnier-Programm (Auszug):**

| Typ | Artikelnummer | Maße (mm) | Stift-∅ | Material | Preis (EUR) |
|-----|--------------|-----------|---------|----------|------------|
| Piano Hinge | S0721-0100 | 50×1,2mm offen/m | 3,2 | 316L | 22/m |
| Piano Hinge (schwer) | S0721-0200 | 76×1,5mm offen/m | 4,8 | 316L | 38/m |
| Butt Hinge | S3413-0200 | 63×50mm | 4,8 | 316L | 15 |
| Butt Hinge | S3413-0300 | 76×63mm | 6,3 | 316L | 22 |
| Butt Hinge | S3413-0400 | 102×76mm | 6,3 | 316L | 28 |
| Strap Hinge (T) | S3827-0600 | 152mm, T-Strap | 6,3 | 316L | 45 |
| Lift-Off Hinge | S3816-0500 | 127×76mm, L/R | 6,3 | 316L | 32 |
| Strap Hinge | S3821-0600 | 152mm, gerade | 6,3 | 316L | 38 |

**Qualitätsmerkmal:** Suncor verwendet ausschließlich 316L (nicht 316 oder 304) und liefert mit Materialzertifikat (3.1 nach EN 10204). Im Yachtbau die verlässlichste Quelle für korrosionsbeständige Scharniere.

(Confidence: documented)

### 8.12 Southco (Concordville, PA, USA) — Verschlüsse und Verriegelungen

**Unternehmensprofil:**
- Gegründet: 1899
- Hauptsitz: Concordville, Pennsylvania, USA
- Europa-Vertrieb: Southco Europe, Worcester, UK
- Spezialität: Verschlusslösungen (Latches, Locks, Hinges, Handles)
- Marktposition: Globaler Marktführer für Verschlusstechnik (Industrie + Marine)
- Marine-Relevanz: Umfangreichste Auswahl an Marine-Verschlüssen; OEM für viele Yacht-Hersteller

**Marine-Verschluss-Programm (Auszug):**

| Kategorie | Serie | Artikelnummer | Beschreibung | Material | Preis (EUR) |
|-----------|-------|---------------|-------------|----------|------------|
| Cam Latch | M1 | M1-43-31 | Flush Cam, abschließbar | 316L | 52 |
| Cam Latch | M1 | M1-41-25 | Flush Cam, nicht abschließbar | 316L | 38 |
| Compression | E3 | E3-5-31 | Compression Latch, 500N | 316L | 65 |
| Compression | E5 | E5-10-301-40 | Mini Compression, bündig, abschließbar | 316L | 48 |
| Quarter-Turn | 62 | 62-10-25 | Flush QT, ∅22mm Ausschnitt | 316L | 18 |
| Quarter-Turn | 62 | 62-10-35 | Flush QT, abschließbar | 316L | 28 |
| Push-to-Close | C2 | C2-32-15 | Slam Latch, bündig | 316L | 22 |
| Toggle | 40 | 40-11-101-20 | Toggle Latch, verstellbar, 600N | 316L | 42 |
| Flush Pull | M5 | M5-92-301-8 | Flush Pull Handle, 76×57mm | 316L | 22 |
| Friction Hinge | E6 | E6-10-301-50 | Torque Hinge, 3,0 Nm | 316L | 35 |
| Friction Hinge | E6 | E6-10-501-50 | Torque Hinge, 5,0 Nm | 316L | 42 |
| Push-Button | 93 | 93-10-301 | Push-Button Lock, bündig | 316L | 18 |

**Southco Vorteile für AYDI-Integration:**
- Jeder Artikel hat eine eindeutige Nummer und ist weltweit verfügbar
- 3D-CAD-Daten (STEP/IGES) downloadbar
- Detaillierte Einbauanleitungen mit Toleranzangaben
- Marine-spezifische Korrosionsprüfung (2000h Salzsprühtest für 316L-Serie)

(Confidence: documented — Southco Marine Catalogue 2025)

### 8.13 Perko (Miami, FL, USA) — Traditionelle Marine-Beschläge

**Unternehmensprofil:**
- Gegründet: 1907
- Hauptsitz: Miami, Florida, USA
- Spezialität: Marine-Beschläge, Beleuchtung, Ventilation
- Marktposition: Traditionsunternehmen, breit aufgestellt, gutes Preis-Leistungs-Verhältnis

**Beschlag-Programm (Auszug):**

| Kategorie | Artikelnummer | Beschreibung | Material | Preis (EUR) |
|-----------|---------------|-------------|----------|------------|
| Cam Latch | 1092DP0CHR | Cam Latch, Messing verchromt | Messing/Cr | 22 |
| Compression | 0931DP0CHR | Compression Latch, abschließbar | Messing/Cr | 35 |
| Quarter-Turn | 1092DP0STS | QT mit Schlüssel | 316 | 32 |
| Barrel Lock | 0927DP0STS | Zylinderschloss | 316 | 25 |
| Slam Latch | 0960DP0STS | Schnappschloss | 316 | 15 |
| Flush Pull | 1232DP0STS | Einlassgriff, 89×64mm | 316 | 18 |
| Piano Hinge | 0726DP0STS | 60×1,5mm/m, vorgebohrt | 316 | 35/m |
| Butt Hinge | 1293DP0CHR | 76×63mm | Messing/Cr | 18 |

**Hinweis für EU-Einsatz:** Perko-Teile sind in Europa schwerer verfügbar. Import über Defender Industries oder Hamilton Marine (USA) mit 5–10 Tagen Lieferzeit + Zoll (2,7% auf Schiffszubehör) + 19% EUSt.

(Confidence: documented)

### 8.14 Sea-Dog (Everett, WA, USA) — Budget-Marine-Beschläge

**Unternehmensprofil:**
- Hauptsitz: Everett, Washington, USA
- Spezialität: Breites Sortiment Marine-Zubehör, Budget- bis Mittelklasse
- Marktposition: US-Markt, Budget-orientiert; in EU über Großhändler

**Beschlag-Programm (Auszug):**

| Kategorie | Artikelnummer | Beschreibung | Material | Preis (EUR) |
|-----------|---------------|-------------|----------|------------|
| Quarter-Turn | 221840 | QT Flush, ∅25mm | 316L | 15 |
| Slam Latch | 221910 | Schnappschloss, federgespannt | 316L | 18 |
| Combination Lock | 221830 | Kombi-Schloss, 3-stellig | Zamak | 22 |
| Ring Pull | 221560 | Ringgriff, versenkbar | 316L | 15 |
| Butt Hinge | 204560 | 63×50mm | 304 | 9 |
| Piano Hinge | 201580 | 50×1,5mm/m | 304 | 15/m |
| Lift-Off Hinge | 204600 | 89×51mm | 304 | 12 |
| Chain Stay | 321860 | Kettenstay 350mm | 316L | 15 |

**AYDI-Bewertung:** Sea-Dog liefert akzeptable Qualität für den Preis. Scharniere sind oft 304 statt 316L — für Mittelmeer/Blauwasser upgraden. Verschlüsse und Griffe in 316L sind gut nutzbar.

(Confidence: estimated)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Decksluken (Deck Hatches) — Beschlag-Konfiguration

#### 9.1.1 Standard-Decksluke (Lewmar Low Profile / Ocean, Size 40–70)

**Typische Beschlag-Konfiguration:**

| Komponente | Anzahl | Typ | Hersteller/Artikel | Funktion |
|-----------|--------|-----|-------------------|---------|
| Integriertes Scharnier | 2 | Verdeckt, im Rahmen | Lewmar (integriert) | Öffnungsbewegung |
| Gasdruckfeder | 1 | Standard 120–300N | Lewmar 89500100–300 | Öffnungshilfe + Halterung |
| Cam-Latch | 1 | Dreh-Nockenriegel | Lewmar 89400066 | Verriegelung + Dichtungsanpressung |
| Flush Pull | 1 | Einlassgriff | Lewmar 89400080 | Bedienung von außen (Deck) |
| Innengriff | 1 | Schwenkgriff | Lewmar (integriert) | Bedienung von innen (Kajüte) |
| Moskitonetz-Clip | 4 | Federclip | Lewmar 39940030/39960030 | Halterung für Fliegennetz |

**Gesamtkosten Beschlagsatz (Ersatzteile):** ~120–180 EUR (ohne Luke selbst)

**Typische Fehlerbilder:**

| Fehler | Ursache | Score-Auswirkung | Maßnahme |
|--------|---------|-----------------|----------|
| Gasdruckfeder hält Luke nicht mehr | Gasverlust nach 4–8 Jahren | score_function -30 | Feder tauschen (45–90 EUR) |
| Cam-Latch rastet nicht mehr ein | Abnutzung der Nockenkontur | score_function -20, score_safety -15 | Cam-Latch tauschen (38–45 EUR) |
| Scharnier hat Spiel (>2mm) | Bolzenverschleiß | score_mechanical -25 | Bolzen tauschen oder Luke tauschen |
| Flush Pull korrodiert | Falsches Material oder Salzverkrustung | score_corrosion -10 | Reinigen oder tauschen (15–28 EUR) |
| Luke klappert bei Seegang | Cam-Latch nicht stramm genug | score_function -10 | Cam nachstellen oder Dichtung erneuern |

(Confidence: documented)

#### 9.1.2 Fluchtluke (Escape Hatch) — Spezielle Anforderungen

**ISO 12216 Mindestanforderungen:**
```
- Mindestgröße: 400 × 520 mm (lichte Öffnung)
- Öffnung von innen: ohne Werkzeug in < 5 Sekunden
- Öffnung von außen: ohne Werkzeug möglich
- Haltevorrichtung: Luke muss bei min. 90° offen gehalten werden
- KEINE Gasdruckfeder als alleinige Halterung (Verletzungsgefahr bei Versagen)
- KEINE abschließbare Verriegelung, die von innen nicht ohne Schlüssel zu öffnen ist
- Kennzeichnung: "EMERGENCY EXIT / NOTAUSGANG" (Symbol nach ISO 7010)
```

**Beschlag-Konfiguration Fluchtluke:**

| Komponente | Anzahl | Typ | Anforderung |
|-----------|--------|-----|-------------|
| Scharnier | 2 | Stumpf/Band, geschmiedet 316L | Keine Aushängescharniere (Luke darf nicht abfallen!) |
| Haltevorrichtung | 1 | Kettenstay oder Reibungsstay | Robust, keine Gasdruckfeder als Alleinhalter |
| Gasdruckfeder (optional) | 1 | Unterstützend, NICHT tragend | Als Komfort-Ergänzung zu mechanischem Stay |
| Notentriegelung | 1 | Hebel, rot markiert | Von innen: ein Handgriff, keine Drehung |
| Notentriegelung außen | 1 | Flush-Mount, beschriftet | Von außen: Rettungskräfte-Zugang |
| Griff innen | 1 | Greifbügel, gut sichtbar | In Dunkelheit tastbar (fluoreszierend empfohlen) |

**AYDI-Bewertungslogik für Fluchtluken:**

```python
def assess_escape_hatch(assembly: HatchHardwareAssembly) -> dict:
    """Spezifische Bewertung einer Fluchtluke nach ISO 12216."""
    findings = []
    score = 100
    
    # Mindestgröße prüfen
    if assembly.hatch_width_mm < 400 or assembly.hatch_length_mm < 520:
        findings.append(
            f"KRITISCH: Fluchtluke unterschreitet Mindestmaß 400×520 mm "
            f"(aktuell: {assembly.hatch_width_mm}×{assembly.hatch_length_mm} mm). "
            f"Nicht normkonform nach ISO 12216."
        )
        score -= 50
    
    # Notentriegelung prüfen
    has_inside_operable_latch = any(
        l.inside_operable and not l.tool_required
        for l in assembly.latches
    )
    if not has_inside_operable_latch:
        findings.append(
            "KRITISCH: Keine werkzeugfreie Notentriegelung von innen vorhanden. "
            "ISO 12216 verlangt Öffnung in < 5 Sekunden ohne Werkzeug."
        )
        score -= 40
    
    # Mechanische Haltevorrichtung prüfen
    has_mechanical_stay = any(
        s.hardware_type in (
            HardwareType.STAY_CHAIN,
            HardwareType.STAY_FRICTION,
            HardwareType.STAY_TELESCOPIC,
        )
        for s in assembly.stays
    )
    if not has_mechanical_stay and assembly.gas_struts:
        findings.append(
            "WARNUNG: Fluchtluke wird nur durch Gasdruckfeder gehalten. "
            "Bei Gasdruckfeder-Versagen kann die Luke auf die flüchtende Person fallen. "
            "Mechanischer Stay (Kette oder Reibung) als Backup empfohlen."
        )
        score -= 20
    
    # Abschließbare Verriegelung prüfen
    has_lock_without_inside_release = any(
        l.lockable and not l.inside_operable
        for l in assembly.latches
    )
    if has_lock_without_inside_release:
        findings.append(
            "KRITISCH: Abschließbare Verriegelung ohne Innen-Notentriegelung an Fluchtluke. "
            "Verstoß gegen ISO 12216 und CE-Richtlinie 2013/53/EU."
        )
        score -= 50
    
    return {
        "score": max(0, score),
        "findings": findings,
        "is_compliant": score >= 80,
        "confidence": "calculated",
    }
```

(Confidence: measured — ISO 12216:2020)

### 9.2 Lazarette-Luken — Beschlag-Konfiguration

#### 9.2.1 Anforderungen

Lazarette-Deckel sind typischerweise die schwersten Lukendeckel an Bord (15–80 kg):

| Größenklasse | Typische Maße | Gewicht | Gasdruckfeder-Kraft (2 Stk.) | Empfohlene Feder |
|-------------|---------------|---------|------------------------------|-----------------|
| Klein (Segelboot 8–10m) | 400×500 mm | 8–15 kg | 150–250 N | Vetus GSSPAA1525 oder Stabilus 085569 |
| Mittel (Segelboot 10–14m) | 600×800 mm | 15–30 kg | 300–500 N | Vetus GSSPAA3530 oder Stabilus 094472 |
| Groß (Motor-/Segelyacht 14–20m) | 800×1200 mm | 30–60 kg | 500–800 N | Stabilus 094488 oder Hahn Custom |
| Sehr groß (>20m) | 1000×1500 mm | 50–100 kg | 750–1200 N | Stabilus 094515 oder Lesjöfors GF-1200 |

#### 9.2.2 Typische Beschlag-Konfiguration (mittelgroßes Lazarett)

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Scharnier | 2–3 | Piano (Meterware) oder 3× Butt | Piano: Suncor S0721-0200 (schwer); Butt: Suncor S3413-0400 |
| Gasdruckfeder | 2 | V4A, 300–500 N | Stabilus 094472 (V4A, 350N/300mm) |
| Verschluss | 2 | Flush Quarter-Turn + Schloss | Southco 62-10-35 (abschließbar) |
| Haltevorrichtung | 1 | Kettenstay als Backup | Osculati 38.700.00 |
| Griff | 1 | Ringgriff oder Flush Pull | Osculati 38.150.01 (Ringgriff) |
| Gummi-Puffer | 2 | Deckelstopper bei 90° | Standard-Gummipuffer ∅20mm |

**Gesamtkosten Beschlagsatz:** ~180–350 EUR

#### 9.2.3 Besonderheit: Cockpit-Lazarette

Cockpit-Lazarette liegen im Spritzwasser-Bereich und sind zudem mechanisch belastet (Sitzen, Stehen):

| Zusatz-Anforderung | Begründung | Lösung |
|--------------------|-----------|--------|
| Verstärkte Scharniere | Personen sitzen/stehen auf dem Deckel | Schwere Stumpfscharniere (min. 100×75 mm, 3 mm Stärke) |
| Korrosionsschutz erhöht | Dauerhaft Salzspritzer | NUR 316L oder Bronze; Zamak = Totalschaden nach 2 Jahren |
| Selbsthaltendes Öffnen | Windschutz der Luke bei Seegang | Gasdruckfeder + Sicherungsriegel oder Blockierbare Feder |
| Entwässerung | Wasser läuft in Lazarett bei offener Luke | Drainagelöcher im Deckelrahmen (ISO 11812) |

(Confidence: documented)

### 9.3 Maschinenraumluken — Beschlag-Konfiguration

#### 9.3.1 Anforderungen (ISO 9094 Brandschutz)

| Anforderung | Norm | Detail |
|-------------|------|--------|
| Brandschutz | ISO 9094:2015 | Luke muss mind. 15 Minuten feuerhemmend sein; Beschläge aus nicht-brennbarem Material |
| Selbstschluss | ISO 9094:2015 | Maschinenraum-Luke sollte bei Brand selbstschließend sein (Federscharnier oder Gasdruckfeder mit Auslösung) |
| Notöffnung | Allgemein | Von außen (Löschangriff) und innen (Flucht) öffenbar |
| Schalldämmung | Komfort | Dichtungen auch schallmindernd (EPDM mit Shore A 40–50) |
| Wärmebeständigkeit | Motorwärme | Gasdruckfedern bis +80°C spezifizieren; Standardfedern ändern Kraft bei Motorwärme (+10–15%) |

#### 9.3.2 Typische Beschlag-Konfiguration

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Scharnier | 3–4 | Aushängescharnier (Lift-Off) | Suncor S3816-0500 — erlaubt komplettes Abnehmen für Motorwartung |
| Gasdruckfeder | 2 | V4A, 500–1000 N, mit Endlagendämpfung | Stabilus 096220 (DAMP, 500N) |
| Verschluss | 4–6 | Toggle Latch (hohe Anpresskraft) | Southco 40-11-101-20 oder De Sta Co 323 |
| Notentriegelung | 1 | Schnellauslösung, markiert | Kundenspezifisch; roter Hebel |
| Stay (Backup) | 1 | Teleskopstay | Vetus STAYLONG |
| Griff | 2 | T-Griff (von außen) | Robuste Ausführung, 316L |
| Gummi-Dämpfer | 4 | Schwingungsdämpfer unter Scharnieren | Shore A 50–60, ∅30mm |

**Gesamtkosten Beschlagsatz:** ~350–800 EUR

(Confidence: documented)

### 9.4 Stauklappen und Cockpit-Locker — Beschlag-Konfiguration

#### 9.4.1 Anforderungen

Cockpit-Stauklappen sind typischerweise leicht (2–8 kg) und klein (300×300 bis 600×400 mm):

| Anforderung | Detail |
|-------------|--------|
| Salzwasser-Beständigkeit | Ständig im Spritzbereich |
| Bündig | Keine Stolperkanten (ISO 15085) |
| Schnellzugriff | Staufächer für Fender, Leinen — schnelles Öffnen wichtig |
| Diebstahlschutz (Hafen) | Abschließbar für wertvolle Ausrüstung |

#### 9.4.2 Typische Beschlag-Konfiguration

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Scharnier | 2 | Stumpfscharnier (Butt), 50×38mm | Suncor S3413-0200 (316L) |
| Gasdruckfeder | 0–1 | Optional bei Deckeln >5kg | Vetus GSSPAA1020 (100N) |
| Verschluss | 1 | Flush Quarter-Turn, abschließbar | Southco 62-10-35 |
| Griff | 0 | (integriert im QT-Verschluss) | — |
| Gummi-Puffer | 2 | Gegen Klappern bei Seegang | ∅10mm, selbstklebend |

**Gesamtkosten Beschlagsatz:** ~40–90 EUR

(Confidence: documented)

### 9.5 Portlights — Beschlag-Konfiguration

#### 9.5.1 Anforderungen

Portlights (öffnende Bulleyentypen) haben spezifische Beschlag-Anforderungen:

| Anforderung | Detail |
|-------------|--------|
| Reibungsscharnier | Portlight muss in jeder Öffnungsposition halten |
| Knebelverschluss | Dichtungsanpressung über Handknebel |
| Kompakte Bauweise | Geringe Einbauhöhe im Aufbau |
| Korrosion | Scharnier in Augenhöhe = Korrosion sofort sichtbar (Ästhetik!) |

#### 9.5.2 Typische Beschlag-Konfiguration (öffnendes Portlight)

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Reibungsscharnier | 2 | Torque Hinge, 2–5 Nm | Southco E6-10-301-50 (3,0 Nm) |
| Knebelverschluss | 1–2 | Handknebel mit Exzenter | Lewmar (integriert) oder Goiot (integriert) |
| Moskitonetz-Halterung | 2–4 | Magnetclips | Lewmar 39940 Serie |

**Hinweis:** Bei den meisten Portlight-Herstellern (Lewmar, Goiot, Gebo, Bomar) sind Scharniere und Verschlüsse integraler Bestandteil des Portlight-Rahmens und nicht einzeln austauschbar. Reibungsscharniere (Southco E6-Serie) werden als Aftermarket-Upgrade eingesetzt, wenn die integrierten Scharniere verschlissen sind.

**Gesamtkosten Beschlagsatz:** ~60–120 EUR (Nachrüstung/Ersatz)

(Confidence: documented)

### 9.6 Ankerkasten-Luken — Beschlag-Konfiguration

#### 9.6.1 Anforderungen

Der Ankerkasten ist die korrosiv aggressivste Umgebung an Bord:

| Belastung | Intensität |
|-----------|-----------|
| Salzwasser | Permanent (Ankerkette tropft, Kettenstopper-Drainage) |
| Mechanisch | Hoch (schwere Deckel, Ankermanöver, Wellenschlag) |
| UV | Maximal (ganz vorn, ungeschützt) |
| Chemisch | Moderat (Algenbewuchs, Schlick, Meersalz-Kristalle) |

#### 9.6.2 Typische Beschlag-Konfiguration

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Scharnier | 2–3 | Band (Strap), schwere Ausführung 316L | Suncor S3827-0600 oder Suncor S3821-0600 |
| Gasdruckfeder | 2 | V4A mit UV-Schutzrohr | Stabilus V4A + PROTECT-250 Schutzrohr |
| Verschluss | 2 | Toggle Latch (hohe Anpresskraft gegen Brecher) | Southco 40-11-101-20 |
| Kettenstay | 1 | 316L Kette, 6mm | Osculati 38.700.00 (verstärkt) |
| Drainage | 2 | Scuppers im Deckelrahmen | Nicht Beschlag, aber relevant für Korrosion |

**Material-Regel Ankerkasten:**
- **316L = Minimum.** 304 korrodiert hier innerhalb von 1–2 Jahren.
- **Bronze (Silizium) = Alternative.** Teurer, aber korrosionsfrei.
- **Titan = Overkill,** aber gelegentlich bei Superyachten anzutreffen.
- **KEIN Zamak, KEIN verzinkter Stahl, KEIN Aluminium** (galvanische Korrosion mit Ankerkette)

**Gesamtkosten Beschlagsatz:** ~180–350 EUR

(Confidence: documented)

### 9.7 Kabinensole-Luken (Cabin Sole Hatches) — Beschlag-Konfiguration

#### 9.7.1 Anforderungen

Bodenluke zum Zugang zu Bilge, Tanks, Ventilen:

| Anforderung | Detail |
|-------------|--------|
| Bündig | Absolut bündig mit Solenoberfläche (Stolpergefahr, Ästhetik) |
| Begehbar | Beschläge müssen unter Personenlast (100 kg) funktionieren |
| Schnellzugang | Zugang zu Bilgepumpe, Seeventilen — im Notfall in Sekunden |
| Korrosion | Gering (Innenraum), aber Kondensat und Bilgewasser möglich |

#### 9.7.2 Typische Beschlag-Konfiguration

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Scharnier | 2 | Verdecktes Scharnier oder Piano (unter der Sole) | Southco C5-21 (verdeckt, 316L) |
| Verschluss | 1 | Flush Pull (versenkter Ringgriff) | Osculati 38.150.01 (316L, ∅55mm) |
| Haltevorrichtung | 1 | Kettenstay kurz (Sole-Luke fällt sonst zu) | 316L Kette, 150–250mm |
| Gasdruckfeder | 0 | Nicht üblich bei Solenluken | — (zu wenig Einbauraum) |
| Gummi-Dichtstreifen | umlaufend | Gegen Klappergeräusche und Gerüche aus Bilge | EPDM, 3×8mm |

**Gesamtkosten Beschlagsatz:** ~40–80 EUR

(Confidence: documented)

### 9.8 Windschutzscheiben-Luken (Windscreen Panels) — Beschlag-Konfiguration

#### 9.8.1 Anforderungen (Motoryachten)

Motoryachten haben häufig öffenbare Windschutzscheiben-Segmente für Belüftung und Zugang:

| Anforderung | Detail |
|-------------|--------|
| Parallelogramm-Beschlag | Scheibe fährt nach vorn und oben, bleibt parallel |
| Gasdruckfeder-Unterstützung | Schwere Scheibe (10–30 kg Glas/Acryl) |
| Wasserdicht | Fahrtwind + Spritzwasser |
| Sicherheitsverriegelung | Gegen unbeabsichtigtes Öffnen bei Fahrt |

#### 9.8.2 Typische Beschlag-Konfiguration

| Komponente | Anzahl | Typ | Empfehlung |
|-----------|--------|-----|-----------|
| Parallelogramm-Arm | 2 | Spezial-Beschlag (316L, geschmiedet) | Vetus oder Boomsma (NL) Custom |
| Gasdruckfeder | 2 | V4A, 300–500 N | Stabilus 094472 (V4A, 350N/300mm) |
| Verriegelung | 2 | Kompressionsverschluss | Southco E3-5-31 |
| Griff | 1 | T-Griff oder Einlassgriff | Southco M5-92-301-8 |

**Gesamtkosten Beschlagsatz:** ~250–600 EUR

(Confidence: documented)

### 9.9 AYDI-Zuordnungsmatrix: Lukentyp → Beschlag-Empfehlung

```python
# AYDI 08.04 — Zuordnungslogik Lukentyp → Beschlag-Konfiguration

HATCH_TYPE_HARDWARE_MAP = {
    "deck_hatch": {
        "hinges": {"type": "integrated", "material": "stainless_316l"},
        "gas_struts": {"count": 1, "force_range_n": (100, 300), "material": "stainless_316"},
        "latches": {"type": "latch_cam", "count": 1, "lockable": False},
        "handles": {"type": "handle_flush", "count": 1},
        "stays": {"type": None, "note": "Gasdruckfeder übernimmt Haltefunktion"},
        "cost_range_eur": (120, 180),
    },
    "escape_hatch": {
        "hinges": {"type": "hinge_butt", "material": "stainless_316l", "count": 2, "forged": True},
        "gas_struts": {"count": 0, "note": "NICHT als Alleinhalter, optional unterstützend"},
        "latches": {"type": "latch_cam", "count": 1, "inside_operable": True, "tool_required": False},
        "handles": {"type": "handle_pull", "count": 1, "fluorescent": True},
        "stays": {"type": "stay_chain", "count": 1, "mandatory": True},
        "cost_range_eur": (150, 280),
    },
    "lazarette": {
        "hinges": {"type": "hinge_piano", "material": "stainless_316l"},
        "gas_struts": {"count": 2, "force_range_n": (200, 800), "material": "stainless_316l"},
        "latches": {"type": "latch_quarter_turn", "count": 2, "lockable": True},
        "handles": {"type": "handle_ring", "count": 1},
        "stays": {"type": "stay_chain", "count": 1, "note": "Backup zu Gasdruckfedern"},
        "cost_range_eur": (180, 350),
    },
    "engine_room": {
        "hinges": {"type": "hinge_lift_off", "material": "stainless_316l", "count": 3},
        "gas_struts": {"count": 2, "force_range_n": (500, 1200), "material": "stainless_316l", "damped": True},
        "latches": {"type": "latch_toggle", "count": 4, "adjustable": True},
        "handles": {"type": "handle_t", "count": 2},
        "stays": {"type": "stay_telescopic", "count": 1},
        "cost_range_eur": (350, 800),
    },
    "cockpit_locker": {
        "hinges": {"type": "hinge_butt", "material": "stainless_316l", "count": 2},
        "gas_struts": {"count": 0, "note": "Optional bei >5 kg Deckelgewicht"},
        "latches": {"type": "latch_quarter_turn", "count": 1, "lockable": True, "flush": True},
        "handles": {"type": None, "note": "Integriert im QT-Verschluss"},
        "stays": {"type": None},
        "cost_range_eur": (40, 90),
    },
    "anchor_locker": {
        "hinges": {"type": "hinge_strap", "material": "stainless_316l", "count": 2, "heavy_duty": True},
        "gas_struts": {"count": 2, "force_range_n": (200, 500), "material": "stainless_316l", "uv_protected": True},
        "latches": {"type": "latch_toggle", "count": 2},
        "handles": {"type": "handle_flush", "count": 1},
        "stays": {"type": "stay_chain", "count": 1},
        "cost_range_eur": (180, 350),
    },
    "portlight": {
        "hinges": {"type": "hinge_friction", "material": "stainless_316l", "count": 2, "torque_nm": 3.0},
        "gas_struts": {"count": 0},
        "latches": {"type": "latch_cam", "count": 1, "note": "Knebelverschluss, integriert"},
        "handles": {"type": None, "note": "Integriert im Rahmen"},
        "stays": {"type": None},
        "cost_range_eur": (60, 120),
    },
    "cabin_sole": {
        "hinges": {"type": "hinge_concealed", "material": "stainless_316l", "count": 2},
        "gas_struts": {"count": 0},
        "latches": {"type": "handle_ring", "count": 1, "flush": True},
        "handles": {"type": "handle_ring", "count": 1},
        "stays": {"type": "stay_chain", "count": 1, "short": True},
        "cost_range_eur": (40, 80),
    },
    "windscreen_panel": {
        "hinges": {"type": "parallelogram", "material": "stainless_316l", "count": 2},
        "gas_struts": {"count": 2, "force_range_n": (300, 500), "material": "stainless_316l"},
        "latches": {"type": "latch_compression", "count": 2},
        "handles": {"type": "handle_flush", "count": 1},
        "stays": {"type": None},
        "cost_range_eur": (250, 600),
    },
    "fuel_tank_access": {
        "hinges": {"type": "hinge_butt", "material": "stainless_316l", "count": 2},
        "gas_struts": {"count": 0},
        "latches": {"type": "latch_quarter_turn", "count": 2, "lockable": True, "non_sparking": True},
        "handles": {"type": "handle_flush", "count": 1},
        "stays": {"type": "stay_chain", "count": 1},
        "cost_range_eur": (60, 120),
        "special": "Funkenfreie Verschlüsse empfohlen (Bronze oder Polyamid); ABYC H-25 beachten",
    },
}
```

### 9.10 Kostenübersicht nach Bootsklasse

```python
# AYDI 08.04 — Parametrische Kosten-Referenz Lukenbeschläge

HARDWARE_COST_BY_BOAT_CLASS = {
    "production_sailboat_8_14m": {
        "description": "Seriensegelboot 8–14m",
        "price_range_eur": "80.000–300.000",
        "total_hatches": "6–12",
        "hardware_cost_total_eur": (600, 1800),
        "hardware_cost_per_hatch_eur": (80, 180),
        "typical_hardware_quality": "OEM Lewmar/Goiot Standard, 304/316 gemischt",
        "replacement_interval_years": 8,
        "annual_maintenance_cost_eur": (50, 150),
    },
    "semi_custom_cruiser_12_20m": {
        "description": "Halb-Custom Fahrtenyacht 12–20m",
        "price_range_eur": "300.000–1.500.000",
        "total_hatches": "10–18",
        "hardware_cost_total_eur": (1500, 5000),
        "hardware_cost_per_hatch_eur": (150, 350),
        "typical_hardware_quality": "Lewmar Ocean / Goiot Opal, durchgehend 316L",
        "replacement_interval_years": 10,
        "annual_maintenance_cost_eur": (100, 300),
    },
    "custom_superyacht_18m_plus": {
        "description": "Custom / Superyacht ab 18m",
        "price_range_eur": "ab 1.500.000",
        "total_hatches": "15–40",
        "hardware_cost_total_eur": (5000, 25000),
        "hardware_cost_per_hatch_eur": (300, 800),
        "typical_hardware_quality": "Custom 316L/Bronze, Southco Marine, Stabilus V4A DAMP",
        "replacement_interval_years": 12,
        "annual_maintenance_cost_eur": (200, 800),
    },
}
```

(Confidence: estimated — Aggregiert aus Werft-Kalkulationen und Fachliteratur)

---

## Technische Referenz & Berechnungen

### Gasdruckfeder: Kraftberechnung

Die erforderliche Kraft einer Gasdruckfeder ergibt sich aus:

```
F = A × P

F = Kraft in Newton [N]
A = Kolbenfläche in mm²
P = Innendruck in MPa (N/mm²)

Kolbenfläche: A = π × (d/2)²
  d = Kolbendurchmesser [mm]
```

**Praxisberechnung für Lukendeckel:**

```python
def gasdruckfeder_kraft_berechnen(
    lukengewicht_kg: float,
    schwerpunktabstand_mm: float,
    feder_hebelarm_mm: float,
    anzahl_federn: int = 2,
    sicherheitsfaktor: float = 1.3,
    oeffnungswinkel_grad: float = 90.0,
) -> dict:
    """
    Berechnet die erforderliche Gasdruckfeder-Kraft für einen Lukendeckel.

    Parameter:
        lukengewicht_kg: Gewicht des Lukendeckels inkl. Beschläge
        schwerpunktabstand_mm: Abstand Drehachse → Schwerpunkt des Deckels
        feder_hebelarm_mm: Abstand Drehachse → Federanlenkung
        anzahl_federn: Anzahl der Gasdruckfedern (Standard: 2)
        sicherheitsfaktor: Aufschlag für Reibung/Wind (Standard: 1.3)
        oeffnungswinkel_grad: Maximaler Öffnungswinkel (Standard: 90°)

    Returns:
        dict mit benötigter Kraft je Feder [N], empfohlener Hublänge [mm],
        Einbaulänge [mm] und Temperaturkompensation.
    """
    import math

    g = 9.81  # m/s²
    gewichtskraft_n = lukengewicht_kg * g

    # Drehmoment des Deckels bei 0° (geschlossen, maximal)
    drehmoment_max_nmm = gewichtskraft_n * schwerpunktabstand_mm

    # Erforderliche Federkraft pro Feder
    kraft_pro_feder_n = (drehmoment_max_nmm / feder_hebelarm_mm) / anzahl_federn
    kraft_mit_sicherheit_n = kraft_pro_feder_n * sicherheitsfaktor

    # Hublänge aus Geometrie
    hub_mm = 2.0 * feder_hebelarm_mm * math.sin(
        math.radians(oeffnungswinkel_grad / 2.0)
    )

    # Einbaulänge (Faustregel: Hub × 2.5)
    einbaulaenge_mm = hub_mm * 2.5

    return {
        "kraft_pro_feder_n": round(kraft_mit_sicherheit_n, 1),
        "hub_mm": round(hub_mm, 1),
        "einbaulaenge_mm": round(einbaulaenge_mm, 1),
        "temperaturkompensation": {
            "minus_20c": round(kraft_mit_sicherheit_n * 0.70, 1),
            "plus_0c": round(kraft_mit_sicherheit_n * 0.85, 1),
            "plus_20c": round(kraft_mit_sicherheit_n * 1.00, 1),
            "plus_40c": round(kraft_mit_sicherheit_n * 1.10, 1),
            "plus_60c": round(kraft_mit_sicherheit_n * 1.20, 1),
        },
        "hinweis": (
            "Temperaturbereich -20°C bis +60°C. "
            "Stickstoff-Füllung verliert ca. 3–4% Kraft pro 10°C Abkühlung. "
            "Einbaulage: Kolbenstange nach unten für längere Lebensdauer."
        ),
    }
```

### Referenzwerte: Typische Gasdruckfeder-Dimensionierung

| Lukendeckel-Typ | Gewicht [kg] | Kraft/Feder [N] | Hub [mm] | Einbaulänge [mm] | Kolben-Ø [mm] |
|-----------------|-------------|-----------------|----------|-------------------|---------------|
| Vorluke 400×400 | 4–8 | 80–160 | 150–200 | 375–500 | 8 |
| Vorluke 500×500 | 6–12 | 120–250 | 180–250 | 450–625 | 10 |
| Decksluke 600×600 | 10–20 | 200–400 | 220–300 | 550–750 | 10 |
| Motorraumluke 700×800 | 15–35 | 300–700 | 250–350 | 625–875 | 15 |
| Lazarette 800×600 | 12–25 | 250–500 | 200–280 | 500–700 | 10 |
| Superyacht-Luke 1000×800 | 25–60 | 500–1200 | 300–450 | 750–1125 | 15–20 |

### Montagegeometrie: Anlenkpunkte

```
Seitenansicht (Luke geschlossen):

        Drehachse (Scharnier)
            ↓
    ────────●──────────────────── Deck
            │╲  α = Anlenkwinkel
            │  ╲
            │    ● Feder-Befestigung (Deckel)
            │    │
            │    │  ← Gasdruckfeder
            │    │
            ●────┘  Feder-Befestigung (Rumpf/Süll)
         Abstand b

Optimaler Anlenkwinkel α bei geschlossener Luke: 5–15°
  → Zu klein (<5°): Feder kann Luke nicht öffnen (Totpunkt-Nähe)
  → Zu groß (>20°): Feder ragt in Durchgang, hohe Querkräfte

Hebelarm-Verhältnis:
  feder_hebelarm / schwerpunktabstand = 0.4–0.7 (optimal: 0.5–0.6)
```

### Temperaturkompensation

Gasdruckfedern sind temperaturempfindlich. Der Innendruck (Stickstoff) folgt annähernd dem idealen Gasgesetz:

```
F(T) = F(20°C) × (T + 273.15) / (20 + 273.15)

Vereinfacht (Linearisierung im Arbeitsbereich):
  F(T) ≈ F(20°C) × (1 + 0.0034 × (T - 20))

Praxis-Korrekturfaktoren:
  -20°C: ×0.70  (Winterlager Skandinavien)
   +0°C: ×0.85  (Wintersaison Mittelmeer)
  +20°C: ×1.00  (Referenz)
  +40°C: ×1.10  (Hochsommer, dunkle Decks)
  +60°C: ×1.20  (direkte Sonneneinstrahlung auf schwarzer Fläche)
```

**Konsequenz für die Auslegung:** Federn werden bei +20°C spezifiziert. Bei Yachten in tropischen Revieren (Karibik, SO-Asien) ist +40°C Deckstemperatur normal — die Luken werden „zu leicht" aufspringen. Bei Winterlager in Nordeuropa können Luken schwergängig werden. Empfehlung: Auslegung bei +25°C als Kompromiss.

### Scharnier-Lastberechnung

```python
def scharnier_last_berechnen(
    lukengewicht_kg: float,
    lukenbreite_mm: float,
    anzahl_scharniere: int = 2,
    oeffnungswinkel_grad: float = 90.0,
) -> dict:
    """
    Berechnet die statische und dynamische Last auf Lukenscharniere.
    """
    import math

    g = 9.81
    gewichtskraft_n = lukengewicht_kg * g

    # Statische Last pro Scharnier (vertikal, Luke geschlossen)
    last_statisch_n = gewichtskraft_n / anzahl_scharniere

    # Dynamische Zuschläge
    wind_faktor = 1.5       # Windlast auf offene Luke
    see_faktor = 2.0        # Seegang-Beschleunigung (bis 2g)
    schlag_faktor = 3.0     # Schlagartige Belastung (Zuschlagen)

    # Auszugskraft bei offener Luke (Hebelarm = halbe Lukenbreite)
    hebelarm_mm = lukenbreite_mm / 2.0
    auszugskraft_n = (gewichtskraft_n * hebelarm_mm) / (lukenbreite_mm / anzahl_scharniere)

    return {
        "last_statisch_pro_scharnier_n": round(last_statisch_n, 1),
        "last_wind_n": round(last_statisch_n * wind_faktor, 1),
        "last_seegang_n": round(last_statisch_n * see_faktor, 1),
        "last_schlagartig_n": round(last_statisch_n * schlag_faktor, 1),
        "auszugskraft_pro_scharnier_n": round(auszugskraft_n, 1),
        "empfehlung_schrauben": {
            "min_anzahl": max(4, anzahl_scharniere * 3),
            "min_durchmesser_mm": 5 if lukengewicht_kg < 15 else 6,
            "material": "A4-70 (316L)",
            "gewinde": "metrisch",
        },
        "empfehlung_backing_plate": (
            "Erforderlich bei Sandwich-Bauweise. "
            f"Min. Dicke: {max(3, round(lukengewicht_kg * 0.2))} mm Edelstahl "
            "oder Aluminium."
        ),
    }
```

---

## Einbau-/Austausch-Anleitung

### Gasdruckfeder: Austausch (Schritt-für-Schritt)

**Werkzeug:**
- Gabelschlüssel 10mm, 13mm
- Sicherungsring-Zange (Seeger)
- Loctite 243 (mittelfest)
- Silikonspray (NICHT Öl — greift Dichtungen an)
- Drehmomentschlüssel 5–25 Nm
- Schutzbrille (Federn stehen unter Druck)

**Vorbereitung:**
1. Luke vollständig öffnen und mit Hilfsstütze sichern (NIEMALS nur auf der alten Feder abstützen)
2. Neue Feder auf korrekte Spezifikation prüfen: Kraft [N], Hub [mm], Einbaulänge [mm]
3. Temperaturausgleich: Neue Feder min. 2h an Umgebungstemperatur anpassen

**Ausbau (alte Feder):**
1. Sicherungsclip am Kugelkopf (Deckelseite) entfernen
2. Feder vom oberen Kugelbolzen abheben (Deckel-Seite zuerst)
3. Unteren Kugelbolzen lösen (Rumpf-Seite)
4. Alte Feder entsorgen (Sondermüll — unter Gasdruck, nicht anbohren)

**Einbau (neue Feder):**
1. Kugelbolzen auf Verschleiß prüfen — Kugelkopf darf max. 0.2mm Spiel haben
2. Bei Bedarf Kugelbolzen erneuern (immer paarweise)
3. Untere Befestigung (Rumpf-Seite) montieren — Schrauben mit Loctite 243
4. Feder auf unteren Kugelbolzen aufsetzen — Kolbenstange zeigt NACH UNTEN
5. Luke anheben, oberen Kugelbolzen einrasten — Sicherungsclip einsetzen
6. Hilfsstütze entfernen, Luke vorsichtig loslassen — Feder muss Luke halten
7. Funktionstest: 10× öffnen/schließen, auf gleichmäßigen Widerstand prüfen
8. Anzugsmomente kontrollieren: M6 = 8–10 Nm, M8 = 15–20 Nm

**Kolbenstange nach unten — warum?**
Die Dichtung der Gasdruckfeder wird durch ein Ölpolster geschmiert. Zeigt die Kolbenstange nach oben, läuft das Öl vom Dichtring weg → Lebensdauer sinkt um 30–50%. Ausnahme: Federn mit „Alllagen-Dichtung" (z.B. Stabilus LIFT-O-MAT mit Endlagendämpfung).

### Scharnier: Einbau (Neuinstallation)

**Werkzeug:**
- Bohrmaschine mit Edelstahl-Bohrern (HSS-Co oder TiN-beschichtet)
- Stufenbohrer für Senkungen
- Gewindeschneider (bei Alu-Backing-Plate)
- Sikaflex 291 oder 3M 5200 (Abdichtung)
- Aceton (Reinigung)
- Klebeband (Bohrschablone fixieren)

**Vorgehensweise:**

1. **Position anreißen:**
   - Scharniere am Lukenrahmen ausrichten (Flucht der Drehachse prüfen)
   - Abstand Scharnier → Lukenecke: min. 50mm
   - Scharniermitte → Scharniermitte: möglichst gleichmäßig verteilt
   - Bohrschablone mit Klebeband fixieren, Körner setzen

2. **Bohren:**
   - Vorbohren 3mm (Führungsbohrung)
   - Aufbohren auf Schraubendurchmesser + 0.5mm
   - Bei Sandwich-Kern: Kernbereich mit Epoxid verfüllen (24h aushärten lassen)
   - Senkung für Schraubenkopf fräsen (wenn bündig erforderlich)

3. **Abdichten:**
   - Bohrlöcher mit Sikaflex 291 füllen (KEIN Silikon — haftet nicht auf GFK)
   - Scharnier-Auflagefläche dünn mit Sikaflex bestreichen
   - Schrauben einsetzen, Überschuss abwischen

4. **Montage:**
   - Schrauben handfest anziehen (Sikaflex darf nicht vollständig verdrängt werden)
   - 24h aushärten lassen
   - Endgültiges Drehmoment anziehen: M5 = 5–7 Nm, M6 = 8–10 Nm
   - Scharnierstift auf Leichtgängigkeit prüfen, ggf. PTFE-Spray

5. **Kontrolle:**
   - Luke 20× öffnen/schließen
   - Spaltmaß prüfen: gleichmäßig umlaufend ±1mm
   - Dichtsitz der Gummidichtung visuell prüfen
   - Schrauben nach 1 Woche nachziehen (Sikaflex-Setzung)

### Verschluss/Riegel: Austausch

1. Alten Riegel demontieren — Schrauben aufheben (Maßreferenz)
2. Gewindeeinsätze auf Festsitz prüfen — bei Ausriss: Helicoil-Einsatz setzen
3. Neuen Riegel probeweise aufsetzen — Bohrungsmuster vergleichen
4. Falls abweichend: Adapterplatte aus 3mm V4A fertigen
5. Dichtfläche des Riegels mit Vaseline (temporär) oder PTFE-Paste (dauerhaft) behandeln
6. Montage mit Loctite 243, Anzug M5 = 5–7 Nm
7. Schließmechanismus einstellen: Riegel soll mit einer Hand bedienbar sein
8. Dichtungskompression prüfen: 1.5–2.5mm Verformung bei geschlossener Luke

---

## Lebensdauer und Alterungsmechanismen

### Gasdruckfedern (Lebensdauer: 3–5 Jahre / 10.000–25.000 Zyklen)

**Primärer Verschleißmechanismus:** Gasverlust durch Dichtungsdiffusion
- Stickstoff diffundiert durch die Kolbenstangendichtung (PTFE/NBR)
- Verlustrate: 2–5% pro Jahr bei Qualitätsfedern, 5–15% bei Billigfedern
- Sichtbar als: Luke öffnet langsamer, bleibt nicht mehr offen, fällt zu

**Sekundäre Alterung:**
- UV-Degradation der Dichtung: Kolbenstange wird ölig, Schmierfett tritt aus
- Korrosion der Kolbenstange (bei ungeschütztem Stahl): Riefen → Dichtungsbeschädigung
- Salzwasser-Kontakt: Lochfraß an Befestigungen, Kugelbolzen-Korrosion

**Lebensdauer-Verlängerung:**
- Kolbenstange nach unten montieren: +30–50% Lebensdauer
- Regelmäßig mit Süßwasser abspülen: +20%
- Silikonspray auf Kolbenstange (2×/Jahr): +15%
- Qualitätsfeder (Stabilus, Suspa, Bansbach): 2–3× länger als No-Name

### Scharniere (Lebensdauer: 15+ Jahre)

**Primärer Verschleißmechanismus:** Scharnierstift-Abrieb
- Stift und Buchse reiben bei jeder Betätigung
- Spiel nimmt zu: 0.1mm/Jahr bei Edelstahl, 0.05mm/Jahr bei Bronze
- Sichtbar als: Luke „klappert", ungleichmäßiges Spaltmaß

**Sekundäre Alterung:**
- Spaltkorrosion (316L in stagnierenden Bereichen): Braunfärbung, Festfressen
- Elektrolytische Korrosion bei Materialmix (Alu-Luke + Edelstahl-Scharnier)
- Ermüdung der Schraubverbindung durch Vibrationen

**Lebensdauer-Verlängerung:**
- Jährlich Scharnierstift ausbauen, reinigen, mit Teflon-Fett schmieren
- Opferanode an Alu-Konstruktionen in Scharniernähe
- Schrauben alle 2 Jahre auf Festsitz prüfen (Vibrationslösung)

### Riegel und Verschlüsse (Lebensdauer: 8–12 Jahre)

**Primärer Verschleißmechanismus:** Nocken-/Cam-Abrieb
- Schließnocken und Gegenplatte verschleißen → Schließkraft nimmt ab
- Sichtbar als: Riegel hält nicht mehr, Luke öffnet bei Seegang

**Sekundäre Alterung:**
- Feder im Riegelmechanismus ermüdet (bei Federverschlüssen)
- Betätigungshebel wird „weich" (Spiel in Achse nimmt zu)
- Gummidichtung im Riegel-Bereich altert schneller (Kompression)

**Lebensdauer-Verlängerung:**
- Nockenflächen 1×/Jahr mit Teflon-Spray behandeln
- Dichtungskompression prüfen: bei <1mm Verformung → Dichtung tauschen
- Bei Seewasserkontakt: Riegel nach jeder Fahrt mit Süßwasser spülen

### Zusammenfassung: Wartungsintervalle

| Komponente | Inspektion | Wartung | Austausch |
|------------|-----------|---------|-----------|
| Gasdruckfeder | Alle 6 Monate | Kolbenstange reinigen, Silikonspray 2×/Jahr | 3–5 Jahre |
| Scharnier (Edelstahl) | Jährlich | Stift schmieren 1×/Jahr | 15–25 Jahre |
| Scharnier (Bronze) | Jährlich | Stift schmieren 1×/Jahr | 20–30 Jahre |
| Riegel/Verschluss | Alle 6 Monate | Nocken schmieren, Dichtung prüfen | 8–12 Jahre |
| Kugelbolzen | Jährlich | Auf Spiel prüfen | 5–8 Jahre |
| Dichtungsgummi | Alle 6 Monate | Reinigen, Silikonpflege | 5–8 Jahre |
| Schraubverbindungen | Jährlich | Drehmoment nachprüfen | Bei Korrosion |
| Backing-Plates | Alle 2 Jahre | Visuelle Kontrolle | Bei Verformung |

---

## Fehlerbild-Atlas

### FB-01: Gasdruckfeder defekt — Luke fällt zu

**Fehlerbild:** Luke bleibt nicht mehr in geöffneter Position, sinkt langsam ab oder fällt schlagartig zu.
**Ursache:** Gasverlust durch Dichtungsverschleiß, UV-Alterung der Dichtung, Kolbenstangenkorrosion.
**Erkennung:** Sichtprüfung: Ölspuren an der Kolbenstange, Luke hält nicht bei 90°, Feder lässt sich von Hand komprimieren.
**Gefährdung:** HOCH — Verletzungsgefahr durch zufallende Luke (Kopf, Hände, Finger).
**Sofortmaßnahme:** Luke mit Holzkeil oder Leinensicherung fixieren. Feder als defekt markieren.
**Behebung:** Gasdruckfeder austauschen (siehe Einbau-Anleitung). Immer paarweise tauschen.
**Kosten:** Material 25–80 EUR/Stück, Einbau 30–60 min, Werft 80–200 EUR.
**Bewertung:** score_abzug = 35, confidence = visual_high
**Referenz:** ISO 12216, Abschnitt 6.4 — Sicherung gegen unbeabsichtigtes Schließen
**Vermeidung:** Regelmäßiger Austausch alle 4 Jahre, Kolbenstange nach unten montieren.
**Häufigkeit:** Sehr häufig (>40% aller Luken nach 5 Jahren betroffen).
**Bootsklasse:** Alle Klassen, besonders Serienboote mit Billigfedern.

### FB-02: Korrodiertes Scharnier — Festsitzen / Schwergängigkeit

**Fehlerbild:** Scharnier lässt sich nur unter erhöhtem Kraftaufwand bewegen, quietscht, oder ist vollständig festgefressen.
**Ursache:** Spaltkorrosion (316L), galvanische Korrosion (Materialmix), mangelnde Schmierung.
**Erkennung:** Rostbraune Verfärbung am Scharnierstift, Luke öffnet nicht mehr gleichmäßig, Knirschgeräusche.
**Gefährdung:** MITTEL — Eingeschränkte Fluchtmöglichkeit bei Notfall-Evakuierung.
**Sofortmaßnahme:** Kriechöl (WD-40 oder Caramba) einsprühen, 30 min einwirken lassen, vorsichtig bewegen.
**Behebung:** Scharnierstift ausbauen, mit Schmirgelpapier K400 glätten, Teflon-Fett auftragen. Bei starker Korrosion: Scharnier komplett tauschen.
**Kosten:** Reinigung/Schmierung 20–40 EUR, Austausch 80–250 EUR/Scharnier inkl. Einbau.
**Bewertung:** score_abzug = 20, confidence = visual_medium
**Referenz:** ISO 15085 — Rettungswege und Fluchtwege auf Sportbooten
**Vermeidung:** Jährliche Schmierung, kein Materialmix (Alu + Edelstahl ohne Isolation).
**Häufigkeit:** Häufig bei Booten >8 Jahre, besonders Tropenreviere.
**Bootsklasse:** Alle, verstärkt bei Alu-Yachten.

### FB-03: Gebrochener Riegel / Verschluss

**Fehlerbild:** Riegelmechanismus lässt sich nicht mehr schließen, Hebel bricht ab, oder Riegel löst sich vom Rahmen.
**Ursache:** Materialermüdung (Zink-Druckguss), Korrosion der Befestigung, Überlastung durch Seegang.
**Erkennung:** Sichtbarer Bruch, Riegel lose, Schließmechanismus ohne Widerstand.
**Gefährdung:** HOCH — Luke kann bei Seegang aufschlagen, Wassereinbruch bei Übernahme.
**Sofortmaßnahme:** Luke mit Spanngurt oder Leine sichern. Nicht auf See gehen.
**Behebung:** Riegel komplett tauschen. Bei Ausriss: Backing-Plate verstärken, Helicoil-Gewindeeinsätze.
**Kosten:** Material 30–120 EUR, Einbau 45–90 min, Werft 100–250 EUR.
**Bewertung:** score_abzug = 40, confidence = visual_high
**Referenz:** CE-Kategorie-Anforderungen — Wasserdichtigkeit von Öffnungen
**Vermeidung:** Keine Zink-Druckguss-Riegel in Seewasserumgebung, nur 316L oder Bronze.
**Häufigkeit:** Mittel, besonders bei Billig-Hardware nach 5–8 Jahren.
**Bootsklasse:** Serienboote 8–14m, häufig bei Charterbooten.

### FB-04: Festsitzendes Schloss — Schlüssel dreht nicht

**Fehlerbild:** Schließzylinder blockiert, Schlüssel lässt sich nicht drehen oder abziehen.
**Ursache:** Salzablagerung im Zylinder, Korrosion der Zuhaltungen, verformter Schlüssel.
**Erkennung:** Schlüssel dreht schwer, knirscht, oder blockt vollständig.
**Gefährdung:** NIEDRIG — Zugang eingeschränkt, aber keine direkte Sicherheitsgefahr.
**Sofortmaßnahme:** Grafitspray in Schlüsselloch sprühen (KEIN Öl — bindet Schmutz).
**Behebung:** Zylinder ausbauen, in Ultraschallbad reinigen, Zuhaltungen prüfen. Bei schwerer Korrosion: Zylinder tauschen.
**Kosten:** Reinigung 15–30 EUR, Zylindertausch 40–120 EUR.
**Bewertung:** score_abzug = 10, confidence = visual_medium
**Referenz:** Herstellerangaben zum Wartungsintervall
**Vermeidung:** Alle 3 Monate Grafitspray, Schutzklappe über Schlüsselloch.
**Häufigkeit:** Häufig bei Außenluken, besonders im Cockpitbereich.
**Bootsklasse:** Alle Klassen.

### FB-05: Lose Schrauben — Scharnier/Riegel wackelt

**Fehlerbild:** Beschlag sitzt nicht mehr fest, wackelt bei Belastung, Schrauben drehen durch.
**Ursache:** Vibrationslösung (kein Loctite verwendet), Holzquellling/Schrumpfung, Kernmaterial-Ausriss bei Sandwich.
**Erkennung:** Sichtbares Spiel, Klapper-Geräusche, Schraubenköpfe stehen hervor.
**Gefährdung:** MITTEL — Beschlag kann sich bei Seegang vollständig lösen.
**Sofortmaßnahme:** Schrauben nachziehen (wenn sie noch greifen). Bei Durchdrehen: provisorische Fixierung mit Kabelbinder.
**Behebung:** Schrauben raus, Löcher mit Epoxid-Filler füllen, 24h aushärten, neu bohren (nächste Größe). Loctite 243 verwenden.
**Kosten:** Material 5–15 EUR, Einbau 30–60 min, Werft 60–150 EUR.
**Bewertung:** score_abzug = 20, confidence = visual_high
**Referenz:** ISO 12216 — Befestigungsanforderungen für Lukenbeschläge
**Vermeidung:** Schraubensicherung (Loctite 243), jährliche Drehmomentprüfung.
**Häufigkeit:** Sehr häufig bei Booten >5 Jahre, besonders bei Motorbooten (Vibration).
**Bootsklasse:** Alle, verstärkt Motorboote und Segelyachten mit Motorsailer-Nutzung.

### FB-06: Gerissene Montageplatte / Backing-Plate

**Fehlerbild:** Die Verstärkungsplatte unter dem Beschlag zeigt Risse, ist verformt oder gebrochen.
**Ursache:** Unterdimensionierung, Ermüdung durch zyklische Belastung, Korrosion (bei Alu ohne Anodisierung).
**Erkennung:** Risse um Schraubenlöcher sichtbar, Beschlag „federt" bei Belastung, Gelcoat-Risse um Befestigung.
**Gefährdung:** HOCH — Beschlagausriss mit Deckschäden möglich.
**Sofortmaßnahme:** Belastung reduzieren, Luke nicht bei Seegang öffnen.
**Behebung:** Backing-Plate komplett erneuern: min. 4mm V4A oder 6mm Alu (anodisiert), größere Fläche als Original.
**Kosten:** Material 20–60 EUR, Einbau 60–120 min (Innenverkleidung demontieren), Werft 150–400 EUR.
**Bewertung:** score_abzug = 30, confidence = visual_medium
**Referenz:** ISO 12216 — Strukturelle Anforderungen Lukenmontage
**Vermeidung:** Großflächige Backing-Plates bei Erstmontage, Lastverteilung berechnen.
**Häufigkeit:** Mittel, besonders bei nachgerüsteten Luken und Sandwich-Decks.
**Bootsklasse:** Alle mit Sandwich-Bauweise, besonders Serienboote.

### FB-07: UV-degradierte Lukendichtung

**Fehlerbild:** Dichtungsgummi ist hart, rissig, verformt oder hat keine Rückstellkraft mehr.
**Ursache:** UV-Strahlung zersetzt EPDM/Neopren, Ozon-Alterung, mechanische Kompression (Druckverformungsrest).
**Erkennung:** Dichtung zeigt Risse (Krokodilhaut-Muster), ist flachgedrückt (Querschnitt <50% des Originals), klebt am Rahmen.
**Gefährdung:** MITTEL — Wassereinbruch bei Regen und Seegangübernahme.
**Sofortmaßnahme:** Dichtungsoberfläche mit Silikonpflegemittel behandeln (temporär).
**Behebung:** Dichtung komplett erneuern. Altes Profil als Muster verwenden, Meterware zuschneiden, Eckverbindungen vulkanisieren oder kleben.
**Kosten:** Material 5–15 EUR/m, Einbau 30–60 min/Luke, Werft 80–200 EUR/Luke.
**Bewertung:** score_abzug = 15, confidence = visual_high
**Referenz:** ISO 12216 — Dichtungsanforderungen für Luken und Fenster
**Vermeidung:** UV-Schutzabdeckungen bei Langzeitliegeplatz, Silikonpflege 2×/Jahr.
**Häufigkeit:** Sehr häufig, >60% aller Boote >7 Jahre.
**Bootsklasse:** Alle Klassen, besonders Tropenreviere und Mittelmeer.

### FB-08: Falsche Gasdruckfeder-Kraft

**Fehlerbild:** Luke springt unkontrolliert auf (Feder zu stark) oder öffnet kaum (Feder zu schwach).
**Ursache:** Falsche Feder bestellt, Temperatureffekt nicht berücksichtigt, Luke nachträglich beschwert (Solarpanel).
**Erkennung:** Luke schlägt beim Öffnen unkontrolliert auf (zu stark) oder bleibt bei 30–45° stehen (zu schwach).
**Gefährdung:** MITTEL — Unkontrolliert aufschlagende Luke kann Beschläge beschädigen und Verletzungen verursachen.
**Sofortmaßnahme:** Bei zu starker Feder: Lukenanschlag prüfen/verstärken. Bei zu schwacher Feder: Hilfsstütze verwenden.
**Behebung:** Korrekte Kraft berechnen (siehe Berechnungsabschnitt), passende Feder bestellen und tauschen.
**Kosten:** Material 25–80 EUR/Stück, Einbau 20–40 min.
**Bewertung:** score_abzug = 15, confidence = visual_medium
**Referenz:** Herstellerdatenblatt der Gasdruckfeder
**Vermeidung:** Kraft immer berechnen, nie schätzen. Temperaturbereich berücksichtigen.
**Häufigkeit:** Mittel, besonders bei Eigeneinbau und After-Market-Federn.
**Bootsklasse:** Alle Klassen.

### FB-09: Fehlende Sicherheitsfangvorrichtung (Safety Catch)

**Fehlerbild:** Luke kann über den vorgesehenen Öffnungswinkel hinaus aufschlagen, kein Fangband oder -seil vorhanden.
**Ursache:** Bei Erstmontage vergessen, Fangband gerissen/korrodiert, Fangvorrichtung bei Wartung nicht wieder montiert.
**Erkennung:** Luke öffnet >90° ohne Widerstand, Fangband-Befestigung sichtbar aber leer.
**Gefährdung:** MITTEL — Überdehnung der Scharniere, Deckelbeschädigung, Verletzungsgefahr.
**Sofortmaßnahme:** Provisorisches Fangband aus Leine mit Knoten als Längenbegrenzung anbringen.
**Behebung:** Fangband aus Edelstahl-Kette (3mm) oder Edelstahl-Drahtseil (4mm) mit Pressklemmen montieren.
**Kosten:** Material 10–30 EUR, Einbau 20–40 min.
**Bewertung:** score_abzug = 20, confidence = visual_high
**Referenz:** ISO 12216 — Öffnungsbegrenzung
**Vermeidung:** Bei jeder Wartung Fangvorrichtung auf Intaktheit prüfen.
**Häufigkeit:** Mittel, oft bei DIY-Lukenumbauten.
**Bootsklasse:** Alle Klassen.

### FB-10: Verschlissener Schließnocken (Cam Wear)

**Fehlerbild:** Riegelverschluss schließt nicht mehr satt, Hebel hat kein „Einrasten" mehr, Luke klappert bei Seegang.
**Ursache:** Abrieb an Nocke und Gegenplatte durch tausende Schließzyklen, Korrosion beschleunigt Verschleiß.
**Erkennung:** Nocke zeigt glänzende Abriebspuren, Hebel schließt ohne Widerstand, Spiel >1mm.
**Gefährdung:** MITTEL — Unzureichende Dichtung, Klappergeräusche, bei Seegang Luke-Öffnung möglich.
**Sofortmaßnahme:** Unterlage (Edelstahl-Shim 0.5mm) unter Gegenplatte als Ausgleich.
**Behebung:** Nocke und Gegenplatte als Paar tauschen (nicht einzeln — ungleichmäßiger Verschleiß).
**Kosten:** Material 15–45 EUR/Satz, Einbau 20–30 min.
**Bewertung:** score_abzug = 15, confidence = visual_medium
**Referenz:** Herstellerangaben zum Nockenverschleiß
**Vermeidung:** Nockenflächen 1×/Jahr mit Teflon-Spray behandeln, saubere Dichtflächen.
**Häufigkeit:** Häufig bei Booten >10 Jahre.
**Bootsklasse:** Alle, verstärkt bei häufig genutzten Hauptluken.

### FB-11: Delaminierte Beschlag-Unterfütterung

**Fehlerbild:** Beschlagmontage zeigt „Pumpen" — Beschlag hebt sich bei Belastung sichtbar vom Deck ab und senkt sich wieder.
**Ursache:** Wassereintritt durch undichte Schraubenlöcher hat Kernmaterial (Balsa, Schaum) zum Quellen/Faulen gebracht.
**Erkennung:** Weiches Gefühl beim Drücken neben dem Beschlag, Wasseraustritt bei Belastung, Verfärbung im Gelcoat.
**Gefährdung:** HOCH — Fortschreitende Delamination bis zum Strukturversagen des Decks.
**Sofortmaßnahme:** Beschlag entlasten, Bereich trocknen (Heizlüfter, min. 48h).
**Behebung:** Beschlag demontieren, delaminierten Kern freilegen, mit Epoxid-Harz injizieren oder Kern ersetzen, neue Backing-Plate, neu montieren.
**Kosten:** Reparatur 200–800 EUR je nach Schadensumfang, Werft 400–1500 EUR.
**Bewertung:** score_abzug = 40, confidence = visual_medium
**Referenz:** ISO 12215 — Rumpfbau und Deckskonstruktion
**Vermeidung:** ALLE Bohrlöcher im Sandwich-Deck mit Sikaflex abdichten, Backing-Plates verwenden.
**Häufigkeit:** Häufig bei Sandwich-Decks >10 Jahre, besonders Balsa-Kern.
**Bootsklasse:** Serienboote und Semi-Custom mit Sandwich-Bauweise.

### FB-12: Vibrations-Ermüdung an Beschlagbefestigung

**Fehlerbild:** Schrauben zeigen Ermüdungsbruch (glatte Bruchfläche), Beschlag hat sich ohne sichtbare Korrosion gelöst.
**Ursache:** Zyklische Belastung durch Motorvibrationen oder Seegangsbeschleunigung, fehlende Schraubensicherung.
**Erkennung:** Glatte, muschelige Bruchfläche an Schrauben (≠ Gewaltbruch), mehrere Schrauben gleichzeitig betroffen.
**Gefährdung:** HOCH — Plötzliches Beschlagversagen ohne Vorwarnung.
**Sofortmaßnahme:** Alle Beschläge in vibrations-exponierter Zone auf Festsitz prüfen.
**Behebung:** Neue Schrauben (A4-80 statt A4-70 für höhere Festigkeit), Loctite 243, ggf. Federringe oder Nordlock-Scheiben.
**Kosten:** Material 10–30 EUR, Einbau 30–60 min.
**Bewertung:** score_abzug = 30, confidence = visual_high
**Referenz:** DIN 267-26 — Mechanische Verbindungselemente, Schwingfestigkeit
**Vermeidung:** Loctite 243 bei Erstmontage, jährliche Kontrolle, Nordlock-Scheiben bei Motorraum-Luken.
**Häufigkeit:** Mittel bei Motorbooten, selten bei Segelbooten.
**Bootsklasse:** Motorboote und Motorsailer, besonders im Maschinenraumbereich.

---

## Fehlerbehebungs-Leitfaden

### Problem 1: Luke ist undicht trotz neuer Dichtung

**Symptom:** Wassereinbruch bei Regen oder Seegangübernahme, obwohl die Dichtung kürzlich erneuert wurde.

**Diagnose-Schritte:**
1. Dichtungsprofil prüfen: Stimmt der Querschnitt? (Zu dünn = zu wenig Kompression, zu dick = Luke schließt nicht vollständig)
2. Eckverbindungen prüfen: Sind die Ecken gestoßen oder auf Gehrung? (Stoß = Kapillarweg für Wasser)
3. Rahmen-Ebenheit prüfen: Haarlineal auf Süllrand, Spaltmaß <0.5mm? (Verzug = lokale Undichtigkeit)
4. Riegel-Schließkraft prüfen: Drückt der Riegel die Luke gleichmäßig auf die Dichtung? (Ungleichmäßig = einseitige Undichtigkeit)
5. Wassertest: Gartenschlauch von unten nach oben abschnittsweise, Eindringpunkt lokalisieren.

**Lösung:**
- Querschnitt falsch: Richtige Dichtung besorgen (Herstellerprofil bestellen, nicht Universal)
- Eckverbindungen undicht: Ecken mit Sikaflex 291 nacharbeiten oder vulkanisieren
- Rahmen verzogen: Unterfütterung mit Epoxid-Filler auf Süllrand, Oberfläche plan schleifen
- Schließkraft ungleich: Gegenplatten-Position justieren, ggf. Shims verwenden
- **Kosten:** 30–200 EUR je nach Ursache

### Problem 2: Gasdruckfeder verliert nach 6 Monaten bereits Kraft

**Symptom:** Neue Feder hält Luke nicht mehr, obwohl sie erst kürzlich eingebaut wurde.

**Diagnose-Schritte:**
1. Einbaulage prüfen: Kolbenstange nach unten? (Falsch montiert = drastischer Lebensdauerverlust)
2. Spezifikation prüfen: Stimmt die Newton-Angabe auf der Feder mit der Berechnung überein?
3. Markenqualität: Ist die Feder von einem Markenhersteller oder No-Name?
4. Temperaturcheck: Wurde die Feder bei extremer Hitze gelagert? (>60°C im Versandkarton auf Deck)
5. Kolbenstange inspizieren: Kratzer, Dellen, Korrosion? (Beschädigte Stange = sofortige Dichtungsschäden)

**Lösung:**
- Falsche Einbaulage: Umdrehen (Kolbenstange nach unten)
- Falsche Kraft: Korrekt dimensionierte Feder bestellen
- Billigfeder: Qualitätshersteller wählen (Stabilus, Suspa, Bansbach)
- Beschädigte Kolbenstange: Feder sofort ersetzen
- **Kosten:** 25–80 EUR für Ersatzfeder

### Problem 3: Luke klemmt bei Kälte, geht bei Hitze zu leicht auf

**Symptom:** Saisonale Schwankung des Öffnungsverhaltens.

**Diagnose-Schritte:**
1. Gasdruckfeder-Typ prüfen: Standard oder temperaturkompensiert?
2. Temperaturbereich des Reviers erfassen (Sommer/Winter-Extremwerte)
3. Federauslegung prüfen: Bei welcher Temperatur wurde die Feder dimensioniert?

**Lösung:**
- Feder auf mittlere Jahrestemperatur des Reviers auslegen (nicht auf +20°C Laborwert)
- Für extreme Reviere: Temperaturkompensierte Federn (z.B. Stabilus LIFT-O-MAT mit Temperaturdämpfung)
- Alternative: Feststellmechanismus nachrüsten (Arretierstange), der temperaturunabhängig ist
- **Kosten:** 40–120 EUR für kompensierte Feder, 30–60 EUR für Arretierstange

### Problem 4: Scharnier quietscht trotz Schmierung

**Symptom:** Unangenehmes Quietschen beim Öffnen/Schließen, auch nach Schmierung.

**Diagnose-Schritte:**
1. Schmiermitteltyp prüfen: Wurde das richtige Mittel verwendet? (Öl = falsch, Teflon-Fett = richtig)
2. Scharnierstift-Zustand: Riefen, Korrosionsnarben, Verformung?
3. Buchsen-Zustand: Ovalisiert, verschlissen?
4. Ausrichtung: Sind alle Scharniere einer Luke exakt fluchtend montiert?

**Lösung:**
- Falsches Schmiermittel: Scharnier komplett reinigen (Aceton), dann Teflon-Fett (z.B. Molykote EM-30L)
- Beschädigte Oberfläche: Scharnierstift mit K600-Schleifpapier glätten, bei tiefen Riefen: Stift tauschen
- Verschlissene Buchsen: Buchsen erneuern (Nachrüst-Buchsen aus PTFE-beschichtetem Bronze)
- Fluchtungsfehler: Scharniere lösen, Luke exakt positionieren, Scharniere nacheinander fixieren
- **Kosten:** 10–50 EUR (Schmierung/Stift), 80–200 EUR (Buchsen/Neuausrichtung)

### Problem 5: Mehrere Riegel derselben Luke schließen nicht gleichzeitig

**Symptom:** Ein Riegel schließt, aber die gegenüberliegende Seite steht noch offen, oder die Riegel „klemmen" bei gleichzeitiger Betätigung.

**Diagnose-Schritte:**
1. Rahmenverzug messen: Diagonalen des Lukenrahmens vergleichen (Differenz >2mm = Verzug)
2. Dichtungsquerschnitt messen: Ist die Dichtung umlaufend gleich dick?
3. Gegenplatten-Position prüfen: Sind alle Gegenplatten auf gleicher Höhe?
4. Riegelverschleiß: Sind alle Nocken gleich abgenutzt?

**Lösung:**
- Rahmenverzug: Unterlegen mit Shims, bei starkem Verzug: Rahmen richten (Werft)
- Ungleiche Dichtung: Dichtung komplett erneuern (nie abschnittsweise)
- Gegenplatten: Höhe mit Shims ausgleichen (0.5mm-Edelstahl-Scheiben)
- Verschleiß: Alle Nocken und Gegenplatten als Satz tauschen
- **Kosten:** 30–100 EUR (Shimming), 80–300 EUR (Rahmenarbeit)

---

## FAQ — Häufig gestellte Fragen

### LB-001: Wie oft müssen Gasdruckfedern an Luken getauscht werden?
**Antwort:** Planmäßig alle 3–5 Jahre. Qualitätsfedern (Stabilus, Suspa) halten bis 5 Jahre, No-Name-Produkte oft nur 2–3 Jahre. Entscheidend ist die korrekte Einbaulage (Kolbenstange nach unten) und regelmäßige Pflege (Silikonspray 2×/Jahr).
**Confidence:** estimated

### LB-002: Kann ich Gasdruckfedern unterschiedlicher Hersteller mischen?
**Antwort:** Nein. Federn einer Luke immer paarweise und vom selben Hersteller/Typ tauschen. Unterschiedliche Kraftkurven führen zu ungleichmäßigem Öffnungsverhalten und einseitiger Belastung der Scharniere.
**Confidence:** measured

### LB-003: Welches Material ist für Lukenscharniere am besten?
**Antwort:** Für Salzwasser: 316L (V4A) Edelstahl oder Manganbronze. Nie 304er (V2A) Edelstahl — korrodiert in Seewasser. Bronze ist langlebiger (20–30 Jahre), aber teurer. Für Süßwasser-Boote ist V2A ausreichend.
**Confidence:** measured

### LB-004: Muss ich beim Schrauben einer Luke immer Sikaflex verwenden?
**Antwort:** Ja, bei Sandwich-Decks ist Sikaflex 291 oder 3M 5200 zwingend erforderlich, um Wassereintritt in den Kern zu verhindern. Bei Massiv-GFK ist die Abdichtung weniger kritisch, aber dennoch empfohlen. KEIN Silikon verwenden — haftet nicht auf GFK.
**Confidence:** measured

### LB-005: Wie erkenne ich, ob eine Gasdruckfeder die richtige Kraft hat?
**Antwort:** Die Luke muss bei halbem Öffnungswinkel (~45°) gerade noch selbstständig weiteröffnen. Springt sie unkontrolliert auf: Feder zu stark. Bleibt sie bei 30° stehen: Feder zu schwach. Kraft ist auf der Feder eingeprägt (z.B. „400N").
**Confidence:** estimated

### LB-006: Was ist der Unterschied zwischen Druckfeder und Zugfeder bei Luken?
**Antwort:** Gasdruckfedern (Druckfedern) werden auf Druck belastet — sie drücken die Luke auf. Zugfedern (selten bei Luken) ziehen die Luke zu. Im Yachtbau werden fast ausschließlich Druckfedern verwendet. Die Kolbenstange wird ausgefahren, wenn kein Druck aufgebracht wird.
**Confidence:** measured

### LB-007: Kann ich eine defekte Gasdruckfeder reparieren?
**Antwort:** Nein. Gasdruckfedern sind wartungsfreie Einwegartikel. Sie können nicht nachgefüllt, nachgestellt oder repariert werden. Austausch ist die einzige Option. NIE eine Gasdruckfeder anbohren oder öffnen — steht unter Druck (bis 150 bar).
**Confidence:** measured

### LB-008: Welche Schrauben verwende ich für Lukenbeschläge?
**Antwort:** Ausschließlich A4-70 oder A4-80 (316L Edelstahl). Mindestdurchmesser M5 für leichte Beschläge, M6 für schwere Luken. Nie selbstschneidende Schrauben bei GFK — immer vorbohren. Immer mit Loctite 243 (mittelfest, lösbar).
**Confidence:** measured

### LB-009: Brauche ich Backing-Plates für Lukenbeschläge?
**Antwort:** Bei Sandwich-Bauweise: JA, zwingend erforderlich. Bei Massiv-GFK >6mm: optional, aber empfohlen bei schweren Luken. Material: V4A 3–5mm oder Alu (anodisiert) 5–8mm. Fläche: mindestens 3× Beschlagfläche.
**Confidence:** measured

### LB-010: Wie verhindere ich galvanische Korrosion bei Lukenbeschlägen?
**Antwort:** Gleiche Materialien verwenden (alles 316L oder alles Bronze). Bei unvermeidlichem Materialmix: Isolierscheiben (Teflon, PEEK) zwischen die Metalle setzen. Elektrische Trennung schafft Schutz. Zusätzlich: Opferanoden in der Nähe.
**Confidence:** measured

### LB-011: Wie stelle ich die Dichtung einer Luke ein?
**Antwort:** Die Dichtung soll bei geschlossener Luke 1.5–2.5mm komprimiert sein (ca. 25–30% des Querschnitts). Zu wenig Kompression: undicht. Zu viel: Luke geht schwer zu, Dichtung altert schneller. Prüfung: Papierstreifentest — Papier soll sich mit leichtem Widerstand herausziehen lassen.
**Confidence:** estimated

### LB-012: Welches Schmiermittel verwende ich für Scharniere?
**Antwort:** Teflon-Fett (z.B. Molykote EM-30L, Weicon AL-F) oder Marine-Spezialfett (z.B. Lewmar Winch Grease). KEIN WD-40 als Dauerschmierung (nur Kriechöl, wäscht sich ab). KEIN Universalfett (bindet Schmutz). KEIN Silikonspray (für Dichtungen, nicht für Metall-auf-Metall).
**Confidence:** measured

### LB-013: Wie groß muss eine Fluchtluke mindestens sein?
**Antwort:** Nach ISO 12216: Minimum 400×520mm lichte Weite. Bei CE-Kategorie A und B ist mindestens eine Fluchtluke pro abgeschottetem Bereich vorgeschrieben. Die Luke muss sich ohne Werkzeug von beiden Seiten öffnen lassen.
**Confidence:** measured

### LB-014: Kann ich eine Lewmar-Luke mit Goiot-Beschlägen ausrüsten?
**Antwort:** Grundsätzlich nicht empfohlen. Die Beschläge sind herstellerspezifisch dimensioniert. Bohrungsmuster, Dichtungsprofile und Schließmechanismen sind nicht kompatibel. Ersatzteile immer vom Lukenhersteller beziehen. Ausnahme: Universelle Gasdruckfedern mit Kugelbolzen-Adapter.
**Confidence:** estimated

### LB-015: Wie reinige ich Lukenbeschläge richtig?
**Antwort:** 1) Süßwasser abspülen. 2) Milde Seifenlauge (keine aggressiven Reiniger). 3) Bei Kalkablagerungen: Essigessenz 10%, 15 min einwirken. 4) Edelstahl: Edelstahlpflege auftragen (z.B. Autosol Marine). 5) Dichtungen: Silikonpflegemittel. 6) NIE Scheuermittel auf Edelstahl.
**Confidence:** measured

### LB-016: Warum beschlägt meine Luke von innen?
**Antwort:** Kondensation durch Temperaturunterschied (Lukenrahmen = Kältebrücke). Lösungen: 1) Thermische Entkopplung (Kunststoff-Profil zwischen Rahmen und Deck). 2) Belüftung verbessern. 3) Luken mit Doppelverglasung (Lewmar Ocean-Serie). 4) Entfeuchter im Boot.
**Confidence:** estimated

### LB-017: Wie prüfe ich Scharniere auf Verschleiß?
**Antwort:** Luke geöffnet festhalten, vertikal und horizontal wackeln. Spiel >1mm = Scharnierstift oder Buchse verschlissen. Quietschen = mangelnde Schmierung oder Riefen. Luke schließen, Spaltmaß prüfen: ungleichmäßig = ein Scharnier stärker verschlissen.
**Confidence:** estimated

### LB-018: Sind Kunststoff-Scharniere für Luken geeignet?
**Antwort:** Nur für kleine, leichte Luken (Staufach-Deckel, Inspektionsluken <300mm). Für tragende Luken und Vorluken: NEIN. Kunststoff (PA, POM) altert unter UV, wird spröde und bricht ohne Vorwarnung. UV-stabilisiertes Delrin ist als Buchsenmaterial akzeptabel.
**Confidence:** measured

### LB-019: Wie dichte ich ein durchgebohrtes Sandwich-Deck nachträglich ab?
**Antwort:** 1) Bohrung mit Stufenbohrer auf den nächsten mm aufweiten. 2) Kernmaterial 10mm um die Bohrung mit Hakendraht entfernen. 3) Hohlraum mit angedictem Epoxid (Colloidal Silica) füllen. 4) 24h aushärten. 5) Endbohrung setzen. 6) Sikaflex in die Bohrung, Schraube setzen.
**Confidence:** measured

### LB-020: Welche Gasdruckfeder-Marken sind empfehlenswert?
**Antwort:** Premium: Stabilus (LIFT-O-MAT, BLOC-O-LIFT), Suspa, Bansbach. Gut: Hahn Gasfedern, ACE. Akzeptabel: Dictator. Vorsicht bei: No-Name aus China/Asien (Lebensdauer oft <2 Jahre). Für Marine-Einsatz auf V4A-Kolbenstange und salzwasserfeste Dichtungen achten.
**Confidence:** estimated

### LB-021: Was kostet der professionelle Austausch aller Lukenbeschläge?
**Antwort:** Abhängig von Bootsgröße und Lukenanzahl. Richtwerte (Material + Werft): Serienboot 10m (4–6 Luken): 800–2.000 EUR. Semi-Custom 15m (8–12 Luken): 2.000–5.000 EUR. Superyacht 20m (15+ Luken): 5.000–15.000 EUR. Eigenleistung spart ca. 50% der Kosten.
**Confidence:** estimated

### LB-022: Kann ich Luken-Gasdruckfedern durch elektrische Stellantriebe ersetzen?
**Antwort:** Ja, bei Superyachten zunehmend üblich (z.B. Linak, SKF). Vorteile: Exakte Positionierung, Fernbedienung, temperaturunabhängig. Nachteile: 5–10× Kosten, Stromanschluss erforderlich, bei Stromausfall manuell öffnen können (Notentriegelung vorschreiben). Nicht für CE-Kategorie-A Fluchtluken als alleiniger Antrieb zulässig.
**Confidence:** estimated

### LB-023: Wie messe ich die korrekte Gasdruckfeder-Länge?
**Antwort:** 1) Luke schließen. 2) Abstand Mitte Kugelbolzen oben → Mitte Kugelbolzen unten messen = Einbaulänge (L1). 3) Luke ganz öffnen. 4) Abstand erneut messen = Einbaulänge + Hub. 5) Hub = L2 - L1. 6) Kugelbolzen-Durchmesser notieren (10mm, 13mm Standard). Feder mit ±5mm Toleranz bei Einbaulänge bestellen.
**Confidence:** measured

### LB-024: Was tun bei abgerissenem Kugelbolzen?
**Antwort:** 1) Abgerissenen Bolzenrest mit Ausdreher (Linksausdreher) entfernen. 2) Gewinde prüfen (M6, M8 Standard). 3) Bei beschädigtem Gewinde: Helicoil-Gewindeeinsatz setzen. 4) Neuen Kugelbolzen mit Loctite 243 einschrauben. 5) Kugelfläche mit PTFE-Spray behandeln. Kugelbolzen immer paarweise tauschen.
**Confidence:** measured

### LB-025: Wie lagere ich Gasdruckfedern korrekt (Winterlager)?
**Antwort:** 1) Luke in geöffneter Position belassen (Feder entlastet). 2) Kolbenstange mit Silikonspray einsprühen. 3) Schutzkappe auf Kolbenstange (UV-Schutz). 4) Temperatur idealerweise >0°C (Frostlager: Kraft sinkt auf 70%, aber kein Defekt). 5) Nie Federn in komprimiertem Zustand über Monate lagern.
**Confidence:** estimated

---

## Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Gasdruckfeder** | Pneumatisches Federelement mit Stickstoff-Füllung, unterstützt das Öffnen und Halten von Luken |
| **Kolbenstange** | Die ausfahrende Stange der Gasdruckfeder, trägt die Dichtung |
| **Kugelbolzen** | Kugelfömiger Befestigungsbolzen, auf den die Gasdruckfeder aufgeschnappt wird |
| **Kugelkopf** | Das Ende der Gasdruckfeder mit Kugelaufnahme (Snap-on) |
| **Hub** | Der nutzbare Federweg der Gasdruckfeder in mm |
| **Einbaulänge** | Gesamtlänge der Gasdruckfeder in komprimiertem Zustand (L1) |
| **Ausschublänge** | Gesamtlänge der Gasdruckfeder in ausgefahrenem Zustand (L2 = L1 + Hub) |
| **Endlagendämpfung** | Mechanismus, der das letzte Wegstück der Feder abbremst (Weichauslauf) |
| **Anlenkpunkt** | Der Befestigungspunkt der Feder am Lukendeckel oder Rahmen |
| **Drehachse** | Die Achse, um die der Lukendeckel schwenkt (= Scharnierachse) |
| **Scharnierstift** | Der Bolzen, der die Scharnierhälften verbindet und als Drehachse dient |
| **Scharnierband** | Die beiden Metallplatten des Scharniers (Flügel) |
| **Augen-Scharnier** | Scharnier mit Ösen-Enden (für Bolzenbefestigung), auch Augenscharnier |
| **Piano-Scharnier** | Durchgehendes Scharnier über die volle Lukenbreite (Stangenscharnier) |
| **Nocken (Cam)** | Exzentrische Kurve im Riegelverschluss, erzeugt Schließkraft |
| **Gegenplatte (Striker)** | Gegenstück zum Riegel, in das der Nocken eingreift |
| **Cam-Lock** | Riegelverschluss mit Nockenmechanismus, Standard bei Lewmar/Goiot |
| **Toggle-Latch** | Hebel-Kniegelenk-Verschluss, erzeugt hohe Schließkraft |
| **Dog-Verschluss** | Drehriegel (T-Griff), typisch für Schiffstüren und schwere Luken |
| **Flush-Lock** | Bündig eingelassener Verschluss, kein hervorstehender Griff |
| **Süllrand** | Der erhöhte Rand der Lukenöffnung, auf dem der Deckel aufliegt |
| **Süllhöhe** | Höhe des Süllrands über Deck, kritisch für Wasserdichtigkeit |
| **Backing-Plate** | Verstärkungsplatte unter dem Deck, verteilt die Beschlaglast |
| **Sandwich-Bauweise** | Deckkonstruktion: GFK-Außenhaut + Kern (Balsa/Schaum) + GFK-Innenhaut |
| **Kernmaterial** | Das Material zwischen den GFK-Häuten (Balsa, PVC-Schaum, SAN-Schaum) |
| **Delamination** | Ablösung der GFK-Haut vom Kern, oft durch Wassereintritt |
| **EPDM** | Ethylen-Propylen-Dien-Kautschuk — Standard-Dichtungsmaterial für Luken |
| **Neopren** | Chloropren-Kautschuk — Dichtungsmaterial, weniger UV-beständig als EPDM |
| **Druckverformungsrest** | Bleibende Verformung einer Dichtung nach Langzeitbelastung (in %) |
| **Loctite 243** | Mittelfeste Schraubensicherung, lösbar mit Handwerkzeug |
| **Sikaflex 291** | Marine-Dichtstoff (Polyurethan), Standard für Decksdurchbrüche |
| **3M 5200** | Permanenter Marine-Kleb-/Dichtstoff, schwer zu lösen (für permanente Verbindungen) |
| **Spaltkorrosion** | Korrosionsform in engen Spalten (Scharnier, unter Schraubenköpfen) |
| **Galvanische Korrosion** | Korrosion durch Kontakt unterschiedlicher Metalle in Elektrolyt (Seewasser) |
| **A4-70 / A4-80** | Bezeichnung für austenitischen Edelstahl (316L) mit Festigkeit 700/800 MPa |
| **V2A / V4A** | Deutsche Handelsbezeichnung für 304 (V2A) bzw. 316L (V4A) Edelstahl |
| **Opferanode** | Elektrochemischer Schutz: unedles Metall (Zink) korrodiert statt der geschützten Teile |
| **Helicoil** | Gewindeeinsatz zum Reparieren beschädigter Gewinde in weichem Material |
| **PTFE** | Polytetrafluorethylen (Teflon) — Schmierstoff und Isoliermaterial |
| **Nordlock-Scheibe** | Keilsicherungsscheibe, verhindert Vibrationslösung zuverlässiger als Federringe |
| **ISO 12216** | Internationale Norm für Fenster, Bullaugen, Luken und Deckel auf Sportbooten |
| **CE-Kategorie** | Konstruktionskategorie A–D nach EU-Richtlinie 2013/53/EU |

---

## Schnell-Referenz

### Drehmomente für Lukenbeschläge

| Schraube | Drehmoment (A4-70) | Drehmoment (A4-80) |
|----------|--------------------|--------------------|
| M4 | 2.5–3.5 Nm | 3.0–4.0 Nm |
| M5 | 5.0–7.0 Nm | 6.0–8.0 Nm |
| M6 | 8.0–10.0 Nm | 10.0–12.0 Nm |
| M8 | 15.0–20.0 Nm | 20.0–25.0 Nm |
| M10 | 30.0–40.0 Nm | 40.0–50.0 Nm |

### Gasdruckfeder-Schnellauswahl

| Lukengewicht [kg] | 2 Federn à [N] | Hub [mm] | Einbaulänge [mm] |
|-------------------|----------------|----------|-------------------|
| 5 | 100 | 160 | 400 |
| 10 | 200 | 200 | 500 |
| 15 | 300 | 220 | 550 |
| 20 | 400 | 250 | 625 |
| 30 | 600 | 280 | 700 |
| 40 | 800 | 320 | 800 |
| 50 | 1000 | 350 | 875 |

### Dichtungsprofil-Schnellauswahl

| Süllhöhe [mm] | Profilquerschnitt [mm] | Material | Kompression |
|----------------|----------------------|----------|-------------|
| 15–20 | 8×12 | EPDM | 2.0 mm |
| 20–30 | 10×15 | EPDM | 2.5 mm |
| 30–40 | 12×18 | EPDM | 3.0 mm |
| >40 | 15×20 | EPDM | 3.5 mm |

### Bewertungs-Kurzreferenz (AYDI Scoring)

| Zustand | Score-Abzug | Confidence |
|---------|------------|------------|
| Gasdruckfeder defekt | -35 | visual_high |
| Scharnier korrodiert | -20 | visual_medium |
| Riegel gebrochen | -40 | visual_high |
| Schloss festsitzend | -10 | visual_medium |
| Schrauben lose | -20 | visual_high |
| Montageplatte gerissen | -30 | visual_medium |
| Dichtung degradiert | -15 | visual_high |
| Falsche Federkraft | -15 | visual_medium |
| Safety Catch fehlt | -20 | visual_high |
| Nocken verschlissen | -15 | visual_medium |
| Unterfütterung delaminiert | -40 | visual_medium |
| Vibrationsermüdung | -30 | visual_high |

---

## Notfall-Ressourcen

### Notfall: Luke lässt sich nicht öffnen (eingeschlossen)

1. **Ruhe bewahren** — Panik erhöht Sauerstoffverbrauch
2. Alle Riegel/Verschlüsse systematisch prüfen — oft ist ein Riegel übersehen
3. Notentriegelung suchen (roter Hebel oder Markierung)
4. Bei festsitzendem Scharnier: Kräftig rütteln, dann gleichmäßig drücken
5. Bei Gasdruckfeder-Blockade: Feder manuell zusammendrücken und Luke anheben
6. Im Notfall: Lukendeckel von innen mit Schulter/Fuß aufdrücken (Acryl hält ca. 500N)
7. Alternative Ausgänge prüfen: andere Luken, Niedergang, Fenster >400×520mm

### Notfall: Luke lässt sich nicht schließen (auf See)

1. **Sofort Kurs ändern** — Welle nicht über die offene Luke nehmen
2. Luke manuell runterdrücken und mit Leine/Spanngurt sichern
3. Provisorische Abdichtung: Segeltuch/Plane über Luke, mit Klebeband fixieren
4. Wassereinbruch: Lenzpumpe aktivieren, Bilge überwachen
5. Nächsten Hafen anlaufen, nicht weitersegeln mit defekter Luke

### Notfall-Kontakte und Ersatzteile unterwegs

| Situation | Aktion |
|-----------|--------|
| Gasdruckfeder defekt | Yachtzubehör-Händler (SVB, Compass, AWN) — Universalfedern M8/M10 vorrätig |
| Scharnier gebrochen | Marina-Werkstatt, alternativ Schlosser an Land |
| Riegel defekt | Provisorisch: Schraube durch Riegel und Rahmen als Bolzen |
| Dichtung gerissen | Provisorisch: Butylband (Decksversiegelung) als Notdichtung |
| Kugelbolzen abgerissen | Provisorisch: Kabelbinder durch Federöse und Schraubauge |

---

## ANHANG A: Hersteller-Referenz Gasdruckfedern (Marine)

| Hersteller | Serie | Kolbenstange | Kraft-Bereich [N] | Marine-Eignung | Preis/Stück [EUR] |
|------------|-------|-------------|-------------------|----------------|-------------------|
| Stabilus | LIFT-O-MAT | V4A | 50–2500 | Sehr gut | 35–120 |
| Stabilus | BLOC-O-LIFT | V4A | 100–5000 | Sehr gut (arretierbar) | 60–200 |
| Suspa | Liftline | V4A | 50–1500 | Gut | 30–90 |
| Bansbach | Marine-Serie | V4A | 100–2000 | Sehr gut | 40–130 |
| Hahn | Gasfedern Marine | V4A | 50–1000 | Gut | 25–70 |
| ACE | GZ-Serie | V4A | 100–2500 | Gut | 30–100 |
| Dictator | Gasfeder | Stahl, vernickelt | 50–1500 | Eingeschränkt | 15–50 |

## ANHANG B: Hersteller-Referenz Lukenscharniere (Marine)

| Hersteller | Typ | Material | Max. Gewicht [kg] | Preis/Stück [EUR] |
|------------|-----|----------|-------------------|-------------------|
| Lewmar | Standard-Luke | 316L | 30 | 15–40 |
| Lewmar | Ocean-Serie | 316L geschmiedet | 50 | 30–80 |
| Goiot | Cristal-Serie | 316L | 25 | 12–35 |
| Goiot | Opal-Serie | 316L | 40 | 25–60 |
| Rutgerson | Deckscharnier | 316L | 45 | 20–55 |
| Vetus | MPHSO-Serie | 316L | 35 | 18–45 |
| Maritim | Custom | Bronze | 60 | 40–120 |
| Wichard | Forkscharnier | 316L geschmiedet | 50 | 35–90 |

## ANHANG C: Hersteller-Referenz Verschlüsse (Marine)

| Hersteller | Typ | Material | Schließkraft [N] | Preis/Stück [EUR] |
|------------|-----|----------|-------------------|-------------------|
| Southco | M1-Serie | 316L | 200–1000 | 25–80 |
| Lewmar | Cam-Lock | 316L | 300–800 | 20–60 |
| Perko | Flush-Lock | Bronze | 200–600 | 30–90 |
| Goiot | Riegel | 316L | 250–700 | 15–50 |
| Bomar | Toggle-Latch | 316L | 500–1500 | 35–100 |
| Hella Marine | Flush-Lock | PA + 316L | 150–400 | 20–55 |
| Vetus | MQDCC | 316L | 300–900 | 25–70 |

## ANHANG D: Dichtungsprofile (Marine-Standard)

| Profil | Querschnitt [mm] | Material | Shore-Härte | Anwendung | Preis/m [EUR] |
|--------|------------------|----------|-------------|-----------|---------------|
| D-Profil | 8×12 | EPDM | 60A | Vorluken, kleine Luken | 3–6 |
| P-Profil | 10×15 | EPDM | 55A | Standard-Decksluken | 4–8 |
| E-Profil | 12×18 | EPDM | 50A | Große Luken, Motorraumluken | 5–10 |
| Hohlkammer | 15×20 | EPDM | 45A | Superyacht-Luken | 8–15 |
| Flachprofil | 3×15 | Neopren | 60A | Inspektionsluken | 2–4 |
| Omega-Profil | 10×12 | Silikon | 50A | Hochtemperatur (Maschinenraum) | 10–20 |

## ANHANG E: Fallstudien

### Fallstudie 1: Bavaria 40 Cruiser — Vorluke klappt unkontrolliert zu

**Boot:** Bavaria 40 Cruiser, Baujahr 2016, Charterboot
**Problem:** Vorluke (Lewmar Size 60) fällt nach 4 Jahren Charternutzung unkontrolliert zu. Zwei Gäste leicht verletzt.
**Diagnose:** Gasdruckfedern (No-Name, China) nach ca. 15.000 Zyklen vollständig kraftlos. Kolbenstange nach oben montiert (Werftfehler). Kein Sicherheitsfangband vorhanden.
**Maßnahme:** 2× Stabilus LIFT-O-MAT 400N, Hub 200mm, V4A. Einbau Kolbenstange nach unten. Fangband aus V4A-Kette nachgerüstet.
**Kosten:** Material 95 EUR, Einbau (Eigenleistung) 45 min.
**Ergebnis:** Seit 2 Jahren problemloser Betrieb. Kontrolle halbjährlich.
**AYDI-Score vorher:** 42/100 | **AYDI-Score nachher:** 91/100
**Confidence:** documented

### Fallstudie 2: Hallberg-Rassy 43 — Scharnier-Korrosion durch Materialmix

**Boot:** Hallberg-Rassy 43, Baujahr 2010, Privatboot, Mittelmeer
**Problem:** Motorraumluke-Scharniere nach 8 Jahren festgefressen. Motorraumzugang nur noch durch Anheben mit zwei Personen möglich.
**Diagnose:** Original-Scharniere aus 316L, aber Backing-Plates aus unbehandeltem Aluminium. Galvanische Korrosion hat Alu-Plates zerfressen, Korrosionsprodukte haben Scharnierstifte blockiert.
**Maßnahme:** Backing-Plates durch anodisiertes Alu 5083-H321 (6mm) ersetzt. Scharnierstifte erneuert. Teflon-Isolierscheiben zwischen Scharnier und Backing-Plate eingefügt.
**Kosten:** Material 180 EUR, Werft 420 EUR (Innenverkleidung Demontage erforderlich).
**Ergebnis:** Scharniere laufen leicht, kein Korrosionszeichen nach 3 Jahren.
**AYDI-Score vorher:** 55/100 | **AYDI-Score nachher:** 94/100
**Confidence:** documented

### Fallstudie 3: Beneteau Oceanis 51.1 — Sandwich-Delamination unter Lukenbeschlag

**Boot:** Beneteau Oceanis 51.1, Baujahr 2018, Blauwasser-Yacht
**Problem:** Decksluke im Salon zeigt „Pumpen" — Rahmen hebt sich bei Belastung sichtbar. Wasserflecken an Decksunterseite.
**Diagnose:** Balsa-Kern unter Lukenbeschlag durch eingedrungenes Wasser aufgequollen und teilweise verfault. Ursache: Schraubenlöcher bei Erstmontage nicht abgedichtet.
**Maßnahme:** Luke demontiert, faulen Kern auf 200×300mm freigelegt und entfernt. Mit Epoxid/Colloidal Silica verfüllt. Neue Backing-Plate (V4A 5mm, 250×350mm). Alle Schrauben mit Sikaflex 291 abgedichtet.
**Kosten:** Material 120 EUR, Werft 850 EUR (aufwendige Kernreparatur).
**Ergebnis:** Deck wieder fest, keine Feuchtigkeit nach 2 Saisons.
**AYDI-Score vorher:** 38/100 | **AYDI-Score nachher:** 88/100
**Confidence:** documented

### Fallstudie 4: Jeanneau Sun Odyssey 440 — Mehrfaches Riegelversagen

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2019, Mittelmeer-Charter
**Problem:** 3 von 4 Riegeln der Hauptdecksluke brechen innerhalb eines Jahres. Luke undicht bei Regen.
**Diagnose:** Riegel aus Zink-Druckguss (Originalteil), galvanisch verchromt. Salzwasser hat Zink unter der Chromschicht angegriffen — Spannungsrisskorrosion.
**Maßnahme:** Alle Riegel durch 316L-Cam-Locks (Southco M1-46) ersetzt. Neue Dichtung (EPDM P-Profil). Gegenplatten aus V4A nachgefertigt.
**Kosten:** Material 220 EUR (4 Riegel + Dichtung), Einbau (Eigenleistung) 90 min.
**Ergebnis:** Kein weiteres Riegelversagen nach 3 Jahren intensiver Nutzung.
**AYDI-Score vorher:** 35/100 | **AYDI-Score nachher:** 93/100
**Confidence:** documented

### Fallstudie 5: Oyster 575 — Elektrische Lukenöffnung nachrüsten

**Boot:** Oyster 575, Baujahr 2014, Blauwasser mit Eignerpaar (65+)
**Problem:** Eigner können schwere Motorraum- und Lazarette-Luken (je 30+ kg) nicht mehr ohne Hilfe öffnen.
**Maßnahme:** 4 Luken mit Linak LA36 Linearantrieben (24V, 1000N, IP66) nachgerüstet. Steuerung über Panel im Cockpit + Not-Handkurbel. Gasdruckfedern als Notfall-Backup belassen.
**Kosten:** Material 2.400 EUR, Werft 1.800 EUR (Elektrik, Montage, Programmierung).
**Ergebnis:** Volle Autonomie des Eignerpaares wiederhergestellt. Batteriebelastung minimal.
**AYDI-Score vorher:** 60/100 | **AYDI-Score nachher:** 95/100
**Confidence:** documented

### Fallstudie 6: Catana 53 — Vibrationsermüdung an Motorraum-Luken

**Boot:** Catana 53, Baujahr 2012, Katamaran, Atlantiküberquerung
**Problem:** Backbord-Motorraumluke hat sich bei Seegang gelöst — 3 von 6 Schrauben abgerissen, Luke nur noch an Scharnieren.
**Diagnose:** Ermüdungsbruch durch Motorvibrationen (Yanmar 4JH). Schrauben A4-70 ohne Schraubensicherung, keine Federringe. Vibrationsbelastung über 8.000 Motorstunden.
**Maßnahme:** Alle Schrauben durch A4-80 mit Nordlock-Scheiben ersetzt. Loctite 243 auf alle Gewinde. Zusätzlicher Riegel auf der Vibrationsseite montiert. Schwingungsdämpfer unter Motorlager geprüft und erneuert.
**Kosten:** Material 85 EUR, Werft 350 EUR (inkl. Motorlager-Check).
**Ergebnis:** Keine weiteren Schraubenbrüche nach 3.000 Motorstunden.
**AYDI-Score vorher:** 30/100 | **AYDI-Score nachher:** 92/100
**Confidence:** documented

### Fallstudie 7: Contest 50CS — Premium-Lukenbeschläge, trotzdem Probleme

**Boot:** Contest 50CS, Baujahr 2008, Nordeuropa
**Problem:** Lewmar Ocean-Luken (Premium-Segment) zeigen nach 12 Jahren deutlichen Dichtungsverschleiß und Kondensation.
**Diagnose:** EPDM-Dichtungen trotz Premium-Qualität nach 12 Jahren am Druckverformungsrest-Limit (>40%). Kein UV-Schutz beim Winterlager verwendet. Scharniere einwandfrei (Bronze).
**Maßnahme:** Kompletter Dichtungssatz erneuert (Lewmar Original-Profil). UV-Schutzabdeckungen (Canvas) für Winterlager angefertigt. Scharniere geschmiert.
**Kosten:** Material 280 EUR (6 Luken komplett), Einbau (Eigenleistung) 3h.
**Ergebnis:** Luken wieder vollständig dicht, Kondensation deutlich reduziert.
**AYDI-Score vorher:** 72/100 | **AYDI-Score nachher:** 96/100
**Confidence:** documented

### Fallstudie 8: Sunseeker Manhattan 52 — Hydraulische Lukensysteme

**Boot:** Sunseeker Manhattan 52, Baujahr 2015, Motoryacht, Mittelmeer
**Problem:** Hydraulisches Luken-Öffnungssystem (Gar-Hatch) zeigt Leckage — Luke öffnet nicht mehr vollständig, Hydrauliköl auf Deck.
**Diagnose:** O-Ring im Hydraulikzylinder gealtert (nach 7 Jahren). Hydraulikflüssigkeit nicht gemäß Wartungsplan gewechselt (alle 2 Jahre vorgeschrieben).
**Maßnahme:** Hydraulikzylinder-Dichtungssatz erneuert, Hydraulikflüssigkeit gewechselt (Total Equivis ZS 32), Leitungen auf Lecks geprüft. Wartungsintervall-Aufkleber angebracht.
**Kosten:** Material 350 EUR, Werft 600 EUR (Spezialwerkzeug für Hydraulik erforderlich).
**Ergebnis:** System funktioniert wieder einwandfrei. Wartungsplan eingehalten.
**AYDI-Score vorher:** 48/100 | **AYDI-Score nachher:** 94/100
**Confidence:** documented

## ANHANG F: Normen-Referenz

| Norm | Titel | Relevanz für Lukenbeschläge |
|------|-------|---------------------------|
| ISO 12216:2020 | Fenster, Bullaugen, Luken, Deckel und Türen | Primärnorm für Luken-Hardware |
| ISO 12215-5:2019 | Rumpfbau — Bemessung | Strukturelle Anforderungen an Luken-Ausschnitte |
| ISO 15085:2003 | Vorrichtungen zur Verhütung von Mann-über-Bord | Sicherheitsanforderungen an Decksöffnungen |
| ISO 12217:2022 | Stabilitäts- und Auftriebsbeurteilung | Einfluss von Lukenöffnungen auf Stabilität |
| ISO 9094:2015 | Brandschutz | Fluchtluken und Notausgänge |
| ISO 11812:2020 | Cockpits (wasserdicht, schnell lenzend) | Cockpitluken und -verschlüsse |
| EN 1670:2007 | Korrosionsbeständigkeit von Baubeschlägen | Salzsprühtest-Anforderungen |
| DIN 267-26 | Mechanische Verbindungselemente | Schwingfestigkeit von Schrauben |

## ANHANG G: Werkzeug-Checkliste Lukenbeschlag-Wartung

| Werkzeug | Verwendung | Preis [EUR] |
|----------|-----------|-------------|
| Drehmomentschlüssel 2–25 Nm | Schraubenmontage | 40–80 |
| Gabelschlüssel-Satz 8–17mm | Muttern, Bolzen | 15–30 |
| Sicherungsring-Zange (Seeger) | Gasdruckfeder-Clips | 10–20 |
| Edelstahl-Bohrer-Set HSS-Co | Bohren in GFK/Edelstahl | 20–40 |
| Gewindeschneider M5–M8 | Gewinde schneiden/nachschneiden | 15–30 |
| Ausdreher-Set (Linksausdreher) | Abgerissene Schrauben entfernen | 12–25 |
| Helicoil-Set M5, M6 | Gewindereparatur | 25–45 |
| Körner | Bohrpositionen markieren | 5–10 |
| Haarlineal 300mm | Ebenheitsprüfung Süllrand | 15–30 |
| Fühlerlehre 0.05–1.0mm | Spaltmaß-Messung | 8–15 |

## ANHANG H: Schmiermittel-Referenz

| Produkt | Typ | Anwendung | Preis [EUR] |
|---------|-----|-----------|-------------|
| Molykote EM-30L | Teflon-Fett | Scharniere, Stifte | 15–25 (100g) |
| Weicon AL-F | Alu/PTFE-Fett | Scharniere, Verschlüsse | 12–20 (100g) |
| Lewmar Winch Grease | Marine-Fett | Winsch, Scharniere | 18–28 (100g) |
| Ballistol Marine | Universalöl | Reinigung, leichte Schmierung | 8–12 (200ml) |
| Caramba Marinespray | Kriechöl | Lösen festsitzender Teile | 6–10 (300ml) |
| Silikonspray (Würth) | Silikonöl | Dichtungspflege, Kolbenstangen | 5–8 (300ml) |
| PTFE-Spray (WD-40 Specialist) | Trockenschmierung | Nocken, Schlösser | 8–12 (250ml) |
| Grafitspray | Feststoffschmierung | Schließzylinder | 5–8 (200ml) |

## ANHANG I: Ersatzteil-Bestellhilfe

**Benötigte Angaben für korrekte Ersatzteilbestellung:**
1. Lukenhersteller und Modell (z.B. Lewmar Size 60, Goiot Cristal 37)
2. Baujahr der Luke (Modelle ändern sich alle 3–5 Jahre)
3. Gasdruckfeder: Kraft [N], Hub [mm], Einbaulänge [mm], Kugelbolzen-Ø [mm]
4. Dichtung: Profilquerschnitt [mm], Gesamtlänge [mm], Material (EPDM/Neopren)
5. Scharnier: Blattlänge [mm], Blattbreite [mm], Stift-Ø [mm], Bohrungsabstand [mm]
6. Riegel: Typ (Cam/Toggle/Dog), Bohrungsabstand [mm], Schließkraft [N]

**Bezugsquellen (DE/EU):**
| Händler | Spezialisierung | Webseite |
|---------|----------------|---------|
| SVB | Yachtzubehör, breites Sortiment | svb-marine.de |
| Compass24 | Yachtzubehör, Ersatzteile | compass24.de |
| AWN | Segelbedarf, Beschläge | awn.de |
| Toplicht | Premium-Yachtzubehör | toplicht.de |
| Lewmar (direkt) | Lewmar-Ersatzteile | lewmar.com |
| Goiot (direkt) | Goiot-Ersatzteile | goiot.com |
| Stabilus (direkt) | Gasdruckfedern | stabilus.com |

## ANHANG J: Saisonale Wartungscheckliste

### Frühjahr (Auswassern / Saisonstart)

- [ ] Alle Luken öffnen und schließen — Funktion prüfen
- [ ] Gasdruckfedern: Haltekraft testen (Luke muss bei 90° selbstständig stehen)
- [ ] Dichtungen: Auf Risse, Verformung, Verhärtung prüfen
- [ ] Scharniere: Leichtgängigkeit prüfen, bei Bedarf schmieren
- [ ] Riegel: Schließfunktion und Nockenabrieb prüfen
- [ ] Schrauben: Drehmoment stichprobenartig prüfen (min. 30%)
- [ ] Süllrand: Auf Risse, Delamination, Verfärbungen prüfen

### Herbst (Einwintern)

- [ ] Alle Luken gründlich mit Süßwasser reinigen
- [ ] Gasdruckfeder-Kolbenstangen mit Silikonspray einsprühen
- [ ] Dichtungen mit Silikonpflegemittel behandeln
- [ ] Scharniere schmieren (Teflon-Fett)
- [ ] Luken leicht geöffnet lassen (Belüftung, Federentlastung)
- [ ] UV-Schutzabdeckungen anbringen (wenn vorhanden)
- [ ] Schlösser mit Grafitspray behandeln

## ANHANG K: Temperaturkompensations-Tabelle (Gasdruckfedern)

| Nennkraft bei 20°C [N] | -20°C [N] | -10°C [N] | 0°C [N] | 10°C [N] | 30°C [N] | 40°C [N] | 50°C [N] | 60°C [N] |
|------------------------|-----------|-----------|---------|----------|----------|----------|----------|----------|
| 100 | 70 | 77 | 85 | 92 | 103 | 110 | 115 | 120 |
| 200 | 140 | 155 | 170 | 185 | 207 | 220 | 230 | 240 |
| 300 | 210 | 232 | 255 | 277 | 310 | 330 | 345 | 360 |
| 400 | 280 | 310 | 340 | 370 | 413 | 440 | 460 | 480 |
| 500 | 350 | 387 | 425 | 462 | 517 | 550 | 575 | 600 |
| 600 | 420 | 465 | 510 | 555 | 620 | 660 | 690 | 720 |
| 800 | 560 | 620 | 680 | 740 | 827 | 880 | 920 | 960 |
| 1000 | 700 | 775 | 850 | 925 | 1033 | 1100 | 1150 | 1200 |

## ANHANG L: Luken-Gewichtsschätzung nach Größe und Material

| Lukengröße [mm] | Acryl 10mm [kg] | Acryl 15mm [kg] | Polycarbonat 10mm [kg] | Alu + Glas [kg] |
|-----------------|----------------|-----------------|----------------------|-----------------|
| 300×300 | 1.5 | 2.2 | 1.6 | 4.0 |
| 400×400 | 2.5 | 3.8 | 2.7 | 6.5 |
| 500×500 | 4.0 | 6.0 | 4.3 | 10.0 |
| 600×600 | 5.8 | 8.7 | 6.2 | 14.5 |
| 700×500 | 5.6 | 8.4 | 6.0 | 14.0 |
| 800×600 | 7.7 | 11.5 | 8.2 | 19.0 |
| 900×700 | 10.0 | 15.0 | 10.7 | 25.0 |
| 1000×800 | 12.8 | 19.2 | 13.7 | 32.0 |

(Gewichte inkl. Rahmen, Dichtung und Beschläge als Schätzwert)

## ANHANG M: AYDI-Bewertungsmatrix Lukenbeschläge

```python
LUKENBESCHLAG_SCORING = {
    "zustand_gasdruckfeder": {
        "einwandfrei": 0,
        "leicht_nachlassend": -10,
        "deutlich_nachlassend": -25,
        "defekt_faellt_zu": -35,
        "fehlend": -40,
    },
    "zustand_scharniere": {
        "einwandfrei": 0,
        "leicht_schwergaengig": -5,
        "deutlich_schwergaengig": -15,
        "festsitzend": -20,
        "korrodiert_strukturell": -30,
        "gebrochen": -45,
    },
    "zustand_riegel": {
        "einwandfrei": 0,
        "leichtes_spiel": -5,
        "deutliches_spiel": -15,
        "schliesst_nicht_satt": -25,
        "gebrochen": -40,
        "fehlend": -45,
    },
    "zustand_dichtung": {
        "einwandfrei": 0,
        "leicht_verhaertet": -5,
        "rissig": -15,
        "stark_deformiert": -20,
        "undicht": -30,
        "fehlend": -35,
    },
    "zustand_befestigung": {
        "einwandfrei": 0,
        "einzelne_schraube_lose": -10,
        "mehrere_schrauben_lose": -20,
        "backing_plate_beschaedigt": -30,
        "delamination_unter_beschlag": -40,
    },
    "sicherheit": {
        "safety_catch_vorhanden": 0,
        "safety_catch_fehlend": -20,
        "notentriegelung_vorhanden": 0,
        "notentriegelung_fehlend": -15,
    },
}
```

## ANHANG N: Kompatibilitätsmatrix Luken ↔ Beschläge

| Lukenhersteller | Gasdruckfeder-Bolzen | Dichtungsprofil | Riegel-Typ | Scharnier-Typ |
|-----------------|---------------------|-----------------|------------|---------------|
| Lewmar (Low Profile) | M8 Kugelbolzen | Lewmar LP-Profil | Cam-Lock integral | Integral (Kunststoff) |
| Lewmar (Ocean) | M10 Kugelbolzen | Lewmar Ocean-Profil | Cam-Lock 316L | Integral (316L) |
| Goiot (Cristal) | M8 Kugelbolzen | Goiot Standard-Profil | Hebelriegel | Integral (316L) |
| Goiot (Opal) | M10 Kugelbolzen | Goiot HD-Profil | Cam-Lock | Integral (316L) |
| Bomar (Voyager) | M8 Kugelbolzen | EPDM Universal | Toggle-Latch | Extern (316L) |
| Freeman | M10 Kugelbolzen | EPDM D-Profil | Dog-Verschluss | Extern (316L/Bronze) |
| Moonlight | M8/M10 | Moonlight-Profil | Cam-Lock | Integral (Alu/316L) |
| Custom/Eigenanfertigung | variabel | nach Zeichnung | nach Zeichnung | nach Zeichnung |

## ANHANG O: Checkliste für visuelle Analyse (AYDI Pipeline B)

```python
VISUAL_ANALYSIS_CHECKLIST_LUKENBESCHLAEGE = {
    "gasdruckfeder": [
        "Kolbenstange sichtbar? (Ölspuren, Korrosion, Kratzer)",
        "Einbaulage korrekt? (Kolbenstange unten)",
        "Kugelbolzen intakt? (Korrosion, Spiel)",
        "Feder hält Luke bei 90°?",
    ],
    "scharniere": [
        "Korrosion sichtbar? (Braunfärbung, Lochfraß)",
        "Spiel erkennbar? (Luke wackelt in Scharnieren)",
        "Schmierung vorhanden? (Fett sichtbar, kein Quietschen)",
        "Befestigungsschrauben vollständig?",
    ],
    "riegel": [
        "Alle Riegel vorhanden und funktional?",
        "Nocken-Abrieb sichtbar? (Glänzende Flächen)",
        "Hebel intakt? (Kein Bruch, kein übermäßiges Spiel)",
        "Schließt satt? (Kein Klappern bei geschlossener Luke)",
    ],
    "dichtung": [
        "Risse oder Krokodilhaut-Muster?",
        "Druckverformungsrest? (Flachgedrückt >50%)",
        "Vollständig umlaufend? (Keine Fehlstellen)",
        "Eckverbindungen dicht?",
    ],
    "befestigung": [
        "Schraubenköpfe bündig? (Keine hervorstehenden Schrauben)",
        "Gelcoat-Risse um Befestigung? (Hinweis auf Backing-Problem)",
        "Pumpen bei Belastung? (Delamination)",
        "Wasserflecken unter der Luke? (Undichtigkeit Befestigung)",
    ],
}
```

## ANHANG P: Temperaturzonen und Feder-Empfehlungen

| Revier | Sommer-Deckstemp. [°C] | Winter-Deckstemp. [°C] | Feder-Auslegung bei [°C] | Empfehlung |
|--------|------------------------|------------------------|--------------------------|------------|
| Ostsee | +35 | -15 | +10 | Standard-Feder, leicht überdimensioniert |
| Nordsee | +30 | -5 | +12 | Standard-Feder |
| Mittelmeer | +50 | +5 | +25 | Auf Sommertemperatur auslegen |
| Karibik | +55 | +20 | +35 | Temperaturkompensierte Feder empfohlen |
| Südostasien | +60 | +25 | +40 | Temperaturkompensierte Feder zwingend |
| Nordpazifik | +25 | -10 | +8 | Standard-Feder, überdimensioniert |
| Südpazifik | +45 | +15 | +28 | Auf Sommertemperatur auslegen |

## ANHANG Q: Kostenvergleich Wartung vs. Vernachlässigung (20 Jahre)

| Szenario | Jährliche Wartung [EUR] | 20-Jahres-Kosten [EUR] | Typische Folgeschäden |
|----------|------------------------|----------------------|----------------------|
| Vorbildliche Wartung | 150–300 | 3.000–6.000 | Keine |
| Durchschnittliche Wartung | 50–100 | 5.000–12.000 | Gelegentliche Reparaturen, Dichtungstausch |
| Minimale Wartung | 0–20 | 8.000–20.000 | Delamination, Korrosionsschäden, Lukenersatz |
| Keine Wartung | 0 | 15.000–40.000 | Kompletter Lukentausch, Deckssanierung, Strukturschäden |

(Werte für Segelyacht 12m, 6 Luken, Mittelmeerrevier)

## ANHANG R: Änderungshistorie dieses Dokuments

| Version | Datum | Änderung |
|---------|-------|----------|
| 1.0 | 2025-01-15 | Erstversion: Grundlagen, Typen, Materialien |
| 2.0 | 2025-03-10 | Erweitert: Kostenrahmen, Bootsklassen-Kalibrierung |
| 3.0 | 2025-06-20 | Erweitert: Technische Referenz, Berechnungen, Fehlerbild-Atlas |
| 3.1 | 2025-06-20 | Erweitert: Einbau-Anleitungen, FAQ, Glossar, Anhänge A–R |

(Confidence: estimated — Aggregiert aus Herstellerangaben, Werft-Erfahrung und Fachliteratur)
