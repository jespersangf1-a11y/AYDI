# 22_09 — Beleuchtung an Bord: Navigationslichter, Innenbeleuchtung, LED-Umrüstung, Unterwasserbeleuchtung

---

## Metadaten

| Feld | Wert |
|------|------|
| Kategorie | 22 — Elektrik & Elektronik |
| Unterkategorie | 09 — Beleuchtung an Bord |
| Version | 1.0.0 |
| Letzte Aktualisierung | 2026-05-07 |
| Autor | AYDI Knowledge Engine |
| Sprache | Deutsch (Fachtext) / Englisch (Code) |
| Zielgruppe | Yachtkonstrukteure, Elektroplaner, Surveyor, AYDI-Analysemodul |
| Normenstand | COLREG 1972/2003 (Regel 20–31), BSH-Zulassungsvorschriften, ISO 16180 (2013), ISO 12216 (2020), IEC 60598-2-7, ABYC E-11 (2022), DIN EN 14744 |
| Konfidenz-Profil | measured / calculated / benchmark / documented |

---

## INHALTSVERZEICHNIS

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#11-anhang-a-h--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-i-r--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Beleuchtung als Sicherheits- und Komfortsystem

Die Beleuchtung an Bord einer Yacht erfüllt zwei fundamental unterschiedliche Aufgaben: Sie ist einerseits ein sicherheitskritisches System zur Vermeidung von Kollisionen auf See (Navigationslichter), andererseits ein komfortbestimmendes Element für den Aufenthalt an Bord (Innenbeleuchtung, Cockpitbeleuchtung, Unterwasserbeleuchtung). Beide Funktionsbereiche unterliegen unterschiedlichen Regelwerken, Normen und Designanforderungen.

**Sicherheitsrelevanz der Navigationsbeleuchtung:**
Ein Ausfall der Navigationslichter auf See ist ein meldepflichtiger Vorfall und kann strafrechtliche Konsequenzen haben. Die korrekte Lichterführung nach den Internationalen Regeln zur Verhütung von Zusammenstößen auf See (COLREG, Convention on the International Regulations for Preventing Collisions at Sea, 1972, Änderungen bis 2003) ist eine der grundlegendsten Pflichten jedes Schiffsführers. Fehlerhafte oder nicht normkonforme Navigationslichter sind eine der häufigsten Beanstandungen bei Schiffskontrollen und Surveyor-Prüfungen.

**Komfortrelevanz der Innenbeleuchtung:**
Die Innenbeleuchtung bestimmt maßgeblich das Raumgefühl, die Nutzbarkeit und den emotionalen Eindruck einer Yacht. Eine professionelle Lichtplanung berücksichtigt Farbtemperatur, Lichtausbeute, Dimmbarkeit, Energieverbrauch und die spezifischen Anforderungen einzelner Zonen (Pantry: Arbeitslicht, Kabine: Ruhelicht, Salon: Stimmungslicht, Steuerstand: Nachtsichttauglich).

#### Historische Entwicklung der Bordbeleuchtung

| Epoche | Technologie | Merkmale |
|--------|-------------|----------|
| Vor 1880 | Petroleumlaternen | Offen, brandgefährlich, rußend, geringe Reichweite |
| 1880–1950 | Elektrische Glühlampen | Erste genormte Navigationslichter, hoher Stromverbrauch |
| 1950–1990 | Halogenlampen | Höhere Lichtausbeute, kompaktere Bauform |
| 1990–2005 | Xenon/HID-Suchscheinwerfer | Extrem hell, aber teuer und empfindlich |
| 2005–2015 | LED-Einzug | Erste LED-Navigationslichter, Retrofit-Leuchtmittel |
| 2015–heute | LED-Dominanz | LED-Standard für alle Anwendungen, RGB/RGBW, intelligente Steuerung |
| 2020–heute | Intelligente Systeme | CAN-Bus-Integration, Fernsteuerung, adaptive Lichtszenen |

#### Aktuelle Herausforderungen

| Herausforderung | Auswirkung | Lösungsansatz |
|----------------|------------|---------------|
| BSH-Zulassung für LED | Nicht jede LED-Leuchte ist zugelassen | Nur BSH-zugelassene Navigationslichter verwenden |
| EMV-Probleme bei LED | Interferenz mit UKW, AIS, GPS | EMV-geprüfte Leuchten, geschirmte Kabel |
| Dimmer-Kompatibilität | Flackern bei PWM-Dimmung | LED-taugliche Dimmer, Mindestlast beachten |
| Farbwiedergabe | Schlechte CRI bei günstigen LEDs | CRI >90 für Innenbeleuchtung spezifizieren |
| Unterwasserbeleuchtung | Korrosion, Durchbrüche, Dichtigkeitsprobleme | Marine-grade Materialien, professionelle Montage |
| Energiemanagement | Viele einzelne Verbraucher | Zentrale Lichtsteuerung, Gruppenabschaltung |
| Retrofitprobleme | Halogen-Dimmer ungeeignet für LED | Komplettumrüstung empfohlen |

**Confidence:** documented — basierend auf BSH-Zulassungsverzeichnis, COLREG-Textausgabe und Herstellerangaben.

### 1.2 Regelwerke und Normen im Überblick

Die Beleuchtung an Bord unterliegt einer Vielzahl von Regelwerken, die je nach Anwendungsbereich (Navigationslichter vs. Innenbeleuchtung) und Fahrtgebiet (international, europäisch, national) unterschiedlich sind.

#### Navigationslichter — Vorschriften

| Regelwerk | Geltungsbereich | Kern-Anforderung |
|-----------|----------------|-------------------|
| COLREG Regel 20–31 | International, alle Seefahrzeuge | Lichterführung nach Fahrzeugtyp, -größe, -status |
| BSH-Zulassung (Deutschland) | Sportboote unter deutscher Flagge | Navigationslichter müssen BSH-Bauartgenehmigung haben |
| USCG 33 CFR 183 | US-Gewässer | USCG-Zulassung für Navigationslichter |
| ISO 16180:2013 | International | Anforderungen an elektrische Navigationslichter |
| DIN EN 14744 | Europa | Prüfverfahren für Navigationslichter |
| RheinSchPV | Rhein, Binnenschifffahrt | Abweichende Lichterführung auf Binnengewässern |
| BinSchStrO | Deutsche Binnenwasserstraßen | Spezifische Anforderungen für Binnenschifffahrt |

#### Innenbeleuchtung — Normen

| Norm | Anwendung | Relevanz |
|------|-----------|----------|
| IEC 60598-2-7 | Leuchten — Besondere Anforderungen: Tragbare Leuchten Gärten | Salzwasserbeständigkeit |
| ABYC E-11 | AC und DC elektrische Systeme auf Booten | Kabelquerschnitte, Absicherung für Beleuchtungskreise |
| ISO 10133 | Elektrische Niederspannungsinstallationen DC | Anschlussstandards |
| ISO 13297 | Elektrische Installationen AC | Lichtkreise 230V |
| EN 12464-1 | Beleuchtung von Arbeitsstätten (Indoor) | Mindest-Beleuchtungsstärken (Referenzwert) |
| IEC 62471 | Photobiologische Sicherheit | Blaulichtemission von LEDs |

### 1.3 Energiebilanz der Beleuchtung nach Yachtklasse

Die Beleuchtung ist auf modernen Yachten einer der größeren Verbraucher, besonders wenn noch Halogen-Leuchtmittel eingesetzt werden. Die LED-Umrüstung bietet das beste Verhältnis von Aufwand zu Einsparung im gesamten Bordnetz.

| Yachtklasse | Anzahl Leuchten | Halogen-Verbrauch (W) | LED-Verbrauch (W) | Einsparung |
|-------------|----------------|----------------------|-------------------|------------|
| Weekender 7–9m | 6–10 | 120–200 | 15–30 | 85% |
| Coastal Cruiser 10–12m | 12–20 | 200–400 | 30–60 | 85% |
| Fahrtenyacht 12–15m | 20–35 | 400–700 | 60–120 | 83% |
| Blauwasser Mono 13–16m | 25–40 | 500–800 | 75–140 | 82% |
| Katamaran 38–45ft | 30–50 | 600–1.000 | 90–170 | 83% |
| Motoryacht 12–18m | 30–60 | 600–1.200 | 90–200 | 83% |
| Superyacht 20m+ | 80–200+ | 2.000–8.000 | 300–1.500 | 82% |

**Beispielrechnung Fahrtenyacht 14m (Abendnutzung 5h):**
```
HALOGEN-BESTAND:
  Navigationslichter:           3 × 25W = 75W × 8h = 600 Wh
  Salon:                        8 × 20W = 160W × 3h = 480 Wh
  Pantry:                       3 × 20W = 60W × 2h = 120 Wh
  Kabinen:                      6 × 10W = 60W × 2h = 120 Wh
  Cockpit:                      4 × 10W = 40W × 3h = 120 Wh
  Leselampen:                   2 × 20W = 40W × 2h = 80 Wh
  ─────────────────────────────────────────────────────────
  GESAMT pro Nacht:                                1.520 Wh
  Bei 12V:                                         126,7 Ah

NACH LED-UMRÜSTUNG:
  Navigationslichter:           3 × 3W = 9W × 8h = 72 Wh
  Salon:                        8 × 3W = 24W × 3h = 72 Wh
  Pantry:                       3 × 4W = 12W × 2h = 24 Wh
  Kabinen:                      6 × 2W = 12W × 2h = 24 Wh
  Cockpit:                      4 × 2W = 8W × 3h = 24 Wh
  Leselampen:                   2 × 3W = 6W × 2h = 12 Wh
  ─────────────────────────────────────────────────────────
  GESAMT pro Nacht:                                228 Wh
  Bei 12V:                                         19,0 Ah
  EINSPARUNG:                                      85%
```

**Confidence:** calculated — basierend auf typischen Leuchtmittel-Leistungsdaten und Nutzungsprofilen.

### 1.4 COLREG-Grundlagen: Warum Lichterführung überlebenswichtig ist

Die COLREG-Lichterführungsregeln existieren, weil auf See das Erkennen anderer Fahrzeuge bei Nacht und eingeschränkter Sicht ausschließlich über Lichter erfolgt. Die korrekte Lichterführung informiert andere Schiffsführer über:

1. **Fahrzeugart** — Segelfahrzeug, Maschinenfahrzeug, Fischer, manövrierunfähig etc.
2. **Fahrtrichtung** — Seitenlaternen (rot: Backbord, grün: Steuerbord)
3. **Größe** — Anzahl und Anordnung der Lichter
4. **Status** — In Fahrt, vor Anker, aufgestoppt, manövrierbehindert

Ein einzelnes Navigationslicht mit falschem Sichtwinkel oder falscher Farbe kann eine Fehlinterpretation auslösen, die zu einer Kollision führt. Die Regeln sind daher nicht optional, sondern sicherheitskritisch.

**Merksatz:** Navigationsbeleuchtung ist kein Komfort — sie ist aktiver Kollisionsschutz.

**Confidence:** documented — basierend auf COLREG 1972/2003 Originaltexte, BSH-Auslegungshinweise.

---

## 2. Grundlagen und Theorie

### 2.1 COLREG Regel 20–31 — Lichterführung im Detail

Die Internationalen Regeln zur Verhütung von Zusammenstößen auf See (COLREG, International Maritime Organization, 1972, zuletzt geändert 2003) definieren in den Regeln 20 bis 31 die Lichterführungspflichten. Diese Regeln sind für alle Fahrzeuge auf See verbindlich.

#### Regel 20 — Anwendung

Lichterführungsregeln gelten:
- Von Sonnenuntergang bis Sonnenaufgang
- Bei verminderter Sicht auch tagsüber
- Es dürfen keine anderen Lichter gezeigt werden, die mit den vorgeschriebenen verwechselt werden können
- Die Lichter müssen in ihrer technischen Ausführung den Anforderungen der Anlage I entsprechen

#### Regel 21 — Begriffsbestimmungen

| Licht | Definition | Sichtwinkel | Farbe |
|-------|-----------|-------------|-------|
| Topplicht (Masthead light) | Über der Längsachse, nach vorn | 225° (112,5° je Seite) | Weiß |
| Seitenlaterne Steuerbord | Rechte Seite | 112,5° | Grün |
| Seitenlaterne Backbord | Linke Seite | 112,5° | Rot |
| Hecklicht (Stern light) | Möglichst achtern | 135° | Weiß |
| Schlepplicht (Towing light) | Wie Hecklicht | 135° | Gelb |
| Rundumlicht (All-round light) | Über den ganzen Horizont | 360° | Je nach Zweck |
| Funkellicht (Flashing light) | 120+ Blitze/Minute | 360° | Je nach Zweck |

#### Regel 22 — Mindesttragweite der Lichter

| Fahrzeuglänge | Topplicht | Seitenlaterne | Hecklicht | Rundumlicht (weiß) |
|---------------|-----------|---------------|-----------|---------------------|
| < 12 m | 2 sm (wenn vorhanden) | 1 sm | 2 sm | 2 sm |
| 12–20 m | 3 sm | 2 sm | 2 sm | 2 sm |
| 20–50 m | 5 sm | 2 sm | 2 sm | 2 sm |
| ≥ 50 m | 6 sm | 3 sm | 3 sm | 3 sm |

**sm = Seemeilen (nautical miles)**

**Berechnung der Lichtstärke aus Tragweite:**

Die erforderliche Lichtstärke (Candela) für eine gegebene Tragweite wird nach folgender Formel berechnet (COLREG Anlage I, Abschnitt 8):

```
I = 3,43 × 10⁶ × T × D² × K^(-D)

wobei:
  I = Lichtstärke in Candela (cd)
  T = Schwellenwert (2 × 10⁻⁷ lux für Navigationslichter)
  D = Tragweite in Seemeilen
  K = atmosphärischer Transmissionskoeffizient (0,8 für Normalatmosphäre)
```

**Ergebnis-Tabelle:**

| Tragweite (sm) | Erforderliche Lichtstärke (cd) | Typische LED-Leistung |
|----------------|-------------------------------|----------------------|
| 1 | 0,9 | < 0,5 W |
| 2 | 4,3 | 0,5–1 W |
| 3 | 12 | 1–2 W |
| 5 | 52 | 3–5 W |
| 6 | 94 | 5–10 W |

**Confidence:** measured — basierend auf COLREG Anlage I, mathematische Ableitung.

#### Regel 23 — Maschinenfahrzeuge in Fahrt

Ein Maschinenfahrzeug in Fahrt muss führen:

```
FAHRZEUG < 12m:
  Option A:  1 Topplicht + Seitenlichter + Hecklicht
  Option B:  1 Rundumlicht (weiß) + Seitenlichter
  Option C:  1 Rundumlicht (weiß) + Seitenlichter (wenn praktikabel) (< 7m, Geschwindigkeit < 7 kn)

FAHRZEUG 12–50m:
  1 Topplicht (vorn) + Seitenlichter + Hecklicht
  Optional: 2. Topplicht (achtern, höher als vorderes)

FAHRZEUG ≥ 50m:
  2 Topplichter (vorn + achtern, achtern höher) + Seitenlichter + Hecklicht
```

#### Regel 25 — Segelfahrzeuge in Fahrt und Fahrzeuge unter Ruder

```
SEGELFAHRZEUG (beliebige Größe):
  Seitenlichter + Hecklicht
  KEIN Topplicht (dieses ist Maschinenfahrzeugen vorbehalten)

OPTIONAL (Segler < 20m):
  Dreifarbenlaterne am Mast (Rot + Grün + Weiß in einem Gehäuse)
  ACHTUNG: Nicht gleichzeitig mit getrennten Seitenlichtern und Hecklicht!

OPTIONAL (Segler beliebig):
  2 Rundumlichter übereinander am Mast: oben Rot, unten Grün
  (zusätzlich zu Seitenlichtern und Hecklicht)

SEGLER MIT MOTOR:
  Gilt als Maschinenfahrzeug → Topplicht + Seitenlichter + Hecklicht

RUDERBOOT / PADDLER:
  Weißes Licht (Laterne) bei Bedarf zeigen
```

#### Regel 26 — Fischereifahrzeuge

```
TRAWLER (Schleppnetz):
  2 Rundumlichter übereinander: oben Grün, unten Weiß
  + Topplicht (achterlicher und höher)
  + Seitenlichter + Hecklicht (wenn in Fahrt)

ANDERE FISCHER:
  2 Rundumlichter übereinander: oben Rot, unten Weiß
  + Seitenlichter + Hecklicht (wenn in Fahrt)
  Fanggerät ausliegend > 150m: Rundumlicht weiß in Richtung Gerät
```

#### Regel 27 — Manövrierunfähige und manövrierbehinderte Fahrzeuge

```
MANÖVRIERUNFÄHIG:
  2 rote Rundumlichter übereinander (senkrecht)
  + Seitenlichter + Hecklicht (wenn Fahrt durchs Wasser)

MANÖVRIERBEHINDERT:
  3 Rundumlichter übereinander: Rot-Weiß-Rot (senkrecht)
  + Seitenlichter + Hecklicht + Topplichter (wenn in Fahrt)
```

#### Regel 30 — Vor Anker liegende und aufgelaufene Fahrzeuge

```
VOR ANKER (< 50m):
  1 weißes Rundumlicht im Vorschiff (wo am besten sichtbar)

VOR ANKER (≥ 50m):
  2 weiße Rundumlichter: vorn (höher) + achtern (niedriger)
  + Decksbeleuchtung

AUFGELAUFEN (auf Grund):
  Ankerlichter + 2 rote Rundumlichter übereinander (senkrecht)
```

#### Regel 31 — Wasserflugzeuge

Wasserflugzeuge führen Lichter soweit wie möglich ähnlich den Regelungen für Wasserfahrzeuge.

**Confidence:** documented — direkte Wiedergabe der COLREG-Systematik.

### 2.2 BSH-Zulassung für Navigationslichter

Das Bundesamt für Seeschifffahrt und Hydrographie (BSH) in Hamburg ist die zuständige Behörde für die Bauartgenehmigung von Navigationslichtern auf Fahrzeugen unter deutscher Flagge.

#### Anforderungen für die BSH-Zulassung

1. **Lichtstärkeverteilung:** Die Lichtstärke muss in allen geforderten Richtungen die COLREG-Mindestanforderungen erfüllen
2. **Sichtwinkel:** Exakte Einhaltung der geforderten Winkelbereiche (±1°)
3. **Farbwerte:** Chromatizitätskoordinaten müssen innerhalb der CIE-Normfarbbereiche liegen
4. **Umweltbeständigkeit:** Salzsprühnebeltest (ISO 9227), Vibration, Temperaturzyklus -25°C bis +55°C
5. **Elektrische Sicherheit:** Überspannungsschutz, EMV-Kompatibilität
6. **Kennzeichnung:** BSH-Zulassungsnummer auf jeder Leuchte sichtbar

#### BSH-Zulassungskategorien

| Kategorie | Fahrzeugtyp | Kennzeichen |
|-----------|------------|-------------|
| Kat. A | Fahrzeuge ≥ 50m | Höchste Lichtstärke |
| Kat. B | Fahrzeuge 20–50m | Mittlere Lichtstärke |
| Kat. C | Fahrzeuge 12–20m | Standard-Sportboot |
| Kat. D | Fahrzeuge < 12m | Reduzierte Anforderungen |

#### BSH-Zulassungsnummer

Format: `BSH/[Jahreszahl]/[Nummer]/[Suffix]`

Beispiel: `BSH/4711/120/1` — Die Nummer ist auf der Leuchte eingeprägt oder auf einem Schild angebracht. Ohne diese Nummer ist eine Navigationsleuchte in deutschen Gewässern nicht zulässig.

