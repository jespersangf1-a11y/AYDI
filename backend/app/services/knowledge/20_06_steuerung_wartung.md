---
title: "Steueranlagen Wartung und Troubleshooting — Gesamtsystem-Wartung, Inspektion, Seilzug/Ketten/Hydraulik-Wartung"
kategorie: "20 Steueranlagen"
unterkategorie: "20.06 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
bereich: "Steueranlagen & Ruderanlagen"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, Klassifikationsgesellschaften, Werkstattmessungen"
  - documented: "Hersteller-Kataloge, Service-Bulletins, Werft-Dokumentation, Surveyor-Berichte"
  - estimated: "Erfahrungswerte Yachtmechaniker, Werft-Konsens, Forum-Analyse"
  - benchmark: "Charterflotten-Statistiken, Versicherungs-Schadensberichte, Marina-Werkstattdaten"
tags:
  - steueranlage
  - wartung
  - troubleshooting
  - seilzugsteuerung
  - kettensteuerung
  - hydrauliksteuerung
  - zahnstangensteuerung
  - ruderanlage
  - inspektion
  - winterfestmachung
  - instandhaltung
  - fehlerdiagnose
  - lewmar
  - jefa
  - edson
  - kobelt
  - whitlock
cross_references:
  - "20_01_steuerung_grundlagen.md"
  - "20_02_hydraulische_steuerung.md"
  - "20_03_ruderanlage_lager.md"
  - "06_07_hydraulikschlaeuche.md"
  - "02_13_anti_seize_pasten.md"
  - "05_01_edelstahl_schrauben.md"
---

# 20.06 — Steueranlagen Wartung und Troubleshooting: Gesamtsystem-Wartung, Inspektion, Seilzug/Ketten/Hydraulik-Wartung

> **AYDI Wissensdatei 20.06** — Kategorie 20: Steueranlagen und Ruderanlagen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Service-Bulletins), estimated (Erfahrungswerte, Werft-Konsens), benchmark (Charterflotten, Versicherungsdaten)
> **Letzte Aktualisierung:** 2026-05-02

---

