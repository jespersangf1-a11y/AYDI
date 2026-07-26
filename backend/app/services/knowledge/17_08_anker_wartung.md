---
titel: "Ankersysteme — Wartung, Inspektion und Troubleshooting"
kategorie: "Anker und Kette"
unterkategorie: "Wartung und Troubleshooting"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 17_08 — Ankersysteme — Wartung, Inspektion und Troubleshooting

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Wartungsplan komplett](#2-wartungsplan-komplett)
3. [Ketten-Inspektion](#3-ketten-inspektion)
4. [Anker-Inspektion](#4-anker-inspektion)
5. [Windlass-Wartung](#5-windlass-wartung)
6. [Galvanisierung](#6-galvanisierung)
7. [Korrosionsschutz](#7-korrosionsschutz)
8. [Ersatzteile und Bezugsquellen](#8-ersatzteile-und-bezugsquellen)
9. [Bordwerkzeug für Ankersystem](#9-bordwerkzeug-für-ankersystem)
10. [Fehlerbild-Atlas](#10-fehlerbild-atlas)
11. [Troubleshooting](#11-troubleshooting)
12. [FAQ](#12-faq)
13. [Glossar](#13-glossar)
14. [Schnell-Referenz](#14-schnell-referenz)
15. [ANHANG A–H: Fallstudien](#15-anhang-ah-fallstudien)
16. [ANHANG I–R: Pydantic v2 Datenmodelle](#16-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Zweck dieses Dokuments

Dieses Dokument bildet die zentrale Wissensbasis für die Wartung, Inspektion
und Fehlerbehebung aller Komponenten des Ankersystems auf Yachten. Es dient
der AYDI-Analyse-Engine als Referenz zur Bewertung des Wartungszustands,
zur Generierung von Wartungsempfehlungen und zur systematischen Diagnose
von Fehlerbildern im Ankersystem.

Ein gut gewartetes Ankersystem ist die Grundvoraussetzung für sicheres
Ankern. Statistiken zeigen, dass die Mehrheit aller Ankerversager nicht
auf falsche Dimensionierung, sondern auf mangelhafte Wartung zurückzuführen
ist:

- **ADAC-Auswertung 2024**: 62 % aller ankerbezogenen Hilfeleistungen
  hatten eine wartungsbedingte Ursache (korrodierte Kette, blockierte
  Winde, defekter Schäkel).
- **Pantaenius-Schadenstatistik 2023**: Durchschnittlicher Schaden durch
  Ankerversagen: 14.800 EUR. Über 70 % hätten durch regelmäßige
  Inspektion verhindert werden können.
- **BSH-Unfallberichte 2022–2024**: Korrodierte Kettenverbindungsglieder
  sind die häufigste Einzelursache für Kettenverlust.

### 1.2 Systemkomponenten im Überblick

Das Ankersystem einer Yacht besteht aus folgenden Hauptkomponenten, die
jeweils eigene Wartungsanforderungen haben:

| Komponente | Funktion | Wartungsintensität | Lebensdauer |
|-----------|----------|-------------------|-------------|
| Anker | Halteorgan am Grund | Niedrig | 15–30 Jahre |
| Kette | Kraftübertragung, Gewicht | Mittel | 8–15 Jahre |
| Windlass (Ankerwinsch) | Mechanisiertes Hieven/Fieren | Hoch | 10–20 Jahre |
| Wirbel/Swivel | Verdrehungskompensation | Mittel | 5–10 Jahre |
| Bugrolle/Klüse | Führung und Lagerung | Niedrig | 15–25 Jahre |
| Snubber/Ruckdämpfer | Stoßdämpfung bei Last | Hoch (Verschleißteil) | 3–7 Jahre |
| Kettenkasten | Lagerung der Kette | Niedrig–Mittel | Schiffslebenszeit |
| Schäkel/Verbindungsglieder | Verbindung der Komponenten | Hoch (Sicherheitskritisch) | 5–10 Jahre |
| Kettenstopper | Sichern der Kette unter Last | Mittel | 10–15 Jahre |

### 1.3 Wartungsphilosophie

Die Wartung des Ankersystems folgt dem Prinzip der zustandsbasierten
Instandhaltung (Condition-Based Maintenance, CBM) mit festen
Mindestintervallen:

1. **Feste Intervalle** — Mindestens einmal jährlich (Pre-Season)
   vollständige Inspektion aller Komponenten.
2. **Zustandsbasiert** — Zusätzliche Inspektion nach Extrembelastungen
   (Sturmankern, Grundberührung, Festsitz-Anker).
3. **Opportunistisch** — Jedes Ankermanöver als Sichtprüfung nutzen.
4. **Lebensdauerbasiert** — Komponenten mit definierter Lebensdauer
   (Snubber, Schäkel) präventiv tauschen.

### 1.4 Relevanz für die AYDI-Analyse

Innerhalb der AYDI-Analyse wird der Wartungszustand des Ankersystems in
folgenden Modulen bewertet:

- **Materialanalyse**: Korrosionszustand, Galvanisierung, Materialermüdung
- **Compliance**: Sicherheitsrelevante Befunde, CE-Konformität
- **Kostenanalyse**: Lifecycle-Kosten, anstehende Ersatzinvestitionen
- **Wartungsanalyse**: Wartungsintervalle, Befundbewertung, Maßnahmenplanung
- **Visuell**: Fotodokumentation des Zustands, Korrosionserkennung

### 1.5 Confidence-Level-Zuordnung

| Datenquelle | Confidence-Level | Beispiel |
|-------------|-----------------|----------|
| Messung vor Ort (Messschieber, Multimeter) | `measured` | Glieddicke 7,2 mm (Nenn 8 mm = 90 %) |
| Foto der Kette / des Ankers | `visual_high` bis `visual_low` | Rost erkennbar, Galvanisierung beurteilt |
| Herstellerzertifikat (Datum, Charge) | `documented` | Kette verzinkt 2021, DIN 766, 10 mm |
| Bootsklasse-Schätzung | `estimated` | Wartungsintervall typisch für 12m-Segler |
| Servicebericht Werft | `documented` | Winde überholt 2024, Öl gewechselt |
| Eigentümerangabe (mündlich) | `estimated` | „Kette ist ca. 5 Jahre alt" |

### 1.6 Normative Grundlagen für Wartung und Inspektion

| Norm / Richtlinie | Inhalt | Relevanz |
|-------------------|--------|----------|
| DIN 766 | Rundstahlkette kurzgliedrig | Maße, Toleranzen, Ablegereife |
| DIN 764 | Rundstahlkette langgliedrig | Alternative Kettenspezifikation |
| ISO 4565:1986 | Ankerketten für Kleinfahrzeuge | Dimensionierung, Materialanforderungen |
| ISO 15084:2003 | Starke Punkte — Ankern, Vertäuen, Schleppen | Belastungsgrenzwerte |
| EN ISO 1461 | Feuerverzinkung | Mindestschichtdicken, Prüfverfahren |
| ASTM A153 | Verzinkung von Eisenwaren | US-Standard, relevant für Import-Ketten |
| ABYC H-40 | Ankern, Vertäuen, starke Punkte | US-Standard für Ankergeschirr und Kettenstopper |

### 1.7 Saisonale Einordnung

| Zeitraum | Phase | Schwerpunkt |
|----------|-------|-------------|
| März–April | Pre-Season | Vollinspektion, Inbetriebnahme |
| Mai–Oktober | In-Season | Betriebsüberwachung, Sichtprüfungen |
| November–Dezember | Winterization | Konservierung, Einlagerung |
| Januar–Februar | Off-Season | Überholung, Ersatzteilbestellung |

---

## 2. Wartungsplan komplett

### 2.1 Pre-Season-Wartung (März–April)

Die Pre-Season-Wartung ist die umfassendste Wartungsmaßnahme des Jahres.
Sie umfasst die Inspektion und Instandsetzung aller Komponenten des
Ankersystems vor Beginn der Saison.

#### 2.1.1 Anker — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| A-01 | Schweißnähte (alle) | Sichtprüfung, Lupe 10× | Kein Riss, keine Porosität | Schweißen lassen oder Anker ersetzen |
| A-02 | Galvanisierung | Sichtprüfung, Magnet | >70 % intakt, kein Flächenrost | Neuverzinken oder Zinkspray |
| A-03 | Schaftgeradheit | Schaft auf flache Fläche legen | Abweichung <2 mm/m | Richten lassen oder ersetzen |
| A-04 | Bewegliche Teile (Flunken, Bügel) | Handbewegung, Spiel prüfen | Leichtgängig, kein Exzessiv-Spiel | Reinigen, schmieren, ggf. Bolzen ersetzen |
| A-05 | Schäkelöse / Verbindungspunkt | Sichtprüfung, Maß prüfen | Kein Verschleiß >10 %, kein Riss | Ersetzen |
| A-06 | Gewicht (optional) | Waage | ±5 % vom Nenngewicht | Bei Masseverlust: Material abgetragen → ersetzen |
| A-07 | Spitze / Flunke-Schärfe | Sichtprüfung, Fingernagel | Keine stumpfe Kante, kein Grat | Nachschleifen (Flex, Feile) |
| A-08 | Beschriftung / Typenschild | Sichtprüfung | Lesbar | Dokumentation aktualisieren |

#### 2.1.2 Kette — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| K-01 | Glieddicke (min. 5 Stellen) | Messschieber | ≥90 % Nenndicke | Kette ersetzen (Abschnitt oder gesamt) |
| K-02 | Teilung (10 Glieder messen) | Messschieber, Maßband | ≤103 % Nenn-Teilung | Kette ersetzen |
| K-03 | Verdrehte Glieder | Sichtprüfung, Kette auslegen | Kein Glied >15° verdreht | Defekten Abschnitt ersetzen |
| K-04 | Galvanisierung | Sichtprüfung | >50 % der Oberfläche intakt | Neuverzinken oder ersetzen |
| K-05 | Rostbildung | Sichtprüfung | Nur Flugrost, kein Lochfraß | Entrosten + Zinkspray oder ersetzen |
| K-06 | Verbindungsglieder / Schäkel | Sicht + Maß | Sicherung vorhanden, kein Verschleiß | Ersetzen |
| K-07 | Markierungen (5m / 10m) | Sichtprüfung | Alle Markierungen vorhanden | Neu markieren (Kabelbinder, Farbe, Draht) |
| K-08 | Endglied / Kettenend-Befestigung | Sichtprüfung | Gesichert, kein Rost | Befestigung erneuern, Sicherung prüfen |
| K-09 | Kettennuss-Kompatibilität | 3m Kette über Nuss laufen lassen | Sauberer Eingriff, kein Spiel | Kette oder Nuss tauschen |
| K-10 | Kette ausspülen | Süßwasser, Hochdruckreiniger | Kein Sand, Schlick, Muscheln | Gründlich reinigen |

#### 2.1.3 Windlass — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| W-01 | Äußere Sichtprüfung | Sichtkontrolle | Kein Rost, kein Gehäuseriss | Reinigen, behandeln, ggf. Hersteller kontaktieren |
| W-02 | Motorraum / Unterdeck-Zugang | Luke öffnen | Trocken, sauber, kein Rost | Trocknen, Ursache für Feuchtigkeit finden |
| W-03 | Getriebeöl prüfen | Ölstandsschraube, Sichtglas | Öl klar, Niveau ok | Ölwechsel durchführen |
| W-04 | Kohlebürsten prüfen | Motor öffnen (4 Schrauben) | Bürstenlänge >5 mm | Kohlebürsten ersetzen |
| W-05 | Elektrische Verbindungen | Sichtprüfung, Wackeltest | Fest, kein Grünspan, kein Abbrand | Säubern, neu befestigen, Kontaktfett |
| W-06 | Kupplung / Clutch | Betätigung, Spiel prüfen | Leichtgängig, hält sicher | Reinigen, schmieren, ggf. Belag ersetzen |
| W-07 | Wellendichtung | Sichtprüfung auf Leckage | Trocken, kein Wasser im Motor | Dichtung ersetzen |
| W-08 | Fußschalter | Funktion + Dichtigkeit prüfen | Schaltet sicher, kein Wasser | Membran ersetzen oder Schalter tauschen |
| W-09 | Solenoid | Funktion prüfen (Klick hörbar) | Schaltet sicher, kein Abbrand | Solenoid ersetzen |
| W-10 | Kettennuss | Zahnprofil prüfen | Kein sichtbarer Verschleiß | Kettennuss ersetzen |
| W-11 | Spillkopf (falls vorhanden) | Oberfläche prüfen | Keine Riefen, kein Grat | Reinigen, ggf. ersetzen |
| W-12 | Probelauf | 5 m Kette ein/aus unter Last | Gleichmäßiger Lauf, keine Geräusche | Fehlersuche starten |

#### 2.1.4 Wirbel / Swivel — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| S-01 | Drehbarkeit | Von Hand drehen | Leichtgängig, kein Knarzen | Reinigen, schmieren (Tef-Gel) |
| S-02 | Verschleiß Drehachse | Sichtprüfung, Spiel fühlen | Kein seitliches Spiel >1 mm | Ersetzen |
| S-03 | Galvanisierung / Korrosion | Sichtprüfung | Keine Lochfraß-Stellen | Ersetzen |
| S-04 | Schäkelverbindungen | Sichtprüfung, Drehmoment | Bolzen gesichert, kein Verschleiß | Schäkel ersetzen |
| S-05 | Bruchlast-Kennzeichnung | Beschriftung lesen | WLL/SWL ≥ Kettenstärke | Upgraden |
| S-06 | Materialtyp | Magnettest (316L = nicht magnetisch) | Edelstahl 316L oder verzinkter Stahl | Bei 304 auf 316L umrüsten |

#### 2.1.5 Bugrolle / Bow Roller — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| B-01 | Rollen-Leichtgängigkeit | Von Hand drehen | Dreht frei, kein Knarzen | Lager schmieren oder ersetzen |
| B-02 | Rollenoberfläche | Sichtprüfung | Keine tiefen Rillen, kein Grat | Rolle ersetzen |
| B-03 | Lager | Spiel prüfen | Kein seitliches Spiel >0,5 mm | Lager ersetzen |
| B-04 | Befestigung am Deck/Bug | Schrauben, Bolzen prüfen | Fest, kein Rost, Dichtung intakt | Nachziehen, Dichtung erneuern |
| B-05 | Anker-Aufnahme | Anker einlegen | Anker sitzt sicher, kein Klappern | Gummipuffer einsetzen |
| B-06 | Kettenführung | Kette einlegen | Kette läuft sauber, kein Verkanten | Ausrichten, ggf. Führung erweitern |
| B-07 | Ankersicherung | Pin, Clip, Schnapper prüfen | Hält sicher, leicht lösbar | Ersetzen |
| B-08 | Materialzustand | Sichtprüfung + Magnettest | Edelstahl 316, keine Risse | Bei Korrosion ersetzen |

#### 2.1.6 Snubber / Ruckdämpfer — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| SN-01 | Leinenzustand | Sichtprüfung, Dehnung | Keine aufgeriebenen Fasern, elastisch | Ersetzen |
| SN-02 | Kettenklaue / Hook | Sichtprüfung, Spiel | Kein Verschleiß, greift sicher | Ersetzen |
| SN-03 | Karabiner / Schäkel | Sichtprüfung | Feder intakt, kein Rost | Ersetzen |
| SN-04 | Schamfil-Schutz | Sichtprüfung | Vorhanden, intakt | Erneuern |
| SN-05 | Gummi-Elemente (Rubber Snubber) | Sichtprüfung, Drucktest | Keine Risse, elastisch | Ersetzen |
| SN-06 | Länge und Durchmesser | Maßband | Gemäß Bootsgröße dimensioniert | Upgraden |

#### 2.1.7 Kettenkasten — Pre-Season-Checkliste

| Nr. | Prüfpunkt | Methode | Akzeptabel | Maßnahme bei Mangel |
|-----|-----------|---------|-----------|-------------------|
| KK-01 | Sauberkeit | Sichtprüfung | Kein stehendes Wasser, kein Geruch | Reinigen, desinfizieren |
| KK-02 | Ablauf / Drainage | Wasser einfüllen, Ablauf prüfen | Wasser läuft zügig ab | Ablauf reinigen / freimachen |
| KK-03 | Belüftung | Sichtprüfung | Belüftungsöffnung vorhanden, frei | Öffnung reinigen oder nachrüsten |
| KK-04 | Kettenführung (Fallrohr) | Sichtprüfung | Kein Riss, kein Verschleiß | Reparieren oder ersetzen |
| KK-05 | Endpunkt-Befestigung | Sichtprüfung | Dyneema/Leine korrekt befestigt | Erneuern (KEIN Metalldraht!) |
| KK-06 | Laminiatzustand | Sichtprüfung, Klopfprobe | Keine Delamination, kein Osmose | Reparieren |
| KK-07 | Geruch | Riechen | Kein Fäulnis- oder Schwefelgeruch | Reinigen, desinfizieren, Belüftung verbessern |

### 2.2 In-Season-Wartung (Mai–Oktober)

Die In-Season-Wartung besteht aus regelmäßigen Sichtprüfungen und
anlassbezogenen Maßnahmen während der aktiven Nutzungsperiode.

#### 2.2.1 Nach jedem Ankermanöver

| Nr. | Prüfpunkt | Aufwand | Methode |
|-----|-----------|---------|---------|
| IS-01 | Kette während des Hievens beobachten | 0 min (beim Aufholen) | Auf verdrehte Glieder, Fremdkörper achten |
| IS-02 | Anker auf Beschädigung prüfen | 30 sek | Sichtprüfung beim Einfahren |
| IS-03 | Snubber auf Beschädigung prüfen | 30 sek | Sichtprüfung beim Abnehmen |
| IS-04 | Windlass-Lauf beurteilen | 0 min (beim Hieven) | Ungewöhnliche Geräusche, Ruckeln? |
| IS-05 | Kettennuss-Eingriff beurteilen | 0 min (beim Hieven) | Kette springt? Rutscht? |

#### 2.2.2 Wöchentlich (bei aktivem Cruising)

| Nr. | Prüfpunkt | Aufwand | Methode |
|-----|-----------|---------|---------|
| IW-01 | Kette und Anker mit Süßwasser spülen | 10 min | Deckwaschpumpe oder Eimer |
| IW-02 | Kettenkastendrainage prüfen | 2 min | Luke öffnen, Wasserstand |
| IW-03 | Windlass-Gehäuse reinigen | 5 min | Süßwasser, weicher Lappen |
| IW-04 | Snubber-Zustand kurz prüfen | 1 min | Sichtprüfung |

#### 2.2.3 Monatlich

| Nr. | Prüfpunkt | Aufwand | Methode |
|-----|-----------|---------|---------|
| IM-01 | Schäkelverbindungen prüfen | 10 min | Sichtprüfung, Sicherungen |
| IM-02 | Wirbel/Swivel prüfen | 5 min | Drehbarkeit, Spiel |
| IM-03 | Windlass-Getriebeöl Sichtprüfung | 5 min | Ölstand, Farbe |
| IM-04 | Elektrische Verbindungen (kurz) | 5 min | Sichtprüfung auf Korrosion |
| IM-05 | Bugrolle prüfen | 3 min | Leichtgängigkeit, Lager |
| IM-06 | Kettenmarkierungen prüfen | 5 min | Beim nächsten Ankermanöver |

#### 2.2.4 Nach Extrembelastung (Sturmankern, Festsitz)

Nach jedem Sturmankern (>6 Bft für >12 Stunden) oder nach einem
Festsitz-Anker-Ereignis ist eine erweiterte Inspektion durchzuführen:

| Nr. | Prüfpunkt | Methode |
|-----|-----------|---------|
| IE-01 | Kette vollständig auslegen und prüfen | Auf Pier/Steg auslegen, jedes 10. Glied messen |
| IE-02 | Anker-Schweißnähte mit Lupe prüfen | Lupe 10×, auf Haarrisse achten |
| IE-03 | Wirbel-Drehachse auf Spiel prüfen | Seitliches Wackeln, Drehung |
| IE-04 | Windlass unter Deck inspizieren | Auf Wassereinbruch, lose Schrauben |
| IE-05 | Snubber-Dehnung prüfen | Verbleibende Elastizität |
| IE-06 | Bugrolle-Befestigung prüfen | Schrauben auf Lockerung |
| IE-07 | Deckbefestigung der Winde prüfen | Risse im Laminat, lose Muttern |
| IE-08 | Kettenstopper prüfen | Backen, Federmechanismus |

### 2.3 Winterization (November–Dezember)

Die Wintereinlagerung ist entscheidend für die Langlebigkeit des
Ankersystems. Korrekte Konservierung verhindert Korrosion und
Materialermüdung während der Standzeit.

#### 2.3.1 Anker — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Anker abnehmen | Bugrolle entlasten, Anker sichern |
| 2 | Gründlich reinigen | Süßwasser + Bürste, Schlick entfernen |
| 3 | Trocknen lassen | Min. 24 Stunden an der Luft |
| 4 | Zustand dokumentieren | Fotos, Gewicht, Befundliste |
| 5 | Galvanisierung behandeln | Zinkspray auf blanke Stellen (CRC Zinc-It) |
| 6 | Bewegliche Teile schmieren | Tef-Gel oder Lanocote auf Bolzen, Flunkengelenk |
| 7 | Trocken lagern | Nicht auf dem Boden, Holzpalette oder Regal |
| 8 | Schäkelöse schützen | Fett oder Lanocote auf Schäkelöse |

#### 2.3.2 Kette — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Kette komplett ausziehen | Auf Pier/Steg auslegen oder in Wanne |
| 2 | Hochdruckreiniger | Alle Glieder reinigen, Sand/Schlick entfernen |
| 3 | Trocknen | Vollständig trocknen lassen (min. 48 Stunden) |
| 4 | Inspektion (Protokoll K-01 bis K-10) | Messprotokoll erstellen |
| 5 | Markierungen erneuern | Falls nötig: Kabelbinder, Farbmarkierung |
| 6 | Optional: Zinkspray | Gesamte Kette mit CRC Zinc-It oder ähnlich |
| 7 | Einlagern | Trocken, belüftet, nicht auf dem Boden |
| 8 | Kettenkasten reinigen | Auswaschen, trocknen, desinfizieren |

#### 2.3.3 Windlass — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Süßwasserspülung | Windlass außen und innen (Luke) reinigen |
| 2 | Trocknen | Motorraum offen lassen zum Durchlüften |
| 3 | Getriebeöl wechseln | Altes Öl ablassen, frisches Getriebeöl einfüllen |
| 4 | Kohlebürsten prüfen | Motor öffnen, Bürstenlänge messen |
| 5 | Wellendichtung prüfen | Auf Leckage, Risse |
| 6 | Korrosionsschutz außen | Edelstahl: Edelstahlpflege; Alu: Teflonspray |
| 7 | Kupplung lösen | Clutch in Neutralposition, entlastet |
| 8 | Elektrische Anschlüsse | Kontaktspray (Ballistol, CRC 2-26) |
| 9 | Batterie-Hauptschalter | AUS, Sicherung entfernen |
| 10 | Abdeckung montieren | Windenabdeckung aus Canvas oder Neopren |

#### 2.3.4 Wirbel / Swivel — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Demontieren | Aus der Kette nehmen |
| 2 | Reinigen | Süßwasser + Drahtbürste |
| 3 | Inspizieren | Verschleiß, Spiel, Korrosion |
| 4 | Schmieren | Tef-Gel auf Drehachse |
| 5 | Trocken lagern | In Plastikbeutel mit Silikagel |

#### 2.3.5 Bugrolle — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Reinigen | Süßwasser, Edelstahlpflege |
| 2 | Lager schmieren | Tropfen WD-40 oder Teflonöl |
| 3 | Befestigung prüfen | Schrauben nachziehen |
| 4 | Abdichten | Silikon/PU um Befestigungspunkte erneuern falls nötig |
| 5 | Ankersicherung prüfen | Pin, Clip reinigen, ggf. ersetzen |

#### 2.3.6 Snubber — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Reinigen | Süßwasser, Seife |
| 2 | Trocknen | Vollständig trocknen lassen |
| 3 | Inspizieren | Fasern, Haken, Elastizität |
| 4 | UV-geschützt lagern | Nicht im Sonnenlicht, drinnen lagern |
| 5 | Ersetzen falls nötig | Bei aufgeriebenen Fasern → neue Snubber bestellen |

#### 2.3.7 Kettenkasten — Winterization

| Schritt | Maßnahme | Detail |
|---------|----------|--------|
| 1 | Kette entnehmen | Komplett leeren |
| 2 | Reinigen | Hochdruckreiniger, dann Desinfektion |
| 3 | Trocknen | Offen lassen, Lüfter oder Heizung |
| 4 | Drainage prüfen | Siphon / Abfluss reinigen |
| 5 | Belüftung sicherstellen | Luke einen Spalt offen oder Belüftungsgitter |
| 6 | Laminiatzustand prüfen | Klopfprobe, Osmose-Check |
| 7 | Optional: Beschichtung | Epoxy-Primer auf blanke Stellen |

### 2.4 Wartungsintervall-Übersicht — Gesamtmatrix

| Komponente | Nach jedem Ankern | Wöchentlich | Monatlich | Pre-Season | Winterization | Alle 5 Jahre |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|
| Anker — Sichtprüfung | ✓ | — | — | ✓ | ✓ | — |
| Anker — Schweißnähte | — | — | — | ✓ | — | ✓ (NDT) |
| Anker — Galvanisierung | — | — | — | ✓ | ✓ | Neuverzinken |
| Kette — Sichtprüfung | ✓ | ✓ | — | ✓ | ✓ | — |
| Kette — Maßprüfung | — | — | — | ✓ | ✓ | — |
| Kette — Süßwasserspülung | — | ✓ | — | ✓ | ✓ | — |
| Kette — Galvanisierung | — | — | — | ✓ | ✓ | Neuverzinken |
| Windlass — Sichtprüfung | ✓ | — | ✓ | ✓ | ✓ | — |
| Windlass — Getriebeöl | — | — | Sichtprüfung | Wechsel | Wechsel | — |
| Windlass — Kohlebürsten | — | — | — | Prüfen | Prüfen | Tauschen |
| Windlass — Wellendichtung | — | — | — | Prüfen | Prüfen | Tauschen |
| Windlass — Elektrisch | — | — | ✓ | ✓ | ✓ | — |
| Wirbel/Swivel | — | — | ✓ | ✓ | ✓ | Ersetzen |
| Bugrolle — Lager | — | — | ✓ | ✓ | ✓ | — |
| Bugrolle — Befestigung | — | — | — | ✓ | ✓ | — |
| Snubber | ✓ | — | — | ✓ | ✓ | Ersetzen |
| Kettenkasten | — | ✓ | — | ✓ | ✓ | Beschichtung |
| Schäkel/Verbinder | — | — | ✓ | ✓ | ✓ | Ersetzen |
| Kettenstopper | — | — | — | ✓ | ✓ | — |

### 2.5 Wartungsaufwand nach Bootsgröße

| Bootsgröße | Pre-Season (Stunden) | Materialkosten/Jahr | Fachwerft-Kosten/Jahr |
|-----------|---------------------|--------------------|--------------------|
| 8–10 m | 4–6 h | 80–150 EUR | 250–450 EUR |
| 10–12 m | 6–8 h | 120–220 EUR | 350–600 EUR |
| 12–14 m | 8–12 h | 180–350 EUR | 500–900 EUR |
| 14–18 m | 12–18 h | 250–500 EUR | 750–1.400 EUR |
| 18–22 m | 18–28 h | 400–800 EUR | 1.200–2.500 EUR |
| 22–30 m | 28–40 h | 600–1.500 EUR | 2.000–5.000 EUR |

### 2.6 Dokumentation und Wartungslogbuch

Jede Wartungsmaßnahme sollte dokumentiert werden. Mindestangaben:

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| Datum | Durchführungsdatum | 2026-03-15 |
| Komponente | Betroffene Systemkomponente | Kette 10 mm DIN 766, 60 m |
| Maßnahme | Durchgeführte Arbeiten | Glieddicke gemessen, 5 Stellen |
| Befund | Ergebnis der Prüfung | Min. 8,9 mm (Nenn 10 mm = 89 %) |
| Bewertung | OK / Beobachten / Handlungsbedarf | Beobachten (knapp über 90 %-Grenze) |
| Nächste Maßnahme | Empfohlener Folgetermin | Kontrolle in 6 Monaten |
| Ausführender | Wer hat die Arbeit durchgeführt | Eigner / Werft XY |
| Kosten | Materialkosten + Arbeitskosten | 0 EUR (Eigenleistung) |
| Fotos | Fotodokumentation | kette_inspektion_2026_03.jpg |

---

## 3. Ketten-Inspektion

### 3.1 Grundlagen der Ketteninspektion

Die Kette ist die Lebensversicherung des Ankersystems. Eine gebrochene
Kette bedeutet Ankerverlust — und bei Starkwind unter Umständen Strandung
oder Kollision. Die Inspektion der Kette ist daher die wichtigste
Einzelmaßnahme in der Ankersystem-Wartung.

#### 3.1.1 Verschleißmechanismen

| Mechanismus | Beschreibung | Betroffene Zone | Geschwindigkeit |
|------------|-------------|----------------|----------------|
| Abrasion | Reibung an Kettennuss, Bugrolle, Grund | Erste 10 m, Kontaktstellen | Schnell (1–3 %/Jahr) |
| Korrosion (allgemein) | Flächenrost nach Galv.-Verlust | Gesamte Kette | Mittel (0,1–0,3 mm/Jahr) |
| Korrosion (Lochfraß) | Lokaler Materialverlust | Schweißstellen, Kerben | Schnell (unkontrolliert) |
| Elongation | Plastische Verformung unter Last | Erste 5–10 m | Langsam |
| Ermüdung | Wechselbelastung (Schwell, Wind) | Gesamte Kette, Endglieder | Sehr langsam |
| Galvanischer Angriff | Kontakt mit edlerem Metall | Verbindungsstellen | Mittel |

#### 3.1.2 Kettenstandards und Nennmaße

| Ketten-Norm | Glieddicke d | Innenlänge | Innenbreite | Teilung | Bruchlast (Güteklasse 3) |
|------------|:-----------:|:----------:|:-----------:|:-------:|:------------------------:|
| DIN 766, 6 mm | 6,0 mm | 18,5 mm | 7,5 mm | 18,5 mm | 11 kN |
| DIN 766, 7 mm | 7,0 mm | 22,0 mm | 9,0 mm | 22,0 mm | 15 kN |
| DIN 766, 8 mm | 8,0 mm | 24,0 mm | 10,0 mm | 24,0 mm | 20 kN |
| DIN 766, 10 mm | 10,0 mm | 28,0 mm | 12,0 mm | 28,0 mm | 32 kN |
| DIN 766, 12 mm | 12,0 mm | 36,0 mm | 15,0 mm | 36,0 mm | 46 kN |
| DIN 766, 13 mm | 13,0 mm | 36,0 mm | 15,0 mm | 36,0 mm | 54 kN |
| ISO 4565, 8 mm | 8,0 mm | 24,0 mm | 10,0 mm | 24,0 mm | 20 kN |
| ISO 4565, 10 mm | 10,0 mm | 28,0 mm | 12,0 mm | 28,0 mm | 32 kN |

**Wichtig**: Kalibrierte Kette (DIN 766) und unkalibrierte Kette (DIN 764)
sind NICHT austauschbar. Die Kettennuss ist auf eine bestimmte Teilung und
Gliedform ausgelegt. Eine falsche Kette führt zu Rutschen oder Klemmen.

### 3.2 Glieddicke-Messung (Link Measurement)

#### 3.2.1 Messverfahren

**Werkzeug:** Messschieber (min. 150 mm Spannweite), idealerweise digital.

**Vorgehensweise:**

1. Kette auslegen (Pier, Steg oder Wanne).
2. Kette reinigen — kein Sand, kein Rost an der Messstelle.
3. An mindestens 5 Stellen über die Kettenlänge messen:
   - Meter 1–3 (höchster Verschleiß durch Kettennuss)
   - Meter 5–8 (erhöhter Verschleiß durch Bugrolle)
   - Meter 15 (mittlerer Bereich)
   - Meter 30 (mittlerer Bereich)
   - Letztes Drittel (geringster Verschleiß)
4. Je Messstelle an 3 Gliedern messen (stehend und liegend).
5. Kleinsten Wert als Ist-Maß notieren.

#### 3.2.2 Bewertungskriterien

| Ist-Dicke / Nenn-Dicke | Bewertung | Maßnahme |
|:----------------------:|-----------|----------|
| ≥95 % | Neuwertig / Sehr gut | Nächste Prüfung in 12 Monaten |
| 90–95 % | Gut | Nächste Prüfung in 12 Monaten |
| 85–90 % | Ausreichend | Nächste Prüfung in 6 Monaten, verstärkt beobachten |
| 80–85 % | Grenzwertig | Kette innerhalb 12 Monate ersetzen |
| <80 % | Unzureichend / Ablegereif | Kette SOFORT ersetzen |

**Beispiel 10 mm DIN 766:**
- Nenndicke: 10,0 mm
- 95 %: 9,5 mm → Sehr gut
- 90 %: 9,0 mm → Grenzwert „Gut"
- 85 %: 8,5 mm → Beobachten
- 80 %: 8,0 mm → Grenzwertig → planen
- <8,0 mm: Sofort tauschen

#### 3.2.3 Protokollvorlage Glieddicke-Messung

```
KETTENINSPEKTION — Glieddicke-Protokoll
========================================
Boot: _________________  Datum: ________
Kette: DIN 766 / ____ mm  Länge: ____ m
Baujahr Kette: ________  Galv: verzinkt / VA

Position (m) | Glied | Dicke 1 | Dicke 2 | Dicke 3 | Min. | % Nenn
-------------|-------|---------|---------|---------|------|-------
      1      |   1   |   _.__  |   _.__  |   _.__  | _._  |  __ %
      3      |   2   |   _.__  |   _.__  |   _.__  | _._  |  __ %
      8      |   3   |   _.__  |   _.__  |   _.__  | _._  |  __ %
     15      |   4   |   _.__  |   _.__  |   _.__  | _._  |  __ %
     30      |   5   |   _.__  |   _.__  |   _.__  | _._  |  __ %
     50      |   6   |   _.__  |   _.__  |   _.__  | _._  |  __ %

Minimaler Messwert: _.___ mm = ___ % Nenn
Bewertung: □ Neuwertig □ Gut □ Ausreichend □ Grenzwertig □ Ablegereif
Nächste Prüfung: ________
Prüfer: _________________
```

### 3.3 Galvanisierungs-Bewertung (Galvanizing Assessment)

#### 3.3.1 Zustandsstufen

| Stufe | Beschreibung | Foto-Merkmal | Maßnahme |
|:-----:|-------------|-------------|----------|
| 1 | Neuwertig | Gleichmäßig silbrig-matt, keine Flecken | Keine |
| 2 | Leicht patiniert | Leichte Grautönung, vereinzelt matte Stellen | Keine |
| 3 | Teilweise oxidiert | 10–30 % orangebraune Flecken | Beobachten, Zinkspray auf Flecken |
| 4 | Stark oxidiert | 30–60 % Rost, Zinkschicht großflächig ab | Neuverzinken oder ersetzen in 1–2 Jahren |
| 5 | Schutzlos | >60 % Rost, kein Zink mehr erkennbar | Sofort neuverzinken oder ersetzen |

#### 3.3.2 Zinkschichtdicke (Referenzwerte Neukette)

| Kettendicke | Zinkschichtdicke (Feuerverzinkung) | Zinkschichtdicke (galvanisch) |
|:-----------:|:----------------------------------:|:-----------------------------:|
| 6 mm | 45–65 µm | 15–25 µm |
| 8 mm | 55–75 µm | 20–30 µm |
| 10 mm | 65–85 µm | 25–35 µm |
| 12 mm | 75–95 µm | 30–40 µm |

**Faustregel**: Feuerverzinkung hält 3–4× länger als galvanische Verzinkung.
Für Ankerketten ist ausschließlich Feuerverzinkung (Hot-Dip Galvanizing)
zu empfehlen.

#### 3.3.3 Magnettest für Edelstahlkette

Edelstahlketten (316L) können mit dem Magnettest überprüft werden:

- **Nicht magnetisch** → 316L (austenitisch) → korrekt für Salzwasser
- **Leicht magnetisch** → 304 oder kaltverformt → bedingt geeignet
- **Stark magnetisch** → Kohlenstoffstahl verzinkt → NICHT als „Edelstahl" deklariert!

### 3.4 Elongation Check (Längenprüfung)

#### 3.4.1 Messverfahren

Die Längung der Kette wird über eine definierte Anzahl Glieder gemessen:

1. 10 Glieder abzählen (= 10 × Teilung).
2. Kette unter leichter Spannung auslegen.
3. Länge über 10 Glieder messen (außen zu außen).
4. Vergleich mit Soll-Maß.

#### 3.4.2 Bewertungskriterien

| Gemessene Länge / Soll-Länge | Bewertung | Maßnahme |
|:----------------------------:|-----------|----------|
| 100–101 % | Neuwertig / Gut | Nächste Prüfung regulär |
| 101–103 % | Beginnende Längung | Beobachten |
| 103–105 % | Erhebliche Längung | Kette zeitnah ersetzen |
| >105 % | Ablegereif | Sofort ersetzen |

**Soll-Maße (10 Glieder):**

| Kette | Teilung | 10 Glieder (Soll) | 103 % (Grenzwert) |
|-------|:-------:|:-----------------:|:-----------------:|
| DIN 766, 6 mm | 18,5 mm | 185 mm | 190,6 mm |
| DIN 766, 8 mm | 24,0 mm | 240 mm | 247,2 mm |
| DIN 766, 10 mm | 28,0 mm | 280 mm | 288,4 mm |
| DIN 766, 12 mm | 36,0 mm | 360 mm | 370,8 mm |

### 3.5 Wann die Kette ersetzen — Entscheidungsmatrix

| Befund | Einzeln = Tausch? | In Kombination = Tausch? |
|--------|:-----------------:|:------------------------:|
| Glieddicke <90 % Nenn | Nein (beobachten) | JA (mit jedem anderen Befund) |
| Glieddicke <85 % Nenn | JA | — |
| Elongation >103 % | Nein (beobachten) | JA (mit jedem anderen Befund) |
| Elongation >105 % | JA | — |
| Lochfraß / Narben >2 mm tief | JA | — |
| Galvanisierung <30 % | Nein (neuverzinken) | JA (wenn >90 % und Dicke <90 %) |
| Verdrehte Glieder (>15°) | Abschnitt tauschen | JA (bei >3 Stellen) |
| Gebrochenes Glied | JA (sofort!) | — |
| Steife Glieder (nicht beweglich) | Abschnitt tauschen | JA (bei >5 Stellen) |

### 3.6 Kettenersatz — Kosten

| Kettendicke | Material | Preis pro Meter (2026) | 50 m Gesamtpreis |
|:-----------:|----------|:---------------------:|:----------------:|
| 6 mm | Verzinkter Stahl DIN 766 | 4–6 EUR/m | 200–300 EUR |
| 8 mm | Verzinkter Stahl DIN 766 | 6–9 EUR/m | 300–450 EUR |
| 10 mm | Verzinkter Stahl DIN 766 | 10–15 EUR/m | 500–750 EUR |
| 12 mm | Verzinkter Stahl DIN 766 | 16–24 EUR/m | 800–1.200 EUR |
| 13 mm | Verzinkter Stahl DIN 766 | 20–30 EUR/m | 1.000–1.500 EUR |
| 8 mm | Edelstahl 316L | 18–28 EUR/m | 900–1.400 EUR |
| 10 mm | Edelstahl 316L | 28–42 EUR/m | 1.400–2.100 EUR |
| 12 mm | Edelstahl 316L | 42–65 EUR/m | 2.100–3.250 EUR |

**Bezugsquellen:** Toplicht, SVB, Compass24, Bukh-Bremen, AWN, Bootsteile24.

### 3.7 Kettenmarkierung

Kettenmarkierungen erleichtern die Längenkontrolle beim Ankern erheblich.
Sie sollten bei jeder Pre-Season-Inspektion erneuert werden.

#### 3.7.1 Markierungsmethoden

| Methode | Material | Haltbarkeit | Kosten | Sichtbarkeit |
|---------|----------|-------------|--------|-------------|
| Kabelbinder (farbig) | Nylon-Kabelbinder | 1–2 Saisons | <5 EUR | Gut |
| Farbspray | Leuchtfarbe, 2K-Lack | 1–3 Saisons | 10–15 EUR | Sehr gut |
| Drahtwicklung | Edelstahldraht 0,5 mm | 3–5 Saisons | 8–12 EUR | Mittel |
| Kettenmarker (Plastik) | Kettenmarkierer (z.B. Plastimo) | 2–4 Saisons | 15–25 EUR | Sehr gut |
| Lederstreifen | Leder um Glied gewickelt | 1–2 Saisons | 5–10 EUR | Mittel |

#### 3.7.2 Empfohlenes Farbschema

| Kettenlänge | Farbe | Markierung |
|:-----------:|-------|-----------|
| 10 m | Rot | 1 Kabelbinder / 1 Streifen |
| 20 m | Gelb | 2 Kabelbinder |
| 30 m | Blau | 3 Kabelbinder |
| 40 m | Grün | 4 Kabelbinder |
| 50 m | Weiß | 5 Kabelbinder |
| 60 m | Orange | 6 Kabelbinder |
| 5 m vor Ende | Rot + Weiß | Auffällige Doppelmarkierung |

---

## 4. Anker-Inspektion

### 4.1 Schweißnaht-Inspektion (Weld Inspection)

Die Schweißnähte sind die kritischsten Stellen eines Ankers. Ein Bruch
an der Schweißnaht führt zum sofortigen Funktionsverlust.

#### 4.1.1 Kritische Schweißstellen nach Ankertyp

| Ankertyp | Kritische Stelle 1 | Kritische Stelle 2 | Kritische Stelle 3 |
|----------|-------------------|-------------------|-------------------|
| Bügelanker (Rocna, Mantus) | Bügel ↔ Schaft | Flunke ↔ Schaft | Schäkelöse ↔ Schaft |
| Delta / Pflug (CQR) | Flunke ↔ Schaft | Schaft-Biegung | Schäkelöse |
| Plattenanker (Danforth) | Flunke ↔ Schaft-Platte | Schaft-Gelenk | Schäkelöse ↔ Schaft |
| Klappanker (Bruce-Typ) | Flunke ↔ Schaft | Schaft-Krümmung | Schäkelöse |
| Fortress (Aluminium) | Flunke ↔ Schaft (Bolzen) | — | Schäkelöse |

#### 4.1.2 Prüfverfahren

**Sichtprüfung (Stufe 1 — Bordmittel):**

1. Anker reinigen (Süßwasser + Drahtbürste).
2. Alle Schweißnähte mit Lupe (10×) untersuchen.
3. Auf folgende Befunde achten:

| Befund | Beschreibung | Bewertung |
|--------|-------------|-----------|
| Haarriss | Feiner Riss in oder neben der Naht | KRITISCH — sofort ersetzen |
| Porosität | Kleine Löcher in der Naht | Mittel — beobachten, bei Zunahme ersetzen |
| Einschlüsse | Schlacke/Fremdkörper in der Naht | Mittel — beobachten |
| Naht-Unterwölbung | Konkave Nahtoberfläche | Gering — kosmetisch, solange keine Risse |
| Nahtüberhöhung | Naht steht stark über Grundmaterial | Gering — akzeptabel |
| Rostbildung an Naht | Rost konzentriert sich auf die Naht | Mittel — Galvanisierung dort verloren |
| Verformung am Nahtbereich | Naht oder angrenzend Material verbogen | KRITISCH — Überbelastung |

**Rissprüfung (Stufe 2 — Semi-professionell):**

Farbeindringprüfung (Penetrant Testing, PT) mit Sprühdosen:

1. Reiniger aufsprühen (z.B. MR Chemie MR 79) — Oberfläche reinigen.
2. Eindringmittel aufsprühen (z.B. MR Chemie MR 68 NF, rot) — 15 min einwirken.
3. Überschuss vorsichtig abwischen.
4. Entwickler aufsprühen (z.B. MR Chemie MR 70, weiß) — 10 min warten.
5. Rote Linien auf weißem Hintergrund = Riss.

**Kosten PT-Set:** MR Chemie Prüfset Nr. 1 (3 Dosen): ca. 28–35 EUR.
Reicht für 10–15 Prüfungen.

### 4.2 Galvanisierung des Ankers

#### 4.2.1 Bewertungsskala

| Zustand | Beschreibung | Verbleibende Schutzwirkung | Maßnahme |
|:-------:|-------------|:-------------------------:|----------|
| 1 — Neuwertig | Gleichmäßig silbrig-matt | 100 % | Keine |
| 2 — Patiniert | Leichte Grautönung | 90 % | Keine |
| 3 — Teilabnutzung | Flunke-Spitzen blank, Rest intakt | 70 % | Zinkspray auf blanke Stellen |
| 4 — Starke Abnutzung | 30–50 % blankes Metall | 40 % | Neuverzinken empfohlen |
| 5 — Kein Schutz | >60 % Rost, Zink weitgehend ab | 10 % | Neuverzinken oder ersetzen |

#### 4.2.2 Anker-Neuverzinkung

Siehe Abschnitt 6 (Galvanisierung) für den vollständigen Neuverzinkungsprozess.

### 4.3 Schaft-Ausrichtung (Shaft Alignment)

Ein verbogener Schaft beeinträchtigt das Eingraberhalten des Ankers
erheblich und kann dazu führen, dass der Anker gar nicht greift.

#### 4.3.1 Prüfverfahren

1. Anker auf flache, ebene Fläche legen (Beton, Steg).
2. Schaft soll plan aufliegen.
3. Abstand zwischen Schaft und Fläche an jeder Stelle messen.
4. Maximale Abweichung notieren.

| Abweichung | Bewertung | Maßnahme |
|:----------:|-----------|----------|
| <2 mm/m | Gut | Keine |
| 2–5 mm/m | Leicht verbogen | Richten lassen (Hydraulikpresse) |
| 5–10 mm/m | Deutlich verbogen | Richten lassen, Ursache klären |
| >10 mm/m | Stark verbogen | Ersetzen (Richten nicht mehr sicher) |

**Ursachen für Schaftverbiegung:**
- Festsitz-Anker zu stark mit Winde ausgebrochen
- Anker in Fels/Koralle eingeklemmt
- Grundberührung bei Fahrt
- Sturz vom Bugrolle-Lagerplatz
- Fertigungsmangel (selten)

### 4.4 Bewegliche Teile

#### 4.4.1 Flunkengelenk (bei klappbaren Ankern: Danforth, Fortress)

| Prüfpunkt | Methode | Akzeptabel | Maßnahme |
|-----------|---------|-----------|----------|
| Schwenkwinkel | Flunke von Hand bewegen | Schwenkt frei im vorgesehenen Bereich | Reinigen, Bolzen schmieren |
| Spiel in der Achse | Seitliches Wackeln prüfen | <1 mm seitliches Spiel | Bolzen ersetzen |
| Bolzenverschleiß | Bolzen herausnehmen, messen | Durchmesser >95 % Nenn | Bolzen ersetzen |
| Sicherung des Bolzens | Splint / Ring prüfen | Vorhanden, intakt | Ersetzen |
| Festsitz-Winkel (Fortress) | Einstellungsring prüfen | Mud oder Sand-Position korrekt | Einstellen |

#### 4.4.2 Bügelanker — Bügel-Kontrolle

| Prüfpunkt | Methode | Akzeptabel | Maßnahme |
|-----------|---------|-----------|----------|
| Bügelform | Sichtprüfung, Vergleich mit Herstellerfoto | Keine Verformung | Bei Verformung: ersetzen |
| Bügel-Schweißnaht | Sichtprüfung, Lupe 10× | Kein Riss | Bei Riss: sofort ersetzen |
| Spiel des Bügels | Bei einigen Typen (Ultra, Spade): Bügelrotation | Dreht frei, kein Blockieren | Reinigen, leicht schmieren |

#### 4.4.3 Rollbügel (bei Rocna Vulcan, Mantus M2)

| Prüfpunkt | Methode | Akzeptabel | Maßnahme |
|-----------|---------|-----------|----------|
| Rollbewegung | Anker auf Seite legen, Rollverhalten testen | Rollt frei über Bügel | Reinigen |
| Verschleiß am Bügel | Sichtprüfung | Keine Abflachung, kein Grat | Bei Verschleiß: ersetzen |

### 4.5 Lebensdauer-Einschätzung nach Ankertyp

| Ankertyp | Material | Erwartete Lebensdauer | Hauptverschleiß |
|----------|----------|:--------------------:|----------------|
| Bügelanker (Stahl, verzinkt) | Stahl + Feuerverzinkung | 15–25 Jahre | Galvanisierung, Flunke-Spitze |
| Bügelanker (316L Edelstahl) | 316L Edelstahl | 25–40+ Jahre | Flunke-Spitze (minimal) |
| Delta / CQR (verzinkt) | Stahl + Feuerverzinkung | 15–25 Jahre | Galvanisierung |
| Danforth (verzinkt) | Stahl + Feuerverzinkung | 10–20 Jahre | Bolzengelenk, Galv. |
| Fortress (Aluminium) | Aluminium-Magnesium | 20–30+ Jahre | Bolzen (Edelstahl) |
| Bruce (verzinkt) | Stahl + Feuerverzinkung | 15–25 Jahre | Galvanisierung |

---

## 5. Windlass-Wartung

### 5.1 Motor-Kohlebürsten (Motor Brushes)

#### 5.1.1 Funktionsprinzip

Die meisten Ankerwinden verwenden Gleichstrom-Reihenschlussmotoren mit
Kohlebürsten. Die Kohlebürsten übertragen den Strom auf den rotierenden
Kommutator. Bei Betrieb verschleißen die Bürsten und müssen regelmäßig
ersetzt werden.

#### 5.1.2 Prüfverfahren

1. Sicherung entfernen / Batterie-Hauptschalter AUS.
2. Motorabdeckung öffnen (typisch 4 Schrauben am Motorgehäuse).
3. Bürstenhalter lokalisieren (2 Stück, gegenüberliegend).
4. Bürsten herausnehmen (Feder zur Seite drücken).
5. Bürstenlänge messen.

#### 5.1.3 Bewertungskriterien

| Bürstenlänge | Bewertung | Maßnahme |
|:------------:|-----------|----------|
| >15 mm (Neuzustand ~20 mm) | Gut | Nächste Prüfung in 12 Monaten |
| 10–15 mm | Ausreichend | Nächste Prüfung in 6 Monaten |
| 5–10 mm | Bald fällig | Ersatzbürsten beschaffen, bei nächster Gelegenheit tauschen |
| <5 mm | SOFORT tauschen | Motor kann ausfallen, Kommutatorschäden möglich |

#### 5.1.4 Bürstenwechsel

1. Alte Bürsten herausnehmen (Federweg notieren).
2. Kommutator-Oberfläche prüfen:
   - Glatt, gleichmäßig dunkelbraun = OK
   - Rillen, Kratzer, blaue Verfärbung = Kommutator beschädigt (Fachwerft!)
3. Neue Bürsten einsetzen (gleicher Typ!).
4. Federn auf korrekte Spannung prüfen.
5. Motor kurz laufen lassen (ohne Last) — Einschleifen.

#### 5.1.5 Kohlebürsten — Ersatzteile und Preise

| Hersteller | Modellreihe | Bürsten-Typ | Preis (Paar) | Bezugsquelle |
|-----------|------------|------------|:------------:|-------------|
| Lofrans | Tigres / Dorado | LZ 630032 | 25–35 EUR | SVB, Toplicht |
| Lofrans | X1 / X2 | LZ 630031 | 22–30 EUR | SVB, Toplicht |
| Lewmar | V1 / V2 / V3 | 66000587 | 30–40 EUR | SVB, Compass24 |
| Lewmar | Pro-Fish / Pro-Sport | 66000587 | 30–40 EUR | Lewmar-Händler |
| Quick | Genius / Prince | 900/3000 | 28–38 EUR | SVB, Bukh |
| Quick | Aleph / Dylan | 900/3003 | 28–38 EUR | SVB, Bukh |
| Maxwell | RC6 / RC8 | P100134 | 35–45 EUR | Maxwell-Händler |
| Maxwell | HRC-FF | P100136 | 35–48 EUR | Maxwell-Händler |
| Muir | Cougar / Cheetah | BR1234 | 38–50 EUR | Muir-Händler |
| Italwinch | Smart / Devon | IW-CB-01 | 25–35 EUR | SVB |

### 5.2 Getriebeöl (Gearbox Oil)

#### 5.2.1 Getriebeöl-Typen

| Hersteller | Empfohlenes Öl | Viskosität | Menge typisch |
|-----------|---------------|-----------|:-------------:|
| Lofrans | SAE 80W-90 GL-4 | 80W-90 | 100–200 ml |
| Lewmar | Lewmar Gear Oil (orig.) oder SAE 80W-90 | 80W-90 | 80–150 ml |
| Quick | SAE 80W-90 GL-5 | 80W-90 | 100–200 ml |
| Maxwell | SAE 90 GL-4 | SAE 90 | 120–250 ml |
| Muir | SAE 80W-90 GL-5 | 80W-90 | 150–300 ml |

**Universal-Empfehlung:** SAE 80W-90 GL-4 oder GL-5 Getriebeöl.
Im Notfall: SAE 30 Motoröl als Übergangsöl bis zum nächsten Hafen.

#### 5.2.2 Ölwechsel-Intervall

| Nutzungsintensität | Intervall |
|-------------------|-----------|
| Wenig (1–2× pro Woche ankern) | Alle 24 Monate |
| Normal (3–5× pro Woche) | Alle 12 Monate |
| Intensiv (täglich) | Alle 6 Monate |
| Nach Wassereinbruch | Sofort |

#### 5.2.3 Ölwechsel-Anleitung

1. Windlass in Position bringen (Ablassschraube unten).
2. Auffangbehälter unter Ablassschraube.
3. Ablassschraube herausdrehen.
4. Altes Öl vollständig ablassen.
5. Altes Öl begutachten:
   - Klar, bernsteinfarben → Normal
   - Milchig → Wassereinbruch! → Dichtung ersetzen
   - Metallisch glänzend → Zahnverschleiß → Getriebe inspizieren
   - Schwarz, verbrannt → Überhitzung → Ursache klären
6. Ablassschraube reinigen, neue Dichtung.
7. Frisches Öl einfüllen (Einfüllschraube oben).
8. Ölstand kontrollieren (Sichtglas oder Einfüllrand).
9. Probelauf, nochmals Ölstand kontrollieren.

### 5.3 Kupplung / Clutch

#### 5.3.1 Funktion

Die Kupplung (Clutch) der Ankerwinsch erlaubt es, die Kettennuss vom
Getriebe zu entkoppeln, sodass die Kette frei auslaufen kann (Freilauf
beim Ankern). Im eingekuppelten Zustand überträgt die Kupplung das
Drehmoment vom Motor/Getriebe auf die Kettennuss.

#### 5.3.2 Kupplungstypen

| Typ | Funktion | Verschleiß | Wartung |
|-----|---------|-----------|--------|
| Reibschluss (Konus) | Konusflächen reiben aneinander | Belag-Abrieb | Belag prüfen/ersetzen |
| Klauenkupplung | Formschlüssige Klauen greifen | Klauenverschleiß | Klauen prüfen |
| Hebelkupplung | Handhebel betätigt Konus | Belag-Abrieb, Hebelmechanik | Belag + Mechanik |
| Hydraulische Kupplung | Hydraulisch betätigt | Dichtungen, Flüssigkeit | Dichtung + Öl |

#### 5.3.3 Kupplungs-Prüfung

| Prüfpunkt | Methode | Akzeptabel | Maßnahme |
|-----------|---------|-----------|----------|
| Betätigung | Hebel bewegen | Leichtgängig, kein Verklemmen | Reinigen, schmieren |
| Haltekraft | Kette belasten (hand), Kupplung soll halten | Kein Durchrutschen | Kupplungsbelag ersetzen |
| Freilauf | Kupplung lösen, Kette von Hand ziehen | Kette läuft frei | Kupplung reinigen |
| Rückstellung | Kupplung lösen, Kettennuss drehen | Dreht frei, kein Schleifen | Mechanik justieren |
| Hebel-Sicherung | Hebel in Position → bleibt er dort? | Bleibt sicher in Position | Rastmechanismus prüfen |

### 5.4 Wellendichtungen (Seals)

#### 5.4.1 Funktion

Die Wellendichtung (Shaft Seal) verhindert das Eindringen von Wasser
vom Deck in den Motorraum unter Deck. Undichte Wellendichtungen sind
eine der häufigsten Ursachen für Windlass-Motorschäden.

#### 5.4.2 Prüfung

| Prüfpunkt | Methode | Akzeptabel | Maßnahme |
|-----------|---------|-----------|----------|
| Wasserspuren unter Deck | Sichtprüfung im Motorraum | Trocken | Dichtung ersetzen |
| Dichtungszustand | Sichtprüfung (Luke offen) | Elastisch, keine Risse | Dichtung ersetzen |
| Wassereintritt-Test | Wasser auf Deck an der Welle | Kein Tropfen unter Deck | Dichtung ersetzen |

#### 5.4.3 Dichtungswechsel

1. Sicherung entfernen, Batterie-Hauptschalter AUS.
2. Kettennuss abnehmen (Sicherungsring, Spannschraube).
3. Alte Dichtung entfernen.
4. Sitzfläche reinigen.
5. Neue Dichtung einsetzen (Lippe nach außen = zum Wasser).
6. Kettennuss wieder montieren.
7. Dichtheit prüfen (Wasser auf Deck).

#### 5.4.4 Dichtungen — Ersatzteile und Preise

| Hersteller | Modellreihe | Dichtungs-Typ | Preis | Bezugsquelle |
|-----------|------------|-------------|:-----:|-------------|
| Lofrans | Tigres / Dorado / X-Reihe | Simmerring 35×52×7 | 12–18 EUR | SVB, Toplicht |
| Lewmar | V1–V3 | Lewmar Shaft Seal 66000424 | 18–28 EUR | SVB, Compass24 |
| Quick | Genius / Prince | Quick Shaft Seal | 15–25 EUR | SVB, Bukh |
| Maxwell | RC6 / RC8 | Maxwell Seal Kit P100150 | 20–32 EUR | Maxwell-Händler |

### 5.5 Elektrische Verbindungen

#### 5.5.1 Kritische elektrische Verbindungen

| Verbindung | Typischer Querschnitt | Häufigstes Problem | Prüfung |
|-----------|:--------------------:|-------------------|---------|
| Batterie → Hauptsicherung | 25–70 mm² | Korrosion an Klemmen | Spannungsabfall <0,5 V |
| Hauptsicherung → Solenoid | 25–70 mm² | Korrosion, Kontaktwiderstand | Spannungsabfall <0,3 V |
| Solenoid → Motor | 16–50 mm² | Korrosion, Wassereinwirkung | Spannungsabfall <0,3 V |
| Steuerkabel (Fußschalter) | 1,5–2,5 mm² | Kabelbruch, Korrosion | Durchgang + Isolation |
| Masse (Motor → Batterie) | 25–70 mm² | Oft vergessen → Korrosion | Spannungsabfall <0,3 V |
| Kettenzähler-Sensor | 0,5–1,5 mm² | Verschmutzung, Kabelbruch | Funktion, Durchgang |

#### 5.5.2 Spannungsabfall-Messung

Der Spannungsabfall über die gesamte Leitung (Plus + Masse) darf unter
Last max. 10 % der Nennspannung betragen:

| System | Max. Spannungsabfall unter Last |
|--------|:------------------------------:|
| 12 V | 1,2 V (10 % von 12 V) |
| 24 V | 2,4 V (10 % von 24 V) |

**Messmethode:**
1. Multimeter auf DC Volt stellen.
2. Plus-Leitung an Batterie-Plus, Minus-Leitung an Motor-Plus.
3. Windlass einschalten (unter Last).
4. Spannung ablesen = Spannungsabfall auf der Plus-Leitung.
5. Wiederholen für Masse-Leitung (Batterie-Minus ↔ Motor-Minus).
6. Beide Werte addieren = Gesamtabfall.

#### 5.5.3 Kontaktpflege

| Verbindungstyp | Reinigungsmethode | Schutz nach Reinigung |
|---------------|------------------|---------------------|
| Batterieklemmen | Drahtbürste, ggf. Schleifvlies | Polfett (Liqui Moly) |
| Kabelschuhe | Kontaktspray (CRC 2-26) | Schrumpfschlauch + Fett |
| Solenoid-Klemmen | Feines Schleifpapier (400er) | Kontaktfett |
| Fußschalter-Stecker | Kontaktspray | WD-40 Specialist Kontaktspray |
| Steuerkabel-Klemmen | Kontaktspray | Vaseline |

### 5.6 Windlass-Winterization (detailliert)

#### 5.6.1 Komplette Winterization-Checkliste

| Schritt | Maßnahme | Werkzeug | Materialkosten |
|:-------:|----------|---------|:--------------:|
| 1 | Kette und Anker abbauen | Schraubenschlüssel | 0 EUR |
| 2 | Windlass außen reinigen | Süßwasser, Schwamm | 0 EUR |
| 3 | Motorraum unter Deck reinigen | Lappen, WD-40 | 5 EUR |
| 4 | Getriebeöl wechseln | Schlüssel, Öl | 8–15 EUR |
| 5 | Kohlebürsten prüfen | Schraubendreher | 0 EUR |
| 6 | Wellendichtung prüfen | Sichtprüfung | 0 EUR |
| 7 | Elektrische Klemmen reinigen | Kontaktspray, Bürste | 5–10 EUR |
| 8 | Kontaktfett auf alle Klemmen | Polfett, Vaseline | 5 EUR |
| 9 | Kupplung lösen (Neutralstellung) | Handhebel | 0 EUR |
| 10 | Kettennuss reinigen + leicht ölen | Lappen, Teflonöl | 5 EUR |
| 11 | Abdeckung montieren | Canvas-Abdeckung | 20–40 EUR (einmalig) |
| 12 | Sicherung entfernen | — | 0 EUR |
| **Gesamt** | | | **48–80 EUR** |

---

## 6. Galvanisierung

### 6.1 Grundlagen der Feuerverzinkung

Feuerverzinkung (Hot-Dip Galvanizing) ist der wichtigste Korrosionsschutz
für Ankerketten und Stahlanker. Die Zinkschicht schützt den Stahl durch:

1. **Barrierewirkung**: Zink isoliert den Stahl von der korrosiven Umgebung.
2. **Kathodischer Schutz**: Zink ist unedler als Stahl und opfert sich
   bei Beschädigung der Schicht „selbstaufopfernd" (Opferanode-Prinzip).
3. **Selbstheilung**: Kleine Kratzer werden durch das Opferanoden-Prinzip
   geschützt (bis ca. 3 mm Breite).

### 6.2 Zustandsbewertung der Galvanisierung

#### 6.2.1 Visuelles Bewertungsschema (5 Stufen)

| Stufe | Bezeichnung | Visuelles Merkmal | Verbleibende Lebensdauer (geschätzt) |
|:-----:|------------|-------------------|:------------------------------------:|
| G1 | Neuwertig | Gleichmäßig silbrig-glänzend oder -matt | 8–15 Jahre |
| G2 | Leicht patiniert | Grautönung, vereinzelte matte Stellen | 6–12 Jahre |
| G3 | Teilweise abgenutzt | 10–30 % braune/orangene Flecken | 3–6 Jahre |
| G4 | Stark abgenutzt | 30–70 % Rost, Zink großflächig ab | 1–3 Jahre |
| G5 | Schutzlos | >70 % Rost, Zink kaum erkennbar | <1 Jahr → sofort handeln |

#### 6.2.2 Schichtdicke-Messung

| Methode | Gerät | Genauigkeit | Kosten |
|---------|-------|:-----------:|:------:|
| Magnetische Induktion | Schichtdicken-Messgerät (z.B. Elcometer 456) | ±3 % | 200–600 EUR (Gerät) |
| Wirbelstrom | Schichtdicken-Messgerät (nicht-magnetisch) | ±5 % | 300–800 EUR (Gerät) |
| Destruktiv (Querschliff) | Labor | ±1 % | 50–100 EUR pro Probe |
| Visuell (Abschätzung) | Auge + Referenzfotos | ±30 % | 0 EUR |

### 6.3 Neuverzinkungsprozess

#### 6.3.1 Prozessschritte (Feuerverzinkung durch Fachbetrieb)

| Schritt | Beschreibung | Dauer |
|:-------:|-------------|:-----:|
| 1 | Anlieferung und Eingangsprüfung | — |
| 2 | Entfettung (alkalische Reinigung) | 10–30 min |
| 3 | Beizen (Salzsäure 12–15 %) | 30–120 min |
| 4 | Spülen (Klarwasser) | 5 min |
| 5 | Fluxen (Zinkammoniumchlorid) | 5–15 min |
| 6 | Trocknen | 15–30 min |
| 7 | Feuerverzinken (450°C Zinkbad) | 3–8 min |
| 8 | Abkühlen (Wasser oder Luft) | 10–30 min |
| 9 | Endkontrolle (Schichtdicke, Optik) | — |
| 10 | Verpackung und Rücktransport | — |

#### 6.3.2 Kosten der Neuverzinkung

| Bauteil | Gewicht typisch | Kosten Feuerverzinkung (2026) |
|---------|:--------------:|:----------------------------:|
| Anker 8 kg | 8 kg | 40–65 EUR |
| Anker 12 kg | 12 kg | 55–85 EUR |
| Anker 16 kg | 16 kg | 65–100 EUR |
| Anker 25 kg | 25 kg | 90–140 EUR |
| Anker 35 kg | 35 kg | 120–180 EUR |
| Kette 6 mm, 30 m | 23 kg | 80–130 EUR |
| Kette 8 mm, 50 m | 69 kg | 180–280 EUR |
| Kette 10 mm, 60 m | 132 kg | 320–500 EUR |
| Kette 10 mm, 80 m | 176 kg | 400–620 EUR |
| Kette 12 mm, 80 m | 252 kg | 550–850 EUR |
| Schäkel (10 Stück) | ~2 kg | 25–40 EUR |

**Hinweis**: Preise variieren regional stark. Mindestauftragsgebühr bei
vielen Verzinkereien: 80–120 EUR. Sammelaufträge (z.B. über Yachtclub)
senken die Kosten erheblich.

#### 6.3.3 Verzinkereien — Bezugsquellen

| Region | Betrieb | Kontakt | Yacht-Erfahrung |
|--------|---------|---------|:---------------:|
| Norddeutschland | Voigt & Schweitzer (Rendsburg) | Tel. 04331/XXX | Ja |
| Norddeutschland | Zinkpower (Hamburg) | Tel. 040/XXX | Ja |
| Ostsee | Galvanische Anstalt (Lübeck) | Tel. 0451/XXX | Bedingt |
| Bodensee | Feuerverzinkung Bodensee GmbH | Tel. 07531/XXX | Ja |
| Mittelmeer (ESP) | Galvanitzats Pujol (Barcelona) | Tel. +34 93/XXX | Ja |
| Mittelmeer (FR) | Galva Méditerranée (La Ciotat) | Tel. +33 4/XXX | Ja |

### 6.4 DIY-Zinkspray vs. professionelle Feuerverzinkung

#### 6.4.1 Vergleich

| Kriterium | DIY Zinkspray | Professionelle Feuerverzinkung |
|-----------|:------------:|:-----------------------------:|
| Schichtdicke | 15–40 µm | 60–100 µm |
| Haftung | Mäßig (mechanische Haftung) | Sehr gut (metallurgische Bindung) |
| Kathodischer Schutz | Begrenzt | Voll |
| Selbstheilung | Nein | Ja (bis ~3 mm) |
| Abriebfestigkeit | Niedrig | Hoch |
| Lebensdauer (Salzwasser) | 6–18 Monate | 5–15 Jahre |
| Kosten (Anker 15 kg) | 8–15 EUR | 60–100 EUR |
| Anwendung | Selbst machbar | Fachbetrieb erforderlich |
| Vorbereitung | Schleifen, entfetten | Beizen, fluxen (Fachbetrieb) |

#### 6.4.2 DIY-Zinkspray — Produkte

| Produkt | Zinkgehalt | Schichtdicke | Preis (400 ml) | Bewertung |
|---------|:----------:|:------------:|:--------------:|:---------:|
| CRC Zinc-It | 98 % Zink | 25–35 µm | 12–15 EUR | Sehr gut |
| Presto Zinkspray | 99 % Zink | 20–30 µm | 8–11 EUR | Gut |
| WEICON Zink Spray | 97 % Zink | 25–35 µm | 14–18 EUR | Sehr gut |
| Liqui Moly Zink-Spray | 96 % Zink | 20–30 µm | 10–14 EUR | Gut |
| Motip Zinkspray | 95 % Zink | 15–25 µm | 7–10 EUR | Befriedigend |
| Fertan Zink-Spray | 98 % Zink | 25–35 µm | 13–17 EUR | Sehr gut |

#### 6.4.3 DIY-Zinkspray — Anwendung

1. Oberfläche vorbereiten:
   - Rost entfernen (Drahtbürste, Schleifscheibe, Winkelschleifer)
   - Oberfläche anrauen (Schleifvlies K80–K120)
   - Entfetten (Silikonentferner oder Aceton)
2. Zinkspray aufschüren:
   - Dose kräftig schütteln (2 Minuten)
   - Abstand 20–30 cm
   - 2–3 dünne Schichten (besser als 1 dicke)
   - Zwischen den Schichten 5–10 Minuten antrocknen lassen
3. Aushärten:
   - Min. 24 Stunden trocknen lassen
   - Nicht bei Regen oder hoher Luftfeuchtigkeit auftragen
   - Temperatur >10°C, <35°C

**Wichtig:** Zinkspray ist eine ZWISCHENLÖSUNG, kein Ersatz für
professionelle Feuerverzinkung. Es verlängert die Lebensdauer um
6–18 Monate, danach sollte eine Neuverzinkung erfolgen.

### 6.5 Galvanisierungsverlust — Einflussfaktoren

| Faktor | Auswirkung | Lebensdauer-Reduktion |
|--------|-----------|:--------------------:|
| Salzwasser (ständig) | Schneller Zinkabbau | −30–50 % |
| Salzwasser (gelegentlich, gespült) | Moderater Zinkabbau | −10–20 % |
| Süßwasser | Minimaler Zinkabbau | ±0 % |
| Schlick/Schlamm-Kontakt | Anaerobe Korrosion möglich | −10–20 % |
| Kettennuss-Abrieb | Mechanischer Zinkabrieb | −20–40 % (erste Meter) |
| Bugrolle-Abrieb | Mechanischer Zinkabrieb | −15–30 % (Kontaktstellen) |
| UV-Exposition (Deck) | Minimal | ±0 % |
| Elektrolytischer Kontakt (Cu, Bronze) | Galvanische Korrosion | −50–80 % |

---

## 7. Korrosionsschutz

### 7.1 Galvanische Isolation

#### 7.1.1 Galvanische Spannungsreihe (Marine-relevante Metalle)

| Metall | Potenzial (mV vs. Ag/AgCl) | Edel/Unedel |
|--------|:-------------------------:|:-----------:|
| Zink | −1.030 | Sehr unedel (Opferanode) |
| Aluminium (rein) | −870 | Unedel |
| Aluminium-Magnesium (Fortress) | −850 | Unedel |
| Stahl (ungeschützt) | −650 | Mäßig unedel |
| Stahl (verzinkt) | −1.000 (Zinkschicht) | Unedel (geschützt) |
| Blei | −500 | Mäßig unedel |
| Edelstahl 316L (passiv) | −100 | Edel |
| Edelstahl 316L (aktiv, im Spalt) | −500 | Mäßig unedel (!) |
| Bronze | −300 | Mäßig edel |
| Kupfer | −200 | Edel |
| Messing | −350 | Mäßig edel |
| Titan | −50 | Sehr edel |

#### 7.1.2 Kritische Materialpaarungen im Ankersystem

| Paarung | Spannung (mV) | Risiko | Maßnahme |
|---------|:------------:|:------:|----------|
| Verzinkte Kette ↔ Edelstahl-Wirbel | ~900 mV | HOCH | Tef-Gel, Isolierung, regelmäßig prüfen |
| Verzinkte Kette ↔ Bronze-Bugrolle | ~700 mV | HOCH | Auf Edelstahl-Bugrolle umrüsten |
| Alu-Anker (Fortress) ↔ Edelstahl-Schäkel | ~750 mV | HOCH | Tef-Gel, Alu-Schäkel verwenden |
| Edelstahl-Kette ↔ Edelstahl-Wirbel | 0 mV | Niedrig | Kein Problem |
| Verzinkte Kette ↔ verzinkter Schäkel | 0 mV | Niedrig | Kein Problem |
| Edelstahl-Windlass ↔ verzinkte Kette | ~900 mV | MITTEL | Tef-Gel auf Kettennuss |

### 7.2 Isoliermittel

#### 7.2.1 Tef-Gel (Sealand/Dometic)

| Eigenschaft | Wert |
|-------------|------|
| Typ | PTFE-basiertes Anti-Seize-Gel |
| Hauptanwendung | Isolation ungleicher Metalle, Anti-Festfressen |
| Temperaturbereich | −50°C bis +280°C |
| Salzwasserbeständig | Ja |
| Gebindegröße | 30 g Tube, 100 g Dose |
| Preis | 12–18 EUR (30 g), 28–38 EUR (100 g) |
| Bezugsquelle | SVB, Toplicht, Compass24, AWN |
| Anwendung im Ankersystem | Schäkel ↔ Kette, Wirbel ↔ Kette, Befestigungsschrauben |
| Auftragung | Dünn auf beide Kontaktflächen, nicht übertreiben |
| Haltbarkeit | 12–24 Monate, dann erneuern |

#### 7.2.2 Duralac (Loctite)

| Eigenschaft | Wert |
|-------------|------|
| Typ | Chromat-basiertes Isoliermittel (gelb-grün) |
| Hauptanwendung | Isolation Aluminium ↔ Edelstahl |
| Salzwasserbeständig | Ja |
| Gebindegröße | 115 ml Tube |
| Preis | 15–22 EUR (115 ml) |
| Bezugsquelle | Compass24, Bootsteile24, Amazon |
| Anwendung im Ankersystem | Alu-Anker (Fortress) ↔ Edelstahl-Schäkel |
| Haltbarkeit | Lange (bildet feste Schicht) |
| Hinweis | Schwierig zu entfernen, nicht auf beweglichen Teilen |

#### 7.2.3 Lanocote (Forespar)

| Eigenschaft | Wert |
|-------------|------|
| Typ | Lanolin-basiertes Korrosionsschutzfett |
| Hauptanwendung | Korrosionsschutz, leichte Isolation |
| Salzwasserbeständig | Ja |
| Gebindegröße | 120 g Dose, 200 g Dose |
| Preis | 18–25 EUR (120 g), 28–35 EUR (200 g) |
| Bezugsquelle | SVB, Toplicht, AWN |
| Anwendung im Ankersystem | Schäkel, Bolzen, bewegliche Teile, Wirbel |
| Auftragung | Dünn auftragen, überschüssiges Material abwischen |
| Haltbarkeit | 6–12 Monate (muss nachgefettet werden) |
| Vorteil | Biologisch abbaubar, lebensmittelecht, ungiftig |

### 7.3 Korrosionsschutz-Maßnahmen nach Komponente

| Komponente | Empfohlenes Mittel | Intervall | Anwendung |
|-----------|-------------------|-----------|-----------|
| Schäkel (verz. Stahl ↔ Edelstahl) | Tef-Gel | Alle 12 Monate | Auf Bolzen und Kontaktflächen |
| Wirbel (Edelstahl ↔ verz. Kette) | Tef-Gel | Alle 12 Monate | Auf Drehachse und Schäkelösen |
| Alu-Anker (Fortress) | Duralac | Bei Montage | Auf Schäkelöse |
| Windlass-Befestigungsschrauben | Tef-Gel | Bei Montage + alle 2 Jahre | Auf Gewindeflanken |
| Bugrolle-Achse | Lanocote | Alle 6 Monate | Auf Achse und Lager |
| Kettenstopper | Lanocote | Alle 6 Monate | Auf bewegliche Teile |
| Anker-Bolzen (Danforth) | Lanocote oder Tef-Gel | Alle 12 Monate | Auf Bolzen und Gelenk |
| Fußschalter-Membrane | WD-40 Specialist Kontakt | Alle 6 Monate | Sprühstoß auf Kontakte |

### 7.4 Spaltkorrosion bei Edelstahl (Crevice Corrosion)

Edelstahl 316L ist in belüftetem Salzwasser passiv und korrosionsbeständig.
In engen Spalten (unter Muttern, in Gewindebohrungen, unter Dichtungen)
kann jedoch Sauerstoffmangel zur Aktivierung führen — die Passivschicht
bricht zusammen und der Edelstahl korrodiert lokal sehr aggressiv.

#### 7.4.1 Kritische Stellen im Ankersystem

| Stelle | Spalttyp | Risiko | Prävention |
|--------|----------|:------:|-----------|
| Windlass-Befestigung (unter Mutter) | Schraube in Sandwich | Hoch | Tef-Gel, regelmäßig lösen/prüfen |
| Bugrolle-Bolzen (in Bohrung) | Bolzen in Alu-Beschlag | Hoch | Tef-Gel oder Duralac, Edelstahl-Bolzen |
| Schäkelbolzen (im Schäkel) | Stift in Öse | Mittel | Lanocote, regelmäßig öffnen |
| Kettenstopper-Backen (innen) | Backe an Backe | Mittel | Reinigen, schmieren |
| Ankersicherungs-Pin | Pin in Bohrung | Mittel | Lanocote |

#### 7.4.2 Erkennung

- Braune/orangene Verfärbung an einem Edelstahlteil → Spaltkorrosion!
- Edelstahl mit Magnettest prüfen: Magnetisch = 304 → Upgrade auf 316L
- Lochfraß (kleine tiefe Löcher) an Edelstahl → Fortgeschrittene Korrosion

### 7.5 Tea Staining bei Edelstahl

Tea Staining ist eine oberflächliche Verfärbung von Edelstahl in
salzwasserhaltiger Atmosphäre. Es ist primär ein kosmetisches Problem,
kann aber auf beginnende Korrosion hinweisen.

| Zustand | Beschreibung | Maßnahme |
|---------|-------------|----------|
| Leichtes Tea Staining | Bräunliche Verfärbung, nur oberflächlich | Edelstahlreiniger (Inox Cleaner) |
| Starkes Tea Staining | Tiefbraun, fühlbar raue Oberfläche | Polieren + Passivieren |
| Lochfraß unter Tea Staining | Löcher unter der Verfärbung | Bauteil ersetzen |

**Präventiv:** Regelmäßig mit Süßwasser spülen, Edelstahlpflege (z.B.
Boat-Life Stainless Steel Cleaner, 12–18 EUR / 500 ml).

---

## 8. Ersatzteile und Bezugsquellen

### 8.1 Windlass-Ersatzteil-Kits nach Hersteller

#### 8.1.1 Lofrans — Service-Kits

| Modell | Service-Kit | Inhalt | Preis (2026) | Teilenummer |
|--------|-----------|--------|:------------:|-------------|
| X1 (600 W) | Annual Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl 100 ml | 58–75 EUR | LZ-SK-X1 |
| X2 (700 W) | Annual Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl 100 ml | 62–80 EUR | LZ-SK-X2 |
| X3 (1000 W) | Annual Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl 200 ml | 68–88 EUR | LZ-SK-X3 |
| Tigres (1500 W) | Annual Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl 200 ml | 78–98 EUR | LZ-SK-TIG |
| Dorado (1000 W) | Annual Service Kit | Kohlebürsten, Dichtung, O-Ringe | 65–85 EUR | LZ-SK-DOR |
| Alle Modelle | Solenoid komplett | 12V oder 24V Solenoid | 85–120 EUR | LZ-SOL-12 / LZ-SOL-24 |
| Alle Modelle | Kettennuss 8mm DIN766 | Kettennuss Edelstahl | 95–140 EUR | LZ-GY-8 |
| Alle Modelle | Kettennuss 10mm DIN766 | Kettennuss Edelstahl | 105–155 EUR | LZ-GY-10 |

#### 8.1.2 Lewmar — Service-Kits

| Modell | Service-Kit | Inhalt | Preis (2026) | Teilenummer |
|--------|-----------|--------|:------------:|-------------|
| V1 (300 W) | Service Kit | Kohlebürsten, Dichtung, Bolzen | 48–65 EUR | 66000600 |
| V2 (500 W) | Service Kit | Kohlebürsten, Dichtung, Bolzen | 52–70 EUR | 66000601 |
| V3 (700 W) | Service Kit | Kohlebürsten, Dichtung, Bolzen | 58–78 EUR | 66000602 |
| V4 (1000 W) | Service Kit | Kohlebürsten, Dichtung, Bolzen, Öl | 65–85 EUR | 66000603 |
| V700 (700 W) | Service Kit | Kohlebürsten, Dichtung | 55–72 EUR | 66000610 |
| Pro-Fish/Pro-Sport | Service Kit | Kohlebürsten, Dichtung | 52–68 EUR | 66000620 |
| Alle Modelle | Solenoid 12V | Solenoid komplett | 75–110 EUR | 68000318 |
| Alle Modelle | Solenoid 24V | Solenoid komplett | 80–115 EUR | 68000319 |
| Alle Modelle | Kettennuss 8mm DIN766 | Kettennuss | 82–120 EUR | 66000445 |
| Alle Modelle | Kettennuss 10mm DIN766 | Kettennuss | 92–135 EUR | 66000446 |

#### 8.1.3 Quick — Service-Kits

| Modell | Service-Kit | Inhalt | Preis (2026) | Teilenummer |
|--------|-----------|--------|:------------:|-------------|
| Genius (300 W) | Service Kit | Kohlebürsten, Dichtung | 45–60 EUR | QK-SK-GEN |
| Prince (500 W) | Service Kit | Kohlebürsten, Dichtung, Öl | 52–68 EUR | QK-SK-PRI |
| Aleph (700 W) | Service Kit | Kohlebürsten, Dichtung, Öl | 58–75 EUR | QK-SK-ALE |
| Dylan (1000 W) | Service Kit | Kohlebürsten, Dichtung, Öl | 65–82 EUR | QK-SK-DYL |
| Hector (1500 W) | Service Kit | Kohlebürsten, Dichtung, Öl | 72–92 EUR | QK-SK-HEC |
| Alle Modelle | Solenoid 12V | Solenoid komplett | 80–105 EUR | QK-SOL-12 |
| Alle Modelle | Kettennuss 8mm | Kettennuss verchromt | 75–110 EUR | QK-GY-8 |
| Alle Modelle | Kettennuss 10mm | Kettennuss verchromt | 85–125 EUR | QK-GY-10 |

#### 8.1.4 Maxwell — Service-Kits

| Modell | Service-Kit | Inhalt | Preis (2026) | Teilenummer |
|--------|-----------|--------|:------------:|-------------|
| RC6 (600 W) | Service Kit | Kohlebürsten, Dichtung, O-Ringe | 55–72 EUR | P100160 |
| RC8 (1000 W) | Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl | 65–85 EUR | P100161 |
| HRC-FF (1500 W) | Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl | 75–98 EUR | P100162 |
| HRC10-FF (2000 W) | Service Kit | Kohlebürsten, Dichtung, O-Ringe, Öl | 85–110 EUR | P100163 |
| Alle Modelle | Solenoid 12V | Solenoid komplett | 90–120 EUR | P100200 |
| Alle Modelle | Kettennuss 8mm | Kettennuss | 88–128 EUR | P100080 |
| Alle Modelle | Kettennuss 10mm | Kettennuss | 98–145 EUR | P100100 |

### 8.2 Kettenverbinder und Schäkel

#### 8.2.1 Kettenverbindungsglieder (Connecting Links)

| Typ | Kettendicke | Bruchlast | Preis (2026) | Bezugsquelle |
|-----|:----------:|:---------:|:------------:|-------------|
| Notglied verzinkt (Kong) | 8 mm | 25 kN | 4–7 EUR | SVB, Toplicht |
| Notglied verzinkt (Kong) | 10 mm | 40 kN | 6–10 EUR | SVB, Toplicht |
| Notglied verzinkt (Kong) | 12 mm | 56 kN | 8–14 EUR | SVB, Toplicht |
| Notglied Edelstahl 316 | 8 mm | 28 kN | 12–18 EUR | SVB |
| Notglied Edelstahl 316 | 10 mm | 45 kN | 16–24 EUR | SVB |
| Ketten-Endglied verzinkt | 8 mm | 20 kN | 5–8 EUR | SVB, Compass24 |
| Ketten-Endglied verzinkt | 10 mm | 32 kN | 7–12 EUR | SVB, Compass24 |

#### 8.2.2 Schäkel (Shackles)

| Typ | Größe | Bruchlast | Preis (2026) | Bezugsquelle |
|-----|:-----:|:---------:|:------------:|-------------|
| D-Schäkel verzinkt | 8 mm | 32 kN | 3–5 EUR | SVB, Toplicht |
| D-Schäkel verzinkt | 10 mm | 50 kN | 5–8 EUR | SVB, Toplicht |
| D-Schäkel verzinkt | 12 mm | 72 kN | 8–12 EUR | SVB, Toplicht |
| D-Schäkel Edelstahl 316 | 8 mm | 32 kN | 8–14 EUR | SVB, Toplicht |
| D-Schäkel Edelstahl 316 | 10 mm | 50 kN | 12–20 EUR | SVB, Toplicht |
| D-Schäkel Edelstahl 316 | 12 mm | 72 kN | 18–28 EUR | SVB, Toplicht |
| Omega-Schäkel (HR) verzinkt | 10 mm | 63 kN | 15–22 EUR | Bukh, SVB |
| Omega-Schäkel (HR) Edelstahl | 10 mm | 63 kN | 28–38 EUR | Bukh, SVB |

#### 8.2.3 Sicherung von Schäkeln

| Methode | Beschreibung | Sicherheit | Kosten |
|---------|-------------|:----------:|:------:|
| Drahtwicklung | Edelstahldraht 0,8 mm durch Bolzenloch | Sehr hoch | 0,10 EUR/Stück |
| Kabelbinder | Durch Bolzenloch, UV-beständig | Mittel | 0,05 EUR/Stück |
| Schraubensicherung (Loctite 243) | Mittelfeste Schraubensicherung | Hoch | 0,50 EUR/Stück |
| Sekundenkleber | Tropfen auf Bolzengewinde | Gering (löst sich) | 0,10 EUR/Stück |
| Splint | Durch Bolzen | Sehr hoch (falls Bolzen gebohrt) | 0,20 EUR/Stück |

**Empfehlung:** Drahtwicklung (Edelstahldraht 0,8 mm) ist die bewährteste
und sicherste Methode. Loctite 243 als Ergänzung, nicht als alleinige
Sicherung.

### 8.3 Wirbel / Swivel

| Typ | Bruchlast | Material | Preis (2026) | Bezugsquelle |
|-----|:---------:|----------|:------------:|-------------|
| Kong Anchor Swivel 8–10 mm | 50 kN | Edelstahl 316 | 35–50 EUR | SVB, Toplicht |
| Kong Anchor Swivel 10–12 mm | 80 kN | Edelstahl 316 | 48–68 EUR | SVB, Toplicht |
| Mantus Swivel M1 (8–10 mm) | 68 kN | Edelstahl 316L | 85–110 EUR | SVB, Compass24 |
| Mantus Swivel M1 (10–12 mm) | 90 kN | Edelstahl 316L | 95–125 EUR | SVB, Compass24 |
| Ultra Marine Swivel (8–10 mm) | 60 kN | Edelstahl 316 | 55–75 EUR | SVB |
| Ultra Marine Swivel (10–12 mm) | 80 kN | Edelstahl 316 | 65–90 EUR | SVB |
| Wichard Anchor Swivel (8 mm) | 40 kN | HR Edelstahl | 45–60 EUR | SVB, AWN |
| Wichard Anchor Swivel (10 mm) | 60 kN | HR Edelstahl | 55–75 EUR | SVB, AWN |

### 8.4 Bezugsquellen — Übersicht

| Händler | Webshop | Sortiment | Versand | Stärke |
|---------|---------|-----------|---------|--------|
| SVB (Bremen) | svb-marine.de | Sehr umfangreich | DE/EU | Breites Sortiment, faire Preise |
| Toplicht (Hamburg) | toplicht.de | Umfangreich | DE/EU | Traditionshaus, kompetente Beratung |
| Compass24 | compass24.de | Umfangreich | DE/EU | Gute Preise, schneller Versand |
| AWN (Düsseldorf) | awn.de | Mittel | DE/EU | Gute Eigenmarke |
| Bukh-Bremen | bukh-bremen.de | Speziell (Motoren, Winden) | DE/EU | Lofrans/Quick Spezialist |
| Bootsteile24 | bootsteile24.de | Umfangreich | DE | Gute Preise |
| Yachticon | yachticon.de | Pflegemittel, Chemie | DE/EU | Spezialist für Pflegeprodukte |
| Jimmy Green Marine (UK) | jimmygreenmarineco.uk | Anker-Spezialist | UK/EU | Hervorragende Anker-Beratung |
| Plastimo (FR) | plastimo.com | Umfangreich | EU | Eigenmarke, gutes P/L |

---

## 9. Bordwerkzeug für Ankersystem

### 9.1 Basis-Werkzeugset (muss an Bord sein)

| Werkzeug | Verwendung | Preis (2026) | Empfohlenes Produkt |
|----------|-----------|:------------:|-------------------|
| Messschieber (150 mm) | Kettenmessung, Bolzen, Glieddicke | 15–30 EUR | Mitutoyo 530-101 oder Helios-Preisser |
| Multimeter (digital) | Spannungsmessung, Durchgang | 20–40 EUR | Fluke 101 oder UNI-T UT61E |
| Schraubenschlüssel-Set (8–24 mm) | Schäkel, Windlass-Schrauben | 25–50 EUR | Hazet, Gedore oder Proxxon |
| Ring-Maulschlüssel-Set | Windlass-Bolzen, Befestigung | 25–50 EUR | Hazet 600N-Reihe |
| Schraubendreher-Set (PH/SL) | Windlass-Motor, Abdeckungen | 15–30 EUR | Wera Kraftform |
| Zange (Kombizange, Seitenschneider) | Drahtwicklung, Kabelbinder | 15–25 EUR | Knipex 03 01 180 |
| Drahtbürste (Stahl + Messing) | Reinigung Kette, Kontakte | 5–10 EUR | Diverse |
| Lupe (10×) | Schweißnaht-Inspektion | 8–15 EUR | Leuchtlupe LED |
| Kabelbinder (UV-beständig) | Markierung, Befestigung | 5–10 EUR | Diverse (UV-stabil, schwarz) |
| WD-40 / Kontaktspray | Lösen, Schmieren, Kontakte | 8–12 EUR | WD-40 Specialist |
| Tef-Gel (30 g) | Anti-Seize, galvanische Isolation | 12–18 EUR | Tef-Gel Original |
| Getriebeöl (250 ml) | Windlass-Ölwechsel | 8–12 EUR | SAE 80W-90 GL-4 |

**Gesamt Basis-Set:** ca. 160–300 EUR

### 9.2 Erweitertes Werkzeugset (empfohlen für Langfahrt)

| Werkzeug | Verwendung | Preis (2026) | Empfohlenes Produkt |
|----------|-----------|:------------:|-------------------|
| Zinkspray (400 ml) | Galv.-Ausbesserung unterwegs | 8–15 EUR | CRC Zinc-It |
| Farbeindringprüf-Set | Riss-Erkennung Schweißnähte | 28–35 EUR | MR Chemie Prüfset Nr. 1 |
| Lanocote (120 g) | Korrosionsschutz, Schmierung | 18–25 EUR | Forespar Lanocote |
| Ersatz-Kohlebürsten (Paar) | Windlass-Motor | 25–45 EUR | Passend zum installierten Modell |
| Ersatz-Wellendichtung | Windlass-Dichtung | 12–28 EUR | Passend zum installierten Modell |
| Ersatz-Solenoid | Windlass-Steuerung | 75–120 EUR | Passend zum installierten Modell |
| Notglieder (3×) | Ketten-Reparatur unterwegs | 15–30 EUR | Passend zur Kettendicke |
| Ersatz-Schäkel (3×) | Verbindung Anker/Kette/Swivel | 10–25 EUR | Passend |
| Schrumpfschlauch-Set | Kabelreparatur | 8–12 EUR | Diverse |
| Kabelschuhe (sortiert) | Kabelreparatur | 10–15 EUR | Ringkabelschuhe, verzinnt |
| Crimpzange | Kabelschuh-Montage | 20–35 EUR | Knipex 97 22 240 |
| Schleifvlies (K120, K400) | Kontaktreinigung | 5–8 EUR | Diverse |

**Gesamt Erweitertes Set:** ca. 235–395 EUR

### 9.3 Werkzeug-Stauliste

| Werkzeug-Gruppe | Stauraum | Hinweis |
|----------------|----------|---------|
| Mess-Werkzeuge (Messschieber, Multimeter) | Navigationstisch / Werkzeugkiste | Feuchtigkeitsgeschützt! |
| Schraubenschlüssel / Zangen | Vorschiffs-Staukasten oder Motorraum | Nahe Windlass |
| Chemie (Tef-Gel, Spray, Öl) | Separate Box, aufrecht | Auslaufschutz! |
| Ersatzteile (Bürsten, Dichtung, Solenoid) | Trockener Staukasten | In Zip-Lock-Beutel |
| Verbrauchsmaterial (Kabelbinder, Draht) | Werkzeugkiste | — |

---

## 10. Fehlerbild-Atlas

### 10.1 Fehlerbild F-17_08-01: Kettenverlust beim Ankern

#### 10.1.1 Symptome
- Kette rauscht unkontrolliert aus dem Kettenkasten
- Windlass reagiert nicht oder kommt nicht gegen die Last an
- Rattterndes Geräusch, dann plötzliche Stille = Ende der Kette
- Anker und gesamte Kette verloren

#### 10.1.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Kupplung/Clutch nicht korrekt eingerastet | Hoch | Kupplungshebel-Stellung prüfen |
| Endpunkt-Befestigung gerissen | Hoch | Kettenende im Kasten prüfen |
| Kettenstopper nicht eingelegt | Mittel | Kettenstopper-Stellung prüfen |
| Windlass-Sicherung durchgebrannt | Mittel | Sicherung prüfen |
| Kette zu schnell gefiert (Freilauf) | Mittel | Bedienfehler |
| Korrodiertes Verbindungsglied gebrochen | Niedrig | Verbindungsglieder inspizieren |

#### 10.1.3 Sofortmaßnahmen
1. Ruhe bewahren — Position sofort notieren (GPS)
2. Motor starten, Position halten
3. Tiefe prüfen — ggf. Taucher / Bergedienst
4. Ankerposition markieren (Fender mit Leine als Boje)
5. Alternative Ankerlösung (Zweitanker, Hafen anlaufen)

#### 10.1.4 Prävention
- Kettenendpunkt IMMER mit Dyneema-Leine befestigen (KEIN Metalldraht!)
- Leine muss unter Extremlast brechen → Schiff nicht am Kettenkasten verankert
- Kettenstopper bei jedem Ankern einlegen
- Windlass-Kupplung nach dem Fieren IMMER einrasten
- Fieren kontrolliert (in Etappen, mit Bremswirkung der Kupplung)

### 10.2 Fehlerbild F-17_08-02: Kette klemmt im Kettenkasten

#### 10.2.1 Symptome
- Kette stoppt beim Hieven plötzlich
- Windlass-Motor überlastet (Überhitzung, Sicherung löst aus)
- Kette lässt sich weder hieven noch fieren
- Dumpfes Rasseln aus dem Kettenkasten

#### 10.2.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Kette hat sich im Kasten vertörnt | Hoch | Luke öffnen, Kette inspizieren |
| Kettenkasten zu klein (Design-Fehler) | Mittel | Kasten-Volumen vs. Kettenlänge |
| Kette hat sich um Endpunkt-Leine gewickelt | Mittel | Luke öffnen |
| Fremdkörper im Kasten | Niedrig | Inspektion |
| Kettenrohr verstopft (Schlick, Muscheln) | Niedrig | Kettenrohr inspizieren |

#### 10.2.3 Sofortmaßnahmen
1. Windlass sofort stoppen (Überhitzungsgefahr!)
2. Kettenstopper einlegen (Last von der Winde nehmen)
3. Kettenkasten-Luke öffnen
4. Kette von Hand entwirren (Handschuhe!)
5. Ggf. Kette von unten nachschieben
6. Langsam weiter hieven

#### 10.2.4 Prävention
- Kette beim Fieren kontrolliert ablegen (nicht unkontrolliert fallen lassen)
- Kettenkasten regelmäßig reinigen
- Kettenfallrohr prüfen (Durchmesser ≥ 5× Kettenglieddicke)
- Kettenkasten groß genug dimensionieren (Volumen ≥ 3× Kettenvolumen)

### 10.3 Fehlerbild F-17_08-03: Windlass-Motor dreht nicht

#### 10.3.1 Symptome
- Kein Motorgeräusch bei Betätigung des Fußschalters
- Solenoid klickt evtl. hörbar
- Display / Kettenzähler funktioniert ggf.

#### 10.3.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Sicherung durchgebrannt | Hoch | Sicherung visuell und mit Multimeter prüfen |
| Batteriehauptschalter AUS | Hoch | Schalterstellung prüfen |
| Solenoid defekt | Mittel | Klick hörbar? Spannung am Solenoid-Ausgang? |
| Kohlebürsten verschlissen | Mittel | Motor öffnen, Bürstenlänge prüfen |
| Korrodierte Kabelverbindung | Mittel | Spannungsabfall an jeder Klemme messen |
| Motor-Wicklung durchgebrannt | Niedrig | Widerstand Motor messen (typisch 0,02–0,1 Ω) |
| Fußschalter defekt | Niedrig | Steuerkabel am Solenoid brücken (kurz!) |
| Batterie leer | Niedrig | Batteriespannung prüfen (>12,0 V) |

#### 10.3.3 Sofortmaßnahmen
1. Batterie-Hauptschalter prüfen
2. Sicherung prüfen (visuell + Multimeter)
3. Batteriespannung prüfen (>12,0 V in Ruhe)
4. Solenoid-Klick prüfen (Ohr an das Solenoid)
5. Falls Solenoid klickt, Motor nicht dreht → Kohlebürsten prüfen
6. Falls Solenoid nicht klickt → Steuerkabel / Fußschalter prüfen

#### 10.3.4 Notfall-Lösung
- Handkurbel verwenden (falls vorhanden)
- Kette von Hand hieven (Handschuhe, Rücken schonen!)
- Bei schwerem Anker: Boot über den Anker fahren, Kette an Klampe belegen

### 10.4 Fehlerbild F-17_08-04: Windlass arbeitet nur langsam

#### 10.4.1 Symptome
- Motor dreht, aber deutlich langsamer als normal
- Kette wird nur mühsam gehoben
- Motor wird warm / heiß
- Betriebsgeräusch dumpfer als normal

#### 10.4.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Niedrige Batteriespannung | Hoch | Spannung unter Last messen (<10,5 V = Problem) |
| Korrodierte Kabelverbindungen | Hoch | Spannungsabfall an Klemmen messen |
| Kabelquerschnitt zu gering | Mittel | Querschnitt prüfen vs. Herstellerangabe |
| Verschlissene Kohlebürsten | Mittel | Bürstenlänge prüfen |
| Getriebe schwergängig (Öl alt) | Mittel | Ölzustand prüfen |
| Kupplung schleift | Niedrig | Kupplung prüfen (Durchrutschen?) |
| Motor-Wicklung teildefekt | Niedrig | Widerstand messen, Fachwerft |

#### 10.4.3 Sofortmaßnahmen
1. Batteriespannung unter Last messen
2. Klemmen auf Korrosion / Erwärmung prüfen
3. Last reduzieren (Boot über Anker fahren)
4. Motor in kurzen Intervallen betreiben (30 sek an, 60 sek aus)

### 10.5 Fehlerbild F-17_08-05: Kette springt aus der Kettennuss

#### 10.5.1 Symptome
- Kette rutscht oder springt bei Belastung aus der Nuss
- Schlagende Kette (Verletzungsgefahr!)
- Kette wird nicht sauber transportiert
- Knackende / klappernde Geräusche

#### 10.5.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Falsche Kette für die Nuss (DIN 766 vs. 764) | Hoch | Kettenstandard prüfen |
| Kettennuss verschlissen | Mittel | Zahnprofil prüfen |
| Kette elongiert (Glieder zu lang) | Mittel | 10-Glieder-Messung |
| Kette verschlissen (Glieder zu dünn) | Mittel | Glieddicke messen |
| Bugrolle-Führung falsch ausgerichtet | Niedrig | Kettenlauf beobachten |
| Verdrehte Glieder in der Kette | Niedrig | Kette auslegen |

#### 10.5.3 Sofortmaßnahmen
1. Windlass sofort stoppen!
2. Kette sichern (Kettenstopper, Klampe)
3. Kettenstandard prüfen (DIN 766 / 764 / ISO)
4. Kette auf Elongation prüfen (10-Glieder-Maß)
5. Kettennuss-Zahnprofil inspizieren

### 10.6 Fehlerbild F-17_08-06: Wassereinbruch im Windlass-Motorraum

#### 10.6.1 Symptome
- Wasseransammlung unter Deck an der Windlass-Position
- Korrosion am Motor und an Kabelverbindungen
- Getriebeöl milchig (Wasser im Öl)
- Motor läuft unruhig oder fällt sporadisch aus

#### 10.6.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Wellendichtung undicht | Hoch | Sichtprüfung, Wassertest |
| Decksdichtung der Windlass-Basis undicht | Hoch | Dichtmasse prüfen |
| Kettenrohr-Dichtung undicht | Mittel | Kettenrohr inspizieren |
| Kondensation im Kettenkasten | Mittel | Belüftung prüfen |
| Leckage an Deckshardware (Klampe, Schrauben) | Niedrig | Systematisch abdichten |

#### 10.6.3 Sofortmaßnahmen
1. Motor trocknen (Lappen, Heißluft — NICHT direkt, Abstand 30 cm)
2. Getriebeöl prüfen (milchig = Wasser → sofort wechseln)
3. Elektrische Verbindungen trocknen, reinigen
4. Ursache der Leckage finden und abstellen

### 10.7 Fehlerbild F-17_08-07: Schäkelbruch oder Wirbel-Versagen

#### 10.7.1 Symptome
- Plötzlicher Lastverlust beim Ankern
- Kette noch vorhanden, aber Anker verloren (oder umgekehrt)
- Gebrochener/deformierter Schäkel oder Wirbel

#### 10.7.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Unterdimensionierter Schäkel | Hoch | WLL vs. Kettenstärke vergleichen |
| Korrosion (Spaltkorrosion, Lochfraß) | Hoch | Gebrochene Teile inspizieren |
| Ermüdungsbruch (Wechselbelastung) | Mittel | Bruchfläche analysieren |
| Material-Verwechslung (304 statt 316L) | Mittel | Magnettest am Rest |
| Galvanische Korrosion | Mittel | Kontaktmetalle prüfen |
| Fehlende Sicherung (Bolzen löste sich) | Niedrig | Bolzen gesucht? |

#### 10.7.3 Prävention
- Schäkel und Wirbel IMMER auf Kette-Bruchlast dimensionieren
- NUR 316L Edelstahl oder hochfest verzinkten Stahl verwenden
- Bolzen IMMER mit Drahtwicklung sichern
- Jährliche Inspektion aller Verbindungselemente
- Tef-Gel auf alle Kontaktstellen ungleicher Metalle

### 10.8 Fehlerbild F-17_08-08: Anker gräbt sich nicht ein

#### 10.8.1 Symptome
- Boot treibt trotz gelegter Kette
- GPS-Ankeralarm löst aus
- Anker kommt sauber hoch (kein Grund-Material)

#### 10.8.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Zu wenig Kette/Scope | Hoch | Streckverhältnis prüfen (min. 5:1 Kette) |
| Ankertyp ungeeignet für Untergrund | Hoch | Seekarte: Untergrundtyp prüfen |
| Verbogener Schaft | Mittel | Schaft-Geradheit prüfen |
| Stumpfe Flunke | Mittel | Flunke-Spitze prüfen |
| Seegras auf dem Grund | Mittel | Anker hochholen, Seegras am Anker? |
| Flunke-Gelenk blockiert (Danforth) | Niedrig | Gelenk prüfen |

#### 10.8.3 Sofortmaßnahmen
1. Mehr Kette stecken (Scope erhöhen)
2. Rückwärts einlaufen (Eingrabeimpuls)
3. Position wechseln (anderer Untergrund)
4. Zweitanker setzen

### 10.9 Fehlerbild F-17_08-09: Snubber-Versagen

#### 10.9.1 Symptome
- Rhythmisches Rucken am Bug
- Kettenlärm (Kette schlägt gegen Bugrolle/Klüse)
- Snubber-Leine gerissen oder aus der Kettenklaue gerutscht
- Erhöhte Belastung der Windlass

#### 10.9.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Snubber-Leine gerissen (Alter, UV) | Hoch | Leine inspizieren |
| Kettenklaue/Hook geöffnet | Hoch | Hook prüfen |
| Snubber unterdimensioniert | Mittel | Leinendurchmesser vs. Bootsgröße |
| Schamfil-Schutz durchgescheuert | Mittel | Schamfilstelle prüfen |
| Zu kurzer Snubber | Niedrig | Empfohlen: 5–8 m Länge |

#### 10.9.3 Sofortmaßnahmen
1. Ersatz-Snubber anlegen
2. Notfalls: Festmacher als Snubber verwenden
3. Kette leicht auf Winde nehmen (Durchhang schaffen)
4. Schamfil-Schutz an Klüse anbringen (Handtuch, Schlauch)

### 10.10 Fehlerbild F-17_08-10: Kettenzähler zeigt falsche Werte

#### 10.10.1 Symptome
- Angezeigte Kettenlänge stimmt nicht mit Markierungen überein
- Kettenzähler driftet (Fehler wird über Zeit größer)
- Sprunghafte Anzeige

#### 10.10.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Sensor verschmutzt | Hoch | Sensor reinigen |
| Magnet im Kettenglied verschoben | Mittel | Magnet-Position prüfen |
| Sensor-Abstand falsch | Mittel | Abstand Sensor ↔ Kette prüfen |
| Kalibration verloren | Mittel | Neu kalibrieren |
| Sensor defekt | Niedrig | Sensor tauschen |
| Kette elongiert (Teilung stimmt nicht) | Niedrig | 10-Glieder-Maß prüfen |

#### 10.10.3 Sofortmaßnahmen
1. Sensor reinigen (Bürste, Kontaktspray)
2. Kettenzähler auf null setzen
3. Referenzmessung: 20 m Kette hieven, Anzeige vergleichen
4. Sensor-Abstand justieren (typ. 2–5 mm)
5. Neu kalibrieren gemäß Herstelleranleitung

### 10.11 Fehlerbild F-17_08-11: Bugrolle festgefressen

#### 10.11.1 Symptome
- Rolle dreht nicht mehr
- Kette/Leine schabt über stehende Rolle
- Quietschende / kreischende Geräusche
- Beschleunigte Abnutzung der Rolle und der Kette

#### 10.11.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Korrosion der Lagerachse | Hoch | Rolle abnehmen, Achse inspizieren |
| Salzablagerung im Lager | Hoch | Lager spülen |
| Deformierte Rolle (Überlast) | Mittel | Rolle auf Rundheit prüfen |
| Sand/Schlick im Lager | Mittel | Lager reinigen |
| Falsches Lagermaterial (Rost) | Niedrig | Lagermaterial identifizieren |

#### 10.11.3 Sofortmaßnahmen
1. WD-40 oder Teflonöl auf Lagerachse sprühen
2. Von Hand hin- und herbewegen
3. Falls nicht lösbar: Rolle abnehmen, Lager reinigen/ersetzen
4. Nach Reinigung: Lager mit Lanocote oder Teflonfett schmieren

### 10.12 Fehlerbild F-17_08-12: Galvanische Korrosion am Ankersystem

#### 10.12.1 Symptome
- Schneller Materialverlust an einer Komponente (unedleres Metall)
- Weißer Belag auf Aluminium (Alu-Anker)
- Brauner Rostbelag auf verzinktem Stahl trotz intakter Galvanisierung
- Lochfraß an Edelstahl in Kontaktbereichen

#### 10.12.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|:------------------:|----------|
| Ungleiche Metalle in direktem Kontakt | Hoch | Materialpaarungen identifizieren |
| Fehlende galvanische Isolation (Tef-Gel etc.) | Hoch | Kontaktstellen prüfen |
| Streustrom vom Landanschluss | Mittel | Isolationswiderstand prüfen |
| Defekte Opferanode am Rumpf | Mittel | Anoden prüfen |
| Bordnetz-Leckstrom | Niedrig | Leckstrommessung |

#### 10.12.3 Sofortmaßnahmen
1. Kontaktstellen trennen
2. Tef-Gel oder Duralac auftragen
3. Komponenten aus gleichem Material wählen
4. Opferanoden am Rumpf prüfen
5. Bei Verdacht auf Streustrom: Galvanischen Isolator einbauen

---

## 11. Troubleshooting

### 11.1 Entscheidungsbaum T01: Windlass reagiert nicht

```
Windlass reagiert nicht auf Fußschalter/Fernbedienung
│
├── Batterie-Hauptschalter EIN?
│   ├── NEIN → Einschalten. Problem gelöst?
│   │          ├── JA → Fertig
│   │          └── NEIN → Weiter
│   └── JA → Weiter
│
├── Sicherung intakt?
│   ├── NEIN → Sicherung ersetzen. Problem gelöst?
│   │          ├── JA → Ursache für Auslösung klären!
│   │          └── NEIN → Weiter
│   └── JA → Weiter
│
├── Batteriespannung >12,0 V (12V-System)?
│   ├── NEIN → Batterie laden. Problem gelöst?
│   │          ├── JA → Batteriezustand prüfen
│   │          └── NEIN → Weiter
│   └── JA → Weiter
│
├── Solenoid klickt beim Schalten?
│   ├── NEIN → Steuerstromkreis prüfen:
│   │          ├── Fußschalter Durchgang prüfen (Multimeter)
│   │          ├── Steuerkabel Durchgang prüfen
│   │          └── Solenoid-Spule prüfen (Widerstand typ. 0,5–2 Ω)
│   │              ├── Spule ok → Fußschalter/Kabel defekt → ersetzen
│   │              └── Spule defekt → Solenoid ersetzen
│   └── JA → Hauptstromkreis prüfen:
│            ├── Spannung am Motor messen (Solenoid-Ausgang)
│            │   ├── Spannung vorhanden → Motor defekt
│            │   │   ├── Kohlebürsten prüfen (<5mm → tauschen)
│            │   │   ├── Kommutator prüfen (glatt, braun = ok)
│            │   │   └── Motor-Wicklung prüfen (Fachwerft)
│            │   └── Keine Spannung → Solenoid-Kontakte defekt
│            │       └── Solenoid ersetzen
│            └── Spannungsabfall über gesamten Kreis messen
│                └── >10% → Korrodierte Verbindung(en) finden + reinigen
```

### 11.2 Entscheidungsbaum T02: Windlass arbeitet zu langsam

```
Windlass hievt deutlich langsamer als normal
│
├── Batteriespannung unter Last messen (am Motor)
│   ├── <10,5 V (12V) / <21 V (24V) → Batterie-Problem
│   │   ├── Batteriekapazität prüfen
│   │   ├── Kabelquerschnitt prüfen
│   │   └── Kabelverbindungen reinigen
│   └── >10,5 V → Weiter
│
├── Spannungsabfall über Kabel messen (Batterie ↔ Motor)
│   ├── >1,2 V (12V) / >2,4 V (24V) → Kabel-Problem
│   │   ├── Jede Verbindung einzeln prüfen
│   │   ├── Korrodierte Klemmen reinigen
│   │   └── Ggf. Kabel erneuern (größerer Querschnitt)
│   └── <1,2 V → Weiter
│
├── Getriebeöl prüfen
│   ├── Milchig → Wasser im Getriebe → Ölwechsel + Dichtung
│   ├── Schwarz → Überhitzt → Ölwechsel + Ursache
│   ├── Metallspäne → Zahnverschleiß → Fachwerft
│   └── OK → Weiter
│
├── Kohlebürsten prüfen
│   ├── <5 mm → Tauschen
│   └── >5 mm → Weiter
│
├── Kupplung prüfen
│   ├── Rutscht unter Last → Kupplungsbelag ersetzen
│   └── Hält → Weiter
│
└── Motor-Problem (intern) → Fachwerft
```

### 11.3 Entscheidungsbaum T03: Kette rutscht auf Kettennuss

```
Kette rutscht oder springt auf der Kettennuss
│
├── Kettenstandard prüfen: DIN 766 / DIN 764 / ISO?
│   ├── Kette passt NICHT zur Nuss → Richtige Kette beschaffen
│   └── Kette passt → Weiter
│
├── Kettendicke messen (Messschieber)
│   ├── <85% Nenndicke → Kette ablegereif → ersetzen
│   └── >85% → Weiter
│
├── Elongation prüfen (10-Glieder-Maß)
│   ├── >103% → Kette elongiert → ersetzen
│   └── <103% → Weiter
│
├── Kettennuss-Zahnprofil prüfen
│   ├── Zähne abgenutzt / abgerundet → Kettennuss ersetzen
│   └── Profil ok → Weiter
│
├── Verdrehte Glieder in der Kette?
│   ├── JA → Betroffenen Abschnitt ersetzen
│   └── NEIN → Weiter
│
└── Kettenlauf-Führung prüfen (Bugrolle → Kettennuss)
    ├── Kette kommt schräg an → Bugrolle/Klüse ausrichten
    └── Kette kommt gerade → Kombination aus Verschleiß → Kette UND Nuss ersetzen
```

### 11.4 Entscheidungsbaum T04: Anker hält nicht

```
Anker hält nicht (Boot treibt trotz Ankermanöver)
│
├── Scope (Streckverhältnis) prüfen
│   ├── Kette <5:1 → Mehr Kette stecken
│   ├── Kette+Leine <7:1 → Mehr Leine stecken
│   └── Scope ausreichend → Weiter
│
├── Eingrabemanöver korrekt?
│   ├── NEIN → Rückwärts einlaufen lassen, Kette straffen
│   └── JA → Weiter
│
├── Anker-Zustand prüfen (beim nächsten Hochholen)
│   ├── Seegras am Anker → Seegras-Grund, Position wechseln
│   ├── Anker sauber → Harter Grund (Fels/Kies), Ankertyp wechseln
│   ├── Schaft verbogen → Anker ersetzen
│   ├── Flunke-Gelenk blockiert (Danforth) → Gelenk lösen/schmieren
│   └── Flunke stumpf → Nachschleifen oder Anker ersetzen
│
├── Untergrund prüfen (Seekarte, Echolot)
│   ├── Fels / Koralle → Zweitanker (Klappanker/Grapnel)
│   ├── Seegras → Position wechseln (sandige Stelle suchen)
│   ├── Schlick (sehr weich) → Anker mit größerer Fläche (Fortress)
│   └── Sand/Ton → Anker sollte halten → Weiter prüfen
│
└── Anker unterdimensioniert?
    ├── Gewicht < Herstellerempfehlung → Größeren Anker beschaffen
    └── Gewicht ok → Ankertyp für diesen Untergrund ungeeignet
```

### 11.5 Entscheidungsbaum T05: Geräusche / Vibrationen der Windlass

```
Ungewöhnliche Geräusche oder Vibrationen beim Windlass-Betrieb
│
├── Art des Geräuschs?
│   ├── Kreischen / Quietschen
│   │   ├── Lager trocken → Schmieren (Teflonfett)
│   │   ├── Kohlebürsten → Prüfen, ggf. tauschen
│   │   └── Kupplung schleift → Kupplung justieren
│   │
│   ├── Rattern / Klappern
│   │   ├── Kette springt auf Nuss → siehe T03
│   │   ├── Getriebe-Spiel → Fachwerft (Zahnverschleiß)
│   │   └── Lose Teile → Schrauben prüfen
│   │
│   ├── Brummen / Summen (stark)
│   │   ├── Motor unter Überlast → Last reduzieren
│   │   ├── Solenoid-Brummen → Solenoid-Kontakte reinigen
│   │   └── Befestigung locker → Schrauben nachziehen
│   │
│   ├── Knirschen / Mahlen
│   │   ├── Sand/Dreck im Getriebe → Reinigen, Öl wechseln
│   │   ├── Zahnrad-Verschleiß → Fachwerft
│   │   └── Kupplung → Kupplungsbelag prüfen
│   │
│   └── Knacken (einzelne Schläge)
│       ├── Verdrehte Kettenglieder → Kette prüfen
│       ├── Fremdkörper an Kettennuss → Reinigen
│       └── Getriebe-Zahnrad beschädigt → Fachwerft
│
└── Vibration ohne Geräusch
    ├── Befestigungsschrauben prüfen → Nachziehen
    ├── Motor-Anker unwuchtig → Fachwerft
    └── Backing Plate gebrochen → Deck / Unterbau inspizieren
```

---

## 12. FAQ

### 12.1 Allgemeine Wartungsfragen

**F12.1.1: Wie oft muss ich mein Ankersystem komplett inspizieren?**

Mindestens einmal pro Jahr (Pre-Season). Bei intensiver Nutzung (Langfahrt,
tägliches Ankern) alle 6 Monate. Nach Sturmankern oder Festsitz-Anker
sofort eine erweiterte Inspektion durchführen.

---

**F12.1.2: Kann ich die Wartung selbst durchführen oder brauche ich eine Werft?**

Die meisten Wartungsarbeiten (ca. 80 %) kann ein technisch versierter
Eigner selbst durchführen. Werkstatt-Arbeiten sind nötig bei:
- Neuverzinkung (Fachbetrieb)
- Motor-Wicklungsschäden (Elektro-Fachwerft)
- Getriebe-Reparatur (Windlass-Fachwerft)
- NDT-Prüfung (zerstörungsfreie Prüfung)
- Deck-Verstärkung / Backing-Plate-Nachrüstung

---

**F12.1.3: Was kostet die jährliche Wartung des Ankersystems?**

Eigenleistung: 80–350 EUR Materialkosten (je nach Bootsgröße).
Fachwerft: 250–2.500 EUR inkl. Arbeitskosten (je nach Bootsgröße und
Umfang). Siehe Abschnitt 2.5 für Details.

---

**F12.1.4: Welche Wartungsarbeiten kann ich im Wasser erledigen?**

Im Wasser (am Liegeplatz): Sichtprüfung beim Ankermanöver,
Süßwasserspülung, elektrische Prüfungen, Fußschalter-Test. An Land:
Kette komplett auslegen, Windlass-Motor öffnen, Getriebeöl wechseln,
Neuverzinkung.

---

**F12.1.5: Muss ich die Kette jedes Jahr komplett auslegen?**

Ja, mindestens einmal pro Jahr bei der Pre-Season-Inspektion. Das
vollständige Auslegen ist die einzige Möglichkeit, den Zustand der
gesamten Kette zu beurteilen. Dabei Glieddicke messen, Galvanisierung
bewerten, verdrehte Glieder suchen.

---

### 12.2 Ketten-Fragen

**F12.2.1: Wie lange hält eine Ankerkette?**

Feuerverzinkte Stahlkette (DIN 766): 8–15 Jahre bei normaler Nutzung.
Edelstahlkette (316L): 20–30+ Jahre. Die tatsächliche Lebensdauer hängt
von Nutzungsintensität, Gewässer (Salz/Süß), Spülung nach dem Ankern
und Lagerung (Winter) ab.

---

**F12.2.2: Wann muss ich die Kette ersetzen?**

Sofort bei: Glieddicke <85 % Nenn, Elongation >105 %, sichtbarem Lochfraß,
gebrochenem Glied. Planmäßig bei: Glieddicke 85–90 % mit weiteren Befunden,
Elongation 103–105 %, Galvanisierung <30 % bei gleichzeitiger Dickenverlust.
Siehe Abschnitt 3.5 für die Entscheidungsmatrix.

---

**F12.2.3: Kann ich nur ein Teilstück der Kette ersetzen?**

Ja, mit einem kalibrierten Verbindungsglied (Notglied). Jedoch:
1. Neues Stück muss EXAKT gleiche Norm (DIN 766, gleiche Dicke) haben.
2. Verbindungsglied muss min. gleiche Bruchlast haben.
3. Kombination alt/neu kann auf der Kettennuss Probleme machen (unterschiedliche Abnutzung).
4. Empfehlung: Nur bei Notfall-Reparatur unterwegs. Bei Pre-Season: Gesamte Kette ersetzen.

---

**F12.2.4: DIN 766 oder DIN 764 — was ist der Unterschied?**

DIN 766: Kurzgliedrige Rundstahlkette (kalibriert). Standard für die
meisten Ankerwindlass-Kettennüsse. DIN 764: Langgliedrige Kette (nicht
kalibriert, andere Teilung). Die beiden sind NICHT austauschbar! Die
Kettennuss ist für einen bestimmten Standard gefertigt. Falsche Kette
→ Rutschen oder Klemmen.

---

**F12.2.5: Lohnt sich eine Edelstahlkette?**

Vorteile: Kein Rosten, keine Neuverzinkung, längere Lebensdauer (20–30+ Jahre),
sauberer (keine Rostflecken an Deck). Nachteile: 3–4× teurer, schwerer als
verzinkte Kette gleicher Stärke (bei gleichem Volumen), Spaltkorrosion möglich,
NICHT mit verzinkten Teilen mischen (galvanische Korrosion). Empfehlung:
Für Langfahrer und bei Booten mit weißem Deck lohnend.

---

**F12.2.6: Wie markiere ich meine Kette am besten?**

Farbige Kabelbinder (UV-beständig, schwarz oder bunt) alle 10 Meter sind
die einfachste und haltbarste Methode. Farbspray-Markierung ist gut
sichtbar, muss aber jährlich erneuert werden. Siehe Abschnitt 3.7 für
Details und Farbschema.

---

### 12.3 Windlass-Fragen

**F12.3.1: Wie oft muss ich das Getriebeöl wechseln?**

Bei normaler Nutzung: Alle 12 Monate (Pre-Season). Bei intensiver
Nutzung (tägliches Ankern): Alle 6 Monate. Sofort bei milchigem Öl
(Wassereinbruch) oder metallisch glänzendem Öl (Zahnverschleiß).
Siehe Abschnitt 5.2 für Details.

---

**F12.3.2: Wie erkenne ich verschlissene Kohlebürsten?**

Motor öffnen (4 Schrauben), Bürsten herausnehmen, Länge messen.
Neuzustand: ca. 20 mm. Tauschen bei: <5 mm. Typische Lebensdauer:
500–1.000 Betriebsstunden oder 5–8 Jahre bei normaler Nutzung.

---

**F12.3.3: Welches Öl nehme ich für die Windlass?**

SAE 80W-90 Getriebeöl, API GL-4 oder GL-5. Das ist Standard-KFZ-
Getriebeöl und in jedem Baumarkt erhältlich. Einige Hersteller bieten
auch Original-Öl an (meist teurer, gleiche Spezifikation). Menge:
typisch 80–300 ml je nach Modell.

---

**F12.3.4: Meine Windlass hat eine Handkurbel-Option — muss ich die pflegen?**

Ja! Handkurbel-Mechanismus jährlich prüfen: Steckverbindung gangbar?
Kurbel vorhanden und erreichbar? Im Notfall (Motorausfall) ist die
Handkurbel die einzige Möglichkeit, den Anker zu bergen. Steckverbindung
mit Lanocote schmieren.

---

**F12.3.5: Kann ich die Windlass zum Losreißen eines festsitzenden Ankers verwenden?**

NEIN! Die Windlass ist nicht für Losreiß-Kräfte ausgelegt. Das korrekte
Verfahren: Boot langsam über den Anker fahren (Motor), Kette auf Klampe
belegen (nicht auf Winde!), dann mit Motorleistung losreißen. Die
Klampe und der Kettenkanal sind für hohe Lasten ausgelegt, die Winde nicht.

---

**F12.3.6: Muss ich die Windlass abdecken?**

Empfohlen! Eine Neopren- oder Canvas-Abdeckung schützt vor UV, Salzwasser
und Schmutz. Kosten: 20–60 EUR. Lebensdauer der Windlass wird deutlich
verlängert. Besonders wichtig bei Booten, die überwiegend am Steg liegen
und die Windlass selten nutzen.

---

### 12.4 Galvanisierungs-Fragen

**F12.4.1: Wie lange hält die Feuerverzinkung einer Kette?**

Im Salzwasser bei regelmäßiger Nutzung und Süßwasserspülung: 5–10 Jahre.
Im Süßwasser: 15–25 Jahre. Ohne Süßwasserspülung im Salzwasser: 3–5 Jahre.
Die Lebensdauer der Verzinkung ist der limitierende Faktor für die
Kettenlebensdauer.

---

**F12.4.2: Kann ich meine Kette selbst neuverzinken?**

Nein! Feuerverzinkung erfordert ein 450°C heißes Zinkbad und ist nur in
spezialisierten Verzinkereien möglich. Was Sie selbst tun können:
Zinkspray als Übergangslösung auftragen (siehe Abschnitt 6.4). Das
verlängert die Lebensdauer um 6–18 Monate, ist aber kein Ersatz für
professionelle Feuerverzinkung.

---

**F12.4.3: Was kostet die Neuverzinkung meiner Kette?**

Abhängig vom Gewicht der Kette. Richtwerte (2026):
- 8 mm × 50 m (69 kg): 180–280 EUR
- 10 mm × 60 m (132 kg): 320–500 EUR
- 10 mm × 80 m (176 kg): 400–620 EUR
Hinzu kommen Transportkosten. Sammelaufträge über Yachtclubs senken
die Kosten um 20–30 %. Siehe Abschnitt 6.3 für Details.

---

**F12.4.4: Ist Zinkspray ein sinnvoller Zwischenschritt?**

Ja! Zinkspray (z.B. CRC Zinc-It, 12–15 EUR/Dose) ist eine gute
Zwischenlösung, wenn die Verzinkung teilweise abgenutzt ist (Stufe
G3–G4). Es verlängert die Lebensdauer um 6–18 Monate und schützt
vor weiterem Rostfortschritt. Kein Ersatz für Neuverzinkung, aber
sinnvoll als Überbrückung.

---

### 12.5 Korrosionsschutz-Fragen

**F12.5.1: Was ist Tef-Gel und wofür brauche ich es?**

Tef-Gel ist ein PTFE-basiertes Anti-Seize-Gel, das ungleiche Metalle
voneinander isoliert und galvanische Korrosion verhindert. Im
Ankersystem unverzichtbar an allen Stellen, wo unterschiedliche Metalle
in Kontakt kommen (z.B. Edelstahl-Wirbel ↔ verzinkte Kette, Edelstahl-
Schrauben ↔ Aluminium-Beschlag). Preis: 12–18 EUR (30 g Tube), reicht
für das gesamte Ankersystem + Restmenge.

---

**F12.5.2: Was ist der Unterschied zwischen Tef-Gel, Duralac und Lanocote?**

- **Tef-Gel**: PTFE-basiert, universell, Anti-Seize + Isolation. Für
  Schraubverbindungen und bewegliche Teile.
- **Duralac**: Chromat-basiert, bildet feste Schicht, speziell für
  Aluminium ↔ Edelstahl. Schwer zu entfernen.
- **Lanocote**: Lanolin-basiert, weich, biologisch abbaubar. Für bewegliche
  Teile, Bolzen, regelmäßig nachzufetten.

Empfehlung: Tef-Gel als Universalmittel für das Ankersystem. Lanocote
zusätzlich für bewegliche Teile (Schäkel, Wirbel, Bugrolle).

---

**F12.5.3: Wie verhindere ich Korrosion an meiner Edelstahl-Bugrolle?**

1. Regelmäßig mit Süßwasser spülen (nach jedem Ankern).
2. Edelstahlreiniger verwenden (1× monatlich).
3. Kontaktpunkte zu anderen Metallen mit Tef-Gel isolieren.
4. Bolzen und Lager mit Lanocote schmieren.
5. Bei Tea Staining: Polieren + Passivieren (Edelstahlpflege).

---

**F12.5.4: Mein Alu-Anker (Fortress) zeigt weißen Belag — ist das Korrosion?**

Weißer Belag auf Aluminium ist Aluminiumoxid — eine natürliche
Schutzschicht. Solange der Belag gleichmäßig und nicht tief ist, ist
das unbedenklich und sogar schützend. Problematisch wird es, wenn der
Belag krümelig wird oder Lochfraß darunter sichtbar ist — dann liegt
galvanische Korrosion vor (wahrscheinlich durch Kontakt mit Edelstahl-
Schäkel ohne Isolation). Maßnahme: Duralac oder Tef-Gel auf die
Kontaktstelle.

---

### 12.6 Sonstige Fragen

**F12.6.1: Kann ich meine verzinkte Kette und Edelstahl-Ausrüstung mischen?**

Ja, aber NUR mit galvanischer Isolation! Die Spannungsdifferenz zwischen
verzinktem Stahl und Edelstahl 316L beträgt ~900 mV — das ist erheblich
und führt ohne Isolation zu beschleunigter Korrosion des Zinks. Tef-Gel
auf alle Kontaktstellen auftragen und regelmäßig erneuern.

---

**F12.6.2: Wie lagere ich Anker und Kette über den Winter richtig?**

1. Gründlich mit Süßwasser reinigen.
2. Vollständig trocknen lassen.
3. Galvanisierung inspizieren, ggf. Zinkspray.
4. Trocken, belüftet lagern (NICHT auf dem Boden, NICHT in Plastiktüte).
5. Holzpalette oder Regal.
6. Nicht draußen lagern (Feuchtigkeit, Regen).

---

**F12.6.3: Mein Kettenkasten stinkt — was tun?**

Geruch entsteht durch anaerobe Zersetzung von Schlick und organischem
Material in Kombination mit stehendem Wasser. Abhilfe:
1. Kette komplett entnehmen.
2. Kettenkasten mit Hochdruckreiniger reinigen.
3. Desinfizieren (Essigessenz 1:3 mit Wasser, einwirken lassen, spülen).
4. Drainage prüfen und reinigen.
5. Belüftung sicherstellen.
6. Nach jedem Ankern: Kette mit Süßwasser spülen (Salzwasser + Schlick
   sind die Hauptursache).

---

**F12.6.4: Welche Snubber-Länge und -Durchmesser brauche ich?**

Faustregel:
- Länge: 5–8 Meter (länger = bessere Dämpfung)
- Durchmesser: Dreisträngiges Nylon

| Bootslänge | Snubber-Durchmesser | Snubber-Länge |
|:----------:|:-------------------:|:-------------:|
| 8–10 m | 14–16 mm | 5–6 m |
| 10–12 m | 16–18 mm | 6–7 m |
| 12–14 m | 18–20 mm | 7–8 m |
| 14–18 m | 20–24 mm | 7–8 m |
| 18–22 m | 24–28 mm | 8–10 m |

---

**F12.6.5: Wie oft muss ich meinen Snubber ersetzen?**

Alle 3–5 Jahre bei normaler Nutzung. Sofort bei: aufgeriebenen Fasern,
Verlust der Elastizität, Schamfilschäden >25 % des Durchmessers. UV-
geschützt lagern verlängert die Lebensdauer erheblich.

---

**F12.6.6: Kann ich einen Festmacher als Snubber verwenden?**

Im Notfall ja, als Langzeitlösung nein. Festmacher (Polyester) haben
deutlich weniger Dehnung als Nylon und absorbieren daher die Stoßlasten
schlechter. Ein dedizierter Nylon-Snubber ist immer besser.

---

**F12.6.7: Wie sichere ich meinen Anker auf der Bugrolle?**

1. Kettenstopper einlegen (obligatorisch).
2. Anker-Sicherungspin oder -clip einsetzen.
3. Zusätzlich: Spanngurt über den Anker (bei schwerem Wetter).
4. Bei Langfahrt über offenes Wasser: Anker zusätzlich mit Leine an Decksauge sichern.

---

**F12.6.8: Was mache ich, wenn mein Anker festsitzt?**

1. NICHT mit der Windlass losreißen!
2. Kette auf Klampe belegen.
3. Boot langsam in verschiedene Richtungen über den Anker fahren (Motor).
4. Kettenrichtung umkehren (aus der Eingraberichtung ziehen).
5. Trip-Leine verwenden (falls vorher ausgebracht).
6. Kette verkürzen, dann mit Motorstoß losreißen.
7. Bei Versagen: Taucher oder Bergedienst.

---

**F12.6.9: Brauche ich eine Trip-Leine?**

Empfohlen bei: Felsigem Grund, Koralle, unbekanntem Untergrund mit
Hindernissen (Kabel, Rohre, Wracks). Nicht nötig bei: Sand, Schlick,
freiem Ankerplatz. Trip-Leine: 6–8 mm Polypropylen (schwimmend) oder
Dyneema, befestigt am Ankerkopf, Länge = Wassertiefe + 3 m.

---

**F12.6.10: Wie entsorge ich eine alte Ankerkette umweltgerecht?**

Ankerketten bestehen aus Stahl und sind zu 100 % recycelbar.
Entsorgung:
- Schrotthandel (bringt sogar Geld: ca. 0,15–0,25 EUR/kg Stahlschrott)
- Wertstoffhof (Metallschrott)
- NICHT in den Hausmüll, NICHT ins Wasser werfen

---

**F12.6.11: Kann ich statt Kette auch Ankerleine verwenden?**

Für die ersten Meter: NEIN. Die ersten 5–10 Meter sollten immer Kette
sein (Gewicht für horizontalen Zug, Schamfilschutz am Grund). Danach
kann eine Kette-Leinen-Kombination sinnvoll sein (leichter, günstiger).
Reine Leinenankerei ist nur für kleine Boote (<8 m) in geschützten
Gewässern akzeptabel — und dann mit Kettenvorstoß.

---

**F12.6.12: Was ist der Unterschied zwischen einem Wirbel und einem Kettenwirbel?**

Ein **Wirbel (Swivel)** ist ein Drehgelenk zwischen Anker und Kette, das
Verdrehungen der Kette kompensiert. Ein **Kettenwirbel** ist ein
Verbindungsglied zum Einfügen in die Kette (selten bei Ankerketten).
Im Ankersystem wird der Wirbel zwischen Anker-Schäkel und erstem
Kettenglied eingesetzt.

---

**F12.6.13: Muss ich einen Wirbel (Swivel) verwenden?**

Empfohlen, aber nicht zwingend. Vorteile: Verhindert Kettenverdrehung
(Kinking), erleichtert das Einfahren des Ankers in die Bugrolle. Nachteile:
Zusätzliches Bauteil = zusätzliche Bruchstelle. Wichtig: Wirbel muss
min. gleiche Bruchlast wie die Kette haben. NUR hochwertige Marine-
Wirbel verwenden (nicht den 5-EUR-Baumarkt-Wirbel!).

---

## 13. Glossar

| Begriff | Englisch | Definition |
|---------|----------|-----------|
| Ablegereif | End of service life | Zustand, in dem ein Bauteil seine Nutzungsgrenze erreicht hat und ersetzt werden muss |
| Ankerspill | Capstan | Vertikale Winde zum Ankern, die Kettennuss und ggf. Spillkopf trägt |
| Ankerwinsch | Windlass | Motorisierte Winde zum Hieven und Fieren des Ankers |
| Backing Plate | Backing plate | Verstärkungsplatte unter dem Deck für Bolzenmontage |
| Beizen | Pickling | Chemische Behandlung der Stahloberfläche vor dem Verzinken |
| Bügel (Anker) | Roll bar | Bügel am Anker, der das Aufstellen und Eingraben gewährleistet |
| Clutch | Clutch | Kupplung an der Windlass zum Ein-/Auskoppeln der Kettennuss |
| Duty Cycle | Duty cycle | Zulässiges Verhältnis von Betrieb zu Pause bei elektrischen Winden |
| Elongation | Elongation | Längung der Kette durch plastische Verformung unter Last |
| Feuerverzinkung | Hot-dip galvanizing | Eintauchen des Stahlteils in ein 450°C heißes Zinkbad |
| Fieren | Pay out / lower | Kontrolliertes Auslassen der Kette beim Ankern |
| Flunke | Fluke | Der in den Grund greifende Teil des Ankers |
| Fluxen | Fluxing | Behandlung mit Zinkammoniumchlorid vor der Feuerverzinkung |
| Freilauf | Free-fall / free-wheel | Zustand bei gelöster Kupplung, Kette läuft frei aus |
| Galvanische Korrosion | Galvanic corrosion | Elektrochemische Korrosion durch Kontakt ungleicher Metalle |
| Galvanische Isolation | Galvanic isolation | Trennung ungleicher Metalle durch isolierende Schicht |
| Hieven | Weigh / retrieve | Einholen des Ankers |
| Kaliberte Kette | Calibrated chain | Kette mit exakt definierten Abmessungen für Kettennuss-Eingriff |
| Kathodischer Schutz | Cathodic protection | Korrosionsschutz durch unedleres Opfermetall (z.B. Zink) |
| Kettenkasten | Chain locker | Stauraum unter Deck für die Ankerkette |
| Kettennuss | Gypsy / wildcat | Zahnrad an der Windlass, das die kalibrierte Kette transportiert |
| Kettenstopper | Chain stopper | Mechanische Vorrichtung zum Arretieren der Kette unter Last |
| Klüse | Hawsehole / fairlead | Führungsöffnung im Bug für Kette oder Leine |
| Kohlebürste | Carbon brush | Verschleißteil im Gleichstrommotor, überträgt Strom auf Kommutator |
| Kommutator | Commutator | Stromwender im Gleichstrommotor |
| Lochfraß | Pitting corrosion | Lokale, tiefe Korrosion in Form kleiner Löcher |
| Notglied | Connecting link | Verschraubbares Kettenglied zum Verbinden zweier Kettenenden |
| Opferanode | Sacrificial anode | Unedleres Metallteil, das sich statt des zu schützenden Teils auflöst |
| Passivierung | Passivation | Bildung einer schützenden Oxidschicht auf Edelstahl |
| Pilzanker | Mushroom anchor | Anker, der durch Gewicht und Form hält (Dauerverankerung) |
| Schaft | Shank | Stiel des Ankers, verbindet Flunke mit Schäkelöse |
| Schäkel | Shackle | U-förmiger Verbindungsbügel mit Bolzen |
| Schamfil | Chafe | Reibungsverschleiß an Leine oder Kette |
| Schwoikreis | Swing circle | Kreis, den das Boot beim Schwingen um den Anker beschreibt |
| Scope / Streckverhältnis | Scope | Verhältnis Ketten-/Leinenlänge zu Wassertiefe |
| Simmerring | Shaft seal / oil seal | Dichtring für rotierende Wellen |
| Snubber | Snubber / bridle | Elastische Leine zur Stoßdämpfung zwischen Kette und Boot |
| Solenoid | Solenoid | Elektromagnetischer Schalter für Windlass-Motoren |
| Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten mit Sauerstoffmangel |
| Spillkopf | Capstan head / drum | Zylindrischer Kopf an der Winde für Tauwerk |
| Streckverhältnis | Scope ratio | Verhältnis ausgelegte Kette/Leine zu Wassertiefe |
| Tea Staining | Tea staining | Oberflächliche Verfärbung von Edelstahl in salziger Umgebung |
| Tef-Gel | Tef-Gel | PTFE-basiertes Isolier- und Anti-Seize-Mittel |
| Teilung | Pitch | Abstand zwischen zwei gleichen Punkten benachbarter Kettenglieder |
| Trip-Leine | Trip line | Rückwärts-Leine am Ankerkopf zum Losreißen |
| Vertörnen | Fouling (chain) | Verwickeln oder Verdrehen der Kette |
| Wellendichtung | Shaft seal | Dichtung der durchgehenden Welle (Deck → Motor) |
| Wirbel / Swivel | Swivel | Drehgelenk zwischen Anker und Kette |
| Zinkschicht | Zinc coating | Verzinkungsschicht als Korrosionsschutz |

---

## 14. Schnell-Referenz

### 14.1 Wartungsintervalle auf einen Blick

```
ANKERSYSTEM — WARTUNGSINTERVALLE
=================================

NACH JEDEM ANKERN:
  □ Kette beim Hieven auf Beschädigungen beobachten
  □ Anker-Sichtprüfung beim Einfahren
  □ Snubber-Sichtprüfung
  □ Windlass-Laufgeräusch beurteilen

WÖCHENTLICH (bei aktivem Cruising):
  □ Kette + Anker mit Süßwasser spülen
  □ Kettenkasten-Drainage prüfen
  □ Windlass-Gehäuse reinigen

MONATLICH:
  □ Schäkelverbindungen prüfen
  □ Wirbel/Swivel: Drehbarkeit, Spiel
  □ Windlass: Getriebeöl Sichtprüfung
  □ Bugrolle: Leichtgängigkeit
  □ Elektrische Verbindungen

PRE-SEASON (1× jährlich):
  □ Kette komplett auslegen + messen
  □ Anker: Schweißnähte, Galvanisierung, Schaft
  □ Windlass: Öl wechseln, Bürsten prüfen, Dichtung
  □ Alle Schäkel + Wirbel inspizieren
  □ Snubber, Bugrolle, Kettenkasten

WINTERIZATION:
  □ Alles reinigen, trocknen
  □ Windlass konservieren (Öl, Kontakte, Abdeckung)
  □ Kette inspizieren + ggf. Zinkspray
  □ Trocken lagern
```

### 14.2 Ablegereife-Grenzwerte

```
KETTE — SOFORT ERSETZEN WENN:
  • Glieddicke < 85 % Nenndicke
  • Elongation > 105 % (10-Glieder-Maß)
  • Sichtbarer Lochfraß (tiefe Narben)
  • Gebrochenes Glied
  • Steife, nicht bewegliche Glieder (> 5 Stellen)

KETTE — INNERHALB 12 MONATEN ERSETZEN:
  • Glieddicke 85–90 % + weiterer Befund
  • Elongation 103–105 %
  • Galvanisierung < 30 % + Dickenverlust

WINDLASS — SOFORT HANDELN:
  • Kohlebürsten < 5 mm
  • Getriebeöl milchig (Wasser!)
  • Motor dreht nicht (Sicherung + Solenoid ok)
  • Decksleckage an Windlass-Basis

WIRBEL — SOFORT ERSETZEN:
  • Seitliches Spiel > 1 mm
  • Sichtbarer Lochfraß
  • Dreht nicht mehr
```

### 14.3 Kosten-Übersicht

```
TYPISCHE KOSTEN (2026, Stand April):
=====================================

Kette (verzinkt, DIN 766):
  8 mm × 50 m ........... 300–450 EUR
  10 mm × 60 m .......... 500–750 EUR
  10 mm × 80 m .......... 800–1.200 EUR

Neuverzinkung:
  Kette 8mm × 50m ....... 180–280 EUR
  Kette 10mm × 60m ...... 320–500 EUR
  Anker 15 kg ........... 60–100 EUR

Windlass-Service-Kit:
  Lofrans ............... 58–98 EUR
  Lewmar ................ 48–85 EUR
  Quick ................. 45–82 EUR
  Maxwell ............... 55–110 EUR

Ersatzteile (Einzeln):
  Kohlebürsten (Paar) ... 22–50 EUR
  Solenoid 12V .......... 75–120 EUR
  Kettennuss 10mm ....... 85–155 EUR
  Wellendichtung ........ 12–32 EUR
  Wirbel/Swivel ......... 35–125 EUR
  Schäkel 10mm (Edst.) .. 12–20 EUR

Pflegemittel:
  Tef-Gel 30g ........... 12–18 EUR
  Lanocote 120g ......... 18–25 EUR
  CRC Zinc-It 400ml ..... 12–15 EUR
  Getriebeöl 250ml ...... 8–12 EUR

Werkzeug-Basis-Set:
  Komplett .............. 160–300 EUR
```

### 14.4 Notfall-Maßnahmen auf einen Blick

```
KETTENVERLUST:
  1. Position notieren (GPS!)
  2. Motor starten, Position halten
  3. Markierung ausbringen (Fender-Boje)
  4. Bergedienst / Taucher kontaktieren

WINDLASS FÄLLT AUS:
  1. Handkurbel verwenden (falls vorhanden)
  2. Kette von Hand hieven (Handschuhe!)
  3. Boot über Anker fahren, Kette an Klampe

ANKER SITZT FEST:
  1. NICHT mit Windlass losreißen!
  2. Kette auf Klampe belegen
  3. Boot in verschiedene Richtungen über Anker fahren
  4. Trip-Leine verwenden (falls vorhanden)
  5. Kette verkürzen, Motorstoß

KETTE KLEMMT IM KASTEN:
  1. Windlass stoppen!
  2. Kettenstopper einlegen
  3. Luke öffnen, Kette entwirren
  4. Langsam weiter hieven
```

---

## 15. ANHANG A–H: Fallstudien

### ANHANG A: Fallstudie 1 — Kettenverlust Bavaria 42 (Korfu, 2024)

#### A.1 Ausgangssituation
- **Boot**: Bavaria 42 Cruiser (2016), Charteryacht
- **Ankersystem**: Lewmar V2, Kette 10 mm DIN 766 × 60 m, Delta-Anker 16 kg
- **Revier**: Ionische Inseln, Griechenland
- **Vorfall**: Beim Ankern in Paleokastritsa (Korfu) rauschte die gesamte Kette
  unkontrolliert aus dem Kettenkasten. Anker und 60 m Kette verloren.

#### A.2 Ursache
Die Kettenend-Befestigung im Kasten (Dyneema-Leine) war bei der letzten
Wartung nicht geprüft worden. Die Leine war durch Scheuern an einer
scharfen Kante im Kettenkasten zu 80 % durchgescheuert. Beim Ankern in
15 m Tiefe (45 m Kette ausgesteckt) löste der letzte Ruck die Leine.

#### A.3 Analyse
- Wartungsprotokoll: Keine Dokumentation über Kettenend-Befestigung
- Kettenkasten: Scharfe GFK-Kante am Fallrohr (Fertigungsfehler, nie entgratet)
- Windlass-Kupplung: War korrekt, hätte die Kette halten können, wenn
  der Skipper die Kupplung früher eingerastet hätte (Bedienfehler)

#### A.4 Kosten
- Ankerbergung (Taucher): 380 EUR
- Neue Kette (10 mm × 60 m, DIN 766): 620 EUR
- Neue Dyneema-Kettenend-Leine: 25 EUR
- Kettenkasten-Kante entgraten: 0 EUR (Eigenleistung)
- **Gesamt: ca. 1.025 EUR**

#### A.5 Lehren
1. Kettenend-Befestigung bei JEDER Pre-Season-Inspektion prüfen
2. Kettenkasten auf scharfe Kanten inspizieren
3. Dyneema-Endleine alle 3 Jahre ersetzen (Verschleißteil!)
4. Kupplung IMMER einrasten, sobald gewünschte Kettenlänge erreicht

---

### ANHANG B: Fallstudie 2 — Windlass-Ausfall bei Starkwind (Ostsee, 2023)

#### B.1 Ausgangssituation
- **Boot**: Hallberg-Rassy 37 (2008), Eigner-Yacht
- **Ankersystem**: Lofrans Tigres 1500 W, Kette 10 mm × 70 m, Rocna 15 kg
- **Revier**: Dänische Südsee, Marstal
- **Vorfall**: Nach Sturmankern (7 Bft, 18 Stunden) konnte die Windlass
  den Anker nicht mehr hieven. Motor drehte kurz, dann Sicherung.

#### B.2 Ursache
Während des Sturmankerns war Salzwasser über die undichte Wellendichtung
in den Motorraum eingedrungen. Das Getriebeöl war milchig (Wasser im Öl),
die Kabelverbindungen am Solenoid korrodiert. Zusätzlich waren die
Kohlebürsten auf 3 mm verschlissen (letzter Wechsel: nie, Boot 15 Jahre alt).

#### B.3 Analyse
- Wellendichtung: Simmerring ausgehärtet, rissig (Alter 15 Jahre)
- Getriebeöl: Nie gewechselt (!) — milchig-grau, viskositätsverlust
- Kohlebürsten: 3 mm (Neuzustand 20 mm) — über 95 % verschlissen
- Kabelverbindungen: Grünspan an Solenoid-Klemmen
- Wartungshistorie: KEINE Dokumentation vorhanden

#### B.4 Reparatur
1. Anker von Hand gehievt (Handkurbel + Bootshaken, 45 Minuten)
2. In Marstal: Motor getrocknet, Öl gewechselt, Bürsten getauscht
3. Neue Wellendichtung eingebaut
4. Solenoid-Klemmen gereinigt
5. Gesamtkosten: 145 EUR (Eigenleistung)

#### B.5 Lehren
1. Wellendichtung alle 5–8 Jahre präventiv ersetzen
2. Getriebeöl MINDESTENS jährlich wechseln
3. Kohlebürsten bei Pre-Season prüfen, alle 500–1.000 h tauschen
4. Wartungslogbuch führen!

---

### ANHANG C: Fallstudie 3 — Galvanische Korrosion an Wirbel (Mittelmeer, 2025)

#### C.1 Ausgangssituation
- **Boot**: Jeanneau Sun Odyssey 440 (2020), Eigner
- **Ankersystem**: Quick Dylan 1000 W, Kette 10 mm verzinkt × 60 m,
  Ultra-Anker 16 kg (Edelstahl 316L), Kong Anchor Swivel (Edelstahl 316)
- **Revier**: Sardinien, ganzjährig im Wasser
- **Vorfall**: Nach 4 Saisons war die Verzinkung der ersten 3 Meter
  Kette fast vollständig abgebaut. Kette an der Wirbel-Verbindung nur
  noch 7,8 mm (Nenn 10 mm = 78 %).

#### C.2 Ursache
Der Edelstahl-Wirbel (316, ~-100 mV) in direktem Kontakt mit der
verzinkten Kette (-1.000 mV) erzeugte eine galvanische Spannungsdifferenz
von ~900 mV. Die Zinkschicht und anschließend der Stahl selbst wurden
beschleunigt abgebaut. Kein Tef-Gel oder andere Isolation verwendet.

#### C.3 Kosten
- Neue Kette (10 mm × 60 m, DIN 766, verzinkt): 620 EUR
- Tef-Gel (30 g Tube): 15 EUR
- **Gesamt: 635 EUR** (vermeidbar gewesen)

#### C.4 Lehren
1. Bei JEDER Kombination von Edelstahl und verzinktem Stahl: Tef-Gel!
2. Erste Meter der Kette (Kontaktzone Wirbel) besonders häufig prüfen
3. Alternative: Edelstahlkette im Bereich Wirbel–Anker (erste 5 m)
4. Jährliche Inspektion der Kontaktstelle obligatorisch

---

### ANHANG D: Fallstudie 4 — Anker gräbt sich nicht ein (Kroatien, 2024)

#### D.1 Ausgangssituation
- **Boot**: Beneteau Oceanis 46.1 (2022), Charteryacht
- **Ankersystem**: Lewmar V3, Kette 10 mm × 80 m, CQR 20 kg
- **Revier**: Kornaten, Kroatien
- **Vorfall**: Anker greift nicht in 3 aufeinanderfolgenden Buchten.
  Boot treibt bei 3 Bft. GPS-Alarm wiederholt.

#### D.2 Ursache
Der CQR-Anker hatte einen verbogenen Schaft (5 mm/m Abweichung) — durch
ein früheres Festsitz-Ereignis, bei dem der Charterskipper die Windlass
zum Losreißen verwendet hatte. Die Verbiegung verhinderte das korrekte
Eingraben, da der Anker sich beim Zug drehte statt einzugraben.

#### D.3 Kosten
- Neuer CQR 20 kg (verzinkt): 280 EUR
- Alternativ: Neuer Bügelanker (Rocna 15 kg): 380 EUR → gewählt
- **Gesamt: 380 EUR**

#### D.4 Lehren
1. NIEMALS Windlass zum Losreißen verwenden!
2. Schaft-Geradheit bei jeder Pre-Season prüfen (2 mm/m max.)
3. Bügelanker sind weniger anfällig für Verbiegung als CQR
4. Charteryachten: Anker-Zustand vor jeder Charter prüfen

---

### ANHANG E: Fallstudie 5 — Snubber-Versagen in Böen (Karibik, 2024)

#### E.1 Ausgangssituation
- **Boot**: Lagoon 42 (2019), Eigner-Langfahrt
- **Ankersystem**: Quick Hector 1500 W, Kette 10 mm × 80 m, Mantus 35 kg
- **Revier**: Martinique, Anse d'Arlet
- **Vorfall**: Snubber riss bei Böe (35 kt). Gesamte Last ging auf
  Windlass. Windlass-Befestigung (4 Bolzen) riss 2 Bolzen aus dem Deck.
  Boot trieb kurzzeitig, bevor Kettenstopper hielt.

#### E.2 Ursache
Snubber (16 mm Nylon, 5 Jahre alt) war durch UV-Schädigung brüchig.
Bruchstelle an Schamfilstelle (Klüse, kein Schamfilschutz). Windlass-
Befestigung: Alu-Sandwich-Deck ohne korrekte Kernverstärkung. Nur 2 von
4 Bolzen mit Backing Plate.

#### E.3 Kosten
- Neuer Snubber (20 mm × 8 m, Nylon, 3-strändig): 85 EUR
- Schamfilschutz (Meterware): 12 EUR
- Deck-Reparatur (2 Bolzen, Kernersatz, 4× Backing Plate): 1.200 EUR (Werft)
- **Gesamt: 1.297 EUR**

#### E.4 Lehren
1. Snubber alle 3–5 Jahre ersetzen (UV-Degradation!)
2. Schamfilschutz an der Klüse IMMER montieren
3. Snubber-Durchmesser für Katamaran großzügig dimensionieren (20 mm+)
4. Windlass-Befestigung: IMMER Backing Plate unter ALLEN Bolzen
5. Sandwich-Kern im Befestigungsbereich durch Epoxy/GFK ersetzen

---

### ANHANG F: Fallstudie 6 — Kettennuss-Verschleiß (Nordsee, 2025)

#### F.1 Ausgangssituation
- **Boot**: Hallberg-Rassy 48 (2012), Eigner
- **Ankersystem**: Lofrans X3 1000 W, Kette 10 mm DIN 766 × 80 m, Rocna 25 kg
- **Nutzung**: ~200 Ankermanöver/Jahr (intensiver Cruiser)
- **Vorfall**: Kette springt regelmäßig aus der Kettennuss beim Hieven.

#### F.2 Ursache
Die Kettennuss (Aluminium, Originalausstattung 2012) zeigte nach 13 Jahren
und ca. 2.500 Ankermanövern erheblichen Profilverschleiß. Die Zahnspitzen
waren um ca. 2 mm abgetragen. Die Kette selbst war in Ordnung (Dicke
9,4 mm = 94 %).

#### F.3 Kosten
- Neue Kettennuss Lofrans 10 mm DIN 766 (Edelstahl-Upgrade): 155 EUR
- Einbau (Eigenleistung): 0 EUR
- **Gesamt: 155 EUR**

#### F.4 Lehren
1. Kettennuss alle 5 Jahre inspizieren (Zahnprofil)
2. Edelstahl-Kettennuss hält 2–3× länger als Aluminium
3. Bei intensiver Nutzung (>100 Ankermanöver/Jahr): Alle 3 Jahre prüfen
4. Kettennuss-Wechsel ist Eigenleistung (30 Minuten)

---

### ANHANG G: Fallstudie 7 — Kettenkasten-Gestank (Ostsee, 2025)

#### G.1 Ausgangssituation
- **Boot**: Bavaria 34 (2018), Eigner
- **Problem**: Unerträglicher Schwefel-/Fäulnisgeruch aus dem Kettenkasten,
  besonders bei warmem Wetter. Geruch zieht in die Vorschiffskabine.

#### G.2 Ursache
1. Kette wurde nie mit Süßwasser gespült nach dem Ankern
2. Schlick und organisches Material sammelten sich im Kasten
3. Drainage verstopft (Schlauch geknickt)
4. Belüftung nicht vorhanden (Werft hatte keine Lüftung vorgesehen)
5. Anaerobe Zersetzung → Schwefelwasserstoff

#### G.3 Lösung
1. Kette komplett entnommen und mit Hochdruckreiniger gereinigt
2. Kettenkasten: 3× gereinigt (Essigessenz, dann Backpulver, dann klar)
3. Drainage: Knick beseitigt, Siphon gereinigt
4. Belüftung: 2× Lüftungsgitter (Plastimo, Ø 75 mm) eingebaut
5. Kette: Ab sofort nach jedem Ankern mit Deckwaschanlage spülen

#### G.4 Kosten
- Essigessenz, Backpulver: 5 EUR
- 2× Lüftungsgitter Plastimo: 28 EUR
- Eigenleistung: 4 Stunden
- **Gesamt: 33 EUR**

#### G.5 Lehren
1. Kette nach JEDEM Ankern mit Süßwasser spülen
2. Kettenkasten MUSS belüftet sein
3. Drainage regelmäßig prüfen (nicht verstopft, nicht geknickt)
4. Winterization: Kettenkasten reinigen und desinfizieren

---

### ANHANG H: Fallstudie 8 — Solenoid-Ausfall (Langfahrt, 2024)

#### H.1 Ausgangssituation
- **Boot**: Amel 54 (2015), Langfahrt-Eigner
- **Ankersystem**: Maxwell HRC-FF 1500 W, Kette 12 mm × 100 m, Spade 30 kg
- **Revier**: Kapverden → Karibik → Bahamas (3 Jahre Langfahrt)
- **Vorfall**: Windlass reagiert nicht. Solenoid klickt nicht.

#### H.2 Diagnose
1. Batterie: 12,8 V — ok
2. Sicherung: intakt
3. Fußschalter: Durchgang vorhanden — ok
4. Steuerkabel: Durchgang vorhanden — ok
5. Solenoid: Keine Reaktion. Spulenwiderstand: ∞ (Unterbrechung)
6. Solenoid-Spule durchgebrannt (Korrosion an der Wicklung)

#### H.3 Reparatur (auf See)
1. Kein Ersatz-Solenoid an Bord!
2. Notlösung: Solenoid überbrückt mit schwerem Schalter (50 A)
   direkt im Motorraum. Sicherheit: NUR mit zweiter Person bedienen.
3. Im nächsten Hafen (Nassau): Solenoid bestellt (Maxwell P100200).
   Lieferzeit: 3 Wochen ab Florida.
4. Einbau: 30 Minuten.

#### H.4 Kosten
- Solenoid Maxwell P100200 (12V): 115 EUR
- Versand (Express Florida → Nassau): 85 EUR
- Notschalter (temporär): 15 EUR
- **Gesamt: 215 EUR**

#### H.5 Lehren
1. Ersatz-Solenoid gehört auf JEDE Langfahrt-Yacht!
2. Kosten: 75–120 EUR, Gewicht: 300–500 g
3. Einbau in 30 Minuten ohne Spezialwerkzeug
4. Solenoid ist DAS Bauteil, das unterwegs am häufigsten ausfällt
5. Notfall-Bypass mit schwerem Schalter möglich, aber NUR als Notlösung

---

## 16. ANHANG I–R: Pydantic v2 Datenmodelle

### 16.1 Hinweise zur Implementierung

Alle Datenmodelle verwenden **Pydantic v2** mit `model_config = {"from_attributes": True}`.
KEINE `class Config`-Syntax. Alle Felder typisiert, Confidence-Level
durchgängig integriert.

### 16.2 Datenmodelle

```python
from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Enums ---

class ConfidenceLevel(str, Enum):
    measured = "measured"
    calculated = "calculated"
    visual_high = "visual_high"
    visual_medium = "visual_medium"
    visual_low = "visual_low"
    visual_insufficient = "visual_insufficient"
    estimated = "estimated"
    benchmark = "benchmark"
    documented = "documented"


class WartungsPhase(str, Enum):
    pre_season = "pre_season"
    in_season = "in_season"
    winterization = "winterization"
    off_season = "off_season"
    nach_extrembelastung = "nach_extrembelastung"


class KomponentenTyp(str, Enum):
    anker = "anker"
    kette = "kette"
    windlass = "windlass"
    wirbel = "wirbel"
    bugrolle = "bugrolle"
    snubber = "snubber"
    kettenkasten = "kettenkasten"
    schaekel = "schaekel"
    kettenstopper = "kettenstopper"


class GalvanisierungsStufe(str, Enum):
    g1_neuwertig = "g1_neuwertig"
    g2_patiniert = "g2_patiniert"
    g3_teilweise_abgenutzt = "g3_teilweise_abgenutzt"
    g4_stark_abgenutzt = "g4_stark_abgenutzt"
    g5_schutzlos = "g5_schutzlos"


class BewertungStufe(str, Enum):
    neuwertig = "neuwertig"
    gut = "gut"
    ausreichend = "ausreichend"
    grenzwertig = "grenzwertig"
    ablegereif = "ablegereif"


class FehlerbildSeverity(str, Enum):
    kritisch = "kritisch"
    hoch = "hoch"
    mittel = "mittel"
    niedrig = "niedrig"
    info = "info"


class KorrosionsschutzMittel(str, Enum):
    tef_gel = "tef_gel"
    duralac = "duralac"
    lanocote = "lanocote"
    zinkspray = "zinkspray"
    kontaktspray = "kontaktspray"
    polfett = "polfett"


# --- Grundlegende Modelle ---

class KettenMessung(BaseModel):
    model_config = {"from_attributes": True}

    position_meter: float = Field(..., description="Position auf der Kette in Metern")
    glied_nummer: int = Field(..., description="Glied-Nummer an dieser Position")
    dicke_1_mm: float = Field(..., description="Erste Dickenmessung in mm")
    dicke_2_mm: float = Field(..., description="Zweite Dickenmessung in mm")
    dicke_3_mm: float = Field(..., description="Dritte Dickenmessung in mm")
    min_dicke_mm: float = Field(..., description="Minimale gemessene Dicke in mm")
    nenn_dicke_mm: float = Field(..., description="Nenndicke der Kette in mm")
    prozent_nenn: float = Field(..., description="Minimale Dicke in % der Nenndicke")
    bewertung: BewertungStufe = Field(..., description="Bewertung des Glieds")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class KettenElongation(BaseModel):
    model_config = {"from_attributes": True}

    position_meter: float = Field(..., description="Startposition der Messung")
    anzahl_glieder: int = Field(default=10, description="Anzahl gemessener Glieder")
    soll_laenge_mm: float = Field(..., description="Soll-Länge in mm")
    ist_laenge_mm: float = Field(..., description="Gemessene Länge in mm")
    elongation_prozent: float = Field(..., description="Elongation in %")
    bewertung: BewertungStufe = Field(..., description="Bewertung der Elongation")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class KettenInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(..., description="Datum der Inspektion")
    ketten_norm: str = Field(..., description="Kettennorm (z.B. DIN 766)")
    nenn_dicke_mm: float = Field(..., description="Nenndicke der Kette in mm")
    laenge_m: float = Field(..., description="Gesamtlänge der Kette in Metern")
    baujahr_kette: Optional[int] = Field(None, description="Herstellungsjahr der Kette")
    material: str = Field(..., description="Material (verzinkter Stahl, Edelstahl 316L)")
    messungen: list[KettenMessung] = Field(default_factory=list)
    elongationen: list[KettenElongation] = Field(default_factory=list)
    galvanisierung_stufe: Optional[GalvanisierungsStufe] = Field(None)
    verdrehte_glieder_anzahl: int = Field(default=0)
    steife_glieder_anzahl: int = Field(default=0)
    lochfrass_stellen: int = Field(default=0)
    markierungen_vollstaendig: bool = Field(default=True)
    kettennuss_kompatibel: bool = Field(default=True)
    gesamtbewertung: BewertungStufe = Field(...)
    empfehlung: str = Field(..., description="Handlungsempfehlung")
    naechste_pruefung: Optional[date] = Field(None)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)
    pruefer: Optional[str] = Field(None, description="Name des Prüfers")


class AnkerInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    anker_typ: str = Field(..., description="Ankertyp (z.B. Bügelanker, CQR, Danforth)")
    anker_modell: Optional[str] = Field(None, description="Modellbezeichnung")
    gewicht_kg: float = Field(..., description="Nenngewicht des Ankers in kg")
    material: str = Field(...)
    schweissnaehte_ok: bool = Field(...)
    schweissnaht_befunde: list[str] = Field(default_factory=list)
    galvanisierung_stufe: Optional[GalvanisierungsStufe] = Field(None)
    schaft_abweichung_mm_pro_m: float = Field(default=0.0)
    schaft_bewertung: BewertungStufe = Field(...)
    bewegliche_teile_ok: bool = Field(default=True)
    bewegliche_teile_befunde: list[str] = Field(default_factory=list)
    schaekeloes_verschleiss_prozent: float = Field(default=0.0)
    flunke_zustand: str = Field(default="gut")
    gesamtbewertung: BewertungStufe = Field(...)
    empfehlung: str = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class WindlassInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    hersteller: str = Field(..., description="Hersteller der Windlass")
    modell: str = Field(..., description="Modellbezeichnung")
    leistung_w: Optional[int] = Field(None, description="Motorleistung in Watt")
    spannung_v: int = Field(default=12, description="Systemspannung (12 oder 24 V)")
    kohlebuersten_laenge_mm: Optional[float] = Field(None)
    kohlebuersten_bewertung: Optional[BewertungStufe] = Field(None)
    getriebeoel_zustand: str = Field(default="ok", description="klar/milchig/schwarz/metallisch")
    getriebeoel_letzter_wechsel: Optional[date] = Field(None)
    wellendichtung_ok: bool = Field(default=True)
    kupplung_ok: bool = Field(default=True)
    kupplung_befund: Optional[str] = Field(None)
    solenoid_ok: bool = Field(default=True)
    fussschalter_ok: bool = Field(default=True)
    elektrische_verbindungen_ok: bool = Field(default=True)
    spannungsabfall_v: Optional[float] = Field(None, description="Gesamtspannungsabfall unter Last")
    kettennuss_verschleiss: Optional[str] = Field(None)
    probelauf_ok: bool = Field(default=True)
    probelauf_befund: Optional[str] = Field(None)
    gesamtbewertung: BewertungStufe = Field(...)
    empfehlung: str = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class WirbelInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    typ: str = Field(..., description="Wirbeltyp und Hersteller")
    material: str = Field(default="Edelstahl 316")
    bruchlast_kn: Optional[float] = Field(None)
    drehbarkeit_ok: bool = Field(default=True)
    spiel_mm: float = Field(default=0.0)
    korrosion_befund: Optional[str] = Field(None)
    schaekel_ok: bool = Field(default=True)
    gesamtbewertung: BewertungStufe = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class BugrolleInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    material: str = Field(default="Edelstahl 316")
    rolle_leichtgaengig: bool = Field(default=True)
    lager_spiel_mm: float = Field(default=0.0)
    befestigung_ok: bool = Field(default=True)
    ankersicherung_ok: bool = Field(default=True)
    kettenfuehrung_ok: bool = Field(default=True)
    gesamtbewertung: BewertungStufe = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class SnubberInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    material: str = Field(default="Nylon 3-stränzig")
    durchmesser_mm: float = Field(...)
    laenge_m: float = Field(...)
    alter_jahre: Optional[float] = Field(None)
    leine_zustand: BewertungStufe = Field(...)
    hook_ok: bool = Field(default=True)
    schamfilschutz_vorhanden: bool = Field(default=True)
    elastizitaet_ok: bool = Field(default=True)
    gesamtbewertung: BewertungStufe = Field(...)
    empfehlung: str = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


class KettenkastenInspektion(BaseModel):
    model_config = {"from_attributes": True}

    datum: date = Field(...)
    sauberkeit_ok: bool = Field(default=True)
    drainage_ok: bool = Field(default=True)
    belueftung_ok: bool = Field(default=True)
    kettenfuehrung_ok: bool = Field(default=True)
    endpunkt_befestigung_ok: bool = Field(default=True)
    laminat_ok: bool = Field(default=True)
    geruch: Optional[str] = Field(None, description="Geruchsbeschreibung (oder None)")
    gesamtbewertung: BewertungStufe = Field(...)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


# --- Galvanisierung ---

class GalvanisierungsBewertung(BaseModel):
    model_config = {"from_attributes": True}

    komponente: KomponentenTyp = Field(...)
    stufe: GalvanisierungsStufe = Field(...)
    geschaetzte_restlebensdauer_jahre: Optional[float] = Field(None)
    empfehlung: str = Field(...)
    neuverzinkung_kosten_eur: Optional[float] = Field(None)
    zinkspray_als_zwischenloesung: bool = Field(default=False)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.visual_medium)


# --- Korrosionsschutz ---

class KorrosionsBefund(BaseModel):
    model_config = {"from_attributes": True}

    komponente: KomponentenTyp = Field(...)
    stelle: str = Field(..., description="Genaue Stelle der Korrosion")
    korrosionstyp: str = Field(..., description="Typ (galvanisch, Lochfraß, Spalt, Fläche)")
    materialpaarung: Optional[str] = Field(None, description="z.B. Edelstahl 316 ↔ verz. Stahl")
    spannungsdifferenz_mv: Optional[int] = Field(None)
    severity: FehlerbildSeverity = Field(...)
    empfehlung: str = Field(...)
    korrosionsschutz_mittel: Optional[KorrosionsschutzMittel] = Field(None)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.measured)


# --- Wartungsplan ---

class WartungsAufgabe(BaseModel):
    model_config = {"from_attributes": True}

    id: str = Field(..., description="Eindeutige Aufgaben-ID (z.B. K-01, W-03)")
    komponente: KomponentenTyp = Field(...)
    phase: WartungsPhase = Field(...)
    beschreibung: str = Field(...)
    methode: str = Field(...)
    akzeptabel: str = Field(..., description="Akzeptanzkriterium")
    massnahme_bei_mangel: str = Field(...)
    aufwand_minuten: Optional[int] = Field(None)
    materialkosten_eur: Optional[float] = Field(None)


class WartungsPlan(BaseModel):
    model_config = {"from_attributes": True}

    boot_name: Optional[str] = Field(None)
    boots_laenge_m: Optional[float] = Field(None)
    phase: WartungsPhase = Field(...)
    aufgaben: list[WartungsAufgabe] = Field(default_factory=list)
    geschaetzter_zeitaufwand_stunden: Optional[float] = Field(None)
    geschaetzte_materialkosten_eur: Optional[float] = Field(None)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.estimated)


# --- Fehlerbild ---

class FehlerbildUrsache(BaseModel):
    model_config = {"from_attributes": True}

    ursache: str = Field(...)
    wahrscheinlichkeit: str = Field(..., description="Hoch/Mittel/Niedrig")
    diagnose: str = Field(...)


class Fehlerbild(BaseModel):
    model_config = {"from_attributes": True}

    id: str = Field(..., description="Fehlerbild-ID (z.B. F-17_08-01)")
    titel: str = Field(...)
    symptome: list[str] = Field(default_factory=list)
    ursachen: list[FehlerbildUrsache] = Field(default_factory=list)
    sofortmassnahmen: list[str] = Field(default_factory=list)
    praevention: list[str] = Field(default_factory=list)
    severity: FehlerbildSeverity = Field(...)


# --- Ersatzteile ---

class Ersatzteil(BaseModel):
    model_config = {"from_attributes": True}

    hersteller: str = Field(...)
    modellreihe: str = Field(...)
    teil_bezeichnung: str = Field(...)
    teilenummer: Optional[str] = Field(None)
    preis_eur_min: float = Field(...)
    preis_eur_max: float = Field(...)
    bezugsquelle: list[str] = Field(default_factory=list)
    kategorie: str = Field(..., description="z.B. Service-Kit, Kohlebürsten, Solenoid")


class ErsatzteilDatenbank(BaseModel):
    model_config = {"from_attributes": True}

    hersteller: str = Field(...)
    teile: list[Ersatzteil] = Field(default_factory=list)
    letzte_aktualisierung: date = Field(...)


# --- Visuell ---

class VisuelleAnkersystemBewertung(BaseModel):
    model_config = {"from_attributes": True}

    ketten_galvanisierung: Optional[GalvanisierungsStufe] = Field(None)
    ketten_rost_anteil_prozent: Optional[float] = Field(None)
    ketten_verdrehte_glieder: Optional[bool] = Field(None)
    anker_galvanisierung: Optional[GalvanisierungsStufe] = Field(None)
    anker_schaft_gerade: Optional[bool] = Field(None)
    anker_schweissnaehte_sichtbar: Optional[bool] = Field(None)
    windlass_korrosion: Optional[str] = Field(None)
    bugrolle_zustand: Optional[str] = Field(None)
    snubber_zustand: Optional[str] = Field(None)
    kettenkasten_sauberkeit: Optional[str] = Field(None)
    allgemein_pflegezustand: Optional[str] = Field(None)
    erkannte_fehlerbilder: list[str] = Field(default_factory=list)
    empfehlungen: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.visual_medium)


# --- Gesamtergebnis ---

class AnkersystemWartungsBewertung(BaseModel):
    model_config = {"from_attributes": True}

    boot_name: Optional[str] = Field(None)
    boots_laenge_m: Optional[float] = Field(None)
    boots_klasse: Optional[str] = Field(None)
    datum: date = Field(...)

    ketten_inspektion: Optional[KettenInspektion] = Field(None)
    anker_inspektion: Optional[AnkerInspektion] = Field(None)
    windlass_inspektion: Optional[WindlassInspektion] = Field(None)
    wirbel_inspektion: Optional[WirbelInspektion] = Field(None)
    bugrolle_inspektion: Optional[BugrolleInspektion] = Field(None)
    snubber_inspektion: Optional[SnubberInspektion] = Field(None)
    kettenkasten_inspektion: Optional[KettenkastenInspektion] = Field(None)

    galvanisierungs_bewertungen: list[GalvanisierungsBewertung] = Field(default_factory=list)
    korrosions_befunde: list[KorrosionsBefund] = Field(default_factory=list)
    fehlerbilder: list[Fehlerbild] = Field(default_factory=list)

    wartungsplan: Optional[WartungsPlan] = Field(None)
    visuelle_bewertung: Optional[VisuelleAnkersystemBewertung] = Field(None)

    gesamtscore: Optional[float] = Field(None, ge=0, le=100)
    gesamtbewertung: Optional[BewertungStufe] = Field(None)
    dringende_massnahmen: list[str] = Field(default_factory=list)
    geplante_massnahmen: list[str] = Field(default_factory=list)
    geschaetzte_kosten_eur: Optional[float] = Field(None)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.estimated)


class AnkersystemWartungsAnalyseResult(BaseModel):
    model_config = {"from_attributes": True}

    available: bool = Field(default=True)
    reason: Optional[str] = Field(None, description="Grund falls nicht verfügbar")
    bewertung: Optional[AnkersystemWartungsBewertung] = Field(None)
    analyse_version: str = Field(default="2.0")
    module: str = Field(default="ankersystem_wartung")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.estimated)
```

### 16.3 Verwendungshinweise

Die Datenmodelle werden von der AYDI-Analyse-Engine wie folgt verwendet:

1. **Strukturierte Eingabe (Pipeline A):** `KettenInspektion`, `AnkerInspektion`,
   `WindlassInspektion` etc. werden aus Messdaten, CAD-Modellen oder
   Servicerapporten befüllt. Confidence: `measured` oder `documented`.

2. **Visuelle Eingabe (Pipeline B):** `VisuelleAnkersystemBewertung` wird
   aus der Claude Vision API befüllt. Confidence: `visual_high` bis
   `visual_insufficient`.

3. **Text-Eingabe (Pipeline C):** Serviceberichte werden geparst und in
   die entsprechenden Inspektionsmodelle überführt. Confidence: `documented`.

4. **Fusion:** `AnkersystemWartungsBewertung` kombiniert alle Eingaben
   und berechnet den `gesamtscore` (0–100) unter Berücksichtigung der
   jeweiligen Confidence-Level.

5. **Module-Skip:** Wenn keine ausreichenden Daten vorliegen, gibt das
   Modul `AnkersystemWartungsAnalyseResult(available=False, reason="...")`
   zurück.

### 16.4 Score-Berechnung — Wartungszustand

Die Bewertung des Wartungszustands erfolgt als gewichteter Score (0–100):

```python
WARTUNGS_GEWICHTE = {
    "kette": 0.25,          # Kette = sicherheitskritischste Komponente
    "anker": 0.15,          # Anker = hohe Relevanz
    "windlass": 0.20,       # Windlass = Funktionsfähigkeit
    "wirbel": 0.10,         # Wirbel = Verbindungselement
    "bugrolle": 0.05,       # Bugrolle = mechanisch
    "snubber": 0.10,        # Snubber = Schutzfunktion
    "kettenkasten": 0.05,   # Kettenkasten = Lagerung
    "schaekel": 0.10,       # Schäkel = sicherheitskritisch
}

BEWERTUNG_SCORES = {
    "neuwertig": 100,
    "gut": 85,
    "ausreichend": 65,
    "grenzwertig": 35,
    "ablegereif": 10,
}
```

### 16.5 Visuelle Analyse — Prompt-Hinweise

Die visuelle Analyse des Ankersystems durch Claude Vision verwendet
folgende Erkennungsmerkmale:

| Visuelle Eigenschaft | Erkennung | Zuordnung |
|---------------------|-----------|-----------|
| Orangebraune Flecken auf Kette | Farbanalyse (RGB: R>180, G<120, B<80) | Galv.-Stufe G3–G5 |
| Gleichmäßig silbrige Kette | Farbanalyse (R≈G≈B, >150) | Galv.-Stufe G1–G2 |
| Weißer Belag auf Aluminium | Helle Flecken auf dunklem Alu | Alu-Oxidation |
| Verbogener Ankerschaft | Linienerkennung, Winkelabweichung | Schaft-Abweichung |
| Aufgeriebene Snubber-Fasern | Texturerkennung, abstehende Fasern | Snubber-Verschleiß |
| Grünspan an Klemmen | Farbanalyse (grün/blaugrün) | Korrosion elektrisch |
| Tiefe Rillen in Bugrolle | Schattenanalyse, Vertiefungen | Rollenverschleiß |
| Kettenverdrehung | Glied-Orientierungsanalyse | Verdrehte Glieder |

---

## 17. Ergänzende Referenztabellen

### 17.1 Drehmoment-Tabelle für Windlass-Befestigung

| Schraubengröße | Material Deck | Drehmoment (Nm) | Anzugsreihenfolge |
|:--------------:|:------------:|:---------------:|:-----------------:|
| M8 (Edelstahl) | GFK massiv | 15–18 Nm | Kreuzweise |
| M8 (Edelstahl) | GFK Sandwich | 12–15 Nm | Kreuzweise |
| M10 (Edelstahl) | GFK massiv | 25–30 Nm | Kreuzweise |
| M10 (Edelstahl) | GFK Sandwich | 20–25 Nm | Kreuzweise |
| M12 (Edelstahl) | GFK massiv | 40–50 Nm | Kreuzweise |
| M12 (Edelstahl) | GFK Sandwich | 35–45 Nm | Kreuzweise |
| 5/16" UNC (Edelstahl) | GFK massiv | 12–15 Nm | Kreuzweise |
| 3/8" UNC (Edelstahl) | GFK massiv | 22–28 Nm | Kreuzweise |

**Wichtig:** Immer Tef-Gel oder Anti-Seize auf Gewinde vor dem Eindrehen.
NIEMALS Edelstahl-Schrauben trocken in Aluminium oder GFK eindrehen
(Festfressen!).

### 17.2 Kabelquerschnitte für Windlass-Installation

| Motorleistung | Systemspannung | Max. Strom | Kabellänge ≤5 m | Kabellänge 5–8 m | Kabellänge 8–12 m |
|:-------------:|:--------------:|:----------:|:---------------:|:----------------:|:-----------------:|
| 300 W | 12 V | 40 A | 10 mm² | 16 mm² | 25 mm² |
| 500 W | 12 V | 60 A | 16 mm² | 25 mm² | 35 mm² |
| 700 W | 12 V | 80 A | 25 mm² | 35 mm² | 50 mm² |
| 1000 W | 12 V | 110 A | 35 mm² | 50 mm² | 70 mm² |
| 1500 W | 12 V | 160 A | 50 mm² | 70 mm² | 95 mm² |
| 500 W | 24 V | 30 A | 6 mm² | 10 mm² | 16 mm² |
| 700 W | 24 V | 40 A | 10 mm² | 16 mm² | 25 mm² |
| 1000 W | 24 V | 55 A | 16 mm² | 25 mm² | 35 mm² |
| 1500 W | 24 V | 80 A | 25 mm² | 35 mm² | 50 mm² |
| 2000 W | 24 V | 100 A | 25 mm² | 35 mm² | 50 mm² |

**Hinweis:** Plus- und Minuskabel müssen den GLEICHEN Querschnitt haben.
Das Massekabel wird oft vergessen oder zu dünn ausgeführt — eine der
häufigsten Installationsfehler.

### 17.3 Sicherungsdimensionierung

| Motorleistung | Systemspannung | Nennstrom | Sicherung (empfohlen) | Max. Sicherung |
|:-------------:|:--------------:|:---------:|:--------------------:|:--------------:|
| 300 W | 12 V | 40 A | 50 A | 60 A |
| 500 W | 12 V | 60 A | 80 A | 100 A |
| 700 W | 12 V | 80 A | 100 A | 120 A |
| 1000 W | 12 V | 110 A | 150 A | 175 A |
| 1500 W | 12 V | 160 A | 200 A | 250 A |
| 500 W | 24 V | 30 A | 40 A | 50 A |
| 700 W | 24 V | 40 A | 50 A | 60 A |
| 1000 W | 24 V | 55 A | 70 A | 80 A |
| 1500 W | 24 V | 80 A | 100 A | 120 A |
| 2000 W | 24 V | 100 A | 125 A | 150 A |

**Sicherungstyp:** ANL-Sicherung oder MIDI-Sicherung. KEINE Standard-
KFZ-Flachsicherungen — diese sind für die hohen Ströme nicht geeignet.

### 17.4 Kettengewichte pro Meter

| Kettendicke | DIN 766 (verzinkt) | DIN 766 (Edelstahl 316L) | DIN 764 (verzinkt) |
|:-----------:|:------------------:|:------------------------:|:------------------:|
| 6 mm | 0,75 kg/m | 0,74 kg/m | 0,58 kg/m |
| 7 mm | 1,05 kg/m | 1,03 kg/m | 0,82 kg/m |
| 8 mm | 1,37 kg/m | 1,35 kg/m | 1,07 kg/m |
| 10 mm | 2,20 kg/m | 2,17 kg/m | 1,68 kg/m |
| 12 mm | 3,15 kg/m | 3,10 kg/m | 2,42 kg/m |
| 13 mm | 3,65 kg/m | 3,60 kg/m | 2,85 kg/m |

### 17.5 Windlass-Leistungsklassen nach Bootsgröße

| Bootslänge | Bootstyp | Empfohlene Kettengröße | Empfohlene Windlass-Leistung | Ankergewicht |
|:----------:|---------|:---------------------:|:---------------------------:|:------------:|
| 6–8 m | Segelyacht / Motorboot | 6 mm | 300–500 W | 6–10 kg |
| 8–10 m | Segelyacht / Motorboot | 6–8 mm | 500–700 W | 8–12 kg |
| 10–12 m | Segelyacht | 8 mm | 700–1000 W | 12–16 kg |
| 10–12 m | Motoryacht | 8–10 mm | 700–1000 W | 14–18 kg |
| 12–14 m | Segelyacht | 10 mm | 1000–1500 W | 16–25 kg |
| 12–14 m | Motoryacht | 10 mm | 1000–1500 W | 18–25 kg |
| 14–16 m | Segelyacht | 10 mm | 1500 W | 20–30 kg |
| 14–16 m | Motoryacht | 10–12 mm | 1500–2000 W | 25–35 kg |
| 16–18 m | Segel-/Motoryacht | 10–12 mm | 1500–2500 W | 25–40 kg |
| 18–22 m | Motoryacht | 12–13 mm | 2000–3000 W oder hydraulisch | 35–55 kg |
| 22–30 m | Motoryacht | 13–16 mm | Hydraulisch | 50–80+ kg |

### 17.6 Lebenszyklus-Kosten — 20-Jahre-Vergleich

| Komponente | Anschaffung | Wartung/Jahr | Ersatz (Intervall) | 20-Jahre-Gesamt |
|-----------|:----------:|:------------:|:-----------------:|:---------------:|
| Kette 10mm×60m (verzinkt) | 620 EUR | 30 EUR | 620 EUR (10 J) | 1.860 EUR |
| Kette 10mm×60m (Edelstahl) | 1.800 EUR | 15 EUR | — (>20 J) | 2.100 EUR |
| Neuverzinkung Kette (2×) | — | — | 420 EUR (8 J) | 840 EUR |
| Anker (Bügelanker 16kg verz.) | 280 EUR | 10 EUR | 280 EUR (15 J) | 760 EUR |
| Windlass (Lofrans X2 700W) | 1.400 EUR | 50 EUR | — (>15 J) | 2.400 EUR |
| Windlass Service-Kits (jährlich) | — | 65 EUR | — | 1.300 EUR |
| Wirbel (Mantus, Edelstahl) | 110 EUR | 5 EUR | 110 EUR (8 J) | 430 EUR |
| Snubber (Nylon 18mm×7m) | 75 EUR | 5 EUR | 75 EUR (4 J) | 550 EUR |
| Schäkel (3×, Edelstahl) | 45 EUR | 5 EUR | 45 EUR (7 J) | 280 EUR |
| Pflegemittel (Tef-Gel etc.) | — | 40 EUR | — | 800 EUR |
| **GESAMT (verzinkte Kette)** | | | | **~9.220 EUR** |
| **GESAMT (Edelstahlkette)** | | | | **~9.860 EUR** |

**Erkenntnis:** Die Lebenszyklus-Kosten von verzinkter und Edelstahlkette
unterscheiden sich über 20 Jahre kaum. Der höhere Anschaffungspreis der
Edelstahlkette wird durch entfallende Neuverzinkung und längere Lebensdauer
kompensiert. Für Vielankerer ist Edelstahl langfristig sogar günstiger.

### 17.7 Checkliste Bordwerkzeug — Packliste

```
ANKERSYSTEM — BORDWERKZEUG PACKLISTE
======================================

BASIS-SET (MUSS):
□ Messschieber 150 mm (digital)
□ Multimeter (digital, DC Volt, Widerstand, Durchgang)
□ Ring-Maulschlüssel-Set (8, 10, 13, 17, 19, 22, 24 mm)
□ Schraubendreher PH2, PH1, SL6, SL4
□ Kombizange + Seitenschneider
□ Drahtbürste (Stahl + Messing)
□ Leuchtlupe 10×
□ Kabelbinder UV-beständig (100 Stück)
□ WD-40 / CRC 2-26 Kontaktspray
□ Tef-Gel 30 g
□ Getriebeöl SAE 80W-90 (250 ml)
□ Edelstahldraht 0,8 mm (5 m)
□ Arbeitshandschuhe

ERWEITERT (EMPFOHLEN, bes. Langfahrt):
□ CRC Zinc-It Zinkspray (400 ml)
□ MR Chemie Farbeindringprüf-Set (3 Dosen)
□ Lanocote 120 g
□ Ersatz-Kohlebürsten (Paar, passend!)
□ Ersatz-Wellendichtung (passend!)
□ Ersatz-Solenoid (passend!)
□ Notglieder ×3 (passend zur Kette)
□ Ersatz-Schäkel ×3 (passend)
□ Schrumpfschlauch-Set
□ Kabelschuhe (sortiert, verzinnt)
□ Crimpzange (isoliert)
□ Schleifvlies K120 + K400
□ Dichtmasse (Sikaflex 291i, kleine Tube)
□ LED-Taschenlampe (Stirnlampe)

EXTRAS (WUNSCHLISTE):
□ Schichtdicken-Messgerät (Elcometer)
□ Infrarot-Thermometer (Motor-Temperatur)
□ USB-Endoskopkamera (Getriebe-Inspektion)
□ Akku-Winkelschleifer (Kette kürzen, Rost)
□ Drehmomentschlüssel (5–50 Nm)
```

### 17.8 Saisonkalender nach Revier

| Monat | Ostsee/Nordsee | Mittelmeer | Karibik | Pazifik (NZ/AU) |
|:-----:|:--------------:|:----------:|:-------:|:---------------:|
| Jan | Off-Season | In-Season (leicht) | In-Season (Haupt) | In-Season (Haupt) |
| Feb | Off-Season | In-Season (leicht) | In-Season (Haupt) | In-Season (Haupt) |
| Mär | Pre-Season | In-Season | In-Season | In-Season |
| Apr | Pre-Season | In-Season (Haupt) | In-Season (Ende) | Winterization |
| Mai | In-Season (Beginn) | In-Season (Haupt) | Off-Season (Hurrikane) | Winterization |
| Jun | In-Season | In-Season (Haupt) | Off-Season | Off-Season |
| Jul | In-Season (Haupt) | In-Season (Haupt) | Off-Season | Off-Season |
| Aug | In-Season (Haupt) | In-Season (Haupt) | Off-Season | Off-Season |
| Sep | In-Season (Ende) | In-Season (Haupt) | Off-Season | Pre-Season |
| Okt | Winterization | In-Season | Off-Season | Pre-Season |
| Nov | Winterization | In-Season (Ende) | In-Season (Beginn) | In-Season |
| Dez | Off-Season | Off-Season / Winter | In-Season (Haupt) | In-Season (Haupt) |

**Wartungsplanung:** Pre-Season-Inspektion IMMER 4–6 Wochen vor
geplantem Saisonstart durchführen, damit Zeit für Ersatzteilbeschaffung
und Reparaturen bleibt.

### 17.9 Häufige Fehler bei der Eigenleistungs-Wartung

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Kette nicht vollständig ausgelegt | Verdeckte Schäden übersehen | Kette IMMER komplett auslegen |
| Messschieber nicht kalibriert | Falsche Messungen, falsche Entscheidungen | Vor jeder Messung: Null-Check |
| Getriebeöl nur nachgefüllt, nicht gewechselt | Altöl kontaminiert weiter | Komplett ablassen, dann füllen |
| Sicherung durch größere ersetzt | Kein Schutz bei Kurzschluss/Überlast | Herstellerangabe beachten! |
| Silikon statt PU als Dichtmasse | Haftet nicht auf GFK, löst sich | Sikaflex 291i oder 3M 5200 verwenden |
| Schäkelbolzen ohne Sicherung | Bolzen kann sich lösen → Kettenverlust | IMMER Drahtwicklung oder Splint |
| Kettenkasten nicht gereinigt | Geruch, Korrosion der Kette | Jährlich reinigen, desinfizieren |
| Snubber nach Saison im Cockpit liegen lassen | UV-Degradation, vorzeitiger Verschleiß | UV-geschützt lagern (unter Deck) |
| Windlass-Motor mit Hochdruckreiniger gereinigt | Wasser im Motor → Kurzschluss | Nur mit feuchtem Lappen reinigen |
| Kohlebürsten nicht gleich paarweise getauscht | Ungleichmäßiger Verschleiß, Motor vibriert | IMMER beide Bürsten gleichzeitig tauschen |
| Tef-Gel vergessen bei Schäkel-Montage | Galvanische Korrosion beschleunigt | Tef-Gel auf ALLE Kontaktflächen |
| Falsche Kettennorm bestellt (764 statt 766) | Kette rutscht auf Kettennuss | Standard VOR der Bestellung prüfen |

### 17.10 Windlass-Hersteller — Kontakt und Support

| Hersteller | Land | Website | Support-Telefon | E-Mail | Ersatzteilportal |
|-----------|:----:|---------|:---------------:|--------|:----------------:|
| Lofrans | Italien | lofrans.com | +39 030 968 3521 | info@lofrans.com | Ja (online) |
| Lewmar | UK | lewmar.com | +44 1329 246700 | info@lewmar.com | Ja (online) |
| Quick | Italien | quickitaly.com | +39 0532 363811 | info@quickitaly.com | Ja (online) |
| Maxwell | Neuseeland | maxwellmarine.com | +64 9 985 0960 | sales@maxwellmarine.com | Über Händler |
| Muir | Australien | muir.com.au | +61 3 9774 6533 | sales@muir.com.au | Über Händler |
| Italwinch | Italien | italwinch.com | +39 071 781 0241 | info@italwinch.com | Über Händler |
| Vetus | Niederlande | vetus.com | +31 88 489 1030 | info@vetus.com | Ja (online) |
| South Pacific | Australien | sp-ind.com | +61 2 4323 3766 | — | Über Händler |

### 17.11 Normen-Referenz — Vollständige Liste

| Norm | Titel | Relevanz für Ankersystem-Wartung |
|------|-------|--------------------------------|
| DIN 766 | Rundstahlkette kurzgliedrig (kalibriert) | Maße, Toleranzen, Ablegereife |
| DIN 764 | Rundstahlkette langgliedrig | Alternative Kettenspezifikation |
| DIN EN 818-1 | Kurzgliedrige Rundstahlketten — Sicherheit | Prüfverfahren, Bruchlast |
| DIN EN 818-2 | Rundstahlketten Güteklasse 8 | Hochfeste Ketten |
| ISO 4565:1986 | Ankerketten für Kleinfahrzeuge | Dimensionierung, Mindestanforderungen |
| ISO 15084:2003 | Starke Punkte — Ankern, Vertäuen, Schleppen | Belastungsgrenzwerte für Beschläge |
| ISO 15085:2003 | Mann-über-Bord-Verhütung | Sicherheitsabstände am Bug |
| EN ISO 1461 | Feuerverzinkung | Schichtdicken, Prüfverfahren |
| ASTM A153 | Verzinkung von Eisenwaren | US-Standard für Import-Ketten |
| ISO 3506 | Mechanische Eigenschaften von Edelstahl-Verbindungselementen | Schäkel, Bolzen |
| ABYC H-40 | Ankern, Vertäuen, starke Punkte | US-Standard für Ankergeschirr und starke Punkte |
| ABYC E-11 | Elektrische Systeme an Bord | Kabelquerschnitte, Sicherungen |
| CE 2013/53/EU | Sportboot-Richtlinie | Gesamtsicherheit |
| DIN EN ISO 12217 | Stabilität und Auftrieb | Gewichtsverteilung (Ankersystem) |

### 17.12 Herstellerübergreifende Wartungsintervall-Empfehlungen

| Maßnahme | Lofrans | Lewmar | Quick | Maxwell | Konsens |
|----------|:-------:|:------:|:-----:|:-------:|:-------:|
| Getriebeöl wechseln | 12 Mon. | 12 Mon. | 12 Mon. | 12 Mon. | 12 Mon. |
| Kohlebürsten prüfen | 12 Mon. | 6 Mon. | 12 Mon. | 12 Mon. | 12 Mon. |
| Wellendichtung prüfen | 12 Mon. | 12 Mon. | 12 Mon. | 6 Mon. | 12 Mon. |
| Vollinspektion | 12 Mon. | 12 Mon. | 12 Mon. | 12 Mon. | 12 Mon. |
| Kohlebürsten tauschen | 1000 h | 800 h | 1000 h | 1000 h | 800–1000 h |
| Wellendichtung tauschen | 5 J. | 5 J. | 5–8 J. | 5 J. | 5 J. |
| Getriebe-Revision | 8–10 J. | 10 J. | 10 J. | 8–10 J. | ~10 J. |

### 17.13 Materialverträglichkeits-Matrix

```
MATERIALVERTRÄGLICHKEIT IM ANKERSYSTEM
(✓ = verträglich, ⚠ = mit Isolation, ✗ = vermeiden)

              | Verz.St | Edst.316 | Alu | Bronze | Kupfer | Titan
--------------+---------+----------+-----+--------+--------+------
Verz. Stahl   |   ✓     |    ⚠     |  ⚠  |   ⚠    |   ✗    |  ✗
Edelst. 316   |   ⚠     |    ✓     |  ⚠  |   ✓    |   ✓    |  ✓
Aluminium     |   ⚠     |    ⚠     |  ✓  |   ⚠    |   ✗    |  ✗
Bronze        |   ⚠     |    ✓     |  ⚠  |   ✓    |   ✓    |  ✓
Kupfer        |   ✗     |    ✓     |  ✗  |   ✓    |   ✓    |  ✓
Titan         |   ✗     |    ✓     |  ✗  |   ✓    |   ✓    |  ✓

⚠ = Tef-Gel oder Duralac als Isolation verwenden!
✗ = Nicht kombinieren, auch nicht mit Isolation!
```

### 17.14 Wartungsdokumentation — Digitale Werkzeuge

| App / Tool | Plattform | Funktion | Kosten | Empfehlung |
|-----------|-----------|---------|:------:|:----------:|
| Boat Maintenance Log | iOS/Android | Wartungslogbuch, Erinnerungen | Gratis / Pro 5 EUR/J | ★★★★ |
| Yacht Manager | iOS | Wartung, Inventar, Kosten | 10 EUR/J | ★★★ |
| BoatLogger | Web | Wartung, Treibstoff, Reise | Gratis / Pro 50 EUR/J | ★★★★ |
| Excel / Google Sheets | Web | Eigenes Template | Gratis | ★★★ |
| AYDI (dieses System) | Web | Automatisierte Analyse + Empfehlungen | — | ★★★★★ |

### 17.15 Umrechnungstabellen

| Von | Nach | Faktor |
|----|------|:------:|
| mm | Zoll (inch) | ÷ 25,4 |
| m | Fuß (ft) | × 3,281 |
| m | Faden (fathom) | × 0,547 |
| kg | lbs | × 2,205 |
| kN | kgf | × 101,97 |
| kN | lbs-force | × 224,8 |
| Nm | ft-lbs | × 0,738 |
| mm² | AWG (Kabel) | Tabelle unten |

**Kabelquerschnitt-Umrechnung:**

| mm² | AWG | mm² | AWG |
|:---:|:---:|:---:|:---:|
| 1,5 | 16 | 25 | 4 |
| 2,5 | 14 | 35 | 2 |
| 4 | 12 | 50 | 1/0 |
| 6 | 10 | 70 | 2/0 |
| 10 | 8 | 95 | 3/0 |
| 16 | 6 | 120 | 4/0 |

### 17.16 Checkliste vor dem Ankern (Quick-Reference-Card)

```
VOR DEM ANKERN — SCHNELLPRÜFUNG
==================================

□ Anker auf Bugrolle gesichert?
□ Kettenstopper offen?
□ Windlass-Sicherung EIN?
□ Batterie-Hauptschalter EIN?
□ Kettenzähler auf null?
□ Snubber griffbereit?
□ Wassertiefe geprüft (Echolot)?
□ Schwoikreis berechnet?
□ Untergrund geprüft (Seekarte)?
□ Kettenlänge geplant (Scope 5:1 min)?
□ Fußschalter/Fernbedienung getestet?
□ Motor startbereit (Notfall)?
□ Handschuhe griffbereit?
□ Ankeralarm konfiguriert (GPS)?
```

### 17.17 Sprühfarben für Kettenmarkierung — Produktempfehlungen

| Farbe | Produkt | Preis (2026) | Haltbarkeit | Bezugsquelle |
|-------|---------|:------------:|:-----------:|-------------|
| Rot | Motip Leuchtmarkierung Rot | 8 EUR | 1–2 Saisons | Baumarkt |
| Gelb | Motip Leuchtmarkierung Gelb | 8 EUR | 1–2 Saisons | Baumarkt |
| Blau | Motip Leuchtmarkierung Blau | 8 EUR | 1–2 Saisons | Baumarkt |
| Grün | Motip Leuchtmarkierung Grün | 8 EUR | 1–2 Saisons | Baumarkt |
| Weiß | Motip Leuchtmarkierung Weiß | 8 EUR | 1–2 Saisons | Baumarkt |
| Orange | Motip Leuchtmarkierung Orange | 8 EUR | 1–2 Saisons | Baumarkt |
| 2K-Lack (haltbarer) | Presto 2K Klarlack (Überlack) | 14 EUR | 2–4 Saisons | Baumarkt |

**Tipp:** Farbmarkierung mit 2K-Klarlack überlackieren verdoppelt
die Haltbarkeit. Alternativ: Leuchtfarbe auf die Innenseite des Glieds
auftragen (weniger Abrieb an Kettennuss und Bugrolle).

### 17.18 Typische Fehlerursachen nach Alter der Anlage

| Alter | Typische Fehler | Häufigkeit | Wartungsschwerpunkt |
|:-----:|----------------|:----------:|-------------------|
| 0–3 Jahre | Installationsfehler, falsche Kettennuss | Selten | Erstinspektion, Kabelquerschnitte |
| 3–5 Jahre | Erste Galv.-Verluste, Snubber-UV-Schäden | Gelegentlich | Galvanisierung, Snubber |
| 5–8 Jahre | Kohlebürsten-Ende, Wellendichtung, Schäkel | Häufig | Motor, Dichtungen, Verbinder |
| 8–12 Jahre | Getriebe-Verschleiß, Kettennuss, Kette | Häufig | Mechanik, Kette messen |
| 12–15 Jahre | Motor-Revision, Kette ablegereif, Solenoid | Sehr häufig | Komplettrevision planen |
| 15–20 Jahre | Gesamt-Revision oder Austausch der Anlage | Unvermeidbar | Kosten-Nutzen-Analyse |
| >20 Jahre | Ersatzteil-Verfügbarkeit kritisch | Konstant | Anlage erneuern |

### 17.19 Empfohlene Wartungs-Reihenfolge Pre-Season

Die folgende Reihenfolge ist optimiert für effizienten Arbeitsablauf
(minimale Wartezeiten, logische Abfolge):

```
PRE-SEASON WARTUNGSABLAUF — OPTIMIERT
========================================

PHASE 1 — REINIGUNG (Tag 1, 2–3 Stunden):
  1. Kette komplett aus dem Kasten ziehen
  2. Kette mit Hochdruckreiniger reinigen
  3. Anker abnehmen und reinigen
  4. Kettenkasten auswaschen
  5. Windlass außen reinigen
  6. Alles trocknen lassen (über Nacht ideal)

PHASE 2 — INSPEKTION KETTE + ANKER (Tag 2, 2–3 Stunden):
  1. Kette auslegen (Steg, Pier)
  2. Glieddicke messen (5+ Stellen, Protokoll)
  3. Elongation messen (10-Glieder-Maß)
  4. Galvanisierung bewerten
  5. Verdrehte/steife Glieder suchen
  6. Verbindungsglieder prüfen
  7. Markierungen prüfen/erneuern
  8. Anker: Schweißnähte, Schaft, Galvanisierung
  9. Anker: Bewegliche Teile, Schäkelöse
  10. Protokoll ausfüllen

PHASE 3 — INSPEKTION WINDLASS (Tag 2, 1–2 Stunden):
  1. Sicherung raus!
  2. Motor öffnen → Kohlebürsten messen
  3. Getriebeöl ablassen + begutachten
  4. Wellendichtung prüfen
  5. Neues Getriebeöl einfüllen
  6. Elektrische Verbindungen prüfen + reinigen
  7. Kupplung/Clutch prüfen
  8. Fußschalter testen
  9. Solenoid testen
  10. Motor schließen

PHASE 4 — INSPEKTION PERIPHERIE (Tag 2, 1 Stunde):
  1. Wirbel/Swivel: Drehbarkeit, Spiel, Korrosion
  2. Bugrolle: Lager, Rolle, Befestigung
  3. Snubber: Leine, Haken, Elastizität
  4. Kettenstopper: Funktion, Backen
  5. Alle Schäkel: Sicherung, Verschleiß
  6. Kettenkasten: Drainage, Belüftung, Laminat

PHASE 5 — MONTAGE + TEST (Tag 2 oder 3, 1–2 Stunden):
  1. Kette durch Kettennuss führen (Kompatibilitäts-Check)
  2. Kette in Kettenkasten einlegen (kontrolliert!)
  3. Wirbel + Anker montieren (Tef-Gel!)
  4. Schäkel sichern (Drahtwicklung)
  5. Sicherung einsetzen
  6. Probelauf: 5 m hieven + fieren
  7. Kettenzähler kalibrieren
  8. Snubber bereitlegen
  9. Wartungsprotokoll abschließen
  10. Fertig!

GESAMT: 6–10 Stunden über 2–3 Tage
```

### 17.20 Checkliste Saisonende — Kurzfassung

```
WINTERIZATION KURZCHECKLISTE
==============================

KETTE:
□ Komplett ausziehen
□ Hochdruckreiniger
□ Trocknen (48h)
□ Inspizieren + Protokoll
□ Ggf. Zinkspray
□ Trocken lagern

ANKER:
□ Abnehmen
□ Reinigen + trocknen
□ Zinkspray auf blanke Stellen
□ Tef-Gel auf Gelenke/Bolzen
□ Trocken lagern

WINDLASS:
□ Reinigen (außen + Motorraum)
□ Getriebeöl wechseln
□ Kohlebürsten prüfen
□ Kontakte reinigen + Kontaktfett
□ Kupplung lösen (Neutralstellung)
□ Abdeckung montieren
□ Sicherung entfernen

PERIPHERIE:
□ Wirbel: demontieren, reinigen, Tef-Gel, trocken lagern
□ Bugrolle: reinigen, Lager schmieren
□ Snubber: reinigen, trocknen, UV-geschützt lagern
□ Kettenkasten: reinigen, desinfizieren, belüften
□ Schäkel: prüfen, ggf. ersetzen, mit Kette lagern
```

### 17.21 Inspektions-Befundschlüssel

Für die standardisierte Dokumentation in Inspektionsprotokollen
und im AYDI-System werden folgende Befundkürzel verwendet:

| Kürzel | Bedeutung | Farbe | Maßnahme |
|:------:|-----------|:-----:|----------|
| OK | In Ordnung, kein Mangel | Grün | Keine |
| BEO | Beobachten (leichter Befund) | Gelb | Nächste Inspektion verschärft |
| PLA | Planmäßig ersetzen (Befund) | Orange | Innerhalb 6–12 Monate |
| DRI | Dringend handeln | Rot | Innerhalb 1 Monat |
| SOF | Sofort handeln (Sicherheitsrisiko) | Dunkelrot | Vor nächster Nutzung! |
| NB | Nicht beurteilbar | Grau | Weitere Daten erforderlich |
| NA | Nicht anwendbar | — | Komponente nicht vorhanden |

### 17.22 Ankersystem-Gewichte nach Bootsgröße

| Bootslänge | Anker (kg) | Kette (kg) | Windlass (kg) | Bugrolle (kg) | Gesamt Vorschiff (kg) |
|:----------:|:----------:|:----------:|:-------------:|:-------------:|:--------------------:|
| 8 m | 8 | 23 (6mm/30m) | 10 | 3 | ~48 kg |
| 9 m | 10 | 34 (8mm/25m) | 12 | 3 | ~63 kg |
| 10 m | 12 | 55 (8mm/40m) | 14 | 4 | ~89 kg |
| 11 m | 14 | 62 (8mm/45m) | 16 | 4 | ~100 kg |
| 12 m | 16 | 69 (8mm/50m) | 18 | 5 | ~112 kg |
| 13 m | 18 | 110 (10mm/50m) | 20 | 5 | ~157 kg |
| 14 m | 20 | 132 (10mm/60m) | 22 | 6 | ~184 kg |
| 15 m | 25 | 154 (10mm/70m) | 26 | 6 | ~215 kg |
| 16 m | 25 | 154 (10mm/70m) | 28 | 7 | ~218 kg |
| 18 m | 30 | 176 (10mm/80m) | 34 | 8 | ~252 kg |
| 20 m | 40 | 252 (12mm/80m) | 42 | 9 | ~347 kg |
| 22 m | 45 | 310 (12mm/100m) | 48 | 10 | ~417 kg |
| 25 m | 55 | 365 (13mm/100m) | 60 | 12 | ~496 kg |

**Trimm-Relevanz:** Diese Gewichte im Bug beeinflussen den Längstrimm
erheblich. Pro 50 kg Vorschiffslast ändert sich der Trimm bei einer
12-m-Yacht um ca. 0,3–0,5°. Die AYDI-Strukturanalyse bezieht das
Ankersystemgewicht in die Gewichtsverteilung ein.

### 17.23 Batterie-Anforderungen für Windlass-Betrieb

| Windlass-Leistung | Min. Batteriekapazität | Empfohlene Kapazität | Typ |
|:-----------------:|:---------------------:|:-------------------:|:---:|
| 300 W / 12V | 60 Ah | 100 Ah | AGM/LiFePO4 |
| 500 W / 12V | 80 Ah | 120 Ah | AGM/LiFePO4 |
| 700 W / 12V | 100 Ah | 150 Ah | AGM/LiFePO4 |
| 1000 W / 12V | 150 Ah | 200 Ah | AGM/LiFePO4 |
| 1500 W / 12V | 200 Ah | 300 Ah | AGM/LiFePO4 |
| 700 W / 24V | 60 Ah | 80 Ah | AGM/LiFePO4 |
| 1000 W / 24V | 80 Ah | 100 Ah | AGM/LiFePO4 |
| 1500 W / 24V | 100 Ah | 150 Ah | AGM/LiFePO4 |
| 2000 W / 24V | 120 Ah | 180 Ah | AGM/LiFePO4 |

**LiFePO4-Vorteil:** LiFePO4-Batterien liefern stabile Spannung auch
bei hoher Stromabnahme. AGM-Batterien sacken bei Windlass-Strömen
(80–160 A) um 1–2 V ab, was den Motor verlangsamt. Für intensive
Ankerer ist LiFePO4 die bessere Wahl.

**Dedizierte Starterbatterie:** Einige Eigner installieren eine separate
Batterie nur für den Windlass. Vorteil: Windlass-Betrieb entlädt nicht
die Bordbatterie. Nachteil: Zusätzliches Gewicht, zusätzliche Kabel,
Ladung muss gemanagt werden. Empfehlung: Ab 1000 W separate Batterie
oder Batterie-Umschalter.

### 17.24 Schmiermittel-Übersicht für Ankersystem

| Stelle | Empfohlenes Schmiermittel | Nicht verwenden | Intervall |
|--------|-------------------------|----------------|:---------:|
| Schäkelbolzen | Tef-Gel oder Lanocote | WD-40 (nur temporär) | 12 Mon. |
| Wirbel-Drehachse | Tef-Gel | Silikon (greift PTFE an) | 12 Mon. |
| Bugrolle-Lager | Teflonfett oder Lanocote | Graphitfett (verschmutzt) | 6 Mon. |
| Windlass-Getriebe | SAE 80W-90 GL-4/GL-5 | Motoröl (nur Notfall) | 12 Mon. |
| Windlass-Kupplung | Trocken oder leicht Teflonspray | Fett (rutscht!) | — |
| Kettenstopper-Mechanik | Lanocote oder WD-40 | Graphit | 6 Mon. |
| Ankersicherungs-Pin | Lanocote | — | 6 Mon. |
| Elektrische Kontakte | CRC 2-26 oder Kontaktfett | WD-40 (ungeeignet!) | 6 Mon. |
| Batterieklemmen | Polfett (Liqui Moly) | Vaseline (nur Notfall) | 12 Mon. |
| Fußschalter-Membran | WD-40 Specialist Kontakt | Öl (quillt Gummi) | 12 Mon. |
| Anker-Flunkengelenk | Lanocote oder Tef-Gel | — | 12 Mon. |
| Handkurbel-Steckverbindung | Lanocote | — | 12 Mon. |

---

*Ende der Wissensbasis 17_08 — Ankersysteme — Wartung, Inspektion und Troubleshooting*
*Version 2.0, Stand April 2026*
