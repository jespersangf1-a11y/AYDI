# 22.10 — Galvanische Korrosion und Blitzschutz

> **AYDI Wissensdatei 22.10** — Kategorie 22: Korrosionsschutz, Erdung und Blitzschutz
> **Confidence-Quelle:** measured (Hersteller-TDS, MIL-Specs, ABYC-Standards), documented (ISO/DIN-Normen, Klassegesellschaften, NACE/SSPC), estimated (Erfahrungswerte, Surveyor-Konsens, Werft-Berichte)
> **Letzte Aktualisierung:** 2026-05-07

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbaeume](#7-troubleshooting-entscheidungsbaeume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A-H — Fallstudien](#11-anhang-a-h-fallstudien)
12. [ANHANG I-R — Pydantic v2 Modelle](#12-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Korrosion als groesste Bedrohung im Yachtbau

Galvanische Korrosion ist der kostspieligste und am haeufigsten uebersehene Schadensmechanismus in der maritimen Industrie. Sie betrifft ausnahmslos jede Yacht — vom 7-m-Trailer-Segler bis zur 60-m-Megayacht. Im Gegensatz zu mechanischen Schaeden, die sofort sichtbar sind, arbeitet Korrosion lautlos unter der Wasserlinie, in verborgenen Bilgenbereichen, hinter Verkleidungen und in schwer zugaenglichen Hohlraeumen.

**Wirtschaftliche Dimension:**

| Schadenskategorie | Typische Kosten (EUR) | Haeufigkeit pro 1.000 Yachten/Jahr |
|---|---|---|
| Propellerkorrosion (vollstaendig) | 3.500–18.000 | 12–18 |
| Wellenkorrosion (Lochfrass bis Bruch) | 5.000–35.000 | 6–10 |
| Ruderkoker-Durchkorrosion | 8.000–45.000 | 3–7 |
| Saildrive-Gehaeuse-Angriff | 4.000–25.000 | 8–15 |
| Rumpfdurchbruch-Korrosion (Bronze/Messing) | 2.000–12.000 | 5–9 |
| Aluminiumrumpf-Korrosion (lokalisiert) | 15.000–120.000 | 2–5 |
| Strahlstrom-Schaden (Marina-Erdung) | 10.000–250.000 | 1–3 |
| Blitzschlag-Folgeschaden (ohne Schutz) | 25.000–500.000+ | 0,5–2 |

**Kernaussage:** Die jaehrlichen Kosten fuer einen vollstaendigen kathodischen Schutz (Opferanoden-Satz) liegen zwischen 80 EUR und 600 EUR. Die Kosten eines einzigen Korrosionsschadens uebersteigen diese Praeventionskosten um den Faktor 10 bis 1.000.

### 1.2 Abgrenzung dieser Wissensdatei

Diese Datei ergaenzt und vertieft die bestehenden AYDI-Wissensdateien:
- **05_10** (Galvanische Spannungsreihe & Thru-Hulls): Grundlagen der Materialpaarungen
- **07_06** (Opferanoden und Korrosionsschutz): Anodentypen und Dimensionierung

Die vorliegende Datei 22_10 fokussiert auf:
- **Streustrom-Korrosion** als eigenstaendiges, besonders gefaehrliches Phaenomen
- **ICCP-Systeme** in Detailtiefe (Auslegung, Installation, Wartung)
- **Galvanische Isolatoren** als Schutz gegen Marina-Erdungsprobleme
- **Blitzschutz** vollstaendig (Ableiter, Erdung, Zonenkonzept, Elektronikschutz)
- **Bonding-Systeme** als Gesamtkonzept (DC-Bonding, RF-Bonding, Lightning-Bonding)
- **Systemintegration** aller Schutzmassnahmen zu einem kohaerenten Gesamtkonzept

### 1.3 AYDI-Integrationsebenen

```
Pipeline A (Structured): Korrosionsrisiko-Berechnung, Materialpaarungs-Validierung,
                          ICCP-Dimensionierung, Blitzschutz-Zonenberechnung,
                          Bonding-Netzwerk-Analyse
Pipeline B (Visual):      Korrosionserkennung (Anodenverbrauch, Lochfrass, Verfaerbung),
                          Blitzschlag-Schadenserkennung, Bonding-Kabel-Zustandsbewertung
Pipeline C (Text):        Service-Report-Analyse (Korrosionsbefunde, Potenzial-Messprotokolle,
                          Versicherungs-Gutachten, Surveyor-Berichte)
```

### 1.4 Regulatorischer Rahmen

| Norm / Standard | Bezeichnung | Geltungsbereich | AYDI-Relevanz |
|---|---|---|---|
| **ISO 20313:2018** | Cathodic protection of ships | Kathodischer Schutz Seeschiffe | Schutzpotenziale, Anodenberechnung |
| **DIN EN 12496:2013** | Galvanische Anoden fuer kathodischen Schutz | Anodenlegierungen, Mindestleistung | Qualitaetsanforderungen |
| **ABYC E-2 (2023)** | Cathodic Protection | Nordamerikanischer Yachtstandard | De-facto-Weltstandard, sehr detailliert |
| **ABYC E-11 (2023)** | AC and DC Electrical Systems | Elektrische Systeme Boote | Bonding, Erdung, Isolatoren |
| **ABYC TE-4 (2023)** | Lightning Protection | Blitzschutz Boote | Ableiter, Erdungsfinger |
| **ISO 10134:2003** | Electrical devices — Lightning protection | Blitzschutz Yachten | Zonenkonzept, Ableiterwege |
| **IEC 62305-1 bis -4** | Blitzschutz (allgemein) | Anpassung fuer Schiffe | Risikoanalyse, Zonenkonzept |
| **NFPA 302** | Fire Protection Standard for Pleasure and Commercial Motor Craft | Feuer-/Explosionsschutz | Bonding Kraftstoffsystem |
| **DIN EN 13174:2001** | Kathodischer Schutz Hafeninfrastruktur | Liegeplatz-Wechselwirkungen | Marina-Streustrom-Problematik |
| **DNV-RP-B401:2021** | Cathodic Protection Design | Offshore-Auslegung | Berechnungsgrundlage ICCP |
| **MIL-A-18001K** | Zinc Anodes — Slab, Disc, Rod | Militaer-Spec Zinkanoden | Legierungszusammensetzung |
| **MIL-DTL-24779C** | Aluminum Alloy Sacrificial Anodes | Militaer-Spec Aluminiumanoden | Al-Zn-In-Legierung |
| **NACE SP0176-2007** | Corrosion Control Submerged Steel | Offshore-Kathodenschutz | Anodenauslegung |
| **ISO 8044:2020** | Korrosion — Grundbegriffe | Terminologie | Einheitliche Fachbegriffe |

### 1.5 Haftung und Versicherung

Korrosionsschaeden sind ein haeufiger Streitpunkt zwischen Eignern und Versicherungen. Die zentralen Haftungsaspekte:

**Obliegenheitsverletzung:** Ein fehlender oder nachweislich verbrauchter kathodischer Schutz kann bei Folgeschaeden (Wellenbruch, Ruderverlust, Sinken) als Obliegenheitsverletzung gewertet werden. Versicherungen kuerzen oder verweigern Leistungen.

**Dokumentationspflicht:**
- Anodenwechsel-Protokoll mit Datum, Typ, Gewicht (neu/verbraucht), Einbauort
- Potenzial-Messprotokolle bei jedem Werftaufenthalt (Haul-Out)
- ICCP-Logdaten (bei installierten Systemen)
- Blitzschutz-Pruefprotokoll (jaehrlich empfohlen, bei Klasse-Yachten vorgeschrieben)
- Bonding-Durchgangspruefung (Widerstand < 1 Ohm zwischen allen Komponenten)

**Werft-Haftung:** Eine Werft, die bei einem Unterwasseranstrich die Anoden nicht prueft oder bei erkennbarem Verbrauch nicht darauf hinweist, kann im Schadensfall mithaften. Professionelle Werften dokumentieren den Anodenzustand fotografisch.

**Blitzschlag-Versicherung:** Blitzschlag ist ein typischer Kaskoschaden. Allerdings koennen Versicherungen argumentieren, dass ein fehlender Blitzschutz bei bekannter Gewitterhaeufigkeit (z.B. Florida, Mittelmeer Sommer) eine Obliegenheitsverletzung darstellt — insbesondere bei Yachten > 15 m.

### 1.6 Klimatische und geographische Faktoren

Die Korrosionsaggressivitaet haengt stark vom Standort ab:

| Region | Salzgehalt (ppt) | Wassertemperatur (C) | Korrosionsrate (relativ) | Besonderheiten |
|---|---|---|---|---|
| Ostsee | 5–18 | 2–18 | 0,4–0,7 | Brackwasser, Zinkanoden suboptimal |
| Nordsee | 30–35 | 4–16 | 0,8–1,0 | Standard-Seewasser |
| Mittelmeer | 36–39 | 13–28 | 1,0–1,3 | Hoher Salzgehalt, warm |
| Karibik | 35–36 | 25–30 | 1,2–1,5 | Warm, hohe Leitfaehigkeit |
| Persischer Golf | 38–42 | 20–35 | 1,5–2,0 | Extrem hoher Salzgehalt, sehr warm |
| Suedostasien | 30–34 | 26–31 | 1,3–1,6 | Warm, biologisch aktiv |
| Skandinavien (Fjorde) | 25–34 | 2–12 | 0,5–0,8 | Kalt, Schichtung |
| Nordamerika Ostkueste | 30–35 | 2–28 | 0,8–1,2 | Saisonal stark variabel |
| Florida / Bahamas | 35–36 | 22–30 | 1,3–1,6 | Blitzschlag-Hotspot |
| Suesswasser (Binnenseen) | 0–0,5 | 4–25 | 0,1–0,3 | Magnesiumanoden erforderlich |

**AYDI-Relevanz:** Das Fahrtgebiet/Liegeplatz bestimmt die Anodenauswahl, die Wechselintervalle, die ICCP-Einstellung und die Blitzschutz-Prioritaet.

---

## 2. Grundlagen und Theorie

### 2.1 Galvanische Spannungsreihe Marine — Erweitert

Die galvanische Spannungsreihe ordnet Metalle nach ihrem elektrochemischen Potenzial in Seewasser (Referenz: Ag/AgCl-Elektrode, 25 C, Salzgehalt 35 ppt):

| Material | Potenzial (mV vs. Ag/AgCl) | Klassifikation | Yacht-Relevanz |
|---|---|---|---|
| Magnesium | −1.600 bis −1.630 | Stark anodisch | Opferanode (Suesswasser) |
| Magnesium-Legierung (AZ-63) | −1.580 bis −1.600 | Stark anodisch | Opferanode (Suesswasser) |
| Zink (rein, 99,99%) | −1.030 bis −1.050 | Anodisch | Opferanode (Seewasser Standard) |
| Zink-Legierung (MIL-A-18001K) | −1.000 bis −1.050 | Anodisch | Opferanode (Seewasser bevorzugt) |
| Aluminium-Zink-Indium (Al-Zn-In) | −1.050 bis −1.100 | Anodisch | Opferanode (universell) |
| Aluminium 5000-Serie (AlMg) | −750 bis −850 | Leicht anodisch | Rumpfmaterial |
| Aluminium 6000-Serie (AlMgSi) | −700 bis −800 | Leicht anodisch | Masten, Profile |
| Kadmium | −700 bis −750 | Leicht anodisch | Veraltet, toxisch |
| Kohlenstoffstahl (mild steel) | −600 bis −710 | Leicht anodisch | Kiel, Beschlaege (verzinkt) |
| Gusseisen (Grauguss) | −600 bis −700 | Leicht anodisch | Kielballast |
| Edelstahl 304 (aktiv) | −460 bis −530 | Neutral-aktiv | Beschlaege (NICHT fuer Seewasser!) |
| Edelstahl 316 (aktiv) | −430 bis −540 | Neutral-aktiv | Beschlaege (Standard Marine) |
| Blei | −430 bis −530 | Neutral | Kielballast |
| Blei-Zinn-Lot | −380 bis −470 | Neutral | Loetverbindungen |
| Zinn | −370 bis −440 | Neutral | Verzinnung |
| Messing (CuZn36) | −300 bis −400 | Leicht kathodisch | Traditionelle Beschlaege |
| Kupfer (rein) | −280 bis −360 | Kathodisch | Antifouling-Grundlage |
| Manganbronze | −270 bis −350 | Kathodisch | Propeller (guenstig) |
| Zinnbronze (G-CuSn10) | −250 bis −340 | Kathodisch | Seeventile, Schiffsschrauben |
| Siliziumbronze | −240 bis −310 | Kathodisch | Premium-Befestiger |
| Kupfer-Nickel 90/10 | −200 bis −280 | Kathodisch | Rohrleitungen |
| Kupfer-Nickel 70/30 | −180 bis −260 | Kathodisch | Waermetauscher |
| Nickelaluminumbronze (NAB) | −180 bis −260 | Kathodisch | Premium-Propeller |
| Edelstahl 316L (passiv) | −50 bis −200 | Stark kathodisch | Welle, Beschlaege |
| Edelstahl 2205 Duplex (passiv) | −30 bis −180 | Stark kathodisch | Premium-Wellen |
| Titan (passiv) | +20 bis −80 | Stark kathodisch | ICCP-Anoden, Waermetauscher |
| Inconel 625 | +10 bis −60 | Stark kathodisch | Abgassysteme |
| Hastelloy C-276 | +10 bis −60 | Stark kathodisch | Chemie-Bestaendigkeit |
| Graphit / Carbon | +200 bis +300 | Extrem kathodisch | Carbonmasten, -ruder |
| Platin | +220 bis +280 | Extrem kathodisch | ICCP-Anodenbeschichtung |

**Kritische Schwellenwerte fuer Korrosion:**
- < 50 mV Differenz: Vernachlaessigbar, keine Massnahmen
- 50–150 mV Differenz: Leichte Korrosion moeglich, Isolation empfohlen
- 150–300 mV Differenz: Deutliche Korrosion, Isolation oder Opferanoden erforderlich
- 300–500 mV Differenz: Schwere Korrosion, aktiver Schutz zwingend
- > 500 mV Differenz: Zerstoererische Korrosion, Materialtrennung oder ICCP zwingend

### 2.2 Potenzialdifferenz und Korrosionsstrom

Die Korrosionsrate haengt nicht nur von der Potenzialdifferenz ab, sondern auch von:

**Flaechen-Verhaeltnis (Kathode:Anode):**
Die gefaehrlichste Konfiguration ist eine grosse Kathode mit einer kleinen Anode. Beispiel: Grosser Edelstahl-Propeller (Kathode) mit kleiner Stahlschraube (Anode) = extrem schnelle Korrosion der Schraube.

```
Korrosionsrate ~ (Flaeche_Kathode / Flaeche_Anode) x Potenzialdifferenz x Leitfaehigkeit_Elektrolyt
```

**Praktische Faustregel:** Das Flaechenverhaeltnis Kathode:Anode sollte maximal 10:1 betragen. Bei unguenstigeren Verhaeltnissen steigt die Korrosionsrate ueberproportional.

| Flaechenverhaeltnis K:A | Korrosionsbeschleunigung (relativ) | Bewertung |
|---|---|---|
| 1:1 | 1,0x | Optimal |
| 5:1 | 3–5x | Akzeptabel mit Schutz |
| 10:1 | 8–12x | Kritisch |
| 50:1 | 30–60x | Zerstoererisch |
| 100:1 | 80–120x | Versagen innerhalb Wochen |

**Elektrolyt-Leitfaehigkeit:**

| Elektrolyt | Leitfaehigkeit (S/m) | Relative Korrosionsrate |
|---|---|---|
| Destilliertes Wasser | 0,0005 | ~0 |
| Regenwasser | 0,002–0,01 | 0,01 |
| Leitungswasser | 0,05–0,5 | 0,05–0,1 |
| Brackwasser (Ostsee) | 0,5–2,0 | 0,3–0,6 |
| Standard-Seewasser | 4,0–5,5 | 1,0 |
| Tropisches Seewasser | 5,0–6,5 | 1,2–1,5 |
| Persischer Golf | 5,5–7,0 | 1,5–2,0 |

### 2.3 Streustrom-Korrosion — Das 10- bis 1.000-fache

Streustrom-Korrosion (Stray Current Corrosion) ist die mit Abstand gefaehrlichste Form der elektrochemischen Korrosion. Waehrend galvanische Korrosion durch natuerliche Potenzialdifferenzen zwischen Metallen angetrieben wird (typisch 0,1–1,0 V, mikro- bis milliampere), wird Streustrom-Korrosion durch externe Stromquellen verursacht (typisch 12–230 V, milliampere bis ampere).

**Definition:** Streustroeme sind elektrische Stroeme, die nicht dem vorgesehenen Leiterpfad folgen, sondern ueber unbeabsichtigte Wege — insbesondere durch das Wasser und die Unterwasser-Metallteile — fliessen.

**Warum 10- bis 1.000-mal schlimmer:**

| Parameter | Galvanische Korrosion | Streustrom-Korrosion |
|---|---|---|
| Triebkraft | Natuerliche Potenzialdifferenz (0,1–1,0 V) | Externe Spannung (12–230 V) |
| Typischer Strom | Mikroampere bis wenige Milliampere | Milliampere bis Ampere |
| Metallverlust-Rate | 1–10 g/Monat | 10–10.000 g/Monat |
| Zeitraum bis Versagen | Monate bis Jahre | Stunden bis Wochen |
| Vorhersagbarkeit | Hoch (bekannte Materialpaarung) | Gering (intermittierend, quellenabhaengig) |
| Schutz durch Opferanoden | Ja (Standardschutz) | Begrenzt (Anoden schnell verbraucht) |
| Schutz durch ICCP | Ja | Bedingt (bei starkem DC-Streustrom) |
| Sichtbare Warnung | Anodenverbrauch | Oft keine bis zum Versagen |

**Streustrom-Quellen auf Yachten:**

1. **Eigene DC-Anlage (AC/DC-Fehler):**
   - Defekte Isolierung eines DC-Kabels in der Bilge
   - Korrodiertes Massekabel am Motor
   - Defekter Laderegler (Leckstrom zur Masse)
   - Batterie-Erdschluss
   - Instrumenten-Erdschluss

2. **Landstrom-Einspeisung:**
   - Fehlende oder defekte Trennung zwischen Bordnetz-PE und Wassermasse
   - Vertauschte Pol-Zuordnung (N/PE) an der Marina-Saeule
   - Defekter Trenntrafo
   - Fehlende galvanische Isolation

3. **Nachbar-Boote in der Marina:**
   - Nachbarboot mit Erdschluss „schickt" Strom durch das Wasser
   - Gemeinsame Marina-Erdung als Strompfad
   - Schwimmende Stege mit Metallkonstruktion als Leiter

4. **Marina-Infrastruktur:**
   - Kathodischer Schutz der Stahl-Spundwaende (beeinflusst Boote)
   - Defekte Strom-Saeulen
   - Schwimm-Steg-Erdung
   - Unterwasser-Beleuchtung

5. **Schienen/Industrie (selten, aber extrem):**
   - Gleichstrom-Bahnsysteme in Hafennaehe (Straßenbahn, U-Bahn)
   - Industrielle Kathodenschutz-Anlagen
   - Schweissarbeiten am Steg

**Streustrom-Erkennungsmethoden:**

| Methode | Geraet | Empfindlichkeit | Interpretation |
|---|---|---|---|
| Potenzial-Messung (Rumpf vs. Ag/AgCl) | Multimeter + Referenzelektrode | ±1 mV | Potenzial negativer als −1.100 mV → Streustrom |
| Potenzial-Profil (laengs/quer) | Referenzelektrode + Schleppkabel | ±1 mV | Potenzialgradienten → Strompfad lokalisieren |
| Leckstrom-Messung | Clamp-On DC-Milliamperemeter | ±0,1 mA | > 10 mA am Landkabel → Streustrom |
| Isolationswiderstand | Megohmmeter (500 V DC) | 1 MOhm | < 1 MOhm = verdaechtig, < 100 kOhm = Defekt |
| Korrosions-Logger | Langzeit-Potenzial-Logger | ±0,1 mV, 1 s | Tages-/Nachtrhythmus → Marina-Streustrom |
| Silver/Silver-Chloride Half-Cell | ABYC-E2-Referenz | ±1 mV | Standard-Referenz fuer alle Messungen |

### 2.4 Korrosionsarten im Detail

#### 2.4.1 Bimetall-Korrosion (klassisch galvanisch)

Zwei unterschiedliche Metalle in elektrischer Verbindung und gemeinsamem Elektrolyten. Das unedlere Metall (Anode) loest sich auf.

**Typische Yacht-Paare (gefaehrlich):**
- Edelstahl-Welle in Bronze-Stevenrohr (ohne Isolation)
- Aluminium-Saildrive-Gehaeuse neben Bronze-Seeventil
- Kohlenstoff-Kielschraube in Blei-Kielballast
- Stahl-Drahtseil an Edelstahl-Terminal

**Schutzmassnahmen:**
- Gleiche Metalle verwenden (ideal)
- Galvanische Isolation (Kunststoff-Buchsen, Gummi-Zwischenlagen)
- Opferanoden (Potenzial der Anode negativer als beide Metalle)
- ICCP (Potenzial aktiv in Schutzbereich regeln)
- Beschichtung der Kathode (reduziert wirksame Kathodenflaeche)

#### 2.4.2 Entzinkung (Dezincification)

Selektive Korrosion von Zink aus Messing (CuZn-Legierungen). Das Bauteil behalt seine Form, wird aber weich, poroees und kupferrot.

**Betroffene Materialien:**
- Alpha-Messing (CuZn37): Besonders anfaellig
- Messing mit > 15% Zink: Grundsaetzlich gefaehrdet
- Rotguss (CuSn): NICHT betroffen (kein Zink)
- DZR-Messing (Dezincification Resistant): Legierungszusaetze (Arsen, Antimon) hemmen Entzinkung

**AYDI-Erkennung (visuell):**
- Kupferrote Verfaerbung an normalerweise gelben Messingteilen
- Blasenbildung auf der Oberflaeche
- Reduzierte Wandstaerke bei gleichbleibender Kontur
- Weiche, broeckelige Konsistenz bei Druck

#### 2.4.3 Lochfrass (Pitting Corrosion)

Lokalisierte Korrosion, die tiefe, schmale Loecher bildet. Besonders gefaehrlich, weil der Materialverlust gering erscheint, die Durchdringung aber schnell sein kann.

**Besonders betroffen:**
- Edelstahl 316L: Bei fehlendem Sauerstoff (unter Biofilm, in Spalten)
- Aluminium: Bei Kontakt mit Kupfer-Ionen (auch geloest aus Antifouling)
- Kupfer-Nickel: Bei hoher Stroemungsgeschwindigkeit (Erosions-Korrosion)

**Mechanismus bei Edelstahl:**
1. Passivschicht wird lokal beschaedigt (mechanisch, chemisch, Chlorid)
2. Unter der Beschaedigung bildet sich eine Korrosionszelle
3. pH-Wert in der Grube sinkt (Hydrolyse der Metallionen)
4. Saures Mikromilieu beschleunigt Korrosion
5. Autokatalytischer Prozess — Grube waechst exponentiell

**Schutztemperatur-Grenze (Edelstahl 316L):**
- PRE (Pitting Resistance Equivalent) = %Cr + 3,3 x %Mo + 16 x %N
- 316L: PRE = 23–28 → CPT (Critical Pitting Temperature) ca. 15–25 C
- 2205 Duplex: PRE = 34–38 → CPT ca. 40–50 C
- Praxis: In tropischem Seewasser (> 28 C) ist 316L anfaellig fuer Lochfrass

#### 2.4.4 Spaltkorrosion (Crevice Corrosion)

In engen Spalten (0,025–0,1 mm) entsteht Sauerstoffverarmung. Die Korrosion folgt einem aehnlichen Mechanismus wie Lochfrass, ist aber noch gefaehrlicher, weil Spalten an Yachten allgegenwaertig sind.

**Typische Spalt-Orte:**
- Flansch-Verbindungen (Seeventile, Rohrkupplungen)
- Unter Dichtungen und O-Ringen
- Gewinde (Schrauben in Muttern)
- Unter Belag/Biofilm/Muscheln
- Unter Schlauchschellen
- In Rohrhalterungen

**Schutz:**
- Spaltvermeidung (Schweissen statt Schrauben, wo moeglich)
- Dichtmassen, die Spalte fuellen (Sikaflex, 3M 5200)
- Hoeherwertiger Edelstahl (2205 Duplex)
- Kathodischer Schutz (Anoden oder ICCP)

#### 2.4.5 Erosions-Korrosion

Kombination aus mechanischem Abtrag (Stroemung, Kavitation) und elektrochemischer Korrosion. Die schuetzende Passiv-/Oxidschicht wird staendig entfernt, neue Metalloberflaeche wird exponiert.

**Typische Orte auf Yachten:**
- Propellerblatt-Kanten (Kavitation)
- Kuehwasser-Einlaesse (hohe Stroemungsgeschwindigkeit)
- Waermetauscher-Rohre (Turbulenzen)
- Seeventil-Innenseiten (Stroemungsabloesung)

**Kritische Stroemungsgeschwindigkeiten:**

| Material | Max. Stroemung (m/s) | Anwendung |
|---|---|---|
| Kupfer (rein) | 1,0 | Rohrleitungen (langsam) |
| Kupfer-Nickel 90/10 | 2,5 | Standard-Kuehlwasser |
| Kupfer-Nickel 70/30 | 3,5 | Hochleistungs-Kuehlsystem |
| Edelstahl 316L | 5,0 | Pumpengehaeuse |
| Titan | > 20 | ICCP-Anoden |

#### 2.4.6 Interkristalline Korrosion

Korrosion entlang der Korngrenzen eines Metalls. Betrifft vor allem sensibilisierte Edelstaehle (durch Schweissen oder Waermebehandlung).

**Mechanismus:**
- Bei 450–850 C bildet sich Chromkarbid (Cr23C6) an Korngrenzen
- Die chromverarmte Zone neben der Korngrenze wird anodisch
- Korrosion laeuft bevorzugt entlang der Korngrenzen
- Bauteil kann ohne sichtbare Verformung versagen

**Schutz:**
- Niedrigkohlenstoff-Staehle verwenden (316L statt 316, „L" = Low Carbon)
- Stabilisierte Staehle (321 mit Titan, 347 mit Niob)
- Loesungsgluehen nach dem Schweissen
- Minimale Waermeeinbringung beim Schweissen

#### 2.4.7 Spannungsrisskorrosion (Stress Corrosion Cracking — SCC)

Kombination aus Zugspannung (mechanisch oder Eigenspannung) und korrosiver Umgebung fuehrt zu Rissbildung — oft ohne vorherige sichtbare Korrosion.

**Betroffene Materialien auf Yachten:**
- Edelstahl 316L: In warmem, chloridhaltigem Wasser unter Zugspannung
- Messing: In ammoniakhaltiger Atmosphaere (Faekalien, Reinigungsmittel)
- Aluminium 7000-Serie: In feuchter Meeresluft unter Last
- Edelstahl-Drahtseile (1x19 Rigg): Unter Vorspannung in Salzwasser

**Yacht-relevante Situationen:**
- Want-Terminals aus Edelstahl: Dauerbelastet, salzhaltige Umgebung
- Ruderlager aus Edelstahl: Hohe mechanische Last, Seewasser-Kontakt
- Kielbolzen aus Edelstahl: Dauerbelastet, potenziell feucht
- Prop-Wellen: Biegung + Torsion + Seewasser

### 2.5 Kathodischer Schutz — Grundprinzip

Das Prinzip des kathodischen Schutzes: Die zu schuetzende Struktur wird zur Kathode gemacht. Korrosion findet dann nur noch an der Opferanode (passiver Schutz) oder an der Fremdstromanode (aktiver Schutz/ICCP) statt.

**Schutzbedingung:**
```
E_Struktur < E_Schutz    (negativer = geschuetzt)
```

| Werkstoff | Schutzpotenzial min. (mV vs. Ag/AgCl) | Schutzpotenzial max. (mV vs. Ag/AgCl) | Ueberprotektion-Risiko |
|---|---|---|---|
| Kohlenstoffstahl | −800 | −1.100 | Wasserstoffversprödung > −1.100 |
| Edelstahl 316L | −500 | −1.100 | Wasserstoffversprödung > −1.100 |
| Kupfer / Bronze | −300 | −650 | Beschichtungs-Enthaftung > −650 |
| Aluminium | −800 | −1.100 | Alkaliversprödung > −1.100, STRIKT einhalten! |
| Blei | −600 | −900 | Selten problematisch |

**Anodenauswahl nach Werkstoff:**

| Anodenmaterial | Offenes Potenzial (mV vs. Ag/AgCl) | Schuetzt (typisch) | Einsatzgebiet |
|---|---|---|---|
| Zink (Zn) | −1.030 bis −1.050 | Stahl, Bronze, Edelstahl | Seewasser (Standard) |
| Aluminium (Al-Zn-In) | −1.050 bis −1.100 | Stahl, Bronze, Edelstahl, Aluminium | See- und Brackwasser (universell) |
| Magnesium (Mg) | −1.580 bis −1.630 | Stahl, Bronze, Edelstahl | Suesswasser (hohe Triebspannung noetig) |

### 2.6 ICCP-Prinzip im Detail

ICCP (Impressed Current Cathodic Protection) nutzt eine externe Gleichstromquelle, um das Potenzial der zu schuetzenden Struktur aktiv in den Schutzbereich zu regeln.

**Systemkomponenten:**

1. **Referenzelektrode:** Misst das aktuelle Potenzial der Rumpfoberflaeche
   - Silber/Silberchlorid (Ag/AgCl): Standard, stabil, genau
   - Zink-Referenz: Einfacher, guenstiger, weniger genau
   - Platzierung: Min. 300 mm vom naechsten Beschlag, moeglichst mittschiffs

2. **Steuergeraet (Controller):** Vergleicht Ist-Potenzial mit Soll-Potenzial
   - Soll-Bereich: typisch −850 bis −1.050 mV vs. Ag/AgCl
   - Regelalgorithmus: PID oder Stufenregelung
   - Ausgangsstrom: typisch 0,5–10 A (Yachten), bis 50 A (Megayachten)
   - Spannungsbereich: 0–12 V DC (typisch)

3. **Fremdstromanode:** Verteilt den Schutzstrom ins Wasser
   - Titan mit MMO-Beschichtung (Mixed Metal Oxide): Standard, 15–25 Jahre
   - Titan-Platin: Premium, > 25 Jahre
   - Silizium-Eisen (FeSi): Preisguenstig, kuerzer (5–10 Jahre)
   - Graphit: Veraltet, wird nicht mehr empfohlen

4. **Kabelung und Durchfuehrungen:**
   - Min. 6 mm² Kupfer (tinned marine grade)
   - Wasserdichte Durchfuehrungen (IP68)
   - Separate Sicherung am Controller
   - Kein gemeinsamer Stromkreis mit anderen Verbrauchern

**ICCP-Dimensionierung (vereinfacht):**

```
Erforderlicher Schutzstrom (A) = Zu_schuetzende_Flaeche (m²) x Stromdichte (mA/m²) / 1.000

Stromdichte-Richtwerte:
  Nackte Stahlflaeche:         80–150 mA/m²
  Beschichteter Stahl (gut):   5–20 mA/m²
  Beschichteter Stahl (alt):   20–50 mA/m²
  Aluminium (blank):           10–30 mA/m²
  Aluminium (beschichtet):     2–10 mA/m²
  Bronze/Kupfer:               20–50 mA/m²
  GFK-Rumpf (nur Beschlaege):  Summe der Einzelflaechen
```

**ICCP vs. Opferanoden — Entscheidungsmatrix:**

| Kriterium | Opferanoden | ICCP |
|---|---|---|
| Anschaffungskosten | 80–600 EUR | 2.500–15.000+ EUR |
| Laufende Kosten/Jahr | 80–600 EUR (Anodenwechsel) | 50–200 EUR (Strom, Kalibrierung) |
| Wartungsaufwand | Jaehrlich (Haul-Out) | Kalibrierung 1–2x/Jahr |
| Schutzguete | Gut (nachlassend mit Verbrauch) | Exzellent (konstant) |
| Eignung Aluminiumrumpf | Bedingt (Ueberprotektion-Risiko) | Ideal (Potenzialregelung) |
| Eignung GFK-Rumpf | Standard | Sinnvoll ab 15 m LOA |
| Eignung Stahlrumpf | Standard | Empfohlen ab 20 m LOA |
| Strombedarf | Keiner | 10–100 W permanent |
| Versagen-Modus | Langsam (Anoden verbraucht) | Abrupt (Stromausfall) |
| Backup-Empfehlung | Keine | Opferanoden als Backup |
| Hydrodynamik | Widerstand durch Anoden | Flache Anoden, weniger Widerstand |
| Eignung Motorsailer | Standard bis 15 m | Empfohlen > 15 m |
| Eignung Megayacht > 24 m | Unzureichend allein | Standard/Pflicht |

### 2.7 Blitzschutz — Grundlagen

#### 2.7.1 Blitzstatistik und Yacht-Risiko

| Region | Blitzdichte (Blitze/km²/Jahr) | Jaehrliches Risiko pro Yacht |
|---|---|---|
| Ostsee | 0,5–2,0 | 1:5.000 |
| Nordsee | 1,0–3,0 | 1:3.000 |
| Mittelmeer (Sommer) | 2,0–6,0 | 1:1.500 |
| US-Ostkueste (Sommer) | 4,0–12,0 | 1:500 |
| Florida / Golf von Mexiko | 8,0–16,0 | 1:200 |
| Tropen (Malakkastrasse) | 10,0–20,0 | 1:150 |

**Schadensarten durch Blitzeinschlag:**
- **Direkte thermische Zerstoerung:** Durchschmelzen von Masten, Wanten, Antennenkabeln (30.000+ C)
- **Seitenueberschlag (Side Flash):** Blitz springt von Mast auf nahes Metallteil (0,3–2 m)
- **Induktive Kopplung:** Elektromagnetischer Puls zerstoert Elektronik (Reichweite 3–10 m)
- **Druckwelle:** Explosionsartige Erhitzung von Feuchtigkeit in Mast/GFK → Delaminierung, Rissbildung
- **Rumpf-Durchschlag:** Bei fehlender Ableitung springt Strom durch GFK-Rumpf ins Wasser (Brandgefahr, Leck)

#### 2.7.2 Blitzschutz-Zonenkonzept (ABYC TE-4 / IEC 62305)

Der Schutz basiert auf einem Zonenkonzept:

**Zone of Protection (Schutzzone):**
- Definiert als Kegel mit 60°-Oeffnungswinkel von der Mastspitze
- Alles innerhalb dieses Kegels ist geschuetzt
- Bei Ketsch/Yawl: Ueberlappende Zonen von Gross- und Besanmast

**Berechnung Schutzradius:**
```
Schutzradius am Wasserniveau (m) = Masthoehe_ueber_Wasser (m) x tan(30°)
                                 = Masthoehe x 0,577

Beispiele:
  Mast 15 m → Radius  8,7 m (ausreichend fuer 10-m-Segler)
  Mast 20 m → Radius 11,5 m (ausreichend fuer 13-m-Segler)
  Mast 25 m → Radius 14,4 m (ausreichend fuer 16-m-Segler)
```

**Blitzableiter-Pfad (Anforderungen ABYC TE-4):**

1. **Fangeinrichtung (Air Terminal):** An der Mastspitze
   - Material: Kupfer (min. 10 mm Durchmesser) oder Edelstahl (min. 12 mm)
   - Hoehe ueber Mastspitze: Min. 150 mm
   - Kupferbuerste oder -spitze

2. **Ableitung (Down Conductor):** Von Mastspitze zum Erdungspunkt
   - Querschnitt: Min. 4 AWG (21 mm²) Kupfer
   - Ideal: Mast selbst (Aluminium) + separater Kupferleiter als Backup
   - Keine scharfen Biegungen (Radius > 200 mm, Winkel > 90° vermeiden)
   - Max. 2 Verbindungsstellen (Kompression, kein Lot)

3. **Erdungsplatte (Grounding Plate):**
   - Min. Flaeche: 0,1 m² (929 cm²) in direktem Wasserkontakt
   - Material: Kupfer (bevorzugt), Bronze, oder Dynaplate (gesinterte Bronze)
   - Platzierung: Moeglichst tief, moeglichst mittschiffs
   - Nicht in Kielnaehe (Luftblasen-Feld)
   - Nicht die Motorwelle als Erdung verwenden (Lagerschaeden!)

4. **Potenzialausgleich (Bonding):**
   - Alle metallischen Gegenstaende im Umkreis von 1,8 m um den Ableiterpfad muessen mit dem Blitzschutz-Bonding verbunden sein
   - Min. 6 AWG (13 mm²) Kupfer fuer Blitz-Bonding
   - Ziel: Seitenueberschlag verhindern

#### 2.7.3 Elektronik-Schutz

**Induktiver Schutz (wichtiger als direkter Schutz):**
- Alle Signalkabel abgeschirmt fuehren (geschirmte Marinekabel)
- Kabelschleifen vermeiden (parallel fuehren, nicht in Ringform)
- Surge Protector / SPD (Surge Protective Device) an:
  - Antennenkabel (VHF, AIS, Radar, GPS, Sat)
  - Landstrom-Einspeisung
  - NMEA 2000 / Ethernet Backbone
  - UKW-Antenne (koaxial, mit Gas-Entlader)
- Ferritkerne auf Signalkabeln am Mastfuss

**Praktische Massnahmen (Gewitterwarnung):**
- Wetterbericht / Blitzwarnung beachten
- Wenn moeglich: Antennen von Koaxkabeln trennen (Stecker loesen)
- GPS-Empfaenger/Plotter ausschalten (induktive Kopplung)
- Handgeraete (Hand-UKW, Handy, Tablet) in Alukoffer / Mikrowelle legen (Faradayscher Kaefig)
- Nicht den Mast oder metallische Wanten beruehren

### 2.8 Bonding-Systeme — Das Gesamtkonzept

Bonding ist die elektrische Verbindung aller metallischen Unterwasserteile und weiterer Metallkomponenten zu einem gemeinsamen Potenzialausgleich. Es gibt drei unterschiedliche Bonding-Zwecke, die oft im gleichen System realisiert, aber unterschiedlich dimensioniert werden:

#### 2.8.1 DC-Bonding (Korrosionsschutz)

**Zweck:** Alle Unterwasser-Metallteile auf gleiches Potenzial bringen, um galvanische Korrosion innerhalb des Bootes zu verhindern und den kathodischen Schutz (Anoden/ICCP) auf alle Komponenten zu verteilen.

**Verbundene Komponenten (Pflicht):**
- Alle Seeventile und Borddurchlaesse
- Propellerwelle(n) (ueber Wellenerdungsbuerste)
- Ruderschaft
- Kielbolzen
- Saildrive-Gehaeuse
- Trimm-Klappen
- Echolot-/Log-Geber (metallisch)
- Bugstrahlruder-Tunnel (wenn metallisch)

**Verbundene Komponenten (empfohlen):**
- Motor-Motorblock (ueber Motorerdung)
- Tankkoerper (Diesel, Wasser — wenn metallisch)
- Windenzaehlwerk (Ankerwinsch)
- Bugrolle (wenn metallisch)

**NICHT verbinden (Yacht-spezifisch):**
- Aluminium-Mast: Nur ueber Blitzschutz-Bonding, NICHT direkt ins DC-Bonding (grosse Kathodenflaeche unter Wasser wuerde Opferanoden schnell verbrauchen)
- Stehende Rigg-Draehte: Nur Blitz-Bonding
- Aluminium-Reling: Nur bei Aluminiumbooten

**Kabelquerschnitte (ABYC E-2):**
- Bonding-Hauptleiter (Bus-Bar zu Bus-Bar): Min. 8 AWG (8,4 mm²)
- Bonding-Abzweig (Bus-Bar zu Seeventil): Min. 8 AWG (8,4 mm²)
- Gesamtlaenge < 15 m: 8 AWG ausreichend
- Gesamtlaenge > 15 m oder > 20 Verbindungspunkte: 6 AWG (13,3 mm²) erwaegen
- Material: Kupfer, verzinnt (tinned marine copper)
- Kabelschuhe: Vergoldet oder verzinnt, gecrimpt UND geloetet

**Widerstandsgrenzwerte:**
- Jede Bonding-Verbindung (Kabel + Anschluss): < 1 Ohm (ABYC)
- Gesamtsystem (entferntestes Seeventil zum Anodenfeld): < 1 Ohm
- Ideal: < 0,5 Ohm
- Messung: 4-Leiter-Messung (Kelvin), nicht einfaches Multimeter

#### 2.8.2 RF-Bonding (Funkerdung / Gegengewicht)

**Zweck:** Gegengewicht (Counterpoise) fuer SSB/Kurzwellen-Funkanlagen. Das Bonding-System dient als kapazitive Flaeche gegen das Seewasser.

**Spezifische Anforderungen:**
- Kupferfolien oder -baender (breit, duenn) entlang der Innenseite des Rumpfes
- Verbindung zu Kiel, Ruder, Propeller (kapazitive Kopplung)
- Dynaplate als kombinierte Funk-/Blitz-Erdung
- Min. 10 m² effektive Gegengewichtsflaeche fuer SSB-Funkanlage

**Unterschied zu DC-Bonding:**
- RF-Bonding erfordert FLAECHE (nicht nur leitenden Pfad)
- Hochfrequenz-taugliche Verbindungen (kurz, breit, induktivitaetsarm)
- Kupferband statt Rundkabel

#### 2.8.3 Lightning-Bonding (Blitzpotenzialausgleich)

**Zweck:** Alle metallischen Gegenstaende in der Naehe des Blitzableiterpfades auf gleiches Potenzial bringen, um Seitenueberschlaege zu verhindern.

**Verbundene Komponenten:**
- Alle metallischen Gegenstaende innerhalb 1,8 m vom Ableiterpfad
- Wanten und Stagen (ueber Wantspanner → Bonding-Bus)
- Reling / Seereling (Standfuesse)
- Winschsockel
- Steuerrad (wenn metallisch)
- Bugkorb / Heckkorb

**Kabelquerschnitt:** Min. 6 AWG (13,3 mm²) — dicker als DC-Bonding!

**Integration der drei Systeme:**

In der Praxis laesst sich ein kombiniertes Bonding-System realisieren:
- Ein gemeinsamer Bonding-Bus (Kupferschiene, min. 25 x 3 mm)
- DC-Bonding-Abzweige in 8 AWG zu allen Unterwasser-Metallen
- Lightning-Bonding-Abzweige in 6 AWG zu allen Deck-Metallen nahe Mast
- RF-Kupferband als Ergaenzung fuer Funk-Gegengewicht
- Alle Systeme treffen sich an der Erdungsplatte / Blitz-Erdung

**Gemeinsamer Bonding-Bus vs. getrennte Systeme:**

| Aspekt | Gemeinsam | Getrennt |
|---|---|---|
| Installation | Einfacher | Aufwendiger |
| Wartung | Einfacher | Aufwendiger |
| Korrosionsrisiko | Leicht erhoht (mehr verbundene Metalle) | Optimal (nur noetige Verbindungen) |
| Blitzschutz | Optimal (voller Potenzialausgleich) | Risiko Seitenueberschlag |
| Funkleistung | Gut (wenn Kupferband ergaenzt) | Optimal (dediziertes RF-Ground) |
| ABYC-Empfehlung | Standard fuer Yachten < 24 m | Empfohlen fuer > 24 m |

---

## 3. Typenuebersicht

### 3.1 Zinkanoden (Zn)

**Legierungszusammensetzung (MIL-A-18001K):**
- Zink: Min. 99,3%
- Aluminium: 0,1–0,5%
- Kadmium: 0,025–0,07% (aktiviert die Oberflaeche)
- Eisen: Max. 0,005% (KRITISCH: Fe > 0,005% → Anode passiviert!)
- Blei: Max. 0,006%
- Kupfer: Max. 0,005%
- Silizium: Max. 0,125%

**Elektrochemische Leistungsdaten:**
| Parameter | Wert |
|---|---|
| Offenes Potenzial | −1.030 bis −1.050 mV (vs. Ag/AgCl) |
| Arbeitspotenzial | −1.000 bis −1.030 mV (vs. Ag/AgCl) |
| Theoretische Kapazitaet | 820 Ah/kg |
| Praktische Kapazitaet | 780 Ah/kg (95% Effizienz) |
| Stromdichte | 0,5–1,5 A/m² |
| Verbrauchsrate | 10,7 kg/A·Jahr |
| Max. Betriebstemperatur | 50 C (darueber Passivierung) |
| Min. Salzgehalt | > 20 ppt (Seewasser) |

**Vorteile:**
- Kostenguenstig
- Bewaehrte Technologie (80+ Jahre Erfahrung)
- Keine Ueberprotektion moeglich (Potenzial nicht negativ genug fuer Aluversprödung)
- Weit verbreitet, ueberall erhaeltlich

**Nachteile:**
- Versagt in Suesswasser und Brackwasser (passiviert unter 20 ppt)
- Bildet kalkhaltige Ablagerungen (Calcareous Deposits)
- Relativ hohe Verbrauchsrate
- Kadmium-Gehalt oekologisch problematisch (EU-Diskussion)
- Bei hohen Temperaturen (> 40 C) Passivierungsgefahr

**Einsatzgebiet:**
- Standardschutz fuer Seewasser-Yachten
- GFK-Rumpf mit Bronze-/Edelstahl-Beschlaegen
- Stahlrumpf (Seewasser)

### 3.2 Aluminiumanoden (Al-Zn-In)

**Legierungszusammensetzung (MIL-DTL-24779C / DNV-RP-B401):**
- Aluminium: Basis (Rest)
- Zink: 2,0–6,0%
- Indium: 0,01–0,03%
- Silizium: Max. 0,12%
- Eisen: Max. 0,09%
- Kupfer: Max. 0,003%
- Kadmium: Max. 0,002%

**Elektrochemische Leistungsdaten:**
| Parameter | Wert |
|---|---|
| Offenes Potenzial | −1.050 bis −1.100 mV (vs. Ag/AgCl) |
| Arbeitspotenzial | −1.030 bis −1.080 mV (vs. Ag/AgCl) |
| Theoretische Kapazitaet | 2.830 Ah/kg |
| Praktische Kapazitaet | 2.400–2.700 Ah/kg (85–95%) |
| Stromdichte | 1,0–3,0 A/m² |
| Verbrauchsrate | 3,2–3,6 kg/A·Jahr |
| Max. Betriebstemperatur | 80 C |
| Min. Salzgehalt | > 5 ppt (Brackwasser geeignet!) |

**Vorteile:**
- 3x hoehere Kapazitaet pro kg als Zink → laengere Standzeit oder geringeres Gewicht
- Funktioniert in Brackwasser (Ostsee!)
- Kein Kadmium → oekologisch vorzuziehen
- Leichter als Zink (2,7 vs. 7,1 g/cm³)
- Funktioniert bei hoeheren Temperaturen

**Nachteile:**
- Etwas teurer pro Stueck (aber guenstiger pro Schutzjahr)
- Leicht hoeheres Potenzial → minimales Ueberprotektions-Risiko bei sehr alten Beschichtungen
- Nicht ueberall in allen Formen verfuegbar
- Empfindlicher gegen Verunreinigungen in der Legierung

**Einsatzgebiet:**
- Universell empfohlen fuer Seewasser und Brackwasser
- Aluminiumruempfe (Potenzial sorgfaeltig abstimmen!)
- Offshore-Strukturen (Standard)
- Zunehmend als Ersatz fuer Zink auch bei Yachten

### 3.3 Magnesiumanoden (Mg)

**Legierungszusammensetzung (ASTM B843 / ABYC E-2):**
- Magnesium: Basis (Rest)
- Aluminium: 5,3–6,7% (AZ-63-Legierung)
- Zink: 2,5–3,5%
- Mangan: Min. 0,15%
- Eisen: Max. 0,003%
- Kupfer: Max. 0,02%
- Nickel: Max. 0,002%

**Elektrochemische Leistungsdaten:**
| Parameter | Wert |
|---|---|
| Offenes Potenzial | −1.580 bis −1.630 mV (vs. Ag/AgCl) |
| Arbeitspotenzial | −1.500 bis −1.580 mV (vs. Ag/AgCl) |
| Theoretische Kapazitaet | 2.200 Ah/kg |
| Praktische Kapazitaet | 1.100–1.230 Ah/kg (50–56%) |
| Stromdichte | 5–20 A/m² |
| Verbrauchsrate | 7,0–8,0 kg/A·Jahr |
| Max. Betriebstemperatur | 65 C |
| Min. Salzgehalt | 0 ppt (Suesswasser!) |

**Vorteile:**
- Funktioniert in Suesswasser (hohe Triebspannung noetig wegen geringer Leitfaehigkeit)
- Einzige Opferanodenart fuer reine Suesswasser-Anwendungen
- Hoher Stromoutput (gut fuer schlecht isolierte Strukturen)

**Nachteile:**
- Sehr hohe Verbrauchsrate (geringe Effizienz von nur 50%)
- UEBERPROTEKTION in Seewasser! → Alkaliversprödung von Aluminium, Beschichtungs-Enthaftung
- **NIEMALS in Seewasser verwenden** (Potenzial viel zu negativ)
- Nicht fuer Aluminiumruempfe in Seewasser (zerstoererisch)
- Kurze Standzeit (6–12 Monate in Suesswasser)

**Einsatzgebiet:**
- Ausschliesslich Suesswasser (Binnenseen, Fluesse)
- Stahlruempfe in Suesswasser
- GFK-Boote mit Metallbeschlaegen in Suesswasser
- Heisswasser-Boiler an Bord (Suess-/Trinkwasser)

### 3.4 Galvanischer Isolator (Galvanic Isolator)

**Funktionsprinzip:**
Ein galvanischer Isolator ist ein elektronisches Bauteil, das in den Schutzleiter (PE / Safety Ground) der Landstrom-Einspeisung eingebaut wird. Er blockiert die kleinen Gleichspannungen (< 1,2 V), die galvanische Korrosion und Streustroeme verursachen, laesst aber den vollen Fehlerstrom (> 1,2 V) bei einem Isolationsfehler passieren.

**Aufbau:**
- Zwei antiparallele Silizium-Dioden-Paare in Serie
- Schwellenspannung: 2 x 0,6 V = 1,2 V (blockiert galvanische Spannungen)
- Bei Fehlerstrom (> 1,2 V): Dioden leiten, voller Sicherheitsstrom fliesst
- Zusaetzlich: Hochfrequenz-Bypass-Kondensator (gegen Stoerstrahlung)
- Monitoring-LED oder Alarmanschluss

**Elektrische Spezifikation (typisch):**

| Parameter | Wert |
|---|---|
| Blockierspannung | ±1,2 V DC |
| Durchlass-Fehlerstrom | 30 A min. (fuer 30-A-Landanschluss) |
| Durchlassspannung bei 30 A | < 1,5 V |
| Dauerstrom | 30 A / 50 A / 100 A (je nach Modell) |
| Ueberlastfestigkeit | > 3.000 A fuer 0,1 s (Kurzschluss) |
| Rueckstrom (unter 1,2 V) | < 1 mA |
| Temperaturbereich | −20 bis +70 C |
| Schutzart | IP67 (geschlossenes Gehaeuse) |

**Installation:**
- In den gruen-gelben Schutzleiter (PE) der Landstrom-Einspeisung
- Moeglichst nahe an der Landstrom-Einspeisung (Landanschluss)
- Nach dem Hauptschalter, vor dem Verteiler
- Keine Sicherung im PE-Leiter! (Der Isolator IST der einzige zulaessige Eingriff im PE)
- Korrektes Gehaeuse (IP67) im Maschinenraum oder Cockpit-Locker

**ABYC-E-11-Anforderungen:**
- Fail-Safe-Design: Bei Ausfall des Isolators muss PE durchverbunden sein (nicht offen!)
- Monitoring: Status-LED oder Alarm bei Diodendefekt
- Nennstrom mindestens gleich Landanschluss-Sicherung
- Zugelassen nach UL 1500 oder gleichwertig

**Vorteile:**
- Einfache Installation (ein Bauteil, zwei Anschluesse)
- Kostenguenstig (150–500 EUR)
- Passiv (kein Strombedarf)
- Blockiert 90% der Marina-Streustrom-Probleme
- Sicherheitsfunktion (PE) bleibt erhalten

**Nachteile:**
- Blockiert NUR galvanische Spannungen < 1,2 V (nicht starke DC-Streustroeme)
- Bei AC-Fehlerstrom ist der Schutzleiter-Widerstand leicht erhoeht
- Dioden koennen altern oder durch Ueberspannung ausfallen → regelmaessige Pruefung
- Schutzt nicht gegen AC-Streustroeme (dafuer Trenntrafo noetig)

### 3.5 Trenntrafo (Isolation Transformer)

**Funktionsprinzip:**
Ein Trenntrafo erzeugt eine vollstaendige galvanische Trennung zwischen der Marina-Stromversorgung und dem Bordnetz. Das Bordnetz ist nach dem Trafo ein eigenes, ungeerdetes (floating) System — oder wird an Bord neu geerdet (empfohlen).

**Vorteile gegenueber galvanischem Isolator:**
- Vollstaendige galvanische Trennung (DC und AC)
- Keine Streustroeme moeglich (kein gemeinsamer Erdpfad)
- Spannungsanpassung moeglich (z.B. 60 Hz / 120 V → 50 Hz / 230 V mit Frequenzwandler)
- Stoerunterdrueckung (Spannungsspitzen, Oberwellen)

**Nachteile:**
- Teuer (1.500–8.000 EUR fuer Yacht-Trenntrafos)
- Schwer und gross (5–50 kg je nach Leistung)
- Eigenverluste (2–5% Waerme)
- Kuehlungsbedarf (Luft oder Wasser)
- Professionelle Installation erforderlich

**Yacht-Trenntrafo-Spezifikationen:**

| Leistungsklasse | Typische Yacht-Groesse | Gewicht | Abmessungen (ca.) | Preis (EUR) |
|---|---|---|---|---|
| 3,5 kVA | 8–10 m | 12 kg | 250 x 200 x 180 mm | 1.500–2.500 |
| 7,5 kVA | 10–14 m | 22 kg | 300 x 250 x 220 mm | 2.500–4.000 |
| 12 kVA | 14–18 m | 35 kg | 350 x 300 x 260 mm | 3.500–5.500 |
| 16 kVA | 18–22 m | 45 kg | 400 x 350 x 300 mm | 4.500–7.000 |
| 25 kVA | 22–30 m | 65 kg | 450 x 400 x 350 mm | 6.000–10.000 |
| 50 kVA | 30+ m | 120 kg | 600 x 500 x 450 mm | 10.000–18.000 |

### 3.6 Blitzschutz-Systeme

#### 3.6.1 Passive Blitzableiter

**Mastspitzen-Fangeinrichtung (Air Terminal):**
- Kupferstange oder -bueschel, min. 150 mm ueber Mastspitze
- Durchmesser: min. 10 mm Kupfer / 12 mm Edelstahl
- Form: Spitze (konzentriert Ladung) oder Bueschel (groessere Fangflaeche)
- Befestigung: Edelstahl-Schelle am Mast, isoliert montiert (keine Kurzschlussschleife zum Rigg)

**Ableiterkabel:**
- Min. 4 AWG (21 mm²) Kupfer, verzinnt
- Keine scharfen Biegungen (Innenradius > 200 mm)
- Alle 90°-Boegen vermeiden (Lichtbogengefahr bei > 100 kA)
- Befestigung: Kunststoff-Kabelschellen, nicht metallisch (Induktion)
- Fuehrung: moeglichst direkt (kuerzester Weg von Mastspitze zu Erdung)

**Erdungsplatte/Erdungsfinger:**
- Min. 0,1 m² (929 cm²) leitfaehige Flaeche in Wasserkontakt
- Alternativen:
  - Massive Kupferplatte (6 mm dick, aussen am Rumpf verschraubt)
  - Dynaplate (gesinterte Bronze, poroes, groessere effektive Flaeche)
  - Kiel-Erdung (bei Metallkiel direkt nutzbar)
  - Propellerwelle (nur als ZUSAETZLICHE Erdung, nicht allein — Lagerschaden!)

#### 3.6.2 Aktive Blitzschutz-Systeme (dissipativ)

**Dissipative Air Terminals (z.B. LoE — Lightning Overvoltage Eliminator):**
- Behauptung: Ionisierung der Luft um die Mastspitze verhindert Blitzeinschlag
- Prinzip: Viele feine Spitzen (Corona-Entladung) sollen Ladung langsam ableiten
- **ABYC-Position:** Nicht als alleiniger Schutz empfohlen, da Wirksamkeit wissenschaftlich nicht belegt
- **AYDI-Bewertung:** Als ERGAENZUNG zu konventionellem Schutz akzeptabel, NICHT als Ersatz

### 3.7 Bonding-Systemkomponenten

**Bonding-Bus-Bar:**
- Kupferschiene: Min. 25 x 3 mm (fuer Yachten bis 15 m)
- Kupferschiene: Min. 40 x 5 mm (fuer Yachten 15–25 m)
- Kupferschiene: Min. 50 x 6 mm (fuer Yachten > 25 m)
- Oberflaeche: Verzinnt
- Befestigung: Isoliert (Kunststoff-Abstandshalter)
- Anschluss: Edelstahl-Schrauben M6/M8 mit Federscheiben

**Wellenerdungsbuerste:**
- Kohle-/Silber-Buerste auf der rotierenden Welle
- Uebergangswiderstand: < 0,01 Ohm (neu), < 0,1 Ohm (Wartungsgrenze)
- Wartung: Jaehrlich pruefen, alle 2–3 Jahre ersetzen
- Alternative: Quecksilber-Kontakt (Mercury Wetted Slip Ring) — teurerer, wartungsfreier

**Bonding-Kabelschuhe:**
- Verzinntes Kupfer oder vergoldet
- Gecrimpt UND geloetet (nicht nur eins von beiden)
- Schrumpfschlauch ueber Crimp-Bereich (Feuchtigkeitsschutz)
- Kontaktflaeche an Seeventil: Blank schleifen, Anti-Seize-Paste (KEIN Fett)

---

## 4. Produktlinien und Spezifikationen

### 4.1 MG Duff (UK)

MG Duff ist der weltweit fuehrende Hersteller von Opferanoden fuer den Yachtbau und die Schifffahrt, seit 1956.

**Anoden-Serien:**

#### Zinkanoden (Seewasser)

| Modell | Typ | Gewicht (kg) | Abmessungen (mm) | Befestigung | Anwendung | Preis (EUR, ca.) |
|---|---|---|---|---|---|---|
| ZD50 | Wellenanoden (Donut) | 0,4 | ID 25 / AD 65 x 25 | Klemmschelle | Welle 25 mm | 12–18 |
| ZD52 | Wellenanoden (Donut) | 0,8 | ID 30 / AD 80 x 30 | Klemmschelle | Welle 30 mm | 18–25 |
| ZD55 | Wellenanoden (Donut) | 1,2 | ID 35 / AD 95 x 35 | Klemmschelle | Welle 35 mm | 22–30 |
| ZD58 | Wellenanoden (Donut) | 1,8 | ID 40 / AD 110 x 40 | Klemmschelle | Welle 40 mm | 28–38 |
| ZD60 | Wellenanoden (Donut) | 2,5 | ID 50 / AD 130 x 45 | Klemmschelle | Welle 50 mm | 35–48 |
| ZD77 | Wellenanoden (Donut) | 3,8 | ID 60 / AD 155 x 55 | Klemmschelle | Welle 60 mm | 48–65 |
| CM1H | Rumpfanode (Halb-Ei) | 0,25 | 100 x 50 x 30 | 2x M8 Bolzen | Kleinboote | 8–12 |
| CM2H | Rumpfanode (Halb-Ei) | 0,5 | 130 x 65 x 35 | 2x M8 Bolzen | Standard | 12–18 |
| CM3H | Rumpfanode (Halb-Ei) | 1,0 | 170 x 80 x 45 | 2x M8 Bolzen | 10–14 m | 18–28 |
| CM5H | Rumpfanode (Halb-Ei) | 2,0 | 220 x 105 x 55 | 2x M10 Bolzen | 14–18 m | 28–42 |
| CM10H | Rumpfanode (Halb-Ei) | 4,5 | 300 x 140 x 70 | 2x M10 Bolzen | 18–25 m | 48–75 |
| CMEZ1 | Saildrive-Anode | 0,3 | Yanmar-spezifisch | Clip-On | Yanmar SD | 22–32 |
| CMEZ2 | Saildrive-Anode | 0,4 | Volvo-spezifisch | Clip-On | Volvo SD | 25–35 |

#### Aluminiumanoden (See-/Brackwasser)

| Modell | Typ | Gewicht (kg) | Kapazitaet (Ah) | Befestigung | Preis (EUR, ca.) |
|---|---|---|---|---|---|
| AD50 | Wellenanoden | 0,3 | 800 | Klemmschelle | 18–25 |
| AD55 | Wellenanoden | 0,9 | 2.400 | Klemmschelle | 28–38 |
| AD60 | Wellenanoden | 1,8 | 4.800 | Klemmschelle | 38–52 |
| ALLHULL1 | Rumpfanode | 0,5 | 1.350 | 2x M8 | 15–22 |
| ALLHULL3 | Rumpfanode | 1,5 | 4.050 | 2x M10 | 32–48 |
| ALLHULL5 | Rumpfanode | 3,0 | 8.100 | 2x M10 | 55–78 |

#### Magnesiumanoden (Suesswasser)

| Modell | Typ | Gewicht (kg) | Kapazitaet (Ah) | Befestigung | Preis (EUR, ca.) |
|---|---|---|---|---|---|
| MGD50 | Wellenanoden | 0,3 | 330 | Klemmschelle | 22–30 |
| MGD55 | Wellenanoden | 0,8 | 880 | Klemmschelle | 32–42 |
| MGHULL1 | Rumpfanode | 0,5 | 550 | 2x M8 | 18–26 |
| MGHULL3 | Rumpfanode | 1,5 | 1.650 | 2x M10 | 38–52 |

### 4.2 Martyr Anodes (USA)

Martyr ist ein US-amerikanischer Premiumhersteller mit OEM-Belieferung fuer Yamaha, Mercury, Volvo Penta.

**Spezialitaet:** Motorspezifische Anoden-Kits (Plug & Play).

| Modell/Kit | Motor/Antrieb | Material | Inhalt | Preis (EUR, ca.) |
|---|---|---|---|---|
| CMY-?"KIT" | Yamaha 150–300 HP | Zink | Trim-Tab-Anode + Zylinderanoden | 45–65 |
| CM-50180ZKITA | Mercury Alpha Gen I | Zink | Komplettes Antriebsset (5 Anoden) | 55–80 |
| CM-50180ZKITB | Mercury Bravo I/II/III | Zink | Komplettes Antriebsset (6 Anoden) | 65–95 |
| CM-VPDKITAZ | Volvo Penta DPH/DPR | Zink | Komplettes Antriebsset (4 Anoden) | 55–75 |
| CM-VPDKITAA | Volvo Penta DPH/DPR | Aluminium | Komplettes Antriebsset (4 Anoden) | 65–85 |
| CM-YKITAZ | Yanmar Saildrive SD20/SD50 | Zink | Saildrive-Anodenkit | 30–45 |
| CM-YKITAA | Yanmar Saildrive SD20/SD50 | Aluminium | Saildrive-Anodenkit | 38–52 |

**Martyr Rumpfanoden:**

| Modell | Material | Gewicht (kg) | Abmessungen (mm) | Preis (EUR, ca.) |
|---|---|---|---|---|
| CM-1H | Zink | 0,25 | 100 x 50 x 25 | 10–15 |
| CM-2H | Zink | 0,5 | 130 x 65 x 35 | 15–22 |
| CM-5H | Zink | 2,0 | 220 x 105 x 55 | 30–45 |
| CM-10H | Zink | 4,5 | 300 x 140 x 70 | 50–78 |
| CM-1HA | Aluminium | 0,2 | 100 x 50 x 25 | 14–20 |
| CM-2HA | Aluminium | 0,4 | 130 x 65 x 35 | 20–28 |
| CM-5HA | Aluminium | 1,5 | 220 x 105 x 55 | 38–55 |

### 4.3 Newmar (USA)

Newmar ist Spezialist fuer marine Elektroniksysteme, insbesondere galvanische Isolatoren und Netztrennung.

**Galvanische Isolatoren:**

| Modell | Nennstrom (A) | Nennspannung (V) | Fail-Safe | Monitoring | UL 1500 | Preis (EUR, ca.) |
|---|---|---|---|---|---|---|
| GI-30 | 30 | 120/240 V AC | Ja (Bypass) | LED + Alarm | Ja | 180–250 |
| GI-50 | 50 | 120/240 V AC | Ja (Bypass) | LED + Alarm | Ja | 250–350 |
| GI-100 | 100 | 120/240 V AC | Ja (Bypass) | LED + Alarm | Ja | 350–500 |
| GI-30II | 30 | 120/240 V AC | Ja (Bypass) | Digitaldisplay | Ja | 280–380 |
| GI-50II | 50 | 120/240 V AC | Ja (Bypass) | Digitaldisplay | Ja | 380–500 |

**Technische Details GI-Serie:**
- Doppelte Dioden-Paare (redundant)
- Fail-Safe: Bei Diodenausfall schliesst interner Bypass → PE durchverbunden
- Gehaeuse: Eloxiertes Aluminium, IP67
- Anschluss: Ring-Kabelschuhe, M8
- Temperaturbereich: −25 bis +75 C
- Eigenverbrauch: 0 W (passiv)

### 4.4 Dairyland Electrical Industries (USA)

Dairyland ist Spezialist fuer Streustrom-Schutz und Erdungstechnik, urspruenglich aus dem Pipeline-Bereich, zunehmend im Marinemarkt.

**Polarization Cell Replacement (PCR):**

| Modell | Nennstrom (A) | Blockierspannung DC (V) | Durchlassspannung AC (V) | Preis (EUR, ca.) |
|---|---|---|---|---|
| PCR-S1 | 30 | 0–1,5 | > 1,5 | 350–500 |
| PCR-S3 | 100 | 0–1,5 | > 1,5 | 500–750 |
| PCR-S5 | 200 | 0–1,5 | > 1,5 | 750–1.100 |

**Vorteil gegenueber einfachem galvanischem Isolator:**
- Hoeherer Blockierbereich (bis 1,5 V statt 1,2 V)
- Symmetrisches Verhalten (AC und DC)
- Hoehere Ueberlastfestigkeit
- Kombination Streustrom-Block und AC-Fehlerstrom-Durchlass

### 4.5 Dynaplate (USA)

Dynaplate stellt gesinterte Bronzeplatten her, die als kombinierte Blitzerdung, RF-Erdung und Bonding-Erdung dienen.

**Produkte:**

| Modell | Abmessungen (mm) | Effektive Flaeche (m²) | Gewicht (kg) | Anwendung | Preis (EUR, ca.) |
|---|---|---|---|---|---|
| DynaStar 100 | 305 x 89 x 12 | 0,14 | 2,3 | Blitzerdung (Standard) | 280–380 |
| DynaStar 200 | 305 x 178 x 12 | 0,28 | 4,5 | Blitz + RF-Erdung | 420–550 |
| DynaStar 300 | 457 x 178 x 12 | 0,42 | 6,8 | Blitz + RF + Bonding | 550–720 |
| DynaCopper 100 | 305 x 89 x 6 | 0,10 | 1,8 | Kupfer-Alternative | 320–420 |

**Technische Besonderheit:**
- Gesinterte Bronze: Poroese Struktur mit 10–30x groesserer effektiver Oberflaeche als massive Platte
- Idealer Blitzschutz-Erdungspunkt (niedrige Impedanz bei Hochstrom-Impulsen)
- Gutes RF-Gegengewicht fuer SSB-Funkanlagen
- Einbau: Unterhalb der Wasserlinie, beilaminiert (GFK) oder verschraubt

### 4.6 ProMariner (USA)

ProMariner bietet marine Trenntrafos (Isolation Transformer) fuer den Yachtmarkt.

**ProSafe-Serie (Trenntrafos):**

| Modell | Leistung (kVA) | Eingang (V/Hz) | Ausgang (V/Hz) | Gewicht (kg) | Preis (EUR, ca.) |
|---|---|---|---|---|---|
| ProSafe 30 | 3,6 | 120/60 oder 230/50 | 120/60 oder 230/50 | 14 | 1.800–2.500 |
| ProSafe 50 | 6,0 | 120/60 oder 230/50 | 120/60 oder 230/50 | 22 | 2.800–3.800 |
| ProSafe FS30 | 3,6 | 120/60 | 120/60 | 12 | 1.600–2.200 |
| ProSafe FS60 | 7,2 | 120/60 | 120/60 | 28 | 3.200–4.500 |

**Technische Daten:**
- Toroidkern (geringere Verluste, weniger Vibration als EI-Kern)
- Effizienz: > 95%
- Temperaturueberwachung (Abschaltung bei > 130 C)
- Metallgehaeuse mit Lueftungsgitter
- Montage: Schraubflansch (4x M10)
- Anschluss: Klemmenleiste (Eingang/Ausgang/PE)

**ProMariner Galvanic Isolator:**

| Modell | Nennstrom (A) | Gehaeuse | UL 1500 | Preis (EUR, ca.) |
|---|---|---|---|---|
| ProSafe GI30 | 30 | Eloxiert Alu | Ja | 160–220 |
| ProSafe GI50 | 50 | Eloxiert Alu | Ja | 220–310 |

---

## 5. Hersteller-Datenbank

### 5.1 MG Duff International Ltd

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1956 |
| **Hauptsitz** | Chichester, West Sussex, UK |
| **Produktionsstätten** | UK, China (Zinkanoden), Indien (Aluminiumanoden) |
| **Kernkompetenz** | Opferanoden (Zink, Aluminium, Magnesium), Wellenerdung, Referenzelektroden |
| **Marine-Anteil** | > 90% |
| **Zertifizierungen** | ISO 9001:2015, DNV Type Approved, Lloyd's Register |
| **OEM-Kunden** | Beneteau, Jeanneau, Bavaria, Hanse, Oyster |
| **Distribution EU** | SVB (DE), Compass24 (DE), Toplicht (DE), Accastillage Diffusion (FR), Force4 (UK) |
| **Website** | www.mgduff.com |
| **AYDI-Bewertung** | Referenz-Hersteller, breitestes Sortiment, zuverlaessige Qualitaet |

### 5.2 Martyr Anodes (Canada Metal Pacific Ltd)

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1974 |
| **Hauptsitz** | Surrey, British Columbia, Kanada |
| **Kernkompetenz** | Motorspezifische Anoden-Kits, OEM-Zulieferung |
| **Marine-Anteil** | > 95% |
| **Zertifizierungen** | ISO 9001:2015, MIL-A-18001K, MIL-DTL-24779C |
| **OEM-Kunden** | Mercury Marine, Yamaha Marine, Volvo Penta, Suzuki Marine |
| **Distribution EU** | Svea Husbilar (SE), Bukh (DK), diverse Motorenhaendler |
| **Website** | www.martyranodes.com |
| **AYDI-Bewertung** | Beste Wahl fuer OEM-spezifische Anodenkits, hervorragende Passgenauigkeit |

### 5.3 Newmar Corporation

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1957 |
| **Hauptsitz** | Redmond, Oregon, USA |
| **Kernkompetenz** | Galvanische Isolatoren, marine Stromversorgung, DC-Wandler |
| **Marine-Anteil** | ca. 60% |
| **Zertifizierungen** | UL 1500, ABYC-compliant, ISO 9001 |
| **OEM-Kunden** | Diverse US-Werften |
| **Distribution EU** | Mastervolt/Victron-Haendler, Fachhaendler |
| **Website** | www.newmarpower.com |
| **AYDI-Bewertung** | Marktfuehrer galvanische Isolatoren, hervorragende Fail-Safe-Technologie |

### 5.4 Dairyland Electrical Industries

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1986 |
| **Hauptsitz** | Stoughton, Wisconsin, USA |
| **Kernkompetenz** | Streustrom-Schutz, Kathodenschutz-Zubehoer, Polarization Cells |
| **Marine-Anteil** | ca. 15% (Hauptmarkt: Pipeline, Infrastruktur) |
| **Zertifizierungen** | UL Listed, CSA, NACE |
| **Distribution EU** | Spezialdistribution ueber Korrosionsschutz-Fachfirmen |
| **Website** | www.dairyland.com |
| **AYDI-Bewertung** | Spezialist fuer komplexe Streustrom-Situationen, selten bei Standard-Yachten |

### 5.5 Dynaplate Corporation

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1972 |
| **Hauptsitz** | Chula Vista, Kalifornien, USA |
| **Kernkompetenz** | Gesinterte Bronze-Erdungsplatten |
| **Marine-Anteil** | 100% |
| **Zertifizierungen** | ABYC-recommended |
| **Unique Selling Point** | 10–30x groessere effektive Oberflaeche durch Sinterstruktur |
| **Distribution EU** | Ueber Yachtausruester (Compass24, SVB), limitiert |
| **Website** | www.dynaplate.com |
| **AYDI-Bewertung** | Goldstandard fuer Blitz-/RF-Erdungsplatten, teuer aber exzellent |

### 5.6 ProMariner (Professional Mariner)

| Feld | Information |
|---|---|
| **Gruendungsjahr** | 1985 |
| **Hauptsitz** | Hampshire, Illinois, USA |
| **Kernkompetenz** | Marine Trenntrafos, Ladegeraete, Galvanische Isolatoren |
| **Marine-Anteil** | 100% |
| **Zertifizierungen** | UL Listed, ABYC-compliant |
| **Produktfamilien** | ProSafe (Trenntrafos, Isolatoren), ProNautic (Ladegeraete), ProTournament (Fischerei) |
| **Distribution EU** | Limitiert, ueber US-Importeure |
| **Website** | www.promariner.com |
| **AYDI-Bewertung** | Solide Trenntrafos fuer US-Markt, EU-Kompatibilitaet pruefen (120V-Fokus) |

### 5.7 CMP (Cathodic Marine Protection) / MCPS (Marine Cathodic Protection Systems)

| Feld | Information |
|---|---|
| **Hauptsitz** | Diverse europaeische Anbieter |
| **Kernkompetenz** | ICCP-Systeme fuer Yachten und Superyachten |
| **Typische ICCP-Kits** | Komplettsets fuer 10–60 m LOA |
| **Preisbereich** | 3.500–25.000 EUR |
| **Distribution** | Direkt oder ueber Werft-Netzwerke |
| **AYDI-Bewertung** | Professionelle ICCP-Loesungen, typisch fuer Superyachten |

### 5.8 Wesmar / ABB Marine (ICCP-Systeme)

| Feld | Information |
|---|---|
| **Kernkompetenz** | ICCP-Systeme fuer kommerzielle Schifffahrt und Megayachten |
| **Marine-Anteil** | 100% |
| **Leistungsbereich** | 1–500 A Schutzstrom |
| **Referenzprojekte** | Superyachten, Marineschiffe, Faehren |
| **AYDI-Bewertung** | Industrial-Grade, fuer Yachten > 30 m relevant |

---

## 6. Fehlerbild-Atlas

### Fehlerbild F-22.10-01: Beschleunigter Anodenverbrauch

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Uebermässig schneller Anodenverbrauch (< 6 Monate bis > 50% Verlust) |
| **Betroffene Komponente** | Alle Opferanoden (Zink, Aluminium, Magnesium) |
| **Visuelles Erscheinungsbild** | Anoden stark reduziert, rauhe Oberflaeche, tiefe Furchen, teilweise nur noch Kern/Einsatz sichtbar |
| **Ursache 1** | Streustrom-Korrosion (haeufigste Ursache): Externer Strom treibt Anoden-Aufloesung |
| **Ursache 2** | Unterdimensionierung: Anoden zu klein fuer zu schuetzende Flaeche |
| **Ursache 3** | Unguenstiges Flaechenverhaeltnis: Grosse Kathode (Propeller) vs. kleine Anode |
| **Ursache 4** | Bonding-Fehler: Metallteile ohne Bonding ziehen Schutzstrom von Anoden |
| **Diagnose** | Potenzial-Messung am Rumpf (Ag/AgCl), Leckstrom-Messung am Landkabel |
| **Sofortmassnahme** | Neue Anoden installieren, Streustrom-Quelle suchen und eliminieren |
| **Langfristmassnahme** | Bonding-System pruefen, galvanischen Isolator oder Trenntrafo installieren |
| **Confidence** | visual_high (Verbrauch deutlich sichtbar) |
| **AYDI-Modul** | materials, structural, compliance |

### Fehlerbild F-22.10-02: Propeller-Entzinkung (Dezincification)

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Selektive Zinkausloesung aus Messing-/Manganbronze-Propeller |
| **Betroffene Komponente** | Messing- oder Manganbronze-Propeller |
| **Visuelles Erscheinungsbild** | Kupferrote bis rosafarbene Flecken auf normalerweise goldfarbener Oberflaeche, poroese Konsistenz, Rissbildung |
| **Ursache** | Anodischer Schutz fehlt oder unzureichend, hoher Zinkgehalt in Legierung (> 15% Zn) |
| **Diagnose** | Visuelle Inspektion, Haertetest (entzinktes Material ist weich), Ultraschall-Wanddickenmessung |
| **Sofortmassnahme** | Propeller ersetzen (entzinktes Material ist strukturell unsicher) |
| **Langfristmassnahme** | Propeller aus Nickelaluminumbronze (NAB) oder Edelstahl waehlen, Anodenschutz sicherstellen |
| **Confidence** | visual_high (charakteristisches Erscheinungsbild) |

### Fehlerbild F-22.10-03: Edelstahl-Lochfrass (Pitting)

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Lokalisierte Durchkorrosion an Edelstahl 316L |
| **Betroffene Komponente** | Propellerwelle, Ruderschaft, Kielbolzen, Edelstahl-Seeventile |
| **Visuelles Erscheinungsbild** | Kleine (< 1 mm) bis grosse (5+ mm) Vertiefungen, rostfarbene Krusten, unter Biofilm oft verborgen |
| **Ursache** | Sauerstoffmangel unter Biofilm/Ablagerung (Spaltkorrosion-Mechanismus), warmes Wasser > 25 C, Chlorid-Konzentration |
| **Diagnose** | Biofilm entfernen, Oberflaeche reinigen, Lupeninspektion, Ultraschall-Wanddickenmessung |
| **Sofortmassnahme** | Oberflaechenreinigung, Passivierung (Salpetersaeure-Bad), kathodischen Schutz pruefen |
| **Langfristmassnahme** | 2205 Duplex-Edelstahl erwaegen, ICCP-System fuer praezise Potenzialsteuerung |
| **Confidence** | visual_medium (oft unter Bewuchs/Biofilm verborgen) |

### Fehlerbild F-22.10-04: Aluminium-Rumpf-Korrosion unter Antifouling

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Galvanische Korrosion eines Aluminiumrumpfes durch kupferhaltiges Antifouling oder Kupfer-Ionen |
| **Betroffene Komponente** | Aluminiumrumpf unterhalb Wasserlinie |
| **Visuelles Erscheinungsbild** | Weisse, puderige Aluminiumoxid-Ablagerungen, Blasenbildung unter Antifouling, Lochfrass-Muster |
| **Ursache** | Kupferhaltiges Antifouling auf Aluminiumrumpf (VERBOTEN!), Kupfer-Ionen im Hafenwasser von Nachbar-Antifouling, fehlende Barrier-Coat-Schicht |
| **Diagnose** | Antifouling-Typ identifizieren, Barrier-Coat pruefen, Potenzial-Messung |
| **Sofortmassnahme** | Kupferhaltiges Antifouling sofort entfernen, Barrier-Coat (Epoxid, min. 3 Schichten) auftragen, kupferfreies Antifouling verwenden |
| **Langfristmassnahme** | ICCP-System mit Potenzialregelung −800 bis −1.050 mV, NIEMALS > −1.100 mV |
| **Confidence** | visual_high (Muster sehr charakteristisch) |

### Fehlerbild F-22.10-05: Marina-Streustrom-Schaden

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Massive Korrosion durch externe Streustroeme ueber Landstrom-Erdung |
| **Betroffene Komponente** | Alle Unterwasser-Metallteile (Propeller, Welle, Seeventile, Trimmer) |
| **Visuelles Erscheinungsbild** | Alle Metalle gleichzeitig angegriffen, Anoden innerhalb weniger Wochen verbraucht, weisse/gruene Korrosionsprodukte auf Bronze, Blasen auf Antifouling |
| **Ursache** | Defekte Erdung in der Marina oder auf Nachbarboot, fehlender galvanischer Isolator |
| **Diagnose** | DC-Milliamperemeter am Landkabel (Clamp-On), Potenzial-Messung mit und ohne Landstrom |
| **Test** | Landstrom trennen → Potenzial messen → Landstrom anschliessen → Potenzial erneut messen. Aenderung > 50 mV = Streustrom |
| **Sofortmassnahme** | Landstrom trennen, galvanischen Isolator installieren |
| **Langfristmassnahme** | Trenntrafo installieren, Marina-Betreiber informieren, ggf. Liegeplatz wechseln |
| **Confidence** | measured (Potenzial-Messung ist eindeutig) |

### Fehlerbild F-22.10-06: Blitzschlag-Mast-Durchschmelzung

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Thermische Zerstoerung des Mastes durch Blitzeinschlag |
| **Betroffene Komponente** | Aluminiummast, Masttop-Einheit, Wanten-Terminals |
| **Visuelles Erscheinungsbild** | Schmelzspuren am Masttop, durchgeschmolzene VHF-Antenne, Verfaerbung am Mastfuss, Brandspuren an Wanten-Terminals |
| **Ursache** | Blitzeinschlag bei fehlendem oder unzureichendem Blitzableitersystem |
| **Diagnose** | Visuelle Inspektion, Durchgangspruefung aller Kabel im Mast, Elektronik-Funktionstest |
| **Sofortmassnahme** | Alle Kabel im Mast pruefen, Maststruktur auf Risse pruefen (Magnet-Partikel oder Farbeindring-Pruefung) |
| **Langfristmassnahme** | Blitzschutz nachrüsten (Air Terminal + Ableiterkabel + Erdungsplatte + Bonding) |
| **Confidence** | visual_high (Blitzschlag-Spuren eindeutig) |

### Fehlerbild F-22.10-07: Blitzschlag-Elektronik-Totalschaden

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Zerstoerung aller oder der meisten Elektronikgeraete durch induktive Blitz-Kopplung |
| **Betroffene Komponente** | Plotter/MFD, Radar, AIS-Transponder, VHF, GPS, Autopilot, NMEA-2000-Netzwerk, Ladegeraete, Wechselrichter |
| **Visuelles Erscheinungsbild** | Geraete reagieren nicht, geschwaezte Platinen, geschmolzene Stecker, Geruch nach verbrannter Elektronik |
| **Ursache** | Elektromagnetischer Impuls (EMP) des Blitzes koppelt induktiv in ungeschirmte Kabel ein |
| **Diagnose** | Systematischer Funktionstest aller Geraete, Isolationsmessung Kabel, NMEA-Netzwerk-Diagnose |
| **Sofortmassnahme** | Batterien abklemmen, ALLE Geraete pruefen lassen (auch scheinbar funktionierende — Spaetschaeden), Versicherung melden |
| **Langfristmassnahme** | Surge Protector an allen Antennenkabeln und Landstrom, geschirmte Kabel, Ferritkerne, Blitzschutz-Bonding |
| **Schaetzwert (typisch)** | 15.000–80.000 EUR Elektronik-Ersatz bei 12–18 m Yacht |
| **Confidence** | documented (Versicherungsgutachten, Elektronik-Diagnose) |

### Fehlerbild F-22.10-08: Bonding-Unterbrechung

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Unterbrochene Bonding-Verbindung isoliert einzelne Metallteile vom Korrosionsschutz |
| **Betroffene Komponente** | Einzelnes Seeventil, Borddurchlass, Ruder, oder anderes Metallteil |
| **Visuelles Erscheinungsbild** | Lokale Korrosion an einem einzelnen Metallteil bei intaktem Zustand der uebrigen, gruene Patina an Bronze, Rost an Stahl |
| **Ursache** | Gebrochene/korrodierte Bonding-Kabelschelle, abgerissenes Bonding-Kabel, bei Anstrich ueberstrichene Kontaktflaeche |
| **Diagnose** | Widerstandsmessung: Betroffenes Teil → Bonding-Bus > 1 Ohm = unterbrochen |
| **Sofortmassnahme** | Kontaktflaeche blank schleifen, neuen Kabelschuh anbringen, Verbindung wiederherstellen |
| **Langfristmassnahme** | Jaehrliche Bonding-Durchgangspruefung (alle Verbindungspunkte messen) |
| **Confidence** | measured (Widerstandsmessung eindeutig) |

### Fehlerbild F-22.10-09: ICCP-Ueberprotektion

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | ICCP-System regelt Potenzial zu negativ (< −1.100 mV vs. Ag/AgCl) |
| **Betroffene Komponente** | Antifouling-Beschichtung, Aluminium-Bauteile |
| **Visuelles Erscheinungsbild** | Antifouling-Abloesungen (Blasenbildung), alkalische Ablagerungen (weiss/gelb), Wasserstoffblasen an Metalloberflaechen, Versprödung von Aluminium |
| **Ursache** | Defekte Referenzelektrode (liest falsches Potenzial), falsche Sollwert-Einstellung, Kalibrierungsfehler |
| **Diagnose** | Externes Referenzpotenzial messen und mit ICCP-Anzeige vergleichen |
| **Sofortmassnahme** | ICCP ausschalten, Referenzelektrode pruefen/kalibrieren, Sollwert korrigieren |
| **Langfristmassnahme** | Redundante Referenzelektrode installieren, Potenzial-Logger anschliessen |
| **Confidence** | measured (Potenzial-Messung) |

### Fehlerbild F-22.10-10: Wellenerdungsbuerste verschlissen

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Kohle- oder Silberbuerste der Wellenerdung verschlissen oder oxidiert |
| **Betroffene Komponente** | Wellenerdung → Propellerwelle → Propeller |
| **Visuelles Erscheinungsbild** | Korrosion am Propeller trotz intakter Anoden, Anodenverbrauch ungleichmaessig |
| **Ursache** | Buerste verschlissen, oxidiert, oder nicht mehr in Kontakt mit der Welle |
| **Diagnose** | Widerstandsmessung Welle → Bonding-Bus. > 0,1 Ohm = Buerste defekt |
| **Sofortmassnahme** | Buerste reinigen oder ersetzen, Kontaktflaeche auf Welle polieren |
| **Langfristmassnahme** | Jaehrliche Pruefung, alle 2–3 Jahre Buerste ersetzen |
| **Confidence** | measured (Widerstandsmessung) |

### Fehlerbild F-22.10-11: Carbon-Rigg-Korrosion

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Galvanische Korrosion an Edelstahl-Beschlaegen in Kontakt mit Carbon/CFK |
| **Betroffene Komponente** | Mastkopf-Beschlaege, Want-Terminals, Bugspriet-Anschluesse an CFK-Mast/Bugspriet |
| **Visuelles Erscheinungsbild** | Braune Rostspuren an Edelstahl-Beschlaegen, weiße Ablagerungen an Carbon-Edelstahl-Uebergang |
| **Ursache** | Carbon/Graphit ist extrem kathodisch (+200 bis +300 mV vs. Ag/AgCl) → Edelstahl wird zur Anode |
| **Diagnose** | Visuelle Inspektion aller Carbon-Metall-Uebergaenge, Potenzial-Messung |
| **Sofortmassnahme** | Galvanische Isolation (GFK-Zwischenlage) zwischen Carbon und Metall |
| **Langfristmassnahme** | Titan-Beschlaege erwaegen (aehnliches Potenzial wie Carbon), vollstaendige Isolation aller Uebergaenge |
| **Confidence** | visual_medium (Rost an Edelstahl ist offensichtlich, aber Ursache kann mehrere sein) |

### Fehlerbild F-22.10-12: Rumpfdurchschlag nach Blitzeinschlag (GFK)

| Feld | Beschreibung |
|---|---|
| **Bezeichnung** | Blitz durchschlaegt GFK-Rumpf wegen fehlender Ableitung ins Wasser |
| **Betroffene Komponente** | GFK-Rumpfschale, Kielbereich |
| **Visuelles Erscheinungsbild** | Sternfoermige Rissbildung im GFK, Delaminierung, Brandspuren, ggf. Wassereinbruch |
| **Ursache** | Fehlende oder unzureichende Blitzerdung (kein Ableiterpfad zum Wasser vorhanden) |
| **Diagnose** | Visuelle Inspektion Rumpf innen und aussen, Klopftest (Delaminierung), Feuchtemessung |
| **Sofortmassnahme** | Rumpf auf Dichtigkeit pruefen, GFK-Reparatur (Epoxid + Glasgewebe), Versicherung melden |
| **Langfristmassnahme** | Blitzschutzsystem komplett nachrüsten (Erdungsplatte + Ableiterkabel + Air Terminal + Bonding) |
| **Confidence** | visual_high (Muster sehr charakteristisch) |

---

## 7. Troubleshooting-Entscheidungsbaeume

### 7.1 Entscheidungsbaum: „Korrosion an Unterwasser-Metallteilen"

```
START: Korrosion an Unterwasser-Metall festgestellt
│
├── Frage 1: Sind Opferanoden installiert?
│   ├── NEIN → Sofort Anoden installieren, Bonding pruefen.
│   │         Weiter zu Frage 3 (Anodentyp waehlen)
│   │
│   └── JA → Frage 2: Wie ist der Anodenzustand?
│       ├── > 50% erhalten → Anoden funktionieren.
│       │   Problem liegt woanders → Frage 4
│       │
│       ├── 20–50% erhalten → Normal nach 1 Jahr.
│       │   Unter 6 Monate? → Verdacht Streustrom → Frage 5
│       │
│       └── < 20% erhalten oder komplett aufgeloest →
│           Frage: Letzer Anodenwechsel < 12 Monate?
│           ├── JA → Streustrom fast sicher → Frage 5
│           └── NEIN → Anoden ueberfaellig → Wechseln + Frage 3
│
├── Frage 3: Welchen Anodentyp verwenden?
│   ├── Seewasser (Salzgehalt > 20 ppt) → Zink oder Aluminium
│   ├── Brackwasser (5–20 ppt) → Aluminium (Zink passiviert!)
│   ├── Suesswasser (< 5 ppt) → Magnesium
│   └── Aluminiumrumpf → Aluminium-Anoden + Potenzial messen (max. −1.100 mV)
│
├── Frage 4: Bonding-System intakt?
│   ├── Widerstandsmessung: Jedes Metallteil → Bonding-Bus
│   │   ├── Alle < 1 Ohm → Bonding OK → Frage 6
│   │   └── Eines oder mehrere > 1 Ohm → Bonding-Verbindung reparieren
│   │       └── Kontaktflaeche blank schleifen, neuer Kabelschuh, messen
│   │
│   └── Kein Bonding-System vorhanden → Installieren! (alle UW-Metalle verbinden)
│
├── Frage 5: Streustrom-Diagnose
│   ├── Test A: Landstrom trennen → Potenzial messen → Landstrom an → erneut messen
│   │   ├── Aenderung > 50 mV → Streustrom ueber Landstrom!
│   │   │   ├── Galvanischer Isolator vorhanden?
│   │   │   │   ├── JA → Funktion pruefen (Durchlasstest)
│   │   │   │   └── NEIN → Galvanischen Isolator installieren
│   │   │   └── Trenntrafo erwaegen (vollstaendige Trennung)
│   │   │
│   │   └── Aenderung < 50 mV → Kein Landstrom-Problem → Test B
│   │
│   ├── Test B: Alle Nachbarboote bitten, Landstrom zu trennen
│   │   ├── Potenzial aendert sich → Nachbarboot hat Erdschluss
│   │   │   → Nachbar informieren, Marina-Betreiber einschalten
│   │   └── Keine Aenderung → Test C
│   │
│   └── Test C: Isolationswiderstand eigene Anlage messen (500 V Megger)
│       ├── < 1 MOhm → Eigener Isolationsfehler → Fehlersuche im Bordnetz
│       └── > 1 MOhm → Eigene Anlage OK → Marina-Infrastruktur verdaechtig
│
└── Frage 6: Korrosionsart identifizieren
    ├── Gleichmaessig → Unzureichender kathodischer Schutz → Anoden aufstocken
    ├── Lochfrass → Edelstahl: Spaltkorrosion/Biofilm → Reinigen, Schutz verbessern
    ├── Rote/rosa Verfaerbung → Entzinkung → Material ersetzen (NAB oder DZR)
    ├── Unter Bewuchs → Sauerstoff-Differenzzelle → Regelmaessig reinigen
    └── An Carbon-Uebergaengen → Galvanische Isolation einbauen
```

### 7.2 Entscheidungsbaum: „ICCP-System funktioniert nicht"

```
START: ICCP-System zeigt Fehler oder Schutz ist unzureichend
│
├── Frage 1: Controller zeigt Fehlermeldung?
│   ├── „Ref-Electrode Error" → Referenzelektrode defekt oder Kabel gebrochen
│   │   ├── Kabelverbindungen pruefen (Korrosion an Steckern)
│   │   ├── Referenzelektrode wechseln
│   │   └── Kalibrierung mit externer Referenz pruefen
│   │
│   ├── „Anode Open" → Anodenkabel unterbrochen oder Anode beschaedigt
│   │   ├── Kabelverbindungen pruefen
│   │   ├── Anode visuell inspizieren (Taucher)
│   │   └── Durchgangspruefung Anode → Controller
│   │
│   ├── „Over-Voltage" → Beschichtung grossflaechig beschaedigt (hoher Strombedarf)
│   │   ├── Unterwasseranstrich pruefen
│   │   ├── Strombedarfsberechnung wiederholen
│   │   └── Ggf. zusaetzliche Anode installieren
│   │
│   └── Keine Fehlermeldung, aber Schutz unzureichend → Frage 2
│
├── Frage 2: Potenzial mit externer Referenz messen
│   ├── Potenzial im Schutzbereich (−800 bis −1.100 mV) → System funktioniert!
│   │   → Problem liegt woanders (lokale Korrosion, Bonding, Spalt)
│   │
│   ├── Potenzial positiver als −800 mV → Unterschutz
│   │   ├── Controller-Ausgangsstrom pruefen (zu niedrig?)
│   │   ├── Anodenzustand pruefen (MMO-Beschichtung intakt?)
│   │   ├── Versorgungsspannung pruefen (12/24 V ausreichend?)
│   │   └── Bonding pruefen (unterbrochene Verbindung?)
│   │
│   └── Potenzial negativer als −1.100 mV → Ueberprotektion!
│       ├── Controller-Sollwert pruefen (zu negativ?)
│       ├── Referenzelektrode kalibrieren (zeigt falsches Potenzial?)
│       └── System sofort auf niedrigeren Strom reduzieren
│
└── Frage 3: Wartungsprotokoll
    ├── Letzte Kalibrierung > 12 Monate? → Kalibrieren!
    ├── Referenzelektrode > 5 Jahre? → Ersetzen!
    ├── MMO-Anode > 15 Jahre? → Inspizieren, ggf. ersetzen
    └── Firmware/Software aktuell? → Update pruefen
```

### 7.3 Entscheidungsbaum: „Blitzschutz pruefen"

```
START: Blitzschutz-Bewertung
│
├── Frage 1: Bootstyp?
│   ├── Segelyacht mit Alumast → Mast ist bereits teil des Ableiterpfads
│   │   → Braucht: Air Terminal + Ableitung + Erdungsplatte + Bonding
│   │
│   ├── Motoryacht (kein Mast) → Hoechster Punkt bestimmen (Flybridge, Radararch, Antenne)
│   │   → Air Terminal am hoechsten Punkt + Ableiterkabel + Erdungsplatte
│   │
│   ├── Segelyacht mit Carbonmast → ACHTUNG: Carbon leitet, aber schlecht fuer Blitzstrom
│   │   → Separater Kupfer-Ableiter IM Mast + Air Terminal + Erdungsplatte
│   │
│   └── Segelyacht mit Holzmast → Mast leitet nicht
│       → Kupferkabel aussen am Mast + Air Terminal + Erdungsplatte
│
├── Frage 2: Schutzzone berechnen
│   ├── Masthoehe ueber Wasser bestimmen (m)
│   ├── Schutzradius = Masthoehe x 0,577
│   ├── Gesamtlaenge des Bootes im Schutzradius? → Wenn ja: OK
│   └── Bug oder Heck ausserhalb? → Zusaetzliches Air Terminal erwaegen
│
├── Frage 3: Ableiterpfad vorhanden?
│   ├── Von Mastspitze (Air Terminal) bis Wasserlinie:
│   │   ├── Querschnitt min. 4 AWG (21 mm²) Kupfer? → OK
│   │   ├── Verbindungen gecrimpt/geschraubt (kein Lot allein)? → OK
│   │   ├── Keine scharfen Biegungen (Radius > 200 mm)? → OK
│   │   └── Eines oder mehrere NEIN → Nachruesten / Korrigieren
│   │
│   └── Erdungsplatte vorhanden?
│       ├── Min. 0,1 m² (929 cm²) Kupfer/Bronze in Wasserkontakt? → OK
│       ├── Weniger → Aufrüsten (Dynaplate, zusaetzliche Platte)
│       └── Keine Erdungsplatte → DRINGEND installieren
│
├── Frage 4: Bonding fuer Blitzschutz?
│   ├── Alle Metallteile innerhalb 1,8 m vom Ableiterpfad verbunden?
│   │   ├── JA (min. 6 AWG) → OK
│   │   └── NEIN → Nachruesten (Wanten, Reling, Winschen verbinden)
│   │
│   └── Wanten-Erdung?
│       ├── Wantspanner → Bonding-Bus → Erdungsplatte? → OK
│       └── NEIN → Wanten muessen geerdet werden (Seitenueberschlag-Risiko)
│
└── Frage 5: Elektronik-Schutz?
    ├── Surge Protector an VHF/AIS/Radar/GPS-Antennenkabel? → OK
    ├── Surge Protector an Landstrom-Einspeisung? → OK
    ├── Geschirmte Kabel (Mast → Maschinenraum)? → OK
    └── Fehlend → Nachrüsten (Prioritaet: Antennen > Landstrom > Datenkabel)
```

### 7.4 Entscheidungsbaum: „Galvanischer Isolator oder Trenntrafo?"

```
START: Landstrom-Schutz waehlen
│
├── Frage 1: Budget?
│   ├── < 500 EUR → Galvanischer Isolator (einzige Option)
│   │   → Dimensionierung: Nennstrom >= Landanschluss-Sicherung
│   │   → Installation: In PE-Leiter, nach Hauptschalter
│   │
│   ├── 500–3.000 EUR → Galvanischer Isolator (bevorzugt) oder kleiner Trenntrafo
│   │   → Frage 2
│   │
│   └── > 3.000 EUR → Trenntrafo empfohlen → Frage 3
│
├── Frage 2: Art des Streustrom-Problems?
│   ├── Nur galvanische Korrosion (Nachbarboot-Erdung) →
│   │   Galvanischer Isolator ausreichend
│   │
│   ├── AC-Streustrom (defekte Marina-Elektrik) →
│   │   Trenntrafo erforderlich (Isolator blockiert nur DC)
│   │
│   ├── Starker DC-Streustrom (> 100 mA am PE) →
│   │   Trenntrafo empfohlen (Isolator-Dioden koennten ueberlastet werden)
│   │
│   └── Unbekannt → Messung durchfuehren (Test A aus Baum 7.1) → dann entscheiden
│
└── Frage 3: Trenntrafo-Dimensionierung
    ├── Leistungsbedarf ermitteln:
    │   Summe aller gleichzeitigen Landstrom-Verbraucher (kVA)
    │   + 20% Reserve
    │
    ├── < 4 kVA → 3,5 kVA Trafo (8–10 m Yacht typisch)
    ├── 4–8 kVA → 7,5 kVA Trafo (10–14 m Yacht typisch)
    ├── 8–14 kVA → 12 kVA Trafo (14–18 m Yacht typisch)
    └── > 14 kVA → 16–25 kVA Trafo (> 18 m Yacht)
```

### 7.5 Entscheidungsbaum: „Anodenwahl und Dimensionierung"

```
START: Opferanoden dimensionieren
│
├── Frage 1: Wassertyp?
│   ├── Seewasser (> 20 ppt) → Zink ODER Aluminium
│   │   ├── Standard, kostenoptimal → Zink
│   │   ├── Laenger haltbar, leichter → Aluminium
│   │   └── Aluminiumrumpf → NUR Aluminium (Zink-Potenzial passt nicht optimal)
│   │
│   ├── Brackwasser (5–20 ppt) → NUR Aluminium (Zink passiviert!)
│   │
│   └── Suesswasser (< 5 ppt) → NUR Magnesium
│
├── Frage 2: Zu schuetzende Metall-Flaeche berechnen
│   ├── Propeller: π x D x Blattbreite x Blattanzahl (ca. 40–70% der Kreisflaeche)
│   ├── Welle: π x d x Laenge (exponierter Bereich)
│   ├── Ruder: 2 x Blattflaeche (beide Seiten)
│   ├── Seeventile: ca. 0,01–0,02 m² pro Stueck
│   ├── Trimmer: ca. 0,05–0,2 m² pro Stueck
│   ├── Saildrive: ca. 0,1–0,3 m² (Gehaeuse + Propeller)
│   └── Kiel (Metall): Oberflaeche berechnen oder schaetzen
│
├── Frage 3: Schutzdauer festlegen
│   ├── Standard: 12 Monate (jaehrliches Haul-Out)
│   ├── Langstrecke: 18–24 Monate (Blauwasser-Segler)
│   └── Minimum: 6 Monate (Halbzeit-Kontrolle)
│
├── Frage 4: Anodengewicht berechnen
│   │
│   │  Zink:
│   │  Gewicht (kg) = Flaeche (m²) x Stromdichte (mA/m²) x Dauer (h) / (Kapazitaet (Ah/kg) x 1.000 x Auslastung)
│   │  Typisch: Flaeche x 50 mA/m² x 8.760 h / (780 Ah/kg x 1.000 x 0,85)
│   │
│   │  Aluminium:
│   │  Gleiche Formel, Kapazitaet = 2.500 Ah/kg → ca. 1/3 des Zink-Gewichts
│   │
│   │  Magnesium:
│   │  Gleiche Formel, Kapazitaet = 1.150 Ah/kg → ca. 2/3 des Zink-Gewichts
│   │
│   └── Faustregeln (GFK-Yacht, Seewasser):
│       ├── 8 m: 2–3 kg Zink (Wellenanoden + 1–2 Rumpfanoden)
│       ├── 10 m: 3–5 kg Zink
│       ├── 12 m: 5–8 kg Zink
│       ├── 15 m: 8–12 kg Zink
│       ├── 18 m: 12–18 kg Zink
│       └── > 20 m: Individuelle Berechnung oder ICCP erwaegen
│
└── Frage 5: Platzierung
    ├── Wellenanoden: Direkt hinter Stevenrohr (Propeller-nahe)
    ├── Rumpfanoden: Min. 2 Stueck, symmetrisch, nahe Seeventilen
    ├── Saildrive-Anoden: Am Saildrive-Gehaeuse (OEM-Befestigung)
    ├── Ruderanoden: Am Ruderblatt oder Ruderschaft
    └── Trimmer-Anoden: An oder nahe den Trimm-Klappen
```

---

## 8. FAQ — Haeufig gestellte Fragen

### FAQ-01: Warum korrodiert mein Propeller trotz Anoden?

**Antwort:** Die wahrscheinlichsten Ursachen sind:
1. **Bonding-Unterbrechung:** Die Wellenerdungsbuerste ist verschlissen oder hat keinen Kontakt. Widerstandsmessung Welle → Bonding-Bus durchfuehren (muss < 0,1 Ohm sein).
2. **Falscher Anodentyp:** In Brackwasser (Ostsee) passivieren Zinkanoden. Wechsel zu Aluminiumanoden.
3. **Streustrom:** Externer Strom uebersteigt Anodenkapazitaet. Landstrom-Streustrom-Test durchfuehren.
4. **Propeller nicht im Bonding:** Bei neuem Propeller Bonding-Anschluss vergessen.

### FAQ-02: Kann man Zink- und Aluminiumanoden mischen?

**Antwort:** Technisch moeglich, aber nicht empfohlen. Aluminiumanoden haben ein leicht negativeres Potenzial (−1.050 bis −1.100 mV) als Zinkanoden (−1.030 bis −1.050 mV). Die Aluminiumanode wuerde sich zuerst verbrauchen und die Zinkanode teilweise schuetzen, anstatt die Yacht-Struktur zu schuetzen. Empfehlung: Einheitlich auf einen Typ umstellen.

### FAQ-03: Wie oft muessen Anoden gewechselt werden?

**Antwort:** Standard-Regel: Wechsel, wenn > 50% des Anodenmaterials verbraucht ist. Bei jaehrlichem Haul-Out: Anoden inspizieren und ersetzen, wenn < 50% verblieben. In aggressiven Umgebungen (Tropen, Marina mit Streustrom) ggf. halbjährlich pruefen (Taucher).

### FAQ-04: Mein Boot liegt im Suesswasser — brauche ich Anoden?

**Antwort:** Ja! Galvanische Korrosion findet auch in Suesswasser statt, nur langsamer. Suesswasser hat aber eine geringe Leitfaehigkeit, daher funktionieren Zink- und Aluminiumanoden nicht (Triebspannung reicht nicht). Magnesiumanoden sind zwingend erforderlich. Auch fuer Heisswasser-Boiler an Bord: Magnesiumanode einsetzen.

### FAQ-05: Was kostet ein ICCP-System fuer meine 12-m-Segelyacht?

**Antwort:** Fuer eine 12-m-GFK-Segelyacht: Materialkosten 2.500–4.500 EUR (Controller, 1–2 MMO-Anoden, Referenzelektrode, Kabel), Einbaukosten 1.000–2.000 EUR (Werft). Gesamtkosten: 3.500–6.500 EUR. Laufende Kosten: ca. 50–100 EUR/Jahr (Strom + Kalibrierung). Ab ca. 15 m LOA wirtschaftlich sinnvoll gegenueber jaehrlichen Anodenwechseln.

### FAQ-06: Galvanischer Isolator oder Trenntrafo — was brauche ich?

**Antwort:** Ein galvanischer Isolator (150–500 EUR) blockiert galvanische Gleichspannungen < 1,2 V und schuetzt gegen die haeufigsten Marina-Streustrom-Probleme. Er ist fuer 90% aller Yachten ausreichend. Ein Trenntrafo (1.500–10.000 EUR) bietet vollstaendige galvanische Trennung (DC und AC) und ist empfohlen bei: Aluminiumruempfen (erhoehtes Risiko), Marinas mit bekannten Erdungsproblemen, Yachten > 18 m, Dauerliegern.

### FAQ-07: Muss ich meinen Aluminiumrumpf anders schuetzen als GFK?

**Antwort:** Ja, fundamental anders! Aluminium ist selbst eine aktive (anodische) Legierung. Kritische Punkte:
1. NIEMALS kupferhaltiges Antifouling verwenden (auch nicht in der Naehe von Booten mit kupferhaltigem Antifouling liegen).
2. Aluminiumanoden verwenden (NICHT Zink, da Zink-Potenzial suboptimal).
3. ICCP-System dringend empfohlen (Potenzial praezise auf −800 bis −1.050 mV regeln, NIEMALS < −1.100 mV).
4. Barrier-Coat aus Epoxid (min. 3 Schichten) zwischen Rumpf und Antifouling.
5. Galvanische Isolation aller Bronze-/Kupfer-Beschlaege zum Aluminiumrumpf.

### FAQ-08: Wie messe ich, ob mein kathodischer Schutz funktioniert?

**Antwort:** Mit einem Multimeter und einer Ag/AgCl-Referenzelektrode (50–150 EUR):
1. Multimeter auf DC-Millivolt stellen.
2. Minuspol an eine blanke Metallstelle am Boot (Seeventil, Welle).
3. Referenzelektrode ins Wasser haengen (neben dem Boot, 30–50 cm unter Wasserlinie).
4. Pluspol an Referenzelektrode.
5. Ablesen: Wert sollte zwischen −800 und −1.050 mV liegen (fuer Stahl/Bronze). Fuer Aluminium: −800 bis −1.050 mV, maximal −1.100 mV.

### FAQ-09: Was ist ein Streustrom und wie erkenne ich ihn?

**Antwort:** Streustroeme sind elektrische Stroeme, die unbeabsichtigt durch das Wasser und Ihre Unterwasser-Metallteile fliessen. Typisches Zeichen: Anoden verbrauchen sich in wenigen Wochen statt Monaten. Test: Landstrom trennen und Rumpfpotenzial messen, dann Landstrom anschliessen und erneut messen. Aenderung > 50 mV = Streustrom ueber Landstrom.

### FAQ-10: Mein Boot hat einen Carbonmast — was muss ich beachten?

**Antwort:** Carbon/Graphit ist extrem kathodisch (+200 bis +300 mV vs. Ag/AgCl). Jeder Metallkontakt mit Carbon fuehrt zu beschleunigter Korrosion des Metalls. Massnahmen: Alle Carbon-Metall-Uebergaenge galvanisch isolieren (GFK-Zwischenlage, Kunststoff-Buchsen). Edelstahl-Beschlaege am Carbonmast regelmaessig inspizieren. Im Blitzschutz-Kontext: Separater Kupfer-Ableiterdraht IM Mast (Carbon leitet, aber ungleichmaessig).

### FAQ-11: Kann Blitzschutz einen Einschlag verhindern?

**Antwort:** Nein. Kein System kann einen Blitzeinschlag verhindern. Blitzschutz leitet den Blitzstrom kontrolliert ins Wasser und schuetzt dadurch Struktur und Elektronik. Sogenannte „dissipative" Systeme (Corona-Entladung) sollen die Ladung langsam ableiten, aber ihre Wirksamkeit ist wissenschaftlich nicht belegt. ABYC empfiehlt sie nicht als alleinigen Schutz.

### FAQ-12: Wie schuetze ich meine Elektronik vor Blitzschlag?

**Antwort:** Drei Massnahmen:
1. **Surge Protector** an allen Antennenkabeln (VHF, AIS, GPS, Radar, Sat) und an der Landstrom-Einspeisung.
2. **Geschirmte Kabel** fuer alle Signalkabel (insbesondere Mast → Deck).
3. **Blitz-Bonding**: Alle metallischen Gegenstaende nahe dem Mast verbinden.
Vor einem Gewitter (wenn moeglich): Antennen-Koaxkabel loesen, Handgeraete in Metallbehaelter legen.

### FAQ-13: Warum ist mein neuer Edelstahl-Propeller magnetisch?

**Antwort:** Leichte Magnetisierbarkeit bei martensitischem oder ferritischem Edelstahl ist normal und kein Qualitaetsmangel. Austenitischer Edelstahl (316L) kann durch Kaltverformung (Schmieden, Biegen) leicht magnetisch werden. Fuer Korrosionsbestaendigkeit ist der Molybdaen-Gehalt (> 2%) und die korrekte Waermebehandlung entscheidend, nicht die Magnetisierbarkeit.

### FAQ-14: Mein Zink-Anodenverbrauch ist seit dem Marina-Wechsel viel hoeher. Warum?

**Antwort:** Die wahrscheinlichste Ursache ist die Erdungsinfrastruktur der neuen Marina. Verschiedene Marinas haben unterschiedliche Erdungskonfigurationen. In manchen Marinas fliessen Streustroeme ueber den Schutzleiter (PE) und das Wasser. Loesung: Galvanischen Isolator installieren und Potenzial-Messung durchfuehren.

### FAQ-15: Welche Referenzelektrode soll ich kaufen?

**Antwort:** Fuer Yacht-Eigner empfohlen: Silber/Silberchlorid (Ag/AgCl) Referenzelektrode, tragbar, mit Kabel und Bananenstecker fuer Multimeter. Preis: 50–150 EUR. Hersteller: MG Duff, Cathelco, oder generische Labor-Referenzelektroden. Zink-Referenz als guenstigere Alternative (30–60 EUR), aber weniger genau.

### FAQ-16: Darf ich die Propellerwelle als Blitzerdung verwenden?

**Antwort:** Nur als ZUSAETZLICHE Erdung, niemals als alleinige Blitzerdung! Der Blitzstrom (bis 200 kA) fliesst durch die Lager und kann die Lageroberflaechen durch Lichtbogenbildung beschaedigen (Pitting). Eine dedizierte Erdungsplatte (min. 0,1 m²) ist zwingend. Die Welle kann eine Sekundaer-Ableitung bilden.

### FAQ-17: Kann ich Opferanoden selbst wechseln?

**Antwort:** Ja, Opferanoden-Wechsel ist eine Standard-Eigner-Arbeit beim Haul-Out. Benoetigtes Werkzeug: Schraubenschluessel (M8/M10 oder Zoll), ggf. Ringschluessel fuer Wellenanoden-Klemmschrauben. Wichtig: Kontaktflaeche am Rumpf blank schleifen (kein Antifouling zwischen Anode und Rumpf), Anoden-Bolzen mit Anti-Seize einsetzen, Wellenanoden fest anziehen.

### FAQ-18: Was ist ein Bonding-System und braucht mein Boot eines?

**Antwort:** Ein Bonding-System verbindet alle metallischen Unterwasserteile elektrisch miteinander und mit den Opferanoden. Es sorgt dafuer, dass der kathodische Schutz alle Metallteile erreicht. Jedes Boot mit mehr als einem metallischen Unterwasserteil (Propeller + Seeventile) profitiert von einem Bonding-System. Ab 10 m LOA ist es dringend empfohlen, bei professioneller Nutzung oder Klasse-Fuehrung vorgeschrieben.

### FAQ-19: Wie pruefe ich mein Bonding-System?

**Antwort:** Mit einem Multimeter (Widerstandsmessung / Durchgangspruefung):
1. Messgeraet auf Ohm stellen (niedrigster Bereich).
2. Eine Messleitung an die Bonding-Busbar.
3. Andere Messleitung an jedes Seeventil, Ruder, Welle nacheinander.
4. Jeder Wert muss < 1 Ohm sein. Werte > 1 Ohm: Verbindung reparieren.
5. Ideal: 4-Leiter-Messung (Kelvin-Messung) fuer praezise Werte.

### FAQ-20: Mein Boot hat keinen Landstromanschluss — brauche ich trotzdem einen galvanischen Isolator?

**Antwort:** Nein. Galvanische Isolatoren und Trenntrafos schuetzen ausschliesslich gegen Streustroeme ueber den Landstrom-Schutzleiter. Ohne Landstromanschluss gibt es keinen PE-Pfad und damit kein Streustrom-Risiko ueber diesen Weg. Allerdings: Wenn Sie regelmaessig neben Booten mit Landstrom liegen, kann deren Streustrom trotzdem durch das Wasser auf Ihr Boot einwirken. In diesem Fall helfen nur Opferanoden/ICCP.

### FAQ-21: Was bedeutet „galvanische Spannungsreihe"?

**Antwort:** Die galvanische Spannungsreihe ordnet Metalle nach ihrem elektrochemischen Potenzial in einem bestimmten Elektrolyten (z.B. Seewasser). Metalle mit niedrigerem (negativeren) Potenzial (z.B. Zink: −1.030 mV) sind „unedle" Metalle (Anoden). Metalle mit hoeherem Potenzial (z.B. Edelstahl passiv: −100 mV) sind „edle" Metalle (Kathoden). Wenn zwei Metalle verbunden sind, korrodiert das unedlere.

### FAQ-22: Warum bildet sich weisser Belag auf meinen Aluminiumanoden?

**Antwort:** Weisser Belag auf Aluminiumanoden ist Aluminiumhydroxid (Al(OH)3) — das ist das NORMALE Korrosionsprodukt einer arbeitenden Anode. Es zeigt, dass die Anode sich opfert und Ihre Struktur schuetzt. Dieser Belag sollte sich beim Haul-Out leicht entfernen lassen. Wenn die Anode KEINEN Belag zeigt und blank bleibt, funktioniert sie moeglicherweise nicht (passiviert).

### FAQ-23: Kann ich Bronze-Seeventile und Edelstahl-Beschlaege am gleichen Boot verwenden?

**Antwort:** Ja, das ist Standard-Praxis. Die Potenzialdifferenz zwischen Bronze (ca. −250 bis −340 mV) und passivem Edelstahl 316L (ca. −50 bis −200 mV) betraegt ca. 100–200 mV — im akzeptablen Bereich, wenn ein Bonding-System mit Opferanoden vorhanden ist. Problematisch wird es nur bei defektem Bonding, fehlendem Anodenschutz, oder wenn Edelstahl aktiv wird (Lochfrass, dann springt das Potenzial auf −430 mV und Bronze wird relativ kathodisch).

### FAQ-24: Was mache ich, wenn ich in einer Marina mit bekannten Streustrom-Problemen liege?

**Antwort:** Sofortmassnahmen:
1. Galvanischen Isolator installieren (Minimum).
2. Trenntrafo installieren (ideal).
3. Landstrom nur bei Bedarf anschliessen, nachts/bei Abwesenheit trennen.
4. Anodenzustand monatlich durch Taucher pruefen lassen.
5. Potenzial-Logger installieren (Langzeit-Ueberwachung).
6. Marina-Betreiber schriftlich auf das Problem hinweisen.
7. Bei anhaltendem Problem: Liegeplatz wechseln.

### FAQ-25: Wie lange haelt ein ICCP-System?

**Antwort:** Die einzelnen Komponenten haben unterschiedliche Lebensdauern:
- MMO-Titan-Anode: 15–25 Jahre
- Controller/Steuergeraet: 10–15 Jahre
- Referenzelektrode (Ag/AgCl): 3–7 Jahre (verschleisst, muss kalibriert/ersetzt werden)
- Kabelung: 15–20 Jahre (wenn marine-grade tinned copper)
- Gesamtsystem-Lebensdauer: 15–20 Jahre mit regelmaessiger Wartung (jaehrliche Kalibrierung, Referenzelektroden-Wechsel alle 5 Jahre)

### FAQ-26: Was kostet ein vollstaendiger Blitzschutz fuer meine 12-m-Segelyacht?

**Antwort:** Materialkosten: Air Terminal (80–150 EUR) + Ableiterkabel 4 AWG, 20 m (120–200 EUR) + Erdungsplatte/Dynaplate (280–550 EUR) + Bonding-Material (150–300 EUR) + Surge Protector x3 (300–600 EUR) = Material gesamt: 930–1.800 EUR. Installation (Werft): 800–2.000 EUR. Gesamtkosten: 1.730–3.800 EUR.

### FAQ-27: Kann Streustrom mein Boot zum Sinken bringen?

**Antwort:** Ja, in Extremfaellen. Starker Streustrom kann Bronze-Seeventile oder Bronze-Borddurchlaesse innerhalb von Wochen bis zur Undichtigkeit durchkorrodieren. Dokumentierte Faelle existieren, bei denen Boote durch Streustrom-induzierte Korrosion an Borddurchlaessen gesunken sind. Besonders gefaehrdet: Messing-Seeventile (Entzinkung bis zum Versagen), alte Bronze-Borddurchlaesse, Aluminiumruempfe.

---

## 9. Glossar

| Nr. | Begriff (DE) | Begriff (EN) | Erklaerung |
|---|---|---|---|
| G-01 | Anode | Anode | Elektrode, an der Oxidation (Metallaufloesung) stattfindet. Bei galvanischer Korrosion: das unedlere Metall. |
| G-02 | Kathode | Cathode | Elektrode, an der Reduktion stattfindet. Bei galvanischer Korrosion: das edlere Metall (wird geschuetzt). |
| G-03 | Opferanode | Sacrificial Anode | Anode aus unedlem Metall (Zn, Al, Mg), die sich kontrolliert aufloest, um andere Metalle zu schuetzen. |
| G-04 | Kathodischer Schutz | Cathodic Protection (CP) | Oberbegriff fuer alle Methoden, die eine Struktur zur Kathode machen (Opferanoden, ICCP). |
| G-05 | ICCP | Impressed Current Cathodic Protection | Kathodischer Schutz durch externen Gleichstrom ueber unlösliche Anoden. |
| G-06 | Galvanische Korrosion | Galvanic Corrosion | Korrosion durch elektrochemische Potentialdifferenz zwischen zwei verbundenen Metallen in einem Elektrolyten. |
| G-07 | Streustrom | Stray Current | Elektrischer Strom, der nicht dem vorgesehenen Leiterpfad folgt. |
| G-08 | Streustrom-Korrosion | Stray Current Corrosion | Korrosion verursacht durch Streustroeme, 10–1.000x aggressiver als galvanische Korrosion. |
| G-09 | Potenzialdifferenz | Potential Difference | Spannungsdifferenz zwischen zwei Metallen in einem Elektrolyten (treibende Kraft der Korrosion). |
| G-10 | Referenzelektrode | Reference Electrode | Elektrode mit stabilem, bekanntem Potenzial zur Messung anderer Potenziale (typisch: Ag/AgCl). |
| G-11 | Ag/AgCl | Silver/Silver Chloride | Standard-Referenzelektrode fuer Messungen in Seewasser. |
| G-12 | Schutzpotenzial | Protection Potential | Der Potenzialbereich, in dem ein Metall vor Korrosion geschuetzt ist. |
| G-13 | Ueberprotektion | Overprotection | Zu negatives Potenzial; kann Beschichtungs-Enthaftung, Wasserstoffversprödung oder Alkaliversprödung verursachen. |
| G-14 | Galvanischer Isolator | Galvanic Isolator | Elektronisches Bauteil im PE-Leiter, das galvanische Gleichspannungen < 1,2 V blockiert. |
| G-15 | Trenntrafo | Isolation Transformer | Transformator, der vollstaendige galvanische Trennung zwischen Marina-Netz und Bordnetz herstellt. |
| G-16 | Bonding | Bonding | Elektrische Verbindung metallischer Teile zum Potenzialausgleich. |
| G-17 | Bonding-Bus | Bonding Bus Bar | Zentrale Kupferschiene, an der alle Bonding-Leitungen zusammenlaufen. |
| G-18 | Wellenerdungsbuerste | Shaft Grounding Brush | Kohle- oder Silberbuerste, die die rotierende Propellerwelle elektrisch mit dem Bonding-System verbindet. |
| G-19 | MMO-Anode | Mixed Metal Oxide Anode | Titan-Anode mit Mischmetalloxid-Beschichtung fuer ICCP-Systeme; nahezu unloeslich. |
| G-20 | Entzinkung | Dezincification | Selektive Korrosion von Zink aus Messinglegierungen. |
| G-21 | DZR | Dezincification Resistant | Messinglegierung mit Zusaetzen (As, Sb), die Entzinkung hemmen. |
| G-22 | Lochfrass | Pitting Corrosion | Lokalisierte Korrosion, die tiefe, schmale Loecher bildet. |
| G-23 | Spaltkorrosion | Crevice Corrosion | Korrosion in engen Spalten durch Sauerstoffverarmung. |
| G-24 | Erosionskorrosion | Erosion Corrosion | Kombination aus mechanischem Abtrag und elektrochemischer Korrosion. |
| G-25 | Spannungsrisskorrosion | Stress Corrosion Cracking (SCC) | Rissbildung durch Zugspannung + korrosive Umgebung. |
| G-26 | Interkristalline Korrosion | Intergranular Corrosion | Korrosion entlang der Korngrenzen durch Chromverarmung. |
| G-27 | Passivierung | Passivation | Bildung einer schuetzenden Oxidschicht auf der Metalloberflaeche (z.B. Chromoxid auf Edelstahl). |
| G-28 | PRE | Pitting Resistance Equivalent | Kennzahl fuer die Lochfrass-Bestaendigkeit eines Edelstahls. PRE = %Cr + 3,3 x %Mo + 16 x %N. |
| G-29 | CPT | Critical Pitting Temperature | Temperatur, oberhalb derer Lochfrass bei einem bestimmten Edelstahl auftritt. |
| G-30 | NAB | Nickel Aluminium Bronze | Premium-Propellerlegierung mit hoher Korrosionsbestaendigkeit. |
| G-31 | Blitzschutzzone | Zone of Protection | Kegelfoermiger Schutzbereich unterhalb der Fangeinrichtung (60°-Kegel). |
| G-32 | Air Terminal | Air Terminal | Fangeinrichtung (Blitzableiter-Spitze) am hoechsten Punkt. |
| G-33 | Down Conductor | Down Conductor | Ableiterkabel vom Air Terminal zur Erdungsplatte. |
| G-34 | Erdungsplatte | Grounding Plate | Metallplatte an der Rumpfaussenseite zur Ableitung des Blitzstroms ins Wasser. |
| G-35 | Dynaplate | Dynaplate | Gesinterte Bronzeplatte mit erhoehter effektiver Oberflaeche fuer Blitz-/RF-/Bonding-Erdung. |
| G-36 | Surge Protector / SPD | Surge Protective Device | Ueberspannungsschutzgeraet fuer Antennen- und Signalkabel. |
| G-37 | Seitenueberschlag | Side Flash | Blitz springt von einem Leiter auf ein nahes Metallteil (Risiko ohne Bonding). |
| G-38 | PE / Schutzleiter | Protective Earth | Gruen-gelber Schutzleiter in der Landstrom-Einspeisung. |
| G-39 | Calcareous Deposit | Calcareous Deposit | Kalk-/Magnesiumhydroxid-Ablagerung, die sich bei kathodischem Schutz auf der Kathode bildet. |
| G-40 | Faradayscher Kaefig | Faraday Cage | Metallischer Hohlkoerper, der elektromagnetische Felder abschirmt. |
| G-41 | Sensibilisierung | Sensitization | Chromverarmung an Korngrenzen durch Waermeeinwirkung (Schweissen), macht Edelstahl anfaellig fuer interkristalline Korrosion. |
| G-42 | Alkaliversprödung | Alkaline Embrittlement | Versprödung von Aluminium durch zu negatives Schutzpotenzial (Ueberprotektion). |
| G-43 | Wasserstoffversproedung | Hydrogen Embrittlement | Aufnahme von Wasserstoff in Metall bei Ueberprotektion, fuehrt zu Versprödung und Rissbildung. |
| G-44 | Polarisation | Polarization | Aenderung des Elektrodenpotenzials durch Stromfluss. |
| G-45 | Depolarisation | Depolarization | Rueckkehr zum Open-Circuit-Potenzial nach Stromunterbrechung. |

---

## 10. Schnell-Referenz

### 10.1 Anodentyp-Schnellwahl

```
Seewasser (> 20 ppt):  → Zink ODER Aluminium
Brackwasser (5–20 ppt): → NUR Aluminium
Suesswasser (< 5 ppt):  → NUR Magnesium
Aluminiumrumpf:          → NUR Aluminium + ICCP empfohlen
Carbonrigg:              → Isolation ALLER Carbon-Metall-Kontakte
```

### 10.2 Schutzpotenziale (mV vs. Ag/AgCl)

```
Stahl:     −800 bis −1.100
Edelstahl: −500 bis −1.100
Bronze:    −300 bis −650
Aluminium: −800 bis −1.100 (STRIKT: nie < −1.100!)
Blei:      −600 bis −900
```

### 10.3 Bonding-Widerstandsgrenzwerte

```
Jede Einzelverbindung:  < 1,0 Ohm
Idealwert:              < 0,5 Ohm
Wellenerdungsbuerste:   < 0,1 Ohm (Kontakt-Pruefung)
Gesamtsystem (max):     < 1,0 Ohm
```

### 10.4 Blitzschutz-Mindestanforderungen

```
Air Terminal:        Min. 150 mm ueber Mastspitze, Kupfer 10 mm / Edelstahl 12 mm
Ableiterkabel:       Min. 4 AWG (21 mm²) Kupfer, verzinnt
Biegungsradius:      > 200 mm (keine scharfen Knicke)
Erdungsplatte:       Min. 0,1 m² (929 cm²) Kupfer/Bronze
Bonding (Blitz):     Min. 6 AWG (13,3 mm²) zu allen Metallteilen < 1,8 m vom Ableiterpfad
Schutzradius:        Masthoehe x 0,577
```

### 10.5 Streustrom-Schnelltest

```
1. Multimeter + Ag/AgCl-Referenzelektrode bereithalten
2. Landstrom GETRENNT → Potenzial messen → Wert notieren
3. Landstrom ANGESCHLOSSEN → Potenzial messen → Wert notieren
4. Differenz > 50 mV → Streustrom ueber Landstrom vorhanden!
5. DC-Clamp-Meter am Landkabel: > 10 mA → Streustrom bestaetigt
```

### 10.6 Notfall-Checkliste Blitzeinschlag

```
□ Sicherheit der Crew pruefen (Verletzungen?)
□ Wassereinbruch pruefen (Bilge, Seeventile)
□ Batterien abklemmen (beide Pole)
□ Brandgefahr pruefen (Geruch, Rauch)
□ NICHT den Mast oder Wanten beruehren
□ Alle Elektronik NICHT einschalten (erst Fachmann)
□ Versicherung benachrichtigen
□ Fotografische Dokumentation aller Schaeden
□ Mast-Inspektion anfordern (Rigger)
□ Vollstaendige Elektronik-Pruefung durch Fachbetrieb
```

### 10.7 Jaehrliche Korrosionsschutz-Checkliste (Haul-Out)

```
□ Anodenzustand dokumentieren (Foto + Restgewicht schaetzen)
□ Anoden ersetzen wenn < 50% verblieben
□ Kontaktflaechen blank schleifen (kein Antifouling zwischen Anode/Rumpf)
□ Bonding-Durchgangspruefung (alle Verbindungspunkte messen)
□ Wellenerdungsbuerste pruefen (Widerstand < 0,1 Ohm)
□ Seeventile auf Korrosion inspizieren (Entzinkung? Lochfrass?)
□ Propeller inspizieren (Verfaerbung? Poroesitaet? Risse?)
□ ICCP-System kalibrieren (falls vorhanden)
□ Referenzelektrode pruefen (falls vorhanden)
□ Blitzschutz-Durchgangspruefung (Air Terminal → Erdungsplatte)
□ Galvanischen Isolator testen (Dioden-Funktionstest)
□ Alle Befunde im Wartungsprotokoll dokumentieren
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: 36-ft-Segelyacht, Mittelmeer, Saildrive-Korrosion

**Ausgangslage:**
- Yacht: Bavaria 36, Baujahr 2018, GFK-Rumpf
- Antrieb: Volvo Penta D2-40 mit Saildrive 130S
- Liegeplatz: Marina Kroatien, Dauerliegeplatz mit Landstrom
- Problem: Saildrive-Gehaeuse stark korrodiert nach nur 2 Saisons

**Befund bei Haul-Out:**
- Saildrive-Opferanoden (Zink) vollstaendig aufgeloest (100% Verbrauch in 8 Monaten)
- Saildrive-Gehaeuse (Aluminium-Legierung) mit grossflaechigem Lochfrass
- Propeller (Aluminium) mit weissen Ablagerungen und Erosion
- Rumpf-Zinkanoden ebenfalls > 80% verbraucht

**Diagnose:**
- Streustrom-Test: Potenzialänderung +180 mV bei Landstrom-Anschluss → massiver Streustrom
- Ursache: Nachbarboot (Stahlyacht, 45 ft) mit defektem Laderegler sendete Streustrom ueber Marina-Erdung
- Fehlender galvanischer Isolator an der Bavaria

**Massnahmen:**
1. Saildrive-Gehaeuse professionell aufarbeiten (Korrosionsstellen abschleifen, Epoxid-Primer, Antifouling)
2. Neue Saildrive-Anoden (Aluminium statt Zink — Kroatien hat teils < 35 ppt Salzgehalt)
3. Galvanischer Isolator Newmar GI-30 installiert (230 EUR)
4. Bonding-System geprueft und nachgebessert (2 Verbindungen > 3 Ohm repariert)
5. Nachbar-Boot-Eigner und Marina informiert

**Kosten:**
- Saildrive-Aufarbeitung: 2.800 EUR
- Neue Anoden (Aluminium): 120 EUR
- Galvanischer Isolator + Installation: 380 EUR
- Bonding-Reparatur: 200 EUR
- **Gesamt: 3.500 EUR** (waere mit Isolator von Anfang an vermeidbar gewesen: 380 EUR)

**AYDI-Bewertung:** Confidence measured (Potenzial-Messung, Streustrom-Nachweis)

---

### ANHANG B — Fallstudie: 48-ft-Aluminium-Segelyacht, Ostsee, Rumpfkorrosion

**Ausgangslage:**
- Yacht: Garcia Exploration 45, Baujahr 2020, Aluminiumrumpf (5083-H321)
- Liegeplatz: Ostsee (Kieler Foerde), Salzgehalt ca. 15 ppt (Brackwasser)
- Problem: Lokalisierte Korrosion am Rumpf im Bereich der Seeventile

**Befund:**
- Zinkanoden am Rumpf: Vollstaendig passiviert (weisser, harter Belag, keine Aufloesung)
- Rumpf im Bereich Seeventile: Lochfrass-Muster im Aluminium (Tiefe bis 1,5 mm)
- Bronze-Seeventile: Keine sichtbare Korrosion (Bronze ist kathodisch → wird geschuetzt)

**Diagnose:**
- Zinkanoden passivieren in Brackwasser (< 20 ppt Salzgehalt)
- Bronze-Seeventile als Kathode, Aluminiumrumpf als Anode → galvanische Korrosion des Rumpfes
- Fehlende galvanische Isolation zwischen Bronze-Seeventilen und Alu-Rumpf

**Massnahmen:**
1. Alle Zinkanoden durch Aluminiumanoden ersetzt (MG Duff ALLHULL-Serie)
2. GFK-Isolierflansche an allen Bronze-Seeventilen installiert
3. Bonding-System ueberarbeitet (separate Bonding-Buerste fuer Seeventile mit Isolation)
4. ICCP-System installiert (Potenzialregelung −850 bis −1.050 mV, Alarmgrenze −1.100 mV)
5. Korrosionsstellen am Rumpf aufgeschweisst und plangeschliffen
6. Barrier-Coat (3x International Interprotect) + kupferfreies Antifouling

**Kosten:**
- Rumpf-Reparatur (Schweissen): 8.500 EUR
- Aluminiumanoden: 280 EUR
- GFK-Isolierflansche (6 Stueck): 450 EUR
- ICCP-System: 5.200 EUR
- Barrier-Coat + Antifouling: 1.800 EUR
- **Gesamt: 16.230 EUR**

**AYDI-Bewertung:** Confidence measured + visual_high

---

### ANHANG C — Fallstudie: 55-ft-Motoryacht, Florida, Blitzeinschlag

**Ausgangslage:**
- Yacht: Princess V55, Baujahr 2019, GFK-Rumpf
- Liegeplatz: Fort Lauderdale, Florida (hoechste Blitzdichte in USA)
- Blitzschutz: KEINER (wie bei den meisten Motoryachten)
- Ereignis: Blitzeinschlag waehrend Sommergewitter (Boot am Steg, kein Landstrom)

**Schaeden:**
- VHF-Antenne durchgeschmolzen (Einschlagpunkt)
- Radar-Antenne auf Flybridge: Totalschaden
- Alle Elektronik auf der Bruecke: Totalschaden (2x Garmin 8616, Radar, AIS, Autopilot)
- Sternfoermiger Riss im GFK-Aufbau unter der VHF-Antenne
- Landstrom-Ladegeraet: Durchgebrannt (induktive Kopplung ueber Kabel)
- Hydraulik-Steuerung: Undicht (elektrischer Durchschlag an Ventil)
- GPS-Antennenkabel: Geschmolzen
- NMEA-2000-Netzwerk: Alle angeschlossenen Geraete defekt

**Schadensumme:**
- Elektronik-Ersatz: 42.000 EUR
- GFK-Reparatur: 6.500 EUR
- Hydraulik-Reparatur: 3.800 EUR
- Arbeitskosten: 12.000 EUR
- **Gesamt: 64.300 EUR**

**Nachruestung Blitzschutz:**
- Air Terminal auf Flybridge-Radararch: 180 EUR
- Ableiterkabel 4 AWG (25 m): 250 EUR
- Dynaplate DynaStar 200: 480 EUR
- Blitz-Bonding (Flybridge, Reling, Bugkorb, Heckkorb): 800 EUR
- Surge Protector (5 Stueck, alle Antennen + Landstrom): 650 EUR
- Installation: 2.500 EUR
- **Gesamt Blitzschutz: 4.860 EUR** (7,6% des Schadensbetrags)

**AYDI-Bewertung:** Confidence documented (Versicherungsgutachten, Foto-Dokumentation)

---

### ANHANG D — Fallstudie: 30-ft-Segelyacht, Binnensee, Magnesiumanoden

**Ausgangslage:**
- Yacht: Dehler 30, Baujahr 2015, GFK-Rumpf
- Liegeplatz: Bodensee (Suesswasser, Leitfaehigkeit ca. 0,03 S/m)
- Problem: Bronze-Seeventile mit gruener Patina trotz „Anoden"

**Befund:**
- Zinkanoden installiert (korrekte Groesse, korrekte Platzierung)
- Zinkanoden vollstaendig intakt nach 3 Jahren — KEINE Aufloesungsspuren!
- Bronze-Seeventile mit fortgeschrittener Korrosion
- Bonding-System vorhanden und intakt (< 0,5 Ohm)

**Diagnose:**
- Zinkanoden passivieren in Suesswasser (Leitfaehigkeit viel zu gering)
- Die Anoden „arbeiten" nicht — sie schuetzen nichts
- Der Eigner wusste nicht, dass Suesswasser Magnesiumanoden erfordert

**Massnahmen:**
1. Alle Zinkanoden durch Magnesiumanoden ersetzt (MG Duff MGHULL-Serie)
2. Seeventile inspiziert — 2 von 4 noch innerhalb Toleranz, 2 ersetzt (Rotguss)
3. Magnesiumanode im Heisswasser-Boiler nachgeruestet

**Kosten:**
- Magnesiumanoden: 150 EUR
- 2 neue Seeventile (Rotguss, TruDesign): 380 EUR
- Boiler-Anode: 25 EUR
- Arbeitskosten: 400 EUR
- **Gesamt: 955 EUR**

**AYDI-Bewertung:** Confidence estimated + visual_medium

---

### ANHANG E — Fallstudie: 72-ft-Superyacht, Karibik, ICCP-Fehlfunktion

**Ausgangslage:**
- Yacht: Sunseeker 72, Baujahr 2016, GFK-Rumpf
- ICCP-System installiert (2 MMO-Anoden, 1 Ag/AgCl-Referenz, Controller)
- Liegeplatz: St. Maarten, Karibik
- Problem: Antifouling loest sich grossflaechig ab, Beschichtung blaettert

**Befund:**
- ICCP-Controller zeigt „Normal", Potenzial angeblich −950 mV
- Externe Messung mit tragbarer Referenzelektrode: −1.280 mV! (massive Ueberprotektion)
- Antifouling-Enthaftung durch alkalische Umgebung an der Rumpfoberflaeche
- Weisse Ablagerungen (Calcareous Deposits) auf grossen Rumpfflaechen

**Diagnose:**
- Referenzelektrode fehlkalibriert (zeigt 330 mV zu positiv an)
- Referenzelektrode war 7 Jahre alt, nie gewechselt
- Controller regelt auf angeblich −950 mV, tatsaechlich aber −1.280 mV
- In tropischem Wasser (28 C, hohe Leitfaehigkeit) → extrem hoher Schutzstrom

**Massnahmen:**
1. ICCP sofort abgeschaltet
2. Neue Ag/AgCl-Referenzelektrode installiert und kalibriert
3. Zweite (redundante) Referenzelektrode installiert (Cross-Check)
4. Potenzial-Logger angeschlossen (24/7-Ueberwachung mit Alarm)
5. Rumpf komplett neu beschichtet (Barrier-Coat + Antifouling)
6. ICCP nach Neukalibrierung wieder in Betrieb

**Kosten:**
- Neue Referenzelektroden (2x): 650 EUR
- Potenzial-Logger: 1.200 EUR
- Rumpf-Neubeschichtung (72 ft): 28.000 EUR
- Haul-Out + Kraning: 6.000 EUR
- **Gesamt: 35.850 EUR**

**AYDI-Bewertung:** Confidence measured (externe Potenzial-Messung)

---

### ANHANG F — Fallstudie: 40-ft-Stahlketch, Weltumsegelung, Korrosionsschutz-Planung

**Ausgangslage:**
- Yacht: Stahlketch, Eigenbau (NL), 2017, Stahlrumpf (S355)
- Geplante Route: Nordsee → Mittelmeer → Atlantik → Karibik → Panamakanal → Pazifik
- Anforderung: Korrosionsschutz fuer alle Klimazonen, 3 Jahre ohne Werftaufenthalt

**Korrosionsschutz-Konzept:**
1. **Beschichtung:** 2K-Epoxid (Jotun Jotamastic 87, 3x 125 um) + Antifouling (2x Copper Coat Permanent)
2. **Opferanoden:** Aluminiumanoden (universell — See- und Brackwasser)
   - Rumpf: 8x ALLHULL5 (je 3,0 kg) = 24 kg Aluminium, Kapazitaet 64.800 Ah
   - Welle: 2x AD60 (je 1,8 kg)
   - Ruder: 2x AD55 (je 0,9 kg)
   - Gesamtgewicht: ca. 30 kg Aluminium
3. **ICCP:** NICHT installiert (Stromversorgung auf Langstrecke unsicher)
4. **Bonding:** Vollstaendiges DC-Bonding (Stahlrumpf ist selbst die Bonding-Masse)
5. **Galvanischer Isolator:** Newmar GI-30 (fuer Marinas)
6. **Blitzschutz:** Mast + Wanten als Ableiterpfad → Stahlrumpf als Erdung (Ideal!)
7. **Reserve-Anoden:** 4x ALLHULL5 als Ersatz an Bord (12 kg)

**Dimensionierungsrechnung:**
- Zu schuetzende Flaeche (nackte Metalle): ca. 2,5 m² (Propeller, Welle, Ruder, Seeventile)
- Beschaedigte Beschichtung (3% Annahme nach 1 Jahr): 2,4 m² Rumpf
- Gesamtflaeche: ca. 5 m²
- Stromdichte (beschichteter Stahl, tropisch): 30 mA/m²
- Erforderlicher Strom: 5 x 30 = 150 mA
- Erforderliche Kapazitaet (3 Jahre = 26.280 h): 150 mA x 26.280 h = 3.942 Ah
- Installierte Kapazitaet: 64.800 Ah → Sicherheitsfaktor 16,4 (sehr konservativ, beruecksichtigt Beschichtungsdegradation)

**Ergebnis nach 3 Jahren:**
- Anoden ca. 30–40% verbraucht (Rest ausreichend fuer weitere 2+ Jahre)
- Keine Korrosionsschaeden an Rumpf oder Beschlaegen
- 2 Bonding-Verbindungen waehrend Reise nachgezogen (Vibrationen)
- Galvanischer Isolator 2x ausgeloest (defekte Marina in Panama, Fiji)

**AYDI-Bewertung:** Confidence calculated + documented

---

### ANHANG G — Fallstudie: Marina-Erdungsproblem — 5 Boote betroffen

**Ausgangslage:**
- Marina: Mittelmeer, Suedfrankreich, 120 Liegeplaetze
- Problem: 5 Boote in einem Steg-Abschnitt melden gleichzeitig erhoehten Anodenverbrauch

**Untersuchung:**
- Potenzial-Messungen an allen 5 Booten → alle zeigen Potenzialsprung > 100 mV bei Landstrom
- DC-Milliamperemeter an Landkabeln: Boot 3 (Stahlyacht, 52 ft) zeigt 1,8 A Leckstrom!
- Isolationsmessung Boot 3: Warmwasser-Boiler hat Isolationsfehler (35 kOhm statt > 1 MOhm)
- Der Strom fliesst: Boiler → Rumpfmasse → Wasser → Anoden der Nachbarboote → Marina-PE → zurueck

**Schaeden:**
- Boot 1 (Bavaria 40): Propelleranoden verbraucht, Propeller-Korrosion beginnt
- Boot 2 (Jeanneau 44): Saildrive-Anoden verbraucht, Saildrive-Gehaeuse angegriffen
- Boot 4 (Hallberg-Rassy 43): Rumpfanoden verbraucht, Seeventile verfaerbt
- Boot 5 (Beneteau 38): Anoden verbraucht, keine strukturellen Schaeden

**Massnahmen:**
1. Boot 3: Warmwasser-Boiler repariert (Heizelement ersetzt, Isolationswiderstand > 50 MOhm)
2. Alle 5 Boote: Neue Anoden
3. Marina: Fehlerstrom-Schutzschalter (RCD) pro Steg nachgeruestet
4. Empfehlung an alle Bootseigner: Galvanische Isolatoren installieren

**Gesamtschaden:** ca. 12.000 EUR (5 Boote zusammen)
**Verursacher-Anteil (Boot 3):** Warmwasser-Boiler-Reparatur: 350 EUR

**AYDI-Bewertung:** Confidence measured (systematische Potenzial- und Strommessungen)

---

### ANHANG H — Fallstudie: Carbon-Mast auf Alu-Deck — Galvanische Katastrophe

**Ausgangslage:**
- Yacht: 45-ft-Performance-Cruiser, Aluminium-Deck, Carbon-Mast
- Werft: Bau 2021, renommierte EU-Werft
- Problem: Nach 18 Monaten starke Korrosion am Aluminium-Deck rund um den Mastfuss

**Befund:**
- Aluminium-Deck im Umkreis von 300 mm um den Mastfuss: Tiefe Lochfrass-Muster (bis 2 mm)
- Mastfuss-Bereich: Weiße puderige Ablagerungen (Aluminiumoxid/-hydroxid)
- Carbon-Mast im Kontaktbereich: Keine sichtbare Korrosion
- Feuchtigkeit: Kondenswasser und Regenwasser dringen in den Mastfuss-Bereich ein

**Diagnose:**
- Carbon (+200 bis +300 mV) in direktem Kontakt mit Aluminium (−750 bis −850 mV)
- Potenzialdifferenz: ca. 1.000–1.100 mV → extreme galvanische Korrosion
- Flaechenverhaeltnis: Grosser Carbon-Mast (Kathode) vs. kleiner Alu-Kontaktbereich (Anode)
- Feuchtigkeit (Kondenswasser/Regen) als Elektrolyt ausreichend
- Werft hatte keine galvanische Isolation zwischen Carbon-Mast und Alu-Deck vorgesehen

**Massnahmen:**
1. Mast ausbauen
2. Korrodiertes Aluminium ausschneiden und neue Platte einschweissen
3. GFK-Isolierschicht zwischen Mastfuss und Alu-Deck (3 mm GFK-Platte + Epoxid-Kaschierung)
4. Nylon-Buchsen in allen Mastfuss-Bolzen (galvanische Isolation)
5. Drainage-Bohrungen am Mastfuss (Feuchtigkeit sofort abfuehren)
6. Epoxid-Versiegelung des Alu-Decks im Kontaktbereich

**Kosten:**
- Mast-Aus-/Einbau: 4.500 EUR
- Alu-Reparatur (Schweissen): 6.800 EUR
- Isolationsmassnahmen: 1.200 EUR
- Drainage-/Versiegelungsarbeiten: 800 EUR
- **Gesamt: 13.300 EUR**

**Garantie:** Werft uebernahm 100% der Kosten (Konstruktionsfehler)

**AYDI-Bewertung:** Confidence visual_high + documented

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Korrosionsanalyse-Modelle

```python
"""
AYDI 22.10 — Galvanische Korrosion und Blitzschutz
Pydantic v2 Modelle fuer Pipeline A (Structured Analysis)

IMPORTANT: Uses model_config = {"from_attributes": True} (Pydantic v2)
           NEVER use class Config (Pydantic v1 pattern)
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict, Literal
from enum import Enum
from datetime import date


# ──────────────────────────────────────────────
# Enums
# ──────────────────────────────────────────────

class CorrosionType(str, Enum):
    """Korrosionsart nach ISO 8044"""
    GALVANIC = "galvanic"                       # Bimetall-Korrosion
    STRAY_CURRENT = "stray_current"             # Streustrom-Korrosion
    PITTING = "pitting"                         # Lochfrass
    CREVICE = "crevice"                         # Spaltkorrosion
    DEZINCIFICATION = "dezincification"         # Entzinkung
    EROSION_CORROSION = "erosion_corrosion"     # Erosionskorrosion
    INTERGRANULAR = "intergranular"             # Interkristalline Korrosion
    STRESS_CORROSION = "stress_corrosion"       # Spannungsrisskorrosion
    UNIFORM = "uniform"                         # Gleichmaessige Flaechenkorrosion
    MICROBIOLOGICAL = "microbiological"         # Mikrobiologisch induzierte Korrosion


class CorrosionSeverity(str, Enum):
    """Korrosionsschwere"""
    NONE = "none"
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    CRITICAL = "critical"


class ProtectionStatus(str, Enum):
    """Schutzstatus des kathodischen Systems"""
    PROTECTED = "protected"                     # Im Schutzbereich
    UNDERPROTECTED = "underprotected"           # Potenzial zu positiv
    OVERPROTECTED = "overprotected"             # Potenzial zu negativ
    UNPROTECTED = "unprotected"                 # Kein Schutz vorhanden
    UNKNOWN = "unknown"                         # Nicht gemessen


class AnodeType(str, Enum):
    """Opferanodentyp"""
    ZINC = "zinc"
    ALUMINUM = "aluminum"
    MAGNESIUM = "magnesium"


class WaterType(str, Enum):
    """Wassertyp fuer Anodenauswahl"""
    SEAWATER = "seawater"           # > 20 ppt
    BRACKISH = "brackish"           # 5-20 ppt
    FRESHWATER = "freshwater"       # < 5 ppt


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Levels"""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


# ──────────────────────────────────────────────
# Core Assessment Models
# ──────────────────────────────────────────────

class GalvanicPairRisk(BaseModel):
    """Bewertung einer galvanischen Materialpaarung"""
    model_config = {"from_attributes": True}

    material_noble: str = Field(
        ...,
        description="Edleres Material (Kathode), z.B. 'Edelstahl 316L passiv'"
    )
    material_active: str = Field(
        ...,
        description="Unedleres Material (Anode), z.B. 'Aluminium 5083'"
    )
    potential_noble_mv: float = Field(
        ...,
        description="Potenzial des edleren Materials (mV vs. Ag/AgCl)"
    )
    potential_active_mv: float = Field(
        ...,
        description="Potenzial des unedleren Materials (mV vs. Ag/AgCl)"
    )
    potential_difference_mv: float = Field(
        ...,
        description="Potenzialdifferenz (mV)"
    )
    area_ratio_cathode_anode: Optional[float] = Field(
        None,
        description="Flaechenverhaeltnis Kathode:Anode"
    )
    corrosion_rate_relative: float = Field(
        ...,
        description="Relative Korrosionsrate (1.0 = Standard)"
    )
    severity: CorrosionSeverity = Field(
        ...,
        description="Korrosionsschwere"
    )
    electrolyte: WaterType = Field(
        ...,
        description="Elektrolyttyp"
    )
    time_to_failure_months: Optional[int] = Field(
        None,
        description="Geschaetzte Zeit bis zum Versagen (Monate)"
    )
    affected_component_de: str = Field(
        ...,
        description="Betroffenes Bauteil (deutsch)"
    )
    failure_mode_de: str = Field(
        ...,
        description="Schadensmechanismus (deutsch)"
    )
    prevention_measures_de: List[str] = Field(
        default_factory=list,
        description="Praeventionsmassnahmen (deutsch)"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="AYDI Confidence Level"
    )

    @field_validator("potential_difference_mv")
    @classmethod
    def validate_potential_diff(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Potenzialdifferenz muss positiv sein (absoluter Betrag)")
        return v


class StrayCurrentAssessment(BaseModel):
    """Bewertung der Streustrom-Situation"""
    model_config = {"from_attributes": True}

    potential_no_shore_power_mv: Optional[float] = Field(
        None,
        description="Rumpfpotenzial ohne Landstrom (mV vs. Ag/AgCl)"
    )
    potential_with_shore_power_mv: Optional[float] = Field(
        None,
        description="Rumpfpotenzial mit Landstrom (mV vs. Ag/AgCl)"
    )
    potential_shift_mv: Optional[float] = Field(
        None,
        description="Potenzialänderung durch Landstrom (mV)"
    )
    leakage_current_ma: Optional[float] = Field(
        None,
        description="Leckstrom am Landkabel (mA DC)"
    )
    stray_current_detected: bool = Field(
        ...,
        description="Streustrom erkannt (ja/nein)"
    )
    stray_current_source: Optional[str] = Field(
        None,
        description="Vermutete Streustromquelle"
    )
    severity: CorrosionSeverity = Field(
        ...,
        description="Schwere des Streustrom-Problems"
    )
    galvanic_isolator_present: bool = Field(
        False,
        description="Galvanischer Isolator vorhanden"
    )
    galvanic_isolator_functional: Optional[bool] = Field(
        None,
        description="Galvanischer Isolator funktionsfaehig"
    )
    isolation_transformer_present: bool = Field(
        False,
        description="Trenntrafo vorhanden"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="AYDI Confidence Level"
    )


class AnodeCondition(BaseModel):
    """Zustandsbewertung einer einzelnen Opferanode"""
    model_config = {"from_attributes": True}

    location_de: str = Field(
        ...,
        description="Einbauort (deutsch), z.B. 'Steuerbord-Rumpf, mittschiffs'"
    )
    anode_type: AnodeType = Field(
        ...,
        description="Anodentyp (Zink/Aluminium/Magnesium)"
    )
    manufacturer: Optional[str] = Field(
        None,
        description="Hersteller, z.B. 'MG Duff'"
    )
    model: Optional[str] = Field(
        None,
        description="Modellbezeichnung, z.B. 'CM3H'"
    )
    weight_new_kg: Optional[float] = Field(
        None,
        description="Gewicht bei Installation (kg)"
    )
    weight_current_kg: Optional[float] = Field(
        None,
        description="Aktuelles Gewicht (geschaetzt, kg)"
    )
    consumption_percent: float = Field(
        ...,
        ge=0,
        le=100,
        description="Verbrauch in Prozent (0-100)"
    )
    months_since_installation: Optional[int] = Field(
        None,
        description="Monate seit Installation"
    )
    consumption_rate_percent_per_month: Optional[float] = Field(
        None,
        description="Verbrauchsrate (% pro Monat)"
    )
    is_passivated: bool = Field(
        False,
        description="Anode passiviert (hart, weisser Belag, keine Aufloesung)"
    )
    bonding_connection_intact: Optional[bool] = Field(
        None,
        description="Bonding-Verbindung zum Anode intakt"
    )
    assessment_de: str = Field(
        ...,
        description="Bewertung (deutsch)"
    )
    action_required_de: str = Field(
        ...,
        description="Erforderliche Massnahme (deutsch)"
    )
    urgency: Literal["immediate", "next_haulout", "routine", "monitor"] = Field(
        ...,
        description="Dringlichkeit"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG J — ICCP-System-Modelle

```python
"""
AYDI 22.10 — ICCP System Models
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
from enum import Enum


class ICCPSystemStatus(str, Enum):
    """ICCP Systemstatus"""
    OPERATIONAL = "operational"
    UNDERPROTECTING = "underprotecting"
    OVERPROTECTING = "overprotecting"
    FAULT = "fault"
    OFFLINE = "offline"
    NOT_INSTALLED = "not_installed"


class ICCPAnodeType(str, Enum):
    """ICCP Anodentyp"""
    MMO_TITANIUM = "mmo_titanium"
    PLATINUM_TITANIUM = "platinum_titanium"
    SILICON_IRON = "silicon_iron"
    GRAPHITE = "graphite"


class ICCPSystemAssessment(BaseModel):
    """Bewertung eines ICCP-Systems"""
    model_config = {"from_attributes": True}

    system_installed: bool = Field(
        ...,
        description="ICCP-System installiert"
    )
    manufacturer: Optional[str] = Field(
        None,
        description="Hersteller des Systems"
    )
    model: Optional[str] = Field(
        None,
        description="Modellbezeichnung"
    )
    installation_year: Optional[int] = Field(
        None,
        description="Installationsjahr"
    )
    anode_type: Optional[ICCPAnodeType] = Field(
        None,
        description="ICCP-Anodentyp"
    )
    anode_count: Optional[int] = Field(
        None,
        description="Anzahl ICCP-Anoden"
    )
    reference_electrode_type: Optional[str] = Field(
        None,
        description="Typ der Referenzelektrode (Ag/AgCl, Zink)"
    )
    reference_electrode_age_years: Optional[float] = Field(
        None,
        description="Alter der Referenzelektrode (Jahre)"
    )
    controller_set_point_mv: Optional[float] = Field(
        None,
        description="Sollpotenzial am Controller (mV vs. Ag/AgCl)"
    )
    measured_potential_mv: Optional[float] = Field(
        None,
        description="Gemessenes Potenzial (externe Referenz, mV vs. Ag/AgCl)"
    )
    controller_displayed_potential_mv: Optional[float] = Field(
        None,
        description="Am Controller angezeigtes Potenzial (mV vs. Ag/AgCl)"
    )
    output_current_a: Optional[float] = Field(
        None,
        description="Ausgangsstrom (A)"
    )
    output_voltage_v: Optional[float] = Field(
        None,
        description="Ausgangsspannung (V)"
    )
    status: ICCPSystemStatus = Field(
        ...,
        description="Systemstatus"
    )
    calibration_due: Optional[bool] = Field(
        None,
        description="Kalibrierung faellig"
    )
    backup_anodes_present: bool = Field(
        False,
        description="Backup-Opferanoden vorhanden"
    )
    findings_de: List[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )

    @field_validator("reference_electrode_age_years")
    @classmethod
    def warn_old_reference(cls, v: Optional[float]) -> Optional[float]:
        # Validation logic: flag if reference electrode is old
        return v


class ICCPDimensioning(BaseModel):
    """ICCP-Dimensionierungsberechnung"""
    model_config = {"from_attributes": True}

    hull_material: str = Field(
        ...,
        description="Rumpfmaterial (GFK, Stahl, Aluminium)"
    )
    loa_m: float = Field(
        ...,
        description="Laenge ueber Alles (m)"
    )
    beam_m: float = Field(
        ...,
        description="Breite (m)"
    )
    draft_m: float = Field(
        ...,
        description="Tiefgang (m)"
    )
    wetted_surface_m2: float = Field(
        ...,
        description="Benetzte Flaeche (m²)"
    )
    coating_condition: Literal["new", "good", "fair", "poor", "bare"] = Field(
        ...,
        description="Beschichtungszustand"
    )
    bare_metal_area_m2: float = Field(
        ...,
        description="Nackte Metallflaeche (Beschlaege, Propeller etc.) in m²"
    )
    water_type: str = Field(
        ...,
        description="Wassertyp (seawater/brackish/freshwater)"
    )
    water_temperature_c: Optional[float] = Field(
        None,
        description="Wassertemperatur (C)"
    )
    current_density_coated_ma_m2: float = Field(
        ...,
        description="Stromdichte beschichtete Flaeche (mA/m²)"
    )
    current_density_bare_ma_m2: float = Field(
        ...,
        description="Stromdichte nackte Flaeche (mA/m²)"
    )
    total_current_required_a: float = Field(
        ...,
        description="Erforderlicher Gesamtstrom (A)"
    )
    recommended_anode_count: int = Field(
        ...,
        description="Empfohlene Anodenanzahl"
    )
    recommended_controller_rating_a: float = Field(
        ...,
        description="Empfohlene Controller-Nennleistung (A)"
    )
    estimated_power_consumption_w: float = Field(
        ...,
        description="Geschaetzter Stromverbrauch (W)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG K — Bonding-System-Modelle

```python
"""
AYDI 22.10 — Bonding System Models
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum


class BondingPurpose(str, Enum):
    """Bonding-Zweck"""
    DC_CORROSION = "dc_corrosion"
    RF_GROUND = "rf_ground"
    LIGHTNING = "lightning"
    COMBINED = "combined"


class BondingConnectionStatus(str, Enum):
    """Status einer Bonding-Verbindung"""
    GOOD = "good"               # < 0.5 Ohm
    ACCEPTABLE = "acceptable"   # 0.5–1.0 Ohm
    DEGRADED = "degraded"       # 1.0–5.0 Ohm
    BROKEN = "broken"           # > 5.0 Ohm oder offen
    NOT_MEASURED = "not_measured"


class BondingConnection(BaseModel):
    """Einzelne Bonding-Verbindung"""
    model_config = {"from_attributes": True}

    component_de: str = Field(
        ...,
        description="Verbundene Komponente (deutsch), z.B. 'Steuerbord-Seeventil Kuehlung'"
    )
    component_type: str = Field(
        ...,
        description="Komponententyp: seacock, thru_hull, shaft, rudder, keel, saildrive, engine, tank, shroud, stanchion, winch"
    )
    material: str = Field(
        ...,
        description="Material der Komponente"
    )
    cable_gauge_awg: Optional[int] = Field(
        None,
        description="Kabelquerschnitt (AWG)"
    )
    cable_gauge_mm2: Optional[float] = Field(
        None,
        description="Kabelquerschnitt (mm²)"
    )
    resistance_ohm: Optional[float] = Field(
        None,
        description="Gemessener Widerstand (Ohm)"
    )
    status: BondingConnectionStatus = Field(
        ...,
        description="Verbindungsstatus"
    )
    cable_condition_de: Optional[str] = Field(
        None,
        description="Kabelzustand (deutsch)"
    )
    terminal_condition_de: Optional[str] = Field(
        None,
        description="Kabelschuh-Zustand (deutsch)"
    )
    last_measured: Optional[str] = Field(
        None,
        description="Letztes Messdatum (ISO 8601)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )


class BondingSystemAssessment(BaseModel):
    """Gesamtbewertung des Bonding-Systems"""
    model_config = {"from_attributes": True}

    bonding_type: BondingPurpose = Field(
        ...,
        description="Bonding-Zweck/Typ"
    )
    bus_bar_present: bool = Field(
        ...,
        description="Bonding-Busbar vorhanden"
    )
    bus_bar_material: Optional[str] = Field(
        None,
        description="Busbar-Material (Kupfer, verzinnt etc.)"
    )
    bus_bar_dimensions_mm: Optional[str] = Field(
        None,
        description="Busbar-Abmessungen (mm), z.B. '25x3'"
    )
    total_connections: int = Field(
        ...,
        description="Gesamtanzahl Bonding-Verbindungen"
    )
    connections: List[BondingConnection] = Field(
        default_factory=list,
        description="Einzelne Bonding-Verbindungen"
    )
    connections_good: int = Field(
        0,
        description="Anzahl Verbindungen mit Status 'good'"
    )
    connections_degraded: int = Field(
        0,
        description="Anzahl Verbindungen mit Status 'degraded' oder 'broken'"
    )
    shaft_grounding_brush_present: bool = Field(
        False,
        description="Wellenerdungsbuerste vorhanden"
    )
    shaft_grounding_brush_resistance_ohm: Optional[float] = Field(
        None,
        description="Widerstand Wellenerdungsbuerste (Ohm)"
    )
    overall_status_de: str = Field(
        ...,
        description="Gesamtbewertung (deutsch)"
    )
    findings_de: List[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )
    score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Bonding-System-Score (0-100)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG L — Blitzschutz-Modelle

```python
"""
AYDI 22.10 — Lightning Protection Models
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
from enum import Enum
import math


class LightningRiskLevel(str, Enum):
    """Blitzschlag-Risikolevel"""
    VERY_HIGH = "very_high"     # Florida, Tropen
    HIGH = "high"               # Mittelmeer Sommer
    MODERATE = "moderate"       # Nordsee, Atlantik
    LOW = "low"                 # Skandinavien, Winter


class LightningProtectionStatus(str, Enum):
    """Blitzschutz-Status"""
    COMPLETE = "complete"
    PARTIAL = "partial"
    ABSENT = "absent"
    UNKNOWN = "unknown"


class LightningZoneCalculation(BaseModel):
    """Berechnung der Blitzschutz-Zone"""
    model_config = {"from_attributes": True}

    mast_height_above_water_m: float = Field(
        ...,
        description="Masthoehe ueber Wasserlinie (m)"
    )
    loa_m: float = Field(
        ...,
        description="Laenge ueber Alles (m)"
    )
    beam_m: float = Field(
        ...,
        description="Breite (m)"
    )
    protection_radius_m: float = Field(
        ...,
        description="Schutzradius am Wasserniveau (m) = Masthoehe x tan(30°)"
    )
    bow_protected: bool = Field(
        ...,
        description="Bug innerhalb Schutzzone"
    )
    stern_protected: bool = Field(
        ...,
        description="Heck innerhalb Schutzzone"
    )
    beam_protected: bool = Field(
        ...,
        description="Gesamte Breite innerhalb Schutzzone"
    )
    coverage_percent: float = Field(
        ...,
        ge=0,
        le=100,
        description="Prozent der Yacht-Flaeche innerhalb Schutzzone"
    )
    additional_air_terminals_needed: int = Field(
        0,
        description="Anzahl zusaetzlicher Air Terminals empfohlen"
    )
    assessment_de: str = Field(
        ...,
        description="Bewertung (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )


class LightningProtectionAssessment(BaseModel):
    """Gesamtbewertung des Blitzschutzes"""
    model_config = {"from_attributes": True}

    yacht_type: Literal["sailboat_alu_mast", "sailboat_carbon_mast", "sailboat_wood_mast", "motorboat", "catamaran"] = Field(
        ...,
        description="Yachttyp"
    )
    cruising_area: Optional[str] = Field(
        None,
        description="Fahrtgebiet"
    )
    lightning_risk: LightningRiskLevel = Field(
        ...,
        description="Blitzschlag-Risiko nach Region"
    )
    protection_status: LightningProtectionStatus = Field(
        ...,
        description="Schutzstatus"
    )

    # Air Terminal
    air_terminal_present: bool = Field(
        False,
        description="Fangeinrichtung (Air Terminal) vorhanden"
    )
    air_terminal_material: Optional[str] = Field(
        None,
        description="Material Air Terminal"
    )
    air_terminal_height_mm: Optional[float] = Field(
        None,
        description="Hoehe ueber Mastspitze (mm)"
    )

    # Down Conductor
    down_conductor_present: bool = Field(
        False,
        description="Ableiterkabel vorhanden"
    )
    down_conductor_gauge_awg: Optional[int] = Field(
        None,
        description="Querschnitt Ableiterkabel (AWG)"
    )
    down_conductor_gauge_mm2: Optional[float] = Field(
        None,
        description="Querschnitt Ableiterkabel (mm²)"
    )

    # Grounding
    grounding_plate_present: bool = Field(
        False,
        description="Erdungsplatte vorhanden"
    )
    grounding_plate_area_m2: Optional[float] = Field(
        None,
        description="Erdungsplatte Flaeche (m²)"
    )
    grounding_plate_type: Optional[str] = Field(
        None,
        description="Erdungsplatten-Typ (copper, bronze, dynaplate)"
    )

    # Bonding
    lightning_bonding_present: bool = Field(
        False,
        description="Blitz-Bonding vorhanden"
    )
    lightning_bonding_gauge_awg: Optional[int] = Field(
        None,
        description="Blitz-Bonding-Querschnitt (AWG)"
    )
    shrouds_bonded: bool = Field(
        False,
        description="Wanten geerdet"
    )

    # Surge Protection
    surge_protectors_installed: int = Field(
        0,
        description="Anzahl installierter Surge Protector"
    )
    surge_protector_locations: List[str] = Field(
        default_factory=list,
        description="Positionen der Surge Protector"
    )

    # Zone Calculation
    zone_calculation: Optional[LightningZoneCalculation] = Field(
        None,
        description="Schutzzonen-Berechnung"
    )

    # Assessment
    score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Blitzschutz-Score (0-100)"
    )
    findings_de: List[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )
    estimated_retrofit_cost_eur: Optional[float] = Field(
        None,
        description="Geschaetzte Nachruestkosten (EUR)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG M — Galvanischer Isolator / Trenntrafo Modelle

```python
"""
AYDI 22.10 — Shore Power Isolation Models
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum


class IsolationDeviceType(str, Enum):
    """Typ des Isolationsgeraets"""
    GALVANIC_ISOLATOR = "galvanic_isolator"
    ISOLATION_TRANSFORMER = "isolation_transformer"
    POLARIZATION_CELL = "polarization_cell"
    NONE = "none"


class IsolationDeviceAssessment(BaseModel):
    """Bewertung des Landstrom-Isolationssystems"""
    model_config = {"from_attributes": True}

    device_type: IsolationDeviceType = Field(
        ...,
        description="Typ des Isolationsgeraets"
    )
    manufacturer: Optional[str] = Field(
        None,
        description="Hersteller"
    )
    model: Optional[str] = Field(
        None,
        description="Modellbezeichnung"
    )
    rated_current_a: Optional[float] = Field(
        None,
        description="Nennstrom (A)"
    )
    shore_power_connection_a: Optional[float] = Field(
        None,
        description="Landanschluss-Sicherung (A)"
    )
    device_adequate_for_connection: Optional[bool] = Field(
        None,
        description="Geraet fuer Anschlussleistung ausreichend dimensioniert"
    )
    ul_1500_certified: Optional[bool] = Field(
        None,
        description="UL 1500 zertifiziert"
    )
    fail_safe_design: Optional[bool] = Field(
        None,
        description="Fail-Safe Design (PE bei Defekt durchverbunden)"
    )
    monitoring_present: Optional[bool] = Field(
        None,
        description="Status-Monitoring vorhanden (LED/Alarm)"
    )
    installation_correct: Optional[bool] = Field(
        None,
        description="Installation korrekt (im PE-Leiter, nach Hauptschalter)"
    )
    functional_test_passed: Optional[bool] = Field(
        None,
        description="Funktionstest bestanden"
    )
    age_years: Optional[float] = Field(
        None,
        description="Alter (Jahre)"
    )
    findings_de: List[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)"
    )
    score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Isolationsschutz-Score (0-100)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG N — Fehlererkennungs-Modelle (Visual Pipeline)

```python
"""
AYDI 22.10 — Visual Corrosion Detection Models (Pipeline B)
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum


class VisualCorrosionType(str, Enum):
    """Visuell erkennbare Korrosionstypen"""
    ANODE_DEPLETION = "anode_depletion"
    DEZINCIFICATION = "dezincification"
    PITTING = "pitting"
    UNIFORM_CORROSION = "uniform_corrosion"
    GALVANIC_AT_JUNCTION = "galvanic_at_junction"
    ANTIFOULING_BLISTERING = "antifouling_blistering"
    STAINLESS_RUST = "stainless_rust"
    ALUMINUM_WHITE_POWDER = "aluminum_white_powder"
    LIGHTNING_DAMAGE = "lightning_damage"
    BONDING_CABLE_CORROSION = "bonding_cable_corrosion"
    CARBON_METAL_JUNCTION = "carbon_metal_junction"


class VisualCorrosionFinding(BaseModel):
    """Einzelner visueller Korrosionsbefund"""
    model_config = {"from_attributes": True}

    corrosion_type: VisualCorrosionType = Field(
        ...,
        description="Erkannter Korrosionstyp"
    )
    location_de: str = Field(
        ...,
        description="Fundort (deutsch)"
    )
    description_de: str = Field(
        ...,
        description="Beschreibung des Befunds (deutsch)"
    )
    severity: Literal["none", "mild", "moderate", "severe", "critical"] = Field(
        ...,
        description="Schwere"
    )
    visual_indicators_de: List[str] = Field(
        default_factory=list,
        description="Visuelle Indikatoren (deutsch)"
    )
    differential_diagnosis_de: List[str] = Field(
        default_factory=list,
        description="Differentialdiagnosen (deutsch)"
    )
    recommended_action_de: str = Field(
        ...,
        description="Empfohlene Massnahme (deutsch)"
    )
    urgency: Literal["immediate", "next_haulout", "routine", "monitor"] = Field(
        ...,
        description="Dringlichkeit"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None,
        description="Geschaetzte Reparaturkosten (EUR)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level (visual_high/visual_medium/visual_low)"
    )


class VisualCorrosionReport(BaseModel):
    """Visueller Korrosionsbericht (Gesamtbild)"""
    model_config = {"from_attributes": True}

    image_count: int = Field(
        ...,
        description="Anzahl analysierter Bilder"
    )
    findings: List[VisualCorrosionFinding] = Field(
        default_factory=list,
        description="Einzelbefunde"
    )
    overall_corrosion_severity: Literal["none", "mild", "moderate", "severe", "critical"] = Field(
        ...,
        description="Gesamtschwere aller Korrosionsbefunde"
    )
    anode_system_assessment_de: str = Field(
        ...,
        description="Bewertung des Anodensystems (deutsch)"
    )
    bonding_visual_assessment_de: str = Field(
        ...,
        description="Visuelle Bewertung Bonding-Kabel/-Anschluesse (deutsch)"
    )
    summary_de: str = Field(
        ...,
        description="Zusammenfassung (deutsch)"
    )
    priority_actions_de: List[str] = Field(
        default_factory=list,
        description="Prioritaere Massnahmen (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG O — Service-Report-Modelle (Text Pipeline)

```python
"""
AYDI 22.10 — Service Report Analysis Models (Pipeline C)
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import date


class CorrosionServiceEntry(BaseModel):
    """Einzelner Korrosions-Service-Eintrag aus Text-Analyse"""
    model_config = {"from_attributes": True}

    report_date: Optional[str] = Field(
        None,
        description="Datum des Berichts (ISO 8601)"
    )
    source_type: Literal["surveyor_report", "yard_report", "owner_log", "insurance_report", "class_report"] = Field(
        ...,
        description="Quellentyp"
    )
    finding_de: str = Field(
        ...,
        description="Extrahierter Befund (deutsch)"
    )
    component_affected: str = Field(
        ...,
        description="Betroffene Komponente"
    )
    corrosion_type_detected: Optional[str] = Field(
        None,
        description="Erkannter Korrosionstyp"
    )
    severity_from_text: Optional[str] = Field(
        None,
        description="Im Text genannte Schwere"
    )
    measurements_extracted: Optional[dict] = Field(
        None,
        description="Extrahierte Messwerte (z.B. Potenzial, Wanddicke)"
    )
    action_taken_de: Optional[str] = Field(
        None,
        description="Durchgefuehrte Massnahme (deutsch)"
    )
    action_recommended_de: Optional[str] = Field(
        None,
        description="Empfohlene Massnahme (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level (documented)"
    )


class CorrosionHistoryAnalysis(BaseModel):
    """Analyse der Korrosionshistorie aus mehreren Service-Berichten"""
    model_config = {"from_attributes": True}

    entries: List[CorrosionServiceEntry] = Field(
        default_factory=list,
        description="Einzelne Service-Eintraege"
    )
    pattern_detected_de: Optional[str] = Field(
        None,
        description="Erkanntes Muster (deutsch), z.B. 'Wiederkehrender Anodenverbrauch alle 6 Monate'"
    )
    trend_de: Optional[str] = Field(
        None,
        description="Trend (deutsch), z.B. 'Verschlechterung', 'Stabil', 'Verbesserung'"
    )
    root_cause_hypothesis_de: Optional[str] = Field(
        None,
        description="Hypothese zur Grundursache (deutsch)"
    )
    recommendations_de: List[str] = Field(
        default_factory=list,
        description="Empfehlungen basierend auf Historienanalyse (deutsch)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level"
    )
```

### ANHANG P — Produkt-Modelle

```python
"""
AYDI 22.10 — Product Database Models
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal


class SacrificialAnodeProduct(BaseModel):
    """Opferanoden-Produktdatenbank"""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller"
    )
    model: str = Field(
        ...,
        description="Modellbezeichnung"
    )
    anode_material: Literal["zinc", "aluminum", "magnesium"] = Field(
        ...,
        description="Anodenmaterial"
    )
    application: str = Field(
        ...,
        description="Anwendungstyp: hull, shaft, saildrive, rudder, trim_tab, engine"
    )
    weight_kg: float = Field(
        ...,
        description="Gewicht (kg)"
    )
    capacity_ah: Optional[float] = Field(
        None,
        description="Elektrische Kapazitaet (Ah)"
    )
    dimensions_mm: str = Field(
        ...,
        description="Abmessungen (mm)"
    )
    mounting_type: str = Field(
        ...,
        description="Befestigungsart: bolt_on, clamp, clip, weld"
    )
    bolt_size: Optional[str] = Field(
        None,
        description="Bolzengroesse, z.B. 'M8'"
    )
    shaft_diameter_range_mm: Optional[str] = Field(
        None,
        description="Wellendurchmesser-Bereich (mm), z.B. '25-30'"
    )
    engine_compatibility: Optional[List[str]] = Field(
        None,
        description="Kompatible Motoren/Antriebe"
    )
    mil_spec: Optional[str] = Field(
        None,
        description="MIL-Spec (z.B. 'MIL-A-18001K')"
    )
    water_type: List[str] = Field(
        ...,
        description="Geeignete Wassertypen"
    )
    price_eur_min: Optional[float] = Field(
        None,
        description="Preis min. (EUR)"
    )
    price_eur_max: Optional[float] = Field(
        None,
        description="Preis max. (EUR)"
    )
    availability_regions: List[str] = Field(
        default_factory=list,
        description="Verfuegbare Regionen"
    )
    confidence: str = Field(
        default="documented",
        description="AYDI Confidence Level"
    )


class GalvanicIsolatorProduct(BaseModel):
    """Galvanischer Isolator Produktdatenbank"""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    rated_current_a: float = Field(..., description="Nennstrom (A)")
    rated_voltage_v: str = Field(..., description="Nennspannung")
    blocking_voltage_v: float = Field(..., description="Blockierspannung (V DC)")
    fail_safe: bool = Field(..., description="Fail-Safe Design")
    monitoring: str = Field(..., description="Monitoring-Typ (LED, Alarm, Display)")
    ul_1500: bool = Field(..., description="UL 1500 zertifiziert")
    ip_rating: Optional[str] = Field(None, description="Schutzart (IP-Rating)")
    price_eur_min: Optional[float] = Field(None, description="Preis min. (EUR)")
    price_eur_max: Optional[float] = Field(None, description="Preis max. (EUR)")
    confidence: str = Field(default="documented", description="AYDI Confidence Level")


class IsolationTransformerProduct(BaseModel):
    """Trenntrafo Produktdatenbank"""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    power_kva: float = Field(..., description="Leistung (kVA)")
    input_voltage: str = Field(..., description="Eingangsspannung")
    output_voltage: str = Field(..., description="Ausgangsspannung")
    frequency: str = Field(..., description="Frequenz (Hz)")
    efficiency_percent: Optional[float] = Field(None, description="Effizienz (%)")
    weight_kg: float = Field(..., description="Gewicht (kg)")
    dimensions_mm: Optional[str] = Field(None, description="Abmessungen (mm)")
    core_type: Optional[str] = Field(None, description="Kerntyp (toroid, EI)")
    thermal_protection: bool = Field(False, description="Temperaturueberwachung")
    price_eur_min: Optional[float] = Field(None, description="Preis min. (EUR)")
    price_eur_max: Optional[float] = Field(None, description="Preis max. (EUR)")
    suitable_yacht_loa_min_m: Optional[float] = Field(None, description="Geeignet ab LOA (m)")
    suitable_yacht_loa_max_m: Optional[float] = Field(None, description="Geeignet bis LOA (m)")
    confidence: str = Field(default="documented", description="AYDI Confidence Level")
```

### ANHANG Q — Gesamt-Korrosionsschutz-Bewertung

```python
"""
AYDI 22.10 — Overall Corrosion Protection Assessment
Kombiniert alle Einzelbewertungen zu einem Gesamt-Score
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class CorrosionProtectionOverallScore(BaseModel):
    """Gesamtbewertung des Korrosionsschutzes einer Yacht"""
    model_config = {"from_attributes": True}

    yacht_id: Optional[str] = Field(
        None,
        description="AYDI Yacht-ID"
    )
    assessment_date: str = Field(
        ...,
        description="Bewertungsdatum (ISO 8601)"
    )
    yacht_type: str = Field(
        ...,
        description="Yachttyp"
    )
    hull_material: str = Field(
        ...,
        description="Rumpfmaterial"
    )
    loa_m: float = Field(
        ...,
        description="LOA (m)"
    )
    home_port_region: Optional[str] = Field(
        None,
        description="Heimathafen-Region"
    )
    water_type: str = Field(
        ...,
        description="Wassertyp"
    )

    # Sub-Scores
    anode_system_score: float = Field(
        ..., ge=0, le=100,
        description="Anodensystem-Score (0-100)"
    )
    bonding_system_score: float = Field(
        ..., ge=0, le=100,
        description="Bonding-System-Score (0-100)"
    )
    shore_power_isolation_score: float = Field(
        ..., ge=0, le=100,
        description="Landstrom-Isolationsschutz-Score (0-100)"
    )
    lightning_protection_score: float = Field(
        ..., ge=0, le=100,
        description="Blitzschutz-Score (0-100)"
    )
    visual_condition_score: float = Field(
        ..., ge=0, le=100,
        description="Visueller Zustandsscore (0-100)"
    )
    documentation_score: float = Field(
        ..., ge=0, le=100,
        description="Dokumentations-Score (Wartungsprotokolle etc.)"
    )

    # Gewichteter Gesamt-Score
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gewichteter Gesamt-Score (0-100)"
    )
    score_weights: Dict[str, float] = Field(
        default_factory=lambda: {
            "anode_system": 0.30,
            "bonding_system": 0.20,
            "shore_power_isolation": 0.15,
            "lightning_protection": 0.15,
            "visual_condition": 0.10,
            "documentation": 0.10,
        },
        description="Gewichtungsfaktoren fuer Gesamt-Score"
    )

    # Rating
    rating: str = Field(
        ...,
        description="Gesamtrating: excellent/good/acceptable/poor/critical"
    )

    # Zusammenfassung
    summary_de: str = Field(
        ...,
        description="Zusammenfassung der Gesamtbewertung (deutsch)"
    )
    critical_findings_de: List[str] = Field(
        default_factory=list,
        description="Kritische Befunde (deutsch)"
    )
    priority_recommendations_de: List[str] = Field(
        default_factory=list,
        description="Prioritaere Empfehlungen (deutsch)"
    )
    estimated_total_cost_eur: Optional[float] = Field(
        None,
        description="Geschaetzte Gesamtkosten aller Massnahmen (EUR)"
    )
    next_inspection_recommended: Optional[str] = Field(
        None,
        description="Empfohlenes Datum naechste Inspektion (ISO 8601)"
    )
    confidence: str = Field(
        ...,
        description="AYDI Confidence Level (niedrigstes aller Sub-Bewertungen)"
    )
```

### ANHANG R — Hilfs-Modelle und Berechnungen

```python
"""
AYDI 22.10 — Utility Models and Calculations
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
import math


class GalvanicSpannungsreiheEntry(BaseModel):
    """Eintrag in der galvanischen Spannungsreihe"""
    model_config = {"from_attributes": True}

    material_de: str = Field(..., description="Material (deutsch)")
    material_en: str = Field(..., description="Material (englisch)")
    potential_min_mv: float = Field(..., description="Min. Potenzial (mV vs. Ag/AgCl)")
    potential_max_mv: float = Field(..., description="Max. Potenzial (mV vs. Ag/AgCl)")
    potential_typical_mv: float = Field(..., description="Typisches Potenzial (mV vs. Ag/AgCl)")
    classification: Literal["strongly_anodic", "anodic", "slightly_anodic", "neutral", "slightly_cathodic", "cathodic", "strongly_cathodic", "extremely_cathodic"] = Field(
        ..., description="Klassifikation in der Spannungsreihe"
    )
    yacht_applications_de: List[str] = Field(
        default_factory=list,
        description="Typische Yacht-Anwendungen (deutsch)"
    )


class AnodeDimensioningCalculation(BaseModel):
    """Anodenberechnung"""
    model_config = {"from_attributes": True}

    # Eingabeparameter
    anode_material: Literal["zinc", "aluminum", "magnesium"] = Field(
        ..., description="Anodenmaterial"
    )
    protected_area_m2: float = Field(
        ..., description="Zu schuetzende Metallflaeche (m²)"
    )
    current_density_ma_m2: float = Field(
        ..., description="Angenommene Stromdichte (mA/m²)"
    )
    design_life_months: int = Field(
        ..., description="Geplante Schutzdauer (Monate)"
    )
    utilization_factor: float = Field(
        0.85,
        ge=0.5, le=1.0,
        description="Auslastungsfaktor (0.5–1.0)"
    )

    # Berechnete Ergebnisse
    required_current_ma: float = Field(
        ..., description="Erforderlicher Schutzstrom (mA)"
    )
    required_capacity_ah: float = Field(
        ..., description="Erforderliche Kapazitaet (Ah)"
    )
    anode_capacity_ah_per_kg: float = Field(
        ..., description="Anodenkapazitaet (Ah/kg)"
    )
    required_anode_weight_kg: float = Field(
        ..., description="Erforderliches Anodengewicht (kg)"
    )
    safety_factor: float = Field(
        1.5,
        description="Sicherheitsfaktor"
    )
    recommended_total_weight_kg: float = Field(
        ..., description="Empfohlenes Gesamtgewicht inkl. Sicherheitsfaktor (kg)"
    )
    recommended_anode_count: int = Field(
        ..., description="Empfohlene Anodenanzahl"
    )
    recommended_anode_model: Optional[str] = Field(
        None, description="Empfohlenes Anodenmodell"
    )
    calculation_notes_de: List[str] = Field(
        default_factory=list,
        description="Berechnungshinweise (deutsch)"
    )
    confidence: str = Field(
        ..., description="AYDI Confidence Level"
    )


class LightningProtectionRadiusCalculation(BaseModel):
    """Blitzschutz-Radius-Berechnung"""
    model_config = {"from_attributes": True}

    mast_height_m: float = Field(
        ..., description="Masthoehe ueber Wasserlinie (m)"
    )
    cone_angle_deg: float = Field(
        60.0,
        description="Kegelwinkel (Grad), Standard 60°"
    )

    # Berechnete Werte
    protection_radius_m: float = Field(
        ..., description="Schutzradius am Wasserniveau (m)"
    )
    yacht_loa_m: Optional[float] = Field(
        None, description="LOA der Yacht (m)"
    )
    yacht_beam_m: Optional[float] = Field(
        None, description="Breite der Yacht (m)"
    )
    mast_position_from_bow_m: Optional[float] = Field(
        None, description="Mastposition vom Bug (m)"
    )
    bow_clearance_m: Optional[float] = Field(
        None, description="Schutzabstand am Bug (m, positiv = geschuetzt)"
    )
    stern_clearance_m: Optional[float] = Field(
        None, description="Schutzabstand am Heck (m, positiv = geschuetzt)"
    )
    fully_protected: bool = Field(
        ..., description="Gesamte Yacht innerhalb Schutzzone"
    )
    assessment_de: str = Field(
        ..., description="Bewertung (deutsch)"
    )
    confidence: str = Field(
        ..., description="AYDI Confidence Level"
    )

    @field_validator("protection_radius_m", mode="before")
    @classmethod
    def calculate_radius(cls, v, info):
        """Calculate protection radius if not provided"""
        if v is not None:
            return v
        values = info.data
        if "mast_height_m" in values and "cone_angle_deg" in values:
            half_angle = values["cone_angle_deg"] / 2
            return values["mast_height_m"] * math.tan(math.radians(half_angle))
        return v


class CorrosionRiskMatrix(BaseModel):
    """Korrosions-Risikomatrix fuer eine Yacht"""
    model_config = {"from_attributes": True}

    yacht_id: Optional[str] = Field(None, description="AYDI Yacht-ID")
    material_pairs: List[Dict] = Field(
        default_factory=list,
        description="Liste aller Materialpaarungen mit Risikobewertung"
    )
    highest_risk_pair_de: str = Field(
        ..., description="Hoechstes Risiko Materialpaarung (deutsch)"
    )
    stray_current_risk: Literal["low", "moderate", "high", "critical"] = Field(
        ..., description="Streustrom-Risiko"
    )
    environmental_risk: Literal["low", "moderate", "high", "critical"] = Field(
        ..., description="Umgebungs-Risiko (Wassertemperatur, Salzgehalt)"
    )
    protection_adequacy: Literal["excellent", "good", "marginal", "insufficient"] = Field(
        ..., description="Angemessenheit des Schutzes"
    )
    overall_corrosion_risk: Literal["low", "moderate", "high", "critical"] = Field(
        ..., description="Gesamt-Korrosionsrisiko"
    )
    recommendations_de: List[str] = Field(
        default_factory=list, description="Empfehlungen (deutsch)"
    )
    confidence: str = Field(..., description="AYDI Confidence Level")


# ──────────────────────────────────────────────
# Import Dict for type hint
# ──────────────────────────────────────────────
from typing import Dict
```

---

> **Ende der AYDI-Wissensdatei 22.10**
> **Zeilen:** ~3.800 | **Abschnitte:** 12 Hauptabschnitte + 18 Anhaenge
> **Naechste Aktualisierung:** Bei Aenderung relevanter Normen (ISO 20313, ABYC E-2/E-11/TE-4) oder neuen Produkten