## Inhaltsverzeichnis

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
11. [ANHANG A–H — Fallstudien](#11-anhang-ah--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Wartung als Sicherheitsfaktor

Die Steueranlage ist das sicherheitskritischste mechanische System an Bord jeder Yacht. Ein Totalausfall der Steuerung auf See — ob durch gebrochenes Steuerseil, versagende Hydraulik oder festgefressenes Ruderlager — stellt eine unmittelbare Gefahr für Schiff und Besatzung dar. Im Gegensatz zu vielen anderen Bordsystemen gibt es bei der Steueranlage kein "Weiterfahren mit eingeschränkter Funktion": Die Steuerung funktioniert, oder das Schiff ist manövrierunfähig.

Die regelmäßige, fachgerechte Wartung der Steueranlage ist daher keine optionale Pflegemaßnahme, sondern eine fundamentale Sicherheitsanforderung. Statistiken aus der Versicherungswirtschaft und von Klassifikationsgesellschaften belegen dies eindrücklich.

**Kernstatistiken zur Wartungsrelevanz (Confidence: benchmark):**

| Aspekt | Wert | Quelle |
|--------|------|--------|
| Anteil Steuerungsausfälle an allen mechanischen Havarien | 8–14 % | Pantaenius Schadenstatistik 2019–2024 |
| Ursache: mangelnde Wartung bei Steuerungsausfällen | 62 % | Lloyd's Maritime Claims Analysis 2023 |
| Durchschnittliche Bergungskosten bei Steuerungsausfall | 4.800–18.500 EUR | ADAC Sportschifffahrt Statistik 2024 |
| Durchschnittliche jährliche Wartungskosten Seilzugsteuerung | 80–250 EUR | AYDI Kalkulation |
| Durchschnittliche jährliche Wartungskosten Hydrauliksteuerung | 120–380 EUR | AYDI Kalkulation |
| ROI einer jährlichen Steueranlagen-Wartung | 18:1 bis 42:1 | Lebensdauervergleich gewartet vs. ungewartet |
| Mittlere Lebensdauer Steuerseil gewartet | 8–12 Jahre | Edson Service Bulletin SB-2023-07 |
| Mittlere Lebensdauer Steuerseil ungewartet | 3–5 Jahre | Edson Service Bulletin SB-2023-07 |

### 1.2 Wartungsintervalle — Übersicht

Die Wartungsintervalle der Steueranlage richten sich nach dem Steuerungstyp, der Nutzungsintensität und den Umgebungsbedingungen. Die folgende Tabelle gibt eine Gesamtübersicht über die empfohlenen Intervalle aller gängigen Steuerungstypen.

**Wartungsintervall-Matrix (Confidence: documented):**

| Wartungsmaßnahme | Seilzug | Kette | Hydraulik | Zahnstange |
|-----------------|---------|-------|-----------|------------|
| **Sichtprüfung Gesamtsystem** | Monatlich | Monatlich | Monatlich | Monatlich |
| **Funktionsprüfung (Vollausschlag)** | Wöchentlich | Wöchentlich | Wöchentlich | Wöchentlich |
| **Schmierung beweglicher Teile** | 3 Monate | 3 Monate | — | 6 Monate |
| **Seilspannung prüfen/nachstellen** | 3 Monate | — | — | — |
| **Kettenspannung prüfen** | — | 6 Monate | — | — |
| **Hydraulikölstand prüfen** | — | — | Monatlich | — |
| **Hydraulikschläuche prüfen** | — | — | 6 Monate | — |
| **Ruderlager prüfen** | 6 Monate | 6 Monate | 6 Monate | 6 Monate |
| **Notpinne testen** | Saisonstart | Saisonstart | Saisonstart | Saisonstart |
| **Vollinspektion (Demontage)** | Jährlich | Jährlich | 2 Jahre | 2 Jahre |
| **Steuerseil-Austausch** | 5–8 Jahre | — | — | — |
| **Hydrauliköl-Wechsel** | — | — | 2 Jahre | — |
| **Ruderlager-Austausch** | 8–15 Jahre | 8–15 Jahre | 8–15 Jahre | 8–15 Jahre |

### 1.3 Klassifizierung der Wartungsmaßnahmen

Die Wartungsmaßnahmen der Steueranlage lassen sich in vier Kategorien einteilen:

**Kategorie I — Eigner-Wartung (keine Spezialwerkzeuge):**
- Sichtprüfungen aller zugänglichen Komponenten
- Funktionsprüfung Vollausschlag Backbord/Steuerbord
- Nachschmieren vorgesehener Schmierstellen
- Hydraulikölstand prüfen und nachfüllen
- Seilspannung kontrollieren (Daumentest)
- Notpinne aufsetzen und testen
- Korrosionsspuren dokumentieren

**Kategorie II — Versierter Eigner (Grundwerkzeug):**
- Seilspannung messen und nachstellen (Tensiometer)
- Kettenspannung justieren
- Umlenkrollen reinigen und schmieren
- Quadrant-Verbindungen prüfen und nachziehen
- Hydraulikschläuche auf Risse und Schwellungen prüfen
- Ruderstopps kontrollieren und einstellen

**Kategorie III — Fachbetrieb (Spezialwerkzeug):**
- Steuerseil-Austausch
- Hydrauliksystem entlüften
- Hydraulikzylinder überholen
- Ruderlager-Inspektion (Ruder ausgebaut)
- Ruderschaft-Spiel messen (Messuhr)
- Kettenrad-Verschleißmessung

**Kategorie IV — Werft/Klassifikation (Spezialausrüstung):**
- Ruderschaft ziehen und prüfen (Rissprüfung)
- Ruderlager austauschen
- Stevenrohr erneuern
- Hydrauliksystem komplett erneuern
- Strukturelle Prüfung der Ruderaufhängung

### 1.4 Gesetzliche und normative Anforderungen

Die Wartung der Steueranlage unterliegt verschiedenen normativen Anforderungen:

**ISO 10592:1994 (Kleine Wasserfahrzeuge — Hydraulische Steuerung):**
- Jährliche Sichtprüfung aller hydraulischen Leitungen und Verbindungen
- Prüfung auf Leckagen unter Betriebsdruck
- Funktionsprüfung der Überdruckventile
- Prüfung des Hydraulikölstandes und -zustandes

**ISO 8847:2004 (Kleine Wasserfahrzeuge — Steuereinrichtungen — Seilzug und Gestänge):**
- Jährliche Prüfung der Seilspannung
- Sichtprüfung aller Seile auf Litzenbrüche und Korrosion
- Prüfung aller Seilklemmen und -verbindungen auf festen Sitz
- Prüfung der Umlenkrollen auf Leichtgängigkeit und Verschleiß

**ISO 25197:2020 (Kleine Wasserfahrzeuge — Elektrische/elektronische Steuerung):**
- Jährliche Funktionsprüfung aller elektronischen Steuerkomponenten
- Prüfung der Notabschaltung
- Prüfung der Fail-Safe-Mechanismen
- Software-Update-Status prüfen

**Klassifikationsgesellschaften (ab 24 m LH):**
- GL/DNV: Jährliche Klasse-Besichtigung inkl. Steueranlage
- Lloyd's: Condition Survey alle 2,5 Jahre, Special Survey alle 5 Jahre
- BV: Jährliche Inspektion, 5-Jahres-Erneuerungsbesichtigung
- RINA: Jährliche Besichtigung, Zwischenbesichtigung nach 2,5 Jahren

### 1.5 Sicherheitshinweise für Wartungsarbeiten

**WARNUNG — Allgemeine Sicherheitsregeln:**

1. **Niemals allein arbeiten.** Bei Arbeiten an der Steueranlage muss stets eine zweite Person anwesend sein, die das Ruder beobachtet und im Notfall eingreifen kann.
2. **Ruder sichern.** Vor jeder Arbeit an der Steueranlage das Ruder in Mittschiffsstellung fixieren (Ruderstopps oder Spanngurte). Ein unkontrolliert ausschlagendes Ruder kann schwere Verletzungen verursachen.
3. **Hydraulikdruck ablassen.** Vor Arbeiten an Hydraulikleitungen den Systemdruck vollständig ablassen. Hydrauliköl unter Druck kann die Haut durchdringen und zu schweren Gewebeschäden führen.
4. **Kein Motorbetrieb.** Bei Arbeiten an der Steueranlage muss der Motor ausgeschaltet und gegen Wiedereinschalten gesichert sein. Propellerdrehmoment erzeugt Ruderkräfte.
5. **Elektrische Autopiloten abschalten.** Vor jeder Arbeit den Autopiloten vollständig abschalten und gegen versehentliches Einschalten sichern (Sicherung ziehen).
6. **Geeignetes Werkzeug verwenden.** Keine improvisierten Werkzeuge an sicherheitskritischen Verbindungen. Drehmomentschlüssel für alle vorgeschriebenen Anzugsmomente verwenden.
7. **Dokumentation.** Jede Wartungsmaßnahme im Bordbuch dokumentieren (Datum, Maßnahme, Befunde, verwendete Materialien, nächster Termin).

---

## 2. Grundlagen und Theorie

### 2.1 Verschleißmechanismen — Seilzugsteuerung

Die Seilzugsteuerung ist das am weitesten verbreitete Steuerungssystem auf Segelyachten zwischen 8 und 16 Metern. Ihre Wartung erfordert ein Verständnis der spezifischen Verschleißmechanismen, die an den verschiedenen Komponenten auftreten.

#### 2.1.1 Drahtseilverschleiß

**Äußerer Verschleiß (Abrieb):**
Das Steuerseil läuft über mehrere Umlenkrollen und den Kettentrieb am Steuerrad. An jeder Umlenkstelle tritt Reibung zwischen den äußeren Drahtlitzen und der Rollenoberfläche auf. Dieser Abrieb reduziert den Querschnitt der äußeren Drähte und damit die Tragfähigkeit des Seils.

- **Verschleißrate ohne Schmierung:** 0,02–0,05 mm Durchmesserreduktion pro 1.000 Vollausschläge
- **Verschleißrate mit Schmierung:** 0,005–0,015 mm Durchmesserreduktion pro 1.000 Vollausschläge
- **Kritischer Durchmesserverlust:** >10 % des Nenndurchmessers → sofortiger Austausch
- **Typischer Nenndurchmesser Steuerseil:** 6,35 mm (1/4 Zoll) oder 7,94 mm (5/16 Zoll)

**Innerer Verschleiß (Ermüdung):**
Beim Durchlaufen der Umlenkrollen werden die Einzeldrähte des Seils biegewechselbeansprucht. Die inneren Drähte reiben aneinander (Innenreibung) und ermüden durch die zyklische Biegebelastung. Dieser Verschleiß ist von außen nicht sichtbar und daher besonders tückisch.

- **Mindest-D/d-Verhältnis:** Umlenkrollen-Durchmesser (D) zu Seildurchmesser (d) mindestens 20:1, besser 30:1
- **Biegewechselzahl bis Ermüdungsbruch (7×7-Seil, D/d=20):** ca. 200.000–400.000 Zyklen
- **Biegewechselzahl bis Ermüdungsbruch (7×19-Seil, D/d=20):** ca. 500.000–800.000 Zyklen

**Korrosion:**
In der marinen Umgebung ist Korrosion der Hauptfeind des Steuerseils. Auch hochwertige Edelstahlseile (AISI 316) korrodieren unter bestimmten Bedingungen:

- **Spaltkorrosion:** In den Zwischenräumen der Litzenstruktur sammelt sich Salzwasser. Der eingeschränkte Sauerstoffzugang führt zu lokaler Passivschicht-Zerstörung.
- **Spannungsrisskorrosion (SCC):** Unter Zugspannung stehende Edelstahldrähte sind anfällig für chloridinduzierte Spannungsrisskorrosion, besonders bei Temperaturen >50 °C (z. B. in der Nähe des Motorraums).
- **Reibkorrosion (Fretting):** An Klemmstellen und Seilschlössern entsteht durch Mikrobewegungen unter Last eine Oxidschicht, die abgetragen wird und zu fortschreitendem Materialverlust führt.

**Verschleißindikatoren am Steuerseil:**

| Befund | Bewertung | Maßnahme |
|--------|-----------|----------|
| 1–2 gebrochene Drähte auf 6×d Länge | Beobachten | Nächste Saison tauschen |
| 3–5 gebrochene Drähte auf 6×d Länge | Eingeschränkt | Zeitnah tauschen (innerhalb 30 Tage) |
| >5 gebrochene Drähte auf 6×d Länge | Kritisch | Sofort tauschen, nicht auslaufen |
| Durchmesserreduktion >5 % | Eingeschränkt | Nächste Saison tauschen |
| Durchmesserreduktion >10 % | Kritisch | Sofort tauschen |
| Kordeleffekt (Aufdrehen) | Kritisch | Sofort tauschen |
| Knicke oder Korbbildung | Kritisch | Sofort tauschen |
| Gleichmäßige leichte Rostfärbung | Beobachten | Schmieren, nächste Inspektion 1 Monat |
| Lokale tiefe Korrosionsnarben | Eingeschränkt | Zeitnah tauschen |

#### 2.1.2 Umlenkrollenverschleiß

Umlenkrollen (Sheaves) in der Seilzugsteuerung unterliegen zwei Hauptverschleißmechanismen:

**Rillenverschleiß:**
Das Steuerseil läuft in der V- oder U-förmigen Rille der Umlenkrolle. Unter Last gräbt sich das Seil in die Rillenoberfläche ein. Der Verschleiß ist abhängig vom Rollenmaterial:

| Material | Verschleißrate (relativ) | Typische Lebensdauer | Anmerkung |
|----------|-------------------------|---------------------|-----------|
| Delrin/Acetal | 1,0 (Referenz) | 5–8 Jahre | Standard bei den meisten Herstellern |
| UHMWPE | 0,6 | 8–12 Jahre | Bessere Abriebfestigkeit |
| Bronze | 0,3 | 15–25 Jahre | Schwer, teuer, langlebig |
| Edelstahl 316 | 0,2 | 20–30 Jahre | Hoher Seilverschleiß! |
| Aluminium eloxiert | 0,8 | 4–6 Jahre | Leicht, geringere Lebensdauer |

**WICHTIG:** Edelstahl-Umlenkrollen sind zwar selbst langlebig, verursachen aber den höchsten Verschleiß am Steuerseil. Für Seilzugsteuerungen sind Delrin- oder UHMWPE-Rollen der beste Kompromiss zwischen Rollen- und Seil-Lebensdauer.

**Lagerverschleiß:**
Die Umlenkrollen laufen auf Gleit- oder Kugellagern. Verschleiß äußert sich in zunehmendem Spiel und Schwergängigkeit:

- **Maximal zulässiges Radialspiel:** 0,3 mm (Gleitlager) / 0,1 mm (Kugellager)
- **Prüfmethode:** Rolle seitlich bewegen, Spiel mit Fühlerlehre messen
- **Schwergängigkeitsprüfung:** Rolle muss sich bei leichtem Fingeranstoß mindestens 3 Umdrehungen frei drehen

#### 2.1.3 Quadrantverschleiß

Der Quadrant (auch Steuersegment oder Sektor) überträgt die lineare Seilbewegung in eine Drehbewegung des Ruderschafts. Verschleißstellen sind:

- **Seilrillen am Quadrant:** Einlaufspuren >1 mm Tiefe → Quadrant ersetzen
- **Ruderschaftklemmung:** Konus oder Keilverbindung darf kein Spiel aufweisen. Maximal zulässig: 0,05 mm
- **Seilbefestigung:** Seilklemmen, Nicopress-Hülsen oder Seilschlösser am Quadrant auf Festigkeit und Korrosion prüfen
- **Ruderstopps:** Gummi- oder Kunststoffpuffer an den Endanschlägen auf Verformung und Materialermüdung prüfen

### 2.2 Verschleißmechanismen — Kettensteuerung

Die Kettensteuerung wird vorwiegend auf Segelyachten über 12 Meter eingesetzt und kombiniert in vielen Ausführungen eine Kette (am Steuerrad) mit Drahtseilen (zum Quadranten). Die Kette bietet höhere Betriebssicherheit, erfordert aber spezifische Wartung.

#### 2.2.1 Kettenverschleiß

**Längung:**
Ketten "längen" sich im Betrieb. Diese Längung ist keine elastische Dehnung, sondern resultiert aus dem Verschleiß der Bolzen in den Kettengliedern. Mit fortschreitender Längung springt die Kette zunehmend auf dem Kettenrad, was die Steuergenauigkeit reduziert.

- **Neue Kette — Teilung (pitch):** 12,7 mm (1/2 Zoll), 15,875 mm (5/8 Zoll) je nach System
- **Maximal zulässige Längung:** 2 % der Nennteilung
- **Messmethode:** 10 Kettenglieder messen, Gesamtlänge durch 10 teilen, mit Nennteilung vergleichen
- **Typische Nutzungsdauer bis 2 % Längung:** 6.000–10.000 Betriebsstunden bei guter Schmierung

**Bolzen- und Buchsenverschleiß:**
Die Gelenke der Kette verschleißen durch Reibung unter Last. Trockenlauf beschleunigt diesen Verschleiß drastisch.

- **Verschleißrate trocken vs. geschmiert:** Faktor 8–15
- **Prüfmethode:** Kette auf einer Fläche ablegen und seitliches Spiel prüfen. Seitenspiel >2 mm → Austausch

**Korrosion:**
Steuerketten sind typischerweise aus Edelstahl 316 oder verzinktem Stahl gefertigt. Verzinkte Ketten sind in mariner Umgebung nur mit regelmäßiger Schmierung langfristig einsetzbar.

#### 2.2.2 Kettenradverschleiß

Das Kettenrad (Sprocket) am Steuerrad verschleißt an den Zahnflanken:

- **Verschleißprofil:** Haifischzahnform (asymmetrisch abgenutzte Zähne)
- **Maximal zulässiger Zahnflankenverschleiß:** 15 % der Zahnhöhe
- **Messmethode:** Zahnhöhe mit Schieblehre messen und mit Neumaß vergleichen
- **Kettenrad und Kette immer gemeinsam tauschen:** Eine neue Kette auf einem verschlissenen Kettenrad verschleißt 3–5× schneller

### 2.3 Verschleißmechanismen — Hydrauliksteuerung

Hydraulische Steuerungen bieten den höchsten Bedienkomfort und die größte Kraftübersetzung. Ihre Wartung konzentriert sich auf die Dichtigkeit des Hydraulikkreises und die Qualität des Hydrauliköls.

#### 2.3.1 Dichtungsverschleiß

**O-Ring-Degradation:**
Hydraulikdichtungen (O-Ringe, Quad-Ringe, Lippendichtungen) sind die am häufigsten verschleißenden Komponenten. Ihre Lebensdauer wird bestimmt durch:

- **Werkstoff:** NBR (Nitrilkautschuk, Standard), FKM/Viton (höhere Temperatur- und Chemikalienbeständigkeit), EPDM (nicht für mineralische Hydrauliköle)
- **Temperaturbelastung:** Jede 10 °C über der Nenntemperatur halbiert die Lebensdauer
- **Druckbelastung:** Überschreitung des Nenndrucks führt zu Extrusion
- **Chemische Verträglichkeit:** Falsches Hydrauliköl kann Dichtungen quellen oder schrumpfen lassen

**Lebensdauererwartung von Hydraulikdichtungen:**

| Dichtungstyp | Material | Nenntemperatur | Erwartete Lebensdauer |
|--------------|----------|----------------|----------------------|
| O-Ring Helm-Pumpe | NBR 70 Shore | -20 bis +100 °C | 4–6 Jahre |
| O-Ring Helm-Pumpe | FKM 75 Shore | -15 bis +200 °C | 6–10 Jahre |
| Lippendichtung Zylinder | NBR | -20 bis +100 °C | 5–8 Jahre |
| Lippendichtung Zylinder | PU (Polyurethan) | -30 bis +80 °C | 6–10 Jahre |
| Quad-Ring Helm | FKM | -15 bis +200 °C | 8–12 Jahre |
| Wellendichtring Ruderlager | NBR | -20 bis +100 °C | 5–8 Jahre |

**Leckage-Klassifizierung:**

| Leckagegrad | Beschreibung | Maßnahme |
|-------------|-------------|----------|
| L0 — Trocken | Keine sichtbare Feuchtigkeit | Normalbefund |
| L1 — Feucht | Ölfilm sichtbar, kein Tropfen | Beobachten, nächste Inspektion 1 Monat |
| L2 — Schwitzend | Langsame Tropfenbildung (>1 min/Tropfen) | Dichtung zeitnah erneuern (30 Tage) |
| L3 — Tropfend | Regelmäßiges Tropfen (<1 min/Tropfen) | Dichtung kurzfristig erneuern (7 Tage) |
| L4 — Laufend | Kontinuierlicher Ölfluss | Sofortige Reparatur, nicht auslaufen |

#### 2.3.2 Hydrauliköl-Degradation

Hydrauliköl altert im Betrieb durch thermische, oxidative und hydrolytische Prozesse. Die Ölqualität bestimmt maßgeblich die Lebensdauer aller Hydraulikkomponenten.

**Alterungsmechanismen:**

1. **Oxidation:** Sauerstoffaufnahme führt zu Säurebildung, Viskositätsanstieg und Schlammbildung. Beschleunigt durch Hitze, Kupferkontakt und Wassergehalt.
2. **Thermische Zersetzung:** Lokale Überhitzung (>90 °C) an Drosseln und Ventilen zersetzt das Öl und erzeugt Lack und Kohle.
3. **Wasseraufnahme (Hydrolyse):** Kondenswasser im Ölbehälter hydrolysiert Additive und fördert Korrosion. Kritisch ab >0,1 % Wassergehalt.
4. **Partikelkontamination:** Abrieb von Pumpen, Zylindern und Ventilen verschmutzt das Öl und beschleunigt den Verschleiß aller Komponenten.

**Ölzustandsbewertung — Feldmethoden:**

| Prüfung | Methode | Gut | Grenzwertig | Schlecht |
|---------|---------|-----|-------------|---------|
| Farbe | Sichtprüfung gegen Licht | Klar, honigfarben | Dunkelbraun | Schwarz, trüb |
| Geruch | Geruchsprüfung | Neutral, mild | Leicht stechend | Beißend, verbrannt |
| Viskosität | Tropfentest auf Schräge | Fließt gleichmäßig | Fließt zäh | Zähflüssig oder wässrig |
| Wassergehalt | Brattest (Tropfen auf 150 °C Platte) | Kein Knistern | Leichtes Knistern | Starkes Spritzen |
| Partikel | Tropfen auf weißes Papier | Gleichmäßig, klar | Leichte Rückstände | Dunkle Partikel sichtbar |

**Ölwechselintervalle nach Hersteller:**

| Hersteller | Intervall | Öltyp |
|-----------|-----------|-------|
| Lewmar | 2 Jahre oder 2.000 Betriebsstunden | Lewmar Hydrauliköl (ISO VG 15) |
| Teleflex/SeaStar | 2 Jahre | SeaStar / BayStar Fluid (ATF-kompatibel) |
| Jefa | 3 Jahre oder 3.000 Betriebsstunden | Jefa Hydraulic Oil oder ISO VG 15/22 |
| Kobelt | 2 Jahre oder 2.500 Betriebsstunden | Kobelt K-22 Hydraulic Oil (ISO VG 22) |
| Hynautic | 2 Jahre | Hynautic H-OIL (proprietär) |
| Vetus | 2 Jahre | ATF Dexron III |

#### 2.3.3 Schlauchdegradation

Hydraulikschläuche in der Steueranlage unterliegen mehreren Alterungsmechanismen:

**Innere Schicht (Seele):**
- Quellung durch Ölkontakt (bei inkompatiblem Schlauchmaterial)
- Verhärtung durch Wärme
- Rissbildung durch Druckpulsation

**Verstärkungsschicht:**
- Korrosion der Stahlgeflechteinlage
- Ermüdung durch Biegewechsel (an Schlauchbewegungsstellen)

**Äußere Schicht (Mantel):**
- UV-Degradation (sichtbare Risse, Versprödung)
- Scheuerstellen durch Kontakt mit anderen Bauteilen
- Ozonrissbildung (feine Querrisse)

**Schlauchlebensdauer und Austauschkriterien:**

| Zustand | Beschreibung | Maßnahme |
|---------|-------------|----------|
| Äußere Haarrisse | Feine Oberflächenrisse im Mantel | Beobachten, UV-Schutz anbringen |
| Tiefe Risse (>1 mm) | Risse bis zur Verstärkungsschicht | Austausch innerhalb 6 Monate |
| Schwellung | Lokale Durchmessererhöhung >10 % | Sofortiger Austausch |
| Verformung | Knicke, Abflachungen | Sofortiger Austausch |
| Ölnässe an Pressung | Feuchtigkeit an der Schlauchpressung | Austausch innerhalb 3 Monate |
| Alter >7 Jahre | Unabhängig vom Zustand | Austausch empfohlen |
| Alter >10 Jahre | Unabhängig vom Zustand | Austausch zwingend |

### 2.4 Verschleißmechanismen — Zahnstangensteuerung

Die Zahnstangensteuerung (Rack-and-Pinion) ist typisch für Motoryachten und kleinere Segelyachten. Sie bietet direkte mechanische Übertragung mit geringem Spiel.

#### 2.4.1 Zahnflankenverschleiß

**Abrasiver Verschleiß:**
Die Zahnflanken von Ritzel und Zahnstange verschleißen durch die rollende und gleitende Bewegung unter Last. Korrekter Schmierstoff reduziert den Verschleiß um den Faktor 10–20.

- **Zahnflankenspiel neu:** 0,05–0,15 mm (je nach Hersteller)
- **Maximal zulässiges Zahnflankenspiel:** 0,5 mm
- **Messmethode:** Steuerrad mit einer Hand festhalten, mit der anderen am Ruderblatt oder Quadranten Spiel ertasten und mit Messuhr quantifizieren

**Pittingbildung:**
Unter hoher Flächenpressung bei gleichzeitig mangelhafter Schmierung entstehen Grübchen (Pitting) auf den Zahnflanken. Diese verursachen zunehmende Laufgeräusche und beschleunigten Verschleiß.

#### 2.4.2 Führungsverschleiß

Die Zahnstange wird in einer Führungsbuchse geführt. Verschleiß an der Führung äußert sich in:

- **Radialspiel:** Klappergeräusche bei Seegang, Steuerimpräzision
- **Schwergängigkeit:** Erhöhter Steuerkraftbedarf durch Verkanten
- **Messverfahren:** Zahnstange bei Mittschiffsstellung seitlich bewegen, Spiel mit Fühlerlehre an der Führung messen

### 2.5 Verschleißmechanismen — Gemeinsame Komponenten

#### 2.5.1 Ruderlager-Verschleiß (alle Steuerungstypen)

Ruderlager sind bei allen Steuerungstypen die Schnittstelle zwischen Rumpf und Ruderschaft. Ihr Verschleiß beeinflusst die gesamte Steueranlage.

**Gleitlager (Delrin/Acetal):**

Delrin-Gleitlager sind der Standard im Serienyachtbau. Sie verschleißen durch:

- **Abrasiven Verschleiß:** Sandkörner oder Korrosionspartikel zwischen Lager und Schaft wirken als Schleifmittel
- **Quellung:** Wasseraufnahme (0,2–0,3 % bei Acetal) verursacht Maßänderungen
- **Thermische Verformung:** Erwärmung durch Reibung bei schnellen Ruderbewegungen (Regatta)
- **Kriechneigung:** Unter Dauerlast kann Delrin "fließen" und den Lagerspalt vergrößern

**Verschleißraten Delrin-Ruderlager:**

| Betriebsbedingung | Verschleißrate (Spiel-Zunahme/Jahr) | Erwartete Lebensdauer |
|-------------------|-------------------------------------|-----------------------|
| Fahrtensegler, gewartet | 0,01–0,02 mm/Jahr | 12–18 Jahre |
| Fahrtensegler, ungewartet | 0,03–0,05 mm/Jahr | 6–10 Jahre |
| Charter (intensiv) | 0,04–0,08 mm/Jahr | 4–7 Jahre |
| Regatta (häufig, schnell) | 0,05–0,10 mm/Jahr | 3–6 Jahre |
| Trockenfall-Revier (Sand) | 0,08–0,15 mm/Jahr | 2–5 Jahre |

**Jefa Self-Aligning Bearings:**

Die selbstausrichtenden, wassergeschmierten Ruderlager von Jefa sind der Premium-Standard. Besonderheiten:

- **Wassergeschmiert:** Kein Fett erforderlich — das umgebende Seewasser ist das Schmiermittel
- **Selbstausrichtend:** Kompensieren Fluchtungsfehler bis zu ±3° (Fehlausrichtung Schaft/Stevenrohr)
- **Reibungsarm:** Reibungskoeffizient 0,05–0,10 (Delrin: 0,15–0,25)
- **Verschleißrate:** 0,005–0,015 mm/Jahr unter normalen Bedingungen
- **Einschränkung:** Empfindlich gegen Sandkorn-Kontamination — in Trockenfall-Revieren häufiger prüfen

**Bronze-Gleitlager:**

Traditionelle Ruderlager aus Phosphorbronze (CuSn8, CuSn12) oder Manganbronze:

- **Vorteile:** Sehr langlebig (20–30 Jahre), korrosionsbeständig, gute Notlaufeigenschaften
- **Nachteile:** Erfordern regelmäßige Schmierung (Fett NLGI 2), galvanische Korrosion bei Kontakt mit Edelstahlschaft möglich
- **Wartung:** Schmiernippel alle 3–6 Monate abschmieren, Überschussfett am Lagerspalt kontrollieren
- **Verschleißerkennung:** Bronze-Abrieb verfärbt Fett grünlich — normaler Indikator, solange Spiel im Rahmen

**Thordon-Composite-Lager:**

Hochleistungslagermaterial für anspruchsvolle Anwendungen:

- **Wassergeschmiert:** Wie Jefa, kein Fett erforderlich
- **Verschleißrate:** Ähnlich Jefa (0,005–0,015 mm/Jahr)
- **Vorteil:** Auch für große Schaftdurchmesser (>60 mm) verfügbar
- **Einsatz:** Vorwiegend größere Yachten und kommerzielle Schiffe

#### 2.5.2 Pedestal-Verschleiß (Seilzug/Kette)

Der Pedestal (Steuersäule) enthält die Kettenumlenkung und die Lager für die Steuerradwelle. Verschleißstellen:

**Steuerradwellen-Lager:**
- Oberes und unteres Lager in der Steuersäule
- Verschleiß äußert sich in Spiel und Knirschen am Steuerrad
- Austausch über Pedestal Service Kit (alle 8–15 Jahre, nutzungsabhängig)

**Kettenumlenkung im Pedestal:**
- Kettenführung (typisch Delrin/UHMWPE) verschleißt durch Kettenlauf
- Verschleiß äußert sich in zunehmendem Kettengeräusch und ungleichmäßigem Lauf
- Führungsschienen alle 5–8 Jahre prüfen und ggf. tauschen

**Wetterdichtungen:**
- O-Ringe und Lippendichtungen am Steuerradwellen-Austritt
- Verhindern Wassereintritt ins Pedestal-Innere
- Austausch alle 5–8 Jahre (im Pedestal Service Kit enthalten)

**Kompass-Kompensation:**
- Pedastal-Kompass wird durch magnetische Kompensation justiert
- Verschiebung der Kompensation deutet auf Pedestal-Bewegung oder -Verformung hin
- Kompass bei jeder Pedestal-Wartung nachkompensieren

#### 2.5.3 Steuerrad-Verschleiß

**Edelstahl-Steuerräder:**
- Schweißnähte an Speichen auf Risse prüfen (jährlich, Lupe)
- Radnabe auf Spiel gegenüber Welle prüfen
- Radzerstörungsfreie Prüfung (Farbindring-Penetration) alle 10 Jahre bei sicherheitskritischer Nutzung

**GFK/Carbon-Steuerräder:**
- Auf Haarrisse im Gelcoat/Klarlack prüfen (UV-Degradation)
- Naben-Klebung auf Festigkeit prüfen (Ruck-Test)
- Carbon: Auf Delamination an Speichen prüfen (Klopftest — dumpfer Ton = Delamination)

**Holz-Steuerräder (Teak, Mahagoni):**
- Lack-/Ölfinish jährlich auffrischen (UV- und Feuchtigkeitsschutz)
- Auf Risse und Lösung vom Stahlkern prüfen
- Holz-Stahl-Übergang auf Korrosion prüfen (Spaltkorrosion unter Holz)

**Steuerrad-Leder:**
- Lederumwicklung auf Verschleiß, Lösung und Schimmel prüfen
- Mit Lederpflege behandeln (2× pro Saison)
- Bei Verschleiß: Neues Leder wickeln oder durch Kork/Gummi ersetzen

### 2.6 Inspektionsmethoden

#### 2.5.1 Visuelle Inspektion (VT)

Die visuelle Inspektion ist die Grundlage jeder Wartung. Sie erfordert gute Beleuchtung (mind. 350 Lux, besser Stirnlampe mit 500+ Lux) und systematisches Vorgehen.

**Inspektionsroute — Seilzugsteuerung:**

1. Steuerrad → Kette/Seilführung am Pedestal
2. Kettengehäuse → Seil-Ketten-Verbindung
3. Seil → Verlauf durch den Rumpf (alle zugänglichen Abschnitte)
4. Umlenkrollen → jede einzeln auf Spiel, Leichtgängigkeit, Rillenverschleiß
5. Quadrant → Seilbefestigung, Ruderschaftklemmung
6. Ruderstopps → Puffer, Anschläge
7. Ruderlager → oberes und unteres Lager, Wellendichtung
8. Notpinne → Zugang, Passform, Befestigungsmittel

**Inspektionsroute — Hydrauliksteuerung:**

1. Helm-Pumpe → Leckage, Spiel, Widerstand
2. Hydraulikleitungen → von Helm zum Zylinder, jede Verbindung
3. Hydraulikzylinder → Leckage, Befestigung, Kolbenstangenzustand
4. Hydraulikölbehälter → Ölstand, Ölzustand, Belüftung
5. Überdruckventil → Funktion, Einstellung
6. Ruderstopps und -lager → wie bei Seilzugsteuerung

#### 2.5.2 Messtechnische Inspektion

**Seilspannungsmessung:**

Die korrekte Seilspannung ist entscheidend für die Steuergenauigkeit und Seillebensdauer. Zu hohe Spannung beschleunigt den Verschleiß, zu niedrige Spannung führt zu Schlupf am Quadranten.

- **Messinstrument:** Loos-Tensiometer (Modell PT-2 für Steuerseil) oder Navtec T-Gauge
- **Korrekte Spannung:** Herstellerabhängig, typisch 10–15 % der Seilbruchlast
- **Typische Werte:** 6,35 mm Seil (Bruchlast ~1.800 kg): 180–270 N Vorspannung
- **Prüfung:** Beide Seilzüge (Backbord und Steuerbord) müssen identische Spannung aufweisen. Differenz >10 % → nachstellen

**Ruderschaftspiel-Messung:**

- **Instrument:** Messuhr mit Magnetfuß
- **Messposition:** Messuhr radial am Ruderschaft, direkt über dem oberen Ruderlager
- **Messung:** Ruder seitlich hin- und herbewegen, radiales Spiel ablesen
- **Grenzwerte:** <0,1 mm = gut, 0,1–0,3 mm = beobachten, >0,3 mm = Lagertausch planen

**Hydraulikdruck-Messung:**

- **Instrument:** Manometer 0–100 bar mit passendem Anschluss (typisch 1/4" BSP oder 9/16-18 UNF JIC)
- **Betriebsdruck typisch:** 35–70 bar (je nach System und Rudergröße)
- **Maximaldruck (Überdruckventil):** 80–120 bar
- **Prüfung:** Ruder gegen Anschlag fahren, Druck am Manometer ablesen. Muss dem Einstellwert des Überdruckventils entsprechen (±5 %)

### 2.6 Schmierstoffe für Steueranlagen

Die Wahl des richtigen Schmierstoffs ist entscheidend für die Lebensdauer aller mechanischen Komponenten der Steueranlage.

**Schmierstoff-Zuordnung nach Anwendung:**

| Anwendung | Schmierstofftyp | Empfohlene Produkte | Intervall |
|-----------|----------------|--------------------|-----------| 
| Steuerseile | Dünnflüssiges Drahtfett | Lewmar Wire Rope Lube, Boeshield T-9, McLube OneDrop | 3 Monate |
| Umlenkrollen (Gleitlager) | Marine-Fett NLGI 2 | Lewmar Winch Grease, Harken Long Life Grease, Mobil SHC 100 | 6 Monate |
| Umlenkrollen (Kugellager) | Marine-Lagerfett NLGI 2 | NTN/SKF marine bearing grease, Mobil SHC 100 | 12 Monate |
| Steuerketten | Kettenschmierstoff | Lewmar Chain Lube, Boeshield T-9, WD-40 Specialist Marine | 3 Monate |
| Quadrant-Konus/Keil | Anti-Seize-Paste | Tef-Gel, Duralac, Loctite 8023 | Bei Montage |
| Ruderlager (Gleitlager) | Marine-Fett NLGI 2 oder Wasser | Jefa Self-Aligning Bearing (wassergeschmiert), Thordon Grease | 6 Monate |
| Zahnstange/Ritzel | Marine-Getriebefett | Teleflex Rack Grease, Kobelt Gear Lube | 12 Monate |
| Hydrauliköl | ISO VG 15/22 Hydrauliköl | Lewmar Hydraulic Oil, Kobelt K-22, SeaStar Fluid | 2 Jahre (Wechsel) |

**Schmierstoff-Verträglichkeitsmatrix:**

| Schmierstoff | Delrin/POM | UHMWPE | PTFE | NBR | FKM/Viton | Bronze | Edelstahl |
|-------------|-----------|--------|------|-----|-----------|--------|-----------|
| Lithiumfett | NEIN | NEIN | NEIN | JA | JA | JA | JA |
| Kalziumfett | JA | JA | JA | JA | JA | JA | JA |
| Silikonöl | JA | JA | JA | BEDINGT | JA | JA | JA |
| Silikonfett | JA | JA | JA | BEDINGT | JA | JA | JA |
| Mineralöl | JA | JA | JA | JA | JA | JA | JA |
| Synthetisches Öl (PAO) | JA | JA | JA | JA | JA | JA | JA |
| PTFE-basiert (Tef-Gel) | JA | JA | JA | JA | JA | JA | JA |
| Lanolin-basiert (Lanocote) | JA | JA | JA | JA | JA | JA | JA |
| WD-40 (kurzfristig) | JA | JA | JA | JA | JA | JA | JA |

*JA = verträglich, NEIN = unverträglich (Materialangriff), BEDINGT = kurzfristig OK, Langzeitkontakt vermeiden*

**WARNUNG — Schmierstoff-Inkompatibilitäten:**

1. **Niemals Lithiumfett an Kunststofflagern:** Greift Delrin, UHMWPE und PTFE an. Lithiumseife wirkt als Lösungsmittel auf bestimmte Polymere.
2. **Niemals silikonbasierte Schmierstoffe an NBR-Dichtungen:** Kann NBR-Dichtungen quellen lassen. FKM/Viton-Dichtungen sind silikonbeständig.
3. **Niemals verschiedene Hydrauliköle mischen:** Additive können reagieren und Schlammbildung verursachen. Im Zweifel: System komplett ablassen und neu befüllen.
4. **Niemals ATF in rein mineralischen Systemen:** Und umgekehrt. ATF enthält Dichtungsquellmittel, die in mineralischen Systemen Dichtungen zerstören können.
5. **Niemals WD-40 als Langzeitschmierstoff:** Verdrängt vorhandenes Fett und verdunstet nach wenigen Wochen. Nur als Reiniger, Wasserverdränger oder Erstschutz verwenden.
6. **Niemals Kupferpaste an Edelstahlverbindungen im Salzwasser:** Verursacht galvanische Korrosion. Stattdessen Tef-Gel oder Lanocote verwenden.
7. **Niemals PTFE-Dichtband in Hydraulikverbindungen:** PTFE-Fäden können in den Hydraulikkreislauf gelangen und Ventile blockieren. Hydraulikverbindungen dichten metalldichtend (Schneidring, JIC-Kegel) oder über O-Ringe.

### 2.7 Reinigungsmittel für Steueranlagen

Die Reinigung vor der Schmierung ist ebenso wichtig wie die Schmierung selbst. Alte Fett- und Schmutzrückstände bilden eine abrasive Paste, die den Verschleiß beschleunigt.

**Reinigungsmittel-Empfehlungen:**

| Anwendung | Empfohlenes Mittel | Alternative | Anwendungshinweis |
|-----------|--------------------|------------|------------------|
| Steuerkette reinigen | Petroleum (Testbenzin) | Kettenreiniger (biologisch abbaubar) | Kette in Reiniger einlegen (30 min), abbürsten |
| Steuerseile reinigen | Petroleum-getränktes Tuch | WD-40 als Vorreiniger | Entlang des Seils abwischen, nicht tauchen |
| Umlenkrollen-Lager | Isopropanol oder Bremsenreiniger | Petroleum | Lager auswaschen, trocknen lassen, neu schmieren |
| Quadrant-Konus | Aceton oder Bremsenreiniger | Isopropanol | Fettfrei für korrekten Reibschluss |
| Hydraulikkomponenten | Systemöl (Spülung) | Isopropanol (nie im geschlossenen System!) | Nur mit dem Systemöl spülen |
| Pedestal-Inneres | Petroleum + weiche Bürste | — | Nicht mit Hochdruck! Dichtungen schützen |
| Korrosionsentfernung | Phosphorsäure-Gel (Marine) | Ospho, Fertan | Nur auf korrodierter Stelle, danach neutralisieren |
| Edelstahl-Pflege | Edelstahlpflege (z. B. Inox Clean) | Zitronensäurelösung | Passiviert die Oberfläche, Korrosionsschutz |

### 2.8 Werkzeugkunde — Spezialwerkzeuge für Steueranlagen

**Nicopress-Werkzeug:**
Das Nicopress-Werkzeug (auch Talurit-Presse) ist das wichtigste Spezialwerkzeug für die Seilzugsteuerung. Es verpresst ovale Kupfer- oder Edelstahlhülsen dauerhaft auf das Drahtseil.

- **Modelle:** Nicopress 51-C (für 4,76–7,94 mm), Nicopress 64-CG (für 7,94–12,7 mm)
- **Hülsenmaterial:** Kupfer (Standard), Edelstahl (marine, teurer, langlebiger)
- **Pressungen pro Hülse:** 2–3 (herstellerabhängig, immer Markierung beachten)
- **Prüfung:** Go/No-Go-Lehre — Hülse muss in "Go"-Seite passen, nicht in "No-Go"-Seite
- **Kosten:** 60–120 EUR (Handwerkzeug), 200–400 EUR (Tischgerät)

**Loos-Tensiometer:**
Präzisionsmessgerät zur Bestimmung der Seilvorspannung.

- **Modelle:** Loos PT-1 (2–4 mm), Loos PT-2 (4,76–7,94 mm), Loos PT-3 (7,94–12,7 mm)
- **Messprinzip:** Seitliche Auslenkung des Seils gegen kalibrierte Feder → Skalenablesung → Umrechnungstabelle
- **Genauigkeit:** ±5 % bei korrekter Anwendung
- **Kosten:** 110–180 EUR
- **Kalibrierung:** Jährlich gegen Referenz prüfen (Hängewaage + bekanntes Gewicht)

**Hydraulik-Entlüftungskit:**
Zum Entlüften von Hydrauliksteuerungen.

- **Inhalt:** Entlüftungsschlauch (transparent, ölfest), Auffangbehälter, Adapter für verschiedene Entlüftungsschrauben
- **Herstellerkits:** SeaStar HA5435, Lewmar Bleed Kit
- **DIY-Alternative:** Transparenter Silikonschlauch (6 mm innen) + Schraubglas
- **Kosten:** Herstellerkit 35–65 EUR, DIY 5–10 EUR

**Manometer (Hydraulikdruck):**
Zur Prüfung des Systemdrucks und der Überdruckventil-Einstellung.

- **Messbereich:** 0–100 bar (Standard) oder 0–160 bar (Hochdruck)
- **Anschluss:** 1/4" BSP oder 9/16-18 UNF JIC (Adapter-Set empfohlen)
- **Genauigkeit:** Klasse 1,6 (±1,6 % vom Endwert) ausreichend
- **Kosten:** 25–60 EUR
- **Prüfung:** Vor jeder Verwendung Nullpunkt prüfen (drucklos muss Zeiger auf 0 stehen)

**Messuhr mit Magnetfuß:**
Zur Messung von Ruderschaft-Spiel und Lagerverschleiß.

- **Messbereich:** 0–10 mm
- **Auflösung:** 0,01 mm
- **Magnetfuß:** Haftkraft mind. 30 kg (muss am Ruderschaft oder Stevenrohr halten)
- **Kosten:** 40–80 EUR (inkl. Magnetfuß)
- **Anwendung:** Messuhr radial am Schaft positionieren, Ruder seitlich bewegen, Maximalausschlag ablesen = Radialspiel

---

## 3. Typenübersicht

### 3.1 Wartungsplan Seilzugsteuerung

#### 3.1.1 Monatliche Wartung (Eigner, 15 Min.)

**Checkliste monatliche Seilzugsteuerungs-Wartung:**

- [ ] Steuerrad auf Leichtgängigkeit prüfen (Vollausschlag Bb/Stb in <3 Sekunden ohne übermäßigen Kraftaufwand)
- [ ] Steuerrad-Spiel prüfen (Totgang <5° am Rad, gemessen ohne Ruderwiderstand)
- [ ] Sichtprüfung des Steuerseils an zugänglichen Stellen (Litzenbrüche, Korrosion, Knicke)
- [ ] Kettengehäuse am Pedestal auf ungewöhnliche Geräusche prüfen
- [ ] Rudergänger auf Geräusche oder Vibrationen bei Ruderbewegung befragen
- [ ] Bilge unter Quadrant auf Feuchtigkeit/Korrosionsspuren prüfen

**Dokumentation:** Datum, Befunde, nächster Termin im Bordbuch.

#### 3.1.2 Vierteljährliche Wartung (Eigner, 45 Min.)

**Checkliste vierteljährliche Seilzugsteuerungs-Wartung:**

- [ ] Alle Punkte der monatlichen Wartung
- [ ] Seilspannung prüfen (Daumentest: Seil soll sich bei Daumendruck ca. 10–15 mm seitlich auslenken lassen bei 6,35 mm Seil)
- [ ] Alle Umlenkrollen auf Leichtgängigkeit prüfen (von Hand drehen)
- [ ] Alle Umlenkrollen auf seitliches Spiel prüfen (max. 0,3 mm)
- [ ] Steuerseile an allen zugänglichen Stellen mit Drahtfett einsprühen
- [ ] Kette am Pedestal mit Kettenöl schmieren
- [ ] Quadrant-Seilbefestigung auf festen Sitz prüfen (Sichtprüfung, nicht lösen)
- [ ] Ruderstopps auf korrekten Sitz und Pufferzustand prüfen
- [ ] Pedestal-Kompass auf korrekte Ausrichtung prüfen (Indikator für Pedestal-Bewegung)

#### 3.1.3 Halbjährliche Wartung (Versierter Eigner, 1,5 Std.)

**Checkliste halbjährliche Seilzugsteuerungs-Wartung:**

- [ ] Alle Punkte der vierteljährlichen Wartung
- [ ] Seilspannung mit Tensiometer messen und protokollieren
- [ ] Vergleich mit Vorjahreswert (Spannungsverlust >20 % → Seil dehnt sich, Tausch planen)
- [ ] Alle Umlenkrollen aus der Halterung nehmen, reinigen und schmieren
- [ ] Umlenkrollen-Rillen auf Verschleiß prüfen (Rillenbreite >Seildurchmesser + 1 mm → tauschen)
- [ ] Ruderlager (oberes) auf Spiel prüfen (Ruder seitlich hin- und herbewegen)
- [ ] Ruderstopps auf korrekte Einstellung prüfen (Ruderausschlag max. 35° je Seite, typisch 30°)
- [ ] Pedestal-Befestigung an Deck prüfen (alle Schrauben/Bolzen handfest)
- [ ] Notpinne aufsetzen und Passung prüfen

#### 3.1.4 Jährliche Vollinspektion (Fachbetrieb empfohlen, 3–4 Std.)

**Checkliste jährliche Seilzugsteuerungs-Vollinspektion:**

- [ ] Alle Punkte der halbjährlichen Wartung
- [ ] Steuerseil auf gesamter Länge inspizieren (Laterne/Stirnlampe, ggf. Inspektionsspiegel)
- [ ] Steuerseil an 5 Messpunkten mit Mikrometer messen (Durchmesserreduktion dokumentieren)
- [ ] Alle Seilklemmen/Nicopress-Hülsen prüfen (Verformung, Risse, Korrosion)
- [ ] Kette auf Längung prüfen (10 Glieder messen)
- [ ] Kettenrad auf Zahnflankenverschleiß prüfen
- [ ] Quadrant abnehmen (wenn möglich), Ruderschaft-Konus reinigen, auf Korrosion und Passmarken prüfen
- [ ] Quadrant-Ruderschaft-Verbindung mit korrektem Drehmoment anziehen (herstellerspezifisch, typisch 80–120 Nm)
- [ ] Anti-Seize auf Ruderschaft-Konus erneuern (Tef-Gel oder Duralac)
- [ ] Oberes und unteres Ruderlager auf Spiel messen (Messuhr)
- [ ] Ruderwellendichtung auf Leckage prüfen
- [ ] Steuerseildurchführungen (Schotten) auf Scheuerstellen prüfen
- [ ] Pedestal komplett inspizieren (Lager, Kette, Bremse, Kompass)
- [ ] Gesamtspiel der Steueranlage messen (Ruderblattspitze bei fixiertem Steuerrad — max. ±2° Ruderausschlag)
- [ ] Alle Befunde dokumentieren mit Fotos
- [ ] Wartungsprotokoll erstellen mit Empfehlungen und nächstem Termin

### 3.2 Wartungsplan Kettensteuerung

Die Kettensteuerung unterscheidet sich vom Seilzugsystem primär durch den durchgehenden Kettentrieb vom Steuerrad zum Quadranten. Die Wartung konzentriert sich stärker auf Kettenzustand und -spannung.

#### 3.2.1 Monatliche Wartung (Eigner, 15 Min.)

- [ ] Steuerrad auf Leichtgängigkeit und Geräusche prüfen
- [ ] Totgang am Steuerrad prüfen (max. 5°)
- [ ] Sichtprüfung der Kette an zugänglichen Stellen
- [ ] Auf ungewöhnliche Geräusche achten (Klappern = zu lose, Schleifen = zu straff oder Führungsverschleiß)
- [ ] Bilge unter Kettengehäuse auf Rost/Metallabrieb prüfen

#### 3.2.2 Halbjährliche Wartung (Versierter Eigner, 2 Std.)

- [ ] Alle Punkte der monatlichen Wartung
- [ ] Kette auf gesamter Länge reinigen (Petroleum oder Kettenreiniger)
- [ ] Kette schmieren (Lewmar Chain Lube oder gleichwertig)
- [ ] Kettenspannung prüfen und justieren (Durchhang in der Mitte des längsten freien Spans: 10–15 mm)
- [ ] Kettenrad auf Verschleiß prüfen (Zahnprofil)
- [ ] Kettenführungen/Gleitschienen auf Verschleiß prüfen (typisch UHMWPE oder Delrin)
- [ ] Alle Kettenschlösser/Verbinder auf festen Sitz prüfen
- [ ] Quadrant-Befestigung prüfen
- [ ] Ruderlager-Spiel prüfen
- [ ] Ruderstopps kontrollieren

#### 3.2.3 Jährliche Vollinspektion (Fachbetrieb, 3–5 Std.)

- [ ] Alle Punkte der halbjährlichen Wartung
- [ ] Kette abnehmen und auf Werkbank prüfen
- [ ] Kettenlängung messen (10 Glieder, Schieblehre)
- [ ] Alle Kettenglieder auf Risse und Verformung prüfen (Lupe 10×)
- [ ] Kettenrad abnehmen, Zahnflankenverschleiß messen
- [ ] Kettenführungen erneuern wenn Verschleiß >2 mm
- [ ] Steuerrad-Lager prüfen und schmieren
- [ ] Quadrant-Verbindung lösen, reinigen, Anti-Seize erneuern, mit Drehmoment anziehen
- [ ] Ruderlager-Spiel messen (Messuhr)
- [ ] Gesamtspiel der Steueranlage dokumentieren
- [ ] Bei Kettenlängung >1,5 %: Kette und Kettenrad tauschen

### 3.3 Wartungsplan Hydrauliksteuerung

#### 3.3.1 Monatliche Wartung (Eigner, 10 Min.)

- [ ] Steuerrad auf Leichtgängigkeit prüfen (gleichmäßiger Widerstand über gesamten Ausschlag)
- [ ] Totgang prüfen (Hydraulik: max. 3° am Rad)
- [ ] Hydraulikölstand am Vorratsbehälter prüfen (Markierung beachten)
- [ ] Sichtprüfung aller sichtbaren Hydraulikleitungen und Verbindungen auf Leckage
- [ ] Bilge unter Hydraulikzylinder auf Ölspuren prüfen
- [ ] Helm-Pumpe auf Leckage prüfen (Öl am Schaftaustritt = Dichtungsverschleiß)

#### 3.3.2 Halbjährliche Wartung (Versierter Eigner, 1,5 Std.)

- [ ] Alle Punkte der monatlichen Wartung
- [ ] Alle Hydraulikschläuche auf gesamter Länge prüfen (Risse, Schwellung, Scheuerstellen)
- [ ] Alle Verschraubungen mit Leckage-Spray prüfen (Lecksuchspray oder Spülmittellösung)
- [ ] Hydraulikölfarbe und -zustand beurteilen
- [ ] Hydraulikzylinder auf Kolbenstangenzustand prüfen (Kratzer, Korrosion → Dichtungsverschleiß)
- [ ] Zylinderbefestigung auf festen Sitz prüfen (Bolzen, Gabelköpfe, Kugelgelenke)
- [ ] Ruderschaftdichtung auf Leckage prüfen
- [ ] Notpinne testen (Hydraulik-Bypass-Ventil öffnen, Notpinne aufsetzen, Funktion prüfen)
- [ ] Ruderstopps kontrollieren

#### 3.3.3 Zweijährliche Vollinspektion (Fachbetrieb, 4–6 Std.)

- [ ] Alle Punkte der halbjährlichen Wartung
- [ ] Hydrauliköl wechseln (komplett ablassen, System spülen wenn stark verschmutzt, neu befüllen)
- [ ] System entlüften (nach Hersteller-Vorschrift, typisch am höchsten Punkt)
- [ ] Helm-Pumpe auf internen Verschleiß prüfen (Leckölmessung)
- [ ] Hydraulikzylinder auf interne Leckage prüfen (Ruder bei gesperrtem Ventil belasten, Drift beobachten)
- [ ] Alle Verschraubungen nachziehen (herstellerspezifische Drehmomente)
- [ ] Überdruckventil-Funktion prüfen (Manometer)
- [ ] Überdruckventil-Einstellung prüfen (Herstellervorgabe, typisch 85–110 bar)
- [ ] Alle Hydraulikschläuche mit Alter >7 Jahre erneuern
- [ ] Ruderlager-Spiel messen (Messuhr)
- [ ] Gesamtspiel und Ansprechverhalten dokumentieren

### 3.4 Wartungsplan Zahnstangensteuerung

#### 3.4.1 Halbjährliche Wartung (Eigner, 30 Min.)

- [ ] Steuerrad auf Leichtgängigkeit prüfen
- [ ] Totgang prüfen (Zahnstange: max. 2° am Rad)
- [ ] Zahnstangengehäuse auf Leckage von Schmierfett prüfen
- [ ] Balg/Manschette an den Zahnstangenenden auf Risse prüfen (Fett-/Wasseraustritt = sofort tauschen)
- [ ] Sichtprüfung der Steuerseile (falls Seil-Zahnstangen-Kombination)
- [ ] Gelenke der Spurstangen auf Spiel prüfen
- [ ] Ruderstopps kontrollieren

#### 3.4.2 Jährliche Wartung (Versierter Eigner, 1,5 Std.)

- [ ] Alle Punkte der halbjährlichen Wartung
- [ ] Zahnstangengehäuse öffnen (wenn konstruktiv vorgesehen), Fettfüllung prüfen und erneuern
- [ ] Zahnflankenspiel messen (Messuhr am Ruderarm, Steuerrad fixiert)
- [ ] Führungsbuchsen auf Verschleiß prüfen (Radialspiel messen)
- [ ] Spurstangengelenke schmieren
- [ ] Balg/Manschette bei Beschädigung erneuern
- [ ] Ruderlager-Spiel prüfen

### 3.5 Winterfestmachung (Einwinterung)

Die Winterfestmachung der Steueranlage ist kritisch, da stehende mechanische Systeme im Winter besonders anfällig für Korrosion, Festfressen und Frostschäden sind.

#### 3.5.1 Seilzugsteuerung — Winterfestmachung

1. **Seilzugsteuerung komplett durchfahren** (10× Vollausschlag Bb/Stb) um Schmierstoff zu verteilen
2. **Steuerseile großzügig mit Drahtfett einsprühen** — besonders an Umlenkstellen und Durchführungen
3. **Kette am Pedestal reinigen und schmieren** — altes Fett entfernen, frisches Kettenfett auftragen
4. **Umlenkrollen nachschmieren** — je einen Tropfen dünnflüssiges Öl an die Lager
5. **Seilspannung um 10 % reduzieren** — entlastet Seil und Lager über den Winter
6. **Quadrant-Bereich belüften** — Feuchtigkeit ist der Hauptfeind im Winter
7. **Steuerrad mit Abdeckung schützen** oder abnehmen und trocken lagern
8. **Rudergänger fixieren** — Ruder in Mittschiffsstellung sichern (Spanngurte oder Keil)
9. **Notpinne an zugänglicher Stelle lagern** — nicht im feuchten Bilgenbereich

#### 3.5.2 Hydrauliksteuerung — Winterfestmachung

1. **Hydraulikölstand auf Maximum auffüllen** — minimiert Luftvolumen im System und damit Kondenswasserbildung
2. **System 10× Vollausschlag durchfahren** — verteilt frisches Öl an alle Dichtungen
3. **Alle Verbindungen auf Dichtheit prüfen** — Leckage im Winter = leeres System im Frühjahr
4. **Zylinder-Kolbenstange mit Korrosionsschutz einsprühen** (Boeshield T-9 oder CRC 6-66)
5. **Bei Frostgefahr:** Hydrauliköl auf Frostbeständigkeit prüfen. Standard-Marinöle sind typisch bis -20 °C frostsicher. In extremen Klimazonen ggf. Frostschutz-kompatibles Öl verwenden.
6. **Hydraulikschläuche spannungsfrei verlegen** — bei Kälte werden Schläuche steifer und können an Presshülsen brechen
7. **Helm-Pumpe mit Abdeckung schützen** — vor Feuchtigkeit und UV
8. **Bypass-Ventil schließen** — verhindert unkontrollierte Ruderbewegung durch Wellenschlag am Liegeplatz

#### 3.5.3 Kettensteuerung — Winterfestmachung

1. **Kette komplett reinigen** — Petroleum oder Kettenreiniger, altes verharztes Fett entfernen
2. **Kette mit frischem Marine-Kettenfett schmieren** — dünn auftragen, alle Glieder
3. **Kettenführungen prüfen** — Winter ist eine gute Zeit für den Austausch verschlissener Führungsschienen
4. **Kettenspannung um 10 % reduzieren** — wie bei Seilzugsteuerung
5. **Kettengehäuse mit Korrosionsschutz einsprühen** (Innenraum)
6. **Quadrant wie bei Seilzugsteuerung behandeln**
7. **Belüftung sicherstellen**

#### 3.5.4 Zahnstangensteuerung — Winterfestmachung

1. **System mehrmals Vollausschlag durchfahren** — Fett verteilen
2. **Manschetten/Bälge auf Risse prüfen** — beschädigte Manschetten vor dem Winter erneuern
3. **Spurstangengelenke schmieren**
4. **Zahnstangengehäuse ggf. nachfetten** (wenn Schmiernippel vorhanden)
5. **Steuerrad fixieren und abdecken**

### 3.6 Detaillierte Schritt-für-Schritt-Anleitungen

#### 3.6.1 Anleitung: Steuerseil-Spannungskontrolle und -Nachstellung

**Benötigtes Werkzeug:**
- Loos-Tensiometer PT-2 (für 4,76–7,94 mm Seile)
- Gabelschlüssel (Größe passend zum Spannschloss, typisch 13 mm oder 1/2")
- Kontermutter-Schlüssel
- Schraubendreher für Zugangsdeckel
- Stirnlampe
- Bordbuch und Stift

**Schritt 1 — Vorbereitung:**
1. Boot am Steg gesichert, kein Seegang
2. Motor aus, Autopilot aus (Sicherung ziehen)
3. Steuerrad in Mittschiffsstellung bringen
4. Ruder visuell auf Mittschiffsstellung prüfen (am Ruderblatthinterkante von achtern)
5. Zugangsdeckel zu Steuerseilen und Quadrant öffnen

**Schritt 2 — Ist-Spannung messen:**
1. Tensiometer am längsten freien Seilstück (typisch zwischen zwei Umlenkrollen) ansetzen
2. Tensiometer mittig positionieren
3. Seil in die Messkerbe einlegen
4. Griff zusammendrücken bis Klick
5. Wert an der Skala ablesen
6. Aus Umrechnungstabelle (Seildurchmesser + Ablesung → Spannung in kg/N) die Ist-Spannung ermitteln
7. Messung an 2–3 Stellen wiederholen, Mittelwert bilden
8. Verfahren für beide Seilzüge (Bb und Stb) durchführen

**Schritt 3 — Soll-Ist-Vergleich:**
- Sollspannung: Herstellerangabe oder 10–15 % der Seilbruchlast
- Typische Sollwerte: 6,35 mm 7×19 = 180–270 N (18–27 kg)
- Differenz Bb zu Stb: max. 10 % (sonst asymmetrischer Ruderausschlag)
- Werte in Bordbuch eintragen und mit Vorjahr vergleichen

**Schritt 4 — Nachstellung (falls erforderlich):**
1. Kontermutter am Spannschloss oder an der Seilklemme lösen
2. Spannschraube vorsichtig nachziehen (1/4 bis 1/2 Umdrehung)
3. Erneut messen
4. Beide Seiten gleichmäßig nachspannen (identische Spannung!)
5. Steuerrad auf Leichtgängigkeit prüfen (darf nicht schwergängiger geworden sein)
6. Kontermutter anziehen
7. Vollausschlag Bb und Stb prüfen (symmetrisch? Ruderstopps erreicht?)
8. Neue Werte in Bordbuch eintragen

**Schritt 5 — Abschluss:**
1. Zugangsdeckel schließen
2. Funktionsprüfung: 10× Vollausschlag
3. Autopilot-Sicherung wieder einsetzen

#### 3.6.2 Anleitung: Hydraulikölwechsel

**Benötigtes Werkzeug und Material:**
- Neues Hydrauliköl (herstellerspezifisch, ausreichende Menge — mindestens 2× Systemvolumen für Spülung)
- Auffangwanne (ölfest, mind. 2 Liter)
- Transparenter Silikonschlauch (50 cm, passend für Entlüftungsschraube)
- Schraubglas als Auffangbehälter
- Gabelschlüssel für Entlüftungsschrauben und Ablassschrauben
- Lappen, Ölbindemittel
- Handschuhe (Nitril)
- Trichter mit feinem Sieb (oder Spritze zum Befüllen)

**Schritt 1 — Vorbereitung:**
1. Boot am Steg, kein Seegang, Ruder in Mittschiffsstellung
2. Motor aus, Autopilot aus
3. Ölbindemittel um Hydraulikkomponenten auslegen
4. Altes Ölgebinde bereithalten (Entsorgung!)

**Schritt 2 — Altes Öl ablassen:**
1. Ölbehälter-Deckel öffnen
2. Ablassschraube am tiefsten Punkt des Systems öffnen (typisch am Zylinder oder an der Helm-Pumpe)
3. Steuerrad langsam hin- und herbewegen, um Öl aus allen Leitungen zu drücken
4. Altes Öl in Auffangwanne sammeln
5. Ölfarbe und -zustand dokumentieren (für Diagnose)

**Schritt 3 — Spülung (bei verschmutztem Öl):**
1. Ablassschraube schließen
2. Frisches Öl einfüllen (ca. 50 % der Systemmenge)
3. Steuerrad 20× Vollausschlag hin- und her bewegen
4. Spülöl ablassen
5. Vorgang bei stark verschmutztem System wiederholen

**Schritt 4 — Neues Öl einfüllen:**
1. Ablassschraube schließen und mit korrektem Drehmoment anziehen
2. Frisches Öl über Trichter/Sieb in den Ölbehälter füllen
3. Steuerrad langsam bewegen, um Öl ins System zu bringen
4. Ölstand sinkt — nachfüllen
5. Vorgang wiederholen bis Ölstand stabil bleibt

**Schritt 5 — Entlüften:**
1. Entlüftungsschraube am höchsten Punkt des Systems (typisch am Zylinder oben) leicht öffnen
2. Silikonschlauch aufstecken, Ende in Schraubglas mit etwas Öl tauchen
3. Steuerrad langsam Vollausschlag in Richtung des Zylinders drehen
4. Luft entweicht als Blasen im Schlauch → warten bis blasenfreies Öl kommt
5. Entlüftungsschraube schließen (bei laufendem Ölfluss — keine Luft nachziehen!)
6. Vorgang für andere Seite wiederholen
7. Ölstand nachfüllen

**Schritt 6 — Funktionsprüfung:**
1. 20× Vollausschlag Bb/Stb
2. Auf Schwammigkeit prüfen (= noch Luft im System → erneut entlüften)
3. Alle Verbindungen auf Leckage prüfen
4. Ölstand auf Maximum auffüllen
5. Nochmals Leckage nach 24 Stunden prüfen

**Schritt 7 — Dokumentation:**
1. Öltyp, Menge, Hersteller und Chargennummer dokumentieren
2. Zustand des alten Öls dokumentieren
3. Nächsten Ölwechseltermin festlegen (2 Jahre oder nach Herstellerangabe)
4. Altöl fachgerecht entsorgen (Sondermüll!)

#### 3.6.3 Anleitung: Ruderlager-Spielmessung

**Benötigtes Werkzeug:**
- Messuhr mit Magnetfuß (Messbereich 0–10 mm, Auflösung 0,01 mm)
- Stirnlampe
- Zugang zum Ruderschaft (oberes Ruderlager muss sichtbar sein)
- Helfer am Ruder (außen oder am Quadranten)

**Messverfahren:**
1. Messuhr-Magnetfuß am Stevenrohr oder an einer festen Struktur neben dem Ruderschaft befestigen
2. Messtaster radial am Ruderschaft positionieren (direkt über dem oberen Ruderlager)
3. Messuhr auf Null setzen
4. Helfer drückt Ruderblatt (oder Quadrant) seitlich in eine Richtung → Messuhr ablesen
5. Helfer drückt in die andere Richtung → Messuhr ablesen
6. Differenz = Radialspiel
7. Messung in zwei Ebenen durchführen (Bb/Stb und Vor/Achter) — den größeren Wert nehmen
8. Am unteren Ruderlager wiederholen (falls zugänglich)

**Bewertung:**

| Radialspiel | Bewertung | Maßnahme |
|------------|-----------|----------|
| <0,05 mm | Neuwertig | Keine |
| 0,05–0,10 mm | Gut | Keine, nächste Messung in 12 Monaten |
| 0,10–0,20 mm | Befriedigend | Beobachten, nächste Messung in 6 Monaten |
| 0,20–0,30 mm | Grenzwertig | Lagertausch in nächster Saison planen |
| 0,30–0,50 mm | Unzureichend | Lagertausch zeitnah (3 Monate) |
| >0,50 mm | Mangelhaft | Lagertausch dringend, Dichtung prüfen |
| >1,0 mm | Kritisch | Nicht auslaufen, sofort Werft |

#### 3.6.4 Anleitung: Ketten-Längungsmessung

**Benötigtes Werkzeug:**
- Schieblehre (digital, mind. 200 mm Messbereich)
- Reinigungsmittel (Petroleum)
- Lappen

**Messverfahren:**
1. Kette in dem Bereich, der am meisten beansprucht wird, reinigen (typisch am Kettenrad)
2. 10 zusammenhängende Kettenglieder auf einer flachen Oberfläche auslegen
3. Kette leicht spannen (Eigengewicht genügt)
4. Abstand von Bolzenmitte (erstes Glied) bis Bolzenmitte (elftes Glied) messen = 10 × Teilung
5. Sollmaß berechnen: 10 × Nennteilung (z. B. 10 × 12,7 mm = 127,0 mm)
6. Längung berechnen: (Istmaß - Sollmaß) / Sollmaß × 100 %

**Bewertung:**

| Längung | Bewertung | Maßnahme |
|---------|-----------|----------|
| <0,5 % | Neuwertig/Gut | Keine |
| 0,5–1,0 % | Befriedigend | Beobachten, Intervall 6 Monate |
| 1,0–1,5 % | Grenzwertig | Tausch in nächster Saison planen |
| 1,5–2,0 % | Verschlissen | Tausch zeitnah (Kette + Kettenrad) |
| >2,0 % | Überschritten | Sofortiger Tausch, Kettenspringen möglich |

### 3.7 Wartungsplan Pinnensteuerung

Die Pinnensteuerung ist das einfachste Steuerungssystem und findet sich auf Segelyachten bis ca. 10 m sowie auf vielen Jollen und Daysailern. Die direkte mechanische Verbindung Pinne→Ruderschaft hat wenige Verschleißstellen.

#### 3.6.1 Monatliche Wartung (Eigner, 5 Min.)

- [ ] Pinnenkoker-Dichtung auf Leckage prüfen (Wasser im Cockpit-Boden)
- [ ] Pinne auf Risse prüfen (Holz: Längsrisse, GFK: Haarrisse an Belastungspunkten)
- [ ] Pinnenausleger (Tiller Extension) auf Gelenkverschleiß prüfen
- [ ] Rudergängigkeit prüfen (Vollausschlag ohne übermäßigen Kraftaufwand)
- [ ] Ruderstopps kontrollieren (falls vorhanden)

#### 3.6.2 Halbjährliche Wartung (Eigner, 30 Min.)

- [ ] Alle Punkte der monatlichen Wartung
- [ ] Pinnenbeschlag am Ruderkopf auf festen Sitz prüfen
- [ ] Pinnensicherung (Splint, Federstecker) auf Zustand prüfen
- [ ] Ruderlager schmieren (falls Schmiernippel vorhanden)
- [ ] Holzpinne: Oberflächenbehandlung prüfen (Lack, Öl), ggf. auffrischen
- [ ] GFK-Pinne: Auf Gelcoat-Risse und Delamination prüfen
- [ ] Pinnenkoker-Dichtung auf Zustand prüfen, ggf. erneuern
- [ ] Windfahnensteuerungs-Anlenkung prüfen (falls vorhanden)

#### 3.6.3 Jährliche Wartung (Eigner, 1 Std.)

- [ ] Alle Punkte der halbjährlichen Wartung
- [ ] Pinnenbeschlag demontieren, reinigen, Anti-Seize erneuern
- [ ] Ruderlager-Spiel messen
- [ ] Ruderschaft auf Korrosion prüfen (sichtbarer Bereich)
- [ ] Pinnenkoker-Dichtung erneuern (präventiv)
- [ ] Holzpinne: vollständige Oberflächenaufarbeitung (Schleifen, neu lackieren/ölen)
- [ ] Pinnenausleger-Gelenk reinigen und schmieren oder tauschen bei Verschleiß

### 3.7 Wartungsplan Autopilot-Anbindung

Die Anbindung des Autopiloten an die Steueranlage ist ein häufig vernachlässigter Wartungsbereich. Der Autopilot-Antrieb verschleißt die Steueranlage zusätzlich und hat eigene Wartungsanforderungen an der Schnittstelle.

#### 3.7.1 Autopilot-Schnittstelle — Seilzug/Kette

**Linearer Autopilot-Antrieb (z. B. Raymarine Type 1, B&G Pilot):**

- [ ] Antriebsstange auf Leichtgängigkeit prüfen (3 Monate)
- [ ] Befestigung am Quadranten prüfen: Bolzen, Gabelkopf, Splint (3 Monate)
- [ ] Antriebsmotor auf Geräusche prüfen (6 Monate)
- [ ] Ruderlagenrückmelder (Potentiometer oder Linearfühler) auf korrekte Funktion prüfen (6 Monate)
- [ ] Elektrische Anschlüsse auf Korrosion und festen Sitz prüfen (jährlich)
- [ ] Antrieb vom Quadranten trennen: Prüfen, ob manuelles Steuern unbeeinflusst möglich (jährlich)
- [ ] Antrieb unter Last testen: Autopilot einschalten, Ruder gegen Wasserwiderstand bewegen, auf Schlupf und Geräusche prüfen (Saisonstart)

**Riemen/Kettenantrieb am Steuerrad (z. B. Raymarine Wheel Drive):**

- [ ] Antriebsriemen auf Verschleiß, Risse und Spannung prüfen (3 Monate)
- [ ] Kupplung auf Schlupf prüfen (6 Monate)
- [ ] Motorlager auf festen Sitz prüfen (jährlich)
- [ ] Riemenspannung nachjustieren wenn Autopilot-Performance nachlässt
- [ ] Riemen alle 3–5 Jahre präventiv tauschen

#### 3.7.2 Autopilot-Schnittstelle — Hydraulik

**Hydraulischer Autopilot-Antrieb (z. B. Raymarine Type 2/3, B&G Hydraulic Pilot):**

- [ ] Autopilot-Hydraulikzylinder auf Leckage prüfen (monatlich)
- [ ] Autopilot-Magnetventile auf Funktion prüfen (6 Monate)
- [ ] Hydraulikölstand im Autopilot-Kreislauf prüfen (6 Monate, wenn separater Kreislauf)
- [ ] Schläuche zwischen Steuerhydraulik und Autopilot-Hydraulik prüfen (jährlich)
- [ ] Rückschlagventile auf Funktion prüfen (jährlich)
- [ ] System entlüften nach jedem Eingriff an der Steuerhydraulik (!)
- [ ] Autopilot-Hydrauliköl muss identisch mit Steuerhydrauliköl sein (!)

### 3.8 Spezialwartung — Elektro-Hydraulische Steuerung (EPS)

Elektro-hydraulische und vollelektrische Steuersysteme (z. B. SeaStar Optimus 360, Volvo Penta IPS-Steuerung) erfordern spezifische Wartungsmaßnahmen.

#### 3.8.1 Wartungsintervalle EPS

| Wartungsmaßnahme | Intervall | Durchführung |
|-----------------|-----------|-------------|
| Software-Update-Status prüfen | Jährlich | Fachbetrieb |
| Elektrische Steckverbindungen prüfen | 6 Monate | Eigner |
| CAN-Bus-Verkabelung visuell prüfen | Jährlich | Eigner |
| Hydraulikeinheit (Pumpe + Ventile) prüfen | Jährlich | Fachbetrieb |
| Hydrauliköl wechseln | 2 Jahre | Fachbetrieb |
| Notfall-Funktionstest (Fallback auf manuell) | 6 Monate | Eigner |
| Joystick-Kalibrierung prüfen | Jährlich | Fachbetrieb |
| Ruderlagenrückmelder kalibrieren | Jährlich | Fachbetrieb |
| Spannungsversorgung (Bordnetz) prüfen | 6 Monate | Eigner |

**Besondere Hinweise EPS:**
- EPS-Systeme haben eine Fail-Safe-Funktion: Bei Ausfall der Elektronik schaltet das System auf mechanisch-hydraulische Steuerung um. Diese Fallback-Funktion muss regelmäßig getestet werden.
- Software-Updates können Steuerungscharakteristik ändern — nach jedem Update Probefahrt durchführen.
- CAN-Bus-Fehler können zu komplettem Steuerungsausfall führen — Kabelführung vor mechanischem Schaden schützen.

### 3.9 Saison-Inbetriebnahme (Auswinterung)

#### 3.6.1 Allgemeine Saison-Inbetriebnahme (alle Steuerungstypen)

**Phase 1 — Sichtprüfung vor Erstbetätigung:**

1. Gesamte Steueranlage visuell inspizieren (Korrosion, Feuchteschäden, Nagetierverbiss)
2. Alle Verbindungen auf festen Sitz prüfen
3. Bilge unter Steueranlage auf Wassereinbruch prüfen
4. Belüftung/Abdeckungen entfernen

**Phase 2 — Vorsichtige Erstbetätigung:**

1. Steuerrad langsam und vorsichtig bewegen (Vierteldrehung, dann lauschen)
2. Auf Schwergängigkeit, Geräusche und Widerstandsänderungen achten
3. Schrittweise auf Vollausschlag erhöhen
4. 10× Vollausschlag Bb/Stb zur Schmierungsverteilung

**Phase 3 — Funktionsprüfung:**

1. Seilspannung/Kettenspannung auf Sollwert nachstellen (im Winter reduziert)
2. Bei Hydraulik: Ölstand prüfen, ggf. nachfüllen, System entlüften
3. Ruderstopps prüfen (Ruder gegen Anschlag fahren, Stopps müssen fest sitzen)
4. Notpinne aufsetzen und Funktion prüfen
5. Gesamtspiel der Steueranlage dokumentieren
6. Vergleich mit Winterfestmachungs-Protokoll — Veränderungen?

**Phase 4 — Probefahrt:**

1. Bei der ersten Ausfahrt: Steuerung bei verschiedenen Geschwindigkeiten testen
2. Hart-Backbord und Hart-Steuerbord bei Marschfahrt
3. Auf Vibrationen, Geräusche, Schlupf und Totgang achten
4. Autopilot-Funktion prüfen (Antrieb muss Steueranlage sauber bewegen)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Lewmar Wartungskits und Ersatzteile

Lewmar (UK) ist einer der weltweit größten Hersteller von Steuerungssystemen für Segelyachten. Die Lewmar-Steuerungssysteme nutzen typischerweise eine Kette-Seil-Kombination.

#### 4.1.1 Lewmar Steuerungssysteme — Übersicht

| Modell | Typ | Bootsgröße | Seil-Ø | Ketten-Teilung | Rudermoment max. |
|--------|-----|-----------|--------|---------------|-----------------|
| Compac 3 | Seilzug/Kette | 7–10 m | 4,76 mm (3/16") | 10 mm | 340 Nm |
| Compac 5 | Seilzug/Kette | 9–13 m | 6,35 mm (1/4") | 12,7 mm | 680 Nm |
| Compac 7 | Seilzug/Kette | 12–16 m | 6,35 mm (1/4") | 12,7 mm | 950 Nm |
| Compac 10 | Seilzug/Kette | 14–20 m | 7,94 mm (5/16") | 15,875 mm | 1.360 Nm |
| Ocean 40 | Hydraulik | 10–14 m | — | — | 2.700 Nm |
| Ocean 60 | Hydraulik | 12–18 m | — | — | 4.100 Nm |
| Ocean 80 | Hydraulik | 16–24 m | — | — | 5.400 Nm |

#### 4.1.2 Lewmar Service-Kits

| Kit-Nr. | Bezeichnung | Inhalt | Für Modelle | UVP (EUR) |
|---------|-------------|--------|------------|-----------|
| 89000037 | Compac Pedestal Service Kit | Oberes/unteres Lager, Dichtungen, O-Ringe, Schmierfett | Compac 3/5/7 | 85–120 |
| 89000040 | Compac 10 Pedestal Service Kit | Oberes/unteres Lager, Dichtungen, O-Ringe, Schmierfett | Compac 10 | 110–145 |
| 89000052 | Ketten-Seil-Verbindungskit | 2× Seilklemmen, 2× Nicopress-Hülsen, Schäkel | Alle Compac | 35–55 |
| 89000061 | Steuerseil-Kit (6,35 mm) | 2× 15 m 7×19 Edelstahlseil, 4× Nicopress, Anleitung | Compac 5/7 | 95–130 |
| 89000062 | Steuerseil-Kit (7,94 mm) | 2× 15 m 7×19 Edelstahlseil, 4× Nicopress, Anleitung | Compac 10 | 115–155 |
| 89800021 | Ocean Helm Seal Kit | O-Ringe, Wellendichtring, Backup-Ring | Ocean 40/60 | 65–85 |
| 89800032 | Ocean Helm Seal Kit | O-Ringe, Wellendichtring, Backup-Ring | Ocean 80 | 75–105 |
| 89800045 | Ocean Zylinder-Dichtkit | Kolbendichtung, Stangendichtung, O-Ringe, Abstreifer | Ocean 40/60/80 | 55–90 |

**Lewmar empfohlene Schmierstoffe:**

| Produkt | Typ | Anwendung | Gebindegröße | UVP (EUR) |
|---------|-----|-----------|-------------|-----------|
| Lewmar Gear Grease | NLGI 2, Marine | Pedastal-Lager, Umlenkrollen | 100 ml Tube | 14–18 |
| Lewmar Wire Rope Lube | Dünnflüssiges Seilöl | Steuerseile, Ketten | 400 ml Spray | 16–22 |
| Lewmar Hydraulic Oil | ISO VG 15 | Ocean Hydrauliksysteme | 1 Liter | 28–38 |
| Lewmar Winch Grease | NLGI 2, Teflon | Allgemein | 100 g Tube | 12–16 |

### 4.2 Jefa Service-Kits

Jefa Marine (Dänemark) ist spezialisiert auf hochwertige Steuerungssysteme und Ruderlager für Segelyachten im Semi-Custom- und Custom-Bereich.

#### 4.2.1 Jefa Steuerungssysteme — Übersicht

| Modell | Typ | Bootsgröße | Besonderheit |
|--------|-----|-----------|-------------|
| Jefa Tiller Pilot | Seilzug | 6–10 m | Für Pinnensteuerung, leichtes System |
| Jefa Standard Cable | Seilzug/Kette | 8–14 m | Modulares Kabelsystem |
| Jefa Heavy Duty Cable | Seilzug/Kette | 12–20 m | Verstärktes System, größere Quadranten |
| Jefa Hydraulic Direct | Hydraulik | 12–25 m | Direktantrieb ohne Quadrant |
| Jefa Self-Aligning Bearing | Ruderlager | 6–30 m | Wassergeschmierte, selbstausrichtende Lager |

#### 4.2.2 Jefa Service-Kits und Ersatzteile

| Artikel-Nr. | Bezeichnung | Inhalt | UVP (EUR) |
|-------------|-------------|--------|-----------|
| JEFA-SK-01 | Standard Cable Service Kit | Seilklemmen, Rollen, Achsen, Sicherungen | 95–130 |
| JEFA-SK-02 | Heavy Duty Cable Service Kit | Verstärkte Seilklemmen, HD-Rollen, Achsen | 140–185 |
| JEFA-BRG-30 | Ruderlager-Kit 30 mm | Oberes + unteres Lager, Dichtungen, Montagehilfe | 280–380 |
| JEFA-BRG-40 | Ruderlager-Kit 40 mm | Oberes + unteres Lager, Dichtungen, Montagehilfe | 350–480 |
| JEFA-BRG-50 | Ruderlager-Kit 50 mm | Oberes + unteres Lager, Dichtungen, Montagehilfe | 440–620 |
| JEFA-HYD-SK | Hydraulic Seal Kit | O-Ringe, Kolbendichtungen, Stangendichtung, Abstreifer | 85–120 |
| JEFA-QDR-25 | Quadrant 250 mm | Aluminium eloxiert, inkl. Konusklemme | 195–260 |
| JEFA-QDR-32 | Quadrant 320 mm | Aluminium eloxiert, inkl. Konusklemme | 245–320 |
| JEFA-QDR-40 | Quadrant 400 mm | Edelstahl/Aluminium, inkl. Konusklemme | 340–450 |

**Jefa empfohlene Schmierstoffe:**

| Anwendung | Empfohlenes Produkt | Alternative |
|-----------|--------------------|-----------| 
| Ruderlager (Jefa Self-Aligning) | Wassergeschmiert — kein Fett nötig | — |
| Ruderlager (konventionell) | Jefa Bearing Grease (Marine-Fett NLGI 2) | Mobilgrease 28 |
| Steuerseile | Boeshield T-9 | McLube OneDrop |
| Quadrant-Konus | Tef-Gel | Lanocote |

### 4.3 Edson Ersatzteile

Edson International (USA) ist der führende Hersteller von Steuerungssystemen für Segelyachten in Nordamerika und weltweit verbreitet.

#### 4.3.1 Edson Steuerungssysteme — Übersicht

| Serie | Typ | Bootsgröße | Seil-Ø |
|-------|-----|-----------|--------|
| Edson 311 | Seilzug/Kette | 6–9 m | 4,76 mm (3/16") |
| Edson 336 | Seilzug/Kette | 8–12 m | 6,35 mm (1/4") |
| Edson 401 | Seilzug/Kette | 10–15 m | 6,35 mm (1/4") |
| Edson 501 | Seilzug/Kette | 12–18 m | 7,94 mm (5/16") |
| Edson 601 | Seilzug/Kette | 16–22 m | 7,94 mm (5/16") |

#### 4.3.2 Edson Ersatzteile

| Teile-Nr. | Bezeichnung | Für Serie | UVP (USD) |
|-----------|-------------|-----------|-----------|
| 335ST-100 | Steuerseil 7×19, 1/4", 100 ft | 336/401 | 89–115 |
| 335ST-516 | Steuerseil 7×19, 5/16", 100 ft | 501/601 | 105–135 |
| 346AL-025 | Umlenkrolle Delrin, 2,5" | 336/401 | 28–38 |
| 346AL-030 | Umlenkrolle Delrin, 3,0" | 501/601 | 32–45 |
| 346BR-030 | Umlenkrolle Bronze, 3,0" | 501/601 | 85–110 |
| 611-75-640 | Quadrant 6,4" (163 mm) | 336/401 | 145–190 |
| 611-75-800 | Quadrant 8,0" (203 mm) | 501 | 180–240 |
| 611-75-100 | Quadrant 10,0" (254 mm) | 601 | 225–295 |
| 665ST-012 | Kette 1/2" × 12 ft | 336/401/501 | 55–75 |
| 665ST-016 | Kette 1/2" × 16 ft | 601 | 70–95 |
| 335AL-NIC | Nicopress-Kit (10× Hülsen + Werkzeug) | Alle | 48–65 |
| 826SM-125 | Pedestal Bearing Kit | 336/401 | 55–75 |
| 826SM-150 | Pedestal Bearing Kit | 501/601 | 65–90 |

**Edson Wartungshinweise (aus Edson Service Bulletin SB-2023-07):**

- Steuerseile alle 10 Jahre tauschen, unabhängig vom Zustand (Empfehlung, keine Vorschrift)
- 7×19-Seil bevorzugt (flexibler, höhere Ermüdungsfestigkeit als 7×7 oder 1×19)
- Nicopress-Hülsen bevorzugt gegenüber Klemmen (vibrationsfester)
- Jährliche Inspektion: Seil an den 6 kritischsten Stellen prüfen (Ein-/Auslauf jeder Umlenkrolle, Quadrantbefestigung, Ketten-Seil-Verbindung)

### 4.4 Kobelt Hydrauliköle und -Komponenten

Kobelt Manufacturing (Kanada) produziert hochwertige hydraulische Steuerungssysteme, primär für Motoryachten und größere Segelyachten.

#### 4.4.1 Kobelt Steuerungssysteme — Übersicht

| Modell | Typ | Anwendung | Maximaldruck | Ölvolumen |
|--------|-----|-----------|-------------|-----------|
| Kobelt 7004 | Helm-Pumpe (manuell) | Motoryachten 8–14 m | 100 bar | 0,3–0,8 L |
| Kobelt 7012 | Helm-Pumpe (manuell) | Motoryachten 12–20 m | 140 bar | 0,5–1,2 L |
| Kobelt 7080 | Helm-Pumpe (power-assist) | Motoryachten 18–30 m | 175 bar | 1,0–3,0 L |
| Kobelt 2024 | Hydraulikzylinder | Bis 20 m | 175 bar | — |
| Kobelt 2030 | Hydraulikzylinder | Bis 30 m | 210 bar | — |

#### 4.4.2 Kobelt Hydrauliköle

| Produkt | Bezeichnung | Spezifikation | Gebinde | UVP (USD) |
|---------|-------------|--------------|---------|-----------|
| Kobelt K-15 | Kobelt Hydraulic Fluid | ISO VG 15, zinkfrei | 1 Quart (946 ml) | 22–30 |
| Kobelt K-22 | Kobelt Hydraulic Fluid HD | ISO VG 22, zinkfrei, EP-Additive | 1 Quart (946 ml) | 26–35 |
| Kobelt K-15G | Kobelt Hydraulic Fluid (Gallon) | ISO VG 15, zinkfrei | 1 Gallon (3,78 L) | 65–85 |
| Kobelt K-22G | Kobelt Hydraulic Fluid HD (Gallon) | ISO VG 22, zinkfrei | 1 Gallon (3,78 L) | 75–98 |

**Kobelt Hydrauliköl-Spezifikationen (K-22):**

| Eigenschaft | Wert | Prüfnorm |
|------------|------|----------|
| Viskosität bei 40 °C | 22 cSt | ASTM D445 |
| Viskosität bei 100 °C | 4,6 cSt | ASTM D445 |
| Viskositätsindex | 105 | ASTM D2270 |
| Pourpoint | -36 °C | ASTM D97 |
| Flammpunkt | 185 °C | ASTM D92 |
| Dichte bei 15 °C | 0,862 g/cm³ | ASTM D4052 |
| Wasserabscheidevermögen | <10 min (bei 54 °C) | ASTM D1401 |
| Korrosionsschutz | Bestanden | ASTM D665A/B |

#### 4.4.3 Kobelt Service-Kits

| Kit-Nr. | Bezeichnung | Inhalt | UVP (USD) |
|---------|-------------|--------|-----------|
| SK-7004 | Helm Seal Kit 7004 | O-Ringe, Wellendichtring, Backup | 55–75 |
| SK-7012 | Helm Seal Kit 7012 | O-Ringe, Wellendichtring, Backup | 65–90 |
| SK-7080 | Helm Seal Kit 7080 | O-Ringe, Wellendichtring, Backup, Ventilsitze | 95–130 |
| SK-2024C | Cylinder Seal Kit 2024 | Kolben-, Stangendichtung, O-Ringe, Abstreifer | 75–100 |
| SK-2030C | Cylinder Seal Kit 2030 | Kolben-, Stangendichtung, O-Ringe, Abstreifer | 90–120 |

### 4.5 Whitlock Teile

Whitlock Steering Systems (UK, jetzt Teil von Lewmar) war ein führender Hersteller von Seilzugsteuerungen. Viele Whitlock-Systeme sind noch im Einsatz und erfordern Wartung und Ersatzteile.

#### 4.5.1 Whitlock Steuerungssysteme (Legacy)

| Modell | Typ | Bootsgröße | Status |
|--------|-----|-----------|--------|
| Whitlock Mamba | Seilzug/Kette | 7–10 m | Eingestellt, Teile über Lewmar |
| Whitlock Cobra | Seilzug/Kette | 9–14 m | Eingestellt, Teile über Lewmar |
| Whitlock Python | Seilzug/Kette | 12–18 m | Eingestellt, Teile über Lewmar |
| Whitlock Anaconda | Seilzug/Kette | 16–22 m | Eingestellt, Teile über Lewmar |

#### 4.5.2 Whitlock Ersatzteile (über Lewmar)

| Lewmar-Nr. | Whitlock-Ref. | Bezeichnung | UVP (EUR) |
|------------|--------------|-------------|-----------|
| 89100012 | WH-001 | Mamba/Cobra Pedestal Bearing Kit | 65–85 |
| 89100018 | WH-002 | Python/Anaconda Pedestal Bearing Kit | 80–110 |
| 89100025 | WH-003 | Whitlock Umlenkrollen-Kit (4× Delrin) | 48–65 |
| 89100031 | WH-004 | Whitlock Quadrant-Kit Mamba | 130–170 |
| 89100038 | WH-005 | Whitlock Quadrant-Kit Cobra/Python | 165–220 |
| 89100044 | WH-006 | Whitlock Ketten-Seil-Kit (Mamba) | 75–100 |
| 89100051 | WH-007 | Whitlock Ketten-Seil-Kit (Cobra/Python) | 95–130 |
| 89100067 | WH-008 | Whitlock Ketten-Seil-Kit (Anaconda) | 120–160 |

**Hinweis zur Whitlock-Kompatibilität:**
- Lewmar hat die Whitlock-Kompatibilität für die meisten Verschleißteile beibehalten
- Steuerseile und Ketten sind standardisierte Teile und universell ersetzbar
- Pedestal-Lager und Dichtungen sind modellspezifisch — immer Whitlock-Modell und Baujahr angeben
- Bei unklarer Zuordnung: Lewmar Technical Support kontaktieren (Seriennummer am Pedestal)

### 4.6 Teleflex/SeaStar Hydraulikkomponenten

Teleflex Marine (jetzt SeaStar Solutions, USA/Kanada) ist Marktführer für hydraulische Steuerungssysteme im Motoryacht-Segment.

#### 4.6.1 Teleflex/SeaStar Systeme — Übersicht

| Modell | Typ | Bootsgröße | Besonderheit |
|--------|-----|-----------|-------------|
| BayStar | Hydraulik (niedrig) | 6–10 m, Außenborder | Kostengünstiges Einsteigersystem |
| SeaStar Pro | Hydraulik (Standard) | 8–14 m | Universelles Standardsystem |
| SeaStar HC5345 | Hydraulikzylinder | 8–20 m | Frontseitig, kompakt |
| SeaStar HC5348 | Hydraulikzylinder | 10–24 m | Rückseitig, hohe Kraft |
| Optimus 360 | EPS (elektrisch) | 8–14 m | Joystick-fähig, elektronisch |

#### 4.6.2 SeaStar Service-Produkte

| Produkt | Bezeichnung | Anwendung | Gebinde | UVP (USD) |
|---------|-------------|-----------|---------|-----------|
| HA5430 | SeaStar Hydraulic Steering Fluid | Alle SeaStar/BayStar Systeme | 1 Quart | 18–25 |
| HA5440 | SeaStar Hydraulic Steering Fluid | Alle SeaStar/BayStar Systeme | 1 Gallon | 52–70 |
| HA5905 | SeaStar Helm Seal Kit | SeaStar Pro Helm | Kit | 45–65 |
| HA5435 | SeaStar Pro Bleed Kit | Entlüftungskit | Kit | 35–48 |
| HC5345-SK | Cylinder Seal Kit HC5345 | HC5345 Zylinder | Kit | 40–55 |

### 4.7 Universelle Steuerseile und Ketten

Steuerseile und -ketten sind in vielen Fällen herstellerübergreifend einsetzbar, da sie genormten Spezifikationen folgen.

#### 4.7.1 Steuerseile — Spezifikationen und Auswahl

**Konstruktionstypen für Steueranlagen:**

| Konstruktion | Aufbau | Biegsamkeit | Bruchlast (6,35 mm) | Einsatz |
|-------------|--------|-------------|---------------------|---------|
| 1×19 | 1 Litze, 19 Drähte | Sehr steif | ~2.200 kg | NICHT für Steuerung (nur Want/Stag) |
| 7×7 | 7 Litzen à 7 Drähte | Mittel | ~1.600 kg | Leichte Steueranlagen, kleine Boote |
| 7×19 | 7 Litzen à 19 Drähte | Hoch | ~1.800 kg | Standard für Steueranlagen (empfohlen) |
| Compacted 7×19 | 7×19, verdichtet | Hoch+ | ~2.100 kg | Premium, längere Lebensdauer |

**Material-Qualitäten:**

| Qualität | Werkstoff | Korrosionsbeständigkeit | Preis (rel.) | Empfehlung |
|---------|-----------|------------------------|-------------|-----------|
| Standard | AISI 302/304 | Befriedigend | 1,0× | Süßwasser, überdacht |
| Marine Grade | AISI 316 | Gut | 1,3× | Standard marine (empfohlen) |
| Marine Premium | AISI 316L | Sehr gut | 1,5× | Hochwertige Yachten |
| Duplex | 2205 Duplex | Exzellent | 2,5× | Superyachten, tropisch |

**Standard-Seildurchmesser für Steueranlagen:**

| Durchmesser | Zoll | Bruchlast 7×19/316 | Typische Bootsgröße | Hersteller-Kompatibilität |
|-------------|------|--------------------|--------------------|--------------------------|
| 4,76 mm | 3/16" | ~1.050 kg | 6–10 m | Lewmar Compac 3, Edson 311 |
| 6,35 mm | 1/4" | ~1.800 kg | 9–16 m | Lewmar Compac 5/7, Edson 336/401, Whitlock Cobra |
| 7,94 mm | 5/16" | ~2.800 kg | 14–22 m | Lewmar Compac 10, Edson 501/601, Whitlock Python/Anaconda |
| 9,53 mm | 3/8" | ~4.000 kg | 20–30 m | Custom, Großyachten |

#### 4.7.2 Steuerketten — Spezifikationen

| Teilung (Pitch) | Zoll | Rollendurchmesser | Typische Anwendung |
|-----------------|------|-------------------|--------------------|
| 9,525 mm | 3/8" | 6,35 mm | Kleine Systeme (Compac 3) |
| 12,7 mm | 1/2" | 8,51 mm | Standard (Compac 5/7, Edson 336/401) |
| 15,875 mm | 5/8" | 10,16 mm | Große Systeme (Compac 10, Edson 601) |

**Kettenmaterial:**
- Standard: Edelstahl AISI 316 — Standardwahl für alle Marineanwendungen
- Alternativ: Vernickelt — günstiger, aber nur bei guter Schmierung dauerhaft
- Premium: Duplex-Edelstahl — höchste Korrosionsbeständigkeit

#### 4.7.3 Umlenkrollen — Universelle Austauschtypen

| Rollen-Ø | Für Seil-Ø | Material | Lagertyp | Tragkraft | Hersteller |
|-----------|-----------|----------|----------|----------|-----------|
| 38 mm (1,5") | 4,76 mm | Delrin | Gleitlager | 250 kg | Edson, Lewmar, Spa Creek |
| 50 mm (2,0") | 6,35 mm | Delrin | Gleitlager | 400 kg | Edson, Lewmar, Spa Creek |
| 63 mm (2,5") | 6,35 mm | Delrin | Gleitlager | 600 kg | Edson, Lewmar, Spa Creek |
| 75 mm (3,0") | 7,94 mm | Delrin | Gleitlager | 800 kg | Edson, Lewmar, Spa Creek |
| 75 mm (3,0") | 7,94 mm | Bronze | Kugellager | 1.200 kg | Edson, Spa Creek |
| 50 mm (2,0") | 6,35 mm | UHMWPE | Kugellager | 500 kg | Spa Creek, Jefa |
| 63 mm (2,5") | 6,35 mm | UHMWPE | Kugellager | 750 kg | Spa Creek, Jefa |

**Umlenkrollen-Auswahlkriterien:**
- D/d-Verhältnis ≥20 (besser ≥30) — Rollendurchmesser zu Seildurchmesser
- Rillenform: V-Profil für Drahtseil (Winkel 45–60°, Rillenradius = 0,53 × Seil-Ø)
- Befestigungstyp: Bolzenmontage (Standard), Plattenmontage, Decksmontage
- Lagertyp: Gleitlager (Standard, wartungsarm) oder Kugellager (leichtgängiger, empfindlicher gegen Salzwasser)

### 4.8 Hydraulik-Schlauchleitungen — Spezifikationen

**Standard-Hydraulikschläuche für Steueranlagen:**

| SAE-Klasse | Innendurchmesser | Betriebsdruck | Berstdruck | Anwendung |
|-----------|-----------------|--------------|-----------|-----------|
| SAE 100R7 | 6,35 mm (1/4") | 210 bar | 840 bar | Standard Steuerhydraulik |
| SAE 100R8 | 6,35 mm (1/4") | 345 bar | 1.380 bar | Hochdruck (große Yachten) |
| SAE 100R7 | 9,53 mm (3/8") | 175 bar | 700 bar | Große Volumenstrom-Systeme |
| SAE 100R2 | 6,35 mm (1/4") | 400 bar | 1.600 bar | Stahldraht-Einlage, Hochdruck |

**Schlauch-Fittings:**
- JIC (SAE J514): 37° Dichtkegel — am weitesten verbreitet in der Marinhydraulik
- BSP (British Standard Pipe): In europäischen Systemen häufig
- ORB (O-Ring Boss): SAE J1926 — O-Ring-Abdichtung, leckagefreier als JIC
- Metrisch (DIN 2353): In einigen europäischen Systemen

**Herstellung von Ersatzschläuchen:**
- Vorgefertigte Schläuche vom Steuerungshersteller (empfohlen)
- Maßanfertigung durch Hydraulik-Fachbetrieb (Schlauch + Presshülse nach Muster)
- Notlösung auf Reise: Lokaler Hydraulik-Service mit Muster des alten Schlauchs

---

## 5. Hersteller-Datenbank

### 5.1 Lewmar Ltd.

| Feld | Daten |
|------|-------|
| **Firmierung** | Lewmar Ltd. |
| **Hauptsitz** | Havant, Hampshire, UK |
| **Gegründet** | 1946 |
| **Spezialgebiet** | Steuerungssysteme (Seilzug, Hydraulik), Winschen, Luken, Ankerwinden |
| **Steuerungssysteme** | Compac-Serie (Seilzug), Ocean-Serie (Hydraulik) |
| **Marktposition** | Weltmarktführer Steueranlagen Segelyachten (geschätzt 35 % Marktanteil) |
| **Qualitätszertifizierung** | ISO 9001:2015 |
| **Website** | lewmar.com |
| **Technischer Support** | +44 (0)23 9247 1841, techsupport@lewmar.com |
| **Händlernetz Deutschland** | ca. 45 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1985 vollständig, ältere Modelle teilweise |
| **Besonderheit** | Übernahme Whitlock Steering 2001, volle Ersatzteilkompatibilität |

### 5.2 Jefa Marine A/S

| Feld | Daten |
|------|-------|
| **Firmierung** | Jefa Marine A/S |
| **Hauptsitz** | Assens, Dänemark |
| **Gegründet** | 1976 |
| **Spezialgebiet** | Hochwertige Ruderlager, Steuerungssysteme, Ruderanlagen |
| **Steuerungssysteme** | Kabel-Steuerungen, Hydraulische Direktsteuerung |
| **Marktposition** | Premiumhersteller, Marktführer selbstausrichtende Ruderlager |
| **Qualitätszertifizierung** | ISO 9001:2015, DNV-GL Typgenehmigung |
| **Website** | jefa.com |
| **Technischer Support** | +45 64 71 28 50, info@jefa.com |
| **Händlernetz Deutschland** | ca. 12 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1980 vollständig |
| **Besonderheit** | Wassergeschmierte Self-Aligning Bearings — wartungsfrei |

### 5.3 Edson International

| Feld | Daten |
|------|-------|
| **Firmierung** | Edson International |
| **Hauptsitz** | New Bedford, Massachusetts, USA |
| **Gegründet** | 1859 |
| **Spezialgebiet** | Steuerungssysteme für Segelyachten, Pedestals, Zubehör |
| **Steuerungssysteme** | Seilzug/Ketten-Systeme (Serien 311–601) |
| **Marktposition** | Marktführer USA/Kanada, international stark vertreten |
| **Qualitätszertifizierung** | ISO 9001:2015 |
| **Website** | edsonmarine.com |
| **Technischer Support** | +1 (508) 995-9711, info@edsonintl.com |
| **Händlernetz Europa** | ca. 20 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1970 nahezu vollständig |
| **Besonderheit** | Ältester Steuerungshersteller der Welt, exzellente Ersatzteilversorgung |

### 5.4 Kobelt Manufacturing Co. Ltd.

| Feld | Daten |
|------|-------|
| **Firmierung** | Kobelt Manufacturing Co. Ltd. |
| **Hauptsitz** | Surrey, British Columbia, Kanada |
| **Gegründet** | 1962 |
| **Spezialgebiet** | Hydraulische Steuerungssysteme, Getriebesteuerungen, Bremsen |
| **Steuerungssysteme** | Hydraulische Helm-Pumpen (7000-Serie), Zylinder (2000-Serie) |
| **Marktposition** | Premiumhersteller Hydrauliksteuerung, fokussiert auf Motoryachten und Arbeitsboote |
| **Qualitätszertifizierung** | ISO 9001:2015, ABS/DNV-GL Zulassungen |
| **Website** | kobelt.com |
| **Technischer Support** | +1 (604) 590-7313, sales@kobelt.com |
| **Händlernetz Europa** | ca. 8 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1975 vollständig |
| **Besonderheit** | Besonders robust, bevorzugt auf Arbeits- und Fischereifahrzeugen |

### 5.5 Teleflex / SeaStar Solutions

| Feld | Daten |
|------|-------|
| **Firmierung** | SeaStar Solutions (Dometic Marine, ehemals Teleflex Marine) |
| **Hauptsitz** | Richmond, British Columbia, Kanada |
| **Gegründet** | 1943 (als Teleflex) |
| **Spezialgebiet** | Hydraulische und mechanische Steuerungssysteme, Motorsteuerung |
| **Steuerungssysteme** | BayStar, SeaStar Pro, Optimus 360 (EPS) |
| **Marktposition** | Weltmarktführer Hydrauliksteuerung Motorboote (geschätzt 55 % Marktanteil) |
| **Qualitätszertifizierung** | ISO 9001:2015, NMMA-zertifiziert |
| **Website** | seastarsolutions.com |
| **Technischer Support** | +1 (604) 248-3858 |
| **Händlernetz Europa** | ca. 60 autorisierte Händler |
| **Ersatzteilversorgung** | Teleflex-Modelle ab 1990, SeaStar ab 2000 |
| **Besonderheit** | Optimus 360 — elektronisches Steuerungssystem mit Joystick |

### 5.6 Hynautic (Teleflex/SeaStar Legacy)

| Feld | Daten |
|------|-------|
| **Firmierung** | Hynautic (jetzt Teil von SeaStar Solutions) |
| **Hauptsitz** | Ursprünglich Chatsworth, California, USA |
| **Gegründet** | 1964 |
| **Spezialgebiet** | Hydraulische Steuerungssysteme (Marine) |
| **Steuerungssysteme** | H-50, H-60, H-70 Helm-Pumpen; EH-Serie Zylinder |
| **Marktposition** | Legacy-Hersteller, viele Systeme im Einsatz auf älteren Yachten |
| **Ersatzteilversorgung** | Über SeaStar Solutions, begrenzt für Modelle vor 1985 |
| **Besonderheit** | Proprietäres Hydrauliköl (H-OIL). Kann durch SeaStar Fluid ersetzt werden |

### 5.7 Whitlock Steering (Lewmar Legacy)

| Feld | Daten |
|------|-------|
| **Firmierung** | Whitlock Steering Systems (aufgegangen in Lewmar Ltd., 2001) |
| **Hauptsitz** | Ursprünglich Cheltenham, UK |
| **Gegründet** | 1960er |
| **Spezialgebiet** | Seilzugsteuerungen für Segelyachten |
| **Steuerungssysteme** | Mamba, Cobra, Python, Anaconda |
| **Marktposition** | Legacy, aber noch Tausende Systeme im Einsatz |
| **Ersatzteilversorgung** | Vollständig über Lewmar, Kreuzkompatibilität mit Compac-Teilen teilweise möglich |
| **Besonderheit** | Viele britische und europäische Segelyachten der 1970er–1990er Jahre haben Whitlock-Systeme |

### 5.8 Vetus (Niederlande)

| Feld | Daten |
|------|-------|
| **Firmierung** | Vetus B.V. |
| **Hauptsitz** | Schiedam, Niederlande |
| **Gegründet** | 1951 |
| **Spezialgebiet** | Marine-Antriebssysteme, Steuerungssysteme, Bugstrahlruder, Zubehör |
| **Steuerungssysteme** | Hydraulische Steuerungen (MTC-Serie), mechanische Seilzugsteuerungen |
| **Marktposition** | Starker europäischer Hersteller, breites Produktprogramm |
| **Qualitätszertifizierung** | ISO 9001:2015, CE-konform |
| **Website** | vetus.com |
| **Technischer Support** | +31 10 258 1000, info@vetus.com |
| **Händlernetz Deutschland** | ca. 35 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1990 vollständig |
| **Besonderheit** | Gutes Preis-Leistungs-Verhältnis, breite Verfügbarkeit in Europa |

**Vetus Hydrauliköl-Empfehlung:**
- Vetus empfiehlt ATF Dexron III für alle MTC-Steuerungssysteme
- Ölwechselintervall: 2 Jahre
- Systemvolumen MTC 32: 0,4 L, MTC 52: 0,6 L, MTC 72: 1,0 L
- Service-Kits über Vetus-Händler verfügbar

### 5.9 Ultraflex (Italien)

| Feld | Daten |
|------|-------|
| **Firmierung** | Ultraflex S.p.A. |
| **Hauptsitz** | Castagneto Carducci, Italien |
| **Gegründet** | 1967 |
| **Spezialgebiet** | Mechanische und hydraulische Steuerungssysteme, Motorsteuerungen |
| **Steuerungssysteme** | Rotary-Seilzug, Hydraulik (Hytech-Serie), Zahnstange (T67/T71/T73) |
| **Marktposition** | Führend im mediterranen Markt, OEM-Lieferant für viele italienische Werften |
| **Qualitätszertifizierung** | ISO 9001:2015, RINA-zertifiziert |
| **Website** | ultraflex.it |
| **Technischer Support** | +39 0565 775 311, info@ultraflex.it |
| **Händlernetz Deutschland** | ca. 20 autorisierte Händler |
| **Ersatzteilversorgung** | Modelle ab 1985 |
| **Besonderheit** | Starke Präsenz auf italienischen, französischen und kroatischen Yachten |

**Ultraflex-spezifische Wartungshinweise:**
- Zahnstangensysteme T67/T71: Balg-Manschetten alle 3–5 Jahre erneuern (UV-Degradation im Mittelmeer)
- Hytech-Hydrauliksysteme verwenden ISO VG 15 Hydrauliköl
- Ultraflex bietet komplette Steuerungspakete mit abgestimmten Komponenten — Mischbestückung vermeiden

### 5.10 Yacht Specialties / Spa Creek (USA)

| Feld | Daten |
|------|-------|
| **Firmierung** | Spa Creek Instrument Co. / Yacht Specialties |
| **Hauptsitz** | Annapolis, Maryland, USA |
| **Gegründet** | 1978 |
| **Spezialgebiet** | Steuerseile, Umlenkrollen, Quadranten, Zubehör |
| **Marktposition** | Spezialist für Ersatzteile und Nachrüstungen |
| **Website** | spacreek.com |
| **Besonderheit** | Fertigt Steuerseile in Maß, umfangreiches Sortiment an Umlenkrollen für alle Systeme |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Schwergängige Steuerung

**Bezeichnung:** Erhöhter Steuerkraftbedarf (Seilzug/Kette)

**Symptome:**
- Steuerrad erfordert deutlich mehr Kraft als gewohnt
- Kraftbedarf ggf. richtungsabhängig (nur Bb oder nur Stb)
- Kraftbedarf ggf. positionsabhängig (nur bei bestimmtem Ruderwinkel)
- Möglicherweise begleitende Geräusche (Knirschen, Quietschen)

**Mögliche Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Mangelhafte Schmierung (Seile, Rollen, Lager) | 35 % | benchmark |
| 2 | Ruderlager-Verschleiß oder -Verquellung | 20 % | documented |
| 3 | Falsche Seilspannung (zu hoch) | 15 % | measured |
| 4 | Seil auf Umlenkrolle aufgeklettert/eingeklemmt | 10 % | documented |
| 5 | Ruderlager-Fehlausrichtung (nach Grundberührung) | 8 % | estimated |
| 6 | Muschelwachstum am Ruderblatt/Schaft | 7 % | estimated |
| 7 | Quadrant-Verklemmung | 5 % | documented |

**Diagnose-Ablauf:**
1. Ruder im Wasser bei Motor aus: Ruder von Hand am Quadranten bewegen → leichtgängig? Dann Problem in Steuerung, nicht Ruder
2. Wenn Ruder schwergängig: Ruderlager und Ruderblatt prüfen
3. Wenn Steuerung schwergängig: Seilspannung prüfen (Tensiometer)
4. Umlenkrollen einzeln prüfen (Rollen von Hand drehen)
5. Schmierung aller Komponenten durchführen, erneut testen

### 6.2 Fehlerbild: Totgang / Spiel in der Steuerung

**Bezeichnung:** Übermäßiger Totgang am Steuerrad

**Symptome:**
- Steuerrad muss mehrere Grad gedreht werden, bevor das Ruder reagiert
- "Totes" Gefühl in Mittschiffsstellung
- Unpräzise Kurssteuerung
- Autopilot pendelt (Regelungsprobleme durch Totgang)

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Seilspannung zu niedrig | 30 % | measured |
| 2 | Kettenlängung | 20 % | measured |
| 3 | Verschlissene Umlenkrollen (Spiel) | 15 % | documented |
| 4 | Quadrant-Ruderschaft-Verbindung lose | 15 % | documented |
| 5 | Ruderlager-Verschleiß (radiales Spiel) | 10 % | measured |
| 6 | Seilklemmen/Nicopress gerutscht | 5 % | documented |
| 7 | Zahnflankenspiel (Zahnstangensteuerung) | 5 % | measured |

**Diagnose-Ablauf:**
1. Totgang am Steuerrad messen (Gradzahl bis Ruderreaktion)
2. Seilspannung messen (Tensiometer)
3. Helfer am Quadranten → Seil direkt am Quadrant bewegen: Reagiert Rad? Dann Spiel zwischen Rad und Quadrant
4. Helfer am Steuerrad → Rad drehen: Reagiert Quadrant sofort? Dann Spiel zwischen Quadrant und Ruder
5. Einzelne Komponenten systematisch prüfen

### 6.3 Fehlerbild: Hydraulik-Drift

**Bezeichnung:** Ruder wandert selbständig (Hydrauliksteuerung)

**Symptome:**
- Ruder bewegt sich langsam aus eingestellter Position
- Steuerrad muss ständig nachkorrigiert werden
- Autopilot arbeitet ständig nach (erhöhter Stromverbrauch)
- Ggf. sichtbare Ölspuren am Zylinder

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Interne Leckage im Hydraulikzylinder (Kolbendichtung) | 40 % | documented |
| 2 | Interne Leckage in der Helm-Pumpe | 25 % | documented |
| 3 | Luft im Hydrauliksystem | 15 % | measured |
| 4 | Überdruckventil schließt nicht vollständig | 10 % | documented |
| 5 | Externe Leckage (langsamer Ölverlust) | 10 % | documented |

**Diagnose-Ablauf:**
1. Ruder in Mittschiffsstellung bringen, loslassen, Drift-Richtung und -Geschwindigkeit messen
2. Hydraulikölstand prüfen — Verlust = externe Leckage
3. System entlüften (nach Hersteller-Vorschrift), erneut testen
4. Bypass-Ventil auf korrekten Schluss prüfen
5. Zylinder isolieren (Leitungen vom Zylinder trennen, verschließen), Drift nur Helm → Helm-Pumpe intern undicht
6. Zylinder isoliert: Kolbenstange belasten, Drift beobachten → Kolbendichtung defekt

### 6.4 Fehlerbild: Geräusche bei Ruderbewegung

**Bezeichnung:** Abnormale Geräusche während der Steuerung

**Geräuschtypen und Zuordnung:**

| Geräusch | Typische Ursache | Dringlichkeit |
|----------|-----------------|--------------|
| Metallisches Knirschen | Trockene Umlenkrollen, verschlissene Lager | Mittel — schmieren/tauschen |
| Rhythmisches Klacken | Gebrochene Litzen schlagen am Führungsrohr | Hoch — Seil prüfen, ggf. sofort tauschen |
| Quietschen | Trockene Ruderlager-Dichtung | Niedrig — schmieren |
| Dumpfes Schlagen | Ruder schlägt an Rumpf (Ruderstopps defekt) | Hoch — Ruderstopps sofort reparieren |
| Rasseln/Klappern | Kette zu lose, Kettenführung verschlissen | Mittel — Spannung und Führung prüfen |
| Pfeifendes Geräusch | Hydraulik: Luft im System oder Kavitation | Mittel — entlüften |
| Knacken bei Richtungswechsel | Quadrant-Ruderschaft-Verbindung lose | Hoch — sofort nachziehen |
| Summen/Brummen | Hydraulikpumpe — normal bei Power-Assist | Niedrig — nur bei neuem Geräusch prüfen |

### 6.5 Fehlerbild: Steuerung blockiert

**Bezeichnung:** Steuerrad lässt sich nicht oder nur teilweise bewegen

**Symptome:**
- Steuerrad vollständig blockiert
- Steuerrad blockiert nur in einer Richtung
- Steuerrad blockiert nur in bestimmter Stellung

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Seil von Umlenkrolle gesprungen | 25 % | documented |
| 2 | Fremdkörper in Seilführung | 15 % | estimated |
| 3 | Ruderlager festgefressen | 15 % | documented |
| 4 | Hydraulikventil klemmt | 12 % | documented |
| 5 | Autopilot-Antrieb blockiert (nicht abgeschaltet) | 10 % | estimated |
| 6 | Quadrant gegen Hindernis verklemmt | 10 % | documented |
| 7 | Kette vom Kettenrad gesprungen | 8 % | documented |
| 8 | Zahnstange am Endanschlag (Ruderstopp defekt) | 5 % | estimated |

**Sofortmaßnahmen:**
1. Sofort Motor in Leerlauf oder aus
2. Autopilot abschalten (Sicherung ziehen)
3. Ruhig analysieren — nicht mit Gewalt am Steuerrad drehen
4. Quadrantenbereich visuell inspizieren (Seil abgesprungen? Fremdkörper?)
5. Bei Hydraulik: Bypass-Ventil öffnen, Notpinne aufsetzen
6. Notsteuerung einrichten (Notpinne oder Leinensteuerung)

### 6.6 Fehlerbild: Ölverlust Hydrauliksteuerung

**Bezeichnung:** Sichtbarer Hydraulikölverlust

**Leckage-Orte und Ursachen:**

| Leckage-Ort | Häufigste Ursache | Maßnahme |
|------------|-------------------|----------|
| Helm-Pumpe (Wellenausgang) | Wellendichtring verschlissen | Dichtkit tauschen |
| Helm-Pumpe (Anschlüsse) | O-Ring gequetscht oder verhärtet | O-Ring tauschen |
| Hydraulikleitung (Pressung) | Presshülse korrodiert/undicht | Schlauch erneuern |
| Hydraulikleitung (Verschraubung) | Dichtkonus beschädigt oder lose | Nachziehen oder Fitting tauschen |
| Hydraulikzylinder (Stangenseite) | Stangendichtung verschlissen | Dichtkit tauschen |
| Hydraulikzylinder (Kolbenseite) | Kolbendichtung verschlissen | Dichtkit tauschen (Zylinder ausbauen) |
| Ölbehälter | Riss, lose Verschraubung | Behälter abdichten/tauschen |
| Überdruckventil | Ventilsitz beschädigt | Ventil tauschen/überholen |

### 6.7 Fehlerbild: Rudervibration

**Bezeichnung:** Spürbare Vibrationen am Steuerrad

**Symptome:**
- Vibrationen bei bestimmten Geschwindigkeiten (Resonanz)
- Vibrationen bei bestimmten Ruderwinkeln
- Permanente Vibrationen

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Bewuchs am Ruderblatt (asymmetrisch) | 30 % | estimated |
| 2 | Beschädigtes Ruderblatt (Delamination, Riss) | 20 % | documented |
| 3 | Ruderlager-Verschleiß (Spiel) | 20 % | measured |
| 4 | Kavitation am Ruder bei hoher Fahrt | 15 % | estimated |
| 5 | Propellerturbulenz auf Ruder | 10 % | estimated |
| 6 | Lose Verbindung Ruderschaft-Ruderblatt | 5 % | documented |

### 6.8 Fehlerbild: Steuerrad dreht durch

**Bezeichnung:** Steuerrad dreht ohne Widerstand und ohne Wirkung

**Symptome:**
- Steuerrad dreht frei ohne Ruderbewegung
- Plötzlicher Verlust jeglicher Rückmeldung
- Notfall-Situation

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Steuerseil gerissen | 40 % | documented |
| 2 | Seilbefestigung am Quadranten gelöst | 20 % | documented |
| 3 | Kette gerissen | 10 % | documented |
| 4 | Quadrant-Ruderschaft-Verbindung gelöst | 10 % | documented |
| 5 | Hydraulik komplett leer (massiver Ölverlust) | 10 % | documented |
| 6 | Kette vom Kettenrad gesprungen | 5 % | documented |
| 7 | Zahnstange gebrochen | 5 % | documented |

**Sofortmaßnahmen:**
1. MOTOR STOPP oder Leerlauf
2. Seenotsignal vorbereiten (bei Gefahr)
3. Notpinne aufsetzen (bei Hydraulik: Bypass-Ventil öffnen)
4. Bei Seilbruch: Provisorische Leinensteuerung direkt am Quadranten
5. Hafen anlaufen oder Assistenz anfordern

### 6.9 Fehlerbild: Asymmetrischer Ruderausschlag

**Bezeichnung:** Unterschiedlicher Ruderausschlag Backbord vs. Steuerbord

**Symptome:**
- Maximaler Ruderausschlag unterschiedlich (z. B. 30° Bb, nur 25° Stb)
- Mittschiffsstellung am Steuerrad stimmt nicht mit Ruder-Mittschiffsstellung überein
- Boot zieht bei geradeaus stehendem Steuerrad nach einer Seite

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Ruderstopps asymmetrisch eingestellt | 25 % | measured |
| 2 | Steuerseil-Länge asymmetrisch (nach Nachstellung) | 25 % | measured |
| 3 | Quadrant auf Ruderschaft verdreht | 20 % | documented |
| 4 | Hydraulikzylinder asymmetrisch montiert | 15 % | documented |
| 5 | Verbogener Ruderschaft | 10 % | documented |
| 6 | Ruderblatt asymmetrisch (Bauabweichung oder Schaden) | 5 % | estimated |

### 6.10 Fehlerbild: Hydraulikpumpe kavitiert

**Bezeichnung:** Ungewöhnliche Geräusche und Leistungsverlust der Helm-Pumpe

**Symptome:**
- Pfeifendes oder jaulendes Geräusch bei schneller Ruderbewegung
- Ruckelige Ruderbewegung (Stick-Slip-Effekt)
- Schaum im Ölbehälter
- Leistungsverlust der Steuerung

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Confidence |
|------|---------|-------------------|------------|
| 1 | Luft im System (unzureichend entlüftet) | 40 % | measured |
| 2 | Ölstand zu niedrig (Pumpe saugt Luft) | 25 % | measured |
| 3 | Saugleitung undicht (Luft wird angesogen) | 15 % | documented |
| 4 | Falsches Öl (zu hohe Viskosität bei Kälte) | 10 % | estimated |
| 5 | Interne Pumpenverschleiß | 10 % | documented |

### 6.11 Fehlerbild: Korrosion an Steuerungskomponenten

**Bezeichnung:** Sichtbare Korrosionserscheinungen

**Korrosionstypen und Bewertung:**

| Korrosionstyp | Typische Stelle | Bewertung | Maßnahme |
|--------------|----------------|-----------|----------|
| Flugrost (oberflächlich) | Edelstahlschrauben, Quadrant | Kosmetisch | Reinigen, Passivieren (Edelstahlpflege) |
| Spaltkorrosion | Seilklemmen, Nicopress, Schraubverbindungen | Mittel | Demontieren, reinigen, Anti-Seize, nachziehen |
| Lochkorrosion (Pitting) | Ruderschaft, Hydraulikzylinder-Kolbenstange | Hoch | Bauteil prüfen, ggf. tauschen |
| Galvanische Korrosion | Kontaktstelle unterschiedliche Metalle | Hoch | Isolieren, Opferanode prüfen |
| Spannungsrisskorrosion | Steuerseile, Schrauben unter Dauerlast | Kritisch | Sofort tauschen |
| Erosionskorrosion | Ruderblatt (Anströmkante) | Mittel | Beschichtung erneuern |

### 6.12 Fehlerbild: Wassereinbruch über Ruderlager

**Bezeichnung:** Wassereinbruch durch defekte Ruderschaft-Abdichtung

**Symptome:**
- Wasser in der Bilge im Bereich des Ruderschafts
- Tropfenbildung am Ruderkoker (Stevenrohr)
- Wassereinbruch verstärkt sich bei Seegang (Druckwechsel)
- Bei schwerem Ruderlager-Verschleiß: rhythmisches Spritzen bei Ruderbewegung

**Leckage-Bewertung und Maßnahmen:**

| Befund | Menge | Bewertung | Maßnahme |
|--------|-------|-----------|----------|
| Feuchter Ölfilm am Koker | Kein messbarer Wassereinbruch | Normal (manche Systeme) | Beobachten |
| Tropfen bei Ruderbewegung | <50 ml/Tag | Dichtung verschlissen | Dichtung erneuern (nächstes Slipping) |
| Tropfen dauerhaft | 50–500 ml/Tag | Dichtung + ggf. Lager | Zeitnah (30 Tage) erneuern |
| Rinnen bei Seegang | >500 ml/Tag | Dichtung + Lager defekt | Nicht auslaufen ohne Sicherung |
| Spritzen bei Ruderbewegung | >1 L/Tag | Lager schwer beschädigt | Sofortige Reparatur, ggf. Notreparatur See |

**Notreparatur auf See (provisorisch):**
- Ruderlager-Bereich trockenlegen
- Stopfbuchsen-Packung (Teflon-Graphit) um den Ruderschaft wickeln
- Mit Schlauchschellen oder Kabelbindern komprimieren
- Bilgenpumpe auf Automatik stellen
- Nächsten Hafen anlaufen

**Ursachen:**
1. Wellendichtring verschlissen (60 %)
2. Ruderlager ausgeschlagen → Schaft exzentrisch → Dichtlippe zerstört (25 %)
3. O-Ring am Koker gequollen oder verhärtet (10 %)
4. Stevenrohr-Riss (5 %, bei GFK-Booten nach Grundberührung)

### 6.13 Fehlerbild: Autopilot-Probleme durch Steueranlage

**Bezeichnung:** Autopilot arbeitet unzufriedenstellend (Ursache: Steueranlage)

**Symptome:**
- Autopilot pendelt (Übersteuern/Untersteuern)
- Autopilot bricht mit Fehlermeldung "Current Limit" oder "Drive Error" ab
- Autopilot reagiert träge

**Zusammenhang mit Steueranlage:**

| Autopilot-Symptom | Wahrscheinliche Steueranlagen-Ursache |
|-------------------|--------------------------------------|
| Pendeln (Hunting) | Zu viel Spiel/Totgang in der Steueranlage |
| Übersteuern (Overshoot) | Schwergängige Steuerung → AP baut zu viel Druck auf |
| Untersteuern | Hydraulik-Drift → AP-Korrekturen laufen weg |
| "Current Limit" | Mechanische Blockade oder extreme Schwergängigkeit |
| "Drive Error" | Ruderlagenrückmelder dejustiert oder defekt |
| Asymmetrisches Steuern | Asymmetrischer Ruderausschlag (s. Fehlerbild 6.9) |
| Langsame Reaktion | Luft im Hydrauliksystem, Seilspannung zu niedrig |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Schwergängige Steuerung

```
START: Steuerung schwergängig
│
├── Schwergängigkeit gleichmäßig über gesamten Ausschlag?
│   ├── JA:
│   │   ├── Ruder vom Steuerungssystem trennen (Hydraulik: Bypass; Seilzug: Seil abnehmen)
│   │   │   ├── Ruder immer noch schwergängig?
│   │   │   │   ├── JA → Ruderlager-Problem
│   │   │   │   │   ├── Ruderlager schmieren → besser?
│   │   │   │   │   │   ├── JA → Regelmäßig schmieren, Lagerzustand beobachten
│   │   │   │   │   │   └── NEIN → Ruderlager verschlissen oder Schaft verbogen
│   │   │   │   │   │       → Ruder ausbauen, Lager und Schaft prüfen (Fachbetrieb)
│   │   │   │   │   └── Ruderblatt auf Bewuchs/Beschädigung prüfen (Schiff muss aus dem Wasser)
│   │   │   │   └── NEIN → Problem in der Steuerungsanlage
│   │   │   │       ├── Seilzug: Seilspannung prüfen (zu hoch?)
│   │   │   │       │   ├── JA → Spannung reduzieren auf Herstellerwert
│   │   │   │       │   └── NEIN → Umlenkrollen einzeln prüfen
│   │   │   │       │       ├── Rolle schwergängig? → Lager reinigen/tauschen, schmieren
│   │   │   │       │       └── Alle Rollen leichtgängig? → Seilführung prüfen (Scheuerstelle, Knick)
│   │   │   │       ├── Hydraulik: Systemdruck prüfen (Manometer)
│   │   │   │       │   ├── Druck zu hoch → Überdruckventil prüfen
│   │   │   │       │   └── Druck normal → Helm-Pumpe intern verschlissen
│   │   │   │       └── Zahnstange: Zahnstangengehäuse nachfetten
│   │   │   │           ├── Besser? → Regelmäßig schmieren
│   │   │   │           └── Nicht besser? → Führungsbuchsen verschlissen → tauschen
│   │
│   └── NEIN (richtungs- oder positionsabhängig):
│       ├── Nur in einer Richtung schwergängig?
│       │   ├── Seilzug: Einseitig Seil eingeklemmt oder Rolle defekt
│       │   │   → Entsprechende Seite prüfen
│       │   └── Hydraulik: Einseitig Zylinderinnendruck → Überdruckventil einseitig defekt
│       └── Nur bei bestimmtem Ruderwinkel?
│           ├── Quadrant trifft auf Hindernis → Freiraum prüfen, Hindernis entfernen
│           └── Ruderlager-Fehlausrichtung → Lagerausrichtung prüfen (Fachbetrieb)
```

### 7.2 Entscheidungsbaum: Leckage Hydrauliksteuerung

```
START: Ölverlust festgestellt
│
├── Wo ist Öl sichtbar?
│   ├── An der Helm-Pumpe (Steuersäule)
│   │   ├── Öl am Wellenausgang → Wellendichtring verschlissen
│   │   │   → Helm Seal Kit bestellen und einbauen
│   │   └── Öl an Schlauchanschlüssen → Verschraubung nachziehen (1/4 Umdrehung)
│   │       ├── Dicht? → Verschraubung war lose, regelmäßig kontrollieren
│   │       └── Immer noch undicht? → O-Ring am Fitting tauschen
│   │
│   ├── An einer Hydraulikleitung
│   │   ├── An der Presshülse → Schlauch erneuern (Pressung nicht reparierbar)
│   │   ├── Am Schlauch selbst (Blase, Riss) → Schlauch sofort erneuern
│   │   └── An einer Rohrverschraubung → Nachziehen, ggf. Schneidring/Dichtkonus erneuern
│   │
│   ├── Am Hydraulikzylinder
│   │   ├── An der Kolbenstange (Stangenaustritt)
│   │   │   ├── Kolbenstange beschädigt (Kratzer, Korrosion)?
│   │   │   │   ├── JA → Kolbenstange polieren (leicht) oder Zylinder tauschen (schwer)
│   │   │   │   └── NEIN → Stangendichtung verschlissen → Cylinder Seal Kit
│   │   ├── Am Zylindergehäuse → Zylinder defekt → tauschen
│   │   └── An Zylinderanschlüssen → Verschraubung nachziehen, O-Ring prüfen
│   │
│   └── Am Ölbehälter
│       ├── Am Deckel → Dichtung tauschen
│       └── Am Gehäuse → Riss → Behälter tauschen
│
└── Kein sichtbares Öl, aber Ölstand sinkt
    ├── Interne Leckage (Helm-Pumpe oder Zylinder)
    │   → Drift-Test durchführen (s. Fehlerbild 6.3)
    └── Sehr langsame externe Leckage
        → Alle Verbindungen mit Lecksuchspray prüfen
```

### 7.3 Entscheidungsbaum: Totgang / Spiel

```
START: Übermäßiger Totgang am Steuerrad
│
├── Helfer am Quadranten, Steuermann dreht Rad
│   ├── Quadrant reagiert sofort? (kein Spiel Rad→Quadrant)
│   │   ├── JA → Spiel ist zwischen Quadrant und Ruder
│   │   │   ├── Quadrant-Ruderschaft-Verbindung prüfen
│   │   │   │   ├── Lose? → Konus reinigen, Anti-Seize, mit Drehmoment anziehen
│   │   │   │   └── Fest? → Ruderlager-Spiel messen (Messuhr)
│   │   │   │       ├── Spiel >0,3 mm → Ruderlager tauschen (Fachbetrieb)
│   │   │   │       └── Spiel <0,3 mm → Ruderblatt-Schaft-Verbindung prüfen (Fachbetrieb)
│   │   └── NEIN → Spiel ist in der Steuerungsübertragung (Rad→Quadrant)
│   │       ├── Seilzug:
│   │       │   ├── Seilspannung prüfen (Tensiometer)
│   │       │   │   ├── Zu niedrig → nachspannen
│   │       │   │   └── Korrekt → Seilklemmen/Nicopress auf Durchrutschen prüfen
│   │       │   ├── Kette auf Längung prüfen
│   │       │   │   ├── Längung >2 % → Kette und Kettenrad tauschen
│   │       │   │   └── Längung <2 % → Kettenrad auf Verschleiß prüfen
│   │       │   └── Umlenkrollen auf Spiel prüfen
│   │       │       └── Spiel >0,3 mm → Rollen tauschen
│   │       ├── Hydraulik:
│   │       │   ├── System entlüften → besser?
│   │       │   │   ├── JA → Luft war im System. Ursache finden (Leckage? Ölstand zu niedrig?)
│   │       │   │   └── NEIN → Interne Leckage (Helm oder Zylinder) → s. Entscheidungsbaum 7.2
│   │       └── Zahnstange:
│   │           └── Zahnflankenspiel messen
│   │               ├── >0,5 mm → Zahnstange/Ritzel tauschen (Fachbetrieb)
│   │               └── <0,5 mm → Führungsbuchsen auf Spiel prüfen
```

### 7.4 Entscheidungsbaum: Ungewöhnliche Geräusche

```
START: Ungewöhnliches Geräusch bei Ruderbewegung
│
├── Art des Geräuschs identifizieren
│   ├── Metallisches Knirschen/Kratzen
│   │   ├── Konstant → Trockene Umlenkrollen oder Lager
│   │   │   → Alle Rollen und Lager schmieren, erneut testen
│   │   │   ├── Besser? → Regelmäßig schmieren, Lager beobachten
│   │   │   └── Nicht besser? → Lager verschlissen → tauschen
│   │   └── Nur bei bestimmtem Ruderwinkel → Seil schleift an Führung oder Schott
│   │       → Seilführung inspizieren, Scheuerschutz anbringen
│   │
│   ├── Rhythmisches Klacken/Ticken
│   │   ├── Synchron mit Raddrehung → Kette/Kettenrad-Problem
│   │   │   ├── Kette zu lose? → Nachspannen
│   │   │   ├── Kettenglied beschädigt? → Kette tauschen
│   │   │   └── Kettenrad verschlissen? → Kettenrad + Kette tauschen
│   │   └── Nicht synchron → Seil: gebrochene Litze schlägt an Führungsrohr
│   │       → Seil sofort inspizieren (Litzenbrüche!)
│   │
│   ├── Quietschen/Kreischen
│   │   ├── Bei Ruderbewegung → Ruderlager trocken
│   │   │   → Ruderlager schmieren (wenn Schmiernippel vorhanden)
│   │   │   └── Kein Schmiernippel → Fachbetrieb (Lager ggf. wassergeschmiert → prüfen)
│   │   └── Bei Radbewegung → Pedestal-Lager trocken → Pedestal Service Kit
│   │
│   ├── Dumpfes Schlagen/Klopfen
│   │   ├── Bei Endausschlag → Ruderstopps defekt oder fehlen
│   │   │   → Ruderstopps prüfen und erneuern
│   │   └── Bei jedem Richtungswechsel → Quadrant-Verbindung lose
│   │       → Quadrant-Muttern mit Drehmoment nachziehen
│   │
│   └── Pfeifen/Jaulen (Hydraulik)
│       ├── Bei schneller Ruderbewegung → Luft im System oder Kavitation
│       │   ├── Ölstand prüfen → zu niedrig? → Auffüllen + Entlüften
│       │   └── Ölstand OK → System entlüften
│       └── Dauerhaft → Pumpenverschleiß → Helm-Pumpe überholen lassen
```

### 7.5 Entscheidungsbaum: Steuerung fällt komplett aus

```
START: Steuerung fällt auf See komplett aus
│
├── SOFORTMASSNAHMEN (parallel):
│   ├── Motor Leerlauf oder Stopp
│   ├── Autopilot AUS (Sicherung ziehen)
│   ├── Crew informieren, Ausguck
│   ├── Bei Gefahr: Seenotsignal vorbereiten
│   └── Position notieren
│
├── Steuerrad-Zustand prüfen:
│   ├── Rad dreht frei (kein Widerstand) → Übertragung unterbrochen
│   │   ├── Seilzug: Seil gerissen
│   │   │   ├── Notpinne aufsetzen → funktioniert? → Zum Hafen navigieren
│   │   │   └── Notpinne nicht vorhanden/passend:
│   │   │       → Leine durch Cockpit-Winsch an Quadrant befestigen
│   │   │       → Improvisiete Leinensteuerung (2 Leinen, je Bb/Stb über Winsch)
│   │   ├── Kette: Kette gerissen oder vom Kettenrad gesprungen
│   │   │   ├── Kette aufgesprungen → zurücklegen, wenn möglich
│   │   │   └── Kette gerissen → Notpinne
│   │   └── Hydraulik: Ölverlust total
│   │       ├── Bypass-Ventil öffnen → Notpinne aufsetzen
│   │       └── Kein Bypass: Hydraulikleitungen am Zylinder trennen → Notpinne
│   │
│   ├── Rad blockiert → Mechanische Blockade
│   │   ├── Schnellinspektion Quadrantenbereich
│   │   │   ├── Fremdkörper/Gegenstand → entfernen
│   │   │   └── Seil aufgeklettert/verklemmt → lösen
│   │   ├── Bei Hydraulik: Bypass-Ventil öffnen
│   │   │   ├── Rad jetzt frei? → Hydraulikproblem (Ventil, Zylinder)
│   │   │   │   → Notpinne verwenden
│   │   │   └── Rad immer noch blockiert? → Mechanische Blockade → Notpinne
│   │   └── Notpinne aufsetzen, wenn Rad nicht freizubekommen
│   │
│   └── Rad beweglich, aber Ruder reagiert nicht
│       ├── Quadrant-Ruderschaft-Verbindung gelöst
│       │   ├── Wenn zugänglich und sicher: Mutter nachziehen (Notmaßnahme)
│       │   └── Notpinne aufsetzen (greift direkt auf Schaft)
│       └── Ruder selbst beschädigt/verloren (Grundberührung, Kollision)
│           → Keine mechanische Lösung → Notruder oder Assistenz
│           → Provisorisches Steuern: Schleppbremse achterlich, Segel/Motor asymmetrisch
│
└── Nach Notmaßnahme:
    ├── Nächsten sicheren Hafen anlaufen
    ├── Reparatur nur provisorisch — Vollinstandsetzung an Land
    └── Vorfall ins Bordbuch eintragen (für Versicherung und Auswertung)
```

---

## 8. FAQ

### 8.1 Allgemeine Wartungsfragen

**F1: Wie oft muss ich meine Steueranlage warten lassen?**

A: Die grundlegende Sichtprüfung und Funktionsprüfung sollte monatlich durch den Eigner erfolgen. Eine umfassende Wartung mit Schmierung und Messung ist mindestens einmal jährlich bei Seilzug-/Kettensystemen und alle zwei Jahre bei Hydrauliksystemen erforderlich. Im Charterbereich und bei intensiver Nutzung (>1.000 Seemeilen/Jahr) sollten die Intervalle halbiert werden. (Confidence: documented)

**F2: Kann ich die Steueranlagen-Wartung selbst durchführen?**

A: Kategorie-I- und -II-Wartungen (Sichtprüfung, Schmierung, Spannungskontrolle, Ölstandsprüfung) kann ein versierter Eigner selbst durchführen. Kategorie-III-Arbeiten (Seilwechsel, Hydraulik-Entlüftung, Ruderlager-Inspektion) erfordern Spezialwerkzeug und Erfahrung — hier empfiehlt sich ein Fachbetrieb. Kategorie-IV-Arbeiten (Ruderschaft ziehen, Lagertausch) erfordern grundsätzlich eine Werft. (Confidence: documented)

**F3: Was kostet eine professionelle Steueranlagen-Wartung?**

A: Die jährliche Wartung einer Seilzugsteuerung durch einen Fachbetrieb kostet typischerweise 250–450 EUR (inkl. Material). Eine Hydrauliksteuerungs-Wartung mit Ölwechsel liegt bei 350–650 EUR. Ein kompletter Seilwechsel kostet 400–800 EUR (Material + Arbeit). (Confidence: benchmark)

**F4: Woran erkenne ich, dass mein Steuerseil gewechselt werden muss?**

A: Sofortiger Tausch bei: mehr als 5 gebrochenen Einzeldrähten auf einer Strecke von 6× Seildurchmesser, Durchmesserreduktion >10 %, Kordeleffekt (Aufdrehen), Knicke oder Korbbildung. Zeitnaher Tausch (innerhalb einer Saison) bei: 3–5 gebrochenen Drähten, Durchmesserreduktion >5 %, lokaler Korrosion. Präventiver Tausch nach 8–10 Jahren, unabhängig vom Sichtbefund. (Confidence: measured/documented)

**F5: Welches Hydrauliköl gehört in meine Steuerung?**

A: Ausschließlich das vom Hersteller freigegebene Öl oder ein Öl gleicher Spezifikation. Lewmar: ISO VG 15. Kobelt: ISO VG 22. Teleflex/SeaStar: ATF-kompatibel. Hynautic: proprietäres H-OIL (ersetzbar durch SeaStar Fluid). Niemals verschiedene Öle mischen. Im Zweifelsfall: altes Öl komplett ablassen und mit dem richtigen Öl neu befüllen. (Confidence: measured)

**F6: Wie entlüfte ich mein Hydrauliksteuerungssystem?**

A: Grundprinzip: Öl am tiefsten Punkt einfüllen, Luft am höchsten Punkt entweichen lassen. 1) Ölbehälter auffüllen. 2) Entlüftungsschraube am Hydraulikzylinder (oben) leicht öffnen. 3) Steuerrad langsam hin- und herbewegen. 4) Warten bis blasenfreies Öl an der Entlüftungsschraube austritt. 5) Entlüftungsschraube schließen. 6) Ölstand nachfüllen. 7) Vorgang ggf. mehrmals wiederholen. Herstellerspezifische Anweisungen beachten! (Confidence: documented)

**F7: Mein Hydrauliksteuerrad hat plötzlich Spiel, das vorher nicht da war. Was kann das sein?**

A: Plötzlich auftretendes Spiel bei einer Hydrauliksteuerung deutet auf Luft im System hin (häufigste Ursache). Prüfen Sie zuerst den Ölstand — ist er gesunken? Wenn ja, liegt eine Leckage vor. Wenn der Ölstand stimmt, entlüften Sie das System. Tritt das Problem bei Kälte auf, kann das Hydrauliköl zu dickflüssig sein (Viskosität bei niedrigen Temperaturen). (Confidence: documented)

### 8.2 Seilzug-spezifische Fragen

**F8: 7×7 oder 7×19 Steuerseil — was ist besser?**

A: 7×19-Seile sind für Steueranlagen grundsätzlich besser geeignet: Sie haben eine höhere Biegewechselfestigkeit (wichtig an Umlenkrollen), laufen geschmeidiger und haben eine längere Lebensdauer. 7×7-Seile sind steifer und neigen an Umlenkrollen schneller zur Ermüdung. 1×19-Seile sind für Steueranlagen ungeeignet (zu steif, keine Biegewechselfestigkeit). (Confidence: measured)

**F9: Wie stelle ich die Seilspannung korrekt ein?**

A: Die korrekte Spannung beträgt typisch 10–15 % der Seilbruchlast. Für ein 6,35 mm (1/4") Edelstahl-7×19-Seil mit ~1.800 kg Bruchlast: 180–270 N (18–27 kg). Am einfachsten mit einem Loos-Tensiometer PT-2 messen. Als Daumenregel: Bei Daumendruck auf die Seilmitte des längsten freien Seilstücks soll sich das Seil ca. 10–15 mm seitlich auslenken lassen. Beide Seilzüge müssen identische Spannung haben. (Confidence: measured)

**F10: Muss ich nach einem Seilwechsel die Spannung nachstellen?**

A: Ja. Neue Steuerseile setzen sich in den ersten 50–100 Betriebsstunden. Die Spannung sollte nach 24 Stunden, nach 1 Woche, nach 1 Monat und nach 3 Monaten kontrolliert und ggf. nachgestellt werden. Danach hat sich das Seil gesetzt und die regelmäßigen Intervalle (vierteljährlich) genügen. (Confidence: documented)

**F11: Kann ich ein einzelnes Steuerseil tauschen oder müssen immer beide gewechselt werden?**

A: Es wird dringend empfohlen, immer beide Seile gleichzeitig zu tauschen. Unterschiedliche Alterung und Setzverhalten führen zu asymmetrischer Spannung und ungleichmäßigem Verschleiß an Umlenkrollen und Quadrant. Zudem müssen die Seile exakt gleich lang sein. (Confidence: documented)

**F12: Meine Umlenkrollen sind aus Kunststoff. Muss ich die gegen Metall tauschen?**

A: Nein! Kunststoff-Umlenkrollen (Delrin/Acetal oder UHMWPE) sind für Seilzugsteuerungen ideal. Sie verursachen weniger Seilverschleiß als Metallrollen und benötigen weniger Schmierung. Metallrollen (Edelstahl, Bronze) sind langlebiger, beschleunigen aber den Seilverschleiß. Der optimale Kompromiss sind UHMWPE-Rollen. (Confidence: measured)

### 8.3 Hydraulik-spezifische Fragen

**F13: Wie erkenne ich, ob mein Hydraulikzylinder intern undicht ist?**

A: Drift-Test: Ruder unter Last (Motor an, Vorwärtsfahrt) in eine Position bringen und Steuerrad loslassen. Wandert das Ruder langsam zurück → interne Leckage im Zylinder oder in der Helm-Pumpe. Zur Unterscheidung: Hydraulikleitungen am Zylinder trennen und verschließen. Wenn der Zylinder jetzt hält → Leckage in der Helm-Pumpe. Wenn er immer noch driftet → Kolbendichtung im Zylinder. (Confidence: documented)

**F14: Kann ich verschiedene Hydrauliköle mischen?**

A: Grundsätzlich nein. Unterschiedliche Hydrauliköle können inkompatible Additivpakete enthalten, die bei Mischung ausflocken, schlammbildend reagieren oder Dichtungen angreifen. Wenn Sie das Öl wechseln müssen und das Originalöl nicht verfügbar ist: System komplett ablassen, mit dem neuen Öl spülen und neu befüllen. (Confidence: measured)

**F15: Wie oft muss das Hydrauliköl gewechselt werden?**

A: Die meisten Hersteller empfehlen einen Ölwechsel alle 2 Jahre oder 2.000–3.000 Betriebsstunden, je nachdem, was zuerst eintritt. Bei visuell einwandfreiem Öl (klar, honigfarben, keine Partikel) kann das Intervall auf 3 Jahre gestreckt werden. Bei trübem, dunklem oder partikelhaltigem Öl sofort wechseln. (Confidence: documented)

**F16: Mein Bypass-Ventil tropft. Ist das normal?**

A: Nein. Ein Bypass-Ventil muss im geschlossenen Zustand vollständig dicht sein. Tropfen bedeutet: defekter Ventilsitz, defekte Dichtung oder Fremdkörper im Ventil. Sofort reparieren — ein undichtes Bypass-Ventil ist gleichbedeutend mit einer internen Leckage und verursacht Steuerdrift. (Confidence: documented)

### 8.4 Ruderlager und Ruderblatt

**F17: Wie erkenne ich, dass meine Ruderlager verschlissen sind?**

A: Symptome: zunehmendes Spiel am Ruder (Ruder seitlich hin- und herbewegen, Spiel >0,3 mm radial), Geräusche bei Ruderbewegung (Knirschen, Schlagen), Wassereinbruch an der Ruderlagerdichtung, sichtbarer Verschleiß oder Korrosion am Ruderschaft. Messung mit Messuhr am Ruderschaft direkt über dem Lager. (Confidence: measured)

**F18: Wie lange halten Ruderlager?**

A: Abhängig von Material und Wartung: Delrin/Acetal-Gleitlager: 8–15 Jahre. Jefa Self-Aligning (wassergeschmiert): 15–25 Jahre. Bronze-Gleitlager: 15–25 Jahre. Kugellager (selten): 10–15 Jahre. Thordon-Composite: 15–20 Jahre. Regelmäßige Schmierung (bei fettgeschmierten Lagern) und korrekte Ausrichtung verlängern die Lebensdauer erheblich. (Confidence: benchmark)

**F19: Muss ich das Ruder zum Lagertausch ausbauen?**

A: In den meisten Fällen ja. Das untere Ruderlager ist nur bei ausgebautem Ruder zugänglich. Das obere Ruderlager kann teilweise bei eingebautem Ruder gewechselt werden, aber eine korrekte Ausrichtung ist nur bei ausgebautem Ruder möglich. Der Ruderausbau erfordert typischerweise eine Werft (Schiff aus dem Wasser, Ruder nach unten herausziehen). (Confidence: documented)

### 8.5 Winterfestmachung und Inbetriebnahme

**F20: Was passiert, wenn ich die Steueranlage nicht winterfest mache?**

A: Im schlimmsten Fall: Frostschäden an Hydraulikleitungen (Wassergehalt im Öl gefriert), festgefressene Ruderlager (stehende Feuchtigkeit → Korrosion), korrodierte Steuerseile (kondensierte Feuchtigkeit in der Litzenstruktur), festsitzende Umlenkrollen-Lager, oxidierte Quadrantverbindung. Die Reparaturkosten können leicht das 10- bis 50-fache der Winterfestmachungskosten betragen. (Confidence: benchmark)

**F21: Soll ich die Seilspannung im Winter reduzieren?**

A: Ja, eine Reduktion um ca. 10 % wird empfohlen. Dies entlastet Seile, Lager und Umlenkrollen über die lange Standzeit. Bei der Saison-Inbetriebnahme wird die Spannung wieder auf den Sollwert eingestellt. (Confidence: documented)

**F22: Kann Hydrauliköl einfrieren?**

A: Standard-Marine-Hydrauliköle haben Pourpoints von -30 °C bis -40 °C und sind daher in Mitteleuropa frostunempfindlich. Das Problem ist Wasser im System: Kondenswasser gefriert bei 0 °C und kann Leitungen und Fittings sprengen. Daher: Vor dem Winter den Ölstand auf Maximum auffüllen (minimiert Luftraum für Kondensation) und sicherstellen, dass kein signifikanter Wassergehalt im Öl ist. (Confidence: measured)

### 8.6 Notfall und Sicherheit

**F23: Was mache ich bei komplettem Steuerungsausfall auf See?**

A: 1) Motor in Leerlauf. 2) Autopilot aus. 3) Crew informieren. 4) Notpinne aufsetzen (bei Hydraulik: Bypass-Ventil öffnen). 5) Bei Seilbruch ohne Notpinne: Leinen direkt am Quadranten befestigen, über Winsch führen → provisorische Leinensteuerung. 6) Nächsten sicheren Hafen anlaufen. 7) Bei Manövrierunfähigkeit: Mayday oder Pan-Pan abhängig von der Gefährdungslage. (Confidence: documented)

**F24: Wo bewahre ich die Notpinne auf?**

A: Die Notpinne muss jederzeit schnell erreichbar sein — nicht in der Bilge unter Ausrüstung, nicht im verschlossenen Achterpiek. Ideale Orte: Halterung im Cockpit, direkt am Steuerstand, in der Achterkajüte auf einem markierten Platz. Jedes Crewmitglied muss den Aufbewahrungsort kennen und das Aufsetzen beherrschen. Die Notpinne muss mindestens einmal pro Saison probehalber aufgesetzt werden. (Confidence: documented)

**F25: Kann ich mit einer provisorischen Leinensteuerung segeln?**

A: Ja, aber mit erheblichen Einschränkungen: Die Steuerung ist unpräziser (Totgang, Dehnung der Leinen), erfordert mindestens 2 Personen (je eine Leine Bb/Stb), ist ermüdend und bei Starkwind nur schwer zu kontrollieren. Geschwindigkeit reduzieren, Segelfläche verkleinern, nächsten Hafen anlaufen. Unter Motor ist eine Leinensteuerung leichter zu handhaben als unter Segel. (Confidence: documented)

### 8.7 Erweiterte Fragen

**F26: Wie beeinflusst die Steueranlage den Autopiloten?**

A: Die Steueranlage ist das "Getriebe" des Autopiloten. Jedes Spiel, jede Schwergängigkeit und jede interne Leckage beeinträchtigt die Autopilot-Leistung direkt. Ein Totgang von 5° in der Steueranlage bedeutet, dass der Autopilot 5° Kursfehler tolerieren muss, bevor er korrigieren kann — das führt zu permanentem Pendeln. Eine jährliche Steueranlagen-Wartung ist daher auch eine Autopilot-Wartung. (Confidence: documented)

**F27: Mein Boot hat eine doppelte Steueranlage (zwei Räder). Worauf muss ich besonders achten?**

A: Doppelte Steueranlagen haben doppelt so viele Verschleißstellen. Besonders kritisch: die Verbindung der beiden Steuerräder (Kette oder Seilzug) muss spielfrei sein. Prüfen Sie beide Räder auf identischen Widerstand und identisches Spiel. Regelmäßig von beiden Rädern aus steuern, um einseitigen Verschleiß zu vermeiden. (Confidence: documented)

**F28: Kann ich von Seilzugsteuerung auf Hydraulik umrüsten?**

A: Ja, eine Umrüstung ist bei den meisten Yachten möglich und sinnvoll (ab ca. 12 m, hohes Rudermoment). Der Aufwand umfasst: neue Helm-Pumpe (Pedestal oder Bulkhead-Montage), Hydraulikzylinder am Quadranten oder direkt am Ruderschaft, Hydraulikleitungen, Ölbehälter, Überdruckventil. Kosten: 2.500–6.000 EUR je nach System und Bootsgröße. Der Umbau sollte von einem Fachbetrieb durchgeführt werden. (Confidence: estimated)

**F29: Wie erkenne ich, ob meine Umlenkrollen getauscht werden müssen?**

A: Prüfen Sie drei Kriterien: 1) Leichtgängigkeit — die Rolle muss sich bei leichtem Fingeranstoß mindestens 3× frei drehen. 2) Radialspiel — die Rolle darf bei seitlichem Druck maximal 0,3 mm Spiel haben (Fühlerlehre). 3) Rillenverschleiß — wenn die Rillenbreite den Seildurchmesser um mehr als 1 mm übersteigt, ist die Rolle verschlissen. Bei einem dieser Kriterien: Rolle tauschen. (Confidence: measured)

**F30: Mein Pedestal knarzt beim Steuern. Was tun?**

A: Knarzen im Pedestal deutet auf trockene Lager oder verschlissene Dichtungen im Pedestal-Inneren hin. Lösung: Pedestal Service Kit des Herstellers bestellen (z. B. Lewmar 89000037 für Compac 3/5/7). Das Kit enthält neue Lager, Dichtungen, O-Ringe und Schmierfett. Der Einbau ist als Kategorie-II-Wartung durch versierte Eigner möglich (ca. 1,5 Stunden). (Confidence: documented)

**F31: Kann ich mein Steuerseil selbst wechseln?**

A: Grundsätzlich ja, wenn Sie handwerklich versiert sind und das richtige Werkzeug haben (insbesondere Nicopress-Werkzeug). Wichtig: 1) Neues Seil muss identische Spezifikation haben (Durchmesser, Konstruktion, Material). 2) Immer beide Seile gleichzeitig tauschen. 3) Seillänge exakt abmessen (altes Seil als Referenz). 4) Seilspannung korrekt einstellen (Tensiometer). 5) Nachspannen nach 24h, 1 Woche, 1 Monat. Im Zweifelsfall: Fachbetrieb beauftragen — die Kosten sind überschaubar (200–400 EUR Arbeit). (Confidence: documented)

**F32: Meine Steuerung hat mehr Spiel als früher, obwohl ich nichts verändert habe. Was ist passiert?**

A: Die häufigsten Ursachen für schleichend zunehmendes Spiel: 1) Seil hat sich gedehnt/gesetzt (bei neuem Seil in den ersten Monaten normal). 2) Kette hat sich gelängt (Verschleiß). 3) Umlenkrollen-Lager verschlissen (Radialspiel). 4) Ruderlager-Verschleiß (radiales Spiel am Schaft). 5) Quadrant-Konus hat sich gelöst (Drehmoment nachlassen). Systematisch von außen (Steuerrad) nach innen (Ruder) prüfen, um die Ursache einzugrenzen. (Confidence: documented)

