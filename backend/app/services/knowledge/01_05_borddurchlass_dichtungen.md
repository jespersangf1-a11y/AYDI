# 01.05 — Borddurchlass-Dichtungen: Kompletthandbuch

> **Modulkontext**: materials, structural, compliance, service_patterns
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-03

---

## Inhaltsverzeichnis

1. Grundlagen und Definitionen
2. Normen und Regularien
3. Materialien für Borddurchlässe
4. Dichtungsmaterialien (O-Ringe, Flachdichtungen)
5. Dichtmassen (Sikaflex, 3M, Soudal)
6. Hersteller-Kataloge — Borddurchlässe
7. Hersteller-Kataloge — Seeventile
8. Gewindespezifikationen (BSP, NPT, Metrisch)
9. Einbau-Anleitung Skin-Fitting
10. Einbau-Anleitung Seeventil-Montage
11. Übergang Seeventil→Schlauch
12. Schlauchschellen-Spezifikationen
13. Materialkompatibilität und Galvanik
14. Fehlerbilder und Diagnostik
15. Schadensfälle / Fallstudien
16. OEM-Spezifikationen nach Bootshersteller
17. Weltweite Bezugsquellen
18. Preisvergleich
19. Lebensdauer und Wartungsintervalle
20. DIY-Reparatur- und Austausch-Anleitungen
21. Versicherung und Survey-Anforderungen
22. Notfall-Maßnahmen
23. Forum-Erfahrungsberichte
24. YouTube-Ressourcen
25. Experten-Referenzen
26. FAQ
27. Glossar
28. Anhänge A–AZ

---

## 1. Grundlagen und Definitionen

### 1.1 Was ist ein Borddurchlass?

Ein Borddurchlass (engl. thru-hull fitting, skin fitting) ist jede Durchführung durch den Rumpf unterhalb oder nahe der Wasserlinie. Die Abdichtung dieses Durchlasses ist die kritischste Dichtungsaufgabe an jedem Boot — ein Versagen führt direkt zu Wassereinbruch und potenziell zum Sinken.

(Confidence: documented)

### 1.2 Systemkomponenten

| Komponente | Englisch | Funktion |
|---|---|---|
| Skin-Fitting | Thru-hull fitting | Durchführung durch den Rumpf |
| Seeventil | Seacock | Absperrventil direkt am Rumpf |
| Mutter/Gegenmutter | Lock nut | Befestigung von innen |
| Backing-Block | Backing plate/block | Lastverteilung auf Rumpflaminat |
| O-Ring | O-ring | Dichtung zwischen Fitting und Ventil |
| Flachdichtung | Flat gasket | Alternative Dichtung |
| Dichtmasse | Sealant | Abdichtung Fitting↔Rumpf |
| Schlauchschelle | Hose clamp/jubilee clip | Schlauch-Befestigung am Seeventil |

(Confidence: documented)

### 1.3 Durchlass-Typen

| Typ | Beschreibung | Einsatz |
|---|---|---|
| Pilzförmig (Mushroom) | Breiter Flansch außen, Gewinde durch Rumpf | Standard unter Wasserlinie |
| Flansch (Flanged) | Beide Seiten mit Flansch | Heavy-duty, Superyachten |
| Flush-Mount | Bündig mit Rumpfaußenseite | Racing, Superyachten |
| Scoop (Einlass) | Mit Schaufel für Wassereinlass | Kühlwasser, Toilettenspülung |
| Ablass (Drain) | Konisches Gewinde, selbstdichtend | Cockpit-Drain, Waschbecken |

(Confidence: documented)

### 1.4 Kritische Dichtungszonen am Borddurchlass

```
Zone 1: Skin-Fitting ↔ Rumpf (Dichtmasse)
Zone 2: Skin-Fitting ↔ Seeventil (O-Ring oder Flachdichtung)
Zone 3: Seeventil ↔ Schlauch (Schlauchschelle — KEIN Dichtstoff!)
Zone 4: Skin-Fitting ↔ Backing-Block (Dichtmasse)
Zone 5: Backing-Block ↔ Rumpf-Innenseite (Dichtmasse)
```

(Confidence: documented)

### 1.5 Wassereintrittspfade — Häufigkeitsranking

| Rang | Undichtigkeit | Häufigkeit | Ursache |
|---|---|---|---|
| 1 | Dichtmasse Skin-Fitting↔Rumpf versagt | 35% | Falsches Produkt, Alterung, Bewegung |
| 2 | O-Ring Skin-Fitting↔Seeventil defekt | 25% | Material-Inkompatibilität, Alterung |
| 3 | Korrosion am Fitting selbst | 20% | Galvanische Korrosion, Dezinkifizierung |
| 4 | Schlauchschelle locker/korrodiert | 12% | Unterdimensioniert, falsches Material |
| 5 | Riss im Rumpflaminat um Durchlass | 8% | Fehlender Backing-Block, Stoß |

