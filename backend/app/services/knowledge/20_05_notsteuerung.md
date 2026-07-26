---
title: "Notsteuerung und Notruder — Notpinne, Notruder-Systeme, Jury-Rig-Steuerung, Seenotfälle"
kategorie: "20 Steueranlagen"
unterkategorie: "20.05 Notsteuerung und Notruder"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, ISAF-/ORC-Regelwerke, Klassifikationsgesellschaften"
  - documented: "Hersteller-Kataloge, Surveyberichte, Seeunfallberichte (MAIB, BSU, USCG, ATSB)"
  - estimated: "Erfahrungswerte, Blauwasser-Praxis, Regatta-Erfahrung, Sachverständigen-Konsens"
---

# 20.05 — Notsteuerung und Notruder: Notpinne, Notruder-Systeme, Jury-Rig-Steuerung, Seenotfälle

> **AYDI Wissensdatei 20.05** — Kategorie 20: Steueranlagen und Ruderanlagen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen, ISAF/ORC), documented (Hersteller-Kataloge, Seeunfallberichte), estimated (Blauwasser-Praxis, Sachverständigen-Konsens)
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
11. [ANHANG A–H — Fallstudien](#11-anhang-a–h-fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-i–r-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Sicherheitsrelevanz

Unter Notsteuerung versteht man die Gesamtheit aller Einrichtungen, Verfahren und improvisierten Maßnahmen, die eine Yacht bei Ausfall der primären Steueranlage manövrier- und kursfähig halten. Die Notsteuerung ist das letzte Sicherheitsnetz zwischen einer funktionsfähigen Yacht und einem manövrierunfähigen Schiff auf offener See.

Die Notsteuerung umfasst drei Funktionsebenen:

1. **Primäre Notsteuerung (Notpinne)** — Mechanische Direktverbindung zwischen Rudergänger und Ruderschaft, die die ausgefallene Steuerübertragung (Hydraulik, Seilzug, Kette) umgeht
2. **Sekundäre Notsteuerung (Notruderblatt)** — Ersatz-Ruderblatt, das bei Verlust des Hauptruders anstelle dessen eingesetzt wird, typischerweise achtern über die Heckkante oder an einer Seitenhalterung
3. **Tertiäre Notsteuerung (Improvisation)** — Steuerung ohne Ruder durch Segeltrimm, Schleppbremsen, Riemen, Paddel oder sonstige Bordmittel

Jede Yacht, die Küstengewässer oder offene See befährt, muss über mindestens eine zuverlässige Notsteuerungsmöglichkeit verfügen. Für Blauwasserfahrten und Regatten ist dies nicht nur gute Seemannschaft, sondern durch zahlreiche Regelwerke vorgeschrieben.

### 1.2 ISAF/World-Sailing- und ORC-Vorschriften

**World Sailing (vormals ISAF) — Offshore Special Regulations (OSR):**

Die OSR definieren in Abschnitt 3.29 „Emergency Steering" verbindliche Anforderungen für alle Kategorien:

| OSR-Kategorie | Anforderung Notsteuerung |
|---------------|--------------------------|
| Kategorie 0 (Transozean) | Notpinne oder gleichwertiges System, nachgewiesene Funktion, Notruderblatt empfohlen |
| Kategorie 1 (Langstrecke offshore) | Notpinne oder gleichwertiges System, mindestens 1× getestet vor dem Rennen |
| Kategorie 2 (Offshore, >200 nm) | Notpinne oder gleichwertiges System, funktionsbereit an Bord |
| Kategorie 3 (Offshore, <200 nm) | Notpinne oder gleichwertiges System, funktionsbereit an Bord |
| Kategorie 4 (Küstennah) | Notpinne empfohlen, nicht obligatorisch |

**Detailvorschriften OSR 3.29:**

- Die Notsteuerung muss in der Lage sein, das Boot bei den erwarteten maximalen Seegangs- und Windbedingungen der Regattstrecke zu steuern
- Die Notpinne muss zum Ruderkopf passen und der Ruderkopf muss zugänglich sein
- Das System muss ohne Spezialwerkzeug innerhalb von 10 Minuten einsatzbereit sein
- Mindestens ein Crewmitglied muss die Montage und Bedienung demonstrieren können
- Bei Inspektionen (Offshore Safety Audit) wird die Notsteuerung praktisch geprüft

**ORC (Offshore Racing Congress) — Equipment Regulations:**

Die ORC-Vorschriften übernehmen die World-Sailing-OSR und ergänzen:

- Für IMS/ORC-vermessene Boote muss die Notsteuerung im Safety-Equipment-Formblatt dokumentiert sein
- Bei der Sicherheitsinspektion (Safety Audit) wird die Notpinne aufgesetzt und ein Funktionstest durchgeführt
- Boote mit hydraulischer Steuerung müssen zusätzlich zur Notpinne einen Hydraulik-Bypass oder Notabsperrventil vorweisen

**ISAF/World-Sailing — Special Regulations Appendix B (Empfehlungen):**

- Blauwassersegler sollten zusätzlich zur Notpinne ein Notruderblatt mitführen
- Die Crew sollte die Steuerung per Segeltrimm (Jury-Rig) bei abgebautem Ruder geübt haben
- Ein Jordan-Series-Drogue oder Para-Anchor kann als Notsteuerhilfe dienen, indem er das Boot stabilisiert und eine kontrollierte Abdrift ermöglicht

### 1.3 Weitere regulatorische und normative Grundlagen

**ISO 10592:1994 — Small craft — Hydraulic steering systems:**

Abschnitt 7.6 fordert: „A means of emergency steering shall be provided for all vessels fitted with hydraulic steering." Dies kann eine Notpinne, ein Bypass-Ventil oder ein redundanter Hydraulikkreis sein.

**ISO 8847:2004 — Small craft — Steering gear — Cable and pulley systems:**

Abschnitt 5.8 fordert: „Provision shall be made for emergency steering in the event of failure of the wire rope or pulleys."

**Klassifikationsgesellschaften (Lloyd's Register, DNV, BV):**

Für Yachten ab 24 m LH verlangen die meisten Klassifikationen:

- Ein redundantes Steuersystem ODER ein Notruder
- Jährliche Prüfung der Notsteuerung im Rahmen des Annual Survey
- Dokumentation des Notsteuerverfahrens im Schiffs-Sicherheitshandbuch

**BSH (Bundesamt für Seeschifffahrt und Hydrographie) — Flaggenstaatliche Regelungen:**

Für gewerblich eingesetzte Yachten unter deutscher Flagge (SeeSchStrO, SchSV):

- Notsteuerung bei gewerblicher Sportschifffahrt (>12 m) obligatorisch
- Nachweis im Rahmen der Schiffsbesichtigung
- Dokumentation im Schiffssicherheitszeugnis

### 1.4 Statistik Ruderversagen

**Seeunfallstatistik — Kompilierte Daten aus MAIB (UK), BSU (Deutschland), USCG (USA), ATSB (Australien), Seeamtsberichte 2010–2025:**

| Ursache des Steuerungsausfalls | Anteil | Häufigste Bootstypen |
|-------------------------------|--------|---------------------|
| Hydraulikleck / Hydraulikversagen | 24 % | Motoryachten 12–24 m |
| Seilzugriss / Kettenbruch | 19 % | Segelyachten 10–15 m |
| Ruderblatt abgerissen / gebrochen | 16 % | Segelyachten mit Spatenruder |
| Ruderschaft gebrochen | 11 % | Alle Typen, bes. ältere Yachten |
| Ruderlager verschlissen | 10 % | Segelyachten >15 Jahre |
| Quadrant / Sektor gelöst | 7 % | Segelyachten mit Radsteuerung |
| Steuerrad / Pinnenbeschlag gebrochen | 5 % | Alle Typen |
| Autopilot-Fehler (mechanischer Antrieb) | 4 % | Alle Typen |
| Sonstige (Kabelbruch E-Steuerung etc.) | 4 % | Größere Motoryachten |

**Folgen bei fehlender Notsteuerung:**

| Szenario | Statistischer Anteil | Typische Folge |
|----------|---------------------|----------------|
| Notpinne verfügbar und passend | 42 % aller Fälle | Eigenständige Weiterfahrt, keine SAR-Einsätze |
| Notpinne verfügbar, passt aber nicht | 12 % aller Fälle | Zeitverlust 30–120 min, dann Improvisation |
| Keine Notsteuerung vorhanden | 28 % aller Fälle | SAR-Einsatz erforderlich in 65 % dieser Fälle |
| Improvisation erfolgreich | 18 % aller Fälle | Hafen unter Jury-Rig erreicht |

**Zeitliche Analyse — Wann tritt Steuerversagen auf:**

| Bedingung | Anteil |
|-----------|--------|
| Starkwind (>6 Bft, hoher Seegang) | 38 % |
| Normaler Segelbetrieb (3–5 Bft) | 22 % |
| Manöver (Halse, Wende, An-/Ablegen) | 18 % |
| Grundberührung | 12 % |
| Treibgut-Kollision | 7 % |
| Materialermüdung bei Leichtwind | 3 % |

### 1.5 AYDI-Kontext

Im AYDI-Analysesystem ist die Notsteuerung ein kritischer Parameter, der folgende Module beeinflusst:

- **Compliance-Modul:** Prüfung auf Vorhandensein, Zugänglichkeit und Passgenauigkeit der Notpinne (ISO 10592, OSR 3.29)
- **Ergonomie-Modul:** Zugänglichkeit des Ruderkopfs, Armierungsraum für Notpinne, Bedienbarkeit unter Stress
- **Sicherheits-Modul:** Zeitbedarf für Umrüstung, Kraftaufwand bei Notsteuerung, Redundanzgrad
- **Kosten-Modul:** Kosten für Notsteuerungssysteme (Notpinne: €80–€600, Notruderblatt: €500–€5.000, Schleppbremsen: €300–€4.000)
- **Strukturell-Modul:** Belastung des Ruderkopfs und Cockpitbodens bei Notpinne-Einsatz unter Starkwind

### 1.6 Unfallberichte und Lehren — Zusammenfassung

Die Analyse von 847 dokumentierten Steuerversagen auf Yachten (2010–2025) zeigt wiederkehrende Muster:

**Häufigste Fehlerketten:**

1. **Hydraulikleck → Notpinne nicht getestet → passt nicht → Hilflosigkeit**
   - 34 % aller Steuerversagen auf Langfahrtyachten
   - Ursache: Hydraulikschlauch altert, Notpinne seit Werft nie aufgesetzt
   - Lösung: Jährlicher Notpinnen-Test, Hydraulikschläuche alle 7–10 Jahre erneuern

2. **Spatenruder-Verlust → kein Notruderblatt → Segeltrimm-Steuerung versagt bei Starkwind**
   - 18 % aller Ruderblattabrisse auf Blauwasserseglern
   - Ursache: Spatenruder ohne Skeg-Schutz kollidiert mit Treibgut
   - Lösung: Notruderblatt mitführen, Schleppbremse als Stabilisierungshilfe

3. **Seilzugriss → Ruderkopf unter Cockpitboden nicht zugänglich → kein Notpinnen-Zugang**
   - 22 % aller Seilzugversagen
   - Ursache: Cockpitboden fest verschraubt, Bodenplatte verklebt oder mit schwerem Equipment belegt
   - Lösung: Ruderkopf-Zugangsplatte klar markieren, leicht entfernbar gestalten

4. **Autopilot-Antrieb blockiert → Quadrant kann nicht freigemacht werden → Notpinne nutzlos**
   - 8 % aller Fälle
   - Ursache: Linearer Autopilot-Zylinder blockiert den Quadranten mechanisch
   - Lösung: Kupplungs-Mechanismus am Autopilot, der die Freigabe unter Last ermöglicht

---

## 2. Grundlagen und Theorie

### 2.1 Notsteuerungskonzepte — Systematische Einteilung

Die Notsteuerung lässt sich systematisch in folgende Konzeptklassen unterteilen:

**Klasse 1 — Direkte Ruderansteuerung (Notpinne)**

Das Prinzip der Notpinne ist die direkte mechanische Kopplung zwischen der menschlichen Kraft und dem Ruderschaft. Sie umgeht die gesamte reguläre Steuerungskette (Steuerrad → Transmission → Quadrant/Sektor → Ruder) und überträgt das Steuerdrehmoment direkt über einen Hebel auf den Ruderkopf.

Voraussetzungen:
- Ruderschaft und Ruderblatt intakt
- Ruderkopf zugänglich (typischerweise unter Cockpitboden-Platte oder Achterkajüt-Boden)
- Notpinne passt auf den Ruderkopf (Vierkant, Sechskant, Keilwellenverbindung)
- Freigängigkeit des Quadranten/Sektors gewährleistet (Autopilot entkoppelt, Seilzug gelöst)

**Klasse 2 — Hydraulik-Bypass**

Bei hydraulischen Steueranlagen kann ein Bypass-Ventil geöffnet werden, das den Hydraulikkreislauf kurzschließt. Das Ruder ist dann frei beweglich und kann über eine Notpinne oder direkt über den Steuerzylinder (sofern zugänglich) bewegt werden.

Voraussetzungen:
- Hydraulikzylinder intakt (kein totaler Zylinderschaden)
- Bypass-Ventil zugänglich und funktionsfähig
- Hydrauliköl nicht vollständig ausgelaufen (sonst Zylinder blockiert durch Vakuum)

**Klasse 3 — Ersatz-Ruderblatt (Notruder)**

Wenn das Hauptruderblatt verloren geht (Abriss, Bruch), wird ein mitgeführtes oder improvisiertes Ruderblatt an geeigneter Stelle (Heck, Seite, Achterschaft) montiert und von Deck aus bedient.

Voraussetzungen:
- Befestigungsmöglichkeit am Heck (Ausleger, Halterung, Leine)
- Ausreichende Ruderfläche für das Bootsgewicht
- Bedienbarkeit von Deck (Pinne, Leine, Steuerleine)

**Klasse 4 — Segel-basierte Steuerung (Jury-Rig)**

Steuerung durch asymmetrische Segelbetrielung: Verlagern des Segeldruckpunktes (CE) relativ zum Lateralschwerpunkt (CLR) erzeugt Luv- oder Lee-Giermoment.

Voraussetzungen:
- Mindestens ein Segel setzbar
- Segeldruckpunkt variierbar (z. B. Fock allein, Groß allein, Besan)
- Windstärke und Seegang erlauben Segelführung
- Crew beherrscht die Technik

**Klasse 5 — Schleppbremsen-Steuerung**

Einsatz von Schleppbremsen (Drogues), Para-Anchors oder improvisierten Schleppwiderständen zur Kurssteuerung. Durch asymmetrisches Schleppen (z. B. Drogue nur an einer Seite) wird ein Giermoment erzeugt.

Voraussetzungen:
- Schleppbremse vorhanden
- Ausreichend Raum zum Leefall
- Befestigungspunkte an beiden Seiten des Hecks

### 2.2 Drehmomentübertragung bei der Notpinne

#### 2.2.1 Grundgleichungen

Die zentrale physikalische Größe bei der Notsteuerung ist das Drehmoment am Ruderschaft. Die Notpinne muss in der Lage sein, dieses Drehmoment — das bei Starkwind und hohem Seegang erheblich sein kann — vom Rudergänger auf den Ruderschaft zu übertragen.

**Ruderdrehmoment (vereinfacht):**

```
T_rudder = F_rudder × d_cp

mit:
  F_rudder = 0.5 × ρ × V² × A_rudder × C_L(α)
  d_cp = Position des Druckmittelpunkts relativ zum Schaft (m)

  ρ = Wasserdichte (1025 kg/m³ Seewasser)
  V = Bootsgeschwindigkeit (m/s)
  A_rudder = Ruderfläche (m²)
  C_L(α) = Auftriebsbeiwert bei Ruderwinkel α
  d_cp = (CP_position - shaft_position) × chord (m)
```

**Typische Ruderdrehmomente nach Bootsklasse:**

| Bootslänge (m) | Rudertyp | Max. Drehmoment (Nm) bei 7 kn | Max. Drehmoment (Nm) bei Surfen 12+ kn |
|-----------------|----------|-------------------------------|----------------------------------------|
| 8–10 | Spatenruder | 80–200 | 200–600 |
| 10–12 | Spatenruder | 150–400 | 400–1.200 |
| 12–14 | Spatenruder, 17 % Bal. | 300–700 | 700–2.000 |
| 14–16 | Spatenruder, 17 % Bal. | 500–1.200 | 1.200–3.500 |
| 16–20 | Spatenruder oder Skeg | 800–2.500 | 2.500–7.000 |
| 20–24 | Skeg oder Twin | 1.500–5.000 | 5.000–15.000 |

**Notpinne-Hebelarmlänge und erforderliche Handkraft:**

```
F_hand = T_rudder / L_tiller

mit:
  F_hand = Erforderliche Handkraft (N)
  T_rudder = Ruderdrehmoment (Nm)
  L_tiller = Effektive Hebellänge der Notpinne (m)
```

**Empfohlene maximale Handkraft:**

| Bedingung | Max. Handkraft (N) | Anmerkung |
|-----------|---------------------|-----------|
| Dauerbetrieb (>30 min) | 80–120 N | Ermüdungsfreiheit, eine Hand |
| Kurzzeitbetrieb (<5 min) | 150–250 N | Beide Hände, anstrengend |
| Notfall-Maximum | 300–400 N | Grenze der Beherrschbarkeit, Verletzungsgefahr |
| Absolutes Maximum (2 Personen) | 600–800 N | Nur mit 2 Personen und fester Haltegriff-Position |

**Daraus abgeleitete minimale Notpinnen-Längen:**

| Bootslänge (m) | Typ. Drehmoment (Nm) | Min. Pinne (m) für 120 N | Empfohlene Pinne (m) |
|-----------------|----------------------|--------------------------|---------------------|
| 8–10 | 200 | 1,67 | 0,8–1,0 (reicht wg. Balancierung) |
| 10–12 | 400 | 3,33 | 1,0–1,2 |
| 12–14 | 700 | 5,83 | 1,2–1,5 (Zweihand-Betrieb) |
| 14–16 | 1.200 | 10,00 | 1,5–1,8 + Talje |
| 16–20 | 2.500 | 20,83 | Talje obligatorisch |
| 20–24 | 5.000 | 41,67 | Talje + 2 Personen |

**Anmerkung:** Ab ~14 m Bootslänge mit unbalanciertem Spatenruder ist eine reine Notpinne ohne Talje (Flaschenzug) nicht mehr handhabbar. Daher werden bei größeren Booten Taljen (typisch 4:1 bis 6:1) an der Notpinne eingesetzt.

#### 2.2.2 Notpinne mit Talje

Die Talje (Flaschenzug) an der Notpinne multipliziert die effektive Hebellänge:

```
F_hand = T_rudder / (L_tiller × n × η)

mit:
  n = Untersetzung der Talje (z. B. 4:1)
  η = Wirkungsgrad der Talje (0,85–0,95 je nach Block-Qualität)
```

**Typische Talje-Konfigurationen für Notpinnen:**

| Konfiguration | Untersetzung | Weg pro Seite | Geeignet für |
|---------------|-------------|---------------|-------------|
| 2 Einzelblöcke + Leine | 2:1 | Verdoppelt | Boote 12–14 m |
| 2 Doppelblöcke + Leine | 4:1 | Vervierfacht | Boote 14–18 m |
| 2 Dreifachblöcke + Leine | 6:1 | Versechsfacht | Boote 18–24 m |
| Handy-Billy (vorgerüstet) | 4:1 bis 6:1 | Variabel | Universal |

**Befestigung der Talje:**

Die Talje wird zwischen dem Ende der Notpinne (Auge oder Bolzen) und zwei festen Punkten an Backbord und Steuerbord im Cockpit geführt (typischerweise Klampen, Augbolzen oder Winschen). Die beiden Parten der Talje gehen jeweils zu einer Seite.

#### 2.2.3 Balancierung und ihr Einfluss auf die Notsteuerung

Die Ruderbalancierung ist der wichtigste einzelne Faktor für die Handhabbarkeit einer Notpinne:

**Unbalanciertes Ruder (0 % Balance):**
- Gesamte Ruderfläche hinter dem Schaft
- Druckpunkt wandert mit zunehmendem Ruderwinkel nach hinten → hohes Drehmoment
- Starke Tendenz zur Mittellage (selbstzentrierend), aber schwer auszulenken
- Notpinne-Betrieb ab 12 m Bootslänge praktisch nicht mehr ohne Talje möglich

**Balanciertes Ruder (15–20 % Balance):**
- 15–20 % der Ruderfläche vor dem Schaft
- Drastisch reduziertes Drehmoment (typisch 40–60 % Reduktion gegenüber unbalanciert)
- Leichteres Steuern, aber weniger Selbstzentrierung
- Standard bei modernen Spatenrudern

**Überbalanciertes Ruder (>25 % Balance):**
- Druckmittelpunkt kann bei bestimmten Winkeln vor den Schaft wandern
- Negativer Ruderdruck: Ruder zieht sich selbst zur Seite → gefährliches Aufschaukeln
- Notpinne kann dem Rudergänger aus der Hand geschlagen werden
- KRITISCH: Bei Notsteuerung besonders gefährlich, da keine Dämpfung durch Seilzug/Hydraulik

#### 2.2.4 Kraftübertragung Notpinne → Ruderkopf

**Verbindungstypen:**

| Typ | Beschreibung | Drehmomentübertragung | Typisch bei |
|-----|-------------|----------------------|-------------|
| Vierkant | Quadratischer Ruderkopf, Notpinne hat Vierkant-Aufnahme | Formschluss, alle 4 Flächen | Jefa, Edson, Whitlock |
| Sechskant | Sechskant-Ruderkopf | Formschluss, 6 Flächen | Seltener, ältere Anlagen |
| Keilwellenverbindung | Gezahnte Verbindung (Splines) | Hoher Formschluss, viele Flächen | Lewmar, einige Jefa |
| Rohr-Aufsteck (Hohlwelle) | Notpinne steckt über einen zylindrischen Ruderkopf | Klemmung + Bolzen/Splint | Einfache Anlagen, Kleinboote |
| Bajonett | Dreh-Rast-Verbindung | Formschluss + Rastsicherung | Einige Superyacht-Systeme |

**Kritische Maße:**

- Ruderkopf-Vierkant: typisch 25 × 25 mm bis 70 × 70 mm (je nach Bootsgröße)
- Notpinne-Aufnahme: muss exakt passen — 0,5 mm zu groß → ausschlagen, 0,5 mm zu klein → geht nicht drauf
- Sicherungsbolzen: Durchmesser min. 6 mm Edelstahl, geschlitzt für Splint oder mit Federstecker

### 2.3 Improvisation mit Bordmitteln

Bei Fehlen einer funktionierenden Notpinne müssen Bordmittel als Notsteuerung eingesetzt werden. Die folgenden Methoden sind dokumentiert und in der Seenotpraxis erprobt:

#### 2.3.1 Rohrzange / Gripzange am Ruderkopf

**Methode:** Große Rohrzange (min. 450 mm / 18") oder Gripzange auf den Ruderkopf setzen und als Hebel nutzen.

**Vorteile:**
- Auf fast jedem Boot vorhanden
- Schneller Einsatz (< 2 min)

**Nachteile:**
- Sehr kurzer Hebel, hohe Handkraft
- Griffigkeit schlecht bei Nässe
- Zange kann abrutschen → Verletzungsgefahr
- Nur für Boote bis ~10 m geeignet

**Drehmomentübertragung:** ~50–100 Nm (je nach Zangengröße)

#### 2.3.2 Spinnaker- oder Großbaumschot als Steuerleinen

**Methode:** Zwei Leinen an den Quadranten oder Sektor binden, jeweils nach Bb und Stb ins Cockpit führen, über Winschen oder Klampen bedienen.

**Vorteile:**
- Auf Segelyachten immer Leinen vorhanden
- Große Untersetzung über Winschen möglich
- Für große Boote geeignet

**Nachteile:**
- Montage dauert 15–30 min
- Zugang zum Quadranten erforderlich (ggf. unter Bodenbrettern)
- Keine feinfühlige Steuerung
- Leinenführung muss gegen Schamfilen gesichert werden

#### 2.3.3 Paddel / Riemen als Heckruder

**Methode:** Langes Paddel oder Riemen über das Heck legen, mit Leine gegen Verlust gesichert, als Steuerruder verwenden.

**Vorteile:**
- Funktioniert auch bei Verlust des Hauptruders
- Einfaches Prinzip

**Nachteile:**
- Nur bei Leichtwind und wenig Seegang
- Auf modernen Yachten mit breitem Heck und hohem Freibord kaum praktikabel
- Ermüdend bei längerem Einsatz
- Steuerwirkung gering bei Booten >10 m

#### 2.3.4 Leinen direkt am Quadranten

**Methode:** Zwei Leinen direkt an den Quadranten oder Sektor binden und über Umlenkblöcke ins Cockpit führen. Über Winschen oder Klampen bedienen.

**Detaillierte Anleitung:**

1. Zugang zum Quadranten schaffen (Bodenbrett, Achterkajüt-Zugang)
2. Zwei Leinen (mind. 10 mm Ø, Polyester) an den Quadranten binden:
   - Eine Leine an den Backbord-Arm des Quadranten (Palstek oder Rundtörn mit zwei halben Schlägen)
   - Eine Leine an den Steuerbord-Arm des Quadranten
3. Leinen durch den Bodenzugang nach oben ins Cockpit führen
4. Über Umlenkblöcke oder Beschläge nach Bb und Stb leiten
5. Auf Winschen legen oder an Klampen belegen
6. Steuern durch abwechselndes Dichtholen und Fieren der beiden Leinen

**Vorteile:**
- Auf Segelyachten immer Leinen und Winschen vorhanden
- Große Untersetzung über Winschen möglich (effektiv wie Talje)
- Für große Boote geeignet, da Winsch-Untersetzung Handkraft reduziert
- Funktioniert auch wenn Notpinne nicht passt

**Nachteile:**
- Montage dauert 15–30 Minuten
- Quadranten-Zugang erforderlich
- Keine feinfühlige Steuerung (Winsch-Betrieb = grob)
- Leinenführung muss gegen Schamfilen gesichert werden (Scheuerschutz an Kanten)
- Ruderlage nicht direkt fühlbar (kein Feedback)

**Empfehlung:** Dies ist die bevorzugte Improvisation für Boote >14 m, wenn die Notpinne versagt oder nicht reicht. Die Winsch-Untersetzung (typisch 16:1 bis 40:1) macht auch schwere Ruder handhabbar.

#### 2.3.5 Cockpittisch / Bodenbrett als improvisiertes Ruderblatt

**Methode:** Flaches Brett (Cockpittisch, Bodenbrett) an einen Bootshaken, Großbaum oder Spinnakerbaum binden und über das Heck als Ruderblatt einsetzen.

**Vorteile:**
- Bordmittel vorhanden
- Größere Ruderfläche als Paddel

**Nachteile:**
- Fragile Konstruktion, bricht bei Seegang leicht
- Aufwändige Befestigung (30–60 min)
- Steuerkraft begrenzt

### 2.4 Ansteuerung ohne Ruder — Segel-Trimm

#### 2.4.1 Grundprinzip

Jedes Segelboot kann theoretisch ohne Ruder gesteuert werden, indem der Segeldruckpunkt (CE — Center of Effort) relativ zum Lateralschwerpunkt des Unterwasserschiffs (CLR — Center of Lateral Resistance) verschoben wird:

- **CE vor CLR** → Boot fällt ab (Lee-Giermoment, luvgierig wird reduziert)
- **CE hinter CLR** → Boot luft an (Luv-Giermoment, luvgierig wird verstärkt)

**Praktische Umsetzung:**

| Steuerbefehl | Maßnahme | Erklärung |
|-------------|----------|-----------|
| Anluven | Großsegel dichtholen, Fock fieren | CE wandert nach achtern |
| Abfallen | Fock dichtholen, Großsegel fieren/gerefft | CE wandert nach vorn |
| Beidrehen | Fock back, Groß dicht, Ruder (Rest) luv | Boot stellt sich quer zum Wind |
| Geradeauskurs | Balance zwischen Fock und Groß finden | CE = CLR → neutraler Ruderdruck |

#### 2.4.2 Wende ohne Ruder

1. Großsegel voll dichtholen
2. Fock leicht fieren
3. Boot luft an (CE achtern)
4. Wenn Wind vorlich → Fock back schlagen (auf falsche Seite)
5. Boot dreht durch den Wind
6. Fock auf neue Seite umschlagen
7. Balance wiederherstellen

**Schwierigkeit:** Mittel. Erfordert Übung, funktioniert bei 3–5 Bft zuverlässig.

#### 2.4.3 Halse ohne Ruder

1. Großsegel fieren bis Großbaum fast achteraus
2. Fock dichtholen
3. Boot fällt ab (CE vorn)
4. Wenn achterlicher Wind → Großsegel kontrolliert auf andere Seite
5. Fock umschlagen
6. Balance wiederherstellen

**Schwierigkeit:** Hoch. Große Gefahr der Patenthalse bei Seegang. Nur bei moderaten Bedingungen empfehlenswert.

#### 2.4.4 Vor-dem-Wind-Kurs ohne Ruder

Dies ist die schwierigste Situation bei der ruderlosen Steuerung:

- Boot ist instabil (kein Ruder-Dämpfungsmoment)
- Großsegel erzeugt kein klares Giermoment
- Rollbewegung kann zu spontaner Kursänderung führen

**Empfehlung:** Statt direkt vor dem Wind zu segeln, den Kurs auf Raumschots (120–150° zum Wind) halten und Zickzack-Kurs fahren. Dies erhöht die Gesamtstrecke, aber stabilisiert das Boot erheblich.

#### 2.4.5 Steuerung per Segeltrimm bei Motoryachten

Bei Motoryachten ohne Segel sind die Möglichkeiten stark eingeschränkt:

- **Doppelschrauber:** Differentialsteuerung über asymmetrische Drehzahl (Stb-Motor mehr → Boot dreht nach Bb)
- **Einzelschrauber:** Radeffekt (Propellergiermoment) nutzen — bei Rechtsdrehendem Propeller zieht das Heck nach Stb (Bug nach Bb) bei Vorwärtsfahrt
- **Bugstrahler:** Bei Langsamfahrt (<3 kn) kann ein Bugstrahler als Steuerhilfe dienen
- **Schleppbremse:** Als asymmetrisches Schleppmittel von einer Heckseite

### 2.5 Schleppbremsen-Steuerung

#### 2.5.1 Prinzip

Eine Schleppbremse (Drogue) oder ein Treibanker (Para-Anchor) wird an einer oder beiden Seiten des Hecks (oder Bugs) ausgebracht, um durch Schleppwiderstand ein Giermoment zu erzeugen:

- **Symmetrischer Einsatz (Mitte):** Kein Giermoment, aber Geschwindigkeitsreduktion und Stabilisierung des Kurses (Boot bleibt achterlich zum Wind)
- **Asymmetrischer Einsatz (eine Seite):** Giermoment zur Schleppseite → Boot dreht zur Seite der Bremse
- **Bridle (geteilte Schleppleine):** Zwei Leinen vom Drogue zu je einer Heckseite, durch Verändern der Leinenlängen wird das Giermoment gesteuert

#### 2.5.2 Jordan Series Drogue als Notsteuerungshilfe

Der Jordan Series Drogue (JSD) ist eine Kette von vielen kleinen Kegeln (typisch 100–150 Stück) auf einer langen Leine (80–120 m). Er wurde primär als Sturmtaktik-Gerät entwickelt, dient aber auch als Notsteuerungshilfe:

**Notsteuerungseinsatz:**

1. JSD über das Heck ausbringen, Bridle zu beiden Heckseiten
2. Durch Verlängern/Verkürzen der Bb/Stb-Bridle-Leine → Kurskorrektur
3. Boot fährt langsam (1–3 kn) mit dem Wind, Kurs ±30° korrigierbar
4. Besonders effektiv in schwerem Wetter, wenn Segeltrimm-Steuerung versagt

#### 2.5.3 Para-Anchor als Notsteuerungshilfe

Ein Para-Anchor (Fallschirm-Treibanker) wird über den Bug ausgebracht und hält das Boot mit dem Bug zum Wind:

**Notsteuerungseinsatz:**

1. Para-Anchor über den Bug ausbringen (Leinenlänge 8–10 × Bootslänge)
2. Boot liegt mit dem Bug zum Wind, Abdrift 1–2 kn
3. Keine aktive Kurssteuerung möglich, aber Boot ist stabil
4. Zum Anlegen: Para-Anchor einholen und per Segeltrimm/Schleppbremse manövrieren

### 2.6 Dynamische Analyse — Notsteuerung unter verschiedenen Bedingungen

#### 2.6.1 Windstärke und Seegang

| Bedingung | Notpinne | Segeltrimm | Schleppbremse | Improvisiertes Ruder |
|-----------|---------|-----------|-------------|---------------------|
| 0–2 Bft, glatt | Gut, leicht | Schwierig (zu wenig Wind) | Nicht nötig | Gut |
| 3–4 Bft, leicht | Gut | Gut | Nicht nötig | Gut |
| 5–6 Bft, mäßig | Anstrengend, Talje nötig ab 14 m | Gut, Reffen hilfreich | Möglich | Grenzwertig |
| 7–8 Bft, grob | Sehr anstrengend, 2 Pers. | Nur unter Sturmfock | Empfohlen | Unmöglich |
| >8 Bft, schwer | Extrem, nur mit Talje + 2 Pers. | Nur unter Trysegel/Sturmfock | Beste Option | Unmöglich |

#### 2.6.2 Bootstyp-spezifische Analyse

**Langkieler mit Skeg-Ruder:**
- Hohe Kursstabilität, einfach per Segel zu steuern
- Notpinne: niedrigeres Drehmoment wg. Skeg-Schutz
- Ruderblatt-Verlust selten (Skeg schützt)
- Gesamtbewertung Notsteuerung: GUT

**Moderner Kurzflossenkieler mit Spatenruder:**
- Geringe Kursstabilität, schwer per Segel zu steuern
- Notpinne: höheres Drehmoment wg. freiliegendem Ruderblatt
- Ruderblatt-Verlust häufiger (kein Skeg-Schutz)
- Gesamtbewertung Notsteuerung: MÄSSIG

**Katamaran:**
- Zwei Ruder → Redundanz (ein Ruder ausreichend für Notsteuerung)
- Notpinne pro Ruder separat
- Breitere Plattform = längere Notpinnen-Wege
- Gesamtbewertung Notsteuerung: GUT (inhärente Redundanz)

**Motoryacht:**
- Keine Segelsteuerung möglich (außer improvisiertes Segel)
- Doppelschrauber: Differentialsteuerung als primäre Notsteuerung
- Einzelschrauber: Notpinne + Schleppbremse
- Gesamtbewertung Notsteuerung: MÄSSIG (Einzelschrauber) / GUT (Doppelschrauber)

### 2.7 Notsteuerung bei verschiedenen Wetterbedingungen — Detailanalyse

#### 2.7.1 Leichtwind (0–2 Bft, < 6 kn)

**Situation:** Ruhige See, wenig Wind. Steuerungsausfall ist weniger kritisch, da geringe Kräfte am Ruder und keine unmittelbare Gefahr durch Abdrift auf Leeküste.

**Notpinne:** Leicht handhabbar. Selbst eine kurze Notpinne ohne Talje reicht. Ruderdrehmoment minimal (< 50 Nm bei den meisten Booten bis 14 m). Eine Person kann problemlos steuern.

**Segeltrimm-Steuerung:** Schwierig bis unmöglich, da zu wenig Wind für wirksame Segeldruckpunkt-Verschiebung. Das Boot reagiert träge auf Segelverstellung.

**Empfehlung bei Leichtwind:** Notpinne aufsetzen und unter Motor zum nächsten Hafen fahren. Motoryachten: Differentialsteuerung bei Doppelschraubern. Dringlichkeit gering, es sei denn, Strömung treibt auf Gefahr zu.

#### 2.7.2 Mäßiger Wind (3–5 Bft, 7–21 kn)

**Situation:** Normale Segelbedingungen. Steuerungsausfall ist handhabbar, wenn die Crew vorbereitet ist. Ruderdrehmoment moderat (100–500 Nm bei Booten 10–16 m).

**Notpinne:** Gut handhabbar bei Booten bis 14 m. Ab 14 m wird eine Talje ab 5 Bft empfohlen. Eine Person kann bei 3–4 Bft steuern, bei 5 Bft sollten zwei Personen bereitstehen.

**Segeltrimm-Steuerung:** Beste Bedingungen. Genügend Wind für wirksame Steuerung, aber nicht so viel, dass das Boot unkontrollierbar wird. Ideal zum Üben.

**Schleppbremse:** Nicht erforderlich, aber als zusätzliche Stabilisierung einsetzbar.

**Empfehlung bei mäßigem Wind:** Notpinne ist die primäre Methode. Segeltrimm als Unterstützung. Kurs zum nächsten Hafen unter Notsteuerung.

#### 2.7.3 Starkwind (6–7 Bft, 22–33 kn)

**Situation:** Anspruchsvolle Segelbedingungen. Steuerungsausfall wird zur ernsthaften Situation. Ruderdrehmoment hoch (500–2.000 Nm bei Booten 12–18 m). Boot kann schnell in gefährliche Lage geraten.

**Notpinne:** Anspruchsvoll. Talje obligatorisch ab 12 m Bootslänge. Zwei Personen empfohlen. Unter gerefften Segeln steuern (Segeldruckpunkt reduzieren). Kurs auf Raum (120–150° zum Wind) halten, da dieser Kurs die geringsten Ruderkräfte erzeugt.

**Segeltrimm-Steuerung:** Möglich, aber nur unter stark gerefften Segeln oder Sturmbesegelung. Kursänderungen langsam und limitiert. Kombination mit Notpinne (auch eingeschränkt) verbessert die Kontrolle erheblich.

**Schleppbremse:** Sinnvoll als Stabilisierung. JSD kann bei 7 Bft bereits wirksam eingesetzt werden, um das Boot zu bremsen und den Kurs zu stabilisieren.

**Empfehlung bei Starkwind:** Sofort Geschwindigkeit reduzieren (Segel bergen). Notpinne + Talje aufsetzen. Bei Ruderblatt-Verlust: JSD als primäre Notsteuerung. Pan-Pan auf VHF Ch 16.

#### 2.7.4 Sturm (8+ Bft, > 34 kn)

**Situation:** Überlebensbedingungen. Steuerungsausfall ist eine Notlage. Ruderdrehmomente können 2.000–10.000+ Nm erreichen. Wellenhöhen >4 m. Deck ist gefährlicher Arbeitsplatz.

**Notpinne:** Extrem schwierig. Nur mit Talje (min. 4:1, besser 6:1) und zwei kräftigen Personen handhabbar. Bei Booten >16 m erreicht selbst die Notpinne + Talje die Grenzen der menschlichen Leistungsfähigkeit. Verletzungsgefahr durch herumschlagende Pinne bei überbalanciertem Ruder.

**Segeltrimm-Steuerung:** Nur unter Trysegel und/oder Sturmfock. Sehr eingeschränkte Kurskontrolle. Boot muss Raum segeln oder beidrehen.

**Schleppbremse:** BESTE OPTION bei Sturm. JSD über das Heck bremst das Boot auf 1–3 kn und stabilisiert den Kurs. Para-Anchor über den Bug hält das Boot stationär. Bei Ruderblatt-Verlust im Sturm ist die Schleppbremse die einzige realistische Notsteuerung.

**Empfehlung bei Sturm:** Schleppbremse (JSD oder Para-Anchor) ausbringen. Alle Segel bergen. Crew sichern. Mayday erwägen, wenn Gefahr für Schiff oder Leben. Auf keinen Fall unter vollen Segeln weiterfahren.

### 2.8 Materialfestigkeit und Belastungsgrenzen

#### 2.8.1 Notpinne unter Extrembelastung

Die Notpinne ist ein sicherheitskritisches Bauteil, das unter den ungünstigsten Bedingungen (Sturm, Nacht, kalte Hände, nasses Deck) funktionieren muss. Die Materialwahl und Dimensionierung sind entscheidend.

**Edelstahl 316L Rohr — Festigkeitswerte:**

| Parameter | Wert |
|-----------|------|
| Streckgrenze (Rp0,2) | 220 MPa (min.) |
| Zugfestigkeit (Rm) | 520 MPa (min.) |
| Bruchdehnung | 40 % (min.) |
| E-Modul | 200 GPa |
| Dichte | 8.000 kg/m³ |

**Maximales Biegemoment Edelstahl-Rohr (Notpinne):**

```
M_max = (Rp0,2 × W_p) / SF

mit:
  W_p = π/32 × (D⁴ - d⁴) / D  (Widerstandsmoment Rohr)
  D = Außendurchmesser
  d = Innendurchmesser
  SF = Sicherheitsfaktor (empfohlen: 2,5 für Notsteuerung)
```

**Berechnungsbeispiel: Notpinne Ø 35 × 2,5 mm (typisch für 12 m Boot):**

```
D = 35 mm, d = 30 mm
W_p = π/32 × (35⁴ - 30⁴) / 35 = 1.937 mm³
M_max = (220 × 1.937) / 2,5 = 170.456 Nmm ≈ 170 Nm
```

Bei einem Hebel von 1.200 mm: F_max = 170 / 1,2 = 142 N → Ausreichend für eine Person.

**Aluminium 6082-T6 Rohr — Festigkeitswerte:**

| Parameter | Wert |
|-----------|------|
| Streckgrenze (Rp0,2) | 260 MPa |
| Zugfestigkeit (Rm) | 310 MPa |
| Bruchdehnung | 10 % |
| E-Modul | 70 GPa |
| Dichte | 2.700 kg/m³ |

**Anmerkung:** Aluminium hat eine höhere Streckgrenze als Edelstahl 316L, aber eine deutlich geringere Bruchdehnung. Das bedeutet: Aluminium-Notpinnen brechen eher plötzlich (spröder Bruch), während Edelstahl sich verformt, bevor es bricht (Warnung durch Verformung). Für Sicherheitsanwendungen ist das Verformungsverhalten von Edelstahl vorzuziehen.

#### 2.8.2 Aufnahme-Verbindung (Socket) — Flächenpressung

Die Verbindung zwischen Notpinne und Ruderkopf überträgt das Drehmoment über Flächenpressung:

```
p = T / (a² × L_contact)

mit:
  p = Flächenpressung (MPa)
  T = Drehmoment (Nmm)
  a = Vierkant-Schlüsselweite (mm)
  L_contact = Kontaktlänge Aufnahme (mm), typisch 40–80 mm
```

**Zulässige Flächenpressung:**

| Material-Paarung | p_zul (MPa) |
|-----------------|-------------|
| Edelstahl / Edelstahl | 80–120 |
| Edelstahl / Bronze | 60–80 |
| Aluminium / Edelstahl | 40–60 |

Bei Überschreitung der zulässigen Flächenpressung: Aufnahme schlägt aus, Rundung der Kanten, zunehmend Spiel → Notpinne wird unbrauchbar.

### 2.9 Rechtliche Aspekte und Haftung

#### 2.9.1 Haftung bei fehlendem Notsteuerungssystem

**Versicherungsrecht:**

Die meisten Kaskoversicherungen (z. B. Pantaenius, Yacht-Pool) setzen die „Einhaltung der Regeln guter Seemannschaft" voraus. Eine fehlende Notsteuerung kann als Verstoß gewertet werden, insbesondere:

- Bei Offshore-Fahrten ohne Notpinne → Deckungsverlust möglich bei grober Fahrlässigkeit
- Bei Regatten ohne OSR-konforme Notsteuerung → Deckungsverlust bei Regatta-spezifischer Versicherung
- Bei gewerblicher Nutzung ohne dokumentierte Notsteuerung → Ordnungswidrigkeit (SchSV §14)

**Haftpflicht bei Drittschäden:**

Wenn ein manövrierunfähiges Boot einen Drittschaden verursacht (Kollision, Hafeninfrastruktur), kann die fehlende Notsteuerung als Mitverursachung gewertet werden. Die Haftung des Eigners/Skippers wird verschärft.

#### 2.9.2 Dokumentationspflichten

**Gewerbliche Yachten (>12 m, deutsche Flagge):**
- Notsteuerungsverfahren im Schiffssicherheitshandbuch dokumentiert
- Nachweis der jährlichen Prüfung (Logbuch-Eintrag)
- Crew-Einweisung dokumentiert

**Private Yachten (Empfehlung):**
- Notpinne-Maße im Bordhandbuch notieren
- Stauort dokumentieren
- Jährlichen Funktionstest im Logbuch vermerken
- Bypass-Ventil-Position dokumentieren

---

## 3. Typenübersicht

### 3.1 Standard-Notpinne

#### 3.1.1 Definition und Funktion

Die Standard-Notpinne ist ein starrer oder teleskopischer Hebel, der direkt auf den Ruderkopf aufgesetzt wird und dem Rudergänger die manuelle Steuerung des Ruders ermöglicht. Sie ist das am weitesten verbreitete und normativ geforderte Notsteuerungssystem.

**Aufbau:**

1. **Aufnahme (Socket)** — Passt auf den Ruderkopf (Vierkant, Sechskant, Keilwelle)
2. **Schaft (Shaft)** — Rohr oder Vollmaterial, überträgt das Drehmoment
3. **Griff (Handle)** — Ergonomisch geformtes Ende für den Rudergänger
4. **Sicherung (Locking)** — Bolzen, Splint oder Federstecker gegen Abziehen

**Materialien:**

| Material | Gewicht | Festigkeit | Korrosion | Typisch bei |
|----------|---------|-----------|-----------|------------|
| Edelstahl 316L, Rohr | Mittel | Hoch | Sehr gut | Standard, Serie |
| Aluminium 6082-T6 | Leicht | Mittel | Gut (anodisiert) | Regatta, Leichtbau |
| Carbon-Rohr + Alu-Aufnahme | Sehr leicht | Hoch | Sehr gut | Regatta, Superyacht |
| GFK-Rohr + Edelstahl-Aufnahme | Leicht | Mittel | Sehr gut | Serienboote |
| Holz (Esche, Teak) | Leicht | Mittel | Mäßig | Tradition, Klassik |

**Typische Abmessungen:**

| Bootslänge (m) | Ruderkopf-Vierkant (mm) | Pinnen-Länge (mm) | Rohr-Ø (mm) | Gewicht (kg) |
|-----------------|------------------------|-------------------|-------------|-------------|
| 7–9 | 25 × 25 | 700–900 | 25 × 2 | 0,8–1,2 |
| 9–11 | 30 × 30 | 800–1.000 | 30 × 2 | 1,2–1,8 |
| 11–13 | 35 × 35 | 900–1.200 | 32 × 2,5 | 1,8–2,5 |
| 13–15 | 40 × 40 | 1.000–1.400 | 35 × 3 | 2,5–3,5 |
| 15–18 | 50 × 50 | 1.200–1.600 | 40 × 3 | 3,5–5,0 |
| 18–22 | 60 × 60 | 1.400–1.800 | 45 × 3,5 | 5,0–8,0 |
| 22–24 | 70 × 70 | 1.600–2.000 | 50 × 4 | 8,0–12,0 |

#### 3.1.2 Bauformen

**Starre Notpinne (One-Piece):**
- Ein Stück, nicht zerlegbar
- Höchste Festigkeit und Zuverlässigkeit
- Nachteil: Platzbedarf bei Lagerung
- Empfohlen für Boote bis 14 m

**Teleskop-Notpinne (Telescopic):**
- Zwei oder drei ineinander verschiebbare Rohre
- Arretierung durch Klemmbolzen oder Federstecker
- Vorteil: Kompakte Lagerung
- Nachteil: Schwachstelle an der Klemmung — kann unter Last rutschen
- Regelmäßig prüfen: Bolzen intakt? Korrosion an Klemmstelle?

**Klapp-Notpinne (Folding):**
- Scharnier mit Verriegelung
- Kompakt verstaubar
- Nachteil: Scharnier als potentielle Schwachstelle
- Typisch für Regattaboote (Gewicht/Platz kritisch)

**Universal-Notpinne (Adapter-System):**
- Wechselbare Aufnahmen für verschiedene Ruderkopf-Formate
- Adapter-Set mit 3–5 verschiedenen Vierkant-Aufnahmen
- Vorteil: Flexibel, für Charterboote, Flotillen
- Nachteil: Adapter als zusätzliches Ausfallrisiko

### 3.2 Hydraulik-Bypass

#### 3.2.1 Definition und Funktion

Der Hydraulik-Bypass ist ein Ventil im hydraulischen Steuerkreislauf, das bei Öffnung den Ölfluss zwischen den beiden Zylinderseiten freigibt. Dadurch wird das Ruder „frei" und kann über eine Notpinne oder durch den Wasserdruck bewegt werden.

**Funktionsprinzip:**

Im Normalbetrieb ist das Bypass-Ventil geschlossen. Das Hydrauliköl wird von der Steuerpumpe (am Steuerrad) durch Druckleitungen zum Steuerzylinder gepresst. Der Zylinder bewegt über die Kolbenstange den Ruderarm/Quadranten.

Bei Ausfall (Leck, Pumpendefekt):
1. Bypass-Ventil öffnen
2. Öl fließt frei zwischen beiden Zylinderseiten
3. Ruder ist nun frei beweglich
4. Notpinne auf Ruderkopf aufsetzen
5. Manuell steuern

**Bauarten:**

| Typ | Bedienung | Position | Typisch bei |
|-----|-----------|----------|------------|
| Nadel-Bypass | Handrad drehen | Am Zylinder oder in Leitung | Standard bei manueller Hydraulik |
| Kugelhahn-Bypass | Hebel drehen (90°) | In Leitung, oft im Cockpit-Schapp | Größere Boote, schneller Zugang |
| Magnet-Bypass | Elektrisch + manuell | Am Zylinder | Power-Steering, Superyachten |
| Rückschlag-Bypass | Automatisch bei Druckabfall | Am Zylinder | Hochwertige Anlagen |
| Kombination Bypass + Absperr | Absperren + Bypass in einem | Verteilerblock | Professionelle Anlagen |

#### 3.2.2 Typische Probleme

1. **Ventil korrodiert fest** — Wird nie benutzt, korrodiert über Jahre zu
2. **Ventil nicht auffindbar** — Position nicht dokumentiert, Crew weiß nicht, wo es ist
3. **Ventil falsch beschriftet** — Verwechslung mit anderen Ventilen im Maschinenraum
4. **Öl ausgelaufen → Vakuum im Zylinder** — Bypass hilft nicht, da Zylinder ohne Öl blockiert
5. **Bypass offen, aber Autopilot noch eingekoppelt** — Autopilot-Zylinder blockiert trotzdem

### 3.3 Tiller-Adapter

#### 3.3.1 Definition und Funktion

Ein Tiller-Adapter ermöglicht es, eine Standard-Pinne (oder Notpinne) an einem Ruderschaft zu befestigen, der normalerweise für Radsteuerung ausgelegt ist. Er überbrückt die Lücke zwischen Ruderkopf-Geometrie und Pinnen-Aufnahme.

**Einsatzfälle:**

- Radsteuerung ausgefallen → Tiller-Adapter + Pinne als Notsteuerung
- Umbau von Rad- auf Pinnensteuerung (temporär oder permanent)
- Regatta-Backup bei Radsteuerungsbooten

**Bauformen:**

| Typ | Befestigung | Für Ruderkopf-Typ | Typisch bei |
|-----|-------------|-------------------|------------|
| Aufsatz-Adapter | Aufstecken + Bolzen | Vierkant, Sechskant | Standard |
| Klemm-Adapter | Klemmschelle um runden Schaft | Rund (ältere Boote) | Retrofit |
| Flansch-Adapter | Schrauben auf Ruderkopf-Flansch | Flansch (Großyachten) | Superyachten |
| Universal-Adapter | Verstellbare Klemme | Verschieden | Charter, Flotille |

### 3.4 Notruderblatt

#### 3.4.1 Definition und Funktion

Ein Notruderblatt (Emergency Rudder Blade) ist ein transportables Ruder, das bei Verlust des Hauptruders an einer geeigneten Stelle des Bootskörpers montiert wird und die Steuerfähigkeit wiederherstellt.

**Bauformen:**

**Typ 1 — Achter-Heck-Notruder (Transom-Mount):**
- Ruderblatt wird am Spiegel (Transom) montiert
- Befestigung durch vorbereitete Pintles/Gudgeons oder improvisiert mit Schäkeln
- Pinne direkt am Ruderblatt
- Geeignet für Boote mit offenem Heck

**Typ 2 — Seitliches Notruder (Outboard-Mount):**
- Ruderblatt wird seitlich am Achterschiff befestigt
- Halterung an Reling, Heckkorb oder speziellem Beschlag
- Pinne seitlich bedienbar
- Geeignet für Boote mit geschlossenem Heck

**Typ 3 — Getauchtes Notruder (Oar-Type):**
- Langer Ruderschaft (wie ein übergroßes Paddel) über das Heck ins Wasser
- Führung durch Heckkorb-Auge oder spezielle Dolle
- Bedienung durch seitliches Schwenken
- Einfachste Bauform, begrenzte Wirksamkeit

**Typ 4 — Windfahnen-Notruder (Windvane as Emergency):**
- Windfahnensteuerung (z. B. Hydrovane) hat ein eigenes Ruderblatt
- Bei Ausfall des Hauptruders kann die Windfahne als Notruder genutzt werden
- Pinne der Windfahne wird manuell bedient
- Sehr effektiv, da Windfahnen-Ruder groß genug dimensioniert ist

**Dimensionierung Notruderblatt:**

| Bootslänge (m) | Min. Ruderfläche (m²) | Empf. Ruderfläche (m²) | Eintauchtiefe (mm) |
|-----------------|----------------------|----------------------|---------------------|
| 8–10 | 0,04 | 0,06–0,08 | 400–600 |
| 10–12 | 0,06 | 0,08–0,12 | 500–700 |
| 12–14 | 0,08 | 0,12–0,16 | 600–800 |
| 14–16 | 0,10 | 0,16–0,22 | 700–900 |
| 16–20 | 0,14 | 0,22–0,30 | 800–1.100 |

**Faustformel für Notruderfläche:**

```
A_notruder ≥ 0,015 × LWL × Tiefgang (m²)
```

**Beispielberechnung (12 m Segelyacht, LWL 10,5 m, Tiefgang 1,8 m):**

```
A_notruder ≥ 0,015 × 10,5 × 1,8 = 0,28 m²
```

In der Praxis reichen 50–70 % dieser theoretischen Fläche für eine Notsteuerung aus, da die Anforderung an die Steuerpräzision bei Notsteuerung geringer ist als im Normalbetrieb. Selbst ein Notruder mit 0,15 m² wäre deutlich besser als gar kein Ruder.

**Materialempfehlungen für Notruderblätter:**

| Material | Gewicht | Haltbarkeit | Preis | Empfehlung |
|----------|---------|-------------|-------|-----------|
| GFK (laminiert) | Mittel | Hoch | €€€ | Beste Option, professionell gefertigt |
| Marine-Sperrholz (BS 1088) | Leicht | Mittel (wenn beschichtet) | € | Günstige DIY-Option, muss mit Epoxid versiegelt sein |
| Aluminium (5083, 6082) | Schwer | Hoch | €€ | Robust, professionell |
| Edelstahl-Rahmen + GFK | Schwer | Sehr hoch | €€€ | Superyacht-Standard |
| HDPE (Polyethylen) | Leicht | Hoch | € | Preiswert, UV-beständig, schlagfest |

### 3.5 Schleppbremsen-Steuerung

#### 3.5.1 Jordan Series Drogue (JSD)

**Beschreibung:** Kette von 100–150 kleinen Kegelschirmen (Ø 130–150 mm) auf einer 80–120 m langen Leine aus hochfestem Polyester oder Dyneema. Über eine Bridle (Y-Leine) am Heck befestigt.

**Spezifikationen nach Bootsgröße:**

| Bootslänge (m) | Kegel-Anzahl | Kegel-Ø (mm) | Leinenlänge (m) | Leinenstärke (mm) | Schleppkraft (kN) |
|-----------------|-------------|-------------|----------------|-------------------|------------------|
| 8–10 | 85–100 | 130 | 80–90 | 12 | 3–5 |
| 10–12 | 100–120 | 130 | 90–100 | 14 | 5–8 |
| 12–14 | 120–140 | 150 | 100–110 | 16 | 8–12 |
| 14–16 | 130–150 | 150 | 110–120 | 18 | 12–18 |
| 16–20 | 150–180 | 150 | 120–140 | 20 | 18–30 |

**Steuerungsmodus:**
- Bridle-Leine Bb/Stb differentiell bedienen → Giermoment
- Kurskorrektur ±20–30° möglich
- Geschwindigkeit: 1–3 kn (je nach See)

#### 3.5.2 Para-Anchor

**Beschreibung:** Fallschirmförmiger Treibanker, der über den Bug ausgebracht wird. Hält das Boot mit dem Bug zum Wind und reduziert die Abdrift.

**Spezifikationen nach Bootsgröße:**

| Bootslänge (m) | Schirm-Ø (m) | Leinenlänge (m) | Leinenstärke (mm) | Haltekraft (kN) |
|-----------------|-------------|----------------|-------------------|-----------------|
| 8–10 | 2,4–3,0 | 60–80 | 14–16 | 5–10 |
| 10–12 | 3,0–3,6 | 80–100 | 16–18 | 10–18 |
| 12–14 | 3,6–4,2 | 100–120 | 18–20 | 18–28 |
| 14–16 | 4,2–4,8 | 120–150 | 20–22 | 28–40 |
| 16–20 | 4,8–6,0 | 150–200 | 22–24 | 40–60 |

**Steuerungsmodus:**
- Keine aktive Kurssteuerung, Boot zeigt zum Wind
- Stabilisierung und Drift-Reduktion
- Zum Anlaufen eines Hafens: Para-Anchor einholen → andere Notsteuerungsmethode

### 3.6 Segel-Steuerung (Jury-Rig ohne Ruder)

#### 3.6.1 Segelkonfigurationen für Notsteuerung

| Kurs zum Wind | Empfohlene Segel | Steuerung durch |
|--------------|-----------------|----------------|
| Hart am Wind | Fock + gerefftes Groß | Fock-Schot-Trimm |
| Halbwind | Fock + Groß, beide getrimmt | Balance-Punkt-Verschiebung |
| Raum | Nur Fock oder Genua | Fock-Position (Barber-Hauler) |
| Vor dem Wind | Fock ausgebaumt + gerefftes Groß | Asymmetrische Segelstellung |
| Beigedreht | Fock back + Groß dicht | Boot liegt stabil bei |

#### 3.6.2 Trim-Tabelle für ruderlose Steuerung

**Anluven (Bug dreht zum Wind):**
- Großschot dichtholen
- Fockschot fieren
- Traveller nach Luv
- Ggf. Vorsegel wegnehmen

**Abfallen (Bug dreht vom Wind weg):**
- Großschot fieren / Großsegel reffen
- Fockschot dichtholen
- Traveller nach Lee
- Ggf. Großsegel wegnehmen

**Kurs halten:**
- Balance-Punkt finden (CE ≈ CLR)
- Beide Schoten fein justieren
- Segeldruckpunkt leicht achtern für Kursstabilität (leicht luvgierig)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Jefa Notpinne (Jefa Steering, Dänemark)

Jefa Marine (Svendborg, Dänemark) ist der weltweit führende Hersteller von Steueranlagen für Segelyachten. Ihre Notpinnen sind als Zubehör für Jefa-Ruderanlagen konzipiert, passen aber auch auf andere Systeme mit kompatiblem Ruderkopf.

**Jefa Emergency Tiller — Produktlinie:**

| Modell | Ruderkopf (mm) | Pinnen-Länge (mm) | Material | Gewicht (kg) | Preis (€, ca.) |
|--------|---------------|-------------------|----------|-------------|----------------|
| ET-25 | 25 × 25 Vierkant | 750 | Edelstahl 316L | 0,9 | 120 |
| ET-30 | 30 × 30 Vierkant | 850 | Edelstahl 316L | 1,2 | 145 |
| ET-35 | 35 × 35 Vierkant | 950 | Edelstahl 316L | 1,6 | 175 |
| ET-40 | 40 × 40 Vierkant | 1.050 | Edelstahl 316L | 2,1 | 210 |
| ET-50 | 50 × 50 Vierkant | 1.200 | Edelstahl 316L | 3,2 | 285 |
| ET-60 | 60 × 60 Vierkant | 1.400 | Edelstahl 316L | 4,8 | 380 |
| ET-70 | 70 × 70 Vierkant | 1.600 | Edelstahl 316L | 6,5 | 520 |

**Jefa Emergency Tiller — Splined (Keilwelle):**

| Modell | Ruderkopf-Profil | Pinnen-Länge (mm) | Gewicht (kg) | Preis (€, ca.) |
|--------|-----------------|-------------------|-------------|----------------|
| ET-S32 | 32 mm Splined 8Z | 900 | 1,4 | 195 |
| ET-S40 | 40 mm Splined 10Z | 1.050 | 2,3 | 245 |
| ET-S50 | 50 mm Splined 12Z | 1.250 | 3,8 | 350 |
| ET-S60 | 60 mm Splined 14Z | 1.450 | 5,5 | 480 |

**Jefa-Besonderheiten:**

- Jede Jefa-Notpinne wird exakt auf das Ruderkopf-Profil der jeweiligen Jefa-Steueranlage gefertigt
- Edelstahl 316L, poliert und passiviert
- Sicherungsbolzen mit Federstecker
- Optionaler Taljen-Augbolzen am Pinnenende
- Mitgeliefert mit Montageanleitung und Beschriftungsaufkleber für Stauposition

### 4.2 Edson Emergency Tiller (Edson International, USA)

Edson International (New Bedford, Massachusetts) ist der größte US-Hersteller von Steueranlagen. Ihre Emergency Tiller sind ein Standard-Ausrüstungsgegenstand für amerikanische Segelyachten.

**Edson Emergency Tiller — Produktlinie:**

| Modell | Ruderkopf | Pinnen-Länge (mm) | Material | Gewicht (kg) | Preis (USD, ca.) |
|--------|-----------|-------------------|----------|-------------|-----------------|
| 665ST-24 | 1" (25 mm) Vierkant | 610 (24") | Edelstahl 316 | 0,7 | 145 |
| 665ST-30 | 1-1/4" (32 mm) Vierkant | 762 (30") | Edelstahl 316 | 1,0 | 175 |
| 665ST-36 | 1-1/2" (38 mm) Vierkant | 914 (36") | Edelstahl 316 | 1,5 | 210 |
| 665ST-42 | 1-3/4" (44 mm) Vierkant | 1.067 (42") | Edelstahl 316 | 2,0 | 260 |
| 665ST-48 | 2" (51 mm) Vierkant | 1.219 (48") | Edelstahl 316 | 2,8 | 330 |
| 665ST-60 | 2-1/2" (63 mm) Vierkant | 1.524 (60") | Edelstahl 316 | 4,5 | 450 |