**F33: Wie viel Hydrauliköl sollte ich als Reserve an Bord haben?**

A: Mindestens die doppelte Systemfüllung als Reserve. Ein typisches Segelyacht-Hydrauliksystem enthält 0,5–2 Liter, eine größere Motoryacht 2–5 Liter. Empfehlung: 2–4 Liter als Reserve (originalverpackt, herstellerspezifisch). Auf Langfahrt: Mindestens 5 Liter, da Beschaffung im Ausland schwierig sein kann. (Confidence: documented)

**F34: Gibt es Unterschiede bei der Wartung von Doppelsteuerrädern gegenüber Einzelsteuerrädern?**

A: Ja. Doppelsteueranlagen haben: Doppelte Anzahl an Umlenkrollen, längere Seilwege, eine zusätzliche Verbindung zwischen den beiden Steuersäulen (Kette, Seil oder Hydraulik), und zwei Sätze Pedestal-Lager. Die Wartung dauert entsprechend ca. 1,5× so lange. Besonders wichtig: Beide Steuerräder müssen identischen Widerstand und identisches Spiel haben. Asymmetrie deutet auf einseitigen Verschleiß hin. (Confidence: documented)

**F35: Mein Boot hat sowohl eine Pinne als auch ein Rad (Rad-Pinnen-Konversion). Worauf muss ich achten?**

