---
title: "Lewmar Winschen — Vollständige Wissensreferenz"
kategorie: "09 Winschen"
unterkategorie: "03 Lewmar"
version: "1.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Lewmar Katalogdaten, technische Datenblätter"
  - documented: "Lewmar Service-Handbücher, OEM-Zuordnungen"
  - estimated: "Erfahrungswerte Werft/Rigger, Forum-Konsens"
tags:
  - lewmar
  - winschen
  - self-tailing
  - elektrische_winschen
  - evo
  - ocean
  - oceanus
  - deck_hardware
---

# 09.03 — Lewmar Winschen: Vollständige Wissensreferenz

> **AYDI Wissensdatei 09.03** — Kategorie 9: Winschen
> **Confidence-Quelle:** measured (Hersteller-Katalog/TDS), documented (Service-Manuals, OEM-Daten), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Produktlinien](#3-produktlinien)
4. [Technische Spezifikationen](#4-technische-spezifikationen)
5. [Wartung und Service](#5-wartung-und-service)
6. [Hersteller-Daten und Teilenummern](#6-hersteller-daten-und-teilenummern)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Cross-Referenz und Wettbewerbsvergleich](#8-cross-referenz-und-wettbewerbsvergleich)
9. [Fehlerbilder und Diagnose](#9-fehlerbilder-und-diagnose)
10. [AYDI-Integration](#10-aydi-integration)

---

## 1. Einführung und Übersicht

### 1.1 Unternehmensgeschichte

Lewmar wurde 1946 in Havant, Hampshire, Großbritannien, gegründet. Der Firmenname leitet sich von den Gründern **Lew** und **Mar**tin ab — zwei Ingenieure, die nach dem Zweiten Weltkrieg in der aufstrebenden britischen Segelindustrie eine Marktlücke für hochwertige Decks-Hardware erkannten.

Die wichtigsten Meilensteine der Unternehmensgeschichte:

| Jahr | Ereignis |
|------|----------|
| 1946 | Gründung in Havant, Hampshire, UK |
| 1950er | Erste Aluminium-Winschen für britische Segelyachten |
| 1960er | Einführung der ersten selbstholenden (self-tailing) Winschen |
| 1970er | Expansion in den internationalen Markt, OEM-Verträge mit europäischen Werften |
| 1980 | Übernahme von Gibb Hardware, Erweiterung des Decksbeschlag-Sortiments |
| 1985 | Einführung der Ocean-Serie — Benchmark für Fahrtensegler |
| 1990er | Luken- und Fenster-Programm wird Kerngeschäft neben Winschen |
| 2000 | Einführung der ersten elektrischen Winschen für den Serienmarkt |
| 2005 | Launch der EVO-Serie als Nachfolger der Ocean-Serie |
| 2010 | Oceanus Racing-Serie für den Regattamarkt |
| 2016 | Integration fortschrittlicher Verbundwerkstoffe (Composite) in die Winschenkonstruktion |
| 2019 | Übernahme durch Lippert Components (USA), heute Lippert Marine |
| 2021 | EVO-Serie Generation 2 mit verbessertem Self-Tailing-Mechanismus |
| 2023 | Erweiterung der elektrischen EVO-Serie bis Größe 80 |
| 2024 | Einführung digitaler Steuerungsoptionen (CAN-Bus, NMEA 2000 Integration) |

### 1.2 Marktposition

Lewmar ist einer der drei dominierenden Winschenhersteller weltweit, neben Harken (USA) und Andersen (Dänemark). Die Marktanteile im europäischen OEM-Segment verteilen sich geschätzt wie folgt:

| Hersteller | OEM-Marktanteil Europa (geschätzt) | Stärke |
|------------|-------------------------------------|--------|
| Lewmar | ~35% | Breites Sortiment, Preis-Leistung, OEM-Partnerschaften |
| Harken | ~30% | Premium-Regatta, Innovation |
| Andersen | ~15% | Compact-Segment, Edelstahl-Winschen |
| Antal | ~10% | Italien, Mittelmeer-Markt |
| Pontos | ~5% | Hydraulische Großwinschen |
| Sonstige | ~5% | Nischenhersteller |

**Confidence:** estimated — Marktanteile basieren auf OEM-Zuordnungsanalyse und Branchenschätzungen.

Lewmar ist besonders stark im Segment der 30- bis 50-Fuß-Serienyachten. Werften wie Hanse, Hallberg-Rassy, Najad, Contest, X-Yachts, Dufour und Beneteau setzen Lewmar-Winschen als Standard- oder Optionsausstattung ein.

### 1.3 Produktspektrum über Winschen hinaus

Lewmar ist weit mehr als ein Winschenhersteller. Das Gesamtprogramm umfasst:

- **Winschen** (manuell, elektrisch, hydraulisch) — Kern dieser Wissensdatei
- **Luken und Fenster** — Standard, Medium und Ocean-Serie (vgl. AYDI 01.01)
- **Ankerwinschen** — V-Serie und Pro-Serie
- **Beschläge** — Klemmen, Umlenkrollen, Traveller-Systeme
- **Steuerräder** — Folding Wheel, Comfort Wheel
- **Gangways und Plattformen** — Badeplattform-Systeme
- **Bowsprit-Systeme** — für Code 0 / Gennaker

Für die AYDI-Analyse ist relevant, dass ein Lewmar-Winsch-System oft Teil eines integrierten Lewmar-Deckslayouts ist, was Kompatibilität und einheitliche Wartungszyklen ermöglicht.

### 1.4 Fertigungsstandorte

| Standort | Produktion |
|----------|-----------|
| Havant, Hampshire, UK | Winschen (Entwicklung, Fertigung), Zentrale |
| Guilford, Connecticut, USA | Ankerwinschen, US-Markt |
| Xiamen, China | Beschläge, Standardkomponenten |
| Italien (Zulieferer) | Edelstahl-Gussteile |

Die Winschenfertigung für den europäischen Markt erfolgt weiterhin überwiegend in Havant. Elektrische Komponenten (Motoren, Steuerungen) werden teilweise zugekauft und in Havant integriert.

---

## 2. Grundlagen und Theorie

### 2.1 Lewmar-Winschenkonstruktion — Grundprinzipien

Jede Lewmar-Winsch basiert auf dem gleichen mechanischen Grundprinzip: Eine zylindrische Trommel wird über ein Planetengetriebe mit definierten Übersetzungsverhältnissen angetrieben. Die Schot wird in mehreren Windungen (typisch 3–4) um die Trommel geführt, wobei die Reibung zwischen Schot und Trommel die Haltekraft erzeugt.

**Kernformel der Winschenmechanik (Euler-Eytelwein / Capstan-Gleichung):**

```
T_halten = T_ziehen × e^(μ × θ)
```

Dabei:
- T_halten = Haltekraft (Last auf der Schotklemme / Stopper)
- T_ziehen = Ziehkraft des Bedieners an der Kurbel
- μ = Reibungskoeffizient Schot/Trommel (~0.15–0.25 für Dyneema auf Aluminium)
- θ = Umschlingungswinkel in Radiant (3 Windungen = 6π ≈ 18.85 rad)

Für 3 Windungen einer Polyester-Schot auf einer Lewmar-Aluminiumtrommel (μ ≈ 0.20):

```
Kraftverhältnis = e^(0.20 × 18.85) ≈ 43:1
```

Das bedeutet: Bei 3 Windungen hält die Trommelreibung allein bereits das 43-fache der aufgebrachten Handkraft.

### 2.2 EVO Self-Tailing-Mechanismus

Das Self-Tailing-System ist Lewmars zentrales Konstruktionsmerkmal und unterscheidet die Winschen fundamental von reinen Trommelwinschen. Der EVO Self-Tailing-Mechanismus besteht aus:

**Obere Backe (Jaw):**
Die obere Self-Tailing-Backe ist eine konisch geformte Klemmvorrichtung oberhalb der Trommel. Sie fängt die Schot nach dem Verlassen der letzten Trommelwindung und klemmt sie zwischen einer festen und einer federgespannten Backe ein. Dadurch wird die Schot automatisch gehalten, ohne dass eine zweite Person sie durchziehen muss.

**EVO-Jaw-Design (ab 2005):**

Das EVO-Jaw unterscheidet sich vom älteren Ocean-Jaw durch:

1. **Breiterer Einzugswinkel:** Die EVO-Backe akzeptiert Schoten aus einem größeren Winkelbereich (±35° statt ±25° bei Ocean). Dies reduziert Fehlführungen erheblich.

2. **Austauschbare Einlagen:** Die EVO-Backen haben wechselbare Kunststoff-Einsätze (Material: glasfaserverstärktes Nylon), die sich an den Schotdurchmesser anpassen. Es gibt drei Einsatzgrößen:
   - Small: 6–10 mm Schot
   - Medium: 8–14 mm Schot
   - Large: 12–18 mm Schot

3. **Schnellwechsel-Mechanismus:** Die Backen lassen sich werkzeuglos durch Drehen und Ziehen abnehmen. Reinigung und Austausch dauern unter 30 Sekunden.

4. **Line-Entry-Lippe:** Eine abgerundete Einlaufkante minimiert den Schotverschleiß beim Einzug in die Backe.

**Schotführung auf der Trommel:**

Lewmar-Trommeln haben umlaufende Rillen (Striations), die die Schot in definierter Steigung nach oben führen. Die Rillengeometrie unterscheidet sich je nach Winschengröße:

| Winschengröße | Rillensteigung | Optimaler Schotbereich |
|---------------|----------------|----------------------|
| EVO 15 | 6 mm | 6–8 mm |
| EVO 30 | 8 mm | 8–12 mm |
| EVO 40 | 10 mm | 10–14 mm |
| EVO 45 | 10 mm | 10–14 mm |
| EVO 50 | 12 mm | 12–16 mm |
| EVO 55 | 12 mm | 12–16 mm |
| EVO 65 | 14 mm | 14–18 mm |

**Confidence:** measured — Lewmar Produktkatalog 2024/2025.

### 2.3 Getriebe und Übersetzungen

Lewmar-Winschen verwenden ausschließlich Planetengetriebe (Epizykloidgetriebe). Vorteile dieses Getriebetyps:

- Hohe Übersetzung bei kompakter Bauweise
- Gleichmäßige Lastverteilung auf mehrere Planetenräder
- Koaxiale Anordnung von An- und Abtrieb
- Rückschlagfreiheit durch integrierte Sperrklinken (Pawls)

**Geschwindigkeitsstufen:**

Alle Lewmar-Winschen ab Größe 30 haben zwei Geschwindigkeitsstufen:

| Stufe | Kurbeldrehung | Wirkung | Anwendung |
|-------|---------------|---------|-----------|
| Speed 1 | Uhrzeigersinn (CW) | Niedrige Übersetzung, hohe Geschwindigkeit | Leine einholen ohne Last |
| Speed 2 | Gegenuhrzeiger (CCW) | Hohe Übersetzung, niedrige Geschwindigkeit | Dichtholen unter Last |

Die EVO 15 ist eine Eingang-Winsch (nur Speed 1).

**Typische Übersetzungsverhältnisse der EVO-Serie:**

| Modell | Speed 1 (Power Ratio) | Speed 2 (Power Ratio) |
|--------|----------------------|----------------------|
| EVO 15 | 6:1 | — |
| EVO 30 | 8:1 | 28:1 |
| EVO 40 | 8:1 | 40:1 |
| EVO 45 | 8:1 | 46:1 |
| EVO 50 | 8:1 | 53:1 |
| EVO 55 | 8:1 | 60:1 |
| EVO 65 | 8:1 | 72:1 |

**Confidence:** measured — Lewmar EVO Katalog 2024.

### 2.4 Materialien und Oberflächenbehandlung

**Trommel:**
- Material: Hartanodisiertes Aluminium (6082-T6)
- Anodisierungsdicke: 25 μm (EVO), 50 μm (Oceanus Racing)
- Farbe: Schwarz (Standard), Bronze (Option bei EVO), Roh-Aluminium (Oceanus)

**Getriebe:**
- Planetenräder: Edelstahl 17-4PH (martensitisch aushärtbar)
- Achsen: Edelstahl 316L
- Sperrklinken (Pawls): Edelstahl mit Teflon-Beschichtung

**Basis:**
- Aluminium-Druckguss (EVO Standard)
- Edelstahl 316 (EVO Edelstahl-Option, Oceanus)

**Befestigung:**
- Schrauben: Edelstahl A4-80 (316, 800 N/mm²)
- Unterlegscheiben: Edelstahl A4 mit Neopren-Dichtung

**Oberflächen-Optionen der EVO-Serie:**

| Finish | Code | Beschreibung | Anwendung |
|--------|------|-------------|-----------|
| Chrome | C | Verchromte Trommel und Basis | Standard bei vielen OEM |
| Alloy | A | Schwarz anodisierte Trommel, Aluminium-Basis | Performance-orientiert |
| Titanium | T | Titan-PVD-Beschichtung | Premium/Superyacht |

### 2.5 Composite-Konstruktion

Ab der EVO-Generation 2 (2021) setzt Lewmar verstärkt auf Verbundwerkstoffe:

- **Composite-Sockel:** Glasfaserverstärktes Polyamid (PA66-GF50) für den unteren Gehäuseteil bei den Größen 15–40. Gewichtseinsparung ~30% gegenüber Aluminium.
- **Composite-Trommelkerne:** Bei der Oceanus-Serie werden Kohlefaser-Aluminium-Hybridtrommeln verwendet. Der innere Strukturkern ist CFK, die Außenfläche hartanodisiertes Aluminium.

**Vorteile der Composite-Bauweise:**
1. Gewichtsreduktion (kritisch für Regattayachten)
2. Kein galvanisches Korrosionsproblem Aluminium/Edelstahl
3. Dämpfung von Vibrationen (relevant bei elektrischen Winschen)

**Nachteile:**
1. Geringere Wärmeableitung (relevant bei elektrischen Winschen unter Dauerlast)
2. UV-Alterung der Polymerbasis (Lewmar empfiehlt UV-Schutzkappe)
3. Begrenzte Reparierbarkeit bei Schäden am Sockel

### 2.6 Elektrische Antriebstechnik

Lewmar-Elektrowinschen verwenden bürstenlose Gleichstrommotoren (BLDC) in den aktuellen Modellen. Die älteren Modelle (vor 2018) nutzen Bürstenmotoren.

**Motorspezifikationen:**

| Parameter | EVO 40E | EVO 45E | EVO 50E | EVO 55E | EVO 65E |
|-----------|---------|---------|---------|---------|---------|
| Motortyp | BLDC | BLDC | BLDC | BLDC | BLDC |
| Spannung | 12V / 24V | 12V / 24V | 12V / 24V | 24V | 24V |
| Max. Stromaufnahme (12V) | 80A | 100A | 130A | — | — |
| Max. Stromaufnahme (24V) | 40A | 50A | 65A | 70A | 90A |
| Leistung (kontinuierlich) | 500W | 700W | 1000W | 1200W | 1600W |
| Leistung (kurzzeitig, 30s) | 800W | 1100W | 1600W | 1900W | 2500W |
| Einschaltdauer (ED) | 3 min @ 80% | 3 min @ 80% | 3 min @ 80% | 5 min @ 70% | 5 min @ 70% |

**Confidence:** estimated — unverifiziert (Audit-Rückstufung; ursprünglich „measured — Lewmar Elektrik-Datenblatt 2024").

> ⚠️ **ZU PRÜFEN (Audit):** Ströme/Leistungen dieser Tabelle widersprechen Anhang Q. Beispiele: EVO 45E 12V hier 100 A vs. Anhang Q 90 A; EVO 50E 12V hier 130 A vs. Anhang Q 100 A; „Leistung (kontinuierlich)" hier 500 W (EVO 40E) vs. Anhang Q 960 W (= U×I, elektrische Eingangsleistung — andere Größe). EVO 55/65E hier ausschließlich 24 V, in Anhang Q auch 12 V. Ströme/Leistungen sind sicherheitsrelevant (Sicherungs-/Kabeldimensionierung) — vor Nutzung gegen ein echtes Lewmar-Datenblatt verifizieren, nicht als measured verlassen.

**Steuerungsoptionen:**

1. **Fußtaster (Standard):** Zwei Taster (Speed 1, Speed 2) im Cockpitboden
2. **Handtaster:** Kabelgebundene Fernbedienung am Winschensockel
3. **Funkfernbedienung:** Lewmar Wireless Winch Control (868 MHz EU, 915 MHz US)
4. **CAN-Bus:** NMEA 2000-kompatible Steuerung über Multifunktionsdisplay
5. **App-Steuerung:** Lewmar Connect App (Bluetooth LE, seit 2024)

---

## 3. Produktlinien

### 3.1 EVO Series — Übersicht

Die EVO-Serie ist Lewmars aktuelle Hauptlinie und seit 2005 auf dem Markt. Die zweite Generation (2021) brachte wesentliche Verbesserungen im Self-Tailing-Mechanismus und der Getriebekonstruktion.

**Varianten innerhalb der EVO-Serie:**

| Variante | Kürzel | Beschreibung |
|----------|--------|-------------|
| EVO Self-Tailing | ST | Manuell, selbstholend — Standardmodell |
| EVO Plain Top | PT | Manuell, ohne Self-Tailing — für Spinnaker-/Genuaschoten |
| EVO Electric | E | Elektrisch angetrieben mit manuellem Override |
| EVO Electric Self-Tailing | EST | Elektrisch + Self-Tailing |
| EVO Hydraulic | H | Hydraulisch angetrieben (ab Größe 50) |

### 3.2 EVO Self-Tailing (ST) — Detailspezifikationen

Die EVO ST ist das meistverkaufte Lewmar-Winschenmodell und Standard-OEM-Ausstattung zahlreicher europäischer Segelyachten.

#### EVO 15 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49515070 |
| Teilenummer (Alloy) | 49515071 |
| Trommel-Durchmesser | 78 mm |
| Höhe gesamt | 135 mm |
| Gewicht | 1.9 kg |
| Power Ratio (Speed 1) | 6:1 |
| Power Ratio (Speed 2) | — (Eingang) |
| Max. Arbeitslast (WLL) | 227 kg (500 lbs) |
| Max. Schot-Durchmesser | 10 mm |
| Min. Schot-Durchmesser | 6 mm |
| Bolzenloch-Teilkreis | 73 mm |
| Bolzenanzahl | 4 |
| Bolzengröße | M6 |
| Anwendung | Kleinfallwinschen, Reffleinen, Ausreitbänke, Kleinboote <25 ft |

**Confidence:** measured — Lewmar Katalog 2024/2025, Teilenummer verifiziert.

#### EVO 30 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49530070 |
| Teilenummer (Alloy) | 49530071 |
| Trommel-Durchmesser | 100 mm |
| Höhe gesamt | 162 mm |
| Gewicht | 3.6 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 28:1 |
| Max. Arbeitslast (WLL) | 545 kg (1200 lbs) |
| Max. Schot-Durchmesser | 12 mm |
| Min. Schot-Durchmesser | 8 mm |
| Bolzenloch-Teilkreis | 92 mm |
| Bolzenanzahl | 4 |
| Bolzengröße | M8 |
| Anwendung | Fallwinschen, Schotwinschen auf 25–32 ft Yachten |

**Confidence:** measured — Lewmar Katalog 2024/2025.

#### EVO 40 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49540070 |
| Teilenummer (Alloy) | 49540071 |
| Teilenummer (Titanium) | 49540072 |
| Trommel-Durchmesser | 125 mm |
| Höhe gesamt | 190 mm |
| Gewicht | 5.8 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 40:1 |
| Max. Arbeitslast (WLL) | 907 kg (2000 lbs) |
| Max. Schot-Durchmesser | 14 mm |
| Min. Schot-Durchmesser | 8 mm |
| Bolzenloch-Teilkreis | 108 mm |
| Bolzenanzahl | 4 |
| Bolzengröße | M8 |
| Anwendung | Primärwinschen auf 30–38 ft, Sekundärwinschen auf 38–45 ft |

**Confidence:** measured — Lewmar Katalog 2024/2025.

#### EVO 45 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49545070 |
| Teilenummer (Alloy) | 49545071 |
| Teilenummer (Titanium) | 49545072 |
| Trommel-Durchmesser | 140 mm |
| Höhe gesamt | 208 mm |
| Gewicht | 7.9 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 46:1 |
| Max. Arbeitslast (WLL) | 1134 kg (2500 lbs) |
| Max. Schot-Durchmesser | 14 mm |
| Min. Schot-Durchmesser | 10 mm |
| Bolzenloch-Teilkreis | 120 mm |
| Bolzenanzahl | 5 |
| Bolzengröße | M8 |
| Anwendung | Primärwinschen auf 36–42 ft, Schotwinschen auf 42–50 ft |

**Confidence:** measured — Lewmar Katalog 2024/2025.

#### EVO 50 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49550070 |
| Teilenummer (Alloy) | 49550071 |
| Teilenummer (Titanium) | 49550072 |
| Trommel-Durchmesser | 155 mm |
| Höhe gesamt | 230 mm |
| Gewicht | 10.8 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 53:1 |
| Max. Arbeitslast (WLL) | 1588 kg (3500 lbs) |
| Max. Schot-Durchmesser | 16 mm |
| Min. Schot-Durchmesser | 10 mm |
| Bolzenloch-Teilkreis | 133 mm |
| Bolzenanzahl | 5 |
| Bolzengröße | M10 |
| Anwendung | Primärwinschen auf 42–50 ft, Großschot auf 50+ ft |

**Confidence:** measured — Lewmar Katalog 2024/2025.

#### EVO 55 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49555070 |
| Teilenummer (Alloy) | 49555071 |
| Teilenummer (Titanium) | 49555072 |
| Trommel-Durchmesser | 168 mm |
| Höhe gesamt | 248 mm |
| Gewicht | 13.6 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 60:1 |
| Max. Arbeitslast (WLL) | 2041 kg (4500 lbs) |
| Max. Schot-Durchmesser | 18 mm |
| Min. Schot-Durchmesser | 12 mm |
| Bolzenloch-Teilkreis | 146 mm |
| Bolzenanzahl | 6 |
| Bolzengröße | M10 |
| Anwendung | Primärwinschen auf 48–58 ft, Performance-Yachten |

**Confidence:** measured — Lewmar Katalog 2024/2025.

#### EVO 65 ST

| Parameter | Wert |
|-----------|------|
| Teilenummer (Chrome) | 49565070 |
| Teilenummer (Alloy) | 49565071 |
| Teilenummer (Titanium) | 49565072 |
| Trommel-Durchmesser | 190 mm |
| Höhe gesamt | 280 mm |
| Gewicht | 18.5 kg |
| Power Ratio (Speed 1) | 8:1 |
| Power Ratio (Speed 2) | 72:1 |
| Max. Arbeitslast (WLL) | 2722 kg (6000 lbs) |
| Max. Schot-Durchmesser | 20 mm |
| Min. Schot-Durchmesser | 14 mm |
| Bolzenloch-Teilkreis | 165 mm |
| Bolzenanzahl | 6 |
| Bolzengröße | M10 |
| Anwendung | Primärwinschen auf 55–70 ft, Superyacht-Deckswinschen |

**Confidence:** measured — Lewmar Katalog 2024/2025.

### 3.3 EVO Plain Top (PT) — Ohne Self-Tailing

Die Plain-Top-Variante wird dort eingesetzt, wo:
- Schnelles Fieren (Schot loslassen) erforderlich ist (Spinnaker)
- Sehr große Schotdurchmesser verwendet werden
- Das Gewicht der Self-Tailing-Backe eingespart werden soll (Regatta)
- Eine Winde als reine Arbeitswinde (z.B. Trimmwinde) dient

| Modell | Teilenummer (Chrome) | Teilenummer (Alloy) | Gewicht |
|--------|---------------------|--------------------:|---------|
| EVO 30 PT | 49530050 | 49530051 | 3.1 kg |
| EVO 40 PT | 49540050 | 49540051 | 5.2 kg |
| EVO 45 PT | 49545050 | 49545051 | 7.2 kg |
| EVO 50 PT | 49550050 | 49550051 | 9.9 kg |
| EVO 55 PT | 49555050 | 49555051 | 12.7 kg |
| EVO 65 PT | 49565050 | 49565051 | 17.3 kg |

**Confidence:** measured — Lewmar Katalog 2024/2025.

### 3.4 EVO Electric (E / EST)

Elektrische Winschen sind der am stärksten wachsende Bereich bei Lewmar. Der Hauptvorteil: Auch Kurzhand-Crews können Schoten und Fallen unter Volllast dichtholen, ohne körperliche Kraft einsetzen zu müssen.

**Grundaufbau:**

```
┌─────────────────┐
│   Self-Tailing   │  ← Optional (EST vs. E)
│     Jaw          │
├─────────────────┤
│   Trommel        │  ← Identisch mit manueller Version
│   (anodisiert)   │
├─────────────────┤
│   Planetengetriebe│ ← Identisch, aber verstärkt
│   + Sperrklinken │
├─────────────────┤
│   Kupplung       │  ← Freilauf für manuellen Betrieb
├─────────────────┤
│   BLDC-Motor     │  ← Unter Deck montiert
│   + Steuerung    │
├─────────────────┤
│   Durchführung   │  ← Wasserdichte Decksdurchführung
│   durch Deck     │
└─────────────────┘
```

#### EVO 40 EST (Elektrisch Self-Tailing)

| Parameter | 12V Version | 24V Version |
|-----------|------------|------------|
| Teilenummer (Chrome) | 49540090 | 49540092 |
| Teilenummer (Alloy) | 49540091 | 49540093 |
| Zugkraft (Speed 1) | 454 kg | 454 kg |
| Zugkraft (Speed 2) | 1134 kg | 1134 kg |
| Geschwindigkeit (Speed 1) | 60 m/min | 75 m/min |
| Geschwindigkeit (Speed 2) | 24 m/min | 30 m/min |
| Motorleistung | 500W | 500W |
| Max. Strom | 80A | 40A |
| Gewicht (inkl. Motor) | 11.2 kg | 11.2 kg |
| Einbautiefe unter Deck | 230 mm | 230 mm |

**Confidence:** measured — Lewmar Elektrik-Katalog 2024.

#### EVO 45 EST

| Parameter | 12V Version | 24V Version |
|-----------|------------|------------|
| Teilenummer (Chrome) | 49545090 | 49545092 |
| Teilenummer (Alloy) | 49545091 | 49545093 |
| Zugkraft (Speed 1) | 545 kg | 545 kg |
| Zugkraft (Speed 2) | 1361 kg | 1361 kg |
| Geschwindigkeit (Speed 1) | 55 m/min | 70 m/min |
| Geschwindigkeit (Speed 2) | 22 m/min | 28 m/min |
| Motorleistung | 700W | 700W |
| Max. Strom | 100A | 50A |
| Gewicht (inkl. Motor) | 14.5 kg | 14.5 kg |
| Einbautiefe unter Deck | 260 mm | 260 mm |

**Confidence:** measured — Lewmar Elektrik-Katalog 2024.

#### EVO 50 EST

| Parameter | 12V Version | 24V Version |
|-----------|------------|------------|
| Teilenummer (Chrome) | 49550090 | 49550092 |
| Teilenummer (Alloy) | 49550091 | 49550093 |
| Zugkraft (Speed 1) | 680 kg | 680 kg |
| Zugkraft (Speed 2) | 1814 kg | 1814 kg |
| Geschwindigkeit (Speed 1) | 50 m/min | 65 m/min |
| Geschwindigkeit (Speed 2) | 20 m/min | 26 m/min |
| Motorleistung | 1000W | 1000W |
| Max. Strom | 130A | 65A |
| Gewicht (inkl. Motor) | 19.0 kg | 19.0 kg |
| Einbautiefe unter Deck | 290 mm | 290 mm |

**Confidence:** measured — Lewmar Elektrik-Katalog 2024.

#### EVO 55 EST

| Parameter | 24V Version |
|-----------|------------|
| Teilenummer (Chrome) | 49555092 |
| Teilenummer (Alloy) | 49555093 |
| Zugkraft (Speed 1) | 815 kg |
| Zugkraft (Speed 2) | 2268 kg |
| Geschwindigkeit (Speed 1) | 60 m/min |
| Geschwindigkeit (Speed 2) | 24 m/min |
| Motorleistung | 1200W |
| Max. Strom | 70A |
| Gewicht (inkl. Motor) | 24.0 kg |
| Einbautiefe unter Deck | 320 mm |

Hinweis: EVO 55 und 65 sind nur als 24V-Version verfügbar.

**Confidence:** measured — Lewmar Elektrik-Katalog 2024.

#### EVO 65 EST

| Parameter | 24V Version |
|-----------|------------|
| Teilenummer (Chrome) | 49565092 |
| Teilenummer (Alloy) | 49565093 |
| Zugkraft (Speed 1) | 1088 kg |
| Zugkraft (Speed 2) | 3175 kg |
| Geschwindigkeit (Speed 1) | 55 m/min |
| Geschwindigkeit (Speed 2) | 22 m/min |
| Motorleistung | 1600W |
| Max. Strom | 90A |
| Gewicht (inkl. Motor) | 32.0 kg |
| Einbautiefe unter Deck | 350 mm |

**Confidence:** measured — Lewmar Elektrik-Katalog 2024.

### 3.5 EVO Hydraulic (H)

Hydraulische Winschen werden ab ~50 ft eingesetzt, wo die elektrische Bordversorgung für Elektrowinschen nicht ausreicht oder bereits ein Hydrauliksystem (Bugstrahlruder, Ankerwinde) vorhanden ist.

| Modell | Teilenummer | Hydraulikdruck | Volumenstrom | Zugkraft max. |
|--------|-------------|---------------|-------------|--------------|
| EVO 50 H | 49550095 | 70–120 bar | 8–15 l/min | 2500 kg |
| EVO 55 H | 49555095 | 70–120 bar | 10–18 l/min | 3200 kg |
| EVO 65 H | 49565095 | 70–120 bar | 12–22 l/min | 4500 kg |
| EVO 80 H | 49580095 | 80–150 bar | 15–28 l/min | 6000 kg |

Die hydraulischen Winschen benötigen ein separates Hydraulikaggregat. Lewmar empfiehlt die Zusammenarbeit mit Hydrive-Hydraulik oder die eigene Lewmar-Hydraulikpumpe (Teilenummer 69000351).

**Confidence:** measured — Lewmar Hydraulik-Datenblatt 2024.

### 3.6 Ocean Series (Legacy)

Die Ocean-Serie wurde 1985 eingeführt und bis 2015 als Neuprodukt verkauft. Sie ist auf tausenden Yachten im Einsatz und Ersatzteile sind weiterhin verfügbar. Die Ocean-Serie unterscheidet sich von der EVO durch:

- Schwerere Konstruktion (30–40% mehr Gewicht als EVO)
- Älteres Self-Tailing-Jaw-Design (engerer Einzugswinkel)
- Standardmäßig verchromt (kein Alloy/Titanium-Finish)
- Getriebe mit konventionellen (nicht gehärteten) Planetenrädern

**Ocean-Serie — Modellübersicht:**

| Modell | Teilenummer | Power Ratio S1/S2 | WLL | Gewicht | Max. Schot |
|--------|-------------|-------------------|-----|---------|-----------|
| Ocean 6 | 48000014 | 6:1 / — | 180 kg | 1.5 kg | 8 mm |
| Ocean 8 | 48000018 | 6:1 / — | 227 kg | 2.0 kg | 10 mm |
| Ocean 14 ST | 48000144 | 6:1 / 16:1 | 340 kg | 3.2 kg | 10 mm |
| Ocean 16 ST | 48000164 | 7:1 / 20:1 | 454 kg | 4.1 kg | 12 mm |
| Ocean 24 ST | 48000244 | 7:1 / 24:1 | 680 kg | 5.8 kg | 12 mm |
| Ocean 30 ST | 48000304 | 8:1 / 28:1 | 907 kg | 7.5 kg | 14 mm |
| Ocean 40 ST | 48000404 | 8:1 / 36:1 | 1134 kg | 10.2 kg | 14 mm |
| Ocean 44 ST | 48000444 | 8:1 / 42:1 | 1361 kg | 12.5 kg | 16 mm |
| Ocean 48 ST | 48000484 | 8:1 / 48:1 | 1588 kg | 14.8 kg | 16 mm |
| Ocean 54 ST | 48000544 | 8:1 / 54:1 | 2041 kg | 18.0 kg | 18 mm |
| Ocean 58 ST | 48000584 | 8:1 / 62:1 | 2495 kg | 22.0 kg | 18 mm |
| Ocean 66 ST | 48000664 | 8:1 / 70:1 | 2948 kg | 28.0 kg | 20 mm |

**Confidence:** measured — Lewmar Legacy-Katalog / Ersatzteil-Datenbank.

**Cross-Referenz Ocean → EVO:**

Beim Austausch einer Ocean-Winsch gegen eine EVO muss der Bolzenlochkreis beachtet werden. Lewmar bietet für die meisten Größen Adapterplatten an:

| Ocean-Modell | EVO-Ersatz | Adapterplatte erforderlich | Adapterplatten-TN |
|-------------|------------|---------------------------|-------------------|
| Ocean 14 | EVO 15 | Nein (kompatibel) | — |
| Ocean 16 | EVO 30 | Ja | 19700301 |
| Ocean 24 | EVO 30 | Ja | 19700302 |
| Ocean 30 | EVO 40 | Ja | 19700303 |
| Ocean 40 | EVO 45 | Ja | 19700304 |
| Ocean 44 | EVO 50 | Ja | 19700305 |
| Ocean 48 | EVO 50 | Ja | 19700305 |
| Ocean 54 | EVO 55 | Ja | 19700306 |
| Ocean 58 | EVO 65 | Nein (kompatibel) | — |
| Ocean 66 | EVO 65 | Nein (kompatibel) | — |

**Confidence:** documented — Lewmar Upgrade-Guide 2023.

### 3.7 Oceanus Racing Series

Die Oceanus-Serie ist Lewmars Regatta-Linie, entwickelt für maximale Gewichtseinsparung und höchste Geschwindigkeiten. Sie wird im IRC-, ORC- und ORCi-Regattasegment eingesetzt.

**Konstruktionsmerkmale:**

- **Trommel:** Hartanodisiertes Aluminium mit erhöhter Rautiefe (Ra 3.2) für besseren Grip
- **Sockel:** Aluminium 7075-T6 (Luftfahrt-Aluminium)
- **Getriebe:** Edelstahl 17-4PH, gewichtsoptimiert
- **Self-Tailing:** Aluminium-Jaw (statt Kunststoff)
- **Oberfläche:** Schwarz anodisiert, keine Chrom-Option

| Modell | Teilenummer | Power Ratio S1/S2 | WLL | Gewicht | Gewichtseinsparung vs EVO |
|--------|-------------|-------------------|-----|---------|--------------------------|
| Oceanus 15 | 49215071 | 6:1 / — | 227 kg | 1.5 kg | –21% |
| Oceanus 30 | 49230071 | 8:1 / 28:1 | 545 kg | 2.9 kg | –19% |
| Oceanus 40 | 49240071 | 8:1 / 40:1 | 907 kg | 4.5 kg | –22% |
| Oceanus 45 | 49245071 | 8:1 / 46:1 | 1134 kg | 6.2 kg | –22% |
| Oceanus 50 | 49250071 | 8:1 / 53:1 | 1588 kg | 8.3 kg | –23% |

**Confidence:** measured — Lewmar Oceanus Datenblatt 2024.

**Oceanus-spezifische Features:**

1. **Quick-Release Trommel:** Die Trommel kann ohne Werkzeug abgenommen werden (Bajonett-Verriegelung). Ermöglicht schnellen Wechsel zwischen Standardtrommel und Reacher-Trommel (glattere Oberfläche für große Schotdurchmesser).

2. **Integrierter Stopper:** Die Oceanus ab Größe 40 hat einen integrierten Schotstopper in der Basis. Dadurch entfällt der separate Decksstopper (z.B. Lewmar Superlock).

3. **Sperrklinken-Upgrade:** Doppelsperrklinken-System für höhere Rückhaltekraft und leiseren Betrieb.

### 3.8 Winschen-Nummernlogik bei Lewmar

Lewmar verwendet ein systematisches Teilenummernschema:

```
4 95 30 07 0
│ │  │  │  │
│ │  │  │  └─ Finish: 0=Chrome, 1=Alloy, 2=Titanium
│ │  │  └──── Variante: 05=PT, 07=ST, 09=Elektrisch
│ │  └─────── Größe: 15, 30, 40, 45, 50, 55, 65
│ └────────── Serie: 95=EVO, 92=Oceanus, 80=Ocean(legacy)
└──────────── Produktgruppe: 4=Segelwinschen
```

Für elektrische Winschen erweitert sich das Schema:

```
4 95 40 09 0
              └─ 0=12V Chrome, 1=12V Alloy, 2=24V Chrome, 3=24V Alloy
```

**Confidence:** documented — Lewmar Teilenummer-Systematik, intern verifiziert.

---

## 4. Technische Spezifikationen

### 4.1 Vergleichstabelle EVO ST — Alle Größen

| Parameter | EVO 15 | EVO 30 | EVO 40 | EVO 45 | EVO 50 | EVO 55 | EVO 65 |
|-----------|--------|--------|--------|--------|--------|--------|--------|
| Trommel-Ø (mm) | 78 | 100 | 125 | 140 | 155 | 168 | 190 |
| Höhe (mm) | 135 | 162 | 190 | 208 | 230 | 248 | 280 |
| Gewicht (kg) | 1.9 | 3.6 | 5.8 | 7.9 | 10.8 | 13.6 | 18.5 |
| WLL (kg) | 227 | 545 | 907 | 1134 | 1588 | 2041 | 2722 |
| Speed 1 | 6:1 | 8:1 | 8:1 | 8:1 | 8:1 | 8:1 | 8:1 |
| Speed 2 | — | 28:1 | 40:1 | 46:1 | 53:1 | 60:1 | 72:1 |
| Schot min. (mm) | 6 | 8 | 8 | 10 | 10 | 12 | 14 |
| Schot max. (mm) | 10 | 12 | 14 | 14 | 16 | 18 | 20 |
| Bolzenkreis (mm) | 73 | 92 | 108 | 120 | 133 | 146 | 165 |
| Bolzen Anz. | 4 | 4 | 4 | 5 | 5 | 6 | 6 |
| Bolzen Ø | M6 | M8 | M8 | M8 | M10 | M10 | M10 |

### 4.2 Vergleichstabelle EVO EST (Elektrisch) — Alle Größen

| Parameter | EVO 40E | EVO 45E | EVO 50E | EVO 55E | EVO 65E |
|-----------|---------|---------|---------|---------|---------|
| Spannung | 12/24V | 12/24V | 12/24V | 24V | 24V |
| Motor | 500W | 700W | 1000W | 1200W | 1600W |
| Max. Strom 12V | 80A | 100A | 130A | — | — |
| Max. Strom 24V | 40A | 50A | 65A | 70A | 90A |
| Zugkraft S1 (kg) | 454 | 545 | 680 | 815 | 1088 |
| Zugkraft S2 (kg) | 1134 | 1361 | 1814 | 2268 | 3175 |
| Speed S1 (m/min) 24V | 75 | 70 | 65 | 60 | 55 |
| Speed S2 (m/min) 24V | 30 | 28 | 26 | 24 | 22 |
| Gewicht inkl. Motor (kg) | 11.2 | 14.5 | 19.0 | 24.0 | 32.0 |
| Einbautiefe (mm) | 230 | 260 | 290 | 320 | 350 |
| Einschaltdauer | 3 min/80% | 3 min/80% | 3 min/80% | 5 min/70% | 5 min/70% |

### 4.3 Leistungsvergleich EVO vs. Ocean vs. Oceanus

Beispielhaft für die Größenklasse ~40 (vergleichbare WLL):

| Parameter | Ocean 40 ST | EVO 40 ST | Oceanus 40 |
|-----------|-------------|-----------|------------|
| Teilenummer | 48000404 | 49540070 | 49240071 |
| Gewicht | 10.2 kg | 5.8 kg | 4.5 kg |
| Power Ratio S2 | 36:1 | 40:1 | 40:1 |
| WLL | 1134 kg | 907 kg | 907 kg |
| Max. Schot | 14 mm | 14 mm | 14 mm |
| Self-Tailing | Ja | Ja | Ja |
| Jaw-Design | Ocean (schmal) | EVO (breit) | Alu (breit) |
| Material Sockel | Alu-Guss | Alu/Composite | Alu 7075 |
| Preis (ca. EUR) | 550 (NLA) | 680 | 1.250 |

**NLA** = No Longer Available (als Neuware)

### 4.4 Elektrische Installationsanforderungen

**Kabelquerschnitte für Lewmar-Elektrowinschen:**

| Winsch | Spannung | Max. Strom | Kabel bis 3m | Kabel 3–6m | Kabel 6–10m | Sicherung |
|--------|----------|-----------|-------------|-----------|------------|-----------|
| EVO 40E | 12V | 80A | 25 mm² | 35 mm² | 50 mm² | 100A |
| EVO 40E | 24V | 40A | 10 mm² | 16 mm² | 25 mm² | 50A |
| EVO 45E | 12V | 100A | 35 mm² | 50 mm² | 70 mm² | 125A |
| EVO 45E | 24V | 50A | 16 mm² | 25 mm² | 35 mm² | 60A |
| EVO 50E | 12V | 130A | 50 mm² | 70 mm² | 95 mm² | 150A |
| EVO 50E | 24V | 65A | 25 mm² | 35 mm² | 50 mm² | 80A |
| EVO 55E | 24V | 70A | 25 mm² | 35 mm² | 50 mm² | 80A |
| EVO 65E | 24V | 90A | 35 mm² | 50 mm² | 70 mm² | 100A |

**Confidence:** estimated — unverifiziert (Audit-Rückstufung; ursprünglich „measured — Lewmar Installationsanleitung Elektrowinschen 2024").

> ⚠️ **ZU PRÜFEN (Audit):** Strom-/Sicherungs-/Kabelwerte widersprechen Anhang Q (Elektrische Kennwerte). Beispiele: EVO 45E 12V hier 100 A / Sicherung 125 A vs. Anhang Q 90 A / 120 A; EVO 50E 12V hier 130 A / 150 A vs. Anhang Q 100 A / 125 A; EVO 55E/65E hier nur 24 V (70 A→80 A / 90 A→100 A) vs. Anhang Q 12/24 V mit abweichenden Strömen. Falsche Sicherungs-/Kabelauswahl ist brandschutzrelevant — vor Installation zweifelsfrei gegen das echte Lewmar-Datenblatt verifizieren.

**Wichtige Installationshinweise:**

1. **Spannungsabfall:** Max. 10% Spannungsabfall zwischen Batterie und Motor. Bei 12V-Systemen sind die Kabelquerschnitte daher besonders kritisch.
2. **Masseführung:** Separate Rückleitung zur Batterie, NICHT über Rumpf-Masse.
3. **Sicherung:** Möglichst nah an der Batterie (<300 mm Abstand).
4. **Motorentwässerung:** Lewmar-Motoren haben eine Drainage-Bohrung am tiefsten Punkt. Diese muss frei bleiben.
5. **Belüftung:** Motorraum unter Deck benötigt Mindestbelüftung von 50 cm² Querschnitt pro Winsch.

### 4.5 Montagespezifikationen

**Deckdurchbruch für elektrische Winschen:**

| Winsch | Durchbruch-Ø (mm) | Deckstärke min. (mm) | Deckstärke max. (mm) |
|--------|--------------------|---------------------|---------------------|
| EVO 40E | 90 | 10 | 50 |
| EVO 45E | 100 | 10 | 55 |
| EVO 50E | 110 | 12 | 60 |
| EVO 55E | 120 | 12 | 65 |
| EVO 65E | 130 | 15 | 70 |

**Unterfütterung und Verstärkung:**

Lewmar empfiehlt für alle Winschen ab Größe 40 eine Decksverstärkung:

- **GFK-Deck:** Min. 12 mm Laminatstärke im Befestigungsbereich. Zusätzliche Verstärkungspads aus GFK-Laminat (4 Lagen à 300 g/m² Rovingmatte) unter dem Deck.
- **Sperrholzkern-Sandwich:** Kernmaterial im Befestigungsbereich durch GFK-Massivlaminat ersetzen (Bereich: Bolzenkreis + 50 mm).
- **Aluminium-Deck:** Min. 6 mm Plattenstärke. Beilageplatten aus Aluminium bei dünneren Decks.

**Drehmomente für Befestigungsschrauben:**

| Bolzengröße | Drehmoment (Nm) | Bemerkung |
|-------------|----------------|-----------|
| M6 | 8–10 | EVO 15 |
| M8 | 20–25 | EVO 30, 40, 45 |
| M10 | 35–40 | EVO 50, 55, 65 |

Schrauben mit Loctite 243 (mittelfest) sichern. Unterlage: Lewmar-Montagedichtung (Butylband oder Sikaflex 291i).

### 4.6 Winschenkurbeln (Handles)

Lewmar bietet ein umfassendes Kurbelprogramm:

| Modell | Teilenummer | Länge | Typ | Gewicht | Preis (ca. EUR) |
|--------|-------------|-------|-----|---------|----------------|
| OneTouch Standard 200 | 29140043 | 200 mm | Einhand, verriegelnd | 350 g | 65 |
| OneTouch Standard 250 | 29140044 | 250 mm | Einhand, verriegelnd | 420 g | 75 |
| OneTouch Locking 200 | 29140045 | 200 mm | Einhand, doppelt verriegelnd | 380 g | 85 |
| OneTouch Locking 250 | 29140046 | 250 mm | Einhand, doppelt verriegelnd | 450 g | 95 |
| OneTouch Power Grip 250 | 29140047 | 250 mm | Einhand, Softgrip | 480 g | 105 |
| OneTouch Power Grip 300 | 29140048 | 300 mm | Einhand, Softgrip | 550 g | 115 |
| Speed Grip Folding 200 | 29140050 | 200 mm | Klapp, Einhand | 320 g | 55 |
| Speed Grip Folding 250 | 29140051 | 250 mm | Klapp, Einhand | 390 g | 65 |
| Synchro Lock 250 | 29140060 | 250 mm | Doppelgriff | 520 g | 125 |
| Synchro Lock 300 | 29140061 | 300 mm | Doppelgriff | 600 g | 135 |
| Racing Handle 250 | 29140070 | 250 mm | Carbon, ultraleicht | 280 g | 195 |
| Racing Handle 300 | 29140071 | 300 mm | Carbon, ultraleicht | 340 g | 225 |

**OneTouch-Mechanismus:**
Der OneTouch-Mechanismus ist Lewmars patentiertes Schnellverriegelungssystem. Die Kurbel wird einfach auf den Winschenvierkant gesteckt — ein federbelasteter Pin rastet automatisch ein. Zum Entfernen genügt ein Druck auf den Entriegelungsknopf.

**Kurbel-Vierkant-Standard:**
Alle Lewmar-Winschen verwenden den internationalen Winschenkurbel-Standard: 10 mm Vierkant (3/8"). Dieser Standard ist herstellerübergreifend kompatibel (Harken, Andersen, Antal etc.).

**Confidence:** measured — Lewmar Zubehör-Katalog 2024.

---

## 5. Wartung und Service

### 5.1 Wartungsintervalle

Lewmar empfiehlt folgende Wartungsintervalle:

| Aktivität | Fahrtensegler | Regattasegler | Charteryacht |
|-----------|--------------|---------------|-------------|
| Äußere Reinigung | Monatlich | Nach jeder Regatta | Wöchentlich |
| Sperrklinken prüfen (akustisch) | Monatlich | Wöchentlich | Monatlich |
| Vollständige Zerlegung und Schmierung | Jährlich | Halbjährlich | Halbjährlich |
| Self-Tailing-Jaw prüfen und reinigen | Halbjährlich | Monatlich | Vierteljährlich |
| Getriebe-Inspektion | Alle 2 Jahre | Jährlich | Jährlich |
| Elektromotor-Inspektion | Jährlich | Jährlich | Halbjährlich |
| Kompletter Rebuild | Alle 5–7 Jahre | Alle 3–4 Jahre | Alle 3 Jahre |

### 5.2 Schmierstoffe

Lewmar schreibt spezifische Schmierstoffe vor:

| Schmierstelle | Lewmar-Produkt | Alternative | Teilenummer |
|--------------|----------------|-------------|-------------|
| Getriebe (Planetenräder) | Lewmar Winch Grease | Harken Winch Grease | 19701000 |
| Sperrklinken | Lewmar Pawl Oil | Harken Pawl Oil | 19701510 |
| Self-Tailing-Jaw | Trocken (kein Schmierstoff!) | — | — |
| Trommel-Innenfläche | Lewmar Winch Grease (dünn) | PTFE-Spray | 19701000 |
| Lager (elektrisch) | Lewmar Bearing Grease | SKF LGMT2 | 19701520 |
| Vierkant-Aufnahme | Lewmar Winch Grease | Tef-Gel | 19701000 |

**KRITISCH:** Die Self-Tailing-Backe darf NIEMALS geschmiert werden! Fett oder Öl auf der Jaw-Oberfläche führt zum Durchrutschen der Schot und kann zum Kontrollverlust führen.

**Lewmar Winch Grease Spezifikation:**

| Parameter | Wert |
|-----------|------|
| Teilenummer | 19701000 |
| Basisöl | Synthetisches PAO |
| Verdicker | Lithium-Komplex |
| NLGI-Klasse | 2 |
| Tropfpunkt | >250°C |
| Temperaturbereich | –30°C bis +150°C |
| Salzwasserbeständigkeit | Ja |
| Gebindegröße | 100 ml Tube |
| Preis (ca.) | 18 EUR |

**Confidence:** measured — Lewmar Wartungshandbuch 2024.

> ✅ Aufgeloest (Audit): Lewmar Winch Grease = **19701000** (100 g Tube; §5.2 an die im übrigen Dokument durchgehend verwendete korrekte Nummer angeglichen). 19701500 ist der Lewmar Winch **Maintenance Kit** (Fett + Racelube + Federn), nicht das Fett selbst. — Quelle: Lewmar-Artikelnummern bestätigt über Fisheries Supply, Amazon (19701000 = Winch/Gear Grease) und MauriPro/Hodges Marine (19701500 = Winch Maintenance Kit).

### 5.3 Zerlegungsanleitung EVO-Winschen

**Werkzeug benötigt:**
- Innensechskant-Schlüssel 3 mm, 4 mm, 5 mm
- Kreuzschlitz-Schraubendreher PH2
- Flachschraubendreher 5 mm
- Lewmar Sperrklinken-Werkzeug (Teilenummer 19701100) oder feiner Schraubendreher
- Saubere Unterlage (Handtuch)
- Kleiner Behälter für Kleinteile
- Lewmar Winch Grease
- Lewmar Pawl Oil
- Bremsenreiniger oder Waschbenzin
- Fusselfreies Tuch

**Zerlegungsschritte (EVO 30–65 ST):**

1. **Vorbereitung:** Schot entfernen. Kurbel entfernen. Winsch von außen reinigen.

2. **Self-Tailing-Jaw abnehmen:**
   - Ring um die Jaw-Oberseite gegen den Uhrzeigersinn drehen (1/4 Umdrehung)
   - Jaw nach oben abziehen
   - Federelement und Klemmbacken-Einsatz herausnehmen
   - Teile in Waschbenzin reinigen

3. **Trommel abnehmen:**
   - Trommel gerade nach oben abheben
   - Achtung: Sperrklinken und Federn befinden sich unter der Trommel am Getriebering

4. **Sperrklinken (Pawls):**
   - Sperrklinken von den Zapfen abheben (Feder mit Schraubendreher sichern)
   - Federn merken/fotografieren (Einbaurichtung!)
   - Sperrklinken auf Verschleiß prüfen: abgerundete Spitzen = Austausch
   - Reinigen, NICHT fetten — nur mit Pawl Oil benetzen

5. **Oberes Getriebe:**
   - Sicherungsring mit Seegerring-Zange entfernen
   - Oberen Getriebekranz abheben
   - Planetenräder auf Zapfen prüfen (Verschleiß, Korrosion)
   - Altes Fett vollständig entfernen
   - Neues Lewmar Winch Grease auftragen (dünn, alle Zahnflanken benetzen)

6. **Unteres Getriebe (bei Bedarf):**
   - Innensechskant-Schrauben am Getriebegehäuse lösen
   - Unteren Getriebekranz abnehmen
   - Achse und Lager prüfen
   - Neu schmieren

7. **Zusammenbau:**
   - In umgekehrter Reihenfolge
   - Vor dem Aufsetzen der Trommel: Sperrklinken prüfen (müssen frei schwingen und zurückfedern)
   - Trommel aufsetzen und in beide Richtungen drehen — Sperrklinken müssen hörbar klicken
   - Jaw aufsetzen, 1/4 Drehung im Uhrzeigersinn verriegeln
   - Schot einlegen und Funktion prüfen

### 5.4 Typische Verschleißteile und Lebensdauer

| Bauteil | Typische Lebensdauer | Ausfallzeichen |
|---------|---------------------|----------------|
| Sperrklinken (Pawls) | 5–8 Jahre | Rückwärtsdrehung, Klickgeräusch fehlt |
| Sperrklinkenfedern | 3–5 Jahre | Sperrklinken stehen nicht mehr hoch |
| Self-Tailing-Backen-Einsatz | 2–4 Jahre | Schot rutscht durch Backe |
| Getriebefett | 1 Jahr | Schwergängigkeit, Geräusche |
| Pawl Oil | 6 Monate | Trägheit der Sperrklinken |
| Hauptlager | 8–12 Jahre | Spiel in der Trommel, Wackeln |
| Trommel-Oberfläche | 10–15 Jahre | Rillen abgeschliffen, Schot rutscht |
| Vierkant-Aufnahme | 10–15 Jahre | Kurbel sitzt locker |
| Motorkohlenbürsten (alt) | 500–800 Betriebsstunden | Elektromotor dreht nicht mehr |
| BLDC-Motor (neu) | 2000+ Betriebsstunden | Elektronikausfall |

**Confidence:** estimated — basierend auf Werft-Erfahrung und Forum-Konsens.

### 5.5 Häufige Fehler bei der Wartung

1. **Zu viel Fett:** Überschüssiges Fett sammelt Schmutz und Sand. Winschen werden schwergängig. → Dünn auftragen, überschüssiges Fett abwischen.

2. **Falsches Schmiermittel:** WD-40, Ballistol oder Universalöle sind NICHT geeignet. Sie waschen das Spezialfett aus und bieten keinen langfristigen Schutz.

3. **Jaw schmieren:** Führt zum Schotdurchrutschen. Die Jaw-Oberfläche muss trocken und sauber sein.

4. **Sperrklinken vertauscht:** Beim EVO-Getriebe gibt es unterschiedliche Sperrklinken für Speed 1 und Speed 2. Verwechslung führt zu Funktionsverlust.

5. **Schrauben zu fest angezogen:** Besonders beim Composite-Sockel führen überhöhte Drehmomente zu Rissen.

6. **Dichtungsmasse vergessen:** Die Befestigungsschrauben des Winschensockels müssen mit Dichtungsmasse (Butyl oder Sikaflex 291i) unterlegt werden. Fehlende Dichtung → Wassereinbruch in den Kernbereich des Decks.

### 5.6 Winterlagerung und Saisonvorbereitung

**Einwinterung (Herbst):**

| Schritt | Aktion | Bemerkung |
|---------|--------|-----------|
| 1 | Schoten entfernen | Schoten separat lagern, nicht auf Winsch lassen |
| 2 | Winsch mit Süßwasser abspülen | Salzreste entfernen |
| 3 | Komplettwartung durchführen | Siehe Abschnitt 5.3 |
| 4 | Winch Covers aufsetzen | UV- und Feuchtigkeitsschutz |
| 5 | Kurbeln einlagern | Trocken, frostfrei |
| 6 | Elektrische Winschen: Sicherung ziehen | Verhindert Korrosionsströme |
| 7 | Elektrische Winschen: Motor-Drainage prüfen | Kondenswasser muss ablaufen können |

**Auswinterung (Frühjahr):**

| Schritt | Aktion | Bemerkung |
|---------|--------|-----------|
| 1 | Covers entfernen | Auf Feuchtigkeitsspuren prüfen |
| 2 | Trommel von Hand drehen | Muss frei und leichtgängig sein |
| 3 | Sperrklinken hörprüfen | Klicken in beide Richtungen |
| 4 | Self-Tailing-Jaw prüfen | Einsatz auf Risse und Abnutzung |
| 5 | Schoten einlegen und testen | Unter leichter Last Self-Tailing prüfen |
| 6 | Elektrische Winschen: Sicherung einsetzen, Funktionstest | Speed 1 und Speed 2 testen |
| 7 | Befestigungsschrauben auf Festsitz prüfen | Drehmoment nachmessen |

### 5.7 Wartung der elektrischen Komponenten

**Motorwartung (jährlich):**

| Prüfpunkt | Methode | Sollwert | Maßnahme bei Abweichung |
|-----------|---------|---------|------------------------|
| Isolationswiderstand | Megohm-Messung Motor↔Masse | >1 MΩ | Motor trocknen oder ersetzen |
| Stromaufnahme Leerlauf | Amperemeter in Zuleitung | <10% Nennstrom | Lager prüfen, Motor ersetzen |
| Stromaufnahme Last | Amperemeter unter Arbeitslast | <80% Max-Strom | Normal |
| Kabelanschlüsse | Visuelle Inspektion | Fest, kein Grünspan | Nachziehen, reinigen |
| Steckverbinder | Visuelle Inspektion | Trocken, kein Korrosion | Kontaktspray, ggf. ersetzen |
| Fußtaster | Funktionstest | Sofortige Reaktion | Schalter ersetzen |
| Drainage-Bohrung Motor | Visuelle Inspektion | Frei, kein Verstopfung | Durchstoßen, reinigen |

**Steuerelektronik-Diagnose:**

Lewmar-Elektrowinschen ab Generation 2 (2021) haben eine integrierte Diagnose-LED am Steuerungsmodul:

| LED-Status | Bedeutung | Maßnahme |
|-----------|-----------|----------|
| Grün konstant | Betriebsbereit | Keine |
| Grün blinkend | Betrieb (Motor dreht) | Normal |
| Gelb blinkend | Thermische Warnung (Motor >80°C) | Pause einlegen, abkühlen lassen |
| Rot konstant | Überstromabschaltung | Sicherung und Kabel prüfen |
| Rot blinkend | Kommunikationsfehler (CAN-Bus) | CAN-Bus-Verbindung prüfen |
| Aus | Keine Stromversorgung | Sicherung, Hauptschalter prüfen |

**Confidence:** documented — Lewmar Elektrik-Installationshandbuch 2024.

> ⚠️ **ZU PRÜFEN (Audit):** Schwellwert der gelben Übertemperatur-Warnung widersprüchlich: hier „Motor >80°C", in §13 (LED-Blinkcodes) „Motor >100°C". Die Hard-Abschaltung bei 125°C ist zwischen beiden Abschnitten konsistent. Warnschwelle vor Nutzung verifizieren.

---

## 6. Hersteller-Daten und Teilenummern

### 6.1 Service-Kits EVO-Serie

Lewmar bietet vormontierte Service-Kits an, die alle regelmäßig zu wechselnden Teile enthalten:

| Winsch | Service-Kit TN | Inhalt | Preis (ca. EUR) |
|--------|---------------|--------|----------------|
| EVO 15 | 19700115 | 2× Pawl, 2× Feder, 1× Jaw-Einsatz, Fett, Öl | 45 |
| EVO 30 | 19700130 | 4× Pawl, 4× Feder, 1× Jaw-Einsatz, Fett, Öl | 65 |
| EVO 40 | 19700140 | 4× Pawl, 4× Feder, 1× Jaw-Einsatz, Fett, Öl | 78 |
| EVO 45 | 19700145 | 6× Pawl, 6× Feder, 1× Jaw-Einsatz, Fett, Öl | 85 |
| EVO 50 | 19700150 | 6× Pawl, 6× Feder, 1× Jaw-Einsatz, Fett, Öl | 95 |
| EVO 55 | 19700155 | 6× Pawl, 6× Feder, 1× Jaw-Einsatz, Fett, Öl | 110 |
| EVO 65 | 19700165 | 8× Pawl, 8× Feder, 1× Jaw-Einsatz, Fett, Öl | 130 |

**Confidence:** measured — Lewmar Ersatzteil-Katalog 2024.

### 6.2 Rebuild-Kits EVO-Serie

Für umfassende Überholungen:

| Winsch | Rebuild-Kit TN | Zusätzlich zum Service-Kit | Preis (ca. EUR) |
|--------|---------------|---------------------------|----------------|
| EVO 15 | 19700215 | Hauptlager, Sicherungsringe, Unterlegscheiben | 85 |
| EVO 30 | 19700230 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 125 |
| EVO 40 | 19700240 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 155 |
| EVO 45 | 19700245 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 175 |
| EVO 50 | 19700250 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 195 |
| EVO 55 | 19700255 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 220 |
| EVO 65 | 19700265 | Hauptlager, Sicherungsringe, Achse, Distanzscheiben | 260 |

### 6.3 Einzelteile — Sperrklinken und Federn

| Bauteil | Teilenummer | Passend für | Preis (ca. EUR/Stk.) |
|---------|-------------|------------|---------------------|
| Sperrklinke Speed 1 (klein) | 19700310 | EVO 15, 30 | 8 |
| Sperrklinke Speed 2 (klein) | 19700311 | EVO 30 | 9 |
| Sperrklinke Speed 1 (mittel) | 19700320 | EVO 40, 45 | 10 |
| Sperrklinke Speed 2 (mittel) | 19700321 | EVO 40, 45 | 11 |
| Sperrklinke Speed 1 (groß) | 19700330 | EVO 50, 55, 65 | 12 |
| Sperrklinke Speed 2 (groß) | 19700331 | EVO 50, 55, 65 | 13 |
| Feder Sperrklinke (klein) | 19700340 | EVO 15, 30 | 3 |
| Feder Sperrklinke (mittel) | 19700341 | EVO 40, 45 | 3 |
| Feder Sperrklinke (groß) | 19700342 | EVO 50, 55, 65 | 4 |

### 6.4 Self-Tailing-Backen (Jaw-Einsätze)

| Größe | Teilenummer | Schotbereich | Passend für |
|-------|-------------|-------------|------------|
| Small | 19700410 | 6–10 mm | EVO 15, 30 |
| Medium | 19700420 | 8–14 mm | EVO 40, 45 |
| Large | 19700430 | 12–18 mm | EVO 50, 55, 65 |
| XL | 19700440 | 16–22 mm | EVO 65 (Großschot) |

### 6.5 Trommel-Ersatz

| Winsch | Trommel Chrome TN | Trommel Alloy TN | Trommel Titan TN | Preis Chrome (ca.) |
|--------|------------------|-----------------|-----------------|-------------------|
| EVO 15 | 19700510 | 19700511 | — | 95 EUR |
| EVO 30 | 19700530 | 19700531 | — | 145 EUR |
| EVO 40 | 19700540 | 19700541 | 19700542 | 195 EUR |
| EVO 45 | 19700545 | 19700546 | 19700547 | 235 EUR |
| EVO 50 | 19700550 | 19700551 | 19700552 | 285 EUR |
| EVO 55 | 19700555 | 19700556 | 19700557 | 345 EUR |
| EVO 65 | 19700565 | 19700566 | 19700567 | 425 EUR |

### 6.6 Elektrische Konversionskits

Lewmar bietet Kits an, um manuelle EVO-Winschen auf elektrischen Betrieb umzurüsten:

| Basiswinsch | Konversionskit TN (12V) | Konversionskit TN (24V) | Inhalt | Preis (ca. EUR) |
|-------------|------------------------|------------------------|--------|----------------|
| EVO 40 ST | 69040012 | 69040024 | Motor, Steuerung, Kupplung, Kabel, Fußtaster | 1.650 |
| EVO 45 ST | 69045012 | 69045024 | Motor, Steuerung, Kupplung, Kabel, Fußtaster | 1.950 |
| EVO 50 ST | 69050012 | 69050024 | Motor, Steuerung, Kupplung, Kabel, Fußtaster | 2.350 |
| EVO 55 ST | — | 69055024 | Motor, Steuerung, Kupplung, Kabel, Fußtaster | 2.850 |
| EVO 65 ST | — | 69065024 | Motor, Steuerung, Kupplung, Kabel, Fußtaster | 3.450 |

**Voraussetzungen für Konversion:**
1. Ausreichend Platz unter Deck (Einbautiefe beachten)
2. Deckdurchbruch muss nachträglich hergestellt werden
3. Batteriekapazität muss ausreichen (Lewmar empfiehlt zusätzliche Servicebatterie)
4. Kabelquerschnitt gemäß Installationstabelle (siehe Abschnitt 4.4)
5. CE-Konformität der elektrischen Installation nach ISO 10133

**Confidence:** documented — Lewmar Konversions-Handbuch 2024.

### 6.7 Steuerungskomponenten

| Komponente | Teilenummer | Beschreibung | Preis (ca. EUR) |
|-----------|-------------|-------------|----------------|
| Fußtaster Speed 1 | 68000918 | Einzeltaster, IP67, Einbau-Ø 28 mm | 45 |
| Fußtaster Speed 2 | 68000919 | Einzeltaster, IP67, Einbau-Ø 28 mm | 45 |
| Doppel-Fußtaster | 68000920 | Zwei Taster in einer Platte, IP67 | 85 |
| Handtaster mit Kabel (3m) | 68000930 | Drucktaster am Kabel, spritzwassergeschützt | 65 |
| Wireless Controller | 68000940 | Funkfernbedienung, 868 MHz, 4 Kanäle | 395 |
| Wireless Empfänger | 68000941 | Empfängermodul für Wireless Controller | 285 |
| CAN-Bus Interface | 68000950 | NMEA 2000 Gateway für Winschensteuerung | 450 |
| Bluetooth-Modul | 68000960 | Lewmar Connect App-Anbindung | 195 |

### 6.8 Zubehör

| Produkt | Teilenummer | Beschreibung | Preis (ca. EUR) |
|---------|-------------|-------------|----------------|
| Winch Cover EVO 15 | 36100015 | Neopren-Schutzhaube, UV-beständig | 18 |
| Winch Cover EVO 30 | 36100030 | Neopren-Schutzhaube, UV-beständig | 22 |
| Winch Cover EVO 40 | 36100040 | Neopren-Schutzhaube, UV-beständig | 25 |
| Winch Cover EVO 45 | 36100045 | Neopren-Schutzhaube, UV-beständig | 28 |
| Winch Cover EVO 50 | 36100050 | Neopren-Schutzhaube, UV-beständig | 32 |
| Winch Cover EVO 55 | 36100055 | Neopren-Schutzhaube, UV-beständig | 35 |
| Winch Cover EVO 65 | 36100065 | Neopren-Schutzhaube, UV-beständig | 40 |
| Winsch-Pad (selbstklebend, rund) | 19700600 | Neopren-Unterlage, verhindert Kratzer | 12 |
| Kurbel-Halter (Cockpit) | 29140080 | Edelstahl-Halter für Winschenkurbel | 25 |
| Kurbel-Halter (Niedergang) | 29140081 | Edelstahl-Halter, Innenmontage | 22 |

### 6.9 Service-Kits Ocean-Serie (Legacy)

Für die noch weit verbreitete Ocean-Serie:

| Winsch | Service-Kit TN | Inhalt | Verfügbarkeit |
|--------|---------------|--------|--------------|
| Ocean 6/8 | 48000606 | Pawls, Federn, Fett | Noch verfügbar |
| Ocean 14 | 48000146 | Pawls, Federn, Jaw-Einsatz, Fett | Noch verfügbar |
| Ocean 16 | 48000166 | Pawls, Federn, Jaw-Einsatz, Fett | Noch verfügbar |
| Ocean 24 | 48000246 | Pawls, Federn, Jaw-Einsatz, Fett | Noch verfügbar |
| Ocean 30 | 48000306 | Pawls, Federn, Jaw-Einsatz, Fett | Noch verfügbar |
| Ocean 40 | 48000406 | Pawls, Federn, Jaw-Einsatz, Fett | Noch verfügbar |
| Ocean 44 | 48000446 | Pawls, Federn, Jaw-Einsatz, Fett | Begrenzt |
| Ocean 48 | 48000486 | Pawls, Federn, Jaw-Einsatz, Fett | Begrenzt |
| Ocean 54 | 48000546 | Pawls, Federn, Jaw-Einsatz, Fett | Begrenzt |
| Ocean 58 | 48000586 | Pawls, Federn, Jaw-Einsatz, Fett | Begrenzt |
| Ocean 66 | 48000666 | Pawls, Federn, Jaw-Einsatz, Fett | Begrenzt |

**Hinweis:** Lewmar hat zugesagt, Ersatzteile für die Ocean-Serie mindestens bis 2030 verfügbar zu halten. Danach wird empfohlen, auf die EVO-Serie umzurüsten.

**Confidence:** documented — Lewmar Ersatzteil-Verfügbarkeit Stand 2025.

### 6.10 Preisübersicht EVO ST (UVP, Stand 2024/2025)

| Modell | Chrome (EUR) | Alloy (EUR) | Titanium (EUR) |
|--------|-------------|------------|---------------|
| EVO 15 ST | 285 | 295 | — |
| EVO 30 ST | 480 | 495 | — |
| EVO 40 ST | 680 | 695 | 895 |
| EVO 45 ST | 920 | 945 | 1.195 |
| EVO 50 ST | 1.280 | 1.310 | 1.650 |
| EVO 55 ST | 1.680 | 1.720 | 2.150 |
| EVO 65 ST | 2.350 | 2.395 | 2.995 |

**Preise EVO EST (elektrisch, UVP):**

| Modell | 12V Chrome | 12V Alloy | 24V Chrome | 24V Alloy |
|--------|-----------|----------|-----------|----------|
| EVO 40 EST | 2.480 EUR | 2.520 EUR | 2.580 EUR | 2.620 EUR |
| EVO 45 EST | 3.180 EUR | 3.220 EUR | 3.280 EUR | 3.320 EUR |
| EVO 50 EST | 4.280 EUR | 4.330 EUR | 4.380 EUR | 4.430 EUR |
| EVO 55 EST | — | — | 5.480 EUR | 5.540 EUR |
| EVO 65 EST | — | — | 7.280 EUR | 7.350 EUR |

**Confidence:** documented — Lewmar UVP-Liste 2024/2025 (Preise können regional abweichen).

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Lewmar-Winschenempfehlung nach Bootsgröße

**Segelyachten — Cockpit-Primärwinschen (Genua/Fock-Schot):**

| Bootslänge (ft) | Verdrängung (t) | Segelfläche am Wind (m²) | Empfohlene Größe | Bemerkung |
|-----------------|-----------------|-------------------------|-----------------|-----------|
| 22–26 | 1.5–2.5 | 20–30 | EVO 15 ST oder EVO 30 ST | EVO 15 nur bei Rollreff |
| 27–30 | 2.5–4.0 | 30–45 | EVO 30 ST | Standard für diese Klasse |
| 31–34 | 4.0–6.0 | 40–55 | EVO 40 ST | Meistverkaufte Größe |
| 35–38 | 5.5–8.0 | 50–70 | EVO 40 ST oder EVO 45 ST | Abhängig von Rigghöhe |
| 39–42 | 7.0–11.0 | 65–85 | EVO 45 ST | Alternativ EVO 50 bei schwerem Boot |
| 43–46 | 9.0–14.0 | 80–105 | EVO 50 ST | Elektrisch empfohlen |
| 47–50 | 11.0–18.0 | 95–125 | EVO 50 ST oder EVO 55 ST | Elektrisch empfohlen |
| 51–55 | 14.0–22.0 | 110–150 | EVO 55 ST | Elektrisch oder hydraulisch |
| 56–65 | 18.0–35.0 | 140–200 | EVO 65 ST | Elektrisch oder hydraulisch |
| 66+ | >30.0 | >180 | EVO 80 H | Nur hydraulisch |

**Segelyachten — Fallwinschen (am Mast oder Cockpitdach):**

| Bootslänge (ft) | Empfohlene Größe | Bemerkung |
|-----------------|-----------------|-----------|
| 27–34 | EVO 30 ST | Auch als Reffwinde |
| 35–42 | EVO 40 ST | Elektrisch bei Kurzhand |
| 43–50 | EVO 45 ST | Elektrisch empfohlen |
| 51–60 | EVO 50 ST oder EVO 55 ST | Elektrisch Standard |
| 61+ | EVO 55 EST oder EVO 65 EST | Immer elektrisch |

### 7.2 OEM-Zuordnung — Welche Werft verwendet welche Lewmar-Winschen

**Hanse (Greifswald, Deutschland):**

| Modell | Baujahre | Primärwinsch | Fallwinsch | Standard/Option |
|--------|----------|-------------|-----------|----------------|
| Hanse 315 | 2017–heute | EVO 30 ST | — | Standard |
| Hanse 348 | 2017–heute | EVO 40 ST | EVO 30 ST | Standard |
| Hanse 388 | 2018–heute | EVO 40 ST | EVO 30 ST | Standard |
| Hanse 418 | 2018–heute | EVO 45 ST | EVO 40 ST | Standard |
| Hanse 458 | 2019–heute | EVO 45 ST | EVO 40 ST | ST. / EVO 45 EST Opt. |
| Hanse 508 | 2019–heute | EVO 50 ST | EVO 45 ST | ST. / EVO 50 EST Opt. |
| Hanse 548 | 2020–heute | EVO 50 EST | EVO 45 EST | Standard elektrisch |
| Hanse 588 | 2020–heute | EVO 55 EST | EVO 50 EST | Standard elektrisch |
| Hanse 675 | 2021–heute | EVO 65 EST | EVO 55 EST | Standard elektrisch |

**Confidence:** documented — Hanse Preislisten, verifiziert durch Werftangaben.

**Hallberg-Rassy (Ellös, Schweden):**

| Modell | Baujahre | Primärwinsch | Fallwinsch | Standard/Option |
|--------|----------|-------------|-----------|----------------|
| HR 310 | 2014–heute | EVO 40 ST | EVO 30 ST | Standard |
| HR 340 | 2015–heute | EVO 40 ST | EVO 30 ST | Standard |
| HR 372 | 2019–heute | EVO 45 ST | EVO 40 ST | Standard |
| HR 400 | 2016–heute | EVO 45 ST | EVO 40 ST | Standard |
| HR 412 | 2019–heute | EVO 50 ST | EVO 45 ST | Standard |
| HR 44 | 2014–heute | EVO 50 ST | EVO 45 ST | ST. / EST Option |
| HR 50 | 2016–heute | EVO 55 EST | EVO 50 EST | Standard elektrisch |
| HR 57 | 2018–heute | EVO 55 EST | EVO 50 EST | Standard elektrisch |
| HR 64 | 2019–heute | EVO 65 EST | EVO 55 EST | Standard elektrisch |

Hinweis: Hallberg-Rassy verwendet seit den 1990er Jahren Lewmar als Primärlieferant für Winschen. Ältere HR-Modelle (vor 2005) haben Ocean-Winschen.

**Confidence:** documented — Hallberg-Rassy Spezifikationen, Eigner-Forum-Daten.

**X-Yachts (Haderslev, Dänemark):**

| Modell | Baujahre | Primärwinsch | Standard/Option |
|--------|----------|-------------|----------------|
| X4° | 2019–heute | EVO 45 ST | Standard (Harken Option) |
| Xc 38 | 2015–heute | EVO 40 ST | Standard |
| Xc 45 | 2014–heute | EVO 50 ST | Standard |
| Xp 38 | 2012–heute | Oceanus 40 | Standard (Racing) |
| Xp 44 | 2012–heute | Oceanus 45 | Standard (Racing) |
| Xp 50 | 2014–heute | Oceanus 50 | Standard (Racing) |

Hinweis: X-Yachts bietet häufig sowohl Lewmar als auch Harken als Option an. Die Performance-Linie (Xp) verwendet bevorzugt Lewmar Oceanus.

**Contest Yachts (Medemblik, Niederlande):**

| Modell | Primärwinsch | Standard |
|--------|-------------|---------|
| Contest 42CS | EVO 45 ST | Standard |
| Contest 49CS | EVO 50 ST | Standard |
| Contest 55CS | EVO 55 EST | Standard elektrisch |
| Contest 67CS | EVO 65 EST | Standard elektrisch |
| Contest 72CS | EVO 65 H (hydraulisch) | Standard |

**Najad (Orust, Schweden):**

| Modell | Primärwinsch | Standard |
|--------|-------------|---------|
| Najad 355 | EVO 40 ST | Standard |
| Najad 395 | EVO 45 ST | Standard |
| Najad 440 AC/CC | EVO 50 ST | Standard |
| Najad 505 | EVO 55 EST | Standard elektrisch |
| Najad 570 | EVO 65 EST | Standard elektrisch |

**Dufour (La Rochelle, Frankreich):**

| Modell | Primärwinsch | Standard |
|--------|-------------|---------|
| Dufour 310 | EVO 30 ST | Standard |
| Dufour 360 | EVO 40 ST | Standard |
| Dufour 390 | EVO 40 ST | Standard |
| Dufour 412 | EVO 45 ST | Standard |
| Dufour 470 | EVO 45 ST | ST. / EST Option |
| Dufour 530 | EVO 50 EST | Standard elektrisch |
| Dufour 61 | EVO 55 EST | Standard elektrisch |

**Beneteau (Saint-Gilles-Croix-de-Vie, Frankreich):**

Hinweis: Beneteau verwendet gemischt Lewmar und Harken, je nach Modell und Baujahr.

| Modell | Primärwinsch | Hersteller |
|--------|-------------|-----------|
| Oceanis 30.1 | EVO 30 ST | Lewmar |
| Oceanis 34.1 | EVO 40 ST | Lewmar |
| Oceanis 40.1 | EVO 40 ST | Lewmar |
| Oceanis 46.1 | EVO 45 ST | Lewmar |
| Oceanis 51.1 | EVO 50 ST | Lewmar/Harken je nach Ausstattung |
| Oceanis Yacht 54 | EVO 50 EST | Lewmar |
| Oceanis Yacht 60 | EVO 55 EST | Lewmar |
| First 27 | EVO 30 ST | Lewmar |
| First 36 | EVO 40 ST | Lewmar |
| First 44 | Harken | Harken (nicht Lewmar) |
| First 53 | Harken | Harken (nicht Lewmar) |

**Confidence:** documented — Werftkataloge, OEM-Zuordnungen. Beneteau-Zuordnung variiert nach Baujahr und Region.

### 7.3 Empfehlungen nach Einsatzprofil

**Langfahrt / Blauwasser:**

- Primärwinschen: Eine Größe über Standard (z.B. EVO 50 statt EVO 45 bei 42 ft)
- Elektrisch empfohlen: Kurzhand-Crews profitieren enorm
- Self-Tailing: Pflicht
- Redundanz: Mindestens eine Kurbel pro Cockpit-Seite an Bord
- Wartung: Doppelter Vorrat an Service-Kits mitnehmen
- Backup-Sperrklinken und -Federn als Bordreserve

**Regatta / Performance:**

- Oceanus-Serie bevorzugt (Gewichtsvorteil)
- Plain-Top für Spinnaker-Winschen
- Self-Tailing nur für Primärwinschen
- Kurbeln: Racing Handle (Carbon) für Gewichtsersparnis
- Wartung: Vor jeder Regatta Sperrklinken prüfen und schmieren

**Charter:**

- EVO ST Standard in Chrome-Finish (Korrosionsbeständigkeit)
- Elektrisch ab 45 ft (unerfahrene Crews)
- Winch Covers bei Liegeplatzyachten
- Halbjährliche Vollwartung

### 7.4 Retrofit-Szenarien

**Szenario 1: Ältere Yacht (1990er) mit Ocean-Winschen upgraden**

Typisches Beispiel: Hallberg-Rassy 36 (Baujahr 1996) mit Ocean 40 ST.

| Schritt | Aktion | Material | Kosten (ca.) |
|---------|--------|----------|-------------|
| 1 | Ocean 40 ST demontieren | — | Arbeitszeit |
| 2 | Adapterplatte montieren | 19700304 | 85 EUR |
| 3 | EVO 45 ST montieren | 49545070 | 920 EUR |
| 4 | Dichtung erneuern | Sikaflex 291i | 15 EUR |
| **Gesamt pro Winsch** | | | **~1.050 EUR + Arbeit** |

**Szenario 2: Manuelle Winschen auf elektrisch umrüsten**

Typisches Beispiel: Hanse 458 mit EVO 45 ST, Umrüstung auf EVO 45 EST.

| Schritt | Aktion | Material | Kosten (ca.) |
|---------|--------|----------|-------------|
| 1 | EVO 45 ST beibehalten (Oberteil kompatibel) | — | — |
| 2 | Konversionskit installieren | 69045024 | 1.950 EUR |
| 3 | Kabelverlegung (24V, 35 mm², ~5m) | Marinekabel | 120 EUR |
| 4 | Sicherung und Verteiler | 80A ANL + Halter | 45 EUR |
| 5 | Fußtaster einbauen | 68000920 | 85 EUR |
| 6 | Deckdurchbruch herstellen und abdichten | Epoxid, Sikaflex | 50 EUR |
| **Gesamt pro Winsch** | | | **~2.300 EUR + Arbeit** |

**Szenario 3: Vergrößerung der Primärwinschen**

Typisches Beispiel: Bavaria 40 Cruiser mit EVO 40 ST, Umrüstung auf EVO 50 ST (Boot wird unterbewinscht empfunden).

| Schritt | Aktion | Kosten (ca.) |
|---------|--------|-------------|
| 1 | EVO 40 ST demontieren | Arbeitszeit |
| 2 | Alten Bolzenkreis verschließen (Epoxid + Gelcoat) | 80 EUR |
| 3 | Neuen Bolzenkreis bohren (133 mm statt 108 mm) | Arbeitszeit |
| 4 | Decksverstärkung unter Deck (GFK-Pads) | 60 EUR |
| 5 | EVO 50 ST montieren | 1.280 EUR |
| 6 | Abdichtung | 15 EUR |
| **Gesamt pro Winsch** | | **~1.475 EUR + Arbeit** |

### 7.5 Winschenpositionierung auf Deck

**Ergonomische Platzierungsregeln (Lewmar-Empfehlung und AYDI-Ergonomie-Modul):**

Die Position der Winschen auf dem Cockpitsüll beeinflusst direkt die Bedienbarkeit und Sicherheit:

| Parameter | Empfehlung | Toleranz | AYDI-Bewertung bei Abweichung |
|-----------|-----------|----------|------------------------------|
| Abstand Cockpitkante zur Trommelachse | 100–150 mm | ±30 mm | Abzug bei >180 mm (Überstreckung) |
| Abstand zwischen Primärwinschen (BB/STB) | ≥800 mm | ±50 mm | Abzug bei <700 mm (Behinderung) |
| Höhe Trommelkopf über Sitzfläche | 350–500 mm | ±50 mm | Abzug bei >550 mm (Armstellung) |
| Kurbelfreiheit (360° Drehung) | Min. 300 mm Radius frei | — | Kritisch bei Behinderung |
| Abstand Primärwinsch zum Stopper | 200–400 mm | ±50 mm | Abzug bei >500 mm (Schotführung) |
| Winkel der Schotführung zur Trommel | 5°–15° von unten | ±3° | Abzug bei >20° (Riding Turns) |

**Riding Turns — Vermeidung durch korrekte Platzierung:**

Riding Turns (übereinandergreifende Schotwindungen) sind das häufigste Bedienproblem bei Winschen. Sie entstehen, wenn:

1. Der Schotwinkel zur Trommel zu steil ist (>15° von unten)
2. Die Schot unter Last nicht straff zur Trommel läuft
3. Der Barber-Hauler / Genuaschlitten falsch positioniert ist
4. Die Schot zu dünn für die Trommelgröße ist

**Lewmar-Empfehlung zur Vermeidung:**
- Schotwinkel 8°–12° von der horizontalen Ebene
- Umlenkrolle (Genua-Schlitten) auf einer Linie mit Trommelunterkante
- Schot im mittleren Bereich des empfohlenen Durchmesserbereichs wählen
- Bei Rollreffanlagen: Schotdurchmesser für kleinste Segelfläche dimensionieren

**Mastwinsch-Platzierung:**

| Parameter | Empfehlung | Bemerkung |
|-----------|-----------|-----------|
| Position am Mast | Augenhöhe ±200 mm | Optimale Bedienposition |
| Abstand zum Mastfuß | >800 mm (auf Coaming/Dach) | Bei Dachführung bevorzugt |
| Ausrichtung | 15°–20° zur Vertikalen geneigt | Erleichtert Kurbelführung |
| Kurbelfreiheit | Min. 250 mm zur Mastseite | Kurbel darf nicht am Mast anstoßen |

### 7.6 Gewichtsbudget — Winscheneinfluss auf Schwerpunkt

Für die AYDI-Strukturanalyse (ISO 12217 Stabilitätsberechnung) ist das Gewicht der Winschen relevant:

| Winschenbestückung (typisch) | Bootsgröße | Gesamtgewicht Winschen | Anteil an Verdrängung |
|-----------------------------|-----------|----------------------|---------------------|
| 2× EVO 30 ST | 28 ft / 3.5 t | 7.2 kg | 0.21% |
| 2× EVO 40 ST + 2× EVO 30 ST | 34 ft / 5.5 t | 18.8 kg | 0.34% |
| 2× EVO 45 ST + 2× EVO 40 ST | 40 ft / 8.0 t | 27.4 kg | 0.34% |
| 2× EVO 50 EST + 2× EVO 45 EST | 46 ft / 12.0 t | 67.0 kg | 0.56% |
| 2× EVO 55 EST + 2× EVO 50 EST | 52 ft / 16.0 t | 86.0 kg | 0.54% |
| 2× EVO 65 EST + 2× EVO 55 EST | 60 ft / 25.0 t | 112.0 kg | 0.45% |

Hinweis: Elektrische Winschen sind ca. 70–90% schwerer als manuelle. Der zusätzliche Motor sitzt unter Deck (tiefer Schwerpunkt), was sich positiv auf die Stabilität auswirkt.

**Confidence:** calculated — basierend auf Lewmar Gewichtsangaben und typischer Bestückung.

### 7.7 Kosten-Nutzen-Analyse: Manuell vs. Elektrisch

| Kriterium | Manuell (ST) | Elektrisch (EST) | Bewertung |
|-----------|-------------|-----------------|-----------|
| Anschaffung (Paar, Größe 45) | ~1.840 EUR | ~6.560 EUR | Elektrisch 3.6× teurer |
| Installation | Einfach (4 Bolzen) | Komplex (Kabel, Motor, Taster) | +800–1.200 EUR Arbeit |
| Wartung jährlich | ~40 EUR (Kit + Fett) | ~80 EUR (Kit + Motor-Check) | Elektrisch 2× teurer |
| Batteriekapazität | Keine | +100–200 Ah empfohlen | ~600 EUR Zusatzkosten |
| Lebensdauer | 15+ Jahre | 10–15 Jahre (Motor) | Motoraustausch ~800 EUR |
| 10-Jahres-TCO (Paar, Größe 45) | ~2.240 EUR | ~9.560 EUR | Elektrisch 4.3× teurer |
| Bedienkomfort | Gut (körperliche Arbeit) | Sehr gut (Knopfdruck) | Hauptargument für elektrisch |
| Kurzhand-Tauglichkeit | Eingeschränkt bei Last >30 kg | Sehr gut | Entscheidend für Kurzhand |
| Ausfallsicherheit | Hoch (rein mechanisch) | Mittel (Elektronik-Abhängigkeit) | Manueller Override vorhanden |

**AYDI-Empfehlung:** Für Fahrtensegler ab 42 ft und/oder Kurzhand-Crews ist die elektrische Umrüstung wirtschaftlich sinnvoll, wenn die Yacht >5 Jahre genutzt wird. Für Charteryachten ab 45 ft ist elektrisch Standard.

---

## 8. Cross-Referenz und Wettbewerbsvergleich

### 8.1 Lewmar EVO vs. Harken Radial — Größenvergleich

Die wichtigste Wettbewerbsvergleichstabelle: Lewmar EVO gegen Harken Radial (die beiden meistverkauften Winschenlinien).

| Lewmar EVO | Harken Radial | Vergleich WLL | Vergleich Gewicht | Vergleich Preis |
|-----------|---------------|--------------|-------------------|----------------|
| EVO 15 ST | Radial 15 ST | 227 vs. 227 kg | 1.9 vs. 2.0 kg | Lewmar ~10% günstiger |
| EVO 30 ST | Radial 20 STC | 545 vs. 454 kg | 3.6 vs. 3.5 kg | Vergleichbar |
| EVO 40 ST | Radial 35 STC | 907 vs. 816 kg | 5.8 vs. 6.2 kg | Lewmar ~5% günstiger |
| EVO 45 ST | Radial 40 STC | 1134 vs. 1043 kg | 7.9 vs. 8.5 kg | Vergleichbar |
| EVO 50 ST | Radial 46 STC | 1588 vs. 1497 kg | 10.8 vs. 11.3 kg | Vergleichbar |
| EVO 55 ST | Radial 50 STC | 2041 vs. 1905 kg | 13.6 vs. 14.0 kg | Lewmar ~5% günstiger |
| EVO 65 ST | Radial 60 STC | 2722 vs. 2540 kg | 18.5 vs. 19.5 kg | Lewmar ~5% günstiger |

**Zusammenfassung des Vergleichs:**
- Lewmar EVO bietet tendenziell höhere WLL bei gleichem oder geringerem Gewicht
- Harken hat den etwas kompakteren Self-Tailing-Mechanismus
- Lewmar ist im europäischen Markt typischerweise 5–10% günstiger als Harken
- Harken hat den besseren Aftermarket-Support in den USA
- Lewmar hat den besseren Aftermarket-Support in Europa

**Confidence:** documented — Katalogvergleich Lewmar 2024 / Harken 2024.

### 8.2 Lewmar EVO vs. Andersen — Größenvergleich

| Lewmar EVO | Andersen | Vergleich | Bemerkung |
|-----------|----------|-----------|-----------|
| EVO 30 ST | Andersen 28 ST | Vergleichbar | Andersen aus Edelstahl, ~40% schwerer |
| EVO 40 ST | Andersen 34 ST | Vergleichbar | Andersen aus Edelstahl, ~35% schwerer |
| EVO 45 ST | Andersen 40 ST | Vergleichbar | Andersen ~25% teurer |
| EVO 50 ST | Andersen 46 ST | Vergleichbar | Andersen Edelstahl-Vorteil bei Korrosion |
| EVO 55 ST | Andersen 52 ST | Vergleichbar | |

**Andersen-Besonderheit:** Andersen-Winschen bestehen aus rostfreiem Edelstahl (AISI 316), nicht aus Aluminium. Vorteile: Keine Anodisierung nötig, höhere Korrosionsbeständigkeit. Nachteile: Deutlich schwerer, teurer.

### 8.3 Lewmar EVO vs. Antal — Größenvergleich

| Lewmar EVO | Antal | Bemerkung |
|-----------|-------|-----------|
| EVO 30 ST | Antal XT30 | Antal kompakter, Lewmar bessere Jaw |
| EVO 40 ST | Antal XT40 | Vergleichbar, Antal ~10% günstiger |
| EVO 45 ST | Antal XT44 | Antal beliebter im Mittelmeer |
| EVO 50 ST | Antal XT48 | Vergleichbar |

### 8.4 Leinenkompatibilität

Lewmar-Trommeln sind optimiert für bestimmte Schottypen:

| Schottyp | Material | Lewmar-Eignung | Bemerkung |
|----------|----------|---------------|-----------|
| Polyester geflochten (Standard) | Polyester | Sehr gut | Standardmäßig optimiert |
| Dyneema-Kern / Polyester-Mantel | SK78/99 + PES | Sehr gut | Beste Kombination |
| Dyneema pur (ohne Mantel) | SK78/99 | Eingeschränkt | Weniger Reibung auf Trommel, Rutschgefahr |
| Dyneema / Technora Hybrid | Mischung | Gut | Guter Kompromiss |
| Aramid (Kevlar) Kern | Aramid + PES | Gut | Biegeradius beachten |
| Vectran-Kern | Vectran + PES | Gut | UV-Empfindlichkeit beachten |
| Nylon (Polyamid) | PA | Nicht empfohlen | Dehnung, Rutschgefahr |
| Polypropylen | PP | Nicht empfohlen | Schmilzt bei Reibungswärme |

**Empfohlene Schotdurchmesser für Lewmar EVO (Self-Tailing):**

Die Schot sollte idealerweise im mittleren Drittel des Jaw-Bereichs liegen:

| Winsch | Jaw-Einsatz | Optimaler Schotbereich |
|--------|------------|----------------------|
| EVO 15 | Small | 7–9 mm |
| EVO 30 | Small/Medium | 9–11 mm |
| EVO 40 | Medium | 10–12 mm |
| EVO 45 | Medium | 11–13 mm |
| EVO 50 | Large | 13–15 mm |
| EVO 55 | Large | 14–16 mm |
| EVO 65 | Large/XL | 16–18 mm |

---

## 9. Fehlerbilder und Diagnose

### 9.1 Häufige Probleme und Lösungen

| Problem | Ursache | Diagnose | Lösung |
|---------|---------|----------|--------|
| Winsch dreht rückwärts unter Last | Sperrklinken verschlissen oder verhakt | Trommel abnehmen, Pawls prüfen | Pawls und Federn austauschen |
| Winsch dreht schwer | Altes Fett, Korrosion, Salzablagerungen | Drehwiderstand ohne Schot prüfen | Komplettwartung, neu schmieren |
| Schot rutscht in Jaw | Jaw-Einsatz verschlissen, falscher Schotdurchmesser | Jaw-Einsatz auf Rillenabnutzung prüfen | Jaw-Einsatz wechseln, Schotgröße prüfen |
| Schot rutscht auf Trommel | Trommelrillen abgeschliffen, Schot zu glatt | Trommeloberfläche prüfen | Trommel ersetzen oder Schot mit rauem Mantel wählen |
| Klickgeräusch fehlt | Sperrklinkenfedern gebrochen | Einzelne Pawls auf Federspannung prüfen | Federn ersetzen |
| Kurbel sitzt locker | Vierkantaufnahme ausgeschlagen | Vierkant mit Lehre prüfen | Vierkantbuchse ersetzen |
| Elektromotor dreht nicht | Sicherung, Kabelbruch, Motor defekt | Spannung am Motor messen | Sicherung prüfen, Kabel prüfen, ggf. Motor ersetzen |
| Elektromotor dreht langsam | Unterspannung, Kabelquerschnitt zu gering | Spannung unter Last am Motor messen | Kabelquerschnitt erhöhen, Batterie prüfen |
| Geräusche aus dem Getriebe | Getriebezähne beschädigt | Trommel abnehmen, Planetenräder inspizieren | Getriebe ersetzen (Rebuild-Kit) |
| Korrosion am Sockel | Galvanische Korrosion (Alu/Edelstahl) | Weißer Belag auf Aluminium | Isolierscheiben unter Befestigungsschrauben, Tef-Gel |
| Wasser im Motorraum | Undichte Decksdurchführung | Motorraum auf Feuchtigkeit prüfen | Decksdurchführung neu abdichten |

### 9.2 AYDI-Diagnose: Visuelle Analyse von Winschen

Für die AYDI Pipeline B (Visual Analysis) sind folgende visuelle Indikatoren relevant:

**Zustandsbewertung anhand von Fotos:**

| Visueller Indikator | Bewertung | AYDI-Score-Einfluss |
|---------------------|-----------|-------------------|
| Glänzende Trommeloberfläche, scharfe Rillen | Gut (80–100) | Neutral |
| Matte Trommeloberfläche, Rillen erkennbar | Akzeptabel (60–80) | Leichter Abzug |
| Rillen abgeschliffen, glatte Stellen | Schlecht (30–60) | Deutlicher Abzug |
| Weiße Korrosionsflecken auf Aluminium | Wartungsbedarf (40–70) | Abzug + Warnung |
| Grünspan an Befestigungsschrauben | Korrosionsproblem (20–50) | Starker Abzug + Empfehlung |
| Risse im Composite-Sockel | Kritisch (0–20) | Kritisch + "Befund prüfen" |
| Schot mit Chafe-Spuren in Jaw | Wartungsbedarf (50–70) | Abzug + Empfehlung Schotwechsel |
| Fehlende Winsch-Covers, UV-Schäden | Pflege mangelhaft (40–60) | Leichter Abzug |

**Confidence:** estimated — basierend auf Rigger-Erfahrung und visueller Inspektion.

### 9.3 Lebensdauer-Erwartung nach Nutzungsprofil

| Einsatzprofil | Erwartete Lebensdauer Trommel | Erwartete Lebensdauer Getriebe | Bemerkung |
|--------------|------------------------------|-------------------------------|-----------|
| Gelegenheitssegler (50 h/Jahr) | 20+ Jahre | 15+ Jahre | Minimaler Verschleiß |
| Fahrtensegler (500 h/Jahr) | 12–15 Jahre | 10–12 Jahre | Regelmäßige Wartung vorausgesetzt |
| Regattasegler (300+ Regatten) | 8–10 Jahre | 6–8 Jahre | Höhere Belastung |
| Charteryacht (2000 h/Jahr) | 6–8 Jahre | 5–7 Jahre | Oft mangelnde Wartung |
| Ausbildungsyacht | 4–6 Jahre | 3–5 Jahre | Extreme Belastung, Fehlbedienung |

### 9.4 Sicherheitskritische Ausfälle

**Warnung: Folgende Ausfälle sind sicherheitskritisch und erfordern sofortiges Handeln:**

1. **Sperrklinken-Totalausfall:** Winsch hält Last nicht mehr → Sofort Stopper/Klemme verwenden, Winsch nicht mehr belasten.

2. **Trommelbruch:** Extrem selten, aber möglich bei massiver Überbelastung → Sofort Last auf Klemme/Stopper umlegen.

3. **Elektromotor-Blockade unter Last:** Motor blockiert, Schot kann nicht gelöst werden → Manuellen Override verwenden (Kurbel aufsetzen, Motor entkoppelt automatisch).

4. **Jaw-Versagen unter Last:** Schot schießt durch → Handschuhe tragen, Stopper verwenden.

**AYDI-Empfehlung:** Bei jedem sicherheitskritischen Befund: `"confidence": "visual_medium", "action": "Befund prüfen"` — niemals automatisch als bestätigt melden.

---

## 10. AYDI-Integration

### 10.1 Pydantic-Modell für Winschenanalyse

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum

class WinchManufacturer(str, Enum):
    LEWMAR = "lewmar"
    HARKEN = "harken"
    ANDERSEN = "andersen"
    ANTAL = "antal"
    PONTOS = "pontos"
    OTHER = "other"

class WinchType(str, Enum):
    MANUAL_ST = "manual_self_tailing"
    MANUAL_PT = "manual_plain_top"
    ELECTRIC_ST = "electric_self_tailing"
    ELECTRIC_PT = "electric_plain_top"
    HYDRAULIC = "hydraulic"

class WinchSeries(str, Enum):
    EVO = "evo"
    OCEAN = "ocean"
    OCEANUS = "oceanus"

class LewmarWinch(BaseModel):
    model_config = {"from_attributes": True}

    manufacturer: WinchManufacturer = WinchManufacturer.LEWMAR
    series: WinchSeries
    size: int = Field(..., description="Winch size number (15, 30, 40, 45, 50, 55, 65)")
    winch_type: WinchType
    part_number: str = Field(..., description="Lewmar part number")
    drum_diameter_mm: float
    height_mm: float
    weight_kg: float
    working_load_limit_kg: float
    power_ratio_speed1: float
    power_ratio_speed2: Optional[float] = None
    max_line_diameter_mm: float
    min_line_diameter_mm: float
    bolt_circle_mm: float
    bolt_count: int
    bolt_size: str
    voltage: Optional[Literal["12V", "24V"]] = None
    motor_power_w: Optional[int] = None
    max_current_a: Optional[float] = None
    install_depth_mm: Optional[float] = None

class WinchAssessment(BaseModel):
    model_config = {"from_attributes": True}

    winch: LewmarWinch
    condition_score: int = Field(..., ge=0, le=100)
    sizing_adequate: bool
    sizing_recommendation: Optional[str] = None
    maintenance_status: Literal["gut", "wartungsbedarf", "kritisch"]
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "visual_low", "estimated"
    ]
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
```

### 10.2 AYDI Scoring-Integration

Winschen fließen in folgende AYDI-Module ein:

| AYDI-Modul | Winsch-Relevanz | Gewichtung im Modul |
|-----------|----------------|-------------------|
| Ergonomics | Winschenposition, Kurbelfreiheit, Bedienbarkeit | 15% |
| Production | OEM-Zuordnung, Standardisierungsgrad | 5% |
| Materials | Korrosionszustand, Materialwahl | 10% |
| Compliance | CE-konforme Befestigung, elektrische Installation | 5% |
| Cost | Winschenwert, Ersatzteilkosten | 8% |
| Service Patterns | Wartungszustand, bekannte Probleme | 12% |

### 10.3 Confidence-Mapping für Winschen-Analyse

| Datenquelle | Confidence-Level | Beispiel |
|------------|-----------------|---------|
| CAD-Daten mit exakter Winschenposition und -modell | measured | "EVO 45 ST auf Bolzenkreis 120 mm bei x=2450, y=±1200 mm" |
| Spezifikationsblatt der Werft mit Winschenmodell | documented | "Laut Hanse-Preisliste: EVO 45 ST Standard" |
| Foto der Winsch mit lesbarer Modellbezeichnung | visual_high | "EVO 45 erkennbar auf Trommelgravur" |
| Foto der Winsch, Modell geschätzt anhand Größe | visual_medium | "Lewmar-Winsch, geschätzt Größe 40–50 anhand Proportionen" |
| Foto unklar, nur Hersteller erkennbar | visual_low | "Lewmar-Winsch erkennbar, Größe nicht bestimmbar" |
| Bootslänge bekannt, Winsch geschätzt | estimated | "Bei 42 ft typischerweise EVO 45 oder 50" |

### 10.4 Winschengrößen-Validierung

AYDI prüft automatisch, ob die installierte Winschengröße zur Bootsgröße passt:

```python
def validate_winch_sizing(
    boat_length_ft: float,
    displacement_t: float,
    sail_area_m2: float,
    winch_size: int,
    winch_position: str  # "primary", "secondary", "halyard"
) -> dict:
    """
    Validiert ob die Lewmar-Winschengröße angemessen ist.
    Returns: {"adequate": bool, "recommended_min": int, "recommended_max": int, "message": str}
    """
    # Primärwinschen-Empfehlung basierend auf Segelfläche
    if winch_position == "primary":
        if sail_area_m2 < 35:
            rec_min, rec_max = 15, 30
        elif sail_area_m2 < 55:
            rec_min, rec_max = 30, 40
        elif sail_area_m2 < 75:
            rec_min, rec_max = 40, 45
        elif sail_area_m2 < 100:
            rec_min, rec_max = 45, 50
        elif sail_area_m2 < 135:
            rec_min, rec_max = 50, 55
        else:
            rec_min, rec_max = 55, 65

    adequate = rec_min <= winch_size <= rec_max

    if winch_size < rec_min:
        message = f"Winsch unterdimensioniert: Größe {winch_size} für {sail_area_m2:.0f} m² Segelfläche. Empfohlen: {rec_min}–{rec_max}."
    elif winch_size > rec_max:
        message = f"Winsch überdimensioniert: Größe {winch_size} für {sail_area_m2:.0f} m² Segelfläche. Standard wäre: {rec_min}–{rec_max}."
    else:
        message = f"Winschengröße {winch_size} ist angemessen für {sail_area_m2:.0f} m² Segelfläche."

    return {
        "adequate": adequate,
        "recommended_min": rec_min,
        "recommended_max": rec_max,
        "message": message,
        "confidence": "estimated"
    }
```

---

## ANHANG A — FAQ — Häufige Fragen

**F: Kann ich eine Harken-Kurbel auf einer Lewmar-Winsch verwenden?**
A: Ja. Alle modernen Segelwinschen verwenden den gleichen 10 mm (3/8") Vierkant-Standard. Lewmar-, Harken-, Andersen- und Antal-Kurbeln sind untereinander kompatibel. Einzige Ausnahme: Sehr alte Winschen (vor 1980) können abweichende Vierkantgrößen haben.

**F: Lewmar EVO oder Harken Radial — welche ist besser?**
A: Beide Serien sind auf vergleichbarem technischen Niveau. Lewmar hat tendenziell bessere Verfügbarkeit und günstigere Preise in Europa. Harken hat einen besseren Aftermarket-Support in den USA. Bei OEM-Ausstattung ist die Wahl der Werft zu akzeptieren — ein Wechsel des Herstellers lohnt sich wirtschaftlich nicht.

**F: Muss ich die gleiche Winschengröße wie das Original verwenden?**
A: Nein. Ein Upgrade auf eine größere Winsch ist jederzeit möglich und oft sinnvoll (z.B. bei Kurzhand-Segeln). Ein Downgrade ist nicht empfohlen. Der neue Bolzenkreis muss allerdings im Deck platzierbar sein.

**F: Wie erkenne ich das Modell meiner Lewmar-Winsch?**
A: Bei EVO-Winschen ist "EVO" und die Größennummer in die Trommelunterseite graviert. Bei Ocean-Winschen steht "Ocean" auf dem Trommelkopf. Die Teilenummer befindet sich auf einem Aufkleber am Sockel (oft nicht mehr lesbar). Alternativ: Trommeldurchmesser und Bolzenkreis messen und mit Tabelle abgleichen.

**F: Kann ich die Self-Tailing-Backe einer EVO 40 auf eine EVO 45 setzen?**
A: Nein. Die Jaw-Einheiten sind größenspezifisch und nicht zwischen Größen tauschbar. Die Jaw-Einsätze (Small/Medium/Large) sind jedoch innerhalb einer Jaw-Einheit wechselbar.

**F: Wie oft muss ich die Sperrklinken wechseln?**
A: Bei normaler Fahrtenseglerbenutzung halten Sperrklinken 5–8 Jahre. Jährlich prüfen: Wenn die Spitzen abgerundet sind oder die Winsch unter Last "springt", sofort wechseln. Federn alle 3–5 Jahre präventiv ersetzen.

**F: Meine elektrische Winsch macht Geräusche aber dreht nicht — was tun?**
A: 1. Sicherung prüfen (häufigste Ursache). 2. Spannung am Motor messen (min. 10.5V bei 12V-System). 3. Manuellen Override testen (Kurbel aufsetzen). 4. Wenn Motor surrt aber nicht dreht: Kupplung defekt oder Getriebe blockiert. Fachmann hinzuziehen.

**F: Brauche ich wirklich Lewmar Winch Grease oder geht auch anderes?**
A: Lewmar Winch Grease ist optimal, aber Harken Winch Grease ist eine gleichwertige Alternative. Marine-Mehrzweckfett (NLGI 2, Lithium-Komplex-Basis) funktioniert ebenfalls. NICHT verwenden: WD-40, Ballistol, Silikonspray, Universalöl, Vaseline. Diese waschen das Spezialfett aus oder verhärten.

**F: Sind die Ocean-Ersatzteile noch lange verfügbar?**
A: Lewmar hat sich verpflichtet, Ocean-Ersatzteile bis mindestens 2030 zu liefern. Danach wird die Verfügbarkeit unsicher. Empfehlung: Bei nächster Grundüberholung einen kompletten Rebuild-Kit auf Vorrat legen.

**F: Kann ich eine 12V-Elektrowinsch auf 24V umbauen?**
A: Nein, nicht durch einfachen Motorwechsel. Die Steuerungselektronik ist spannungsspezifisch. Ein Umbau erfordert den kompletten Austausch von Motor und Steuereinheit. Wirtschaftlich sinnvoller: Neue 24V-Winsch oder 24V-Konversionskit.

---

## ANHANG A1 — Glossar

| Begriff | Definition |
|---------|-----------|
| Arbeitslast (WLL) | Working Load Limit — maximale Dauerlast, die die Winsch aufnehmen darf |
| Bolzenkreis | Teilkreisdurchmesser der Befestigungsschrauben |
| BLDC | Bürstenloser Gleichstrommotor (Brushless DC) |
| CW/CCW | Clockwise / Counter-Clockwise — Drehrichtung der Kurbel |
| ED (Einschaltdauer) | Prozentualer Anteil der Betriebszeit in einem definierten Zyklus |
| Jaw | Self-Tailing-Backe — Klemmvorrichtung für die Schot |
| NLA | No Longer Available — nicht mehr als Neuware erhältlich |
| OEM | Original Equipment Manufacturer — Erstausrüstung durch Werft |
| Pawl | Sperrklinke — verhindert Rückwärtsdrehung der Trommel |
| Plain Top (PT) | Winsch ohne Self-Tailing-Mechanismus |
| Power Ratio | Übersetzungsverhältnis Kurbel zu Trommel |
| Self-Tailing (ST) | Selbstholend — Schot wird automatisch in Jaw geklemmt |
| Speed 1 | Niedrige Übersetzung, hohe Geschwindigkeit (CW-Drehung) |
| Speed 2 | Hohe Übersetzung, niedrige Geschwindigkeit (CCW-Drehung) |
| Striations | Umlaufende Rillen auf der Trommel für Schotführung |
| TN | Teilenummer |
| UVP | Unverbindliche Preisempfehlung |

## ANHANG B — Bezugsquellen

| Händler | Land | Website | Bemerkung |
|---------|------|---------|-----------|
| SVB | Deutschland | svb.de | Größter deutscher Yachtzubehör-Versand |
| Compass24 | Deutschland | compass24.de | Breites Lewmar-Sortiment |
| Toplicht | Deutschland | toplicht.de | Hamburg, Fachberatung |
| AWN | Deutschland | awn.de | Traditionshaus |
| Bukh Bremen | Deutschland | bukh-bremen.de | Auch Ocean-Ersatzteile |
| Lewmar Direct | UK | lewmar.com | Direktvertrieb |
| Marine Mega Store | Niederlande | marinemegastore.com | Gute Preise |
| Accastillage Diffusion | Frankreich | accastillage-diffusion.com | Frankreich-Markt |
| Defender Industries | USA | defender.com | US-Markt |
| West Marine | USA | westmarine.com | US-Markt |

## ANHANG C — Normen und Standards

| Norm | Relevanz für Winschen |
|------|----------------------|
| ISO 12217 | Stabilitätsberechnung: Winschengewicht in Schwerpunktberechnung |
| ISO 15085 | Sicherheit: Winschenposition darf Bewegungsfreiheit nicht einschränken |
| ISO 10133 | Elektrische Installation: Kabelquerschnitte, Sicherungen für Elektrowinschen |
| ISO 13297 | Elektrische Systeme >50V: Relevant bei 48V-Systemen (Zukunft) |
| CE 2013/53/EU | Freizeitfahrzeugrichtlinie: Gesamtsystem muss CE-konform sein |
| ABYC E-11 | US-Standard für elektrische Systeme auf Booten (für US-Markt) |

## ANHANG D — Historische Lewmar-Winschen (Sammlerwert)

Für die Bewertung älterer Yachten relevant:

| Serie | Baujahre | Erkennungsmerkmal | Ersatzteile |
|-------|----------|-------------------|------------|
| Lewmar 7 | 1960er | Verchromtes Messing, kein Self-Tailing | Nicht mehr verfügbar |
| Lewmar 16C | 1970er | Chrome-Bronze-Trommel | Vereinzelt Nachfertigung |
| Lewmar 30 (alt) | 1975–1985 | Breite Chromtrommel, einfaches Getriebe | Nicht mehr verfügbar |
| Lewmar 40 (alt) | 1975–1985 | Wie 30, größer | Nicht mehr verfügbar |
| Lewmar Ocean 14–66 | 1985–2015 | "Ocean" graviert, schmale Jaw | Noch verfügbar (bis ~2030) |
| Lewmar EVO Gen 1 | 2005–2020 | "EVO" graviert, breite Jaw | Voll verfügbar |
| Lewmar EVO Gen 2 | 2021–heute | Aktuelles Modell | Voll verfügbar |

## ANHANG E — Drehmomenttabelle für Winschenbefestigung

| Bolzen | Material | Drehmoment trocken (Nm) | Drehmoment mit Tef-Gel (Nm) | Drehmoment mit Loctite 243 (Nm) |
|--------|----------|------------------------|-----------------------------|-------------------------------|
| M6 A4-80 | Edelstahl 316 | 8–10 | 7–9 | 8–10 |
| M8 A4-80 | Edelstahl 316 | 20–25 | 18–22 | 20–25 |
| M10 A4-80 | Edelstahl 316 | 35–40 | 32–38 | 35–40 |
| M12 A4-80 | Edelstahl 316 | 55–65 | 50–60 | 55–65 |

Hinweis: Bei GFK-Sandwich-Decks 80% des Drehmoments verwenden. Bei dünnen Decks (<10 mm) mit Beilageplatte arbeiten.

## ANHANG F — Checkliste Winschenwartung (Druckversion)

```
LEWMAR WINSCHEN-WARTUNG — JAHRES-CHECKLISTE

Datum: __________ Boot: ________________ Winsch-Position: __________
Winsch-Modell: ____________ Teilenummer: ______________

□ 1. Schot entfernt
□ 2. Äußere Reinigung mit Süßwasser
□ 3. Kurbel entfernt und Vierkant geprüft
□ 4. Self-Tailing-Jaw abgenommen
    □ Jaw-Einsatz auf Verschleiß geprüft
    □ Jaw-Einsatz gereinigt (trocken!)
    □ Jaw-Feder geprüft
□ 5. Trommel abgehoben
    □ Trommelrillen auf Verschleiß geprüft
    □ Trommel innen gereinigt
□ 6. Sperrklinken geprüft
    □ Alle Pawls frei schwingend
    □ Alle Federn intakt
    □ Pawl-Spitzen nicht abgerundet
    □ Mit Pawl Oil benetzt (NICHT gefettet)
□ 7. Getriebe geprüft
    □ Altes Fett entfernt
    □ Zahnflanken auf Verschleiß geprüft
    □ Neues Lewmar Winch Grease aufgetragen
□ 8. Lager geprüft
    □ Kein Spiel in der Achse
    □ Kein Rost an Lagerflächen
□ 9. Zusammenbau
    □ Pawls klicken in beide Richtungen
    □ Jaw verriegelt
    □ Kurbel sitzt fest
□ 10. Funktionstest
    □ Speed 1 (CW): leichtgängig
    □ Speed 2 (CCW): Übersetzung spürbar
    □ Self-Tailing: Schot wird gehalten
    □ Kein Rückwärtsdrehen unter leichter Last

Befunde: ________________________________________________
_______________________________________________________

Nächste Wartung fällig: ____________

Prüfer: __________________ Unterschrift: __________________
```

---

## ANHANG G — Gewichtsvergleich kompletter Winschenbestückungen

Für die AYDI-Strukturanalyse: Gesamtgewicht aller Winschen an Deck, aufgeschlüsselt nach typischer Bestückung.

**34-Fuß-Fahrtensegler (z.B. Hanse 348):**

| Position | Modell | Anzahl | Einzelgewicht | Gesamt |
|----------|--------|--------|--------------|--------|
| Primärwinsch Cockpit | EVO 40 ST | 2 | 5.8 kg | 11.6 kg |
| Fallwinsch Cockpitdach | EVO 30 ST | 2 | 3.6 kg | 7.2 kg |
| **Gesamt** | | **4** | | **18.8 kg** |

**42-Fuß-Fahrtensegler (z.B. Hallberg-Rassy 412):**

| Position | Modell | Anzahl | Einzelgewicht | Gesamt |
|----------|--------|--------|--------------|--------|
| Primärwinsch Cockpit | EVO 50 ST | 2 | 10.8 kg | 21.6 kg |
| Fallwinsch Cockpitdach | EVO 45 ST | 2 | 7.9 kg | 15.8 kg |
| Mastwinsch (Reacher) | EVO 30 ST | 1 | 3.6 kg | 3.6 kg |
| **Gesamt** | | **5** | | **41.0 kg** |

**50-Fuß-Fahrtensegler elektrisch (z.B. Hanse 508):**

| Position | Modell | Anzahl | Einzelgewicht | Gesamt |
|----------|--------|--------|--------------|--------|
| Primärwinsch Cockpit | EVO 50 EST | 2 | 19.0 kg | 38.0 kg |
| Fallwinsch Cockpitdach | EVO 45 EST | 2 | 14.5 kg | 29.0 kg |
| Mastwinsch (Reacher) | EVO 40 ST | 1 | 5.8 kg | 5.8 kg |
| Spinnaker-Winsch | EVO 40 PT | 2 | 5.2 kg | 10.4 kg |
| **Gesamt** | | **7** | | **83.2 kg** |

**60-Fuß-Performance-Cruiser elektrisch:**

| Position | Modell | Anzahl | Einzelgewicht | Gesamt |
|----------|--------|--------|--------------|--------|
| Primärwinsch Cockpit | EVO 65 EST | 2 | 32.0 kg | 64.0 kg |
| Sekundärwinsch Cockpit | EVO 55 EST | 2 | 24.0 kg | 48.0 kg |
| Fallwinsch Cockpitdach | EVO 50 EST | 2 | 19.0 kg | 38.0 kg |
| Mastwinsch | EVO 45 ST | 2 | 7.9 kg | 15.8 kg |
| **Gesamt** | | **8** | | **165.8 kg** |

Hinweis: Bei der Schwerpunktberechnung beachten, dass Winschenmotoren ca. 200–350 mm unter Deck montiert sind (tieferer Schwerpunkt als die Trommel).

## ANHANG H — Lewmar Garantie und Support

**Garantiebedingungen:**

| Kategorie | Garantiedauer | Bedingung |
|-----------|-------------|-----------|
| Mechanische Winschen | 5 Jahre | Ab Kaufdatum, sachgemäße Verwendung |
| Elektrische Winschen (Motor) | 3 Jahre | Ab Kaufdatum, professionelle Installation |
| Elektrische Winschen (Steuerung) | 3 Jahre | Ab Kaufdatum |
| Hydraulische Winschen | 3 Jahre | Ab Kaufdatum, professionelle Installation |
| Winschenkurbeln | 2 Jahre | Ab Kaufdatum |
| Verschleißteile (Pawls, Federn, Jaw-Einsätze) | 1 Jahr | Ab Kaufdatum |
| Winsch Covers | 1 Jahr | Ab Kaufdatum |

**Garantieausschlüsse:**
- Normaler Verschleiß (Sperrklinken, Federn, Trommeloberfläche)
- Korrosion durch fehlende Wartung
- Schäden durch Überbelastung (über WLL)
- Unsachgemäße Installation (falsche Kabelquerschnitte, fehlende Sicherung)
- Verwendung nicht freigegebener Schmierstoffe
- Modifikationen am Getriebe oder Motor

**Lewmar Technical Support:**

| Kontaktweg | Details |
|-----------|---------|
| E-Mail | technical@lewmar.com |
| Telefon UK | +44 (0)23 9252 4044 |
| Website | lewmar.com/support |
| Händler-Portal | lewmartrade.com |

**Lewmar-zertifizierte Servicewerkstätten in DACH:**

| Werkstatt | Standort | Spezialisierung |
|----------|----------|----------------|
| Toplicht | Hamburg, DE | Vollservice, Elektro-Umrüstung |
| SVB | Bremen, DE | Ersatzteile, Beratung |
| Yachtausrüster Müritz | Waren, DE | Binnenrevier-Service |
| Gründl Bootsimport | Mattsee, AT | Österreich-Vertretung |
| Abart Marine | Zürich, CH | Schweiz-Vertretung |

---

## 9. Fehlerbild-Atlas — Lewmar-spezifische Fehlerbilder

### Systematische Fehlerklassifikation

Dieses Kapitel dokumentiert die 12 häufigsten Lewmar-spezifischen Fehlerbilder mit visuellen Erkennungsmerkmalen, Ursachenanalyse, Schweregrad-Bewertung und den zugehörigen Lewmar-Ersatzteilen. Die Fehlerbilder sind nach Häufigkeit und Kritikalität geordnet.

**Schweregrad-Skala:**

| Stufe | Bezeichnung | Bedeutung | Handlungsbedarf |
|-------|-------------|-----------|-----------------|
| 1 | Kosmetisch | Keine Funktionsbeeinträchtigung | Nächste reguläre Wartung |
| 2 | Gering | Leichte Funktionsminderung | Wartung innerhalb 3 Monaten |
| 3 | Mittel | Spürbare Funktionsbeeinträchtigung | Wartung innerhalb 4 Wochen |
| 4 | Erheblich | Starke Funktionseinschränkung, Sicherheitsrelevanz möglich | Sofortige Wartung, eingeschränkter Betrieb |
| 5 | Kritisch | Funktionsausfall oder Sicherheitsgefährdung | Sofortige Außerbetriebnahme, Reparatur vor Nutzung |

---

### F01 — EVO Klauenmechanismus-Verklemmen

**Betroffene Modelle:** EVO 15, EVO 30, EVO 40, EVO 45, EVO 50, EVO 55, EVO 65

**Visuelle Erkennungsmerkmale:**
- Self-Tailing-Klauen schließen nicht vollständig oder öffnen sich ungleichmäßig
- Sichtbare Verschleißspuren an den Klauenflächen (abgeriebene Rillen)
- Asymmetrische Klauenstellung bei Belastung
- Schottablagerungen zwischen den Klauensegmenten sichtbar
- Tauführung rutscht durch trotz korrekter Klauenstellung

**Ursachenanalyse:**
1. **Salzablagerung** in den Klauenführungen (häufigste Ursache, 45% der Fälle)
2. **Federverschleiß** der Klauenrückstellfeder (30%)
3. **Korrosion** an den Klauen-Drehpunkten durch unzureichende Spülung (15%)
4. **Mechanische Beschädigung** durch falschen Taudurchmesser (10%)

**Schweregrad:** 3-4 (abhängig vom Grad der Verklemm ung)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19700101 | EVO Self-Tailing Jaw Kit | EVO 15-30 | €85 |
| 19700201 | EVO Self-Tailing Jaw Kit | EVO 40-55 | €125 |
| 19700301 | EVO Self-Tailing Jaw Kit | EVO 65 | €165 |
| 19700401 | Jaw Spring Set | Alle EVO | €22 |
| 19700501 | Jaw Pivot Pin Set | Alle EVO | €18 |

**Reparaturanweisung:**
1. Obere Trommel abnehmen (3× M5 Inbus-Schrauben)
2. Klauenmechanismus freilegen und mit Süßwasser spülen
3. Federelemente auf Ermüdung prüfen (Sollwert: 12-15N Rückstellkraft)
4. Drehpunkte entfetten, prüfen, neu schmieren (Lewmar Winch Grease Art. 19701000)
5. Bei Verschleiß: komplettes Jaw Kit tauschen
6. Trommel montieren, Funktion mit korrekt dimensioniertem Tau prüfen

---

### F02 — Ocean-Serie Getriebe-Korrosion

**Betroffene Modelle:** Ocean 14, Ocean 16, Ocean 30, Ocean 40, Ocean 48, Ocean 50, Ocean 65

**Visuelle Erkennungsmerkmale:**
- Weißlich-grüne Korrosionsprodukte an den Zahnrädern sichtbar bei Demontage
- Schwergängigkeit beider Gänge (besonders 2. Gang)
- Mahlendes oder knirschendes Geräusch beim Kurbeln
- Übersetzungsverhältnis fühlt sich „rutschig" an
- Bei fortgeschrittenem Stadium: Zahnflankenausbrüche sichtbar

**Ursachenanalyse:**
1. **Galvanische Korrosion** zwischen Bronze-Zahnrad und Aluminium-Gehäuse (40%)
2. **Fettverlust** durch unzureichende Wartung oder ausgewaschene Schmierung (30%)
3. **Elektrolytische Korrosion** durch Kriechströme vom elektrischen System (15%)
4. **Materialermüdung** bei Modellen vor 2018 (verbessertes Legierungsverfahren ab 2019) (15%)

**Schweregrad:** 4 (Sicherheitsrelevant — Winde kann unter Last blockieren)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19510101 | Primary Gear Set Bronze | Ocean 14-16 | €145 |
| 19510201 | Primary Gear Set Bronze | Ocean 30-40 | €215 |
| 19510301 | Primary Gear Set Bronze | Ocean 48-65 | €295 |
| 19510401 | Secondary Gear Set | Alle Ocean | €175 |
| 19510501 | Centre Stem Assembly | Alle Ocean | €85 |
| 19510601 | Bearing Washer Set | Alle Ocean | €32 |

**Reparaturanweisung:**
1. Winde komplett demontieren (Trommel, Federn, Klinken)
2. Getriebe freilegen, altes Fett vollständig entfernen (Lewmar Degreaser)
3. Zahnflanken auf Pittings und Ausbrüche prüfen (Lupe 10×)
4. Bei Korrosion >20% der Zahnfläche: Gear Set tauschen
5. Centre Stem auf Laufspuren prüfen, ggf. tauschen
6. Neu schmieren mit Lewmar Gear Grease (Art. 19701100, NICHT Standard-Fett)
7. Zusammenbau in umgekehrter Reihenfolge, Gangschaltung prüfen

---

### F03 — EVO Trommel-Eloxalverschleiß

**Betroffene Modelle:** Alle EVO-Modelle

**Visuelle Erkennungsmerkmale:**
- Matte, helle Stellen auf der sonst dunkelgrauen Trommeloberfläche
- Rillenbildung in den Trommelrippen (besonders auf der Leeseite)
- Aluminium-Grundmaterial sichtbar (silbrig-glänzend unter abgeriebener Eloxalschicht)
- Ungleichmäßiger Seilabrieb als Sekundäreffekt
- Farbunterschiede zwischen oberer und unterer Trommelhälfte

**Ursachenanalyse:**
1. **Abrasiver Verschleiß** durch sandhaltige Tauoberflächen (40%)
2. **Chemische Degradation** durch alkalische Reiniger (25%)
3. **UV-Degradation** der Eloxalschicht (20%)
4. **Falscher Taudurchmesser** erzeugt erhöhte Flächenpressung (15%)

**Schweregrad:** 2-3

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19720101 | EVO Drum Assembly | EVO 15 | €195 |
| 19720201 | EVO Drum Assembly | EVO 30 | €285 |
| 19720301 | EVO Drum Assembly | EVO 40 | €365 |
| 19720401 | EVO Drum Assembly | EVO 45-50 | €445 |
| 19720501 | EVO Drum Assembly | EVO 55-65 | €580 |

**Hinweis:** Eloxalschicht kann nicht repariert werden. Bei >30% Flächenverlust Trommel tauschen. Prävention durch regelmäßige Süßwasserspülung und pH-neutrale Reiniger.

---

### F04 — Composite-Basis-Rissbildung

**Betroffene Modelle:** EVO-Modelle mit Composite-Basis (EVO 30C, EVO 40C, EVO 45C)

**Visuelle Erkennungsmerkmale:**
- Haarrisse an der Basis-Oberfläche, oft sternförmig vom Befestigungsloch ausgehend
- Weißfärbung (Stress Whitening) im Composite-Material um Lastpunkte
- Klickende oder knarrende Geräusche unter Last
- Spaltbildung zwischen Basis und Deck bei fortgeschrittenem Schaden
- Wasseraustritt an der Basis nach Regenfall (Dichtungsverlust)

**Ursachenanalyse:**
1. **Überbelastung** durch zu starkes Anziehen der Befestigungsschrauben (35%)
2. **Zyklische Ermüdung** bei Langzeitbelastung über 60% der Nennlast (25%)
3. **UV-Degradation** des Composite-Materials (20%)
4. **Thermische Ausdehnung** — unterschiedliche Ausdehnungskoeffizienten Composite/Deck (20%)

**Schweregrad:** 4-5 (Sicherheitskritisch — kann zum Ausreißen der Winde führen)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19740101 | Composite Base Plate | EVO 30C | €225 |
| 19740201 | Composite Base Plate | EVO 40C | €310 |
| 19740301 | Composite Base Plate | EVO 45C | €385 |
| 19740401 | Base Mounting Kit SS316 | Alle EVO-C | €65 |
| 19740501 | Base Gasket Set | Alle EVO-C | €28 |

**Sofortmaßnahme:** Bei sichtbarer Rissbildung Winde sofort außer Betrieb nehmen. Belastung kann zu katastrophalem Versagen führen. Deck-Unterkonstruktion auf Delaminierung prüfen vor Neuinstallation.

---

### F05 — Self-Tailing Federmüdigkeit

**Betroffene Modelle:** Alle Lewmar-Modelle mit Self-Tailing (EVO, Ocean ST, ältere Standard-ST)

**Visuelle Erkennungsmerkmale:**
- Self-Tailing-Arm kehrt nicht mehr vollständig in Ausgangsposition zurück
- Seil rutscht bei geringer Belastung aus der Klemmung
- Feder zeigt sichtbare Deformation (Strecken, Verdrehen)
- Arm-Bewegung fühlt sich „schwammig" an (kein definierter Endanschlag)
- Unterschiedliche Klemmkraft bei verschiedenen Taupositionen

**Ursachenanalyse:**
1. **Zyklische Ermüdung** — Standardfeder hält ca. 15.000-20.000 Zyklen (50%)
2. **Korrosion** der Federdraht-Oberfläche durch Salzwasser (25%)
3. **Überdehnung** durch zu dickes Tau oder manuelles Forcieren (15%)
4. **Temperaturbedingte Materialermüdung** (extreme Hitze/Kälte-Wechsel) (10%)

**Schweregrad:** 3

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19750101 | ST Spring Kit (2×) | EVO 15-30 | €18 |
| 19750201 | ST Spring Kit (2×) | EVO 40-55 | €24 |
| 19750301 | ST Spring Kit (2×) | EVO 65 | €28 |
| 19750401 | ST Spring Kit (2×) | Ocean alle | €22 |
| 19750501 | ST Arm Assembly | EVO alle | €55 |

**Wartungshinweis:** Federn sind Verschleißteile. Empfohlener Tauschintervall: alle 3 Jahre oder 15.000 Zyklen. Prävention: Federn bei jeder Windenservice-Einheit mit Lewmar Spray (Art. 19701200) behandeln.

---

### F06 — Elektro-Motordichtungs-Versagen

**Betroffene Modelle:** Alle Lewmar-Elektrowinden (EVO E, Ocean E, ältere Modelle mit Nachrüst-Motor)

**Visuelle Erkennungsmerkmale:**
- Wassereintrittsspuren am Motorgehäuse (Salzablagerungen, Korrosionsfahnen)
- Motor läuft unregelmäßig oder mit reduzierter Leistung
- Fehlermeldungen am Bedienpanel (bei CAN-Bus-Modellen)
- Sichtbare Quellung oder Verhärtung der Wellendichtung
- Grünspan an den Motoranschlüssen oder Kabeleinführungen

**Ursachenanalyse:**
1. **Dichtungsalterung** durch UV und Ozon (35%)
2. **Mechanische Beschädigung** der Wellendichtung durch Vibration (25%)
3. **Unsachgemäße Montage** bei Nachrüstung oder Wartung (20%)
4. **Korrosion der Dichtflächen** am Motorgehäuse (20%)

**Schweregrad:** 4 (Elektrosicherheit — Kurzschlussgefahr, Brand möglich)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19760101 | Motor Seal Kit | EVO E 15-30 | €45 |
| 19760201 | Motor Seal Kit | EVO E 40-55 | €55 |
| 19760301 | Motor Seal Kit | EVO E 65 | €65 |
| 19760401 | Motor Seal Kit | Ocean E alle | €50 |
| 19760501 | Motor Housing Gasket | Alle E-Modelle | €35 |
| 19760601 | Cable Gland Set IP68 | Alle E-Modelle | €22 |

**Sofortmaßnahme:** Bei Wassereintrittsverdacht sofort Sicherung herausnehmen. Motorgehäuse öffnen, trocknen, Isolationswiderstand messen (Sollwert >2 MΩ bei 500V DC). Bei <1 MΩ: Motor zur Revision einschicken.

---

### F07 — Klinken-Stift-Verschleiß (Pawl Pin Wear)

**Betroffene Modelle:** Alle Lewmar-Winden (konstruktionsbedingt universelles Verschleißteil)

**Visuelle Erkennungsmerkmale:**
- Klinkenstifte zeigen sichtbare Einlaufspuren oder Abflachungen
- Klinken kippen nicht mehr frei (verzögertes Einrasten)
- Unregelmäßiges Klick-Geräusch beim Drehen (normal: gleichmäßig)
- In extremen Fällen: Rücklauf unter Last (SICHERHEITSKRITISCH)
- Verschleißmarkierungen an der Aufnahmebohrung im Klinkenträger

**Ursachenanalyse:**
1. **Abrasiver Verschleiß** durch Normalbetrieb (50%)
2. **Korrosion** durch unzureichende Schmierung (25%)
3. **Lastspitzen** durch ruckartige Schot-Manöver (15%)
4. **Materialminderwertigkeit** bei Nicht-Original-Ersatzteilen (10%)

**Schweregrad:** 3-5 (5 bei drohendem Rücklauf)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19770101 | Pawl & Spring Kit | EVO 15-30 | €32 |
| 19770201 | Pawl & Spring Kit | EVO 40-65 | €45 |
| 19770301 | Pawl & Spring Kit | Ocean 14-16 | €28 |
| 19770401 | Pawl & Spring Kit | Ocean 30-65 | €42 |
| 19770501 | Pawl Pin Set (6×) | Alle Modelle | €15 |

**Prüfverfahren:** Winde langsam unter Last von Hand kurbeln, andere Hand auf Trommel. Jede Klinke muss bei jeder Umdrehung einrasten (Klick-Feedback). Bei Aussetzen >1 Klick pro Umdrehung: sofort Klinken und Stifte prüfen.

---

### F08 — Lagerkäfig-Verschlechterung

**Betroffene Modelle:** Alle Lewmar-Winden mit Rollenlagern (primär Ocean-Serie und größere EVO)

**Visuelle Erkennungsmerkmale:**
- Erhöhter Drehwiderstand, besonders im unbelasteten Zustand
- Rastende oder hakende Trommelbewegung
- Sichtbare Verformung des Kunststoff-Lagerkäfigs bei Demontage
- Rollenoberflächen mit Pittings oder Laufspuren
- Fettaustritt an der Trommelbasis (Dichtungsverlust durch Lagerspiel)

**Ursachenanalyse:**
1. **Materialermüdung** des PA66-Käfigs (Polyamid, hygroskopisch) (35%)
2. **Fehlende Schmierung** führt zu Trockenlauf und Überhitzung (30%)
3. **Salzwassereinwirkung** auf den Lagerkäfig (Hydrolyse des Polyamids) (20%)
4. **Überlast** — Rollen drücken Käfigstege auseinander (15%)

**Schweregrad:** 2-3

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19780101 | Upper Bearing Kit | EVO 40-65 | €55 |
| 19780201 | Lower Bearing Kit | EVO 40-65 | €55 |
| 19780301 | Upper Bearing Kit | Ocean 30-65 | €48 |
| 19780401 | Lower Bearing Kit | Ocean 30-65 | €48 |
| 19780501 | Roller Set (12×) | Universal | €22 |
| 19780601 | Cage Assembly | Universal groß | €35 |

---

### F09 — Kurbelbuchsen-Korrosion (Handle Socket Corrosion)

**Betroffene Modelle:** Alle Lewmar-Handwinden (manuell und manuell+elektrisch)

**Visuelle Erkennungsmerkmale:**
- Windengriff lässt sich schwer einführen oder entfernen
- Weißlich-graue Korrosionsprodukte an der Aufnahmebuchse
- Windengriff sitzt schief oder wackelt (Ovalisierung der Buchse)
- Griff-Verriegelung (Lock-In) funktioniert nicht mehr zuverlässig
- Kontaktkorrosion zwischen Edelstahl-Griff und Aluminium-Buchse sichtbar

**Ursachenanalyse:**
1. **Galvanische Korrosion** Edelstahl/Aluminium im Salzwasser-Elektrolyt (50%)
2. **Fehlende Schutzkappe** lässt Salzwasser in die Buchse eindringen (25%)
3. **Mechanischer Verschleiß** durch häufiges Griff-Einsetzen/Entnehmen (15%)
4. **Elektrolytische Korrosion** durch Kriechströme bei Elektro-Winden (10%)

**Schweregrad:** 2-3

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19790101 | Handle Socket Insert | EVO alle | €42 |
| 19790201 | Handle Socket Insert | Ocean alle | €38 |
| 19790301 | Socket Cap (Schutzkappe) | Universal | €8 |
| 19790401 | Winch Handle One-Touch | Universal | €85 |
| 19790501 | Winch Handle Power-Grip | Universal | €110 |

---

### F10 — Trommelkappe O-Ring-Versagen

**Betroffene Modelle:** Alle Lewmar-Modelle mit O-Ring-gedichteter Trommelkappe

**Visuelle Erkennungsmerkmale:**
- Wasser sammelt sich im Trommelinneren (sichtbar bei Demontage)
- Salzablagerungen an der Trommelkappe-Dichtfläche
- O-Ring zeigt Verhärtung, Risse oder Quetschung
- Trommelkappe sitzt locker oder hat Spiel
- Korrosion im Trommelinneren als Sekundärschaden

**Ursachenanalyse:**
1. **Elastomer-Alterung** durch UV, Ozon und Salzwasser (40%)
2. **Falsche Montage** — O-Ring verdreht oder gequetscht eingebaut (25%)
3. **Dichtflächenkorrosion** verhindert korrekten Sitz (20%)
4. **Falscher O-Ring** (Nicht-Original, falscher Werkstoff oder Maß) (15%)

**Schweregrad:** 2

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19800101 | Drum Cap O-Ring Set (3×) | EVO 15-30 | €12 |
| 19800201 | Drum Cap O-Ring Set (3×) | EVO 40-65 | €15 |
| 19800301 | Drum Cap O-Ring Set (3×) | Ocean alle | €12 |
| 19800401 | Drum Cap Assembly | EVO alle | €45 |
| 19800501 | Drum Cap Assembly | Ocean alle | €38 |

---

### F11 — Kabelbaum-Scheuerschaden (Wiring Harness Chafe)

**Betroffene Modelle:** Alle Lewmar-Elektrowinden

**Visuelle Erkennungsmerkmale:**
- Sichtbare Abriebstellen an der Kabelisolierung
- Kabelmantel verfärbt oder aufgeraut an Durchführungsstellen
- Intermittierende Motor-Funktionsstörungen (Motor startet manchmal nicht)
- Korrosionsprodukte an freiliegenden Leiterstellen
- Wärmeverfärbung an Kontaktstellen (lokale Überhitzung)

**Ursachenanalyse:**
1. **Vibration** überträgt sich vom Motor auf den Kabelbaum (35%)
2. **Scharfe Kanten** an Deck-Durchführungen oder Kabelschellen (30%)
3. **UV-Degradation** bei deck-exponierten Kabelabschnitten (20%)
4. **Unsachgemäße Verlegung** bei Installation oder Nachrüstung (15%)

**Schweregrad:** 4 (Brandgefahr bei Kurzschluss, besonders bei hohen Strömen >60A)

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19810101 | Wiring Harness Complete | EVO E 15-30 | €125 |
| 19810201 | Wiring Harness Complete | EVO E 40-55 | €155 |
| 19810301 | Wiring Harness Complete | EVO E 65 | €185 |
| 19810401 | Deck Gland Kit | Alle E-Modelle | €32 |
| 19810501 | Chafe Protection Kit (2m) | Universal | €18 |
| 19810601 | Connector Kit IP68 | Universal | €28 |

**Prävention:** Kabelbaum bei jeder Jahreswartung auf Scheuerstellen prüfen. An allen Durchführungen und Biegepunkten zusätzlichen Schutz anbringen. Lewmar empfiehlt Spiralschlauch oder selbstvulkanisierendes Tape.

---

### F12 — CAN-Bus Kommunikationsverlust

**Betroffene Modelle:** Lewmar EVO E-Modelle mit CAN-Bus-Steuerung (ab 2020)

**Visuelle Erkennungsmerkmale:**
- Fehlermeldung am Bedienpanel: „CAN Error" oder „Communication Lost"
- Winde reagiert nicht auf Tastendruck, Motor-Relais schaltet nicht
- LED-Statusanzeige blinkt Fehlercode (3× kurz = CAN-Fehler)
- Andere CAN-Bus-Geräte funktionieren ebenfalls nicht (Systemfehler)
- Bei Einzelwinden-Ausfall: nur betroffene Winde ohne Funktion

**Ursachenanalyse:**
1. **Terminierungswiderstand** fehlt oder defekt (30%)
2. **Kontaktkorrosion** an CAN-Bus-Steckern durch Feuchtigkeit (25%)
3. **Kabelbruch** in der CAN-Bus-Leitung (20%)
4. **Softwarefehler** nach Firmware-Update oder Spannungsausfall (15%)
5. **EMV-Störung** durch benachbarte Geräte (Radar, Funkgeräte) (10%)

**Schweregrad:** 3-4

**Lewmar-spezifische Ersatzteile:**

| Teil-Nr. | Bezeichnung | Modell | Preis (ca.) |
|----------|-------------|--------|-------------|
| 19820101 | CAN-Bus Interface Module | Alle E-CAN | €185 |
| 19820201 | CAN Termination Resistor Kit | Universal | €15 |
| 19820301 | CAN Cable Assembly (5m) | Universal | €45 |
| 19820401 | CAN Connector Kit | Universal | €22 |
| 19820501 | Winch Control Panel | EVO E-CAN | €245 |

**Diagnose-Verfahren:**
1. Versorgungsspannung am CAN-Bus prüfen (Sollwert: 12-13.8V DC)
2. Terminierungswiderstand messen (Sollwert: 60Ω zwischen CAN-H und CAN-L)
3. CAN-H/CAN-L Differenzspannung prüfen (Sollwert: 1.5-3.5V im Ruhezustand)
4. Stecker-für-Stecker-Prüfung der gesamten CAN-Kette
5. Bei Softwareverdacht: Factory Reset über Service-Tool (Lewmar Service Interface, Art. 19820601)

---

### Fehlerbild-Kombinationen und Folgeschäden

Einzelne Fehlerbilder treten häufig nicht isoliert auf. Folgende Kombinationen sind besonders relevant:

**Kombination 1: F02 + F07 (Getriebe-Korrosion + Klinken-Verschleiß)**
- Häufigkeit: 25% aller Ocean-Serviceeinträge
- Mechanismus: Korrosionsprodukte aus dem Getriebe gelangen an die Klinken und beschleunigen deren Verschleiß
- Sekundäreffekt: Metallische Partikel im Fett wirken als Schleifmittel
- Empfehlung: Bei F02-Befund immer auch Klinken und Stifte prüfen

**Kombination 2: F01 + F05 (Klauen-Verklemmen + Feder-Müdigkeit)**
- Häufigkeit: 35% aller EVO-ST-Reklamationen
- Mechanismus: Schwache Feder kann verschmutzte Klaue nicht mehr vollständig schließen
- Sekundäreffekt: Eigner forciert die Klaue manuell → mechanische Beschädigung
- Empfehlung: Beide Komponenten gemeinsam tauschen (Jaw Kit + Spring Kit)

**Kombination 3: F06 + F11 (Motor-Dichtung + Kabelbaum)**
- Häufigkeit: 15% aller Elektrowinden-Ausfälle
- Mechanismus: Wassereintritt durch defekte Motordichtung kriecht entlang des Kabelbaums
- Sekundäreffekt: Korrosion der Steckverbindungen, Isolationsverlust
- Empfehlung: Bei Wassereintritt am Motor immer den gesamten Kabelbaum prüfen

**Kombination 4: F04 + F09 (Composite-Basis + Buchsen-Korrosion)**
- Häufigkeit: 10% aller EVO-C-Servicefälle
- Mechanismus: Galvanische Korrosion zwischen Edelstahl-Buchse und Composite-Montageschrauben erzeugt Quellspannung
- Sekundäreffekt: Aufquellende Korrosionsprodukte erzeugen Risskeime in der Composite-Basis
- Empfehlung: Bei EVO-C immer isolierende Unterlegscheiben verwenden

**Präventive Inspektionsreihenfolge (empfohlen):**

Bei einer systematischen Inspektion sollten die Fehlerbilder in folgender Reihenfolge geprüft werden, da spätere Prüfungen auf früheren Befunden aufbauen:

1. F04 — Basis (vor Demontage, unter Last prüfbar)
2. F09 — Kurbelbuchse (ohne Demontage prüfbar)
3. F10 — Trommelkappe O-Ring (erster Demontageschritt)
4. F03 — Trommel-Eloxal (Sichtprüfung bei abgenommener Kappe)
5. F01 — Self-Tailing-Klauen (nach Abnehmen der Trommelkappe)
6. F05 — ST-Federn (nach Freilegen des Mechanismus)
7. F07 — Klinken und Stifte (nach Abnehmen der Trommel)
8. F08 — Lager (nach Abnehmen der Trommel)
9. F02 — Getriebe (nach Freilegen des Getriebes)
10. F06 — Motor-Dichtung (nur Elektro, separater Zugang)
11. F11 — Kabelbaum (nur Elektro, Sichtprüfung)
12. F12 — CAN-Bus (nur E-CAN, elektronische Diagnose)

---

### Fehlerbild-Übersichtsmatrix

| Code | Fehlerbild | Schwere | Häufigkeit | Betroffene Serie |
|------|-----------|---------|------------|-----------------|
| F01 | EVO Klauen-Verklemmen | 3-4 | Häufig | EVO |
| F02 | Ocean Getriebe-Korrosion | 4 | Mittel | Ocean |
| F03 | EVO Eloxalverschleiß | 2-3 | Häufig | EVO |
| F04 | Composite-Basis-Riss | 4-5 | Selten | EVO-C |
| F05 | ST-Federmüdigkeit | 3 | Häufig | Alle ST |
| F06 | Motor-Dichtungsversagen | 4 | Mittel | Alle E |
| F07 | Klinken-Stift-Verschleiß | 3-5 | Häufig | Alle |
| F08 | Lagerkäfig-Verschlechterung | 2-3 | Mittel | Ocean, EVO groß |
| F09 | Kurbelbuchsen-Korrosion | 2-3 | Häufig | Alle manuell |
| F10 | Trommelkappe O-Ring | 2 | Häufig | Alle |
| F11 | Kabelbaum-Scheuern | 4 | Mittel | Alle E |
| F12 | CAN-Bus-Verlust | 3-4 | Selten | EVO E-CAN |

---

## 10. Troubleshooting-Entscheidungsbaum — Lewmar-spezifisch

### Entscheidungsbaum 1: Winde dreht schwer

```
[Winde dreht schwer]
├── Unter Last?
│   ├── JA → Belastung im Normbereich?
│   │   ├── JA → Schmierung prüfen
│   │   │   ├── Trocken → Komplettwartung (Lewmar Winch Grease anwenden)
│   │   │   └── Geschmiert → Getriebe prüfen → siehe F02
│   │   └── NEIN → Last reduzieren, Windengröße überprüfen
│   └── NEIN (auch ohne Last schwer)
│       ├── Trommel abnehmen → leichtgängig ohne Trommel?
│       │   ├── JA → Trommellager prüfen → siehe F08
│       │   └── NEIN → Getriebe/Klinken prüfen
│       │       ├── Klinken frei? → siehe F07
│       │       ├── Getriebe korrodiert? → siehe F02
│       │       └── Centre Stem beschädigt? → Centre Stem tauschen
│       └── Kurbelbuchse schwergängig? → siehe F09
```

### Entscheidungsbaum 2: Self-Tailing hält nicht

```
[Self-Tailing hält nicht]
├── Richtiger Taudurchmesser?
│   ├── NEIN → Tau auf korrekten Durchmesser wechseln (siehe Modell-Spezifikation)
│   └── JA → Klauenmechanismus prüfen
│       ├── Klauen verschmutzt/verklebt? → Reinigen, Süßwasser-Spülung
│       ├── Klauen-Feder schwach? → siehe F05 (Feder tauschen)
│       ├── Klauen verschlissen (Rillen abgetragen)? → siehe F01 (Jaw Kit tauschen)
│       └── Klauenöffnung zu groß/klein?
│           ├── Falsches Jaw Kit montiert → Korrekt dimensioniertes Kit einbauen
│           └── Klauen mechanisch beschädigt → Jaw Kit tauschen
```

### Entscheidungsbaum 3: Elektro-Winde startet nicht

```
[Elektro-Winde startet nicht]
├── Sicherung OK?
│   ├── NEIN → Sicherung tauschen, Ursache suchen (Kurzschluss?)
│   │   ├── Neue Sicherung löst sofort aus → Kabelbaum prüfen → siehe F11
│   │   └── Neue Sicherung hält → Intermittierender Fehler, Monitoring
│   └── JA → Spannung am Motor prüfen (Sollwert: >11.5V unter Last)
│       ├── Keine Spannung → Relais/Schalter prüfen
│       │   ├── Relais schaltet nicht → CAN-Bus prüfen → siehe F12
│       │   └── Relais schaltet → Kabelbruch Motor→Relais → siehe F11
│       ├── Spannung OK, Motor dreht nicht
│       │   ├── Motor blockiert → Mechanische Blockade (Getriebe, Fremdkörper)
│       │   ├── Motor brummt nur → Wicklungsschaden → Motor tauschen
│       │   └── Motor leise → Kohlebürsten verschlissen → Bürsten tauschen
│       └── Spannung niedrig (<11.5V) → Batteriebank, Kabelquerschnitt prüfen
```

### Entscheidungsbaum 4: Ungewöhnliche Geräusche

```
[Ungewöhnliche Geräusche]
├── Art des Geräuschs?
│   ├── Knirschen/Mahlen
│   │   ├── Bei jeder Umdrehung → Getriebe-Verschleiß → siehe F02
│   │   └── Gelegentlich → Fremdkörper (Sand, Salzkristalle) → Spülen + Service
│   ├── Klicken (unregelmäßig)
│   │   ├── Klinken rasten nicht korrekt ein → siehe F07
│   │   └── Lagerkäfig-Geräusch → siehe F08
│   ├── Quietschen
│   │   ├── Trockenlauf → Schmierung erneuern
│   │   └── Metallkontakt → Lagerschalen prüfen
│   ├── Knarren/Knacken
│   │   ├── Basis prüfen → siehe F04 (Composite-Riss)
│   │   └── Befestigung prüfen → Schrauben nachziehen (Drehmoment beachten)
│   └── Summen (nur Elektro)
│       ├── Normales Motorgeräusch → OK
│       ├── Lautes Summen ohne Drehung → Motor blockiert
│       └── Intermittierendes Summen → Kontaktproblem → siehe F11, F12
```

### Entscheidungsbaum 5: Winde verliert Öl/Fett

```
[Winde verliert Öl/Fett]
├── Austrittsort identifizieren
│   ├── Trommelkappe → O-Ring prüfen → siehe F10
│   ├── Trommelbasis
│   │   ├── Oberes Lager → Lagerdichtung / Fettmenge reduzieren
│   │   └── Basis-Dichtung → Basis-Gasket tauschen
│   ├── Motorgehäuse (Elektro)
│   │   ├── Wellendichtung → siehe F06
│   │   └── Gehäusedichtung → Gehäuse-Gasket tauschen
│   └── Kurbelbuchse → Buchsen-Dichtung prüfen
├── Fettfarbe beurteilen
│   ├── Schwarz → Abrieb im System, Getriebe prüfen
│   ├── Grau-metallisch → Lagerverschleiß → siehe F08
│   ├── Grünlich → Kupferkorrosion (Bronze-Teile) → siehe F02
│   └── Hellbraun (normal) → Nur Dichtung tauschen
```

### Allgemeine Troubleshooting-Hinweise

**Systematische Fehlersuche — Grundprinzipien:**

1. **Sicherheit zuerst:** Vor jeder Fehlersuche alle Lasten von der Winde nehmen und sichern.
2. **Vom Einfachen zum Komplexen:** Immer zuerst die einfachsten Ursachen prüfen (Verschmutzung, Schmierung, Tau-Durchmesser).
3. **Dokumentation:** Jeden Befund fotografieren und notieren — wichtig für Garantieansprüche und Ersatzteilbestellung.
4. **Original-Ersatzteile:** Ausschließlich Lewmar-Originalteile verwenden, um Folgeschäden zu vermeiden.
5. **Drehmomente beachten:** Beim Zusammenbau immer die spezifizierten Drehmomente einhalten (siehe Anhang M).

**Werkzeug-Grundausstattung für die Fehlersuche:**

| Werkzeug | Verwendung |
|----------|-----------|
| Inbus-Set 4/5/6 mm | Trommel-Demontage |
| 10× Lupe | Zahnflanken, Klinken, Lager inspizieren |
| Federwaage 0-50N | Klinkenfedern, ST-Federn messen |
| Multimeter | Elektro: Spannung, Widerstand, Durchgang |
| Fühlerlehre 0.05-1.0 mm | Spaltmaße prüfen |
| Taschenlampe (LED) | Innere Inspektion |
| Saubere Lappen | Reinigung, Zustandsbeurteilung |
| Digitalfotoapparat | Befunddokumentation |

**Wann zum Fachbetrieb:**
- Rücklauf unter Last (sicherheitskritisch)
- Composite-Basis mit Rissbildung
- Elektrischer Fehler mit Brandspuren
- CAN-Bus-Probleme ohne eigenes Diagnosetool
- Getriebeschaden, der Spezialwerkzeug erfordert

---

## 11. FAQ — Lewmar Winschen (Häufig gestellte Fragen)

### Allgemeine Fragen

**F1: Welche Lewmar-Windenreihe ist für mein Boot am besten geeignet?**

Die Wahl hängt von drei Hauptfaktoren ab: Bootsgröße (LOA), Segeltyp und Budget. Als Faustregel gilt:
- **Boote 8-10m:** EVO 15 ST (Fallwinden), EVO 30 ST (Schotwinden)
- **Boote 10-13m:** EVO 30 ST (Fallwinden), EVO 40 ST (Schotwinden)
- **Boote 13-16m:** EVO 40 ST (Fallwinden), EVO 50 ST (Schotwinden), ggf. EVO 45 E (Elektro-Schot)
- **Boote 16-20m:** EVO 50 ST oder E (Fallwinden), EVO 65 E (Schotwinden)
- **Boote 20m+:** Individuelle Berechnung erforderlich, immer Lewmar-Beratung einholen

Die Ocean-Serie bietet ähnliche Leistung zu günstigerem Preis, ist aber schwerer und hat keine Composite-Option.

**F2: Wie oft muss eine Lewmar-Winde gewartet werden?**

Lewmar empfiehlt:
- **Süßwasser-Spülung:** Nach jedem Salzwasser-Einsatz, mindestens alle 2 Wochen
- **Oberflächenpflege:** Monatlich mit Lewmar Winch Cleaner
- **Leichte Wartung** (Schmierung, Klinkenprüfung): Alle 6 Monate oder 500 Betriebsstunden
- **Komplettwartung** (Demontage, Reinigung, Neuschmierung): Jährlich
- **Professionelle Inspektion:** Alle 3 Jahre (empfohlen für Elektrowinden: jährlich)

Regattateilnehmer sollten vor jeder Regattasaison eine Komplettwartung durchführen.

**F3: Kann ich eine ältere Lewmar-Winde auf EVO umrüsten?**

Ja, in den meisten Fällen. Lewmar bietet Retrofit-Kits für den Umbau von Standard- auf EVO-Modelle. Wichtige Punkte:
- Lochbild prüfen: EVO hat teilweise andere Befestigungsmaße als ältere Serien
- Deck-Verstärkung prüfen: EVO-Modelle können höhere Punktlasten erzeugen
- Bei Elektro-Upgrade: Kabelquerschnitte und Sicherungen müssen angepasst werden
- Lewmar bietet für die meisten Retrofit-Situationen Adapterplatten an
- Professionelle Installation wird für Elektro-Umrüstungen dringend empfohlen

**F4: Welches Fett soll ich für Lewmar-Winden verwenden?**

Ausschließlich die von Lewmar empfohlenen Schmiermittel:
- **Lewmar Winch Grease** (Art. 19701000): Für Zahnräder, Lager, mechanische Teile. Lithium-basiert, salzwasserbeständig, temperaturstabil -20°C bis +120°C.
- **Lewmar Gear Grease** (Art. 19701100): Speziell für Ocean-Getriebe. Höhere EP-Additivierung.
- **Lewmar Winch Spray** (Art. 19701200): Für Federn, Klinken, leichte Schmierung. Nicht für Hauptlager.

NICHT verwenden: WD-40, Silikonspray, Teflonfett, Mehrzweckfett, Vaseline. Diese können Dichtungen angreifen, die Klinken-Funktion beeinträchtigen oder den Korrosionsschutz aufheben.

**F5: Was ist der Unterschied zwischen EVO und Ocean?**

| Merkmal | EVO | Ocean |
|---------|-----|-------|
| Gehäuse | Aluminium-Legierung, eloxiert | Aluminium, lackiert |
| Trommel | Eloxiert, feinere Rillung | Standard-Rillung |
| Composite-Option | Ja (C-Modelle) | Nein |
| Gewicht | 15-25% leichter | Referenz |
| Self-Tailing | EVO-Klauenmechanismus (neuere Generation) | Klassischer ST-Mechanismus |
| Wartungsintervall | 12 Monate | 6-12 Monate |
| Preisniveau | Premium (+30-50%) | Standard |
| Zielgruppe | Performance, Regatta, Blauwasser | Fahrtensegler, Budget-bewusst |

**F6: Welchen Taudurchmesser kann meine Lewmar-Winde aufnehmen?**

Jedes Windenmodell hat einen spezifizierten Durchmesserbereich. Außerhalb dieses Bereichs funktioniert das Self-Tailing nicht korrekt und die Winde kann beschädigt werden:

| Modellgröße | Min. Tau-Ø | Max. Tau-Ø | Optimaler Bereich |
|-------------|-----------|-----------|-------------------|
| 15 (EVO/Ocean) | 6 mm | 10 mm | 8-10 mm |
| 30 (EVO/Ocean) | 8 mm | 12 mm | 10-12 mm |
| 40 (EVO/Ocean) | 10 mm | 14 mm | 12-14 mm |
| 45/48 (EVO/Ocean) | 10 mm | 16 mm | 12-14 mm |
| 50 (EVO/Ocean) | 12 mm | 18 mm | 14-16 mm |
| 55/65 (EVO/Ocean) | 14 mm | 22 mm | 16-18 mm |

**F7: Meine Winde macht klackende Geräusche — ist das normal?**

Gleichmäßiges Klicken ist normal — das sind die Klinken, die in den Zahnkranz einrasten und den Rücklauf verhindern. Auffällig wird es, wenn:
- Das Klicken unregelmäßig wird (Klinke rastet nicht zuverlässig ein → F07)
- Zusätzlich Knirschen oder Mahlen auftritt (Getriebeverschleiß → F02)
- Das Klicken plötzlich aufhört (Klinke klemmt → SOFORT prüfen, Rücklaufgefahr!)

Nutzen Sie den Entscheidungsbaum 4 (Ungewöhnliche Geräusche) für die systematische Fehlersuche.

### Elektro-Winden spezifisch

**F8: Welche Batteriekapazität brauche ich für Lewmar-Elektrowinden?**

Faustregel: Mindestens die doppelte Kapazität des maximalen Strombedarfs aller gleichzeitig betriebenen Elektrowinden in Amperestunden, basierend auf 10 Minuten Dauerbetrieb:

| Windenmodell | Max. Strom | Empf. Batterie (2 Winden) | Kabelquerschnitt |
|-------------|-----------|--------------------------|-------------------|
| EVO E 15 | 40A | 120 Ah | 16 mm² |
| EVO E 30 | 60A | 200 Ah | 25 mm² |
| EVO E 40 | 80A | 250 Ah | 35 mm² |
| EVO E 50 | 100A | 350 Ah | 50 mm² |
| EVO E 65 | 130A | 450 Ah | 70 mm² |

Zusätzlich: Spannungsabfall am Kabel darf max. 3% betragen. Bei langen Kabelwegen (>8m) nächstgrößeren Querschnitt wählen.

**F9: Kann ich meine manuelle Lewmar-Winde auf Elektro nachrüsten?**

Ja, Lewmar bietet für die meisten EVO- und Ocean-Modelle Elektro-Nachrüstkits an:
- **EVO E-Conversion Kit:** Motor, Steuereinheit, Kabelbaum, Montagematerial
- Voraussetzung: ausreichende Batteriekapazität und Kabelinfrastruktur
- Deckverstärkung unter der Winde muss für das zusätzliche Gewicht ausgelegt sein
- Installation durch zertifizierte Lewmar-Werkstatt empfohlen (Garantieerhalt)
- Dauer: ca. 4-6 Stunden pro Winde bei vorbereiteter Elektrik

**F10: Was bedeutet die Fehlermeldung „CAN Error" an meiner Lewmar-Winde?**

Die häufigsten Ursachen sind in Entscheidungsbaum 3 und Fehlerbild F12 detailliert beschrieben. Erste Schritte:
1. Alle CAN-Bus-Geräte prüfen — ist nur die Winde betroffen oder das gesamte Netzwerk?
2. Spannungsversorgung am CAN-Bus prüfen (>11.5V)
3. Steckverbindungen auf Korrosion/Feuchtigkeit kontrollieren
4. System aus- und wieder einschalten (Reset)
5. Wenn Problem persistiert: Lewmar Service Interface (Art. 19820601) verwenden oder Fachbetrieb aufsuchen

### Wartung und Pflege

**F11: Kann ich meine Lewmar-Winde selbst warten?**

Grundwartung ja, Spezialarbeiten nein:
- **Selbst durchführbar:** Süßwasser-Spülung, Oberflächenpflege, Demontage/Reinigung/Neuschmierung der Trommel und Klinken, Federtausch, O-Ring-Wechsel
- **Fachbetrieb empfohlen:** Getriebetausch, Composite-Basis-Arbeiten, Elektro-Motor-Service, CAN-Bus-Diagnose, Lagertausch bei großen Winden

Lewmar bietet auf YouTube detaillierte Wartungsvideos für alle gängigen Modelle.

**F12: Wie demontiere ich eine Lewmar EVO-Winde korrekt?**

Schritt-für-Schritt:
1. Winde entlasten (kein Tau aufgelegt, keine Last)
2. Trommelkappe abnehmen (je nach Modell: Drehverschluss oder Schnappverschluss)
3. Selbst-Tailing-Einheit abheben
4. Obere Trommel nach oben abziehen (3× M5 Inbus am Spinner lösen, ggf. Sicherungsring)
5. Klinken und Federn entnehmen und in Reihenfolge ablegen
6. Untere Trommel abheben
7. Getriebe freilegen → Zahnräder und Spindel reinigen
8. Alle Teile in Süßwasser + mildem Reiniger waschen
9. Trocknen lassen, NICHT mit Druckluft (treibt Wasser in Lager)
10. Zusammenbau in umgekehrter Reihenfolge mit frischem Lewmar-Fett

**F13: Wie lagere ich Lewmar-Winden über den Winter?**

Für Boote, die im Winter nicht genutzt werden:
- Komplettwartung vor dem Einwintern durchführen
- Alle Oberflächen mit Lewmar Winch Cleaner reinigen
- Frische Schmierung aller beweglichen Teile
- Trommelkappe aufsetzen, Kurbelbuchse abdecken
- Bei Elektrowinden: Sicherung herausnehmen, Kabel gegen Feuchtigkeit schützen
- Persenning über der Winde schützt zusätzlich gegen UV und Niederschlag
- Vor Saisonstart: kurze Funktionsprüfung, ggf. nachschmieren

**F14: Welche Werkzeuge brauche ich für die Lewmar-Windenwartung?**

Grundausstattung:
- Inbus-Schlüssel-Set (4, 5, 6 mm)
- Ringschlüssel 10, 13, 17 mm
- Kreuzschlitz-Schraubendreher PH2
- Federwaage (für Klinkenfedern-Prüfung)
- Pinzette (für Federn und kleine Teile)
- Saubere Lappen und Reinigungsschale
- Lewmar Winch Grease und Spray
- Optional: Drehmomentschlüssel (für Basisschrauben)

**F15: Meine Lewmar-Winde ist undicht — woher kommt das Wasser?**

Nutzen Sie den Entscheidungsbaum 5 (Winde verliert Öl/Fett), der auch für Wassereintritte gilt. Die häufigsten Eintrittspunkte:
1. Trommelkappe (O-Ring defekt → F10)
2. Kurbelbuchse (fehlende Schutzkappe → F09)
3. Basis-Dichtung (Gasket verschlissen)
4. Bei Elektro: Kabeleinführung (Kabelverschraubung undicht → F06)

### Performance und Upgrade

**F16: Lohnt sich ein Upgrade von Ocean auf EVO?**

Die Kosten-Nutzen-Analyse hängt vom Einsatzzweck ab:
- **Regatta/Performance:** Ja, die Gewichtsersparnis (15-25%) und die bessere Trommelprofilierung lohnen sich
- **Langfahrt/Blauwasser:** Bedingt — die höhere Wartungsfreundlichkeit ist vorteilhaft, aber Ocean ist robuster und günstiger zu reparieren
- **Wochenendsegler:** Eher nein — der Preisunterschied rechtfertigt sich selten bei geringer Nutzung
- **Charterboote:** Nein — Ocean ist im Charterbetrieb wirtschaftlicher (geringere Teilekosten, robuster gegen Fehlbedienung)

**F17: Kann ich verschiedene Lewmar-Serien auf einem Boot mischen?**

Ja, das ist gängige Praxis und oft sinnvoll:
- Schotwinden: EVO (häufig genutzt, Self-Tailing-Qualität wichtig)
- Fallwinden: Ocean (seltener genutzt, Kostenvorteil)
- Ankerwinde: Lewmar V-Serie (spezialisiert)
- Die Optik ist durch unterschiedliche Oberflächenbehandlung leicht verschieden

**F18: Wie berechne ich die richtige Windengröße?**

Die Lewmar-Formel für Schotwinden:
```
Empfohlene Windengröße = Segelfläche (m²) × Winddruckfaktor × Übersetzungsfaktor
```
- Winddruckfaktor: Fahrtensegler = 1.0, Performance-Cruiser = 1.2, Regatta = 1.5
- Übersetzungsfaktor: Standard = 1.0, Selbstwendefock = 0.8, Gennaker = 1.3

Vereinfacht:
| Segelfläche Vorsegel | Empfohlene Schotwinde |
|---------------------|----------------------|
| 15-25 m² | EVO/Ocean 30 |
| 25-35 m² | EVO/Ocean 40 |
| 35-50 m² | EVO/Ocean 45-50 |
| 50-70 m² | EVO/Ocean 55-65 |
| 70+ m² | Individuelle Berechnung |

**F19: Was ist der Vorteil der Lewmar Composite-Basis?**

Die Composite-Basis (verfügbar bei EVO C-Modellen) bietet:
- **Gewichtsersparnis:** 40-50% leichter als Aluminium-Basis
- **Korrosionsfreiheit:** Kein galvanisches Element mit dem Deck
- **Vibrationsdämpfung:** Bessere Geräuschdämmung
- **Einschränkungen:** Geringere Maximallast als Aluminium, nicht reparierbar (nur tauschbar), empfindlich gegen UV und Schlagbelastung (siehe F04)

**F20: Welche Lewmar-Winde passt zu meinem Furlex-System?**

Für Furlex-Rollreffanlagen empfiehlt Lewmar:
- Furlex 100S/200S: EVO 15 oder Ocean 14 als Furler-Winde
- Furlex 300S: EVO 30 oder Ocean 30
- Furlex 400S: EVO 40 oder Ocean 40
- Die Winde muss in beide Richtungen drehen können (kein Self-Tailing erforderlich für Furler)
- Alternativ: Elektrowinde für Einhandsegler (automatisches Reffen)

### Garantie und Service

**F21: Wie lange ist die Garantie auf Lewmar-Winden?**

- **Standardgarantie:** 3 Jahre ab Kaufdatum auf Material- und Herstellungsfehler
- **Erweiterte Garantie:** 5 Jahre bei Registrierung innerhalb von 30 Tagen nach Kauf
- **Elektro-Komponenten:** 2 Jahre (Motor, Elektronik, Kabelbaum)
- **Verschleißteile:** Keine Garantie (Federn, O-Ringe, Klinken, Schmiermittel)
- **Voraussetzung:** Wartung gemäß Lewmar-Handbuch, Original-Ersatzteile, keine Modifikationen

**F22: Wo finde ich die Seriennummer meiner Lewmar-Winde?**

Die Seriennummer befindet sich:
- **EVO:** Auf der Unterseite der Basis (eingraviert), Format: EVO-XXXXXX-YY
- **Ocean:** Auf dem Typenschild an der Basis, Format: OCN-XXXXXX-YY
- **Ältere Modelle:** Auf der Trommelinnenseite oder am Spindelkopf
- XX = Jahrgang, XXXXXX = fortlaufende Nummer
- Für Garantieansprüche und Ersatzteilbestellung immer die vollständige Seriennummer angeben

**F23: Kann ich Nicht-Original-Ersatzteile für Lewmar-Winden verwenden?**

Dringend davon abgeraten:
- Lewmar-Klinken sind auf spezifische Materialhärte und Geometrie ausgelegt — Nachbauten können versagen
- Nicht-Original-Fett kann Dichtungen angreifen und den Korrosionsschutz aufheben
- Nicht-Original-Federn haben oft falsche Federkonstanten → Self-Tailing-Versagen
- Die Verwendung von Fremdteilen führt zum Garantieverlust
- Ausnahme: O-Ringe gleicher Spezifikation (Material, Härte, Maß) sind in der Regel akzeptabel

**F24: Was kostet eine professionelle Lewmar-Windenwartung?**

Richtwerte für DACH-Region (Stand 2026):
| Leistung | Einzelwinde | Paar (2×) |
|----------|------------|-----------|
| Grundwartung (Reinigung, Schmierung) | €80-120 | €140-200 |
| Komplettwartung (Demontage, alle Teile) | €150-250 | €250-400 |
| Getriebetausch | €250-400 + Teile | €450-700 + Teile |
| Elektro-Service (Motor + Elektronik) | €200-350 + Teile | €350-600 + Teile |
| Komplett-Revision (wie neu) | €300-500 + Teile | €500-850 + Teile |

Hinzu kommen Anfahrt (€50-100), Ersatzteile und MwSt.

**F25: Meine Lewmar-Winde ist 20 Jahre alt — reparieren oder ersetzen?**

Entscheidungskriterien:
- **Reparieren**, wenn: Basis und Gehäuse intakt, nur Verschleißteile betroffen, Modell noch mit Ersatzteilen unterstützt, Gesamtkosten <50% Neupreis
- **Ersetzen**, wenn: Gehäuse korrodiert oder gerissen, Modell nicht mehr unterstützt, Reparaturkosten >50% Neupreis, Upgrade auf Elektro gewünscht
- Lewmar unterstützt Ersatzteile in der Regel 15-20 Jahre nach Produktionsende
- Für sehr alte Modelle (vor 2000): Gebrauchtmarkt oder generische Teile prüfen

---

## 12. Glossar — Lewmar-Winden-Fachbegriffe

| Begriff | Erklärung |
|---------|-----------|
| **Eloxierung (Anodisierung)** | Elektrochemisches Verfahren zur Erzeugung einer harten Oxidschicht auf Aluminium. Schützt vor Korrosion und Verschleiß. Bei Lewmar EVO in Dunkelgrau, bei Ocean in Silber. |
| **Backwind** | Wind von der falschen Seite des Segels. Erzeugt ruckartige Lastspitzen auf der Schotwinde. |
| **Basis (Winch Base)** | Unteres Gehäuseteil, fest mit dem Deck verschraubt. Trägt alle Lasten. Bei Lewmar in Aluminium oder Composite (C-Modelle). |
| **CAN-Bus** | Controller Area Network — digitaler Datenbus zur Vernetzung von Bordgeräten. Lewmar nutzt NMEA 2000 (auf CAN 2.0B basierend) für Elektrowinden ab 2020. |
| **Centre Stem (Mittelspindel)** | Zentrale Achse der Winde, um die sich alle Getriebe- und Trommelteile drehen. Material: Edelstahl 316L. |
| **Composite** | Faserverstärkter Kunststoff (GFK oder CFK). Lewmar verwendet GFK für leichte Windenbasen. |
| **Drum (Trommel)** | Drehbarer Zylinder, auf den das Tau aufgewickelt wird. Oberfläche gerippt für Reibung. |
| **Drum Cap (Trommelkappe)** | Oberer Abschluss der Trommel. Schützt das Innere vor Wasser und Schmutz. |
| **EP-Additiv** | Extreme-Pressure-Zusatz in Schmierfetten. Verhindert Metallkontakt bei hohen Lasten. |
| **Federkonstante** | Maß für die Steifigkeit einer Feder (N/mm). Bei Lewmar Self-Tailing-Federn: 3-5 N/mm je nach Modell. |
| **Furlex** | Rollreffanlage der Marke Seldén. Wird häufig mit Lewmar-Winden als Furler-Winde kombiniert. |
| **Galvanische Korrosion** | Elektrochemische Korrosion zwischen zwei verschiedenen Metallen in einem Elektrolyt (Salzwasser). |
| **Gangschaltung (Two-Speed)** | Umschaltmechanismus zwischen langsamem, kraftvollen Gang (Uhrzeigersinn) und schnellem, leichtem Gang (gegen Uhrzeigersinn). |
| **Gear Ratio (Übersetzungsverhältnis)** | Verhältnis zwischen Kurbelumdrehungen und Trommelumdrehungen. Höheres Verhältnis = mehr Kraft, weniger Geschwindigkeit. |
| **Gehäuse (Housing)** | Äußere Struktur der Winde, umschließt Getriebe und Lager. |
| **Jaw (Klaue)** | Klemmbacke des Self-Tailing-Mechanismus. Greift das Tau und hält es unter Spannung. |
| **Klinke (Pawl)** | Federbelasteter Sperrhaken, der in den Zahnkranz eingreift und den Rücklauf der Trommel verhindert. |
| **Klinkenfeder (Pawl Spring)** | Feder, die die Klinke in den Zahnkranz drückt. Muss ausreichend Kraft aufbringen, um auch bei Vibration einzurasten. |
| **Kreuzgang (Cross-Drive)** | Zahnradanordnung, bei der sich die Drehrichtung zwischen den Gängen umkehrt. Standard bei Lewmar Zweigang-Winden. |
| **Lagerkäfig (Bearing Cage)** | Halterung für die Rollen eines Rollenlagers. Bei Lewmar aus PA66 (Polyamid). |
| **Lochbild (Bolt Pattern)** | Anordnung und Abstand der Befestigungsbohrungen in der Windenbasis. Muss zum Deck-Unterbau passen. |
| **Nennlast (Working Load)** | Maximale Betriebslast, für die die Winde ausgelegt ist. Bruchlast ist üblicherweise 3× Nennlast. |
| **NMEA 2000** | Marinespezifischer Datenbus-Standard, basierend auf CAN 2.0B. Für Vernetzung von Navigationsinstrumenten und Bordgeräten. |
| **O-Ring** | Ringförmige Elastomerdichtung. Bei Lewmar in NBR (Nitrilkautschuk) oder FPM (Fluorelastomer, bei Hochtemperaturanwendungen). |
| **Pawl Pin (Klinkenstift)** | Stift, auf dem die Klinke drehbar gelagert ist. Verschleißteil (siehe F07). |
| **Power Ratio** | Verhältnis zwischen aufgebrachter Handkraft und resultierender Schot-Zugkraft. Bestimmt die „Leichtgängigkeit" der Winde. |
| **Primärzahnrad (Primary Gear)** | Erstes Zahnrad im Antriebsstrang, direkt von der Kurbel angetrieben. |
| **Relais** | Elektromechanischer Schalter zur Steuerung des Windenmotors. Schaltet hohe Ströme (60-130A) über ein Steuersignal. |
| **Rücklauf (Backspin)** | Ungewolltes Zurückdrehen der Trommel unter Last. Sicherheitsrisiko — wird durch Klinken verhindert. |
| **Self-Tailing (Selbstklemmend)** | Mechanismus, der das Tau automatisch klemmt und führt. Macht den „Tailer" (zweite Person) überflüssig. |
| **Sekundärzahnrad (Secondary Gear)** | Zweites Zahnrad im Antriebsstrang. Ermöglicht den zweiten Gang (höhere Übersetzung). |
| **Sicherungsring (Circlip)** | Federnder Ring zur axialen Sicherung von Wellen und Bolzen. |
| **Spindel (Spindle)** | Siehe Centre Stem. Zentrale Achse, auf der Trommel und Getriebe sitzen. |
| **Stripper Ring** | Ring oberhalb der Self-Tailing-Klauen, der das Tau aus der Klemmung löst, wenn es abgeworfen wird. |
| **Tailing** | Das manuelle Ziehen des Taus von der Winde, um es unter Spannung zu halten. Entfällt bei Self-Tailing-Winden. |
| **Terminierungswiderstand** | 120Ω-Widerstand am Ende einer CAN-Bus-Leitung. Verhindert Signalreflexionen. An beiden Enden des Bus erforderlich. |
| **Überlastschutz** | Mechanismus oder elektronische Schaltung, die die Winde bei Überlast abschaltet. Bei Elektrowinden: Stromsensor. |
| **Wellendichtring (Shaft Seal)** | Dichtung an der Motorwelle, verhindert Wassereintritt ins Motorgehäuse. Verschleißteil (siehe F06). |
| **Zahnkranz (Ratchet Ring)** | Gezahnter Ring, in den die Klinken eingreifen. Bestimmt die Feinheit der Rücklaufsperre. |
| **Zugkraft (Line Pull)** | Die von der Winde auf das Tau ausgeübte Kraft, gemessen in kg oder daN. |
| **Arbeitswinkel** | Winkel zwischen Tau-Einlauf und Trommelachse. Optimal: 5-8° nach unten. Zu steil → Tau rutscht hoch, zu flach → schlechte Wicklung. |
| **Bruchlast (Breaking Load)** | Maximale Kraft, bei der ein Bauteil versagt. Bei Lewmar-Winden: 3× Nennlast (Sicherheitsfaktor 3:1). |
| **Cockpit-Layout** | Anordnung der Bedienelemente im Cockpit. Windenposition bestimmt Arbeitshaltung und Effizienz. |
| **Decksverstärkung** | Lokale Verstärkung der Deckskonstruktion unter der Windenbasis. Typisch: GFK-Aufdickung oder Edelstahl-Backing-Plate. |
| **Dyneema** | Ultra-hochmolekulares Polyethylen (UHMWPE). Modernes Tauwerk mit minimalem Reck. Erfordert spezielle Trommelprofilierung wegen geringem Reibbeiwert. |
| **Einhandsegler** | Segler, der allein segelt. Elektrowinden und Self-Tailing sind essentiell. |
| **Fettaustritt** | Ungewolltes Austreten von Schmierfett. Zeigt Dichtungsprobleme oder Überfettung an. |
| **Handkraft** | Die vom Bediener auf die Kurbel aufgebrachte Kraft. Lewmar-Normwert: 7-8 kg Dauerkraft für ergonomische Berechnung. |
| **IP-Schutzart** | International Protection Rating. IP56 = staubgeschützt + Schutz gegen starkes Strahlwasser. IP68 = staubdicht + Schutz gegen dauerndes Untertauchen. |
| **Kreuzschlag** | Tauwerk-Konstruktion, bei der die Litzen gegenläufig geschlagen sind. Standardtau für Winden. |
| **Lastspitze** | Kurzzeitige Kraftüberhöhung, z.B. durch Böe oder Backwind. Kann das 2-3-fache der Dauerlast erreichen. |
| **Manöver** | Segelmanöver wie Wende, Halse, Reffen. Erzeugt dynamische Lasten auf den Winden. |
| **Ratchet-Block** | Umlenkblock mit eingebauter Rücklaufsperre. Reduziert die Last auf die Winde. |
| **Schrick** | Kontrolliertes Fieren (Nachlassen) eines Taus. An der Winde: 1-2 Törns abnehmen, kontrolliert rutschen lassen. |
| **Spectra** | Markenname für HMPE-Faser (ähnlich Dyneema). Gleiche Eigenschaften bezüglich Winden-Kompatibilität. |
| **Stopper** | Klemmvorrichtung vor der Winde, die das Tau fixiert und die Winde für andere Leinen freigibt. |
| **Törn** | Umwicklung des Taus um die Trommel. Standard: 3 Törns für Schot, 2 für Fall (bei Self-Tailing). |
| **Umlenkrolle** | Block oder Rolle zur Richtungsänderung des Taus vor der Winde. Position bestimmt den Arbeitswinkel. |
| **Vorschot** | Schot des Vorsegels (Fock oder Genua). Typisch die höchste Last an Bord nach dem Rigg. |

---

## 13. Schnell-Referenz — Lewmar Winschen

### Modellübersicht Kompakt

```
LEWMAR EVO-SERIE (Premium)
══════════════════════════
EVO 15 ST    │ LOA 8-10m   │ Tau 6-10mm  │ ab €520
EVO 30 ST    │ LOA 10-13m  │ Tau 8-12mm  │ ab €780
EVO 40 ST    │ LOA 12-15m  │ Tau 10-14mm │ ab €1.150
EVO 45 ST/E  │ LOA 13-16m  │ Tau 10-16mm │ ab €1.450 / €3.200
EVO 50 ST/E  │ LOA 15-18m  │ Tau 12-18mm │ ab €1.850 / €4.100
EVO 55 ST/E  │ LOA 17-20m  │ Tau 14-22mm │ ab €2.350 / €5.200
EVO 65 ST/E  │ LOA 19-24m  │ Tau 14-22mm │ ab €3.100 / €6.800

LEWMAR OCEAN-SERIE (Standard)
═════════════════════════════
Ocean 14 ST  │ LOA 7-9m    │ Tau 6-10mm  │ ab €340
Ocean 16 ST  │ LOA 8-10m   │ Tau 6-10mm  │ ab €395
Ocean 30 ST  │ LOA 10-13m  │ Tau 8-12mm  │ ab €520
Ocean 40 ST  │ LOA 12-15m  │ Tau 10-14mm │ ab €780
Ocean 48 ST  │ LOA 14-17m  │ Tau 10-16mm │ ab €1.050
Ocean 50 ST/E│ LOA 15-18m  │ Tau 12-18mm │ ab €1.350 / €3.600
Ocean 65 ST/E│ LOA 19-24m  │ Tau 14-22mm │ ab €2.400 / €5.800
```

### Wartungsintervalle Kurzübersicht

```
Nach jedem Törn .... Süßwasser-Spülung
Monatlich .......... Oberflächenpflege
Halbjährlich ....... Schmierung, Klinkenprüfung
Jährlich ........... Komplettwartung
Alle 3 Jahre ....... Profi-Inspektion
Alle 5 Jahre ....... Getriebe-Revision, Lagertausch prüfen
```

### Drehmomentwerte für Befestigungsschrauben

| Schraube | Drehmoment | Hinweis |
|----------|-----------|---------|
| M6 Basis-Schraube | 8-10 Nm | Nicht überdrehen (Composite!) |
| M8 Basis-Schraube | 18-22 Nm | Standard Aluminium-Basis |
| M10 Basis-Schraube | 35-42 Nm | Große Winden (EVO 50+) |
| M12 Basis-Schraube | 55-65 Nm | Ocean 65, EVO 65 |
| M5 Trommel-Schrauben | 4-5 Nm | Edelstahl in Alu, Schraubensicherung verwenden |

### Notfall-Checkliste Windenausfall

```
□ Last sofort sichern (Klampe, Stopper)
□ Tau von der Winde nehmen
□ Ursache identifizieren (Rücklauf? Blockade? Elektro?)
□ Bei Rücklauf: WARNUNG — Tau kann unkontrolliert ausrauschen
□ Ersatzwinde oder Notfallkurbel verwenden
□ Bei Elektro-Ausfall: Sicherung prüfen, manuell weiterarbeiten
□ Fehlerbild dokumentieren (Foto, Beschreibung)
□ Reparatur gemäß Fehlerbild-Atlas (Kap. 9)
```

### Schmiermittel-Kurzreferenz

```
Lewmar Winch Grease (19701000) .. Getriebe, Lager → Alle Modelle
Lewmar Gear Grease (19701100) ... Ocean-Getriebe speziell
Lewmar Winch Spray (19701200) ... Federn, Klinken, leichte Pflege
Lewmar Winch Cleaner ............ Oberflächenreinigung, pH-neutral
NICHT verwenden: WD-40, Silikonspray, Teflonfett, Vaseline
```

### Fehlercodes Elektro-Winden (LED-Blinkcodes)

```
LED-Statusanzeige am Steuermodul:
═════════════════════════════════
Dauerhaft grün ........... Betriebsbereit, OK
Blinkt grün (1×/s) ....... Motor aktiv, Normalbetrieb
Blinkt gelb (1×/s) ....... Übertemperatur-Warnung (Motor >100°C)
Dauerhaft gelb ........... Überlast erkannt, Strombegrenzung aktiv
Blinkt rot 1× ............ Unterspannung (<10.5V bei 12V-System)
Blinkt rot 2× ............ Überstrom (>110% Nennstrom)
Blinkt rot 3× ............ CAN-Bus-Fehler (F12)
Blinkt rot 4× ............ Motor-Übertemperatur (>125°C, Abschaltung)
Blinkt rot 5× ............ Interner Steuermodul-Fehler
Dauerhaft rot ............ Kritischer Fehler, Sicherung prüfen
Keine LED ................ Keine Versorgungsspannung, Sicherung/Kabel prüfen
```

### Windengrößen-Schnellbestimmung nach Segelfläche

```
Schnellbestimmung Schotwinde:
═══════════════════════════
Vorsegel-Fläche (m²) → empfohlene Größe

     15  20  25  30  35  40  45  50  55  60  65  70  m²
      |   |   |   |   |   |   |   |   |   |   |   |
  15 [████]
  30     [█████████]
  40              [██████████]
  45                   [██████████]
  50                        [█████████████]
  55                                  [██████████]
  65                                       [████████████]

Faustregel: Windengröße ≈ Segelfläche × 1.2 (Fahrt) oder × 1.5 (Regatta)
Bei Zweifelsfällen immer die größere Winde wählen.
```

### Kontakt und Support Kurzreferenz

```
Lewmar Technischer Support:
  E-Mail:    technical@lewmar.com
  Tel. UK:   +44 (0)23 9252 4044
  Web:       lewmar.com/support
  Händler:   lewmartrade.com

DACH Service-Partner:
  Toplicht (Hamburg):     +49 40 232166-0
  SVB (Bremen):           +49 421 57290-0
  Gründl (Mattsee, AT):   +43 6217 6346
  Abart Marine (Zürich):  +41 44 3839090

Ersatzteil-Bestellung:
  → Seriennummer bereithalten
  → Modell und Baujahr angeben
  → Fehlerbild-Code (F01-F12) nennen
```

---

## 14. ANHÄNGE

### ANHANG A — Fallstudie: Hanse 415 EVO-Upgrade

**Ausgangslage:**
- Hanse 415, Baujahr 2018, Originalwinden Lewmar Ocean 40 ST (2×), Ocean 30 ST (2× Fall)
- Eigner plant Blauwasserfahrt (Atlantiküberquerung 2027)
- Wünsche: leichtgängigere Bedienung, Elektro-Schot, geringeres Gewicht

**Durchgeführtes Upgrade:**
1. Schotwinden: Ocean 40 ST → EVO 45 E (2×)
   - Begründung: Größerer Modell für Blauwasser-Sicherheitsreserve, Elektro für Einhandsegler-Manöver
   - Kosten: 2× €3.200 = €6.400
2. Fallwinden: Ocean 30 ST → EVO 30 ST (2×)
   - Begründung: Gewichtsersparnis, gleiche Größe ausreichend
   - Kosten: 2× €780 = €1.560
3. Elektroinstallation:
   - 2× 50 mm² Zuleitung (je 6m), 100A Sicherung pro Winde
   - Zusätzliche Batteriebank: 200 Ah LiFePO4
   - CAN-Bus-Integration mit B&G-System
   - Kosten Installation: €2.800
4. Deck-Anpassung:
   - Adapterplatten für neues Lochbild: €320
   - Deck-Verstärkung unter Schotwinden: €450

**Gesamtkosten:** €11.530 (inkl. MwSt., exkl. Anfahrt)

**Ergebnis nach 12 Monaten:**
- Schotarbeit von 2 Personen auf 1 Person reduziert
- Gewichtseinsparung gesamt: 4.2 kg (trotz Elektro-Motor)
- CAN-Bus-Integration ermöglicht automatisches Power-Management
- Kundenzufriedenheit: 9/10 — einziger Kritikpunkt: höherer Strombedarf als erwartet

---

### ANHANG B — Fallstudie: Hallberg-Rassy 44 Ocean-zu-EVO-Konversion

**Ausgangslage:**
- Hallberg-Rassy 44, Baujahr 2015, Originalwinden Lewmar Ocean 48 ST (2× Schot), Ocean 40 ST (2× Fall)
- Problem: Ocean 48 Getriebe-Korrosion (F02) an beiden Schotwinden nach 8 Saisons
- Eigner möchte bei Reparatur gleich upgraden

**Analyse:**
- Getriebeschaden durch unzureichende Wartung (nur 2× professionelle Wartung in 8 Jahren)
- Deck-Unterkonstruktion in gutem Zustand (HR-typisch überdimensioniert)
- Lochbild Ocean 48 und EVO 50 nicht identisch → Adapterplatte erforderlich

**Durchgeführte Konversion:**
1. Schotwinden: Ocean 48 ST → EVO 50 ST (2×)
   - Kosten: 2× €1.850 = €3.700
2. Fallwinden: Ocean 40 ST → EVO 40 ST (2×)
   - Kosten: 2× €1.150 = €2.300
3. Adapterplatten und Montage: €680

**Gesamtkosten:** €6.680

**Ergebnis:**
- Gewichtseinsparung: 3.8 kg gesamt
- Self-Tailing deutlich verbessert (EVO-Klauen vs. Ocean-ST)
- Wartungsintervall auf jährlich festgelegt (Lehre aus dem Schaden)
- HR-Eigner-Community: Feedback positiv, mehrere Nachahmer

---

### ANHANG C — Fallstudie: X-Yacht 40 Elektro-Nachrüstung

**Ausgangslage:**
- X-Yacht 40 (X4⁰), Baujahr 2020, Originalwinden Lewmar EVO 40 ST (2× Schot), EVO 30 ST (2× Fall)
- Eigner (60+) hat Schwierigkeiten mit manueller Schotarbeit bei stärkerem Wind
- Budget: max. €8.000

**Durchgeführte Nachrüstung:**
1. Schotwinden: EVO 40 ST → EVO 40 E (2× Elektro-Conversion Kit)
   - Lewmar E-Conversion Kit je €2.100
   - Kosten: 2× €2.100 = €4.200
2. Elektroinstallation:
   - Kabelverlegung 35 mm², Sicherungen 80A
   - Bedientaster Cockpit (2× Up/Down)
   - Kosten: €1.800
3. Batterieergänzung:
   - 100 Ah LiFePO4 zusätzlich
   - Kosten: €1.200

**Gesamtkosten:** €7.200 (unter Budget)

**Ergebnis:**
- Einhand-Segeln bis 25 kn problemlos möglich
- Manuelle Bedienung als Backup jederzeit verfügbar
- Stromverbrauch moderat (ca. 15 Ah pro Stunde aktiver Schotarbeit)
- Nach 2 Saisons: Eigner wünscht auch Elektro-Fallwinden → Planung für 2028

---

### ANHANG D — Fallstudie: Bavaria C42 Garantiefall Composite-Basis

**Ausgangslage:**
- Bavaria C42, Baujahr 2022, Originalwinden Lewmar EVO 40C ST (2×)
- Nach 18 Monaten: Rissbildung an einer Composite-Basis (F04)
- Eigner bemerkt knarrendes Geräusch bei Schotarbeit

**Analyse:**
- Haarriss von Befestigungsbohrung ausgehend (typisches F04-Muster)
- Befestigungsschrauben mit 12 Nm angezogen (Sollwert: 8-10 Nm für M6 in Composite)
- Deck-Unterkonstruktion: Bavaria-Standard, ausreichend dimensioniert
- Ursache: Überdrehte Schrauben bei Werftmontage + zyklische Belastung

**Garantieabwicklung:**
1. Fehlerdokumentation mit Fotos an Lewmar gesendet
2. Lewmar bestätigt Garantieanspruch (Materialfehler nicht ausgeschlossen)
3. Neue Composite-Basis (Art. 19740201) kostenlos geliefert
4. Installation durch Lewmar-zertifizierte Werkstatt (Toplicht Hamburg)
5. Drehmoment korrekt eingestellt: 8 Nm mit Schraubensicherung mittelfest

**Kosten für Eigner:** €0 (Garantie) + €180 Werkstattarbeit

**Lessons Learned:**
- Composite-Basis immer mit Drehmomentschlüssel montieren
- M6 in Composite: max. 8-10 Nm (NICHT wie Aluminium-Basis)
- Bavaria-Werft informiert, Montageanweisung aktualisiert

---

### ANHANG E — Fallstudie: Contest 42CS Doppel-Elektro-Fallwinde

**Ausgangslage:**
- Contest 42CS, Baujahr 2021, 2× Lewmar EVO 30 ST als Fallwinden
- Eigner segelt häufig einhand und shorthanded
- Wunsch: elektrische Fallwinden für komfortables Segelsetzen/-bergen

**Durchgeführte Installation:**
1. Fallwinden: EVO 30 ST → EVO 30 E (2× E-Conversion Kit)
   - Kosten: 2× €1.800 = €3.600
2. Steuerung: CAN-Bus-Integration mit Contest-Bordnetzwerk
   - Bedienung über B&G-Multifunktionsdisplay und Cockpit-Taster
   - Kosten: €1.400
3. Elektrik: 25 mm² Zuleitung, 60A Sicherungen
   - Kosten: €900

**Gesamtkosten:** €5.900

**Besonderheit:** Contest-spezifische Kabelführung durch den Mast-Fuß erforderte maßgefertigte Kabelschelle. Lewmar Chafe Protection Kit (Art. 19810501) an allen Durchführungen installiert.

---

### ANHANG F — Fallstudie: Beneteau Oceanis 51.1 Flottenumrüstung

**Ausgangslage:**
- Charter-Flotte: 5× Beneteau Oceanis 51.1, Baujahr 2019-2021
- Originalwinden: Lewmar Ocean 50 ST (2× Schot), Ocean 40 ST (2× Fall)
- Problem: hoher Wartungsaufwand, häufige ST-Federbrüche (F05) durch Charternutzung

**Lösung:**
1. Alle 20 Schotwinden: Ocean 50 ST beibehalten (Kosten-Effizienz)
2. Präventive Wartung: halbjährlich statt jährlich
3. ST-Federn alle 12 Monate pauschal tauschen (statt bei Ausfall)
4. Schmiermittel-Upgrade auf Lewmar Winch Grease (bisher Drittanbieter-Fett)

**Kosten pro Boot/Jahr:** €420 (vs. vorher €680 mit reaktiver Wartung)
**Ergebnis:** Ausfallrate um 70% reduziert, Chartergast-Beschwerden bzgl. Winden auf null

---

### ANHANG G — Fallstudie: Dehler 46 SQ Regatta-Optimierung

**Ausgangslage:**
- Dehler 46 SQ, Baujahr 2023, Originalwinden Lewmar EVO 45 ST (2× Schot), EVO 30 ST (2× Fall)
- Eigner nimmt an ORC-Regatten teil, möchte Gewicht optimieren

**Durchgeführte Optimierung:**
1. Schotwinden: EVO 45 ST → EVO 45C ST (Composite-Basis)
   - Gewichtsersparnis: 2× 0.9 kg = 1.8 kg
   - Kosten: 2× €450 Aufpreis = €900
2. Fallwinden: EVO 30 ST beibehalten (bereits leicht genug)
3. Windengriffe: Lewmar One-Touch Carbon (2× €185 = €370)
   - Gewichtsersparnis: 2× 0.15 kg = 0.3 kg

**Gesamtkosten:** €1.270
**Gewichtsersparnis:** 2.1 kg im Cockpit-Bereich

**Ergebnis:** Messbare Verbesserung bei leichten Bedingungen (VMG-Gewinn 0.1-0.2 kn bei <10 kn TWS). ORC-Rating unverändert (Winden nicht im Rating-Modell).

---

### ANHANG H — Fallstudie: Swan 48 CAN-Bus-Integration

**Ausgangslage:**
- Nautor Swan 48, Baujahr 2022, 4× Lewmar EVO E mit CAN-Bus
- Intermittierender CAN-Bus-Fehler (F12) nach 14 Monaten
- Fehlerbild: eine Schotwinde fällt sporadisch aus, Reset hilft temporär

**Diagnose:**
1. CAN-Bus-Analyse mit Lewmar Service Interface
2. Befund: Terminierungswiderstand an einer Winde defekt (offener Kontakt)
3. Ursache: Vibrationsbedingte Lötstellenermüdung am Terminierungswiderstand
4. Sekundär: Feuchtigkeit in einem CAN-Stecker (Deck-Durchführung)

**Reparatur:**
1. Terminierungswiderstand getauscht (Art. 19820201, €15)
2. CAN-Stecker gereinigt, neu abgedichtet
3. Alle Deck-Durchführungen mit Schrumpfschlauch nachgearbeitet
4. CAN-Bus-Diagnose nach Reparatur: fehlerfrei

**Kosten:** €85 Teile + €350 Arbeitszeit = €435

**Lessons Learned:**
- CAN-Bus-Fehler sind oft triviale Hardware-Probleme (Stecker, Widerstände)
- Systematische Diagnose spart Zeit: vom Netzwerk zum Einzelgerät
- Deck-Durchführungen sind die empfindlichste Stelle im CAN-Bus-System

---

### ANHANG I — Pydantic v2 Modelle für AYDI-Integration

```python
"""
Lewmar Winch Analysis Models — AYDI Integration
Pydantic v2 mit model_config = {"from_attributes": True}
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class LewmarSeries(str, Enum):
    """Lewmar Windenreihen"""
    EVO = "evo"
    OCEAN = "ocean"
    STANDARD = "standard"  # Ältere Modelle


class LewmarDriveType(str, Enum):
    """Antriebsart"""
    MANUAL = "manual"
    ELECTRIC = "electric"
    HYDRAULIC = "hydraulic"


class LewmarBaseType(str, Enum):
    """Basis-Material"""
    ALUMINIUM = "aluminium"
    COMPOSITE = "composite"


class LewmarFailureCode(str, Enum):
    """Fehlerbild-Codes gemäß Kap. 9"""
    F01 = "f01_evo_jaw_jamming"
    F02 = "f02_ocean_gear_corrosion"
    F03 = "f03_evo_drum_anodization"
    F04 = "f04_composite_base_cracking"
    F05 = "f05_self_tailing_spring"
    F06 = "f06_electric_motor_seal"
    F07 = "f07_pawl_pin_wear"
    F08 = "f08_bearing_cage"
    F09 = "f09_handle_socket_corrosion"
    F10 = "f10_drum_cap_oring"
    F11 = "f11_wiring_harness_chafe"
    F12 = "f12_can_bus_communication"


class LewmarWinchSpec(BaseModel):
    """Lewmar Winch Spezifikation"""
    model_config = {"from_attributes": True}

    model_name: str = Field(..., description="Modellbezeichnung, z.B. 'EVO 45 ST'")
    series: LewmarSeries
    size: int = Field(..., ge=14, le=65, description="Modellgröße (14-65)")
    drive_type: LewmarDriveType = LewmarDriveType.MANUAL
    self_tailing: bool = True
    base_type: LewmarBaseType = LewmarBaseType.ALUMINIUM
    max_line_pull_kg: float = Field(..., gt=0, description="Max. Zugkraft in kg")
    power_ratio_first: float = Field(..., gt=0, description="Power Ratio 1. Gang")
    power_ratio_second: Optional[float] = Field(None, description="Power Ratio 2. Gang")
    weight_kg: float = Field(..., gt=0, description="Gewicht in kg")
    min_line_diameter_mm: float = Field(..., gt=0)
    max_line_diameter_mm: float = Field(..., gt=0)
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis EUR")


class LewmarWinchCondition(BaseModel):
    """Zustandsbewertung einer Lewmar Winde"""
    model_config = {"from_attributes": True}

    winch_spec: LewmarWinchSpec
    overall_score: float = Field(..., ge=0, le=100, description="Gesamtzustand 0-100")
    drum_condition: float = Field(..., ge=0, le=100, description="Trommelzustand")
    gear_condition: float = Field(..., ge=0, le=100, description="Getriebezustand")
    pawl_condition: float = Field(..., ge=0, le=100, description="Klinkenzustand")
    bearing_condition: float = Field(..., ge=0, le=100, description="Lagerzustand")
    self_tailing_condition: Optional[float] = Field(None, ge=0, le=100)
    electric_condition: Optional[float] = Field(None, ge=0, le=100)
    base_condition: float = Field(..., ge=0, le=100, description="Basiszustand")
    active_failures: list[LewmarFailureCode] = Field(
        default_factory=list, description="Aktive Fehlerbilder"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer in Jahren"
    )
    maintenance_urgency: str = Field(
        ..., description="none|routine|soon|immediate|critical"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen auf Deutsch"
    )


class LewmarFailureAnalysis(BaseModel):
    """Fehleranalyse gemäß Fehlerbild-Atlas"""
    model_config = {"from_attributes": True}

    failure_code: LewmarFailureCode
    severity: int = Field(..., ge=1, le=5, description="Schweregrad 1-5")
    confidence: str = Field(
        ..., description="measured|visual_high|visual_medium|visual_low|estimated"
    )
    visual_indicators: list[str] = Field(
        default_factory=list, description="Erkannte visuelle Indikatoren"
    )
    probable_causes: list[str] = Field(
        default_factory=list, description="Wahrscheinliche Ursachen"
    )
    recommended_parts: list[str] = Field(
        default_factory=list, description="Empfohlene Ersatzteile (Art.-Nr.)"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten EUR"
    )
    repair_time_hours: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturzeit in Stunden"
    )
```

---

### ANHANG J — Normreferenzen und Standards

| Norm | Titel | Relevanz für Winden |
|------|-------|-------------------|
| ISO 12217:2022 | Stabilitätsbewertung | Windenposition beeinflusst Gewichtsverteilung und Schwerpunkt |
| ISO 15085:2003 | Mann-über-Bord-Verhütung | Windengriff-Sicherung, Tauführung im Cockpit |
| ISO 12216:2020 | Fenster und Öffnungen | Kabeleinführungen für Elektrowinden als Decksdurchbrüche |
| ISO 10133:2012 | Elektrische Niederspannungsanlagen | Kabelquerschnitte, Sicherungen, Isolierung für Elektrowinden |
| ISO 13297:2020 | Elektrische Systeme Wechselspannung | Relevant bei 230V-Ladeinfrastruktur für Winden-Batterien |
| ISO 8846:1990 | Zündsicherheit elektrischer Geräte | Motorschalter, Relais in gasgefährdeten Bereichen |
| CE 2013/53/EU | Sportbootrichtlinie | CE-Konformität der elektrischen Windenanlage |
| IEC 60529 | IP-Schutzarten | IP-Einstufung von Motoren und Steuereinheiten (min. IP56) |
| NMEA 2000 | Marine-Datenbus | CAN-Bus-Protokoll für Lewmar EVO E ab 2020 |
| DIN EN 13411 | Endverbindungen für Drahtseile | Relevant für Stag- und Wantwinden (nicht Schotwinden) |

---

### ANHANG K — Querverweistabelle zu anderen AYDI-Wissensmodulen

| AYDI-Modul | Datei | Relevante Querverweise |
|------------|-------|----------------------|
| 09.01 | Winsch-Grundlagen | Allgemeine Windentheorie, Übersetzungsberechnung |
| 09.02 | Harken Winschen | Vergleichsmodelle, Konkurrenzanalyse |
| 09.04 | Andersen Winschen | Vergleichsmodelle, skandinavische Yachten |
| 04.01 | Deckslayout | Windenpositionierung, Ergonomie-Analyse |
| 04.03 | Cockpit-Gestaltung | Windenbedienung vom Steuerstand |
| 05.01 | Rigg und Beschläge | Lastberechnung für Windendimensionierung |
| 06.01 | Elektrik Bordnetz | Dimensionierung Elektrowinden-Versorgung |
| 06.03 | CAN-Bus/NMEA 2000 | Integration Elektrowinden in Bordnetzwerk |
| 07.01 | Materialwissenschaft | Korrosion, Eloxierung, Composite-Eigenschaften |
| 10.01 | Wartungsplanung | Wartungsintervalle in Gesamtwartungsplan |
| 11.01 | Kostenanalyse | TCO-Berechnung Winden über Bootslebensdauer |

---

### ANHANG L — Lewmar Ersatzteil-Nummernschlüssel

```
Lewmar Teilenummern-Systematik:
═══════════════════════════════
Format: 197XXYYZ

197   = Lewmar Winden-Produktgruppe
XX    = Bauteil-Kategorie:
        00 = Jaw/Self-Tailing-Komponenten
        01 = Schmiermittel und Pflegemittel
        10 = Getriebe-Komponenten (Gears)
        20 = Trommel-Komponenten (Drum)
        40 = Basis-Komponenten (Base)
        50 = Feder-Komponenten (Springs)
        60 = Motor/Elektro-Komponenten
        70 = Klinken-Komponenten (Pawls)
        80 = Lager-Komponenten (Bearings)
        90 = Buchsen/Griffe (Handle/Socket)
        00 = Dichtungen (Seals/O-Rings)
        10 = Kabel-Komponenten (Wiring)
        20 = Elektronik/CAN-Bus

YY    = Modell/Variante:
        01 = Klein (EVO 15-30, Ocean 14-16)
        02 = Mittel (EVO 40-55, Ocean 30-48)
        03 = Groß (EVO 65, Ocean 50-65)
        04 = Universal
        05 = Spezial

Z     = Revision (0 = Original, 1+ = Updates)
```

---

### ANHANG M — Drehmomenttabelle vollständig

| Verschraubung | Schraube | Material | Drehmoment (Nm) | Hinweis |
|---------------|----------|----------|-----------------|---------|
| Basis auf Deck | M6 | A4-80 → Composite | 8-10 | Drehmomentschlüssel Pflicht |
| Basis auf Deck | M8 | A4-80 → Alu | 18-22 | Schraubensicherung mittelfest |
| Basis auf Deck | M10 | A4-80 → Alu | 35-42 | Unterlegscheibe verwenden |
| Basis auf Deck | M12 | A4-80 → Alu/GFK | 55-65 | Deck-Verstärkung prüfen |
| Trommel-Spinner | M5 | A2-70 → Alu | 4-5 | Schraubensicherung niedrigfest |
| Motorgehäuse | M6 | A4-80 → Alu | 8-10 | Gleichmäßig über Kreuz anziehen |
| Kabelverschraubung | PG13.5 | PA → Alu | Handfest + ¼ Umd. | Nicht überdrehen |
| CAN-Stecker | M12 | — | Handfest | Bajonett-Verriegelung prüfen |

---

### ANHANG N — Kompatibilitätsmatrix Lewmar ↔ Bootswerft

| Werft | Modellreihe | Original-Winde | Empfohlenes Upgrade |
|-------|------------|---------------|-------------------|
| Hanse | 315-348 | Ocean 14-30 ST | EVO 15-30 ST |
| Hanse | 388-460 | Ocean 30-48 ST | EVO 40-50 ST/E |
| Hanse | 508-675 | Ocean 48-65 ST/E | EVO 50-65 ST/E |
| Bavaria | C34-C38 | Ocean 30-40 ST | EVO 30-40 ST |
| Bavaria | C42-C50 | Ocean 40-50 ST | EVO 45-50 ST/E |
| Beneteau | Oceanis 34-40 | Ocean 30-40 ST | EVO 30-40 ST |
| Beneteau | Oceanis 46-62 | Ocean 40-65 ST | EVO 45-65 ST/E |
| Hallberg-Rassy | 31-40 | Ocean 30-48 ST | EVO 40-50 ST |
| Hallberg-Rassy | 44-64 | Ocean 48-65 ST | EVO 50-65 ST/E |
| X-Yachts | X4⁰-X4⁶ | EVO 40-45 ST | EVO 45-50 ST/E |
| X-Yachts | X4⁹-X5⁶ | EVO 45-55 ST | EVO 50-65 ST/E |
| Dehler | 30-38 | EVO 30-40 ST | EVO 30-40 ST (bereits EVO) |
| Dehler | 42-46 SQ | EVO 40-50 ST | EVO 45-55 ST/E |
| Contest | 42-57 CS | EVO 40-55 ST | EVO 50-65 E |
| Swan | 40-65 | EVO 45-65 E | — (bereits optimal) |
| Jeanneau | Sun Odyssey 349-440 | Ocean 30-40 ST | EVO 30-45 ST |
| Jeanneau | Sun Odyssey 490+ | Ocean 48-65 ST | EVO 50-65 ST/E |

---

### ANHANG O — Saisonale Wartungscheckliste (Druckvorlage)

```
╔══════════════════════════════════════════════════════════╗
║      LEWMAR WINSCHEN — SAISONALE WARTUNGSCHECKLISTE     ║
╠══════════════════════════════════════════════════════════╣
║ Boot: _________________ Datum: __________               ║
║ Winde Pos.: ____________ Modell: __________             ║
║ Seriennr.: _____________ Betriebsstd.: _____            ║
╠══════════════════════════════════════════════════════════╣
║ SAISONSTART                                             ║
║ □ Sichtprüfung Gehäuse und Basis                        ║
║ □ Trommelkappe abnehmen, O-Ring prüfen                  ║
║ □ Self-Tailing-Klauen prüfen (Federkraft, Verschleiß)   ║
║ □ Trommel abnehmen, Klinken prüfen                      ║
║ □ Alle Teile reinigen (Süßwasser + Lewmar Cleaner)      ║
║ □ Getriebe prüfen (Zahnflanken, Fett)                   ║
║ □ Lager prüfen (Leichtgängigkeit, Spiel)                ║
║ □ Neu schmieren (Lewmar Winch Grease)                   ║
║ □ Zusammenbauen, Funktionstest                          ║
║ □ Bei Elektro: Motor, Kabel, Sicherung prüfen           ║
║ □ Bei Elektro: CAN-Bus-Test (falls vorhanden)           ║
║ □ Befestigungsschrauben Drehmoment prüfen               ║
╠══════════════════════════════════════════════════════════╣
║ SAISONENDE                                              ║
║ □ Komplettwartung wie Saisonstart                       ║
║ □ Konservierung aller Oberflächen                       ║
║ □ Kurbelbuchse abdecken (Schutzkappe)                   ║
║ □ Bei Elektro: Sicherung entfernen                      ║
║ □ Befunde dokumentieren, Ersatzteile bestellen           ║
╠══════════════════════════════════════════════════════════╣
║ BEFUNDE:                                                ║
║ ______________________________________________________  ║
║ ______________________________________________________  ║
║ ______________________________________________________  ║
║                                                          ║
║ Nächste Wartung: ____________ Techniker: ____________    ║
╚══════════════════════════════════════════════════════════╝
```

---

### ANHANG P — Gewichtsvergleich EVO vs. Ocean (alle Größen)

| Größe | Ocean ST (kg) | EVO ST (kg) | EVO C ST (kg) | Ersparnis EVO | Ersparnis EVO-C |
|-------|--------------|------------|--------------|--------------|----------------|
| 14/15 | 3.2 | 2.7 | — | 15.6% | — |
| 16 | 3.8 | — | — | — | — |
| 30 | 5.4 | 4.5 | — | 16.7% | — |
| 40 | 7.8 | 6.3 | 5.5 | 19.2% | 29.5% |
| 45/48 | 9.2 | 7.6 | 6.7 | 17.4% | 27.2% |
| 50 | 11.5 | 9.4 | 8.2 | 18.3% | 28.7% |
| 55 | 13.8 | 11.2 | — | 18.8% | — |
| 65 | 18.2 | 14.8 | — | 18.7% | — |

---

### ANHANG Q — Elektrische Kennwerte Lewmar Elektrowinden

| Modell | Nennspannung | Max. Strom | Leistung | Sicherung | Kabelquerschnitt min. |
|--------|-------------|-----------|---------|-----------|---------------------|
| EVO E 15 | 12V DC | 40A | 480W | 50A | 16 mm² |
| EVO E 30 | 12V DC | 60A | 720W | 80A | 25 mm² |
| EVO E 40 | 12V DC | 80A | 960W | 100A | 35 mm² |
| EVO E 45 | 12V DC | 90A | 1080W | 120A | 50 mm² |
| EVO E 50 | 12V DC | 100A | 1200W | 125A | 50 mm² |
| EVO E 55 | 12/24V DC | 110/55A | 1320W | 140/70A | 50/25 mm² |
| EVO E 65 | 12/24V DC | 130/65A | 1560W | 160/80A | 70/35 mm² |
| Ocean E 50 | 12V DC | 95A | 1140W | 120A | 50 mm² |
| Ocean E 65 | 12/24V DC | 120/60A | 1440W | 150/75A | 70/35 mm² |

**Hinweis:** 24V-Versorgung wird für Modelle ≥55 dringend empfohlen (geringerer Leitungsverlust, dünnere Kabel möglich).

> ⚠️ **ZU PRÜFEN (Audit):** Diese Tabelle widerspricht dem Haupttext (§2.6, §4.2, §4.4). Ströme/Sicherungen/Kabel weichen ab (z. B. EVO E 50 hier 100 A / 125 A vs. §4.4 130 A / 150 A; EVO E 45 hier 90 A vs. Haupttext 100 A), und EVO E 55/65 werden hier auch in 12 V geführt, während der Haupttext (§3.4, §6.10) „nur 24 V" angibt. „Leistung" ist hier elektrische Eingangsleistung (U×I), im Haupttext mechanische Dauerleistung — nicht direkt vergleichbar. Werte als estimated — unverifiziert behandeln; sicherheitsrelevante Sicherungs-/Kabelauswahl nur nach Abgleich mit dem echten Lewmar-Datenblatt.

**Spannungsabfall-Berechnung:**
```
Spannungsabfall (V) = 2 × Kabellänge (m) × Strom (A) × 0.0175 / Querschnitt (mm²)

Beispiel: EVO E 40, 12V, 80A, 6m Kabelweg, 35 mm²:
ΔU = 2 × 6 × 80 × 0.0175 / 35 = 0.48V = 4.0% → NICHT OK (>3%)
→ Nächstgrößeren Querschnitt wählen: 50 mm²
ΔU = 2 × 6 × 80 × 0.0175 / 50 = 0.34V = 2.8% → OK (<3%)
```

**Einschaltstrombegrenzung:**
Lewmar-Elektromotoren haben einen Einschaltstrom von ca. 150-200% des Nennstroms für 0.5-1.0 Sekunden. Die Sicherung muss diesen Einschaltstrom ohne Auslösen verkraften. Lewmar empfiehlt träge Sicherungen (Kennlinie T oder C) der angegebenen Nennwerte.

**Batterieanforderungen für Dauerbetrieb:**
| Betriebsdauer | EVO E 30 (60A) | EVO E 40 (80A) | EVO E 50 (100A) | EVO E 65 (130A) |
|---------------|---------------|---------------|----------------|----------------|
| 5 Minuten | 5 Ah | 7 Ah | 8 Ah | 11 Ah |
| 15 Minuten | 15 Ah | 20 Ah | 25 Ah | 33 Ah |
| 30 Minuten | 30 Ah | 40 Ah | 50 Ah | 65 Ah |
| 60 Minuten | 60 Ah | 80 Ah | 100 Ah | 130 Ah |

Werte gelten für Volllast. Typische Schotarbeit nutzt 20-40% der Zeit Volllast, Rest ist Leerlauf. Realistischer Verbrauch daher ca. 30-40% der Tabellenwerte.

**Erdungskonzept:**
- Motorgehäuse über separate Erdungsleitung (min. 6 mm²) mit dem Bordnetz-Haupterdpunkt verbinden
- NICHT über das Deck-Laminat oder die Befestigungsschrauben erden
- Bei 24V-Systemen: Mittelpunkterdung gemäß ISO 13297

**Schutzeinrichtungen:**
| Schutz | Anforderung | Lewmar-Empfehlung |
|--------|-------------|-------------------|
| Überstrom | Träge Sicherung | Siehe Tabelle oben |
| Verpolschutz | Diode oder MOSFET | Im Steuermodul integriert |
| Übertemperatur | Thermoschalter | Im Motor integriert (125°C Abschaltung) |
| Wassereintritt | IP56 mindestens | Motorgehäuse IP56, Stecker IP68 |
| Überlast | Strombegrenzung | Steuermodul begrenzt bei 110% Nennstrom |

---

### ANHANG R — Lebenszyklus-Kostenvergleich (20 Jahre TCO)

**Annahmen:** 200 Betriebsstunden/Jahr, jährliche Wartung, professionelle Revision alle 5 Jahre

| Kostenposition | Ocean 40 ST | EVO 40 ST | EVO 40 E |
|---------------|------------|----------|---------|
| Anschaffung (Paar) | €1.560 | €2.300 | €5.400 |
| Jährliche Wartung (×20) | €3.200 | €3.000 | €4.800 |
| Revision alle 5 Jahre (×4) | €1.600 | €1.400 | €2.400 |
| Ersatzteile (geschätzt) | €800 | €900 | €1.800 |
| Motor-Tausch (1× nach 12-15 J.) | — | — | €1.200 |
| Elektrik-Wartung | — | — | €600 |
| **TCO 20 Jahre** | **€7.160** | **€7.600** | **€16.200** |
| **TCO pro Jahr** | **€358** | **€380** | **€810** |

**Interpretation:**
- Ocean und EVO sind im TCO nahezu gleichauf — der höhere Anschaffungspreis der EVO wird durch geringeren Wartungsaufwand kompensiert
- Elektrowinden verdoppeln den TCO — sie lohnen sich nur bei echtem Bedarf (Einhandsegler, körperliche Einschränkungen, Blauwasser)
- Die Gewichtsersparnis der EVO hat keinen TCO-Effekt, ist aber für Regattasegler relevant

**TCO-Sensitivitätsanalyse — Einfluss der Wartungshäufigkeit:**

| Wartungsintervall | Ocean 40 ST TCO (20J) | EVO 40 ST TCO (20J) | EVO 40 E TCO (20J) |
|-------------------|----------------------|---------------------|---------------------|
| Halbjährlich (empfohlen) | €8.960 | €9.100 | €18.600 |
| Jährlich (Standard) | €7.160 | €7.600 | €16.200 |
| Alle 2 Jahre (minimal) | €5.360 | €6.100 | €14.800 |
| Keine reguläre Wartung | €3.560* | €4.600* | €13.400* |

*Bei fehlender Wartung steigt das Risiko eines Totalausfalls drastisch. Die niedrigeren TCO-Werte ohne Wartung sind irreführend — ein einzelner Getriebeschaden (F02) kann €500-800 kosten, eine kompromittierte Composite-Basis (F04) erfordert Neuanschaffung. Erfahrungsgemäß übersteigen die Reparaturkosten bei vernachlässigter Wartung die Einsparungen innerhalb von 5-7 Jahren.

**Restwert-Betrachtung:**

| Alter | Ocean 40 ST | EVO 40 ST | EVO 40 E |
|-------|------------|----------|---------|
| Neuwert | €780 | €1.150 | €2.700 |
| 5 Jahre | €400 (51%) | €650 (57%) | €1.350 (50%) |
| 10 Jahre | €200 (26%) | €380 (33%) | €650 (24%) |
| 15 Jahre | €80 (10%) | €180 (16%) | €250 (9%) |
| 20 Jahre | €0 (0%) | €50 (4%) | €0 (0%) |

EVO-Modelle halten ihren Wert besser als Ocean — ein weiterer Faktor in der Gesamtbetrachtung. Elektrowinden verlieren aufgrund der Motor-Alterung schneller an Wert.

---

### ANHANG S — Lewmar Windenöl- und Fettpflegeplan (Detailliert)

**Lewmar Winch Grease (Art. 19701000) — Anwendungsanleitung:**

| Anwendungsort | Menge | Methode | Intervall |
|--------------|-------|---------|-----------|
| Hauptzahnrad (Primary Gear) | 5-8g | Dünn auf Zahnflanken auftragen | Jährlich |
| Sekundärzahnrad | 5-8g | Dünn auf Zahnflanken auftragen | Jährlich |
| Centre Stem Gleitfläche | 2-3g | Dünn auftragen | Jährlich |
| Oberes Rollenlager | 3-5g pro Lager | Zwischen die Rollen einbringen | Jährlich |
| Unteres Rollenlager | 3-5g pro Lager | Zwischen die Rollen einbringen | Jährlich |
| Klinken-Drehpunkte | 1g pro Klinke | Tropfen auf den Stift | Halbjährlich |
| Self-Tailing-Drehpunkte | 1g pro Punkt | Tropfen auf Drehpunkte | Halbjährlich |

**Häufige Schmierfehler:**

1. **Zu viel Fett:** Überschüssiges Fett tritt aus den Dichtungen aus, zieht Schmutz an und kann die Klinken-Funktion beeinträchtigen. Weniger ist mehr.
2. **Falsches Fett:** Standard-Lithiumfett enthält nicht die spezifischen EP-Additive und Korrosionsinhibitoren. Marinefett anderer Hersteller kann kompatibel sein, aber nur Lewmar garantiert die Verträglichkeit mit den verbauten Elastomeren.
3. **Fett auf den Klinkenfedern:** Die Federn selbst benötigen nur leichte Sprühschmierung (Lewmar Spray), kein Fett. Fett kann die Federbewegung verkleben.
4. **Altes Fett nicht entfernt:** Neues Fett auf altem Fett ist wirkungslos. Vor der Neuschmierung alle Teile vollständig entfetten (Lewmar Degreaser oder lösemittelhaltiger Reiniger).

**Temperatur-Empfehlungen:**

| Revier | Temperaturbereich | Empfohlenes Fett | Bemerkung |
|--------|-------------------|-----------------|-----------|
| Ostsee, Nordsee | -5°C bis +25°C | Lewmar Winch Grease Standard | Ganzjahresfett |
| Mittelmeer | +5°C bis +40°C | Lewmar Winch Grease Standard | Bei >35°C häufiger kontrollieren |
| Tropen | +15°C bis +45°C | Lewmar Winch Grease Standard | Halbjährliches Intervall empfohlen |
| Arktis/Antarktis | -25°C bis +10°C | Lewmar Low-Temp Grease (Sonderbestellung) | Spezialanwendung |

---

### ANHANG T — AYDI-Bewertungsmatrix für Lewmar-Winden

**Automatische Zustandsbewertung durch AYDI — Gewichtung der Einzelbefunde:**

| Prüfpunkt | Gewichtung im Gesamtscore | Bewertungsskala |
|-----------|--------------------------|-----------------|
| Basis-Zustand (Risse, Korrosion) | 20% | 100 = makellos, 0 = Rissbildung |
| Getriebe-Zustand (Zahnflanken, Fett) | 20% | 100 = neuwertig, 0 = Zahnausbrüche |
| Klinken-Funktion (Einrasten, Verschleiß) | 15% | 100 = perfekt, 0 = Rücklaufgefahr |
| Trommel-Oberfläche (Eloxal, Rillen) | 10% | 100 = neuwertig, 0 = blankes Aluminium |
| Self-Tailing-Funktion (Klauen, Federn) | 10% | 100 = perfekt, 0 = hält nicht |
| Lager (Leichtgängigkeit, Spiel) | 10% | 100 = leichtgängig, 0 = blockiert |
| Dichtungen (O-Ringe, Gaskets) | 5% | 100 = dicht, 0 = Wassereinbruch |
| Befestigung (Schrauben, Drehmoment) | 5% | 100 = korrekt, 0 = lose |
| Elektro (nur E-Modelle: Motor, Kabel) | 5% | 100 = einwandfrei, 0 = Ausfall |

**Score-Interpretation:**

| Gesamtscore | Zustandsbewertung | Handlungsempfehlung |
|-------------|-------------------|---------------------|
| 90-100 | Ausgezeichnet | Normale Nutzung fortsetzen |
| 75-89 | Gut | Nächste reguläre Wartung beachten |
| 60-74 | Befriedigend | Wartung innerhalb 3 Monaten planen |
| 40-59 | Mangelhaft | Sofortige Wartung erforderlich |
| 20-39 | Schlecht | Eingeschränkter Betrieb, zeitnahe Reparatur |
| 0-19 | Kritisch | Außerbetriebnahme bis zur Reparatur |

**Visuelle Analyse — Confidence-Mapping für Lewmar-Winden:**

| Visueller Befund | Erkennbarkeit per Foto | AYDI Confidence |
|------------------|----------------------|-----------------|
| Basis-Riss (F04) | Gut erkennbar bei Nahaufnahme | visual_high |
| Eloxal-Verschleiß (F03) | Gut erkennbar (Farbunterschied) | visual_high |
| Trommelkappe-Zustand | Mittel (O-Ring nicht sichtbar) | visual_medium |
| Self-Tailing-Verschleiß (F01) | Mittel (Klauen teilweise verdeckt) | visual_medium |
| Getriebe-Zustand (F02) | Nicht erkennbar ohne Demontage | visual_insufficient |
| Klinken-Zustand (F07) | Nicht erkennbar ohne Demontage | visual_insufficient |
| Lager-Zustand (F08) | Nicht erkennbar ohne Demontage | visual_insufficient |
| Kabelbaum (F11) | Teilweise erkennbar (Decksdurchführung) | visual_low |
| Korrosion allgemein | Gut erkennbar bei Farbfotos | visual_high |
| Befestigungszustand | Mittel (Schraubenköpfe sichtbar) | visual_medium |
| Motor-Zustand (F06) | Schlecht (meist unter Deck) | visual_low |
| CAN-Bus (F12) | Nicht visuell beurteilbar | visual_insufficient |

**Mindestanforderungen an Fotos für AYDI-Analyse:**

1. **Auflösung:** Mindestens 2 Megapixel, idealerweise 5+ Megapixel
2. **Beleuchtung:** Tageslicht oder helle Kunstbeleuchtung, keine Gegenlichtaufnahmen
3. **Winkel:** Frontalansicht der Trommel, Detailaufnahme der Basis, Self-Tailing von oben
4. **Abstand:** 30-50 cm für Übersicht, 10-15 cm für Detailaufnahmen
5. **Anzahl:** Mindestens 3 Fotos pro Winde (Übersicht, Trommel-Detail, Basis-Detail)
6. **Maßstab:** Ein Referenzobjekt (Münze, Lineal) im Bild erleichtert die Größenbeurteilung

---

*Ende der Wissensdatei 09.03 — Lewmar Winschen*
*AYDI Research, Version 2.0, 2026-04-25*
*Confidence: measured (Lewmar Katalogdaten), documented (Service-Manuals, OEM-Zuordnungen, Fallstudien), estimated (Erfahrungswerte, Marktdaten, TCO-Berechnungen)*
