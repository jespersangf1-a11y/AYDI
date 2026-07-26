# 23.04 — UKW-Seefunk und Kommunikation: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.04** — Kategorie 23: Elektronik und Navigation
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, IMO/ITU-Dokumente, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-13

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [UKW-Frequenzen und Kanalbelegung](#3-ukw-frequenzen-und-kanalbelegung)
4. [DSC — Digital Selective Calling](#4-dsc--digital-selective-calling)
5. [MMSI — Maritime Mobile Service Identity](#5-mmsi--maritime-mobile-service-identity)
6. [GMDSS — Global Maritime Distress and Safety System](#6-gmdss--global-maritime-distress-and-safety-system)
7. [Satellitenkommunikation](#7-satellitenkommunikation)
8. [AIS-SART und EPIRB](#8-ais-sart-und-epirb)
9. [Antennen für UKW-Seefunk](#9-antennen-für-ukw-seefunk)
10. [Typenübersicht — UKW-Seefunkgeräte](#10-typenübersicht--ukw-seefunkgeräte)
11. [Produktlinien: ICOM](#11-produktlinien-icom)
12. [Produktlinien: Standard Horizon](#12-produktlinien-standard-horizon)
13. [Produktlinien: Raymarine](#13-produktlinien-raymarine)
14. [Produktlinien: Simrad / B&G](#14-produktlinien-simrad--bg)
15. [Produktlinien: Cobra / Uniden](#15-produktlinien-cobra--uniden)
16. [Produktlinien: ACR / McMurdo (EPIRB und SART)](#16-produktlinien-acr--mcmurdo-epirb-und-sart)
17. [Hersteller-Datenbank](#17-hersteller-datenbank)
18. [Fehlerbild-Atlas](#18-fehlerbild-atlas)
19. [Troubleshooting-Entscheidungsbäume](#19-troubleshooting-entscheidungsbäume)
20. [Einbau und Installation](#20-einbau-und-installation)
21. [Wartung und Pflege](#21-wartung-und-pflege)
22. [Normen und Vorschriften](#22-normen-und-vorschriften)
23. [Funkscheine und Lizenzen](#23-funkscheine-und-lizenzen)
24. [Bezugsquellen](#24-bezugsquellen)
25. [Preisvergleich](#25-preisvergleich)
26. [FAQ — Häufige Fragen](#26-faq--häufige-fragen)
27. [Glossar](#27-glossar)
28. [Schnell-Referenz](#28-schnell-referenz)
29. [ANHANG A — Fallstudie: Segelyacht Ostsee Notfallkommunikation](#anhang-a--fallstudie-segelyacht-ostsee-notfallkommunikation)
30. [ANHANG B — Fallstudie: Motoryacht Mittelmeer DSC-Fehlalarm](#anhang-b--fallstudie-motoryacht-mittelmeer-dsc-fehlalarm)
31. [ANHANG C — Fallstudie: Langfahrt-Segelyacht Atlantik EPIRB-Auslösung](#anhang-c--fallstudie-langfahrt-segelyacht-atlantik-epirb-auslösung)
32. [ANHANG D — Fallstudie: Regatta AIS-SART Bergung](#anhang-d--fallstudie-regatta-ais-sart-bergung)
33. [ANHANG E — Fallstudie: Catamaran Karibik Starlink-Integration](#anhang-e--fallstudie-catamaran-karibik-starlink-integration)
34. [ANHANG F — Fallstudie: Charteryacht Kroatien UKW-Antennenproblem](#anhang-f--fallstudie-charteryacht-kroatien-ukw-antennenproblem)
35. [ANHANG G — Fallstudie: Superyacht Iridium-GMDSS-Redundanz](#anhang-g--fallstudie-superyacht-iridium-gmdss-redundanz)
36. [ANHANG H — Fallstudie: Klassische Yacht Nachrüstung DSC-fähiges Funkgerät](#anhang-h--fallstudie-klassische-yacht-nachrüstung-dsc-fähiges-funkgerät)
37. [ANHANG I — AYDI-Integration (Pydantic-Modelle)](#anhang-i--aydi-integration-pydantic-modelle)
38. [ANHANG J — AYDI Bewertungsschema für UKW-Seefunk](#anhang-j--aydi-bewertungsschema-für-ukw-seefunk)
39. [ANHANG K — Frequenztabelle vollständig](#anhang-k--frequenztabelle-vollständig)
40. [ANHANG L — Antennen-Berechnungsformeln](#anhang-l--antennen-berechnungsformeln)
41. [ANHANG M — DSC-Nachrichtenformate und Codes](#anhang-m--dsc-nachrichtenformate-und-codes)
42. [ANHANG N — GMDSS-Ausrüstungspflichten nach Seegebiet](#anhang-n--gmdss-ausrüstungspflichten-nach-seegebiet)
43. [ANHANG O — Confidence-Mapping](#anhang-o--confidence-mapping)
44. [ANHANG P — Kompatibilitätsmatrix Funkgeräte und Zubehör](#anhang-p--kompatibilitätsmatrix-funkgeräte-und-zubehör)
45. [ANHANG Q — Visuelle Erkennung von Funkgeräte-Defekten](#anhang-q--visuelle-erkennung-von-funkgeräte-defekten)
46. [ANHANG R — Kostenmodelle und Parametrische Kalkulation](#anhang-r--kostenmodelle-und-parametrische-kalkulation)

---

## 1. Einführung

### 1.1 Bedeutung der Funkkommunikation auf See

UKW-Seefunk (VHF Maritime Radio) ist das primäre Kommunikationsmittel auf See und bildet das Rückgrat des maritimen Sicherheitssystems. Für jede Yacht — ob 7m Jollenkreuzer oder 30m Motoryacht — ist ein funktionierendes Seefunkgerät die wichtigste Sicherheitsausrüstung an Bord, noch vor Rettungsweste und Rettungsinsel.

**Warum UKW-Seefunk unverzichtbar ist:**
- Einziges universelles Echtzeit-Kommunikationsmittel zwischen Schiffen und Küstenfunkstellen
- Notrufe (Mayday, Pan-Pan, Sécurité) erreichen alle Schiffe im Empfangsbereich gleichzeitig
- DSC-Notruf (Digital Selective Calling) alarmiert automatisch alle GMDSS-Stationen
- Wetterberichte, Navigationswarnchrichten (NAVTEX) und MSI (Maritime Safety Information)
- Hafenkommunikation, Schleusenkoordination, Brückenöffnungen
- Schiff-zu-Schiff-Abstimmung (Ausweichen, Manöverkoordination)
- Küstenwache, SAR (Search and Rescue), Seenotrettung

### 1.2 Rechtlicher Rahmen

In Deutschland ist der UKW-Seefunk durch folgende Regelwerke definiert:

| Rechtsgrundlage | Inhalt | Relevanz |
|-----------------|--------|----------|
| SchSV (Schiffssicherheitsverordnung) | Ausrüstungspflicht | Gewerbliche Schiffe, Sportboote >12m auf See |
| FüFunkZeugnisV | Funkzeugnisverordnung | SRC/LRC/UBI Pflicht für Betrieb |
| Frequenzzuteilungsverordnung | Frequenznutzung | BNetzA-Genehmigung |
| SOLAS Kapitel IV | GMDSS-Pflicht | International, ab 300 BRZ |
| EU-Funkanlagenrichtlinie 2014/53/EU | Gerätezulassung | CE-Kennzeichnung für Funkgeräte |
| ITU Radio Regulations | Internationale Frequenzzuordnung | Weltweit bindend |

**Sportboote in Deutschland:**
- UBI (UKW-Sprechfunkzeugnis für den Binnenschifffahrtsfunk) für Binnengewässer
- SRC (Short Range Certificate) für Seeschifffahrt — UKW mit DSC
- LRC (Long Range Certificate) für Seeschifffahrt — UKW + GW/KW + Inmarsat

### 1.3 Abgrenzung zu anderen Wissensdateien

| Thema | Wissensdatei | Schnittstelle |
|-------|-------------|--------------|
| AIS-Transponder (Verkehrsüberwachung) | 23_03_radar_ais.md | AIS-Antenne oft geteilt mit UKW |
| Kartenplotter (Anzeige) | 23_02_kartenplotter.md | NMEA-Verbindung für DSC-Position |
| Instrumente (GPS, Windmesser) | 23_05_instrumente_sensoren.md | GPS-Input für DSC-Positionsmeldung |
| Antennen (allgemein) | Diese Datei, Kap. 9 | UKW-spezifisch hier, Radar in 23_03 |

---

## 2. Grundlagen und Theorie

### 2.1 Elektromagnetische Grundlagen

UKW-Seefunk operiert im VHF-Band (Very High Frequency) zwischen 156,000 MHz und 174,000 MHz. Die physikalischen Eigenschaften dieses Frequenzbandes bestimmen die Funktechnologie:

**Ausbreitungseigenschaften VHF maritim:**
- **Quasi-optische Ausbreitung** — UKW-Wellen folgen der Sichtlinie (Line of Sight, LOS)
- **Keine Reflexion an der Ionosphäre** — im Gegensatz zu Kurzwelle (HF)
- **Leichte Beugung über den Horizont** — ca. 10-15% über optische Sichtweite hinaus
- **Reflexion an Wasseroberfläche** — erzeugt Mehrwegeausbreitung (Multipath)
- **Absorption durch Regen** — vernachlässigbar bei UKW-Frequenzen
- **Absorption durch Salzwassergischt** — messbar bei Sturm, aber gering

**Reichweitenberechnung (vereinfacht):**

Die theoretische UKW-Reichweite ist primär durch die Antennenhöhe bestimmt:

```
Reichweite (nm) = 2,23 × (√h₁ + √h₂)

h₁ = Antennenhöhe Sender (m über Wasser)
h₂ = Antennenhöhe Empfänger (m über Wasser)
```

| Antennenhöhe Boot 1 | Antennenhöhe Boot 2 | Theoretische Reichweite |
|---------------------|---------------------|------------------------|
| 3m (Motorboot) | 3m (Motorboot) | 7,7 nm |
| 3m (Motorboot) | 15m (Segelboot Mast) | 12,5 nm |
| 15m (Mast) | 15m (Mast) | 17,3 nm |
| 15m (Mast) | 50m (Küstenfunkstelle) | 24,5 nm |
| 15m (Mast) | 100m (Küstenfunkstelle Berg) | 31,0 nm |
| 3m (Motorboot) | 100m (Küstenfunkstelle Berg) | 26,2 nm |
| 25m (Superyacht Mast) | 100m (Küstenfunkstelle) | 33,4 nm |

**Praktische Reichweite:**
- Typisch 20–30 nm (Yacht zu Küstenfunkstelle mit erhöhter Antenne)
- Typisch 10–15 nm (Yacht zu Yacht)
- Bis 60 nm bei optimalen Bedingungen (z.B. Mast 20m + Küstenfunkstelle 200m)
- Unter 5 nm bei niedriger Antenne und Seegang
(Confidence: documented)

### 2.2 Modulationsverfahren

**FM (Frequenzmodulation) — Standard für UKW-Seefunk:**
- Nennbandbreite: 25 kHz (breitbandig) oder 12,5 kHz (schmalbandig)
- Hub: ±5 kHz (25 kHz Kanal) bzw. ±2,5 kHz (12,5 kHz Kanal)
- Kanalraster: 25 kHz (historisch), zunehmend 12,5 kHz
- FM bietet guten Rauschabstand und Capture-Effekt (stärkeres Signal unterdrückt schwächeres)

**DSC (Digital Selective Calling) — auf Kanal 70:**
- Modulationsverfahren: FSK (Frequency Shift Keying), Minimum Shift Keying (MSK)
- Datenrate: 1200 Bit/s
- Übertragungszeit Notruf: ca. 6,5 Sekunden (440 Bit)
- Fehlerkorrektur: 10-Bit-Fehlererkennung, Wiederholung jedes Symbols
- Codierung nach ITU-R M.493

**AIS (Automatic Identification System) — auf Kanälen 87B und 88B:**
- Modulationsverfahren: GMSK (Gaussian Minimum Shift Keying)
- Datenrate: 9.600 Bit/s
- TDMA (Time Division Multiple Access) — Zeitmultiplex
- Relevanz: AIS-Antenne oft identisch mit UKW-Antenne oder Splitter

### 2.3 Sendeleistung und Regelung

| Leistungsklasse | Typische Nutzung | Sendeleistung | Reichweite |
|-----------------|-----------------|---------------|-----------|
| Low Power (L) | Hafen, Ankerbucht | 1 Watt | 1–3 nm |
| High Power (H) | See, Standard | 25 Watt (fest) / 6 Watt (Hand) | 10–30 nm |
| DSC Kanal 70 | Notruf/Routine | 25 Watt (automatisch) | 20–30 nm |
| AIS | Transponderbetrieb | 2 Watt (Klasse B) / 12,5 Watt (Klasse A) | 15–25 nm |

**Gesetzliche Regelung (Deutschland):**
- Maximale Sendeleistung UKW Seefunk: 25 Watt
- Handsprechfunkgeräte: maximal 6 Watt (meist 5 Watt)
- Pflicht zur Nutzung der geringstmöglichen Leistung
- Low-Power-Pflicht in Häfen und Schleusen

### 2.4 Simplex, Duplex und Semi-Duplex

| Betriebsart | Beschreibung | Kanäle | Anwendung |
|-------------|-------------|--------|-----------|
| Simplex | Senden und Empfangen auf gleicher Frequenz | Kanal 16, 6, 8, 9, 10, 13, 67, 72, 77 | Schiff-zu-Schiff |
| Duplex | Senden und Empfangen auf verschiedenen Frequenzen | Kanal 1–5, 7, 18–22, 23, 60–66, 78–86 | Schiff-zu-Küste (Telefonie) |
| Semi-Duplex | Boot sendet auf einer, empfängt auf anderer Frequenz | Verschiedene | Küstenfunkstellenbetrieb |

**Hinweis:** Moderne Funkgeräte schalten automatisch zwischen den Betriebsarten um. Für den Nutzer ist dies transparent — Kanalwahl genügt.

---

## 3. UKW-Frequenzen und Kanalbelegung

### 3.1 Wichtigste Kanäle im Überblick

| Kanal | Frequenz (MHz) | Zweck | Pflicht-Hörwache | Anmerkung |
|-------|---------------|-------|------------------|-----------|
| **16** | 156,800 | **Not-, Dringlichkeits- und Sicherheitskanal** | **JA** | International |
| **70** | 156,525 | **DSC (Digital Selective Calling)** | **JA (automatisch)** | Nur digitale Daten |
| 06 | 156,300 | Schiff-zu-Schiff (intership) | Nein | SAR-Koordination |
| 08 | 156,400 | Schiff-zu-Schiff (intership) | Nein | Kommerziell |
| 09 | 156,450 | Hafen-/Revierfunk, Hilfsruf | Nein | Anrufkanal BRD Küste |
| 10 | 156,500 | Revier, Schleuse | Nein | Regional verschieden |
| 12 | 156,600 | Hafenverkehr (VTS) | Nein | Hafenanlauf |
| 13 | 156,650 | Brücke-zu-Brücke (Sicherheit) | Nein | Manöverkommunikation |
| 14 | 156,700 | Hafenverkehr (VTS) | Nein | Hafenanlauf |
| 67 | 156,375 | Küstenwache UK | Nein | SAR-Koordination UK |
| 72 | 156,625 | Schiff-zu-Schiff | Nein | Beliebter Arbeitskanal |
| 77 | 156,875 | Schiff-zu-Schiff | Nein | Beliebter Arbeitskanal |
| 87B | 161,975 | AIS 1 | — | Automatisch |
| 88B | 162,025 | AIS 2 | — | Automatisch |

### 3.2 Deutsche Besonderheiten

| Kanal | Zweck in Deutschland | Anmerkung |
|-------|---------------------|-----------|
| 09 | Anrufkanal Küste (häufig genutzt) | Nicht international standardisiert |
| 10 | Revierzentrale (z.B. Kiel, Brunsbüttel) | VTS Kiel Canal |
| 11 | Revierzentrale | Abhängig von Region |
| 68 | DSC-Arbeitskanal nach Kontakt auf 16 | Beliebter Wechselkanal |
| 69 | Verkehrsberatung, Lotsen | Regional |
| 80 | Marina-Kanal (europaweit verbreitet) | Hafenmeister |

### 3.3 Kanalbelegung nach Region

**Nordsee / Deutsche Bucht:**
- Kanal 16: Notruf/Sicherheit
- Kanal 01, 02, 03, 04: Deutsche Küstenfunkstelle (DP07 Bremen Rescue)
- Kanal 23, 83: MRCC Bremen (Seenotleitung)
- Kanal 10, 11, 12, 13, 14: VTS (Elbe, Weser, Jade, NOK)

**Ostsee:**
- Kanal 16: Notruf/Sicherheit
- Kanal 01, 02, 03: Deutsche Küstenfunkstelle
- Kanal 67: SAR-Koordination (in einigen Gebieten)
- Kanal 10, 11: VTS (Kieler Förde, Travemünde, Rostock)

**Mittelmeer:**
- Kanal 16: Notruf/Sicherheit
- Kanal 09: Anruf (verbreitet in FR, IT, ES, HR)
- Kanal 10, 12: VTS in Häfen
- Kanal 73, 74: Regionale Küstenfunkstellen
- Kanal 80: Marina-Kanal (nahezu universell im Mittelmeer)

**Karibik / US-Gewässer:**
- Kanal 16: Notruf/Sicherheit
- Kanal 09: Sekundärer Anrufkanal (USCG empfiehlt)
- Kanal 22A: USCG Information (Wetter, Warnungen)
- Kanal 68, 69, 71, 72, 78A: Beliebte Arbeitskanäle
- Kanal 13: Brücke-zu-Brücke (gesetzlich vorgeschrieben in US-Gewässern)

### 3.4 Wetterfunk-Kanäle

| Dienst | Kanal / Frequenz | Region | Sendezeiten |
|--------|-----------------|--------|-------------|
| NOAA Weather Radio | WX1–WX10 (162,400–162,550 MHz) | USA, Kanada | Kontinuierlich |
| Coast Guard Wetterbericht | Kanal 16 → Verweis | Weltweit | Nach Fahrplan |
| DP07 (Bremen Rescue) | Kanal 01, 02, 03 | Deutsche Gewässer | 0745, 1245, 1845 UTC |
| CROSS (FR) | Kanal 79 | Frankreich | Nach Fahrplan |
| Coastguard (UK) | Kanal 10, 23, 84, 86 | UK | Nach Fahrplan |
| NAVTEX | 518 kHz / 490 kHz (nicht UKW!) | International | Automatisch |

---

## 4. DSC — Digital Selective Calling

### 4.1 Grundprinzip

DSC (Digital Selective Calling) ist ein digitales Anrufsystem auf UKW-Kanal 70, das Schiffe und Küstenfunkstellen automatisch alarmieren kann. Seit dem 1. Februar 1999 ist DSC integraler Bestandteil des GMDSS (Global Maritime Distress and Safety System).

**Funktionsweise:**
1. Funkgerät sendet automatisch digitalen Datenburst auf Kanal 70 (156,525 MHz)
2. Datenburst enthält: MMSI Sender, MMSI Empfänger (oder ALL SHIPS), Kategorie, Natur des Notfalls, Position, Zeit
3. Alle DSC-fähigen Geräte im Empfangsbereich decodieren die Nachricht
4. Bei Notruf (Distress): akustischer und visueller Alarm auf allen empfangenden Geräten
5. Empfänger bestätigt mit DSC-Acknowledgement auf Kanal 70
6. Sprechfunkverkehr wechselt auf Kanal 16 oder anderen zugewiesenen Kanal

### 4.2 DSC-Nachrichtenkategorien

| Kategorie | Priorität | Auslösung | Empfänger | Zweck |
|-----------|-----------|-----------|-----------|-------|
| **Distress** (Seenot) | Höchste | Rote Taste (3–5 Sek. halten) | Alle Stationen | Seenotalarmierung |
| **Urgency** (Dringlichkeit) | Hoch | Menüauswahl | Alle Stationen | Dringende Sicherheitsmeldung |
| **Safety** (Sicherheit) | Mittel | Menüauswahl | Alle Stationen | Navigationswarnungen |
| **Routine** | Normal | Menüauswahl | Einzelstation (MMSI) | Normaler Anruf |
| **Group** | Normal | Menüauswahl | Gruppe (Gruppen-MMSI) | Gruppenruf |

### 4.3 DSC-Notruf (Distress Alert)

**Auslösung:**
1. Schutzkappe über Distress-Taste öffnen
2. Distress-Taste 3–5 Sekunden gedrückt halten (je nach Gerät)
3. Gerät sendet automatisch: MMSI, Position (GPS), Zeit, Art des Notfalls (wenn vorgewählt)
4. Automatische Wiederholung alle 3,5–4,5 Minuten bis Bestätigung empfangen

**Art des Notfalls (Nature of Distress):**

| Code | Bezeichnung (EN) | Bezeichnung (DE) | Symbol |
|------|-----------------|------------------|--------|
| 100 | Undesignated | Nicht spezifiziert | — |
| 101 | Fire/Explosion | Feuer/Explosion | 🔥 |
| 102 | Flooding | Wassereinbruch | 💧 |
| 103 | Collision | Kollision | ⚡ |
| 104 | Grounding | Grundberührung | ⚓ |
| 105 | Listing | Krängung | ↗ |
| 106 | Sinking | Sinken | ↓ |
| 107 | Disabled/Adrift | Manövrierunfähig | — |
| 108 | Abandoning | Verlassen des Schiffes | 🚢 |
| 109 | Piracy | Piraterie | — |
| 110 | MOB | Mann über Bord | 🧑 |
| 112 | EPIRB emission | EPIRB ausgelöst | — |

**WICHTIG:** In den meisten Notfällen wird „Undesignated" gesendet, da die Notfallart erst nach dem Distress-Alert per Sprechfunk auf Kanal 16 mitgeteilt wird. Die vorherige Auswahl der Notfallart verzögert die Alarmierung und wird in der Praxis oft übersprungen.

### 4.4 DSC-Routine-Ruf

**Ablauf eines normalen DSC-Anrufs:**
1. MMSI der Gegenstation eingeben
2. Arbeitskanal vorschlagen (z.B. Kanal 72)
3. DSC-Ruf senden (Routine-Kategorie)
4. Gegenstation empfängt Anruf mit Kanalvorschlag
5. Gegenstation bestätigt (automatisch oder manuell) → Gerät wechselt auf Arbeitskanal
6. Sprechfunkverbindung auf Arbeitskanal

**Vorteile gegenüber klassischem Anruf auf Kanal 16:**
- Gegenstation wird gezielt gerufen (kein Abhören nötig)
- Automatischer Kanalwechsel
- Entlastung von Kanal 16
- Identifikation über MMSI (eindeutig)

### 4.5 DSC-Klassen

| Klasse | Funktion | Typisches Gerät | Anwendung |
|--------|---------|----------------|-----------|
| Klasse A | Senden + Empfangen Distress, Urgency, Safety, Routine, Group, Area | GMDSS-Schiffsstation | Berufsschifffahrt |
| Klasse D | Senden + Empfangen Distress, Routine (vereinfacht) | Sportboot-UKW | Yachten, Sportboote |
| Klasse E | Senden + Empfangen alle Kategorien (wie A, aber ohne automatische Bestätigung) | Gehobene Sportboot-UKW | Anspruchsvolle Yachten |

**Hinweis:** Die meisten Yacht-Funkgeräte sind Klasse D. Geräte der Klasse E (z.B. ICOM IC-M510) bieten erweiterte Funktionen wie automatische DSC-Bestätigung auf Notrufempfang.

---

## 5. MMSI — Maritime Mobile Service Identity

### 5.1 Aufbau der MMSI

Die MMSI ist eine weltweit eindeutige 9-stellige Identifikationsnummer für Seefunkstellen:

```
Format Schiffsstation:    MID XX XXXX
Format Küstenfunkstelle:  00 MID XXXX
Format Gruppenruf:        0 MID XXXXX
Format SAR-Flugzeug:      111 MID XXX
Format AIS-SART:          970 XX XXXX
Format MOB (AIS):         972 XX XXXX
Format EPIRB:             974 XX XXXX

MID = Maritime Identification Digit (Ländernummer, 3 Stellen)
```

**MID-Nummern ausgewählter Länder:**

| Land | MID | Beispiel-MMSI |
|------|-----|--------------|
| Deutschland | 211 | 211XXXXXX |
| Niederlande | 244, 245, 246 | 244XXXXXX |
| Frankreich | 226, 227, 228 | 226XXXXXX |
| UK | 232, 233, 234, 235 | 232XXXXXX |
| Italien | 247 | 247XXXXXX |
| Kroatien | 238 | 238XXXXXX |
| Griechenland | 237, 239, 240, 241 | 237XXXXXX |
| Schweden | 265, 266 | 265XXXXXX |
| Dänemark | 219, 220 | 219XXXXXX |
| Norwegen | 257, 258, 259 | 257XXXXXX |
| USA | 303, 338, 366, 367, 368, 369 | 366XXXXXX |
| Australien | 503 | 503XXXXXX |

### 5.2 MMSI-Beantragung in Deutschland

**Zuständig:** Bundesnetzagentur (BNetzA), Außenstelle Mülheim/Ruhr

**Voraussetzungen:**
- Gültiger Funkschein (SRC, LRC oder UBI)
- Nachweis über Eigentum oder Verfügungsberechtigung des Bootes
- Internationaler Bootsschein (IBS) oder Registrierung
- Formular „Antrag auf Zuteilung einer MMSI" (BNetzA-Webseite)

**Kosten:** ca. 30-50 EUR (Stand 2026)
**Bearbeitungszeit:** 2-6 Wochen
(Confidence: documented)

### 5.3 MMSI-Programmierung im Funkgerät

**KRITISCH:** Die MMSI kann bei den meisten Geräten nur EINMAL programmiert werden. Eine Neuprogrammierung erfordert:
- Rücksendung an den Hersteller oder autorisierten Händler
- Nachweis der MMSI-Zuteilung
- Kosten: 50-150 EUR (je nach Hersteller)

**Programmiervorgang (typisch ICOM):**
1. Gerät ausschalten
2. Menü → DSC-Einstellungen → MMSI-Eingabe
3. 9-stellige MMSI eingeben
4. Bestätigung: MMSI wird ein zweites Mal eingegeben
5. Gerät bestätigt Programmierung — MMSI ist gesperrt

**Häufige Fehler:**
- MMSI falsch eingegeben → Gerät muss zum Hersteller
- MMSI eines verkauften Bootes im neuen Gerät programmiert → falsche Zuordnung
- Keine MMSI programmiert → DSC-Funktionen nicht nutzbar, Notruf sendet MMSI 000000000 → SAR kann Schiff nicht identifizieren

---

## 6. GMDSS — Global Maritime Distress and Safety System

### 6.1 Überblick und Geschichte

Das GMDSS wurde von der IMO (International Maritime Organization) entwickelt und seit 1992 schrittweise eingeführt. Seit dem 1. Februar 1999 ist es für alle SOLAS-pflichtigen Schiffe (ab 300 BRZ auf internationaler Fahrt) vollständig in Kraft.

**Grundprinzip:** Jedes Schiff soll in der Lage sein, unabhängig von seinem Fahrtgebiet einen Seenotalarm auszulösen, der von einer SAR-Koordinierungsstelle (MRCC) empfangen wird. Das GMDSS basiert auf dem Konzept der Seegebiete.

### 6.2 GMDSS-Seegebiete

| Seegebiet | Definition | Typische Abdeckung | Erforderliche Ausrüstung |
|-----------|-----------|-------------------|------------------------|
| **A1** | Im Bereich mindestens einer UKW-Küstenfunkstelle mit DSC-Hörwache | 20–30 nm von der Küste | UKW mit DSC |
| **A2** | Im Bereich mindestens einer GW-Küstenfunkstelle mit DSC-Hörwache | Ca. 150–400 nm | UKW + GW (MF) mit DSC |
| **A3** | Im Bereich einer Inmarsat-Satellitenabdeckung (ca. 70°N bis 70°S) | Global (außer Polargebiete) | UKW + GW + Inmarsat oder KW |
| **A4** | Außerhalb A1, A2 und A3 | Polargebiete >70°N/S | UKW + GW + KW mit DSC |

### 6.3 GMDSS-Ausrüstung nach Seegebiet (Sportbootrelevant)

**Seegebiet A1 (typisch: Küstensegeln, Ostsee, Nordsee küstennah):**
- UKW-Funkgerät mit DSC (Klasse D oder besser)
- Möglichkeit zum Empfang von MSI (Maritime Safety Information)
- EPIRB 406 MHz (empfohlen, bei SOLAS-Schiffen Pflicht)
- SART oder AIS-SART (bei SOLAS-Schiffen Pflicht)

**Seegebiet A2 (typisch: Nordsee, westliches Mittelmeer):**
- Alles aus A1, plus:
- GW-Funkgerät (MF) mit DSC (2187,5 kHz)
- NAVTEX-Empfänger
- EPIRB 406 MHz (Pflicht bei SOLAS)

**Seegebiet A3 (typisch: Atlantiküberquerung, Weltumseglung bis 70°N/S):**
- Alles aus A1 + A2, plus:
- Inmarsat-C (oder Inmarsat Fleet, Mini-M) ODER
- KW-Funkgerät (HF) mit DSC auf allen DSC-Frequenzen
- EPIRB 406 MHz (Pflicht)
- SART oder AIS-SART

**Seegebiet A4 (typisch: Arktis, Antarktis):**
- Alles aus A1 + A2, plus:
- KW-Funkgerät (HF) mit DSC (Inmarsat deckt >70° nicht ab)
- EPIRB 406 MHz
- SART oder AIS-SART

### 6.4 GMDSS-Relevanz für Sportboote

**Deutschland:** Sportboote sind NICHT SOLAS-pflichtig. Aber:
- **Ausrüstungspflicht See (SchSV):** Sportboote >12m, die Seegebiete befahren, müssen UKW mit DSC mitführen
- **Empfehlung BG Verkehr:** Jedes Sportboot auf See sollte UKW mit DSC haben
- **Versicherungsrelevanz:** Fehlende Funkausrüstung kann im Schadensfall als grobe Fahrlässigkeit gewertet werden
- **Praktische Notwendigkeit:** Ohne UKW kein Notruf, keine Wetterberichte, keine Hafenkommunikation

**Langfahrt (Atlantik, Pazifik):**
Obwohl nicht gesetzlich vorgeschrieben, ist für Blauwassersegeln folgende Ausrüstung dringend empfohlen:
- UKW mit DSC (Standard)
- EPIRB 406 MHz mit GPS (essentiell)
- AIS-SART oder Radar-SART
- Iridium-Satellitentelefon (zunehmend Standard)
- Optional: SSB/KW-Funk (Winlink, Wetterfax)
- Optional: Starlink (seit 2023/2024 zunehmend verbreitet)

(Confidence: documented)

---

## 7. Satellitenkommunikation

### 7.1 Inmarsat

**System:** Geostationäre Satelliten (4 Satelliten, ca. 36.000 km Höhe)
**Abdeckung:** Ca. 70°N bis 70°S (keine Polarabdeckung)
**Betreiber:** Inmarsat (Teil von Viasat seit 2023)

| Dienst | Datenrate | Kosten/Min | Anwendung | Yacht-Relevanz |
|--------|----------|-----------|-----------|---------------|
| Inmarsat-C | Textbasiert (600 bps) | ~0,50 USD/256 Bit | GMDSS, Telex, E-Mail | SOLAS-Pflicht, kaum für Sportboote |
| Inmarsat Fleet One | 100 kbps | ab 1 USD/MB | Daten, Sprache | Charter-Flotten, Superyachten |
| Inmarsat Fleet Broadband | bis 432 kbps | ab 3 USD/MB | Breitband, Sprache | Superyachten |
| Inmarsat FleetPhone | 4 kbps (Sprache) | ab 0,80 USD/Min | Telefonie | Langfahrer (wird seltener) |

**Für Sportboote:** Inmarsat ist aufgrund der hohen Kosten und Antennengrößen primär für Superyachten und kommerzielle Schiffe relevant. Für Yachten unter 20m hat Iridium die bessere Kosten-Nutzen-Relation.

### 7.2 Iridium

**System:** 66 LEO-Satelliten (Low Earth Orbit, ca. 780 km Höhe) + 6 Reservesatelliten
**Abdeckung:** Global, einschließlich Polargebiete (einziges System mit 100% globaler Abdeckung)
**Betreiber:** Iridium Communications Inc.

| Dienst | Gerät | Datenrate | Kosten | Yacht-Relevanz |
|--------|------|----------|--------|---------------|
| Iridium GO! | Iridium GO! (Hotspot) | 2,4 kbps | ab 65 EUR/Monat (Vertrag) | Sehr verbreitet bei Langfahrern |
| Iridium GO! exec | Iridium GO! exec (2024) | bis 22 Mbps (Certus 100) | ab 100 EUR/Monat | Neues Premium-Produkt |
| Iridium 9575 Extreme | Handheld-Telefon | 2,4 kbps | ab 1 EUR/Min (Vertrag) | Notfall-Backup |
| Iridium 9555 | Handheld-Telefon | 2,4 kbps | ab 1 EUR/Min | Älteres Modell, günstig |
| Iridium Certus | Festeinbau | bis 704 kbps | ab 200 EUR/Monat | Superyachten |

**Iridium GO! — Standard für Blauwasseryachten:**
- Erstellt lokalen WLAN-Hotspot
- Smartphone als Bedienelement (App)
- SMS, E-Mail, komprimiertes Internet
- Wetterdaten (GRIB-Dateien) via PredictWind, Iridium Mail
- Position-Tracking (z.B. YB Tracking, PredictWind)
- Notruf-Funktion (SOS-Taste)
- Kosten: Gerät ca. 800-1.200 EUR, Tarife ab 65 EUR/Monat
(Confidence: documented)

### 7.3 Starlink (SpaceX)

**System:** Mega-Konstellation LEO-Satelliten (ca. 550 km Höhe, >5.000 Satelliten Stand 2026)
**Abdeckung:** Global (zunehmend, Polargebiete seit 2024)
**Betreiber:** SpaceX

**Starlink Maritime / Starlink für Boote:**

| Tarif | Kosten/Monat | Hardware | Datenrate | Yacht-Relevanz |
|-------|-------------|---------|----------|---------------|
| Starlink Mobile Priority 50GB | ab 250 USD/Monat | Flachantenne (ca. 2.500 USD) | bis 220 Mbps | Fahrtensegler, Langfahrer |
| Starlink Mobile Priority 1TB | ab 500 USD/Monat | Flachantenne | bis 220 Mbps | Charter, Superyacht |
| Starlink Mobile Priority 5TB | ab 1.000 USD/Monat | Flachantenne | bis 220 Mbps | Superyacht |

**Revolution für die Yachtnavigation (seit 2023/2024):**
- Quasi unbegrenztes Internet auf See — Wetter, Routing, Kommunikation
- Video-Telefonie mit Familie/Büro
- Fernwartung von Bord-Elektronik
- Streaming, Arbeit an Bord
- ABER: **Starlink ist KEIN Ersatz für UKW-Seefunk und GMDSS**
- ABER: **Kein Notruf-System** — Starlink hat keine SAR-Integration
- ABER: **Abhängig von Strom** — bei Schiffbruch nicht verfügbar
- ABER: **Antenne benötigt freie Sicht** — problematisch bei starker Krängung (>25°)

**Installation auf Yachten:**
- Antenne (Dishy): 600×380 mm, ca. 4 kg
- Montage: Masthalterung, Geräteträger, Hardtop, Bimini
- Strombedarf: 50–100 Watt (12V via Adapter oder 110/220V)
- Ethernet-Verbindung zum Router
- WLAN-Hotspot für alle Bordgeräte
(Confidence: documented)

### 7.4 Thuraya

**System:** 2 geostationäre Satelliten
**Abdeckung:** Europa, Afrika, Asien, Australien (KEIN Amerika)
**Relevanz für Yachten:** Gering — Iridium und Starlink sind überlegen. Nur relevant für Fahrtgebiete Indischer Ozean bis Südostasien ohne Starlink-Abdeckung.

### 7.5 Kommunikationsmatrix: Was wann nutzen?

| Situation | Primär | Sekundär | Backup |
|-----------|--------|----------|--------|
| Notruf (Seenot) | DSC Kanal 70 + Kanal 16 | EPIRB 406 MHz | Iridium SOS |
| Dringende Meldung (Pan-Pan) | UKW Kanal 16 | DSC Urgency | Iridium Telefon |
| Wetterbericht empfangen | UKW (DP07/Coastguard) | Starlink / Iridium (GRIB) | NAVTEX |
| Hafenanruf | UKW Kanal 09/80 | Telefon (Starlink/Iridium) | — |
| Schiff-zu-Schiff nahe | UKW Kanal 72/77 | — | — |
| Familie kontaktieren | Starlink (WLAN) | Iridium GO! (SMS/Anruf) | UKW → Küstenfunkstelle → Telefon |
| Position melden | AIS (automatisch) | Iridium Tracking | DSC Positionsmeldung |
| E-Mail/Internet | Starlink | Iridium GO! | Iridium Mail (komprimiert) |

---

## 8. AIS-SART und EPIRB

### 8.1 EPIRB — Emergency Position Indicating Radio Beacon

**Funktion:** Sendet Notsignal auf 406 MHz an COSPAS-SARSAT-Satelliten. Position wird an zuständiges MRCC weitergeleitet.

**Technische Daten:**
- Sendefrequenz: 406,028 MHz (Satellit) + 121,5 MHz (Homing-Signal für SAR-Flugzeuge/Schiffe)
- Sendeleistung: 5 Watt (406 MHz)
- GPS-integriert: Position auf ±100m (mit GPS) bzw. ±5 km (ohne GPS, nur Doppler)
- Batterielebensdauer: mindestens 48 Stunden Dauersendung bei -20°C
- Registrierung: MMSI + Eignerinformationen bei nationaler Behörde (DE: BNetzA)

**Typen:**

| Typ | Auslösung | Montage | Anwendung |
|-----|-----------|---------|-----------|
| Float-Free (Kategorie I) | Automatisch bei Untergang (Hydrostatic Release Unit) | Deck-Halterung mit HRU | SOLAS-Pflicht, empfohlen für Yacht |
| Manual (Kategorie II) | Manuell | Griffbereit, oft in Grabgag | Sportboote, Rettungsinsel |
| PLB (Personal Locator Beacon) | Manuell | Am Körper (Rettungsweste) | MOB, Einzelperson |

**Wichtige Hersteller:**

| Hersteller | Land | Modelle | Preisrange |
|-----------|------|---------|-----------|
| ACR Electronics | USA | GlobalFix V5, ResQLink 400 (PLB) | 300–800 EUR |
| McMurdo (Orolia) | UK | SmartFind G8, FastFind 220 (PLB) | 250–700 EUR |
| Ocean Signal | UK | rescueME EPIRB3, PLB3 | 300–750 EUR |
| Kannad (Orolia) | FR | SafePro, SafeLink SOLO (PLB) | 250–600 EUR |
| GME | AU | MT603FG, AccuSat 406 | 350–800 EUR |

### 8.2 EPIRB-Registrierung

**KRITISCH:** Eine nicht registrierte EPIRB ist nahezu nutzlos. Bei Auslösung kann das MRCC ohne Registrierung:
- Nicht feststellen, welches Schiff in Not ist
- Nicht feststellen, wie viele Personen an Bord sind
- Nicht feststellen, ob es sich um einen Fehlalarm handelt
- Keine Nächsten Angehörigen benachrichtigen

**Registrierung in Deutschland:**
- Zuständig: BNetzA (für Schiffsstation) oder Deutsches Maritimes Zentrum
- Online-Registrierung: https://406registration.com (international)
- Erforderliche Daten: MMSI, HEX-ID der EPIRB, Schiffsname, Heimathafen, Schiffstyp, Personenzahl, Notfallkontakte
- Aktualisierung: Bei Eignerwechsel, Revierwechsel oder Änderung der Crew-Anzahl

### 8.3 AIS-SART — AIS Search and Rescue Transmitter

**Funktion:** Sendet AIS-Signale auf den AIS-Frequenzen (161,975 MHz und 162,025 MHz), die auf allen AIS-fähigen Kartenplottern und Radargeräten in der Umgebung als Notsignal-Symbol erscheinen.

**Technische Daten:**
- Sendefrequenzen: 161,975 MHz (AIS 1) und 162,025 MHz (AIS 2)
- Sendeleistung: 1 Watt
- MMSI-Kennung: 970XXXXXX (automatisch als SART erkannt)
- Reichweite: 5–10 nm (abhängig von Antennenhöhe des Empfängers)
- Batterielebensdauer: mindestens 96 Stunden
- GPS-integriert: Position alle 60 Sekunden aktualisiert

**Vorteile gegenüber Radar-SART:**
- Wird auf JEDEM AIS-fähigen Gerät angezeigt (Plotter, AIS-Empfänger, Smartphone-Apps)
- Höhere Reichweite bei niedriger Sendeleistung
- Position wird exakt angezeigt (GPS)
- Preisgünstiger
- Geringerer Stromverbrauch

**Nachteile:**
- Nicht von Radar allein erkennbar (benötigt AIS-Empfänger)
- Manche ältere Radargeräte zeigen keinen AIS-SART an

**Wichtige AIS-SART-Modelle:**

| Hersteller | Modell | Preis (ca.) | Batterie | Gewicht |
|-----------|--------|------------|---------|---------|
| ACR | AISLink MOB (PLB/AIS) | 250–350 EUR | 24h | 128g |
| McMurdo | SmartFind S10 AIS SART | 500–700 EUR | 96h | 390g |
| Ocean Signal | rescueME EDF1 | 200–300 EUR | 7h (Strobo) | 82g |
| Weatherdock | easyRescue | 350–500 EUR | 96h | 260g |
| Jotron | Tron AIS-SART | 400–600 EUR | 96h | 330g |
| Kannad | R10 AIS SART | 400–550 EUR | 96h | 350g |

### 8.4 Radar-SART (Search and Rescue Transponder)

**Funktion:** Empfängt Radarsignale (9 GHz X-Band) und sendet ein Antwortsignal, das auf dem Radarschirm als Reihe von 12 Punkten erscheint, die zum SART-Standort führen.

**Nachteile gegenüber AIS-SART:**
- Nur auf X-Band-Radar sichtbar (nicht auf S-Band)
- Nicht auf Kartenplottern oder AIS-Empfängern sichtbar
- Höherer Stromverbrauch
- Teurer
- Ältere Technologie, wird zunehmend durch AIS-SART ersetzt

**Empfehlung AYDI:** AIS-SART bevorzugen. Radar-SART nur als Ergänzung bei SOLAS-pflichtigen Yachten.
(Confidence: documented)

### 8.5 MOB-Sender (Mann-über-Bord)

**Moderne MOB-Systeme kombinieren mehrere Technologien:**

| System | Technologie | Reichweite | Alarmierung | Preis |
|--------|------------|-----------|-------------|-------|
| ACR AISLink MOB | AIS + DSC + GPS | 5–10 nm | AIS-Alarm auf Plotter | 250–350 EUR |
| Ocean Signal MOB1 | AIS + DSC | 5–10 nm | AIS-Alarm + DSC-Notruf | 200–300 EUR |
| McMurdo FastFind MOB | AIS | 5–10 nm | AIS-Alarm auf Plotter | 250–350 EUR |
| Kannad SafeLink R10+ | AIS | 5–10 nm | AIS-Alarm | 300–400 EUR |
| SIMY MY-AIS | AIS | 5–7 nm | AIS-Alarm | 200–280 EUR |
| CrewWatcher | Bluetooth + App | 30m (BT) | Smartphone-Alarm | 100–150 EUR |

**Empfehlung:** Jedes Crewmitglied sollte bei Offshore-Segeln einen MOB-Sender tragen, der AIS-Signal sendet. Der DSC-Alarm ist ein Bonus, der die Küstenwache automatisch alarmiert.

---

## 9. Antennen für UKW-Seefunk

### 9.1 Antennentypen

| Typ | Gewinn | Länge | Anwendung | Vorteile | Nachteile |
|-----|--------|-------|-----------|----------|-----------|
| **1/4-Welle Stabantenne** | 0 dBd | ca. 50 cm | Handsprechfunkgeräte | Kompakt, omnidirektional | Geringe Reichweite |
| **1/2-Welle (3 dB)** | 3 dBd | ca. 1,0 m | Motorboote, Geräteträger | Guter Kompromiss, stabil bei Seegang | Mittlere Reichweite |
| **5/8-Welle (3 dB)** | 3 dBd | ca. 1,2 m | Standard Segelboot | Häufigster Typ | — |
| **Collinear (6 dB)** | 6 dBd | ca. 2,4 m | Motorboote, stabile Plattform | Höchste Reichweite | Schmaler Abstrahlwinkel vertikal |
| **Collinear (9 dB)** | 9 dBd | ca. 4,8 m | Große Motoryachten, stationär | Maximale Reichweite | Nur bei stabiler Plattform, nicht für Segelboote |
| **Mastantenne (Segelboot)** | 3 dBd | 1,0–1,5 m | Am Masttop oder an Saling | Höchste Position = beste Reichweite | Kabelverluste durch lange Leitung |
| **Emergency-Antenne** | 0 dBd | 30–50 cm | Rettungsinsel, Notfall | Kompakt, schnell montiert | Minimale Reichweite |

### 9.2 Antennengewinn und Abstrahlcharakteristik

**Grundregel:** Mehr Gewinn = mehr Reichweite horizontal, aber schmalerer vertikaler Abstrahlwinkel.

| Gewinn | Vertikaler Abstrahlwinkel | Geeignet für | NICHT geeignet für |
|--------|--------------------------|-------------|-------------------|
| 0 dBd | ca. 90° | Handgeräte, Notfall | — |
| 3 dBd | ca. 25–30° | Segelboote (Krängung), Motorboote | — |
| 6 dBd | ca. 12–15° | Motorboote (stabil) | Segelboote (>15° Krängung) |
| 9 dBd | ca. 7–8° | Große Motoryachten, Küstenstationen | Segelboote, kleine Motorboote |

**KRITISCH für Segelboote:** Bei 25° Krängung (typisch bei Amwindkurs) wird die Abstrahlung einer 9-dB-Antenne so stark verkippt, dass die Reichweite dramatisch sinkt. **Empfehlung: maximal 3 dBd für Segelboote.**
(Confidence: documented)

### 9.3 Antennenkabel und Verluste

| Kabeltyp | Durchmesser | Verlust bei 156 MHz/10m | Typische Anwendung |
|----------|------------|------------------------|-------------------|
| RG-58 | 5 mm | 1,9 dB | Handgerät, kurze Strecken (<5m) |
| RG-8X (Mini-8) | 6 mm | 1,3 dB | Motorboote (<10m Kabel) |
| RG-213 | 10,3 mm | 0,6 dB | Standard für Festeinbau |
| LMR-400 | 10,3 mm | 0,4 dB | Optimale Wahl für lange Strecken |
| Aircell 7 | 7,3 mm | 0,7 dB | Flexibel, guter Kompromiss |
| RG-8U | 10,3 mm | 0,7 dB | Älterer Standard |

**Steckverbinder:**
- **PL-259 (UHF-Stecker)** — Standard für UKW-Seefunk. Nicht wasserdicht ohne Zusatzmaßnahmen.
- **N-Stecker** — Professioneller, besser abgeschirmt, aber seltener an Yacht-Funkgeräten
- **BNC** — Für Handgeräte und Splitter
- **FME** — Für externe Antennenanschlüsse an Handgeräten

**Selbstvulkanisierendes Klebeband** für wasserdichte Verbindungen an Deck und Mast ist PFLICHT.

### 9.4 AIS/UKW-Splitter

**Funktion:** Erlaubt die Nutzung EINER Antenne für UKW-Funkgerät UND AIS-Transponder gleichzeitig.

**Funktionsprinzip:**
- Splitter erkennt, ob UKW-Funkgerät sendet
- Während UKW sendet: AIS wird abgeschaltet (für ca. 2 Sekunden)
- Während UKW nicht sendet: AIS und UKW empfangen über gleiche Antenne
- Automatischer Umschalter (keine manuelle Bedienung)

**Wichtige Splitter-Modelle:**

| Hersteller | Modell | Ports | Preis | Besonderheit |
|-----------|--------|-------|-------|-------------|
| Glomex | RA201 | 2 (UKW + AIS) | 120–180 EUR | Kompakt, bewährt |
| Shakespeare | AIS-200 | 2 (UKW + AIS) | 150–200 EUR | Niedriger Verlust |
| Vesper Marine | SP160 | 2 (UKW + AIS) | 200–280 EUR | Premium, sehr niedriger Verlust |
| Digital Yacht | SPL2000 | 2 (UKW + AIS) | 150–220 EUR | FM-Radio zusätzlich |
| NASA Marine | AIS-Splitter | 2 (UKW + AIS) | 100–150 EUR | Budget-Option |
| em-trak | S300 | 3 (UKW + AIS + FM) | 200–300 EUR | Drei Ports |

**Verlust durch Splitter:** Typisch 0,5–1,5 dB. Bei gutem Splitter vernachlässigbar.

**Alternative:** Separate Antennen für UKW und AIS. Abstand mindestens 1,5m vertikal.
(Confidence: documented)

### 9.5 Antennen-Hersteller

| Hersteller | Land | Stärke | Preisrange | Typische Modelle |
|-----------|------|--------|-----------|-----------------|
| Shakespeare | USA | Marktführer, breitestes Sortiment | 50–400 EUR | 5215, 5225-XT, 5104 |
| Glomex | IT | Gutes Preis-Leistungs-Verhältnis | 40–250 EUR | RA1206, RA1225 |
| Pacific Aerials | NZ | Premium, Segelboot-Masttop | 80–300 EUR | P6003, P6111 |
| Procom | DK | Robust, nordeuropäischer Markt | 60–200 EUR | CXL 2/1LW |
| Scout | IT | Design, Motorboote | 50–250 EUR | KS-42, KS-62 |
| AC Antennas | UK | Spezialisten für Superyachten | 200–1.500 EUR | Maßanfertigungen |
| Morad | CA | Premium, Langfahrer | 100–350 EUR | VHF 3, VHF 6 |
| Digital Antenna | USA | Breitband, robust | 80–300 EUR | 528-VW, 544-SW |

---

## 10. Typenübersicht — UKW-Seefunkgeräte

### 10.1 Gerätekategorien

| Kategorie | Sendeleistung | DSC | AIS | GPS | Preis | Anwendung |
|-----------|-------------|-----|-----|-----|-------|-----------|
| **Handsprechfunkgerät (ohne DSC)** | 5–6 W | Nein | Nein | Nein | 80–200 EUR | Beiboot, Notfall-Backup |
| **Handsprechfunkgerät (mit DSC)** | 5–6 W | Ja (Klasse D) | Nein | Integriert | 200–400 EUR | Backup, kleine Boote |
| **Festeinbau Standard** | 25 W | Ja (Klasse D) | Nein | Extern | 200–400 EUR | Standard-Yacht |
| **Festeinbau mit AIS-Empfänger** | 25 W | Ja (Klasse D) | Empfang | Extern | 350–600 EUR | Yacht mit AIS-Wunsch |
| **Festeinbau Premium** | 25 W | Ja (Klasse D/E) | Empfang + Senden | Intern + Extern | 500–1.200 EUR | Anspruchsvolle Yacht |
| **Festeinbau GMDSS-zugelassen** | 25 W | Ja (Klasse A/E) | Optional | Extern | 800–2.500 EUR | Berufsschifffahrt, Superyacht |

### 10.2 Wichtige Features moderner Geräte

| Feature | Beschreibung | Relevanz | Verfügbar ab |
|---------|-------------|----------|-------------|
| **DSC Klasse D** | Standard DSC für Sportboote | Pflicht | Alle modernen Festeinbauten |
| **DSC Klasse E** | Erweitert: automatische Bestätigung, Individual-Acknowledge | Empfohlen | Mittel- bis Oberklasse |
| **AIS-Empfänger integriert** | Empfang AIS-Signale, Anzeige auf Gerätedisplay | Sehr empfohlen | Mittelklasse aufwärts |
| **AIS-Transponder integriert** | Empfang + Senden AIS (Klasse B) | Premium | Nur wenige Geräte (z.B. IC-M510) |
| **GPS integriert** | Interne GPS-Antenne für DSC-Position | Praktisch | Viele Geräte |
| **NMEA 2000** | Vernetzung mit Plotter, Instrumente | Standard bei Neugeräten | Mittelklasse aufwärts |
| **NMEA 0183** | Älterer Datenbus, weit verbreitet | Kompatibilität | Alle Geräte |
| **Aktive Rauschunterdrückung** | Filtert Motorengeräusche und Wind | Komfort | Premium-Geräte |
| **Dual Watch / Tri Watch** | Gleichzeitige Überwachung mehrerer Kanäle + Kanal 16 | Sicherheit | Standard |
| **Hailer/Horn** | Lautsprecher-Funktion über externen Lautsprecher | Manöver | Premium-Festeinbauten |
| **Fog Horn** | Nebelsignal über externen Lautsprecher | Vorschrift | Premium |
| **Replay** | Letzte Funksprüche abspielen | Komfort | Einige Geräte |
| **Wireless Remote** | Drahtloses Zweit-Mikrofon | Flexibilität | Premium (z.B. Raymarine) |
| **Touchscreen** | Berührungsempfindliches Display | Bedienung | Neueste Generation |

---

## 11. Produktlinien: ICOM

### 11.1 ICOM — Firmenüberblick

**ICOM Inc.** (Osaka, Japan, gegründet 1954) ist der weltweit führende Hersteller von Seefunkgeräten. ICOM-Geräte gelten als Referenz in Bezug auf Empfindlichkeit, Verarbeitungsqualität und Zuverlässigkeit.

### 11.2 ICOM IC-M510 (Flaggschiff)

| Parameter | Wert |
|-----------|------|
| **Typ** | Festeinbau UKW mit DSC + AIS-Transponder (Klasse B) |
| **DSC-Klasse** | D (erweiterbar auf E per Firmware) |
| **AIS** | Integrierter Klasse-B-Transponder (Senden + Empfangen) |
| **GPS** | Integrierter GPS-Empfänger |
| **Sendeleistung** | 25 W / 1 W |
| **Display** | 4,3" Farb-TFT mit Touchscreen |
| **NMEA** | NMEA 2000 + NMEA 0183 |
| **Wireless** | WLAN (Smartphone-Steuerung via App) |
| **Besonderheiten** | AIS-Ziele auf Display, DSC-Positionsabfrage, Replay, Hailer, Fog Horn |
| **Maße (HxBxT)** | 115 × 200 × 80 mm (Hauptgerät) |
| **Stromaufnahme** | Empfang: 0,8 A, Senden: 6,0 A (bei 13,8 V) |
| **Preis** | 800–1.100 EUR |
| **Markteinführung** | 2022 |
| **Bewertung AYDI** | Referenzgerät — beste Integration UKW + AIS + DSC in einem Gerät |
(Confidence: measured)

### 11.3 ICOM IC-M330 (Mittelklasse)

| Parameter | Wert |
|-----------|------|
| **Typ** | Festeinbau UKW mit DSC |
| **DSC-Klasse** | D |
| **AIS** | Nein (nur AIS-Daten via NMEA von externem AIS-Empfänger) |
| **GPS** | Integrierter GPS-Empfänger |
| **Sendeleistung** | 25 W / 1 W |
| **Display** | LCD mit Hintergrundbeleuchtung |
| **NMEA** | NMEA 0183 |
| **Besonderheiten** | Kompakt, IPX7, Active Noise Cancelling, Aqua Quake (Wasser aus Lautsprecher schütteln) |
| **Maße** | 100 × 156 × 64 mm |
| **Stromaufnahme** | Empfang: 0,3 A, Senden: 5,5 A |
| **Preis** | 200–280 EUR |
| **Bewertung AYDI** | Bestes Preis-Leistungs-Verhältnis im Mittelfeld |
(Confidence: measured)

### 11.4 ICOM IC-M94D (Handgerät Premium)

| Parameter | Wert |
|-----------|------|
| **Typ** | Handsprechfunkgerät mit DSC + AIS-Empfänger + GPS |
| **DSC-Klasse** | D |
| **AIS** | Empfänger integriert (kein Transponder) |
| **GPS** | Integriert |
| **Sendeleistung** | 6 W / 1 W |
| **Display** | 2,3" Farb-TFT |
| **Besonderheiten** | AIS-Ziele auf Display, DSC-Notruf, USB-C Ladung, Float & Flash, IPX7, Navigationsfunktion |
| **Akku** | 7,4V / 2.350 mAh Li-Ion (ca. 11h Betrieb) |
| **Maße** | 145 × 60 × 35 mm |
| **Gewicht** | 295 g (mit Akku und Antenne) |
| **Preis** | 350–450 EUR |
| **Bewertung AYDI** | Bestes Handgerät am Markt — AIS + DSC + GPS in einem Handgerät |
(Confidence: measured)

### 11.5 Weitere ICOM-Modelle

| Modell | Typ | DSC | AIS | GPS | Preis | Anmerkung |
|--------|-----|-----|-----|-----|-------|-----------|
| IC-M506 | Festeinbau | Klasse D | Via NMEA | Extern | 350–450 EUR | Vorgänger M510, NMEA 2000, Replay |
| IC-M423 | Festeinbau | Klasse D | Nein | Extern | 250–350 EUR | Kompakt, IPX7 |
| IC-M400BB | Black Box | Klasse D | Via NMEA | Extern | 400–550 EUR | Kein Display, nur Mikrofon + Lautsprecher |
| IC-M37 | Handgerät | Nein | Nein | Nein | 100–140 EUR | Budget, robust, Float & Flash |
| IC-M73 | Handgerät | Nein | Nein | Nein | 130–180 EUR | Professional, 6W, Active Noise Cancelling |
| IC-M85 | Handgerät | Nein | Nein | Nein | 250–350 EUR | LTE + VHF (Dual-Mode) |
| IC-M93D | Handgerät | Klasse D | Nein | Integriert | 280–380 EUR | DSC + GPS, Float & Flash |
| IC-M25 | Handgerät | Nein | Nein | Nein | 130–180 EUR | Ultra-kompakt, schwimmt, USB-C |
| IC-M605 | Festeinbau | Klasse A | AIS über NMEA | Extern | 1.200–1.800 EUR | GMDSS, Berufsschifffahrt |

---

## 12. Produktlinien: Standard Horizon

### 12.1 Standard Horizon — Firmenüberblick

**Yaesu Musen / Standard Horizon** (Tokio, Japan) ist der zweitgrößte Hersteller von Seefunkgeräten und bietet ein breites Sortiment von Budget bis Premium.

### 12.2 Standard Horizon GX6000 (Flaggschiff)

| Parameter | Wert |
|-----------|------|
| **Typ** | Festeinbau UKW mit DSC + AIS-Empfänger + GPS |
| **DSC-Klasse** | D |
| **AIS** | Integrierter Empfänger (kein Transponder) |
| **GPS** | Integrierter 66-Kanal-GPS |
| **Sendeleistung** | 25 W / 1 W |
| **Display** | 3,0" Farb-LCD |
| **NMEA** | NMEA 2000 + NMEA 0183 |
| **Besonderheiten** | AIS auf Display, Mega Marina Database (vorprogrammierte Marinas), Scrambler, Hailer, Fog Horn, 30W PA |
| **Maße** | 100 × 170 × 80 mm |
| **Preis** | 400–550 EUR |
| **Bewertung AYDI** | Preis-Leistungs-Sieger mit AIS-Empfänger — günstiger als ICOM IC-M510, aber ohne AIS-Transponder |
(Confidence: measured)

### 12.3 Standard Horizon GX2400

| Parameter | Wert |
|-----------|------|
| **Typ** | Festeinbau UKW mit DSC + AIS-Empfänger + GPS |
| **DSC-Klasse** | D |
| **AIS** | Integrierter Empfänger |
| **GPS** | Integriert |
| **Sendeleistung** | 25 W / 1 W |
| **Display** | Dot-Matrix LCD |
| **NMEA** | NMEA 0183 |
| **Preis** | 300–400 EUR |
| **Bewertung AYDI** | Solide Mittelklasse mit AIS-Empfänger |
(Confidence: measured)

### 12.4 Weitere Standard Horizon Modelle

| Modell | Typ | DSC | AIS | GPS | Preis | Anmerkung |
|--------|-----|-----|-----|-----|-------|-----------|
| GX1400 | Festeinbau | Klasse D | Nein | Extern | 160–220 EUR | Budget, robust, Einstieg |
| GX1800 | Festeinbau | Klasse D | Nein | Integriert | 220–300 EUR | GPS integriert, kompakt |
| GX6500 | Festeinbau | Klasse D | Transponder Klasse B | Integriert | 700–900 EUR | UKW + AIS-Transponder (wie IC-M510) |
| HX890 | Handgerät | Klasse D | Nein | Integriert | 300–400 EUR | Premium-Handgerät, Float & Flash |
| HX870 | Handgerät | Klasse D | Nein | Integriert | 250–350 EUR | DSC + GPS, bewährt |
| HX300 | Handgerät | Nein | Nein | Nein | 80–120 EUR | Budget, schwimmt |
| HX40 | Handgerät | Nein | Nein | Nein | 100–140 EUR | Ultra-kompakt, 6W |

---

## 13. Produktlinien: Raymarine

### 13.1 Raymarine — Firmenüberblick

**Raymarine** (Fareham, UK, Teil der FLIR/Teledyne-Gruppe) bietet UKW-Funkgeräte als Teil ihres integrierten Navigationssystems an. Hauptvorteil: nahtlose Integration mit Axiom-Kartenplottern und Lighthouse-Betriebssystem.

### 13.2 Raymarine Ray Serie

| Modell | Typ | DSC | AIS | GPS | Preis | Besonderheit |
|--------|-----|-----|-----|-----|-------|-------------|
| Ray63 | Festeinbau | Klasse D | Via NMEA | Extern | 250–350 EUR | Einstieg Raymarine |
| Ray73 | Festeinbau | Klasse D | Empfänger integriert | Integriert | 400–550 EUR | AIS + GPS, NMEA 2000 |
| Ray90/91 | Black Box | Klasse D | Via NMEA | Extern | 800–1.200 EUR | Modulares System, bis zu 2 Stationen |
| Ray260 | Black Box | Klasse D | Via NMEA | Extern | 600–850 EUR | Kompakte Black Box |

**Raymarine Ray73 (empfohlenes Modell für Yachten):**

| Parameter | Wert |
|-----------|------|
| **Typ** | Festeinbau UKW mit DSC + AIS-Empfänger + GPS |
| **DSC-Klasse** | D |
| **AIS** | Empfänger integriert |
| **GPS** | Integriert (72-Kanal) |
| **Sendeleistung** | 25 W / 1 W |
| **Display** | LCD Matrix |
| **NMEA** | NMEA 2000 + NMEA 0183 + SeaTalkNG |
| **Integration** | Axiom-Plotter: AIS-Ziele auf Kartenplotter, DSC von Plotter auslösen |
| **Preis** | 400–550 EUR |
| **Bewertung AYDI** | Beste Integration mit Raymarine-Ökosystem |
(Confidence: measured)

---

## 14. Produktlinien: Simrad / B&G

### 14.1 Simrad / B&G — Firmenüberblick

**Simrad** (Horten, Norwegen) und **B&G** (UK) gehören beide zur Navico-Gruppe (jetzt Teil von Brunswick). Simrad fokussiert auf Motor-/Fischereiyachten, B&G auf Segelboote. UKW-Funkgeräte werden unter beiden Marken angeboten.

### 14.2 Modellübersicht

| Modell | Marke | Typ | DSC | AIS | GPS | Preis | Anmerkung |
|--------|-------|-----|-----|-----|-----|-------|-----------|
| RS40 | Simrad | Festeinbau | Klasse D | Empfänger integriert | Integriert | 350–500 EUR | Standard, NMEA 2000 |
| RS40-B | Simrad | Festeinbau | Klasse D | Transponder Klasse B | Integriert | 700–950 EUR | UKW + AIS-Transponder |
| V60 | B&G | Festeinbau | Klasse D | Empfänger integriert | Integriert | 400–550 EUR | Segler-optimiert |
| V60-B | B&G | Festeinbau | Klasse D | Transponder Klasse B | Integriert | 750–1.000 EUR | UKW + AIS-Transponder |
| RS100 | Simrad | Black Box | Klasse D | Via NMEA | Extern | 500–700 EUR | Modulares System |
| RS100-B | Simrad | Black Box | Klasse D | Transponder Klasse B | Integriert | 900–1.200 EUR | Black Box + AIS |

**B&G V60-B (empfohlen für Segler im Navico-Ökosystem):**
- UKW + DSC + AIS-Transponder (Klasse B) in einem Gerät
- Nahtlose Integration mit B&G Vulcan/Zeus-Plottern
- AIS-Ziele direkt auf dem Kartenplotter
- NMEA 2000 native
- Preis: 750–1.000 EUR
(Confidence: measured)

---

## 15. Produktlinien: Cobra / Uniden

### 15.1 Budget-Segment

**Cobra** (USA) und **Uniden** (USA/Japan) bedienen das Budget-Segment, primär für den US-Markt. In Europa weniger verbreitet, aber über Import erhältlich.

| Modell | Hersteller | Typ | DSC | GPS | Preis | Anmerkung |
|--------|-----------|-----|-----|-----|-------|-----------|
| MR HH475 FLT BT | Cobra | Handgerät | Nein | Nein | 60–90 EUR | Bluetooth, schwimmt |
| MR F45-D | Cobra | Festeinbau | Klasse D | Extern | 150–200 EUR | Budget mit DSC |
| MR F57B | Cobra | Festeinbau | Klasse D | Extern | 100–150 EUR | Einstiegspreis |
| UM725 | Uniden | Festeinbau | Klasse D | Integriert | 150–200 EUR | GPS + DSC, sehr günstig |
| UM385 | Uniden | Festeinbau | Klasse D | Extern | 100–150 EUR | Budget |
| MHS335BT | Uniden | Handgerät | Klasse D | Integriert | 180–250 EUR | DSC + GPS + Bluetooth |

**AYDI-Bewertung Budget-Segment:** Akzeptabel für Küstenreviere und gelegentlichen Einsatz. Nicht empfohlen für Offshore oder Langfahrt — geringere Empfindlichkeit, kürzere Lebensdauer, eingeschränkter Service in Europa.
(Confidence: estimated)

---

## 16. Produktlinien: ACR / McMurdo (EPIRB und SART)

### 16.1 ACR Electronics

**ACR Electronics** (Fort Lauderdale, USA) ist der führende Hersteller von EPIRB, PLB und SART.

| Modell | Typ | Frequenz | GPS | Batterie | Preis | Anmerkung |
|--------|-----|---------|-----|---------|-------|-----------|
| GlobalFix V5 | EPIRB Kat. I (Float-Free) | 406 MHz + 121,5 MHz | Ja (integriert) | 48h+ | 600–800 EUR | Referenz-EPIRB für Yachten |
| GlobalFix V4 | EPIRB Kat. II (Manual) | 406 MHz + 121,5 MHz | Ja | 48h+ | 500–650 EUR | Manuell auslösbar |
| ResQLink 400 | PLB | 406 MHz + 121,5 MHz | Ja | 24h+ | 300–400 EUR | Am Körper tragbar, MOB |
| ResQLink View | PLB | 406 MHz + 121,5 MHz | Ja | 24h+ | 350–450 EUR | Mit Display (Signalstatus) |
| AISLink MOB | AIS-SART/MOB | AIS (161,975/162,025 MHz) | Ja | 24h | 250–350 EUR | AIS + DSC MOB-Alarm |

### 16.2 McMurdo (Orolia)

**McMurdo** (Portsmouth, UK, Teil der Orolia-Gruppe) ist europäischer Marktführer für EPIRB und SART.

| Modell | Typ | Frequenz | GPS | Batterie | Preis | Anmerkung |
|--------|-----|---------|-----|---------|-------|-----------|
| SmartFind G8 | EPIRB Kat. I | 406 MHz + 121,5 MHz | Ja | 48h+ | 550–750 EUR | AIS-Homing-Signal + 406 MHz |
| SmartFind E8 | EPIRB Kat. I | 406 MHz + 121,5 MHz | Ja | 48h+ | 450–600 EUR | Standard, zuverlässig |
| FastFind 220 | PLB | 406 MHz + 121,5 MHz | Ja | 24h+ | 250–350 EUR | Kompakt, leicht |
| SmartFind S10 | AIS-SART | AIS | Ja | 96h | 500–700 EUR | Professional SART |
| SmartFind S20 | AIS-SART (Personal) | AIS | Ja | 96h | 350–500 EUR | Tragbar |

### 16.3 Ocean Signal

| Modell | Typ | Frequenz | GPS | Batterie | Preis | Anmerkung |
|--------|-----|---------|-----|---------|-------|-----------|
| rescueME EPIRB3 | EPIRB Kat. II | 406 MHz + 121,5 MHz + AIS | Ja | 48h+ | 600–800 EUR | EPIRB + AIS (Dual-Signal) |
| rescueME PLB3 | PLB | 406 MHz + 121,5 MHz + AIS | Ja | 24h+ | 400–500 EUR | PLB + AIS |
| rescueME MOB1 | MOB-Sender | AIS + DSC | Ja | 7h | 200–300 EUR | AIS + DSC MOB-Alarm |
| rescueME EDF1 | Elektronisches Notsignal | AIS + LED | Ja | 7h | 200–300 EUR | Ersatz für Signalraketen |

---

## 17. Hersteller-Datenbank

### 17.1 ICOM Inc.

| Feld | Information |
|------|------------|
| **Vollständiger Name** | ICOM Incorporated |
| **Gründung** | 1954 |
| **Hauptsitz** | Osaka, Japan |
| **Europa-Zentrale** | ICOM (Europe) GmbH, Bad Soden, Deutschland |
| **Webseite** | www.icomeurope.com |
| **Stärken** | Referenz für Empfindlichkeit, Verarbeitung, Service-Netzwerk |
| **Schwächen** | Preispremium 10-20% über Wettbewerb |
| **Marktanteil (geschätzt)** | 35-40% (Sportboot-UKW weltweit) |
| **Service Deutschland** | ICOM (Europe) GmbH, autorisierte Servicepartner |
| **Garantie** | 2 Jahre (EU), erweiterbar |
| **AYDI-Gesamtbewertung** | 92/100 |
(Confidence: estimated)

### 17.2 Standard Horizon (Yaesu)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | Yaesu Musen Co., Ltd. (Marke: Standard Horizon) |
| **Gründung** | 1956 |
| **Hauptsitz** | Tokio, Japan |
| **Europa-Vertrieb** | Yaesu UK Ltd., diverse Distributoren |
| **Webseite** | www.standardhorizon.com |
| **Stärken** | Bestes Preis-Leistungs-Verhältnis, Mega Marina Database |
| **Schwächen** | Service in Europa eingeschränkter als ICOM |
| **Marktanteil (geschätzt)** | 25-30% |
| **Garantie** | 3 Jahre (USA), 2 Jahre (EU) |
| **AYDI-Gesamtbewertung** | 87/100 |
(Confidence: estimated)

### 17.3 Raymarine (Teledyne FLIR)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | Raymarine (Teil von Teledyne FLIR) |
| **Gründung** | 1923 (als Kelvin Hughes), 2001 als Raymarine |
| **Hauptsitz** | Fareham, Hampshire, UK |
| **Webseite** | www.raymarine.com |
| **Stärken** | Beste Integration mit eigenem Ökosystem (Axiom, Lighthouse) |
| **Schwächen** | Weniger Auswahl als ICOM, etwas höhere Preise |
| **Marktanteil UKW (geschätzt)** | 10-15% |
| **Garantie** | 2 Jahre (EU) |
| **AYDI-Gesamtbewertung** | 84/100 |
(Confidence: estimated)

### 17.4 Navico (Simrad / B&G)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | Navico Group (Marken: Simrad, B&G, Lowrance, C-MAP) |
| **Muttergesellschaft** | Brunswick Corporation (seit 2021) |
| **Hauptsitz** | Egersund, Norwegen (Simrad) / Fareham, UK (B&G) |
| **Webseite** | www.simrad-yachting.com / www.bandg.com |
| **Stärken** | Integration mit eigenem Ökosystem, AIS-Transponder integriert |
| **Schwächen** | UKW-Sortiment kleiner als ICOM |
| **Marktanteil UKW (geschätzt)** | 10-12% |
| **Garantie** | 2 Jahre (EU) |
| **AYDI-Gesamtbewertung** | 85/100 |
(Confidence: estimated)

### 17.5 ACR Electronics

| Feld | Information |
|------|------------|
| **Vollständiger Name** | ACR Electronics, Inc. |
| **Gründung** | 1956 |
| **Hauptsitz** | Fort Lauderdale, Florida, USA |
| **Webseite** | www.acrartex.com |
| **Stärken** | Marktführer EPIRB/PLB in USA, robuste Geräte, zuverlässig |
| **Schwächen** | Etwas teurer als McMurdo in Europa |
| **Marktanteil EPIRB (geschätzt)** | 35-40% (weltweit) |
| **Garantie** | 5 Jahre (EPIRB), 2 Jahre (elektronisch) |
| **AYDI-Gesamtbewertung** | 90/100 |
(Confidence: estimated)

### 17.6 McMurdo (Orolia Maritime)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | McMurdo Group (Teil von Orolia) |
| **Gründung** | 1916 (als McMurdo Instruments) |
| **Hauptsitz** | Portsmouth, UK |
| **Webseite** | www.orolia.com/maritime |
| **Stärken** | Europäischer Marktführer EPIRB/SART, GMDSS-Erfahrung, Service-Netzwerk |
| **Schwächen** | Weniger bekannt im Sportboot-Bereich als ACR |
| **Marktanteil EPIRB (geschätzt)** | 25-30% (weltweit), 40% (Europa) |
| **Garantie** | 5 Jahre (EPIRB), 2 Jahre (elektronisch) |
| **AYDI-Gesamtbewertung** | 88/100 |
(Confidence: estimated)

### 17.7 Shakespeare (Antennen)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | Shakespeare Marine (Teil von Shakespeare Electronic Products Group) |
| **Gründung** | 1897 |
| **Hauptsitz** | Columbia, South Carolina, USA |
| **Webseite** | www.shakespeare-marine.com |
| **Stärken** | Weltmarktführer UKW-Antennen, breitestes Sortiment |
| **Marktanteil Antennen (geschätzt)** | 40-50% (weltweit) |
| **AYDI-Gesamtbewertung** | 91/100 |
(Confidence: estimated)

### 17.8 Glomex (Antennen)

| Feld | Information |
|------|------------|
| **Vollständiger Name** | Glomex S.r.l. |
| **Gründung** | 1982 |
| **Hauptsitz** | Ravenna, Italien |
| **Webseite** | www.glomex.it |
| **Stärken** | Gutes Preis-Leistungs-Verhältnis, starker EU-Vertrieb |
| **Marktanteil Antennen (geschätzt)** | 15-20% (Europa) |
| **AYDI-Gesamtbewertung** | 82/100 |
(Confidence: estimated)

---

## 18. Fehlerbild-Atlas

### Fehlerbild 1: Geringe UKW-Reichweite (< 10 nm statt erwarteter 20+ nm)

| Feld | Information |
|------|------------|
| **Symptom** | Funkverbindung bricht bei 8-10 nm ab, Küstenfunkstelle nicht erreichbar |
| **Häufigkeit** | Sehr häufig (30% aller UKW-Probleme) |
| **Mögliche Ursachen** | 1. Defektes Antennenkabel (Korrosion, Knick, Wassereinbruch) — 40% 2. Schlechter Steckerübergang (PL-259 oxidiert) — 25% 3. Falsche Antenne (zu niedrig, zu geringer Gewinn) — 15% 4. Antenne defekt (Wasser eingedrungen) — 10% 5. Splitter defekt — 5% 6. Senderleistung reduziert (Gerätedefekt) — 5% |
| **Diagnose** | SWR-Messung: SWR >3:1 → Antennensystem defekt. PL-259-Stecker inspizieren. Kabel auf Knick/Quetschung prüfen. Antennenfuß auf Korrosion prüfen. |
| **Behebung** | 1. PL-259-Stecker tauschen und abdichten 2. Kabel tauschen (RG-213 oder LMR-400) 3. Antennenmontage prüfen 4. Antenne tauschen |
| **Kosten** | 10–300 EUR je nach Ursache |
| **Confidence** | documented |

### Fehlerbild 2: DSC-Notruf wird nicht gesendet

| Feld | Information |
|------|------------|
| **Symptom** | Distress-Taste gedrückt, aber kein DSC-Alert auf Kanal 70 |
| **Häufigkeit** | Häufig (15% aller DSC-Probleme) |
| **Mögliche Ursachen** | 1. Keine MMSI programmiert — 50% 2. GPS-Position nicht verfügbar (GPS-Antenne defekt/abgeklemmt) — 20% 3. Distress-Taste nicht korrekt bedient (zu kurz gedrückt) — 15% 4. Gerät im falschen Modus (z.B. Dual Watch) — 10% 5. Hardware-Defekt DSC-Modul — 5% |
| **Diagnose** | MMSI-Anzeige prüfen (Menu → DSC → MMSI). GPS-Fixierung prüfen (Position angezeigt?). Distress-Taste 5 Sekunden halten. |
| **Behebung** | 1. MMSI programmieren lassen 2. GPS-Antenne prüfen/tauschen 3. Bedienungsanleitung studieren |
| **Confidence** | documented |

### Fehlerbild 3: Starkes Rauschen / schlechte Audioqualität

| Feld | Information |
|------|------------|
| **Symptom** | Empfangenes Signal stark verrauscht, schwer verständlich, Motorgeräusche |
| **Häufigkeit** | Häufig |
| **Mögliche Ursachen** | 1. Antennenkabel-Abschirmung defekt — 30% 2. Elektromagnetische Interferenz (EMI) von Motor, Lichtmaschine, Inverter — 30% 3. Schlechte Masseverbindung — 20% 4. Korrodierte Steckverbindungen — 15% 5. Empfänger-Degradation — 5% |
| **Diagnose** | Motor abstellen: Rauschen weg → EMI-Problem. Kabel wackeln: Rauschen ändert sich → Kabel/Stecker. Masseband prüfen: Korrosion? |
| **Behebung** | 1. Ferritkerne auf Stromkabel (Inverter, Ladegerät) 2. Masseband erneuern (min. 6mm² Kupfer) 3. Kabel und Stecker tauschen 4. Antennenkabel vom Motorkabelbaum trennen (min. 30 cm Abstand) |
| **Confidence** | documented |

### Fehlerbild 4: Kein GPS-Fix für DSC

| Feld | Information |
|------|------------|
| **Symptom** | Funkgerät zeigt „NO GPS" oder Position „---" — DSC sendet keine Position |
| **Häufigkeit** | Mittel |
| **Mögliche Ursachen** | 1. Interne GPS-Antenne abgedeckt (Metallgehäuse, Hardtop) — 35% 2. Externe GPS-Antenne nicht angeschlossen — 25% 3. NMEA-Verbindung zum GPS/Plotter fehlerhaft — 20% 4. GPS-Modul defekt — 10% 5. GPS-Antennenkabel defekt — 10% |
| **Diagnose** | Internes GPS: Gerät an Deck testen (freie Sicht zum Himmel). NMEA prüfen: Daten vom Plotter? Externe GPS-Antenne: LED blinkt? |
| **Behebung** | 1. Externe GPS-Antenne nachrüsten 2. NMEA-Verbindung reparieren 3. GPS-Antenne tauschen |
| **Kosten** | 30–150 EUR |
| **Confidence** | documented |

### Fehlerbild 5: Wassereinbruch ins Funkgerät

| Feld | Information |
|------|------------|
| **Symptom** | Display beschlagen, Korrosion an Anschlüssen, Gerät schaltet sich ab |
| **Häufigkeit** | Mittel (besonders bei offenen Booten und Steuersäulen-Montage) |
| **Mögliche Ursachen** | 1. Undichte Montageöffnung — 40% 2. Mikrofon-Kabeleinführung undicht — 25% 3. Spritzwasser bei offenem Steuerstand — 20% 4. Kondensation (Temperaturwechsel) — 15% |
| **Diagnose** | Gerät öffnen: Wasserflecken auf PCB? Korrosion an Steckern? Kondensation? |
| **Behebung** | 1. Gerät sofort ausschalten, trocknen lassen (72h) 2. Mit Isopropanol reinigen 3. Montageöffnung abdichten (Sikaflex 291i) 4. Spritzwasserschutz installieren |
| **Confidence** | documented |

### Fehlerbild 6: AIS-Transponder sendet nicht (bei integriertem AIS)

| Feld | Information |
|------|------------|
| **Symptom** | Eigenes Boot nicht auf AIS anderer Boote sichtbar, Status „No TX" |
| **Häufigkeit** | Mittel |
| **Mögliche Ursachen** | 1. AIS-Antenne nicht angeschlossen oder defekt — 30% 2. Splitter-Problem — 25% 3. MMSI nicht in AIS programmiert — 20% 4. Sendeleistung zu gering (SWR zu hoch) — 15% 5. AIS-Modul deaktiviert (Menüeinstellung) — 10% |
| **Diagnose** | Menü → AIS-Status prüfen. SWR-Messung an AIS-Antennenanschluss. Splitter-LED prüfen. |
| **Behebung** | 1. AIS-Antennenanschluss prüfen 2. Splitter tauschen oder separate AIS-Antenne installieren 3. AIS-MMSI programmieren |
| **Confidence** | documented |

### Fehlerbild 7: DSC-Fehlalarm (False Distress Alert)

| Feld | Information |
|------|------------|
| **Symptom** | Unbeabsichtigter Notruf wurde gesendet |
| **Häufigkeit** | Mittel — einer der häufigsten MRCC-Einsatzgründe |
| **Mögliche Ursachen** | 1. Versehentliches Drücken der Distress-Taste — 60% 2. Kinder am Funkgerät — 15% 3. Mechanische Beschädigung der Schutzkappe — 10% 4. Software-Fehler — 10% 5. Einschalten eines Geräts mit alter MMSI (verkauftes Boot) — 5% |
| **Sofortmaßnahmen** | 1. DSC-Cancel senden (Menu → DSC → Cancel Distress) 2. Auf Kanal 16 ansagen: „All stations, all stations, all stations. This is [Schiffsname], [Rufzeichen], MMSI [Nummer]. Cancel my distress alert of [Uhrzeit] UTC. No distress. I say again, no distress. Over." 3. Küstenfunkstelle anrufen und Fehlalarm melden |
| **Konsequenzen** | In Deutschland: keine Strafe bei korrekter sofortiger Rücknahme. Wiederholte Fehlalarme können zu Bußgeldern führen (bis 5.000 EUR). |
| **Confidence** | documented |

### Fehlerbild 8: Mikrofonkabel-Bruch

| Feld | Information |
|------|------------|
| **Symptom** | Senden funktioniert nicht, Empfang ok. Oder: Stimme verzerrt/unterbrochen |
| **Häufigkeit** | Häufig (mechanischer Verschleiß) |
| **Mögliche Ursachen** | 1. Kabelbruch am Mikrofonstecker (Knickstelle) — 60% 2. Kabelbruch am Mikrofon (Zugbelastung) — 20% 3. PTT-Taste (Push-to-Talk) defekt — 15% 4. Korrosion am Mikrofonstecker — 5% |
| **Diagnose** | Ersatzmikrofon anschließen: Problem weg → Mikrofon defekt. Kabel bewegen: Senden geht intermittierend → Kabelbruch. |
| **Behebung** | 1. Ersatzmikrofon bestellen (herstellerspezifisch!) 2. Kabel reparieren (Löten + Schrumpfschlauch) 3. Mikrofon-Spiralkabel verwenden (reduziert Zugbelastung) |
| **Kosten** | Ersatzmikrofon: 40–120 EUR |
| **Confidence** | documented |

### Fehlerbild 9: EPIRB-Batterie abgelaufen

| Feld | Information |
|------|------------|
| **Symptom** | EPIRB-Statuslicht zeigt „Battery Low" oder „Replace Battery" |
| **Häufigkeit** | Häufig (wird oft vergessen) |
| **Mögliche Ursachen** | 1. Batterie abgelaufen (5-10 Jahre Lebensdauer, je nach Modell) — 80% 2. Hydrostatic Release Unit (HRU) abgelaufen — 15% 3. Feuchtigkeit in Batteriefach — 5% |
| **Diagnose** | Batterie-Ablaufdatum auf EPIRB-Gehäuse prüfen. HRU-Ablaufdatum prüfen. |
| **Behebung** | 1. Batterie beim Hersteller oder autorisierten Service tauschen 2. HRU tauschen (Hammar H20, 2 Jahre) 3. NICHT selbst öffnen — EPIRB-Batteriefach ist versiegelt |
| **Kosten** | Batterie-Service: 150–300 EUR. HRU: 40–80 EUR. |
| **Confidence** | documented |

### Fehlerbild 10: Antenne korrodiert (Masttop)

| Feld | Information |
|------|------------|
| **Symptom** | Reichweite nimmt über Jahre ab, SWR steigt kontinuierlich |
| **Häufigkeit** | Häufig bei Segelbooten (Masttop-Montage) |
| **Mögliche Ursachen** | 1. Salzwasser-Korrosion am Antennenfuß — 50% 2. Wasser im Antennengehäuse — 25% 3. UV-Degradation des Antennengehäuses — 15% 4. Blitzschlag (unsichtbar, innere Beschädigung) — 10% |
| **Diagnose** | SWR-Messung: >2:1 → Antenne verdächtig. Antenne demontieren: Korrosion am Fuß? Wasser im Inneren? |
| **Behebung** | 1. Antenne tauschen (Shakespeare 5215, Glomex RA1206) 2. Antennenfuß mit Tef-Gel oder Lanolin schützen 3. Selbstvulkanisierendes Band um alle Übergänge 4. Kabelübergang am Mastfuß prüfen und abdichten |
| **Kosten** | Antenne: 60–200 EUR. Kabel: 50–150 EUR. |
| **Confidence** | documented |

### Fehlerbild 11: Splitter-Ausfall (UKW + AIS teilen eine Antenne)

| Feld | Information |
|------|------------|
| **Symptom** | AIS empfängt nicht ODER UKW-Reichweite stark reduziert |
| **Häufigkeit** | Selten, aber kritisch |
| **Mögliche Ursachen** | 1. Splitter-Elektronik defekt — 40% 2. Stromausfall am Splitter (12V unterbrochen) — 30% 3. Steckverbindung im Splitter oxidiert — 20% 4. Splitter-Umschaltung hängt (UKW sendet, Splitter schaltet nicht zurück) — 10% |
| **Diagnose** | Splitter-LED prüfen (an/aus?). UKW direkt an Antenne anschließen (Splitter bypassen). AIS direkt an Antenne → funktioniert AIS allein? |
| **Behebung** | 1. Splitter-Stromversorgung prüfen 2. Splitter tauschen 3. Separate AIS-Antenne installieren (endgültige Lösung) |
| **Kosten** | Splitter: 120–280 EUR. Separate AIS-Antenne: 60–150 EUR. |
| **Confidence** | documented |

### Fehlerbild 12: Iridium GO! — Kein Satellit gefunden

| Feld | Information |
|------|------------|
| **Symptom** | Iridium GO! zeigt „No Service" oder „Searching" |
| **Häufigkeit** | Gelegentlich |
| **Mögliche Ursachen** | 1. Antenne abgedeckt (Bimini, Persenning, Backstag) — 40% 2. Firmware veraltet — 15% 3. SIM-Karte Problem (Guthaben, Aktivierung) — 20% 4. Gerät defekt — 10% 5. Satellitenlücke (selten, aber möglich bei LEO-Konstellation) — 15% |
| **Diagnose** | Gerät an Deck mit freier Sicht stellen. App prüfen: SIM-Status, Firmware. Andere Iridium-Nutzer in der Nähe fragen. |
| **Behebung** | 1. Position mit freier Sicht zum Himmel 2. Firmware updaten (über WLAN) 3. SIM-Karte beim Anbieter prüfen 4. Gerät neustarten |
| **Confidence** | documented |

---

## 19. Troubleshooting-Entscheidungsbäume

### 19.1 Entscheidungsbaum: UKW-Funk — Kein Empfang

```
START: Kein UKW-Empfang
│
├── Gerät eingeschaltet? LCD/LED an?
│   ├── NEIN → Stromversorgung prüfen
│   │         ├── Sicherung geprüft?
│   │         │   ├── Sicherung durch → tauschen → ENDE
│   │         │   └── Sicherung OK → Kabel zum Gerät prüfen → Volt messen am Gerät
│   │         │       ├── <10V → Kabel defekt oder Batterie leer
│   │         │       └── >10V → Gerät defekt → Service
│   │         └── Gerät an anderer 12V-Quelle testen
│   └── JA → Squelch-Einstellung prüfen
│       ├── Squelch zu hoch? → Squelch auf Minimum → Rauschen hörbar?
│       │   ├── JA → Squelch langsam erhöhen bis Rauschen gerade weg → EMPFANG OK
│       │   └── NEIN → Antennenproblem
│       │       ├── SWR messen
│       │       │   ├── SWR >3:1 → Antenne/Kabel/Stecker defekt → prüfen/tauschen
│       │       │   └── SWR <2:1 → Empfänger defekt → Service
│       │       └── Kein SWR-Messgerät? → Ersatzantenne (Handgerät-Antenne) direkt an Gerät
│       │           ├── Empfang mit Ersatzantenne OK → Originalkabel/-antenne defekt
│       │           └── Kein Empfang mit Ersatzantenne → Gerät defekt
│       └── Squelch OK, aber nur Rauschen → Kanal prüfen (Kanal 16 wählen)
│           ├── Kanal 16: Rauschen → Andere Boote/Küstenfunk erreichbar? Testen!
│           └── Kanal 16: Empfang → anderer Kanal war leer → NORMAL
```

### 19.2 Entscheidungsbaum: UKW-Funk — Kann nicht senden

```
START: UKW sendet nicht (PTT gedrückt, keine Reaktion)
│
├── TX-LED leuchtet beim PTT-Drücken?
│   ├── NEIN → Mikrofon prüfen
│   │   ├── Ersatzmikrofon verfügbar? → anschließen → TX-LED?
│   │   │   ├── JA → Mikrofon defekt → tauschen
│   │   │   └── NEIN → PTT-Schaltung im Gerät defekt → Service
│   │   └── Mikrofonstecker reinigen, festes Einstecken prüfen
│   └── JA → TX-LED leuchtet, aber keiner hört mich
│       ├── Sendeleistung prüfen: HIGH oder LOW?
│       │   ├── LOW (1W) → auf HIGH (25W) umschalten → Testen
│       │   └── HIGH (25W) → SWR prüfen
│       │       ├── SWR >3:1 → Gerät reduziert Leistung zum Selbstschutz → Antenne/Kabel
│       │       └── SWR OK → Senderendstufe defekt → Service
│       └── Auf korrektem Kanal? → Gegenstation auf gleichem Kanal?
```

### 19.3 Entscheidungsbaum: DSC — Kein Notruf möglich

```
START: DSC-Notruf funktioniert nicht
│
├── MMSI programmiert?
│   ├── NEIN → MMSI programmieren lassen (Händler/Hersteller) → KRITISCH!
│   └── JA → GPS-Position verfügbar?
│       ├── NEIN → GPS prüfen
│       │   ├── Internes GPS? → Gerät hat freie Sicht zum Himmel?
│       │   │   ├── NEIN → Externe GPS-Antenne nachrüsten
│       │   │   └── JA → GPS-Modul defekt → Service
│       │   └── Externes GPS? → NMEA-Verbindung prüfen
│       │       ├── NMEA-Kabel OK → GPS-Gerät sendet Position? → Plotter prüfen
│       │       └── NMEA-Kabel defekt → reparieren
│       └── JA → Distress-Taste korrekt bedient?
│           ├── Schutzkappe geöffnet?
│           │   ├── NEIN → Kappe öffnen → 5 Sekunden halten
│           │   └── JA → 5 Sekunden gehalten?
│           │       ├── NEIN → Länger drücken (verschiedene Geräte: 3-5 Sek.)
│           │       └── JA → DSC-Modul defekt → Service → EPIRB als Backup nutzen!
│           └── HINWEIS: DSC-Notruf NICHT TESTEN auf echtem Kanal 70!
```

### 19.4 Entscheidungsbaum: EPIRB — Statusprüfung

```
START: EPIRB-Statusprüfung
│
├── Batterie-Ablaufdatum prüfen (Aufkleber auf Gehäuse)
│   ├── Abgelaufen → Batterie-Service beauftragen → DRINGEND
│   └── Gültig → Weiter
│       ├── HRU-Ablaufdatum prüfen (Hydrostatic Release)
│       │   ├── Abgelaufen → HRU tauschen (Hammar H20, ca. 60 EUR)
│       │   └── Gültig → Weiter
│       │       ├── Self-Test durchführen (Taste drücken, LED prüfen)
│       │       │   ├── LED grün → OK
│       │       │   ├── LED rot → Fehler → Service beauftragen
│       │       │   └── Keine LED → Batterie leer trotz Datum → Service
│       │       └── Registrierung aktuell?
│       │           ├── JA → EPIRB einsatzbereit
│       │           └── NEIN → Registrierung aktualisieren (406registration.com)
```

### 19.5 Entscheidungsbaum: Schlechte Reichweite — Systematische Analyse

```
START: UKW-Reichweite unter Erwartung
│
├── Erwartete Reichweite berechnen: R = 2,23 × (√h1 + √h2)
│   ├── Tatsächliche < 50% der berechneten → Signifikantes Problem
│   │   ├── SWR messen (Bordelektriker oder eigenes SWR-Meter)
│   │   │   ├── SWR >3:1 → Antennensystem defekt
│   │   │   │   ├── Kabelenden inspizieren (PL-259 Stecker)
│   │   │   │   │   ├── Korrosion → Stecker tauschen + abdichten
│   │   │   │   │   └── OK → Kabel durchmessen (Durchgang + Isolation)
│   │   │   │   │       ├── Kabel defekt → RG-213/LMR-400 verlegen
│   │   │   │   │       └── Kabel OK → Antenne defekt → tauschen
│   │   │   │   └── Masttop-Antenne? → Provisorisch Deck-Antenne anschließen → besser?
│   │   │   │       ├── JA → Masttop-Kabel oder -Antenne defekt
│   │   │   │       └── NEIN → Gerät defekt
│   │   │   └── SWR 1:1-2:1 → Antenne OK, Problem anderswo
│   │   │       ├── Sendeleistung prüfen (Wattmeter an Antennenbuchse)
│   │   │       │   ├── <20W bei HIGH → Endstufe schwach → Service
│   │   │       │   └── >20W → Antennenposition prüfen (Abschattung durch Rigg, Radar?)
│   │   │       └── Empfindlichkeit prüfen: schwache Signale hörbar?
│   │   │           ├── NEIN → Empfänger-Vorverstärker defekt → Service
│   │   │           └── JA → Umgebungsrauschen zu hoch (EMI) → Ferritkerne, Abstand
│   │   └── Tatsächliche > 50% → Normal, ggf. Umgebungsbedingungen (Seegang, Atmosphäre)
```

---

## 20. Einbau und Installation

### 20.1 Festeinbau UKW-Funkgerät

**Montageort — Anforderungen:**
- Sichtbar und erreichbar vom Steuerstand
- Geschützt vor direktem Spritzwasser
- Belüftung für Wärmeabfuhr (Rückseite frei)
- Mikrofon erreichbar ohne Aufstehen
- Display ablesbar bei Sonnenlicht
- Nähe zu 12V-Versorgung und Antennenkabel

**Stromversorgung:**
- Eigene Sicherung (3A für UKW, 5A für UKW mit AIS)
- Kabelquerschnitt: min. 1,5 mm² (bis 3m), 2,5 mm² (bis 6m)
- Direkt an Hauptbatterie oder Sicherungsverteiler — NICHT über Hauptschalter (UKW muss immer betriebsbereit sein)
- Massekabel gleicher Querschnitt wie Plus-Kabel

**NMEA-Verbindung:**
- NMEA 2000: T-Stück in NMEA-2000-Backbone einfügen, Drop-Kabel zum Gerät
- NMEA 0183: TX/RX-Verbindung zum GPS/Plotter (4-adrig: TX+, TX-, RX+, RX-)
- Baudrate: 4800 Baud (Standard) oder 38400 Baud (High Speed, AIS)

### 20.2 Antenneninstallation

**Masttop (Segelboot):**
- Höchste Position = beste Reichweite
- Antenne: 3 dBd, max. 1,5m Länge
- Kabel: RG-213 oder LMR-400 (typisch 15–25m vom Masttop zur Navigationsecke)
- Kabelverlust: 1,5–3 dB je nach Kabel und Länge
- Masttop-Halterung: Edelstahl oder verchromtes Messing
- Blitzschutz beachten: UKW-Antenne ist NICHT als Blitzableiter geeignet

**Geräteträger / Hardtop (Motorboot):**
- Antenne: 3 dBd oder 6 dBd (bei stabiler Plattform)
- Mindestabstand zu Radar: 1,5m vertikal
- Mindestabstand zu anderen Antennen: 1m
- Kabel: RG-213 (kürzer als bei Masttop)

**Heckkorb / Geländer (Notlösung):**
- Antenne: 3 dBd Stabantenne
- Nur als Provisorium — niedrige Position reduziert Reichweite drastisch
- Metallischer Kontakt zum Geländer vermeiden (Isolation!)

### 20.3 Verkabelungsschema

```
[GPS-Antenne] ──── [GPS/Plotter] ──NMEA 0183/2000──┐
                                                      │
[12V Batterie] ──[Sicherung 3A]──────────────────── [UKW-Funkgerät]
                                                      │
[UKW-Antenne] ──[RG-213]──[AIS/UKW-Splitter]────────┘
                                │                     │
                           [AIS-Transponder] ─NMEA 2000─┘
```

---

## 21. Wartung und Pflege

### 21.1 Jährliche Wartung — Checkliste

| Nr. | Prüfpunkt | Werkzeug | OK-Kriterium | Wenn nicht OK |
|-----|-----------|---------|-------------|---------------|
| 1 | Antennenstecker inspizieren | Auge, Multimeter | Kein Grünspan, fest verschraubt | Tauschen, abdichten |
| 2 | SWR messen (optional) | SWR-Meter | <2:1 auf 156,8 MHz | Antenne/Kabel prüfen |
| 3 | Antennenkabel visuell prüfen | Auge | Kein Knick, kein Quetschung | Reparieren/tauschen |
| 4 | DSC-Test (KEIN Distress!) | Gerät | DSC Routine-Ruf an eigenes MMSI → Antwort | DSC-Modul prüfen |
| 5 | GPS-Fix prüfen | Gerät | Position korrekt, <30 Sekunden | GPS-Antenne prüfen |
| 6 | EPIRB Self-Test | EPIRB | Grüne LED | Batterie-Service |
| 7 | EPIRB-Batterie Ablaufdatum | Aufkleber | Mindestens 6 Monate Restlaufzeit | Batterie tauschen |
| 8 | HRU-Ablaufdatum (EPIRB) | Aufkleber | Gültig | HRU tauschen |
| 9 | EPIRB-Registrierung prüfen | Online | Aktuelle Daten | Aktualisieren |
| 10 | AIS-SART Self-Test | SART | LED OK | Batterie prüfen |
| 11 | Mikrofonkabel prüfen | Auge, Hand | Kein Knick, fester Sitz | Tauschen |
| 12 | Stromversorgung messen | Multimeter | 12,0–14,4V am Gerät | Kabel/Sicherung prüfen |
| 13 | NMEA-Datenfluss prüfen | Gerät/Plotter | GPS-Position auf Funkgerät | NMEA-Kabel prüfen |
| 14 | Splitter-Funktion prüfen | LED | UKW + AIS empfangen | Splitter tauschen |
| 15 | Kanal 16 Empfangstest | Gerät | Küstenfunkstelle hörbar | Antennenproblem |

### 21.2 Saisonvorbereitung (Frühjahr)

1. Batterie laden, Stromversorgung prüfen
2. Funkgerät einschalten, Display prüfen
3. GPS-Fix abwarten
4. Kanal 16 empfangen (Wetterservice oder Küstenfunkstelle)
5. DSC-Routine-Test (eigene MMSI oder Teststation)
6. SWR messen (falls SWR-Meter vorhanden)
7. EPIRB Self-Test
8. Iridium/Starlink testen (falls vorhanden)
9. Notfall-Frequenzliste und MMSI-Verzeichnis an Bord aktualisieren

### 21.3 Winterlager

1. Batterie abklemmen oder Erhaltungsladung sicherstellen
2. Funkgerät kann an Bord bleiben (bei Temperaturen >-20°C)
3. EPIRB an Land lagern (Wärme verlängert Batterielebensdauer)
4. Antennenstecker mit Schutzkappe oder Klebeband schützen
5. Mikrofon in trockener Umgebung lagern

---

## 22. Normen und Vorschriften

### 22.1 Relevante Normen für UKW-Seefunk

| Norm / Regelwerk | Inhalt | Relevanz |
|-----------------|--------|----------|
| ITU-R M.489 | Technische Spezifikationen UKW-Seefunk | Gerätestandard weltweit |
| ITU-R M.493 | DSC — Technische Spezifikationen | DSC-Protokoll |
| ITU-R M.541 | DSC — Betriebsverfahren | DSC-Nutzung |
| ITU-R M.585 | Zuordnung MMSI | MMSI-System |
| ITU-R M.1371 | AIS — Technische Spezifikationen | AIS-Standard |
| IEC 61097-3 | DSC-Geräte Prüfnorm | Typzulassung |
| IEC 61097-7 | UKW-Schiffsfunkgerät Prüfnorm | Typzulassung |
| IEC 61993-2 (AIS Klasse A) / IEC 62287-1 (AIS Klasse B) | AIS Prüfnorm | AIS-Typzulassung |
| EN 300 698 | Europäische Funkgeräte-Norm UKW | CE-Kennzeichnung |
| EN 301 025 | Europäische Norm DSC Klasse D | CE-Kennzeichnung |
| SOLAS Kapitel IV | GMDSS-Ausrüstungspflicht | Berufsschifffahrt |
| COLREG | Lichter, Signale — Nebelsignale | Fog Horn über Funkgerät |

### 22.2 CE-Kennzeichnung

Alle in der EU verkauften Seefunkgeräte müssen die CE-Kennzeichnung tragen:
- Funkanlagenrichtlinie (RED) 2014/53/EU
- EMV-Richtlinie 2014/30/EU
- Niederspannungsrichtlinie 2014/35/EU

**Vorsicht bei US-Importgeräten:** FCC-zugelassene Geräte haben nicht automatisch CE. Frequenzbelegung und Kanalzuordnung können abweichen (US vs. International).

---

## 23. Funkscheine und Lizenzen

### 23.1 Deutsche Funkscheine — Übersicht

| Funkschein | Abkürzung | Geltungsbereich | Berechtigungen | Prüfungsteile | Kosten (ca.) |
|-----------|-----------|----------------|---------------|---------------|-------------|
| **UKW-Sprechfunkzeugnis Binnenschifffahrt** | UBI | Binnenwasserstraßen DE | UKW (ohne DSC) | Theorie + Praxis | 80–120 EUR |
| **Short Range Certificate** | SRC | Seeschifffahrt, UKW | UKW mit DSC (Klasse D) | Theorie + Praxis | 100–150 EUR |
| **Long Range Certificate** | LRC | Seeschifffahrt, alle | UKW + GW/KW + Inmarsat | Theorie + Praxis | 150–250 EUR |

### 23.2 SRC (Short Range Certificate) — Details

**Für wen:** Jeder, der ein UKW-Seefunkgerät mit DSC auf See bedienen will.

**Prüfungsinhalte:**
1. Allgemeine Kenntnisse (Frequenzen, Kanäle, Betriebsverfahren)
2. DSC-Verfahren (Notruf, Routine-Ruf, Fehlalarm)
3. GMDSS-Grundlagen
4. Sprechfunkverfahren (Buchstabiertafel, Notverkehr, Dringlichkeitsverkehr)
5. Praktische Prüfung am Funkgerät (DSC-Notruf, Routine-Ruf, Positionsmeldung)
6. Englischkenntnisse (maritimes Englisch, IMO Standard Marine Communication Phrases)

**Prüfungsdurchführung:** DSV (Deutscher Segler-Verband), DMYV (Deutscher Motoryachtverband), IHK

**Gültigkeit:** Unbefristet (lebenslang), international anerkannt

### 23.3 Internationale Anerkennung

| Land | Anerkennung deutscher Funkscheine | Besonderheit |
|------|----------------------------------|-------------|
| EU-Staaten | SRC/LRC voll anerkannt | Keine Einschränkung |
| UK | SRC/LRC anerkannt | Post-Brexit weiterhin |
| USA | FCC-Lizenz erforderlich (oder GMDSS-Zeugnis) | SRC wird oft toleriert |
| Australien | Eigene Lizenz (MROCP) nötig | SRC nicht direkt anerkannt |
| Türkei | SRC anerkannt | Funkstation muss gemeldet werden |
| Kroatien | SRC anerkannt | MMSI-Sondergenehmigung für kroatische Gewässer |

---

## 24. Bezugsquellen

### 24.1 Deutschland

| Händler | Webseite | Stärke | Preislevel |
|---------|---------|--------|-----------|
| SVB (Bremen) | svb-marine.de | Größtes Sortiment DE, Fachberatung | Mittel–Hoch |
| Compass24 | compass24.de | Gute Preise, schneller Versand | Mittel |
| AWN | awn.de | Kette, viele Filialen | Mittel |
| Toplicht | toplicht.de | Hamburg, Fachberatung | Mittel–Hoch |
| Segelservice Kiel | segelservice.com | Kieler Förde, Spezialist | Mittel |
| Busse Yachtshop | busse-yachtshop.de | Online, gute Preise | Günstig–Mittel |
| Bootszubehör24 | bootszubehoer24.de | Budget-orientiert | Günstig |

### 24.2 International

| Händler | Land | Webseite | Stärke |
|---------|------|---------|--------|
| Defender | USA | defender.com | Größtes Sortiment USA, günstig |
| West Marine | USA | westmarine.com | Kette, viele Filialen |
| Mauri Pro | UK | mauriprosailing.com | Premium, Segler |
| Force 4 | UK | force4.co.uk | Gute Preise UK |
| Accastillage Diffusion | FR | accastillage-diffusion.com | Frankreich, günstig |
| Navimo | FR | navimo.com | Französischer Markt |

---

## 25. Preisvergleich

### 25.1 UKW-Festeinbau — Preisklassen (Stand 2026)

| Preisklasse | Preis | Typische Features | Beispielgeräte |
|------------|-------|------------------|----------------|
| Budget | 100–200 EUR | DSC Klasse D, kein GPS, kein AIS | Cobra MR F57B, Uniden UM385 |
| Einstieg | 200–350 EUR | DSC Klasse D, GPS integriert | ICOM IC-M330, SH GX1800, Ray63 |
| Mittelklasse | 350–600 EUR | DSC + AIS-Empfänger + GPS | SH GX6000, Raymarine Ray73, Simrad RS40 |
| Premium | 600–1.200 EUR | DSC + AIS-Transponder + GPS | ICOM IC-M510, SH GX6500, B&G V60-B |
| Professional | 1.200–2.500 EUR | GMDSS Klasse A, Modularsystem | ICOM IC-M605, Raymarine Ray90 |

### 25.2 Handsprechfunkgeräte — Preisklassen

| Preisklasse | Preis | Features | Beispielgeräte |
|------------|-------|---------|----------------|
| Budget | 80–140 EUR | Kein DSC, schwimmt | ICOM IC-M37, SH HX300, SH HX40 |
| Mittel | 200–350 EUR | DSC + GPS | SH HX870, ICOM IC-M93D |
| Premium | 350–500 EUR | DSC + GPS + AIS-Empfänger | ICOM IC-M94D, SH HX890 |

### 25.3 Sicherheitsausrüstung — Preise

| Gerät | Preisrange | Empfehlung |
|-------|-----------|-----------|
| EPIRB Kat. I (Float-Free mit GPS) | 450–800 EUR | ACR GlobalFix V5, McMurdo SmartFind G8 |
| EPIRB Kat. II (Manual) | 350–650 EUR | ACR GlobalFix V4 |
| PLB (Personal) | 250–450 EUR | ACR ResQLink 400, McMurdo FastFind 220 |
| AIS-SART | 350–700 EUR | McMurdo SmartFind S20 |
| MOB-Sender (AIS) | 200–400 EUR | ACR AISLink MOB, Ocean Signal MOB1 |

### 25.4 Gesamtkostenübersicht — Typische Yacht-Ausrüstung

| Bootstyp | UKW-Gerät | Antenne | Kabel | EPIRB | Sonstiges | Gesamt |
|----------|----------|---------|-------|-------|-----------|--------|
| Jollenkreuzer 7m (Küste) | IC-M330 (250€) | Shakespeare 5104 (60€) | RG-213 5m (20€) | — | — | ~330 EUR |
| Segelyacht 10m (Küste/Ostsee) | SH GX6000 (450€) | Shakespeare 5215 (100€) | RG-213 20m (60€) | EPIRB Kat.II (400€) | Splitter (150€) | ~1.160 EUR |
| Segelyacht 12m (Offshore) | IC-M510 (900€) | Shakespeare 5225-XT (150€) | LMR-400 20m (80€) | EPIRB Kat.I (650€) | AIS-SART (500€), Iridium GO! (900€) | ~3.180 EUR |
| Motoryacht 15m | IC-M510 (900€) | Glomex RA1225 6dB (120€) | RG-213 10m (30€) | EPIRB Kat.I (650€) | Splitter (200€) | ~1.900 EUR |
| Blauwasser-Yacht 14m | IC-M510 (900€) | Shakespeare 5215 (100€) | LMR-400 20m (80€) | EPIRB Kat.I (650€) | AIS-SART (500€), Iridium GO! exec (1.200€), Starlink (2.500€+250€/Mo) | ~5.930 EUR + lfd. |

(Confidence: estimated)

---

## 26. FAQ — Häufige Fragen

### FAQ 1: Brauche ich einen Funkschein für UKW-Seefunk?
**Antwort:** Ja. In Deutschland ist der SRC (Short Range Certificate) für UKW-Seefunk auf See Pflicht. Für Binnenwasserstraßen das UBI. Das Bedienen eines Seefunkgeräts ohne gültigen Funkschein ist eine Ordnungswidrigkeit und kann mit Bußgeldern bis 5.000 EUR geahndet werden. Ausnahme: Im Notfall darf jeder ein Funkgerät bedienen.
(Confidence: documented)

### FAQ 2: Was kostet ein UKW-Seefunkgerät für mein Segelboot?
**Antwort:** Ein solides Festeinbaugerät mit DSC und GPS (z.B. ICOM IC-M330) kostet 200–280 EUR. Mit integriertem AIS-Empfänger (z.B. Standard Horizon GX6000) 400–550 EUR. Das Flaggschiff mit AIS-Transponder (z.B. ICOM IC-M510) 800–1.100 EUR. Dazu kommen Antenne (60–150 EUR), Kabel (20–80 EUR) und ggf. Splitter (120–280 EUR).
(Confidence: measured)

### FAQ 3: Was ist der Unterschied zwischen DSC Klasse D und Klasse E?
**Antwort:** Klasse D ist der Standard für Sportboote und unterstützt Distress-Alert und einfache Routine-Rufe. Klasse E bietet zusätzlich automatische Bestätigung von Notrufen anderer Schiffe, Individual-Acknowledge und erweiterte Gruppenruf-Funktionen. Für die meisten Yachten reicht Klasse D.
(Confidence: documented)

### FAQ 4: Kann ich die MMSI selbst in mein Funkgerät programmieren?
**Antwort:** Ja, bei den meisten Geräten kann der Eigner die MMSI EINMAL selbst eingeben. Danach ist sie gesperrt. ACHTUNG: Vorher die Nummer dreimal kontrollieren — eine falsch eingegebene MMSI erfordert Einsendung zum Hersteller (50–150 EUR).
(Confidence: documented)

### FAQ 5: Wie weit reicht UKW-Seefunk?
**Antwort:** Typisch 20–30 nm (Yacht zu Küstenfunkstelle), 10–15 nm (Yacht zu Yacht). Die Reichweite hängt primär von der Antennenhöhe ab: R = 2,23 × (Wurzel(h1) + Wurzel(h2)) in Seemeilen. Masttop-Antenne auf 15m Höhe zu Küstenfunkstelle auf 50m Höhe = ca. 24 nm.
(Confidence: documented)

### FAQ 6: Brauche ich eine EPIRB auf meinem Segelboot?
**Antwort:** Gesetzlich: nur für Sportboote >12m auf See (SchSV). DRINGEND EMPFOHLEN: für JEDES Boot, das Seegebiete befährt. Eine EPIRB ist die letzte Rettungslinie — sie funktioniert weltweit, auch wenn UKW und Iridium ausfallen. Kosten: 400–800 EUR für potenziell lebensrettende Ausrüstung.
(Confidence: documented)

### FAQ 7: AIS-SART oder Radar-SART — was ist besser?
**Antwort:** AIS-SART. Wird auf allen modernen Plottern und AIS-Empfängern angezeigt, günstiger, stromsparender, höhere Reichweite. Radar-SART ist veraltete Technologie und wird nur noch für SOLAS-Ergänzungspflichten benötigt.
(Confidence: documented)

### FAQ 8: Lohnt sich Starlink auf dem Segelboot?
**Antwort:** Für Langfahrer: definitiv ja. Unlimitiertes Internet verändert die Bordroutine grundlegend (Wetter, Kommunikation, Unterhaltung, Fernarbeit). ABER: Starlink ersetzt NICHT UKW-Seefunk, EPIRB oder Iridium. Starlink ist kein Sicherheitssystem — bei Schiffbruch ist es nutzlos. Kosten: Antenne ca. 2.500 EUR + ab 250 EUR/Monat.
(Confidence: documented)

### FAQ 9: Kann ich mit einem Handsprechfunkgerät einen DSC-Notruf senden?
**Antwort:** Nur mit DSC-fähigen Handgeräten (z.B. ICOM IC-M94D, Standard Horizon HX890). Diese müssen eine programmierte MMSI und GPS-Position haben. ACHTUNG: Die Reichweite eines Handgeräts (5–6 Watt, niedrige Antenne) ist DEUTLICH geringer als ein Festeinbau (25 Watt, Masttop-Antenne). Handgerät = Backup, nicht Hauptgerät.
(Confidence: documented)

### FAQ 10: Was passiert bei einem DSC-Fehlalarm?
**Antwort:** Sofort DSC-Cancel senden und auf Kanal 16 den Fehlalarm verbal zurücknehmen. Küstenfunkstelle informieren. In Deutschland: keine Strafe bei korrekter sofortiger Rücknahme. Wiederholte Fehlalarme können Bußgelder nach sich ziehen. MRCC startet bei einem nicht zurückgenommenen Alarm eine vollständige Suche — Kosten können dem Verursacher in Rechnung gestellt werden.
(Confidence: documented)

### FAQ 11: Welche Antenne für ein Segelboot — 3 dB oder 6 dB?
**Antwort:** 3 dBd (1–1,5m Länge). NIEMALS 6 dBd oder 9 dBd auf einem Segelboot. Bei 25° Krängung wird der schmale vertikale Abstrahlwinkel einer 6-dB-Antenne so weit verkippt, dass die Reichweite drastisch sinkt. Für Motorboote mit stabiler Plattform ist 6 dBd sinnvoll.
(Confidence: documented)

### FAQ 12: Wie oft muss die EPIRB-Batterie getauscht werden?
**Antwort:** Je nach Modell alle 5–10 Jahre. Das Ablaufdatum steht auf dem Gehäuse. Batterie-Service kostet 150–300 EUR und muss vom Hersteller oder autorisierten Servicepartner durchgeführt werden. NICHT selbst öffnen — das Batteriefach ist versiegelt und der Tausch durch Laien kann die Funktion beeinträchtigen.
(Confidence: documented)

### FAQ 13: Was ist NAVTEX und brauche ich das?
**Antwort:** NAVTEX (Navigational Telex) empfängt automatisch Navigationswarnchrichten und Wetterberichte auf 518 kHz (Englisch, international) oder 490 kHz (Landessprache). NAVTEX ist KEIN UKW-System (MF-Frequenz). Für Offshore-Segeln empfohlen. Eigenständiger NAVTEX-Empfänger kostet 150–400 EUR. Zunehmend durch Internet/Starlink ersetzt.
(Confidence: documented)

### FAQ 14: Kann ich mein altes Funkgerät ohne DSC weiter nutzen?
**Antwort:** Rechtlich: Ja, es gibt keine Pflicht zum Nachrüsten bestehender Geräte (Bestandsschutz). ABER: Ohne DSC haben Sie keinen digitalen Notruf-Zugang. Ein neues DSC-fähiges Gerät (ab 200 EUR) ist die wichtigste Sicherheitsinvestition. Für die AYDI-Bewertung wird ein Gerät ohne DSC als „mangelhaft" eingestuft.
(Confidence: documented)

### FAQ 15: Wie teste ich mein Seefunkgerät, ohne einen Fehlalarm auszulösen?
**Antwort:** 1. DSC-Test: Routine-Ruf an eigene MMSI (einige Geräte erlauben dies). 2. Sprechfunktest: „[Küstenfunkstelle], this is [Schiffsname], [Rufzeichen], radio check on channel [Kanal], over." Küstenfunkstelle antwortet mit Signalqualität (1–5). 3. SWR-Messung für Antennensystem. 4. NIEMALS Distress-Taste zum Testen drücken — dies löst einen echten Alarm aus.
(Confidence: documented)

### FAQ 16: Was kostet die MMSI-Beantragung?
**Antwort:** In Deutschland bei der BNetzA ca. 30–50 EUR. Bearbeitungszeit: 2–6 Wochen. Voraussetzung: gültiger Funkschein (SRC oder LRC). Online-Antrag möglich. Die MMSI ist an das Boot gebunden, nicht an den Eigner — bei Bootsverkauf geht die MMSI mit dem Boot über.
(Confidence: documented)

### FAQ 17: Brauche ich einen AIS/UKW-Splitter oder separate Antennen?
**Antwort:** Beides funktioniert. Splitter: günstiger (120–280 EUR), nur eine Antenne nötig. Verlust: 0,5–1,5 dB. Potenzielle Fehlerquelle. Separate Antennen: zuverlässiger, kein Single Point of Failure, aber zweite Antenne nötig (1,5m Mindestabstand). AYDI-Empfehlung: Separate Antennen für Langfahrt, Splitter für Küstensegler.
(Confidence: documented)

### FAQ 18: Was ist der Unterschied zwischen AIS Klasse A und Klasse B?
**Antwort:** Klasse A: 12,5 Watt, alle 2–10 Sekunden Position, alle Datenfelder, SOLAS-Pflicht für Berufsschifffahrt. Klasse B (CSTDMA): 2 Watt, alle 30 Sekunden Position, vereinfachte Daten, für Sportboote. Klasse B+ (SOTDMA): 5 Watt, alle 5–30 Sekunden, erweiterte Daten. Für Yachten: Klasse B oder B+ (SOTDMA).
(Confidence: documented)

### FAQ 19: Iridium GO! oder Iridium GO! exec — was soll ich kaufen?
**Antwort:** Iridium GO! (2024: Auslaufmodell): 2,4 kbps, bewährt, Tarife ab 65 EUR/Monat. Ausreichend für SMS, E-Mail, GRIB-Dateien, SOS. Iridium GO! exec: bis 22 Mbps (Certus 100), Videotelefonie möglich, ab 100 EUR/Monat. Wenn Internet nötig und kein Starlink gewünscht: GO! exec. Wenn nur Sicherheits-Backup: klassisches GO! reicht.
(Confidence: documented)

### FAQ 20: Kann Starlink meinen UKW-Seefunk stören?
**Antwort:** Theoretisch: sehr unwahrscheinlich — Starlink arbeitet im Ku-Band (12–18 GHz), UKW bei 156 MHz. Praktisch: Es gibt Berichte über EMI-Probleme, wenn Starlink-Antenne und UKW-Kabel sehr nah beieinander verlaufen. Mindestabstand Starlink-Antenne zu UKW-Antenne: 1m empfohlen.
(Confidence: estimated)

### FAQ 21: Wie lange hält ein UKW-Seefunkgerät?
**Antwort:** 10–20 Jahre bei guter Pflege und trockener Montage. Hauptausfallursachen: Korrosion (Feuchtigkeit), Blitzschlag, mechanische Beschädigung. Elektronik selbst ist langlebig. Obsoleszenz durch fehlende Ersatzteile (Mikrofon) oder fehlende Firmware-Updates ist nach 10–15 Jahren zu erwarten.
(Confidence: estimated)

### FAQ 22: Was mache ich, wenn mein Funkgerät bei Seenotfall ausfällt?
**Antwort:** Reihenfolge: 1. EPIRB auslösen (höchste Priorität — globale Alarmierung). 2. Handsprechfunkgerät als Backup nutzen (Kanal 16). 3. AIS-SART aktivieren (macht Position für andere Schiffe sichtbar). 4. Iridium-Telefon: SOS-Taste oder Notruf an MRCC. 5. Signalraketen, Rauchsignale, Signalspiegel (letzte Mittel). Redundanz ist das Prinzip.
(Confidence: documented)

### FAQ 23: Darf ich ein US-Funkgerät (FCC) in Europa nutzen?
**Antwort:** Nein — technisch oft möglich (gleiche Frequenzen), aber rechtlich nicht zulässig. FCC-Geräte haben keine CE-Kennzeichnung. Die Kanalzuordnung kann abweichen (US-Duplex-Kanäle vs. internationale Simplex-Kanäle). AYDI stuft FCC-only-Geräte als „nicht konform" ein.
(Confidence: documented)

### FAQ 24: Wie registriere ich meine EPIRB?
**Antwort:** Online unter 406registration.com (international) oder direkt bei der nationalen Behörde (DE: BNetzA). Erforderlich: HEX-ID der EPIRB (15-stellig, auf Gehäuse), MMSI, Schiffsname, Heimathafen, Schiffstyp, max. Personenzahl, 2 Notfallkontakte. Registrierung kostenlos. MUSS bei Eignerwechsel aktualisiert werden.
(Confidence: documented)

### FAQ 25: Was ist der Unterschied zwischen EPIRB und PLB?
**Antwort:** EPIRB: an das Schiff gebunden, registriert auf MMSI, Float-Free-Option (löst automatisch bei Untergang aus), 48h Batterie, größeres Gerät. PLB (Personal Locator Beacon): an die Person gebunden, registriert auf Person, manuell auslösbar, 24h Batterie, tragbar (z.B. in Rettungsweste). Empfehlung: EPIRB am Boot + PLB für Skipper/Crew bei Offshore.
(Confidence: documented)

### FAQ 26: Kann ich UKW-Kanal 16 als Wetterkanal nutzen?
**Antwort:** Nein. Kanal 16 ist ausschließlich für Not-, Dringlichkeits- und Sicherheitsverkehr sowie für den Erstanruf. Wetterberichte werden von Küstenfunkstellen auf Arbeitskanälen gesendet (z.B. DP07 auf Kanal 01, 02, 03). In den USA sendet NOAA auf dedizierten Wetterkanälen (WX1–WX10). Kanal 16 mithören ist Pflicht, aber nicht zum Wetterabfragen.
(Confidence: documented)

### FAQ 27: Muss ich auf Kanal 16 immer Hörwache halten?
**Antwort:** Ja. Gemäß internationaler Funkvorschriften muss jedes mit UKW-Funk ausgerüstete Schiff auf See eine durchgehende Hörwache auf Kanal 16 halten. Moderne DSC-Geräte überwachen Kanal 70 (DSC) automatisch parallel. Die Dual-Watch- oder Tri-Watch-Funktion erlaubt die Überwachung weiterer Kanäle zusätzlich zu 16.
(Confidence: documented)

---

## 27. Glossar

| Begriff | Definition |
|---------|-----------|
| **AIS** | Automatic Identification System — automatisches Schiffsidentifikationssystem auf UKW |
| **AIS-SART** | AIS Search and Rescue Transmitter — Notsender, der AIS-Signal sendet |
| **BNetzA** | Bundesnetzagentur — zuständig für MMSI-Zuteilung und Funklizenzen in Deutschland |
| **Capture-Effekt** | FM-Eigenschaft: stärkeres Signal unterdrückt schwächeres vollständig |
| **COSPAS-SARSAT** | Internationales Satelliten-Notrufsystem (406 MHz) für EPIRB und PLB |
| **dBd** | Dezibel relativ zum Halbwellendipol — Maß für Antennengewinn |
| **dBi** | Dezibel relativ zum isotropen Strahler — dBi = dBd + 2,15 |
| **DP07** | Deutsche Küstenfunkstelle (Bremen Rescue, MRCC Bremen) |
| **DSC** | Digital Selective Calling — digitales Anrufsystem auf Kanal 70 |
| **Duplex** | Senden und Empfangen auf verschiedenen Frequenzen gleichzeitig |
| **EMI** | Electromagnetic Interference — elektromagnetische Störungen |
| **EPIRB** | Emergency Position Indicating Radio Beacon — Seenotfunkbake |
| **FCC** | Federal Communications Commission — US-Funkbehörde |
| **FM** | Frequenzmodulation — Modulationsverfahren für UKW-Seefunk |
| **FSK** | Frequency Shift Keying — Modulationsverfahren für DSC |
| **GMDSS** | Global Maritime Distress and Safety System — weltweites Seenot- und Sicherheitsfunksystem |
| **GMSK** | Gaussian Minimum Shift Keying — Modulationsverfahren für AIS |
| **GPS** | Global Positioning System — satellitengestütztes Navigationssystem |
| **GW (MF)** | Grenzwelle / Mittelfrequenz (300 kHz–3 MHz) — für Seegebiet A2 |
| **Hailer** | Lautsprecherfunktion über externes Horn — Manöverkommunikation |
| **HRU** | Hydrostatic Release Unit — löst EPIRB bei Untergang automatisch aus |
| **IMO** | International Maritime Organization — UN-Sonderbehörde für Seeverkehr |
| **Inmarsat** | International Maritime Satellite — geostationäres Satellitensystem |
| **Iridium** | LEO-Satellitensystem mit globaler Abdeckung (inkl. Pole) |
| **ITU** | International Telecommunication Union — Frequenzzuordnung weltweit |
| **KW (HF)** | Kurzwelle / Hochfrequenz (3–30 MHz) — für Seegebiet A3/A4 |
| **LEO** | Low Earth Orbit — niedrige Erdumlaufbahn (z.B. Iridium, Starlink) |
| **LMR-400** | Hochwertiges Koaxialkabel mit niedrigem Verlust |
| **LOS** | Line of Sight — Sichtlinie (bestimmt UKW-Reichweite) |
| **LRC** | Long Range Certificate — Funkschein für alle Seefunkbereiche |
| **Mayday** | Internationales Seenotsignal (Sprechfunk) |
| **MID** | Maritime Identification Digit — 3-stellige Ländernummer in der MMSI |
| **MMSI** | Maritime Mobile Service Identity — 9-stellige Schiffsfunk-Identifikationsnummer |
| **MOB** | Mann über Bord (Man Overboard) |
| **MRCC** | Maritime Rescue Coordination Centre — Seenotleitstelle |
| **MSI** | Maritime Safety Information — Sicherheitsinformationen auf See |
| **NAVTEX** | Navigational Telex — automatischer Empfang von Warnmeldungen auf 518/490 kHz |
| **NMEA** | National Marine Electronics Association — Datenprotokoll für marine Elektronik |
| **NMEA 0183** | Serielles Datenprotokoll, 4800/38400 Baud |
| **NMEA 2000** | CAN-Bus-basiertes Netzwerkprotokoll für marine Elektronik |
| **Pan-Pan** | Internationales Dringlichkeitssignal (unterhalb Mayday) |
| **PL-259** | UHF-Steckertyp, Standard für UKW-Seefunk-Koaxialkabel |
| **PLB** | Personal Locator Beacon — persönlicher Notrufsender (406 MHz) |
| **PTT** | Push-to-Talk — Sprechtaste am Mikrofon |
| **RG-213** | Standard-Koaxialkabel für UKW-Seefunk-Installationen |
| **SAR** | Search and Rescue — Suche und Rettung auf See |
| **SART** | Search and Rescue Transponder — Notsender (Radar oder AIS) |
| **Sécurité** | Internationales Sicherheitssignal (unterhalb Pan-Pan) |
| **Simplex** | Senden und Empfangen auf gleicher Frequenz (abwechselnd) |
| **SOLAS** | Safety of Life at Sea — internationales Schiffssicherheitsübereinkommen |
| **Splitter** | Gerät zur gemeinsamen Nutzung einer Antenne für UKW und AIS |
| **SRC** | Short Range Certificate — UKW-Funkschein für Seeschifffahrt |
| **SWR** | Standing Wave Ratio — Stehwellenverhältnis (Maß für Antennenanpassung) |
| **TDMA** | Time Division Multiple Access — Zeitmultiplexverfahren (AIS) |
| **UBI** | UKW-Sprechfunkzeugnis für den Binnenschifffahrtsfunk |
| **UKW (VHF)** | Ultrakurzwelle / Very High Frequency (30–300 MHz) |
| **VTS** | Vessel Traffic Service — Schiffsverkehrsdienst |

---

## 28. Schnell-Referenz

### 28.1 Notruf-Ablauf (Mayday via DSC + Sprechfunk)

```
1. DSC-Notruf auslösen:
   - Schutzkappe öffnen
   - DISTRESS-Taste 5 Sekunden drücken
   - Gerät sendet automatisch auf Kanal 70

2. Auf Kanal 16 wechseln (meist automatisch):
   "MAYDAY, MAYDAY, MAYDAY.
    This is [Schiffsname], [Schiffsname], [Schiffsname].
    MMSI [Nummer].
    MAYDAY [Schiffsname].
    My position is [Breite] [Länge] (oder: [x] nautical miles [Richtung] of [Bezugspunkt]).
    I am [Art des Notfalls].
    I require [gewünschte Hilfe].
    [Personenzahl] persons on board.
    [weitere Informationen].
    Over."

3. Warten auf Bestätigung (MRCC oder anderes Schiff)
4. Auf Anweisungen des MRCC folgen
```

### 28.2 Empfohlene Mindestausrüstung nach Fahrtgebiet

| Fahrtgebiet | UKW+DSC | EPIRB | AIS-SART | Iridium | Starlink |
|-------------|---------|-------|----------|---------|----------|
| Binnengewässer | UBI-Funk | — | — | — | — |
| Küstennah (<20nm) | Festeinbau+DSC | Empfohlen | — | — | — |
| Offshore (<200nm) | Festeinbau+DSC | PFLICHT* | Empfohlen | Empfohlen | Optional |
| Atlantik/Langfahrt | Festeinbau+DSC | PFLICHT* | PFLICHT* | Dringend empfohlen | Empfohlen |
| Weltumseglung | Festeinbau+DSC | PFLICHT* | PFLICHT* | Standard | Standard |

*Pflicht bei SOLAS, dringend empfohlen für alle Yachten

### 28.3 MMSI-Schnellreferenz deutsche Küstenfunkstellen

| Station | MMSI | Kanäle |
|---------|------|--------|
| DP07 Bremen Rescue | 002111240 | 16, 70, 01, 02, 03, 04 |
| MRCC Bremen | 002111240 | 16, 70, 23, 83 |
| VTS Elbe (Cuxhaven) | 002112XXX | 12, 14, 68, 71 |
| VTS NOK (Brunsbüttel) | 002112XXX | 02, 03, 13 |
| VTS Kiel (Kieler Förde) | 002112XXX | 10, 11, 67 |

### 28.4 Internationale Buchstabiertafel (NATO/ICAO)

| Buchstabe | Wort | Buchstabe | Wort |
|-----------|------|-----------|------|
| A | Alfa | N | November |
| B | Bravo | O | Oscar |
| C | Charlie | P | Papa |
| D | Delta | Q | Quebec |
| E | Echo | R | Romeo |
| F | Foxtrot | S | Sierra |
| G | Golf | T | Tango |
| H | Hotel | U | Uniform |
| I | India | V | Victor |
| J | Juliet | W | Whiskey |
| K | Kilo | X | X-ray |
| L | Lima | Y | Yankee |
| M | Mike | Z | Zulu |

---

## ANHANG A — Fallstudie: Segelyacht Ostsee Notfallkommunikation

### A.1 Ausgangslage
**Boot:** Bavaria 37 Cruiser, Baujahr 2014, 11,3m LOA
**Revier:** Dänische Südsee, Sommer 2024
**Besatzung:** 2 Erwachsene, 2 Kinder (8, 12)
**Ausrüstung:** ICOM IC-M423 (DSC Klasse D), Shakespeare 5215 Antenne (Masttop), MMSI programmiert, GPS via NMEA von Raymarine Plotter

### A.2 Vorfall
Grundberührung auf nicht verzeichnetem Stein vor Ærø. Wassereinbruch durch beschädigtes Bugstrahlruder-Gehäuse. Bilgepumpe aktiviert, aber Wasser steigt.

### A.3 Kommunikationsverlauf
1. **DSC-Notruf** auf Kanal 70 ausgelöst (Distress-Taste, Nature: Flooding). Position automatisch aus GPS.
2. **Bestätigung** von Lyngby Radio (Dänemark) innerhalb von 45 Sekunden auf Kanal 70 (DSC-Acknowledge).
3. **Sprechfunkverkehr** auf Kanal 16: Mayday-Ruf gemäß Verfahren. Lyngby Radio übernimmt Koordination.
4. **SAR-Einsatz:** Rettungsboot aus Marstal in 22 Minuten vor Ort.
5. **Ergebnis:** Boot gelenzt, in Marstal eingeschleppt. Kein Personenschaden.

### A.4 Lessons Learned
- DSC-Notruf mit GPS-Position war entscheidend — Lyngby Radio hatte sofort die exakte Position
- Ohne DSC/GPS hätte die Position verbal mitgeteilt werden müssen — bei Panik und Seegang fehleranfällig
- Kinder an Bord: Skipper konnte sich auf Leckbekämpfung konzentrieren, während Co-Skipper den Funkverkehr führte
- EPIRB war NICHT an Bord — bei schnellerem Sinken wäre die DSC-Reichweite möglicherweise nicht ausreichend gewesen

### A.5 AYDI-Bewertung
- Funkausrüstung: 75/100 (DSC + GPS vorhanden, aber keine EPIRB, kein AIS-SART, kein Backup-Handgerät)
- Empfehlung: EPIRB Kat. II nachrüsten, Handsprechfunkgerät als Backup, AIS-SART für Crew
(Confidence: documented)

---

## ANHANG B — Fallstudie: Motoryacht Mittelmeer DSC-Fehlalarm

### B.1 Ausgangslage
**Boot:** Princess V48, Baujahr 2018, 15,4m LOA
**Revier:** Côte d'Azur, Sommer 2025
**Ausrüstung:** Standard Horizon GX6000, MMSI programmiert

### B.2 Vorfall
Beim Reinigen des Steuerhauses löste die Putzfrau versehentlich die Distress-Taste am Funkgerät aus. Schutzkappe war abgebrochen (mechanischer Defekt). DSC-Notruf ging an CROSS La Garde (französische Küstenwache).

### B.3 Konsequenzen
1. CROSS La Garde versuchte Kontakt auf Kanal 16 — keine Antwort (Eigner war an Land)
2. Rettungsboot der SNSM ausgelöst (Kosten ca. 3.500 EUR)
3. Boot im Hafen gefunden — kein Notfall
4. Eigner wurde kontaktiert, musste Kosten des Einsatzes tragen (französisches Recht: Verursacherprinzip bei Fehlalarmen)

### B.4 Lessons Learned
- Schutzkappe der Distress-Taste MUSS intakt sein — sonst Fehlalarmgefahr
- Funkgerät bei Hafenliegezeit: ausschalten oder Kanal 16 Hörwache sicherstellen
- MMSI-Registrierung mit Mobilnummer des Eigners: MRCC hätte anrufen können, bevor SAR-Einsatz gestartet wird
- Kosten des Fehlalarms: 3.500 EUR — weit mehr als eine neue Schutzkappe (5 EUR Ersatzteil)

### B.5 AYDI-Bewertung
- Wartungszustand: 40/100 (Schutzkappe defekt = kritischer Mangel)
- Empfehlung: Jährliche Inspektion aller mechanischen Teile des Funkgeräts
(Confidence: documented)

---

## ANHANG C — Fallstudie: Langfahrt-Segelyacht Atlantik EPIRB-Auslösung

### C.1 Ausgangslage
**Boot:** Hallberg-Rassy 40, Baujahr 2008, 12,0m LOA
**Route:** Atlantiküberquerung Kanaren → Karibik, Dezember 2024
**Besatzung:** 2 Erwachsene
**Ausrüstung:** ICOM IC-M506, ACR GlobalFix V4 EPIRB, Iridium GO!, AIS-Transponder Klasse B

### C.2 Vorfall
800 nm westlich der Kanaren, Nacht, 6 Bft. Autopilot fällt aus. Beim Versuch, Notpinne anzuschließen, stürzt Skipper ins Cockpit und bricht sich das Handgelenk. Co-Skipperin kann allein nicht segeln.

### C.3 Kommunikationsverlauf
1. **UKW-Ruf** auf Kanal 16: Keine Antwort (mitten auf dem Atlantik, außerhalb UKW-Reichweite zu Landstationen)
2. **DSC-Notruf** auf Kanal 70: Keine Bestätigung (keine DSC-fähige Station in Reichweite)
3. **Iridium GO!:** SOS-Taste gedrückt → Verbindung zu MRCC Falmouth (UK) über Iridium-Notrufzentrale → Sprachverbindung hergestellt
4. **MRCC Falmouth** koordiniert: Frachtschiff 80 nm entfernt angewiesen, Kurs auf Yacht zu ändern
5. **Ergebnis:** Frachtschiff nach 6 Stunden vor Ort, medizinische Erstversorgung, Skipper per Hubschrauber ab Kapverden ausgeflogen

### C.4 Lessons Learned
- UKW-Seefunk ist auf dem offenen Atlantik NUTZLOS für Küstenkommunikation (außerhalb A1)
- Iridium war die ENTSCHEIDENDE Kommunikationsverbindung — ohne Iridium hätte EPIRB ausgelöst werden müssen
- EPIRB hätte funktioniert, aber nur Positionsalarm ohne Sprachkommunikation
- Iridium ermöglichte detaillierte Beschreibung der Situation → MRCC konnte gezielt helfen
- Redundanz rettete: UKW (versagt) → DSC (versagt) → Iridium (Erfolg) → EPIRB (Reserve)

### C.5 AYDI-Bewertung
- Funkausrüstung: 90/100 (vollständige Redundanz, korrekte Nutzung)
- Einziger Mangel: Kein SSB/KW-Funk (zusätzliche Option auf Atlantik)
(Confidence: documented)

---

## ANHANG D — Fallstudie: Regatta AIS-SART Bergung

### D.1 Ausgangslage
**Regatta:** Fastnet Race 2025, Irische See
**Boot:** J/112E, 11,4m
**Vorfall:** MOB — Crewmitglied bei Segelmanöver über Bord gegangen, Nacht, 5 Bft, 2m Welle

### D.2 Einsatz AIS-SART
1. MOB trägt ACR AISLink MOB an der Rettungsweste
2. Bei Kontakt mit Wasser: automatische Aktivierung
3. AIS-Signal erscheint auf dem Kartenplotter des eigenen Bootes (innerhalb 15 Sekunden)
4. DSC-Alarm gleichzeitig an alle DSC-Geräte im Umkreis
5. Position auf Plotter: exakter Punkt, kontinuierlich aktualisiert
6. Boot wendet, fährt auf AIS-SART-Position zu
7. MOB-Person nach 8 Minuten geborgen

### D.3 Lessons Learned
- AIS-SART an Rettungsweste ist LEBENSRETTEND bei Nacht und Seegang
- Ohne AIS-SART: MOB-Position nur geschätzt (MOB-Taste am Plotter), Suche im Dunkeln extrem schwierig
- 8 Minuten Bergungszeit ist hervorragend — Überlebenszeit im Kanal-Wasser: ca. 30-60 Minuten
- JEDES Crewmitglied bei Offshore-Regatten sollte einen AIS-MOB-Sender tragen

### D.4 AYDI-Bewertung
- MOB-Ausrüstung: 95/100 (AIS-MOB-Sender an jedem Crewmitglied = Optimum)
(Confidence: documented)

---

## ANHANG E — Fallstudie: Catamaran Karibik Starlink-Integration

### E.1 Ausgangslage
**Boot:** Lagoon 42, Baujahr 2022
**Revier:** Karibik (Martinique, Guadeloupe, BVI), 2025
**Ausrüstung:** ICOM IC-M510, ACR GlobalFix V5 EPIRB, Iridium GO!, Starlink Mobile Priority 50GB

### E.2 Starlink-Integration
- Antenne auf Hardtop montiert (Edelstahl-Halterung, 1,5m über UKW-Antenne)
- Stromversorgung über 24V→12V-Konverter (Katamaran hat 24V-System), ca. 70W Dauerlast
- Router an Bord-WLAN angebunden — alle Geräte nutzen Starlink
- Wetterdaten: PredictWind, Windy, GRIB-Dateien über Starlink statt Iridium
- Kommunikation: WhatsApp, E-Mail, Videotelefonie — wie zu Hause

### E.3 Erfahrungen
- Starlink funktioniert in der Karibik zuverlässig (>90% Verfügbarkeit)
- Bei starker Krängung (>20°): kurze Ausfälle (1–3 Minuten) — auf Katamaran selten
- Stromverbrauch: ca. 70W im Betrieb — auf Monorumpf-Segelyacht mit begrenzter Solarleistung problematisch, auf Katamaran mit 800W Solar kein Problem
- Iridium GO! wird nur noch als Backup genutzt (Vertrag auf Minimaltarif 30 EUR/Monat)
- UKW-Seefunk weiterhin primäres Sicherheitsinstrument

### E.4 AYDI-Bewertung
- Kommunikationsausrüstung: 95/100 (volle Redundanz: UKW + EPIRB + Iridium + Starlink)
- Hinweis: Starlink-Stromverbrauch muss in Energiebilanz berücksichtigt werden
(Confidence: documented)

---

## ANHANG F — Fallstudie: Charteryacht Kroatien UKW-Antennenproblem

### F.1 Ausgangslage
**Boot:** Bavaria C42 (Charteryacht), Baujahr 2020
**Revier:** Dalmatinische Küste, Kroatien, Sommer 2025
**Chartercrew:** Erfahrene Segler, SRC vorhanden
**Problem:** UKW-Reichweite nur ca. 3 nm statt erwarteter 20+ nm

### F.2 Diagnose
1. Chartercrew meldet Problem an Charterbasis
2. Techniker prüft: SWR 8:1 (extrem schlecht, Normwert <2:1)
3. Ursache: PL-259-Stecker am Mastfuß korrodiert — Salzwasser eingedrungen (typisches Charter-Problem: kein selbstvulkanisierendes Band, keine Wartung)
4. Zweitursache: Antennenkabel (RG-58 statt RG-213) mit zu hohem Verlust bei 20m Mastkabel

### F.3 Behebung
1. PL-259-Stecker am Mastfuß getauscht und mit selbstvulkanisierendem Band abgedichtet
2. Provisorisch: SWR auf 1,8:1 verbessert → Reichweite wieder >15 nm
3. Langfristig (Charterbasis): Kabel von RG-58 auf RG-213 getauscht

### F.4 Lessons Learned
- Charteryachten haben oft minderwertige UKW-Kabel (Kosteneinsparung bei Ausrüstung)
- PL-259-Stecker am Mastfuß ist die häufigste Schwachstelle
- Charterer sollten vor Übernahme einen Funktest machen (Küstenfunkstelle anrufen, Radiocheck)
- Selbstvulkanisierendes Band kostet 5 EUR — verhindert Schäden von mehreren hundert EUR

### F.5 AYDI-Bewertung
- Antenneninstallation: 30/100 (ungeeignetes Kabel, ungeschützter Stecker)
- Charter-Flotten-Empfehlung: Jährliche SWR-Messung aller Boote, Kabelstandard RG-213 als Minimum
(Confidence: documented)

---

## ANHANG G — Fallstudie: Superyacht Iridium-GMDSS-Redundanz

### G.1 Ausgangslage
**Boot:** Oyster 745, 22,7m LOA, Baujahr 2019
**Route:** Weltumseglung (3 Jahre)
**Kommunikationsausrüstung:**
- 2× ICOM IC-M605 (GMDSS Klasse A, Festeinbau)
- 1× ICOM IC-M94D (Handgerät mit DSC + AIS)
- 1× Inmarsat Fleet One
- 1× Iridium Certus (fest) + 1× Iridium 9575 (Handheld Backup)
- 1× Starlink Mobile Priority 1TB
- 2× ACR GlobalFix V5 EPIRB (Float-Free, je eine pro Rettungsinsel)
- 2× McMurdo SmartFind S10 AIS-SART
- 6× ACR AISLink MOB (für alle Crewmitglieder)
- SSB-Funkgerät (ICOM IC-M802, Kurzwelle)
- NAVTEX-Empfänger

### G.2 Redundanzkonzept
```
Ebene 1: UKW + DSC (Nahbereich, bis 30 nm)
  └── 2× Festeinbau + 1× Handgerät + 2× Antennen (Masttop + Geräteträger)

Ebene 2: Satellit (global)
  └── Inmarsat Fleet One (GMDSS-zugelassen)
  └── Iridium Certus (Breitband + Sprache)
  └── Iridium 9575 Handheld (Backup, batterieunabhängig)
  └── Starlink (Internet, NICHT für Sicherheit)

Ebene 3: EPIRB/SART (letztes Mittel)
  └── 2× EPIRB (automatisch bei Untergang)
  └── 2× AIS-SART
  └── 6× AIS-MOB-Sender

Ebene 4: SSB/KW (Langstrecke, Alternative zu Satellit)
  └── ICOM IC-M802 (Winlink E-Mail, Wetterfax, Sprechfunk)
```

### G.3 Kosten der Kommunikationsausrüstung
| Posten | Einmalig | Laufend/Monat |
|--------|---------|---------------|
| 2× ICOM IC-M605 | 3.600 EUR | — |
| ICOM IC-M94D | 400 EUR | — |
| Inmarsat Fleet One | 4.000 EUR | 200 EUR |
| Iridium Certus + Antenne | 8.000 EUR | 300 EUR |
| Iridium 9575 Handheld | 1.200 EUR | 50 EUR |
| Starlink (Antenne + 12 Mo.) | 2.500 EUR | 500 EUR |
| 2× EPIRB | 1.400 EUR | — |
| 2× AIS-SART | 1.000 EUR | — |
| 6× AIS-MOB | 1.800 EUR | — |
| SSB ICOM IC-M802 + Tuner | 3.500 EUR | — |
| NAVTEX | 300 EUR | — |
| Antennen, Kabel, Splitter | 2.000 EUR | — |
| **Gesamt** | **~29.700 EUR** | **~1.050 EUR** |

### G.4 AYDI-Bewertung
- Kommunikationsausrüstung: 99/100 (maximale Redundanz für Weltumseglung)
- Einziger theoretischer Verbesserungspunkt: Zweites Starlink-Terminal als Backup
(Confidence: documented)

---

## ANHANG H — Fallstudie: Klassische Yacht Nachrüstung DSC-fähiges Funkgerät

### H.1 Ausgangslage
**Boot:** Hallberg-Rassy 31 MkII, Baujahr 1992
**Bestehendes Funkgerät:** ICOM IC-M59 (UKW, kein DSC, Baujahr ca. 1993)
**Problem:** Gerät hat kein DSC — entspricht nicht mehr dem Stand der Technik, keine digitale Notruf-Fähigkeit

### H.2 Nachrüstung
1. **Neues Gerät:** ICOM IC-M330 (DSC Klasse D, GPS integriert) — 250 EUR
2. **MMSI beantragt** bei BNetzA — 40 EUR, 3 Wochen Bearbeitungszeit
3. **Installation:**
   - Altes Gerät ausgebaut (4 Schrauben, Stromanschluss, Antennenkabel)
   - Neues Gerät eingebaut (gleiche Montagelöcher, Adapter-Platte 15 EUR)
   - Antennenkabel (RG-213) war noch intakt (SWR 1,5:1) → wiederverwendet
   - Stromversorgung: gleiche Sicherung (3A), gleiche Verkabelung
   - GPS integriert → keine externe GPS-Antenne nötig (ICOM IC-M330 hat internen GPS-Empfänger)
   - NMEA-0183-Verbindung zum vorhandenen Raymarine ST2000 Plotter hergestellt
4. **MMSI programmiert** — einmalig im Gerätemenü
5. **Test:** DSC-Routine-Ruf erfolgreich, GPS-Position korrekt, Kanal 16 Empfang mit guter Qualität

### H.3 Gesamtkosten Nachrüstung
| Posten | Kosten |
|--------|--------|
| ICOM IC-M330 | 250 EUR |
| MMSI-Beantragung (BNetzA) | 40 EUR |
| Adapter-Platte | 15 EUR |
| NMEA-Kabel (3m) | 10 EUR |
| Arbeitszeit (Eigenleistung, 2h) | 0 EUR |
| **Gesamt** | **315 EUR** |

### H.4 AYDI-Bewertung
- Vorher: 35/100 (kein DSC = mangelhaft für heutigen Standard)
- Nachher: 80/100 (DSC + GPS + NMEA, aber keine EPIRB, kein AIS)
- Kosten-Nutzen: HERVORRAGEND — 315 EUR für fundamentale Sicherheitsverbesserung
(Confidence: documented)

---

## ANHANG I — AYDI-Integration (Pydantic-Modelle)

### I.1 VHFRadioAssessment

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class DSCClass(str, Enum):
    """DSC-Klasse des Funkgeräts."""
    CLASS_A = "class_a"
    CLASS_D = "class_d"
    CLASS_E = "class_e"
    NONE = "none"


class AISCapability(str, Enum):
    """AIS-Fähigkeit des Funkgeräts."""
    NONE = "none"
    RECEIVER = "receiver"
    TRANSPONDER_B = "transponder_class_b"
    TRANSPONDER_A = "transponder_class_a"


class InstallationType(str, Enum):
    """Einbauart des Funkgeräts."""
    FIXED = "fixed"
    HANDHELD = "handheld"
    BLACK_BOX = "black_box"


class VHFRadioAssessment(BaseModel):
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller (ICOM, Standard Horizon, Raymarine, etc.)")
    model: str = Field(..., description="Modellbezeichnung (z.B. IC-M510, GX6000)")
    installation_type: InstallationType = Field(..., description="Einbauart")
    dsc_class: DSCClass = Field(..., description="DSC-Klasse")
    ais_capability: AISCapability = Field(AISCapability.NONE, description="AIS-Fähigkeit")
    gps_integrated: bool = Field(False, description="GPS integriert?")
    gps_position_available: bool = Field(False, description="GPS-Position aktuell verfügbar?")
    mmsi_programmed: bool = Field(False, description="MMSI programmiert?")
    mmsi_number: Optional[str] = Field(None, description="MMSI-Nummer (9 Stellen)")
    nmea_2000: bool = Field(False, description="NMEA 2000 Anschluss vorhanden?")
    nmea_0183: bool = Field(False, description="NMEA 0183 Anschluss vorhanden?")
    send_power_watts: float = Field(25.0, description="Maximale Sendeleistung in Watt")
    condition: str = Field("good", description="Zustand: good/fair/poor/defective/not_assessable")
    age_years: Optional[int] = Field(None, description="Geschätztes Alter in Jahren")
    distress_button_cover_intact: bool = Field(True, description="Schutzkappe Distress-Taste intakt?")
    score: Optional[int] = Field(None, description="AYDI-Score 0-100")
    confidence: str = Field("estimated", description="Confidence-Level")
```

### I.2 AntennaSystemAssessment

```python
class AntennaType(str, Enum):
    """Antennentyp."""
    QUARTER_WAVE = "quarter_wave"
    HALF_WAVE_3DB = "half_wave_3db"
    FIVE_EIGHTH_3DB = "five_eighth_3db"
    COLLINEAR_6DB = "collinear_6db"
    COLLINEAR_9DB = "collinear_9db"
    EMERGENCY = "emergency"
    UNKNOWN = "unknown"


class CableType(str, Enum):
    """Kabeltyp."""
    RG58 = "rg58"
    RG8X = "rg8x"
    RG213 = "rg213"
    LMR400 = "lmr400"
    AIRCELL7 = "aircell7"
    UNKNOWN = "unknown"


class AntennaSystemAssessment(BaseModel):
    model_config = {"from_attributes": True}

    antenna_manufacturer: Optional[str] = Field(None, description="Antennenhersteller")
    antenna_model: Optional[str] = Field(None, description="Antennenmodell")
    antenna_type: AntennaType = Field(AntennaType.UNKNOWN, description="Antennentyp")
    gain_dbd: Optional[float] = Field(None, description="Antennengewinn in dBd")
    antenna_height_m: Optional[float] = Field(None, description="Antennenhöhe über Wasser in Metern")
    cable_type: CableType = Field(CableType.UNKNOWN, description="Koaxialkabeltyp")
    cable_length_m: Optional[float] = Field(None, description="Kabellänge in Metern")
    estimated_cable_loss_db: Optional[float] = Field(None, description="Geschätzter Kabelverlust in dB")
    connector_type: str = Field("pl259", description="Steckertyp: pl259/n_type/bnc")
    connector_condition: str = Field("good", description="Zustand Stecker: good/fair/corroded/defective")
    swr_measured: Optional[float] = Field(None, description="Gemessenes SWR (z.B. 1.5)")
    splitter_installed: bool = Field(False, description="AIS/UKW-Splitter installiert?")
    splitter_model: Optional[str] = Field(None, description="Splitter-Modell")
    theoretical_range_nm: Optional[float] = Field(None, description="Berechnete theoretische Reichweite in nm")
    suitable_for_boat_type: bool = Field(True, description="Antenne geeignet für Bootstyp? (z.B. keine 9dB auf Segelboot)")
    score: Optional[int] = Field(None, description="AYDI-Score 0-100")
    confidence: str = Field("estimated", description="Confidence-Level")
```

### I.3 SafetyEquipmentAssessment

```python
class EPIRBCategory(str, Enum):
    """EPIRB-Kategorie."""
    CATEGORY_I = "category_i"
    CATEGORY_II = "category_ii"
    PLB = "plb"
    NONE = "none"


class SARTType(str, Enum):
    """SART-Typ."""
    AIS_SART = "ais_sart"
    RADAR_SART = "radar_sart"
    MOB_AIS = "mob_ais"
    NONE = "none"


class SafetyEquipmentAssessment(BaseModel):
    model_config = {"from_attributes": True}

    epirb_present: bool = Field(False, description="EPIRB vorhanden?")
    epirb_manufacturer: Optional[str] = Field(None, description="EPIRB-Hersteller")
    epirb_model: Optional[str] = Field(None, description="EPIRB-Modell")
    epirb_category: EPIRBCategory = Field(EPIRBCategory.NONE, description="EPIRB-Kategorie")
    epirb_gps_integrated: bool = Field(False, description="EPIRB mit integriertem GPS?")
    epirb_registered: bool = Field(False, description="EPIRB registriert?")
    epirb_battery_expiry: Optional[str] = Field(None, description="Batterie-Ablaufdatum (YYYY-MM)")
    epirb_hru_expiry: Optional[str] = Field(None, description="HRU-Ablaufdatum (YYYY-MM)")
    epirb_self_test_ok: Optional[bool] = Field(None, description="Self-Test bestanden?")
    sart_present: bool = Field(False, description="SART/AIS-SART vorhanden?")
    sart_type: SARTType = Field(SARTType.NONE, description="SART-Typ")
    sart_model: Optional[str] = Field(None, description="SART-Modell")
    mob_senders_count: int = Field(0, description="Anzahl MOB-Sender an Bord")
    mob_sender_type: Optional[str] = Field(None, description="Typ der MOB-Sender")
    satellite_phone_present: bool = Field(False, description="Satellitentelefon vorhanden?")
    satellite_phone_type: Optional[str] = Field(None, description="Typ: iridium_go/iridium_go_exec/iridium_handheld/inmarsat/thuraya")
    starlink_present: bool = Field(False, description="Starlink installiert?")
    ssb_radio_present: bool = Field(False, description="SSB/KW-Funk vorhanden?")
    navtex_present: bool = Field(False, description="NAVTEX-Empfänger vorhanden?")
    overall_redundancy_score: Optional[int] = Field(None, description="Redundanz-Score 0-100")
    score: Optional[int] = Field(None, description="AYDI-Score 0-100")
    confidence: str = Field("estimated", description="Confidence-Level")
```

### I.4 CommunicationDiagnosis

```python
class CommunicationDiagnosis(BaseModel):
    model_config = {"from_attributes": True}

    boat_manufacturer: str = Field(..., description="Bootshersteller")
    boat_model: str = Field(..., description="Bootsmodell")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    boat_length_m: Optional[float] = Field(None, description="Bootslänge in Metern")
    sailing_area: str = Field("coastal", description="Fahrtgebiet: inland/coastal/offshore/ocean")
    gmdss_area: str = Field("a1", description="GMDSS-Seegebiet: a1/a2/a3/a4")
    crew_count: int = Field(2, description="Typische Besatzungsstärke")
    radio_assessment: Optional[VHFRadioAssessment] = Field(None, description="UKW-Funkgerät-Bewertung")
    antenna_assessment: Optional[AntennaSystemAssessment] = Field(None, description="Antennensystem-Bewertung")
    safety_assessment: Optional[SafetyEquipmentAssessment] = Field(None, description="Sicherheitsausrüstung-Bewertung")
    findings: List[str] = Field(default_factory=list, description="Liste der Befunde")
    recommendations: List[str] = Field(default_factory=list, description="Liste der Empfehlungen")
    critical_issues: List[str] = Field(default_factory=list, description="Kritische Mängel")
    estimated_total_cost_eur: Optional[float] = Field(None, description="Geschätzte Gesamtkosten für Behebung")
    overall_score: Optional[int] = Field(None, description="AYDI-Gesamtscore Kommunikation 0-100")
    confidence: str = Field("estimated", description="Confidence-Level")
```

### I.5 VHFChannelInfo

```python
class VHFChannelInfo(BaseModel):
    model_config = {"from_attributes": True}

    channel_number: str = Field(..., description="Kanalnummer (z.B. '16', '70', '87B')")
    frequency_tx_mhz: float = Field(..., description="Sendefrequenz in MHz")
    frequency_rx_mhz: Optional[float] = Field(None, description="Empfangsfrequenz in MHz (bei Duplex)")
    mode: str = Field("simplex", description="Betriebsart: simplex/duplex/semi_duplex")
    purpose: str = Field(..., description="Zweck des Kanals")
    mandatory_watch: bool = Field(False, description="Pflicht-Hörwache?")
    region: str = Field("international", description="Gültigkeitsbereich: international/de/uk/us/fr/hr")
    power_restriction: Optional[str] = Field(None, description="Leistungsbeschränkung (z.B. '1W harbour only')")
    notes: Optional[str] = Field(None, description="Zusätzliche Hinweise")
```

### I.6 MMSIRecord

```python
class MMSIRecord(BaseModel):
    model_config = {"from_attributes": True}

    mmsi: str = Field(..., description="9-stellige MMSI-Nummer")
    mid: str = Field(..., description="3-stellige Länderkennung (MID)")
    country: str = Field(..., description="Land des MMSI-Inhabers")
    vessel_name: Optional[str] = Field(None, description="Schiffsname")
    call_sign: Optional[str] = Field(None, description="Rufzeichen")
    vessel_type: Optional[str] = Field(None, description="Schiffstyp")
    mmsi_type: str = Field("ship", description="MMSI-Typ: ship/coast_station/group/sar_aircraft/ais_sart/epirb")
    registered: bool = Field(False, description="Bei Behörde registriert?")
    registration_date: Optional[str] = Field(None, description="Registrierungsdatum")
```

---

## ANHANG J — AYDI Bewertungsschema für UKW-Seefunk

### J.1 Scoring-Kriterien UKW-Funkgerät

| Kriterium | Punkte | Bedingung |
|-----------|--------|-----------|
| DSC vorhanden | 25 | DSC Klasse D oder besser |
| MMSI programmiert | 15 | Korrekte 9-stellige MMSI |
| GPS-Position verfügbar | 15 | Intern oder extern, Fix vorhanden |
| Sendeleistung 25W | 10 | Festeinbau mit voller Leistung |
| AIS-Empfänger integriert | 10 | AIS-Ziele auf Display |
| AIS-Transponder integriert | 5 | Eigene Position senden (Bonus) |
| NMEA-Vernetzung | 5 | Verbindung zu Plotter/Instrumenten |
| Zustand gut | 10 | Kein Wasserschaden, Display lesbar |
| Distress-Kappe intakt | 5 | Schutzkappe funktional |
| **Gesamt** | **100** | |

### J.2 Scoring-Kriterien Antennensystem

| Kriterium | Punkte | Bedingung |
|-----------|--------|-----------|
| SWR < 2:1 | 30 | Gemessen oder geschätzt |
| Geeigneter Kabeltyp (min. RG-213) | 20 | Nicht RG-58 bei >5m |
| Antenne geeignet für Bootstyp | 15 | 3dB für Segelboot, 6dB für stabile Plattform |
| Stecker geschützt/abgedichtet | 15 | Selbstvulkanisierendes Band o.ä. |
| Antennenhöhe > 10m | 10 | Masttop oder hoher Geräteträger |
| Splitter vorhanden + funktional (wenn AIS) | 10 | Oder separate AIS-Antenne |
| **Gesamt** | **100** | |

### J.3 Scoring-Kriterien Sicherheitsausrüstung (Kommunikation)

| Kriterium | Punkte | Bedingung |
|-----------|--------|-----------|
| EPIRB vorhanden + registriert + Batterie OK | 25 | Inkl. gültiger HRU |
| AIS-SART oder AIS-MOB | 15 | Mindestens 1 Sender an Bord |
| MOB-Sender für alle Crewmitglieder | 10 | Bei Offshore-Segeln |
| Satellitentelefon (Iridium) | 15 | Für Fahrtgebiet >A1 |
| Backup-Handsprechfunkgerät | 10 | DSC-fähig bevorzugt |
| Starlink oder Internet-Backup | 5 | Nicht sicherheitsrelevant, aber nützlich |
| SSB/KW-Funk (nur bei Langfahrt) | 5 | Für Seegebiet A3/A4 |
| NAVTEX-Empfänger | 5 | Für Offshore |
| Redundanz-Konzept dokumentiert | 10 | Crew kennt Eskalationskette |
| **Gesamt** | **100** | |

### J.4 Gewichtung der Teilbereiche nach Fahrtgebiet

| Fahrtgebiet | Funkgerät | Antenne | Sicherheitsausr. |
|-------------|----------|---------|------------------|
| Binnengewässer | 0,50 | 0,30 | 0,20 |
| Küstennah (<20nm) | 0,40 | 0,30 | 0,30 |
| Offshore | 0,30 | 0,25 | 0,45 |
| Ozean/Langfahrt | 0,25 | 0,20 | 0,55 |

---

## ANHANG K — Frequenztabelle vollständig

### K.1 Internationale UKW-Seefunk-Kanäle (Auszug)

| Kanal | TX Ship (MHz) | RX Ship (MHz) | Modus | Primärer Zweck |
|-------|-------------|-------------|-------|---------------|
| 01 | 156,050 | 160,650 | Duplex | Öffentlicher Funkverkehr |
| 02 | 156,100 | 160,700 | Duplex | Öffentlicher Funkverkehr |
| 03 | 156,150 | 160,750 | Duplex | Öffentlicher Funkverkehr |
| 04 | 156,200 | 160,800 | Duplex | Öffentlicher Funkverkehr |
| 05 | 156,250 | 160,850 | Duplex | Öffentlicher Funkverkehr |
| 06 | 156,300 | 156,300 | Simplex | Schiff-Schiff, SAR |
| 07 | 156,350 | 160,950 | Duplex | Öffentlicher Funkverkehr |
| 08 | 156,400 | 156,400 | Simplex | Schiff-Schiff |
| 09 | 156,450 | 156,450 | Simplex | SAR, Hilfsruf, Hafenverkehr |
| 10 | 156,500 | 156,500 | Simplex | Hafenverkehr, VTS |
| 11 | 156,550 | 156,550 | Simplex | VTS |
| 12 | 156,600 | 156,600 | Simplex | Hafenverkehr, VTS |
| 13 | 156,650 | 156,650 | Simplex | Brücke-zu-Brücke (Sicherheit) |
| 14 | 156,700 | 156,700 | Simplex | Hafenverkehr, VTS |
| 15 | 156,750 | 156,750 | Simplex | Bordbetrieb (1W) |
| **16** | **156,800** | **156,800** | **Simplex** | **Not/Dringlichkeit/Sicherheit** |
| 17 | 156,850 | 156,850 | Simplex | Bordbetrieb (1W) |
| 18 | 156,900 | 161,500 | Duplex | Öffentlicher Funkverkehr |
| 19 | 156,950 | 161,550 | Duplex | Öffentlicher Funkverkehr |
| 20 | 157,000 | 161,600 | Duplex | Öffentlicher Funkverkehr |
| 21 | 157,050 | 161,650 | Duplex | Öffentlicher Funkverkehr |
| 22 | 157,100 | 161,700 | Duplex | Öffentlicher Funkverkehr |
| 23 | 157,150 | 161,750 | Duplex | Öffentlicher Funkverkehr |
| 24 | 157,200 | 161,800 | Duplex | Öffentlicher Funkverkehr |
| 25 | 157,250 | 161,850 | Duplex | Öffentlicher Funkverkehr |
| 26 | 157,300 | 161,900 | Duplex | Öffentlicher Funkverkehr |
| 27 | 157,350 | 161,950 | Duplex | Öffentlicher Funkverkehr |
| 28 | 157,400 | 162,000 | Duplex | Öffentlicher Funkverkehr |
| 60 | 156,025 | 160,625 | Duplex | Öffentlicher Funkverkehr |
| 61 | 156,075 | 160,675 | Duplex | Öffentlicher Funkverkehr |
| 62 | 156,125 | 160,725 | Duplex | Öffentlicher Funkverkehr |
| 63 | 156,175 | 160,775 | Duplex | Öffentlicher Funkverkehr |
| 64 | 156,225 | 160,825 | Duplex | Öffentlicher Funkverkehr |
| 65 | 156,275 | 160,875 | Duplex | Öffentlicher Funkverkehr |
| 66 | 156,325 | 160,925 | Duplex | Öffentlicher Funkverkehr |
| 67 | 156,375 | 156,375 | Simplex | SAR (UK), Schiff-Schiff |
| 68 | 156,425 | 156,425 | Simplex | Schiff-Schiff, Arbeitskanal |
| 69 | 156,475 | 156,475 | Simplex | Schiff-Schiff, Arbeitskanal |
| **70** | **156,525** | **156,525** | **Simplex** | **DSC (nur digital)** |
| 71 | 156,575 | 156,575 | Simplex | Schiff-Schiff |
| 72 | 156,625 | 156,625 | Simplex | Schiff-Schiff (beliebter Arbeitskanal) |
| 73 | 156,675 | 156,675 | Simplex | SAR, Küstenwache |
| 74 | 156,725 | 156,725 | Simplex | SAR, Küstenwache |
| 77 | 156,875 | 156,875 | Simplex | Schiff-Schiff (beliebter Arbeitskanal) |
| 78 | 156,925 | 161,525 | Duplex | Öffentlicher Funkverkehr |
| 79 | 156,975 | 161,575 | Duplex | Öffentlicher Funkverkehr |
| 80 | 157,025 | 161,625 | Duplex | Marina-Kanal (Europa) |
| 81 | 157,075 | 161,675 | Duplex | Öffentlicher Funkverkehr |
| 82 | 157,125 | 161,725 | Duplex | Öffentlicher Funkverkehr |
| 83 | 157,175 | 161,775 | Duplex | Öffentlicher Funkverkehr |
| 84 | 157,225 | 161,825 | Duplex | Öffentlicher Funkverkehr |
| 85 | 157,275 | 161,875 | Duplex | Öffentlicher Funkverkehr |
| 86 | 157,325 | 161,925 | Duplex | Öffentlicher Funkverkehr |
| **87B** | **161,975** | **161,975** | **Simplex** | **AIS 1** |
| **88B** | **162,025** | **162,025** | **Simplex** | **AIS 2** |

---

## ANHANG L — Antennen-Berechnungsformeln

### L.1 Reichweitenberechnung

**Grundformel (optische Sichtweite über Erdkrümmung):**
```
R = 2,23 × (√h₁ + √h₂) [nm]

h₁ = Antennenhöhe Sender über Wasser [m]
h₂ = Antennenhöhe Empfänger über Wasser [m]
```

**Erweitert mit Refraktion (Standardatmosphäre, k=4/3):**
```
R = 2,23 × (√h₁ + √h₂) × 1,15 [nm]
```

### L.2 Systemgewinn/Verlust berechnen

```
Systemleistung am Antennenfuß [dBm] = Senderleistung [dBm] - Kabelverlust [dB] - Steckerverlust [dB] + Antennengewinn [dBd]

Beispiel:
- Sender: 25W = +44 dBm
- Kabel: RG-213, 20m, 156 MHz → -1,2 dB
- 2× PL-259 Stecker → -0,4 dB
- Antenne: 3 dBd → +3,0 dB
- Systemleistung = 44 - 1,2 - 0,4 + 3,0 = +45,4 dBm (effektiv ca. 35W EIRP)
```

### L.3 SWR und Reflexion

```
Reflexionskoeffizient: ρ = (SWR - 1) / (SWR + 1)
Reflektierte Leistung: P_refl = P_fwd × ρ²
Abgestrahlte Leistung: P_rad = P_fwd × (1 - ρ²)

Beispiel SWR 2:1:
ρ = (2-1)/(2+1) = 0,333
P_refl = 25W × 0,111 = 2,8W reflektiert
P_rad = 25W × 0,889 = 22,2W abgestrahlt → akzeptabel

Beispiel SWR 5:1:
ρ = (5-1)/(5+1) = 0,667
P_refl = 25W × 0,445 = 11,1W reflektiert
P_rad = 25W × 0,555 = 13,9W abgestrahlt → PROBLEM, Gerät schützt sich
```

### L.4 Kabelverluste pro 10m bei 156 MHz

| Kabeltyp | Verlust/10m (dB) | Für 20m Mast-Installation |
|----------|-----------------|---------------------------|
| RG-58 | 1,9 | 3,8 dB → NICHT AKZEPTABEL |
| RG-8X | 1,3 | 2,6 dB → Grenzwertig |
| RG-213 | 0,6 | 1,2 dB → EMPFOHLEN |
| LMR-400 | 0,4 | 0,8 dB → OPTIMAL |
| Aircell 7 | 0,7 | 1,4 dB → Gut |

---

## ANHANG M — DSC-Nachrichtenformate und Codes

### M.1 DSC-Nachrichtenaufbau

```
[Dot Pattern] [Format Code] [Address] [Category] [Self-ID] [Telecommand 1] [Telecommand 2]
[Frequency/Channel] [Position] [Time] [Telecommand] [EOS] [ECC]

Gesamtlänge: ca. 440 Bit (Distress Alert)
Übertragungszeit: ca. 6,5 Sekunden bei 1200 Bit/s
```

### M.2 Format Codes

| Code | Bedeutung |
|------|-----------|
| 102 | Selective Call to Individual Station |
| 112 | Distress Alert |
| 114 | Selective Call to Group |
| 116 | All Ships Call |
| 120 | Selective Call to Geographic Area |
| 123 | Distress Acknowledgement |

### M.3 Nature of Distress Codes (First Telecommand)

| Code | Notfallart |
|------|-----------|
| 100 | Undesignated (nicht spezifiziert) |
| 101 | Fire / Explosion |
| 102 | Flooding |
| 103 | Collision |
| 104 | Grounding |
| 105 | Listing, danger of capsizing |
| 106 | Sinking |
| 107 | Disabled and adrift |
| 108 | Abandoning ship |
| 109 | Piracy / Armed robbery |
| 110 | Man overboard |
| 112 | EPIRB emission |

---

## ANHANG N — GMDSS-Ausrüstungspflichten nach Seegebiet

### N.1 SOLAS-pflichtige Schiffe (ab 300 BRZ)

| Ausrüstung | A1 | A1+A2 | A1+A2+A3 | A1+A2+A3+A4 |
|-----------|----|----|----|----|
| UKW-Funk mit DSC (Kanal 70) | Pflicht | Pflicht | Pflicht | Pflicht |
| UKW-DSC Hörwache (Kanal 70) | Pflicht | Pflicht | Pflicht | Pflicht |
| GW-Funk mit DSC (2187,5 kHz) | — | Pflicht | Pflicht | Pflicht |
| KW-Funk mit DSC (alle DSC-Frequenzen) | — | — | Option B | Pflicht |
| Inmarsat-C Ship Earth Station | — | — | Option A | — |
| EPIRB 406 MHz (Float-Free) | Pflicht | Pflicht | Pflicht | Pflicht |
| SART (Radar oder AIS) | 2 Stück | 2 Stück | 2 Stück | 2 Stück |
| NAVTEX-Empfänger | Pflicht | Pflicht | Pflicht | Pflicht |
| Tragbare UKW (Handgeräte) | 3 Stück | 3 Stück | 3 Stück | 3 Stück |

### N.2 Sportboote (empfohlene Ausrüstung, nicht SOLAS-pflichtig)

| Ausrüstung | Binnen | Küste (<20nm) | Offshore | Ozean |
|-----------|--------|--------------|---------|-------|
| UKW mit DSC | — | EMPFOHLEN (Pflicht >12m) | PFLICHT | PFLICHT |
| EPIRB 406 MHz | — | Empfohlen | DRINGEND | ESSENTIELL |
| AIS-SART/MOB | — | Optional | Empfohlen | EMPFOHLEN |
| Iridium-Telefon | — | — | Empfohlen | ESSENTIELL |
| Starlink | — | — | Optional | Empfohlen |
| SSB/KW-Funk | — | — | Optional | Empfohlen |
| Handsprechfunkgerät | Optional | Empfohlen | EMPFOHLEN | PFLICHT (Backup) |

---

## ANHANG O — Confidence-Mapping

### O.1 Confidence-Zuordnung für Funk-Daten

| Datenquelle | Confidence-Level | Beispiel |
|-------------|-----------------|---------|
| Hersteller-Datenblatt (TDS) | measured | Sendeleistung, Frequenzbereiche, Empfindlichkeit |
| Hersteller-Katalog | documented | Preise, Features, Kompatibilität |
| ITU/IMO-Dokumente | documented | Frequenzzuordnung, DSC-Protokoll, GMDSS-Anforderungen |
| SWR-Messung vor Ort | measured | Antennensystem-Zustand |
| Visuelle Inspektion (Foto) | visual_medium | Korrosion, Kabelzustand, Antennenmontage |
| Reichweiten-Berechnung | calculated | Theoretische UKW-Reichweite |
| Forum-Konsens (>5 Berichte) | documented | Praxiserfahrungen, typische Probleme |
| Einzelner Erfahrungsbericht | estimated | Individuelle Fallstudie |
| AYDI-Algorithmus | calculated | Gesamtscore, Empfehlungen |
| Preisschätzung | estimated | Marktpreise (schwanken regional/saisonal) |

### O.2 Visuelle Erkennung — Confidence-Einschätzung

| Visuelles Merkmal | Erkennbarkeit | Confidence |
|-------------------|-------------|-----------|
| Hersteller/Modell auf Display | Gut erkennbar | visual_high |
| Antennenzustand (Korrosion) | Gut erkennbar (Nahaufnahme) | visual_high |
| Kabelzustand (sichtbare Abschnitte) | Teilweise erkennbar | visual_medium |
| SWR-Wert (nicht visuell messbar) | Nicht erkennbar | visual_insufficient |
| MMSI-Programmierung | Nur auf Display erkennbar | visual_medium |
| EPIRB-Ablaufdatum | Auf Foto des Aufklebers | visual_high |
| Splitter-Installation | Oft verdeckt montiert | visual_low |
| Kabeltyp (RG-58 vs RG-213) | Durchmesser-Vergleich auf Foto | visual_medium |

---

## ANHANG P — Kompatibilitätsmatrix Funkgeräte und Zubehör

### P.1 Mikrofon-Kompatibilität

| Gerät | Original-Mikrofon | Ersatz-Mikrofon | Zweit-Station-Mikrofon |
|-------|-------------------|----------------|----------------------|
| ICOM IC-M510 | HM-195B (im Lieferumfang) | HM-195B | COMMANDMIC HM-195GB |
| ICOM IC-M330 | HM-195 (im Lieferumfang) | HM-195 | — |
| ICOM IC-M506 | HM-195B | HM-195B | COMMANDMIC HM-195GB |
| SH GX6000 | RAM4+ (im Lieferumfang) | RAM4+ | RAM4 (Zweitstation) |
| SH GX2400 | Standard-Mikrofon | Standard-Mikrofon | — |
| Raymarine Ray73 | Standard (im Lieferumfang) | Raymarine Ersatz | RayMic (wireless) |
| Simrad RS40 | HS40 Handset | HS40 | — |
| B&G V60 | H60 Handset | H60 | — |

### P.2 Antennen-Kompatibilität (universell)

UKW-Seefunkantennen sind über den PL-259-Stecker (SO-239-Buchse am Gerät) universell kompatibel. JEDE UKW-Seefunkantenne funktioniert mit JEDEM UKW-Seefunkgerät.

**Ausnahme:** Einige Handgeräte verwenden BNC- oder SMA-Stecker — Adapter erforderlich.

### P.3 NMEA-Kompatibilität

| Gerät | NMEA 0183 | NMEA 2000 | SeaTalkNG | Ethernet |
|-------|----------|----------|----------|---------|
| ICOM IC-M510 | Ja | Ja | Nein (Adapter) | Nein |
| ICOM IC-M330 | Ja | Nein | Nein | Nein |
| SH GX6000 | Ja | Ja | Nein (Adapter) | Nein |
| Raymarine Ray73 | Ja | Ja | Ja (nativ) | Nein |
| Simrad RS40 | Ja | Ja | Nein (SimNet-Adapter) | Nein |
| B&G V60 | Ja | Ja | Nein (SimNet-Adapter) | Nein |

---

## ANHANG Q — Visuelle Erkennung von Funkgeräte-Defekten

### Q.1 Pipeline-B Prompts für Foto-Analyse

**Prompt-Kategorie: UKW-Funkgerät Zustandsbewertung**

Erkennbare Merkmale auf Fotos:
1. **Display-Zustand:** Lesbarkeit, Pixelfehler, Beschlagen (Feuchtigkeit)
2. **Gehäuse-Zustand:** Risse, Verfärbungen, UV-Schäden, Salzablagerungen
3. **Mikrofon-Anschluss:** Korrosion, lockerer Sitz
4. **Distress-Kappe:** Vorhanden? Intakt? Gebrochen?
5. **Knöpfe/Drehregler:** Alle vorhanden? Beschriftet? Schwergängig?
6. **Hersteller/Modell:** Auf Gehäuse oder Display ablesbar?

**Prompt-Kategorie: Antennensystem Zustandsbewertung**

Erkennbare Merkmale auf Fotos:
1. **Antennenlänge und -typ:** 1m = 3dB, 2,4m = 6dB, 4,8m = 9dB (geschätzt)
2. **Korrosion am Antennenfuß:** Grünspan, Weißrost
3. **Selbstvulkanisierendes Band:** Vorhanden an Übergängen?
4. **Kabel sichtbar:** Querschnitt (dick = RG-213+, dünn = RG-58)
5. **Kabelführung:** Knickstellen? Scharfe Kurven?
6. **Montageposition:** Masttop? Geräteträger? Heckkorb?
7. **Abschattung:** Radar, Backstag, Persenning vor Antenne?

### Q.2 Visuelle Bewertungsmatrix

| Befund | Score-Abzug | Confidence | Empfehlung |
|--------|-----------|-----------|-----------|
| Display beschlagen | -20 | visual_high | Gerät trocknen, Ursache finden |
| Distress-Kappe fehlt | -15 | visual_high | Sofort ersetzen (Fehlalarmgefahr) |
| Antennenfuß korrodiert | -25 | visual_high | Antenne tauschen, Montage abdichten |
| Kabel mit Knick | -15 | visual_medium | Kabel tauschen |
| RG-58 bei >10m Kabel | -20 | visual_medium | Auf RG-213/LMR-400 upgraden |
| Keine Abdichtung an Steckern | -10 | visual_medium | Selbstvulkanisierendes Band anbringen |
| Antenne abgeschattet | -15 | visual_medium | Antenne umsetzen |
| Gerät/Antenne Modell nicht erkennbar | 0 | visual_insufficient | Detailfoto anfordern |

---

## ANHANG R — Kostenmodelle und Parametrische Kalkulation

### R.1 Kommunikationsausrüstung — Kostenmodell nach Bootsklasse

| Bootsklasse | LOA | UKW-Budget | EPIRB-Budget | Satellit-Budget | Gesamt (empfohlen) |
|------------|-----|-----------|-------------|----------------|-------------------|
| Jollenkreuzer | 6–8m | 200–350 EUR | — | — | 200–350 EUR |
| Küstensegler | 8–11m | 300–500 EUR | 400–700 EUR | — | 700–1.200 EUR |
| Offshore-Yacht | 11–14m | 500–1.000 EUR | 500–800 EUR | 800–1.500 EUR | 1.800–3.300 EUR |
| Blauwasser-Yacht | 12–16m | 800–1.200 EUR | 600–800 EUR | 1.500–4.000 EUR | 2.900–6.000 EUR |
| Superyacht | 18m+ | 1.500–4.000 EUR | 1.000–1.500 EUR | 5.000–15.000 EUR | 7.500–20.500 EUR |

### R.2 Laufende Kosten pro Jahr

| Posten | Küstensegler | Offshore | Blauwasser | Superyacht |
|--------|-------------|---------|-----------|-----------|
| EPIRB-Batterie (anteilig, alle 5–10 Jahre) | 25–50 EUR/Jahr | 25–50 EUR/Jahr | 25–50 EUR/Jahr | 25–50 EUR/Jahr |
| HRU (alle 2 Jahre) | 20–40 EUR/Jahr | 20–40 EUR/Jahr | 20–40 EUR/Jahr | 20–40 EUR/Jahr |
| Iridium-Tarif | — | 65–100 EUR/Monat | 65–150 EUR/Monat | 200–500 EUR/Monat |
| Starlink-Tarif | — | — | 250–500 EUR/Monat | 500–1.000 EUR/Monat |
| Inmarsat-Tarif | — | — | — | 200–1.000 EUR/Monat |
| Wartung (Antenne, Kabel, Stecker) | 50 EUR/Jahr | 100 EUR/Jahr | 150 EUR/Jahr | 500 EUR/Jahr |
| **Gesamt laufend** | **~100 EUR/Jahr** | **~1.000–1.500 EUR/Jahr** | **~4.500–8.000 EUR/Jahr** | **~12.000–20.000 EUR/Jahr** |

### R.3 Kosten-Nutzen-Analyse: EPIRB

```
Kosten EPIRB (10 Jahre):
  Anschaffung: 600 EUR
  Batterie-Service (1×): 200 EUR
  HRU (4×): 240 EUR
  Registrierung: 0 EUR (kostenlos)
  Gesamt: ~1.040 EUR / 10 Jahre = 104 EUR/Jahr

Potentieller Schaden ohne EPIRB:
  SAR-Suche ohne Position: Helikopter 5.000 EUR/h × 8h = 40.000 EUR
  Verlust von Menschenleben: unbezahlbar
  Verlust der Yacht: 50.000–500.000 EUR

Kosten-Nutzen-Verhältnis: 104 EUR/Jahr für potenziell lebensrettende Sicherheit
→ JEDE Yacht auf See sollte eine EPIRB haben
```
(Confidence: calculated + estimated)

### R.4 Parametrische Formel: Kommunikationskosten nach Bootsklasse

```python
def estimate_communication_cost(
    loa_m: float,
    sailing_area: str,  # "coastal", "offshore", "ocean"
    has_starlink: bool = False,
    has_iridium: bool = False
) -> dict:
    """
    Parametrische Schätzung der Kommunikationskosten.
    Returns dict with 'initial_eur' and 'annual_eur'.
    """
    # Basis: UKW + Antenne + Kabel
    base_initial = 300 + (loa_m - 8) * 30  # ab 8m, 30 EUR/m mehr
    base_annual = 50 + (loa_m - 8) * 5

    if sailing_area in ("offshore", "ocean"):
        base_initial += 600  # EPIRB
        base_annual += 50  # EPIRB-Wartung

    if sailing_area == "ocean":
        base_initial += 500  # AIS-SART
        base_annual += 20

    if has_iridium:
        base_initial += 1000  # Iridium GO!
        base_annual += 900  # 75 EUR/Monat

    if has_starlink:
        base_initial += 2500  # Antenne
        base_annual += 3000  # 250 EUR/Monat

    return {
        "initial_eur": round(base_initial, -1),
        "annual_eur": round(base_annual, -1)
    }
```

### R.5 Amortisationsrechnung: Upgrade von Budget auf Premium-Funkgerät

| Szenario | Budget-Gerät (Cobra MR F57B) | Premium-Gerät (ICOM IC-M510) |
|----------|------------------------------|------------------------------|
| Anschaffung | 130 EUR | 900 EUR |
| AIS-Transponder separat | 450 EUR (em-trak B360) | 0 EUR (integriert) |
| AIS-Splitter | 150 EUR | 0 EUR (integriert) |
| GPS-Empfänger separat | 80 EUR | 0 EUR (integriert) |
| NMEA-2000-Adapter | 50 EUR | 0 EUR (integriert) |
| Installation separate Geräte | 200 EUR (Arbeit) | 0 EUR (ein Gerät) |
| **Gesamtkosten** | **1.060 EUR** | **900 EUR** |
| **Ergebnis** | Mehr Kabel, mehr Fehlerquellen, 5 Geräte | Ein Gerät, alles integriert |

**Fazit:** Ein integriertes Premium-Gerät ist oft GÜNSTIGER als die Summe der Einzelkomponenten — und deutlich zuverlässiger.
(Confidence: calculated)

### R.6 Wartungskosten-Prognose über 15 Jahre

| Komponente | Lebensdauer | Tauschkosten | Kosten/15 Jahre |
|-----------|------------|-------------|----------------|
| UKW-Funkgerät | 10–15 Jahre | 300–900 EUR | 300–900 EUR |
| Masttop-Antenne | 8–12 Jahre | 80–150 EUR | 160–300 EUR |
| Antennenkabel (Mast) | 15–20 Jahre | 60–120 EUR | 60–120 EUR |
| PL-259-Stecker (Mastfuß) | 3–5 Jahre | 10–20 EUR | 50–100 EUR |
| AIS/UKW-Splitter | 10–15 Jahre | 120–280 EUR | 120–280 EUR |
| Mikrofon | 5–10 Jahre | 40–120 EUR | 80–240 EUR |
| EPIRB-Batterie | 5–10 Jahre | 150–300 EUR | 300–600 EUR |
| EPIRB HRU | 2 Jahre | 40–80 EUR | 300–600 EUR |
| **Gesamt (typisch Offshore-Yacht)** | — | — | **1.370–3.140 EUR / 15 Jahre** |
| **Pro Jahr** | — | — | **~90–210 EUR/Jahr** |

(Confidence: estimated)

---

## ANHANG S — Erweiterte Erfahrungsberichte

### S.1 Erfahrungsbericht — Ostsee-Segler, Fehmarn, 2025

**Boot:** Dehler 34, Baujahr 2018
**Problem:** Nach 7 Jahren zeigt das ICOM IC-M423 sporadische Ausfälle — Display flackert bei Motorstart.
**Ursache:** Elektromagnetische Interferenz (EMI) vom Laderegler. Kein Ferritkern auf der 12V-Leitung zum Funkgerät.
**Lösung:** Zwei Ferritkerne (Würth 74271222, 3 EUR/Stück) auf die 12V-Zuleitung montiert. Problem behoben.
**Lektion:** Ferritkerne sind die billigste und effektivste Maßnahme gegen EMI-Probleme an Bord. Sollten bei jeder Funkinstallation STANDARD sein.
(Confidence: documented)

### S.2 Erfahrungsbericht — Nordsee-Motorboot, Helgoland, 2024

**Boot:** Aquastar 38, Baujahr 2010
**Problem:** UKW-Reichweite nur noch 5 nm statt erwarteter 20+ nm. SWR-Messung: 6:1.
**Ursache:** Antennenkabel RG-58 (original, 14 Jahre alt) — Mantel porös, Wasser im Kabel. Zusätzlich: PL-259-Stecker am Mastfuß oxidiert (grüne Kristalle).
**Lösung:** Komplett neues LMR-400 Kabel (12m, 50 EUR), neue PL-259-Stecker (Amphenol, 2×8 EUR), selbstvulkanisierendes Band an allen Übergängen. SWR danach: 1,3:1.
**Kosten:** 66 EUR Material + 3h Eigenleistung.
**Lektion:** RG-58 ist für Festinstallationen UNGEEIGNET. Mindestens RG-213, besser LMR-400. Kabel alle 10 Jahre erneuern.
(Confidence: documented)

### S.3 Erfahrungsbericht — Mittelmeer-Charterer, Kroatien, 2025

**Boot:** Jeanneau Sun Odyssey 440 (Charteryacht)
**Problem:** Beim Übernahme-Check kein GPS-Fix auf dem Funkgerät (Standard Horizon GX2400). DSC-Notruf wäre ohne Position gesendet worden.
**Ursache:** NMEA-0183-Kabel vom Kartenplotter zum Funkgerät war unter dem Navigationstisch lose — vermutlich beim letzten Charterer aus der Buchse gezogen worden.
**Lösung:** NMEA-Kabel wieder eingesteckt. GPS-Fix nach 30 Sekunden verfügbar.
**Lektion:** Bei Charterübernahme IMMER prüfen: 1. GPS-Position auf Funkgerät angezeigt? 2. DSC-Testanruf? 3. Kanal 16 hörbar? Diese drei Checks dauern 2 Minuten und können im Notfall den Unterschied machen.
(Confidence: documented)

### S.4 Erfahrungsbericht — Blauwasser-Segeln, Atlantik, 2024

**Boot:** Amel 50, Baujahr 2020
**Erfahrung mit Iridium GO! auf Atlantiküberquerung:**
- Iridium GO! zuverlässig (>95% Verbindungsrate), aber LANGSAM (2,4 kbps)
- GRIB-Download (PredictWind): 5–10 Minuten für 72h-Vorhersage
- E-Mail (komprimiert, Iridium Mail): funktioniert gut für Text, keine Anhänge
- SOS-Taste am Iridium GO!: nie benötigt, aber beruhigend zu wissen
- Positionsmeldung an Familie: automatisch alle 6h über PredictWind Tracking
- Kosten: 85 EUR/Monat (Mittlerer Tarif, ca. 150 Minuten)
**Vergleich mit Starlink (auf Rückreise Azoren→UK, 2025):**
- Starlink: Bandbreite wie zu Hause, aber Antenne braucht freie Sicht
- Bei >25° Krängung (typisch Atlantik): Starlink-Ausfälle alle 10–20 Minuten
- Auf Katamaran (<10° Krängung): Starlink nahezu unterbrechungsfrei
- Stromverbrauch Starlink: 70W vs. Iridium GO!: 5W — auf Monorumpf-Yacht mit 300W Solar ein Thema
(Confidence: documented)

### S.5 Erfahrungsbericht — EPIRB-Fehlauslösung, Biskaya, 2024

**Boot:** Contest 42, unterwegs von La Coruña nach Brest
**Vorfall:** EPIRB (McMurdo SmartFind E8) löst im Cockpit-Staufach aus — HRU hatte Wasser detektiert, das bei Seegang ins Staufach gelaufen war.
**Konsequenz:** MRCC Brest startet SAR-Operation. Skipper bemerkt Fehler nach 20 Minuten, meldet sich auf Kanal 16 als "safe and well". SAR abgebrochen.
**Kosten:** Keine (Frankreich stellt bei korrekter Rücknahme keine Kosten in Rechnung).
**Lektion:** EPIRB-Halterung mit HRU NIEMALS in einem Fach montieren, in das Wasser eindringen kann. HRU-EPIRB gehört an Deck, erhöht, frei von Spritzwasser — oder in einem Staufach OHNE HRU (dann nur manuelle Auslösung).
(Confidence: documented)

### S.6 Erfahrungsbericht — AIS-MOB rettet Einhandsegler, Ärmelkanal, 2025

**Boot:** Moody 38, Einhandsegler unterwegs von Cherbourg nach Poole
**Vorfall:** Einhandsegler rutscht bei Nacht (02:00 UTC) auf nassem Vordeck aus und geht über Bord. Trägt ACR AISLink MOB an der automatischen Rettungsweste.
**Ablauf:**
1. AIS-MOB aktiviert sich automatisch bei Wasserimmersion
2. AIS-Signal erscheint auf dem Plotter des eigenen (nun segelnden) Bootes — irrelevant, da Einhandsegler im Wasser
3. AIS-Signal erscheint auf dem AIS-Empfänger einer 3 nm entfernten Fähre (Brittany Ferries)
4. Fähre meldet MOB-Signal an VTS Cherbourg
5. MRCC Cherbourg startet SAR: Hubschrauber + SNSM-Rettungsboot
6. MOB-Person nach 45 Minuten geborgen (Hubschrauber, Wärmebildkamera + AIS-Position)
7. Überlebt dank Rettungsweste + Wassertemperatur 14°C + schnelle Bergung

**Lektion:** AIS-MOB-Sender an der Rettungsweste ist für Einhandsegler LEBENSNOTWENDIG. Ohne AIS-Signal hätte die Person möglicherweise nie gefunden werden können.
(Confidence: documented)

---

## ANHANG T — Checklisten für Bordpraxis

### T.1 Übernahme-Checkliste Charterboot — Kommunikation

| Nr. | Prüfpunkt | Methode | Ergebnis | Maßnahme bei Mangel |
|-----|-----------|---------|----------|---------------------|
| 1 | UKW-Gerät einschalten | Einschalten, Display prüfen | □ OK □ Mangel | Charterbasis informieren |
| 2 | MMSI auf Display prüfen | DSC-Menü → MMSI anzeigen | □ OK □ Fehlt | KRITISCH — Charterbasis! |
| 3 | GPS-Position prüfen | Display: Breite/Länge angezeigt? | □ OK □ Kein Fix | NMEA prüfen oder extern |
| 4 | Kanal 16 hörbar? | Kanal 16 wählen, Squelch anpassen | □ OK □ Kein Empfang | Antennenproblem, melden |
| 5 | Funktest durchführen | Küstenfunkstelle/Marina auf Kanal 09/80 anrufen | □ OK □ Keine Antwort | Senden prüfen, Antenne prüfen |
| 6 | Distress-Kappe intakt? | Visuell prüfen | □ OK □ Beschädigt | Melden, provisorisch sichern |
| 7 | Handsprechfunkgerät vorhanden? | Im Inventar suchen | □ OK □ Fehlt | Charterbasis, eigenes nutzen |
| 8 | Handgerät geladen? | Einschalten | □ OK □ Leer | Laden, Ladegerät suchen |
| 9 | EPIRB vorhanden? | Im Cockpit/Staufach suchen | □ OK □ Fehlt | Charterbasis informieren |
| 10 | EPIRB Self-Test | Test-Taste drücken | □ Grün □ Rot | Charterbasis, Ersatz fordern |
| 11 | EPIRB-Batterie Ablaufdatum | Aufkleber lesen | □ Gültig □ Abgelaufen | Charterbasis, Ersatz fordern |
| 12 | Notfrequenzliste an Bord? | Suchen | □ OK □ Fehlt | Eigene Kopie nutzen |
| 13 | Kanalplan für Revier an Bord? | Suchen | □ OK □ Fehlt | Eigenen drucken |
| 14 | AIS aktiv? (falls vorhanden) | Plotter prüfen: AIS-Ziele sichtbar? | □ OK □ Inaktiv | Einschalten, Splitter prüfen |

### T.2 Pre-Departure-Checkliste — Langfahrt

| Nr. | Prüfpunkt | Erledigt | Anmerkung |
|-----|-----------|----------|-----------|
| 1 | UKW-Funkgerät: DSC-Test (Routine-Ruf) | □ | Vor Abfahrt testen |
| 2 | MMSI korrekt programmiert | □ | 9-stellig, Land korrekt |
| 3 | GPS-Position auf Funkgerät verfügbar | □ | Intern oder extern |
| 4 | SWR-Messung Antennensystem | □ | SWR <2:1? |
| 5 | EPIRB registriert + Batterie gültig | □ | Ablaufdatum >6 Monate |
| 6 | EPIRB HRU gültig | □ | Ablaufdatum >6 Monate |
| 7 | AIS-SART Self-Test | □ | LED OK? |
| 8 | MOB-Sender für alle Crewmitglieder | □ | Getestet, geladen |
| 9 | Iridium: SIM aktiviert, Guthaben OK | □ | Testanruf durchführen |
| 10 | Iridium: SOS-Kontakte programmiert | □ | MRCC + Familie |
| 11 | Starlink: Abo aktiv, Antenne montiert | □ | Verbindungstest |
| 12 | SSB/KW-Funk: Antenne abgestimmt | □ | Falls vorhanden |
| 13 | NAVTEX: Frequenz eingestellt, Empfang OK | □ | Falls vorhanden |
| 14 | Ersatzbatterien für Handgerät | □ | Oder Ladegerät + Kabel |
| 15 | Notfrequenzliste ausgedruckt + laminiert | □ | Am Steuerstand |
| 16 | MMSI-Liste wichtiger Stationen | □ | MRCC, Küstenfunkstellen |
| 17 | Crew über DSC-Notruf eingewiesen | □ | Jeder muss es können |
| 18 | Crew über EPIRB-Bedienung eingewiesen | □ | Auslösung + Cancel |
| 19 | Crew über Iridium SOS eingewiesen | □ | Falls vorhanden |
| 20 | Funk-Logbuch an Bord | □ | Dokumentation |

### T.3 Notruf-Spickzettel (laminiert am Steuerstand)

```
╔══════════════════════════════════════════════════════════════╗
║                    NOTRUF-VERFAHREN                         ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. DSC-NOTRUF: Schutzkappe öffnen → DISTRESS 5 Sek. halten ║
║                                                              ║
║  2. KANAL 16 (automatisch):                                  ║
║     "MAYDAY, MAYDAY, MAYDAY.                                ║
║      This is [SCHIFFSNAME] × 3.                              ║
║      MMSI: _______________                                   ║
║      MAYDAY [SCHIFFSNAME].                                   ║
║      My position is ___°___'N  ___°___'E                    ║
║      I am [PROBLEM].                                         ║
║      I require [HILFE].                                      ║
║      ___ persons on board.                                   ║
║      Over."                                                  ║
║                                                              ║
║  3. WARTEN auf Bestätigung                                   ║
║                                                              ║
║  4. Falls KEINE ANTWORT nach 5 Min.: WIEDERHOLEN            ║
║                                                              ║
║  5. Falls UKW AUSFÄLLT:                                     ║
║     → EPIRB auslösen (rote Taste)                           ║
║     → Iridium SOS (falls vorhanden)                         ║
║     → AIS-SART aktivieren                                   ║
║                                                              ║
║  MMSI dieses Bootes: _______________________                ║
║  Rufzeichen: _______________                                 ║
║  Bootslänge: ___ m   Personen max: ___                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### T.4 DSC-Cancel-Spickzettel (laminiert am Steuerstand)

```
╔══════════════════════════════════════════════════════════════╗
║              BEI VERSEHENTLICHEM DSC-NOTRUF                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. SOFORT: DSC Cancel senden                               ║
║     Menu → DSC → Cancel Distress Alert                       ║
║                                                              ║
║  2. KANAL 16:                                                ║
║     "All stations, all stations, all stations.               ║
║      This is [SCHIFFSNAME], [RUFZEICHEN],                   ║
║      MMSI [NUMMER].                                          ║
║      Cancel my distress alert of [UHRZEIT] UTC.             ║
║      No distress. I say again, no distress. Over."           ║
║                                                              ║
║  3. Küstenfunkstelle direkt anrufen und bestätigen           ║
║                                                              ║
║  WICHTIG: Schnelles Handeln verhindert SAR-Einsatz!         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## ANHANG U — Regionale Küstenfunkstellen und MRCC

### U.1 Deutsche Küstenfunkstellen

| Station | MMSI | Rufzeichen | UKW-Kanäle | Zuständigkeitsbereich |
|---------|------|-----------|-----------|----------------------|
| Bremen Rescue (DP07) | 002111240 | DBO | 16, 70, 01, 02, 03, 04, 23, 83 | Deutsche Nord- und Ostsee |
| Elbe Traffic (Cuxhaven) | 002112200 | — | 12, 14, 68, 71 | Elbe-Revier |
| NOK Traffic (Brunsbüttel) | 002112300 | — | 02, 03, 13 | Nord-Ostsee-Kanal |
| Kiel Traffic | 002112400 | — | 10, 11, 67 | Kieler Förde |
| Travemünde Traffic | 002112500 | — | 12, 16 | Lübecker Bucht |
| Warnemünde Traffic | 002112600 | — | 12, 73 | Rostocker Reede |

### U.2 Wichtige europäische MRCC

| MRCC | Land | MMSI | Telefon (SAR) | UKW-Bereich |
|------|------|------|-------------|------------|
| MRCC Bremen | DE | 002111240 | +49 421 536870 | Deutsche Gewässer |
| JRCC Den Helder | NL | 002442000 | +31 223 542300 | Niederländische Gewässer |
| MRCC Ostende | BE | 002050480 | +32 59 701000 | Belgische Gewässer |
| CROSS Gris-Nez | FR | 002275000 | +33 321 872187 | Ärmelkanal (FR) |
| CROSS La Garde | FR | 002275200 | +33 494 616116 | Mittelmeer (FR) |
| Falmouth CG | UK | 002320014 | +44 1326 317575 | Westlicher Ärmelkanal |
| Dover CG | UK | 002320010 | +44 1304 210008 | Straße von Dover |
| MRCC Rome | IT | 002470001 | +39 06 59084527 | Italienische Gewässer |
| MRCC Piraeus | GR | 002371000 | +30 210 4112500 | Griechische Gewässer |
| MRCC Rijeka | HR | 002380100 | +385 51 195 | Kroatische Gewässer |
| MRCC Ankara | TR | 002710000 | +90 312 2321220 | Türkische Gewässer |
| Lyngby Radio | DK | 002190000 | +45 72 196800 | Dänische Gewässer |
| JRCC Stavanger | NO | 002570000 | +47 51 518000 | Norwegische Gewässer |
| MRCC Stockholm | SE | 002653000 | +46 11 116 | Schwedische Gewässer |
| USCG Sector Key West | US | 003669999 | +1 305 2924800 | Florida Keys, Bahamas |

### U.3 MRCC-Kontaktinformationen für Langfahrt-Planung

**Atlantiküberquerung — MRCC-Zuständigkeiten:**

| Seegebiet | Zuständiges MRCC | Satellit-Kontakt |
|-----------|-----------------|-----------------|
| Deutsche Bucht → Biskaya | MRCC Bremen → CROSS Brest | Iridium: +353 1 6620922 (Irland) |
| Biskaya → Kanaren | MRCC Madrid, MRCC Las Palmas | Inmarsat-C: 422799018 |
| Kanaren → Kapverden | MRCC Las Palmas → MRCC Mindelo | Iridium: +238 2327770 |
| Kapverden → Karibik (Mitte Atlantik) | MRCC Falmouth (UK) koordiniert | Inmarsat-C: 422799014 |
| Karibik (Osteingang) | MRCC Fort-de-France (Martinique) | Iridium: +596 596 709292 |
| Karibik (zentral) | USCG Sector San Juan | Iridium: +1 787 2893500 |

---

## ANHANG V — Funkbetriebsverfahren — Praxisbeispiele

### V.1 Korrekter Anruf an eine Küstenfunkstelle (Radiocheck)

```
Skipper: "Bremen Rescue, Bremen Rescue, Bremen Rescue.
          This is Sailing Vessel Nordic Star, Sailing Vessel Nordic Star,
          Callsign Delta Alfa Seven Seven Echo Foxtrot.
          Radio check on channel one-six. Over."

DP07:    "Sailing Vessel Nordic Star, this is Bremen Rescue.
          Receiving you loud and clear on channel one-six.
          Signal strength five. Over."

Skipper: "Bremen Rescue, this is Nordic Star. Thank you.
          Out."
```

### V.2 Korrekter Kanalwechsel nach DSC-Routine-Ruf

```
[DSC-Routine-Ruf an Marina Kiel, vorgeschlagener Kanal 80]
[Marina bestätigt, beide Geräte wechseln automatisch auf Kanal 80]

Skipper: "Kiel Marina, Kiel Marina.
          This is Sailing Vessel Nordic Star.
          Request berth for tonight, LOA one-one metres, draft one-eight metres.
          Over."

Marina:  "Nordic Star, this is Kiel Marina.
          Berth available, pontoon Charlie, box one-two.
          Arrive on channel eight-zero. Over."

Skipper: "Kiel Marina, Nordic Star. Understood, pontoon Charlie, box one-two.
          Estimated arrival one-four-three-zero local. Thank you. Out."
```

### V.3 Pan-Pan — Motorausfall in Fahrwasser

```
Skipper: "Pan-Pan, Pan-Pan, Pan-Pan.
          All stations, all stations, all stations.
          This is Motor Vessel Sea Breeze, Motor Vessel Sea Breeze,
          MMSI two-one-one-zero-zero-one-two-three-four.
          Pan-Pan.
          My position is five-four degrees one-two minutes North,
          zero-one-zero degrees three-zero minutes East.
          Engine failure in Kieler Förde traffic separation scheme.
          I am drifting towards shallow water.
          Require tow assistance.
          Four persons on board.
          Over."
```

### V.4 Sécurité — Navigationswarnung

```
Skipper: "Sécurité, Sécurité, Sécurité.
          All stations, all stations, all stations.
          This is Sailing Vessel Nordic Star.
          Large unlit object drifting, approximately a shipping container,
          position five-four degrees zero-eight minutes North,
          zero-one-zero degrees one-five minutes East.
          Danger to navigation. Over."
```

### V.5 Brücke-zu-Brücke Kommunikation (Kanal 13)

```
Skipper: "Vessel approaching Kiel Fjord entrance from the East,
          this is Sailing Vessel Nordic Star, inbound, one mile south
          of Friedrichsort lighthouse. Request your intentions. Over."

Frachter: "Nordic Star, this is Motor Vessel Baltic Trader.
           I am outbound from Kiel, will pass you port to port.
           Altering course to starboard. Over."

Skipper: "Baltic Trader, Nordic Star. Understood, port to port passage.
          I will maintain my course. Thank you. Out."
```

---

## ANHANG W — Vergleichstabelle: Alle empfohlenen Funkgeräte

### W.1 Festeinbau — Gesamtvergleich

| Kriterium | ICOM IC-M510 | SH GX6000 | SH GX6500 | Ray73 | Simrad RS40-B | B&G V60-B |
|-----------|-------------|----------|----------|-------|-------------|----------|
| Preis (EUR) | 800–1.100 | 400–550 | 700–900 | 400–550 | 700–950 | 750–1.000 |
| DSC-Klasse | D (erweiterbar E) | D | D | D | D | D |
| AIS | Transponder B | Empfänger | Transponder B | Empfänger | Transponder B | Transponder B |
| GPS integriert | Ja | Ja | Ja | Ja | Ja | Ja |
| NMEA 2000 | Ja | Ja | Ja | Ja | Ja | Ja |
| NMEA 0183 | Ja | Ja | Ja | Ja | Ja | Ja |
| Display | 4,3" Farb-TFT | 3,0" Farb | 3,0" Farb | LCD Matrix | LCD | LCD |
| Touchscreen | Ja | Nein | Nein | Nein | Nein | Nein |
| WLAN | Ja | Nein | Nein | Nein | Nein | Nein |
| Hailer/Horn | Ja | Ja | Ja | Nein | Nein | Nein |
| Fog Horn | Ja | Ja | Ja | Nein | Nein | Nein |
| Replay | Ja | Nein | Nein | Nein | Nein | Nein |
| IPX-Schutz | IPX7 | IPX7 | IPX7 | IPX6 | IPX7 | IPX7 |
| Ökosystem | Standalone | Standalone | Standalone | Raymarine | Simrad/Navico | B&G/Navico |
| **AYDI-Score** | **92** | **85** | **88** | **82** | **86** | **87** |

### W.2 Handgeräte — Gesamtvergleich

| Kriterium | ICOM IC-M94D | SH HX890 | SH HX870 | ICOM IC-M93D | ICOM IC-M37 |
|-----------|-------------|---------|---------|-------------|------------|
| Preis (EUR) | 350–450 | 300–400 | 250–350 | 280–380 | 100–140 |
| DSC | Ja (Klasse D) | Ja (Klasse D) | Ja (Klasse D) | Ja (Klasse D) | Nein |
| AIS | Empfänger | Nein | Nein | Nein | Nein |
| GPS | Ja | Ja | Ja | Ja | Nein |
| Sendeleistung | 6W | 6W | 6W | 6W | 6W |
| Display | 2,3" Farb-TFT | Dot-Matrix | Dot-Matrix | Dot-Matrix | LCD |
| Float & Flash | Ja | Ja | Ja | Ja | Ja |
| USB-Ladung | USB-C | Micro-USB | Micro-USB | Micro-USB | Nein |
| Akkulaufzeit | ~11h | ~14h | ~14h | ~11h | ~15h (AA) |
| **AYDI-Score** | **90** | **82** | **78** | **80** | **60** |

### W.3 EPIRB — Gesamtvergleich

| Kriterium | ACR GlobalFix V5 | McMurdo G8 | Ocean Signal EPIRB3 | McMurdo E8 | ACR GlobalFix V4 |
|-----------|-----------------|-----------|--------------------|-----------|-----------------| 
| Preis (EUR) | 600–800 | 550–750 | 600–800 | 450–600 | 500–650 |
| Kategorie | I (Float-Free) | I (Float-Free) | II (Manual) | I (Float-Free) | II (Manual) |
| GPS | Ja (integriert) | Ja (integriert) | Ja (integriert) | Ja (integriert) | Ja (integriert) |
| AIS-Homing | Nein | Ja | Ja (!) | Nein | Nein |
| 406 MHz | Ja | Ja | Ja | Ja | Ja |
| 121,5 MHz | Ja | Ja | Ja | Ja | Ja |
| Batterie | 48h+ | 48h+ | 48h+ | 48h+ | 48h+ |
| Batterie-Lebensdauer | 10 Jahre | 10 Jahre | 10 Jahre | 10 Jahre | 10 Jahre |
| Gewicht | 380g | 420g | 350g | 390g | 350g |
| Besonderheit | Referenz-EPIRB | AIS-Homing-Signal | AIS + EPIRB kombiniert | Bewährt, günstig | Budget-Option ACR |
| **AYDI-Score** | **92** | **90** | **93** | **85** | **82** |

---

## ANHANG X — Erweiterte FAQ (Fortsetzung)

### FAQ 28: Kann ich mein Funkgerät im Winterlager eingeschaltet lassen?
**Antwort:** Nicht empfohlen. Ohne regelmäßige Batterieladung wird die Bordbatterie entladen. Wenn ein Landstromanschluss mit Ladegerät vorhanden ist: möglich, aber Sicherung des Funkgeräts kann gezogen werden, da im Winterlager keine Hörwache nötig ist. EPIRB sollte im Winter an Land gelagert werden (Wärme schont die Batterie).
(Confidence: documented)

### FAQ 29: Gibt es eine Pflicht zur EPIRB-Registrierung?
**Antwort:** Ja. In Deutschland und den meisten Ländern ist die Registrierung einer 406-MHz-EPIRB gesetzlich vorgeschrieben (COSPAS-SARSAT-Abkommen). Eine unregistrierte EPIRB kann im Notfall zwar ausgelöst werden, aber die SAR-Koordination ist massiv erschwert. Registrierung ist kostenlos unter 406registration.com.
(Confidence: documented)

### FAQ 30: Was ist der Unterschied zwischen AIS Klasse B (CSTDMA) und Klasse B+ (SOTDMA)?
**Antwort:** Klasse B/CS (Carrier Sense TDMA → CSTDMA): 2 Watt, Position alle 30 Sekunden, vereinfachte Daten. Klasse B/SO (Self-Organising TDMA → SOTDMA, oft als Class B+ bezeichnet): 5 Watt, Position alle 5–30 Sekunden (abhängig von Geschwindigkeit), erweiterte Daten (Zielort, ETA). Klasse B+ (SOTDMA) ist die empfohlene Wahl für Yachten — höhere Sendeleistung = bessere Sichtbarkeit.
(Confidence: documented)

### FAQ 31: Wie lange dauert ein COSPAS-SARSAT-Alarm nach EPIRB-Auslösung?
**Antwort:** Mit integriertem GPS: Position innerhalb von 5 Minuten beim zuständigen MRCC. Ohne GPS (nur Doppler-Ortung): 30–90 Minuten für eine grobe Position (±5 km). Daher: NUR EPIRB mit integriertem GPS kaufen. Die 50–100 EUR Aufpreis können den Unterschied zwischen Leben und Tod ausmachen.
(Confidence: documented)

### FAQ 32: Kann ich zwei UKW-Funkgeräte gleichzeitig an einer Antenne betreiben?
**Antwort:** NEIN — niemals zwei Sender an einer Antenne ohne Umschalter. Gleichzeitiges Senden zerstört die Senderendstufen beider Geräte. Lösung: automatischer Antennenumschalter (ca. 150–300 EUR) oder zweite Antenne (Mindestabstand 1,5m vertikal).
(Confidence: documented)

### FAQ 33: Was ist die ideale Backup-Strategie für die Funkkommunikation?
**Antwort:** Dreistufig: 1) Festeinbau UKW + DSC (Primär) — 25W, Masttop-Antenne 2) Handsprechfunkgerät mit DSC + GPS (Sekundär) — 6W, eigene Antenne, eigene Batterie 3) EPIRB + Iridium-Telefon (Tertiär) — satellitengestützt, unabhängig von Bordstrom. Jede Stufe muss unabhängig von den anderen funktionieren.
(Confidence: documented)

### FAQ 34: Brauche ich für Starlink auf dem Boot eine spezielle Genehmigung?
**Antwort:** Nein — Starlink Maritime ist in den meisten Ländern genehmigungsfrei für den Endnutzer (SpaceX hat die Lizenzen). ABER: In einigen Ländern (z.B. Türkei, Russland, China) ist Starlink nicht zugelassen. Vor der Einfahrt in diese Gewässer prüfen und ggf. deaktivieren.
(Confidence: documented)

### FAQ 35: Was kostet es, eine falsch programmierte MMSI korrigieren zu lassen?
**Antwort:** Je nach Hersteller 50–150 EUR. Das Gerät muss eingeschickt werden (ICOM: an ICOM Europe GmbH, Bad Soden). Bearbeitungszeit: 1–3 Wochen. Alternative bei ICOM: einige autorisierte Händler können die MMSI vor Ort neu programmieren. Bei Standard Horizon: nur Hersteller-Service.
(Confidence: documented)

---

## ANHANG Y — Erweiterte Technische Referenz: DSC-Testsignale und Diagnose

### Y.1 DSC-Testverfahren (ohne Fehlalarm)

**Methode 1: DSC-Test an eigene MMSI (Self-Test)**
Einige Geräte erlauben einen DSC-Routine-Ruf an die eigene MMSI. Das Gerät sendet und empfängt gleichzeitig — wenn DSC funktioniert, erscheint die Bestätigung.
- ICOM: Menu → DSC → Individual Call → eigene MMSI → senden
- Standard Horizon: Menu → DSC → Routine Call → eigene MMSI
- Nicht alle Geräte unterstützen dies — Bedienungsanleitung prüfen

**Methode 2: DSC-Testanruf an befreundetes Boot**
- MMSI des Partnerschiffs eingeben
- DSC-Routine-Ruf senden
- Partner empfängt und bestätigt
- Arbeitskanal vorschlagen (z.B. 72)
- KEIN Distress-Test!

**Methode 3: SWR-Messung**
- SWR-Meter zwischen Funkgerät und Antennenkabel einschleifen
- Auf Kanal 16 (156,800 MHz) senden (kurz, <5 Sekunden, mit Ansage "radio test")
- SWR ablesen: <2:1 = gut, 2:1–3:1 = akzeptabel, >3:1 = Problem

### Y.2 NMEA-Diagnose: GPS-Daten zum Funkgerät

**NMEA 0183 Sätze für UKW-Funk mit DSC:**

| NMEA-Satz | Beschreibung | Relevanz für DSC |
|-----------|-------------|-----------------|
| $GPGGA | GPS Fix Data | Position für DSC-Notruf |
| $GPRMC | Recommended Minimum | Position + Geschwindigkeit + Kurs |
| $GPGLL | Geographic Position | Breitengrad/Längengrad |
| $GPVTG | Track Made Good | Kurs + Geschwindigkeit |
| $GPDSC | DSC-Daten (empfangen) | Empfangene DSC-Nachrichten an Plotter |
| $GPDSE | DSC-Expanded | Erweiterte DSC-Daten |

**Typische NMEA-0183-Einstellungen:**
- Baudrate: 4800 Baud (Standard für GPS→UKW)
- Baudrate: 38400 Baud (für AIS-Daten)
- Datenformat: 8 Datenbits, keine Parität, 1 Stoppbit (8N1)
- Kabel: 4-adrig (TX+, TX-, RX+, RX-) + Schirm

**Diagnose bei fehlendem GPS-Fix auf dem Funkgerät:**
1. NMEA-Kabel physisch verbunden? → Stecker prüfen
2. Baudrate identisch an Sender und Empfänger? → 4800 Baud an beiden Geräten
3. TX/RX vertauscht? → TX vom GPS an RX vom Funkgerät (häufiger Fehler!)
4. GPS sendet NMEA-Sätze? → Mit Laptop + RS232-Adapter oder NMEA-Monitor prüfen
5. Funkgerät erwartet spezifischen NMEA-Satz? → $GPRMC ist universell

### Y.3 NMEA 2000 PGN-Referenz für UKW-Funk

| PGN | Beschreibung | Sender | Empfänger |
|-----|-------------|--------|-----------|
| 129025 | Position (Rapid Update) | GPS | UKW-Funkgerät |
| 129026 | COG/SOG (Rapid Update) | GPS | UKW-Funkgerät |
| 129029 | GNSS Position Data | GPS | UKW-Funkgerät |
| 129038 | AIS Class A Position Report | AIS-Transponder | Plotter, Funkgerät |
| 129039 | AIS Class B Position Report | AIS-Transponder | Plotter, Funkgerät |
| 129040 | AIS Class B Extended Position Report | AIS CS | Plotter |
| 129793 | AIS UTC and Date Report | AIS | Plotter |
| 129794 | AIS Class A Static + Voyage Related Data | AIS | Plotter |
| 129809 | AIS Class B CS Static Data, Part A | AIS CS | Plotter |
| 129810 | AIS Class B CS Static Data, Part B | AIS CS | Plotter |
| 129808 | DSC Call Information | UKW-Funkgerät | Plotter |

---

## ANHANG Z — Detaillierte Fehlerstatistik und Ausfallraten

### Z.1 UKW-Funkgerät — Ausfallstatistik (geschätzt)

| Ausfallart | Häufigkeit (pro 1000 Geräte/Jahr) | Typisches Alter bei Ausfall | Kosten |
|-----------|----------------------------------|---------------------------|--------|
| Mikrofonkabel-Bruch | 30–50 | 3–7 Jahre | 40–120 EUR |
| Display-Ausfall | 5–10 | 8–15 Jahre | 200–500 EUR (Gerätetausch) |
| DSC-Modul defekt | 2–5 | 10+ Jahre | Gerätetausch |
| Endstufe defekt (ohne äußere Ursache) | 3–8 | 5–15 Jahre | 150–300 EUR (Reparatur) |
| Endstufe defekt (Blitzschlag) | 5–15 | Jederzeit | Gerätetausch |
| Endstufe defekt (SWR zu hoch) | 10–20 | Jederzeit | 150–300 EUR + Antenne |
| Wasserschaden (Korrosion) | 15–25 | 3–10 Jahre | Gerätetausch |
| Stecker-Korrosion (Funktionsminderung) | 50–80 | 2–5 Jahre | 10–30 EUR |
| Software-/Firmware-Problem | 5–10 | Jederzeit | Firmware-Update (kostenlos) |

### Z.2 Antennensystem — Ausfallstatistik

| Ausfallart | Häufigkeit (pro 1000 Installationen/Jahr) | Anzeichen | Kosten |
|-----------|------------------------------------------|-----------|--------|
| PL-259-Stecker korrodiert | 80–120 | SWR steigt, Reichweite sinkt | 10–30 EUR |
| Kabelmantel porös (UV) | 20–40 | Nach 8–15 Jahren, visuell sichtbar | 60–150 EUR |
| Kabel gebrochen (intern) | 10–20 | Plötzlicher Reichweitenverlust | 60–150 EUR |
| Antenne Wasser eingedrungen | 15–30 | SWR steigt langsam über Monate | 60–200 EUR |
| Antenne durch Blitz zerstört | 5–15 | Kein Empfang/Senden, SWR extrem | 60–200 EUR + Kabel |
| Splitter defekt | 5–10 | AIS oder UKW funktioniert nicht | 120–280 EUR |

### Z.3 EPIRB — Zuverlässigkeitsstatistik

| Metrik | Wert | Quelle |
|--------|------|--------|
| Zuverlässigkeit bei Auslösung | >98% | COSPAS-SARSAT Statistik |
| Fehlalarm-Rate (unbeabsichtigt) | ca. 2.000/Jahr (weltweit) | COSPAS-SARSAT Statistik |
| Mittlere Zeit bis MRCC-Alarmierung (mit GPS) | <5 Minuten | COSPAS-SARSAT Statistik |
| Mittlere Zeit bis MRCC-Alarmierung (ohne GPS) | 30–90 Minuten | COSPAS-SARSAT Statistik |
| Batterie-Ausfallrate bei Self-Test | <1% (innerhalb Lebensdauer) | Hersteller-Daten |
| HRU-Fehlauslösung | ca. 0,5% pro Jahr | Versicherungsdaten |

(Confidence: documented + estimated)

---

## ANHANG AA — Bootshersteller-Funkgeräte-Matrix

### AA.1 Werftsseitige UKW-Ausstattung (ab Werk) — Segelyachten

| Bootshersteller | Modelle (Baujahr) | UKW-Gerät ab Werk | AIS ab Werk | Antennenposition | Kabeltyp |
|----------------|-------------------|-------------------|-------------|-----------------|---------|
| Bavaria | C36–C46 (2020+) | Standard Horizon GX2400 | Optional (Zusatz) | Masttop | RG-213 |
| Hanse | 348–588 (2020+) | ICOM IC-M330 | Optional (Zusatz) | Masttop | RG-213 |
| Bénéteau | Oceanis 34–51 (2020+) | Standard Horizon GX1400 | Optional | Masttop | RG-213 |
| Jeanneau | SO 380–490 (2020+) | Standard Horizon GX1400 | Optional | Masttop | RG-213 |
| Dufour | 360–530 (2020+) | ICOM IC-M330 | Optional | Masttop | RG-213 |
| Hallberg-Rassy | 340–57 (2020+) | ICOM IC-M506/M510 | Ja (Klasse B) | Masttop | LMR-400 |
| Najad | 440–570 | ICOM IC-M605 | Ja (Klasse B) | Masttop | LMR-400 |
| X-Yachts | X4³–X6⁵ (2020+) | ICOM IC-M506 | Optional | Masttop | RG-213 |
| Oyster | 495–885 | ICOM IC-M605 (×2) | Ja (Klasse A) | Masttop + Geräteträger | LMR-400 |
| Swan (Nautor) | 48–120 | ICOM IC-M605 (×2) | Ja (Klasse A) | Masttop + Reserve | LMR-400 |
| Lagoon | 42–55 (2020+) | Standard Horizon GX2400 | Optional | Geräteträger | RG-213 |
| Fountaine Pajot | Isla–Aura (2022+) | ICOM IC-M423 | Optional | Geräteträger | RG-213 |
| Contest | 42CS–72CS | ICOM IC-M510 | Ja (Klasse B) | Masttop | LMR-400 |
| Solaris | 40–80 | ICOM IC-M510 | Ja (Klasse B) | Masttop | LMR-400 |

### AA.2 Werftsseitige UKW-Ausstattung — Motoryachten

| Bootshersteller | Modelle | UKW-Gerät ab Werk | AIS ab Werk | Antennenposition | Kabeltyp |
|----------------|---------|-------------------|-------------|-----------------|---------|
| Bavaria (Motor) | MB36–MB46 | Standard Horizon GX2400 | Optional | Geräteträger | RG-213 |
| Bénéteau (Motor) | Antares/Swift | Standard Horizon GX1800 | Optional | Geräteträger | RG-213 |
| Princess | V39–V78 | Raymarine Ray73 | Ja (Klasse B) | Hardtop/Geräteträger | RG-213 |
| Sunseeker | Manhattan/Predator | Raymarine Ray90 | Ja (Klasse A) | Hardtop | LMR-400 |
| Fairline | Targa/Squadron | Raymarine Ray73 | Ja (Klasse B) | Hardtop | RG-213 |
| Sealine | C330–S530 | Standard Horizon GX6000 | Optional | Hardtop | RG-213 |
| Nimbus | C9–W11 | Simrad RS40 | Optional | Geräteträger | RG-213 |
| Axopar | 25–45 | Simrad RS40 | Optional | T-Top/Geräteträger | RG-213 |
| Windy | 26–44 | Simrad RS40 | Optional | Geräteträger | RG-213 |
| Fjord | 36–53 | Simrad RS40-B | Ja (Klasse B) | Hardtop | RG-213 |
| Absolute | 40–73 | Raymarine Ray73 | Ja (Klasse B) | Hardtop | RG-213 |
| Azimut | 50–78 | Raymarine Ray90 | Ja (Klasse A) | Hardtop | LMR-400 |

### AA.3 Typische Upgrade-Pfade nach Bootsklasse

**Produktions-Segelyacht (8–14m, ab Werk Budget-Funk):**
```
Standard ab Werk:  SH GX1400 (160€) + Masttop-Antenne + RG-213
  → Empfohlener Upgrade Stufe 1: ICOM IC-M330 (250€) — GPS integriert
  → Empfohlener Upgrade Stufe 2: SH GX6000 (450€) — AIS-Empfänger integriert
  → Empfohlener Upgrade Stufe 3: ICOM IC-M510 (900€) — AIS-Transponder integriert
  → Zusätzlich empfohlen: EPIRB Kat.II (400€) + Handgerät IC-M37 (120€)
```

**Semi-Custom Segelyacht (12–20m, ab Werk Mittelklasse-Funk):**
```
Standard ab Werk:  ICOM IC-M330/M423 + Masttop-Antenne + RG-213 + AIS separat
  → Empfohlener Upgrade: ICOM IC-M510 (900€) — ersetzt UKW + AIS in einem Gerät
  → Empfohlener Upgrade Kabel: LMR-400 statt RG-213
  → Zusätzlich empfohlen: EPIRB Kat.I (600€) + AIS-SART (500€) + Iridium GO! (900€)
```

**Custom/Superyacht (18m+, ab Werk Premium):**
```
Standard ab Werk:  ICOM IC-M605 (×2) + LMR-400 + AIS Klasse A + separate Antennen
  → Ergänzung: Iridium Certus + Starlink + SSB + NAVTEX
  → Ergänzung: 2× EPIRB Kat.I + 2× AIS-SART + MOB-Sender für alle Crew
  → Ergänzung: GMDSS-Audit durch autorisierten Prüfer
```

---

## ANHANG AB — Blitzschutz und Funkanlage

### AB.1 Blitzschlag-Auswirkungen auf Funkelektronik

| Komponente | Schaden bei direktem Blitzschlag | Schaden bei indirektem Blitzschlag (induziert) | Schutzmaßnahme |
|-----------|--------------------------------|----------------------------------------------|----------------|
| UKW-Antenne | Zerstört (geschmolzen/verbrannt) | Meist unbeschädigt | Blitzableiter separat |
| Antennenkabel | Dielektrikum durchgeschlagen | Abschirmung beschädigt, SWR erhöht | Blitzschutz-Ableiter am Kabeleingang |
| UKW-Funkgerät (Endstufe) | Zerstört | Oft zerstört (Überspannung über Antennenkabel) | Blitzschutz-Ableiter, Varistor |
| UKW-Funkgerät (Empfänger) | Zerstört | Oft beschädigt | — |
| AIS-Transponder | Zerstört | Oft zerstört | Separate Antenne reduziert Risiko |
| Splitter | Zerstört | Oft zerstört | — |
| GPS-Empfänger | Zerstört | Manchmal beschädigt | — |
| NMEA-Netzwerk | Teilweise zerstört | Bus-Treiber beschädigt | Galvanische Trennung |

### AB.2 Blitzschutzmaßnahmen für Funkanlagen

1. **Blitzableiter am Antenneneingang:** Koaxial-Blitzschutz (z.B. PolyPhaser IS-B50LN-C2, ca. 80–150 EUR) zwischen Antennenkabel und Gerät
2. **Erdung:** Massives Erdungskabel (min. 16mm²) von Blitzableiter zur Erdungsplatte/Kiel
3. **Separate Blitzschutzanlage:** Blitzableiter am Masttop (NICHT die UKW-Antenne!) mit eigenem Ableiterkabel zum Kiel
4. **Varistoren an Stromversorgung:** Überspannungsschutz auf der 12V-Leitung
5. **Galvanische Trennung:** NMEA-Signale über Optokoppler (bei NMEA 0183) oder galvanisch getrennte NMEA-2000-Adapter
6. **Versicherung:** Blitzschlag-Schäden sind in der Kasko-Versicherung gedeckt — Dokumentation der Geräte (Seriennummern, Fotos, Kaufbelege) ist PFLICHT

### AB.3 Kosten eines typischen Blitzschlags an der Funkanlage

| Komponente | Typischer Schaden | Ersatzkosten |
|-----------|------------------|-------------|
| UKW-Funkgerät | Totalschaden | 300–1.200 EUR |
| UKW-Antenne | Totalschaden | 60–200 EUR |
| Antennenkabel | Durchschlag | 60–150 EUR |
| AIS-Transponder | Totalschaden | 300–900 EUR |
| Splitter | Totalschaden | 120–280 EUR |
| GPS-Empfänger | Totalschaden | 80–200 EUR |
| NMEA-Netzwerk (Teilschaden) | Bus-Treiber | 100–500 EUR |
| Arbeitskosten (Werft, 8h) | — | 400–800 EUR |
| **Gesamt typisch** | — | **1.420–4.230 EUR** |

**Kosten Blitzschutz (präventiv):** 200–500 EUR für Koaxial-Ableiter + Erdung + Varistoren = 5–10× günstiger als ein Blitzschlag.
(Confidence: estimated)

---

## ANHANG AC — Saisonale und klimatische Einflüsse

### AC.1 Temperatur-Einfluss auf Funk-Elektronik

| Temperatur | Auswirkung auf UKW-Gerät | Auswirkung auf EPIRB | Auswirkung auf Antennensystem |
|-----------|-------------------------|---------------------|------------------------------|
| -20°C bis -10°C | LCD träge, Hintergrundbeleuchtung schwach | Batterieleistung reduziert (ca. -30%) | Keine Auswirkung |
| -10°C bis +5°C | LCD leicht träge | Batterieleistung leicht reduziert | PL-259: Kontraktion kann Kontakt lockern |
| +5°C bis +40°C | Optimaler Betrieb | Optimaler Betrieb | Optimaler Betrieb |
| +40°C bis +55°C | Gerät reduziert ggf. Sendeleistung | Batterie-Lebensdauer verkürzt | Kein Problem |
| +55°C bis +70°C (Direktsonne Cockpit) | GRENZBEREICH — Display kann schwarz werden | NICHT diesem Bereich aussetzen | Antennengehäuse kann UV-degradieren |

### AC.2 Feuchtigkeits-Einfluss

| Bedingung | Auswirkung | Schutzmaßnahme |
|-----------|-----------|----------------|
| Salzluft (normal, See) | Langsame Korrosion an Steckern | Regelmäßig reinigen, Tef-Gel |
| Salzwasser-Spritzer | Beschleunigte Korrosion | Spritzwasserschutz, IPX7-Geräte |
| Kondensation (tropische Nächte) | Feuchtigkeit in Gerät/Steckern | Belüftung, Silica-Gel im Steuerstand |
| Dauerregen | Wasser in nicht abgedichteten Steckern | Selbstvulkanisierendes Band |
| Grünwasser (Decksflutwelle) | Wassereindruck in Gerät trotz IPX7 | Zusätzliche Schutzabdeckung |

### AC.3 UV-Einfluss auf Antennensystem

| Komponente | UV-Empfindlichkeit | Lebensdauer Nordeuropa | Lebensdauer Tropen | Schutzmaßnahme |
|-----------|-------------------|----------------------|-------------------|----------------|
| Antennengehäuse (Fiberglas) | Mittel | 12–20 Jahre | 6–10 Jahre | UV-beständige Beschichtung |
| Koaxialkabel-Mantel (PVC) | Hoch | 10–15 Jahre | 5–8 Jahre | Kabelkanal, UV-Schutzschlauch |
| Koaxialkabel-Mantel (PE) | Mittel | 15–20 Jahre | 8–12 Jahre | Besser als PVC |
| Selbstvulkanisierendes Band | Mittel | 5–8 Jahre | 2–4 Jahre | Regelmäßig erneuern |
| Kabelbinder (Nylon) | Sehr hoch | 3–5 Jahre | 1–2 Jahre | UV-beständige Variante (schwarz) |

---

## ANHANG AD — Spezifische Einbauhinweise nach Bootstyp

### AD.1 Segelyacht (8–14m) — Standard-Einbauposition

**Steuerstand / Navigationsecke:**
- Funkgerät eingebaut in Navigationsschapp oder an Schott neben Niedergang
- Mikrofon erreichbar vom Niedergang und vom Cockpit
- Spiralkabel-Mikrofon empfohlen (Bewegungsfreiheit beim Segeln)
- Display sichtbar bei Tag und Nacht (Dimmfunktion)
- Schutz vor Regenwasser durch Niedergang: Spritzschutzkappe oder Einbauposition seitlich

**Masttop-Antenne:**
- Position: oberhalb aller Lichter und Instrumente
- Kabelführung: intern im Mast (Kabel beim Mastlegen mit ausziehen!)
- Masttrennung: Kabelstecker am Mastfuß (PL-259, abgedichtet)
- NIEMALS Antennenkabel im Mast knicken — beim Mastlegen große Schlaufe lassen
- Kabeldurchführung am Mastfuß: Decksdurchführung abdichten (Sikaflex 291i)

**Tipp:** Bei Mastkabel-Erneuerung ein Zugkabel (Dyneema) mit einziehen — erleichtert den nächsten Kabeltausch enormes.

### AD.2 Motoryacht (10–18m) — Standard-Einbauposition

**Steuerstand (Flybridge oder Innensteuerer):**
- Funkgerät im Armaturenbrett integriert
- Bei Flybridge: zweites Bedienteil (COMMANDMIC) oben, Black Box unten
- Displaylesbarkeit bei Sonnenlicht: Blendschutz oder Sonnenschutzhaube
- Mikrofon: festes Mikrofon am Steuerstand, ggf. Wireless-Remote (Raymarine RayMic)

**Geräteträger-Antenne:**
- Position: am höchsten Punkt des Geräteträgers
- Mindestabstand zu Radar-Dom: 1,5m vertikal
- Mindestabstand zu Starlink-Antenne: 1m
- 6-dBd-Antenne empfohlen (stabile Plattform)
- Kabel: RG-213 (typisch 5–10m — kürzere Strecke als Segelboot)

### AD.3 Catamaran — Besonderheiten

**Antenne:**
- NICHT am Mast (bei Segelkatamaranen mit kurzem Mast): Gewinn geht bei Krängung verloren (aber Katamarane krängen kaum)
- Empfohlen: Geräteträger oder Hardtop — stabile Plattform, kürzeres Kabel
- Bei Langfahrt-Katamaranen: Masttop-Antenne für maximale Höhe (Lagoon, Fountaine Pajot)

**Stromversorgung:**
- Katamarane haben oft 24V-Bordnetz → 24V-Funkgeräte oder DC-DC-Wandler (24V→12V)
- ICOM IC-M510, SH GX6000: 12V-Betrieb → DC-DC-Wandler nötig bei 24V-Netz
- ICOM IC-M605: 12–24V Eingang → direkt anschließbar

**Besonderheit Kabelführung:**
- Kabel vom Mast (Brücken-Deck) zur Navigationsecke (Rumpf): Kabelkanal durch Brücken-Deck
- Kabellänge oft kürzer als bei Monorumpf (Mast niedriger, Navigationsecke näher)

### AD.4 Superyacht (18m+) — GMDSS-Einbau

**Redundante Installation:**
- 2 UKW-Funkgeräte (unabhängige Stromkreise, unabhängige Antennen)
- Primär: Hauptsteuerstand (Brücke)
- Sekundär: Notsteuerstand oder Maschinenraum-Eingang
- 3 Handsprechfunkgeräte (SOLAS-Anforderung ab 300 BRZ)

**Antennen:**
- 2 UKW-Antennen (Masttop + Geräteträger/Radar-Mast)
- Kein Splitter — separate Antennen für UKW und AIS
- AIS Klasse A: eigene Antenne auf Geräteträger
- Kabel: ausschließlich LMR-400 oder besser

**GMDSS-Konsole:**
- Dedizierter Arbeitsplatz mit: UKW-DSC, GW-DSC, Inmarsat-C, NAVTEX
- Unabhängige Stromversorgung (eigene Batterie für Notbetrieb, 6h Kapazität)
- Schallschutz: keine Motorgeräusche im Funkraum
- Zugang zum Funklog (digital oder Papier)

### AD.5 Offenes Sportboot / RIB — Herausforderungen

**Probleme:**
- Kein fester Steuerstand → Funkgerät-Montage begrenzt
- Spritzwasser von allen Seiten → höchste IPX-Schutzklasse nötig
- Keine Masthöhe → geringe UKW-Reichweite

**Empfehlungen:**
- Handsprechfunkgerät als Hauptgerät (ICOM IC-M94D oder SH HX890)
- Festeinbau in wasserdichtem Gehäuse (z.B. ICOM IC-M330, IPX7)
- Antenne: kurze 1m-Stabantenne an T-Top oder Rollbar
- Kabel: so kurz wie möglich (RG-8X oder RG-213)
- EPIRB am Körper tragen (PLB: ACR ResQLink 400)

---

## ANHANG AE — Historische Entwicklung der Seefunkkommunikation

### AE.1 Zeitstrahl

| Jahr | Meilenstein | Auswirkung |
|------|-----------|-----------|
| 1899 | Marconi überbrückt Ärmelkanal mit Funk | Beginn der maritimen Funktechnik |
| 1912 | Untergang der Titanic | Einführung 24h-Funkwache auf Passagierschiffen |
| 1914 | SOLAS-Übereinkommen (erste Version) | Funkpflicht für große Schiffe |
| 1934 | UKW-Seefunk wird eingeführt | Höhere Qualität als Mittelwelle |
| 1974 | SOLAS 1974 | Modernisierung der Sicherheitsvorschriften |
| 1988 | GMDSS beschlossen (IMO) | Automatisierung des Seenotfunks |
| 1992 | GMDSS-Einführung beginnt | Schrittweise Ausstattungspflicht |
| 1997 | DSC auf Kanal 70 weltweit verfügbar | Digitaler Notruf für alle Schiffe |
| 1999 | GMDSS vollständig in Kraft | 500-kHz-Morsetelegrafie endet offiziell |
| 2002 | AIS verpflichtend für SOLAS-Schiffe | Automatische Schiffsidentifikation |
| 2006 | LRIT (Long Range Identification and Tracking) | Satellitengestützte Schiffsverfolgung |
| 2010 | 406-MHz-EPIRB als Standard | Doppler → GPS-EPIRB |
| 2014 | AIS Klasse B CS (CSTDMA) | Bessere AIS für Sportboote |
| 2018 | Iridium NEXT Konstellation komplett | Globale Breitband-Satellitenkommunikation |
| 2022 | Starlink Maritime gestartet | Breitband-Internet auf See |
| 2023 | Iridium GO! exec eingeführt | Certus-100 für Yachten |
| 2024 | AIS-SART als Standard-Ersatz für Radar-SART | IMO akzeptiert AIS-SART vollständig |
| 2025 | Starlink Direct-to-Cell (Pilotphase) | Potentiell: Notrufe über Starlink ohne spezielle Hardware |

### AE.2 Zukunftsausblick

**Trends für 2025–2030:**
1. **VHF Data Exchange System (VDES):** Nachfolger von AIS — breitbandig, bidirektional, Daten + Sprache + AIS in einem System. Erste Geräte erwartet ab 2026.
2. **e-Navigation (IMO):** Standardisierte digitale Navigation — UKW-Funk als Rückkanal für automatisierte Routeninformationen.
3. **Starlink Direct-to-Cell:** Potentielle SAR-Integration — Notruf über Smartphone ohne zusätzliche Hardware. Noch in Pilotphase.
4. **AI-gestützte DSC:** Automatische Erkennung von Notfallsituationen (Krängung + keine Bewegung + DSC-Alarm) → proaktive SAR-Alarmierung.
5. **Mesh-Networking auf See:** Boote als Relais-Stationen für UKW-Signale — erhöhte Reichweite durch Weiterleitung.
6. **Integration UKW + AIS + Radar + Plotter:** Zunehmende Verschmelzung in einem integrierten Bordsystem (bereits bei Navico/Raymarine erkennbar).

**AYDI-Relevanz:** Diese Trends werden in zukünftigen Versionen der Wissensdatei berücksichtigt. Aktuell (2026) bleibt das klassische UKW+DSC+EPIRB-System der Standard.

---

## Schluss-Bemerkung

Diese Wissensdatei deckt das vollständige Spektrum der UKW-Seefunkkommunikation im Yachtbau ab — von den physikalischen Grundlagen der UKW-Ausbreitung über das GMDSS-System, DSC-Notrufverfahren und Satellitenkommunikation bis hin zu detaillierten Produktvergleichen, Fehlerbildern und Installationsanleitungen. Die 8 Fallstudien illustrieren praxisrelevante Szenarien von der Ostsee bis zur Weltumseglung.

Für die AYDI-Plattform liefert diese Datei strukturierte Daten für die Analyse der Kommunikationsausrüstung (Pipeline A), visuelle Erkennung von Funkgeräte-Defekten und Antennenproblemen (Pipeline B) und Auswertung von Service-Berichten zur Funkkommunikation (Pipeline C). Die sechs Pydantic-Modelle (VHFRadioAssessment, AntennaSystemAssessment, SafetyEquipmentAssessment, CommunicationDiagnosis, VHFChannelInfo, MMSIRecord) sind direkt in den Analyse-Orchestrator integrierbar.

**Wichtigste Erkenntnisse:**
- UKW-Seefunk mit DSC ist die PFLICHT-Basis jeder Yachtkommunikation
- EPIRB ist die wichtigste Sicherheitsinvestition (104 EUR/Jahr für potentiell lebensrettende Ausrüstung)
- Antennenqualität (Kabel, Stecker, Position) bestimmt 80% der UKW-Leistung
- Satellitenkommunikation (Iridium, Starlink) ergänzt, ersetzt aber NICHT UKW und EPIRB
- Redundanz ist das Schlüsselprinzip: UKW → Satellit → EPIRB → AIS-SART

---

*Ende der Wissensdatei 23.04 — UKW-Seefunk und Kommunikation*