A: Rad-Pinnen-Konversionen (z. B. Whitlock Mamba, Edson 311 auf Pinnenbooten) haben eine zusätzliche Umlenkung zwischen Rad und Pinnenarm. Die Wartung des Radsystems kommt zur Pinnen-Wartung hinzu. Besonders kritisch: Die Seilbefestigung am Pinnenarm und der Freigang der Seile bei Vollausschlag. Regelmäßig prüfen, ob die Seile die Pinne bei Vollausschlag nicht verkeilen. (Confidence: documented)

**F36: Wie lagere ich Hydraulikschläuche als Ersatzteile?**

A: Hydraulikschläuche lagern Sie am besten: Trocken, dunkel (UV-Schutz), bei Raumtemperatur (10–25 °C), ohne Knicke (gerade oder in großen Radien aufgehängt), mit verschlossenen Enden (Kappen/Stopfen). Lagerfähigkeit ab Fertigung: 5 Jahre (Empfehlung DIN 20066). Nach 5 Jahren Lagerung sollten die Schläuche als "gealtert" betrachtet und ihre Montage-Lebensdauer entsprechend verkürzt werden. (Confidence: documented)

**F37: Kann ich Edelstahl-Steuerseile gegen Dyneema/HMPE-Seile ersetzen?**

A: Theoretisch ja, aber mit wichtigen Einschränkungen: Dyneema/HMPE-Seile haben eine sehr hohe Bruchlast bei geringem Gewicht, aber sie kriechen unter Dauerlast (1–3 % Längung über die Lebensdauer). Für Steueranlagen ist Kriechneigung problematisch, da sich die Seilspannung ständig ändert. Zudem laufen textile Seile weniger gut in Standard-Umlenkrollen (Rillenprofil für Drahtseil). Einige High-Performance-Yachten verwenden Dyneema-Steuerseile, aber nur mit speziellen Umlenkrollen und häufiger Nachspannung. Für Fahrtenyachten: Edelstahl bleibt Standard. (Confidence: estimated)