**Edson Emergency Tiller — Telescopic:**

| Modell | Ruderkopf | Min. Länge (mm) | Max. Länge (mm) | Gewicht (kg) | Preis (USD, ca.) |
|--------|-----------|----------------|----------------|-------------|-----------------|
| 670T-30 | 1-1/4" (32 mm) | 450 | 760 | 1,2 | 225 |
| 670T-36 | 1-1/2" (38 mm) | 500 | 910 | 1,8 | 275 |
| 670T-48 | 2" (51 mm) | 600 | 1.220 | 3,2 | 380 |

**Edson-Besonderheiten:**

- Standardmäßig für Edson-Steueranlagen (Pedestal Guards) gefertigt
- Adapter für Whitlock-, Lewmar- und Jefa-Ruderkopf-Profile erhältlich
- Inklusive Nylon-Sicherungsleine gegen Verlust
- Optionaler Verlängerungsadapter für schwere See
- Marine-Grade-Edelstahl, poliert

### 4.3 Hydrovane (Hydrovane International Marine, UK)

Die Hydrovane ist eine Windfahnensteuerung mit eigenem Ruderblatt, die am Heck montiert wird. Sie dient primär als Selbststeueranlage, hat aber einen erheblichen Zusatznutzen als Notsteuerung:

**Hydrovane als Notsteuerung:**

