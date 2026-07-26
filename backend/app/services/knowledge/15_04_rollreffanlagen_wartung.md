---
titel: "Rollreffanlagen – Wartung, Service und Troubleshooting"
kategorie: "Rollreffanlagen und Furler"
unterkategorie: "Wartung und Troubleshooting"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 15_04 — Rollreffanlagen – Wartung, Service und Troubleshooting

> **AYDI Wissensdatei 15.04** — Kategorie 15: Rollreffanlagen und Furler
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Einführung und Überblick](#1-einführung-und-überblick)
2. [Grundlagen der Rollreffanlagen-Wartung](#2-grundlagen-der-rollreffanlagen-wartung)
3. [Wartungsplan und Intervalle](#3-wartungsplan-und-intervalle)
4. [Lager-Wartung und -Austausch](#4-lager-wartung-und--austausch)
5. [Drum- und Trommel-Wartung](#5-drum--und-trommel-wartung)
6. [Profilstagsysteme — Wartung und Reparatur](#6-profilstagsysteme--wartung-und-reparatur)
7. [Schmierstoffe und Korrosionsschutz](#7-schmierstoffe-und-korrosionsschutz)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting-Entscheidungsbäume](#9-troubleshooting-entscheidungsbäume)
10. [Saisonale Wartungsprotokolle](#10-saisonale-wartungsprotokolle)
11. [Werkzeuge und Spezialwerkzeug](#11-werkzeuge-und-spezialwerkzeug)
12. [Ersatzteil-Management](#12-ersatzteil-management)
13. [FAQ — Häufig gestellte Fragen](#13-faq--häufig-gestellte-fragen)
14. [Glossar](#14-glossar)
15. [Schnell-Referenz](#15-schnell-referenz)
16. [ANHANG A–H: Fallstudien](#anhang-ah-fallstudien)
17. [ANHANG I–R: Pydantic v2 Modelle](#anhang-ir-pydantic-v2-modelle)

---

## 1. Einführung und Überblick

### 1.1 Bedeutung der Rollreffanlagen-Wartung

Rollreffanlagen (Roller Furling Systems) gehören zu den am stärksten beanspruchten mechanischen Systemen an Bord einer Segelyacht. Sie sind permanenten Belastungen durch Wind, Salzwasser, UV-Strahlung und mechanische Kräfte ausgesetzt. Eine vernachlässigte Wartung führt nicht nur zu Komforteinbußen beim Segeln, sondern kann schwerwiegende Sicherheitsrisiken verursachen.

Die Rollreffanlage ist das einzige System an Bord, dessen Versagen gleichzeitig die Segelführung UND die Rigg-Integrität gefährdet. Ein blockierter Furler bei 30 Knoten Wind kann innerhalb von Minuten zu einer unkontrollierbaren Situation führen — ein Szenario, das durch regelmäßige Wartung nahezu vollständig vermeidbar ist.

### 1.2 Konsequenzen vernachlässigter Wartung

**Unmittelbare Risiken:**
- Blockierter Furler bei Starkwind → Segel kann nicht geborgen werden
- Vorstag-Versagen durch korrodierte Lager → Mastfall
- Segelbeschädigung durch klemmende Profile → Luff-Tape-Riss
- Leinenbruch an der Trommel → Kontrollverlust über Segelgröße

**Mittelfristige Schäden (1–3 Saisons ohne Wartung):**
- Korrosion an Lagern und Drehwirbeln → erhöhter Reibungswiderstand (+30–80 %)
- Profilverbindungen lockern sich → Segel klemmt intermittierend
- UV-Degradation von Kunststoffteilen → Drum-Risse, Halyard-Swivel-Bruch
- Festsitzen von Edelstahl-Verbindungen → Demontage nur noch mit Gewalt möglich

**Langfristige Folgen (3+ Saisons ohne Wartung):**
- Kompletter Lagerausfall → Furler-Totalaustausch erforderlich (3.000–15.000 EUR)
- Vorstag-Korrosion unter dem Profil → nicht sichtbar, plötzliches Versagen
- Profilverformung → neues Profilsystem erforderlich
- Sicherheitsrelevante Klassifikation: KRITISCH nach AYDI-Bewertungsstandard

### 1.3 Wartungsphilosophie: Präventiv vs. Reaktiv

**Präventive Wartung (empfohlen):**
- Systematische Inspektionen nach festgelegten Intervallen
- Schmierung und Reinigung als Routinemaßnahmen
- Austausch von Verschleißteilen vor dem Versagen
- Dokumentation aller Maßnahmen für Wertverfolgung
- Kostenrahmen: 150–400 EUR/Saison (abhängig von Systemgröße)

**Reaktive Wartung (Notfallbasis):**
- Eingriff erst bei Funktionseinschränkung oder Ausfall
- Häufig höhere Kosten durch Folgeschäden
- Reparatur unter Zeitdruck → fehleranfällig
- Kostenrahmen: 800–5.000 EUR pro Ereignis (Lager, Profile, Segel)

**AYDI-Empfehlung:** Strikt präventive Wartung mit saisonalen Intervallen. Die Investition von 200–400 EUR pro Saison in Wartung spart langfristig das 5- bis 20-Fache an Reparaturkosten.

### 1.4 Geltungsbereich dieses Dokuments

Dieses Dokument deckt folgende Rollreffanlagen-Typen ab:
- **Vorstag-Rollreffanlagen** (Headsail Furlers): Furlex, Profurl, Harken, Facnor, Karver, Selden
- **Großsegel-Rollreffsysteme** (In-Mast / In-Boom Furling): Selden, Facnor, Leisure Furl, Bamar, Reckmann
- **Code 0 / Gennaker Furler**: Karver, Facnor, Ronstan, Harken
- **Elektrische Furler-Antriebe**: Facnor FX+e, Selden GXe, Reckmann, Bamar V-Serie
- **Hydraulische Furler-Antriebe**: Reckmann, Bamar, Profurl Hydraulic

**Nicht abgedeckt:**
- Reine Renn-Furler ohne Reff-Funktion (werden in 15_05 behandelt)
- Rollreff-Großbäume (werden in 15_06 behandelt)

### 1.5 Zielgruppe

- Eigner mit technischem Grundverständnis (DIY-Wartung Level 1–2)
- Professionelle Rigger und Servicetechniker (Level 3–4)
- Werften und Refit-Betriebe
- AYDI-Analyse-Engine für automatisierte Zustandsbewertung

---

## 2. Grundlagen der Rollreffanlagen-Wartung

### 2.1 Wartungskategorien nach Systemtyp

#### 2.1.1 Vorstag-Furler (Headsail Furlers)

Die häufigste Furler-Bauart. Das Vorstag wird von einem Aluminium-Profil umschlossen, in dem das Segel mit dem Luff-Tape läuft. Unten sitzt die Trommel (Drum) mit der Reffleine, oben der Halyard-Swivel (Drehwirbel).

**Kritische Wartungspunkte:**

| Komponente | Wartungsintervall | Typische Lebensdauer | Ausfallrisiko |
|---|---|---|---|
| Unteres Lager (Drum) | Jährlich schmieren, alle 5 Jahre prüfen | 8–15 Jahre | HOCH |
| Oberes Lager (Swivel) | Jährlich schmieren, alle 5 Jahre prüfen | 8–15 Jahre | HOCH |
| Profilverbindungen | Jährlich prüfen | 15–20+ Jahre | MITTEL |
| Drum-Dichtungen | Alle 3–5 Jahre tauschen | 5–8 Jahre | NIEDRIG |
| Furling-Leine | Alle 3–5 Jahre tauschen | 3–7 Jahre | MITTEL |
| Vorstag unter Profil | Alle 10 Jahre prüfen | 15–25 Jahre | KRITISCH |

**Marktübliche Systeme und Größenklassen:**

| Hersteller | Modell | Bootsgröße | Vorstag-Durchmesser | Gewicht |
|---|---|---|---|---|
| Selden/Furlex | 200S | 7–10 m | 5–7 mm | 3,2 kg |
| Selden/Furlex | 300S | 10–14 m | 6–10 mm | 5,8 kg |
| Selden/Furlex | 400S | 14–18 m | 8–12 mm | 9,1 kg |
| Profurl | C290 | 7–10 m | 5–7 mm | 2,9 kg |
| Profurl | C350 | 9–13 m | 6–8 mm | 4,2 kg |
| Profurl | C430 | 12–16 m | 7–10 mm | 7,1 kg |
| Profurl | NEX 1.0 | 7–10 m | 5–7 mm | 3,0 kg |
| Profurl | NEX 2.0 | 10–14 m | 6–9 mm | 5,5 kg |
| Harken | MKIV Unit 0 | 6–9 m | 4–6 mm | 2,4 kg |
| Harken | MKIV Unit 1 | 8–11 m | 5–8 mm | 3,9 kg |
| Harken | MKIV Unit 2 | 10–14 m | 6–10 mm | 6,2 kg |
| Harken | MKIV Unit 3 | 13–17 m | 8–12 mm | 9,8 kg |
| Harken | MKIV Unit 4 | 16–22 m | 10–14 mm | 14,5 kg |
| Facnor | FX+ 1500 | 8–12 m | 5–8 mm | 3,8 kg |
| Facnor | FX+ 2500 | 12–16 m | 7–10 mm | 6,5 kg |
| Facnor | FX+ 3500 | 15–20 m | 8–12 mm | 10,2 kg |
| Facnor | LS 170 | 10–14 m | 6–9 mm | 4,9 kg |
| Facnor | LS 200 | 13–17 m | 7–11 mm | 7,8 kg |

#### 2.1.2 Großsegel-Rollreff (In-Mast / In-Boom)

Komplexere Systeme mit höheren Wartungsanforderungen, da das Profil im Mast integriert ist und der Zugang eingeschränkt ist.

**Kritische Wartungspunkte:**

| Komponente | Wartungsintervall | Typische Lebensdauer | Ausfallrisiko |
|---|---|---|---|
| Mandrel-Lager | Jährlich schmieren | 10–15 Jahre | HOCH |
| Mast-Schlitz/Track | Jährlich reinigen | Mastlebensdauer | MITTEL |
| Outhaul-System | Jährlich prüfen und schmieren | 10–20 Jahre | MITTEL |
| Segel-Führungsschienen | Alle 2 Jahre prüfen | 15–20 Jahre | NIEDRIG |
| Furling-Motor (elektr.) | Alle 2 Jahre Service | 8–12 Jahre | HOCH |

**Marktübliche Systeme:**
- Selden Furling Mast System (Rodkick, C-Mast)
- Facnor In-Mast Furling
- Leisure Furl In-Boom System
- Bamar In-Mast / In-Boom

#### 2.1.3 Code 0 / Gennaker Furler

Leichtbau-Furler für Leichtwind-Vorsegel. Geringere strukturelle Belastung, aber höhere Anforderungen an Leichtgängigkeit.

**Kritische Wartungspunkte:**

| Komponente | Wartungsintervall | Typische Lebensdauer | Ausfallrisiko |
|---|---|---|---|
| Torsionsseil | Jährlich prüfen | 5–10 Jahre | HOCH |
| Top-Swivel | Jährlich schmieren | 8–12 Jahre | MITTEL |
| Bottom-Tacker | Jährlich prüfen | 10–15 Jahre | NIEDRIG |
| Anti-Wrap-Netz | Jährlich prüfen | 3–5 Jahre | NIEDRIG |

**Marktübliche Systeme:**
- Karver KF3, KF4, KF5, KF7, KF8
- Facnor FX+ Code 0
- Ronstan Series 80, 120, 160
- Harken Code 0 Furler

### 2.2 Umgebungsfaktoren und deren Einfluss

#### 2.2.1 Salzwasser-Exposition

Salzwasser ist der Hauptfeind aller Furler-Komponenten. Salzablagerungen in Lagern erhöhen die Reibung exponentiell und fördern galvanische Korrosion zwischen unterschiedlichen Metallen.

**Einflussfaktoren:**
- Spray-Zone: Bug-Furler deutlich stärker belastet als Großsegel-Furler
- Regatta-Einsatz: häufigeres Furling/Unfurling → mehr Salzeintrag in Lager
- Tidenhub-Reviere: regelmäßiges Trockenfallen → Salzkrusten-Bildung
- Tropen-Einsatz: höhere Salzkonzentration + UV-Belastung

**Wartungskonsequenz:** In Salzwasser-Revieren mindestens 2x pro Saison Süßwasser-Spülung der Trommel und Lager. Nach jedem Starkwind-Einsatz (>20 kn) Süßwasser-Abspülung des gesamten Furlers.

#### 2.2.2 UV-Strahlung

UV-Strahlung zerstört Kunststoffkomponenten (Drum-Gehäuse, Profilverbindungen, Halyard-Swivel-Gehäuse) und den UV-Schutzstreifen am Segel.

**Degradationsraten:**
- Drum-Kunststoff (POM/Delrin): sichtbare Versprödung nach 5–8 Jahren (Mittelmeer), 8–12 Jahren (Nordeuropa)
- Profilverbindungen (Kunststoff): Versprödung nach 8–12 Jahren
- UV-Schutzstreifen (Sunbrella): Austausch alle 5–8 Jahre (Mittelmeer), 8–12 Jahre (Nordeuropa)
- Furling-Leinen (Polyester): UV-Degradation nach 3–5 Jahren

**Wartungskonsequenz:** UV-exponierte Kunststoffteile bei jeder Jahresinspektion auf Risse, Versprödung und Verfärbung prüfen. Schutzabdeckung für Trommel empfohlen.

#### 2.2.3 Klimazonen und Wartungsanpassung

| Klimazone | Salzbelastung | UV-Belastung | Feuchtigkeit | Wartungsintervall-Faktor |
|---|---|---|---|---|
| Nordsee/Ostsee | Mittel | Niedrig | Hoch | 1,0x (Basis) |
| Mittelmeer | Hoch | Sehr hoch | Niedrig-Mittel | 1,3x |
| Karibik/Tropen | Sehr hoch | Extrem | Hoch | 1,5x |
| Süßwasser (Seen) | Sehr niedrig | Mittel | Mittel | 0,7x |
| Hochsee/Blauwasser | Extrem | Hoch | Hoch | 1,5x |

**Praxisbeispiel:** Eine Furlex 300S in der Ostsee benötigt eine jährliche Schmierung. Dasselbe System in der Karibik sollte alle 8 Monate geschmiert werden, und die 5-Jahres-Überholung wird zur 3-Jahres-Überholung.

### 2.3 Werkstoffkunde für die Furler-Wartung

#### 2.3.1 Aluminium (Profile und Drum-Gehäuse)

- Legierung: überwiegend 6061-T6 oder 6082-T6 (eloxiert)
- Eloxalschicht: 15–25 µm (hart-eloxiert bis 50 µm bei Premium-Systemen)
- Korrosionsverhalten: Lochfraß bei beschädigter Eloxalschicht, insbesondere in Kontakt mit Edelstahl
- Wartung: Eloxalschicht niemals mit Schleifmitteln behandeln, nur milde alkalische Reiniger verwenden
- Galvanische Korrosion: Aluminium/Edelstahl-Kontakt nur mit Isolierung (Tef-Gel, Duralac)

#### 2.3.2 Edelstahl (Lager, Achsen, Befestiger)

- Standard: AISI 316L (1.4404) — einzig akzeptabel für Salzwasser
- AISI 304 (1.4301): NICHT für Furler-Komponenten in Salzwasser geeignet
- Crevice Corrosion: Hauptproblem bei Edelstahl in sauerstoffarmen Spalten
- Passivierung: Edelstahl-Oberflächen müssen passiviert bleiben (Citrussäure, Oxalsäure)
- Tea-Staining: kosmetisch, aber Indikator für unzureichende Legierungsqualität

#### 2.3.3 Kunststoffe und Verbundwerkstoffe

| Material | Einsatz | Lebensdauer | Schwachstelle |
|---|---|---|---|
| POM (Delrin) | Drum-Gehäuse, Profilverbindungen | 8–15 Jahre | UV-Versprödung |
| PTFE (Teflon) | Gleitlager, Dichtungen | 10–20 Jahre | Kriechneigung unter Last |
| Torlon (PAI) | Hochlast-Gleitlager | 15–25 Jahre | Wasseraufnahme (+0,3 %) |
| PA6.6 (Nylon) | Drum-Deckel, Kleinteile | 5–10 Jahre | UV + Wasseraufnahme |
| GFK/CFK | Profil-Hüllen (Premium) | 20+ Jahre | Impact-Schäden |

---

## 3. Wartungsplan und Intervalle

### 3.1 Vor jeder Ausfahrt — Pre-Sail Check (5 Minuten)

Diese Kurzinspektion sollte vor jeder Ausfahrt zur Routine gehören:

**Checkliste Pre-Sail:**

| Nr. | Prüfpunkt | Methode | OK-Kriterium |
|---|---|---|---|
| 3.1.1 | Furling-Leine: Zustand | Sichtprüfung | Keine Ausfransungen, Knicke oder Quetschungen |
| 3.1.2 | Furling-Leine: Wicklung auf Trommel | Sichtprüfung | Saubere, gleichmäßige Wicklungen ohne Überwerfer |
| 3.1.3 | Segel: Aufrollzustand | Sichtprüfung | Sauber aufgerollt, kein Lose-Flattern |
| 3.1.4 | UV-Schutzstreifen | Sichtprüfung | Vollständig sichtbar, keine offenen Stellen |
| 3.1.5 | Profilstag: Geradheit | Sichtprüfung von achtern | Keine sichtbare S-Kurve oder Knicke |
| 3.1.6 | Vorstag-Spannung | Hand-Test | Kein übermäßiges Durchhängen |
| 3.1.7 | Funktionstest: Ein-/Ausrollen | 1x komplett furlen/unfurlen | Leichtgängig, keine Geräusche |
| 3.1.8 | Halyard-Spannung | Klemme prüfen | Fest, kein Rutschen |

**Zeitaufwand:** 3–5 Minuten
**Werkzeug:** Keines erforderlich
**Durchführung:** Skipper oder erfahrenes Crew-Mitglied

### 3.2 Monatliche Kontrollen (während der Saison)

Erweiterte Inspektion bei aktiver Nutzung des Bootes:

**Checkliste Monatlich:**

| Nr. | Prüfpunkt | Methode | OK-Kriterium | Aktion bei Mangel |
|---|---|---|---|---|
| 3.2.1 | Drum-Bereich: Salzablagerungen | Sichtprüfung | Keine weißen Krusten | Süßwasser-Spülung |
| 3.2.2 | Drum-Drehung von Hand | Manuell drehen | Leichtgängig, kein Kratzen | Schmierung erforderlich |
| 3.2.3 | Profilverbindungen | Sichtprüfung auf Spalt | Kein sichtbarer Spalt >0,5 mm | Nachziehen oder tauschen |
| 3.2.4 | Segel-Eintritt am Profil | Sichtprüfung | Luff-Tape vollständig im Kanal | Kanal reinigen |
| 3.2.5 | Furling-Leine: Verschleiß | Befühlen über gesamte Länge | Kein Pilling, keine harten Stellen | Leine ersetzen |
| 3.2.6 | Halyard-Swivel oben | Fernglas | Kein sichtbarer Verschleiß, gerade | Bei Verdacht: Mast besteigen |
| 3.2.7 | Steckbolzen und Splinte | Sichtprüfung | Alle Splinte vorhanden, Bolzen fest | Sofort ersetzen |
| 3.2.8 | Drum-Abdeckung (falls vorhanden) | Sichtprüfung | Intakt, UV-beständig | Ersetzen |

**Zeitaufwand:** 15–20 Minuten
**Werkzeug:** Fernglas, Taschenlampe, Lappen
**Durchführung:** Eigner oder Crew

### 3.3 Saisonale Wartung — Einwassern / Saisonstart

Umfassende Inspektion und Wartung vor der ersten Ausfahrt der Saison:

**Protokoll Saisonstart:**

| Schritt | Maßnahme | Details | Zeitaufwand |
|---|---|---|---|
| 1 | Segel anschlagen | Luff-Tape in Profil-Kanal einführen, auf Leichtgängigkeit achten | 30–60 min |
| 2 | Furling-Leine einscheren | Neue oder geprüfte Leine, korrekte Wickelrichtung auf Trommel | 15–30 min |
| 3 | Drum-Schmierung | 2–3 Tropfen McLube OneDrop Ball Bearing Conditioner auf Drum-Achse | 5 min |
| 4 | Halyard-Swivel-Schmierung | McLube OneDrop oder Harken Pawl Oil am Swivel-Lager | 5 min |
| 5 | Profilverbindungen kontrollieren | Alle Verbindungsstücke auf festen Sitz prüfen, ggf. nachsetzen | 15–30 min |
| 6 | Vorstag-Spannung einstellen | Über Wantenspanner auf korrekte Spannung bringen (Hersteller-Vorgabe) | 15 min |
| 7 | Funktionstest komplett | 3x vollständig furlen/unfurlen bei Windstille | 10 min |
| 8 | UV-Schutzstreifen prüfen | Gesamte Länge auf Risse, Ausbleichung, Nähte | 10 min |

**Gesamtzeitaufwand:** 2–3 Stunden
**Werkzeug:** Standard-Bordwerkzeug, Schmiermittel, ggf. Ersatz-Leine
**Empfohlene Schmiermittel:**
- McLube OneDrop Ball Bearing Conditioner (Art.-Nr. 0860)
- Alternativ: Harken Pawl Oil (Art.-Nr. BK4521)
- NICHT verwenden: WD-40, Silikonspray, Vaseline

### 3.4 Saisonale Wartung — Auswassern / Saisonende

**Protokoll Saisonende:**

| Schritt | Maßnahme | Details | Zeitaufwand |
|---|---|---|---|
| 1 | Segel abschlagen | Luff-Tape vorsichtig aus Profil ziehen, Profil-Kanal reinigen | 30–60 min |
| 2 | Süßwasser-Spülung | Gesamtes Furler-System gründlich mit Süßwasser abspülen | 15 min |
| 3 | Drum-Inspektion | Drum-Abdeckung entfernen, Innenleben prüfen, Dichtungen kontrollieren | 20 min |
| 4 | Lager-Leichtgängigkeit | Drum und Swivel von Hand drehen, auf Rauheit achten | 5 min |
| 5 | Profil-Inspektion | Gesamtes Profil auf Verformungen, Risse, Korrosion kontrollieren | 30 min |
| 6 | Konservierung | Lager nachschmieren, Aluminium-Profile mit Schutzwachs behandeln | 20 min |
| 7 | Furling-Leine entfernen | Leine abziehen, waschen, trocknen, lagern oder entsorgen | 10 min |
| 8 | Abdeckung | Drum und Profilstag mit atmungsaktiver Plane abdecken | 10 min |
| 9 | Dokumentation | Zustand dokumentieren, nötige Winterarbeiten notieren | 10 min |

**Gesamtzeitaufwand:** 2,5–3,5 Stunden

### 3.5 Jährliche Inspektion (Detailliert)

Die jährliche Inspektion geht über die saisonale Wartung hinaus und beinhaltet eine systematische Zustandserfassung:

**Inspektionsprotokoll Jährlich:**

| Bereich | Prüfpunkt | Methode | Bewertung (1-5) | Toleranz |
|---|---|---|---|---|
| **Unteres Lager** | Axialspiel | Lager anheben/senken | 1–2 = OK | <0,5 mm |
| | Radialspiel | Seitliches Wackeln | 1–2 = OK | <0,3 mm |
| | Drehwiderstand | Handgefühl | 1–2 = OK | Leichtgängig, gleichmäßig |
| | Geräusch | Akustisch | 1 = OK | Kein Kratzen/Knirschen |
| | Korrosion | Sichtprüfung | 1–2 = OK | Keine Rostspuren |
| **Oberes Lager** | Axialspiel | Mast besteigen, prüfen | 1–2 = OK | <0,5 mm |
| | Radialspiel | Seitliches Wackeln | 1–2 = OK | <0,3 mm |
| | Drehwiderstand | Handgefühl | 1–2 = OK | Leichtgängig |
| | Halyard-Anschluss | Sichtprüfung Schäkel | 1–2 = OK | Kein Verschleiß >10 % |
| **Profilsystem** | Profilverbindungen (alle) | Sicht + Handprüfung | 1–2 = OK | Kein Spalt, kein Spiel |
| | Profilgeradheit | Visieren von unten | 1–2 = OK | <5 mm Abweichung/m |
| | Kanal-Zustand | Draht durchschieben | 1 = OK | Widerstandsfrei |
| | Korrosion/Eloxal | Sichtprüfung | 1–2 = OK | Keine Lochfraß-Stellen |
| **Trommel** | Leinen-Einlauf | Sichtprüfung | 1–2 = OK | Kein Verschleiß |
| | Dichtungen/O-Ringe | Sichtprüfung | 1–2 = OK | Elastisch, keine Risse |
| | Gehäuse | Sichtprüfung | 1–2 = OK | Keine Risse, UV-Schäden |
| | Schraubverbindungen | Drehmoment prüfen | 1 = OK | Herstellervorgabe ±10 % |
| **Vorstag** | Sichtbarer Bereich | Sichtprüfung | 1 = OK | Keine gebrochenen Litzen |
| | Spannung | Rig-Gauge oder Lothsen | 1–2 = OK | Herstellervorgabe |
| | Toggle/Gabelkopf | Sichtprüfung Bolzen | 1–2 = OK | Kein Verschleiß >5 % |

**Bewertungsskala:**
- 1 = Einwandfrei (neuwertig)
- 2 = Gut (normale Alterung, wartungsfrei)
- 3 = Akzeptabel (Wartung empfohlen)
- 4 = Mangelhaft (Wartung erforderlich vor nächster Nutzung)
- 5 = Kritisch (Sofortige Reparatur/Austausch)

**Gesamtzeitaufwand:** 3–5 Stunden (inkl. Mastbesteigung)
**Empfehlung:** Jährliche Inspektion durch qualifizierten Rigger bei Booten >12 m

### 3.6 5-Jahres-Generalüberholung

Alle 5 Jahre sollte die Rollreffanlage komplett demontiert, inspiziert und überholt werden:

**Arbeitsschritte 5-Jahres-Service:**

| Schritt | Maßnahme | Details | Zeitaufwand |
|---|---|---|---|
| 1 | Segel abschlagen | Luff-Tape komplett aus Profil entfernen | 30–60 min |
| 2 | Halyard lösen | Halyard vom Swivel trennen | 10 min |
| 3 | Vorstag entspannen | Achterstag lösen, Wantenspanner aufdrehen | 15 min |
| 4 | Profilstag demontieren | Profil-Sektionen einzeln abnehmen, nummerieren | 60–120 min |
| 5 | Drum-Unit demontieren | Drum von Vorstag-Terminal lösen | 30 min |
| 6 | Halyard-Swivel demontieren | Vom Masttop abnehmen (Mastbesteigung) | 45 min |
| 7 | Lager ausbauen | Alle Lager aus Drum und Swivel entfernen | 30–60 min |
| 8 | Lager prüfen/tauschen | Spiel, Geräusch, Korrosion bewerten → bei Zweifeln tauschen | 15 min |
| 9 | Vorstag inspizieren | Gesamte Länge auf gebrochene Litzen (Magnete, Dye-Penetrant) | 30–60 min |
| 10 | Profil-Sektionen prüfen | Verformung, Kanal-Zustand, Verbindungsstücke | 30 min |
| 11 | Drum-Dichtungen erneuern | Alle O-Ringe und Dichtungen durch Neu-Teile ersetzen | 15 min |
| 12 | Alles reinigen | Süßwasser + milder Reiniger, trocknen | 30 min |
| 13 | Neu schmieren | Frisches Fett/Öl auf alle Lager und Gleitflächen | 15 min |
| 14 | Zusammenbau | In umgekehrter Reihenfolge, Drehmomente beachten | 120–180 min |
| 15 | Funktionstest | 5x furlen/unfurlen, Geräuschprüfung | 15 min |

**Gesamtzeitaufwand:** 8–14 Stunden (1,5–2 Arbeitstage)
**Kosten (Fachbetrieb):** 800–2.500 EUR (je nach Systemgröße und Befund)
**Kosten (DIY, nur Material):** 150–500 EUR (Lager, Dichtungen, Schmierstoff)

### 3.7 10-Jahres-Komplettrevision

Nach 10 Jahren empfiehlt sich eine Komplettrevision, die zusätzlich umfasst:

- **Vorstag-Austausch** (empfohlen nach 10–15 Jahren): 400–1.800 EUR (je nach Länge und Durchmesser)
- **Profil-Verbindungsstücke komplett erneuern**: 150–400 EUR
- **Alle Kunststoff-Komponenten erneuern** (Drum-Gehäuse, Abdeckungen): 200–600 EUR
- **Toggle und Gabelköpfe prüfen/tauschen**: 100–300 EUR
- **Erwägung eines System-Upgrades**: z.B. Furlex 200S → 300S bei Wechsel auf größere Genua

**Gesamtkosten 10-Jahres-Revision:** 1.500–5.000 EUR
**Alternative:** Komplett-Neuanlage ab 2.500–8.000 EUR (bei älteren Systemen oft wirtschaftlicher)

---

## 4. Lager-Wartung und -Austausch

### 4.1 Übersicht Lagertypen in Rollreffanlagen

Rollreffanlagen verwenden verschiedene Lagertypen, deren Kenntnis für korrekte Wartung und Austausch entscheidend ist:

#### 4.1.1 Kugellager (Ball Bearings)

**Einsatz:** Hauptlager in Drum und Swivel der meisten Furler
**Bauart:** Einreihige Rillenkugellager (Deep Groove Ball Bearings), meist abgedichtet (2RS) oder gedeckelt (ZZ)
**Material:** Kugeln und Laufbahnen aus Edelstahl AISI 440C oder 316L, Käfig aus PA6.6 oder Messing

**Typische Lagergrößen nach Furler-Modell:**

| Furler-Modell | Position | Lagergröße | Lagertyp | Anzahl |
|---|---|---|---|---|
| Furlex 200S | Unteres Lager | 6004-2RS | 20×42×12 mm | 2 |
| Furlex 200S | Oberes Lager | 6003-2RS | 17×35×10 mm | 2 |
| Furlex 300S | Unteres Lager | 6005-2RS | 25×47×12 mm | 2 |
| Furlex 300S | Oberes Lager | 6004-2RS | 20×42×12 mm | 2 |
| Furlex 400S | Unteres Lager | 6006-2RS | 30×55×13 mm | 2 |
| Furlex 400S | Oberes Lager | 6005-2RS | 25×47×12 mm | 2 |
| Profurl C290 | Unteres Lager | 6003-2RS | 17×35×10 mm | 2 |
| Profurl C290 | Oberes Lager | 6002-2RS | 15×32×9 mm | 2 |
| Profurl C430 | Unteres Lager | 6005-2RS | 25×47×12 mm | 2 |
| Profurl C430 | Oberes Lager | 6004-2RS | 20×42×12 mm | 2 |
| Profurl NEX 1.0 | Unteres Lager | 6003-2RS | 17×35×10 mm | 2 |
| Profurl NEX 1.0 | Oberes Lager | 6002-2RS | 15×32×9 mm | 2 |
| Profurl NEX 2.0 | Unteres Lager | 6005-2RS | 25×47×12 mm | 2 |
| Profurl NEX 2.0 | Oberes Lager | 6003-2RS | 17×35×10 mm | 2 |
| Harken MKIV Unit 0 | Unteres Lager | 6002-2RS | 15×32×9 mm | 2 |
| Harken MKIV Unit 1 | Unteres Lager | 6003-2RS | 17×35×10 mm | 2 |
| Harken MKIV Unit 2 | Unteres Lager | 6004-2RS | 20×42×12 mm | 2 |
| Harken MKIV Unit 3 | Unteres Lager | 6005-2RS | 25×47×12 mm | 2 |
| Harken MKIV Unit 4 | Unteres Lager | 6006-2RS | 30×55×13 mm | 2 |
| Facnor FX+ 1500 | Unteres Lager | 6003-2RS | 17×35×10 mm | 2 |
| Facnor FX+ 2500 | Unteres Lager | 6005-2RS | 25×47×12 mm | 2 |
| Facnor FX+ 3500 | Unteres Lager | 6006-2RS | 30×55×13 mm | 2 |

**Hinweis:** Lager müssen IMMER als Paar getauscht werden (oberes + unteres Lager einer Position). Niemals nur ein Lager eines Paares ersetzen.

#### 4.1.2 Nadellager (Needle Bearings)

**Einsatz:** Vereinzelt in älteren Profurl-Systemen und Harken-Winschen-basiert
**Bauart:** Nadelhülse mit oder ohne Innenring
**Vorteil:** Hohe Tragfähigkeit bei kompakter Bauform
**Nachteil:** Empfindlicher gegen Verschmutzung, höherer Wartungsbedarf
**Wartung:** Jährliches Nachschmieren mit Harken Winch Grease (Art.-Nr. BK4513) oder gleichwertigem wasserfestem Fett

#### 4.1.3 Torlon/PTFE Gleitlager (Sleeve Bearings)

**Einsatz:** Halyard-Swivel (oberes Lager) vieler Systeme, einige Code-0-Furler
**Bauart:** Buchse aus Torlon (PAI) oder PTFE-Compound
**Material:** Torlon 4301 (Standard), Torlon 4275 (verstärkt), Virgin PTFE, PTFE+Glasfaser

**Verschleißmuster:**
- Gleichmäßiger Abtrag: Normal, Austausch bei >15 % Spiel-Zunahme
- Einseitiger Abtrag: Hinweis auf Fehlbelastung (schiefes Vorstag, Halyard-Winkel)
- Rillenbildung: Hinweis auf Fremdkörper im Lager → Reinigung und Austausch
- Verfärbung (Torlon): Wasseraufnahme → Trocknung und Nachprüfung

**Lebensdauer Gleitlager:**
- Torlon: 15.000–25.000 Betriebszyklen (Furling/Unfurling)
- PTFE: 10.000–20.000 Betriebszyklen
- Praxis-Lebensdauer: 8–15 Jahre bei normaler Nutzung

### 4.2 Lager-Inspektion: Detailliertes Verfahren

#### 4.2.1 Prüfung ohne Demontage (Basis-Check)

**Schritt 1: Akustische Prüfung**
- Segel langsam furlen/unfurlen bei Windstille
- Ohren nah an die Drum halten
- OK: Leises, gleichmäßiges Laufgeräusch
- MANGEL: Kratzen, Knirschen, periodisches Klicken, Quietschen

**Schritt 2: Taktile Prüfung**
- Drum-Trommel von Hand drehen (ohne Segel, Furling-Leine gelöst)
- OK: Gleichmäßiger, leichter Widerstand über 360°
- MANGEL: Schwergängige Stellen, Rastpunkte, plötzliche Widerstandsänderungen

**Schritt 3: Spiel-Prüfung**
- Drum-Trommel axial (hoch/runter) und radial (seitlich) bewegen
- OK: Kein fühlbares Spiel oder <0,3 mm
- MANGEL: Deutlich fühlbares Spiel >0,5 mm, Klacken

**Schritt 4: Drehwiderstand-Messung (für Profis)**
- Federwaage oder Drehmomentschlüssel an Furling-Leine
- Messung: Kraft zum Drehen der leeren Trommel (ohne Segel)
- Richtwerte: 0,5–2,0 Nm für kleine Furler, 1,0–4,0 Nm für große Furler
- >5,0 Nm: Lager defekt oder verschmutzt

#### 4.2.2 Prüfung mit Demontage (Detailcheck)

**Voraussetzung:** Furler demontiert gemäß Hersteller-Anleitung

**Schritt 1: Lager-Entnahme**
- Sicherungsringe (Seeger-Ringe) entfernen mit Seeger-Ringzange
- Lager mit Lagerabzieher oder Dorn vorsichtig heraustreiben
- NIEMALS mit Hammer direkt auf den Lageraußenring schlagen

**Schritt 2: Sichtprüfung**
- Laufbahnen auf Riefen, Pittings (Grübchen), Verfärbungen prüfen
- Dichtungen auf Risse und Elastizitätsverlust prüfen
- Käfig auf Bruch oder Verformung prüfen

**Schritt 3: Funktionsprüfung einzelner Lager**
- Lager zwischen Daumen und Zeigefinger drehen
- OK: Absolut gleichmäßig, kein fühlbarer Rast- oder Kratzpunkt
- MANGEL: Jedes Kratzen, Rasten oder Ungleichmäßigkeit → Austausch

**Schritt 4: Spiel-Messung**
- Axialspiel: Innenring gegen Außenring verschieben
- Standard-Toleranz: C3 (erhöhtes Spiel für thermische Ausdehnung) oder CN (Normal)
- Lager mit deutlich fühlbarem Spiel: Austausch

### 4.3 Lager-Schmierung

#### 4.3.1 Empfohlene Schmierstoffe

| Produkt | Typ | Einsatz | Gebindegröße | ca. Preis |
|---|---|---|---|---|
| McLube OneDrop Ball Bearing Conditioner | Niedrigviskoses Öl | Kugellager Furler | 28 ml (Art. 0860) | 18–22 EUR |
| Harken Pawl Oil | Niedrigviskoses Öl | Kugellager, Klinken | 30 ml (Art. BK4521) | 14–18 EUR |
| Harken Winch Grease (White) | PTFE-Fett | Nadellager, Gleitlager | 100 g (Art. BK4513) | 16–20 EUR |
| Selden Furler Bearing Grease | Spezialfett | Selden/Furlex Lager | 50 g (Art. 507-879) | 22–28 EUR |
| Lewmar Winch Oil | Niedrigviskoses Öl | Universell, Lager | 55 ml (Art. 19700100) | 12–16 EUR |
| Tef-Gel | Anti-Seize/Korrosionsschutz | Gewinde, Alu/Edelstahl-Kontakt | 60 g (Art. TG-60) | 25–30 EUR |
| Duralac | Isolierpaste | Galvanische Isolierung | 115 ml | 15–20 EUR |
| Lanocote | Lanolin-Paste | Universalschutz, Gewinde | 120 g | 18–24 EUR |

#### 4.3.2 Schmierverfahren: Abgedichtete Kugellager (2RS)

Abgedichtete Lager (2RS-Suffix) sind werkseitig gefettet und theoretisch „wartungsfrei". In der Praxis auf Yachten empfiehlt sich dennoch eine regelmäßige Nachschmierung:

**Methode A: Öl-Nachschmierung (ohne Demontage)**
1. Furling-Leine lösen, Drum freilegen
2. 2–3 Tropfen McLube OneDrop oder Harken Pawl Oil auf die sichtbare Lagerdichtung tropfen
3. Drum mehrmals von Hand drehen, damit Öl eindringt
4. Überschüssiges Öl abwischen
5. **Intervall:** Alle 6 Monate (Salzwasser), jährlich (Süßwasser)

**Methode B: Fett-Nachschmierung (mit Demontage)**
1. Lager ausbauen (siehe 4.2.2)
2. Dichtung vorsichtig mit feinem Schraubendreher abhebeln (nur eine Seite!)
3. Altes Fett mit Bremsenreiniger ausspülen
4. Neues Fett einbringen: Lagerhohlraum zu 30–40 % füllen (NICHT vollständig!)
5. Dichtung wieder aufdrücken
6. Lager einbauen
7. **Intervall:** Alle 5 Jahre oder bei 5-Jahres-Überholung

**WARNUNG:** Lager NIEMALS mit mehr als 40 % Fettfüllung betreiben. Überfüllung führt zu erhöhter Reibung, Wärmeentwicklung und vorzeitigem Dichtungsversagen.

#### 4.3.3 Verbotene Schmierstoffe

| Produkt | Warum verboten | Folgeschaden |
|---|---|---|
| WD-40 | Kein Schmierstoff, löst vorhandenes Fett auf | Trockenlauf, Lagerausfall |
| Silikonspray | Bildet keine tragfähige Schmierfilme | Unzureichende Schmierung |
| Vaseline | Nicht temperaturbeständig, wird ausgewaschen | Korrosion nach Auswaschen |
| Motoröl | Enthält Detergenzien, greift Dichtungen an | Dichtungsquellung/-bruch |
| Grafitpaste | Grafitpartikel wirken abrasiv auf Edelstahl-Laufbahnen | Vorzeitiger Verschleiß |
| Kupferpaste | Galvanische Korrosion mit Aluminium | Zerstörung Alu-Komponenten |
| Lithium-Fett (Standard) | Nicht salzwasserbeständig, nicht lagerfest | Auswaschen, Korrosion |

### 4.4 Lager-Austausch: Schritt-für-Schritt

#### 4.4.1 Furlex 200S/300S — Unteres Lager (Drum)

**Benötigte Teile:**
- 2x Kugellager (Furlex 200S: 6004-2RS; Furlex 300S: 6005-2RS)
- Selden Service Kit (Art.-Nr. 507-955-01 für 200S; 507-956-01 für 300S) enthält: Lager, Dichtungen, Sicherungsringe
- Preis Service Kit: 85–120 EUR

**Benötigtes Werkzeug:**
- Seeger-Ringzange (innen + außen)
- Lagerabzieher (alternativ: zwei flache Schraubendreher + Vorsicht)
- Lagereinpresswerkzeug (Selden Art.-Nr. 507-899) oder passende Nuss/Hülse
- Drehmomentschlüssel (5–25 Nm)
- Bremsenreiniger

**Vorgehensweise:**
1. Furling-Leine entfernen, Drum-Abdeckung abnehmen (3x Innensechskant M4)
2. Unteren Sicherungsring mit Seeger-Ringzange entfernen
3. Drum-Gehäuse nach unten abziehen (ggf. mit leichten Hebelkräften)
4. Oberen Sicherungsring entfernen
5. Unteres Lager mit Abzieher oder Dorn nach unten heraustreiben
6. Oberes Lager mit Abzieher oder Dorn nach oben heraustreiben
7. Lagersitze reinigen (Bremsenreiniger, fusselfreier Lappen)
8. Lagersitze auf Korrosion und Verschleiß prüfen (bei Beschädigung: Komplettaustausch Drum)
9. Neue Lager mit Einpresswerkzeug einsetzen — IMMER am Außenring drücken!
10. Sicherungsringe einsetzen
11. Drum-Gehäuse wieder aufsetzen, Dichtungen korrekt positionieren
12. Drum-Abdeckung montieren, Schrauben mit Tef-Gel sichern (3 Nm)
13. Funktionstest: Drum muss sich leichtgängig und geräuschfrei drehen

**WICHTIG:** Lager dürfen NIEMALS am Innenring eingedrückt werden, wenn sie am Außenring sitzen (und umgekehrt). Kraft immer auf den Ring ausüben, der im Sitz sitzt.

#### 4.4.2 Profurl NEX 1.0/2.0 — Lager-Austausch

**Benötigte Teile:**
- Profurl Bearing Kit NEX (Art.-Nr. KNEX-BEAR)
- Enthält: 2x Kugellager, 2x O-Ring, 1x Sicherungsring
- Preis: 75–95 EUR

**Vorgehensweise:**
1. Drei Schrauben der Drum-Abdeckung entfernen (Torx T25)
2. Abdeckung abnehmen, Innenleben freilegen
3. Distanzhülse nach oben herausziehen
4. Unteres Lager mit Dorn nach unten heraustreiben
5. Oberes Lager mit Dorn nach oben heraustreiben
6. Reinigung und Inspektion der Lagersitze
7. Neue O-Ringe einsetzen (leicht gefettet mit Selden Bearing Grease)
8. Neues unteres Lager einpressen (Außenring-Führung)
9. Distanzhülse einsetzen
10. Neues oberes Lager einpressen
11. Sicherungsring einrasten
12. Abdeckung montieren (Torx T25, 2,5 Nm)
13. Funktionstest

#### 4.4.3 Harken MKIV — Lager-Austausch

**Benötigte Teile:**
- Harken Furler Bearing Kit (Modellspezifisch):
  - Unit 0: Art.-Nr. BK4515-0 (ca. 65 EUR)
  - Unit 1: Art.-Nr. BK4515-1 (ca. 78 EUR)
  - Unit 2: Art.-Nr. BK4515-2 (ca. 95 EUR)
  - Unit 3: Art.-Nr. BK4515-3 (ca. 120 EUR)
  - Unit 4: Art.-Nr. BK4515-4 (ca. 155 EUR)

**Besonderheit Harken MKIV:**
Harken verwendet eine patentierte Lageranordnung mit zwei axialen Kugellagern und einem radialen Kugellager. Die Demontage erfordert das Harken-Spezialwerkzeug (Bearing Press, Art.-Nr. BK4590), das im Fachhandel ausgeliehen werden kann.

**Vorgehensweise:**
1. Locking Ring mit Hakenschlüssel lösen (Linksgewinde bei Unit 2–4!)
2. Drum-Oberteil abheben
3. Lageranordnung als Einheit entnehmen
4. Alle drei Lager mit Harken Bearing Press austauschen
5. Lageranordnung mit frischem Harken Winch Grease bestücken
6. Zusammenbau in umgekehrter Reihenfolge
7. Locking Ring mit korrektem Drehmoment anziehen (Unit 2: 8 Nm, Unit 3: 12 Nm, Unit 4: 15 Nm)

#### 4.4.4 Facnor FX+ — Lager-Austausch

**Benötigte Teile:**
- Facnor Bearing Service Kit (Modellspezifisch):
  - FX+ 1500: Art.-Nr. FX15-BRG (ca. 70 EUR)
  - FX+ 2500: Art.-Nr. FX25-BRG (ca. 95 EUR)
  - FX+ 3500: Art.-Nr. FX35-BRG (ca. 125 EUR)

**Besonderheit Facnor:**
Facnor FX+ verwendet vorgespannte Lagerpaare (Back-to-Back/O-Anordnung). Bei Austausch IMMER als Satz tauschen, da die Lager aufeinander eingeschliffen sind.

**Vorgehensweise:**
1. Vier Schrauben der Drum-Basis lösen (Innensechskant M5)
2. Drum nach oben abziehen
3. Lagerhülse komplett entnehmen
4. Alte Lager herausdrücken (Lagerpresse empfohlen)
5. Neue Lager einpressen — auf korrekte Orientierung achten (O-Anordnung!)
6. Lagerspiel prüfen: Axialspiel 0,02–0,05 mm (Facnor-Spezifikation)
7. Lagerhülse einsetzen, Drum aufsetzen
8. Schrauben mit Tef-Gel sichern (5 Nm)
9. Funktionstest mit Drehmomentmessung

#### 4.4.5 Karver KF-Serie — Lager-Austausch

**Benötigte Teile:**
- Karver Service Kit (Modellspezifisch):
  - KF3: Art.-Nr. KF3-SRV (ca. 55 EUR)
  - KF4: Art.-Nr. KF4-SRV (ca. 65 EUR)
  - KF5: Art.-Nr. KF5-SRV (ca. 80 EUR)
  - KF7: Art.-Nr. KF7-SRV (ca. 110 EUR)
  - KF8: Art.-Nr. KF8-SRV (ca. 145 EUR)

**Besonderheit Karver:**
Karver-Furler verwenden Torlon-Gleitlager im oberen Swivel und Kugellager in der Drum. Die Torlon-Buchsen haben eine definierte Einbaurichtung (Kerbe nach oben).

### 4.5 Lager-Ersatzteil-Referenz: Universallager

Wer keine Original-Herstellerteile beziehen kann oder will, kann bei den meisten Furlern Standard-Industrielager verwenden:

**Bezugsquellen für Marine-Edelstahllager:**
- SMB Bearings (UK): www.smbbearings.com — Edelstahllager Einzelstück ab 8 EUR
- GBS Bearing (DE): www.gbs-bearing.de — 316L-Lager auf Anfrage
- Kugellager-Express (DE): www.kugellager-express.de — Standard-Edelstahllager

**Wichtig bei Universallagern:**
- Nur Edelstahl AISI 440C oder 316L verwenden (NIEMALS verchromten Stahl!)
- Dichtung: 2RS (beidseitig abgedichtet), NICHT ZZ (beidseitig gedeckelt)
- Lagerluft: C3 (erhöht) bevorzugt, da thermische Ausdehnung in der Sonne
- Käfig: Nylon (PA6.6) oder Messing, NICHT Stahl

---

## 5. Drum- und Trommel-Wartung

### 5.1 Funktionsprinzip der Furler-Trommel

Die Trommel (Drum) ist das Herzstück der Rollreffanlage. Sie wandelt die Zugkraft der Furling-Leine in eine Drehbewegung um, die über das Profil das Segel aufrollt. Die Drum enthält:
- Die Hauptlager (siehe Kapitel 4)
- Den Leineneinlauf mit Führung
- Dichtungen gegen Salz- und Spritzwasser
- Die mechanische Verbindung zum Vorstag-Terminal

### 5.2 Leinenführung und Verschleiß

**Häufige Probleme:**

| Problem | Ursache | Lösung |
|---|---|---|
| Leine springt aus der Trommel | Zu wenig Leinenspannung, falsche Wickelrichtung | Leinenführung korrekt einstellen, Rücklaufsperre prüfen |
| Ungleichmäßige Wicklung | Abgenutzte Leinenführung, zu dünne Leine | Leinenführung austauschen, korrekte Leinenstärke verwenden |
| Leine schneidet in Kunststoff | Übermäßige Last, zu dünne Leine | Leinenstärke erhöhen, Drum-Einlauf auf scharfe Kanten prüfen |
| Leine klemmt | Überwerfer, Salzablagerungen | Wicklung korrigieren, Drum reinigen |

**Korrekte Leinenstärken nach Furler-Modell:**

| Furler-Modell | Leinen-Ø empfohlen | Min. Ø | Max. Ø | Empfohlenes Produkt |
|---|---|---|---|---|
| Furlex 200S | 6 mm | 5 mm | 8 mm | Marlow D2 Racing 6 mm |
| Furlex 300S | 8 mm | 6 mm | 10 mm | Liros Top Cruising 8 mm |
| Furlex 400S | 10 mm | 8 mm | 12 mm | Robline Orion 500 10 mm |
| Profurl C290 | 6 mm | 5 mm | 8 mm | FSE Robline Admiral 6 mm |
| Profurl NEX 1.0 | 6 mm | 5 mm | 8 mm | Marlow Excel Pro 6 mm |
| Profurl NEX 2.0 | 8 mm | 6 mm | 10 mm | Liros Top Cruising 8 mm |
| Harken MKIV Unit 0-1 | 6 mm | 5 mm | 8 mm | Harken Flexi Flyer 6 mm |
| Harken MKIV Unit 2-3 | 8 mm | 6 mm | 10 mm | Harken Flexi Flyer 8 mm |
| Harken MKIV Unit 4 | 10 mm | 8 mm | 12 mm | Harken Flexi Flyer 10 mm |
| Facnor FX+ 1500 | 6 mm | 5 mm | 8 mm | Cousin Diflex 6 mm |
| Facnor FX+ 2500 | 8 mm | 7 mm | 10 mm | Cousin Diflex 8 mm |

### 5.3 Dichtungen und O-Ringe

**Inspektion:**
- Dichtungen bei jeder 5-Jahres-Überholung erneuern (auch wenn optisch noch in Ordnung)
- O-Ringe auf Risse, Quetschung und Elastizitätsverlust prüfen
- Verhärtete oder verformte O-Ringe sofort tauschen

**Dichtungsmaterialien:**
- Standard: NBR (Nitril-Butadien-Kautschuk) — Shore A 70, -30 bis +100 °C
- Premium: FKM (Viton) — Shore A 75, -20 bis +200 °C, bessere Chemikalienbeständigkeit
- Für Salzwasser empfohlen: FKM/Viton wegen besserer Langzeitbeständigkeit

**O-Ring-Schmierung bei Einbau:**
- IMMER mit Silikonfett (nicht Silikonspray!) leicht einreiben
- Empfohlen: Dow Corning Molykote 111 oder Super Lube Silicone Grease
- Erleichtert Einbau und verlängert Lebensdauer um 30–50 %

### 5.4 Drum-Demontage und Reassembly

#### 5.4.1 Allgemeines Verfahren (gilt für die meisten Systeme)

**Demontage:**
1. Furling-Leine komplett entfernen
2. Drum-Abdeckung entfernen (Schrauben/Clips)
3. Sicherungsringe und Distanzstücke entnehmen (Reihenfolge dokumentieren!)
4. Drum-Gehäuse vom Vorstag-Terminal trennen
5. Alle Teile in beschriftete Gefäße sortieren

**KRITISCH:** Vor der Demontage IMMER fotografieren! Jede Position, jede Scheibe, jede Orientierung. Viele Teile sehen ähnlich aus, haben aber definierte Einbaurichtungen.

**Reassembly:**
1. Alle Teile reinigen und prüfen
2. Neue Dichtungen und O-Ringe einsetzen (gefettet)
3. Lager einpressen oder einsetzen
4. Distanzstücke in korrekter Reihenfolge einbauen
5. Drum-Gehäuse aufsetzen, auf korrekten Sitz aller Dichtungen achten
6. Sicherungsringe einsetzen
7. Abdeckung montieren mit korrektem Drehmoment
8. Funktionstest

#### 5.4.2 Spezifische Verfahren: Furlex 200S/300S

**Besonderheit:** Furlex verwendet eine zweiteilige Drum mit innerem und äußerem Ring. Der innere Ring sitzt auf dem Vorstag-Terminal, der äußere Ring trägt die Furling-Leine.

**Demontage-Reihenfolge (von oben nach unten):**
1. Drei Innensechskant-Schrauben M4 × 16 der oberen Abdeckung (3 Nm)
2. Obere Abdeckung abheben
3. Sicherungsring oben mit Seeger-Ringzange entfernen
4. Distanzscheibe entnehmen
5. Drum-Trommel (äußerer Ring) nach oben abziehen
6. Oberes Lager entnehmen
7. Unteres Lager mit Dorn nach unten heraustreiben
8. Sicherungsring unten entfernen
9. Innerer Ring bleibt auf Vorstag-Terminal

**Zusammenbau in umgekehrter Reihenfolge. Drehmomente:**
- Abdeckungsschrauben: 3 Nm
- Alle Schrauben mit Tef-Gel oder Loctite 243 (mittelfest) sichern

#### 5.4.3 Spezifische Verfahren: Profurl NEX

**Besonderheit:** Profurl NEX hat ein modulares Design mit austauschbaren Trommelgrößen. Die Drum-Basis ist identisch, nur der Wickelkörper variiert.

**Demontage-Reihenfolge:**
1. Drei Torx-T25-Schrauben der Drum-Abdeckung entfernen
2. Abdeckung abheben
3. Wickelkörper nach oben abziehen
4. Lagerbuchse mit Sicherungsring entfernen
5. Lager mit Dorn heraustreiben

**Zusammenbau: Drehmomente:**
- Torx-Schrauben Abdeckung: 2,5 Nm
- Vorstag-Terminal-Mutter: modellabhängig (15–25 Nm)

#### 5.4.4 Spezifische Verfahren: Harken MKIV

**Besonderheit:** Harken MKIV hat einen patentierten Schnellverschluss (Locking Ring) mit Linksgewinde (Unit 2–4). Unit 0–1 haben Rechtsgewinde.

**Demontage-Reihenfolge:**
1. Locking Ring mit Hakenschlüssel (Harken Art.-Nr. BK4591) lösen
2. Oberteil abheben — Vorsicht, Kugeln können herausfallen!
3. Lageranordnung als Einheit entnehmen
4. Bei Bedarf: Einzellager mit Harken Bearing Press (BK4590) austauschen

**Zusammenbau: Drehmomente:**
- Locking Ring Unit 0–1: 5 Nm (Rechtsgewinde)
- Locking Ring Unit 2: 8 Nm (Linksgewinde!)
- Locking Ring Unit 3: 12 Nm (Linksgewinde!)
- Locking Ring Unit 4: 15 Nm (Linksgewinde!)

### 5.5 UV-Schutz der Kunststoffteile

**Problematik:** Drum-Gehäuse, Abdeckungen und Profilverbindungen sind der UV-Strahlung permanent ausgesetzt. UV-Degradation führt zu:
- Versprödung → Rissbildung unter Last
- Verfärbung (Vergilbung oder Ausbleichung)
- Festigkeitsverlust → plötzliches Versagen möglich

**Schutzmaßnahmen:**
1. **Drum-Cover verwenden:** Selden Furlex Drum Cover (Art.-Nr. 507-862-XX), Profurl Drum Cover, Harken Drum Bag
2. **UV-Schutzmittel:** 303 Aerospace Protectant auf alle Kunststoffteile (alle 3 Monate)
3. **Regelmäßige Inspektion:** Klopftest — spröder Kunststoff klingt höher und heller als intakter
4. **Rechtzeitig tauschen:** Sichtbare Haarrisse = sofortiger Austausch

---

## 6. Profilstagsysteme — Wartung und Reparatur

### 6.1 Aufbau eines Profilstags

Das Profilstag (Foil System, Luff Extrusion) umhüllt das Vorstag und bildet den Kanal für das Luff-Tape des Segels. Es besteht aus:

- **Profil-Sektionen** (1,5–2,5 m lang) aus eloxiertem Aluminium
- **Verbindungsstücke** (Connectors, Joining Pieces) aus Kunststoff oder Aluminium
- **Halteklammern** (Retention Clips) am Vorstag
- **Top-Fitting** (Übergang zum Halyard-Swivel)
- **Bottom-Fitting** (Übergang zur Drum-Unit)

### 6.2 Profilverbindungen — Inspektion und Austausch

**Funktion:** Profilverbindungen halten die einzelnen Profil-Sektionen zusammen und ermöglichen gleichzeitig eine gewisse Flexibilität für die Rotation.

**Inspektion:**

| Prüfpunkt | Methode | OK-Kriterium | Mangel-Kriterium |
|---|---|---|---|
| Spalt an Verbindung | Sichtprüfung, Fühllehre | <0,5 mm | >1,0 mm = Austausch |
| Rotation in Verbindung | Hand-Drehtest | Gleichmäßig, kein Spiel | Klacken, Spiel >1° |
| Kunststoff-Zustand | Sichtprüfung, Klopftest | Elastisch, keine Risse | Spröde, Risse, Verfärbung |
| Korrosion | Sichtprüfung | Keine Verfärbung | Weißer Belag = Alu-Korrosion |
| Sicherung | Splinte/Clips prüfen | Alle vorhanden | Fehlend = sofort ersetzen |

**Austausch-Verbindungsstücke nach Hersteller:**

| Hersteller | Profilserie | Verbindungsstück Art.-Nr. | Preis/Stk. |
|---|---|---|---|
| Selden/Furlex | 200S | 507-821-01 | 12–18 EUR |
| Selden/Furlex | 300S | 507-822-01 | 15–22 EUR |
| Selden/Furlex | 400S | 507-823-01 | 18–25 EUR |
| Profurl | C-Serie | CON-C290 / CON-C430 | 10–20 EUR |
| Profurl | NEX-Serie | CON-NEX10 / CON-NEX20 | 12–18 EUR |
| Harken | MKIV | HAR-FOIL-CON (modellspez.) | 15–25 EUR |
| Facnor | FX+/LS | FAC-FOIL-CON (modellspez.) | 12–22 EUR |

### 6.3 Profilverschleiß und Verformung

**Typische Verschleißbilder:**

1. **Kanalverengung:** Luff-Tape reibt an den Profilwänden → erhöhter Widerstand beim Furling
   - Ursache: Seitliche Belastung, oft durch zu geringe Vorstag-Spannung
   - Lösung: Profil richten (bei leichter Verformung) oder ersetzen

2. **Kanalaufweitung:** Segel rutscht im Profil, schlechte Segelform
   - Ursache: Übermäßige Belastung, falsche Profilgröße für Segelgewicht
   - Lösung: Profil-Sektion ersetzen

3. **Korrosion im Kanal:** Raue Oberfläche, Segel klemmt
   - Ursache: Beschädigte Eloxalschicht, Salzwasser-Stagnation im Kanal
   - Lösung: Schleifen mit Scotch-Brite (fein), Konservierung mit McLube SailKote

4. **Verformung durch Impact:** Delle oder Knicke im Profil
   - Ursache: Anschlagen gegen Mast, Fallen, Deckshardware
   - Lösung: Bei geringfügiger Verformung: Richten mit Profil-Richtblock. Bei starker Verformung: Sektion ersetzen.

### 6.4 Luff-Tape-Kanal: Reinigung und Pflege

**Warum wichtig:** Ein verschmutzter oder korrodierter Luff-Tape-Kanal ist die häufigste Ursache für schwergängiges Furling und Segel-Klemmer.

**Reinigungsverfahren:**

**Methode A: Reinigungsleine (Standard)**
1. Dünne Leine (3 mm) mit angeknoteter Scotch-Brite-Rolle durch den Kanal ziehen
2. Von oben nach unten arbeiten
3. Mit Süßwasser nachspülen
4. Mit McLube SailKote (Art.-Nr. 0870) behandeln
5. **Intervall:** Jährlich oder bei Schwergängigkeit

**Methode B: Profilreiniger-Stab (Professionell)**
1. Selden Foil Cleaning Rod (Art.-Nr. 507-895) oder Profurl Foil Cleaner einführen
2. Stab mit rotierenden Bewegungen durch den gesamten Kanal führen
3. Abrasivreste mit Druckluft oder Wasser ausblasen
4. McLube SailKote auftragen
5. **Intervall:** Bei hartnäckigen Verschmutzungen oder Korrosion

**Methode C: Segel als Reiniger (Unterwegs)**
1. Segel mehrfach schnell furlen/unfurlen
2. Luff-Tape wirkt als mechanischer Reiniger
3. Nur als Notlösung, nicht als Regelwartung!

### 6.5 Segel-Einfädelprobleme — Ursachen und Lösungen

**Problem: Segel lässt sich nicht in den Profil-Kanal einführen**

| Mögliche Ursache | Diagnose | Lösung |
|---|---|---|
| Luff-Tape zu dick | Tape-Maß prüfen vs. Kanal-Maß | Segelmacher: Tape anpassen |
| Kanal verschmutzt/korrodiert | Draht durchschieben, Widerstand fühlen | Reinigung (Methode A/B) |
| Profil verdreht | Profil von unten visieren | Verdrehte Sektion demontieren und korrekt einbauen |
| Verbindungsstück versetzt | Finger am Übergang in Kanal einführen | Verbindungsstück ausrichten oder tauschen |
| Kanal vereist (Winter) | Sichtprüfung | Erwärmen mit Heißluftfön (max. 80 °C) |
| Falsches Luff-Tape | Tape-Profil mit Kanal-Profil vergleichen | Segelmacher konsultieren |

**Luff-Tape-Kanalgrößen nach Hersteller:**

| Profilserie | Kanal-Breite | Empf. Tape-Breite | Max. Tape + Segel |
|---|---|---|---|
| Furlex 200S | 11,0 mm | 9,0 mm | 10,5 mm |
| Furlex 300S | 13,5 mm | 11,0 mm | 13,0 mm |
| Furlex 400S | 16,0 mm | 13,0 mm | 15,5 mm |
| Profurl C290 | 10,5 mm | 8,5 mm | 10,0 mm |
| Profurl C430 | 14,0 mm | 11,5 mm | 13,5 mm |
| Profurl NEX 1.0 | 11,0 mm | 9,0 mm | 10,5 mm |
| Profurl NEX 2.0 | 13,5 mm | 11,0 mm | 13,0 mm |
| Harken MKIV (klein) | 10,0 mm | 8,0 mm | 9,5 mm |
| Harken MKIV (groß) | 15,0 mm | 12,5 mm | 14,5 mm |

### 6.6 Profilgeradheits-Prüfung

**Warum wichtig:** Ein gekrümmtes Profil verursacht ungleichmäßiges Furling, Segelklemmer und erhöhten Verschleiß an Lagern.

**Prüfmethode:**
1. Von achtern auf das stehende Profilstag visieren
2. Visuelle Referenz: Das Profil sollte von der Drum bis zum Masttop eine gerade Linie bilden
3. Akzeptable Abweichung: <5 mm pro Meter Profillänge
4. Problematisch: >10 mm pro Meter oder S-Kurve

**Häufige Ursachen für Profilkrümmung:**
- Ungleichmäßige Vorstag-Spannung (Wantenspanner nachstellen)
- Verbogene Profil-Sektion (austauschen)
- Falsch montierte Verbindungsstücke (neu ausrichten)
- Gebrochene Retention Clips (ersetzen)

---

## 7. Schmierstoffe und Korrosionsschutz

### 7.1 Schmierstoff-Matrix nach Anwendung

| Anwendung | Empfohlener Schmierstoff | Alternativen | Menge | Intervall |
|---|---|---|---|---|
| Kugellager (Drum) | McLube OneDrop (0860) | Harken Pawl Oil | 2–3 Tropfen | 6 Monate |
| Kugellager (Swivel) | McLube OneDrop (0860) | Harken Pawl Oil | 2–3 Tropfen | 6 Monate |
| Nadellager | Harken Winch Grease (BK4513) | Selden Bearing Grease | 5 g | Jährlich |
| Gleitlager (Torlon) | McLube SailKote (0870) | Trocken-PTFE-Spray | Dünn aufsprühen | Jährlich |
| Profil-Kanal | McLube SailKote (0870) | Harken McLube Speed Coat | Dünn aufsprühen | Jährlich |
| Gewinde Alu/Edelstahl | Tef-Gel (TG-60) | Duralac, Lanocote | Dünn auftragen | Bei Montage |
| Drum-Dichtungen/O-Ringe | Molykote 111 Silikonfett | Super Lube 21030 | Dünn einreiben | Bei Montage |
| Furling-Leine | Kein Schmierstoff! | — | — | — |
| Schäkel und Bolzen | Lanocote Lanolin-Paste | Tef-Gel | Dünn auftragen | Jährlich |

### 7.2 Schmierstoff-Detailprofile

#### 7.2.1 McLube OneDrop Ball Bearing Conditioner (Art.-Nr. 0860)

**Typ:** Niedrigviskoses synthetisches Öl
**Basis:** PTFE-Dispersion in Trägerlösung
**Eigenschaften:**
- Extrem niedrige Viskosität — dringt in abgedichtete Lager ein
- Bildet dauerhaften PTFE-Film auf Lagerlaufbahnen
- Temperaturbereich: -40 bis +120 °C
- Wasserabweisend, salzwasserbeständig
- Verdrängt Feuchtigkeit aus dem Lager

**Anwendung:** 2–3 Tropfen auf die Lagerdichtung, Lager mehrmals drehen
**Preis:** 18–22 EUR / 28 ml Flasche
**Bezug:** SVB (Art. 601245), Toplicht, Compass, AWN

#### 7.2.2 Harken Pawl Oil (Art.-Nr. BK4521)

**Typ:** Leichtes synthetisches Öl
**Eigenschaften:**
- Speziell für Marine-Lager und Winsch-Klinken
- Tropfpipette für präzise Dosierung
- Guter Korrosionsschutz
- Temperaturbereich: -30 bis +100 °C

**Anwendung:** 2–3 Tropfen auf Lagerdichtung, alternativ Winsch-Klinken
**Preis:** 14–18 EUR / 30 ml Flasche
**Bezug:** SVB (Art. 603112), Toplicht, Segelladen

#### 7.2.3 Harken Winch Grease White (Art.-Nr. BK4513)

**Typ:** PTFE-Hochleistungsfett (weiß)
**Basis:** Lithiumkomplex-Seife mit PTFE-Partikeln
**Eigenschaften:**
- Wasserfest (NLGI 2)
- Beständig gegen Salzwasser und Auswaschen
- Weißes Fett — Verschmutzungen sofort sichtbar
- Temperaturbereich: -20 bis +130 °C
- Tropfpunkt: >260 °C

**Anwendung:** Nadellager, Gleitflächen, Gewinde (dünn!)
**Preis:** 16–20 EUR / 100 g Tube
**Bezug:** SVB, Toplicht, direkt bei Harken-Händlern

#### 7.2.4 McLube SailKote (Art.-Nr. 0870)

**Typ:** Trocken-PTFE-Spray (Aerosol)
**Eigenschaften:**
- Bildet trockenen, nicht klebenden PTFE-Film
- Reduziert Reibung um bis zu 60 %
- Zieht keinen Schmutz an (trocken!)
- Ideal für Profil-Kanäle, Segellatten-Taschen, Traveller
- Temperaturbereich: -50 bis +260 °C

**Anwendung:** Profil-Kanal aussprühen, Segel-Luff-Tape behandeln, alle Gleitflächen
**Preis:** 22–28 EUR / 300 ml Dose
**Bezug:** SVB (Art. 601247), Toplicht, Compass

#### 7.2.5 Tef-Gel (Art.-Nr. TG-60)

**Typ:** Anti-Seize-Paste mit PTFE
**Zusammensetzung:** Petroleumbasis mit 40 % PTFE
**Hauptanwendung:** Galvanische Isolierung zwischen Aluminium und Edelstahl
**Eigenschaften:**
- Verhindert galvanische Korrosion und Festfressen
- Temperaturbereich: -54 bis +260 °C
- Wasserbeständig
- Kompatibel mit allen in Furlern verwendeten Materialien

**Anwendung:** Dünn auf alle Gewinde und Kontaktflächen zwischen verschiedenen Metallen
**Preis:** 25–30 EUR / 60 g Tube
**Bezug:** SVB (Art. 602890), Toplicht, AWN

### 7.3 Galvanische Korrosion — Materialkombinationen

**Grundprinzip:** Wenn zwei unterschiedliche Metalle in Gegenwart eines Elektrolyten (Salzwasser!) in Kontakt kommen, korrodiert das unedlere Metall (Anode) zum Schutz des edleren Metalls (Kathode).

**Galvanische Reihe (in Seewasser, relevante Materialien):**

| Material | Potenzial (V vs. SCE) | Rolle in typischen Paarungen |
|---|---|---|
| Zink | -1,03 | Opferanode |
| Aluminium 6061-T6 | -0,74 | Anode (korrodiert!) |
| Stahl (verzinkt) | -0,61 | Leicht anodisch |
| Edelstahl 316L (passiv) | -0,05 | Kathode (geschützt) |
| Edelstahl 316L (aktiv) | -0,50 | Leicht anodisch |
| Bronze/Messing | -0,24 | Kathodisch zu Alu |
| Titan | +0,06 | Stark kathodisch |
| Carbon/CFK | +0,20 | Extrem kathodisch |

**Kritische Kombinationen in Furlern:**

| Kombination | Risiko | Schutzmaßnahme |
|---|---|---|
| Alu-Profil ↔ Edelstahl-Vorstag | HOCH | Tef-Gel, Duralac, Kunststoff-Isolation |
| Alu-Profil ↔ Edelstahl-Schrauben | MITTEL | Tef-Gel auf alle Gewinde |
| Alu-Profil ↔ CFK-Vorstag | SEHR HOCH | Zwingend Isolationsschicht (GFK-Hülse) |
| Edelstahl-Lager ↔ Alu-Drum | MITTEL | Kunststoff-Lagerbuchse als Isolator |
| Bronze-Toggle ↔ Alu-Profil | HOCH | Tef-Gel + Isolierscheibe |

**Praxisregel:** Jede Metall-Metall-Verbindung am Furler mit Tef-Gel oder Duralac montieren. Ausnahme: Edelstahl auf Edelstahl (kein galvanisches Problem, aber Tef-Gel verhindert Festfressen).

### 7.4 Anodenschutz und Opferanoden

**Einige Furler-Systeme haben eigene Opferanoden:**
- Reckmann Hydraulik-Furler: Zink-Anode am Fuß des Hydraulikzylinders
- Bamar In-Mast Systeme: Zink-Anode am Mast-Fuß
- Selden GXe (elektrisch): Zink-Anode am Motor-Gehäuse

**Prüfung:** Anode jährlich inspizieren. Austausch wenn >50 % aufgezehrt.
**Typische Lebensdauer:** 2–4 Jahre (Salzwasser), 5–8 Jahre (Brackwasser)

### 7.5 Edelstahl-Pflege: 316L vs. 304

**316L (1.4404):** Molybdänlegiert, beständig gegen Lochfraß und Crevice Corrosion in Seewasser. Standard für alle Marine-Anwendungen.

**304 (1.4301):** Preiswerter, aber NICHT für permanenten Salzwasserkontakt geeignet. Leider bei einigen Billig-Furlern und No-Name-Schäkeln verbaut.

**Identifikation:**
- 316L: Markierung „A4" oder „316" oder „1.4404" auf dem Bauteil
- 304: Markierung „A2" oder „304" oder „1.4301"
- Im Zweifelsfall: Molybdän-Schnelltest (Tropftest, ca. 20 EUR)

**Edelstahl-Pflege am Furler:**
1. Regelmäßig Süßwasser abspülen (nach jedem Segeltörn ideal)
2. Fingerabdrücke und Fettflecken entfernen (Edelstahl-Reiniger)
3. Bei Tea-Staining: Oxalsäure-Reiniger (z.B. Bar Keeper's Friend) oder Citrussäure
4. Passivierung wiederherstellen: Beize (Citrussäure 10 %, 30 min einwirken)
5. Politur nur mit Edelstahl-spezifischen Mitteln (z.B. Autosol Edelstahl-Politur)

### 7.6 Aluminium-Profilschutz

**Eloxalschicht bewahren:**
- KEINE Schleifmittel verwenden (zerstört die Eloxalschicht irreversibel)
- Reinigung mit mildem alkalischem Reiniger (pH 8–10), z.B. Star Brite Alu-Reiniger
- NIEMALS säurehaltige Reiniger auf Aluminium anwenden
- KEIN Aceton oder Lösungsmittel auf eloxiertes Aluminium

**Konservierung:**
- Nach Reinigung: Wachs auftragen (z.B. Collinite 845 Insulator Wax)
- Alternative: Tef-Gel dünn auf die Oberfläche einreiben (langfristig)
- UV-Schutz: McLube SailKote bildet eine dünne Schutzschicht

**Bei beschädigter Eloxalschicht:**
- Kleine Stellen: Sofort mit Tef-Gel oder Aluminium-Primer abdecken
- Große Flächen: Professionelle Nachbehandlung (Re-Eloxierung) oder Profil-Sektion tauschen
- Aktive Korrosion (weißer Belag): Mit Scotch-Brite (fein) entfernen, sofort versiegeln

---

## 8. Fehlerbild-Atlas

### Fehlerbild F-15_04-01: Schwergängiges Furling

**Fehlerbild-ID:** F-15_04-01
**Bezeichnung:** Schwergängiges Furling (Heavy/Stiff Furling)
**Schweregrad:** 3 von 5
**Dringlichkeit:** Mittel — vor nächster längerer Fahrt beheben

**Erscheinungsbild:**
- Furling-Leine lässt sich nur unter erhöhter Kraft einziehen
- Segel rollt sich langsam und widerwillig auf
- Spürbare Schwergängigkeit über den gesamten Drehbereich oder in bestimmten Positionen
- Crew beklagt sich über schweres Handling beim Reffen

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Verschmutzte/korrodierte Lager | 35 % |
| 2 | Verschmutzter Profil-Kanal | 25 % |
| 3 | Zu hohe Vorstag-Spannung | 15 % |
| 4 | Verformtes Profil | 10 % |
| 5 | Trockene/fehlende Schmierung | 10 % |
| 6 | Lager-Defekt (Pittings, Korrosion) | 5 % |

**Diagnose-Schritte:**
1. Segel abschlagen → Furler ohne Segel drehen. Leichtgängig? → Problem am Segel/Profil-Kanal
2. Furling-Leine lösen → Drum von Hand drehen. Schwergängig? → Lager-Problem
3. Profil-Verbindungen einzeln prüfen → Blockade an bestimmter Stelle? → Profilproblem
4. Vorstag-Spannung prüfen → Zu hoch? → Wantenspanner nachlassen (Versuch)

**Behebung:**
- Lager schmieren: McLube OneDrop, 2–3 Tropfen je Lager (Kosten: 18–22 EUR)
- Profil-Kanal reinigen: McLube SailKote (Kosten: 22–28 EUR)
- Bei Lager-Defekt: Lager tauschen (Kosten: 65–155 EUR je nach Modell)
- Bei Profilverformung: Betroffene Sektion tauschen (Kosten: 80–200 EUR)

**Präventivmaßnahmen:**
- Halbjährliche Lager-Schmierung
- Jährliche Profil-Kanal-Reinigung
- Vorstag-Spannung nach Hersteller-Vorgabe einstellen
- Drum-Cover verwenden

**Kostenrahmen:** 20–200 EUR (Schmierung) / 200–500 EUR (Lageraustausch) / 300–800 EUR (Profilaustausch)

---

### Fehlerbild F-15_04-02: Ungleichmäßiges Aufrollen

**Fehlerbild-ID:** F-15_04-02
**Bezeichnung:** Ungleichmäßiges Aufrollen (Uneven Furling)
**Schweregrad:** 2 von 5
**Dringlichkeit:** Niedrig bis Mittel — beeinträchtigt Segelperformance

**Erscheinungsbild:**
- Segel rollt sich nicht gleichmäßig auf — Wulste oder Falten
- Unteres Drittel stärker aufgerollt als oberes (oder umgekehrt)
- Segel bildet beim Reffen eine „Kegelform" statt gleichmäßiger Rolle
- UV-Schutzstreifen deckt nicht vollständig ab

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Ungleichmäßige Halyard-Spannung | 30 % |
| 2 | Fehlende Gegenspannung (Schot) beim Furling | 25 % |
| 3 | Profilstag nicht gerade | 15 % |
| 4 | Luff-Tape-Problem | 10 % |
| 5 | Unterschiedliche Lagerreibung oben/unten | 10 % |
| 6 | Segel-Schnitt nicht für Furler optimiert | 10 % |

**Diagnose-Schritte:**
1. Halyard-Spannung prüfen → Soll: fest, aber nicht überspannt
2. Furling-Technik prüfen → Schot muss beim Furling kontrolliert Gegenzug geben
3. Profil von achtern visieren → S-Kurve oder Bogen?
4. Segel komplett entrollen → Luff-Tape auf voller Länge im Kanal?

**Behebung:**
- Halyard-Spannung anpassen: 2-Finger-Regel (Halyard soll bei Windstille 2 Finger breit durchhängen)
- Furling-Technik korrigieren: Schot-Gegenzug = ca. 20–30 % der Furling-Kraft
- Profil richten oder betroffene Sektion tauschen
- Segelmacher konsultieren bei Luff-Tape-Problem

**Präventivmaßnahmen:**
- Crew-Training: Korrektes Furling-Verfahren (Schot-Gegenzug!)
- Regelmäßige Profil-Geradheits-Kontrolle
- Halyard-Markierungen für korrekte Spannung anbringen

**Kostenrahmen:** 0 EUR (Technik-Korrektur) / 80–200 EUR (Profil-Reparatur) / 200–600 EUR (Segel-Anpassung)

---

### Fehlerbild F-15_04-03: Lagergeräusche und Vibrationen

**Fehlerbild-ID:** F-15_04-03
**Bezeichnung:** Lagergeräusche und Vibrationen (Bearing Noise and Vibration)
**Schweregrad:** 4 von 5
**Dringlichkeit:** Hoch — zeitnah beheben, Ausfall droht

**Erscheinungsbild:**
- Kratzendes, knirschendes oder klickendes Geräusch beim Furling
- Spürbare Vibrationen in der Furling-Leine
- Periodisches Klacken bei jeder Umdrehung
- Geräusch verstärkt sich unter Last (Wind)

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Korrodierte Lagerlaufbahnen (Pittings) | 40 % |
| 2 | Fremdkörper im Lager (Sand, Salzkristalle) | 25 % |
| 3 | Lagerspiel durch Verschleiß | 15 % |
| 4 | Gebrochener Lagerkäfig | 10 % |
| 5 | Lose Lager-Befestigung (Sicherungsring) | 5 % |
| 6 | Lose Profilverbindung (sekundäres Geräusch) | 5 % |

**Diagnose-Schritte:**
1. Geräuschquelle lokalisieren: Ohr an Drum → unteres Lager. Ohr an Profilstag in Masthöhe (Stethoskop!) → oberes Lager
2. Drum von Hand drehen (ohne Segel, ohne Last) → Geräusch vorhanden?
3. Sicherungsringe und Befestigungen prüfen → Spiel?
4. Bei Verdacht: Drum öffnen, Lager entnehmen, einzeln prüfen (siehe 4.2.2)

**Behebung:**
- Fremdkörper: Lager spülen mit Bremsenreiniger, neu schmieren (Kosten: 5–10 EUR)
- Korrosion/Verschleiß: Lager tauschen (Kosten: 65–155 EUR je nach Modell + 1–3 Std. Arbeit)
- Gebrochener Käfig: Lager sofort tauschen! Gefahr weiterer Schäden
- Lose Befestigung: Sicherungsring erneuern, Drehmoment prüfen

**Präventivmaßnahmen:**
- Halbjährliche Schmierung (McLube OneDrop)
- Regelmäßige Süßwasser-Spülung
- Drum-Cover gegen Salz-Spray und Sand

**Kostenrahmen:** 10 EUR (Reinigung) / 100–250 EUR (Lageraustausch) / 500–1.500 EUR (bei Folgeschäden)

---

### Fehlerbild F-15_04-04: Segel klemmt im Profil

**Fehlerbild-ID:** F-15_04-04
**Bezeichnung:** Segel klemmt im Profil (Sail Jams in Foil)
**Schweregrad:** 4 von 5
**Dringlichkeit:** Hoch — kann bei Wind nicht reffen/bergen

**Erscheinungsbild:**
- Segel lässt sich nicht vollständig ein- oder ausrollen
- Blockade an einer bestimmten Stelle des Profils
- Luff-Tape sichtbar aus dem Kanal herausgetreten
- Erhöhte Kraft führt nicht zur Lösung, sondern verschlimmert

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Lose Profilverbindung → Versatz im Kanal | 30 % |
| 2 | Korrosion/Verschmutzung im Kanal | 25 % |
| 3 | Luff-Tape beschädigt oder aufgespleißt | 15 % |
| 4 | Profil-Verformung (Delle, Knicke) | 15 % |
| 5 | Fremdkörper im Kanal | 10 % |
| 6 | Falsches Luff-Tape für Profiltyp | 5 % |

**Diagnose-Schritte:**
1. Position der Blockade identifizieren (von unten zählen: welche Profilsektion?)
2. An der Blockadestelle: Profilverbindung prüfen — Versatz? Spalt?
3. Segel vorsichtig in entgegengesetzter Richtung bewegen — löst sich die Blockade?
4. Wenn möglich: Segel komplett herausnehmen und Kanal inspizieren

**Behebung (auf See — Notfall):**
1. KEINEN Gewalt-Versuch! → Risiko des Luff-Tape-Risses
2. Halyard leicht lösen (5–10 cm) → Entlastung des Profils
3. Segel vorsichtig in entgegengesetzter Richtung bewegen
4. Falls unlösbar: Halyard komplett lösen, Segel am Profil herunterziehen, provisorisch bergen

**Behebung (im Hafen):**
1. Blockadestelle identifizieren
2. Profilverbindung ggf. lösen → Segel befreien
3. Kanal reinigen und mit McLube SailKote behandeln
4. Beschädigtes Verbindungsstück oder Profilsektion tauschen
5. Luff-Tape vom Segelmacher prüfen lassen

**Präventivmaßnahmen:**
- Jährliche Profil-Kanal-Reinigung
- Profilverbindungen bei jeder Saison-Wartung prüfen
- Luff-Tape alle 3 Jahre vom Segelmacher prüfen lassen

**Kostenrahmen:** 0 EUR (Reinigung) / 15–25 EUR (Verbindungsstück) / 200–600 EUR (Profil-Sektion) / 300–800 EUR (Luff-Tape-Reparatur)

---

### Fehlerbild F-15_04-05: Trommel-Leinenwicklung fehlerhaft

**Fehlerbild-ID:** F-15_04-05
**Bezeichnung:** Trommel-Leinenwicklung fehlerhaft (Drum Line Wrap Failure)
**Schweregrad:** 2 von 5
**Dringlichkeit:** Niedrig bis Mittel

**Erscheinungsbild:**
- Furling-Leine wickelt sich ungleichmäßig auf die Trommel
- Überwerfer (Leine springt über sich selbst)
- Leine klemmt in der Trommel
- Leine springt aus der Trommelführung

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Falsche Leinenführung zum Cockpit | 30 % |
| 2 | Falsche Leinenstärke | 25 % |
| 3 | Verschlissene Leinenführung an der Trommel | 20 % |
| 4 | Falscher Wicklungswinkel | 15 % |
| 5 | Leine zu alt/steif | 10 % |

**Diagnose-Schritte:**
1. Leinenführung vom Cockpit zur Trommel prüfen → Leine muss tangential einlaufen
2. Leinenstärke prüfen → Herstellervorgabe beachten (siehe Tabelle in 5.2)
3. Leineneinlauf an der Trommel prüfen → Verschleiß, Grate?
4. Leinenzustand prüfen → Steif, verformt, Pilling?

**Behebung:**
- Leinenführungsblock versetzen (korrekte Tangentialposition)
- Leine durch korrekte Stärke ersetzen
- Leinenführung an Trommel mit feiner Feile entgraten
- Neue Furling-Leine einscheren (Kosten: 30–80 EUR für 15–25 m)

**Präventivmaßnahmen:**
- Korrekte Leinenführung bei Installation sicherstellen
- Leine alle 3–5 Jahre tauschen
- Trommel-Leineneinlauf jährlich auf Verschleiß prüfen

**Kostenrahmen:** 30–80 EUR (neue Leine) / 0–50 EUR (Block versetzen) / 15–25 EUR (Trommelführung-Ersatz)

---

### Fehlerbild F-15_04-06: Profilverbindung gelöst

**Fehlerbild-ID:** F-15_04-06
**Bezeichnung:** Profilverbindung gelöst (Foil Joint Separation)
**Schweregrad:** 4 von 5
**Dringlichkeit:** Hoch — Sicherheitsrelevant

**Erscheinungsbild:**
- Sichtbarer Spalt zwischen zwei Profilsektionen
- Klapperndes Geräusch bei Seegang
- Segel klemmt an der betroffenen Stelle
- Im Extremfall: Profil-Sektion dreht sich nicht mehr mit → Vorstag sichtbar

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | UV-degradiertes Kunststoff-Verbindungsstück | 35 % |
| 2 | Fehlender/gebrochener Sicherungssplint | 25 % |
| 3 | Vibrations-induziertes Lockern | 20 % |
| 4 | Mechanische Beschädigung (Impact) | 10 % |
| 5 | Montagefehler (falsches Verbindungsstück) | 10 % |

**Diagnose-Schritte:**
1. Betroffene Verbindung lokalisieren (von unten nach oben prüfen)
2. Spalt messen → >2 mm = sofortige Reparatur
3. Sicherungssplint prüfen → vorhanden und intakt?
4. Verbindungsstück-Material prüfen → Kunststoff spröde?

**Behebung (auf See — Notfall):**
1. Segel komplett furlen
2. Betroffene Stelle mit Tape sichern (selbstverschweißendes Tape, z.B. Rescue Tape)
3. Wenn möglich: Kabelbinder als provisorische Sicherung
4. Bei nächster Gelegenheit: Fachgerechte Reparatur im Hafen

**Behebung (im Hafen):**
1. Segel abschlagen
2. Betroffene Profilsektionen trennen
3. Altes Verbindungsstück entfernen
4. Neues Verbindungsstück einsetzen (Herstellerspezifisch, siehe Tabelle 6.2)
5. Sicherungssplint/Clip einsetzen
6. Segel wieder anschlagen, Funktionstest

**Präventivmaßnahmen:**
- Alle Profilverbindungen jährlich prüfen
- Kunststoff-Verbindungsstücke nach 10 Jahren prophylaktisch tauschen
- Alle Sicherungssplinte bei der 5-Jahres-Überholung erneuern

**Kostenrahmen:** 15–25 EUR (Verbindungsstück) / 50–150 EUR (Rigger-Arbeitszeit)

---

### Fehlerbild F-15_04-07: Korrosion am Drehwirbel (Swivel)

**Fehlerbild-ID:** F-15_04-07
**Bezeichnung:** Korrosion am Drehwirbel (Swivel Corrosion)
**Schweregrad:** 4 von 5
**Dringlichkeit:** Hoch — Tragfähigkeit beeinträchtigt

**Erscheinungsbild:**
- Braune oder weiße Flecken am Halyard-Swivel
- Schwergängigkeit des Swivels
- Sichtbare Pittings (Grübchen) auf der Edelstahl-Oberfläche
- Weißer Belag auf Aluminium-Komponenten
- Festsitzen des Halyard-Schäkels

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Galvanische Korrosion (Alu/Edelstahl ohne Isolierung) | 35 % |
| 2 | Crevice Corrosion (Edelstahl in Spalten) | 25 % |
| 3 | Minderwertiges Material (304 statt 316L) | 20 % |
| 4 | Beschädigte Passivierung | 10 % |
| 5 | Fehlende Wartung/Reinigung | 10 % |

**Diagnose-Schritte:**
1. Mastbesteigung (Bosunsstuhl oder Mast legen)
2. Swivel visuell inspizieren — Korrosionstyp identifizieren
3. Swivel von Hand drehen — Leichtgängigkeit prüfen
4. Material identifizieren (Markierung, Magnettest: 316L = nicht magnetisch)
5. Halyard-Schäkel prüfen — sitzt er fest?

**Behebung:**
- Leichte Korrosion: Reinigung mit Edelstahl-Reiniger, Re-Passivierung (Citrussäure)
- Galvanische Korrosion: Kontaktflächen isolieren (Tef-Gel, Kunststoffscheibe)
- Starke Korrosion/Pittings: Swivel komplett tauschen
- Swivel-Kosten: 150–500 EUR (je nach Furler-Modell)

**Präventivmaßnahmen:**
- Jährliche Süßwasser-Spülung des Swivels bei Mastbesteigung
- Alle Metall-Kontaktflächen mit Tef-Gel isolieren
- Halyard-Schäkel aus identischem Material wie Swivel verwenden

**Kostenrahmen:** 30 EUR (Reinigung) / 50–100 EUR (Re-Passivierung + Isolierung) / 200–600 EUR (Swivel-Austausch)

---

### Fehlerbild F-15_04-08: Furling-Leine gerissen oder verschlissen

**Fehlerbild-ID:** F-15_04-08
**Bezeichnung:** Furling-Leine gerissen oder verschlissen (Furling Line Failure)
**Schweregrad:** 3 von 5
**Dringlichkeit:** Mittel bis Hoch — Furler nicht bedienbar

**Erscheinungsbild:**
- Furling-Leine gebrochen → Segel lässt sich nicht mehr furlen
- Starker Abrieb, Pilling, harte Stellen an der Leine
- Mantel-Kern-Trennung sichtbar
- Leine rutscht in der Klemme

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Alterung/UV-Degradation | 35 % |
| 2 | Mechanischer Abrieb an scharfen Kanten | 25 % |
| 3 | Überlastung (zu hohe Windlasten) | 15 % |
| 4 | Falsche Leinenstärke (zu dünn) | 10 % |
| 5 | Klemmen-Verschleiß (Leine wird gequetscht) | 10 % |
| 6 | Chemische Degradation (Kraftstoff, Reiniger) | 5 % |

**Diagnose-Schritte:**
1. Bruchstelle analysieren: Glatter Schnitt → mechanischer Abrieb. Faserig → Überlastung/Alterung
2. Gesamte Leine auf Verschleiß prüfen: alle 50 cm zwischen Fingern durchziehen
3. Leinenführung auf scharfe Kanten prüfen (Umlenkrollen, Klemmen, Durchführungen)
4. Klemmen-Zustand prüfen

**Behebung (auf See — Notfall):**
1. Ersatz-Furling-Leine einscheren (sollte immer an Bord sein!)
2. Falls keine Ersatzleine: Fall oder Schot als Notlösung verwenden
3. Provisorische Befestigung an der Drum mit Palstek

**Behebung (im Hafen):**
1. Neue Leine in korrekter Stärke einscheren (siehe Tabelle 5.2)
2. Scharfe Kanten an Leinenführung beseitigen
3. Klemmen bei Verschleiß tauschen
4. Leinenführungsblöcke auf freie Drehung prüfen

**Präventivmaßnahmen:**
- Leine alle 3–5 Jahre prophylaktisch tauschen
- Jährlich auf Verschleiß prüfen
- Immer Ersatzleine an Bord mitführen
- UV-exponierte Teile der Leine mit Schutzschlauch versehen

**Kostenrahmen:** 30–80 EUR (neue Leine) / 10–30 EUR (Leinenführungsblock) / 20–60 EUR (Klemme)

---

### Fehlerbild F-15_04-09: Vorstag-Spannung verloren

**Fehlerbild-ID:** F-15_04-09
**Bezeichnung:** Vorstag-Spannung verloren (Forestay Tension Loss)
**Schweregrad:** 5 von 5
**Dringlichkeit:** KRITISCH — Rigg-Sicherheit gefährdet

**Erscheinungsbild:**
- Vorstag hängt deutlich durch
- Furler dreht sich nicht mehr sauber (Profil knickt)
- Segel-Profil stark beeinträchtigt (Am-Wind-Leistung)
- Im Extremfall: Vorstag-Schwingung, Rigg-Instabilität

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Wantenspanner hat sich gelöst | 30 % |
| 2 | Stag-Streckung (Langzeit-Dehnung) | 25 % |
| 3 | Gebrochene Litzen im Vorstag | 20 % |
| 4 | Toggle/Gabelkopf-Verschleiß | 10 % |
| 5 | Mastfuß-/Deck-Problem | 10 % |
| 6 | Achterstag-Problem (Gegenspannung fehlt) | 5 % |

**Diagnose-Schritte:**
1. Wantenspanner prüfen → Hat sich das Gewinde gelöst?
2. Vorstag visuell inspizieren → Gebrochene Litzen? (ACHTUNG: Unter Profil oft nicht sichtbar!)
3. Toggle und Gabelkopf → Bolzen-Verschleiß, Spiel?
4. Achterstag-Spannung prüfen
5. Mastfuß-Bereich und Deck-Durchführung inspizieren
6. Rig-Tension messen (Loos-Gauge oder Professionelle Messung)

**Behebung:**
- Wantenspanner nachstellen: Kontermutter lösen, Spannung einstellen, Kontermutter sichern
- Bei Litzenbruch: SOFORTIGER STOPP. Vorstag tauschen lassen (Rigger)
- Toggle/Gabelkopf: Verschlissene Bolzen ersetzen
- Vorstag-Austausch: 400–1.800 EUR (je nach Durchmesser und Länge)

**Präventivmaßnahmen:**
- Wantenspanner regelmäßig prüfen und Kontermutter nachziehen
- Vorstag alle 10 Jahre tauschen (auch ohne sichtbaren Defekt)
- Jährliche Rig-Inspektion durch qualifizierten Rigger
- Bei Furler-Systemen: Vorstag unter Profil alle 10 Jahre röntgen oder ersetzen

**Kostenrahmen:** 0 EUR (Wantenspanner nachstellen) / 100–300 EUR (Toggle/Bolzen) / 500–2.500 EUR (Vorstag-Austausch)

---

### Fehlerbild F-15_04-10: UV-Schutzstreifen defekt

**Fehlerbild-ID:** F-15_04-10
**Bezeichnung:** UV-Schutzstreifen defekt (UV Strip Damage)
**Schweregrad:** 2 von 5
**Dringlichkeit:** Niedrig — langfristiger Segelschaden

**Erscheinungsbild:**
- UV-Schutzstreifen ausgeblichen, dünn oder fehlend
- Nähte lösen sich
- Stoff-Risse im Schutzstreifen
- Durchscheinen des Segeltuchs unter dem Streifen

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Natürliche UV-Alterung | 50 % |
| 2 | Minderwertige Qualität des Streifens | 20 % |
| 3 | Mechanische Beschädigung (Scheuern) | 15 % |
| 4 | Nähte mit nicht-UV-beständigem Garn | 10 % |
| 5 | Falsches Waschmittel/Reiniger | 5 % |

**Diagnose-Schritte:**
1. Segel vollständig ausrollen und UV-Streifen auf gesamter Länge inspizieren
2. Reißfestigkeit prüfen: vorsichtig am Streifen ziehen
3. Nähte prüfen: lösen sich Stiche?
4. Farbvergleich: original-Farbe vs. aktueller Zustand

**Behebung:**
- Leichte Abnutzung: UV-Schutzspray als Überbrückung (z.B. 303 Fabric Guard)
- Lose Nähte: Segelmacher reparieren lassen (50–150 EUR)
- Streifenaustausch: Segelmacher → neuen Sunbrella-Streifen aufnähen (300–600 EUR je nach Segelgröße)
- Alternativ: UV-Schutz-Folie (weniger haltbar, aber schnelle Lösung)

**Präventivmaßnahmen:**
- UV-Schutzstreifen alle 5 Jahre prüfen (Mittelmeer), alle 8 Jahre (Nordeuropa)
- 303 Fabric Guard halbjährlich auftragen
- Segel bei Langzeitliegezeit vollständig furlen → Streifenbelastung minimieren
- Hochwertiges Sunbrella-Tuch für den Streifen verwenden (nicht Billig-Acryl)

**Kostenrahmen:** 20 EUR (UV-Spray) / 50–150 EUR (Naht-Reparatur) / 300–600 EUR (Streifenaustausch)

---

### Fehlerbild F-15_04-11: Elektrischer Furler-Antrieb Ausfall

**Fehlerbild-ID:** F-15_04-11
**Bezeichnung:** Elektrischer Furler-Antrieb Ausfall (Electric Furler Motor Failure)
**Schweregrad:** 3 von 5
**Dringlichkeit:** Mittel — manuelles Backup verfügbar

**Erscheinungsbild:**
- Motor reagiert nicht auf Schalter/Fernbedienung
- Motor dreht, aber Furler bewegt sich nicht
- Motor läuft nur in eine Richtung
- Ungewöhnliche Geräusche vom Motor
- Sicherung fällt wiederholt aus

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Elektrischer Defekt (Kabel, Stecker, Korrosion) | 30 % |
| 2 | Sicherung/Schutzschalter ausgelöst | 20 % |
| 3 | Motor-Verschleiß (Kohlebürsten) | 15 % |
| 4 | Getriebe-Schaden | 10 % |
| 5 | Steuerung/Relais defekt | 10 % |
| 6 | Batterie-Spannung zu niedrig | 10 % |
| 7 | Feuchtigkeitsschaden im Motor | 5 % |

**Diagnose-Schritte:**
1. Sicherung prüfen → Durchgebrannt? → Ersetzen und beobachten
2. Batteriespannung messen → >12,0 V? (bei Last)
3. Spannung am Motor messen → Kommt Strom an?
4. Kabelverbindungen und Stecker prüfen → Korrosion? Lose?
5. Motor-Strom messen → Überstrom = mechanische Blockade
6. Getriebe prüfen → Spiel, Geräusche?

**Behebung:**
- Sicherung: Ersetzen durch korrekte Ampere-Stärke (z.B. Facnor FX+e: 60A)
- Kabelkorrosion: Stecker reinigen, Kontaktspray, ggf. neu crimpen
- Motor-Bürsten: Austausch durch Fachbetrieb (150–300 EUR)
- Getriebe: Reparatur oder Austausch (300–800 EUR)
- Steuerung: Relais/Solenoid tauschen (80–200 EUR)
- Motor komplett: 800–2.500 EUR (Facnor FX+e, Selden GXe, Reckmann)

**Relevante Systeme:**
- Facnor FX+e: 12V/24V DC-Motor, 60A Sicherung, Fernbedienung
- Selden GXe: 12V/24V DC-Motor, 50A Sicherung, Kabelfernbedienung
- Reckmann: 24V DC oder 230V AC, variable Sicherung, SPS-Steuerung
- Bamar V-Serie: 24V DC, elektronische Steuerung mit Endschaltern

**Präventivmaßnahmen:**
- Motor-Service alle 2 Jahre (Bürsten, Getriebe-Fett, Dichtungen)
- Kabelverbindungen jährlich auf Korrosion prüfen
- Motorspeisekabel auf korrekte Dimensionierung prüfen (Spannungsabfall <5 %)
- Manuelle Backup-Prozedur kennen und üben!

**Kostenrahmen:** 5 EUR (Sicherung) / 50–200 EUR (elektrische Reparatur) / 300–800 EUR (Getriebe) / 800–2.500 EUR (Motor)

---

### Fehlerbild F-15_04-12: Hydraulischer Furler — Leckage und Druckverlust

**Fehlerbild-ID:** F-15_04-12
**Bezeichnung:** Hydraulischer Furler — Leckage und Druckverlust (Hydraulic Furler Leak and Pressure Loss)
**Schweregrad:** 4 von 5
**Dringlichkeit:** Hoch — System nicht voll funktionsfähig

**Erscheinungsbild:**
- Ölflecken am Mastfuß oder Deck
- Furler reagiert langsam oder unvollständig
- Druckanzeige zeigt Abfall
- Hydraulikpumpe läuft dauerhaft nach
- Schaum im Hydrauliköl-Reservoir

**Ursachen (nach Häufigkeit):**

| Rang | Ursache | Wahrscheinlichkeit |
|---|---|---|
| 1 | Dichtungsversagen am Zylinder | 30 % |
| 2 | Undichte Verschraubung/Fitting | 25 % |
| 3 | Schlauch-Leckage (Alterung, Abrieb) | 20 % |
| 4 | Pumpen-Verschleiß | 10 % |
| 5 | Luft im System (nach Service) | 10 % |
| 6 | Hydrauliköl-Degradation | 5 % |

**Diagnose-Schritte:**
1. Leckage-Stelle lokalisieren (Papiertuch unter Fittings legen)
2. Hydrauliköl-Stand und -Zustand prüfen (Farbe, Schaum, Verschmutzung)
3. Systemdruck messen → Herstellervorgabe (typisch: 100–250 bar)
4. Pumpenlaufzeit messen → >30 Sek. für eine Umdrehung = Leckage
5. Schläuche visuell prüfen → Risse, Ausbauchungen, Scheuerstellen?

**Behebung:**
- Undichte Fittings: Nachziehen (Drehmoment beachten!), ggf. O-Ring tauschen
- Dichtungsaustausch am Zylinder: Dichtungssatz des Herstellers (50–200 EUR)
- Schlauch-Austausch: Marine-Hydraulikschlauch mit korrekten Anschlüssen (100–300 EUR)
- Entlüften: System nach jedem Eingriff vollständig entlüften
- Ölwechsel: Empfohlen alle 3–5 Jahre (ATF Dexron III oder Herstellervorgabe)

**Relevante Systeme:**
- Reckmann Hydraulik-Furler: 200–250 bar, HLP-46 Hydrauliköl
- Bamar V-Serie Hydraulik: 150–200 bar, ATF Dexron III
- Profurl Hydraulic: 100–180 bar, HLP-32 Hydrauliköl

**Präventivmaßnahmen:**
- Hydrauliköl-Stand monatlich prüfen
- Ölwechsel alle 3 Jahre oder 500 Betriebsstunden
- Schläuche alle 5 Jahre tauschen (auch ohne sichtbaren Defekt)
- Dichtungen alle 5 Jahre prophylaktisch erneuern
- Fittings mit Drehmomentschlüssel nachziehen (jährlich)

> ⚠️ **ZU PRÜFEN (Audit):** Ölwechsel-Intervall „500 Betriebsstunden" (hier, F-15_04-12) vs. „2.000 Betriebsstunden" (S.19.2) vs. „alle 3–5 Jahre" (Behebung oben) — widersprüchliche Angaben zum selben Wartungsschritt. 500 h entspricht dem Ölfilter-Intervall (S.19.2) und ist vermutlich damit verwechselt. Verbindlich ist die Herstellervorgabe; die Stunden-Angabe hier ist nicht gesichert.

**Kostenrahmen:** 50–200 EUR (Dichtungssatz) / 100–300 EUR (Schlauch) / 200–500 EUR (Pumpe) / 50–100 EUR (Ölwechsel)

---

## 9. Troubleshooting-Entscheidungsbäume

### TB-15_04-01: "Furler lässt sich nicht ein-/ausrollen"

```
START: Furler lässt sich nicht ein-/ausrollen
│
├─ Schritt 1: Ist die Furling-Leine intakt?
│  ├─ NEIN → Leine gerissen
│  │  └─ Notleine einscheren → See: Halyard lösen, Segel bergen
│  │     └─ Hafen: Neue Leine gemäß Herstellervorgabe (Kap. 5.2)
│  │
│  └─ JA → Weiter mit Schritt 2
│
├─ Schritt 2: Furling-Leine unter Zug — blockiert oder durchrutschend?
│  ├─ BLOCKIERT → Mechanische Blockade
│  │  ├─ Schritt 2a: Ist die Blockade an der Trommel?
│  │  │  ├─ JA → Überwerfer in der Drum, Leine verklemmt
│  │  │  │  └─ Leine abwickeln, Überwerfer korrigieren (Kap. 5.2)
│  │  │  └─ NEIN → Weiter mit Schritt 2b
│  │  │
│  │  ├─ Schritt 2b: Ist die Blockade am Profil?
│  │  │  ├─ JA → Segel klemmt im Profil
│  │  │  │  └─ Halyard lösen, Segel vorsichtig bewegen → F-15_04-04
│  │  │  └─ NEIN → Weiter mit Schritt 2c
│  │  │
│  │  └─ Schritt 2c: Ist die Blockade am Halyard-Swivel?
│  │     ├─ JA → Swivel blockiert (Lager defekt, Korrosion)
│  │     │  └─ Mastbesteigung, Swivel-Inspektion → F-15_04-07
│  │     └─ NEIN → Komplette Systemprüfung erforderlich (Rigger)
│  │
│  └─ DURCHRUTSCHEND → Leine rutscht auf Trommel
│     └─ Leinenstärke prüfen, Drum-Zustand prüfen → F-15_04-05
│
├─ Schritt 3: Furler dreht schwer aber nicht blockiert?
│  ├─ JA → Schwergängig
│  │  ├─ Schritt 3a: Ohne Segel auch schwergängig?
│  │  │  ├─ JA → Lager-Problem → F-15_04-01
│  │  │  └─ NEIN → Profil-Problem → Kanal reinigen (Kap. 6.4)
│  │  └─ ENDE
│  │
│  └─ NEIN → Weiter mit Schritt 4
│
└─ Schritt 4: Wind zu stark für Furling?
   ├─ JA → Windlast zu hoch
   │  └─ Schot dichter → Segel fieren → dann furlen. Notfalls: anluvend furlen
   └─ NEIN → Systemfehler unklar → Professionelle Inspektion empfohlen
```

---

### TB-15_04-02: "Ungewöhnliche Geräusche beim Furling"

```
START: Ungewöhnliche Geräusche beim Furling
│
├─ Schritt 1: Art des Geräuschs identifizieren
│  ├─ KRATZEN/KNIRSCHEN → Lager-Problem
│  │  ├─ Geräusch von unten (Drum)?
│  │  │  ├─ JA → Drum-Lager defekt/verschmutzt
│  │  │  │  └─ Schmierung versuchen → Bei Persistenz: Lager tauschen (Kap. 4)
│  │  │  └─ NEIN → Von oben (Swivel)?
│  │  │     └─ JA → Swivel-Lager defekt → Mastbesteigung, Inspektion
│  │  └─ ENDE
│  │
│  ├─ KLAPPERN/KLACKERN → Lose Teile
│  │  ├─ Bei bestimmter Profil-Position?
│  │  │  ├─ JA → Lose Profilverbindung → F-15_04-06
│  │  │  └─ NEIN → Bei jeder Umdrehung?
│  │  │     ├─ JA → Loser Sicherungsring, Bolzen oder Schäkel
│  │  │     │  └─ Alle Befestigungen prüfen und nachziehen
│  │  │     └─ NEIN → Intermittierend → Leine schlägt gegen Profil
│  │  │        └─ Leinenführung prüfen und korrigieren
│  │  └─ ENDE
│  │
│  ├─ QUIETSCHEN → Trockene Reibung
│  │  ├─ Am Drum-Bereich?
│  │  │  ├─ JA → Drum-Lager trocken → Schmierung (McLube OneDrop)
│  │  │  └─ NEIN → Am Profil?
│  │  │     └─ JA → Luff-Tape reibt trocken im Kanal
│  │  │        └─ McLube SailKote auf Kanal und Luff-Tape
│  │  └─ ENDE
│  │
│  ├─ SUMMEN/VIBRIEREN → Resonanz
│  │  └─ Tritt nur bei bestimmter Windgeschwindigkeit auf?
│  │     ├─ JA → Windinduzierte Vibration → Normal bei 10–20 kn
│  │     │  └─ Bei starker Vibration: Vorstag-Spannung erhöhen
│  │     └─ NEIN → Motor-Geräusch (bei elektrischem Furler)
│  │        └─ Motor-Inspektion → F-15_04-11
│  │
│  └─ KNALL/SCHLAG → Sofort stoppen!
│     └─ Furling sofort unterbrechen!
│        ├─ Gebrochene Profilverbindung? → F-15_04-06
│        ├─ Vorstag-Litzen gebrochen? → F-15_04-09 → RIGGER!
│        └─ Halyard-Schäkel gebrochen? → Segel sichern, Hafen anlaufen
│
└─ ENDE: Bei Unsicherheit → Professionelle Inspektion
```

---

### TB-15_04-03: "Segel kommt nicht vollständig heraus"

```
START: Segel kommt nicht vollständig heraus (entrollen)
│
├─ Schritt 1: Wie weit kommt das Segel heraus?
│  ├─ GAR NICHT → Totale Blockade
│  │  ├─ Halyard angeschlagen und gespannt?
│  │  │  ├─ NEIN → Halyard anschlagen/spannen
│  │  │  └─ JA → Furling-Leine blockiert die Drum?
│  │  │     ├─ JA → Leine aus Klemme lösen, Drum freidrehen
│  │  │     └─ NEIN → Segel im Profil eingeklemmt → F-15_04-04
│  │  └─ ENDE
│  │
│  ├─ TEILWEISE (stoppt an bestimmter Stelle) → Lokale Blockade
│  │  ├─ Position der Blockade bestimmen
│  │  │  ├─ An Profilverbindung → Verbindung versetzt → F-15_04-06
│  │  │  ├─ Am Luff-Tape → Tape beschädigt/aufgeplustert
│  │  │  │  └─ Tape vorsichtig glätten, Segelmacher konsultieren
│  │  │  └─ Am oberen Ende → Halyard-Swivel-Problem
│  │  │     └─ Swivel prüfen, ggf. Mastbesteigung
│  │  └─ ENDE
│  │
│  └─ FAST VOLLSTÄNDIG (letzten 10-20% klemmen) → Endbereich-Problem
│     ├─ Halyard-Spannung ausreichend?
│     │  ├─ NEIN → Halyard nachspannen → Hersteller-Vorgabe
│     │  └─ JA → Wind reicht nicht zum Entrollen?
│     │     ├─ JA → Bei Leichtwind: Schot einholen, Kurswechsel
│     │     └─ NEIN → Profil-Kanal am oberen Ende blockiert
│     │        └─ Reinigung erforderlich → Kap. 6.4
│     └─ ENDE
│
└─ ENDE: Bei wiederkehrendem Problem → Systematische Profil-Inspektion
```

---

### TB-15_04-04: "Elektrischer/Hydraulischer Antrieb reagiert nicht"

```
START: Elektrischer oder Hydraulischer Antrieb reagiert nicht
│
├─ Schritt 1: Welcher Antriebstyp?
│  ├─ ELEKTRISCH → Weiter mit Elektrik-Diagnose
│  │  ├─ Schritt E1: Sicherung prüfen
│  │  │  ├─ DURCHGEBRANNT → Sicherung ersetzen (korrekte Stärke!)
│  │  │  │  ├─ Fällt erneut? → JA → Kurzschluss oder Motorblockade
│  │  │  │  │  ├─ Kabel auf Scheuerstellen prüfen
│  │  │  │  │  ├─ Motor auf Blockade prüfen (manuell drehen)
│  │  │  │  │  └─ Elektriker/Fachbetrieb
│  │  │  │  └─ Fällt nicht erneut → OK, beobachten
│  │  │  └─ INTAKT → Weiter mit Schritt E2
│  │  │
│  │  ├─ Schritt E2: Batteriespannung prüfen
│  │  │  ├─ <11,5V (12V-System) → Batterie laden/ersetzen
│  │  │  └─ >12,0V → Weiter mit Schritt E3
│  │  │
│  │  ├─ Schritt E3: Spannung am Motor-Stecker messen
│  │  │  ├─ KEINE SPANNUNG → Kabel-/Steckerdefekt, Relais defekt
│  │  │  │  └─ Kabelweg verfolgen, Stecker reinigen, Relais prüfen
│  │  │  └─ SPANNUNG VORHANDEN → Motor-Defekt
│  │  │     ├─ Motor surrt aber dreht nicht → Bürsten verschlissen
│  │  │     ├─ Motor stumm → Wicklung defekt
│  │  │     └─ Motor dreht aber Furler nicht → Getriebe/Kupplung defekt
│  │  └─ ENDE
│  │
│  └─ HYDRAULISCH → Weiter mit Hydraulik-Diagnose
│     ├─ Schritt H1: Pumpe prüfen
│     │  ├─ Pumpe läuft nicht → Elektrische Versorgung prüfen (wie oben E1-E3)
│     │  └─ Pumpe läuft → Weiter mit Schritt H2
│     │
│     ├─ Schritt H2: Ölstand prüfen
│     │  ├─ NIEDRIG → Öl nachfüllen, Leckage suchen → F-15_04-12
│     │  └─ OK → Weiter mit Schritt H3
│     │
│     ├─ Schritt H3: Druck prüfen (Manometer)
│     │  ├─ KEIN DRUCK → Pumpe defekt oder Überdruckventil offen
│     │  ├─ DRUCK NIEDRIG → Interne Leckage (Zylinder-Dichtung)
│     │  └─ DRUCK OK → Ventil-Steuerung defekt (Solenoid, Wegeventil)
│     └─ ENDE
│
├─ Schritt 2: IMMER → Manuelles Backup aktivieren!
│  ├─ Elektrischer Furler: Notkurbel oder Furling-Leine verwenden
│  └─ Hydraulischer Furler: Manuelles Bypassventil öffnen → Handpumpe nutzen
│
└─ ENDE: Bei Motor-/Pumpendefekt → Fachbetrieb
```

---

### TB-15_04-05: "Vorstag-Spannung ungenügend nach Furler-Service"

```
START: Vorstag-Spannung ungenügend nach Furler-Service
│
├─ Schritt 1: Wurde das Vorstag beim Service getrennt?
│  ├─ JA → Weiter mit Schritt 2
│  └─ NEIN → Spannung war vorher OK?
│     ├─ JA → Service hat etwas verändert
│     │  ├─ Profil falsch zusammengebaut? (Sektion fehlt/doppelt?)
│     │  ├─ Distanzstück vergessen? (Drum oder Swivel)
│     │  └─ Toggle falsch montiert?
│     └─ NEIN → Vorbestehendes Problem → F-15_04-09
│
├─ Schritt 2: Vorstag-Terminal korrekt angeschlossen?
│  ├─ Gabelkopf/Toggle → Bolzen korrekt eingesetzt, Splint vorhanden?
│  │  ├─ NEIN → Korrekt montieren
│  │  └─ JA → Weiter mit Schritt 3
│  └─ ENDE
│
├─ Schritt 3: Wantenspanner korrekt eingestellt?
│  ├─ NEIN → Wantenspanner auf korrekte Vorstag-Spannung einstellen
│  │  ├─ Richtwert Vorstag-Spannung:
│  │  │  ├─ 8-10 m Segelboot: 15-20 % Bruchlast des Vorstags
│  │  │  ├─ 10-14 m Segelboot: 20-25 % Bruchlast
│  │  │  └─ >14 m Segelboot: 25-30 % Bruchlast (Rigger konsultieren)
│  │  └─ Kontermutter nach Einstellung sichern!
│  └─ JA → Weiter mit Schritt 4
│
├─ Schritt 4: Achterstag-Spannung prüfen
│  ├─ ZU NIEDRIG → Achterstag spannen (Vorstag-Spannung steigt mit)
│  └─ OK → Weiter mit Schritt 5
│
├─ Schritt 5: Hat sich das Vorstag gelängt?
│  ├─ Alter >10 Jahre → Wahrscheinlich Stag-Streckung → Vorstag tauschen
│  └─ Alter <10 Jahre → Unwahrscheinlich → weitere Diagnose
│     ├─ Mastfuß-Position prüfen (hat sich Mast bewegt?)
│     ├─ Decksdurchführungen prüfen (Pütting-Bolzen)
│     └─ Wanten prüfen (Seitenwanten ebenfalls korrekt?)
│
└─ ENDE: Bei Unsicherheit → Qualifizierter Rigger für Rig-Tune
   └─ Kosten Rig-Tune: 300-600 EUR (inkl. Messung und Einstellung)
```

---

## 10. Saisonale Wartungsprotokolle

### 10.1 Frühjahrs-Inbetriebnahme (Spring Commissioning)

**Zeitpunkt:** 2–4 Wochen vor erstem Segeltörn der Saison

#### Protokoll-Checkliste Frühjahr

| Nr. | Arbeitsschritt | Erledigt | Befund | Maßnahme | Unterschrift |
|---|---|---|---|---|---|
| F-01 | Winterabdeckung entfernen | ☐ | | | |
| F-02 | Sichtprüfung Gesamtsystem (Drum, Profil, Swivel) | ☐ | | | |
| F-03 | Drum-Abdeckung öffnen, Innenleben inspizieren | ☐ | | | |
| F-04 | Unteres Lager: Handprüfung (Spiel, Drehung, Geräusch) | ☐ | | | |
| F-05 | Unteres Lager: Schmierung (McLube OneDrop, 3 Tropfen) | ☐ | | | |
| F-06 | Drum-Dichtungen/O-Ringe: Sichtprüfung | ☐ | | | |
| F-07 | Drum-Abdeckung schließen (Drehmoment beachten) | ☐ | | | |
| F-08 | Profilverbindungen: alle einzeln auf festen Sitz prüfen | ☐ | | | |
| F-09 | Profil-Geradheit: von achtern visieren | ☐ | | | |
| F-10 | Profil-Kanal: Reinigung mit McLube SailKote | ☐ | | | |
| F-11 | Halyard-Swivel: Sichtprüfung (Fernglas/Mastbesteigung) | ☐ | | | |
| F-12 | Halyard-Swivel: Schmierung (bei Mastbesteigung) | ☐ | | | |
| F-13 | Vorstag: Sichtprüfung sichtbarer Bereiche | ☐ | | | |
| F-14 | Vorstag-Spannung: Messung (Loos-Gauge oder subjektiv) | ☐ | | | |
| F-15 | Toggle/Gabelkopf: Bolzen und Splinte prüfen | ☐ | | | |
| F-16 | Furling-Leine: Zustandsprüfung gesamte Länge | ☐ | | | |
| F-17 | Furling-Leine einscheren (korrekte Wickelrichtung!) | ☐ | | | |
| F-18 | Segel anschlagen (Luff-Tape in Kanal einführen) | ☐ | | | |
| F-19 | UV-Schutzstreifen: Gesamtlänge prüfen | ☐ | | | |
| F-20 | Funktionstest: 3x komplett furlen/unfurlen | ☐ | | | |
| F-21 | Geräuschprüfung während Funktionstest | ☐ | | | |
| F-22 | Drum-Cover aufsetzen (falls verwendet) | ☐ | | | |

**Datum:** ________________
**Durchgeführt von:** ________________
**Nächste Wartung fällig:** ________________

### 10.2 Sommer-Zwischenkontrolle

**Zeitpunkt:** Mitte der Saison (Juli/August in Nordeuropa)

#### Protokoll-Checkliste Sommer

| Nr. | Arbeitsschritt | Erledigt | Befund | Maßnahme |
|---|---|---|---|---|
| S-01 | Furling-Leichtgängigkeit prüfen (subjektiv: besser/gleich/schlechter als Saisonstart?) | ☐ | | |
| S-02 | Drum-Bereich: Salzablagerungen → Süßwasser-Spülung | ☐ | | |
| S-03 | Lager-Nachschmierung (McLube OneDrop, 2 Tropfen) | ☐ | | |
| S-04 | Profilverbindungen: Stichprobe (jede 3. prüfen) | ☐ | | |
| S-05 | Furling-Leine: Verschleißprüfung | ☐ | | |
| S-06 | UV-Schutzstreifen: Kurzprüfung oberes/unteres Drittel | ☐ | | |
| S-07 | Steckbolzen und Splinte: Vollständigkeit | ☐ | | |
| S-08 | Funktionstest: 1x komplett furlen/unfurlen | ☐ | | |

**Zeitaufwand:** 20–30 Minuten
**Datum:** ________________
**Durchgeführt von:** ________________

### 10.3 Herbst-Einwinterung (Winterization)

**Zeitpunkt:** Innerhalb von 2 Wochen nach letztem Segeltörn

#### Protokoll-Checkliste Herbst

| Nr. | Arbeitsschritt | Erledigt | Befund | Maßnahme | Unterschrift |
|---|---|---|---|---|---|
| H-01 | Segel abschlagen: Luff-Tape vorsichtig aus Profil ziehen | ☐ | | | |
| H-02 | Segel: Zustand dokumentieren, Waschbedarf? | ☐ | | | |
| H-03 | Süßwasser-Spülung: Gesamtes Furler-System (Schlauch) | ☐ | | | |
| H-04 | Drum öffnen: Innenleben inspizieren, Befund notieren | ☐ | | | |
| H-05 | Unteres Lager: Detailprüfung (Spiel, Geräusch, Zustand) | ☐ | | | |
| H-06 | Drum-Dichtungen: Zustand bewerten (Tausch nötig?) | ☐ | | | |
| H-07 | Lager-Konservierung: Schmierung mit McLube OneDrop | ☐ | | | |
| H-08 | Drum schließen, Schrauben mit Tef-Gel | ☐ | | | |
| H-09 | Profil-Inspektion: alle Sektionen einzeln, Verbindungen | ☐ | | | |
| H-10 | Profil-Kanal: Reinigung nach Saisonende | ☐ | | | |
| H-11 | Profil-Konservierung: Wachs oder McLube SailKote | ☐ | | | |
| H-12 | Halyard-Swivel: Inspektion (bei Mastlegen) | ☐ | | | |
| H-13 | Vorstag sichtbare Bereiche: Inspektion | ☐ | | | |
| H-14 | Toggle/Gabelkopf: Inspektion, Bolzen-Verschleiß messen | ☐ | | | |
| H-15 | Furling-Leine: entfernen, waschen, trocknen | ☐ | | | |
| H-16 | Furling-Leine: Zustandsbewertung (weiter verwenden?) | ☐ | | | |
| H-17 | Kunststoffteile: UV-Zustand bewerten | ☐ | | | |
| H-18 | Winterabdeckung: Drum und Profil abdecken (atmungsaktiv!) | ☐ | | | |
| H-19 | Winterarbeiten-Liste erstellen | ☐ | | | |
| H-20 | Wartungsbericht dokumentieren und ablegen | ☐ | | | |

**Datum:** ________________
**Durchgeführt von:** ________________
**Identifizierte Winterarbeiten:** ________________

### 10.4 Winter-Lagerung und Off-Season-Service

**Empfohlene Winterarbeiten (während der Lagerung durchführen):**

| Priorität | Arbeit | Typische Kosten (DIY) | Typische Kosten (Fachbetrieb) |
|---|---|---|---|
| HOCH | Lageraustausch (falls bei H-05 festgestellt) | 65–155 EUR | 250–450 EUR |
| HOCH | Vorstag-Inspektion (falls >8 Jahre alt) | 0 EUR (visuell) | 150–300 EUR (professionell) |
| MITTEL | Profil-Verbindungsstücke tauschen (falls nötig) | 30–100 EUR | 150–300 EUR |
| MITTEL | Furling-Leine erneuern (falls >3 Jahre) | 30–80 EUR | 80–150 EUR |
| NIEDRIG | UV-Schutzstreifen erneuern | 300–600 EUR (Segelmacher) | — |
| NIEDRIG | Drum-Cover erneuern | 30–60 EUR | — |

**Winter-Lagerung des Furler-Systems:**
- Profil mit atmungsaktiver Plane abdecken (KEIN Plastik → Kondenswasser!)
- Drum-Abdeckung dicht schließen oder zusätzlich abdecken
- Furling-Leine gewaschen und trocken lagern (NICHT auf der Trommel!)
- Segel gewaschen, getrocknet und trocken lagern (gerollt, nicht gefaltet)
- Bei stehendem Rigg: Vorstag-Spannung leicht reduzieren (10–15 % weniger)

---

## 11. Werkzeuge und Spezialwerkzeug

### 11.1 Standard-Werkzeugsatz für Furler-Wartung

| Werkzeug | Verwendung | Empfohlene Qualität | ca. Preis |
|---|---|---|---|
| Innensechskant-Satz (2–10 mm) | Drum-Schrauben, Befestiger | Wera Hex-Plus oder Bondhus | 20–35 EUR |
| Torx-Satz (T15–T40) | Profurl-Schrauben | Wera oder Wiha | 15–25 EUR |
| Maulschlüssel-Satz (8–24 mm) | Wantenspanner, Muttern | Stahlwille oder Gedore | 40–60 EUR |
| Ringschlüssel-Satz (8–24 mm) | Vorstag-Terminal | Stahlwille oder Gedore | 40–60 EUR |
| Drehmomentschlüssel (2–25 Nm) | Alle kritischen Verschraubungen | Hazet 5107-3CT oder Stahlwille 730/2 | 80–120 EUR |
| Seeger-Ringzange (innen/außen) | Sicherungsringe Drum-Lager | Knipex 44 11 / 46 11 | 25–40 EUR |
| Spitzzange, lang | Splinte, Kleinteile | Knipex 25 06 160 | 20–30 EUR |
| Seitenschneider | Splinte, Kabelbinder | Knipex 70 02 160 | 15–25 EUR |
| Hakenschlüssel (verstellbar) | Harken Locking Ring | Gedore 36 0-100 | 30–45 EUR |
| Federwaage (0–10 kg) | Drehwiderstand-Messung | Pesola Medio | 25–35 EUR |
| Fühllehre (0,05–1,0 mm) | Lagerspiel, Profil-Spalte | Standardqualität | 8–12 EUR |
| Taschenlampe (stark) | Inspektion dunkler Bereiche | LED Lenser P7R | 30–50 EUR |
| Fernglas (8x oder 10x) | Swivel-Inspektion von Deck | Standardqualität | 50–100 EUR |
| Drahtbürste (Edelstahl, fein) | Reinigung von Korrosion | Standardqualität | 5–8 EUR |
| Scotch-Brite (fein, grün) | Profil-Reinigung | 3M Standard | 3–5 EUR |
| Bremsenreiniger | Lager-Reinigung | Standardqualität (Dose) | 5–8 EUR |
| Fusselfreie Lappen | Reinigung und Trocknung | Mikrofaser | 5–10 EUR |
| Kabelbinder (diverse) | Provisorische Sicherung | UV-beständig! | 5–10 EUR |

**Gesamtkosten Standard-Werkzeugsatz:** 450–700 EUR (einmalige Investition)

### 11.2 Spezialwerkzeuge nach Hersteller

#### 11.2.1 Selden/Furlex Spezialwerkzeug

| Werkzeug | Art.-Nr. | Verwendung | ca. Preis |
|---|---|---|---|
| Furlex Bearing Press 200 | 507-899-01 | Lager ein-/auspressen Furlex 200S | 45 EUR |
| Furlex Bearing Press 300 | 507-899-02 | Lager ein-/auspressen Furlex 300S | 55 EUR |
| Furlex Bearing Press 400 | 507-899-03 | Lager ein-/auspressen Furlex 400S | 65 EUR |
| Foil Assembly Tool | 507-895 | Profil-Montage und Kanal-Reinigung | 35 EUR |
| Furlex Service Tool Kit | 507-890 | Komplettes Kit für alle Furlex-Modelle | 120 EUR |

#### 11.2.2 Profurl Spezialwerkzeug

| Werkzeug | Art.-Nr. | Verwendung | ca. Preis |
|---|---|---|---|
| NEX Assembly Tool | TOOL-NEX | Profil-Verbindungsmontage NEX-Serie | 30 EUR |
| C-Serie Bearing Tool | TOOL-CBRG | Lager-Austausch C-Serie | 40 EUR |
| Foil Cleaner Rod | TOOL-FCR | Profil-Kanal-Reinigung (alle Serien) | 25 EUR |

#### 11.2.3 Harken Spezialwerkzeug

| Werkzeug | Art.-Nr. | Verwendung | ca. Preis |
|---|---|---|---|
| MKIV Bearing Press | BK4590 | Lager-Austausch MKIV (alle Units) | 75 EUR |
| MKIV Locking Ring Wrench | BK4591 | Drum-Locking Ring lösen/anziehen | 40 EUR |
| Furler Assembly Tool Kit | BK4595 | Komplettes Montage-Kit MKIV | 150 EUR |

#### 11.2.4 Facnor Spezialwerkzeug

| Werkzeug | Art.-Nr. | Verwendung | ca. Preis |
|---|---|---|---|
| FX+ Bearing Set Tool | TOOL-FX-BRG | Lager-Austausch FX+ Serie | 50 EUR |
| FX+ Assembly Tool | TOOL-FX-ASS | Profil- und Drum-Montage | 35 EUR |
| LS Foil Tool | TOOL-LS-FOIL | Profil-Montage LS-Serie | 30 EUR |

### 11.3 DIY vs. Professionell — Entscheidungshilfe

| Arbeit | DIY geeignet? | Begründung | Rigger empfohlen? |
|---|---|---|---|
| Schmierung (Lager, Profil) | JA | Einfach, kein Spezialwerkzeug | Nein |
| Drum öffnen/schließen | JA | Mit Anleitung machbar | Bei Unsicherheit |
| Lager-Austausch (Drum) | BEDINGT | Spezialwerkzeug erforderlich | Empfohlen beim ersten Mal |
| Profilverbindungen tauschen | JA | Einfach, logische Arbeit | Nein |
| Furling-Leine tauschen | JA | Einfach | Nein |
| Profil-Kanal reinigen | JA | Etwas aufwändig, aber machbar | Nein |
| Swivel-Lager tauschen | BEDINGT | Mastbesteigung erforderlich | JA |
| Vorstag-Inspektion unter Profil | NEIN | Professionelle Prüfmethoden nötig | JA |
| Vorstag-Austausch | NEIN | Rigg-Integrität, korrekte Längung | JA |
| 5-Jahres-Generalüberholung | BEDINGT | Zeitaufwändig, Erfahrung nötig | Empfohlen |
| 10-Jahres-Komplettrevision | NEIN | Umfangreich, sicherheitsrelevant | JA |
| Elektrischer Motor-Service | NEIN | Spezialwissen erforderlich | JA (Elektriker) |
| Hydraulik-Service | NEIN | Drucksystem, Spezialwissen | JA (Hydrauliker) |

### 11.4 Drehmoment-Spezifikationen

| Verschraubung | Furlex 200S | Furlex 300S | Furlex 400S | Profurl NEX | Harken MKIV | Facnor FX+ |
|---|---|---|---|---|---|---|
| Drum-Abdeckung | 3 Nm | 3 Nm | 4 Nm | 2,5 Nm | — | 3 Nm |
| Locking Ring | — | — | — | — | 5–15 Nm* | — |
| Drum-Basis | — | — | — | — | — | 5 Nm |
| Vorstag-Terminal | 20 Nm | 25 Nm | 30 Nm | 15–25 Nm | 20–30 Nm | 20–28 Nm |
| Profilverbindung | Handtest | Handtest | Handtest | Handtest | Handtest | Handtest |
| Toggle-Bolzen | 10 Nm | 12 Nm | 15 Nm | 10–15 Nm | 12–18 Nm | 10–15 Nm |

*Harken MKIV Locking Ring: Unit 0–1: 5 Nm, Unit 2: 8 Nm, Unit 3: 12 Nm, Unit 4: 15 Nm

---

## 12. Ersatzteil-Management

### 12.1 Empfohlene Bordersatzteile

**Für jede Yacht mit Rollreffanlage sollten folgende Ersatzteile an Bord sein:**

#### 12.1.1 Basis-Ersatzteile (Küstenfahrt)

| Teil | Menge | Grund | ca. Preis |
|---|---|---|---|
| Furling-Leine (Ersatz, komplette Länge) | 1 | Leinenriss = Furler unbedienbar | 30–80 EUR |
| O-Ringe für Drum (komplett) | 1 Satz | Dichtungswechsel unterwegs | 10–20 EUR |
| Sicherungssplinte (diverse) | 10 | Verlorene Splinte ersetzen | 5–10 EUR |
| Sicherungsringe (Seeger) | 4 | Für Drum-Lager | 5–10 EUR |
| Profilverbindungsstücke | 2 | Für Notfall-Reparatur | 25–50 EUR |
| Schäkel (passend für Halyard/Swivel) | 2 | Ersatz bei Verschleiß/Verlust | 10��20 EUR |
| Tef-Gel (kleine Tube) | 1 | Montage, Korrosionsschutz | 15 EUR |
| McLube OneDrop (28 ml) | 1 | Lager-Schmierung | 20 EUR |
| Selbstverschweißendes Tape | 1 Rolle | Notfall-Abdichtung | 8–12 EUR |
| Kabelbinder UV-beständig (diverse) | 20 | Provisorische Sicherung | 5 EUR |

**Gesamtkosten Basis-Kit:** 130–240 EUR

#### 12.1.2 Erweiterte Ersatzteile (Blauwasser/Langfahrt)

Zusätzlich zum Basis-Kit:

| Teil | Menge | Grund | ca. Preis |
|---|---|---|---|
| Komplett-Lagersatz (Drum + Swivel) | 1 | Lageraustausch fernab von Werft | 65��155 EUR |
| Drum-Dichtungssatz komplett | 1 | Drum-Service unterwegs | 20–40 EUR |
| Ersatz-Profilsektion (1,5 m) | 1 | Beschädigte Sektion ersetzen | 80–200 EUR |
| Vorstag-Terminal (passend) | 1 | Notfall-Reparatur | 50–100 EUR |
| McLube SailKote (300 ml) | 1 | Profil-Pflege | 25 EUR |
| Harken Winch Grease | 1 | Universal-Schmierfett | 18 EUR |
| Seeger-Ringzange (kompakt) | 1 | Lager-Demontage | 25 EUR |
| Drehmomentschlüssel (kompakt) | 1 | Korrekte Montage | 50–80 EUR |

**Gesamtkosten Erweitertes Kit:** 330–620 EUR (zusätzlich zum Basis-Kit)

### 12.2 Ersatzteil-Kits nach Hersteller und Modell

#### 12.2.1 Selden/Furlex Service Kits

| Kit | Inhalt | Art.-Nr. | ca. Preis |
|---|---|---|---|
| Furlex 200S Service Kit | 4 Lager, Dichtungen, Sicherungsringe, Anleitung | 507-955-01 | 85–120 EUR |
| Furlex 300S Service Kit | 4 Lager, Dichtungen, Sicherungsringe, Anleitung | 507-956-01 | 105–140 EUR |
| Furlex 400S Service Kit | 4 Lager, Dichtungen, Sicherungsringe, Anleitung | 507-957-01 | 130–170 EUR |
| Furlex 200S Drum Seal Kit | O-Ringe, Dichtungen | 507-950-01 | 25–35 EUR |
| Furlex 300S Drum Seal Kit | O-Ringe, Dichtungen | 507-951-01 | 30–40 EUR |
| Furlex Foil Connector Set (5 Stk.) | Profilverbindungen | 507-821-05 / -822-05 / -823-05 | 45–80 EUR |

#### 12.2.2 Profurl Service Kits

| Kit | Inhalt | Art.-Nr. | ca. Preis |
|---|---|---|---|
| NEX 1.0 Bearing Kit | 2 Lager, O-Ringe, Sicherungsring | KNEX-BEAR-10 | 75–95 EUR |
| NEX 2.0 Bearing Kit | 2 Lager, O-Ringe, Sicherungsring | KNEX-BEAR-20 | 85–110 EUR |
| C290 Bearing Kit | 2 Lager, Dichtungen | KC290-BEAR | 70–90 EUR |
| C430 Bearing Kit | 2 Lager, Dichtungen | KC430-BEAR | 90–115 EUR |
| NEX Seal Kit | O-Ringe, Dichtungen komplett | KNEX-SEAL | 20–30 EUR |
| NEX Foil Connector (5 Stk.) | Profilverbindungen | KNEX-CON-5 | 40–60 EUR |

#### 12.2.3 Harken Service Kits

| Kit | Inhalt | Art.-Nr. | ca. Preis |
|---|---|---|---|
| MKIV Unit 0 Bearing Kit | 3 Lager, Dichtungen | BK4515-0 | 65 EUR |
| MKIV Unit 1 Bearing Kit | 3 Lager, Dichtungen | BK4515-1 | 78 EUR |
| MKIV Unit 2 Bearing Kit | 3 Lager, Dichtungen | BK4515-2 | 95 EUR |
| MKIV Unit 3 Bearing Kit | 3 Lager, Dichtungen | BK4515-3 | 120 EUR |
| MKIV Unit 4 Bearing Kit | 3 Lager, Dichtungen | BK4515-4 | 155 EUR |
| MKIV Foil Connector Kit | Profilverbindungen (10 Stk.) | BK4520 | 60–90 EUR |

#### 12.2.4 Facnor Service Kits

| Kit | Inhalt | Art.-Nr. | ca. Preis |
|---|---|---|---|
| FX+ 1500 Bearing Kit | 2 Lager, Dichtungen | FX15-BRG | 70 EUR |
| FX+ 2500 Bearing Kit | 2 Lager, Dichtungen | FX25-BRG | 95 EUR |
| FX+ 3500 Bearing Kit | 2 Lager, Dichtungen | FX35-BRG | 125 EUR |
| LS 170 Bearing Kit | 2 Lager, Dichtungen | LS17-BRG | 80 EUR |
| LS 200 Bearing Kit | 2 Lager, Dichtungen | LS20-BRG | 110 EUR |
| FX+ Seal Kit (alle Modelle) | O-Ringe, Dichtungen | FX-SEAL | 25–35 EUR |

#### 12.2.5 Karver Service Kits

| Kit | Inhalt | Art.-Nr. | ca. Preis |
|---|---|---|---|
| KF3 Service Kit | Lager, Torlon-Buchse, O-Ringe | KF3-SRV | 55 EUR |
| KF4 Service Kit | Lager, Torlon-Buchse, O-Ringe | KF4-SRV | 65 EUR |
| KF5 Service Kit | Lager, Torlon-Buchse, O-Ringe | KF5-SRV | 80 EUR |
| KF7 Service Kit | Lager, Torlon-Buchse, O-Ringe | KF7-SRV | 110 EUR |
| KF8 Service Kit | Lager, Torlon-Buchse, O-Ringe | KF8-SRV | 145 EUR |

### 12.3 Bezugsquellen in Europa

| Händler | Land | Webshop | Stärken | Lieferzeit (DE) |
|---|---|---|---|---|
| SVB | DE | www.svb-marine.de | Größtes Sortiment DE, alle Hersteller | 1–3 Tage |
| Toplicht | DE | www.toplicht.de | Gute Beratung, Furler-Spezialisten | 1–3 Tage |
| Compass24 | DE | www.compass24.de | Breites Sortiment, gute Preise | 2–4 Tage |
| AWN | DE | www.awn.de | Breites Sortiment, Filialen | 1–3 Tage |
| 12° West | DE | www.12west.de | Premium-Segelzubehör, Regatta | 2–5 Tage |
| Furlex/Selden Direkt | SE | www.sfrurlex.com | Original-Ersatzteile Selden/Furlex | 5–10 Tage |
| Profurl Direkt | FR | www.profurl.com | Original-Ersatzteile Profurl | 5–10 Tage |
| Harken Direkt | IT (EU) | www.harken.com | Original-Ersatzteile Harken | 5–10 Tage |
| Facnor Direkt | FR | www.facnor.com | Original-Ersatzteile Facnor | 5–10 Tage |
| Pirates Cave | UK | www.piratescave.co.uk | Günstige Preise, großes Sortiment | 5–10 Tage |
| Force 4 Chandlery | UK | www.force4.co.uk | Marine-Spezialist UK | 5–10 Tage |
| Accastillage Diffusion | FR | www.accastillage-diffusion.com | Großes Sortiment, günstig | 5–10 Tage |

### 12.4 Lieferzeiten und Notfallbeschaffung

**Standard-Lieferzeiten:**
- Lagerware (SVB, Toplicht): 1–3 Werktage (DE)
- Herstellerbestellung: 5–15 Werktage
- Sonderanfertigung (ältere Modelle): 3–6 Wochen

**Notfall-Beschaffung (Boot liegt fest):**
1. **Express-Versand:** SVB bietet DHL-Express (nächster Werktag) gegen Aufpreis (ca. 15 EUR)
2. **Lokaler Rigger:** Viele Rigger haben Lager für gängige Modelle vorrätig
3. **Universal-Lager:** Standard-Industrielager (6003, 6004, 6005, 6006 in 2RS/Edelstahl) sind über Industriebedarf (z.B. SKF-Händler) oft innerhalb von 24 Stunden lieferbar
4. **3D-Druck:** Profilverbindungsstücke und Drum-Abdeckungen können im Notfall gedruckt werden (ABS oder PETG, nur als Provisorium!)
5. **Hersteller-Hotline:** Die meisten Hersteller haben eine Service-Hotline für Notfälle:
   - Selden: +46 31 69 69 00
   - Profurl: +33 2 97 87 65 00
   - Harken: +39 039 9000 775 (EU)
   - Facnor: +33 2 97 42 42 78

---

## 13. FAQ — Häufig gestellte Fragen

### FAQ 1: Wie oft muss ich meinen Furler warten?

**Antwort:** Mindestens zweimal pro Saison (Saisonstart und Saisonende), plus eine Zwischenkontrolle bei aktiver Nutzung. In Salzwasser-Revieren empfiehlt sich eine monatliche Kurzinspektion (5 Minuten) und eine halbjährliche Schmierung. Die Generalüberholung (komplett Demontage) erfolgt alle 5 Jahre. Siehe Kapitel 3 für detaillierte Intervalle.

### FAQ 2: Kann ich Standard-Industrielager statt Original-Herstellerlager verwenden?

**Antwort:** Ja, in den meisten Fällen ist das möglich und sinnvoll. Voraussetzung: Das Lager muss aus Edelstahl (AISI 440C oder 316L) sein, beidseitig abgedichtet (2RS-Suffix) und die identische Abmessung haben. Standard-Bezeichnungen (6003-2RS, 6004-2RS etc.) sind genormt. Kosten: 8–25 EUR pro Lager statt 30–50 EUR für Original-Teile. Siehe Kapitel 4.5 für Details.

### FAQ 3: Welches Schmiermittel soll ich verwenden?

**Antwort:** Für Kugellager: McLube OneDrop Ball Bearing Conditioner (Art. 0860) oder Harken Pawl Oil (Art. BK4521). Für den Profil-Kanal: McLube SailKote (Art. 0870). Für Gewinde und Metall-Kontaktflächen: Tef-Gel. NIEMALS: WD-40, Silikonspray, Vaseline oder Motoröl. Siehe Kapitel 7 für die vollständige Schmierstoff-Matrix.

### FAQ 4: Mein Furler knirscht — muss ich sofort handeln?

**Antwort:** Ja, Knirschgeräusche sind ein ernstes Warnsignal für Lagerschäden (Schweregrad 4/5). Sofortige Schmierung kann als Erstmaßnahme helfen. Wenn das Knirschen nach Schmierung weiterbesteht, müssen die Lager zeitnah getauscht werden. Weiterfahren mit knirschenden Lagern riskiert einen plötzlichen Lagerausfall. Siehe Fehlerbild F-15_04-03.

### FAQ 5: Wie erkenne ich, ob mein Vorstag unter dem Profil korrodiert?

**Antwort:** Von außen ist das leider kaum möglich — das ist das Hauptrisiko bei Rollreffanlagen. Indirekte Hinweise: rostfarbene Ablagerungen am Profilfuß, Spannungsverlust ohne erkennbare Ursache, Alter >15 Jahre. Die einzig sichere Methode ist die Demontage des Profils und visuelle Inspektion (oder Röntgen). AYDI-Empfehlung: Vorstag alle 10–15 Jahre prophylaktisch tauschen.

### FAQ 6: Kann ich meinen manuellen Furler auf elektrischen Antrieb umrüsten?

**Antwort:** Ja, mehrere Hersteller bieten Nachrüst-Kits an. Facnor FX+e ist als Nachrüstung für FX+-Systeme konzipiert. Selden bietet den GXe-Motor als Upgrade für Furlex-Systeme an. Kosten: 1.500–4.000 EUR inkl. Motor, Steuerung und Installation. Voraussetzung: ausreichende Batterie-Kapazität (min. 200 Ah für komfortablen Betrieb). Siehe Fallstudie D (Anhang).

### FAQ 7: Wie lang sollte meine Furling-Leine sein?

**Antwort:** Faustregel: Furling-Leine = Vorstag-Länge x pi x Anzahl_Umdrehungen + Weg_zur_Klemme. In der Praxis: für eine 10-m-Yacht mit 12 m Vorstag ca. 20–25 m Furling-Leine. Exakte Berechnung: Drum-Umfang x benötigte Wicklungen + Cockpit-Führung. Im Zweifelsfall: lieber 2 m zu lang als zu kurz.

### FAQ 8: Mein UV-Schutzstreifen ist ausgeblichen — wie dringend ist der Austausch?

**Antwort:** Mittelfristig dringend (Schweregrad 2/5). Ein ausgeblichener UV-Streifen bietet noch teilweisen Schutz. Ohne UV-Streifen degradiert das Segeltuch (Dacron) jedoch innerhalb von 1–2 Saisons merklich — Festigkeitsverlust, Versprödung. Übergangslösung: 303 Fabric Guard alle 3 Monate auftragen. Langfristig: Segelmacher beauftragen (300–600 EUR). Siehe F-15_04-10.

### FAQ 9: Darf ich den Furler bei Starkwind bedienen?

**Antwort:** Ja, aber mit Vorsicht. Moderne Rollreffanlagen sind für das Reffen bei Wind ausgelegt — das ist ihr Hauptzweck. Wichtig: Schot IMMER unter kontrolliertem Zug halten (Schot-Gegenzug beim Furling). Bei >30 kn wahrem Wind: Anluvend reffen, um die Windlast zu reduzieren. Das Entrollen bei Starkwind mit Vorsicht — nur die benötigte Segelfläche herauslassen.

### FAQ 10: Was kostet eine komplette Furler-Neuanlage?

**Antwort:** Abhängig von Bootsgröße und System:
- 8–10 m Boot: 1.500–3.000 EUR (z.B. Furlex 200S, Profurl NEX 1.0)
- 10–14 m Boot: 2.500–5.000 EUR (z.B. Furlex 300S, Profurl NEX 2.0, Harken MKIV Unit 2)
- 14–18 m Boot: 4.000–8.000 EUR (z.B. Furlex 400S, Harken MKIV Unit 3)
- >18 m Boot: 6.000–15.000 EUR (z.B. Harken MKIV Unit 4, Reckmann)
Preise inkl. Material, exkl. Montage (Montage: 500–1.500 EUR zusätzlich).

### FAQ 11: Mein Furlex 200S ist 20 Jahre alt — lohnt sich eine Überholung?

**Antwort:** Kommt auf den Zustand an. Wenn Profil, Drum-Gehäuse und Vorstag in gutem Zustand sind, lohnt sich eine Generalüberholung (neue Lager, Dichtungen, Verbindungsstücke) für ca. 200–400 EUR. Wenn Profile verformt, Drum gerissen oder Vorstag korrodiert: Neukauf wirtschaftlicher (ab 1.500 EUR für 200S). Als Faustregel: Überholung lohnt, wenn die Kosten <40 % des Neupreises betragen.

### FAQ 12: Profurl oder Furlex — welcher Hersteller ist besser?

**Antwort:** Beide Hersteller produzieren hochwertige, zuverlässige Systeme. Furlex/Selden hat leichte Vorteile bei der Ersatzteilverfügbarkeit in Nordeuropa, Profurl bei Innovation (NEX-Baureihe) und Preis-Leistung. Harken überzeugt bei größeren Systemen. Die Wahl hängt von persönlicher Präferenz, Ersatzteilverfügbarkeit im Revier und dem Budget ab. AYDI empfiehlt: Beim Refit den gleichen Hersteller beibehalten (Kompatibilität!).

### FAQ 13: Wie lagere ich meinen Furler im Winter richtig?

**Antwort:** Siehe Kapitel 10.3 und 10.4 für das vollständige Winterlagerungsprotokoll. Kurzfassung: Segel abschlagen, gesamtes System mit Süßwasser spülen, Lager nachschmieren, Furling-Leine entfernen und waschen, Drum und Profil mit atmungsaktiver Plane abdecken (KEIN Plastik!), Vorstag-Spannung leicht reduzieren.

### FAQ 14: Kann ich einen Furler selbst installieren?

**Antwort:** Eine Erstinstallation erfordert Erfahrung mit Rigg-Arbeit und sollte idealerweise von einem Rigger durchgeführt oder zumindest überwacht werden. Kritische Punkte: korrekte Vorstag-Spannung, korrekte Profil-Ausrichtung, korrekte Drum-Positionierung. Ein Furler-Austausch (gleicher Typ, gleiches System) ist für erfahrene Eigner machbar. Kosten für professionelle Installation: 500–1.500 EUR.

### FAQ 15: Mein Halyard-Swivel sitzt fest — was tun?

**Antwort:** NIEMALS mit Gewalt lösen — das kann den Swivel oder das Vorstag-Terminal beschädigen. Stattdessen: Kriechöl (z.B. Fluid Film AS-R oder CRC 5-56) großzügig auftragen, 24 Stunden einwirken lassen, dann vorsichtig mit Schraubenschlüssel lösen. Bei extremem Festsitzen: Wärme anwenden (Heißluftfön, max. 150 °C) — die thermische Ausdehnung löst den Verbund. Danach: Tef-Gel auf alle Gewinde für die Zukunft.

### FAQ 16: Wie messe ich die korrekte Vorstag-Spannung?

**Antwort:** Professionell: Mit einem Rig-Tension-Gauge (z.B. Loos & Co. Gauge, ca. 100 EUR). Die Spannung sollte 15–25 % der Bruchlast des Vorstags betragen. Richtwerte: 7mm-Vorstag: 800–1.200 kg, 8mm: 1.000–1.500 kg, 10mm: 1.500–2.200 kg. Ohne Messgerät: Subjektiver Test — bei Windstille sollte das Vorstag sich maximal 3–5 cm seitlich auslenken lassen (handbreit bei 10 m Vorstag).

### FAQ 17: Kann Salzwasser in die Drum eindringen?

**Antwort:** Ja, trotz Dichtungen. Alle Drum-Dichtungen sind Spritzwasserschutz, keine druckdichte Abdichtung. Bei Kenterung, Überspülung oder Dauerspray dringt Salzwasser ein. Deshalb: regelmäßige Süßwasser-Spülung und Schmierung sind unverzichtbar. Drum-Cover reduziert den Salzeintrag deutlich.

### FAQ 18: Wie reinige ich mein Rollsegel?

**Antwort:** Segel komplett entrollen, mit Süßwasser abspülen (Gartenschlauch genügt). Bei Verschmutzung: mildes Seifenwasser (Spülmittel), weiche Bürste. Für Schimmel/Algen: 5 % Essigwasser, einwirken lassen, abspülen. NIEMALS: Chlor, Bleiche, Hochdruckreiniger, Waschmaschine. Professionelle Segelwäsche: 100–250 EUR (inkl. Imprägnierung).

### FAQ 19: Was bedeutet die Nummerierung auf meinem Profurl-Furler (C290, C350, C430)?

**Antwort:** Die Zahl gibt den maximalen Vorstag-Durchmesser in Zehntel-Millimetern an. C290 = max. 29,0 mm Profil-Umfang (ca. 7 mm Vorstag-Ø), C350 = max. 35,0 mm (ca. 8 mm), C430 = max. 43,0 mm (ca. 10 mm). Bei der NEX-Serie gibt die Zahl die Bootsklasse an: NEX 1.0 = bis 10 m, NEX 2.0 = 10–14 m.

### FAQ 20: Mein Furler hat einen "Totpunkt" — er klemmt immer an derselben Stelle.

**Antwort:** Das deutet auf ein lokales Profilproblem hin. Häufigste Ursachen: 1) Versetztes Verbindungsstück an dieser Stelle: prüfen und ggf. tauschen. 2) Verformte Profilsektion (Delle): Sektion identifizieren und ersetzen. 3) Korrosion im Kanal an dieser Stelle: lokale Reinigung. Position der Blockade durch langsames Furling und Beobachtung eingrenzen. Zählen Sie die Wicklungen: 1 Wicklung entspricht ca. 1 Profilsektion.

### FAQ 21: Ist ein Alu-Profil oder ein GFK-Profil besser?

**Antwort:** Aluminium-Profile (Standard bei 95 % aller Furler) sind bewährt, preiswert und leicht zu reparieren. GFK/CFK-Profile (z.B. bei einigen Reckmann- und Premium-Systemen) bieten leichte Vorteile bei Gewicht und Korrosionsbeständigkeit, sind aber deutlich teurer (3–5x) und schwerer zu reparieren. Für Fahrtenyachten: Aluminium ist die richtige Wahl. Für Performance-orientierte Yachten >18 m: CFK kann sinnvoll sein.

### FAQ 22: Wie oft sollte das Vorstag getauscht werden?

**Antwort:** Empfehlung: alle 10–15 Jahre, unabhängig vom sichtbaren Zustand. Bei Rollreffanlagen ist das Vorstag unter dem Profil unsichtbar — Korrosion und Litzenbrüche bleiben unentdeckt. In den Tropen/Blauwasser: alle 8–10 Jahre. Bei Regatta-Einsatz: alle 5–8 Jahre. Kosten: 400–1.800 EUR für das Stag + 200–500 EUR für Montage inkl. Profil-Ab-/Aufbau.

### FAQ 23: Mein elektrischer Furler macht Geräusche — Motor oder Getriebe?

**Antwort:** Motor-Geräusche: Hochfrequentes Summen oder Brummen. Getriebe-Geräusche: Tieffrequentes Klackern oder Mahlen. Motor unter Last deutlich lauter als im Leerlauf: Normal (Strom steigt). Getriebe mit zunehmendem Spiel: Klappergeräusch, Service nötig. Diagnose: Motor von Getriebe trennen (falls möglich) und separat betreiben. Siehe F-15_04-11.

### FAQ 24: Kann ich einen Furler nachträglich an mein Boot anbauen?

**Antwort:** In den meisten Fällen ja. Voraussetzung: Das Vorstag muss als 1x19-Draht oder als Rundstab-Rigg ausgeführt sein. Bei Drahtseil-Vorstag (7x19): oft nicht kompatibel mit Furler-Profilen — Vorstag muss gegen 1x19 getauscht werden. Die Drum muss am Deck genug Platz haben. Kosten: 2.000–6.000 EUR komplett (System + neues Vorstag + Montage + ggf. neues Segel mit Luff-Tape).

### FAQ 25: Welche Furling-Leine ist die beste?

**Antwort:** Empfohlen: Polyester-Kern mit Dyneema-Mantel oder reines Polyester mit hoher Abriebfestigkeit. Bewährte Produkte: Marlow D2 Racing, Liros Top Cruising, FSE Robline Admiral, Cousin Diflex. Die Leine muss: glatt sein (kein Pilling), UV-beständig, korrekte Stärke für die Trommel (siehe Tabelle 5.2). Preis: 1,50–4,00 EUR/m. Leinenlänge: ca. 2x Vorstag-Länge + Cockpit-Führung.

### FAQ 26: Kann ich den Furler auch für ein asymmetrisches Spinnaker verwenden?

**Antwort:** Der Vorstag-Furler ist NICHT für Spinnaker geeignet — der Luff-Tape-Kanal und die Lager sind für ein flaches Vorsegel ausgelegt. Für asymmetrische Spinnaker/Gennaker gibt es spezielle Code-0-Furler (z.B. Karver KF-Serie, Facnor FX+ Code 0, Ronstan), die mit einem Torsionsseil statt Profilstag arbeiten.

---

## 14. Glossar

| Nr. | Deutscher Begriff | Englischer Begriff | Definition |
|---|---|---|---|
| 1 | Rollreffanlage | Roller Furling System | Mechanismus zum Auf- und Abrollen eines Segels um das Vorstag oder den Mast |
| 2 | Furler | Furler | Kurzbezeichnung für Rollreffanlage |
| 3 | Vorstag | Forestay | Draht oder Stab vom Bug zum Masttop, der den Mast nach vorn abstützt |
| 4 | Profilstag | Luff Extrusion / Foil | Aluminium-Profil, das das Vorstag umhüllt und den Kanal für das Luff-Tape bildet |
| 5 | Profil-Sektion | Foil Section | Einzelnes Segment des Profilstags (typisch 1,5–2,5 m lang) |
| 6 | Profilverbindung | Foil Connector / Joint | Verbindungsstück zwischen zwei Profilsektionen |
| 7 | Trommel / Drum | Drum Unit | Untere Einheit des Furlers, die die Furling-Leine aufnimmt und die Drehbewegung erzeugt |
| 8 | Drehwirbel | Halyard Swivel | Obere Einheit des Furlers, die das Halyard mit dem drehenden Profilstag verbindet |
| 9 | Halyard | Halyard | Fall (Leine zum Setzen des Segels) |
| 10 | Furling-Leine | Furling Line | Leine, die auf die Trommel gewickelt wird, um das Segel aufzurollen |
| 11 | Luff-Tape | Luff Tape / Bolt Rope | Verstärktes Band oder Tau am Vorliek des Segels, das in den Profil-Kanal läuft |
| 12 | Kugellager | Ball Bearing | Wälzlager mit Kugeln als Rollelemente |
| 13 | Nadellager | Needle Bearing | Wälzlager mit zylindrischen Rollen (Nadeln) als Rollelemente |
| 14 | Gleitlager | Sleeve Bearing / Bushing | Lager ohne Rollelemente, Gleitung zwischen Buchse und Welle |
| 15 | Torlon | Torlon (PAI) | Polyamid-Imid, Hochleistungskunststoff für Gleitlager |
| 16 | PTFE | PTFE (Teflon) | Polytetrafluorethylen, reibungsarmer Kunststoff für Lager und Beschichtungen |
| 17 | Seeger-Ring | Circlip / Snap Ring | Federring zur axialen Sicherung von Lagern und Wellen |
| 18 | O-Ring | O-Ring | Ringförmige Dichtung mit kreisrundem Querschnitt |
| 19 | Eloxal | Anodizing | Elektrolytische Oxidation von Aluminium zum Korrosionsschutz |
| 20 | Galvanische Korrosion | Galvanic Corrosion | Korrosion durch elektrochemische Reaktion zwischen verschiedenen Metallen |
| 21 | Opferanode | Sacrificial Anode | Unedleres Metall (Zink), das sich zum Schutz des edleren Metalls auflöst |
| 22 | Crevice Corrosion | Crevice Corrosion | Spaltkorrosion — Korrosion in engen Spalten durch Sauerstoffverarmung |
| 23 | Tea Staining | Tea Staining | Bräunliche Verfärbung von Edelstahl durch Oberflächenkorrosion |
| 24 | Passivierung | Passivation | Natürliche oder erzeugte Oxidschicht auf Edelstahl, die vor Korrosion schützt |
| 25 | Toggle | Toggle | Gelenkstück zwischen Vorstag-Terminal und Befestigungspunkt am Bug |
| 26 | Gabelkopf | Clevis / Fork Terminal | Gabelförmiges Terminal am Ende des Vorstags |
| 27 | Wantenspanner | Turnbuckle / Rigging Screw | Schraub-Spannvorrichtung zum Einstellen der Vorstag-Spannung |
| 28 | Bruchlast | Breaking Load | Maximale Kraft, bei der ein Bauteil versagt |
| 29 | Arbeitslast | Working Load / SWL | Maximal zulässige Betriebslast (typisch 40–50 % der Bruchlast) |
| 30 | Torsionsseil | Torsion Cable / Anti-Wrap Rope | Innenliegendes Seil bei Code-0-Furlern, das die Drehbewegung überträgt |
| 31 | Code 0 | Code 0 / Code Zero | Flaches Leichtwindsegel zwischen Genua und Gennaker |
| 32 | Gennaker | Gennaker | Asymmetrisches Leichtwindsegel |
| 33 | Reffen | Reefing | Verkleinern der Segelfläche |
| 34 | Furlen | Furling | Aufrollen des Segels um das Vorstag oder in den Mast |
| 35 | Entfurlen / Entrollen | Unfurling | Ausrollen des Segels aus dem Furler |
| 36 | UV-Schutzstreifen | UV Strip / Sun Cover | Textilstreifen am Achterliek und Unterliek des Rollsegels zum UV-Schutz |
| 37 | Luff | Luff / Vorliek | Vorderkante des Segels (am Vorstag) |
| 38 | Achterliek | Leech | Hinterkante des Segels |
| 39 | Unterliek | Foot | Unterkante des Segels |
| 40 | In-Mast-Furling | In-Mast Furling | Rollreffsystem, bei dem das Großsegel in einem Schlitz im Mast aufgerollt wird |
| 41 | In-Boom-Furling | In-Boom Furling | Rollreffsystem, bei dem das Großsegel im Großbaum aufgerollt wird |
| 42 | Mandrel | Mandrel | Drehbare Welle im Mast, um die das Großsegel gewickelt wird |
| 43 | Retention Clip | Retention Clip | Halteklammer, die das Profil am Vorstag zentriert |
| 44 | Drehmoment | Torque | Kraft mal Hebelarm — Maß für Verschraubungsfestigkeit |
| 45 | Axialspiel | Axial Play | Bewegungsspiel in Richtung der Drehachse |
| 46 | Radialspiel | Radial Play | Bewegungsspiel quer zur Drehachse |

---

## 15. Schnell-Referenz

### 15.1 Drehmoment-Tabelle (Kurzreferenz)

| Verschraubung | Drehmoment | Bemerkung |
|---|---|---|
| Drum-Abdeckung (Furlex) | 3 Nm | M4 Innensechskant |
| Drum-Abdeckung (Profurl NEX) | 2,5 Nm | Torx T25 |
| Drum-Abdeckung (Facnor FX+) | 3 Nm | M5 Innensechskant |
| Harken Locking Ring (Unit 0-1) | 5 Nm | Rechtsgewinde |
| Harken Locking Ring (Unit 2) | 8 Nm | LINKSGEWINDE! |
| Harken Locking Ring (Unit 3) | 12 Nm | LINKSGEWINDE! |
| Harken Locking Ring (Unit 4) | 15 Nm | LINKSGEWINDE! |
| Vorstag-Terminal (klein) | 15–20 Nm | Herstellervorgabe beachten |
| Vorstag-Terminal (mittel) | 20–25 Nm | Herstellervorgabe beachten |
| Vorstag-Terminal (groß) | 25–30 Nm | Herstellervorgabe beachten |
| Toggle-Bolzen | 10–18 Nm | Je nach Größe |

### 15.2 Schmierintervall-Tabelle (Kurzreferenz)

| Komponente | Küste (Salzwasser) | Binnensee (Süßwasser) | Tropen | Schmierstoff |
|---|---|---|---|---|
| Drum-Lager | Alle 6 Monate | Jährlich | Alle 4 Monate | McLube OneDrop |
| Swivel-Lager | Alle 6 Monate | Jährlich | Alle 4 Monate | McLube OneDrop |
| Profil-Kanal | Jährlich | Alle 2 Jahre | Alle 8 Monate | McLube SailKote |
| Gewinde (Alu/Edelstahl) | Bei jeder Montage | Bei jeder Montage | Bei jeder Montage | Tef-Gel |
| Nadellager | Jährlich | Alle 2 Jahre | Alle 8 Monate | Harken Winch Grease |
| Drum-Dichtungen | Bei jeder Montage | Bei jeder Montage | Bei jeder Montage | Molykote 111 |

### 15.3 Lager-Austausch-Intervalle

| Lagertyp | Standard-Intervall | Verschärft (Tropen/Regatta) | Anzeichen für Austausch |
|---|---|---|---|
| Kugellager (2RS, Edelstahl) | Alle 8–12 Jahre | Alle 5–8 Jahre | Kratzen, Spiel, Schwergängigkeit |
| Nadellager | Alle 5–8 Jahre | Alle 3–5 Jahre | Spiel, Geräusche |
| Torlon-Gleitlager | Alle 10–15 Jahre | Alle 8–10 Jahre | Spiel >15 % Zunahme |
| PTFE-Gleitlager | Alle 8–12 Jahre | Alle 5–8 Jahre | Spiel >15 % Zunahme |

### 15.4 Häufig benötigte Teilenummern (Kurzreferenz)

| Beschreibung | Furlex | Profurl | Harken | Facnor |
|---|---|---|---|---|
| Service Kit (klein) | 507-955-01 | KNEX-BEAR-10 | BK4515-0/1 | FX15-BRG |
| Service Kit (mittel) | 507-956-01 | KNEX-BEAR-20 | BK4515-2 | FX25-BRG |
| Service Kit (groß) | 507-957-01 | KC430-BEAR | BK4515-3/4 | FX35-BRG |
| Drum Seal Kit | 507-950-01 | KNEX-SEAL | — | FX-SEAL |
| Profilverbinder (5 Stk.) | 507-821-05 | KNEX-CON-5 | BK4520 | — |
| Bearing Press Tool | 507-899-XX | TOOL-CBRG | BK4590 | TOOL-FX-BRG |
| Locking Ring Wrench | — | — | BK4591 | — |

---

## ANHANG A–H: Fallstudien

### ANHANG A: Furlex 200S Generalüberholung nach 12 Jahren

**Boot:** Bavaria 34 Cruiser, Baujahr 2013
**System:** Selden Furlex 200S, installiert 2013
**Einsatz:** Ostsee, ca. 600 Seemeilen/Jahr, Winterlager an Land
**Anlass:** Zunehmend schwergängiges Furling, leichtes Knirschen

**Befund:**
- Untere Lager: deutliche Schwergängigkeit, Rasten bei Drehung — Pittings auf Laufbahnen
- Obere Lager: leicht schwergängig, aber noch akzeptabel
- Profil: in gutem Zustand, keine Verformung, 2 von 6 Verbindungsstücken mit UV-Versprödung
- Drum-Dichtungen: verhärtet, Elastizität verloren
- Vorstag: keine sichtbaren Schäden (8 Jahre alter 1x19 Draht, 7 mm)
- UV-Schutzstreifen: ausgeblichen, Nähte teilweise gelöst

**Durchgeführte Arbeiten:**
1. Komplett-Demontage Drum und Profilstag
2. 4 Kugellager getauscht (6004-2RS + 6003-2RS, Selden Service Kit 507-955-01)
3. Alle Drum-Dichtungen erneuert
4. 2 Profilverbindungsstücke getauscht (507-821-01)
5. Profil-Kanal gereinigt und mit McLube SailKote behandelt
6. Vorstag visuell inspiziert — OK
7. Alle Gewinde mit Tef-Gel montiert
8. Zusammenbau und Funktionstest

**Kosten:**
- Selden Service Kit 507-955-01: 95 EUR
- 2x Profilverbindung 507-821-01: 30 EUR
- McLube OneDrop + SailKote: 45 EUR
- Tef-Gel (60g): 28 EUR
- Summe Material: 198 EUR
- Arbeit (DIY): 6 Stunden

**Ergebnis:** Furler wie neu. Empfehlung: UV-Schutzstreifen erneuern lassen (Segelmacher: 380 EUR), Vorstag in 3 Jahren tauschen (dann 15 Jahre alt).

---

### ANHANG B: Profurl NEX Profilverbindung-Reparatur auf See

**Boot:** Jeanneau Sun Odyssey 389, Baujahr 2019
**System:** Profurl NEX 2.0, installiert 2019
**Situation:** Überführungstörn Kiel nach Cuxhaven, 18 kn wahrem Wind
**Problem:** Segel klemmt plötzlich beim Reffen bei ca. einem Drittel der Profillänge

**Diagnose auf See:**
1. Furling gestoppt, Schot kontrolliert
2. Halyard leicht gelöst — Segel ließ sich 10 cm bewegen
3. Von Deck aus sichtbar: Profilverbindung hat sich gelöst, Spalt ca. 5 mm
4. Segel mit vorsichtigem Hin-und-Her-Bewegen durch die Blockade gearbeitet
5. Segel komplett gefurlt, mit Bändsel gesichert

**Notfall-Reparatur auf See:**
1. Segel gefurlt gelassen (gesichert mit 3 Bändseln)
2. Betroffene Verbindungsstelle mit selbstverschweißendem Tape (Rescue Tape) umwickelt
3. Zusätzlich 2 UV-beständige Kabelbinder als Sicherung
4. Weiterfahrt unter Motor nach Cuxhaven

**Reparatur im Hafen (Cuxhaven):**
1. Segel abgeschlagen
2. Betroffene Profilsektion identifiziert (3. Sektion von unten)
3. Altes Verbindungsstück entfernt — Kunststoff gerissen (UV-Schaden nach 6 Jahren)
4. Neues Verbindungsstück eingesetzt (KNEX-CON, über Toplicht Express bestellt, 14 EUR)
5. Alle übrigen Verbindungen geprüft — 1 weitere präventiv getauscht
6. Segel wieder angeschlagen, Funktionstest

**Kosten:** 28 EUR (2 Verbindungsstücke) + 15 EUR Express-Versand = 43 EUR
**Lektion:** Profilverbindungen alle 5 Jahre prüfen, Ersatz-Verbindungsstücke an Bord mitführen!

---

### ANHANG C: Harken MKIV Drum-Unit Lageraustausch

**Boot:** Hallberg-Rassy 40, Baujahr 2010
**System:** Harken MKIV Unit 3, installiert 2010
**Einsatz:** Nordsee + Mittelmeer (Sommer), ca. 2.000 sm/Jahr
**Anlass:** Starkes Knirschen, spürbare Vibrationen in der Furling-Leine

**Befund:**
- Unteres Lager: Schwergängig, deutliches Kratzen, Rostspuren an der Dichtung
- Axiales Kugellager: Korrosion auf Kugeln (Pittings)
- Radiales Kugellager: In Ordnung, aber prophylaktischer Austausch empfohlen
- Locking Ring: Leichter Korrosionsansatz am Gewinde
- Drum-Gehäuse: OK, keine Risse

**Durchgeführte Arbeiten (durch Rigger):**
1. Locking Ring gelöst (LINKSGEWINDE! — Hakenschlüssel BK4591, Unit 3: 12 Nm)
2. Drum-Oberteil abgenommen
3. Lageranordnung als Einheit entnommen
4. Alle 3 Lager mit Harken Bearing Press (BK4590) ausgetauscht
5. Neue Lager aus Harken Kit BK4515-3 eingesetzt
6. Frisches Harken Winch Grease auf Lagersitze
7. Zusammenbau, Locking Ring mit 12 Nm angezogen
8. Funktionstest: einwandfrei, leise, leichtgängig

**Kosten:**
- Harken Bearing Kit BK4515-3: 120 EUR
- Harken Winch Grease: 18 EUR
- Rigger-Arbeitszeit (2 Stunden): 190 EUR
- Summe: 328 EUR

**Ergebnis:** Problem vollständig behoben. Nächster Lageraustausch in 8–10 Jahren empfohlen.

---

### ANHANG D: Facnor FX+ Umrüstung von manuell auf elektrisch

**Boot:** Beneteau Oceanis 46.1, Baujahr 2020
**System:** Facnor FX+ 2500 manuell wird zu FX+ 2500e elektrisch
**Anlass:** Eigner (67 Jahre) wünscht komfortableres Handling bei Einhand-Segeln

**Umrüstung:**
1. Facnor FX+e Nachrüst-Motor-Kit bestellt (über Facnor-Händler: 2.200 EUR)
2. Elektrische Installation:
   - 24V-Speiseleitung (25 mm2) vom Batterieverteiler zum Mastfuß
   - 80A-Sicherungsautomat am Batterieverteiler
   - Kabelfernbedienung im Cockpit (Doppeltaster: Furling/Unfurling)
   - Nothalt-Schalter am Mastfuß
3. Motor-Montage:
   - Motor an Drum-Basis adaptiert (Facnor-Adapter, im Kit enthalten)
   - Kupplung zwischen Motor und Drum
   - Manuelle Entkopplung (Notfall-Hebel) getestet
4. Funktionstest: Furling/Unfurling in 15 Sekunden (Genua 45 m2)

**Kosten:**
- Facnor FX+e Motor-Kit: 2.200 EUR
- Kabel und Installation: 350 EUR
- Fernbedienung und Schalter: 180 EUR
- Arbeitszeit (Elektriker + Rigger): 650 EUR
- Summe: 3.380 EUR

**Ergebnis:** Eigner kann Genua nun per Knopfdruck furlen/unfurlen. Manuelle Bedienung als Backup weiterhin möglich. Batterie-Verbrauch: ca. 25 Ah pro Tag bei normalem Segelbetrieb.

---

### ANHANG E: Selden GX15 Korrosionsschaden durch falsche Anoden

**Boot:** Contest 42CS, Baujahr 2008
**System:** Selden GX15 (Großsegel In-Mast Furling), elektrischer Antrieb (GXe)
**Einsatz:** Mittelmeer ganzjährig (Spanien), Liegeplatz im Wasser
**Problem:** Motor dreht langsam, Knirschen im Mastfuß-Bereich

**Befund:**
- Massive galvanische Korrosion am Aluminium-Mandrel im Mastfuß
- Ursache: Falsche Anoden — Boot hatte bei einem Refit Magnesium-Anoden (für Süßwasser) statt Zink-Anoden (für Salzwasser) erhalten
- Zusätzlich: Landstrom ohne galvanischen Isolator — Streu-Strom-Korrosion
- Mandrel-Lager: durch Korrosionsprodukte blockiert
- Motor: OK, aber durch erhöhten Widerstand überlastet

**Reparatur (Werft Palma):**
1. Mast gelegt
2. Mandrel und Lager komplett ausgebaut
3. Korrodierte Mandrel-Sektion getauscht (Selden-Ersatzteil: 850 EUR)
4. Neue Lager eingebaut (Selden Kit: 180 EUR)
5. ALLE Anoden durch korrekte Zink-Anoden ersetzt (4 Stk., je 35 EUR)
6. Galvanischer Isolator (Dairex GI-30) installiert (320 EUR)
7. Motor-Service (Bürsten, Dichtungen): 280 EUR
8. Mast gestellt, System getestet

**Kosten:**
- Ersatzteile (Mandrel, Lager, Anoden, Isolator): 1.630 EUR
- Arbeitszeit (Mast legen/stellen + Reparatur): 2.800 EUR
- Summe: 4.430 EUR

**Lektion:** IMMER korrekte Anoden für das Revier verwenden. Salzwasser = Zink. Süßwasser = Magnesium. Brackwasser = Aluminium. Galvanischer Isolator bei Landstrom ist PFLICHT.

---

### ANHANG F: Karver KF7 Rennsegler — Saisonales Race-Service

**Boot:** Fast 42 Custom, Baujahr 2017
**System:** Karver KF7 (Code 0 Furler), Regatta-Einsatz
**Einsatz:** 25+ Regatten/Saison, Mittelmeer + Atlantik
**Service-Philosophie:** Vierteljährliches Service, kompromisslose Leichtgängigkeit

**Saisonales Race-Service-Protokoll:**
1. **Vor Saisonbeginn (März):**
   - Komplett-Demontage KF7
   - Torlon-Gleitlager prüfen — Austausch bei >10 % Spiel-Zunahme
   - Kugellager prüfen — Austausch bei geringstem Zweifel
   - Torsionsseil auf Knicke und Litzen prüfen — alle 2 Jahre tauschen
   - Alles mit McLube OneDrop schmieren
   - Gewicht der Einheit wiegen (Referenz: 4,2 kg) — >4,3 kg = Salzeinlagerung!

2. **Mitte Saison (Juli):**
   - Funktionstest unter Last
   - Lager-Geräuschprüfung
   - Torsionsseil-Spannung prüfen
   - Nachschmierung

3. **Saisonende (November):**
   - Komplett-Demontage, Reinigung, Konservierung
   - Verschleißteile für nächste Saison bestellen

**Kosten pro Saison:** ca. 250 EUR (Material) + 400 EUR (Rigger, 2x Service)
**Ergebnis:** Null Ausfälle in 4 Saisons. Furling-Zeit Code 0 (85 m2): 8 Sekunden.

---

### ANHANG G: Code 0 Furler Notfall-Reparatur während Überführung

**Boot:** Oyster 575, Baujahr 2015
**System:** Facnor FX+ Code 0 Furler
**Situation:** Atlantik-Überquerung (Las Palmas nach Barbados), Tag 12, Position 20 N 42 W
**Problem:** Code 0 Furler blockiert vollständig — Segel kann nicht gefurlt werden

**Sofortmaßnahmen auf See:**
1. Kurs so geändert, dass Code 0 killt (Vorwind nach Raumer Kurs)
2. Segel mit Bändseln provisorisch an Vorstag gebunden
3. Torsionsseil-Zustand geprüft — gerissen (Ermüdungsbruch nach 8 Jahren)
4. Code 0 per Hand von Deck aus heruntergeholt (2 Personen, 45 Minuten)

**Provisorische Reparatur:**
1. Gebrochenes Torsionsseil an der Bruchstelle mit Takling-Garn und Epoxid verspleißt
2. Verstärkung mit Dyneema-Leine (4 mm) spiralförmig um die Reparaturstelle gewickelt
3. Furler-Funktionstest ohne Segel: dreht, aber mit Widerstand an Reparaturstelle
4. Code 0 nicht mehr gesetzt für den Rest der Überquerung (Risiko zu hoch)

**Endgültige Reparatur (Barbados):**
1. Neues Torsionsseil bestellt (Facnor, 18 m Länge: 280 EUR)
2. Lieferzeit: 8 Tage per DHL Express aus Frankreich
3. Torsionsseil gewechselt, Furler komplett getestet
4. Gleichzeitig: alle Lager geprüft und geschmiert

**Kosten:** 280 EUR (Torsionsseil) + 85 EUR (Versand Express) + 120 EUR (Rigger Barbados) = 485 EUR
**Lektion:** Torsionsseil alle 5–6 Jahre prophylaktisch tauschen (Regatta: alle 3–4 Jahre). Ein Ersatz-Torsionsseil auf Langfahrt mitführen!

---

### ANHANG H: Grosssegel-Rollreff Leisetrim — Wartung nach 5 Jahren

**Boot:** Hanse 548, Baujahr 2020
**System:** Selden In-Mast Furling, C-Mast
**Einsatz:** Nordsee/Mittelmeer, ca. 1.500 sm/Jahr
**Anlass:** 5-Jahres-Service gemäß Wartungsplan

**Durchgeführte Arbeiten:**
1. Mast gelegt (Kran, Werft Heiligenhafen)
2. Mandrel aus dem Mast gezogen
3. Mandrel-Lager inspiziert:
   - Unteres Lager: leichte Schwergängigkeit — getauscht
   - Oberes Lager: OK — geschmiert und belassen
4. Mast-Schlitz (Track) gereinigt:
   - Salzablagerungen mit Süßwasser + Bürste entfernt
   - Gleitflächen mit McLube SailKote behandelt
5. Outhaul-Mechanismus:
   - Seil geprüft — OK (Dyneema, 3 Jahre alt)
   - Umlenkrollen geprüft — 1 Rolle schwergängig — getauscht
6. Mandrel wieder eingebaut, Mast gestellt
7. Segel eingefahren, Funktionstest:
   - Furling: gleichmäßig, leise
   - Unfurling: vollständig, gutes Profil
   - Reffen auf 3 Positionen: einwandfrei

**Kosten:**
- Lager (1 Stk.): 45 EUR
- Umlenkrolle: 65 EUR
- McLube SailKote: 25 EUR
- Mastlegen/-stellen (Kran): 380 EUR
- Rigger-Arbeitszeit (4 Stunden): 380 EUR
- Summe: 895 EUR

**Ergebnis:** System wieder in einwandfreiem Zustand. Nächstes 5-Jahres-Service: 2030.

---

## ANHANG S: Erweiterte Wartungstabellen und Referenzdaten

### S.1 Vorstag-Dimensionierung und Bruchlasten

| Vorstag-Ø (mm) | Bauart | Bruchlast (kg) | Arbeitslast 25% (kg) | Empf. Furler-Modelle |
|---|---|---|---|---|
| 4 | 1x19 Edelstahl | 1.600 | 400 | Harken MKIV Unit 0, Furlex 104 |
| 5 | 1x19 Edelstahl | 2.500 | 625 | Furlex 200S, Profurl C290, Harken MKIV Unit 0-1 |
| 6 | 1x19 Edelstahl | 3.500 | 875 | Furlex 200S/300S, Profurl C290/C350, Harken MKIV Unit 1-2 |
| 7 | 1x19 Edelstahl | 4.900 | 1.225 | Furlex 300S, Profurl C350/C430, Harken MKIV Unit 2, Facnor FX+ 1500 |
| 8 | 1x19 Edelstahl | 6.300 | 1.575 | Furlex 300S/400S, Profurl C430, Harken MKIV Unit 2-3, Facnor FX+ 2500 |
| 9 | 1x19 Edelstahl | 7.900 | 1.975 | Furlex 400S, Profurl C430, Harken MKIV Unit 3, Facnor FX+ 2500 |
| 10 | 1x19 Edelstahl | 9.900 | 2.475 | Furlex 400S, Harken MKIV Unit 3-4, Facnor FX+ 3500 |
| 12 | 1x19 Edelstahl | 14.100 | 3.525 | Harken MKIV Unit 4, Facnor FX+ 3500, Reckmann |
| 14 | 1x19 Edelstahl | 19.000 | 4.750 | Harken MKIV Unit 4, Reckmann |
| 5 | Nitronic 50 Rod | 3.400 | 850 | Furlex 200S, Profurl NEX 1.0 |
| 6 | Nitronic 50 Rod | 4.900 | 1.225 | Furlex 300S, Profurl NEX 1.0/2.0 |
| 7 | Nitronic 50 Rod | 6.600 | 1.650 | Furlex 300S, Profurl NEX 2.0, Harken MKIV Unit 2 |
| 8 | Nitronic 50 Rod | 8.600 | 2.150 | Furlex 400S, Harken MKIV Unit 3 |
| 10 | Nitronic 50 Rod | 13.500 | 3.375 | Harken MKIV Unit 3-4, Reckmann |
| 12 | Nitronic 50 Rod | 19.400 | 4.850 | Harken MKIV Unit 4, Reckmann |

### S.2 Segelflächen-Richtwerte für Furler-Dimensionierung

| Bootslänge (m) | Genua-Fläche (m2) | Furler-Klasse (empf.) | Vorstag-Ø (empf.) |
|---|---|---|---|
| 7–8 | 15–22 | Klein (Furlex 200S, NEX 1.0, MKIV 0) | 5–6 mm |
| 8–9 | 20–28 | Klein (Furlex 200S, NEX 1.0, MKIV 1) | 5–6 mm |
| 9–10 | 25–35 | Klein/Mittel (Furlex 200S/300S, NEX 1.0/2.0, MKIV 1) | 6–7 mm |
| 10–11 | 30–40 | Mittel (Furlex 300S, NEX 2.0, MKIV 2) | 6–8 mm |
| 11–12 | 35–48 | Mittel (Furlex 300S, NEX 2.0, MKIV 2, FX+ 1500) | 7–8 mm |
| 12–13 | 40–55 | Mittel (Furlex 300S, C430, MKIV 2, FX+ 2500) | 7–9 mm |
| 13–14 | 45–60 | Mittel/Groß (Furlex 300S/400S, C430, MKIV 2-3, FX+ 2500) | 8–9 mm |
| 14–15 | 50–70 | Groß (Furlex 400S, MKIV 3, FX+ 2500) | 8–10 mm |
| 15–17 | 60–85 | Groß (Furlex 400S, MKIV 3, FX+ 3500) | 9–10 mm |
| 17–20 | 75–110 | Sehr groß (MKIV 3-4, FX+ 3500, Reckmann) | 10–12 mm |
| 20–25 | 100–150 | Extra groß (MKIV 4, Reckmann, Bamar) | 12–14 mm |

### S.3 Saisonale Wartungskosten-Übersicht (Richtwerte)

#### S.3.1 Jährliche Wartungskosten DIY

| Kostenposition | Klein (7–10 m) | Mittel (10–14 m) | Groß (14–18 m) | Sehr groß (>18 m) |
|---|---|---|---|---|
| Schmiermittel (McLube, Tef-Gel) | 30 EUR | 40 EUR | 50 EUR | 60 EUR |
| Furling-Leine (anteilig, alle 4 Jahre) | 10 EUR | 15 EUR | 20 EUR | 25 EUR |
| Verbrauchsmaterial (Reiniger, Lappen) | 10 EUR | 15 EUR | 20 EUR | 25 EUR |
| Lager (anteilig, alle 10 Jahre) | 10 EUR | 12 EUR | 15 EUR | 20 EUR |
| Dichtungen (anteilig, alle 5 Jahre) | 5 EUR | 8 EUR | 10 EUR | 12 EUR |
| **Summe pro Jahr (DIY)** | **65 EUR** | **90 EUR** | **115 EUR** | **142 EUR** |

#### S.3.2 Jährliche Wartungskosten Fachbetrieb

| Kostenposition | Klein (7–10 m) | Mittel (10–14 m) | Groß (14–18 m) | Sehr groß (>18 m) |
|---|---|---|---|---|
| Material (wie oben) | 65 EUR | 90 EUR | 115 EUR | 142 EUR |
| Rigger-Stunden (2–4 Std./Jahr) | 200 EUR | 300 EUR | 400 EUR | 500 EUR |
| Mastbesteigung (1x/Jahr) | 100 EUR | 120 EUR | 150 EUR | 200 EUR |
| **Summe pro Jahr (Fachbetrieb)** | **365 EUR** | **510 EUR** | **665 EUR** | **842 EUR** |

#### S.3.3 Lebenszykluskosten-Vergleich (20 Jahre)

| Szenario | Klein (7–10 m) | Mittel (10–14 m) | Groß (14–18 m) |
|---|---|---|---|
| Präventive Wartung (DIY, 20 Jahre) | 1.300 EUR | 1.800 EUR | 2.300 EUR |
| + 1x Lageraustausch (Jahr 10) | +200 EUR | +300 EUR | +400 EUR |
| + 1x Vorstag-Austausch (Jahr 12) | +600 EUR | +900 EUR | +1.400 EUR |
| + 2x Furling-Leine (Jahr 5, 10) | +100 EUR | +140 EUR | +200 EUR |
| **GESAMT Präventiv (20 Jahre)** | **2.200 EUR** | **3.140 EUR** | **4.300 EUR** |
| | | | |
| Reaktive Wartung (20 Jahre, geschätzt) | | | |
| + 2x Notfall-Lagerausfall | +800 EUR | +1.200 EUR | +1.800 EUR |
| + 1x Profilschaden durch Korrosion | +600 EUR | +800 EUR | +1.200 EUR |
| + 1x Segelschaden durch Furler-Ausfall | +1.500 EUR | +2.500 EUR | +4.000 EUR |
| + 1x Vorstag-Notaustausch | +1.000 EUR | +1.500 EUR | +2.500 EUR |
| **GESAMT Reaktiv (20 Jahre)** | **3.900 EUR** | **6.000 EUR** | **9.500 EUR** |

**Fazit:** Präventive Wartung spart über 20 Jahre 45–55 % der Gesamtkosten im Vergleich zur reaktiven Wartung.

### S.4 Fehlerbild-Häufigkeitsverteilung nach Alter

| Fehlerbild | 0–3 Jahre | 3–7 Jahre | 7–12 Jahre | >12 Jahre |
|---|---|---|---|---|
| F-01: Schwergängig | Selten (2 %) | Gelegentlich (8 %) | Häufig (25 %) | Sehr häufig (40 %) |
| F-02: Ungleichmäßig | Gelegentlich (5 %) | Gelegentlich (5 %) | Gelegentlich (8 %) | Häufig (15 %) |
| F-03: Lagergeräusche | Sehr selten (1 %) | Selten (3 %) | Gelegentlich (12 %) | Häufig (30 %) |
| F-04: Segel klemmt | Selten (2 %) | Gelegentlich (5 %) | Gelegentlich (10 %) | Häufig (20 %) |
| F-05: Leinenwicklung | Gelegentlich (3 %) | Gelegentlich (5 %) | Gelegentlich (5 %) | Gelegentlich (8 %) |
| F-06: Profilverbindung | Sehr selten (0 %) | Selten (2 %) | Gelegentlich (8 %) | Häufig (18 %) |
| F-07: Swivel-Korrosion | Sehr selten (0 %) | Selten (2 %) | Gelegentlich (8 %) | Häufig (15 %) |
| F-08: Leinenversagen | Selten (1 %) | Gelegentlich (5 %) | Häufig (12 %) | Häufig (15 %) |
| F-09: Vorstag-Spannung | Sehr selten (0 %) | Selten (1 %) | Selten (3 %) | Gelegentlich (8 %) |
| F-10: UV-Streifen | Selten (1 %) | Gelegentlich (8 %) | Häufig (20 %) | Sehr häufig (35 %) |
| F-11: Elektro-Ausfall | Selten (2 %) | Gelegentlich (5 %) | Gelegentlich (10 %) | Häufig (20 %) |
| F-12: Hydraulik-Leck | Selten (1 %) | Selten (3 %) | Gelegentlich (8 %) | Häufig (15 %) |

### S.5 Kompatibilitäts-Matrix: Profil → Luff-Tape

| Profil-Hersteller | Profil-Typ | Luff-Tape Typ | Kompatibel mit Segel von | Bemerkung |
|---|---|---|---|---|
| Selden/Furlex | 200S | Selden Type 1 | Elvstrom, North, Doyle, Quantum, Hood | Standard-Tape, weit verbreitet |
| Selden/Furlex | 300S | Selden Type 2 | Elvstrom, North, Doyle, Quantum, Hood | Breiteres Tape für größere Segel |
| Selden/Furlex | 400S | Selden Type 3 | Elvstrom, North, Doyle, Quantum, Hood | Noch breiteres Tape |
| Profurl | C-Serie | Profurl Luff Tape | North, Doyle, Quantum, UK Sailmakers | Eigener Standard |
| Profurl | NEX-Serie | Profurl NEX Tape | North, Doyle, Quantum, UK Sailmakers | Kompatibel mit C-Serie Tape |
| Harken | MKIV (klein) | Harken Luff Tape S | Diverse | Eigener Standard, aber ähnlich Selden Type 1 |
| Harken | MKIV (groß) | Harken Luff Tape L | Diverse | Eigener Standard |
| Facnor | FX+ | Facnor Universal Tape | Diverse | Universell kompatibel |
| Facnor | LS | Facnor LS Tape | Diverse | Breiter als FX+ |

**WICHTIG:** Bei Segelbestellung IMMER den genauen Furler-Typ und das Profil angeben. Segelmacher braucht:
1. Hersteller und Modell des Furlers
2. Profiltyp (z.B. Furlex 300S)
3. Vorstag-Länge (Drum-Oberkante bis Swivel-Unterkante)
4. Luff-Tape-Typ (Herstellervorgabe)

### S.6 Checkliste: Furler-Kauf (Neukauf oder Gebraucht)

#### S.6.1 Neukauf-Checkliste

| Kriterium | Frage | Hinweis |
|---|---|---|
| Bootsgröße | Passt die Furler-Klasse zur Bootsgröße? | Siehe Tabelle S.2 |
| Vorstag-Ø | Passt der Furler zum vorhandenen Vorstag? | Ggf. Vorstag tauschen |
| Segelfläche | Ist der Furler für die geplante Segelfläche ausgelegt? | Max. Segelfläche beachten |
| Profiltyp | Passt das Profil zum vorhandenen Segel? | Luff-Tape-Kompatibilität! |
| Ersatzteile | Sind Ersatzteile im Revier verfügbar? | In Nordeuropa: Furlex, Profurl gut verfügbar |
| Service | Gibt es einen Service-Partner im Revier? | Für 5-Jahres-Service wichtig |
| Budget | Passt das System zum Budget? | Inkl. Montage und ggf. neues Vorstag |
| Antrieb | Manuell, elektrisch oder hydraulisch? | Elektrisch ab ca. 1.500 EUR Aufpreis |

#### S.6.2 Gebraucht-Kauf: Prüfpunkte

| Nr. | Prüfpunkt | Methode | Risiko bei Mangel |
|---|---|---|---|
| 1 | Lager-Zustand | Handprüfung: Drehung, Geräusch, Spiel | HOCH — Lageraustausch 65–155 EUR |
| 2 | Profil-Zustand | Sichtprüfung: Verformung, Korrosion, Kanal | MITTEL — Profil-Sektion 80–200 EUR |
| 3 | Profilverbindungen | Sichtprüfung: Spalt, Kunststoff-Zustand | NIEDRIG — Verbinder 15–25 EUR |
| 4 | Drum-Gehäuse | Sichtprüfung: Risse, UV-Schäden | HOCH — Drum-Austausch 200–500 EUR |
| 5 | Dichtungen | Sichtprüfung: Elastizität, Risse | NIEDRIG — Seal Kit 25–40 EUR |
| 6 | Halyard-Swivel | Sichtprüfung: Korrosion, Drehung | HOCH — Swivel 150–500 EUR |
| 7 | Vorstag (falls inkl.) | Sichtprüfung: Litzen, Korrosion | KRITISCH — Vorstag 400–1.800 EUR |
| 8 | Vollständigkeit | Alle Teile vorhanden? (Abdeckung, Splinte, Anleitung) | NIEDRIG |
| 9 | Alter | Herstellungsjahr prüfen (Seriennummer) | Info für Lebensdauer-Abschätzung |
| 10 | Provenienz | Salzwasser oder Süßwasser? Tropen? Regatta? | Beeinflusst Verschleißzustand |

**Gebraucht-Preise (Richtwerte, guter Zustand):**
- Furlex 200S (5–10 Jahre): 500–800 EUR
- Furlex 300S (5–10 Jahre): 800–1.200 EUR
- Profurl NEX 2.0 (3–8 Jahre): 700–1.100 EUR
- Harken MKIV Unit 2 (5–10 Jahre): 900–1.500 EUR
- Harken MKIV Unit 3 (5–10 Jahre): 1.200–2.000 EUR

### S.7 Herstellerkontakte und Service-Netzwerke

| Hersteller | Hauptsitz | Service-Hotline | E-Mail Service | Autorisierte Händler (DE) |
|---|---|---|---|---|
| Selden/Furlex | Göteborg, SE | +46 31 69 69 00 | service@sfrurlex.com | SVB, Toplicht, Compass |
| Profurl | Lorient, FR | +33 2 97 87 65 00 | service@profurl.com | SVB, Toplicht, AWN |
| Harken | Limone, IT (EU) | +39 039 9000 775 | service@harken.it | SVB, 12 West, Toplicht |
| Facnor | Vannes, FR | +33 2 97 42 42 78 | sav@facnor.com | SVB, Toplicht |
| Karver | La Trinité, FR | +33 2 97 55 79 80 | service@karfrver.fr | SVB, 12 West |
| Ronstan | Melbourne, AU | +61 3 9355 1877 | service@ronstan.com | 12 West, Segelladen |
| Reckmann | Bergisch Gladbach, DE | +49 2202 9598-0 | service@reckmann.com | Direkt, Toplicht |
| Bamar | Montebelluna, IT | +39 0423 603 522 | service@bamar.it | SVB, Toplicht |

### S.8 Normen und Vorschriften für Rollreffanlagen

| Norm/Vorschrift | Titel | Relevanz für Furler |
|---|---|---|
| ISO 15084 | Small craft — Anchoring, mooring and towing — Strong points | Befestigungspunkte für Vorstag |
| ISO 12215-6 | Hull construction — Structural arrangement | Deck-Durchführung Vorstag-Befestigung |
| ISO 15085 | Man-overboard prevention | Keine Stolperfallen durch Drum am Bug |
| EN 795 | Personal fall protection equipment | Mastbesteigung für Swivel-Wartung |
| DNV GL Rules | Classification of Yachts | Rigg-Dimensionierung >24 m |
| CE-Richtlinie 2013/53/EU | Sportboot-Richtlinie | Allgemeine Sicherheitsanforderungen Rigg |
| ISAF OSR | Offshore Special Regulations | Anforderungen an Regattateilnahme |

### S.9 Typische Fehler bei der Furler-Montage

Die folgenden Fehler werden bei der Installation oder Remontage nach Service am häufigsten beobachtet:

**Fehler 1: Profilsektionen in falscher Reihenfolge montiert**
- Konsequenz: Profil passt nicht zusammen, Segel klemmt
- Vermeidung: Sektionen vor Demontage nummerieren (wasserfester Marker)

**Fehler 2: Lager falsch herum eingebaut**
- Konsequenz: Erhöhte Reibung, vorzeitiger Verschleiß
- Vermeidung: Markierung auf Lager beachten, Einbaurichtung fotografieren

**Fehler 3: Dichtungen beim Zusammenbau verrutscht**
- Konsequenz: Salzwasser dringt ein, Lager korrodieren schnell
- Vermeidung: Dichtungen mit Silikonfett fixieren, beim Zusammenbau kontrollieren

**Fehler 4: Profilverbindung nicht vollständig eingerastet**
- Konsequenz: Spalt im Profil, Segel klemmt
- Vermeidung: Jede Verbindung einzeln auf Spaltmaß prüfen (<0,5 mm)

**Fehler 5: Furling-Leine in falscher Wickelrichtung aufgelegt**
- Konsequenz: Leine wickelt sich bei Gebrauch ab statt auf
- Vermeidung: Herstelleranleitung beachten, Funktionstest vor Segel setzen

**Fehler 6: Vorstag-Spannung nicht nachgestellt nach Profil-Montage**
- Konsequenz: Durchhängendes Vorstag, Profil knickt
- Vermeidung: Spannung nach jedem Profil-Aus-/Einbau neu einstellen

**Fehler 7: Schrauben ohne Tef-Gel montiert (Alu/Edelstahl)**
- Konsequenz: Festfressen nach 1–2 Saisons, Demontage nur mit Gewalt
- Vermeidung: ALLE Schrauben in Alu-Edelstahl-Kombination mit Tef-Gel

**Fehler 8: Halyard-Swivel-Schäkel zu klein/falsche Qualität**
- Konsequenz: Verschleiß, Bruchrisiko
- Vermeidung: Original-Schäkel des Herstellers verwenden, 316L-Qualität

**Fehler 9: Sicherungssplinte vergessen**
- Konsequenz: Bolzen vibriert heraus, Rigg-Versagen möglich
- Vermeidung: Checkliste verwenden, alle Splinte vor Funktionstest kontrollieren

**Fehler 10: Drum-Abdeckung überdreht**
- Konsequenz: Gewinde im Kunststoff zerstört, Abdeckung hält nicht mehr
- Vermeidung: Drehmomentschlüssel verwenden (2,5–4 Nm je nach Modell)

### S.10 Inspektion des Vorstags unter dem Profil

Das Vorstag unter dem Profil ist der am schwierigsten zu inspizierende Teil der Rollreffanlage. Korrosion und Litzenbrüche bleiben oft jahrelang unentdeckt.

**Inspektionsmethoden:**

| Methode | Genauigkeit | Aufwand | Kosten | Wann empfohlen? |
|---|---|---|---|---|
| Visuelle Inspektion (Profil demontiert) | Gut (80 %) | 4–8 Std. | 300–600 EUR (Rigger) | Alle 5 Jahre ab Jahr 8 |
| Magnetische Rissprüfung (MPI) | Sehr gut (95 %) | 6–10 Std. | 500–1.000 EUR | Alle 5 Jahre ab Jahr 10 |
| Röntgen / Durchstrahlung | Exzellent (99 %) | 1–2 Tage | 800–2.000 EUR | Bei Verdacht oder >15 Jahre |
| Ultraschall | Gut (85 %) | 4–6 Std. | 400–800 EUR | Alternative zu MPI |
| Dye-Penetrant-Test | Mittel (70 %) | 3–5 Std. | 200–400 EUR | Ergänzend zur visuellen Inspektion |

**Warnzeichen für verdeckte Vorstag-Korrosion:**
1. Rostfarbene Ablagerungen am unteren Profil-Anschluss
2. Unerklärlicher Vorstag-Spannungsverlust
3. Leicht erkennbare Litzenbrüche am oberen oder unteren Ende (außerhalb des Profils)
4. Alter >15 Jahre ohne dokumentierte Inspektion
5. Einsatz in tropischen Gewässern >5 Jahre

**AYDI-Empfehlung:** Vorstag alle 10–15 Jahre prophylaktisch tauschen. Die Kosten von 500–2.000 EUR für einen neuen Vorstag stehen in keinem Verhältnis zum Risiko eines plötzlichen Vorstag-Versagens auf See (Mastfall, Lebensgefahr).

### S.11 Windlast-Referenztabelle für Furler-Dimensionierung

| Windstärke (kn) | Windstärke (Bft) | Druck auf Segel (kg/m2) | Kraft auf 30-m2-Genua (kg) | Kraft auf 50-m2-Genua (kg) |
|---|---|---|---|---|
| 5 | 1–2 | 0,2 | 6 | 10 |
| 10 | 3 | 0,8 | 24 | 40 |
| 15 | 4 | 1,8 | 54 | 90 |
| 20 | 5 | 3,2 | 96 | 160 |
| 25 | 6 | 5,0 | 150 | 250 |
| 30 | 7 | 7,2 | 216 | 360 |
| 35 | 7–8 | 9,8 | 294 | 490 |
| 40 | 8 | 12,8 | 384 | 640 |

**Hinweis:** Diese Werte sind Näherungen für eine aufgetuchte Genua. Gerefftes Segel hat proportional geringere Kräfte. Die Furling-Kraft liegt typischerweise bei 5–15 % der Gesamtwindlast auf das Segel.

### S.12 Vergleichstabelle: Furler-Systeme nach Gewicht und Kosten

| System | Bootslänge | Gewicht komplett (kg) | Listenpreis (EUR) | Straßenpreis (EUR) |
|---|---|---|---|---|
| Furlex 200S | 7–10 m | 3,2 | 1.800 | 1.400–1.600 |
| Furlex 300S | 10–14 m | 5,8 | 2.600 | 2.100–2.400 |
| Furlex 400S | 14–18 m | 9,1 | 3.800 | 3.200–3.500 |
| Profurl NEX 1.0 | 7–10 m | 3,0 | 1.600 | 1.200–1.400 |
| Profurl NEX 2.0 | 10–14 m | 5,5 | 2.400 | 1.900–2.200 |
| Profurl C290 | 7–10 m | 2,9 | 1.400 | 1.100–1.300 |
| Profurl C430 | 12–16 m | 7,1 | 3.200 | 2.600–2.900 |
| Harken MKIV Unit 0 | 6–9 m | 2,4 | 1.500 | 1.200–1.400 |
| Harken MKIV Unit 1 | 8–11 m | 3,9 | 2.000 | 1.600–1.800 |
| Harken MKIV Unit 2 | 10–14 m | 6,2 | 2.800 | 2.300–2.600 |
| Harken MKIV Unit 3 | 13–17 m | 9,8 | 4.200 | 3.500–3.800 |
| Harken MKIV Unit 4 | 16–22 m | 14,5 | 6.500 | 5.500–6.000 |
| Facnor FX+ 1500 | 8–12 m | 3,8 | 1.800 | 1.400–1.600 |
| Facnor FX+ 2500 | 12–16 m | 6,5 | 3.000 | 2.500–2.800 |
| Facnor FX+ 3500 | 15–20 m | 10,2 | 4.500 | 3.800–4.200 |
| Facnor LS 170 | 10–14 m | 4,9 | 2.200 | 1.800–2.000 |
| Facnor LS 200 | 13–17 m | 7,8 | 3.500 | 2.900–3.200 |
| Karver KF3 | 6–8 m | 1,8 | 1.200 | 950–1.100 |
| Karver KF5 | 8–12 m | 2,8 | 1.800 | 1.400–1.600 |
| Karver KF7 | 12–16 m | 4,2 | 2.800 | 2.300–2.600 |
| Karver KF8 | 14–20 m | 5,5 | 3.500 | 2.900–3.200 |

**Alle Preise Stand 2025/2026, inkl. MwSt., ohne Vorstag und Montage.**

### S.13 Erweiterte Diagnose-Tabellen

#### S.13.1 Geräusch-Diagnose-Matrix

| Geräuschtyp | Frequenz | Ort | Belastungsabhängig | Wahrscheinliche Ursache | Dringlichkeit |
|---|---|---|---|---|---|
| Kratzen, kontinuierlich | Niedrig-Mittel | Drum | Ja, stärker unter Last | Lager-Pittings, Korrosion auf Laufbahnen | HOCH |
| Kratzen, intermittierend | Niedrig | Drum | Teils | Fremdkörper im Lager (Sand, Salz) | MITTEL |
| Knirschen, metall. | Mittel-Hoch | Drum oder Swivel | Ja | Trockene Lager, Fettmangel | HOCH |
| Klicken, periodisch | Mittel | Drum | Nein, bei jeder Umdrehung | Beschädigter Lagerkäfig, Delle in Laufbahn | HOCH |
| Klappern, unregelmäßig | Niedrig | Profil | Nein, bei Seegang | Lose Profilverbindung | MITTEL |
| Klappern, bei jeder Umdrehung | Mittel | Drum | Bei Drehung | Loser Sicherungsring oder Distanzstück | HOCH |
| Quietschen | Hoch | Drum oder Profil | Ja, bei Drehung | Trockene Reibung (Lager oder Luff-Tape) | MITTEL |
| Summen, tonal | Mittel-Hoch | Gesamtes Profil | Windabhängig | Windinduzierte Vibration (Aeolian Hum) | NIEDRIG |
| Summen, elektrisch | Hoch | Motor | Bei Motor-Betrieb | Motor-Bürsten, Lager | MITTEL |
| Mahlen, dumpf | Niedrig | Motor/Getriebe | Bei Last | Getriebeschaden | HOCH |
| Pfeifen | Sehr hoch | Profil | Nur bei bestimmtem Wind | Spalt in Profilverbindung oder Kanal | NIEDRIG |
| Knall, einmalig | — | Variabel | Plötzlich | Litzenbruch, Bolzenbruch, Profilbruch | KRITISCH |

#### S.13.2 Symptom-Ursache-Matrix für elektrische Furler

| Symptom | Sicherung OK? | Spannung am Motor? | Motor dreht? | Furler dreht? | Diagnose |
|---|---|---|---|---|---|
| Keine Reaktion | NEIN | — | — | — | Sicherung durchgebrannt → ersetzen, Ursache suchen |
| Keine Reaktion | JA | NEIN | — | — | Kabelbruch, Stecker-Korrosion, Relais defekt |
| Keine Reaktion | JA | JA | NEIN | — | Motor-Defekt (Wicklung, Bürsten) |
| Motor surrt | JA | JA | Versucht | NEIN | Motor blockiert oder Getriebe defekt |
| Motor dreht | JA | JA | JA | NEIN | Kupplung defekt, Getriebe ausgefallen |
| Motor dreht langsam | JA | NIEDRIG | Langsam | Langsam | Batterie schwach, Kabel zu dünn (Spannungsabfall) |
| Motor dreht langsam | JA | OK | Langsam | Langsam | Motor-Verschleiß (Bürsten), Getriebe schwergängig |
| Dreht nur eine Richtung | JA | JA | Einseitig | Einseitig | Relais/Schütz defekt (ein Relais hängt) |
| Sicherung fällt sofort | — | — | — | — | Kurzschluss im Kabel oder Motor |
| Sicherung fällt unter Last | — | — | Startet | Startet | Motor zieht zu viel Strom (Überlast, mech. Blockade) |

#### S.13.3 Symptom-Ursache-Matrix für hydraulische Furler

| Symptom | Pumpe läuft? | Ölstand OK? | Druck OK? | Leckage sichtbar? | Diagnose |
|---|---|---|---|---|---|
| Keine Reaktion | NEIN | — | — | — | Elektrische Versorgung Pumpe prüfen |
| Pumpe läuft, nichts passiert | JA | NIEDRIG | KEIN | Ja | Externe Leckage → Fittings, Schläuche |
| Pumpe läuft, nichts passiert | JA | OK | KEIN | Nein | Pumpe defekt (interne Leckage), Überdruckventil offen |
| Pumpe läuft, langsame Reaktion | JA | OK | NIEDRIG | Leicht | Interne Zylinder-Leckage (Dichtung) |
| Pumpe läuft, langsame Reaktion | JA | NIEDRIG | NIEDRIG | Ja | Externe + interne Leckage |
| Ruckartige Bewegung | JA | OK | Schwankt | Nein | Luft im System → Entlüften |
| Geräusche aus Pumpe | JA | NIEDRIG | Variabel | — | Kavitation durch Lufteintritt → Ölstand auffüllen |
| Öl schäumt | JA | — | — | — | Wasser im Öl oder massive Lufteinschlüsse → Ölwechsel |

### S.14 Wartungsprotokoll-Vorlagen für digitale Dokumentation

#### S.14.1 AYDI-kompatibles Wartungs-Datenformat

Für die digitale Erfassung in der AYDI-Plattform wird folgendes JSON-Schema empfohlen:

```json
{
  "furler_maintenance_event": {
    "boat_id": "HR40-2010-001",
    "date": "2026-04-15",
    "type": "seasonal_spring",
    "technician": "Rigger Meyer, Kiel",
    "system": {
      "manufacturer": "harken",
      "model": "MKIV Unit 3",
      "serial": "HK-MK4-3-2010-4521",
      "installation_year": 2010
    },
    "inspections": [
      {
        "component": "drum_bearing_lower",
        "condition": 2,
        "action": "lubricated",
        "lubricant": "McLube OneDrop 0860",
        "quantity_ml": 0.3,
        "notes": "Leichtgängig, kein Geräusch"
      },
      {
        "component": "foil_connectors",
        "condition": 2,
        "action": "inspected",
        "defects_found": 0,
        "notes": "Alle 8 Verbindungen OK, kein Spalt"
      },
      {
        "component": "furling_line",
        "condition": 3,
        "action": "noted_for_replacement",
        "notes": "Leichtes Pilling bei m 8-10, Austausch Herbst empfohlen"
      }
    ],
    "overall_condition": 2,
    "next_service_due": "2026-10",
    "cost_eur": 85.00,
    "confidence": "documented"
  }
}
```

#### S.14.2 QR-Code-System für Furler-Identifikation

Moderne Wartungsansätze nutzen QR-Codes am Furler für schnelle Identifikation:

**Empfohlene Position für QR-Code-Aufkleber:**
1. Innenseite der Drum-Abdeckung (geschützt vor UV)
2. Am Toggle oder Mastfuß-Beschlag (leicht zugänglich)

**QR-Code-Inhalt (empfohlen):**
```
AYDI-FURLER:v1
MFR:harken
MDL:mkiv-3
SER:HK-MK4-3-2010-4521
INST:2010
FST:1x19-10mm
LAST_SVC:2026-04-15
NEXT_SVC:2026-10
BEAR_AGE:2023
```

**Vorteile:**
- Sofortige Identifikation des Systems bei Service
- Wartungshistorie direkt verknüpfbar
- Ersatzteil-Bestellung ohne Handbuch möglich
- AYDI-App kann Wartungsempfehlungen direkt anzeigen

### S.15 Regionale Rigger-Empfehlungen (Deutschland)

| Region | Betrieb | Spezialisierung | Kontakt-Info |
|---|---|---|---|
| Kieler Förde | Yachtservice Kiel (Rigging Team) | Alle Hersteller, Regatta-Service | Kiel-Schilksee |
| Flensburger Förde | Riggerservice Flensburg | Furlex, Profurl, Selden | Flensburg-Sonwik |
| Lübecker Bucht | Hanseatische Rigger GmbH | Alle Hersteller, Superyacht-Erfahrung | Travemünde |
| Rügen/Stralsund | Rigger Nord | Furlex, Harken, Standard-Service | Stralsund |
| Bodensee | Rigg-Service Bodensee | Süßwasser-Spezialisten | Konstanz |
| Hamburg/Elbe | Hamburg Rigging | Alle Hersteller, Blauwasser-Ausrüstung | Hamburg-Wedel |
| Nordsee | Offshore Rigging Cuxhaven | Harken, Facnor, Offshore-Yachten | Cuxhaven |
| Berlin/Brandenburg | Regatta-Rigg Berlin | Karver, Harken, Regatta-Furler | Berlin-Grünau |
| Müritz/Mecklenb. Seen | Müritz-Rigg | Standard-Wartung, Furlex | Waren/Müritz |

**Stundensätze Rigger (Richtwerte 2025/2026):**
- Standard-Rigger: 65–85 EUR/Std. (netto)
- Spezialist/Meister: 85–120 EUR/Std. (netto)
- Mastbesteigung: Pauschal 80–150 EUR
- Anfahrt: 0,50–0,80 EUR/km (ab >20 km)
- Wochenend-/Feiertagszuschlag: +50 %
- Notdienst: +100 %

### S.16 Versicherungsrelevante Aspekte

**Furler-Ausfall und Versicherungsschutz:**

- **Kaskoversicherung:** Deckt Schäden am Rigg inkl. Furler durch Materialversagen, Sturm, Blitzschlag
- **Verschleiß:** NICHT versichert. Lager-Verschleiß, Korrosion durch mangelnde Wartung = Eigenrisiko
- **Folgeschäden:** Mastfall durch Vorstag-Versagen → Kaskofall (wenn kein Wartungsversäumnis nachweisbar)
- **Wartungsdokumentation:** Versicherungen können bei Großschäden Wartungsnachweise fordern
- **AYDI-Empfehlung:** Alle Wartungsmaßnahmen dokumentieren und archivieren (min. 10 Jahre)

**Typische Selbstbeteiligungen (Kasko) für Rigg-Schäden:**
- Deutschland: 500–2.500 EUR (je nach Police und Bootswert)
- Zeitwert-Abzug: Nach 10 Jahren Rigg-Alter typisch 30–50 % Abzug vom Neuwert

---

## S.17 Erweiterte Wartungsintervalle nach Einsatzprofil

### S.17.1 Regattaeinsatz (>30 Segeltage/Jahr, häufiges Bergen/Setzen)

| Komponente | Standard-Intervall | Regatta-Intervall | Begründung |
|-----------|-------------------|-------------------|------------|
| Lager-Inspektion | Jährlich | Alle 6 Monate | Höhere Zyklenbelastung |
| Trommel-Leine | 2–3 Jahre | Jährlich | Abrieb durch häufiges Reffen |
| Foil-Verbinder | 2 Jahre | Jährlich | Vibrationsbelastung |
| Oberlager | 3–5 Jahre | 2 Jahre | Dynamische Lasten bei Manövern |
| Halyard-Swivel | 2 Jahre | Jährlich | Hohe Zyklen |
| Drum-Dichtungen | 3 Jahre | 2 Jahre | Salzwasser-Exposition |
| Vorstag-Spannung | Saisonstart | Vor jeder Regatta-Serie | Kritisch für VMG |

**Regatta-spezifische Checks:**
- Torsionssteifigkeit des Profils prüfen (Messung: Verdrehwinkel bei definiertem Drehmoment)
- Lager-Spiel messen: Radialspiel >0.15mm → Austausch vor Regatta
- Endanschläge und Überdrehschutz verifizieren
- Reservefall auf Funktion prüfen
- Furling-Leine auf Abrieb inspizieren (Kern sichtbar = sofort tauschen)

### S.17.2 Blauwassereinsatz (Langfahrt, >200 Tage/Jahr)

| Komponente | Standard-Intervall | Blauwasser-Intervall | Begründung |
|-----------|-------------------|---------------------|------------|
| Lager Komplett-Service | 3–5 Jahre | 2 Jahre | Keine Werft verfügbar |
| Ersatzteil-Kit | Vorhalten | Doppelter Umfang mitführen | Verfügbarkeit Tropen |
| Vorstag-Inspektion | Jährlich | Alle 6 Monate | Ermüdung durch ständiges Segeln |
| Korrosionsschutz | Jährlich | Alle 6 Monate | Tropische Feuchtigkeit + Salz |
| UV-Schutzband | 2 Jahre | Jährlich | Höhere UV-Exposition Tropen |
| Drum-Spülung | Monatlich | Wöchentlich | Korallenstaub, Sand |

**Blauwasser-Besonderheiten:**
- Ersatzteil-Liste für Rollreffanlage als Teil der Offshore-Ausrüstung pflegen
- Kontaktdaten von Rigger-Betrieben in geplanten Anlaufhäfen recherchieren
- Notfallverfahren für Lager-Ausfall auf See trainieren
- Provisorische Reparaturmethoden beherrschen (z.B. Lager-Tausch an der Kaimauer)
- Schmiermittel und Korrosionsschutzmittel in ausreichender Menge mitführen
- Bordwerkzeug muss alle Spezialwerkzeuge für Lager-Service umfassen

### S.17.3 Chartereinsatz (Vermietung, wechselnde Crews)

| Komponente | Standard-Intervall | Charter-Intervall | Begründung |
|-----------|-------------------|-------------------|------------|
| Trommel-Inspektion | Jährlich | Alle 4 Wochen | Fehlbedienung durch unerfahrene Crews |
| Furling-Leine | 2–3 Jahre | Jährlich | Hoher Verschleiß |
| Endanschläge | Jährlich | Alle 3 Monate | Überdrehung durch Unwissenheit |
| Drum-Rastmechanismus | Jährlich | Alle 3 Monate | Fehlbedienung |
| Segel-Patches | Jährlich | Alle 6 Monate | UV-Schaden bei Dauerbelegung |

**Charter-spezifische Maßnahmen:**
- Farbliche Markierungen an der Furling-Leine (Reff 1, Reff 2, Vollgeborgen)
- Laminierte Bedienungsanleitung im Cockpit anbringen
- Endanschläge auf Ratschen-System umrüsten (verhindert Überdrehung)
- Trommel mit verstärktem Leinenführer (Edelstahl statt Kunststoff)
- Automatische Rückholfedern für Furling-Leinen installieren

---

## S.18 Detaillierte Schadensdokumentation für Versicherungen

### S.18.1 Dokumentationsanforderungen

Versicherungen verlangen bei Schäden an Rollreffanlagen eine lückenlose Dokumentation.

**Pflichtdokumentation bei Schadensmeldung:**
1. **Datum und Uhrzeit** des Schadensereignisses
2. **Wetterbedingungen** (Wind in Beaufort, Seegang, Temperatur)
3. **Segelbelegung** zum Zeitpunkt des Schadens (Segelgröße, Reffstellung)
4. **Handlungsablauf** (Was wurde unmittelbar vor dem Schaden getan?)
5. **Schadensort** (GPS-Position, Revier)
6. **Sofortmaßnahmen** nach dem Schaden
7. **Fotodokumentation** (Mindestens 10 Fotos aus verschiedenen Winkeln)
8. **Zeugenaussagen** (falls vorhanden)

### S.18.2 Foto-Dokumentationsstandard

| Foto-Nr | Motiv | Wichtige Details |
|---------|-------|-----------------|
| 1 | Gesamtansicht Rollreffanlage | Zustand des gesamten Systems |
| 2 | Schadensbereich Übersicht | Mit Maßstab (Lineal, Münze) |
| 3 | Schadensbereich Detail | Nahaufnahme der Beschädigung |
| 4 | Trommel/Drum | Zustand, Position der Leine |
| 5 | Oberlager/Swivel | Zustand, Risse, Verformung |
| 6 | Vorstag-Anschluss oben | Toggle, Gabel, Bolzen |
| 7 | Vorstag-Anschluss unten | Spanner, Gabel, Bolzen |
| 8 | Foilprofil | Verbinder, Verformung, Brüche |
| 9 | Segel am Vorstag | Zustand der Segelbefestigung |
| 10 | Typenschild | Hersteller, Modell, Seriennummer |

### S.18.3 Schadensbewertung und Ersatzkosten

**Typische Schadensszenarien und Versicherungsleistung:**

| Schadenstyp | Ursache | Versichert (Kasko) | Versichert (Haftpflicht) | Typische Kosten |
|------------|---------|-------------------|------------------------|-----------------|
| Lager-Ausfall | Verschleiß | Nein (Verschleiß) | Nein | €300–€800 |
| Lager-Ausfall | Sturmschaden | Ja | Nein | €300–€800 |
| Foil-Bruch | Materialermüdung | Teilweise | Nein | €1.500–€4.000 |
| Foil-Bruch | Kollision | Ja | Ggf. Verursacher | €1.500–€4.000 |
| Vorstag-Bruch | Korrosion (vernachlässigt) | Nein (mangelnde Wartung) | Nein | €3.000–€8.000 |
| Vorstag-Bruch | Sturmschaden | Ja | Nein | €3.000–€8.000 |
| Gesamt-Totalschaden | Rigg-Verlust | Ja | Nein | €8.000–€25.000 |
| Drum zerstört | Leinenbruch + Peitschen | Ja | Nein | €600–€2.500 |

**Wartungsnachweis als Versicherungsvoraussetzung:**
- Viele Kaskoversicherungen verlangen jährlichen Rigg-Check durch zertifizierten Rigger
- Ohne Wartungsnachweis kann Versicherung Leistung kürzen oder verweigern
- AYDI-Wartungsprotokolle als anerkannter Nachweis (Signatur des Durchführenden)
- Empfehlung: Alle 5 Jahre Rigg-Gutachten durch Sachverständigen

---

## S.19 Elektrische und Hydraulische Furler — Erweiterte Wartung

### S.19.1 Elektrische Furler-Antriebe

**Hersteller und Modelle:**

| Hersteller | Modell | Motortyp | Spannung | Max. Vorstag | Leistung |
|-----------|--------|----------|----------|-------------|----------|
| Furlex | E-Drive | Brushless DC | 12V/24V | 12mm | 250W |
| Profurl | E-Cruise | Brushless DC | 12V/24V | 14mm | 350W |
| Harken | Unit 0 E | Brushless DC | 12V/24V | 10mm | 200W |
| Reckmann | FS | Brushless DC | 24V | 16mm | 500W |
| Bamar | V60E | Brushless DC | 12V/24V | 14mm | 300W |

> ⚠️ **ZU PRÜFEN (Audit):** Motortyp „Brushless DC" (Tabelle oben) widerspricht der Bürsten-Wartung „Motor-Bürsten alle 500 h prüfen (min. 8 mm)" (Tabelle unten) sowie den Bürsten-Ausfällen in F-15_04-11 und FAQ 23. Bürstenlose (brushless) Motoren haben konstruktiv keine Kohlebürsten — entweder die Motortyp-Angabe oder die Bürsten-Wartung ist je Modell falsch. Motortyp anhand der Herstellerdaten je Modell verifizieren; Angabe nicht gesichert.

**Wartungsintervalle Elektrische Antriebe:**

| Komponente | Intervall | Prüfung |
|-----------|-----------|---------|
| Motor-Bürsten | 500 Betriebsstunden | Länge messen (min. 8mm) |
| Getriebe-Schmierung | Jährlich | Getriebeöl prüfen/wechseln |
| Kabelverbindungen | Halbjährlich | Korrosion, Wackelkontakt |
| Endschalter | Jährlich | Funktion und Justierung |
| Magnetbremse | Jährlich | Haltemoment prüfen |
| Steuereinheit | Jährlich | Fehlerspeicher auslesen |
| Sicherungen | Halbjährlich | Wert und Zustand |

**Fehlerdiagnose Elektrischer Furler:**

| Symptom | Mögliche Ursache | Diagnose | Lösung |
|---------|-----------------|----------|--------|
| Motor dreht nicht | Sicherung | Multimeter an Sicherung | Sicherung tauschen |
| Motor dreht nicht | Kabelbruch | Durchgangsprüfung | Kabel reparieren |
| Motor dreht langsam | Unterspannung | Spannung am Motor messen | Batterie laden, Querschnitt prüfen |
| Motor dreht, Segel bewegt nicht | Getriebe defekt | Getriebe öffnen | Zahnräder tauschen |
| Motor stoppt unter Last | Überstromschutz | Strom messen | Mechanischen Widerstand suchen |
| Unregelmäßige Drehzahl | Bürstenverschleiß | Bürsten inspizieren | Bürsten tauschen |
| Endposition nicht korrekt | Endschalter verstellt | Schalter prüfen | Neu justieren |
| Steuerung reagiert nicht | Elektronik defekt | Fehlerspeicher auslesen | Steuereinheit tauschen |

### S.19.2 Hydraulische Furler-Antriebe

**Typische Systeme (Superyacht, >20m):**

| Hersteller | Modell | Druck | Volumenstrom | Max. Vorstag |
|-----------|--------|-------|-------------|-------------|
| Reckmann | HS-Serie | 200 bar | 8–25 l/min | 22mm |
| Profurl | Hydra | 180 bar | 6–20 l/min | 20mm |
| Rondal | Custom | 250 bar | 10–30 l/min | 26mm |
| Cariboni | Hydro | 200 bar | 8–22 l/min | 22mm |

**Hydraulik-Wartungsprotokoll:**

| Komponente | Intervall | Prüfung/Maßnahme |
|-----------|-----------|-----------------|
| Hydrauliköl | Jährlich | Partikelzählung, Wassergehalt |
| Ölfilter | 500h oder jährlich | Tauschen |
| Dichtungen Zylinder | 2 Jahre | Leckage-Inspektion |
| Schläuche | Jährlich | Risse, Alterung, Scheuerstellen |
| Pumpe | Jährlich | Fördermenge, Druckaufbau |
| Ventilblock | 2 Jahre | Funktion aller Ventile |
| Druckspeicher | Jährlich | Vordruck prüfen |

**Hydrauliköl-Spezifikationen:**
- ISO VG 32 oder VG 46 (herstellerabhängig)
- Wassergehalt: max. 0.1% (500 ppm)
- Partikelklasse: ISO 4406 max. 18/16/13
- Ölwechsel: alle 2.000 Betriebsstunden oder 3 Jahre
- Füllmenge: typisch 5–15 Liter je nach Systemgröße

### S.19.3 Kabelquerschnitte für Elektrische Furler

| Kabellänge (m) | 12V / 20A | 12V / 30A | 24V / 15A | 24V / 20A |
|----------------|-----------|-----------|-----------|-----------|
| 5 | 6 mm² | 10 mm² | 4 mm² | 6 mm² |
| 10 | 10 mm² | 16 mm² | 6 mm² | 10 mm² |
| 15 | 16 mm² | 25 mm² | 10 mm² | 16 mm² |
| 20 | 25 mm² | 35 mm² | 16 mm² | 25 mm² |

*Spannungsabfall max. 3% (ISO 13297)*

---

## S.20 Historische Entwicklung der Rollreffanlagen

### S.20.1 Meilensteine

| Jahr | Entwicklung | Bedeutung |
|------|-----------|-----------|
| 1969 | Stearn/Schaefer Roller Furling | Erstes kommerzielles System für Yachten |
| 1975 | Hood Seafurl | Erster Profilstag für Rollreff |
| 1978 | Furlex (Seldén) Markteinführung | Skandinavisches Qualitätsprodukt |
| 1982 | Profurl Markteinführung | Französische Innovation mit Dual-Groove |
| 1985 | Harken Roller Furling | Hochleistungs-System aus den USA |
| 1990 | Facnor Markteinführung | Kompakte Bauweise, gutes P/L-Verhältnis |
| 1995 | Erste elektrische Furler | Reckmann Superyacht-Systeme |
| 2000 | Karver Markteinführung | Leichtbau für Regatta |
| 2005 | Code 0 Furler | Spezial-Furler für asymmetrische Segel |
| 2010 | Continuous-Line Drum | Vereinfachte Bedienung |
| 2015 | Carbonfoil-Systeme | Gewichtsersparnis im Topp |
| 2018 | App-gesteuerte E-Furler | Digitale Integration |
| 2020 | Hybrid-Furler (manuell + elektrisch) | Redundanz für Blauwasser |
| 2023 | KI-gestützte Wartungsplanung | Predictive Maintenance (AYDI) |

### S.20.2 Technologietrends

**Aktuelle Entwicklungen (2024–2026):**
- Integration von Sensoren in Lager (Temperatur, Vibration, Drehzahl)
- Predictive Maintenance durch Datenanalyse (AYDI-Kernkompetenz)
- Carbonfoil als Standard bei Regatta-Systemen
- Lithium-Akku-betriebene kabellose E-Furler
- 3D-gedruckte Ersatzteile für Drum-Komponenten
- Selbstschmierende Lager mit PTFE-Beschichtung

**Zukünftige Entwicklungen:**
- Vollautomatische Reffanlagen mit Windmesser-Kopplung
- KI-gesteuerte Segelform-Optimierung durch variierbares Reffen
- IoT-Fernüberwachung von Rollreffanlagen über Satellit
- Biologisch abbaubare Schmierstoffe speziell für Marine-Lager

---

## S.21 Checklisten als Kopiervorlagen

### S.21.1 Vorsaison-Checkliste Rollreffanlage

```
VORSAISON-CHECK ROLLREFFANLAGE
Datum: ___________  Boot: ___________  Anlage: ___________

□ Segel ausrollen und auf Schäden inspizieren
□ UV-Schutzband auf Verschleiß prüfen
□ Furling-Leine auf Abrieb prüfen
□ Trommel drehen — Leichtgängigkeit bewerten
  Bewertung: □ leichtgängig  □ schwergängig  □ blockiert
□ Geräusche beim Drehen: □ keine  □ leicht  □ deutlich
□ Foilprofil auf Geradheit sichtprüfen
□ Foil-Verbinder auf festen Sitz prüfen
□ Oberlager/Swivel: Drehwiderstand prüfen
□ Vorstag-Spannung prüfen (Durchhang max. ____mm bei ____m)
□ Vorstag auf Drahtbrüche inspizieren (visuell + Lappen-Test)
□ Drum-Leinenführung auf Verschleiß prüfen
□ Endanschläge auf Funktion testen
□ Alle Bolzen und Splinte auf festen Sitz prüfen
□ Korrosionsspuren dokumentieren
□ Schmierstellen versorgen (McLube OneDrop / Harken Pawl Oil)

Gesamtbewertung: □ einsatzbereit  □ Nacharbeit nötig  □ Werft erforderlich
Durchgeführt von: ___________  Unterschrift: ___________
```

### S.21.2 Nachsaison-Checkliste Rollreffanlage

```
NACHSAISON-CHECK ROLLREFFANLAGE
Datum: ___________  Boot: ___________  Anlage: ___________

□ Segel vollständig ausrollen
□ Gesamtes System mit Süßwasser abspülen (30 min einwirken lassen)
□ Trommel öffnen — Innenleben auf Korrosion prüfen
□ Trommel-Leine entnehmen und waschen
□ Lager schmieren (McLube OneDrop)
□ Foilprofil komplett auf Korrosion inspizieren
□ Vorstag-Anschlüsse mit Korrosionsschutz behandeln
□ Alle Edelstahl-Teile mit Tef-Gel behandeln
□ Segel abnehmen und trocken lagern (oder UV-Schutz prüfen)
□ Drum-Öffnung gegen Feuchtigkeit abdecken
□ Falls E-Furler: Batterie abklemmen, Motor konservieren
□ Wartungsbedarf für nächste Saison notieren

Festgestellte Mängel:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________

Nächste Saison zu erledigen:
1. ___________________________________________
2. ___________________________________________

Durchgeführt von: ___________  Unterschrift: ___________
```

### S.21.3 Lager-Service-Protokoll

```
LAGER-SERVICE PROTOKOLL
Datum: ___________  Boot: ___________
Anlage: ___________  Hersteller: ___________  Modell: ___________

UNTERLAGER:
  Lager-Typ: □ Kugellager  □ Nadellager  □ Gleitlager
  Lager-Nr: ___________  Hersteller-Teilenr: ___________
  Zustand alt: □ gut  □ Spiel  □ rau  □ blockiert
  Maßnahme: □ geschmiert  □ gereinigt  □ getauscht
  Spiel gemessen: _____ mm (max. zulässig: _____ mm)

OBERLAGER / SWIVEL:
  Lager-Typ: □ Kugellager  □ Nadellager  □ Gleitlager
  Lager-Nr: ___________  Hersteller-Teilenr: ___________
  Zustand alt: □ gut  □ Spiel  □ rau  □ blockiert
  Maßnahme: □ geschmiert  □ gereinigt  □ getauscht
  Spiel gemessen: _____ mm (max. zulässig: _____ mm)

Schmierstoff verwendet: ___________
Drehmomente: Lager-Mutter _____ Nm, Drum-Mutter _____ Nm

Bemerkungen: ___________________________________________

Nächster Service fällig: ___________
Durchgeführt von: ___________  Unterschrift: ___________
```

## ANHANG I–R: Pydantic v2 Modelle

```python
"""
AYDI Pydantic v2 Modelle für Rollreffanlagen-Wartung (15_04)

WICHTIG: Verwendet model_config = {"from_attributes": True}
NIEMALS class Config verwenden!
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class FurlerManufacturer(str, Enum):
    """Hersteller von Rollreffanlagen."""
    FURLEX_SELDEN = "furlex_selden"
    PROFURL = "profurl"
    HARKEN = "harken"
    FACNOR = "facnor"
    KARVER = "karver"
    RONSTAN = "ronstan"
    BAMAR = "bamar"
    RECKMANN = "reckmann"
    OTHER = "other"


class FurlerType(str, Enum):
    """Typ der Rollreffanlage."""
    HEADSAIL = "headsail"
    IN_MAST = "in_mast"
    IN_BOOM = "in_boom"
    CODE_0 = "code_0"
    GENNAKER = "gennaker"


class DriveType(str, Enum):
    """Antriebsart des Furlers."""
    MANUAL = "manual"
    ELECTRIC = "electric"
    HYDRAULIC = "hydraulic"


class BearingType(str, Enum):
    """Lagertyp."""
    BALL_BEARING = "ball_bearing"
    NEEDLE_BEARING = "needle_bearing"
    TORLON_SLEEVE = "torlon_sleeve"
    PTFE_SLEEVE = "ptfe_sleeve"


class ConditionRating(int, Enum):
    """Zustandsbewertung 1-5."""
    EXCELLENT = 1
    GOOD = 2
    ACCEPTABLE = 3
    POOR = 4
    CRITICAL = 5


class SeverityLevel(int, Enum):
    """Schweregrad 1-5."""
    LOW = 1
    MODERATE = 2
    ELEVATED = 3
    HIGH = 4
    CRITICAL = 5


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


class FurlerMaintenanceRecord(BaseModel):
    """Hauptmodell für einen Furler-Wartungsdatensatz."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    boat_id: int = Field(..., description="Referenz zum Boot")
    furler_manufacturer: FurlerManufacturer
    furler_model: str = Field(..., description="z.B. 'Furlex 300S', 'NEX 2.0'")
    furler_type: FurlerType
    drive_type: DriveType = DriveType.MANUAL
    installation_year: Optional[int] = None
    forestay_diameter_mm: Optional[float] = None
    forestay_material: Optional[str] = None
    last_full_service_date: Optional[date] = None
    last_bearing_change_date: Optional[date] = None
    last_forestay_change_date: Optional[date] = None
    total_service_hours: float = 0.0
    overall_condition: ConditionRating = ConditionRating.GOOD
    notes: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BearingInspection(BaseModel):
    """Inspektion eines einzelnen Lagers."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    position: str = Field(..., description="z.B. 'drum_lower', 'drum_upper', 'swivel'")
    bearing_type: BearingType
    bearing_size: Optional[str] = Field(None, description="z.B. '6004-2RS'")
    bearing_material: Optional[str] = Field(None, description="z.B. 'AISI 440C', '316L'")
    axial_play_mm: Optional[float] = None
    radial_play_mm: Optional[float] = None
    rotation_resistance_nm: Optional[float] = None
    noise_level: ConditionRating = ConditionRating.GOOD
    corrosion_level: ConditionRating = ConditionRating.GOOD
    overall_condition: ConditionRating = ConditionRating.GOOD
    action_taken: Optional[str] = Field(
        None, description="z.B. 'lubricated', 'replaced', 'none'"
    )
    replacement_part_number: Optional[str] = None
    replacement_cost_eur: Optional[float] = None
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
    inspection_date: date = Field(default_factory=date.today)
    notes: Optional[str] = None


class FoilCondition(BaseModel):
    """Zustandsbewertung des Profilstags."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    total_sections: int = Field(..., ge=1, description="Gesamtzahl Profilsektionen")
    sections_inspected: int = Field(..., ge=0)
    sections_with_damage: int = Field(0, ge=0)
    connectors_total: int = Field(..., ge=0)
    connectors_replaced: int = Field(0, ge=0)
    straightness_ok: bool = True
    max_deviation_mm_per_m: Optional[float] = None
    channel_condition: ConditionRating = ConditionRating.GOOD
    anodizing_condition: ConditionRating = ConditionRating.GOOD
    corrosion_spots: int = Field(0, ge=0)
    overall_condition: ConditionRating = ConditionRating.GOOD
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
    inspection_date: date = Field(default_factory=date.today)
    notes: Optional[str] = None


class DrumServiceRecord(BaseModel):
    """Service-Protokoll der Trommeleinheit."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    drum_opened: bool = False
    seals_condition: ConditionRating = ConditionRating.GOOD
    seals_replaced: bool = False
    housing_condition: ConditionRating = ConditionRating.GOOD
    uv_damage_visible: bool = False
    line_guide_condition: ConditionRating = ConditionRating.GOOD
    line_guide_replaced: bool = False
    furling_line_condition: ConditionRating = ConditionRating.GOOD
    furling_line_replaced: bool = False
    furling_line_diameter_mm: Optional[float] = None
    furling_line_length_m: Optional[float] = None
    torque_specs_checked: bool = False
    overall_condition: ConditionRating = ConditionRating.GOOD
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
    service_date: date = Field(default_factory=date.today)
    notes: Optional[str] = None


class LubricationLog(BaseModel):
    """Schmierungsprotokoll."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    lubrication_date: date = Field(default_factory=date.today)
    component: str = Field(
        ..., description="z.B. 'drum_bearing', 'swivel_bearing', 'foil_channel'"
    )
    lubricant_product: str = Field(
        ..., description="z.B. 'McLube OneDrop 0860', 'Harken Pawl Oil BK4521'"
    )
    lubricant_quantity_ml: Optional[float] = None
    application_method: str = Field(
        "drops", description="z.B. 'drops', 'spray', 'grease_gun', 'manual'"
    )
    previous_lubrication_date: Optional[date] = None
    condition_before: Optional[ConditionRating] = None
    condition_after: Optional[ConditionRating] = None
    notes: Optional[str] = None


class TroubleshootingCase(BaseModel):
    """Troubleshooting-Fall für die AYDI-Analyse."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    failure_pattern_id: str = Field(
        ..., description="z.B. 'F-15_04-01' bis 'F-15_04-12'"
    )
    severity: SeverityLevel
    reported_symptoms: str
    diagnosed_cause: Optional[str] = None
    repair_actions: Optional[str] = None
    repair_cost_eur: Optional[float] = None
    repair_duration_hours: Optional[float] = None
    parts_used: Optional[list[str]] = None
    resolved: bool = False
    resolution_date: Optional[date] = None
    preventive_measures: Optional[str] = None
    recurrence_risk: Optional[str] = Field(
        None, description="'low', 'medium', 'high'"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
    reported_date: date = Field(default_factory=date.today)
    notes: Optional[str] = None


class SeasonalProtocol(BaseModel):
    """Saisonales Wartungsprotokoll."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    maintenance_record_id: int
    protocol_type: str = Field(
        ..., description="'spring_commissioning', 'summer_check', 'winterization'"
    )
    season_year: int
    protocol_date: date = Field(default_factory=date.today)
    checklist_items_total: int = Field(..., ge=1)
    checklist_items_completed: int = Field(0, ge=0)
    checklist_items_failed: int = Field(0, ge=0)
    issues_found: Optional[list[str]] = None
    actions_taken: Optional[list[str]] = None
    next_maintenance_due: Optional[date] = None
    performed_by: Optional[str] = None
    signed_off: bool = False
    overall_assessment: ConditionRating = ConditionRating.GOOD
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
    notes: Optional[str] = None


class SparePartInventory(BaseModel):
    """Ersatzteil-Inventar an Bord."""

    model_config = {"from_attributes": True}

    id: Optional[int] = None
    boat_id: int
    part_description: str = Field(
        ..., description="z.B. 'Furlex 300S Bearing Kit'"
    )
    part_number: Optional[str] = Field(
        None, description="z.B. '507-956-01'"
    )
    manufacturer: Optional[FurlerManufacturer] = None
    compatible_models: Optional[list[str]] = Field(
        None, description="z.B. ['Furlex 300S', 'Furlex 300S Mk2']"
    )
    quantity_on_board: int = Field(1, ge=0)
    quantity_minimum: int = Field(1, ge=0)
    purchase_date: Optional[date] = None
    purchase_price_eur: Optional[float] = None
    supplier: Optional[str] = None
    storage_location: Optional[str] = Field(
        None, description="z.B. 'Backbord-Backskiste', 'Werkzeugschapp'"
    )
    expiry_date: Optional[date] = Field(
        None, description="Falls relevant (z.B. Schmierstoffe)"
    )
    reorder_needed: bool = False
    notes: Optional[str] = None
```

---

*Ende der AYDI Wissensdatei 15.04 — Rollreffanlagen – Wartung, Service und Troubleshooting*
*Letzte Aktualisierung: 2026-04*
*Nächste geplante Überarbeitung: 2026-10*