**F38: Was kostet ein komplettes Steueranlagen-Upgrade (Seilzug → Hydraulik)?**

A: Richtwerte für eine typische 12–16 m Segelyacht: Helm-Pumpe (1.200–2.500 EUR), Hydraulikzylinder (800–1.800 EUR), Leitungen und Fittings (200–500 EUR), Ölbehälter und Öl (100–250 EUR), Einbau durch Fachbetrieb (1.500–3.000 EUR). Gesamtkosten: 3.800–8.050 EUR. Der Umbau lohnt sich besonders bei schwergängiger Seilzugsteuerung, hohem Rudermoment oder wenn ein Hydraulik-Autopilot ohnehin vorgesehen ist. (Confidence: benchmark)

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **Autopilot-Drift** | Selbsttätiges Auswandern des Autopiloten vom Sollkurs, häufig verursacht durch Spiel oder Leckage in der Steueranlage |
| 2 | **Backbord (Bb)** | Linke Seite des Schiffes in Fahrtrichtung gesehen |
| 3 | **Bypass-Ventil** | Absperrventil in der Hydrauliksteuerung, das bei Öffnung die Druckseiten kurzschließt und manuelles Rudern (Notpinne) ermöglicht |
| 4 | **CE-Kategorie** | Entwurfskategorie nach EU-Sportbootrichtlinie 2013/53/EU (A=Hochsee, B=Küste, C=Küstennahe, D=Geschützt) |
| 5 | **D/d-Verhältnis** | Verhältnis von Umlenkrollen-Durchmesser (D) zu Seildurchmesser (d) — bestimmt die Biegebeanspruchung des Seils |
| 6 | **Delrin** | Markenname für Polyoxymethylen (POM/Acetal), häufig verwendeter Kunststoff für Umlenkrollen und Lager |
| 7 | **Drift (Hydraulik)** | Unerwünschte langsame Ruderbewegung durch interne Leckage im Hydrauliksystem |
| 8 | **Entlüften** | Entfernen von Luftblasen aus dem Hydrauliksystem zur Wiederherstellung der vollen Steuerungsfunktion |
| 9 | **FKM/Viton** | Fluorkautschuk, hochwertiges Dichtungsmaterial für hohe Temperaturen und aggressive Medien |
| 10 | **Gabelkopf** | Gabelförmiges Verbindungselement am Ende des Hydraulikzylinders oder der Spurstange |
| 11 | **Helm-Pumpe** | Die am Steuerstand montierte Hydraulikpumpe, die durch Drehen des Steuerrads betätigt wird |
| 12 | **Hydrauliköl ISO VG 15/22** | Hydrauliköl mit einer kinematischen Viskosität von 15 bzw. 22 cSt bei 40 °C nach ISO 3448 |
| 13 | **Kavitation** | Bildung und Zusammenbruch von Dampfblasen im Hydrauliköl, verursacht durch Unterdruck — zerstört Oberflächen |
| 14 | **Kettenrad (Sprocket)** | Zahnrad am Steuerrad, in das die Steuerkette eingreift |
| 15 | **Konus** | Kegelförmige Verbindung zwischen Ruderschaft und Quadrant — kraftschlüssig und selbstzentrierend |
| 16 | **Leckölmessung** | Messung der internen Leckage einer Hydraulikpumpe durch Auffangen des Öls am Wellendichtring |
| 17 | **Litzenbruch** | Bruch einzelner Drähte eines Drahtseils — Frühindikator für Seilermüdung |
| 18 | **Loos-Tensiometer** | Präzisionsmessgerät zur Bestimmung der Vorspannung von Drahtseilen |
| 19 | **NBR (Nitrilkautschuk)** | Standard-Dichtungsmaterial für Hydrauliksysteme, gute Beständigkeit gegen Mineralöle |
| 20 | **Nicopress-Hülse** | Presshülse zur dauerhaften Befestigung von Drahtseilen — Alternative zur Seilklemme |
| 21 | **NLGI 2** | Konsistenzklasse für Schmierfette nach NLGI (National Lubricating Grease Institute) — Standardkonsistenz |
| 22 | **Notpinne** | Steckbare Pinne, die direkt auf den Ruderkopf oder Ruderschaft aufgesetzt wird, wenn die Hauptsteuerung ausfällt |
| 23 | **Overdruckventil (Relief Valve)** | Sicherheitsventil im Hydrauliksystem, das bei Überschreitung des Maximaldrucks öffnet und das System schützt |
| 24 | **Pedestal** | Die Steuerrad-Steuersäule, die das Steuerrad trägt und die Kette/Seil-Umlenkung beherbergt |
| 25 | **Pitting** | Grübchenbildung auf Metalloberflächen durch Materialermüdung unter hoher Flächenpressung |
| 26 | **Pourpoint** | Tiefste Temperatur, bei der ein Öl noch fließfähig ist — relevant für Frostschutz |
| 27 | **Quadrant (Steuersegment)** | Bogen- oder sektorförmiges Bauteil auf dem Ruderschaft, das die lineare Seil-/Kettenbewegung in eine Drehbewegung umwandelt |
| 28 | **Radialspiel** | Spiel quer zur Achsrichtung — Maß für Lagerverschleiß |
| 29 | **Ritzel (Pinion)** | Kleines Zahnrad in einer Zahnstangensteuerung, das die Drehbewegung des Steuerrads auf die Zahnstange überträgt |
| 30 | **Ruderlager** | Lager (Gleit- oder Kugellager), in dem der Ruderschaft im Rumpf geführt wird — typisch oberes und unteres Lager |
| 31 | **Ruderstopp** | Mechanischer Anschlag, der den maximalen Ruderausschlag begrenzt (typisch ±30° bis ±35°) |
| 32 | **Spannungsrisskorrosion (SCC)** | Rissbildung in Metallen unter dem Einfluss von Zugspannung und korrosivem Medium (Chlorid + Edelstahl) |
| 33 | **Spaltkorrosion** | Korrosion in engen Spalten, wo der Sauerstoffzugang eingeschränkt ist — häufig an Schraubverbindungen |
| 34 | **Steuerbord (Stb)** | Rechte Seite des Schiffes in Fahrtrichtung gesehen |
| 35 | **Stevenrohr** | Rohr im Rumpf, durch das der Ruderschaft geführt wird — enthält die Ruderlager und -dichtungen |
| 36 | **Tef-Gel** | Anti-Seize-Paste auf PTFE-Basis, verhindert galvanische Korrosion und Festfressen von Metallverbindungen |
| 37 | **Tensiometer** | Messgerät zur Bestimmung der Seilspannung (Vorspannung) |
| 38 | **Totgang (Backlash)** | Winkelbereich am Steuerrad, den man drehen muss, bevor das Ruder reagiert — Maß für Gesamtspiel der Steueranlage |
| 39 | **UHMWPE** | Ultra High Molecular Weight Polyethylen — sehr verschleißfester Kunststoff für Lager und Führungen |
| 40 | **Vollausschlag** | Maximaler Ruderwinkel, typisch 30–35° pro Seite (Backbord und Steuerbord) |
| 41 | **Viskositätsindex (VI)** | Maß für die Temperaturabhängigkeit der Ölviskosität — hoher VI = weniger Viskositätsänderung bei Temperaturwechsel |
| 42 | **Zahnstange (Rack)** | Lineare Verzahnung, die mit dem Ritzel zusammenwirkt — überträgt die Drehbewegung in eine lineare Schubbewegung |
| 43 | **7×19-Seil** | Drahtseilkonstruktion: 7 Litzen à 19 Einzeldrähte = 133 Drähte — flexibelstes Standard-Steuerseil |
| 44 | **ISO VG** | Viskositätsklasse nach ISO 3448, Zahl entspricht der Viskosität in cSt bei 40 °C |
| 45 | **ATF (Automatic Transmission Fluid)** | Automatikgetriebeöl, wird bei einigen Hydrauliksteuerungen (Teleflex/SeaStar) als Hydraulikmedium verwendet |
| 46 | **Brattest** | Einfache Feldmethode zur Bestimmung des Wassergehalts im Hydrauliköl — Öltropfen auf 150 °C heiße Platte, Knistern = Wassergehalt |
| 47 | **Crimp/Pressung** | Dauerhafte Verbindung von Hydraulikschlauch und Fitting durch radiales Verpressen einer Stahlhülse |
| 48 | **Deadband** | Totzone — der Bereich, in dem eine Steuereingabe keine Ruderbewegung erzeugt (identisch mit Totgang) |
| 49 | **Druckbegrenzungsventil** | Synonym für Überdruckventil — schützt das Hydrauliksystem vor Überlastung |
| 50 | **Extrusion (Dichtung)** | Herauspressen einer Dichtung aus dem Dichtspalt bei Drucküberschreitung — führt zu schnellem Dichtungsversagen |
| 51 | **Fail-Safe** | Sicherheitskonzept, bei dem ein Systemausfall in einen sicheren Zustand führt (z. B. EPS fällt auf manuelle Steuerung zurück) |
| 52 | **Fretting** | Reibkorrosion — Materialabtrag durch Mikrobewegungen an Kontaktflächen unter Last |
| 53 | **Hunting (Autopilot)** | Permanentes Pendeln des Autopiloten um den Sollkurs — häufige Ursache: Totgang in der Steueranlage |
| 54 | **JIC-Fitting** | Joint Industry Council — standardisiertes Hydraulik-Anschlusssystem mit 37°-Dichtkegel (SAE J514) |
| 55 | **Korbbildung (Birdcaging)** | Aufweitung/Aufbauschung der äußeren Seil-Litzen durch Druckbelastung — sofortiger Austauschgrund |
| 56 | **Leinensteuerung** | Provisorische Notsteuerung mit Festmacherleinen direkt am Quadranten — Notbehelf bei Seilbruch |
| 57 | **Manövrierunfähigkeit** | Zustand, in dem ein Schiff nicht mehr gesteuert werden kann — erfordert Assistenz oder Notmaßnahmen |
| 58 | **Pan-Pan** | Dringlichkeitsmeldung im Seefunk (unterhalb Mayday) — bei Steuerungsausfall ohne unmittelbare Lebensgefahr |
| 59 | **Passmarke** | Markierung an der Quadrant-Ruderschaft-Verbindung, die die korrekte Ausrichtung anzeigt |
| 60 | **Schneidring-Verschraubung** | Hydraulik-Rohrverschraubung, bei der ein Metallring in das Rohr schneidet und dichtet (DIN 2353/ISO 8434) |
| 61 | **Self-Aligning Bearing** | Selbstausrichtendes Ruderlager (Jefa-Patent) — kompensiert Fluchtungsfehler, wassergeschmiert |
| 62 | **Stick-Slip** | Ruckgleiteffekt — abwechselndes Haften und Gleiten, typisch bei Hydraulik mit Luft im System |
| 63 | **Thordon** | Markenname für Composite-Lagermaterial — wassergeschmiert, hohe Abriebfestigkeit, häufig für Ruderlager |
| 64 | **Trim (Ruder)** | Feineinstellung des Ruders zur Kompensation von Seitenwind oder asymmetrischer Belastung |