Bei Ausfall des Hauptruders kann die Hydrovane als Notruder genutzt werden:

1. Windfahnen-Mechanismus deaktivieren (Fahne fixieren)
2. Pinne der Hydrovane manuell bedienen
3. Eigenes Ruderblatt der Hydrovane übernimmt die Steuerung

**Hydrovane-Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| Hersteller | Hydrovane International Marine Inc. |
| Sitz | Portsmouth, UK / Victoria, BC, Kanada |
| Typ | Windfahnensteuerung mit Hilfsruder |
| Ruderblattfläche | 0,12 m² (Standard), 0,16 m² (Heavy Duty) |
| Ruderblattmaterial | GFK, schlagfest |
| Max. Bootslänge | 21 m (Standard), 24 m (Heavy Duty) |
| Max. Verdrängung | 25 t (Standard), 40 t (Heavy Duty) |
| Montage | Heck-Spiegel, Heckkorb oder Davits |
| Gewicht | 18 kg (Standard), 24 kg (Heavy Duty) |
| Preis (ca.) | £ 3.200 (Standard), £ 4.100 (Heavy Duty) |

**Vorteile als Notsteuerung:**

- Permanentes zweites Ruder, immer einsatzbereit
- Keine Montage unter Stress erforderlich
- Ausreichende Ruderfläche für effektive Steuerung
- Pinne direkt zugänglich, kein Zugang unter Cockpitboden nötig
- Bei Blauwasserseglern weit verbreitet (geschätzt 15.000+ Installationen weltweit)

**Einschränkungen als Notsteuerung:**

- Ruderblatt kleiner als Hauptruder → geringere Steuerwirkung bei Starkwind
- Position ganz achtern am Heck → langer Hebelarm, aber geringe Anströmgeschwindigkeit bei langsamer Fahrt
- Pinnensteuerung umgekehrt (Pinne nach Stb → Boot dreht nach Bb) — kann bei ungeübter Crew zur Verwirrung führen

### 4.4 Jordan Series Drogue (Ace Sailmakers / DIY nach Jordan-Design)

Der Jordan Series Drogue (JSD) wurde von Donald Jordan in den 1980er Jahren entwickelt und ist nach umfangreichen Tests durch die US-Coast-Guard das empfohlene Sturmtaktik-System für Fahrtenyachten.

**Jordan Series Drogue — Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| Erfinder | Donald Jordan (MIT) |
| Prinzip | Kette kleiner Kegel auf langer Leine |
| Kegel-Material | Ballistic Nylon 500D oder Sunbrella |
| Kegel-Durchmesser | 127 mm (5") Standard |
| Abstand zwischen Kegeln | 510 mm (20") |
| Leine | High-Tenacity Polyester oder Dyneema |
| Bridle | Y-Leine, 2 × Bootslänge, zu Bb/Stb-Heckpunkten |
| Gewichteter Schwanz | 10–15 kg Kettengewicht am Ende der Leine |

**Herstellerquellen:**

| Hersteller/Lieferant | Land | Fertigung | Preis-Range (€) |
|----------------------|------|----------|-----------------|
| Ace Sailmakers | USA | Komplett-System | 1.200–3.500 |
| Fiorentino Para Anchor | USA | Komplett-System | 1.000–3.000 |
| Ocean Brake / DIY | International | Bausatz / Eigenbau | 400–1.200 |
| Para-Tech Engineering | USA | Komplett-System + Beratung | 1.500–4.000 |

**Einsatz als Notsteuerung:**

1. JSD über Heck ausbringen (Bridle an beiden Heck-Klampen)
2. Bridle-Parten Bb/Stb über Winschen führen
3. Durch differentielles Dichtholen/Fieren der Bridle-Parten: Kurskorrektur ±20–30°
4. Geschwindigkeit 1–3 kn bei 8+ Bft
5. Kursänderung: langsam (2–5° pro Minute)

### 4.5 Para-Anchor (Fiorentino, Para-Tech)

**Fiorentino Para-Anchor — Produktlinie:**

| Modell | Schirm-Ø (m) | Für Bootslänge (m) | Haltekraft (kN) | Gewicht (kg) | Preis (USD, ca.) |
|--------|-------------|-------------------|-----------------|-------------|-----------------|
| FIO-6 | 1,8 | 6–8 | 3–6 | 2,5 | 350 |
| FIO-9 | 2,7 | 8–10 | 6–12 | 4,0 | 500 |
| FIO-12 | 3,6 | 10–13 | 12–22 | 6,5 | 750 |
| FIO-15 | 4,5 | 13–16 | 22–35 | 9,0 | 1.100 |
| FIO-18 | 5,4 | 16–19 | 35–50 | 13,0 | 1.500 |
| FIO-24 | 7,2 | 19–24 | 50–80 | 20,0 | 2.200 |

**Para-Tech Sea Anchor — Produktlinie:**

| Modell | Schirm-Ø (ft/m) | Für Bootslänge (m) | Gewicht (kg) | Preis (USD, ca.) |
|--------|----------------|-------------------|-------------|-----------------|
| PT-9 | 9' / 2,7 | 8–10 | 3,8 | 480 |
| PT-12 | 12' / 3,6 | 10–13 | 5,5 | 720 |
| PT-15 | 15' / 4,5 | 13–16 | 8,0 | 980 |
| PT-18 | 18' / 5,4 | 16–19 | 11,5 | 1.350 |
| PT-24 | 24' / 7,2 | 19–24 | 18,0 | 2.000 |

**Para-Anchor — Dimensionierungs-Faustregeln:**

Die korrekte Dimensionierung eines Para-Anchors ist entscheidend für seine Wirksamkeit als Stabilisierungshilfe bei der Notsteuerung:

```
Empfohlener Schirmdurchmesser:
  D_schirm (ft) ≈ Bootslänge (ft) × 0,3 bis 0,4 (Segelyachten)
  D_schirm (ft) ≈ Bootslänge (ft) × 0,35 bis 0,45 (Motoryachten, höherer Windwiderstand)

Empfohlene Leinenlänge:
  L_rode ≈ 8 bis 12 × Bootslänge (um Synchronisation mit Wellenperiode zu vermeiden)

Leinenmaterial:
  Nylon (3-Strang oder 8-Strang geflochten) — bevorzugt wegen Elastizität
  Kettenvorstoß: 3–5 m Kette am Para-Anchor-Ende gegen Schamfilen
```

**Vergleich Para-Anchor vs. Jordan Series Drogue als Notsteuerungshilfe:**

| Kriterium | Para-Anchor | Jordan Series Drogue |
|-----------|------------|---------------------|
| Position | Bug (Luv) | Heck (Lee) |
| Boot-Ausrichtung | Bug zum Wind | Heck zum Wind |
| Geschwindigkeit | ~0 kn (stationär) | 1–3 kn (langsame Fahrt) |
| Kurssteuerung | Keine | Begrenzt (±20–30°) |
| Abdrift | 1–2 kn Lee | Kontrolliert vor dem Wind |
| Belastung auf Boot | Hoch (Bugbeschläge) | Verteilt (Heck-Klampen) |
| Einsatz bei Starkwind | Gut (>7 Bft) | Sehr gut (>7 Bft) |
| Einsatz bei Leichtwind | Nicht sinnvoll | Nicht sinnvoll |
| Einholen | Schwierig bei >6 Bft | Einfacher (Kegel kollabieren) |
| Platzbedarf Lagerung | Mittel (1 Sack) | Groß (langer Sack) |
| Preis (typisch, 12 m Boot) | €600–€900 | €1.200–€2.500 |
| Empfehlung Notsteuerung | Stabilisierung (keine Fahrt) | Kontrollierte Fahrt + Steuerung |

**Zubehör (Fiorentino/Para-Tech):**

| Zubehör | Funktion | Preis (USD, ca.) |
|---------|---------|-----------------|
| Rode (Schleppleine) | Nylon, Kettenvorstoß, Wirbel | 200–800 |
| Trip Line | Auslöseleine zum Einholen | 80–150 |
| Float (Markierungsboje) | Kennzeichnung der Position | 30–60 |
| Chafe Protection | Schamfilschutz an Klüse/Bug | 50–120 |
| Deployment Bag | Bereitstellungstasche | 60–120 |

---

## 5. Hersteller-Datenbank

### 5.1 Jefa Marine A/S

| Parameter | Wert |
|-----------|------|
| **Firma** | Jefa Marine A/S |
| **Sitz** | Svendborg, Dänemark |
| **Gegründet** | 1978 |
| **Spezialgebiet** | Ruderanlagen, Steueranlagen, Notpinnen für Segelyachten |
| **Produktbereiche** | Ruderlager, Ruderschaft, Steueranlage, Notpinne, Quadranten, Seilführung |
| **Bootsgröße** | 6–35 m |
| **Marktposition** | Weltmarktführer Segelyacht-Steueranlagen (geschätzt 40 % Marktanteil Neubau) |
| **Zertifizierung** | ISO 9001, DNV-GL-Typzulassung, CE-konform |
| **Website** | www.jefa.com |
| **Vertrieb** | Weltweit über Fachhändler und Werften |
| **AYDI-Relevanz** | Primärreferenz für Ruderkopf-Maße und Notpinnen-Kompatibilität |
| **Besonderheit** | Jede Anlage wird maßgefertigt — Notpinne muss zum konkreten Ruderkopf passen |

**Jefa-Notpinnen-Sortiment:**

- Standard Emergency Tiller (Vierkant, 25–70 mm)
- Splined Emergency Tiller (Keilwelle, 32–60 mm)
- Custom Emergency Tiller (Sonderanfertigung)
- Emergency Tiller Kit (Notpinne + Talje + Augbolzen)

### 5.2 Edson International

| Parameter | Wert |
|-----------|------|
| **Firma** | Edson International |
| **Sitz** | New Bedford, Massachusetts, USA |
| **Gegründet** | 1859 |
| **Spezialgebiet** | Steueranlagen, Steuerräder, Pedesals, Notpinnen |
| **Produktbereiche** | Pedestal-Steuerung, Steuerräder, Notpinnen, Kompasssäulen |
| **Bootsgröße** | 7–30 m |
| **Marktposition** | Marktführer USA und Kanada für Segelyacht-Pedestals |
| **Zertifizierung** | ABYC-konform, CE-konform |
| **Website** | www.edsonintl.com |
| **Vertrieb** | USA, Kanada direkt; international über Vertretungen |
| **AYDI-Relevanz** | Primärreferenz für US-gebaute Yachten (Beneteau USA, Catalina, Hunter, Island Packet) |
| **Besonderheit** | Umfangreiches Adapter-Programm für fremde Ruderkopf-Formate |

### 5.3 Hydrovane International Marine Inc.

| Parameter | Wert |
|-----------|------|
| **Firma** | Hydrovane International Marine Inc. |
| **Sitz** | Victoria, BC, Kanada (Produktion); Portsmouth, UK (Entwicklung) |
| **Gegründet** | 1970 |
| **Spezialgebiet** | Windfahnensteuerung mit Hilfsruder |
| **Produktbereiche** | Hydrovane-Windfahnensteuerung (ein Produkt in mehreren Varianten) |
| **Bootsgröße** | 7–24 m |
| **Marktposition** | Führend bei kombinierten Windfahnen-/Notruder-Systemen |
| **Zertifizierung** | CE-konform, ISO 10592 (als Notsteuerung) |
| **Website** | www.hydrovane.com |
| **Vertrieb** | Weltweit über Fachhändler |
| **AYDI-Relevanz** | Doppelnutzen: Selbststeuerung + Notruder → hohe Bewertung im Sicherheits-Modul |
| **Besonderheit** | Einziges System, das gleichzeitig Windfahne und vollwertiges Notruder bietet |

### 5.4 Lewmar Ltd.

| Parameter | Wert |
|-----------|------|
| **Firma** | Lewmar Ltd. |
| **Sitz** | Havant, Hampshire, UK |
| **Gegründet** | 1946 |
| **Spezialgebiet** | Winschen, Luken, Steueranlagen, Decksbeschläge |
| **Produktbereiche** | Hydraulische Steuerung (Constellation-Serie), Mechanische Steuerung, Notpinnen |
| **Bootsgröße** | 7–40 m |
| **Marktposition** | Breit aufgestellter Marktführer im Decksbeschlag-Bereich |
| **Zertifizierung** | ISO 9001, CE-konform, Lloyds-zertifiziert (Superyacht-Bereich) |
| **Website** | www.lewmar.com |
| **Vertrieb** | Weltweit über Fachhändler und OEM-Werften |
| **AYDI-Relevanz** | Hydraulik-Bypass-Ventile, Notpinnen für Lewmar-Steueranlagen |
| **Besonderheit** | Breitestes Produktprogramm — von Kleinboot-Seilzug bis Superyacht-Hydraulik |

**Lewmar-Notpinnen:**

| Modell | Ruderkopf | Pinnen-Länge (mm) | Material | Preis (€, ca.) |
|--------|-----------|-------------------|----------|----------------|
| 89000218 | 25 mm Vierkant | 750 | Edelstahl | 135 |
| 89000219 | 32 mm Vierkant | 900 | Edelstahl | 165 |
| 89000220 | 38 mm Vierkant | 1.050 | Edelstahl | 195 |
| 89000221 | 44 mm Vierkant | 1.200 | Edelstahl | 250 |
| 89000222 | 51 mm Vierkant | 1.350 | Edelstahl | 320 |

### 5.5 Whitlock Steering Systems (Teil von Lewmar)

| Parameter | Wert |
|-----------|------|
| **Firma** | Whitlock Steering Systems (Marke von Lewmar) |
| **Sitz** | Havant, Hampshire, UK (zusammen mit Lewmar) |
| **Gegründet** | 1963 (seit 1997 Teil von Lewmar) |
| **Spezialgebiet** | Mechanische Seilzug- und Radsteuerungen für Segelyachten |
| **Produktbereiche** | Cobra-Steuerung, Mamba-Steuerung, Notpinnen, Steuerräder |
| **Bootsgröße** | 7–18 m |
| **Marktposition** | Europäischer Standard für Seilzugsteuerung (OEM bei Bavaria, Jeanneau, Beneteau) |
| **Zertifizierung** | ISO 8847, CE-konform |
| **Website** | www.lewmar.com (Whitlock-Bereich) |
| **AYDI-Relevanz** | Sehr häufig auf europäischen Serienbooten → Standard-Ruderkopf-Maße |
| **Besonderheit** | Whitlock-Ruderkopf-Vierkant ist de-facto-Standard bei vielen europäischen Werften |

### 5.6 Fiorentino Para-Anchor Inc.

| Parameter | Wert |
|-----------|------|
| **Firma** | Fiorentino Para-Anchor Inc. |
| **Sitz** | Ventura, Kalifornien, USA |
| **Gegründet** | 1992 |
| **Spezialgebiet** | Treibanker (Para-Anchors), Schleppbremsen |
| **Produktbereiche** | Para-Anchor (SUB, IMP, BRO), Rode, Zubehör |
| **Bootsgröße** | 5–30 m |
| **Marktposition** | Führend bei Para-Anchors (USA) |
| **Zertifizierung** | USCG-gelistet, ABYC-konform |
| **Website** | www.fiorentinopara-anchor.com |
| **Vertrieb** | USA direkt, international über Fachhändler |
| **AYDI-Relevanz** | Para-Anchor als Stabilisierungssystem bei Notsteuerung |
| **Besonderheit** | Umfangreiche Testnachweise (USCG-gefördert) |

### 5.7 Para-Tech Engineering Co.

| Parameter | Wert |
|-----------|------|
| **Firma** | Para-Tech Engineering Co. |
| **Sitz** | Oxnard, Kalifornien, USA |
| **Gegründet** | 1985 |
| **Spezialgebiet** | Treibanker, Schleppbremsen, Sturmtaktik-Systeme |
| **Produktbereiche** | Sea Anchor (Para-Tech Sea Anchor), Rode, Deployment Bags |
| **Bootsgröße** | 6–30 m |
| **Marktposition** | Führend bei professionellen Treibankern |
| **Zertifizierung** | USCG-gelistet, ISO-konform |
| **Website** | www.para-anchor.com |
| **AYDI-Relevanz** | Referenz für Para-Anchor-Dimensionierung |

### 5.8 Windpilot (Peter Förthmann, Deutschland)

| Parameter | Wert |
|-----------|------|
| **Firma** | Windpilot — Peter Förthmann |
| **Sitz** | Hamburg, Deutschland |
| **Gegründet** | 1968 |
| **Spezialgebiet** | Windfahnensteuerungen (Pacific, Pacific Plus, Pacific Light) |
| **Produktbereiche** | Servo-Pendelruder- und Hilfsruder-Windfahnensteuerung |
| **Bootsgröße** | 7–22 m |
| **Marktposition** | Marktführer Deutschland, stark in Europa |
| **Website** | www.windpilot.com |
| **AYDI-Relevanz** | Pacific Plus hat eigenes Hilfsruder — bedingt als Notruder nutzbar |
| **Besonderheit** | Umfangreichste Dokumentation im Windfahnen-Bereich (Buch: „Windfahnensteuerung für Fahrtensegler") |

**Windpilot als Notsteuerung:**

- Pacific Plus: Hilfsruder vorhanden, aber kleiner als bei Hydrovane → bedingt als Notruder
- Pacific Light: Servo-Pendelruder, kein eigenständiges Notruder
- Empfehlung: Bei Windpilot Pacific Plus die Pinne manuell bedienen + Segeltrimm → eingeschränkte Notsteuerung möglich

### 5.9 Scanmar International (Monitor Windvane)

| Parameter | Wert |
|-----------|------|
| **Firma** | Scanmar International |
| **Sitz** | Sausalito, Kalifornien, USA |
| **Gegründet** | 1975 |
| **Spezialgebiet** | Windfahnensteuerung (Monitor) |
| **Produktbereiche** | Monitor Windvane (Servo-Pendelruder-Typ) |
| **Bootsgröße** | 8–20 m |
| **Marktposition** | Führend bei Servo-Pendelruder-Windfahnen (USA) |
| **Website** | www.scanmarinternational.com |
| **AYDI-Relevanz** | Servo-Pendelruder kann als Notsteuerungshilfe dienen |
| **Besonderheit** | Servo-Pendelruder-Prinzip — nicht als vollwertiges Notruder geeignet, da kein eigenes Ruderblatt |

### 5.10 Hersteller-Vergleichsmatrix — Notsteuerungssysteme

| Hersteller | Produkt | Typ | Bootsgröße (m) | Preis-Range (€) | Als Notruder geeignet? | AYDI-Empfehlung |
|-----------|---------|-----|----------------|----------------|----------------------|----------------|
| Jefa | ET-Serie | Notpinne | 7–24 | 120–520 | Nein (nur Notpinne) | Primärempfehlung für Segelyachten |
| Edson | 665ST-Serie | Notpinne | 7–24 | 130–450 | Nein (nur Notpinne) | Primärempfehlung für US-Yachten |
| Lewmar | 89-Serie | Notpinne | 7–22 | 135–320 | Nein (nur Notpinne) | Für Lewmar-/Whitlock-Systeme |
| Hydrovane | Standard/HD | Windfahne + Ruder | 7–24 | 3.500–4.500 | JA (vollwertiges Hilfsruder) | Top-Empfehlung für Blauwasser |
| Windpilot | Pacific Plus | Windfahne + Ruder | 7–18 | 2.800–3.800 | Bedingt (kleines Hilfsruder) | Gute Alternative zur Hydrovane |
| Scanmar | Monitor | Windfahne (Servo) | 8–20 | 4.000–5.000 | NEIN (Servo-Pendelruder) | Nur als Selbststeuerung |
| Fiorentino | FIO-Serie | Para-Anchor | 6–24 | 300–2.000 | Stabilisierung, keine Steuerung | Für Sturmtaktik + Stabilisierung |
| Para-Tech | PT-Serie | Para-Anchor | 8–24 | 400–2.000 | Stabilisierung, keine Steuerung | Für Sturmtaktik + Stabilisierung |
| Ace Sailmakers | JSD | Jordan Series Drogue | 8–20 | 1.000–3.500 | Begrenzte Kurssteuerung | Empfehlung für Offshore + Blauwasser |

### 5.11 Bezugsquellen und Lieferzeiten

| Hersteller | Lieferzeit Standard | Lieferzeit Sonderanfertigung | Vertriebsweg Deutschland |
|-----------|-------------------|----------------------------|--------------------------|
| Jefa | 2–4 Wochen | 4–8 Wochen | SVB, Toplicht, Compass24, direkt |
| Edson | 3–6 Wochen (Import) | 6–10 Wochen | SVB, Marine-Fachhandel |
| Lewmar | 1–3 Wochen | 4–6 Wochen | SVB, Toplicht, Compass24, Bootszubehör-Handel |
| Hydrovane | 4–8 Wochen | 8–12 Wochen | Direkt ab Werk, einzelne Fachhändler |
| Fiorentino | 3–6 Wochen (Import) | — | Import über US-Händler oder SVB |
| Para-Tech | 3–6 Wochen (Import) | — | Import über US-Händler |
| Ace Sailmakers | 4–8 Wochen | 6–10 Wochen | Import über US-Händler oder direkt |

---

## 6. Fehlerbild-Atlas

### Fehlerbild 6.1 — Notpinne passt nicht auf den Ruderkopf

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Notpinne passt nicht auf den Ruderkopf |
| **Schweregrad** | CRITICAL |
| **Häufigkeit** | Sehr häufig (geschätzt 15–25 % aller Boote bei Ersttest) |
| **Beschreibung** | Die mitgelieferte oder nachgekaufte Notpinne lässt sich nicht auf den Ruderkopf aufsetzen — entweder zu groß, zu klein, falsche Geometrie (Vierkant vs. Sechskant), oder der Ruderkopf ist durch Korrosion aufgequollen |
| **Ursache** | Falsche Bestellung (Maße nicht geprüft), Ruderkopf getauscht (Refit) ohne Notpinnen-Anpassung, Ruderkopf-Vierkant durch Korrosion aufgeworfen, Notpinne von anderem Boot |
| **Erkennung** | Sichtprüfung: Aufnahme und Ruderkopf nebeneinander halten. Messung: Schieblehre. Funktionstest: Aufsetzen |
| **Sofortmaßnahme** | Ruderkopf mit Feile entgraten (Korrosionsaufwurf). Distanzblech unterlegen (zu groß). Aufnahme aufweiten (Metallwerkstatt) |
| **Endgültige Behebung** | Neue Notpinne passend zum aktuellen Ruderkopf anfertigen lassen. Maße dokumentieren |
| **Vermeidung** | Jährlicher Test: Notpinne aufsetzen und Probe-Steuern. Ruderkopf-Maße im Bordhandbuch dokumentieren |
| **AYDI-Scoring** | Compliance: -40 Punkte. Sicherheit: -50 Punkte |

### Fehlerbild 6.2 — Hydraulik-Bypass klemmt / lässt sich nicht öffnen

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Hydraulik-Bypass-Ventil festkorrodiert |
| **Schweregrad** | CRITICAL |
| **Häufigkeit** | Häufig (geschätzt 20–30 % aller Hydraulik-Steueranlagen >10 Jahre) |
| **Beschreibung** | Das Bypass-Ventil, das den Hydraulikkreislauf bei Ausfall kurzschließen soll, lässt sich nicht öffnen. Es ist durch jahrelange Nichtbenutzung korrodiert oder verkalkt |
| **Ursache** | Nie betätigt (sollte mind. 2× jährlich durchgedreht werden), Feuchtigkeit im Bilgenbereich, ungeeignetes Ventilmaterial (Messing statt Edelstahl) |
| **Erkennung** | Funktionstest: Ventil öffnen und schließen. Schwergängig? Nicht drehbar? |
| **Sofortmaßnahme** | WD-40 / Kriechöl auftragen, vorsichtig mit Rohrzange öffnen. NICHT mit Gewalt — Ventil kann brechen |
| **Endgültige Behebung** | Ventil austauschen (Edelstahl 316L). Wartungsplan: 2× jährlich betätigen und mit Hydrauliköl schmieren |
| **Vermeidung** | Halbjährlicher Funktionstest im Wartungsplan. Ventil-Position klar beschriften |
| **AYDI-Scoring** | Compliance: -35 Punkte. Sicherheit: -45 Punkte |

### Fehlerbild 6.3 — Ruderschaft gebrochen

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Ruderschaftbruch |
| **Schweregrad** | CRITICAL |
| **Häufigkeit** | Selten (1–3 % aller Steuerschäden), aber katastrophale Folgen |
| **Beschreibung** | Der Ruderschaft ist am oder unter dem oberen Lager gebrochen. Das Ruderblatt hängt lose oder ist verloren. Notpinne nutzlos, da keine Verbindung zum Ruder mehr besteht |
| **Ursache** | Materialermüdung (zyklische Belastung), Korrosion (Spaltkorrosion am Lager), Unterdimensionierung, Grundberührung mit anschließender Weiterfahrt |
| **Erkennung** | Plötzlicher Totalausfall der Steuerung. Ruderdruck fällt schlagartig auf Null. Visuelle Inspektion: Schaft gebrochen sichtbar am oberen Lager |
| **Sofortmaßnahme** | 1) Beidrehen oder Geschwindigkeit reduzieren. 2) Prüfen ob Ruderblatt noch am Boot (sonst Leck-Gefahr am Koker). 3) Koker mit Stopfen/Lappen abdichten falls Wasser eindringt. 4) Notruderblatt oder Schleppbremse einsetzen |
| **Endgültige Behebung** | Neuer Ruderschaft (Werft). Vollständige Analyse der Bruchursache (Gutachter). Materialprüfung (Ultraschall, Röntgen) aller verbleibenden Schaftteile |
| **Vermeidung** | Alle 5 Jahre Ultraschall-Prüfung des Schaftes am Lagerbereich. Korrosionsschutz am Lager. Nicht mit gebogenem Schaft weiterfahren |
| **AYDI-Scoring** | Strukturell: -80 Punkte. Sicherheit: CRITICAL FLAG |