(Confidence: documented — Steve D'Antonio, Marine Surveyor Reports)

---

## 2. Normen und Regularien

### 2.1 ISO 9093 — Borddurchlässe und Seeventile

| Teil | Titel | Geltungsbereich |
|---|---|---|
| ISO 9093-1:2020 | Metallische Borddurchlässe | Bronze, Edelstahl, Messing |
| ISO 9093-2:2020 | Nicht-metallische Borddurchlässe | Kunststoff, Composite |

**Wesentliche Anforderungen:**

| Parameter | Anforderung | Prüfung |
|---|---|---|
| Strukturelle Belastung | ≥227 kg (500 lbs) Axiallast | Zugversuch |
| Vibrationsbeständigkeit | 1 Mio. Zyklen ohne Leckage | Vibrationstest |
| Korrosionsbeständigkeit | 30 Tage Salzsprühtest (ASTM B117) | Keine Funktionseinschränkung |
| Frostbeständigkeit | –20°C ohne Rissbildung | Kältetest |
| UV-Beständigkeit (Composite) | 2.000 Stunden UV-Exposition | Kein signifikanter Festigkeitsverlust |
| Druckfestigkeit | 0,5 bar Innendruck, 5 min | Keine Leckage |

(Confidence: measured — ISO 9093:2020)

### 2.2 ABYC H-27 — Seacocks and Thru-Hull Fittings

| Anforderung | Detail |
|---|---|
| Seeventil-Pflicht | Jeder Borddurchlass ≤150mm über Wasserlinie muss Seeventil haben |
| Material | Seewasserbeständige Bronze, Composite oder Edelstahl 316L |
| Messing verboten | Messing (Brass) ist NICHT zulässig — Dezinkifizierungsrisiko |
| Absperren möglich | Jedes Seeventil muss mit einem Handgriff absperrbar sein |
| Kennzeichnung | Jeder Durchlass muss zugänglich und klar gekennzeichnet sein |
| Doppelte Schlauchschellen | Unterhalb Wasserlinie: Doppelschelle Pflicht |
| Backing-Block | Strukturelle Lastverteilung bei unter 12mm Rumpfstärke |

(Confidence: measured — ABYC H-27)

### 2.3 CE-Anforderungen (EU Recreational Craft Directive 2013/53/EU)

| Kategorie | Relevante ISO-Norm | Borddurchlass-Implikation |
|---|---|---|
| A (Ozean) | ISO 9093, ISO 12217 | Höchste Materialanforderungen, redundante Absperrmöglichkeiten |
| B (Offshore) | ISO 9093, ISO 12217 | Standard-Anforderungen |
| C (Küstennah) | ISO 9093 | Standard-Anforderungen |
| D (Geschützt) | ISO 9093 | Vereinfachte Anforderungen möglich |

(Confidence: measured — EU RCD 2013/53/EU)

### 2.4 Klassifikationsgesellschaften

| Gesellschaft | Regelwerk | Besonderheiten |
|---|---|---|
| Lloyd's Register | Rules for Classification of Yachts & Small Craft | Mindestens Bronze UNI EN 1982 CC491K |
| Bureau Veritas | NR500, NR217 | Jährliche Inspektion aller Unterwasser-Durchlässe |
| DNV-GL | Rules for Classification of Yachts | Material-Zertifikat für jeden Durchlass |
| RINA | Rules for Classification of Yachts | Farbcodierung: Rot = Notabsperrung |
| ABS | Guide for Building and Classing Yachts | Mindestwandstärke nach Durchmesser |

(Confidence: documented)

### 2.5 ABYC vs. ISO Vergleich

| Kriterium | ABYC H-27 | ISO 9093 |
|---|---|---|
| Seeventil-Pflicht | ≤150mm über WL | ≤300mm über WL |
| Messing erlaubt? | Nein | Nein (seit 2020) |
| Strukturelle Last | 500 lbs (227 kg) | 500 lbs (227 kg) |
| Schlauchschellen | Doppelt unter WL | Doppelt unter WL |
| Backing-Block | Empfohlen | Pflicht bei <12mm Laminat |

(Confidence: measured)

---

## 3. Materialien für Borddurchlässe

### 3.1 Bronze (Rotguss / Gunmetal)

**Legierungen im Marineeinsatz:**

| Legierung | UNS | Zusammensetzung | Eigenschaften |
|---|---|---|---|
| C83600 (Ounce Metal) | C83600 | 85Cu-5Sn-5Pb-5Zn | Standard-Marinebronze, gute Gießbarkeit |
| C84400 (Naval Bronze) | C84400 | 81Cu-3Sn-7Pb-9Zn | Höherer Zinkanteil — Dezinkifizierungsrisiko! |
| C95200 (Aluminiumbronze) | C95200 | 88Cu-3Fe-9Al | Höchste Festigkeit, exzellente Korrosionsbeständigkeit |
| C95800 (Nickel-Alu-Bronze/Nibral) | C95800 | 81Cu-4Fe-5Ni-9Al | Premium, Superyacht-Standard |
| CC491K (EN 1982) | — | 85Cu-5Sn-5Pb-5Zn | EU-Bezeichnung ≈ C83600 |
| DZR-Messing | CZ132 | Cu-Zn + As/Sn | Entzinkungsbeständig, UK-Standard |

**Vor-/Nachteile Bronze:**

| Vorteil | Nachteil |
|---|---|
| Bewährt seit Jahrhunderten | Schwer (Gewichtsnachteil) |
| Gute Korrosionsbeständigkeit in Seewasser | Galvanische Probleme mit Edelstahl/Aluminium |
| Exzellente mechanische Festigkeit | Teurer als Kunststoff |
| Reparierbar (nachdrehen, nachschleifen) | Kann verkrusten (marine growth) |
| Antibiofouling-Eigenschaften (Kupfergehalt) | Dezinkifizierungsrisiko bei falscher Legierung |

(Confidence: measured — ASTM B505, EN 1982)

### 3.2 Edelstahl 316L

| Eigenschaft | Wert |
|---|---|
| Legierung | 316L (UNS S31603) |
| Zusammensetzung | Fe-17Cr-12Ni-2.5Mo-0.03C(max) |
| Zugfestigkeit | ≥485 MPa |
| Streckgrenze | ≥170 MPa |
| Korrosionsbeständigkeit | Gut, ABER Spaltkorrosion in sauerstoffarmem Seewasser! |
| PREN (Pitting Resistance) | 23–28 |

**WARNUNG**: Edelstahl 316L ist NICHT die erste Wahl für Unterwasser-Borddurchlässe. Spaltkorrosion (crevice corrosion) in sauerstoffarmem Wasser zwischen Fitting und Rumpf kann zu katastrophalem Versagen führen — ohne äußere Anzeichen.

(Confidence: documented — Steve D'Antonio, Practical Sailor)

### 3.3 Composite / Kunststoff

**Marelon (Forespar):**

| Eigenschaft | Wert |
|---|---|
| Material | Glasfaserverstärktes Nylon (GF-PA) |
| Zugfestigkeit | 110 MPa |
| Druckfestigkeit | 145 MPa |
| Max. Betriebstemperatur | 93°C (200°F) |
| UV-Beständigkeit | Gut (UV-Stabilisatoren) |
| Farbe | Weiß |
| Galvanische Korrosion | Keine (elektrisch inert) |
| Max. Anzugsdrehmoment | 27 Nm (20 ft-lbs) — KRITISCH! |

**TruDesign (Neuseeland):**

| Eigenschaft | Wert |
|---|---|
| Material | Glasfaserverstärktes Polypropylen (GF-PP) |
| Zugfestigkeit | 90 MPa |
| Max. Betriebstemperatur | 82°C (180°F) |
| UV-Beständigkeit | Sehr gut |
| Farbe | Weiß |
| Galvanische Korrosion | Keine |
| Max. Anzugsdrehmoment | 27 Nm (20 ft-lbs) |
| Besonderheit | Modulares System — Fitting + Ventil + Schlauchstutzen |

(Confidence: measured — Hersteller-TDS)

### 3.4 Materialvergleich Borddurchlass

| Kriterium | Bronze C83600 | Edelstahl 316L | Marelon | TruDesign |
|---|---|---|---|---|
| Korrosion Seewasser | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★★★ |
| Galvanik-Risiko | ★★★☆☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ |
| Festigkeit | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| Gewicht | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ |
| Lebensdauer | 30–50 Jahre | 15–25 Jahre | 15–25 Jahre | 15–25 Jahre |
| Preis (1" Fitting) | €35–80 | €40–90 | €15–35 | €20–40 |
| Alu-Rumpf geeignet? | NEIN (galvanisch!) | Bedingt (isoliert) | JA | JA |
| GFK-Rumpf geeignet? | JA | JA (mit Vorsicht) | JA | JA |
| Antibiofouling | JA (Kupfer) | NEIN | NEIN | NEIN |

(Confidence: documented — Practical Sailor Comparative Test 2019)

---

## 4. Dichtungsmaterialien — O-Ringe und Flachdichtungen

### 4.1 O-Ring-Materialien

| Material | Code | Temperaturbereich | Shore A | Seewasser | Diesel/Öl | UV | Empfehlung |
|---|---|---|---|---|---|---|---|
| NBR (Nitril) | — | –30°C bis +100°C | 70±5 | Gut | Sehr gut | Mäßig | Standard für Kraftstoff/Öl |
| EPDM | — | –40°C bis +130°C | 70±5 | Sehr gut | Schlecht | Sehr gut | Standard für Seewasser |
| FKM/Viton | — | –20°C bis +200°C | 75±5 | Sehr gut | Sehr gut | Sehr gut | Premium, universell |
| Silikon (VMQ) | — | –60°C bis +230°C | 60±5 | Gut | Mäßig | Sehr gut | Hochtemperatur |
| PTFE | — | –200°C bis +260°C | N/A (hart) | Excellent | Excellent | Excellent | Flachdichtungen, Chemie |

(Confidence: measured — Parker O-Ring Handbook)

### 4.2 O-Ring-Empfehlung nach Einsatzort

| Einsatzort | Material-Empfehlung | Begründung |
|---|---|---|
| Seewasser-Einlass (Kühlung) | EPDM oder FKM | Seewasserbeständig, keine Kraftstoffexposition |
| Diesel-Durchlass | NBR oder FKM | Kraftstoffbeständig! EPDM quillt! |
| Abwasser/Fäkalien | FKM/Viton | Chemikalienbeständig, Geruchsdicht |
| Abgas (Nass-Auspuff) | FKM/Viton oder Silikon | Temperaturbeständig + seewasserfest |
| Wäscheschacht/Decksdurchführung | EPDM | Kostengünstig, UV-beständig |

(Confidence: documented — Parker, Trelleborg Sealing Solutions)

### 4.3 O-Ring-Größen nach Gewindedurchmesser

**BSP-Gewinde (British Standard Pipe — EU/UK/AUS Standard):**

| Gewindegröße | Fitting-OD (mm) | O-Ring ID (mm) | O-Ring CS (mm) | AS-568 Äquivalent | Parker Nr. |
|---|---|---|---|---|---|
| 3/4" BSP | 26,44 | 23,0 | 3,0 | 2-119 | 2-119-N674-70 |
| 1" BSP | 33,25 | 29,5 | 3,5 | 2-126 | 2-126-N674-70 |
| 1-1/4" BSP | 41,91 | 37,5 | 3,5 | 2-131 | 2-131-N674-70 |
| 1-1/2" BSP | 47,80 | 43,5 | 3,5 | 2-135 | 2-135-N674-70 |
| 2" BSP | 59,61 | 55,0 | 4,0 | 2-143 | 2-143-N674-70 |
| 2-1/2" BSP | 75,18 | 70,0 | 4,0 | 2-151 | 2-151-N674-70 |

**NPT-Gewinde (National Pipe Thread — USA Standard):**

| Gewindegröße | Fitting-OD (mm) | O-Ring ID (mm) | O-Ring CS (mm) | AS-568 Nr. |
|---|---|---|---|---|
| 3/4" NPT | 26,67 | 23,0 | 3,0 | 2-119 |
| 1" NPT | 33,40 | 29,5 | 3,5 | 2-126 |
| 1-1/4" NPT | 42,16 | 37,5 | 3,5 | 2-131 |
| 1-1/2" NPT | 48,26 | 43,5 | 3,5 | 2-135 |
| 2" NPT | 60,33 | 55,0 | 4,0 | 2-143 |

(Confidence: measured — AS-568 / ISO 3601)

### 4.4 O-Ring-Lieferanten

| Lieferant | Land | Sortiment | Mindestbestellung | Website |
|---|---|---|---|---|
| Parker Hannifin | USA/DE | Komplett (alle Materialien) | 1 Stk | parker.com |
| Trelleborg Sealing | SE/DE | Premium Marine | 10 Stk | trelleborg.com |
| Freudenberg/Simrit | DE | Industrie + Marine | 10 Stk | fst.com |
| Dichtomatik | DE | Alle Größen ab Lager | 1 Stk | dichtomatik.de |
| Apple Rubber | USA | Custom + Standard | 1 Stk | applerubber.com |
| Eriks | NL/UK | Industrie, großes Lager | 5 Stk | eriks.com |
| Polymax | UK | Marine-Fokus, Online-Shop | 1 Stk | polymax.co.uk |
| Marco Rubber | USA | Alle AS-568 Größen | 1 Stk | marcorubber.com |
| ORing.de | DE | Online-Konfigurator | 1 Stk | oring.de |
| Hennlich | DE/AT/CZ | Industrie + Spezialdichtungen | 5 Stk | hennlich.de |

(Confidence: documented)

### 4.5 Flachdichtungen

| Material | Dicke (mm) | Max. Temp. | Seewasser | Einsatz |
|---|---|---|---|---|
| Gummi (NBR) | 1,5 / 2,0 / 3,0 | +80°C | Gut | Standard-Flanschdichtung |
| PTFE (Teflon) | 1,5 / 2,0 / 3,0 | +260°C | Exzellent | Universell, chemisch inert |
| Klingersil (Faserdichtung) | 1,0 / 1,5 / 2,0 | +200°C | Sehr gut | Hochtemperatur (Auspuff) |
| Neoprene (CR) | 1,5 / 2,0 / 3,0 | +90°C | Sehr gut | Seewasser, Ölbeständig |
| EPDM-Folie | 1,0 / 2,0 / 3,0 | +130°C | Sehr gut | Trinkwasser, Seewasser |

(Confidence: documented)

### 4.6 Flachdichtungen — Dimensionen nach Flanschgröße

| Fitting-Größe | Flansch-AD (mm) | Dichtung-AD (mm) | Dichtung-ID (mm) | Dicke (mm) | Lochkreis (mm) | Bolzenanzahl |
|---|---|---|---|---|---|---|
| 3/4" | 50 | 48 | 28 | 2,0 | 38 | 4 |
| 1" | 55 | 53 | 35 | 2,0 | 42 | 4 |
| 1-1/4" | 65 | 63 | 43 | 2,0 | 52 | 4 |
| 1-1/2" | 75 | 73 | 50 | 3,0 | 60 | 4 |
| 2" | 90 | 88 | 62 | 3,0 | 72 | 4 oder 8 |
| 2-1/2" | 105 | 103 | 78 | 3,0 | 88 | 8 |
| 3" | 120 | 118 | 90 | 3,0 | 100 | 8 |

(Confidence: measured — Groco, Perko Flansch-Spezifikationen)

### 4.7 Spezial: TruDesign-Dichtungssystem

TruDesign verwendet ein proprietäres Dichtungssystem:

| Komponente | TruDesign-Teil | Material | Funktion |
|---|---|---|---|
| Innere O-Ring-Dichtung | 90316 (3/4"), 90317 (1"), 90318 (1-1/4"), 90319 (1-1/2"), 90320 (2") | EPDM | Fitting↔Seeventil |
| Außen-Flachdichtung | 90321 (3/4"), 90322 (1"), 90323 (1-1/4"), 90324 (1-1/2"), 90325 (2") | EPDM | Flansch↔Rumpf |
| Lock-Nut-Dichtring | 90326 (alle Größen) | EPDM | Mutter↔Rumpf innen |

(Confidence: measured — TruDesign Parts Catalogue 2024)

---

## 5. Dichtmassen — Abdichtung Skin-Fitting↔Rumpf

### 5.1 Übersicht empfohlene Dichtmassen

| Produkt | Typ | Aushärtung | Shore A | Dehnung | Seewasser | Empfehlung |
|---|---|---|---|---|---|---|
| Sikaflex 291 | PU (1K) | 7 Tage / 23°C | 40 | 600% | Exzellent | **Standard-Empfehlung Borddurchlass** |
| Sikaflex 291i | PU (1K) | 7 Tage / 23°C | 40 | 600% | Exzellent | EU-Version von 291 (isocyanatfrei) |
| Sikaflex 292i | PU (1K, struktur.) | 7 Tage / 23°C | 55 | 300% | Exzellent | Für strukturelle Verklebung |
| 3M 5200 | PU (1K) | 7 Tage / 23°C | 55 | 400% | Exzellent | **WARNUNG: Permanente Verklebung!** |
| 3M 4200 | PU (1K) | 5 Tage / 23°C | 40 | 500% | Exzellent | Demontierbar — gute Alternative |
| Soudal Fix All HT | SMP (1K) | 4 Tage / 23°C | 40 | 500% | Sehr gut | Budget-Alternative |
| BoatLIFE Life Seal | Polysulfid | 7 Tage / 23°C | 30 | 500% | Exzellent | US-Klassiker |
| BoatLIFE Life Calk | Polysulfid | 7 Tage / 23°C | 25 | 700% | Exzellent | Sehr elastisch |

(Confidence: measured — Hersteller-TDS)

### 5.2 KRITISCH: Was NICHT verwenden

| Produkt | Warum NICHT |
|---|---|
| **Silikon** (alle Typen) | Haftet nicht dauerhaft auf GFK! Kriecht unter Belastung. Keine strukturelle Festigkeit. |
| **Acryl-Dichtmasse** | Nicht seewasserbeständig. Schrumpft beim Aushärten. |
| **3M 5200 am Borddurchlass** | Zu stark verklebt — Fitting kann nicht demontiert werden! Bronze wird beim Entfernen beschädigt. |
| **Butyl-Band** | Nicht druckbeständig unter Wasser. Nur für Deckshardware über Wasser. |
| **Gewindedichtband (PTFE-Tape)** | NICHT an Borddurchlässen! Nur für Rohrleitungen. Kann sich lösen und Ventil blockieren. |

(Confidence: documented — Steve D'Antonio, Nigel Calder, Forum-Konsens)

### 5.3 Dichtmasse-Anwendung Schritt für Schritt

**Vorbereitung:**

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | Altes Dichtmittel vollständig entfernen | Kunststoffspachtel, Schaber |
| 2 | Oberflächen anschleifen (P80–P120) | Schleifpapier |
| 3 | Entfetten mit Aceton oder Sika Aktivator 205 | Lappen, Aceton |
| 4 | Primer auftragen (Sika Primer 209D auf GFK) | Pinsel |
| 5 | 30 min ablüften lassen | — |
| 6 | Dichtmasse auftragen — durchgehende Raupe | Kartuschenpistole |
| 7 | Fitting einsetzen, handfest anziehen | Handkraft |
| 8 | Überschuss entfernen (Spülmittel-Wasser) | Finger mit Spüli |
| 9 | 7 Tage aushärten vor Wasserkontakt | — |

(Confidence: documented — Sika Marine Guide)

### 5.4 Sika-Primer-Zuordnung

| Untergrund | Primer | Trockenzeit |
|---|---|---|
| GFK (Gelcoat) | Sika Primer 209D | 30 min |
| GFK (geschliffen, kein Gelcoat) | Sika Aktivator 205 | 15 min |
| Aluminium | Sika Primer 209D | 30 min |
| Bronze/Messing | Sika Aktivator 205 | 15 min |
| Edelstahl | Sika Aktivator 205 | 15 min |
| Holz (Teak, Mahagoni) | Sika Primer 209D | 60 min |
| Kunststoff (Marelon, TruDesign) | Kein Primer nötig | — |
| Alte Sikaflex-Reste | Vollständig entfernen! | — |

(Confidence: measured — Sika TDS)

### 5.5 Dichtmasse-Schichtstärke

| Situation | Optimale Schichtdicke | Begründung |
|---|---|---|
| Skin-Fitting↔Rumpf (Flansch) | 1–2 mm | Ausreichend für Abdichtung, nicht zu dick |
| Skin-Fitting↔Backing-Block | 2–3 mm | Ausgleich von Unebenheiten |
| Flansch-Verschraubung | 0,5–1 mm | Dünne, gleichmäßige Schicht unter Flansch |

(Confidence: documented — Sika Technical Advisory)

---

## 6. Hersteller-Kataloge — Borddurchlässe (Skin Fittings)

### 6.1 Groco (USA)

**Modellreihen:**

| Modell | Material | Typ | Gewinde | Anmerkung |
|---|---|---|---|---|
| HTH | Bronze C83600 | Mushroom | NPT | Standard, meistverkauft |
| TH | Bronze C83600 | Flanged | NPT | Für Flansch-Seeventile |
| HSTH | Edelstahl 316L | Mushroom | NPT | Premium, höherpreisig |
| SC | Bronze C83600 | Scoop | NPT | Kühlwasser-Einlass |
| SSC | Edelstahl 316L | Scoop | NPT | Kühlwasser, Edelstahl |

**Groco HTH-Serie (Mushroom Thru-Hull) — Komplettliste:**

| Modell | Gewinde | ID (mm) | OD Flansch (mm) | Länge (mm) | Gewicht (g) | Preis USD |
|---|---|---|---|---|---|---|
| HTH-500 | 1/2" NPT | 15,8 | 38 | 38 | 120 | $22–28 |
| HTH-750 | 3/4" NPT | 22,2 | 45 | 45 | 185 | $28–35 |
| HTH-1000 | 1" NPT | 28,6 | 52 | 52 | 280 | $35–48 |
| HTH-1250 | 1-1/4" NPT | 34,9 | 60 | 55 | 400 | $48–65 |
| HTH-1500 | 1-1/2" NPT | 41,3 | 70 | 60 | 520 | $55–80 |
| HTH-2000 | 2" NPT | 54,0 | 85 | 65 | 750 | $80–120 |
| HTH-2500 | 2-1/2" NPT | 66,7 | 100 | 75 | 1.100 | $120–170 |
| HTH-3000 | 3" NPT | 80,0 | 120 | 85 | 1.500 | $170–240 |

(Confidence: measured — Groco Katalog 2024)

### 6.2 Forespar / Marelon (USA)

**Marelon Thru-Hull Fittings — Komplettliste:**

| Modell | Gewinde | ID (mm) | Typ | Preis USD |
|---|---|---|---|---|
| 250-1 | 1/2" NPT | 15,8 | Mushroom | $8–12 |
| 250-2 | 3/4" NPT | 22,2 | Mushroom | $10–15 |
| 250-3 | 1" NPT | 28,6 | Mushroom | $14–22 |
| 250-4 | 1-1/4" NPT | 34,9 | Mushroom | $18–28 |
| 250-5 | 1-1/2" NPT | 41,3 | Mushroom | $22–32 |
| 250-6 | 2" NPT | 54,0 | Mushroom | $28–42 |
| 251-1 | 1/2" NPT | 15,8 | Flush | $12–18 |
| 251-2 | 3/4" NPT | 22,2 | Flush | $15–22 |
| 251-3 | 1" NPT | 28,6 | Flush | $18–28 |
| 253-1 | 1/2" NPT | 15,8 | Scoop | $12–18 |
| 253-2 | 3/4" NPT | 22,2 | Scoop | $14–22 |
| 253-3 | 1" NPT | 28,6 | Scoop | $18–28 |

(Confidence: measured — Forespar Katalog 2024)

### 6.3 TruDesign (Neuseeland)

**TruDesign Thru-Hull Fittings — 90xxx Serie:**

| Modell | Gewinde | ID (mm) | Typ | Farbe | Preis USD |
|---|---|---|---|---|---|
| 90280 | 3/4" BSP | 22 | Mushroom | Weiß | $18–25 |
| 90281 | 1" BSP | 28 | Mushroom | Weiß | $22–30 |
| 90282 | 1-1/4" BSP | 35 | Mushroom | Weiß | $28–38 |
| 90283 | 1-1/2" BSP | 41 | Mushroom | Weiß | $32–45 |
| 90284 | 2" BSP | 54 | Mushroom | Weiß | $42–58 |
| 90290 | 3/4" BSP | 22 | Scoop | Weiß | $22–30 |
| 90291 | 1" BSP | 28 | Scoop | Weiß | $28–38 |
| 90292 | 1-1/4" BSP | 35 | Scoop | Weiß | $32–42 |
| 90293 | 1-1/2" BSP | 41 | Scoop | Weiß | $38–50 |

**TruDesign Seeventile (Ball Valves):**

| Modell | Gewinde | Typ | Preis USD |
|---|---|---|---|
| 90300 | 3/4" BSP | Kugelventil | $45–60 |
| 90301 | 1" BSP | Kugelventil | $55–75 |
| 90302 | 1-1/4" BSP | Kugelventil | $70–95 |
| 90303 | 1-1/2" BSP | Kugelventil | $85–115 |
| 90304 | 2" BSP | Kugelventil | $110–150 |

(Confidence: measured — TruDesign Marine Catalogue 2024)

### 6.4 Vetus (Niederlande)

**Skin Fittings:**

| Modell | Gewinde | Material | ID (mm) | Preis EUR |
|---|---|---|---|---|
| TRC34 | 3/4" BSP | Kunststoff (Polyamid) | 20 | €8–12 |
| TRC1 | 1" BSP | Kunststoff | 25 | €10–15 |
| TRC114 | 1-1/4" BSP | Kunststoff | 32 | €14–20 |
| TRC112 | 1-1/2" BSP | Kunststoff | 38 | €16–24 |
| TRC2 | 2" BSP | Kunststoff | 50 | €22–32 |
| BTC34 | 3/4" BSP | Bronze | 20 | €28–40 |
| BTC1 | 1" BSP | Bronze | 25 | €35–50 |
| BTC114 | 1-1/4" BSP | Bronze | 32 | €45–65 |
| BTC112 | 1-1/2" BSP | Bronze | 38 | €55–80 |
| BTC2 | 2" BSP | Bronze | 50 | €75–110 |

(Confidence: measured — Vetus Katalog 2024/2025)

### 6.5 Guidi (Italien)

| Modell | Gewinde | Material | Typ | Preis EUR |
|---|---|---|---|---|
| 1042 | 3/4" BSP | Bronze | Mushroom | €25–35 |
| 1043 | 1" BSP | Bronze | Mushroom | €30–45 |
| 1044 | 1-1/4" BSP | Bronze | Mushroom | €40–55 |
| 1045 | 1-1/2" BSP | Bronze | Mushroom | €50–70 |
| 1046 | 2" BSP | Bronze | Mushroom | €70–95 |
| 1050 | 3/4" BSP | Bronze | Scoop | €30–42 |
| 1051 | 1" BSP | Bronze | Scoop | €38–52 |

(Confidence: measured — Guidi Srl Katalog)

### 6.6 Blakes (UK)

| Modell | Gewinde | Material | Typ | Preis GBP |
|---|---|---|---|---|
| BTH34 | 3/4" BSP | DZR Messing | Mushroom | £18–25 |
| BTH1 | 1" BSP | DZR Messing | Mushroom | £22–32 |
| BTH114 | 1-1/4" BSP | DZR Messing | Mushroom | £28–40 |
| BTH112 | 1-1/2" BSP | DZR Messing | Mushroom | £35–48 |
| BTH2 | 2" BSP | DZR Messing | Mushroom | £48–65 |

(Confidence: documented — Blakes Marine)

### 6.7 Perko (USA)

| Modell | Gewinde | Material | Typ | Preis USD |
|---|---|---|---|---|
| 0340 | 3/4" NPT | Bronze | Mushroom | $25–35 |
| 0340 | 1" NPT | Bronze | Mushroom | $32–45 |
| 0340 | 1-1/4" NPT | Bronze | Mushroom | $42–58 |
| 0340 | 1-1/2" NPT | Bronze | Mushroom | $52–72 |
| 0340 | 2" NPT | Bronze | Mushroom | $75–105 |
| 0342 | 3/4" NPT | Bronze | Scoop | $30–42 |
| 0342 | 1" NPT | Bronze | Scoop | $38–52 |
| 0342 | 1-1/4" NPT | Bronze | Scoop | $48–65 |

(Confidence: measured — Perko Marine Hardware Catalogue)

### 6.8 Plastimo (Frankreich)

| Modell | Gewinde | Material | Typ | Preis EUR |
|---|---|---|---|---|
| 400768 | 3/4" BSP | Kunststoff (GF-PA) | Mushroom | €6–10 |
| 400769 | 1" BSP | Kunststoff | Mushroom | €8–12 |
| 400770 | 1-1/4" BSP | Kunststoff | Mushroom | €10–16 |
| 400771 | 1-1/2" BSP | Kunststoff | Mushroom | €14–20 |
| 400781 | 3/4" BSP | Bronze | Mushroom | €22–32 |
| 400782 | 1" BSP | Bronze | Mushroom | €28–40 |
| 400783 | 1-1/4" BSP | Bronze | Mushroom | €35–50 |

(Confidence: measured — Plastimo Catalogue)

### 6.9 Seaflow (UK/China)

Budget-Hersteller, in UK und DE über Amazon/eBay erhältlich:

| Modell | Gewinde | Material | Typ | Preis EUR |
|---|---|---|---|---|
| SF-TH34 | 3/4" BSP | Kunststoff (GF-PA) | Mushroom | €4–7 |
| SF-TH1 | 1" BSP | Kunststoff | Mushroom | €5–8 |
| SF-TH114 | 1-1/4" BSP | Kunststoff | Mushroom | €6–10 |
| SF-TH112 | 1-1/2" BSP | Kunststoff | Mushroom | €8–12 |

**WARNUNG**: Seaflow-Produkte sind NICHT ISO 9093-zertifiziert. Für Unterwasser-Anwendungen wird von Surveyor-Seite ausdrücklich abgeraten.

(Confidence: documented — Forum-Berichte, UK Surveyor Empfehlung)

---

## 7. Hersteller-Kataloge — Seeventile

### 7.1 Groco Seeventile

| Modell | Gewinde | Material | Typ | Preis USD |
|---|---|---|---|---|
| BV-750 | 3/4" NPT | Bronze C83600 | Kugelventil | $75–100 |
| BV-1000 | 1" NPT | Bronze | Kugelventil | $95–130 |
| BV-1250 | 1-1/4" NPT | Bronze | Kugelventil | $130–175 |
| BV-1500 | 1-1/2" NPT | Bronze | Kugelventil | $170–230 |
| BV-2000 | 2" NPT | Bronze | Kugelventil | $240–320 |
| SC-750 | 3/4" NPT | Bronze | Hahnventil (Cone) | $115–155 |
| SC-1000 | 1" NPT | Bronze | Hahnventil | $140–190 |
| SC-1500 | 1-1/2" NPT | Bronze | Hahnventil | $225–300 |

(Confidence: measured — Groco Marine 2024)

### 7.2 Seeventil-Typen

| Typ | Vorteile | Nachteile | Empfehlung |
|---|---|---|---|
| Kugelventil (Ball Valve) | Einfache Bedienung, preiswert, 1/4-Drehung | Kugel kann festsitzen, nicht zerlegbar | Standard für alle Boote |
| Hahnventil (Cone Valve / Tapered Plug) | Zerlegbar, wartbar, kein Festsitzen | Teurer, regelmäßiges Fetten nötig | Premium, Blauwasser |
| Schieberventil (Gate Valve) | — | **VERBOTEN unter Wasserlinie** (ABYC, ISO) | NICHT VERWENDEN |

(Confidence: measured — ABYC H-27, ISO 9093)

### 7.3 Komplettsysteme (Fitting + Ventil + Schlauchstutzen)

| Hersteller | System | Materialien | Preis (1" Komplett) |
|---|---|---|---|
| TruDesign | 90xxx Modular | GF-PP | €80–110 |
| Forespar/Marelon | 905/906 System | GF-PA | $70–100 |
| Groco | HTH + BV + HB | Bronze C83600 | $160–220 |
| Vetus | BTC + BCV + HST | Bronze + Kunststoff | €120–170 |

(Confidence: documented)

---

## 8. Gewindespezifikationen

### 8.1 BSP vs. NPT vs. Metrisch

| Parameter | BSP (G) | NPT | Metrisch (M) |
|---|---|---|---|
| Standard | ISO 228-1 / BS EN 10226 | ANSI B1.20.1 | ISO 261 |
| Gewindeprofil | Parallel (BSPP) oder konisch (BSPT) | Konisch (1:16 Steigung) | Parallel |
| Dichtprinzip | O-Ring oder Dichtring (BSPP), Gewinde (BSPT) | Gewindedichtung (PTFE-Band) | O-Ring oder Flachdichtung |
| Verbreitung Marine | EU, UK, AUS, NZ | USA, Kanada | Seltener im Marinebau |
| Flankenwinkel | 55° | 60° | 60° |

**KRITISCH**: BSP und NPT sind NICHT kompatibel, obwohl die Nenndurchmesser ähnlich klingen! Ein 1" BSP-Fitting passt NICHT auf ein 1" NPT-Seeventil.

(Confidence: measured — ISO 228-1, ANSI B1.20.1)

### 8.2 Gewinde-Abmessungen

| Nenngröße | BSP-AD (mm) | NPT-AD (mm) | Steigung BSP (Gänge/Zoll) | Steigung NPT (Gänge/Zoll) |
|---|---|---|---|---|
| 3/4" | 26,441 | 26,669 | 14 | 14 |
| 1" | 33,249 | 33,401 | 11 | 11,5 |
| 1-1/4" | 41,910 | 42,164 | 11 | 11,5 |
| 1-1/2" | 47,803 | 48,260 | 11 | 11,5 |
| 2" | 59,614 | 60,325 | 11 | 11,5 |

(Confidence: measured)

### 8.3 Adapter BSP↔NPT

| Hersteller | Modell | Von | Nach | Material | Preis |
|---|---|---|---|---|---|
| Groco | ARG-750 | 3/4" NPT | 3/4" BSP | Bronze | $15–22 |
| Groco | ARG-1000 | 1" NPT | 1" BSP | Bronze | $18–28 |
| TruDesign | 90400 | 3/4" NPT | 3/4" BSP | GF-PP | $12–18 |
| TruDesign | 90401 | 1" NPT | 1" BSP | GF-PP | $15–22 |
| Vetus | AD34 | 3/4" NPT | 3/4" BSP | Kunststoff | €8–12 |

(Confidence: documented)

---

## 9. Einbau-Anleitung: Skin-Fitting

### 9.1 Werkzeugliste

| Werkzeug | Verwendung |
|---|---|
| Lochsäge (Bi-Metall) | Rumpfbohrung (Durchmesser = Fitting-OD + 1mm) |
| Schleifpapier P80 + P120 | Rumpf anschleifen, Entgraten |
| Aceton | Entfetten |
| Sika Primer 209D | GFK-Primer |
| Sikaflex 291 (oder 291i) | Dichtmasse |
| Kartuschenpistole | Dichtmasse auftragen |
| Maulschlüssel (passend) | Gegenmutter anziehen |
| Backing-Block (GFK oder Holz/Epoxy) | Lastverteilung |
| Drehmomentschlüssel | Definiertes Anzugsmoment |

(Confidence: documented)

### 9.2 Einbau-Schritte

| Schritt | Aktion | Detail | Fehlerquelle |
|---|---|---|---|
| 1 | Position markieren | Von innen, Zugang zu Seeventil sicherstellen | Zu nah an Kiel, Ruder, Schott |
| 2 | Rumpfstärke messen | Ultraschall oder Kernbohrung | Zu dünn → Backing-Block Pflicht |
| 3 | Loch bohren (von außen) | Lochsäge, Durchmesser = Fitting-AD + 1mm | Schräges Bohren → undichter Sitz |
| 4 | Laminat versiegeln | Epoxidharz auf Schnittkante, 24h trocknen | Offene Schnittkante → Osmose |
| 5 | Backing-Block vorbereiten | Innenform an Rumpfkrümmung anpassen | Kein Kontakt → Punkt-Belastung |
| 6 | Oberflächen anschleifen | P80 innen + außen, Staub entfernen | Zu glatt → Haftungsproblem |
| 7 | Entfetten | Aceton, sauber wischen | Fettspuren → Dichtmasse-Versagen |
| 8 | Primer auftragen | Sika 209D auf GFK, 30 min ablüften | Ohne Primer → 50% Haftverlust |
| 9 | Dichtmasse auftragen | Sikaflex 291, 2mm Raupe auf Flansch + Gewindegänge | Zu wenig → Undicht; Zu viel → Quetscht raus |
| 10 | Fitting einsetzen | Von außen, drehen bis Flansch satt aufliegt | Nicht verkanten |
| 11 | Gegenmutter + Backing-Block | Von innen, Dichtmasse zwischen Block und Rumpf | Vergessener Backing-Block → Riss |
| 12 | Anzugsmoment | Bronze: 35–45 Nm; Composite: MAX 27 Nm | Composite: Überdreht → Flansch bricht! |
| 13 | Überschuss entfernen | Spüli-Finger | Frisch machen, nicht ausgehärtet |
| 14 | Aushärten | 7 Tage (Sikaflex 291), kein Wasserkontakt | Zu früh ins Wasser → Dichtung versagt |

(Confidence: documented — Steve D'Antonio, Sika Marine Application Guide)

### 9.3 Backing-Block Dimensionierung

| Rumpfstärke (mm) | Backing-Block Pflicht? | Block-Material | Block-Dicke (mm) | Block-Fläche |
|---|---|---|---|---|
| ≥12 | Empfohlen | GFK-Platte oder Hartholz/Epoxy | 10–15 | 2× Flansch-AD |
| 8–12 | Ja | GFK-Platte oder Hartholz/Epoxy | 12–20 | 2,5× Flansch-AD |
| <8 | Unbedingt! | GFK-Laminat (aufbauen) + Block | 15–25 | 3× Flansch-AD |

(Confidence: documented — ABYC H-27, Nigel Calder)

### 9.4 Drehmoment-Spezifikationen

| Material | 3/4" | 1" | 1-1/4" | 1-1/2" | 2" |
|---|---|---|---|---|---|
| Bronze | 25 Nm | 30 Nm | 35 Nm | 40 Nm | 45 Nm |
| Edelstahl 316L | 25 Nm | 30 Nm | 35 Nm | 40 Nm | 45 Nm |
| Marelon/TruDesign | 20 Nm | 22 Nm | 24 Nm | 26 Nm | 27 Nm |

**WARNUNG COMPOSITE**: Max. 27 Nm (20 ft-lbs)! Überdrehen = Flanschbruch = Wassereinbruch!

(Confidence: measured — Forespar TI-007, TruDesign Installation Guide)

---

## 10. Einbau-Anleitung: Seeventil-Montage

### 10.1 Seeventil auf Skin-Fitting

| Schritt | Aktion | Detail |
|---|---|---|
| 1 | O-Ring prüfen | Material korrekt? (Seewasser = EPDM, Diesel = FKM) |
| 2 | O-Ring einlegen | In Nut am Skin-Fitting, leicht mit Vaseline fetten |
| 3 | Seeventil aufschrauben | Handfest, dann 1/4-Drehung mit Schlüssel |
| 4 | Kontermutter sichern | Gegenmutter gegen Ventil kontern |
| 5 | Funktion prüfen | Ventilhebel muss 90° schließen, leichtgängig |
| 6 | Drucktest | 0,5 bar, 5 min — keine Leckage |

(Confidence: documented)

### 10.2 Bonding-Draht (elektrische Erdung)

| Anforderung | Detail |
|---|---|
| ABYC E-11 | Alle metallischen Borddurchlässe müssen mit Bonding-System verbunden sein |
| Draht | Verzinntes Kupferkabel, min. 8 AWG (8 mm²) |
| Anschluss | Kabelschuh auf Seeventil-Körper (eigene Bohrung/Klemme) |
| Verbindung | Sternförmig zum zentralen Bonding-Bus, dann zum Zinkanode |

**Warum**: Ohne Bonding → unkontrollierte galvanische Korrosion, besonders in Häfen mit Fremd-Streuströmen.

(Confidence: measured — ABYC E-11)

---

## 11. Übergang Seeventil → Schlauch

### 11.1 Grundregel: KEIN Dichtstoff!

Die Verbindung Seeventil→Schlauch wird ausschließlich durch Schlauchschellen hergestellt. KEIN Sikaflex, KEIN Silikon, KEIN Kleber. Grund:

| Warum kein Dichtstoff | Detail |
|---|---|
| Schlauch muss austauschbar sein | Dichtstoff verhindert Demontage |
| Schlauch arbeitet (Vibration, Temperatur) | Dichtstoff reißt → falsches Sicherheitsgefühl |
| Schlauchschelle ist die Dichtung | Richtig dimensionierte Schelle + richtiger Schlauch = dicht |

(Confidence: documented — ABYC H-27, Nigel Calder "Boatowner's Mechanical & Electrical Manual")

### 11.2 Schlauch-Spezifikationen

| Typ | Norm | Einsatz | Temperatur | Preis/m |
|---|---|---|---|---|
| Marineschlauch (verstärkt) | SAE J1942 / ISO 7840 | Kühlwasser, Seewasser | –30 bis +70°C | €8–15 |
| Auspuffschlauch (nass) | SAE J2006 / ISO 13363 | Nass-Auspuff | –30 bis +100°C | €15–35 |
| Kraftstoffschlauch | SAE J1527 / ISO 7840-A1 | Diesel, Benzin | –30 bis +65°C | €12–25 |
| Trinkwasserschlauch | KTW/W270 / FDA | Trinkwasser | –10 bis +60°C | €5–10 |
| Sanitärschlauch (geruchsdicht) | — | Fäkalien, Abwasser | –10 bis +60°C | €8–18 |

(Confidence: documented)

---

## 12. Schlauchschellen-Spezifikationen

### 12.1 Anforderungen unter Wasserlinie

| Kriterium | Anforderung | Norm |
|---|---|---|
| Material Band | Edelstahl 316 (AISI 316) | ABYC H-27 |
| Material Schraube | Edelstahl 316 | ABYC H-27 |
| Doppelschelle | Pflicht unter Wasserlinie | ABYC H-27, ISO 9093 |
| Bandbreite | ≥12mm (besser 16mm) | Best Practice |
| Perforiert vs. Vollband | Vollband bevorzugt (höhere Klemmkraft) | Steve D'Antonio |
| Anzugsdrehmoment | 3–4 Nm (Schlauch, nicht Fitting!) | Hersteller |

(Confidence: measured — ABYC H-27)

### 12.2 Schlauchschellen-Hersteller

| Hersteller | Modell | Material | Bandbreite | Band-Typ | Preis/Stk |
|---|---|---|---|---|---|
| AWAB (Marine Grade) | W5 | 316L | 12mm | Vollband | €2,50–4 |
| Norma (TORRO) | W5 | 316L | 12mm | Halbperforiert | €1,80–3 |
| Mikalor | SUPRA W5 | 316L | 12mm | Vollband | €2–3,50 |
| Jubilee (UK) | Marine Grade | 316 | 12mm | Perforiert | £1,50–2,50 |
| Trident Marine (USA) | 720 | 316 | 5/8" (16mm) | Vollband | $3–5 |
| Murray (USA) | All-Stainless | 316 | 9/16" (14mm) | Perforiert | $2–3,50 |
| ABA (Schweden) | Original W5 | 316L | 12mm | Vollband | €2,50–4 |
| Breeze Industrial (USA) | Breeze 63 | 316 | 9/16" | Vollband | $2–3,50 |
| Hi-Grip (UK) | Marine | 316 | 12mm | Perforiert | £1,50–2,50 |

**WARNUNG**: Billige Schlauchschellen mit Band aus 304-Stahl und Schraube aus Kohlenstoffstahl sind die häufigste Ursache für Schlauchschellen-Versagen. Die Schraube rostet, das Band löst sich — Wassereinbruch.

(Confidence: documented — Steve D'Antonio, Practical Sailor Schlauchschellen-Test 2018)

### 12.3 Doppelschellen — Anordnung

```
Richtig:                          Falsch:
┌─────────────┐                  ┌─────────────┐
│  Schelle 2  │ 25mm Abstand    │  Schelle 2  │ direkt übereinander
│  Schelle 1  │                  │  Schelle 1  │
└──────┬──────┘                  └──────┬──────┘
       │ Schlauch                       │
───────┴───────                  ───────┴───────
    Seeventil                       Seeventil
```

Doppelschellen immer mit 20–30mm Abstand zueinander. Schrauben um 180° versetzt.

(Confidence: documented)

---

## 13. Materialkompatibilität und Galvanik

### 13.1 Galvanische Spannungsreihe (Marine)

| Material | Potenzial in Seewasser (V vs. Ag/AgCl) |
|---|---|
| Zink (Anode) | –1,03 |
| Aluminium | –0,76 bis –1,00 |
| Stahl | –0,60 bis –0,71 |
| Blei | –0,50 |
| Messing (unlegiert) | –0,30 |
| Bronze C83600 | –0,24 bis –0,31 |
| Kupfer | –0,20 |
| Nibral C95800 | –0,15 bis –0,22 |
| Edelstahl 316L (passiv) | –0,05 bis –0,10 |
| Titan | –0,05 |
| Graphit/Kohlefaser | +0,20 |

(Confidence: measured — MIL-STD-889C)

### 13.2 Kompatibilitätsmatrix Borddurchlass ↔ Rumpf

| Kombination | Kompatibel? | Galv. Diff. (mV) | Maßnahme |
|---|---|---|---|
| Bronze ↔ GFK | ✅ JA | 0 (GFK = inert) | Standard, keine Sondermaßnahme |
| Edelstahl ↔ GFK | ⚠️ BEDINGT | 0 (GFK = inert) | Spaltkorrosionsrisiko am Fitting selbst |
| Composite ↔ GFK | ✅ JA | 0 | Ideale Kombination |
| Bronze ↔ Aluminium | ❌ NEIN | ~500 mV | **Katastrophal! Alu wird zerstört!** |
| Edelstahl ↔ Aluminium | ❌ NEIN | ~700 mV | Noch schlimmer als Bronze! |
| Composite ↔ Aluminium | ✅ JA | 0 | **Einzig sichere Option für Alu-Rumpf** |
| Bronze ↔ Stahl | ⚠️ BEDINGT | ~350 mV | Nur mit Isolation + Zinkanode |
| Edelstahl ↔ Stahl | ⚠️ BEDINGT | ~550 mV | Nur mit Isolation + Zinkanode |
| Composite ↔ Stahl | ✅ JA | 0 | Empfohlen für Stahl-Rumpf |

(Confidence: documented — Steve D'Antonio, ABYC E-2)

### 13.3 Aluminium-Rumpf: Sonderregeln

| Regel | Detail |
|---|---|
| NUR Composite-Durchlässe | TruDesign oder Marelon — KEINE Metalle unter Wasser! |
| Kein Bronze, kein Edelstahl | Galvanische Korrosion zerstört Alu-Rumpf in 1–3 Jahren |
| Bonding-System | Alle metallischen Teile AN Bord müssen mit Alu-Rumpf verbunden sein |
| Zinkanoden | Zinkanoden (NICHT Magnesium) für Aluminium |
| Trennschicht | Butylband oder Tef-Gel zwischen Nicht-Alu-Metall und Alu |
| Hafenlieger | Besondere Vorsicht: Streu-Ströme im Hafen beschleunigen Galvanik |

(Confidence: documented — Steve D'Antonio "Metal Boat Building", Forum-Konsens)

### 13.4 Dezinkifizierung — Das versteckte Problem

**Was passiert:** Zink löst sich aus Messing/Bronze-Legierung. Das Fitting wird porös, rosa/kupferfarben, und verliert Festigkeit — kann mit dem Finger eingedrückt werden.

| Risikofaktor | Detail |
|---|---|
| Betroffene Legierungen | Messing (>15% Zn), Bronze C84400 (9% Zn) |
| Sichere Legierungen | C83600 (5% Zn), DZR-Messing (mit Arsen-Zugabe), Nibral |
| Beschleuniger | Warmes Wasser, niedriger pH, Streu-Ströme |
| Erkennungsmerkmale | Rosa/kupferfarbene Oberfläche, sprödes Material, Aufblühungen |
| Zeitrahmen | 5–15 Jahre (langsam), 1–3 Jahre (mit Streu-Strömen) |
| Prüfung | Messer-Test: Gesundes Bronze ist hart; dezinkifiziertes kratzt weich |

(Confidence: documented — Practical Sailor, Marine Surveyor Reports)

---

## 14. Fehlerbilder und Diagnostik

### 14.1 Fehlerbild-Katalog

| Nr. | Fehlerbild | Ursache | Diagnose | Maßnahme | Dringlichkeit |
|---|---|---|---|---|---|
| F-01 | Tropfen am Flansch (außen) | Dichtmasse versagt | Visuell, Farbstofftest | Fitting ausbauen, neu abdichten | HOCH |
| F-02 | Tropfen am O-Ring | O-Ring defekt/falsches Material | Seeventil lösen, O-Ring prüfen | O-Ring tauschen | HOCH |
| F-03 | Grüne Ablagerungen (Grünspan) | Korrosion, galvanisch | Visuell | Ursache beheben, Anode prüfen | MITTEL |
| F-04 | Rosa/kupferfarbene Oberfläche | Dezinkifizierung | Messer-Test, visuell | SOFORT TAUSCHEN | KRITISCH |
| F-05 | Fitting wackelt im Rumpf | Backing-Block fehlt/gebrochen | Händisch prüfen | Backing-Block nachrüsten | HOCH |
| F-06 | Riss im Rumpf um Fitting | Stoß, fehlender Block, Überdreht | Visuell, UV-Lampe, Klopftest | Laminat reparieren | KRITISCH |
| F-07 | Schlauchschelle rostet | 304er oder Kohlenstoffstahl | Visuell | Alle Schellen durch 316L ersetzen | MITTEL |
| F-08 | Schlauch hart/rissig | UV, Ozon, Alter (>10 Jahre) | Biegen, visuell | Schlauch komplett tauschen | HOCH |
| F-09 | Composite-Flansch gebrochen | Überdreht (>27 Nm) | Visuell, offensichtlich | Fitting tauschen, korrekt montieren | KRITISCH |
| F-10 | Elektrolyse-Fraß | Streu-Ströme (Marina) | Galvanischer Isolationstest | Galvanischer Isolator, Bonding prüfen | KRITISCH |
| F-11 | Seeventil schwergängig | Korrosion, Fouling, fehlende Wartung | Betätigen | Demontieren, reinigen, fetten | MITTEL |
| F-12 | Seeventil-Hebel gebrochen | Materialermüdung, Überbelastung | Visuell | Ventil tauschen | HOCH |
| F-13 | Wassereinbruch unter Bilge | Undichtes Fitting | Trockentest: alle Ventile zu | Systematic check aller Durchlässe | KRITISCH |
| F-14 | Biofouling im Fitting | Muscheln, Seepocken im Rohrdurchmesser | Durchfluss reduziert | Mechanisch reinigen | NIEDRIG |
| F-15 | PTFE-Band im Seeventil | Falscher Einbau (PTFE löst sich) | Ventil demontieren | Band entfernen, O-Ring verwenden | MITTEL |
| F-16 | Schwarze Verfärbung (Sulfid) | Anaerobe Korrosion (unter Antifouling) | Visuell | Antifouling erneuern, Fitting prüfen | MITTEL |
| F-17 | Spaltkorrosion an Edelstahl | Sauerstoffmangel in Spalten | Erst spät sichtbar! | Edelstahl durch Bronze/Composite ersetzen | HOCH |
| F-18 | Rissbildung am Scoop-Einlass | Berührung Grund, Anker, Dalbe | Visuell, Taucher | Scoop tauschen | HOCH |

(Confidence: documented — Steve D'Antonio, Marine Surveyor Reports, Forum-Berichte)

### 14.2 Diagnose-Flussdiagramm

```
Wassereinbruch festgestellt?
├── JA → Alle Seeventile schließen!
│   ├── Wasser stoppt? → Undichtigkeit an einem Borddurchlass
│   │   ├── Systematisch jedes Ventil einzeln öffnen
│   │   └── Tropfentest an jedem Fitting
│   └── Wasser stoppt NICHT? → Rumpfriss, Kielbefestigung, Ruderschaft
└── NEIN (Routineinspektion)
    ├── Visuell: Grünspan, Rosa, Risse?
    │   ├── Rosa → Dezinkifizierung → SOFORT TAUSCHEN
    │   ├── Grünspan → Galvanik → Anode prüfen
    │   └── Riss → Rumpflaminat → Surveyor
    ├── Messer-Test (Bronze): Hart oder weich?
    │   ├── Weich → Dezinkifizierung → TAUSCHEN
    │   └── Hart → OK
    ├── Schlauchschellen prüfen: Rost? Locker?
    │   ├── Rost → Durch 316L ersetzen
    │   └── Locker → Nachziehen (3–4 Nm)
    └── Seeventil betätigen: Leichtgängig?
        ├── Schwer → Demontieren, reinigen, fetten
        └── Leicht → OK, jährlich prüfen
```

(Confidence: documented)

### 14.3 Ultraschall-Wandstärkenprüfung

| Parameter | Wert |
|---|---|
| Gerät | Cygnus Mini, GE DM5E, Elcometer MTG8 |
| Koppelmittel | Ultraschall-Gel oder Wasser |
| Messstellen | Rumpf um Fitting (4 Punkte: 12/3/6/9 Uhr) |
| Mindestwandstärke GFK | ≥8mm für Borddurchlass ohne Backing-Block |
| Mindestwandstärke Alu | ≥4mm (6mm empfohlen) |
| Wiederholung | Alle 5 Jahre, jährlich bei >20 Jahre altem Boot |

(Confidence: documented)

---

## 15. Schadensfälle / Fallstudien

### 15.1 Fallstudie: Bénéteau Océanis 38.1 — Dezinkifizierung

| Feld | Detail |
|---|---|
| Boot | Bénéteau Océanis 38.1, Baujahr 2018 |
| Standort | Mittelmeer (Griechenland), Charterboot |
| Problem | Borddurchlass Toiletteneinlass porös, rosa Verfärbung |
| Alter des Fittings | 5 Jahre |
| Ursache | Werksseitiges Messing-Fitting (nicht Bronze), beschleunigt durch Marina-Streu-Ströme |
| Entdeckung | Routineinspektion beim Haul-out |
| Reparatur | Alle 7 Unterwasser-Durchlässe getauscht gegen TruDesign Composite |
| Kosten | €2.200 (Teile: €900, Werft: €1.300) |
| Lektion | Bénéteau hat 2020 auf TruDesign Composite als OEM umgestellt |
| Quelle | CruisersForum Thread #235817, Bestätigt durch SVB Service-Report |

(Confidence: documented)

### 15.2 Fallstudie: Hallberg-Rassy 37 — 35 Jahre alter Bronze-Durchlass

| Feld | Detail |
|---|---|
| Boot | Hallberg-Rassy 37 MK II, Baujahr 1989 |
| Standort | Schweden → Mittelmeer → Karibik (Blauwasser-Segler) |
| Problem | Kein Problem! Bronze C83600 noch einwandfrei nach 35 Jahren |
| Wartung | Jährliches Fetten der Seeventile, Zinkanoden alle 2 Jahre |
| Befund | Wandstärke nur 0,2mm reduziert (Ultraschall) |
| Lektion | Korrekte Bronze-Legierung + konsequente Wartung = extreme Langlebigkeit |
| Quelle | YBW Forum, Eigner-Bericht, bestätigt durch RINA-Surveyor |

(Confidence: documented)

### 15.3 Fallstudie: Catalina 30 — Spaltkorrosion Edelstahl

| Feld | Detail |
|---|---|
| Boot | Catalina 30, Baujahr 2005 |
| Standort | Chesapeake Bay, USA |
| Problem | 316L Edelstahl-Borddurchlass (Motor-Kühlwasser) von innen durchkorrodiert |
| Alter | 12 Jahre |
| Ursache | Spaltkorrosion in sauerstoffarmem Bereich zwischen Fitting und Rumpf |
| Entdeckung | Wassereinbruch beim Motorlauf, Motor-Kühlwasser läuft ins Bilge |
| Reparatur | Edelstahl entfernt, durch Groco HTH-1000 (Bronze) ersetzt |
| Kosten | $650 (Teile: $180, Yard: $470) |
| Lektion | Edelstahl ist NICHT die beste Wahl für Unterwasser-Durchlässe |
| Quelle | SailboatOwners.com, Thread Catalina 30 Seacock Failure |

(Confidence: documented)

### 15.4 Fallstudie: J/105 — Composite-Flansch übergedreht

| Feld | Detail |
|---|---|
| Boot | J/105, Baujahr 2012 |
| Standort | San Francisco Bay, USA |
| Problem | Marelon-Borddurchlass (Cockpit-Drain), Flansch gerissen |
| Alter | 4 Jahre |
| Ursache | Mechaniker hat Gegenmutter mit 40+ Nm angezogen (Max. 27 Nm!) |
| Entdeckung | Wassereinbruch bei Kränkung, Wasser läuft über Cockpit-Drain zurück |
| Reparatur | Fitting getauscht, Drehmomentschlüssel verwendet |
| Kosten | $320 (Teile: $85, DIY + Haul-out-Anteil) |
| Lektion | IMMER Drehmomentschlüssel bei Composite! |
| Quelle | Sailing Anarchy Forum, J/105 Class Association |

(Confidence: documented)

### 15.5 Fallstudie: Alubat Ovni 435 — Galvanik-Katastrophe

| Feld | Detail |
|---|---|
| Boot | Alubat Ovni 435, Baujahr 2008 |
| Standort | Karibik (Martinique) |
| Problem | Alu-Rumpf um Bronze-Durchlass massiv korrodiert, "weich wie Käse" |
| Alter | 6 Jahre |
| Ursache | Voreigner hat Bronze-Skin-Fitting auf Alu-Rumpf montiert — galvanische Korrosion |
| Entdeckung | Surveyor bei Kaufinspektion |
| Reparatur | Alu-Rumpf großflächig schweißen (200×200mm Patch), alle Durchlässe auf TruDesign |
| Kosten | €15.000+ (Schweißarbeiten: €12.000, Teile: €3.000) |
| Lektion | NIEMALS Metall auf Aluminium-Rumpf ohne galvanische Trennung |
| Quelle | CruisersForum Aluminium Thread, Bestätigt durch BV-Surveyor |

(Confidence: documented)

### 15.6 Fallstudie: Nordhavn 47 — Exemplarische Borddurchlass-Installation

| Feld | Detail |
|---|---|
| Boot | Nordhavn 47, Baujahr 2014 |
| Standort | Pacific Northwest → Pacific Crossing |
| System | Groco Bronze SC-1000 Hahnventile, alle Durchlässe |
| Besonderheit | Schiffbau-Standard: jeder Durchlass mit Backing-Block, Bonding-Draht, Doppelschellen |
| Ergebnis | Null Probleme nach 10 Jahren und 35.000 sm |
| Wartung | Jährlich: Seeventile fetten, Anoden prüfen, Schlauchschellen nachziehen |
| Lektion | Premium-Installation zahlt sich über Bootslebensdauer aus |
| Quelle | TrawlerForum, Nordhavn Owners Association |

(Confidence: documented)

### 15.7 Fallstudie: Bavaria 34 — Falsches Dichtmittel

| Feld | Detail |
|---|---|
| Boot | Bavaria 34, Baujahr 2016 |
| Standort | Ostsee (Kiel) |
| Problem | Wassereinbruch am Toiletten-Borddurchlass nach 3 Jahren |
| Ursache | Werft hat Silikon statt Polyurethan als Dichtmasse verwendet |
| Diagnose | Silikon hat sich vom GFK gelöst — typisches Versagensmuster |
| Reparatur | Fitting ausbauen, Silikon komplett entfernen, neu mit Sikaflex 291i |
| Kosten | €180 (DIY, Teile: €35, Haul-out-Anteil: €145) |
| Lektion | Silikon ist NICHT für Borddurchlässe geeignet |
| Quelle | segeln-forum.de, SVB Kundenbericht |

(Confidence: documented)

### 15.8 Fallstudie: X4³ — Racing-Standard meets Langfahrt

| Feld | Detail |
|---|---|
| Boot | X-Yachts X4³, Baujahr 2019 |
| Standort | Dänemark → Transatlantik → Karibik |
| Problem | Alle Borddurchlässe werksseitig TruDesign Composite, Cockpit-Drain-Fitting UV-spröde nach 4 Jahren |
| Ursache | Offener Cockpit-Drain (ständig UV-exponiert), TruDesign hat UV-Stabilisator, aber tropische UV-Intensität höher |
| Reparatur | Cockpit-Drains auf Groco Bronze getauscht, Unterwasser-Durchlässe TruDesign belassen |
| Kosten | DKK 8.500 (€1.140) |
| Lektion | Composite in tropischer UV = höherer Verschleiß, über Wasser Bronze oder Nibral erwägen |
| Quelle | Dansk Sejlunion Forum, X-Yachts Owners Group |

(Confidence: documented)

### 15.9 Fallstudie: Swan 48 — Superyacht-Standard

| Feld | Detail |
|---|---|
| Boot | Nautor Swan 48, Baujahr 2021 |
| System | Nibral C95800 Skin-Fittings, Groco SC-Serie Hahnventile |
| Besonderheit | Jeder Durchlass mit eigenem Bonding-Draht, Nibral-Backing-Plate, Sikaflex 292i |
| Dichtungssystem | FKM/Viton O-Ringe, Trident Marine 720 Doppelschellen |
| Wartung | Jährlich durch autorisierte Werft |
| Lektion | Was "richtig" aussieht — Referenzinstallation für alle anderen |
| Quelle | Nautor Swan Technical Bulletin, Marine Surveyor Report Helsinki |

(Confidence: documented)

### 15.10 Fallstudie: Lagoon 42 — Katamaran-Spezifisches

| Feld | Detail |
|---|---|
| Boot | Lagoon 42, Baujahr 2020 |
| Standort | Karibik (BVI) |
| Besonderheit | Katamaran: 2× so viele Borddurchlässe (2 Rümpfe), teilweise weit auseinander |
| Problem | Motor-Kühlwasser-Einlass (Steuerbord): Schlauchschelle gelöst, langsamer Wassereinbruch |
| Ursache | Bilge-Pump lief ständig, aber wegen Katamaran-Volumen nicht sofort bemerkt |
| Entdeckung | Nach 3 Tagen, als Motor-Bilge voll |
| Reparatur | Schlauchschelle getauscht (304er → 316L), beide Rümpfe komplett überprüft |
| Kosten | $85 (DIY) — aber hätte das Boot versenken können |
| Lektion | Katamaran: doppelte Anzahl Durchlässe = doppelte Wartung! |
| Quelle | CruisersForum Catamaran Section |

(Confidence: documented)

---

## 16. OEM-Spezifikationen nach Bootshersteller

### 16.1 Bénéteau (Frankreich)

| Parameter | Detail |
|---|---|
| OEM-Lieferant (ab 2020) | TruDesign (Neuseeland) |
| OEM-Lieferant (vor 2020) | Plastimo, teilweise Messing |
| Standard-Größen | 3/4" BSP (Waschbecken), 1" BSP (Toilette), 1-1/4" BSP (Motor) |
| Dichtmasse (Werk) | Sikaflex 291i |
| Schlauchschellen (Werk) | Norma W5, 12mm |
| Ersatzteile über | SVB (DE), Accastillage Diffusion (FR) |
| Bekanntes Problem | Vor 2020: Messing-Fittings anfällig für Dezinkifizierung |

(Confidence: documented — Bénéteau Service Bulletin, SVB)

### 16.2 Jeanneau (Frankreich)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | TruDesign (seit 2019), vorher Plastimo |
| Standard-Größen | Wie Bénéteau (selber Konzern: Groupe Bénéteau) |
| Dichtmasse (Werk) | Sikaflex 291i |
| Ersatzteile über | Jeanneau-Händlernetz, SVB, AD |

(Confidence: documented)

### 16.3 Bavaria (Deutschland)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Vetus (Kunststoff), teilweise TruDesign |
| Standard-Größen | 3/4" BSP, 1" BSP, 1-1/4" BSP |
| Dichtmasse (Werk) | Sikaflex 291i |
| Schlauchschellen (Werk) | Norma W5 |
| Ersatzteile über | SVB (offizieller Partner), Compass24 |
| Bekanntes Problem | Ältere Modelle (<2015): Kunststoff-Seeventile von geringer Qualität |

(Confidence: documented — SVB, boote-forum.de)

### 16.4 Hanse (Deutschland)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Vetus, TruDesign (neuere Modelle) |
| Dichtmasse (Werk) | Sikaflex 291i |
| Ersatzteile über | SVB, HanseYachts Ersatzteilservice |

(Confidence: documented)

### 16.5 Hallberg-Rassy (Schweden)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Guidi (Bronze), eigene Spezifikation |
| Material | Ausschließlich Bronze (kein Kunststoff unter Wasser) |
| Dichtmasse (Werk) | Sikaflex 292i (strukturell) |
| Backing-Blocks | Standard (GFK-laminiert, werkseitig) |
| Bonding-System | Komplett, ab Werk |
| Ersatzteile über | HR-Vertragswerften, Hallberg-Rassy Direkt |
| Reputation | Referenz-Standard für Borddurchlass-Installation |

(Confidence: documented — HR Technical Specifications)

### 16.6 Catalina (USA)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Groco (Bronze), Forespar/Marelon (Kunststoff) |
| Gewinde | NPT (US-Standard!) |
| Dichtmasse (Werk) | 3M 4200 oder Sikaflex 291 |
| Schlauchschellen | Breeze Industrial, 316 |
| Ersatzteile über | Catalina Direct, West Marine, Defender |

(Confidence: documented — Catalina Owners Association)

### 16.7 Oyster (UK)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Blakes (DZR Messing/Bronze) |
| Gewinde | BSP |
| Qualitätsstandard | Lloyd's Register zertifiziert |
| Dichtmasse | Sikaflex 292i |
| Backing-Blocks | Integriert in Laminataufbau |

(Confidence: documented)

### 16.8 Lagoon / Fountaine-Pajot (Katamarane)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | TruDesign (Lagoon ab 2019), Plastimo (ältere) |
| Besonderheit | 2× Rumpf = doppelte Anzahl Durchlässe |
| Motor-Einlass | Oft 1-1/4" BSP (Zweirumpf = 2× Motor) |
| Dichtmasse | Sikaflex 291i |
| Wartungshinweis | Beide Rümpfe EINZELN prüfen! |

(Confidence: documented)

---

## 17. Weltweite Bezugsquellen

### 17.1 Deutschland

| Händler | Sortiment | Versand | Besonderheit |
|---|---|---|---|
| SVB (svb24.com) | Groco, TruDesign, Vetus, Guidi, Sikaflex | DE + EU | Offizieller Bavaria/Hanse-Partner |
| AWN (awn.de) | Vetus, Plastimo, Sikaflex | DE + EU | Breites Sortiment |
| Compass24 (compass24.de) | Vetus, TruDesign, Plastimo | DE + EU | Guter Preisvergleich |
| Toplicht (toplicht.de) | Premium-Auswahl, Guidi, Groco | DE + EU | Hamburg, Ladengeschäft |
| Bukh-Bremen | Vetus, Perkins-Teile | DE | Motoren + Zubehör |

(Confidence: documented)

### 17.2 UK

| Händler | Sortiment | Besonderheit |
|---|---|---|
| Force4 (force4.co.uk) | Blakes, TruDesign, Plastimo | Größter UK-Versand |
| Marine Superstore | Blakes, Vetus | South Coast |
| CH Marine (chmarine.com) | Blakes, TruDesign | Irland + UK |
| Seadog (seadog.co.uk) | Blakes, Budget-Alternativen | Online-Spezialist |
| Simpson Marine Hardware | Premium Bronze | Traditioneller Hersteller |

(Confidence: documented)

### 17.3 USA

| Händler | Sortiment | Besonderheit |
|---|---|---|
| West Marine (westmarine.com) | Groco, Forespar/Marelon, Perko | Größte Kette, Filialen landesweit |
| Defender (defender.com) | Groco, Forespar, Perko | Online, oft günstiger als WM |
| Hamilton Marine (hamiltonmarine.com) | Groco, Marine-Spezialist | Maine, New England |
| Jamestown Distributors (jamestowndistributors.com) | Groco, Sikaflex, Epoxy | Profi-Bedarf |
| Fisheries Supply (fisheriessupply.com) | Groco, Perko | Pacific Northwest |
| Marine Hardware Direct | Budget Bronze | Online |

(Confidence: documented)

### 17.4 Frankreich

| Händler | Sortiment | Besonderheit |
|---|---|---|
| Accastillage Diffusion (ad-europe.com) | Plastimo, Guidi, TruDesign | Größte FR-Kette |
| Uship (uship.fr) | Breites Sortiment | Franchise, viele Standorte |
| Comptoir Nautique | Plastimo, Vetus | Online |

(Confidence: documented)

### 17.5 Niederlande

| Händler | Sortiment | Besonderheit |
|---|---|---|
| Maritieme-Producten.nl | Vetus (NL-Hersteller), TruDesign | Direkt-Import |
| Vetus Direkt (vetus.com) | Vetus Komplettsortiment | Hersteller-Shop |
| Nautic Gear | Vetus, Plastimo | Online |

(Confidence: documented)

### 17.6 Skandinavien

| Händler | Sortiment | Land |
|---|---|---|
| Gumbodeals (gumbodeals.se) | TruDesign, Vetus | Schweden |
| Biltema (biltema.se) | Budget-Marine | SE/NO/FI/DK |
| Maritim (maritim.no) | Vetus, TruDesign | Norwegen |
| Sailing Parts (sailingparts.dk) | TruDesign, Guidi | Dänemark |

(Confidence: documented)

### 17.7 Australien / Neuseeland

| Händler | Sortiment | Besonderheit |
|---|---|---|
| Whitworths (whitworths.com.au) | TruDesign (NZ!), Groco | Größte AU-Kette |
| Burnsco (burnsco.co.nz) | TruDesign | NZ-Hersteller direkt |
| BIA (bia.com.au) | TruDesign, Vetus | Großhandel |
| Bias Boating (biasboating.com.au) | Breites Sortiment | Online AU |

(Confidence: documented)

### 17.8 Karibik

| Händler | Sortiment | Standorte |
|---|---|---|
| Budget Marine (budgetmarine.com) | Groco, TruDesign | 12 Standorte karibikweit |
| Island Water World (islandwaterworld.com) | Groco, Forespar | St. Maarten, Curaçao |
| Parts & Power (partsandpower.com) | Groco | BVI |
| Carib Marine Supplies | Budget-Sortiment | Trinidad |

(Confidence: documented)

### 17.9 Mittelmeer

| Händler | Sortiment | Standorte |
|---|---|---|
| Guidi Direkt (guidi.it) | Guidi Bronze | Italien |
| Index Marine (Türkei) | Vetus, TruDesign | Türkei |
| Navtec (navtec.gr) | TruDesign, Plastimo | Griechenland |
| Yacht Parts Mallorca | Vetus, Guidi | Spanien |
| Rodman (rodman.es) | Plastimo | Spanien |

(Confidence: documented)

---

## 18. Preisvergleich

### 18.1 Skin-Fitting 1" — Alle Hersteller

| Hersteller | Modell | Material | Gewinde | Preis (lokale Währung) | Preis (EUR) |
|---|---|---|---|---|---|
| Groco | HTH-1000 | Bronze C83600 | 1" NPT | $35–48 | €32–44 |
| Perko | 0340-006 | Bronze | 1" NPT | $32–45 | €29–41 |
| Forespar | 250-3 | Marelon (GF-PA) | 1" NPT | $14–22 | €13–20 |
| TruDesign | 90281 | GF-PP | 1" BSP | $22–30 | €20–28 |
| Vetus | BTC1 | Bronze | 1" BSP | €35–50 | €35–50 |
| Vetus | TRC1 | Kunststoff | 1" BSP | €10–15 | €10–15 |
| Guidi | 1043 | Bronze | 1" BSP | €30–45 | €30–45 |
| Blakes | BTH1 | DZR Messing | 1" BSP | £22–32 | €26–37 |
| Plastimo | 400769 | Kunststoff | 1" BSP | €8–12 | €8–12 |
| Seaflow | SF-TH1 | Kunststoff | 1" BSP | €5–8 | €5–8 |

(Confidence: documented — Preise Stand 2025/2026)

### 18.2 Komplettsystem 1" (Fitting + Seeventil + Schlauchstutzen)

| Hersteller | Materialien | Preis | Lebensdauer (erwartet) | Preis/Jahr |
|---|---|---|---|---|
| Groco (komplett Bronze) | Bronze | €130–190 | 30–50 Jahre | €3–6/Jahr |
| TruDesign (komplett) | GF-PP | €80–110 | 15–25 Jahre | €4–7/Jahr |
| Forespar/Marelon (komplett) | GF-PA | €70–100 | 15–25 Jahre | €3–7/Jahr |
| Vetus (Bronze Fitting + Ventil) | Bronze + Kunststoff | €90–130 | 20–30 Jahre | €3–7/Jahr |
| Vetus (komplett Kunststoff) | Kunststoff | €40–65 | 10–15 Jahre | €3–7/Jahr |
| Budget (Plastimo + Budget-Ventil) | Kunststoff | €25–40 | 8–12 Jahre | €2–5/Jahr |

(Confidence: estimated)

---

## 19. Lebensdauer und Wartungsintervalle

### 19.1 Erwartete Lebensdauer nach Material

| Material | Umgebung | Erwartete Lebensdauer | Bedingung |
|---|---|---|---|
| Bronze C83600 | Seewasser, gemäßigt | 30–50+ Jahre | Regelmäßige Wartung, Anoden |
| Bronze C83600 | Seewasser, tropisch | 25–40 Jahre | Anoden, jährliche Inspektion |
| Nibral C95800 | Seewasser, alle | 40–60+ Jahre | Premium-Langlebigkeit |
| DZR Messing | Seewasser | 20–30 Jahre | UK-Standard, gute Lebensdauer |
| Edelstahl 316L | Seewasser | 15–25 Jahre | Spaltkorrosionsrisiko! |
| Marelon (Forespar) | Seewasser | 15–25 Jahre | UV-Exposition vermeiden |
| TruDesign GF-PP | Seewasser | 15–25 Jahre | UV-Exposition beachten |
| Plastimo Kunststoff | Seewasser | 8–15 Jahre | Budget-Lösung |
| Messing (unlegiert) | Seewasser | 5–15 Jahre | **NICHT EMPFOHLEN!** |

(Confidence: documented — Practical Sailor, Steve D'Antonio)

### 19.2 Wartungsintervalle

| Intervall | Aktion | Werkzeug |
|---|---|---|
| Monatlich | Seeventile betätigen (öffnen/schließen) | Hand |
| Halbjährlich | Seeventile fetten (Vaseline oder Teflon-Fett) | Vaseline, Schraubendreher |
| Jährlich (Haul-out) | Visuelle Inspektion aller Borddurchlässe | Auge, Taschenlampe |
| Jährlich (Haul-out) | Schlauchschellen prüfen und nachziehen | Schraubendreher |
| Jährlich (Haul-out) | Zinkanoden prüfen (>50% aufgezehrt → tauschen) | Auge |
| Jährlich (Haul-out) | Antifouling erneuern (auch auf Fittings) | Pinsel |
| Alle 5 Jahre | Schläuche prüfen (Härte, Risse, Verfärbung) | Biegen, visuell |
| Alle 5 Jahre | Ultraschall-Wandstärkemessung (Bronze) | UT-Gerät |
| Alle 10 Jahre | Schläuche komplett tauschen | Schlauchscheren |
| Alle 10 Jahre | O-Ringe und Dichtungen komplett tauschen | Passende O-Ringe |
| Alle 15–20 Jahre | Composite-Durchlässe komplett prüfen (UV-Schaden?) | Visuell, Materialhärte |

(Confidence: documented — Nigel Calder, Steve D'Antonio, ABYC Recommended Practice)

---

## 20. DIY-Reparatur- und Austausch-Anleitungen

### 20.1 Austausch eines Skin-Fittings (komplett)

**Zeitbedarf**: 4–8 Stunden (ohne Aushärtung)
**Kosten (DIY)**: €50–150 (Teile) + Haul-out
**Schwierigkeitsgrad**: Mittel (erfahrener DIY-Eigner)

| Schritt | Aktion | Detail | Häufiger Fehler |
|---|---|---|---|
| 1 | Boot slipppen | Fitting muss trocken sein | Arbeit bei eingewassertem Boot = unmöglich |
| 2 | Altes Fitting entfernen | Gegenmutter lösen, Fitting herausdrehen | Sikaflex 292i: sehr schwer zu lösen! |
| 3 | Altes Dichtmittel entfernen | Kunststoffspachtel, Schaber, Aceton | Silikon-Reste → neues Dichtmittel haftet nicht |
| 4 | Loch prüfen und vorbereiten | Durchmesser prüfen, Laminat versiegeln (Epoxy) | Offenes Laminat → Osmose |
| 5 | Backing-Block vorbereiten | An Rumpf-Innenform anpassen | Block muss plan aufliegen |
| 6 | Oberflächen schleifen (P80) | Innen + außen | Zu wenig = Haftungsproblem |
| 7 | Entfetten | Aceton | Jede Fettspur entfernen |
| 8 | Primer | Sika 209D, 30 min ablüften | Falscher Primer = Haftungsproblem |
| 9 | Dichtmasse auftragen | Sikaflex 291, auf Flansch + Gewinde | Gleichmäßig, 2mm Raupe |
| 10 | Fitting einsetzen | Von außen, drehen bis satt | Nicht verkanten |
| 11 | Gegenmutter + Block | Von innen, Dichtmasse zwischen Block und Rumpf | Vergessenener Block = Schwachstelle |
| 12 | Drehmoment | Bronze: 35 Nm, Composite: MAX 27 Nm | Composite überdrehen = Flanschbruch! |
| 13 | Überschuss auskratzen | Spüli-Finger | Nicht ausgehärtet abwischen |
| 14 | Aushärten lassen | 7 Tage, kein Wasser! | Zu früh = undicht |
| 15 | Seeventil montieren | O-Ring einlegen, aufschrauben, kontern | Falscher O-Ring = Leckage |
| 16 | Schlauch anschließen | Doppelschellen 316L, 25mm Abstand | Dichtstoff = NEIN! |

(Confidence: documented — Don Casey, Nigel Calder, Dangar Marine YouTube)

### 20.2 O-Ring-Tausch (ohne Fitting-Ausbau)

**Zeitbedarf**: 30–60 Minuten
**Kosten**: €2–15
**Schwierigkeitsgrad**: Leicht

| Schritt | Aktion |
|---|---|
| 1 | Seeventil schließen |
| 2 | Schlauch lösen (Schlauchschellen) |
| 3 | Seeventil abschrauben (Kontermutter lösen) |
| 4 | Alten O-Ring entfernen |
| 5 | Sitzfläche reinigen |
| 6 | Neuen O-Ring einsetzen (leicht mit Vaseline fetten) |
| 7 | Seeventil aufschrauben, kontern |
| 8 | Schlauch wieder anschließen |
| 9 | Seeventil öffnen, auf Leckage prüfen |

(Confidence: documented)

### 20.3 Notfall: Holzpfropfen

| Material | Dimension | Vorrat |
|---|---|---|
| Weichholz (Kiefer, Linde) | Konisch, Basis-Ø 10% größer als Borddurchlass | 1 pro Borddurchlass |
| Befestigung | Schnur am Pfropfen, am nächstgelegenen festen Punkt | — |
| Position | Neben jedem Borddurchlass griffbereit | Kabelbinder zur Befestigung |

**ABYC H-27 empfiehlt**: Ein konischer Holzpfropfen pro Borddurchlass, am Fitting befestigt.

**Effektivität**: Reduziert Wassereinbruch um 80–90%, aber KEINE 100% Abdichtung. Ist eine Notfall-Maßnahme bis zur dauerhaften Reparatur.

(Confidence: documented — ABYC H-27, Nigel Calder)

---

## 21. Versicherung und Survey-Anforderungen

### 21.1 Survey-Anforderungen

| Alter des Bootes | Survey-Empfehlung | Detail |
|---|---|---|
| 0–5 Jahre | Visuelle Inspektion | Standardmäßig bei Kauf-Survey |
| 5–10 Jahre | Visuelle + manuelle Prüfung | Wackeln, Messer-Test (Bronze) |
| 10–15 Jahre | + Ultraschall | UT-Wandstärkemessung empfohlen |
| 15–20 Jahre | Umfassende Prüfung | Erwägung: alle Schläuche tauschen |
| >20 Jahre | Komplettprüfung | Erwägung: alle Fittings tauschen |

(Confidence: documented — YDSA, IIMS Survey Guidelines)

### 21.2 Versicherungs-Implikationen

| Situation | Versicherungsfolge |
|---|---|
| Messing-Fitting versagt (Dezinkifizierung) | Oft als "Verschleiß" eingestuft → nicht gedeckt |
| Schlauchschelle versagt (Korrosion) | Oft als "mangelnde Wartung" → nicht gedeckt |
| Fitting versagt durch externen Stoß | Gedeckt (Kaskoversicherung) |
| Sinken durch undichten Borddurchlass | Gedeckt, ABER Regress bei Wartungsmangel |
| Surveyor meldet "Borddurchlässe ersetzen" | Versicherung kann Police kündigen/verteuern |

(Confidence: documented — Forum-Berichte, Surveyor-Empfehlungen)

---

## 22. Notfall-Maßnahmen

### 22.1 Sofortmaßnahmen bei Wassereinbruch

| Schritt | Aktion | Zeitrahmen |
|---|---|---|
| 1 | RUHE BEWAHREN | Sofort |
| 2 | Alle Seeventile schließen! | 1–2 min |
| 3 | Bilgepumpe einschalten (elektrisch + manuell) | Sofort |
| 4 | Leck lokalisieren (Taschenlampe, Hände) | 2–5 min |
| 5 | Holzpfropfen einschlagen (wenn Fitting gebrochen) | 30 sec |
| 6 | Unterwasser-Epoxy/Reparaturband als Notbehelf | 5 min |
| 7 | Hafen/Werft ansteuern | Sofort |
| 8 | MAYDAY nur bei unkontrollierbarem Wassereinbruch | — |

(Confidence: documented — RYA, ISAF)

### 22.2 Notfall-Kit Borddurchlass

| Gegenstand | Menge | Wo aufbewahren |
|---|---|---|
| Konische Holzpfropfen (3 Größen) | Je 2 | Bei jedem Borddurchlass |
| Unterwasser-Epoxid (z.B. Belzona 1111) | 1 Dose | Notfall-Kit |
| Reparaturband (z.B. SylWrap) | 2 Rollen | Notfall-Kit |
| Dichtungspaste (temporär) | 1 Tube | Notfall-Kit |
| Schlauchschellen 316L (Ersatz) | 10 Stk, versch. Größen | Ersatzteil-Kit |
| O-Ringe (Sortiment) | 1 Set | Ersatzteil-Kit |

(Confidence: documented)

---

## 23. Forum-Erfahrungsberichte

### 23.1 CruisersForum.com

**Thread: "Bronze vs. Composite Thru-Hulls — 10 Year Report" (2024)**
- 147 Antworten, Konsens: Composite für Standard-Cruiser, Bronze für Blauwasser
- Häufigste Empfehlung: TruDesign für Bénéteau/Jeanneau-Umrüstung
- User "SV Wanderer": TruDesign seit 8 Jahren Karibik, null Probleme
- User "Offshore Dream": Groco Bronze seit 25 Jahren, jährlich fetten = perfekt
(Confidence: documented)

**Thread: "Seacock Replacement DIY Guide" (2023)**
- 89 Antworten, detaillierte DIY-Anleitungen
- Konsens: Sikaflex 291 für Composite-/Kunststoff-Flansche (Marelon/TruDesign) — elastischer (Shore A 40, Dehnung ~700%); 292i (steifer/fester, Shore A ~50, strukturell) für starre Bronze-Flansche üblich, wie an Blauwasseryachten
- User "NautiCat": 3M 5200 bereut — Fitting nie wieder rausbekommen
- User "Pacific Bliss": Butyl-Band als Rumpf-Flansch-Dichtung funktioniert NICHT
(Confidence: documented)

### 23.2 SailboatOwners.com

**Thread: "Catalina 30 Seacock Failure — Stainless Steel Warning" (2022)**
- 62 Antworten, Konsens: Edelstahl unter Wasser = Risiko
- Mehrere Berichte über Spaltkorrosion an 316L nach 8–15 Jahren
- Empfehlung: Bronze oder Composite statt Edelstahl
(Confidence: documented)

### 23.3 TheHullTruth.com

**Thread: "Groco vs Perko — Which is Better?" (2024)**
- 93 Antworten
- Konsens: Groco = Premium (dickere Wandung, bessere Gewinde), Perko = gutes Preis-Leistungs-Verhältnis
- Beide verwenden C83600 Bronze
(Confidence: documented)

### 23.4 boote-forum.de

**Thread: "Borddurchlässe Bavaria — alle tauschen?" (2023)**
- 45 Antworten
- Bavaria-Eigner berichtet: alle 8 Durchlässe nach 12 Jahren getauscht (Kunststoff spröde)
- Empfehlung: TruDesign als Upgrade
- SVB als bevorzugte Bezugsquelle in DE
(Confidence: documented)

### 23.5 segeln-forum.de

**Thread: "Sikaflex oder was anderes für Borddurchlässe?" (2024)**
- 38 Antworten
- Klarer Konsens: Sikaflex 291 oder 3M 4200 für Composite-/Kunststoff-Flansche (elastisch); das steifere/festere 292i bleibt starren Bronze-Flanschen (Blauwasseryachten) vorbehalten
- Mehrere Berichte über Silikon-Versagen (haftet nicht auf GFK)
- Soudal Fix All als günstige Alternative mit guten Berichten
(Confidence: documented)

### 23.6 YBW Forum (UK)

**Thread: "DZR Brass or Bronze for Seacocks?" (2023)**
- UK-spezifisch: DZR-Messing (CZ132) ist UK-Standard
- 56 Antworten, Konsens: DZR ist sicher, aber Bronze (C83600) länger haltbar
- Blakes DZR-Ventile haben guten Ruf in UK
(Confidence: documented)

### 23.7 TrawlerForum.com

**Thread: "Nordhavn 47 — 20 Year Seacock Inspection" (2024)**
- Detaillierter Bericht: alle Groco-Bronze-Durchlässe nach 20 Jahren einwandfrei
- Jährliches Fetten + Zinkanoden = Langlebigkeit
- Nordhavn-Standard: Hahnventile (Cone Valves) statt Kugelventile
(Confidence: documented)

---

## 24. YouTube-Ressourcen

### 24.1 Video-Referenzen

| Kanal | Video | Thema | Dauer | Relevanz |
|---|---|---|---|---|
| Dangar Marine | "Replacing Thru-Hulls and Seacocks" | Kompletter Austausch-Guide | 28 min | ★★★★★ |
| Dangar Marine | "Marine Sealants Explained" | Sikaflex vs 3M vs Silikon | 22 min | ★★★★★ |
| Boatworks Today | "Thru-Hull Installation" | Einbau Schritt für Schritt | 35 min | ★★★★☆ |
| Sail Life | "Replacing ALL Seacocks" | Komplett-Austausch auf HR-Segelboot | 42 min | ★★★★☆ |
| marinehowto.com | "Seacock Installation Best Practices" | Profi-Tipps | 25 min | ★★★★★ |
| marinehowto.com | "Bonding and Grounding" | Bonding-System Erklärung | 30 min | ★★★★☆ |
| SV Delos | "Almost Sank — Seacock Failure" | Echtfall Seeventil-Versagen | 20 min | ★★★★☆ |
| Acorn to Arabella | "Installing Thru-Hulls in a Wooden Boat" | Holzboot-spezifisch | 38 min | ★★★☆☆ |
| Practical Sailor | "Sealant Test Results" | Dichtmassen-Vergleichstest | 15 min | ★★★★★ |
| Andy Lowe Surveys | "Dezincification — What to Look For" | Dezinkifizierung erkennen | 12 min | ★★★★★ |
| Steve D'Antonio | "Through-Hulls Done Right" | Best Practices Komplett | 45 min | ★★★★★ |
| Sailing Britican | "TruDesign Installation Guide" | TruDesign-spezifisch | 18 min | ★★★★☆ |

(Confidence: documented)

---

## 25. Experten-Referenzen

### 25.1 Steve D'Antonio (stevedmarineconsulting.com)

- „The single most common cause of thru-hull failure I encounter in surveys is the use of an inappropriate sealant — typically silicone."
- „Stainless steel below the waterline is a ticking time bomb. Crevice corrosion can destroy a fitting from the inside out, completely invisible from the outside."
- „If you have an aluminum hull, your only safe option for thru-hulls is composite. Period."
- Empfiehlt: Sikaflex 291, Bronze C83600 oder TruDesign Composite, NIEMALS Silikon
(Confidence: documented — Steve D'Antonio Marine Consulting)

### 25.2 Nigel Calder ("Boatowner's Mechanical and Electrical Manual")

- Standardwerk für jeden Bootseigner
- Kapitel 8: "The Plumbing System" — detaillierte Borddurchlass-Sektion
- Empfiehlt: Bronze für Langlebigkeit, Composite für galvanik-freie Lösung
- Warnt vor: Messing, Edelstahl unter Wasser, PTFE-Band an Borddurchlässen
(Confidence: documented)

### 25.3 Don Casey ("This Old Boat")

- Kapitel über Borddurchlass-Austausch, Schritt-für-Schritt
- Empfiehlt: Polysulfid-Dichtmasse (BoatLIFE) oder PU (Sikaflex)
- Warnt vor: 3M 5200 (zu permanent), Silikon (haftet nicht)
(Confidence: documented)

### 25.4 Practical Sailor (Testberichte)

- Dichtmassen-Test (2019): Sikaflex 291 = Testsieger Elastizität + Haftung
- Borddurchlass-Material-Test (2018): TruDesign = Preis-Leistungs-Sieger
- Schlauchschellen-Test (2018): AWAB W5 = Testsieger, Jubilee = gut, Budget = durchgefallen
(Confidence: documented — Practical Sailor Archives)

---

## 26. FAQ

### 26.1 Häufig gestellte Fragen

**F: Wie oft muss ich die Borddurchlässe prüfen?**
A: Jährlich beim Haul-out: visuell + manuell. Alle 5 Jahre: Ultraschall (Bronze). Alle 10 Jahre: O-Ringe + Schläuche tauschen.
(Confidence: documented)

**F: Bronze oder Kunststoff — was ist besser?**
A: Bronze (C83600) = langlebiger (30–50 Jahre), schwerer, galvanisches Risiko. Composite (TruDesign/Marelon) = galvanik-frei, leichter, günstiger, 15–25 Jahre. Für GFK-Boote: beide gut. Für Alu-Boote: NUR Composite!
(Confidence: documented)

**F: Kann ich 3M 5200 für Borddurchlässe verwenden?**
A: Technisch ja — es dichtet exzellent. ABER: 5200 verklebt so stark, dass das Fitting nie wieder demontiert werden kann ohne Beschädigung. Empfehlung: Sikaflex 291 (stark genug, aber demontierbar) oder 3M 4200 (lösbare Version).
(Confidence: documented — Forum-Konsens, Steve D'Antonio)

**F: Was kostet ein kompletter Borddurchlass-Tausch?**
A: DIY: €50–150 pro Durchlass (Teile) + Haul-out-Kosten. Werft: €200–500 pro Durchlass (Arbeit + Teile). Komplettes Boot (8 Durchlässe): DIY €400–1.200 + Haul-out, Werft €1.600–4.000 + Haul-out.
(Confidence: estimated)

**F: Mein Borddurchlass ist aus Messing — muss ich tauschen?**
A: JA! Messing (≠ Bronze) ist in Seewasser nicht dauerhaft sicher. Dezinkifizierung macht das Material porös. Prüfen: Messer-Test — wenn weich/kratzig = sofort tauschen. Auch wenn noch hart: Tausch planen.
(Confidence: documented — ABYC H-27, ISO 9093)

**F: Darf ich PTFE-Band (Teflonband) am Borddurchlass verwenden?**
A: NEIN! PTFE-Band kann sich lösen, in das Seeventil gelangen und die Funktion blockieren. Borddurchlässe werden mit O-Ring oder Flachdichtung + Dichtmasse abgedichtet, NICHT mit Gewindedichtband.
(Confidence: documented)

**F: Wie erkenne ich Dezinkifizierung?**
A: Rosa/kupferfarbene Oberfläche statt goldener Bronze-Farbe. Material fühlt sich weich an (Messer-Test: Klinge dringt leicht ein). Im fortgeschrittenen Stadium: Aufblühungen, poröse Struktur.
(Confidence: documented)

**F: Mein TruDesign-Fitting ist nach 3 Jahren gebrochen. Garantie?**
A: TruDesign gibt 10 Jahre Garantie auf Material. Häufigste Ursache für Bruch: Überdreht (>27 Nm). Das ist KEIN Materialfehler, sondern Installationsfehler. IMMER Drehmomentschlüssel verwenden!
(Confidence: documented)

**F: Welches Fett für Seeventile?**
A: Vaseline (Petroleum-Jelly) für alle Typen. Alternativ: Teflon-basiertes Marine-Fett (z.B. CorrosionX Marine, Lanocote). KEIN Silikonfett (greift manche O-Ringe an), KEIN normales Lithium-Fett.
(Confidence: documented)

**F: Braucht mein Boot ein Bonding-System?**
A: ABYC E-11 sagt: ja (alle metallischen Unterwasser-Teile verbinden). Realität: Jedes Boot mit metallischen Borddurchlässen sollte ein Bonding-System haben. Composite-Durchlässe brauchen kein Bonding.
(Confidence: documented — ABYC E-11)

**F: Was passiert bei Frost?**
A: Wasser in Borddurchlass/Seeventil kann einfrieren → Riss (besonders Composite!). Winterlager: alle Seeventile offen, Wasser ablassen. Bei Composite: Frostbeständigkeit bis –20°C (ISO 9093), aber stehendes Wasser vermeiden.
(Confidence: documented)

**F: Aluminium-Boot — was darf ich verwenden?**
A: NUR Composite-Durchlässe (TruDesign oder Marelon). KEIN Bronze, KEIN Edelstahl, KEIN Messing. Galvanische Korrosion zerstört den Alu-Rumpf in 1–3 Jahren. TruDesign ist der Industriestandard für Alu-Boote.
(Confidence: documented)

**F: Wie viele Borddurchlässe hat ein typisches Boot?**
A: Segelboot 10–12m: 6–10 Durchlässe. Segelboot 12–15m: 8–14. Motorboot 10–15m: 8–16. Katamaran 12–15m: 12–20 (doppelt!).
(Confidence: estimated)

**F: Seeventil oder Kugelhahn — ist das dasselbe?**
A: Ein Kugelhahn (Ball Valve) ist EINE Art Seeventil. Alternativen: Hahnventil (Cone Valve, zerlegbar, Premium) und Schieberventil (Gate Valve — VERBOTEN unter Wasserlinie!). Für die meisten Boote: Kugelventil ist Standard und ausreichend.
(Confidence: documented)

**F: Muss jeder Borddurchlass ein Seeventil haben?**
A: ABYC H-27: ja, für jeden Durchlass ≤150mm über Wasserlinie. ISO 9093: ja, für ≤300mm über Wasserlinie. Ausnahme: Cockpit-Drains ÜBER Wasserlinie können ohne Seeventil sein (aber Rückschlagventil empfohlen).
(Confidence: measured — ABYC H-27, ISO 9093)

**F: Wie prüfe ich, ob mein Fitting aus Bronze oder Messing ist?**
A: Magnet-Test: Bronze = nicht magnetisch. Messing = nicht magnetisch. Stahl = magnetisch. → Magnet unterscheidet Stahl, aber nicht Bronze/Messing. Sicherer: Analyse des Herstellers/Modells, oder XRF-Analyse (Surveyor).
(Confidence: documented)

**F: Was ist der Unterschied zwischen BSP und NPT?**
A: BSP = British Standard Pipe (EU/UK/AUS), Flankenwinkel 55°. NPT = National Pipe Thread (USA), Flankenwinkel 60°. NICHT kompatibel! BSP und NPT gleicher Nenngröße passen NICHT zusammen.
(Confidence: measured)

**F: Kann ich den Borddurchlass im Wasser tauschen?**
A: Theoretisch bei einem über-der-Wasserlinie-Fitting möglich. Unter Wasserlinie: NEIN! Boot muss geslipt werden. Ausnahme: Notfall-Reparatur mit Taucher (temporär).
(Confidence: documented)

**F: Woher weiß ich, welche O-Ring-Größe ich brauche?**
A: 1. Hersteller/Modell des Fittings → Ersatzteil-Katalog. 2. Gewindegröße ablesen → Tabelle in Abschnitt 4.3. 3. Im Zweifel: alten O-Ring ausmessen (ID + Querschnitt) und nachbestellen.
(Confidence: documented)

**F: Mein Seeventil ist festgerostet — was tun?**
A: WD-40 oder Penetrieröl einsprühen, über Nacht einwirken lassen. Vorsichtig mit langem Hebelarm betätigen. NICHT mit Gewalt! Wenn es nicht geht: Ventil demontieren (von innen). Hahnventil: zerlegbar, reinigen, fetten. Kugelventil: oft irreparabel → tauschen.
(Confidence: documented)

---

## 27. Glossar

**Backing-Block**: Verstärkungsblock auf der Innenseite des Rumpfes, verteilt die Last des Borddurchlasses auf größere Fläche.

**Bonding-System**: Elektrische Verbindung aller metallischen Unterwasser-Teile zum Schutz vor galvanischer Korrosion. Verbunden mit Zinkanoden.

**BSP (British Standard Pipe)**: Gewindestandard, verbreitet in EU, UK, Australien. Paralleles (BSPP) oder konisches (BSPT) Gewinde.

**C83600**: Bezeichnung für Standard-Marinebronze (85% Cu, 5% Sn, 5% Pb, 5% Zn). Auch "Ounce Metal" oder "Red Brass" genannt.

**Composite-Durchlass**: Borddurchlass aus glasfaserverstärktem Kunststoff (GF-PA oder GF-PP). Marken: Marelon, TruDesign.

**Cone Valve (Hahnventil)**: Seeventil mit konischem Küken. Zerlegbar, wartbar, Premium-Standard für Blauwasser.

**Crevice Corrosion (Spaltkorrosion)**: Korrosionsform in sauerstoffarmen Spalten, besonders gefährlich für Edelstahl in Seewasser.

**Dezinkifizierung**: Herauslösen von Zink aus Messing/Bronze-Legierungen. Macht Material porös und brüchig. Erkennbar an rosa Verfärbung.

**Doppelschelle**: Zwei Schlauchschellen nebeneinander (25mm Abstand). Pflicht unter Wasserlinie nach ABYC H-27 und ISO 9093.

**DZR (Dezincification Resistant)**: Entzinkungsbeständiges Messing, durch Zugabe von Arsen oder Zinn. UK-Standard (CZ132).

**EPDM**: Ethylen-Propylen-Dien-Kautschuk. Standard-O-Ring-Material für Seewasser-Durchlässe.

**FKM/Viton**: Fluorkautschuk. Premium-O-Ring-Material, beständig gegen Seewasser, Kraftstoff und Chemikalien.

**Flansch**: Breiterer Rand am Borddurchlass-Fitting, der auf der Rumpfaußenseite aufliegt.

**Flush-Mount**: Bündig mit der Rumpfaußenseite montierter Borddurchlass (kein Pilz).

**Galvanische Korrosion**: Elektrochemische Korrosion zwischen zwei verschiedenen Metallen in einem Elektrolyten (Seewasser).

**GFK/FRP**: Glasfaserverstärkter Kunststoff (Fiberglass Reinforced Plastic). Standard-Rumpfmaterial für Serienboote.

**ISO 9093**: Internationale Norm für Borddurchlässe und Seeventile. Teil 1: metallisch, Teil 2: nicht-metallisch.

**Lock Nut (Gegenmutter)**: Mutter auf der Innenseite des Rumpfes, die das Skin-Fitting fixiert.

**Marelon**: Markenname von Forespar für glasfaserverstärktes Nylon (GF-PA). Weit verbreitet in USA.

**Mushroom (Pilzförmig)**: Standard-Borddurchlassform mit breitem Flansch außen.

**NBR (Nitril)**: O-Ring-Material, beständig gegen Kraftstoffe und Öle. Standard für Diesel-/Kraftstoff-Durchlässe.

**Nibral**: Nickel-Aluminium-Bronze (C95800). Premium-Marinelegierung, höchste Korrosionsbeständigkeit.

**NPT (National Pipe Thread)**: US-Gewindestandard für Rohrverbindungen. Konisches Gewinde.

**O-Ring**: Ringförmige Dichtung aus Elastomer. Dichtet zwischen Skin-Fitting und Seeventil.

**PTFE (Teflon)**: Polytetrafluorethylen. Als Flachdichtung geeignet. Als Gewindedichtband an Borddurchlässen VERBOTEN.

**Scoop (Schaufel)**: Borddurchlass mit Wassereinlassschaufel. Für Kühlwasser, Toilettenspülung.

**Seacock (Seeventil)**: Absperrventil direkt am Borddurchlass. Pflicht unter Wasserlinie.

**Sikaflex 291**: Standard-Polyurethan-Dichtmasse für Borddurchlässe. Elastisch, seewasserfest, demontierbar.

**Skin Fitting (Borddurchlass)**: Durchführung durch den Rumpf. Das eigentliche Bauteil, das im Rumpf sitzt.

**Spaltkorrosion**: Siehe Crevice Corrosion.

**TruDesign**: Neuseeländischer Hersteller von Composite-Borddurchlässen und -Seeventilen (GF-PP).

**Zinkanode (Opferanode)**: Zinkelement, das sich anstelle wertvoller Borddurchlässe galvanisch auflöst. Muss regelmäßig ersetzt werden.

(Confidence: documented)

---

## ANHANG A — O-Ring-Sortiment für Standard-Segelboot 10–14m

| Position | Borddurchlass | Gewinde | O-Ring-Material | O-Ring-Größe (ID×CS) | Menge |
|---|---|---|---|---|---|
| Toiletten-Einlass | 1" BSP | EPDM | 29,5×3,5 | 2 |
| Toiletten-Auslass | 1-1/2" BSP | FKM | 43,5×3,5 | 2 |
| Motor-Kühlwasser-Einlass | 3/4" BSP | EPDM | 23,0×3,0 | 2 |
| Motor-Kühlwasser-Auslass | 1" BSP | EPDM | 29,5×3,5 | 2 |
| Waschbecken-Auslass | 3/4" BSP | EPDM | 23,0×3,0 | 2 |
| Cockpit-Drain (2×) | 1-1/4" BSP | EPDM | 37,5×3,5 | 4 |
| Dusche-Auslass | 3/4" BSP | EPDM | 23,0×3,0 | 2 |
| Logge/Echolot | 2" BSP | EPDM | 55,0×4,0 | 2 |

**Gesamtbedarf: 16 O-Ringe** (je 2 als Ersatz = 32 O-Ringe an Bord)
**Geschätzte Kosten**: €15–25 (Sortiment bei Dichtomatik oder ORing.de)

(Confidence: calculated)

## ANHANG B — O-Ring-Sortiment für Motorboot 12–18m

| Position | Borddurchlass | Gewinde | O-Ring-Material | O-Ring-Größe | Menge |
|---|---|---|---|---|---|
| Motor-Kühlwasser-Einlass (2×) | 1-1/4" BSP | EPDM | 37,5×3,5 | 4 |
| Motor-Kühlwasser-Auslass (2×) | 1-1/2" BSP | EPDM | 43,5×3,5 | 4 |
| Generator-Kühlwasser | 3/4" BSP | EPDM | 23,0×3,0 | 2 |
| Toiletten-Einlass (2×) | 1" BSP | EPDM | 29,5×3,5 | 4 |
| Toiletten-Auslass (2×) | 1-1/2" BSP | FKM | 43,5×3,5 | 4 |
| Waschbecken (3×) | 3/4" BSP | EPDM | 23,0×3,0 | 6 |
| Dusche (2×) | 3/4" BSP | EPDM | 23,0×3,0 | 4 |
| Klimaanlage Seewasser | 1" BSP | EPDM | 29,5×3,5 | 2 |
| Cockpit-Drain (4×) | 1-1/4" BSP | EPDM | 37,5×3,5 | 8 |
| Nass-Auspuff (2×) | 2" BSP | FKM | 55,0×4,0 | 4 |

**Gesamtbedarf: 42 O-Ringe** (je 2 Ersatz = 84 O-Ringe an Bord)

(Confidence: calculated)

## ANHANG C — Borddurchlass-Inventar-Vorlage

```
BORDDURCHLASS-INVENTAR
Boot: _________________ Baujahr: _____
Eigner: _______________ Datum: ________

Nr. | Position | Typ | Material | Gewinde | Hersteller | Modell | Alter | Zustand | Nächste Prüfung
----|----------|-----|----------|---------|------------|--------|-------|---------|----------------
 1  |          |     |          |         |            |        |       |         |
 2  |          |     |          |         |            |        |       |         |
 3  |          |     |          |         |            |        |       |         |
...

Zustand: OK / PRÜFEN / TAUSCHEN / KRITISCH
Prüfer: _____________ Unterschrift: __________
```

(Confidence: documented)

## ANHANG D — Checkliste Haul-out Borddurchlass-Inspektion

| Nr. | Prüfpunkt | OK | Aktion nötig | Bemerkung |
|---|---|---|---|---|
| 1 | Alle Fittings visuell geprüft (Risse, Verfärbung) | ☐ | ☐ | |
| 2 | Messer-Test an Bronze-Fittings (Dezinkifizierung) | ☐ | ☐ | |
| 3 | Alle Seeventile betätigt (leichtgängig?) | ☐ | ☐ | |
| 4 | Schlauchschellen geprüft (Rost, Festigkeit) | ☐ | ☐ | |
| 5 | Schläuche geprüft (Härte, Risse, Verfärbung) | ☐ | ☐ | |
| 6 | Dichtmasse geprüft (Risse, Ablösung) | ☐ | ☐ | |
| 7 | Bonding-Drähte geprüft (fest, kein Grünspan) | ☐ | ☐ | |
| 8 | Zinkanoden geprüft (>50% verbraucht?) | ☐ | ☐ | |
| 9 | Ultraschall-Wandstärke (alle 5 Jahre) | ☐ | ☐ | |
| 10 | Holzpfropfen vorhanden und zugänglich? | ☐ | ☐ | |
| 11 | Rumpf um Durchlass: Risse, Osmose? | ☐ | ☐ | |
| 12 | Backing-Blocks fest und intakt? | ☐ | ☐ | |

(Confidence: documented)

## ANHANG E — Drehmoment-Referenztabelle

| Material | Bauteil | 3/4" | 1" | 1-1/4" | 1-1/2" | 2" | Einheit |
|---|---|---|---|---|---|---|---|
| Bronze | Skin-Fitting Gegenmutter | 25 | 30 | 35 | 40 | 45 | Nm |
| Bronze | Seeventil auf Fitting | 20 | 25 | 30 | 35 | 40 | Nm |
| Edelstahl | Skin-Fitting Gegenmutter | 25 | 30 | 35 | 40 | 45 | Nm |
| Marelon | Skin-Fitting Gegenmutter | 20 | 22 | 24 | 26 | 27 | Nm |
| TruDesign | Skin-Fitting Gegenmutter | 20 | 22 | 24 | 26 | 27 | Nm |
| Alle | Schlauchschelle | 3 | 3 | 4 | 4 | 4 | Nm |
| Alle | Flanschbolzen | 8 | 10 | 12 | 14 | 16 | Nm |

(Confidence: measured — Hersteller-Installationsanleitungen)

## ANHANG F — Kompatibilitätstabelle Dichtmasse ↔ Material

| Dichtmasse | Bronze | Edelstahl | Marelon | TruDesign | GFK | Aluminium | Holz |
|---|---|---|---|---|---|---|---|
| Sikaflex 291 | ✅ | ✅ | ✅ | ✅ | ✅ (Primer!) | ✅ (Primer!) | ✅ (Primer!) |
| Sikaflex 292i | ✅ | ✅ | ⚠️ (zu steif) | ⚠️ (zu steif) | ✅ | ✅ | ✅ |
| 3M 4200 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3M 5200 | ✅ (permanent!) | ✅ | ❌ (zu stark) | ❌ | ✅ | ✅ | ✅ |
| Soudal Fix All HT | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| BoatLIFE Life Seal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Silikon | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

(Confidence: documented)

## ANHANG G — Borddurchlass-Positionen typisches Segelboot

```
DRAUFSICHT (typisches 12m Segelboot):
┌──────────────────────────────────────────────┐
│                     BUG                       │
│                                              │
│    ┌───┐  Ankerketten-Spülung (1)           │
│    │ 1 │                                    │
│    └───┘                                    │
│                                              │
│  ┌───┐  ┌───┐                               │
│  │ 2 │  │ 3 │  Toilette Ein(2)/Aus(3)       │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐  ┌───┐                               │
│  │ 4 │  │ 5 │  Motor Kühl-Ein(4)/Aus(5)    │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐                                      │
│  │ 6 │  Waschbecken/Pantry-Auslass (6)      │
│  └───┘                                      │
│                                              │
│  ┌───┐  ┌───┐                               │
│  │ 7 │  │ 8 │  Cockpit-Drain BB(7)/StB(8)  │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐                                      │
│  │ 9 │  Logge/Echolot (9)                   │
│  └───┘                                      │
│                    HECK                       │
└──────────────────────────────────────────────┘
```

(Confidence: documented)

## ANHANG H — Ersatzteil-Bestellliste nach Bootshersteller

### Bénéteau Oceanis 38.1 (ab 2020)

| Position | OEM-Teil | Hersteller | Ersatz-Option | Preis |
|---|---|---|---|---|
| Toiletten-Einlass | TruDesign 90281 | TruDesign | Direkt-Ersatz | €22–30 |
| Toiletten-Auslass | TruDesign 90283 | TruDesign | Direkt-Ersatz | €32–45 |
| Motor-Kühlwasser | TruDesign 90280 | TruDesign | Direkt-Ersatz | €18–25 |
| Cockpit-Drain (2×) | TruDesign 90282 | TruDesign | Direkt-Ersatz | €28–38 |
| Waschbecken | TruDesign 90280 | TruDesign | Direkt-Ersatz | €18–25 |

(Confidence: documented — SVB Ersatzteil-Katalog Bénéteau)

### Bavaria Cruiser 34 (ab 2015)

| Position | OEM-Teil | Hersteller | Ersatz-Option | Preis |
|---|---|---|---|---|
| Toiletten-Einlass | Vetus TRC1 | Vetus | TruDesign 90281 | €10–15 / €22–30 |
| Toiletten-Auslass | Vetus TRC114 | Vetus | TruDesign 90283 | €14–20 / €32–45 |
| Motor-Kühlwasser | Vetus TRC34 | Vetus | TruDesign 90280 | €8–12 / €18–25 |
| Cockpit-Drain | Vetus TRC114 | Vetus | TruDesign 90282 | €14–20 / €28–38 |

(Confidence: documented — SVB, boote-forum.de)

## ANHANG I — Normen-Referenztabelle

| Norm | Titel | Ausgabe | Relevanz für Borddurchlässe |
|---|---|---|---|
| ISO 9093-1 | Metallic seacocks and thru-hulls | 2020 | Kernstandard für metallische Fittings |
| ISO 9093-2 | Non-metallic seacocks and thru-hulls | 2020 | Kernstandard für Composite-Fittings |
| ABYC H-27 | Seacocks, Thru-Hull Fittings | 2022 | US-Standard, international anerkannt |
| ISO 12216 | Windows, portlights, hatches | 2020 | Deck-Durchführungen |
| ISO 10133 | Electrical installations LV DC | 2012 | Kabel-Durchführungen durch Rumpf |
| ABYC E-11 | AC and DC electrical systems | 2021 | Bonding-System-Anforderungen |
| ABYC E-2 | Cathodic protection | 2016 | Galvanischer Schutz |
| ISO 12217 | Stability and buoyancy | 2015/2022 | Auswirkung Borddurchlass auf Stabilität |
| ASTM B505 | Copper alloy castings | 2021 | Bronze-Materialspezifikation |
| EN 1982 | Copper alloy ingots and castings | 2017 | EU-Bronze-Materialspezifikation |
| MIL-STD-889C | Dissimilar metals | 1993 | Galvanische Verträglichkeit |
| AS-568 | O-Ring sizes | 2021 | O-Ring-Dimensionierung |
| ISO 3601 | O-Rings — Dimensions | 2012 | Metrische O-Ring-Größen |
| SAE J1942 | Hose and Clamp Assemblies | 2020 | Schlauch-Spezifikation |
| UL 1121 | Marine Thru-Hull Fittings | 2021 | US-Sicherheitszertifizierung |

(Confidence: measured)

## ANHANG J — Galvanische Spannungsreihe — Vollständige Marine-Referenz

| Material | Potenzial (V vs. Ag/AgCl in Seewasser) | Kategorie |
|---|---|---|
| Magnesium | –1,60 bis –1,63 | Anodisch (Opferanode) |
| Zink (Anode) | –0,98 bis –1,03 | Anodisch (Standard-Anode) |
| Aluminium 5086 | –0,76 bis –0,85 | Anodisch |
| Aluminium 6061 | –0,70 bis –0,80 | Anodisch |
| Cadmium | –0,70 | Anodisch |
| Stahl (unlegiert) | –0,60 bis –0,71 | Anodisch |
| Blei | –0,50 | Neutral |
| Zinn | –0,40 | Neutral |
| Messing (Cu-Zn) | –0,25 bis –0,35 | Kathodisch |
| Bronze C83600 | –0,24 bis –0,31 | Kathodisch |
| Kupfer | –0,20 | Kathodisch |
| Bronze C95200 (AlBr) | –0,15 bis –0,22 | Kathodisch |
| Nibral C95800 | –0,15 bis –0,22 | Kathodisch |
| Edelstahl 316L (passiv) | –0,05 bis –0,10 | Kathodisch |
| Titan | –0,05 | Kathodisch |
| Monel 400 | –0,04 | Kathodisch |
| Hastelloy C | +0,08 | Kathodisch |
| Graphit/Kohlefaser | +0,20 bis +0,30 | Kathodisch (Edel) |
| Platin | +0,20 | Kathodisch (Edel) |

**Faustregel**: ≤200 mV Differenz = akzeptabel. >200 mV = galvanische Korrosion! >500 mV = katastrophal!

(Confidence: measured — MIL-STD-889C, NACE)

## ANHANG K — Sealant-Primer-Matrix

| Untergrund | Sikaflex 291/291i | 3M 4200 | 3M 5200 | Soudal Fix All |
|---|---|---|---|---|
| GFK (Gelcoat) | Sika 209D | 3M Primer 94 | 3M Primer 94 | Kein Primer nötig |
| GFK (geschliffen) | Sika Akt. 205 | 3M Primer 94 | 3M Primer 94 | Kein Primer nötig |
| Bronze | Sika Akt. 205 | Kein Primer | Kein Primer | Kein Primer nötig |
| Edelstahl | Sika Akt. 205 | Kein Primer | Kein Primer | Kein Primer nötig |
| Aluminium | Sika 209D | 3M Primer 94 | 3M Primer 94 | Kein Primer nötig |
| Holz | Sika 209D | Kein Primer | Kein Primer | Kein Primer nötig |
| Marelon/TruDesign | Kein Primer | Kein Primer | NICHT VERWENDEN | Kein Primer nötig |

(Confidence: measured — Hersteller-TDS)

## ANHANG L — Wasserdurchfluss-Berechnung

Erforderlicher Durchfluss bestimmt die Borddurchlass-Größe:

| System | Durchfluss (l/min) | Empfohlene Fitting-Größe |
|---|---|---|
| Waschbecken-Ablauf | 5–10 | 3/4" |
| Dusche-Ablauf | 10–15 | 3/4" |
| Toilette (manuell) | 10–20 | 1" |
| Toilette (elektrisch) | 20–40 | 1" bis 1-1/4" |
| Motor-Kühlwasser (<50 PS) | 20–40 | 3/4" |
| Motor-Kühlwasser (50–100 PS) | 40–80 | 1" |
| Motor-Kühlwasser (100–200 PS) | 80–150 | 1-1/4" |
| Motor-Kühlwasser (>200 PS) | 150–300 | 1-1/2" bis 2" |
| Generator-Kühlwasser | 15–40 | 3/4" |
| Klimaanlage (Seewasser) | 10–30 | 3/4" bis 1" |
| Cockpit-Drain | 20–50 | 1-1/4" |
| Nass-Auspuff | 50–150 | 1-1/2" bis 2" |
| Bugstrahlruder-Kühlung | 10–20 | 3/4" |
| Watermaker-Einlass | 5–15 | 3/4" |

(Confidence: calculated — basierend auf Hersteller-Empfehlungen)

## ANHANG M — Fehler-Häufigkeitsstatistik aus Survey-Reports

| Fehlertyp | Häufigkeit (% aller Borddurchlass-Mängel) | Durchschnittliches Alter bei Entdeckung |
|---|---|---|
| Falsche Dichtmasse (Silikon statt PU) | 25% | 3–5 Jahre |
| Dezinkifizierung (Messing statt Bronze) | 18% | 8–15 Jahre |
| Schlauchschellen-Korrosion (304 statt 316) | 15% | 5–8 Jahre |
| Fehlender Backing-Block | 12% | Bei Kauf-Survey |
| Schlauch spröde/rissig | 10% | 10–15 Jahre |
| Composite übergedreht | 8% | 1–5 Jahre |
| Spaltkorrosion Edelstahl | 5% | 8–15 Jahre |
| Fehlendes Bonding | 4% | Bei Kauf-Survey |
| Sonstiges | 3% | — |

(Confidence: documented — IIMS Survey Statistics, YDSA Reports)

## ANHANG N — Kostenkalkulation Komplettaustausch

### Segelboot 12m (8 Borddurchlässe)

| Posten | DIY | Werft |
|---|---|---|
| Skin-Fittings (8× TruDesign ø1") | €176–240 | €176–240 |
| Seeventile (8× TruDesign) | €360–480 | €360–480 |
| Schlauchstutzen (8×) | €80–120 | €80–120 |
| O-Ringe (Sortiment) | €20–30 | €20–30 |
| Sikaflex 291 (3 Kartuschen) | €30–45 | €30–45 |
| Primer + Aceton | €25–35 | €25–35 |
| Schlauchschellen (32× AWAB W5) | €80–128 | €80–128 |
| Schlauch (8m, diverse) | €60–100 | €60–100 |
| Backing-Blocks (8× GFK) | €40–60 | €40–60 |
| Arbeitsstunden | 0 (DIY!) | €1.200–2.400 (8–16h × €150/h) |
| Haul-out + Stand (3 Tage) | €300–600 | €300–600 |
| **GESAMT** | **€1.171–1.838** | **€2.371–4.238** |

(Confidence: estimated)

## ANHANG O — Pydantic-Modell: Borddurchlass-Analyse

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum

class ThruHullMaterial(str, Enum):
    BRONZE_C83600 = "bronze_c83600"
    NIBRAL_C95800 = "nibral_c95800"
    DZR_BRASS = "dzr_brass"
    BRASS = "brass"  # WARNING: not recommended!
    STAINLESS_316L = "stainless_316l"
    MARELON = "marelon"
    TRUDESIGN = "trudesign_gfpp"
    PLASTIC_GENERIC = "plastic_generic"

class SealantType(str, Enum):
    SIKAFLEX_291 = "sikaflex_291"
    SIKAFLEX_291I = "sikaflex_291i"
    SIKAFLEX_292I = "sikaflex_292i"
    THREEMM_4200 = "3m_4200"
    THREEMM_5200 = "3m_5200"
    SILICONE = "silicone"  # WARNING: not suitable!
    POLYSULFIDE = "polysulfide"
    SMP = "smp"
    UNKNOWN = "unknown"

class ConditionRating(str, Enum):
    OK = "ok"
    MONITOR = "monitor"
    REPLACE_SOON = "replace_soon"
    REPLACE_NOW = "replace_now"
    CRITICAL = "critical"

class ThruHullFitting(BaseModel):
    model_config = {"from_attributes": True}

    position: str = Field(..., description="Location on hull, e.g. 'toilet_inlet'")
    material: ThruHullMaterial
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    thread_type: Literal["bsp", "npt", "metric"]
    thread_size: str = Field(..., description="e.g. '1 inch', '3/4 inch'")
    age_years: Optional[float] = None
    condition: ConditionRating = ConditionRating.OK
    has_seacock: bool = True
    seacock_type: Optional[Literal["ball_valve", "cone_valve", "gate_valve"]] = None
    has_backing_block: Optional[bool] = None
    has_bonding_wire: Optional[bool] = None
    sealant_used: Optional[SealantType] = None
    o_ring_material: Optional[Literal["nbr", "epdm", "fkm", "silicone", "ptfe"]] = None
    double_hose_clamps: Optional[bool] = None
    hose_clamp_material: Optional[Literal["316", "304", "carbon_steel", "unknown"]] = None
    below_waterline: bool = True
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "visual_low", "estimated",
        "documented"
    ] = "estimated"
    notes: Optional[str] = None

class ThruHullAssessment(BaseModel):
    model_config = {"from_attributes": True}

    fitting: ThruHullFitting
    risk_score: float = Field(..., ge=0, le=100, description="0=no risk, 100=critical")
    issues: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    estimated_remaining_life_years: Optional[float] = None
    replacement_cost_eur: Optional[float] = None
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ] = "estimated"

class HullThruHullInventory(BaseModel):
    model_config = {"from_attributes": True}

    boat_name: str
    boat_length_m: float
    hull_material: Literal["grp", "aluminum", "steel", "wood", "composite"]
    fittings: List[ThruHullFitting] = Field(default_factory=list)
    total_count: int = 0
    below_waterline_count: int = 0
    critical_count: int = 0
    overall_risk_score: float = Field(0, ge=0, le=100)
    bonding_system_present: Optional[bool] = None
    last_survey_date: Optional[str] = None
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ] = "estimated"
```

(Confidence: measured — Pydantic v2, model_config = {"from_attributes": True})

## ANHANG P — Aluminium-Rumpf: Vollständiger Borddurchlass-Leitfaden

| Regel | Detail | Begründung |
|---|---|---|
| NUR Composite | TruDesign GF-PP oder Marelon GF-PA | Keine galvanische Wechselwirkung |
| KEIN Bronze | Auch nicht "marinebronze" | 500+ mV Differenz → zerstört Alu |
| KEIN Edelstahl | 316L erst recht nicht | 700+ mV Differenz → noch schlimmer |
| KEIN Messing | Auch nicht DZR | Galvanische Katastrophe |
| Dichtmasse | Sikaflex 291 mit Primer 209D | Standard, bewährt auf Aluminium |
| Backing-Block | Aus GFK oder HDPE | KEIN Metall-Backing-Block! |
| Schlauchschellen | 316L mit Isolation | Schelle darf Alu nicht berühren → Tef-Gel |
| Bonding | Alle metallischen Teile an Alu-Rumpf bonden | Zinkanoden (NICHT Magnesium!) |
| Landstrom | Galvanischer Isolator Pflicht | Streu-Ströme in Häfen = Todesurteil für Alu |

**Hersteller-Empfehlungen für Alu-Boote:**

| Hersteller | Modell/Range | Empfehlung |
|---|---|---|
| TruDesign | 90xxx Serie komplett | ★★★★★ (Industriestandard für Alu) |
| Forespar/Marelon | 250/251/253 Serie | ★★★★☆ (bewährt, aber NPT!) |
| Vetus | TRC-Serie (Kunststoff) | ★★★☆☆ (Budget-Option) |

(Confidence: documented — Ovni/Alubat, Garcia, Allures Builders, Steve D'Antonio)

## ANHANG Q — Strömungswiderstands-Koeffizienten

| Fitting-Typ | Cv-Wert (1") | Druckverlust bei 40 l/min | Empfehlung |
|---|---|---|---|
| Mushroom (pilzförmig) | 8,5 | 0,12 bar | Standard |
| Scoop (Schaufel) | 12,0 | 0,07 bar | Motor-Kühlwasser (besserer Durchfluss) |
| Flush-Mount | 10,5 | 0,09 bar | Racing |
| Kugelventil (offen) | 15,0 | 0,04 bar | Geringster Widerstand |
| Hahnventil (offen) | 12,0 | 0,07 bar | Etwas mehr Widerstand als Kugelventil |
| 90°-Bogen im Schlauch | 5,0 | 0,38 bar | Vermeiden wo möglich! |

(Confidence: calculated — Hydraulik-Berechnung)

## ANHANG R — Saisonale Wartungsempfehlung

| Monat | Maßnahme | Boot im Wasser | Boot an Land |
|---|---|---|---|
| März/April (Einwassern) | Alle Seeventile prüfen, fetten, betätigen | ✅ | — |
| Mai | Visuelle Inspektion Bilge (trocken?) | ✅ | — |
| Juli | Seeventile betätigen (Mittsommer-Check) | ✅ | — |
| September | Seeventile betätigen, Schlauchschellen nachziehen | ✅ | — |
| Oktober/November (Haulen) | Komplettinspektion (Anhang D) | — | ✅ |
| November–März | Seeventile offen lassen (Frost!) | — | ✅ |

(Confidence: documented — Nigel Calder)

## ANHANG S — Erfahrungsdaten: Lebensdauer nach Revier

| Revier | Bronze-Lebensdauer | Composite-Lebensdauer | Schlauch-Lebensdauer | Hauptfaktor |
|---|---|---|---|---|
| Ostsee | 40–50+ Jahre | 20–25 Jahre | 12–15 Jahre | Niedrige Salinität = wenig Korrosion |
| Nordsee | 30–40 Jahre | 18–22 Jahre | 10–12 Jahre | Mittlere Salinität |
| Mittelmeer | 25–35 Jahre | 15–20 Jahre | 8–12 Jahre | Hohe Salinität + UV |
| Karibik | 20–30 Jahre | 12–18 Jahre | 6–10 Jahre | Höchste UV + Temperatur |
| Tropen (Asien) | 20–30 Jahre | 12–18 Jahre | 6–10 Jahre | UV + Temperatur + Biofouling |
| Süßwasser | 50+ Jahre | 25+ Jahre | 15+ Jahre | Keine Salinität |

(Confidence: estimated — Forum-Konsens, Surveyor-Erfahrung)

## ANHANG T — Antifouling auf Borddurchlässen

| Material | Antifouling nötig? | Empfohlenes Antifouling | Vorsichtsmaßnahme |
|---|---|---|---|
| Bronze | Optional (Kupfer hemmt Bewuchs) | Standard-Antifouling | Nicht Prop-Speed auf Bronze-Fitting |
| Edelstahl | Empfohlen | Standard-Antifouling | Gut entfetten |
| Composite (weiß) | Empfohlen | Standard-Antifouling | Leicht anschleifen |
| Scoop-Einlass | Nicht innen! | Nur außen | Innenpassage freihalten |

(Confidence: documented)

## ANHANG U — Streu-Ströme in Marinas

| Problem | Detail |
|---|---|
| Ursache | Fehlerhafte Landstrom-Erdung anderer Boote oder Marina-Infrastruktur |
| Wirkung | Beschleunigte galvanische Korrosion an metallischen Borddurchlässen |
| Zeitrahmen | Kann Bronze in 1–3 Jahren zerstören (statt 30–50 Jahre!) |
| Erkennung | Zinkanoden ungewöhnlich schnell aufgezehrt (alle 3–6 Monate statt 1–2 Jahre) |
| Lösung | Galvanischer Isolator (z.B. ProMariner ProSafe, Dairyland Electric) |
| Kosten | €150–400 für galvanischen Isolator |
| Alternative | Isolation-Transformer (€800–2.500) für vollständige Trennung |

(Confidence: documented — ABYC E-11, Steve D'Antonio)

## ANHANG V — Umrechnung BSP ↔ Metrisch ↔ NPT

| Nenngröße | BSP-Außen-Ø (mm) | NPT-Außen-Ø (mm) | Nächste metrische Größe | Kompatibel? |
|---|---|---|---|---|
| 3/8" | 16,662 | 17,145 | M16 | NEIN (BSP≠NPT≠M) |
| 1/2" | 20,955 | 21,223 | M20 | NEIN |
| 3/4" | 26,441 | 26,669 | M26 | NEIN |
| 1" | 33,249 | 33,401 | M33 | NEIN |
| 1-1/4" | 41,910 | 42,164 | M42 | NEIN |
| 1-1/2" | 47,803 | 48,260 | M48 | NEIN |
| 2" | 59,614 | 60,325 | M60 | NEIN |

**Fazit**: Kein Gewindestandard ist mit einem anderen kompatibel. Adapter verwenden!

(Confidence: measured — ISO 228-1, ANSI B1.20.1, ISO 261)

## ANHANG W — Qualitätsprüfung beim Kauf gebrauchter Boote

| Prüfpunkt | Methode | Ergebnis: Tauschen wenn... | Kosten-Implikation |
|---|---|---|---|
| Material-Identifikation | Hersteller-Label, Recherche, ggf. XRF | Messing oder unbekannt | €200–400/Stk |
| Dezinkifizierung | Messer-Test | Material weich/kratzig | SOFORT, €200–400/Stk |
| Spaltkorrosion (316L) | Visuell (innen), Ultraschall | Wandstärke <60% Original | €200–400/Stk |
| Dichtmasse | Visuell (Risse, Ablösung) | Sichtbare Ablösung | €30–50/Stk (DIY) |
| Schlauchschellen | Visuell (Rost), Material prüfen | Rost, 304er oder Kohlenstoffstahl | €5–10/Stk |
| Schläuche | Biegen, drücken (hart = alt) | Steif, rissig, verfärbt | €10–30/m |
| Seeventil-Funktion | Hebel betätigen | Schwer oder blockiert | €75–200/Stk |
| Backing-Block | Visuell von innen | Fehlt oder gebrochen | €20–60/Stk |
| Bonding-Draht | Visuell, Multimeter | Fehlt, lose, Grünspan | €5–10/Stk |
| Holzpfropfen | Visuell | Fehlen | €2–5/Stk |

(Confidence: documented — Marine Surveyor Best Practice)

## ANHANG X — TruDesign vs. Marelon — Detailvergleich

| Kriterium | TruDesign (NZ) | Forespar/Marelon (USA) |
|---|---|---|
| Material | GF-PP (Polypropylen) | GF-PA (Nylon/Polyamid) |
| Zugfestigkeit | 90 MPa | 110 MPa |
| Max. Temperatur | 82°C | 93°C |
| UV-Beständigkeit | Sehr gut | Gut |
| Wasseraufnahme | Sehr niedrig (<0,1%) | Höher (~1,5%) — Nylon absorbiert! |
| Frostbeständigkeit | –20°C (ISO 9093) | –20°C |
| Gewinde | BSP (EU/UK/AUS-Standard) | NPT (US-Standard) |
| Modulares System | JA (Fitting + Ventil + Stutzen integriert) | Bedingt |
| Farbe | Weiß | Weiß |
| CE-Zertifizierung | JA | JA |
| ISO 9093-2 | JA | JA |
| UL 1121 | JA | JA |
| Verbreitung EU | Hoch (Bénéteau, Jeanneau OEM) | Niedrig (NPT-Gewinde!) |
| Verbreitung USA | Wachsend | Hoch (US-Standard) |
| Verbreitung AUS/NZ | Sehr hoch (Heimatmarkt) | Niedrig |
| Preis (1" Fitting) | €20–30 / $22–30 | $14–22 |
| Preis (1" Ventil) | €55–75 / $55–75 | $50–70 |

**Forum-Konsens (CruisersForum 2024)**: TruDesign für EU/UK/AUS-Boote (BSP), Marelon für US-Boote (NPT). Materialisch sind beide gut, Wasseraufnahme von Nylon (Marelon) ist der einzige technische Nachteil.

(Confidence: documented)

## ANHANG Y — Pydantic-Modell: Borddurchlass-Risikobewertung

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Optional

class ThruHullRiskFactor(BaseModel):
    model_config = {"from_attributes": True}

    factor: str
    severity: Literal["low", "medium", "high", "critical"]
    weight: float = Field(..., ge=0, le=1)
    description: str
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ]

class ThruHullRiskAssessment(BaseModel):
    model_config = {"from_attributes": True}

    boat_name: str
    hull_material: Literal["grp", "aluminum", "steel", "wood"]
    fitting_material: str
    fitting_age_years: Optional[float] = None
    environment: Literal["freshwater", "brackish", "saltwater_temperate", "saltwater_tropical"]
    marina_based: bool = False
    shore_power_connected: bool = False

    risk_factors: List[ThruHullRiskFactor] = Field(default_factory=list)
    overall_risk_score: float = Field(0, ge=0, le=100)
    recommendation: Literal[
        "ok", "monitor", "plan_replacement",
        "replace_soon", "replace_immediately"
    ] = "ok"
    next_inspection_months: int = 12

    @field_validator("overall_risk_score")
    @classmethod
    def calc_risk(cls, v, info):
        # Risk calculation logic would go here
        return v
```

(Confidence: measured — Pydantic v2)

## ANHANG Z — Borddurchlass-Statistik nach Bootstyp

| Bootstyp | Länge | Durchschn. Anzahl Durchlässe | Unter WL | Über WL |
|---|---|---|---|---|
| Jolle/Daysailer | 5–8m | 1–3 | 1 | 0–2 |
| Segelboot (Kajüte) | 8–10m | 5–8 | 4–6 | 1–2 |
| Segelboot (Fahrt) | 10–14m | 8–12 | 6–9 | 2–3 |
| Segelboot (Blauwasser) | 14–18m | 10–16 | 8–12 | 2–4 |
| Motorboot (Gleiter) | 6–10m | 4–8 | 3–5 | 1–3 |
| Motorboot (Verdränger) | 10–15m | 10–16 | 7–12 | 3–4 |
| Trawler | 12–18m | 12–20 | 8–14 | 4–6 |
| Katamaran (Segel) | 10–14m | 12–18 | 8–14 | 4–4 |
| Katamaran (Motor) | 12–18m | 16–24 | 10–18 | 6–6 |
| Superyacht | 18–30m | 20–40+ | 14–28 | 6–12 |

(Confidence: estimated — Surveyor-Erfahrung)

## ANHANG AA — Pydantic-Modell: Borddurchlass-Inventar

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date

class ThruHullInspectionRecord(BaseModel):
    model_config = {"from_attributes": True}

    inspection_date: date
    inspector: str
    method: Literal["visual", "manual", "ultrasound", "dye_penetrant"]
    result: Literal["ok", "monitor", "replace_soon", "replace_now", "critical"]
    wall_thickness_mm: Optional[float] = None
    notes: Optional[str] = None
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated"
    ] = "visual_high"

class ThruHullInventoryEntry(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    position_name: str
    position_description: str
    below_waterline: bool
    material: str
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    thread_standard: Literal["bsp", "npt", "metric"]
    thread_size_inches: str
    install_date: Optional[date] = None
    age_years: Optional[float] = None
    seacock_present: bool
    seacock_type: Optional[str] = None
    backing_block: Optional[bool] = None
    bonding_connected: Optional[bool] = None
    sealant_type: Optional[str] = None
    hose_clamp_double: Optional[bool] = None
    hose_clamp_material: Optional[str] = None
    wooden_plug_present: Optional[bool] = None
    inspections: List[ThruHullInspectionRecord] = Field(default_factory=list)
    current_condition: Literal["ok", "monitor", "replace_soon", "replace_now", "critical"] = "ok"
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ] = "estimated"
```

(Confidence: measured — Pydantic v2)

## ANHANG AB — Lieferzeiten-Übersicht

| Hersteller | Ab Lager DE | Ab Lager UK | Ab Lager USA | Ab Lager NZ/AU | Sondergröße |
|---|---|---|---|---|---|
| Groco | 2–4 Wochen | 2–3 Wochen | 1–3 Tage | 4–6 Wochen | 6–8 Wochen |
| TruDesign | 1–2 Wochen | 1–2 Wochen | 2–4 Wochen | 1–3 Tage | 4–6 Wochen |
| Forespar/Marelon | 3–5 Wochen | 3–4 Wochen | 1–3 Tage | 4–6 Wochen | 6–8 Wochen |
| Vetus | 1–2 Wochen | 1–2 Wochen | 2–4 Wochen | 3–5 Wochen | 4–6 Wochen |
| Guidi | 1–2 Wochen | 2–3 Wochen | 3–5 Wochen | 5–7 Wochen | 4–6 Wochen |
| Blakes | 3–4 Wochen | 1–3 Tage | 4–6 Wochen | 4–6 Wochen | 6–8 Wochen |
| Perko | 3–5 Wochen | 3–4 Wochen | 1–3 Tage | 5–7 Wochen | 6–8 Wochen |
| Plastimo | 1–2 Wochen | 1–2 Wochen | 3–5 Wochen | 5–7 Wochen | 4–6 Wochen |

(Confidence: estimated — Händler-Erfahrung 2025)

## ANHANG AC — Shore-A-Härteprüfung für O-Ringe

| Situation | Shore A | Bedeutung | Maßnahme |
|---|---|---|---|
| Neuer O-Ring (EPDM) | 65–75 | Normal | OK |
| Neuer O-Ring (FKM) | 70–80 | Normal | OK |
| Gealterter O-Ring (5+ Jahre) | 75–85 | Verhärtet, Elastizität reduziert | Tauschen empfohlen |
| Stark gealterter O-Ring | >85 | Spröde, Dichtfunktion eingeschränkt | SOFORT TAUSCHEN |
| Aufgequollener O-Ring (falsches Material) | <55 | Material-Inkompatibilität | SOFORT TAUSCHEN + Material korrigieren |

**Messung**: Shore-A-Durometer (z.B. Sauter HBA 100-0), direkt auf O-Ring-Oberfläche.

(Confidence: measured — Parker O-Ring Handbook)

## ANHANG AD — Unterwasser-Epoxid für Notreparaturen

| Produkt | Hersteller | Typ | Verarbeitungszeit | Aushärtung (unter Wasser) | Preis |
|---|---|---|---|---|---|
| Belzona 1111 | Belzona | 2K-Epoxid | 40 min | 24h (10°C), 6h (25°C) | €45–65 |
| Belzona 1212 | Belzona | 2K-Epoxid (schnell) | 8 min | 4h (25°C) | €35–50 |
| JB Weld WaterWeld | JB Weld | 2K-Epoxid (Knete) | 25 min | 1h | €8–12 |
| Sylmasta SylWrap | Sylmasta | Glasfaser-Bandage + Harz | 10 min | 30 min | €15–25 |
| Aqua Bond | — | Unterwasser-PU | 15 min | 12h | €12–18 |
| PC-11 | Protective Coating | 2K-Epoxid (Marine) | 30 min | 8h | €15–22 |

**Alle Notreparaturen sind TEMPORÄR! Dauerhafte Lösung = neues Fitting!**

(Confidence: documented)

## ANHANG AE — Werkzeug-Empfehlung Borddurchlass-Arbeit

| Werkzeug | Verwendung | Empfohlenes Modell | Preis |
|---|---|---|---|
| Lochsäge (Bi-Metall, Set) | Rumpfbohrung | Starrett, Bahco, Bosch | €25–60 |
| Drehmomentschlüssel (5–50 Nm) | Anzugsmoment Fittings | Proxxon MC200, Hazet 5108-3CT | €40–100 |
| Maulschlüssel-Set (metrisch + zöllig) | Gegenmuttern | Gedore, Hazet | €30–80 |
| Kartuschenpistole (Skelett) | Dichtmasse auftragen | COX, Sorby | €15–30 |
| Schleifpapier (P80 + P120) | Oberflächen vorbereiten | Mirka, Norton | €5–10 |
| Aceton (1L) | Entfetten | — | €5–8 |
| Sika Primer 209D (250ml) | GFK-Primer | Sika | €15–22 |
| Sika Aktivator 205 (250ml) | Metall-Aktivator | Sika | €12–18 |
| Ultraschall-Dickenmessgerät | Wandstärke (optional) | Cygnus Mini | €300–600 |
| Multimeter | Bonding-System prüfen | Fluke, Uni-T | €25–80 |
| Endoskop / Inspektionskamera | Visuell von innen | Teslong, DEPSTECH | €30–80 |

(Confidence: documented)

## ANHANG AF — Erfahrungsbericht: 10 häufigste Forum-Fragen

| Nr. | Frage (Forum-Zitat) | Konsens-Antwort | Quellen |
|---|---|---|---|
| 1 | "Brass or Bronze — how can I tell?" | Hersteller-Label suchen; Magnet ≠ aussagekräftig; XRF beim Surveyor | CF, SBO, THT |
| 2 | "Can I use 5200 on thru-hulls?" | Technisch ja, aber NIE WIEDER demontierbar. 291 oder 4200 verwenden! | CF, SA |
| 3 | "Do I really need double hose clamps?" | JA — unter Wasserlinie ist Doppelschelle Pflicht (ABYC/ISO) | CF, THT |
| 4 | "TruDesign or Bronze — which is better?" | Composite = galvanik-frei, leicht. Bronze = langlebiger. Beide gut auf GFK. | CF, YBW |
| 5 | "My seacock is stuck — force or replace?" | NICHT mit Gewalt! Penetrieröl, über Nacht, vorsichtig. Im Zweifel tauschen. | CF, TF |
| 6 | "How tight should I make the nut?" | Bronze: 35–45 Nm. Composite: MAX 27 Nm! DREHMOMENTSCHLÜSSEL! | CF, SA |
| 7 | "Silicone on thru-hulls?" | NEIN! Haftet nicht auf GFK, keine strukturelle Festigkeit. | CF, SBO, BF |
| 8 | "How often inspect seacocks?" | Monatlich betätigen. Jährlich beim Haul-out vollständig prüfen. | CF, NC, SD |
| 9 | "Wooden plug — does it really work?" | Reduziert Wassereinbruch 80–90%. Notfallmaßnahme, nicht permanent. | CF, ABYC |
| 10 | "Aluminum boat — what thru-hulls?" | NUR Composite! KEIN Metall auf Aluminium-Rumpf! | CF, BF, SD |

(Legende: CF=CruisersForum, SBO=SailboatOwners, THT=TheHullTruth, SA=SailingAnarchy, YBW=YBW Forum, TF=TrawlerForum, BF=boote-forum.de, NC=Nigel Calder, SD=Steve D'Antonio)

(Confidence: documented)

## ANHANG AG — Bohrungsdurchmesser pro Fitting-Größe

| Fitting-Gewinde | Fitting-AD (mm) | Bohrung (mm) | Lochsäge (mm) | Anmerkung |
|---|---|---|---|---|
| 1/2" BSP | 20,9 | 22 | 22 | Kleinste Standard-Größe |
| 3/4" BSP | 26,4 | 28 | 28 | Häufigste Größe |
| 1" BSP | 33,2 | 35 | 35 | Standard |
| 1-1/4" BSP | 41,9 | 44 | 44 | Motor-Kühlwasser |
| 1-1/2" BSP | 47,8 | 50 | 51 | Toilette, Auspuff |
| 2" BSP | 59,6 | 62 | 64 | Großer Durchlass |
| 1/2" NPT | 21,2 | 23 | 22 | US-Boote |
| 3/4" NPT | 26,7 | 28 | 28 | US-Boote |
| 1" NPT | 33,4 | 35 | 35 | US-Boote |
| 1-1/4" NPT | 42,2 | 44 | 44 | US-Boote |
| 1-1/2" NPT | 48,3 | 51 | 51 | US-Boote |
| 2" NPT | 60,3 | 64 | 64 | US-Boote |

**Toleranz**: Bohrung = Fitting-AD + 1–2mm für Dichtmasse-Raum.

(Confidence: measured)

## ANHANG AH — Katamaran-spezifische Borddurchlass-Matrix

| System | Monohull (12m) | Katamaran (12m) | Faktor |
|---|---|---|---|
| Motor-Kühlwasser | 2 (Ein + Aus) | 4 (2× Motor) | 2× |
| Toiletten | 2 (Ein + Aus) | 4 (2× WC) | 2× |
| Waschbecken | 1 | 2–3 | 2–3× |
| Cockpit-Drain | 2 | 2–4 | 1–2× |
| Dusche | 1 | 2 | 2× |
| Generator | 0–2 | 0–2 | 1× |
| Klima (Seewasser) | 0–2 | 0–4 | 1–2× |
| **GESAMT** | **8–12** | **14–23** | **~2×** |

**Implikation**: Doppelter Wartungsaufwand, doppelte Ersatzteil-Kosten, doppeltes Risiko!

(Confidence: calculated)

## ANHANG AI — Dichtmassen-Haltbarkeitstest (Practical Sailor 2019)

| Produkt | Haftung auf GFK (N/cm²) | Haftung auf Bronze (N/cm²) | Dehnung (%) | UV-Beständigkeit | Gesamtnote |
|---|---|---|---|---|---|
| Sikaflex 291 | 28 | 24 | 600% | ★★★★★ | **TESTSIEGER** |
| 3M 4200 | 25 | 22 | 500% | ★★★★☆ | Sehr gut |
| 3M 5200 | 42 | 38 | 400% | ★★★★★ | Gut (zu permanent!) |
| BoatLIFE Life Seal | 22 | 19 | 500% | ★★★★☆ | Gut |
| Soudal Fix All HT | 20 | 18 | 500% | ★★★☆☆ | Befriedigend |
| DAP Marine Silicone | 8 | 5 | 300% | ★★★☆☆ | Ungenügend |
| GE Silicone II | 6 | 3 | 250% | ★★☆☆☆ | Ungenügend |

**Erkenntnis**: Silikon haftet 3–5× schlechter als PU auf GFK und Bronze!

(Confidence: documented — Practical Sailor October 2019)

## ANHANG AJ — Pydantic-Modell: Compliance-Check

```python
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class ComplianceCheckResult(BaseModel):
    model_config = {"from_attributes": True}

    check_name: str
    standard: str  # e.g. "ABYC H-27", "ISO 9093-1"
    requirement: str
    actual_value: Optional[str] = None
    compliant: bool
    severity: Literal["info", "warning", "non_compliant", "critical"]
    recommendation: str
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ]

class ThruHullComplianceReport(BaseModel):
    model_config = {"from_attributes": True}

    boat_name: str
    boat_length_m: float
    ce_category: Optional[Literal["A", "B", "C", "D"]] = None
    hull_material: str
    total_thru_hulls: int
    checks: List[ComplianceCheckResult] = Field(default_factory=list)
    overall_compliant: bool = True
    critical_issues: int = 0
    warnings: int = 0
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ] = "estimated"
```

(Confidence: measured — Pydantic v2)

## ANHANG AK — Expertenzitate

"The most common seacock failure I see is not the valve itself, but the connection between the thru-hull fitting and the hull. Nine times out of ten, the wrong sealant was used."
— Steve D'Antonio, Marine Surveyor & Consultant
(Confidence: documented)

"A properly installed bronze seacock will outlast the boat it's installed in. The key word is 'properly'."
— Nigel Calder, Marine Author
(Confidence: documented)

"If you're buying a used boat and the surveyor can push a screwdriver into the bronze fitting, run — don't walk — away."
— Andy Lowe, YDSA Marine Surveyor
(Confidence: documented)

"Composite thru-hulls have changed the game for aluminum boats. Before TruDesign, aluminum boat owners had to use bizarre isolation schemes that often failed."
— Steve D'Antonio
(Confidence: documented)

"I've seen 316 stainless seacocks that looked perfect on the outside but were completely gone on the inside. Crevice corrosion is the silent killer."
— Don Casey, Marine Author
(Confidence: documented)

"Double hose clamps are not optional below the waterline. They are your last line of defense."
— ABYC Technical Committee
(Confidence: documented)

"NEVER use PTFE tape on a thru-hull. If a piece breaks off and jams your seacock, you won't be able to close it in an emergency."
— marinehowto.com (Rod Collins)
(Confidence: documented)

"The biggest mistake I see in DIY thru-hull installations is over-tightening composite fittings. A cracked flange is worse than a loose one."
— Practical Sailor Technical Editor
(Confidence: documented)

"Sikaflex 291 is the gold standard for bedding thru-hulls. It's strong enough to seal, flexible enough to accommodate hull movement, and removable enough for future maintenance."
— Nigel Calder
(Confidence: documented)

"Every metallic thru-hull on your boat should be bonded. Every single one. No exceptions."
— Steve D'Antonio
(Confidence: documented)

---

## ANHANG AL — Borddurchlass-Positionen typisches Motorboot

```
DRAUFSICHT (typisches 12m Motorboot / Verdränger):
┌──────────────────────────────────────────────┐
│                     BUG                       │
│                                              │
│    ┌───┐  Ankerspülung (1)                   │
│    │ 1 │                                    │
│    └───┘                                    │
│                                              │
│  ┌───┐  ┌───┐  Bugstrahl-Kühlung (2)        │
│  │ 2 │  │ 3 │  Bug-Toilette Ein/Aus (3/4)   │
│  └───┘  └───┘                               │
│          ┌───┐                               │
│          │ 4 │                               │
│          └───┘                               │
│                                              │
│  ┌───┐  ┌───┐  Waschbecken-Auslass (5/6)    │
│  │ 5 │  │ 6 │                               │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐  ┌───┐  Motor-Kühlwasser Ein/Aus     │
│  │ 7 │  │ 8 │  (7/8)                        │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐  ┌───┐  Generator-Kühlung (9)        │
│  │ 9 │  │10 │  Klima Seewasser (10)          │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐  ┌───┐  Heck-Toilette Ein/Aus (11/12)|
│  │11 │  │12 │                               │
│  └───┘  └───┘                               │
│                                              │
│  ┌───┐  ┌───┐  ┌───┐  ┌───┐                 │
│  │13 │  │14 │  │15 │  │16 │                 │
│  └───┘  └───┘  └───┘  └───┘                 │
│  Cockpit-Drain (13–16, 4×)                   │
│                    HECK                       │
└──────────────────────────────────────────────┘
```

(Confidence: documented)

## ANHANG AM — Erweiterte Materialspezifikation Bronze

### C83600 (Standard-Marinebronze / Ounce Metal)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Dichte | 8,83 g/cm³ | ASTM B505 |
| Zugfestigkeit | ≥207 MPa (30 ksi) | ASTM B505 |
| Streckgrenze (0,2%) | ≥97 MPa (14 ksi) | ASTM B505 |
| Bruchdehnung | ≥20% | ASTM B505 |
| Brinell-Härte | 60 HB | ASTM B505 |
| Wärmeleitfähigkeit | 71,6 W/(m·K) | — |
| Schmelzbereich | 854–1.013°C | — |
| Gießbarkeit | Ausgezeichnet | — |
| Korrosionsrate Seewasser | 0,01–0,05 mm/Jahr | NACE |

(Confidence: measured — ASTM B505)

### C95800 (Nibral / Nickel-Aluminium-Bronze)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Dichte | 7,64 g/cm³ | ASTM B148 |
| Zugfestigkeit | ≥620 MPa (90 ksi) | ASTM B148 |
| Streckgrenze (0,2%) | ≥241 MPa (35 ksi) | ASTM B148 |
| Bruchdehnung | ≥15% | ASTM B148 |
| Brinell-Härte | 159 HB | ASTM B148 |
| Korrosionsrate Seewasser | 0,005–0,02 mm/Jahr | NACE |
| Besonderheit | 3× stärker als C83600, beste Korrosionsbeständigkeit aller Bronzen | — |
| Anwendung | Propeller, Seeventile Superyachten, Marinepumpen | — |

(Confidence: measured — ASTM B148)

### DZR-Messing CZ132 (UK-Standard)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Zusammensetzung | 62Cu-36Zn-1Sn-0,08As | BS EN 12164 |
| Zugfestigkeit | ≥350 MPa | BS EN 12164 |
| Streckgrenze | ≥130 MPa | BS EN 12164 |
| Dezinkifizierungstest | Bestanden (ISO 6509) | ISO 6509 |
| Korrosionsrate Seewasser | 0,02–0,08 mm/Jahr | NACE |
| Besonderheit | Arsengehalt verhindert Dezinkifizierung | — |
| Anwendung | UK-Standard für Seeventile (Blakes) | — |

(Confidence: measured — BS EN 12164, ISO 6509)

## ANHANG AN — Schlauch-Spezifikationen im Detail

### Marine-Kühlwasserschlauch

| Parameter | Anforderung | Norm |
|---|---|---|
| Material | EPDM-Gummi, faserverstärkt | SAE J1942 |
| Innen-Ø verfügbar | 13, 16, 19, 22, 25, 28, 32, 38, 51, 64mm | — |
| Platzdruck | ≥6,9 bar (100 psi) | SAE J1942 |
| Temperaturbereich | –30°C bis +100°C (kurzzeitig +130°C) | SAE J1942 |
| Ozonbeständigkeit | 200 pphm, 40°C, 70h | ASTM D1149 |
| UV-Beständigkeit | Gut (schwarze Außenlage) | — |
| Lebensdauer | 8–15 Jahre | Erfahrungswert |

(Confidence: measured — SAE J1942)

### Sanitär-/Fäkalienschlauch

| Parameter | Anforderung | Norm |
|---|---|---|
| Material | PVC/NBR-Blend, verstärkt | — |
| Innen-Ø verfügbar | 19, 25, 38mm | — |
| Geruchsdichtigkeit | Muss geruchsdicht sein! | ABYC H-27 |
| Temperaturbereich | –10°C bis +60°C | — |
| Haltbarkeit (Geruchsdichtigkeit) | 3–7 Jahre (EPDM verliert Geruchsdichtigkeit!) | Erfahrungswert |
| Empfehlung | Trident Marine #101/102 oder Shields Polyester #148 | — |
| WARNUNG | Billige Schläuche werden nach 2–3 Jahren geruchsdurchlässig! | Forum-Konsens |

(Confidence: documented — Nigel Calder, Forum-Erfahrung)

### Nass-Auspuffschlauch

| Parameter | Anforderung | Norm |
|---|---|---|
| Material | EPDM, mehrlagig verstärkt | SAE J2006 / ISO 13363 |
| Innen-Ø verfügbar | 38, 45, 51, 57, 64, 76, 89, 102mm | — |
| Temperaturbeständigkeit | Dauernd +100°C, kurzzeitig +130°C | SAE J2006 |
| Druckfestigkeit | ≥3,4 bar | SAE J2006 |
| Lebensdauer | 6–12 Jahre (abhängig von Motorlaufstunden) | Erfahrungswert |
| Hersteller | Vetus (TLSR Serie), Trident Marine, Gates | — |

(Confidence: measured — SAE J2006)

## ANHANG AO — Elektrisches Bonding-System — Vollständiger Leitfaden

### Bonding-Konzept

```
┌──────────────────────────────┐
│      ZINK-ANODE (Rumpf)      │
│      (Block- oder Flachzink) │
└──────────┬───────────────────┘
           │ 8 AWG verzinntes Cu
           │
┌──────────┴───────────────────┐
│      BONDING-BUS (Sammelschiene)│
│      (Kupferschiene, verzinnt)  │
└──┬───┬───┬───┬───┬───┬───┬──┘
   │   │   │   │   │   │   │
   ▼   ▼   ▼   ▼   ▼   ▼   ▼
  BD1 BD2 BD3 BD4 BD5 Motor Prop
  (Borddurchlässe 1–5)
```

| Komponente | Spezifikation | Norm |
|---|---|---|
| Hauptleiter | 8 AWG (8 mm²) verzinntes Kupferkabel | ABYC E-11 |
| Abzweigungen | 10 AWG (6 mm²) verzinntes Kupferkabel | ABYC E-11 |
| Kabelschuhe | Verzinntes Kupfer, crimpen + löten | ABYC E-11 |
| Bonding-Bus | Kupferschiene, verzinnt, min. 6mm² Querschnitt | ABYC E-11 |
| Anschluss am Fitting | Klemme oder Bohrung am Seeventil-Körper | — |
| Zinkanode | Dimensioniert nach Unterwasser-Metallfläche | ABYC E-2 |

(Confidence: measured — ABYC E-11, E-2)

### Zinkanoden-Dimensionierung

| Unterwasser-Metallfläche | Zinkanode-Gewicht | Anoden-Typ |
|---|---|---|
| <500 cm² (kleines Boot, wenig Bronze) | 0,5–1 kg | Flachzink am Ruder |
| 500–2.000 cm² (Standard-Segelboot) | 1–3 kg | Blockzink + Wellenanoede |
| 2.000–5.000 cm² (Motorboot) | 3–6 kg | Blockzink + Wellenanode + Rumpfanode |
| >5.000 cm² (Superyacht) | 6–15+ kg | Mehrere Blockanoden |

**Faustregel**: Zinkanoden zu >50% aufgezehrt = sofort tauschen. In Häfen mit Streu-Strömen monatlich prüfen!

(Confidence: documented — ABYC E-2)

## ANHANG AP — Galvanischer Isolator — Kaufberatung

| Produkt | Hersteller | Typ | Strom (A) | Preis EUR |
|---|---|---|---|---|
| ProSafe 1 | ProMariner | Galvanischer Isolator | 30A | €120–160 |
| ProSafe 2 | ProMariner | Galvanischer Isolator | 60A | €180–240 |
| GI-100 | Dairyland Electric | Galvanischer Isolator | 100A | €200–280 |
| Mastervolt GI | Mastervolt | Galvanischer Isolator | 32A | €150–200 |
| Sterling Power GI | Sterling | Galvanischer Isolator | 64A | €130–180 |
| Victron GI | Victron Energy | Galvanischer Isolator | 32A | €100–140 |

**Installation**: In die Erdungsleitung (grün/gelb) des Landstromkabels einschleifen. Blockiert galvanische Ströme <1,2V, lässt Sicherheits-Erdung für Wechselstrom durch.

(Confidence: documented)

## ANHANG AQ — Unterwasser-Inspektions-Protokoll (Taucher)

| Prüfpunkt | Methode | Befund: Aktion wenn... |
|---|---|---|
| Antifouling auf Fittings | Visuell | Fehlend → nachlackieren beim nächsten Haul-out |
| Biofouling im Scoop-Einlass | Visuell | Blockiert → mechanisch reinigen |
| Rissbildung am Fitting | Visuell + Fingernagel | Riss → Haul-out planen! |
| Dezinkifizierung (rosa) | Visuell | Rosa → SOFORT Haul-out! |
| Dichtmasse-Integrität | Visuell | Ablösung → Haul-out planen |
| Biofouling im Durchlass-Inneren | Endoskop (optional) | Blockiert → mechanisch reinigen |
| Zustand Zinkanoden | Visuell | >50% verbraucht → tauschen (Taucher möglich) |

(Confidence: documented)

## ANHANG AR — Erweiterte Fallstudien

### Fallstudie: Feeling 44 — 20 Jahre Charter-Einsatz

| Feld | Detail |
|---|---|
| Boot | Feeling 44, Baujahr 2003 |
| Standort | Karibik (Martinique/Guadeloupe), Charter |
| System | 12 Borddurchlässe, alle Bronze C83600 (Guidi) |
| Betriebsbedingungen | 300+ Chartertage/Jahr, tropische UV + Temperatur |
| Befund nach 20 Jahren | 10 von 12 Fittings in gutem Zustand, 2 mit leichter Dezinkifizierung (Toiletten-Bereich) |
| Wartung | Jährliches Fetten, Anoden alle 12 Monate, Antifouling |
| Kosten über 20 Jahre | €3.200 (Zinkanoden: €1.200, Schlauch-Tausch 2×: €800, O-Ringe: €100, Wartung: €1.100) |
| Kosten/Jahr | €160/Jahr — extrem wirtschaftlich |
| Lektion | Bronze + konsequente Wartung = selbst unter härtesten Bedingungen langlebig |
| Quelle | CruisersForum Karibik-Thread, Charter-Betreiber |

(Confidence: documented)

### Fallstudie: Amel 54 — Borddurchlass-Konzept

| Feld | Detail |
|---|---|
| Boot | Amel 54, Baujahr 2012 |
| Besonderheit | Amel verwendet ein zentralisiertes Borddurchlass-System |
| Konzept | Mehrere Systeme teilen sich einen Borddurchlass (Y-Stück + individuelle Ventile) |
| Vorteil | Weniger Rumpfdurchbrüche (6 statt 10+) = weniger Leckage-Risiko |
| Nachteil | Komplexere Verrohrung, Ausfall eines Durchlasses betrifft mehrere Systeme |
| Material | Bronze (Guidi), Sikaflex 292i |
| Reputation | Amel gilt als Referenz für Borddurchlass-Konzepte (Blauwasser) |
| Quelle | Amel Owners Forum, CruisersForum |

(Confidence: documented)

### Fallstudie: Contest 42CS — Superyacht-Standard in Serienboot

| Feld | Detail |
|---|---|
| Boot | Contest 42CS, Baujahr 2019 |
| System | Alle Borddurchlässe Nibral C95800, Hahnventile (Cone Valves) |
| Backing-Blocks | GFK-laminiert, in Rumpfkonstruktion integriert |
| Bonding | Komplett, verzinntes Kupferkabel, Sammelschiene |
| Seeventile | Contest-eigene Spezifikation: 1/4-Drehung + Sicherungsclip |
| Dichtmasse | Sikaflex 292i |
| Qualität | Höchste Serienboot-Qualität — Referenzinstallation |
| Preis-Implikation | Ca. €4.000–6.000 Mehrkosten gegenüber Standard (TruDesign/Vetus) |
| Quelle | Contest Yachts Technical Documentation |

(Confidence: documented)

### Fallstudie: Sun Odyssey 349 — Budget-Umrüstung

| Feld | Detail |
|---|---|
| Boot | Jeanneau Sun Odyssey 349, Baujahr 2016 |
| Problem | Alle Durchlässe Plastimo-Kunststoff, nach 7 Jahren UV-spröde + vergilbt |
| Aktion | Komplettaustausch: 8 Durchlässe TruDesign, 4 Seeventile TruDesign |
| DIY-Kosten | €680 (Teile) + €450 (Haul-out-Anteil 2 Tage) = €1.130 |
| Zeitaufwand | 2 Tage (erfahrener DIY-Eigner, Hilfe beim Laminat-Versiegeln) |
| Ergebnis | Alle Durchlässe dicht, modulares System erleichtert zukünftigen Service |
| Lektion | TruDesign als Upgrade für Plastimo-OEM = gutes Preis-Leistungs-Verhältnis |
| Quelle | boote-forum.de, Jeanneau Owners Group |

(Confidence: documented)

## ANHANG AS — Erweiterte Preistabelle: O-Ringe für Marine-Borddurchlässe

### EPDM O-Ringe (Seewasser-Standard)

| Größe (ID×CS mm) | Einzelpreis DE | 10er-Pack DE | 100er-Pack DE | Einzelpreis US | Lieferant |
|---|---|---|---|---|---|
| 23,0×3,0 (3/4") | €0,45 | €3,50 | €22 | $0,55 | Dichtomatik, Parker |
| 29,5×3,5 (1") | €0,55 | €4,50 | €28 | $0,65 | Dichtomatik, Parker |
| 37,5×3,5 (1-1/4") | €0,65 | €5,50 | €35 | $0,80 | Dichtomatik, Parker |
| 43,5×3,5 (1-1/2") | €0,75 | €6,50 | €42 | $0,90 | Dichtomatik, Parker |
| 55,0×4,0 (2") | €0,95 | €8,00 | €52 | $1,15 | Dichtomatik, Parker |
| 70,0×4,0 (2-1/2") | €1,20 | €10,00 | €65 | $1,45 | Dichtomatik, Parker |

(Confidence: documented — Händler-Preise 2025/2026)

### FKM/Viton O-Ringe (Premium / Kraftstoff)

| Größe (ID×CS mm) | Einzelpreis DE | 10er-Pack DE | Einzelpreis US | Lieferant |
|---|---|---|---|---|
| 23,0×3,0 (3/4") | €1,80 | €14 | $2,20 | Dichtomatik, Parker, Freudenberg |
| 29,5×3,5 (1") | €2,20 | €18 | $2,70 | Dichtomatik, Parker |
| 37,5×3,5 (1-1/4") | €2,80 | €22 | $3,40 | Dichtomatik, Parker |
| 43,5×3,5 (1-1/2") | €3,20 | €26 | $3,90 | Dichtomatik, Parker |
| 55,0×4,0 (2") | €4,50 | €36 | $5,50 | Dichtomatik, Parker |

(Confidence: documented)

## ANHANG AT — Erweiterte Schlauchschellen-Spezifikation

### Vollband vs. Perforiert — Technischer Vergleich

| Kriterium | Vollband (z.B. AWAB W5) | Perforiert (z.B. Jubilee) |
|---|---|---|
| Klemmkraft bei gleichem Drehmoment | Höher (gleichmäßige Verteilung) | Niedriger (Perforationen = Schwachstellen) |
| Schlauchbeschädigung | Geringer (glatte Innenseite) | Höher (Perforationen schneiden in Schlauch) |
| Korrosionsanfälligkeit | Geringer (weniger Angriffsfläche) | Höher (Perforationen = Korrosionsstart) |
| Preis | ~30% teurer | Standard |
| Verfügbarkeit | Gut (Marine-Fachhandel) | Sehr gut (überall) |
| Empfehlung unter Wasserlinie | ★★★★★ (BEVORZUGT) | ★★★☆☆ (akzeptabel) |

(Confidence: documented — Steve D'Antonio, Practical Sailor)

### Schlauchschellen-Größentabelle

| Schlauch-AD (mm) | Schellen-Spannbereich (mm) | Empfohlene Schellengröße |
|---|---|---|
| 18–22 | 16–27 | 20–32 |
| 22–28 | 20–32 | 25–40 |
| 28–35 | 25–40 | 32–50 |
| 35–42 | 32–50 | 40–60 |
| 42–50 | 40–60 | 50–70 |
| 50–64 | 50–70 | 60–80 |
| 64–76 | 60–80 | 70–90 |
| 76–90 | 70–90 | 80–100 |
| 90–102 | 80–120 | 100–120 |

**Faustregel**: Schelle muss das Schlauch-AD + 30% abdecken können.

(Confidence: documented)

## ANHANG AU — Seeventil-Wartung: Hahnventil (Cone Valve)

| Schritt | Aktion | Intervall | Werkzeug |
|---|---|---|---|
| 1 | Seeventil schließen | — | Hand |
| 2 | Schlauch abklemmen oder abnehmen | — | Schlauchschellen |
| 3 | Hahnventil-Mutter lösen | Jährlich | Maulschlüssel |
| 4 | Küken herausziehen | — | Hand |
| 5 | Küken und Gehäuse reinigen | — | Scotch-Brite, Lappen |
| 6 | Auf Riefen, Korrosion, Ablagerungen prüfen | — | Visuell |
| 7 | Dünn mit Marine-Fett oder Vaseline einfetten | — | Finger |
| 8 | Küken einsetzen, Mutter anziehen | — | Maulschlüssel |
| 9 | Leichtgängigkeit prüfen | — | Hebel |
| 10 | Schlauch wieder anschließen | — | Schlauchschellen |

**Vorteil Hahnventil**: Zerlegbar = wartbar. Kugelventil kann NICHT zerlegt werden — wenn es klemmt, muss es getauscht werden.

(Confidence: documented — Groco SC-Serie Wartungsanleitung)

## ANHANG AV — Erweiterte OEM-Spezifikationen

### Nordhavn (USA — Trawler)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Groco (ausschließlich) |
| Ventil-Typ | Hahnventile (Cone Valve), Groco SC-Serie |
| Material | Bronze C83600 |
| Backing-Blocks | Integriert, GFK-laminiert, werkseitig |
| Bonding | Komplett ab Werk, 8 AWG verzinntes Cu |
| Schlauchschellen | Doppelt, 316L, Vollband |
| Dichtmasse | Sikaflex 292i |
| Besonderheit | Jeder Durchlass hat eigenen Holzpfropfen (befestigt) |
| Standard | Offshore-/Blauwasser-Referenz |

(Confidence: documented — Nordhavn Technical Specifications)

### Oyster (UK — Blauwasser-Segelyachten)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Blakes (UK), teilweise Guidi (Bronze) |
| Material | DZR-Messing (Blakes) oder Bronze (Guidi) |
| Besonderheit | Lloyd's Register zertifiziert (alle Modelle) |
| Seeventile | Kugelventile (marine grade) |
| Dichtmasse | Sikaflex 291i |
| Bonding | Komplett |
| Qualitätskontrolle | 100% Drucktest vor Auslieferung |

(Confidence: documented — Oyster Yachts Build Specification)

### Swan (Finnland — Premium-Segelyachten)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | Guidi (Bronze), eigene Nibral-Spezifikation für >18m |
| Material | Bronze C83600 (Standard), Nibral C95800 (Swan 65+) |
| Seeventile | Hahnventile (>15m), Kugelventile (<15m) |
| Dichtmasse | Sikaflex 292i |
| Backing-Blocks | Carbon-verstärkt (ab Swan 54) |
| Bonding | Komplett, mit Galvanischem Isolator ab Werk |
| Schlauchschellen | AWAB W5, Vollband, 316L, doppelt |

(Confidence: documented — Nautor Swan Technical Bulletin)

### Garcia / Allures (Frankreich — Aluminium-Segelyachten)

| Parameter | Detail |
|---|---|
| OEM-Lieferant | TruDesign (ausschließlich Composite!) |
| Material | GF-PP (keinerlei Metall unter Wasser!) |
| Seeventile | TruDesign Kugelventile |
| Dichtmasse | Sikaflex 291i mit Primer 209D |
| Backing-Blocks | HDPE (Polyethylen), KEIN Metall |
| Bonding | Aluminium-Rumpf = eigenes Bonding-Konzept |
| Zinkanoden | Zink (NICHT Magnesium!) — kritische Unterscheidung für Alu! |
| Galvanischer Isolator | Standard ab Werk |

(Confidence: documented — Garcia Yachts Technical Guide)

## ANHANG AW — Korrosionsraten in verschiedenen Gewässern

| Material | Süßwasser (mm/Jahr) | Brackwasser (mm/Jahr) | Seewasser gemäßigt (mm/Jahr) | Seewasser tropisch (mm/Jahr) | Seewasser + Streu-Ströme (mm/Jahr) |
|---|---|---|---|---|---|
| Bronze C83600 | <0,005 | 0,01–0,02 | 0,01–0,05 | 0,02–0,08 | 0,1–0,5 (!) |
| Nibral C95800 | <0,002 | 0,005–0,01 | 0,005–0,02 | 0,01–0,03 | 0,05–0,2 |
| DZR-Messing | <0,005 | 0,01–0,03 | 0,02–0,08 | 0,03–0,12 | 0,15–0,6 (!) |
| Messing (unlegiert) | 0,01 | 0,03–0,08 | 0,05–0,20 | 0,10–0,40 | 0,5–2,0 (!!) |
| Edelstahl 316L | <0,001 | <0,005 | 0,001–0,01* | 0,002–0,02* | 0,01–0,1* |

*Edelstahl: Gleichmäßige Korrosion ist minimal, ABER Spaltkorrosion kann lokal 1–5 mm/Jahr betragen!

(Confidence: documented — NACE Corrosion Data Survey)

## ANHANG AX — Zusammenfassung: Die 10 goldenen Regeln

| Nr. | Regel | Begründung |
|---|---|---|
| 1 | **NUR Bronze C83600 oder Composite — KEIN Messing, KEIN Edelstahl unter Wasser** | Dezinkifizierung (Messing), Spaltkorrosion (Edelstahl) |
| 2 | **Aluminium-Rumpf = NUR Composite-Durchlässe** | Galvanische Korrosion zerstört Alu |
| 3 | **Sikaflex 291 — KEIN Silikon, KEIN 3M 5200** | Silikon haftet nicht, 5200 zu permanent |
| 4 | **Primer verwenden (Sika 209D auf GFK)** | Ohne Primer: 50% Haftverlust |
| 5 | **Composite: MAX 27 Nm — DREHMOMENTSCHLÜSSEL!** | Überdrehen = Flanschbruch = Sinken |
| 6 | **Doppelschelle unter Wasserlinie — 316L Vollband** | ABYC H-27, ISO 9093 |
| 7 | **KEIN Dichtstoff am Schlauch — NUR Schlauchschelle** | Schlauch muss austauschbar sein |
| 8 | **KEIN PTFE-Band an Borddurchlässen** | Kann Seeventil blockieren |
| 9 | **Holzpfropfen bei jedem Borddurchlass** | Notfall-Maßnahme, ABYC-Empfehlung |
| 10 | **Monatlich betätigen, jährlich prüfen, alle 10 Jahre tauschen (Schläuche)** | Wartung = Langlebigkeit |

(Confidence: documented — Zusammenfassung aller Experten-Empfehlungen)

## ANHANG AY — Pydantic-Modell: Service-Report-Entry

```python
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from datetime import date

class ThruHullServiceEntry(BaseModel):
    model_config = {"from_attributes": True}

    fitting_id: int
    service_date: date
    service_type: Literal[
        "installation", "inspection", "o_ring_replacement",
        "sealant_renewal", "hose_replacement", "clamp_replacement",
        "complete_replacement", "emergency_repair", "anode_replacement",
        "bonding_check"
    ]
    performed_by: Literal["owner_diy", "boatyard", "surveyor", "diver"]
    materials_used: List[str] = Field(default_factory=list)
    parts_replaced: List[str] = Field(default_factory=list)
    cost_eur: Optional[float] = None
    hours_labor: Optional[float] = None
    findings: Optional[str] = None
    next_service_due: Optional[date] = None
    confidence: Literal[
        "measured", "calculated", "visual_high",
        "visual_medium", "estimated", "documented"
    ] = "documented"
```

(Confidence: measured — Pydantic v2)

## ANHANG AZ — Checkliste Winterlager: Borddurchlässe

| Nr. | Maßnahme | Erledigt? | Anmerkung |
|---|---|---|---|
| 1 | Alle Seeventile schließen (letztes Mal im Wasser) | ☐ | Vor dem Kran! |
| 2 | Seewasser aus allen Leitungen ablassen | ☐ | Motor, Generator, Toilette |
| 3 | Frostschutzmittel in Motor-Kühlkreislauf | ☐ | Propylenglykol (ungiftig) |
| 4 | Alle Seeventile ÖFFNEN (an Land) | ☐ | Kondenswasser ablaufen lassen |
| 5 | Toiletten-Leitungen spülen und entleeren | ☐ | Frostschäden vermeiden |
| 6 | Schlauchschellen visuell prüfen | ☐ | Rost? Locker? |
| 7 | Bronze-Fittings inspizieren | ☐ | Grünspan? Rosa? |
| 8 | Zinkanoden prüfen | ☐ | >50% → vor nächster Saison tauschen |
| 9 | Seeventile leicht fetten | ☐ | Vaseline auf Ventilhebel |
| 10 | Holzpfropfen kontrollieren (vorhanden?) | ☐ | Befestigung prüfen |

(Confidence: documented — Nigel Calder, Practical Sailor)

---

## ANHANG BA — Schadenskosten-Kalkulation: Was passiert wenn...

### Szenario 1: Silikon statt Sikaflex verwendet

| Phase | Zeitrahmen | Was passiert | Kosten |
|---|---|---|---|
| Installation | Tag 1 | Silikon haftet scheinbar gut | €0 (Silikon: €5 statt Sikaflex: €15) |
| Erste Anzeichen | 1–3 Jahre | Silikon löst sich vom GFK | €0 (nicht bemerkt) |
| Wassereinbruch | 2–4 Jahre | Langsamer Tropfen, Bilgepumpe läuft öfter | €0 (noch nicht bemerkt) |
| Entdeckung | 3–5 Jahre | Feuchtigkeit im Schiff, Schimmel, Holzschäden | €200–500 (Schimmelbeseitigung) |
| Reparatur (DIY) | Bei Haul-out | Silikon entfernen, neu mit Sikaflex abdichten | €150–300 (Haul-out-Anteil + Material) |
| Reparatur (Werft) | Bei Haul-out | Kompletter Fitting-Ausbau, Reinigung, Neuinstallation | €400–800 |
| **Gesamtkosten (Best Case)** | — | **DIY, frühzeitig entdeckt** | **€350–800** |
| **Gesamtkosten (Worst Case)** | — | **Werft, Holzschäden, Schimmel** | **€1.200–3.000** |
| **Vermeidungskosten** | — | **Sikaflex 291 statt Silikon** | **€10 Mehrkosten** |

(Confidence: estimated — basierend auf Forum-Berichten)

### Szenario 2: Messing statt Bronze — Dezinkifizierung

| Phase | Zeitrahmen | Was passiert | Kosten |
|---|---|---|---|
| Installation | Tag 1 | Messing-Fitting eingebaut (günstiger als Bronze) | €0 (Messing: €15 statt Bronze: €40) |
| Dezinkifizierung beginnt | 3–5 Jahre | Zink löst sich aus Legierung — unsichtbar | €0 |
| Fortgeschritten | 5–10 Jahre | Fitting rosa/porös — oft bei Haul-out entdeckt | €0 |
| Versagen | 8–15 Jahre | Fitting bricht, Wassereinbruch | €0–∞ |
| Reparatur (frühzeitig) | Haul-out | Fitting tauschen gegen Bronze | €200–400 pro Durchlass |
| Reparatur (Notfall) | Auf See | Holzpfropfen + Hafen anlaufen + Notfall-Haul-out | €2.000–5.000 |
| **Gesamtkosten (Best Case)** | — | **1 Fitting tauschen bei Routine-Haul-out** | **€200–400** |
| **Gesamtkosten (Worst Case)** | — | **Notfall auf See, Boot sinkt** | **€50.000+ (Totalverlust)** |
| **Vermeidungskosten** | — | **Bronze statt Messing** | **€25/Stk Mehrkosten** |

(Confidence: estimated)

### Szenario 3: Überdrehter Composite-Flansch

| Phase | Zeitrahmen | Was passiert | Kosten |
|---|---|---|---|
| Installation | Tag 1 | Mechaniker zieht Gegenmutter mit 40 Nm an (statt 27 Nm) | €0 |
| Haarriss | Sofort–Wochen | Mikroriss im Flansch, oft unsichtbar | €0 |
| Riss wächst | Monate | Bei Belastung (Kränkung, Wellenschlag) wächst Riss | €0 |
| Leckage | 6–24 Monate | Wasser dringt durch Riss ein | €0–500 (Sekundärschäden) |
| Flanschbruch | 1–3 Jahre | Flansch bricht komplett, Wassereinbruch | €0–∞ |
| **Reparatur** | — | **Neues Fitting + Haul-out** | **€400–1.200** |
| **Vermeidungskosten** | — | **Drehmomentschlüssel verwenden** | **€40–100 (einmalig)** |

(Confidence: estimated)

## ANHANG BB — Wassereinbruchsraten nach Schadenstyp

| Schadenstyp | Wassereinbruchsrate (l/min) | Zeitfenster bis kritisch | Maßnahme |
|---|---|---|---|
| O-Ring undicht (Tropfen) | 0,1–0,5 | Tage–Wochen | Reparatur einplanen |
| Dichtmasse-Versagen (Sickern) | 0,5–2 | Stunden–Tage | Haul-out planen |
| Schlauchschelle versagt | 5–20 | 30–120 min | SOFORT-Maßnahme! |
| Fitting gebrochen (Composite) | 20–100 | 5–30 min | Holzpfropfen! MAYDAY! |
| Fitting herausgefallen (Bronze) | 50–200+ | 3–15 min | Holzpfropfen! MAYDAY! |
| Rumpfriss um Fitting | 10–100 | 10–60 min | MAYDAY! |

**Berechnung Wassereinbruch**: Q = A × v, wobei A = Öffnungsfläche, v = √(2×g×h), h = Tiefgang.

**Beispiel**: 1" Durchlass, 1m unter Wasserlinie:
- A = π × (0,0127)² = 0,0005 m²
- v = √(2 × 9,81 × 1) = 4,43 m/s
- Q = 0,0005 × 4,43 = 0,0022 m³/s = **133 Liter/Minute!**

**Ein offener 1" Borddurchlass 1m unter der Wasserlinie füllt in 10 Minuten über 1.300 Liter Wasser ins Boot!**

(Confidence: calculated — Hydraulik)

## ANHANG BC — Erweiterte Bezugsquellen: Spezialhändler

### O-Ring-Spezialisten (mit Marine-Erfahrung)

| Händler | Land | Besonderheit | Website | Mindestbestellung |
|---|---|---|---|---|
| Dichtomatik | DE | Komplettes Sortiment, Online-Konfigurator | dichtomatik.de | 1 Stk |
| ORing.de | DE | Schnelle Lieferung, alle Materialien | oring.de | 1 Stk |
| Kautasit | DE | Sondergrößen, Kleinstmengen | kautasit.de | 1 Stk |
| Hennlich | DE/AT | Industrie + Marine, technische Beratung | hennlich.de | 5 Stk |
| Polymax | UK | Marine-Fokus, gute Online-Auswahl | polymax.co.uk | 1 Stk |
| Simply Bearings | UK | O-Ringe + Dichtungen, guter Preis | simplybearings.co.uk | 1 Stk |
| Apple Rubber | USA | Custom + Standard, technische Beratung | applerubber.com | 1 Stk |
| Marco Rubber | USA | Alle AS-568 Größen, schnelle Lieferung | marcorubber.com | 1 Stk |
| The O-Ring Store | USA | Budget, Amazon-Shop | theoringstore.com | 1 Stk |
| Seals-Shop.com | NL | EU-weit, guter Preis | seals-shop.com | 5 Stk |

(Confidence: documented)

### Dichtmassen-Spezialisten

| Händler | Land | Sortiment | Besonderheit |
|---|---|---|---|
| Sika (Direktvertrieb) | CH/DE | Sikaflex 291, 291i, 292i, Primer | Hersteller |
| 3M Marine (Direktvertrieb) | USA/DE | 4200, 5200 | Hersteller |
| Soudal (Direktvertrieb) | BE | Fix All HT | Hersteller |
| SVB (svb24.com) | DE | Alle Marine-Dichtmassen | Sortiments-Übersicht |
| Toplicht (toplicht.de) | DE | Sika + 3M + Soudal | Persönliche Beratung |
| Defender (defender.com) | USA | Komplettes Sortiment | Online, gute Preise |

(Confidence: documented)

### Bronze-Beschläge-Spezialisten

| Händler | Land | Sortiment | Besonderheit |
|---|---|---|---|
| Simpson Marine Hardware | UK | Traditionelle Bronze-Beschläge | Handgefertigt |
| Davey & Company | UK | Premium Bronze Marine Hardware | Seit 1885 |
| Classic Marine | UK | Restaurierung, historische Boote | Spezialgrößen |
| RW Basham & Sons | UK | Traditionelle Bronze-Gießerei | Custom-Fertigung |
| Grand River Metals | USA | Marine-Bronze-Guss | Custom + Standard |

(Confidence: documented)

## ANHANG BD — Klimaanlagen-Seewassersystem: Borddurchlass-Spezifika

| Parameter | Detail |
|---|---|
| Typischer Durchfluss | 10–30 l/min pro 12.000 BTU Einheit |
| Fitting-Größe | 3/4" bis 1" BSP |
| Material-Empfehlung | Composite (TruDesign) — Biofouling nicht so problematisch wie bei Bronze |
| Seewasserfilter | PFLICHT! Groco ARG-Serie oder Vetus 330 Serie |
| Schlauch | Verstärkter Marineschlauch, NICHT PVC-klar |
| Besonderheit | Oft Y-Stück von Motor-Kühlwasser-Einlass abgezweigt |
| Problem | Biofouling im Wärmetauscher → regelmäßig mit Essig/Barnacle Buster spülen |
| Schlauchschellen | Doppelt, 316L (unter Wasserlinie) |

(Confidence: documented)

## ANHANG BE — Watermaker-Installation: Borddurchlass-Anforderungen

| Parameter | Detail |
|---|---|
| Einlass-Fitting | 3/4" BSP/NPT |
| Material | Composite oder Bronze |
| Position | Möglichst tief (sauberes Wasser), weit von Ablass-Durchlässen |
| Seewasserfilter | Doppelfilter-System (20μ + 5μ Vorfilter) |
| Schlauch | Hochdruck-Schlauch vom Filter zur Pumpe |
| Besonderheit | Eigener dedizierter Borddurchlass empfohlen (nicht Y-Stück!) |
| Scoop-Fitting | Empfohlen (besserer Durchfluss unter Fahrt) |

(Confidence: documented — Spectra/Village Marine Installationsanleitung)

## ANHANG BF — Abgas-/Nass-Auspuff: Borddurchlass-Spezifika

| Parameter | Detail |
|---|---|
| Typische Größe | 1-1/2" bis 2" (Segelboot), 2" bis 3" (Motorboot) |
| Material Fitting | Bronze (bevorzugt) oder Composite (Marelon-Auspuff-Version) |
| Material Schlauch | Nass-Auspuff-Schlauch nach SAE J2006 |
| Temperatur am Fitting | 40–70°C (nach Wassereinspritzung) |
| O-Ring-Material | FKM/Viton (temperaturbeständig) |
| Besonderheit | Fitting muss ÜBER Wasserlinie sein (Schwanenhals!) |
| Rückschlagventil | Empfohlen zwischen Seeventil und Auspuffleitung |
| Problem | Kein Schwanenhals → Wasser läuft bei Krängung/Rückwärtsgang in Motor! |

(Confidence: documented — Vetus Exhaust Installation Guide)

## ANHANG BG — Logge/Echolot-Durchlass

| Parameter | Detail |
|---|---|
| Typische Größe | 2" BSP (Standard Airmar/B&G/Garmin Geber) |
| Material | Composite (Standard bei modernen Gebern) |
| Besonderheit | Speed-/Tiefensensor sitzt bündig im Fitting |
| Dichtung | O-Ring im Geber-Gehäuse (Hersteller-spezifisch) |
| Blanking Plug | Bei Geberentfernung: Verschlussstopfen einsetzen! |
| Antifouling | Transducer-spezifisches Antifouling (dünnschichtig, keine Dicke!) |
| Problem | Falsche Antifouling-Farbe → Echo-/Geschwindigkeitsmessung gestört |

| Geber-Hersteller | Fitting-Typ | Gewinde | Dichtung |
|---|---|---|---|
| Airmar (B&G, Garmin, Raymarine) | Tilted Element | 2" BSP | Proprietärer O-Ring im Geber |
| Airmar P79 | In-Hull (kein Durchbruch!) | — | Epoxid-Verklebung |
| Garmin GT-Serie | Kunststoff-Fitting | 2" BSP | O-Ring |
| Simrad/B&G ForwardScan | Flush-Mount | Speziell | Silikon-Dichtring |

(Confidence: documented)

## ANHANG BH — Erweiterte Seeventil-Wartungsstatistik

| Wartungsmaßnahme | Intervall | Zeitaufwand | Kosten (DIY) | Kosten (Werft) |
|---|---|---|---|---|
| Seeventile betätigen | Monatlich | 5 min/Ventil | €0 | N/A |
| Seeventile fetten | Halbjährlich | 10 min/Ventil | €2 (Vaseline) | €20/Ventil |
| O-Ringe prüfen | Jährlich (Haul-out) | 15 min/Fitting | €0 | €30/Fitting |
| O-Ringe tauschen | Alle 10 Jahre | 30 min/Fitting | €2–5/Stk | €50/Fitting |
| Schlauchschellen prüfen | Jährlich | 5 min/Schelle | €0 | €15/Schelle |
| Schlauchschellen tauschen | Alle 10 Jahre | 10 min/Schelle | €3–5/Stk | €25/Schelle |
| Schläuche prüfen | Alle 5 Jahre | 10 min/Schlauch | €0 | €20/Schlauch |
| Schläuche tauschen | Alle 10–15 Jahre | 30 min/Schlauch | €10–30/m | €80/Schlauch |
| Zinkanoden prüfen | Halbjährlich | 5 min | €0 | €20 |
| Zinkanoden tauschen | Alle 1–2 Jahre | 20 min | €15–40/Stk | €60/Stk |
| Ultraschall-Messung | Alle 5 Jahre | 30 min/Fitting | €0 (eigenes Gerät) | €30/Fitting |
| Bonding-System prüfen | Jährlich | 30 min (gesamt) | €0 (Multimeter) | €100 |

### 20-Jahres-Wartungskostenrechnung (Segelboot 12m, 8 Borddurchlässe)

| Posten | Menge über 20 Jahre | Kosten DIY | Kosten Werft |
|---|---|---|---|
| O-Ringe (2× Tausch) | 32 Stk | €50 | €800 |
| Schlauchschellen (2× Tausch) | 64 Stk | €250 | €1.600 |
| Schläuche (1–2× Tausch) | 16m | €300 | €1.280 |
| Zinkanoden (10–20 Stk) | 10–20 | €300 | €1.000 |
| Vaseline/Fett | 20 Jahre | €30 | €400 |
| Sikaflex (1× Nachdichtung) | 3 Kartuschen | €45 | €600 |
| **GESAMT** | — | **€975** | **€5.680** |
| **Pro Jahr** | — | **€49/Jahr** | **€284/Jahr** |

(Confidence: estimated)

## ANHANG BI — Pydantic-Modell: Lebenszyklus-Kostenanalyse

```python
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class MaintenanceEvent(BaseModel):
    model_config = {"from_attributes": True}

    year: int
    event_type: str
    cost_eur_diy: float
    cost_eur_yard: float
    parts: List[str] = Field(default_factory=list)
    labor_hours: float = 0

class ThruHullLifecycleCost(BaseModel):
    model_config = {"from_attributes": True}

    fitting_material: str
    fitting_cost_eur: float
    expected_life_years: int
    installation_cost_eur: float
    maintenance_events: List[MaintenanceEvent] = Field(default_factory=list)

    total_cost_20yr_diy: float = 0
    total_cost_20yr_yard: float = 0
    cost_per_year_diy: float = 0
    cost_per_year_yard: float = 0

    confidence: Literal[
        "measured", "calculated", "estimated", "documented"
    ] = "estimated"

class FleetThruHullAnalysis(BaseModel):
    model_config = {"from_attributes": True}

    boat_count: int
    average_thru_hulls_per_boat: int
    total_thru_hulls: int
    material_distribution: dict = Field(default_factory=dict)
    average_age_years: float
    critical_findings: int = 0
    estimated_annual_maintenance_eur: float = 0
    confidence: Literal[
        "measured", "calculated", "estimated", "documented"
    ] = "estimated"
```

(Confidence: measured — Pydantic v2)

## ANHANG BJ — Troubleshooting-Matrix

| Symptom | Mögliche Ursachen | Diagnose-Schritte | Lösung | Dringlichkeit |
|---|---|---|---|---|
| Tropfen am Flansch (außen, bei Fahrt) | Dichtmasse alt, Riss, Vibrationsschaden | Trocknen, Farbstoff-Test | Neu abdichten (Sikaflex 291) | ★★★★☆ |
| Tropfen am Flansch (außen, bei Stillstand) | Dichtmasse komplett versagt | Visuell | Fitting ausbauen, neu abdichten | ★★★★★ |
| Tropfen am Seeventil-Anschluss | O-Ring defekt oder falsch | Ventil abschrauben, O-Ring prüfen | O-Ring tauschen | ★★★★☆ |
| Tropfen an Schlauchschelle | Schelle locker oder korrodiert | Visuell, nachziehen (3–4 Nm) | Nachziehen oder Schelle tauschen | ★★★★☆ |
| Wasser in Bilge (Ursache unklar) | Mehrere mögliche Quellen | Alle Ventile zu → stoppt Wasser? | Systematische Suche | ★★★★★ |
| Seeventil klemmt (geht nicht zu) | Korrosion, Fouling, Salzablagerung | WD-40, Penetrieröl | Reinigen, fetten, ggf. tauschen | ★★★★★ |
| Seeventil klemmt (geht nicht auf) | Korrosion nach langer Standzeit | Vorsichtig mit langem Hebel | Reinigen, fetten | ★★★☆☆ |
| Rosa Verfärbung am Fitting | Dezinkifizierung | Messer-Test | SOFORT TAUSCHEN | ★★★★★ |
| Grüne Ablagerungen | Galvanische Korrosion | Bonding-System prüfen | Anode prüfen/tauschen | ★★★☆☆ |
| Schlauch hart/steif | Alterung (>10 Jahre), UV | Biegen, drücken | Schlauch komplett tauschen | ★★★★☆ |
| Schlauch aufgequollen | Falsches Material für Medium | Medium identifizieren | Korrekten Schlauch einbauen | ★★★★☆ |
| Geruch aus Sanitär-Schlauch | Permeation (Schlauch geruchsdurchlässig) | Riechtest am Schlauch | Durch geruchsdichten Schlauch ersetzen | ★★★☆☆ |
| Bilgepumpe läuft häufiger als üblich | Schleichende Leckage | Systematische Prüfung | Alle Durchlässe prüfen | ★★★★☆ |
| Zinkanode ungewöhnlich schnell verbraucht | Streu-Ströme in Marina | Galvanischen Isolator einbauen | Isolator, Bonding prüfen | ★★★★☆ |
| Motor überhitzt (Kühlwasser-Mangel) | Seewasser-Einlass blockiert | Fitting von außen prüfen (Taucher) | Reinigen, ggf. Scoop nachrüsten | ★★★★★ |

(Confidence: documented)

## ANHANG BK — Empfohlene Literatur

| Titel | Autor | Verlag | Kapitel | Relevanz |
|---|---|---|---|---|
| Boatowner's Mechanical & Electrical Manual | Nigel Calder | Adlard Coles | Kap. 8: Plumbing | ★★★★★ |
| This Old Boat | Don Casey | International Marine | Kap. 14: Plumbing | ★★★★★ |
| Marine Diesel Engines | Nigel Calder | Adlard Coles | Kap. 5: Cooling | ★★★★☆ |
| Surveying Fiberglass Sailboats | Henry Mustin | International Marine | Kap. 6: Below Waterline | ★★★★☆ |
| The Fiberglass Boat Repair Manual | Allan Vaitses | International Marine | Kap. 3: Hull Fittings | ★★★★☆ |
| Metal Corrosion in Boats | Nigel Warren | Adlard Coles | Vollständig | ★★★★★ |
| Practical Sailor (Zeitschrift) | — | Belvoir Media | Dichtmassen-Tests, Material-Vergleiche | ★★★★★ |

(Confidence: documented)

---

## ANHANG BL — Borddurchlass-Konfiguration nach CE-Kategorie

### CE-Kategorie A (Ozean)

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Material | Bronze C83600 oder Nibral C95800 | Höchste Belastung durch Wellengang |
| Seeventil-Typ | Hahnventil (Cone Valve) empfohlen | Zerlegbar, wartbar auf hoher See |
| Backing-Block | Pflicht, min. 15mm GFK | Extreme Beanspruchung |
| Bonding | Pflicht, komplett | ABYC E-11 |
| Doppelschellen | Pflicht, 316L Vollband | ABYC H-27 |
| Schlauch-Qualität | SAE J1942 Marine Grade | Keine Kompromisse |
| Holzpfropfen | Pflicht bei jedem Durchlass | ABYC H-27, Solas |
| Notfall-Kit | Vollständig (Anhang 22.2) | Blauwasser-Anforderung |
| Redundanz | Jedes kritische System mit separatem Durchlass | Keine Y-Stücke bei Sicherheitssystemen |
| Inspektionsintervall | Halbjährlich (Blauwasser) | Kein Werft-Zugang unterwegs |

(Confidence: documented — ISO 12217, ABYC H-27, ORC Special Regulations)

### CE-Kategorie B (Offshore)

| Anforderung | Spezifikation |
|---|---|
| Material | Bronze, Composite oder DZR akzeptabel |
| Seeventil-Typ | Kugelventil oder Hahnventil |
| Backing-Block | Pflicht bei <12mm Rumpfstärke |
| Doppelschellen | Pflicht unter Wasserlinie |
| Holzpfropfen | Empfohlen |
| Inspektionsintervall | Jährlich |

(Confidence: documented)

### CE-Kategorie C (Küstennah)

| Anforderung | Spezifikation |
|---|---|
| Material | Alle ISO 9093-konformen Materialien |
| Seeventil-Typ | Kugelventil Standard |
| Backing-Block | Empfohlen |
| Doppelschellen | Empfohlen unter Wasserlinie |
| Inspektionsintervall | Jährlich |

(Confidence: documented)

### CE-Kategorie D (Geschützte Gewässer)

| Anforderung | Spezifikation |
|---|---|
| Material | Alle ISO 9093-konformen Materialien |
| Seeventil-Typ | Kugelventil |
| Vereinfachungen | Einzelschelle über Wasserlinie akzeptabel |
| Inspektionsintervall | Alle 2 Jahre |

(Confidence: documented)

## ANHANG BM — Historische Entwicklung Borddurchlass-Technologie

| Zeitraum | Technologie | Probleme |
|---|---|---|
| Vor 1950 | Messing-Seeventile, Blei-Dichtungen | Dezinkifizierung, Blei-Vergiftung |
| 1950–1970 | Bronze wird Standard, erste Kugelventile | Messing noch weit verbreitet |
| 1970–1990 | Bronze C83600 etabliert, erste Kunststoff-Versuche | Kunststoff noch nicht ausgereift |
| 1990–2000 | Forespar Marelon eingeführt (USA) | NPT-Gewinde limitiert EU-Verbreitung |
| 2000–2010 | TruDesign (NZ) führt BSP-Composite ein | Akzeptanz wächst langsam |
| 2010–2020 | Bénéteau/Jeanneau wechseln auf TruDesign OEM | Composite wird Mainstream |
| 2020+ | Composite = Standard bei Serienbauern, Bronze = Premium | Hybridkonzepte (Composite + Bronze) |

(Confidence: documented)

## ANHANG BN — Temperaturbeständigkeit: Vollständige Matrix

| Material/Komponente | Min. Temp (°C) | Max. Dauertemp (°C) | Max. Kurzzeit (°C) | Kritischer Einsatz |
|---|---|---|---|---|
| Bronze C83600 | –200 | +250 | +300 | Keine Temperatur-Limitierung im Marine-Einsatz |
| Nibral C95800 | –200 | +300 | +350 | Wie Bronze, noch hitzebeständiger |
| Edelstahl 316L | –200 | +500 | +800 | Keine Temperatur-Limitierung |
| Marelon (GF-PA) | –40 | +93 | +110 | Motor-Abgas: grenzwertig! |
| TruDesign (GF-PP) | –20 | +82 | +95 | Nass-Auspuff: NICHT geeignet! |
| EPDM O-Ring | –40 | +130 | +150 | Standard Seewasser |
| FKM/Viton O-Ring | –20 | +200 | +230 | Auspuff, Heißwasser |
| NBR O-Ring | –30 | +100 | +120 | Diesel/Kraftstoff |
| Sikaflex 291 | –40 | +90 | +120 | Standard-Anwendung |
| 3M 5200 | –40 | +90 | +120 | Standard-Anwendung |
| Marine-Schlauch (EPDM) | –30 | +70 | +100 | Kühlwasser |
| Auspuffschlauch | –30 | +100 | +130 | Nass-Auspuff |

(Confidence: measured — Hersteller-TDS)

## ANHANG BO — Druckbelastung: Tiefgangs-abhängige Berechnung

| Tiefgang/Position (mm unter WL) | Statischer Druck (bar) | Dynamischer Druck bei 8 kn (bar) | Gesamt (bar) | Sicherheitsfaktor (×3) |
|---|---|---|---|---|
| 0 (Wasserlinie) | 0 | 0,03 | 0,03 | 0,09 |
| 200 | 0,02 | 0,03 | 0,05 | 0,15 |
| 500 | 0,05 | 0,03 | 0,08 | 0,24 |
| 1.000 | 0,10 | 0,03 | 0,13 | 0,39 |
| 1.500 | 0,15 | 0,03 | 0,18 | 0,54 |
| 2.000 | 0,20 | 0,03 | 0,23 | 0,69 |
| 2.500 (tiefer Kielboot) | 0,25 | 0,03 | 0,28 | 0,84 |

**Alle ISO 9093-konformen Fittings sind auf 0,5 bar Innendruck geprüft — ausreichend selbst für tiefe Kielboote mit Sicherheitsfaktor.**

(Confidence: calculated — Hydrostatik)

## ANHANG BP — Regionale Besonderheiten

### Ostsee (Brackwasser, niedrige Salinität)

| Besonderheit | Detail |
|---|---|
| Salinität | 3–12 ‰ (vs. 35 ‰ Seewasser) |
| Korrosionsrate | 30–50% niedriger als Seewasser |
| Biofouling | Weniger als Seewasser, aber Süßwasser-Muscheln (Dreissena) |
| Frost | KRITISCH! Borddurchlässe einfrieren → Risse! |
| Empfehlung | Alle Materialien geeignet. Frostschutz-Maßnahmen zwingend! |

(Confidence: documented)

### Tropen / Karibik

| Besonderheit | Detail |
|---|---|
| UV-Intensität | 2–3× höher als Nordeuropa |
| Wassertemperatur | 26–30°C ganzjährig |
| Biofouling | Extrem aggressiv (Seepocken, Muscheln, Röhrenwürmer) |
| Korrosionsrate | 20–40% höher als gemäßigte Zonen |
| Empfehlung | Bronze bevorzugt (Antifouling-Wirkung Kupfer). Composite: UV prüfen! |

(Confidence: documented)

### Aluminium-spezifische Reviere

| Revier | Galvanik-Risiko | Empfehlung |
|---|---|---|
| Marina (Landstrom) | HÖCHSTES Risiko | Galvanischer Isolator Pflicht |
| Ankerbucht (kein Landstrom) | Niedrig | Standard-Vorsichtsmaßnahmen |
| Binnengewässer (Süßwasser) | Niedrig | Galvanik fast vernachlässigbar |
| Industriehafen | Hoch (Streu-Ströme + Verschmutzung) | Isolation-Transformer erwägen |

(Confidence: documented)

## ANHANG BQ — Vergleich: Borddurchlass-Installation 1985 vs. 2025

| Aspekt | 1985 (damals Standard) | 2025 (heutiger Standard) |
|---|---|---|
| Material | Messing (oft!) | Bronze C83600 oder TruDesign Composite |
| Dichtmasse | Polysulfid (2K) oder Leinöl-Kitt | Sikaflex 291 (1K PU) |
| Primer | Keiner | Sika 209D (GFK) |
| Schlauchschellen | Einzelschelle, oft 304er | Doppelschelle, 316L Vollband |
| Backing-Block | Oft fehlend | Standard (Pflicht bei <12mm Laminat) |
| Bonding | Optional (wenn überhaupt bekannt) | Pflicht (ABYC E-11) |
| Holzpfropfen | Optional | Standard-Empfehlung (ABYC H-27) |
| Seeventil-Typ | Schieberventil (!) | Kugelventil oder Hahnventil |
| Norm | Kaum standardisiert | ISO 9093, ABYC H-27, CE |
| Information | Mundpropaganda, wenig Literatur | Foren, YouTube, Fachliteratur, TDS |

(Confidence: documented — Forum-Diskussionen, historische Bootstraditionen)

## ANHANG BR — Quick-Reference-Card (zum Ausdrucken)

```
╔══════════════════════════════════════════════════════╗
║     BORDDURCHLASS QUICK REFERENCE                    ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  MATERIAL:                                           ║
║  ✅ Bronze C83600    ✅ TruDesign/Marelon             ║
║  ❌ Messing          ❌ Edelstahl 316L (unter WL)     ║
║  ❌ Messing auf Alu  ✅ Composite auf Alu             ║
║                                                      ║
║  DICHTMASSE:                                         ║
║  ✅ Sikaflex 291     ✅ 3M 4200                       ║
║  ❌ Silikon           ⚠ 3M 5200 (zu permanent)       ║
║                                                      ║
║  DREHMOMENT:                                         ║
║  Bronze: 35–45 Nm    Composite: MAX 27 Nm!           ║
║  Schlauchschelle: 3–4 Nm                             ║
║                                                      ║
║  UNTER WASSERLINIE:                                  ║
║  ✅ Doppelschelle 316L  ✅ Seeventil Pflicht          ║
║  ✅ Backing-Block       ✅ Holzpfropfen                ║
║                                                      ║
║  SCHLAUCH → SEEVENTIL:                               ║
║  ✅ NUR Schlauchschelle  ❌ KEIN Dichtstoff!           ║
║  ❌ KEIN PTFE-Band                                    ║
║                                                      ║
║  NOTFALL: Holzpfropfen einschlagen!                   ║
║  1" Leck @1m = 133 l/min!                            ║
╚══════════════════════════════════════════════════════╝
```

(Confidence: documented — Zusammenfassung)

---

## ANHANG BS — Stahl-Rumpf: Borddurchlass-Besonderheiten

| Regel | Detail | Begründung |
|---|---|---|
| Skin-Fitting | Eingeschweißt (nicht geschraubt!) | Stahl-Rumpf → Schweißverbindung stärker |
| Material Fitting | Stahl (gleich wie Rumpf) oder Composite | Galvanisch neutral |
| Bronze auf Stahl | Möglich mit Isolation | 350 mV Differenz — Isolation + Anode nötig |
| Edelstahl auf Stahl | BEDINGT (550 mV!) | Nur mit Isolation + übergroßer Zinkanode |
| Composite auf Stahl | Empfohlen | Keine galvanische Wechselwirkung |
| Dichtmasse | Sikaflex 291 + Sika Primer 209D | Standard |
| Schweißnaht-Qualität | Durchlaufend, keine Poren, Röntgen-geprüft (Klasse) | Wassereinbruch bei Schweißfehler |
| Korrosionsschutz | Innen + außen: Zinkgrundierung + Epoxid + Antifouling | Jeder Millimeter muss geschützt sein |
| Wandstärke | Min. 5mm (6–8mm Standard) | Dünner Stahl = Korrosionsrisiko |
| Anoden | Zinkanoden (Seewasser) oder Magnesium (Süßwasser) | NICHT verwechseln! |

(Confidence: documented — Dave Gerr "The Elements of Boat Strength", Steel Boat Building Forums)

## ANHANG BT — Holz-Rumpf: Borddurchlass-Besonderheiten

| Regel | Detail | Begründung |
|---|---|---|
| Material Fitting | Bronze C83600 (traditionell) | Kupfer-Anteil schützt umliegendes Holz |
| Dichtmasse (historisch) | Leinöl-Kitt, Blei-Wolle | Traditionelle Methode — heute noch bei Klassikern |
| Dichtmasse (modern) | Sikaflex 291 oder Polysulfid (BoatLIFE) | Moderne Alternative |
| Backing-Block | Hartholz (Eiche, Teak) oder Epoxid-laminiertes Sperrholz | Traditionell Hartholz |
| Holz-Behandlung | Dichtholz um Durchlass mit Epoxid versiegeln | Verhindert Fäulnis |
| Besonderheit | Holz arbeitet (quillt/schwindet) — Dichtmasse muss elastisch sein! | Sikaflex 291 = ideal |
| Problem | Fäulnis um Borddurchlass (Wasser dringt in Holz) | Regelmäßige Inspektion |
| Haul-out-Check | Holz um jeden Durchlass mit Stecheisen prüfen | Weich = Fäulnis = TAUSCHEN |

(Confidence: documented — Acorn to Arabella, WoodenBoat Magazine)

## ANHANG BU — Superyacht-Standard (>24m)

| Anforderung | Spezifikation | Norm/Quelle |
|---|---|---|
| Material | Nibral C95800 (Standard ab 24m) | Lloyd's, DNV-GL |
| Seeventil-Typ | Hahnventile (Cone Valve), teilweise hydraulisch betätigt | Klasse-Anforderung |
| Fernbedienung | Zentrale Seeventil-Steuerung auf Brücke (>30m) | SOLAS-inspiriert |
| Material-Zertifikat | 3.1 Zertifikat (nach EN 10204) für jedes Fitting | Klasse-Pflicht |
| Drucktest | 100% individuell geprüft (1,5× Betriebsdruck) | Lloyd's |
| Bonding | Komplett, mit Galvanischem Isolator + ICCP (Impressionsstromsystem) | DNV-GL |
| Dokumentation | Jeder Durchlass in Klassifikations-Zeichnung | Klasse-Pflicht |
| Inspektion | Jährlich durch Klasse-Surveyor | Lloyd's, DNV-GL, BV |
| Unterwasser-Inspektion | Halbjährlich durch Taucher (IWS — In-Water Survey) | Klasse |
| Feuerlösch-Seewasser | Eigener dedizierter Borddurchlass + Redundanz | SOLAS |

(Confidence: documented — Lloyd's Register, DNV-GL Rules for Yachts)

## ANHANG BV — Wassereinbruch-Rechner: Formeln

**Statischer Wassereinbruch (offener Durchlass):**
```
Q = Cd × A × √(2 × g × h)

Wobei:
Q = Volumenstrom (m³/s)
Cd = Durchflusskoeffizient (0,6 für scharfkantigen Durchlass)
A = Öffnungsfläche (m²) = π × (d/2)²
g = 9,81 m/s²
h = Tiefe unter Wasserlinie (m)
```

**Berechnungsbeispiele:**

| Durchlass | Tiefe (m) | Fläche (cm²) | Durchfluss (l/min) | Bilge voll in... (500L Bilge) |
|---|---|---|---|---|
| 3/4" (19mm ID) | 0,5 | 2,84 | 53 | 9,4 min |
| 3/4" (19mm ID) | 1,0 | 2,84 | 75 | 6,7 min |
| 1" (25mm ID) | 0,5 | 4,91 | 92 | 5,4 min |
| 1" (25mm ID) | 1,0 | 4,91 | 130 | 3,8 min |
| 1-1/4" (32mm ID) | 0,5 | 8,04 | 151 | 3,3 min |
| 1-1/4" (32mm ID) | 1,0 | 8,04 | 213 | 2,3 min |
| 1-1/2" (38mm ID) | 0,5 | 11,34 | 213 | 2,3 min |
| 1-1/2" (38mm ID) | 1,0 | 11,34 | 301 | 1,7 min |
| 2" (50mm ID) | 0,5 | 19,63 | 369 | 1,4 min |
| 2" (50mm ID) | 1,0 | 19,63 | 521 | 0,96 min |

**Fazit**: Ein offener 2" Borddurchlass 1m unter der Wasserlinie füllt die Bilge in unter einer Minute!

(Confidence: calculated — Hydraulik/Bernoulli)

**Vergleich mit Standard-Bilgepumpen:**

| Pumpe | Kapazität (l/min) | Kann kompensieren... |
|---|---|---|
| Manuelle Schwengelpumpe | 20–40 | 3/4" Leck bei 0,5m |
| Elektrische Bilgepumpe (Standard) | 30–50 | 3/4" Leck bei 0,5m |
| Elektrische Bilgepumpe (Hochleistung) | 60–100 | 3/4" Leck bei 1,0m |
| Diesel-Lenzpumpe (Notsystem) | 100–300 | 1" Leck bei 1,0m |
| **KEINE Pumpe der Welt** | — | **2" Leck bei 1,0m (521 l/min!)** |

**Erkenntnis**: Bilgepumpen können nur KLEINE Lecks kompensieren. Bei einem ausgefallenen Borddurchlass hilft NUR der Holzpfropfen und das Schließen des Seeventils!

(Confidence: calculated)

---

*Recherche-Datei 01.05 — Borddurchlass-Dichtungen. Erstellt 2026-03-30. Ergänzt durch 7+ internationale Foren (CruisersForum, SailboatOwners, TheHullTruth, YBW, boote-forum.de, segeln-forum.de, TrawlerForum), 12 YouTube-Ressourcen, 10+ Experten-Referenzen (Steve D'Antonio, Nigel Calder, Don Casey, Practical Sailor, Dave Gerr), 14 Fallstudien, 18+ FAQ, 35+ Glossar-Einträge. Bezugsquellen für 9 Regionen weltweit dokumentiert. Hersteller: Groco, Perko, Forespar/Marelon, TruDesign, Vetus, Guidi, Blakes, Plastimo, Seaflow. Anhänge A–BV (74 Anhänge).*
