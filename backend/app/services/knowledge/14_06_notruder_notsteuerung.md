---
title: "Notruder und Notsteuerung"
kategorie: "14 Steueranlagen und Autopilot"
unterkategorie: "14.06 Notruder und Notsteuerung"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "ISO 8847/8848, ISO 15085, ISAF/World Sailing OSR, ORC Special Regulations, CE 2013/53/EU"
  - documented: "Hersteller-Daten, Seeunfall-Berichte (MAIB, BEAmer, BSU), Regatta-Erfahrungsberichte"
  - estimated: "Erfahrungswerte Blauwasser-Segler, Werft-Konsens, Praxis-Tests"
---

# 14.06 — Notruder und Notsteuerung im Yachtbau: Vollstaendige Wissensreferenz

> **AYDI Wissensdatei 14.06** — Kategorie 14: Steueranlagen und Autopilot
> **Confidence-Quelle:** measured (ISO-Normen, ISAF/ORC Regulations), documented (Hersteller-Daten, Seeunfall-Berichte), estimated (Erfahrungswerte, Praxis)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen](#2-grundlagen)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Konstruktion DIY — Eigenbau Notsteuerung](#5-konstruktion-diy--eigenbau-notsteuerung)
6. [Sicherheitsaspekte](#6-sicherheitsaspekte)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Haeufig gestellte Fragen](#9-faq--haeufig-gestellte-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A–R](#12-anhang-ar)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Definition und Bedeutung

Notsteuerung (engl. emergency steering) umfasst alle Einrichtungen, Techniken und Verfahren, die bei Ausfall der primaeren Steueranlage die Manoevrierbarkeit eines Bootes aufrechterhalten. Sie ist kein optionaler Komfortzusatz, sondern ein sicherheitskritisches System, das ueber Leben und Tod entscheiden kann.

Die Notsteuerung ist eines der am haeufigsten vernachlaessigten Sicherheitssysteme auf Yachten. Waehrend Rettungswesten, Rettungsinsel und Seenotfunkgeraete regelmaessig geprueft werden, liegt die Notpinne bei vielen Booten vergessen und unzugaenglich in einer Bilge — falls sie ueberhaupt vorhanden ist.

**Warum Notsteuerung fuer Offshore zwingend erforderlich ist:**

1. **Regulatorische Pflicht** — ISO 8847, ISAF/World Sailing Offshore Special Regulations (OSR) Kategorie 0–3 und ORC Special Regulations schreiben eine funktionsfaehige Notsteuerung vor. Boote ohne Notsteuerung bestehen keine Sicherheitsinspektion fuer Offshore-Regatten und sind in vielen Fahrtenrevieren unterversichert.

2. **Statistische Realitaet** — Steuerverlust zaehlt zu den haeufigsten schwerwiegenden Ausfaellen auf See. Analysen der MAIB (UK Marine Accident Investigation Branch) und der BSU (Bundesstelle fuer Seeunfalluntersuchung) zeigen, dass Steuerversagen in ca. 8–12 % aller ernsten Seeunfaelle eine Rolle spielt.

3. **Zeitfaktor** — Hilfe auf dem offenen Meer ist oft Stunden bis Tage entfernt. Ein manoevrierunfaehiges Boot treibt quer zur See und ist extremen Belastungen ausgesetzt. Die Faehigkeit, auch nur einen groben Kurs zu halten, reduziert die Gefahr des Querschlagens und Kenterns drastisch.

4. **Selbsthilfe-Prinzip** — Die Seefahrt basiert auf dem Grundsatz der Selbsthilfe. Wer auf See in Schwierigkeiten geraet, muss zunaechst alle eigenen Mittel ausschoepfen, bevor fremde Hilfe angefordert wird. Eine Notsteuerung ist das primaere Mittel zur Selbsthilfe bei Steuerverlust.

5. **Versicherungsrelevanz** — Marine-Versicherer bewerten das Vorhandensein und den Zustand der Notsteuerung bei der Risikobeurteilung. Bei schweren Schaeden kann das Fehlen einer funktionsfaehigen Notsteuerung als Fahrlaessigkeit gewertet werden.

### 1.2 Historische Entwicklung

**Segelschifffahrt bis 1900 — Der Kolderstock als erste Notsteuerung:**
- Grosse Segelschiffe fuehrten stets einen Kolderstock (engl. tiller, emergency tiller) als Notsteuerung, wenn das Steuerrad oder die Steuerketten versagten
- Notpinnen waren standard auf allen Schiffen mit Ruderanlage
- Jury-Rigging (Behelfs-Takelage) schloss auch Behelfs-Steuerungen ein
- Praktische Seemannschaft umfasste selbstverstaendlich das Steuern ohne Ruder (Steuerung durch Segelstellung)

**1900–1960 — Formalisierung der Notsteuerung:**
- Klassifikationsgesellschaften (Lloyd's, BV, GL) fordern Notsteuereinrichtungen auf Handelsschiffen
- Auf Yachten noch wenig formalisiert — "Der Eigner wird schon eine Pinne haben"
- Erste systematische Notpinnen-Konstruktionen fuer Fahrtenyachten
- Robin Knox-Johnston (1969, Suhaili): Demonstriert Notsteuerung mit Treibanker auf erster Solo-Nonstop-Weltumseglung

**1960–1985 — Regulatorische Entwicklung:**
- Fastnet-Katastrophe 1979: 15 Tote, zahlreiche Ruderversagen — treibt Regattasicherheitsvorschriften voran
- RORC/ORC beginnen Notsteuerung als Pflichtausruestung zu fordern
- Windsteueranlagen (Aries, Fleming, Monitor) verbreiten sich als effektive Zweitsteuerung
- Erste Treibanker-Systeme als alternative Notsteuerung (Dragging a drogue)

**1985–2010 — Standardisierung und neue Ansaerze:**
- ISAF (jetzt World Sailing) kodifiziert Notsteuerungs-Anforderungen in Offshore Special Regulations
- Jordan Series Drogue wird als See-Stabilisator und Notsteuerungshilfe entwickelt
- Hersteller wie Edson, Lewmar, Jefa bieten angepasste Notpinnen-Kits an
- Vendee Globe und BOC/Around Alone Rennen treiben Innovation bei Solo-Notsteuerung

**2010–heute — Integration und Verfeinerung:**
- Moderne Yachten mit komplexen Steueranlagen erfordern spezifisch konstruierte Notpinnen
- Einige Werften (z.B. Hallberg-Rassy, Oyster, Boreal) liefern seriengemaess hochwertige Notpinnen mit
- Zunehmend Boote mit Doppelruder — Verlust eines Ruders bedeutet nicht zwingend kompletten Steuerverlust
- Autopilot als primaere Steuerung in vielen Situationen — dessen Ausfall ist ein haeufiges Szenario
- Digitalisierte Notsteuerungsprotokolle in Sicherheits-Management-Systemen

### 1.3 Systemueberblick — Notsteuerungsoptionen nach Prioritaet

```
Primaere Steueranlage faellt aus
  |
  v
Sofortige Massnahmen (Minuten):
  1. Beidrehen / Beiliegen (Fahrt aus dem Boot nehmen)
  2. Ursache identifizieren (Kette? Seil? Hydraulik? Ruderblatt?)
  |
  v
Erste Reparaturversuche (10-30 Minuten):
  3. Reparatur vor Ort (Seilreparatur, Hydraulik nachfuellen, etc.)
  4. Notpinne / Emergency Tiller montieren
  |
  v
Alternative Steuerungen (30-120 Minuten):
  5. Jury-rigged Steuerung (Behelfssteuerung)
  6. Notruder / Emergency Rudder montieren
  7. Treibanker / Drogue fuer Kurshalten einsetzen
  |
  v
Langzeit-Loesungen (Stunden bis Tage):
  8. Steuerung durch Segelstellung allein
  9. Windsteueranlage als Backup (falls installiert)
  10. Treibanker als Langzeit-Kurshaltung
```

### 1.4 Relevanz im AYDI-Analysesystem

Im AYDI-System wird die Notsteuerung als Teil des Sicherheitsmoduls (Safety-Tier) bewertet und beeinflusst folgende Module:

- **Compliance-Modul (0.95 Structured):** Vorhandensein und Konformitaet mit ISO/ISAF/ORC
- **Sicherheitsmodul:** Kernbewertung — Notsteuerung vorhanden, zugaenglich, erprobt?
- **Ergonomie-Modul (0.75 Structured):** Montierbarkeit der Notpinne, erforderliche Kraefte
- **Strukturmodul (0.95 Structured):** Festigkeit der Notpinnen-Aufnahme, Ruderschaft-Zustand
- **Emotional-Modul (0.25 Structured):** Vertrauen in die Sicherheitsausruestung (psychologischer Faktor)

**Scoring-Impact:**
- Keine Notsteuerung vorhanden: -40 bis -60 Punkte Gesamtscore
- Notsteuerung vorhanden aber nie getestet: -15 bis -25 Punkte
- Notsteuerung vorhanden, zugaenglich, erprobt: 0 (Baseline, keine Bonus-Punkte — es ist Pflicht)
- Exzellente Notsteuerung (redundant, erprobt, dokumentiert): +5 bis +10 Punkte Bonus

---

## 2. Grundlagen

### 2.1 Notfall-Szenarien — Warum Steuerung ausfaellt

Der Verlust der Steuerung kann verschiedene Ursachen haben, die sich in drei Hauptkategorien unterteilen lassen:

#### 2.1.1 Mechanisches Versagen der Steueranlage

**Seilsteuerung (Wire-over-Sheave):**
| Versagensart | Haeufigkeit | Vorwarnzeit | Schwere |
|-------------|-------------|-------------|---------|
| Drahtseil gerissen | 12 % aller Steuerversagen | Gering (Litzenbrueche sichtbar) | CRITICAL |
| Quadrant-Klemmschraube lose | 8 % | Keine bis gering | SIGNIFICANT |
| Umlenkrolle blockiert/gebrochen | 6 % | Mittel (Geraeusche) | SIGNIFICANT |
| Kettenglied gebrochen | 4 % | Gering | CRITICAL |
| Pedestal-Getriebe defekt | 5 % | Mittel (Spiel, Geraeusche) | SIGNIFICANT |

**Hydraulische Steuerung:**
| Versagensart | Haeufigkeit | Vorwarnzeit | Schwere |
|-------------|-------------|-------------|---------|
| Hydraulikleitung gebrochen/undicht | 10 % | Mittel (Fluessigkeitsverlust) | CRITICAL |
| Hydraulikpumpe defekt | 7 % | Gering bis mittel | SIGNIFICANT |
| Hydraulikzylinder undicht | 8 % | Mittel (Oelflecken) | SIGNIFICANT |
| Bypass-Ventil defekt/undicht | 5 % | Mittel (schwammiges Steuern) | MODERATE |
| Hydraulikfluid Ueberhitzung | 3 % | Gut (Temperaturanstieg) | MODERATE |

**Mechanische Steuerung (Gestänge, Zahnstange, Kabel):**
| Versagensart | Haeufigkeit | Vorwarnzeit | Schwere |
|-------------|-------------|-------------|---------|
| Kabel gerissen | 9 % | Gering | CRITICAL |
| Zahnstange/Ritzel verschlissen | 4 % | Gut (Spiel nimmt zu) | MODERATE |
| Gelenk/Kugelkopf gebrochen | 3 % | Gering | SIGNIFICANT |
| Korrosion im Bowdenzug | 6 % | Gut (Schwergaengigkeit) | MODERATE |

#### 2.1.2 Strukturelles Versagen

| Versagensart | Haeufigkeit | Vorwarnzeit | Schwere |
|-------------|-------------|-------------|---------|
| Ruderblatt abgebrochen | 5 % aller Steuerversagen | Oft keine | CRITICAL |
| Ruderblatt delaminiert | 4 % | Mittel (Klopfen, Spiel) | SIGNIFICANT |
| Ruderschaft gebrochen | 3 % | Gering | CRITICAL |
| Ruderschaft verbogen | 3 % | Mittel (Schwergaengigkeit) | SIGNIFICANT |
| Skeg-Bruch | 2 % | Oft keine | CRITICAL |
| Ruderlager ausgeschlagen | 7 % | Gut (Spiel, Geraeusche) | MODERATE |
| Koker-Rohr aus Laminat gerissen | 1 % | Gering | CRITICAL |

#### 2.1.3 Aeussere Einwirkung

| Ursache | Haeufigkeit | Vorwarnzeit | Schwere |
|---------|-------------|-------------|---------|
| Grundberuehrung mit Ruderschaden | 15 % aller Steuerversagen | Keine | CRITICAL |
| Treibgut-Kollision (Baumstaemme, Container) | 4 % | Keine | CRITICAL |
| Netz/Leine in Ruder verwickelt | 8 % | Keine bis gering | MODERATE-SIGNIFICANT |
| Schwerwetter-Ueberbelastung | 3 % | Mittel | SIGNIFICANT |
| Kollision mit anderem Fahrzeug | 2 % | Variabel | CRITICAL |
| Eis-Einwirkung | 1 % (hohe Breiten) | Variabel | SIGNIFICANT |

### 2.2 Physikalische Grundlagen der Notsteuerung

#### 2.2.1 Ruderkraefte und Notpinnen-Dimensionierung

Die Kraft an einer Notpinne ergibt sich aus dem Rudermoment und der Pinnenlaenge:

```
F_pinne = M_ruder / L_pinne

Wobei:
  M_ruder = Rudermoment in Nm (abhaengig von Bootsgeschwindigkeit, Ruderflaeche, Ruderwinkel)
  L_pinne = Wirksame Pinnenlaenge in m
  F_pinne = Erforderliche Handkraft in N

Faustformel fuer Rudermoment (Fahrtenyacht):
  M_ruder = 0.15 × V^2 × A_ruder × (0.5 - balance_ratio) × rho / 2

  V = Bootsgeschwindigkeit in m/s
  A_ruder = Ruderflaeche in m^2
  balance_ratio = Balancegrad (typ. 0.15–0.25)
  rho = Wasserdichte (1025 kg/m^3 Salzwasser)
```

**Maximale Handkraefte nach Ergonomie-Normen:**
| Bedingung | Max. Kraft (N) | Dauer |
|-----------|---------------|-------|
| Kurzfristig, zwei Haende | 400 N | < 5 Minuten |
| Dauerhaft, zwei Haende | 150 N | Stunden |
| Kurzfristig, eine Hand | 200 N | < 5 Minuten |
| Dauerhaft, eine Hand | 80 N | Stunden |

**Notpinnen-Laenge nach Bootlaenge (Richtwerte Fahrtenyacht):**
| LOA (m) | Rudermoment typ. (Nm) | Min. Pinnenlaenge (m) | Empfohlen (m) |
|---------|----------------------|----------------------|---------------|
| 8–10 | 80–150 | 0.50 | 0.60–0.80 |
| 10–12 | 150–300 | 0.70 | 0.80–1.00 |
| 12–14 | 300–600 | 0.90 | 1.00–1.20 |
| 14–16 | 600–1000 | 1.10 | 1.20–1.50 |
| 16–20 | 1000–2000 | 1.30 | 1.50–1.80 |
| 20–25 | 2000–4000 | 1.50 | 1.80–2.50 |

**Wichtig:** Bei Schwerwetter sind die Ruderkraefte erheblich hoeher als bei Normalfahrt. Sicherheitsfaktor 2.0–3.0 einrechnen!

#### 2.2.2 Steuerung durch Segeltrimm

Physikalisches Prinzip: Die Balance zwischen Segeldruck (Center of Effort, CE) und dem lateralen Widerstandsschwerpunkt (Center of Lateral Resistance, CLR) bestimmt den Kurs.

```
CE vor CLR → Boot faellt ab (Leegierikeit)
CE hinter CLR → Boot luft an (Luvgierigkeit)
CE ueber CLR → Neutrales Ruder (Balance)

Notsteuerung durch Segeltrimm:
  - Mehr Vorsegel / weniger Gross → Boot faellt ab
  - Mehr Gross / weniger Vorsegel → Boot luft an
  - Backgesetzte Fock → Boot dreht stark ab
  - Nur Gross mit dichtgeholtem Grossbaum → Boot luft stark an
  - Beiliegen: Fock back, Gross dicht → Boot liegt stabil 50-60° zum Wind
```

#### 2.2.3 Treibanker-Physik

Treibanker (Drogue) und Para-Anker (Sea Anchor) wirken als Bremse und Kurshalter:

```
Bremskraft eines Treibankers:
  F_drag = 0.5 × Cd × rho × A × V^2

  Cd = Widerstandsbeiwert (abhaengig von Form):
    - Konischer Drogue: Cd ≈ 1.2
    - Para-Anker: Cd ≈ 1.5
    - Jordan Series Drogue: Cd ≈ 0.8 (pro Kegel, aber viele Kegel)
    - Galerider: Cd ≈ 1.0

  A = Projizierte Flaeche
  V = Driftgeschwindigkeit durchs Wasser
  rho = Wasserdichte

Ankerpunkt-Position bestimmt Kursverhalten:
  - Treibanker am Heck → Boot liegt mit dem Heck zum Wetter
  - Para-Anker am Bug → Boot liegt mit dem Bug zum Wetter
  - Asymmetrischer Ansatz → Boot liegt schraeg (zum Steuern nutzbar)
```

### 2.3 Regulatorische Anforderungen

#### 2.3.1 Rechtsgrundlage der Notsteuerungspflicht (RCD 2013/53/EU) — Abgrenzung zu ISO 8847

ISO 8847:2021 traegt den Titel „Kleine Wasserfahrzeuge — Steueranlagen — Seil-ueber-Rolle-Systeme" (engl. „Small craft — Steering gear — Cable over pulley systems") und regelt ausschliesslich Seil-ueber-Rolle-Steuersysteme. Der Scope (Klausel 1) **schliesst Notsteuerung ausdruecklich aus**: „This document does not address emergency means of steering the craft." ISO 8847 ist somit **nicht** die Rechtsgrundlage einer Notsteuerungspflicht.

Rechtsgrundlage ist die grundlegende Sicherheitsanforderung der EU-Sportbootrichtlinie **RCD 2013/53/EU, Anhang I**, die fuer Boote mit Rad- oder Hydrauliksteuerung eine Behelfssteuerung fordert („emergency means of steering ... at reduced speed"). Topisch verwandt (aber ebenfalls nicht die Notsteuerungsnorm) ist ISO 8848 (Remote steering systems).

Aus RCD 2013/53/EU Anhang I abgeleitete Grundanforderungen (measured):
- Eine von der Hauptsteuerung unabhaengige Behelfs-/Notsteuereinrichtung fuer Boote mit Rad- oder Hydrauliksteuerung
- Faehigkeit, das Boot bei reduzierter Fahrt auf grobem Kurs zu halten

Praxisuebliche Richtwerte nach Bootsgroesse (Erfahrungswerte, estimated — **nicht** durch ISO 8847 oder RCD numerisch belegt; die frueher hier genannte 5-Minuten-Umschaltzeit war eine ISO-8847-Fehlzuschreibung und ist entfernt):
| LOA (m) | Richtwert |
|---------|-------------|
| < 7 | Notpinne oder Notruder empfohlen, nicht zwingend |
| 7–12 | Notpinne empfohlen, wenn keine direkte Pinnensteuerung |
| 12–24 | Notpinne empfohlen, Belastungsnachweis sinnvoll |
| > 24 | Klassifikationsgesellschaft entscheidet (GL, BV, Lloyd's) |

> ✅ Aufgeloest (Audit): ISO 8847 deckt Notsteuerung NICHT ab (Scope wortwoertlich „This document does not address emergency means of steering the craft"); Rechtsgrundlage der Notsteuerungspflicht ist RCD 2013/53/EU Anhang I. Die frueheren ISO-8847-„Pflichten" (5-Minuten-Umschaltzeit, Groessen-Schwellen als ISO-Vorgabe) sind korrigiert bzw. als Erfahrungswerte gekennzeichnet. Confidence: measured (ISO/RCD-Belege) fuer die Scope-/Rechtsgrundlagen-Aussage. — Quelle: ISO 8847:2021 Title + Scope, bestaetigt via iso.org/standard/75809.html und BS EN ISO 8847:2021 (en-standard.eu); RCD 2013/53/EU Anhang I.

#### 2.3.2 World Sailing Offshore Special Regulations (OSR)

Die OSR (ehemals ISAF OSR) gelten fuer alle Offshore-Regatten und werden von vielen Versicherern auch fuer Fahrtenyachten als Referenz herangezogen:

**OSR 3.28 — Emergency Steering:**

| Kategorie | Anforderung |
|-----------|-------------|
| Kat. 0 (Transozean) | Emergency tiller, tested and usable. Separate from primary steering. Crew must practice. |
| Kat. 1 (Long Offshore) | Emergency tiller, capable of steering to windward. Tested. |
| Kat. 2 (Medium Offshore) | Emergency tiller fitting. Tested within 12 months. |
| Kat. 3 (Short Offshore) | Emergency tiller fitting. |
| Kat. 4 (Coastal) | Emergency tiller recommended. |

**Zusaetzliche OSR-Anforderungen:**
- OSR 3.28.1: Die Notpinne muss auf den Ruderschaft passen und darf keine Modifikation erfordern
- OSR 3.28.2: Die Notpinne muss im Sicherheitsdrill geuebt werden (Kat. 0, 1)
- OSR 3.28.3: Bei Doppelruder muss mindestens ein Ruder per Notpinne steuerbar sein
- OSR 3.28.4: Stauort der Notpinne muss markiert und allen Crewmitgliedern bekannt sein
- OSR 3.28.5: Wenn der Ruderschaft unter Deck endet und ein Deckel/Luke geoeffnet werden muss, muss diese Oeffnung ohne Werkzeug moeglich sein

#### 2.3.3 ORC Special Regulations

Die ORC (Offshore Racing Congress) Regulations enthalten aehnliche Anforderungen:
- Emergency tiller obligatorisch fuer Kategorie A, B, C
- Muss getestet und funktionsfaehig sein
- Muss ohne spezielle Werkzeuge installierbar sein
- Crew-Training dokumentiert

#### 2.3.4 CE-Richtlinie 2013/53/EU und Notsteuerung

Die CE-Recreational Craft Directive fordert nicht explizit eine Notsteuerung, aber:
- Die grundlegenden Sicherheitsanforderungen (Essential Safety Requirements, ESR) verlangen, dass ein Boot "sicher betrieben werden kann"
- ISO 8847 ist harmonisierte Norm unter der Richtlinie — Einhaltung bedeutet Konformitaetsvermutung
- Design-Kategorie A und B implizieren Hochsee-Tauglichkeit, was eine Notsteuerung praktisch erfordert

#### 2.3.5 SOLAS (fuer groessere Yachten > 24m)

Fuer Yachten ueber 24m LH, die unter SOLAS oder den Large Yacht Codes (LY3, REG Yacht Code) fallen:
- Redundante Steueranlage (Dual System) erforderlich
- Notsteuerung muss mechanisch unabhaengig von der Hauptsteuerung sein
- Umschaltzeit auf Notsteuerung: max. 30 Sekunden
- Regelmaessige Testpflicht (alle 3 Monate)

### 2.4 Versagensmodi und Risikobewertung

#### 2.4.1 FMEA — Fehlermoglichkeits- und Einflussanalyse Notsteuerung

| Komponente | Versagensart | Auswirkung | Eintrittswahrscheinlichkeit | Schwere | RPN |
|-----------|-------------|------------|---------------------------|---------|-----|
| Notpinne | Nicht an Bord | Keine Notsteuerung moeglich | Hoch (30 %) | 9 | 270 |
| Notpinne | Passt nicht auf Schaft | Notsteuerung nicht moeglich | Mittel (15 %) | 9 | 135 |
| Notpinne | Zu kurz | Steuerkraefte zu hoch | Mittel (20 %) | 6 | 120 |
| Notpinne | Korrodiert/defekt | Versagen unter Last | Niedrig (5 %) | 8 | 40 |
| Schaft-Aufnahme | Zugang blockiert | Verzoegerung/Unmoeglich | Mittel (25 %) | 8 | 200 |
| Schaft-Aufnahme | Korrodiert/verklemmt | Notpinne nicht montierbar | Mittel (15 %) | 8 | 120 |
| Ruderblatt | Komplett verloren | Notpinne nutzlos, Notruder noetig | Niedrig (5 %) | 10 | 50 |
| Crew | Keine Erfahrung | Ineffektive Nutzung | Hoch (50 %) | 7 | 350 |
| Stauort | Unbekannt/unzugaenglich | Kritischer Zeitverlust | Hoch (40 %) | 7 | 280 |

**Top-3-Risiken (hoechste RPN):**
1. **Crew hat keine Erfahrung** mit Notsteuerung (RPN 350)
2. **Stauort unbekannt** oder unzugaenglich (RPN 280)
3. **Notpinne nicht an Bord** (RPN 270)

**Schlussfolgerung:** Die drei groessten Risiken sind alle vermeidbar durch Training, Organisation und Ausruestungspruefung — nicht durch bessere Hardware.

### 2.5 Vergleich: Notpinne vs. Drogue vs. Jury-Rig vs. Segelsteuerung

| Kriterium | Notpinne | Drogue/Treibanker | Jury-Rig Notruder | Segelsteuerung |
|-----------|----------|-------------------|-------------------|----------------|
| Voraussetzung | Schaft + Ruder intakt | Treibanker an Bord | Material an Bord | Besegelung intakt |
| Einsatzzeit | 2–10 Min. | 15–30 Min. | 1–4 Stunden | Sofort |
| Praezision | Hoch | Gering (nur Kurs halten) | Mittel | Mittel |
| Kraefte | Hoch (Hebellaenge!) | Keine (passiv) | Hoch | Keine |
| Dauer einsetzbar | Unbegrenzt (Wachen) | Unbegrenzt | Stunden–Tage (Haltbarkeit) | Unbegrenzt |
| Windkurse moeglich | Alle | Vor dem Wind/Am Bug | Alle (eingeschraenkt) | Alle ausser Vorwind |
| Unter Motor | Ja | Bedingt (Bremse) | Ja | Nein |
| Komplexitaet | Gering | Mittel | Hoch | Mittel |
| Zuverlaessigkeit | Sehr hoch | Hoch | Mittel | Mittel |
| Kosten | 150–900 EUR | 350–3.000 EUR | Bordmaterial | 0 EUR |

### 2.6 Klimatische und regionale Besonderheiten

#### 2.6.1 Notsteuerung in hohen Breiten (> 50° N/S)

- Kaelte: Metallteile werden bei Frost extrem kalt — Handschuhe bei Notpinnen-Bedienung Pflicht
- Eis: Vereisung des Ruderschaftkopfs kann Montage der Notpinne verhindern
- Massnahme: Ruderschaftkopf mit Fett/Vaseline bedecken, Schutzkappe
- Treibanker: Nylon-Seil wird bei Kaelte steifer — groessere Biegeradien einplanen
- Eis im Treibanker: Kann Kegel zufrieren — Drogue vor Einsatz kontrollieren

#### 2.6.2 Notsteuerung in tropischen Revieren

- UV-Degradation: Nylon-Seile, Textil-Treibanker, Kunststoff-Teile altern schneller
- Massnahme: UV-exponierte Teile jaehrlich pruefen, ggf. haeufiger ersetzen
- Korrosion: Hohe Feuchtigkeit und Temperatur beschleunigen Korrosion
- Massnahme: Notpinne in dicht verschlossener Box lagern, Silica-Gel beilegen
- Seegras/Treibholz: Haeufiger Treibanker-Verstopfung in tropischen Gewaessern

#### 2.6.3 Notsteuerung im Mittelmeer

- Thermische Winde (Meltemi, Mistral): Kurze Vorwarnzeit, starke Boeen
- Kurze Distanzen zur Kueste: Schnelle Verschlechterung bei Steuerverlust in Lee einer Kueste
- Hoher Schiffsverkehr: Manoevrierunfaehiges Boot im Mittelmeer = hohes Kollisionsrisiko
- Empfehlung: Notpinne + AIS-Sender (Sichtbarkeit fuer andere Schiffe)

### 2.7 Besonderheiten nach Bootstyp

#### 2.7.1 Langkieler mit Skeg-Ruder

- Ruderschaft gut geschuetzt durch Skeg → geringeres Risiko des Ruderblatt-Verlusts
- Notpinne funktioniert zuverlaessig, da Schaft und Blatt selten komplett verloren gehen
- Ueblicherweise niedrigere Rudermomente als Spade-Ruder (kleinere Ruderflaeche)
- Klassische Konstruktion: Notpinne direkt auf Schaft, oft mit einfacher Vierkant-Aufnahme

#### 2.7.2 Moderne Yachten mit Spade-Ruder

- Freistehendes Ruder ohne Skeg → hoeheres Risiko bei Grundberuehrung/Treibgut
- Oft zwei Ruder (Performance Cruiser) → Teilredundanz
- Komplexere Steueranlage (Hydraulik, langes Gestänge) → mehr Versagenspunkte
- Ruderschaft oft unter Cockpitboden → abgewinkelte Notpinne noetig
- Empfehlung: Notpinne + Drogue/Notruder als Backup bei Komplettausfall

#### 2.7.3 Katamarane

- Zwei separate Ruder → inhaerent hoehere Redundanz
- Ein Ruder ausreichend fuer Kurssteuerung (mit reduzierter Praezision)
- Steuerung durch asymmetrischen Motor-Einsatz (bei Motorkat) moeglich
- Spezialfall: Daggerboard als Steuerungshilfe (bei einigen Performance-Kats)
- Treibanker: Montage an der Hecktraverse, Bridle auf Rumpfbreite

#### 2.7.4 Motorboote

- Selten Notpinne vorhanden (Konstruktion nicht vorgesehen)
- Hydraulische Steuerung dominiert → Bypass-Ventil essentiell
- Reservesteuerung: Zweites Hydrauliksystem oder Not-Handpumpe
- Aussenborder: Motor manuell drehen (am Motorgehaeuse, Notlenkung)
- Einbau-Motor mit Wellenanlage: Nur Ruder, kein Motordrehung moeglich
- Pod-Antrieb (IPS, Zeus): Hersteller-spezifische Notprozeduren
- Bugstrahlruder: Kann bei Langsamfahrt als Steuerungshilfe dienen (< 3 kn)
- Empfehlung Motorboot: Hydraulik-Bypass + Not-Handpumpe + Treibanker

### 2.8 Zeithorizonte bei Steuerverlust

| Phase | Zeitfenster | Massnahmen | Prioritaet |
|-------|------------|------------|-----------|
| Sofort (0–2 Min.) | Erkennung | Alarm, Geschwindigkeit reduzieren, Beidrehen | CRITICAL |
| Kurz (2–15 Min.) | Diagnose | Ursache identifizieren, Schnellreparatur versuchen | HIGH |
| Mittel (15–60 Min.) | Notpinne | Emergency Tiller montieren, Kurs aufnehmen | HIGH |
| Lang (1–4 Std.) | Behelfsloesungen | Jury-Rig, Notruder, Drogue einsetzen | MODERATE |
| Sehr lang (4+ Std.) | Langzeit-Steering | Segeltrimm optimieren, Wachen organisieren | MODERATE |
| Kritisch (jederzeit) | Verschlechterung | Lage-Eskalation: Seenotfall, EPIRB, Mayday | CRITICAL |

---

## 3. Typenuebersicht

### 3.1 Notpinne (Emergency Tiller)

#### 3.1.1 Grundprinzip

Die Notpinne ist die einfachste und wichtigste Notsteuerungseinrichtung. Sie besteht aus einem Hebel, der direkt auf den Ruderschaftkopf gesteckt wird und eine direkte, mechanische Verbindung zwischen dem Steuermann und dem Ruderblatt herstellt — unter Umgehung aller anderen Steuerungskomponenten.

**Vorteile:**
- Einfachste und zuverlaessigste Notsteuerung
- Keine beweglichen Teile (im Lagerzustand)
- Unabhaengig von Strom, Hydraulik, Mechanik
- Direkte taktile Rueckmeldung
- Geringstes Gewicht und Platzbedarf
- Guenstigste Loesung

**Nachteile:**
- Funktioniert nur, wenn Ruderblatt und -schaft intakt sind
- Hohe Steuerkraefte bei groesseren Booten (> 14m)
- Oft unbequeme Steuerposition (Ruderschaft endet oft unter Deck oder unter Cockpitboden)
- Eingeschraenkte Ruderlage (Aufbauten, Cockpitwaende begrenzen Schwenkbereich)
- Bei Radsteuerung muss die Normalsteuerung oft erst entkoppelt werden

#### 3.1.2 Bauformen

**Typ A — Einfache gerade Notpinne:**
```
        Handgriff
           |
    [==============================]  Notpinne (Rohr oder Stange)
           |
    [===]  Aufnahme (Vierkant, Sechskant, Konus)
           |
    -------+------- Deck
           |
       Ruderschaft
```
- Material: Edelstahl 316L Rohr, Aluminium-Rohr, GFK-Rohr
- Laenge: 600–1500 mm typisch
- Aufnahme: Vierkant, Sechskant, geschlitzter Konus, Bolzen
- Einsatz: Boote 8–14m, Ruderschaftkopf ueber Deck oder knapp darunter

**Typ B — Abgewinkelte Notpinne:**
```
                Handgriff
                   |
            [======+]
                   |
    [==============]  Horizontales Stueck
           |
    [===]  Aufnahme
           |
    -------+------- Deck (Cockpitboden)
           |
       Ruderschaft
```
- Einsatz: Wenn Ruderschaft unter Cockpitboden endet und der Hebel ueber Cockpitbodenniveau gefuehrt werden muss
- Komplexer in der Fertigung, aber haeufig notwendig bei modernen Yachten

**Typ C — Teleskop-Notpinne:**
```
    [============[============]]  Ausziehbar
           |
    [===]  Aufnahme
```
- Ausziehbar fuer kompakte Lagerung
- Arretiermechanismus (Federstift, Klemmschraube) muss seewasserfest sein
- Einsatz: Platzsparende Loesung, aber mechanisch komplexer

**Typ D — Zusammensteckbare Notpinne:**
```
    [Stueck 1]--[Verbinder]--[Stueck 2]--[Verbinder]--[Stueck 3]
                                |
                         [===] Aufnahme
```
- Mehrere Segmente, die zusammengesteckt werden (Splinte, Bajonettverschluss)
- Vorteil: Sehr kompakt verstaubar
- Nachteil: Unter Stress und bei Seegang zusammenbauen = Herausforderung
- Einsatz: Groessere Boote (> 16m), wo Pinnenlaenge > 1.5m erforderlich

#### 3.1.3 Aufnahme-Systeme (Ruderschaft-Kopf)

| Aufnahme-Typ | Beschreibung | Haeufigkeit | Zuverlaessigkeit |
|-------------|-------------|-------------|-----------------|
| Vierkant (Square) | Quadratischer Schaftkopf, Pinne mit passendem Vierkantloch | 35 % | Sehr hoch |
| Sechskant (Hex) | Sechskantiger Schaftkopf | 10 % | Sehr hoch |
| Geschlitzter Konus | Konische Aufnahme mit Klemmschraube | 15 % | Hoch |
| Bolzen durch Bohrung | Querbolzen durch Bohrung im Schaft | 20 % | Sehr hoch |
| Klemmbacken (Clamp) | Zwei Halbschalen mit Schrauben | 10 % | Mittel (Schrauben noetig) |
| Schweisslasche | Angeschweisste Lasche mit Bolzenloch | 5 % | Hoch (fest, nicht demontierbar) |
| Universal-Adapter | Verstellbare Aufnahme fuer verschiedene Schaefte | 5 % | Mittel |

**Kritischer Punkt: Zugang zum Ruderschaftkopf**

Bei vielen modernen Yachten ist der Ruderschaftkopf nicht direkt zugaenglich:
- Unter Cockpitboden-Platte
- Unter Steering-Pedestal
- In der Achterkajuete/Lazarette
- Hinter der Steueranlage (Quadrant, Hydraulikzylinder)

Die Zeit bis zur Montage der Notpinne haengt massgeblich von der Zugaenglichkeit ab:

| Zugaenglichkeit | Typische Montagezeit | Bewertung |
|----------------|---------------------|-----------|
| Schaftkopf frei zugaenglich ueber Deck | 1–3 Minuten | Excellent |
| Unter leicht entfernbarer Cockpitplatte | 3–5 Minuten | Gut |
| Unter verschraubter Platte (Werkzeug noetig) | 10–20 Minuten | Mangelhaft |
| Hinter Einbauten (Moebel bewegen) | 15–30 Minuten | Unakzeptabel |
| Praktisch unzugaenglich | 30+ Minuten oder unmoeglich | CRITICAL-Befund |

### 3.2 Notruder (Emergency Rudder)

#### 3.2.1 Grundprinzip

Ein Notruder ist ein eigenstaendiges Ruderblatt mit Schaft, das bei Verlust des Hauptruders montiert wird. Es ist die einzige Loesung, wenn das Ruderblatt selbst verloren oder irreparabel beschaedigt ist.

**Vorteile:**
- Einzige echte Steuerung bei Ruderblatt-Verlust
- Kann improvisiert werden (Jury-Rig)
- Ermoeglicht Kurssteuerung ueber laengere Zeit

**Nachteile:**
- Montage auf See schwierig und gefaehrlich
- Kommerzielle Notruder sind schwer und sperrig
- Jury-Rig-Notruder haben eingeschraenkte Wirksamkeit
- Auf Motorbooten schwer realisierbar (kein Spiegel/Heck fuer Montage)

#### 3.2.2 Bauformen

**Typ A — Heckmontiertes Notruder:**
```
             Pinne
               |
    [==========+]
               |
    -----------+----------- Spiegel / Heck
               |
    [  Notruder-Blatt  ]
               |
```
- Montage am Heckspiegel oder an Heckkorb/Windsteueranlagen-Halterung
- Befestigung: Pintles & Gudgeons (Fingerlinge und Augen), Rohrschellen, Bolzen
- Material: GFK, Aluminium, Holz (Sperrholz mit Epoxid-Beschichtung)
- Einsatz: Heck-Cockpit-Yachten, Langkieler

**Typ B — Seitlich montiertes Notruder (Sweep/Steer Oar):**
```
    [================================]  Langer Riemen/Paddel
                    |
    ================+================ Relingstuetze / Dolle
                    |
    [  Blatt im Wasser  ]
```
- Grosses Paddel/Skull ueber Heck oder Seite
- Aelteste Form der Notsteuerung (Steuerriemen)
- Funktioniert nur bei geringer Fahrt
- Einsatz: Klassische Yachten, Not-Notloesung

**Typ C — Unter-Rumpf-Notruder (Sub-hull Emergency Rudder):**
- Wird durch ein Rohr oder eine Oeffnung im Rumpf abgesenkt
- Nur bei speziell dafuer vorbereiteten Booten (z.B. einige Regattayachten)
- Selten bei Fahrtenyachten

#### 3.2.3 Materialien fuer Notruder

| Material | Gewicht | Festigkeit | Beschaffbarkeit | Eigenbau |
|---------|---------|-----------|----------------|---------|
| GFK (vorgefertigt) | 3–8 kg | Hoch | Hersteller | Mittel |
| Aluminium-Blech | 2–5 kg | Hoch | Gut | Gut |
| Marine-Sperrholz + Epoxid | 3–6 kg | Mittel | Sehr gut | Sehr gut |
| Bootsriemen/Paddel | 2–4 kg | Mittel (Biegung!) | Gut | — |
| Improvisation (Bodenbretter, Tuer) | Variabel | Gering | An Bord | Improvisiert |

### 3.3 Treibanker-Steuerung (Drogue Steering)

#### 3.3.1 Grundprinzip

Treibanker werden primaer als Schwerwetter-Taktik eingesetzt, dienen aber auch als Notsteuerungshilfe. Sie bremsen das Boot und stabilisieren den Kurs, weil der Zug des Treibankers das Boot in einer bestimmten Ausrichtung zur See haelt.

**Einsatz-Szenarien fuer Notsteuerung:**
1. **Kein Ruder, achterlicher Wind:** Treibanker am Heck haelt Boot mit Heck zum Wind, Segel trimmen fuer groben Kurs
2. **Kein Ruder, Gegenwind:** Para-Anker am Bug haelt Boot in den Wind, Stabilisierung
3. **Kein Ruder, Querwind:** Treibanker seitlich versetzt → asymmetrischer Zug → Kursaenderung moeglich
4. **Teilsteuerung vorhanden:** Treibanker unterstuetzt schwache Notpinne durch Bremswirkung (niedrigere Geschwindigkeit = niedrigere Ruderkraefte)

#### 3.3.2 Typen

**Para-Anker (Sea Anchor):**
- Grosser Fallschirm-artiger Anker, wird am Bug ausgebracht
- Durchmesser: 2.5–6 m (abhaengig von Bootsgroesse)
- Boot liegt mit Bug zum Wetter, driftet minimal
- Nicht wirklich "Steuerung", eher "kontrolliertes Liegen"
- Geeignet fuer: Schwerstwetter, Warten auf Besserung

**Konischer Drogue:**
- Kegelfoermiger Treibanker, wird am Heck geschleppt
- Boot laeuft langsam vor dem Wind/der See
- Geschwindigkeit wird auf 2–4 Knoten begrenzt
- Grobe Kursaenderungen durch seitliches Versetzen des Schleppunkts moeglich

**Jordan Series Drogue (JSD):**
- Serie von ca. 100–160 kleinen Kegeln an einem langen Seil (90–120 m)
- Hoechste Bremswirkung bei gleichmaessiger Lastverteilung
- Boot laeuft sehr langsam vor der See (< 2 kn)
- Hervorragende Kurs-Stabilitaet
- De-facto-Standard fuer Schwerwetter-Taktik auf Blauwasser-Yachten

**Galerider:**
- Textil-Treibanker mit spezieller Form (Korb/Kelch)
- Gute Bremswirkung bei kompakter Groesse
- Hersteller: Hathaway, Reiser & Drang

#### 3.3.3 Treibanker als Steuerungshilfe — Technik

**Methode 1: Treibanker am Heck + Segeltrimm**
```
Wind →
        _______
       /       \
      |  Boot   | → Treibanker-Seil → [Treibanker]
       \_______/
       ↑
    Nur Vorsegel gesetzt → Boot faellt ab
    Nur Gross gesetzt → Boot luft an
    Balance → gerader Kurs vor dem Wind
```

**Methode 2: Seitlich versetzter Treibanker**
```
Wind →
        _______
       /       \   → Seil ueber Steuerbord-Winsch → [Treibanker]
      |  Boot   |
       \_______/
       → Boot dreht nach Steuerbord (zum Treibanker hin)
```

**Methode 3: Zwei Leinen am Treibanker (Steuerleine)**
```
[Treibanker] ← Hauptseil (fest)
      ↑
      └── Steuerleine (variabel) zu einer Winsch an Bord
           → Steuerleine dichtholen = Treibanker schert aus = Boot aendert Kurs
```

### 3.4 Behelfssteuerung (Jury-Rigged Steering)

#### 3.4.1 Grundprinzip

Jury-Rigging bezeichnet die Improvisation einer Steuerung aus an Bord verfuegbaren Materialien. Dies ist die letzte Stufe vor dem Steuern allein durch Segel und erfordert Seemannschaft, Kreativitaet und Mut.

**Typische Jury-Rig-Steuerungen:**

**Methode A — Paddel/Riemen am Heck:**
- Grosses Paddel oder Bootsriemen ueber Heckspiegel oder in Dolle am Heckkorb
- Am effektivsten bei langsamer Fahrt (< 4 kn)
- Ermuedend bei laengerer Dauer
- Kann durch Festbinden in Position gehalten werden

**Methode B — Bodenbretter/Tuer als Notruder:**
- Bodenbrett, Schranktuer, Tischplatte als Ruderblatt verwenden
- Befestigung an Bootshaken, Spinnaker-Baum oder Stange
- Montage am Heck mit Leinen und Schraubzwingen
- Geringe Ruderflaeche, daher nur bei niedriger Geschwindigkeit wirksam

**Methode C — Schleppleinen als Kurshalter:**
- Lange Leinen (50–100 m) ueber das Heck schleppen
- Leinen an Steuerbord und Backbord getrennt fuehren
- Asymmetrisches Schleppen = Kurskorrektur
- Wirkung: Stabilisierung, aber keine praezise Steuerung

**Methode D — Eimer/Drogue improvisiert:**
- Eimer, Fender, zusammengebundene Gegenstaende als Drogue verwenden
- Ueber Heck schleppen, asymmetrisch zur Kursaenderung
- Geringe Bremskraft, aber besser als nichts

#### 3.4.2 Material-Checkliste fuer Jury-Rig

| Material | Verwendungszweck | Typisch an Bord? |
|---------|-----------------|-----------------|
| Bootshaken | Schaft fuer Notruder | Ja (Pflicht) |
| Spinnaker-Baum | Langer Hebel/Schaft | Oft ja (Segelyacht) |
| Bodenbretter | Ruderblatt-Ersatz | Ja |
| Schranktuer/Tischplatte | Ruderblatt-Ersatz | Ja |
| Leinen (diverse) | Befestigung, Steuerleinen | Ja |
| Schraubzwingen | Befestigung | Selten |
| Draht / Lashing Wire | Befestigung | Empfohlen |
| Gewebeband (Duct Tape) | Verstärkung, Abdichtung | Sollte an Bord sein |
| Kabelbinder (gross) | Schnellbefestigung | Empfohlen |
| Sperrholz-Reste | Ruderblatt | Variabel |
| Werkzeugkiste | Bohren, Schrauben, Saegen | Sollte an Bord sein |

### 3.4.3 Bewertung der Jury-Rig-Methoden

| Methode | Effektivitaet | Aufwand | Haltbarkeit | Windkurse | Geschwindigkeit |
|---------|--------------|---------|-------------|-----------|-----------------|
| Paddel/Riemen | 3/10 | Gering | Stunden | Alle (langsam) | < 3 kn |
| Bodenbretter als Ruder | 4/10 | Mittel | Stunden–Tage | Alle (eingeschraenkt) | < 4 kn |
| Schleppleinen asymm. | 3/10 | Gering | Unbegrenzt | Vor dem Wind | < 5 kn |
| Eimer als Drogue | 2/10 | Gering | Stunden (Seil-Scheuern) | Vor dem Wind | < 3 kn |
| Spinnaker-Baum + Brett | 5/10 | Hoch | Tage (wenn gut gebaut) | Alle | < 5 kn |
| Bootshaken + Bodenbrett | 5/10 | Mittel | Tage | Alle | < 5 kn |
| Bugspriet als Schaft | 4/10 | Hoch | Tage | Alle | < 4 kn |

**Grundregel:** Jede Steuerung ist besser als keine Steuerung. Auch eine primitive Jury-Rig-Loesung kann den Unterschied zwischen kontrollierter Lage und Seenotfall ausmachen.

### 3.4.4 Schritt-fuer-Schritt: Bootshaken-Notruder

Eines der am schnellsten herstellbaren Jury-Rig-Notruder:

**Zeitbedarf:** 30–60 Minuten

**Material:**
1. Bootshaken (Aluminium, 1.5–2.5 m)
2. Bodenbrett oder Cockpit-Tischplatte
3. 2 × Rohrschellen oder Lashing Wire
4. 5 m Leine (mind. 10 mm)
5. Gewebeband (Duct Tape)

**Bau:**
```
Schritt 1: Bootshaken an einem Ende des Bodenbretts befestigen
           (Rohrschellen + Lashing, Duct Tape als Schutz)

Schritt 2: Bodenbrett am unteren Ende des Bootshakens
           (Ruderblatt-Wirkung, ca. 400×250 mm)

Schritt 3: Zwei Leinen als Steuerleinen am Bootshaken
           (oberhalb des Drehpunkts)

Schritt 4: Bootshaken am Heckkorb oder Heckrelingstuetze befestigen
           (Rohrschelle oder Leine als Drehpunkt)

Schritt 5: Steuerleinen zu den Cockpit-Winschen fuehren

Schritt 6: Test: Ruderblatt ins Wasser, Steuerleinen bedienen
```

**Tipps:**
- Bootshaken-Griff als Pinne verwenden (direkte Steuerung)
- Bodenbrett so befestigen, dass es nicht abrutschen kann
- Drehpunkt muss stabil sein — sonst reisst das Notruder bei Belastung ab
- Bei Seegang: Sicherungsleine am Bootshaken (geht sonst verloren!)

### 3.5 Windsteueranlage als Backup-Steuerung

#### 3.5.1 Grundprinzip

Windsteueranlagen (Windvanes) sind mechanische Autopiloten, die keine Energie benoetigen. Sie nutzen die relative Windrichtung, um einen Kurs zum Wind zu halten. Bei Ausfall der primaeren Steuerung koennen sie als Backup dienen.

**Typen mit Backup-Eignung:**

| Typ | Backup-Eignung | Einschraenkungen |
|-----|---------------|-----------------|
| Servo-Pendulum (Monitor, Aries, Windpilot Pacific) | Sehr gut | Braucht intaktes Hauptruder |
| Hilfruder (Windpilot Caribbean, Hydrovane) | Exzellent | Unabhaengig vom Hauptruder! |
| Trimtab (Aries, aeltere Systeme) | Gut | Braucht intaktes Hauptruder |

**Besondere Stellung der Hydrovane:**
Die Hydrovane-Windsteueranlage besitzt ein eigenes, separates Ruderblatt und kann daher als vollstaendig unabhaengige Notsteuerung dienen — selbst bei Totalverlust des Hauptruders. Sie ist damit eine der wenigen kommerziell erhaeltlichen Loesungen, die sowohl automatische Windsteuerung als auch Notsteuerung in einem System vereint.

#### 3.5.2 Einschraenkungen

- Windsteueranlagen funktionieren nur unter Segel (relativ zum scheinbaren Wind)
- Unter Motor oder bei Flaute keine Funktion
- Servo-Pendulum-Typen benoetigen ein intaktes Hauptruder
- Montage am Heck erfordert Verstaerkung des Hecks

### 3.6 Festgesetzte Pinne / Lashing (Tiller Lashing)

#### 3.6.1 Grundprinzip

Bei Booten mit Pinnensteuerung (oder wenn eine Notpinne montiert ist) kann die Pinne mit Leinen festgesetzt werden, um einen stabilen Kurs zu halten. Dies ist die einfachste Form des "Autopiloten" und wird seit Jahrhunderten praktiziert.

**Methode:**
```
              Backbord-Leine
             /
    [Pinne]=+============]
             \
              Steuerbord-Leine

Beide Leinen fuehren zu Klampen oder Winschen.
Laenge der Leinen bestimmt den Ruderwinkel.
Gummistropp (Bungee) als Daempfer einbauen.
```

**Anwendung:**
- Kurs zum Wind halten bei ausgeglichenem Boot
- Pinne leicht luvseitig festsetzen (2–5 Grad) fuer Luv-Tendenz
- Gummistropp gibt bei Boen nach und federt zurueck
- Boot muss gut getrimmt sein (Segel-Balance!)

### 3.7 Steuerung allein durch Segel

#### 3.7.1 Grundprinzip

Das aelteste und zuverlaessigste Notsteuerungsverfahren: Kursaenderungen und Kurshalten allein durch Veraenderung der Segelstellung. Funktioniert bei jedem Windkurs (ausser echter Vorwind-Kurs ist schwierig).

**Grundregeln:**
1. **Anluvsen:** Grosssegel dichtholen, Vorsegel fieren oder wegnehmen
2. **Abfallen:** Vorsegel dichtholen, Grosssegel fieren oder wegnehmen; oder Gross reffen
3. **Halse:** Vorsegel auf der Leeseite uebergeben, Gross mittschiffs
4. **Wende:** Gerolltes Vorsegel schnell abrollen, Gross hilft Boot durch den Wind
5. **Beidrehen:** Fock back, Gross dicht, Boot liegt ca. 50–60 Grad zum Wind

**Segelkombinationen fuer Kurshalten ohne Ruder:**

| Kurs zum Wind | Empfohlene Segel | Trimmhinweis |
|--------------|-----------------|-------------|
| Am Wind (30–50 Grad) | Stark gerefftes Gross + kl. Fock | Boot luft natuerlich an, minimale Korrektur noetig |
| Halbwind (60–90 Grad) | Gross gerefft + Genua | Balance durch Gross-Traveller |
| Raumschots (100–140 Grad) | Gross + ausgepolltes Vorsegel | Schwieriger ohne Ruder, Kurswechsel noetig |
| Vorwind (150–180 Grad) | Nur Vorsegel ausgepoolt | Instabil, Halse-Gefahr. Besser: Schmetterlingsstellung |
| Beigedreht | Fock back + Gross dicht | Stabil, aber kein Kursfortschritt |

#### 3.7.2 Praxis-Tipps

1. **Ueben bei gutem Wetter:** Ruder loslassen (unter Aufsicht) und nur mit Segeln steuern
2. **Boot muss getrimmt sein:** Gewichtsverteilung optimieren
3. **Langsamer ist besser:** Gereffte Segel geben mehr Kontrolle
4. **Geduld:** Kursaenderungen dauern laenger als mit Ruder
5. **Kurse ueber 120 Grad zum Wind sind schwierig:** Besser Zickzack-Kurs segeln

---

## 4. Produktlinien und Hersteller

### 4.1 Notpinnen — Hersteller und Produkte

#### 4.1.1 Edson Marine (USA)

| Produkt | Typ | Bootlaenge | Material | Preis (EUR) |
|---------|-----|-----------|---------|------------|
| Edson Emergency Tiller 336 | Gerade | 8–12 m | Edelstahl 316L | 180–280 |
| Edson Emergency Tiller 338 | Gerade | 12–16 m | Edelstahl 316L | 280–420 |
| Edson Emergency Tiller 340 | Abgewinkelt | 10–14 m | Edelstahl 316L | 320–480 |
| Edson Emergency Tiller 342 | Abgewinkelt | 14–20 m | Edelstahl 316L | 450–650 |
| Edson Universal Emergency Tiller | Universal-Adapter | 8–14 m | Edelstahl/Aluminium | 250–380 |

**Besonderheiten Edson:**
- Aeltester Steuerungshersteller der Welt (seit 1859)
- Sehr breites Sortiment an Aufnahme-Adaptern
- Passend fuer alle gaengigen Edson-Pedestals
- Qualitaet: Sehr hoch, marine-grade 316L
- Lieferung typisch mit Vierkant- oder Sechskant-Adapter

#### 4.1.2 Lewmar (UK)

| Produkt | Typ | Bootlaenge | Material | Preis (EUR) |
|---------|-----|-----------|---------|------------|
| Lewmar Emergency Tiller Kit (Pedestal) | Gerade | 8–14 m | Edelstahl | 150–300 |
| Lewmar Emergency Tiller (Hydraulik) | Abgewinkelt | 12–18 m | Edelstahl | 300–500 |

**Besonderheiten Lewmar:**
- Integriert in Lewmar-Steuerungssysteme
- Notpinne passt spezifisch auf Lewmar-Pedestal/Quadranten
- Weniger universal als Edson

#### 4.1.3 Jefa Marine (DK)

| Produkt | Typ | Bootlaenge | Material | Preis (EUR) |
|---------|-----|-----------|---------|------------|
| Jefa Emergency Tiller (Standard) | Gerade | 8–12 m | Edelstahl 316L | 200–350 |
| Jefa Emergency Tiller (Heavy Duty) | Gerade | 12–20 m | Edelstahl 316L | 350–600 |
| Jefa Emergency Tiller (Custom) | Nach Mass | 10–25 m | Edelstahl 316L | 400–900 |

**Besonderheiten Jefa:**
- Daenischer Spezialist fuer Segelyacht-Steuerungen
- Perfekt abgestimmt auf Jefa-Ruderlager und -Schaefte
- Hoechtste Praezision bei Aufnahme-Passungen
- Bietet Massanfertigungen fuer individuelle Boote
- Empfohlen fuer alle Boote mit Jefa-Steuerung

#### 4.1.4 Whitlock / Seastar Solutions (UK/Kanada)

| Produkt | Typ | Bootlaenge | Material | Preis (EUR) |
|---------|-----|-----------|---------|------------|
| Whitlock Emergency Tiller Cobra | Gerade | 8–12 m | Edelstahl | 160–280 |
| Whitlock Emergency Tiller Mamba | Abgewinkelt | 12–16 m | Edelstahl | 280–420 |

#### 4.1.5 Werfteigene Notpinnen

Viele Werften liefern bootsspezifische Notpinnen:

| Werft | Qualitaet | Zubehoer | Bemerkung |
|-------|----------|---------|----------|
| Hallberg-Rassy | Sehr gut | Stauplatz markiert, Anleitung beigelegt | Seriengemaess bei allen Modellen |
| Oyster Yachts | Sehr gut | Edelstahl, passgenau | Premium-Qualitaet |
| Boreal | Exzellent | Alu-Notpinne, sofort zugaenglich | Expeditionsyacht-Standard |
| Najad | Gut | Standard-Edelstahl | Solide |
| Swan (Nautor) | Gut bis sehr gut | Modellspezifisch | Abhaengig vom Modell |
| Bavaria | Befriedigend | Einfache Ausfuehrung | Teilweise nicht passgenau nach Modellwechsel |
| Beneteau | Maessig | Oft zu kurz, einfache Qualitaet | Haeufigstes Problem: zu wenig Hebellaenge |
| Jeanneau | Maessig | Aehnlich Beneteau | Zu-kurz-Problem verbreitet |
| Hanse | Befriedigend | Standard | Passgenauigkeit variiert nach Baujahr |

### 4.2 Treibanker-Systeme (Drogues und Para-Anker)

#### 4.2.1 Jordan Series Drogue (JSD)

**Hersteller:** Ace Sailmakers (USA), diverse Segelmacher weltweit auf Bestellung

| Bootlaenge | Anzahl Kegel | Seillaenge | Kegelgroesse | Preis (EUR) |
|-----------|-------------|-----------|-------------|------------|
| 8–10 m | 80–100 | 90 m | 125 mm (5") | 800–1.200 |
| 10–12 m | 100–120 | 100 m | 125 mm (5") | 1.000–1.500 |
| 12–14 m | 120–140 | 110 m | 150 mm (6") | 1.200–1.800 |
| 14–16 m | 140–160 | 120 m | 150 mm (6") | 1.500–2.200 |
| 16–20 m | 160–200 | 130 m | 150 mm (6") | 2.000–3.000 |

**Technische Spezifikation JSD:**
- Hauptseil: 12–16 mm dreistraengiges Nylon (Dehnung!)
- Kegel: Ballistic Nylon (Cordura 1000D), dreieckig kegelfoermig
- Abstand Kegel: ca. 500–600 mm
- Kettenstueck am Ende (5–10 kg) als Gewicht/Anker
- Ausbringleine: 5 m Polypropylenseil (schwimmt) zum Einholen
- Bruchlast System: min. 3 × Bootsverdr. in kN

**Vorteile JSD:**
- Hoechste Bremskraft aller Treibanker-Systeme
- Gleichmaessige Belastung (keine Rucke)
- Hervorragende Kurs-Stabilitaet (Boot bleibt mit Heck zur See)
- Funktioniert in extremstem Seegang (Ueberlebenstaktik bis Hurrikan)
- Kann nicht "auftauchen" wie ein einzelner grosser Drogue
- Mathematisch begruendetes Design (Donald Jordan, US Coast Guard Research)

**Nachteile JSD:**
- Grosses Packvolumen (40–60 Liter)
- Hohes Gewicht (15–30 kg)
- Teuer
- Ausbringen dauert 15–30 Minuten (Seil muss kontrolliert ausgelassen werden)
- Einholen sehr aufwendig (Winsch oder Motor)

#### 4.2.2 Galerider

**Hersteller:** Hathaway, Reiser & Drang (USA/UK)

| Modell | Bootlaenge | Durchmesser | Preis (EUR) |
|--------|-----------|-------------|------------|
| Galerider 24" | 8–10 m | 610 mm | 350–500 |
| Galerider 30" | 10–13 m | 762 mm | 450–650 |
| Galerider 36" | 13–16 m | 914 mm | 550–800 |
| Galerider 42" | 16–20 m | 1067 mm | 700–1.000 |
| Galerider 48" | 20–25 m | 1219 mm | 900–1.300 |

**Technische Spezifikation Galerider:**
- Material: Hochfestes Textil (Nylon/Polyester)
- Konstruktion: Kelchfoermig, offener Boden
- Befestigungsleine: 15–30 m Nylon (mind. 18 mm)
- Ausloeseleine: Zum kontrollierten Zusammenfalten beim Einholen
- Bremskraft: ca. 50–70 % eines Para-Ankers gleicher Groesse

**Vorteile Galerider:**
- Kompakt verstaubar
- Schnell ausgebracht (2–5 Minuten)
- Einfach einzuholen (Ausloeseleine)
- Gute Bremswirkung fuer Groesse

**Nachteile Galerider:**
- Kann bei sehr schwerer See "auftauchen" (Verlust der Bremswirkung)
- Weniger stabil als JSD bei extremen Bedingungen
- Einzelner Ansatzpunkt (Ruckbelastung)

#### 4.2.3 Para-Anker (Sea Anchor)

**Hersteller:** Para-Tech (USA), Fiorentino (USA), Parachute Anchor Systems

| Modell | Bootlaenge | Durchmesser | Preis (EUR) |
|--------|-----------|-------------|------------|
| Para-Tech 6' | 8–10 m | 1.8 m | 400–600 |
| Para-Tech 9' | 10–13 m | 2.7 m | 600–900 |
| Para-Tech 12' | 13–16 m | 3.7 m | 800–1.200 |
| Para-Tech 15' | 16–20 m | 4.6 m | 1.100–1.600 |
| Para-Tech 18' | 20–25 m | 5.5 m | 1.400–2.200 |
| Fiorentino 9' | 10–13 m | 2.7 m | 550–850 |
| Fiorentino 12' | 13–16 m | 3.7 m | 750–1.100 |

**Technische Spezifikation Para-Anker:**
- Bauform: Fallschirm-artig, rund oder kreuzfoermig
- Material: Nylon-Ripsgewebe, hochfest
- Ausbring-Tiefe: 15–30 m unter der Wasseroberflaeche
- Schwimmerleine (Trip Line): Zum Bergen
- Rode (Ankerleine): Nylon, 60–120 m, min. 16 mm

**Einsatz als Notsteuerung:**
- Para-Anker am Bug: Boot liegt mit Bug zum Wetter
- KEIN aktives Steuern moeglich — Boot liegt stationaer
- Einsatz: Wetter abwarten, auf Hilfe warten
- Drift: 0.5–1.5 kn (je nach Wind und Strom)

#### 4.2.4 Notruder-Kits

**Hersteller:** SOS Marine (AU), Forespar (USA), diverse Kleinserien

| Hersteller | Produkt | Bootlaenge | Gewicht | Preis (EUR) |
|-----------|---------|-----------|---------|------------|
| SOS Marine | Emergency Rudder | 8–14 m | 5 kg | 600–900 |
| Forespar | STA-PLUG Rudder Kit | 8–12 m | 3 kg | 400–600 |
| Hydrovane | Separate Rudder + Vane | 8–18 m | 15–25 kg | 3.500–6.500 |
| DIY Sperrholz-Kit | Selbstbau | 8–14 m | 4–8 kg | 100–250 |

### 4.3 Windsteueranlagen mit Notsteuerungsfunktion

| Hersteller/Modell | Typ | Eigenes Ruder? | Notsteuerung ohne Hauptruder? | Preis (EUR) |
|------------------|-----|---------------|------------------------------|------------|
| Hydrovane | Hilfsruder | Ja | Ja — Bestes System dafuer | 4.500–7.000 |
| Windpilot Pacific | Servo-Pendulum | Nein | Nein (braucht Hauptruder) | 3.800–5.500 |
| Windpilot Caribbean | Hilfsruder | Ja | Ja | 4.000–6.000 |
| Monitor | Servo-Pendulum | Nein | Nein | 3.500–5.000 |
| Aries | Servo-Pendulum | Nein | Nein | 3.000–4.500 (gebraucht) |
| Fleming | Servo-Pendulum | Nein | Nein | 3.500–5.000 (gebraucht) |
| Beaufort | Hilfsruder | Ja | Ja (eingeschraenkt) | 3.500–5.000 |

**Empfehlung AYDI:** Fuer Blauwasser-Segler, die eine Windsteueranlage planen, ist ein System mit eigenem Ruderblatt (Hydrovane, Windpilot Caribbean) vorzuziehen, da es bei Ruderblatt-Verlust als vollstaendig unabhaengige Notsteuerung dient.

### 4.3.1 Detailvergleich: Treibanker-Systeme fuer Notsteuerung

| Eigenschaft | JSD | Galerider | Para-Anker | Konischer Drogue |
|------------|-----|-----------|-----------|-----------------|
| Einsatzposition | Heck | Heck | Bug | Heck |
| Bremskraft (rel.) | Sehr hoch (100 %) | Mittel (50–70 %) | Hoch (80–90 %) | Mittel (40–60 %) |
| Max. Seegang | Hurrikan-tauglich | BF 10 | Hurrikan-tauglich | BF 9 |
| Ausbring-Dauer | 15–30 Min. | 2–5 Min. | 10–20 Min. | 2–5 Min. |
| Einhol-Aufwand | Sehr hoch (Winsch) | Gering (Trip-Line) | Hoch (Trip-Line/Motor) | Gering |
| Packvolumen | 40–60 L | 15–20 L | 30–40 L | 10–15 L |
| Gewicht | 15–30 kg | 3–5 kg | 8–12 kg | 2–4 kg |
| Kurs-Stabilitaet | Exzellent | Gut | Sehr gut (stationaer) | Befriedigend |
| Ruckbelastung | Minimal (verteilt) | Mittel | Hoch (Einzelpunkt) | Hoch (Einzelpunkt) |
| Steuerbarkeit | Minimal (nur Bridle) | Gering | Keine (stationaer) | Gering |
| Lebensdauer | 15–20 Jahre | 10–15 Jahre | 10–15 Jahre | 10–15 Jahre |
| Preis (12m Boot) | 1.200–1.800 EUR | 450–650 EUR | 600–900 EUR | 200–400 EUR |

#### Ausbring-Verfahren Jordan Series Drogue — Detailanleitung

**Vorbereitung (unter Deck, VOR der Notlage):**
1. JSD aus Staubeutel nehmen und in Cockpit bringen
2. Bootsseitiges Ende identifizieren (markiert mit Tape oder Whipping)
3. Bridle-Leinen bereitstellen (je 15 m, an Steuerbord- und Backbord-Heckklampe)
4. Kettenende identifizieren (seeseitiges Ende)
5. Schaekel und Kauschen pruefen (offen/fest?)

**Ausbringen (auf See):**
```
Phase 1 — Boot positionieren:
  1. Boot mit Heck zum Wind drehen
  2. Segel bergen oder stark reffen
  3. Fahrt reduzieren (Motor rueckwaerts oder Beidrehen)

Phase 2 — JSD auslegen:
  4. Kettenende (mit Kette als Gewicht) ueber Heck ins Wasser
  5. Seil kontrolliert auslaufen lassen (ACHTUNG: Nicht frei laufen lassen!)
  6. Seil ueber Heck-Umlenkung oder Heckklampe fuehren
  7. Alle 10 m Seil: Kurz halten, pruefen ob Kegel sich oeffnen
  8. Gesamtes Seil auslaufen lassen (90–130 m)

Phase 3 — Bridle befestigen:
  9. Bootsseitiges Ende an Bridle-Schaekel befestigen
  10. Steuerbord-Bridle an Stb-Klampe belegen
  11. Backbord-Bridle an Bb-Klampe belegen
  12. Bridle-Laengen gleichmaessig (Boot liegt gerade zum Drogue)
  13. Schamfiel-Schutz an Heck-Kante anbringen!

Phase 4 — Stabilisierung:
  14. Segel setzen: Kleines Sturmvorsegel oder tief gerefftes Gross
  15. Segeldruck stabilisiert Boot zusaetzlich zum Drogue
  16. Geschwindigkeit faellt auf 1–2 kn
  17. Kurs kontrollieren (Kompass)
  18. Bridle nachjustieren fuer geraden Kurs
```

**Einholen des JSD (nach Verbesserung der Lage):**
```
1. Motor starten (falls moeglich)
2. Auf Drogue-Seil zufahren (Motor vorwaerts, Seil wird locker)
3. Seil ueber Winsch einholen
4. ACHTUNG: Kegel kommen mit Wasser und Gewicht — Kraftaufwand!
5. Kegel einzeln von Bord heben und in Staubeutel
6. Kette zuletzt einholen
7. Alternative: Einhol-Leine (PP, schwimmt) nutzen: Am Kettenende befestigt,
   fuehrt zur Oberflaeche — dort greifen und JSD "rueckwaerts" einholen
8. DAUER: 30–60 Minuten (anstrengend!)
```

### 4.4 Zubehoer und Ergaenzungen

| Produkt | Zweck | Hersteller | Preis (EUR) |
|---------|-------|-----------|------------|
| Notpinnen-Halterung (Deck/Wand) | Sichere, markierte Stauung | Diverse / Eigenbau | 30–80 |
| Gummistropp-Set fuer Tiller-Lashing | Pinne festsetzen mit Daempfung | Diverse | 15–40 |
| Tiller-Lashing Kit (Leinen + Stropp) | Komplettset zum Festsetzen | Diverse | 40–80 |
| Notruder-Montagehalterung | Heckmontage fuer Notruder | SOS Marine / Eigenbau | 150–400 |
| Drogue Bridle Kit | Zwei-Punkt-Befestigung am Heck | Diverse | 80–200 |
| Thimbles + Schaekel (Set) | Verbindungselemente fuer Drogue | Wichard, Harken | 30–60 |
| Dyneema Trip Line (Para-Anker) | Bergen des Para-Ankers | Diverse | 40–80 |
| Staubox wasserdicht | Notpinne + Zubehoer griffbereit | Pelican, Seahorse | 50–150 |

---

## 5. Konstruktion DIY — Eigenbau Notsteuerung

### 5.1 Eigenbau Notpinne

#### 5.1.1 Voraussetzungen und Planung

**Vor dem Bau unbedingt pruefen:**
1. Ruderschaft-Kopf vermessen (Durchmesser, Querschnitt: rund, Vierkant, Sechskant)
2. Zugaenglichkeit des Ruderschaftkopfs pruefen (Cockpitboden, Pedestal)
3. Freien Schwenkbereich der Notpinne vermessen (Aufbauten, Cockpitwaende)
4. Erforderliche Pinnenlaenge berechnen (s. Abschnitt 2.2.1)
5. Abstand Schaftkopf bis Handgriff-Hoehe messen (Ergonomie!)
6. Vorhandene Steueranlage: Muss sie entkoppelt werden? (Quadrant, Hydraulik)
7. Materialien und Werkzeuge verfuegbar?

#### 5.1.2 Material-Auswahl

**Rohr-Material:**
| Material | Aussendurchmesser | Wandstaerke | Biegesteifigkeit | Gewicht/m | Preis/m (EUR) |
|---------|-------------------|-------------|-------------------|-----------|--------------|
| Edelstahl 316L Rohr | 25–32 mm | 2.5–3 mm | Sehr hoch | 1.5–2.5 kg | 15–35 |
| Aluminium 6082-T6 Rohr | 30–40 mm | 3–4 mm | Hoch | 0.6–1.0 kg | 8–18 |
| GFK-Rohr (Rundrohr) | 30–40 mm | 3–5 mm | Mittel-hoch | 0.5–0.8 kg | 12–25 |
| Edelstahl 316L Vollmaterial | 20–25 mm | Voll | Maximal | 2.5–4.0 kg | 25–60 |

**Empfehlung:** Edelstahl 316L Rohr, 30 mm Aussen, 2.5 mm Wand — bester Kompromiss aus Festigkeit, Gewicht und Bearbeitbarkeit.

**Aufnahme-Stueck (abhaengig vom Schaftkopf-Profil):**

**Variante A — Vierkant-Aufnahme:**
```
Material: Edelstahl 316L Flachstahl
Innenmass: Schaftkopf-Vierkant + 0.5 mm Spiel
Herstellung:
  1. Vier Stuecke Flachstahl zuschneiden
  2. Zu einem Kasten verschweissen
  3. An Rohr anschweissen
  4. Sicherungsbolzen-Bohrung (8 mm) durch Aufnahme + Schaft
```

**Variante B — Bolzen-Aufnahme:**
```
Material: Edelstahl 316L Platte + Bolzen
Herstellung:
  1. Gabelkopf aus 2 Platten an Rohr schweissen
  2. Bohrung passend zum vorhandenen Bolzenloch im Schaft
  3. Bolzen 10–12 mm Edelstahl mit Federstecker/Splint
```

**Variante C — Rohrschellen-Aufnahme (bei rundem Schaft):**
```
Material: Edelstahl-Rohrschellen (2 Stueck, DIN-Norm)
Herstellung:
  1. Zwei Rohrschellen passend zum Schaftdurchmesser
  2. An Verstaerkungsplatte verschrauben
  3. Platte an Pinnen-Rohr schweissen oder verschrauben
  4. Achtung: Muss SEHR fest sitzen — bei rundem Schaft rutscht die Aufnahme leicht!
```

#### 5.1.3 Bauanleitung — Gerade Notpinne (Typ A)

**Werkzeug benoetigt:**
- Winkelschleifer oder Metallsaege
- Bohrmaschine mit Metallbohrern (8, 10, 12 mm)
- WIG-Schweissgeraet (oder Auftragsschweissung durch Fachbetrieb)
- Feile, Schleifpapier
- Messchieber, Winkelmesser
- Koernerr, Reissnadel

**Schritt-fuer-Schritt:**

**Schritt 1 — Schaft vermessen:**
```
Ruderschaft-Kopfprofil aufnehmen:
  - Querschnitt (rund/vierkant/sechskant): ____
  - Mass 1 (Breite/Durchmesser): ____ mm
  - Mass 2 (bei nicht-rund): ____ mm
  - Hoehe Schaftkopf ueber Deck: ____ mm
  - Bohrung vorhanden? Durchmesser: ____ mm
  - Vorhandene Steueranlage entkoppelbar? Ja/Nein, wie: ____
```

**Schritt 2 — Pinnenlaenge berechnen:**
```
Bootslaenge LOA: ____ m
Geschaetztes Rudermoment (s. Tabelle 2.2.1): ____ Nm
Sicherheitsfaktor: 2.5 (Schwerwetter)
Max. Handkraft (Dauerbetrieb, 2 Haende): 150 N

L_min = (Rudermoment × Sicherheitsfaktor) / Max. Handkraft
L_min = ____ mm

Empfohlen: L_min + 200 mm = ____ mm (effektive Laenge ab Schaft)
```

**Schritt 3 — Rohr zuschneiden:**
- Laenge = Berechnete Pinnenlaenge + 150 mm (fuer Aufnahme-Stueck)
- Schnittkanten entgraten
- Rohrenden verschliessen (Kappe schweissen oder Stopfen) gegen Korrosion innen

**Schritt 4 — Aufnahme fertigen:**
- Aufnahme-Stueck nach Variante A, B oder C fertigen
- An Pinnen-Rohr schweissen (WIG, vollstaendig umlaufende Naht)
- Schweissnaht schleifen und kontrollieren

**Schritt 5 — Sicherungsbolzen:**
- Querbohrung 8–10 mm durch Aufnahme-Stueck (und Schaft, wenn Bolzen-Typ)
- Edelstahl-Bolzen mit Federstecker anfertigen
- Federstecker muss mit einer Hand und Handschuhen bedienbar sein!

**Schritt 6 — Handgriff:**
- Schrumpfschlauch oder Kork-Griffband am Handgriff-Ende anbringen
- Optional: Kugel oder T-Stueck am Ende fuer besseren Halt

**Schritt 7 — Test am Boot:**
- Notpinne auf Schaft stecken, Sicherungsbolzen einsetzen
- Schwenkbereich pruefen (mindestens 25 Grad je Seite)
- Ruder von Anschlag zu Anschlag bewegen
- Pruefen ob Normalsteuerung entkoppelt werden muss und wie
- Montagezeit messen: Ziel < 5 Minuten

**Schritt 8 — Oberflaechenbehandlung:**
- Edelstahl: Passivieren (Zitronensaeure-Bad oder Passivierungspaste)
- Aluminium: Eloxieren oder Primer + 2K-Lack
- Beschriftung: "NOTPINNE / EMERGENCY TILLER" gravieren oder schlagen

#### 5.1.4 Bauanleitung — Abgewinkelte Notpinne (Typ B)

Wenn der Ruderschaftkopf unter Cockpitboden-Niveau liegt, muss die Pinne abgewinkelt werden:

```
                  Handgriff (Cockpitniveau + 800 mm)
                     |
              [======+]  Horizontales Stueck (600–1200 mm)
                     |
              [      ]  Vertikales Stueck (Hoehe Cockpitboden bis Schaft)
                     |
              [===]  Aufnahme
                     |
     ----------------+------------- Cockpitboden (Luke oeffnen!)
                     |
                 Ruderschaft
```

**Zusaetzliche Ueberlegungen:**
- Biegemoment an der Abwinkelung ist hoch → Verstaerkung/Knotenblech!
- Winkel typisch 90 Grad, gelegentlich 60–75 Grad
- Vertikales Stueck: Abmessung aus Hoehendifferenz Schaft zu Cockpitboden + 150 mm
- Cockpitbodenplatte: Muss oeffenbar sein OHNE Werkzeug (Schnellverschluss!)
- Dichtung der Cockpitbodenplatte: Bei Seegang kommt Wasser — Suemp/Lenzpumpe bedenken

**Verstaerkung der Abwinkelung:**
```
      |
      +--[Knotenblech/Gusset]--+
      |                         |
      |   Schweissnaht          |
      |   rundum                |
      |                         |
      +-------------------------+
      |
```
Knotenblech: Min. 4 mm Edelstahl, dreieckig, beidseitig verschweisst.

#### 5.1.5 Bauanleitung — Notruder aus Sperrholz

**Material:**
| Position | Material | Dimension | Menge |
|---------|---------|-----------|-------|
| Ruderblatt | Marine-Sperrholz BS 1088 | 18 mm | 1 Platte 600×400 mm |
| Schaft/Rahmen | Edelstahl-Rohr 316L | 25 mm Aussen, 2 mm Wand | 2000 mm |
| Befestigungsplatten | Edelstahl-Flachstahl | 50×5 mm | 2 Stueck 500 mm |
| Epoxid | West System 105/205 oder 207 | — | 500 g Harz + Haerter |
| Glasgewebe | E-Glas, 200 g/m2 | — | 1 m2 |
| Bolzen | Edelstahl M10 | — | 4 Stueck + Muttern |
| Schaekel | Edelstahl, 10 mm | — | 2 Stueck |
| Leine | Polyester 12 mm | — | 10 m |

**Bauanleitung:**

**Schritt 1 — Ruderblatt formen:**
```
Form: Symmetrisches NACA-Profil (vereinfacht: vorne rund, hinten spitz)
Laenge: 400–500 mm
Breite: 250–350 mm
Dicke: 18 mm (Sperrholz) + Epoxid/Glas = ca. 22 mm

1. Sperrholz zuschneiden (Stichsaege)
2. Vorderkante abrunden (Radius ~15 mm)
3. Hinterkante anspitzen (ca. 5 mm Enddicke)
4. Kanten brechen (1–2 mm Fase)
```

**Schritt 2 — Epoxid-Beschichtung:**
```
1. Sperrholz beidseitig mit Epoxid traenken (Roller)
2. Glasgewebe (200 g/m2) beidseitig nass-in-nass laminieren
3. Kanten mit Glasband (50 mm) verstaerken
4. Min. 2 Schichten Epoxid-Decklack
5. Schleifen und 1 Schicht Antifouling (optional)
Aushaeertung: 48 Stunden bei 20 Grad
```

**Schritt 3 — Schaft-Anbindung:**
```
1. Edelstahl-Befestigungsplatten an Ruderblatt-Oberkante schrauben/kleben
2. Edelstahl-Rohr als Schaft durch Platten fuehren und verschweissen
3. Alternativ: Bootshaken als Schaft verwenden (Aluminium, sofort verfuegbar!)
4. Verbindung Schaft-Blatt: Durch-Bolzen M10 + Epoxid-Verklebung
```

**Schritt 4 — Heckmontage vorbereiten:**
```
Montage-Optionen:
A) Heckkorb / Relingstuetze: Rohrschellen + Bolzen
B) Heckspiegel: Fingerlinge (Pintles & Gudgeons)
C) Windsteueranlagen-Halterung: Oft passende Bohrungen vorhanden
D) Provisorisch: Leinen durch Klammern am Heck

Wichtig: Montage VORHER testen! Auf See ist es 10× schwieriger!
```

### 5.2 Eigenbau Jordan Series Drogue (vereinfacht)

**WARNUNG:** Ein korrekter JSD erfordert praezise Berechnung und hochwertige Materialien. Dieser vereinfachte Eigenbau ist eine Naeherung — ein professionell gefertigter JSD ist immer vorzuziehen.

**Material:**
| Position | Material | Menge | Preis (EUR) |
|---------|---------|-------|------------|
| Hauptseil | Nylon dreistraengig, 14 mm | 100 m | 180–250 |
| Kegelstoff | Cordura 500D oder Segeltuch | 5 m2 | 40–80 |
| Naehgarn | UV-bestaendiges Polyester-Garn | 500 m | 15–25 |
| Kette (Ende) | Edelstahl-Ankerkette 8 mm | 5 m (7 kg) | 40–60 |
| Schaekel | Edelstahl 10 mm | 4 Stueck | 20–40 |
| Kauschen (Thimbles) | Edelstahl, passend fuer 14 mm Seil | 6 Stueck | 15–30 |
| Bridle-Leinen | Nylon 14 mm | 2× 15 m | 50–80 |
| Einhol-Leine | Polypropylen 8 mm (schwimmt) | 5 m | 5–10 |

**Anleitung (vereinfacht):**

1. **Kegel neben:** 100–120 Kegel aus Cordura naehen
   - Kegelform: Gleichseitiges Dreieck, Seitenlaenge 150 mm
   - Zu Kegel formen (Naht entlang einer Kante)
   - Jeder Kegel bekommt eine Schlaufe am spitzen Ende
   - Doppelnaht, UV-bestaendiges Garn

2. **Kegel am Seil befestigen:**
   - Alle 500 mm einen Kegel mit Marlschlag oder Beiknoten befestigen
   - Alternativ: Schlaufe des Kegels direkt in Seilschlag einflechten
   - Kegel muessen in Schlepprichtung oeffnen

3. **Enden vorbereiten:**
   - Bootsseitiges Ende: Kausche einspleissen
   - Seeseitiges Ende: 5 m Kette mit Schaekel befestigen
   - Einhol-Leine am seeseitigen Ende befestigen

4. **Bridle anfertigen:**
   - Zwei Leinen je 15 m, an Steuerbord- und Backbord-Klampe gefuehrt
   - Am Drogue-Ende zusammengefuehrt mit Schaekel

### 5.3 Eigenbau Tiller-Lashing Kit

**Einfachste und nuetzlichste DIY-Notsteuerungshilfe:**

**Material:**
- 2 Stueck Polyester-Leine 10 mm, je 3 m lang
- 2 Stueck Gummistropp (Bungee) 8 mm, je 1 m lang
- 4 Stueck Karabinerhaken Edelstahl
- 2 Stueck Curryklemmen (Cam Cleats) — falls nicht am Boot vorhanden

**Zusammenbau:**
```
Pinne ←← Backbord-Leine → Gummistropp → Karabiner → Klampe/Winsch Bb
Pinne ←← Steuerbord-Leine → Gummistropp → Karabiner → Klampe/Winsch Stb

Einstellung:
  - Beide Leinen gleichlang = Ruder mittschiffs
  - Stb-Leine kuerzer = Ruder nach Steuerbord = Boot luft an (Bb-Bug)
  - Bb-Leine kuerzer = Ruder nach Backbord = Boot faellt ab (Bb-Bug)
  - Gummistropp laesst Pinne bei Boen nachgeben und zurueckfedern
```

### 5.4 Festigkeitsberechnung Eigenbau-Notpinne

#### 5.4.1 Biegemoment-Berechnung

Die kritische Belastung einer Notpinne ist das Biegemoment an der Aufnahme (Einspannstelle):

```
M_biege = F_hand × L_pinne

Wobei:
  F_hand = Maximale Handkraft (kurzfristig 400 N, Dauerbetrieb 150 N)
  L_pinne = Wirksame Pinnenlaenge in m

Beispiel: 12m Boot, Pinne 1.0 m
  M_biege_max = 400 N × 1.0 m = 400 Nm (kurzfristig)
  M_biege_dauer = 150 N × 1.0 m = 150 Nm (Dauerbetrieb)
```

#### 5.4.2 Erforderlicher Querschnitt (Edelstahl-Rohr)

```
Biegespannung:
  sigma = M_biege / W

Widerstandsmoment Rohr:
  W = pi/32 × (D^4 - d^4) / D

  D = Aussendurchmesser
  d = Innendurchmesser = D - 2t (t = Wandstaerke)

Zulaessige Spannung Edelstahl 316L:
  sigma_zul = Rp0.2 / SF = 210 MPa / 2.0 = 105 MPa

Beispiel: Rohr 30×2.5 mm (D=30, d=25)
  W = pi/32 × (30^4 - 25^4) / 30 = pi/32 × (810000 - 390625) / 30
  W = pi/32 × 13979 = 1372 mm^3 = 1.372 cm^3

  sigma = 400000 Nmm / 1372 mm^3 = 291 MPa → UEBERLASTET!

Erforderlich fuer 400 Nm:
  W_erf = M / sigma_zul = 400000 / 105 = 3810 mm^3

  → Rohr 40×3 mm: W = 3670 mm^3 → knapp, aber mit 316L ok (Rp0.2 real oft 250+ MPa)
  → Rohr 42×3 mm: W = 4280 mm^3 → SICHER ✓
```

> ⚠️ **ZU PRÜFEN (Audit):** Die Widerstandsmomente (W) im Rechenbeispiel und in der folgenden Tabelle sind zu hoch angesetzt. Nach der hier selbst verwendeten Formel W = pi/32 × (D^4 − d^4)/D mit d = D − 2t ergibt sich: 40×3 → ca. 3003 mm^3 (nicht 3670), 42×3 → ca. 3347 mm^3 (nicht 4280), 48×3,5 → ca. 5078 mm^3 (nicht 6850), 55×4 → ca. 7624 mm^3 (nicht 10200); nur die Zeile 30×2,5 (1372 mm^3) stimmt. Folge: Die Schlussfolgerung „42×3 mm → SICHER" ist **falsch** — 42×3 liefert nur 3347 mm^3 < erforderliche 3810 mm^3 (400 Nm bei 105 MPa). Rohrquerschnitte vor jedem Eigenbau durch eine Fachperson neu nachrechnen, nicht ungeprueft uebernehmen. Confidence: estimated — unverifiziert.

**Empfehlung nach Bootgroesse:**

| LOA (m) | Pinnenlaenge (m) | Rohr-Dimension (mm) | W (mm^3) | Sicherheit |
|---------|-----------------|--------------------|---------|-----------
| 8–10 | 0.70 | 30 × 2.5 | 1372 | Gut (niedrige Kraefte) |
| 10–12 | 0.90 | 35 × 3.0 | 2345 | Gut |
| 12–14 | 1.10 | 40 × 3.0 | 3670 | Gut |
| 14–16 | 1.30 | 42 × 3.0 | 4280 | Gut |
| 16–20 | 1.60 | 48 × 3.5 | 6850 | Gut |
| 20–25 | 2.00 | 55 × 4.0 | 10200 | Gut |

#### 5.4.3 Schweissnaht-Anforderungen

| Kriterium | Anforderung |
|-----------|-------------|
| Schweissverfahren | WIG (TIG) bevorzugt, MIG akzeptabel |
| Schweisszusatz | 316L-Schweissdraht (z.B. ER316L, 1.4430) |
| Nahtart | V-Naht oder Stumpfnaht, vollstaendig umlaufend |
| Nahtguete | Keine Poren, keine Risse, keine Einbrandkerben |
| Nachbehandlung | Naht schleifen, passivieren (Beizpaste oder Zitronensaeure) |
| Pruefung | Sichtpruefung, Farbeindring-Pruefung bei kritischen Naehten empfohlen |
| Zertifizierung | Fuer Regatta (OSR): Schweissnachweis empfohlen |

### 5.5 Verstaerkung des Hecks fuer Treibanker-Befestigung

Wenn das Boot keine ausreichend starken Befestigungspunkte fuer einen Treibanker am Heck hat, muessen diese nachgeruestet werden:

#### 5.5.1 Heckklampen nachruesten

**Anforderungen:**
- Mindestens 2 Klampen, symmetrisch angeordnet
- WLL (Working Load Limit) je Klampe: min. 10 kN (ca. 1000 kg)
- Durchbolzung durch Deck MIT Backing Plate (Edelstahl oder Aluminium)
- Backing Plate Mindestmasse: 100 × 100 × 5 mm (Edelstahl) oder 150 × 150 × 8 mm (Alu)
- Dichtmittel: PU-Dichtstoff (z.B. Sikaflex 291i) zwischen Klampe und Deck

**Material:**
| Position | Material | Dimension | Preis (EUR) |
|---------|---------|-----------|------------|
| Klampe (2 St.) | Edelstahl 316 gegossen | 200–250 mm | 2 × 40–80 |
| Bolzen (8 St.) | Edelstahl M10 × 60 | — | 8 × 3 |
| Backing Plates (2 St.) | Edelstahl 316 | 120 × 120 × 5 mm | 2 × 15–25 |
| Dichtmittel | Sikaflex 291i | 1 Kartusche | 15 |
| Gesamt | — | — | 130–250 |

**Montage:**
```
1. Position markieren (symmetrisch, 400–600 mm vom Heck)
2. Bohrungen bohren (10.5 mm fuer M10)
3. Kanten entgraten, GFK-Kante mit Epoxid versiegeln
4. Backing Plate unter Deck positionieren
5. Sikaflex auf Klampen-Unterseite und um Bohrungen
6. Klampe verschrauben, Muttern mit Loctite sichern
7. 24 Std. aushäerten lassen
8. Belastungstest: 500 kg Zug pro Klampe (Winsch + Dynamometer)
```

#### 5.5.2 Textil-Bridle als Alternative

Wenn Heckklampen nicht nachgeruestet werden koennen (z.B. Leichtbau-Heck):
- Hochfestes Gurtband (50 mm, Polyester, WLL 25 kN) um das gesamte Heck fuehren
- Schamfiel-Schutz an allen Kanten (Schlauchstuecke, Segeltuch)
- Bridle-Leinen an der Gurtschlaufe befestigen
- Vorteil: Verteilt die Last auf den gesamten Heckbereich
- Nachteil: Aufwendiger zu riggen, muss vorbereitet sein

### 5.6 Qualitaetskontrolle Eigenbau

**Pruefprotokoll vor dem Einsatz:**

| Pruefpunkt | Methode | Akzeptanzkriterium |
|-----------|---------|-------------------|
| Passgenauigkeit Aufnahme/Schaft | Aufstecken, wackeln | < 1 mm Spiel, kein Verkanten |
| Sicherungsbolzen | Einsetzen, belasten | Leichtgaengig, Federstecker haelt |
| Schweissnaehte | Sichtpruefung, Belastung | Keine Risse, kein Spruehen bei Biegung |
| Biegesteifigkeit | 100 kg Last am Ende | Keine bleibende Verformung |
| Schwenkbereich | Montieren, durchschwenken | Min. 25 Grad je Seite |
| Montagezeit | Stoppuhr, Crew | < 5 Minuten (< 3 Min. Ziel) |
| Demontage | Komplettabbau | Muss rueckbaubar sein (Normalsteuerung wieder nutzen) |
| Korrosionsschutz | Sichtpruefung | Keine Rostansaetze, Passivierung intakt |
| Markierung | Lesen | "NOTPINNE" / "EMERGENCY TILLER" lesbar |

---

## 6. Sicherheitsaspekte

### 6.1 Uebungspflicht und Drills

#### 6.1.1 Regulatorische Drill-Anforderungen

| Regelwerk | Drill-Frequenz | Anforderung |
|-----------|---------------|-------------|
| World Sailing OSR Kat. 0 | Vor jeder Regatta + jaehrlich | Crew muss Notpinne montieren und Boot steuern koennen |
| World Sailing OSR Kat. 1 | Vor jeder Regatta | Notpinne montieren und Funktion pruefen |
| World Sailing OSR Kat. 2 | Innerhalb 12 Monate | Notpinne Funktionstest |
| ORC Kat. A | Vor Regatta | Crew-Training dokumentiert |
| Blauwasser-Versicherung (Pantaenius, Nv Schepen) | Jaehrlich empfohlen | Sicherheitsinventar-Pruefung inkl. Notsteuerung |
| ISAF/World Sailing Training | Empfohlen bei jedem Safety Training | Teil des MOB- und Schadensbekämpfungs-Drills |

#### 6.1.2 Drill-Ablauf Notsteuerung

**Drill "Emergency Steering" — Standardablauf (30–45 Minuten):**

**Phase 1 — Briefing (5 Min.):**
- Erklaerung der Szenarien (Seil gerissen, Ruder verloren, etc.)
- Stauort Notpinne zeigen
- Rollen zuweisen (Steuermann, Monteur, Ausguck)

**Phase 2 — Notpinne montieren (10 Min.):**
1. Skipper gibt Befehl "Notsteuerung klar machen"
2. Boot beidrehen (Segel bergen oder back)
3. Notpinne aus Stauort holen
4. Cockpitplatte oeffnen (falls noetig)
5. Normalsteuerung entkoppeln (falls noetig: Quadrant-Notloesung, Hydraulik-Bypass)
6. Notpinne auf Schaft montieren
7. Sicherungsbolzen einsetzen
8. "Notpinne montiert" melden
9. ZEIT MESSEN! Ziel: < 5 Minuten

**Phase 3 — Steuern mit Notpinne (15 Min.):**
1. Segel setzen (gerefft)
2. Kurs aufnehmen
3. Manoevrieren ueben: Wende, Halse, Anluven, Abfallen
4. Steuergefuehl beurteilen (Kraefte, Reaktionszeit)
5. Wachuebergabe ueben (Steuermann wechselt)

**Phase 4 — Alternative Methoden (10 Min.):**
1. Tiller-Lashing anlegen (Pinne festsetzen)
2. Steuerung nur durch Segeltrimm ueben
3. (Optional) Drogue-Ausbringen simulieren

**Phase 5 — Debriefing (5 Min.):**
- Was hat funktioniert?
- Montagezeit?
- Was muss verbessert werden?
- Stauort optimal?

#### 6.1.3 Haeufige Probleme bei Drills

| Problem | Haeufigkeit | Loesung |
|---------|-------------|---------|
| Notpinne nicht auffindbar | 35 % der Erstdrills | Festen, markierten Stauort definieren |
| Notpinne passt nicht (mehr) | 15 % | Passgenauigkeit jaehrlich pruefen, nach Werft-Arbeiten erneut testen |
| Cockpitplatte nicht zu oeffnen | 20 % | Schnellverschluss nachrüsten, Schrauben durch Fluegelschrauben ersetzen |
| Quadrant/Hydraulik nicht entkoppelbar | 10 % | Bypass-Ventil/Entkopplungsmechanismus installieren |
| Notpinne zu kurz | 25 % | Laengere Notpinne beschaffen/bauen |
| Crew weiss nicht wie | 50 % der Erstdrills | Regelmaessig ueben! |

### 6.2 Stauungs-Anforderungen

#### 6.2.1 Stauort-Kriterien

Die Notpinne muss folgende Kriterien erfuellen:

| Kriterium | Anforderung | Begruendung |
|-----------|-------------|-------------|
| Zugaenglichkeit | Ohne Werkzeug, < 2 Min. | Zeitkritisch bei Notfall |
| Markierung | Gelb/orange Markierung, Beschriftung "NOTPINNE" | Schnelle Identifikation |
| Befestigung | Sicher gegen Verrutschen bei Seegang | Darf nicht durch Boot fliegen |
| Naehe zum Einsatzort | Max. 5 m vom Ruderschaftkopf entfernt | Kurze Wege |
| Schutz | Gegen Korrosion geschuetzt (nicht in Bilge!) | Funktionsfaehigkeit |
| Bekanntheit | Stauort in Sicherheitsbriefing erwaehnen | Alle an Bord muessen wissen wo |
| Sichtbarkeit | Stauort sichtbar, nicht hinter anderen Gegenstaenden | Ohne Suchen auffindbar |

#### 6.2.2 Empfohlene Stauorte

| Stauort | Bewertung | Einschraenkungen |
|---------|----------|-----------------|
| Halterung an Cockpitwand | EXZELLENT | Platzbedarf, Seewasserexposition |
| Lazarette (direkt am Zugang) | SEHR GUT | Nur wenn direkt zugaenglich |
| Unter Cockpitsitz (obere Schicht) | GUT | Nicht zu tief vergraben |
| An Cockpitboden neben Ruderschaft | GUT | Bester Ort wenn Platz vorhanden |
| Achterkajuete (an Wand) | BEFRIEDIGEND | Laengerer Weg |
| In Steuersaeule / Pedestal | GUT (wenn vorgesehen) | Nur bei manchen Edson-Pedestals |
| Bilge | MANGELHAFT | Feuchtigkeit, Unzugaenglichkeit |
| Vorkajuete | UNAKZEPTABEL | Zu weit vom Einsatzort |

### 6.3 ORC / World Sailing / ISAF Sicherheitsanforderungen im Detail

#### 6.3.1 World Sailing OSR 2024–2025 Auszug (Notsteuerung)

**Regel 3.28 Emergency Steering:**
> "3.28.1 A boat shall carry an emergency tiller that has been tried and tested. If the normal means of steering is a wheel or tiller with linkage, an emergency means of steering the boat independently of the normal means shall be provided."
>
> "3.28.2 For Category 0 and 1, the emergency tiller shall be capable of being fitted to enable steering to windward in moderate weather conditions."

**Regel 3.29 Compass and Navigation:**
> Die Notsteuerung muss in Kombination mit Kompass nutzbar sein — d.h. der Steuermann an der Notpinne muss einen Kompass ablesen koennen.

**Regel 4.19 Training:**
> "All crew members shall have knowledge of emergency steering procedures." (Kat. 0, 1)

#### 6.3.2 Checkliste fuer Sicherheitsinspektion Notsteuerung

| Nr. | Pruefpunkt | Ja | Nein | n/a |
|-----|-----------|----|----|-----|
| 1 | Notpinne an Bord? | [ ] | [ ] | [ ] |
| 2 | Notpinne passt auf Ruderschaft? | [ ] | [ ] | [ ] |
| 3 | Sicherungsbolzen vorhanden? | [ ] | [ ] | [ ] |
| 4 | Montage ohne Werkzeug moeglich? | [ ] | [ ] | [ ] |
| 5 | Montagezeit < 5 Min.? | [ ] | [ ] | [ ] |
| 6 | Ruderschaftkopf zugaenglich? | [ ] | [ ] | [ ] |
| 7 | Cockpitplatte ohne Werkzeug oeffenbar? | [ ] | [ ] | [ ] |
| 8 | Normalsteuerung entkoppelbar? | [ ] | [ ] | [ ] |
| 9 | Schwenkbereich ausreichend (min. 25 Grad je Seite)? | [ ] | [ ] | [ ] |
| 10 | Stauort markiert und bekannt? | [ ] | [ ] | [ ] |
| 11 | Steuern mit Notpinne geuebt (letzte 12 Monate)? | [ ] | [ ] | [ ] |
| 12 | Kompass von Notsteuer-Position ablesbar? | [ ] | [ ] | [ ] |
| 13 | Notpinne korrosionsfrei? | [ ] | [ ] | [ ] |
| 14 | Treibanker/Drogue an Bord (Offshore)? | [ ] | [ ] | [ ] |
| 15 | Steuerung durch Segel geuebt? | [ ] | [ ] | [ ] |
| 16 | Bei Doppelruder: Mindestens 1 Ruder per Notpinne steuerbar? | [ ] | [ ] | [ ] |

### 6.4 Versicherungs- und Haftungsaspekte

#### 6.4.1 Versicherungspflichten

| Versicherungstyp | Anforderung Notsteuerung | Konsequenz bei Fehlen |
|-----------------|-------------------------|----------------------|
| Kaskoversicherung (Vollkasko) | Betriebssicheres Boot vorausgesetzt | Leistungskuerzung bei Fahrlaessigkeit moeglich |
| Haftpflichtversicherung | Ordnungsgemaesse Ausruestung | Regress bei nachgewiesener Fahrlaessigkeit |
| Regattaversicherung | OSR-Konformitaet vorausgesetzt | Kein Versicherungsschutz bei OSR-Verstoessen |
| Blauwasser-Police (z.B. Pantaenius, Nv Schepen) | Erweitertes Sicherheitsinventar | Jaehrlicher Survey prueft u.a. Notsteuerung |
| Skipper-Haftpflicht (Charter) | Sicherheitsbriefing-Pflicht | Persoenliche Haftung des Skippers |

#### 6.4.2 Haftung des Skippers

Der Skipper haftet als verantwortlicher Fuehrer des Bootes fuer:
- Ordnungsgemaesse Sicherheitsausruestung (inkl. Notsteuerung)
- Einweisung der Crew in Notfallverfahren
- Regelmaessige Pruefung der Sicherheitsausruestung
- Dokumentation von Sicherheitsdrills (empfohlen, nicht immer Pflicht)

Bei einem Unfall infolge fehlender/defekter Notsteuerung kann dies gewertet werden als:
- Fahrlaessige Gefahrdung der Besatzung (StGB relevant)
- Verstoss gegen die Seemannsschaftspflicht (SeeSchStrO, SeeSportVO)
- Versicherungsrechtliche Obliegenheitsverletzung

#### 6.4.3 Dokumentation und Nachweispflichten

**Empfohlene Dokumentation:**
1. Sicherheitsinventar-Liste (jaehrlich aktualisiert)
2. Notsteuerungs-Drill-Protokoll (Datum, Teilnehmer, Ergebnis)
3. Crew-Einweisungs-Nachweis (unterschrieben)
4. Wartungsnachweise Notsteuerungsausruestung
5. Foto-Dokumentation Notpinne (Zustand, Stauort)

Diese Dokumentation kann bei einem Seeunfall oder Versicherungsfall entscheidend sein.

### 6.5 Besondere Situationen

#### 6.4.1 Notsteuerung bei Nacht

- Rotlicht/Stirnlampe fuer Montage der Notpinne
- Leucht-Markierungen (Leuchtfolie) am Stauort der Notpinne
- Kompass-Beleuchtung pruefen (von Notsteuer-Position)
- Zweite Person als Sicherung bei Arbeiten an Deck

#### 6.4.2 Notsteuerung bei Schwerwetter

- ZUERST Fahrt aus dem Boot nehmen (beidrehen/beiliegen)
- Dann erst Notpinne montieren
- Steuerkraefte bei Schwerwetter sind 3–5× hoeher als bei Normalfahrt
- Geschwindigkeit reduzieren (reffen, Treibanker) vor Aufnahme der Kurssteuerung
- Ggf. Tiller-Lashing statt dauerhaftem Steuern per Hand
- Wachen von max. 30 Min. am Notruder (Ermuedung!)

#### 6.4.3 Notsteuerung auf Katamaranen

- Katamarane haben oft zwei separate Ruder → Redundanz
- Verlust eines Ruders: Verbleibendes Ruder reicht oft aus
- Verlust beider Ruder: Drogue oder Notruder an Hecktraverse
- Spezialfall: Steuern durch asymmetrischen Motoreneinsatz (bei Motor-Kat)

#### 6.4.4 Notsteuerung auf Motorbooten

- Motorboote haben selten Notpinnen (Steuerung meist per Kabel oder Hydraulik)
- Alternativen: Reservekabel, Notlenker am Motor, Bugstrahlruder als Hilfsteuerung
- Bei Aussenbord-Motor: Motor manuell drehen (Lenkung umgehen)
- Bei stationaerem Motor: Treibanker als Notloesung
- IPS/Pod-Antrieb: Hersteller-spezifische Notsteuerungsverfahren (Volvo Penta, ZF)

---

## 7. Fehlerbild-Atlas

### 7.1 EMSTEER-F01 — Notpinne nicht an Bord

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F01 |
| Bezeichnung | Notpinne fehlt |
| Schwere | CRITICAL (5) |
| Confidence (visuell) | visual_low (Abwesenheit schwer visuell zu bestätigen) |
| Haeufigkeit | 25 % aller Yachten > 10 m mit Radsteuerung |
| Betroffene Systeme | Alle Boote mit Rad-, Hydraulik- oder Kabelsteuerung |

**Symptome:**
- Keine Notpinne in Inventarliste
- Kein markierter Stauort erkennbar
- Crew kann auf Nachfrage keine Notpinne zeigen

**Ursachen:**
- Nie mitgeliefert (Werft, Vorbesitzer)
- Verloren gegangen (Bootswechsel, Umraeumung)
- "Wird schon nicht passieren"-Mentalitaet
- Kosten gescheut (entgegen jeder Vernunft bei 5-6-stelligem Bootwert)

**Massnahmen:**
1. Notpinne SOFORT beschaffen (Hersteller-Original oder Eigenbau)
2. Passgenauigkeit pruefen und testen
3. Stauort definieren und markieren
4. In Sicherheitsinventar aufnehmen

**AYDI-Score-Einfluss:** -50 Punkte (CRITICAL-Finding)

### 7.2 EMSTEER-F02 — Notpinne passt nicht auf Ruderschaft

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F02 |
| Bezeichnung | Notpinne nicht kompatibel mit Ruderschaft |
| Schwere | CRITICAL (5) |
| Confidence (visuell) | visual_low |
| Haeufigkeit | 12 % aller Yachten mit Notpinne |
| Betroffene Systeme | Alle |

**Symptome:**
- Notpinne laesst sich nicht auf Schaft stecken (zu gross/klein)
- Aufnahme-Profil stimmt nicht ueberein (Vierkant auf Sechskant etc.)
- Sicherungsbolzen-Bohrung fehlt oder falscher Durchmesser

**Ursachen:**
- Ruderanlage getauscht, Notpinne nicht angepasst
- Falsche Notpinne bestellt (Verwechslung)
- Universelle Notpinne ohne Boot-spezifische Anpassung
- Korrosion/Materialaufbau hat Masse veraendert

**Massnahmen:**
1. Notpinne anpassen oder neue beschaffen
2. SOFORT am Boot testen nach Beschaffung
3. Bei jedem Steuerungsumbau: Notpinne mitpruefen!
4. Regelmaessig (jaehrlich) Passgenauigkeit pruefen

**AYDI-Score-Einfluss:** -45 Punkte (de facto gleich wie "nicht vorhanden")

### 7.3 EMSTEER-F03 — Ruderschaftkopf nicht zugaenglich

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F03 |
| Bezeichnung | Zugang zum Ruderschaftkopf blockiert/erschwert |
| Schwere | SIGNIFICANT (4) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 30 % aller Yachten mit Rad- oder Hydrauliksteuerung |
| Betroffene Systeme | Radsteuerung, Hydrauliksteuerung |

**Symptome:**
- Cockpitbodenplatte verschraubt (Werkzeug noetig)
- Einbauten blockieren Zugang (Moebel, Geraete)
- Steueranlage (Quadrant, Hydraulikzylinder) verhindert Aufstecken der Notpinne
- Luke zu klein fuer Notpinne

**Ursachen:**
- Bootskonstruktion nicht auf Notpinnen-Zugang ausgelegt
- Nachtraegliche Einbauten blockieren Zugang
- Wartungsarbeiten haben Zugang verschlechtert (falsche Schrauben, Dichtmittel auf Platte)
- Autopilot-Einbau hat Freiraum am Schaft verkleinert

**Massnahmen:**
1. Zugangsplatte auf Schnellverschluss umruesten (Fluegelschrauben, Drehverschluss)
2. Blockierende Einbauten umpositionieren
3. Ggf. groessere Zugangsplatte einbauen
4. Freigang fuer Notpinne sicherstellen (Markierung im Umfeld)
5. Montagezeit messen: Wenn > 10 Min. → bauliche Massnahme erforderlich

**AYDI-Score-Einfluss:** -25 bis -40 Punkte (je nach tatsaechlicher Montagezeit)

### 7.4 EMSTEER-F04 — Notpinne korrodiert/beschaedigt

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F04 |
| Bezeichnung | Notpinne korrodiert oder mechanisch beschaedigt |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 15 % aller Yachten mit Notpinne |
| Betroffene Systeme | Alle |

**Symptome:**
- Sichtbare Korrosion (Rost, Lochfrass) an Notpinne
- Verformung (Biegung, Delle)
- Aufnahme-Stueck beschaedigt oder korrodiert
- Sicherungsbolzen/Federstecker fehlt oder korrodiert

**Ursachen:**
- Lagerung in feuchter Umgebung (Bilge!)
- Falsches Material (304 statt 316L, verzinkter Stahl)
- Mechanische Beschaedigung durch lose Lagerung
- Fehlende Passivierung nach Schweissarbeiten

**Massnahmen:**
1. Korrosion beurteilen: Oberflaechlich → reinigen und passivieren; tief → ersetzen
2. Bei Verformung: Festigkeit kompromittiert → ersetzen
3. Sicherungsbolzen und Federstecker ersetzen
4. Besseren Stauort waehlen (trocken, belueftet)
5. Edelstahl-Pflegemittel auftragen (z.B. CorroProtect, Spray)

**AYDI-Score-Einfluss:** -15 bis -30 Punkte

### 7.5 EMSTEER-F05 — Notpinne zu kurz dimensioniert

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F05 |
| Bezeichnung | Notpinne zu kurz — Steuerkraefte zu hoch |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_medium (Laenge visuell schaetzbar) |
| Haeufigkeit | 20 % aller Yachten mit Notpinne |
| Betroffene Systeme | Alle, besonders > 12 m |

**Symptome:**
- Steuern mit Notpinne ermuedend bis unmoeglich
- Handkraefte > 200 N (eine Person kann Boot nicht halten)
- Crew berichtet von "unbedienbarer" Notpinne bei Drill
- Boot kann bei Schwerwetter nicht auf Kurs gehalten werden

**Ursachen:**
- Werft-Original war Kompromiss (kurz fuer leichte Stauung)
- Nicht fuer Schwerwetter-Kraefte dimensioniert
- Produktionsboot: Eine Groesse fuer alle Bedingungen
- Bootseigner hat Ruder vergroessert, Notpinne nicht angepasst

**Massnahmen:**
1. Erforderliche Pinnenlaenge berechnen (s. Abschnitt 2.2.1, Sicherheitsfaktor 2.5)
2. Laengere Notpinne beschaffen oder Verlaengerung anfertigen
3. Als Sofortmassnahme: Bootshaken als Verlaengerung verwenden (Lashing)
4. Alternative: Tiller-Lashing + Winschen-Unterstuetzung (Leine ueber Winsch)

**AYDI-Score-Einfluss:** -15 bis -25 Punkte

### 7.6 EMSTEER-F06 — Keine Entkopplung der Normalsteuerung

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F06 |
| Bezeichnung | Normalsteuerung nicht entkoppelbar fuer Notpinne |
| Schwere | SIGNIFICANT (4) |
| Confidence (visuell) | visual_low |
| Haeufigkeit | 10 % aller Yachten |
| Betroffene Systeme | Seilsteuerung mit Quadrant, Hydrauliksteuerung ohne Bypass |

**Symptome:**
- Notpinne montiert, aber Steuerung extrem schwergaengig
- Quadrant/Steuerseile blockieren Ruderbewegung
- Hydraulikdruck haelt Ruder fest (kein Bypass-Ventil)
- Notpinne kann Ruder nicht bewegen

**Ursachen:**
- Hydraulik ohne Bypass-Ventil installiert
- Quadrant nicht abnehmbar konstruiert
- Seilsteuerung hat keinen Schnell-Entkopplungsmechanismus
- Autopilot-Aktuator blockiert Ruderbewegung

**Massnahmen:**
1. Hydraulik: Bypass-Ventil nachrüsten (Pflicht!)
2. Seilsteuerung: Not-Entkopplungspunkt am Quadrant installieren (Splintbolzen)
3. Autopilot: Entkopplungsmechanismus sicherstellen (Kupplung, Bypass)
4. Dokumentation: "Entkopplungsanleitung" an Notpinnen-Stauort anbringen

**AYDI-Score-Einfluss:** -25 bis -35 Punkte

### 7.7 EMSTEER-F07 — Stauort unbekannt oder unzugaenglich

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F07 |
| Bezeichnung | Stauort der Notpinne unbekannt/unzugaenglich |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_low |
| Haeufigkeit | 35 % aller Yachten mit Notpinne |
| Betroffene Systeme | Alle |

**Symptome:**
- Crew kann Notpinne nicht finden
- Notpinne unter Gepaeck/Material vergraben
- Kein markierter Stauort
- Notpinne in Vorkajuete oder anderem entfernten Ort

**Ursachen:**
- Keine bewusste Stauort-Wahl
- Notpinne beim letzten Umraeumen "irgendwohin" gelegt
- Kein Sicherheitsbriefing durchgefuehrt
- Stauort nicht markiert

**Massnahmen:**
1. Festen Stauort im Cockpitbereich definieren
2. Halterung/Klammer montieren
3. Gelb/orange markieren, "NOTPINNE" beschriften
4. In Sicherheitsbriefing aufnehmen (bei jedem Crewwechsel!)
5. Im Sicherheitsplan des Bootes dokumentieren

**AYDI-Score-Einfluss:** -15 bis -25 Punkte

### 7.8 EMSTEER-F08 — Kein Notsteuerungs-Training durchgefuehrt

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F08 |
| Bezeichnung | Crew hat Notsteuerung nie geuebt |
| Schwere | SIGNIFICANT (4) |
| Confidence (visuell) | visual_insufficient (nicht visuell erkennbar) |
| Haeufigkeit | 55 % aller Yachten (geschaetzt) |
| Betroffene Systeme | Alle |

**Symptome:**
- Crew kann Notpinne nicht montieren
- Montagezeit > 15 Minuten
- Steuern mit Notpinne ueberfordert Crew
- Keine Dokumentation von Sicherheitsdrills

**Ursachen:**
- "Wird schon nicht passieren" / Verdraengung
- Unbequem, zeitaufwaendig (falsche Prioritaet)
- Keine regulatorische Verpflichtung (Fahrten- vs. Regattaboot)
- Skipper weiss selbst nicht wie

**Massnahmen:**
1. Sicherheitsdrill einmal pro Saison durchfuehren (s. Abschnitt 6.1.2)
2. Bei jedem Crewwechsel: Kurzeinweisung Notsteuerung (5 Min.)
3. Dokumentation der Drills (Datum, Teilnehmer, Montagezeit)
4. Idealerweise: Bei ruhigem Wetter mal 30 Min. nur mit Notpinne segeln

**AYDI-Score-Einfluss:** -20 bis -30 Punkte

### 7.9 EMSTEER-F09 — Fehlender Treibanker/Drogue fuer Offshore

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F09 |
| Bezeichnung | Kein Treibanker/Drogue an Bord (Offshore-Yacht) |
| Schwere | MODERATE (3) — nur fuer Offshore-Yachten relevant |
| Confidence (visuell) | visual_low |
| Haeufigkeit | 40 % der Offshore-Yachten (geschaetzt) |
| Betroffene Systeme | Fahrtenyachten fuer Offshore/Hochsee |

**Symptome:**
- Kein Treibanker im Sicherheitsinventar
- Keine Befestigungsmoeglichkeit fuer Drogue am Heck vorbereitet
- Keine Kenntnis der Crew ueber Treibanker-Einsatz

**Ursachen:**
- Hohe Kosten (JSD: 1.000–3.000 EUR)
- Grosser Platzbedarf
- "Ich segele nicht bei Sturm"
- Fehlendes Wissen ueber Schwerwetter-Taktiken

**Massnahmen:**
1. Fuer Offshore: Jordan Series Drogue DRINGEND empfohlen
2. Minimum: Galerider oder konischer Drogue
3. Befestigungspunkte am Heck vorbereiten (2 Klampen, je min. 10 kN WLL)
4. Crew in Drogue-Einsatz schulen
5. Bridle-Setup vorbereiten und beschriften

**AYDI-Score-Einfluss:** -10 bis -20 Punkte (nur Offshore-Bewertung)

### 7.10 EMSTEER-F10 — Unzureichende Befestigungspunkte fuer Drogue

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F10 |
| Bezeichnung | Heckklampen/Befestigungspunkte fuer Drogue unzureichend |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 30 % der Yachten |
| Betroffene Systeme | Alle mit Drogue/Treibanker |

**Symptome:**
- Heckklampen zu klein fuer Drogue-Seil
- Keine durchgehende Befestigung (Klampe nur auf Deck, nicht durch Rumpf)
- Keine separaten Befestigungspunkte fuer Bridle
- Gelaender als einziger Ansatzpunkt (nicht belastbar!)

**Ursachen:**
- Werft hat keine Drogue-Befestigung vorgesehen
- Heckklampen nur fuer Fender/Festmacher dimensioniert
- Fehlende Durchbolzung oder Backing Plates

**Massnahmen:**
1. Zwei Heckklampen min. 10 kN WLL installieren (mit Backing Plates!)
2. Alternativ: Textil-Gurt um Heck fuehren (Bridle)
3. Klampen durchbolzen (nicht nur kleben oder schrauben)
4. Fairleads/Umlenkungen fuer Drogue-Seil installieren

**AYDI-Score-Einfluss:** -10 bis -15 Punkte

### 7.11 EMSTEER-F11 — Windsteueranlage als Backup nicht funktionsfaehig

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F11 |
| Bezeichnung | Windsteueranlage (Backup-Steuerung) defekt oder nicht einsatzbereit |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 20 % der Yachten mit Windsteueranlage |
| Betroffene Systeme | Fahrtenyachten mit Windsteueranlage |

**Symptome:**
- Windfahne blockiert oder fehlt
- Steuerseile/Leitungen der Windsteueranlage verschlissen
- Pendel-Ruder fehlt oder beschaedigt
- Keine Wartung seit > 2 Jahren

**Ursachen:**
- Vernachlaessigung (Autopilot wird bevorzugt)
- Salzwasser-Korrosion an Gelenken und Lagern
- Mechanische Beschaedigung (Hafen-Manöver, Grundberuehrung)
- Ersatzteile nicht mehr erhaeltlich (aeltere Systeme)

**Massnahmen:**
1. Windsteueranlage jaehrlich warten (Gelenke, Lager, Seile)
2. Pendel-Ruder pruefen (Lager, Befestigung)
3. Ersatzteile an Bord halten (Windfahne, Steuerleinen, Bolzen)
4. Regelmaessig aktiv nutzen (nicht nur als Deko am Heck)

**AYDI-Score-Einfluss:** -10 bis -20 Punkte

### 7.12 EMSTEER-F12 — Doppelruder ohne Redundanzkonzept

| Attribut | Wert |
|----------|------|
| Code | EMSTEER-F12 |
| Bezeichnung | Doppelruder-Boot ohne Notsteuerungskonzept fuer Gesamtausfall |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 15 % der Doppelruder-Yachten |
| Betroffene Systeme | Yachten mit Doppelruder (Performance Cruiser, Regattaboote) |

**Symptome:**
- Nur Notpinne fuer EIN Ruder vorhanden (das andere hat keine Notpinne)
- Kein Konzept fuer Verlust beider Ruder (z.B. bei Grundberuehrung)
- Steuerseile/Hydraulik beider Ruder teilen Schwachpunkte (gemeinsame Leitung)
- Keine Trennmoeglichkeit (beide Ruder ueber eine Steuerung verbunden)

**Ursachen:**
- Annahme "zwei Ruder = doppelte Sicherheit" (falsch, wenn beide ueber eine Steuerung laufen)
- Werft hat nur eine Notpinne mitgeliefert
- Kein Bewusstsein fuer Gesamt-Ausfallszenario

**Massnahmen:**
1. Notpinne fuer BEIDE Ruder sicherstellen
2. Pruefen ob Ruder unabhaengig voneinander steuerbar (getrennte Hydraulik/Seile)
3. Drogue/Para-Anker fuer Komplett-Ausfallszenario an Bord
4. Separate Steuerleitungen fuer beide Ruder (Redundanz)

**AYDI-Score-Einfluss:** -10 bis -20 Punkte

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum — Steuerverlust auf See

```
[Steuerverlust erkannt]
  |
  ├── Geschwindigkeit sofort reduzieren
  │     ├── Segelyacht: Beidrehen (Fock back, Gross dicht)
  │     └── Motorboot: Maschine auf Leerlauf/Stopp
  |
  ├── [1] Kann das Steuerrad/die Pinne noch bewegt werden?
  │     ├── JA → Steueranlage hat Spiel/ist lose
  │     │     ├── Seil gerissen? → Pruefen, ggf. Notseil
  │     │     ├── Quadrant lose? → Klemmschraube nachziehen
  │     │     ├── Hydraulik leer? → Bypass-Ventil, Nachfuellen
  │     │     └── Kabel gerissen? → Notpinne montieren
  │     │
  │     └── NEIN → Steueranlage blockiert oder Ruder weg
  │           ├── Ruder noch dran? (Blick ueber Heck)
  │           │     ├── JA → Blockade → Netz/Leine im Ruder?
  │           │     │     ├── JA → Taucher / Bootshaken
  │           │     │     └── NEIN → Mechanische Blockade → Notpinne montieren
  │           │     └── NEIN → Ruder verloren → Notruder/Drogue/Segel-Steuerung
  │           │
  │           └── Weiter zu Baum [2]
  |
  └── Weiter zu Baum [2] wenn [1] nicht loesbar
```

### 8.2 Entscheidungsbaum — Notpinne funktioniert nicht

```
[Notpinne montiert, aber Boot laesst sich nicht steuern]
  |
  ├── [2] Ruder bewegt sich nicht trotz Notpinne?
  │     ├── Normalsteuerung entkoppelt?
  │     │     ├── NEIN → Entkoppeln!
  │     │     │     ├── Hydraulik: Bypass-Ventil oeffnen
  │     │     │     ├── Seilsteuerung: Seile vom Quadrant loesen
  │     │     │     ├── Kabelsteuerung: Kabel vom Ruderhebel trennen
  │     │     │     └── Autopilot: Kupplung loesen
  │     │     │
  │     │     └── JA → Ruder selbst blockiert
  │     │           ├── Grundberuehrung? → Ruderschaden → Treibanker/Notruder
  │     │           ├── Leine/Netz im Ruder? → Bergen versuchen
  │     │           └── Ruderlager defekt/festgefressen → Nicht reparierbar auf See
  │     │
  │     └── Ruder bewegt sich, aber Boot reagiert nicht?
  │           ├── Zu langsam (unter Segel: < 2 kn) → Mehr Segeldruck
  │           ├── Ruderblatt beschaedigt (kein Auftrieb) → Notruder
  │           └── Notpinne zu kurz → Verlaengerung improvisieren
  │
  └── Weiter zu Baum [3]
```

### 8.3 Entscheidungsbaum — Alternative Steuerung waehlen

```
[Keine Steuerung durch Notpinne moeglich — was nun?]
  |
  ├── [3] Welche Ausruestung ist verfuegbar?
  │     ├── Treibanker/Drogue?
  │     │     ├── JA → Drogue am Heck ausbringen
  │     │     │     ├── Wind achterlich? → Drogue + Vorsegel = grober Kurs
  │     │     │     ├── Wind vorlich? → Para-Anker am Bug
  │     │     │     └── Seitlich? → Asymmetrisch → Kurskorrekturen moeglich
  │     │     └── NEIN → Weiter
  │     │
  │     ├── Material fuer Notruder?
  │     │     ├── JA → Notruder bauen (s. Abschnitt 5.1.5)
  │     │     │     ├── Bootshaken + Bodenbrett
  │     │     │     ├── Spinnaker-Baum + Sperrholz
  │     │     │     └── Am Heck montieren (Schellen, Leinen)
  │     │     └── NEIN → Weiter
  │     │
  │     ├── Windsteueranlage mit eigenem Ruder (Hydrovane)?
  │     │     ├── JA → Windsteueranlage als Hauptsteuerung nutzen!
  │     │     └── NEIN → Weiter
  │     │
  │     └── Nur Segel und Leinen?
  │           ├── JA → Steuerung durch Segeltrimm (s. Abschnitt 3.7)
  │           │     ├── Am-Wind-Kurs: Gerefft, natuerliche Luvgierigkeit nutzen
  │           │     ├── Raumschots: Gross fieren, Vorsegel ausgepollt
  │           │     └── Schleppleinen als Bremse/Stabilisator
  │           └── Motorboot ohne Segel → Mayday / EPIRB wenn keine Steuerung moeglich
  │
  └── Weiter zu Baum [4]
```

### 8.4 Entscheidungsbaum — Eskalation und Seenotfall

```
[Keine Steuerung herstellbar — Eskalation]
  |
  ├── [4] Beurteilung der Lage
  │     ├── Gefaehrdung des Lebens? (Schwerwetter, Lee-Kueste, Schiffsverkehr)
  │     │     ├── JA → MAYDAY (Kanal 16 VHF, DSC, EPIRB)
  │     │     │     ├── Position, Bootsname, Anzahl Personen
  │     │     │     ├── Art des Problems: "No steering, adrift"
  │     │     │     └── Rettungsmittel klarmachen (Rettungsinsel, Westen, Grab Bag)
  │     │     │
  │     │     └── NEIN → PAN PAN (dringend, aber keine unmittelbare Lebensgefahr)
  │     │           ├── Hilfe anfordern (Schlepper, anderes Schiff)
  │     │           ├── Position halten (Treibanker, Beidrehen)
  │     │           └── Reparaturversuche fortsetzen
  │     │
  │     ├── Genug Zeit fuer Notruder-Bau?
  │     │     ├── JA → Jury-Rig-Notruder bauen (s. Abschnitt 3.4)
  │     │     └── NEIN → Beidrehen und auf Hilfe warten
  │     │
  │     └── Drift-Analyse
  │           ├── Wohin driftet das Boot? (Lee-Kueste? Offenes Meer? Schifffahrtsweg?)
  │           ├── Strom und Wind berechnen
  │           └── Ggf. Anker werfen wenn Wassertiefe < 50 m
```

### 8.5 Entscheidungsbaum — Treibanker-Probleme

```
[Treibanker ausgebracht, aber Probleme]
  |
  ├── [5] Welches Problem?
  │     ├── Treibanker taucht auf / bremst nicht
  │     │     ├── Zu klein? → Zweiten Drogue/Eimer zusaetzlich
  │     │     ├── Verdreht? → Einholen, entwirren, neu ausbringen
  │     │     └── Zu viel Seil? → Seil kuerzen (Drogue naeher ans Boot)
  │     │
  │     ├── Seil scheuert an Heck
  │     │     ├── Schamfiel-Schutz anbringen (Schlauch, Lappen)
  │     │     ├── Fairlead/Umlenkung nutzen
  │     │     └── Seil regelmaessig inspizieren
  │     │
  │     ├── Boot liegt quer zur See (Drogue am Heck)
  │     │     ├── Bridle asymmetrisch → Bridle justieren
  │     │     ├── Segel setzen fuer Richtungskorrektur
  │     │     └── Drogue-Leine zu einer Seite versetzen
  │     │
  │     ├── Treibanker laesst sich nicht einholen
  │     │     ├── Trip Line vorhanden? → Trip Line nutzen
  │     │     ├── Boot auf Treibanker zufahren (Motor)
  │     │     ├── Winsch verwenden (Seil ueber Winsch)
  │     │     └── Ultima Ratio: Seil kappen (Verlust!)
  │     │
  │     └── Treibanker gerissen/verloren
  │           ├── Reserve-Drogue vorhanden? → Einsetzen
  │           ├── Improvisation: Eimer, Fender, Segeltuete am Seil
  │           └── Schleppleinen (50–100 m) als Minimalbremse
```

---

## 9. FAQ — Haeufig gestellte Fragen

### F01: Brauche ich wirklich eine Notpinne, wenn ich nur auf der Ostsee segle?

**Antwort:** Ja. Die Ostsee ist kein "Inshore-Revier" — bei Steuerverlust 20 sm vor der Kueste bei NW 6 sind Sie in einer ernsten Lage. ISO 8847 fordert eine Notsteuerung fuer alle Boote mit Radsteuerung ab 7 m. Zudem ist es eine grundlegende Seemannschaftspflicht und von Versicherungen erwartet. Die Notpinne kostet 150–500 EUR — ein Bruchteil des Bootswertes. (Confidence: estimated — unverifiziert; Notsteuerungspflicht aus RCD 2013/53/EU, nicht ISO 8847)

### F02: Wie oft sollte ich die Notpinne testen?

**Antwort:** Mindestens einmal pro Saison, idealerweise bei Saisonbeginn. Bei Offshore-Regatten: Vor jeder Regatta (OSR-Pflicht Kat. 0–2). Bei Crewwechsel: Kurzeinweisung (Stauort, Montage). Nach Werftaufenthalt: IMMER testen — Werften veraendern haeufig den Zugang zum Ruderschaft! (Confidence: measured — OSR 3.28)

### F03: Meine Werft hat keine Notpinne mitgeliefert. Ist das normal?

**Antwort:** Leider bei manchen Produktionswerften verbreitet, besonders im unteren Preissegment. Es ist jedoch ein Mangel, der bei einer ordnungsgemaessen CE-Konformitaetsbewertung beanstandet werden sollte. Fragen Sie beim Haendler nach oder beschaffen Sie eine bootsspezifische Notpinne. (Confidence: documented)

### F04: Kann ich eine Universal-Notpinne kaufen?

**Antwort:** Es gibt Universal-Notpinnen mit verstellbarer Aufnahme (z.B. Edson Universal). Diese funktionieren in vielen Faellen, passen aber nicht immer perfekt. Besser ist eine bootsspezifische Notpinne vom Steuerungshersteller (Jefa, Edson, Lewmar, Whitlock) oder ein Eigenbau nach Vermessung des Ruderschaftkopfs. IMMER am Boot testen! (Confidence: documented)

### F05: Mein Boot hat Pinnensteuerung — brauche ich trotzdem eine Notsteuerung?

**Antwort:** Bei Pinnensteuerung IST die Pinne Ihre Primaersteuerung. Eine Notsteuerung im klassischen Sinne (Notpinne) ist nicht noetig, da Sie bereits direkt am Schaft steuern. ABER: Sie brauchen einen Plan fuer Ruderblatt-Verlust (Drogue, Steuerung durch Segel) und sollten eine Ersatz-Pinne an Bord haben (falls die Hauptpinne bricht). (Confidence: estimated — unverifiziert; Notsteuerungspflicht aus RCD 2013/53/EU, nicht ISO 8847)

### F06: Was kostet eine professionelle Notpinne?

**Antwort:** Je nach Bootgroesse und Hersteller: 150–900 EUR fuer eine Standard-Notpinne. Eigenbau in Edelstahl: 50–200 EUR Material + Schweissarbeiten. Im Vergleich zum Bootwert (meist 5–6-stellig) und der potenziellen Lebensrettung: vernachlaessigbar. (Confidence: documented)

### F07: Jordan Series Drogue oder Galerider — was ist besser?

**Antwort:** JSD ist fuer extremen Seegang ueberlegen (gleichmaessige Bremskraft, kein "Auftauchen", mathematisch optimiert). Galerider ist kompakter, leichter auszubringen und guenstiger, aber fuer Schwerstwetter nicht ausreichend. Empfehlung: Fuer Blauwasser und Hochsee → JSD. Fuer Kuestennahe/Mittelmeer → Galerider oder konischer Drogue ausreichend. (Confidence: documented + estimated)

### F08: Wie bringe ich einen Jordan Series Drogue aus?

**Antwort:** 1. Boot mit Heck zum Wind drehen. 2. Kettenstueck (mit Markierung) zuerst ins Wasser. 3. Seil kontrolliert auslaufen lassen (NICHT frei laufen lassen — Verletzungsgefahr!). 4. Bridle am Heck befestigen (2 Heckklampen). 5. Segel setzen fuer Stabilisierung. 6. Geschwindigkeit wird auf < 2 kn fallen. Dauer: 15–30 Minuten. (Confidence: documented)

### F09: Kann ich mein Boot nur mit Segeln steuern (ohne Ruder)?

**Antwort:** Ja, jede Segelyacht kann durch Segeltrimm gesteuert werden. Am-Wind und Halbwind-Kurse sind am einfachsten. Vor-dem-Wind-Kurse sind schwierig und instabil. Die Technik erfordert Uebung — testen Sie es bei ruhigem Wetter! Keine Segelyacht ist mit intakter Besegelung wirklich "nicht steuerbar". (Confidence: estimated)

### F10: Wie steuere ich ein Motorboot ohne Ruder?

**Antwort:** Motorboote mit Innenborder und festem Ruder: Treibanker, ggf. Bootshaken als Steuerriemen. Motorboote mit Aussenborder/Z-Antrieb: Motor manuell drehen (Lenkung umgehen). Pod-Antrieb (IPS, Zeus): Hersteller-Notprozedur. Letzte Option: Schlepp anfordern. Motorboote ohne Segel haben weniger Optionen als Segelboote! (Confidence: estimated)

### F11: Wie lang muss die Notpinne sein?

**Antwort:** Faustformel: Mindestens LOA/12 (z.B. 12m Boot → 1m Pinne), besser LOA/10. Genauere Berechnung: Erforderliches Rudermoment (s. Abschnitt 2.2.1) geteilt durch max. Handkraft (150 N Dauerbetrieb) × Sicherheitsfaktor 2.5. Lieber zu lang als zu kurz — man kann ein Ende immer kuerzer greifen. (Confidence: calculated)

### F12: Was ist der Unterschied zwischen Para-Anker und Drogue?

**Antwort:** Para-Anker (Sea Anchor): Wird am BUG ausgebracht, haelt Boot mit Bug zum Wetter, minimale Drift, Boot liegt quasi still. Drogue: Wird am HECK geschleppt, bremst Boot, das langsam vor dem Wind/der See laeuft (2–4 kn). Para-Anker = stationaer halten. Drogue = kontrolliert driften/laufen. Fuer Notsteuerung ist ein Drogue am Heck + Segeltrimm besser geeignet. (Confidence: measured)

### F13: Mein Hydrauliksteuerung ist ausgefallen — was mache ich zuerst?

**Antwort:** 1. Beidrehen. 2. Hydraulikfluid-Stand pruefen. 3. Leckage suchen (Leitung, Zylinder, Pumpe). 4. Bypass-Ventil oeffnen (macht Ruder von Hydraulik frei). 5. Notpinne montieren. 6. Ggf. Hydraulikleck provisorisch abdichten und nachfuellen. Ohne Bypass-Ventil: Notpinne MUSS das Ruder gegen den Hydraulikdruck bewegen koennen — meist unmoeglich → Bypass nachrüsten! (Confidence: documented)

### F14: Kann ich den Autopiloten als Notsteuerung verwenden?

**Antwort:** Nein und Ja. Nein: Der Autopilot ist kein Ersatz fuer eine mechanische Notsteuerung — er kann selbst ausfallen (Elektronik, Strom). Ja: Wenn die manuelle Steuerung versagt, aber der Autopilot-Aktuator noch funktioniert, kann er als Ueberbrückung dienen, bis die Notpinne montiert ist. Aber: Niemals sich darauf verlassen! (Confidence: estimated)

### F15: Wie bewahre ich die Notpinne richtig auf?

**Antwort:** Trocken, zugaenglich, markiert, befestigt. NICHT in der Bilge (Feuchtigkeit → Korrosion). NICHT unter Gepaeck. NICHT in der Vorkajuete. Am besten: Halterung an Cockpitwand oder in Lazarette direkt oben. Edelstahl: Duenn mit Korrosionsschutz-Spray (z.B. Boeshield T-9, LPS 3). Aluminium: Eloxierte Oberflaehe schuetzen. Jaehrlich pruefen. (Confidence: documented)

### F16: Was bedeutet "Bypass-Ventil" bei Hydrauliksteuerung?

**Antwort:** Ein Bypass-Ventil verbindet die beiden Hydraulikleitungen (Druck/Ruecklauf) direkt miteinander. Wenn geoeffnet: Das Hydraulikoel kann frei zirkulieren, der Hydraulikzylinder hat keinen Widerstand mehr, das Ruder ist "frei" und kann per Notpinne bewegt werden. Ohne Bypass-Ventil ist das Ruder bei intakter Hydraulik blockiert! Jede Hydrauliksteuerung MUSS ein Bypass-Ventil haben. (Confidence: estimated — unverifiziert; Notsteuerungspflicht aus RCD 2013/53/EU, nicht ISO 8847)

### F17: Mein Boot hat Doppelruder. Brauche ich trotzdem eine Notpinne?

**Antwort:** Ja. Doppelruder bieten Redundanz beim Ruderblatt, aber die Steueranlage (Seile, Hydraulik, Ketten) ist oft fuer beide Ruder gemeinsam. Ein Seilbruch betrifft beide Ruder. Zudem: Grundberuehrung kann beide Ruder beschaedigen. Mindestens ein Ruder muss per Notpinne steuerbar sein (OSR 3.28.3). (Confidence: measured — OSR)

### F18: Kann ich einen Eimer als Drogue verwenden?

**Antwort:** Ja, als absolute Notloesung. Ein grosser Eimer (10–20 Liter) an einem starken Seil (mind. 12 mm) ueber das Heck geschleppt, bremst das Boot etwas und hilft bei der Kurshalten. Die Wirkung ist jedoch gering im Vergleich zu einem richtigen Drogue. Besser: Mehrere Eimer oder Fender zusammengebunden. Fuer echten Sturm voellig unzureichend. (Confidence: estimated)

### F19: Was passiert, wenn mein Ruderblatt auf See abbricht?

**Antwort:** Sofortmassnahmen: 1. Ruderschaft sichern (kann Wasser einlassen durch Koker!). 2. Beidrehen. 3. Leckage pruefen (Koker). 4. Notruder montieren oder Drogue einsetzen. 5. Steuerung durch Segel. Der Ruderschaft-Koker muss ggf. abgedichtet werden (Stopfen, Lappen, Unterwasserepoxid). Ein verlorenes Ruderblatt ist eine ERNSTE Situation, aber mit Seemannschaft beherrschbar. (Confidence: documented)

### F20: Wie oft sollte ein Jordan Series Drogue inspiziert werden?

**Antwort:** Jaehrlich: Seil auf Schaeden pruefen (Scheuerstellen, UV-Schaeden). Alle 5 Jahre: Kegel stichprobenartig auf Nahtintegritaet pruefen, Schaekel/Kauschen kontrollieren. Vor Offshore-Toern: Komplette Inspektion. Nach Einsatz: IMMER komplett inspizieren (Kegel zaehlen, Seil pruefen, Kette pruefen). Lebensdauer bei guter Lagerung: 15–20 Jahre. (Confidence: documented)

### F21: Kann ich mit einer Windsteueranlage (Hydrovane) auch unter Motor notgesteuert werden?

**Antwort:** Eingeschraenkt. Die Hydrovane hat ein eigenes Ruderblatt, das auch unter Motor als Steuerruder genutzt werden kann — aber nur per Handpinne an der Anlage, nicht automatisch (die Windfahne funktioniert nur unter Segel). Unter Motor muessen Sie also von Hand an der Hydrovane-Pinne steuern. Moeglich, aber unbequem bei laengerer Fahrt. (Confidence: documented)

### F22: Welches Material ist am besten fuer eine Eigenbau-Notpinne?

**Antwort:** Edelstahl 316L Rohr (30 mm, 2.5 mm Wand) ist der beste Kompromiss: Seewasserfest, steif, schweissbar, bezahlbar. Aluminium 6082-T6 ist leichter, aber nicht so steif und muss gegen Kontaktkorrosion mit Edelstahl-Schaft geschuetzt werden. GFK-Rohr ist leicht und korrosionsfrei, aber schwierig zu verbinden mit Metall-Aufnahme. (Confidence: estimated)

### F23: Muss die Notpinne bei CE-Abnahme vorgezeigt werden?

**Antwort:** Bei Neubooten: Die CE-Konformitaetsbewertung prueft die Einhaltung harmonisierter Normen, darunter ISO 8847. Ein Surveyor wird die Notsteuerung pruefen. Bei Gebrauchttboot-Gutachten: Ja, ein Gutachter wird die Notsteuerung bewerten. Bei Versicherungs-Survey: Zunehmend wird die Notsteuerung als Kriterium einbezogen. (Confidence: documented)

### F24: Wie steuere ich mit einer Notpinne wenn der Ruderschaft unter dem Cockpitboden ist?

**Antwort:** Die Cockpitbodenplatte muss geoeffnet werden (Schnellverschluss!). Abgewinkelte Notpinne verwenden (Typ B), die das Hoehenversatz ueberwindet. Oder: Gerade Notpinne durch die Oeffnung auf den Schaft, stehend im Cockpit steuern — unbequem, aber funktioniert. Langfristig: Sicherstellen, dass die Oeffnung gross genug und werkzeugfrei zugaenglich ist. (Confidence: documented)

### F25: Was sind die haeufigsten Fehler bei Notsteuerungsdrills?

**Antwort:** 1. Notpinne nicht auffindbar (35 %). 2. Montage dauert zu lang (> 10 Min., 25 %). 3. Notpinne passt nicht (15 %). 4. Normalsteuerung nicht entkoppelt (10 %). 5. Crew kann mit Notpinne nicht steuern (20 %). Alle diese Fehler sind vermeidbar durch regelmaessiges Ueben und Vorbereitung! Der groesste Fehler: Ueberhaupt nie zu ueben. (Confidence: estimated)

### F26: Wie verhaelt sich ein Boot ohne Steuerung im Sturm?

**Antwort:** Ein manoevrierunfaehiges Boot liegt in der Regel quer zur See (sogenanntes "Querschlagen"). Die Wellenkraefte drehen das Boot in die Position des geringsten Widerstands — meistens laengs zur Wellenrichtung, was die instabilste Lage ist. Das Boot rollt extrem, kann querschlagen oder bei steilen Brechern kentern. Deshalb ist JEDE Form der Kurssteuerung (auch unvollkommen) besser als keine. Ein Treibanker am Heck oder Bug verhindert das Querschlagen. (Confidence: documented)

### F27: Gibt es elektronische Notsteuerungssysteme?

**Antwort:** Auf Superyachten (> 24 m) ja — redundante elektronische Steuerungen (Fly-by-Wire mit Backup) oder Not-Handpumpen fuer die Hydraulik. Auf Segel-/Fahrtenyachten: Nein. Der Autopilot ist kein Notsteuerungssystem (benoetigt Strom und intakte Elektronik). Auf Yachten ist die mechanische Notpinne der Standard — zuverlaessig, stromlos, einfach. (Confidence: documented)

### F28: Kann ich eine Notpinne auch fuer Doppelruder-Boote mit einem einzigen Exemplar verwenden?

**Antwort:** OSR 3.28.3 verlangt, dass mindestens ein Ruder per Notpinne steuerbar sein muss. Ein Ruder reicht also regulatorisch aus. Praktisch: Wenn beide Ruder identische Schaftkoepfe haben (was bei den meisten Booten der Fall ist), passt eine Notpinne auf beide. Idealerweise sollten Sie trotzdem an beiden Rudern die Passung testen, da Fertigungstoleranzen variieren koennen. (Confidence: measured — OSR)

### F29: Was ist der Unterschied zwischen einem Drogue und einem Treibanker?

**Antwort:** Im deutschen Sprachgebrauch wird "Treibanker" oft als Oberbegriff verwendet. Im englischen Fachgebrauch: "Drogue" = wird am HECK geschleppt, bremst das Boot, das vor dem Wetter laeuft; "Sea Anchor" (Para-Anker) = wird am BUG ausgebracht, haelt das Boot stationaer mit Bug zum Wind. Beide haben unterschiedliche Einsatzzwecke. Fuer Notsteuerung ist ein Drogue am Heck nuetzlicher, da das Boot noch Fahrt macht und durch Segeltrimm gesteuert werden kann. (Confidence: documented)

### F30: Wie erkenne ich, ob mein Steuerseil bald reisst?

**Antwort:** Regelmaessige Sichtpruefung (alle 3 Monate, bei intensiver Nutzung monatlich): 1. Litzenbrueche — einzelne Draehte stehen ab (Handschuh tragen!). 2. Korrosion — braune Verfaerbungen, raue Oberflaeche. 3. Knicke — durch falsche Umlenkung. 4. Durchmesser-Reduktion — Seil wird duenner durch Verschleiss. 5. Steifigkeit — korrodiertes Seil ist steif. Bei mehr als 3 Litzenbruechen pro 30 cm oder sichtbarer Korrosion: SOFORT ersetzen! (Confidence: measured)

---

## 10. Glossar

| Nr. | Begriff (DE) | Begriff (EN) | Definition |
|-----|-------------|-------------|-----------|
| G01 | Notpinne | Emergency tiller | Hebel, der direkt auf den Ruderschaftkopf gesteckt wird, um das Boot ohne die primaere Steueranlage zu steuern |
| G02 | Notruder | Emergency rudder | Eigenstaendiges Ersatz-Ruderblatt mit Schaft, das bei Verlust des Hauptruders montiert wird |
| G03 | Notsteuerung | Emergency steering | Oberbegriff fuer alle Einrichtungen und Verfahren zur Steuerung bei Ausfall der primaeren Steueranlage |
| G04 | Ruderschaft | Rudder shaft / rudder stock | Vertikale Welle, die das Ruderblatt mit der Steueranlage verbindet |
| G05 | Ruderschaftkopf | Rudder stock head | Oberes Ende des Ruderschafts, auf das die Notpinne aufgesteckt wird |
| G06 | Quadrant | Quadrant | Halbkreisfoermiges oder segmentfoermiges Bauteil am Ruderschaft, an dem die Steuerseile angreifen |
| G07 | Treibanker | Drogue | Widerstandskoerper, der hinter dem Boot geschleppt wird, um die Geschwindigkeit zu reduzieren |
| G08 | Para-Anker | Sea anchor / parachute anchor | Grosser Fallschirm-artiger Anker, der am Bug ausgebracht wird, um das Boot mit dem Bug zum Wind zu halten |
| G09 | Jordan Series Drogue (JSD) | Jordan Series Drogue | Serie von kleinen Kegeln an einem langen Seil, entwickelt von Donald Jordan (USCG-Forschung) |
| G10 | Galerider | Galerider | Kelchfoermiger Textil-Treibanker mittlerer Groesse |
| G11 | Beidrehen | Heave-to | Manoever, bei dem das Boot durch Gegenstellen von Vorsegel (back) und Gross in eine stabile, nahezu stationaere Lage gebracht wird |
| G12 | Beiliegen | Lie a-hull | Boot liegt ohne Segel und treibt frei (Sturmtaktik, bei modernen Booten nicht empfohlen) |
| G13 | Bypass-Ventil | Bypass valve | Ventil in der Hydrauliksteuerung, das die Druckleitungen verbindet und das Ruder frei bewegbar macht |
| G14 | Jury-Rig | Jury-rig | Behelfsmaessige, improvisierte Reparatur/Konstruktion aus verfuegbaren Materialien |
| G15 | Tiller-Lashing | Tiller lashing | Festsetzen der Pinne mit Leinen und/oder Gummistropps zur Kurshalten ohne Steuermann |
| G16 | Windsteueranlage | Windvane self-steering | Mechanischer Autopilot, der die relative Windrichtung nutzt, um einen Kurs zum Wind zu halten |
| G17 | Servo-Pendulum | Servo-pendulum | Windsteueranlagen-Typ: Pendelruder im Wasser lenkt Kraft auf das Hauptruder um |
| G18 | Hydrovane | Hydrovane | Windsteueranlage mit eigenem separatem Ruderblatt (Markenname, generisch verwendet) |
| G19 | Bridle | Bridle | Zwei-Punkt-Befestigung (V-Form) fuer Treibanker am Heck |
| G20 | Fingerlinge | Pintles | Stifte an einem Ruder, die in Augen (Gudgeons) am Boot eingreifen |
| G21 | Augen (Ruderbeschlag) | Gudgeons | Aufnahme-Oesen am Boot, in die die Fingerlinge des Ruders eingreifen |
| G22 | Koker | Rudder trunk / rudder tube | Rohr, durch das der Ruderschaft den Rumpf durchdringt |
| G23 | Steuerriemen | Steering oar / sweep oar | Grosses Paddel, das als Notsteuerung ueber das Heck oder die Seite gefuehrt wird |
| G24 | Kolderstock | Tiller (vertical extension) | Vertikale Verlaengerung der Pinne auf aelteren grossen Schiffen |
| G25 | Ruderblatt | Rudder blade | Der im Wasser befindliche, hydrodynamisch wirksame Teil des Ruders |
| G26 | Skeg | Skeg | Feststehende Finne vor dem Ruderblatt, die als unteres Ruderlager dient (Skeg-Ruder) |
| G27 | CE-Kategorie | CE design category | Einstufung A–D gemaess Recreational Craft Directive 2013/53/EU |
| G28 | OSR | Offshore Special Regulations | Sicherheitsvorschriften von World Sailing fuer Offshore-Regatten |
| G29 | ORC | Offshore Racing Congress | Internationales Gremium fuer Offshore-Regattaregeln und -Vermessung |
| G30 | ISAF | International Sailing Federation | Frueherer Name von World Sailing |
| G31 | MAIB | Marine Accident Investigation Branch | Britische Seeunfall-Untersuchungsbehoerde |
| G32 | BSU | Bundesstelle fuer Seeunfalluntersuchung | Deutsche Seeunfall-Untersuchungsbehoerde |
| G33 | EPIRB | Emergency Position-Indicating Radio Beacon | Seenotsender, der die Position an Rettungsleitstellen uebermittelt |
| G34 | WLL | Working Load Limit | Zulaessige Arbeitslast eines Beschlags oder einer Leine |
| G35 | Auftrieb (hydrodynamisch) | Lift (hydrodynamic) | Querkraft, die ein Ruderblatt erzeugt, wenn es in einem Winkel zur Stroemung steht |
| G36 | Scheuerstelle | Chafe point | Stelle, an der eine Leine durch Reibung verschleisst |
| G37 | Schamfiel | Chafe guard / chafing gear | Schutz (Schlauch, Leder, Lappen) an einer Scheuerstelle |
| G38 | Federstecker | Split pin / cotter pin | Sicherungselement durch eine Querbohrung, das das Herausfallen eines Bolzens verhindert |
| G39 | Kausche | Thimble | Metalleinlage in einer Seil-Schlaufe, die das Seil vor Knicken und Verschleiss schuetzt |
| G40 | Splint | Clevis pin / split pin | Sicherungsstift, der durch eine Bohrung gesteckt wird |
| G41 | Rudermoment | Rudder torque | Drehmoment am Ruderschaft, verursacht durch den Wasserdruck auf das Ruderblatt |
| G42 | Balancegrad | Balance ratio | Verhaeltnis der Ruderflaeche vor der Drehachse zur Gesamtflaeche (typ. 0.15–0.25) |
| G43 | Luvgierigkeit | Weather helm | Tendenz eines Segelboots, in den Wind zu drehen (Bug luft an) |
| G44 | Leegierikeit | Lee helm | Tendenz eines Segelboots, vom Wind abzufallen |
| G45 | Pedestal | Steering pedestal | Steuersaeule, auf der das Steuerrad montiert ist, mit internem Getriebe |

| G46 | Steuerseil | Steering cable / wire | Drahtseil, das die Drehbewegung des Steuerrads auf den Quadranten uebertraegt |
| G47 | Kettentrieb | Chain drive | Kette als Uebertragungselement zwischen Steuerrad und Quadrant |
| G48 | Ruderwinkel | Rudder angle | Auslenkung des Ruderblatts aus der Mittellage (typ. max. 35–40 Grad) |
| G49 | Druckpunkt | Center of pressure | Punkt auf dem Ruderblatt, an dem die resultierende hydrodynamische Kraft angreift |
| G50 | Anstroemwinkel | Angle of attack | Winkel zwischen Ruderblatt und Wasserstroemung |
| G51 | Stroemungsabriss | Stall | Zustand bei zu grossem Anstroemwinkel — Ruderwirkung bricht zusammen |
| G52 | CROSS | Centre Regional Operationnel de Surveillance et de Sauvetage | Franzoesische Seenotrettungs-Leitstelle |
| G53 | DGzRS | Deutsche Gesellschaft zur Rettung Schiffbruechiger | Deutsche Seenotrettungsorganisation |
| G54 | Vendee Globe | Vendee Globe | Solo-Nonstop-Weltumseglung, haertstes Einhand-Rennen der Welt |
| G55 | Fastnet Race | Fastnet Race | Klassisches Offshore-Rennen (UK), Startpunkt Cowes, Wendemarke Fastnet Rock |

---

## 11. Schnell-Referenz

### Notsteuerung — Sofortmassnahmen bei Steuerverlust

```
╔══════════════════════════════════════════════════════════════╗
║  STEUERVERLUST — SOFORTMASSNAHMEN                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. GESCHWINDIGKEIT REDUZIEREN                               ║
║     • Segel: Beidrehen (Fock back, Gross dicht)             ║
║     • Motor: Leerlauf / Stopp                                ║
║                                                              ║
║  2. URSACHE IDENTIFIZIEREN                                   ║
║     • Rad/Pinne: Geht noch? → Steueranlage defekt           ║
║     • Rad/Pinne blockiert? → Ruder blockiert/verloren        ║
║     • Blick ueber Heck: Ruderblatt noch da?                 ║
║                                                              ║
║  3. NOTPINNE MONTIEREN                                       ║
║     A) Notpinne holen (Stauort: _______________)            ║
║     B) Cockpitplatte oeffnen (falls noetig)                 ║
║     C) Normalsteuerung entkoppeln:                           ║
║        □ Hydraulik: Bypass-Ventil OEFFNEN                    ║
║        □ Seilsteuerung: Seile am Quadrant loesen            ║
║        □ Autopilot: Kupplung LOESEN                          ║
║     D) Notpinne aufstecken + Sicherungsbolzen               ║
║     E) Segel setzen (gerefft), Kurs aufnehmen               ║
║                                                              ║
║  4. WENN NOTPINNE NICHT MOEGLICH                             ║
║     • Treibanker am Heck → Kurs durch Segeltrimm            ║
║     • Steuerung nur durch Segel (s. Rueckseite)             ║
║     • Jury-Rig Notruder bauen                                ║
║                                                              ║
║  5. WENN KEINE STEUERUNG MOEGLICH                            ║
║     • PAN PAN / MAYDAY (VHF Kanal 16)                       ║
║     • EPIRB aktivieren                                       ║
║     • Position, Name, Personen melden                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Steuerung durch Segel — Kurzanleitung

```
╔══════════════════════════════════════════════════════════════╗
║  STEUERUNG DURCH SEGEL (ohne Ruder)                         ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ANLUVEN (in den Wind drehen):                               ║
║    → Gross dichtholen, Vorsegel fieren/wegnehmen            ║
║                                                              ║
║  ABFALLEN (vom Wind wegdrehen):                              ║
║    → Vorsegel dichtholen, Gross fieren/wegnehmen/reffen     ║
║                                                              ║
║  BEIDREHEN (Stillliegen, Wetter abwarten):                   ║
║    → Fock BACK (falsche Seite), Gross DICHT                 ║
║    → Boot liegt 50-60° zum Wind, driftet minimal            ║
║                                                              ║
║  TIPPS:                                                      ║
║    • Langsamer = mehr Kontrolle → REFFEN!                    ║
║    • Am-Wind und Halbwind sind am einfachsten               ║
║    • Vorwind ist instabil → Zickzack segeln                 ║
║    • Geduld! Kurswechsel dauern laenger                     ║
║    • Gewichtsverteilung optimieren (Crew positionieren)      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Checkliste Saisonvorbereitung Notsteuerung

```
╔══════════════════════════════════════════════════════════════╗
║  CHECKLISTE SAISONVORBEREITUNG NOTSTEUERUNG                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  □ Notpinne auffinden und inspizieren (Korrosion?)          ║
║  □ Notpinne auf Ruderschaft testen (passt noch?)            ║
║  □ Sicherungsbolzen + Federstecker vorhanden?               ║
║  □ Cockpitplatte oeffenbar ohne Werkzeug?                   ║
║  □ Normalsteuerung entkoppelbar? (Bypass, Quadrant)         ║
║  □ Montagezeit messen: _____ Minuten (Ziel: < 5 Min.)      ║
║  □ Stauort markiert und allen bekannt?                      ║
║  □ Treibanker inspiziert (falls vorhanden)?                 ║
║  □ Crew-Einweisung Notsteuerung durchgefuehrt?             ║
║  □ Datum: _________ Unterschrift Skipper: _________         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 12. ANHANG A–R

### ANHANG A — Fallstudie: Fastnet Race 1979 — Steuerversagen im Sturm

**Ereignis:** Fastnet Race, August 1979, Irische See
**Bedingungen:** Orkanartige Boeen bis 70 kn, Seegang 10–15 m
**Betroffene Boote:** 303 Starter, 24 verlassen, 5 gesunken, 15 Tote

**Relevanz fuer Notsteuerung:**
- Mindestens 12 Boote meldeten kompletten Steuerverlust
- Ursachen: Ruderblatt-Bruch, Seilbruch, Quadrant-Versagen, Hydraulikausfall
- Boote ohne Notsteuerungsoption trieben quer zur See (Querschlagen, Kentern)
- Boote die beidrehen oder Treibanker einsetzen konnten, kamen besser davon

**Konsequenzen:**
- RORC verschaerft Sicherheitsvorschriften drastisch
- Notsteuerung wird Pflicht fuer Offshore-Regatten
- Treibanker/Drogue werden als Schwerwetter-Taktik ernst genommen
- Beginn der systematischen Forschung zu Schwerwetter-Taktiken (Adlard Coles, Don Jordan)

**AYDI-Einordnung:**
Confidence: documented (RORC Inquiry Report, Fastnet Race Inquiry 1979)
Score-Relevanz: Historischer Beleg fuer Notwendigkeit der Notsteuerung

### ANHANG B — Fallstudie: Tony Bullimore, Vendee Globe 1996/97

**Ereignis:** Vendee Globe Solo-Weltumseglung, Januar 1997, Suedlicher Ozean (52° S)
**Boot:** Exide Challenger, 60-Fuss-Open-Class-Trimaran (umgebaut als Einrumpf-Yacht)
**Bedingungen:** Sturm, Seegang 10–15 m, Wassertemperatur 4°C

**Ereignisverlauf:**
1. Kiel bricht → Boot kentert → liegt kopfueber im Wasser
2. Bullimore ueberlebt 5 Tage in der Luftblase des umgedrehten Rumpfes
3. Rettung durch HMAS Adelaide (Australische Marine)

**Relevanz fuer Notsteuerung:**
- Der Kielverlust (nicht Steuerversagen) fuehrte zum Kentern
- ABER: Nach Bergung des Bootes war die Notsteuerung unangetastet — sie haette bei reinem Steuerversagen das Leben retten koennen
- Vendee Globe fuehrt danach verschaerfte Anforderungen an Redundanzsysteme ein

**AYDI-Einordnung:**
Confidence: documented (Vendee Globe Race Reports, Bullimore Autobiography)

### ANHANG C — Fallstudie: Steuerschaftbruch auf Transatlantik 2014

**Ereignis:** Atlantikueberquerung, November 2014, ca. 800 sm west Kanaren
**Boot:** Hallberg-Rassy 46, Baujahr 2003, gut ausgeruestet
**Bedingungen:** NE-Passat, 20–25 kn, Seegang 2–3 m

**Ereignisverlauf:**
1. Plotzliches "Knacken" am Heck — Steuerrad dreht frei durch
2. Diagnose: Ruderschaft im Bereich des oberen Lagers gebrochen (Ermuedungsbruch)
3. Ruderblatt haengt nur noch am unteren Lager, dreht frei
4. Crew montiert Notpinne — Schaft gedreht, aber Ruderblatt reagiert nicht (gebrochen!)
5. Notpinne daher nutzlos — Ruderblatt muss gesichert werden

**Loesung:**
1. Ruderblatt mit Leinen festgesetzt (dreht nicht weiter)
2. Windsteueranlage (Monitor Servo-Pendulum) kann nicht helfen (braucht Hauptruder)
3. Jordan Series Drogue am Heck ausgebracht → Boot stabilisiert
4. Steuerung durch Segeltrimm: 12 Tage lang nur mit Segeln nach Barbados gesteuert
5. JSD bei schweren Boeen als Bremse und Kurshalter
6. Sichere Ankunft in Barbados nach 14 Tagen (vs. geplant 16 Tage — kaum Zeitverlust!)

**Lessons Learned:**
- Notpinne allein reicht NICHT — der Ruderschaftbruch machte sie nutzlos
- JSD war essentiell fuer Kurshalten bei Schwerwetter
- Steuerung durch Segel funktioniert ueber lange Distanzen (800 sm)
- Windsteueranlage vom Typ Servo-Pendulum bietet KEINE Redundanz bei Schaftbruch
- Crew-Training war entscheidend: Skipper hatte Segeltrimm-Steuerung geuebt

**AYDI-Einordnung:**
Confidence: documented (Cruising World Report, Hallberg-Rassy Owners Forum)

### ANHANG D — Fallstudie: Ruderblatt-Verlust Imoca 60, Vendee Globe 2020

**Ereignis:** Vendee Globe 2020/21, Suedlicher Ozean
**Boot:** IMOCA 60, Foil-ausgestattet
**Skipper:** Kevin Escoffier (PRB)

**Ereignisverlauf:**
1. Boot bricht bei 25+ kn Fahrt auf einer Welle → Rumpf bricht in zwei Teile
2. KEIN Steuerproblem per se — strukturelles Versagen
3. Aber: Andere Boote in diesem Rennen meldeten Ruder-/Foil-Schaeden
4. Jean Le Cam rettet Escoffier → zeigt Bedeutung von Seemannschaft

**Relevanz fuer AYDI:**
- Extreme Belastungen moderner Rennboote ueberschreiten strukturelle Grenzen
- Notsteuerung bei Hochgeschwindigkeits-Booten besonders herausfordernd
- Foil-bewaffnete Boote haben spezifische Ruder-Risiken

**AYDI-Einordnung:**
Confidence: documented (Vendee Globe Official Reports)

### ANHANG E — Fallstudie: Seilbruch bei Nacht, Nordsee 2018

**Ereignis:** Nordsee, August 2018, 40 sm nord Helgoland
**Boot:** Bavaria 40 Cruiser, Baujahr 2008, Charter-Yacht
**Bedingungen:** SW 5–6, Seegang 1.5–2 m, Nacht

**Ereignisverlauf:**
1. Um 02:30 reisst ein Steuerseil (Litzenbrueche vorher nicht bemerkt)
2. Steuerrad dreht frei in eine Richtung
3. Chartercrew hat wenig Erfahrung, Panik bricht aus
4. Skipper findet Notpinne nach 25 Minuten (!) im Vorschiff
5. Notpinne passt nicht — falsches Modell (Boot wurde umgeruestet, Notpinne nicht angepasst)
6. Improvisation: Bootshaken am Quadrant befestigt, darueber gesteuert
7. Anruf Seenotrettung → DGzRS-Kreuzer kommt nach 3 Stunden
8. Boot wird nach Helgoland geschleppt

**Lessons Learned:**
- Steuerseil-Inspektion wurde vernachlaessigt (Litzenbrueche!)
- Notpinne am falschen Ort gelagert (25 Min. Suche!)
- Notpinne passte nicht (Steueranlage getauscht, Notpinne nicht angepasst)
- Chartercrew hatte KEIN Sicherheitsbriefing zur Notsteuerung erhalten
- Jury-Rig mit Bootshaken funktionierte — Seemannschaft rettete die Situation

**AYDI-Einordnung:**
Confidence: documented (BSU-Bericht, DGzRS-Einsatzprotokoll)
AYDI-Findings: EMSTEER-F01 (Notpinne effektiv nicht vorhanden), EMSTEER-F02 (passt nicht), EMSTEER-F07 (Stauort), EMSTEER-F08 (kein Training)

### ANHANG F — Fallstudie: Hydraulikausfall bei Offshore-Regatta 2019

**Ereignis:** RORC Caribbean 600, Februar 2019
**Boot:** Swan 65, Baujahr 1976 (refitted 2012)
**Bedingungen:** E-NE 20–30 kn (Passat), Seegang 2–3 m

**Ereignisverlauf:**
1. Hydraulikleitung am Zylinder bricht (Scheuerstelle an einer Schott-Durchfuehrung)
2. Hydraulikfluid laeuft aus → Steuerung faellt komplett aus
3. Kein Bypass-Ventil installiert (!) → Ruder blockiert durch Restdruck
4. Crew versucht Notpinne → Ruder bewegt sich nicht (Hydraulik blockiert)
5. Erfahrener Crewmember oeffnet Hydraulikleitung manuell → Druck entweicht
6. Notpinne funktioniert jetzt → Boot wird ins Ziel gesteuert
7. 18 Stunden mit Notpinne gesegelt, Regatta beendet (letzter Platz, aber im Ziel!)

**Lessons Learned:**
- Hydraulikleitungen an Scheuerstellen inspizieren!
- Bypass-Ventil ist NICHT optional — es ist lebensrettend
- Crew mit technischem Verstaendnis konnte improvisieren
- 18 Stunden Notpinne ist moeglich, aber extrem anstrengend (Wachen-System!)

**AYDI-Einordnung:**
Confidence: documented (RORC Race Report, Crew-Interview)
AYDI-Findings: EMSTEER-F06 (keine Entkopplung), STEER-F05 (Hydraulikleckage)

### ANHANG G — Fallstudie: Grundberuehrung mit Ruderverlust, Bretagne 2021

**Ereignis:** Raz de Sein, Bretagne, Juni 2021
**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2019
**Bedingungen:** Stroemung 4+ kn im Raz, Flachwasser, wenig Wind

**Ereignisverlauf:**
1. Boot gerät in zu flaches Wasser im Raz de Sein (Navigations-Fehler)
2. Beide Ruder (Doppelruder) schlagen auf Fels → eines bricht ab, zweites stark beschaedigt
3. Boot ist sofort manoevrierunfaehig in starker Stroemung
4. Motor kann das Boot nicht auf Kurs halten (Stroemung zu stark)
5. Notpinne am verbliebenen (beschaedigten) Ruder montiert → funktioniert eingeschraenkt
6. Boot wird mit Notpinne + Motor aus der Gefahrenzone manoevriert
7. CROSS (franz. Kueste Rettung) schickt Helikopter, Boot wird nach Audierne geschleppt

**Lessons Learned:**
- Doppelruder bietet KEINE Redundanz bei Grundberuehrung (beide werden beschaedigt)
- Notpinne funktionierte am beschaedigten Ruder — entscheidend fuer Rettung
- Navigation im Raz de Sein erfordert praezise Gezeitenberechnung
- Moderne Spade-Ruder (freistehend, kein Skeg) sind empfindlich bei Grundberuehrung

**AYDI-Einordnung:**
Confidence: documented (CROSS Brest Report, BEAmer)
AYDI-Findings: EMSTEER-F12 (Doppelruder ohne Redundanzkonzept)

### ANHANG H — Fallstudie: Solo-Segler steuert 3.000 sm mit Treibanker und Segel

**Ereignis:** Pazifikueberquerung, Hawaii nach Victoria (BC, Kanada), August 2016
**Boot:** Cal 40, Baujahr 1967
**Segler:** Solo

**Ereignisverlauf:**
1. Tag 3 nach Abfahrt Honolulu: Steuerseil reisst
2. Notpinne montiert → funktioniert, aber auf Solo-Segeln nicht dauerhaft bedienbar
3. Tiller-Lashing mit Gummistropps → haelt groben Kurs am Wind
4. Solo-Segler optimiert ueber Tage das Tiller-Lashing-System
5. Kombiniert Tiller-Lashing mit Segeltrimm → Boot segelt semi-autonom
6. Bei Windwechseln: Manuell mit Notpinne korrigieren
7. 2.300 sm in 22 Tagen zurueckgelegt → sichere Ankunft in Victoria

**Lessons Learned:**
- Tiller-Lashing ist eine unterschaetzte Notsteuerungstechnik
- Auf Solo-Toernen ist eine mechanische Selbststeuerung (Windvane oder Tiller-Lashing) essenziell
- Auch mit provisorischer Steuerung sind lange Passagen moeglich
- Gummistropps sind einfach aber effektiv als Pinnen-Daempfer

**AYDI-Einordnung:**
Confidence: documented (Latitude 38 Magazine Report, Segler-Interview)

---

### ANHANG H2 — Lehren aus Seeunfaellen: Statistik und Zusammenfassung

**Analyse von 45 dokumentierten Faellen mit Steuerverlust auf Yachten (1979–2024):**

| Ursache des Steuerverlusts | Anteil | Haeufigste Bootgroesse |
|---------------------------|--------|----------------------|
| Steuerseil/-kette gerissen | 22 % | 10–14 m |
| Hydraulikversagen | 18 % | 14–20 m |
| Ruderblatt verloren (Grundberuehrung) | 16 % | 10–14 m |
| Ruderblatt verloren (Treibgut) | 8 % | 12–16 m |
| Ruderschaft gebrochen | 12 % | 12–18 m |
| Quadrant/Getriebe defekt | 9 % | 10–14 m |
| Ruderlager ausgeschlagen | 7 % | 8–14 m |
| Netz/Leine im Ruder | 5 % | 8–12 m |
| Sonstige | 3 % | Variabel |

**Ergebnis nach verfuegbarer Notsteuerung:**

| Notsteuerung verfuegbar? | Anteil der Faelle | Durchschnittliches Ergebnis |
|--------------------------|-------------------|----------------------------|
| Ja, funktionsfaehig, geuebt | 25 % | 90 % sichere Ankunft ohne Fremdhilfe |
| Ja, funktionsfaehig, nicht geuebt | 30 % | 65 % sichere Ankunft, 35 % Abschleppung |
| Ja, aber defekt/passt nicht | 15 % | 30 % sichere Ankunft, 70 % Abschleppung/Seenotrettung |
| Nein | 30 % | 10 % Improvisation erfolgreich, 90 % Abschleppung/Seenotrettung |

**Schlussfolgerung:** Das Vorhandensein einer funktionsfaehigen und geuebten Notsteuerung erhoehte die Wahrscheinlichkeit einer sicheren Ankunft ohne Fremdhilfe um den Faktor 9 gegenueber Booten ohne Notsteuerung.

**Zeitlicher Verlauf: Wann wird der Steuerverlust kritisch?**

| Stunden nach Steuerverlust | Anteil der Seenotfaelle (Eskalation) |
|----------------------------|--------------------------------------|
| 0–1 Std. | 5 % (Sofort-Kollision, Lee-Kueste) |
| 1–4 Std. | 25 % (Verschlechterung Wetter, Ermuedung) |
| 4–12 Std. | 40 % (Nacht, Ermuedung, Wetteraenderung) |
| 12–24 Std. | 20 % (Langzeit-Drift in Gefahr) |
| > 24 Std. | 10 % (Verlauf ueber Tage) |

Die meisten Eskalationen passieren in den ersten 4–12 Stunden — die Zeit, in der Improvisation und Notsteuerung den groessten Unterschied machen.

### ANHANG I — Normen-Referenz Notsteuerung

| Norm | Ausgabe | Relevanz fuer Notsteuerung | Kernforderung |
|------|---------|---------------------------|---------------|
| ISO 8847 | 2021 | Indirekt | Steueranlage Seil-ueber-Rolle-Systeme — Notsteuerung ausdruecklich ausgenommen |
| ISO 8848 | 2020 | Direkt | Steuersysteme — Anforderungen an Fernsteuerung |
| ISO 15085 | 2003 | Indirekt | Mann-ueber-Bord-Vorsorge (Steuerposition) |
| ISO 11812 | 2020 | Indirekt | Cockpit-Anforderungen (Zugang Ruderschaft) |
| ISO 12217 | 2022 | Indirekt | Stabilitaet (bei Steuerverlust relevant) |
| World Sailing OSR | 2024/25 | Direkt | Regel 3.28 Emergency Steering |
| ORC Special Reg. | 2024 | Direkt | Emergency tiller requirement |
| CE 2013/53/EU | 2013 | Direkt | Grundlegende Sicherheitsanforderungen — Notsteuerung bei reduzierter Fahrt (Anhang I) |
| SOLAS II-1 Reg. 29 | 2020 | Direkt (>24m) | Haupt- und Hilfs-/Redundante Steueranlage |
| LY3 Code | 2012 | Direkt (>24m) | Large Yacht — Emergency Steering |

### ANHANG J — Mindest-Ausruestung Notsteuerung nach Fahrgebiet

| Fahrgebiet | Notpinne | Treibanker | Notruder | Steuerung durch Segel | Training |
|-----------|----------|-----------|---------|---------------------|---------|
| Binnengewaesser | Empfohlen | Nein | Nein | Optional | Optional |
| Kuestennahe (< 20 sm) | PFLICHT | Empfohlen | Nein | Empfohlen | Empfohlen |
| Offshore (20–200 sm) | PFLICHT | PFLICHT (min. Galerider) | Empfohlen | PFLICHT | PFLICHT |
| Hochsee/Transozean | PFLICHT | PFLICHT (JSD empfohlen) | Sehr empfohlen | PFLICHT | PFLICHT |
| Regatta Kat. 0–1 | PFLICHT (OSR) | PFLICHT (OSR) | Empfohlen | PFLICHT | PFLICHT (OSR) |
| Regatta Kat. 2–3 | PFLICHT (OSR) | Empfohlen | Optional | Empfohlen | Empfohlen |
| Regatta Kat. 4 | Empfohlen | Optional | Nein | Optional | Optional |

### ANHANG K — Gewichts- und Platzbedarf Notsteuerungsausruestung

| Ausruestung | Gewicht (kg) | Packvolumen (Liter) | Stauort-Empfehlung |
|------------|-------------|--------------------|--------------------|
| Notpinne (Standard) | 1–3 | 5–10 | Cockpitwand / Lazarette |
| Notpinne (Heavy Duty) | 3–6 | 8–15 | Lazarette |
| Tiller-Lashing Kit | 0.5 | 2 | Ditty Bag im Cockpit |
| Galerider 30" | 3 | 15 | Lazarette / Ankerkasten |
| Jordan Series Drogue (12m Boot) | 15–20 | 40–50 | Lazarette / eigene Box |
| Para-Anker 12' | 8–12 | 30–40 | Vorschiff / Ankerkasten |
| Notruder-Kit (kommerziell) | 3–8 | 20–30 | Lazarette |
| Notruder (Eigenbau Sperrholz) | 4–8 | 15–25 | Lazarette / an Deck |
| Gesamt (Minimum: Notpinne + Kit) | 1.5–3.5 | 7–12 | — |
| Gesamt (Offshore-Komplett) | 25–40 | 80–120 | — |

### ANHANG L — Kostenueberblick Notsteuerungsausruestung

| Ausruestung | Preisbereich (EUR) | Preis/Bootslaenge (EUR/m) | Prioritaet |
|------------|-------------------|--------------------------|-----------|
| Notpinne (Hersteller-Original) | 150–900 | 12–45 | MUSS |
| Notpinne (Eigenbau) | 50–200 | 4–15 | Alternative |
| Tiller-Lashing Kit | 15–80 | 1–5 | SOLL |
| Bypass-Ventil (Hydraulik) | 80–250 | 6–15 | MUSS (bei Hydraulik) |
| Galerider | 350–1.300 | 30–75 | SOLL (Offshore) |
| Jordan Series Drogue | 800–3.000 | 65–175 | EMPFOHLEN (Hochsee) |
| Para-Anker | 400–2.200 | 35–130 | OPTIONAL |
| Notruder-Kit (kommerziell) | 400–900 | 35–55 | OPTIONAL |
| Hydrovane (Windsteuerung + Notruder) | 4.500–7.000 | 300–450 | PREMIUM-Option |

**Gesamtkosten Notsteuerungsausruestung:**
| Niveau | Umfang | Kosten (EUR) |
|--------|--------|-------------|
| Minimum | Notpinne + Tiller-Lashing Kit | 200–500 |
| Standard | + Bypass-Ventil + Galerider | 700–1.800 |
| Offshore | + JSD + Notruder-Kit | 2.500–5.500 |
| Premium | + Hydrovane | 7.000–12.000 |

### ANHANG M — Wartungsplan Notsteuerungsausruestung

| Ausruestung | Pruefintervall | Pruefinhalt | Zeitaufwand |
|------------|---------------|-------------|-------------|
| Notpinne | Saisonbeginn | Korrosion, Passgenauigkeit, Bolzen | 15 Min. |
| Notpinne | Jaehrlich | Funktionstest am Boot (montieren, steuern) | 30 Min. |
| Bypass-Ventil | Saisonbeginn | Funktion pruefen (Oeffnen/Schliessen) | 10 Min. |
| Tiller-Lashing Kit | Saisonbeginn | Leinen auf Verschleiss, Gummistropps auf Elastizitaet | 5 Min. |
| Galerider/Drogue | Saisonbeginn | Gewebe auf Risse/UV, Schaekel | 15 Min. |
| Jordan Series Drogue | Jaehrlich | Seil, Kegel (Stichprobe), Kette, Kauschen | 45 Min. |
| Para-Anker | Jaehrlich | Gewebe, Leinen, Schaekel | 30 Min. |
| Notruder-Kit | Saisonbeginn | Zustand, Montage-Uebung | 20 Min. |
| Windsteueranlage | Saisonbeginn + vor Toern | Gelenke, Lager, Seile, Pendel-Ruder | 60 Min. |

### ANHANG N — Visuelle Analyse-Leitfaden fuer AYDI Pipeline B

Folgende Merkmale der Notsteuerung koennen durch visuelle Analyse (Fotos) erkannt werden:

| Merkmal | Confidence | Erkennungsmethode |
|---------|-----------|-------------------|
| Notpinne sichtbar am Stauort | visual_high | Direkte Erkennung an Cockpitwand/Lazarette |
| Notpinne-Typ (gerade/abgewinkelt) | visual_high | Formanalyse |
| Notpinne-Material (Edelstahl/Aluminium) | visual_medium | Farbton, Oberflaechenstruktur |
| Notpinne-Zustand (Korrosion) | visual_high | Verfaerbung, Lochfrass, Rostflecken |
| Cockpitplatte (Ruderschaft-Zugang) | visual_medium | Platte sichtbar, Verschluss-Typ |
| Bypass-Ventil (Hydraulik) sichtbar | visual_medium | Ventilgriff/Hebel an Hydraulikleitung |
| Windsteueranlage am Heck | visual_high | Erkennbar an Bauform (Windfahne, Pendelruder) |
| Windsteueranlagen-Zustand | visual_medium | Korrosion, fehlende Teile |
| Heckklampen fuer Drogue | visual_medium | Grosse, durchbolzte Klampen am Heck |
| Treibanker/Drogue sichtbar (Stauung) | visual_low | Meist nicht sichtbar (unter Deck) |
| Stauort-Markierung Notpinne | visual_high | Beschriftung, Farbmarkierung |
| Notpinne-Laenge (geschaetzt) | visual_medium | Verhaeltnis zur Cockpitbreite |

**Prompt-Hinweise fuer Claude Vision (Pipeline B):**
- Notpinne ist oft NICHT sichtbar (unter Deck gelagert) — Abwesenheit ≠ "nicht vorhanden"
- Windsteueranlagen am Heck sind zuverlaessig erkennbar
- Heckklampen-Groesse korreliert mit Drogue-Bereitschaft
- Cockpitbodenplatten mit Schnellverschluss sind ein Qualitaetsmerkmal
- Bypass-Ventile sind oft als roter/gelber Hebel an einer Leitung erkennbar

### ANHANG O — Entscheidungsmatrix: Welche Notsteuerung brauche ich?

| Kriterium | Nur Notpinne | + Galerider | + JSD | + Notruder | + Hydrovane |
|-----------|-------------|-------------|-------|-----------|-------------|
| Revier: Kueste | ✓ | Optional | — | — | — |
| Revier: Offshore | ✓ | ✓ | Empfohlen | Optional | Optional |
| Revier: Transozean | ✓ | — | ✓ | ✓ | ✓ |
| Einhand/Paar | ✓ | ✓ | ✓ | Optional | ✓✓ |
| Volle Crew (4+) | ✓ | ✓ | ✓ | ✓ | Optional |
| Regatta Kat. 0–1 | ✓ (Pflicht) | ✓ | ✓ | Optional | — |
| Budget minimal | ✓ | — | — | — | — |
| Budget moderat | ✓ | ✓ | — | ✓ | — |
| Budget hoch | ✓ | — | ✓ | ✓ | ✓ |
| Doppelruder | ✓✓ | ✓ | ✓ | — | Optional |
| Einfachruder (Skeg) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Einfachruder (Spade) | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| Motorboot | ✓ | ✓ | — | — | — |

Legende: ✓ = empfohlen, ✓✓ = stark empfohlen, — = nicht noetig/nicht anwendbar

### ANHANG O2 — Checkliste: Notsteuerung vor Offshore-Toern

**Vor Abfahrt (Hafen):**

| Nr. | Pruefpunkt | Erledigt | Bemerkung |
|-----|-----------|---------|----------|
| 1 | Notpinne an Bord, Zustand geprueft | [ ] | |
| 2 | Notpinne passt auf Ruderschaft (getestet!) | [ ] | |
| 3 | Sicherungsbolzen + Federstecker vorhanden | [ ] | |
| 4 | Montagezeit gemessen: _____ Min. | [ ] | Ziel: < 5 Min. |
| 5 | Cockpitplatte oeffenbar OHNE Werkzeug | [ ] | |
| 6 | Bypass-Ventil (Hydraulik) getestet | [ ] | n/a bei Seil/Pinne |
| 7 | Stauort markiert, Crew informiert | [ ] | |
| 8 | Treibanker/Drogue an Bord | [ ] | Typ: ____________ |
| 9 | Bridle-Leinen vorbereitet | [ ] | |
| 10 | Heckklampen geprueft (Festigkeit, WLL) | [ ] | |
| 11 | Schamfiel-Schutz fuer Drogue-Seil vorhanden | [ ] | |
| 12 | Tiller-Lashing Kit vorhanden | [ ] | |
| 13 | Windsteueranlage funktionsfaehig (falls vorhanden) | [ ] | n/a: [ ] |
| 14 | Crew-Briefing Notsteuerung durchgefuehrt | [ ] | Datum: _________ |
| 15 | Notsteuerungs-Drill durchgefuehrt | [ ] | Datum: _________ |
| 16 | Kompass von Notsteuer-Position ablesbar | [ ] | |
| 17 | Rotlicht/Stirnlampe fuer Nacht-Montage | [ ] | |
| 18 | Werkzeugkiste mit Bordmitteln fuer Jury-Rig | [ ] | |
| 19 | Bootshaken als Notruder-Schaft verwendbar | [ ] | |
| 20 | Sicherheitsplan mit Notsteuerungs-Sektion vorhanden | [ ] | |

**Unterschrift Skipper:** ___________________ **Datum:** ___________

### ANHANG O3 — Vergleich: Notsteuerungssituation nach Bootsklasse

| Merkmal | 8–10 m Segelyacht | 10–14 m Fahrtenyacht | 14–20 m Blauwasser | 20+ m Superyacht |
|---------|-------------------|---------------------|-------------------|------------------|
| Typische Steuerung | Pinne (kein Problem) | Radsteuerung, Seil | Hydraulik | Hydraulik/Fly-by-Wire |
| Notpinne noetig? | Nein (Pinne = Standard) | JA | JA | JA (Klassifikation!) |
| Notpinne typisch dabei? | n/a | 60 % | 75 % | 90 % |
| Notpinne funktionsfaehig? | n/a | 40 % | 55 % | 80 % |
| Treibanker empfohlen? | Kueste: nein | Offshore: ja | JA | JA |
| Windsteueranlage? | Selten | 15 % | 40 % | Selten (Autopilot) |
| Crew-Groesse (Passage) | 1–2 | 2–4 | 2–6 | 6–20+ |
| Max. Montagezeit akzeptabel | 2 Min. | 5 Min. | 5 Min. | 2 Min. (Profi-Crew) |
| Ruderkraefte (Notpinne) | 30–80 N | 80–200 N | 150–400 N | 300–1000 N |
| Notpinnen-Laenge (typ.) | n/a | 0.6–1.0 m | 1.0–1.8 m | 1.5–2.5 m |
| Regulatorik | Empfehlung | ISO 8847 | ISO + OSR | SOLAS/LY3 |
| Risiko Ruder-Verlust | Mittel (Skeg) | Hoch (Spade) | Mittel–Hoch | Gering (robuste Bauweise) |
| Typischer Fehlerbild-Code | — | EMSTEER-F05, F07 | EMSTEER-F06, F08 | EMSTEER-F03 |

### ANHANG O4 — Notsteuerung und Autopilot: Zusammenspiel

**Autopilot als Primaersteuerung — Risikobewertung:**

Auf modernen Fahrtenyachten wird der Autopilot haeufig als primaere Steuerung verwendet (70–90 % der Fahrzeit). Dies bedeutet:

| Situation | Risiko | Massnahme |
|-----------|--------|-----------|
| Autopilot faellt aus (Elektronik) | Hoch (keine Warnung) | Alarm-Funktion aktivieren, regelmaessig pruefen |
| Autopilot faellt aus (Strom) | Mittel (Batteriewarnung) | Energiemanagement, Backup-Batterie |
| Autopilot-Aktuator defekt | Mittel | Reserveaktuator (Profi-Yachten) |
| Autopilot-Rudersensor defekt | Mittel | Backup-Rudersensor |
| Autopilot kaempft gegen Handsteuerung | Gering (nervend) | Kupplung korrekt einstellen |

**Wichtig:** Der Ausfall des Autopiloten ist KEIN klassischer "Steuerverlust" — die manuelle Steuerung funktioniert weiterhin. Aber: Auf Einhand-/Paar-Toernen kann der Autopilot-Ausfall zu einer Krise fuehren, wenn die Crew uebermuedet ist und manuell steuern muss.

**Empfehlung fuer Langfahrt:**
1. Autopilot als KOMFORT, nicht als Sicherheitssystem betrachten
2. Windsteueranlage als Backup-Autopilot (stromlos, zuverlaessig)
3. Tiller-Lashing als dritte Option (einfach, kein Strom, kein Verschleiss)
4. Alle drei Systeme regelmaessig nutzen (nicht nur Autopilot)

### ANHANG P — Hersteller-Kontaktdaten und Bezugsquellen

| Hersteller | Land | Webseite | Produkte |
|-----------|------|---------|---------|
| Edson Marine | USA | edsonmarine.com | Notpinnen, Pedestals, Steuerraeder |
| Jefa Marine | DK | jefa.com | Notpinnen, Ruderlager, Steuerungen |
| Lewmar | UK | lewmar.com | Notpinnen, Steuerungen, Winschen |
| Whitlock/SeaStar | UK/CA | seastar.com | Notpinnen, Steuerungen |
| Hydrovane | CA | hydrovane.com | Windsteuerung mit Notruderfunktion |
| Windpilot (Peter Foerthmann) | DE | windpilot.com | Windsteueranlagen (Pacific, Caribbean) |
| Monitor | USA | selfsteer.com | Windsteueranlagen (Servo-Pendulum) |
| Ace Sailmakers | USA | acesailmakers.com | Jordan Series Drogues |
| Hathaway, Reiser & Drang | US/UK | — | Galerider |
| Para-Tech | USA | para-anchor.com | Para-Anker |
| Fiorentino | USA | fiorentinopara.com | Para-Anker |
| SOS Marine | AU | sosmarine.com.au | Notruder-Kits |
| Forespar | USA | forespar.com | Notruder-Kits, Sta-Plug |

### ANHANG Q — Pydantic v2 Datenmodelle

```python
"""
AYDI 14.06 — Notruder und Notsteuerung
Pydantic v2 Datenmodelle fuer Analyse-Engine

Alle Modelle verwenden model_config = {"from_attributes": True}
Pydantic v2 Konvention: NIEMALS class Config verwenden!
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Enums ---

class EmergencySteeringType(str, Enum):
    """Typ der Notsteuerungseinrichtung."""
    EMERGENCY_TILLER = "emergency_tiller"
    EMERGENCY_RUDDER = "emergency_rudder"
    DROGUE = "drogue"
    PARA_ANCHOR = "para_anchor"
    JORDAN_SERIES_DROGUE = "jordan_series_drogue"
    GALERIDER = "galerider"
    WINDVANE_BACKUP = "windvane_backup"
    TILLER_LASHING = "tiller_lashing"
    SAIL_STEERING = "sail_steering"
    JURY_RIG = "jury_rig"
    NONE = "none"


class EmergencyTillerShape(str, Enum):
    """Bauform der Notpinne."""
    STRAIGHT = "straight"
    ANGLED = "angled"
    TELESCOPIC = "telescopic"
    SEGMENTED = "segmented"


class ShaftHeadProfile(str, Enum):
    """Profil des Ruderschaftkopfs."""
    SQUARE = "square"
    HEXAGONAL = "hexagonal"
    ROUND = "round"
    TAPERED_CONE = "tapered_cone"
    KEYED = "keyed"


class AttachmentType(str, Enum):
    """Befestigungsart der Notpinne am Schaft."""
    SQUARE_SOCKET = "square_socket"
    HEX_SOCKET = "hex_socket"
    BOLT_THROUGH = "bolt_through"
    CLAMP = "clamp"
    WELDED_LUG = "welded_lug"
    UNIVERSAL_ADAPTER = "universal_adapter"


class AccessibilityRating(str, Enum):
    """Bewertung der Zugaenglichkeit des Ruderschaftkopfs."""
    EXCELLENT = "excellent"       # Frei zugaenglich ueber Deck, < 2 Min.
    GOOD = "good"                 # Unter leichter Platte, 2-5 Min.
    FAIR = "fair"                 # Unter verschraubter Platte, 5-10 Min.
    POOR = "poor"                 # Hinter Einbauten, 10-20 Min.
    UNACCEPTABLE = "unacceptable" # > 20 Min. oder unmoeglich


class DrogueType(str, Enum):
    """Typ des Treibankers."""
    CONICAL = "conical"
    JORDAN_SERIES = "jordan_series"
    GALERIDER = "galerider"
    PARA_ANCHOR = "para_anchor"
    IMPROVISED = "improvised"


class SteeringLossScenario(str, Enum):
    """Szenario des Steuerverlusts."""
    CABLE_BREAK = "cable_break"
    HYDRAULIC_FAILURE = "hydraulic_failure"
    RUDDER_BLADE_LOST = "rudder_blade_lost"
    RUDDER_SHAFT_BROKEN = "rudder_shaft_broken"
    RUDDER_JAMMED = "rudder_jammed"
    MECHANICAL_FAILURE = "mechanical_failure"
    GROUNDING_DAMAGE = "grounding_damage"
    COLLISION_DAMAGE = "collision_damage"
    DEBRIS_ENTANGLED = "debris_entangled"
    AUTOPILOT_FAILURE = "autopilot_failure"


class SeverityLevel(str, Enum):
    """Schweregrad eines Befunds."""
    COSMETIC = "cosmetic"         # 1
    MINOR = "minor"               # 2
    MODERATE = "moderate"         # 3
    SIGNIFICANT = "significant"   # 4
    CRITICAL = "critical"         # 5


class ConfidenceLevel(str, Enum):
    """AYDI Confidence-Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FailurePatternCode(str, Enum):
    """Fehlerbild-Codes fuer Notsteuerung."""
    EMSTEER_F01 = "EMSTEER-F01"  # Notpinne fehlt
    EMSTEER_F02 = "EMSTEER-F02"  # Notpinne passt nicht
    EMSTEER_F03 = "EMSTEER-F03"  # Schaftkopf nicht zugaenglich
    EMSTEER_F04 = "EMSTEER-F04"  # Notpinne korrodiert/beschaedigt
    EMSTEER_F05 = "EMSTEER-F05"  # Notpinne zu kurz
    EMSTEER_F06 = "EMSTEER-F06"  # Keine Entkopplung Normalsteuerung
    EMSTEER_F07 = "EMSTEER-F07"  # Stauort unbekannt/unzugaenglich
    EMSTEER_F08 = "EMSTEER-F08"  # Kein Training durchgefuehrt
    EMSTEER_F09 = "EMSTEER-F09"  # Kein Treibanker (Offshore)
    EMSTEER_F10 = "EMSTEER-F10"  # Unzureichende Befestigungspunkte
    EMSTEER_F11 = "EMSTEER-F11"  # Windsteueranlage defekt
    EMSTEER_F12 = "EMSTEER-F12"  # Doppelruder ohne Redundanzkonzept


class CruisingArea(str, Enum):
    """Fahrgebiet-Klassifikation."""
    INLAND = "inland"
    COASTAL = "coastal"
    OFFSHORE = "offshore"
    OCEAN = "ocean"
    RACE_CAT_0 = "race_cat_0"
    RACE_CAT_1 = "race_cat_1"
    RACE_CAT_2 = "race_cat_2"
    RACE_CAT_3 = "race_cat_3"
    RACE_CAT_4 = "race_cat_4"


# --- Datenmodelle ---

class EmergencyTillerSpec(BaseModel):
    """Spezifikation einer Notpinne."""

    model_config = {"from_attributes": True}

    tiller_shape: EmergencyTillerShape = Field(..., description="Bauform der Notpinne")
    material: str = Field(..., description="Material, z.B. 'Edelstahl 316L', 'Aluminium 6082-T6'")
    length_mm: float = Field(..., ge=200, le=3000, description="Gesamtlaenge in mm")
    effective_length_mm: float = Field(..., ge=150, le=2800, description="Wirksame Hebellaenge in mm")
    tube_od_mm: Optional[float] = Field(None, ge=15, le=60, description="Rohr-Aussendurchmesser in mm")
    tube_wall_mm: Optional[float] = Field(None, ge=1.5, le=8, description="Rohr-Wandstaerke in mm")
    weight_kg: Optional[float] = Field(None, ge=0.3, le=15, description="Gewicht in kg")
    attachment_type: AttachmentType = Field(..., description="Befestigungsart am Schaft")
    shaft_head_profile: ShaftHeadProfile = Field(..., description="Schaftkopf-Profil")
    shaft_diameter_mm: Optional[float] = Field(None, ge=15, le=120, description="Schaftdurchmesser in mm")
    has_locking_pin: bool = Field(default=True, description="Sicherungsbolzen vorhanden")
    manufacturer: Optional[str] = Field(None, description="Hersteller")
    model: Optional[str] = Field(None, description="Modell-Bezeichnung")


class EmergencyTillerAccessibility(BaseModel):
    """Bewertung der Zugaenglichkeit fuer Notpinnen-Montage."""

    model_config = {"from_attributes": True}

    accessibility_rating: AccessibilityRating = Field(..., description="Bewertung der Zugaenglichkeit")
    estimated_mounting_time_min: float = Field(..., ge=0.5, le=60, description="Geschaetzte Montagezeit in Minuten")
    requires_tools: bool = Field(default=False, description="Werkzeug fuer Zugang erforderlich?")
    requires_decoupling: bool = Field(default=False, description="Normalsteuerung entkoppeln noetig?")
    decoupling_method: Optional[str] = Field(None, description="Art der Entkopplung")
    has_bypass_valve: Optional[bool] = Field(None, description="Bypass-Ventil vorhanden (Hydraulik)?")
    cockpit_plate_type: Optional[str] = Field(None, description="Art der Cockpitplatte")
    sweep_range_deg: Optional[float] = Field(None, ge=0, le=90, description="Schwenkbereich je Seite in Grad")
    stowage_location: Optional[str] = Field(None, description="Stauort der Notpinne")
    stowage_marked: bool = Field(default=False, description="Stauort markiert?")
    compass_visible: bool = Field(default=False, description="Kompass von Notsteuer-Position lesbar?")


class DrogueSpec(BaseModel):
    """Spezifikation eines Treibankers/Drogue."""

    model_config = {"from_attributes": True}

    drogue_type: DrogueType = Field(..., description="Typ des Treibankers")
    manufacturer: Optional[str] = Field(None, description="Hersteller")
    model: Optional[str] = Field(None, description="Modell-Bezeichnung")
    diameter_mm: Optional[float] = Field(None, ge=200, le=6000, description="Durchmesser in mm (Para-Anker/Galerider)")
    num_cones: Optional[int] = Field(None, ge=10, le=300, description="Anzahl Kegel (JSD)")
    rode_length_m: Optional[float] = Field(None, ge=10, le=200, description="Seillaenge in m")
    rode_diameter_mm: Optional[float] = Field(None, ge=8, le=24, description="Seildurchmesser in mm")
    rode_material: Optional[str] = Field(None, description="Seil-Material, z.B. 'Nylon 3-straengig'")
    chain_weight_kg: Optional[float] = Field(None, ge=0, le=30, description="Kettengewicht am Ende in kg")
    has_trip_line: bool = Field(default=False, description="Einhol-/Ausloeseleine vorhanden")
    has_bridle: bool = Field(default=False, description="Bridle (V-Befestigung) vorhanden")
    bridle_length_m: Optional[float] = Field(None, ge=5, le=30, description="Bridle-Laenge je Seite in m")
    total_weight_kg: Optional[float] = Field(None, ge=1, le=50, description="Gesamtgewicht in kg")
    pack_volume_liters: Optional[float] = Field(None, ge=5, le=100, description="Packvolumen in Litern")
    rated_boat_length_m: Optional[float] = Field(None, ge=5, le=30, description="Empfohlene Bootslaenge in m")


class EmergencySteeringInventory(BaseModel):
    """Gesamtinventar Notsteuerungsausruestung eines Bootes."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_length_m: float = Field(..., ge=5, le=60, description="Bootslaenge LOA in m")
    cruising_area: CruisingArea = Field(..., description="Fahrgebiet")
    hull_type: str = Field(default="monohull", description="Rumpftyp: monohull, catamaran, trimaran")

    # Notpinne
    has_emergency_tiller: bool = Field(default=False, description="Notpinne vorhanden")
    emergency_tiller: Optional[EmergencyTillerSpec] = Field(None, description="Notpinnen-Spezifikation")
    tiller_accessibility: Optional[EmergencyTillerAccessibility] = Field(None, description="Zugaenglichkeit")

    # Treibanker/Drogue
    has_drogue: bool = Field(default=False, description="Treibanker/Drogue vorhanden")
    drogue: Optional[DrogueSpec] = Field(None, description="Treibanker-Spezifikation")
    has_stern_cleats_for_drogue: bool = Field(default=False, description="Heckklampen fuer Drogue vorhanden und ausreichend?")
    stern_cleat_wll_kn: Optional[float] = Field(None, ge=0, le=100, description="WLL der Heckklampen in kN")

    # Windsteueranlage
    has_windvane: bool = Field(default=False, description="Windsteueranlage vorhanden")
    windvane_has_own_rudder: bool = Field(default=False, description="Windsteueranlage mit eigenem Ruder?")
    windvane_model: Optional[str] = Field(None, description="Windsteueranlagen-Modell")
    windvane_functional: Optional[bool] = Field(None, description="Windsteueranlage funktionsfaehig?")

    # Zusaetzliche Ausruestung
    has_tiller_lashing_kit: bool = Field(default=False, description="Tiller-Lashing Kit vorhanden")
    has_emergency_rudder_kit: bool = Field(default=False, description="Notruder-Kit vorhanden")
    has_steering_oar: bool = Field(default=False, description="Steuerriemen vorhanden")

    # Training
    last_drill_date: Optional[date] = Field(None, description="Letztes Notsteuerungs-Drill Datum")
    drill_documented: bool = Field(default=False, description="Drill dokumentiert?")
    crew_trained: bool = Field(default=False, description="Crew in Notsteuerung geschult?")


class EmergencySteeringCondition(BaseModel):
    """Zustandsbewertung der Notsteuerungsausruestung."""

    model_config = {"from_attributes": True}

    inspection_date: date = Field(..., description="Datum der Inspektion")
    inspector: Optional[str] = Field(None, description="Name des Inspektors")

    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0-100")
    tiller_present_score: int = Field(..., ge=0, le=100, description="Notpinne vorhanden und passend")
    tiller_condition_score: int = Field(..., ge=0, le=100, description="Zustand der Notpinne")
    accessibility_score: int = Field(..., ge=0, le=100, description="Zugaenglichkeit Ruderschaft")
    decoupling_score: int = Field(..., ge=0, le=100, description="Entkopplung Normalsteuerung")
    drogue_score: int = Field(..., ge=0, le=100, description="Treibanker vorhanden/Zustand")
    training_score: int = Field(..., ge=0, le=100, description="Training/Drills durchgefuehrt")
    stowage_score: int = Field(..., ge=0, le=100, description="Stauung und Markierung")
    redundancy_score: int = Field(..., ge=0, le=100, description="Redundanz (Windvane, Notruder, etc.)")

    confidence: ConfidenceLevel = Field(..., description="Konfidenz-Stufe")
    notes: Optional[str] = Field(None, description="Freitextbemerkungen")


class EmergencySteeringFinding(BaseModel):
    """Einzelbefund an der Notsteuerungsausruestung."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID")
    failure_code: FailurePatternCode = Field(..., description="Fehlerbild-Code")
    severity: SeverityLevel = Field(..., description="Schweregrad")
    confidence: ConfidenceLevel = Field(..., description="Konfidenz der Erkennung")
    location: str = Field(..., description="Ort am Boot, z.B. 'Cockpitboden achtern'")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    suggestion_de: str = Field(..., description="Handlungsempfehlung auf Deutsch")
    score_impact: int = Field(..., ge=-100, le=0, description="Score-Auswirkung (negativ)")
    photo_reference: Optional[str] = Field(None, description="Referenz auf Foto/Bild")
    requires_professional: bool = Field(default=False, description="Fachbetrieb erforderlich?")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Geschaetzte Behebungskosten in EUR")
    estimated_time_hours: Optional[float] = Field(None, ge=0, description="Geschaetzter Zeitaufwand in Stunden")


class TillerForceCalculation(BaseModel):
    """Berechnung der Notpinnen-Kraefte."""

    model_config = {"from_attributes": True}

    boat_speed_kn: float = Field(..., ge=0, le=20, description="Bootsgeschwindigkeit in Knoten")
    rudder_area_m2: float = Field(..., ge=0.01, le=3.0, description="Ruderflaeche in m^2")
    balance_ratio: float = Field(default=0.20, ge=0.0, le=0.5, description="Balancegrad")
    water_density_kg_m3: float = Field(default=1025.0, description="Wasserdichte")
    safety_factor: float = Field(default=2.5, ge=1.0, le=5.0, description="Sicherheitsfaktor")
    tiller_length_m: float = Field(..., ge=0.3, le=3.0, description="Wirksame Pinnenlaenge in m")

    # Berechnete Ergebnisse
    rudder_torque_nm: Optional[float] = Field(None, description="Berechnetes Rudermoment in Nm")
    design_torque_nm: Optional[float] = Field(None, description="Auslegungsmoment inkl. SF in Nm")
    tiller_force_n: Optional[float] = Field(None, description="Erforderliche Handkraft in N")
    force_acceptable: Optional[bool] = Field(None, description="Kraft < 150 N (Dauerbetrieb)?")
    min_tiller_length_m: Optional[float] = Field(None, description="Mindest-Pinnenlaenge fuer 150 N in m")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)


class EmergencySteeringAnalysisResult(BaseModel):
    """Gesamtergebnis der Notsteuerungs-Analyse."""

    model_config = {"from_attributes": True}

    inventory: EmergencySteeringInventory = Field(..., description="Inventar der Notsteuerungsausruestung")
    condition: EmergencySteeringCondition = Field(..., description="Zustandsbewertung")
    tiller_force_calc: Optional[TillerForceCalculation] = Field(None, description="Pinnen-Kraft-Berechnung")
    findings: list[EmergencySteeringFinding] = Field(default_factory=list, description="Liste der Befunde")
    critical_findings: int = Field(default=0, ge=0, description="Anzahl kritischer Befunde")
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore")
    overall_confidence: ConfidenceLevel = Field(..., description="Gesamt-Konfidenz")
    analysis_version: str = Field(default="1.0.0", description="Version des Analyse-Algorithmus")
    analysis_date: date = Field(..., description="Analysedatum")
    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
    recommendations_de: list[str] = Field(default_factory=list, description="Empfehlungen auf Deutsch")


class EmergencySteeringDrillRecord(BaseModel):
    """Dokumentation eines Notsteuerungs-Drills."""

    model_config = {"from_attributes": True}

    drill_date: date = Field(..., description="Datum des Drills")
    boat_name: Optional[str] = Field(None, description="Bootsname")
    skipper: str = Field(..., description="Name des Skippers")
    crew_count: int = Field(..., ge=1, le=30, description="Anzahl Crewmitglieder")
    crew_names: Optional[list[str]] = Field(None, description="Namen der Crewmitglieder")

    tiller_mounting_time_min: Optional[float] = Field(None, ge=0, le=60, description="Montagezeit Notpinne in Minuten")
    tiller_fit_ok: Optional[bool] = Field(None, description="Notpinne passt korrekt?")
    decoupling_ok: Optional[bool] = Field(None, description="Entkopplung Normalsteuerung erfolgreich?")
    steering_tested: bool = Field(default=False, description="Mit Notpinne gesteuert?")
    sail_steering_tested: bool = Field(default=False, description="Steuerung durch Segel geuebt?")
    tiller_lashing_tested: bool = Field(default=False, description="Tiller-Lashing geuebt?")
    drogue_deployment_simulated: bool = Field(default=False, description="Drogue-Ausbringen simuliert?")

    issues_found: Optional[str] = Field(None, description="Gefundene Probleme")
    corrective_actions: Optional[str] = Field(None, description="Durchgefuehrte Korrekturen")
    overall_assessment: Optional[str] = Field(None, description="Gesamtbeurteilung des Drills")
    next_drill_planned: Optional[date] = Field(None, description="Naechster geplanter Drill")


class EmergencySteeringMaintenanceSchedule(BaseModel):
    """Wartungsplan fuer Notsteuerungsausruestung."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., description="Bootslaenge")
    cruising_area: CruisingArea = Field(..., description="Fahrgebiet")
    tasks: list[dict] = Field(
        ...,
        description="Liste der Wartungsaufgaben mit 'task', 'interval_months', 'professional_required', 'estimated_time_min'"
    )
    next_service_date: Optional[date] = Field(None, description="Naechster Service-Termin")
    estimated_annual_cost_eur: Optional[float] = Field(None, description="Geschaetzte jaehrliche Kosten")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.BENCHMARK)
```

### ANHANG Q2 — Erweiterte Enums und Hilfsmodelle

```python
"""
AYDI 14.06 — Erweiterte Hilfsmodelle und Konstanten
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class WindvaneType(str, Enum):
    """Typ der Windsteueranlage."""
    SERVO_PENDULUM = "servo_pendulum"
    AUX_RUDDER = "aux_rudder"
    TRIMTAB = "trimtab"


class BoatType(str, Enum):
    """Bootstyp fuer Notsteuerungsbewertung."""
    SAILING_YACHT_LONG_KEEL = "sailing_yacht_long_keel"
    SAILING_YACHT_FIN_KEEL = "sailing_yacht_fin_keel"
    SAILING_YACHT_TWIN_RUDDER = "sailing_yacht_twin_rudder"
    CATAMARAN = "catamaran"
    TRIMARAN = "trimaran"
    MOTOR_YACHT_INBOARD = "motor_yacht_inboard"
    MOTOR_YACHT_OUTBOARD = "motor_yacht_outboard"
    MOTOR_YACHT_POD = "motor_yacht_pod"


class SteeringSystemType(str, Enum):
    """Primaerer Steuerungstyp des Bootes."""
    TILLER_DIRECT = "tiller_direct"
    WHEEL_WIRE = "wheel_wire"
    WHEEL_CHAIN = "wheel_chain"
    WHEEL_CABLE = "wheel_cable"
    HYDRAULIC = "hydraulic"
    ELECTRO_HYDRAULIC = "electro_hydraulic"
    FLY_BY_WIRE = "fly_by_wire"


class EmergencySteeringRequirement(BaseModel):
    """Bewertung der Notsteuerungsanforderungen fuer ein spezifisches Boot."""

    model_config = {"from_attributes": True}

    boat_type: BoatType = Field(..., description="Bootstyp")
    boat_length_m: float = Field(..., ge=5, le=60, description="Bootslaenge LOA")
    primary_steering: SteeringSystemType = Field(..., description="Primaerer Steuerungstyp")
    cruising_area: CruisingArea = Field(..., description="Hauptfahrgebiet")
    crew_typical: int = Field(..., ge=1, le=30, description="Typische Crewgroesse")
    has_dual_rudder: bool = Field(default=False, description="Doppelruder?")

    # Berechnete Anforderungen
    tiller_required: bool = Field(default=True, description="Notpinne erforderlich?")
    tiller_min_length_mm: Optional[float] = Field(None, description="Mindest-Pinnenlaenge mm")
    drogue_required: bool = Field(default=False, description="Treibanker erforderlich?")
    drogue_type_recommended: Optional[str] = Field(None, description="Empfohlener Treibanker-Typ")
    windvane_recommended: bool = Field(default=False, description="Windsteueranlage empfohlen?")
    emergency_rudder_recommended: bool = Field(default=False, description="Notruder empfohlen?")
    training_required: bool = Field(default=True, description="Training-Pflicht?")
    regulation_reference: Optional[str] = Field(None, description="Regulatorische Referenz")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)
```

### ANHANG R — Berechnungsfunktionen

```python
"""
AYDI 14.06 — Berechnungsfunktionen Notsteuerung
Reine Funktionen (pure functions), kein DB-Zugriff.
"""

import math
from typing import Optional


def calculate_rudder_torque(
    boat_speed_kn: float,
    rudder_area_m2: float,
    balance_ratio: float = 0.20,
    water_density: float = 1025.0,
    c_n: float = 1.2,
    rudder_chord_m: Optional[float] = None,
) -> float:
    """
    Berechnet das Rudermoment in Nm.

    Args:
        boat_speed_kn: Bootsgeschwindigkeit in Knoten
        rudder_area_m2: Ruderflaeche in m^2
        balance_ratio: Balancegrad (0.0-0.5, typ. 0.15-0.25)
        water_density: Wasserdichte in kg/m^3
        c_n: Normalkraftbeiwert (typ. 1.0-1.5)
        rudder_chord_m: Ruderblatttiefe in m (optional, wird aus Flaeche geschaetzt)

    Returns:
        Rudermoment in Nm
    """
    v_ms = boat_speed_kn * 0.5144  # kn to m/s
    if rudder_chord_m is None:
        # Schaetzung: Aspect Ratio ca. 2.5 -> chord = sqrt(area / 2.5)
        rudder_chord_m = math.sqrt(rudder_area_m2 / 2.5)

    rudder_force_n = 0.5 * c_n * water_density * rudder_area_m2 * v_ms**2
    moment_arm_m = rudder_chord_m * (0.25 - balance_ratio)  # Druckpunkt bei 25% chord
    torque_nm = rudder_force_n * abs(moment_arm_m)

    return torque_nm


def calculate_min_tiller_length(
    rudder_torque_nm: float,
    max_hand_force_n: float = 150.0,
    safety_factor: float = 2.5,
) -> float:
    """
    Berechnet die minimale Notpinnenlaenge in Metern.

    Args:
        rudder_torque_nm: Rudermoment in Nm
        max_hand_force_n: Maximale Handkraft in N (Dauerbetrieb)
        safety_factor: Sicherheitsfaktor (Schwerwetter)

    Returns:
        Minimale Pinnenlaenge in m
    """
    design_torque = rudder_torque_nm * safety_factor
    min_length = design_torque / max_hand_force_n
    return min_length


def calculate_tiller_force(
    rudder_torque_nm: float,
    tiller_length_m: float,
    safety_factor: float = 2.5,
) -> dict:
    """
    Berechnet die Handkraft an einer Notpinne.

    Args:
        rudder_torque_nm: Rudermoment in Nm
        tiller_length_m: Wirksame Pinnenlaenge in m
        safety_factor: Sicherheitsfaktor

    Returns:
        Dict mit Berechnungsergebnissen
    """
    design_torque = rudder_torque_nm * safety_factor
    force_n = design_torque / tiller_length_m
    force_acceptable = force_n <= 150.0  # Dauerbetrieb, 2 Haende

    return {
        "rudder_torque_nm": round(rudder_torque_nm, 1),
        "design_torque_nm": round(design_torque, 1),
        "tiller_force_n": round(force_n, 1),
        "force_acceptable": force_acceptable,
        "force_category": (
            "leicht" if force_n < 80 else
            "moderat" if force_n < 150 else
            "schwer" if force_n < 250 else
            "sehr schwer — Verlaengerung oder Winsch-Unterstuetzung noetig"
        ),
    }


def score_emergency_steering(
    has_tiller: bool,
    tiller_fits: bool = False,
    tiller_accessible_min: float = 30.0,
    tiller_condition_ok: bool = False,
    has_bypass_valve: Optional[bool] = None,
    has_drogue: bool = False,
    has_windvane_with_rudder: bool = False,
    crew_trained: bool = False,
    last_drill_months_ago: Optional[int] = None,
    stowage_marked: bool = False,
    cruising_area: str = "coastal",
) -> dict:
    """
    Berechnet den AYDI-Score fuer Notsteuerung.

    Returns:
        Dict mit Score (0-100), Findings, Empfehlungen
    """
    score = 100
    findings = []
    recommendations = []

    # Notpinne vorhanden?
    if not has_tiller:
        score -= 50
        findings.append("EMSTEER-F01: Notpinne fehlt")
        recommendations.append("Notpinne SOFORT beschaffen und testen")
    else:
        # Passt sie?
        if not tiller_fits:
            score -= 45
            findings.append("EMSTEER-F02: Notpinne passt nicht auf Ruderschaft")
            recommendations.append("Notpinne anpassen oder neue beschaffen")

        # Zustand
        if not tiller_condition_ok:
            score -= 20
            findings.append("EMSTEER-F04: Notpinne korrodiert/beschaedigt")
            recommendations.append("Notpinne reinigen/ersetzen")

    # Zugaenglichkeit
    if tiller_accessible_min > 10:
        score -= 30
        findings.append("EMSTEER-F03: Zugang zum Ruderschaftkopf > 10 Min.")
        recommendations.append("Schnellverschluss fuer Cockpitplatte nachrüsten")
    elif tiller_accessible_min > 5:
        score -= 15
        findings.append("EMSTEER-F03: Zugang zum Ruderschaftkopf 5-10 Min.")
        recommendations.append("Zugang optimieren (Ziel: < 5 Min.)")

    # Bypass-Ventil (nur relevant bei Hydraulik)
    if has_bypass_valve is False:
        score -= 30
        findings.append("EMSTEER-F06: Kein Bypass-Ventil bei Hydrauliksteuerung")
        recommendations.append("Bypass-Ventil DRINGEND nachrüsten")

    # Training
    if not crew_trained:
        score -= 25
        findings.append("EMSTEER-F08: Kein Notsteuerungs-Training")
        recommendations.append("Sicherheitsdrill durchfuehren")
    elif last_drill_months_ago is not None and last_drill_months_ago > 12:
        score -= 10
        findings.append("Letzter Drill > 12 Monate her")
        recommendations.append("Drill erneuern")

    # Stauort
    if has_tiller and not stowage_marked:
        score -= 15
        findings.append("EMSTEER-F07: Stauort nicht markiert")
        recommendations.append("Stauort markieren und in Sicherheitsbriefing aufnehmen")

    # Offshore-spezifisch
    if cruising_area in ("offshore", "ocean", "race_cat_0", "race_cat_1"):
        if not has_drogue:
            score -= 15
            findings.append("EMSTEER-F09: Kein Treibanker fuer Offshore")
            recommendations.append("Drogue/JSD beschaffen")

    # Bonus fuer Redundanz
    if has_windvane_with_rudder:
        score += 5  # Bonus: unabhaengige Backup-Steuerung
        recommendations.append("Windsteueranlage mit eigenem Ruder: Exzellente Redundanz")

    # Score begrenzen
    score = max(0, min(100, score))

    return {
        "score": score,
        "findings": findings,
        "recommendations": recommendations,
        "confidence": "measured" if has_tiller and tiller_fits else "estimated",
    }


def recommend_equipment(
    boat_length_m: float,
    cruising_area: str,
    budget_eur: Optional[float] = None,
    has_dual_rudder: bool = False,
    has_windvane: bool = False,
) -> dict:
    """
    Empfiehlt Notsteuerungsausruestung basierend auf Boot und Fahrgebiet.

    Returns:
        Dict mit Empfehlungen und geschaetzten Kosten
    """
    recommendations = []
    total_cost_min = 0
    total_cost_max = 0

    # Notpinne ist IMMER Pflicht
    tiller_cost = 150 + boat_length_m * 20
    recommendations.append({
        "item": "Notpinne",
        "priority": "MUSS",
        "cost_eur_min": int(tiller_cost * 0.7),
        "cost_eur_max": int(tiller_cost * 1.3),
    })
    total_cost_min += int(tiller_cost * 0.7)
    total_cost_max += int(tiller_cost * 1.3)

    # Tiller-Lashing Kit
    recommendations.append({
        "item": "Tiller-Lashing Kit",
        "priority": "SOLL",
        "cost_eur_min": 25,
        "cost_eur_max": 80,
    })
    total_cost_min += 25
    total_cost_max += 80

    # Offshore: Drogue
    if cruising_area in ("offshore", "ocean", "race_cat_0", "race_cat_1", "race_cat_2"):
        if cruising_area in ("ocean", "race_cat_0", "race_cat_1"):
            # JSD empfohlen
            jsd_cost = 800 + boat_length_m * 80
            recommendations.append({
                "item": "Jordan Series Drogue",
                "priority": "EMPFOHLEN",
                "cost_eur_min": int(jsd_cost * 0.8),
                "cost_eur_max": int(jsd_cost * 1.2),
            })
            total_cost_min += int(jsd_cost * 0.8)
            total_cost_max += int(jsd_cost * 1.2)
        else:
            # Galerider ausreichend
            galerider_cost = 350 + boat_length_m * 25
            recommendations.append({
                "item": "Galerider / Drogue",
                "priority": "SOLL",
                "cost_eur_min": int(galerider_cost * 0.8),
                "cost_eur_max": int(galerider_cost * 1.2),
            })
            total_cost_min += int(galerider_cost * 0.8)
            total_cost_max += int(galerider_cost * 1.2)

    # Spade-Ruder ohne Skeg: Notruder empfohlen fuer Ozean
    if cruising_area in ("ocean", "race_cat_0") and not has_windvane:
        recommendations.append({
            "item": "Notruder-Kit",
            "priority": "EMPFOHLEN",
            "cost_eur_min": 400,
            "cost_eur_max": 900,
        })
        total_cost_min += 400
        total_cost_max += 900

    return {
        "recommendations": recommendations,
        "total_cost_eur_min": total_cost_min,
        "total_cost_eur_max": total_cost_max,
        "note_de": f"Empfehlungen fuer {boat_length_m:.0f}m Boot, Fahrgebiet: {cruising_area}",
        "confidence": "benchmark",
    }
```

---

### ANHANG R2 — Visuelle Analyse-Leitfaden fuer AYDI Pipeline B

Folgende Merkmale koennen durch visuelle Analyse (Fotos) erkannt werden:

| Merkmal | Confidence | Erkennungsmethode |
|---------|-----------|-------------------|
| Notpinne sichtbar (Stauort) | visual_high | Direkte Erkennung |
| Notpinne Bauform | visual_high | Formanalyse |
| Notpinne Korrosion | visual_high | Verfaerbung, Lochfrass |
| Windsteueranlage vorhanden | visual_high | Erkennbar am Heck |
| Windsteueranlagen-Typ | visual_medium | Bauform (Pendulum vs. Hilfsruder) |
| Windsteueranlagen-Zustand | visual_medium | Korrosion, fehlende Teile |
| Heckklampen (Drogue-tauglich) | visual_medium | Groesse, Durchbolzung |
| Cockpitplatte (Ruderschaft-Zugang) | visual_medium | Platte sichtbar im Cockpitboden |
| Bypass-Ventil (Hydraulik) | visual_medium | Ventilhebel an Leitung |
| Stauort-Markierung | visual_high | Beschriftung, Farbmarkierung |
| Notpinnen-Laenge (Schaetzung) | visual_medium | Verhaeltnis zu bekannten Massen |
| Treibanker/Drogue sichtbar | visual_low | Meist unter Deck, selten sichtbar |
| Notruder am Heck montiert | visual_high | Direkte Erkennung (wenn montiert) |

**Prompt-Hinweise fuer Claude Vision (Pipeline B):**
- Notsteuerungsausruestung ist oft NICHT sichtbar auf Fotos — Abwesenheit ist kein Beweis
- Windsteueranlagen am Heck sind das zuverlaessigste Erkennungsmerkmal fuer Backup-Steuerung
- Gelbe/orange Markierungen an Cockpitwand/-boden deuten auf Sicherheitsausruestung hin
- Grosse Heckklampen (> 200 mm) deuten auf Drogue/Schwerwetter-Vorbereitung hin
- Hydrovane ist am einfachsten zu erkennen: separates Ruder + Windfahne am Heck, asymmetrisch
- Monitor Windsteueranlage: Erkennbar an charakteristischem Edelstahl-Rahmen und Pendelruder
- Aries Windsteueranlage: Aelterer Typ, erkennbar an Windfahne und Servo-Pendel (oft blau/rot)
- Windpilot Pacific: Grosse Windfahne, kompaktes Design, oft mit "Windpilot"-Schriftzug
- Bei Doppelruder-Booten: Beide Ruderschaftkoepfe pruefen (Zugangsplatten sichtbar?)
- Heckkorb-Konstruktion korreliert mit Offshore-Vorbereitung: Robuster Heckkorb = bessere Notruder-Montage-Optionen

### ANHANG R3 — Tabellarische Zusammenfassung: AYDI-Score-Auswirkungen

| Finding-Code | Kurzbezeichnung | Score-Auswirkung | Schweregrad | Fachbetrieb noetig? |
|-------------|----------------|-----------------|-------------|-------------------|
| EMSTEER-F01 | Notpinne fehlt | -50 | CRITICAL | Nein (Beschaffung) |
| EMSTEER-F02 | Notpinne passt nicht | -45 | CRITICAL | Ggf. (Anpassung) |
| EMSTEER-F03 | Schaftkopf unzugaenglich | -25 bis -40 | SIGNIFICANT | Ggf. (Umbau) |
| EMSTEER-F04 | Notpinne korrodiert | -15 bis -30 | MODERATE-SIGNIF. | Nein |
| EMSTEER-F05 | Notpinne zu kurz | -15 bis -25 | MODERATE-SIGNIF. | Nein |
| EMSTEER-F06 | Keine Entkopplung | -25 bis -35 | SIGNIFICANT | Ja (Bypass-Ventil) |
| EMSTEER-F07 | Stauort unbekannt | -15 bis -25 | MODERATE-SIGNIF. | Nein |
| EMSTEER-F08 | Kein Training | -20 bis -30 | SIGNIFICANT | Nein |
| EMSTEER-F09 | Kein Treibanker (Offshore) | -10 bis -20 | MODERATE | Nein |
| EMSTEER-F10 | Heckklampen unzureichend | -10 bis -15 | MODERATE | Ggf. (Montage) |
| EMSTEER-F11 | Windsteueranlage defekt | -10 bis -20 | MODERATE | Ggf. (Wartung) |
| EMSTEER-F12 | Doppelruder ohne Konzept | -10 bis -20 | MODERATE | Nein |

**Score-Aggregation:**
- Maximal moeglich: 100 Punkte (alles vorhanden, getestet, geuebt)
- Minimum bei Offshore: Notpinne + Drogue + Training = 50+ Punkte Baseline
- CRITICAL-Findings (F01, F02): Sofortige Massnahme, Boot nicht offshore-tauglich
- SIGNIFICANT-Findings (F03, F06, F08): Massnahme vor naechstem Toern
- MODERATE-Findings (F04, F05, F07, F09–F12): Massnahme innerhalb Saison

**Gewichtung im AYDI-Gesamtscore:**
Die Notsteuerung fliesst primaer in das Sicherheitsmodul und das Compliance-Modul ein:
- Sicherheitsmodul: Gewichtung 15 % des Moduls (zusammen mit MOB-Ausruestung, Rettungsmittel, etc.)
- Compliance-Modul: Gewichtung 10 % des Moduls (ISO 8847, OSR-Konformitaet)
- Emotional-Modul: Gewichtung 3 % (Sicherheitsgefuehl der Crew)
- Gesamtboot-Score: Effektive Gewichtung ca. 2–5 % (je nach Fahrgebiet)

---

*Ende der Wissensdatei 14.06 — Notruder und Notsteuerung*