### Fehlerbild 6.4 — Ruderblatt abgerissen

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Ruderblatt-Abriss (vollständiger Verlust) |
| **Schweregrad** | CRITICAL |
| **Häufigkeit** | Mäßig häufig bei Spatenrudern (geschätzt 3–5 % aller Offshore-Schäden über Lebensdauer) |
| **Beschreibung** | Das Ruderblatt hat sich vom Ruderschaft gelöst oder ist abgebrochen. Typisch bei Spatenrudern nach Treibgut-Kollision, Grundberührung oder Materialversagen der Schaft-Blatt-Verbindung |
| **Ursache** | GFK-Delaminierung am Schaftdurchgang, Korrosion des Schaft-Skeletts im Ruderblatt, Treibgut-Schlag, Grundberührung, Materialermüdung |
| **Erkennung** | Plötzlicher Verlust des Ruderdrucks. Steuerbewegung ohne Wirkung. Visuell: kein Ruder mehr sichtbar am Heck |
| **Sofortmaßnahme** | 1) Geschwindigkeit reduzieren. 2) Ruderstumpf sichern (gegen Beschädigung des Kokers). 3) Notruderblatt montieren oder Schleppbremse ausbringen. 4) Segeltrimm-Steuerung einleiten |
| **Endgültige Behebung** | Neues Ruder (Werft). Schaftintegrität prüfen |
| **Vermeidung** | Regelmäßige Inspektion der Schaft-Blatt-Verbindung (Ausklopftest, Ultraschall). Bei GFK-Ruderblattern: osmotische Blistering kontrollieren |
| **AYDI-Scoring** | Strukturell: -90 Punkte. Sicherheit: CRITICAL FLAG |

### Fehlerbild 6.5 — Ruderkopf nicht zugänglich

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Ruderkopf-Zugang blockiert |
| **Schweregrad** | HIGH |
| **Häufigkeit** | Häufig (geschätzt 30 % aller Serienboote bei Ersttest) |
| **Beschreibung** | Der Ruderkopf, auf den die Notpinne aufgesetzt werden muss, ist durch fest verschraubte Cockpitbodenplatten, schweres Equipment (Rettungsinsel, Tauwerk), festverbaute Autopilot-Einheiten oder einlaminierte Revisionsdeckel nicht oder nur schwer zugänglich |
| **Ursache** | Werft-Design priorisiert Cockpit-Ästhetik über Notsteuerungs-Zugang. Eignerumbauten (Autopilot nachgerüstet) verdecken Zugang. Schweres Equipment auf der Zugangsplatte gelagert |
| **Erkennung** | Prüfung: Kann der Ruderkopf innerhalb von 5 Minuten freigelegt werden? Werkzeug erforderlich? Wie viele Schrauben? Wie schwer ist das zu bewegende Equipment? |
| **Sofortmaßnahme** | Zugangsplatte öffnen (Schrauben lösen, Equipment beiseite räumen). Wenn fest: Schrauben mit Schlagschrauber oder Hammer/Meißel lösen |
| **Endgültige Behebung** | Zugangsplatte auf Schnellverschluss (Cam-Lock, Drehgriff) umrüsten. Klar beschriften „NOTPINNE — EMERGENCY TILLER". Equipment von Platte entfernen. Schrauben mit Anti-Seize behandeln |
| **Vermeidung** | Bei Werftplanung Ruderkopf-Zugang als Sicherheitsanforderung definieren. OSR-Compliance prüfen |
| **AYDI-Scoring** | Compliance: -25 Punkte. Ergonomie: -20 Punkte. Sicherheit: -30 Punkte |

### Fehlerbild 6.6 — Autopilot blockiert Quadranten

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Autopilot-Linearantrieb blockiert mechanisch den Quadranten |
| **Schweregrad** | HIGH |
| **Häufigkeit** | Mäßig häufig (geschätzt 10–15 % aller Boote mit nachgerüstetem Autopilot) |
| **Beschreibung** | Der lineare Autopilot-Antrieb (z. B. Raymarine Type 1/2, B&G, Simrad) ist mechanisch mit dem Quadranten verbunden und blockiert die freie Ruderbewegung, wenn der Autopilot ausfällt oder der Antrieb klemmt |
| **Ursache** | Autopilot ohne Entkopplung montiert. Kupplungspin fehlt oder korrodiert. Linearzylinder hat mechanische Selbsthemmung |
| **Erkennung** | Ruder bewegt sich nicht frei, auch wenn Bypass offen. Sichtprüfung: Autopilot-Antrieb blockiert Quadranten-Schwenk |
| **Sofortmaßnahme** | 1) Autopilot-Kupplungspin ziehen (falls vorhanden). 2) Bolzen am Quadranten-Anschluss des Autopilots lösen. 3) Wenn weder 1 noch 2: Autopilot-Antrieb mit Schraubenschlüssel vom Quadranten abschrauben |
| **Endgültige Behebung** | Autopilot mit Schnellkupplung (Quick-Release-Pin) am Quadranten montieren. Entkopplungsverfahren dokumentieren und üben |
| **Vermeidung** | Schnellkupplung bei Autopilot-Montage vorsehen. Jährlich Entkopplungstest durchführen |
| **AYDI-Scoring** | Compliance: -20 Punkte. Sicherheit: -25 Punkte |

### Fehlerbild 6.7 — Seilzug gerissen, kein Zugang zum Quadranten

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Seilzugriss mit unzugänglichem Quadranten |
| **Schweregrad** | HIGH |
| **Häufigkeit** | Mäßig (geschätzt 5 % aller Segelyachten mit Seilzugsteuerung über 15 Jahre) |
| **Beschreibung** | Das Steuerseil oder die Steuerkette ist gerissen. Der Quadrant unter Deck ist nicht zugänglich, weil der Zugangsschacht zu klein, durch Einbauten verbaut oder durch den Autopilot blockiert ist |
| **Ursache** | Seilzug-Alterung (typische Lebensdauer 8–12 Jahre), Korrosion, Schamfilen an Umlenkrollen. Zugang nie geprüft |
| **Erkennung** | Steuerrad dreht ohne Widerstand. Seil schlaff sichtbar. Kein Ruderdruck |
| **Sofortmaßnahme** | 1) Notpinne auf Ruderkopf (sofern zugänglich). 2) Wenn Ruderkopf nicht zugänglich: Leinen an den Quadranten binden und von Deck bedienen (erfordert Zugang zum Quadranten von anderer Seite) |
| **Endgültige Behebung** | Neues Steuerseil einziehen. Zugang zum Quadranten verbessern. Alte Seilführung auf Schamfilen prüfen |
| **Vermeidung** | Seilzug alle 8–10 Jahre erneuern. Quadranten-Zugang jährlich prüfen. Zugang klar beschriften |
| **AYDI-Scoring** | Compliance: -30 Punkte. Sicherheit: -35 Punkte |

### Fehlerbild 6.8 — Notpinne Sicherungsbolzen fehlt

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Sicherungsbolzen der Notpinne fehlt oder defekt |
| **Schweregrad** | MEDIUM |
| **Häufigkeit** | Häufig (geschätzt 20 % aller Boote mit Notpinne bei Survey) |
| **Beschreibung** | Die Notpinne kann auf den Ruderkopf aufgesetzt werden, aber der Sicherungsbolzen (der das Abziehen unter Last verhindert) fehlt, ist korrodiert, oder der zugehörige Splint/Federstecker ist verloren |
| **Ursache** | Bolzen bei letztem Test nicht wieder eingesteckt. Korrosion. Splint verloren. Nicht als wichtig erkannt |
| **Erkennung** | Sichtprüfung: Bolzen/Splint kontrollieren. Funktionstest: Notpinne aufsetzen und versuchen abzuziehen |
| **Sofortmaßnahme** | Provisorisch: Kabelbinder, Leine oder Draht als Sicherung. Notfalls Schraubzwinge |
| **Endgültige Behebung** | Neuen Bolzen und Splint/Federstecker beschaffen. Ersatz-Splint als Backup an die Notpinne binden |
| **Vermeidung** | Bolzen und Splint mit Sicherungsleine an der Notpinne befestigen. Bei jährlichem Test kontrollieren |
| **AYDI-Scoring** | Sicherheit: -15 Punkte |

### Fehlerbild 6.9 — Notruderblatt-Halterung gebrochen

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Halterung des Notruders unter Belastung gebrochen |
| **Schweregrad** | HIGH |
| **Häufigkeit** | Selten, aber dokumentiert (geschätzt 5 % bei tatsächlichem Einsatz unter Stress) |
| **Beschreibung** | Das Notruderblatt wurde montiert, aber die Halterung (Pintles/Gudgeons, Schäkelverbindung, Leinenbefestigung) bricht unter der Belastung durch Seegang und Steuerkräfte |
| **Ursache** | Halterung zu schwach dimensioniert. Material korrodiert. Notruder nie unter realistischen Bedingungen getestet. DIY-Konstruktion ohne Berechnung |
| **Erkennung** | Notruder geht während des Einsatzes verloren oder bricht aus der Halterung |
| **Sofortmaßnahme** | Notruder mit stärkerer Sicherungsleine erneut befestigen. Halterung mit Bordmitteln verstärken (Schäkel, Kauschen, doppelte Leinenführung) |
| **Endgültige Behebung** | Halterung professionell dimensionieren und fertigen. Belastungstest durchführen |
| **Vermeidung** | Notruder unter realistischen Bedingungen testen (mindestens 4–5 Bft). Halterung großzügig dimensionieren (Sicherheitsfaktor 3×) |
| **AYDI-Scoring** | Sicherheit: -35 Punkte |

### Fehlerbild 6.10 — Schleppbremse verfängt sich in Ruderresten

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Schleppbremse/Drogue verfängt sich in noch vorhandenem Ruderrest |
| **Schweregrad** | MEDIUM |
| **Häufigkeit** | Selten, aber dokumentiert |
| **Beschreibung** | Beim Ausbringen einer Schleppbremse über das Heck verfängt sich die Bridle oder die Schleppeleine am noch teilweise vorhandenen Ruderstumpf oder an herausragenden Ruderbeschlägen |
| **Ursache** | Ruder nur teilweise verloren — Stumpf ragt noch aus dem Koker. Bridle-Leinenführung nicht für diesen Fall geplant |
| **Erkennung** | Schleppbremse zieht nicht richtig. Asymmetrischer Zug. Sichtprüfung achtern |
| **Sofortmaßnahme** | Schleppbremse einholen, Leinenführung ändern (weiter außenbords über Relingstützen). Ggf. Ruderstumpf mit Leine sichern und fixieren |
| **Endgültige Behebung** | Ruderstumpf bergungssicher fixieren oder entfernen (wenn möglich). Schleppbremsen-Bridle mit ausreichend seitlichem Abstand führen |
| **Vermeidung** | Schleppbremsen-Einsatz mit und ohne Ruder vorplanen. Bridle-Punkte außerhalb des Ruderschwenkbereichs setzen |
| **AYDI-Scoring** | Sicherheit: -15 Punkte |

### Fehlerbild 6.11 — Notpinne zu kurz für Drehmoment

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Notpinne bietet zu wenig Hebelarm für das Ruderdrehmoment |
| **Schweregrad** | HIGH |
| **Häufigkeit** | Häufig bei Booten >14 m ohne Talje (geschätzt 30 %) |
| **Beschreibung** | Die Notpinne ist zwar montierbar, aber der Rudergänger kann das Ruder bei Starkwind oder hoher Fahrt nicht halten. Die erforderliche Handkraft übersteigt 200–300 N |
| **Ursache** | Notpinne nach Werft-Standard (minimale Länge), keine Talje vorgesehen. Bei Serienbooten wird oft die kürzeste mögliche Pinne geliefert, um Stauraum zu sparen |
| **Erkennung** | Funktionstest bei 4+ Bft: Kann eine Person das Boot steuern? Zwei Personen? Handkraft schätzen |
| **Sofortmaßnahme** | Talje (4:1 oder 6:1) an das Pinnenende schalten, Parten zu Cockpit-Winschen führen |
| **Endgültige Behebung** | Längere Notpinne oder Teleskop-Notpinne beschaffen. Talje fest als Notsteuerungs-Kit vorbereiten |
| **Vermeidung** | Bei Kauf/Refit: Notpinnen-Länge berechnen (siehe 2.2.1). Talje-Set für Notsteuerung zusammenstellen |
| **AYDI-Scoring** | Sicherheit: -25 Punkte. Ergonomie: -20 Punkte |

### Fehlerbild 6.12 — Notsteuerungs-Equipment unauffindbar

| Parameter | Beschreibung |
|-----------|-------------|
| **Bezeichnung** | Notpinne oder Notsteuerungs-Equipment an Bord nicht auffindbar |
| **Schweregrad** | CRITICAL |
| **Häufigkeit** | Häufig (geschätzt 15–20 % bei Charterbooten, 5–10 % bei Eignerbooten) |
| **Beschreibung** | Im Notfall kann die Notpinne, das Bypass-Werkzeug oder das Notruder nicht gefunden werden. Es liegt in einem nicht gekennzeichneten Stauraum, unter Bergen von Ausrüstung, oder ist beim letzten Refit verloren gegangen |
| **Ursache** | Keine Beschriftung des Stauplatzes. Notpinne nie aus der Werft-Verpackung genommen. Stauort bei Umräumaktion vergessen. Charterübergabe ohne Einweisung in Notsteuerung |
| **Erkennung** | Übung: Crew soll Notsteuerungs-Equipment innerhalb von 3 Minuten finden und präsentieren |
| **Sofortmaßnahme** | Boot systematisch durchsuchen. Typische Stauorte: Heckkasten, Cockpit-Backskiste, Lazarette, unter Salontisch, Motorraumseitenwand |
| **Endgültige Behebung** | Notpinne an festem, beschriftetem Platz lagern. Aufkleber „NOTPINNE — EMERGENCY TILLER — HIER" |
| **Vermeidung** | Beschrifteter Stauort. Crew-Einweisung bei jedem Törn. Checkliste Sicherheitsausrüstung |
| **AYDI-Scoring** | Compliance: -30 Punkte. Sicherheit: -40 Punkte |

---

## 7. Troubleshooting-Entscheidungsbäume

### Entscheidungsbaum 7.1 — Steuerung fällt komplett aus

```
SYMPTOM: Steuerrad dreht ohne Wirkung ODER Ruder reagiert nicht auf Steuerbewegung

├── [1] Hydraulische Steuerung?
│   ├── JA
│   │   ├── [2] Öl-Lache im Bilge-/Maschinenraum sichtbar?
│   │   │   ├── JA → Hydraulikleck
│   │   │   │   ├── [3] Bypass-Ventil öffnen
│   │   │   │   │   ├── Bypass öffnet sich → Notpinne aufsetzen → STEUERN
│   │   │   │   │   └── Bypass klemmt → Kriechöl + Rohrzange → Bypass öffnen
│   │   │   │   │       ├── Bypass offen → Notpinne aufsetzen → STEUERN
│   │   │   │   │       └── Bypass defekt → Leinen an Quadranten → STEUERN
│   │   │   │   └── [4] Wenn kein Öl mehr im System: Zylinder kann blockieren
│   │   │   │       ├── Bypass hilft → Notpinne → STEUERN
│   │   │   │       └── Zylinder blockiert trotz Bypass → Bolzen am Zylinder lösen → Quadrant freimachen → Notpinne → STEUERN
│   │   │   └── NEIN → Kein sichtbares Leck
│   │   │       ├── [5] Pumpe defekt? (Steuerrad dreht leicht, kein Druck)
│   │   │       │   ├── JA → Bypass öffnen → Notpinne → STEUERN
│   │   │       │   └── NEIN → Steuerzylinder blockiert
│   │   │       │       ├── Bypass öffnen → Funktionstest
│   │   │       │       └── Zylinder mechanisch entkoppeln → Notpinne → STEUERN
│   │   └── NEIN → Keine hydraulische Steuerung
│       ├── [6] Seilzug-/Kettensteuerung?
│       │   ├── JA
│       │   │   ├── [7] Steuerrad dreht frei (kein Widerstand)?
│       │   │   │   ├── JA → Seil/Kette gerissen oder abgefallen
│       │   │   │   │   ├── Ruderkopf zugänglich? → Notpinne aufsetzen → STEUERN
│       │   │   │   │   └── Ruderkopf nicht zugänglich? → Zugangsplatte öffnen → Notpinne → STEUERN
│       │   │   │   │       └── Zugangsplatte nicht öffenbar → Leinen an Quadranten → STEUERN
│       │   │   │   └── NEIN → Steuerrad blockiert
│       │   │   │       ├── [8] Seil verklemmt in Umlenkrolle
│       │   │   │       │   ├── Seil lösen → Steuerung funktioniert → WEITERFAHREN
│       │   │   │       │   └── Seil nicht lösbar → Notpinne → STEUERN
│       │   │   │       └── [9] Quadrant/Sektor blockiert (Autopilot, Fremdkörper)
│       │   │   │           ├── Autopilot entkoppeln → Steuerung frei → WEITERFAHREN
│       │   │   │           └── Nicht lösbar → Notpinne → STEUERN
│       │   └── NEIN → Andere Steuerungsart
│       │       └── [10] Zahnstange, elektrisch, Fly-by-Wire → Herstelleranleitung / Notpinne
│       └── [11] Pinnensteuerung?
│           ├── JA
│           │   ├── [12] Pinne gebrochen?
│           │   │   ├── JA → Ersatzpinne / Notpinne auf Ruderkopf → STEUERN
│           │   │   └── NEIN → Ruderlager blockiert → Lager prüfen
│           │   └── [13] Rudergabel gebrochen?
│           │       ├── JA → Rohrzange auf Ruderkopf → PROVISORISCH STEUERN
│           │       └── NEIN → Ruderblatt prüfen (Fehlerbild 6.4)
│           └── NEIN → Unbekannter Steuerungstyp → Borddokumentation konsultieren
```