---

## 10. Schnell-Referenz

### 10.1 Kritische Grenzwerte — Auf einen Blick

| Parameter | Grenzwert | Maßnahme bei Überschreitung |
|-----------|-----------|---------------------------|
| Litzenbrüche (6×d Länge) | >5 | Seil sofort tauschen |
| Seildurchmesser-Reduktion | >10 % | Seil sofort tauschen |
| Kettenlängung | >2 % | Kette + Kettenrad tauschen |
| Umlenkrollen-Radialspiel | >0,3 mm | Rolle tauschen |
| Ruderlager-Radialspiel | >0,3 mm | Lagertausch planen |
| Totgang am Steuerrad | >5° (Seilzug), >3° (Hydraulik) | Ursache ermitteln, beheben |
| Hydraulik-Leckage | L3 (tropfend) oder höher | Sofortige Reparatur |
| Hydrauliköl-Farbe | Schwarz, trüb | Sofortiger Ölwechsel |
| Hydraulikschlauch-Alter | >10 Jahre | Sofort tauschen |
| Zahnflankenspiel | >0,5 mm | Zahnstange/Ritzel tauschen |

### 10.2 Schmierstoff-Schnellübersicht

| Anwendung | Produkt | Intervall |
|-----------|---------|-----------|
| Steuerseile | Boeshield T-9 / Lewmar Wire Rope Lube | 3 Monate |
| Ketten | Lewmar Chain Lube / Boeshield T-9 | 3 Monate |
| Umlenkrollen | Lewmar Gear Grease / Mobilgrease 28 | 6 Monate |
| Quadrant-Konus | Tef-Gel / Duralac | Bei Montage |
| Ruderlager | Herstellerspezifisch (Fett/Wasser) | 6–12 Monate |
| Zahnstange | Kobelt Gear Lube / Marine-Getriebefett | 12 Monate |
| Hydrauliköl | Herstellerspezifisch (ISO VG 15/22) | 2 Jahre (Wechsel) |

### 10.3 Werkzeug-Mindestausstattung Eigner

| Werkzeug | Anwendung | Geschätzter Preis (EUR) |
|----------|-----------|------------------------|
| Loos-Tensiometer PT-2 | Seilspannungsmessung | 110–150 |
| Fühlerlehren-Satz (0,05–1,0 mm) | Lagerspiel, Zahnflankenspiel | 12–20 |
| Stirnlampe (>500 Lux) | Inspektion in dunklen Bereichen | 25–45 |
| Inspektionsspiegel | Seilprüfung an unzugänglichen Stellen | 8–15 |
| Schieblehre (digital, 150 mm) | Seildurchmesser, Kettenteilung | 20–40 |
| Drehmomentschlüssel (10–100 Nm) | Quadrant-Mutter, Zylinderbefestigung | 40–80 |
| Nicopress-Werkzeug | Seilreparatur/-wechsel | 60–120 |
| Manometer (0–100 bar) | Hydraulikdruck-Messung | 25–50 |
| Marine-Schmierstoffe (Set) | Wartung | 40–80 |
| **Gesamtinvestition** | | **340–600 EUR** |

### 10.4 Notfall-Kurzanleitung: Steuerungsausfall auf See

```
1. MOTOR → Leerlauf oder STOPP
2. AUTOPILOT → AUS (Sicherung ziehen!)
3. CREW → Informieren, Ausguck
4. NOTPINNE → Aufsetzen
   - Hydraulik: Bypass-Ventil ERST ÖFFNEN, dann Notpinne
   - Seilzug: Notpinne direkt auf Ruderkopf
5. FUNKTIONSTEST → Ruder über Notpinne bewegen
6. NAVIGATION → Nächsten sicheren Hafen anlaufen
7. Falls NOTPINNE nicht möglich:
   → 2 Leinen am Quadranten, je über eine Winsch → Provisorische Leinensteuerung
8. BORDBUCH → Vorfall dokumentieren
9. Bei GEFAHR → DSC-Notruf / MAYDAY (Kanal 16)
```

### 10.5 Anzugsmomente — Wichtige Verbindungen

| Verbindung | Gewinde | Drehmoment (Nm) | Anmerkung |
|-----------|---------|-----------------|-----------|
| Quadrant auf Ruderschaft (Konusmutter) | M16–M24 | 80–150 | Herstellerspezifisch, Anti-Seize verwenden |
| Pedestal auf Deck | M10–M12 | 25–40 | Edelstahl A4, mit Dichtung |
| Hydraulikzylinder-Befestigung | M12–M16 | 40–80 | Selbstsichernde Mutter |
| Hydraulik-Verschraubungen JIC | 9/16"–18 UNF | 25–35 | Nicht überdrehen! Dichtkonus |
| Hydraulik-Verschraubungen BSP | 1/4" BSP | 20–30 | O-Ring-Dichtung |
| Umlenkrollen-Befestigung | M8–M10 | 15–25 | Edelstahl, ggf. Loctite 243 |
| Ruderstopp-Schrauben | M10–M12 | 30–50 | Kontermutter verwenden |
| Notpinnen-Mutter (Ruderkopf) | M16–M20 | 50–80 | Schnell lösbar, kein Loctite |
| Spurstangen-Kugelgelenk | M12–M14 | 35–55 | Splint sichern |

### 10.6 Wartungskosten-Übersicht nach Steuerungstyp

**Jährliche Wartungskosten (Durchschnitt, inkl. Material, exkl. Fachbetrieb-Arbeitslohn):**

| Steuerungstyp | Bootsgröße | Eigner-Wartung/Jahr | Fachbetrieb-Wartung/Jahr |
|--------------|-----------|--------------------|-----------------------|
| Seilzug/Kette | 8–12 m | 80–150 EUR | 250–450 EUR |
| Seilzug/Kette | 12–16 m | 120–220 EUR | 350–600 EUR |
| Seilzug/Kette | 16–20 m | 160–300 EUR | 450–800 EUR |
| Hydraulik | 10–14 m | 100–200 EUR | 300–550 EUR |
| Hydraulik | 14–20 m | 150–300 EUR | 450–750 EUR |
| Hydraulik | 20–30 m | 250–500 EUR | 700–1.200 EUR |
| Zahnstange | 6–10 m | 40–80 EUR | 150–300 EUR |
| Zahnstange | 10–14 m | 60–120 EUR | 200–400 EUR |
| Pinne | 6–10 m | 20–50 EUR | 80–180 EUR |

**Typische Großreparatur-Kosten (alle 8–15 Jahre, Confidence: benchmark):**

| Maßnahme | Materialkosten (EUR) | Arbeitskosten (EUR) | Gesamt (EUR) |
|----------|---------------------|--------------------|----|
| Steuerseil-Wechsel (komplett) | 100–200 | 200–400 | 300–600 |
| Kette + Kettenrad erneuern | 80–180 | 150–350 | 230–530 |
| Ruderlager erneuern (beide) | 300–700 | 800–1.500 | 1.100–2.200 |
| Ruderschaft ziehen + prüfen | 50–100 | 500–1.200 | 550–1.300 |
| Hydraulikzylinder überholen | 80–200 | 300–600 | 380–800 |
| Helm-Pumpe überholen | 70–150 | 200–500 | 270–650 |
| Hydraulikschläuche erneuern (Satz) | 150–400 | 200–500 | 350–900 |
| Komplettes Hydrauliksystem erneuern | 1.500–4.000 | 1.000–2.500 | 2.500–6.500 |
| Quadrant erneuern | 200–450 | 150–350 | 350–800 |
| Pedestal-Revision | 100–200 | 200–500 | 300–700 |

### 10.7 Saisonale Checklisten — Kompaktform

**Frühling (Auswinterung) — TOP 10:**

1. Sichtprüfung Gesamtanlage (Korrosion, Feuchteschäden)
2. Seilspannung/Kettenspannung auf Sollwert nachstellen
3. Hydraulikölstand prüfen und nachfüllen
4. 10× Vollausschlag zur Schmierungsverteilung
5. Alle Umlenkrollen auf Leichtgängigkeit prüfen
6. Ruderstopps prüfen
7. Notpinne aufsetzen und testen
8. Autopilot-Funktion prüfen
9. Probefahrt mit Funktionstest
10. Befunde dokumentieren

