# 08.01 — Decksluken im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 08.01** — Kategorie 8: Decksöffnungen, Luken und Fenster
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Werftunterlagen), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien](#2-zukunftstechnologien)
3. [Best Practices nach Revier](#3-best-practices-nach-revier)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle (DeckHatchSpec, DeckHatchCondition, HatchSystemAssessment)](#6-pydantic-modelle)
7. [Grundlagen](#7-grundlagen)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Definition und Funktion

Decksluken (engl. deck hatches) sind verschließbare Öffnungen im Bootsdeck, die drei wesentliche Funktionen erfüllen:

1. **Belüftung** — Natürlicher Luftaustausch unter Deck, entscheidend für Feuchtigkeitskontrolle, Schimmelprävention und Bewohnbarkeit
2. **Tageslicht** — Transparente oder transluzente Lukendeckel lassen natürliches Licht in Kabinen, Salon und Vorschiff
3. **Notausstieg** — Gemäß ISO 12216 und RCD 2013/53/EU müssen bestimmte Wohnbereiche über Fluchtluken verfügen

Darüber hinaus dienen Decksluken als:
- Zugangsluken zu Lazarette, Ankerkästen, Stauräumen
- Wartungszugang zu Maschinenraum, Tanks, technischen Räumen
- Lastöffnungen für Proviantierung und Ausrüstung

### 1.2 Regulatorischer Rahmen — Überblick

#### 1.2.1 EU Recreational Craft Directive (RCD) 2013/53/EU

Die RCD gilt für alle Wasserfahrzeuge von 2,5 m bis 24 m Rumpflänge, die in der EU in Verkehr gebracht werden. Decksluken fallen unter mehrere Anforderungen:

- **Anhang I, Abschnitt 3.2 (Stabilität und Auftrieb):** Alle Öffnungen, die bei Flutung die Stabilität beeinträchtigen, müssen schnell und sicher verschlossen werden können.
- **Anhang I, Abschnitt 3.4 (Schutz vor Wassereinbruch):** Luken müssen der jeweiligen Design-Kategorie entsprechend wasserdicht sein.
- **Anhang I, Abschnitt 3.6 (Fluchtwege):** Wohnbereiche benötigen alternative Ausgänge (Fluchtluken).
- **Anhang I, Abschnitt 5.5 (Brandschutz):** Fluchtluken müssen auch bei Brand zugänglich bleiben.

**Design-Kategorien und Luken-Anforderungen:**

| Kategorie | See-Bedingungen | Mindestanforderung Luken |
|-----------|----------------|--------------------------|
| A (Hochsee) | Beaufort >8, Wellen >4 m | Alle Luken verschließbar gegen Grünwasser, Fluchtluken mit Schnellverschluss, Süllhöhe ≥300 mm (ISO 11812) |
| B (Offshore) | Beaufort ≤8, Wellen ≤4 m | Alle Luken verschließbar gegen überkommendes Wasser, Fluchtluken vorgeschrieben, Süllhöhe ≥250 mm |
| C (Küstennah) | Beaufort ≤6, Wellen ≤2 m | Luken wasserdicht bei Spritzwasser, Fluchtluken empfohlen, Süllhöhe ≥150 mm |
| D (Geschützt) | Beaufort ≤4, Wellen ≤0,3 m | Luken spritzwasserdicht, Fluchtluken empfohlen, keine Süllhöhenanforderung |

#### 1.2.2 ISO 12216:2002 (+ Amendment 2020)

**ISO 12216 "Small craft — Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements"**

Dies ist DIE zentrale Norm für Decksluken im Yachtbau. Sie definiert:

**Anwendungsbereich:**
- Luken in Booten von 2,5 m bis 24 m Rumpflänge
- Unterscheidung zwischen Luken in „weather-exposed" und „protected" Positionen
- Luken werden nach Position auf dem Boot klassifiziert (Höhe über Wasserlinie, Lage relativ zur Bugwelle)

**Wesentliche Anforderungen nach ISO 12216:**

| Parameter | Anforderung | Anmerkung |
|-----------|-------------|-----------|
| Festigkeit Lukendeckel | Druckprüfung gemäß Design-Kategorie | Kat. A: 6,0 kPa, Kat. B: 4,0 kPa, Kat. C: 2,5 kPa, Kat. D: 1,5 kPa (bei Position 1, Expositionsklasse A) |
| Wasserdichtheit | Berieselungsprüfung (spray test) ODER Überflutungsprüfung (flood test) | Kein Wasser darf in den Innenraum gelangen |
| Fluchtluken | Mindestöffnung 400 mm × 520 mm ODER Durchmesser 450 mm | Messung der lichten Weite bei vollständiger Öffnung |
| Fluchtluken — Zugänglichkeit | Von innen ohne Werkzeug zu öffnen | Keine Schlösser, die nur mit Schlüssel geöffnet werden |
| Transparente Lukendeckel | Acrylglas (PMMA): min. 10 mm bei bis zu 600 mm Kantenlänge | Polycarbonat (PC): geringere Dicke erlaubt wegen höherer Schlagfestigkeit |
| Rahmenverankerung | Mindest-Schraubenabstand 150 mm | Minimum 6 Befestigungspunkte pro Luke |
| Rückhaltung | Luke muss bei Öffnung gesichert bleiben | Lukendeckel darf nicht unkontrolliert zuschlagen (Verletzungsgefahr) |

**Luken-Positionsklassen nach ISO 12216:**

- **Position 1:** Vordeck, dem Bug zugewandt, unterhalb der Deckslinie — höchste Belastung
- **Position 2:** Mittschiffs, seitlich oder achtern, auf Deckshöhe — mittlere Belastung
- **Position 3:** Aufbaudeck, geschützt durch Aufbauten — geringere Belastung

**Amendment 2020 — Wesentliche Änderungen:**
- Verschärfte Prüfdrücke für Luken in Position 1 bei Kategorie A und B
- Zusätzliche Anforderung an Ermüdungsfestigkeit von Scharnieren (min. 10.000 Zyklen)
- Klarstellung der Anforderungen an motorisch betriebene Luken (Einklemmschutz)
- Erweiterte UV-Alterungsanforderungen für transparente Lukendeckel (2.000 h Xenon-Bogenlampe)

#### 1.2.3 ISO 9097:1991 "Small craft — Electric fans and ventilators"

Bezug zu Decksluken: Die Norm regelt die Belüftungsanforderungen, die teilweise durch Decksluken erfüllt werden:

- **Wohnbereiche:** Mindest-Lüftungsquerschnitt = 0,04 × Bodenfläche (m²) des Raumes
- **Kombüse:** Erhöhte Anforderung wegen Kochdämpfen und Feuchtigkeit
- **Maschinenraum:** Belüftungsquerschnitt = max(0,05 m², Motor_kW × 0,0003 m²)
- **WC/Nasszelle:** Eigenständige Belüftung erforderlich, Luke oder Ventilator

Decksluken tragen zum passiven Lüftungsquerschnitt bei. Eine Standardluke 500 × 500 mm mit 90°-Öffnung bietet ca. 0,25 m² effektiven Lüftungsquerschnitt. Mit Mückenschutzgitter reduziert sich dies auf ca. 0,15–0,18 m² (Reduktionsfaktor 0,6–0,72).

#### 1.2.4 ISO 15085:2003 "Small craft — Man-overboard prevention and recovery"

Bezug zu Decksluken bezüglich Stolper- und Sturzgefahr:

- **Lukensüll (Coaming/Sill):** Erhöhte Lukenrahmen müssen so konstruiert sein, dass sie keine Stolperfalle auf dem Arbeitsdeck darstellen
- **Flush-Luken:** Bevorzugt auf Arbeitsdecks wegen geringer Stolpergefahr
- **Lukenrückhaltung:** Geöffnete Luken dürfen nicht in den Fußweg ragen (Stoßgefahr)
- **Grip-Oberfläche:** Lukendeckel, die begangen werden, müssen rutschhemmend sein (Anti-Skid)

**Süllhöhen nach ISO 11812 (Cockpits) — übertragen auf Decksluken:**

| Position | Kat. A | Kat. B | Kat. C | Kat. D |
|----------|--------|--------|--------|--------|
| Cockpitboden → Niedergang | 300 mm | 250 mm | 150 mm | 0 mm |
| Deck → Vordeck-Luke (Süll) | 50–80 mm | 30–50 mm | 0–30 mm | 0 mm |
| Deck → Salon-Luke (Aufbau) | 80–120 mm | 50–80 mm | 30–50 mm | 0 mm |

**Hinweis:** Flush-Luken (Süllhöhe 0 mm) sind in Kategorie A nicht für Position 1 zulässig, es sei denn, sie erfüllen die Druckprüfung für Grünwasser.

#### 1.2.5 ABYC H-2 "Ventilation of Boats Using Gasoline"

Primär relevant für US-Markt (American Boat and Yacht Council):

- Definiert Pflicht-Belüftung für Räume mit Benzindämpfen (Motoryachten)
- Luken im Maschinenraum benötigen Funkenfreiheit bei Benzinbetrieb
- Natürliche Belüftung durch Luken kann mechanische Belüftung ergänzen, aber nicht ersetzen bei Benzinmotoren
- Luken in der Nähe von Tankfüllstutzen: Abstand ≥600 mm (ABYC A-7)

#### 1.2.6 ABS Guide for Building and Classing Motor Pleasure Yachts

Für Yachten >24 m (Superyachten), die ABS-klassifiziert sind:

- **Kapitel 6, Section 4:** Luken und Öffnungen auf freiliegendem Deck
- **Scantling-Anforderungen:** Rahmenstärke und Deckelverstärkung berechnet nach Wellenhöhe und Schiffsgeschwindigkeit
- **Wetterdecks-Luken:** Verschraubung alle 100 mm bei Edelstahl, alle 75 mm bei Aluminium
- **Watertight-Integrity:** Luken auf Wetterdeck müssen watertight sein, nicht nur weathertight

#### 1.2.7 Lloyd's SSC (Special Service Craft) Rules

Für Charter- und Passagieryachten sowie schnelle Motorboote:

- Verschärfte Anforderungen an Fluchtluken (größere Mindestmaße: 450 × 600 mm)
- Brandschutzanforderungen an Luken in Fluchtwegen
- Luken in Maschinenräumen: selbstschließend und feuerhemmend (30 min)
- Periodische Prüfung der Lukendichtigkeit (jährlich bei Charter)

#### 1.2.8 Zusammenfassung: Normenhierarchie

```
RCD 2013/53/EU (gesetzlich bindend in der EU)
  └─ harmonisierte Normen:
       ├─ ISO 12216 (Festigkeit & Wasserdichtheit) — PRIMÄRE Lukennorm
       ├─ ISO 11812 (Cockpits — Süllhöhen)
       ├─ ISO 9097 (Belüftung)
       ├─ ISO 15085 (MOB-Prävention — Stolperschutz)
       ├─ ISO 12217 (Stabilität — Gewicht von Luken)
       └─ ISO 9094 (Brandschutz — Fluchtluken)
  Ergänzend:
       ├─ ABYC H-2 / A-7 (US-Markt)
       ├─ ABS Guide (Superyachten >24 m)
       └─ Lloyd's SSC (Charter/Passagier)
```

### 1.3 Normkonforme Prüfverfahren für Decksluken

#### 1.3.1 Festigkeitsprüfung (ISO 12216, Clause 8)

**Druckprüfung des Lukendeckels:**
1. Luke einbauen in Prüfstand oder auf Bootssektion
2. Gleichmäßig verteilte Last auf Lukendeckel aufbringen (Wasserballon oder pneumatisch)
3. Prüfdruck gemäß Position und Design-Kategorie halten für 5 Minuten
4. Keine permanente Verformung >0,5 % der Diagonale
5. Keine Rissbildung in Linse oder Rahmen
6. Scharniere und Verschlüsse bleiben funktionsfähig

**Prüfdrücke (kPa) — Luken in Position 1:**

| Design-Kategorie | Expositionsklasse A | Expositionsklasse B |
|-------------------|--------------------|--------------------|
| A (Hochsee) | 6,0 | 4,5 |
| B (Offshore) | 4,0 | 3,0 |
| C (Küstennah) | 2,5 | 2,0 |
| D (Geschützt) | 1,5 | 1,0 |

**Expositionsklasse A:** Luken ohne Schutz durch Aufbauten
**Expositionsklasse B:** Luken teilweise geschützt durch Aufbauten, Hardtop oder Windschild

> ⚠️ **ZU PRÜFEN (Audit):** Diese ISO-12216-Prüfdrücke für Position 1, Expositionsklasse A (Kat. A: 6,0 kPa, B: 4,0, C: 2,5, D: 1,5) stehen im Widerspruch zu den Werten in Abschnitt 10.1.2, wo für dieselbe Zone und Kategorie (Kat. A, Vorschiff/Position 1) ein Prüfdruck von 12,0–18,0 kPa angegeben ist — ein Faktor 2–3 bei gleicher Design-Kategorie und Einbauposition. Der 6,0-kPa-Wert steht intern konsistent an drei Stellen (Abschnitte 1.2.2, 1.3.1 und 9.1.1); Abschnitt 10.1.2 ist die abweichende Einzelquelle. Die genormten Prüfdruckwerte (ISO 12216:2002/2020, Bemessungsdruck P nach Fläche und Design-Kategorie) konnten nicht aus frei zugänglichen Quellen verifiziert werden. Zahlen daher NICHT geändert — durch Fachprüfer gegen die Originalnorm abzugleichen und zu vereinheitlichen.

#### 1.3.2 Wasserdichtheitsprüfung (ISO 12216, Clause 9)

**Methode 1 — Berieselungsprüfung (Spray Test):**
- Wasserstrahl aus Düse, Druck 0,5 bar, Abstand 1,5 m
- 5 Minuten pro Seite der Luke
- Luke ist geschlossen und verriegelt
- Kein Wasser darf auf der Innenseite erscheinen

**Methode 2 — Überflutungsprüfung (Flood Test):**
- Luke horizontal montiert
- 100 mm Wasserstand über Lukenoberkante
- 10 Minuten Standzeit
- Kein Wasser darf auf der Innenseite erscheinen

**Methode 3 — Schlauchprüfung (Hose Test, für Superyachten):**
- Feuerwehrschlauch, 2 bar Druck, Düsendurchmesser 12 mm
- Abstand 1,5 m, systematisch alle Kanten und Ecken
- 2 Minuten pro Seite
- Kein Wasser darf auf der Innenseite erscheinen

---

## 2. Zukunftstechnologien

### 2.1 Elektrisch betriebene Luken

**Status quo:**
Elektrisch betriebene Decksluken sind im Superyachtbereich (>24 m) bereits Standard, im Serienboot-Segment (8–18 m) jedoch noch Nischenprodukt.

**Marktführer für elektrische Luken:**
- **Freeman Marine (USA):** Hydraulisch und elektrisch betriebene Luken für Superyachten, ab ca. 5.000 EUR (800 × 800 mm). Modellreihe FH-Serie mit integriertem Controller, Einklemmschutz gemäß ISO 12216:2020 Amendment.
- **Lewmar Power Hatch:** Nachrüstbarer Elektromotor für Lewmar Ocean Serie (Size 50–70), Teilenummer 361710xxx. Motorspannung 12 V oder 24 V, Stromaufnahme 8 A bei 12 V. Öffnungszeit ca. 12 Sekunden. Preis ab ca. 1.200 EUR inkl. Controller.
- **Besenzoni (Italien):** Luxus-Luken für Motoryachten, vollautomatisch mit Regensensor. Modell PK-Serie, ab 3.500 EUR.

**Anforderungen nach ISO 12216:2020 Amendment an elektrische Luken:**
- Einklemmschutz: Abschaltung bei Widerstand >150 N
- Manuelle Override-Möglichkeit von innen
- Statusanzeige (offen/geschlossen) am Steuerstand
- Automatische Schließung bei Seegangsalarm (optional)

**Retrofitproblematik:**
- Kabelführung durch Deckskern erfordert Abdichtung
- Stromversorgung typisch 3–5 A bei 12 V, muss in Bordnetz-Berechnung einfließen
- Controller-Position: trocken, belüftet, zugänglich

### 2.2 Intelligente Luken mit Sensorik

**Konzepte in Entwicklung:**

| Feature | Sensor | Status | Erwartete Marktreife |
|---------|--------|--------|---------------------|
| Offen/Geschlossen-Erkennung | Reed-Kontakt | Verfügbar (Raymarine, B&G) | Jetzt |
| Wassereinbruch-Detektion | Leitfähigkeitssensor in Dichtungsnut | Prototyp | 2027–2028 |
| Regensensor → Auto-Close | Kapazitiver Regensensor | Verfügbar (Besenzoni) | Jetzt |
| Dichtungszustand-Monitoring | Druckdifferenz über Dichtung | Forschung | 2029+ |
| UV-Belastung Acryllinse | UV-Dosimeter integriert | Forschung | 2030+ |

**Integration in AYDI:**
Sensorische Luken-Daten können als Pipeline-A-Input (measured) verarbeitet werden. Status offen/geschlossen ist binär und liefert confidence: measured. Dichtungszustand-Monitoring würde die visuelle Inspektion (Pipeline B) ergänzen.

### 2.3 Materialinnovationen

**Acrylglas-Alternativen:**
- **PMMA mit integrierten Solar-Zellen:** Transluzent, generiert 10–30 W pro Luke. Prototypen bei Solbian (Italien). Problem: Blasenbildung bei Temperaturwechsel.
- **Electrochromic Glas:** Tönung per Knopfdruck (Gentex / Gauzy). Bereits in Superyacht-Fenstern, für Luken noch nicht adaptiert. Preis: ca. 2.000 EUR/m².
- **Self-healing Acrylglas:** Mikrokapseln mit Methyl-Methacrylat-Monomer heilen Kratzer bis 0,5 mm Tiefe. Laborstadium.

**Rahmenmaterialien:**
- **Kohlefaser-Composite-Rahmen:** 40–60 % leichter als Aluminium bei gleicher Festigkeit. Bisher nur im Racing-Segment (z.B. custom für Vendée-Globe-Boote). Preis: 5–10× Aluminium.
- **Recyceltes Aluminium:** Zunehmend bei Lewmar und Goiot, kein Qualitätsunterschied bei korrekter Legierung (EN AW-5083 oder 6061-T6).

### 2.4 3D-gedruckte Lukenkomponenten

**Aktueller Stand:**
- **Griffe und Hebel:** FDM-Druck in ASA oder PETG möglich, UV-beständig. Für Prototypen und Einzelstücke sinnvoll.
- **Dichtungsprofile:** TPU-Druck möglich, aber Druckverformungsrest deutlich höher als bei EPDM. Nur als Notlösung.
- **Lukenrahmen:** SLA-Druck in Hochleistungsresin möglich, aber nicht UV-stabil genug für Dauereinsatz.
- **Vollständige Luken:** Nicht realistisch im 3D-Druck. Festigkeits- und Dichtungsanforderungen gemäß ISO 12216 nicht erfüllbar.

---

## 3. Best Practices nach Revier

### 3.1 Nordeuropa (Ostsee, Nordsee, Britische Inseln, Skandinavien)

**Bedingungen:** Kalte Winter (-15 °C bis +25 °C), moderate UV-Belastung, Salzwasser (Nordsee: 35 ‰, Ostsee: 6–18 ‰), häufiger Regen, gelegentlich Grünwasser.

**Empfehlungen:**
- **Lukentyp:** Ocean-Profil oder Medium-Profil bevorzugt (Süllhöhe für Grünwasser)
- **Linse:** Acrylglas 10 mm ausreichend (moderate UV), getönt unnötig
- **Dichtung:** EPDM (Standard, gute Kälteflexibilität bis -40 °C)
- **Rahmen:** Eloxiertes Aluminium (Standardlegierung EN AW-6060-T5)
- **Mückenschutz:** In Schweden/Finnland: obligatorisch, Fliegengitter als Festrahmen
- **Winterabdeckung:** Plane oder Hardcover über Luken bei Winterlager verhindert Schnee/Eis-Belastung und verlängert Dichtungslebensdauer um 30–50 %
- **Intervall Dichtungswechsel:** Alle 8–12 Jahre (moderate UV)
- **Intervall Acrylpolitur:** Alle 3–5 Jahre
- **Typische Hersteller ab Werft:** Lewmar (UK-Werften), Goiot (französische Werften), Bomar (US-Importe)

### 3.2 Mittelmeer (Côte d'Azur, Italien, Griechenland, Türkei, Kroatien, Spanien)

**Bedingungen:** Milde Winter (+5 °C bis +38 °C), extreme UV-Belastung (2.500–3.000 Sonnenstunden/Jahr), Salzwasser 38 ‰, seltenes Grünwasser, Staub/Sand.

**Empfehlungen:**
- **Lukentyp:** Flush-Luken oder Low-Profile bevorzugt (Ästhetik, weniger Verschmutzung)
- **Linse:** Acrylglas 10–12 mm, getönt (Rauchglas, Bronzeton) reduziert Hitze unter Deck. Bei Superyachten: laminiertes Sicherheitsglas
- **Dichtung:** Silikon bevorzugt (bessere UV-Beständigkeit als EPDM), alternativ EPDM mit erhöhtem UV-Stabilisator
- **Rahmen:** Eloxiertes Aluminium (hart eloxiert, 20+ µm Schichtdicke), bei Superyachten Edelstahl 316L
- **Mückenschutz:** Absolut obligatorisch Juni–September, Magnetrahmen-System am komfortabelsten
- **Sonnenschutz:** Innen-Jalousie (Pleated Blind) essenziell, reduziert Kabinentemperatur um 5–10 °C
- **Intervall Dichtungswechsel:** EPDM alle 5–7 Jahre (hohe UV), Silikon alle 10–15 Jahre
- **Intervall Acrylpolitur:** Alle 2–3 Jahre (UV-bedingt)
- **Speziell:** Sandstaub aus Sahara (Scirocco/Sirocco) setzt sich in Dichtungsnuten fest → regelmäßig ausspülen
- **Typische Hersteller ab Werft:** Goiot (Bénéteau, Jeanneau), Moonlight (italienische Werften), Lewmar

### 3.3 Tropen (Karibik, Pazifik, Südostasien)

**Bedingungen:** Ganzjährig warm (+25 °C bis +45 °C Oberfläche), extreme UV, Salzwasser 35 ‰, tropische Regengüsse (Intensität 100+ mm/h), Hurrikane/Zyklone.

**Empfehlungen:**
- **Lukentyp:** Ocean-Profil (Hurrikan-Sicherheit), Flush nur bei Motoryachten im geschützten Bereich
- **Linse:** Polycarbonat (Lexan) statt Acrylglas wegen Schlagfestigkeit (Debris bei Stürmen). Nachteil: schnellere UV-Trübung (Vergilbung nach 3–5 Jahren)
- **Dichtung:** Silikon zwingend (EPDM verhärtet bei dauerhaft >35 °C schneller)
- **Rahmen:** Eloxiertes Aluminium mit extra UV-Schutz oder Edelstahl 316L
- **Mückenschutz:** Obligatorisch ganzjährig (Moskitos, No-See-Ums). Feinmaschig (1,0 mm) für No-See-Ums
- **Sturm-Deadlights:** Massive Abdeckungen (Edelstahl oder Aluminium) zum Aufbolzen bei Hurrikan-Warnung. Freeman Marine und Lewmar bieten passende Sturmdeckel
- **Intervall Dichtungswechsel:** EPDM alle 3–5 Jahre (!), Silikon alle 6–10 Jahre
- **Intervall Acrylpolitur:** Jährlich bei Acryl, alle 2 Jahre bei Polycarbonat
- **Schimmel:** Dichtungsnuten alle 4–6 Wochen mit Essigwasser reinigen
- **Typische Hersteller ab Werft:** Bomar (US-Markt), Lewmar (britische/internationale Werften)

### 3.4 Hochsee / Blauwasser-Segeln

**Bedingungen:** Alle Klimazonen, Grünwasser, lang andauernde Seegänge, keine Werftbesuche für Monate.

**Empfehlungen:**
- **Lukentyp:** Ausschließlich Ocean-Profil (Lewmar Ocean oder Goiot Opal) auf Vorschiff. Flush-Luken NUR achtern/auf Aufbau in geschützter Position.
- **Linse:** 12 mm Acrylglas oder Polycarbonat für Vorschiff-Luken. Sturmdeckel (Deadlights) als Backup.
- **Dichtung:** Ersatzdichtung für jede Lukengröße an Bord. Satz Lewmar-Ersatzdichtungen ca. 150–250 EUR.
- **Rahmen:** Ocean-Profil mit erhöhtem Süll bietet strukturelle Sicherheit
- **Reparatur-Kit an Bord:** Dichtungsprofil (2 m Meterware), Dichtungskleber (3M 4200 oder Saba 70T), Acryl-Reparaturpaste (Acrifix 192), Ersatz-Gasdruckfedern, Edelstahl-Schrauben M5/M6
- **Öffnungsverriegelung:** Luken MÜSSEN bei Seegang sicher verriegelt werden können — sowohl in offener als auch in geschlossener Position
- **Fluchtluken:** Mindestens 2 alternative Ausgänge für jede Schlafkabine, monatlich Funktionsprüfung

### 3.5 Binnengewässer (Seen, Flüsse, Kanäle)

**Bedingungen:** Süßwasser, keine Salzkorrosion, moderate Belastung, häufig Niedrigprofil wegen Brücken.

**Empfehlungen:**
- **Lukentyp:** Low-Profile oder Flush bevorzugt (Brückendurchfahrt, Ästhetik)
- **Linse:** Acrylglas 8 mm ausreichend (keine Grünwasser-Belastung)
- **Dichtung:** EPDM Standard, lange Lebensdauer in Süßwasser (12–15 Jahre)
- **Rahmen:** Aluminium Standard-Eloxierung ausreichend, kein 316L nötig
- **Budget-Tipp:** Manship oder Vetus Libero ausreichend für CE Kat. D
- **Speziell:** Niedrige Luken-Profile (Lewmar Low Profile, <40 mm Süll) für Kanalboote

---

## 4. Regional Sourcing

### 4.1 Europa

| Region | Bevorzugter Lieferant | Lieferzeit | Versandkosten (Pauschal, 1 Luke) |
|--------|----------------------|------------|----------------------------------|
| Deutschland | SVB (Bremen), Toplicht (Hamburg), AWN (Wedel) | 2–5 Werktage | 8–15 EUR |
| Frankreich | Accastillage Diffusion, Uship | 3–5 Werktage | 10–18 EUR |
| UK | Force 4, Marine Superstore, Sea Teach | 2–4 Werktage | 12–20 GBP |
| Italien | Forniture Nautiche Italiane (FNI), Osculati Direct | 3–7 Werktage | 12–22 EUR |
| Niederlande | Maritiem, Sailing Chandlery | 2–4 Werktage | 10–15 EUR |
| Skandinavien | Hjertmans (SE), Biltema Marine (SE/NO/FI) | 3–6 Werktage | 15–25 EUR |
| Griechenland | Naftaid, SunSails | 5–10 Werktage | 15–30 EUR |
| Kroatien | Nautic Center, Pro Marine | 5–10 Werktage | 15–25 EUR |
| Türkei | Setur Marina Shops, lokale Händler | 3–7 Werktage | 10–20 EUR |

### 4.2 Nordamerika

| Region | Bevorzugter Lieferant | Lieferzeit | Versandkosten |
|--------|----------------------|------------|---------------|
| US Ostküste | West Marine, Defender, Hamilton Marine | 2–5 Werktage | 15–35 USD |
| US Westküste | West Marine, Fisheries Supply | 3–7 Werktage | 15–35 USD |
| Kanada | Maritime Chandlery, National Sailboat Hardware | 5–10 Werktage | 20–40 CAD |

### 4.3 Karibik / Tropisch

| Region | Bevorzugter Lieferant | Lieferzeit | Anmerkung |
|--------|----------------------|------------|-----------|
| Karibik (US VI, BVI) | Budget Marine | 5–15 Werktage | Vor Ort in Tortola, St. Maarten, Trinidad |
| Karibik (Martinique/Guadeloupe) | Accastillage Diffusion | 7–14 Werktage | Französisches Übersee-Departement |
| Panama | Panamarine, ISM Agents | 10–20 Werktage | US-Importe über Colon Free Zone |
| Australien | Whitworths, CH Smith | 3–7 Werktage (Festland) | Gute Lewmar-Verfügbarkeit |
| Neuseeland | Burnsco, Marine Deals | 3–7 Werktage | Gute Verfügbarkeit |

### 4.4 Notfall-Sourcing

Wenn eine Luke auf See oder in abgelegener Region beschädigt wird:

1. **Lewmar-Niederlassung:** Lewmar hat Vertretungen in 40+ Ländern. Service-Netz: lewmar.com/distributors
2. **Bootshersteller-Service:** Bénéteau, Bavaria, Hanse haben Service-Stützpunkte in allen wichtigen Revieren
3. **Universalersatz:** Bomar Standard-Luken sind in fast jedem West Marine verfügbar (US-Markt)
4. **3D-Druck Notlösung:** Griffe, Hebel, Abstandshalter in ASA/PETG druckbar in Maker-Spaces (verfügbar in vielen Marinas)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Rolle innerhalb AYDI

Diese Wissensdatei dient als domänenspezifische Referenz für die AYDI-Analyse-Engine. Sie wird in drei Pipelines genutzt:

**Pipeline A (Strukturierte Daten):**
- Bewertung von Luken-Spezifikationen aus CAD-Daten oder Bootsdatenblättern
- Normkonformitätsprüfung (ISO 12216, RCD 2013/53/EU)
- Parametrische Kostenabschätzung für Luken (Neubau und Retrofit)
- Materialverträglichkeitsprüfung (Rahmenmaterial vs. Befestigung vs. Dichtung)

**Pipeline B (Visuelle Analyse):**
- Erkennung von Lukentypen auf Fotos (Ocean/Low Profile/Flush)
- Zustandsbeurteilung: Crazing in Acryllinse, verfärbte Dichtungen, korrodierte Rahmen
- Identifikation von Hersteller und Serie anhand visueller Merkmale
- Erkennung von unsachgemäßen Installationen (fehlende Dichtung, falsche Schrauben)

**Pipeline C (Textanalyse):**
- Auswertung von Service-Berichten und Gutachten bezüglich Lukenprobleme
- Mustererkennung: wiederkehrende Probleme bei bestimmten Boots-/Lukenkombinationen
- Forum-Thread-Analyse: Community-Erfahrungen mit spezifischen Lukenmodellen

### 5.2 Abgrenzung

Diese Datei behandelt **Decksluken** — verschließbare Öffnungen im Deck. NICHT behandelt werden:
- Fenster und Portlights (→ 08_02_fenster_portlights.md)
- Niedergang / Companionway (→ 08_03_niedergang.md)
- Türen (→ 08_04_tueren.md)
- Bullaugen (→ 08_02_fenster_portlights.md)
- Motorraumluken mit Schalldämmung (→ 08_05_motorraumluken.md)

### 5.3 Confidence-Zuordnung in dieser Datei

| Datenquelle | Confidence-Code | Beispiel |
|-------------|----------------|---------|
| ISO-Normen | measured | Prüfdrücke, Mindestmaße |
| Hersteller-TDS / Katalog | measured | Abmessungen, Materialspezifikationen |
| Hersteller-Preislisten | documented | Preise (Stand 2025/2026) |
| Werft-Dokumentation | documented | OEM-Zuordnung Bootshersteller → Luke |
| Forum-Konsens (>5 unabhängige Quellen) | documented | Lebensdauer-Erfahrungen |
| Einzelne Erfahrungsberichte | estimated | Retrofit-Erfahrungen |
| AYDI-Berechnung | calculated | Belüftungsbeitrag, Gewichtsschätzung |

---

## 6. Pydantic-Modelle

### 6.1 DeckHatchSpec — Spezifikation einer einzelnen Decksluke

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum


class HatchType(str, Enum):
    """Luken-Grundtyp."""
    OPENING = "opening"           # Öffnungsluke (Standard, klappbar)
    FLUSH = "flush"               # Flächenbündige Luke
    SLIDING = "sliding"           # Schiebeluke
    BUTTERFLY = "butterfly"       # Schmetterlingsöffnung (2 Klappen)
    ESCAPE = "escape"             # Fluchtluke (Notausstieg)
    ACCESS = "access"             # Zugangsluke (Lazarette, Stauräume)
    ENGINE = "engine"             # Maschinenraumluke
    ANCHOR = "anchor"             # Ankerkastenluke
    FOREDECK_SAIL = "foredeck_sail"  # Vorschiff-Segelluke (Spinnaker-Chute)


class HatchProfile(str, Enum):
    """Profil-Höhe der Luke."""
    OCEAN = "ocean"               # Hoher Süll, 60-80 mm über Deck
    MEDIUM = "medium"             # Mittlerer Süll, 35-55 mm über Deck
    LOW = "low"                   # Niedriger Süll, 15-35 mm über Deck
    FLUSH = "flush"               # Flächenbündig, 0-5 mm über Deck


class FrameMaterial(str, Enum):
    """Rahmenmaterial."""
    ALUMINUM_ANODIZED = "aluminum_anodized"       # Eloxiertes Aluminium (Standard)
    ALUMINUM_PAINTED = "aluminum_painted"          # Lackiertes Aluminium
    ALUMINUM_HARD_ANODIZED = "aluminum_hard_anodized"  # Hart-eloxiert
    STAINLESS_316L = "stainless_316l"              # Edelstahl 316L
    COMPOSITE = "composite"                        # GFK/CFK-Composite
    BRONZE = "bronze"                              # Bronze (klassische Yachten)
    TEAK_FRAMED = "teak_framed"                    # Teakholz-Rahmen (Decor)


class LensMaterial(str, Enum):
    """Linsenmaterial des Lukendeckels."""
    ACRYLIC_CLEAR = "acrylic_clear"               # Acrylglas (PMMA) klar
    ACRYLIC_TINTED = "acrylic_tinted"             # Acrylglas getönt (Rauchglas/Bronze)
    POLYCARBONATE_CLEAR = "polycarbonate_clear"   # Polycarbonat (Lexan) klar
    POLYCARBONATE_TINTED = "polycarbonate_tinted" # Polycarbonat getönt
    TEMPERED_GLASS = "tempered_glass"             # Einscheiben-Sicherheitsglas (ESG)
    LAMINATED_GLASS = "laminated_glass"           # Verbundsicherheitsglas (VSG)
    SOLID_ALUMINUM = "solid_aluminum"             # Massiver Aludeckel (kein Licht)
    SOLID_GRP = "solid_grp"                       # Massiver GFK-Deckel
    SOLID_TEAK = "solid_teak"                     # Teakholz-Deckel


class SealType(str, Enum):
    """Dichtungstyp."""
    EPDM_COMPRESSION = "epdm_compression"         # EPDM Kompressionsdichtung (Standard)
    SILICONE_COMPRESSION = "silicone_compression"  # Silikon Kompressionsdichtung
    EPDM_LIP = "epdm_lip"                         # EPDM Lippendichtung
    INFLATABLE = "inflatable"                      # Aufblasbare Dichtung (Superyacht)
    NEOPRENE = "neoprene"                          # Neopren (historisch)
    TPE = "tpe"                                    # Thermoplastisches Elastomer
    PUR_SEAL = "pur_seal"                          # PU-Rahmen-Verklebung (nicht austauschbar)


class HatchLocation(str, Enum):
    """Position der Luke auf dem Boot."""
    FOREDECK = "foredeck"                  # Vorschiff (Bug-Kabine)
    FOREDECK_SAIL = "foredeck_sail"        # Vorschiff Segelluke
    SALOON_PORT = "saloon_port"            # Salon Backbord
    SALOON_STARBOARD = "saloon_starboard"  # Salon Steuerbord
    SALOON_CENTER = "saloon_center"        # Salon Mitte
    AFT_CABIN_PORT = "aft_cabin_port"      # Achterkabine Backbord
    AFT_CABIN_STARBOARD = "aft_cabin_starboard"  # Achterkabine Steuerbord
    COCKPIT = "cockpit"                    # Cockpit
    LAZARETTE = "lazarette"                # Lazarett (achtern)
    ENGINE_ROOM = "engine_room"            # Maschinenraum
    ANCHOR_LOCKER = "anchor_locker"        # Ankerkasten
    ESCAPE = "escape"                      # Fluchtluke (beliebige Position)
    HEAD = "head"                          # WC/Nasszelle
    PASSAGEWAY = "passageway"              # Gangbord


class CECategory(str, Enum):
    """CE Design-Kategorie."""
    A = "A"  # Hochsee
    B = "B"  # Offshore
    C = "C"  # Küstennah
    D = "D"  # Geschützt


class DeckHatchSpec(BaseModel):
    """Vollständige Spezifikation einer einzelnen Decksluke.

    Dient als Input für die AYDI-Analyse-Engine (Pipeline A).
    Alle Maße in mm, Gewichte in kg, Preise in EUR.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(
        ...,
        description="Lukenhersteller (z.B. 'Lewmar', 'Goiot', 'Bomar')"
    )
    series: str = Field(
        ...,
        description="Lukenserie (z.B. 'Ocean', 'Low Profile', 'Cristal', 'Opal')"
    )
    model_number: Optional[str] = Field(
        None,
        description="Hersteller-Modellnummer (z.B. 'Size 50', '53050', 'T25')"
    )
    part_number: Optional[str] = Field(
        None,
        description="OEM-Teilenummer (z.B. Lewmar '39950070')"
    )

    # Typ und Profil
    hatch_type: HatchType = Field(
        HatchType.OPENING,
        description="Lukentyp"
    )
    profile: HatchProfile = Field(
        HatchProfile.OCEAN,
        description="Profilhöhe"
    )
    location: HatchLocation = Field(
        ...,
        description="Position auf dem Boot"
    )

    # Abmessungen (alle in mm)
    outer_width_mm: float = Field(
        ...,
        description="Außenmaß Breite in mm (Rahmen-Außenkante)"
    )
    outer_length_mm: float = Field(
        ...,
        description="Außenmaß Länge in mm (Rahmen-Außenkante)"
    )
    cutout_width_mm: float = Field(
        ...,
        description="Deckausschnitt Breite in mm"
    )
    cutout_length_mm: float = Field(
        ...,
        description="Deckausschnitt Länge in mm"
    )
    clear_opening_width_mm: Optional[float] = Field(
        None,
        description="Lichte Weite Breite in mm (relevant für Fluchtluken)"
    )
    clear_opening_length_mm: Optional[float] = Field(
        None,
        description="Lichte Weite Länge in mm (relevant für Fluchtluken)"
    )
    profile_height_mm: float = Field(
        ...,
        description="Profilhöhe über Deck in mm"
    )
    lens_thickness_mm: float = Field(
        10.0,
        description="Linsendicke in mm (typisch 8-15 mm)"
    )
    deck_thickness_range_mm: str = Field(
        "10-50",
        description="Geeignete Decksstärke in mm (z.B. '10-50', '15-60')"
    )

    # Materialien
    frame_material: FrameMaterial = Field(
        FrameMaterial.ALUMINUM_ANODIZED,
        description="Rahmenmaterial"
    )
    lens_material: LensMaterial = Field(
        LensMaterial.ACRYLIC_CLEAR,
        description="Linsenmaterial"
    )
    seal_type: SealType = Field(
        SealType.EPDM_COMPRESSION,
        description="Dichtungstyp"
    )

    # Mechanik
    opening_mechanism: str = Field(
        "hinged_forward",
        description="Öffnungsmechanismus: hinged_forward, hinged_aft, hinged_side, "
                    "sliding, butterfly, lift_off, power"
    )
    opening_angle_max_deg: int = Field(
        60,
        description="Maximaler Öffnungswinkel in Grad (typisch 55-180)"
    )
    stay_type: str = Field(
        "gas_strut",
        description="Haltesystem: gas_strut, friction_stay, spring_arm, "
                    "telescopic, chain, none"
    )
    locking_mechanism: str = Field(
        "cam_lever",
        description="Verschlussmechanismus: cam_lever, toggle, spindle, "
                    "push_button, slam_latch, over_center"
    )
    lock_points: int = Field(
        2,
        description="Anzahl Verriegelungspunkte (typisch 1-4)"
    )

    # CE / Norm
    ce_category_max: CECategory = Field(
        CECategory.B,
        description="Maximale CE-Kategorie, für die die Luke zugelassen ist"
    )
    iso_12216_position: int = Field(
        2,
        description="ISO 12216 Positionsklasse (1, 2 oder 3)"
    )
    is_escape_hatch: bool = Field(
        False,
        description="Erfüllt Anforderungen als Fluchtluke (min. 400×520 mm lichte Weite)"
    )
    is_walkable: bool = Field(
        False,
        description="Für Begehung zugelassen (Anti-Skid-Oberfläche)"
    )

    # Zubehör
    has_mosquito_screen: bool = Field(
        False,
        description="Mückenschutz-Gitter enthalten/eingebaut"
    )
    has_blind: bool = Field(
        False,
        description="Verdunkelungs-Rollo oder Plissee enthalten"
    )
    has_ventilation_position: bool = Field(
        True,
        description="Arretierung in Lüftungsstellung (10-15°) möglich"
    )

    # Gewicht und Preis
    weight_kg: Optional[float] = Field(
        None,
        description="Gewicht komplett in kg"
    )
    price_eur: Optional[float] = Field(
        None,
        description="Listenpreis in EUR (Stand 2025/2026)"
    )

    # Confidence
    confidence: str = Field(
        "measured",
        description="Confidence-Level: measured, documented, estimated"
    )
```

### 6.2 DeckHatchCondition — Zustandsbeurteilung einer verbauten Luke

```python
class HatchConditionRating(str, Enum):
    """Zustandsbewertung Einzelaspekt."""
    EXCELLENT = "excellent"       # Neuwertig, keine Mängel
    GOOD = "good"                 # Gebrauchsspuren, voll funktionsfähig
    FAIR = "fair"                 # Deutliche Abnutzung, funktionsfähig mit Einschränkungen
    POOR = "poor"                 # Starke Abnutzung, Funktion beeinträchtigt
    CRITICAL = "critical"        # Sicherheitsrelevanter Mangel, sofortige Maßnahme
    NOT_ASSESSABLE = "not_assessable"  # Nicht beurteilbar (nicht zugänglich, kein Foto)


class DeckHatchCondition(BaseModel):
    """Zustandsbeurteilung einer einzelnen verbauten Decksluke.

    Wird von Pipeline A (Inspektion) und Pipeline B (Foto-Analyse) befüllt.
    Jeder Zustandswert hat ein eigenes Confidence-Feld.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    hatch_id: str = Field(
        ...,
        description="Eindeutige ID der Luke im Boot (z.B. 'foredeck_main', 'saloon_p1')"
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
    hatch_manufacturer: Optional[str] = Field(
        None,
        description="Lukenhersteller (erkannt oder dokumentiert)"
    )
    hatch_series: Optional[str] = Field(
        None,
        description="Lukenserie"
    )
    location: HatchLocation = Field(
        ...,
        description="Position auf dem Boot"
    )
    estimated_age_years: Optional[float] = Field(
        None,
        description="Geschätztes Alter der Luke in Jahren"
    )

    # Zustand Linse
    lens_condition: HatchConditionRating = Field(
        HatchConditionRating.NOT_ASSESSABLE,
        description="Zustand der Linse (Acryl/PC/Glas)"
    )
    lens_condition_confidence: str = Field(
        "estimated",
        description="Confidence der Linsen-Bewertung"
    )
    lens_crazing: bool = Field(
        False,
        description="Haarrisse (Crazing) in der Linse sichtbar"
    )
    lens_yellowing: bool = Field(
        False,
        description="UV-bedingte Vergilbung sichtbar"
    )
    lens_scratches: str = Field(
        "none",
        description="Kratzer: none, light, moderate, deep"
    )
    lens_delamination: bool = Field(
        False,
        description="Delamination bei Verbundglas sichtbar"
    )

    # Zustand Dichtung
    seal_condition: HatchConditionRating = Field(
        HatchConditionRating.NOT_ASSESSABLE,
        description="Zustand der Dichtung"
    )
    seal_condition_confidence: str = Field(
        "estimated",
        description="Confidence der Dichtungs-Bewertung"
    )
    seal_compression_set: bool = Field(
        False,
        description="Dauerhafter Druckverformungsrest sichtbar (Dichtung bleibt flach)"
    )
    seal_hardened: bool = Field(
        False,
        description="Dichtung verhärtet (bei Berührung hart, nicht elastisch)"
    )
    seal_cracked: bool = Field(
        False,
        description="Risse in der Dichtung sichtbar"
    )
    seal_displaced: bool = Field(
        False,
        description="Dichtung aus der Nut gerutscht"
    )
    seal_mold: bool = Field(
        False,
        description="Schimmelbildung auf der Dichtung"
    )

    # Zustand Rahmen
    frame_condition: HatchConditionRating = Field(
        HatchConditionRating.NOT_ASSESSABLE,
        description="Zustand des Rahmens"
    )
    frame_condition_confidence: str = Field(
        "estimated",
        description="Confidence der Rahmen-Bewertung"
    )
    frame_corrosion: str = Field(
        "none",
        description="Korrosion: none, surface, pitting, structural"
    )
    frame_anodizing_worn: bool = Field(
        False,
        description="Eloxierung abgetragen/fleckig"
    )
    frame_crevice_corrosion: bool = Field(
        False,
        description="Spaltkorrosion an Rahmen-Deck-Übergang"
    )

    # Zustand Mechanik
    mechanism_condition: HatchConditionRating = Field(
        HatchConditionRating.NOT_ASSESSABLE,
        description="Zustand der Mechanik (Scharniere, Verschlüsse, Gasdruckfedern)"
    )
    mechanism_condition_confidence: str = Field(
        "estimated",
        description="Confidence der Mechanik-Bewertung"
    )
    gas_strut_weak: bool = Field(
        False,
        description="Gasdruckfeder(n) schwach (Luke fällt zu oder hält nicht)"
    )
    hinge_play: bool = Field(
        False,
        description="Spiel in den Scharnieren"
    )
    lock_functional: bool = Field(
        True,
        description="Verriegelung funktioniert korrekt"
    )

    # Wasserdichtheit
    watertight: Optional[bool] = Field(
        None,
        description="Luke ist wasserdicht (True/False/None=nicht geprüft)"
    )
    watertight_confidence: str = Field(
        "estimated",
        description="Confidence der Dichtheitsbewertung"
    )
    leak_location: Optional[str] = Field(
        None,
        description="Undichtigkeit wo: corner_forward, corner_aft, hinge_side, "
                    "lock_side, all_around, none"
    )

    # Gesamtbewertung
    overall_score: Optional[int] = Field(
        None,
        description="Gesamtscore 0-100 (100=neuwertig, 0=nicht mehr funktionsfähig)"
    )
    replacement_urgency: str = Field(
        "unknown",
        description="Dringlichkeit: immediate, soon, routine, ok, unknown"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    recommended_actions: List[str] = Field(
        default_factory=list,
        description="Empfohlene Maßnahmen (z.B. 'Dichtung tauschen', 'Linse polieren')"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None,
        description="Geschätzte Reparaturkosten in EUR"
    )

    # Meta
    confidence: str = Field(
        "estimated",
        description="Gesamt-Confidence-Level der Bewertung"
    )
    data_sources: List[str] = Field(
        default_factory=list,
        description="Datenquellen: 'visual', 'measured', 'documented', 'owner_report'"
    )
```

### 6.3 HatchSystemAssessment — Gesamtbewertung aller Luken eines Bootes

```python
class HatchSystemAssessment(BaseModel):
    """Gesamtbewertung des Lukensystems eines Bootes.

    Aggregiert alle Einzelluken-Bewertungen und prüft Systemaspekte
    (Normkonformität, Belüftungsbilanz, Fluchtweg-Analyse).
    """
    model_config = {"from_attributes": True}

    # Boot-Identifikation
    boat_manufacturer: str = Field(..., description="Bootshersteller")
    boat_model: str = Field(..., description="Bootsmodell")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    boat_length_mm: Optional[float] = Field(None, description="Bootslänge (LOA) in mm")
    boat_class: str = Field(
        "production_sailboat",
        description="Bootsklasse: production_sailboat, semicustom_cruiser, "
                    "custom_yacht, superyacht, production_motorboat"
    )
    ce_category: CECategory = Field(
        CECategory.C,
        description="CE-Designkategorie des Bootes"
    )

    # Einzelluken
    hatch_count: int = Field(0, description="Gesamtanzahl Decksluken")
    hatches: List[DeckHatchCondition] = Field(
        default_factory=list,
        description="Liste aller bewerteten Einzelluken"
    )

    # Normkonformität
    iso_12216_compliant: Optional[bool] = Field(
        None,
        description="Alle Luken konform zu ISO 12216 (True/False/None=nicht geprüft)"
    )
    iso_12216_findings: List[str] = Field(
        default_factory=list,
        description="Einzelbefunde zur ISO 12216 Konformität"
    )
    escape_hatches_compliant: Optional[bool] = Field(
        None,
        description="Fluchtluken vorhanden und konform"
    )
    escape_hatch_findings: List[str] = Field(
        default_factory=list,
        description="Befunde zu Fluchtluken"
    )

    # Belüftungsbilanz
    total_ventilation_area_mm2: Optional[float] = Field(
        None,
        description="Gesamter Lüftungsquerschnitt aller Luken in mm²"
    )
    ventilation_sufficient: Optional[bool] = Field(
        None,
        description="Belüftung ausreichend nach ISO 9097"
    )
    ventilation_findings: List[str] = Field(
        default_factory=list,
        description="Befunde zur Belüftung"
    )

    # Systemzustand
    overall_system_score: Optional[int] = Field(
        None,
        description="Gesamtscore Lukensystem 0-100"
    )
    weakest_hatch_id: Optional[str] = Field(
        None,
        description="ID der Luke mit dem niedrigsten Score"
    )
    total_estimated_repair_cost_eur: Optional[float] = Field(
        None,
        description="Gesamtkosten für alle empfohlenen Reparaturen in EUR"
    )
    priority_actions: List[str] = Field(
        default_factory=list,
        description="Priorisierte Maßnahmen über alle Luken"
    )

    # Meta
    confidence: str = Field(
        "estimated",
        description="Gesamt-Confidence-Level"
    )
    assessment_date: Optional[str] = Field(
        None,
        description="Datum der Bewertung (ISO 8601)"
    )
```

---

## 7. Grundlagen

### 7.1 Lukentypen — Systematik

#### 7.1.1 Öffnungsluken (Opening Hatches)

Die häufigste Bauform. Ein transparenter oder opaker Deckel ist über Scharniere am Rahmen befestigt und öffnet sich nach vorne, hinten oder zur Seite. Gasdruckfedern oder Reibungsgelenke halten den Deckel in geöffneter Position.

**Varianten nach Öffnungsrichtung:**

| Öffnungsrichtung | Bezeichnung | Vorteile | Nachteile | Typischer Einsatz |
|-------------------|------------|----------|-----------|-------------------|
| Nach vorne (bugwärts) | Hinged forward | Fängt Fahrtwind, maximale Ventilation bei Fahrt | Grünwasser-Risiko wenn offen, kann bei Seegang zuschlagen | Vorschiff, Salon |
| Nach achtern | Hinged aft | Kein Grünwasser-Fang, sicherer bei Seegang | Weniger Ventilation bei Fahrt | Achterdeck, Salon achtern |
| Zur Seite | Hinged side | Kompromiss Ventilation/Sicherheit | Asymmetrische Windbelastung | Salonluken, Gangbord |
| Beidseitig (Butterfly) | Butterfly / bi-fold | Maximale Öffnung, symmetrisch | Komplexe Mechanik, teuer, mehr Wartung | Salon Zentral, Luxusyachten |

**Öffnungswinkel nach Kategorie:**

| Profiltyp | Typischer max. Öffnungswinkel | Effektiver Lüftungsquerschnitt |
|-----------|-------------------------------|-------------------------------|
| Ocean | 55–70° | 70–85 % der Lukenöffnung |
| Medium Profile | 55–70° | 70–85 % |
| Low Profile | 50–65° | 60–80 % |
| Flush | 45–60° | 50–70 % |

#### 7.1.2 Flush-Luken (Bündige Luken)

Flush-Luken schließen bündig mit der Decksoberfläche ab (Profilhöhe 0–5 mm über Deck). Sie bieten:

**Vorteile:**
- Keine Stolperkante auf dem Arbeitsdeck
- Ästhetisch ansprechend (cleanes Decksbild)
- Kein Widerstand für überlaufendes Wasser
- Geringere Windbelastung
- Schoten und Leinen fangen nicht an erhabenen Rahmen

**Nachteile:**
- Geringerer Schutz gegen Grünwasser (kein Süll)
- Höhere Anforderungen an Dichtung (Wasser steht direkt auf Luke)
- Aufwändiger Einbau (Deck muss exakt planiert werden)
- Schwächere Deckstruktur bei großen Öffnungen
- Teurer als erhabene Luken (30–50 % Aufpreis)

**Typische Flush-Hersteller:**
- Lewmar Flush Serie (Art.-Nr. 396xxxxx)
- Moonlight (Italien) — Spezialist für Flush-Luken
- Freeman Marine — Custom Flush für Superyachten
- Rutgerson — Premium Flush für Performance-Segler

#### 7.1.3 Schiebeluken (Sliding Hatches)

Schiebeluken verschieben den Deckel horizontal über Schienen. Im Yachtbau primär als Niedergangsluke (Companionway Hatch) verwendet, selten als Decksluke.

**Einsatz als Decksluke:**
- Salonbereich auf Motoryachten (Schiebedach-Effekt)
- Große Öffnungen auf Superyachten (elektrisch angetrieben)
- Steuerstand-Luken auf Flybridge

**Besonderheiten:**
- Brauchen Schienensystem auf dem Deck
- Entwässerung der Schienen kritisch
- Dichtung: Bürsten- oder Lippendichtung (nicht Kompressionsdichtung)
- Schienenmaterial: Edelstahl 316L oder HDPE-Gleitschienen

#### 7.1.4 Butterfly-Luken (Schmetterlingsluken)

Zwei Deckelhälften öffnen sich symmetrisch nach beide Seiten. Jede Hälfte ist an der Längsachse des Bootes scharniergiert.

**Einsatz:**
- Große Salonluken (>700 mm) auf Premium-Yachten
- Maximale Öffnung und Ventilation
- Eindrucksvolle Ästhetik (offener Salon-Effekt)

**Hersteller:**
- Lewmar (Sonder-Konfiguration auf Basis Ocean/Medium Profile)
- Freeman Marine (Custom Butterfly für Superyachten)
- Goiot (Sonderfertigung)

**Preis:** 2–3× Einzelluke gleicher Größe wegen doppelter Scharnier- und Gasdruckfeder-Mechanik.

#### 7.1.5 Fluchtluken (Escape Hatches)

**Normative Anforderungen (ISO 12216 + RCD):**

- **Mindest-Lichte-Weite:** 400 mm × 520 mm ODER Durchmesser 450 mm
- **Zugang von innen:** Ohne Werkzeug, ohne Schlüssel, mit einer Hand bedienbar
- **Zugang von außen:** Muss auch von außen geöffnet werden können (Rettung)
- **Beschriftung:** Innen und außen als Notausstieg gekennzeichnet ("EMERGENCY EXIT" / "NOTAUSSTIEG")
- **Keine Blockade:** Der Zugangsweg zur Fluchtluke darf nicht durch Möbel, Polster oder Stauung blockiert werden

**Wo Fluchtluken erforderlich sind:**
- Jede Kabine mit nur einem Ausgang (Vorkabine, Achterkabine)
- Salons, die bei geschlossenem Niedergang keinen zweiten Ausgang haben
- Maschinenräume (Flucht bei Brand)

**Dedizierte Fluchtluken-Hersteller:**
- **Houdini (UK):** Spezialist für Escape Hatches. Modell "Ocean" (500 × 500 mm lichte Weite, 670 × 670 mm Außenmaß). CE Kat. A zugelassen. Preis ca. 450–650 EUR. Art.-Nr. HO500-500.
- **Lewmar:** Mehrere Größen als Fluchtluke einsetzbar (Size 50 und größer erfüllen Mindestmaß)
- **Goiot:** Modell Opal T50 und T60 erfüllen Fluchtluken-Anforderung

**Hinweis:** AYDI-Analyse prüft automatisch, ob jede Schlafkabine eine normkonforme Fluchtluke hat (Pipeline A, Modul Compliance).

#### 7.1.6 Zugangsluken (Access Hatches)

Nicht-transparente Luken für den Zugang zu:
- Lazarette (Stauräume achtern)
- Ankerkästen
- Technischen Räumen (Tanks, Pumpen, Elektrik)
- Bodenluken (Bilgenzugang)

**Besonderheiten:**
- Oft massiver Deckel (Aluminium, GFK, Teak)
- Keine Transparenz erforderlich
- Müssen teilweise begehbar sein (Anti-Skid)
- Einfachere Dichtungsanforderungen (oft nur spritzwasserdicht)
- Verriegelung: Flush-Ring-Griffe, um Stolpergefahr zu minimieren

**Typische Produkte:**
- Lewmar Flush Inspection Hatch (Art.-Nr. 39xxxx30): rund, Ø 200–350 mm, ABS oder Aluminium, ab 35 EUR
- Vetus Inspektionsluke DLUX (Art.-Nr. DLUX xxxx): weiß oder schwarz, Ø 170–420 mm, ab 25 EUR
- Beckson Screw-Out Deck Plate (Art.-Nr. DP-xxx): rund, Ø 100–300 mm, ab 15 EUR (Budget)

### 7.2 Profilhöhen — Ocean, Medium, Low, Flush

Die Profilhöhe einer Luke definiert, wie weit der Rahmen über die Decksoberfläche ragt. Dies beeinflusst Wasserdichtheit, Stolpergefahr und Ästhetik.

#### 7.2.1 Ocean-Profil (60–80 mm über Deck)

**Charakteristik:**
- Höchster Süll, maximaler Grünwasser-Schutz
- Robusteste Konstruktion (dickster Rahmenquerschnitt)
- Scharniere, Verschlüsse und Gasdruckfedern außen sichtbar
- CE Kat. A zugelassen für Position 1
- Höchstes Gewicht (typisch 6–12 kg für 500×500 mm Luke)

**Zielgruppe:** Blauwasser-Segler, Kat. A/B Yachten, Vorschiff-Luken.

**Lewmar Ocean Serie — Programmübersicht:**

| Lewmar Size | Außenmaß (mm) | Ausschnitt (mm) | Lichte Weite (mm) | Gewicht (kg) | Preis EUR (2025) | Art.-Nr. (klar) |
|-------------|---------------|------------------|--------------------|-------------|-----------------|-----------------|
| Size 00 | 278 × 278 | 213 × 213 | 185 × 185 | 1,8 | 280–320 | 39930070 |
| Size 10 | 360 × 360 | 289 × 289 | 258 × 258 | 2,7 | 340–390 | 39940070 |
| Size 20 | 437 × 437 | 363 × 363 | 332 × 332 | 3,6 | 410–470 | 39950070 |
| Size 30 | 510 × 510 | 433 × 433 | 400 × 400 | 4,5 | 480–540 | 39960070 |
| Size 40 | 588 × 588 | 510 × 510 | 477 × 477 | 5,8 | 560–640 | 39970070 |
| Size 50 | 665 × 665 | 584 × 584 | 550 × 550 | 7,2 | 680–780 | 39980070 |
| Size 60 | 748 × 748 | 664 × 664 | 628 × 628 | 9,1 | 820–940 | 39990070 |
| Size 70 | 830 × 830 | 743 × 743 | 705 × 705 | 11,4 | 980–1.120 | 39900070 |

**Hinweis:** Size 30 erfüllt mit 400 mm lichter Weite gerade die ISO 12216 Fluchtluken-Anforderung in einer Richtung. Für vollständige Compliance als Fluchtluke (400 × 520 mm) ist eine rechteckige Konfiguration nötig. Lewmar bietet Ocean-Luken auch in rechteckig an (z.B. Size 30LR: 510 × 680 mm).

#### 7.2.2 Medium-Profil (35–55 mm über Deck)

**Charakteristik:**
- Kompromiss zwischen Wasserschutz und Ästhetik
- Scharniere teils verdeckt, kompakterer Rahmenquerschnitt
- CE Kat. A/B zugelassen (modellabhängig), Position 1 bei einigen Herstellern
- Mittleres Gewicht (typisch 4–8 kg für 500×500 mm)

**Zielgruppe:** Fahrtensegler Kat. B/C, Motoryachten, Salonluken.

**Lewmar Medium Profile Serie:**

| Lewmar Size | Außenmaß (mm) | Ausschnitt (mm) | Gewicht (kg) | Preis EUR (2025) | Art.-Nr. (klar) |
|-------------|---------------|-----------------|-------------|-----------------|-----------------|
| Size 10 | 350 × 350 | 279 × 279 | 2,1 | 290–340 | 39610070 |
| Size 20 | 424 × 424 | 350 × 350 | 2,8 | 360–420 | 39620070 |
| Size 30 | 497 × 497 | 420 × 420 | 3,6 | 430–500 | 39630070 |
| Size 40 | 575 × 575 | 497 × 497 | 4,7 | 510–590 | 39640070 |
| Size 50 | 652 × 652 | 571 × 571 | 5,8 | 620–720 | 39650070 |
| Size 60 | 734 × 734 | 650 × 650 | 7,4 | 760–880 | 39660070 |

#### 7.2.3 Low-Profil (15–35 mm über Deck)

**Charakteristik:**
- Niedrige Silhouette, Scharniere und Mechanik weitgehend verdeckt
- Wenig Grünwasser-Schutz (nur geringer Süll)
- CE Kat. B/C zugelassen, Position 2/3
- Geringes Gewicht (typisch 3–6 kg für 500×500 mm)
- Eleganteres Erscheinungsbild

**Zielgruppe:** Motoryachten, Küstensegler, Aufbau-Luken.

**Lewmar Low Profile Serie:**

| Lewmar Size | Außenmaß (mm) | Ausschnitt (mm) | Gewicht (kg) | Preis EUR (2025) | Art.-Nr. (klar) |
|-------------|---------------|-----------------|-------------|-----------------|-----------------|
| Size 20 | 419 × 419 | 350 × 350 | 2,2 | 320–380 | 39520070 |
| Size 30 | 493 × 493 | 420 × 420 | 2,9 | 390–450 | 39530070 |
| Size 40 | 570 × 570 | 497 × 497 | 3,8 | 470–540 | 39540070 |
| Size 50 | 647 × 647 | 571 × 571 | 4,7 | 560–650 | 39550070 |
| Size 60 | 730 × 730 | 650 × 650 | 6,0 | 700–810 | 39560070 |

#### 7.2.4 Flush-Profil (0–5 mm über Deck)

**Charakteristik:**
- Bündig mit Deck, keine Stolperkante
- Komplette Mechanik unter Deck
- Höchste Anforderungen an Decksvorbereitung und Einbau
- CE Kat. C/D (Position 2/3), bei Spezialanfertigung auch B
- Leichteste Bauform (Rahmen minimal)
- Höchster Preis pro Quadratmeter Öffnung

**Lewmar Flush Serie:**

| Lewmar Size | Außenmaß (mm) | Ausschnitt (mm) | Gewicht (kg) | Preis EUR (2025) | Art.-Nr. (klar) |
|-------------|---------------|-----------------|-------------|-----------------|-----------------|
| Size 20 | 422 × 422 | 350 × 350 | 2,4 | 480–560 | 39720070 |
| Size 30 | 496 × 496 | 420 × 420 | 3,2 | 570–660 | 39730070 |
| Size 40 | 573 × 573 | 497 × 497 | 4,1 | 680–790 | 39740070 |
| Size 50 | 650 × 650 | 571 × 571 | 5,2 | 810–940 | 39750070 |

### 7.3 Materialien — Rahmen

#### 7.3.1 Aluminium (eloxiert) — Standardmaterial

**Legierungen im Einsatz:**

| Legierung | EN-Bezeichnung | UNS | Streckgrenze (MPa) | Korrosionsbest. | Einsatz |
|-----------|---------------|-----|--------------------|-----------------|---------| 
| 6060-T5 | EN AW-6060-T5 | A96060 | 120 | Gut | Standard-Lukenrahmen (Lewmar, Goiot) |
| 6061-T6 | EN AW-6061-T6 | A96061 | 240 | Gut | Hochbelastete Rahmen, Superyacht |
| 6082-T6 | EN AW-6082-T6 | A96082 | 260 | Gut | Strukturelle Rahmenteile |
| 5083-H111 | EN AW-5083-H111 | A95083 | 115 | Sehr gut | Seewasserbeständige Teile |

**Eloxierung (Anodisierung):**
- **Standard-Eloxierung:** 10–15 µm Schichtdicke. Ausreichend für Küstengewässer. Lewmar Standard.
- **Hart-Eloxierung:** 20–50 µm Schichtdicke. Für Tropen und Hochsee. Aufpreis ca. 20–30 %.
- **Farb-Eloxierung:** Schwarz oder Bronze. Ästhetisch. Lewmar "Black" Variante (Aufpreis 15 %).

**Lebensdauer Aluminium-Rahmen:**
- Süßwasser / Binnenrevier: 25–40 Jahre
- Küste, gemäßigt: 20–30 Jahre
- Salzwasser, Tropen: 15–25 Jahre (abhängig von Eloxierung und Pflege)

**Häufigste Korrosionsprobleme:**
1. **Kontaktkorrosion (galvanisch):** Aluminium in Kontakt mit Edelstahl-Schrauben ohne Isolierung → weißer Belag, Lochfraß. Lösung: Isolierscheiben (Nylon), Duralac-Paste.
2. **Spaltkorrosion:** An Rahmen-Deck-Übergang, wo Salzwasser unter den Flansch kriecht. Lösung: Dauerelastische Dichtmasse (Sikaflex 291i, 3M 4200).
3. **Lochfraß (Pitting):** In stehender Salzlake (nicht gespülte Luken). Lösung: Nach jedem Segeln Süßwasser spülen.

#### 7.3.2 Edelstahl 316L

**Spezifikation:**
- Werkstoff-Nr. 1.4404 / AISI 316L
- Streckgrenze: 170 MPa (geglüht), bis 690 MPa (kaltverformt)
- Korrosionsbeständigkeit: Sehr gut in Salzwasser
- Dichte: 8,0 g/cm³ (vs. Aluminium 2,7 g/cm³ → 3× schwerer!)

**Einsatz bei Luken:**
- Superyachten (>24 m): Edelstahl-Rahmen für Ästhetik und Langlebigkeit
- Verschlüsse und Scharniere: Häufig Edelstahl auch bei Aluminium-Rahmen
- Sicherheitskritische Anwendungen: Fluchtluken auf Passagieryachten

**WARNUNG:** Edelstahl 304 (1.4301) ist NICHT ausreichend für dauerhafte Salzwasserexposition. Es MUSS 316L (1.4404) oder besser Duplex 2205 (1.4462) sein. Tea-Staining (braune Flecken) bei 304 ist ein kosmetisches Problem, Lochfraß (pitting) ein strukturelles.

**Preis:** Lukenrahmen in Edelstahl 316L: ca. 3–5× Aluminiumpreis. Eine 500 × 500 mm Luke: ca. 1.500–3.000 EUR (vs. 400–600 EUR in Aluminium).

#### 7.3.3 Composite (GFK / CFK)

**GFK-Rahmen (Glasfaserverstärkter Kunststoff):**
- Leicht (Dichte ca. 1,8 g/cm³)
- Korrosionsfrei
- Geringere Festigkeit als Aluminium → dickerer Rahmenquerschnitt nötig
- Schwierig zu reparieren bei Beschädigung
- UV-empfindlich (Gelcoat-Schutz erforderlich)

**CFK-Rahmen (Kohlefaserverstärkter Kunststoff):**
- Leichteste Option (Dichte ca. 1,5 g/cm³)
- Höchste spezifische Festigkeit
- Nur im Racing-Segment (Vendée Globe, Volvo Ocean Race)
- Preis: 5–10× Aluminium
- Empfindlich gegen Schlagbelastung (Delamination)

**Hersteller von Composite-Lukenrahmen:**
- Lewmar: GFK-Flansch bei einigen Modellen (nicht für den Rahmen selbst)
- Rutgerson: Carbon-Option für Racing-Luken
- Custom-Fertigung: Diverse Composite-Werften

#### 7.3.4 Bronze

**Einsatz:** Ausschließlich bei klassischen Yachten und Repliken. Optisch ansprechend, ausgezeichnete Korrosionsbeständigkeit.

- **Material:** Aluminiumbronze (CuAl10Ni5Fe4) oder Manganbronze
- **Oberfläche:** Poliert (regelmäßige Pflege nötig) oder patiniert
- **Preis:** 4–8× Aluminium
- **Hersteller:** New Found Metals (USA), Davey & Company (UK) — historische Repliken
- **Gewicht:** Ca. 3× Aluminium (Dichte 8,8 g/cm³)

### 7.4 Materialien — Linse (Lukendeckel)

#### 7.4.1 Acrylglas (PMMA — Polymethylmethacrylat)

**DER Standard** für Lukendeckel im Yachtbau. Wird von allen großen Herstellern als Standardlinse verwendet.

**Eigenschaften:**

| Parameter | Wert | Relevanz |
|-----------|------|----------|
| Lichtdurchlässigkeit | 92 % (klar) | Höchste aller Kunststoffe |
| Dichte | 1,19 g/cm³ | Leicht |
| Biegefestigkeit | 105–120 MPa | Ausreichend für Lukengrößen bis ca. 800 mm |
| Schlagfestigkeit | 10–15 kJ/m² (ungek.) | NIEDRIG — Bruchgefahr bei Punktbelastung |
| E-Modul | 3.000–3.300 MPa | Steif |
| Wärmeformbeständigkeit | 95–105 °C (HDT-B) | Ausreichend |
| UV-Beständigkeit | Gut (eigenständig UV-stabil) | Vergilbt kaum, aber Crazing nach 10–20 Jahren |
| Kratzfestigkeit | Gering (Mohs 3) | Muss regelmäßig poliert werden |
| Chemische Beständigkeit | Empfindlich gegen Lösemittel, Aceton | NIEMALS Lösemittel für Reinigung verwenden! |

**Handelsbezeichnungen:**
- Plexiglas (Evonik, DE)
- Perspex (Lucite, UK)
- Altuglas (Arkema, FR)
- Acrylite (Röhm, DE/US)

**Typische Dicken in Luken:**

| Lukengröße (Diagonale) | Min. Dicke ISO 12216 | Empfehlung AYDI |
|------------------------|---------------------|-----------------|
| ≤400 mm | 8 mm | 8–10 mm |
| 400–600 mm | 10 mm | 10–12 mm |
| 600–800 mm | 12 mm | 12–15 mm |
| >800 mm | 15 mm | 15–20 mm oder Sicherheitsglas |

**UV-Degradation und Crazing:**

Acrylglas ist intrinsisch UV-stabil (absorbiert UV-A/B), entwickelt aber nach 10–20 Jahren im Außeneinsatz **Crazing** (feine Haarrisse an der Oberfläche). Ursachen:
1. UV-induzierter Polymerabbau an der Oberfläche
2. Thermische Spannungen (Tag/Nacht-Zyklen, insbesondere in Tropen)
3. Chemischer Angriff (Lösemittel, Reiniger)
4. Mechanische Spannung durch zu strammen Rahmeneinbau

**Behandlung von Crazing:**
- **Leichtes Crazing (Tiefe <0,1 mm):** Polieren mit Acrylpolitur (Novus Plastic Polish #2, ca. 12 EUR/237 ml)
- **Mittleres Crazing (Tiefe 0,1–0,5 mm):** Nassschliff (Körnung 800→1200→2000→3000) + Polieren
- **Tiefes Crazing (>0,5 mm):** Linse tauschen. Nicht reparierbar.

**Ersatzlinsen-Preise (Zuschnitt, klar, 10 mm):**

| Größe | Preis Acrylglas-Zuschnitt | Preis Lewmar OEM-Linse |
|-------|--------------------------|----------------------|
| 300 × 300 mm | 25–40 EUR | 80–120 EUR |
| 400 × 400 mm | 40–60 EUR | 120–180 EUR |
| 500 × 500 mm | 60–90 EUR | 180–260 EUR |
| 600 × 600 mm | 90–130 EUR | 260–380 EUR |

**Hinweis:** OEM-Linsen sind exakt geformt (Wölbung, Randprofil) und garantiert passend. Zuschnitt-Acrylglas ist plan und muss eventuell angepasst werden.

#### 7.4.2 Polycarbonat (PC — Lexan / Makrolon)

**Alternative zu Acrylglas** mit deutlich höherer Schlagfestigkeit, aber schlechterer UV-Beständigkeit.

**Eigenschaften:**

| Parameter | Wert | Vergleich zu PMMA |
|-----------|------|-------------------|
| Lichtdurchlässigkeit | 88 % (klar) | Etwas geringer |
| Dichte | 1,20 g/cm³ | Gleichwertig |
| Biegefestigkeit | 90–100 MPa | Etwas geringer |
| Schlagfestigkeit | 60–80 kJ/m² (ungek.) | 4–6× HÖHER |
| E-Modul | 2.300–2.400 MPa | Etwas flexibler |
| UV-Beständigkeit | SCHLECHT (ohne Beschichtung) | Deutlich schlechter |
| Kratzfestigkeit | Gering (Mohs 2–3) | Gleichwertig bis schlechter |
| Vergilbung | Nach 3–5 Jahren ohne UV-Schutz | Deutlich schneller |

**Handelsbezeichnungen:**
- Lexan (SABIC)
- Makrolon (Covestro, DE)
- Palsun (Palram)

**Einsatz bei Luken:**
- **Blauwasser / Tropen:** Bevorzugt wegen Schlagfestigkeit (Debris bei Sturm, Hagelschlag)
- **Racing:** Leichter und bruchsicherer als Acrylglas gleicher Dicke
- **Charter:** Vandalismus-Schutz (kaum brechbar)

**UV-Schutz zwingend erforderlich:**
- Werksseitige UV-Beschichtung (Co-Extrusion oder Hardbeschichtung): hält 10–15 Jahre
- Nachträgliche UV-Schutzfolie (3M, Llumar): hält 5–7 Jahre, austauschbar
- OHNE UV-Schutz: Vergilbung und Spröd-Werden nach 3–5 Jahren

**Typische Dicken:** 6–10 mm (dünner als Acrylglas möglich wegen höherer Schlagfestigkeit).

#### 7.4.3 Einscheiben-Sicherheitsglas (ESG / Tempered Glass)

**Einsatz:** Premium-Motoryachten und Superyachten. Optisch überlegen (keine Kunststoff-Trübung), kratzsicher, UV-stabil.

**Eigenschaften:**
- Lichtdurchlässigkeit: 90 %
- Biegefestigkeit: 120–200 MPa (thermisch vorgespannt)
- Schlagfestigkeit: Mittel (bricht in kleine, stumpfe Würfel)
- UV-Beständigkeit: Dauerhaft (Glas altert nicht UV-bedingt)
- Gewicht: ca. 2,5× schwerer als Acrylglas gleicher Dicke (Dichte 2,5 g/cm³)
- Preis: 2–4× Acrylglas

**Typische Dicken:** 8–12 mm (ESG). Lukendeckel aus ESG MÜSSEN werkseitig auf Maß gefertigt werden (kein nachträglicher Zuschnitt möglich).

**Hersteller von ESG-Lukenlinsen:**
- AGC Marine (BE)
- Pilkington (UK)
- Saint-Gobain Marine (FR)

#### 7.4.4 Verbundsicherheitsglas (VSG / Laminated Safety Glass)

**Einsatz:** Superyachten, wo Splitterschutz UND optische Qualität gefordert sind.

- Aufbau: 2 Schichten Glas mit PVB- oder EVA-Folie dazwischen
- Bei Bruch: Splitter bleiben an der Folie haften
- Schalldämmend (3–5 dB besser als ESG)
- UV-Filter integrierbar (in der PVB-Folie)
- Preis: 4–8× Acrylglas
- Gewicht: 3× Acrylglas

**Typische Dicken:** 2 × 4 mm + 0,76 mm PVB = 8,76 mm Gesamt. Oder 2 × 5 mm + 1,52 mm PVB = 11,52 mm.

#### 7.4.5 Vergleichsmatrix — Linsenmaterialien

| Eigenschaft | PMMA (Acryl) | PC (Lexan) | ESG | VSG |
|-------------|-------------|------------|-----|-----|
| Lichtdurchlässigkeit | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| Schlagfestigkeit | ★★ | ★★★★★ | ★★★ | ★★★★ |
| UV-Beständigkeit | ★★★★ | ★★ | ★★★★★ | ★★★★★ |
| Kratzfestigkeit | ★★ | ★★ | ★★★★★ | ★★★★★ |
| Gewicht | ★★★★★ | ★★★★★ | ★★★ | ★★ |
| Preis | ★★★★★ | ★★★★ | ★★★ | ★★ |
| Reparierbarkeit | ★★★★ | ★★★ | ★ | ★ |
| Einsatz bis Lukengröße | 800 mm | 1.000 mm | 1.200 mm | 1.500 mm |

### 7.5 Dichtungen (Seals)

#### 7.5.1 EPDM-Kompressionsdichtung — Standard

**EPDM (Ethylen-Propylen-Dien-Monomer)** ist das Standardmaterial für Lukendichtungen im Yachtbau.

**Eigenschaften:**
- Temperaturbereich: -40 °C bis +120 °C
- Shore-Härte: 50–70 A (typisch 60 A für Luken)
- Druckverformungsrest: 15–25 % (24 h bei 70 °C) — GUT
- UV-Beständigkeit: Gut (mit Carbon-Black-Füller: sehr gut)
- Ozon-Beständigkeit: Sehr gut
- Salzwasser-Beständigkeit: Sehr gut
- Lebensdauer (gemäßigtes Klima): 8–15 Jahre
- Lebensdauer (Tropen): 5–8 Jahre

**Profilformen für Luken:**

| Profilform | Querschnitt | Einsatz | Kompressionsweg |
|------------|-------------|---------|-----------------|
| D-Profil | Halbrund, massiv | Standard bei Lewmar, Bomar | 20–35 % der Höhe |
| Hohlprofil | Rohrförmig (hohl) | Goiot, große Luken | 30–50 % der Höhe |
| P-Profil | D mit Fuß-Lippe | Selbstklebend, Retrofit | 20–30 % der Höhe |
| Keilprofil (Wedge) | Dreieckig | Spezial-Anwendungen | 15–25 % der Höhe |
| Lippenprofil | Flach mit Lippe | Schiebeluken, Zugangsluken | Lippenbiegung |
| U-Kanal | U-Form, klemmt auf Kante | Houdini Escape Hatches | 20–30 % der Höhe |

**Typische EPDM-Dichtungsmaße für gängige Luken:**

| Lukenhersteller | Serie | Dichtungsmaß (B × H mm) | Nutmaß (B × T mm) | Houdini-Ref. |
|-----------------|-------|--------------------------|--------------------|-----------| 
| Lewmar | Standard/Classic | 8 × 6 D-Profil | 6,0 × 4,0 | 2120 |
| Lewmar | Ocean | 10 × 8 Hohlprofil | 6,5 × 5,0 | 2300 |
| Lewmar | Low Profile | 8 × 6 D-Profil | 6,0 × 4,0 | 2120 |
| Lewmar | Medium Profile | 10 × 7 D-Profil | 6,5 × 4,5 | 2280 |
| Goiot | Cristal | 10 × 7 speziell | 5,5 × 4,5 | 2260 |
| Goiot | Opal | 12 × 8 Hohlprofil | 7,0 × 5,0 | 2340 |
| Bomar | Standard | 9 × 7 D-Profil | 6,0 × 4,5 | 2180 |
| Houdini | Ocean | 10 × 8 U-Kanal | — | — |
| Vetus | Libero | 8 × 6 D-Profil | 5,5 × 4,0 | 2120 |
| Rutgerson | Premium | 10 × 8 D-Profil | 6,5 × 5,0 | 2300 |

#### 7.5.2 Silikon-Kompressionsdichtung

**Silikon (VMQ — Vinyl-Methyl-Polysiloxan)** als Premium-Alternative zu EPDM.

**Eigenschaften:**
- Temperaturbereich: -60 °C bis +200 °C
- Shore-Härte: 40–60 A (typisch 50 A, weicher als EPDM)
- Druckverformungsrest: 10–15 % — BESSER als EPDM
- UV-Beständigkeit: Ausgezeichnet (kein Carbon-Black nötig)
- Farbe: Transluzent oder weiß (auch farbig möglich)
- Lebensdauer: 15–25 Jahre (gemäßigt), 10–15 Jahre (Tropen)
- Preis: 2–3× EPDM

**Nachteile gegenüber EPDM:**
- Geringere Reißfestigkeit (leichter beschädigt bei scharfen Kanten)
- Höherer Preis
- Nicht alle Hersteller bieten Silikon-Version an

**Verfügbarkeit Silikon-Dichtungen:**
- Houdini: Silikon-Version für alle Profile (3xxx-Serie statt 2xxx)
- Lewmar: Nicht ab Werk, nur Aftermarket (Houdini)
- Goiot: Nicht ab Werk
- Rutgerson: Silikon-Option ab Werk (Aufpreis 80–120 EUR pro Luke)

#### 7.5.3 Aufblasbare Dichtungen (Inflatable Seals)

**Exklusiv im Superyacht-Segment.** Pneumatisch aufblasbare Dichtungen, die erst beim Schließen der Luke aktiviert werden.

**Prinzip:**
1. Luke wird geschlossen
2. Pneumatikpumpe (12 V oder 24 V) bläst Dichtung auf (0,3–0,8 bar)
3. Dichtung presst sich gleichmäßig an Lukendeckel
4. Zum Öffnen: Druck ablassen (automatisch bei Entriegelung)

**Vorteile:**
- Perfekte, gleichmäßige Anpressung auf gesamtem Umfang
- Kein Druckverformungsrest (Dichtung entspannt sich vollständig)
- Kompensiert Rahmenverformungen und Toleranzen
- Lebensdauer: 15–25 Jahre

**Nachteile:**
- Extrem teuer (500–2.000 EUR pro Luken-Dichtungssatz)
- Erfordert pneumatisches System an Bord
- Komplexität (Pumpe, Ventile, Leitungen)
- Nur bei großen Luken (>600 mm) sinnvoll

**Hersteller:**
- Seal Master (UK): Marktführer für marine Inflatable Seals
- Trelleborg Sealing Solutions (SE): Industrieprodukt, adaptiert für Marine
- Freeman Marine: Eigene inflatable Seals für ihre Luken

#### 7.5.4 Dichtungswechsel — Intervalle und Kosten

| Material | Revier | Intervall (Jahre) | Material-Kosten (500 mm Luke) | Arbeitszeit |
|----------|--------|-------------------|-------------------------------|-------------|
| EPDM | Gemäßigt (Ostsee/Nordsee) | 8–12 | 15–30 EUR | 30 min DIY |
| EPDM | Mittelmeer | 5–8 | 15–30 EUR | 30 min DIY |
| EPDM | Tropen | 3–5 | 15–30 EUR | 30 min DIY |
| Silikon | Gemäßigt | 12–20 | 35–70 EUR | 30 min DIY |
| Silikon | Mittelmeer | 8–12 | 35–70 EUR | 30 min DIY |
| Silikon | Tropen | 6–10 | 35–70 EUR | 30 min DIY |
| Inflatable | Alle | 15–25 | 500–2.000 EUR | 2–4 h Fachmann |

### 7.6 CE-Kategorie-Anforderungen an Luken

#### 7.6.1 Zusammenfassung nach Kategorie

**Kategorie A — Hochsee (Wind >8 Bft, Wellen >4 m):**
- Alle Luken: Wasserdicht nach ISO 12216 Flood Test
- Vorschiff-Luken: Ocean-Profil empfohlen (hoher Süll)
- Fluchtluken: Mindestens 2 pro Wohnbereich, Schnellverschluss
- Sturmdeckel (Deadlights): Empfohlen für alle transparenten Luken in Position 1
- Verriegelung: Mindestens 2-Punkt-Verriegelung für Position-1-Luken
- Scharniere: Min. 10.000 Zyklen Ermüdungsfestigkeit (ISO 12216:2020)

**Kategorie B — Offshore (Wind ≤8 Bft, Wellen ≤4 m):**
- Alle Luken: Wasserdicht nach ISO 12216 Spray Test
- Vorschiff-Luken: Ocean- oder Medium-Profil
- Fluchtluken: Mindestens 1 pro abgeschlossener Kabine
- Verriegelung: 2-Punkt-Verriegelung für Position-1-Luken
- Scharniere: Min. 5.000 Zyklen

**Kategorie C — Küstennah (Wind ≤6 Bft, Wellen ≤2 m):**
- Alle Luken: Spritzwasserdicht nach ISO 12216 Spray Test
- Lukentyp: Beliebig (Low Profile, Flush erlaubt)
- Fluchtluken: Empfohlen
- Verriegelung: 1-Punkt-Verriegelung ausreichend

**Kategorie D — Geschützt (Wind ≤4 Bft, Wellen ≤0,3 m):**
- Luken: Spritzwasserdicht
- Lukentyp: Beliebig
- Fluchtluken: Empfohlen, nicht zwingend
- Verriegelung: Einfacher Verschluss ausreichend

### 7.7 Deckausschnitt-Verstärkung (Deck Cutout Reinforcement)

#### 7.7.1 Problematik

Jeder Deckausschnitt für eine Luke schwächt die Deckstruktur. Die Spannungskonzentration an den Ecken des Ausschnitts kann das 2–3-fache der normalen Decksspannung erreichen. Dies ist besonders kritisch bei:
- Großen Luken (>600 mm)
- Sandwich-Decks (GFK-Balsa/PVC-Schaum-GFK)
- Luken in strukturell beanspruchten Bereichen (Vorschiff, Mastfuß-Nähe)

#### 7.7.2 Verstärkungstechniken

**A) Massivlaminat-Ring:**
- Der Sandwich-Kern wird im Bereich des Ausschnitts + 50–100 mm ringsum durch massives GFK-Laminat ersetzt
- Typische Dicke: Gesamte Decksstärke als massives Laminat (z.B. 20 mm)
- IMMER erforderlich bei Sandwich-Decks

**B) Rahmenversteifung (Coaming):**
- Vertikales GFK- oder Aluminiumband um den Ausschnitt, verklebt/laminiert
- Höhe: 30–80 mm unter Deck
- Breite: 6–12 mm
- Schafft eine "Badewanne" um den Ausschnitt → leitet Kräfte um

**C) Eckradien:**
- NIEMALS scharfe Ecken beim Deckausschnitt!
- Mindestradius: 25 mm (Produktionsboote), 50 mm (empfohlen)
- Große Radien (75–100 mm) bei Luken >600 mm
- Stress-Konzentrationsfaktor bei R=25mm: ca. 2,5× ; bei R=50mm: ca. 1,8× ; bei R=100mm: ca. 1,3×

**D) Zusätzliche Lagen (Verstärkungslaminat):**
- 2–4 zusätzliche Lagen Glasgewebe (300–450 g/m²) um den Ausschnitt
- Überlappung: 100–150 mm über den Ausschnittrand hinaus
- Von unter Deck aufgebracht

#### 7.7.3 Spezifische Anforderungen nach Bootsgröße

| Bootslänge | Typische Decksstärke | Luken-Ausschnitt max. | Verstärkung |
|------------|---------------------|----------------------|-------------|
| 8–10 m | 12–18 mm (Sandwich) | 500 × 500 mm | Massivlaminat-Ring + 2 Zusatzlagen |
| 10–14 m | 15–25 mm (Sandwich) | 600 × 600 mm | Massivlaminat-Ring + Coaming + 3 Zusatzlagen |
| 14–18 m | 20–30 mm (Sandwich) | 700 × 700 mm | Massivlaminat-Ring + Coaming + 4 Zusatzlagen |
| 18–24 m | 25–40 mm (Sandwich) | 800 × 800 mm | Berechnung durch Strukturingenieur |
| >24 m | Nach Berechnung | Nach Berechnung | Klassifikationsgesellschaft (ABS/Lloyd's) |

#### 7.7.4 Retrofit-Einbau in Sandwich-Deck — Schritt für Schritt

Beim nachträglichen Einbau einer Luke in ein bestehendes Sandwich-Deck:

1. **Ausschnitt anzeichnen:** Luken-Cutout-Maß + Toleranz (±2 mm). Schablone vom Hersteller verwenden.
2. **Obere GFK-Haut schneiden:** Stichsäge mit Diamant-Klinge oder Oszillierwerkzeug. NIEMALS Flex!
3. **Kern entfernen:** 50–80 mm ringsum über den Ausschnitt hinaus. Vorsichtig mit Stechbeitel und Oszillierwerkzeug.
4. **Kern-Hohlraum füllen:** Mit Epoxid-Füllmasse (West System 105/205 + Glasmikrosphären) oder vorgefertigtem GFK-Massiv-Ring.
5. **Verstärkungslaminat:** 2–4 Lagen Glasgewebe unter Deck auflaminieren, Überlappung 100 mm.
6. **Coaming einbauen:** GFK- oder Alu-Ring unter Deck verkleben (Sikaflex 292i oder Epoxid).
7. **Lukenrahmen montieren:** Bohrlöcher auf Massivlaminat (NIE in den Sandwich-Kern!). Schrauben mit Dichtmasse (Sikaflex 291i, 3M 4200).
8. **Abdichten:** Rahmen-Flansch mit dauerelastischer Dichtmasse zum Deck.

**Typische Kosten Retrofit:**

| Arbeitsschritt | Material (EUR) | Arbeitszeit (Werft, 80 EUR/h) |
|---------------|---------------|-------------------------------|
| Ausschnitt + Kernentfernung | 20–50 | 2–3 h |
| Massivlaminat + Verstärkung | 80–150 | 3–5 h |
| Coaming | 50–100 | 1–2 h |
| Lukenmontage | — | 1–2 h |
| Dichtmasse + Befestigung | 30–60 | 1 h |
| **Gesamt (ohne Luke)** | **180–360 EUR** | **8–13 h = 640–1.040 EUR** |
| **Gesamt inkl. Lewmar Ocean Size 40** | **740–1.000 EUR** | **8–13 h** |

### 7.8 Mückenschutz und Sonnenschutz

#### 7.8.1 Mückenschutzgitter (Fly Screens)

**Typen:**

| Typ | Beschreibung | Vorteile | Nachteile | Preis (500 mm Luke) |
|-----|-------------|----------|-----------|---------------------|
| Fest-Rahmen (Clip-in) | Aluminium-Rahmen mit Gaze, clipt in Lukenrahmen | Stabil, gut abdichtend | Schwer zu verstauen | 60–120 EUR |
| Magnet-Rahmen | Magnetstreifen hält Gaze am Lukenrahmen | Schnell ein/aushängbar | Magnete können korrodieren | 40–80 EUR |
| Roll-Screen (Rollo) | Aufrrollbares Gaze-Rollo unter Lukenrahmen | Platzsparend, permanent montiert | Mechanik kann klemmen | 80–150 EUR |
| Klett-Gaze | Gaze mit Klettband am Rahmen befestigt | Billig, einfach | Klett löst sich nach 1–2 Jahren | 15–30 EUR |

**Gaze-Materialien:**

| Material | Maschenweite | Gegen | Luftdurchlass-Reduktion |
|----------|-------------|-------|------------------------|
| Fiberglas-Gaze | 1,2–1,4 mm | Mücken, Fliegen | 30–40 % |
| Feinmaschig (No-See-Um) | 0,6–1,0 mm | Sand-Fliegen, No-See-Ums | 40–55 % |
| Edelstahl-Gaze (316L) | 1,0–1,2 mm | Mücken, Fliegen, Ratten | 25–35 % |
| Pollenschutz | 0,2–0,5 mm | Pollen, Feinstaub | 50–70 % |

**Hersteller-Lösungen:**
- **Lewmar:** Fly Screen für Ocean/Medium/Low Profile, Modell 361830xxx. Clip-in Aluminium-Rahmen. Preis 80–140 EUR je nach Größe.
- **Oceanair (UK):** SkyScreen-System. Roll-Gaze unter dem Lukenrahmen. Spur-geführt. Preis 100–200 EUR.
- **Goiot:** Integrierter Mückenschutz bei Opal-Serie (ab Werk). Abnehmbar.
- **Houdini:** Fly Screen separat erhältlich für alle Houdini-Luken. Preis 50–90 EUR.

#### 7.8.2 Verdunkelungs-Rollos und Plissees (Blinds / Shades)

**Typen:**

| Typ | Funktion | Verdunkelung | Preis (500 mm Luke) |
|-----|----------|-------------|---------------------|
| Pleated Blind (Plissee) | Lichtschutz, teilweise Verdunkelung | 60–80 % | 80–160 EUR |
| Blackout Blind (Rollo) | Vollverdunkelung | 95–100 % | 120–220 EUR |
| Combo Blind (Gaze + Plissee) | Mücken + Verdunkelung | Variabel | 140–250 EUR |

**Hersteller:**
- **Oceanair (UK):** Marktführer für marine Blinds. SkyShade-Serie. Verfügbar für Lewmar, Goiot, Bomar. Online-Konfigurator mit Lukenmaß-Eingabe.
- **Lewmar:** Integrierter Blind für Medium/Low/Flush Profile (ab Werk optional). Art.-Nr. 361840xxx.
- **Dometic (SE/US):** Seitz Oceanair Blinds (nach Übernahme von Oceanair). Premium-Qualität.
- **Goiot:** Integrierter Blind bei Harmonie-Serie.

### 7.9 Gasdruckfedern und Hatch Stays

#### 7.9.1 Gasdruckfedern (Gas Struts / Gas Springs)

**Funktion:** Halten die Luke in geöffneter Position und unterstützen beim Öffnen. Die häufigste Haltekraft-Komponente bei modernen Luken.

**Auslegung:**

Die richtige Gasdruckfeder-Kraft F (Newton) hängt ab von:
- Gewicht des Lukendeckels W (kg)
- Öffnungswinkel α
- Hebelarm L (mm) — Abstand Scharnier → Gasdruckfeder-Anlenkpunkt
- Anzahl der Gasdruckfedern (1 oder 2)

**Faustformel:** F = (W × 9,81 × L_deckel/2) / (L_hebel × cos(α/2) × n)

Wobei:
- W = Deckelgewicht in kg
- L_deckel = Abstand Scharnier → Schwerpunkt Deckel in mm
- L_hebel = Effektiver Hebelarm der Gasdruckfeder in mm
- α = Halber maximaler Öffnungswinkel
- n = Anzahl Gasdruckfedern

**Typische Gasdruckfeder-Kräfte:**

| Lukengröße | Deckelgewicht (ca.) | Gasdruckfeder Kraft | Menge | Lewmar Art.-Nr. |
|------------|--------------------|--------------------|-------|-----------------|
| 300 × 300 mm | 1,5–2,5 kg | 80–120 N | 1 | 361410xxx |
| 400 × 400 mm | 2,5–4,0 kg | 100–150 N | 1 | 361420xxx |
| 500 × 500 mm | 4,0–6,0 kg | 150–200 N | 1–2 | 361430xxx |
| 600 × 600 mm | 6,0–9,0 kg | 180–250 N | 2 | 361440xxx |
| 700 × 700 mm | 9,0–12,0 kg | 250–350 N | 2 | 361450xxx |

**Lebensdauer:**
- Qualitäts-Gasdruckfedern (Stabilus, Suspa, Bansbach): 5–10 Jahre / 20.000 Zyklen
- Budget-Gasdruckfedern (China-Import): 2–4 Jahre / 5.000 Zyklen
- Lewmar OEM (Stabilus): 6–10 Jahre

**Warnsignale für defekte Gasdruckfeder:**
- Luke fällt langsam zu oder hält nicht mehr in geöffneter Position
- Ölfilm am Zylinder (Dichtung undicht)
- Gasdruckfeder lässt sich von Hand leicht zusammendrücken (Gasverlust)

**Ersatz-Gasdruckfedern — Universalmaße:**

| Hub (mm) | Einbaulänge (mm) | Anschluss | Preis (EUR) | Passend für |
|----------|-----------------|-----------|------------|-------------|
| 200 | 475 | M8 Kugelkopf | 15–25 | Kleine Luken (300–400 mm) |
| 250 | 550 | M8 Kugelkopf | 18–30 | Mittlere Luken (400–500 mm) |
| 300 | 650 | M8/M10 Kugelkopf | 22–35 | Große Luken (500–600 mm) |
| 350 | 750 | M10 Kugelkopf | 28–45 | Sehr große Luken (600–700 mm) |

#### 7.9.2 Reibungsgelenke (Friction Stays)

**Alternative zu Gasdruckfedern** bei kleineren Luken und Budget-Modellen.

- Einstellbare Reibungskraft über Stellschraube
- Kein Gasverlust möglich (rein mechanisch)
- Stufenlose Positionierung in jedem Winkel
- Nachteil: Bei falsch eingestellter Reibung rutscht die Luke oder lässt sich schwer bewegen

**Einsatz:** Zugangsluken, Lazaretteluken, kleine Kabinenluken.

#### 7.9.3 Ketten und Spannschlösser (Chain Stays)

**Klassische Methode** bei älteren Booten und traditionellen Designs:
- Edelstahl-Kette (316L) mit Karabiner oder Schäkel
- Länge bestimmt maximalen Öffnungswinkel
- Robust, langlebig, einfach
- Nachteil: Keine Unterstützung beim Öffnen, keine stufenlose Arretierung

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Lewmar (UK) — Marktführer

**Firmenprofil:**
- **Gründung:** 1946 in Emsworth, Hampshire, UK
- **Eigentümer:** Lippert Components (USA), seit 2018
- **Hauptsitz:** Havant, Hampshire, UK
- **Mitarbeiter:** ca. 400
- **Marktanteil (geschätzt):** 45–55 % im europäischen Serienboot-Markt
- **Vertrieb:** Weltweit, Niederlassungen in UK, USA, Italien, Frankreich

**Produktlinien Decksluken:**

#### 8.1.1 Lewmar Ocean Serie

- **Positionierung:** Premium, Hochsee, CE Kat. A/B
- **Profil:** Ocean (60–80 mm über Deck)
- **Rahmen:** Eloxiertes Aluminium EN AW-6060-T5 (Standard), EN AW-6061-T6 (ab Size 60)
- **Linse:** 10 mm Acrylglas (klar oder getönt), auf Wunsch 12 mm
- **Dichtung:** EPDM Hohlprofil 10 × 8 mm, schwarz
- **Scharniere:** Edelstahl 316L, 4 mm Bolzen
- **Verschluss:** 2-Punkt Cam-Lever (Nockenverschluss) aus Edelstahl
- **Gasdruckfeder:** Stabilus, 1 × (bis Size 40), 2 × (ab Size 50)
- **Farbe:** Silber (Standard-Eloxierung), Schwarz (Black Anodized, Aufpreis 15 %)
- **CE:** Kat. A, Position 1
- **ISO 12216:** Geprüft und zertifiziert

**Besonderheiten der Ocean-Serie:**
- Luken-Rückhaltung: Sicherheitskette verhindert unkontrolliertes Zuschlagen bei Böe
- Entwässerung: Integrierte Drainagekanäle im Rahmen
- Lukendeckel: Leicht gewölbt (konvex) für Wasserablauf
- Ventilationsstellung: Arretierung bei ca. 10° möglich (Dog-Ventilation)
- Retrofit-freundlich: Umfangreiche Bohrschablonen und Einbauanleitungen

**Preise Ocean Serie (2025/2026, UVP):**

| Size | Klar (EUR) | Getönt (EUR) | Schwarz (EUR) | Art.-Nr. Basis |
|------|-----------|-------------|--------------|---------------|
| 00 | 280 | 310 | 320 | 399300xx |
| 10 | 340 | 375 | 390 | 399400xx |
| 20 | 410 | 455 | 475 | 399500xx |
| 30 | 480 | 530 | 555 | 399600xx |
| 40 | 560 | 620 | 650 | 399700xx |
| 50 | 680 | 750 | 790 | 399800xx |
| 60 | 820 | 910 | 955 | 399900xx |
| 70 | 980 | 1.080 | 1.135 | 399000xx |

#### 8.1.2 Lewmar Medium Profile Serie

- **Positionierung:** Mittelklasse, Fahrtensegler, CE Kat. A/B
- **Profil:** Medium (35–55 mm über Deck)
- **Rahmen:** Eloxiertes Aluminium EN AW-6060-T5
- **Linse:** 10 mm Acrylglas
- **Dichtung:** EPDM D-Profil 10 × 7 mm
- **Scharniere:** Aluminium/Edelstahl Kombination
- **Verschluss:** 2-Punkt Cam-Lever
- **Gasdruckfeder:** 1 × (bis Size 40), 2 × (ab Size 50)
- **CE:** Kat. A (Size ≤40), Kat. B (Size >40)

**Preise:** ca. 15–20 % günstiger als Ocean-Serie bei gleicher Größe.

#### 8.1.3 Lewmar Low Profile Serie

- **Positionierung:** Ästhetik-orientiert, Küstensegler, CE Kat. B/C
- **Profil:** Low (15–35 mm über Deck)
- **Rahmen:** Eloxiertes Aluminium, schlanker Querschnitt
- **Linse:** 10 mm Acrylglas
- **Dichtung:** EPDM D-Profil 8 × 6 mm
- **Scharniere:** Verdeckt (unter Rahmen)
- **Verschluss:** 1–2-Punkt Cam-Lever oder Push-Button
- **CE:** Kat. B (Position 2), Kat. C (Position 1)

#### 8.1.4 Lewmar Flush Serie

- **Positionierung:** Premium, Design-orientiert, CE Kat. C/D
- **Profil:** Flush (0–5 mm über Deck)
- **Rahmen:** Aluminium mit Flansch unter Deck
- **Linse:** 10 mm Acrylglas, bündig mit Decksebene
- **Dichtung:** EPDM Kompressionsdichtung in Rahmennut
- **Scharniere:** Komplett unter Deck
- **Verschluss:** Flush-Ring-Griff mit Over-Center-Verschluss
- **CE:** Kat. C (Position 2/3), Kat. D
- **Preis:** ca. 30–50 % teurer als Ocean-Serie bei gleicher Größe

#### 8.1.5 Lewmar Inspection Hatches

- **Positionierung:** Zugangsluken, Service-Luken
- **Formen:** Rund (Ø 200–350 mm), quadratisch (250 × 250 bis 375 × 375 mm)
- **Material:** ABS (Budget) oder Aluminium
- **Verschluss:** Screw-Out (rund) oder Cam-Lever (quadratisch)
- **Preis:** 35–120 EUR
- **Art.-Nr.:** 39xxxx30 (rund), 39xxxx40 (quadratisch)

#### 8.1.6 Lewmar Ersatzteile — Übersicht

| Ersatzteil | Art.-Nr. Basis | Preis-Bereich (EUR) |
|------------|---------------|---------------------|
| Dichtung (Meterware) | 369xxxx | 8–15 /m |
| Gasdruckfeder | 3614xxxx | 25–65 |
| Scharnier komplett | 3616xxxx | 45–120 |
| Lukendeckel (Linse + Rahmen) | 3618xxxx | 120–450 |
| Verschluss-Hebel | 3615xxxx | 20–55 |
| Fly Screen | 3618xxxx | 80–140 |
| Blind/Shade | 3618xxxx | 100–200 |

### 8.2 Goiot / Bénéteau Group (Frankreich)

**Firmenprofil:**
- **Gründung:** 1927 in Nantes, Frankreich
- **Eigentümer:** Bénéteau Group (seit 2005)
- **Produktion:** Herbignac, Loire-Atlantique, Frankreich
- **Spezialgebiet:** OEM-Lieferant für Bénéteau, Jeanneau, Lagoon, CNB
- **Marktanteil (geschätzt):** 20–30 % in Europa (primär französische Werften)

**Produktlinien:**

#### 8.2.1 Goiot Cristal

- **Positionierung:** Standard, Produktionsboote, CE Kat. B/C
- **Profil:** Medium bis Low (30–50 mm über Deck)
- **Rahmen:** Eloxiertes Aluminium
- **Linse:** 10 mm Acrylglas
- **Dichtung:** EPDM Spezialprofil 10 × 7 mm (NICHT Lewmar-kompatibel!)
- **Verschluss:** Einhand-Hebelverschluss (typisch für Goiot)
- **Größen:** T15 (340×340), T20 (400×400), T25 (460×460), T30 (520×520), T40 (600×600), T50 (680×680), T60 (770×770)
- **Preise:** ca. 10–15 % günstiger als Lewmar Ocean bei vergleichbarer Größe

**Preise Cristal (2025, UVP):**

| Modell | Außenmaß (mm) | Ausschnitt (mm) | Preis klar (EUR) | Art.-Nr. |
|--------|---------------|-----------------|-----------------|----------|
| T15 | 340 × 340 | 275 × 275 | 220–260 | 25.12.15xx |
| T20 | 400 × 400 | 330 × 330 | 280–330 | 25.12.20xx |
| T25 | 460 × 460 | 385 × 385 | 340–400 | 25.12.25xx |
| T30 | 520 × 520 | 440 × 440 | 400–470 | 25.12.30xx |
| T40 | 600 × 600 | 515 × 515 | 490–570 | 25.12.40xx |
| T50 | 680 × 680 | 590 × 590 | 590–680 | 25.12.50xx |
| T60 | 770 × 770 | 675 × 675 | 710–820 | 25.12.60xx |

**Hinweis für AYDI:** Bei Bénéteau- und Jeanneau-Booten ab Werk fast immer Goiot Cristal oder Opal verbaut. Dichtungsprofil NICHT mit Lewmar austauschbar — Nutmaße weichen ab.

#### 8.2.2 Goiot Opal

- **Positionierung:** Premium, Blauwasser, CE Kat. A/B
- **Profil:** Ocean (55–75 mm über Deck)
- **Rahmen:** Eloxiertes Aluminium EN AW-6061-T6
- **Linse:** 10–12 mm Acrylglas
- **Dichtung:** EPDM Hohlprofil 12 × 8 mm
- **Verschluss:** 2-Punkt Hebelverschluss mit Sicherheitsarretierung
- **Scharniere:** Edelstahl 316L, verstärkt
- **CE:** Kat. A, Position 1

**Preise:** ca. 5–10 % unter Lewmar Ocean.

**Besonderheiten:**
- Integrierter Mückenschutz (abnehmbar) bei Opal ab T30
- Optionaler Blind (Plissee) ab Werk integrierbar
- Spezielle "Tropicale"-Version mit UV-getönter Linse und Silikon-Dichtung

#### 8.2.3 Goiot Harmonie

- **Positionierung:** Luxus-Linie, Motoryachten und Katamarane
- **Profil:** Flush bis Low (0–25 mm über Deck)
- **Rahmen:** Aluminium oder Edelstahl 316L
- **Linse:** 10 mm Acrylglas oder Sicherheitsglas
- **Dichtung:** EPDM oder Silikon
- **Verschluss:** Push-Button oder Flush-Ring
- **CE:** Kat. B/C
- **Integriert:** Blind + Fly Screen ab Werk
- **Preis:** ca. 40–60 % Aufpreis gegenüber Cristal

### 8.3 Bomar / Pompanette (USA)

**Firmenprofil:**
- **Gründung:** 1946 in Fall River, Massachusetts, USA
- **Eigentümer:** Pompanette Inc.
- **Markt:** Primär US-Produktionsboote (Hunter, Catalina, Beneteau USA)
- **Marktanteil:** Dominant in Nordamerika (60–70 % OEM)

**Produktlinien:**

#### 8.3.1 Bomar Voyager

- **Positionierung:** Premium, Hochsee
- **Profil:** Ocean (55–70 mm)
- **Rahmen:** Extrudiertes Aluminium, eloxiert
- **Linse:** 10 mm Acrylglas (Standard), Polycarbonat (Option)
- **Dichtung:** EPDM 9 × 7 mm
- **Verschluss:** 2-Punkt Toggle-Verschluss
- **CE:** Kat. A/B
- **Größen:** 10" × 10" (254 mm²) bis 24" × 24" (610 mm²)
- **Preise:** 250–750 USD (ca. 230–700 EUR)

#### 8.3.2 Bomar Contour

- **Positionierung:** Standard, Küste/Binnenrevier
- **Profil:** Low bis Medium (20–40 mm)
- **Rahmen:** Aluminium, eloxiert
- **Linse:** 10 mm Acrylglas
- **Verschluss:** 1-Punkt Toggle
- **CE:** Kat. C/D
- **Preise:** 180–450 USD (ca. 165–415 EUR)

#### 8.3.3 Bomar Cast-Inspect

- **Positionierung:** Zugangs- und Inspektionsluken
- **Material:** Aluminium-Druckguss
- **Formen:** Rund, rechteckig
- **Preise:** 60–200 USD

**Hinweis:** Bomar-Luken verwenden zöllige Maße (Inch). Ausschnittmaße sind NICHT identisch mit metrischen Lewmar/Goiot-Maßen. Bei Austausch Bomar → Lewmar ist der Ausschnitt fast immer anzupassen.

### 8.4 Moonlight (Italien) — Flush-Spezialist

**Firmenprofil:**
- **Sitz:** Ravenna, Italien
- **Spezialgebiet:** Flächenbündige Luken für italienische Motoryachten und Segelyachten
- **Kunden:** Azimut, Benetti, Sanlorenzo, Ferretti, Cranchi, Arcadia
- **Marktposition:** Führend im Flush-Segment in Italien

**Produktlinien:**

#### 8.4.1 Moonlight MLC (Marine Luxury Collection)

- **Profil:** Flush (0–3 mm über Deck)
- **Rahmen:** Aluminium hart-eloxiert oder Edelstahl 316L gebürstet
- **Linse:** 10–12 mm Acrylglas, Sicherheitsglas optional
- **Dichtung:** EPDM oder Silikon, verdeckte Nut
- **Verschluss:** Flush-Griff (versenkt), Magnetverschluss oder Druckknopf
- **CE:** Kat. C/D (Standard), Kat. B (verstärkte Version)
- **Größen:** Custom (200 × 200 mm bis 1.200 × 600 mm)
- **Preise:** Ab ca. 600 EUR (400 × 400 mm) bis 3.500 EUR (1.000 × 500 mm)

**Besonderheiten:**
- Extrem niedrige Profilhöhe (Spezialität des Hauses)
- Maßanfertigung Standard (kein Serienprogramm wie Lewmar)
- Integrierte LED-Beleuchtung optional (Ambiente-Licht im Rahmen)
- Elektrische Öffnung optional (mit Besenzoni-Antrieb)

### 8.5 Houdini (UK) — Escape-Hatch-Spezialist

**Firmenprofil:**
- **Sitz:** UK
- **Spezialgebiet:** Fluchtluken, Ersatzdichtungen, Nachrüstluken
- **Besonderheit:** Umfassendstes Programm an Ersatzdichtungen für alle Lukenhersteller
- **Marktposition:** Standard-Referenz für Luken-Dichtungen im Aftermarket

**Produkte:**

#### 8.5.1 Houdini Escape Hatches

- **Modell Ocean:** 670 × 670 mm Außenmaß, 500 × 500 mm lichte Weite. CE Kat. A. Rahmen: eloxiertes Aluminium. Linse: 12 mm Acrylglas. Gewicht: 7,5 kg. Preis: ca. 550–650 EUR. Art.-Nr.: HO500-500.
- **Modell Coastal:** 570 × 570 mm Außenmaß, 400 × 520 mm lichte Weite (minimum Fluchtluke). CE Kat. B. Preis: ca. 450–550 EUR. Art.-Nr.: HO400-520.
- **Modell Flush Escape:** Flächenbündig, 620 × 720 mm Außenmaß, 450 × 550 mm lichte Weite. CE Kat. B. Preis: ca. 700–850 EUR.

**Merkmale aller Houdini Escape Hatches:**
- Von innen und außen ohne Werkzeug zu öffnen
- Beschriftung "EMERGENCY EXIT" beidseitig
- 90° Öffnungswinkel für ungehinderten Durchstieg
- Sicherheitsarretierung verhindert Zuschlagen
- Erfüllt ISO 12216 Fluchtluken-Anforderungen

#### 8.5.2 Houdini Ersatzdichtungen

Houdini ist DIE Referenz für Luken-Ersatzdichtungen und bietet Kompatibilität mit praktisch allen Lukenherstellern:

**EPDM-Serie (2xxx):**

| Houdini Nr. | Profil | Maß (B × H mm) | Kompatibel mit | Preis /m (EUR) |
|-------------|--------|-----------------|---------------|----------------|
| 2100 | D-Profil | 6 × 5 | Gebo Classic | 7–10 |
| 2120 | D-Profil | 8 × 6 | Lewmar Standard/Classic/Low Profile | 8–12 |
| 2180 | D-Profil | 9 × 7 | Bomar Standard | 9–13 |
| 2200 | D-Profil | 10 × 6 | Vetus Libero | 9–13 |
| 2260 | Spezialprofil | 10 × 7 | Goiot Cristal | 10–14 |
| 2280 | D-Profil | 10 × 7 | Lewmar Medium Profile | 10–14 |
| 2300 | Hohlprofil | 10 × 8 | Lewmar Ocean, Rutgerson | 11–16 |
| 2340 | Hohlprofil | 12 × 8 | Goiot Opal | 12–17 |
| 2400 | D-Profil | 12 × 10 | Freeman Marine, Superyacht | 14–20 |
| 2500 | U-Kanal | 10 × 8 | Houdini Escape Hatches | 12–17 |

**Silikon-Serie (3xxx) — gleiche Profile wie 2xxx, aber Silikon:**

| Houdini Nr. | Profil | Maß (B × H mm) | Preis /m (EUR) | Vorteil ggü. EPDM |
|-------------|--------|-----------------|----------------|-------------------|
| 3120 | D-Profil | 8 × 6 | 18–28 | UV-Beständigkeit, Lebensdauer |
| 3180 | D-Profil | 9 × 7 | 20–30 | UV-Beständigkeit |
| 3260 | Spezialprofil | 10 × 7 | 22–32 | UV-Beständigkeit |
| 3300 | Hohlprofil | 10 × 8 | 25–36 | UV-Beständigkeit |
| 3340 | Hohlprofil | 12 × 8 | 28–40 | UV-Beständigkeit |

### 8.6 Freeman Marine (USA) — Superyacht-Spezialist

**Firmenprofil:**
- **Gründung:** 1971 in Gold Beach, Oregon, USA
- **Spezialgebiet:** Luken, Fenster und Türen für Superyachten (>24 m)
- **Kunden:** Lürssen, Feadship, Heesen, Benetti, Perini Navi
- **Zertifizierungen:** ABS, Lloyd's, DNV, BV

**Produktlinien:**

#### 8.6.1 Freeman FH-Serie (Flush Hatches)

- **Größen:** Custom von 400 × 400 mm bis 2.000 × 1.500 mm
- **Rahmen:** Edelstahl 316L (Standard) oder Aluminium 5083
- **Linse:** VSG (Verbundsicherheitsglas), ESG, oder Acrylglas 15–25 mm
- **Dichtung:** Inflatable (pneumatisch aufblasbar) oder EPDM Premium
- **Antrieb:** Manuell, elektrisch, oder hydraulisch
- **CE / Klasse:** ABS, Lloyd's SSC, ISO 12216
- **Preise:** 3.000–25.000 EUR je nach Größe und Ausstattung

#### 8.6.2 Freeman WH-Serie (Watertight Hatches)

- **Einsatz:** Maschinenraum, technische Räume
- **Dichtigkeit:** Watertight (nicht nur weathertight) nach IMO SOLAS
- **Rahmen:** Edelstahl 316L, Flanschstärke 6–12 mm
- **Verschluss:** Dog-Bolzen (4–8 Stück), manuell oder hydraulisch
- **Feuerwiderstand:** 30 oder 60 Minuten (A-30 / A-60)

### 8.7 Rutgerson (Schweden) — Premium Racing/Cruising

**Firmenprofil:**
- **Sitz:** Göteborg, Schweden
- **Spezialgebiet:** Hochwertige Luken für Performance-Cruiser und Racing-Yachten
- **Kunden:** Hallberg-Rassy, Najad, Sweden Yachts, Arcona

**Produktlinien:**

#### 8.7.1 Rutgerson RC-Serie (Racing/Cruising)

- **Profil:** Ocean bis Medium (45–70 mm)
- **Rahmen:** EN AW-6082-T6 Aluminium, hart-eloxiert (25 µm)
- **Linse:** 10–12 mm Acrylglas
- **Dichtung:** EPDM Standard, Silikon optional
- **Verschluss:** 2-Punkt Cam-Lever, Edelstahl 316L
- **Scharniere:** Edelstahl 316L, 5 mm Bolzen (verstärkt)
- **CE:** Kat. A, Position 1
- **Besonderheit:** CFK-Rahmen-Option (Carbon) für Racing, -40 % Gewicht
- **Größen:** 350 × 350 mm bis 750 × 750 mm
- **Preise:** 450–1.200 EUR (Aluminium), 1.200–3.500 EUR (Carbon)

### 8.8 Manship (Taiwan) — Budget-Segment

**Firmenprofil:**
- **Sitz:** Taiwan
- **Markt:** OEM für asiatische Werften, Aftermarket weltweit
- **Positionierung:** Budget, preiswert, akzeptable Qualität

**Produktlinie:**

- **Profil:** Medium (30–50 mm)
- **Rahmen:** Aluminium eloxiert (Standard-Qualität)
- **Linse:** 8–10 mm Acrylglas
- **Dichtung:** EPDM (kürzere Lebensdauer als Lewmar/Goiot, ca. 5–8 Jahre)
- **Verschluss:** 1–2-Punkt Toggle
- **CE:** Kat. C/D (teilweise B bei kleinen Größen)
- **Größen:** 300 × 300 mm bis 600 × 600 mm
- **Preise:** 120–350 EUR (40–50 % günstiger als Lewmar)

**AYDI-Bewertungshinweis:** Manship-Luken sind funktional, aber Finish und Langlebigkeit deutlich unter Lewmar/Goiot. Eloxierung dünner (8–12 µm vs. 15+ µm), Schrauben teilweise 304 statt 316L. Für Küstenreviere und Binnengewässer akzeptabel, für Hochsee nicht empfohlen.

### 8.9 Vetus (Niederlande)

**Firmenprofil:**
- **Sitz:** Schiedam, Niederlande
- **Gründung:** 1966
- **Spezialgebiet:** Universelles marine Zubehörprogramm
- **Stärke:** Gutes Preis-Leistungs-Verhältnis, breite Verfügbarkeit

**Luken-Produktlinien:**

#### 8.9.1 Vetus Libero

- **Profil:** Low (20–35 mm)
- **Rahmen:** Aluminium eloxiert
- **Linse:** 10 mm Acrylglas
- **Dichtung:** EPDM D-Profil 8 × 6 mm
- **Verschluss:** 1-Punkt Push-Button
- **CE:** Kat. C/D
- **Größen:** 290 × 290 mm bis 580 × 580 mm
- **Preise:** 200–500 EUR
- **Artikelnummern:** DLUXXXX (z.B. DLU3030 = 300 × 300 mm)

#### 8.9.2 Vetus Altus

- **Profil:** Medium/Ocean (40–60 mm)
- **Rahmen:** Aluminium hart-eloxiert
- **Linse:** 10 mm Acrylglas
- **Dichtung:** EPDM Hohlprofil
- **Verschluss:** 2-Punkt Cam-Lever
- **CE:** Kat. B/A (modellabhängig)
- **Größen:** 350 × 350 mm bis 630 × 630 mm
- **Preise:** 350–700 EUR

### 8.10 Nemo (Italien)

**Firmenprofil:**
- **Sitz:** Italien
- **Spezialgebiet:** Luken und Portlights für italienische Motoryachten
- **Kunden:** Azimut, Cranchi, Sessa

**Produktlinie:**
- **Profil:** Low bis Flush (10–30 mm)
- **Rahmen:** Aluminium oder Edelstahl 316L
- **Linse:** Acrylglas oder ESG
- **Dichtung:** EPDM oder Silikon
- **CE:** Kat. B/C
- **Preise:** 300–800 EUR (vergleichbar Lewmar Medium/Low Profile)

### 8.11 Raboesch (Niederlande)

**Firmenprofil:**
- **Sitz:** Niederlande
- **Spezialgebiet:** Luken, Ventile, Bootsbeschläge
- **Markt:** Binnenschifffahrt und Küsten-Motorboote

**Produktlinie:**
- **Profil:** Low bis Medium
- **Rahmen:** Aluminium eloxiert
- **Linse:** Acrylglas 8–10 mm
- **Dichtung:** EPDM
- **CE:** Kat. C/D
- **Preise:** 150–400 EUR
- **Besonderheit:** Gutes Programm an runden und ovalen Luken für Binnenboote

### 8.12 Plastimo (Frankreich)

**Firmenprofil:**
- **Gründung:** 1963 in Lorient, Frankreich
- **Spezialgebiet:** Breites marine Zubehörprogramm
- **Luken:** Einsteigerbereich bis Mittelklasse

**Luken-Programm:**
- **Profil:** Low bis Medium
- **Rahmen:** Aluminium eloxiert
- **Linse:** 8–10 mm Acrylglas
- **Dichtung:** EPDM
- **CE:** Kat. C (Standard), Kat. B (verstärkt)
- **Größen:** 280 × 280 mm bis 500 × 500 mm
- **Preise:** 150–400 EUR

### 8.13 Osculati (Italien)

**Firmenprofil:**
- **Sitz:** Segrate (Mailand), Italien
- **Gründung:** 1958
- **Spezialgebiet:** Universeller marine Zubehörkatalog (>50.000 Artikel)

**Luken-Programm:**
- Budget-Segment, ABS-Kunststoff-Luken (ab 30 EUR) bis Aluminium-Luken (ab 150 EUR)
- Inspektionsluken, Zugangsluken, einfache Decksluken
- CE Kat. D (Kunststoff), Kat. C (Aluminium)
- **Vorteil:** Breite Verfügbarkeit, auch in kleinen Marinas
- **Nachteil:** Qualität unter Lewmar/Goiot, für anspruchsvolle Anwendungen nicht empfohlen

### 8.14 Besenzoni (Italien) — Elektrische Luken

**Firmenprofil:**
- **Sitz:** Sarnico, Italien
- **Spezialgebiet:** Elektrische und hydraulische Decksbeschläge, Gangways, Kräne, Luken
- **Kunden:** Azimut, Ferretti, Riva, Sunseeker

**Luken-Programm:**
- **Serie PK:** Vollautomatische Decksluken mit Elektromotor
- **Rahmen:** Edelstahl 316L poliert oder Aluminium
- **Linse:** VSG (Sicherheitsglas) oder Acrylglas
- **Antrieb:** 12 V oder 24 V Linearaktuator, Einklemmschutz
- **Regensensor:** Optional (Auto-Close bei Regen)
- **Steuerung:** Drucktaster, Fernbedienung, oder Integration in Yacht-Bussystem (CAN/NMEA 2000)
- **CE:** Kat. B/C (modellabhängig)
- **Preise:** 2.500–8.000 EUR je nach Größe und Ausstattung

### 8.15 Hersteller-Vergleichsmatrix

| Hersteller | Land | Stärke | Schwäche | Preislevel | CE max. | OEM für |
|------------|------|--------|----------|------------|---------|---------|
| Lewmar | UK | Breitstes Programm, Ersatzteilversorgung | Preis | ★★★★ | A | Bavaria, Hanse, Hallberg-Rassy, Oyster |
| Goiot | FR | Preis-Leistung, gute Qualität | Ersatzteile außerhalb FR | ★★★ | A | Bénéteau, Jeanneau, Lagoon |
| Bomar | USA | US-Markt-Dominanz, robust | Zöllige Maße, EU-Verfügbarkeit | ★★★ | A | Hunter, Catalina, Island Packet |
| Moonlight | IT | Flush-Spezialist, Ästhetik | Kleine Firma, lange Lieferzeiten | ★★★★★ | C | Azimut, Sanlorenzo (Flush) |
| Houdini | UK | Escape Hatches, Dichtungen | Keine Standard-Luken | ★★★ | A | — (Aftermarket) |
| Freeman | USA | Superyacht-Qualität, Klassifikation | Extrem teuer | ★★★★★★ | ABS/LR | Lürssen, Feadship, Heesen |
| Rutgerson | SE | Premium, Carbon-Option | Nische, geringe Verfügbarkeit | ★★★★★ | A | Hallberg-Rassy, Najad |
| Manship | TW | Preis | Qualität, Langlebigkeit | ★★ | C | Asiatische Werften |
| Vetus | NL | Preis-Leistung, Verfügbarkeit | Keine Hochsee-Zulassung | ★★★ | B | — (Aftermarket) |
| Nemo | IT | Ital. Motoryachten | Nische | ★★★★ | B | Azimut, Cranchi |
| Raboesch | NL | Binnenluken | Keine Hochsee | ★★ | D | — |
| Plastimo | FR | Preis, Verfügbarkeit | Einsteigerqualität | ★★ | C | — |
| Osculati | IT | Breitstes Sortiment, Budget | Qualität | ★–★★ | D | — |
| Besenzoni | IT | Elektro-Luken, Automatik | Extrem teuer | ★★★★★★ | B | Azimut, Ferretti, Riva |

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Vorschiff-Luke (Foredeck Hatch)

#### 9.1.1 Anforderungen

Die Vorschiff-Luke ist die am stärksten beanspruchte Luke auf jedem Segelboot. Sie liegt in **Position 1** (ISO 12216), direkt im Bereich der Bugwelle und überkommenden Seen.

**Spezifische Anforderungen:**
- **Wasserdichtheit:** Muss Grünwasser standhalten (Welle überspült gesamtes Vordeck)
- **Festigkeit:** Druckprüfung Kat. A: 6,0 kPa (Position 1, Expositionsklasse A)
- **Profil:** Ocean-Profil EMPFOHLEN (Süllhöhe 60–80 mm bietet Barriere gegen überströmendes Wasser)
- **Ventilation:** Öffnung nach vorne (hinged forward) fängt Fahrtwind → beste Belüftung der Vorkabine
- **Segelhandling:** Vorschiff-Luke wird zum Segeln genutzt (Spinnaker-Bergemannöver, Segel unter Deck reichen)
- **Fluchtluke:** Oft die einzige Fluchtmöglichkeit aus der Vorkabine → muss ISO-12216-Fluchtluken-Anforderung erfüllen

**Doppelfunktion Belüftung + Flucht:**
Die Vorkabinen-Luke muss sowohl als Belüftung als auch als Fluchtluke dienen. Das bedeutet:
- Mindestlichte Weite 400 × 520 mm
- Von innen ohne Werkzeug öffenbar
- Sicherheitsarretierung in geöffneter Position

#### 9.1.2 Empfohlene Luken nach Bootsgröße

| Bootslänge (LOA) | Empf. Lukengröße | Empf. Profil | Empf. Hersteller | Fluchtluke? |
|-------------------|------------------|-------------|-----------------|-------------|
| 8–9 m | 400 × 400 mm | Ocean | Lewmar Ocean Size 20, Goiot Cristal T20 | Grenzwertig (empf. Size 30) |
| 9–11 m | 500 × 500 mm | Ocean | Lewmar Ocean Size 30/40, Goiot Opal T30 | Ja (ab Size 30) |
| 11–14 m | 500–600 mm | Ocean | Lewmar Ocean Size 40/50, Goiot Opal T40/T50 | Ja |
| 14–18 m | 600–700 mm | Ocean | Lewmar Ocean Size 50/60, Houdini Ocean | Ja |
| 18–24 m | 700–800 mm | Ocean | Lewmar Ocean Size 60/70, Freeman FH | Ja |

#### 9.1.3 Typische Probleme bei Vorschiff-Luken

| Problem | Häufigkeit | Ursache | Lösung | Kosten (EUR) |
|---------|-----------|--------|--------|-------------|
| Undichtheit Dichtung | Sehr häufig | UV-Alterung, Druckverformungsrest | Dichtung tauschen | 20–40 (DIY) |
| Acrylglas Crazing | Häufig | UV + thermische Zyklen | Polieren oder Linse tauschen | 30–300 |
| Gasdruckfeder schwach | Häufig (nach 5–8 J.) | Gasverlust | Gasdruckfeder tauschen | 25–65 |
| Scharnier-Spiel | Gelegentlich | Verschleiß, Korrosion | Bolzen tauschen oder Scharnier erneuern | 45–120 |
| Rahmen-Korrosion | Selten (bei Alu) | Spaltkorrosion, galvanisch | Rahmen abdichten, ggf. Luke tauschen | 50–800 |
| Luke undicht trotz neuer Dichtung | Gelegentlich | Rahmenverformung, Deck-Setzung | Rahmen richten, Shims, ggf. neu einbauen | 200–600 |

### 9.2 Salon-Luken (Saloon Hatches)

#### 9.2.1 Anforderungen

Salon-Luken liegen auf dem Aufbaudeck (Coachroof/Deckhaus), typisch in **Position 2 oder 3** (ISO 12216). Sie sind teilweise durch das Deckhaus geschützt.

**Spezifische Anforderungen:**
- **Licht:** Primäre Tageslichtquelle für den Salon → große Luken, klare Linse
- **Ventilation:** Querbelüftung durch gegenüberliegende Luken (Bb + Stb)
- **Ästhetik:** Sichtbar aus dem Salon → optisch ansprechend (Low Profile oder Flush bevorzugt bei Motoryachten)
- **Verdunkelung:** Blinds/Plissees essenziell (Sonne auf Polster → Hitze, UV-Schäden)
- **Mückenschutz:** Wichtig (Salon als Aufenthaltsraum)
- **Begehbarkeit:** Salon-Luken auf dem Aufbaudeck werden oft begangen → Anti-Skid!

#### 9.2.2 Typische Konfigurationen

**Segelboot 10–14 m:**
- 2–4 Salon-Luken auf dem Aufbaudeck (je 1–2 Bb/Stb)
- Größe: 400 × 400 mm bis 500 × 500 mm
- Profil: Low oder Medium (wenig Stolpergefahr auf Aufbaudeck)
- Lewmar Low Profile Size 20–40 oder Goiot Cristal T20–T30

**Motoryacht 10–16 m:**
- 2–6 Salon-Luken, teils im Hardtop, teils im Aufbaudeck
- Größe: 500 × 500 mm bis 700 × 700 mm
- Profil: Flush oder Low (Ästhetik)
- Moonlight MLC, Lewmar Flush, Nemo

**Katamaran 12–18 m:**
- 4–8 Salon-Luken auf dem Brückendeck
- Größe: 400 × 400 mm bis 600 × 600 mm
- Profil: Low oder Flush (Trampoln-Netz liegt nahe)
- Goiot Cristal/Opal, Lewmar Low Profile

#### 9.2.3 Ventilations-Optimierung Salon

Für optimale Querbelüftung im Salon:

1. **Gegenüberliegende Luken öffnen** (Bb + Stb) → Durchzug
2. **Luv-seitige Luke nach vorne öffnen** (Windeinlass)
3. **Lee-seitige Luke nach achtern öffnen** oder ganz öffnen (Windauslass, Sog-Effekt)
4. **Ventilationsstellung:** Bei Regen Luken in 10°-Stellung arretieren → Belüftung ohne Wassereinbruch (nur bei Spritzwasser, nicht bei Regen direkt auf Luke)

**Effektiver Ventilationsquerschnitt (Berechnung für AYDI):**

```
Q_eff = Σ (A_luke × sin(α) × f_screen × f_wind)

Wobei:
  A_luke = Fläche der Lukenöffnung (mm²)
  α = Öffnungswinkel der Luke
  f_screen = Reduktionsfaktor Mückenschutz (0,6–0,72 mit Gaze)
  f_wind = Winddruckfaktor (1,0 bei Luv, 0,5 bei Lee, 0,3 bei seitlich)
```

### 9.3 Achterkabinen-Luken (Aft Cabin Hatches)

#### 9.3.1 Anforderungen

Achterkabinen-Luken liegen typisch auf dem Achterdeck oder dem hinteren Aufbaudeck. Position 2 oder 3 (ISO 12216). Weniger Grünwasser-Belastung als Vorschiff.

**Spezifische Anforderungen:**
- **Fluchtluke:** Achterkabine hat meist nur einen Zugang (durch den Salon) → Fluchtluke ERFORDERLICH
- **Privatsphäre:** Oft nahe am Cockpit → Verdunkelungs-Blind sinnvoll
- **Geräusch:** Bei Motorbooten nahe am Motor → Schallschutz-Aspekte
- **Ventilation:** Wichtig für Schlafkomfort

#### 9.3.2 Empfohlene Konfiguration

| Bootslänge | Anzahl Achterkab.-Luken | Empf. Größe | Profil | Fluchtluke? |
|------------|------------------------|-------------|--------|-------------|
| 10–12 m | 1 (Stb oder Bb) | 400 × 400 mm | Medium/Low | Ja (wenn einziger Ausgang) |
| 12–15 m | 2 (Bb + Stb) | 400–500 mm | Medium/Low | Ja (mindestens 1) |
| 15–18 m | 2–4 | 500 × 500 mm | Low/Flush | Ja |
| 18+ m | Nach Kabinen-Layout | 500–600 mm | Low/Flush | Ja |

### 9.4 Lazarette-Luken (Lazarette Hatches)

#### 9.4.1 Anforderungen

Lazarette (Stauräume achtern im Cockpit oder unter dem Achterdeck) benötigen Zugangsluken. Diese Luken sind funktional, nicht dekorativ.

**Spezifische Anforderungen:**
- **Begehbarkeit:** Lazaretteluken im Cockpitboden MÜSSEN begehbar sein
- **Anti-Skid:** Oberfläche rutschhemmend
- **Keine Transparenz nötig:** Massiver Deckel (Aluminium, GFK, Teak) üblich
- **Dichtigkeit:** Spritzwasserdicht ausreichend (Cockpit ist teilweise geschützt)
- **Handhabung:** Schnelles Öffnen/Schließen für Zugang zu Festmachern, Fendern, Gasflaschen
- **Verriegelung:** Flush-Ring-Griffe (keine erhabenen Griffe → Stolpergefahr im Cockpit)
- **Gasflaschen-Stauung:** Wenn Gasflaschen im Lazarett → Belüftungsöffnung am Boden (schwerer als Luft)

#### 9.4.2 Typische Produkte

| Produkt | Typ | Größe | Material | Preis (EUR) |
|---------|-----|-------|----------|-------------|
| Lewmar Flush Inspection Hatch | Rund, Screw-Out | Ø 200–350 mm | ABS/Alu | 35–90 |
| Lewmar Flush Access Hatch | Quadratisch | 375 × 375 mm | Aluminium | 180–280 |
| Vetus DLUXXXX | Quadratisch | 290–580 mm | Aluminium | 200–500 |
| Beckson Deck Plate | Rund, Screw-Out | Ø 100–300 mm | ABS | 15–45 |
| Custom GFK/Teak | Rechteckig | Nach Maß | GFK/Teak | 100–500 |

### 9.5 Maschinenraum-Luken (Engine Room Hatches)

#### 9.5.1 Anforderungen

Maschinenraum-Luken unterliegen zusätzlichen Anforderungen wegen Brandschutz und Belüftung.

**Regulatorische Anforderungen:**
- **ISO 9094 (Brandschutz):** Maschinenraumluke muss feuerhemmend sein (min. 15 min bei Charter/Passagier)
- **Belüftung:** Maschinenraum benötigt Lüftungsquerschnitt = max(0,05 m², Motor_kW × 0,0003 m²)
- **ABYC H-2:** Bei Benzinmotoren: funkensichere Belüftung, Luke darf keine Zündquelle sein
- **Lloyd's SSC:** Bei Charter/Passagieryachten: A-30 Brandschutz, selbstschließend

**Konstruktive Anforderungen:**
- **Schallschutz:** Lukendeckel mit Schallschutzmatten (Polyurethanschaum, 20–50 mm) ausgekleidet
- **Gewicht:** Massive Deckel (GFK/Aluminium + Schalldämmung) → 15–40 kg → Gasdruckfedern oder Hydraulik
- **Belüftungsgitter:** Integrierte Lüftungsschlitze oder separater Lüftungskanal
- **Sicherheit:** Von außen und innen öffenbar (Flucht bei Brand)

#### 9.5.2 Schalldämmung

| Material | Dicke (mm) | Schalldämmung (dB) | Temperaturbeständigkeit | Preis (/m²) |
|----------|-----------|-------------------|------------------------|-------------|
| PU-Schaum (selbstklebend) | 20 | 8–12 | bis 120 °C | 25–50 EUR |
| PU-Schaum mit Alukaschierung | 30 | 12–18 | bis 150 °C | 40–80 EUR |
| Mineralwolle mit Folie | 40 | 18–25 | bis 700 °C | 30–60 EUR |
| Composite-Sandwich | 50 | 22–30 | bis 200 °C | 80–150 EUR |

**Empfohlene Hersteller für Schalldämmung:**
- Isover (Saint-Gobain): Marine-Mineralwolle
- Soundown (USA): Marine-Schallschutz-Systeme
- VETUS: Selbstklebende Schallschutzmatten, Art.-Nr. SILENTxxxx

### 9.6 Fluchtluken — Zusammenfassung und Planungshilfe

#### 9.6.1 Wo Fluchtluken erforderlich sind (Entscheidungsbaum)

```
Raum unter Deck?
  └─ Ja → Hat der Raum ≥2 voneinander unabhängige Ausgänge?
            └─ Ja → Keine zusätzliche Fluchtluke nötig
            └─ Nein → IST eine Decksluke vorhanden?
                        └─ Ja → Lichte Weite ≥400 × 520 mm?
                                  └─ Ja → Von innen ohne Werkzeug öffenbar?
                                            └─ Ja → Fluchtluke OK ✓
                                            └─ Nein → Verschluss ändern!
                                  └─ Nein → Luke zu klein → größere einbauen oder zusätzliche
                        └─ Nein → Fluchtluke einbauen!
```

#### 9.6.2 Mindestmaße nach Norm und Klassifikation

| Norm / Klasse | Mindest-Lichte-Weite | Mindest-Durchmesser (rund) |
|---------------|---------------------|---------------------------|
| ISO 12216 (Standard) | 400 × 520 mm | 450 mm |
| Lloyd's SSC | 450 × 600 mm | 500 mm |
| ABS Guide | 400 × 520 mm (ISO-konform) | 450 mm |
| SOLAS (Handelsschiffe) | 600 × 600 mm | 600 mm |

#### 9.6.3 Kosten Fluchtluken-Nachrüstung

| Szenario | Luke | Einbau (Material) | Einbau (Arbeit, Werft) | Gesamt |
|----------|------|-------------------|----------------------|--------|
| Vorhandene Luke vergrößern | — | 200–400 EUR | 6–10 h = 480–800 EUR | 680–1.200 EUR |
| Neue Fluchtluke einbauen | 450–700 EUR | 300–500 EUR | 8–14 h = 640–1.120 EUR | 1.390–2.320 EUR |
| Houdini Escape Hatch komplett | 550–650 EUR | 250–400 EUR | 8–12 h = 640–960 EUR | 1.440–2.010 EUR |

**AYDI-Empfehlung:** Bei Booten ohne normkonforme Fluchtluke in der Vorkabine generiert das Compliance-Modul automatisch einen **CRITICAL**-Befund: "Fluchtluke Vorkabine: nicht normkonform / nicht vorhanden. Nachrüstung empfohlen. Confidence: measured (ISO 12216)."

---

**— Ende der Sektionen 1–9 —**

---

# 10. Technische Referenz & Berechnungen

## 10.1 Wasserdichtigkeit — Druckberechnung

### 10.1.1 Grundlagen der Druckbelastung auf Decksluken

Die auf eine Decksluke wirkende hydrodynamische Last setzt sich zusammen aus:

- **Statischer Druck (hydrostatisch):** P_stat = ρ × g × h, wobei h = Überflutungshöhe über Decksluke
- **Dynamischer Druck (Slamming/Wellenschlag):** P_dyn = 0,5 × ρ × v², wobei v = Aufprallgeschwindigkeit
- **Kombinierte Belastung:** P_total = P_stat + C_d × P_dyn, mit C_d = dynamischer Koeffizient (1,0–2,5 je nach Lukenposition)

### 10.1.2 Druckwerte nach CE-Kategorie und Position

| CE-Kategorie | Lukenposition | Min. Prüfdruck (kPa) | Bemerkung |
|--------------|--------------|----------------------|-----------|
| A (Ozean) | Vorschiff (< 0,25 × LWL von Bug) | 12,0–18,0 | Höchste Slamming-Belastung |
| A (Ozean) | Mittschiffs | 8,0–12,0 | Moderate Wellenbelastung |
| A (Ozean) | Achterdeck | 5,0–8,0 | Geringste Belastung |
| B (Küste) | Vorschiff | 8,0–12,0 | — |
| B (Küste) | Mittschiffs | 5,0–8,0 | — |
| C (Binnengewässer) | Alle Positionen | 3,0–5,0 | Reduzierte Anforderungen |
| D (Geschützt) | Alle Positionen | 1,5–3,0 | Minimale Anforderungen |

> ⚠️ **ZU PRÜFEN (Audit):** Die hier genannten Prüfdrücke (u. a. Kat. A Vorschiff 12,0–18,0 kPa) widersprechen den ISO-12216-Prüfdrücken in Abschnitt 1.2.2/1.3.1 sowie 9.1.1 (Kat. A, Position 1: 6,0 kPa) für dieselbe Zone und Design-Kategorie. Beide Stellen bezeichnen den normativen Prüfdruck einer exponierten Bug-/Position-1-Luke der Kategorie A, geben aber um Faktor 2–3 abweichende Werte an. Diese Tabelle ist gegenüber den drei konsistenten 6,0-kPa-Fundstellen die abweichende Einzelquelle. Werte NICHT ohne Abgleich mit der Originalnorm (ISO 12216) vereinheitlichen — Zahlen bewusst unverändert belassen. Hinweis zur Abgrenzung: Die deutlich höheren Werte im folgenden Berechnungsbeispiel 10.1.3 (49,1/73,7 kPa) sind ein rechnerischer Worst-Case-Lastfall inkl. dynamischer Slamming-Überhöhung und damit eine andere Größe als der Prüfdruck (siehe Anmerkung dort).

### 10.1.3 Berechnungsbeispiel: Vorschiffsluke 500×500mm, CE-Kat A

```
Gegebene Werte:
  Lukenabmessung: 500 × 500 mm = 0,25 m²
  Überflutungshöhe (worst case): h = 1,2 m
  Aufprallgeschwindigkeit (Slamming): v = 6 m/s
  Seewasserdichte: ρ = 1025 kg/m³
  Dynamischer Koeffizient Vorschiff: C_d = 2,0

Statischer Druck:
  P_stat = 1025 × 9,81 × 1,2 = 12.066 Pa ≈ 12,1 kPa

Dynamischer Druck:
  P_dyn = 0,5 × 1025 × 6² = 18.450 Pa ≈ 18,5 kPa

Kombinierter Prüfdruck:
  P_total = 12,1 + 2,0 × 18,5 = 49,1 kPa

Resultierende Kraft auf Luke:
  F = P_total × A = 49.100 × 0,25 = 12.275 N ≈ 1.252 kg

→ Die Decksluke muss einer Drucklast von mind. 49,1 kPa standhalten.
→ Sicherheitsfaktor ×1,5 → Auslegungsdruck: 73,7 kPa
```

> **Hinweis (Audit):** Der hier berechnete Wert (P_total = 49,1 kPa; mit Sicherheitsfaktor ×1,5 → 73,7 kPa) ist ein rechnerischer hydrodynamischer Worst-Case-Lastfall (statischer Überflutungsdruck P_stat + dynamisch überhöhter Slamming-Anteil C_d × P_dyn, hier C_d = 2,0) und NICHT identisch mit dem normativen ISO-12216-Prüfdruck aus Abschnitt 1.3.1/10.1.2. Die scheinbare Diskrepanz (Faktor >10 gegenüber 6,0 kPa) resultiert aus dem grundlegend anderen Bemessungskonzept (rechnerische Auslegungslast vs. genormter Proof-Test-Druck) und ist insoweit kein Widerspruch. Die Rechnung selbst ist arithmetisch konsistent (P_stat = 1025·9,81·1,2 ≈ 12,1 kPa; P_dyn = 0,5·1025·6² ≈ 18,5 kPa; P_total = 12,1 + 2,0·18,5 = 49,1 kPa). Der eigentliche Normwiderspruch betrifft ausschließlich die genormten Prüfdrücke (6,0 kPa vs. 12,0–18,0 kPa, siehe Flags in 1.3.1 und 10.1.2).

### 10.1.4 Dichtungsprüfung nach ISO 12216

**Prüfverfahren:**
1. Luke geschlossen, alle Verschlüsse angezogen
2. Wasserstrahl aus 25 mm Düse, Druck 1 bar (100 kPa), Abstand 1,5 m
3. Besprühung aller Dichtungsflansche für min. 5 Minuten
4. Kriterium: Kein sichtbarer Wasserdurchtritt auf Innenseite

**AYDI-Bewertung Wasserdichtigkeit:**

| Zustand | Score | Confidence |
|---------|-------|------------|
| Keine Leckage bei Prüfdruck | 95–100 | measured |
| Tropfenbildung nach >3 min | 70–85 | measured |
| Tropfenbildung nach <1 min | 40–60 | measured |
| Durchgängiger Wasserfilm | 10–30 | measured |
| Freier Wassereintritt | 0–10 | measured |

## 10.2 Belüftungsberechnung

### 10.2.1 Ventilationsanforderungen nach ISO 11999 / Klassifikation

Die erforderliche natürliche Ventilationsfläche für Wohnräume unter Deck berechnet sich:

```
A_vent = V_raum × n_wechsel / (3600 × v_luft)

Wobei:
  A_vent = erforderliche freie Ventilationsöffnung (m²)
  V_raum = Raumvolumen (m³)
  n_wechsel = Luftwechselrate (1/h) — Wohnraum: 6–10, Pantry: 15–20, Nasszelle: 10–15
  v_luft = mittlere Luftgeschwindigkeit durch Öffnung (m/s) — natürliche Ventilation: 0,5–1,5
```

### 10.2.2 Berechnungsbeispiel: Vorschiffskabine

```
Gegebene Werte:
  Kabinenlänge: 2.800 mm, Breite: 2.200 mm, Höhe: 1.900 mm
  V_raum = 2,8 × 2,2 × 1,9 = 11,7 m³
  Luftwechselrate Schlafkabine: n = 8 /h
  Mittlere Luftgeschwindigkeit: v = 0,8 m/s

Erforderliche Ventilationsfläche:
  A_vent = 11,7 × 8 / (3600 × 0,8) = 0,0325 m² = 325 cm²

Typische Decksluke 500×500 mm:
  Freie Öffnungsfläche bei 70° Öffnung: ca. 1.800 cm²
  → Eine einzige Decksluke übererfüllt die Anforderung um Faktor 5,5

Aber: Zuluft allein reicht nicht — Abluft muss gewährleistet sein.
  Empfehlung: Decksluke (Zuluft) + Dorade-Ventilator oder Lüftungsgitter (Abluft)
```

### 10.2.3 Ventilationseffektivität verschiedener Lukentypen

| Lukentyp | Öffnungswinkel | Freie Fläche (% der Lukenöffnung) | Regenresistenz | Ventilations-Score |
|----------|---------------|-----------------------------------|----------------|-------------------|
| Decksluke mit Scharnier achtern | 70° | 65–75% | Gering bei Regen | 75 |
| Decksluke mit Scharnier vorn | 70° | 65–75% | Mittel (Windabweisung) | 80 |
| Schiebe-Decksluke | 100% offen | 45–55% (halbe Fläche) | Hoch (teilweise gedeckt) | 70 |
| Pilzlüfter (Dorade) | Permanent | 80–120 cm² | Sehr hoch | 40 |
| Lüftungsgitter fest | Permanent | 50–100 cm² | Hoch | 30 |

## 10.3 Strukturelle Ausschnittberechnung

### 10.3.1 Spannungskonzentration am Deckausschnitt

Ein Ausschnitt im Deck erzeugt eine Spannungskonzentration. Die Spannungsüberhöhung an den Ecken beträgt:

```
K_t = 1 + 2 × (a/r)

Wobei:
  K_t = Spannungskonzentrationsfaktor
  a = halbe Ausschnittlänge (mm)
  r = Eckenradius (mm)

Beispiel: Luke 500×500 mm, Eckenradius 40 mm:
  K_t = 1 + 2 × (250 / 40) = 13,5

→ Ohne Verstärkung: 13,5-fache Nennspannung an den Ecken!
→ Mindest-Eckenradius für Sandwich-Deck: r ≥ 50 mm (besser: ≥ 80 mm)
→ Aluminium-Deck: r ≥ 25 mm (Radius ≥ 3× Deckdicke)
```

### 10.3.2 Verstärkung des Deckausschnitts — Sandwich-Bauweise

**Schichtaufbau typisch GFK-Sandwich:**
1. Äußere GFK-Laminatschicht (Deckseite): 2–4 mm
2. Kernmaterial (PVC-Schaum, Balsa, Nomex): 15–30 mm
3. Innere GFK-Laminatschicht (Unterdeck): 2–3 mm
4. Gesamtdicke: 19–37 mm

**Verstärkungsmaßnahmen am Lukenausschnitt:**

| Maßnahme | Beschreibung | Mehrgewicht | Effekt |
|----------|-------------|-------------|--------|
| Kernverdichtung | Kernmaterial 80 mm um Ausschnitt durch GFK-Masse oder Sperrholz ersetzen | +0,5–1,2 kg | Verhindert Kernversagen unter Schraubenlast |
| Zusatzlaminat | 2–4 Lagen Biaxialgewebe (300 g/m²) überlappend | +0,8–1,5 kg | Erhöht Biegefestigkeit um Ausschnitt |
| Rahmeneinleger | Edelstahl- oder Alu-Rahmen eingeklebt/verschraubt | +1,5–3,0 kg | Verteilt Schraubenlast, dichtet Kernmaterial ab |
| Radiusverstärkung | Zusätzliches Roving in Eckenradien | +0,2–0,4 kg | Reduziert Spannungskonzentration K_t um 40–60% |

### 10.3.3 Schraubenanzahl und -verteilung

```
Empfohlener Schraubenabstand am Lukenflansch:
  GFK-Sandwich: 60–80 mm Achsmaß
  GFK-Massiv: 50–70 mm Achsmaß
  Aluminium: 40–60 mm Achsmaß

Schraubengröße:
  Luken bis 500×500 mm: M5 oder M6 Edelstahl A4
  Luken 500–800 mm: M6 Edelstahl A4
  Luken >800 mm: M6 oder M8 Edelstahl A4

Anzugsmoment:
  M5 A4 in GFK: 3–4 Nm (NICHT überdrehen!)
  M6 A4 in GFK: 5–7 Nm
  M6 A4 in Alu: 8–10 Nm
  M8 A4 in Alu: 12–16 Nm
```

### 10.3.4 AYDI-Strukturbewertung Lukenausschnitt

| Kriterium | Score 90–100 | Score 60–89 | Score <60 |
|-----------|-------------|-------------|-----------|
| Eckenradien | r ≥ 80 mm | r = 30–79 mm | r < 30 mm oder eckig |
| Kernverdichtung | Vollständig, sauber | Teilweise vorhanden | Fehlend oder beschädigt |
| Flanschbreite | ≥ 40 mm umlaufend | 25–39 mm | < 25 mm |
| Schraubenabstand | 60–80 mm gleichmäßig | Ungleichmäßig, aber <100 mm | > 100 mm oder fehlende Schrauben |
| Dichtmasse | Sauber aufgetragen, komprimiert | Teilweise lückenhaft | Fehlend oder verhärtet |

---

# 11. Einbau-/Austausch-Anleitung

## 11.1 Decksluke nachrüsten in Sandwich-Deck — Schritt-für-Schritt

### 11.1.1 Planung und Vorbereitung

**Benötigtes Werkzeug:**
- Stichsäge mit Hartmetallblatt (für GFK)
- Oberfräse mit Bündigfräser (für Kernmaterial)
- Winkelschleifer mit Schleifscheibe 80er Korn
- Bohrmaschine mit Stufenbohrer
- Abklebeband (Krepp, 50 mm breit)
- Messchieber, Wasserwaage, Anreißnadel
- Epoxidharz + Härter (langsam, z.B. West System 105/206)
- Füllstoff: Baumwollflocken oder Glasmikrosphären
- Biaxialgewebe 300 g/m², mindestens 1 m²
- Trennfolie (Mylar)
- Sikaflex 291 oder 3M 4200 (Abdichtung)
- Schrauben: M6×40 A4, entsprechende Anzahl
- Schablone (vom Lukenhersteller oder selbst gefertigt)

**Zeitaufwand:**
| Phase | Dauer | Bemerkung |
|-------|-------|-----------|
| Anzeichnen und Ausschneiden | 2–3 h | Sorgfalt vor Geschwindigkeit |
| Kernmaterial entfernen und vorbereiten | 2–3 h | Kernverdichtung aushärten lassen |
| Kernverdichtung (Epoxid aushärten) | 12–24 h | Über Nacht, nicht beschleunigen |
| Nachfräsen und Schleifen | 1–2 h | Flanschfläche plan schleifen |
| Zusatzlaminat (optional) | 2–3 h | Plus Aushärtezeit 12–24 h |
| Montage und Abdichtung | 2–3 h | Sikaflex muss Hautbildung zeigen |
| Gesamt | 2–3 Tage | Inkl. Aushärtezeiten |

### 11.1.2 Schritt 1 — Positionsbestimmung

1. **Unterdeck prüfen:** Kopf unter Deck stecken, Hindernisse identifizieren (Stringer, Versteifungen, Kabelkanäle, Schläuche)
2. **Pilobohrung:** 4 mm Bohrung von unten nach oben an geplanter Lukenmitte — prüfen, ob Position auf Deck sinnvoll
3. **Schablone positionieren:** Lukenschablone auf Deck ausrichten, Symmetrie zur Mittschiffslinie prüfen
4. **Abstand zu bestehenden Beschlägen:** Mindestens 100 mm zu Relingstützen, Klampen, Winschen
5. **Abstand zu Deckskante:** Mindestens 150 mm zur Schanzkante (strukturelle Integrität)
6. **Anreißen:** Mit wasserfestem Stift, Ausschnittlinie + 5 mm Übermaß für Flansch

### 11.1.3 Schritt 2 — Deckausschnitt

1. **Abkleben:** Beidseitig des Schnitts 100 mm breit abkleben (Gelcoat-Schutz)
2. **Ecken vorbohren:** An allen vier Ecken mit Lochsäge (∅ = 2× gewünschter Eckenradius, min. ∅ 60 mm) durchbohren
3. **Stichsäge ansetzen:** Von Eckbohrung zu Eckbohrung, langsamer Vorschub (max. 50% Geschwindigkeit)
4. **Unterstützung:** Ausschnittplatte von unten mit Helfer oder Klebeband stützen — darf nicht unkontrolliert herausfallen
5. **Kanten prüfen:** Keine Ausfransungen, Kernmaterial sichtbar, innere Laminatschicht intakt

### 11.1.4 Schritt 3 — Kernverdichtung

1. **Kernmaterial zurückfräsen:** Mit Oberfräse 25–35 mm tief und 30–40 mm breit ringsum den Ausschnitt (zwischen oberer und unterer GFK-Schicht)
2. **Hohlraum reinigen:** Staub absaugen, mit Aceton auswischen, trocknen lassen
3. **Epoxid-Füllmasse anmischen:** Epoxidharz + Härter + Baumwollflocken zu thixotroper Paste (Konsistenz wie Erdnussbutter)
4. **Hohlraum füllen:** Spachtel oder Spritze, blasenfrei, leicht überstehend
5. **Aushärten lassen:** Mindestens 12 h bei 20°C, besser 24 h
6. **Plan fräsen/schleifen:** Verdichtung bündig zur Decksoberfläche abtragen

### 11.1.5 Schritt 4 — Zusatzlaminat (empfohlen)

1. **Oberfläche anschleifen:** Gelcoat im Flanschbereich mit 80er Korn aufrauen
2. **Biaxialgewebe zuschneiden:** 4 Lagen, jede 15 mm kleiner als die vorherige (Stufenaufbau)
3. **Nassaufbau:** Epoxidharz auftragen, Gewebe einlegen, entlüften, nächste Lage
4. **Trennfolie und Lochblech:** Für gleichmäßigen Harzdruck
5. **Aushärten:** 24 h bei Raumtemperatur, danach schleifen

### 11.1.6 Schritt 5 — Flanschfläche vorbereiten

1. **Planheit prüfen:** Stahllineal über Flanschfläche legen — max. 1 mm Abweichung über gesamte Länge
2. **Schleifen:** 120er Korn bis gleichmäßig matte Oberfläche
3. **Bohrlöcher:** Nach Herstellerschablone vorbohren, Durchmesser = Schraubenkerndurchmesser
4. **Bohrlöcher versiegeln:** Jedes Bohrloch mit unverdünntem Epoxidharz benetzen und trocknen lassen (verhindert Feuchtigkeitseintritt in Kernmaterial)
5. **Passprobe:** Luke ohne Dichtmasse auflegen, Schrauben lose eindrehen, Ausrichtung prüfen

### 11.1.7 Schritt 6 — Abdichtung und Montage

1. **Sikaflex 291 auftragen:** Gleichmäßige Raupe (∅ 6–8 mm) auf Lukenflansch, innen und außen der Schraubenlinie
2. **Hinterfüllung:** Zweite Raupe auf die Decksflanschfläche — die beiden Raupen bilden eine geschlossene Kammer
3. **Luke aufsetzen:** Gleichmäßig andrücken, Dichtmasse muss ringsum leicht austreten
4. **Schrauben eindrehen:** Kreuzweise anziehen, Drehmoment beachten (M6 in GFK: 5–7 Nm)
5. **Überschüssige Dichtmasse:** Nach Hautbildung (ca. 2 h) sauber abschneiden, NICHT abwischen
6. **Aushärtezeit:** 48 h bis zur vollen Belastung, 24 h bis zur vorsichtigen Nutzung

### 11.1.8 Häufige Einbaufehler

| Fehler | Folge | Vermeidung |
|--------|-------|------------|
| Kein Eckenradius (eckiger Ausschnitt) | Rissbildung unter Last | Immer Eckbohrungen ≥ ∅ 60 mm |
| Kernverdichtung vergessen | Wassereinbruch ins Kernmaterial | Obligatorisch bei Sandwich |
| Bohrlöcher nicht versiegelt | Kernmaterial saugt Wasser | Epoxid-Versiegelung |
| Dichtmasse zu dünn | Undicht nach Temperaturschwankung | Raupendicke ≥ 6 mm |
| Schrauben zu fest | GFK-Gewinde zerstört | Drehmomentschlüssel verwenden |
| Silikon statt Polyurethan | Haftet nicht auf GFK | Nur PU-Dichtmasse (Sikaflex, 3M 4200) |
| Trockeneinbau ohne Passprobe | Luke sitzt schief | Immer trockene Passprobe zuerst |

## 11.2 Austausch einer bestehenden Decksluke

### 11.2.1 Demontage

1. **Alte Luke öffnen:** Alle Verschlüsse lösen, Luke in Offenstellung sichern
2. **Schrauben lösen:** Kreuzweise, bei Korrosion: Kriechöl (WD-40, Caramba) 24 h einwirken lassen
3. **Dichtmasse trennen:** Scharfes Messer zwischen Flansch und Deck, vorsichtig hebeln
4. **Luke abnehmen:** Mit Helfer, da Luken mit altem Dichtmittel fest kleben
5. **Alte Dichtmasse entfernen:** Kunststoffspachtel + Isopropanol, KEIN Schleifpapier auf Gelcoat
6. **Flanschfläche reinigen:** Aceton, anschleifen mit 180er Korn
7. **Zustand prüfen:** Kernmaterial freigelegt? Feucht? Delaminiert? → Ggf. Kernverdichtung erneuern

### 11.2.2 Passung prüfen bei Austausch-Luke

- **Gleicher Hersteller, gleiches Modell:** Direkt passend, Bohrlöcher wiederverwenden
- **Gleicher Hersteller, neueres Modell:** Häufig leicht abweichende Flanschmaße — neue Bohrlöcher erforderlich
- **Anderer Hersteller:** Ausschnittgröße und Flanschbreite vergleichen. Alte Löcher mit Epoxid-Füllmasse verschließen
- **Größere Luke als Bestand:** Ausschnitt vergrößern, dabei Kernverdichtung und Verstärkungslaminat erneuern

### 11.2.3 Kosten Luken-Austausch (Selbsteinbau vs. Werft)

| Leistung | Selbsteinbau | Werft |
|----------|-------------|-------|
| Material (Dichtmasse, Schrauben, Epoxid) | 50–120 EUR | 50–120 EUR |
| Arbeitszeit | 4–8 h (eigene Zeit) | 4–8 h × 80–120 EUR/h = 320–960 EUR |
| Gesamt (ohne Luke) | 50–120 EUR | 370–1.080 EUR |
| Risiko | Mittel (Erfahrung nötig) | Gering (Garantie) |

---

# 12. Lebensdauer und Alterungsmechanismen

## 12.1 Lebensdauer-Übersicht nach Komponente

| Komponente | Erwartete Lebensdauer | Einflussfaktoren | Austauschkosten |
|------------|----------------------|------------------|----------------|
| Acrylglas (PMMA) Scheibe | 15–20 Jahre | UV-Exposition, Reinigung, mechanische Belastung | 150–600 EUR |
| Polycarbonat (PC) Scheibe | 8–12 Jahre | UV-Beschichtung, Kratzer, Vergilbung | 120–500 EUR |
| Sicherheitsglas (ESG) | 25–35 Jahre | Mechanischer Schlag, Rahmenkorrosion | 300–900 EUR |
| EPDM-Dichtung | 5–8 Jahre | UV, Ozon, Kompression, Salz | 30–80 EUR |
| Neopren-Dichtung | 4–6 Jahre | UV-Empfindlichkeit, Verhärtung | 25–60 EUR |
| Silikon-Dichtung | 8–12 Jahre | Haftverlust, Veralgung | 15–40 EUR |
| Gasdruckfeder | 3–5 Jahre | Zyklen, UV, Salzluft, Temperatur | 25–60 EUR/Stück |
| Edelstahl-Scharnier (316L) | 15–25 Jahre | Spaltkorrosion, Salzablagerung | 40–120 EUR |
| Edelstahl-Scharnier (304) | 5–10 Jahre | Lochfraß, Teeflecken | 30–80 EUR |
| Alu-Rahmen eloxiert | 12–18 Jahre | Eloxalschicht-Abrieb, galvanische Korrosion | 200–500 EUR |
| Alu-Rahmen lackiert | 8–12 Jahre | Lackhaftung, Blasenbildung | 200–500 EUR |
| PU-Bettungsmasse (Sikaflex) | 10–15 Jahre | UV, Vibrationen, thermische Zyklen | 20–40 EUR/Kartusche |
| Moskitonetz-Einsatz | 5–8 Jahre | UV-Zerfall, mechanische Beschädigung | 40–120 EUR |
| Verdunkelungsrollo | 5–10 Jahre | Federermüdung, Stoffalterung | 60–180 EUR |

## 12.2 Alterungsmechanismen im Detail

### 12.2.1 Acrylglas (PMMA) — 15–20 Jahre

**Phase 1 (0–5 Jahre):** Minimale Veränderung. Mikrokratzer durch Reinigung akkumulieren. Lichtdurchlässigkeit sinkt von 92% auf ~90%.

**Phase 2 (5–10 Jahre):** Erste Crazing-Muster (Haarrisse) an Spannungspunkten. UV-bedingte leichte Gelbverfärbung messbar (Yellowness-Index +2–5). Randbereich durch Dichtungsdruck stärker betroffen.

**Phase 3 (10–15 Jahre):** Crazing breitet sich aus. Gelbverfärbung sichtbar (YI +5–12). Schlagfestigkeit sinkt um 20–30%. Biegerisse möglich bei starker Belastung.

**Phase 4 (15–20 Jahre):** Deutliche Vergilbung (YI >12). Sprödigkeit erhöht. Bruchgefahr bei Slamming. **Austausch empfohlen.**

**Beschleunigende Faktoren:**
- Reinigung mit Lösungsmitteln (Aceton zerstört PMMA sofort)
- Mechanische Spannungen durch falsches Anzugsmoment
- Kontakt mit bestimmten Dichtmassen (manche Silikone greifen PMMA an)
- Tropische UV-Exposition reduziert Lebensdauer um 30–40%

### 12.2.2 Dichtungen — 5–8 Jahre (EPDM)

**Haupt-Alterungsmechanismen:**

| Mechanismus | Ursache | Anzeichen | Zeitrahmen |
|-------------|---------|-----------|------------|
| Druckverformungsrest | Permanente Kompression | Dichtung bleibt flach nach Öffnen | 3–6 Jahre |
| UV-Degradation | Sonneneinstrahlung | Rissbildung, Verhärtung | 4–8 Jahre |
| Ozonrissbildung | Ozonexposition | Feine parallele Risse | 5–10 Jahre |
| Salzablagerung | Seewasser | Weiße Kristalle, Reibung | Permanent |
| Biofilm / Algen | Feuchtigkeit | Grünlich-schwarzer Belag | 1–3 Jahre |

**AYDI-Wartungsintervall:** Dichtungsinspektion alle 12 Monate, Austausch bei Druckverformungsrest >40% oder sichtbaren Rissen. Silikonspray (NICHT -öl) alle 6 Monate auf Dichtlippen.

### 12.2.3 Gasdruckfedern — 3–5 Jahre

**Versagensmechanismen:**
1. **Gasverlust:** Schleichende Leckage am Kolbenstangenausgang. Druckverlust 5–15% pro Jahr typisch. Folge: Luke fällt langsam zu, dann gar nicht mehr gehalten.
2. **Kolbenstangenkorrosion:** Salzluft greift Chromschicht an. Raue Oberfläche beschädigt Dichtung. Beschleunigt Gasverlust.
3. **Lagerverschleiß:** Kugelköpfe an Befestigungspunkten erodieren. Spiel nimmt zu, Geräuschentwicklung.
4. **Temperaturfehler:** Gasdruckfedern sind temperaturabhängig. Bei 40°C: +20% Kraft, bei 0°C: -20% Kraft. Extreme können zu Überlast oder Versagen führen.

**Prüfmethode:**
- Luke auf 90° öffnen, loslassen: Muss mindestens 30 s in Position bleiben
- Fällt die Luke innerhalb von 10 s: Sofortiger Austausch
- Fällt die Luke langsam (10–30 s): Austausch planen (nächste Saison)

## 12.3 AYDI-Altersberechnung

```
Alter_effektiv = Alter_kalendarisch × K_klima × K_nutzung × K_wartung

Korrekturfaktoren:
  K_klima:
    Nordeuropa (Ostsee, Nordsee): 1,0
    Mittelmeer: 1,3
    Tropen / Karibik: 1,6
    Süßwasser / Binnenrevier: 0,8

  K_nutzung:
    Gelegenheitssegler (<30 Tage/Jahr): 0,8
    Normalnutzung (30–90 Tage/Jahr): 1,0
    Vollzeitliveaboard: 1,4
    Charter: 1,8

  K_wartung:
    Regelmäßig (jährliche Inspektion): 0,8
    Gelegentlich: 1,0
    Vernachlässigt: 1,5

Beispiel: 8 Jahre alte Luke, Mittelmeer, Charter, gelegentliche Wartung
  Alter_eff = 8 × 1,3 × 1,8 × 1,0 = 18,7 effektive Jahre
  → Dichtungen: weit über Lebensdauer → Sofortiger Austausch
  → Acrylglas: nahe Lebensdauerende → Inspektion auf Crazing
  → Gasdruckfedern: 3–4× über Lebensdauer → sicher defekt
```

---

# 13. Fehlerbild-Atlas

## 13.1 FB-DL-001: Gerissenes Acrylglas

**Erscheinungsbild:** Sternförmiger oder linearer Riss im Acrylglas der Decksluke. Riss durchgehend oder nur oberflächlich (Crazing). Oft ausgehend von Schraubenloch oder Eckenbereich.
**Ursache:** Mechanische Überlastung (Slamming, Betreten), Spannungsrisskorrosion (Kontakt mit Lösungsmitteln), falsches Anzugsmoment der Rahmenschrauben, thermische Spannungen bei dunkler Tönung.
**Risiko:** HOCH — bei Wellengang kann Scheibe komplett brechen, Wassereinbruch unter Deck.
**AYDI-Score:** 10–25 (je nach Risslänge und -tiefe)
**Confidence:** visual_high (Risse klar erkennbar auf Fotos)
**Maßnahme:** Rissstopp-Bohrung (∅ 3 mm am Rissende) als Sofortmaßnahme. Mittelfristig: Scheibenaustausch.
**Kosten:** Scheibenaustausch 150–600 EUR Material, 2–4 h Arbeit.
**Häufigkeit:** 12% aller Luken >15 Jahre, 25% aller Luken >20 Jahre.
**AYDI-Klassifikation:** CRITICAL wenn durchgehend, WARNING wenn oberflächlich.
**Verwechslungsgefahr:** Kratzer (oberflächlich, keine Tiefe) vs. Crazing (Netzwerk feiner Risse) vs. Riss (einzelner durchgehender Bruch).
**Prävention:** Korrekte Anzugsmomente, kein Betreten, keine Lösungsmittel, UV-Schutzfolie.

## 13.2 FB-DL-002: Versagende Dichtung

**Erscheinungsbild:** Wasserflecken unter Luke, Salzablagerungen am Rahmeninnenrand, feuchter oder schimmeliger Geruch in Kabine. Dichtung zeigt Risse, Verformung oder Ablösung.
**Ursache:** Alterung (Druckverformungsrest >40%), UV-Degradation, falscher Dichtungstyp, mechanische Beschädigung durch Fremdkörper im Dichtspalt.
**Risiko:** MITTEL bis HOCH — progressiver Wassereinbruch, Schimmelbildung, Elektronikschäden.
**AYDI-Score:** 30–55 (je nach Leckrate)
**Confidence:** visual_medium (Wasserflecken sichtbar, Dichtungszustand teils verdeckt)
**Maßnahme:** Dichtung reinigen und Silikonspray auftragen (temporär). Austausch der Dichtung (definitiv).
**Kosten:** Dichtungssatz 30–80 EUR, Selbsteinbau 1–2 h.
**Häufigkeit:** 30% aller Luken >5 Jahre, 60% aller Luken >8 Jahre.
**AYDI-Klassifikation:** WARNING standardmäßig, CRITICAL bei aktivem Wassereintritt.
**Verwechslungsgefahr:** Kondenswasser (symmetrisch, jahreszeitenabhängig) vs. Leckage (einseitig, bei Regen/Seegang).
**Prävention:** Halbjährliche Silikonpflege, Luken bei Nichtgebrauch leicht offen (Dichtungsentlastung).

## 13.3 FB-DL-003: Gebrochenes Scharnier

**Erscheinungsbild:** Luke lässt sich nicht vollständig öffnen oder hängt schief. Sichtbarer Riss oder Bruch im Scharnierkörper. Ausgerissene Scharnierbolzen.
**Ursache:** Materialermüdung (Edelstahl 304 statt 316L), Korrosion am Scharnierbolzen, Überbelastung durch Wind (Luke offen bei Starkwind), fehlende Schmierung.
**Risiko:** MITTEL — Luke kann bei Seegang unkontrolliert zuschlagen, Verletzungsgefahr.
**AYDI-Score:** 25–45
**Confidence:** visual_high (mechanische Schäden gut sichtbar)
**Maßnahme:** Scharnier austauschen, dabei Schraubenlöcher prüfen und ggf. neu setzen. Beide Scharniere gleichzeitig wechseln.
**Kosten:** Scharniersatz 40–120 EUR, Einbau 1–2 h.
**Häufigkeit:** 8% aller Luken >10 Jahre.
**AYDI-Klassifikation:** WARNING, CRITICAL wenn Luke nicht mehr sicher arretierbar.
**Verwechslungsgefahr:** Verbogenes Scharnier (Deformation ohne Bruch) vs. gebrochenes Scharnier (Materialversagen).
**Prävention:** Jährliche Schmierung mit Teflon-Spray, 316L-Material spezifizieren, Windstützen verwenden.

## 13.4 FB-DL-004: Blockierte Gasdruckfeder

**Erscheinungsbild:** Luke lässt sich nur mit erhöhtem Kraftaufwand öffnen oder fällt unkontrolliert zu. Gasdruckfeder zeigt keinen Widerstand oder ist komplett steif.
**Ursache:** Gasverlust (Dichtungsverschleiß), Kolbenstangenkorrosion, Verharzung des Ölfilms, Temperaturfehler (extreme Kälte/Hitze).
**Risiko:** MITTEL — Verletzungsgefahr durch zuschlagende Luke (bis 15 kg Gewicht, Beschleunigung durch Seegang).
**AYDI-Score:** 35–55
**Confidence:** visual_low (Defekt oft nicht sichtbar, nur funktional prüfbar)
**Maßnahme:** Gasdruckfeder(n) austauschen. Immer paarweise wechseln. Auf korrekte Nennkraft achten (N-Angabe).
**Kosten:** 2× Gasdruckfeder 50–120 EUR, Einbau 30–60 min.
**Häufigkeit:** 50% aller Gasdruckfedern >4 Jahre, 80% >6 Jahre.
**AYDI-Klassifikation:** WARNING.
**Verwechslungsgefahr:** Schwergängiges Scharnier vs. defekte Gasdruckfeder — Differenzialdiagnose durch Abklemmen der Feder.
**Prävention:** Kolbenstange mit Silikonspray pflegen, Schutzkappe gegen Salzluft, alle 3–4 Jahre präventiv tauschen.

## 13.5 FB-DL-005: Delaminierter Lukenrahmen

**Erscheinungsbild:** Rahmenecken lösen sich, sichtbarer Spalt zwischen Rahmenprofilen. Bei Alu-Rahmen: aufquellende Klebe-/Schweißnaht. Bei GFK-Rahmen: Laminat blättert ab.
**Ursache:** Galvanische Korrosion (Alu-Rahmen auf Edelstahlschrauben ohne Isolation), Wassereinbruch in Rahmenhohlprofil, Frost-Tau-Zyklen (Winterlager ohne Schutz), UV-Degradation der Klebenaht.
**Risiko:** HOCH — Strukturversagen des Rahmens führt zu Undichtigkeit und kann Lukendeckel lösen.
**AYDI-Score:** 15–35
**Confidence:** visual_medium (Delamination nicht immer sofort sichtbar)
**Maßnahme:** Leichte Fälle: Epoxid-Reparatur mit Klemmung. Schwere Fälle: Kompletter Rahmenaustausch.
**Kosten:** Reparatur 80–200 EUR, Austausch 200–600 EUR + Einbau.
**Häufigkeit:** 15% aller Alu-Rahmenluken >12 Jahre.
**AYDI-Klassifikation:** CRITICAL bei struktureller Beeinträchtigung.
**Verwechslungsgefahr:** Kosmetischer Lackabplatzer vs. strukturelle Delamination — Klopftest mit Münze offenbart Hohlstellen.
**Prävention:** Isolationsscheiben zwischen ungleichen Metallen, Drainagelöcher in Rahmenprofilen, Rahmenversiegelung.

## 13.6 FB-DL-006: Ausgelaufene Bettungsmasse

**Erscheinungsbild:** Bettungsmasse quillt unter Lukenflansch hervor, ist verhärtet, gerissen oder von Deck gelöst. Sichtbare Lücken zwischen Flansch und Deck.
**Ursache:** Alterung der PU-Bettung (15+ Jahre), UV-Exposition der sichtbaren Kante, thermische Ausdehnung/Kontraktion, falsche Dichtmasse verwendet (Silikon auf GFK).
**Risiko:** MITTEL — Schleichender Wassereinbruch ins Sandwich-Kernmaterial, Langzeitschaden am Deck.
**AYDI-Score:** 35–55
**Confidence:** visual_high (Bettungszustand gut sichtbar am Flanschrand)
**Maßnahme:** Luke demontieren, alte Bettung komplett entfernen, Flanschfläche reinigen, neue PU-Bettung (Sikaflex 291) auftragen, Luke neu montieren.
**Kosten:** Material 40–80 EUR, Arbeit 4–8 h (Selbst) oder 320–960 EUR (Werft).
**Häufigkeit:** 20% aller Luken >10 Jahre, 50% aller Luken >15 Jahre.
**AYDI-Klassifikation:** WARNING, CRITICAL wenn Deck-Kernmaterial bereits feucht.
**Verwechslungsgefahr:** Überschüssige Bettung (Einbaufehler, harmlos) vs. ausgetretene Bettung (Alterung, problematisch).
**Prävention:** UV-beständige Bettungsmasse, Flanschrand mit Gelcoat-Farbton abdecken.

## 13.7 FB-DL-007: UV-Vergilbung

**Erscheinungsbild:** Acrylglas zeigt gelbliche bis bräunliche Verfärbung, besonders an Sonnenseite. Lichtdurchlässigkeit reduziert. Kann mit Verschmutzung verwechselt werden.
**Ursache:** UV-induzierte Photooxidation des PMMA-Polymers. Verstärkt durch fehlende UV-Stabilisatoren, tropische Breiten, dunkle Tönung (Wärmeabsorption).
**Risiko:** GERING (kosmetisch) bis MITTEL (reduzierte Festigkeit bei fortgeschrittener Degradation).
**AYDI-Score:** 55–75
**Confidence:** visual_medium (Vergilbung kann auf Fotos schwer von Weißabgleich-Fehlern unterschieden werden)
**Maßnahme:** Leicht: Politur mit Acrylglas-Polierpaste (Novus #2). Mittel: Nasschliff 1500er + Politur. Stark: Scheibenaustausch.
**Kosten:** Politur 15–30 EUR, Scheibenaustausch 150–600 EUR.
**Häufigkeit:** 40% aller Acrylglas-Luken >10 Jahre.
**AYDI-Klassifikation:** INFO bei leichter Vergilbung, WARNING bei YI >10.
**Verwechslungsgefahr:** Vergilbung (gleichmäßig, nicht abwischbar) vs. Verschmutzung (ungleichmäßig, abwischbar) vs. Algenfilm (grünlich, feucht).
**Prävention:** UV-Schutzfolie (3M, Llumar), Lukenabdeckung bei Nichtgebrauch, helles Acryl statt getöntes.

## 13.8 FB-DL-008: Spannungsrisse um Befestigungslöcher

**Erscheinungsbild:** Sternförmige oder radiale Risse ausgehend von Schraubenlöchern im Acrylglas oder GFK-Flansch. Oft 10–40 mm lang. Mehrere Löcher gleichzeitig betroffen.
**Ursache:** Übermäßiges Anzugsmoment der Schrauben, fehlende Unterlegscheiben, zu kleiner Lochdurchmesser (Spiel fehlt), thermische Spannungen durch unterschiedliche Ausdehnungskoeffizienten.
**Risiko:** HOCH — Risse breiten sich unter Belastung aus, Luke kann sich lösen.
**AYDI-Score:** 15–35
**Confidence:** visual_high (Risse um Schrauben klar erkennbar)
**Maßnahme:** Schrauben lösen, Rissstopp-Bohrungen setzen, größere Unterlegscheiben verwenden, Anzugsmoment reduzieren. Bei >3 betroffenen Löchern: Scheibe/Flansch austauschen.
**Kosten:** Rissstopp + Unterlegscheiben 20–40 EUR, Scheibenaustausch 150–600 EUR.
**Häufigkeit:** 18% aller Luken, besonders bei DIY-Einbau.
**AYDI-Klassifikation:** CRITICAL bei mehreren Rissen oder Risslänge >30 mm.
**Verwechslungsgefahr:** Spannungsriss (radial von Loch ausgehend) vs. Materialriss (unabhängig von Löchern).
**Prävention:** Drehmomentschlüssel, Lochdurchmesser = Schraubendurchmesser + 1,5 mm, Neopren-Unterlegscheiben.

## 13.9 FB-DL-009: Rahmenkorrosion

**Erscheinungsbild:** Weiße pulverige Ablagerungen (Aluminium), braune Flecken (Edelstahl 304), grüne Patina (Bronze/Messing). Lochfraß, Spaltkorrosion an verdeckten Bereichen.
**Ursache:** Galvanische Korrosion (unterschiedliche Metalle), Spaltkorrosion (stagnierende Feuchtigkeit unter Dichtung), chloridinduzierter Lochfraß (Salzwasser auf 304er Stahl).
**Risiko:** MITTEL bis HOCH — Tragfähigkeit des Rahmens reduziert, Dichtfläche beschädigt.
**AYDI-Score:** 25–55
**Confidence:** visual_high (Korrosionsprodukte klar erkennbar)
**Maßnahme:** Oberflächliche Korrosion: Reinigung mit Oxalsäure (Edelstahl) oder Phosphorsäure (Alu), dann Versiegelung. Tiefe Korrosion: Rahmenaustausch.
**Kosten:** Reinigung 20–50 EUR, Rahmenaustausch 200–600 EUR + Einbau.
**Häufigkeit:** 35% aller 304er-Edelstahl-Luken >8 Jahre, 10% aller 316L-Luken >15 Jahre.
**AYDI-Klassifikation:** WARNING bei Oberfläche, CRITICAL bei Lochfraß >1 mm Tiefe.
**Verwechslungsgefahr:** Teeflecken (kosmetisch, oberflächlich) vs. Lochfraß (strukturell, tiefgehend) — Prüfung mit Tiefenmessschieber.
**Prävention:** 316L-Material spezifizieren, galvanische Isolation, regelmäßige Süßwasserspülung.

## 13.10 FB-DL-010: Verzogene Scheibe

**Erscheinungsbild:** Lukendeckel liegt nicht plan auf Rahmen, Spalt sichtbar. Beim Schließen federt Deckel zurück. Dichtung wird nur teilweise komprimiert.
**Ursache:** Thermische Verformung (dunkle Tönungen absorbieren Wärme), einseitige Sonneneinstrahlung, zu dünnes Material, falsche Lagerung (Luke offen über Monate).
**Risiko:** MITTEL — Undichtigkeit im Spaltbereich, ungleichmäßiger Dichtungsverschleiß.
**AYDI-Score:** 40–60
**Confidence:** visual_medium (Verzug auf Fotos schwer quantifizierbar)
**Maßnahme:** Leicht (<2 mm): Dichtung durch stärkere Profilhöhe ersetzen. Mittel (2–5 mm): Thermische Rückformung (Heißluftfön, 80°C, langsam). Stark (>5 mm): Scheibenaustausch.
**Kosten:** Dichtungsanpassung 30–80 EUR, Rückformung 50–100 EUR, Austausch 150–600 EUR.
**Häufigkeit:** 10% aller Acrylglas-Luken >8 Jahre, 25% bei getönten Scheiben.
**AYDI-Klassifikation:** WARNING.
**Verwechslungsgefahr:** Verzogene Scheibe vs. verzogener Rahmen vs. unebene Deckfläche — Stahllineal-Test auf verschiedenen Elementen.
**Prävention:** Helle Acrylfarbe bevorzugen, Luke bei Nichtgebrauch geschlossen halten, Sonnensegel.

## 13.11 FB-DL-011: Fehlendes Moskitonetz

**Erscheinungsbild:** Lukenöffnung ohne Insektenschutz, improvisierte Lösungen (Klettband, loses Netz). Steckmückenbefall unter Deck.
**Ursache:** Netz im Lieferumfang nicht enthalten (günstige Luken), Original-Netz beschädigt und nicht ersetzt, falsche Größe nachgekauft.
**Risiko:** GERING (Komfort) — kein strukturelles oder sicherheitsrelevantes Problem.
**AYDI-Score:** 65–80
**Confidence:** visual_high (An-/Abwesenheit klar erkennbar)
**Maßnahme:** Passenden Moskitonetz-Einsatz vom Lukenhersteller nachbestellen. Alternativ: Magnetrahmen-Lösung (universell, z.B. Oceanair).
**Kosten:** Original-Einsatz 40–120 EUR, Universallösung 30–80 EUR.
**Häufigkeit:** 25% aller Yachten in Mittelmeer/Tropen-Revieren.
**AYDI-Klassifikation:** INFO.
**Verwechslungsgefahr:** N/A — eindeutiges Fehlerbild.
**Prävention:** Bei Lukenkauf auf inkludierten Moskito-Einsatz achten, Ersatzteile frühzeitig bestellen.

## 13.12 FB-DL-012: Deckweichstelle um Luke

**Erscheinungsbild:** Deck gibt nach bei Betreten im Bereich 50–200 mm um Lukenflansch. Hörbares Knacken oder Knirschen. Möglicherweise sichtbare Risse in Gelcoat.
**Ursache:** Wassereinbruch ins Sandwich-Kernmaterial durch undichte Bettung oder unversiegelte Bohrlöcher. Kernmaterial (besonders Balsa) verfault, PVC-Schaum verliert Stützwirkung.
**Risiko:** KRITISCH — Strukturelle Deckintegrität gefährdet, Luke kann sich bei Belastung lösen, Sturzgefahr.
**AYDI-Score:** 5–20
**Confidence:** visual_low (Weichstelle auf Fotos nicht erkennbar, erfordert physische Prüfung), measured bei Feuchtemessung
**Maßnahme:** Sofort: Bereich nicht betreten, Luke provisorisch abdichten. Reparatur: Deckplatte öffnen, feuchtes Kernmaterial entfernen, trocknen (Wärmelampe, 2–5 Tage), neues Kernmaterial einsetzen, Nachlamination, neue Luke montieren.
**Kosten:** 800–3.500 EUR je nach Umfang (Material + Werft).
**Häufigkeit:** 8% aller Sandwich-Decks >15 Jahre, 20% bei vernachlässigter Wartung.
**AYDI-Klassifikation:** CRITICAL.
**Verwechslungsgefahr:** Deckweichstelle (lokal um Luke) vs. generelle Deck-Delamination (großflächig) — Klopftest mit Münze: dumpf = feucht/delaminiert, hell = intakt.
**Prävention:** Bohrlöcher versiegeln, Bettung regelmäßig prüfen, Feuchtemessung alle 2–3 Jahre.

---

# 14. Fehlerbehebungs-Leitfaden

## 14.1 Problem: Luke undicht bei Regen

**Symptom:** Wassertropfen unter Luke, Wasserflecken an Decksunterseite, feuchter Geruch in Kabine.

**Diagnose-Schritte:**
1. Luke von außen visuell prüfen: Bettung, Dichtung, Rahmenzustand
2. Wassertest: Mit Gartenschlauch (kein Druck!) gezielt einzelne Flanschseiten besprühen — Leckstelle identifizieren
3. Dichtung prüfen: Dichtlippe mit Finger abfahren — Risse, Verhärtung, Verformungsrest?
4. Verschlüsse prüfen: Alle Hebel vollständig schließen — ausreichende Kompression?

**Lösung nach Ursache:**

| Ursache | Lösung | Aufwand | Kosten |
|---------|--------|---------|--------|
| Dichtung verhärtet/gerissen | Dichtung austauschen | 1–2 h | 30–80 EUR |
| Bettung rissig/gelöst | Luke neu betten (Sikaflex 291) | 4–8 h | 40–80 EUR |
| Verschluss greift nicht | Verschlussmechanismus einstellen/erneuern | 1–2 h | 20–60 EUR |
| Acrylglas gerissen | Scheibe austauschen | 2–4 h | 150–600 EUR |
| Rahmen korrodiert/verzogen | Rahmen austauschen | 4–8 h | 200–600 EUR |

## 14.2 Problem: Luke lässt sich nicht öffnen

**Symptom:** Luke klemmt, Verschlüsse lassen sich nicht lösen, Scharnier blockiert.

**Diagnose-Schritte:**
1. Verschlusshebel prüfen: Korrosion, Verformung, Blockade?
2. Dichtung prüfen: Verklebt durch Algen oder UV-Degradation?
3. Scharnier prüfen: Korrosion, Fremdkörper, fehlende Schmierung?
4. Rahmenverformung: Thermischer Verzug? Mechanische Einwirkung?

**Lösung nach Ursache:**

| Ursache | Lösung | Aufwand | Kosten |
|---------|--------|---------|--------|
| Korrodierter Verschluss | Kriechöl, ggf. Verschluss erneuern | 30 min–1 h | 15–50 EUR |
| Verklebte Dichtung | Silikonspray zwischen Dichtung und Rahmen | 15 min | 5–10 EUR |
| Festsitzendes Scharnier | Schmierung, Reinigung, ggf. Austausch | 1–2 h | 10–120 EUR |
| Thermischer Verzug | Abkühlen lassen, ggf. Scheibenaustausch | 0–4 h | 0–600 EUR |

## 14.3 Problem: Luke beschlägt von innen

**Symptom:** Kondenswasser auf Innenseite der Acrylglasscheibe, Tropfenbildung auf Polster/Kojen.

**Diagnose-Schritte:**
1. Unterscheiden: Kondenswasser (gleichmäßig, temperaturabhängig) vs. Leckage (lokal, wetterabhängig)
2. Temperaturdifferenz prüfen: Innen warm/feucht + außen kalt = Kondensation
3. Belüftung prüfen: Ist Luftzirkulation möglich?
4. Feuchtigkeitsquelle: Nasse Kleidung, Kochen, Atemluft, Bilgewasser?

**Lösung:**

| Ursache | Lösung | Aufwand | Kosten |
|---------|--------|---------|--------|
| Fehlende Ventilation | Zwangsbelüftung einbauen (12V-Lüfter) | 2–3 h | 40–120 EUR |
| Keine Luftzirkulation | Luken-Lüftungsstellung ermöglichen | 0 h | 0 EUR |
| Hohe Innenfeuchte | Luftentfeuchter (elektrisch oder Granulat) | 0 h | 20–150 EUR |
| Wärmebrücke Alu-Rahmen | Alu-Rahmen innen isolieren (Armaflex 6 mm) | 1–2 h | 15–30 EUR |

## 14.4 Problem: Gasdruckfeder hält Luke nicht

**Symptom:** Luke sackt langsam ab oder fällt unkontrolliert zu, Gasdruckfeder zeigt keinen Widerstand.

**Diagnose-Schritte:**
1. Temperatur prüfen: Bei Kälte (<5°C) kann Kraft vorübergehend reduziert sein
2. Kolbenstange prüfen: Korrosion, Kratzer, Ölaustritt?
3. Kugelköpfe prüfen: Spiel, Ausbruch, Korrosion?
4. Einbaulage prüfen: Gasdruckfeder muss mit Kolbenstange nach unten montiert sein

**Lösung:**

| Ursache | Lösung | Aufwand | Kosten |
|---------|--------|---------|--------|
| Gasverlust (Alterung) | Beide Federn austauschen | 30–60 min | 50–120 EUR |
| Kolbenstangenkorrosion | Sofort austauschen | 30–60 min | 50–120 EUR |
| Kugelkopf defekt | Kugelkopf-Aufnahme erneuern | 1 h | 10–30 EUR |
| Falsche Einbaulage | Umdrehen (Kolbenstange unten) | 15 min | 0 EUR |
| Falsche Nennkraft | Feder mit korrekter Newton-Angabe bestellen | 30 min | 25–60 EUR |

## 14.5 Problem: Deck weich um Luke herum

**Symptom:** Deck gibt nach beim Betreten neben der Luke, Knackgeräusche, Gelcoat-Risse.

**Diagnose-Schritte:**
1. Klopftest: Mit Münze/kleinem Hammer ringsum klopfen — dumpfer Klang = feuchtes Kernmaterial
2. Feuchtemessung: Tramex oder ähnliches Messgerät — Werte >10% = feucht
3. Optische Prüfung: Gelcoat-Risse, Verfärbungen, Ausblühungen
4. Befestigungsprüfung: Schrauben lose? Flansch angehoben?

**Lösung:**

| Schweregrad | Lösung | Aufwand | Kosten |
|-------------|--------|---------|--------|
| Leicht (lokal, <100 mm) | Epoxid-Injektion durch Bohrlöcher | 3–5 h | 80–200 EUR |
| Mittel (100–300 mm ringsum) | Kernmaterial sektionsweise erneuern | 2–4 Tage | 500–1.500 EUR |
| Schwer (>300 mm, nass) | Deckssektion erneuern, neue Luke | 1–2 Wochen | 2.000–5.000 EUR |
| Kritisch (strukturell kompromittiert) | Professionelle Werft-Reparatur | 2–4 Wochen | 3.000–8.000 EUR |

**AYDI-Empfehlung:** Bei Deckweichstellen immer Feuchtemessung durchführen. Visuelle Analyse allein reicht nicht (confidence: visual_low). Feuchtemessung erhöht Confidence auf measured.

---

# 15. FAQ — Häufig gestellte Fragen

## DL-001: Welche Lukengröße brauche ich als Fluchtluke?
**Antwort:** Nach ISO 12216 mindestens 400×520 mm lichte Öffnung. Für CE-Kategorie A/B ist eine Fluchtluke in jedem separat zugänglichen Raum vorgeschrieben. AYDI prüft dies automatisch im Compliance-Modul.

## DL-002: Acrylglas oder Polycarbonat — was ist besser?
**Antwort:** Acrylglas (PMMA) hat höhere Lichtdurchlässigkeit (92% vs. 88%), bessere UV-Beständigkeit und kratzfestere Oberfläche. Polycarbonat ist schlagfester (250× stärker), aber vergilbt schneller. Empfehlung: Acrylglas für Decksluken (UV-Exposition), Polycarbonat nur für stark schlaggefährdete Bereiche.

## DL-003: Wie oft müssen Dichtungen getauscht werden?
**Antwort:** EPDM-Dichtungen alle 5–8 Jahre, Neopren alle 4–6 Jahre. Halbjährliche Pflege mit Silikonspray verlängert die Lebensdauer um 20–30%. AYDI berechnet den effektiven Dichtungszustand basierend auf Alter, Revier und Nutzungsintensität.

## DL-004: Kann ich eine Luke selbst einbauen?
**Antwort:** Ja, mit handwerklichem Geschick und richtigen Werkzeugen (siehe Kapitel 11). Kritisch: Kernverdichtung bei Sandwich-Decks und korrekte Abdichtung. Fehler hier führen zu Langzeitschäden. Bei Unsicherheit: Werft beauftragen (Mehrkosten 320–960 EUR).

## DL-005: Welche Dichtmasse verwende ich?
**Antwort:** Polyurethan-basiert: Sikaflex 291 (Standard), 3M 4200 (etwas flexibler). NIEMALS Silikon auf GFK — haftet nicht dauerhaft und verunreinigt die Oberfläche für spätere PU-Anwendung. Butyldichtband als Alternative bei Aluminium-Rahmen.

## DL-006: Wie erkenne ich ob mein Deck um die Luke feucht ist?
**Antwort:** Klopftest (dumpfer Klang = feucht), Feuchtemessgerät (Tramex, >10% = kritisch), Gelcoat-Risse oder Verfärbungen ringsum. AYDI kann Deckweichstellen nicht zuverlässig per Foto erkennen (confidence: visual_low) und empfiehlt immer physische Prüfung.

## DL-007: Welche Schrauben für die Lukenmontage?
**Antwort:** Ausschließlich Edelstahl A4 (316L). Größe M5 oder M6 für Standard-Luken, M8 für große Luken >800 mm. Neopren-Unterlegscheiben verwenden. Bohrlöcher immer mit Epoxid versiegeln (Kernmaterial-Schutz).

## DL-008: Muss jede Luke von außen zu öffnen sein?
**Antwort:** Fluchtluken ja — sie müssen von beiden Seiten ohne Werkzeug zu öffnen sein. Standard-Decksluken: keine Anforderung, aber Empfehlung für Sicherheit. AYDI prüft Öffnungsrichtung im Compliance-Modul.

## DL-009: Wie verhindere ich Kondenswasser an der Luke?
**Antwort:** Drei Ansätze: 1) Ventilation verbessern (Lüfter, Dorade), 2) Alu-Rahmen innen isolieren (Armaflex), 3) Innenfeuchte reduzieren (Entfeuchter). Kondenswasser ist kein Lukendefekt sondern ein Klimaproblem.

## DL-010: Kann ich getönte gegen klare Luken tauschen?
**Antwort:** Ja, solange Flanschmaße und Dicke identisch sind. Getönte Scheiben reduzieren Lichteinfall um 30–50%, heizen sich aber stärker auf (Verformungsrisiko). Klare Scheiben mit Rollos/Jalousien sind die bessere Lösung.

## DL-011: Was kostet eine komplette Decksluke?
**Antwort:** Budgetbereich (Gebo, Vetus): 180–400 EUR. Mittelklasse (Lewmar Standard): 350–700 EUR. Premium (Lewmar Ocean, Goiot Cristal): 600–1.200 EUR. Superyacht (Trend Marine, Freeman): 2.000–8.000 EUR. Jeweils ohne Einbau.

## DL-012: Wie viele Gasdruckfedern braucht meine Luke?
**Antwort:** Luken bis 500×500 mm: 1–2 Federn. Luken 500–800 mm: 2 Federn. Luken >800 mm: 2–4 Federn. Nennkraft pro Feder: Lukengewicht × 0,6 ÷ Anzahl Federn. Immer paarweise wechseln.

## DL-013: Welcher Öffnungswinkel ist ideal?
**Antwort:** 60–70° für gute Ventilation ohne Windanfälligkeit. >80° erhöht die Windlast erheblich. <45° reduziert die Ventilationsleistung um >40%. Windstützen verhindern unkontrolliertes Aufschlagen.

## DL-014: Darf ich auf Decksluken treten?
**Antwort:** Nur wenn vom Hersteller explizit als begehbar klassifiziert. Typische Acrylglas-Luken: NEIN. Luken mit 15+ mm Sicherheitsglas und entsprechendem Rahmen: bedingt. AYDI bewertet die Begehbarkeit basierend auf Material, Dicke und Rahmenkonstruktion.

## DL-015: Wie reinige ich Acrylglas richtig?
**Antwort:** Reichlich klares Wasser, weiches Tuch (Mikrofaser). Bei Salzkrusten: einweichen lassen, NICHT reiben. Keine Lösungsmittel (Aceton, Benzin, Spiritus — zerstören PMMA!). Spezialreiniger: Novus #1, Burnus Plexiklar. Politur: Novus #2 bei leichten Kratzern.

## DL-016: Sind billige Luken ihr Geld wert?
**Antwort:** No-Name-Luken unter 150 EUR haben typischerweise: dünneres Acryl (6 statt 10 mm), Edelstahl 304 statt 316L, minderwertige Dichtungen, keine Ersatzteilversorgung. Lebensdauer 5–8 statt 15–20 Jahre. AYDI empfiehlt mindestens Markenprodukte der Mittelklasse.

## DL-017: Kann ich eine runde Luke gegen eine eckige tauschen?
**Antwort:** Grundsätzlich ja, aber der Deckausschnitt muss angepasst werden. Runde Ausschnitte haben geringere Spannungskonzentration — der neue eckige Ausschnitt braucht größere Eckenradien und ggf. Verstärkung. Werft-Arbeit empfohlen.

## DL-018: Wie dichte ich eine Luke provisorisch ab?
**Antwort:** Für die Überfahrt: Selbstverschweißendes Dichtband (Rescue Tape) um Flanschrand. Für länger: Butyldichtband auf gereinigten Flansch drücken. Für Notfall: Segelmacher-Tape (Dacron) über geschlossene Luke. Alles nur temporär!

## DL-019: Warum beschlagen manche Luken und andere nicht?
**Antwort:** Entscheidend ist das Rahmenmaterial. Aluminium leitet Wärme 180× besser als GFK — Alu-Rahmen sind Kältebrücken. Kunststoff- oder GFK-Rahmenluken beschlagen deutlich weniger. Lösung bei Alu: Innen-Isolation mit Armaflex (6–10 mm).

## DL-020: Wie lange hält Sikaflex unter einer Luke?
**Antwort:** 10–15 Jahre unter optimalen Bedingungen. UV-Exposition der sichtbaren Kante reduziert auf 8–10 Jahre. Vibrationen (Motorboot) auf 7–10 Jahre. AYDI berechnet die effektive Bettungslebensdauer mit Korrekturfaktoren.

## DL-021: Brauche ich eine Baugenehmigung für einen neuen Deckausschnitt?
**Antwort:** Nein, aber die CE-Konformität des Bootes muss erhalten bleiben. Ein Lukeneinbau kann die Stabilität (ISO 12217) und Freibord beeinflussen. Bei CE-markierten Booten: Dokumentation des Umbaus für RCD-Konformität.

## DL-022: Welche Luke für welche Position?
**Antwort:** Vorschiff: Fluchtluke ≥ 400×520 mm, beidseitig öffenbar. Salon: Große Luke für Licht, Schiebe- oder Klappversion. Pantry: Luke mit guter Ventilation (Vorwindöffnung). Nasszelle: Kleine Luke, opakes oder mattiertes Glas.

## DL-023: Kann eine undichte Luke das Boot sinken lassen?
**Antwort:** Theoretisch ja, bei schwerer See und offenem/defektem Lukendeckel. Realistisch gefährlich: Vorschiffsluken unter Deck bei Downwind-Segeln. Deshalb sind Vorschiffsluken als sicherheitskritisch eingestuft — AYDI gibt einen CRITICAL-Befund bei Defekten.

## DL-024: Wie transportiere ich eine neue Luke zum Boot?
**Antwort:** Acrylglas-Luken hochkant transportieren, Schutzfolie bis zum Einbau belassen. Nicht in direkter Sonne im Auto lagern (>60°C = Verformung). Flanschseite polstern. Schrauben und Dichtmasse separat verpacken.

## DL-025: Wann lohnt sich Nachrüstung vs. Reparatur?
**Antwort:** Faustregel: Wenn Reparaturkosten >50% des Neupreises einer Luke betragen, lohnt sich Austausch. Bei Deckweichstellen: immer Gesamtsanierung (Deck + neue Luke). AYDI berechnet den Break-Even automatisch im Kostenmodul.

---

# 16. Glossar

| Begriff | Definition |
|---------|-----------|
| **Acrylglas (PMMA)** | Polymethylmethacrylat, transparenter Kunststoff mit 92% Lichtdurchlässigkeit, UV-beständiger als Polycarbonat, Standard für Decksluken |
| **Armaflex** | Geschlossenzelliger Elastomerschaum zur Wärme-/Kälteisolation, verhindert Kondensation an Metallrahmen, typisch 6–10 mm Dicke |
| **Bettungsmasse** | Dauerelastische Dichtmasse zwischen Lukenflansch und Deck, Standard: Polyurethan (Sikaflex 291), Lebensdauer 10–15 Jahre |
| **Biaxialgewebe** | GFK-Verstärkungsgewebe mit Fasern in ±45°-Orientierung, Flächengewicht typisch 300–600 g/m², für Lukenausschnitt-Verstärkung |
| **Butyldichtband** | Nicht aushärtendes Dichtband auf Butylkautschuk-Basis, Alternative zu PU-Bettung bei Alu-Luken, permanent elastisch |
| **CE-Kategorie** | Klassifizierung nach EU-Richtlinie 2013/53/EU für Seegebiete (A=Ozean, B=Küste, C=Binnen, D=Geschützt), bestimmt Lukenanforderungen |
| **Crazing** | Netzwerk feiner Haarrisse in Acrylglas, verursacht durch UV-Alterung oder chemische Einwirkung, Vorstufe zum Materialversagen |
| **Deckweichstelle** | Lokaler Bereich reduzierter Decksteifigkeit durch feuchtes/verfaultes Kernmaterial, oft um undichte Durchbrüche wie Luken |
| **Dorade-Ventilator** | Belüftungssystem mit Wasserabscheider, ermöglicht Frischluftzufuhr auch bei Regen/Seegang, benannt nach der Yacht DORADE (1929) |
| **Druckverformungsrest** | Prozentuale bleibende Verformung einer Dichtung nach dauerhafter Kompression, >40% = Austausch erforderlich (DIN ISO 815) |
| **EPDM** | Ethylen-Propylen-Dien-Kautschuk, Standard-Dichtungsmaterial für Decksluken, UV-/Ozon-beständig, Lebensdauer 5–8 Jahre |
| **Epoxidharz** | Zweikomponenten-Reaktionsharz für Kernverdichtung, Laminierung und Bohrlochversiegelung, z.B. West System 105/206 |
| **ESG (Einscheiben-Sicherheitsglas)** | Thermisch vorgespanntes Glas, zerfällt bei Bruch in stumpfe Krümel, für begehbare oder sicherheitskritische Luken |
| **Flanschbreite** | Breite der Auflagefläche des Lukenrahmens auf dem Deck, mindestens 25 mm, optimal ≥40 mm für sichere Abdichtung |
| **Fluchtluke** | Decksluke, die als Notausstieg dient, ISO 12216: min. 400×520 mm lichte Öffnung, beidseitig ohne Werkzeug bedienbar |
| **Galvanische Korrosion** | Elektrochemische Korrosion bei Kontakt unterschiedlicher Metalle in Elektrolyt (Seewasser), z.B. Alu-Rahmen auf Edelstahlschrauben |
| **Gasdruckfeder** | Gasgefüllter Zylinder zur Unterstützung der Lukenöffnung, Nennkraft in Newton, Lebensdauer 3–5 Jahre |
| **Gelcoat** | Pigmentierte Polyesterharz-Deckschicht auf GFK-Bauteilen, Dicke 0,5–0,8 mm, UV-Schutz und Oberflächenfinish |
| **GFK (Glasfaserverstärkter Kunststoff)** | Faserverbundwerkstoff aus Glasfaser und Polyester-/Epoxidharz, Standardmaterial für Bootsdecks und -rümpfe |
| **ISO 12216** | Internationale Norm für Fenster, Bullaugen, Luken, Deckel und Türen auf Sportbooten, definiert Prüfdrücke und Mindestmaße |
| **Kernverdichtung** | Ersetzen des Sandwich-Kernmaterials um einen Deckdurchbruch durch massive Füllmasse (Epoxid+Füllstoff), verhindert Wassereinbruch |
| **Lichte Öffnung** | Freie Durchgangsöffnung einer Luke ohne Rahmen und Dichtung, maßgebend für Fluchtlukennorm |
| **Lochfraß (Pitting)** | Lokale Korrosionsform bei Edelstahl, kleine tiefe Löcher, besonders bei 304er Stahl in Salzwasser |
| **Moskitonetz-Einsatz** | Feinmaschiges Netz (Maschenweite <1,5 mm) in Rahmen, klappbar oder mit Magnetverschluss, für Insektenschutz bei offener Luke |
| **Nennkraft** | In Newton angegebene Ausschubkraft einer Gasdruckfeder bei 20°C, temperaturabhängig (±20% über Temperaturbereich) |
| **Polycarbonat (PC)** | Schlagfester transparenter Kunststoff, 250× schlagfester als Glas, aber UV-empfindlicher als PMMA, vergilbt in 8–12 Jahren |
| **PU-Dichtmasse** | Polyurethan-basierte Dichtmasse (z.B. Sikaflex 291, 3M 4200), dauerelastisch, UV-beständig, Standard für GFK-Bootsbau |
| **Sandwich-Bauweise** | Deckaufbau: äußeres Laminat + Kernmaterial (PVC-Schaum, Balsa) + inneres Laminat, hohe Steifigkeit bei geringem Gewicht |
| **Sikaflex 291** | Marine-Polyurethan-Dichtmasse von Sika, Industriestandard für Deckbeschläge und Luken, Shore A 40, Zugfestigkeit 2,0 MPa |
| **Slamming** | Aufprall der Bootsunterseite oder des Decks auf Wellenoberfläche, erzeugt kurzzeitig hohe dynamische Lasten auf Luken |
| **Spaltkorrosion** | Korrosionsform in engen Spalten (unter Dichtungen, zwischen Flansch und Deck), begünstigt durch stagnierende Feuchtigkeit |
| **Spannungskonzentration** | Lokale Erhöhung der mechanischen Spannung an Kerben, Ecken und Durchbrüchen, Faktor K_t, reduzierbar durch Radien |
| **Spannungsrisskorrosion** | Rissbildung unter kombinierter Einwirkung von mechanischer Spannung und chemischem Angriff, z.B. Aceton auf gespanntem PMMA |
| **Teeflecken (Tea Staining)** | Bräunliche Verfärbung auf Edelstahloberflächen durch oberflächliche Korrosion, kosmetisch, häufig bei 304, selten bei 316L |
| **Tramex** | Markenname für kapazitive Feuchtemessgeräte, Industriestandard zur zerstörungsfreien Feuchtemessung in GFK-Laminaten |
| **Yellowness-Index (YI)** | Maß für die Gelbverfärbung transparenter Materialien, ASTM D1925, Neuwert PMMA: YI ≈ 1, Austausch empfohlen bei YI >12 |
| **3M 4200** | Marine-Polyurethan-Dichtmasse von 3M, etwas flexibler als Sikaflex 291, Shore A 35, geeignet für Luken, die gelegentlich demontiert werden |
| **316L** | Niedrigkohlenstoff-Variante des austenitischen Edelstahls 1.4404, Molybdänlegierung für Salzwasserbeständigkeit, Pflicht für marine Anwendungen |
| **304** | Austenitischer Edelstahl 1.4301, NICHT für dauerhafte Salzwasserexposition geeignet, Lochfraßrisiko, nur für Binnengewässer akzeptabel |

---

# 17. Schnell-Referenz

## 17.1 Entscheidungsmatrix: Welche Luke brauche ich?

| Bootstyp | Position | Mindestgröße (mm) | Empfohlenes Material | Preisrahmen |
|----------|----------|--------------------|---------------------|-------------|
| Segelboot 8–10m | Vorschiff (Flucht) | 400×520 | Acryl 10 mm, 316L-Rahmen | 350–600 EUR |
| Segelboot 8–10m | Salon | 500×500 | Acryl 10 mm | 300–500 EUR |
| Segelboot 12–15m | Vorschiff (Flucht) | 500×600 | Acryl 12 mm, 316L-Rahmen | 500–900 EUR |
| Segelboot 12–15m | Salon | 600×600 | Acryl 12 mm | 400–700 EUR |
| Motorboot 8–12m | Vorschiff | 400×520 | Acryl 10 mm | 300–500 EUR |
| Motorboot 12–18m | Salon | 700×700 | ESG 10 mm, Alu-Rahmen | 600–1.200 EUR |
| Motoryacht 18–24m | Diverse | 600–900 | ESG 12–15 mm, Alu elox. | 1.200–4.000 EUR |
| Superyacht >24m | Custom | Nach Entwurf | ESG/VSG, Custom-Rahmen | 3.000–12.000 EUR |

## 17.2 Wartungskalender Decksluken

| Intervall | Maßnahme | Aufwand | Werkzeug |
|-----------|----------|---------|----------|
| Monatlich | Acrylglas mit Süßwasser reinigen | 10 min/Luke | Wassereimer, Mikrofaser |
| Vierteljährlich | Dichtungen mit Silikonspray pflegen | 5 min/Luke | Silikonspray (NICHT Silikonöl) |
| Vierteljährlich | Scharniere und Verschlüsse schmieren | 5 min/Luke | Teflon-Spray oder Lanolin |
| Halbjährlich | Gasdruckfedern-Funktionsprüfung | 2 min/Luke | Keine |
| Jährlich | Dichtungszustand inspizieren (Risse, Verformungsrest) | 10 min/Luke | Lupe, Fingerdruck |
| Jährlich | Bettungszustand prüfen (Flanschrand) | 10 min/Luke | Sichtkontrolle |
| Jährlich | Schrauben-Anzugsmoment prüfen | 10 min/Luke | Drehmomentschlüssel |
| Alle 2 Jahre | Feuchtemessung Deck um Luke | 15 min/Luke | Tramex oder ähnlich |
| Alle 3–4 Jahre | Gasdruckfedern präventiv tauschen | 30 min/Luke | Schraubendreher |
| Alle 5–8 Jahre | Dichtungen komplett tauschen | 1–2 h/Luke | Spezialwerkzeug |
| Alle 10–15 Jahre | Bettung erneuern | 4–8 h/Luke | Sikaflex, Spachtel, Aceton |

## 17.3 Sofortmaßnahmen bei Luken-Notfällen

| Notfall | Sofortmaßnahme | Material |
|---------|----------------|----------|
| Gebrochenes Acrylglas | Segelmacher-Tape von innen, Sperrholzplatte von außen | Tape, Holz, Schrauben |
| Lukendeckel abgerissen | Sperrholz/GFK-Platte über Öffnung, mit Spanngurten fixieren | Platte, Spanngurte |
| Massive Undichtigkeit | Lukenrand mit Butylband oder Rescue Tape abdichten | Dichtband |
| Verschluss defekt | Luke mit Spanngurt oder Zurrleine sichern | Gurt, Karabiner |
| Gasdruckfeder bricht | Luke mit Holzstab abstützen (NIE Kopf in Öffnung ohne Sicherung!) | Besenstiel, Klemme |

---

# 18. Notfall-Ressourcen

## 18.1 Sicherheitshinweise Decksluken

**WARNUNG: Decksluken sind sicherheitskritische Bauteile.**

1. **Niemals den Kopf in eine Lukenöffnung stecken, die nur von einer Gasdruckfeder gehalten wird.** Immer mechanische Arretierung oder Abstützung verwenden.
2. **Fluchtluken müssen jederzeit funktionsfähig sein.** Regelmäßig prüfen, dass Öffnungsmechanismus von beiden Seiten ohne Werkzeug bedienbar ist.
3. **Bei schwerem Wetter alle Luken schließen und verriegeln.** Auch Luken mit "sturmfest"-Dichtung können bei Wellenschlag brechen.
4. **Defekte Luken nie ignorieren.** Ein gebrochenes Acrylglas oder ein fehlender Verschluss kann bei Kenterung oder schwerem Wetter zum Untergang des Bootes führen.
5. **Luken nicht als Trittstufe verwenden.** Auch vermeintlich stabile Luken sind nicht für Personenlast ausgelegt (Ausnahme: explizit als begehbar zertifizierte Luken mit ESG).

## 18.2 Hersteller-Kontaktdaten für Ersatzteile

| Hersteller | Ersatzteil-Hotline | Webshop | Lieferzeit Dichtungen |
|------------|--------------------|---------|-----------------------|
| Lewmar | +44 145 323 3500 | lewmar.com/spares | 5–10 Werktage |
| Goiot | +33 2 40 65 29 29 | goiot.com | 7–14 Werktage |
| Gebo Marine | +31 78 615 42 00 | gebomarine.com | 3–7 Werktage |
| Vetus | +31 78 618 92 33 | vetus.com | 5–10 Werktage |
| Bomar | +1 860 673 2533 | bomarhatches.com | 14–21 Werktage (USA) |
| Trend Marine | +44 145 687 0077 | trendmarine.com | 10–15 Werktage |
| Freeman Marine | +1 541 888 6245 | freemanmarine.com | 14–28 Werktage (USA) |
| Moonlight (Hood) | +44 2380 731 420 | moonlighthatches.com | 7–14 Werktage |

## 18.3 Notfall-Reparatursätze (empfohlener Bordvorrat)

| Artikel | Menge | Kosten | Verwendung |
|---------|-------|--------|-----------|
| Rescue Tape (selbstverschweißend) | 2 Rollen | 15–25 EUR | Provisorische Abdichtung |
| Butyldichtband 3 mm × 10 m | 1 Rolle | 8–12 EUR | Provisorische Bettung |
| Sikaflex 291 Kartusche (klein) | 1 Stück | 12–18 EUR | Permanente Abdichtung |
| Sperrholzplatte 6 mm, 600×600 mm | 1 Stück | 8–15 EUR | Notabdeckung |
| Spanngurte 25 mm, 2 m | 4 Stück | 10–20 EUR | Fixierung |
| Edelstahl-Schrauben M6×40 A4 | 20 Stück | 8–12 EUR | Ersatz |
| Neopren-Unterlegscheiben M6 | 20 Stück | 5–8 EUR | Ersatz |
| EPDM-Dichtungsprofil (Meterware) | 3 m | 10–20 EUR | Dichtungsersatz |
| **Gesamt Notfall-Set** | — | **76–130 EUR** | — |

---

# ANHANG A: Hersteller-Vergleichstabelle

| Kriterium | Lewmar Ocean | Lewmar Low Profile | Goiot Cristal | Gebo Flushline | Vetus Libero |
|-----------|-------------|-------------------|---------------|----------------|-------------|
| Verfügbare Größen | 10 (200–900 mm) | 8 (240–700 mm) | 7 (300–700 mm) | 6 (280–620 mm) | 5 (360–580 mm) |
| Rahmenmaterial | Alu eloxiert | Alu eloxiert | Alu eloxiert | Alu eloxiert | Alu eloxiert |
| Acryldicke | 10–12 mm | 8–10 mm | 10 mm | 8–10 mm | 8 mm |
| Dichtungstyp | EPDM | EPDM | EPDM | Neopren | EPDM |
| Scharniertyp | 316L Edelstahl | 316L Edelstahl | 316L Edelstahl | 316L Edelstahl | 316 Edelstahl |
| Gasdruckfeder | Ja (ab Größe 40) | Ja (ab Größe 50) | Ja (alle) | Optional | Ja (alle) |
| Moskitonetz | Optional | Optional | Inklusiv | Optional | Inklusiv |
| Fluchtluken-Variante | Ja (ab Größe 50) | Nein | Ja (Größe 50+) | Nein | Nein |
| CE-Kat. max. | A | B | A | B | C |
| Preis (500 mm) | 650–800 EUR | 380–480 EUR | 550–700 EUR | 320–420 EUR | 280–380 EUR |
| AYDI-Gesamtscore | 88 | 75 | 85 | 72 | 68 |
| Ersatzteilverfügbarkeit | Sehr gut | Sehr gut | Gut | Gut | Mittel |

---

# ANHANG B: Bootsklassen-spezifische Lukenanforderungen

| Bootsklasse | Lukenanzahl (typisch) | Vorschiff | Salon | Pantry | Nasszelle | Achterkabine |
|-------------|----------------------|-----------|-------|--------|-----------|-------------|
| Segelboot 8–10m | 2–3 | 1× Flucht 400×520 | 1× 500×500 | Über Salon | Über Salon | — |
| Segelboot 10–12m | 3–5 | 1× Flucht 500×500 | 1–2× 500×500 | 1× 400×400 | 1× 300×300 | — |
| Segelboot 12–15m | 4–7 | 1× Flucht 500×600 | 2× 600×600 | 1× 400×400 | 1× 400×400 | 1× 400×520 |
| Segelboot 15–20m | 6–10 | 1× Flucht 600×600 | 2–3× 600×600 | 1× 500×500 | 1–2× 400×400 | 1× 500×520 |
| Motorboot 8–12m | 2–4 | 1× 400×520 | 1–2× 500×500 | Über Salon | 1× 300×300 | — |
| Motorboot 12–18m | 4–6 | 1× 500×500 | 2× 600×600 | 1× 400×400 | 1–2× 400×400 | 1× 500×500 |
| Motoryacht 18–24m | 6–12 | 1× Flucht 600×600 | 2–4× Custom | 1× 500×500 | 2× 400×400 | 2× 500×600 |

---

# ANHANG C: Normenverzeichnis Decksluken

| Norm | Titel | Ausgabe | Relevanz für Decksluken |
|------|-------|---------|------------------------|
| ISO 12216 | Fenster, Bullaugen, Luken, Deckel und Türen — Festigkeits- und Dichtanforderungen | 2020 | Primärnorm für Decksluken |
| ISO 12217-1/2/3 | Stabilität und Auftrieb — Bewertung und Kategorisierung | 2015/2022 | Einfluss auf Lukenpositionierung und -größe |
| ISO 11812 | Wasserdichte Cockpits und Schnelllenzer | 2020 | Luken in Cockpitbereichen |
| ISO 9094 | Brandschutz | 2015 | Fluchtluken, Notausstiege |
| ISO 15085 | Schutz gegen Mann-über-Bord | 2003 | Luken als potenzielle Stolperfallen |
| ISO 12215-5/6 | Rumpfbau — Konstruktionsdrücke, Versteifungen | 2019 | Deckausschnitte, Verstärkung |
| EN 1279-2/3 | Isolierglas — Feuchteaufnahme, Gasverlust | 2018 | Doppelverglaste Luken |
| ABYC H-27 | Hatches and Weathertight Closures | 2018 | US-Standard, relevant für US-Boote |
| ABS Rules | Superyacht-Klassifikation | 2023 | Luken auf klassifizierten Yachten >24m |

---

# ANHANG D: AYDI-Bewertungsschema Decksluken

## D.1 Score-Berechnung

```
Score_gesamt = Σ (w_i × Score_i) / Σ w_i

Gewichtete Teilscores:
  Wasserdichtigkeit:     w = 0,25  Score: 0–100
  Strukturintegrität:    w = 0,20  Score: 0–100
  Bedienbarkeit:         w = 0,15  Score: 0–100
  Materialzustand:       w = 0,15  Score: 0–100
  Ventilationsleistung:  w = 0,10  Score: 0–100
  Compliance (Norm):     w = 0,10  Score: 0–100
  Optik/Kosmetik:        w = 0,05  Score: 0–100
```

## D.2 Score-Interpretation

| Score-Bereich | Bewertung | Farbe | Handlungsempfehlung |
|---------------|-----------|-------|---------------------|
| 90–100 | Ausgezeichnet | Grün | Keine Maßnahme erforderlich |
| 75–89 | Gut | Hellgrün | Wartung gemäß Kalender |
| 60–74 | Befriedigend | Gelb | Wartung zeitnah, Monitoring |
| 40–59 | Mangelhaft | Orange | Reparatur planen (nächste Saison) |
| 20–39 | Schlecht | Rot | Sofortige Reparatur erforderlich |
| 0–19 | Kritisch | Dunkelrot | Sofortmaßnahme, Boot nicht auslaufen |

---

# ANHANG E: Fallstudien

## E.1 Fallstudie: Bavaria 37 Cruiser — Vorschiffsluke undicht nach 8 Jahren

**Ausgangslage:** Bavaria 37 (Bj. 2016), Ostsee-Revier, Lewmar Low Profile 50, seit 2 Saisons Wassereinbruch bei Regen in Vorschiffskabine. Dichtung nie gewechselt, keine Silikonpflege.
**AYDI-Analyse:** Pipeline A (structured): Alter 8 Jahre, K_klima 1,0, K_nutzung 0,8, K_wartung 1,5 → Alter_eff = 9,6 Jahre. Pipeline B (visual): Dichtung sichtbar verformt, Bettung intakt. Score Wasserdichtigkeit: 35.
**Diagnose:** Druckverformungsrest >50%, EPDM verhärtet. Bettung (Sikaflex) noch intakt. Verschlüsse funktionsfähig.
**Maßnahme:** Dichtungssatz Lewmar (Artikelnr. 361029900) getauscht, Kosten 65 EUR, Selbsteinbau 1,5 h.
**Ergebnis:** Wasserdichtigkeit wiederhergestellt. AYDI-Score: 35 → 92. Gesamtkosten: 65 EUR.
**Lehre:** Halbjährliche Silikonpflege hätte Dichtungswechsel um 2–3 Jahre verzögert. AYDI-Wartungskalender generiert automatisch Erinnerungen.

## E.2 Fallstudie: Hallberg-Rassy 40 — Deckweichstelle um Salonluke

**Ausgangslage:** HR 40 (Bj. 2004), Mittelmeer, Goiot Cristal 60, Deck neben Salonluke gibt spürbar nach. Eigner seit 3 Jahren Liveaboard, keine Feuchtemessung durchgeführt.
**AYDI-Analyse:** Pipeline A: Alter 20 Jahre, K_klima 1,3, K_nutzung 1,4, K_wartung 1,0 → Alter_eff = 36,4 Jahre. Pipeline B: Gelcoat-Risse sichtbar, confidence visual_medium. Feuchtemessung (Tramex): 28% Feuchtigkeit im Kernmaterial.
**Diagnose:** Wassereinbruch über unversiegelte Schraubenlöcher seit mindestens 5 Jahren. Balsa-Kern verfault in 300 mm Radius um Luke.
**Maßnahme:** Decksektion (800×800 mm) geöffnet, nasses Balsa entfernt, Trocknung (5 Tage), neuer PVC-Schaum-Kern eingesetzt, Nachlamination, neue Goiot-Luke montiert.
**Ergebnis:** AYDI-Score: 12 → 95. Gesamtkosten: 2.800 EUR (Werft). Reparaturdauer: 8 Werktage.
**Lehre:** Bohrlöcher-Versiegelung mit Epoxid ist obligatorisch. Alle 2 Jahre Feuchtemessung durchführen.

## E.3 Fallstudie: Jeanneau Sun Odyssey 440 — Gasdruckfeder-Versagen

**Ausgangslage:** SO 440 (Bj. 2019), Charterboot Kroatien, Lewmar Ocean 60, Luke fällt nach Öffnen sofort zu. Bereits ein Chartergast am Kopf verletzt.
**AYDI-Analyse:** Pipeline A: Alter 4 Jahre, K_klima 1,3, K_nutzung 1,8, K_wartung 1,0 → Alter_eff = 9,4 Jahre. Gasdruckfedern: Effektives Alter 9,4 Jahre → weit über Lebensdauer (3–5 Jahre).
**Diagnose:** Beide Gasdruckfedern drucklos. Kolbenstangen zeigen Korrosionsspuren. Charterbetrieb mit >200 Öffnungszyklen/Saison.
**Maßnahme:** 2× Gasdruckfeder Lewmar (Artikelnr. 662000101) getauscht, Kugelkopfaufnahmen gereinigt. Kosten: 95 EUR Material, 45 min Einbau.
**Ergebnis:** AYDI-Score Bedienbarkeit: 20 → 98. Sicherheitsrisiko beseitigt.
**Lehre:** Charterboote benötigen doppelte Wartungsfrequenz. AYDI berechnet dies über K_nutzung = 1,8.

## E.4 Fallstudie: Beneteau Oceanis 51.1 — Nachrüstung Fluchtluke Achterkabine

**Ausgangslage:** Oceanis 51.1 (Bj. 2020), geplante Atlantiküberquerung (CE-Kat A erforderlich). Achterkabine hat keine Fluchtluke — nur Zugang über Salon.
**AYDI-Analyse:** Pipeline A (Compliance): Fluchtluke Achterkabine fehlt. CRITICAL-Befund. ISO 12216 schreibt für CE-Kat A min. 400×520 mm Fluchtluke in jedem separaten Raum vor.
**Diagnose:** Compliance-Score: 15/100 für Achterkabine. Nachrüstung zwingend für Atlantik-Zulassung.
**Maßnahme:** Houdini Escape Hatch (460×560 mm lichte Öffnung) in Achterkabinen-Decke eingebaut. Sandwich-Deck: Kernverdichtung, Verstärkungslaminat, Flanschversiegelung. Werftarbeit.
**Ergebnis:** Compliance-Score: 15 → 100. Kosten: 1.850 EUR (Luke 620 EUR + Werft 1.230 EUR). Zeitaufwand: 3 Tage.
**Lehre:** AYDI-Compliance-Modul identifiziert fehlende Fluchtluken automatisch bei Eingabe der geplanten CE-Kategorie.

## E.5 Fallstudie: Contest 42CS — UV-geschädigtes Acrylglas nach 18 Jahren

**Ausgangslage:** Contest 42CS (Bj. 2006), Karibik seit 2018 (zuvor Nordeuropa), alle 6 Salonluken (Goiot Opal) stark vergilbt. Eigner beklagt Lichtmangel im Salon.
**AYDI-Analyse:** Pipeline B (visual): Yellowness-Index geschätzt >15 (deutliche Gelbfärbung auf Fotos). Pipeline A: Alter 18 Jahre, davon 6 Jahre Tropen (K_klima 1,6 für Tropen-Phase). Gewichtetes Alter: 12 Jahre × 1,0 + 6 Jahre × 1,6 = 21,6 effektive Jahre.
**Diagnose:** PMMA weit über Lebensdauer. Crazing an 4 von 6 Scheiben. Lichtdurchlässigkeit geschätzt <75% (Neuwert 92%).
**Maßnahme:** Alle 6 Acrylglas-Scheiben getauscht (Goiot-Originalteile), UV-Schutzfolie (3M Prestige 70) auf neue Scheiben aufgebracht.
**Ergebnis:** AYDI-Score Materialzustand: 30 → 98. Kosten: 6× 180 EUR Scheiben + 6× 35 EUR UV-Folie + 8 h Arbeit = 1.290 EUR + 640 EUR Werft = 1.930 EUR.
**Lehre:** In tropischen Revieren: UV-Schutzfolie von Anfang an, Lukenabdeckung bei Nichtgebrauch.

## E.6 Fallstudie: Dehler 38 SQ — Galvanische Korrosion am Lukenrahmen

**Ausgangslage:** Dehler 38 SQ (Bj. 2012), Nordsee, Alu-Rahmenluken mit Edelstahl-Befestigung. Weiße Ablagerungen am Rahmen, einzelne Schrauben nicht mehr lösbar.
**AYDI-Analyse:** Pipeline B (visual): Weißliche Korrosionsprodukte am Alu-Rahmen, confidence visual_high. Pipeline A: Galvanische Paarung Aluminium/Edelstahl ohne Isolation erkannt.
**Diagnose:** Galvanische Korrosion durch direkten Alu/Edelstahl-Kontakt in Salzwasserumgebung. Rahmen-Wandstärke lokal um 30% reduziert. Drei Schrauben im Alu festkorrodiert.
**Maßnahme:** Luken demontiert (festsitzende Schrauben ausgebohrt), Alu-Rahmen gereinigt und passiviert (Alodine), Neopren-Isolationsscheiben zwischen Rahmen und Edelstahlschrauben, Neumont.
**Ergebnis:** AYDI-Score: 40 → 82. Kosten: 180 EUR Material + 6 h Arbeit = 660 EUR (Werft). Rahmen vorerst weiterverwendbar.
**Lehre:** Galvanische Isolation bei Metallpaarungen ist Pflicht. AYDI prüft Material-Kombinationen im Materialmodul.

## E.7 Fallstudie: Lagoon 42 — Luken-Upgrade bei Katamaranbau

**Ausgangslage:** Lagoon 42 (Bj. 2021), 8 Standard-Luken (Lewmar Low Profile 44), Eigner wünscht bessere Ventilation für Tropen-Einsatz. Original-Luken ohne Moskitonetz.
**AYDI-Analyse:** Pipeline A (Ventilation): Kabinen-Luftwechselrate mit aktuellen Luken berechnet — ausreichend für Nordeuropa (n=6/h), unzureichend für Tropen (Ziel n=10/h). Ventilations-Score: 55.
**Diagnose:** Luken funktional intakt, aber zu klein für tropische Ventilationsanforderungen. Fehlende Moskitonetze verhindern Nacht-Ventilation.
**Maßnahme:** 4 Luken durch Lewmar Ocean 50 (größerer Ausschnitt, +30% Öffnungsfläche) ersetzt. 4 weitere Luken mit Oceanair-Moskitonetzen nachgerüstet. Ausschnitte vergrößert, Kernverdichtung erneuert.
**Ergebnis:** Ventilations-Score: 55 → 87. Kosten: 4× 720 EUR Luken + 4× 85 EUR Netze + 3 Tage Werft (2.400 EUR) = 5.620 EUR.
**Lehre:** Revierplanung beeinflusst Lukenanforderungen erheblich. AYDI passt Bewertungen an geplantes Fahrgebiet an.

## E.8 Fallstudie: Oyster 565 — Spannungsrisse nach DIY-Einbau

**Ausgangslage:** Oyster 565 (Bj. 2008), Eigner hat 2022 zwei Salonluken selbst getauscht. Nach 6 Monaten: sternförmige Risse an 5 von 12 Schraubenlöchern einer Luke.
**AYDI-Analyse:** Pipeline B (visual): Spannungsrisse klar erkennbar um Befestigungslöcher, confidence visual_high. Score Strukturintegrität: 22.
**Diagnose:** Anzugsmoment zu hoch (geschätzt 12–15 Nm statt 5–7 Nm für M6 in GFK). Lochdurchmesser zu eng (6,0 mm statt empfohlen 7,5 mm). Keine Neopren-Unterlegscheiben verwendet. Thermische Spannungen durch fehlende Dehnungsfuge.
**Maßnahme:** Luke demontiert, alle Löcher auf ∅ 8 mm aufgebohrt, Rissstopp-Bohrungen an Rissenden, Neopren-Unterlegscheiben, Wiedereinbau mit Drehmomentschlüssel (6 Nm). Scheibe trotz Rissen weiterverwendbar (Risse gestoppt).
**Ergebnis:** AYDI-Score: 22 → 72 (Risse bleiben sichtbar, aber gestoppt). Kosten: 40 EUR Material + 3 h Arbeit.
**Lehre:** Drehmomentschlüssel ist kein optionales Werkzeug. AYDI gibt Installationshinweise mit spezifischen Drehmomenten aus.

---

# ANHANG F: Cross-Referenz Bootshersteller → Lukentyp

| Bootshersteller | Standardmäßig verbaut | Zeitraum | Ersatz-Kompatibel |
|----------------|----------------------|----------|-------------------|
| Bavaria | Gebo Flushline | 2010–2020 | Lewmar Low Profile |
| Bavaria | Lewmar Low Profile | 2020– | Original |
| Beneteau | Lewmar Low Profile | 2015– | Original |
| Beneteau | Goiot Opal | 2005–2015 | Goiot Cristal |
| Contest | Goiot Cristal | 2000– | Original |
| Dehler | Gebo Flushline | 2008–2018 | Lewmar Low Profile |
| Dufour | Lewmar Low Profile | 2015– | Original |
| Hallberg-Rassy | Goiot Cristal | 1995– | Original |
| Hanse | Lewmar Low Profile | 2010– | Original |
| Jeanneau | Lewmar Low/Ocean | 2012– | Original |
| Lagoon | Lewmar Low Profile | 2015– | Lewmar Ocean |
| Najad | Goiot Cristal | 2000–2015 | Original |
| Oyster | Lewmar Ocean | 2005– | Original |
| X-Yachts | Lewmar Ocean | 2010– | Original |

---

# ANHANG G: Preiskalkulator-Referenztabelle

## G.1 Lukenpreise nach Hersteller und Größe (EUR, inkl. MwSt., Stand 2025)

| Größe (mm) | Lewmar Ocean | Lewmar LP | Goiot Cristal | Gebo Flush | Vetus Libero |
|------------|-------------|-----------|---------------|------------|-------------|
| 250×250 | — | 280 | — | 220 | — |
| 300×300 | 420 | 310 | 380 | 260 | 280 |
| 400×400 | 520 | 380 | 460 | 320 | 330 |
| 500×500 | 680 | 450 | 580 | 390 | 380 |
| 600×600 | 850 | 560 | 720 | 470 | — |
| 700×700 | 1.050 | 680 | 880 | — | — |
| 800×800 | 1.280 | — | — | — | — |
| 900×900 | 1.520 | — | — | — | — |

## G.2 Zubehör und Ersatzteile (EUR, inkl. MwSt.)

| Artikel | Lewmar | Goiot | Gebo | Vetus |
|---------|--------|-------|------|-------|
| Dichtungssatz | 45–85 | 40–70 | 35–60 | 30–55 |
| Gasdruckfeder (Stück) | 35–55 | 30–50 | 25–40 | 25–45 |
| Acrylglas-Scheibe | 180–450 | 150–380 | 120–300 | 100–250 |
| Scharniersatz | 60–120 | 50–100 | 40–80 | 35–70 |
| Moskitonetz-Einsatz | 55–95 | 50–85 | 45–75 | 40–70 |
| Verdunkelungsrollo | 75–130 | 70–120 | 60–100 | 55–90 |
| Verschlusshebel (Stück) | 25–45 | 20–40 | 18–35 | 15–30 |

---

# ANHANG H: Material-Datenblätter (Kurzfassung)

| Eigenschaft | PMMA (Acryl) | PC (Polycarb.) | ESG (Glas) | Einheit |
|-------------|-------------|----------------|------------|---------|
| Dichte | 1.190 | 1.200 | 2.500 | kg/m³ |
| Lichtdurchlässigkeit | 92 | 88 | 90 | % |
| Schlagfestigkeit (Charpy) | 15 | 65 | 6 | kJ/m² |
| Biegefestigkeit | 110 | 90 | 120 | MPa |
| E-Modul | 3.300 | 2.400 | 70.000 | MPa |
| Wärmeausdehnungskoeff. | 70 | 65 | 9 | 10⁻⁶/K |
| Max. Dauereinsatztemp. | 80 | 120 | 250 | °C |
| UV-Beständigkeit | Gut | Mäßig (ohne Beschichtung) | Sehr gut | — |
| Yellowness-Index (Neuwert) | 1,0 | 1,5 | 0,3 | — |

---

# ANHANG I: Werkzeug-Checkliste für Lukeneinbau

| Werkzeug | Verwendung | Geschätzter Preis |
|----------|-----------|-------------------|
| Stichsäge mit HM-Blatt | Deckausschnitt | 80–200 EUR |
| Oberfräse mit Bündigfräser | Kernmaterial abtragen | 120–300 EUR |
| Bohrmaschine + Stufenbohrer | Bohrlöcher, Eckradien | 60–150 EUR |
| Lochsäge-Set (25–80 mm) | Eckenradien vorbohren | 30–60 EUR |
| Drehmomentschlüssel (1–25 Nm) | Schrauben anziehen | 40–80 EUR |
| Winkelschleifer + Schleifscheibe | Kanten bearbeiten | 50–120 EUR |
| Schleifpapier-Set (80–1500er) | Oberflächenvorbereitung | 15–30 EUR |
| Kunststoffspachtel-Set | Dichtmasse auftragen/entfernen | 10–20 EUR |
| Messchieber (150 mm) | Maße kontrollieren | 15–40 EUR |
| Stahllineal (600 mm) | Planheit prüfen | 10–20 EUR |
| Wasserwaage (300 mm) | Ausrichtung | 10–25 EUR |
| Abklebeband (50 mm, 3 Rollen) | Gelcoat-Schutz | 8–15 EUR |
| Mischbecher + Rührstäbe | Epoxid anrühren | 5–10 EUR |
| Handschuhe (Nitril, 50 Stk.) | Hautschutz | 8–12 EUR |
| Atemschutzmaske (P2 + A1) | Staub- und Dampfschutz | 20–40 EUR |
| **Gesamt Werkzeug-Set** | — | **480–1.120 EUR** |

---

# ANHANG J: Dichtmassen-Vergleich

| Eigenschaft | Sikaflex 291 | 3M 4200 | Sikaflex 292i | Butyldichtband | Silikon (NICHT empfohlen) |
|-------------|-------------|---------|---------------|----------------|--------------------------|
| Basis | Polyurethan | Polyurethan | Polyurethan | Butylkautschuk | Siloxan |
| Aushärtezeit | 3–5 Tage | 2–4 Tage | 5–7 Tage | Keine (plastisch) | 24 h |
| Shore A Härte | 40 | 35 | 55 | — (plastisch) | 20–30 |
| Zugfestigkeit | 2,0 MPa | 1,7 MPa | 4,5 MPa | — | 1,0 MPa |
| Bruchdehnung | 400% | 500% | 300% | — | 300% |
| UV-Beständigkeit | Gut | Gut | Gut | Mäßig | Gut |
| Haftung auf GFK | Sehr gut | Sehr gut | Sehr gut | Gut | Schlecht |
| Haftung auf Alu | Gut (mit Primer) | Gut (mit Primer) | Sehr gut | Sehr gut | Mäßig |
| Demontierbarkeit | Schwierig | Mittel | Sehr schwierig | Leicht | Leicht |
| Preis (310 ml) | 14–18 EUR | 16–22 EUR | 18–24 EUR | 8–12 EUR/10m | 5–8 EUR |
| AYDI-Empfehlung | Standard | Alternative | Strukturklebung | Alu-Luken/Provisorium | NICHT verwenden |

---

# ANHANG K: Checkliste Gebrauchtboot-Lukeninspektion

Für die Bewertung von Decksluken beim Gebrauchtkauf. Jedes Kriterium mit Score 0–100:

| # | Prüfpunkt | Score 90–100 | Score 50–70 | Score <30 |
|---|-----------|-------------|-------------|-----------|
| 1 | Acrylglas-Klarheit | Klar, keine Vergilbung | Leichte Vergilbung | Stark vergilbt, Crazing |
| 2 | Dichtungszustand | Elastisch, intakt | Leicht verhärtet | Rissig, deformiert |
| 3 | Bettungszustand | Intakt, keine Lücken | Leichte Risse am Rand | Gelöst, verhärtet |
| 4 | Scharnierfunktion | Leichtgängig, spielfrei | Leicht schwergängig | Blockiert, ausgeschlagen |
| 5 | Verschlussfunktion | Greift satt, dicht | Leicht nachstellbar | Defekt, kein Griff |
| 6 | Gasdruckfeder | Hält Luke >30 s | Hält Luke 10–30 s | Hält nicht (<10 s) |
| 7 | Rahmenkorrosion | Keine sichtbar | Oberflächlich | Lochfraß, Delamination |
| 8 | Deck um Luke | Fest, kein Nachgeben | Leicht elastisch | Weich, Knarzen |
| 9 | Wasserdichtigkeit | Kein Eintritt | Feuchtigkeit bei starkem Regen | Tropft regelmäßig |
| 10 | Fluchtluken-Norm | Konform, beidseitig öffenbar | Teilweise konform | Nicht konform / fehlt |

---

# ANHANG L: Klimakorrektur-Tabelle

| Revier | K_klima | UV-Index (Ø Sommer) | Salzgehalt | Luftfeuchtigkeit | Bemerkung |
|--------|---------|---------------------|------------|-------------------|-----------|
| Ostsee | 0,9 | 4–6 | Niedrig (8‰) | Mittel | Frost im Winter |
| Nordsee | 1,0 | 4–6 | Mittel (32‰) | Hoch | Wind, Salz |
| Atlantik (Biskaya) | 1,1 | 5–7 | Hoch (35‰) | Hoch | Seegang |
| Mittelmeer West | 1,2 | 7–9 | Hoch (38‰) | Mittel | Starke UV |
| Mittelmeer Ost/Ägäis | 1,3 | 8–10 | Hoch (39‰) | Niedrig | Sehr starke UV |
| Karibik | 1,5 | 9–11 | Hoch (35‰) | Hoch | Tropisch |
| Südostasien | 1,6 | 10–12 | Hoch (34‰) | Sehr hoch | Höchste Belastung |
| Süßwasser / Binnensee | 0,7 | 4–6 | Kein | Mittel | Minimale Korrosion |
| Polargebiet | 0,8 | 2–3 | Hoch (35‰) | Niedrig | Frost, UV gering |

---

# ANHANG M: Thermische Ausdehnungsberechnung

```
ΔL = α × L₀ × ΔT

Typische Berechnung für Acrylglas-Luke 500 mm:
  α (PMMA) = 70 × 10⁻⁶ /K
  L₀ = 500 mm
  ΔT = 50 K (Winter -5°C bis Sommer +45°C auf Deck)

  ΔL = 70 × 10⁻⁶ × 500 × 50 = 1,75 mm

→ Jede Befestigungsschraube muss ±0,9 mm Bewegung erlauben
→ Lochdurchmesser = Schraubendurchmesser + 2 mm
→ Neopren-Unterlegscheiben dämpfen thermische Spannungen

Vergleich:
  PMMA (70 × 10⁻⁶): ΔL = 1,75 mm
  Alu-Rahmen (24 × 10⁻⁶): ΔL = 0,60 mm
  GFK-Deck (18 × 10⁻⁶): ΔL = 0,45 mm
  Differenz PMMA → GFK: 1,30 mm → Quelle für Spannungsrisse!
```

---

# ANHANG N: Lukenöffnungs-Sicherheitssystem

| Sicherungsmethode | Beschreibung | Kosten | AYDI-Empfehlung |
|-------------------|-------------|--------|-----------------|
| Gasdruckfeder | Standard-Haltevorrichtung, druckverlustanfällig | 25–60 EUR/Stk | Standard, paarweise |
| Reibungsscharnier | Scharnier mit einstellbarer Friktion, hält jede Position | 60–120 EUR/Satz | Empfohlen für kleine Luken |
| Kettenbegrenzer | Kette limitiert Öffnungswinkel, kein Haltemechanismus | 15–30 EUR/Stk | Zusätzlich, nicht allein |
| Ratschenstütze | Mechanische Stütze mit Rastpositionen, formschlüssig | 30–60 EUR/Stk | Sicherste Variante |
| Magnethalter | Magnet hält Luke offen, versagt bei Vibration | 10–20 EUR/Stk | Nicht für Seegang |

---

# ANHANG O: AYDI-Integrations-Referenz

## O.1 Luken-Datenmodell (Pydantic v2)

```python
class HatchAssessment(BaseModel):
    model_config = {"from_attributes": True}

    hatch_id: str
    position: str  # "foredeck", "salon", "pantry", "head", "aft_cabin"
    manufacturer: str | None
    model: str | None
    size_mm: tuple[int, int]  # (breite, laenge)
    material_lens: str  # "pmma", "pc", "esg", "vsg"
    material_frame: str  # "alu_anodized", "alu_painted", "316l", "304", "grp"
    age_years: float
    effective_age_years: float  # nach Klimakorrektur

    score_watertightness: int  # 0-100
    score_structural: int  # 0-100
    score_operability: int  # 0-100
    score_material_condition: int  # 0-100
    score_ventilation: int  # 0-100
    score_compliance: int  # 0-100
    score_cosmetic: int  # 0-100
    score_total: float  # gewichteter Durchschnitt

    confidence: str  # "measured", "visual_high", "visual_medium", "estimated"
    findings: list[str]
    recommendations: list[str]
```

## O.2 Modul-Registrierung

```python
# In analysis orchestrator: Luken-Bewertung als Sub-Modul von "compliance" und "materials"
HATCH_MODULE = {
    "id": "hatch_assessment",
    "parent_modules": ["compliance", "materials"],
    "tier": 2,
    "weight_structured": 0.70,
    "weight_visual": 0.30,
    "skip_conditions": ["no_hatch_data", "no_photos_deck"],
}
```

---

# ANHANG P: Visuelle Analyse-Prompts für Claude Vision

## P.1 Decksluke-Gesamtzustand

```
Prompt-Template (deutsch):
"Analysiere diese Decksluke. Bewerte folgende Aspekte auf einer Skala von 0-100:
1. Acrylglas-Zustand (Klarheit, Vergilbung, Crazing, Risse)
2. Dichtungszustand (soweit sichtbar)
3. Rahmenzustand (Korrosion, Verformung, Delamination)
4. Bettungszustand (Flanschrand sichtbar?)
5. Mechanik (Scharnier, Verschlüsse, Gasdruckfeder soweit sichtbar)

Antworte im JSON-Format. Setze Confidence für jeden Aspekt:
- visual_high: klar erkennbar
- visual_medium: eingeschränkt beurteilbar
- visual_low: kaum beurteilbar
- visual_insufficient: nicht beurteilbar (dann Score weglassen)

Sage 'nicht beurteilbar' wenn ein Aspekt nicht erkennbar ist."
```

---

# ANHANG Q: Wartungsprotokoll-Vorlage

| Datum | Luke Nr. | Prüfpunkt | Zustand (Score) | Maßnahme | Nächste Prüfung |
|-------|---------|-----------|----------------|----------|----------------|
| __.__.__ | __ | Dichtung | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Acrylglas | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Gasdruckfeder | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Bettung | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Scharnier | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Verschlüsse | __ /100 | __________ | __.__.__ |
| __.__.__ | __ | Deck-Feuchte | __ % | __________ | __.__.__ |

---

# ANHANG R: Änderungshistorie dieser Wissensdatei

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | 2025-01 | Sektionen 1–9: Grundlagen, Typen, Materialien, Bewertung, Hersteller, Compliance, Wartung, Retrofit, Fluchtluken | AYDI |
| 2.0 | 2025-04 | Sektionen 10–18, Anhänge A–R: Technische Berechnungen, Einbau-Anleitung, Alterungsmechanismen, Fehlerbild-Atlas, Fehlerbehebung, FAQ, Glossar, Schnell-Referenz, Notfall, Fallstudien | AYDI |

---

**— Ende der Wissensdatei 08_01_decksluken.md, Version 2.0 —**