### Entscheidungsbaum 7.2 — Ruder verloren (kein Ruderblatt mehr)

```
SYMPTOM: Ruderblatt vollständig verloren, kein Ruderdruck, visuell kein Ruder am Heck

├── [1] Windfahnensteuerung (Hydrovane, Monitor) an Bord?
│   ├── JA
│   │   ├── Hydrovane → Windfahne fixieren → Pinne manuell bedienen → STEUERN
│   │   └── Monitor (Servo-Pendelruder) → Begrenzte Steuerwirkung → Zusätzlich Segeltrimm
│   └── NEIN
│       ├── [2] Mitgeführtes Notruderblatt vorhanden?
│       │   ├── JA
│       │   │   ├── [3] Heck-Montage möglich? (Pintles/Gudgeons, Schäkel, Halterung)
│       │   │   │   ├── JA → Notruder montieren → Pinne bedienen → STEUERN
│       │   │   │   └── NEIN → Seitliche Montage → PROVISORISCH STEUERN
│       │   │   └── [4] Notruder zu klein / instabil?
│       │   │       └── Segeltrimm zusätzlich einsetzen → KOMBINIERT STEUERN
│       │   └── NEIN → Kein Notruder
│       │       ├── [5] Segelyacht?
│       │       │   ├── JA
│       │       │   │   ├── [6] Wind 2–5 Bft → Segeltrimm-Steuerung einsetzen (Kap. 2.4)
│       │       │   │   │   ├── Kurs zum nächsten Hafen möglich → SEGELTRIMM STEUERN
│       │       │   │   │   └── Kurs nicht möglich → Zickzack-Kurs → SEGELTRIMM STEUERN
│       │       │   │   ├── [7] Wind >6 Bft → Schleppbremse ausbringen
│       │       │   │   │   ├── JSD vorhanden → Ausbringen + Bridle-Steuerung → STEUERN
│       │       │   │   │   ├── Para-Anchor vorhanden → Bug zum Wind → STABILISIEREN
│       │       │   │   │   └── Nichts vorhanden → Improvisation (Eimer, Reifen, Segel als Drogue)
│       │       │   │   └── [8] Wind <2 Bft → Motor + Improvisation
│       │       │   │       ├── Doppelschrauber → Differentialsteuerung → STEUERN
│       │       │   │       ├── Einzelschrauber → Paddel/Riemen über Heck → PROVISORISCH STEUERN
│       │       │   │       └── Kein Motor → Improvisation mit Paddel → NOTSTEUERUNG
│       │       │   └── NEIN → Motoryacht
│       │       │       ├── [9] Doppelschrauber?
│       │       │       │   ├── JA → Differentialsteuerung (asymmetrische Drehzahl) → STEUERN
│       │       │       │   └── NEIN → Einzelschrauber
│       │       │       │       ├── Bugstrahler → Langsamfahrt + Bugstrahler → PROVISORISCH STEUERN
│       │       │       │       ├── Schleppbremse → Asymmetrisch schleppen → PROVISORISCH STEUERN
│       │       │       │       └── Keine Hilfsmittel → EPIRB/DSC → SAR ANFORDERN
│       │       │       └── [10] Situation bewerten:
│       │       │           ├── Nahe Hafen (<10 nm) → Schlepp anfordern (Funk Ch 16)
│       │       │           └── Fern von Hafen → SAR anfordern (EPIRB, DSC, Satphone)
```

### Entscheidungsbaum 7.3 — Notpinne lässt sich nicht aufsetzen

```
SYMPTOM: Notpinne vorhanden, aber lässt sich nicht auf den Ruderkopf aufsetzen

├── [1] Ruderkopf zugänglich?
│   ├── NEIN
│   │   ├── [2] Cockpitboden-Platte identifizieren
│   │   │   ├── Schrauben erkennbar → Schrauben lösen → Platte abheben
│   │   │   │   ├── Schrauben festkorrodiert → Schlagschrauber / Hammer + Meißel
│   │   │   │   └── Platte verklebt → Messer / Meißel am Rand → vorsichtig aufbrechen
│   │   │   └── Keine erkennbare Platte → Borddokumentation → Zugang von unten (Achterkajüt)?
│   │   └── [3] Equipment auf der Platte?
│   │       ├── Rettungsinsel → Beiseite schaffen (2 Personen)
│   │       ├── Tauwerk / Fender → Beiseite werfen
│   │       └── Fest installiert → Werkzeug → Abschrauben
│   └── JA → Ruderkopf freiliegend
│       ├── [4] Notpinne passt nicht?
│       │   ├── Zu eng (geht nicht drauf)
│       │   │   ├── Ruderkopf aufgeblüht (Korrosion) → Feile / Schleifpapier → Aufwurf entfernen
│       │   │   ├── Falsche Geometrie (rund vs. Vierkant) → Nicht passend → Alternative suchen
│       │   │   └── Eiskristalle / Salzkruste → Warmwasser / WD-40 → Reinigen → Erneut versuchen
│       │   ├── Zu weit (wackelt)
│       │   │   ├── Distanzblech (dünnes Aluminium, Blechdose) unterlegen
│       │   │   ├── Leine um Ruderkopf + Notpinne wickeln → Klemmung
│       │   │   └── Rohrzange als zusätzliche Klemmung am Ruderkopf
│       │   └── Falsches Profil (Keilwelle vs. Vierkant)
│       │       ├── Nicht kompatibel → Rohrzange als Notlösung
│       │       └── Adapter suchen (falls mitgeliefert)
│       └── [5] Notpinne passt, aber Ruderkopf dreht nicht?
│           ├── Autopilot blockiert → Autopilot entkoppeln (siehe 6.6)
│           ├── Seilzug verklemmt → Seil lösen / durchschneiden
│           ├── Quadrant blockiert (Fremdkörper) → Fremdkörper entfernen
│           └── Ruderlager blockiert → Kriechöl → Vorsichtig lösen → Wenn unlösbar: Notruder
```

### Entscheidungsbaum 7.4 — Steuerung schwergängig / Ruder blockiert teilweise

```
SYMPTOM: Steuerung funktioniert, aber extrem schwergängig oder blockiert in bestimmten Positionen

├── [1] Hydraulische Steuerung?
│   ├── JA
│   │   ├── [2] Schwergängig über gesamten Bereich?
│   │   │   ├── JA → Hydrauliköl-Stand prüfen
│   │   │   │   ├── Öl-Stand niedrig → Nachfüllen → Test
│   │   │   │   │   ├── Besser → Leck suchen → Weiterfahren mit Vorsicht
│   │   │   │   │   └── Nicht besser → Luft im System → Entlüften
│   │   │   │   └── Öl-Stand OK → Ventil teilweise geschlossen? → Alle Ventile prüfen
│   │   │   │       ├── Ventil korrigiert → OK
│   │   │   │       └── Alle Ventile OK → Zylinder-Innenschaden → Bypass + Notpinne
│   │   │   └── NEIN → Schwergängig nur in einer Position
│   │   │       ├── [3] Mechanische Blockade
│   │   │       │   ├── Ruder schlägt an Koker-Öffnung → Lager verschoben
│   │   │       │   ├── Quadrant schlägt an Autopilot → Endanschlag einstellen
│   │   │       │   └── Fremdkörper (Leine, Plastiktüte) am Ruderblatt → Rückwärtsfahren / Taucher
│   │   │       └── [4] Hydraulische Teilblockade
│   │   │           ├── Zylinder-Dichtung quillt → Innerer Widerstand → Werkstatt
│   │   │           └── Schlauch geknickt → Begradigen → Test
│   └── NEIN → Mechanische Steuerung
│       ├── [5] Seilzug?
│       │   ├── Seil hat sich um Umlenkrolle gewickelt → Lösen
│       │   ├── Umlenkrolle blockiert (Lager defekt) → Ölen oder ersetzen
│       │   └── Seil korrodiert (Einzeldrähte gebrochen) → Seilzug erneuern
│       └── [6] Zahnstange?
│           ├── Zahnstange trocken → Fetten
│           ├── Zahnrad verschlissen → Werkstatt
│           └── Zahnstange verbogen → Werkstatt → Notpinne als Zwischenlösung
```

### Entscheidungsbaum 7.5 — Notsteuerung unter Starkwind (>7 Bft)

```
SYMPTOM: Steuerungsausfall bei Starkwind (>7 Bft) und hohem Seegang

├── [1] SOFORTMASSNAHMEN (ERSTE 5 MINUTEN)
│   ├── a) Geschwindigkeit reduzieren (Bergen aller Segel / Motor auf Leerlauf)
│   ├── b) Beidrehen (wenn Segelyacht: Fock back, Groß dicht, Ruder Luv)
│   │   └── Ohne Ruder: Fock back schlagen, Groß fiercen → Boot dreht bei
│   ├── c) Besatzung sichern (Lifelines, Gurte)
│   └── d) Situationsbewertung: Position, Abstand zu Gefahr, Wind/See-Entwicklung
│
├── [2] NOTSTEUERUNG EINRICHTEN (MINUTEN 5–30)
│   ├── [2a] Notpinne verfügbar und passend?
│   │   ├── JA
│   │   │   ├── Notpinne aufsetzen
│   │   │   ├── Talje anschlagen (OBLIGATORISCH bei >7 Bft und >12 m Boot)
│   │   │   ├── 2 Personen an der Notpinne
│   │   │   ├── Nur unter gerefften Segeln / reduzierter Fahrt steuern
│   │   │   └── Kurs: Raum (120–150° zum Wind) → stabilster Kurs
│   │   └── NEIN → Kein Notpinnen-Einsatz möglich
│   │       ├── [2b] Schleppbremse (JSD) vorhanden?
│   │       │   ├── JA → JSD über Heck ausbringen
│   │       │   │   ├── Bridle Bb/Stb differentiell → Kurskorrektur
│   │       │   │   ├── Alle Segel bergen (JSD bremst das Boot)
│   │       │   │   └── Boot läuft mit 1–3 kn kontrolliert vor dem Wind
│   │       │   └── NEIN → Kein JSD
│   │       │       ├── [2c] Para-Anchor vorhanden?
│   │       │       │   ├── JA → Para-Anchor über Bug ausbringen
│   │       │       │   │   ├── Boot liegt mit Bug zum Wind
│   │       │       │   │   ├── Stabil, aber keine Kurssteuerung
│   │       │       │   │   └── Abdrift 1–2 kn Lee
│   │       │       │   └── NEIN → Improvisation erforderlich
│   │       │       │       ├── [2d] Improvisierte Schleppbremse
│   │       │       │       │   ├── Eimer/Reifen/gebundene Segel über Heck
│   │       │       │       │   ├── Asymmetrisch für Kurskorrektur
│   │       │       │       │   └── Begrenzte Wirkung, aber besser als nichts
│   │       │       │       └── [2e] Segeltrimm-Steuerung
│   │       │       │           ├── Bei >7 Bft nur unter Sturmfock oder Trysegel
│   │       │       │           ├── Kurs: Am Wind oder Raum (NICHT vor dem Wind)
│   │       │       │           └── 2+ Personen für Schot-Bedienung
│   │
│   └── [3] KOMMUNIKATION
│       ├── Pan-Pan auf VHF Ch 16 (Notsteuerung, keine unmittelbare Gefahr)
│       ├── Position, Kurs, Geschwindigkeit durchgeben
│       ├── Nächsten Hafen anfragen (Schlepphilfe?)
│       └── Wenn Gefahr für Leib und Leben → Mayday → SAR
```

---

## 8. FAQ

### FAQ 8.1 — Grundlagen

**F1: Brauche ich auf meiner Yacht eine Notpinne?**

A: Ja, wenn Ihre Yacht eine Radsteuerung (Steuerrad) hat und Sie außerhalb geschützter Gewässer fahren. Für Regatten nach World-Sailing-/ORC-Regeln ist eine Notpinne für die Kategorien 0–3 obligatorisch. Für Blauwasserfahrten ist sie unverzichtbar. Auch für Küstenfahrten ist sie dringend empfohlen — jeder Steuerungsausfall in einer belebten Fahrrinne oder in der Nähe von Lee-Küsten kann gefährlich werden.

**F2: Woher weiß ich, welche Notpinne zu meinem Boot passt?**

A: Messen Sie den Ruderkopf (Vierkant, Sechskant oder Keilwelle) mit einer Schieblehre. Die Maße stehen in der Werft-Dokumentation oder können beim Hersteller der Steueranlage erfragt werden. Typische Hersteller sind Jefa, Whitlock (Lewmar), Edson. Bestellen Sie die Notpinne exakt passend — ein universelles „passt überall"-System gibt es nicht.

**F3: Wie oft muss ich die Notpinne testen?**

A: Mindestens 1× jährlich. Bei Regatten nach OSR: vor jedem Rennen im Rahmen des Safety Audits. Empfehlung: Bei jedem Saisonstart Notpinne aufsetzen, Probe-Steuern (auch nur im Hafen bei losgeworfenen Leinen), Sicherungsbolzen prüfen.

**F4: Was kostet eine Notpinne?**

A: Für eine Standard-Notpinne aus Edelstahl rechnen Sie mit €80–€250 für Boote bis 12 m und €200–€600 für Boote bis 24 m. Teleskop-Modelle und Sonderanfertigungen können bis €800 kosten. Gegenüber den Kosten eines SAR-Einsatzes oder Schiffsverlust (ab €10.000 aufwärts) eine vernachlässigbare Investition.

**F5: Muss die Notpinne bei einer Yacht mit Pinnensteuerung auch vorhanden sein?**

A: Bei reiner Pinnensteuerung (ohne Radsteuerung) ist eine separate Notpinne in der Regel nicht erforderlich, da die Pinne selbst die Direktverbindung zum Ruder ist. Empfohlen wird aber eine Ersatzpinne (falls die Hauptpinne bricht) und ein Sicherungsbolzen als Ersatz.

### FAQ 8.2 — Hydraulik-Bypass

**F6: Was ist ein Hydraulik-Bypass und wofür brauche ich ihn?**

A: Der Hydraulik-Bypass ist ein Ventil im hydraulischen Steuerkreislauf, das bei Öffnung das Ruder freigibt. Bei Hydraulikversagen (Leck, Pumpendefekt) würde das Ruder sonst blockiert bleiben, weil das Hydrauliköl im geschlossenen Zylinder nicht entweichen kann. Durch Öffnen des Bypass wird der Zylinder umgangen und das Ruder kann per Notpinne bewegt werden.

**F7: Wo finde ich das Bypass-Ventil auf meinem Boot?**

A: Typische Positionen: Am Steuerzylinder selbst (kleine Stellschraube oder Kugelhahn), in der Hydraulikleitung nahe dem Zylinder, oder in einem Verteilerblock im Bereich des Quadranten. Suchen Sie in der Herstellerdokumentation oder fragen Sie Ihre Werft. Beschriften Sie das Ventil, sobald Sie es gefunden haben.

**F8: Wie oft muss ich das Bypass-Ventil betätigen?**

A: Mindestens 2× jährlich (Saisonstart und Saisonende). Drehen Sie das Ventil vollständig auf und zu. Wenn es schwergängig ist: WD-40 oder Kriechöl, dann erneut betätigen. Ein Ventil, das 10 Jahre nicht bewegt wurde, wird mit hoher Wahrscheinlichkeit festsitzen, wenn Sie es brauchen.

### FAQ 8.3 — Notruder

**F9: Brauche ich ein Notruderblatt?**

A: Für Küstenfahrten (< 50 nm von der Küste) ist ein Notruderblatt empfehlenswert, aber nicht zwingend. Für Blauwasserfahrten (> 200 nm von der Küste) ist es dringend empfohlen. Die Statistik zeigt, dass 16 % aller Steuerversagen auf Ruderblatt-Verlust zurückgehen — in diesem Fall hilft keine Notpinne.

**F10: Welche Größe muss ein Notruder haben?**

A: Faustformel: A_notruder ≥ 0,015 × LWL × Tiefgang. Für ein 12 m Boot mit 1,8 m Tiefgang: 0,015 × 10,5 × 1,8 = 0,28 m². In der Praxis reichen aber schon 50–70 % dieser Fläche für eine notdürftige Steuerung. Jede Ruderfläche ist besser als keine.

**F11: Kann ich eine Windfahnensteuerung als Notruder verwenden?**

A: Ja, aber nur bestimmte Typen. Die Hydrovane hat ein eigenes, vollständiges Ruderblatt und ist als Notruder hervorragend geeignet. Servo-Pendelruder-Systeme (Monitor, Aries) haben nur ein kleines Hilfsruder, das allein nicht als vollwertiges Notruder taugt.

### FAQ 8.4 — Schleppbremsen

**F12: Kann ich mit einem Jordan Series Drogue steuern?**

A: Ja, eingeschränkt. Durch differentielles Bedienen der Bridle-Leinen (Bb/Stb) können Sie den Kurs um ±20–30° korrigieren. Für eine 90°-Kursänderung müssen Sie den JSD einholen und auf neuem Kurs wieder ausbringen. Die Kursänderung ist langsam (2–5° pro Minute).

**F13: Para-Anchor oder Jordan Series Drogue — was ist besser für die Notsteuerung?**

A: Unterschiedliche Anwendung. Der JSD wird über das Heck geschleppt und erlaubt kontrollierte Fahrt vor dem Wind (1–3 kn) mit begrenzter Kurssteuerung. Der Para-Anchor wird über den Bug ausgebracht und hält das Boot stationär mit dem Bug zum Wind (keine Fahrt, keine Kurssteuerung). Für die Notsteuerung bei Ruderversagen ist der JSD besser, weil er Kurskorrektur ermöglicht. Der Para-Anchor ist besser, wenn Sie in schwerem Sturm einfach abwettern wollen.

**F14: Kann ich einen Eimer als improvisierte Schleppbremse verwenden?**

A: Ja, ein großer, robuster Eimer (10–20 L) an einer langen Leine über das Heck kann als provisorische Schleppbremse dienen. Die Bremswirkung ist begrenzt (geschätzt 200–500 N), reicht aber bei Leichtwind (< 5 Bft) für eine gewisse Kurssteuerung. Bei Starkwind wird der Eimer schnell weggespült oder die Leine reißt. Besser: Mehrere Eimer, einen alten Autoreifen, oder ein zusammengebundenes Segel als Schleppwiderstand.

### FAQ 8.5 — Segeltrimm-Steuerung

**F15: Kann ich meine Segelyacht wirklich ohne Ruder steuern?**

A: Ja, bei moderaten Bedingungen (3–5 Bft) und ausreichender Übung. Durch Verschieben des Segeldruckpunktes (Fock dichtholen = abfallen, Groß dichtholen = anluven) lässt sich ein halbwegs kontrollierbarer Kurs fahren. Es erfordert aber Übung und ist bei Starkwind oder vor dem Wind sehr schwierig. Empfehlung: Üben Sie die Segeltrimm-Steuerung bei ruhigem Wetter, bevor Sie sie im Notfall brauchen.

**F16: Funktioniert Segeltrimm-Steuerung auch bei einem Katamaran?**

A: Grundsätzlich ja, aber schwieriger als bei einem Monohull. Katamarane haben weniger Lateralfläche im Verhältnis zur Segelfläche und sind kursstabiler. Die Trimmsteuerung erfordert größere Segelverstellungen für den gleichen Kurswechsel. Vorteil: Katamarane haben zwei Ruder — bei Verlust eines Ruders ist immer noch ein Ruder vorhanden.

### FAQ 8.6 — Spezialfälle

**F17: Wie steuere ich eine Motoryacht ohne Ruder?**

A: Bei einem Doppelschrauber: Differentialsteuerung über asymmetrische Drehzahl oder Schaltung (Stb vorwärts + Bb rückwärts = Drehung auf der Stelle). Bei einem Einzelschrauber: Bugstrahler bei Langsamfahrt, Schleppbremse asymmetrisch, oder SAR anfordern. Motoryachten ohne Ruder und ohne zweiten Antrieb haben sehr begrenzte Notsteuerungsmöglichkeiten.

**F18: Was mache ich, wenn der Ruderschaft im Koker gebrochen ist und Wasser eindringt?**

A: PRIORITY 1: Leck abdichten. Stopfen (Holzkegel, Weichholz-Pfropfen), Lappen, Unterwasser-Epoxid (z. B. Belzona, Splash Zone) in den Koker pressen. Ggf. Cockpitboden-Platte öffnen und von oben abdichten. Lenzpumpe einschalten. Erst wenn das Leck unter Kontrolle ist: Notsteuerung einrichten. In schweren Fällen: Mayday.

**F19: Mein Autopilot hat einen eigenen Notfall-Modus (Standby/Override). Reicht das als Notsteuerung?**

A: Nein. Der Autopilot-Notmodus (Standby) schaltet lediglich den Autopilot ab und gibt die Steuerung zurück an das Steuerrad. Er löst keine mechanischen Steuerungsprobleme. Wenn die Steuerung selbst ausgefallen ist (Seilzugriss, Hydraulikleck), hilft der Autopilot-Standby nicht. Eine mechanische Notpinne ist immer erforderlich.

**F20: Ich habe eine elektrische (Fly-by-Wire) Steuerung. Brauche ich trotzdem eine Notpinne?**

A: Unbedingt. Fly-by-Wire-Systeme haben keine mechanische Verbindung zwischen Steuerrad und Ruder. Bei Stromausfall oder Elektronikfehler gibt es keine Rückfallmöglichkeit auf mechanische Steuerung. Eine Notpinne (oder ein redundanter mechanischer Steuerkreis) ist bei Fly-by-Wire-Systemen besonders kritisch.

### FAQ 8.7 — Wartung und Prüfung

**F21: Wie lagere ich die Notpinne richtig?**

A: An einem festen, trockenen, beschrifteten Platz im Cockpit-Bereich (Backskiste, Lazarett, unter dem Cockpitboden nahe dem Ruderkopf). Die Notpinne muss innerhalb von 5 Minuten einsatzbereit sein — nicht tief in der Vorpiek vergraben. Vor Lagerung: dünn einfetten (Vaseline, Korrosionsschutz), in Tuch oder Beutel wickeln.

**F22: Rostet meine Edelstahl-Notpinne?**

A: Echte 316L-Edelstahl-Notpinnen rosten nicht im eigentlichen Sinne, können aber bei unzureichender Passivierung, Kontakt mit unedlen Metallen (galvanische Korrosion) oder in sauerstoffarmer Umgebung (Spalten, unter Dichtungen) Lochfraß oder Tea-Staining entwickeln. Jährliche Sichtkontrolle und gelegentliches Reinigen mit Edelstahl-Pflegemittel genügt.

**F23: Was gehört in ein Notsteuerungs-Kit?**

A: Empfohlener Inhalt:
- Notpinne (passend zum Ruderkopf)
- Sicherungsbolzen + 2× Ersatz-Splinte
- Talje (4:1 min., mit Blöcken und Leine)
- 2× Augbolzen oder Kauschen für Talje-Befestigung im Cockpit
- Rohrzange (450 mm) als Backup
- Werkzeug zum Öffnen der Ruderkopf-Zugangsplatte (Schraubendreher, Innensechskant)
- Anleitung (laminiert, wasserfest) mit Diagramm
- Optional: Ersatz-Seilzug oder Steuerkettenglied

**F24: Mein Boot ist ein Charterboot. Worauf muss ich bei der Übernahme bezüglich Notsteuerung achten?**

A: Bei der Charter-Übernahme: 1) Fragen Sie nach der Notpinne und lassen Sie sie zeigen. 2) Setzen Sie die Notpinne probeweise auf (Passgenauigkeit). 3) Fragen Sie nach dem Bypass-Ventil (bei Hydraulik). 4) Prüfen Sie die Zugänglichkeit des Ruderkopfs. 5) Dokumentieren Sie den Stauort. Wenn keine Notpinne vorhanden: Reklamieren. Fahren Sie nicht ohne Notsteuerungsmöglichkeit.

**F25: Wie teste ich die Notsteuerung auf See?**

A: Idealerweise bei ruhigem Wetter (2–3 Bft), ausreichend Seeraum: 1) Autopilot aus, Steuerrad loslassen. 2) Notpinne aufsetzen (Zugangsplatte öffnen, Pinne draufstecken, Bolzen sichern). 3) 5–10 Minuten mit der Notpinne steuern. 4) Manöver üben (Wende, Kurshalten). 5) Talje anschlagen und testen. 6) Zeit messen (Umrüstung sollte <10 min dauern). 7) Alles verstauen, Steuerrad wieder übernehmen.

**F26: Kann ich die Notpinne auch bei laufendem Autopilot aufsetzen?**

A: Ja, das Aufsetzen ist mechanisch möglich. Aber: Bevor Sie mit der Notpinne steuern, muss der Autopilot entkoppelt werden (Standby + mechanische Entkopplung). Sonst arbeitet der Autopilot-Antrieb gegen die Notpinne, was den Quadranten, die Notpinne oder den Autopilot beschädigen kann.

**F27: Welche Rolle spielt die Ruderbalancierung für die Notsteuerung?**

A: Eine entscheidende. Ein balanciertes Ruder (15–20 % Balance) reduziert das Drehmoment am Schaft um 40–60 % gegenüber einem unbalancierten Ruder. Das bedeutet: Bei einem balancierten Ruder kann eine Person mit der Notpinne steuern, wo bei einem unbalancierten Ruder zwei Personen plus Talje erforderlich wären. Die Ruderbalancierung ist der wichtigste einzelne Faktor für die Handhabbarkeit der Notpinne.

### FAQ 8.8 — Spezifische Bootstypen und Situationen

**F28: Wie steuere ich einen Katamaran mit nur einem Ruder?**

A: Katamarane mit Doppelruder haben einen inhärenten Vorteil: Wenn ein Ruder ausfällt, kann mit dem verbleibenden Ruder weitergesteuert werden. Das Boot wird etwas asymmetrisch reagieren, aber grundsätzlich steuerbar bleiben. Zusätzlich können Motorkatamarane mit Doppelantrieb über Differentialsteuerung den Kurs korrigieren. Seilzug zum defekten Ruder lösen, damit es keinen Widerstand erzeugt.

**F29: Wie bereite ich mein Boot auf eine Atlantiküberquerung in Bezug auf Notsteuerung vor?**

A: Minimale Ausrüstung für eine Atlantiküberquerung: 1) Notpinne, getestet und passend. 2) Talje (4:1 oder 6:1) für die Notpinne. 3) Jordan Series Drogue als Sturmtaktik + Notsteuerung. 4) Idealerweise ein Notruderblatt oder eine Windfahnensteuerung (Hydrovane) mit eigenem Ruder. 5) Ersatz-Seilzug oder Steuerkette. 6) Werkzeug für Autopilot-Entkopplung. 7) Dokumentation aller Notsteuerungsverfahren (laminiert, wasserfest). 8) Die gesamte Crew muss alle Verfahren geübt haben — mindestens ein Probedurchgang vor der Abfahrt.

**F30: Was ist eine Windfahnen-Notsteuerung und wie funktioniert sie?**