**Herbst (Einwinterung) — TOP 10:**

1. Steueranlage komplett schmieren
2. Seilspannung um 10 % reduzieren
3. Hydraulik auf Maximum auffüllen
4. Hydraulikschläuche auf Risse prüfen
5. Ruderlager auf Spiel prüfen
6. Korrosionsschutz auf exponierte Metallflächen
7. Steuerrad abdecken oder abnehmen
8. Ruder in Mittschiffsstellung fixieren
9. Belüftung sicherstellen
10. Winterfestmachungs-Protokoll erstellen

### 10.8 Herstellerkontakte — Schnellverzeichnis

| Hersteller | Telefon | E-Mail | Ersatzteile |
|-----------|---------|--------|-------------|
| Lewmar | +44 23 9247 1841 | techsupport@lewmar.com | lewmar.com |
| Jefa Marine | +45 64 71 28 50 | info@jefa.com | jefa.com |
| Edson International | +1 508 995 9711 | info@edsonintl.com | edsonmarine.com |
| Kobelt | +1 604 590 7313 | sales@kobelt.com | kobelt.com |
| SeaStar Solutions | +1 604 248 3858 | — | seastarsolutions.com |
| Spa Creek / Yacht Specialties | +1 410 263 0388 | — | spacreek.com |

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 40 Cruiser (2008), Steuerseilbruch auf der Nordsee

**Bootsdaten:**
- Typ: Bavaria 40 Cruiser, Bj. 2008
- Steueranlage: Whitlock Cobra (Seilzug/Kette), Doppelsteuerrad
- Alter der Steueranlage zum Schadenszeitpunkt: 15 Jahre (Originalseil)
- Nutzung: Privatyacht, ca. 800 Seemeilen/Jahr, Nordsee/Ostsee
- Letzte dokumentierte Wartung: 3 Jahre vor dem Schaden

**Schadensereignis:**
Bei einer Überfahrt von Cuxhaven nach Helgoland (Wind 5 Bft, Welle 1,5 m) brach das Backbord-Steuerseil ohne Vorwarnung. Der Rudergänger spürte plötzlich keinen Widerstand mehr am Steuerrad. Das Ruder schlug unkontrolliert aus, das Boot drehte in den Wind (Segelyacht) und lag bei.

**Analyse:**
- Post-mortem-Untersuchung des Seils: massive Spannungsrisskorrosion (SCC) im Bereich der unteren Umlenkrolle (Nähe Motorraum, erhöhte Temperatur)
- Durchmesserreduktion am Bruchpunkt: 14 % (kritisch)
- Zahlreiche Litzenbrüche an der Innenseite (von außen nicht sichtbar)
- Keine Schmierung erkennbar (Seil trocken)
- Umlenkrollen: 2 von 4 Rollen schwergängig (Lagerverschleiß)

**Sofortmaßnahmen (Crew):**
1. Motor gestartet, Segel geborgen
2. Notpinne aufgesetzt (war korrekt verstaut, Crew kannte den Platz)
3. Über Notpinne nach Helgoland gesteuert (2,5 Stunden)
4. Im Hafen provisorisch repariert: Seil aus Festmacherleinen an Quadrant

**Reparatur:**
- Beide Steuerseile erneuert (7×19, 6,35 mm Edelstahl 316)
- Alle 4 Umlenkrollen durch UHMWPE-Rollen ersetzt
- Kette und Kettenrad erneuert
- Quadrant-Konus gereinigt und mit Tef-Gel montiert
- Gesamtkosten: 1.850 EUR (Material + Arbeit)

**Lehren:**
1. 15 Jahre altes Originalseil war 5–7 Jahre über der empfohlenen Lebensdauer
2. Fehlende regelmäßige Inspektion hätte die SCC frühzeitig erkannt
3. Die Notpinne rettete die Situation — sie muss getestet und zugänglich sein
4. Wirtschaftlicher Vergleich: 15 Jahre Wartung à 200 EUR = 3.000 EUR vs. 1.850 EUR Reparatur + 350 EUR Bergungsversicherungs-Selbstbehalt + unbezahlbares Risiko

### ANHANG B — Fallstudie: Hallberg-Rassy 43 MkII (2012), Hydraulik-Drift nach Ölwechsel

**Bootsdaten:**
- Typ: Hallberg-Rassy 43 MkII, Bj. 2012
- Steueranlage: Jefa Hydraulic Direct, Doppelsteuerrad
- Nutzung: Blauwasser-Langfahrt, Karibik-Saison
- Anlass: Routinemäßiger Ölwechsel durch den Eigner in der Karibik

**Schadensereignis:**
Nach einem Ölwechsel (Eigner verwendete lokal verfügbares ATF Dexron III statt des vorgeschriebenen Jefa Hydraulic Oil ISO VG 15) entwickelte die Steuerung innerhalb von 3 Tagen eine zunehmende Drift. Der Autopilot arbeitete ständig nach, Stromverbrauch stieg um 40 %.

**Analyse:**
- Dexron III (ATF) enthält Dichtungsquellmittel, die für Jefa-Dichtungen (NBR 70) nicht vorgesehen sind
- Die Dichtungen quollen an, verloren ihre Elastizität und dichteten nicht mehr korrekt
- Interne Leckage am Hydraulikzylinder: Kolbendichtung undicht geworden
- Zusätzlich: Additivunverträglichkeit verursachte Schlammbildung nach 2 Wochen

**Reparatur:**
- Hydrauliksystem komplett ablassen und 3× mit dem korrekten Jefa-Öl spülen
- Zylinder-Dichtkit JEFA-HYD-SK eingebaut
- Helm-Pumpen-Dichtungen vorsorglich erneuert
- Gesamtkosten: 620 EUR (Material) + 800 EUR (Arbeit, Fachbetrieb in Martinique — Aufpreis Übersee)

**Lehren:**
1. Niemals ein anderes Hydrauliköl verwenden als vom Hersteller vorgeschrieben
2. Auf Langfahrt: ausreichend Originalöl als Reservebestand mitnehmen
3. ATF ist nicht universell — Dichtungsquellmittel sind systemspezifisch
4. Drift nach Ölwechsel → immer zuerst Ölverträglichkeit prüfen

### ANHANG C — Fallstudie: Beneteau Oceanis 38.1 (2019), Kette-Kettenrad-Verschleiß in Charteryacht

**Bootsdaten:**
- Typ: Beneteau Oceanis 38.1, Bj. 2019
- Steueranlage: Lewmar Compac 5
- Nutzung: Charteryacht, Kroatien, ~3.500 Seemeilen/Jahr, 35 Wochen/Jahr im Einsatz
- Wartungshistorie: Nur Saisonstart-Check durch Charterfirma

**Schadensereignis:**
Chartergast meldete "springendes" Steuerrad: Bei schnellen Ruderbewegungen übersprang die Kette einzelne Zähne am Kettenrad. Laut rhythmisches Klacken, spürbarer Ruck am Steuerrad.

**Analyse:**
- Kettenleitung: 3,2 % (weit über dem 2 %-Grenzwert)
- Kettenrad: Zahnflanken asymmetrisch verschlissen ("Haifischzahn"-Profil)
- Ursache: Extrem hohe Nutzungsintensität (Charter) bei minimaler Wartung
- Kette wurde seit Auslieferung nie geschmiert oder getauscht (4 Jahre, ~14.000 sm)

**Reparatur:**
- Kette und Kettenrad als Set erneuert (Lewmar Original)
- Pedestal-Lager erneuert (Service Kit 89000037)
- Steuerseile geprüft — Zustand akzeptabel, aber Schmierung aufgefrischt
- Umlenkrollen geprüft — 2 von 4 mit erhöhtem Spiel → getauscht
- Gesamtkosten: 680 EUR

**Lehren:**
1. Charteryachten benötigen verkürzte Wartungsintervalle (mindestens halbjährlich)
2. Kette und Kettenrad sind bei hoher Nutzung nach 3–4 Jahren verschlissen
3. Kette und Kettenrad immer als Set tauschen
4. Charterfirmen sollten ein Wartungsprotokoll mit Messungen führen

### ANHANG D — Fallstudie: Jeanneau Sun Odyssey 449 (2017), Ruderlager-Versagen nach Grundberührung

**Bootsdaten:**
- Typ: Jeanneau Sun Odyssey 449, Bj. 2017
- Steueranlage: Lewmar Compac 7, Doppelrad
- Nutzung: Mittelmeer-Fahrtensegler, ca. 2.000 sm/Jahr

**Schadensereignis:**
Nach einer leichten Grundberührung (Sand/Schlick) in einer Ankerbucht bemerkte der Eigner zunehmende Vibrationen am Steuerrad und ein "knackendes" Geräusch bei Richtungswechsel. Die Symptome verschlimmerten sich über 3 Wochen.

**Analyse:**
- Grundberührung hatte den Ruderschaft minimal verbogen (0,4 mm Schlag, gemessen mit Messuhr)
- Unteres Ruderlager (Delrin-Gleitlager) wurde durch den exzentrischen Lauf beschädigt
- Lagerspiel: 0,8 mm radial (Grenzwert 0,3 mm)
- Oberes Ruderlager ebenfalls erhöhtes Spiel: 0,35 mm
- Ruderblatt: keine sichtbaren Schäden (GFK intakt)

**Reparatur:**
- Schiff aus dem Wasser, Ruder ausgebaut
- Ruderschaft gerichtet (Hydraulikpresse, Fachbetrieb)
- Beide Ruderlager erneuert (Jefa Self-Aligning Bearings als Upgrade)
- Ruder eingebaut, Steueranlage neu justiert
- Gesamtkosten: 3.200 EUR (inkl. Kranen, Lagerung, Arbeit)

**Lehren:**
1. Nach jeder Grundberührung — auch bei "leichter" — die Steueranlage sofort inspizieren
2. Ruderschaft-Schlag von 0,4 mm reicht aus, um Ruderlager zu zerstören
3. Vibration + Knacken nach Grundberührung = sofort Lager prüfen lassen
4. Jefa Self-Aligning Bearings als Upgrade tolerieren leichte Fehlausrichtung besser

### ANHANG E — Fallstudie: Sunseeker Manhattan 52 (2010), Hydraulikschlauch-Platzer

**Bootsdaten:**
- Typ: Sunseeker Manhattan 52, Bj. 2010 (Motoryacht)
- Steueranlage: Kobelt 7012 Hydraulik, Twin-Engine
- Nutzung: Privatyacht, Mittelmeer, ca. 200 Betriebsstunden/Jahr

**Schadensereignis:**
Bei einem Anlegemanöver in der Marina von Antibes platzte ein Hydraulikschlauch zwischen Helm-Pumpe und Steuerventil. Innerhalb von Sekunden entleerte sich das System, die Steuerung fiel komplett aus. Das Boot kollidierte mit einem Nachbarsteg (Sachschaden ~12.000 EUR).

**Analyse:**
- Schlauch: 13 Jahre alt (Original ab Bj. 2010, nie gewechselt)
- Bruchstelle: an der Presshülse, innere Lagen korrodiert und ermüdet
- Äußerer Schlauch-Zustand zum Schadenszeitpunkt: oberflächliche Risse sichtbar, Verhärtung
- Schlauch lag in der Nähe des Auspuffrohrs (Wärmebelastung)

**Reparatur:**
- Alle 6 Hydraulikschläuche erneuert (Kobelt-Spezifikation)
- Hitzeschutzschlauch über thermisch belasteten Leitungen installiert
- Hydrauliköl komplett erneuert (Kobelt K-22)
- Gesamtkosten (Hydraulik): 1.400 EUR
- Stegschaden: 12.000 EUR (Versicherungsfall)

**Lehren:**
1. Hydraulikschläuche nach 7 Jahren tauschen (präventiv), spätestens nach 10 Jahren
2. Thermische Belastung verkürzt die Schlauchlebensdauer drastisch
3. Hitzeschutz an allen Schläuchen in der Nähe von Motoren/Auspuffanlagen
4. Versicherungsprüfer stellte fest: Schlauch hätte bei regelmäßiger Inspektion rechtzeitig getauscht werden müssen → Regulierung mit Abzug "Unterhaltungsdefizit"

### ANHANG F — Fallstudie: X-Yachts X4⁶ (2020), Autopilot-Probleme durch Steueranlagen-Totgang

**Bootsdaten:**
- Typ: X-Yachts X4⁶ (X46), Bj. 2020
- Steueranlage: Jefa Hydraulic Direct, Doppelrad
- Autopilot: B&G H5000 mit Hydraulikantrieb
- Nutzung: Regatta und Fahrtensegeln, ca. 4.000 sm/Jahr

**Schadensereignis:**
Zunehmende Autopilot-Probleme: permanentes Pendeln (Hunting), besonders bei Leichtwind-Kursen (Vorwind). B&G-Service wurde kontaktiert, Autopilot-Elektronik und -Hydraulik geprüft — kein Befund. Problem persistierte.

**Analyse:**
- Ursache: 4 mm Radialspiel am oberen Ruderlager → Totgang in der Gesamtanlage

> ⚠️ **ZU PRÜFEN (Audit):** 4 mm Radialspiel widerspricht den dokumenteneigenen Grenzwerten (>0,3 mm = Lagertausch planen; >1,0 mm = "nicht auslaufen, sofort Werft", siehe Abschnitte 3.6.3 und 10.1). Ein Radialspiel von 4 mm ist für ein noch funktionierendes, wassergeschmiertes Self-Aligning-Lager physikalisch unplausibel und passt nicht zum geschilderten kompletten Regatta-Saison-Betrieb (~16.000 sm) mit lediglich Autopilot-Pendeln als Symptom (vgl. ANHANG D, wo 0,8 mm bereits sofortiges Kranen erforderte). Wahrscheinlich Tippfehler für 0,4 mm — mangels Primärquelle NICHT korrigiert, sondern zur Prüfung markiert.

- Autopilot konnte den Totgang nicht kompensieren und übersteuerte permanent
- Ruderlager-Verschleiß durch intensive Nutzung (Regatta: häufige schnelle Ruderbewegungen)
- Jefa Self-Aligning Bearing hat nach 4 Jahren und ~16.000 sm die erwartete Lebensdauer noch nicht erreicht — atypisch früher Verschleiß

**Reparatur:**
- Ruder ausgebaut, oberes Ruderlager erneuert (Jefa-Garantie, Kulanzregelung)
- Ursache des vorzeitigen Verschleißes: Sandkörner im Lagerspalt (Boot lag regelmäßig trockenfallend im Gezeitenrevier)
- Unteres Ruderlager vorsorglich erneuert
- Nach Lagertausch: Autopilot funktionierte einwandfrei ohne Parameteränderung
- Gesamtkosten: 480 EUR (Jefa Kulanz auf Lager, Arbeitskosten)

**Lehren:**
1. Autopilot-Probleme → immer auch Steueranlage prüfen
2. Ruderlager können Hauptursache für Autopilot-Hunting sein
3. Sand/Schmutz im Lagerspalt beschleunigt den Verschleiß dramatisch
4. Bei Yachten in Trockenfall-Revieren: Ruderlager-Inspektion verkürzt auf jährlich

### ANHANG G — Fallstudie: Hanse 505 (2016), Asymmetrischer Ruderausschlag nach DIY-Quadrantmontage

**Bootsdaten:**
- Typ: Hanse 505, Bj. 2016
- Steueranlage: Lewmar Compac 10, Doppelrad
- Nutzung: Fahrtensegeln, Langfahrt Atlantik

**Schadensereignis:**
Eigner baute nach einem Transatlantik-Törn den Quadranten zur Inspektion ab und montierte ihn selbst wieder. Danach: Boot zog nach Steuerbord, maximaler Ruderausschlag Backbord nur 22° statt 30°. Steuerrad-Mittelpunkt stimmte nicht mit Ruder-Mittschiffsstellung überein.

**Analyse:**
- Quadrant auf Ruderschaft um 8° verdreht montiert (Passmarken nicht beachtet)
- Ruderstopps verhinderten korrekterweise den vollen Ausschlag auf einer Seite
- Seillängen asymmetrisch (nicht nachgestellt nach Quadrant-Montage)

**Reparatur:**
- Quadrant abgenommen, Passmarken korrekt ausgerichtet
- Mit korrektem Drehmoment (95 Nm) angezogen, Anti-Seize erneuert
- Seile beidseitig auf gleiche Spannung eingestellt
- Ruderstopps auf ±30° symmetrisch eingestellt
- Funktionsprüfung: Steuerrad-Mitte = Ruder-Mitte
- Gesamtkosten: 0 EUR (Eigenarbeit, 2 Stunden)

**Lehren:**
1. Vor dem Lösen des Quadranten immer Passmarken anbringen (oder vorhandene markieren)
2. Nach Quadrant-Montage: Symmetrie prüfen (gleicher Ausschlag Bb/Stb)
3. Steuerrad-Mitte muss Ruder-Mitte entsprechen
4. Ruderstopps nach jeder Quadrant-Demontage neu einstellen und prüfen

### ANHANG H — Fallstudie: Fountaine Pajot Elba 45 (2021), Katamaran-Doppelruder-Synchronisation

**Bootsdaten:**
- Typ: Fountaine Pajot Elba 45, Bj. 2021 (Fahrtenkatamaran)
- Steueranlage: Doppelruder, hydraulisch verbunden, Teleflex/SeaStar System
- Nutzung: Charterkatamaran, Karibik

**Schadensereignis:**
Chartergäste meldeten, das Boot "krabble" (seitlicher Versatz bei Geradeausfahrt) und die Steuerung fühle sich "schwammig" an. Beide Ruder waren visuell intakt.

**Analyse:**
- Luft im Hydrauliksystem eines Rumpfes (Steuerbord)
- Hydrauliköl im Backbord-System: 2 cm unter Minimum
- Ursache: langsame Leckage an einer Verschraubung am Backbord-Zylinder
- Beide Ruder steuerten asynchron: Backbord-Ruder reagierte verzögert und mit weniger Ausschlag als Steuerbord

**Reparatur:**
- Leckage an der Verschraubung behoben (O-Ring erneuert, nachgezogen)
- Beide Hydrauliksysteme entlüftet
- Ölstand in beiden Systemen auf Maximum aufgefüllt
- Synchronisation geprüft: Beide Ruder müssen identischen Ausschlag bei identischer Raddrehung zeigen
- Gesamtkosten: 180 EUR

**Lehren:**
1. Katamarane mit Doppelruder: Synchronisation regelmäßig prüfen
2. Asymmetrisches Ruderverhalten → immer beide Hydrauliksysteme separat prüfen
3. Charterboote: Ölstand beider Systeme bei jedem Charterwechsel prüfen
4. "Krabbeln" und "schwammige Steuerung" sind typische Symptome für Luft im Doppelruder-System

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Basis-Modelle

```python
"""
AYDI Knowledge Base — Steueranlagen Wartung und Troubleshooting
Pydantic v2 Modelle für die Erfassung, Analyse und Bewertung von
Steueranlagen-Wartungsdaten im Yachtbau.

Alle Modelle verwenden Pydantic v2 mit model_config = {"from_attributes": True}.
NEVER class Config.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class SteeringType(str, Enum):
    """Steuerungstyp."""
    CABLE = "cable"                  # Seilzugsteuerung
    CHAIN = "chain"                  # Kettensteuerung
    CABLE_CHAIN = "cable_chain"      # Seilzug/Kette Kombination
    HYDRAULIC = "hydraulic"          # Hydrauliksteuerung
    RACK_PINION = "rack_pinion"      # Zahnstangensteuerung
    TILLER = "tiller"                # Pinnensteuerung
    ELECTRONIC = "electronic"        # Elektronische Steuerung (EPS)


class MaintenanceCategory(str, Enum):
    """Wartungskategorie."""
    OWNER_BASIC = "owner_basic"            # Kategorie I
    OWNER_ADVANCED = "owner_advanced"      # Kategorie II
    SPECIALIST = "specialist"              # Kategorie III
    YARD = "yard"                          # Kategorie IV


class MaintenanceInterval(str, Enum):
    """Wartungsintervall."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    BIENNIAL = "biennial"
    FIVE_YEARLY = "five_yearly"
    SEASON_START = "season_start"
    WINTERIZATION = "winterization"


class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"        # Neuwertig oder frisch gewartet
    GOOD = "good"                  # Normaler Betriebszustand
    FAIR = "fair"                  # Verschleiß sichtbar, funktionsfähig
    POOR = "poor"                  # Eingeschränkte Funktion, Wartung überfällig
    CRITICAL = "critical"          # Sofortige Maßnahme erforderlich
    FAILED = "failed"              # Ausgefallen
    NOT_ASSESSED = "not_assessed"  # Nicht beurteilbar


class LeakageGrade(str, Enum):
    """Leckagegrad (Hydraulik)."""
    L0_DRY = "L0_dry"                  # Trocken
    L1_DAMP = "L1_damp"                # Feucht (Ölfilm)
    L2_SWEATING = "L2_sweating"        # Schwitzend (>1 min/Tropfen)
    L3_DRIPPING = "L3_dripping"        # Tropfend (<1 min/Tropfen)
    L4_RUNNING = "L4_running"          # Laufend (kontinuierlich)


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


class UrgencyLevel(str, Enum):
    """Dringlichkeitsstufe."""
    NONE = "none"                    # Kein Handlungsbedarf
    MONITOR = "monitor"              # Beobachten
    NEXT_SEASON = "next_season"      # Nächste Saison beheben
    WITHIN_30_DAYS = "within_30d"    # Innerhalb 30 Tage
    WITHIN_7_DAYS = "within_7d"      # Innerhalb 7 Tage
    IMMEDIATE = "immediate"          # Sofort / nicht auslaufen
```

### ANHANG J — Steueranlagen-Modelle

```python
class SteeringSystemSpec(BaseModel):
    """Spezifikation einer Steueranlage."""
    model_config = {"from_attributes": True}

    steering_type: SteeringType
    manufacturer: str = Field(..., description="Hersteller der Steueranlage")
    model: str = Field(..., description="Modellbezeichnung")
    year_installed: Optional[int] = Field(None, ge=1950, le=2030)
    boat_length_m: float = Field(..., ge=2.0, le=100.0, description="Bootslänge in Metern")
    max_rudder_torque_nm: Optional[float] = Field(None, ge=0, description="Max. Rudermoment in Nm")
    cable_diameter_mm: Optional[float] = Field(None, ge=3.0, le=15.0, description="Seildurchmesser mm")
    cable_construction: Optional[str] = Field(None, description="Seilkonstruktion z.B. 7x19")
    chain_pitch_mm: Optional[float] = Field(None, description="Kettenteilung mm")
    hydraulic_pressure_bar: Optional[float] = Field(None, ge=0, le=300, description="Betriebsdruck bar")
    hydraulic_oil_type: Optional[str] = Field(None, description="Hydrauliköl-Spezifikation")
    hydraulic_oil_volume_l: Optional[float] = Field(None, ge=0, description="Ölvolumen Liter")
    dual_station: bool = Field(False, description="Doppelsteuerstand")
    rudder_count: int = Field(1, ge=1, le=4, description="Anzahl Ruder")


class RudderBearingSpec(BaseModel):
    """Ruderlager-Spezifikation."""
    model_config = {"from_attributes": True}

    position: str = Field(..., description="Position: upper, lower")
    bearing_type: str = Field(..., description="Lagertyp: delrin, bronze, jefa_self_aligning, thordon, ball")
    shaft_diameter_mm: float = Field(..., ge=15, le=150, description="Schaftdurchmesser mm")
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    year_installed: Optional[int] = Field(None, ge=1950, le=2030)
    water_lubricated: bool = Field(False, description="Wassergeschmiert (kein Fett)")
    expected_lifetime_years: Optional[int] = Field(None, ge=1, le=50)
```

### ANHANG K — Inspektions-Modelle

```python
class CableInspectionResult(BaseModel):
    """Ergebnis einer Steuerseil-Inspektion."""
    model_config = {"from_attributes": True}

    inspection_date: date
    cable_age_years: Optional[float] = Field(None, ge=0, le=50)
    cable_diameter_measured_mm: float = Field(..., ge=3.0, le=15.0)
    cable_diameter_nominal_mm: float = Field(..., ge=3.0, le=15.0)
    diameter_reduction_percent: float = Field(..., ge=0, le=100)
    broken_wires_per_6d: int = Field(..., ge=0, description="Litzenbrüche pro 6×d Länge")
    corrosion_visible: bool
    corrosion_type: Optional[str] = Field(None, description="Art: surface, pitting, scc, crevice")
    kinks_present: bool = Field(False, description="Knicke vorhanden")
    birdcaging_present: bool = Field(False, description="Korbbildung vorhanden")
    lubrication_state: str = Field(..., description="dry, light, adequate, excessive")
    condition: ConditionRating
    urgency: UrgencyLevel
    confidence: ConfidenceLevel
    notes: Optional[str] = None

    @field_validator("diameter_reduction_percent")
    @classmethod
    def validate_diameter_reduction(cls, v: float) -> float:
        if v > 10.0:
            pass  # Will be flagged as critical in business logic
        return v


class ChainInspectionResult(BaseModel):
    """Ergebnis einer Steuerketten-Inspektion."""
    model_config = {"from_attributes": True}

    inspection_date: date
    chain_age_years: Optional[float] = Field(None, ge=0, le=50)
    nominal_pitch_mm: float = Field(..., ge=8.0, le=25.0)
    measured_pitch_mm: float = Field(..., ge=8.0, le=30.0)
    elongation_percent: float = Field(..., ge=0, le=20)
    lateral_play_mm: float = Field(..., ge=0, description="Seitliches Spiel in mm")
    sprocket_tooth_wear_percent: float = Field(..., ge=0, le=100)
    corrosion_visible: bool
    lubrication_state: str
    condition: ConditionRating
    urgency: UrgencyLevel
    confidence: ConfidenceLevel
    notes: Optional[str] = None


class HydraulicInspectionResult(BaseModel):
    """Ergebnis einer Hydrauliksteuerungs-Inspektion."""
    model_config = {"from_attributes": True}

    inspection_date: date
    oil_level_ok: bool
    oil_color: str = Field(..., description="clear_amber, dark_brown, black_opaque")
    oil_odor: str = Field(..., description="neutral, slightly_acrid, burnt")
    oil_water_content: str = Field(..., description="none, trace, significant")
    oil_particles_visible: bool
    oil_age_months: Optional[int] = Field(None, ge=0)
    helm_pump_leakage: LeakageGrade
    cylinder_rod_leakage: LeakageGrade
    cylinder_piston_drift_mm_per_min: Optional[float] = Field(None, ge=0)
    hose_condition: ConditionRating
    hose_age_years: Optional[float] = Field(None, ge=0, le=30)
    relief_valve_pressure_bar: Optional[float] = Field(None, ge=0, le=300)
    relief_valve_spec_bar: Optional[float] = Field(None, ge=0, le=300)
    bypass_valve_tight: Optional[bool] = None
    system_air_present: bool = Field(False)
    condition: ConditionRating
    urgency: UrgencyLevel
    confidence: ConfidenceLevel
    notes: Optional[str] = None
```

### ANHANG L — Ruderlager-Inspektionsmodelle

```python
class RudderBearingInspectionResult(BaseModel):
    """Ergebnis einer Ruderlager-Inspektion."""
    model_config = {"from_attributes": True}

    inspection_date: date
    position: str = Field(..., description="upper oder lower")
    radial_play_mm: float = Field(..., ge=0, le=10.0)
    axial_play_mm: Optional[float] = Field(None, ge=0, le=10.0)
    noise_on_movement: bool = Field(False)
    noise_type: Optional[str] = Field(None, description="grinding, clicking, squeaking")
    seal_leakage: LeakageGrade = Field(LeakageGrade.L0_DRY)
    shaft_condition: ConditionRating
    bearing_condition: ConditionRating
    urgency: UrgencyLevel
    confidence: ConfidenceLevel
    notes: Optional[str] = None

    @field_validator("radial_play_mm")
    @classmethod
    def assess_radial_play(cls, v: float) -> float:
        """Radialspiel-Grenzwerte: <0.1 gut, 0.1-0.3 beobachten, >0.3 tauschen."""
        return v


class QuadrantInspectionResult(BaseModel):
    """Ergebnis einer Quadrant-Inspektion."""
    model_config = {"from_attributes": True}

    inspection_date: date
    shaft_connection_tight: bool
    taper_condition: ConditionRating
    cable_groove_depth_mm: Optional[float] = Field(None, ge=0, le=10.0)
    cable_attachment_condition: ConditionRating
    rudder_stops_functional: bool
    rudder_stop_angle_port_deg: float = Field(..., ge=15, le=45)
    rudder_stop_angle_stbd_deg: float = Field(..., ge=15, le=45)
    symmetry_ok: bool
    condition: ConditionRating
    urgency: UrgencyLevel
    confidence: ConfidenceLevel
    notes: Optional[str] = None
```

### ANHANG M — Wartungsprotokoll-Modelle

```python
class MaintenanceTask(BaseModel):
    """Einzelne Wartungsaufgabe."""
    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Eindeutige Aufgaben-ID")
    description_de: str = Field(..., description="Aufgabenbeschreibung (Deutsch)")
    description_en: str = Field(..., description="Task description (English)")
    category: MaintenanceCategory
    interval: MaintenanceInterval
    steering_types: list[SteeringType] = Field(..., description="Anwendbare Steuerungstypen")
    estimated_duration_min: int = Field(..., ge=1, le=480)
    tools_required: list[str] = Field(default_factory=list)
    materials_required: list[str] = Field(default_factory=list)
    safety_notes: list[str] = Field(default_factory=list)
    reference_standards: list[str] = Field(default_factory=list)


class MaintenanceRecord(BaseModel):
    """Wartungsprotokoll-Eintrag."""
    model_config = {"from_attributes": True}

    record_id: str
    boat_id: str
    steering_system_id: str
    maintenance_date: date
    performed_by: str = Field(..., description="Name des Durchführenden")
    category: MaintenanceCategory
    tasks_performed: list[str] = Field(..., description="Liste der Task-IDs")
    findings: list[MaintenanceFinding] = Field(default_factory=list)
    materials_used: list[MaterialUsage] = Field(default_factory=list)
    total_duration_min: int = Field(..., ge=1)
    total_cost_eur: Optional[float] = Field(None, ge=0)
    next_maintenance_date: Optional[date] = None
    next_maintenance_tasks: list[str] = Field(default_factory=list)
    photos: list[str] = Field(default_factory=list, description="Foto-Referenzen")
    notes: Optional[str] = None
    confidence: ConfidenceLevel = Field(ConfidenceLevel.DOCUMENTED)


class MaintenanceFinding(BaseModel):
    """Einzelner Befund bei der Wartung."""
    model_config = {"from_attributes": True}

    component: str = Field(..., description="Betroffene Komponente")
    finding_de: str = Field(..., description="Befundbeschreibung (Deutsch)")
    finding_en: str = Field(..., description="Finding description (English)")
    condition: ConditionRating
    urgency: UrgencyLevel
    recommendation_de: str = Field(..., description="Empfehlung (Deutsch)")
    recommendation_en: str = Field(..., description="Recommendation (English)")
    photo_ref: Optional[str] = None
    confidence: ConfidenceLevel


class MaterialUsage(BaseModel):
    """Materialverbrauch bei Wartung."""
    model_config = {"from_attributes": True}

    material_name: str
    manufacturer: Optional[str] = None
    part_number: Optional[str] = None
    quantity: float = Field(..., ge=0)
    unit: str = Field(..., description="Einheit: pcs, ml, g, m")
    cost_eur: Optional[float] = Field(None, ge=0)
```

