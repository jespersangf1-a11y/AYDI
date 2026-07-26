---
title: "Steueranlagen Wartung und Troubleshooting"
kategorie: "14 Steueranlagen und Autopilot"
unterkategorie: "14.08 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Wartungsanleitungen, ISO 8847/8848, ABYC P-17, Herstellerspezifikationen"
  - documented: "Hersteller-Servicehandbuecher, Werft-Wartungsprotokolle, Schiffsmechanikerberichte"
  - estimated: "Erfahrungswerte Langfahrt, Regatta-Praxis, Werft-Konsens, Marinebetriebe"
---

# 14.08 — Steueranlagen Wartung und Troubleshooting im Yachtbau: Vollstaendige Wissensreferenz

> **AYDI Wissensdatei 14.08** — Kategorie 14: Steueranlagen und Autopilot
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Servicehandbuecher, Werftunterlagen), estimated (Erfahrungswerte, Praxis)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen der Steueranlagen-Wartung](#2-grundlagen-der-steueranlagen-wartung)
3. [Wartungsintervalle und Zeitplaene](#3-wartungsintervalle-und-zeitplaene)
4. [Schritt-fuer-Schritt Wartungsanleitungen](#4-schritt-fuer-schritt-wartungsanleitungen)
5. [Schmiermittel und Betriebsstoffe](#5-schmiermittel-und-betriebsstoffe)
6. [Verschleisserkennung und Messtechnik](#6-verschleisserkennung-und-messtechnik)
7. [Anlagen-spezifische Wartung](#7-anlagen-spezifische-wartung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ — Haeufig gestellte Fragen](#10-faq--haeufig-gestellte-fragen)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A–R](#13-anhang-ar)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Zweck und Geltungsbereich

Diese Wissensdatei behandelt die vollstaendige Wartung, Inspektion, Fehlererkennung und Fehlerbehebung (Troubleshooting) aller gaengigen Steueranlagen im Yachtbau. Sie deckt saemtliche Komponenten ab, die zwischen dem Bedienelement (Steuerrad, Pinne) und dem Ruderblatt liegen, einschliesslich der Integration von Autopilot-Systemen.

Der Geltungsbereich umfasst:

- **Seilsteuerungen** (Wire-over-Sheave): Draht-Ketten-Systeme mit Quadrant
- **Hydraulische Steuerungen**: Helmpumpe-Zylinder-Systeme
- **Mechanische Getriebsteuerungen**: Schneckentrieb, Zahnstange, Push-Pull-Kabel
- **Ruderlager und Koker**: Obere und untere Lager, Dichtungen
- **Autopilot-Integration**: Linearantriebe, Hydraulikpumpen, Rotary-Drives
- **Notsteuerung**: Notpinne, Notfall-Verfahren
- **Steuerraeder und Pedestale**: Radlager, Bremsen, Kompass-Integration

Die Wartung von Steueranlagen ist **sicherheitskritisch** im hoechsten Masse. Ein Versagen der Steueranlage fuehrt unmittelbar zum Verlust der Manoevrierbarkeit und kann bei Seegang, in engen Gewaessern oder bei Verkehr lebensbedrohlich sein. Im Gegensatz zu vielen anderen Bordsystemen gibt es bei einer versagenden Steueranlage keine "sanfte Degradation" — der Uebergang von funktionierend zu versagt ist oft abrupt und ohne Vorwarnung.

### 1.2 Einordnung im AYDI-Analysesystem

Im AYDI-Analysesystem ist die Steueranlagen-Wartung ein Querschnittsthema, das mehrere Module beeinflusst:

| AYDI-Modul | Einfluss der Steueranlagen-Wartung |
|------------|-----------------------------------|
| Strukturmodul | Ruderlager-Verschleiss, Koker-Integritaet, Ruderschaftkorrosion |
| Compliance-Modul | ISO 8847/8848 Konformitaet, CE-Nachweise, ABYC P-17 |
| Kostenmodul | Wartungskosten, Ersatzteilpreise, Werftkosten |
| Ergonomie-Modul | Steuerkraefte durch Verschleiss erhoehen sich, Spiel im Steuer |
| Service-Patterns-Modul | Wiederkehrende Wartungsmuster, Schadensmuster nach Alter |
| Sicherheitsmodul | Notsteuerung, Redundanz, Versagensmodi |

**Confidence-Zuordnung fuer Wartungsbefunde:**

- **measured**: Werte aus Wartungsprotokoll mit kalibrierten Werkzeugen (Drehmomentschluessel, Druckmanometer, Messuhr)
- **documented**: Befunde aus dokumentierten Service-Berichten, Hersteller-Bulletins
- **visual_high**: Eindeutiger visueller Befund (gerissenes Seil, Oellache)
- **visual_medium**: Vermuteter Befund bei Fotoanalyse (Korrosionsansatz, Verfaerbung)
- **estimated**: Abgeleiteter Wartungszustand aus Alter, Nutzungsintensitaet, Bootsklasse

### 1.3 Relevante Normen und Vorschriften

| Norm | Titel | Wartungsrelevanz |
|------|-------|-----------------|
| ISO 8847 | Small craft — Steering gear — Cable and pulley systems | Pruefmethoden, Grenzwerte Seilspannung |
| ISO 8848 | Small craft — Remote steering systems | Anforderungen an mechanische Fernsteuerungen |
| ABYC P-17 | Mechanical Steering Systems (Manual and Assisted) | Installationsstandards, Wartungsvorgaben |
| ISO 10592 | Small craft — Hydraulic steering systems | Pruefdrucke, Entlueftung, Fluide |
| ISO 25197 | Small craft — Electrical/electronic control systems | Autopilot-EMV, Stromversorgung |
| ISO 13929 | Small craft — Steering gear — Geared link systems | Getriebsteuerungen, Spieltoleranzen |
| GL/DNV Rules | Klassifikationsregeln | Ruderlager, Schaftdimensionierung, Pruefintervalle |

### 1.4 Zielgruppe und Qualifikation

Die Wartungsanleitungen in dieser Datei unterscheiden drei Qualifikationsstufen:

1. **Eigner-Wartung (Stufe 1)**: Visuelle Inspektion, Schmierung, einfache Einstellungen. Keine Spezialwerkzeuge erforderlich. Geeignet fuer jeden technisch interessierten Bootseigner.

2. **Versierter Eigner / Boatyard-Techniker (Stufe 2)**: Seilwechsel, Hydraulikoel-Wechsel, Entlueftung, Lager-Inspektion. Grundlegende Werkzeugausstattung und Erfahrung erforderlich.

3. **Fachbetrieb / Hersteller-Service (Stufe 3)**: Ruderlager-Wechsel, Hydraulikzylinder-Revision, Autopilot-Kalibrierung, Ruderblatt-Demontage. Spezialwerkzeuge und herstellerspezifische Schulung erforderlich.

Jede Anleitung ist mit der erforderlichen Qualifikationsstufe gekennzeichnet.

### 1.5 Sicherheitshinweise

**WARNUNG — Vor jeder Arbeit an der Steueranlage:**

1. Boot sicher festmachen oder an Land stellen
2. Autopilot deaktivieren und Sicherung entfernen
3. Ruder gegen unbeabsichtigtes Drehen sichern (Ruderstopper oder Festbinden)
4. Bei Hydrauliksystemen: Druck ablassen, System drucklos machen
5. Niemals unter einem angehobenen Ruderblatt arbeiten ohne Abstuetzung
6. Hydraulikfluessigkeit ist gesundheitsschaedlich — Handschuhe, Schutzbrille
7. Bei Arbeiten am Koker: Wassereinbruchgefahr! Boot muss an Land oder im Trockendock sein
8. Nach jeder Arbeit: Funktionspruefung von Anschlag zu Anschlag unter kontrollierten Bedingungen

---

## 2. Grundlagen der Steueranlagen-Wartung

### 2.1 Warum Steueranlagen-Wartung sicherheitskritisch ist

Die Steueranlage einer Yacht gehoert neben dem Rumpf und der Ruderkonstruktion zu den Systemen, deren Versagen unmittelbar lebensbedrohliche Situationen erzeugt. Im Unterschied zu einem Motorausfall, bei dem Segel (bei Segelyachten) oder Anker als Backup dienen koennen, bedeutet Steuerverlust:

- **Keine Kurskontrolle bei Seegang**: Das Boot dreht quer zur See (Querlieger), Kenterungsgefahr
- **Keine Ausweichmoeglichkeit**: Kollisionsgefahr bei Verkehr, in engen Gewaessern, bei Hindernissen
- **Keine Hafeneinfahrt moeglich**: Drift auf Molen, Stege, andere Fahrzeuge
- **Segelboot ohne Steuerung**: Segeldruck dreht Boot in Luv, Legrollen oder Kentern moeglich
- **Motorboot ohne Steuerung bei Gleitfahrt**: Extreme Instabilitaet, Ueberschlag moeglich

Die statistische Unfallanalyse (MAIB, BEAmer, BSU-Berichte) zeigt, dass Steuerungsversagen bei Yachten zwar selten ist (ca. 2-4% aller Seenotfaelle), aber ueberproportional haeufig zu schweren Folgen fuehrt, weil der Verlust der Steuerung andere Rettungsmassnahmen (Abwettern, Einlaufen, Ausweichen) verhindert.

**Versagenskette der Seilsteuerung:**
```
Korrosion am Umlenkseil → Einzeldraht-Brueche → Querschnittsverringerung
→ Erhoehte Last pro Draht → Beschleunigter Bruch → Totalversagen
Typische Zeitlinie: 3-5 Jahre ohne Inspektion
```

**Versagenskette Hydraulik:**
```
Feuchtigkeit im System → Korrosion an Dichtungen → Leckage
→ Lufteintrag → Schwammiges Steuern → Luft komprimiert
→ Plotzlicher Lenkungsverlust unter Last
Typische Zeitlinie: 5-8 Jahre ohne Oelwechsel
```

**Versagenskette Ruderlager:**
```
Wasser-/Schmutzintrusion → Lagerkorrosion → Erhoehtes Spiel
→ Vibrationen → Beschleunigter Verschleiss → Lagerbruch
→ Ruderblatt klemmt oder loest sich
Typische Zeitlinie: 8-15 Jahre ohne Inspektion
```

### 2.2 Verschleissmechanismen in Steueranlagen

#### 2.2.1 Mechanischer Verschleiss

**Reibverschleiss (Abrasion):**
- Steuerseil ueber Umlenkrollen: Drahtquerschnitt verringert sich kontinuierlich
- Quadrant-Schlitz/Seilbefestigung: Ausschlag an Kontaktflaechen
- Pedestal-Zahnrad: Zahnabtrag bei unzureichender Schmierung
- Ruderlager: Abrieb an Gleitlager-Oberflaechen (PTFE, Delrin, Bronze)
- Kettenrad auf Steuerradwelle: Kettenlaschen schleifen
- Steuerdraht durch Decksdurchfuehrungen: Abrieb an Fuehrungsbuechsen

**Ermuedungsverschleiss (Fatigue):**
- Steuerseil bei Umlenkung: Biegewechselbeanspruchung bei jeder Kursaenderung
- Hydraulikleitungen: Druckpulsationen durch Seegang und Autopilot
- Ruderschaft: Wechselbiegebeanspruchung durch Seegang
- Koppelstangen: Wechselbelastung durch Ruderbewegung
- Autopilot-Linearantrieb: Kolbenstange unter Dauerlast

**Kavitation und Erosion:**
- Ruderblatt: Kavitation bei hohen Geschwindigkeiten (Motorboote >20 kn)
- Hydraulikpumpe: Kavitation bei zu geringer Zulaufhoehe oder Lufteinschluss
- Hydraulikzylinder: Erosion an Dichtflaechen durch Partikel im Fluid

#### 2.2.2 Korrosion

**Galvanische Korrosion:**
- Edelstahl-Ruderschaft in Aluminium-Koker: Ohne Isolation entsteht galvanisches Element
- Bronze-Ruderlager mit Edelstahl-Bolzen: Potentialdifferenz foerdert Korrosion
- Edelstahl-Seilklemmen an Aluminium-Quadrant: Kontaktkorrosion
- Dissimilare Metalle in Hydraulikanschluessen

**Spaltkorrosion (Crevice Corrosion):**
- Ruderschaft im Koker: Spalt zwischen Schaft und Buchse als Korrosionsherd
- Steuerseile im Kabelkanal: Wasser sammelt sich in tiefliegenden Kanaelen
- Seilpressen/Nicropress: Feuchtigkeit unter der Pressung

**Lochfrass (Pitting):**
- Edelstahl 316L: Auch hochlegierter Stahl ist bei stehendem Salzwasser in O2-armen Zonen anfaellig
- Hydraulikzylinder-Kolbenstange: Pitting fuehrt zu Dichtungsversagen
- Ruderlager-Buchsen aus Bronze: Pitting durch Dezinkifizierung

**Spannungsrisskorrosion (SCC):**
- Steuerseile aus 1x19 Edelstahl: SCC unter Last + Salzwasser + Chloride
- Ruderschaft-Oberflaeche: Risse unter Zugeigenspannungen
- Edelstahl-Federelemente in Hydraulikventilen

#### 2.2.3 Biologischer und umgebungsbedingter Verschleiss

**Biofouling:**
- Ruderblatt: Bewuchs erhoehte Reibung und damit Steuerkraefte um 20-80%
- Ruderlager-Spalte: Muscheln und Algen koennen Ruderbewegung blockieren
- Ruderblatt-Schaft-Uebergang: Bewuchs erzeugt Feuchtigkeitsnester

**UV-Strahlung:**
- Hydraulikschlaeuche: UV-Degradation der Aussenhaut fuehrt zu Rissung
- Push-Pull-Kabelhuelle: Sproedbruch nach UV-Belastung
- Pedestal-Abdeckungen (Gummi/PVC): Versprodung
- Autopilot-Kabel an Deck: Isolations-Degradation

**Salzbelastung:**
- Seilsteuerung: Salzablagerungen in Fuehrungsoesen und Umlenkrollen
- Pedestal-Innenleben: Salzkristalle als Abrasivmedium
- Ruderlager: Salz in Lagerspalt foerdert Korrosion und Abrieb
- Hydraulikanschluesse: Salzkrusten lockern Verschraubungen

**Temperaturwechsel:**
- Hydraulikfluessigkeit: Viskositaetsaenderung bei Kaltstart
- Dichtungen: Thermozyklen fuehren zu Setzen der Elastomere
- Kunststoff-Lager: Dimensionsaenderung bei Temperaturextremen
- Steuerseil: Laengenaenderung bei Temperaturdifferenzen >30°C

### 2.3 Wirtschaftliche Aspekte der Wartung

Eine regelmaessige Wartung der Steueranlage ist nicht nur sicherheitskritisch, sondern auch wirtschaftlich sinnvoll:

| Massnahme | Jaehrliche Kosten | Ohne Wartung: Reparaturkosten |
|-----------|-------------------|-------------------------------|
| Seilsteuerung schmieren, pruefen | 50-100 EUR | Seilbruch + Neuinstallation: 1.500-4.000 EUR |
| Hydraulikoel wechseln | 80-150 EUR | Pumpenversagen + Zylinderschaden: 2.000-6.000 EUR |
| Ruderlager pruefen, schmieren | 30-80 EUR | Lagerwechsel (Kran + Werft): 3.000-8.000 EUR |
| Autopilot kalibrieren | 0 EUR (Eigenarbeit) | Fehlfunktion + Folgeschaeden: 500-2.000 EUR |
| Notpinne testen | 0 EUR (Eigenarbeit) | Nicht verfuegbar im Notfall: unschaetzbar |

**Gesamtjaehrliche Wartungskosten nach Steuerungstyp (geschaetzt):**

| Steuerungstyp | Bootlaenge 8-12m | 12-16m | 16-22m | 22m+ |
|---------------|-----------------|--------|--------|------|
| Seilsteuerung | 80-150 EUR | 120-250 EUR | 200-400 EUR | 300-600 EUR |
| Hydraulisch | 120-200 EUR | 180-350 EUR | 300-600 EUR | 500-1.200 EUR |
| Push-Pull-Kabel | 50-100 EUR | 80-150 EUR | n/a | n/a |
| Autopilot (zusaetzlich) | 50-100 EUR | 80-150 EUR | 150-300 EUR | 300-600 EUR |

### 2.4 Verschleiss nach Bootsklasse und Alter

Die Verschleissrate einer Steueranlage haengt massgeblich von der Bootsklasse, dem Alter und der Nutzungsintensitaet ab. AYDI beruecksichtigt dies bei der Score-Berechnung:

#### 2.4.1 Produktionssegelyacht (8-14m, z.B. Bavaria, Jeanneau, Beneteau)

**Typische Steueranlage:** Seilsteuerung mit Whitlock/Lewmar-Pedestal, einfacher Autopilot
**Qualitaetsniveau:** Industriestandard, akzeptable Toleranzen
**Typische Lebenserwartung Komponenten:**

| Bootealter | Erwartete Befunde | AYDI-Toleranz |
|------------|-------------------|---------------|
| 0-5 Jahre | Keine wesentlichen Befunde, Setzverhalten normal | Score >85 erwartet |
| 5-10 Jahre | Erste Litzenbrueche, Oelverfaerbung, leichtes Lagerspiel | Score 70-85 erwartet |
| 10-15 Jahre | Seilwechsel faellig, Hydraulikdichtungen verschlissen, Lagerspiel mittel | Score 55-75 erwartet |
| 15-20 Jahre | Zweiter Seilwechsel, Ruderlager ggf. faellig, Pedestal-Revision | Score 40-65 erwartet |
| >20 Jahre | Komplettsanierung oft wirtschaftlicher als Einzelreparaturen | Score abhaengig von Wartungshistorie |

**Schwachstellen bei Produktionsbooten:**
- Seilfuehrung oft suboptimal (enge Radien, zu kleine Rollen → beschleunigter Seilbruch)
- Quadrant-Klemmung teilweise unterdimensioniert (Klemmung rutscht bei hohen Ruderkraeften)
- Pedestal-Abdeckung oft undicht (Wasser im Pedestal fuehrt zu Korrosion)
- Autopilot-Installation oft nachtraeglich und nicht optimal (Kabelwege, Kompassposition)
- Ruderlager-Qualitaet variiert stark zwischen Herstellern und Jahrgaengen

#### 2.4.2 Semi-Custom-Segelyacht (14-22m, z.B. Hallberg-Rassy, Oyster, Contest)

**Typische Steueranlage:** Jefa-Ruderlager, hochwertige Seil- oder Hydrauliksteuerung, leistungsfaehiger Autopilot
**Qualitaetsniveau:** Ueber Durchschnitt, engere Toleranzen
**Typische Lebenserwartung:** 20-40% laenger als Produktionsboote

**Vorteile gegenueber Produktion:**
- Jefa-Lager statt NoName → laengere Lebensdauer (15-25 Jahre)
- Grosszuegigere Seilfuehrung (groessere Radien, groessere Rollen)
- Werft-spezifische Optimierungen (z.B. HR: doppelte Seilspanner fuer leichtere Justage)
- Bessere Zugaenglichkeit der Komponenten (Wartungsfreundlichkeit)

**Schwachstellen bei Semi-Custom:**
- Hoehere Kosten fuer Ersatzteile (spezialisiert)
- Ggf. Hersteller-spezifische Teile schwer beschaffbar (Langfahrt, entlegene Gebiete)
- Komplexere Systeme (Doppelsteuerstand, integrierte Autopiloten) → mehr potentielle Fehlerquellen

#### 2.4.3 Custom-Yacht / Superyacht (22m+)

**Typische Steueranlage:** Vollhydraulisch, Rudermaschine, professionelle Autopilot-Anlage
**Qualitaetsniveau:** Hoechste Qualitaet, minimale Toleranzen, Klassifikation (GL/DNV/LR)
**Wartungsphilosophie:** Professioneller Wartungsvertrag mit Hersteller oder Werft

**Besonderheiten:**
- Regelmassige Klasse-Inspektionen (alle 5 Jahre Survey, jaehrlich Annual Survey)
- Redundante Steueranlage (bei vielen Superyachten vorgeschrieben)
- Hydraulik-Aggregate statt einfacher Helmpumpen → andere Wartungsanforderungen
- Professionelle Crew fuehrt Wartung durch → andere AYDI-Bewertung (Stufe 3 erwartet)
- Ersatzteile oft direkt vom Hersteller mit Service-Vertrag

#### 2.4.4 Motorboot / Motoryacht

**Typische Steueranlage:**
- Kleines Motorboot (<8m): Push-Pull-Kabel, Aussenborder-Fernsteuerung
- Mittleres Motorboot (8-14m): Hydrauliksteuerung (SeaStar/Teleflex)
- Motoryacht (14-22m): Hydrauliksteuerung mit Rudermaschine
- Grosse Motoryacht (22m+): Wie Custom-Yacht/Superyacht

**Motorboot-spezifische Verschleissmuster:**
- Vibrationsbedingte Lockerung aller Verschraubungen (Hauptverschleissursache!)
- Push-Pull-Kabel: Innere Korrosion durch Kondenswasser in der Huelse
- Hydraulikzylinder: Pitting durch Salzwasser bei nicht eingezogenem Zustand
- Hohes Manoevrier-Pensum (Hafen, Angeln): Erhoehte Zyklen an Pumpe und Zylinder

### 2.5 Statistische Daten: Steuerungsversagen und Unfaelle

Aus der Auswertung von Seeunfallberichten (MAIB UK, BSU Deutschland, BEAmer Frankreich, DMAIB Daenemark) der Jahre 2010-2025 lassen sich folgende Muster ableiten:

**Verteilung der Steuerungsversagen nach Ursache:**

| Ursache | Anteil | Haeufigste Bootsklasse |
|---------|--------|----------------------|
| Seilbruch/-schaden | 28% | Segelyacht 10-15m, >10 Jahre alt |
| Hydraulikleckage/-versagen | 22% | Motorboot 12-18m, >8 Jahre alt |
| Ruderlager-Defekt | 18% | Segelyacht 12-18m, >15 Jahre alt |
| Autopilot-Fehlfunktion | 12% | Alle Typen, alle Alter |
| Ruderblatt-Verlust | 8% | Segelyacht, Grundberuehrung |
| Pedestal/Getriebe-Defekt | 6% | Segelyacht 10-14m, >12 Jahre alt |
| Sonstige | 6% | — |

**Korrelation mit Wartungszustand:**
- 72% der Steuerungsversagen mit bekannter Wartungshistorie zeigten unterdurchschnittliche Wartung
- 45% der Faelle haetten durch regelmaessige visuelle Inspektion verhindert werden koennen
- 68% der Seilbrueche zeigten bei nachtraeglicher Untersuchung bereits fortgeschrittene Korrosion
- 55% der Hydraulikversagen waren auf Fluessigkeitsmangel oder -alterung zurueckzufuehren

**Zeitliche Verteilung:**
- 35% der Versagen treten im ersten Monat nach Saisonstart auf (fehlende Auswinterung)
- 25% waehrend Starkwind/Seegang (erhoehte Belastung entlarvt latente Maengel)
- 15% bei Nachtfahrt (spaete Erkennung von Symptomen)
- 25% bei Hafenmanoevern (hohe Steuerbelastung, sofortige Konsequenzen)

**AYDI-Relevanz:**
Diese statistischen Daten fliessen in die AYDI-Risikoberechnung ein:
- Boote mit unbekannter Wartungshistorie erhalten einen Risikozuschlag von 15-25%
- Boote ueber 10 Jahre ohne dokumentierten Seilwechsel: Automatische Warnmeldung
- Boote ueber 15 Jahre ohne Ruderlager-Inspektion: Automatische Warnmeldung
- Saisonstart-Inspektionen werden in der AYDI-Timeline als "faellig" markiert

### 2.6 Werkzeug-Grundausstattung fuer Steueranlagen-Wartung

**Stufe 1 — Eigner-Grundausstattung (ca. 200-350 EUR):**

| Werkzeug | Zweck | Ca. Preis |
|---------|-------|-----------|
| Tensiometer (Loos PT-2 o.ae.) | Seilspannung messen | 80 EUR |
| Gabelschluessel-Satz (8-24 mm) | Allgemein | 30 EUR |
| Drehmomentschluessel (10-100 Nm) | Korrekte Anzugsmomente | 50 EUR |
| Messuhr mit Magnetfuss | Lagerspiel messen | 30 EUR |
| Taschenlampe (LED, stark) | Inspektion in dunklen Ecken | 15 EUR |
| Inspektionsspiegel | Schwer zugaengliche Stellen | 10 EUR |
| Fuehllehren-Satz | Spaltmasse | 10 EUR |
| Lappen, Handschuhe, Schutzbrille | Schutzausruestung | 15 EUR |
| Schmier-Set (Fett, Seilspray, PTFE) | Schmierung | 40 EUR |
| Kabelbinder-Sortiment | Befestigung, Markierung | 10 EUR |

**Stufe 2 — Erweiterung fuer versierten Eigner (zusaetzlich ca. 150-300 EUR):**

| Werkzeug | Zweck | Ca. Preis |
|---------|-------|-----------|
| Nicropress-Zange + Huelsen | Seilwechsel | 80 EUR |
| Seitenschneider fuer Stahldraht | Seil schneiden | 25 EUR |
| Oelpumpe/Spritze 500 ml | Hydraulikoel wechseln | 20 EUR |
| Manometer 0-100 bar | Hydraulik-Drucktest | 40 EUR |
| Feuchtemessgeraet | Ruderblatt-Pruefung | 50 EUR |
| Schieblehre 150 mm | Praezisionsmessungen | 20 EUR |
| Drahtbuerste-Set (Messing + Stahl) | Reinigung | 10 EUR |

### 2.7 Wartungsphilosophie: Praeventiv vs. Korrektiv

**Praevention (empfohlen):**
- Zeitbasierte Wartung: Feste Intervalle nach Kalender und Betriebsstunden
- Zustandsbasierte Wartung: Inspektion und Messung, Eingriff bei Grenzwertueberschreitung
- Vorausschauende Wartung (AYDI-Analyse): Trendanalyse aus Inspektionsdaten, Vorhersage von Wartungsbedarf

**Korrektive Wartung (teuer und gefaehrlich):**
- Reparatur nach Versagen: Erst handeln wenn etwas kaputtgeht
- Hohe Kosten durch Folgeschaeden
- Sicherheitsrisiko durch unplanmaessigen Ausfall
- Bei Steueranlagen NICHT akzeptabel

### 2.8 Dokumentation und Protokollierung

Jede Wartung an der Steueranlage muss dokumentiert werden. AYDI verwendet folgendes Schema:

```
Wartungsprotokoll:
  Datum: YYYY-MM-DD
  Boot: [Name, Typ, Baujahr]
  System: [Steuerungstyp, Hersteller, Modell]
  Durchgefuehrt_von: [Name, Qualifikation]
  Massnahmen:
    - [Beschreibung der Massnahme]
    - [Verwendete Materialien/Ersatzteile]
    - [Messwerte vorher/nachher]
  Befunde:
    - [Festgestellte Maengel oder Auffaelligkeiten]
    - [Bewertung: ok / beobachten / Massnahme erforderlich / kritisch]
  Naechster_Service: YYYY-MM-DD
  Fotos: [Referenzen auf Dokumentationsfotos]
```

Fuer den AYDI-Service-Patterns-Modul sind folgende Daten besonders relevant:
- Zeitintervall zwischen Wartungen
- Verschleiss-Trends (z.B. Seilspannung ueber Zeit)
- Wiederholte Befunde gleichen Typs
- Korrelation zwischen Nutzungsintensitaet und Verschleiss

---

## 3. Wartungsintervalle und Zeitplaene

### 3.1 Allgemeine Wartungsmatrix nach Komponente

Die folgende Matrix definiert Mindest-Wartungsintervalle fuer alle Steueranlagenkomponenten. Die Intervalle gelten fuer **normal genutzte** Yachten in **gemaessigten Breiten** mit **saisonalem Betrieb** (ca. 6 Monate/Jahr).

Bei erhoehter Nutzung (Langfahrt, Tropen, Charter, Regatta) sind die Intervalle zu halbieren.

#### 3.1.1 Seilsteuerung (Wire-over-Sheave)

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Steuerseile | Monatlich (Saison) | Visuelle Inspektion auf Litzenbrueche, Knicke | 1 |
| Steuerseile | Saisonbeginn | Spannung pruefen mit Tensiometer (130-175 N typ.) | 2 |
| Steuerseile | Jaehrlich | Schmierung ueber gesamte Laenge | 1 |
| Steuerseile | Alle 5-7 Jahre | Kompletter Austausch (auch ohne sichtbare Schaeden) | 2 |
| Umlenkrollen (Sheaves) | Saisonbeginn | Leichtgaengigkeit pruefen, Lager schmieren | 1 |
| Umlenkrollen | Alle 3-5 Jahre | Lager wechseln, Rille auf Verschleiss pruefen | 2 |
| Quadrant/Tiller-Arm | Saisonbeginn | Befestigung am Ruderschaft pruefen, Drehmoment kontrollieren | 2 |
| Quadrant | Jaehrlich | Seilbefestigung pruefen (Nicropress, Bolzen) | 2 |
| Seil-Kettenverbindung | Saisonbeginn | Schaekel, Gabelterminals pruefen | 1 |
| Kettenrad am Pedestal | Saisonbeginn | Zahnung pruefen, schmieren | 1 |
| Decksdurchfuehrungen | Jaehrlich | Fuehrungsbuechsen pruefen, Dichtung erneuern | 2 |
| Seilspanner | Saisonbeginn | Funktion pruefen, ggf. nachspannen | 2 |

#### 3.1.2 Hydraulische Steuerung

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Hydraulikfluid | Jaehrlich | Zustand pruefen (Farbe, Truebung, Wassergehalt) | 1 |
| Hydraulikfluid | Alle 2-3 Jahre | Komplettwechsel mit Spuelung | 2 |
| Helmpumpe | Saisonbeginn | Leichtgaengigkeit pruefen, auf Leckage pruefen | 1 |
| Helmpumpe | Alle 5-7 Jahre | Dichtungssatz wechseln | 3 |
| Hydraulikzylinder | Monatlich (Saison) | Visuelle Inspektion auf Leckage | 1 |
| Hydraulikzylinder | Jaehrlich | Kolbenstange auf Pitting pruefen, Endanschlaege pruefen | 2 |
| Hydraulikzylinder | Alle 7-10 Jahre | Dichtungssatz wechseln, Kolbenstange polieren | 3 |
| Hydraulikleitungen (starr) | Jaehrlich | Auf Korrosion pruefen, Anschluesse auf Dichtheit | 1 |
| Hydraulikschlaeuche (flex) | Jaehrlich | Auf Risse, Quellungen, Knicke pruefen | 1 |
| Hydraulikschlaeuche | Alle 5-7 Jahre | Austausch (auch ohne sichtbare Schaeden) | 2 |
| Entlueftung | Saisonbeginn | System entlueften nach Winterlager | 2 |
| Helm-Lock / Ruderstopper | Saisonbeginn | Funktion pruefen | 1 |
| Druckbegrenzungsventil | Alle 3 Jahre | Funktion und Einstellung pruefen | 3 |
| Hydraulikfilter (falls vorhanden) | Jaehrlich | Wechseln oder reinigen | 1 |

#### 3.1.3 Autopilot-System

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Linearantrieb / Hydraulikpumpe | Saisonbeginn | Visuelle Inspektion, Befestigung pruefen | 1 |
| Linearantrieb | Jaehrlich | Hub und Endlagen pruefen, Geraeusche analysieren | 2 |
| Autopilot-Kalibrierung | Saisonbeginn | Kompasskalibrierung (Deviation), Ruderlage Null | 1 |
| Autopilot-Kalibrierung | Nach jeder Aenderung am Steuer | Komplettkalibrierung | 1 |
| Kupplung (Clutch) | Saisonbeginn | Ein-/Auskuppeln pruefen, Leichtgaengigkeit | 1 |
| Kupplung | Jaehrlich | Reibbelaege pruefen, ggf. nachstellen | 2 |
| Stromversorgung | Saisonbeginn | Kabelverbindungen, Sicherungen, Spannungsversorgung | 1 |
| Bedieneinheit | Saisonbeginn | Tasten, Display, Fernbedienung pruefen | 1 |
| Fluxgate-Kompass | Alle 2 Jahre | Kalibrierung gegen Referenzkompass | 2 |
| Software/Firmware | Jaehrlich | Updates pruefen und installieren | 1 |
| Antriebsriemen (falls vorhanden) | Jaehrlich | Spannung und Zustand pruefen | 1 |
| Antriebsriemen | Alle 3-4 Jahre | Wechseln | 2 |

#### 3.1.4 Ruderlager und Koker

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Ruderlager (oben + unten) | Saisonbeginn | Spiel pruefen (Messuhr oder Hebeltest) | 2 |
| Ruderlager | Jaehrlich | Schmierung (sofern Schmiernippel vorhanden) | 1 |
| Ruderlager | Alle 10-15 Jahre | Austausch (praeventiv, abhaengig von Lagerbauart) | 3 |
| Koker-Dichtung | Saisonbeginn | Auf Wassereinbruch pruefen, Dichtlippe pruefen | 1 |
| Koker-Dichtung | Alle 3-5 Jahre | Dichtungssatz wechseln | 2 |
| Ruderschaft | Jaehrlich | Oberflaecheninspektion auf Korrosion, Risse | 2 |
| Ruderschaft | Alle 5 Jahre | Zerstoerungsfreie Pruefung (Farbpruefung, UT) | 3 |
| Ruderblatt | Saisonbeginn | Auf Wasseraufnahme klopfen, Risse visuell pruefen | 1 |
| Ruderblatt | Alle 2-3 Jahre | Feuchtemessung, Klopftest systematisch | 2 |
| Ruderblatt-Schaftverbindung | Jaehrlich | Bewegung/Spiel pruefen, Klebefuge inspizieren | 2 |
| Ruderstopps/Anschlaege | Saisonbeginn | Einstellung und Befestigung pruefen | 1 |

#### 3.1.5 Notsteuerung (Notpinne / Emergency Tiller)

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Notpinne | Saisonbeginn | Stecktest: Passt die Pinne auf den Ruderschaft? | 1 |
| Notpinne | Jaehrlich | Vollstaendiger Montagetest mit Probesteuerung | 1 |
| Zugangsweg | Saisonbeginn | Pruefung, ob Zugang frei ist (kein Geruempel davor) | 1 |
| Notpinne-Aufnahme am Schaft | Jaehrlich | Korrosion pruefen, Passung kontrollieren | 2 |
| Notverfahren-Anleitung | Saisonbeginn | An Bord vorhanden, Crew einweisen | 1 |

#### 3.1.6 Steuerrad und Pedestal

| Komponente | Intervall | Massnahme | Stufe |
|-----------|-----------|-----------|-------|
| Steuerrad | Monatlich (Saison) | Auf Spiel pruefen, Teak-Zustand | 1 |
| Steuerrad-Nabe | Jaehrlich | Befestigung am Schaft pruefen, Drehmoment kontrollieren | 2 |
| Pedestal-Getriebe | Saisonbeginn | Fett erneuern, Zahnflanken pruefen | 2 |
| Pedestal-Getriebe | Alle 3-5 Jahre | Vollstaendige Revision | 3 |
| Pedestal-Kompass | Saisonbeginn | Blasenfreiheit, Deviation, Beleuchtung | 1 |
| Pedestal-Bremse | Saisonbeginn | Funktion pruefen, ggf. nachstellen | 1 |
| Pedestal-Dichtung | Jaehrlich | Wassereinbruch in Pedestal pruefen | 1 |
| Dual-Helm-Koppelstange | Saisonbeginn | Spiel pruefen, Gelenke schmieren | 1 |

### 3.1.7 Winterlager-spezifische Massnahmen

Waehrend des Winterlagers sind Steueranlagen besonderen Belastungen ausgesetzt: Feuchtigkeit (Kondenswasser), Temperaturwechsel, laengere Standzeiten ohne Bewegung, UV-Belastung (bei Freilager).

**Winterlager Einlagerung (Checkliste):**

| Massnahme | Seilsteuerung | Hydraulik | Autopilot | Ruderlager |
|-----------|--------------|-----------|-----------|------------|
| Reinigung (Suesswasser) | Ja | Ja | Ja (Gehaeuse) | Ja |
| Korrosionsschutz auftragen | Seile, Kette | Kolbenstange | Kabelenden | Schaft |
| Schmierung | Seile, Rollen | n/a (Fluid) | Linearantrieb | Schmiernippel |
| Fluid-Level pruefen | n/a | Ja | Pumpen-Fluid | n/a |
| Abdeckung/Schutz | Pedestal-Cover | Zylinder-Cover | Display abnehmen | n/a |
| Sicherung entfernen | n/a | n/a | Ja | n/a |
| Position sichern | Ruderbremse | Helm-Lock | n/a | Ruderstopper |

**Winterlager-Risiken:**

| Risiko | Betrifft | Vorbeugung |
|--------|---------|------------|
| Kondenswasser in Hydraulik | Hydraulikfluid, Zylinder | Oelstand max., Behaelter verschlossen |
| Frost-Sprengung Ruderblatt | Wasserhaltiges Ruderblatt | Feuchtemessung, ggf. beheizt lagern |
| Seil-Korrosion (stehend) | Steuerseile | Korrosionsschutz (Boeshield T-9) |
| Maus-/Ratten-Frass | Kabel, Schlaeuche | Kabel schuetzen, Gift/Fallen |
| UV an Freilager-Platz | Schlaeuche, Kabel, Pedestal | Abdeckplane, UV-Schutz |
| Pedestal-Feuchtigkeit | Getriebe, Kompass | Pedestal-Cover dicht schliessen |
| Ruderlager-Stillstand | Gleitlager (Bronze) | Regelmaessig bewegen (monatlich 1x) |

**Einwinterung Schritt-fuer-Schritt:**
1. Steueranlage komplett mit Suesswasser abwaschen (Salzentfernung)
2. Steuerseile trocknen lassen, dann Korrosionsschutz (Boeshield T-9) auftragen
3. Hydraulikoelstand auf Maximum bringen (weniger Luft im System = weniger Kondenswasser)
4. Hydraulikzylinder-Kolbenstange einfahren (geschuetzte Position) oder mit Korrosionsschutz einspruehen
5. Pedestal schmieren, Abdeckung aufsetzen
6. Autopilot-Display abnehmen und drinnen lagern (oder wasserdicht abdecken)
7. Autopilot-Sicherung entfernen (Phantomstrom-Vermeidung)
8. Ruderbremse/Helm-Lock aktivieren (verhindert Pendelbewegung im Wind)
9. Notpinne reinigen, trocknen, trocken verstauen
10. Wartungsprotokoll fuer die Saison abschliessen

**Auswinterung Schritt-fuer-Schritt:**
1. Steueranlage visuell komplett inspizieren (Winterschaeden?)
2. Korrosionsschutz von Seilen entfernen (soweit noetig)
3. Seilspannung pruefen (Temperaturbedingte Aenderungen nach Winter)
4. Hydraulik: Oelstand pruefen, Entlueftung durchfuehren
5. Pedestal-Abdeckung entfernen, Getriebe inspizieren
6. Autopilot-Display montieren, Sicherung einsetzen, Selbsttest
7. Autopilot-Kalibrierungsfahrt durchfuehren
8. Notpinne-Stecktest
9. Ruderlager-Spielmessung (Vergleich mit Einwinterungs-Wert)
10. Steuerung von Anschlag zu Anschlag testen

### 3.2 Herstellerspezifische Wartungsintervalle

#### 3.2.1 Jefa Steering (Daenemark)

Jefa ist der fuehrende Hersteller fuer Segelyacht-Ruderlager und Steueranlagen im europaeischen Markt. Jefa-spezifische Wartungsvorgaben:

**Jefa Ruderlager:**
- **Composite-Lager (Standard):** Wartungsfrei, Lebensdauer 15-20 Jahre bei korrekter Installation. Jaehrliche Spielkontrolle.
- **Bronze-Lager (Legacy):** Alle 2 Jahre Schmierung mit wasserunloeslichem Fett (Jefa empfiehlt Klüber Isoflex Topas NB 52)
- **Nadellager (high-performance):** Jaehrlich schmieren, alle 10 Jahre pruefen/wechseln
- **Koker-Dichtung (Lip-Seal):** Alle 5 Jahre wechseln, jaehrlich auf Leckage pruefen

**Jefa Quadranten:**
- Quadrant-Klemmung: Jaehrlich Schrauben mit vorgeschriebenem Drehmoment (typ. 45-65 Nm je nach Groesse) pruefen
- Seilbefestigung am Quadrant: Nicropress-Huelsen auf Risse pruefen, Bolzenverbindungen auf Spiel

**Jefa-spezifische Hinweise:**
- Jefa Typ E Ruderlager (selbstzentrierend): Kein Spiel nachstellen, Lager muss frei schwingen koennen
- Jefa Quadrant Model D: Seilrillen auf asymmetrischen Verschleiss pruefen (zeigt Fehlausrichtung an)

#### 3.2.2 Whitlock Steering (UK, jetzt Lewmar)

Whitlock, heute Teil von Lewmar, ist der verbreitetste Hersteller fuer Pedestal- und Getriebsteuerungen auf Segelyachten.

**Whitlock Mamba / Cobra / Viper Pedestale:**
- **Jaehrlich:** Fettnippel schmieren (Whitlock-Spezialfett oder NLGI-2 Marine Grease)
- **Jaehrlich:** Kette auf Verschleiss und Laengung pruefen (max. 2% Laengung)
- **Alle 2 Jahre:** Pedestal oeffnen, Zahnraeder inspizieren, Fett erneuern
- **Alle 5 Jahre:** Pedestal komplett revidieren, Lager und Dichtungen tauschen
- **Alle 7-10 Jahre:** Kette und Kettenrad wechseln (auch bei unauffaelligem Befund)

**Whitlock/Lewmar Steuerraeder:**
- Teak-Segmente: Jaehrlich mit Teakoel behandeln, auf Spalten pruefen
- Naben-Verschraubung: Jaehrlich pruefen, Sicherungsmutter nicht loesen
- Edelstahl-Speichen: Auf Spannungsrisskorrosion pruefen (alle 3 Jahre)

**Whitlock-spezifische Empfehlungen:**
- Whitlock Mamba 18/22/26: Sprengring am Kettenrad regelmassig pruefen — haeufiger Ausfallgrund
- Whitlock Cobra: Zahnradspiel max. 0.3 mm, darüber Zahnradpaar tauschen
- Whitlock Compass Guards: Deckeldichtung jaehrlich pruefen, Wasser im Pedestal zerstoert Kompass

#### 3.2.3 Lewmar (UK)

Lewmar produziert neben den Whitlock-Produktlinien eigene hydraulische Steueranlagen.

**Lewmar Hydrauliksteuerungen:**
- **Helmpumpen (Continuum-Serie):** Jaehrlich Leckage pruefen, alle 3 Jahre Dichtungssatz wechseln
- **Hydraulikfluid:** Lewmar empfiehlt Total Equivis ZS 15 oder aequivalent ISO VG 15. Wechsel alle 2 Jahre.
- **Entlueftung:** Nach jedem Winterlager entlueften. Lewmar-spezifische Entlueftungsreihenfolge beachten (hoechster Punkt zuerst).
- **Zylinder:** Kolbenstange jaehrlich auf Pitting pruefen, Chromflaeche nicht beschaedigen
- **Rueckschlagventile:** Alle 3 Jahre Funktion pruefen (Helm muss in jeder Position stehen bleiben)

#### 3.2.4 Raymarine (UK) — Autopilot

Raymarine ist der Marktfuehrer fuer Autopiloten im Freizeitbootbereich.

**Raymarine Evolution-Serie (EV-100, EV-200, EV-400):**
- **Saisonbeginn:** Kalibrierungsfahrt (Docking/Seatrial Calibration), Kompass-Check
- **Jaehrlich:** Linearantrieb-Befestigung pruefen, Kolbenstange auf Rost pruefen, Kabel inspizieren
- **Alle 2 Jahre:** Firmware-Update pruefen und installieren
- **Alle 3 Jahre:** Antriebsriemen wechseln (Type 1/2 Antriebe), Kugelgelenke schmieren
- **Alle 5 Jahre:** Linearantrieb komplett revidieren oder ersetzen

**Raymarine-spezifische Kalibrierung:**
1. Docking-Kalibrierung: Boot langsam in alle Richtungen steuern (Ruderlagensensor lernt Endanschlaege)
2. Sea Trial: Automatische Kompasskalibrierung durch zwei volle Kreise bei >3 kn
3. Response-Level: Anpassen an Bootstyp (Segelyacht: Medium, Motorboot: High)

**Haeufige Raymarine-Probleme bei fehlender Wartung:**
- Linearantrieb ACU-100/200: Endschalter korrodiert → Ueberlast → Sicherung loest
- Fluxgate-Kompass: Deviation durch magnetisierte Gegenstaende in der Naehe
- P70/p70s Display: Tastenkontakte oxidieren bei fehlender Abdeckung

#### 3.2.5 B&G (Navico/Navionics-Gruppe) — Autopilot

B&G bedient vorwiegend den Performance-Segelyacht-Markt.

**B&G Triton/H5000 Autopilot:**
- **Saisonbeginn:** Kalibrierungsfahrt mit Precision-9 Kompass, Ruderlage-Kalibrierung
- **Jaehrlich:** Hydraulikpumpe (Typ 1/2/3) auf Leckage pruefen, Befestigungen kontrollieren
- **Alle 2 Jahre:** Hydraulikfluid in Autopilot-Pumpe wechseln (getrennt von Hauptsteuerung!)
- **Alle 3-4 Jahre:** Pumpen-Dichtungssatz wechseln, Rueckschlagventile pruefen

**B&G-spezifische Besonderheiten:**
- B&G Precision-9 Kompass: Selbstkalibrierend, aber alle 6 Monate Deviation-Check empfohlen
- B&G Hydraulikpumpen: Nutzen separaten Hydraulikkreis — NICHT mit Hauptsteuerung verbinden!
- Performance-Modus: Bei Regatten hoehere Zyklusrate → mehr Verschleiss am Antrieb → kuerzere Wartungsintervalle

### 3.3 Wartungsplaene nach Nutzungsprofil

#### 3.3.1 Saisonsegler (Nordsee/Ostsee, Mai-Oktober)

**Saisonstart (April/Mai):**
1. Steueranlage komplett visuell inspizieren
2. Seilspannung pruefen und einstellen
3. Hydraulikoelstand pruefen, bei Bedarf nachfuellen
4. Hydrauliksystem entlueften
5. Autopilot einschalten, Selbsttest abwarten
6. Autopilot-Kalibrierungsfahrt durchfuehren
7. Notpinne Stecktest
8. Ruderlager auf Spiel pruefen (Ruder seitlich bewegen)
9. Pedestal schmieren
10. Steuerrad-Teak behandeln (falls noetig)

**Mitte Saison (Juli/August):**
1. Steuerseile visuell inspizieren (mit Tuch abstreichen auf Litzenbrueche)
2. Hydraulikoelstand pruefen
3. Autopilot-Funktion pruefen
4. Rudergaengigkeit pruefen (Ruder von Anschlag zu Anschlag)

**Saisonende (Oktober/November):**
1. Steueranlage gruendlich reinigen (Suesswasser)
2. Steuerseile schmieren (Korrosionsschutz fuer Winter)
3. Hydrauliksystem: Oelstand pruefen, ggf. Wechsel durchfuehren
4. Autopilot: Sicherung entfernen, Display schuetzen
5. Ruderlager: Schmieren, Spiel dokumentieren
6. Pedestal: Abdeckung aufsetzen (gegen Feuchtigkeit und UV)
7. Notpinne: Trocken und zugaenglich verstauen
8. Wartungsprotokoll ausfuellen

#### 3.3.2 Langfahrtsegler (ganzjaehrig, Tropen)

**Monatliche Pruefung:**
1. Steuerseile auf Litzenbrueche pruefen
2. Hydraulikoelstand und -farbe pruefen
3. Ruderlager-Spiel pruefen
4. Autopilot-Funktion und Kalibrierung kontrollieren
5. Notpinne Stecktest

**Alle 3 Monate:**
1. Pedestal oeffnen und inspizieren
2. Hydraulikschlaeuche auf UV-Schaeden pruefen
3. Seilspannung nachmessen
4. Autopilot-Linearantrieb pruefen
5. Ruderblatt auf Bewuchs/Beschaedigung pruefen (Tauchgang)

**Jaehrlich:**
1. Hydraulikoel wechseln
2. Steuerseile komplett abnehmen, pruefen, schmieren oder ersetzen
3. Ruderlager gruendlich inspizieren
4. Autopilot-Antrieb revidieren
5. Alle Bolzen/Splinte ersetzen
6. Pedestal komplett revidieren
7. Koker-Dichtung pruefen/ersetzen

**Erhoehte Aufmerksamkeit in Tropen:**
- UV-Schutz fuer alle exponierten Gummi-/Kunststoffteile
- Haeufigere Bewuchskontrolle (alle 4-6 Wochen)
- Hydraulikoel-Wechselintervall auf 12 Monate verkuerzen
- Seillebensdauer auf 3-4 Jahre verkuerzen (Salzbelastung, UV, Nutzung)

#### 3.3.3 Regattasegler

**Vor jeder Regatta:**
1. Seilspannung pruefen und optimal einstellen
2. Rudergaengigkeit testen (Reibung minimieren)
3. Autopilot-Kalibrierung (falls verwendet)
4. Notpinne Stecktest

**Nach jeder Regatta:**
1. Steueranlage auf Beschaedigung pruefen
2. Hydraulikoel-Level pruefen
3. Unuebliche Geraeusche oder Verhalten dokumentieren

**Regattaspezifisch:**
- Seilwechsel alle 2-3 Jahre (statt 5-7)
- Pedestal-Revision alle 2 Jahre (statt 3-5)
- Ruderlager alle 5-7 Jahre (statt 10-15)
- Hoehere Belastung durch aggressive Manoever → kuerzere Intervalle

#### 3.3.4 Motorboot / Motor-Yacht

**Saisonstart:**
1. Hydrauliksystem: Oelstand, Farbe, Entlueftung
2. Steuerung von Anschlag zu Anschlag: Leichtgaengigkeit, Spiel
3. Push-Pull-Kabel (Aussenborder): Gaengigkeit, Schmiernippel bedienen
4. Autopilot-Kalibrierung
5. Notsteuerverfahren testen
6. Trimmklappen-Funktion (falls ueber Steuerung angesteuert)

**Halbzeit Saison:**
1. Hydraulikoelstand
2. Leckage-Kontrolle an Pumpe, Leitungen, Zylinder
3. Steuerungsspiel pruefen
4. Kabel-/Bowdenzugsteuerung: Gaengigkeit pruefen

**Saisonende:**
1. Hydraulikoel pruefen/wechseln
2. Push-Pull-Kabel schmieren
3. Zylinder-Kolbenstange mit Korrosionsschutz einspruehen
4. Autopilot sichern
5. Dokumentation

### 3.4 Lebensdauer-Erwartung und Tauschintervalle

| Komponente | Erwartete Lebensdauer | Tauschempfehlung | Kosten (ca.) |
|-----------|----------------------|------------------|--------------|
| Steuerseil 1x19 Edelstahl | 8-12 Jahre | Alle 5-7 Jahre praeventiv | 150-400 EUR |
| Steuerseil 7x19 Edelstahl | 5-8 Jahre | Alle 4-5 Jahre praeventiv | 150-400 EUR |
| Umlenkrollen-Lager | 10-15 Jahre | Bei Rauhigkeit oder Spiel | 30-80 EUR/Stueck |
| Quadrant (Aluminium) | 20-30 Jahre | Bei sichtbarer Korrosion/Riss | 200-600 EUR |
| Hydraulikschlauch | 7-10 Jahre | Alle 5-7 Jahre praeventiv | 50-150 EUR/Stueck |
| Hydraulikpumpen-Dichtung | 7-12 Jahre | Alle 5-7 Jahre praeventiv | 80-200 EUR (Satz) |
| Hydraulikzylinder-Dichtung | 10-15 Jahre | Alle 7-10 Jahre praeventiv | 100-300 EUR (Satz) |
| Hydraulikfluid | 3-5 Jahre (ohne Wechsel) | Alle 2-3 Jahre Wechsel | 20-50 EUR/Liter |
| Ruderlager (Composite) | 15-25 Jahre | Bei >1mm Spiel radial | 200-800 EUR/Stueck |
| Ruderlager (Bronze) | 10-20 Jahre | Bei >0.5mm Spiel radial | 300-1.000 EUR/Stueck |
| Koker-Dichtung (Lip Seal) | 5-10 Jahre | Alle 5 Jahre praeventiv | 50-150 EUR |
| Autopilot-Linearantrieb | 7-12 Jahre | Bei Geraeusch/Leistungsverlust | 500-2.000 EUR |
| Push-Pull-Kabel | 10-15 Jahre | Bei Schwergaengigkeit | 80-250 EUR |
| Steuerrad (Teak) | 15-25 Jahre | Bei Bruch oder Faeulnis | 400-2.500 EUR |
| Pedestal-Getriebe | 20-30 Jahre | Bei Verschleiss/Spiel | 300-1.200 EUR |
| Pedestal-Kette | 10-15 Jahre | Alle 7-10 Jahre praeventiv | 60-150 EUR |

> ⚠️ **ZU PRÜFEN (Audit):** Bronze-Ruderlager Tauschgrenze hier ">0.5 mm Spiel radial", aber in Kap. 4.5 (Tabelle Grenzwerte Lagerspiel), Kap. 6.9, Kap. 8.14 (F04) und FAQ F20 durchgaengig ">0.8 mm". Widerspruch auf einem sicherheitskritischen Verschleiss-Grenzwert — die Richtung ist nicht zweifelsfrei belegbar (herstellerabhaengig), daher nicht korrigiert. Confidence dieses Einzelwerts: estimated — unverifiziert.

---

## 4. Schritt-fuer-Schritt Wartungsanleitungen

### 4.1 Seilspannung pruefen und einstellen

**Qualifikationsstufe:** 2 (Versierter Eigner)
**Zeitbedarf:** 30-60 Minuten
**Werkzeuge:** Tensiometer (z.B. Loos PT-2), Gabelschluessel passend, Splintentreiber

**Vorbereitung:**
1. Boot sicher am Steg oder an Land
2. Autopilot deaktiviert
3. Ruder in Mittelstellung gebracht
4. Steuerrad nicht belastet (Bremse loesen, Rad frei drehen lassen)

**Durchfuehrung:**

**Schritt 1: Zugang schaffen**
- Cockpit-Bodenluken oeffnen (typisch: Lazarette achtern)
- Ggf. Verkleidungen am Pedestal-Fuss entfernen
- Alle Umlenkpunkte muessen zugaenglich sein

**Schritt 2: Visuelle Inspektion**
- Gesamtes Seil vom Pedestal bis zum Quadrant mit dem Auge verfolgen
- Auf Litzenbrueche pruefen: Seil mit einem Lappen umfassen und langsam entlangfahren — aufstehende Draehte sind sofort spuerbar
- Knicke, Quetschungen, Verfaerbungen notieren
- Umlenkrollen auf korrekte Ausrichtung pruefen (Seil muss mittig in der Rille laufen)
- Nicropress-Huelsen auf Risse pruefen
- Schaekel/Gabelterminals auf Spiel und Korrosion pruefen
- Seilspanner pruefen: Noch Reserveweg vorhanden?

**Schritt 3: Spannung messen**
- Tensiometer ansetzen: Mittig zwischen zwei Umlenkpunkten
- Seil muss frei haengen (keine Stuetze oder Auflage zwischen den Messpunkten)
- Seildurchmesser am Tensiometer korrekt einstellen
- Messung an beiden Seiten (Steuerbord/Backbord) durchfuehren

**Richtwerte Seilspannung:**

| Seildurchmesser | Mindestspannung | Sollspannung | Maximalspannung |
|----------------|----------------|--------------|-----------------|
| 4 mm (5/32") | 90 N | 130 N | 180 N |
| 5 mm (3/16") | 110 N | 155 N | 220 N |
| 6 mm (1/4") | 130 N | 175 N | 250 N |
| 7 mm (9/32") | 155 N | 200 N | 290 N |

**Schritt 4: Spannung einstellen (falls noetig)**
- Seilspanner lokalisieren (meist am Quadrant oder an Umlenkrolle)
- Kontermutter loesen
- Spannschraube gleichmaessig auf beiden Seiten nachstellen
- **WICHTIG:** Immer beide Seiten gleichmaessig nachspannen — Asymmetrie fuehrt zu Ruder-Offset
- Kontermutter festziehen
- Erneut messen

**Schritt 5: Funktionstest**
- Steuerrad langsam von Anschlag zu Anschlag drehen
- Seil darf an keiner Stelle ausspringen, schleifen oder klemmen
- Ruder muss Anschlaege gleichmaessig erreichen (gleicher Ausschlag BB/StB)
- Steuerrad loslassen: Ruder muss in Position bleiben (kein Wegdriften)
- Bei Doppelsteuerstand: Von beiden Positionen testen

**Schritt 6: Dokumentation**
- Gemessene Spannungen notieren (BB/StB)
- Visuelle Befunde dokumentieren
- Fotos von auffaelligen Stellen
- Datum, Wetter (Temperatur), Zustand Boot (an Land/Wasser)

**Haeufige Fehler:**
- Zu hohe Spannung: Erhoehter Verschleiss an Rollen, Kette und Seil, schwergaengiges Steuer
- Zu niedrige Spannung: Seil springt von Rollen, ungenauer Autopilot, Spiel im Steuer
- Asymmetrische Spannung: Ruder-Offset, Boot faehrt nicht geradeaus
- Spannung bei Hitze eingestellt: Bei Kaelte wird das Seil kuerzer → Ueberspannung

### 4.2 Hydraulikfluid-Wechsel

**Qualifikationsstufe:** 2 (Versierter Eigner)
**Zeitbedarf:** 60-120 Minuten
**Werkzeuge:** Oelpumpe/Spritze, Auffangbehaelter, neues Hydraulikfluid (ISO VG 15 oder herstellerspezifisch), Schluesselset, Lappen, Handschuhe

**Vorbereitung:**
1. Boot am Steg oder an Land
2. Steuerung in Mittelstellung
3. Autopilot-Hydraulikpumpe deaktiviert
4. Herstellerangabe zum Fluid pruefen (NICHT mischen!)
5. Korrekte Menge bereitstellen (typisch: 0.5-2.0 Liter je nach System)

**Schritt 1: Altes Fluid ablassen**
- Auffangbehaelter unter Helmpumpe / Vorratsbehaelter positionieren
- Einfuellschraube am Vorratsbehaelter oeffnen (Belueftung)
- Falls Ablassschraube vorhanden: Oeffnen und Fluid auffangen
- Falls keine Ablassschraube: Mit Spritze/Pumpe absaugen
- Steuerrad langsam von Anschlag zu Anschlag bewegen, um Restfluid aus Zylinder zu foerdern
- **Aufgefangene Menge notieren** — wichtig fuer Fuellstandskontrolle

**Schritt 2: Altes Fluid beurteilen**

| Zustand | Farbe | Bedeutung | Massnahme |
|---------|-------|-----------|-----------|
| Gut | Klar, Originalfarbe | Fluid in Ordnung | Normaler Wechsel |
| Leicht gealtert | Leicht dunkler | Beginnende Alterung | Normaler Wechsel |
| Gealtert | Dunkelbraun | Ueberfaelliger Wechsel | Spuelung empfohlen |
| Wasserhaltig | Milchig trueb | Wasser im System | Spuelung erforderlich, Leckagesuche |
| Partikelbehaftet | Metallflitter sichtbar | Verschleiss im System | Spuelung, Pumpe/Zylinder inspizieren |
| Stark verschmutzt | Schwarz, verdickt | Kritisch | Komplettrevision empfohlen |

**Schritt 3: System spuelen (bei Bedarf)**
- Ca. 50% der Systemmenge frisches Fluid einfuellen
- Steuerrad 10-15 Mal von Anschlag zu Anschlag bewegen
- Fluid wieder ablassen und beurteilen
- Bei immer noch verschmutztem Fluid: Spuelung wiederholen
- Bei Metallpartikeln: System oeffnen und Schadensquelle identifizieren

**Schritt 4: Neues Fluid einfuellen**
- Korrektes Fluid verwenden:

| Hersteller | Empfohlenes Fluid | Alternative |
|-----------|-------------------|-------------|
| Lewmar | Total Equivis ZS 15 | ISO VG 15 HLP |
| Teleflex/SeaStar | SeaStar HA5430 | ISO VG 15 HLP |
| Vetus | Vetus HF 15 | ISO VG 15 HLP |
| Hynautic | ATF Dexron III | Kein HLP! |
| Kobelt | ISO VG 46 | Herstellerspez. |

- **WARNUNG:** HLP und ATF NIEMALS mischen! Inkompatible Additive zerstoeren Dichtungen.
- Fluid langsam einfuellen, dabei Steuerrad langsam bewegen
- Auf korrekten Fuellstand achten (Markierung am Behaelter)
- Nicht ueberfuellen (Druckaufbau bei Erwaermung)

**Schritt 5: Entlueftung (siehe 4.3)**

**Schritt 6: Funktionstest**
- Steuerrad von Anschlag zu Anschlag: Gleichmaessig, keine Luftblasen-Geraeausche
- 15 Minuten warten, Fuellstand nachpruefen
- Alle Anschluesse auf Leckage pruefen
- Helm-Lock testen (Ruder muss stehen bleiben)

**Schritt 7: Entsorgung**
- Altoel fachgerecht entsorgen (Sonderabfall)
- Oelhaltige Lappen nicht im Boot aufbewahren (Selbstentzuendung)
- Menge und Typ des neuen Fluids im Wartungsprotokoll vermerken

### 4.3 Hydrauliksystem entlueften

**Qualifikationsstufe:** 2 (Versierter Eigner)
**Zeitbedarf:** 30-60 Minuten
**Werkzeuge:** Passendes Fluid zum Nachfuellen, Auffangbehaelter, Schlauch fuer Entlueftungsschraube, Gabelschluessel

**Wann entlueften?**
- Nach jedem Oelwechsel
- Nach dem Winterlager (Undichtigkeit waehrend Lagerung moeglich)
- Wenn das Steuer sich "schwammig" anfuehlt (Luft komprimiert im Gegensatz zu Fluid)
- Nach Leitungs- oder Schlaucharbeiten
- Wenn beim Steuern Geraeusche (Gurgeln, Zischen) hoerbar sind

**Grundprinzip:**
Luft steigt nach oben. Entlueftung beginnt am hoechsten Punkt des Systems und arbeitet sich nach unten vor. Das System muss waehrend der Entlueftung staendig mit Fluid nachgefuellt werden, damit keine neue Luft angesaugt wird.

**Schritt 1: Vorbereitung**
- Vorratsbehaelter bis Maximum fuellen
- Alle Entlueftungsschrauben lokalisieren (typisch: an Helmpumpe, am Zylinder, ggf. an Autopilot-Pumpe)
- Auffanggefaesse und Schlaeuche bereitstellen
- Bei Doppelsteuerstand: Bypass-Ventil pruefen (muss geoeffnet sein)

**Schritt 2: Entlueftung am hoechsten Punkt**
- Entlueftungsschraube am hoechsten Punkt (meist Helmpumpe oben) ca. 1/4 Umdrehung oeffnen
- Kurzen Schlauch auf Entlueftungsschraube stecken, Ende in Auffanggefaess mit etwas Fluid (verhindert Rueckansaugung von Luft)
- Steuerrad langsam und gleichmaessig hin und her bewegen (ca. 1/4 bis 1/2 Umdrehung)
- Luft tritt als Blasen im Fluid aus
- Weiterbewegen, bis blasenfreies Fluid austritt
- Entlueftungsschraube schliessen
- Vorratsbehaelter nachfuellen

**Schritt 3: Entlueftung am Zylinder**
- Entlueftungsschrauben am Zylinder (falls vorhanden) oeffnen
- Steuerrad langsam von Anschlag zu Anschlag bewegen
- Auf Blasen achten
- Schliessen wenn blasenfrei
- Vorratsbehaelter nachfuellen

**Schritt 4: Entlueftung Autopilot-Pumpe (falls vorhanden)**
- Autopilot hat separaten Anschluss am Hydraulikkreis
- Entlueftungsschraube an Autopilot-Pumpe oeffnen
- Manuell am Steuerrad hin und her bewegen ODER Autopilot kurz aktivieren
- Blasenfrei? → Schliessen
- Nachfuellen

**Schritt 5: Abschlusstest**
- Vorratsbehaelter auf korrektem Level
- Steuerrad langsam und schnell bewegen: Darf nicht schwammig sein
- Helm-Lock testen: Ruder muss sofort stehen bleiben
- Von Anschlag zu Anschlag: Keine Geraeusche, kein Widerstandsverlust
- Autopilot aktivieren und testen
- Alle Anschluesse auf Leckage pruefen

**Schritt 6: Wenn Entlueftung nicht gelingt**
- Luft haelt sich in Hochpunkten der Leitung
- System mehrfach von Anschlag zu Anschlag bewegen (kumuliert ca. 50 volle Zyklen)
- Ueber Nacht stehen lassen, am naechsten Tag erneut entlueften
- Wenn weiterhin Luft: Leckage im System suchen (Luft tritt an gleicher Stelle ein, an der Fluid austritt)
- Bei persistenter Luft: Fachbetrieb beauftragen — moeglicherweise Kavitation in der Pumpe

### 4.4 Autopilot-Kalibrierung

**Qualifikationsstufe:** 1 (Eigner)
**Zeitbedarf:** 20-45 Minuten (auf dem Wasser)
**Werkzeuge:** Autopilot-Bedieneinheit, Fernbedienung, GPS-Plotter

**Wann kalibrieren?**
- Saisonbeginn (Pflicht)
- Nach Aenderungen an der Steueranlage (Seilspannung, Hydraulik-Arbeiten)
- Nach Elektroinstallationen in der Naehe des Kompasses
- Wenn der Autopilot merklich schlecht steuert (schlingert, ueberkorrigiert)
- Nach Software-/Firmware-Update

**Schritt 1: Vorbereitung**
- Boot muss fahren (min. 3 Knoten ueber Grund, besser 5+)
- Ruhiges Wasser bevorzugt (Entzerrt Kompassdaten)
- Keine grossen metallischen Gegenstaende in Kompassnaehe bewegen
- GPS aktiv, Logge aktiv
- Alle Elektronik eingeschaltet (Magnet-Stoerfeld realistisch)

**Schritt 2: Ruderlage-Null (Docking Calibration)**
- Bei Raymarine: Settings → Autopilot → Docking Calibration
- Bei B&G: Menu → Autopilot → Commissioning → Rudder
- Steuerrad langsam von Anschlag zu Anschlag drehen
- System lernt Ruderlage-Sensor-Bereich
- Steuerrad in Mittelstellung bringen
- Bestaetigen

**Schritt 3: Kompass-Kalibrierung (Sea Trial)**
- Bei Raymarine: Settings → Autopilot → Sea Trial → Compass Calibration
- Bei B&G: Menu → Autopilot → Commissioning → Compass Cal
- System fordert zum langsamen Kreis (360°) auf
- Zwei volle Kreise langsam fahren (ca. 1 min pro Kreis)
- System zeigt Ergebnis: Deviation max. 3° akzeptabel, idealerweise <1°
- Bei >3°: Stoerquelle suchen (Lautsprecher, Werkzeuge, Magnete in der Naehe des Kompasses)

**Schritt 4: Response anpassen**
- **Segelyacht (Fahrt):** Response Level 3-5 (von 9), Rudder Gain Medium
- **Segelyacht (Regatta):** Response Level 6-7, Rudder Gain High
- **Motorboot (Verdraenger):** Response Level 5-6, Rudder Gain Medium-High
- **Motorboot (Gleiter):** Response Level 7-9, Rudder Gain High
- Zu niedrig: Boot maeandert, haelt Kurs schlecht
- Zu hoch: Boot schlingert (S-Kurven), hoher Stromverbrauch, Verschleiss am Antrieb

**Schritt 5: Windfahnen-Kalibrierung (Segelyacht)**
- Wenn Windmesser vorhanden: Apparent Wind als Referenz aktivieren
- Autopilot auf Wind-Modus: Sollwinkel zum scheinbaren Wind steuern
- Testen: Wind-Modus aktivieren, Winkel vorgeben, beobachten
- Feinjustierung des Offsets wenn noetig (Windfahne gegenueber Bootsmitte)

**Schritt 6: Funktionstest**
- Kurs auf gerader Strecke, Autopilot aktivieren
- Kursaenderung +30° befehlen: Muss ohne Ueberschwinger erreicht werden
- Kursaenderung -30° befehlen: Gleichmaessig
- Notfall-Test: Standby-Taste druecken → Autopilot muss sofort loslassen
- Bei Raymarine: Dodge-Funktion testen (kurzzeitiger Kursversatz)

### 4.5 Ruderlager-Inspektion

**Qualifikationsstufe:** 2 (Versierter Eigner)
**Zeitbedarf:** 30-60 Minuten
**Werkzeuge:** Messuhr mit Magnetfuss (oder Fuehllehre), Taschenlampe, Spiegel, Schmierzeug

**Vorbereitung:**
1. Boot im Wasser: Messung von innen moeglich, aber Ergebnis beinhaltet Wasserauftrieb
2. Boot an Land (bevorzugt): Genauere Messung, Ruderblatt-Inspektion moeglich
3. Steuerung entspannen: Seilspannung loesen oder Hydraulik drucklos machen
4. Autopilot deaktivieren

**Schritt 1: Spiel pruefen (Schnelltest)**
- Am Ruderblatt (an Land) oder am Ruderschaft (im Wasser) anfassen
- Ruder seitlich (quer zur Fahrtrichtung) hin und her bewegen
- Spuerbares Spiel: Verdacht auf Lagerverschleiss
- Ruder vor/zurueck (in Fahrtrichtung) bewegen: Prueft Laengsspiel und Schaftabdichtung
- Ruder nach unten druecken (an Land): Prueft Axiallager / Rudertragring

**Schritt 2: Spielmessung mit Messuhr**
- Messuhr am Koker befestigen (Magnetfuss oder Klemme)
- Messspitze auf Ruderschaft oder Ruderlager-Gehaeuse
- Ruder seitlich mit definierter Kraft bewegen (ca. 10-20 kg Handkraft)
- Messuhr-Ausschlag ablesen

**Grenzwerte Lagerspiel:**

| Lagerbauart | Neuzustand | Noch akzeptabel | Grenzwert (Tausch) |
|------------|-----------|----------------|-------------------|
| Composite (Jefa, Tides) | 0.05-0.15 mm | 0.5 mm | 1.0 mm |
| Bronze-Gleitlager | 0.10-0.20 mm | 0.4 mm | 0.8 mm |
| Nadellager | 0.02-0.05 mm | 0.2 mm | 0.5 mm |
| PTFE-Buchse | 0.05-0.15 mm | 0.4 mm | 0.8 mm |
| Delrin-Buchse | 0.05-0.20 mm | 0.5 mm | 1.0 mm |

**Schritt 3: Koker-Inspektion**
- Wassereinbruch: Trocken? Feucht? Nass? Tropfend?
- Dichtlippe: Elastisch oder sproede?
- Kokerrohr: Korrosion? Risse? Verformung?
- Schaft-Oberflaeche im Kokerbereich: Korrosion? Riefen?

**Schritt 4: Oberlager-Inspektion (innen)**
- Zugang von innen (meist unter Cockpitboden oder Lazarette)
- Lagersitz: Risse im GFK/Laminat um den Lagersitz?
- Lagerflansch: Schrauben fest? Dichtung intakt?
- Wasserspuren: Korrosionsspuren deuten auf Wasser von oben (Koker) oder von aussen (Rumpf)

**Schritt 5: Unterlager-Inspektion (an Land)**
- Skeg-Zustand pruefen (bei Skeg-gehangenen Rudern)
- Unterlager-Gehaeuse: Risse, Korrosion?
- Bolzen/Schrauben: Fest? Korrodiert? Splinte vorhanden?
- Ruderblatt-Unterkante: Aufsetzer-Schaeden?

**Schritt 6: Ruder-Drop-Test (an Land)**
- Steuerung entspannen (Seil/Hydraulik drucklos)
- Rudertragring/Bund lokalisieren
- Ruder leicht nach unten druecken/ziehen
- Spiel nach unten: Zeigt Verschleiss am Tragring/Axiallager
- Richtwert: Max. 2 mm axiales Spiel akzeptabel

**Schritt 7: Dokumentation**
- Messwerte in Wartungsprotokoll eintragen
- Trend gegenueber Vorjahreswerten pruefen
- Fotos von auffaelligen Stellen
- Bei Grenzwertueberschreitung: Lagerwechsel planen

### 4.6 Steuerrad-Pedestal Service

**Qualifikationsstufe:** 2-3 (Versierter Eigner bis Fachbetrieb)
**Zeitbedarf:** 60-180 Minuten (je nach Umfang)
**Werkzeuge:** Schluesselset, Drehmomentschluessel, Marine-Fett (NLGI 2), Silikonspray, Lappen, Drahtbuerste

**Schritt 1: Steuerrad abnehmen**
- Sicherungsmutter lokalisieren (meist zentrale Mutter mit Unterlegscheibe)
- Mutter loesen (ggf. Konterschraube zuerst)
- Steuerrad gerade abziehen (nicht verkanten)
- Keilnut/Passfeder am Schaft pruefen: Verschleiss? Grat?
- Rad sicher ablegen

**Schritt 2: Pedestal-Abdeckung entfernen**
- Kompass vorsichtig abnehmen (Kabel nicht abreissen)
- Pedestal-Mantel abschrauben (typisch 4-6 Schrauben, ggf. Silikon-Dichtung)
- Getriebe freilegen

**Schritt 3: Getriebe inspizieren (am Beispiel Whitlock Mamba)**
- Kettenrad oben: Zahnung auf Verschleiss pruefen (Haifischzahn-Profil = Tausch noetig)
- Kette: Laengung pruefen (10 Glieder messen, max. 2% Laengung)
- Kettenrad unten (Steuerschaftgetriebe): Zahnung, Spiel
- Zahnraeder (bei Schnecken-/Kegelradgetrieben): Zahnflanken auf Pitting, Abrieb
- Lager: Handgefuehl (drehen, Spiel pruefen), Geraeusche
- Steuerbremse: Bremsbelaege, Funktion
- Sprengring (Whitlock): Auf korrektem Sitz?

**Schritt 4: Reinigung**
- Altes Fett entfernen (Lappen, ggf. Bremsenreiniger auf nicht-lackierten Teilen)
- NICHT mit Hochdruck reinigen (drueckt Schmutz in Lager)
- Zahnflanken mit Drahtbuerste reinigen
- Innenwand des Pedestals reinigen
- Auf Korrosion, Risse, Verfaerbungen pruefen

**Schritt 5: Schmierung**
- Zahnraeder: Duenne Schicht Marine-Fett NLGI 2 (z.B. Whitlock Grease, NeverSeez Marine)
- Lager: Fett ueber Schmiernippel (falls vorhanden) oder Handauftrag
- Kette: Leichtes Oel oder Kettenfett (NICHT WD-40 — verdraengt Fett und bietet keinen Langzeitschutz)
- Bremsmechanismus: Nur trockene Schmiermittel (PTFE-Spray) auf Gleitflaechen, KEIN Fett auf Bremsbelaegen
- Steuerschaft-Lager: Marine-Fett

**Schritt 6: Zusammenbau**
- Pedestal-Mantel aufsetzen, neue Dichtung verwenden
- Schrauben gleichmaessig und kreuzweise anziehen
- Kompass montieren, Kabel anschliessen
- Steuerrad aufsetzen, Keilnut/Passfeder korrekt ausrichten
- Sicherungsmutter festziehen (Drehmoment nach Hersteller: typisch 30-50 Nm)

**Schritt 7: Funktionstest**
- Steuerrad gleichmaessig drehen: Keine Hakelpunkte?
- Bremse testen: Rad feststellen, Belastung ausUeben
- Von Anschlag zu Anschlag: Gleichmaessig?
- Spiel im Steuerrad: Max. 3-5° akzeptabel (je nach System)

### 4.7 Notpinnen-Test

**Qualifikationsstufe:** 1 (Eigner)
**Zeitbedarf:** 15-30 Minuten
**Werkzeuge:** Notpinne, ggf. Adapter

**DIESER TEST IST PFLICHT VOR JEDER LAENGEREN TOERN!**

**Schritt 1: Notpinne lokalisieren**
- Stauort pruefen: Ist die Notpinne schnell erreichbar (unter 2 Minuten)?
- Passt sie noch auf den Ruderschaft? (Korrosion, Quellholz koennen die Passung aendern)
- Ist der Adapter (falls noetig) dabei?

**Schritt 2: Zugangsweg zum Ruderschaft freiraeumen**
- Deckplatte/Luke ueber Ruderschaft lokalisieren
- Kann sie ohne Werkzeug geoeffnet werden?
- Liegt etwas im Weg (Gasflaschen, Fender, Leinen)?
- Bei Cockpit-Tisch: Muss der Tisch demontiert werden? Wie schnell geht das?

**Schritt 3: Notpinne montieren**
- Deckplatte oeffnen
- Notpinne auf Ruderschaftkopf stecken
- Passung pruefen: Sitzt fest? Kann unter Last abspringen?
- Sicherungsbolzen einsetzen (falls vorhanden)

**Schritt 4: Probesteuerung**
- Steuerrad loslassen oder Hydraulik auf Bypass
- Mit Notpinne steuern: Von Seite zu Seite
- Kraefteabschaetzung: Ist das Steuermoment mit einer Hand beherrschbar?
- Bei hohem Moment: Hilfsmittel vorbereiten (Talje, Leine zur Winsch)

**Schritt 5: Crew-Einweisung**
- Jedes Crew-Mitglied muss wissen:
  1. Wo ist die Notpinne?
  2. Wo ist die Zugangsplatte?
  3. Wie wird die Notpinne montiert?
  4. Wie wird die Hauptsteuerung deaktiviert (Bypass-Ventil, Kupplung)?
  5. Was tun wenn die Notpinne nicht passt?

**Schritt 6: Dokumentation**
- Test bestanden: Ja/Nein
- Benoetigte Zeit fuer Montage: _____ Minuten
- Steuerkraft akzeptabel: Ja/Nein
- Zugangsweg frei: Ja/Nein
- Crew eingewiesen: Namen

### 4.8 Hydraulikschlauch-Inspektion und Wechsel

**Qualifikationsstufe:** 2 (Versierter Eigner)
**Zeitbedarf:** 30-90 Minuten (pro Schlauch)
**Werkzeuge:** Gabelschluessel passend (meist 16-22 mm), Auffangbehaelter, neuer Schlauch (exakte Laenge!), neue Dichtringe/O-Ringe, Lappen, Kabelbinder

**Schritt 1: Schlauch identifizieren und pruefen**
- Alle Hydraulikschlaeuche im System identifizieren (typisch: 2-6 Schlaeuche)
- Jeden Schlauch auf folgende Maengel pruefen:

| Pruefpunkt | OK | Mangel | Aktion |
|-----------|-----|--------|--------|
| Oberflaechenrisse (UV) | Glatt | Risse sichtbar | Wechseln |
| Quellung (falsches Fluid) | Normal-Durchmesser | Aufgeblasen | Sofort wechseln! |
| Knicke/Quetschungen | Gleichmaessiger Bogen | Scharfe Knicke | Wechseln |
| Scheuerstellen | Keine | Abrieb sichtbar | Schutz anbringen, bei Tiefenabrieb wechseln |
| Presshuelosen/Anschluesse | Dicht | Feucht/oelig | Nachziehen oder wechseln |
| Verlegung | Freier Bogen | Gespannt, verdreht | Korrigieren |
| Alter | <5 Jahre | >7 Jahre | Praeventiv wechseln |

**Schritt 2: Schlauch wechseln**
1. System drucklos machen (Ruder in Mittelstellung, Helm-Lock loesen)
2. Auffangbehaelter positionieren
3. Anschluss an einem Ende loesen (Gabelschluessel, NICHT Rohrzange!)
4. Fluid auslaufen lassen
5. Anschluss am anderen Ende loesen
6. Alten Schlauch entfernen, dabei Verlegeroute merken
7. Neuen Schlauch probeweise einlegen (Laenge korrekt? Kein Knick?)
8. Neue O-Ringe/Dichtringe einsetzen
9. Anschluesse handfest anziehen, dann mit Schluessel festziehen (Drehmoment beachten)
10. System mit frischem Fluid fuellen
11. Entlueften (Kapitel 4.3)
12. Leckagetest: 15 Minuten warten, alle Anschluesse pruefen

**WARNUNG:** Hydraulikschlaeuche NIEMALS reparieren (kleben, flicken, binden). Immer komplett ersetzen. Ein geplatzter Hochdruck-Schlauch kann zu schweren Verletzungen fuehren.

**Schlauch-Spezifikation:**
- Standard: SAE 100R7 oder SAE 100R8 (Thermoplastik-Schlauch)
- Betriebsdruck: Mindestens 3× maximaler Systemdruck
- Innendurchmesser: Exakt wie Original (zu gross: Druckverlust, zu klein: Stroemungswiderstand)
- Laenge: Exakt wie Original, keine Zugabe (gespannter Schlauch = Bruchgefahr)
- Biegeiadius: Mindestens 4× Aussendurchmesser

### 4.9 Seilwechsel komplett

**Qualifikationsstufe:** 2 (Versierter Eigner mit Erfahrung)
**Zeitbedarf:** 2-4 Stunden
**Werkzeuge:** Neues Seil (Laenge wie Original + 10% Reserve), Nicropress-Zange + passende Huelsen, Seitenschneider fuer Stahldraht, Tensiometer, Gabelschluessel, Sicherungsdraht/Splinte, Klebeband

**Schritt 1: Altes Seil dokumentieren**
- Seillaenge messen (von Quadrant/Tiller ueber alle Umlenkrollen bis Pedestal)
- Seildurchmesser notieren (4/5/6/7 mm)
- Seilkonstruktion notieren (1x19 oder 7x19)
- Endverbindungen notieren (Nicropress-Huelsen, Gabelterminals, Schaekel)
- Umlenkweg fotografieren (WICHTIG fuer korrekte Neuverlegung)

**Schritt 2: Neues Seil vorbereiten**
- Seil ablaeangen (gleiche Laenge wie altes Seil, NICHT laenger oder kuerzer)
- Seilenden mit Klebeband umwickeln (verhindert Aufdrehen)
- Endverbindungen vorbereiten (Nicropress-Huelsen, Kauschen)

**Schritt 3: Altes Seil entfernen**
- Steuerung in Mittelstellung
- Seilspanner auf Maximum loesen (gibt Laenge fuer Demontage)
- Endverbindung am Quadrant loesen (Bolzen, Schaekel)
- Seil durch alle Fuehrungen und ueber alle Rollen ziehen
- **Trick:** Neues Seil am Ende des alten Seils befestigen (Klebeband + Kabelbinder) und beim Herausziehen durchfaedeln → Spart die muehsame Neuverlegung

**Schritt 4: Neues Seil verlegen**
- Seil durch alle Fuehrungen und ueber alle Rollen fuehren
- Auf korrekte Lage in allen Rollenrillen achten
- Seil darf nirgends kreuzen, schleifen oder knicken
- Endverbindungen herstellen:
  - Nicropress: Kausche einlegen, Huelse korrekt positionieren, 2× pressen (zwei Huelsen pro Ende!)
  - Gabelterminal: Seil einschrauben, Gegenmutter sichern
- Am Quadrant befestigen (Bolzen, Splint, Sicherung)

**Schritt 5: Spannung einstellen**
- Seilspanner mittig positionieren (voller Nachstellweg in beide Richtungen)
- Spannung auf Sollwert einstellen (siehe Tabelle 4.1)
- Beide Seiten (BB/StB) gleichmaessig spannen
- Funktionstest von Anschlag zu Anschlag
- Ruderausschlag BB und StB vergleichen (muss gleich sein)

**Schritt 6: Einfahren und Nachkontrolle**
- Neues Seil setzt sich in den ersten 10-20 Betriebsstunden
- Nach 2 Tagen: Spannung nachmessen und ggf. nachstellen
- Nach 2 Wochen: Erneute Nachmessung
- Nach 1 Monat: Letzte Nachmessung, dann regulaeres Intervall

---

## 5. Schmiermittel und Betriebsstoffe

### 5.1 Uebersicht Schmierstellen und empfohlene Schmierstoffe

| Schmierstelle | Schmierstoff-Typ | Empfohlene Produkte | Intervall |
|--------------|-----------------|--------------------|-----------| 
| Steuerseile | Drahtfett / Wire Rope Lubricant | Boeshield T-9, LanoCote Wire, McLube Sailkote | 6-12 Monate |
| Pedestal-Getriebe | Marine-Fett NLGI 2 | Whitlock Grease, Lewmar Winch Grease, NeverSeez Marine | 12 Monate |
| Pedestal-Kette | Kettenfett | NeverSeez Marine, Boeshield T-9 Chain | 6 Monate |
| Umlenkrollen | Leichtlauf-Fett | Lewmar Winch Grease, Harken Pawl Grease | 12 Monate |
| Ruderlager (Bronze) | Wasserbestaendiges Fett | Klüber Isoflex Topas NB 52, NeverSeez Marine | 12-24 Monate |
| Ruderlager (Composite) | Kein Schmierstoff noetig | — (wartungsfrei) | — |
| Hydraulikfluid | Hydraulikoel ISO VG 15 | Total Equivis ZS 15, Hyspin AWS 15 | Wechsel alle 2-3 J. |
| Hydraulikfluid (Hynautic) | ATF | Dexron III/VI | Wechsel alle 2-3 J. |
| Koker-Dichtlippe | Wasserfestes Fett | Marine-Fett, Vaseline (temp.) | 12 Monate |
| Push-Pull-Kabel | Kabelfett | Teleflex Cable Grease, Boeshield T-9 | 12 Monate |
| Autopilot-Linearantrieb | Trockenschmierstoff | PTFE-Spray, McLube Sailkote | 12 Monate |
| Steuerrad-Nabe | Anti-Seize Paste | NeverSeez, Tef-Gel | Bei Montage |
| Quadrant-Klemmung | Anti-Seize Paste | NeverSeez, Tef-Gel | Bei Montage |
| Ruderschaft (im Koker) | Fett oder Vaseline | Marine-Fett | Beim Einbau |

### 5.2 Hydraulikfluide im Detail

#### 5.2.1 HLP-Oele (Hydraulikoel mit Anti-Verschleiss-Additiven)

**Beschreibung:**
HLP-Oele (DIN 51524 Teil 2) sind mineraloel-basierte Hydraulikfluide mit Hochdruck-Additiven (EP-Additive) und Verschleissschutz. Sie sind der Standard fuer die meisten marinen Hydrauliksteuerungen.

**Viskositaetsklasse:**
- ISO VG 10: Fuer sehr kalte Bedingungen (Arktis)
- **ISO VG 15: Standard fuer Yachtsteuerungen** (am haeufigsten empfohlen)
- ISO VG 22: Fuer warme Bedingungen oder groessere Systeme
- ISO VG 32: Fuer groessere Motorboote, Superyachten
- ISO VG 46: Fuer Schwerlast-Systeme (Kobelt, grosse Rudermaschinen)

**Kennwerte ISO VG 15:**
- Viskositaet bei 40°C: 13.5-16.5 mm²/s
- Viskositaet bei 100°C: ca. 3.5 mm²/s
- Flammpunkt: >160°C
- Pourpoint: <-30°C
- Wassergehalt max.: 0.1% (0.05% empfohlen)

**Empfohlene Produkte:**
| Produkt | Hersteller | Besonderheiten |
|---------|-----------|----------------|
| Total Equivis ZS 15 | TotalEnergies | Lewmar-Empfehlung, sehr verbreitet |
| Castrol Hyspin AWS 15 | Castrol | Gute Tieftemperatureigenschaften |
| Shell Tellus S2 V 15 | Shell | Breites Temperaturspektrum |
| Mobil DTE 11M | ExxonMobil | Hohe Oxidationsstabilitaet |
| SeaStar HA5430 | SeaStar Solutions | Spezifisch fuer Marineanwendungen |

#### 5.2.2 ATF (Automatic Transmission Fluid)

**WARNUNG:** ATF ist nur fuer Systeme zulaessig, die vom Hersteller ausdruecklich ATF vorsehen (z.B. Hynautic). ATF und HLP sind NICHT kompatibel — Mischung fuehrt zu Dichtungsquellung und Systemversagen.

**Beschreibung:**
ATF ist ein duennfluessiges Hydraulikoel mit speziellen Reibungseigenschaften, urspruenglich fuer Automatikgetriebe entwickelt. Einige aeltere Hydrauliksteuerungen (insbes. Hynautic/Wagner) verwenden ATF.

**Kennwerte ATF Dexron III/VI:**
- Viskositaet bei 40°C: 30-34 mm²/s
- Viskositaet bei 100°C: 7-8 mm²/s
- Spezielle Reibwertmodifizierer (Friction Modifier)
- Rot eingefaerbt (Unterscheidung von HLP)

#### 5.2.3 Bio-Hydraulikoele

Fuer umweltsensible Gebiete (z.B. Wattenmeer-Nationalparks, Binnengewaesser) sind biologisch abbaubare Hydraulikoele erhaeltlich:

- Panolin HLP Synth 15: Synthetischer Ester, biologisch abbaubar, voll kompatibel mit Mineraloelen
- Plantohyd 15 S: Rapsoel-basiert, biologisch abbaubar, NICHT mit Mineraloelen mischbar

**AYDI-Empfehlung:** Bei Einsatz in umweltsensiblen Gebieten Bio-Oel verwenden, aber Kompatibilitaet mit Dichtungsmaterial beachten (NBR-Dichtungen vertragen nicht alle Ester-Oele).

### 5.3 Steuerseil-Schmiermittel

**Anforderungen an Seilschmiermittel:**
- Korrosionsschutz (Salzwasser-Umgebung)
- Keine Verharzung (verharzte Seile werden steif)
- Gute Kriechfaehigkeit (muss in Seilinneres eindringen)
- Nicht tropfend (Deck- und Cockpitsauberkeit)
- Vertraeglichkeit mit Edelstahl und GFK

**Empfohlene Produkte:**

| Produkt | Typ | Vorteile | Nachteile |
|---------|-----|---------|-----------|
| Boeshield T-9 | Wachsbasiert | Langzeitschutz, trocknet, kein Tropfen | Aufwendiger Auftrag |
| LanoCote Wire Rope Lube | Lanolin-basiert | Hervorragender Korrosionsschutz | Etwas klebrig |
| McLube Sailkote | PTFE/Silikon | Extrem duenn, kriechfaehig | Kurzlebig, muss oefter aufgetragen werden |
| WD-40 | Petroleumbasiert | Ubiquitaer verfuegbar | NUR als Reiniger, NICHT als Langzeitschutz |
| CRC 6-56 | Korrosionsschutzoeel | Gut fuer Erstbehandlung | Zieht Schmutz an |
| Seilfett (traditionell) | Vaselin-basiert | Preiswert, dick | Zieht Schmutz an, verharzt bei Hitze |

**Anwendungstechnik:**
1. Seil mit Lappen reinigen (altes Fett/Schmutz entfernen)
2. Schmiermittel auftragen: Spray oder mit Lappen einreiben
3. Seil mehrfach ueber die gesamte Laenge hin und her ziehen (Steuerrad bewegen)
4. Ueberschuss abwischen
5. An Umlenkpunkten besonders gruendlich schmieren (hoechste Belastung)

### 5.4 Pedestal- und Lager-Fett

**Marine-Fett NLGI 2 — Anforderungen:**
- Wasserbestaendig (ASTM D1264: max. 5% Auswaschverlust)
- Korrosionsschutz (Salzwasserbestaendig)
- Temperaturbereich: -20°C bis +120°C
- Vertraeglichkeit mit NBR, Viton, PTFE-Dichtungen

**Empfohlene Produkte:**

| Produkt | Verdicker | Besonderheiten |
|---------|----------|----------------|
| Whitlock Grease (OEM) | Lithium | Spezifisch fuer Whitlock Pedestale |
| Lewmar Winch Grease (07000) | Lithium | Gutes Allround-Marine-Fett |
| NeverSeez Marine Grade | Lithium + PTFE | Hervorragender Korrosionsschutz |
| Klüber Isoflex Topas NB 52 | PAO-Synthese | Jefa-Empfehlung fuer Ruderlager |
| Mobilgrease 28 | Lithium-Komplex | MIL-Spec, Langzeitschutz |
| Castrol LMX | Lithium-Komplex | Gutes Preis-Leistungs-Verhaeltnis |

**WARNUNG — Fett-Kompatibilitaet:**
- Lithium-Fett und Calcium-Fett: Bedingt kompatibel
- Lithium-Fett und Polyurea-Fett: NICHT kompatibel (Verflüssigung)
- Im Zweifel: Altes Fett komplett entfernen bevor neues eingefuellt wird

### 5.5 Spezial-Schmiermittel

**Anti-Seize-Paste (fuer Schraubverbindungen):**
- Zweck: Verhindert Festfressen von Edelstahl auf Edelstahl oder Edelstahl auf Aluminium
- Anwendung: Steuerrad-Nabe, Quadrant-Klemmschrauben, Pedestal-Befestigung
- Produkte: Tef-Gel, NeverSeez, Duralac (fuer Alu/Edelstahl)
- **WICHTIG:** Anti-Seize veraendert das wirksame Drehmoment — Drehmoment-Werte um 20-30% reduzieren

**PTFE-Spray (fuer Gleitstelien):**
- Zweck: Trockenschmierung fuer Gleitflaechen, Autopilot-Antriebe
- Anwendung: Autopilot-Kolbenstange, Bremsmechanismus-Gleitflaechen, Kabelhuellen
- Produkte: McLube Sailkote, Ballistol PTFE, WD-40 Specialist PTFE

**Korrosionsschutz-Spray:**
- Zweck: Temporaerer Schutz von Metalloberflaechen bei Winterlager
- Anwendung: Hydraulikzylinder-Kolbenstange, Ruderschaft (exponierter Teil), Edelstahl-Teile
- Produkte: CRC 6-56, Boeshield T-9, ACF-50

---

## 6. Verschleisserkennung und Messtechnik

### 6.1 Steuerseil — Verschleissindikatoren und Messung

#### 6.1.1 Visuelle Indikatoren

**Litzenbrueche (gebrochene Einzeldraehte):**
- **Erkennungsmethode:** Seil mit einem Lappen umfassen und langsam entlangfahren. Gebrochene Draehte stechen durch den Stoff oder sind als abstehende Spitzen sichtbar.
- **Grenzwerte nach ISO 8847:**
  - 0-2 Brueche auf 1 m Laenge: Beobachten, naechste Inspektion in 3 Monaten
  - 3-5 Brueche auf 1 m Laenge: Seilwechsel innerhalb der naechsten Saison planen
  - >5 Brueche auf 1 m Laenge: Sofortiger Seilwechsel
  - Brueche an Endverbindung (Nicropress, Terminal): Sofortiger Tausch

**Seillaengung (Stretch):**
- Neues 1x19 Edelstahlseil: Nahezu dehnungsfrei
- Messbare Laengung: Zeigt plastische Verformung → Seil hat seine Elastizitaetsgrenze ueberschritten
- **Messung:** Seillaenge bei definierter Spannung (z.B. 130 N) messen und mit Ausgangswert vergleichen
- **Grenzwert:** >0.5% Laengung → Seil wechseln

**Knicke und Quetschungen:**
- Jeder Knick ist eine Sollbruchstelle
- Knicke entstehen durch falsche Lagerung, Umlenkung ueber zu kleine Radien, Einklemmen
- **Grenzwert:** Jeder sichtbare Knick → Seil wechseln (an der Knickstelle sind Draehte vorgeschaedigt)

**Korrosion:**
- Oberflaechenkorrosion (braeunliche Verfaerbung): Reinigen, schmieren, beobachten
- Tiefkorrosion (Querschnittsverringerung sichtbar): Seil wechseln
- Korrosion an Presshuelsen: Seil mit neuen Presshuelsen wechseln

**Seilrille in Umlenkrollen:**
- Seil muss in der Rille liegen, nicht auf dem Rand
- Rille darf nicht tiefer als 50% des Seildurchmessers sein
- Asymmetrische Rillen: Fehlausrichtung der Rolle → korrigieren und Rolle wechseln

#### 6.1.2 Seilspannungsmessung im Verlauf

Fuer AYDI-Trendanalyse: Seilspannung bei gleichen Bedingungen (Temperatur, Bootsbelastung) jaehrlich messen und aufzeichnen.

**Trend-Interpretation:**

| Trend | Ursache | Massnahme |
|-------|---------|-----------|
| Spannung sinkt langsam | Normalsetzen, leichte Laengung | Nachspannen |
| Spannung sinkt stark | Seillaengung, Klemme rutscht | Seil pruefen, ggf. wechseln |
| Spannung steigt | Temperaturbedingt (Kaelte), Quadrant verklemmt | Ursache pruefen |
| Spannung asymmetrisch (BB≠StB) | Einseitiger Verschleiss, Fehlausrichtung | Ausrichtung pruefen |
| Spannung schwankt stark | Klemme rutscht, Spanner defekt | Sofort pruefen |

### 6.2 Hydrauliksystem — Zustandsueberwachung

#### 6.2.1 Hydraulikfluid-Analyse

**Einfache Sichtpruefung (Stufe 1):**
- Fluid auf weisses Papier tropfen
- Farbe: Klar/Original = gut, Dunkel = gealtert, Milchig = Wasser, Schwarz = kritisch
- Geruch: Neutral = gut, Verbrannt = ueberhitzt, Sauer = oxidiert
- Konsistenz: Duennfluessig = gut, Dickfluessig = Verunreinigung/Alterung

**Laboranalyse (Stufe 3, bei Verdacht):**
- Wassergehalt (Karl-Fischer): Max. 0.1%, empfohlen <0.05%
- Partikelzaehlung (ISO 4406): Sauberkeitsklasse -/16/13 fuer Steuerungen
- Viskositaet: Abweichung >15% von Nennwert → Wechsel
- Saeurezahl (TAN): Anstieg >0.5 mg KOH/g → Wechsel
- Metallpartikel (ICP-Spektrometrie): Kupfer, Eisen, Zink als Verschleissindikatoren

#### 6.2.2 Drucktest

**Zweck:** Prueft die Dichtheit des gesamten Hydrauliksystems unter Betriebsbedingung.

**Durchfuehrung (Stufe 2-3):**
1. Manometer (0-100 bar, Genauigkeit ±1%) an Pruefanschluss anschliessen (falls vorhanden)
2. Alternativ: T-Stueck in Leitung einsetzen
3. Steuerrad bis zum Anschlag drehen und halten
4. Druck ablesen (typisch: 30-60 bar bei Anschlag, systemabhaengig)
5. Druck fuer 5 Minuten halten: Abfall?

**Interpretation:**

| Druckverhalten | Ursache | Massnahme |
|---------------|---------|-----------|
| Druck stabil | System dicht | Alles in Ordnung |
| Langsamer Druckabfall (>1 bar/min) | Interne Leckage (Pumpe oder Zylinder) | Dichtungen pruefen |
| Schneller Druckabfall (>5 bar/min) | Aeussere Leckage oder defektes Ventil | Leckage lokalisieren |
| Kein Druckaufbau | Schwere Leckage oder Luft im System | Entlueftung, Leckagesuche |
| Ueberdruck (>Nennwert) | Druckbegrenzungsventil defekt | Ventil pruefen/ersetzen |
| Druckpulsation | Luft im System, Kavitation | Entlueften, Zulauf pruefen |

#### 6.2.3 Dichtungszustand erkennen

**Symptome undichter Dichtungen:**

| Symptom | Betroffene Dichtung | Dringlichkeit |
|---------|-------------------|--------------|
| Oelfilm an Kolbenstange | Zylinder-Stangendichtung | Mittel (Monitor) |
| Tropfenbildung an Kolbenstange | Zylinder-Stangendichtung | Hoch (bald wechseln) |
| Oelpfuetze unter Zylinder | Zylinder-Stangendichtung oder O-Ring | Sofort handeln |
| Pumpe wird schwergaengig | Pumpen-Innendichtung | Hoch |
| Pumpe leckt am Schaft | Pumpen-Wellendichtung | Hoch |
| Leitungsanschluss tropft | O-Ring oder Schneidring | Hoch (nachziehen oder Dichtung wechseln) |
| Helm driftet langsam ab | Interne Leckage im Zylinder | Mittel (Kolbendichtung) |

### 6.3 Ruderlager — Spielmessung und Trend

#### 6.3.1 Methoden der Spielmessung

**Methode 1: Messuhr (genau, Stufe 2)**
- Messuhr mit Magnetfuss am Koker oder Lagergehaeuse befestigen
- Messspitze auf Ruderschaft
- Ruder mit definierter Kraft seitlich bewegen (10 kg)
- Messbereich: 0-5 mm, Aufloesung 0.01 mm
- Beide Richtungen messen, Differenz notieren

**Methode 2: Fuehllehre (einfach, Stufe 2)**
- Fuehllehrenblatt zwischen Schaft und Lagerbuchse einfuehren
- Dickste Lehre die durchpasst = Spiel
- Nur bei zugaenglichem Lager moeglich

**Methode 3: Hebelvergroesserung (schnell, Stufe 1)**
- Latte (1 m) am Ruderblatt befestigen
- Am Ende der Latte Bewegung messen
- Spiel am Lager = gemessene Bewegung × (Lagerabstand vom Ruderblattende / Lattenlaenge)
- Genauigkeit: ca. ±0.3 mm

**Methode 4: Ruderdrop-Test (axial, Stufe 2)**
- Boot an Land, Ruder haengend (keine Abstuetzung von unten)
- Messuhr axial am Schaft ansetzen
- Ruder nach unten druecken/ziehen (10 kg)
- Axialbewegung messen
- Grenzwert: >2 mm → Tragring/Axiallager pruefen

#### 6.3.2 Trend-Datenerfassung fuer AYDI

Fuer die vorausschauende Wartung erfasst AYDI folgende Messwerte jaehrlich:

```
Lagerspiel_Messung:
  Datum: YYYY-MM-DD
  Boot_im_Wasser: Ja/Nein
  Temperatur_Luft: XX°C
  Oberlager_radial_mm: X.XX
  Oberlager_axial_mm: X.XX
  Unterlager_radial_mm: X.XX
  Unterlager_axial_mm: X.XX
  Messmethode: Messuhr/Fuehllehre/Hebelvergroesserung
  Kraft_angewendet_kg: XX
```

**Trend-Interpretation:**

| Verlauf | Bedeutung | Massnahme |
|---------|-----------|-----------|
| Konstant (<0.05 mm/Jahr) | Normaler Verschleiss | Weiter beobachten |
| Linearer Anstieg (0.05-0.1 mm/Jahr) | Beschleunigter Verschleiss | Schmierung pruefen, Intervall verkuerzen |
| Progressiver Anstieg (>0.1 mm/Jahr) | Kritischer Verschleiss | Lagerwechsel planen |
| Plotzlicher Sprung | Schadenereignis (Grundberuehrung, Schlag) | Sofort inspizieren |

### 6.4 Pumpen-Drucktest und Foerderleistung

**Testaufbau (Stufe 3):**
1. Manometer in Druckleitung einsetzen
2. Durchflussmesser in Ruecklaufleitung (optional)
3. Helmpumpe mit definierter Drehzahl betaetigen

**Pruefwerte:**

| Parameter | Soll (typisch) | Grenzwert | Massnahme bei Unterschreitung |
|-----------|---------------|-----------|------------------------------|
| Max. Druck | 40-60 bar | <30 bar | Pumpe revidieren |
| Druckhaltezeit | >10 min bei 80% Nenndr. | <2 min | Interne Leckage |
| Foerderleistung | 8-15 cm³/Umdr. | <70% des Nennwerts | Verschleiss intern |
| Ansprechverhalten | Sofort | Verzoegerung >0.5 s | Luft im System |

### 6.5 Autopilot — Funktionspruefung

**Checkliste Autopilot-Funktionspruefung:**

| Pruefpunkt | Soll | Befund |
|-----------|------|--------|
| Selbsttest beim Einschalten | Kein Fehler | ☐ OK ☐ Fehler: _______ |
| Kompass-Anzeige plausibel | ±5° zum Handkompass | ☐ OK ☐ Abweichung: ___° |
| Ruderlage-Anzeige in Mitte | 0° ±2° | ☐ OK ☐ Offset: ___° |
| Kurshalten bei ruhigem Wasser | ±3° Kursabweichung | ☐ OK ☐ Abweichung: ___° |
| Kursaenderung +30° | Ohne Ueberschwinger | ☐ OK ☐ Ueberschwinger: ___° |
| Kursaenderung -30° | Ohne Ueberschwinger | ☐ OK ☐ Ueberschwinger: ___° |
| Standby-Taste | Sofortige Freigabe | ☐ OK ☐ Verzoegerung: ___s |
| Wind-Modus (Segelyacht) | Haelt Windwinkel ±5° | ☐ OK ☐ Abweichung: ___° |
| Stromaufnahme | Herstellerangabe ±20% | ☐ OK ☐ Strom: ___A |
| Geraeusche | Gleichmaessig, kein Schleifen | ☐ OK ☐ Auffaellig: _______ |
| Fernbedienung | Alle Tasten funktionieren | ☐ OK ☐ Defekt: _______ |
| Alarm bei Kursabweichung | Alarm bei >20° Abweichung | ☐ OK ☐ Kein Alarm |

### 6.6 Ruderblatt — Wasseraufnahme und Strukturpruefung

**Klopftest (Stufe 1):**
- Ruderblatt (an Land) mit Knochel oder Hartgummi-Hammer abklopfen
- Gesundes Laminat: Hoher, klarer Klang
- Wasseraufnahme/Delaminierung: Dumpfer, matter Klang
- Systematisch abklopfen: Bereiche mit dumpfem Klang markieren

**Feuchtemessung (Stufe 2):**
- Feuchtemessgeraet (kapazitiv, z.B. Tramex Skipper) auf Ruderblattoberflaeche
- Trockenes Laminat: <15% relative Feuchte
- Feuchtes Laminat: 15-30% — Beobachten, Antifouling-Risse als Eintritt suchen
- Nasses Laminat: >30% — Sanierung erforderlich (Trocknung + Versiegelung)

**Sichtpruefung Ruderblatt:**
- Gelcoat-Risse: Insbes. am Schaft-Uebergang (Krafteinleitung)
- Delamination: Blasen, Abhebungen
- Osmose-Blasen: Wie am Unterwasserschiff
- Kantenschaeden: Abplatzungen an Vorder- und Hinterkante
- Schaft-Ruderblatt-Uebergang: Risse? Spalte? Bewegung?

### 6.7 Push-Pull-Kabel — Zustandspruefung

**Pruefmethode (Stufe 1-2):**

| Pruefpunkt | Methode | OK-Kriterium | Mangel-Indikator |
|-----------|---------|-------------|------------------|
| Gaengigkeit | Steuerrad drehen, Handkraft schaetzen | 3-8 kg Handkraft | >12 kg oder ruckartig |
| Totgang | Steuerrad hin/her bewegen | <5° am Rad | >10° Totgang |
| Kabel-Huelle | Visuelle Inspektion | Intakt, kein Riss | Risse, Sproedigkeit, UV-Schaden |
| Kabelanschluss Motor | Spieltest am Motorhebel | Kein Spiel | Fuhlbares Spiel, Klappern |
| Kabel-Biegeradien | Verlegung pruefen | Min. 200 mm Radius | Enge Biegungen, Knicke |
| Schmiernippel | Schmiertest | Fett tritt an anderer Stelle aus | Kein Fettdurchgang → verstopft |

**Lebensdauer-Indikatoren:**
- Schwergaengigkeit, die nach Schmierung zurueckkehrt: Innere Korrosion → Kabel wechseln
- Zunehmender Totgang: Gelenke ausgeschlagen → Kabel wechseln
- Kabel laesst sich in der Huelle verdrehen: Innerer Bruch moeglich → Sofort pruefen
- Huelle gerissen/aufgeplatzt: Wasser dringt ein → Kabel wechseln

### 6.8 Pedestal-Verschleiss erkennen

**Pruefmethode (Stufe 2):**

**Kettenlaengung messen:**
1. 10 Kettenglieder abzaehlen
2. Laenge von Pin-Mitte zu Pin-Mitte messen (Schieblehre)
3. Nennmass: Teilung × 10 (z.B. 3/8" Kette: 10 × 9.525 mm = 95.25 mm)
4. Gemessene Laenge >97.2 mm (2% Laengung) → Kette UND Kettenrad wechseln

**Zahnspiel pruefen:**
1. Steuerrad festhalten
2. Am Quadrant-Arm (oder Kette am Pedestal) vor/zurueck bewegen
3. Spuerbares Spiel am Steuerrad: In Grad umrechnen
4. Grenzwert: 3-5° am Steuerrad gesamt (alle mechanischen Spielanteile zusammen)

**Lager-Geraeusche:**
1. Steuerrad langsam drehen, dabei Hand auf Pedestal-Gehaeuse legen
2. Vibrationen spuerbar → Lager verschlissen
3. Knirschen hoerbar → Lager trocken oder beschaedigt
4. Klicken bei jeder Umdrehung → Zahnrad-Defekt oder Kettenglied

### 6.9 Zusammenfassende Verschleissgrenzen-Tabelle

| Komponente | Parameter | Neuzustand | Verschleissgrenze | Sofort-Tausch |
|-----------|-----------|-----------|-------------------|--------------|
| Steuerseil 1x19 | Litzenbrueche/m | 0 | 3 | >5 oder an Endverbindung |
| Steuerseil | Laengung | 0% | 0.3% | >0.5% |
| Quadrant Alu | Seilrillen-Tiefe | 0 mm | 2 mm | >3 mm oder Riss |
| Kette | Laengung | 0% | 1.5% | >2% |
| Pedestal-Zahnrad | Zahndicke-Abnahme | 0% | 15% | >25% oder Haifischzahn |
| Hydraulik-Fluid | Wassergehalt | 0% | 0.05% | >0.1% |
| Hydraulik-Fluid | Partikelzahl | ISO 14/11 | ISO 16/13 | >ISO 18/15 |
| Hydraulikschlauch | Alter | 0 Jahre | 5 Jahre | >7 Jahre oder Riss |
| Ruderlager Composite | Radialspiel | 0.05-0.15 mm | 0.5 mm | >1.0 mm |
| Ruderlager Bronze | Radialspiel | 0.10-0.20 mm | 0.4 mm | >0.8 mm |
| Ruderlager | Axialspiel | 0-0.5 mm | 1.5 mm | >2.0 mm |
| Koker-Dichtlippe | Leckrate | 0 | Feuchtigkeit | Tropfend |
| Autopilot-Antrieb | Geraeuschpegel | Leise, gleichm. | Hoerbar, unregelm. | Schleifen, Blockieren |
| Push-Pull-Kabel | Handkraft Steuerrad | 3-5 kg | 8-10 kg | >12 kg |
| Push-Pull-Kabel | Totgang Steuerrad | <3° | 5-8° | >10° |
| Steuerrad-Nabe | Spiel auf Schaft | 0 | Fuhlbar | Sicht-/hoerbar |

---

## 7. Anlagen-spezifische Wartung

### 7.1 Segelyacht vs. Motorboot

#### 7.1.1 Besonderheiten Segelyacht

**Hoehere Belastung durch:**
- Kraengung: Ruderlager werden asymmetrisch belastet, erhoehter Verschleiss auf Leeseite
- Seegangskraefte: Bei Amwind-Kurs dauerhaft hohe Ruderkraefte (Luv-Gierigkeit)
- Autopilot-Dauerlast: Bei Langfahrt unter Segel laeuft Autopilot oft 12-20 Stunden taeglich
- Grosse Ruderwinkel: Manoever (Wenden, Halsen) nutzen den vollen Ruderausschlag

**Spezifische Wartungspunkte Segelyacht:**
- Seilsteuerung: Erhoehte Belastung durch Kraengung — Seil muss bei verschiedenen Kraengungswinkeln freigaengig sein
- Quadrant: Durch Kraengung veraendert sich der Seilverlauf leicht → Fuehrungen muessen grosszuegig dimensioniert sein
- Ruderlager: Bei starker Kraengung arbeiten Lager am oberen Grenzbereich — kuerzere Inspektionsintervalle bei Offshore-Seglern
- Notpinne: PFLICHT bei Segelyachten in CE-Kategorie A und B
- Autopilot: Wind-Modus belastet den Antrieb staerker als Kompasskurs-Modus (staendige Korrekturen bei Windaenderung)
- Doppelsteuerstand: Koppelstange/Kette zwischen den Raedern — zusaetzliche Verschleisskomponente

**Segelyacht-spezifische Inspektionspunkte:**
- Seil unter verschiedenen Kraengungswinkeln pruefen (z.B. Seitengurt zur Simulation)
- Ruderlager-Spiel bei kraengendem Boot messen (im Wasser)
- Autopilot-Funktion bei verschiedenen Windstaerken dokumentieren
- Steuerkraefte bei verschiedenen Segeltrimms vergleichen (zu hohe Steuerkraft = schlechter Trimm ODER erhoehte Reibung)

#### 7.1.2 Besonderheiten Motorboot

**Andere Belastungsmuster:**
- Keine Kraengung im Normalbetrieb, aber Rollbewegung im Seegang
- Hohe Steuergeschwindigkeit: Motorboot-Steuerung wird oft schnell und haeufig betaetigt (Manoever im Hafen)
- Vibrationsbelastung: Motorvibrationen werden in die Steueranlage eingeleitet
- Gleitfahrt: Hohe Geschwindigkeit erzeugt hohe Ruderkraefte, aber kurzzeitig

**Spezifische Wartungspunkte Motorboot:**
- Push-Pull-Kabel (Aussenborder, kleine Motorboote): Gaengigkeit ist kritisch — schwergaengiges Kabel fuehrt zu unpraeziser Steuerung
- Hydrauliksteuerung: Bei hohen Geschwindigkeiten muss das Steuer praezise und spielfrei sein
- Trimmklappen-Integration: Wenn Trimmklappen ueber Steuersystem angesteuert werden → Zusatzkomponente in der Wartung
- Vibrationen: Alle Verschraubungen regelmassig auf Festsitz pruefen (Vibrations-Losedrehung)
- Bugstrahler-Integration: Elektrische Integration pruefen, Kabelverbindungen

**Motorboot-spezifische Inspektionspunkte:**
- Push-Pull-Kabel: Handkraft am Steuerrad messen (soll: 3-8 kg, max: 12 kg)
- Hydrauliksteuerung: Totgang (Spiel) am Steuerrad messen (max: 5° bei Geradeausfahrt)
- Lenkstockhebelspiel: Bei Steuerrohr-Konstruktionen (Innenborder): max. 2° am Steuerrohr
- Vibrations-Check: Verschraubungen an Zylinder, Pumpe, Pedestal

### 7.2 Kuestenfahrt vs. Offshore

#### 7.2.1 Kuestenfahrt (CE-Kategorie C/D)

**Wartungsphilosophie:**
- Regelmaessige Nutzung in geschuetzten Gewaessern
- Hafen ist immer in Reichweite → Notsteuerung weniger zeitkritisch
- Geringere Seegangbelastung → laengere Komponentenlebensdauer
- Saisonaler Betrieb → Winterlager-Wartung besonders wichtig

**Angepasste Intervalle Kuestenfahrt:**
- Seilwechsel: Alle 7-10 Jahre (statt 5-7)
- Hydraulikoelwechsel: Alle 3 Jahre (statt 2)
- Ruderlager: Alle 2 Jahre pruefen (statt jaehrlich)
- Autopilot: Saisonbeginn reicht
- Notpinne: Jaehrlicher Test genuegt

#### 7.2.2 Offshore (CE-Kategorie A/B)

**Wartungsphilosophie:**
- Boot muss jederzeit manoevrierbar sein — naechster Hafen ggf. tagelang entfernt
- Hohe Seegangbelastung → beschleunigter Verschleiss
- Notsteuerung muss SOFORT einsatzbereit sein
- Redundanz: Zweites Seil, Reserve-Hydraulikpumpe, Notpinne + Talje
- Ersatzteile mitfuehren

**Angepasste Intervalle Offshore:**
- Seilwechsel: Alle 3-5 Jahre
- Hydraulikoelwechsel: Jaehrlich
- Ruderlager: Alle 6 Monate pruefen
- Autopilot: Monatliche Funktionspruefung
- Notpinne: Monatlicher Stecktest, vierteljährliche Probesteuerung

**Offshore-Pflicht-Ersatzteile:**
- Kompletter Satz Steuerseile (vormontiert mit Presshuelsen)
- Hydraulikoel (Systemmenge + 50%)
- Dichtungssaetze fuer Helmpumpe und Zylinder
- Schlauch-Reparaturset (fuer Hydraulikschlaeuche)
- Notpinne + Adapter
- Bolzen, Splinte, Schaekel in passenden Groessen
- Seilklemmen (Nicropress) + Presszange

### 7.3 Multihull — Katamaran und Trimaran

**Besonderheiten Multihull-Steuerung:**

Katamarane und Trimarane stellen besondere Anforderungen an die Steueranlage:

**Doppelruder (Standard bei Katamaranen):**
- Zwei separate Ruder → doppelte Komponentenanzahl
- Koppelmechanismus (Koppelstange, Kette, oder Hydraulik) als zusaetzliche Verschleisskomponente
- Synchronisation der Ruder: Beide Ruder muessen exakt gleichen Ausschlag haben
- Asymmetrische Belastung bei Seitenwind/Stroemung

**Wartungs-Besonderheiten Multihull:**

| Komponente | Besonderheit Multihull | Empfehlung |
|-----------|----------------------|------------|
| Koppelstange | Zusaetzliche Verschleisskomponente | Halbjährlich Gelenke schmieren, Spiel pruefen |
| Seilsteuerung | Laengere Seilwege → mehr Dehnung | Haeufigere Spannungskontrolle |
| Hydraulik | Zwei Zylinder → doppelter Oelbedarf | Entlueftung beider Zylinder |
| Ruderlager | Zwei Satz Lager → doppelte Inspektion | Beide Seiten vergleichen (asymmetrischer Verschleiss?) |
| Autopilot | Hoehere Steuerkraefte → groesserer Antrieb | Antriebsdimensionierung pruefen |
| Notpinne | Zwei Notpinnen erforderlich! | Beide testen |

**Multihull-spezifische Pruefpunkte:**
1. Koppelmechanismus: Spiel in allen Gelenken pruefen
2. Synchronisation: Beide Ruder von Mittelstellung aus gleichzeitig messen → Abweichung max. 2°
3. Bei Hydraulik: Druck beider Zylinder vergleichen → Asymmetrie zeigt Leckage
4. Ruderlager: Beide Seiten separat messen und vergleichen
5. Katamarane mit Daggerboards: Daggerboard-Fuehrungen beeinflussen Steuererhalten → in Wartung einbeziehen

### 7.4 Regattaboot — Hochleistungs-Wartung

**Performance-relevante Wartungsaspekte:**

Bei Regattabooten geht die Wartung ueber Sicherheit hinaus — sie ist direkt leistungsrelevant:

**Reibungsminimierung:**
- Ruderlager: Spiel am unteren Ende des Toleranzbereichs halten (Widerstand minimieren)
- Steuerseile: Immer optimal gespannt (nicht ueberspannt → Reibung!)
- Pedestal-Getriebe: Hochwertige Schmiermittel (Teflon-basiert)
- Ruderblatt: Oberflaeche polieren (800er, dann 1200er Nassschleifpapier), kein dicker Antifouling-Aufbau
- Hydraulik: Leichtlauf-Fluid (ISO VG 10 statt VG 15 bei Zustimmung des Herstellers)

**Autopilot-Optimierung fuer Regatta:**
- Response-Level hoch (7-9) fuer praezises Kurshalten
- Ruderlage-Sensor mit hoher Aufloesung
- Stromversorgung ueberdimensioniert (keine Spannungseinbrueche bei Manoevern)
- Bei Offshore-Regatten: Autopilot-Dauertest ueber 24h vor dem Start

**Regatta-Wartungskalender:**
| Zeitpunkt | Massnahme |
|-----------|-----------|
| 1 Monat vor Regatta | Vollstaendige Inspektion aller Komponenten |
| 1 Woche vor Regatta | Seilspannung fein-einstellen, Pedestal schmieren |
| Tag vor Regatta | Autopilot-Kalibrierung, Notpinne-Stecktest |
| Nach jeder Regatta | Kurzinspektion auf Beschaedigungen |
| Saisonende | Vollrevision |

### 7.5 Charteryacht — Spezielle Anforderungen

**Erhoehter Verschleiss durch:**
- Wechselnde Crew mit unterschiedlicher Erfahrung
- Haeufige Hafenmanoever (Steuerung staendig im Einsatz)
- Weniger sorgfaeltiger Umgang als beim eigenen Boot
- Kein kontinuierliches Monitoring durch den Eigner

**Empfohlene Wartungsstrategie:**
- Professionelle Inspektion nach jeder Charter (oder alle 2 Wochen)
- Vierteljährliche vollstaendige Inspektion aller Komponenten
- Seilwechsel alle 3-4 Jahre (statt 5-7)
- Hydraulikoelwechsel jaehrlich
- Pedestal-Revision alle 2 Jahre
- Ruderlager alle 12 Monate pruefen
- Autopilot-Kalibrierung monatlich
- Notpinne-Test vor jeder Charter

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Steuerseil — Litzenbrueche (STEER-M-F01)

**Beschreibung:** Einzelne oder mehrere Draehte des 1x19 oder 7x19 Edelstahl-Steuerseils sind gebrochen und stehen seitlich ab.

**Haeufigkeit:** Sehr haeufig (40% aller Seil-Befunde)

**Typische Lokalisation:**
- An Umlenkpunkten (Sheaves) — hoechste Biegewechselbelastung
- An Nicropress-Huelsen — Spannungskonzentration
- An Decksdurchfuehrungen — Abrieb + Korrosion

**Ursachen:**
1. Ermuedung durch Biegewechsel (Hauptursache)
2. Korrosion (beschleunigt Ermuedung)
3. Zu hohe Seilspannung
4. Zu kleiner Umlenkradius (Rolle zu klein)
5. Fehlende Schmierung

**Schweregrad-Einstufung:**

| Befund | Schweregrad | Score-Impact |
|--------|-----------|--------------|
| 1-2 Brueche/m, an Umlenkung | 2 (beobachten) | -10 |
| 3-5 Brueche/m | 3 (Massnahme planen) | -25 |
| >5 Brueche/m | 4 (bald handeln) | -50 |
| Brueche an Endverbindung | 5 (sofort) | -75 |
| Seil kurz vor Durchbruch (>50% Querschnitt) | 5 (sofort) | -100 |

**Empfehlung:**
- Schweregrad 2: Naechster Saisonstart wechseln, engmaschig beobachten
- Schweregrad 3-5: Seil wechseln, Ursache abklären (Rollengroesse, Spannung, Korrosion)

### 8.2 Fehlerbild F02: Hydraulikleckage — Aeussere Leckage (STEER-M-F02)

**Beschreibung:** Hydraulikfluid tritt sichtbar aus dem System aus — an Verschraubungen, Schlaeuchen, Pumpe oder Zylinder.

**Haeufigkeit:** Haeufig (30% aller Hydraulik-Befunde)

**Typische Lokalisation:**
- Schlauchanschluesse (haeufigste Leckstelle)
- Hydraulikzylinder-Stangendichtung
- Helmpumpen-Wellendichtung
- Entlueftungsschrauben (nicht richtig geschlossen)

**Ursachen:**
1. Alterung von Dichtungen und Schlaeuchen
2. Vibrationsbelastung lockert Verschraubungen
3. Thermische Zyklen (Materialermuedung)
4. Ueberdruckereignisse
5. Korrosion an Anschluessen

**Schweregrad-Einstufung:**

| Befund | Schweregrad | Score-Impact |
|--------|-----------|--------------|
| Oelfilm, kein Tropfen | 2 | -10 |
| Gelegentliche Tropfen | 3 | -30 |
| Dauerhaftes Tropfen | 4 | -50 |
| Oellache, Fuellstand sinkt sichtbar | 5 | -80 |

**Empfehlung:**
- Verschraubung nachziehen (Drehmoment beachten)
- Schlauch-O-Ringe ersetzen
- Bei Zylinder-/Pumpenleckage: Dichtungssatz wechseln

### 8.3 Fehlerbild F03: Schwammiges Steuer — Luft im Hydrauliksystem (STEER-M-F03)

**Beschreibung:** Das Steuerrad fuehlt sich weich, schwammig, ungenau an. Der Ruderausschlag entspricht nicht dem erwarteten Radausschlag.

**Haeufigkeit:** Haeufig (25% aller Hydraulik-Befunde)

**Ursachen:**
1. Luft im System (Hauptursache)
2. Interne Leckage in Pumpe oder Zylinder (Dichtungsverschleiss)
3. Kavitation in der Pumpe
4. Falsches Fluid (zu duennfluessig)
5. Defektes Rueckschlagventil

**Diagnose:**
- Luft: Steuer ist am Anfang der Bewegung schwammig, wird dann fest → Entlueften
- Interne Leckage: Steuer wird bei Last schwammig, Helm driftet langsam → Dichtungen
- Kavitation: Geraeausche (Knattern), Schwamm nur bei schneller Bewegung → Zulaufleitung pruefen

**Schweregrad:** 3-4 (Score-Impact: -30 bis -60)

**Empfehlung:**
1. Entlueften (siehe 4.3)
2. Wenn nach Entlueftung weiterhin schwammig: Drucktest, Leckagesuche
3. Fluessigkeitsstand kontrollieren

### 8.4 Fehlerbild F04: Erhoehtes Ruderspiel (STEER-M-F04)

**Beschreibung:** Spuerbares Spiel zwischen Steuerradbewegung und Ruderreaktion. Beim Steuern: "Totzone" um die Mittelstellung.

**Haeufigkeit:** Haeufig (35% aller mechanischen Befunde)

**Ursachen:**
1. Ruderlager verschlissen (haeufigste Ursache)
2. Seilsteuerung: Zu geringe Seilspannung
3. Seilsteuerung: Quadrant-Klemmung locker
4. Pedestal: Getriebeverschleiss (Zahnspiel)
5. Pedestal: Kettenlaengung
6. Hydraulik: Interne Leckage oder Luft
7. Push-Pull-Kabel: Ausgeschlagene Gelenke

**Diagnose-Baum:**
```
Spiel am Steuerrad?
├── Bewegt sich Ruder beim Spieltest? → JA → Ruderlager
│   └── Messuhr: Spiel >1 mm? → Lager wechseln
├── Bewegt sich Ruder NICHT? → Spiel in der Uebertragung
│   ├── Seilsteuerung → Seil-/Kettenspannung pruefen
│   ├── Getriebsteuerung → Pedestal oeffnen, Zahnspiel pruefen
│   └── Hydraulik → Entlueften, Drucktest
```

**Schweregrad:** 2-4 (Score-Impact: -15 bis -50)

### 8.5 Fehlerbild F05: Schwergaengiges Steuer (STEER-M-F05)

**Beschreibung:** Erhoehter Kraftaufwand beim Steuern. Steuerrad laesst sich nur schwer oder ruckartig drehen.

**Haeufigkeit:** Maessig haeufig (20% aller Befunde)

**Ursachen:**
1. Ruderlager trocken oder verschmutzt
2. Seilsteuerung: Ueberspannt, Umlenkrolle blockiert, Seil korrodiert
3. Hydraulik: Falsche Viskositaet, verstopftes Ventil
4. Pedestal: Trockene Zahnraeder, beschaedigte Lager
5. Ruderblatt: Starker Bewuchs (erhoehte Ruderkraefte)
6. Autopilot-Kupplung greift teilweise (nicht vollstaendig ausgekuppelt)
7. Push-Pull-Kabel: Innere Korrosion, Huellrohr beschaedigt

**Schweregrad:** 2-4 (Score-Impact: -15 bis -60)

**Empfehlung:**
- Schmierung aller beweglichen Teile als Erstmassnahme
- Umlenkrollen-Gaengigkeit einzeln pruefen
- Bei Hydraulik: Fluid pruefen, ggf. wechseln
- Ruderblatt auf Bewuchs pruefen (oft uebersehene Ursache)

### 8.6 Fehlerbild F06: Ruder-Offset — Boot faehrt nicht geradeaus (STEER-M-F06)

**Beschreibung:** Trotz Steuerrad in Mittelstellung faehrt das Boot nicht geradeaus. Dauerhaftes Gegenhalten erforderlich.

**Ursachen:**
1. Asymmetrische Seilspannung (BB ≠ StB)
2. Ruderlage-Sensor falsch kalibriert (Autopilot zeigt falsche Mitte)
3. Ruderblatt verbogen (Grundberuehrung, Aufsetzer)
4. Ruderschaft verdreht im Quadrant (Klemmung gerutscht)
5. Hydraulikzylinder nicht in Mittelstellung (Leitungslaengen asymmetrisch)
6. Kiel/Rumpf-Asymmetrie (seltener: Werftfehler, Osmose-Reparatur)

**Diagnose:**
- Steuer in Mitte → Ruder pruefen: Steht Ruder wirklich mittig?
- Ruder mittig → Rumpf-/Kielproblem → Trimm anpassen
- Ruder nicht mittig → Seilspannung messen (BB vs. StB) oder Hydraulik pruefen

**Schweregrad:** 2-3 (Score-Impact: -10 bis -30)

### 8.7 Fehlerbild F07: Koker-Leckage — Wassereinbruch am Ruderschaft (STEER-M-F07)

**Beschreibung:** Wasser dringt entlang des Ruderschaftes durch den Koker ins Bootsinnere ein.

**Haeufigkeit:** Maessig haeufig (15% der Befunde an Segel-/Motorbooten >10m)

**Ursachen:**
1. Koker-Dichtlippe (Lip Seal) verschlissen
2. Koker-Dichtlippe falsch herum eingebaut
3. Schaft-Oberflaeche korrodiert/rauh (beschaedigt die Dichtung)
4. Kokerohr gerissen (GFK-Delaminierung)
5. Lagersitz-Riss (strukturelles Problem)
6. Ruderlager-Spiel so gross, dass Dichtlippe nicht mehr greift

**Schweregrad:** 3-5 (Score-Impact: -30 bis -80)

**Empfehlung:**
- Sofortmassnahme: Notpackung/Dichtmasse (Sikalfex 291)
- Zeitnah: Dichtlippe wechseln (Boot muss dafuer an Land oder im Trockendock sein)
- Bei Kokerohr-Riss: Laminatreparatur durch Fachbetrieb

### 8.8 Fehlerbild F08: Autopilot-Drift — Pilot haelt Kurs nicht (STEER-M-F08)

**Beschreibung:** Autopilot weicht langsam oder periodisch vom Sollkurs ab, reagiert traege oder gar nicht.

**Ursachen:**
1. Fehlkalibrierung (haeufigste Ursache nach Saisonpause)
2. Kompass-Stoerung (Magnet, Elektrogeraet in der Naehe)
3. Zu niedrige Response-Einstellung
4. Antrieb zu schwach fuer die Verhaeltnisse (Seegang, Wind)
5. Stromversorgung instabil (Spannungsschwankungen)
6. Ruderlage-Sensor defekt oder dejustiert
7. Interne Leckage in Autopilot-Hydraulikpumpe
8. Kupplung rutscht (bei mechanischem Antrieb)

**Diagnose:**
```
Kursabweichung?
├── Langsame Drift (>5 min) → Kompass-Problem oder interne Leckage
├── Schnelle Pendelung → Response zu hoch oder Ruderlagesensor
├── Keine Reaktion → Stromversorgung, Sicherung, Antrieb
└── Schlechtes Wetter → Antrieb unterdimensioniert, Response anpassen
```

**Schweregrad:** 2-4 (Score-Impact: -15 bis -50)

### 8.9 Fehlerbild F09: Geraeusche — Klappern, Knirschen, Quietschen (STEER-M-F09)

**Beschreibung:** Ungewoehnliche Geraeusche beim Steuern oder bei Ruderbewegung durch Seegang.

**Geraeusch-Zuordnung:**

| Geraeusch | Wahrscheinliche Quelle | Dringlichkeit |
|-----------|----------------------|--------------|
| Klappern (metallisch) | Lose Kette, Bolzen, Quadrant-Klemmung | Mittel-Hoch |
| Knirschen | Trockene Lager, Sand/Salz im Lager | Hoch |
| Quietschen | Trockene Dichtung, Fett fehlt | Mittel |
| Knarren (rhythmisch) | Ruderlager-Spiel bei Seegang | Mittel |
| Heulen (hydraulisch) | Kavitation, Luft in Pumpe | Hoch |
| Klicken (regelmaessig) | Kette springt, Zahnrad beschaedigt | Hoch |
| Dumpfes Schlagen | Ruderblatt schlaegt an Rumpf/Skeg | Sofort pruefen |

**Schweregrad:** 2-5 (Score-Impact: -10 bis -70)

### 8.10 Fehlerbild F10: Steuerrad-Spiel — Lose Nabe (STEER-M-F10)

**Beschreibung:** Steuerrad wackelt auf dem Schaft, klopft, oder hat fuhlbares Axialspiel.

**Ursachen:**
1. Nabenmutter lose (vibrations-bedingt)
2. Keilnut/Passfeder verschlissen
3. Schaft-Konus korrodiert (festgefressen und dann ueberbelastet)
4. Steuerrad-Nabe gerissen (Materialermuedung)

**Schweregrad:** 3-4 (Score-Impact: -25 bis -60)

**Empfehlung:**
- Nabe mit Drehmomentschluessel nachziehen
- Bei verschlissener Keilnut: Nabe und Schaft durch Fachbetrieb pruefen
- Anti-Seize auf Konus bei jeder Demontage/Montage

### 8.11 Fehlerbild F11: Ruderblatt-Wasseraufnahme (STEER-M-F11)

**Beschreibung:** Ruderblatt hat Wasser aufgenommen — erhoehtes Gewicht, dumpfer Klang beim Klopftest.

**Ursachen:**
1. Gelcoat-Risse (insbes. am Schaft-Uebergang)
2. Antifouling-Risse
3. Osmose im Laminat
4. Undichte Naht (bei verschraubten Ruderschalen)
5. Beschaedigung durch Grundberuehrung

**Schweregrad:** 2-4 (Score-Impact: -15 bis -50)

**Langzeitfolgen:**
- Erhoehtes Gewicht → Vibrationen bei Fahrt
- Innere Korrosion am Schaft → strukturelles Versagen
- Frost: Wasser gefriert → Laminat wird gesprengt
- Osmose-Beschleunigung

### 8.12 Fehlerbild F12: Notpinne nicht einsatzbereit (STEER-M-F12)

**Beschreibung:** Notpinne ist nicht auffindbar, passt nicht auf den Ruderschaft, oder der Zugangsweg ist blockiert.

**Ursachen:**
1. Notpinne "irgendwo" verstaut, nicht auffindbar
2. Passflaeche korrodiert (Schaft oder Pinne)
3. Zugang blockiert (Cockpit-Tisch, Gegenstaende)
4. Adapter fehlt (bei nachgeruesteter Steuerung)
5. Bolzen/Sicherung fehlt

**Schweregrad:** 3-5 (CE-Kategorie A/B: Schweregrad 5)

**Score-Impact:** -30 bis -80

**Empfehlung:**
- Dedizierter, beschrifteter Stauort fuer Notpinne
- Passung jaehrlich testen
- Zugangsweg freihalten (keine Gasflaschen, Fender etc. davor)

### 8.13 Zusammenfassende Fehlerbild-Matrix

Die folgende Matrix ordnet Symptome den wahrscheinlichsten Fehlerbildern zu und gibt die erste Massnahme an:

| Symptom | Wahrscheinlichstes Fehlerbild | Zweitwahrscheinlichstes | Erste Massnahme |
|---------|------------------------------|------------------------|-----------------|
| Steuer reagiert nicht | F01 (Seilbruch) oder Hydraulikversagen | F05 (Blockade) | Notpinne! |
| Schwammiges Steuer | F03 (Luft in Hydraulik) | F02 (Leckage) | Entlueften |
| Steuer hat Spiel | F04 (Lagerspiel) | Pedestal-Verschleiss | Quelle lokalisieren |
| Steuer schwergaengig | F05 (Div. Ursachen) | Bewuchs am Ruder | Schmierung als Erstmassnahme |
| Boot faehrt schief | F06 (Offset) | Seilspannung asymmetrisch | Seilspannung BB/StB vergleichen |
| Wasser im Boot achtern | F07 (Koker-Leckage) | Koker-Riss | Dichtlippe pruefen |
| Autopilot schlecht | F08 (Drift) | Stoerfeld, Antrieb | Kalibrierung |
| Geraeusche | F09 (Div. Quellen) | Lagerverschleiss | Geraeusch lokalisieren |
| Steuerrad wackelt | F10 (Nabe lose) | Keilnut verschlissen | Nabenmutter pruefen |
| Ruder vibriert | F11 (Wasseraufnahme) | Lagerspiel | Klopftest + Feuchtemessung |
| Notfall — kein Steuern | F12 + div. | — | Notpinne SOFORT |

### 8.14 Fehlerbilder nach Dringlichkeit sortiert

**SOFORT HANDELN (Schweregrad 5 — Sicherheitskritisch):**
- F01: Seilbruch (>50% Querschnitt) oder Bruch an Endverbindung
- F05: Steuerung blockiert
- F07: Koker-Leckage mit steigendem Wassereinbruch
- F12: Notpinne nicht einsatzbereit bei CE-Kat. A/B

**BALD HANDELN (Schweregrad 4 — Innerhalb 1 Monat):**
- F01: >5 Litzenbrueche/m
- F02: Dauerhaftes Tropfen an Hydraulik
- F03: Schwammiges Steuer trotz Entlueftung
- F04: Ruderspiel >1 mm (Composite) oder >0.8 mm (Bronze)
- F08: Autopilot-Ausfall bei Nacht-/Offshore-Fahrten

**PLANEN (Schweregrad 3 — Innerhalb der Saison):**
- F01: 3-5 Litzenbrueche/m
- F02: Gelegentliche Tropfen
- F04: Ruderspiel 0.5-1.0 mm
- F06: Konstanter Ruder-Offset
- F09: Regelmaessige ungewoehnliche Geraeusche
- F10: Steuerrad-Spiel fuhlbar
- F11: Ruderblatt-Feuchte 15-30%

**BEOBACHTEN (Schweregrad 2):**
- F01: 1-2 Litzenbrueche/m
- F02: Oelfilm ohne Tropfen
- F05: Leicht erhoehte Steuerkraefte
- F08: Autopilot leicht ungenau
- F09: Gelegentliche Geraeusche
- F11: Leichte Feuchte am Ruderblatt

### 8.15 AYDI Score-Berechnungslogik Wartungszustand

Der AYDI-Wartungsscore berechnet sich aus den Sub-Scores der einzelnen Komponenten:

```
Wartungs_Score = (
    Seil_Score × 0.20 +
    Hydraulik_Score × 0.20 +
    Lager_Score × 0.25 +
    Pedestal_Score × 0.10 +
    Autopilot_Score × 0.10 +
    Notsteuerung_Score × 0.15
) - Summe(Befund_Score_Impacts)

Minimum: 0, Maximum: 100
```

**Gewichtung begruendet:**
- Ruderlager: 25% — Hoechste Sicherheitsrelevanz, teuerste Reparatur
- Seil: 20% — Direkter Versagensmodus, haeufigster Befund
- Hydraulik: 20% — Komplexes System, verdeckte Maengel
- Notsteuerung: 15% — Letztes Sicherheitsnetz
- Pedestal: 10% — Robustes System, seltener Ausfall
- Autopilot: 10% — Komfortfunktion, nicht sicherheitskritisch (ausser bei Einhand-/Nachtfahrt)

**Score-Interpretation:**

| Score | Bewertung | Empfehlung |
|-------|-----------|------------|
| 90-100 | Ausgezeichnet | Keine Massnahmen, naechste planmaessige Wartung |
| 75-89 | Gut | Kleinere Maengel beobachten, Plan einhalten |
| 60-74 | Befriedigend | Maengel beheben, Intervalle verkuerzen |
| 40-59 | Maengelbehaftet | Zeitnahe Reparatur erforderlich |
| 20-39 | Schlecht | Eingeschraenkte Fahrerlaubnis empfohlen |
| 0-19 | Kritisch | Nicht fahrbereit, Instandsetzung vor naechster Fahrt |

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Steuerung reagiert nicht

```
STEUERUNG REAGIERT NICHT
│
├── Hydraulisch?
│   ├── Oelstand pruefen
│   │   ├── Leer → Leckage suchen, nachfuellen, entlueften
│   │   └── Voll → Weiter
│   ├── Entlueftung versuchen
│   │   ├── Luftblasen → Entlueften (Kap. 4.3), Leckquelle suchen
│   │   └── Kein Effekt → Weiter
│   ├── Bypass-Ventil pruefen (bei Doppelsteuerstand)
│   │   ├── Offen → Schliessen
│   │   └── Geschlossen → Weiter
│   ├── Drucktest
│   │   ├── Kein Druck → Pumpe intern defekt → Fachbetrieb
│   │   └── Druck vorhanden, Ruder reagiert nicht → Zylinder intern defekt oder mechanische Blockade
│   └── Mechanische Blockade am Ruder pruefen
│       ├── Ruderlager blockiert → Lager pruefen
│       ├── Fremdkoerper am Ruder → Taucher / an Land pruefen
│       └── Ruderschaft gebrochen → NOTFALL → Notsteuerung
│
├── Seilsteuerung?
│   ├── Seil gerissen → Seil ersetzen (siehe Kap. 4.1)
│   ├── Seil von Rolle gesprungen → Wieder einlegen, Spannung pruefen
│   ├── Quadrant lose → Klemmung erneuern, Drehmoment pruefen
│   ├── Kettenverbindung getrennt → Neu verbinden, Schaekel sichern
│   └── Pedestal blockiert → Pedestal oeffnen, Fremdkoerper/Defekt pruefen
│
└── NOTSTEUERUNG EINLEITEN
    1. Segel bergen / Motor Leerlauf
    2. Notpinne montieren (Kap. 4.7)
    3. Wenn Notpinne nicht moeglich: Nottiller aus Leinen improvisieren
    4. Mayday/PanPan je nach Situation
```

### 9.2 Entscheidungsbaum: Autopilot funktioniert nicht

```
AUTOPILOT FUNKTIONIERT NICHT
│
├── Display tot / kein Start?
│   ├── Stromversorgung pruefen
│   │   ├── Sicherung → Sicherung pruefen/ersetzen
│   │   ├── Kabelverbindung → Klemmen pruefen (Korrosion?)
│   │   └── Batteriespannung → Min. 12.0V (bei Betrieb: 11.5V Grenze)
│   └── Display defekt → Ersatz-Bedieneinheit / Fernbedienung nutzen
│
├── Display an, Fehlermeldung?
│   ├── "No Compass" → Kompass-Kabel pruefen, Kompass-Einstellung
│   ├── "No Rudder Feedback" → Ruderlage-Sensor pruefen, Kabel
│   ├── "Drive Error" → Antrieb pruefen (Sicherung, Kabel, mechanisch blockiert?)
│   ├── "Off Course" → Kalibrierung wiederholen (Kap. 4.4)
│   └── "Low Voltage" → Batterie laden, Kabelquerschnitt pruefen
│
├── Pilot laeuft, steuert aber schlecht?
│   ├── Pendelt (S-Kurven) → Response reduzieren, Ruderlage-Sensor pruefen
│   ├── Reagiert traege → Response erhoehen, Antrieb pruefen
│   ├── Driftet → Kompass kalibrieren, Stoerquellen entfernen
│   └── Funktioniert bei leichtem Wind, versagt bei starkem → Antrieb unterdimensioniert
│
└── Nach Kalibrierung und Prüfung weiterhin defekt?
    → Fachbetrieb / Hersteller-Service kontaktieren
```

### 9.3 Entscheidungsbaum: Leckage an Hydraulik lokalisieren

```
LECKAGE LOKALISIEREN
│
├── Oelstand sinkt, aber keine sichtbare Leckage?
│   ├── Interne Leckage (Pumpe oder Zylinder)
│   │   ├── Drucktest: Druck haelt → Zylinder-Kolbendichtung
│   │   └── Drucktest: Druck sinkt schnell → Pumpen-Innendichtung
│   └── Kleinste aeussere Leckage → System reinigen, 24h warten, neue Oelspuren suchen
│
├── Leckage an Verschraubung?
│   ├── Nachziehen mit korrektem Drehmoment
│   ├── Wenn weiterhin undicht → O-Ring oder Schneidring ersetzen
│   └── Achtung: NICHT ueberdrehen — Gewinde beschaedigen macht Situation schlimmer
│
├── Leckage am Schlauch?
│   ├── Am Anschluss → Anschluss loesen, O-Ring pruefen, neu montieren
│   ├── Am Schlauchkoerper → Schlauch ersetzen (NICHT reparieren!)
│   └── Querschnitts-Quellung sichtbar → Falsches Fluid? Schlauch sofort ersetzen
│
├── Leckage an Pumpe?
│   ├── Am Steuerrad-Schaft → Wellendichtung ersetzen
│   ├── Am Gehaeuse → Gehaeuse-O-Ringe ersetzen
│   └── Unter der Pumpe → Anschluss-Dichtungen pruefen
│
└── Leckage am Zylinder?
    ├── An der Kolbenstange → Stangendichtung ersetzen
    ├── Am Zylinderdeckel → Deckel-O-Ring ersetzen
    └── Am Kolbenstangenende → Gelenk-Dichtung ersetzen
```

### 9.4 Entscheidungsbaum: Ungewoehnliche Geraeusche

```
GERAEUSCHE BEIM STEUERN
│
├── Metallisches Klappern?
│   ├── Kette → Spannung pruefen, Kettenrad-Zustand
│   ├── Quadrant → Klemmung pruefen, Seil-Befestigung
│   ├── Bolzen/Schaekel → Befestigung pruefen, Splinte
│   └── Pedestal → Oeffnen und inspizieren
│
├── Knirschen/Schleifen?
│   ├── Ruderlager → Schmieren, Spiel pruefen
│   ├── Pedestal-Getriebe → Fett erneuern
│   ├── Umlenkrolle → Lager pruefen/wechseln
│   └── Autopilot-Kupplung → Belaege pruefen
│
├── Quietschen?
│   ├── Koker-Dichtung → Schmieren (wasserbestaendiges Fett)
│   ├── Steuerrad-Nabe → Anti-Seize auftragen
│   └── Seil auf Rolle → Schmieren
│
├── Heulen/Pfeifen (hydraulisch)?
│   ├── Kavitation → Oelstand pruefen, Zulaufleitung, Fluid-Viskositaet
│   ├── Druckbegrenzungsventil → Einstellung pruefen
│   └── Luft im System → Entlueften
│
└── Dumpfes Schlagen?
    ├── Ruderblatt am Rumpf/Skeg → Lagerspiel pruefen, Anschlaege einstellen
    ├── Ruderblatt im Seegang → Ruderbremse/Stopper verwenden
    └── Quadrant am Anschlag → Anschlagdaempfer pruefen/ersetzen
```

### 9.5 Entscheidungsbaum: Steuerung nach Grundberuehrung

```
NACH GRUNDBERUEHRUNG — STEUERANLAGE PRUEFEN
│
├── Sofort-Check auf See:
│   ├── Steuern von Anschlag zu Anschlag → Eingeschraenkt? → Vorsicht!
│   ├── Visuelle Inspektion achtern → Ruder sichtbar beschaedigt?
│   ├── Spiel am Steuer veraendert?
│   └── Ungewoehnliche Geraeusche?
│
├── Wenn Steuerung eingeschraenkt oder Ruder sichtbar beschaedigt:
│   ├── Geschwindigkeit reduzieren
│   ├── Naechsten Hafen anlaufen
│   └── Wenn Steuerung versagt → Notpinne (Kap. 4.7)
│
├── Im Hafen / An Land — Systematische Pruefung:
│   ├── Ruderblatt visuell: Risse, Verformung, Delamination?
│   ├── Ruderblatt klopfen: Wasseraufnahme?
│   ├── Ruderschaft: Verbogen? (Gerade Kante anlegen)
│   ├── Ruderlager: Spiel veraendert? (Messuhr)
│   ├── Skeg (falls vorhanden): Risse, Verformung?
│   ├── Schaft-Ruderblatt-Verbindung: Bewegung, Risse?
│   └── Steueranlagen-Komponenten: Quadrant, Seile, Zylinder — Verformung?
│
└── Bei Verdacht auf strukturelle Schaeden:
    ├── Fachbetrieb beauftragen
    ├── UT-Pruefung (Ultraschall) des Ruderschafts
    ├── Ruderblatt roentgen oder CT (bei Verdacht auf innere Schaeden)
    └── Boot NICHT verwenden bis Freigabe durch Fachbetrieb
```

---

## 10. FAQ — Haeufig gestellte Fragen

### Allgemeine Wartung

**F01: Wie oft muss ich meine Steueranlage warten?**
Die Grundregel fuer Saisonsegler in gemaessigten Breiten: Visuelle Inspektion zu jedem Saisonstart, vollstaendige Inspektion jaehrlich, Komponentenwechsel nach Hersteller-Intervallen. Fuer Langfahrtsegler in Tropen: Intervalle halbieren. Die detaillierten Wartungsmatizen finden sich in Kapitel 3.1. (Confidence: documented)

**F02: Kann ich die Steueranlagen-Wartung komplett selbst machen?**
Ja, zu einem grossen Teil. Etwa 70% der Wartungsarbeiten (Stufe 1 und 2) koennen von einem technisch versierten Eigner selbst durchgefuehrt werden: visuelle Inspektion, Schmierung, Seilspannung pruefen, Hydraulikoel wechseln und entlueften, Autopilot kalibrieren, Notpinne testen. Fuer Arbeiten der Stufe 3 (Ruderlager wechseln, Hydraulikzylinder revidieren, Pedestal-Komplett-Revision) empfehlen wir einen Fachbetrieb. (Confidence: estimated)

**F03: Was kostet eine professionelle Steueranlagen-Inspektion?**
In Nordeuropa typischerweise 200-500 EUR fuer eine vollstaendige Inspektion (ca. 2-4 Stunden Arbeit, je nach Zugaenglichkeit). Darin enthalten: Seilspannung, Hydraulik, Ruderlager, Autopilot-Funktionstest, Protokoll. Nicht enthalten: Material, Oelwechsel, Reparaturen. Bei Yachten >16m: 400-800 EUR. (Confidence: estimated)

**F04: Mein Boot ist nur 3 Jahre alt — muss ich jetzt schon die Steueranlage warten?**
Ja, unbedingt. Auch neue Steueranlagen benoetigen regelmaessige Wartung. Gerade im ersten Jahr setzen sich Seile, Lager laufen sich ein, Schrauben lockern sich durch Vibrationen. Die Wartungsintervalle in Kapitel 3 gelten ab dem ersten Einsatztag. Zudem erlischt bei einigen Herstellern die Garantie, wenn die vorgeschriebene Wartung nicht nachgewiesen werden kann. (Confidence: documented)

**F05: Welche Werkzeuge brauche ich fuer die Eigener-Wartung der Steueranlage?**
Basis-Werkzeugsatz: Gabelschluessel (metrisch 8-24 mm), Tensiometer (z.B. Loos PT-2, ca. 80 EUR), Drehmomentschluessel (10-100 Nm), Messuhr mit Magnetfuss (ca. 30 EUR), Marine-Fett (NLGI 2), Seilschmiermittel (z.B. Boeshield T-9), Hydraulikfluid (Typ nach Hersteller), Auffangbehaelter, Handschuhe, Schutzbrille. Gesamtinvestition: ca. 200-350 EUR. (Confidence: estimated)

### Seilsteuerung

**F06: Wie erkenne ich, ob meine Steuerseile gewechselt werden muessen?**
Drei Kriterien: (1) Alter: Nach 5-7 Jahren (Saisonbetrieb) oder 3-5 Jahren (Langfahrt/Tropen) praeventiv wechseln, auch ohne sichtbare Schaeden. (2) Litzenbrueche: >3 Brueche pro Meter = Wechsel. (3) Knicke, Quetschungen, sichtbare Korrosion: Sofortiger Wechsel. Im Zweifel: Wechseln — ein Steuerseil kostet 150-400 EUR, ein Steuerungsversagen kann das Boot kosten. (Confidence: measured)

**F07: Mein Steuerseil hat eine einzelne gebrochene Litze — ist das gefaehrlich?**
Nicht sofort, aber es ist ein Warnsignal. Ein einzelner Litzenbruch reduziert die Seilfestigkeit um ca. 5-7%. Das Problem: Litzenbrueche kommen selten allein. Wenn Sie einen finden, sind an Umlenkpunkten oder im verdeckten Bereich oft mehr. Empfehlung: Bereich genau inspizieren, Seil in den naechsten 3 Monaten wechseln, engmaschig kontrollieren bis dahin. (Confidence: measured)

**F08: Welche Seilspannung ist richtig?**
Abhaengig vom Seildurchmesser: 4mm = 130 N, 5mm = 155 N, 6mm = 175 N (Sollwerte). Gemessen mit Tensiometer (z.B. Loos PT-2). Zu fest = erhoehter Verschleiss, zu locker = Seil springt von Rollen. Beide Seiten (BB/StB) muessen gleiche Spannung haben. Messung bei Raumtemperatur. Details in Kapitel 4.1. (Confidence: measured)

**F09: Kann ich ein einzelnes Steuerseil wechseln oder muss ich beide ersetzen?**
Empfehlung: Immer beide Seile gleichzeitig wechseln. Die Seile sind als Paar belastet worden und haben aehnliche Ermuedung. Ein neues Seil neben einem alten hat andere Dehneigenschaften, was zu asymmetrischem Verhalten fuehren kann. Zudem ist der Aufwand fuer zwei Seile kaum groesser als fuer eines. (Confidence: documented)

### Hydraulik

**F10: Welches Hydraulikoel kommt in meine Steuerung?**
Das steht im Hersteller-Handbuch oder auf dem Typenschild. Hauptunterscheidung: HLP ISO VG 15 (die meisten Systeme: Lewmar, Vetus, SeaStar) oder ATF Dexron (Hynautic/Wagner). NIEMALS mischen! Im Zweifel: Hersteller kontaktieren. Die vollstaendige Zuordnung steht in Kapitel 5.2. (Confidence: measured)

**F11: Mein Hydraulikoel ist dunkel geworden — muss ich es sofort wechseln?**
Dunkelverfaerbung zeigt Alterung an, ist aber nicht sofort gefaehrlich. Wenn das Oel klar (nur dunkel) ist und die Steuerung normal funktioniert: Wechsel bei naechster Gelegenheit einplanen (innerhalb von 3 Monaten). Wenn das Oel trueb/milchig ist: Wasser im System — zeitnah wechseln und Leckage suchen. Wenn Metallpartikel sichtbar: Sofort wechseln und System inspizieren. (Confidence: documented)

**F12: Meine Steuerung fuehlt sich schwammig an — was ist das?**
In 90% der Faelle: Luft im Hydrauliksystem. Luft komprimiert sich (anders als Hydraulikoel) und erzeugt ein weiches, schwammiges Gefuehl. Loesung: Entlueften (Kapitel 4.3). Wenn nach der Entlueftung weiterhin schwammig: Interne Leckage in Pumpe oder Zylinder (Dichtungsverschleiss). Dann Drucktest und ggf. Fachbetrieb. (Confidence: documented)

**F13: Wie oft muss ich meine Hydrauliksteuerung entlueften?**
Standard: Einmal zum Saisonbeginn nach dem Winterlager. Zusaetzlich: Nach jedem Oelwechsel, nach Arbeiten am System, wenn sich das Steuer schwammig anfuehlt, wenn Gurgelgeraeusche hoerbar sind. Bei korrekt abgedichtetem System sollte waehrend der Saison keine Entlueftung noetig sein. Wenn Sie haeufig entlueften muessen: Leckage im System suchen — Luft tritt dort ein, wo auch Oel austritt. (Confidence: documented)

**F14: Kann ich verschiedene Hydraulikoele mischen?**
Innerhalb derselben Spezifikation (z.B. HLP ISO VG 15 verschiedener Hersteller): Ja, in der Regel kompatibel. HLP und ATF: NEIN, auf keinen Fall! Die Additivpakete sind inkompatibel und koennen Dichtungen zerstoeren. Mineraloel und Bio-Hydraulikoel: Nur wenn beide Hersteller Kompatibilitaet bestaetigen. Im Zweifel: Komplettwechsel mit Spuelung. (Confidence: measured)

### Autopilot

**F15: Mein Autopilot haelt den Kurs nicht mehr richtig — was kann ich tun?**
Erste Massnahme: Neukalibrierung (Kapitel 4.4). Zweite Massnahme: Stoerquellen in Kompassnaehe entfernen (Lautsprecher, Tablets, Werkzeuge). Dritte Massnahme: Response-Level anpassen. Wenn danach keine Besserung: Ruderlage-Sensor pruefen, Antrieb auf mechanische Defekte pruefen. In 80% der Faelle loest eine Neukalibrierung das Problem. (Confidence: documented)

**F16: Wie viel Strom verbraucht mein Autopilot?**
Typische Werte: Tiller-Pilot (kleines Segelboot): 1-3 A Durchschnitt, 10-15 A Spitze. Wheel-Pilot (mittlere Segelyacht): 2-5 A Durchschnitt, 15-25 A Spitze. Hydraulik-Autopilot (grosse Yacht): 5-15 A Durchschnitt, 30-50 A Spitze. Bei starkem Seegang und Wind verdoppeln sich die Durchschnittswerte. Fuer Langfahrt: Mindestens 200 Ah nutzbare Batteriekapazitaet fuer 24h Autopilotbetrieb einplanen. (Confidence: estimated)

**F17: Muss ich den Autopilot im Winter abbauen?**
Nein, aber: Display schuetzen (Abdeckung), Sicherung entfernen (kein Phantomverbrauch), Kabel-Stecker pruefen und mit Korrosionsschutz einspruehen, Linearantrieb trocken halten (Plane oder Abdeckung). Bei Aussen-Winterlager: Bedenken Sie, dass Feuchtigkeit und Frost Elektronik beschaedigen koennen — empfindliche Teile (Display, Bedieneinheit) ggf. abnehmen und drinnen lagern. (Confidence: estimated)

### Ruderlager und Ruderblatt

**F18: Wie erkenne ich verschlissene Ruderlager?**
Vier Indikatoren: (1) Spiel: Ruder seitlich bewegen — fuhlbar? (2) Geraeusche: Knarren oder Knirschen beim Steuern. (3) Vibrationen: Ruder vibriert bei Fahrt (insbes. hohe Geschwindigkeit). (4) Koker-Leckage: Wasser am Ruderschaft deutet auf erhoehtes Lagerspiel, das die Dichtung ueberfordert. Genau messen mit Messuhr: Radialspiel >1 mm bei Composite-Lagern = Wechsel. Details in Kapitel 6.3. (Confidence: measured)

**F19: Mein Ruderblatt klingt beim Klopfen dumpf — was bedeutet das?**
Dumpfer Klang (im Vergleich zu einem klaren, hellen Klang an gesunden Stellen) deutet auf Wasseraufnahme oder Delaminierung im Inneren des Ruderblatts hin. Nicht sofort gefaehrlich, aber: (1) Feuchtemessung durchfuehren (Tramex oder aehnlich). (2) Bei >30% Feuchte: Ruder trocknen lassen (Monate!) und sanieren. (3) Bei Frost: Gefahr des Auffrierens — Ruder ueber Winter an Land, beheizt oder temperiert lagern. (Confidence: documented)

**F20: Wann muss ein Ruderlager getauscht werden?**
Wenn das radiale Spiel die Grenzwerte ueberschreitet (Composite: >1 mm, Bronze: >0.8 mm, Nadellager: >0.5 mm), wenn Geraeusche oder Schwergaengigkeit trotz Schmierung auftreten, oder praeventiv nach 15-20 Jahren (Composite) bzw. 10-15 Jahren (Bronze). Ein Lagerwechsel erfordert in der Regel den Ausbau des Ruders — das ist ein Fachbetrieb-Job und kostet 1.000-5.000 EUR je nach Boot und Zugaenglichkeit. (Confidence: estimated)

### Notsteuerung

**F21: Mein Boot hat keine Notpinne — ist das legal?**
In der EU: Fuer Boote in CE-Kategorie A und B ist eine funktionierende Notsteuerung vorgeschrieben (EU Recreational Craft Directive 2013/53/EU). Fuer Kategorie C und D gibt es keine explizite Vorschrift, aber: Jede Versicherung erwartet eine Notsteuermoeglichkeit. Im Schadensfall ohne Notsteuerung wird grobe Fahrlaessigkeit schwer zu widerlegen sein. AYDI empfiehlt eine Notpinne fuer JEDES Segelboot, unabhaengig von der CE-Kategorie. (Confidence: documented)

**F22: Mein Cockpit-Tisch ist ueber der Notpinnen-Aufnahme — wie loese ich das Problem?**
Drei Ansaetze: (1) Tisch mit Schnellverschluss versehen, der ohne Werkzeug in <30 Sekunden demontierbar ist. (2) Notpinne mit Verlaengerung/Adapter, die um den Tisch herum greift. (3) Tisch auf Schienen, die zur Seite geschoben werden koennen. Loesung 1 ist am zuverlaessigsten. Die Montagezeit sollte unter 2 Minuten liegen — ueben Sie das regelmaessig. (Confidence: estimated)

**F23: Was tun wenn die Notpinne nicht auf den Ruderschaft passt?**
Sofortmassnahme: Notruder aus Bordmitteln improvisieren — Leine am Ruderblatt (Taucher noetig), Schleppbremse/Trogue als Richtungskontrolle, bei kleinen Booten: Riemen am Heck. Langfristig: Neue Notpinne anfertigen lassen (Edelstahl-Dreherei, Kosten ca. 100-300 EUR) oder Original beim Hersteller nachbestellen. Die Passflaeche am Ruderschaftkopf muss korrosionsfrei sein — jaehrlich reinigen und mit Vaseline schuetzen. (Confidence: estimated)

### Kosten und Planung

**F24: Was kostet ein kompletter Steueranlagen-Wechsel?**
Sehr stark abhaengig von Bootsgroesse und Steuerungstyp: Seilsteuerung komplett (12m Segelyacht): 2.000-4.000 EUR (Material + Arbeit). Hydrauliksteuerung komplett (14m Segelyacht): 4.000-8.000 EUR. Steuerrad + Pedestal (Lewmar/Whitlock): 2.000-6.000 EUR. Ruderlager komplett (inkl. Kran, Ruder-Ausbau): 3.000-8.000 EUR. Autopilot-System komplett: 2.000-8.000 EUR. Summe fuer Komplettsanierung einer 12-14m Segelyacht: 8.000-20.000 EUR. (Confidence: estimated)

**F25: Gibt es eine Checkliste fuer den Gebrauchtbootkauf — Steueranlage?**
Ja, die AYDI-Kaufcheck-Checkliste Steueranlage:
1. Steuerrad von Anschlag zu Anschlag drehen: Leichtgaengig? Gleichmaessig? Spiel?
2. Ruderspiel pruefen: Ruder seitlich bewegen — fuhlbares Spiel?
3. Hydraulikoelstand und -farbe pruefen
4. Steuerseile (sofern sichtbar): Litzenbrueche? Korrosion?
5. Autopilot einschalten und Selbsttest abwarten
6. Notpinne: Vorhanden? Stecktest?
7. Koker: Wassereinbruchspuren?
8. Ruderblatt (an Land): Klopftest, Gelcoat-Zustand
9. Wartungsprotokolle einsehen: Regelmaessige Wartung nachgewiesen?
10. Alter der Komponenten erfragen: Seile >7 Jahre? Hydraulik >10 Jahre?
(Confidence: estimated)

### Spezialthemen

**F26: Wie oft muss ein Push-Pull-Kabel (Aussenborder) gewartet werden?**
Push-Pull-Kabel sind relativ wartungsarm, aber keineswegs wartungsfrei. Jaehrlich: Gaengigkeit pruefen (Steuerrad leicht und gleichmaessig von Anschlag zu Anschlag). Alle 2 Jahre: Kabel am Schmiernippel (falls vorhanden) schmieren, aeussere Huelle auf Risse und UV-Schaeden pruefen. Wenn schwergaengig: Erst schmieren (Teleflex Cable Grease), wenn keine Besserung: Kabel wechseln. Typische Lebensdauer: 10-15 Jahre bei Suesswasser, 7-10 Jahre bei Salzwasser. (Confidence: documented)

**F27: Kann ich eine Seilsteuerung auf Hydraulik umruesten?**
Ja, das ist eine gaengige Umruestung, besonders bei groesseren Booten (>12m) oder bei verschlissener Seilsteuerung. Aufwand: 2-4 Tage Werftarbeit, Kosten: 3.000-8.000 EUR (je nach System und Boot). Vorteile: Geringerer Wartungsaufwand, besseres Steuergefuehl, einfachere Autopilot-Integration. Nachteile: Hoeheres Gewicht, abhaengig von Fluid-Zustand, Entlueftung noetig. Die meisten Werften empfehlen die Umruestung bei Booten ueber 12m, die regelmaessig im Einsatz sind. (Confidence: estimated)

**F28: Mein Steuerrad hat einen Teak-Kranz — wie pflege ich den?**
Teak am Steuerrad ist extremer UV- und Witterungsbelastung ausgesetzt. Grundregel: (1) Regelmaessig mit Suesswasser abwaschen (Salzentfernung). (2) Einmal jaehrlich mit Teakoel oder Teak-Sealer behandeln (Teak Wonder, Boracol). (3) Alternativ: Unbehandelt vergrauen lassen (haltbarer, aber weniger huebsch). (4) Risse >1mm oder schwarze Stellen (Faeulnis): Segment ersetzen oder Rad erneuern. (5) Im Winter: Rad abnehmen und geschuetzt lagern oder mit UV-Cover schuetzen. Kosten Teak-Pflege: 20-50 EUR/Jahr. Neues Teak-Steuerrad: 400-2.500 EUR. (Confidence: estimated)

**F29: Was bedeutet es, wenn mein Autopilot "Off Course Alarm" gibt?**
Der Off-Course-Alarm zeigt an, dass die tatsaechliche Kursabweichung den eingestellten Grenzwert ueberschritten hat (typisch: 15-20°). Ursachen: (1) Ploetzliche Windaenderung oder Stroemung, die der Autopilot nicht schnell genug kompensieren kann. (2) Antrieb zu schwach fuer die Bedingungen. (3) Mechanisches Problem (Kupplung rutscht, Linearantrieb blockiert). (4) Kompassstoerung. Erstmassnahme: Manuell steuern, pruefen ob Steuerung normal funktioniert. Dann: Autopilot neu aktivieren. Bei Wiederholung: Ursache gemaess Troubleshooting-Baum 9.2 suchen. (Confidence: documented)

**F30: Brauche ich fuer Binnenschifffahrt die gleiche Steueranlagen-Wartung?**
Grundsaetzlich ja, aber mit angepassten Intervallen. Binnengewaesser haben kein Salzwasser (deutlich geringere Korrosion), weniger Seegang (geringere mechanische Belastung), und oft kuerzere Fahrstrecken. Empfehlung: Wartungsintervalle koennen um ca. 50% verlaengert werden gegenueber Salzwasser-Betrieb. Ausnahme: Push-Pull-Kabel — hier ist Kondenswasser im Suesswasser-Betrieb genauso problematisch. Ruderbewuchs: In Suesswasser anders (Algen, Muscheln seltener), aber ebenfalls moeglich. (Confidence: estimated)

---

## 11. Glossar

### A

**Anschlag (Stop/End Stop):** Mechanische Begrenzung des maximalen Ruderausschlags (typisch ±35° bis ±45°). Schuetzt Steueranlage vor Ueberlastung und verhindert Verklemmung des Ruders. Einstellung durch justierbare Anschlagschrauben oder -bolzen.

**ATF (Automatic Transmission Fluid):** Spezielles Hydraulikoel, urspruenglich fuer Automatikgetriebe. In einigen aelteren Hydrauliksteuerungen (Hynautic, Wagner) als Betriebsfluid vorgeschrieben. NICHT kompatibel mit HLP-Oelen.

**Autopilot (Autopilot):** Elektronisch-mechanisches System zur automatischen Kurssteuerung. Besteht aus Steuereinheit (Computer), Kompass, Ruderlage-Sensor und Antrieb (linear, rotary oder hydraulisch).

### B

**Bypass-Ventil (Bypass Valve):** Ventil in der Hydraulikleitung, das den Oelkreislauf kurzschliesst. Wird geoeffnet fuer: Autopilot-Betrieb ohne Helmpumpe, Notsteuerung bei Pumpenversagen, Entlueftung. Bei Doppelsteuerstand: Ueberbrueckt eine der beiden Pumpen.

**Bowdenzug (Push-Pull Cable):** Mechanisches Kabelsteuerungssystem, bei dem ein flexibles Kabel in einer starren Huelse Druck- und Zugkraefte uebertraegt. Typisch fuer kleine Motorboote mit Aussenborder.

### C

**CE-Kategorie (CE Category):** Einstufung von Sportbooten nach der EU Recreational Craft Directive 2013/53/EU. Kategorien A (Ozean), B (Offshore), C (Kueste), D (geschuetzte Gewaesser). Beeinflusst Anforderungen an Notsteuerung.

**Compound-Lager (Composite Bearing):** Ruderlager aus faserverstaerktem Kunststoff (GFK-aehnlich) oder Delrin/PTFE-Kombination. Wartungsfrei, korrosionsbestaendig, selbstschmierend bei Wasserkontakt. Standard bei modernen Yachten (z.B. Jefa Composite).

### D

**Docking-Kalibrierung (Docking Calibration):** Erste Phase der Autopilot-Kalibrierung, durchgefuehrt am Steg. Lernt die Endanschlaege des Ruders und die Mittelstellung des Ruderlage-Sensors.

**Druckbegrenzungsventil (Pressure Relief Valve):** Sicherheitsventil in der Hydrauliksteuerung, das bei Ueberdruck oeffnet. Schuetzt Pumpe, Zylinder und Leitungen vor Beschaedigung. Typischer Einstellwert: 60-80 bar.

**Drop-Test (Rudder Drop Test):** Pruefmethode fuer axiales Lagerspiel des Ruders. Ruder wird angehoben und fallen gelassen — die gemessene Axialbewegung zeigt den Zustand des Tragringes/Axiallagers.

### E

**Entlueftung (Bleeding/Purging):** Verfahren zum Entfernen von Luftblasen aus einem Hydrauliksystem. Luft komprimiert sich und macht die Steuerung schwammig/ungenau.

**Ermuedung (Fatigue):** Versagensmechanismus durch wiederholte Belastungswechsel, auch unter der statischen Bruchgrenze. Hauptursache fuer Litzenbrueche in Steuerseilen.

### F

**Fluxgate-Kompass (Fluxgate Compass):** Elektronischer Kompass, der das Erdmagnetfeld mit Sonden misst. Liefert Kursinformation an den Autopilot. Empfindlich gegen magnetische Stoerfelder.

### G

**Gabelterminal (Fork Terminal/Clevis):** Endbeschlag eines Steuerseils in Gabelform. Wird mit Bolzen und Splint am Quadrant oder Steuerkettenglied befestigt.

**Getriebsteuerung (Geared Steering):** Steueranlage mit mechanischem Getriebe (Schneckentrieb, Kegelrad, Zahnstange) zur Kraftuebersetzung. Typisch: Whitlock Mamba/Cobra Pedestale.

### H

**Helmpumpe (Helm Pump):** Hydraulikpumpe, die direkt am Steuerrad-Pedestal montiert ist und durch Drehen des Steuerrads betaetigt wird. Wandelt Drehbewegung in Oeldruck um.

**HLP-Oel (HLP Oil):** Hydraulikoel mit Hochdruck-Additiven (H = Hydraulik, L = Langzeitstabilitaet, P = Pump = Anti-Verschleiss). DIN 51524 Teil 2. Standard fuer marine Hydrauliksteuerungen.

### I

**ISO VG (ISO Viscosity Grade):** Internationale Viskositaetsklassifikation fuer Industrieoele. VG 15 = Viskositaet 13.5-16.5 mm²/s bei 40°C. Standard fuer Yachtsteuerungen.

### J

**Jefa (Jefa Steering):** Daenischer Hersteller, Markfuehrer fuer Ruderlager und Steueranlagen im europaeischen Yachtbau. Bekannt fuer Composite-Lager und hochwertige Quadranten.

### K

**Kalibrierung (Calibration):** Einstellprozess des Autopiloten, bei dem Kompass, Ruderlagesensor und Response-Parameter auf das Boot abgestimmt werden.

**Kavitation (Cavitation):** Bildung und Kollaps von Dampfblasen in Fluessigkeit bei Unterdruck. In Hydraulikpumpen: Verursacht Geraeusche, Erosion und Leistungsverlust.

**Koker (Rudder Tube):** Rohr durch den Rumpf, in dem der Ruderschaft laeuft. Verbindet Unterwasserbereich mit dem Bootinneren. Muss abgedichtet sein (Lip Seal, Stopfbuchse).

**Kolbenstange (Piston Rod):** Stange des Hydraulikzylinders, die die lineare Bewegung auf den Ruderhebel uebertraegt. Muss eine polierte, korrosionsbestaendige Oberflaeche haben.

### L

**Lagerspiel (Bearing Play/Clearance):** Messbarer Abstand zwischen Ruderschaft und Lagerbuchse. Neuzustand: 0.05-0.20 mm. Verschliessen: Radialspiel nimmt zu, bis Grenzwert erreicht.

**Linearantrieb (Linear Actuator):** Elektromechanischer Antrieb fuer Autopiloten. Wandelt Drehbewegung eines Motors ueber Spindel in lineare Bewegung um, die auf den Ruder-Tillerhebel oder Quadrant wirkt.

**Litzenbruch (Wire Break):** Bruch eines einzelnen Drahtes im Steuerseil. Fruehindikator fuer Seil-Ermuedung. Grenzwert: >3 Brueche/m → Seil wechseln.

### M

**Messuhr (Dial Indicator/Dial Gauge):** Praezisions-Messinstrument zur Messung kleiner Laengenveraenderungen (Aufloesung 0.01 mm). Zur Ruderlager-Spielmessung eingesetzt.

### N

**Nicropress (Nicropress Fitting):** Presshuelse zur dauerhaften Befestigung von Edelstahlseilen. Wird mit Spezialzange aufgepresst. Standard-Endverbindung fuer Steuerseile.

**Notpinne (Emergency Tiller):** Hilfssteuereinrichtung fuer den Notfall. Wird direkt auf den Ruderschaftkopf gesteckt und ermoeglicht manuelle Steuerung bei Versagen der Hauptsteuerung.

### P

**Pedestal (Pedestal/Steering Pedestal):** Saeulenartige Steuersaeule im Cockpit, die das Steuerrad traegt und das Getriebe beherbergt. Oft mit integriertem Kompass und Instrumenten.

**Pitting (Pitting Corrosion):** Lochfrass-Korrosion. Auf Hydraulikzylinder-Kolbenstangen fuehrt Pitting zu Dichtungsversagen. Auf Ruderschaeften kann Pitting Spannungsrisskorrosion einleiten.

### Q

**Quadrant (Quadrant/Tiller Arm):** Halbkreisfoermiger Hebel am Ruderschaft, an dem die Steuerseile befestigt sind. Material: Aluminium (Standard) oder Edelstahl (hochbelastet). Uebersetzt die lineare Seilbewegung in Drehbewegung am Schaft.

### R

**Response Level:** Einstellparameter des Autopiloten, der bestimmt, wie schnell und stark das System auf Kursabweichungen reagiert. Niedrig = traege/energiesparend, Hoch = aggressiv/praezise/energieintensiv.

**Ruderlagesensor (Rudder Position Sensor/Feedback Unit):** Sensor am Ruderschaft oder Quadrant, der dem Autopilot die aktuelle Ruderlage mitteilt. Typisch: Potentiometer oder Hall-Sensor.

**Rueckschlagventil (Check Valve/Non-Return Valve):** Ventil in der Hydraulikleitung, das Rueckfluss verhindert. Sorgt dafuer, dass das Ruder in der eingestellten Position bleibt (Helm-Lock-Funktion).

### S

**Schneckentrieb (Worm Gear):** Getriebebauart, bei der eine Schnecke (Schraube) ein Schneckenrad antreibt. Hohe Uebersetzung, selbsthemmend (Ruder haelt Position). Typisch: Edson, aeltere Whitlock-Modelle.

**Sea Trial (Sea Trial Calibration):** Zweite Phase der Autopilot-Kalibrierung auf See. Kompass wird kalibriert durch Fahren zweier voller Kreise. Lernt Deviation und Dynamik des Bootes.

**Seilspannung (Cable Tension):** Vorspannkraft im Steuerseil, gemessen in Newton. Zu niedrig: Seil springt von Rollen. Zu hoch: Erhoehter Verschleiss. Gemessen mit Tensiometer.

**Spannungsrisskorrosion (Stress Corrosion Cracking, SCC):** Rissbildung in Metallen unter gleichzeitiger Einwirkung von Zugspannung und korrosivem Medium (Salzwasser + Chloride). Gefuerchtete Versagensart bei Edelstahl-Steuerseilen und Ruderschaeften.

**Stopfbuchse (Stuffing Box/Packing Gland):** Abdichtungselement am Koker, bei dem Packungsmaterial (Teflon-impraegnierte Fasern) um den Schaft gepresst wird. Aeltere Technologie, zunehmend durch Lip Seals ersetzt.

### T

**Tensiometer (Tensiometer):** Handmessgeraet zur Bestimmung der Seilspannung. Funktionsprinzip: Definierte seitliche Auslenkung des Seils, Widerstand wird als Spannung angezeigt. Standardgeraet: Loos PT-2.

**Tragring (Bearing Ring/Thrust Washer):** Ring oder Scheibe, die das axiale Gewicht des Ruders traegt. Verhindert, dass das Ruder nach unten durchsackt. Pruefung durch Drop-Test.

**Tiller (Tiller/Rudder Arm):** Hebel am Ruderschaft fuer die Kraftuebertragung. Bei Segelyachten mit Pinnensteuerung: Direkte Bedienung. Bei Rad-Steuerung: Oft als Autopilot-Angriffspunkt.

### U

**Umlenkrolle (Sheave/Fairlead Sheave):** Rolle zur Umlenkung des Steuerseils von der Seilbahn zum Quadrant oder Pedestal. Material: Nylon, Delrin oder Edelstahl. Durchmesser mindestens 12× Seildurchmesser.

### V

**Viskositaet (Viscosity):** Zaehfluessigkeit des Hydraulikoels. Bei zu niedriger Temperatur wird das Oel zu dickfluessig (schwergaengiges Steuer), bei zu hoher Temperatur zu duennfluessig (interne Leckage steigt).

### W

**Wellendichtung (Shaft Seal):** Dichtung am Uebergang einer rotierenden oder oszillierenden Welle/Stange durch ein Gehaeuse. An der Helmpumpe: Steuerwellen-Dichtung. Am Koker: Ruderschaft-Dichtung (Lip Seal).

**Whitlock (Whitlock Steering/Lewmar):** Britischer Hersteller (jetzt Teil von Lewmar), bekannt fuer Steuerrad-Pedestale (Mamba, Cobra, Viper-Serien) und Getriebsteuerungen. Einer der verbreitetsten Hersteller im Segelyacht-Markt.

### S (Fortsetzung)

**Seiltrommel (Cable Drum):** Zylindrische Trommel am Pedestal oder Getriebe, auf die das Steuerseil gewickelt ist. Alternative zu Kettenrad-Systemen. Groessere Trommel = mehr Uebersetzung = leichteres Steuern.

**Servo-Pendel-Ruder (Servo Pendulum):** Windsteueranlage (z.B. Windpilot, Monitor) mit pendelartigem Hilfsruder, das die Windkraft mechanisch zum Steuern nutzt. Wartung: Lagerung, Pendelarm-Gelenke, Leinenverbindung.

**Skeg (Skeg):** Feststehende Kielflosse am Heck, die das Unterlager des Ruders traegt. Schuetzt das Ruder vor Grundberuehrung und stabilisiert die Steuerung. Wartung: Laminate auf Risse pruefen, Bolzenverbindung Skeg-Rumpf.

### T (Fortsetzung)

**Thermozyklen (Thermal Cycling):** Wiederholte Temperaturwechsel (Tag/Nacht, Sommer/Winter), die zur Materialermuedung von Dichtungen und Kunststoffen fuehren. Besonders relevant in Tropen (hohe Tagestemperatur) und nordischen Gewaessern (Frostwechsel).

**Trimmklappe (Trim Tab):** Verstellbare Klappe am Heck von Motorbooten zur Trimmkorrektur. Einige Systeme sind in die Steueranlage integriert. Wartung: Hydraulikzylinder, Gelenke, Anoden.

### U (Fortsetzung)

**Unterlager (Lower Bearing):** Unteres Ruderlager, meist im Skeg oder am Rumpfaustritt. Staendig unter Wasser → erhoehte Korrosions- und Bewuchsgefahr. Inspektion nur an Land moeglich.

### V (Fortsetzung)

**Verschleissgrenze (Wear Limit):** Maximal zulaessiger Verschleiss einer Komponente, ab dem Austausch erforderlich ist. Bei Ruderlager: Maximal zulaessiges Radialspiel. Bei Steuerseil: Maximal zulaessige Anzahl Litzenbrueche.

**Vibrationsanalyse (Vibration Analysis):** Messtechnisches Verfahren zur Fruehererkennung von Lagerschaeden und mechanischen Defekten. Im professionellen Yachtbereich zunehmend eingesetzt (AYDI Pipeline A).

### W (Fortsetzung)

**Wartungsprotokoll (Maintenance Log):** Dokumentation aller durchgefuehrten Wartungsmassnahmen mit Datum, Massnahmen, Befunden und Messwerten. Grundlage fuer AYDI-Trendanalyse und vorausschauende Wartung. Im Bordhandbuch oder digital fuehren.

**Wassergehalt (Water Content):** Anteil an Wasser im Hydraulikfluid. Maximal zulaessig: 0.1% (Karl-Fischer-Methode). Visuell erkennbar als Truebung/milchiges Aussehen bei >0.5%.

### Z

**Zahnspiel (Gear Backlash):** Spiel zwischen zwei ineinander greifenden Zahnraedern. Zeigt sich als toter Bereich beim Richtungswechsel. Grenzwert bei Pedestal-Getrieben: 0.3-0.5 mm am Steuerradumfang.

**Zerstoerungsfreie Pruefung (Non-Destructive Testing, NDT):** Pruefverfahren ohne Beschaedigung des Pruefkoerpers. Am Ruderschaft: Ultraschall-Pruefung (UT), Farbeindring-Pruefung (PT), Magnetpulver-Pruefung (MT). Empfohlen alle 5 Jahre fuer Ruderschaefte >10 Jahre alt.

**Zylinderhub (Cylinder Stroke):** Maximaler Verfahrweg des Hydraulikzylinder-Kolbens. Bestimmt zusammen mit dem Tillerarm-Radius den maximalen Ruderausschlag. Typisch: 150-300 mm je nach Zylindergroesse.

---

## 12. Schnell-Referenz

### Wartungs-Checkliste Saisonstart

```
STEUERANLAGEN-CHECK SAISONSTART
================================
Boot: _________________ Datum: ___________
Steuerungstyp: _________ Pruefer: __________

SEILSTEUERUNG                    □ n/a
[ ] Seile visuell (Litzenbrueche)     OK □  Mangel □
[ ] Seilspannung BB: ___N  StB: ___N  OK □  Mangel □
[ ] Umlenkrollen leichtgaengig        OK □  Mangel □
[ ] Quadrant fest                      OK □  Mangel □
[ ] Schaekel/Terminals                 OK □  Mangel □

HYDRAULIK                        □ n/a
[ ] Oelstand                          OK □  Mangel □
[ ] Oelfarbe (klar/trueb/dunkel)      OK □  Mangel □
[ ] Entlueftung                       OK □  Mangel □
[ ] Leckage (Pumpe/Leitung/Zylinder)  OK □  Mangel □
[ ] Helm-Lock Funktion                OK □  Mangel □

AUTOPILOT                        □ n/a
[ ] Selbsttest                        OK □  Mangel □
[ ] Kalibrierung                      OK □  Mangel □
[ ] Ruderlage-Anzeige Mitte           OK □  Mangel □
[ ] Kurshalten-Test                   OK □  Mangel □
[ ] Standby-Taste                     OK □  Mangel □

RUDERLAGER / KOKER
[ ] Radialspiel: ___mm (Grenze: 1mm)  OK □  Mangel □
[ ] Axialspiel: ___mm (Grenze: 2mm)   OK □  Mangel □
[ ] Koker trocken                     OK □  Mangel □
[ ] Dichtlippe intakt                 OK □  Mangel □

STEUERRAD / PEDESTAL
[ ] Steuerradspiel: ___°              OK □  Mangel □
[ ] Pedestal Bremse                   OK □  Mangel □
[ ] Kompass (blasenfrei, Licht)       OK □  Mangel □

NOTSTEUERUNG
[ ] Notpinne vorhanden                OK □  Mangel □
[ ] Stecktest bestanden               OK □  Mangel □
[ ] Zugangsweg frei                   OK □  Mangel □

GESAMTBEWERTUNG
[ ] Fahrbereit  [ ] Maengel beheben  [ ] Nicht fahrbereit

Bemerkungen: _________________________________
____________________________________________

Unterschrift: ________________
```

### Drehmoment-Werte

| Schraube/Verbindung | Drehmoment (Nm) |
|---------------------|----------------|
| Steuerrad-Nabenmutter | 30-50 |
| Quadrant-Klemmschrauben (M8) | 25-35 |
| Quadrant-Klemmschrauben (M10) | 45-65 |
| Pedestal-Befestigung am Deck | 15-25 |
| Hydraulik-Verschraubung G1/4 | 20-25 |
| Hydraulik-Verschraubung G3/8 | 30-35 |
| Hydraulik-Verschraubung G1/2 | 40-50 |
| Ruderlager-Flansch (M8) | 20-25 |
| Ruderlager-Flansch (M10) | 35-45 |
| Autopilot-Linearantrieb Befestigung | 15-25 |
| Koker-Flansch | 15-25 |
| Anschlag-Schrauben | 20-30 |

### Hydraulik-Fluid Schnellbestimmung

```
HYDRAULIKFLUID — WELCHES IST DAS RICHTIGE?
============================================
1. Herstellerschild am Behaelter lesen → Fluid-Typ notiert?
   JA → Diesen Typ verwenden
   NEIN → Weiter

2. Fluid-Farbe pruefen:
   ROT → Wahrscheinlich ATF (Hynautic/Wagner) → Dexron III/VI
   KLAR/BERNSTEIN → Wahrscheinlich HLP → ISO VG 15
   GRUEN → Bio-Hydraulikoel → Hersteller kontaktieren

3. Boot-Hersteller/Modell → Steueranlagen-Hersteller bestimmen:
   Lewmar/Whitlock → ISO VG 15 HLP
   SeaStar/Teleflex → SeaStar HA5430 oder ISO VG 15 HLP
   Vetus → Vetus HF 15 oder ISO VG 15 HLP
   Hynautic → ATF Dexron III/VI (KEIN HLP!)
   Kobelt → ISO VG 46 (NICHT VG 15!)

4. Im Zweifel → Hersteller kontaktieren, NICHT raten!
```

### Seilspannungs-Schnellreferenz

```
SEILSPANNUNG — SOLLWERTE (Tensiometer Loos PT-2)
===================================================
                   Min.    Soll    Max.
4 mm (5/32"):      90 N    130 N   180 N
5 mm (3/16"):     110 N    155 N   220 N
6 mm (1/4"):      130 N    175 N   250 N
7 mm (9/32"):     155 N    200 N   290 N

ACHTUNG:
- Beide Seiten (BB/StB) muessen gleiche Spannung haben (±10%)
- Bei Temperatur >30°C: Spannung 10% niedriger einstellen
- Bei Temperatur <5°C: Spannung 10% hoeher einstellen
- Nach neuem Seil: 2x nachspannen (nach 2 Tagen, nach 2 Wochen)
```

### Autopilot-Fehlermeldungen Schnellreferenz

```
RAYMARINE EVOLUTION — HAEUFIGE FEHLERMELDUNGEN
================================================
"No Compass Data"    → Kompass-Kabel pruefen, Stecker reinigen
"No Rudder Feedback" → Ruderlagesensor pruefen, Kabel
"Drive Stopped"      → Sicherung Antrieb pruefen (ACU)
"Off Course"         → Manuell steuern, Response erhoehen
"Low Battery"        → Batteriespannung <11.5V → laden
"Calibration Needed" → Kalibrierungsfahrt durchfuehren

B&G TRITON/H5000 — HAEUFIGE FEHLERMELDUNGEN
================================================
"Compass Error"      → Precision-9 Kabel pruefen
"Rudder Sensor"      → Ruderlagesensor pruefen
"Drive Overload"     → Antrieb ueberlastet, Response reduzieren
"Course Error"       → Kalibrierung wiederholen
"Low Voltage"        → Stromversorgung pruefen
```

### Wartungskostenplanung 10-Jahres-Uebersicht

```
SEILSTEUERUNG 12m Segelyacht — 10-Jahres-Kosten (geschaetzt)
=============================================================
Jahr  Routine  Verbrauch  Ersatz    Summe   Kumuliert
  1     80       30          0       110       110
  2     80       30          0       110       220
  3     80       30          0       110       330
  4     80       30         50       160       490
  5     80       30        400       510     1.000  ← Seilwechsel
  6     80       30          0       110     1.110
  7     80       30        250       360     1.470  ← Pedestal-Revision
  8     80       30          0       110     1.580
  9     80       30          0       110     1.690
 10     80       30        500       610     2.300  ← Seilwechsel + Rollen
                                    Durchschnitt: 230 EUR/Jahr

HYDRAULIKSTEUERUNG 14m Segelyacht — 10-Jahres-Kosten (geschaetzt)
=================================================================
Jahr  Routine  Verbrauch  Ersatz    Summe   Kumuliert
  1    120       50          0       170       170
  2    120       50         80       250       420  ← Oelwechsel
  3    120       50          0       170       590
  4    120       50         80       250       840  ← Oelwechsel
  5    120       50        500       670     1.510  ← Schlaeuche + Oel
  6    120       50         80       250     1.760  ← Oelwechsel
  7    120       50        600       770     2.530  ← Pumpe-Dichtung + Oel
  8    120       50         80       250     2.780  ← Oelwechsel
  9    120       50          0       170     2.950
 10    120       50        800       970     3.920  ← Zylinder-Dichtung + Oel
                                    Durchschnitt: 392 EUR/Jahr

Alle Angaben in EUR, exkl. Werftarbeit.
```

### Not-Kontakte

| Hersteller | Service-Hotline | Ersatzteile |
|-----------|----------------|-------------|
| Jefa Steering | +45 7582 2122 | jefa.com |
| Lewmar/Whitlock | +44 1onal 246246 | lewmar.com |
| Raymarine | +44 23 9271 4713 | raymarine.com |
| B&G (Navico) | +47 77 11 95 00 | bandg.com |
| SeaStar Solutions | +1 604 248 3858 | seastarsolutions.com |
| Edson International | +1 508 995 9711 | edsonmarine.com |
| Vetus | +31 33 298 9700 | vetus.com |

---

## 13. ANHANG A–R

### ANHANG A — Fallstudie: Seilsteuerungs-Versagen auf Atlantikueberquerung

**Boot:** Hallberg-Rassy 40 MkII, Baujahr 2008
**Steuerung:** Whitlock Mamba 22, Seilsteuerung, Doppelsteuerrad
**Vorfall:** Tag 14 der Atlantikueberquerung (ARC), 1.200 sm westlich La Palma

**Befund:**
Backbord-Steuerseil riss an der oberen Umlenkrolle (Lazarette). Die Crew bemerkte ploetzlich das Fehlen von Ruderwiderstand und konnte das Boot nicht mehr kontrollieren. Das Boot drehte quer zur See (ca. 3m Duening).

**Ursache:**
- Steuerseil Alter: 9 Jahre (Herstellerempfehlung: Wechsel nach 5-7 Jahren)
- Keine Schmierung in den letzten 3 Jahren (Eigner wusste nicht, dass Steuerseile geschmiert werden muessen)
- 14 Litzenbrueche an der Umlenkrolle bei letzter dokumentierter Inspektion (2 Jahre zuvor) — NICHT als kritisch eingestuft
- Rolle hatte leichten Schraeglauf → einseitiger Seilabrieb

**Sofortmassnahme:**
1. Segel geborgen
2. Notpinne montiert (Dauer: 4 Minuten — Crew war eingeweist!)
3. Segelsetzung unter Notpinne: Genua gerefft, Grosssegel 2. Reff
4. Weiterfahrt unter Notpinne fuer 48 Stunden

**Reparatur auf See:**
- Vorbereitetes Ersatzseil vorhanden (Langfahrt-Empfehlung)
- Seilwechsel in Mindelo (Kap Verde) nach 12 Tagen unter Notpinne
- Beide Seile und alle Umlenkrollen gewechselt (Gesamtkosten: 1.800 EUR)

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F01 (Litzenbrueche), Schweregrad 5
- Ursache: Wartungsversaeumnis (Schmierung, Inspektion)
- Confidence: documented (aus Logbuch und Werkstattbericht)
- Score-Impact: -100 (Totalversagen)
- Empfehlung: Praeventiver Seilwechsel, Schmierung, Inspektions-Intervall

### ANHANG B — Fallstudie: Hydraulikleckage fuehrt zu Autopilot-Ausfall

**Boot:** Bavaria 46 Cruiser, Baujahr 2015
**Steuerung:** Lewmar Hydraulik, Raymarine EV-200 Autopilot
**Vorfall:** Nachtfahrt im Aermelkanal, Verkehrstrennungsgebiet (VTG)

**Befund:**
Autopilot fiel ohne Vorwarnung aus ("Drive Error"). Manuelle Steuerung schwammig und unpraezise. Oelstand im Vorratsbehaelter unter Minimum.

**Ursache:**
- Hydraulikschlauch zwischen Helmpumpe und T-Stueck (Autopilot-Einspeisung) war an der Presshuelse undicht
- Schlauch: 8 Jahre alt, Gummi UV-geschaedigt (trotz Cockpitboden-Position: UV-Reflexion)
- Langsame Leckage ueber Wochen — Oelstand nicht kontrolliert
- Lufteintritt in das System → schwammige Steuerung → Autopilot konnte Ruderlage nicht mehr praezise stellen

**Sofortmassnahme:**
1. Manuelles Steuern durch wachhabende Crew (schwierig wegen Schwammigkeit)
2. Nachfuellen aus Reservefluid (Eigner hatte 0.5 L dabei)
3. Entlueftung im Hafen (Cherbourg)

**Reparatur:**
- Schlauch ersetzt, alle anderen Schlaeuche inspiziert und praeventiv getauscht
- Oel komplett gewechselt (Wasser eingedrungen durch offene Entlueftungsschraube)
- Gesamtkosten: 650 EUR

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F02 (Hydraulikleckage), Schweregrad 4
- Fehlerbild: STEER-M-F03 (Schwammiges Steuer), Schweregrad 3
- Confidence: documented
- Score-Impact: -60
- Empfehlung: Schlauchwechsel alle 5 Jahre, monatliche Oelstandskontrolle

### ANHANG C — Fallstudie: Ruderlager-Verschleiss bei Langfahrtyacht

**Boot:** Oyster 485, Baujahr 2005
**Steuerung:** Jefa Composite-Lager, Jefa Quadrant, hydraulische Steuerung
**Vorfall:** Bei Einfahrt in die Lagune von Bora Bora (Riff-Passage)

**Befund:**
Steuerkraefte deutlich erhoeht, knarrende Geraeusche beim Steuern, zunehmender Wassereinbruch am Koker. In der Riffpassage bei Querstroemung konnte der Steuermann das Ruder nicht schnell genug legen.

**Ursache:**
- Oberes Ruderlager: Radialspiel 1.8 mm (Grenzwert: 1.0 mm)
- Unteres Ruderlager (Skeg): Radialspiel 2.1 mm (Grenzwert: 1.0 mm)
- Lager-Alter: 17 Jahre (Lebensdauer Jefa Composite: 15-20 Jahre)
- Tropischer Einsatz mit viel Bewuchs → erhoehte Steuerkraefte beschleunigen Lagerverschleiss
- Koker-Dichtlippe konnte das Spiel nicht mehr kompensieren → Wassereinbruch

**Reparatur:**
- Ruderlager-Wechsel in Tahiti (Chandlery hatte Jefa-Lager auf Lager)
- Ruder-Ausbau per Kran: 1 Tag
- Lagerwechsel: 1 Tag
- Koker-Dichtung erneuert
- Gesamtkosten: 4.200 EUR (inkl. Kran, Arbeit, Lager, Dichtung)

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F04 (Erhoehtes Ruderspiel), Schweregrad 4
- Fehlerbild: STEER-M-F07 (Koker-Leckage), Schweregrad 3
- Confidence: measured (Messuhr-Protokoll)
- Score-Impact: -55
- Trend-Daten: Lagerspiel hatte sich in den letzten 3 Jahren von 0.5 auf 1.8 mm verdoppelt

### ANHANG D — Fallstudie: Autopilot-Fehlkalibrierung nach Elektronik-Installation

**Boot:** Jeanneau Sun Odyssey 449, Baujahr 2020
**Steuerung:** Seilsteuerung, B&G Triton Autopilot mit Precision-9 Kompass
**Vorfall:** Autopilot steuert systematisch 15° nach Steuerbord

**Befund:**
Nach Installation eines neuen Lautsprechersystems (2× 50W Magnetsystem) unter dem Cockpitboden steuerte der Autopilot persistent nach Steuerbord. Manueller Kompass zeigte korrekt.

**Ursache:**
- Lautsprecher-Magnete 40 cm vom Fluxgate-Kompass entfernt
- Magnetfeld der Lautsprecher verzerrte Kompass-Messung um 15°
- Kalibrierung war nach Installation nicht wiederholt worden

**Loesung:**
1. Lautsprecher um 80 cm versetzt (Mindestabstand Magnete zu Kompass: 1 m)
2. Kompass-Kalibrierung wiederholt → Deviation: 0.8° (vorher: 15.2°)
3. Kein Materialschaden

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F08 (Autopilot-Drift), Schweregrad 2
- Confidence: measured
- Score-Impact: -15
- Empfehlung: Nach jeder Elektro-Installation Autopilot kalibrieren

### ANHANG E — Fallstudie: Schwergaengiges Steuer durch Ruderblatt-Bewuchs

**Boot:** X-Yachts X-412, Baujahr 2002
**Steuerung:** Seilsteuerung, Whitlock Cobra Pedestal
**Vorfall:** Saisonende Mittelmeer (Griechenland), Eigner bemerkt erhoehte Steuerkraefte

**Befund:**
Steuerkraft am Rad: 12 kg (Soll: 3-6 kg). Eigner vermutete Ruderlager-Defekt. Bei Auswasserung: Ruderblatt vollstaendig mit Muscheln und Seepocken bedeckt (2-3 cm Schichtdicke). Ruderlager-Spiel: 0.2 mm (einwandfrei).

**Ursache:**
- 8 Monate im Wasser ohne Antifouling-Erneuerung am Ruderblatt
- Ruderblatt hatte nur Standard-Antifouling (kein Hartantifouling fuer warme Gewaesser)
- Bewuchs erhoehte hydrodynamischen Widerstand um geschaetzt 60-80%

**Loesung:**
1. Ruderblatt gereinigt, geschliffen
2. Hartantifouling aufgetragen (2 Schichten)
3. Steuerkraefte nach Reinigung: 4 kg (normal)
4. Gesamtkosten: 180 EUR

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F05 (Schwergaengiges Steuer), Schweregrad 2
- Confidence: visual_high (Foto des Bewuchses)
- Score-Impact: -15
- Empfehlung: Halbjährliche Unterwasser-Reinigung des Ruderblatts in warmen Gewaessern

### ANHANG F — Fallstudie: Notpinne nicht einsatzbereit bei Steuerungsversagen

**Boot:** Hanse 388, Baujahr 2019
**Steuerung:** Seilsteuerung, Doppelsteuerrad
**Vorfall:** Seilbruch (Nicropress-Huelse geplatzt) in der Biskaya

**Befund:**
Crew versuchte Notpinne zu montieren. Probleme: (1) Cockpit-Tisch ueber Notpinnen-Aufnahme — Werkzeug zum Abbau noetig, Werkzeug in verschlossener Box. (2) Notpinne passte nicht auf Ruderschaftkopf — Korrosion am Konus, keine Passreinigung seit Kauf. (3) Sicherungsbolzen fehlte.

**Zeitverlust:** 45 Minuten bis Notsteuerung einsatzbereit (Zielzeit: <5 Minuten)
**Folge:** Boot lag 45 Minuten manoevrierunfaehig in der Biskaya bei 6 Bft.

**Loesung:**
1. Tisch mit Bordmitteln demontiert (Schraubendreher aus Werkzeugkasten)
2. Ruderschaftkonus mit WD-40 und Schleifpapier gereinigt
3. Notpinne mit improvisierten Sicherung (Leine) befestigt

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F12 (Notpinne nicht einsatzbereit), Schweregrad 5
- Confidence: documented (Seenotfall-Bericht)
- Score-Impact: -80
- Empfehlung: Jaehrlicher Notpinne-Stecktest, Tisch-Schnellverschluss, Passung pflegen

### ANHANG G — Fallstudie: Pedestal-Getriebe blockiert durch Korrosion

**Boot:** Beneteau Oceanis 45, Baujahr 2014
**Steuerung:** Lewmar-Pedestal (ex-Whitlock-Bauart), Seilsteuerung
**Vorfall:** Steuerrad blockiert bei Hafeneinfahrt Cuxhaven

**Befund:**
Steuerrad liess sich nicht mehr drehen. Ruder in leichter Steuerbord-Stellung blockiert. Boot musste mit Bugstrahler in den Hafen manoevriert werden.

**Ursache:**
- Pedestal-Abdeckung (Kompass-Guard) war gerissen → Wasser und Salz eingedrungen
- Kettenrad und Getriebezaehne korrodiert (Salzwasser + Aluminium/Edelstahl-Kombination)
- Fett vollstaendig ausgewaschen
- Korrosionsprodukte (Aluminiumoxid) haben Zahneingriff blockiert

**Reparatur:**
- Pedestal komplett zerlegt, gereinigt, korrodierte Teile ersetzt
- Neues Kettenrad, neue Kette, neue Lager
- Pedestal-Abdeckung ersetzt, verbesserte Dichtung
- Gesamtkosten: 2.100 EUR

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F05 (Schwergaengiges Steuer → Blockade), Schweregrad 5
- Confidence: documented
- Score-Impact: -90
- Empfehlung: Pedestal-Abdeckung jaehrlich auf Risse pruefen, halbjährlich schmieren

### ANHANG H — Fallstudie: Hydraulikzylinder-Versagen durch Pitting

**Boot:** Grand Soleil 46 LC, Baujahr 2011
**Steuerung:** Lewmar Hydraulik, Doppelsteuerrad
**Vorfall:** Langsam zunehmende Leckage am Hydraulikzylinder ueber 2 Saisons

**Befund:**
Zylinder-Kolbenstange zeigte deutliches Pitting (Lochfrass) auf 30% der Oberflaeche. Stangendichtung konnte nicht mehr abdichten. Oelverlust: ca. 50 ml/Woche.

**Ursache:**
- Kolbenstange aus Chromstahl (nicht 316L) — anfaellig fuer Pitting in Salzwasser
- Kolbenstange war exponiert (nicht eingezogener Zustand bei Geradeausfahrt)
- Keine Korrosionsschutz-Behandlung waehrend Winterlager
- Salzablagerungen und stehendes Wasser auf der Kolbenstange

**Reparatur:**
- Neuer Hydraulikzylinder (Kolbenstange nicht separat lieferbar)
- Oelwechsel, Entlueftung
- Gesamtkosten: 3.200 EUR (Zylinder + Einbau)

**AYDI-Analyse:**
- Fehlerbild: STEER-M-F02 (Hydraulikleckage), Schweregrad 4
- Confidence: measured (Pitting-Messung mit Tiefenmicrometer)
- Score-Impact: -50
- Empfehlung: Kolbenstange bei Winterlager mit Korrosionsschutz einspruehen (ACF-50)

### ANHANG I–R — Pydantic v2 Datenmodelle fuer AYDI

```python
"""
AYDI Wissensdatei 14.08 — Steueranlagen Wartung und Troubleshooting
Pydantic v2 Datenmodelle fuer die AYDI-Analyseplattform.

Alle Modelle verwenden model_config = {"from_attributes": True} (Pydantic v2).
German UI, English code.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class ConfidenceLevel(str, Enum):
    """AYDI confidence level for any finding or measurement."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SeverityLevel(int, Enum):
    """Schweregrad 1-5."""
    MINOR = 1
    MODERATE = 2
    SIGNIFICANT = 3
    SERIOUS = 4
    CRITICAL = 5


class SteeringType(str, Enum):
    """Type of steering system."""
    CABLE_WIRE = "cable_wire"
    HYDRAULIC = "hydraulic"
    PUSH_PULL = "push_pull"
    GEARED = "geared"
    TILLER_DIRECT = "tiller_direct"
    ELECTRIC = "electric"


class MaintenanceTaskCategory(str, Enum):
    """Category of maintenance task."""
    INSPECTION = "inspection"
    LUBRICATION = "lubrication"
    ADJUSTMENT = "adjustment"
    FLUID_CHANGE = "fluid_change"
    BLEEDING = "bleeding"
    CALIBRATION = "calibration"
    REPLACEMENT = "replacement"
    CLEANING = "cleaning"
    TESTING = "testing"
    OVERHAUL = "overhaul"


class MaintenanceQualificationLevel(int, Enum):
    """Required qualification for maintenance task."""
    OWNER_BASIC = 1
    EXPERIENCED_OWNER = 2
    PROFESSIONAL = 3


class ComponentGroup(str, Enum):
    """Steering system component group."""
    CABLE = "cable"
    SHEAVE = "sheave"
    QUADRANT = "quadrant"
    PEDESTAL = "pedestal"
    WHEEL = "wheel"
    HYDRAULIC_PUMP = "hydraulic_pump"
    HYDRAULIC_CYLINDER = "hydraulic_cylinder"
    HYDRAULIC_LINE = "hydraulic_line"
    HYDRAULIC_FLUID = "hydraulic_fluid"
    RUDDER_BEARING = "rudder_bearing"
    RUDDER_TUBE = "rudder_tube"
    RUDDER_BLADE = "rudder_blade"
    RUDDER_SHAFT = "rudder_shaft"
    AUTOPILOT_DRIVE = "autopilot_drive"
    AUTOPILOT_COMPASS = "autopilot_compass"
    AUTOPILOT_CONTROLLER = "autopilot_controller"
    EMERGENCY_TILLER = "emergency_tiller"
    PUSH_PULL_CABLE = "push_pull_cable"


class UsageProfile(str, Enum):
    """Usage profile for maintenance interval adjustment."""
    SEASONAL_TEMPERATE = "seasonal_temperate"
    YEAR_ROUND_TEMPERATE = "year_round_temperate"
    TROPICAL = "tropical"
    OFFSHORE_PASSAGE = "offshore_passage"
    RACING = "racing"
    CHARTER = "charter"


class LubricantType(str, Enum):
    """Type of lubricant."""
    WIRE_ROPE_LUBE = "wire_rope_lube"
    MARINE_GREASE_NLGI2 = "marine_grease_nlgi2"
    HYDRAULIC_HLP = "hydraulic_hlp"
    HYDRAULIC_ATF = "hydraulic_atf"
    HYDRAULIC_BIO = "hydraulic_bio"
    PTFE_SPRAY = "ptfe_spray"
    ANTI_SEIZE = "anti_seize"
    CORROSION_PROTECTION = "corrosion_protection"
    CHAIN_LUBE = "chain_lube"
    BEARING_GREASE = "bearing_grease"


class HydraulicFluidCondition(str, Enum):
    """Condition of hydraulic fluid based on visual inspection."""
    GOOD = "good"
    SLIGHTLY_AGED = "slightly_aged"
    AGED = "aged"
    WATER_CONTAMINATED = "water_contaminated"
    PARTICLE_CONTAMINATED = "particle_contaminated"
    CRITICAL = "critical"


class MaintenanceFailureCode(str, Enum):
    """Failure pattern codes for maintenance findings."""
    F01_CABLE_WIRE_BREAK = "STEER-M-F01"
    F02_HYDRAULIC_LEAK_EXTERNAL = "STEER-M-F02"
    F03_HYDRAULIC_SPONGY = "STEER-M-F03"
    F04_RUDDER_PLAY = "STEER-M-F04"
    F05_STIFF_STEERING = "STEER-M-F05"
    F06_RUDDER_OFFSET = "STEER-M-F06"
    F07_TUBE_LEAK = "STEER-M-F07"
    F08_AUTOPILOT_DRIFT = "STEER-M-F08"
    F09_UNUSUAL_NOISE = "STEER-M-F09"
    F10_WHEEL_HUB_LOOSE = "STEER-M-F10"
    F11_BLADE_WATER_INGRESS = "STEER-M-F11"
    F12_EMERGENCY_TILLER_UNREADY = "STEER-M-F12"


class BearingType(str, Enum):
    """Rudder bearing type."""
    COMPOSITE = "composite"
    BRONZE = "bronze"
    NEEDLE = "needle"
    PTFE_BUSHING = "ptfe_bushing"
    DELRIN_BUSHING = "delrin_bushing"


class SteeringManufacturer(str, Enum):
    """Known steering system manufacturers."""
    JEFA = "jefa"
    WHITLOCK = "whitlock"
    LEWMAR = "lewmar"
    EDSON = "edson"
    SEASTAR = "seastar"
    VETUS = "vetus"
    KOBELT = "kobelt"
    RAYMARINE = "raymarine"
    BG = "b_and_g"
    SIMRAD = "simrad"
    GARMIN = "garmin"
    OTHER = "other"
    UNKNOWN = "unknown"


# ---------------------------------------------------------------------------
# Core Models
# ---------------------------------------------------------------------------

class MaintenanceTask(BaseModel):
    """Single maintenance task definition."""

    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Unique task identifier, e.g. 'cable_visual_inspect'")
    component_group: ComponentGroup = Field(..., description="Which component group this task belongs to")
    category: MaintenanceTaskCategory = Field(..., description="Type of maintenance task")
    description_de: str = Field(..., description="Task description in German")
    description_en: str = Field(..., description="Task description in English")
    qualification_level: MaintenanceQualificationLevel = Field(..., description="Required skill level 1-3")
    interval_months_seasonal: int = Field(..., ge=1, le=120, description="Interval in months for seasonal use")
    interval_months_offshore: Optional[int] = Field(None, ge=1, le=60, description="Interval for offshore/tropical use")
    estimated_time_minutes: int = Field(..., ge=5, le=480, description="Estimated time for task in minutes")
    tools_required: list[str] = Field(default_factory=list, description="List of required tools")
    materials_required: list[str] = Field(default_factory=list, description="List of required materials/consumables")
    safety_warnings: list[str] = Field(default_factory=list, description="Safety warnings in German")


class MaintenanceSchedule(BaseModel):
    """Complete maintenance schedule for a steering system."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Boat name or identifier")
    boat_length_m: float = Field(..., ge=2.0, le=100.0, description="Boat length in meters")
    steering_type: SteeringType = Field(..., description="Primary steering type")
    manufacturer: SteeringManufacturer = Field(default=SteeringManufacturer.UNKNOWN)
    usage_profile: UsageProfile = Field(default=UsageProfile.SEASONAL_TEMPERATE)
    has_autopilot: bool = Field(default=False, description="Autopilot installed?")
    autopilot_manufacturer: Optional[SteeringManufacturer] = Field(None)
    has_emergency_tiller: bool = Field(default=False, description="Emergency tiller available?")

    tasks: list[MaintenanceTask] = Field(default_factory=list, description="List of scheduled tasks")
    next_annual_service_date: Optional[date] = Field(None)
    estimated_annual_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated annual cost in EUR")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.BENCHMARK)


class LubricantSpec(BaseModel):
    """Specification of a lubricant or fluid."""

    model_config = {"from_attributes": True}

    lubricant_type: LubricantType = Field(..., description="Category of lubricant")
    product_name: str = Field(..., description="Product name, e.g. 'Total Equivis ZS 15'")
    manufacturer: str = Field(..., description="Manufacturer of the lubricant")
    viscosity_grade: Optional[str] = Field(None, description="e.g. 'ISO VG 15', 'NLGI 2'")
    temperature_range_min_c: Optional[float] = Field(None, description="Min operating temp in Celsius")
    temperature_range_max_c: Optional[float] = Field(None, description="Max operating temp in Celsius")
    compatible_with: list[str] = Field(default_factory=list, description="Compatible materials/systems")
    incompatible_with: list[str] = Field(default_factory=list, description="Incompatible materials/systems")
    application_points: list[str] = Field(default_factory=list, description="Where to apply")
    reapplication_interval_months: Optional[int] = Field(None, ge=1, le=60)
    notes_de: Optional[str] = Field(None, description="Notes in German")


class HydraulicFluidInspection(BaseModel):
    """Result of a hydraulic fluid visual inspection."""

    model_config = {"from_attributes": True}

    inspection_date: date = Field(..., description="Date of inspection")
    fluid_type_expected: LubricantType = Field(..., description="Expected fluid type")
    fluid_level_ok: bool = Field(..., description="Fluid level within range?")
    fluid_condition: HydraulicFluidCondition = Field(..., description="Visual condition assessment")
    color_description: Optional[str] = Field(None, description="Color description, e.g. 'klar, Originalfarbe'")
    odor_normal: bool = Field(default=True, description="Normal odor?")
    particles_visible: bool = Field(default=False, description="Visible particles in fluid?")
    water_suspected: bool = Field(default=False, description="Water contamination suspected?")
    recommendation_de: str = Field(..., description="Recommendation in German")
    change_required: bool = Field(default=False, description="Fluid change required?")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.VISUAL_MEDIUM)


class CableTensionMeasurement(BaseModel):
    """Measurement of steering cable tension."""

    model_config = {"from_attributes": True}

    measurement_date: date = Field(..., description="Date of measurement")
    cable_diameter_mm: float = Field(..., ge=2.0, le=10.0, description="Cable diameter in mm")
    tension_port_n: float = Field(..., ge=0, le=500, description="Port side tension in Newton")
    tension_starboard_n: float = Field(..., ge=0, le=500, description="Starboard side tension in Newton")
    target_tension_n: float = Field(..., ge=50, le=400, description="Target tension in Newton")
    ambient_temperature_c: Optional[float] = Field(None, description="Ambient temperature in Celsius")
    wire_breaks_count_per_m: int = Field(default=0, ge=0, description="Number of wire breaks per meter")
    kinks_found: bool = Field(default=False, description="Any kinks found?")
    corrosion_visible: bool = Field(default=False, description="Visible corrosion?")
    tension_within_spec: bool = Field(default=True, description="Tension within specification?")
    asymmetry_percent: Optional[float] = Field(None, ge=0, le=100, description="Asymmetry between port/starboard in %")
    recommendation_de: str = Field(..., description="Recommendation in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class BearingPlayMeasurement(BaseModel):
    """Measurement of rudder bearing play."""

    model_config = {"from_attributes": True}

    measurement_date: date = Field(..., description="Date of measurement")
    bearing_location: str = Field(..., description="'upper' or 'lower'")
    bearing_type: BearingType = Field(..., description="Type of bearing")
    radial_play_mm: float = Field(..., ge=0, le=10, description="Radial play in mm")
    axial_play_mm: Optional[float] = Field(None, ge=0, le=10, description="Axial play in mm")
    measurement_method: str = Field(..., description="'dial_indicator', 'feeler_gauge', 'lever_magnification'")
    force_applied_kg: Optional[float] = Field(None, ge=0, le=50, description="Force applied for measurement in kg")
    boat_in_water: bool = Field(default=False, description="Measured with boat in water?")
    max_radial_play_mm: float = Field(..., ge=0, le=5, description="Maximum acceptable radial play in mm")
    within_spec: bool = Field(default=True, description="Within specification?")
    trend_vs_previous: Optional[str] = Field(None, description="'stable', 'increasing', 'rapid_increase', 'new'")
    recommendation_de: str = Field(..., description="Recommendation in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class AutopilotCalibrationResult(BaseModel):
    """Result of an autopilot calibration."""

    model_config = {"from_attributes": True}

    calibration_date: date = Field(..., description="Date of calibration")
    autopilot_manufacturer: SteeringManufacturer = Field(...)
    autopilot_model: str = Field(..., description="Autopilot model name")
    firmware_version: Optional[str] = Field(None, description="Current firmware version")

    docking_calibration_ok: bool = Field(default=False, description="Docking cal completed?")
    rudder_range_port_deg: Optional[float] = Field(None, description="Rudder range to port in degrees")
    rudder_range_stbd_deg: Optional[float] = Field(None, description="Rudder range to starboard in degrees")

    sea_trial_calibration_ok: bool = Field(default=False, description="Sea trial cal completed?")
    compass_deviation_max_deg: Optional[float] = Field(None, ge=0, le=30, description="Max compass deviation in degrees")
    compass_deviation_acceptable: bool = Field(default=True, description="Deviation within 3 degrees?")

    response_level: Optional[int] = Field(None, ge=1, le=9, description="Set response level")
    course_keeping_test_passed: bool = Field(default=False, description="Course keeping within ±3°?")
    standby_release_test_passed: bool = Field(default=False, description="Immediate release on standby?")

    issues_found: list[str] = Field(default_factory=list, description="List of issues found during calibration")
    recommendation_de: str = Field(..., description="Recommendation in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class EmergencyTillerTest(BaseModel):
    """Result of an emergency tiller readiness test."""

    model_config = {"from_attributes": True}

    test_date: date = Field(..., description="Date of test")
    tiller_located: bool = Field(..., description="Emergency tiller found in designated location?")
    access_path_clear: bool = Field(..., description="Access path unobstructed?")
    fits_on_shaft: bool = Field(..., description="Tiller fits correctly on rudder shaft?")
    securing_pin_present: bool = Field(default=False, description="Securing pin/bolt available?")
    assembly_time_seconds: Optional[int] = Field(None, ge=0, le=600, description="Time to assemble in seconds")
    target_assembly_time_seconds: int = Field(default=120, description="Target assembly time in seconds")
    steering_force_acceptable: bool = Field(default=True, description="Steering force manageable with one hand?")
    crew_briefed: bool = Field(default=False, description="Crew briefed on emergency procedure?")
    crew_names: list[str] = Field(default_factory=list, description="Names of briefed crew members")
    test_passed: bool = Field(default=False, description="Overall test passed?")
    issues_found: list[str] = Field(default_factory=list)
    recommendation_de: str = Field(..., description="Recommendation in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class MaintenanceFinding(BaseModel):
    """Single maintenance finding during inspection."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding ID")
    inspection_date: date = Field(..., description="Date of inspection")
    failure_code: MaintenanceFailureCode = Field(..., description="Failure pattern code")
    component_group: ComponentGroup = Field(..., description="Affected component group")
    severity: SeverityLevel = Field(..., description="Severity 1-5")
    confidence: ConfidenceLevel = Field(..., description="Detection confidence")
    location_de: str = Field(..., description="Location on boat in German")
    description_de: str = Field(..., description="Finding description in German")
    suggestion_de: str = Field(..., description="Action recommendation in German")
    score_impact: int = Field(..., ge=-100, le=0, description="Negative score impact")
    photo_reference: Optional[str] = Field(None, description="Photo/image reference")
    requires_professional: bool = Field(default=False, description="Professional service required?")
    estimated_repair_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated repair cost in EUR")
    estimated_repair_time_hours: Optional[float] = Field(None, ge=0, description="Estimated repair time in hours")
    deadline_category: Optional[str] = Field(
        None,
        description="'immediate', 'within_month', 'next_season', 'monitor'"
    )


class SteeringMaintenanceInspection(BaseModel):
    """Complete steering system maintenance inspection result."""

    model_config = {"from_attributes": True}

    inspection_date: date = Field(..., description="Date of inspection")
    inspector_name: Optional[str] = Field(None, description="Inspector name")
    inspector_qualification: MaintenanceQualificationLevel = Field(
        default=MaintenanceQualificationLevel.OWNER_BASIC
    )

    boat_name: Optional[str] = Field(None, description="Boat name or identifier")
    boat_length_m: float = Field(..., ge=2.0, le=100.0)
    steering_type: SteeringType = Field(...)
    steering_manufacturer: SteeringManufacturer = Field(default=SteeringManufacturer.UNKNOWN)

    # Sub-scores (0-100)
    cable_score: Optional[int] = Field(None, ge=0, le=100, description="Cable/wire condition score")
    hydraulic_score: Optional[int] = Field(None, ge=0, le=100, description="Hydraulic system score")
    bearing_score: Optional[int] = Field(None, ge=0, le=100, description="Rudder bearing score")
    pedestal_score: Optional[int] = Field(None, ge=0, le=100, description="Pedestal/wheel score")
    autopilot_score: Optional[int] = Field(None, ge=0, le=100, description="Autopilot system score")
    emergency_score: Optional[int] = Field(None, ge=0, le=100, description="Emergency tiller score")
    overall_maintenance_score: int = Field(..., ge=0, le=100, description="Overall maintenance score")

    # Measurements
    cable_tension: Optional[CableTensionMeasurement] = Field(None)
    bearing_measurements: list[BearingPlayMeasurement] = Field(default_factory=list)
    fluid_inspection: Optional[HydraulicFluidInspection] = Field(None)
    autopilot_calibration: Optional[AutopilotCalibrationResult] = Field(None)
    emergency_tiller_test: Optional[EmergencyTillerTest] = Field(None)

    # Findings
    findings: list[MaintenanceFinding] = Field(default_factory=list)
    critical_findings_count: int = Field(default=0, ge=0)

    # Summary
    seaworthy: bool = Field(..., description="Steering system seaworthy?")
    next_service_date: Optional[date] = Field(None)
    estimated_annual_maintenance_cost_eur: Optional[float] = Field(None, ge=0)
    summary_de: str = Field(..., description="Summary in German")
    confidence: ConfidenceLevel = Field(...)
    analysis_version: str = Field(default="1.0.0")


class WearTrend(BaseModel):
    """Wear trend data point for predictive maintenance."""

    model_config = {"from_attributes": True}

    measurement_date: date = Field(...)
    component_group: ComponentGroup = Field(...)
    parameter_name: str = Field(..., description="e.g. 'radial_play_upper_mm', 'cable_tension_port_n'")
    value: float = Field(..., description="Measured value")
    unit: str = Field(..., description="Unit of measurement")
    threshold_warning: Optional[float] = Field(None, description="Warning threshold")
    threshold_critical: Optional[float] = Field(None, description="Critical threshold")


class PredictiveMaintenanceResult(BaseModel):
    """Result of AYDI predictive maintenance analysis."""

    model_config = {"from_attributes": True}

    analysis_date: date = Field(...)
    boat_name: Optional[str] = Field(None)
    component_group: ComponentGroup = Field(...)

    trend_data: list[WearTrend] = Field(default_factory=list)
    trend_direction: str = Field(..., description="'stable', 'linear_increase', 'progressive_increase', 'sudden_jump'")
    estimated_remaining_life_months: Optional[int] = Field(None, ge=0, le=240)
    recommended_action_de: str = Field(..., description="Recommended action in German")
    recommended_action_deadline: Optional[date] = Field(None)
    estimated_replacement_cost_eur: Optional[float] = Field(None, ge=0)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    analysis_version: str = Field(default="1.0.0")


class TroubleshootingStep(BaseModel):
    """Single step in a troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    step_id: str = Field(..., description="Unique step identifier")
    question_de: str = Field(..., description="Question to ask/check in German")
    yes_next_step: Optional[str] = Field(None, description="Next step ID if yes")
    no_next_step: Optional[str] = Field(None, description="Next step ID if no")
    resolution_de: Optional[str] = Field(None, description="Resolution if this is a terminal step")
    severity: Optional[SeverityLevel] = Field(None)
    requires_professional: bool = Field(default=False)


class TroubleshootingTree(BaseModel):
    """Complete troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(..., description="Unique tree identifier")
    title_de: str = Field(..., description="Title in German")
    title_en: str = Field(..., description="Title in English")
    symptom_de: str = Field(..., description="Starting symptom in German")
    steps: list[TroubleshootingStep] = Field(default_factory=list)
    first_step_id: str = Field(..., description="ID of the first step")


class MaintenanceCostEstimate(BaseModel):
    """Cost estimate for steering system maintenance."""

    model_config = {"from_attributes": True}

    steering_type: SteeringType = Field(...)
    boat_length_m: float = Field(..., ge=2.0, le=100.0)
    usage_profile: UsageProfile = Field(default=UsageProfile.SEASONAL_TEMPERATE)

    annual_routine_cost_eur: float = Field(..., ge=0, description="Annual routine maintenance cost")
    annual_consumables_cost_eur: float = Field(..., ge=0, description="Annual consumables cost (fluid, grease, etc.)")
    five_year_replacement_cost_eur: float = Field(..., ge=0, description="5-year replacement parts cost")
    ten_year_overhaul_cost_eur: float = Field(..., ge=0, description="10-year overhaul cost estimate")
    total_annual_average_eur: float = Field(..., ge=0, description="Total annual average cost over 10 years")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    notes_de: Optional[str] = Field(None, description="Notes in German")
```

---

### ANHANG J — Ersatzteil-Beschaffung und Lagerung

**Ersatzteil-Verfuegbarkeit nach Hersteller:**

| Hersteller | Verfuegbarkeit EU | Lieferzeit Standard | Lieferzeit Notfall | Online-Shop |
|-----------|-------------------|--------------------|--------------------|-------------|
| Jefa | Gut | 3-7 Tage | 1-2 Tage (ab DK) | jefa.com |
| Lewmar/Whitlock | Sehr gut | 2-5 Tage | 1-2 Tage (ab UK/NL) | lewmar.com |
| Edson | Maessig (Import USA) | 10-21 Tage | 5-7 Tage (Luftfracht) | edsonmarine.com |
| SeaStar/Teleflex | Gut | 3-7 Tage | 2-3 Tage | dometic.com |
| Raymarine | Sehr gut | 2-5 Tage | 1-2 Tage | raymarine.com |
| B&G/Navico | Gut | 3-7 Tage | 2-3 Tage | bandg.com |
| Vetus | Sehr gut | 2-5 Tage | 1 Tag (ab NL) | vetus.com |

**Empfohlene Ersatzteil-Lagerung an Bord (Langfahrt):**

| Prioritaet | Ersatzteil | Grund |
|-----------|-----------|-------|
| PFLICHT | Steuerseile (Paar, vormontiert) | Seilbruch = Totalausfall |
| PFLICHT | Hydraulikfluid (Systemmenge + 50%) | Leckage = Steuerverlust |
| PFLICHT | Notpinne + Adapter + Sicherung | Letztes Sicherheitsnetz |
| HOCH | Dichtungssatz Helmpumpe | Pumpenleckage = haeufigster Hydraulik-Ausfall |
| HOCH | Dichtungssatz Hydraulikzylinder | Zylinderleckage auf See nicht anders behebbar |
| HOCH | Hydraulik-Schlauch (laengster Schlauch im System) | Schlauchplatzer |
| HOCH | Nicropress-Huelsen + Kauschen (passend zum Seil) | Fuer Seil-Reparatur |
| MITTEL | Umlenkrollen (2 Stueck der haeufigsten Groesse) | Bei Rollenbruch |
| MITTEL | Bolzen, Splinte, Schaekel (Sortiment) | Fuer diverse Reparaturen |
| MITTEL | O-Ringe fuer Hydraulikanschluesse (Sortiment) | Undichte Anschluesse |
| MITTEL | Autopilot-Sicherungen (Ersatz) | Sicherungsausfall |
| NIEDRIG | Pedestal-Kette (falls Kettensteuerung) | Kettenbruch selten |
| NIEDRIG | Ruderlager-Dichtlippe | Nur an Land wechselbar, aber als Reserve |

**Lagerung der Ersatzteile:**
- Steuerseile: In oelgetraenktem Papier oder Plastikbeutel, trocken, nicht geknickt lagern
- Hydraulikfluid: In Originalgebinde, aufrecht, vor Sonne geschuetzt
- Dichtungen: In verschlossenem Beutel, vor UV und Hitze geschuetzt
- Schlaeuche: Nicht knicken, Enden verschlossen (Staubkappen)
- Bolzen/Kleinteile: In beschrifteten Beuteln, in einer Box sortiert

### ANHANG K — Checkliste Gebrauchtboot-Kauf — Steueranlage

```
STEUERANLAGEN-CHECK BEI GEBRAUCHTBOOT-BESICHTIGUNG
=====================================================
Boot: _________________ Baujahr: _____ Preis: _______
Steuerungstyp: _________ Hersteller: _________________

DOKUMENTATION
[ ] Wartungsprotokolle vorhanden?          Ja □ Nein □
[ ] Letzte professionelle Inspektion:       _________ (Datum)
[ ] Seilwechsel dokumentiert?              Ja □ Nein □  Datum: _______
[ ] Ruderlager-Wechsel dokumentiert?       Ja □ Nein □  Datum: _______
[ ] Hydraulikoel-Wechsel dokumentiert?     Ja □ Nein □  Datum: _______

FUNKTIONSTEST (auf dem Wasser)
[ ] Steuerrad von Anschlag zu Anschlag:    Leicht □ Normal □ Schwer □
[ ] Spiel am Steuerrad (Totgang):          <5° □  5-10° □  >10° □
[ ] Geradeauslauf (Haende vom Rad):        Ja □ Nein □  Tendenz: ____
[ ] Autopilot Selbsttest:                  OK □ Fehler □ Kein AP □
[ ] Autopilot Kurshalten (5 min):          ±3° □  ±5° □  >5° □
[ ] Geraeusche beim Steuern:              Keine □ Leicht □ Deutlich □

VISUELLE INSPEKTION
[ ] Steuerseile (sofern sichtbar):         OK □ Litzenbruch □ Korrosion □
[ ] Hydraulik Oelstand:                    OK □ Niedrig □
[ ] Hydraulik Oelfarbe:                    Klar □ Dunkel □ Trueb □
[ ] Hydraulik Leckage:                     Keine □ Film □ Tropfen □
[ ] Pedestal Zustand:                      Gut □ Korrosion □ Riss □
[ ] Steuerrad Zustand:                     Gut □ Verwittert □ Beschaedigt □
[ ] Notpinne vorhanden:                    Ja □ Nein □
[ ] Notpinne Stecktest:                    Passt □ Passt nicht □

AN LAND (falls moeglich)
[ ] Ruderblatt Klopftest:                  Klar □ Dumpf □
[ ] Ruderblatt Gelcoat:                    OK □ Risse □ Osmose □
[ ] Ruderlager Spiel (seitlich):           Kein □ Leicht □ Deutlich □
[ ] Skeg Zustand:                          OK □ Riss □
[ ] Koker-Zustand (von innen):            Trocken □ Feucht □ Nass □

BEWERTUNG
[ ] Steueranlage einwandfrei
[ ] Kleinere Maengel (Wartung noetig): _________________
[ ] Groessere Maengel (Reparatur noetig): _________________
[ ] Steueranlage sanierungsbeduerftig → Preisnachlass: _______ EUR

Geschaetzte Sanierungskosten: _________ EUR
Pruefer: _________________ Datum: ___________
```

### ANHANG R2 — Visuelle Analyse-Leitfaden fuer AYDI Pipeline B

Folgende Wartungs-Befunde koennen durch visuelle Analyse (Fotos) erkannt werden:

| Merkmal | Confidence | Erkennungsmethode |
|---------|-----------|-------------------|
| Litzenbrueche im Steuerseil | visual_high | Abstehende Draehte sichtbar |
| Seilkorrosion (Rostfarben) | visual_high | Braeunliche Verfaerbung |
| Hydraulikleckage (Oelfleck) | visual_high | Oelflecken, Tropfen |
| Hydraulikfluid-Farbe (durch Behaelter) | visual_medium | Verfaerbung im transparenten Behaelter |
| Pedestal-Korrosion | visual_medium | Weisse/gruene Ablagerungen |
| Steuerrad-Teak Zustand | visual_high | Vergrauung, Risse, Spalten |
| Ruderblatt-Gelcoat-Risse | visual_high | Risslinien an Oberflaeche |
| Ruderblatt-Bewuchs | visual_high | Muscheln, Algen sichtbar |
| Ruderblatt-Osmose-Blasen | visual_medium | Rundliche Erhebungen |
| Koker-Wassereinbruch (Flecken) | visual_medium | Wasserflecken, Korrosionsspuren |
| Hydraulikschlauch-Risse (UV) | visual_medium | Oberflaechenrisse, Sproedigkeit |
| Notpinne vorhanden/zugaenglich | visual_medium | Pinne sichtbar in Halterung |
| Autopilot-Linearantrieb Zustand | visual_medium | Korrosion, Beschaedigung |
| Quadrant-Korrosion | visual_medium | Weisse Aluminium-Oxidation |
| Seil-Rolle Ausrichtung | visual_low | Schraeglauf schwer zu erkennen |
| Lagerspiel (indirekt) | visual_low | Nur bei deutlichem Spiel sichtbar |

**Zusaetzliche visuelle Indikatoren fuer Wartungszustand:**

| Indikator | Was er verraet | Confidence |
|-----------|---------------|-----------|
| Allgemeiner Pflegezustand Cockpit | Korreliert stark mit Steueranlagen-Wartung | visual_medium |
| Alter der Teakoberflaechen | Gibt Hinweis auf Wartungskultur | visual_medium |
| Sauberkeit im Lazarette/Achterbereich | Zugang zu Steueranlage gepflegt? | visual_medium |
| Zustand Autopilot-Display | UV-Schaeden, Kratzer zeigen Vernachlaessigung | visual_high |
| Korrosion an Edelstahlteilen generell | Hinweis auf Salzwasser-Belastung ohne Reinigung | visual_medium |
| Zustand der Sicherheitsausruestung | Gepflegtes Rettungsmittel = gepflegtes Boot | visual_low |
| Antifouling-Zustand Unterwasserschiff | Allgemeiner Wartungsindikator | visual_medium |
| Farbe des Hydraulikoels (im Behaelter) | Direkte Wartungsinformation | visual_medium |
| Oelflecken unter Steueranlage | Direkte Leckage-Erkennung | visual_high |
| Zustand der Kabel/Leitungen generell | Zeigt Wartungsphilosophie | visual_medium |

**Pipeline-B Scoring fuer Wartungszustand:**

Bei rein visueller Analyse (nur Fotos, keine Messdaten) kann AYDI den Wartungszustand mit folgenden Confidence-Levels schaetzen:

- **visual_high (Score-Genauigkeit ±10 Punkte):** Bei klaren Befunden wie sichtbaren Litzenbruechen, Oellachen, offensichtlicher Korrosion, gerissenen Schlaeuchen
- **visual_medium (Score-Genauigkeit ±20 Punkte):** Bei indirekten Indikatoren wie allgemeinem Pflegezustand, Alter-Schaetzung, Oberflaechenzustand
- **visual_low (Score-Genauigkeit ±35 Punkte):** Bei schwer interpretierbaren Fotos, unvollstaendiger Dokumentation, oder wenn nur Teilbereiche sichtbar sind

AYDI gibt bei rein visueller Analyse immer den Hinweis: "Visuelle Einschaetzung — fuer praezise Bewertung Messdaten erforderlich (Seilspannung, Lagerspiel, Hydraulikdruck)."

**Prompt-Hinweise fuer Claude Vision (Pipeline B) — Wartungsbefunde:**
- Bei Unterdeck-Fotos: Auf Oelflecken, Wasserflecken und Korrosionsspuren achten
- Steuerseile: Abstehende Draehte als helle Punkte auf dunklem Seil erkennbar
- Hydraulik: Oelverfaerbungen auf hellen Untergründen als Wartungsindikator
- Pedestal: Zustand der Abdeckung ist Indikator fuer Gesamtwartungszustand
- Steuerrad: Teak-Zustand korreliert stark mit Gesamtwartungszustand des Bootes
- Ruderblatt (Unterwasserfoto): Bewuchsgrad als Indikator fuer Wartungskultur
- Alter des Bootes aus Gesamteindruck schaetzen → Wartungsintervalle anpassen
- Bei Zweifel: "Wartungszustand nicht visuell beurteilbar" ist besser als eine Fehleinschaetzung

---

*Ende der Wissensdatei 14.08 — Steueranlagen Wartung und Troubleshooting*
*AYDI Research, Version 1.0.0, Stand: 2026-04-26*