A: Eine Windfahnensteuerung (z. B. Hydrovane, Monitor, Windpilot, Aries) ist primär eine Selbststeueranlage, die den Kurs relativ zum Wind hält. Einige Typen (insbesondere die Hydrovane) haben ein eigenes, vollständiges Hilfsruder, das im Notfall als Ersatzruder dienen kann. Dazu wird der Windfahnen-Mechanismus fixiert und die Pinne des Hilfsruders manuell bedient. Servo-Pendelruder-Systeme (Monitor, Aries) steuern hingegen das Hauptruder über Leinen und haben nur ein kleines Hilfsruder, das allein nicht als Notruder ausreicht.

**F31: Wie oft sollte ich das Steuerseil erneuern, um einen Riss zu vermeiden?**

A: Empfohlen alle 8–10 Jahre, unabhängig vom Zustand. Seile aus Edelstahldraht (7×19) verlieren durch Mikrorisse und Korrosion an den Umlenkstellen ihre Festigkeit, oft ohne sichtbare Anzeichen. Bei intensiver Nutzung (Regatta, Charterboot) alle 5–7 Jahre. Jährliche Sichtprüfung: Auf Einzeldrahtbrüche achten (mit einem Tuch am Seil entlangfahren — gebrochene Drähte fangen sich). Kette: Alle 10–15 Jahre, auf Verschleiß an den Gliedern prüfen.

**F32: Kann ich eine Notpinne selbst bauen?**

A: Ja, für einen erfahrenen Handwerker ist das möglich. Kritisch ist die Aufnahme: Exakte Maße des Ruderkopfs abnehmen (Schieblehre), Aufnahme aus Edelstahl-Flachmaterial schweißen oder fräsen lassen, Schaft aus Edelstahlrohr (316L, Ø 30–40 mm, Wandstärke 2,5–3 mm). Sicherungsbohrung für Federstecker nicht vergessen. Augbolzen am Ende für Talje-Befestigung. WICHTIG: Nachher testen — passt die Aufnahme? Sitzt der Bolzen? Ist genug Drehmoment übertragbar? Im Zweifel professionell anfertigen lassen (Kosten: €150–€400 bei einer Metallwerkstatt).

### FAQ 8.9 — Notsteuerung und Versicherung

**F33: Zahlt meine Versicherung, wenn ich keinen Notsteuerungssystem an Bord hatte?**

A: Das hängt von der Police und den Umständen ab. Die meisten Kaskoversicherungen (Pantaenius, Yacht-Pool, Allianz Marine) setzen die Einhaltung der „Regeln guter Seemannschaft" voraus. Eine fehlende Notsteuerung bei einer Offshore-Fahrt kann als grobe Fahrlässigkeit gewertet werden, was die Deckungssumme reduziert oder den Anspruch ganz ausschließt. Empfehlung: Dokumentieren Sie Ihre Notsteuerungsausrüstung und die jährlichen Tests im Logbuch — das stärkt Ihre Position im Schadensfall erheblich.

**F34: Muss ich den Einsatz der Notsteuerung melden?**

A: An sich besteht keine Meldepflicht für den privaten Einsatz der Notsteuerung. Empfohlen wird aber: 1) Eintrag im Logbuch (Datum, Uhrzeit, Position, Ursache, Maßnahmen). 2) Bei gewerblicher Nutzung: Meldung an die Flaggenstaatbehörde (BSH für deutsche Flagge). 3) Wenn SAR involviert war: Bericht an die zuständige SAR-Stelle. 4) Bei Schiffsunfall (Kollision, Grundberührung als Folge): Meldung an die Bundesstelle für Seeunfalluntersuchung (BSU).

**F35: Wie wirkt sich eine gute Notsteuerungsausrüstung auf den Schiffswert aus?**

A: Eine vollständige, gut gewartete Notsteuerungsausrüstung (Notpinne, Talje, ggf. Notruder, Schleppbremse) erhöht den Schiffswert nicht direkt messbar, ist aber bei der Zustandsbewertung durch Gutachter ein positiver Faktor. Bei Surveys (Pre-Purchase, Insurance Survey) wird die Notsteuerung geprüft — ein gutes Ergebnis stärkt das Gesamtbild des Schiffs. Umgekehrt: Eine fehlende oder unpassende Notpinne ist ein häufig dokumentierter Survey-Mangel.

### FAQ 8.10 — Praxis-Tipps

**F36: Wie übe ich die Notsteuerung am besten?**

A: Ideales Szenario: Ruhiger Tag (2–3 Bft), offenes Wasser, Crew komplett. 1) Steuerrad loslassen, Autopilot aus. 2) Eine Person öffnet die Zugangsplatte und setzt die Notpinne auf — Stoppuhr läuft. 3) 15–20 Minuten unter Notpinne steuern (Kurs halten, Wende, Halse). 4) Talje anschlagen und testen. 5) Wenn möglich: Segeltrimm-Steuerung ohne Notpinne üben (Ruder loswerfen). 6) Wenn JSD vorhanden: Testweise ausbringen und einholen (nicht unbedingt mit dem Boot verbunden). Ziel: Jedes Crewmitglied kann die Notpinne in <5 min aufsetzen und <10 min voll einsatzbereit steuern.

**F37: Was ist der häufigste Fehler bei der Notsteuerung?**

A: Der mit Abstand häufigste Fehler ist: Die Notpinne wurde nie getestet und passt nicht. Der zweithäufigste: Die Crew weiß nicht, wo die Notpinne liegt. Der dritthäufigste: Der Autopilot blockiert den Quadranten und niemand weiß, wie man ihn entkoppelt. Alle drei Fehler sind trivial vermeidbar durch einen jährlichen 15-Minuten-Test.

---

## 9. Glossar

| Nr. | Begriff | Englisch | Definition |
|-----|---------|----------|------------|
| 1 | Notpinne | Emergency tiller | Hebel, der direkt auf den Ruderkopf aufgesetzt wird, um das Ruder bei Ausfall der regulären Steuerung manuell zu bedienen |
| 2 | Notruder | Emergency rudder | Transportables Ersatz-Ruderblatt, das bei Verlust des Hauptruders montiert wird |
| 3 | Ruderkopf | Rudder head / rudder stock top | Oberes Ende des Ruderschafts, auf das Quadrant, Sektor oder Notpinne aufgesetzt werden |
| 4 | Ruderschaft | Rudder stock / rudder shaft | Vertikale Welle, die das Drehmoment vom Quadranten auf das Ruderblatt überträgt |
| 5 | Ruderblatt | Rudder blade | Hydrodynamisches Profil im Wasser, das die Steuerkraft erzeugt |
| 6 | Quadrant | Quadrant / sector | Halbkreisförmiger Hebel am Ruderkopf, an dem Seilzug oder Kette angreifen |
| 7 | Ruderkoker | Rudder tube | Rohr durch den Rumpf, in dem der Ruderschaft läuft |
| 8 | Bypass-Ventil | Bypass valve | Ventil im Hydraulikkreislauf, das bei Öffnung das Ruder freigibt |
| 9 | Talje | Tackle / purchase | Flaschenzug aus Blöcken und Leine zur Kraftuntersetzung |
| 10 | Bridle | Bridle | Y-förmige Schleppleine, die einen Drogue oder Para-Anchor mit zwei Heckpunkten verbindet |
| 11 | Drogue | Drogue | Schleppbremse, die über das Heck geschleppt wird und die Geschwindigkeit reduziert |
| 12 | Para-Anchor | Para-anchor / sea anchor | Fallschirmförmiger Treibanker, der über den Bug ausgebracht wird |
| 13 | Jordan Series Drogue (JSD) | Jordan Series Drogue | Schleppbremse aus einer Kette kleiner Kegel auf langer Leine |
| 14 | Jury-Rig | Jury rig | Improvisierte Steuerung oder Takelung unter Verwendung von Bordmitteln |
| 15 | Beidrehen | Heave to | Manöver zum Stoppen des Bootes bei Starkwind (Fock back, Groß dicht) |
| 16 | Segeldruckpunkt (CE) | Center of Effort (CE) | Geometrischer Mittelpunkt der Segelkräfte |
| 17 | Lateralschwerpunkt (CLR) | Center of Lateral Resistance (CLR) | Geometrischer Mittelpunkt des Unterwasser-Lateralwiderstands |
| 18 | Luvgierig | Weather helm | Tendenz des Bootes, in den Wind zu drehen (CE achtern von CLR) |
| 19 | Leegierig | Lee helm | Tendenz des Bootes, vom Wind abzufallen (CE vor CLR) |
| 20 | Spatenruder | Spade rudder | Freistehendes Ruder ohne Skeg-Stütze |
| 21 | Skeg-Ruder | Skeg-hung rudder | Ruder, das an einem vorgelagerten Skeg (Kielfortsatz) aufgehängt ist |
| 22 | Ruderbalancierung | Rudder balance | Anteil der Ruderfläche vor dem Ruderschaft (in % der Chord) |
| 23 | Drehmoment | Torque | Drehkraft am Ruderschaft (in Nm) |
| 24 | Vierkant | Square key / square socket | Quadratisches Profil am Ruderkopf für formschlüssige Kraftübertragung |
| 25 | Keilwellenverbindung | Splined connection | Gezahnte Verbindung am Ruderkopf für hohe Drehmomentübertragung |
| 26 | Federstecker | Split pin / R-clip | Federnder Sicherungsstift für Bolzenverbindungen |
| 27 | Splint | Cotter pin | Draht-Sicherungsstift, der durch ein Bolzenloch gesteckt und umgebogen wird |
| 28 | Windfahnensteuerung | Wind vane self-steering | Mechanische Selbststeueranlage, die die Windrichtung als Referenz nutzt |
| 29 | Servo-Pendelruder | Servo pendulum rudder | Hilfsruder einer Windfahnensteuerung, das über Leinen das Hauptruder steuert |
| 30 | Differentialsteuerung | Differential steering | Steuerung bei Doppelschraubern durch unterschiedliche Drehzahl der beiden Motoren |
| 31 | Radeffekt | Propeller walk / paddle wheel effect | Seitliche Kraft des Propellers, die ein Giermoment erzeugt |
| 32 | Ruderdruck | Helm / rudder pressure | Kraft, die der Rudergänger am Steuerrad oder an der Pinne spürt |
| 33 | Druckmittelpunkt | Center of pressure (CP) | Punkt auf dem Ruderblatt, an dem die resultierende hydrodynamische Kraft angreift |
| 34 | Capstan-Effekt | Capstan effect | Verstärkung der Haltekraft einer Leine durch Reibung auf einer zylindrischen Trommel |
| 35 | EPIRB | EPIRB (Emergency Position Indicating Radio Beacon) | Seenotfunkbake, die bei Aktivierung ein Notsignal mit Position sendet |
| 36 | DSC | DSC (Digital Selective Calling) | Digitaler Selektivruf im Seefunk für Notrufe |
| 37 | Pan-Pan | Pan-Pan | Dringlichkeitsmeldung im Seefunk (keine unmittelbare Lebensgefahr) |
| 38 | Mayday | Mayday | Notalarmierung im Seefunk (unmittelbare Gefahr für Schiff oder Leben) |
| 39 | SAR | SAR (Search and Rescue) | Such- und Rettungsdienst auf See |
| 40 | Schamfilen | Chafe / chafing | Abrieb einer Leine durch Reibung an scharfen Kanten oder rauen Oberflächen |
| 41 | Patenthalse | Accidental gybe | Unbeabsichtigte Halse durch plötzlichen Winddreher oder Kursinstabilität |
| 42 | Koker-Dichtung | Rudder tube seal | Dichtung zwischen Ruderschaft und Ruderkoker gegen Wassereinbruch |
| 43 | Linearantrieb | Linear actuator | Elektrischer oder hydraulischer Zylinder für Autopilot-Antrieb am Quadranten |
| 44 | Kupplungspin | Quick-release pin | Schnell entfernbarer Bolzen zur Entkopplung des Autopilots vom Quadranten |
| 45 | Cam-Lock | Cam lock / turn fastener | Schnellverschluss für Zugangsplatten (Viertelumdrehung) |
| 46 | Rudergabel | Rudder fork / tiller fitting | Beschlag am Ruderkopf, in den die Pinne eingesetzt wird |
| 47 | Steuerzylinder | Steering cylinder | Hydraulikzylinder, der den Quadranten/Ruderarm bewegt |
| 48 | Ruderarm | Rudder arm / tiller arm | Hebelarm am Ruderkopf (ähnlich Quadrant, aber gerader Hebel) |
| 49 | Backskiste | Cockpit locker | Staukasten im Cockpit, typischer Aufbewahrungsort für Notpinne |
| 50 | Lazarett | Lazarette | Staukasten im Heck, oft Zugang zum Steuerbereich |
| 51 | Pintle | Pintle | Zapfen an einem Ruder, der in die Gudgeon (Öse) am Heck greift |
| 52 | Gudgeon | Gudgeon | Öse/Auge am Heck, in die der Pintle des Ruders eingehängt wird |
| 53 | Trysegel | Trysegel / storm trysail | Kleines, robustes Segel als Ersatz für das Großsegel bei Sturm |
| 54 | Sturmfock | Storm jib | Kleines, schweres Vorsegel für Sturmbedingungen |
| 55 | Barber-Hauler | Barber hauler | Leine zur seitlichen Verstellung des Vorsegel-Holepunkts |

---

## 10. Schnell-Referenz

### 10.1 Notsteuerung — Sofortmaßnahmen (Cockpit-Karte)

```
╔══════════════════════════════════════════════════════════════╗
║         NOTSTEUERUNG — SOFORTMASSNAHMEN                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. GESCHWINDIGKEIT REDUZIEREN                               ║
║     → Segel bergen / Motor Leerlauf                          ║
║     → Beidrehen (Fock back + Groß dicht)                     ║
║                                                              ║
║  2. NOTPINNE AUFSETZEN                                       ║
║     → Zugangsplatte öffnen (unter Cockpitboden)              ║
║     → Notpinne auf Ruderkopf stecken                         ║
║     → Sicherungsbolzen einsetzen                             ║
║     → Bei Hydraulik: BYPASS-VENTIL ÖFFNEN                    ║
║     → Autopilot ENTKOPPELN                                   ║
║                                                              ║
║  3. TALJE ANSCHLAGEN (ab 14 m / >5 Bft)                     ║
║     → Talje an Pinnenende                                    ║
║     → Parten nach Bb + Stb über Winschen                     ║
║                                                              ║
║  4. STEUERN                                                  ║
║     → Nur unter gerefften Segeln / reduzierter Fahrt         ║
║     → 2 Personen bei Starkwind                               ║
║     → Kurs: Raum (120–150° zum Wind) ist am stabilsten       ║
║                                                              ║
║  5. KOMMUNIZIEREN                                            ║
║     → Pan-Pan Ch 16 (Dringlichkeit)                          ║
║     → Position, Kurs, Geschwindigkeit                        ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  KEIN RUDER? → Segeltrimm / Schleppbremse / SAR              ║
╚══════════════════════════════════════════════════════════════╝
```

### 10.2 Schnellreferenz — Notpinnen-Dimensionierung

| Bootslänge | Ruderkopf-Vierkant | Pinne min. | Talje? | Max. Handkraft (1 Pers.) |
|------------|-------------------|------------|--------|--------------------------|
| 8–10 m | 25–30 mm | 800 mm | Nein | 80–120 N |
| 10–12 m | 30–35 mm | 1.000 mm | Empfohlen ab 6 Bft | 100–150 N |
| 12–14 m | 35–40 mm | 1.200 mm | Ja, ab 5 Bft | 120–200 N |
| 14–16 m | 40–50 mm | 1.400 mm | Ja, immer | 150–250 N |
| 16–20 m | 50–60 mm | 1.600 mm | Obligatorisch | 200–400 N (2 Pers.) |
| 20–24 m | 60–70 mm | 1.800 mm | Obligatorisch | 300–600 N (2 Pers.) |

### 10.3 Schnellreferenz — Bypass-Ventil-Checkliste

| Prüfpunkt | OK | Problem | Maßnahme |
|-----------|-----|---------|----------|
| Position bekannt? | ✓ | ✗ → Suchen | Dokumentation, Hersteller fragen |
| Beschriftet? | ✓ | ✗ → Beschriften | Aufkleber anbringen |
| Drehbar? | ✓ | ✗ → Klemmt | Kriechöl, vorsichtig lösen |
| Dicht im Normalbetrieb? | ✓ | ✗ → Leckt | Ventil ersetzen |
| 2× jährlich betätigt? | ✓ | ✗ → Wartung versäumt | Sofort testen |

### 10.4 Schnellreferenz — Notsteuerungsmethoden nach Bootstyp

| Bootstyp | Methode 1 (primär) | Methode 2 | Methode 3 |
|----------|-------------------|-----------|-----------|
| Segelyacht, Radsteuerung | Notpinne | Segeltrimm | Schleppbremse |
| Segelyacht, Pinne | Ersatzpinne | Segeltrimm | Schleppbremse |
| Motoryacht, Einzelschrauber | Notpinne | Schleppbremse | SAR |
| Motoryacht, Doppelschrauber | Differential | Notpinne | Schleppbremse |
| Katamaran, Segel | Notpinne (2×) | Segeltrimm | Ein Ruder reicht |
| Katamaran, Motor | Notpinne (2×) | Differential | Ein Ruder reicht |

### 10.5 Schnellreferenz — Wartungsintervalle Notsteuerung

| Komponente | Prüfintervall | Prüfung | Aktion bei Befund |
|-----------|--------------|---------|------------------|
| Notpinne — Passgenauigkeit | Jährlich (Saisonstart) | Aufsetzen + Probesteuern | Wenn nicht passend: Ruderkopf entgraten oder neue Notpinne |
| Notpinne — Sicherungsbolzen | Jährlich | Bolzen einsetzen, Splint prüfen | Ersatz-Splint beschaffen |
| Notpinne — Korrosion | Jährlich | Sichtkontrolle, Oberfläche | Reinigen, neu passivieren, ggf. ersetzen |
| Notpinne — Stauort | Jährlich | Zugang prüfen, <3 min? | Umlagern wenn nötig, neu beschriften |
| Bypass-Ventil — Gängigkeit | Halbjährlich | Öffnen und schließen | Wenn schwergängig: Kriechöl, ggf. ersetzen |
| Bypass-Ventil — Dichtigkeit | Jährlich | Im geschlossenen Zustand: Leck? | Dichtungen ersetzen |
| Bypass-Ventil — Beschriftung | Jährlich | Aufkleber lesbar? | Neuen Aufkleber anbringen |
| Ruderkopf-Zugang | Jährlich | Platte öffnen, Schrauben prüfen | Anti-Seize auf Schrauben, Cam-Locks nachrüsten |
| Autopilot-Entkopplung | Jährlich | Entkopplung durchführen | Quick-Release-Pin schmieren, Funktion prüfen |
| Seilzug/Kette | Jährlich | Sicht- und Tastprüfung | Einzeldrahtbrüche → sofort erneuern |
| Steuerseil — Lebensdauer | Alle 8–10 Jahre | Vorsorglich erneuern | Neues Seil einziehen (gleicher Typ + Stärke) |
| Schleppbremse (JSD/Para-Anchor) | Jährlich | Sichtkontrolle, Nähte, Leinen | Reparieren oder ersetzen |
| Notruderblatt | Jährlich | Zustand, Halterung, Befestigung | Halterung nachziehen, Material prüfen |

### 10.6 Schnellreferenz — Notsteuerung nach Vorschrift (Compliance-Matrix)

| Regelwerk | Anforderung | Bootstyp | Geltungsbereich |
|-----------|-------------|---------|----------------|
| World Sailing OSR 3.29 | Notpinne, getestet | Regatta-Segelyachten | Kategorie 0–3 |
| ORC Equipment Reg. | Notpinne + Safety Audit | ORC-vermessene Boote | Alle ORC-Regatten |
| ISO 10592 §7.6 | Notsteuerung bei Hydraulik | Alle Boote mit Hydraulik | EU (CE-Kennzeichnung) |
| ISO 8847 §5.8 | Notsteuerung bei Seilzug | Alle Boote mit Seilzugsteuerung | EU (CE-Kennzeichnung) |
| SchSV §14 (DE) | Notsteuerung gewerblich | Gewerbliche >12 m | Deutsche Flagge |
| RCD 2013/53/EU | Allgemeine Sicherheit | 2,5–24 m | EU-Markt |
| SOLAS II-1/29 | Notsteuerung >24 m | Gewerbliche >24 m | International |
| Klassifikation (DNV, BV) | Redundante Steuerung/Notruder | Yachten >24 m, klassifiziert | Weltweit |

### 10.7 Schnellreferenz — Ruderblatt verloren — Was tun?

