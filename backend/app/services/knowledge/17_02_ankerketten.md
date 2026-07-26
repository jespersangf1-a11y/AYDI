---
titel: "Ankerketten — Güten, Dimensionierung und Pflege"
kategorie: "Anker und Kette"
unterkategorie: "Ankerketten"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 17_02 — Ankerketten — Güten, Dimensionierung und Pflege

> **AYDI Wissensdatei 17.02** — Kategorie 17: Anker und Kette
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO/DIN-Normen), documented (Hersteller-Kataloge, Klassifikationsgesellschaften), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Kettentypen und Güten](#2-kettentypen-und-güten)
3. [Kettendimensionierung](#3-kettendimensionierung)
4. [Kettenmaterialien](#4-kettenmaterialien)
5. [Kettenmaße und Kompatibilität](#5-kettenmaße-und-kompatibilität)
6. [Kettenverbindungen](#6-kettenverbindungen)
7. [Hersteller und Bezugsquellen](#7-hersteller-und-bezugsquellen)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [Kettenpflege](#10-kettenpflege)
11. [FAQ — Häufige Fragen](#11-faq--häufige-fragen)
12. [Glossar](#12-glossar)
13. [Schnell-Referenz](#13-schnell-referenz)
14. [ANHANG A — Fallstudie: Kettentausch 38-Fuß-Blauwasseryacht](#anhang-a)
15. [ANHANG B — Fallstudie: Kettenbruch bei Sturmankern](#anhang-b)
16. [ANHANG C — Fallstudie: Elektrolyse an Edelstahlkette](#anhang-c)
17. [ANHANG D — Fallstudie: Windlass-Inkompatibilität nach Kettenwechsel](#anhang-d)
18. [ANHANG E — Fallstudie: Mixed Rode Optimierung](#anhang-e)
19. [ANHANG F — Fallstudie: Kettenmarkierung Langfahrt](#anhang-f)
20. [ANHANG G — Fallstudie: Re-Galvanisierung 100m Kette](#anhang-g)
21. [ANHANG H — Fallstudie: Kettenkasten-Redesign Katamaran](#anhang-h)
22. [ANHANG I — AYDI-Integration (Pydantic-Modelle)](#anhang-i)

---

## 1. Einführung

### 1.1 Die Rolle der Ankerkette im Ankersystem

Die Ankerkette ist das entscheidende Verbindungselement zwischen Anker und Yacht. Während der Anker selbst die Haltekraft im Grund erzeugt, bestimmt die Kette maßgeblich die Funktionsfähigkeit des gesamten Ankersystems. Ihre Aufgabe geht weit über die reine Kraftübertragung hinaus — sie beeinflusst den Einzugswinkel des Ankers, die Dämpfungseigenschaften des Systems und die Sicherheit bei wechselnden Bedingungen.

Ein Ankersystem ist nur so stark wie sein schwächstes Glied — im wörtlichen Sinne. Eine unterdimensionierte oder verschlissene Kette kann bei plötzlichen Windstößen oder Strömungsänderungen zum vollständigen Versagen des Systems führen. Die Auswahl der richtigen Kette ist daher eine der wichtigsten Entscheidungen bei der Ausrüstung einer Yacht.

### 1.2 Das Prinzip der Kettenary (Kettenlinie)

Die Kettenary — auch Kettenlinie oder Catenary genannt — ist das physikalische Prinzip, das die Ankerkette zu einem so effektiven Element macht. Wenn eine Kette zwischen zwei Punkten hängt, bildet sie unter Eigengewicht eine charakteristische Kurve. Diese Kurve sorgt dafür, dass die Kraft am Anker nahezu horizontal ankommt — der entscheidende Faktor für die Haltekraft moderner Ankerdesigns.

**Die Kettenary wirkt als natürlicher Stoßdämpfer:**

Bei leichten Bedingungen hängt die Kette in einer tiefen Kurve. Wenn die Yacht durch Wind oder Strom nach hinten gezogen wird, muss zunächst die durchhängende Kette angehoben werden, bevor die Kraft am Anker ankommt. Dieser Vorgang absorbiert Energie und verhindert abrupte Belastungsspitzen am Anker.

**Formel der Kettenary:**

```
y = a × cosh(x/a) - a

wobei:
  y = vertikale Auslenkung (m)
  x = horizontale Distanz (m)
  a = T_H / (w × g)
  T_H = horizontale Zugkraft (N)
  w = Kettengewicht pro Meter (kg/m)
  g = 9,81 m/s²
```

**Praktische Bedeutung:**

| Windstärke (Bft) | Scope (Kette:Tiefe) | Zugwinkel am Anker | Horizontale Kraft (10m Boot) |
|---|---|---|---|
| 3 (leicht) | 3:1 | 8–12° | 50–120 N |
| 5 (frisch) | 4:1 | 5–8° | 200–400 N |
| 6 (stark) | 5:1 | 3–5° | 500–1.000 N |
| 7 (steif) | 7:1 | 1–3° | 1.200–2.500 N |
| 8+ (stürmisch) | 10:1+ | <1° | 3.000–8.000 N |

**Confidence: documented** — Werte basieren auf Berechnungen nach Chapman Piloting & Seamanship und ABYC Standards.

### 1.3 Gewicht als Vorteil — nicht als Nachteil

Viele Yachtbesitzer betrachten das Gewicht der Ankerkette primär als Belastung. Tatsächlich ist das Gewicht der Kette ein wesentlicher Sicherheitsfaktor:

**Vorteile des Kettengewichts:**

1. **Kettenary-Effekt**: Je schwerer die Kette, desto ausgeprägter die Kettenary-Kurve und desto besser die Stoßdämpfung
2. **Horizontaler Zugwinkel**: Schwere Kette hält den Zug am Anker flacher — der Anker gräbt sich tiefer ein statt herausgezogen zu werden
3. **Reduzierter Schwoikreis**: Bei moderaten Bedingungen hält schwere Kette das Boot näher am Anker
4. **Natürliches Ruckeln-Dämpfen**: Die Masse der Kette absorbiert Stöße bei Böen und Wellenschlag
5. **Unempfindlichkeit gegen Schamfilen**: Kette auf Grund kann über Fels, Koralle und Sand scheuern ohne Schaden

**Gewichtsvergleich Kette vs. Leine:**

| Rode-Typ | Gewicht pro 30m | Vorteil |
|---|---|---|
| 8mm Kette G40 | 42 kg | Maximale Kettenary, kein Scheuerschutz nötig |
| 10mm Kette G40 | 66 kg | Schwere Kettenary, für Boote >12m |
| 14mm Nylon-Leine | 3,2 kg | Leicht, elastisch, aber keine Kettenary |
| Mixed Rode (15m 8mm Kette + 30m Nylon) | 24 kg | Kompromiss |

### 1.4 Kette vs. Leine vs. Mixed Rode — Grundsatzentscheidung

**Ganz-Kette (All-Chain Rode):**
- Empfohlen für: Blauwasser-Yachten, Dauerlieger, Ankerplätze mit Felsgrund
- Vorteile: Maximale Sicherheit, kein Scheuerschutz nötig, Windlass-kompatibel
- Nachteile: Hohes Gewicht im Bug, teurer, Kettenkasten-Volumen
- Typische Längen: 50–100m (je nach Revier)

**Mixed Rode (Kette + Leine):**
- Empfohlen für: Küstenfahrer, Regattayachten, gewichtsbewusste Segler
- Vorteile: Leichter, elastische Komponente, günstiger
- Nachteile: Scheuerschutz an der Verbindung, Leine empfindlich am Grund
- Typisch: 10–20m Kette + 40–60m Nylon

**Ganz-Leine (All-Rope Rode):**
- Empfohlen für: Kleine Boote <7m, Tagesankern, geschützte Reviere
- Vorteile: Sehr leicht, einfach zu handhaben, elastisch
- Nachteile: Keine Kettenary, scheuert auf Grund, kein Windlass
- Typisch: Nur bei Jollen und kleinen Tagesseglern

### 1.5 Historischer Überblick

Die Geschichte der Ankerkette reicht über 2.000 Jahre zurück. Die Römer nutzten bereits einfache Eisenketten, jedoch dominierten Hanftrossen bis ins 19. Jahrhundert. Erst mit der industriellen Fertigung ab ~1810 wurde die kalibrierte Kurzgliedkette zum Standard.

**Meilensteine:**
- 1810: Samuel Brown patentiert geschweißte Eisenkette in England
- 1834: Stegkette (Stud-Link) wird Standard für große Schiffe
- 1930er: Feuerverzinkung wird Standard für Sportboote
- 1970er: Elektrische Ankerwinden werden in Yachten üblich
- 1990er: Kalibrierte Ketten für Windlass-Kompatibilität
- 2010er: Hochfeste G70-Ketten für leichtgewichtige Anwendungen
- 2020er: Verbesserte Legierungen und Beschichtungen

### 1.6 Geltungsbereich dieser Wissensdatei

Diese Wissensdatei behandelt Ankerketten für Sportboote und Yachten im Bereich von 6 bis 30 Metern Länge. Kommerzielle Schiffsketten (Stud-Link >22mm, Klasse-geprüft nach IACS) werden nur zum Vergleich erwähnt. Der Fokus liegt auf:

- Kalibrierte Kurzgliedketten 6–14mm
- Feuerverzinkter Stahl und Edelstahl 316L
- Windlass-kompatible Güten und Maße
- Europäische und US-amerikanische Normen
- Praxis der Yachtausrüstung im europäischen Markt

---

## 2. Kettentypen und Güten

### 2.1 Grundlegende Unterscheidung: Kalibriert vs. Unkalibriert

Der wichtigste Unterschied bei Ankerketten für Yachten ist die Kalibrierung. Kalibrierte Ketten haben eng tolerierte Gliedermaße und passen exakt in die Kettennuss (Wildcat/Gypsy) einer Ankerwinch.

**Kalibrierte Kette:**
- Jedes Glied hat definierte Innen- und Außenmaße
- Toleranzen: typisch ±0,5mm bei Teilung, ±0,3mm bei Innenweite
- Passt in Standard-Kettennüsse der großen Hersteller
- Kennzeichnung: "calibrated" oder "kalibriert" oder DIN 766
- Preis: ca. 20–40% teurer als unkalibrierte Kette gleicher Güte

**Unkalibrierte Kette:**
- Glieder haben größere Toleranzen
- Kann in Kettennüsse springen oder klemmen
- Nur für handgeborgene Ankersysteme geeignet
- Beispiele: DIN 5685, DIN 764 Langglied
- Preise niedriger, aber für Windlass-Anwendung unbrauchbar

> **AYDI-Regel:** Für jede Yacht mit elektrischer Ankerwinde ist ausschließlich kalibrierte Kette zulässig. Die Kettennuss muss zum exakten Kettentyp und -maß passen.

### 2.2 Kurzglied vs. Langglied

**Kurzgliedkette (Short Link):**
- Verhältnis Innenweite zu Durchmesser: ca. 3,5:1
- Standard für Ankerwindlass
- DIN 766, ISO 4565
- Nahezu alle Yacht-Ankerketten

**Langgliedkette (Long Link):**
- Verhältnis Innenweite zu Durchmesser: ca. 5:1 bis 6:1
- DIN 763, DIN 764
- Nicht für Windlass geeignet
- Verwendung: Festmacherketten, Moorings, Liegeplätze
- Vorteil: Leichter pro Meter bei gleicher Bruchlast
- Nachteil: Passt nicht in Kettennüsse

### 2.3 Stegkette (Stud-Link) vs. Stegloskette (Studless)

**Stegkette (Stud-Link):**
- Querstrebe (Steg) in jedem Glied
- Verhindert Verknoten und Verschlingen
- Standard ab 22mm Durchmesser für kommerzielle Schifffahrt
- Für Yachten: ab 16mm gelegentlich zu finden
- Gewicht: ca. 10–15% schwerer als stegloses Pendant
- Vorteile: Verdrehsicher, stapelt sich geordneter im Kettenkasten
- Nachteile: Schwerer, teurer, bei Korrosion bricht Steg aus (Verletzungsgefahr)

**Stegloskette (Studless):**
- Standard für Yachten bis 30m
- Alle gängigen DIN/ISO-Ketten im Yachtbereich
- Leichter, flexibler, günstiger
- Stapelt sich weniger geordnet — Kettenkasten kann "verstopfen"

### 2.4 DIN 766 — Kalibrierte Rundstahlkette (Kurzglied)

**DIN 766: Rundstahlkette, kalibriert, kurzgliedrig**

Dies ist der Standard für Yacht-Ankerketten in Europa. Die DIN 766 definiert exakte Maße für jeden Durchmesser und garantiert Windlass-Kompatibilität.

**Spezifikationen DIN 766:**

| Durchmesser (mm) | Innenweite (mm) | Innenlänge (mm) | Teilung (mm) | Gewicht (kg/m) | Bruchlast (kN) |
|---|---|---|---|---|---|
| 4 | 6,5 | 16 | 16 | 0,35 | 4,0 |
| 5 | 7,5 | 18,5 | 18,5 | 0,54 | 6,3 |
| 6 | 8,4 | 21,0 | 21,0 | 0,79 | 9,0 |
| 7 | 10,0 | 24,5 | 24,5 | 1,08 | 12,3 |
| 8 | 11,3 | 28,0 | 28,0 | 1,40 | 16,0 |
| 10 | 14,0 | 35,0 | 35,0 | 2,20 | 25,0 |
| 12 | 16,8 | 42,0 | 42,0 | 3,15 | 36,0 |
| 13 | 18,2 | 45,5 | 45,5 | 3,70 | 42,3 |
| 14 | 19,6 | 49,0 | 49,0 | 4,30 | 49,0 |

**Material:** Unlegierter Stahl, typisch S235JR oder vergleichbar
**Oberfläche:** Feuerverzinkt nach DIN EN ISO 1461 (Mindestschichtdicke 45µm)
**Kalibrierung:** Jedes 10. Glied wird geprüft (Serienfertigung)
**Kennzeichnung:** Geprägt oder gelasert am Anfangs-/Endglied
**Prüfung:** Zugprüfung auf Prüflast (ca. 50% der Bruchlast)

**Windlass-Kompatibilität:** DIN 766 ist der europäische Standard. Alle europäischen Windlass-Hersteller (Lofrans, Quick, Muir) bieten Kettennüsse für DIN 766.

**Confidence: measured** — DIN-Norm, Werte aus Norm-Tabellen.

### 2.5 DIN 764 — Rundstahlkette (Langglied)

**DIN 764: Rundstahlkette, langgliedrig**

Die DIN 764 definiert langgliedrige Ketten, die primär für Festmacher, Moorings und industrielle Anwendungen gedacht sind. Für Ankerzwecke mit Windlass sind sie ungeeignet.

**Spezifikationen DIN 764:**

| Durchmesser (mm) | Innenweite (mm) | Innenlänge (mm) | Teilung (mm) | Gewicht (kg/m) |
|---|---|---|---|---|
| 5 | 7,0 | 27,5 | 27,5 | 0,44 |
| 6 | 8,0 | 33,0 | 33,0 | 0,64 |
| 8 | 11,0 | 44,0 | 44,0 | 1,13 |
| 10 | 14,0 | 55,0 | 55,0 | 1,76 |
| 12 | 16,5 | 66,0 | 66,0 | 2,53 |
| 13 | 18,0 | 71,5 | 71,5 | 2,97 |

**Anwendung im Yachtbereich:**
- Mooringketten (permanente Bojenanbindung)
- Ankervorleinen (vor dem Anker, am Grund liegend)
- Festmacher auf massiven Pollern
- Rückhalteketten für Dinghis

> **AYDI-Warnung:** DIN 764 Kette passt NICHT in Standard-Kettennüsse. Der Einsatz als Ankerkette in einer Windlass-Anwendung führt unweigerlich zu Kettenklemmern und kann die Windlass-Mechanik beschädigen.

### 2.6 ISO 4565 — Kalibrierte Kurzgliedkette

**ISO 4565: Ankerketten für Sportboote (Small craft — Anchor chains), kalibriert**

Die ISO 4565 ist der internationale Gegenpart zur DIN 766 und definiert kalibrierte Ankerketten für Sportboot-Ankerwinden (Nenndurchmesser 6–12mm). Im Yachtbereich hat diese Norm Relevanz, weil viele internationale Hersteller (besonders aus Asien) nach ISO 4565 fertigen.

**Unterschiede zu DIN 766:**
- Teilungsmaße können minimal abweichen (±0,5mm)
- Innenweitentoleranz: enger als DIN 766 bei höheren Güten
- Materialanforderungen: höhere Mindestzugfestigkeit bei Grade T
- Kennzeichnung: "ISO 4565" oder "ISO T" geprägt

**Kompatibilität:**
ISO 4565 Ketten in Standardgüte sind meist kompatibel mit DIN-766-Kettennüssen, da die Maße sehr ähnlich sind. Ein Test auf der konkreten Windlass ist dennoch empfohlen.

**Confidence: measured** — ISO-Norm, Werte aus Norm-Tabellen.

### 2.7 US-Güten: G30 (Proof Coil)

**G30 — Proof Coil Chain (ASTM A413, NACM Standard)**

G30 ist die niedrigste Güte, die im US-amerikanischen Markt als Ankerkette verkauft wird. "Proof Coil" bedeutet, dass die Kette einer Prüflast (Proof Load) standgehalten hat.

**Eigenschaften G30:**
- Material: Kohlenstoffstahl, niedrige Festigkeit
- Zugfestigkeit: 370–430 N/mm² (MPa)
- Working Load Limit (WLL): niedrigste aller Güten
- Bruchlast: ca. 4× WLL (Sicherheitsfaktor 4, siehe Lasttabelle)
- Gewicht: gleich wie andere Güten bei gleichem Durchmesser (Material, nicht Güte bestimmt Gewicht)
- Oberfläche: Feuerverzinkt oder selbstfärbend (plain)

**G30 Lasttabelle (NACM):**

| Durchmesser (inch/mm) | WLL (lbs/kg) | Proof Load (lbs/kg) | Bruchlast (lbs/kg) | Gewicht (lbs/ft / kg/m) |
|---|---|---|---|---|
| 1/4" (6,35mm) | 1.300 / 590 | 2.600 / 1.179 | 5.200 / 2.359 | 0,42 / 0,63 |
| 5/16" (7,94mm) | 1.900 / 862 | 3.800 / 1.724 | 7.600 / 3.447 | 0,63 / 0,94 |
| 3/8" (9,53mm) | 2.650 / 1.202 | 5.300 / 2.404 | 10.600 / 4.808 | 0,92 / 1,37 |
| 7/16" (11,11mm) | 3.700 / 1.678 | 7.400 / 3.357 | 14.800 / 6.713 | 1,24 / 1,85 |
| 1/2" (12,70mm) | 4.500 / 2.041 | 9.000 / 4.082 | 18.000 / 8.165 | 1,55 / 2,31 |

**Bewertung für Yachtanwendung:**
- Grundsätzlich geeignet, aber niedrigste empfohlene Güte
- Häufig in günstigen Ketten-Sets für kleine Boote
- Nicht windlass-kalibriert (es sei denn, extra spezifiziert)
- Für Küstenfahrt auf Booten <10m akzeptabel
- Nicht empfohlen für Blauwasserfahrt

**Confidence: documented** — NACM-Spezifikationen und Herstellerangaben.

### 2.8 US-Güten: G40 (High Test BBB)

**G40 — High Test / BBB Chain (ASTM A413)**

G40 ist der De-facto-Standard für Yacht-Ankerketten im US-amerikanischen Markt. "BBB" (Triple-B oder "BB") ist eine historische Bezeichnung für die Kettenklasse, die speziell für marine Windlass-Anwendungen entwickelt wurde.

**Eigenschaften G40 / BBB:**
- Material: Kohlenstoffstahl, mittlere Festigkeit
- Zugfestigkeit: 410–520 N/mm² (MPa)
- Working Load Limit: ca. 40% höher als G30
- Bruchlast: ca. 3× WLL (Sicherheitsfaktor 3, siehe Lasttabelle)
- Kalibriert: Standard für US-Windlass-Hersteller
- Standard bei Lewmar, Maxwell, Muir (in US-Abmessungen)

**G40 Lasttabelle (NACM):**

| Durchmesser (inch/mm) | WLL (lbs/kg) | Proof Load (lbs/kg) | Bruchlast (lbs/kg) | Gewicht (lbs/ft / kg/m) |
|---|---|---|---|---|
| 1/4" (6,35mm) | 2.600 / 1.179 | 5.200 / 2.359 | 7.800 / 3.538 | 0,42 / 0,63 |
| 5/16" (7,94mm) | 3.900 / 1.769 | 7.800 / 3.538 | 11.700 / 5.307 | 0,66 / 0,98 |
| 3/8" (9,53mm) | 5.400 / 2.449 | 10.800 / 4.899 | 16.200 / 7.348 | 0,95 / 1,41 |
| 7/16" (11,11mm) | 7.200 / 3.266 | 14.400 / 6.532 | 21.600 / 9.798 | 1,28 / 1,91 |
| 1/2" (12,70mm) | 9.200 / 4.173 | 18.400 / 8.346 | 27.600 / 12.519 | 1,60 / 2,38 |

**Bewertung für Yachtanwendung:**
- Empfohlener Standard für US-Boote mit Windlass
- Sehr gutes Preis-Leistungs-Verhältnis
- Kalibriert für gängige US-Windlass-Kettennüsse
- Passend für Lewmar V-Serie, Maxwell, Muir
- Äquivalent zur DIN 766 in Bezug auf Kalibrierung und Anwendung

> **AYDI-Empfehlung:** G40/BBB ist der empfohlene US-Standard für Ankerketten. In Europa ist DIN 766 das Äquivalent. Beide Systeme sind NICHT untereinander kompatibel — Kettennüsse müssen zum jeweiligen Standard passen.

**Confidence: measured** — NACM-Spezifikationen, verifiziert durch Herstellerangaben.

### 2.9 US-Güten: G43 (High Test)

**G43 — High Test Chain (ASTM A413)**

G43 ist eine höherfeste Version der G40 und bietet bei gleichem Durchmesser ca. 15–20% höhere Arbeitslast. Im Yachtmarkt weniger verbreitet als G40, aber bei gewichts- und platzbewussten Eignern beliebt.

**Eigenschaften G43:**
- Material: Kohlenstoffstahl, erhöhte Festigkeit durch Legierungszusätze
- Zugfestigkeit: 480–580 N/mm² (MPa)
- Working Load Limit: ca. 15–20% höher als G40
- Gewicht: identisch zu G30/G40 bei gleichem Durchmesser
- Kalibrierung: Verfügbar, aber seltener als G40

**G43 Lasttabelle (NACM):**

| Durchmesser (inch/mm) | WLL (lbs/kg) | Proof Load (lbs/kg) | Bruchlast (lbs/kg) |
|---|---|---|---|
| 1/4" (6,35mm) | 2.900 / 1.315 | 5.800 / 2.631 | 8.750 / 3.969 |
| 5/16" (7,94mm) | 4.500 / 2.041 | 9.000 / 4.082 | 13.500 / 6.124 |
| 3/8" (9,53mm) | 6.500 / 2.948 | 13.000 / 5.897 | 19.500 / 8.845 |
| 7/16" (11,11mm) | 8.750 / 3.969 | 17.500 / 7.938 | 26.250 / 11.907 |
| 1/2" (12,70mm) | 11.200 / 5.080 | 22.400 / 10.160 | 33.600 / 15.241 |

**Bewertung für Yachtanwendung:**
- Gute Option, wenn höhere Festigkeit bei gleichem Durchmesser gewünscht
- Sinnvoll bei Upgrade ohne Kettennuss-Wechsel
- Etwas teurer als G40 (ca. 10–15% Aufpreis)
- Gute Verfügbarkeit im US-Markt

**Confidence: documented** — NACM-Spezifikationen und Herstellerangaben.

### 2.10 US-Güten: G70 (Transport Chain)

**G70 — Transport Chain (ASTM A413)**

G70 ist eine hochfeste Transportkette, die ursprünglich für die Ladungssicherung auf LKW entwickelt wurde. Im Yachtbereich wird sie gelegentlich als leichtgewichtige Alternative diskutiert.

**Eigenschaften G70:**
- Material: Legierter Stahl, wärmebehandelt
- Zugfestigkeit: 700–800 N/mm² (MPa)
- Working Load Limit: ca. 100% höher als G30
- Bruchlast: ca. 4× WLL (NACM/ASTM A413 Design-Faktor 4:1)
- Gewicht: identisch zu anderen Güten bei gleichem Durchmesser
- Kalibrierung: Nicht standardmäßig für marine Windlass

> ✅ Aufgeloest (Audit): NACM Grade 70 (ASTM A413) verwendet Design-Faktor 4:1 — Bruchlast ≈ 4× WLL (z.B. 5/16": WLL 4.700 lbs, Mindestbruchlast 18.800 lbs). Quelle: NACM/ASTM A413 Herstellerspezifikationen (Peerless, US Cargo Control, Harris).

**Vorteile für Yachtanwendung:**
- Höchste Festigkeit pro Durchmesser
- Theoretisch könnte eine Gütestufe kleinerer Durchmesser verwendet werden
- Gewichtseinsparung durch dünnere Kette bei gleicher Arbeitslast

**Nachteile und Warnungen:**
- NICHT kalibriert für marine Kettennüsse
- Kein Korrosionsschutz für marine Umgebung standardmäßig
- Wärmebehandlung kann durch Re-Galvanisierung beeinträchtigt werden
- Sprödbruchgefahr bei Kälte (wärmebehandelter Stahl)
- Keine marine Zulassung oder Prüfung

> **AYDI-Warnung:** G70 Kette ist für marine Ankerzwecke NICHT empfohlen. Die fehlende Kalibrierung, die Sprödbruchgefahr und die mangelnde Korrosionsbeständigkeit machen sie zu einem Sicherheitsrisiko. Die theoretische Gewichtsersparnis durch dünnere Kette wird durch die reduzierte Kettenary-Wirkung konterkariert.

**Confidence: documented** — NACM-Spezifikationen, ergänzt durch marine Fachpresse.

### 2.11 US-Güten: G80 (Alloy Lifting Chain)

**G80 — Alloy Steel Lifting Chain (ASTM A391)**

G80 ist eine hochfeste Legierungskette für Hebezeuge und industrielle Anwendungen. Im Yachtbereich taucht sie gelegentlich in Diskussionen auf.

**Eigenschaften G80:**
- Material: Legierter Stahl, vergütet (gehärtet und angelassen)
- Zugfestigkeit: 800–1.000 N/mm² (MPa)
- Working Load Limit: ca. 2× G30
- Oberfläche: Meist schwarz lackiert oder selbstfärbend
- Kalibrierung: Für Hebezeuge, nicht für marine Windlass

**Gründe gegen den Einsatz als Ankerkette:**

1. **Keine marine Verzinkung**: G80 wird nicht feuerverzinkt angeboten (Wärmebehandlung würde zerstört)
2. **Sprödbruchgefahr**: Vergüteter Stahl ist empfindlich gegen Wasserstoffversprödung
3. **Keine Kalibrierung für Windlass**: Passt nicht in marine Kettennüsse
4. **Korrosion**: Ohne Verzinkung rostet die Kette im Seewasser extrem schnell
5. **Nicht reparierbar**: Geschweißte Reparaturen zerstören die Wärmebehandlung
6. **Kein Sicherheitsstandard für marine Anwendung**

> **AYDI-Warnung:** G80 ist für Ankerketten KATEGORISCH UNGEEIGNET. Die Verwendung stellt ein erhebliches Sicherheitsrisiko dar. Kein seriöser Yacht-Ausrüster bietet G80 als Ankerkette an.

**Confidence: measured** — NACM-Spezifikationen und ASTM-Normen.

### 2.12 Vergleichstabelle aller Güten

| Eigenschaft | DIN 766 | G30 | G40/BBB | G43 | G70 | G80 |
|---|---|---|---|---|---|---|
| Zugfestigkeit (MPa) | 370–500 | 370–430 | 410–520 | 480–580 | 700–800 | 800–1.000 |
| Marine-geeignet | Ja | Bedingt | Ja | Ja | Nein | Nein |
| Windlass-kalibriert | Ja | Nein* | Ja | Verfügbar | Nein | Nein |
| Feuerverzinkung | Standard | Standard | Standard | Standard | Selten | Nein |
| Preis (10mm, pro m) | 5–8 EUR | 3–5 USD | 5–8 USD | 6–10 USD | 8–12 USD | 10–15 USD |
| Empfehlung Yacht | Standard EU | Minimum | Standard US | Upgrade | Nicht empf. | Ungeeignet |

*G30 kann kalibriert verfügbar sein, ist aber nicht der Standard.

### 2.13 Gütebezeichnungen und Verwechslungsgefahr

In der Praxis kommt es häufig zu Verwechslungen zwischen europäischen und US-amerikanischen Gütebezeichnungen. Dies kann zu gefährlichen Situationen führen:

**Häufige Verwechslungen:**

| Bezeichnung | Tatsächlich | Oft verwechselt mit |
|---|---|---|
| "ISO Kette" | ISO 4565 kalibriert | DIN 766 (ähnlich, aber nicht identisch) |
| "BBB" | G40 High Test | G30 Proof Coil |
| "High Test" | G43 oder G40 | G70 Transport |
| "Kalibrierte Kette" | DIN 766 oder ISO 4565 | Jede beliebige Kurzgliedkette |
| "Marine Grade" | Kein definierter Standard | Beliebige Qualitätsstufe |
| "Edelstahlkette" | 316L oder 304 | Keine Güteangabe = Risiko |

**Prüfpunkte beim Kauf:**
1. Exakte Normbezeichnung verlangen (DIN 766, ASTM A413 G40 etc.)
2. Prüfzertifikat (Mill Certificate) anfordern
3. Kalibrierungs-Bestätigung für Windlass-Anwendung
4. Verzinkungsnachweis (EN ISO 1461 oder ASTM A153)
5. Ein Testglied auf der eigenen Kettennuss prüfen

### 2.14 Spezialtypen: Duplex-Kette

**Duplex-Stahlkette (Duplex Stainless Steel):**
- Material: Duplex 2205 (UNS S31803)
- Zugfestigkeit: ca. 620 MPa (doppelt so hoch wie 316L)
- Korrosionsbeständigkeit: besser als 316L
- Gewicht: identisch zu Standard-Edelstahl
- Preis: ca. 3–4× Preis von verzinkter Stahlkette
- Verfügbarkeit: Sehr eingeschränkt, Sonderanfertigung
- Anwendung: Superyachten, wo Rostfreiheit UND Festigkeit gefordert

**Bewertung:**
Duplex-Kette ist die technisch beste, aber auch teuerste Lösung. Sie kombiniert die Korrosionsbeständigkeit von Edelstahl mit deutlich höherer Festigkeit. Für Yachten unter 20m ist sie wirtschaftlich selten sinnvoll.

### 2.15 Spezialtypen: Beschichtete Ketten

**Polyester-beschichtete Kette (z.B. Maggi Aqua-Met):**
- Basis: Feuerverzinkter Stahl nach DIN 766
- Beschichtung: Polyester- oder PVC-Ummantelung
- Farben: Schwarz, Weiß, Blau, Rot
- Zweck: Schutz von Gelcoat und Teak im Bugbereich
- Nachteile: Beschichtung nutzt sich ab, verdeckt Korrosion
- Preis: ca. 50–80% Aufpreis gegenüber blanker Verzinkung

> **AYDI-Hinweis:** Beschichtete Ketten verdecken den Zustand der Verzinkung. Regelmäßige Inspektion ist bei beschichteten Ketten SCHWIERIGER, nicht einfacher. Die Beschichtung ist kein Ersatz für intakte Verzinkung.

---

## 3. Kettendimensionierung

### 3.1 Grundregel: Bootslänge und Verdrängung

Die Kettendimensionierung richtet sich primär nach der Bootsgröße (Länge über alles und Verdrängung), dem Fahrtengebiet und den zu erwartenden Bedingungen.

**Dimensionierungstabelle nach Bootslänge:**

| Bootslänge (m) | Verdrängung (t) | Empf. Kette (mm) | Min. Kette (mm) | Empf. Länge (m) |
|---|---|---|---|---|
| 6–8 | 1,5–3,0 | 6 | 6 | 30–40 |
| 8–10 | 3,0–6,0 | 8 | 6 | 40–60 |
| 10–12 | 6,0–10,0 | 8 | 8 | 50–70 |
| 12–14 | 10,0–16,0 | 10 | 8 | 60–80 |
| 14–16 | 14,0–22,0 | 10 | 10 | 70–100 |
| 16–18 | 18,0–30,0 | 10–12 | 10 | 80–100 |
| 18–22 | 25,0–45,0 | 12 | 10 | 100–120 |
| 22–26 | 35,0–70,0 | 12–13 | 12 | 100–150 |
| 26–30 | 50,0–100,0 | 13–14 | 12 | 120–150 |

**Confidence: documented** — Zusammenstellung aus ABYC H-40, Herstellerempfehlungen und Erfahrungswerten.

### 3.2 ABYC H-40 Standard

Der amerikanische ABYC (American Boat and Yacht Council) Standard H-40 "Anchoring, Mooring, and Strong Points" definiert Empfehlungen für die Ankerketten-Dimensionierung:

**ABYC H-40 Kernpunkte:**
- Horizontal Load (HL): abhängig von Bootslänge, Typ und Windstärke
- Design Load: HL × 1,5 Sicherheitsfaktor
- Kette WLL muss Design Load übersteigen
- Scope-Empfehlungen: mindestens 5:1 für normale Bedingungen, 7:1 für Sturm

**Windlast-Berechnung nach ABYC H-40:**

```
Horizontal Load (lbs) = (PA × Area_bow × Cd) + (PA × Area_hull × Cd × cos²α)

wobei:
  PA = Staudruck (psf) = 0,00256 × V² (V in Knoten)
  Area_bow = projizierte Bugfläche (ft²)
  Area_hull = projizierte Rumpffläche (ft²)
  Cd = Widerstandsbeiwert (typ. 1,0–1,3)
  α = Windwinkel (0° = von vorn)
```

**Vereinfachte Tabelle — Horizontalkraft nach ABYC H-40:**

| Bootslänge (ft/m) | 15 kn (lbs/N) | 30 kn (lbs/N) | 42 kn (lbs/N) | 60 kn (lbs/N) |
|---|---|---|---|---|
| 20 / 6,1 | 40 / 178 | 160 / 712 | 315 / 1.401 | 640 / 2.847 |
| 25 / 7,6 | 60 / 267 | 240 / 1.068 | 470 / 2.091 | 960 / 4.271 |
| 30 / 9,1 | 80 / 356 | 320 / 1.423 | 625 / 2.781 | 1.280 / 5.694 |
| 35 / 10,7 | 100 / 445 | 400 / 1.779 | 785 / 3.492 | 1.600 / 7.117 |
| 40 / 12,2 | 125 / 556 | 500 / 2.224 | 980 / 4.360 | 2.000 / 8.896 |
| 45 / 13,7 | 150 / 667 | 600 / 2.669 | 1.175 / 5.227 | 2.400 / 10.675 |
| 50 / 15,2 | 175 / 778 | 700 / 3.114 | 1.370 / 6.094 | 2.800 / 12.455 |
| 60 / 18,3 | 225 / 1.001 | 900 / 4.003 | 1.760 / 7.829 | 3.600 / 16.013 |

### 3.3 Scope-Berechnung

Der Scope (Verhältnis ausgegebener Rode zu Wassertiefe) ist der wichtigste Faktor für die Ankerhaltekraft nach dem Ankerdesign selbst.

**Scope-Berechnung:**

```
Scope = L_rode / (D_wasser + H_bug)

wobei:
  L_rode = Länge der ausgegebenen Kette/Rode (m)
  D_wasser = Wassertiefe bei Hochwasser (m)
  H_bug = Höhe der Bugrolle über Wasser (m)
```

**Scope-Empfehlungen für Ganzkette:**

| Bedingung | Min. Scope | Empf. Scope | Kommentar |
|---|---|---|---|
| Ruhige Bedingungen, kurz | 3:1 | 4:1 | Nur für Mittagspause |
| Normale Nacht-Ankerung | 4:1 | 5:1 | Standardwert |
| Starkwind erwartet (>20 kn) | 5:1 | 7:1 | Sicherheit erhöhen |
| Sturm (>30 kn) | 7:1 | 10:1 | Maximale Sicherheit |
| Enges Ankern (Bucht) | 3:1 | 4:1 | Schwoikreis beachten! |

**Scope-Empfehlungen für Mixed Rode (Kette + Nylon):**
Wenn nur ein Teil der Rode Kette ist, muss der Scope erhöht werden, da die Nylon-Leine keine Kettenary erzeugt:
- Kettenanteil >50%: Scope wie Ganzkette
- Kettenanteil 30–50%: Scope +1 gegenüber Ganzkette
- Kettenanteil <30%: Scope +2 gegenüber Ganzkette

**Beispielrechnung:**
```
Boot: 12m Segelyacht
Wassertiefe: 5m (Niedrigwasser) + 1,5m Tidenhub = 6,5m Hochwasser
Bughöhe: 1,5m
Bedingung: Normale Nachtankerung
Scope: 5:1

Benötigte Kette = 5 × (6,5m + 1,5m) = 5 × 8m = 40m
```

### 3.4 Kettenlängen-Empfehlungen nach Fahrtengebiet

**Küstenfahrt (Ostsee, Mittelmeer, Kanäle):**

| Parameter | Empfehlung |
|---|---|
| Kettenlänge | 40–60m |
| Kettentyp | DIN 766, 8mm (Boote bis 12m), 10mm (12–16m) |
| Scope | 4:1 bis 5:1 |
| Typische Ankertiefen | 3–10m |
| Reservekapazität | 20% über Maximum-Scope |
| Alternativ | Mixed Rode: 20m Kette + 40m Nylon |

**Offshore-Fahrt (Biskaya, Nordsee, Atlantik-Küste):**

| Parameter | Empfehlung |
|---|---|
| Kettenlänge | 60–80m |
| Kettentyp | DIN 766, 8–10mm (Boote bis 14m), 10–12mm (>14m) |
| Scope | 5:1 bis 7:1 |
| Typische Ankertiefen | 5–15m |
| Reservekapazität | 30% über Maximum-Scope |
| Alternativ | Mixed Rode: 30m Kette + 50m Nylon |

**Blauwasserfahrt (Atlantiküberquerung, Weltumseglung):**

| Parameter | Empfehlung |
|---|---|
| Kettenlänge | 80–120m |
| Kettentyp | DIN 766, 10mm (Boote bis 14m), 10–12mm (>14m) |
| Scope | 5:1 bis 10:1 |
| Typische Ankertiefen | 3–25m (Atolle, offene Buchten) |
| Reservekapazität | 50% über Maximum-Scope |
| Zweitkette | Empfohlen: 20–30m als Backup |
| Alternativ | Keine Mixed Rode empfohlen — Ganzkette Standard |

### 3.5 Mixed Rode — Kette + Leine

**Aufbau einer Mixed Rode:**

```
[Anker] — [Schäkel] — [Kette 10-20m] — [Kette-Leine-Verbindung] — [Nylon-Leine 40-60m] — [Boot]
```

**Kette-Leine-Verbindung:**
Die Verbindung zwischen Kette und Leine ist das kritischste Element einer Mixed Rode. Optionen:

| Verbindungstyp | Haltekraft | Handhabung | Windlass-Fähigkeit | Preis |
|---|---|---|---|---|
| Gespleißtes Auge + Schäkel | 90–95% der Leinenkraft | Gut | Problematisch | Niedrig |
| Kettenkonnekter (z.B. Kong) | 100% der Leinenkraft | Sehr gut | Gut | Mittel |
| Dyneema-Verbindung | 95–100% | Gut | Gut | Mittel |
| Schraubschäkel | 80–90% | Mittel | Problematisch | Niedrig |

**Leinen-Empfehlungen für Mixed Rode:**

| Kettenmaß (mm) | Leinendurchmesser (mm) | Leinentyp | Bruchlast Leine (kN) |
|---|---|---|---|
| 6 | 12–14 | 3-schäftig Nylon | 18–24 |
| 8 | 14–16 | 3-schäftig Nylon | 24–32 |
| 10 | 16–18 | 3-schäftig Nylon | 32–42 |
| 12 | 18–20 | 3-schäftig Nylon | 42–52 |
| 14 | 20–22 | 3-schäftig Nylon | 52–64 |

**Warum 3-schäftiges Nylon?**
Gedrehtes (3-schäftiges) Nylon hat ca. 15–20% Dehnung und wirkt als Stoßdämpfer. Geflochtenes Nylon hat nur ca. 8–12% Dehnung. Die Dehnung ist der Hauptgrund für die Wahl von Nylon als Ankerleine.

### 3.6 Kettenmarkierungssysteme

Eine zuverlässige Kettenmarkierung ist essenziell, um die ausgegebene Kettenlänge zu kontrollieren. Ohne Markierung weiß der Skipper nicht, wie viel Kette draußen ist.

**System 1: Farbmarkierung mit Sprühlack**

| Meter | Farbe | Muster |
|---|---|---|
| 10m | Rot | 1 Glied |
| 15m | Rot | 2 Glieder |
| 20m | Gelb | 1 Glied |
| 25m | Gelb | 2 Glieder |
| 30m | Blau | 1 Glied |
| 35m | Blau | 2 Glieder |
| 40m | Rot | 3 Glieder |
| 45m | Gelb | 3 Glieder |
| 50m | Blau | 3 Glieder |
| 60m | Rot | 4 Glieder |
| 70m | Gelb | 4 Glieder |
| 80m | Blau | 4 Glieder |
| 90m | Rot/Gelb | je 2 Glieder |
| 100m | Rot/Gelb/Blau | je 2 Glieder |

**System 2: Kabelbinder (Cable Ties)**

Farbige Kabelbinder werden an spezifischen Gliedern befestigt:
- 1 Kabelbinder = 10m
- 2 Kabelbinder = 20m
- 3 Kabelbinder = 30m
- usw.

Farben können nach System 1 verwendet werden.

Vorteile: Einfach anzubringen, im Kettenkasten sichtbar, ersetzen sich leicht
Nachteile: Können abreißen, im Windlass-Durchlauf problematisch

**System 3: Farbige Kunststoff-Glieder (Chain Markers)**

Dedizierte Kunststoff-Marker, die zwischen Kettenglieder gesteckt werden:
- Hersteller: Niko, Muir, Quick
- Farben: wie System 1
- Vorteil: Windlass-kompatibel, haltbar
- Nachteil: Können bei Verdrehen der Kette verloren gehen

**System 4: Kettenrechner (Chain Counter)**

Elektronische Zähler, die an der Kettennuss montiert werden:
- Hersteller: Quick, Lofrans, Maxwell, Lewmar
- Genauigkeit: ±1–2% bei korrekt kalibrierter Kette
- Kalibrierung: Alle 2–3 Jahre prüfen, nach Kettenwechsel neu kalibrieren
- Anzeige: Digital, oft integriert in Ankersteuerung

> **AYDI-Empfehlung:** Kombinieren Sie mindestens zwei Systeme — idealerweise Farbmarkierung PLUS Kettenzähler. Farbmarkierung allein ist bei Dunkelheit oder wenn der Vormann vom Cockpit aus steuert unzureichend.

### 3.7 Berechnung des Kettengewichts im Bug

Das Kettengewicht hat signifikante Auswirkungen auf die Trimmung, insbesondere bei leichten Yachten:

**Gewicht der Ankerkette im Bug:**

| Kette (mm) | 40m (kg) | 60m (kg) | 80m (kg) | 100m (kg) |
|---|---|---|---|---|
| 6mm DIN 766 | 31,6 | 47,4 | 63,2 | 79,0 |
| 8mm DIN 766 | 56,0 | 84,0 | 112,0 | 140,0 |
| 10mm DIN 766 | 88,0 | 132,0 | 176,0 | 220,0 |
| 12mm DIN 766 | 126,0 | 189,0 | 252,0 | 315,0 |
| 13mm DIN 766 | 148,0 | 222,0 | 296,0 | 370,0 |
| 14mm DIN 766 | 172,0 | 258,0 | 344,0 | 430,0 |

**Auswirkung auf den Trimm:**

```
Trimm-Änderung (mm) ≈ (Kettengewicht × Abstand_zum_LCG) / (Verdrängung × GM_L)

Beispiel: 12m Segelyacht, 8.000 kg Verdrängung, GM_L = 5m
100m × 10mm Kette = 220 kg im Bug (ca. 5m vor LCG)
Trimm-Änderung ≈ (220 × 5) / (8.000 × 5) = 27,5 mm Buglastigkeit
```

Bei leichten Booten (Regattadesigns, Katamarane) kann dieser Effekt erheblich sein. Lösung: Kettenkasten weiter mittschiffs verlegen oder Mixed Rode verwenden.

### 3.8 Windlass-Leistung und Kettendimensionierung

Die Kettendimensionierung muss mit der Windlass-Kapazität abgestimmt sein:

**Windlass-Leistungsklassen:**

| Windlass-Klasse | Max. Kette (mm) | Max. Zugkraft (kg) | Typische Boote |
|---|---|---|---|
| 500W | 6–8 | 350–500 | 7–10m |
| 700W | 8–10 | 500–700 | 10–12m |
| 1.000W | 8–10 | 700–1.000 | 12–14m |
| 1.500W | 10–12 | 1.000–1.500 | 14–18m |
| 2.000W | 12–13 | 1.500–2.000 | 18–22m |
| 2.500W | 13–14 | 2.000–2.500 | 22–26m |
| 3.500W | 14–16 | 2.500–3.500 | 26–30m |

**Wichtig:** Die Windlass-Zugkraft muss das Gewicht der maximalen Kettenlänge PLUS den vertikalen Zug des Ankers + Kette im Wasser überwinden. Faustregel: Windlass muss mindestens 3× das Gewicht von Anker + Kette bei maximaler Tiefe ziehen können.

---

## 4. Kettenmaterialien

### 4.1 Feuerverzinkter Baustahl — Der Standard

**Material: Unlegierter Baustahl S235JR / A36**

Feuerverzinkter Baustahl ist das Standardmaterial für 99% aller Yacht-Ankerketten. Die Kombination aus ausreichender Festigkeit, gutem Korrosionsschutz und vertretbarem Preis macht ihn zur ersten Wahl.

**Eigenschaften des Grundmaterials:**
- Zugfestigkeit: 360–510 MPa (je nach Norm und Güte)
- Streckgrenze: min. 235 MPa
- Bruchdehnung: >26% (duktil, warnt vor Bruch)
- Dichte: 7.850 kg/m³
- E-Modul: 210.000 MPa
- Magnetisch: Ja (kann Kompass beeinflussen)

**Korrosionsverhalten ohne Schutz:**
- Korrosionsrate in Seewasser: 0,1–0,3 mm/Jahr (beidseitig)
- In Spritzwasser/Wechselzone: 0,05–0,15 mm/Jahr
- Vollständig untergetaucht (ohne O₂): 0,02–0,05 mm/Jahr
- Lebensdauer ohne Verzinkung: 2–5 Jahre bis zum Versagen

### 4.2 Feuerverzinkung — Normen und Qualität

**EN ISO 1461: Feuerverzinkung auf Stahl**

Die Feuerverzinkung (Hot-Dip Galvanizing, HDG) ist der Standard-Korrosionsschutz für Ankerketten. Dabei wird die Kette in ein Bad aus flüssigem Zink (ca. 450°C) getaucht.

**Prozess:**
1. Entfetten (alkalisches Bad)
2. Beizen (Salzsäure, entfernt Rost und Zunder)
3. Flussmittel (Zinkammoniumchlorid)
4. Verzinken (Eintauchen in Zinkbad, 450°C, 3–6 Minuten)
5. Abkühlen (Luft oder Wasserbad)
6. Inspektion und Prüfung

**Schichtdicke nach EN ISO 1461:**

| Materialdicke | Min. mittlere Schichtdicke | Min. lokale Schichtdicke |
|---|---|---|
| >6mm | 70 µm (505 g/m²) | 55 µm (395 g/m²) |
| >3mm bis ≤6mm | 55 µm (395 g/m²) | 45 µm (325 g/m²) |
| ≥1,5mm bis ≤3mm | 45 µm (325 g/m²) | 35 µm (250 g/m²) |

**Für Ankerketten relevante Schichtdicken:**
- 6mm Kette: min. 45 µm (Drahtdurchmesser ≤6mm)
- 8mm Kette: min. 55 µm (Drahtdurchmesser >6mm)
- 10mm+ Kette: min. 70 µm

**Lebensdauer der Verzinkung in mariner Umgebung:**

| Umgebung | Abtragrate Zink (µm/Jahr) | Lebensdauer bei 70µm |
|---|---|---|
| Atmosphäre (Küste) | 1–3 | 25–70 Jahre |
| Spritzwasser | 5–15 | 5–14 Jahre |
| Seewasser (getaucht) | 10–25 | 3–7 Jahre |
| Kettenkasten (feucht) | 3–8 | 9–23 Jahre |
| Im Einsatz (gemischt) | 8–20 | 3,5–9 Jahre |

**Confidence: measured** — EN ISO 1461 Normwerte und Langzeitstudien der Verzinkungsindustrie.

### 4.3 ASTM A153 — US-Verzinkungsstandard

**ASTM A153: Standard Specification for Zinc Coating (Hot-Dip) on Iron and Steel Hardware**

Der US-Standard ASTM A153 definiert die Verzinkungsanforderungen für Befestigungselemente und Hardware — einschließlich Ketten.

**Mindestschichtdicken nach ASTM A153:**

| Klasse | Artikeltyp | Min. Schichtdicke (oz/ft² / µm) |
|---|---|---|
| B | Formteile, Verbinder | 2,0 / 86 |
| C | Befestigungselemente >3/8" | 1,25 / 54 |
| D | Befestigungselemente ≤3/8" | 1,00 / 43 |

Ankerketten fallen typisch unter Klasse B oder C.

**Vergleich ASTM A153 vs. EN ISO 1461:**
- ASTM A153 Class B (86 µm) > EN ISO 1461 für >6mm (70 µm)
- US-Ketten haben tendenziell dickere Verzinkung
- Praxis: Beide Standards liefern vergleichbare Lebensdauer

### 4.4 Re-Galvanisierung — Prozess und Wirtschaftlichkeit

**Wann Re-Galvanisieren?**

Eine Ankerkette sollte re-galvanisiert werden, wenn:
- Mehr als 50% der sichtbaren Oberfläche blanken Stahl zeigt
- Rostflecken größer als Daumennagel auftreten
- Die Kette mehr als 5–7 Jahre im Einsatz war (bei regelmäßiger Nutzung)
- Einzelne Glieder merklich dünner erscheinen als neue

**Prozess der Re-Galvanisierung:**

1. **Anlieferung:** Kette wird aufgetrommelt oder in Waschkörben angeliefert
2. **Entrostung:** Sandstrahlen oder Beizen in Salzsäure
3. **Inspektion:** Prüfung auf Verschleiß, Risse, Längung (>5% = Austausch)
4. **Flussmittel:** Zinkammoniumchlorid-Bad
5. **Verzinkung:** Eintauchen in Zinkbad (450°C)
6. **Inspektion:** Schichtdickenmessung, visuelle Prüfung
7. **Verpackung:** Auf Trommel oder in Fass

**Kosten der Re-Galvanisierung (Stand 2026):**

| Kettenlänge | Kettenmaß | Kosten Re-Galv. | Kosten Neukauf | Empfehlung |
|---|---|---|---|---|
| 50m | 8mm | 150–250 EUR | 300–450 EUR | Re-Galv. lohnt |
| 50m | 10mm | 200–350 EUR | 450–650 EUR | Re-Galv. lohnt |
| 50m | 12mm | 300–450 EUR | 600–900 EUR | Re-Galv. lohnt |
| 100m | 8mm | 300–450 EUR | 550–850 EUR | Re-Galv. lohnt |
| 100m | 10mm | 400–600 EUR | 800–1.200 EUR | Re-Galv. lohnt |
| 100m | 12mm | 550–800 EUR | 1.100–1.700 EUR | Re-Galv. lohnt |

**Bezugsquellen für Re-Galvanisierung in Europa:**
- Voigt & Schweitzer (Deutschland, mehrere Standorte)
- Wiegel Feuerverzinkung (Deutschland, >30 Standorte)
- Zinkpower (international)
- Lokale Verzinkereien: Anfrage mit "Feuerverzinkung Kleinteil-Lohnauftrag"

**Confidence: documented** — Preise geschätzt basierend auf Marktrecherche 2025/2026, regional variabel.

### 4.5 Edelstahl 316L Kette — Vor- und Nachteile

**Material: Austenitischer Edelstahl 1.4404 (AISI 316L)**

Edelstahl-Ankerketten sind eine Premium-Alternative zu verzinktem Stahl. Sie werden vor allem auf Yachten eingesetzt, wo Ästhetik, Sauberkeit und Wartungsfreiheit im Vordergrund stehen.

**Mechanische Eigenschaften 316L:**
- Zugfestigkeit: 480–620 MPa
- Streckgrenze: min. 170 MPa (deutlich niedriger als Baustahl!)
- Bruchdehnung: >40%
- Dichte: 8.000 kg/m³ (ca. 2% schwerer als Stahl)
- Magnetisch: Nein (Vorteil bei Kompass-Nähe)

**Vorteile:**
1. Korrosionsfrei in Seewasser (keine Verzinkung nötig)
2. Ästhetisch (glänzend, kein Rost)
3. Kein Zinkabrieb auf Deck und Gelcoat
4. Kompass-neutral (nicht magnetisch)
5. Kein Re-Galvanisieren nötig
6. Lebensdauer: 20+ Jahre bei korrekter Legierung

**Nachteile:**
1. Niedrigere Streckgrenze → bei gleicher Bruchlast größerer Durchmesser nötig
2. Crevice Corrosion (Spaltkorrosion) in sauerstoffarmer Umgebung (Kettenkasten!)
3. Preis: ca. 3–5× teurer als verzinkter Stahl
4. Elektrolyse-Risiko bei Kontakt mit anderen Metallen
5. Schwer zu prüfen: Korrosion von innen, nicht sichtbar
6. Falsche Legierung (304 statt 316L) = Desaster im Seewasser

**Preisvergleich (pro Meter, inkl. MwSt., 2026):**

| Kettenmaß | Verzinkt DIN 766 | Edelstahl 316L |
|---|---|---|
| 6mm | 3,50–5,00 EUR | 12–18 EUR |
| 8mm | 5,50–8,00 EUR | 18–28 EUR |
| 10mm | 8,00–12,00 EUR | 28–42 EUR |
| 12mm | 11,00–16,00 EUR | 38–58 EUR |

> **AYDI-Warnung:** Edelstahl 316L Kette hat eine NIEDRIGERE Streckgrenze als verzinkter Baustahl. Bei gleicher Bruchlast-Anforderung muss eine Nummer größerer Durchmesser gewählt werden. Beispiel: Wo 10mm verzinkter Stahl ausreicht, sollte 12mm Edelstahl verwendet werden.

### 4.6 Spaltkorrosion bei Edelstahlketten

Spaltkorrosion (Crevice Corrosion) ist die größte Gefahr bei Edelstahl-Ankerketten. Sie tritt in sauerstoffarmen Bereichen auf — genau dort, wo Kettenglieder ineinandergreifen.

**Mechanismus:**
1. Im Spalt zwischen zwei Gliedern wird der Sauerstoff verbraucht
2. Das Passivierungsschicht (Chromoxid) kann sich nicht regenerieren
3. Chlorid-Ionen aus dem Seewasser greifen den ungeschützten Stahl an
4. Korrosion schreitet von innen nach außen fort — unsichtbar!
5. Plötzliches Versagen unter Last

**Risikofaktoren:**
- Kette liegt dauerhaft in stehendem Seewasser (Kettenkasten ohne Drainage)
- Kette liegt wochen- oder monatelang nicht bewegt
- Hohe Wassertemperaturen (Tropen) beschleunigen den Prozess
- Verschmutzung (Schlamm, Sand) in den Spalten

**Prävention:**
- Kettenkasten muss VOLLSTÄNDIG entwässert werden
- Kette nach jedem Einsatz mit Frischwasser spülen
- Regelmäßig die Kette durchlaufen lassen (Glieder bewegen)
- Niemals Edelstahlkette in stehendem Salzwasser lagern
- Jährliche Inspektion: auf dem ganzen Verlauf Glieder einzeln prüfen

**Confidence: documented** — Marine-Korrosionsliteratur, bestätigt durch zahlreiche Praxisberichte.

### 4.7 Kettenbeschichtungen

**Aqua-Met (Polyester-Beschichtung):**
- Hersteller: Maggi (Italien)
- Beschichtung: Polyester über Feuerverzinkung
- Schichtdicke: ca. 200–400 µm
- Farben: Schwarz, Weiß, Blau
- Vorteil: Schützt Gelcoat, reduziert Lärm im Kettenkasten
- Nachteil: Nutzt sich ab (2–5 Jahre), verdeckt Verzinkungszustand
- Preis: ca. 40–80% Aufpreis
- Windlass: Spezial-Kettennuss nötig (größerer Durchmesser durch Beschichtung!)

**Kettenlack (Chain Paint):**
- Typ: Metallschutzlack auf Epoxid- oder PU-Basis
- Auftrag: Streichen oder Sprühen nach Reinigung
- Schichtdicke: 30–80 µm
- Zweck: Kosmetisch, temporärer Zusatzschutz
- Haltbarkeit: 1–3 Saisons
- Nachteil: Blättert in der Kettennuss ab, kann Windlass verschmutzen

**Zinksilikat-Grundierung:**
- Typ: Zinkstaubfarbe (Cold Galvanizing Compound)
- Produkte: ZRC, Galvit, CRC Zinc-It
- Zweck: Reparatur beschädigter Verzinkungsstellen
- Auftrag: Spray oder Pinsel auf sandgestrahlte/geschliffene Stelle
- Haltbarkeit: 2–5 Jahre (deutlich weniger als HDG)
- Anwendung: Notfall-Reparatur, nicht als Ersatz für HDG

### 4.8 Kettenöl und Schmiermittel

**Braucht eine Ankerkette Schmierung?**

Grundsätzlich nein. Die Kette arbeitet in einem Seewasser-Umfeld, das natürlich schmiert. Jedoch gibt es spezifische Anwendungsfälle:

**Windlass-Schmierung:**
- Die Kettennuss/Gypsy kann von leichter Schmierung profitieren
- Produkte: Teflon-Spray, Lanolin-Spray (z.B. Lanotec)
- NICHT verwenden: Fett (sammelt Schmutz), WD-40 (wäscht Fett aus)
- Frequenz: 2–3× pro Saison

**Kettenkasten-Konservierung:**
- Während der Winterlagerung: Kette mit Lanolin oder ACF-50 einsprühen
- Verhindert Korrosion während der Standzeit
- Vor erster Nutzung: nicht nötig abzuwaschen (biologisch abbaubar)

---

## 5. Kettenmaße und Kompatibilität

### 5.1 6mm Kette — Spezifikationen und Anwendung

**6mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 6,0 mm |
| Innenweite | 8,4 mm |
| Innenlänge | 21,0 mm |
| Teilung | 21,0 mm |
| Außenmaß Breite | 20,4 mm |
| Außenmaß Länge | 33,0 mm |
| Gewicht pro Meter | 0,79 kg |
| Bruchlast (verzinkt) | ca. 9,0 kN (918 kg) |
| Prüflast | ca. 4,5 kN (459 kg) |
| WLL (Faktor 4) | ca. 2,25 kN (230 kg) |

**Anwendungsbereich:**
- Boote: 6–8m (Jollen, Daysailer, kleine Kajütboote)
- Verdrängung: bis ca. 3 Tonnen
- Ankergewicht: 5–8 kg (Delta, Bruce, CQR)
- Typische Windlass: 300–500W (Lofrans X1, Lewmar V1)

**Windlass-Kompatibilität 6mm:**

| Hersteller | Modelle | Kettennuss |
|---|---|---|
| Lofrans | X1, Cayman 88 | 6mm DIN 766 (Standard) |
| Lewmar | V1, Pro-Series 700 | 6mm DIN 766 (Tausch-Gypsy) |
| Quick | Aleph | 6mm DIN 766 |
| Maxwell | HRC6 | 6mm DIN 766 |

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.2 8mm Kette — Spezifikationen und Anwendung

**8mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 8,0 mm |
| Innenweite | 11,3 mm |
| Innenlänge | 28,0 mm |
| Teilung | 28,0 mm |
| Außenmaß Breite | 27,3 mm |
| Außenmaß Länge | 44,0 mm |
| Gewicht pro Meter | 1,40 kg |
| Bruchlast (verzinkt) | ca. 16,0 kN (1.631 kg) |
| Prüflast | ca. 8,0 kN (816 kg) |
| WLL (Faktor 4) | ca. 4,0 kN (408 kg) |

**Anwendungsbereich:**
- Boote: 8–12m (Standardsegelyachten, kleine Motoryachten)
- Verdrängung: 3–10 Tonnen
- Ankergewicht: 8–15 kg
- Häufigste Größe im europäischen Yachtmarkt

**Dies ist die meistverkaufte Ankerkettengröße für Segelyachten in Europa.**

**Windlass-Kompatibilität 8mm:**

| Hersteller | Modelle | Kettennuss | Kommentar |
|---|---|---|---|
| Lofrans | X2, Tigres, Kobra | 8mm DIN 766 | Europäischer Marktführer |
| Lewmar | V2, V3, Pro-Fish 700 | 8mm DIN 766 | Tausch-Gypsy verfügbar |
| Quick | Genius, Hector | 8mm DIN 766 | Italienischer Hersteller |
| Maxwell | RC8, HRC8 | 8mm DIN 766 | Australisch/Neuseeländisch |
| Muir | VR500, VR1000 | 8mm DIN 766 | Australisch |
| Vetus | MAXWELL | 8mm DIN 766 | OEM für viele Werften |
| Italwinch | Smart Plus | 8mm DIN 766 | Budget-Option |

**Preis 8mm DIN 766 (Stand 2026, pro Meter):**
- Standard verzinkt: 5,50–7,00 EUR
- Premium verzinkt (Maggi, Titan): 7,00–9,00 EUR
- Edelstahl 316L: 18,00–28,00 EUR
- Aqua-Met beschichtet: 10,00–14,00 EUR

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.3 10mm Kette — Spezifikationen und Anwendung

**10mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 10,0 mm |
| Innenweite | 14,0 mm |
| Innenlänge | 35,0 mm |
| Teilung | 35,0 mm |
| Außenmaß Breite | 34,0 mm |
| Außenmaß Länge | 55,0 mm |
| Gewicht pro Meter | 2,20 kg |
| Bruchlast (verzinkt) | ca. 25,0 kN (2.549 kg) |
| Prüflast | ca. 12,5 kN (1.275 kg) |
| WLL (Faktor 4) | ca. 6,25 kN (637 kg) |

**Anwendungsbereich:**
- Boote: 12–18m (mittlere bis große Segelyachten, Motoryachten)
- Verdrängung: 10–30 Tonnen
- Ankergewicht: 15–25 kg
- Standard für Blauwasseryachten ab 12m

**Windlass-Kompatibilität 10mm:**

| Hersteller | Modelle | Kettennuss | Min. Leistung |
|---|---|---|---|
| Lofrans | Kobra, Royal, Dorado | 10mm DIN 766 | 1.000W |
| Lewmar | V4, V5, Pro-Series 1000 | 10mm DIN 766 | 1.000W |
| Quick | Hector, Prince DP3 | 10mm DIN 766 | 1.000W |
| Maxwell | RC10, HRC10, Freedom | 10mm DIN 766 | 1.000W |
| Muir | VR2000, VR2500 | 10mm DIN 766 | 1.500W |
| Lofrans | Falkon | 10mm DIN 766 | 1.500W |

**Preis 10mm DIN 766 (Stand 2026, pro Meter):**
- Standard verzinkt: 8,00–11,00 EUR
- Premium verzinkt: 11,00–14,00 EUR
- Edelstahl 316L: 28,00–42,00 EUR
- Aqua-Met beschichtet: 15,00–22,00 EUR

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.4 12mm Kette — Spezifikationen und Anwendung

**12mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 12,0 mm |
| Innenweite | 16,8 mm |
| Innenlänge | 42,0 mm |
| Teilung | 42,0 mm |
| Außenmaß Breite | 40,8 mm |
| Außenmaß Länge | 66,0 mm |
| Gewicht pro Meter | 3,15 kg |
| Bruchlast (verzinkt) | ca. 36,0 kN (3.670 kg) |
| Prüflast | ca. 18,0 kN (1.835 kg) |
| WLL (Faktor 4) | ca. 9,0 kN (918 kg) |

**Anwendungsbereich:**
- Boote: 16–22m (große Segelyachten, Motoryachten)
- Verdrängung: 20–45 Tonnen
- Ankergewicht: 20–35 kg
- Standard für Fahrtenyachten ab 16m und Blauwasser ab 14m

**Windlass-Kompatibilität 12mm:**

| Hersteller | Modelle | Kettennuss | Min. Leistung |
|---|---|---|---|
| Lofrans | Royal, Dorado, Titan | 12mm DIN 766 | 1.500W |
| Lewmar | V6, V700, Pro-Series | 12mm DIN 766 | 1.500W |
| Quick | Prince, Duke DC4 | 12mm DIN 766 | 1.500W |
| Maxwell | Freedom 500, VWC | 12mm DIN 766 | 1.500W |
| Muir | VR3500, VR4000 | 12mm DIN 766 | 2.000W |

**Preis 12mm DIN 766 (Stand 2026, pro Meter):**
- Standard verzinkt: 11,00–15,00 EUR
- Premium verzinkt: 15,00–20,00 EUR
- Edelstahl 316L: 38,00–58,00 EUR
- Aqua-Met beschichtet: 22,00–32,00 EUR

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.5 13mm Kette — Spezifikationen und Anwendung

**13mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 13,0 mm |
| Innenweite | 18,2 mm |
| Innenlänge | 45,5 mm |
| Teilung | 45,5 mm |
| Außenmaß Breite | 44,2 mm |
| Außenmaß Länge | 71,5 mm |
| Gewicht pro Meter | 3,70 kg |
| Bruchlast (verzinkt) | ca. 42,3 kN (4.312 kg) |
| Prüflast | ca. 21,2 kN (2.161 kg) |
| WLL (Faktor 4) | ca. 10,6 kN (1.081 kg) |

**Anwendungsbereich:**
- Boote: 20–26m
- Verdrängung: 30–70 Tonnen
- Ankergewicht: 30–50 kg
- Zwischengröße, besonders im US-Markt (äquivalent zu 1/2")

**Windlass-Kompatibilität 13mm:**

| Hersteller | Modelle | Min. Leistung |
|---|---|---|
| Lofrans | Titan, NX8 | 2.000W |
| Lewmar | V700, V8 | 2.000W |
| Quick | Duke, Count | 2.000W |
| Maxwell | VWC 3500 | 2.500W |
| Muir | VR4000, Thor | 2.500W |

**Preis 13mm DIN 766 (Stand 2026, pro Meter):**
- Standard verzinkt: 13,00–18,00 EUR
- Premium verzinkt: 18,00–24,00 EUR
- Edelstahl 316L: 45,00–68,00 EUR

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.6 14mm Kette — Spezifikationen und Anwendung

**14mm DIN 766 — Kalibrierte Kurzgliedkette**

| Parameter | Wert |
|---|---|
| Nenn-Durchmesser | 14,0 mm |
| Innenweite | 19,6 mm |
| Innenlänge | 49,0 mm |
| Teilung | 49,0 mm |
| Außenmaß Breite | 47,6 mm |
| Außenmaß Länge | 77,0 mm |
| Gewicht pro Meter | 4,30 kg |
| Bruchlast (verzinkt) | ca. 49,0 kN (4.996 kg) |
| Prüflast | ca. 24,5 kN (2.498 kg) |
| WLL (Faktor 4) | ca. 12,25 kN (1.249 kg) |

**Anwendungsbereich:**
- Boote: 24–30m (große Motoryachten, Superyacht-Bereich)
- Verdrängung: 50–100 Tonnen
- Ankergewicht: 40–75 kg
- Oberes Ende des Yachtbereichs, Übergang zu Schiffsketten

**Windlass-Kompatibilität 14mm:**

| Hersteller | Modelle | Min. Leistung |
|---|---|---|
| Lofrans | NX8, Cayman 88 Pro | 2.500W |
| Lewmar | V8, V10 | 2.500W |
| Quick | Count, Marquis | 2.500W |
| Maxwell | VWC 4000 | 3.000W |
| Muir | Thor, Cougar | 3.500W |

**Preis 14mm DIN 766 (Stand 2026, pro Meter):**
- Standard verzinkt: 16,00–22,00 EUR
- Premium verzinkt: 22,00–30,00 EUR
- Edelstahl 316L: 55,00–82,00 EUR

**Confidence: measured** — DIN-Norm und Herstellerkataloge.

### 5.7 Kettennuss (Wildcat/Gypsy) — Dimensionierung

Die Kettennuss ist das Zahnrad in der Ankerwinch, das die Kette greift. Die exakte Abstimmung zwischen Kette und Kettennuss ist entscheidend für die Funktion.

**Begriffe:**
- **Wildcat**: Kettennuss für Kette (mit Taschen für Kettenglieder)
- **Gypsy**: Kann Kette und/oder Leine aufnehmen
- **Drum**: Glatte Trommel für Leine (kein Kettengriff)
- **Combo-Gypsy**: Wildcat + Drum auf einer Welle

**Kompatibilitätsregeln:**

1. Die Kettennuss muss exakt zum Kettentyp und -durchmesser passen
2. DIN 766 Kettennüsse passen NICHT auf G40/BBB Ketten (und umgekehrt)
3. 8mm DIN 766 ≠ 5/16" G40 (ähnlich, aber nicht identisch)
4. Kalibrierte Kette ist Pflicht — unkalibrierte Kette springt
5. Kettennüsse verschleißen — nach 50.000–100.000m Durchlauf prüfen

**Typische Kettennuss-Optionen pro Hersteller:**

| Hersteller | Ketten-Standards | Wechsel-Gypsy verfügbar |
|---|---|---|
| Lofrans | DIN 766 (6–14mm), ISO 4565, G40 BBB | Ja, alle Modelle |
| Lewmar | DIN 766 (6–14mm), G40 BBB (1/4"–1/2") | Ja, Pro-Series |
| Quick | DIN 766 (6–14mm), ISO 4565 | Ja |
| Maxwell | DIN 766 (6–14mm), G40 BBB | Ja |
| Muir | DIN 766, G40 BBB, ISO | Ja |

### 5.8 Chain Counter — Kalibrierung

**Elektronische Kettenzähler** messen die ausgegebene Kettenlänge durch Zählen der Kettenglieder, die durch einen Sensor laufen.

**Kalibrierung:**

```
Kette_pro_Impuls = Teilung_mm / 1000

Beispiel 8mm DIN 766:
Teilung = 28mm
Kette_pro_Impuls = 0,028m
100 Impulse = 2,80m Kette
```

**Kalibrierungsprobleme:**
- Nach Kettenwechsel: IMMER neu kalibrieren
- Verschiedene Kettendurchmesser haben verschiedene Teilungen
- Verschleiß kann Teilung vergrößern → Zähler zeigt zu wenig an
- Lösung: Alle 2 Jahre manuelle Kontrolle (20m Kette messen, mit Anzeige vergleichen)

**Einstellwerte für gängige Kettenzähler:**

| Kettenmaß DIN 766 | Teilung (mm) | Impulse/Meter | Quick Count | Lofrans Counter |
|---|---|---|---|---|
| 6mm | 21,0 | 47,6 | P = 21 | d = 6 |
| 8mm | 28,0 | 35,7 | P = 28 | d = 8 |
| 10mm | 35,0 | 28,6 | P = 35 | d = 10 |
| 12mm | 42,0 | 23,8 | P = 42 | d = 12 |
| 13mm | 45,5 | 22,0 | P = 45 | d = 13 |
| 14mm | 49,0 | 20,4 | P = 49 | d = 14 |

### 5.9 Metrisch vs. Imperial — Umrechnungen

Im internationalen Yachtmarkt treffen metrische (europäische) und imperiale (US-amerikanische) Kettenmaße aufeinander. Die Maße sind NICHT identisch:

**Umrechnungstabelle:**

| Metrisch (mm) | Nächstes US-Äquivalent (inch) | Tatsächliches US-Maß (mm) | Differenz (mm) | Kompatibel? |
|---|---|---|---|---|
| 6,0 | 1/4" | 6,35 | +0,35 | NEIN |
| 7,0 | — | — | — | Kein US-Äquivalent |
| 8,0 | 5/16" | 7,94 | -0,06 | BEDINGT* |
| 10,0 | 3/8" | 9,53 | -0,47 | NEIN |
| 12,0 | 7/16" | 11,11 | -0,89 | NEIN |
| 13,0 | 1/2" | 12,70 | -0,30 | NEIN |
| 14,0 | 9/16" | 14,29 | +0,29 | NEIN |

*8mm DIN 766 und 5/16" G40 sind in der Praxis manchmal austauschbar, aber die Kettennuss-Hersteller empfehlen dies NICHT. Ein Testlauf auf der eigenen Kettennuss ist zwingend.

> **AYDI-Warnung:** Metrische und imperiale Ketten sind GRUNDSÄTZLICH NICHT austauschbar. Selbst kleine Maßdifferenzen führen zu Kettenspringern, Klemmern und gefährlichem Versagen des Windlass-Systems. Beim Kettenwechsel IMMER die exakte Spezifikation der vorhandenen Kettennuss prüfen.

---

## 6. Kettenverbindungen

### 6.1 Ankerwirbel (Anchor Swivel)

Der Ankerwirbel verbindet die Kette mit dem Anker und ermöglicht die Rotation des Ankers um die Kettenachse. Dies verhindert, dass sich die Kette beim Schwoien verdreht.

**Typen:**

**Drehwirbel (Fixed Swivel):**
- Einfachste Bauform
- Schäkel an beiden Enden
- Preis: 15–40 EUR (je nach Größe)
- Nachteil: Kann unter Last blockieren

**Kugelgelagerte Wirbel (Ball Bearing Swivel):**
- Kugellager ermöglicht Rotation auch unter Last
- Premium-Option für dauerhafte Anlagen
- Preis: 40–120 EUR
- Hersteller: Mantus, Kong, Wichard

**Gabelwirbel (Fork Swivel):**
- Gabel greift direkt in Ankeröse
- Kein separater Schäkel am Anker nötig
- Kompakter und stärker
- Hersteller: Ultra, Mantus

### 6.2 Bekannte Wirbel-Hersteller und Produkte

**Mantus Swivel:**
- Material: Edelstahl 316L, geschmiedet
- Bruchlast: 12.000–25.000 lbs (je nach Größe)
- Passend für: 6mm–14mm Kette
- Besonderheit: Integrierter Auslösemechanismus
- Preis: 80–180 EUR
- Verfügbarkeit: gut über Online-Händler

**Kong Anchor Swivel:**
- Material: Edelstahl 316, geschmiedet
- Bruchlast: 6.000–20.000 lbs
- Passend für: 6mm–13mm Kette
- Besonderheit: Italienische Qualität, kompakte Bauform
- Preis: 50–120 EUR

**Ultra Marine Swivel:**
- Material: Edelstahl 316L
- Bruchlast: 8.000–22.000 lbs
- Passend für: 8mm–14mm Kette
- Besonderheit: Spezifisch für Ultra-Anker, sehr flache Bauform
- Preis: 90–200 EUR

**Wichard HR Swivel:**
- Material: Edelstahl 316L, geschmiedet
- Bruchlast: 6.000–18.000 lbs
- Passend für: 6mm–12mm Kette
- Besonderheit: Französische Qualität, breite Verfügbarkeit
- Preis: 60–150 EUR

**Crosby Screw-Pin Shackle (Budget-Option):**
- Material: Verzinkter Stahl
- WLL: nach Schäkelgröße (1–5 Tonnen)
- Nicht als Wirbel — nur als Verbindung
- Preis: 5–20 EUR
- Nachteil: Kein Drehgelenk, Bolzen kann sich lösen

### 6.3 Kettenverbinder (Joining Links / Chain Connectors)

Kettenverbinder dienen dazu, zwei Kettenstücke zu verbinden oder einen Endschäkel an die Kette anzuschließen.

**Typen von Kettenverbindern:**

**Schraubglied (Connecting Link / C-Link):**
- Aufschraubbares Glied, das zwischen Kettenglieder gesetzt wird
- Vorteil: Einfach zu installieren
- Nachteil: Kann sich lösen, oft nicht kalibriert
- WLL: typisch 50–70% der Kettenbruchlast
- Preis: 5–15 EUR
- Sicherung: Kontermutter oder Draht

**Kenter-Glied (Kenter Link / Kenter Shackle):**
- Dreiteiliges Verbindungsglied, gestiftet
- Außenmaße entsprechen dem Kettenglied → windlass-fähig
- WLL: 80–100% der Kettenbruchlast
- Standard für Schiffsketten ab 16mm
- Im Yachtbereich für 10–14mm verfügbar
- Preis: 15–40 EUR
- Installation: Erfordert Spezialwerkzeug (Bolzen einschlagen)

**Omega-Glied (Omega Link):**
- Omega-förmiges Verbindungsglied mit Bolzen
- Passgenau für spezifische Kettenmaße
- WLL: 90–100% der Kettenbruchlast
- Preis: 20–50 EUR
- Hersteller: Maggi, Titan

**Hammerschloss (Hammer Lock / Safety Chain Connector):**
- Geschmiedeter Verbinder mit Bolzen und Splint
- Sehr hohe WLL (oft >100% der Kettenbruchlast)
- Kompakte Bauform
- Standard im industriellen Bereich
- Preis: 25–60 EUR

### 6.4 Ankerschäkel — Dimensionierung

Der Ankerschäkel verbindet den Anker mit der Kette oder dem Wirbel. Die korrekte Dimensionierung ist kritisch.

**Dimensionierungsregel:**
- Schäkel-WLL muss ≥ Ketten-WLL sein
- Schäkelbolzen muss in die Ankeröse passen
- Schäkelbreite muss in das nächste Kettenglied passen

**Empfohlene Schäkelgrößen:**

| Kettenmaß | Schäkelgröße | WLL (t) | Bolzen-Ø (mm) |
|---|---|---|---|
| 6mm | 6mm (1/4") | 0,5 | 7 |
| 8mm | 8mm (5/16") | 0,75 | 9,5 |
| 8mm | 10mm (3/8") | 1,0 | 11 |
| 10mm | 10mm (3/8") | 1,0 | 11 |
| 10mm | 12mm (1/2") | 2,0 | 13 |
| 12mm | 12mm (1/2") | 2,0 | 13 |
| 12mm | 14mm (9/16") | 2,5 | 16 |
| 13mm | 14mm (9/16") | 2,5 | 16 |
| 14mm | 16mm (5/8") | 3,25 | 19 |

**Material-Empfehlung:**
- Verzinkter Stahl: Standard, muss zum Kettenmaterial passen
- Edelstahl 316L: NUR bei Edelstahlkette (sonst Kontaktkorrosion!)
- NIEMALS verschiedene Metalle mischen (Edelstahl + Verzinkung = galvanische Korrosion)

### 6.5 Kalibrierte vs. Unkalibrierte Verbindungen

**Problem:** Jede Verbindung in der Kette (Wirbel, Schäkel, Konnekter) muss durch die Kettennuss laufen. Unkalibrierte Verbindungen können:

1. In der Kettennuss klemmen → Windlass stoppt unter Last
2. Über die Kettennuss springen → Unkontrolliertes Abspulen
3. Die Kettennuss beschädigen → Teure Reparatur
4. Beim Einholen am Bug-Roller hängen bleiben

**Lösung:**
- Verbindungen vor dem Einbau auf der Kettennuss testen
- Kenter-Glieder sind dimensionsgleich mit Kettengliedern → beste Windlass-Kompatibilität
- Wirbel und Schäkel müssen VOR der Bugrolle sitzen (nicht durch Windlass laufen)
- Ideale Anordnung: Anker — Schäkel — Wirbel — Schäkel — Kette — (durch Windlass) — Kettenkasten

### 6.6 Sicherung von Verbindungen

Jede Schraubverbindung in der Ankerkette muss gegen unbeabsichtigtes Lösen gesichert werden:

**Sicherungsmethoden:**

| Methode | Geeignet für | Haltbarkeit | Lösbarkeit |
|---|---|---|---|
| Sicherungsdraht (Seizing Wire) | Schäkelbolzen | Sehr gut | Gut (Draht schneiden) |
| Kabelbinder (Cable Tie) | Schraubglieder | Mittel | Sehr gut |
| Kontermutter | Schraubglieder | Gut | Gut |
| Loctite 243 (mittelfest) | Bolzen | Gut | Mittel (Wärme) |
| Splint | Kenter-Glieder | Sehr gut | Mittel |
| Schweißen | Permanent | Dauerhaft | Nicht lösbar |

> **AYDI-Empfehlung:** Sicherungsdraht aus Edelstahl (1,0–1,2mm) ist die bewährte Methode für Ankerschäkel. Der Draht wird durch das Bolzenauge und das Schäkelgehäuse geführt und verdreht. Alle 1–2 Jahre erneuern.

### 6.7 Kettenendverbindung (Bitter End)

Das "bittere Ende" der Kette muss im Kettenkasten befestigt sein — aber lösbar:

**Warum lösbar?**
In einer Notsituation (Anker nicht loszubekommen, schleppender Anker bei Gefahr, Kette um Koralle) muss die Kette schnell gekappt werden können. Eine verschweißte oder fest geschraubte Verbindung kann in einer Notsituation das Boot gefährden.

**Empfohlene Bitter-End-Befestigung:**

1. **Nylon-Leinenstück (2–3m):** Kette → Schäkel → Nylon-Auge → Stahlring im Kettenkasten
   - Vorteil: Kann mit Messer gekappt werden
   - Nachteil: Nylon kann durch Reibung/Quetschung brechen

2. **Kettenschäkel mit Schnellverschluss:** Kette → Hammerschloss mit Splint → Augbolzen
   - Vorteil: Schnell lösbar durch Splint ziehen
   - Nachteil: Erfordert Zugang zum Kettenkasten

3. **Dyneema-Schlinge:** Kette → Dyneema-Stropp → Ringbolzen
   - Vorteil: Sehr stark, kappbar
   - Nachteil: UV-empfindlich im Kettenkasten (meist unkritisch)

> **AYDI-Warnung:** Die Kette darf NIEMALS fest mit dem Boot verschweißt oder verbolzt sein. Bei jedem Ankermanöver muss der Skipper in der Lage sein, die Kette innerhalb von Sekunden zu lösen.

---

## 7. Hersteller und Bezugsquellen

### 7.1 ACCO (USA)

**Acco Peerless / Campbell Chain (USA)**
- Größter US-Hersteller von Ketten
- Produkte: G30, G40/BBB, G43, G70
- Qualität: Gut, konsistent, US-Standards
- Kalibrierung: G40 BBB ist windlass-kalibriert
- Verzinkung: ASTM A153
- Verfügbarkeit: Hauptsächlich US-Markt, über West Marine, Defender
- Preis: Mittelfeld für US-Markt
- Zertifizierung: NACM/ASTM geprüft

### 7.2 Titan (Neuseeland)

**Titan Marine Products (Neuseeland)**
- Premium-Hersteller für marine Anker und Kette
- Produkte: DIN 766, ISO 4565, G40 BBB
- Qualität: Sehr gut, strenge Qualitätskontrolle
- Besonderheit: Überprüft jede Charge, eigene Tests
- Verzinkung: Überdurchschnittlich (80–100 µm)
- Verfügbarkeit: Weltweit über Fachhändler
- Preis: Premium (ca. 15–25% über Standard)
- Bekannt für: Titan-Anker (ehem. Rocna)

### 7.3 Maggi (Italien)

**Maggi S.p.A. (Italien)**
- Traditioneller italienischer Kettenhersteller
- Produkte: DIN 766, ISO, beschichtete Ketten (Aqua-Met)
- Qualität: Gut bis sehr gut
- Besonderheit: Polyester-beschichtete Ketten (Aqua-Met-Verfahren)
- Verzinkung: EN ISO 1461, gute Schichtdicke
- Verfügbarkeit: Europa-weit, gute Vertriebspartner
- Preis: Mittel bis Premium
- OEM-Lieferant für mehrere Windlass-Hersteller

### 7.4 Chinesische Ketten — Qualitätsbewertung

**Chinesische Kettenhersteller (diverse)**

China ist der weltweit größte Produzent von Ketten aller Art. Die Qualität variiert extrem:

**A-Qualität (Premium, für Marine-Marken):**
- Hergestellt nach DIN 766, ISO 4565 oder G40
- Zertifiziert und geprüft
- Verzinkung nach EN ISO 1461
- Preis: nur minimal günstiger als europäische Ketten
- Erkennbar an: Normbezeichnung, Prüfzertifikat, Markenname

**B-Qualität (Mittelsegment):**
- Maße entsprechen DIN/ISO, aber größere Toleranzen
- Verzinkung: oft dünner als Norm-Minimum
- Kalibrierung: kann abweichen → Windlass-Test nötig
- Preis: 30–50% günstiger als Markenware
- Risiko: Vereinzelt mangelhafte Glieder

**C-Qualität (Billig, nicht empfohlen):**
- Keine nachweisbare Normkonformität
- Verzinkung: oft <30 µm, ungleichmäßig
- Maße: Abweichungen bis zu 1–2mm → Windlass-inkompatibel
- Bruchlast: deutlich unter Nennwert
- Preis: 50–70% günstiger als Markenware
- NICHT EMPFOHLEN für Ankerzwecke

**Erkennungsmerkmale billiger China-Kette:**
1. Kein Prüfzertifikat oder nur Fotokopie ohne Chargennummer
2. Gliedmaße variieren sichtbar (Lehre anlegen!)
3. Verzinkung ist ungleichmäßig, Tropfnasen, blanke Stellen
4. Gewicht pro Meter weicht >5% vom Nennwert ab
5. Keine Normbezeichnung eingeprägt

> **AYDI-Warnung:** Bei Ankerketten ist die Preisdifferenz zwischen Qualitäts- und Billigkette gering im Vergleich zum Risiko. 100m 10mm Kette kosten als Markenware ca. 1.000 EUR, als Billig-China-Kette ca. 400 EUR. Die Differenz von 600 EUR steht in keinem Verhältnis zu den Kosten einer Strandung oder eines Kettenbruchs.

### 7.5 Europäische Bezugsquellen

**SVB (Deutschland — svb-marine.de):**
- Größter deutscher Online-Yachtausrüster
- Sortiment: Maggi, Titan, Eigenmarke
- DIN 766: 6–14mm, verzinkt und Edelstahl
- Preis: Wettbewerbsfähig, regelmäßige Angebote
- Versand: Innerhalb Deutschlands und EU
- Service: Gute Beratung, Rückgabe möglich
- Meterware: Ja, auf Wunschlänge

**Toplicht (Deutschland — toplicht.de):**
- Hamburger Traditions-Yachtausrüster
- Sortiment: Maggi, Titan, ACCO
- Besonderheit: Sehr gute Fachberatung
- Preis: Mittel bis gehoben
- Meterware: Ja
- Zusatzservice: Kettennuss-Beratung

**Compass24 (Deutschland — compass24.de):**
- Großer Online-Yachtausrüster
- Sortiment: Breit, mehrere Marken
- DIN 766: 6–14mm
- Preis: Wettbewerbsfähig
- Versand: Schnell innerhalb DE/EU
- Meterware: Ja

**Busse Yachtshop (Deutschland — busse-yachtshop.de):**
- Qualitätsorientierter Fachhandel
- Sortiment: Maggi, Premium-Ketten
- Besonderheit: Gute technische Beratung
- Preis: Mittel
- Meterware: Ja

**AWN (Deutschland — awn.de):**
- Großer Multichannel-Yachtausrüster
- Sortiment: Breit, Eigenmarke und Marken
- Preis: Wettbewerbsfähig, oft Aktionsangebote
- Filialen: Mehrere Standorte
- Meterware: Ja

**Jimmy Green Marine (UK — jimmygreenmarinne.co.uk):**
- Spezialist für Anker und Kette
- Sortiment: Hochwertige Ketten, eigene Qualitätskontrolle
- Besonderheit: Experte für Blauwasser-Ausrüstung
- Preis: Premium
- Versand: UK und EU
- Sehr gute technische Dokumentation

### 7.6 Preisübersicht — DIN 766, feuerverzinkt (pro Meter, 2026)

| Kettenmaß | Budget | Standard | Premium |
|---|---|---|---|
| 6mm | 2,50–3,50 EUR | 3,50–5,00 EUR | 5,00–7,00 EUR |
| 8mm | 4,00–5,50 EUR | 5,50–8,00 EUR | 8,00–11,00 EUR |
| 10mm | 6,00–8,00 EUR | 8,00–12,00 EUR | 12,00–16,00 EUR |
| 12mm | 8,00–11,00 EUR | 11,00–16,00 EUR | 16,00–22,00 EUR |
| 13mm | 10,00–14,00 EUR | 14,00–20,00 EUR | 20,00–28,00 EUR |
| 14mm | 12,00–16,00 EUR | 16,00–22,00 EUR | 22,00–32,00 EUR |

**Preisübersicht — DIN 766, Edelstahl 316L (pro Meter, 2026):**

| Kettenmaß | Standard | Premium |
|---|---|---|
| 6mm | 10,00–15,00 EUR | 15,00–22,00 EUR |
| 8mm | 16,00–24,00 EUR | 24,00–35,00 EUR |
| 10mm | 24,00–36,00 EUR | 36,00–50,00 EUR |
| 12mm | 32,00–48,00 EUR | 48,00–70,00 EUR |

**Confidence: estimated** — Preise basieren auf Marktrecherche 2025/2026, unterliegen Rohstoffschwankungen.

### 7.7 Großgebinde und Trommeln

Für Langfahrtsegler oder Yachten mit hohem Kettenbedarf lohnt sich der Kauf in Großgebinden:

**Trommeln (50m, 75m, 100m):**
- 50m Trommel: ca. 5–10% Rabatt gegenüber Meterware
- 100m Trommel: ca. 10–20% Rabatt gegenüber Meterware
- Vorteil: Durchgehende Kette ohne Verbindungsglieder
- Transport: Schwer! 100m 10mm Kette = 220 kg + Trommel

**Fässer (Drams):**
- Einige Hersteller liefern Kette in Fässern (50–200m)
- Fass schützt Verzinkung während Transport und Lagerung
- Entnahme: Kette abrollen, nicht aus dem Fass "angeln" (Verheddern!)

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Korrosion und Lochfraß (Pitting)

**Beschreibung:**
Punktueller oder flächiger Abtrag der Verzinkung mit anschließender Korrosion des Grundmaterials. Lochfraß zeigt sich als kleine, tiefe Korrosionsgruben im Stahl.

**Erscheinungsbild:**
- Orangebraune Rostflecken auf sonst silberner Verzinkung
- Kleine, tiefe Löcher (Pits) im Metallquerschnitt
- Aufgequollene, blätternde Korrosionsprodukte
- Rauer, unebener Gliedoberfläche

**Ursachen:**
- Natürliche Alterung der Verzinkung
- Beschleunigt durch: Seewasser, hohe Temperaturen, Verschmutzung
- Kontaktkorrosion (andere Metalle im Kettenkasten)
- Mangelhafte Verzinkung (zu dünn, Poren)

**Risikobewertung:**

| Ausmaß | Risiko | Maßnahme |
|---|---|---|
| <10% Oberfläche, kein Pitting | Gering | Beobachten, Re-Galv. planen |
| 10–30% Oberfläche, leichtes Pitting | Mittel | Re-Galvanisierung in 1–2 Saisons |
| 30–50% Oberfläche, Pitting <0,5mm tief | Erhöht | Re-Galvanisierung diese Saison |
| >50% Oberfläche, Pitting >0,5mm | Hoch | Austausch empfohlen |
| Pitting >1mm Tiefe bei 8mm Kette | Kritisch | Sofortiger Austausch |

**Prüfmethode:**
1. Kette reinigen (Hochdruckreiniger)
2. Trocknen lassen
3. Visuelle Inspektion jedes 5. Gliedes
4. Verdächtige Glieder mit Schieblehre messen
5. Querschnittsverlust >10% = Austausch

**Confidence: documented** — Korrosionswissenschaft und Praxiserfahrung.

### 8.2 Fehlerbild F02: Gelängte Glieder

**Beschreibung:**
Durch Überlastung oder Dauerbeanspruchung können sich Kettenglieder plastisch verformen und längen. Gelängte Glieder passen nicht mehr korrekt in die Kettennuss.

**Erscheinungsbild:**
- Glied ist sichtbar "ovaler" als Nachbarglieder
- Messbare Längenzunahme >5% gegenüber Nennmaß
- Glied "wackelt" in der Kettennuss
- Kette springt bei Einholen/Ausgeben

**Ursachen:**
- Einmalige Überlastung (Sturmankern, festsitzender Anker)
- Dauerbelastung nahe der Streckgrenze
- Materialermüdung nach vielen Lastzyklen
- Minderwertige Stahlqualität

**Prüfmethode:**
```
Längung (%) = ((L_gemessen - L_nenn) / L_nenn) × 100

Nennmaße DIN 766:
  8mm Kette: Innenlänge = 28,0mm
  10mm Kette: Innenlänge = 35,0mm
  12mm Kette: Innenlänge = 42,0mm

Toleranz: ±1%
Grenzwert: >5% = Austausch
Warnung: >3% = intensive Beobachtung
```

**Maßnahme:**
- Einzelne gelängte Glieder: Kettenstück austauschen (Kenter-Glied)
- Mehrere gelängte Glieder: Gesamte Kette austauschen
- Windlass prüfen: Gelängte Kette kann Kettennuss beschädigt haben

### 8.3 Fehlerbild F03: Abgenutzte Verzinkung

**Beschreibung:**
Mechanischer Abrieb der Verzinkung durch Kontakt mit der Kettennuss, der Bugrolle und dem Ankergrund.

**Erscheinungsbild:**
- Silbern-matte Zinkschicht wird dunkler/grauer
- Blanke Stahlstellen an Kontaktpunkten
- Typisch: Innenseite der Glieder (Kettennuss-Kontakt) zuerst blank
- Bugrolle-Kontaktbereich stark abgerieben

**Ursachen:**
- Normaler Verschleiß (unvermeidlich)
- Beschleunigt durch: Sand/Schlick am Grund, häufiges Ankern
- Kettennuss aus gehärtetem Stahl → reibt Zink ab
- Bugrolle zu eng oder falsch ausgerichtet

**Verschleißrate:**
| Nutzung | Geschätzte Lebensdauer der Verzinkung |
|---|---|
| Wochenendsegler (20–30 Ankermanöver/Jahr) | 8–15 Jahre |
| Dauerliegeplatz + gelegentliches Ankern | 10–20 Jahre |
| Langfahrt/Blauwasser (100+ Ankermanöver/Jahr) | 3–7 Jahre |
| Charterboot (200+ Ankermanöver/Jahr) | 2–4 Jahre |

**Maßnahme:**
- Bei >50% blanker Oberfläche: Re-Galvanisierung
- Bugrolle und Kettennuss auf scharfe Kanten prüfen
- Kettenkontaktflächen polieren (reduziert Abrieb)

### 8.4 Fehlerbild F04: Festsitzende/Verklemmte Glieder

**Beschreibung:**
Einzelne Kettenglieder sind miteinander verklemmt und lassen sich nicht mehr gegeneinander bewegen.

**Erscheinungsbild:**
- Kette bildet steife Abschnitte statt flexibler Kurve
- Glieder rasten nicht mehr um 90° gegeneinander
- Kette "knickt" an bestimmten Stellen
- Windlass kann steifen Abschnitt nicht einziehen

**Ursachen:**
- Salzablagerungen in den Gliedkontakten
- Korrosionsprodukte (Rost) verkleben Glieder
- Eingedrungener Sand/Schlick
- Verformung durch Überlast
- Mangelhafter Stahl (Werkstoffversagen)

**Maßnahme:**
1. Kette 24h in Frischwasser einweichen
2. Vorsichtig mit Hammer auf verklemmtes Glied klopfen
3. Bei Korrosion: Rostlöser (WD-40, Owatrol) aufsprühen, einwirken lassen
4. Wenn Glied sich nicht löst: visuell auf Verformung prüfen
5. Verformtes Glied = Kettenstück austauschen

### 8.5 Fehlerbild F05: Windlass-Kettensprung

**Beschreibung:**
Die Kette springt aus der Kettennuss oder wird nicht korrekt gegriffen. Die Windlass kann die Kette nicht kontrolliert einholen oder ablassen.

**Erscheinungsbild:**
- Kette rutscht durch ohne Zugkraft
- Kette springt seitlich aus der Kettennuss
- Klackernde Geräusche beim Einfahren
- Windlass blockiert periodisch
- Kette "überspringt" ein oder mehrere Taschen

**Ursachen:**
1. **Falsche Kette für Kettennuss** (häufigste Ursache!)
2. Verschlissene Kettennuss
3. Gelängte Kettenglieder
4. Unkalibrierte Kette
5. Beschichtete Kette in Standard-Kettennuss (Beschichtung zu dick)
6. Verdrehte Kette
7. Fremdkörper in der Kettennuss

**Diagnose:**

```
Kettensprung-Diagnose:

1. Kette korrekt? → DIN 766 / G40 prüfen, Maße mit Lehre prüfen
2. Kettennuss verschlissen? → Zahnprofil prüfen (Verschleißmarker)
3. Kette gelängt? → Gliedmaße messen (>5% = Problem)
4. Verdrehung? → Kette begradigen, im Kettenkasten neu aufschießen
5. Fremdkörper? → Kettennuss reinigen, Grate entfernen
```

**Maßnahme:**
- Falsche Kette: Richtige Kette kaufen ODER richtige Kettennuss bestellen
- Verschlissene Kettennuss: Austausch (Verschleißteil, ca. 80–200 EUR)
- Verdrehung: Kette komplett ausgeben, auf Steg auffieren, begradigt einholen

### 8.6 Fehlerbild F06: Verdrehter Kettenhaufen im Kettenkasten

**Beschreibung:**
Die Kette bildet im Kettenkasten einen verdrehten, verfilzten Haufen, der nicht mehr frei ablaufen kann.

**Erscheinungsbild:**
- Kette "verstopft" beim Ausgeben
- Kette kommt verdreht aus dem Kettenkasten
- Windlass zieht, aber Kette folgt nicht
- Klemmgeräusche aus dem Kettenkasten

**Ursachen:**
- Kettenkasten zu klein für die Kettenlänge
- Keine Kettenführung (Kette fällt ungeordnet)
- Kette wird beim Einholen verdreht (Kettennuss-Problem)
- Kette nie "durchgesetzt" (nie komplett ausgegeben und geordnet eingeholt)

**Prävention:**
1. Kettenkasten mindestens 3× Kettenvolumen
2. Kette einmal pro Saison komplett ausgeben und geordnet einholen
3. Kettenführungsrohr vom Deck in den Kasten (gerade, ohne Knicke)
4. Abgerundete Kanten im Kettenkasten
5. Trennwand in Kettenkasten (Kette fällt links, rechts abwechselnd)

**Kettenkasten-Volumen (Faustregel):**

| Kettenlänge × Kettenmaß | Kettenvolumen (Liter) | Min. Kastenvolumen (Liter) |
|---|---|---|
| 50m × 8mm | ca. 20 | 60 |
| 60m × 8mm | ca. 24 | 72 |
| 80m × 10mm | ca. 50 | 150 |
| 100m × 10mm | ca. 62 | 186 |
| 100m × 12mm | ca. 90 | 270 |

### 8.7 Fehlerbild F07: Ketten-Konnektorversagen

**Beschreibung:**
Ein Schraubglied, Schäkel oder Kenter-Glied versagt — die Kette bricht an der Verbindungsstelle.

**Erscheinungsbild:**
- Kette liegt auf Grund, Anker ist verloren
- Verbindungsglied geöffnet oder gebrochen
- Bolzen herausgefallen (nicht gesichert)
- Verschraubung gelöst (Vibrationen)

**Ursachen:**
1. Fehlende Sicherung (kein Draht, kein Splint)
2. Unterdimensionierter Verbinder
3. Korrosion am Verbinder (oft schneller als an der Kette)
4. Ungeeigneter Verbinder (falsche Güte, falsches Material)
5. Fehlerhafter Einbau (Bolzen nicht vollständig eingesetzt)
6. Galvanische Korrosion (verschiedene Metalle)

**Prävention:**
- Sicherungsdraht an jedem Schäkelbolzen
- Verbinder alle 6 Monate inspizieren
- WLL des Verbinders ≥ WLL der Kette
- Gleiches Material wie Kette (kein Edelstahlschäkel an verzinkter Kette)
- Kenter-Glieder bevorzugen (dimensionsgleich, hohe Festigkeit)

### 8.8 Fehlerbild F08: Antifouling-Kontamination

**Beschreibung:**
Antifouling-Farbe vom Rumpf kontaminiert die Ankerkette. Die Kette wird mit giftigem Antifouling bedeckt.

**Erscheinungsbild:**
- Kette hat Farbrückstände (blau, rot, schwarz)
- Farbabrieb an Händen und Ausrüstung
- Kettenkasten ist mit Antifouling verschmiert
- Deck und Bugrolle verfärbt

**Ursachen:**
- Antifouling reicht zu nah an die Ankernase/Bugrolle
- Kette liegt beim Ankern am Rumpf an (z.B. bei Strömungswechsel)
- Kette wird über frisch antifoulingiertes Unterwasserschiff gezogen

**Maßnahme:**
- Antifouling-freien Streifen um Ankerrolle und Bug lassen (20–30cm)
- Kette mit Hochdruckreiniger säubern
- Bei hartlackigem Antifouling: mechanisch entfernen schwierig
- Kontaminiertes Spülwasser umweltgerecht entsorgen

### 8.9 Fehlerbild F09: Elektrolyse-Schäden

**Beschreibung:**
Galvanische Korrosion an der Ankerkette durch Kontakt mit unedleren oder edleren Metallen im Seewasser.

**Erscheinungsbild:**
- Rapider Zinkverlust an spezifischen Bereichen
- Kraterartige Korrosion am Grundmaterial
- Verfärbung (weiße Zinkoxide, braune Eisenoxide)
- Typisch: An Verbindungsstellen zu anderen Metallen

**Ursachen:**
1. Edelstahl-Wirbel an verzinkter Kette (galvanisches Element)
2. Aluminium-Bugrolle mit Stahlkette
3. Vagabundierende Ströme im Hafen (Landstrom, Nachbarboote)
4. Zinkanode der Kette fehlt (selten nötig, aber in Häfen möglich)
5. Bronze-Kettennuss mit Stahlkette

**Spannungsreihe maritimer Metalle (Anode → Kathode):**
```
Zink (-1,05V) → Aluminium (-0,76V) → Stahl (-0,60V)
→ Blei (-0,55V) → Bronze (-0,30V) → Kupfer (-0,22V)
→ Edelstahl passiv (-0,08V) → Titan (+0,06V)
```

**Maßnahme:**
- Isolierscheiben zwischen verschiedenen Metallen
- Bei Edelstahl-Wirbel: Opferanode in der Nähe montieren
- Landstrom-Galvanik: FI-Schalter und Trenntrafo verwenden
- Kettenkasten: Keine anderen Metalle in Kontakt mit der Kette lagern

### 8.10 Fehlerbild F10: Verlorene Kettenmarkierung

**Beschreibung:**
Die Farbmarkierung oder Marker an der Kette sind nicht mehr erkennbar. Die ausgegebene Kettenlänge kann nicht mehr bestimmt werden.

**Erscheinungsbild:**
- Farbmarkierungen abgerieben oder ausgeblichen
- Kabelbinder abgerissen
- Kunststoff-Marker fehlen
- Kettenzähler nicht kalibriert oder defekt

**Ursachen:**
- Mechanischer Abrieb durch Kettennuss und Bugrolle
- UV-Ausbleichung der Farbe
- Salzwasser wäscht Farbe ab
- Kabelbinder brechen durch UV und Kälte
- Nie erneuert

**Maßnahme:**
1. Kette komplett ausgeben (auf Steg oder sauberen Boden)
2. Kette messen: Maßband anlegen, alle 5m oder 10m markieren
3. Neues Markierungssystem aufbringen:
   - Sprühlack auf trockener, entfetteter Kette
   - 2-Komponentenlack für Haltbarkeit
   - Zusätzlich Kabelbinder als Backup
4. Kettenzähler neu kalibrieren
5. Markierungssystem jährlich erneuern

### 8.11 Fehlerbild F11: Kette-Leine-Verbindungsversagen (Mixed Rode)

**Beschreibung:**
Die Verbindung zwischen Kette und Nylon-Leine bei einer Mixed Rode versagt.

**Erscheinungsbild:**
- Leine rutscht aus dem Auge oder Schäkel
- Spleiß öffnet sich
- Schäkel an der Verbindung bricht
- Kette und Anker gehen verloren, Leine bleibt am Boot

**Ursachen:**
1. Unzureichender Spleiß (zu wenig Tucks)
2. Schäkel zu klein oder zu scharf (schneidet Leine)
3. Kein Kausch im Leinenauge (Schäkel reibt auf Fasern)
4. UV-Degradierung der Nylon-Leine am Übergang
5. Scheuern der Leine am letzten Kettenglied

**Prävention:**
- Min. 5 Tucks beim Augspleiß in 3-schäftiger Leine
- Edelstahl-Kausch im Leinenauge
- Schäkel mit abgerundeten Kanten oder dedizierten Ketten-Leine-Konnekter
- Schrumpfschlauch oder Klebeband über den Übergang
- Leine regelmäßig auf Scheuerstellen prüfen

### 8.12 Fehlerbild F12: Kettenkasten-Drainage blockiert

**Beschreibung:**
Der Ablauf des Kettenkastens ist verstopft. Wasser steht dauerhaft im Kasten und beschleunigt die Korrosion.

**Erscheinungsbild:**
- Stehendes Wasser im Kettenkasten (erkennbar am Geruch: faulig, metallisch)
- Kettenkasten riecht nach Schwefelwasserstoff
- Kette zeigt beschleunigte Korrosion
- Bug sitzt tiefer als normal (Gewicht durch Wasser)
- Edelstahlkette: Spaltkorrosion setzt ein

**Ursachen:**
- Ablaufloch mit Schmutz, Sand, Muscheln verstopft
- Ablaufschlauch geknickt
- Bilgepumpe im Vorschiff defekt
- Kein Ablauf vorhanden (Konstruktionsfehler!)
- Rost-/Kalkablagerungen im Ablaufrohr

**Maßnahme:**
1. Kette komplett entnehmen
2. Kettenkasten reinigen (Hochdruckreiniger)
3. Ablaufloch/Schlauch freimachen
4. Ablauf mit Sieb versehen (verhindert Verstopfung)
5. Regelmäßig prüfen (monatlich in der Saison)
6. Wenn kein Ablauf: Nachrüsten (Seeventil mit Rückschlagklappe)

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum T01: Kette klemmt in Windlass

```
PROBLEM: Kette klemmt in der Windlass
│
├─ Klemmt beim EINHOLEN?
│  ├─ Klemmt regelmäßig (jedes Glied)?
│  │  ├─ Kette korrekt für Kettennuss? → PRÜFEN (Maße mit Lehre)
│  │  ├─ Kettennuss verschlissen? → KETTENNUSS TAUSCHEN
│  │  └─ Kette gelängt? → KETTE MESSEN (>5% = tauschen)
│  │
│  ├─ Klemmt unregelmäßig (bestimmte Stellen)?
│  │  ├─ Einzelne Glieder verformt? → GLIEDER IDENTIFIZIEREN & TAUSCHEN
│  │  ├─ Verdrehte Kette? → KETTE BEGRADIGEN
│  │  ├─ Verbindungsglied? → VERBINDER PRÜFEN (Außenmaße!)
│  │  └─ Fremdkörper (Muscheln, Steine)? → REINIGEN
│  │
│  └─ Klemmt NUR beim Übergang Wasser→Deck?
│     ├─ Bugrolle zu eng? → BUGROLLE ANPASSEN
│     ├─ Bugrolle falsch ausgerichtet? → AUSRICHTEN
│     └─ Kette verdreht sich im Bugbeschlag? → FÜHRUNGSBLECHE
│
├─ Klemmt beim AUSGEBEN?
│  ├─ Kettenkasten verstopft? → KETTE DURCHSETZEN
│  ├─ Kette verheddered? → ENTWIRREN (im Hafen!)
│  ├─ Kettenlänge verklemmt Ablauf? → KETTENKASTEN UMBAUEN
│  └─ Kette zu steif (Korrosion)? → REINIGEN, ggf. TAUSCHEN
│
└─ Klemmt in BEIDEN Richtungen?
   ├─ Komplett falsche Kette → PRÜFEN UND TAUSCHEN
   ├─ Kettennuss defekt → MECHANIKER
   └─ Elektrisches Problem (Windlass dreht nicht richtig) → ELEKTRIKER
```

### 9.2 Entscheidungsbaum T02: Ankerkette zu kurz

```
PROBLEM: Ankerkette reicht nicht für gewünschte Ankertiefe
│
├─ Tiefe bekannt?
│  ├─ JA → Scope berechnen:
│  │  Benötigte Kette = (Wassertiefe + Bughöhe) × Scope
│  │  ├─ Scope 5:1 reicht → OK, weiter ankern
│  │  ├─ Scope 5:1 reicht NICHT →
│  │  │  ├─ Flachere Stelle suchen
│  │  │  ├─ Scope auf 3:1 reduzieren (NUR bei ruhigen Bedingungen!)
│  │  │  └─ Ankerwache verstärken
│  │  └─ Kette PLUS Leine verfügbar?
│  │     ├─ JA → Mixed Rode: Leine an Kette anschlagen
│  │     └─ NEIN → Flachere Stelle ist Pflicht
│  │
│  └─ NEIN → Tiefe messen!
│     ├─ Echolot ablesen
│     ├─ Gezeitenkalender: max. Tiefe berechnen
│     └─ Scope berechnen (s.o.)
│
├─ Langfristige Lösung:
│  ├─ Mehr Kette kaufen → Windlass und Kettenkasten prüfen!
│  │  ├─ Windlass-Kapazität ausreichend? (Gewicht!)
│  │  ├─ Kettenkasten groß genug?
│  │  └─ Bugtrimm noch akzeptabel?
│  ├─ Mixed Rode einrichten →
│  │  ├─ 15–20m Kette + 40–60m Nylon
│  │  ├─ Gewicht sparen
│  │  └─ Scope erhöhen (+1 gegenüber Ganzkette)
│  └─ Zweitanker mit separater Rode →
│     ├─ Entlastet Hauptanker
│     └─ Ermöglicht Bahamaanker-Konfiguration
```

### 9.3 Entscheidungsbaum T03: Kettenmarkierungssystem

```
PROBLEM: Welches Markierungssystem verwenden?
│
├─ Boot hat Kettenzähler?
│  ├─ JA → Kettenzähler ist primäres System
│  │  ├─ ABER: Backup-Markierung trotzdem anbringen!
│  │  └─ Sprühlack alle 10m als visuelles Backup
│  └─ NEIN → Visuelles System ist primär
│
├─ Wie oft wird geankert?
│  ├─ Wochenende (10–20×/Jahr)
│  │  ├─ Sprühlack: reicht 2–3 Saisons
│  │  └─ Kabelbinder als Backup
│  ├─ Regelmäßig (50–100×/Jahr)
│  │  ├─ 2K-Lack: haltbarer, jährlich nachbessern
│  │  ├─ Kunststoff-Marker: dauerhaft
│  │  └─ Kabelbinder erneuern jede Saison
│  └─ Intensiv / Langfahrt (100+×/Jahr)
│     ├─ 2K-Lack als Basis
│     ├─ Kunststoff-Marker als Haupt-System
│     ├─ Kabelbinder als Backup
│     └─ Kettenzähler nachrüsten!
│
├─ Farbsystem:
│  ├─ Standard: Rot-Gelb-Blau (s. Abschnitt 3.6)
│  ├─ US-Standard: Rot-Weiß-Blau
│  └─ Eigenes System: DOKUMENTIEREN und im Logbuch notieren!
│
└─ Markierungsintervall:
   ├─ Alle 5m: für Boote <10m mit kurzer Kette
   ├─ Alle 10m: Standard
   └─ Alle 5m bis 30m, dann alle 10m: Kompromiss
```

### 9.4 Entscheidungsbaum T04: Verzinkungszustand beurteilen

```
PROBLEM: Ist die Verzinkung noch ausreichend?
│
├─ Schritt 1: Visuelle Inspektion
│  ├─ Kette komplett ausgeben (Steg oder sauberer Boden)
│  ├─ Hochdruckreiniger: Kette reinigen
│  └─ Trocknen lassen (min. 2h)
│
├─ Schritt 2: Beurteilung
│  ├─ >90% silber/grau-matt → SEHR GUT (5+ Jahre)
│  ├─ 70–90% silber, vereinzelt braune Flecken → GUT (3–5 Jahre)
│  ├─ 50–70% silber, mehrfach braune Bereiche → MÄSSIG (1–2 Jahre)
│  ├─ 30–50% silber, große Rostflächen → SCHLECHT (Re-Galv. diese Saison)
│  └─ <30% silber, durchgehend Rost → KRITISCH (Austausch oder sofort Re-Galv.)
│
├─ Schritt 3: Messung (optional, für AYDI-Analyse)
│  ├─ Schichtdickenmessgerät (Elcometer, DeFelsko)
│  ├─ 5 Messpunkte pro 10m Kette
│  ├─ >50 µm = OK
│  ├─ 20–50 µm = Verschleiß fortgeschritten
│  └─ <20 µm = Schutz unzureichend
│
├─ Schritt 4: Entscheidung
│  ├─ Re-Galvanisierung (wenn Kette mechanisch OK)
│  │  ├─ Gliedmaße prüfen (<5% Längung)
│  │  ├─ Kein Pitting >0,5mm
│  │  └─ Kosten: ca. 3–6 EUR/m (je nach Dicke)
│  ├─ Austausch (wenn mechanisch nicht mehr OK)
│  │  ├─ Längung >5%
│  │  ├─ Pitting >0,5mm
│  │  └─ Risse oder Brüche
│  └─ Notmaßnahme (wenn Re-Galv. nicht sofort möglich)
│     ├─ Kaltverzinkungsspray (ZRC, Galvit) auftragen
│     ├─ Kette leicht einölen (Lanolin)
│     └─ Engmaschig kontrollieren (monatlich)
```

### 9.5 Entscheidungsbaum T05: Mixed-Rode-Spleiß

```
PROBLEM: Kette-Leine-Verbindung herstellen
│
├─ Leinen-Typ?
│  ├─ 3-schäftiges Nylon (Standard für Ankerleine)
│  │  ├─ Augspleiß mit min. 5 Tucks
│  │  ├─ Kausch einlegen (Edelstahl, passend für Schäkel)
│  │  ├─ Spleiß ausrollen und belasten (50 kg für 10 min)
│  │  └─ Schrumpfschlauch über Spleißbereich
│  │
│  ├─ Geflochtenes Nylon
│  │  ├─ Augspleiß nach Herstelleranleitung
│  │  ├─ Kausch einlegen
│  │  └─ Bruchlast nach Spleiß: ca. 80–90% der Leine
│  │
│  └─ Dyneema/HMPE
│     ├─ NUR als Verbindungsstropp, nicht als Ankerleine
│     ├─ Brummel-Spleiß oder Dyneema-Softschäkel
│     └─ KEINE Elastizität → nicht als Rode-Leine geeignet
│
├─ Verbindung Kette → Leine:
│  ├─ Option A: Schäkel durch Kausch
│  │  ├─ Schäkel WLL ≥ Kette WLL
│  │  ├─ Sicherungsdraht am Bolzen
│  │  └─ Kausch-Innendurchmesser passend für Schäkelbolzen
│  │
│  ├─ Option B: Dedizierter Kette-Leine-Konnekter
│  │  ├─ Produkte: Kong, Mantus Chain-Rope Connector
│  │  ├─ Vorteil: Windlass-kompatibel, sauberer Übergang
│  │  └─ Preis: 30–80 EUR
│  │
│  └─ Option C: Kenter-Glied mit angespleißtem Auge
│     ├─ Kenter durch Leinenauge → windlass-fähig
│     └─ Vorteil: Maßgleich mit Kettenglied
│
└─ Test vor Erstverwendung:
   ├─ Verbindung mit 50% der Leinen-WLL belasten (Winch oder Auto)
   ├─ 30 Sekunden halten
   ├─ Prüfen auf Rutschen, Verformung, Kausch-Öffnung
   └─ Windlass-Test: Verbindung muss durch Bugrolle und über Kettennuss laufen
```

---

## 10. Kettenpflege

### 10.1 Reinigung

**Nach jeder Ankerung:**
- Kette beim Einholen mit Frischwasser abspritzen (Deckwaschanlage)
- Schlamm, Sand und Seewasser entfernen
- Reduziert Salzkristallbildung im Kettenkasten
- Reduziert Geruchsbildung im Kettenkasten

**Saisonale Reinigung (Frühjahr/Herbst):**
- Kette komplett ausgeben
- Hochdruckreiniger (100–150 bar) über die gesamte Länge
- Festsitzenden Schlamm und Bewuchs entfernen
- Trocknen lassen (min. 4h bei Sonnenschein)

**Tiefenreinigung (alle 2–3 Jahre):**
- Kette in Zitronensäure-Bad einlegen (10% Lösung, 24h)
- Löst Kalkablagerungen und leichte Korrosion
- Anschließend gründlich mit Frischwasser spülen
- NICHT mit Salzsäure reinigen (greift Zink an!)

### 10.2 Inspektion

**Inspektionsintervalle:**

| Nutzung | Visuelle Prüfung | Detaillierte Prüfung | Messung |
|---|---|---|---|
| Wochenendsegler | Jede Ankerung (grob) | Saisonbeginn | Alle 3 Jahre |
| Fahrtensegler | Jede Ankerung | Halbjährlich | Jährlich |
| Blauwasser | Jede Ankerung | Vierteljährlich | Halbjährlich |
| Charterboot | Jede Rückgabe | Monatlich | Vierteljährlich |

**Inspektions-Checkliste:**

```
□ Verzinkung: Prozent blanker Stahlstellen geschätzt
□ Rost: Flächig oder punktuell? Wo in der Kette?
□ Gliedermaße: Stichproben alle 10m (Schieblehre)
□ Längung: >5% gegenüber Nennmaß?
□ Steife Glieder: Jedes Glied muss frei drehen
□ Wirbel: Drehbar unter Last? Korrosion?
□ Schäkel: Bolzen fest? Sicherungsdraht intakt?
□ Markierung: Noch lesbar?
□ Konnektoren: Alle fest, gesichert?
□ Bitter End: Befestigung intakt, lösbar?
□ Kettenkasten: Drainage frei?
□ Bugrolle: Scharfe Kanten? Verschleiß?
□ Kettennuss: Zahnprofil verschlissen?
```

### 10.3 Re-Galvanisierung — Zeitplanung

**Typischer Lebenszyklus:**

```
Jahr 0:   Neue Kette, 70–100 µm Zink
Jahr 1-3: Geringe Abnutzung, 50–80 µm verbleibend
Jahr 3-5: Sichtbarer Verschleiß, 30–50 µm verbleibend
Jahr 5-7: Deutlicher Verschleiß, <30 µm, erste Rostflecken
          → RE-GALVANISIERUNG EMPFOHLEN
Jahr 7-10: Ohne Re-Galv.: zunehmend Rost, Pitting beginnt
           → AUSTAUSCH ERWÄGEN
Jahr 10+: Ohne Pflege: Kette nicht mehr vertrauenswürdig
          → AUSTAUSCH ERFORDERLICH
```

**Timing der Re-Galvanisierung:**
- Idealerweise im Winterlager (Oktober–März)
- Vorlaufzeit bei Verzinkerei: 2–4 Wochen
- Transport organisieren (Kette ist schwer!)
- Alternative: Kette während Werftaufenthalt mitgeben

### 10.4 Kettenkastenmanagement

**Probleme durch mangelhaftes Kettenkastenmanagement:**
1. Fauliger Geruch (anaerobe Bakterien im stehenden Wasser)
2. Beschleunigte Korrosion
3. Verklemmte Kette
4. Wasseransammlung im Bug (Trimm!)
5. Spaltkorrosion bei Edelstahlkette

**Best Practices:**

1. **Drainage sicherstellen:**
   - Ablaufloch am tiefsten Punkt des Kastens
   - Sieb gegen Verstopfung
   - Schlauch zur Bilge (mit Rückschlagventil)
   - Monatlich prüfen

2. **Belüftung:**
   - Decksventilator über Kettenkasten (Dorade-Box)
   - Oder: Lüftungsschlitze in der Zugangsluke
   - Verhindert Kondensation und Geruchsbildung

3. **Kettenführung:**
   - Rohr vom Deck in den Kasten (gerade, Ø = 3× Kettendurchmesser)
   - Kein scharfer Knick
   - Gummidurchführung oben (reduziert Lärm)

4. **Reinigung:**
   - Einmal pro Saison: Kette raus, Kasten auswaschen
   - Desinfizieren: verdünnte Essigessenz oder Natron
   - Trocknen lassen vor Wiederbefüllung

### 10.5 Frischwasserspülung

Die Frischwasserspülung der Kette beim Einholen ist die einfachste und effektivste Pflegemaßnahme:

**Methoden:**

| Methode | Effektivität | Kosten | Aufwand |
|---|---|---|---|
| Eimer Frischwasser über Bugrolle | 30% | 0 EUR | Gering |
| Gartenschlauch an Steg | 70% | 0 EUR | Mittel |
| Deckwaschpumpe mit Düse | 90% | 200–500 EUR (Pumpe) | Gering (einmal installiert) |
| Druckwassersystem mit Sprühdüse | 95% | 50–100 EUR (Düse) | Sehr gering |

**Empfehlung:** Eine fest montierte Sprühdüse am Ankerbugrolle-Bereich, die beim Einholen automatisch die Kette absprüht, ist die effektivste Lösung. Kosten: ca. 50–100 EUR für Düse und Schlauch, gespeist aus der Bord-Druckwasseranlage.

### 10.6 Winterlagerung

**Vorbereitung:**
1. Kette komplett ausgeben und mit Hochdruckreiniger reinigen
2. Trocknen lassen (min. 24h)
3. Visuelle Inspektion (Checkliste s. Abschnitt 10.2)
4. Verzinkungszustand dokumentieren (Fotos für AYDI-Analyse)
5. Leichte Konservierung: Lanolin-Spray oder ACF-50

**Lagerung:**
- Trocken lagern (nicht im feuchten Kettenkasten über Winter)
- Kette in Plastikfass oder auf Palette
- Vor Nässe und Spritzwasser schützen
- Nicht direkt auf Betonboden (Feuchtigkeit von unten)

**Wiederinbetriebnahme:**
- Kette auf Beschädigungen prüfen (Transportschäden)
- Markierung prüfen/erneuern
- Probelauf über Windlass
- Verbindungen und Sicherungen prüfen
- Kettenzähler kalibrieren

---

## 11. FAQ — Häufige Fragen

### F01: Welche Kettengröße brauche ich für mein Boot?

**Antwort:** Die Kettengröße richtet sich nach Bootslänge und Verdrängung. Als Faustregel: 6mm für Boote bis 8m, 8mm für 8–12m, 10mm für 12–16m, 12mm für 16–22m. Die detaillierte Tabelle finden Sie in Abschnitt 3.1. Entscheidend ist aber auch die Windlass-Kompatibilität — die Kettennuss muss zum Kettendurchmesser und -typ passen.

### F02: Wie viel Kette brauche ich?

**Antwort:** Küstenfahrt: 40–60m. Offshore: 60–80m. Blauwasser: 80–120m. Die Berechnung basiert auf der maximalen Ankertiefe multipliziert mit dem Scope (5:1 bis 7:1) plus Reserve. Details in Abschnitt 3.4.

### F03: DIN 766 oder G40 — was ist besser?

**Antwort:** Keines ist "besser" — es sind verschiedene Standards. DIN 766 ist der europäische Standard, G40/BBB der US-amerikanische. Die Kettennuss Ihres Windlass bestimmt, welchen Standard Sie brauchen. In Europa: DIN 766. In den USA: G40. Mischen ist nicht möglich.

### F04: Kann ich eine größere Kettengröße auf meinen Windlass setzen?

**Antwort:** Nur wenn der Windlass-Hersteller eine Tausch-Kettennuss für die größere Kette anbietet UND der Motor die größere Kette bewältigen kann. Eine Nummer größer ist oft möglich (z.B. 8→10mm), zwei Nummern größer (z.B. 8→12mm) erfordert fast immer einen neuen Windlass.

### F05: Edelstahl oder verzinkter Stahl?

**Antwort:** Verzinkter Stahl ist der Standard und empfehlenswert. Vorteile: günstiger, höhere Streckgrenze, einfach re-galvanisierbar. Edelstahl 316L: teurer, niedrigere Streckgrenze, Risiko der Spaltkorrosion, aber rostfrei und ästhetisch. Edelstahl nur für Yachten, wo Sauberkeit/Optik entscheidend und Budget kein Thema ist.

### F06: Wie erkenne ich, ob meine Verzinkung noch gut ist?

**Antwort:** Kette reinigen und inspizieren. >70% silber/grau = gut. 50–70% = mäßig, Re-Galvanisierung planen. <50% = schlecht, Re-Galvanisierung nötig. Details im Entscheidungsbaum T04 (Abschnitt 9.4).

### F07: Was kostet eine Re-Galvanisierung?

**Antwort:** Ca. 3–6 EUR pro Meter, abhängig von Kettendurchmesser und Länge. 100m 10mm Kette: ca. 400–600 EUR. Inklusive Transport, Entrostung, Verzinkung. Lohnt sich fast immer gegenüber Neukauf (Neukette ca. 800–1.200 EUR).

### F08: Wie markiere ich meine Kette am besten?

**Antwort:** Kombination aus Sprühlack-Markierung (alle 10m, Rot-Gelb-Blau-System) und Kabelbindern als Backup. Idealerweise zusätzlich einen elektronischen Kettenzähler. Markierung jährlich erneuern. Details in Abschnitt 3.6.

### F09: Muss ich die Kette nach jedem Ankern spülen?

**Antwort:** Idealerweise ja. In der Praxis: mindestens nach Ankerungen in Schlick, Sand oder bei längerem Ankern. Eine Frischwasser-Sprühdüse am Bug (fest installiert, an die Druckwasserpumpe angeschlossen) macht dies einfach. Kostet ca. 50–100 EUR und verlängert die Lebensdauer der Kette erheblich.

### F10: Was ist der Unterschied zwischen Scope 3:1 und 7:1?

**Antwort:** Der Scope ist das Verhältnis von ausgegebener Kette zu Wassertiefe (+ Bughöhe). 3:1: Minimum für ruhige Bedingungen, der Zugwinkel am Anker ist relativ steil. 7:1: für Starkwind, der Zug kommt fast horizontal am Anker an. Mehr Scope = mehr Sicherheit, aber größerer Schwoikreis.

### F11: Kann ich verschiedene Kettengüten mischen?

**Antwort:** Technisch ja, wenn die Maße identisch sind (z.B. zwei Stücke DIN 766 mit gleichen Maßen). Verschiedene Standards mischen (z.B. DIN 766 + G40) ist nicht empfehlenswert, da die Maße minimal abweichen und Probleme mit der Kettennuss entstehen können.

### F12: Wie sicher ist ein Schraubglied (C-Link) als Verbinder?

**Antwort:** Ein Schraubglied ist die schwächste Verbindungsmethode. WLL nur 50–70% der Kettenbruchlast. Bolzen muss mit Sicherungsdraht oder Kontermutter gesichert werden. Besser: Kenter-Glied (80–100% Bruchlast) oder Hammerschloss. Für dauerhafte Installation ein Kenter-Glied verwenden.

### F13: Mein Windlass schafft es nicht, den Anker zu heben. Woran liegt das?

**Antwort:** Mögliche Ursachen: 1) Windlass unterdimensioniert für Kette + Anker + Tiefe. 2) Batteriespannung zu niedrig (häufigste Ursache!). 3) Kette klemmt im Kasten. 4) Anker sitzt fest im Grund. 5) Korrodierte Elektrik. Erste Maßnahme: Batteriespannung unter Last messen.

### F14: Wie lange hält eine Ankerkette?

**Antwort:** Richtig gepflegt: 10–20 Jahre (mit Re-Galvanisierung nach 5–7 Jahren). Ohne Pflege: 5–8 Jahre. Blauwasser-Intensivnutzung: 5–10 Jahre. Die mechanische Lebensdauer des Stahls übersteigt die der Verzinkung bei weitem — daher ist Re-Galvanisierung die wirtschaftlichste Maßnahme.

### F15: Was mache ich, wenn der Anker nicht loskommt?

**Antwort:** 1) Motor voraus über den Anker fahren (Zug umkehren). 2) Kette kurzstag einholen und warten (Swell kann Anker lösen). 3) Kette mit Snatch-Block an Klampe legen, unter Motorkraft "ausbrechen". 4) Trip-Leine verwenden (wenn vorhanden). 5) Taucher. 6) Letztes Mittel: Kette am Bitter End kappen und Anker aufgeben.

### F16: Soll ich einen Ankerwirbel verwenden?

**Antwort:** Ja, empfohlen. Ein Wirbel verhindert, dass sich die Kette beim Schwoien verdreht. Verdrehte Kette kann in der Kettennuss klemmen. Qualitätsprodukte: Mantus, Kong, Wichard. Bruchlast muss ≥ Kettenbruchlast sein. Kein Billigwirbel verwenden.

### F17: Wie befestige ich das Ende der Kette im Kettenkasten?

**Antwort:** Mit einer LÖSBAREN Verbindung! Niemals schweißen oder dauerhaft verbolzen. Standard: 2–3m Nylon-Leine vom Kettenende zu einem Augbolzen im Kasten, die im Notfall mit einem Messer gekappt werden kann. Alternativ: Hammerschloss mit Splint. Details in Abschnitt 6.7.

### F18: Meine Kette riecht fürchterlich im Kettenkasten. Was tun?

**Antwort:** Ursache ist anaerobe Bakterien in stehendem Wasser mit organischem Material (Schlamm, Algen). Lösung: 1) Kette raus. 2) Kasten mit Essigessenz oder Natronlösung reinigen. 3) Drainage prüfen und freihalten. 4) Belüftung verbessern. 5) Kette beim Einholen IMMER mit Frischwasser abspritzen. 6) Periodisch Kasten trocknen lassen.

### F19: Kann ich meine 8mm Kette durch 10mm ersetzen, ohne den Windlass zu tauschen?

**Antwort:** Nur wenn Ihr Windlass eine Wechsel-Kettennuss für 10mm anbietet UND die Motorleistung ausreicht. Die meisten 700W+ Windlasses unterstützen 8mm und 10mm mit Tausch-Gypsy. Prüfen Sie auch den Kettenkasten (10mm Kette braucht ca. 60% mehr Volumen) und den Bugtrimm (ca. 60% mehr Gewicht).

### F20: Was ist eine "kalibrierte" Kette?

**Antwort:** Eine kalibrierte Kette hat eng tolerierte Gliedermaße, die exakt in die Taschen der Kettennuss passen. Ohne Kalibrierung springt die Kette oder klemmt. Für jede Windlass-Anwendung ist kalibrierte Kette Pflicht. DIN 766 und G40/BBB sind kalibriert. Baumarkt-Kette oder DIN 764 (Langglied) sind es nicht.

### F21: Brauche ich einen Kettenstopper?

**Antwort:** Ja, dringend empfohlen. Ein Kettenstopper (auch Devil's Claw) entlastet den Windlass bei geankerten Boot. Ohne Kettenstopper hängt die gesamte Last am Windlass-Getriebe — das ist nicht dafür ausgelegt. Zusätzlich: Bridle oder Reitgewicht für schwere Bedingungen.

### F22: Was ist ein Reitgewicht und wann brauche ich es?

**Antwort:** Ein Reitgewicht (Kellet) ist ein Gewicht (5–15 kg), das an einem Karabiner auf der Kette heruntergelassen wird. Es vertieft die Kettenary und reduziert den Zugwinkel am Anker. Sinnvoll bei: wenig Kette ausgegeben (enger Ankerplatz), erwarteten Starkwind, zusätzlicher Sicherheit. Nachteil: Kompliziert das Bergen.

### F23: Meine Kette ist 10 Jahre alt und nie re-galvanisiert worden. Taugen die noch?

**Antwort:** Wahrscheinlich nicht ohne gründliche Inspektion. Nach 10 Jahren ohne Re-Galvanisierung ist die Verzinkung bei normaler Nutzung vollständig aufgebraucht. Prüfpunkte: Querschnittsverlust der Glieder (<10%?), Pitting-Tiefe (<0,5mm?), Längung (<5%?). Wenn mechanisch OK: Re-Galvanisierung möglich. Im Zweifel: Neukauf.

### F24: Wie wichtig ist die Bitter-End-Befestigung?

**Antwort:** Lebenswichtig — in zweifacher Hinsicht. Erstens muss die Kette gesichert sein, damit nicht die gesamte Rode verloren geht, wenn zu viel Kette ausgegeben wird. Zweitens muss sie lösbar sein, um die Kette in einer Notsituation kappen zu können. Die Bitter-End-Befestigung muss einmal pro Saison geprüft werden.

### F25: Kann ich Kette aus dem Baumarkt als Ankerkette verwenden?

**Antwort:** NEIN. Baumarktkette ist typisch DIN 5685 (unkalibriert), hat keine garantierte Bruchlast, keine marine Verzinkung und passt nicht in Windlass-Kettennüsse. Für Anwendungen ohne Windlass (Handanker kleiner Boote <7m) kann DIN 766 aus dem Baumarkt akzeptabel sein — aber nur mit Normbezeichnung und Prüfzertifikat.

### F26: Was ist der Unterschied zwischen WLL, Bruchlast und Prüflast?

**Antwort:** **WLL (Working Load Limit):** Die maximale Last, die im normalen Betrieb aufgebracht werden darf. Typisch: 25% der Bruchlast (Faktor 4). **Bruchlast (Breaking Load):** Die Last, bei der die Kette mit Sicherheit bricht. **Prüflast (Proof Load):** Eine definierte Last, der jede Kette bei der Herstellung standhalten muss. Typisch: 50% der Bruchlast. Für Ankerketten ist der Scope so zu wählen, dass die WLL nie überschritten wird.

### F27: Woher weiß ich, ob meine Kette DIN 766 oder G40 ist?

**Antwort:** 1) Kaufbeleg/Rechnung prüfen. 2) Normbezeichnung auf dem Endglied eingeprägt? 3) Gliedmaße messen und mit Tabellen vergleichen (DIN 766: 8mm hat Teilung 28mm, G40 5/16" hat Teilung 22,2mm). 4) Kettenuss-Hersteller fragen, welche Kette für Ihr Modell. 5) Im Zweifel: Testglied beim Windlass-Hersteller anfragen.

---

## 12. Glossar

### A

**ABYC H-40:** American Boat and Yacht Council Standard für Ankern, Festmachen und Kraftpunkte ("Anchoring, Mooring, and Strong Points"). Definiert Empfehlungen für Dimensionierung, Scope und Ausrüstung.

**Ankerschäkel:** Verbindungsschäkel zwischen Anker und Kette/Wirbel. Muss mindestens die WLL der Kette haben.

**Ankerstopper:** Siehe Kettenstopper.

**Ankerwirbel (Anchor Swivel):** Drehbares Verbindungselement zwischen Kette und Anker. Verhindert Verdrehung der Kette beim Schwoien.

**Aqua-Met:** Polyester-Beschichtung für Ankerketten, entwickelt von Maggi (Italien). Schützt Deck und Gelcoat vor Zinkabrieb.

### B

**BBB (Triple-B):** US-amerikanische Bezeichnung für G40 High-Test-Ankerkette. Kalibriert für marine Windlass-Anwendungen.

**Bitter End:** Das bootsseitige Ende der Ankerkette im Kettenkasten. Muss befestigt, aber lösbar sein.

**Bridle (Ankerbridle):** Y-förmige Leine vom Bug zum Ankergeschirr, verteilt die Last auf beide Bugklampen und dämpft Rucken.

**Bruchlast (Breaking Load, BL):** Die Last, bei der die Kette unter Zugbelastung bricht. Immer höher als WLL und Prüflast.

### C

**Catenary (Kettenary/Kettenlinie):** Die natürliche Kurve, die eine hängende Kette unter Eigengewicht bildet. Entscheidend für Stoßdämpfung und horizontalen Zugwinkel.

**CE-Kategorie:** Einstufung nach EU-Richtlinie 2013/53/EU für Sportboote (A=Ozean, B=Offshore, C=Küste, D=Geschützt).

**Chain Counter (Kettenzähler):** Elektronisches Gerät, das die ausgegebene Kettenlänge misst (durch Zählen der Kettennuss-Impulse).

**Chain Locker:** Siehe Kettenkasten.

**Crevice Corrosion:** Siehe Spaltkorrosion.

### D

**DIN 766:** Deutsche Industrienorm für kalibrierte Kurzglied-Rundstahlketten. Europäischer Standard für Yacht-Ankerketten.

**DIN 764:** Deutsche Industrienorm für langgliedrige Rundstahlketten. NICHT für Windlass geeignet.

**DIN 5685:** Deutsche Industrienorm für unkalibrierte Ketten. Nicht für Ankerzwecke empfohlen.

**Duplex-Stahl:** Hochlegierter Edelstahl (z.B. 2205) mit höherer Festigkeit als 316L. Premium-Material für Ankerketten.

### E

**Elektrolyse:** Galvanische Korrosion durch Kontakt verschiedener Metalle in einem Elektrolyten (Seewasser). Kann Ankerketten schnell zerstören.

**EN ISO 1461:** Europäische Norm für Feuerverzinkung. Definiert Mindestschichtdicken und Prüfverfahren.

### F

**Feuerverzinkung (Hot-Dip Galvanizing, HDG):** Korrosionsschutzverfahren, bei dem Stahl in flüssiges Zink (450°C) getaucht wird. Standard für Ankerketten.

### G

**G30 (Proof Coil):** US-Kettengrade mit niedrigster Festigkeit. Bedingt für Ankerzwecke geeignet.

**G40 (High Test/BBB):** US-Standard-Kettengrade für marine Ankerketten. Kalibriert für Windlass.

**G43 (High Test):** Höherfeste US-Kettengrade. Ca. 15–20% höhere WLL als G40.

**G70 (Transport):** Hochfeste Transportkette. NICHT für marine Ankerzwecke geeignet.

**G80 (Alloy Lifting):** Legierte Hebezeugkette. KATEGORISCH UNGEEIGNET für Ankerzwecke.

**Gypsy (Kettennuss):** Profiliertes Rad in der Ankerwinch, das die Kettenglieder greift und transportiert.

### H

**Hammerschloss (Hammer Lock):** Robuster Kettenverbinder mit Bolzen und Splint. Hohe Bruchlast.

### I

**ISO 4565:** Internationale Norm für kalibrierte Kurzgliedketten. Internationaler Gegenpart zu DIN 766.

### K

**Kalibrierte Kette:** Kette mit eng tolerierten Gliedermaßen für Windlass-Kompatibilität. Pflicht bei elektrischer Ankerwinde.

**Kenter-Glied (Kenter Link):** Dreiteiliges Verbindungsglied mit Außenmaßen, die dem Kettenglied entsprechen. Windlass-kompatibel.

**Kettenkasten (Chain Locker):** Stauraum im Bug für die Ankerkette. Muss entwässert und belüftet sein.

**Kettenlinie:** Siehe Catenary.

**Kettennuss:** Siehe Gypsy/Wildcat.

**Kettenstopper (Chain Stopper):** Mechanisches Klemmgerät, das die Kette fixiert und den Windlass entlastet.

**Kurzgliedkette (Short Link Chain):** Kette mit kurzem Gliedverhältnis (ca. 3,5:1). Standard für Ankerwindlass.

### L

**Langgliedkette (Long Link Chain):** Kette mit langem Gliedverhältnis (5:1 bis 6:1). NICHT für Windlass geeignet. Verwendet für Moorings.

### M

**Mixed Rode:** Kombination aus Kette (unten) und Nylon-Leine (oben) als Ankerleine.

**Mooring:** Festgelegter Ankerplatz mit permanent installiertem Ankerstein und Boje.

### N

**NACM:** National Association of Chain Manufacturers (USA). Definiert US-Kettenstandards und -prüfungen.

### O

**Opferanode:** Zinkanode, die galvanische Korrosion auf sich zieht und damit andere Metalle schützt.

### P

**Pitting (Lochfraß):** Punktueller Korrosionsangriff, der tiefe Gruben im Metallquerschnitt erzeugt.

**Proof Load (Prüflast):** Die Last, mit der jede Kette bei der Herstellung geprüft wird. Typisch 50% der Bruchlast.

### R

**Reitgewicht (Kellet/Sentinel):** Gewicht, das auf der Ankerkette herabgelassen wird, um die Kettenary zu vertiefen.

**Rode:** Gesamtheit der Verbindung zwischen Boot und Anker (Kette und/oder Leine).

### S

**Schäkel (Shackle):** U-förmiger Metallbügel mit Bolzen. Verbindungselement zwischen Kette, Wirbel und Anker.

**Scope:** Verhältnis der ausgegebenen Rode-Länge zur Wassertiefe (plus Bughöhe). Standard: 5:1 bis 7:1.

**Schwoien:** Drehen des Bootes um den Ankerpunkt durch Strömung oder Wind.

**Sicherungsdraht (Seizing Wire):** Edelstahldraht (1,0–1,2mm) zur Sicherung von Schäkelbolzen gegen unbeabsichtigtes Lösen.

**Spaltkorrosion (Crevice Corrosion):** Korrosion in engen Spalten (z.B. zwischen Kettengliedern), wo Sauerstoffmangel die Passivierung von Edelstahl verhindert.

**Stegkette (Stud-Link):** Kette mit Querstrebe in jedem Glied. Standard ab 22mm für Schiffe. Im Yachtbereich selten.

**Stegloskette (Studless):** Kette ohne Querstrebe. Standard für Yachten.

**Streckgrenze (Yield Strength):** Die Spannung, ab der sich das Material plastisch (dauerhaft) verformt. Bei Ankerketten: darf nicht überschritten werden.

### T

**Teilung (Pitch):** Der Abstand zwischen zwei gleichliegenden Punkten aufeinanderfolgender Kettenglieder. Entscheidend für Kettennuss-Kompatibilität.

### U

**Unkalibrierte Kette:** Kette mit größeren Maßtoleranzen. NICHT für Windlass geeignet.

### W

**Wildcat:** Profiliertes Rad speziell für Kettenbetrieb (im Gegensatz zur Gypsy, die auch Leine aufnehmen kann).

**Windlass (Ankerwinch):** Elektrische oder hydraulische Winde zum Einholen und Ausgeben der Ankerkette.

**WLL (Working Load Limit):** Die maximale zulässige Arbeitslast im normalen Betrieb. Typisch: 25% der Bruchlast (Sicherheitsfaktor 4).

### Z

**Zinkanode:** Opferanode aus Zink zum Schutz gegen galvanische Korrosion.

**Zugfestigkeit (Tensile Strength):** Die maximale Spannung, die ein Material vor dem Bruch erträgt.

---

## 13. Schnell-Referenz

### Kettenwahl auf einen Blick

```
┌─────────────────────────────────────────────────────────┐
│              ANKERKETTEN-SCHNELLREFERENZ                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  BOOTSLÄNGE → KETTENMASS                                │
│   6–8m  → 6mm DIN 766                                  │
│   8–12m → 8mm DIN 766  ← Meistverkauft                 │
│  12–16m → 10mm DIN 766                                  │
│  16–22m → 12mm DIN 766                                  │
│  22–26m → 13mm DIN 766                                  │
│  26–30m → 14mm DIN 766                                  │
│                                                         │
│  KETTENLÄNGE → FAHRTENGEBIET                            │
│  Küste:      40–60m                                     │
│  Offshore:   60–80m                                     │
│  Blauwasser: 80–120m                                    │
│                                                         │
│  SCOPE → BEDINGUNG                                      │
│  3:1  Minimum (nur Mittag, ruhig)                       │
│  5:1  Standard (Nachtankerung)                          │
│  7:1  Starkwind (>20 Knoten)                            │
│  10:1 Sturm (>30 Knoten)                                │
│                                                         │
│  VERZINKUNG → ZUSTAND                                   │
│  >70% silber: GUT (5+ Jahre)                            │
│  50-70%:      MÄSSIG (2-3 Jahre)                        │
│  <50%:        SCHLECHT (Re-Galv. nötig)                 │
│                                                         │
│  VERBINDUNGEN                                           │
│  Anker—Schäkel—Wirbel—Schäkel—KETTE—Kettennuss—Kasten  │
│  Alle Schäkel: Sicherungsdraht!                         │
│  Bitter End: LÖSBAR befestigt!                          │
│                                                         │
│  PFLEGE                                                 │
│  Nach Ankern: Frischwasser über Kette                   │
│  Saisonbeginn: Inspektion + Markierung                  │
│  Alle 5–7 Jahre: Re-Galvanisierung                      │
│  Jährlich: Verbindungen prüfen                          │
│                                                         │
│  PREIS (verzinkt, pro Meter, 2026)                      │
│  6mm: 3–5 EUR  │  10mm: 8–12 EUR  │ 14mm: 16–22 EUR   │
│  8mm: 5–8 EUR  │  12mm: 11–16 EUR │                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Notfall-Checkliste

```
┌─────────────────────────────────────────────────────────┐
│              NOTFALL-CHECKLISTE ANKERKETTE               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ANKER HÄLT NICHT:                                      │
│  □ Mehr Kette ausgeben (Scope erhöhen)                  │
│  □ Motor in Bereitschaft                                │
│  □ Zweitanker vorbereiten                               │
│  □ GPS-Ankeralarm aktiv?                                │
│                                                         │
│  KETTE KLEMMT:                                          │
│  □ Windlass AUS                                         │
│  □ Kette manuell prüfen (am Bug)                        │
│  □ Verdrehung? → Begradigen                             │
│  □ Fremdkörper? → Entfernen                             │
│                                                         │
│  ANKER SITZT FEST:                                      │
│  □ Kette kurzstag → warten (Swell nutzen)               │
│  □ Motor voraus über Anker fahren                       │
│  □ Kette an Klampe → unter Motor "ausbrechen"           │
│  □ Im Notfall: Bitter End kappen                        │
│                                                         │
│  KETTE BRICHT:                                          │
│  □ Zweitanker sofort ausbringen                         │
│  □ Motor starten                                        │
│  □ Position mit GPS markieren (Bergung)                  │
│  □ Hafenbehörde informieren                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ANHANG A — Fallstudie: Kettentausch 38-Fuß-Blauwasseryacht {#anhang-a}

### A.1 Ausgangssituation

**Yacht:** Bavaria 38 Cruiser, Baujahr 2015, Segelyacht
**Eigner:** Deutsche Crew, plant Atlantiküberquerung 2027
**Bestehende Kette:** 50m, 8mm DIN 766, feuerverzinkt, Alter: 8 Jahre
**Windlass:** Lofrans Tigres 1000W, Kettennuss 8mm DIN 766
**Anker:** Delta 14 kg

### A.2 Problemanalyse

Die bestehende 50m 8mm Kette war nach 8 Jahren in gutem mechanischen Zustand, aber:
- Verzinkung zu 60% aufgebraucht
- 50m Kette für Blauwasser unzureichend (max. Ankertiefe 20m → Scope 5:1 = nur 100m Tiefe + Bughöhe)
- 8mm Kette grenzwertig für 10-Tonnen-Yacht in Sturmankern

### A.3 Entscheidungsprozess

**Option 1: Bestehende Kette re-galvanisieren + verlängern**
- Re-Galv. 50m 8mm: ca. 180 EUR
- Zusätzliche 50m 8mm: ca. 400 EUR
- Kenter-Glied: 20 EUR
- Gesamt: ca. 600 EUR
- Nachteil: Immer noch 8mm, Verbindungsstelle, alte Kette neben neuer

**Option 2: Komplett neue 100m 10mm Kette**
- 100m 10mm DIN 766 Premium (Maggi): ca. 1.200 EUR
- Neue Kettennuss 10mm für Lofrans Tigres: ca. 120 EUR
- Neuer Ankerwirbel (Mantus, für 10mm): ca. 130 EUR
- Gesamt: ca. 1.450 EUR
- Vorteil: Durchgehend, stärker, neuer Windlass-Nuss

**Option 3: Upgrade auf 10mm + neuen Windlass**
- Neuer Windlass Lofrans Kobra 1500W: ca. 1.800 EUR
- 100m 10mm Kette: ca. 1.200 EUR
- Einbau: ca. 400 EUR
- Gesamt: ca. 3.400 EUR
- Vorteil: Zukunftssicher, leistungsstärkere Ankerwinch

### A.4 Gewählte Lösung

Die Crew entschied sich für **Option 2**. Der bestehende Lofrans Tigres 1000W unterstützt 10mm DIN 766 mit Wechsel-Kettennuss. Die 1000W Leistung ist für 100m × 10mm (220 kg) grenzwertig, aber ausreichend, da die Kette nie vollständig senkrecht geborgen wird.

### A.5 Durchführung

1. Alte Kette komplett ausgeben und auf Steg auflegen
2. Windlass-Kettennuss von 8mm auf 10mm wechseln (4 Schrauben, 30 Minuten)
3. Neue 100m 10mm Kette auf Steg auslegen
4. Kettenmarkierung aufbringen (2K-Sprühlack, alle 10m)
5. Kettenzähler neu kalibrieren (Teilung 35mm statt 28mm)
6. Wirbel und Schäkel montieren, Sicherungsdraht anbringen
7. Kette einholen und Windlass-Funktion prüfen
8. Bitter End mit Nylon-Leine befestigen

### A.6 Ergebnis

Gesamtkosten: 1.480 EUR inkl. Versand und Kleinteile. Zeitaufwand: ca. 6 Stunden (ein Samstag). Die neue 10mm Kette bietet 56% höhere Bruchlast (25 kN vs. 16 kN), ausreichende Länge für Blauwasser-Scope und 70µm+ frische Verzinkung für die nächsten 7–10 Jahre.

**Confidence: documented** — Realer Erfahrungsbericht, typische Konfiguration.

---

## ANHANG B — Fallstudie: Kettenbruch bei Sturmankern {#anhang-b}

### B.1 Ausgangssituation

**Yacht:** Jeanneau Sun Odyssey 45, Baujahr 2008
**Position:** Ankerbucht, Kroatien, Juli
**Kette:** 60m, 10mm, angeblich G40, gekauft bei unbekanntem Online-Händler
**Windstärke:** Bora, bis 55 Knoten in Böen (Bft 10)

### B.2 Hergang

Die Yacht lag seit 3 Tagen vor Anker (Rocna 25 kg). Nachts kam eine Bora-Front mit 55-Knoten-Böen. Die Yacht begann zu gieren und ruckte heftig in der Kette. Nach ca. 2 Stunden brach die Kette am 5. Glied vor dem Ankerwirbel. Die Yacht trieb auf eine Felsküste. Schaden: ca. 35.000 EUR (Rumpf, Ruder, Kiel).

### B.3 Fehleranalyse

**Untersuchung der Bruchstelle:**
- Bruch an einem Glied, das deutlich dünner war als die Nachbarglieder
- Querschnittsverlust: ca. 25% durch Korrosion (Pitting)
- Verzinkung: vollständig aufgebraucht an den ersten 10m
- Materialprüfung: Zugfestigkeit nur 320 MPa (unter G30-Minimum von 370 MPa!)
- Kalibrierung: Gliedermaße variierten um ±1,5mm (außerhalb jeder Norm)

**Ursache:** Die als "G40" verkaufte Kette war eine minderwertige China-Kette ohne echte Normkonformität. Die niedrige Zugfestigkeit, mangelhafte Verzinkung und fehlende Kalibrierung zeigen, dass es sich um unkontrollierte Ware handelte.

### B.4 Lehren

1. **Kette nur von vertrauenswürdigen Quellen kaufen** (Fachhändler, nicht eBay/AliExpress)
2. **Prüfzertifikat verlangen** und auf Chargennummer prüfen
3. **Kettenanfang inspizieren**: Die ersten 10m tragen die meiste Last
4. **Jährliche Inspektion der gesamten Kettenlänge**
5. **Bei Sturmwarnung: Kette prüfen, bevor der Sturm kommt**
6. **Zweitanker immer seeklar haben**

**Confidence: documented** — Anonymisierter Schadensfall, typisches Szenario.

---

## ANHANG C — Fallstudie: Elektrolyse an Edelstahlkette {#anhang-c}

### C.1 Ausgangssituation

**Yacht:** Hallberg-Rassy 40, Baujahr 2018
**Kette:** 80m, 10mm Edelstahl 316L, Neupreis ca. 3.200 EUR
**Liegeplatz:** Marina, Mittelmeer, Dauerliegeplatz mit Landstrom
**Ankerwirbel:** Mantus (Edelstahl 316L)
**Kettenstopper:** Bronze

### C.2 Problem

Nach 3 Jahren bemerkte der Eigner bei der Frühjahrskontrolle, dass die ersten 5 Glieder der Kette stark korrodiert waren — an einer angeblich "rostfreien" Edelstahlkette. Die Korrosion zeigte sich als tiefe Gruben (Pitting bis 2mm) an den Kontaktflächen zwischen den Gliedern.

### C.3 Ursache

Zwei Faktoren wirkten zusammen:

1. **Galvanische Korrosion:** Der Bronze-Kettenstopper (edler als Edelstahl) erzeugte ein galvanisches Element mit der Edelstahlkette in Seewasser. Die Kette war die Anode und korrodierte.

2. **Spaltkorrosion:** Im Kettenstopperbereich lag die Kette dauerhaft in stehendem Seewasser. In den Spalten zwischen den Gliedern entstand Sauerstoffmangel → Passivierung brach zusammen → Spaltkorrosion.

3. **Vagabundierende Ströme:** Die Marina hatte Probleme mit der Erdung der Landstromversorgung. Vagabundierende Ströme beschleunigten die Korrosion zusätzlich.

### C.4 Lösung

1. Erste 10m der Kette durch neues 316L-Segment ersetzt (Kenter-Glieder)
2. Bronze-Kettenstopper durch Edelstahl 316L ersetzt
3. Isolierscheibe zwischen Kettenstopper und Deck montiert
4. Galvanischer Isolator (Galvanic Isolator) in der Landstromleitung installiert
5. Opferanode (Zink) am Bugbeschlag montiert
6. Kettenkasten-Drainage verbessert (Kette darf nicht in stehendem Wasser liegen)

### C.5 Kosten

- 10m Edelstahlkette 10mm: 360 EUR
- 2× Kenter-Glieder 316L: 80 EUR
- Edelstahl-Kettenstopper: 280 EUR
- Galvanischer Isolator: 150 EUR
- Zinkanode + Montage: 40 EUR
- Arbeitszeit: ca. 8h
- **Gesamt: ca. 910 EUR** (plus 3.200 EUR für die beschädigte Originalkette)

### C.6 Lehren

1. Edelstahlkette ist NICHT wartungsfrei
2. Verschiedene Metalle im Seewasser = galvanisches Element
3. Landstrom ohne Isolator kann massive Schäden verursachen
4. Spaltkorrosion ist das Hauptrisiko bei Edelstahlketten
5. Drainage im Kettenkasten ist bei Edelstahl NOCH wichtiger als bei verzinktem Stahl

**Confidence: documented** — Anonymisierter Praxisfall, häufiges Szenario.

---

## ANHANG D — Fallstudie: Windlass-Inkompatibilität nach Kettenwechsel {#anhang-d}

### D.1 Ausgangssituation

**Yacht:** Bénéteau Océanis 41.1, Baujahr 2019
**Windlass:** Lewmar V3, 1000W
**Originalkette:** 50m, 8mm DIN 766
**Neue Kette:** 50m, 5/16" G40 BBB (in den USA bestellt, deutlich günstiger)

### D.2 Problem

Der Eigner bestellte während eines Aufenthalts in den USA eine 50m G40-BBB-Kette (5/16"), da diese dort ca. 40% günstiger war als DIN 766 in Europa. Nach der Montage traten sofort Probleme auf:

- Kette sprang alle 3–5 Glieder aus der Kettennuss
- Windlass konnte die Kette nicht kontrolliert einholen
- Kette verklemmte sich bei jedem 8. Durchlauf
- Unter Last rutschte die Kette durch

### D.3 Ursache

5/16" G40 hat eine Teilung von 22,2mm und eine Innenweite von 8,7mm. 8mm DIN 766 hat eine Teilung von 28,0mm und eine Innenweite von 11,3mm. Die Maße sind trotz ähnlichem Nenndurchmesser (7,94mm vs. 8,0mm) fundamental verschieden. Die DIN-766-Kettennuss kann die G40-Glieder nicht korrekt greifen.

### D.4 Lösung

Der Eigner hatte zwei Optionen:
1. G40-Kettennuss für den Lewmar V3 bestellen (ca. 120 EUR, 6 Wochen Lieferzeit)
2. DIN-766-Kette kaufen und die G40 verkaufen

Er entschied sich für Option 1 und bestellte eine G40-BBB-5/16"-Gypsy von Lewmar. Nach dem Einbau funktionierte die Kette einwandfrei.

### D.5 Kosten und Zeitverlust

- G40-Kettennuss: 135 EUR (inkl. Versand)
- 6 Wochen Wartezeit (konnte in dieser Zeit nicht ankern, nur Marina)
- Liegergebühren zusätzlich: ca. 600 EUR (Marina statt Ankerbucht)
- Eigentliche "Ersparnis" der günstigen US-Kette: ca. 200 EUR
- **Netto-Verlust: ca. 535 EUR plus 6 Wochen ohne Ankermöglichkeit**

### D.6 Lehren

1. DIN 766 ≠ G40 BBB — trotz ähnlichem Durchmesser
2. Kettennuss und Kette MÜSSEN zusammenpassen
3. "Günstiger" aus den USA bestellen lohnt sich selten
4. Vor dem Kauf: Kettennuss-Spezifikation prüfen
5. Ein Testglied auf der Kettennuss prüfen, BEVOR man 50 oder 100m bestellt

**Confidence: documented** — Typischer Praxisfehler, häufig berichtet in Segelforums.

---

## ANHANG E — Fallstudie: Mixed Rode Optimierung {#anhang-e}

### E.1 Ausgangssituation

**Yacht:** Dufour 390 Grand Large, Baujahr 2021, Mittelmeer-Küstenfahrt
**Verdrängung:** 8.400 kg
**Bestehende Rode:** 50m, 8mm DIN 766, Ganzkette
**Problem:** Buglastigkeit, Kette zu schwer für Regattaeinsatz
**Windlass:** Lofrans X2, 700W

### E.2 Analyse

Die 50m 8mm Kette wiegt 70 kg im Bug. Bei einer 8,4-Tonnen-Yacht ergibt sich:
- Buglastigkeit: ca. 15–20mm zusätzlicher Trimm
- Gewicht: 70 kg im ungünstigsten Moment (Bug) = signifikanter Nachteil bei Regatta
- Kettenkasten: Voll, kein Platz für längere Kette

### E.3 Lösung: Optimierte Mixed Rode

**Neue Konfiguration:**
- 20m 8mm DIN 766 Kette (28 kg)
- 50m 16mm 3-schäftiges Nylon (6,5 kg)
- Kong Kette-Leine-Konnekter (0,3 kg)
- Kausch Edelstahl im Nylon-Auge

**Gewichtsersparnis:** 70 kg → 34,8 kg = **35,2 kg weniger im Bug**

### E.4 Scope-Anpassung

Mit 20m Kette (von 50m) muss der Scope angepasst werden:
- Vorher: 50m Kette bei 8m Tiefe + 1m Bug = 5,5:1 Scope
- Nachher: 70m Rode (20m Kette + 50m Nylon) bei gleicher Tiefe = 7,8:1 Scope
- Plus: Nylon-Dehnung (15%) bietet Stoßdämpfung

### E.5 Ergebnis

- Regatta: Spürbar besserer Trimm, ca. 0,1–0,2 Knoten schneller
- Ankern: Dank längerem Scope (70m statt 50m) sogar bessere Ankerhaltung
- Nachteile: Nylon muss gegen Schamfilen geschützt werden, Mixed Rode erfordert Sorgfalt an der Verbindung
- Kosten: ca. 350 EUR (20m Kette + 50m Nylon + Konnekter + Kausch)

**Confidence: documented** — Praxisbericht, typische Konfiguration für Küstensegler.

---

## ANHANG F — Fallstudie: Kettenmarkierung Langfahrt {#anhang-f}

### F.1 Ausgangssituation

**Yacht:** Ovni 435, Aluminium-Segelyacht
**Route:** Atlantik-Rundreise 2024–2026 (Europa → Karibik → Azoren → Europa)
**Kette:** 100m, 10mm DIN 766
**Windlass:** Lofrans Falcon mit Kettenzähler

### F.2 Erste Markierung (vor Abfahrt)

Das Markierungssystem vor der Abfahrt:
- Sprühlack: Standard Rot-Gelb-Blau, alle 10m
- Kabelbinder: Farbig, als Backup alle 10m
- Kettenzähler: Quick Chain Counter, kalibriert

### F.3 Problem nach 6 Monaten

Nach 6 Monaten Karibik-Fahrt (ca. 150 Ankermanöver):
- Sprühlack: 70% abgerieben (Sand, Koralle, Kettennuss)
- Kabelbinder: 50% verloren oder gebrochen (UV, Hitze)
- Kettenzähler: 8% Abweichung (Sensor verschmutzt)
- Ergebnis: Keine zuverlässige Längenangabe mehr

### F.4 Verbessertes System

**Neues Markierungssystem (in Martinique überarbeitet):**

1. **Basis:** 2K-Epoxid-Sprühlack (International Perfection) auf entfetteter Kette
   - Haftung: Deutlich besser als Sprühlack aus der Dose
   - Haltbarkeit: 12–18 Monate statt 4–6

2. **Edelstahl-Drahtmarker:** 1,5mm Edelstahldraht um Glieder gewickelt (3 Windungen)
   - Abriebfest, UV-resistent
   - Farbcodes: Wärmeschrumpfschlauch über den Draht
   - Windlass-kompatibel (dünn genug)

3. **Ketten-Nummern-System:** Jedes 10. Meter-Glied mit eingravierter Zahl (elektrischer Graveur)
   - Dauerhaft, unzerstörbar
   - Nur 10 Glieder graviert (10, 20, 30... 100)
   - Vertiefung mit Epoxid-Farbe gefüllt

4. **Kettenzähler:** Gereinigt, neu kalibriert, Sensor-Position korrigiert

### F.5 Ergebnis nach weiteren 12 Monaten

- 2K-Lack: 60% noch sichtbar (deutlich besser als Sprühlack)
- Edelstahlmarker: 100% intakt
- Gravierte Zahlen: 100% lesbar
- Kettenzähler: 3% Abweichung (akzeptabel)
- **Fazit:** Kombination aus Gravur + Edelstahlmarker + Kettenzähler ist das beste System für Langfahrt

**Confidence: documented** — Realer Langfahrt-Erfahrungsbericht.

---

## ANHANG G — Fallstudie: Re-Galvanisierung 100m Kette {#anhang-g}

### G.1 Ausgangssituation

**Yacht:** Hallberg-Rassy 48, Dauerliegeplatz Ostsee
**Kette:** 100m, 12mm DIN 766, Alter: 6 Jahre
**Zustand:** Verzinkung zu ca. 60% aufgebraucht, kein mechanischer Verschleiß

### G.2 Vorbereitung

1. Kette komplett ausgeben (auf Steg, 80m Stegplatz nötig!)
2. Hochdruckreiniger: Gesamte Kette reinigen (ca. 2h)
3. Trocknen: 1 Tag Sonnenschein
4. Inspektion: Jedes 10. Glied messen — Durchmesser OK, Längung <2%, kein Pitting

### G.3 Transport

- Kette auf Palette gewickelt (spiralförmig, nicht lose gehäuft)
- Gewicht: 315 kg + Palette = ca. 340 kg
- Transport: Spedition, Abhol- und Lieferservice der Verzinkerei
- Kosten Transport: 180 EUR (hin und zurück, 120 km)

### G.4 Verzinkungsprozess

Die Verzinkerei (Wiegel, Standort bei Hamburg) führte folgenden Prozess durch:

1. **Eingangskontrolle:** Maße, Zustand, Gewicht
2. **Strahlen:** Sandstrahlen auf Sa 2.5 (alle Altbeschichtung und Rost entfernt)
3. **Beizen:** Salzsäure-Bad (15%, 30 Min.)
4. **Spülen:** Frischwasser
5. **Flussmittel:** Zinkammoniumchlorid-Bad (5 Min.)
6. **Verzinken:** 450°C Zinkbad, 4 Minuten Tauchzeit
7. **Abkühlen:** Luftkühlung
8. **Prüfung:** Schichtdickenmessung an 10 Punkten: Ergebnis 72–95 µm (Vorgabe: min. 70 µm)
9. **Ausgangskontrolle:** Visuelle Prüfung, keine Zinknasen, keine Tropfen in Gliedöffnungen

### G.5 Kosten

| Position | Kosten |
|---|---|
| Verzinkung 100m × 12mm (315 kg) | 520 EUR |
| Sandstrahlen (Zusatzleistung) | 180 EUR |
| Transport (hin + zurück) | 180 EUR |
| Kran (Palette auf Steg) | 60 EUR |
| **Gesamt** | **940 EUR** |

Vergleich: Neukette 100m 12mm Premium = ca. 1.600–2.000 EUR

**Ersparnis: 660–1.060 EUR**

### G.6 Ergebnis

Die re-galvanisierte Kette sieht aus wie neu. Die Schichtdicke ist gleichmäßig und liegt über dem Minimum. Die Kalibrierung wurde nicht beeinträchtigt — die Kette läuft einwandfrei über die Kettennuss. Geschätzte Lebensdauer der neuen Verzinkung: weitere 7–10 Jahre.

### G.7 Empfehlung

Re-Galvanisierung lohnt sich, wenn:
- Kette mechanisch einwandfrei (Längung <5%, kein Pitting >0,5mm)
- Kosten Re-Galv. < 60% Neukauf
- Verzinkerei erreichbar (Transport nicht zu teuer)
- Kette kann 2–3 Wochen entbehrt werden

**Confidence: documented** — Realer Vorgang, typische Kosten.

---

## ANHANG H — Fallstudie: Kettenkasten-Redesign Katamaran {#anhang-h}

### H.1 Ausgangssituation

**Yacht:** Lagoon 42, Baujahr 2019, Katamaran
**Problem:** Kettenkasten im Brückendeck, Kette verheddered sich permanent
**Kette:** 80m, 10mm DIN 766
**Windlass:** Quick Genius 1000W

### H.2 Problem

Katamarane haben oft den Kettenkasten im Brückendeck-Bereich zwischen den Rümpfen. Der Kettenkasten der Lagoon 42 ist breit und flach — die Kette fällt ohne Führung in den Kasten und bildet einen chaotischen Haufen.

**Symptome:**
- Kette verklemmt sich beim Ausgeben in 3 von 5 Ankermanövern
- Skipper muss regelmäßig in den Kasten greifen (Verletzungsgefahr!)
- Kette verdreht sich beim Einholen → Windlass-Sprünge
- Maximaler Wassereinbruch durch offene Luke während Ketten-Entwirrung

### H.3 Lösung: Kettenkasten-Redesign

**Maßnahmen:**

1. **Kettenführungsrohr verlängert:**
   - Ursprünglich: Rohr endet 30cm über Kastenboden
   - Neu: Rohr bis 10cm über Kastenboden verlängert (GFK-Rohr, Ø 120mm)
   - Kette fällt nun gezielter und stapelt sich besser

2. **Trennwand eingebaut:**
   - Vertikale GFK-Trennwand in der Mitte des Kastens
   - Kette fällt abwechselnd links und rechts der Wand
   - Verhindert großflächige Verhedderung

3. **Kettenleit-Trichter:**
   - Am unteren Ende des Führungsrohrs: konischer Trichter
   - Leitet die Kette nach links oder rechts (je nach Fallrichtung)
   - Material: HDPE, 3D-gedruckt

4. **Drainage verbessert:**
   - Zweiter Ablauf auf der gegenüberliegenden Seite
   - Beide Abläufe mit Sieb
   - Schlauch zur Bilge mit Rückschlagventil

### H.4 Kosten

| Position | Kosten |
|---|---|
| GFK-Rohr Ø 120mm (1,5m) | 45 EUR |
| GFK-Trennwand (Zuschnitt + Laminierung) | 120 EUR |
| HDPE-Trichter (3D-Druck) | 35 EUR |
| Drainage-Material (Seeventil, Schlauch, Siebe) | 80 EUR |
| Epoxid, Glasgewebe, Kleinteile | 50 EUR |
| **Gesamt (Material)** | **330 EUR** |
| Arbeitszeit (ca. 16h, Eigenbau) | Eigenleistung |

### H.5 Ergebnis

Nach dem Umbau:
- Kettenverhedderer: Von 3/5 auf 0/20 Ankermanövern (kein einziges Mal!)
- Kette läuft frei aus und ein
- Kettenkasten bleibt geordnet
- Drainage funktioniert, kein stehendes Wasser mehr
- Geruch im Vorschiff deutlich reduziert

### H.6 Lessons Learned

1. Kettenkastendesign ist bei Katamaranen oft suboptimal ab Werft
2. Führungsrohr bis fast zum Boden = wichtigste Einzelmaßnahme
3. Trennwand = zweitwichtigste Maßnahme
4. Kosten gering, Wirkung enorm
5. Empfehlung: Bei jedem Katamaran den Kettenkasten prüfen und ggf. nachrüsten

**Confidence: documented** — Anonymisierter Praxisbericht, häufiges Problem bei Katamaranen.

---

## ANHANG I — AYDI-Integration (Pydantic-Modelle) {#anhang-i}

### I.1 Ankerketten-Datenmodell

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date


class ChainStandard(str, Enum):
    """Normbezeichnung der Ankerkette."""
    DIN_766 = "din_766"
    DIN_764 = "din_764"
    ISO_4565 = "iso_4565"
    G30 = "g30"
    G40_BBB = "g40_bbb"
    G43 = "g43"
    G70 = "g70"
    G80 = "g80"
    UNKNOWN = "unknown"


class ChainMaterial(str, Enum):
    """Werkstoff der Ankerkette."""
    GALVANIZED_STEEL = "galvanized_steel"
    STAINLESS_316L = "stainless_316l"
    STAINLESS_304 = "stainless_304"
    DUPLEX_2205 = "duplex_2205"
    COATED = "coated"
    UNKNOWN = "unknown"


class GalvanizingCondition(str, Enum):
    """Zustand der Verzinkung."""
    NEW = "new"                          # >90% intakt
    GOOD = "good"                        # 70-90% intakt
    MODERATE = "moderate"                # 50-70% intakt
    POOR = "poor"                        # 30-50% intakt
    CRITICAL = "critical"                # <30% intakt
    NOT_APPLICABLE = "not_applicable"    # Edelstahl/unbeschichtet


class ChainDefectType(str, Enum):
    """Typ des Kettendefekts (Fehlerbild-Atlas)."""
    CORROSION_PITTING = "corrosion_pitting"
    ELONGATED_LINKS = "elongated_links"
    WORN_GALVANIZING = "worn_galvanizing"
    STUCK_LINKS = "stuck_links"
    WINDLASS_JUMP = "windlass_jump"
    TWISTED_PILE = "twisted_pile"
    CONNECTOR_FAILURE = "connector_failure"
    ANTIFOULING_CONTAMINATION = "antifouling_contamination"
    ELECTROLYSIS_DAMAGE = "electrolysis_damage"
    MARKING_LOST = "marking_lost"
    RODE_CONNECTION_FAILURE = "rode_connection_failure"
    LOCKER_DRAINAGE_BLOCKED = "locker_drainage_blocked"


class AnchorChainSpec(BaseModel):
    """Technische Spezifikation einer Ankerkette."""
    model_config = {"from_attributes": True}

    diameter_mm: float = Field(
        ...,
        ge=4.0, le=22.0,
        description="Nenn-Durchmesser der Kette in mm"
    )
    standard: ChainStandard = Field(
        ...,
        description="Normbezeichnung (DIN 766, G40 etc.)"
    )
    material: ChainMaterial = Field(
        default=ChainMaterial.GALVANIZED_STEEL,
        description="Werkstoff der Kette"
    )
    length_m: float = Field(
        ...,
        ge=5.0, le=300.0,
        description="Gesamtlänge der Kette in Metern"
    )
    weight_per_m_kg: Optional[float] = Field(
        default=None,
        ge=0.1, le=20.0,
        description="Gewicht pro Meter in kg"
    )
    breaking_load_kn: Optional[float] = Field(
        default=None,
        ge=1.0, le=500.0,
        description="Bruchlast in kN"
    )
    wll_kn: Optional[float] = Field(
        default=None,
        ge=0.5, le=125.0,
        description="Working Load Limit in kN"
    )
    pitch_mm: Optional[float] = Field(
        default=None,
        ge=10.0, le=100.0,
        description="Teilung (Pitch) in mm"
    )
    inner_width_mm: Optional[float] = Field(
        default=None,
        ge=5.0, le=50.0,
        description="Innenweite des Gliedes in mm"
    )
    calibrated: bool = Field(
        default=True,
        description="Kette ist kalibriert (für Windlass)"
    )
    short_link: bool = Field(
        default=True,
        description="Kurzgliedkette (True) oder Langglied (False)"
    )
    stud_link: bool = Field(
        default=False,
        description="Stegkette (True) oder Stegloskette (False)"
    )
    manufacturer: Optional[str] = Field(
        default=None,
        description="Hersteller der Kette"
    )
    purchase_date: Optional[date] = Field(
        default=None,
        description="Kaufdatum"
    )
    last_reglavanized: Optional[date] = Field(
        default=None,
        description="Datum der letzten Re-Galvanisierung"
    )


class ChainConditionAssessment(BaseModel):
    """Zustandsbewertung einer Ankerkette."""
    model_config = {"from_attributes": True}

    chain_spec: AnchorChainSpec = Field(
        ...,
        description="Technische Spezifikation der bewerteten Kette"
    )
    galvanizing_condition: GalvanizingCondition = Field(
        ...,
        description="Zustand der Verzinkung"
    )
    galvanizing_percent_intact: Optional[float] = Field(
        default=None,
        ge=0.0, le=100.0,
        description="Prozent intakte Verzinkung (geschätzt)"
    )
    galvanizing_thickness_um: Optional[float] = Field(
        default=None,
        ge=0.0, le=200.0,
        description="Gemessene Zinkschichtdicke in µm"
    )
    max_elongation_percent: Optional[float] = Field(
        default=None,
        ge=0.0, le=50.0,
        description="Maximale gemessene Gliedlängung in %"
    )
    max_pitting_depth_mm: Optional[float] = Field(
        default=None,
        ge=0.0, le=5.0,
        description="Maximale Pitting-Tiefe in mm"
    )
    defects: list[ChainDefectType] = Field(
        default_factory=list,
        description="Liste erkannter Defekte"
    )
    overall_score: float = Field(
        ...,
        ge=0.0, le=100.0,
        description="Gesamtbewertung 0-100"
    )
    recommendation: str = Field(
        ...,
        description="Empfehlung (deutsch)"
    )
    remaining_life_years: Optional[float] = Field(
        default=None,
        ge=0.0, le=30.0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    confidence: str = Field(
        ...,
        description="Confidence-Level der Bewertung"
    )
    assessment_date: date = Field(
        ...,
        description="Datum der Bewertung"
    )
    notes: Optional[str] = Field(
        default=None,
        description="Zusätzliche Anmerkungen"
    )


class ChainDimensioningRequest(BaseModel):
    """Anfrage zur Kettendimensionierung."""
    model_config = {"from_attributes": True}

    boat_length_m: float = Field(
        ...,
        ge=4.0, le=40.0,
        description="Bootslänge über alles in Metern"
    )
    displacement_kg: float = Field(
        ...,
        ge=500, le=200_000,
        description="Verdrängung in kg"
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp (sailboat, motorboat, catamaran)"
    )
    sailing_area: str = Field(
        ...,
        description="Fahrtengebiet (coastal, offshore, bluewater)"
    )
    max_anchor_depth_m: float = Field(
        default=15.0,
        ge=1.0, le=100.0,
        description="Maximale geplante Ankertiefe in Metern"
    )
    bow_height_m: float = Field(
        default=1.5,
        ge=0.3, le=5.0,
        description="Höhe der Bugrolle über Wasser in Metern"
    )
    windlass_power_w: Optional[int] = Field(
        default=None,
        ge=200, le=5000,
        description="Leistung der Ankerwinch in Watt"
    )
    windlass_model: Optional[str] = Field(
        default=None,
        description="Modell der Ankerwinch"
    )
    prefer_all_chain: bool = Field(
        default=True,
        description="Bevorzugt Ganzkette (True) oder Mixed Rode (False)"
    )
    budget_eur: Optional[float] = Field(
        default=None,
        ge=100, le=20_000,
        description="Budget in EUR"
    )


class ChainDimensioningResult(BaseModel):
    """Ergebnis der Kettendimensionierung."""
    model_config = {"from_attributes": True}

    recommended_diameter_mm: float = Field(
        ...,
        description="Empfohlener Kettendurchmesser in mm"
    )
    minimum_diameter_mm: float = Field(
        ...,
        description="Minimaler akzeptabler Durchmesser in mm"
    )
    recommended_standard: ChainStandard = Field(
        ...,
        description="Empfohlene Norm"
    )
    recommended_length_m: float = Field(
        ...,
        description="Empfohlene Kettenlänge in Metern"
    )
    minimum_length_m: float = Field(
        ...,
        description="Minimale Kettenlänge in Metern"
    )
    scope_normal: float = Field(
        ...,
        description="Empfohlener Scope für Normalbedingungen"
    )
    scope_storm: float = Field(
        ...,
        description="Empfohlener Scope für Sturm"
    )
    total_weight_kg: float = Field(
        ...,
        description="Gesamtgewicht der empfohlenen Kette in kg"
    )
    estimated_cost_eur: float = Field(
        ...,
        description="Geschätzte Kosten in EUR"
    )
    windlass_compatible: bool = Field(
        ...,
        description="Kompatibel mit vorhandenem Windlass"
    )
    windlass_upgrade_needed: bool = Field(
        ...,
        description="Windlass-Upgrade erforderlich"
    )
    mixed_rode_alternative: Optional[dict] = Field(
        default=None,
        description="Alternative Mixed-Rode-Konfiguration"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen und Hinweise (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="Confidence-Level"
    )


class ChainScopeCalculation(BaseModel):
    """Scope-Berechnung für eine Ankerung."""
    model_config = {"from_attributes": True}

    water_depth_m: float = Field(
        ..., ge=0.5, le=100.0,
        description="Wassertiefe in Metern"
    )
    tidal_range_m: float = Field(
        default=0.0, ge=0.0, le=15.0,
        description="Tidenhub in Metern"
    )
    bow_height_m: float = Field(
        ..., ge=0.3, le=5.0,
        description="Bughöhe über Wasser in Metern"
    )
    chain_length_available_m: float = Field(
        ..., ge=5.0, le=300.0,
        description="Verfügbare Kettenlänge in Metern"
    )
    wind_speed_kn: float = Field(
        default=15.0, ge=0.0, le=100.0,
        description="Erwartete Windgeschwindigkeit in Knoten"
    )
    all_chain: bool = Field(
        default=True,
        description="Ganzkette (True) oder Mixed Rode (False)"
    )

    # Berechnete Felder (nicht in der Eingabe)
    max_depth_m: Optional[float] = Field(
        default=None,
        description="Maximale Wassertiefe (inkl. Tidenhub)"
    )
    total_depth_plus_bow_m: Optional[float] = Field(
        default=None,
        description="Gesamttiefe + Bughöhe"
    )
    recommended_scope: Optional[float] = Field(
        default=None,
        description="Empfohlener Scope"
    )
    required_rode_m: Optional[float] = Field(
        default=None,
        description="Benötigte Rode-Länge in Metern"
    )
    rode_sufficient: Optional[bool] = Field(
        default=None,
        description="Rode-Länge ausreichend"
    )
    swing_radius_m: Optional[float] = Field(
        default=None,
        description="Schwoikreis-Radius in Metern"
    )


class ChainDefectAssessment(BaseModel):
    """Einzelne Defekt-Bewertung aus dem Fehlerbild-Atlas."""
    model_config = {"from_attributes": True}

    defect_type: ChainDefectType = Field(
        ...,
        description="Typ des Defekts"
    )
    severity: str = Field(
        ...,
        description="Schweregrad (low, medium, high, critical)"
    )
    location_description: str = Field(
        ...,
        description="Beschreibung der Position (deutsch)"
    )
    affected_length_m: Optional[float] = Field(
        default=None,
        ge=0.0,
        description="Betroffene Kettenlänge in Metern"
    )
    recommendation: str = Field(
        ...,
        description="Empfohlene Maßnahme (deutsch)"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        default=None,
        ge=0.0,
        description="Geschätzte Reparaturkosten in EUR"
    )
    urgency: str = Field(
        ...,
        description="Dringlichkeit (immediate, this_season, next_season, monitor)"
    )
    confidence: str = Field(
        ...,
        description="Confidence-Level der Bewertung"
    )


class WindlassCompatibility(BaseModel):
    """Windlass-Ketten-Kompatibilitätsprüfung."""
    model_config = {"from_attributes": True}

    windlass_manufacturer: str = Field(
        ...,
        description="Hersteller der Ankerwinch"
    )
    windlass_model: str = Field(
        ...,
        description="Modell der Ankerwinch"
    )
    windlass_power_w: int = Field(
        ...,
        ge=200, le=5000,
        description="Leistung in Watt"
    )
    chain_diameter_mm: float = Field(
        ...,
        ge=4.0, le=22.0,
        description="Kettendurchmesser in mm"
    )
    chain_standard: ChainStandard = Field(
        ...,
        description="Kettenstandard"
    )
    gypsy_available: bool = Field(
        ...,
        description="Passende Kettennuss verfügbar"
    )
    gypsy_installed: bool = Field(
        ...,
        description="Passende Kettennuss installiert"
    )
    power_sufficient: bool = Field(
        ...,
        description="Motorleistung ausreichend für Kette + Anker"
    )
    max_chain_length_m: float = Field(
        ...,
        description="Maximale empfohlene Kettenlänge für diesen Windlass"
    )
    compatible: bool = Field(
        ...,
        description="Gesamtkompatibilität"
    )
    notes: Optional[str] = Field(
        default=None,
        description="Zusätzliche Hinweise (deutsch)"
    )
```

### I.2 Confidence-Mapping für Ankerketten-Analyse

```python
CHAIN_CONFIDENCE_MAPPING = {
    # Structured Analysis (Pipeline A)
    "chain_spec_from_database": "measured",
    "chain_spec_from_user_input": "estimated",
    "dimensioning_calculation": "calculated",
    "scope_calculation": "calculated",
    "windlass_compatibility_db": "measured",
    "windlass_compatibility_estimated": "estimated",
    "cost_estimation": "estimated",
    "weight_calculation": "calculated",

    # Visual Analysis (Pipeline B)
    "galvanizing_visual_clear": "visual_high",
    "galvanizing_visual_moderate": "visual_medium",
    "galvanizing_visual_poor": "visual_low",
    "defect_visual_clear": "visual_high",
    "defect_visual_ambiguous": "visual_medium",
    "chain_type_visual": "visual_low",
    "chain_diameter_visual": "visual_low",

    # Text Analysis (Pipeline C)
    "defect_from_report": "documented",
    "maintenance_from_log": "documented",
    "age_from_receipt": "measured",
}
```

### I.3 Bewertungsschema

```python
CHAIN_SCORING_WEIGHTS = {
    "galvanizing_condition": 0.30,     # Verzinkungszustand
    "mechanical_condition": 0.25,      # Mechanischer Zustand (Längung, Pitting)
    "dimensioning_adequacy": 0.20,     # Korrekte Dimensionierung
    "windlass_compatibility": 0.10,    # Windlass-Kompatibilität
    "marking_system": 0.05,            # Markierungssystem
    "connection_quality": 0.05,        # Verbindungen (Wirbel, Schäkel)
    "bitter_end": 0.03,                # Bitter-End-Befestigung
    "chain_locker": 0.02,             # Kettenkastenzustand
}

CHAIN_SEVERITY_THRESHOLDS = {
    "critical": 30,      # Score < 30: Sofortiger Handlungsbedarf
    "warning": 50,       # Score < 50: Handlung in dieser Saison
    "attention": 70,     # Score < 70: Aufmerksamkeit, Plan erstellen
    "good": 85,          # Score < 85: Guter Zustand, normal warten
    "excellent": 100,    # Score >= 85: Sehr guter Zustand
}
```

### I.4 AYDI-Analyse-Funktionen

```python
def calculate_chain_recommendation(
    boat_length_m: float,
    displacement_kg: float,
    sailing_area: str,
) -> dict:
    """
    Berechnet die empfohlene Kettendimensionierung basierend auf
    Bootslänge, Verdrängung und Fahrtengebiet.

    Returns:
        dict mit recommended_diameter_mm, recommended_length_m,
        recommended_standard, estimated_cost_eur
    """
    # Durchmesser-Empfehlung basierend auf Bootslänge
    if boat_length_m <= 8:
        diameter = 6.0
    elif boat_length_m <= 12:
        diameter = 8.0
    elif boat_length_m <= 16:
        diameter = 10.0
    elif boat_length_m <= 22:
        diameter = 12.0
    elif boat_length_m <= 26:
        diameter = 13.0
    else:
        diameter = 14.0

    # Verdrängungskorrektur: schwere Boote eine Nummer größer
    displacement_threshold = {
        6.0: 3000, 8.0: 10000, 10.0: 22000,
        12.0: 45000, 13.0: 70000, 14.0: 100000,
    }
    if displacement_kg > displacement_threshold.get(diameter, 100000):
        diameter = min(diameter + 2, 14.0)

    # Längen-Empfehlung basierend auf Fahrtengebiet
    length_ranges = {
        "coastal": (40, 60),
        "offshore": (60, 80),
        "bluewater": (80, 120),
    }
    min_length, max_length = length_ranges.get(sailing_area, (50, 70))
    # Größere Boote brauchen tendenziell mehr Kette
    length_factor = min(boat_length_m / 12.0, 1.5)
    recommended_length = min_length + (max_length - min_length) * length_factor
    recommended_length = round(recommended_length / 10) * 10  # Auf 10m runden

    # Gewicht berechnen
    weight_per_m = {
        6.0: 0.79, 8.0: 1.40, 10.0: 2.20,
        12.0: 3.15, 13.0: 3.70, 14.0: 4.30,
    }
    total_weight = weight_per_m.get(diameter, 2.20) * recommended_length

    # Kosten schätzen (Standard verzinkt)
    cost_per_m = {
        6.0: 4.50, 8.0: 6.50, 10.0: 10.00,
        12.0: 14.00, 13.0: 17.00, 14.0: 20.00,
    }
    estimated_cost = cost_per_m.get(diameter, 10.00) * recommended_length

    return {
        "recommended_diameter_mm": diameter,
        "minimum_diameter_mm": max(diameter - 2, 6.0),
        "recommended_standard": "din_766",
        "recommended_length_m": recommended_length,
        "minimum_length_m": min_length,
        "total_weight_kg": round(total_weight, 1),
        "estimated_cost_eur": round(estimated_cost, 0),
        "confidence": "calculated",
    }


def calculate_scope(
    water_depth_m: float,
    tidal_range_m: float,
    bow_height_m: float,
    wind_speed_kn: float,
    all_chain: bool = True,
) -> dict:
    """
    Berechnet den empfohlenen Scope und die benötigte Rode-Länge.

    Returns:
        dict mit recommended_scope, required_rode_m, swing_radius_m
    """
    max_depth = water_depth_m + tidal_range_m
    total_depth = max_depth + bow_height_m

    # Scope basierend auf Windstärke
    if wind_speed_kn <= 10:
        scope = 3.0
    elif wind_speed_kn <= 20:
        scope = 5.0
    elif wind_speed_kn <= 30:
        scope = 7.0
    elif wind_speed_kn <= 40:
        scope = 8.0
    else:
        scope = 10.0

    # Mixed Rode: Scope erhöhen
    if not all_chain:
        scope += 1.0

    required_rode = total_depth * scope
    swing_radius = required_rode + 5.0  # ca. Bootslänge/2 als Puffer

    return {
        "max_depth_m": round(max_depth, 1),
        "total_depth_plus_bow_m": round(total_depth, 1),
        "recommended_scope": scope,
        "required_rode_m": round(required_rode, 1),
        "swing_radius_m": round(swing_radius, 1),
        "confidence": "calculated",
    }


def assess_galvanizing_condition(
    percent_intact: float,
    thickness_um: float | None = None,
    chain_age_years: float | None = None,
) -> dict:
    """
    Bewertet den Zustand der Verzinkung.

    Returns:
        dict mit condition, score, recommendation, remaining_life_years
    """
    if percent_intact > 90:
        condition = "new"
        score = 95.0
        recommendation = "Verzinkung in ausgezeichnetem Zustand. Keine Maßnahme nötig."
        remaining = 7.0
    elif percent_intact > 70:
        condition = "good"
        score = 80.0
        recommendation = "Verzinkung in gutem Zustand. Re-Galvanisierung in 3-5 Jahren planen."
        remaining = 5.0
    elif percent_intact > 50:
        condition = "moderate"
        score = 55.0
        recommendation = "Verzinkung mäßig. Re-Galvanisierung in 1-2 Saisons empfohlen."
        remaining = 2.0
    elif percent_intact > 30:
        condition = "poor"
        score = 30.0
        recommendation = "Verzinkung schlecht. Re-Galvanisierung diese Saison dringend empfohlen."
        remaining = 0.5
    else:
        condition = "critical"
        score = 10.0
        recommendation = "Verzinkung kritisch. Sofortige Re-Galvanisierung oder Austausch erforderlich."
        remaining = 0.0

    # Schichtdickenmessung verfeinert die Bewertung
    if thickness_um is not None:
        if thickness_um > 60:
            score = min(score + 10, 100)
            remaining += 2.0
        elif thickness_um < 20:
            score = max(score - 15, 0)
            remaining = max(remaining - 1.0, 0)

    return {
        "condition": condition,
        "score": round(score, 1),
        "recommendation": recommendation,
        "remaining_life_years": round(remaining, 1),
        "confidence": "estimated" if thickness_um is None else "measured",
    }
```

### I.5 Visuelle Analyse-Prompts

```python
CHAIN_VISUAL_ANALYSIS_PROMPTS = {
    "galvanizing_assessment": """
    Analysiere das Foto einer Ankerkette und bewerte den Verzinkungszustand:

    1. Schätze den Prozentsatz der intakten Verzinkung (silber/grau-matte Fläche)
    2. Identifiziere Rostflecken (braun/orange) und deren Ausdehnung
    3. Bewerte, ob Pitting (Lochfraß) sichtbar ist
    4. Prüfe auf blanke Stahlstellen
    5. Bewerte die Gleichmäßigkeit der Verzinkung

    Antworte auf Deutsch mit:
    - galvanizing_percent_intact: (0-100)
    - condition: (new/good/moderate/poor/critical)
    - visible_defects: [Liste]
    - confidence: (visual_high/visual_medium/visual_low/visual_insufficient)
    - recommendation: Empfehlung auf Deutsch

    Wenn das Foto nicht ausreicht für eine Bewertung, sage "nicht beurteilbar"
    und setze confidence auf "visual_insufficient".
    """,

    "chain_type_identification": """
    Analysiere das Foto und identifiziere den Kettentyp:

    1. Kurzglied oder Langglied?
    2. Kalibriert (gleichmäßige Glieder) oder unkalibriert?
    3. Geschätzter Durchmesser (anhand von Referenzobjekten im Bild)
    4. Material: verzinkter Stahl, Edelstahl, beschichtet?
    5. Stegkette oder Stegloskette?

    Antworte auf Deutsch mit:
    - chain_type: (short_link/long_link)
    - calibrated: (ja/nein/unklar)
    - estimated_diameter_mm: (Zahl oder null)
    - material: (galvanized_steel/stainless/coated/unknown)
    - stud_link: (ja/nein)
    - confidence: (visual_high/visual_medium/visual_low)

    Wenn kein Referenzobjekt im Bild ist, kann der Durchmesser
    nicht geschätzt werden — setze estimated_diameter_mm auf null.
    """,

    "defect_detection": """
    Analysiere das Foto einer Ankerkette auf Defekte:

    Prüfe auf folgende Fehlerbilder:
    1. Korrosion/Lochfraß (Pitting)
    2. Gelängte Glieder (ovale statt runde Form)
    3. Abgenutzte Verzinkung
    4. Festsitzende/verklemmte Glieder
    5. Verdrehte Kette
    6. Konnektorversagen (offene Schäkel, fehlende Sicherung)
    7. Antifouling-Kontamination
    8. Elektrolyse-Schäden

    Antworte auf Deutsch mit:
    - detected_defects: [Liste der erkannten Defekte]
    - severity: (low/medium/high/critical) pro Defekt
    - location: Beschreibung der Position
    - recommendation: Empfehlung pro Defekt
    - confidence: (visual_high/visual_medium/visual_low)
    - overall_assessment: Gesamteinschätzung auf Deutsch

    Sage "nicht beurteilbar" wenn das Foto nicht ausreicht.
    """,
}
```

---

*Ende der Wissensdatei 17.02 — Ankerketten — Güten, Dimensionierung und Pflege*
*AYDI Maritime Knowledge Base v2.0 — Stand: 2026-04*
*Confidence: measured (Normen, Herstellerdaten) + documented (Praxisberichte, Fachliteratur) + estimated (Marktpreise, Erfahrungswerte)*