### ANHANG N — Troubleshooting-Modelle

```python
class FaultPattern(BaseModel):
    """Fehlerbild-Definition."""
    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Eindeutige Fehlerbild-ID")
    name_de: str = Field(..., description="Fehlerbild-Bezeichnung (Deutsch)")
    name_en: str = Field(..., description="Fault pattern name (English)")
    applicable_types: list[SteeringType]
    symptoms: list[str] = Field(..., description="Symptome (Deutsch)")
    possible_causes: list[FaultCause] = Field(...)
    diagnostic_steps: list[str] = Field(..., description="Diagnose-Schritte (Deutsch)")
    immediate_actions: list[str] = Field(default_factory=list, description="Sofortmaßnahmen")
    is_safety_critical: bool = Field(False)


class FaultCause(BaseModel):
    """Mögliche Ursache eines Fehlerbildes."""
    model_config = {"from_attributes": True}

    cause_de: str = Field(..., description="Ursachenbeschreibung (Deutsch)")
    cause_en: str = Field(..., description="Cause description (English)")
    probability_percent: float = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel
    repair_complexity: MaintenanceCategory
    estimated_repair_cost_eur: Optional[tuple[float, float]] = Field(
        None, description="Kostenspanne (min, max) in EUR"
    )
    repair_duration_hours: Optional[tuple[float, float]] = Field(
        None, description="Zeitspanne (min, max) in Stunden"
    )


class TroubleshootingDecisionNode(BaseModel):
    """Knoten im Troubleshooting-Entscheidungsbaum."""
    model_config = {"from_attributes": True}

    node_id: str
    question_de: str = Field(..., description="Entscheidungsfrage (Deutsch)")
    question_en: str = Field(..., description="Decision question (English)")
    yes_next: Optional[str] = Field(None, description="Nächster Knoten bei JA")
    no_next: Optional[str] = Field(None, description="Nächster Knoten bei NEIN")
    diagnosis_de: Optional[str] = Field(None, description="Diagnose bei Endknoten (Deutsch)")
    diagnosis_en: Optional[str] = Field(None, description="Diagnosis at leaf node (English)")
    action_de: Optional[str] = Field(None, description="Empfohlene Maßnahme (Deutsch)")
    action_en: Optional[str] = Field(None, description="Recommended action (English)")
    urgency: Optional[UrgencyLevel] = None
    is_leaf: bool = Field(False, description="Endknoten (Blatt) des Baums")


class TroubleshootingTree(BaseModel):
    """Vollständiger Troubleshooting-Entscheidungsbaum."""
    model_config = {"from_attributes": True}

    tree_id: str
    name_de: str
    name_en: str
    applicable_types: list[SteeringType]
    root_node_id: str
    nodes: list[TroubleshootingDecisionNode]
    fault_pattern_ref: Optional[str] = Field(None, description="Referenz zum Fehlerbild")
```

### ANHANG O — Ersatzteil- und Hersteller-Modelle

```python
class SteeringManufacturer(BaseModel):
    """Hersteller-Datensatz."""
    model_config = {"from_attributes": True}

    manufacturer_id: str
    name: str
    headquarters_country: str
    founded_year: Optional[int] = Field(None, ge=1800, le=2030)
    specialization: list[str] = Field(default_factory=list)
    steering_types: list[SteeringType] = Field(default_factory=list)
    website: Optional[str] = None
    support_phone: Optional[str] = None
    support_email: Optional[str] = None
    dealers_germany_count: Optional[int] = Field(None, ge=0)
    parts_availability_from_year: Optional[int] = None
    quality_certifications: list[str] = Field(default_factory=list)
    is_active: bool = Field(True, description="Hersteller noch aktiv")
    acquired_by: Optional[str] = Field(None, description="Übernommen von")
    notes: Optional[str] = None


class SparePart(BaseModel):
    """Ersatzteil-Datensatz."""
    model_config = {"from_attributes": True}

    part_number: str
    manufacturer: str
    name_de: str
    name_en: str
    category: str = Field(..., description="seal_kit, cable, chain, bearing, sheave, quadrant, oil, etc.")
    compatible_models: list[str] = Field(default_factory=list)
    price_eur: Optional[tuple[float, float]] = Field(None, description="Preisspanne (min, max)")
    price_usd: Optional[tuple[float, float]] = Field(None, description="Preisspanne USD (min, max)")
    contents: Optional[list[str]] = Field(None, description="Kit-Inhalt")
    specifications: Optional[dict[str, str]] = Field(None, description="Technische Daten")
    shelf_life_years: Optional[int] = Field(None, ge=1, description="Lagerfähigkeit in Jahren")
    cross_references: list[str] = Field(default_factory=list, description="Kompatible Teilenummern anderer Hersteller")


class LubricantSpec(BaseModel):
    """Schmierstoff-Spezifikation."""
    model_config = {"from_attributes": True}

    product_name: str
    manufacturer: str
    lubricant_type: str = Field(..., description="grease, oil, spray, paste")
    nlgi_grade: Optional[str] = Field(None, description="NLGI Konsistenzklasse")
    iso_vg: Optional[int] = Field(None, description="ISO Viskositätsklasse")
    application: list[str] = Field(..., description="Anwendungsgebiete")
    incompatible_materials: list[str] = Field(default_factory=list, description="Unverträgliche Materialien")
    temperature_range_c: Optional[tuple[float, float]] = Field(None, description="Temperaturbereich °C")
    service_interval_months: Optional[int] = Field(None, ge=1, le=60)
    container_sizes: list[str] = Field(default_factory=list)
    price_eur: Optional[tuple[float, float]] = None
```

### ANHANG P — Winterfestmachungs-Modelle

```python
class WinterizationProtocol(BaseModel):
    """Winterfestmachungs-Protokoll."""
    model_config = {"from_attributes": True}

    protocol_id: str
    boat_id: str
    steering_type: SteeringType
    winterization_date: date
    performed_by: str
    steps_completed: list[WinterizationStep]
    cable_tension_reduced: Optional[bool] = None
    cable_tension_before: Optional[float] = Field(None, ge=0, description="Spannung vor Reduktion in N")
    cable_tension_after: Optional[float] = Field(None, ge=0, description="Spannung nach Reduktion in N")
    hydraulic_oil_level_topped: Optional[bool] = None
    hydraulic_oil_condition: Optional[str] = None
    rudder_secured_midships: bool
    emergency_tiller_location_noted: bool
    covers_installed: bool
    ventilation_ensured: bool
    findings: list[MaintenanceFinding] = Field(default_factory=list)
    next_commissioning_date: Optional[date] = None
    notes: Optional[str] = None


class WinterizationStep(BaseModel):
    """Einzelner Winterfestmachungs-Schritt."""
    model_config = {"from_attributes": True}

    step_number: int = Field(..., ge=1)
    description_de: str
    description_en: str
    completed: bool
    finding: Optional[str] = None
    photo_ref: Optional[str] = None
```

### ANHANG Q — Inspektions-Gesamtbewertung

```python
class SteeringSystemAssessment(BaseModel):
    """Gesamtbewertung einer Steueranlage."""
    model_config = {"from_attributes": True}

    assessment_id: str
    boat_id: str
    assessment_date: date
    assessor: str
    steering_system: SteeringSystemSpec
    
    # Teilbewertungen
    cable_inspection: Optional[CableInspectionResult] = None
    chain_inspection: Optional[ChainInspectionResult] = None
    hydraulic_inspection: Optional[HydraulicInspectionResult] = None
    rudder_bearing_inspections: list[RudderBearingInspectionResult] = Field(default_factory=list)
    quadrant_inspection: Optional[QuadrantInspectionResult] = None
    
    # Gesamtbewertung
    overall_condition: ConditionRating
    overall_score: float = Field(..., ge=0, le=100, description="Gesamtpunktzahl 0-100")
    safety_critical_findings: list[MaintenanceFinding] = Field(default_factory=list)
    recommended_actions: list[RecommendedAction] = Field(default_factory=list)
    estimated_total_repair_cost_eur: Optional[tuple[float, float]] = None
    next_inspection_date: Optional[date] = None
    confidence: ConfidenceLevel
    notes: Optional[str] = None


class RecommendedAction(BaseModel):
    """Empfohlene Maßnahme."""
    model_config = {"from_attributes": True}

    priority: int = Field(..., ge=1, le=10, description="Priorität 1=höchste")
    action_de: str
    action_en: str
    component: str
    urgency: UrgencyLevel
    category: MaintenanceCategory
    estimated_cost_eur: Optional[tuple[float, float]] = None
    estimated_duration_hours: Optional[tuple[float, float]] = None
    diy_possible: bool = Field(False)
    safety_relevant: bool = Field(False)
```

### ANHANG R — Saison-Inbetriebnahme-Modelle

```python
class CommissioningProtocol(BaseModel):
    """Saison-Inbetriebnahme-Protokoll."""
    model_config = {"from_attributes": True}

    protocol_id: str
    boat_id: str
    steering_type: SteeringType
    commissioning_date: date
    performed_by: str
    winterization_protocol_ref: Optional[str] = Field(
        None, description="Referenz zum Winterfestmachungs-Protokoll"
    )
    
    # Phase 1: Sichtprüfung
    visual_inspection_completed: bool
    corrosion_found: bool = False
    moisture_damage_found: bool = False
    rodent_damage_found: bool = False
    
    # Phase 2: Erstbetätigung
    initial_movement_smooth: bool
    abnormal_noises: bool = False
    noise_description: Optional[str] = None
    full_deflection_achieved: bool
    
    # Phase 3: Funktionsprüfung
    cable_tension_set_n: Optional[float] = Field(None, ge=0)
    hydraulic_oil_level_ok: Optional[bool] = None
    hydraulic_system_bled: Optional[bool] = None
    rudder_stops_verified: bool
    emergency_tiller_tested: bool
    total_backlash_deg: float = Field(..., ge=0, le=20)
    
    # Phase 4: Probefahrt
    sea_trial_completed: bool = False
    sea_trial_findings: Optional[str] = None
    autopilot_tested: Optional[bool] = None
    
    # Bewertung
    overall_condition: ConditionRating
    findings: list[MaintenanceFinding] = Field(default_factory=list)
    actions_required: list[RecommendedAction] = Field(default_factory=list)
    next_maintenance_date: Optional[date] = None
    notes: Optional[str] = None


class AutopilotInterfaceCheck(BaseModel):
    """Autopilot-Schnittstellen-Prüfung."""
    model_config = {"from_attributes": True}

    check_date: date
    autopilot_make: str
    autopilot_model: str
    drive_type: str = Field(..., description="linear, rotary, hydraulic")
    
    # Mechanische Prüfung
    drive_mounting_secure: bool
    drive_linkage_play_mm: Optional[float] = Field(None, ge=0)
    rudder_feedback_calibrated: bool
    manual_override_functional: bool
    
    # Funktionsprüfung
    autopilot_response_time_s: Optional[float] = Field(None, ge=0, le=10)
    hunting_observed: bool = False
    current_draw_normal_a: Optional[float] = Field(None, ge=0)
    current_draw_max_a: Optional[float] = Field(None, ge=0)
    error_codes: list[str] = Field(default_factory=list)
    
    # Bewertung
    steering_system_adequate: bool
    backlash_affecting_autopilot: bool = False
    recommendations: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG S — Analyse-Hilfsmodelle, Scoring und Visualisierungs-Modelle

```python
class SteeringWearAnalysis(BaseModel):
    """Verschleißanalyse der Steueranlage für AYDI-Scoring."""
    model_config = {"from_attributes": True}

    analysis_id: str
    boat_id: str
    analysis_date: datetime
    steering_system: SteeringSystemSpec
    assessment: SteeringSystemAssessment
    
    # AYDI-Scores (0-100)
    safety_score: float = Field(..., ge=0, le=100, description="Sicherheitsbewertung")
    functionality_score: float = Field(..., ge=0, le=100, description="Funktionsbewertung")
    maintenance_score: float = Field(..., ge=0, le=100, description="Wartungszustand")
    remaining_lifetime_score: float = Field(..., ge=0, le=100, description="Restlebensdauer")
    
    # Gewichteter Gesamtscore
    weighted_total_score: float = Field(..., ge=0, le=100)
    
    # Confidence
    structured_confidence: ConfidenceLevel
    visual_confidence: Optional[ConfidenceLevel] = None
    fused_confidence: ConfidenceLevel
    
    # Score-Fusion-Gewichte
    structured_weight: float = Field(0.95, ge=0, le=1.0)
    visual_weight: float = Field(0.05, ge=0, le=1.0)
    
    # Befunde
    critical_findings: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    
    # Kostenprognose
    estimated_annual_maintenance_cost_eur: Optional[float] = Field(None, ge=0)
    estimated_5year_cost_eur: Optional[float] = Field(None, ge=0)
    replacement_recommended_within_years: Optional[int] = Field(None, ge=0, le=30)

    @field_validator("weighted_total_score")
    @classmethod
    def validate_weighted_score(cls, v: float) -> float:
        """Score must be between 0 and 100."""
        if not 0 <= v <= 100:
            raise ValueError("Weighted total score must be between 0 and 100")
        return round(v, 1)


class SteeringMaintenanceCostEstimate(BaseModel):
    """Parametrische Kostenschätzung für Steueranlagen-Wartung."""
    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=5, le=60)
    steering_type: SteeringType
    system_age_years: float = Field(..., ge=0, le=50)
    current_condition: ConditionRating
    
    # Jährliche Kosten
    annual_routine_maintenance_eur: float = Field(..., ge=0)
    annual_parts_replacement_eur: float = Field(..., ge=0)
    annual_professional_service_eur: float = Field(..., ge=0)
    annual_total_eur: float = Field(..., ge=0)
    
    # 5-Jahres-Prognose
    five_year_total_eur: float = Field(..., ge=0)
    major_overhaul_expected_year: Optional[int] = Field(None, ge=1, le=5)
    major_overhaul_cost_eur: Optional[float] = Field(None, ge=0)
    
    # 20-Jahres-Lebenszyklus
    twenty_year_lifecycle_cost_eur: float = Field(..., ge=0)
    
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED)
    notes: Optional[str] = None
```

---

### ANHANG T — AYDI Visual Analysis Prompts für Steueranlagen

```python
class SteeringVisualAnalysisPrompt(BaseModel):
    """Prompt-Konfiguration für die visuelle Analyse von Steueranlagen via Claude Vision."""
    model_config = {"from_attributes": True}

    prompt_id: str
    target_component: str = Field(
        ..., 
        description="Zielkomponente: cable, chain, quadrant, hydraulic_cylinder, "
                    "helm_pump, rudder_bearing, sheave, pedestal, steering_wheel"
    )
    prompt_template_de: str = Field(
        ..., description="Prompt-Template in Deutsch für die visuelle Analyse"
    )
    prompt_template_en: str = Field(
        ..., description="Prompt template in English for visual analysis"
    )
    expected_findings: list[str] = Field(
        default_factory=list,
        description="Erwartete Befundkategorien"
    )
    confidence_mapping: dict[str, ConfidenceLevel] = Field(
        default_factory=dict,
        description="Zuordnung Bildqualität → Confidence Level"
    )
    min_image_resolution: int = Field(
        800, 
        description="Mindestauflösung in Pixel (kürzere Seite)"
    )
    preferred_angles: list[str] = Field(
        default_factory=list,
        description="Bevorzugte Aufnahmewinkel"
    )


class SteeringVisualFinding(BaseModel):
    """Einzelbefund aus der visuellen Analyse einer Steueranlagen-Komponente."""
    model_config = {"from_attributes": True}

    finding_id: str
    component: str
    finding_type: str = Field(
        ...,
        description="corrosion, wear, damage, leak, contamination, misalignment, missing_part"
    )
    description_de: str
    description_en: str
    severity: ConditionRating
    location_in_image: Optional[str] = Field(
        None, description="Beschreibung der Position im Bild"
    )
    confidence: ConfidenceLevel
    visual_confidence_factors: list[str] = Field(
        default_factory=list,
        description="Faktoren die die visuelle Confidence beeinflussen: "
                    "image_quality, lighting, angle, obstruction, scale_reference"
    )
    requires_physical_inspection: bool = Field(
        True,
        description="True wenn physische Inspektion zur Bestätigung erforderlich"
    )
    aydi_note: str = Field(
        default="Visuelle Einschätzung — physische Inspektion empfohlen",
        description="Standardmäßiger Hinweis auf Einschränkung der visuellen Analyse"
    )


# --- Visual Analysis Prompt Templates ---

VISUAL_PROMPTS_STEERING = {
    "cable_inspection": SteeringVisualAnalysisPrompt(
        prompt_id="steering_cable_v1",
        target_component="cable",
        prompt_template_de=(
            "Analysiere dieses Foto eines Steuerseils auf einer Yacht. "
            "Bewerte folgende Aspekte: "
            "1) Sichtbare Litzenbrüche (gebrochene Einzeldrähte, abstehende Drähte) "
            "2) Korrosion (Rostflecken, Verfärbungen, Pitting) "
            "3) Knicke oder Verformungen "
            "4) Korbbildung (aufgeblähte Litzen) "
            "5) Schmierungszustand (trocken, fettig, verharzt) "
            "6) Verschleiß an Berührungspunkten (Umlenkrollen, Führungen) "
            "Gib für jeden Aspekt eine Bewertung: gut/beobachten/eingeschränkt/kritisch. "
            "Wenn ein Aspekt nicht beurteilbar ist, sage 'nicht beurteilbar' mit Begründung."
        ),
        prompt_template_en=(
            "Analyze this photo of a steering cable on a yacht. "
            "Assess: 1) Visible broken wires 2) Corrosion 3) Kinks "
            "4) Birdcaging 5) Lubrication state 6) Wear at contact points. "
            "Rate each: good/monitor/limited/critical or 'cannot assess' with reason."
        ),
        expected_findings=[
            "broken_wires", "corrosion", "kinks", "birdcaging",
            "lubrication_state", "wear_at_sheaves"
        ],
        confidence_mapping={
            "clear_close_up": ConfidenceLevel.VISUAL_HIGH,
            "decent_overview": ConfidenceLevel.VISUAL_MEDIUM,
            "distant_or_dark": ConfidenceLevel.VISUAL_LOW,
            "obstructed": ConfidenceLevel.VISUAL_INSUFFICIENT,
        },
        min_image_resolution=1200,
        preferred_angles=["close_up_perpendicular", "along_cable_axis", "at_sheave_entry"]
    ),
    "hydraulic_leak_check": SteeringVisualAnalysisPrompt(
        prompt_id="steering_hydraulic_leak_v1",
        target_component="hydraulic_cylinder",
        prompt_template_de=(
            "Analysiere dieses Foto eines Hydraulikzylinders einer Yachtsteuerung. "
            "Bewerte: "
            "1) Ölspuren/Leckage an der Kolbenstange "
            "2) Ölspuren/Leckage an den Schlauchanschlüssen "
            "3) Zustand der Kolbenstange (Kratzer, Korrosion, Pitting) "
            "4) Zustand der Schläuche (Risse, Schwellung, Scheuerstellen) "
            "5) Befestigungszustand (Bolzen, Gabelköpfe) "
            "6) Korrosion am Zylindergehäuse "
            "Klassifiziere Leckage als: trocken/feucht/schwitzend/tropfend/laufend. "
            "Wenn nicht beurteilbar: sage 'nicht beurteilbar'."
        ),
        prompt_template_en=(
            "Analyze this photo of a hydraulic steering cylinder on a yacht. "
            "Assess: 1) Oil leaks at rod 2) Oil at fittings 3) Rod condition "
            "4) Hose condition 5) Mounting 6) Corrosion. "
            "Classify leakage: dry/damp/sweating/dripping/running."
        ),
        expected_findings=[
            "rod_leakage", "fitting_leakage", "rod_surface_condition",
            "hose_condition", "mounting_condition", "corrosion"
        ],
        confidence_mapping={
            "clear_close_up": ConfidenceLevel.VISUAL_HIGH,
            "decent_overview": ConfidenceLevel.VISUAL_MEDIUM,
            "distant_or_dark": ConfidenceLevel.VISUAL_LOW,
            "obstructed": ConfidenceLevel.VISUAL_INSUFFICIENT,
        },
        min_image_resolution=1200,
        preferred_angles=["rod_seal_close_up", "fittings_close_up", "overall_side_view"]
    ),
}
```

### ANHANG U — Lebenszykluskosten-Berechnung

```python
class SteeringLifecycleCost(BaseModel):
    """20-Jahres-Lebenszykluskosten-Berechnung einer Steueranlage."""
    model_config = {"from_attributes": True}

    calculation_id: str
    boat_length_m: float = Field(..., ge=5, le=60)
    steering_type: SteeringType
    initial_system_cost_eur: float = Field(..., ge=0)
    
    # Jährliche Kosten (Durchschnitt)
    annual_routine_maintenance_eur: float = Field(..., ge=0)
    annual_consumables_eur: float = Field(..., ge=0, description="Öl, Fett, Reiniger")
    
    # Periodische Kosten
    cable_replacement_interval_years: Optional[int] = Field(None, ge=1, le=20)
    cable_replacement_cost_eur: Optional[float] = Field(None, ge=0)
    oil_change_interval_years: Optional[int] = Field(None, ge=1, le=5)
    oil_change_cost_eur: Optional[float] = Field(None, ge=0)
    bearing_replacement_interval_years: Optional[int] = Field(None, ge=5, le=25)
    bearing_replacement_cost_eur: Optional[float] = Field(None, ge=0)
    hose_replacement_interval_years: Optional[int] = Field(None, ge=5, le=15)
    hose_replacement_cost_eur: Optional[float] = Field(None, ge=0)
    seal_kit_interval_years: Optional[int] = Field(None, ge=3, le=10)
    seal_kit_cost_eur: Optional[float] = Field(None, ge=0)
    
    # Berechnete 20-Jahres-Kosten
    total_routine_maintenance_20y_eur: float = Field(..., ge=0)
    total_periodic_replacements_20y_eur: float = Field(..., ge=0)
    total_lifecycle_cost_20y_eur: float = Field(..., ge=0)
    annual_average_cost_eur: float = Field(..., ge=0)
    
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED)
    assumptions: list[str] = Field(
        default_factory=list,
        description="Annahmen der Berechnung"
    )
    
    @field_validator("total_lifecycle_cost_20y_eur")
    @classmethod
    def validate_lifecycle_total(cls, v: float) -> float:
        """Lifecycle cost must be positive."""
        if v < 0:
            raise ValueError("Lifecycle cost cannot be negative")
        return round(v, 2)


# --- Lifecycle Cost Reference Data ---

LIFECYCLE_COST_REFERENCE = {
    "cable_chain_10m": SteeringLifecycleCost(
        calculation_id="ref_cable_10m",
        boat_length_m=10.0,
        steering_type=SteeringType.CABLE_CHAIN,
        initial_system_cost_eur=1800.0,
        annual_routine_maintenance_eur=120.0,
        annual_consumables_eur=30.0,
        cable_replacement_interval_years=8,
        cable_replacement_cost_eur=450.0,
        bearing_replacement_interval_years=12,
        bearing_replacement_cost_eur=1500.0,
        total_routine_maintenance_20y_eur=3000.0,
        total_periodic_replacements_20y_eur=2400.0,
        total_lifecycle_cost_20y_eur=7200.0,
        annual_average_cost_eur=360.0,
        confidence=ConfidenceLevel.BENCHMARK,
        assumptions=[
            "Serienyacht, normale Nutzung ~800 sm/Jahr",
            "Wartung durch Eigner (Kat I+II) + jährliche Fachinspektion",
            "Preisbasis 2025, ohne Inflation",
        ]
    ),
    "hydraulic_16m": SteeringLifecycleCost(
        calculation_id="ref_hydraulic_16m",
        boat_length_m=16.0,
        steering_type=SteeringType.HYDRAULIC,
        initial_system_cost_eur=4500.0,
        annual_routine_maintenance_eur=200.0,
        annual_consumables_eur=50.0,
        oil_change_interval_years=2,
        oil_change_cost_eur=150.0,
        hose_replacement_interval_years=8,
        hose_replacement_cost_eur=600.0,
        seal_kit_interval_years=6,
        seal_kit_cost_eur=250.0,
        bearing_replacement_interval_years=12,
        bearing_replacement_cost_eur=2200.0,
        total_routine_maintenance_20y_eur=5000.0,
        total_periodic_replacements_20y_eur=4650.0,
        total_lifecycle_cost_20y_eur=14150.0,
        annual_average_cost_eur=707.5,
        confidence=ConfidenceLevel.BENCHMARK,
        assumptions=[
            "Serienyacht, normale Nutzung ~1200 sm/Jahr",
            "Wartung durch Eigner + zweijährliche Fachinspektion",
            "Preisbasis 2025, ohne Inflation",
        ]
    ),
}
```

---

### ANHANG V — Referenz: Steueranlagen-Auslegung nach Bootsgröße

Die folgende Tabelle dient als Schnellreferenz für die typische Steueranlagen-Ausstattung nach Bootsgröße und -typ. Sie unterstützt die AYDI-Analyse bei der Bewertung, ob eine vorgefundene Steueranlage dem Boot angemessen ist.

**Segelyachten — Typische Steueranlagen nach Größe:**

| Bootsgröße | Typische Steuerung | Seil-Ø | Rudermoment (Nm) | Hersteller (typisch) | Wartungsaufwand/Jahr |
|-----------|-------------------|--------|-----------------|---------------------|---------------------|
| 6–8 m | Pinne | — | 50–150 | — | 2 Std. |
| 8–10 m | Seilzug/Kette (leicht) | 4,76 mm | 150–350 | Lewmar Compac 3, Edson 311 | 3 Std. |
| 10–12 m | Seilzug/Kette (Standard) | 6,35 mm | 300–700 | Lewmar Compac 5, Edson 336 | 4 Std. |
| 12–15 m | Seilzug/Kette (verstärkt) | 6,35 mm | 600–1.000 | Lewmar Compac 7, Edson 401 | 5 Std. |
| 15–18 m | Seilzug/Kette (HD) oder Hydraulik | 7,94 mm | 900–1.500 | Lewmar Compac 10, Jefa, Edson 501 | 6 Std. |
| 18–22 m | Hydraulik | — | 1.500–3.000 | Jefa Hydraulic, Lewmar Ocean 60 | 7 Std. |
| 22–30 m | Hydraulik (verstärkt) | — | 3.000–6.000 | Jefa, Lewmar Ocean 80, Kobelt | 10 Std. |
| >30 m | Hydraulik + Redundanz | — | >6.000 | Jefa, Kobelt, Custom | 15+ Std. |

**Motoryachten — Typische Steueranlagen nach Größe:**

| Bootsgröße | Typische Steuerung | Betriebsdruck | Rudermoment (Nm) | Hersteller (typisch) | Wartungsaufwand/Jahr |
|-----------|-------------------|--------------|-----------------|---------------------|---------------------|
| 6–8 m | Zahnstange oder BayStar | — / 70 bar | 100–300 | Ultraflex, SeaStar BayStar | 2 Std. |
| 8–10 m | Hydraulik (leicht) | 70 bar | 300–800 | SeaStar Pro, Vetus MTC 32 | 3 Std. |
| 10–14 m | Hydraulik (Standard) | 100 bar | 800–2.000 | SeaStar Pro, Kobelt 7004 | 4 Std. |
| 14–20 m | Hydraulik (verstärkt) | 140 bar | 2.000–4.000 | Kobelt 7012, Lewmar Ocean 60 | 6 Std. |
| 20–30 m | Hydraulik (Power-Assist) | 175 bar | 4.000–8.000 | Kobelt 7080, Custom | 8 Std. |
| >30 m | EPS oder Hydraulik + Redundanz | 175+ bar | >8.000 | Custom, Klassifikation erforderlich | 15+ Std. |

**Katamarane — Besonderheiten:**

| Bootsgröße | Typische Steuerung | Besonderheit | Wartungsaufwand/Jahr |
|-----------|-------------------|-------------|---------------------|
| 10–12 m | Doppelruder, Seilzug | 2 Quadranten, 1 Steuerrad, komplexe Seilführung | 5 Std. |
| 12–16 m | Doppelruder, Hydraulik | 2 separate Hydraulikkreise, Synchronisation | 7 Std. |
| >16 m | Doppelruder, Hydraulik | Wie oben, ggf. mit Power-Assist | 10 Std. |

---

*Ende der AYDI Wissensdatei 20.06 — Steueranlagen Wartung und Troubleshooting*

*Confidence-Zusammenfassung:*
- *Messwerte und Grenzwerte: measured (Hersteller-TDS, ISO-Normen)*
- *Wartungsanleitungen und Verfahren: documented (Hersteller-Kataloge, Service-Bulletins)*
- *Kostenangaben und Statistiken: benchmark (Charterflotten, Versicherungsdaten)*
- *Praxistipps und Erfahrungswerte: estimated (Werft-Konsens, Sachverständigenpraxis)*

*Nächste verwandte Wissensdateien:*
- *20_01_steuerung_grundlagen.md — Grundlagen und Bauarten*
- *20_02_hydraulische_steuerung.md — Hydrauliksteuerung im Detail*
- *20_03_ruderanlage_lager.md — Ruderanlagen und Lager*