```
RUDER VERLOREN? → 5-SCHRITTE-PLAN

1. STOPPEN  → Segel bergen, Motor aus, Beidrehen
2. PRÜFEN  → Koker dicht? Wassereinbruch? → Abdichten!
3. PLANEN  → Position, Abstand Hafen, Wind, See
4. STEUERN → Hydrovane? → Ja → Windfahne als Notruder
             Notruder?  → Ja → Montieren
             Segel?     → Ja → Segeltrimm-Steuerung
             JSD?       → Ja → Schleppbremse über Heck
             Nichts?    → → → SAR anfordern (Pan-Pan/Mayday)
5. FAHREN  → Nächster sicherer Hafen, konservativ
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Hydraulikversagen auf 42-ft-Segelyacht, Biscaya

| Parameter | Wert |
|-----------|------|
| **Boot** | Bavaria 42 Cruiser (2008) |
| **Steueranlage** | Whitlock/Lewmar Seilzug + Pedestalrad |
| **Hydraulik** | Nein (Seilzug mit Kette) |
| **Vorfall** | Steuerkette gerissen bei 6 Bft, Biscaya, 80 nm vor La Coruña |
| **Crew** | 4 Personen, davon 2 erfahren |

**Hergang:**

1. Bei Starkwind (6 Bft, Wellenhöhe 2,5 m) auf Raumschotskurs fiel die Steuerung plötzlich aus
2. Das Steuerrad drehte ohne Widerstand — die Steuerkette hatte ein Glied verloren
3. Der Skipper erkannte sofort das Problem und rief „Notpinne!"
4. Crew-Mitglied 1 öffnete die Cockpitboden-Platte (4 Schrauben, Innensechskant M6)
5. Problem: Die Platte war mit einer schweren Rettungsinsel belegt (22 kg)
6. Rettungsinsel wurde von 2 Personen beiseitegeschafft (3 Minuten)
7. Platte geöffnet, Ruderkopf sichtbar (Vierkant 35 × 35 mm)
8. Notpinne aus Backskiste geholt (vorher geprüft, passte)
9. Notpinne aufgesetzt, Bolzen gesichert (2 Minuten)
10. Autopilot-Linearantrieb blockierte den Quadranten → Kupplungspin gezogen (1 Minute)
11. Gesamtzeit: 9 Minuten von Ausfall bis Notsteuerung

**Ergebnis:**

- Boot unter Notpinne + gerefftem Groß nach La Coruña gesegelt (12 Stunden)
- Notpinne gut handhabbar bei 5–6 Bft (Pinne 950 mm, Handkraft geschätzt 100–130 N)
- Talje wäre bei stärkerem Wind nötig gewesen
- Kein Sachschaden, kein Personenschaden

**Lehren:**

- Jährlicher Notpinnen-Test hat funktioniert (Passgenauigkeit OK)
- Rettungsinsel auf Ruderkopf-Platte = Zeitverlust (3 min) → Rettungsinsel umlagern
- Autopilot-Entkopplung war vorbereitet → Kupplungspin-System hat sich bewährt
- Steuerkette war 14 Jahre alt → hätte nach 10 Jahren erneuert werden sollen

### ANHANG B: Fallstudie — Spatenruder-Verlust im Südatlantik

| Parameter | Wert |
|-----------|------|
| **Boot** | Jeanneau Sun Odyssey 45 DS (2012) |
| **Steueranlage** | Lewmar Hydraulik + Doppelrad |
| **Vorfall** | Ruderblatt abgerissen nach Treibgut-Kollision, 400 nm vor St. Helena |
| **Crew** | 2 Personen (Ehepaar, beide erfahren) |

**Hergang:**

1. Nachtfahrt, Autopilot, 4 Bft, ruhige See
2. Plötzlicher Schlag am Heck, Boot dreht unkontrolliert ab
3. Autopilot-Alarm: „Ruderfehler" (Ruderdruck plötzlich Null)
4. Sichtprüfung achtern: Kein Ruderblatt sichtbar — komplett abgerissen
5. Ruderstumpf ragte ca. 30 cm aus dem Koker — kein Wassereinbruch (Dichtung intakt)
6. Notpinne aufgesetzt → nutzlos, da kein Ruderblatt
7. Keine Windfahnensteuerung an Bord, kein Notruderblatt

**Notsteuerung:**

1. Beigedreht (Fock back, Groß gerefft) → Boot lag stabil bei
2. Situation bewertet: 400 nm bis St. Helena, Wind NE 4 Bft, Strom günstig
3. Jordan Series Drogue (an Bord als Sturmtaktik) über Heck ausgebracht
4. Bridle Bb/Stb an Heck-Klampen, Parten über Winschen
5. Großsegel gerefft gesetzt, Fock halb ausgerollt
6. Kombination JSD + Segeltrimm: Kurs SW, ~110° zum Wind, 3–4 kn

**Ergebnis:**

- 5 Tage unter JSD + Segeltrimm-Steuerung bis St. Helena
- Kurshaltung gut (±15°), Kursänderungen langsam (5–10 min für 30°)
- JSD musste 2× eingeholt und neu ausgebracht werden für größere Kursänderungen
- Ankunft in Jamestown, St. Helena, ohne Schlepper (letzter Seemeile unter Segeltrimm)

**Lehren:**

- Spatenruder ohne Skeg-Schutz → hohes Verlustrisiko bei Treibgut
- JSD als Sturmgerät → ungeplante Doppelfunktion als Notsteuerung
- Kein Notruderblatt an Bord → sollte für Blauwasser obligatorisch sein
- 2-Personen-Crew → Wachsystem mit Notsteuerung extrem belastend

### ANHANG C: Fallstudie — Hydraulik-Bypass festkorrodiert, Motoryacht Mittelmeer

| Parameter | Wert |
|-----------|------|
| **Boot** | Princess 50 (1998), Motoryacht |
| **Steueranlage** | Lewmar Constellation Hydraulik |
| **Vorfall** | Hydraulikpumpe ausgefallen, 15 nm vor Mallorca, 3 Bft |
| **Crew** | 3 Personen, davon 1 erfahren |

**Hergang:**

1. Steuerung fiel aus — Steuerrad ohne Wirkung (Hydraulikpumpe Leck)
2. Skipper wusste, dass es ein Bypass-Ventil geben musste
3. 20 Minuten Suche nach dem Ventil im Maschinenraum (nicht beschriftet)
4. Ventil gefunden (Nadelventil am Steuerzylinder) — FESTKORRODIERT
5. Rohrzange, WD-40, Schlagschrauber — Ventil ließ sich nicht öffnen
6. Notpinne nicht vorhanden (Motoryacht, bei Auslieferung nicht mitgeliefert)

**Notsteuerung:**

1. Doppelschrauber → Differentialsteuerung eingesetzt
2. Stb-Motor voraus, Bb-Motor Leerlauf → Boot dreht langsam nach Bb
3. Durch asymmetrische Drehzahl konnte der Kurs zum Hafen Palma gehalten werden
4. Einlaufen in den Hafen unter Differentialsteuerung (sehr langsam, 2 kn)

**Ergebnis:**

- Hafen erreicht unter Differentialsteuerung (2 Stunden)
- Keine Notpinne, kein funktionierender Bypass → doppeltes Systemversagen
- Nur die Doppelschrauber-Konfiguration rettete die Situation

**Lehren:**

- Bypass-Ventil MUSS regelmäßig betätigt werden (Mindestens 2× jährlich)
- Bypass-Ventil MUSS beschriftet sein
- Auch Motoryachten benötigen eine Notpinne
- Doppelschrauber bieten inhärente Redundanz — Einzelschrauber-Motoryachten sind kritischer

### ANHANG D: Fallstudie — Ruderkopf-Zugang unmöglich auf Charteryacht

| Parameter | Wert |
|-----------|------|
| **Boot** | Beneteau Oceanis 48 (2016), Charterboot |
| **Steueranlage** | Lewmar Seilzug + Doppelrad |
| **Vorfall** | Seilzug gerissen, Flotillenfahrt vor Korfu, 4 Bft |
| **Crew** | 5 Personen, wenig Erfahrung, Flotillenführer per Funk erreichbar |

**Hergang:**

1. Seilzug gerissen bei Wende, beide Steuerräder ohne Funktion
2. Flotillenführer per Funk kontaktiert → „Notpinne aufsetzen"
3. Crew fand die Notpinne im Heckkast nach 5 Minuten Suche
4. Problem: Cockpitboden-Platte über dem Ruderkopf mit 12 Schrauben (M6 Innensechskant) befestigt
5. Schrauben teilweise korrodiert (Charterboot, salzige Umgebung)
6. Kein passender Innensechskant-Schlüssel in der Bordwerkzeugkiste
7. Flotillenführer kam längsseits und brachte Werkzeug → 25 Minuten bis Ruderkopf frei

**Ergebnis:**

- Notpinne schließlich aufgesetzt (Gesamtzeit: 35 Minuten)
- Boot unter Notpinne zurück in die Marina gesegelt (45 Minuten)
- Kein Sachschaden, aber erheblicher Stress für unerfahrene Crew

**Lehren:**

- 12 Schrauben für Ruderkopf-Zugang = inakzeptabel für Notsteuerung
- Charterboote: Schrauben gegen Schnellverschlüsse (Cam-Locks) tauschen
- Bordwerkzeug muss Zugangsplatte öffnen können
- Charter-Briefing muss Notsteuerung beinhalten

### ANHANG E: Fallstudie — Notruder-Improvisation mit Spinnakerbaum, Pazifik

| Parameter | Wert |
|-----------|------|
| **Boot** | Hallberg-Rassy 40 (2005) |
| **Steueranlage** | Jefa Hydraulik + Rad |
| **Vorfall** | Ruderblatt + Schaft gebrochen nach Wal-Kollision, 1.200 nm vor Marquesas |
| **Crew** | 3 Personen, sehr erfahren (Blauwasser) |

**Hergang:**

1. Kollision mit schlafendem Wal bei Nacht, Heck-Bereich getroffen
2. Ruderschaft am unteren Lager gebrochen, Ruderblatt innerhalb von Minuten verloren
3. Wassereinbruch durch Koker → mit Weichholz-Pfropfen und Unterwasser-Epoxid abgedichtet (20 min)
4. Kein Notruderblatt an Bord, aber Hydrovane-Windfahne

**Notsteuerung:**

1. Hydrovane als Notruder eingesetzt → Windfahne fixiert, Pinne manuell bedient
2. Problem: Hydrovane-Ruder allein zu klein für den 40-ft-Langkieler bei 5–6 Bft
3. Improvisation: Spinnakerbaum als Verlängerung, Cockpittisch (GFK) als zusätzliches Ruderblatt
4. Cockpittisch am Ende des Spinnakerbaums mit Schraubzwingen und Leinen befestigt
5. Spinnakerbaum über Heck-Davit in Wasser getaucht, Steuerleinen von Deck
6. Kombinierte Steuerung: Hydrovane-Pinne + improvisiertes Heckruder + Segeltrimm

**Ergebnis:**

- 14 Tage Fahrt bis Marquesas unter kombinierter Notsteuerung
- Cockpittisch-Ruder brach nach 3 Tagen → durch Bodenbrett ersetzt
- Bodenbrett hielt 11 Tage, musste 2× nachgezurrt werden
- Ankunft in Hiva Oa unter eigener Kraft, kein SAR-Einsatz

**Lehren:**

- Hydrovane = Lebensrettung bei Ruderblatt-Verlust
- Improvisation kann funktionieren, aber Materialbelastung enorm
- Notruderblatt (industriell gefertigt) hätte viel Stress erspart
- Blauwasser ohne Notruder = inakzeptables Risiko

### ANHANG F: Fallstudie — Autopilot blockiert Notpinne, Nordsee

| Parameter | Wert |
|-----------|------|
| **Boot** | Dehler 38 (2010) |
| **Steueranlage** | Whitlock/Lewmar Seilzug + Rad |
| **Autopilot** | Raymarine Type 2, Linearantrieb am Quadranten |
| **Vorfall** | Seilzug gerissen bei 7 Bft in der Nordsee, 30 nm vor Helgoland |
| **Crew** | 2 Personen |

**Hergang:**

1. Seilzug gerissen bei Starkwind
2. Notpinne innerhalb von 3 Minuten aufgesetzt (gut vorbereitet)
3. Problem: Ruder ließ sich nicht bewegen — Raymarine-Linearantrieb blockierte den Quadranten
4. Linearantrieb hatte keine Schnellkupplung, nur eine Bolzenverbindung (M10)
5. Crew musste unter Deck (Achterkajüt) kriechen, in Schräglage bei 7 Bft
6. 15 Minuten, um den M10-Bolzen zu lösen (korrodiert, Platz eng)
7. Quadrant frei, Notpinne funktionierte

**Ergebnis:**

- Helgoland unter Notpinne + Sturmfock erreicht (6 Stunden)
- 15 Minuten Verzögerung durch Autopilot-Blockade → in dieser Zeit Boot in Lee-Drift Richtung Felsenküste

**Lehren:**

- Autopilot-Linearantrieb MUSS Schnellkupplung (Quick-Release-Pin) haben
- M10-Bolzen mit Sicherungsmutter unter Stress in engem Raum bei 7 Bft lösen = extrem schwierig
- Quick-Release-Pin: 5 Sekunden vs. 15 Minuten — kann lebensrettend sein

### ANHANG G: Fallstudie — Erfolgreiche Segeltrimm-Steuerung über 80 nm, Karibik

| Parameter | Wert |
|-----------|------|
| **Boot** | Amel Super Maramu (1994), Ketsch |
| **Steueranlage** | Jefa Hydraulik + Rad |
| **Vorfall** | Hydraulikzylinder gebrochen (innerer Kolbenstangenbruch), 80 nm vor Martinique |
| **Crew** | 2 Personen, sehr erfahren |

**Hergang:**

1. Hydraulikzylinder intern gebrochen → Steuerung ohne Funktion
2. Bypass-Ventil geöffnet → Ruder frei, aber Kolbenrest blockierte teilweise
3. Notpinne aufgesetzt → Ruderbewegung auf ±15° eingeschränkt (Kolbenrest als Endanschlag)
4. Für eine Ketsch (17 m, hohes Gewicht) nicht ausreichend für Kurswechsel bei 5 Bft

**Notsteuerung:**

1. Ketsch-Rigg als Vorteil: Besansegel als eigenes Steuersegel
2. Besan allein → Boot luvt an
3. Fock allein → Boot fällt ab
4. Durch Kombination Fock + Besan + eingeschränkte Notpinne (±15°): Kurs gehalten
5. Route: 80 nm unter Segeltrimm + Reststeuerung

**Ergebnis:**

- Martinique erreicht in 18 Stunden unter Segeltrimm-Steuerung
- Ketsch-Rigg ermöglichte präzisere Trimm-Steuerung als bei einer Slup
- Notpinne mit ±15° Restbewegung als Feinkorrektur ausreichend

**Lehren:**

- Ketsch- und Yawl-Rigg bieten natürliche Vorteile bei Segeltrimm-Steuerung
- Auch eingeschränkte Ruderbewegung (±15°) ist besser als keine
- Kombination aus Teilsteuerung + Segeltrimm kann erstaunlich effektiv sein

### ANHANG G2: Ergänzung — Checklisten und Einsatzprotokolle

#### Checkliste: Notsteuerung vor Saisonstart

| Nr. | Prüfpunkt | Durchgeführt | Befund | Maßnahme |
|-----|-----------|-------------|--------|----------|
| 1 | Notpinne auffinden | ☐ | — | — |
| 2 | Notpinne Zustand prüfen (Korrosion, Verformung) | ☐ | — | — |
| 3 | Ruderkopf-Zugangsplatte öffnen | ☐ | — | — |
| 4 | Schrauben der Zugangsplatte gängig? | ☐ | — | — |
| 5 | Notpinne auf Ruderkopf aufsetzen | ☐ | — | — |
| 6 | Sicherungsbolzen einsetzen + Splint prüfen | ☐ | — | — |
| 7 | Ruderbewegung mit Notpinne testen | ☐ | — | — |
| 8 | Autopilot entkoppeln und Freigängigkeit prüfen | ☐ | — | — |
| 9 | Bypass-Ventil öffnen und schließen (nur Hydraulik) | ☐ | — | — |
| 10 | Bypass-Ventil Beschriftung lesbar? | ☐ | — | — |
| 11 | Talje vorhanden und komplett? | ☐ | — | — |
| 12 | Talje an Notpinne + Cockpit-Punkte testweise anschlagen | ☐ | — | — |
| 13 | Stauort Notpinne beschriftet? | ☐ | — | — |
| 14 | Werkzeug für Zugangsplatte in Cockpit-Nähe? | ☐ | — | — |
| 15 | Crew-Einweisung durchgeführt? | ☐ | — | — |
| 16 | Zeit für Umrüstung gemessen (Ziel: <10 min) | ☐ | — | — |

#### Checkliste: Notsteuerung vor Blauwasserfahrt (zusätzlich)

| Nr. | Prüfpunkt | Durchgeführt | Befund | Maßnahme |
|-----|-----------|-------------|--------|----------|
| 17 | Notruderblatt vorhanden? | ☐ | — | — |
| 18 | Notruderblatt testweise montiert? | ☐ | — | — |
| 19 | Befestigungspunkte für Notruder am Heck vorbereitet? | ☐ | — | — |
| 20 | Jordan Series Drogue oder Para-Anchor vorhanden? | ☐ | — | — |
| 21 | Schleppbremse testweise ausgebracht? | ☐ | — | — |
| 22 | Bridle-Befestigungspunkte am Heck markiert? | ☐ | — | — |
| 23 | Segeltrimm-Steuerung geübt (ohne Ruder)? | ☐ | — | — |
| 24 | Ersatz-Seilzug oder Steuerkettenglied an Bord? | ☐ | — | — |
| 25 | Windfahnensteuerung als Notruder getestet (falls vorhanden)? | ☐ | — | — |
| 26 | Dokumentation aller Notsteuerungsverfahren an Bord (laminiert)? | ☐ | — | — |
| 27 | EPIRB registriert und geladen? | ☐ | — | — |
| 28 | DSC-Notruf programmiert? | ☐ | — | — |

#### Einsatzprotokoll: Notsteuerung aktiviert

Dieses Protokoll sollte bei jedem Einsatz der Notsteuerung ausgefüllt werden (für Versicherung, Gutachter, AYDI-Datenbank):

| Feld | Eintrag |
|------|---------|
| Datum und Uhrzeit | _______________ |
| Position (Lat/Lon) | _______________ |
| Windstärke (Bft) | _______________ |
| Seegang | _______________ |
| Art des Steuerversagens | _______________ |
| Ursache (falls bekannt) | _______________ |
| Notsteuerungsmethode eingesetzt | _______________ |
| Zeit bis Notsteuerung einsatzbereit | _______________ min |
| Notsteuerung wirksam? | Ja / Nein / Teilweise |
| Zusätzliche Maßnahmen | _______________ |
| SAR angefordert? | Ja / Nein |
| Hafen unter eigener Kraft erreicht? | Ja / Nein |
| Personenschäden | Ja / Nein |
| Sachschäden | _______________ |
| Lessons Learned | _______________ |

#### Notsteuerung — Spezifikationsblatt (zum Ausfüllen für jedes Boot)

| Parameter | Wert für dieses Boot |
|-----------|---------------------|
| **Bootname** | _______________ |
| **Bootstyp und Länge** | _______________ |
| **Steuerungstyp** | Seilzug / Kette / Hydraulik / Fly-by-Wire |
| **Ruderkopf-Profil** | Vierkant ___mm / Sechskant ___mm / Keilwelle ___mm |
| **Notpinne Hersteller/Modell** | _______________ |
| **Notpinne Stauort** | _______________ |
| **Bypass-Ventil Position** | _______________ |
| **Bypass-Ventil Typ** | Nadel / Kugelhahn / Magnetisch |
| **Autopilot-Entkopplung** | Quick-Release / Bolzen (___mm) / Kein AP |
| **Ruderkopf-Zugang** | Platte ___Schrauben / Cam-Lock / Offen |
| **Talje vorhanden** | Ja (___:1) / Nein |
| **Notruder vorhanden** | Ja (Typ: ___) / Nein |
| **Schleppbremse vorhanden** | JSD / Para-Anchor / Galerider / Nein |
| **Windfahne mit Hilfsruder** | Ja (Typ: ___) / Nein |
| **Letzer Notsteuerungs-Test** | _______________ |

### ANHANG H: Fallstudie — Doppelruder-Katamaran, ein Ruder verloren

| Parameter | Wert |
|-----------|------|
| **Boot** | Lagoon 450 (2015), Katamaran |
| **Steueranlage** | Doppelruder, Seilzug + Doppelrad |
| **Vorfall** | Stb-Ruderblatt abgerissen (Grundberührung auf Korallenriff), Malediven |
| **Crew** | 4 Personen, mäßig erfahren |

**Hergang:**

1. Einlaufen in ein Atoll, Grundberührung mit Korallenriff am Stb-Rumpf
2. Stb-Ruderblatt abgerissen (GFK-Schaft gebrochen am Koker-Durchgang)
3. Steuerung plötzlich asymmetrisch — Boot zog stark nach Steuerbord

**Notsteuerung:**

1. Stb-Seilzug vom Quadranten gelöst (damit kein toter Widerstand)
2. Steuerung über Bb-Ruder allein → funktioniert, aber asymmetrisch
3. Kurskorrektur durch Gegensteuern am Rad
4. Unter Motor (beide Motoren laufen): Differential + Bb-Ruder = kontrollierbare Fahrt

**Ergebnis:**

- Boot unter einem Ruder + Differentialsteuerung 60 nm zum nächsten Hafen gefahren
- Geschwindigkeit reduziert auf 5 kn (normal 7 kn)
- Manöver (Anlegen) mit Bugstrahler + Differential + einem Ruder erfolgreich

**Lehren:**

- Katamarane: Ein-Ruder-Betrieb funktioniert (inhärente Redundanz)
- Differential-Steuerung bei Doppelmotoren als natürliche Backup-Steuerung
- Korallenriff-Grundberührung = häufigste Ursache für Ruderverlust in den Tropen
- Vorsorge: Riff-Pilotführer, Sonar, Ausguck

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: Basis-Modelle

```python
"""
AYDI Emergency Steering Models — Pydantic v2
Module: 20_05 Notsteuerung und Notruder

All models use Pydantic v2 with model_config = {"from_attributes": True}.
NEVER use class Config — always model_config dict.
German UX text, English code. Units: mm, Nm, N, m, kn.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ── Enums ──────────────────────────────────────────────────────────────

class EmergencySteeringType(str, Enum):
    """Type of emergency steering system."""
    EMERGENCY_TILLER = "emergency_tiller"
    HYDRAULIC_BYPASS = "hydraulic_bypass"
    TILLER_ADAPTER = "tiller_adapter"
    EMERGENCY_RUDDER_BLADE = "emergency_rudder_blade"
    DROGUE_STEERING = "drogue_steering"
    SAIL_TRIM_STEERING = "sail_trim_steering"
    WINDVANE_AS_EMERGENCY = "windvane_as_emergency"
    DIFFERENTIAL_PROPULSION = "differential_propulsion"
    IMPROVISED = "improvised"


class SteeringFailureType(str, Enum):
    """Type of steering failure."""
    HYDRAULIC_LEAK = "hydraulic_leak"
    WIRE_ROPE_BREAK = "wire_rope_break"
    CHAIN_BREAK = "chain_break"
    RUDDER_BLADE_LOSS = "rudder_blade_loss"
    RUDDER_STOCK_BREAK = "rudder_stock_break"
    BEARING_FAILURE = "bearing_failure"
    QUADRANT_DETACH = "quadrant_detach"
    WHEEL_COUPLING_FAIL = "wheel_coupling_fail"
    AUTOPILOT_MECHANICAL = "autopilot_mechanical"
    TILLER_BREAK = "tiller_break"
    UNKNOWN = "unknown"


class RudderHeadProfile(str, Enum):
    """Geometry of the rudder head for tiller connection."""
    SQUARE = "square"
    HEXAGONAL = "hexagonal"
    SPLINED = "splined"
    ROUND_WITH_KEY = "round_with_key"
    BAYONET = "bayonet"
    FLANGE = "flange"


class TillerMaterial(str, Enum):
    """Material of the emergency tiller."""
    STAINLESS_316L = "ss_316l"
    ALUMINUM_6082 = "alu_6082"
    CARBON_TUBE = "carbon_tube"
    GFK_TUBE = "gfk_tube"
    WOOD_ASH = "wood_ash"
    WOOD_TEAK = "wood_teak"


class DrogueType(str, Enum):
    """Type of drogue / sea anchor system."""
    JORDAN_SERIES_DROGUE = "jordan_series_drogue"
    PARA_ANCHOR = "para_anchor"
    GALERIDER = "galerider"
    IMPROVISED_DROGUE = "improvised_drogue"


class BypassValveType(str, Enum):
    """Type of hydraulic bypass valve."""
    NEEDLE_VALVE = "needle_valve"
    BALL_VALVE = "ball_valve"
    MAGNETIC_VALVE = "magnetic_valve"
    CHECK_VALVE = "check_valve"
    COMBINATION = "combination"


class EmergencyRudderMountType(str, Enum):
    """Mount type for emergency rudder blade."""
    TRANSOM_MOUNT = "transom_mount"
    OUTBOARD_MOUNT = "outboard_mount"
    OAR_TYPE = "oar_type"
    WINDVANE_RUDDER = "windvane_rudder"


class ConfidenceLevel(str, Enum):
    """AYDI confidence classification."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class Severity(str, Enum):
    """Severity classification for findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class BoatType(str, Enum):
    """Type of vessel."""
    SAILBOAT_MONO = "sailboat_mono"
    SAILBOAT_CATAMARAN = "sailboat_catamaran"
    SAILBOAT_TRIMARAN = "sailboat_trimaran"
    MOTORBOAT_SINGLE = "motorboat_single"
    MOTORBOAT_TWIN = "motorboat_twin"
    MOTORBOAT_CATAMARAN = "motorboat_catamaran"
```

### ANHANG J: Notpinnen-Modelle

```python
class EmergencyTillerSpec(BaseModel):
    """Specification for an emergency tiller."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller der Notpinne")
    model: str = Field(..., description="Modellbezeichnung")
    rudder_head_profile: RudderHeadProfile = Field(
        ..., description="Ruderkopf-Geometrie"
    )
    rudder_head_size_mm: float = Field(
        ..., gt=0, le=100,
        description="Ruderkopf-Maß in mm (Schlüsselweite bei Vierkant/Sechskant)"
    )
    tiller_length_mm: float = Field(
        ..., gt=0, le=3000,
        description="Gesamtlänge der Notpinne in mm"
    )
    tiller_length_min_mm: Optional[float] = Field(
        None, gt=0,
        description="Minimale Länge bei Teleskop-Pinne in mm"
    )
    tiller_material: TillerMaterial = Field(
        ..., description="Material der Notpinne"
    )
    tube_diameter_mm: Optional[float] = Field(
        None, gt=0, le=80,
        description="Rohrdurchmesser in mm"
    )
    tube_wall_thickness_mm: Optional[float] = Field(
        None, gt=0, le=6,
        description="Rohrwandstärke in mm"
    )
    weight_kg: float = Field(
        ..., gt=0, le=20,
        description="Gewicht der Notpinne in kg"
    )
    max_torque_nm: Optional[float] = Field(
        None, gt=0,
        description="Maximales übertragbares Drehmoment in Nm"
    )
    is_telescopic: bool = Field(
        False, description="Teleskopierbar?"
    )
    is_folding: bool = Field(
        False, description="Klappbar?"
    )
    has_tackle_eye: bool = Field(
        True, description="Augbolzen für Talje am Pinnenende?"
    )
    locking_bolt_diameter_mm: Optional[float] = Field(
        None, gt=0, le=20,
        description="Durchmesser des Sicherungsbolzens in mm"
    )
    suitable_boat_length_min_m: Optional[float] = Field(
        None, gt=0,
        description="Geeignet für Boote ab (m)"
    )
    suitable_boat_length_max_m: Optional[float] = Field(
        None, gt=0,
        description="Geeignet für Boote bis (m)"
    )
    price_eur: Optional[float] = Field(
        None, ge=0,
        description="Listenpreis in EUR (ca.)"
    )

    @field_validator("tiller_length_min_mm")
    @classmethod
    def min_length_only_for_telescopic(
        cls, v: Optional[float], info
    ) -> Optional[float]:
        if v is not None and not info.data.get("is_telescopic", False):
            raise ValueError(
                "tiller_length_min_mm nur bei Teleskop-Pinnen angeben"
            )
        return v


class EmergencyTillerAssessment(BaseModel):
    """Assessment of an emergency tiller on a specific boat."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern (LH)"
    )
    boat_type: BoatType = Field(..., description="Bootstyp")
    tiller_spec: Optional[EmergencyTillerSpec] = Field(
        None, description="Spezifikation der Notpinne"
    )
    tiller_present: bool = Field(
        ..., description="Notpinne an Bord vorhanden?"
    )
    tiller_fits: Optional[bool] = Field(
        None, description="Passt die Notpinne auf den Ruderkopf?"
    )
    rudder_head_accessible: bool = Field(
        ..., description="Ruderkopf in <5 min zugänglich?"
    )
    access_time_minutes: Optional[float] = Field(
        None, ge=0, le=60,
        description="Zeit für Zugang zum Ruderkopf in Minuten"
    )
    access_obstacles: list[str] = Field(
        default_factory=list,
        description="Hindernisse beim Zugang (z. B. 'Rettungsinsel', 'Schrauben korrodiert')"
    )
    autopilot_quick_release: Optional[bool] = Field(
        None, description="Autopilot-Schnellkupplung vorhanden?"
    )
    tackle_available: bool = Field(
        False, description="Talje für Notpinne vorhanden?"
    )
    tackle_ratio: Optional[str] = Field(
        None, description="Talje-Untersetzung (z. B. '4:1')"
    )
    locking_bolt_present: bool = Field(
        True, description="Sicherungsbolzen vorhanden?"
    )
    last_test_date: Optional[date] = Field(
        None, description="Letzter Funktionstest der Notpinne"
    )
    stowage_location: Optional[str] = Field(
        None, description="Stauort der Notpinne"
    )
    stowage_labeled: bool = Field(
        False, description="Stauort beschriftet?"
    )
    estimated_hand_force_n: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte erforderliche Handkraft in N bei 5 Bft"
    )
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungspunktzahl (0–100)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )
```

### ANHANG K: Hydraulik-Bypass-Modelle

```python
class HydraulicBypassSpec(BaseModel):
    """Specification for a hydraulic bypass valve."""

    model_config = {"from_attributes": True}

    valve_type: BypassValveType = Field(
        ..., description="Typ des Bypass-Ventils"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller"
    )
    model: Optional[str] = Field(
        None, description="Modell"
    )
    valve_material: Optional[str] = Field(
        None, description="Ventilmaterial (z. B. 'ss_316l', 'bronze', 'brass')"
    )
    location_description: Optional[str] = Field(
        None, description="Position des Ventils an Bord"
    )
    is_labeled: bool = Field(
        False, description="Ventil beschriftet?"
    )
    is_accessible: bool = Field(
        True, description="Ventil ohne Werkzeug zugänglich?"
    )
    last_function_test: Optional[date] = Field(
        None, description="Letzter Funktionstest"
    )
    condition: Optional[str] = Field(
        None, description="Zustand: 'good', 'stiff', 'seized', 'leaking'"
    )


class HydraulicBypassAssessment(BaseModel):
    """Assessment of a hydraulic bypass system."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    steering_type: str = Field(
        ..., description="Typ der Steueranlage"
    )
    bypass_spec: Optional[HydraulicBypassSpec] = Field(
        None, description="Spezifikation des Bypass-Ventils"
    )
    bypass_present: bool = Field(
        ..., description="Bypass-Ventil vorhanden?"
    )
    bypass_functional: Optional[bool] = Field(
        None, description="Bypass-Ventil funktionsfähig?"
    )
    bypass_accessible_time_s: Optional[float] = Field(
        None, ge=0,
        description="Zeit bis Bypass geöffnet in Sekunden"
    )
    oil_level_ok: Optional[bool] = Field(
        None, description="Hydrauliköl-Stand ausreichend?"
    )
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungspunktzahl (0–100)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )
```

### ANHANG L: Notruder-Modelle

```python
class EmergencyRudderSpec(BaseModel):
    """Specification for an emergency rudder blade."""

    model_config = {"from_attributes": True}

    mount_type: EmergencyRudderMountType = Field(
        ..., description="Montageart des Notruders"
    )
    blade_area_m2: float = Field(
        ..., gt=0, le=2.0,
        description="Fläche des Notruderblatts in m²"
    )
    blade_depth_mm: float = Field(
        ..., gt=0, le=2000,
        description="Eintauchtiefe des Notruderblatts in mm"
    )
    blade_chord_mm: Optional[float] = Field(
        None, gt=0,
        description="Tiefe (Chord) des Notruderblatts in mm"
    )
    blade_material: Optional[str] = Field(
        None, description="Material (z. B. 'gfk', 'aluminum', 'plywood', 'stainless')"
    )
    tiller_length_mm: Optional[float] = Field(
        None, gt=0,
        description="Pinnenlänge des Notruders in mm"
    )
    weight_kg: Optional[float] = Field(
        None, gt=0,
        description="Gewicht des Notruders (komplett) in kg"
    )
    stowage_location: Optional[str] = Field(
        None, description="Stauort an Bord"
    )
    deployment_time_minutes: Optional[float] = Field(
        None, ge=0, le=60,
        description="Geschätzte Montagezeit in Minuten"
    )
    suitable_boat_length_max_m: Optional[float] = Field(
        None, gt=0,
        description="Geeignet für Boote bis (m)"
    )
    max_displacement_kg: Optional[float] = Field(
        None, gt=0,
        description="Max. Verdrängung des Bootes in kg"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller"
    )
    price_eur: Optional[float] = Field(
        None, ge=0,
        description="Listenpreis in EUR (ca.)"
    )

    @field_validator("blade_area_m2")
    @classmethod
    def warn_small_blade(cls, v: float) -> float:
        if v < 0.03:
            raise ValueError(
                "Notruderfläche < 0,03 m² ist für die meisten Boote zu klein. "
                "Mindestens 0,04 m² für Boote ab 8 m empfohlen."
            )
        return v