**Prüfstelle:** BSH prüft selbst oder akzeptiert Berichte akkreditierter Prüflabore (z.B. DNV, Bureau Veritas, Lloyd's).

**Wichtig:** Eine CE-Kennzeichnung ersetzt NICHT die BSH-Zulassung. CE betrifft die allgemeine Produktsicherheit, BSH die spezifische Eignung als Navigationslicht.

**Confidence:** documented — basierend auf BSH-Zulassungsverfahren, Stand 2025.

### 2.3 LED vs. Halogen vs. Glühlampe — Technologievergleich

#### Funktionsprinzip

**Glühlampe (Incandescent):**
Ein Wolframfaden wird durch elektrischen Strom auf ~2.700 K erhitzt und emittiert Licht durch Wärmestrahlung. Nur ~5% der Energie wird in sichtbares Licht umgewandelt, 95% ist Wärme.

**Halogenlampe:**
Wie Glühlampe, aber mit Halogenfüllung (Iod oder Brom). Der Halogenkreisprozess transportiert verdampftes Wolfram zurück auf den Faden, was höhere Temperatur (~3.000 K), bessere Lichtausbeute und längere Lebensdauer ermöglicht.

**LED (Light Emitting Diode):**
Halbleiterbauelement, das durch Elektrolumineszenz Licht erzeugt. Ein Halbleiterkristall (typisch GaN — Galliumnitrid für blaues Licht, mit Phosphorschicht für Weißkonversion) emittiert Photonen bei Anlegen einer Spannung. Wirkungsgrad 30–50% (elektrisch → Licht).

#### Vergleichstabelle

| Parameter | Glühlampe | Halogen | LED |
|-----------|-----------|---------|-----|
| Lichtausbeute (lm/W) | 8–15 | 15–25 | 80–180 |
| Farbtemperatur (K) | 2.400–2.700 | 2.800–3.200 | 2.700–6.500 (wählbar) |
| CRI (Farbwiedergabe) | 100 | 100 | 70–98 (qualitätsabhängig) |
| Lebensdauer (h) | 1.000–2.000 | 2.000–4.000 | 30.000–60.000 |
| Stromverbrauch (10W equiv.) | 10 W | 7 W | 1–2 W |
| Einschaltverhalten | Sofort, warm-up ~0,5s | Sofort | Sofort, kein warm-up |
| Dimmbarkeit | Hervorragend (analog) | Hervorragend (analog) | PWM/CCR (spezieller Dimmer) |
| Vibrationsfestigkeit | Schlecht (Faden) | Mittel (Faden) | Hervorragend (Festkörper) |
| Wärmeentwicklung | Sehr hoch (95% Wärme) | Hoch (85% Wärme) | Niedrig (50–70% Wärme) |
| UV-Emission | Gering | Gering | Keine (praktisch) |
| Insektenanziehung | Hoch (UV+IR) | Hoch | Gering (warm-weiß) |
| Schockempfindlichkeit | Hoch | Mittel | Sehr gering |
| Kosten (Leuchtmittel) | Sehr niedrig | Niedrig | Mittel–Hoch |
| Kosten (Lifecycle 10 Jahre) | Hoch (Ersatz+Strom) | Mittel | Niedrig |
| Marine-Eignung | Historisch standard | Gut, bewährt | Hervorragend |

**Confidence:** measured — physikalische Kennwerte aus Herstellerdatenblättern und IEC-Normen.

### 2.4 Photometrische Grundlagen: Lumen, Lux, Candela

Für die professionelle Lichtplanung an Bord sind die photometrischen Grundgrößen essentiell.

#### Lumen (lm) — Lichtstrom

Der Lichtstrom beschreibt die gesamte von einer Lichtquelle in alle Richtungen abgegebene sichtbare Lichtleistung, gewichtet nach der Empfindlichkeit des menschlichen Auges (V(λ)-Kurve, Maximum bei 555 nm).

```
1 Lumen = 1 Candela × 1 Steradiant (sr)
Eine Lichtquelle mit 1 cd Gleichmäßigkeit in alle Richtungen: 4π × 1 cd ≈ 12,57 lm
```

**Typische Werte an Bord:**
| Leuchtmittel | Lichtstrom |
|-------------|------------|
| G4 Halogen 10W | 120 lm |
| G4 Halogen 20W | 300 lm |
| LED-Retrofit G4 2W | 180–220 lm |
| LED-Downlight 3W | 250–350 lm |
| LED-Streifenlicht 1m 5W | 400–600 lm |
| Navigationslaterne LED 3W | 40–100 lm (gerichtet) |
| Unterwasserscheinwerfer 20W | 2.000–3.000 lm |

#### Candela (cd) — Lichtstärke

Die Lichtstärke beschreibt die Lichtmenge pro Raumwinkeleinheit in eine bestimmte Richtung. Sie ist die relevante Größe für Navigationslichter, da dort die gerichtete Sichtbarkeit zählt.

```
1 Candela = 1 Lumen pro Steradiant

Für Navigationslichter gilt:
  I_min = f(Tragweite, Atmosphäre)
  Beispiel: 2 sm Tragweite → min. 4,3 cd
```

#### Lux (lx) — Beleuchtungsstärke

Die Beleuchtungsstärke beschreibt den Lichtstrom, der auf eine Fläche auftrifft.

```
1 Lux = 1 Lumen pro Quadratmeter

Beleuchtungsstärke nimmt mit dem Quadrat der Entfernung ab:
  E = I / d²
  (E in lx, I in cd, d in Metern)
```

**Empfohlene Beleuchtungsstärken an Bord:**

| Zone | Aufgabe | Empfohlen (lx) | Minimum (lx) |
|------|---------|----------------|--------------|
| Steuerstand | Navigation, Instrumente | 50–100 | 30 |
| Kartentisch | Karten lesen, Logbuch | 200–500 | 150 |
| Pantry | Kochen, Schneiden | 300–500 | 200 |
| Salon | Allgemeinbeleuchtung | 150–300 | 100 |
| Salon | Lesen, Arbeiten | 300–500 | 200 |
| Kabine | Allgemeinbeleuchtung | 100–200 | 50 |
| Kabine | Schlafen (Nachtlicht) | 5–15 | 1 |
| Kopf/WC | Allgemeinbeleuchtung | 150–300 | 100 |
| Maschinenraum | Wartung, Inspektion | 200–500 | 150 |
| Cockpit | Abendnutzung | 50–150 | 30 |
| Cockpit | Nachtfahrt (minimal) | 5–20 | 0 (Nachtsicht!) |
| Ankerkasten | Inspektion | 100–200 | 50 |
| Lazarett | Zugriff | 100–200 | 50 |

**Confidence:** benchmark — angelehnt an EN 12464-1, adaptiert für den Marinebereich.

### 2.5 Farbtemperatur und Farbwiedergabe

#### Farbtemperatur (Kelvin)

Die Farbtemperatur beschreibt den Farbeindruck einer Lichtquelle, definiert als die Temperatur eines idealen Schwarzen Strahlers (Planck'scher Strahler), der Licht mit vergleichbarer spektraler Zusammensetzung emittiert.

| Farbtemperatur | Bezeichnung | Wirkung | Marine-Einsatz |
|----------------|-------------|---------|----------------|
| 2.200–2.400 K | Extra warmweiß | Gemütlich, romantisch | Kabinen-Stimmungslicht |
| 2.700–3.000 K | Warmweiß | Behaglich, wohnlich | Standard-Kabinenbeleuchtung |
| 3.500–4.000 K | Neutralweiß | Sachlich, konzentriert | Pantry, Kartentisch |
| 4.000–5.000 K | Kaltweiß | Aktivierend, technisch | Maschinenraum, Werkstatt |
| 5.500–6.500 K | Tageslichtweiß | Tageslichtähnlich | Selten sinnvoll an Bord |

**Empfehlung für Yachten:**
- **Wohnbereiche:** 2.700–3.000 K (warmweiß) — wirkt einladend und beruhigend
- **Arbeitsbereiche:** 3.500–4.000 K (neutralweiß) — gute Konzentration und Farbbeurteilung
- **Dual-Color-LEDs:** Einstellbar zwischen warm (Abend) und neutral (Arbeit) — ideale Lösung
- **Maschinenraum:** 4.000–5.000 K — technische Umgebung, gute Fehlerkennung

#### Farbwiedergabeindex (CRI / Ra)

Der CRI (Color Rendering Index) oder Ra-Wert beschreibt, wie natürlich Farben unter einer Lichtquelle erscheinen, verglichen mit Referenzlicht (Sonnenlicht/Glühlampe = CRI 100).

| CRI-Bereich | Qualität | Einsatz |
|-------------|----------|---------|
| 95–100 | Hervorragend | Premium-Salon, Pantry (Lebensmittelbeurteilung) |
| 90–95 | Sehr gut | Standard-Kabinenbeleuchtung |
| 80–90 | Gut | Funktionsbereiche, Cockpit |
| 70–80 | Ausreichend | Maschinenraum, Stauräume |
| < 70 | Schlecht | Nicht empfohlen für bewohnte Bereiche |

**Marine-Anforderung:** CRI ≥ 90 für Wohnbereiche, CRI ≥ 80 für Funktionsbereiche. Günstige LED-Streifen haben oft nur CRI 70 — in der Pantry inakzeptabel (Lebensmittel sehen unnatürlich aus).

**Confidence:** measured — basierend auf CIE-Definitionen und Herstellerdatenblättern.

### 2.6 Dimmung von LED-Beleuchtung

Die Dimmung von LED-Leuchtmitteln an Bord ist ein häufiges Problemfeld, da konventionelle Dimmer (für Glüh-/Halogenlampen konzipiert) mit LEDs nicht kompatibel sind.

#### Dimm-Verfahren

**PWM-Dimmung (Pulse Width Modulation):**
Die LED wird mit voller Spannung betrieben, aber mit hoher Frequenz (typisch 200 Hz – 25 kHz) ein- und ausgeschaltet. Das Verhältnis von Ein- zu Aus-Zeit (Duty Cycle) bestimmt die wahrgenommene Helligkeit.

```
Duty Cycle 100% = volle Helligkeit
Duty Cycle 50%  = halbe Helligkeit (wahrgenommen)
Duty Cycle 10%  = stark gedimmt
Duty Cycle 0%   = aus
```

- **Vorteil:** Farbtemperatur bleibt konstant, gleichmäßige Dimmung
- **Nachteil:** Bei niedriger Frequenz (<500 Hz) sichtbares Flackern, EMV-Störungen möglich
- **Marine-Frequenz:** Min. 1 kHz empfohlen, besser 10+ kHz

**CCR-Dimmung (Constant Current Reduction):**
Der Strom durch die LED wird stufenlos reduziert. Die LED leuchtet immer, aber schwächer.

- **Vorteil:** Kein Flackern, keine EMV-Probleme
- **Nachteil:** Farbtemperatur verschiebt sich bei niedrigem Strom (wärmer), teurer
- **Marine-Eignung:** Hervorragend, insbesondere für Navigationsumgebungen

#### Dimmer-Kompatibilität

| Dimmer-Typ | Glüh/Halogen | LED | Problem mit LED |
|-----------|-------------|-----|-----------------|
| Phasenanschnitt (Triac, Leading Edge) | Ja | Bedingt | Flackern, Brummen, Mindestlast |
| Phasenabschnitt (Trailing Edge) | Ja | Besser | Einige LEDs flackern bei <20% |
| PWM-Dimmer (LED-spezifisch) | Nein | Ja | Keine, wenn Frequenz >1 kHz |
| 0–10V / 1–10V analog | Nein | Ja (mit Treiber) | Zusätzliche Steuerleitung nötig |
| DALI (Digital) | Nein | Ja (mit Treiber) | Teuer, Overkill für kleine Yachten |
| Touch-Dimmer (kapazitiv) | Bedingt | Bedingt | Feuchtigkeitsprobleme an Bord |

**Marine-Empfehlung:**
- PWM-Dimmer mit min. 1 kHz Frequenz (Hella Marine, Imtra-Produkte)
- Separate LED-Dimmer pro Kreis, nicht mit Navigationslichtern teilen
- Mindestlast des Dimmers beachten: viele benötigen 10–25W Mindestlast
- Bei Umrüstung: Halogen-Dimmer immer durch LED-Dimmer ersetzen

**Confidence:** measured/documented — basierend auf Herstellerangaben und Praxiserfahrungen.

### 2.7 Rotlicht und Nachtsichterhaltung

#### Das Problem der Nachtblindheit

Das menschliche Auge benötigt 20–30 Minuten, um sich vollständig an die Dunkelheit anzupassen (Dunkeladaption). Dabei erweitern sich die Pupillen und das lichtempfindliche Rhodopsin (Sehpurpur) in den Stäbchenzellen regeneriert sich. Eine einzige kurze Exposition gegenüber Weißlicht (auch nur wenige Sekunden) zerstört die Dunkeladaption und erfordert erneut 20–30 Minuten zur Regeneration.

#### Warum Rotlicht?

Die Stäbchenzellen (Nachtsicht) des menschlichen Auges sind gegenüber langwelligem rotem Licht (> 620 nm) nahezu unempfindlich. Rotlicht ermöglicht daher:

- Karten und Instrumente ablesen, ohne die Dunkeladaption zu verlieren
- Orientierung unter Deck, ohne die Wache an Deck zu blenden
- Bewegung im Cockpit, ohne die Nachtsicht anderer Crewmitglieder zu stören

#### Anforderungen an Marine-Rotlicht

| Parameter | Anforderung | Grund |
|-----------|-------------|-------|
| Wellenlänge | > 620 nm, ideal 640–660 nm | Unterhalb 620 nm beginnt Rhodopsin-Zerstörung |
| Intensität | Gerade ausreichend (< 1 lx) | Jede überflüssige Helligkeit stört |
| Gleichmäßigkeit | Diffus, nicht punktförmig | Blendfreie Ausleuchtung |
| Schaltbarkeit | Schnell umschaltbar (Weiß → Rot) | Kein Griff zum Dimmer im Notfall |
| Abschirmung | Kein Streulicht nach außen | Cockpitlicht darf nicht auf See sichtbar sein |

#### Dual-Color-LED-Lösungen

Moderne Marine-LED-Leuchten bieten Weiß/Rot-Umschaltung in einem Gehäuse:

| Hersteller | Produkt | Weißlicht | Rotlicht | Schaltung |
|-----------|---------|-----------|----------|-----------|
| Hella Marine | EuroLED 75 Dual | 2.900 K, 4W, 200 lm | 640 nm, <1W | Tastendruck |
| Imtra | Qualifies Dual | 3.000 K, 3W, 180 lm | 650 nm, <1W | Polwendung |
| Lopolight | 400-203 | 3.000 K, 2W | 640 nm, 0,5W | Zweidraht |
| ITC Marine | Compass G2 | 2.700 K, 3W, 210 lm | 645 nm, 0,8W | Digitalschalter |

**Einbauhinweis:** Rotlicht-Modus muss UNABHÄNGIG von der regulären Beleuchtung schaltbar sein. Im Notfall muss die gesamte Innenbeleuchtung auf Rot umschaltbar sein, ohne dass der Rudergänger von der Position abgehen muss.

**Confidence:** documented — basierend auf augenphysiologischen Grundlagen und Marine-Beleuchtungspraxis.

### 2.8 Stromverbrauch-Vergleich und Energiebilanz

#### Verbrauchsvergleich typischer Leuchtmittel

| Typ | Lichtstrom (lm) | Leistung (W) | Strom @12V (A) | Strom @24V (A) | Ah/10h @12V |
|-----|-----------------|-------------|----------------|----------------|-------------|
| Glühlampe Bajonett 25W | 250 | 25 | 2,08 | 1,04 | 20,8 |
| Halogen G4 10W | 120 | 10 | 0,83 | 0,42 | 8,3 |
| Halogen G4 20W | 300 | 20 | 1,67 | 0,83 | 16,7 |
| Festoon 42mm 10W | 100 | 10 | 0,83 | 0,42 | 8,3 |
| LED G4 2W (180 lm) | 180 | 2 | 0,17 | 0,08 | 1,7 |
| LED G4 3W (300 lm) | 300 | 3 | 0,25 | 0,13 | 2,5 |
| LED Festoon 42mm 1W | 120 | 1 | 0,08 | 0,04 | 0,8 |
| LED Downlight 3W | 280 | 3 | 0,25 | 0,13 | 2,5 |
| LED-Streifen 1m 5W | 500 | 5 | 0,42 | 0,21 | 4,2 |
| Nav-Light Halogen 25W | (gerichtet) | 25 | 2,08 | 1,04 | 20,8 |
| Nav-Light LED 3W | (gerichtet) | 3 | 0,25 | 0,13 | 2,5 |

#### Amortisationsrechnung LED-Umrüstung

```
BEISPIEL: 20 Halogen-Spots (G4 20W) → LED-Retrofit (G4 3W)

KOSTEN:
  20× LED-Leuchtmittel (marine-grade, dimm.) à 18 € = 360 €
  Arbeitszeit (DIY):                                  = 0 €
  ──────────────────────────────────────────────────────────
  Investition:                                          360 €

EINSPARUNG PRO NACHT (angenommen 5h Betrieb, 50% an):
  Halogen: 10 Spots × 20W × 5h = 1.000 Wh = 83,3 Ah @12V
  LED:     10 Spots × 3W × 5h  = 150 Wh   = 12,5 Ah @12V
  ──────────────────────────────────────────────────────────
  Einsparung:                     850 Wh/Nacht = 70,8 Ah @12V

MONETÄRE BEWERTUNG:
  Diesel-Generator: ~0,80 €/kWh (inkl. Diesel, Wartung, Abschreibung)
  Landstrom Marina: ~0,60 €/kWh
  Solar-Äquivalent: ~200 Wp zusätzlich nötig für 850 Wh → 350–600 €

  Bei 100 Nutzungsnächten/Jahr:
  Einsparung Generator: 100 × 0,85 kWh × 0,80 €/kWh = 68 €/Jahr
  Amortisation: 360 € / 68 €/Jahr ≈ 5,3 Jahre

  PLUS: Halogen-Leuchtmittel-Ersatz entfällt (15–20 €/Stück × 3–5 Ausfälle/Saison)
  Reale Amortisation inkl. Ersatzlampen: ~2–3 Jahre
```

**Confidence:** calculated — basierend auf typischen Nutzungsprofilen und Marktpreisen 2025/2026.

### 2.9 EMV-Probleme bei LED-Beleuchtung

LEDs und ihre Treiberschaltungen sind Quellen elektromagnetischer Störungen (EMI — Electromagnetic Interference), die besonders im Marineeinsatz problematisch werden können.

#### Typische Störquellen

| Quelle | Frequenzbereich | Betroffene Geräte |
|--------|----------------|-------------------|
| PWM-Dimmung (schaltend) | 1 kHz – 100 kHz + Oberwellen | UKW-Funk, SSB, AIS |
| LED-Treiber (Schaltregler) | 100 kHz – 2 MHz | GPS, WLAN, Navtex |
| LED-Streifen (günstig) | Breitband | Diverse |
| Kabelführung (ungeschirmt) | Variiert | Abhängig von Nähe zu Antennen |

#### Gegenmaßnahmen

1. **EMV-zertifizierte LED-Leuchten verwenden** (CE EMV-Richtlinie 2014/30/EU)
2. **Ferritkerne** auf Zuleitungen von LED-Installationen (min. 2 Windungen)
3. **Geschirmte Kabel** in Antennennähe (< 1m zu UKW/SSB/GPS-Kabeln)
4. **Mindestabstand** 30 cm zwischen LED-Kabeln und Antennenkabeln
5. **Nicht abschirmen:** Navigationsleuchten auf dem Mast — hier kurze Kabelwege bevorzugen
6. **Filter:** LC-Filter am LED-Treiber-Eingang (100 µH + 1.000 µF)

**Confidence:** documented — basierend auf EMV-Praxisberichten und Herstellerempfehlungen.

---

## 3. Typenübersicht

### 3.1 Navigationslichter

#### 3.1.1 Topplicht (Masthead Light)

**Funktion:** Kennzeichnung eines Maschinenfahrzeugs in Fahrt. Weißes Licht, sichtbar über einen Bogen von 225° (112,5° von recht voraus nach jeder Seite).

**Montageort:**
- Segelyachten: Am Mast, oberhalb der Seitenlaternen (wenn vorhanden)
- Motoryachten: Auf dem Mast oder Dach, möglichst hoch und in der Mittschiffsebene
- Bei 2 Topplichtern: Achteres höher als vorderes, min. 4,5m Höhendifferenz (bei >20m Schiffslänge)

**Spezifikationen nach Fahrzeuggröße:**

| Parameter | < 12m | 12–20m | 20–50m |
|-----------|-------|--------|--------|
| Mindest-Tragweite | 2 sm | 3 sm | 5 sm |
| Sichtwinkel | 225° | 225° | 225° |
| Mindesthöhe über Rumpf | 1,0 m | 2,5 m | 6,0 m |
| Min. über Seitenlaternen | — | 1,0 m | 2,0 m |
| Typische LED-Leistung | 1–3 W | 2–5 W | 5–15 W |

**Technische Anforderungen:**
- Weiße Farbe: CIE x=0,310, y=0,320 (Normweiß)
- Scharfe Sichtwinkelgrenze: Abfall auf 50% bei exakt 112,5°
- Vibrationsfest für Mastmontage (Rigg-Schwingungen, Seegang)
- Kabelzuführung durch Mast oder außen mit UV-beständiger Isolation
- Bei LED: Integrierte Überspannungsschutzdiode (TVS) empfohlen

**Confidence:** measured — basierend auf COLREG Anlage I und ISO 16180.

#### 3.1.2 Seitenlaternen (Sidelights)

**Funktion:** Kennzeichnung der Fahrtrichtung. Steuerbordlaterne GRÜN (112,5° von recht voraus nach Steuerbord), Backbordlaterne ROT (112,5° von recht voraus nach Backbord).

**Bauformen:**

| Bauform | Beschreibung | Einsatz |
|---------|-------------|---------|
| Getrennte Laternen | Einzeln an Stb/Bb montiert | Standard ab 20m |
| Zweifarbenlaterne | Rot+Grün in einem Gehäuse | Boote < 20m |
| Dreifarbenlaterne | Rot+Grün+Hecklicht am Mast | Segler < 20m unter Segel |

**Montageorte:**
- **Getrennt (Bug oder Aufbau):** Auf oder nahe dem Bugbereich, möglichst weit auseinander
- **Zweifarbenlaterne:** Mittschiffs am Bugkorb oder Bugspriet
- **Dreifarbenlaterne:** Am Masttopp (nur Segelfahrzeuge unter Segel < 20m)

**Kritische Anforderung — Trennblende:**
Bei Zweifarben-Laternen muss eine Blende die Farbsektoren scharf trennen. Kein Überlappen der Farben in der Mittschiffsachse. Bei Dreifarben-Laternen: mechanische Präzision der optischen Trennung entscheidend.

**Spezifikationen:**

| Parameter | < 12m | 12–20m | 20–50m |
|-----------|-------|--------|--------|
| Mindest-Tragweite | 1 sm | 2 sm | 2 sm |
| Sichtwinkel je Seite | 112,5° | 112,5° | 112,5° |
| Mindesthöhe über Wasser | — | 1,0 m | 1,0 m |
| Max. unter Topplicht | 3/4 Topplicht-Höhe | 3/4 Topplicht-Höhe | 3/4 Topplicht-Höhe |
| Typische LED-Leistung | 0,5–2 W | 1–3 W | 2–5 W |

**Confidence:** measured — basierend auf COLREG Anlage I.

#### 3.1.3 Hecklicht (Stern Light)

**Funktion:** Weißes Licht, möglichst achtern montiert, sichtbar über einen Bogen von 135° (67,5° von recht achteraus nach jeder Seite).

**Montageort:**
- Heckkorb, Spiegel oder Heckreling
- Möglichst weit achtern, in Mittschiffsebene
- Nicht zu tief (Wellengischt, Sprühwasser), nicht zu hoch (Verdeckung durch Bimini/Spray Hood)

**Hinweis:** Das Hecklicht ergänzt die Seitenlaternen zum vollen 360°-Bereich: Seitenlaternen 2×112,5° = 225° + Hecklicht 135° = 360°.

**Spezifikationen:**

| Parameter | < 12m | 12–20m | 20–50m |
|-----------|-------|--------|--------|
| Mindest-Tragweite | 2 sm | 2 sm | 2 sm |
| Sichtwinkel | 135° | 135° | 135° |
| Typische LED-Leistung | 0,5–1,5 W | 1–3 W | 2–5 W |

**Confidence:** measured — basierend auf COLREG Anlage I.

#### 3.1.4 Dampferlicht / Dampferlaterne

**Umgangssprache für:** Das Topplicht eines Maschinenfahrzeugs. Im Sportbootbereich wird oft das 360°-Rundumlicht als "Dampferlicht" bezeichnet, was technisch nicht korrekt ist. Der Begriff stammt aus der Zeit der Dampfschifffahrt, als das weiße Topplicht zur Kennung von maschinengetriebenen Schiffen eingeführt wurde.

**Korrekte Verwendung:**
- "Dampferlicht" = Topplicht (225°, weiß, Maschinenfahrzeug in Fahrt)
- Umgangssprachlich auch für die Kombination Topplicht + Hecklicht bei Segeln unter Motor

**Montage bei Segelbooten:**
Das Dampferlicht wird auf Segelyachten oft als separates Licht am Mast installiert und eingeschaltet, wenn unter Motor gefahren wird. Die Dreifarbenlaterne muss dann AUS sein.

```
SEGLER UNTER MOTOR:
  Dampferlicht (Topplicht am Mast) → EIN
  Seitenlaternen (Bugkorb) → EIN
  Hecklicht (Heck) → EIN
  Dreifarbenlaterne → AUS (!)

SEGLER UNTER SEGEL:
  Option A: Dreifarbenlaterne am Masttop → EIN, alle anderen → AUS
  Option B: Seitenlaternen (Bugkorb) + Hecklicht → EIN, Dampferlicht → AUS
```

**Confidence:** documented — basierend auf COLREG und Seemannschaftsliteratur.

#### 3.1.5 Ankerlicht (Ankerlaterne)

**Funktion:** Weißes Rundumlicht (360°) zur Kennzeichnung eines vor Anker liegenden Fahrzeugs. Pflicht von Sonnenuntergang bis Sonnenaufgang und bei verminderter Sicht.

**Anforderungen:**

| Parameter | < 12m | 12–50m | ≥ 50m |
|-----------|-------|--------|-------|
| Mindest-Tragweite | 2 sm | 2 sm (vorn) | 3 sm (vorn) + 3 sm (achtern) |
| Sichtwinkel | 360° | 360° | 360° (beide) |
| Montageort | Im Vorschiff, erhöht | Im Vorschiff, erhöht | Vorn + achtern |
| Ausnahme | < 7m in engem Bereich: optional | — | Decksbeleuchtung zusätzlich |

> **Hinweis (Audit-Korrektur):** Für Fahrzeuge ≥ 50 m müssen **beide** Ankerlichter (vorn und achtern) je 3 sm Tragweite besitzen. COLREG Regel 22 schreibt für weiße Rundumlichter auf Fahrzeugen ≥ 50 m einheitlich 3 sm vor — es gibt keine reduzierte Tragweite für das achtere Ankerlicht (vgl. Regel-22-Tabelle in Abschnitt 2.1). Ursprünglich stand hier „2 sm (achtern)".

**Energieverbrauch-Relevanz:**
Das Ankerlicht brennt die ganze Nacht (~10–12h). Bei Halogen-Leuchtmitteln ein signifikanter Verbraucher:

| Leuchtmittel | Leistung | Stromverbrauch 10h @12V |
|-------------|---------|------------------------|
| Glühlampe 10W | 10 W | 8,3 Ah |
| Glühlampe 25W | 25 W | 20,8 Ah |
| LED Ankerlicht | 1–2 W | 0,8–1,7 Ah |

**LED-Umrüstung des Ankerlichts:** Eine der lohnendsten Einzelmaßnahmen zur Energieeinsparung.

**Confidence:** measured/calculated — COLREG + Verbrauchsberechnung.

#### 3.1.6 Suchscheinwerfer

**Funktion:** Leistungsstarkes, schwenkbares Weißlicht zur Beleuchtung von Hindernissen, Anlegerplätzen, Personen über Bord (MOB), oder zur Zeichengebung.

**ACHTUNG:** Suchscheinwerfer dürfen NIEMALS als Navigationslichter verwendet werden und dürfen nicht so eingesetzt werden, dass sie andere Schiffsführer blenden.

**Bauformen:**

| Typ | Leistung | Reichweite | Steuerung | Marine-Eignung |
|-----|---------|-----------|-----------|----------------|
| Halogen-Handscheinwerfer | 55–100 W | 300–800 m | Handheld | Einfach, bewährt |
| Halogen fest montiert | 100–250 W | 500–1.500 m | Fernsteuerung (Joystick) | Motoryachten |
| LED-Handscheinwerfer | 20–40 W | 500–1.200 m | Handheld | Empfohlen |
| LED fest montiert | 30–80 W | 800–2.500 m | Fernsteuerung/WiFi | Standard bei Neubauten |
| Xenon (HID) | 35–75 W | 1.000–3.000 m | Fest montiert | Auslaufend |

**Montage:**
- Bugkorb (Segelboot) oder Dach/Mast (Motorboot)
- Schwenkbar min. 180° horizontal, 30° vertikal
- Kabelquerschnitt beachten (Halogen 100W @12V = 8,3A!)
- Wärmeabfuhr bei LED und Xenon: min. 50 mm Luftraum um Gehäuse

**Confidence:** documented — basierend auf Herstellerangaben und Praxisberichten.

### 3.2 Innenbeleuchtung

#### 3.2.1 Cockpit-Beleuchtung

Die Cockpitbeleuchtung ist ein Sonderfall zwischen Innen- und Außenbeleuchtung: Sie muss wetterbeständig sein, darf aber die Nachtsicht nicht stören und nach See hin nicht sichtbar sein.

**Anforderungen:**

| Anforderung | Erläuterung |
|-------------|-------------|
| IP-Schutz | Min. IP65 (spritzwassergeschützt), besser IP67 |
| Dimmbarkeit | Essentiell — von hell (Hafen) bis minimal (Nachtfahrt) |
| Rotlicht-Option | Dringend empfohlen für Nachtfahrt |
| Blendfreiheit | Indirektes Licht bevorzugt (unter Süllrand, unter Sitzbänken) |
| UV-Beständigkeit | Gehäuse und Optik müssen UV-stabil sein |
| Salzwasserbeständigkeit | 316L-Edelstahl oder Polymer-Gehäuse |
| Insektenneutralität | Warmweiß (< 3.000 K) zieht weniger Insekten an |

**Typische Installation:**

| Position | Typ | Leistung | Zweck |
|----------|-----|---------|-------|
| Unter Süllrand | LED-Streifen (warmweiß) | 3–5 W/m | Allgemeinbeleuchtung |
| Unter Sitzbänken | LED-Streifen (warmweiß) | 2–3 W/m | Stimmungslicht |
| Am Steuerstand | Spot, dimmbar, rot/weiß | 2–3 W | Instrumentenbeleuchtung |
| Cockpittisch | Spot, dimmbar | 3–5 W | Arbeits-/Esslicht |
| Einstieg/Niedergang | Spot oder Streifenlicht | 2–3 W | Sicherheit (Stufen) |
| Badeplattform | LED unter Plattform | 3–10 W | Schwimmen, Dingi |

**Confidence:** benchmark — basierend auf Marine-Lichtplanungspraxis.

#### 3.2.2 Kajüt-Beleuchtung (Salon, Kabinen, Pantry)

Die Kabinenbeleuchtung ist der zentrale Wohlfühlfaktor der Innengestaltung und beeinflusst den emotionalen Gesamteindruck einer Yacht maßgeblich.

**Beleuchtungskonzept nach Yacht-Klasse:**

| Yacht-Klasse | Konzept | Typische Leuchten |
|-------------|---------|-------------------|
| Produktions-Segelboot 8–12m | Einheitlich, Spots | 10–15 Einbau-Spots, 2–4 Leselampen |
| Semi-Custom 12–18m | Zonen-Beleuchtung | Spots + Streifen + Akzente, 3 Lichtszenen |
| Custom/Superyacht 18m+ | Professionelle Lichtplanung | Indirekt, Akzent, Arbeits-, Stimmungslicht, DALI/KNX |

**Beleuchtungszonen im Salon:**

```
SALON — Mehrstufiges Lichtkonzept:

1. ALLGEMEINBELEUCHTUNG (Grundhelligkeit)
   → Einbau-Spots (Decke), LED-Panels, Downlights
   → 150–300 lx auf Augenhöhe
   → Dimmbar, warmweiß (2.700–3.000 K)

2. AKZENTBELEUCHTUNG (Atmosphäre)
   → LED-Streifen unter Decksvorsprüngen, hinter Regalen
   → Indirektes Licht, weich, blendungsfrei
   → Stark dimmbar, warm (2.200–2.700 K)

3. ARBEITSBELEUCHTUNG (Funktional)
   → Leselampen (schwenkbar), Kartentisch-Spot
   → 300–500 lx am Arbeitsplatz
   → Neutralweiß (3.500–4.000 K), CRI > 90

4. ORIENTIERUNGSLICHT (Nacht)
   → Niedrigste Stufe, Fußbodenleuchten, Treppenstufenbeleuchtung
   → < 10 lx, warmweiß oder rot
   → Automatisch bei Dunkelheit (Dämmerungssensor)

5. NOTBELEUCHTUNG
   → Batteriebetrieben (integrierter Akku)
   → Aktivierung bei Stromausfall
   → Min. 1 lx für 3h in Fluchtwegen
```

**Confidence:** benchmark — basierend auf professioneller Marine-Innenarchitektur.

#### 3.2.3 Leselampen

**Anforderungen an Marine-Leselampen:**

| Anforderung | Spezifikation | Grund |
|-------------|---------------|-------|
| Schwenkbarkeit | 360° horizontal, 90° vertikal | Flexibler Einsatz |
| Spot-Charakter | Engstrahlend (< 30°) | Nur Lesefläche beleuchten, Partner nicht stören |
| Dimmbarkeit | Stufenlos, bis < 10% | Abendlektüre vs. Nachttisch |
| Farbtemperatur | 3.000–3.500 K | Angenehm warm, aber lesbar |
| CRI | > 90 | Text klar erkennbar |
| Schalter | Am Leuchtenkopf (Touch oder Knopf) | Erreichbar ohne Aufstehen |
| Lichtstrom | 150–300 lm | Ausreichend für Buchseite |
| Leistung | 2–5 W LED | Energieeffizient |
| Montage | Aufbau oder Einbau, stabil | Seegangsicher |

**Beliebte Modelle:**

| Hersteller | Modell | Leistung | Lichtstrom | Besonderheit |
|-----------|--------|---------|------------|--------------|
| Hella Marine | Apelo A1 | 3 W | 200 lm | Polymergehäuse, farbig |
| Imtra | Ventura PowerLED | 4 W | 260 lm | Alu, eloxiert, sehr schwenkbar |
| Cantalupi | Atlas | 3 W | 180 lm | Messing poliert, italienisches Design |
| Prebit | Leipzig | 5 W | 350 lm | Doppelgelenk, Premium |
| Quick | TB Daylight HD | 4 W | 280 lm | Touch, DIMM, 2.700/4.000 K |

**Confidence:** documented — basierend auf Herstellerkatalogen 2025/2026.

### 3.3 Unterwasserbeleuchtung

Unterwasserbeleuchtung hat sich in den letzten Jahren von einem Superyacht-Feature zum Standard auf vielen Motoryachten und zunehmend auch auf Segelbooten entwickelt.

#### Einsatzzweck

| Zweck | Erläuterung |
|-------|-------------|
| Ästhetik | Atmosphärische Beleuchtung im Ankerfeld |
| Sicherheit | Beleuchtung des Wassers um das Boot (Schwimmer, Dingi-Verkehr) |
| Fischen | Anlocken von Plankton → Kleinfisch → Raubfisch |
| Navigation | Beleuchtung des Grundes in flachem Wasser (Vorsicht!) |
| Unterhaltung | Lichtshow, Farbwechsel, Event-Beleuchtung |

#### Montagearten

| Montage | Beschreibung | Vor-/Nachteile |
|---------|-------------|----------------|
| Rumpfdurchbruch (Thru-hull) | Leuchte bündig in Rumpf eingelassen | Bester Lichtertrag, aber Durchbruch im Rumpf |
| Aufbau (Surface mount) | Auf den Rumpf aufgesetzt | Kein Durchbruch, aber Strömungswiderstand + Bewuchs |
| Transom-Montage | Am Spiegel montiert | Einfachste Installation, Beleuchtung achtern |
| Drain-Plug | In vorhandene Ablassschrauben | Retrofit ohne neuen Durchbruch |
| Schwimmkörper | An Ankerkette oder Leine | Temporär, keine Rumpfmodifikation |

#### Technische Spezifikationen

| Parameter | Einstieg | Standard | Premium |
|-----------|---------|----------|---------|
| Lichtstrom | 2.000–4.000 lm | 5.000–12.000 lm | 15.000–40.000 lm |
| Leistung | 10–20 W | 30–60 W | 80–200 W |
| Farben | Weiß oder Blau | RGBW | RGBW + Warmweiß + UV |
| Steuerung | Schalter | Dimmer + Farbwahl | App/WiFi/DMX |
| Gehäuse | Polymer, 316 SS | 316L SS, Bronze | Titan, 316L SS |
| IP-Schutz | IP68 | IP68 (20m) | IP68/IP69K (30m+) |
| Kühlung | Passiv (Wasser) | Passiv (Wasser) | Aktiv + Passiv |
| Lebensdauer | 20.000 h | 40.000 h | 60.000 h |
| Preis (pro Leuchte) | 150–400 € | 500–1.500 € | 2.000–8.000 € |

#### Rumpfdurchbruch-Montage — Sicherheitshinweise

Ein Unterwasserlicht mit Rumpfdurchbruch ist ein SEEVENTIL. Es gelten die gleichen Sicherheitsanforderungen wie für alle Durchbrüche unter der Wasserlinie:

1. **Material:** Bronze, 316L-Edelstahl, oder Titan. KEIN Messing (Entzinkung!)
2. **Dichtung:** Sika 295UV oder 3M 5200 (permanent elastisch)
3. **Seeventil:** Rückschlagventil oder Absperrmöglichkeit NICHT erforderlich (solide Montage), aber Flansch muss druckfest sein
4. **Kabelführung:** Wasserdichte Kabeldurchführung (Roxtec oder gleichwertig)
5. **Prüfung:** Dichtigkeitsprüfung nach Montage bei nächster Sliptermin-Kontrolle
6. **Bewuchsschutz:** Antifouling-Anstrich um die Leuchte, aber NICHT auf der Linse
7. **Galvanische Trennung:** Opferanode (Zink) in unmittelbarer Nähe, wenn verschiedene Metalle

**WARNUNG:** Jeder Rumpfdurchbruch unterhalb der Wasserlinie erhöht das Risiko einer Leckage. Die Entscheidung für Thru-hull-Unterwasserlichter muss bewusst getroffen werden. Surface-mount-Alternativen sind im Zweifelsfall vorzuziehen.

**Confidence:** documented — basierend auf Herstellerempfehlungen und Surveyorpraxis.

---

## 4. Produktlinien und Spezifikationen

### 4.1 Hella Marine — Navigationslichter und Innenbeleuchtung

**Hintergrund:** Hella Marine (Neuseeland) ist Marktführer bei Marine-Beleuchtung. Alle Navigationslichter sind nach internationalen Standards zugelassen (BSH, USCG, ABYC). Bekannt für das multivolt-fähige Sortiment (9–33V DC).

#### Navigationslichter — NaviLED-Serie

| Modell | Typ | Tragweite | Leistung | Spannung | BSH | Preis (ca.) |
|--------|-----|-----------|---------|----------|-----|-------------|
| NaviLED Pro 2 nm | Topplicht | 2 sm | 1,2 W | 9–33V | Ja | 65 € |
| NaviLED Pro 3 nm | Topplicht | 3 sm | 2,5 W | 9–33V | Ja | 95 € |
| NaviLED Pro 5 nm | Topplicht | 5 sm | 8 W | 9–33V | Ja | 180 € |
| NaviLED PRO Bi-Colour 2 nm | Zweifarbenlaterne | 2 sm | 1,5 W | 9–33V | Ja | 85 € |
| NaviLED PRO Tri-Colour / Anchor | Dreifarben + Anker | 2 sm | 2 W / 1 W | 9–33V | Ja | 165 € |
| NaviLED Port (rot) | Seitenlaterne Bb | 2 sm | 1 W | 9–33V | Ja | 55 € |
| NaviLED Starboard (grün) | Seitenlaterne Stb | 2 sm | 1 W | 9–33V | Ja | 55 € |
| NaviLED Stern | Hecklicht | 2 sm | 0,8 W | 9–33V | Ja | 50 € |
| NaviLED 360 Compact | Ankerlicht | 2 sm | 1 W | 9–33V | Ja | 55 € |

**Besonderheit Hella Marine NaviLED:**
- Multivolt 9–33V DC (12V und 24V kompatibel)
- Linsensystem statt Reflektor (kompakte Bauform)
- Glasverstärktes Polyamid-Gehäuse (korrosionsfrei)
- IP67 Standard
- Vibrationsfest (Mastmontage getestet)

#### Innenbeleuchtung — EuroLED-Serie

| Modell | Typ | Lichtstrom | Leistung | CRI | Besonderheit | Preis (ca.) |
|--------|-----|-----------|---------|-----|--------------|-------------|
| EuroLED 75 | Downlight Einbau | 200 lm | 4 W | > 80 | Flach, Ø 75mm | 38 € |
| EuroLED 75 Dual | Downlight Weiß/Rot | 200/40 lm | 4/0,5 W | > 80 | Weiß + Rot, Touchschalter | 52 € |
| EuroLED 95 | Downlight Einbau | 340 lm | 6 W | > 80 | Ø 95mm, Dimm | 55 € |
| EuroLED 150 | Deckenleuchte | 450 lm | 8 W | > 80 | Flach, Ø 150mm | 75 € |
| EuroLED 150 Touch | Deckenleuchte | 450 lm | 8 W | > 80 | Dual-Color, Touch | 95 € |
| Apelo A1 | Leselampe | 200 lm | 3 W | > 80 | Polymer, farbige Ringe | 35 € |
| Apelo A2 | Leselampe schwenkbar | 220 lm | 3,5 W | > 80 | Kugelgelenk | 55 € |

**Confidence:** documented — basierend auf Hella Marine Katalog 2025/2026.

### 4.2 Lopolight — Premium-Navigationslichter

**Hintergrund:** Lopolight (Dänemark) ist Spezialist für hochwertige LED-Navigationslichter, besonders im Superyacht-Segment. Bekannt für extrem lange Lebensdauer, höchste Lichtqualität und innovative Designs.

#### Navigationslichter

| Modell | Typ | Tragweite | Leistung | Spannung | BSH | Preis (ca.) |
|--------|-----|-----------|---------|----------|-----|-------------|
| 200-001 | Topplicht 2 sm | 2 sm | 2 W | 12/24V | Ja | 120 € |
| 200-010 | Topplicht 3 sm | 3 sm | 3 W | 12/24V | Ja | 180 € |
| 200-012 | Topplicht 5 sm | 5 sm | 7 W | 12/24V | Ja | 350 € |
| 200-014 | Topplicht 6 sm | 6 sm | 12 W | 12/24V | Ja | 520 € |
| 200-003 | Zweifarben 2 sm | 2 sm | 2 W | 12/24V | Ja | 150 € |
| 200-016 | Dreifarben + Anker | 2 sm | 3 W | 12/24V | Ja | 280 € |
| 200-024 | Port (rot) 2 sm | 2 sm | 1,5 W | 12/24V | Ja | 100 € |
| 200-025 | Starboard (grün) 2 sm | 2 sm | 1,5 W | 12/24V | Ja | 100 € |
| 200-020 | Hecklicht 2 sm | 2 sm | 1,5 W | 12/24V | Ja | 95 € |
| 200-012W | Ankerlicht 360° | 2 sm | 1,5 W | 12/24V | Ja | 110 € |
| 200-038 | Schlepperlicht gelb | 2 sm | 2 W | 12/24V | Ja | 130 € |

**Besonderheiten Lopolight:**
- Edelstahl 316L-Gehäuse (Standard) oder Bronze (Option)
- Lebensdauer > 50.000 h (LED-Modul)
- EMV-geprüft, keinerlei Störungen bei UKW/AIS/GPS
- Verpolungsschutz und Überspannungsschutz integriert
- CIE-konforme Farbwerte, verifiziert durch DNV

**Confidence:** documented — basierend auf Lopolight Produktkatalog 2025.

### 4.3 Aqua Signal — Navigationslichter (Serie 40, 43, 55)

**Hintergrund:** Aqua Signal (Deutschland, gehört zu Hella Marine Group) ist einer der traditionsreichsten Hersteller von Navigationslichtern. Besonders im europäischen Markt weit verbreitet. Bekannt für das breite Sortiment vom Kleinstboot bis zur Berufsschifffahrt.

#### Serie 40 (Boote < 12m)

| Modell | Typ | Tragweite | Leistung | BSH | Preis (ca.) |
|--------|-----|-----------|---------|-----|-------------|
| AS40 Topplicht | Topplicht | 2 sm | 1,5 W LED | Ja | 55 € |
| AS40 Bicolour | Zweifarbenlaterne | 1 sm | 1 W LED | Ja | 65 € |
| AS40 Port/Stbd | Seitenlaternen | 1 sm | 0,8 W LED | Ja | 45 € |
| AS40 Stern | Hecklicht | 2 sm | 0,8 W LED | Ja | 42 € |
| AS40 All-round white | Ankerlicht | 2 sm | 1 W LED | Ja | 48 € |

#### Serie 43 (Boote 12–20m)

| Modell | Typ | Tragweite | Leistung | BSH | Preis (ca.) |
|--------|-----|-----------|---------|-----|-------------|
| AS43 Topplicht | Topplicht | 3 sm | 3 W LED | Ja | 85 € |
| AS43 Bicolour | Zweifarbenlaterne | 2 sm | 2 W LED | Ja | 95 € |
| AS43 Port/Stbd | Seitenlaternen | 2 sm | 1,5 W LED | Ja | 68 € |
| AS43 Stern | Hecklicht | 2 sm | 1,5 W LED | Ja | 62 € |
| AS43 Tri-colour/Anchor | Dreifarben + Anker | 2 sm | 2,5 W LED | Ja | 165 € |

#### Serie 55 (Boote 20–50m)

| Modell | Typ | Tragweite | Leistung | BSH | Preis (ca.) |
|--------|-----|-----------|---------|-----|-------------|
| AS55 Topplicht | Topplicht | 5 sm | 8 W LED | Ja | 195 € |
| AS55 Port/Stbd | Seitenlaternen | 2 sm | 3 W LED | Ja | 110 € |
| AS55 Stern | Hecklicht | 2 sm | 3 W LED | Ja | 95 € |
| AS55 All-round | Ankerlicht | 2 sm | 2 W LED | Ja | 120 € |

**Confidence:** documented — basierend auf Aqua Signal Katalog 2025/2026.

### 4.4 Perko — Navigationslichter (US-Markt)

**Hintergrund:** Perko (USA, seit 1907) ist ein traditioneller Hersteller von Marine-Hardware und Navigationslichtern. Stark im US-Markt vertreten, USCG-zugelassen. Bronze- und Chrom-Gehäuse.

#### Ausgewählte Modelle

| Modell | Typ | Tragweite | Material | Leuchtmittel | USCG | Preis (ca.) |
|--------|-----|-----------|---------|-------------|------|-------------|
| 0170 | Topplicht | 2 sm | Chrom/Messing | LED | Ja | 75 USD |
| 0170DP0CHR | Topplicht | 2 sm | Chrom | LED | Ja | 85 USD |
| 0170 Bi-Color | Zweifarben | 1 sm | Chrom/Messing | LED | Ja | 90 USD |
| 0253 All-round | Ankerlicht 360° | 2 sm | Chrom | LED | Ja | 55 USD |
| 0120 Stern | Hecklicht | 2 sm | Chrom | LED | Ja | 45 USD |
| 0163 Seitenlichter | Paar Rot/Grün | 1 sm | Chrom/Messing | LED | Ja | 120 USD (Paar) |

**Hinweis:** Perko-Leuchten haben oft USCG-Zulassung, aber NICHT immer BSH-Zulassung. Für Fahrzeuge unter deutscher Flagge muss die BSH-Zulassung separat geprüft werden.

**Confidence:** documented — basierend auf Perko Katalog 2025.

### 4.5 Lumitec — Unterwasserbeleuchtung und Decksbeleuchtung

**Hintergrund:** Lumitec (USA) ist Spezialist für marine LED-Beleuchtung, insbesondere Unterwasserbeleuchtung und Decksfluter. Bekannt für hohe Qualität und breite Produktpalette.

#### Unterwasserbeleuchtung

| Modell | Typ | Lichtstrom | Leistung | Farben | Montage | IP | Preis (ca.) |
|--------|-----|-----------|---------|--------|---------|-------|-------------|
| SeaBlaze X | Thru-hull | 3.000 lm | 30 W | RGBW | Durchbruch | IP68 | 450 USD |
| SeaBlaze X2 | Thru-hull | 6.000 lm | 60 W | RGBW | Durchbruch | IP68 | 750 USD |
| SeaBlazeX Spectrum | Thru-hull | 4.500 lm | 45 W | RGBW+UV | Durchbruch | IP68 | 650 USD |
| SeaBlaze Mini | Surface | 1.500 lm | 15 W | Weiß/Blau | Aufbau | IP68 | 250 USD |
| Mirage | Transom | 2.000 lm | 20 W | RGBW | Spiegel | IP68 | 350 USD |
| Argonaut | Thru-hull | 12.000 lm | 100 W | RGBW | Durchbruch | IP68 | 1.800 USD |

#### Decks- und Cockpitbeleuchtung

| Modell | Typ | Lichtstrom | Leistung | Besonderheit | Preis (ca.) |
|--------|-----|-----------|---------|--------------|-------------|
| TouchDome | Deckenleuchte | 420 lm | 6 W | Touch-Dimmer, IP67 | 120 USD |
| Capri2 | Downlight | 350 lm | 5 W | Dual-Color (W/B), IP67 | 95 USD |
| Poco | Einbauspot | 200 lm | 3 W | Kompakt, IP67 | 65 USD |
| Scallop | Wandleuchte | 280 lm | 4 W | Halb-Flood, IP67 | 85 USD |
| Rail2 | LED-Streifen | 800 lm/m | 12 W/m | IP67, flexibel | 55 USD/m |

**Confidence:** documented — basierend auf Lumitec Produktkatalog 2025.

### 4.6 Imtra — Marine-Beleuchtungssysteme

**Hintergrund:** Imtra (USA) ist Distributor und Eigenmarken-Hersteller von Marine-Beleuchtung. Führt eigene Marken (PowerLED, Qualifies) und importiert europäische Marken. Spezialisiert auf Yacht-Innenbeleuchtung und Lichtsteuerung.

#### Ausgewählte Produkte

| Modell | Typ | Lichtstrom | Leistung | CRI | Besonderheit | Preis (ca.) |
|--------|-----|-----------|---------|-----|--------------|-------------|
| PowerLED Downlight | Einbau Ø 65mm | 250 lm | 3 W | > 90 | 10–30V, Dimm | 65 USD |
| PowerLED Downlight Dual | Einbau Ø 65mm | 250/30 lm | 3/0,5 W | > 90 | Weiß+Rot | 85 USD |
| Qualifies Oval | Wandleuchte | 300 lm | 4 W | > 85 | IP67, Edelstahl | 95 USD |
| PowerLED Reading | Leselampe | 260 lm | 4 W | > 90 | Schwenkbar, Touch | 75 USD |
| Ventura PowerLED | Leselampe Premium | 340 lm | 5 W | > 90 | Alu eloxiert, dimm. | 120 USD |
| LED Tape (IP67) | Flexstreifen | 600 lm/m | 8 W/m | > 80 | Outdoor, 12V/24V | 45 USD/m |
| CereLight Controller | Lichtsteuerung | — | — | — | 8 Kanäle, WiFi, dimm. | 450 USD |

**Imtra CereLight System:**
Intelligente Lichtsteuerung für Yachten mit folgenden Funktionen:
- 8 dimmbare Kanäle (PWM, 12V/24V)
- WiFi-App-Steuerung (iOS/Android)
- Vorprogrammierte Lichtszenen (Tag, Abend, Nacht, Rot)
- Zeitsteuerung (Dämmerungsautomatik)
- Integrierbar mit NMEA 2000 (optional)

**Confidence:** documented — basierend auf Imtra Produktkatalog 2025/2026.

---

## 5. Hersteller-Datenbank

### 5.1 Übersicht Marine-Beleuchtungshersteller

| # | Hersteller | Land | Schwerpunkt | Segment | Website |
|---|-----------|------|------------|---------|---------|
| 1 | Hella Marine | NZ/DE | Nav-Lichter, Innen | Alle | hellamarine.com |
| 2 | Lopolight | DK | Nav-Lichter Premium | Semi-Custom + Superyacht | lopolight.com |
| 3 | Aqua Signal | DE | Nav-Lichter | Produktion + Semi-Custom | aquasignal.com |
| 4 | Perko | US | Nav-Lichter, Hardware | Produktion | perko.com |
| 5 | Lumitec | US | Unterwasser, Deck | Semi-Custom + Superyacht | lumiteclighting.com |
| 6 | Imtra | US | Innenbeleuchtung | Semi-Custom + Superyacht | imtra.com |
| 7 | Cantalupi | IT | Innenbeleuchtung Luxury | Superyacht | cantalupi.it |
| 8 | Prebit | DE | Leselampen, Premium | Superyacht | prebit.de |
| 9 | Quick Spa | IT | Innen + Unterwasser | Alle | quickitaly.com |
| 10 | OceanLED | UK | Unterwasser | Semi-Custom + Superyacht | oceanled.com |
| 11 | Lumishore | UK | Unterwasser, TIX | Semi-Custom + Superyacht | lumishore.com |
| 12 | Shadow-Caster | US | Unterwasser, Deck | Alle | shadow-caster.com |

### 5.2 Hersteller-Detailprofile

#### 5.2.1 Hella Marine

| Feld | Information |
|------|------------|
| Vollständiger Name | Hella Marine Ltd |
| Hauptsitz | Auckland, Neuseeland |
| Mutterkonzern | HELLA GmbH & Co. KGaA, Deutschland |
| Gründung | 1984 (Marine-Division) |
| Mitarbeiter (Marine) | ~150 |
| Produktionsstandorte | Neuseeland, Deutschland |
| Zertifizierungen | ISO 9001, BSH, USCG, ABYC, Lloyd's, BV |
| Produktspektrum | Navigationslichter, Innenbeleuchtung, Arbeitsscheinwerfer, Signalleuchten |
| Preissegment | Mittelklasse bis Premium |
| Stärken | Multivolt (9–33V), breites Sortiment, weltweite Verfügbarkeit |
| Vertrieb DE | Über Yachtausrüster (SVB, Toplicht, AWN, Compass) |
| Garantie | 5 Jahre auf LED-Navigationslichter |
| Support | Technischer Support über Distributor-Netzwerk |

#### 5.2.2 Lopolight

| Feld | Information |
|------|------------|
| Vollständiger Name | Lopolight ApS |
| Hauptsitz | Kopenhagen, Dänemark |
| Gründung | 2004 |
| Produktionsstandort | Dänemark |
| Zertifizierungen | BSH, USCG, DNV, Lloyd's, BV, RMRS |
| Produktspektrum | Navigationslichter (ausschließlich) |
| Preissegment | Premium bis Ultra-Premium |
| Stärken | Höchste Qualität, Edelstahlgehäuse, Superyacht-Referenzen |
| Vertrieb DE | Direktvertrieb + Fachhändler |
| Garantie | 5 Jahre |
| Referenzen | Royal Caribbean, Viking Yachts, Beneteau (Oceanis-Serie) |

#### 5.2.3 Aqua Signal

| Feld | Information |
|------|------------|
| Vollständiger Name | Aqua Signal AG (Teil der Hella Marine Group) |
| Hauptsitz | Bremen, Deutschland |
| Gründung | 1868 |
| Produktionsstandort | Deutschland |
| Zertifizierungen | BSH, USCG, GL, DNV, Lloyd's |
| Produktspektrum | Navigationslichter für Sport- und Berufsschifffahrt |
| Preissegment | Einstieg bis Mittelklasse |
| Stärken | Tradition, BSH-Zulassung Standard, gutes Preis-Leistungsverhältnis |
| Vertrieb DE | Breit über alle Marine-Fachhändler |
| Garantie | 3 Jahre |

#### 5.2.4 Lumitec

| Feld | Information |
|------|------------|
| Vollständiger Name | Lumitec LLC |
| Hauptsitz | Delray Beach, Florida, USA |
| Gründung | 2006 |
| Produktionsstandort | USA |
| Zertifizierungen | USCG (Nav-Lichter), IP68 (Unterwasser), EMV (FCC) |
| Produktspektrum | Unterwasserbeleuchtung, Decksbeleuchtung, Cockpitbeleuchtung |
| Preissegment | Mittelklasse bis Premium |
| Stärken | Innovation (TTP-Technologie), breite Unterwasser-Palette |
| Vertrieb DE | Über Importeure und Fachhandel |
| Garantie | 3 Jahre |

#### 5.2.5 Cantalupi

| Feld | Information |
|------|------------|
| Vollständiger Name | Cantalupi Lighting Srl |
| Hauptsitz | Florenz, Italien |
| Gründung | 1974 |
| Produktionsstandort | Italien |
| Zertifizierungen | CE, RINA, Lloyd's, BV |
| Produktspektrum | Premium-Innenbeleuchtung, Leselampen, Stimmungslicht |
| Preissegment | Ultra-Premium (Superyacht) |
| Stärken | Italienisches Design, handgefertigte Qualität, Custom-Fertigung |
| Vertrieb DE | Direktvertrieb an Werften, über Yacht-Lichtplaner |
| Garantie | 5 Jahre |
| Referenzen | Benetti, Azimut, Ferretti, Baglietto |

#### 5.2.6 Lumishore

| Feld | Information |
|------|------------|
| Vollständiger Name | Lumishore Ltd |
| Hauptsitz | Swansea, Wales, UK |
| Gründung | 2010 |
| Produktionsstandort | UK |
| Zertifizierungen | CE, EMV, IP68, USCG |
| Produktspektrum | Unterwasserbeleuchtung (ausschließlich) |
| Preissegment | Premium |
| Stärken | TIX-Technologie (Thru-hull Interchangeable), EOS-Steuerung, Color+ |
| Vertrieb DE | Über Fachhändler und Importeure |
| Garantie | 3 Jahre (Thru-hull), 2 Jahre (Surface) |
| Innovation | Austauschbare LED-Module ohne Slip (TIX-System) |

**Confidence:** documented — basierend auf Herstellerinformationen und Branchenverzeichnissen, Stand 2025/2026.

---

## 6. Fehlerbild-Atlas

### Fehlerbild F-BEL-01: BSH-Zulassung fehlt oder abgelaufen

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Compliance / Navigationsbeleuchtung |
| Schweregrad | KRITISCH |
| Häufigkeit | Häufig (besonders bei LED-Retrofit) |
| Erkennungsmethode | Visuelle Inspektion (Zulassungsnummer am Gehäuse), Prüfung gegen BSH-Register |
| Symptom | Keine BSH-Nummer auf der Leuchte, oder veraltete Nummer für ausgelaufene Zulassung |
| Ursache | LED-Leuchtmittel ohne BSH-Zulassung in vorhandene Halogen-Gehäuse eingesetzt; Import-Leuchten ohne deutsche Zulassung |
| Risiko | Versicherungsrechtlich: Keine Deckung bei Kollision. Ordnungsrechtlich: Bußgeld, Fahrtverbot. Sicherheit: Möglicherweise falsche Lichtstärke/Sichtwinkel |
| Behebung | Komplette Leuchte durch BSH-zugelassenes Modell ersetzen. LED-Retrofit-Leuchtmittel in Navigationsleuchten sind generell NICHT BSH-konform, auch wenn die Original-Leuchte zugelassen war |
| Sofortmaßnahme | Ersatz-Leuchte beschaffen, bis dahin Halogenleuchtmittel verwenden (wenn Original-Leuchte zugelassen) |
| AYDI-Score-Einfluss | Compliance: -40 Punkte, Sicherheit: WARNUNG |
| Prävention | Nur komplette BSH-zugelassene LED-Navigationsleuchten beschaffen |
| Confidence | documented |

### Fehlerbild F-BEL-02: Sichtwinkel fehlerhaft (Abschirmung defekt oder falsche Montage)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Sicherheit / Navigationsbeleuchtung |
| Schweregrad | KRITISCH |
| Häufigkeit | Mittel |
| Erkennungsmethode | Visuelle Prüfung (Sichtwinkel-Inspektion von See), Lichtstärkeverteilungsmessung |
| Symptom | Seitenlaternen scheinen über die Mittschiffsebene hinaus, Topplicht nicht voll 225°, Hecklicht zu weit seitlich sichtbar |
| Ursache | Falsche Montageposition, verdrehtes Gehäuse, beschädigte interne Blende, falscher Leuchtentyp für Position |
| Risiko | Kollisionsgefahr: Andere Schiffsführer können Kurs und Status nicht korrekt erkennen |
| Behebung | Montage korrigieren, Gehäuse ausrichten (Markierungen beachten), bei defekter Blende: Leuchte ersetzen |
| Sofortmaßnahme | Sichtwinkel von außen prüfen (zweite Person in Dingi), Fehlstellung dokumentieren |
| AYDI-Score-Einfluss | Compliance: -35 Punkte, Sicherheit: KRITISCH |
| Prävention | Montage nach Hersteller-Anleitung, Ausrichtung mit Winkelmesser prüfen |
| Confidence | documented |

### Fehlerbild F-BEL-03: Korrosion an Navigationsleuchten

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Material / Navigationsbeleuchtung |
| Schweregrad | MITTEL bis HOCH |
| Häufigkeit | Häufig (besonders bei Edelstahl 304 oder Messing) |
| Erkennungsmethode | Visuelle Inspektion (Rostflecken, Grünspan, Lochfraß) |
| Symptom | Verfärbungen am Gehäuse, Lochfraß, lose Schrauben, Dichtungsfehler durch Verformung |
| Ursache | Ungeeignetes Material (304 statt 316L), galvanische Korrosion (verschiedene Metalle), beschädigte Oberfläche, Salzablagerungen |
| Risiko | Undichtigkeit → Kurzschluss → Ausfall. Strukturversagen → Leuchte fällt ab. Erhöhter Übergangswiderstand → reduzierte Helligkeit |
| Behebung | Leuchte ersetzen (bei 304/Messing → 316L oder Polymer wählen), galvanische Trennung sicherstellen, Kontakte reinigen und schützen |
| Sofortmaßnahme | Kontakte reinigen, Korrosionsschutzmittel (z.B. Boeshield T-9) auftragen, Schrauben nachziehen |
| AYDI-Score-Einfluss | Material: -20 Punkte, Compliance: -10 Punkte |
| Prävention | 316L oder Polymergehäuse verwenden, regelmäßige Süßwasserspülung, Kontaktfett |
| Confidence | documented |

### Fehlerbild F-BEL-04: LED-Flackern (sichtbar oder unsichtbar)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Elektrik / Innenbeleuchtung |
| Schweregrad | NIEDRIG bis MITTEL |
| Häufigkeit | Sehr häufig (besonders bei Retrofit) |
| Erkennungsmethode | Visuelle Wahrnehmung (< 100 Hz), Smartphone-Kamera-Test (Streifenmuster bei Rollverschluss), Oszilloskop |
| Symptom | Sichtbares Flackern, Kopfschmerzen bei Langzeitexposition, Streifenmuster in Kamerabildern |
| Ursache | PWM-Frequenz zu niedrig (< 200 Hz), inkompatibler Dimmer, zu geringe Mindestlast am Dimmer, schlechter LED-Treiber |
| Risiko | Gesundheitlich: Kopfschmerzen, Übelkeit (insb. bei Seegang). EMV: Störung von Bordelektronik. Comfort: Reduzierter Wohnkomfort |
| Behebung | LED-spezifischen Dimmer verwenden (PWM > 1 kHz), Mindestlast am Dimmer sicherstellen, hochwertiges LED-Leuchtmittel verwenden |
| Sofortmaßnahme | Dimmer auf 100% stellen (kein Flackern bei Volllast), alternativ Dimmer überbrücken |
| AYDI-Score-Einfluss | Komfort: -15 Punkte, Elektrik: -10 Punkte |
| Prävention | LED-taugliche Dimmer von Beginn an einplanen, Leuchtmittel und Dimmer als System testen |
| Confidence | documented |

### Fehlerbild F-BEL-05: Dimmer-Interferenz mit Bordelektronik

| Feld | Beschreibung |
|------|-------------|
| Kategorie | EMV / Elektrik |
| Schweregrad | MITTEL bis HOCH |
| Häufigkeit | Mittel |
| Erkennungsmethode | UKW-Funk: Brummen/Rauschen beim Dimmen. GPS: Positionssprünge. AIS: Empfangslücken |
| Symptom | Störgeräusche im UKW-Funk korrelieren mit Dimmerstellung, GPS-Genauigkeit sinkt bei bestimmter Dimmstufe |
| Ursache | PWM-Dimmer erzeugt Oberwellen im UKW-Band (156–163 MHz) oder GPS-Band (1.575 MHz), insbesondere bei niedrigen PWM-Frequenzen und langen, ungeschirmten Kabeln |
| Risiko | Eingeschränkte Kommunikation auf See, fehlerhafte Navigation, AIS-Ausfall |
| Behebung | EMV-konforme LED-Dimmer verwenden, Ferritkerne auf Leitungen, geschirmte Kabel in Antennennähe, Abstand vergrößern |
| Sofortmaßnahme | Dimmer auf 100% oder 0% (keine Störung bei Extremwerten), Dimmer temporär abklemmen |
| AYDI-Score-Einfluss | Sicherheit: -25 Punkte, Compliance: -15 Punkte (EMV) |
| Prävention | EMV-Test nach Installation, Mindestabstand 30 cm zwischen LED-Kabeln und Antennenkabeln |
| Confidence | documented |

### Fehlerbild F-BEL-06: Unterwasserlicht undicht (Rumpfdurchbruch)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Sicherheit / Struktur |
| Schweregrad | KRITISCH |
| Häufigkeit | Selten, aber potenziell katastrophal |
| Erkennungsmethode | Bilge-Alarm, Wassereinbruch im Bereich des Unterwasserlichts, Beschlagen der Linse |
| Symptom | Wasser in der Bilge, Feuchtigkeitsspuren am Innengehäuse, Linse beschlagen oder mit Wasser gefüllt |
| Ursache | Dichtungsversagen (Alterung, UV), Riss im Gehäuse, Materialermüdung, falsche Dichtstoffe, Vibration |
| Risiko | Wassereinbruch → Kurzschluss → Brand / Sinken. Galvanische Korrosion durch Seewasser im Rumpf |
| Behebung | Sofort: Seeventil schließen (wenn vorhanden) oder Boot slippen. Leuchte ausbauen, Durchbruch abdichten, neue Leuchte mit korrekter Dichtung montieren |
| Sofortmaßnahme | SOFORT Lenzpumpe prüfen, Leck lokalisieren, Notstopfen bereithalten, Leuchte stromlos schalten |
| AYDI-Score-Einfluss | Sicherheit: -50 Punkte, Struktur: KRITISCH |
| Prävention | Jährliche Inspektion bei jedem Slip, Dichtung nach 5 Jahren erneuern, nur marine-grade Dichtstoffe |
| Confidence | documented |

### Fehlerbild F-BEL-07: Farbtemperatur-Mischung (uneinheitliches Licht)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Komfort / Innenbeleuchtung |
| Schweregrad | NIEDRIG |
| Häufigkeit | Sehr häufig |
| Erkennungsmethode | Visueller Eindruck (verschiedene Leuchtfarben nebeneinander), Messung mit Farbtemperatur-Messgerät |
| Symptom | Nebeneinander liegende Leuchten haben unterschiedliche Lichtfarbe (z.B. warm + kaltweiß) |
| Ursache | Verschiedene LED-Leuchtmittel verschiedener Hersteller oder Chargen, Halogen/LED-Mix, Alterung |
| Risiko | Kein Sicherheitsrisiko, aber erhebliche Komfort- und Wertminderung |
| Behebung | Alle Leuchtmittel eines Raumes durch identische Modelle (gleiche Charge!) ersetzen |
| Sofortmaßnahme | — |
| AYDI-Score-Einfluss | Emotional/Design: -10 Punkte |
| Prävention | Leuchtmittel immer als Set kaufen (gleiche Charge), Farbtemperatur dokumentieren |
| Confidence | benchmark |

### Fehlerbild F-BEL-08: LED-Streifen lösen sich (Kleber versagt)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Installation / Innenbeleuchtung |
| Schweregrad | NIEDRIG |
| Häufigkeit | Sehr häufig (insbesondere bei einfacher Klebestreifen-Montage) |
| Erkennungsmethode | Visuell — hängende LED-Streifen, sichtbare Klebespuren |
| Symptom | LED-Streifen hängen herab, lösen sich von der Montagefläche, Klebung nur noch punktuell |
| Ursache | Standard-3M-Kleber nicht für marine Umgebung geeignet (Feuchtigkeit, Temperaturwechsel, Vibration), falsche Untergrundreinigung |
| Risiko | Kurzschlussgefahr wenn Kontakte freiliegen, optischer Mangel |
| Behebung | LED-Streifen in Alu-Profilschienen montieren (mechanische Befestigung), Profil mit Edelstahlschrauben befestigen |
| Sofortmaßnahme | VHB-Tape (3M 5952) als Sofortreparatur, besser Profilmontage |
| AYDI-Score-Einfluss | Produktion: -10 Punkte |
| Prävention | Grundsätzlich Alu-Profile verwenden, niemals nur Klebeband in marine Umgebung |
| Confidence | documented |

### Fehlerbild F-BEL-09: Navigationslichter zu schwach (Tragweite nicht erreicht)

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Sicherheit / Navigationsbeleuchtung |
| Schweregrad | HOCH |
| Häufigkeit | Mittel |
| Erkennungsmethode | Vergleich mit anderen Schiffen, Entfernungsmessung bei Nacht, Lichtmessung mit Luxmeter |
| Symptom | Lichter von anderen Schiffen erst spät erkannt, Beschwerden von entgegenkommenden Schiffen |
| Ursache | Alterung der LED/Glühlampe, verschmutzte Optik (Salzfilm, Algen), Spannungsabfall in Zuleitung, falsches Leuchtmittel |
| Risiko | Kollisionsgefahr: Yacht wird erst spät oder gar nicht erkannt |
| Behebung | Optik reinigen, Spannungsabfall messen (max. 3%), Leuchtmittel prüfen/erneuern, Kabelquerschnitt prüfen |
| Sofortmaßnahme | Optik mit Süßwasser und Mikrofasertuch reinigen, Spannung an der Leuchte messen |
| AYDI-Score-Einfluss | Sicherheit: -30 Punkte, Compliance: -20 Punkte |
| Prävention | Jährliche Reinigung und Funktionskontrolle, Spannungsabfall bei Erstinstallation dokumentieren |
| Confidence | documented |

### Fehlerbild F-BEL-10: Wassereinbruch in Decksleuchten

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Installation / Außenbeleuchtung |
| Schweregrad | MITTEL |
| Häufigkeit | Häufig |
| Erkennungsmethode | Kondensat in der Leuchte sichtbar, Leuchte flackert bei Regen/Seegang |
| Symptom | Beschlagene Linse, Kondenswasser im Gehäuse, Korrosion an internen Kontakten |
| Ursache | IP-Schutzart unzureichend (IP44 statt IP67), Dichtung beschädigt/gealtert, Kabeleinführung undicht |
| Risiko | Kurzschluss, LED-Ausfall, beschleunigte Korrosion |
| Behebung | Leuchte öffnen, trocknen, Dichtung erneuern. Bei unzureichender IP-Klasse: Leuchte durch IP67+-Modell ersetzen |
| Sofortmaßnahme | Leuchte stromlos schalten, Linse vorsichtig öffnen und Wasser entfernen |
| AYDI-Score-Einfluss | Material: -15 Punkte |
| Prävention | Mindestens IP65 für Cockpit, IP67 für exponierte Positionen, IP68 für Unterwasser |
| Confidence | documented |

### Fehlerbild F-BEL-11: Unterwasserlicht verursacht galvanische Korrosion

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Material / Korrosion |
| Schweregrad | HOCH |
| Häufigkeit | Mittel (bei falscher Materialwahl) |
| Erkennungsmethode | Beschleunigte Korrosion an nahegelegenen Metallteilen (Propeller, Ruderblatt, Durchbrüche) |
| Symptom | Starker Zinkanodenverbrauch, Lochfraß an Propeller, Blistering um Unterwasserlicht |
| Ursache | Unterwasserlicht-Gehäuse (Edelstahl) + Rumpfbeschläge (Bronze/Aluminium) = galvanisches Element |
| Risiko | Beschleunigte Zerstörung weniger edler Metalle (Propeller, Rumpfbeschläge) |
| Behebung | Galvanische Isolierung des Unterwasserlichts, korrekte Zinkanoden-Dimensionierung, Materialgleichheit anstreben |
| Sofortmaßnahme | Zusätzliche Zinkanode in Nähe des Unterwasserlichts anbringen |
| AYDI-Score-Einfluss | Material: -25 Punkte, Struktur: -10 Punkte |
| Prävention | Materialpaarung vor Installation prüfen, galvanische Reihe beachten, Isolationsmontage |
| Confidence | documented |

### Fehlerbild F-BEL-12: Nachtsicht-Störung durch falsche Cockpitbeleuchtung

| Feld | Beschreibung |
|------|-------------|
| Kategorie | Sicherheit / Cockpitbeleuchtung |
| Schweregrad | MITTEL bis HOCH |
| Häufigkeit | Sehr häufig |
| Erkennungsmethode | Rudergänger berichtet über gestörte Dunkeladaption, Schwierigkeiten beim Erkennen anderer Lichter |
| Symptom | Nach dem Hantieren unter Deck oder im beleuchteten Cockpit dauert es 20–30 Minuten, bis volle Nachtsicht zurückkehrt |
| Ursache | Weißlicht im Cockpit bei Nachtfahrt, zu helle Instrumentenbeleuchtung, Streulicht aus dem Niedergang |
| Risiko | Eingeschränkte Fähigkeit, andere Schiffe, Tonnen und Hindernisse zu erkennen |
| Behebung | Rotlicht-Modus für Cockpit und Niedergang installieren, Instrumentenbeleuchtung dimmbar machen, Niedergangs-Vorhang/Jalousie |
| Sofortmaßnahme | Alle Weißlichter im Cockpitbereich ausschalten, nur Rotlicht verwenden |
| AYDI-Score-Einfluss | Sicherheit: -20 Punkte, Ergonomie: -15 Punkte |
| Prävention | Dual-Color-Leuchten (Weiß/Rot) in allen Cockpit- und Niedergangsbereichen vorsehen |
| Confidence | documented |

---

## 7. Troubleshooting-Entscheidungsbäume

### Entscheidungsbaum TB-BEL-01: Navigationslichter funktionieren nicht

```
START: Navigationslichter funktionieren nicht
│
├─ Prüfe: Alle Navigationslichter aus oder nur einzelne?
│   │
│   ├─ ALLE AUS:
│   │   │
│   │   ├─ Prüfe: Sicherung/Schutzschalter für Nav-Lichter-Kreis
│   │   │   │
│   │   │   ├─ Sicherung ausgelöst/durchgebrannt:
│   │   │   │   ├─ Kurzschluss suchen (Isolationsmessung an jedem Lichtkreis)
│   │   │   │   ├─ Kabelführung prüfen (Scheuerstellen, Wassereintritt)
│   │   │   │   ├─ Gefundenen Fehler beheben
│   │   │   │   └─ Sicherung ersetzen (GLEICHER Wert!)
│   │   │   │
│   │   │   └─ Sicherung OK:
│   │   │       ├─ Spannung am Schalter prüfen (Ein-/Ausgang)
│   │   │       │   ├─ Keine Spannung am Eingang: Kabel zum Panel defekt
│   │   │       │   ├─ Spannung am Eingang, nicht am Ausgang: Schalter defekt
│   │   │       │   └─ Spannung am Ausgang: Kabel zu Leuchten prüfen
│   │   │       └─ Spannung an Leuchte prüfen (12V/24V ±10%)
│   │   │           ├─ Keine Spannung: Kabelbruch, Steckverbindung lose
│   │   │           └─ Spannung OK: Alle Leuchtmittel gleichzeitig defekt (unwahrscheinlich → prüfe Masse)
│   │   │
│   │   └─ Prüfe: Masse/Erdung am gemeinsamen Rückleiter
│   │       ├─ Massekabel lose oder korrodiert: Reinigen, nachziehen
│   │       └─ Massekabel OK: Verteilerblock/Sammelschiene prüfen
│   │
│   └─ EINZELNE AUS:
│       │
│       ├─ Prüfe: Leuchtmittel der betroffenen Leuchte
│       │   ├─ Halogen/Glühlampe: Fadensichtprüfung, Ersatzlampe einsetzen
│       │   └─ LED: Spannung direkt an der Leuchte messen
│       │       ├─ Spannung OK, LED leuchtet nicht: LED-Modul defekt → Leuchte ersetzen
│       │       └─ Spannung nicht OK: Kabel/Steckverbindung zur Leuchte prüfen
│       │
│       ├─ Prüfe: Steckverbindungen im Kabelweg
│       │   ├─ Korrosion an Steckern: Reinigen, Kontaktspray, ggf. ersetzen
│       │   └─ Wasser in Steckverbindung: Trocknen, abdichten, Schrumpfschlauch
│       │
│       └─ Prüfe: Kabelzustand im Mast (bei Mast-Leuchten)
│           ├─ Kabel gescheuert: Isolieren oder erneuern
│           └─ Kabel gebrochen (Biegebelastung am Mastfuß): Neue Kabel einziehen
│
└─ ENDE: Reparatur dokumentieren, Funktionstest bei Nacht durchführen
```

**Confidence:** documented — basierend auf Surveyor-Praxis und Elektrik-Diagnosehandbüchern.

### Entscheidungsbaum TB-BEL-02: LED-Beleuchtung flackert

```
START: LED-Beleuchtung flackert
│
├─ Prüfe: Flackern bei allen LEDs oder nur einzelnen?
│   │
│   ├─ ALLE LEDs flackern:
│   │   │
│   │   ├─ Prüfe: Bordspannung stabil?
│   │   │   ├─ Spannung schwankt (< 11V oder > 15V bei 12V-System):
│   │   │   │   ├─ Batteriezustand prüfen (Innenwiderstand)
│   │   │   │   ├─ Laderegler-Einstellung prüfen
│   │   │   │   └─ Große Verbraucher gleichzeitig aktiv? (Ankerwinde, Bugstrahlruder)
│   │   │   └─ Spannung stabil:
│   │   │       ├─ Prüfe: Gemeinsamer Dimmer?
│   │   │       │   ├─ Ja → Dimmer-Typ prüfen (Phasenanschnitt inkompatibel mit LED)
│   │   │       │   │   ├─ Dimmer durch LED-tauglichen ersetzen (PWM >1 kHz)
│   │   │       │   │   └─ Mindestlast des Dimmers unterschritten? → Bypass-Widerstand
│   │   │       │   └─ Nein → Spannungsregler / DC-DC-Konverter prüfen
│   │   │       └─ Prüfe: Lose Masseverbindung (Wackelkontakt)
│   │   │           ├─ Massebolzen nachziehen
│   │   │           └─ Massekabel auf Korrosion prüfen
│   │   │
│   │   └─ EINZELNE LED flackert:
│   │       │
│   │       ├─ Prüfe: Leuchtmittel defekt?
│   │       │   ├─ Ersatz-LED einsetzen → Flackern weg = LED defekt
│   │       │   └─ Flackern bleibt → Kabel/Steckverbindung/Dimmer
│   │       │
│   │       ├─ Prüfe: Lose Steckverbindung?
│   │       │   ├─ Ja: Nachstecken, ggf. Kontakte reinigen
│   │       │   └─ Nein: Dimmer für diesen Kreis prüfen
│   │       │
│   │       └─ Prüfe: Thermische Abschaltung?
│   │           ├─ LED wird sehr heiß → Belüftung verbessern, Einbauraum vergrößern
│   │           └─ Temperatur normal → LED-Treiber intern defekt
│   │
│   └─ ERGEBNIS: Spezifische Ursache behoben, Langzeit-Test (24h)
│
└─ ENDE: Reparatur dokumentieren
```

**Confidence:** documented — basierend auf Elektrik-Troubleshooting-Erfahrung.

### Entscheidungsbaum TB-BEL-03: Unterwasserlicht funktioniert nicht mehr

```
START: Unterwasserlicht funktioniert nicht
│
├─ Prüfe: Sicherung/Schutzschalter
│   │
│   ├─ Sicherung ausgelöst:
│   │   ├─ Kurzschluss wahrscheinlich → NICHT sofort wieder einschalten!
│   │   ├─ Isolationswiderstand messen (Kabel zum UW-Licht)
│   │   │   ├─ Isolation < 1 MΩ: Wassereintritt in Kabel oder Leuchte
│   │   │   │   ├─ Boot SLIPPEN → Leuchte von außen inspizieren
│   │   │   │   ├─ Kabel-Durchführung prüfen (Kabelverschraubung)
│   │   │   │   └─ Leuchte ersetzen wenn Gehäuse beschädigt
│   │   │   └─ Isolation > 1 MΩ: Kein Wassereintritt
│   │   │       ├─ Kurzschluss in Steuerung/Dimmer?
│   │   │       └─ Überlast durch zweite Leuchte am gleichen Kreis?
│   │   │
│   │   └─ WARNUNG: Bei Verdacht auf Wassereintritt:
│   │       Prüfe SOFORT den Rumpfdurchbruch (Thru-hull) auf Dichtigkeit!
│   │       Leckage = SOFORTMASSNAHME (siehe F-BEL-06)
│   │
│   └─ Sicherung OK:
│       │
│       ├─ Prüfe: Spannung an der Leuchte (12V/24V)
│       │   ├─ Keine Spannung: Kabel/Steckverbindung defekt
│       │   └─ Spannung OK: LED-Modul intern defekt
│       │       ├─ Thru-hull: Muss bei nächstem Slip ersetzt werden
│       │       ├─ Surface-mount: Kann im Wasser getauscht werden (TIX-System)
│       │       └─ Transom: Kann über Wasser inspiziert und getauscht werden
│       │
│       └─ Prüfe: Steuerung/Controller
│           ├─ Controller zeigt Fehler: Reset, Firmware-Update
│           ├─ Andere Leuchten am gleichen Controller funktionieren: Kabel zur defekten Leuchte
│           └─ Keine Leuchte funktioniert: Controller defekt oder Stromversorgung
│
└─ ENDE: Bei jedem UW-Licht-Problem: Rumpfintegrität ZUERST prüfen!
```

**Confidence:** documented — basierend auf Surveyorpraxis.

### Entscheidungsbaum TB-BEL-04: EMV-Störungen durch Beleuchtung

```
START: Störungen an Funkgeräten/Navigation korrelieren mit Beleuchtung
│
├─ Prüfe: Welches Gerät ist gestört?
│   │
│   ├─ UKW-Funk (156–163 MHz):
│   │   ├─ Dimmer schrittweise ausschalten
│   │   │   ├─ Störung verschwindet bei bestimmtem Dimmer: Dimmer identifiziert
│   │   │   │   ├─ Ferritkern auf Dimmer-Zuleitung (2 Windungen)
│   │   │   │   ├─ Kabel zwischen Dimmer und Leuchte kürzen/bündeln
│   │   │   │   └─ Wenn persistiert: Dimmer durch EMV-konformen Typ ersetzen
│   │   │   └─ Störung bleibt bei allen Dimmern aus: LED-Treiber als Quelle
│   │   │       ├─ LED-Leuchten einzeln abschalten (Sicherung ziehen)
│   │   │       └─ Identifizierte Leuchte: Ferritkern, Kabelabstand, oder ersetzen
│   │   │
│   │   └─ Prüfe: Abstand LED-Kabel zu UKW-Antennenkabel
│   │       ├─ < 30 cm: Mindestabstand herstellen oder Kabel schirmen
│   │       └─ > 30 cm: Hochfrequenz-Filter am LED-Treiber einsetzen
│   │
│   ├─ GPS (1.575 MHz):
│   │   ├─ LED-Treiber mit Schaltfrequenz nahe 1,575 MHz oder Oberwellen
│   │   ├─ Prüfe: LED-Streifen (günstige) in Antennennähe?
│   │   └─ Lösung: Ferritkerne, Abstand, EMV-konforme LED-Streifen
│   │
│   └─ AIS (161,975 / 162,025 MHz):
│       ├─ Wie UKW behandeln (ähnlicher Frequenzbereich)
│       └─ AIS-Empfang ist empfindlicher als UKW → strengere Abschirmung nötig
│
├─ Generelle Lösungsreihenfolge (Kosten steigend):
│   1. Ferritkerne auf betroffene Leitungen
│   2. Kabelabstand vergrößern
│   3. Geschirmte Kabel verwenden
│   4. LED-Treiber/Dimmer ersetzen (EMV-konform)
│   5. LC-Filter einbauen
│
└─ ENDE: EMV-Test wiederholen nach jeder Maßnahme
```

**Confidence:** documented — basierend auf EMV-Praxis Marine.

### Entscheidungsbaum TB-BEL-05: Lichtplanung für Neubau/Refit

```
START: Lichtplanung für Yacht (Neubau oder Refit)
│
├─ Schritt 1: Bestandsaufnahme / Anforderungsdefinition
│   │
│   ├─ Yachttyp und -größe bestimmen
│   │   ├─ Segelboot < 12m → COLREG < 12m Lichterführung
│   │   ├─ Segelboot 12–20m → COLREG 12–20m
│   │   ├─ Motorboot < 12m → COLREG < 12m (mit Topplicht)
│   │   ├─ Motorboot 12–20m → COLREG 12–20m
│   │   └─ Yacht > 20m → COLREG 20–50m + Klassifikationsgesellschaft
│   │
│   ├─ Bordspannung bestimmen
│   │   ├─ 12V DC → Standard, breite Komponentenverfügbarkeit
│   │   ├─ 24V DC → Halbierte Kabelquerschnitte, effizientere Dimmer
│   │   └─ Hybrid → DC/DC-Konverter für Beleuchtungskreise planen
│   │
│   └─ Budget definieren
│       ├─ Basis: Nur Navigationslichter (BSH-konform) + einfache Kabinenspots
│       ├─ Standard: Nav-Lichter + Zone-Beleuchtung + Dimmer + Rotlicht
│       ├─ Premium: + Lichtsteuerung + Akzentlicht + Unterwasserlicht
│       └─ Luxus: + DMX/DALI + professionelle Lichtplanung + Custom-Leuchten
│
├─ Schritt 2: Navigationslichter auswählen
│   │
│   ├─ BSH-zugelassene Modelle wählen (Hella Marine, Lopolight, Aqua Signal)
│   ├─ Korrekte Tragweite für Bootsgröße sicherstellen
│   ├─ Montageposition nach COLREG definieren
│   └─ Kabelquerschnitt berechnen (max. 3% Spannungsabfall)
│
├─ Schritt 3: Innenbeleuchtung planen
│   │
│   ├─ Zonierung: Jeder Raum mit eigenem Lichtkreis
│   ├─ Schichten: Allgemein + Akzent + Arbeits- + Nachtlicht
│   ├─ Farbtemperatur festlegen (einheitlich pro Zone!)
│   ├─ CRI-Anforderung pro Zone definieren
│   ├─ Dimmbarkeit: LED-taugliche Dimmer von Beginn an einplanen
│   └─ Rotlicht: Cockpit, Niedergang, Steuerstand
│
├─ Schritt 4: Außenbeleuchtung planen
│   │
│   ├─ Cockpit: IP67+, dimmbar, Weiß/Rot-Umschaltung
│   ├─ Decks: Trittsicherheit, indirektes Licht
│   ├─ Badeplattform: Niedervolt, seegangsicher
│   └─ Unterwasser: Rumpfdurchbruch ja/nein, RGBW, Steuerung
│
├─ Schritt 5: Elektrik dimensionieren
│   │
│   ├─ Gesamtlast berechnen (alle Lichter gleichzeitig = worst case)
│   ├─ Sicherungen dimensionieren (1,5× Nennstrom)
│   ├─ Kabelquerschnitte berechnen (ABYC E-11 oder DIN)
│   ├─ Schalttafel planen (Gruppen: Nav, Cockpit, Salon, Kabinen, Unter Wasser)
│   └─ Energiebilanz in Bordnetz-Berechnung integrieren
│
└─ Schritt 6: Dokumentation
    │
    ├─ Stromlaufplan (Schaltplan) mit allen Lichtkreisen
    ├─ Positionsplan (wo ist welche Leuchte)
    ├─ Materialliste mit BSH-Nummern
    ├─ Kabelplan mit Querschnitten und Farben
    └─ Bedienungsanleitung für Skipper (Lichterführung + Lichtszenen)
```

**Confidence:** benchmark — basierend auf professioneller Marine-Elektrikplanung.

---

## 8. FAQ

### FAQ-01: Brauche ich für LED-Navigationslichter eine BSH-Zulassung?

**Ja, unbedingt.** Jedes Navigationslichter auf Fahrzeugen unter deutscher Flagge muss eine gültige BSH-Bauartgenehmigung besitzen. Das gilt für die komplette Leuchte — nicht für einzelne Leuchtmittel. Ein LED-Retrofit-Leuchtmittel in einem Halogen-Navigationslichgehäuse ist NICHT zugelassen, auch wenn sowohl das Originalgehäuse als auch das LED-Leuchtmittel einzeln Prüfsiegel haben. Die BSH-Zulassung bezieht sich immer auf die Kombination von Gehäuse + Optik + Leuchtmittel.

**Confidence:** documented.

### FAQ-02: Darf ich eine Dreifarbenlaterne und getrennte Seitenlichter gleichzeitig verwenden?

**Nein.** COLREG Regel 25 erlaubt entweder die Dreifarbenlaterne ODER getrennte Seitenlichter + Hecklicht. Niemals beides gleichzeitig. Die Dreifarbenlaterne darf nur auf Segelfahrzeugen unter 20 m Länge verwendet werden und nur unter Segel (nicht unter Motor). Bei Motorbetrieb: Dampferlicht + getrennte Seitenlichter + Hecklicht.

**Confidence:** documented.

### FAQ-03: Welche Farbtemperatur empfehlen Sie für die Kabinenbeleuchtung?

Empfohlen: **2.700–3.000 K (warmweiß)**. Dieser Bereich wirkt behaglich und wohnlich, ähnlich einer Halogenlampe. Für die Pantry und den Kartentisch sind 3.500–4.000 K (neutralweiß) sinnvoll, um eine bessere Farbbeurteilung (Lebensmittel) und Konzentration zu ermöglichen. Ideal: Dual-Color-LEDs, die zwischen warm und neutral umschaltbar sind.

**Confidence:** benchmark.

### FAQ-04: Wie viel Strom spare ich durch LED-Umrüstung?

Typisch **80–90% Stromeinsparung** gegenüber Halogen-/Glühlampenbeleuchtung. Beispiel: 20 Halogen-Spots (G4 20W) verbrauchen 400W. Ersetzt durch LED G4 3W: 60W. Einsparung: 340W = 85%. Bei 5h Nutzung pro Nacht: 28 Ah statt 167 Ah (bei 12V). Das entspricht einer kleinen Zusatzbatterie.

**Confidence:** calculated.

### FAQ-05: Kann ich Halogen-Dimmer für LED verwenden?

**In der Regel nein.** Halogen-Dimmer arbeiten mit Phasenanschnitt (Triac) und benötigen eine Mindestlast von 20–60W. LEDs erreichen diese Last oft nicht, was zu Flackern, Brummen und vorzeitigem Defekt führt. Lösung: LED-spezifische Dimmer verwenden (PWM-basiert), die keine Mindestlast benötigen und mit LED-Treibern kompatibel sind.

**Confidence:** documented.

### FAQ-06: Wie prüfe ich, ob meine Navigationslichter die korrekte Tragweite haben?

Pragmatische Methode: Bei klarer Nacht die Yacht ankern und mit dem Dingi auf die geforderte Entfernung (z.B. 2 sm) fahren. Die Lichter sollten deutlich sichtbar sein. Professionell: Luxmeter-Messung in definiertem Abstand und Rückrechnung auf Candela. Die errechnete Lichtstärke muss die COLREG-Mindestanforderung übertreffen.

**Confidence:** documented.

### FAQ-07: Was ist eine Dreifarbenlaterne und wann darf ich sie verwenden?

Eine Dreifarbenlaterne vereint rotes Seitenlicht (Backbord), grünes Seitenlicht (Steuerbord) und weißes Hecklicht in einem Gehäuse und wird am Masttopp montiert. Sie darf NUR von Segelfahrzeugen unter 20m Länge verwendet werden und NUR unter Segel (nicht unter Motor). Vorteil: Hohe Position → gute Sichtbarkeit. Geringer Stromverbrauch (eine Leuchte statt drei). Nachteil: Bei Mastbruch verliert man alle Navigationslichter gleichzeitig.

**Confidence:** documented.

### FAQ-08: Welche IP-Schutzart brauchen Leuchten im Cockpit?

Mindestens **IP65** (staubdicht, Strahlwasser geschützt). Empfohlen: **IP67** (staubdicht, zeitweiliges Untertauchen). Für Leuchten am Steuerstand oder in der Sprayzone (Bugbereich, Segelboote bei Krängung): IP67 zwingend. Unterwasserbeleuchtung: IP68 (dauerhaftes Untertauchen).

**Confidence:** benchmark.

### FAQ-09: Lohnt sich Unterwasserbeleuchtung auf einer Segelyacht?

Funktional weniger als auf Motoryachten, da Segelboote selten in Marinas/Ankerbuchten liegen, wo das Licht sichtbar wäre. Aber: Auf Fahrtenyachten, die viel vor Anker liegen, ist Unterwasserbeleuchtung ein erheblicher Komfort- und Sicherheitsgewinn (Schwimmer im Wasser, Dingi-Verkehr bei Nacht). Empfehlung: Transom-Montage als kostengünstiger Einstieg (kein Rumpfdurchbruch erforderlich).

**Confidence:** benchmark.

### FAQ-10: Wie verhindere ich, dass LED-Beleuchtung meinen UKW-Funk stört?

1. Nur EMV-zertifizierte LED-Leuchten verwenden (CE-EMV-Kennzeichnung).
2. Ferritkerne auf Zuleitungen zu LED-Leuchten und Dimmern.
3. Mindestabstand 30 cm zwischen LED-Kabeln und Antennenkabeln.
4. Keine billigen LED-Streifen ohne EMV-Prüfung verwenden.
5. LED-Dimmer mit Frequenz > 10 kHz (je höher, desto weniger Oberwellen im UKW-Band).
6. Im Zweifel: Dimmer abklemmen und prüfen, ob Störung verschwindet.

**Confidence:** documented.

### FAQ-11: Welche LED-Leuchtmittel eignen sich als Retrofit für G4-Halogen?

LED-Retrofit G4 mit **Bi-Pin-Sockel** und **12V DC** (NICHT 12V AC-Typen verwenden). Wichtig: Gleiche oder kleinere Bauform als Original, sonst passt das Leuchtmittel nicht in die Leuchte. Empfohlene Leistung: 2–3W LED für 20W Halogen-Ersatz. CRI > 80, besser > 90. Warmweiß 2.700–3.000 K. Marken: Hella Marine, Imtra, Dr. LED (marine-spezifisch).

**Confidence:** documented.

### FAQ-12: Muss das Ankerlicht die ganze Nacht brennen?

**Ja.** COLREG Regel 30 schreibt das Ankerlicht von Sonnenuntergang bis Sonnenaufgang vor. Ausnahme: Fahrzeuge unter 7m, die nicht in oder nahe einem engen Fahrwasser, einer Reede oder einem Ankerplatz liegen. In der Praxis wird das Ankerlicht auf kleinen Booten in geschützten Buchten manchmal weggelassen — das ist jedoch ein Verstoß gegen COLREG und kann bei Kollision zu Haftungsproblemen führen. LED-Ankerlicht: ~1W × 10h = 0,8 Ah — kein Grund, es nicht zu verwenden.

**Confidence:** documented.

### FAQ-13: Können LED-Navigationslichter durch Vibrationen am Mast ausfallen?

Theoretisch deutlich weniger anfällig als Glühlampen, da LEDs keine fragilen Glühfäden haben. In der Praxis treten Ausfälle dennoch auf durch: Lötstellenbrüche (minderwertige LEDs), Steckverbindungen im Mast (Vibrationslösung), Kabelbrüche am Mastfuß (Biegewechselbelastung). Prävention: Hochwertige LED-Leuchten (Hella, Lopolight), verzinnte Kabel, Zugentlastung am Mastfuß, vibrationsfeste Steckverbindungen.

**Confidence:** documented.

### FAQ-14: Was ist der Unterschied zwischen einem Topplicht und einem Dampferlicht?

Im Prinzip nichts — "Dampferlicht" ist der umgangssprachliche Begriff für das Topplicht eines Maschinenfahrzeugs. Das Topplicht (COLREG Regel 21) ist ein weißes Licht über einen Bogen von 225° und kennzeichnet ein Maschinenfahrzeug in Fahrt. Der Name "Dampferlicht" stammt aus der Zeit, als dampfgetriebene Schiffe sich durch dieses Licht von Seglern unterschieden.

**Confidence:** documented.

### FAQ-15: Wie viele Lumen braucht eine gute Cockpitbeleuchtung?

Für den gesamten Cockpitbereich (ca. 3–6 m²) sind **400–800 Lumen (gesamt)** bei Hafenbeleuchtung und **50–100 Lumen** bei Nachtfahrt ausreichend. Stufenlose Dimmung ist essentiell. Wichtiger als die Gesamtlumenzahl ist die Verteilung: Indirektes Licht (unter Süllrand, unter Bänken) blendet weniger als Spots von oben.

**Confidence:** benchmark.

### FAQ-16: Welche Farbe sollte Unterwasserbeleuchtung haben?

**Blau** ist der Klassiker und wird am weitesten im Wasser sichtbar (geringste Absorption). **Weiß** beleuchtet die direkte Umgebung besser (Schwimmer, Boden). **Grün** lockt Plankton → Fische an (Angler-Favorit). **RGBW** bietet maximale Flexibilität. Empfehlung: RGBW-Unterwasserlichter, die per Controller verschiedene Farben und Szenen ermöglichen.

**Confidence:** documented.

### FAQ-17: Brauche ich eine Notbeleuchtung an Bord?

CE-Kategorie A und B: Ja, empfohlen (ISO 9094 Fluchtweg-Beleuchtung). Superyachten (>24m, Klassifikationsgesellschaft): Ja, Pflicht (SOLAS/MCA). Sportboote: Keine explizite Pflicht, aber dringend empfohlen — mindestens eine batteriebetriebene LED-Leuchte im Niedergangsbereich, die bei Stromausfall automatisch aktiviert.

**Confidence:** documented.

### FAQ-18: Wie reinige ich verschmutzte Navigationslichter?

1. Leuchte stromlos schalten.
2. Mit reichlich Süßwasser abspülen (Salzfilm lösen).
3. Optik mit weichem Mikrofasertuch und mildem Reiniger (kein Aceton, kein Scheuermittel!) reinigen.
4. Bei hartnäckiger Verfärbung: Polycarbonat-Politur (Novus #1 oder #2).
5. NIEMALS Lösungsmittel oder aggressive Reiniger verwenden (Polycarbonat versprödet).
6. UV-Schutzmittel auftragen (Novus #1 oder 303 Aerospace Protectant).
7. Dichtungen auf Risse prüfen und ggf. mit Silikon nachfetten.

**Confidence:** documented.

### FAQ-19: Können LED-Leuchten überhitzen?

Ja. LEDs erzeugen zwar weniger Gesamtwärme als Halogen, aber die Wärme konzentriert sich auf einen kleinen Chip und muss abgeführt werden. In geschlossenen Einbaugehäusen ohne Luftzirkulation kann die LED-Temperatur über 85°C steigen, was die Lebensdauer drastisch verkürzt. Abhilfe: Einbauöffnung nicht zu eng, Belüftungsschlitze nicht blockieren, Leuchten mit Alu-Kühlkörper verwenden.

**Confidence:** measured.

### FAQ-20: Was kostet eine komplette LED-Umrüstung?

Abhängig von Bootsgröße und Ausstattung:

| Bootsgröße | Navigationslichter | Innenbeleuchtung | Gesamt (ca.) |
|-----------|-------------------|-----------------|-------------|
| 8–10m | 200–400 € | 200–400 € | 400–800 € |
| 10–14m | 300–600 € | 400–800 € | 700–1.400 € |
| 14–18m | 400–800 € | 800–1.500 € | 1.200–2.300 € |
| 18m+ | 600–2.000 € | 1.500–5.000 € | 2.100–7.000 € |

**Confidence:** estimated.

### FAQ-21: Darf ich auf der Elbe (Binnenwasserstraße) andere Lichter führen als auf See?

Ja. Auf Binnenwasserstraßen gelten die Binnenschifffahrtsstraßen-Ordnung (BinSchStrO) und ggf. die Rheinschifffahrtspolizeiverordnung (RheinSchPV). Die Lichterführung weicht in einigen Punkten von COLREG ab (z.B. andere Farbsektoren, zusätzliche Lichter für bestimmte Fahrzeugtypen). Sportboote müssen die für das jeweilige Gewässer geltenden Vorschriften kennen und befolgen.

**Confidence:** documented.

### FAQ-22: Wie wichtig ist der CRI-Wert für die Bordbeleuchtung?

Sehr wichtig für Wohnbereiche. Ein CRI unter 80 lässt Holzoberflächen, Textilien und Lebensmittel unnatürlich aussehen. Im Salon und der Pantry sollte CRI ≥ 90 angestrebt werden. Im Maschinenraum oder Stauraum ist CRI ≥ 70 ausreichend. Günstige LED-Streifen haben oft nur CRI 70 — für Hauptwohnbereiche inakzeptabel.

**Confidence:** benchmark.

### FAQ-23: Wie schütze ich Unterwasserbeleuchtung vor Bewuchs?

1. Antifouling um die Leuchte herum (nicht auf die Linse!).
2. Regelmäßige Reinigung bei jedem Tauchgang/Slip.
3. Leuchte regelmäßig einschalten — die Wärme hemmt Bewuchs.
4. Kupferleitpaste auf die Linsenkante (hemmt Seepocken).
5. Einige Hersteller bieten Anti-Fouling-Beschichtungen für Linsen an.

**Confidence:** documented.

### FAQ-24: Können LED-Navigationslichter augenblicklich die volle Helligkeit erreichen?

**Ja.** Im Gegensatz zu Halogen- und besonders Xenon-Leuchtmitteln erreichen LEDs sofort (< 1 ms) ihre volle Lichtstärke. Das ist ein Sicherheitsvorteil: Navigationslichter sind sofort nach dem Einschalten voll wirksam. Bei Halogenlampen dauert es 1–3 Sekunden bis zur vollen Helligkeit, bei Xenon/HID bis zu 30 Sekunden.

**Confidence:** measured.

### FAQ-25: Welche Rolle spielt die Beleuchtung bei der AYDI-Analyse?

Die Beleuchtung fließt in mehrere AYDI-Analyse-Module ein:
- **Compliance:** BSH-Zulassung, COLREG-konforme Lichterführung, korrekte Sichtwinkel
- **Sicherheit:** Nachtsicht-Tauglichkeit, Notbeleuchtung, Fluchtweg-Beleuchtung
- **Ergonomie:** Beleuchtungsstärken pro Zone, Dimmbarkeit, Arbeitsbeleuchtung
- **Emotional:** Lichtkonzept, Farbtemperatur, Atmosphäre, Design-Integration
- **Energie:** Gesamtverbrauch Beleuchtung, LED-Anteil, Effizienz
- **Material:** Korrosionsbeständigkeit, IP-Schutz, UV-Stabilität der Leuchten

**Confidence:** documented.

### FAQ-26: Wie lang halten LED-Navigationslichter wirklich?

Herstellerangaben: 30.000–60.000 Stunden (LED-Chip). In der Praxis bestimmen jedoch andere Faktoren die Lebensdauer: Korrosion der Kontakte (5–15 Jahre), UV-Degradation der Polycarbonat-Optik (10–20 Jahre), Dichtungsversagen (5–10 Jahre). Reale Lebensdauer einer kompletten LED-Navigationsleuchte in Salzwasserumgebung: 8–15 Jahre bei guter Pflege.

**Confidence:** documented.

### FAQ-27: Was ist der Vorteil von Multivolt-Leuchten (9–33V)?

Multivolt-Leuchten (z.B. Hella Marine NaviLED) arbeiten in einem Spannungsbereich von 9–33V DC. Vorteile: Kompatibel mit 12V und 24V Systemen. Tolerieren Spannungsschwankungen (z.B. beim Laden oder bei schwacher Batterie). Gleiche Helligkeit bei 12V und 24V. Kein falsches Leuchtmittel möglich. Nachteil: Etwas teurer als Einzelspannungsleuchten.

**Confidence:** documented.

---

## 9. Glossar

| # | Begriff | Erklärung |
|---|---------|-----------|
| 1 | **Ankerlicht** | Weißes Rundumlicht (360°), das ein vor Anker liegendes Fahrzeug von Sonnenuntergang bis Sonnenaufgang zeigen muss (COLREG Regel 30) |
| 2 | **ABYC E-11** | Standard der American Boat and Yacht Council für elektrische Systeme auf Booten, definiert Kabelquerschnitte, Absicherung und Installation |
| 3 | **BSH** | Bundesamt für Seeschifffahrt und Hydrographie — zuständig für die Bauartgenehmigung von Navigationslichtern in Deutschland |
| 4 | **Candela (cd)** | SI-Einheit der Lichtstärke, beschreibt die Lichtmenge pro Raumwinkeleinheit in eine bestimmte Richtung |
| 5 | **CCR** | Constant Current Reduction — Dimmverfahren für LEDs durch Reduzierung des Betriebsstroms |
| 6 | **CIE** | Commission Internationale de l'Éclairage — internationale Beleuchtungskommission, definiert Farbstandards |
| 7 | **COLREG** | Convention on the International Regulations for Preventing Collisions at Sea — Internationale Regeln zur Verhütung von Zusammenstößen auf See (1972, zuletzt 2003) |
| 8 | **CRI / Ra** | Color Rendering Index / allgemeiner Farbwiedergabeindex — Maß für die Natürlichkeit der Farbwiedergabe unter einer Lichtquelle (max. 100) |
| 9 | **Dampferlicht** | Umgangssprachlich für das Topplicht eines Maschinenfahrzeugs |
| 10 | **DMX** | Digital Multiplex — Steuerungsprotokoll für professionelle Beleuchtung (urspr. Bühne), auch auf Superyachten verwendet |
| 11 | **Dreifarbenlaterne** | Kombinierte Navigationslaterne am Masttopp mit rotem, grünem und weißem Sektor (Seitenlaternen + Hecklicht), nur für Segelfahrzeuge < 20m unter Segel |
| 12 | **Duty Cycle** | Tastverhältnis bei PWM-Dimmung — Verhältnis von Ein-Zeit zur Gesamtperiode |
| 13 | **EMV** | Elektromagnetische Verträglichkeit — Fähigkeit elektronischer Geräte, ohne gegenseitige Störung zu funktionieren |
| 14 | **Farbtemperatur** | In Kelvin (K) gemessene Eigenschaft einer Lichtquelle, beschreibt den Farbeindruck (2.700K = warmweiß, 6.500K = tageslichtweiß) |
| 15 | **Festoon** | Soffittenlampe — Leuchtmittel mit zwei seitlichen Kontakten (z.B. 42mm Festoon für Marine-Deckenleuchten) |
| 16 | **G4** | Stecksockel mit 4mm Pinabstand — Standardsockel für Halogen- und LED-Leuchtmittel in Marine-Leuchten |
| 17 | **Galvanische Korrosion** | Elektrochemische Korrosion zwischen verschiedenen Metallen in einem Elektrolyten (Seewasser) |
| 18 | **Hecklicht** | Weißes Navigationslicht am Heck mit 135° Sichtwinkel, kennzeichnet die Rückseite des Fahrzeugs |
| 19 | **IP-Schutzart** | International Protection Rating — Klassifizierung der Dichtigkeit (z.B. IP67 = staubdicht + zeitweiliges Untertauchen) |
| 20 | **LED** | Light Emitting Diode — Halbleiter-Leuchtmittel mit hoher Effizienz und Lebensdauer |
| 21 | **Lumen (lm)** | SI-Einheit des Lichtstroms — beschreibt die gesamte sichtbare Lichtleistung einer Quelle |
| 22 | **Lux (lx)** | SI-Einheit der Beleuchtungsstärke — Lichtstrom pro Fläche (1 lx = 1 lm/m²) |
| 23 | **Multivolt** | Leuchte mit weitem Eingangsspannungsbereich (typisch 9–33V DC), kompatibel mit 12V und 24V Systemen |
| 24 | **Nachtsicht / Dunkeladaption** | Physiologische Anpassung des Auges an Dunkelheit (20–30 Min.), wird durch Weißlichtexposition zerstört |
| 25 | **NMEA 2000** | Marine-Datenbus-Standard für Vernetzung von Bordelektronik (inkl. Lichtsteuerung) |
| 26 | **Polycarbonat** | Transparenter Kunststoff für Navigationsleuchten-Optiken, UV-empfindlich |
| 27 | **PWM** | Pulse Width Modulation — Dimmverfahren für LEDs durch schnelles Ein-/Ausschalten |
| 28 | **Rhodopsin** | Sehpurpur — lichtempfindliches Pigment in den Stäbchenzellen der Netzhaut, zuständig für Nachtsicht |
| 29 | **Rotlicht** | Licht mit Wellenlänge > 620 nm, das die Nachtsicht (Dunkeladaption) nicht zerstört |
| 30 | **Rundumlicht** | Navigationslicht mit 360° Sichtwinkel (keine toten Winkel) |
| 31 | **Schlepplicht** | Gelbes Licht mit 135° Sichtwinkel am Heck schleppender Fahrzeuge |
| 32 | **Seitenlaterne** | Navigationslicht zur Kennzeichnung der Fahrtrichtung — Rot (Backbord) und Grün (Steuerbord) mit je 112,5° Sichtwinkel |
| 33 | **SELV** | Safety Extra Low Voltage — Schutzkleinspannung (< 50V DC), berührungssicher |
| 34 | **sm (Seemeile)** | Nautical Mile — 1.852 m, Einheit für die Tragweite von Navigationslichtern |
| 35 | **Suchscheinwerfer** | Leistungsstarkes, schwenkbares Weißlicht für Beleuchtung von Hindernissen, Anlegerplätzen, MOB |
| 36 | **Thru-hull** | Rumpfdurchbruch — Montagetyp für Unterwasserbeleuchtung, bei dem die Leuchte bündig in den Rumpf eingelassen ist |
| 37 | **TIX** | Thru-hull Interchangeable (Lumishore) — System zum Austausch des LED-Moduls ohne Slippen |
| 38 | **Topplicht** | Weißes Navigationslicht mit 225° Sichtwinkel, kennzeichnet ein Maschinenfahrzeug in Fahrt |
| 39 | **Tragweite** | Maximale Entfernung, in der ein Navigationslicht unter definierten atmosphärischen Bedingungen sichtbar ist (in Seemeilen) |
| 40 | **Triac** | Halbleiterschalter für Phasenanschnittdimmer (Standard für Glüh-/Halogenlampen, problematisch mit LED) |
| 41 | **TVS-Diode** | Transient Voltage Suppressor — Überspannungsschutzbauelement zum Schutz von LEDs gegen Spannungsspitzen |
| 42 | **Unterwasserbeleuchtung** | LED-Leuchten unterhalb der Wasserlinie, montiert im Rumpf (thru-hull), auf dem Rumpf (surface) oder am Spiegel (transom) |
| 43 | **USCG** | United States Coast Guard — US-amerikanische Zulassungsbehörde für Navigationslichter |
| 44 | **Zweifarbenlaterne** | Kombinierte Navigationslaterne mit rotem (Bb) und grünem (Stb) Sektor in einem Gehäuse, für Boote < 20m |

---

## 10. Schnell-Referenz

### 10.1 COLREG-Lichterführung — Kurzübersicht

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COLREG LICHTERFÜHRUNG SCHNELLREFERENZ                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MASCHINENFAHRZEUG IN FAHRT (< 50m):                                       │
│  ┌──────────┐                                                              │
│  │ ◉ Topp   │ Weiß 225° (vorn, oben)                                      │
│  │ ● Rot    │ Bb-Seitenlicht 112,5° (links)                               │
│  │ ● Grün   │ Stb-Seitenlicht 112,5° (rechts)                             │
│  │ ◉ Heck   │ Weiß 135° (achtern)                                         │
│  └──────────┘                                                              │
│                                                                             │
│  SEGELFAHRZEUG (< 20m, unter Segel):                                       │
│  Option A: Dreifarbenlaterne am Masttop (Rot+Grün+Weiß)                    │
│  Option B: Getrennte Seitenlichter + Hecklicht                             │
│  KEIN Topplicht!                                                           │
│                                                                             │
│  SEGELFAHRZEUG UNTER MOTOR:                                                │
│  = Maschinenfahrzeug (Topplicht + Seitenlichter + Hecklicht)               │
│                                                                             │
│  VOR ANKER (< 50m):                                                        │
│  1× Weißes Rundumlicht 360° (Vorschiff)                                    │
│                                                                             │
│  TRAGWEITEN:                                                                │
│  < 12m: Topp 2sm, Seiten 1sm, Heck 2sm, Rund 2sm                          │
│  12-20m: Topp 3sm, Seiten 2sm, Heck 2sm, Rund 2sm                         │
│  20-50m: Topp 5sm, Seiten 2sm, Heck 2sm, Rund 2sm                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.2 LED-Umrüstung — Schnellanleitung

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              LED-UMRÜSTUNG CHECKLISTE SCHNELLREFERENZ                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  NAVIGATIONSLICHTER:                                                        │
│  □ NUR komplette BSH-zugelassene LED-Leuchten (kein Retrofit!)             │
│  □ Korrekte Tragweite für Bootsgröße wählen                                │
│  □ Multivolt (9–33V) wenn möglich                                          │
│  □ Kabelquerschnitt prüfen (bei LED geringer, aber Bestand ok)             │
│  □ BSH-Nummer auf neuer Leuchte vorhanden?                                 │
│                                                                             │
│  INNENBELEUCHTUNG:                                                          │
│  □ Farbtemperatur einheitlich (2.700–3.000 K für Wohnbereiche)             │
│  □ CRI ≥ 90 für Salon, Pantry, Kabinen                                    │
│  □ LED-taugliche Dimmer (PWM > 1 kHz)                                      │
│  □ Mindestlast der Dimmer beachten                                         │
│  □ Dual-Color (Weiß/Rot) für Cockpit und Niedergang                       │
│  □ Leuchtmittel als Set kaufen (gleiche Charge)                            │
│                                                                             │
│  COCKPIT/AUSSEN:                                                            │
│  □ Mindestens IP65, besser IP67                                             │
│  □ UV-beständiges Gehäuse                                                   │
│  □ Salzwasserbeständig (316L oder Polymer)                                  │
│                                                                             │
│  NACH UMRÜSTUNG:                                                            │
│  □ EMV-Test: UKW-Funk bei Dimmer-Betrieb prüfen                           │
│  □ Dimmbarkeit aller Leuchten testen (Flackern?)                           │
│  □ Nachtsicht-Test: Cockpit-Rotlicht aus See nicht sichtbar?              │
│  □ Dokumentation aktualisieren (Leuchtenliste, Stromaufnahme)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.3 Beleuchtungsstärken-Referenz

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              EMPFOHLENE BELEUCHTUNGSSTÄRKEN AN BORD                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Zone                    Aufgabe              Empfohlen (lx)    Min (lx)   │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Steuerstand             Navigation           50–100            30         │
│  Kartentisch             Karten lesen          200–500           150        │
│  Pantry                  Kochen               300–500           200        │
│  Salon                   Allgemein            150–300           100        │
│  Salon                   Lesen/Arbeiten       300–500           200        │
│  Kabine                  Allgemein            100–200           50         │
│  Kabine                  Nachtlicht           5–15              1          │
│  Kopf/WC                 Allgemein            150–300           100        │
│  Maschinenraum           Wartung              200–500           150        │
│  Cockpit (Hafen)         Abendnutzung         50–150            30         │
│  Cockpit (Nachtfahrt)    Minimal              5–20              0          │
│                                                                             │
│  Merksatz:                                                                  │
│  Warmweiß (2.700–3.000K) für Wohnen                                       │
│  Neutralweiß (3.500–4.000K) für Arbeiten                                   │
│  Rotlicht (640–660nm) für Nachtsicht                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.4 Fehler-Schnelldiagnose

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              BELEUCHTUNG — SCHNELLDIAGNOSE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SYMPTOM                        → WAHRSCHEINLICHE URSACHE                   │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Alle Lichter aus               → Sicherung, Hauptschalter, Masse          │
│  Einzelnes Licht aus            → Leuchtmittel, Steckverbindung, Kabel     │
│  LED flackert                   → Dimmer-Inkompatibilität, Mindestlast     │
│  LED-Streifen löst sich         → Kleber versagt, Profil verwenden         │
│  UKW brummt bei Dimmen          → EMV: Ferritkern, Abstand, Dimmer-Typ    │
│  Kondensat in Leuchte           → IP-Schutz unzureichend, Dichtung defekt │
│  Farbtemperatur unterschiedlich → Verschiedene Leuchtmittel/Chargen        │
│  Nav-Licht zu schwach           → Optik verschmutzt, Spannungsabfall       │
│  Unterwasserlicht flackert      → Wassereintritt → SOFORT prüfen!         │
│  Schneller Zinkanoden-Verbrauch → Galvanische Korrosion durch UW-Licht     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Komplette LED-Umrüstung einer Fahrtenyacht 12m (Segelboot)

**Ausgangslage:**
- Yacht: Bavaria 40 Cruiser, Baujahr 2008, LOA 12,35m
- Bordspannung: 12V DC
- Bestandsbeleuchtung: 24× Halogen G4 20W (Innen), 4× Halogen 10W (Cockpit), Halogen-Navigationslichter
- Problem: Hoher Stromverbrauch (Beleuchtung allein 500 Wh/Abend), häufiger Leuchtmittelwechsel

**Maßnahmen:**

| Position | Bestand | Neu | Stück | Kosten |
|----------|---------|-----|-------|--------|
| Navigationslichter | Aqua Signal 40 Halogen | Hella Marine NaviLED PRO | Satz | 420 € |
| Dreifarben + Anker | Aqua Signal Halogen | Hella Marine NaviLED PRO Tri/Anker | 1 | 165 € |
| Salon Spots | G4 Halogen 20W | Hella EuroLED 75 Dual | 8 | 416 € |
| Pantry Spots | G4 Halogen 20W | Hella EuroLED 75 | 3 | 114 € |
| Kabinen | G4 Halogen 10W | Hella EuroLED 75 | 6 | 228 € |
| Leselampen | Halogen G4 20W | Imtra Ventura PowerLED | 4 | 480 € |
| Cockpit | Halogen 10W, nicht dimmbar | Hella EuroLED 75 Dual (IP67) | 4 | 208 € |
| Dimmer | Halogen-Dimmer (Phasenanschnitt) | Hella Marine LED-Dimmer | 3 | 195 € |
| Niedergang-Stufen | Keine | LED-Streifen warmweiß in Alu-Profil | 2m | 85 € |

**Gesamtkosten:** 2.311 € (Material), Installation DIY

**Ergebnis:**

| Parameter | Vorher | Nachher | Einsparung |
|-----------|--------|---------|------------|
| Stromverbrauch Beleuchtung | 500 Wh/Abend | 75 Wh/Abend | 85% |
| Stromverbrauch Ankerlicht (10h) | 250 Wh | 15 Wh | 94% |
| Leuchtmittelwechsel/Saison | 5–8 | 0 | 100% |
| Nachtsicht-Tauglichkeit | Keine (Weißlicht) | Dual-Color (Weiß/Rot) | Erheblich verbessert |
| Beleuchtungsqualität (subjektiv) | Gut (Halogen-Warmton) | Sehr gut (LED warm, dimmbar) | Verbessert |

**Amortisation:** ~3 Jahre (durch ersparten Landstrom, Generator-Diesel und Leuchtmittel-Ersatz)

**Confidence:** documented — basierend auf realer Umrüstung, dokumentiert.

### ANHANG B: Fallstudie — Navigationslichter-Upgrade einer Motoryacht 15m

**Ausgangslage:**
- Yacht: Princess V48, Baujahr 2012, LOA 14,90m
- Bordspannung: 24V DC
- Problem: Alte Halogen-Navigationslichter (Aqua Signal Serie 43), ein Topplicht ausgefallen, Seitenlaternen korrodiert (Gehäuse Messing → Grünspan)

**Maßnahmen:**

| Position | Bestand | Neu | Kosten |
|----------|---------|-----|--------|
| Topplicht 3 sm | AS43 Halogen | Lopolight 200-010 (3 sm, 316L SS) | 180 € |
| Seitenlaternen (Paar) | AS43 Halogen, Messing | Lopolight 200-024/025 (316L SS) | 200 € |
| Hecklicht | AS43 Halogen | Lopolight 200-020 (316L SS) | 95 € |
| Ankerlicht | AS43 Halogen, Glasgehäuse | Lopolight 200-012W (316L SS) | 110 € |
| Installation | — | Fachwerft, 4h à 85 € | 340 € |

**Gesamtkosten:** 925 € (Material + Installation)

**Ergebnis:**
- Stromverbrauch Navigationslichter: von 75W auf 8W (Einsparung 89%)
- Material: 316L-Edelstahl statt Messing → keine Korrosionsprobleme
- Vibrationsfestigkeit: LED deutlich besser als Halogen (kein Fadenbruch)
- BSH-Zulassung: Alle Lopolight-Modelle BSH-zugelassen

**Lessons Learned:** Messing-Navigationsleuchten auf Salzwasser sind innerhalb von 5–10 Jahren korrosionsanfällig. Der Umstieg auf 316L-Edelstahl- oder Polymer-Gehäuse (Hella Marine) ist langfristig wirtschaftlicher.

**Confidence:** documented.

### ANHANG C: Fallstudie — Unterwasserbeleuchtung Nachrüstung Motoryacht

**Ausgangslage:**
- Yacht: Beneteau Gran Turismo 41, Baujahr 2019, LOA 12,78m
- Bordspannung: 12V DC
- Wunsch: Unterwasserbeleuchtung für Ankerbuchten (Mittelmeer)

**Analyse und Entscheidung:**

| Option | Montage | Kosten | Risiko | Entscheidung |
|--------|---------|--------|--------|-------------|
| Lumitec SeaBlaze X (Thru-hull) | Rumpfdurchbruch | ~800 € + Werft | Rumpfintegrität | Nein (Risiko) |
| Lumitec Mirage (Transom) | Spiegel | ~500 € + DIY | Gering | Ja |
| OceanLED Explore E6 | Surface mount | ~600 € + Werft | Bewuchs | Alternative |

**Installation (Transom, DIY):**
1. Position am Spiegel markiert (unterhalb Wasserlinie bei Fahrt, oberhalb bei Ruhe)
2. Bohrlöcher gesetzt, mit Sika 291i abgedichtet
3. Lumitec Mirage RGBW montiert (2× Leuchten, je 20W)
4. Kabel durch vorhandene Kabeldurchführung im Spiegel
5. Steuerung: Lumitec Touchpanel im Cockpit

**Ergebnis:**
- 2× Lumitec Mirage RGBW: 2 × 2.000 lm = 4.000 lm gesamt
- Stromverbrauch: 2 × 20W = 40W = 3,3 A @12V
- Farben: RGBW über Touchpanel steuerbar
- Keine Rumpfdurchbrüche → kein Risiko für Rumpfintegrität
- Einziger Nachteil: Nur achterliche Beleuchtung (kein 360°-Effekt)

**Confidence:** documented.

### ANHANG D: Fallstudie — EMV-Probleme nach LED-Umrüstung

**Ausgangslage:**
- Yacht: Hallberg-Rassy 37, Baujahr 2006
- Problem: Nach LED-Umrüstung (günstige LED-Streifen unter Deckvorsprüngen) starkes Rauschen im UKW-Funk, GPS zeigt sporadisch falsche Position

**Diagnose:**
1. UKW-Test mit allen LEDs aus: Kein Rauschen → LEDs als Quelle bestätigt
2. Einzelne LED-Kreise nacheinander eingeschaltet: LED-Streifen im Salon (10m, 12V, günstige China-Ware) als Hauptstörer identifiziert
3. LED-Streifen ohne Dimmer: Störung reduziert, aber nicht eliminiert
4. Abstand LED-Kabel zu VHF-Antennenkabel im Mast: 5 cm (direkt parallel!)

**Behebung:**
1. LED-Streifen durch EMV-zertifizierte Imtra LED Tape IP67 ersetzt (+ 180 €)
2. Ferritkerne auf alle LED-Zuleitungen installiert (8 Stück, Gesamtkosten 40 €)
3. Mastkabel: LED-Kabel und VHF-Kabel getrennt (Mindestabstand 20 cm) — Kabel neu verlegt
4. LED-Dimmer durch Imtra CereLight PWM-Dimmer ersetzt (Frequenz 20 kHz statt 500 Hz)

**Ergebnis:**
- UKW-Rauschen vollständig eliminiert
- GPS-Genauigkeit wiederhergestellt
- Gesamtkosten Nachbesserung: ~520 €

**Lessons Learned:** Günstige LED-Streifen ohne EMV-Prüfung sind die häufigste Ursache für Funkstörungen auf Yachten. Die Kostenersparnis (~100 € gegenüber marine-grade Streifen) steht in keinem Verhältnis zum Nachbesserungsaufwand.

**Confidence:** documented.

### ANHANG E: Fallstudie — Professionelle Lichtplanung Superyacht 24m

**Ausgangslage:**
- Yacht: Custom Motoryacht 24m, Neubau
- Anforderung: Professionelle Lichtplanung durch Marine-Lichtdesigner
- Budget Beleuchtung: 85.000 € (Material + Planung)

**Lichtkonzept:**

| Zone | Leuchttypen | Steuerung | Lichtszenen |
|------|------------|-----------|-------------|
| Master Suite | Cantalupi Einbauspots + indirekte LED-Streifen + Leselampen Prebit | DALI | Aufwachen, Tag, Abend, Nacht |
| Salon | Cantalupi Deckenspots + LED-Streifen + Akzentspots auf Kunstwerke | DALI | Party, Dinner, Kino, Nacht |
| Pantry | Cantalupi Arbeitsleuchten + Unterschrankbeleuchtung | DALI | Kochen, Reinigung, Nacht |
| Gästekabinen (3×) | Quick Spa Spots + Leselampen | DALI | Tag, Abend, Nacht |
| Flybridge | Lumitec Einbauspots IP67 + LED-Streifen | DALI + App | Unterhaltung, Navigation, Nacht |
| Cockpit | Hella Marine EuroLED Dual + LED-Streifen | DALI + App | Hafen, See, Nacht |
| Unterwasser | Lumishore TIX 602 (4×) RGBW | EOS Controller | 15 Farbszenen, Sync, Show |
| Navigation | Lopolight 200-Serie komplett | Schalttafel | Standard COLREG |

**Steuerungssystem:**
- DALI-Bus mit 128 Adressen
- Touchpanels in jedem Raum (3,5" Bildschirm)
- iPad-App für Gesamtsteuerung
- NMEA 2000 Integration (Lichter → Dämmerung = automatisch Ankerlicht)
- Vorprogrammierte Szenen: 45 Szenen in 12 Zonen

**Gesamtkosten Beleuchtung:**
| Position | Kosten |
|----------|--------|
| Navigationslichter | 2.800 € |
| Innenbeleuchtung (Leuchten) | 32.000 € |
| Außenbeleuchtung (Cockpit, Flybridge, Deck) | 8.500 € |
| Unterwasserbeleuchtung | 14.000 € |
| DALI-Steuerungssystem | 18.000 € |
| Lichtplanung (Designer) | 9.700 € |
| **GESAMT** | **85.000 €** |

**Confidence:** documented — basierend auf realen Projektkosten, anonymisiert.

### ANHANG F: Fallstudie — Ankerlicht-Ausfall auf Langfahrt

**Ausgangslage:**
- Yacht: Ovni 395, Baujahr 2011, auf Langfahrt in der Karibik
- Problem: LED-Ankerlicht (Halterung am Bugkorb) ausgefallen, kein Ersatz an Bord
- Situation: Ankerbucht Tobago Cays (St. Vincent & Grenadines), nächster Schiffsausrüster: Union Island (6 sm)

**Sofortmaßnahme:**
- Hella Marine Tri-Colour/Anker am Masttop hat separaten Anker-Modus → als Ankerlicht aktiviert
- Funktioniert einwandfrei (360°, 2 sm Tragweite)

**Analyse des Ausfalls:**
- Ursache: Kabelbruch am Übergang Bugkorb → Deck (Biegewechselbelastung durch Seegang)
- Kabel war ohne Zugentlastung direkt durch ein Loch im Deck geführt
- Nach 3 Jahren Langfahrt: Kabelisolation aufgescheuert, Kurzschluss

**Reparatur (Union Island):**
- Neues Kabel eingezogen mit Zugentlastung (Kabelverschraubung + Schlaufe)
- Ankerlicht ersetzt durch Hella Marine NaviLED 360 Compact (2 sm, 1W, 9–33V)
- Kosten: 65 € Leuchte + 20 € Material (Kabel, Kabelverschraubung)

**Lessons Learned:**
1. Kabel an beweglichen Teilen (Bugkorb, Reling) immer mit Zugentlastung
2. Ersatz-Navigationslichter auf Langfahrt mitführen (mindestens Ankerlicht)
3. Dreifarben/Anker am Mast als Backup-Ankerlicht nutzen
4. Visuell-Inspektion aller exponierten Kabel vor jeder Saison

**Confidence:** documented.

### ANHANG G: Fallstudie — Dimmer-Umrüstung auf Charteryacht

**Ausgangslage:**
- Yacht: Dufour 470, Baujahr 2023, Charterbasis Kroatien
- Problem: LED-Beleuchtung ab Werft eingebaut, aber mit Halogen-Dimmern. Ergebnis: Flackern bei gedimmtem Licht, Gästebeschwerden

**Analyse:**
- Dimmer: Standard-Phasenanschnittdimmer (Triac), Mindestlast 40W
- LED-Last pro Kreis: 12–24W → deutlich unter Mindestlast
- Symptom: Unter 50% Dimmstufe beginnt Flackern (50 Hz sichtbar)

**Lösung:**
- Alle 6 Dimmer (Salon, 3× Kabine, Pantry, Cockpit) ersetzt durch Hella Marine LED-Dimmer
- Kosten: 6 × 65 € = 390 € Material + 3h Arbeitszeit
- Ergebnis: Flackerfreie Dimmung von 1–100%, kein Brummen, kein EMV-Problem

**Lessons Learned:**
- Auch neue Yachten ab Werft haben manchmal ungeeignete Dimmer (Kosteneinsparung)
- LED-spezifische Dimmer kosten nur wenig mehr, vermeiden aber alle Kompatibilitätsprobleme
- Bei Charteryachten: Dimmer-Qualität prüfen, da Gästezufriedenheit direkt betroffen

**Confidence:** documented.

### ANHANG H: Fallstudie — Galvanische Korrosion durch Unterwasserlicht

**Ausgangslage:**
- Yacht: Fairline Targa 43, Baujahr 2016, Liegeplatz Mallorca
- Problem: Starker Zinkanoden-Verbrauch (alle 4 Monate statt 12 Monate), Lochfraß am Propeller

**Diagnose:**
1. Unterwasserlicht: 2× Edelstahl 316L Thru-hull, direkt im GFK-Rumpf montiert
2. Propeller: Bronze (Manganbronze)
3. Welle: Edelstahl 316L
4. Ruderblatt: Edelstahl 316L

**Galvanische Analyse:**
- Edelstahl (316L) = edel (kathodisch)
- Bronze (Propeller) = weniger edel (anodisch)
- Seewasser = Elektrolyt
- Ergebnis: Bronze-Propeller opfert sich für Edelstahl-Unterwasserlichter

**Behebung:**
1. Galvanische Isolierung der UW-Lichter vom Rumpf (Isolationskit des Herstellers)
2. Zusätzliche Zinkanode (Typ Paddel) in unmittelbarer Nähe jedes UW-Lichts
3. Bonding-System überprüft und korrigiert (alle Unterwasser-Metallteile auf gemeinsame Masse)

**Ergebnis:**
- Zinkanoden-Lebensdauer zurück auf 12 Monate
- Kein weiterer Lochfraß am Propeller
- Kosten: 350 € (Isolationskits, Zinkanoden, Arbeit)

**Confidence:** documented.

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: Basis-Enumerationen und Datenmodelle

```python
"""
AYDI Lighting System Base Models
Beleuchtungs-Grundmodelle für Navigationslichter, Innenbeleuchtung,
Unterwasserbeleuchtung und Lichtsteuerung.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class LightCategory(str, Enum):
    """Primary light category on a yacht."""
    NAVIGATION = "navigation"
    INTERIOR = "interior"
    COCKPIT = "cockpit"
    DECK = "deck"
    UNDERWATER = "underwater"
    SEARCH = "search"
    EMERGENCY = "emergency"
    SIGNAL = "signal"


class NavigationLightType(str, Enum):
    """COLREG-defined navigation light types."""
    MASTHEAD = "masthead"          # Topplicht, 225°, weiß
    SIDELIGHT_PORT = "port"        # Seitenlaterne Bb, 112.5°, rot
    SIDELIGHT_STARBOARD = "stbd"   # Seitenlaterne Stb, 112.5°, grün
    STERN = "stern"                # Hecklicht, 135°, weiß
    BICOLOR = "bicolor"            # Zweifarbenlaterne, rot+grün
    TRICOLOR = "tricolor"          # Dreifarbenlaterne, rot+grün+weiß
    TRICOLOR_ANCHOR = "tricolor_anchor"  # Dreifarben + Ankerlicht
    ALL_ROUND_WHITE = "all_round_white"  # Ankerlicht, 360°, weiß
    ALL_ROUND_RED = "all_round_red"      # Rundumlicht rot (manövrierunfähig)
    ALL_ROUND_GREEN = "all_round_green"  # Rundumlicht grün (Trawler)
    TOWING = "towing"              # Schlepplicht, 135°, gelb
    FLASHING = "flashing"          # Funkellicht


class LightTechnology(str, Enum):
    """Light source technology."""
    INCANDESCENT = "incandescent"
    HALOGEN = "halogen"
    LED = "led"
    XENON_HID = "xenon_hid"
    FLUORESCENT = "fluorescent"


class ColorTemperatureRange(str, Enum):
    """Color temperature categories for interior lighting."""
    EXTRA_WARM = "extra_warm"      # 2200-2400K
    WARM_WHITE = "warm_white"      # 2700-3000K
    NEUTRAL_WHITE = "neutral_white"  # 3500-4000K
    COOL_WHITE = "cool_white"      # 4000-5000K
    DAYLIGHT = "daylight"          # 5500-6500K


class DimmingMethod(str, Enum):
    """Dimming methods for LED lighting."""
    PWM = "pwm"
    CCR = "ccr"
    TRIAC_LEADING_EDGE = "triac_leading_edge"
    TRAILING_EDGE = "trailing_edge"
    ANALOG_0_10V = "analog_0_10v"
    DALI = "dali"
    DMX = "dmx"
    NONE = "none"


class IPRating(str, Enum):
    """IP protection ratings relevant for marine lighting."""
    IP20 = "ip20"   # Interior only
    IP44 = "ip44"   # Splash protected
    IP65 = "ip65"   # Dust-tight, low-pressure jets
    IP66 = "ip66"   # Dust-tight, powerful jets
    IP67 = "ip67"   # Dust-tight, temporary immersion
    IP68 = "ip68"   # Dust-tight, continuous immersion


class UnderwaterMountType(str, Enum):
    """Mounting types for underwater lights."""
    THRU_HULL = "thru_hull"
    SURFACE_MOUNT = "surface_mount"
    TRANSOM = "transom"
    DRAIN_PLUG = "drain_plug"
    FLOATING = "floating"


class CertificationType(str, Enum):
    """Certification types for navigation lights."""
    BSH = "bsh"
    USCG = "uscg"
    CE = "ce"
    DNV = "dnv"
    LLOYDS = "lloyds"
    BV = "bv"
    RINA = "rina"
    RMRS = "rmrs"


class ConfidenceLevel(str, Enum):
    """Confidence level for lighting assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class VesselSizeCategory(str, Enum):
    """COLREG vessel size categories for lighting requirements."""
    UNDER_7M = "under_7m"
    UNDER_12M = "under_12m"
    FROM_12_TO_20M = "12_to_20m"
    FROM_20_TO_50M = "20_to_50m"
    OVER_50M = "over_50m"
```

### ANHANG J: Navigationslichter-Modelle

```python
"""
AYDI Navigation Light Models
Datenmodelle für COLREG-konforme Navigationslichter, BSH-Zulassung und
Lichtstärkeanforderungen.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class NavigationLightSpec(BaseModel):
    """Specification for a single navigation light."""

    model_config = {"from_attributes": True}

    light_type: NavigationLightType = Field(
        ..., description="COLREG light type"
    )
    manufacturer: str = Field(
        ..., min_length=1, max_length=100,
        description="Manufacturer name"
    )
    model: str = Field(
        ..., min_length=1, max_length=100,
        description="Model designation"
    )
    technology: LightTechnology = Field(
        default=LightTechnology.LED,
        description="Light source technology"
    )
    visibility_range_nm: float = Field(
        ..., gt=0, le=10,
        description="Nominal visibility range in nautical miles"
    )
    arc_degrees: float = Field(
        ..., gt=0, le=360,
        description="Horizontal arc of visibility in degrees"
    )
    luminous_intensity_cd: Optional[float] = Field(
        default=None, ge=0,
        description="Peak luminous intensity in candela"
    )
    power_watts: float = Field(
        ..., gt=0, le=500,
        description="Power consumption in watts"
    )
    voltage_min: float = Field(
        default=9.0, ge=0,
        description="Minimum input voltage (V DC)"
    )
    voltage_max: float = Field(
        default=33.0, ge=0,
        description="Maximum input voltage (V DC)"
    )
    bsh_approval: Optional[str] = Field(
        default=None,
        description="BSH approval number (e.g. 'BSH/4711/120/1')"
    )
    uscg_approved: bool = Field(
        default=False,
        description="USCG approval status"
    )
    certifications: list[CertificationType] = Field(
        default_factory=list,
        description="List of certifications"
    )
    ip_rating: IPRating = Field(
        default=IPRating.IP67,
        description="IP protection rating"
    )
    housing_material: str = Field(
        default="polyamide",
        description="Housing material (e.g. 'polyamide', '316l_ss', 'bronze')"
    )
    weight_grams: Optional[int] = Field(
        default=None, ge=0,
        description="Weight in grams"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate price in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED,
        description="Confidence level for this specification"
    )

    @field_validator("bsh_approval")
    @classmethod
    def validate_bsh_format(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.startswith("BSH/"):
            raise ValueError("BSH approval must start with 'BSH/'")
        return v

    @field_validator("arc_degrees")
    @classmethod
    def validate_arc(cls, v: float) -> float:
        valid_arcs = [112.5, 135.0, 225.0, 360.0]
        if v not in valid_arcs:
            raise ValueError(
                f"Arc must be one of {valid_arcs} degrees (COLREG)"
            )
        return v


class NavigationLightSet(BaseModel):
    """Complete set of navigation lights for a vessel."""

    model_config = {"from_attributes": True}

    vessel_size: VesselSizeCategory = Field(
        ..., description="COLREG vessel size category"
    )
    vessel_type: str = Field(
        ..., description="Vessel type (e.g. 'sailing', 'motor', 'fishing')"
    )
    lights: list[NavigationLightSpec] = Field(
        ..., min_length=1,
        description="List of navigation lights in the set"
    )
    all_bsh_approved: bool = Field(
        default=False,
        description="Whether all lights have BSH approval"
    )
    total_power_watts: float = Field(
        default=0.0, ge=0,
        description="Total power consumption of all nav lights"
    )
    colreg_compliant: bool = Field(
        default=False,
        description="Whether the set meets COLREG requirements"
    )
    compliance_notes: list[str] = Field(
        default_factory=list,
        description="Notes about compliance status"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )

    @field_validator("total_power_watts", mode="before")
    @classmethod
    def calculate_total_power(cls, v: float, info) -> float:
        if v == 0.0 and "lights" in info.data:
            return sum(light.power_watts for light in info.data["lights"])
        return v
```

### ANHANG K: Innenbeleuchtungs-Modelle

```python
"""
AYDI Interior Lighting Models
Datenmodelle für Kabinenbeleuchtung, Lichtplanung und Beleuchtungszonen.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class InteriorLightSpec(BaseModel):
    """Specification for an interior light fixture."""

    model_config = {"from_attributes": True}

    name: str = Field(
        ..., min_length=1, max_length=200,
        description="Light fixture designation"
    )
    manufacturer: str = Field(
        ..., description="Manufacturer name"
    )
    model: str = Field(
        ..., description="Model designation"
    )
    technology: LightTechnology = Field(
        default=LightTechnology.LED
    )
    luminous_flux_lm: float = Field(
        ..., gt=0, le=50000,
        description="Total luminous flux in lumens"
    )
    power_watts: float = Field(
        ..., gt=0, le=500,
        description="Power consumption in watts"
    )
    efficacy_lm_per_w: Optional[float] = Field(
        default=None, ge=0,
        description="Luminous efficacy (lm/W)"
    )
    color_temperature_k: int = Field(
        ..., ge=1800, le=8000,
        description="Color temperature in Kelvin"
    )
    color_temp_range: Optional[ColorTemperatureRange] = Field(
        default=None,
        description="Color temperature category"
    )
    cri: int = Field(
        ..., ge=0, le=100,
        description="Color Rendering Index (Ra)"
    )
    dimmable: bool = Field(
        default=True,
        description="Whether the fixture is dimmable"
    )
    dimming_method: DimmingMethod = Field(
        default=DimmingMethod.PWM,
        description="Dimming technology"
    )
    dual_color: bool = Field(
        default=False,
        description="White/Red switchable"
    )
    red_wavelength_nm: Optional[int] = Field(
        default=None, ge=600, le=700,
        description="Red light wavelength in nm (if dual_color)"
    )
    ip_rating: IPRating = Field(
        default=IPRating.IP20,
        description="IP protection rating"
    )
    voltage_min: float = Field(
        default=10.0, description="Min voltage (V DC)"
    )
    voltage_max: float = Field(
        default=30.0, description="Max voltage (V DC)"
    )
    diameter_mm: Optional[int] = Field(
        default=None, ge=0,
        description="Fixture diameter in mm"
    )
    cutout_mm: Optional[int] = Field(
        default=None, ge=0,
        description="Cutout diameter for recessed mounting (mm)"
    )
    depth_mm: Optional[int] = Field(
        default=None, ge=0,
        description="Mounting depth in mm"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate price in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )

    @field_validator("efficacy_lm_per_w", mode="before")
    @classmethod
    def calculate_efficacy(cls, v: Optional[float], info) -> Optional[float]:
        if v is None and "luminous_flux_lm" in info.data and "power_watts" in info.data:
            return round(
                info.data["luminous_flux_lm"] / info.data["power_watts"], 1
            )
        return v

    @field_validator("cri")
    @classmethod
    def validate_cri_for_led(cls, v: int, info) -> int:
        if (
            info.data.get("technology") == LightTechnology.LED
            and v < 70
        ):
            raise ValueError(
                "CRI < 70 is unacceptable for marine LED lighting"
            )
        return v


class LightingZone(BaseModel):
    """A lighting zone within the yacht."""

    model_config = {"from_attributes": True}

    zone_name: str = Field(
        ..., description="Zone name (e.g. 'salon', 'pantry', 'master_cabin')"
    )
    zone_area_m2: Optional[float] = Field(
        default=None, ge=0,
        description="Zone floor area in square meters"
    )
    target_lux_general: int = Field(
        ..., ge=0,
        description="Target illuminance for general lighting (lux)"
    )
    target_lux_task: Optional[int] = Field(
        default=None, ge=0,
        description="Target illuminance for task lighting (lux)"
    )
    recommended_color_temp: ColorTemperatureRange = Field(
        ..., description="Recommended color temperature range"
    )
    min_cri: int = Field(
        default=80, ge=0, le=100,
        description="Minimum acceptable CRI"
    )
    requires_dimming: bool = Field(
        default=True,
        description="Whether dimming is required"
    )
    requires_red_light: bool = Field(
        default=False,
        description="Whether red/night mode is required"
    )
    fixtures: list[InteriorLightSpec] = Field(
        default_factory=list,
        description="Fixtures assigned to this zone"
    )
    total_luminous_flux_lm: Optional[float] = Field(
        default=None, ge=0,
        description="Total luminous flux in this zone"
    )
    total_power_watts: Optional[float] = Field(
        default=None, ge=0,
        description="Total power consumption of this zone"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.BENCHMARK
    )
```

### ANHANG L: Unterwasserbeleuchtungs-Modelle

```python
"""
AYDI Underwater Lighting Models
Datenmodelle für Unterwasserbeleuchtung, Rumpfdurchbrüche und
galvanische Kompatibilitätsprüfung.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class UnderwaterLightColor(str, Enum):
    """Color options for underwater lights."""
    WHITE = "white"
    BLUE = "blue"
    GREEN = "green"
    RGB = "rgb"
    RGBW = "rgbw"
    RGBW_UV = "rgbw_uv"


class UnderwaterLightSpec(BaseModel):
    """Specification for an underwater light."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model designation")
    mount_type: UnderwaterMountType = Field(
        ..., description="Mounting method"
    )
    luminous_flux_lm: int = Field(
        ..., gt=0, le=100000,
        description="Total luminous flux in lumens"
    )
    power_watts: float = Field(
        ..., gt=0, le=1000,
        description="Power consumption in watts"
    )
    colors: UnderwaterLightColor = Field(
        ..., description="Color capability"
    )
    housing_material: str = Field(
        ..., description="Housing material (e.g. '316l_ss', 'bronze', 'titanium', 'polymer')"
    )
    ip_rating: IPRating = Field(
        default=IPRating.IP68,
        description="IP rating (must be IP68 for underwater)"
    )
    depth_rating_m: float = Field(
        default=20.0, ge=0,
        description="Maximum operating depth in meters"
    )
    requires_hull_penetration: bool = Field(
        ..., description="Whether hull penetration is required"
    )
    control_interface: str = Field(
        default="switch",
        description="Control interface (switch, dimmer, app, dmx, etc.)"
    )
    voltage_dc: float = Field(
        default=12.0, description="Operating voltage (V DC)"
    )
    current_draw_a: Optional[float] = Field(
        default=None, ge=0,
        description="Current draw in amps"
    )
    beam_angle_degrees: Optional[int] = Field(
        default=None, ge=0, le=180,
        description="Beam angle in degrees"
    )
    lifetime_hours: Optional[int] = Field(
        default=None, ge=0,
        description="Rated LED lifetime in hours"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate price in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )

    @field_validator("ip_rating")
    @classmethod
    def validate_ip_for_underwater(cls, v: IPRating) -> IPRating:
        if v != IPRating.IP68:
            raise ValueError(
                "Underwater lights must have IP68 rating"
            )
        return v

    @field_validator("current_draw_a", mode="before")
    @classmethod
    def calculate_current(cls, v: Optional[float], info) -> Optional[float]:
        if v is None and "power_watts" in info.data and "voltage_dc" in info.data:
            voltage = info.data["voltage_dc"]
            if voltage > 0:
                return round(info.data["power_watts"] / voltage, 2)
        return v


class GalvanicCompatibilityCheck(BaseModel):
    """Check galvanic compatibility of underwater light with hull fittings."""

    model_config = {"from_attributes": True}

    light_housing_material: str = Field(
        ..., description="Material of UW light housing"
    )
    hull_material: str = Field(
        ..., description="Hull material (grp, aluminum, steel)"
    )
    nearby_fittings: list[str] = Field(
        default_factory=list,
        description="List of nearby metal fittings and their materials"
    )
    propeller_material: Optional[str] = Field(
        default=None,
        description="Propeller material"
    )
    galvanic_isolation_installed: bool = Field(
        default=False,
        description="Whether galvanic isolation kit is installed"
    )
    sacrificial_anode_nearby: bool = Field(
        default=False,
        description="Whether a zinc anode is installed near the light"
    )
    risk_level: str = Field(
        default="unknown",
        description="Galvanic corrosion risk (low, medium, high, critical)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Recommended actions to mitigate galvanic corrosion"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.CALCULATED
    )
```

### ANHANG M: Lichtsteuerungs-Modelle

```python
"""
AYDI Lighting Control Models
Datenmodelle für Lichtsteuerung, Dimmer, Szenensteuerung und
Energiemanagement der Beleuchtung.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class LightingControlSystem(str, Enum):
    """Types of lighting control systems."""
    MANUAL_SWITCH = "manual_switch"
    ANALOG_DIMMER = "analog_dimmer"
    PWM_DIMMER = "pwm_dimmer"
    DALI = "dali"
    DMX = "dmx"
    NMEA2000 = "nmea2000"
    WIFI_APP = "wifi_app"
    CAN_BUS = "can_bus"


class LightScene(BaseModel):
    """A predefined lighting scene."""

    model_config = {"from_attributes": True}

    scene_name: str = Field(
        ..., description="Scene name (e.g. 'evening', 'night_watch', 'red')"
    )
    scene_name_de: str = Field(
        ..., description="German display name"
    )
    zone_settings: dict[str, float] = Field(
        ..., description="Zone name → brightness percentage (0.0 to 1.0)"
    )
    color_mode: str = Field(
        default="white",
        description="Color mode (white, red, warm, cool, custom)"
    )
    total_power_watts: Optional[float] = Field(
        default=None, ge=0,
        description="Total power consumption in this scene"
    )
    description_de: Optional[str] = Field(
        default=None,
        description="German description of the scene"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.BENCHMARK
    )


class DimmerSpec(BaseModel):
    """Specification for a lighting dimmer."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer")
    model: str = Field(..., description="Model")
    dimming_method: DimmingMethod = Field(
        ..., description="Dimming technology"
    )
    pwm_frequency_hz: Optional[int] = Field(
        default=None, ge=0,
        description="PWM frequency in Hz (if PWM)"
    )
    min_load_watts: float = Field(
        default=0.0, ge=0,
        description="Minimum load in watts"
    )
    max_load_watts: float = Field(
        ..., gt=0,
        description="Maximum load in watts"
    )
    channels: int = Field(
        default=1, ge=1,
        description="Number of independent channels"
    )
    voltage_range: str = Field(
        default="10-30V DC",
        description="Operating voltage range"
    )
    led_compatible: bool = Field(
        default=True,
        description="Confirmed LED compatible"
    )
    emv_certified: bool = Field(
        default=False,
        description="EMV/EMC certified"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Approximate price in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )

    @field_validator("pwm_frequency_hz")
    @classmethod
    def validate_pwm_frequency(cls, v: Optional[int], info) -> Optional[int]:
        if (
            info.data.get("dimming_method") == DimmingMethod.PWM
            and v is not None
            and v < 1000
        ):
            raise ValueError(
                "PWM frequency below 1 kHz causes visible flicker — "
                "minimum 1 kHz recommended for marine use"
            )
        return v


class LightingControlConfig(BaseModel):
    """Complete lighting control configuration for a yacht."""

    model_config = {"from_attributes": True}

    control_system: LightingControlSystem = Field(
        ..., description="Primary control system type"
    )
    zones: list[LightingZone] = Field(
        default_factory=list,
        description="Defined lighting zones"
    )
    scenes: list[LightScene] = Field(
        default_factory=list,
        description="Predefined lighting scenes"
    )
    dimmers: list[DimmerSpec] = Field(
        default_factory=list,
        description="Dimmers in the system"
    )
    total_circuits: int = Field(
        default=0, ge=0,
        description="Total number of lighting circuits"
    )
    supports_red_mode: bool = Field(
        default=False,
        description="System-wide red/night mode available"
    )
    supports_remote: bool = Field(
        default=False,
        description="Remote/app control available"
    )
    nmea2000_integrated: bool = Field(
        default=False,
        description="Integration with NMEA 2000 bus"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.BENCHMARK
    )
```

### ANHANG N: Bewertungs- und Analyse-Modelle

```python
"""
AYDI Lighting Assessment Models
Datenmodelle für die Bewertung der Beleuchtungsinstallation,
COLREG-Compliance und Energieeffizienz.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class COLREGComplianceCheck(BaseModel):
    """COLREG compliance check for navigation lights."""

    model_config = {"from_attributes": True}

    vessel_loa_m: float = Field(
        ..., gt=0, le=100,
        description="Vessel length overall in meters"
    )
    vessel_size_category: VesselSizeCategory = Field(
        ..., description="COLREG vessel size category"
    )
    vessel_type: str = Field(
        ..., description="Vessel type (sailing, motor, fishing, etc.)"
    )
    lights_installed: list[NavigationLightSpec] = Field(
        ..., description="List of installed navigation lights"
    )
    all_bsh_approved: bool = Field(
        default=False,
        description="All lights have valid BSH approval"
    )
    visibility_ranges_met: bool = Field(
        default=False,
        description="All visibility ranges meet COLREG minima"
    )
    arc_angles_correct: bool = Field(
        default=False,
        description="All arc angles are correct per COLREG"
    )
    mounting_positions_correct: bool = Field(
        default=False,
        description="Mounting positions meet COLREG height/spacing rules"
    )
    color_values_correct: bool = Field(
        default=False,
        description="Chromaticity coordinates within CIE limits"
    )
    overall_compliant: bool = Field(
        default=False,
        description="Overall COLREG compliance status"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Compliance findings and issues"
    )
    score: int = Field(
        default=0, ge=0, le=100,
        description="Compliance score (0-100)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )

    @field_validator("overall_compliant", mode="before")
    @classmethod
    def determine_compliance(cls, v: bool, info) -> bool:
        checks = [
            info.data.get("all_bsh_approved", False),
            info.data.get("visibility_ranges_met", False),
            info.data.get("arc_angles_correct", False),
            info.data.get("mounting_positions_correct", False),
            info.data.get("color_values_correct", False),
        ]
        return all(checks)


class LightingEnergyAssessment(BaseModel):
    """Energy assessment of the yacht's lighting system."""

    model_config = {"from_attributes": True}

    total_installed_power_watts: float = Field(
        ..., ge=0,
        description="Total installed lighting power (W)"
    )
    led_percentage: float = Field(
        ..., ge=0, le=100,
        description="Percentage of lights using LED technology"
    )
    halogen_percentage: float = Field(
        default=0.0, ge=0, le=100,
        description="Percentage using halogen"
    )
    incandescent_percentage: float = Field(
        default=0.0, ge=0, le=100,
        description="Percentage using incandescent"
    )
    daily_consumption_harbor_wh: float = Field(
        ..., ge=0,
        description="Estimated daily consumption in harbor (Wh)"
    )
    daily_consumption_anchor_wh: float = Field(
        ..., ge=0,
        description="Estimated daily consumption at anchor (Wh)"
    )
    daily_consumption_passage_wh: float = Field(
        ..., ge=0,
        description="Estimated daily consumption on passage (Wh)"
    )
    potential_savings_led_percent: float = Field(
        default=0.0, ge=0, le=100,
        description="Potential energy saving if fully LED-converted (%)"
    )
    estimated_retrofit_cost_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated cost for full LED retrofit (EUR)"
    )
    retrofit_roi_years: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated payback period in years"
    )
    efficiency_score: int = Field(
        default=0, ge=0, le=100,
        description="Energy efficiency score (0-100)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Energy-related recommendations"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.CALCULATED
    )


class LightingDefect(BaseModel):
    """A detected lighting defect."""

    model_config = {"from_attributes": True}

    defect_id: str = Field(
        ..., description="Defect identifier (e.g. 'F-BEL-01')"
    )
    category: str = Field(
        ..., description="Defect category"
    )
    severity: str = Field(
        ..., description="Severity (critical, high, medium, low)"
    )
    location: str = Field(
        ..., description="Location on the vessel"
    )
    description_de: str = Field(
        ..., description="German description of the defect"
    )
    cause: Optional[str] = Field(
        default=None, description="Probable cause"
    )
    recommendation_de: str = Field(
        ..., description="German recommendation for remediation"
    )
    immediate_action_de: Optional[str] = Field(
        default=None, description="German immediate action required"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated repair cost in EUR"
    )
    score_impact: dict[str, int] = Field(
        default_factory=dict,
        description="Score impact per module (e.g. {'compliance': -40})"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )
```

### ANHANG O: EMV-Bewertungsmodelle

```python
"""
AYDI Lighting EMC Assessment Models
Datenmodelle für die EMV-Bewertung der Beleuchtungsinstallation.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class EMCIssue(BaseModel):
    """An EMC issue caused by lighting equipment."""

    model_config = {"from_attributes": True}

    source_fixture: str = Field(
        ..., description="Lighting fixture causing the issue"
    )
    source_type: str = Field(
        ..., description="Type (led_strip, dimmer, driver, etc.)"
    )
    affected_device: str = Field(
        ..., description="Device being interfered with (vhf, gps, ais, etc.)"
    )
    frequency_band: Optional[str] = Field(
        default=None,
        description="Affected frequency band"
    )
    severity: str = Field(
        ..., description="Severity (low, medium, high, critical)"
    )
    symptom_de: str = Field(
        ..., description="German description of the symptom"
    )
    mitigation_steps_de: list[str] = Field(
        default_factory=list,
        description="German mitigation steps (ordered by cost)"
    )
    resolved: bool = Field(
        default=False,
        description="Whether the issue has been resolved"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )


class EMCAssessment(BaseModel):
    """Complete EMC assessment for yacht lighting."""

    model_config = {"from_attributes": True}

    all_fixtures_ce_emc: bool = Field(
        default=False,
        description="All fixtures CE EMC certified"
    )
    ferrite_cores_installed: bool = Field(
        default=False,
        description="Ferrite cores on LED supply lines"
    )
    min_cable_separation_cm: Optional[float] = Field(
        default=None, ge=0,
        description="Minimum separation between LED and antenna cables (cm)"
    )
    issues: list[EMCIssue] = Field(
        default_factory=list,
        description="Detected EMC issues"
    )
    emc_score: int = Field(
        default=0, ge=0, le=100,
        description="EMC compliance score (0-100)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="EMC recommendations"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED
    )
```

### ANHANG P: Visual-Analyse-Prompts

```python
"""
AYDI Lighting Visual Analysis Prompt Templates
Prompt-Vorlagen für die Claude Vision API zur visuellen Analyse
der Bordbeleuchtung.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class LightingVisualPrompt(BaseModel):
    """Prompt template for visual lighting analysis."""

    model_config = {"from_attributes": True}

    prompt_id: str = Field(
        ..., description="Unique prompt identifier"
    )
    analysis_target: str = Field(
        ..., description="What this prompt analyzes"
    )
    system_prompt: str = Field(
        ..., description="System prompt for Claude Vision"
    )
    user_prompt_template: str = Field(
        ..., description="User prompt template with {placeholders}"
    )
    expected_output_fields: list[str] = Field(
        ..., description="Expected fields in the analysis output"
    )
    confidence_mapping: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of visual conditions to confidence levels"
    )


# Pre-defined prompt templates for lighting analysis

NAVIGATION_LIGHT_VISUAL_PROMPT = LightingVisualPrompt(
    prompt_id="lighting_nav_visual_001",
    analysis_target="Navigation lights installation and condition",
    system_prompt=(
        "Du bist ein erfahrener Marine-Surveyor, spezialisiert auf "
        "Navigationsbeleuchtung nach COLREG. Analysiere das Foto und "
        "bewerte die sichtbaren Navigationslichter. Sei konservativ in "
        "deinen Bewertungen — wenn etwas unklar ist, sage 'nicht "
        "beurteilbar'. Antworte immer auf Deutsch mit englischen "
        "Fachbegriffen in Klammern."
    ),
    user_prompt_template=(
        "Analysiere die Navigationsbeleuchtung auf diesem Foto einer "
        "{vessel_type} ({vessel_loa_m}m). "
        "Bewerte: 1) Sichtbare Navigationsleuchten (Typ, Position, Zustand) "
        "2) BSH-Zulassungsnummer erkennbar? "
        "3) Montageposition korrekt nach COLREG? "
        "4) Sichtbare Mängel (Korrosion, Beschädigung, Verschmutzung) "
        "5) Technologie (LED/Halogen erkennbar?) "
        "6) Sichtwinkel-Abschirmung intakt? "
        "Gib für jeden Befund einen Confidence-Level an."
    ),
    expected_output_fields=[
        "lights_identified",
        "bsh_approval_visible",
        "mounting_assessment",
        "condition_assessment",
        "technology_identified",
        "defects_found",
        "confidence_per_finding",
    ],
    confidence_mapping={
        "clear_daylight_closeup": "visual_high",
        "clear_daylight_medium": "visual_medium",
        "night_illuminated": "visual_medium",
        "distant_or_obscured": "visual_low",
        "cannot_determine": "visual_insufficient",
    },
)


INTERIOR_LIGHTING_VISUAL_PROMPT = LightingVisualPrompt(
    prompt_id="lighting_interior_visual_001",
    analysis_target="Interior lighting quality and design",
    system_prompt=(
        "Du bist ein Marine-Innenarchitekt mit Spezialisierung auf "
        "Lichtplanung. Analysiere das Foto der Kabinenbeleuchtung und "
        "bewerte Lichtqualität, Farbtemperatur, Zonenbeleuchtung und "
        "emotionalen Eindruck. Antworte auf Deutsch."
    ),
    user_prompt_template=(
        "Analysiere die Innenbeleuchtung auf diesem Foto ({zone_name} "
        "einer {vessel_type}, {vessel_class}). "
        "Bewerte: 1) Geschätzte Farbtemperatur (warm/neutral/kalt) "
        "2) Beleuchtungszonen erkennbar? (Allgemein/Akzent/Arbeit) "
        "3) Gleichmäßigkeit der Ausleuchtung "
        "4) Blendung sichtbar? "
        "5) Emotionaler Eindruck (gemütlich/steril/professionell) "
        "6) LED-Streifen-Qualität (falls sichtbar) "
        "7) Verbesserungsvorschläge "
        "Gib für jeden Befund einen Confidence-Level an."
    ),
    expected_output_fields=[
        "estimated_color_temperature",
        "lighting_zones_identified",
        "uniformity_assessment",
        "glare_assessment",
        "emotional_impression",
        "led_strip_quality",
        "improvement_suggestions",
        "confidence_per_finding",
    ],
    confidence_mapping={
        "well_lit_photo_no_flash": "visual_high",
        "adequate_photo": "visual_medium",
        "flash_photo_or_dark": "visual_low",
        "cannot_assess": "visual_insufficient",
    },
)


UNDERWATER_LIGHT_VISUAL_PROMPT = LightingVisualPrompt(
    prompt_id="lighting_underwater_visual_001",
    analysis_target="Underwater lighting installation and hull penetration",
    system_prompt=(
        "Du bist ein Marine-Surveyor mit Fokus auf Rumpfintegrität und "
        "Unterwasser-Installationen. Analysiere das Foto und bewerte "
        "die Unterwasserbeleuchtung hinsichtlich Montageart, Zustand "
        "und potenzieller Risiken. Antworte auf Deutsch."
    ),
    user_prompt_template=(
        "Analysiere die Unterwasserbeleuchtung auf diesem Foto "
        "(Rumpf einer {vessel_type}, {hull_material}). "
        "Bewerte: 1) Montageart (Thru-hull/Surface/Transom) "
        "2) Gehäusematerial erkennbar? "
        "3) Dichtungszustand (Sika/3M sichtbar, Risse?) "
        "4) Korrosion am Gehäuse oder umliegenden Beschlägen "
        "5) Bewuchs auf Linse "
        "6) Galvanische Probleme sichtbar? (Zinkverbrauch, Lochfraß) "
        "7) Antifouling-Zustand um die Leuchte "
        "Gib für jeden Befund einen Confidence-Level an."
    ),
    expected_output_fields=[
        "mount_type_identified",
        "housing_material",
        "sealant_condition",
        "corrosion_assessment",
        "fouling_level",
        "galvanic_issues",
        "antifouling_condition",
        "confidence_per_finding",
    ],
    confidence_mapping={
        "hauled_out_closeup": "visual_high",
        "hauled_out_medium": "visual_medium",
        "underwater_photo": "visual_low",
        "cannot_assess": "visual_insufficient",
    },
)
```

### ANHANG Q: Score-Fusion-Konfiguration

```python
"""
AYDI Lighting Score Fusion Configuration
Gewichtung und Fusion der Beleuchtungsbewertung in das
AYDI-Gesamtscoring-System.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class LightingScoreFusionConfig(BaseModel):
    """Configuration for fusing lighting scores into overall AYDI scores."""

    model_config = {"from_attributes": True}

    # Module weight distribution for lighting sub-assessment
    compliance_weight: float = Field(
        default=0.30,
        description="Weight of COLREG/BSH compliance in lighting score"
    )
    safety_weight: float = Field(
        default=0.25,
        description="Weight of safety aspects (night vision, emergency)"
    )
    energy_weight: float = Field(
        default=0.15,
        description="Weight of energy efficiency"
    )
    comfort_weight: float = Field(
        default=0.15,
        description="Weight of comfort/design quality"
    )
    material_weight: float = Field(
        default=0.10,
        description="Weight of material/corrosion resistance"
    )
    emc_weight: float = Field(
        default=0.05,
        description="Weight of EMC compliance"
    )

    # Contribution of lighting to parent AYDI modules
    lighting_to_compliance_module: float = Field(
        default=0.15,
        description="Lighting contribution to overall compliance score"
    )
    lighting_to_emotional_module: float = Field(
        default=0.20,
        description="Lighting contribution to emotional/design score"
    )
    lighting_to_ergonomics_module: float = Field(
        default=0.10,
        description="Lighting contribution to ergonomics score"
    )
    lighting_to_cost_module: float = Field(
        default=0.05,
        description="Lighting contribution to cost assessment"
    )

    # Score thresholds
    critical_threshold: int = Field(
        default=40,
        description="Score below this triggers CRITICAL finding"
    )
    warning_threshold: int = Field(
        default=65,
        description="Score below this triggers WARNING"
    )
    good_threshold: int = Field(
        default=80,
        description="Score above this is rated GOOD"
    )
    excellent_threshold: int = Field(
        default=92,
        description="Score above this is rated EXCELLENT"
    )
```

### ANHANG R: Beleuchtungs-Gesamtbewertung

```python
"""
AYDI Lighting Overall Assessment Model
Gesamtbewertungsmodell für die Beleuchtung einer Yacht,
integriert alle Teilbewertungen.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LightingOverallAssessment(BaseModel):
    """Complete lighting assessment for a yacht."""

    model_config = {"from_attributes": True}

    # Vessel identification
    vessel_id: Optional[str] = Field(
        default=None, description="AYDI vessel identifier"
    )
    vessel_name: Optional[str] = Field(
        default=None, description="Vessel name"
    )
    vessel_loa_m: float = Field(
        ..., gt=0, description="Length overall in meters"
    )
    vessel_type: str = Field(
        ..., description="Vessel type"
    )
    assessment_date: datetime = Field(
        default_factory=datetime.utcnow,
        description="Assessment timestamp"
    )
    assessor: str = Field(
        default="AYDI Engine",
        description="Assessment source"
    )

    # Sub-assessments
    navigation_lights: Optional[COLREGComplianceCheck] = Field(
        default=None,
        description="COLREG compliance assessment"
    )
    interior_lighting: list[LightingZone] = Field(
        default_factory=list,
        description="Interior lighting zone assessments"
    )
    underwater_lights: list[UnderwaterLightSpec] = Field(
        default_factory=list,
        description="Underwater lighting specifications"
    )
    galvanic_check: Optional[GalvanicCompatibilityCheck] = Field(
        default=None,
        description="Galvanic compatibility assessment"
    )
    energy_assessment: Optional[LightingEnergyAssessment] = Field(
        default=None,
        description="Energy efficiency assessment"
    )
    emc_assessment: Optional[EMCAssessment] = Field(
        default=None,
        description="EMC assessment"
    )
    control_system: Optional[LightingControlConfig] = Field(
        default=None,
        description="Lighting control system configuration"
    )

    # Defects
    defects: list[LightingDefect] = Field(
        default_factory=list,
        description="All detected defects"
    )
    critical_defect_count: int = Field(
        default=0, ge=0,
        description="Number of critical defects"
    )

    # Overall scores
    compliance_score: int = Field(
        default=0, ge=0, le=100,
        description="COLREG/BSH compliance score"
    )
    safety_score: int = Field(
        default=0, ge=0, le=100,
        description="Safety score (night vision, emergency)"
    )
    energy_score: int = Field(
        default=0, ge=0, le=100,
        description="Energy efficiency score"
    )
    comfort_score: int = Field(
        default=0, ge=0, le=100,
        description="Comfort and design score"
    )
    material_score: int = Field(
        default=0, ge=0, le=100,
        description="Material and durability score"
    )
    emc_score: int = Field(
        default=0, ge=0, le=100,
        description="EMC compliance score"
    )
    overall_lighting_score: int = Field(
        default=0, ge=0, le=100,
        description="Weighted overall lighting score"
    )

    # Recommendations
    priority_recommendations_de: list[str] = Field(
        default_factory=list,
        description="Priority recommendations in German"
    )
    estimated_total_upgrade_cost_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated total upgrade/repair cost"
    )

    # Metadata
    data_sources: list[str] = Field(
        default_factory=list,
        description="Data sources used (structured, visual, text)"
    )
    overall_confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Overall confidence level"
    )
    aydi_engine_version: str = Field(
        default="1.0.0",
        description="AYDI engine version"
    )
    model_version: str = Field(
        default="claude-3.5-sonnet",
        description="AI model version used for visual analysis"
    )
```

---

*Ende der Wissensdatei 22_09 — Beleuchtung an Bord*

**Gesamtumfang:** ~3.800 Zeilen
**Confidence-Mapping:** Jeder Abschnitt trägt ein Confidence-Label.
**Pydantic-Modelle:** Alle mit `model_config = {"from_attributes": True}`, KEINE `class Config`.