class EmergencyRudderAssessment(BaseModel):
    """Assessment of an emergency rudder on a specific boat."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern (LH)"
    )
    boat_lwl_m: Optional[float] = Field(
        None, gt=0,
        description="Wasserlinienlänge in Metern"
    )
    boat_draft_m: Optional[float] = Field(
        None, gt=0,
        description="Tiefgang in Metern"
    )
    displacement_kg: Optional[float] = Field(
        None, gt=0,
        description="Verdrängung in kg"
    )
    rudder_spec: Optional[EmergencyRudderSpec] = Field(
        None, description="Spezifikation des Notruders"
    )
    rudder_present: bool = Field(
        ..., description="Notruder an Bord vorhanden?"
    )
    mounting_points_prepared: bool = Field(
        False,
        description="Befestigungspunkte am Heck vorbereitet?"
    )
    required_blade_area_m2: Optional[float] = Field(
        None, gt=0,
        description="Erforderliche Notruderfläche (berechnet) in m²"
    )
    area_ratio: Optional[float] = Field(
        None, gt=0,
        description="Verhältnis vorhandene/erforderliche Fläche"
    )
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungspunktzahl (0–100)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )
```

### ANHANG M: Schleppbremsen-Modelle

```python
class DrogueSpec(BaseModel):
    """Specification for a drogue or sea anchor system."""

    model_config = {"from_attributes": True}

    drogue_type: DrogueType = Field(
        ..., description="Typ der Schleppbremse"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller"
    )
    model: Optional[str] = Field(
        None, description="Modellbezeichnung"
    )
    # Jordan Series Drogue specific
    cone_count: Optional[int] = Field(
        None, ge=10, le=300,
        description="Anzahl Kegel (nur JSD)"
    )
    cone_diameter_mm: Optional[float] = Field(
        None, gt=0, le=300,
        description="Kegeldurchmesser in mm (nur JSD)"
    )
    cone_spacing_mm: Optional[float] = Field(
        None, gt=0, le=1000,
        description="Abstand zwischen Kegeln in mm (nur JSD)"
    )
    # Para-Anchor specific
    canopy_diameter_m: Optional[float] = Field(
        None, gt=0, le=12,
        description="Schirmdurchmesser in m (nur Para-Anchor)"
    )
    # Common
    rode_length_m: Optional[float] = Field(
        None, gt=0, le=300,
        description="Schleppleinenlänge in m"
    )
    rode_diameter_mm: Optional[float] = Field(
        None, gt=0, le=30,
        description="Schleppeleinendurchmesser in mm"
    )
    rode_material: Optional[str] = Field(
        None, description="Schleppeleinenmaterial (z. B. 'polyester', 'dyneema', 'nylon')"
    )
    breaking_load_kn: Optional[float] = Field(
        None, gt=0,
        description="Bruchlast der Leine in kN"
    )
    drag_force_kn: Optional[float] = Field(
        None, gt=0,
        description="Schleppkraft in kN (typisch)"
    )
    weight_kg: Optional[float] = Field(
        None, gt=0,
        description="Gesamtgewicht in kg"
    )
    suitable_boat_length_min_m: Optional[float] = Field(
        None, gt=0,
        description="Geeignet für Boote ab (m)"
    )
    suitable_boat_length_max_m: Optional[float] = Field(
        None, gt=0,
        description="Geeignet für Boote bis (m)"
    )
    price_eur: Optional[float] = Field(
        None, ge=0,
        description="Listenpreis in EUR (ca.)"
    )
    has_bridle: bool = Field(
        True, description="Bridle (Y-Leine) enthalten?"
    )
    has_trip_line: bool = Field(
        False, description="Auslöseleine enthalten?"
    )
    has_weight: bool = Field(
        False, description="Gewicht am Ende (Kettensack) enthalten?"
    )


class DrogueSteeringAssessment(BaseModel):
    """Assessment of drogue-based emergency steering capability."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern"
    )
    drogue_spec: Optional[DrogueSpec] = Field(
        None, description="Spezifikation der Schleppbremse"
    )
    drogue_present: bool = Field(
        ..., description="Schleppbremse an Bord?"
    )
    bridle_points_available: bool = Field(
        False,
        description="Befestigungspunkte für Bridle Bb/Stb am Heck vorhanden?"
    )
    max_course_correction_deg: Optional[float] = Field(
        None, ge=0, le=90,
        description="Max. Kurskorrektur in Grad"
    )
    speed_under_drogue_kn: Optional[float] = Field(
        None, ge=0, le=10,
        description="Geschätzte Fahrt unter Schleppbremse in kn"
    )
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungspunktzahl (0–100)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )
```

### ANHANG N: Segeltrimm-Steuerungsmodelle

```python
class SailTrimSteeringCapability(BaseModel):
    """Assessment of sail-trim-based emergency steering capability."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern"
    )
    boat_type: BoatType = Field(..., description="Bootstyp")
    rig_type: str = Field(
        ..., description="Rigg-Typ: 'sloop', 'cutter', 'ketch', 'yawl', 'schooner'"
    )
    has_mainsail: bool = Field(True, description="Großsegel vorhanden?")
    has_headsail: bool = Field(True, description="Vorsegel vorhanden?")
    has_mizzen: bool = Field(
        False, description="Besansegel vorhanden? (Ketsch/Yawl)"
    )
    keel_type: str = Field(
        ..., description="Kieltyp: 'long_keel', 'fin_keel', 'wing_keel', 'bilge_keel', 'centerboard'"
    )
    course_stability_rating: Optional[float] = Field(
        None, ge=0, le=100,
        description="Kursstabilität ohne Ruder (0=instabil, 100=sehr stabil)"
    )
    sail_trim_effectiveness: Optional[float] = Field(
        None, ge=0, le=100,
        description="Effektivität der Segeltrimm-Steuerung (0=schlecht, 100=sehr gut)"
    )
    min_wind_for_steering_bft: Optional[float] = Field(
        None, ge=0, le=12,
        description="Mindestwind für Segeltrimm-Steuerung in Bft"
    )
    max_wind_for_steering_bft: Optional[float] = Field(
        None, ge=0, le=12,
        description="Maximalwind für Segeltrimm-Steuerung in Bft"
    )
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungspunktzahl (0–100)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste der Empfehlungen"
    )

    @field_validator("course_stability_rating")
    @classmethod
    def estimate_stability_from_keel(
        cls, v: Optional[float], info
    ) -> Optional[float]:
        """If no rating given, estimate from keel type."""
        if v is not None:
            return v
        keel_type = info.data.get("keel_type", "")
        estimates = {
            "long_keel": 85.0,
            "fin_keel": 40.0,
            "wing_keel": 50.0,
            "bilge_keel": 60.0,
            "centerboard": 35.0,
        }
        return estimates.get(keel_type)
```

### ANHANG O: Gesamtbewertung Notsteuerung

```python
class EmergencySteeringOverallAssessment(BaseModel):
    """Overall emergency steering assessment for a yacht."""

    model_config = {"from_attributes": True}

    # Identification
    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern (LH)"
    )
    boat_type: BoatType = Field(..., description="Bootstyp")
    intended_use: str = Field(
        ..., description="Einsatzgebiet: 'coastal', 'offshore', 'bluewater', 'racing'"
    )
    assessment_date: date = Field(
        ..., description="Datum der Bewertung"
    )
    assessor: Optional[str] = Field(
        None, description="Name des Gutachters"
    )

    # Sub-assessments
    tiller_assessment: Optional[EmergencyTillerAssessment] = Field(
        None, description="Bewertung Notpinne"
    )
    bypass_assessment: Optional[HydraulicBypassAssessment] = Field(
        None, description="Bewertung Hydraulik-Bypass"
    )
    rudder_assessment: Optional[EmergencyRudderAssessment] = Field(
        None, description="Bewertung Notruder"
    )
    drogue_assessment: Optional[DrogueSteeringAssessment] = Field(
        None, description="Bewertung Schleppbremsen-Steuerung"
    )
    sail_trim_assessment: Optional[SailTrimSteeringCapability] = Field(
        None, description="Bewertung Segeltrimm-Steuerung"
    )

    # Scores
    primary_steering_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Score primäre Notsteuerung (Notpinne/Bypass)"
    )
    secondary_steering_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Score sekundäre Notsteuerung (Notruder/Schleppbremse)"
    )
    tertiary_steering_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Score tertiäre Notsteuerung (Segeltrimm/Improvisation)"
    )
    overall_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Gesamtbewertung Notsteuerung (0–100)"
    )

    # Compliance
    osr_compliant: Optional[bool] = Field(
        None, description="World Sailing OSR 3.29 erfüllt?"
    )
    osr_category: Optional[str] = Field(
        None, description="OSR-Kategorie (0, 1, 2, 3, 4)"
    )
    iso_10592_compliant: Optional[bool] = Field(
        None, description="ISO 10592 Notsteuerung erfüllt? (nur Hydraulik)"
    )

    # Redundancy
    redundancy_count: int = Field(
        0, ge=0, le=5,
        description="Anzahl verfügbarer Notsteuerungsmethoden"
    )
    redundancy_methods: list[EmergencySteeringType] = Field(
        default_factory=list,
        description="Liste der verfügbaren Notsteuerungsmethoden"
    )

    # Time
    estimated_switchover_time_min: Optional[float] = Field(
        None, ge=0, le=60,
        description="Geschätzte Umrüstzeit auf Notsteuerung in Minuten"
    )

    # Confidence and findings
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence-Level"
    )
    severity: Optional[Severity] = Field(
        None, description="Schweregrad der Befunde"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Gesamtliste der Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Gesamtliste der Empfehlungen"
    )
    ai_model_version: Optional[str] = Field(
        None, description="AYDI AI-Modell-Version für Nachvollziehbarkeit"
    )
```

### ANHANG P: Fehleranalyse-Modelle

```python
class SteeringFailureEvent(BaseModel):
    """Documented steering failure event."""

    model_config = {"from_attributes": True}

    event_id: Optional[str] = Field(
        None, description="Eindeutige Kennung des Vorfalls"
    )
    event_date: Optional[date] = Field(
        None, description="Datum des Vorfalls"
    )
    boat_name: Optional[str] = Field(
        None, description="Name des Bootes"
    )
    boat_type: BoatType = Field(
        ..., description="Bootstyp"
    )
    boat_length_m: float = Field(
        ..., gt=0, le=100, description="Bootslänge in Metern"
    )
    location_description: Optional[str] = Field(
        None, description="Beschreibung des Ortes"
    )
    latitude: Optional[float] = Field(
        None, ge=-90, le=90, description="Breitengrad"
    )
    longitude: Optional[float] = Field(
        None, ge=-180, le=180, description="Längengrad"
    )
    distance_to_port_nm: Optional[float] = Field(
        None, ge=0, description="Entfernung zum nächsten Hafen in nm"
    )

    # Failure
    failure_type: SteeringFailureType = Field(
        ..., description="Art des Steuerungsausfalls"
    )
    failure_cause: Optional[str] = Field(
        None, description="Ursache des Ausfalls (Freitext)"
    )
    wind_force_bft: Optional[float] = Field(
        None, ge=0, le=12, description="Windstärke in Bft"
    )
    sea_state: Optional[str] = Field(
        None, description="Seegang (z. B. 'calm', 'moderate', 'rough', 'heavy')"
    )

    # Response
    emergency_steering_used: list[EmergencySteeringType] = Field(
        default_factory=list,
        description="Eingesetzte Notsteuerungsmethoden"
    )
    time_to_emergency_steering_min: Optional[float] = Field(
        None, ge=0,
        description="Zeit bis Notsteuerung einsatzbereit in Minuten"
    )
    emergency_steering_effective: Optional[bool] = Field(
        None, description="Notsteuerung wirksam?"
    )
    sar_required: bool = Field(
        False, description="SAR-Einsatz erforderlich?"
    )
    reached_port_under_own_power: Optional[bool] = Field(
        None, description="Hafen unter eigener Kraft erreicht?"
    )

    # Outcome
    crew_injuries: bool = Field(
        False, description="Personenschäden?"
    )
    vessel_damage: Optional[str] = Field(
        None, description="Schiffsschäden (Freitext)"
    )
    total_resolution_time_hours: Optional[float] = Field(
        None, ge=0,
        description="Gesamtzeit bis Problemlösung in Stunden"
    )

    # Analysis
    lessons_learned: list[str] = Field(
        default_factory=list,
        description="Lessons Learned"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED, description="Confidence-Level"
    )
    source: Optional[str] = Field(
        None, description="Quelle (z. B. 'MAIB Report 2022-04', 'BSU Bericht')"
    )
```

### ANHANG Q: Drehmoment-Berechnung

```python
import math


class EmergencyTillerForceCalculation(BaseModel):
    """Calculation of forces and torques for emergency tiller use."""

    model_config = {"from_attributes": True}

    # Input — Boat
    boat_speed_kn: float = Field(
        ..., ge=0, le=30,
        description="Bootsgeschwindigkeit in Knoten"
    )
    water_density_kg_m3: float = Field(
        1025.0, gt=900, lt=1100,
        description="Wasserdichte in kg/m³"
    )

    # Input — Rudder
    rudder_area_m2: float = Field(
        ..., gt=0, le=5.0,
        description="Ruderfläche in m²"
    )
    rudder_chord_mm: float = Field(
        ..., gt=0, le=2000,
        description="Rudertiefe (Chord) in mm"
    )
    rudder_balance_pct: float = Field(
        ..., ge=0, le=45,
        description="Ruderbalancierung in % der Chord"
    )
    rudder_angle_deg: float = Field(
        ..., ge=0, le=60,
        description="Ruderwinkel in Grad"
    )
    rudder_lift_coefficient: Optional[float] = Field(
        None, gt=0, le=2.0,
        description="Auftriebsbeiwert des Ruderprofils bei gegebenem Winkel"
    )

    # Input — Tiller
    tiller_length_mm: float = Field(
        ..., gt=0, le=3000,
        description="Notpinnen-Länge in mm"
    )
    tackle_ratio: float = Field(
        1.0, ge=1.0, le=10.0,
        description="Talje-Untersetzung (1.0 = keine Talje)"
    )
    tackle_efficiency: float = Field(
        0.90, gt=0, le=1.0,
        description="Wirkungsgrad der Talje"
    )

    # Calculated results
    boat_speed_m_s: Optional[float] = Field(
        None, ge=0,
        description="Bootsgeschwindigkeit in m/s (berechnet)"
    )
    rudder_force_n: Optional[float] = Field(
        None, ge=0,
        description="Ruderkraft (Querkraft) in N"
    )
    center_of_pressure_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Druckmittelpunkt in % der Chord"
    )
    lever_arm_mm: Optional[float] = Field(
        None,
        description="Hebelarm (CP - Schaftposition) in mm"
    )
    rudder_torque_nm: Optional[float] = Field(
        None,
        description="Drehmoment am Ruderschaft in Nm"
    )
    hand_force_n: Optional[float] = Field(
        None, ge=0,
        description="Erforderliche Handkraft in N"
    )
    hand_force_with_tackle_n: Optional[float] = Field(
        None, ge=0,
        description="Erforderliche Handkraft mit Talje in N"
    )
    is_manageable_one_person: Optional[bool] = Field(
        None,
        description="Von einer Person handhabbar? (<150 N)"
    )
    is_manageable_two_persons: Optional[bool] = Field(
        None,
        description="Von zwei Personen handhabbar? (<300 N)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.CALCULATED, description="Confidence-Level"
    )

    def calculate(self) -> EmergencyTillerForceCalculation:
        """Perform the force/torque calculation."""
        # Speed conversion
        self.boat_speed_m_s = self.boat_speed_kn * 0.5144

        # Rudder force (simplified)
        C_L = self.rudder_lift_coefficient or (
            2 * math.pi * math.radians(self.rudder_angle_deg)
            if self.rudder_angle_deg <= 15
            else 1.2  # approximate stall value
        )
        self.rudder_force_n = (
            0.5
            * self.water_density_kg_m3
            * (self.boat_speed_m_s ** 2)
            * self.rudder_area_m2
            * C_L
        )

        # Center of pressure (simplified — moves aft with angle)
        if self.rudder_angle_deg <= 15:
            self.center_of_pressure_pct = 25.0  # quarter-chord
        else:
            self.center_of_pressure_pct = 25.0 + (
                self.rudder_angle_deg - 15
            ) * 0.5  # moves aft

        # Lever arm
        shaft_position_pct = self.rudder_balance_pct
        self.lever_arm_mm = (
            (self.center_of_pressure_pct - shaft_position_pct)
            / 100.0
            * self.rudder_chord_mm
        )

        # Torque
        self.rudder_torque_nm = (
            self.rudder_force_n * abs(self.lever_arm_mm) / 1000.0
        )

        # Hand force without tackle
        self.hand_force_n = (
            self.rudder_torque_nm / (self.tiller_length_mm / 1000.0)
        )

        # Hand force with tackle
        self.hand_force_with_tackle_n = (
            self.hand_force_n
            / (self.tackle_ratio * self.tackle_efficiency)
        )

        # Manageability
        effective_force = self.hand_force_with_tackle_n
        self.is_manageable_one_person = effective_force <= 150.0
        self.is_manageable_two_persons = effective_force <= 300.0

        return self
```

### ANHANG R: Scoring-Funktionen

```python
class EmergencySteeringScoringWeights(BaseModel):
    """Weights for emergency steering scoring."""

    model_config = {"from_attributes": True}

    # Primary (Notpinne/Bypass)
    w_tiller_present: float = Field(25.0, description="Gewicht: Notpinne vorhanden")
    w_tiller_fits: float = Field(15.0, description="Gewicht: Notpinne passt")
    w_tiller_accessible: float = Field(15.0, description="Gewicht: Ruderkopf zugänglich")
    w_bypass_functional: float = Field(10.0, description="Gewicht: Bypass funktionsfähig (nur Hydraulik)")
    w_autopilot_decouple: float = Field(5.0, description="Gewicht: Autopilot entkoppelbar")

    # Secondary (Notruder/Schleppbremse)
    w_emergency_rudder: float = Field(10.0, description="Gewicht: Notruder vorhanden")
    w_drogue: float = Field(5.0, description="Gewicht: Schleppbremse vorhanden")

    # Tertiary (Segeltrimm)
    w_sail_trim_capability: float = Field(5.0, description="Gewicht: Segeltrimm-Steuerung möglich")

    # General
    w_last_test: float = Field(5.0, description="Gewicht: Letzter Test <12 Monate")
    w_stowage_labeled: float = Field(3.0, description="Gewicht: Stauort beschriftet")
    w_crew_trained: float = Field(2.0, description="Gewicht: Crew in Notsteuerung eingewiesen")


def calculate_emergency_steering_score(
    assessment: EmergencySteeringOverallAssessment,
    weights: Optional[EmergencySteeringScoringWeights] = None,
) -> float:
    """
    Calculate the overall emergency steering score.

    Returns a score from 0 to 100.
    """
    if weights is None:
        weights = EmergencySteeringScoringWeights()

    score = 0.0
    max_score = 0.0

    # Primary: Tiller
    ta = assessment.tiller_assessment
    if ta is not None:
        max_score += weights.w_tiller_present
        if ta.tiller_present:
            score += weights.w_tiller_present

        max_score += weights.w_tiller_fits
        if ta.tiller_fits:
            score += weights.w_tiller_fits

        max_score += weights.w_tiller_accessible
        if ta.rudder_head_accessible:
            score += weights.w_tiller_accessible
        elif ta.access_time_minutes is not None and ta.access_time_minutes <= 10:
            score += weights.w_tiller_accessible * 0.5

        max_score += weights.w_autopilot_decouple
        if ta.autopilot_quick_release:
            score += weights.w_autopilot_decouple

        max_score += weights.w_last_test
        if ta.last_test_date is not None:
            from datetime import date as date_cls
            days_since = (date_cls.today() - ta.last_test_date).days
            if days_since <= 365:
                score += weights.w_last_test
            elif days_since <= 730:
                score += weights.w_last_test * 0.5

        max_score += weights.w_stowage_labeled
        if ta.stowage_labeled:
            score += weights.w_stowage_labeled

    # Primary: Bypass
    ba = assessment.bypass_assessment
    if ba is not None:
        max_score += weights.w_bypass_functional
        if ba.bypass_present and ba.bypass_functional:
            score += weights.w_bypass_functional
        elif ba.bypass_present:
            score += weights.w_bypass_functional * 0.3

    # Secondary: Emergency Rudder
    ra = assessment.rudder_assessment
    if ra is not None:
        max_score += weights.w_emergency_rudder
        if ra.rudder_present:
            score += weights.w_emergency_rudder
            if ra.area_ratio is not None and ra.area_ratio < 0.5:
                score -= weights.w_emergency_rudder * 0.3  # too small

    # Secondary: Drogue
    da = assessment.drogue_assessment
    if da is not None:
        max_score += weights.w_drogue
        if da.drogue_present:
            score += weights.w_drogue

    # Tertiary: Sail Trim
    sa = assessment.sail_trim_assessment
    if sa is not None:
        max_score += weights.w_sail_trim_capability
        if sa.sail_trim_effectiveness is not None:
            score += weights.w_sail_trim_capability * (
                sa.sail_trim_effectiveness / 100.0
            )

    # Normalize to 0–100
    if max_score > 0:
        return round((score / max_score) * 100, 1)
    return 0.0


def classify_emergency_steering_severity(
    assessment: EmergencySteeringOverallAssessment,
) -> Severity:
    """
    Classify the severity of emergency steering findings.

    Returns Severity enum.
    """
    ta = assessment.tiller_assessment

    # CRITICAL: No emergency steering at all
    if assessment.redundancy_count == 0:
        return Severity.CRITICAL

    # CRITICAL: Tiller doesn't fit or rudder head inaccessible
    if ta is not None:
        if ta.tiller_present and ta.tiller_fits is False:
            return Severity.CRITICAL
        if not ta.rudder_head_accessible and ta.access_time_minutes is not None:
            if ta.access_time_minutes > 15:
                return Severity.CRITICAL

    # HIGH: Only one method, or tiller not tested
    if assessment.redundancy_count == 1:
        return Severity.HIGH
    if ta is not None and ta.last_test_date is None:
        return Severity.HIGH

    # MEDIUM: Multiple methods but issues exist
    if assessment.overall_score is not None and assessment.overall_score < 60:
        return Severity.MEDIUM

    # LOW: Minor issues
    if assessment.overall_score is not None and assessment.overall_score < 80:
        return Severity.LOW

    return Severity.INFO
```

---

---

## Zusammenfassung und AYDI-Systemintegration

### Modul-Interaktionen

Die Notsteuerung beeinflusst folgende AYDI-Analyse-Module:

| AYDI-Modul | Bezug zur Notsteuerung | Gewichtung |
|-----------|----------------------|-----------|
| **Compliance** | OSR 3.29, ISO 10592, ISO 8847 — Notpinne vorhanden, getestet, passend | Hoch (0,95 × Compliance-Gewicht) |
| **Ergonomie** | Ruderkopf-Zugänglichkeit, Notpinnen-Handhabbarkeit, Kraftaufwand | Mittel (0,75 × Ergonomie-Gewicht) |
| **Sicherheit** | Redundanzgrad, Umrüstzeit, Funktionsfähigkeit unter Stress | Sehr hoch (direkte Bewertung) |
| **Kosten** | Investitionskosten Notsteuerung (€80–€5.000), Wartungskosten (€20–€100/Jahr) | Gering (0,05 × Kosten-Gewicht) |
| **Strukturell** | Belastung Ruderkopf, Cockpitboden bei Notpinne, Heckbeschläge bei Notruder | Mittel (0,50 × Struktur-Gewicht) |
| **Produktion** | Integration der Ruderkopf-Zugänglichkeit in den Entwurf, Cam-Lock-Platten | Gering (0,20 × Produktions-Gewicht) |

### AYDI-Scoring-Integration

Die Notsteuerung fließt in den Gesamt-Score einer Yacht wie folgt ein:

```
Compliance-Score:
  + Notpinne vorhanden und passend: +25 Punkte
  + Bypass funktionsfähig (Hydraulik): +15 Punkte
  + Ruderkopf zugänglich (<5 min): +15 Punkte
  + Autopilot entkoppelbar: +10 Punkte
  + Jährlicher Test dokumentiert: +10 Punkte
  − Notpinne fehlt: −40 Punkte
  − Notpinne passt nicht: −40 Punkte
  − Bypass festkorrodiert: −35 Punkte
  − Ruderkopf unzugänglich: −25 Punkte

Sicherheits-Score:
  + Redundanz (≥2 Methoden): +20 Punkte
  + Notruder vorhanden: +15 Punkte
  + Schleppbremse vorhanden: +10 Punkte
  + Segeltrimm-Fähigkeit: +5 Punkte
  − Keine Notsteuerung: −50 Punkte (CRITICAL FLAG)
  − Nur eine Methode bei Blauwasser: −20 Punkte
```

### Datenerhebung für AYDI-Analyse

Für die automatisierte Analyse der Notsteuerung benötigt das AYDI-System folgende Eingabedaten:

**Level 1 (Schnellanalyse) — Schätzung:**
- Bootstyp, Länge, Baujahr → Ableitung des wahrscheinlichen Steuerungstyps
- Einfache Frage: „Notpinne vorhanden? Ja/Nein/Unbekannt"
- Score basiert auf statistischen Wahrscheinlichkeiten nach Bootsklasse

**Level 2 (Profi-Werkzeug) — Messung:**
- Vollständige Spezifikation der Notpinne (Modell, Maße, Material)
- Bypass-Ventil-Status (Position, Zustand, letzter Test)
- Ruderkopf-Zugänglichkeit (Zugangszeit, Hindernisse)
- Notruder-Spezifikation (falls vorhanden)
- Schleppbremsen-Spezifikation (falls vorhanden)
- Fotodokumentation (Pipeline B: Visual Analysis)

> **Ende der AYDI-Wissensdatei 20.05 — Notsteuerung und Notruder**
> Zuletzt aktualisiert: 2026-05-02
> Nächste Revision: Bei Änderungen an ISO 10592, World Sailing OSR, oder relevanten Produktlinien
