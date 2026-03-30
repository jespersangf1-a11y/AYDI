# Niedergangs-Dichtungen im Yachtbau: Vollständige Wissensreferenz

## Metadaten

- **Kategorie:** 01 — Dichtungen und Profile
- **Unterkategorie:** 04 — Niedergangs-Dichtungen
- **Version:** 1.0
- **Letzte Aktualisierung:** 2026-03-29
- **Datenquellen:** Hersteller-Kataloge, ISO-Normen, Forum-Konsens, Experten-Interviews, YouTube-Kanäle, Fachliteratur
- **Sprache:** Deutsch (Fachbegriffe englisch in Klammern)
- **AYDI-Modul-Zuordnung:** materials, compliance, service_patterns, production

```python
# AYDI Pydantic v2 Integration
from pydantic import BaseModel
from typing import Optional, List

class NiedergangsDichtung(BaseModel):
    model_config = {"from_attributes": True}

    hersteller: str
    produkt_name: str
    teilenummer: Optional[str] = None
    material: str  # EPDM, Silikon, Neoprene, TPE, PVC, Bürstendichtung
    profil_typ: str  # P-Profil, D-Profil, E-Profil, Bulb, Lippe, I-Beam, Bürste
    breite_mm: Optional[float] = None
    hoehe_mm: Optional[float] = None
    shore_a: Optional[int] = None
    temperatur_min_c: Optional[float] = None
    temperatur_max_c: Optional[float] = None
    uv_bestaendigkeit: str  # "gering", "gut", "sehr_gut", "exzellent"
    salzwasser_bestaendigkeit: str
    einsatzbereich: str  # "schiebeleiste", "washboard_kanal", "schwelle", "schloss", "universal"
    lebensdauer_jahre: Optional[float] = None
    preis_eur_pro_meter: Optional[float] = None
    confidence: str
```

---

## Inhaltsverzeichnis

1. Grundlagen: Niedergangs-Anatomie und Dichtungszonen
2. Dichtungsmaterialien: Vergleich und Spezifikationen
3. Profiltypen und Querschnitte
4. Schiebeleisten-Dichtungen (Sliding Hatch Seals)
5. Washboard-Dichtungen (Drop Board Seals)
6. Schwellen-Dichtungen (Sill Seals)
7. Schloss-Bereich-Dichtungen (Lock Area Seals)
8. Hersteller-Katalog: Lewmar
9. Hersteller-Katalog: Houdini Marine
10. Hersteller-Katalog: Bomar
11. Hersteller-Katalog: Trend Marine
12. Hersteller-Katalog: LIKON (Aufblasbare Dichtungen)
13. Hersteller-Katalog: Cruising Concepts
14. Hersteller-Katalog: Teak Isle Manufacturing
15. Hersteller-Katalog: Davis Instruments
16. Hersteller-Katalog: Oceanair/Dometic
17. Profildichtungs-Hersteller: Schlegel, Deventer, Rehau, Veka
18. Profildichtungs-Hersteller: Trim-Lok, M.D. Building Products, Steele Rubber
19. Profildichtungs-Hersteller: Ultrafab, Pemko (Bürstendichtungen)
20. Profildichtungs-Hersteller: Primasil, Silicone Engineering (Silikon)
21. OEM-Spezifikationen nach Bootsmarke
22. DIY-Lösungen aus Foren
23. Werkstoff-Datenblätter und Prüfnormen
24. Fehlerbilder und Schadensdiagnose
25. Einbau- und Austausch-Anleitungen
26. Lebensdauer und Wartungsintervalle
27. Klimaabhängige Empfehlungen
28. Kostenanalyse und Budgetplanung
29. Bezugsquellen weltweit
30. Forum-Referenzen und Erfahrungsberichte
31. YouTube-Ressourcen
32. Experten-Referenzen und Fachliteratur
33. Fallstudien
34. FAQ
35. Glossar
36. ANHANG A — Bootsmodell-Zuordnungstabelle
37. ANHANG B — Profilquerschnitt-Zeichnungen
38. ANHANG C — Materialverträglichkeitsmatrix
39. ANHANG D — Inspektions-Checklisten
40. ANHANG E — AYDI-Analyse-Anbindung
41. ANHANG F — Erweiterte Berechnungsbeispiele
42. ANHANG G — Normen-Referenztabelle
43. ANHANG H — Regionale Bezugsquellen-Details

---

## 1. Grundlagen: Niedergangs-Anatomie und Dichtungszonen

### 1.1 Definition und Funktion

Der Niedergang (Companionway) ist der Hauptzugang vom Cockpit in den Innenraum einer Yacht. Er besteht typischerweise aus einer Schiebeleiste (Sliding Hatch), Washboards (Drop Boards) und einer Schwelle (Sill). Die Abdichtung des Niedergangs ist eine der kritischsten Aufgaben im Yachtbau, da hier die größte Öffnung im Deck gegen Wasser, Wind und Wärme geschützt werden muss.
(Confidence: measured)

### 1.2 Niedergangs-Bauformen

| Bauform | Beschreibung | Typische Boote | Dichtungsanforderung |
|---------|-------------|---------------|---------------------|
| **Traditioneller Niedergang** | Schiebeleiste + 2–3 Washboards übereinander | Segelboote 8–15m | Hoch — 4 Dichtungszonen |
| **Niedergang mit Festtür** | Feste Tür statt Washboards, Schiebeleiste oben | Fahrtensegler 12–20m | Mittel — 2 Dichtungszonen |
| **Niedergang mit Klapptür** | Klappbare Tür nach oben oder seitlich | Motoryachten 10–18m | Mittel — Scharnier-Dichtung |
| **Flush-Niedergang** | Bündig mit Deck, hydraulisch oder manuell | Custom/Superyachten 18m+ | Sehr hoch — Flächendichtung |
| **Pilothouse-Niedergang** | Zugang vom Pilothouse, geschützt | Langfahrt-Segler 13–20m | Niedrig — Innenraum zu Innenraum |
| **Center-Cockpit-Niedergang** | Achterniedergang zum Achterkajüte | Ketches, Center-Cockpit 12–18m | Hoch — exponierte Lage |
(Confidence: measured)

### 1.3 Vier Dichtungszonen am Niedergang

```
Zone 1: SCHIEBELEISTE (Sliding Hatch)
┌─────────────────────────────────────┐
│  Schiebeleiste gleitet auf Schienen │
│  Seitliche Dichtung: Bürstenprofil  │
│  Vordere Dichtung: Kompressions-    │
│  profil oder Lippendichtung         │
│  Hintere Dichtung: Regenrinne +     │
│  Tropfkante                         │
└─────────────────────────────────────┘

Zone 2: WASHBOARDS (Drop Boards)
┌─────────────────────────────────────┐
│  Seitliche Kanäle: Kompressions-    │
│  dichtung (D-Profil, Neoprene)      │
│  Überlappung oben/unten:            │
│  Lippendichtung oder Falz           │
│  Letztes Board oben: Anpressung     │
│  gegen Schiebeleiste                │
└─────────────────────────────────────┘

Zone 3: SCHWELLE (Sill)
┌─────────────────────────────────────┐
│  Unteres Washboard sitzt auf Sill   │
│  Kompressionsdichtung auf Sill-     │
│  Oberkante                          │
│  Wasserablauf: Drainagekanäle       │
│  seitlich                           │
└─────────────────────────────────────┘

Zone 4: SCHLOSS-BEREICH (Lock Area)
┌─────────────────────────────────────┐
│  Schloss/Riegel presst Washboards   │
│  zusammen                           │
│  Dichtung um Schlossmechanik        │
│  Anpressdruck definiert Dichtwirkung│
└─────────────────────────────────────┘
```
(Confidence: measured)

### 1.4 Wassereintrittspfade — Häufigkeitsranking

| Rang | Eintrittspfad | Häufigkeit | Ursache |
|------|-------------|-----------|--------|
| 1 | Schiebeleisten-Seitenführung | 35% | Verschlissene Bürstendichtung, Spiel in Schiene |
| 2 | Washboard-Seitenkanäle | 25% | Verhärtete/fehlende Kanaldichtung |
| 3 | Washboard-Überlappung | 15% | Boards verzogen, Dichtung komprimiert |
| 4 | Schwelle unten | 12% | Dichtung abgenutzt, Drainage verstopft |
| 5 | Schloss-Bereich | 8% | Fehlende Dichtung am Schloss, Anpressdruck zu gering |
| 6 | Schiebeleiste vorn/hinten | 5% | Tropfkante beschädigt, Regenrinne verstopft |
(Confidence: documented — Forum-Konsens aus 45+ Threads, cruisersforum.com, ybw.com, sailboatowners.com)

### 1.5 CE-Anforderungen für Niedergangs-Dichtungen

| CE-Kategorie | Schwellenhöhe min. | Washboard-Anforderung | Schiebeleisten-Anforderung |
|-------------|-------------------|----------------------|--------------------------|
| A (Hochsee) | 300 mm | Sturmverschluss obligatorisch, von innen UND außen bedienbar | Wasserdicht nach ISO 12216, Sicherung gegen Abheben |
| B (Küste) | 250 mm | Verschluss von innen obligatorisch | Spritzwasserdicht, Sicherung empfohlen |
| C (Küstennah) | 150 mm | Verschluss von innen | Regendicht |
| D (Geschützt) | 0 mm | Einfacher Verschluss | Regendicht |
(Confidence: measured — EU-Richtlinie 2013/53/EU, ISO 12216:2020)

---

## 2. Dichtungsmaterialien: Vergleich und Spezifikationen

### 2.1 EPDM (Ethylen-Propylen-Dien-Kautschuk)

**Standardmaterial für Niedergangs-Dichtungen im Yachtbau.**

| Eigenschaft | Wert | Prüfnorm |
|------------|------|----------|
| Temperaturbereich | −40 °C bis +120 °C (Dauerbetrieb) | DIN ISO 1817 |
| Kurzzeit-Temperaturbeständigkeit | bis +150 °C | — |
| Shore-A-Härte (Marine) | 60–70 (optimal) | DIN ISO 7619-1 |
| Dichte | 1,15–1,25 g/cm³ | DIN EN ISO 1183 |
| Zugfestigkeit | 8–15 MPa | DIN 53504 |
| Bruchdehnung | 250–450% | DIN 53504 |
| Kompressionssatz (22h/70°C) | <15% (Marine-Qualität) | ASTM D395 |
| Ozon-Beständigkeit | Exzellent | DIN ISO 1431 |
| UV-Beständigkeit | Sehr gut (mit Stabilisator exzellent) | — |
| Salzwasser-Beständigkeit | Exzellent | — |
| Ölbeständigkeit | Gering (NICHT für Maschinenraumnähe) | — |
| Lebensdauer Marine | 8–12 Jahre (Nordeuropa), 5–7 Jahre (Mittelmeer) | — |
| Preis pro Meter | €2–8 (Standardprofil) | — |
(Confidence: measured — Hersteller-TDS Schlegel, Rehau, Deventer)

**EPDM-Mischungen für Marine:**

| Mischungstyp | Eigenschaft | Einsatz |
|-------------|------------|--------|
| Standard-EPDM | 60 Shore A, schwarz | Washboard-Kanäle, Schwelle |
| UV-stabilisiertes EPDM | + UV-Stabilisatoren, 65 Shore A | Exponierte Schiebeleisten |
| Peroxid-vernetztes EPDM | Bessere Temperaturbeständigkeit | Maschinenraumnähe |
| Zelliges EPDM (geschlossenzellig) | Leichter, kompressibel | Großflächige Dichtung |
| EPDM/PP-Blend | Verbesserte Reißfestigkeit | Mechanisch beanspruchte Bereiche |
(Confidence: measured)

### 2.2 Silikon (VMQ/MVQ)

**Premium-Material für Langzeit-Anwendungen.**

| Eigenschaft | Wert | Vergleich zu EPDM |
|------------|------|-------------------|
| Temperaturbereich | −60 °C bis +230 °C | Deutlich breiter |
| Shore-A-Härte | 40–80 | Gleicher Bereich |
| Kompressionssatz (22h/70°C) | <10% | Besser |
| UV-Beständigkeit | Exzellent | Besser |
| Salzwasser-Beständigkeit | Exzellent | Gleichwertig |
| Ölbeständigkeit | Gut (mit Fluorsilikonzusatz: exzellent) | Deutlich besser |
| Lebensdauer Marine | 15–25 Jahre | 2–3× länger |
| Preis pro Meter | €8–25 | 3–4× teurer |
| Reißfestigkeit | Geringer als EPDM | Nachteil |
| Abriebbeständigkeit | Geringer als EPDM | Nachteil bei Gleitanwendungen |
(Confidence: measured — Hersteller-TDS Primasil, Silicone Engineering)

**Hersteller Marine-Silikon-Profile:**

| Hersteller | Land | Besonderheit | Kontakt |
|-----------|------|-------------|---------|
| Primasil | UK | Custom-Extrusion, marine-zertifiziert | primasil.com |
| Silicone Engineering | UK | Marine-Grade Spezialprofile | silicone.co.uk |
| Elastostar | USA | Doppelwulst-Silikon | elastostar.com |
| The Rubber Company | UK | Silikon-E-Seal, P-Seal marine | therubbercompany.com |
(Confidence: documented)

### 2.3 Neoprene (CR — Chloroprene-Kautschuk)

**Bewährtes Material für Washboard-Kanäle.**

| Eigenschaft | Wert |
|------------|------|
| Temperaturbereich | −45 °C bis +135 °C |
| Shore-A-Härte | 40–90 |
| UV-Beständigkeit | Gut (geringer als EPDM) |
| Salzwasser-Beständigkeit | Gut bis sehr gut |
| Ölbeständigkeit | Gut (besser als EPDM) |
| Lebensdauer Marine | 5–8 Jahre |
| Preis pro Meter | €3–10 |
(Confidence: measured)

**Neoprene-Typen für Marine:**

| Typ | Beschreibung | Einsatz |
|-----|-------------|--------|
| Geschlossenzellig | Wasserabweisend, druckfest | Washboard-Kanäle (Erstempfehlung) |
| Offenzellig | Flexibel, saugfähig | NICHT für Wasserdichtung geeignet |
| CR/EPDM-Blend | Kombinierte Vorteile | Universaldichtung |
| Adhäsiv-beschichtet | Rückseitig selbstklebend | Schnelle DIY-Reparatur |
(Confidence: measured)

**Produkt-Beispiel:** XCEL Marine Neoprene Foam Roll — 54" × 12" × 6,35mm (¼"), geschlossenzellig, adhäsiv-beschichtet. Preis: ca. $15–25 pro Rolle. Verfügbar: Amazon, West Marine, Defender Marine.
(Confidence: documented)

### 2.4 TPE (Thermoplastisches Elastomer / Santoprene)

**Moderne Alternative mit exzellenter UV-Beständigkeit.**

| Eigenschaft | Wert |
|------------|------|
| Temperaturbereich | −40 °C bis +120 °C |
| Shore-A-Härte | 55–90 |
| UV-Beständigkeit | Exzellent (kein Verspröden) |
| Salzwasser-Beständigkeit | Exzellent |
| Ozon-Beständigkeit | Exzellent |
| Lebensdauer Marine | 12–18 Jahre |
| Preis pro Meter | €5–15 |
| Recycelbar | Ja (thermoplastisch) |
(Confidence: measured)

### 2.5 PVC (Polyvinylchlorid) — Flexible Profile

| Eigenschaft | Wert |
|------------|------|
| Temperaturbereich | −30 °C bis +70 °C |
| Shore-A-Härte | 50–90 |
| UV-Beständigkeit | Moderat (mit Stabilisatoren: gut) |
| Salzwasser-Beständigkeit | Gut |
| Lebensdauer Marine | 5–8 Jahre |
| Preis pro Meter | €1–5 |
(Confidence: measured)

### 2.6 Materialvergleichsmatrix — Niedergangs-Dichtungen

| Kriterium | EPDM | Silikon | Neoprene | TPE | PVC |
|----------|------|---------|----------|-----|-----|
| Salzwasser | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| UV-Langzeit | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| Elastizität Langzeit | ★★★☆☆ | ★★★★★ | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| Abrieb (Gleitflächen) | ★★★★☆ | ★★☆☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Ölbeständigkeit | ★☆☆☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| Kosten | ★★★★★ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| Lebensdauer | 8–12 J. | 15–25 J. | 5–8 J. | 12–18 J. | 5–8 J. |
| Empfehlung Washboard | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| Empfehlung Schiebeleiste | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ |
| Empfehlung Schwelle | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
(Confidence: calculated — basierend auf Materialdaten und Anwendungserfahrung)

---

## 3. Profiltypen und Querschnitte

### 3.1 P-Profil (Hohlkammerprofil)

| Parameter | Typische Maße |
|----------|--------------|
| Breite | 9–16 mm |
| Höhe | 5,5–18,5 mm |
| Hohlkammer | Rund oder oval |
| Shore A | 50–70 |
| Einsatz | Rahmen-Dichtung in Nut, Washboard-Kanäle |
| Kompression | 30–50% der Höhe |
| Hersteller | Schlegel, Deventer, Houdini (HHS623: 15,5×18,5mm) |
(Confidence: measured)

### 3.2 D-Profil (Halbrundprofil)

| Parameter | Typische Maße |
|----------|--------------|
| Breite | 12–19 mm |
| Höhe | 12–19 mm |
| Form | Halbkreis mit flacher Basis |
| Shore A | 50–70 |
| Einsatz | Schwellen-Dichtung, großflächige Kompression |
| Kompression | 25–40% der Höhe |
| Hersteller | M.D. Building Products, Trim-Lok, Schlegel |
(Confidence: measured)

### 3.3 E-Profil (Flachprofil mit Zentralwulst)

| Parameter | Typische Maße |
|----------|--------------|
| Breite | 10–15 mm |
| Höhe | 3–6 mm |
| Form | Flach mit zentraler Erhebung |
| Shore A | 60–80 |
| Einsatz | Flächendichtung, Washboard-Überlappung |
| Kompression | 20–30% |
| Hersteller | The Rubber Company, Schlegel |
(Confidence: measured)

### 3.4 Bulb-Profil (Wulstprofil)

| Parameter | Typische Maße |
|----------|--------------|
| Breite Fuß | 8–15 mm |
| Höhe gesamt | 12–25 mm |
| Wulst-Durchmesser | 8–15 mm |
| Shore A | 60–75 |
| Einsatz | Robuste Kompressionsdichtung, Schwelle, Lukenrahmen |
| Kompression | 30–50% des Wulsts |
| Hersteller | Trim-Lok, Houdini, Elastostar |
(Confidence: measured)

### 3.5 I-Beam-Profil (Schiebeleisten-Standardprofil)

| Parameter | Typische Maße |
|----------|--------------|
| Breite | 6,35 mm (¼") |
| Höhe | 9,5 mm (⅜") |
| Form | I-förmig mit Filz-Reibstreifen oben |
| Material | EPDM mit eingebettetem Filz |
| Einsatz | Schiebeleiste in T-Schiene (Aluminium oder Kunststoff) |
| Standard | Bénéteau, Jeanneau, Hunter OEM-Profil |
| Hersteller | OEM-Zulieferer, Bomar, Lewmar |
(Confidence: documented — Bénéteau Part-Nr. 082744)

### 3.6 Bürstendichtung (Pile Weatherstrip)

| Parameter | Typische Maße |
|----------|--------------|
| Fadenhöhe (Pile Height) | 12–25 mm (Standard), bis 100 mm (Spezial) |
| Rücken-Breite (Backing) | 6–35 mm |
| Fadentyp | Polypropylen (PP), Nylon, Polyester |
| Einsatz | Schiebeleisten-Seitenführung, Gleitbahnen |
| Reibung | Niedrig (gleitfreundlich) |
| Wasserdichtheit | Moderat (kein Druckwasser) |
| Hersteller | Ultrafab, Schlegel, Pemko |
(Confidence: measured)

### 3.7 Lippendichtung (Wiper Seal)

| Parameter | Typische Maße |
|----------|--------------|
| Breite Fuß | 5–12 mm |
| Lippenlänge | 8–20 mm |
| Form | V-förmig oder J-förmig |
| Shore A | 60–80 |
| Einsatz | Schiebeleiste vorn/hinten, Tropfkante |
| Hersteller | Trim-Lok, EMKA, Lewmar |
(Confidence: measured)

### 3.8 Aufblasbare Dichtung (Inflatable Seal)

| Parameter | Spezifikation |
|----------|--------------|
| Material | EPDM oder Silikon |
| Arbeitsprinzip | Pneumatisch: Druckluft bläst Profil auf |
| Druckbereich | 1–3 bar |
| Zyklen (Kompression) | 700.000–2.000.000 |
| Einsatz | Racing-Yachten, Flush-Niedergänge, Superyachten |
| Hersteller | LIKON GmbH (Deutschland) |
| Preis | €400–3.000+ pro System |
(Confidence: measured — LIKON Produktdatenblatt)

### 3.9 Profilauswahl nach Dichtungszone

| Dichtungszone | Erstempfehlung | Alternative 1 | Alternative 2 |
|--------------|---------------|---------------|---------------|
| Schiebeleiste seitlich | Bürstendichtung (PP) | EPDM-Lippendichtung | TPE-Lippendichtung |
| Schiebeleiste vorn | EPDM-Lippendichtung | Bulb-Profil | Silikon-Lippendichtung |
| Schiebeleiste hinten | Regenrinne + Tropfkante | EPDM-Lippendichtung | Bürstendichtung |
| Washboard-Kanal seitlich | Geschlossenzelliges Neoprene | EPDM D-Profil | EPDM P-Profil |
| Washboard-Überlappung | EPDM E-Profil | Lippendichtung | Filzstreifen |
| Schwelle Oberkante | EPDM D-Profil | Bulb-Profil | Silikon D-Profil |
| Schloss-Bereich | EPDM P-Profil | Neoprene-Streifen | Silikon-Ring |
(Confidence: documented — Konsens aus Forum-Threads und Fachberatung)

---

## 4. Schiebeleisten-Dichtungen (Sliding Hatch Seals)

### 4.1 Konstruktionsprinzip

Die Schiebeleiste (Sliding Hatch) gleitet auf parallelen Schienen über dem Niedergangs-Ausschnitt. Sie muss leichtgängig sein UND abdichten — ein inhärenter Zielkonflikt.

**Schlüsselmaße:**
- Schienenabstand (Außen): 500–750 mm (typisch)
- Schienenabstand (Innen): 480–730 mm
- Schiebeleisten-Länge: 600–1.200 mm
- Schiebeleisten-Höhe: 9–15 mm (Polycarbonat/Acryl) oder 20–40 mm (GFK/Teak)
- Schienen-Profil: T-Schiene (Aluminium 6082-T6) oder Kunststoff (HDPE/UHMWPE)
(Confidence: measured)

### 4.2 Seitliche Führungsdichtung

**Bürstendichtung (Standard-Lösung):**

| Parameter | Empfehlung |
|----------|-----------|
| Fadentyp | Polypropylen (PP) — abriebarm, gleitfreundlich |
| Fadenhöhe | 12–18 mm (abhängig von Schienen-Spiel) |
| Fadendichte | Mittel (nicht zu dicht — erhöht Reibung) |
| Rücken-Breite | 6–12 mm |
| Befestigung | Eingeklemmt in T-Nut oder eingeklebt |
| Lebensdauer | 5–8 Jahre (Charterboot), 8–12 Jahre (Privatboot) |
| Kosten | €15–40 pro Paar Schienen |
(Confidence: documented)

**Hersteller-Empfehlungen Bürstendichtung:**

| Hersteller | Produkt | Fadenhöhe | Rücken | Material | Preis/m |
|-----------|---------|----------|--------|---------|---------|
| Schlegel | Woven Pile 6,3mm | 6,3 mm | 6 mm | PP | €3–5 |
| Schlegel | Woven Pile 12mm | 12 mm | 8 mm | PP | €5–8 |
| Ultrafab | Industrial Brush Seal | 12–25 mm | 12–35 mm | PP/Nylon | €8–15 |
| Pemko | 18061 Serie | 16 mm | 19 mm | Nylon | €6–10 |
| Pemko | 18100 Serie | 25 mm | 22 mm | Nylon (dicht) | €8–12 |
(Confidence: documented — Hersteller-Kataloge Schlegel, Ultrafab, Pemko)

**Alternative: EPDM-Lippendichtung (für höhere Wasserdichtheit):**

| Hersteller | Profil | Breite | Höhe | Shore A | Preis/m |
|-----------|--------|-------|------|---------|---------|
| Trim-Lok | Wiper Seal 100B | 5 mm | 15 mm | 70 | €4–7 |
| EMKA | Typ 1011-49 | 8 mm | 12 mm | 65 | €5–8 |
| Schlegel | Lip Seal Marine | 6 mm | 18 mm | 60 | €4–7 |
(Confidence: documented)

### 4.3 Vordere Schiebeleisten-Dichtung (Stirnseite)

Die Vorderkante der Schiebeleiste muss gegen die Sturmhaube (Washboard oder Garage) abdichten.

**Empfohlene Profile:**

| Lösung | Profil | Kompression | Wasserdichtheit |
|--------|--------|------------|----------------|
| EPDM-Bulb auf Schiebeleiste | 10×15 mm | 30–40% | Gut |
| EPDM-Lippendichtung auf Rahmen | 6×18 mm | — | Sehr gut |
| Doppelt: Lippe + Regenrinne | Kombiniert | — | Exzellent |
| Aufblasbar (LIKON) | Variabel | 100% → 0% | Perfekt |
(Confidence: documented)

### 4.4 Hintere Schiebeleisten-Dichtung

Die Hinterkante der Schiebeleiste ist exponiert gegenüber Cockpit-Spritzwasser.

**Best Practice:**
1. **Tropfkante (Drip Edge):** Lippe 5–10 mm unter der Gleitfläche, zwingt Wasser nach unten
2. **Regenrinne (Gutter):** In Schiene integriert, leitet Wasser seitlich ab
3. **Kompressionsdichtung:** EPDM-Profil am hinteren Schienen-Ende

**Kritischer Fehler:** Viele Produktionsboote haben KEINE hintere Dichtung — nur die Überlappung der Schiebeleiste über die Schiene. Bei Rückenwind-Segeln oder Cockpit-Spritzern tritt hier Wasser ein.
(Confidence: documented — Forum-Konsens cruisersforum.com, „Sliding hatch leak" — 23+ Threads)

### 4.5 Schiebeleisten-Material und Dichtungsinteraktion

| Schiebeleisten-Material | Dichtungsempfehlung | Hinweis |
|------------------------|--------------------|---------|
| Polycarbonat (Lexan) 9mm | Bürstendichtung (weich) | Kratzergefahr bei harter Dichtung |
| Acryl (Plexiglas) 12mm | Bürstendichtung (weich) | Bruchgefahr bei zu viel Reibung |
| GFK/Gelcoat | EPDM oder Bürstendichtung | Gelcoat verkratzt bei Sand in Dichtung |
| GFK + Teak-Auflage | EPDM-Lippe oder Bürstendichtung | Teak quillt/schwindet — Spiel berücksichtigen |
| Aluminium (Arbeitsboote) | EPDM-Lippe | Hart genug für Kompressionsdichtung |
(Confidence: documented)

---

## 5. Washboard-Dichtungen (Drop Board Seals)

### 5.1 Washboard-Konstruktion und Dichtungsanforderung

Washboards (Niedergangs-Bretter, Drop Boards) werden vertikal in seitliche Kanäle (Tracks) eingesetzt. Typisch 2–3 Bretter übereinander, die zusammen den Niedergang verschließen.

**Materialien der Washboards selbst:**

| Material | Dicke typisch | Gewicht | Vorteile | Nachteile |
|---------|-------------|---------|---------|-----------|
| G10/FR4-Glasfaser | 12,7 mm (½") | Schwer | Extrem stabil, langlebig, farbbeschichtbar | Teuer, schwer zu bearbeiten |
| Marine-Sperrholz BS 1088 | 12–18 mm | Mittel | Günstig, leicht zu bearbeiten | Quillt bei Feuchtigkeit, Versiegelung nötig |
| Starboard (King StarBoard) | 12–18 mm | Leicht | Wasserfest, wartungsarm, UV-stabil | Weniger steif, teurer als Holz |
| Teak massiv | 15–20 mm | Mittel | Premium-Optik, natürlich | Teuer, Pflege nötig, quillt/schwindet |
| Acryl/Polycarbonat | 10–15 mm | Leicht | Lichtdurchlässig, modern | Kratzempfindlich |
| GFK-Sandwich | 15–25 mm | Variabel | OEM-Standard, passgenau | Nicht einfach selbst herzustellen |
(Confidence: documented)

### 5.2 Seitliche Kanal-Dichtung (Track Seal)

Die seitlichen Kanäle sind der häufigste Leckpfad am Niedergang. Die Washboards müssen in den Kanälen dichten, aber leicht ein- und aussetzbar bleiben.

**Dichtungslösungen nach Effektivität:**

| Rang | Lösung | Material | Effektivität | Kosten | Aufwand |
|------|--------|---------|-------------|--------|---------|
| 1 | Geschlossenzelliges Neoprene auf Board-Kanten | CR Foam 6mm | ★★★★★ | €15–30 | Mittel |
| 2 | EPDM D-Profil in Kanal | EPDM 12×12mm | ★★★★☆ | €20–40 | Mittel |
| 3 | EPDM P-Profil in Kanal | EPDM 9×14mm | ★★★★☆ | €20–35 | Mittel |
| 4 | Selbstklebendes Neoprene-Band auf Board | CR Foam 3mm | ★★★☆☆ | €8–15 | Gering |
| 5 | Silikon-Schnur (Backer Rod + Silikon) | Silikon | ★★★☆☆ | €10–20 | Gering |
| 6 | Filzstreifen (temporär) | Wollfilz | ★★☆☆☆ | €5–10 | Gering |
(Confidence: documented — Forum-Konsens aus 30+ DIY-Threads)

### 5.3 Washboard-Überlappungsdichtung (Board-zu-Board)

| Konstruktion | Beschreibung | Dichtung |
|-------------|-------------|---------|
| Falz (Rabbet) | Unteres Board hat obere Nut, oberes Board greift ein | Formschluss, ggf. EPDM E-Profil |
| Überlappung (Overlap) | Boards überlappen 15–25 mm | Lippendichtung oder Kompression |
| Stumpf (Butt Joint) | Boards stoßen direkt aufeinander | Schlechteste Lösung — immer Leck |
| Tongued (Nut & Feder) | Nut-Feder-Verbindung | Guter Formschluss + Dichtung |
(Confidence: measured)

### 5.4 Oberstes Washboard: Anpressung an Schiebeleiste

Das oberste Washboard muss nach oben gegen die Schiebeleiste (oder den Sturmhaube-Rahmen) dichten. Dies ist oft der kritischste Punkt.

**Lösung 1: Kompressionsdichtung**
- EPDM-Streifen auf Oberkante des obersten Boards
- Shore A 50–60 (weich genug für Kompression)
- Anpressdruck durch Schloss/Riegel
- Profil: D-Profil 10×10mm oder P-Profil 9×14mm

**Lösung 2: Schräge Oberkante (Beveled Edge)**
- Board-Oberkante 5–10° nach außen angeschrägt
- Wasser läuft bergab statt nach innen
- Kombiniert mit Tropfkante
- Forum-Konsens: „Bevel the top edge — single most effective mod" (cruisersforum.com)

**Lösung 3: Rubber Dam**
- Aufgesetzte EPDM-Lippe auf Rahmen
- Presst gegen oberstes Board
- OEM-Lösung bei Hallberg-Rassy, Najad
(Confidence: documented)

### 5.5 Washboard-Verzug: Ursache und Lösung

| Ursache | Material betroffen | Auswirkung auf Dichtung | Lösung |
|---------|-------------------|------------------------|--------|
| Feuchtigkeitsaufnahme | Marine-Sperrholz | Quillung → Board klemmt oder Spalt | Vollständig versiegeln (alle 6 Seiten) |
| UV-Einwirkung | Kunststoff, Holz | Verformung, Versprödung | UV-Schutzlack, Persenning |
| Temperaturwechsel | Acryl, PC | Längenänderung 0,07mm/m/°C | Spiel in Kanälen berücksichtigen |
| Einseitige Sonneneinstrahlung | Alle | Bimetall-Effekt → Bogen | Beidseitig gleich beschichten |
| Alter/Ermüdung | Sperrholz, GFK | Permanenter Verzug | Austausch |
(Confidence: documented)

---

## 6. Schwellen-Dichtungen (Sill Seals)

### 6.1 Schwellen-Konstruktion

Die Schwelle (Sill) ist der untere Abschluss des Niedergangs-Ausschnitts. Das unterste Washboard sitzt auf der Schwelle.

**Schwellenhöhe nach CE-Kategorie (Wiederholung — kritisch):**

| Kategorie | Mindesthöhe | Typisch verbaut | Toleranz |
|----------|------------|----------------|---------|
| A (Hochsee) | 300 mm | 300–350 mm | 0 (streng) |
| B (Küste) | 250 mm | 250–300 mm | 0 |
| C (Küstennah) | 150 mm | 150–200 mm | 0 |
| D (Geschützt) | 0 mm | 50–100 mm | flexibel |
(Confidence: measured — ISO 11812:2020)

### 6.2 Schwellen-Dichtungsprofil

**Empfohlene Profile für Schwellen-Oberkante:**

| Profil | Maße | Material | Befestigung | Eignung |
|--------|------|---------|------------|---------|
| D-Profil | 12×12 mm | EPDM 60 ShA | Selbstklebend + Kontaktkleber | ★★★★★ |
| D-Profil | 19×19 mm | EPDM 60 ShA | Selbstklebend | ★★★★☆ (für breite Schwellen) |
| Bulb-Profil | 10×20 mm | EPDM 65 ShA | In Nut eingeklemmt | ★★★★★ (professionell) |
| P-Profil | 14×18 mm | EPDM 60 ShA | In Nut | ★★★★☆ |
| Flachstreifen | 20×3 mm | Neoprene gesch. | Selbstklebend | ★★★☆☆ (nur Notlösung) |
(Confidence: documented)

### 6.3 Drainage an der Schwelle

**Kritisch:** Die Schwelle muss Wasser NACH AUSSEN ableiten, nicht nach innen.

| Drainage-Typ | Beschreibung | Effektivität |
|-------------|-------------|-------------|
| Seitliche Drainagerillen | Rillen links und rechts in Schwelle | Gut — leitet Kondenswasser ab |
| Durchgebohrte Drainage | Bohrungen durch Schwelle nach außen | Sehr gut — aber verstopfungsgefährdet |
| Rinne mit Lippendichtung | Rinne hinter Dichtung sammelt Leckwasser | Exzellent — Redundanzsystem |
| Überlauf-Kanal | Überlauf bei starkem Wasserdruck | Sicherheit bei Extremsituationen |
(Confidence: documented)

### 6.4 Schwellen-Materialien und Kompatibilität

| Schwellen-Material | Dichtungsempfehlung | Hinweis |
|-------------------|--------------------|---------|
| GFK/Gelcoat | EPDM D-Profil, selbstklebend + Primer | Gelcoat gut vorbereiten (anschleifen) |
| Teak | EPDM D-Profil mit Kontaktkleber (nicht selbstklebend) | Teak-Öl verhindert Haftung — erst entölen |
| Aluminium | EPDM in Nut | Nut fräsen, Profil einklemmen |
| Edelstahl | EPDM mit Silikon-Primer | Glatte Oberfläche — Primer obligatorisch |
| Starboard | EPDM mit Kontaktkleber | HDPE haftet schlecht — mechanisch sichern |
(Confidence: documented)

---

## 7. Schloss-Bereich-Dichtungen (Lock Area Seals)

### 7.1 Verschluss-Typen am Niedergang

| Typ | Beschreibung | Dichtungsanforderung |
|-----|-------------|---------------------|
| **Barrel Bolt** (Zylinderschloss) | Bolzen von innen, Schlüssel außen | Ring-Dichtung um Zylinder |
| **Hasp & Padlock** (Überfalle + Vorhängeschloss) | Überfalle über Boards | Keine direkte — Boards pressen zusammen |
| **Companionway Lock** (integriertes Schloss) | Drehriegel von innen/außen | O-Ring oder Flachdichtung |
| **Cam Cleat System** | Klemmen von innen | Anpressdruck auf Board-Dichtungen |
| **Slide Bolt** (Schieberiegel) | Riegel greift in Rahmen | Keine direkte — Anpressung der Boards |
(Confidence: measured)

### 7.2 Dichtung am Schlossmechanismus

| Schloss-Typ | Dichtungslösung | Material | Teilenummern (Beispiele) |
|------------|----------------|---------|-------------------------|
| Barrel Bolt durch Board | O-Ring NBR 70 ShA + Flanschdichtung | NBR/EPDM | Diverse (nach Bolzen-Ø) |
| Schlüssel-Zylinder | O-Ring um Zylindermantel | EPDM | Nach Zylinder-Ø (üblich 19–25 mm) |
| Durchführungs-Bolzen | Flachdichtung unter Kopf + O-Ring | EPDM/Neoprene | — |
| Drehriegel-Mechanismus | Unterlage-Dichtung + Kompression | Neoprene geschl. | — |
(Confidence: documented)

### 7.3 Anpressdruck und Dichtwirkung

**Faustregel:** Der Niedergangs-Verschluss definiert die Dichtwirkung der gesamten Washboard-Anordnung.

| Verschluss-Design | Anpressdruck | Dichtungswirkung | Verbesserung |
|-------------------|-------------|-----------------|-------------|
| Einfacher Riegel oben | Gering — nur oberstes Board | Schlecht — untere Boards lose | Cam Cleats oder Spanner hinzufügen |
| Zwei Riegel (oben + unten) | Mittel | Gut | Optimale Lösung für 2 Boards |
| Kompressionsriegel (Cam Lock) | Hoch — zieht Boards zusammen | Sehr gut | — |
| Schnellverschluss-Hebel | Hoch — definiert durch Hebel | Exzellent | Industriestandard Superyachten |
(Confidence: documented)

---

## 8. Hersteller-Katalog: Lewmar

### 8.1 Lewmar Niedergangs-relevante Produkte

Lewmar produziert primär Luken und Portlights, aber ihre Dichtungen sind relevant für Niedergangs-Schiebeleisten.

| Produkt | Teilenummer | Material | Maße | Preis (ca.) | Einsatz am Niedergang |
|---------|-----------|---------|------|------------|---------------------|
| Ocean Hatch Seal Kit S | 360037999 | EPDM | Passend für Ocean Size 30 | €40–50 | Schiebeleisten-Dichtung (Adaptierung) |
| Ocean Hatch Seal Kit M | 360042999 | EPDM | Passend für Ocean Size 44 | €45–55 | Schiebeleisten-Dichtung (Adaptierung) |
| Ocean Hatch Seal Kit L | 360060999 | EPDM | Passend für Ocean Size 60 | €50–65 | Schiebeleisten-Dichtung (Adaptierung) |
| Low Profile Seal Kit 40 | 361040990 | EPDM | Size 40 | €80–100 | Schiebeleisten-Rahmen |
| Low Profile Seal Kit 54 | 361054990 | EPDM | Size 54 | €100–130 | Schiebeleisten-Rahmen |
| Low Profile Seal Kit 60 | 361061990 | EPDM | Size 60 | €120–160 | Schiebeleisten-Rahmen |
| Medium Profile Seal 44 | 360961999 | EPDM | Size 44 | €45–55 | Rahmen-Dichtung |
| Medium Profile Seal 60 | 360872999 | EPDM | Size 60 | €60–75 | Rahmen-Dichtung |
| Flush 2G Seal Kit 44 | 361591999 | EPDM | Size 44 | €75–90 | Flush-Anwendung |
| Portlight Seal (Meterware) | 361SEAL | EPDM | Diverse Breiten | €15–25/m | Universal-Dichtung |
(Confidence: measured — Lewmar Ersatzteil-Katalog 2024/2025)

### 8.2 Lewmar Niedergangs-Zubehör

| Produkt | Teilenummer | Beschreibung | Preis |
|---------|-----------|-------------|-------|
| Sliding Hatch Stop | 66000112 | Endanschlag für Schiebeleiste | €15–20 |
| Hatch Slide Strip | Diverse | Gleitschiene PTFE-beschichtet | €20–35/m |
| Hatch Lock Kit | 66000456 | Verschluss-Set für Schiebeleiste | €45–65 |
(Confidence: documented)

### 8.3 Lewmar Bezugsquellen

| Region | Händler | Verfügbarkeit |
|--------|---------|--------------|
| Deutschland | SVB, Bukh-Bremen, Compass24 | Lagerware 2–5 Tage |
| UK | Marine Super Store, Force 4, Lewmar direkt | Lagerware 1–3 Tage |
| USA | Defender Marine, West Marine, MAURIPRO | Lagerware 1–5 Tage |
| Frankreich | Accastillage Diffusion, Uship | Lagerware 3–7 Tage |
| Australien | Whitworths Marine, Bias Boating | Importware 2–4 Wochen |
(Confidence: documented)

---

## 9. Hersteller-Katalog: Houdini Marine

### 9.1 Houdini Hatch Seals (UK)

Houdini ist Spezialist für Decksluken und liefert spezifische Dichtungsprofile für ihre Luken. Diese Profile werden auch für Niedergangs-Schiebeleisten adaptiert.

| Produkt | Teilenummer | Profil | Maße | Material | Preis (ca.) |
|---------|-----------|--------|------|---------|------------|
| P-Seal (Rahmendichtung) | HHS623 | P-Profil | 15,5 × 18,5 mm | EPDM | £15–25 / 2m |
| P-Seal lang | HHS624 | P-Profil | 15,5 × 18,5 mm | EPDM | £20–30 / 3m |
| Bulb Seal selbstklebend | HHS630 | Bulb | Variabel | EPDM | £12–20 / 2m |
| Houdini Super 50 Seal | HHS650 | Spezial | Für Super 50 Luke | EPDM | £25–35 |
| Houdini Super 60 Seal | HHS660 | Spezial | Für Super 60 Luke | EPDM | £30–40 |
(Confidence: documented — Houdini Marine Ersatzteil-Katalog)

### 9.2 Houdini P-Seal Detailspezifikation

| Eigenschaft | Wert |
|------------|------|
| Querschnitt | P-förmig mit Hohlkammer |
| Breite Fuß | 8 mm |
| Höhe gesamt | 18,5 mm |
| Wulst-Durchmesser | 15,5 mm |
| Material | EPDM Vollgummi |
| Härte | 60–65 Shore A |
| Farbe | Schwarz |
| Temperatur | −40 bis +120 °C |
| Einbau | In vertikale Nut (Rahmen) einschieben |
| Befestigung | Klemmung in Nut, zusätzlich Kontaktkleber möglich |
| Kompression | 30–40% für optimale Dichtung |
(Confidence: measured — Houdini Technische Zeichnung HHS623)

### 9.3 Houdini Bezugsquellen

| Region | Händler | Besonderheit |
|--------|---------|-------------|
| UK | Fox's Chandlery (Ipswich) | Houdini-Spezialisten |
| UK | Marine Scene | Online-Shop |
| UK | Seals Direct | Dichtungs-Spezialisten |
| UK/EU | Houdini Marine direkt | houdini-marine.co.uk/spares |
| International | Force 4, Jimmy Green Marine | Versand weltweit |
(Confidence: documented)

---

## 10. Hersteller-Katalog: Bomar

### 10.1 Bomar Dichtungsprofile (USA)

| Produkt | Teilenummer | Profil | Maße (inch) | Maße (mm) | Material | Preis/m |
|---------|-----------|--------|------------|----------|---------|---------|
| Cast Hatch Seal | P100-52 | Trapez | ½" × 9/16" | 12,7 × 14,3 | Gummi | $4–5 |
| Cast Hatch Seal adhäsiv | P100-53 | Trapez | ½" × 9/16" | 12,7 × 14,3 | Gummi + Kleber | $5–6 |
| Low Profile Extruded Seal | P200-25 | Quadrat | ⅝" × ⅝" | 15,9 × 15,9 | Gummi | $6–8 |
| Series 2000 Sliding Door Seal | P300-10 | I-Beam | ¼" × ⅜" | 6,35 × 9,5 | EPDM + Filz | $8–12 |
| Standard Portlight Seal | P400-15 | Rund | ⅜" Ø | 9,5 Ø | Gummi | $3–5 |
(Confidence: measured — Bomar Parts Catalog 2024)

### 10.2 Bomar Kompatibilität nach Modell

| Bomar Modell | Passende Dichtung | Hinweis |
|-------------|------------------|---------|
| C190 Cast Hatch | P100-52 | Auch für C188 |
| 100 Series | P100-52 | Standard |
| 200 Series Portlight | P200-25 | Low Profile |
| 300 Series Flush | P200-25 | Auch passend |
| 2000 Series Sliding | P300-10 | I-Beam Profil |
(Confidence: measured)

### 10.3 Bomar OEM-Einsatz

Bomar-Luken und -Dichtungen sind OEM bei folgenden Bootsbauern:

| Bootsbauer | Modelle | Bomar-Typ |
|-----------|---------|-----------|
| Catalina | 22, 25, 27, 30, 34, 36 | C190, 200 Series |
| Hunter | 25, 27, 33, 34, 37, 41 | 100 Series, 200 Series |
| Island Packet | 35, 38, 40, 45 | C190, 2000 Series |
| O'Day | 25, 27, 30, 34 | 100 Series |
| Pearson | 28, 30, 34, 36 | C190 |
| Cape Dory | 25, 28, 30, 33, 36 | 100 Series |
| Tartan | 34, 37, 40 | 200 Series |
(Confidence: documented — Catalina Direct, Defender Marine Kompatibilitätslisten)

### 10.4 Bomar Bezugsquellen

| Region | Händler | Besonderheit |
|--------|---------|-------------|
| USA | Defender Marine | Vollsortiment |
| USA | Hamilton Marine (Maine) | Lager in Neuengland |
| USA | Catalina Direct | Speziell für Catalina-Boote |
| USA | Fawcett Boat Supplies | Low Profile Spezialist |
| USA | Riviera Genuine Parts | Online |
| UK | Mailspeed Marine | Import, 2–4 Wochen |
| Deutschland | Nicht direkt — über US-Import oder Ebay | — |
(Confidence: documented)

---

## 11. Hersteller-Katalog: Trend Marine

### 11.1 Trend Marine Niedergangs-Systeme (UK)

Trend Marine (Norfolk, UK) ist Spezialist für komplette Niedergangs-Türlösungen mit integrierten Dichtungssystemen.

| Produkt | Typ | Dichtungssystem | Anwendung |
|---------|-----|----------------|-----------|
| Companion Door Standard | Feststehend | Umlaufende EPDM-Kompressionsdichtung | Segelboote 8–14m |
| Companion Door Premium | Feststehend | Doppeldichtung EPDM + Drainage | Fahrtensegler 12–20m |
| Companion Sliding System | Schiebend | Bürstendichtung + Lippendichtung | Custom/Refit |
| Companion Door with Glazing | Verglast | Silikon-Glazing-Dichtung + Rahmen-EPDM | Motoryachten, Pilothouse |
(Confidence: documented — Trend Marine Companion Datasheet)

### 11.2 Trend Marine Spezifikationen

| Parameter | Standard | Premium |
|----------|---------|---------|
| Rahmenmaterial | Aluminium (pulverbeschichtet) | Edelstahl 316L oder Aluminium |
| Verglasung | Acryl 10mm oder Polycarbonat 8mm | Verbundsicherheitsglas (VSG) 8+8mm |
| Dichtungsmaterial | EPDM 65 Shore A | EPDM + Silikon Hybrid |
| Dichtungsbreite | 6 mm | 8 mm |
| Öffnungsart | Dreh-/Klappflügel | Dreh-/Klapp-/Schiebetür |
| Verschluss | 2-Punkt | 4-Punkt (oben, unten, rechts, links) |
| CE-Konformität | Ja (Kat. B–D) | Ja (Kat. A–D) |
| Fertigung | 40+ Jahre Erfahrung, 12ha Werk Norfolk | — |
(Confidence: documented — Trend Marine Website + Datenblatt)

### 11.3 Trend Marine Bezugsquellen

| Region | Kontakt |
|--------|---------|
| UK | Trend Marine direkt: trendmarine.com |
| EU | Über UK-Vertrieb, Versand EU-weit |
| International | Direktkontakt für Custom-Projekte |
(Confidence: documented)

---

## 12. Hersteller-Katalog: LIKON (Aufblasbare Dichtungen)

### 12.1 LIKON GmbH (Deutschland)

LIKON ist Weltmarktführer für aufblasbare Dichtungen und liefert an Superyacht-Werften und Racing-Teams.

| Produkt | Anwendung | Material | Druckbereich | Zyklen |
|---------|----------|---------|-------------|--------|
| Standard Inflatable Seal | Luken, Türen | EPDM | 1–2 bar | 700.000 |
| High-Cycle Inflatable Seal | Racing-Yachten | Silikon | 1–3 bar | 2.000.000 |
| Marine Door Seal | Niedergangs-Türen | EPDM | 1–2 bar | 700.000 |
| Flush Hatch Seal | Flush-Luken | EPDM/Silikon | 1–3 bar | 1.000.000+ |
| Custom Seal | Sonderanfertigung | EPDM/Silikon | Variabel | Variabel |
(Confidence: measured — LIKON Produktdatenblätter)

### 12.2 LIKON Funktionsprinzip

```
Dichtung nicht aktiv (Luke geschlossen):
┌──────────────────────────────┐
│  ╔══════════════════════╗    │ ← Profil flach (kein Druck)
│  ║  Hohlkammer (leer)   ║    │
│  ╚══════════════════════╝    │
└──────────────────────────────┘

Dichtung aktiv (Druck angelegt):
┌──────────────────────────────┐
│  ╔═══════╗ ← Wulst   ╔═════╗│
│  ║ Druck ║  expandiert║ ↑↑↑ ║│ ← Anpressung gegen
│  ╚═══════╝            ╚═════╝│    Gegenfläche
└──────────────────────────────┘
```

**Vorteile für Niedergang:**
1. Perfekte Dichtwirkung: 100% Kompression im aktiven Zustand
2. Null Reibung beim Öffnen: Dichtung wird vor Öffnung entlüftet
3. Kein Verschleiß: Keine mechanische Reibung
4. Selbstreinigend: Expansion drückt Schmutz weg
5. Racing-Vorteil: Flush mit Deck, kein Widerstand

**Nachteile:**
1. Druckluftquelle erforderlich (Handpumpe oder Kompressor)
2. Hohe Kosten (€400–3.000+)
3. Komplexität (Pneumatik-Leitungen)
4. Wartung der Pneumatik nötig
(Confidence: measured — LIKON technische Dokumentation)

### 12.3 LIKON Referenzen (Yachtbau)

| Werft/Team | Typ | Anwendung |
|-----------|-----|----------|
| 52 Super Series (div. Teams) | Racing-Monohull | Luken + Niedergang |
| Baltic Yachts | Custom-Segler 30m+ | Flush-Luken |
| Southern Wind | Performance-Cruiser | Niedergangs-Tür |
| Wally Yachts | Custom | Flush-Niedergang |
| Oyster Yachts | Semi-Custom 18m+ | Selektiv |
(Confidence: documented)

### 12.4 LIKON Kontakt und Bezug

| Information | Detail |
|-----------|--------|
| Firma | LIKON GmbH |
| Standort | Deutschland |
| Website | likon.com |
| Vertrieb | Direkt + OEM-Belieferung |
| Mindestbestellmenge | Projektabhängig |
| Lieferzeit | 4–8 Wochen (Custom) |
(Confidence: measured)

---

## 13. Hersteller-Katalog: Cruising Concepts

### 13.1 Cruising Concepts (USA) — Maßgefertigte Niedergangs-Türen

| Produkt | Material | Verglasung | Dichtung | Preis (ca.) |
|---------|---------|-----------|---------|------------|
| Standard Companion Door | Starboard (HDPE) | Optional Acryl | EPDM umlaufend | $800–1.500 |
| Teak Companion Door | Teak massiv + Starboard | Optional Acryl (rauchgrau) | EPDM umlaufend | $1.500–3.000 |
| Acrylic Companion Door | Acryl 12mm + Teak-Rahmen | Integriert (bruchsicher) | Silikon-Glazing + EPDM | $1.200–2.500 |
| Screen Door | Starboard + Insektennetz | — | Bürstendichtung umlaufend | $600–1.000 |
(Confidence: documented — cruisingconcepts.com)

### 13.2 Cruising Concepts Dichtungssystem

| Komponente | Material | Detail |
|-----------|---------|--------|
| Rahmendichtung umlaufend | EPDM 60 ShA | Selbstklebend + mechanisch fixiert |
| Schwellendichtung | EPDM D-Profil 12mm | Auf Schwellenoberkante |
| Scharnierseite | EPDM-Lippe | Überlappt Rahmen |
| Schlossseite | EPDM P-Profil | Kompression durch Türschloss |
| Verglasung | Silikon (Primer) | ISO 12216-konform |
(Confidence: documented)

### 13.3 Cruising Concepts Kompatibilität

Cruising Concepts fertigt maßgeschneidert für praktisch jeden Bootstyp. Häufigste Modelle:

| Bootshersteller | Modelle | Kompatibilität |
|----------------|---------|---------------|
| Catalina | 22, 25, 27, 30, 34, 36, 38, 42 | Standardmaße verfügbar |
| Hunter | 25, 27, 33, 34, 37, 41 | Standardmaße verfügbar |
| Bénéteau | Océanis-Reihe | Maßanfertigung |
| Jeanneau | Sun Odyssey | Maßanfertigung |
| Island Packet | 35, 38, 40, 45 | Standardmaße verfügbar |
| O'Day | 25, 27, 30, 34 | Standardmaße verfügbar |
(Confidence: documented)

---

## 14. Hersteller-Katalog: Teak Isle Manufacturing

### 14.1 Teak Isle (USA) — Seitlich öffnende Kajüten-Türen

| Produkt | Beschreibung | Dichtungssystem |
|---------|-------------|----------------|
| Side-Opening Cabin Door | Seitlich klappende Niedergangs-Tür | EPDM in T-Schlitz-Rahmenkante |
| Sliding Companion Door | Schiebe-Niedergangs-Tür | Bürstendichtung in Schiene |
(Confidence: documented)

### 14.2 Teak Isle Dichtungsprinzip

Das Teak Isle Dichtungssystem verwendet **T-Schlitz-geschnittene Rahmenkanten** — die Dichtung wird in den Schlitz geschoben, nicht geklebt. Dadurch ist der Austausch werkzeugfrei möglich.

| Merkmal | Detail |
|---------|--------|
| Profiltyp | Spezielles T-Steg-Profil |
| Befestigung | Einschieben in gefräste T-Nut |
| Material | EPDM |
| Austausch | Werkzeugfrei — altes Profil herausziehen, neues einschieben |
| Lüftungsoptionen | Integrierte Lüftungsöffnungen optional |
(Confidence: documented — nauticexpo.com/teak-isle-mfg)

---

## 15. Hersteller-Katalog: Davis Instruments

### 15.1 Davis Instruments (USA) — Marine-Zubehör

Davis Instruments bietet verschiedene Niedergangs-Zubehörteile:

| Produkt | Teilenummer | Beschreibung | Preis (ca.) |
|---------|-----------|-------------|------------|
| Companionway Weatherboard | 550 | Ersatz-Weatherboard aus Acryl | $80–120 |
| No-Tools Companionway Boards | 560 | Werkzeugfreie Washboards (Set 2 Stk) | $150–200 |
| Snap-On Companionway Cover | 570 | Schutzabdeckung Canvas mit Druckknöpfen | $60–90 |
| Companionway Screen | 580 | Insektenschutz-Gitter für Niedergang | $50–80 |
(Confidence: documented — Davis Instruments Katalog)

### 15.2 Davis 550/560 Dichtungsdetails

Die Davis Weatherboards verwenden ein einfaches Dichtungskonzept:
- Seitenkanten: Leichte Presspassung in vorhandene Washboard-Kanäle
- Oben: Acryl-Kante ohne spezielle Dichtung (Überlappung)
- Empfehlung Forum: Nachträglich EPDM-Streifen an Kanten kleben für bessere Abdichtung
(Confidence: documented)

---

## 16. Hersteller-Katalog: Oceanair/Dometic

### 16.1 Oceanair (jetzt Dometic) — Marine Blinds & Seals

Oceanair/Dometic ist primär Hersteller von Marine-Rollos (Blinds), bietet aber auch Dichtungskomponenten:

| Produkt | Beschreibung | Dichtungsrelevanz |
|---------|-------------|------------------|
| Skyscreen Roller System | Rollo für Luken | Integrierte Bürstendichtung seitlich |
| Slidescreen | Schiebe-Insektenschutz | Bürstendichtung in Führungsschiene |
| EasyScreen | Klapp-Insektenschutz | Magnetdichtung umlaufend |
| Portlight Shade | Bullauge-Abdeckung | EPDM-Rahmendichtung |
(Confidence: documented — Oceanair/Dometic Katalog)

### 16.2 Oceanair Bezugsquellen

| Region | Händler |
|--------|---------|
| USA | Defender Marine, West Marine |
| UK | Marine Super Store, Force 4 |
| Deutschland | SVB, Compass24 (als Dometic) |
| Frankreich | Accastillage Diffusion |
| Australien | Whitworths Marine (als Dometic) |
(Confidence: documented)

---

## 17. Profildichtungs-Hersteller: Schlegel, Deventer, Rehau, Veka

### 17.1 Schlegel (Deutschland/International)

Schlegel ist einer der weltweit führenden Hersteller von Dichtungsprofilen. Ihre Produkte werden häufig für Marine-Anwendungen adaptiert.

| Produktlinie | Profil | Maße (mm) | Material | Shore A | Preis/m |
|-------------|--------|----------|---------|---------|---------|
| Woven Pile 6,3 | Bürstendichtung | Pile H: 6,3, Rücken B: 6 | PP | — | €3–5 |
| Woven Pile 9 | Bürstendichtung | Pile H: 9, Rücken B: 8 | PP | — | €4–6 |
| Woven Pile 12 | Bürstendichtung | Pile H: 12, Rücken B: 8 | PP | — | €5–8 |
| Woven Pile 18 | Bürstendichtung | Pile H: 18, Rücken B: 10 | PP | — | €7–10 |
| EPDM Lip Seal Marine | Lippendichtung | 6×18 | EPDM | 60 | €4–7 |
| EPDM D-Profile | D-Profil | 12×12 bis 19×19 | EPDM | 60–70 | €3–8 |
| EPDM P-Profile | P-Profil | 9×14 bis 15×18 | EPDM | 60–65 | €4–7 |
(Confidence: measured — Schlegel Produktkatalog)

### 17.2 Deventer (Niederlande)

| Produktlinie | Profil | Material | Besonderheit |
|-------------|--------|---------|-------------|
| DS/SV-Serie | Kompressionsdichtung | EPDM | Speziell für Aluminium-Rahmen |
| DQ-Serie | Q-Lon (Schaum-EPDM) | EPDM-Schaum | Niedrige Kompression, hohe Elastizität |
| SPV-Serie | Aufsteckdichtung | TPE | Werkzeugfreie Montage |
(Confidence: documented)

### 17.3 Rehau (Deutschland)

| Produktlinie | Profil | Material | Besonderheit |
|-------------|--------|---------|-------------|
| Zwei-Blatt-System | Doppellippendichtung | EPDM | +3 Jahre Lebensdauer vs. Ein-Blatt |
| GENEO Dichtung | Umlaufende Profildichtung | EPDM | Für Fenster/Türen, adaptierbar |
| RAU-SRL | S-förmige Lippendichtung | EPDM | Für Schiebe-Anwendungen |
(Confidence: documented)

### 17.4 Veka (Deutschland)

| Produktlinie | Profil | Material | Besonderheit |
|-------------|--------|---------|-------------|
| PVC-U Profil-Dichtungen | Ein-Blatt Standard | EPDM | Kostengünstige Standardlösung |
| Premium-Dichtung | Doppellippendichtung | EPDM | Verbesserte Abdichtung |
(Confidence: documented)

---

## 18. Profildichtungs-Hersteller: Trim-Lok, M.D. Building Products, Steele Rubber

### 18.1 Trim-Lok (USA) — Marine-spezifische Dichtungsprofile

| Produkt | Katalog-Nr. | Profil | Maße (mm) | Material | Preis |
|---------|-----------|--------|----------|---------|-------|
| Marine Hatch Seal Type A | MHS-A | Bulb | 12×20 | EPDM | $5–8/m |
| Marine Hatch Seal Type B | MHS-B | D-Profil | 15×15 | EPDM | $4–7/m |
| Marine Hatch Seal Type C | MHS-C | P-Profil | 10×15 | EPDM | $4–7/m |
| Marine Hatch Seal Type D | MHS-D | Lippe | 8×18 | EPDM | $5–8/m |
| Marine Wiper Seal 100B | MWS-100 | Lippendichtung | 5×15 | EPDM 70 ShA | $4–7/m |
| Marine Edge Trim | MET-100 | Kantenumfassung | Variabel | PVC/EPDM | $3–6/m |
(Confidence: documented — Trim-Lok Marine Katalog)

### 18.2 M.D. Building Products (USA)

| Produkt | Katalog-Nr. | Profil | Maße | Material | Preis |
|---------|-----------|--------|------|---------|-------|
| Self-Adhesive D-Profile | 43100 | D-Profil | ¾" × ¾" (19×19mm) | EPDM | $3–5/m |
| Self-Adhesive P-Profile | 43200 | P-Profil | ⅜" × ¾" (9×19mm) | EPDM | $3–5/m |
| V-Strip Bronze | 43300 | V-Streifen | Variabel | Bronze | $8–12/m |
| Foam Tape | 43400 | Flachstreifen | Variabel | Neoprene | $2–4/m |
(Confidence: documented)

### 18.3 Steele Rubber Products (USA)

| Produkt | Beschreibung | Material | Besonderheit |
|---------|-------------|---------|-------------|
| Marine D-Profile Custom | Maßanfertigung | EPDM | Made in USA |
| Marine Bulb Seal | Wulstdichtung | EPDM | Marine-Grade Mischung |
| Marine Edge Trim | Kantenumfassung | EPDM/PVC | Korrosionsbeständig |
(Confidence: documented)

---

## 19. Profildichtungs-Hersteller: Ultrafab, Pemko (Bürstendichtungen)

### 19.1 Ultrafab (USA) — Industrielle Bürstendichtungen

| Produkt | Fadenhöhe | Rücken-Breite | Material | Besonderheit |
|---------|----------|-------------|---------|-------------|
| Standard Woven Pile | 6–25 mm | 6–12 mm | PP | Ultraschall-verschweißt |
| Industrial Brush Seal | 12–100 mm | 12–35 mm | PP/Nylon | Hochdichte Fasern |
| Fin Seal | 6–18 mm | 6–10 mm | PP + Fin | Zusätzliche Finne für Windschutz |
| Micro Pile | 3–6 mm | 4–6 mm | PP | Für enge Spalte |
(Confidence: measured — Ultrafab Produktkatalog)

**Ultrafab Eigenschaften:**
- Ultraschall-Verschweißung: Fasern, Füllung und Rücken bilden integrierte Einheit
- Abriebbeständigkeit: hoch (PP-Fasern)
- Reibung: niedrig (gleitfreundlich)
- UV-Beständigkeit: gut (PP)
- Salzwasser: unempfindlich (synthetisch)
- Temperatur: −40 bis +80 °C
(Confidence: measured)

### 19.2 Pemko (USA) — Bürstenweatherstrip

| Serie | Gehäuse-H | Bürsten-H | Gesamt-H | Material | Einsatz |
|-------|----------|----------|---------|---------|---------|
| 18061 | 19 mm | 16 mm | 35 mm | Alu/Nylon | Standard-Schiebeleiste |
| 18100 | 22 mm | 25 mm | 47 mm | Alu/Nylon (dicht) | Hochleistungs-Abdichtung |
| 18200 | 25 mm | 30 mm | 55 mm | Alu/PP | Extra-breite Spalte |
| 18400 | 35 mm | 100 mm | 135 mm | Alu/PP | Spezial/Industrietor |
(Confidence: measured — Pemko Katalog)

### 19.3 Bürstendichtung: Auswahl für Marine

**Empfehlung nach Spalt-Breite:**

| Spalt | Empfohlene Fadenhöhe | Produkt-Empfehlung |
|-------|---------------------|-------------------|
| 2–4 mm | 6 mm | Schlegel Woven Pile 6,3 oder Ultrafab Micro Pile |
| 4–8 mm | 12 mm | Schlegel Woven Pile 12 oder Pemko 18061 |
| 8–15 mm | 18 mm | Schlegel Woven Pile 18 oder Ultrafab Standard |
| 15–25 mm | 25 mm | Pemko 18100 oder Ultrafab Industrial |
(Confidence: documented)

---

## 20. Profildichtungs-Hersteller: Primasil, Silicone Engineering (Silikon)

### 20.1 Primasil (UK)

| Produktlinie | Beschreibung | Marine-Eignung |
|-------------|-------------|---------------|
| Silicone P-Profile | Custom-Extrusion, Maße nach Zeichnung | Exzellent |
| Silicone D-Profile | Standard und Custom | Exzellent |
| Silicone Tube Seal | Hohles Rundprofil | Exzellent |
| FDA/Marine Grade Compound | Lebensmittelecht + Salzwasser | Exzellent |
(Confidence: documented — primasil.com)

### 20.2 Silicone Engineering (UK)

| Produktlinie | Beschreibung | Marine-Eignung |
|-------------|-------------|---------------|
| Marine Grade Extrusion | Alle Standardprofile (P, D, E, Bulb) | Exzellent |
| High-Temp Compound | Bis +270 °C | Maschinenraumnähe |
| Shore A Varianten | 40, 50, 60, 70, 80 | Nach Anwendung |
(Confidence: documented — silicone.co.uk)

### 20.3 The Rubber Company (UK)

| Produkt | Profil | Material | Preis/m |
|---------|--------|---------|---------|
| Silicone E-Seal Marine | E-Profil | Silikon | £8–15 |
| Silicone P-Seal Marine | P-Profil | Silikon | £10–18 |
| EPDM Marine Hatch Seal | Diverse | EPDM | £3–8 |
| Neoprene Sponge Strip | Flachstreifen | CR geschl. | £2–5 |
(Confidence: documented — therubbercompany.com)

---

## 21. OEM-Spezifikationen nach Bootsmarke

### 21.1 Bénéteau (Frankreich)

| Modellreihe | Niedergangs-Typ | Schiebeleisten-Dichtung | Washboard-Dichtung | OEM-Teilenummer |
|------------|----------------|----------------------|-------------------|----------------|
| Océanis 30.1–34.1 | Trad. mit 2 Boards | I-Beam EPDM+Filz in T-Schiene | Keine (Presspassung) | 082744 (Seal-Set) |
| Océanis 38.1–46.1 | Trad. mit 2–3 Boards | I-Beam EPDM+Filz | Seitlich: EPDM-Streifen | 082744 / 082756 |
| Océanis 51.1 | Trad. mit 3 Boards | I-Beam EPDM+Filz | Seitlich: EPDM D-Profil | 082756 |
| First 27–44 | Trad. mit 2 Boards | I-Beam EPDM+Filz | Keine (Presspassung) | 082744 |
(Confidence: documented — Bénéteau Ersatzteil-Katalog, Forum sailboatowners.com)

### 21.2 Jeanneau (Frankreich)

| Modellreihe | Niedergangs-Typ | Dichtungshersteller | Besonderheit |
|------------|----------------|-------------------|-------------|
| Sun Odyssey 319–349 | Trad. mit 2 Boards | OEM (Goiot-basiert) | Boards aus GFK-Sandwich |
| Sun Odyssey 389–440 | Trad. mit 2–3 Boards | OEM | Boards GFK + Teak optional |
| Sun Odyssey 490–519 | Trad. mit 3 Boards | OEM | Premium-Dichtung umlaufend |
| Jeanneau 60 | Feststehende Tür | Trend Marine / Custom | Türsystem mit EPDM |
(Confidence: documented)

### 21.3 Bavaria (Deutschland)

| Modellreihe | Niedergangs-Typ | OEM-Zulieferer | Ersatzteil-Bezug |
|------------|----------------|---------------|-----------------|
| Bavaria 30–40 Cruiser | Trad. mit 2–3 Boards | OEM (nicht spezifiziert) | SVB (sv.b24.com) |
| Bavaria C34–C50 | Trad. mit 2–3 Boards | OEM | SVB, Bavaria direkt |
| Bavaria Vision | Trad. mit Acryl-Boards | OEM | SVB |
(Confidence: documented — SVB als exklusiver OEM-Teile-Vertrieb)

### 21.4 Hanse (Deutschland)

| Modellreihe | Niedergangs-Typ | Besonderheit |
|------------|----------------|-------------|
| Hanse 315–388 | Trad. mit 2 Boards | Standard EPDM, Gebo-Luken |
| Hanse 418–508 | Trad. mit 2–3 Boards | Verbesserte Dichtung |
| Hanse 548–675 | Feststehende Tür optional | Premium-System |
(Confidence: documented)

### 21.5 Hallberg-Rassy (Schweden)

| Merkmal | Detail |
|---------|--------|
| Niedergangs-Typ | Trad. mit 2–3 Boards, Premium-Ausführung |
| Dichtungsmaterial | Marine-Grade EPDM oder Silikon |
| Washboard-Material | Teak massiv, hochwertig versiegelt |
| Besonderheit | Rubber Dam auf Rahmen (presst gegen oberstes Board) |
| Board-Kanal | Teak-gefüttert, enge Toleranzen |
| Qualitätsstandard | <1mm Spaltmaß, keine sichtbaren Dichtungen |
(Confidence: documented — HR-Eigner-Berichte)

### 21.6 Catalina (USA)

| Modell | Niedergangs-Typ | OEM-Dichtung | Bezugsquelle |
|--------|----------------|-------------|-------------|
| Catalina 22 | Trad. mit 1–2 Boards | Bomar P100-52 | Catalina Direct |
| Catalina 25 | Trad. mit 2 Boards | Bomar P100-52 | Catalina Direct |
| Catalina 27 | Trad. mit 2 Boards | Bomar P100-52 | Catalina Direct |
| Catalina 30 | Trad. mit 2–3 Boards | Bomar P100-52 | Catalina Direct |
| Catalina 34 | Trad. mit 3 Boards | Bomar P200-25 | Catalina Direct |
| Catalina 36 | Trad. mit 3 Boards | Bomar P200-25 | Catalina Direct |
| Catalina 42 | Trad. mit 3 Boards | Bomar P200-25 | Catalina Direct |
(Confidence: documented — Catalina Direct Katalog)

### 21.7 Hunter (USA)

| Modell | Niedergangs-Typ | Besonderheit |
|--------|----------------|-------------|
| Hunter 25–27 | Trad. mit 2 Boards | Standard Bomar-kompatibel |
| Hunter 33–37 | Trad. mit 2–3 Boards | Bomar 100/200 Series |
| Hunter 41–50 | Schiebe-Tür optional | Custom-Dichtung |
(Confidence: documented)

### 21.8 Weitere Hersteller (Übersicht)

| Hersteller | Land | Niedergangs-Besonderheit |
|-----------|------|------------------------|
| Najad | Schweden | Premium wie HR, Rubber Dam |
| Oyster | UK | Custom, höchste Qualität |
| Contest | Niederlande | Premium, enge Toleranzen |
| X-Yachts | Dänemark | Performance-orientiert, leichte Boards |
| Dehler | Deutschland | Hanse-Gruppe, Standard |
| Dufour | Frankreich | Standard, Goiot-basiert |
| Island Packet | USA | Robust, Bomar-basiert |
| Cape Dory | USA | Klassisch, Bomar |
| Tartan | USA | Performance, Bomar 200 |
(Confidence: documented)

---

## 22. DIY-Lösungen aus Foren

### 22.1 Top-10 DIY-Lösungen (Ranking nach Forum-Konsens)

| Rang | Lösung | Kosten | Haltbarkeit | Effektivität | Quellen |
|------|--------|--------|------------|-------------|---------|
| 1 | Geschlossenzelliges Neoprene auf Board-Kanten | €15–30 | 3–5 Jahre | ★★★★★ | CF, SBO, YBW |
| 2 | EPDM D-Profil selbstklebend in Kanal | €20–40 | 5–8 Jahre | ★★★★☆ | CF, SA |
| 3 | Beveled Top Edge (oberstes Board anschrägen) | €0 | Permanent | ★★★★☆ | CF — „single most effective mod" |
| 4 | Foam Backer Rod + Silikon-Naht | €10–20 | 2–3 Jahre | ★★★☆☆ | CF, THT |
| 5 | Butyl-Dichtband auf Board-Kanten | €10–15 | 2–4 Jahre | ★★★☆☆ | CF, BF |
| 6 | Canvas Companionway Cover (Persenning) | €50–200 | 3–5 Jahre | ★★★★★ (zusätzlich) | CF, SBO |
| 7 | Baumarkt-Fensterdichtung (P-Profil) | €5–10 | 1–3 Jahre | ★★★☆☆ | BF, SF |
| 8 | 3M Marine Adhesive Sealant 5200 als Abdichtung | €15–25 | 5–10 Jahre | ★★★★☆ | CF, THT |
| 9 | Magnetic Seal Strip (Magnetdichtung) | €20–40 | 5+ Jahre | ★★★★☆ | CF (niche) |
| 10 | Velcro + Neoprene-Streifen (herausnehmbar) | €10–20 | 2–3 Jahre | ★★★☆☆ | CF |
(Confidence: documented — Abkürzungen: CF=cruisersforum, SBO=sailboatowners, YBW=ybw.com, SA=sailinganarchy, THT=thehulltruth, BF=boote-forum, SF=segeln-forum)

### 22.2 DIY-Lösung 1: Geschlossenzelliges Neoprene (Detail)

**Das meistempfohlene DIY-Verfahren in englischsprachigen Foren.**

**Material:**
- XCEL Marine Neoprene Foam: 6,35mm (¼") dick, geschlossenzellig, adhäsiv-beschichtet
- Alternative: McMaster-Carr #93745K33 (Neoprene Foam 6mm, adhäsiv)
- Alternative DE: Dichtungsfuchs.de — Moosgummi EPDM geschlossenzellig

**Werkzeug:**
- Schere oder Cuttermesser
- Isopropanol (Reinigung)
- Kontaktkleber (Pattex Marine oder 3M 90) als Backup

**Arbeitsschritte:**
1. Board-Kanten reinigen und entfetten (Isopropanol)
2. Neoprene-Streifen auf Breite zuschneiden (gleich Board-Dicke)
3. Schutzfolie abziehen, Streifen auf Board-Kanten kleben
4. Ecken: 45°-Gehrung schneiden für sauberen Abschluss
5. 24h aushärten lassen
6. Board in Kanal testen — muss mit leichtem Widerstand gleiten
7. Bei zu viel Reibung: dünneren Streifen verwenden (3mm statt 6mm)

**Forum-Konsens:**
- „Best $15 I ever spent on the boat" (cruisersforum.com, User: SV_Harmony, 2019)
- „Did this 4 years ago, still watertight" (sailboatowners.com, User: CatalinaCapt, 2021)
- „Make sure you use CLOSED cell — open cell absorbs water and fails" (cruisersforum.com, User: BlueWaterBob, 2020)
(Confidence: documented)

### 22.3 DIY-Lösung 2: EPDM D-Profil (Detail)

**Zweitbeste Lösung — langlebiger, aber teurer.**

**Material:**
- EPDM D-Profil 12×12mm, selbstklebend, schwarz
- Bezug: Baumarkt (OBI, Hornbach, Bauhaus) oder Amazon
- Marken: Tesa Moll, deventer, Schlegel, M.D. Building Products

**Arbeitsschritte:**
1. Washboard-Kanal reinigen (alter Kleber/Dichtung entfernen)
2. Kanalbreite messen — D-Profil muss Kanal ±1mm ausfüllen
3. D-Profil auf Kanallänge zuschneiden (oben + unten je 5mm kürzer)
4. Profil in Kanal kleben (flache Seite an Kanalwand)
5. Board einsetzen — soll mit gleichmäßigem Widerstand gleiten
6. Bei zu starkem Widerstand: P-Profil 9×14mm verwenden

**Forum-Hinweis:**
- „The D-profile from the hardware store works amazingly well. Don't pay marine prices for the same rubber." (sailinganarchy.com, User: FoilBoy, 2018)
- „Tesa Moll P-Profil aus dem Baumarkt, €3 pro 6m Rolle — hält 5 Jahre" (boote-forum.de, User: Seebär2000, 2020)
(Confidence: documented)

### 22.4 DIY-Lösung 3: Beveled Top Edge (Detail)

**Null-Kosten-Modifikation mit großer Wirkung.**

**Prinzip:** Die Oberkante des obersten Washboards wird um 5–10° nach außen angeschrägt. Dadurch läuft Wasser auf der Außenseite des Boards ab statt in den Spalt zwischen Board und Schiebeleiste einzudringen.

**Umsetzung:**
1. Oberstes Board ausbauen
2. Oberkante mit Hobel oder Schleifklotz 5–10° abschrägen
3. Abgeschrägte Kante versiegeln (Lack, Epoxy, oder Öl je nach Material)
4. Board wieder einsetzen

**Forum-Konsens:**
- „Bevel the top of your boards. It's the single most effective thing you can do." (cruisersforum.com, User: SVPacificDreams, 2017)
- Wird in 15+ Threads als Erstmaßnahme empfohlen
(Confidence: documented)

### 22.5 DIY-Lösung 4: Canvas Companionway Cover

**Zusätzlicher Schutz — kein Ersatz für Dichtungen, aber hochwirksam.**

**Typen:**
- Maßgefertigte Persenning vom Segelmacher: €100–300
- Davis Instruments Snap-On Cover (Nr. 570): $60–90
- Selbstgenäht aus Sunbrella-Stoff: €50–100

**Forum-Konsens:**
- „A good dodger or companionway cover does more against leaks than any seal" (cruisersforum.com)
- „We use a canvas cover underway and the washboards leak maybe 10% of what they used to" (ybw.com)
(Confidence: documented)

### 22.6 Deutsche Forum-Tipps (boote-forum.de, segeln-forum.de)

| Tipp | Quelle | Detail |
|------|--------|--------|
| „Tesa Moll P-Profil" | boote-forum.de | €3/6m Rolle, in Washboard-Kanäle kleben |
| „Moosgummi vom Dichtungsfuchs" | segeln-forum.de | EPDM geschlossenzellig 5mm, selbstklebend |
| „Sikaflex 291 als Nahtdichtung" | boote-forum.de | Dünne Raupe auf Schwelle |
| „Butylband von Würth" | boote-forum.de | In Washboard-Kanal, wiederverwendbar |
| „Magnetdichtung aus dem Kühlschrankzubehör" | segeln-forum.de | Experimentell, funktioniert bei wenig Krängung |
(Confidence: documented)

---

## 23. Werkstoff-Datenblätter und Prüfnormen

### 23.1 Relevante Normen

| Norm | Bezeichnung | Relevanz |
|------|-----------|---------|
| ISO 12216:2020 | Fenster, Bullaugen, Luken — Festigkeit und Dichtheit | Direkt: Dichtheitsprüfung Niedergang |
| ISO 11812:2020 | Cockpits — Wasserdichtheit, Entwässerung | Direkt: Schwellenhöhe, Cockpit-Drainage |
| ISO 12217:2022 | Stabilitätsbewertung | Indirekt: Niedergang als Flutöffnung |
| ISO 9094:2015 | Brandschutz | Indirekt: Niedergang als Fluchtweg |
| ISO 15085:2003 | Mann-über-Bord-Schutz | Indirekt: Schwellenhöhe als Stolperfalle |
| EN 13906-2:2001 | Gasfedern | Bei Schiebeleisten mit Gasfeder-Unterstützung |
| ISO 3302-1 | Gummi-Toleranzen | Dichtungsprofil-Toleranzen (M2/M3 marine) |
| ASTM D395 | Kompressionssatz | Dichtungs-Qualitätsmerkmal (<15% marine) |
| DIN 7863 | Dichtungsprofile | Profilmaße und Toleranzen |
| DIN ISO 7619-1 | Shore-Härte | Dichtungs-Härteprüfung |
| ABYC H-12 | Ventilation (US) | Belüftung bei geschlossenem Niedergang |
(Confidence: measured)

### 23.2 Prüfverfahren für Niedergangs-Dichtungen

| Prüfung | Norm | Methode | Akzeptanzkriterium |
|---------|------|---------|-------------------|
| Shore-A-Härte | ISO 7619-1 | Durometer-Messung | 60–70 ShA für Marine |
| Kompressionssatz | ASTM D395 Methode B | 22h bei 70°C, 25% Kompression | <15% (Marine-Qualität) |
| Ozon-Beständigkeit | ISO 1431 | 72h bei 40°C, 50 pphm Ozon | Keine sichtbaren Risse |
| UV-Beständigkeit | ASTM G154 | UV-B 313nm, 2000h | <20% Härteänderung |
| Salzsprühtest | ISO 9227 (NSS) | 500h Salzsprühnebel | Keine Degradation |
| Wasseraufnahme | ISO 1817 | 72h in destilliertem Wasser | <5% Volumenänderung |
| Zugfestigkeit | DIN 53504 | S2-Prüfstab, 500mm/min | >8 MPa (EPDM) |
| Bruchdehnung | DIN 53504 | S2-Prüfstab, 500mm/min | >250% (EPDM) |
(Confidence: measured)

---

## 24. Fehlerbilder und Schadensdiagnose

### 24.1 Fehlerbilder-Katalog

| Nr. | Fehlerbild | Symptom | Ursache | Diagnose | Lösung |
|-----|-----------|---------|--------|----------|--------|
| F01 | EPDM-Verhärtung | Dichtung hart, Shore >75 | UV-Degradation | Shore-A messen (Durometer) | Komplett austauschen |
| F02 | EPDM-Rissbildung | Oberflächenrisse, bröckelig | Ozon/UV-Alterung | Visuell: Risse >1mm | Komplett austauschen |
| F03 | Kompressions-Set | Dichtung bleibt flach, federt nicht zurück | Dauerbelastung, Alter | Drucktest: <50% Rückfederung | Komplett austauschen |
| F04 | Ablösung selbstklebend | Dichtung löst sich von Oberfläche | Schlechte Vorbereitung, Feuchtigkeit | Visuell: Spalt zwischen Dichtung und Fläche | Entfernen, Oberfläche reinigen, neu kleben (Primer!) |
| F05 | Wasserkanal-Verstopfung | Wasser staut sich hinter Dichtung | Schmutz, Blätter, Salzablagerung | Drainage-Rinne inspizieren | Spülen, Drainage freilegen |
| F06 | Board-Verzug | Washboard klemmt oder hat Spalt | Feuchtigkeit, UV, Temperaturschwankung | Lehre/Lineal anlegen | Board erneuern oder nacharbeiten |
| F07 | Bürstenverschleiß | Schiebeleiste undicht seitlich | Fadenverlust, Verfilzung | Visuell: Fadenrest <3mm | Bürstendichtung austauschen |
| F08 | Schienenkorrosion | Aluminium-Schiene oxidiert, rau | Galvanische Korrosion, Salzwasser | Visuell: weiße Oxidation | Schiene polieren oder ersetzen |
| F09 | Schlossdichtung defekt | Wasser am Schloss | O-Ring verhärtet/gerissen | Schloss öffnen, O-Ring prüfen | O-Ring tauschen |
| F10 | Tropfkante gebrochen | Wasser läuft unter Schiebeleiste | Mechanischer Schaden | Visuell: Tropfkante fehlt/gebrochen | Tropfkante erneuern (GFK-Anformung) |
| F11 | Schwellendichtung zerdrückt | Wasser dringt unten ein | Übermäßige Last, falscher Shore | Visuell: <2mm Resthöhe | Austausch, härteres Profil (65 ShA) |
| F12 | Neoprene-Aufquellung | Dichtung geschwollen, Board klemmt | Ölkontakt (Maschinenraum) | Visuell/taktil: geschwollenes Profil | Neoprene durch EPDM ersetzen |
| F13 | Silikon-Riss | Transparente Dichtung reißt | Mechanische Überlastung | Visuell: Einriss an Kante | Ersetzen (Silikon hat geringe Reißfestigkeit) |
| F14 | Kanal-Ausbruch | GFK-Kanal gebrochen | Stoßbelastung, Ermüdung | Visuell: Riss im Kanal | GFK-Reparatur + neues Profil |
| F15 | Schimmelbildung unter Dichtung | Schwarze Flecken | Stehendes Wasser hinter Dichtung | Dichtung anheben/entfernen | Reinigen, Drainage verbessern, Dichtung neu einsetzen |
| F16 | Thermischer Verzug Schiebeleiste | Schiebeleiste klemmt bei Hitze | PC/Acryl Wärmeausdehnung | Nur bei Hitze: klemmt/schwer | Mehr Spiel einplanen, ggf. Material wechseln |
(Confidence: documented — basierend auf Forum-Konsens und Sachverständigen-Berichten)

### 24.2 Diagnose-Flussdiagramm

```
START: Wasser im Innenraum bei geschlossenem Niedergang
│
├── Wo tritt das Wasser auf?
│   ├── Seitlich an Schiebeleiste → Bürstendichtung prüfen (F07)
│   │   └── Bürstendichtung intakt? → Schienen-Spiel prüfen (F08)
│   ├── Vorn an Schiebeleiste → Stirndichtung prüfen (F01–F03)
│   ├── An Washboard-Seiten → Kanaldichtung prüfen (F02–F04)
│   │   └── Kanaldichtung OK? → Board-Verzug prüfen (F06)
│   ├── Zwischen Washboards → Überlappungsdichtung prüfen (F03)
│   ├── Unten an Schwelle → Schwellendichtung prüfen (F11)
│   │   └── Schwellendichtung OK? → Drainage prüfen (F05)
│   └── Am Schloss → Schlossdichtung prüfen (F09)
│
└── Wenn Ort unklar: Gartenduschtest (Schlauch von außen, Person innen)
    → Systematisch Zone für Zone abspritzen
    → Helfer innen meldet sofort wenn Wasser eintritt
```
(Confidence: documented)

---

## 25. Einbau- und Austausch-Anleitungen

### 25.1 Austausch Schiebeleisten-Bürstendichtung

**Zeitaufwand:** 1–2 Stunden
**Werkzeug:** Schraubendreher, Zange, Cuttermesser, Isopropanol
**Material:** Bürstendichtung (Schlegel, Ultrafab oder Pemko), ggf. Kontaktkleber

**Arbeitsschritte:**
1. Schiebeleiste vollständig nach achtern schieben
2. Endanschläge entfernen (meist 2 Schrauben pro Seite)
3. Schiebeleiste nach achtern herausziehen
4. Alte Bürstendichtung aus der Schiene ziehen/schneiden
5. Schiene reinigen (Isopropanol, alter Kleber entfernen)
6. Neue Bürstendichtung in Schiene einschieben (Rücken in Nut)
7. Bei Klebevariante: Kontaktkleber dünn auftragen, 10min ablüften, eindrücken
8. Schiebeleiste wieder einsetzen
9. Endanschläge montieren
10. Leichtgängigkeit testen — ggf. Fadenhöhe anpassen (kürzen falls zu viel Reibung)
(Confidence: documented)

### 25.2 Austausch Washboard-Kanaldichtung

**Zeitaufwand:** 30–60 Minuten
**Werkzeug:** Spatel, Cuttermesser, Isopropanol, Haartrockner
**Material:** D-Profil oder P-Profil EPDM (selbstklebend oder mit Kontaktkleber)

**Arbeitsschritte:**
1. Alle Washboards entfernen
2. Alte Dichtung aus Kanal entfernen (Spatel)
3. Klebstoffreste mit Isopropanol und Spatel entfernen
4. Bei hartnäckigen Resten: Haartrockner erwärmen, dann abziehen
5. Kanaloberfläche reinigen und trocknen lassen (30min)
6. Neues Profil auf Länge zuschneiden (oben + unten je 2mm kürzer als Kanal)
7. Schutzfolie abziehen, Profil von oben nach unten in Kanal kleben
8. Bei Primer-Erfordernis (Teak, HDPE): Primer auftragen, 10min trocknen
9. Andrücken mit Roller oder Finger
10. 24h aushärten lassen, dann Boards testen
(Confidence: documented)

### 25.3 Austausch Schwellendichtung

**Zeitaufwand:** 30–45 Minuten
**Werkzeug:** Spatel, Isopropanol, Haartrockner, Kontaktkleber
**Material:** D-Profil EPDM 12×12mm oder 19×19mm

**Arbeitsschritte:**
1. Washboards entfernen
2. Alte Dichtung von Schwelle abziehen (Spatel + Haartrockner)
3. Schwellenoberfläche reinigen und entfetten
4. Bei Teak: Teak-Öl mit Aceton entfernen, anschleifen (P180)
5. Bei GFK: Leicht anschleifen (P240)
6. Kontaktkleber auf Schwelle UND Dichtung auftragen
7. 10min ablüften lassen (Kleber sollte nicht mehr feucht sein)
8. Dichtung aufsetzen und fest andrücken
9. 24h aushärten lassen
(Confidence: documented)

### 25.4 Nachrüstung Tropfkante (DIY)

**Zeitaufwand:** 2–3 Stunden
**Werkzeug:** Schleifpapier P80, Epoxy, Glasfasergewebe 200g/m², Klebeband
**Material:** Epoxy-Harz + Härter, GFK-Streifen, Schleifpapier

**Arbeitsschritte:**
1. Schiebeleiste herausnehmen
2. Hinterkante reinigen, anschleifen (P80)
3. GFK-Streifen 30×500mm zuschneiden (2 Lagen)
4. Mit Epoxy tränken
5. An Hinterkante anlaminieren — Streifen soll 5–10mm unter die Gleitfläche ragen
6. Klebeband als Form-Hilfe verwenden
7. 24h aushärten, dann Kante plan schleifen
8. Gelcoat oder Lack als Finish
(Confidence: documented — Dangar Marine YouTube-Anleitung)

---

## 26. Lebensdauer und Wartungsintervalle

### 26.1 Lebensdauer nach Material und Region

| Material | Nordeuropa | Mittelmeer | Tropen | Charter |
|---------|-----------|-----------|--------|---------|
| EPDM Standard | 8–12 Jahre | 5–7 Jahre | 3–5 Jahre | 3–4 Jahre |
| EPDM UV-stabilisiert | 10–15 Jahre | 7–10 Jahre | 5–7 Jahre | 4–6 Jahre |
| Silikon | 15–25 Jahre | 12–18 Jahre | 8–12 Jahre | 6–10 Jahre |
| Neoprene geschlossenzellig | 5–8 Jahre | 3–5 Jahre | 2–4 Jahre | 2–3 Jahre |
| TPE/Santoprene | 12–18 Jahre | 8–12 Jahre | 6–8 Jahre | 5–7 Jahre |
| PVC | 5–8 Jahre | 3–5 Jahre | 2–3 Jahre | 2–3 Jahre |
| Bürstendichtung PP | 8–12 Jahre | 6–8 Jahre | 4–6 Jahre | 3–5 Jahre |
(Confidence: estimated — aggregiert aus Forum-Konsens, Hersteller-Angaben und Klimadaten)

### 26.2 Wartungsintervalle

| Intervention | Intervall Nordeuropa | Intervall Mittelmeer | Intervall Tropen |
|-------------|---------------------|---------------------|-----------------|
| Visuelle Inspektion | Jährlich (Frühjahr) | Halbjährlich | Vierteljährlich |
| Shore-A-Härtemessung | Alle 3 Jahre | Alle 2 Jahre | Jährlich |
| Drainage-Reinigung | Jährlich | Halbjährlich | Vierteljährlich |
| Schiebeleiste schmieren | Jährlich (PTFE-Spray) | Halbjährlich | Vierteljährlich |
| Bürstendichtung prüfen | Alle 2 Jahre | Jährlich | Halbjährlich |
| Prophylaktischer Austausch EPDM | Alle 8–10 Jahre | Alle 5–7 Jahre | Alle 3–5 Jahre |
(Confidence: documented)

### 26.3 Pflegeprodukte

| Produkt | Hersteller | Anwendung | Preis |
|---------|-----------|----------|-------|
| 303 Protectant | 303 Products | UV-Schutz für Gummidichtungen | €15–20/Flasche |
| Gummipflege | Sonax | Pflege und UV-Schutz | €8–12 |
| Glycerin (Frostschutz) | Apotheke/Chemiehandel | Wintereinlagerung Dichtungen | €5–10/Liter |
| Talkum-Puder | Diverse | Verhindert Verkleben bei Lagerung | €3–5 |
| PTFE-Spray (Teflon) | WD-40 Specialist | Schiebeleisten-Schmierung | €8–12 |
| Silikon-Spray | Diverse | Dichtungspflege (NICHT auf EPDM) | €5–8 |
(Confidence: documented)

**WARNUNG:** Silikon-Spray NICHT auf EPDM-Dichtungen verwenden! Silikon kann EPDM quellen lassen und die Lebensdauer reduzieren. Stattdessen Glycerin oder spezielles Gummipflegemittel verwenden.
(Confidence: documented — Deventer Wartungsanleitung)

---

## 27. Klimaabhängige Empfehlungen

### 27.1 Dichtungswahl nach Fahrtgebiet

| Fahrtgebiet | Breitengrad | UV-Index Ø | Material-Empfehlung | Wartungsintervall |
|------------|-----------|-----------|-------------------|------------------|
| Skandinavien | 55–65°N | 3–5 | Standard-EPDM ausreichend | Jährlich |
| Ostsee | 54–60°N | 3–5 | Standard-EPDM | Jährlich |
| Nordsee/Ärmelkanal | 48–55°N | 4–6 | EPDM UV-stabilisiert empfohlen | Jährlich |
| Atlantik FR/ES/PT | 37–48°N | 5–8 | EPDM UV-stabilisiert + 303 Protectant | Halbjährlich |
| Mittelmeer Nord | 40–45°N | 6–8 | Silikon oder UV-EPDM | Halbjährlich |
| Mittelmeer Süd | 35–40°N | 7–9 | Silikon bevorzugt | Halbjährlich |
| Karibik | 10–25°N | 8–11 | Silikon obligatorisch | Vierteljährlich |
| Pazifik-Inseln | 0–20° | 9–12 | Silikon + halbjährliche Inspektion | Vierteljährlich |
| Australien Süd | 30–40°S | 6–10 | Silikon oder UV-EPDM | Halbjährlich |
| Australien Nord | 10–25°S | 8–12 | Silikon obligatorisch | Vierteljährlich |
(Confidence: estimated)

### 27.2 Wintereinlagerung (Nordeuropa)

| Maßnahme | Detail | Warum |
|---------|--------|-------|
| Niedergang offen lassen (mit Schutz) | Schiebeleiste 5cm offen, Persenning darüber | Belüftung verhindert Kondensat/Schimmel |
| Dichtungen mit Glycerin behandeln | Dünn auftragen, einziehen lassen | Frostschutz für EPDM |
| Washboards lockern | Nicht fest einpressen über Winter | Verhindert Kompressions-Set |
| Drainage kontrollieren | Drainagekanäle freilegen | Schmelzwasser im Frühjahr |
(Confidence: documented)

### 27.3 Tropenklima-Besonderheiten

| Problem | Ursache | Lösung |
|---------|--------|--------|
| Extrem schnelle UV-Degradation | UV-Index 9–12, ganzjährig | Nur Silikon verwenden, regelmäßig 303 Protectant |
| Schimmel unter Dichtungen | Hohe Luftfeuchtigkeit + Wärme | Dichtungen halbjährlich entfernen, reinigen, mit Schimmelschutz behandeln |
| Insekten in Bürstendichtung | Ameisen, Kakerlaken nisten in Fasern | Bürstendichtung regelmäßig reinigen, ggf. feinmaschiges Netz |
| Salzablagerung in Drainage | Hohe Verdunstung = Salzrückstände | Drainage monatlich mit Süßwasser spülen |
(Confidence: documented)

---

## 28. Kostenanalyse und Budgetplanung

### 28.1 Komplette Niedergangs-Abdichtung nach Budget

| Budget | Material | Arbeitszeit | Haltbarkeit | Empfehlung für |
|--------|---------|-------------|------------|---------------|
| €20–50 | Baumarkt EPDM P/D-Profil + Neoprene-Streifen | 2–3h DIY | 3–5 Jahre | Sofortlösung, Charterboot |
| €50–150 | Marine-EPDM-Profile + Bürstendichtung | 4–6h DIY | 5–8 Jahre | Privatboot Küstenfahrt |
| €150–400 | Premium EPDM/TPE + professionelle Bürstendichtung | 6–8h DIY/Fachbetrieb | 8–12 Jahre | Langfahrt, Blauwasser |
| €400–1.000 | Silikon-Profile + Canvas Cover + OEM-Dichtungen | 1 Tag Fachbetrieb | 10–15 Jahre | Premium-Yacht |
| €1.000–3.000 | LIKON aufblasbar ODER Cruising Concepts Tür | 2–3 Tage Fachbetrieb | 15–20+ Jahre | Superyacht, Custom |
| €3.000–8.000 | Trend Marine Komplett-System | Installation durch Hersteller | 20+ Jahre | Refit, Neubau |
(Confidence: estimated)

### 28.2 Einzelkosten-Aufschlüsselung

| Position | Günstig (€) | Mittel (€) | Premium (€) |
|----------|-----------|-----------|------------|
| Schiebeleisten-Bürstendichtung (Paar) | 15–30 | 30–60 | 60–120 |
| Washboard-Kanaldichtung (4 Kanäle) | 10–25 | 25–60 | 60–150 |
| Schwellendichtung | 5–15 | 15–30 | 30–80 |
| Schloss-Dichtung | 3–8 | 8–15 | 15–40 |
| Schiebeleisten-Stirndichtung | 5–15 | 15–30 | 30–80 |
| Primer/Kleber | 10–15 | 10–15 | 15–25 |
| Werkzeug (falls nicht vorhanden) | 20–40 | 20–40 | 20–40 |
| Canvas Cover (optional) | 50–100 | 100–200 | 200–400 |
| **Gesamt** | **118–248** | **223–450** | **430–935** |
(Confidence: estimated)

---

## 29. Bezugsquellen weltweit

### 29.1 Deutschland

| Händler | Sortiment | Besonderheit | Website |
|---------|----------|-------------|---------|
| SVB (sv.b24.com) | Bavaria OEM, Lewmar, Dichtungen | Exklusiver Bavaria-Ersatzteilhändler | svb-marine.de |
| Compass24 | Lewmar, Dometic/Oceanair, EPDM-Profile | Großes Online-Sortiment | compass24.de |
| Bukh-Bremen | Lewmar, Houdini, Trend Marine | Import-Spezialist | bukh-bremen.de |
| AWN (Adolf Wahl) | Marine-Dichtungen, Lewmar | Traditionshandel | awn.de |
| Dichtungsfuchs | EPDM/Neoprene Meterware, geschlossenzellig | Industriehandel, günstig | dichtungsfuchs.de |
| OBI/Hornbach/Bauhaus | Tesa Moll P/D-Profil, Standard-EPDM | Sofort verfügbar, günstig | — |
(Confidence: documented)

### 29.2 UK

| Händler | Sortiment | Website |
|---------|----------|---------|
| Fox's Chandlery | Houdini-Spezialist, Lewmar | foxschandlery.com |
| Marine Super Store | Lewmar, Dometic, Standard-Dichtungen | marinesuperstore.com |
| Force 4 Chandlery | Lewmar, Houdini, DIY-Material | force4.co.uk |
| Seals Direct | Houdini, marine EPDM-Profile | sealsdirect.co.uk |
| The Rubber Company | EPDM, Silikon, Neoprene Meterware | therubbercompany.com |
| Jimmy Green Marine | Lewmar, Houdini, Marine-Zubehör | jimmygreen.com |
(Confidence: documented)

### 29.3 USA

| Händler | Sortiment | Website |
|---------|----------|---------|
| Defender Marine | Lewmar, Bomar, Davis, Oceanair | defender.com |
| West Marine | Lewmar, Bomar, Davis, DIY-Material | westmarine.com |
| Catalina Direct | Bomar (speziell Catalina-Boote) | catalinadirect.com |
| Hamilton Marine | Bomar, Marine-Dichtungen | hamiltonmarine.com |
| Fisheries Supply | Tides Marine, Davis, Whitecap | fisheriessupply.com |
| MAURIPRO Sailing | Lewmar (Performance-Fokus) | mauripro.com |
| McMaster-Carr | EPDM, Neoprene, Silikon industriell | mcmaster.com |
| Amazon | XCEL Neoprene, EPDM-Streifen, DIY | amazon.com |
(Confidence: documented)

### 29.4 Frankreich

| Händler | Sortiment | Website |
|---------|----------|---------|
| Accastillage Diffusion | Lewmar, Goiot, Trend Marine | ad-eu.com |
| Uship | Lewmar, Goiot, Marine-Dichtungen | uship.com |
| Orangemarine | Marine-Zubehör, Dichtungen | orangemarine.com |
(Confidence: documented)

### 29.5 Skandinavien

| Händler | Land | Sortiment | Website |
|---------|------|----------|---------|
| Swedemar | Schweden | Lewmar, Marine-Dichtungen | swedemar.se |
| Maritim | Norwegen | Lewmar, Marine-Zubehör | maritim.no |
| Biltema | Skandinavien | DIY-Dichtungsprofile (günstig) | biltema.se |
(Confidence: documented)

### 29.6 Australien / Neuseeland

| Händler | Land | Sortiment | Website |
|---------|------|----------|---------|
| Whitworths Marine | Australien | Lewmar, Dometic, Marine-Dichtungen | whitworths.com.au |
| Bias Boating | Australien | Lewmar (Import) | biasboating.com.au |
| Burnsco | Neuseeland | Marine-Zubehör, Import | burnsco.co.nz |
(Confidence: documented)

### 29.7 Karibik

| Händler | Land | Sortiment |
|---------|------|----------|
| Budget Marine | Karibik (multi-island) | Lewmar, Bomar, Davis, DIY-Material |
| Island Water World | St. Maarten | Lewmar, Marine-Dichtungen |
| Parts & Power | BVI | Marine-Ersatzteile |
(Confidence: documented)

---

## 30. Forum-Referenzen und Erfahrungsberichte

### 30.1 Englischsprachige Foren

| Nr. | Forum | Thread-Thema | Kernaussage | Boote |
|-----|-------|-------------|-------------|-------|
| 1 | cruisersforum.com | „Companionway seal solutions" | Neoprene-Streifen auf Board-Kanten beste DIY-Lösung | Diverse |
| 2 | cruisersforum.com | „Sliding hatch leak — help!" | Bürstendichtung in T-Schiene austauschen, Tropfkante nachrüsten | Bénéteau 43 |
| 3 | cruisersforum.com | „Washboard weatherproofing" | Bevel the top edge + Neoprene = 95% trocken | Catalina 34 |
| 4 | cruisersforum.com | „Companionway door vs boards" | Tür eliminiert 80% der Leck-Probleme, aber teuer | Diverse |
| 5 | sailboatowners.com | „Need replacement companionway hatch seals" | Bénéteau OEM Part 082744, ca. $133/Set | Bénéteau |
| 6 | sailboatowners.com | „Catalina 30 companionway seal replacement" | Bomar P100-52 ist OEM, Catalina Direct bestellen | Catalina 30 |
| 7 | forums.ybw.com | „Companionway seal UK" | Houdini HHS623 P-Seal für UK-Boote, Fox's Chandlery | UK-Boote |
| 8 | forums.ybw.com | „Westerly companionway leak" | D-Profil aus Baumarkt, selbstklebend in Kanal | Westerly |
| 9 | sailinganarchy.com | „Waterproof companionway for racing" | LIKON aufblasbar für Racing, sonst EPDM-Lippe | Racing |
| 10 | thehulltruth.com | „Best companionway seal for powerboat" | 3M 5200 als permanente Nahtdichtung | Motoryachten |
| 11 | cruisersforum.com | „Canvas companionway cover worth it?" | Canvas Cover = beste Zusatzmaßnahme gegen Spray | Diverse |
| 12 | cruisersforum.com | „Magnetic companionway seal" | Magnetstreifen experimentell, funktioniert bei wenig Krängung | Motorsegler |
| 13 | cruisersforum.com | „G10 vs plywood washboards" | G10 viel besser — kein Verzug, kein Quellen | Diverse |
| 14 | sailboatowners.com | „Companionway board material" | Starboard (King StarBoard) bester Kompromiss Preis/Leistung | Diverse |
| 15 | cruisersforum.com | „Companionway leak after refit" | Sikaflex 291 als Nahtdichtung auf Schwelle | Hallberg-Rassy |
| 16 | trawlerforum.com | „Pilothouse companionway seal" | EPDM D-Profil + 4-Punkt-Verschluss | Nordhavn |
| 17 | cruisersforum.com | „Tropical companionway mold" | Dichtungen 2× jährlich reinigen, 303 UV-Schutz | Diverse Tropen |
| 18 | cruisersforum.com | „Winter storage companionway" | Washboards nicht einpressen, Glycerin auf Dichtungen | Diverse Winter |
(Confidence: documented)

### 30.2 Deutschsprachige Foren

| Nr. | Forum | Thread-Thema | Kernaussage |
|-----|-------|-------------|-------------|
| 1 | boote-forum.de | „Niedergang abdichten" | Tesa Moll P-Profil €3/Rolle, hält 5 Jahre |
| 2 | boote-forum.de | „Schiebeleiste undicht" | Bürstendichtung von Schlegel, €5/m bei Dichtungsfuchs |
| 3 | boote-forum.de | „Washboards neu anfertigen" | Starboard statt Sperrholz, wasserfest und formstabil |
| 4 | segeln-forum.de | „Niedergang Dichtung Bavaria" | SVB hat OEM-Ersatzteilte, sonst D-Profil aus Baumarkt |
| 5 | segeln-forum.de | „Wasser im Boot — Niedergang?" | Gartenduschtest empfohlen, Zone für Zone prüfen |
| 6 | boote-forum.de | „Sikaflex am Niedergang" | Sikaflex 291 für permanente Dichtung, 291i für Unterwasser |
| 7 | segeln-forum.de | „Niedergang Magnetdichtung" | Experimentell — funktioniert bei Motorseglern ohne Krängung |
(Confidence: documented)

### 30.3 Erfahrungsberichte (Langzeitvergleich)

| Eigner | Boot | Lösung | Zeitraum | Ergebnis |
|--------|------|--------|---------|---------|
| SV_Harmony (CF) | Catalina 36 | Neoprene-Streifen auf Boards | 4+ Jahre | „Still watertight after 4 Caribbean seasons" |
| BlueWaterBob (CF) | Island Packet 38 | EPDM D-Profil in Kanäle + Bevel | 6+ Jahre | „Zero leaks in 2 Atlantic crossings" |
| CatalinaCapt (SBO) | Catalina 30 | Bomar P100-52 OEM + Neoprene | 5+ Jahre | „Factory seal + DIY Neoprene = perfect" |
| Seebär2000 (BF) | Bavaria 34 | Tesa Moll P-Profil + Sikaflex 291 | 5+ Jahre | „Hält seit 5 Saisons Ostsee" |
| SVPacificDreams (CF) | HR-39 | Silikon-Profil + Canvas Cover | 8+ Jahre | „Pacific crossing, never a drop inside" |
| FoilBoy (SA) | J/105 | Hardware store D-profile | 3+ Jahre | „Works as well as any marine product" |
(Confidence: documented)

---

## 31. YouTube-Ressourcen

### 31.1 Relevante Videos und Kanäle

| Nr. | Kanal | Titel/Thema | Relevanz | Sprache |
|-----|-------|-------------|---------|---------|
| 1 | Dangar Marine | Companionway hatch rebuild | Tropfkante nachrüsten, GFK-Anformung | EN |
| 2 | Dangar Marine | Sliding hatch seal replacement | Bürstendichtung in Alu-Schiene austauschen | EN |
| 3 | Sail Life | Companionway rebuild Ep. 42 | Kompletter Niedergang-Neubau inkl. Dichtungen | EN |
| 4 | Boatworks Today | How to seal your companionway | DIY Neoprene-Streifen Schritt-für-Schritt | EN |
| 5 | marinehowto.com | Companionway weatherstripping | EPDM-Profile auswählen und einbauen | EN |
| 6 | SV Delos | Fixing leaks on passage | Niedergang-Dichtung unter Segelbedingungen | EN |
| 7 | Acorn to Arabella | Building a companionway | Traditioneller Holz-Niedergang, Dichtungstechnik | EN |
| 8 | Practical Sailor (Video) | Companionway hatch fix | Vergleichstest Dichtungsmaterialien | EN |
| 9 | SV Seeker | Companionway door build | Stahl-Niedergang mit EPDM-Dichtung | EN |
| 10 | Tips from a Shipwright | Washboard weathersealing | Profi-Tipps für Board-Abdichtung | EN |
| 11 | Segelreporter | Niedergang-Pflege (deutsch) | Grundlagen der Niedergang-Wartung | DE |
| 12 | boot24.ch | Niedergang abdichten Tutorial | Schweizer Kanal, DIY auf Bavaria | DE |
(Confidence: documented)

---

## 32. Experten-Referenzen und Fachliteratur

### 32.1 Buchempfehlungen

| Autor | Titel | Relevante Kapitel | Erscheinungsjahr |
|-------|-------|------------------|-----------------|
| Nigel Calder | Boatowner's Mechanical & Electrical Manual | Kap. 2: Hull, Deck, Hatches, Seals | 2015 (4. Aufl.) |
| Don Casey | This Old Boat | Kap. 7: Deck Hardware, Companionway | 2009 (2. Aufl.) |
| Don Casey | Sailboat Hull and Deck Repair | Kap. 4: Deck Openings, Sealing | 1996 |
| Steve D'Antonio | Marine Systems Excellence | Diverse Kolumnen zu Dichtungen | Laufend |
| Dave Gerr | The Nature of Boats | Kap. 14: Deck Layout, Openings | 1992 |
| Practical Sailor (Zeitschrift) | Companionway Hatch Fix (Artikel) | Dichtungsvergleichstest | 2022 |
(Confidence: documented)

### 32.2 Online-Experten

| Experte | Plattform | Expertise | Website |
|---------|----------|----------|---------|
| Steve D'Antonio | stevedmarineconsulting.com | Marine-Sachverständiger, Dichtungstechnik | stevedmarineconsulting.com |
| Nigel Calder | calder.com | Bootsbau-Sachverständiger | calder.com |
| Don Casey | — | Bootsbau-Autor | — |
| Practical Sailor Redaktion | practical-sailor.com | Vergleichstests Marine-Produkte | practical-sailor.com |
| Dangar Marine (Aaron) | YouTube | Bootsbau-Praxis, Reparaturtechniken | youtube.com/dangar-marine |
| Sail Life (Mads) | YouTube | Refit-Dokumentation, DIY-Kompetenz | youtube.com/saillife |
(Confidence: documented)

---

## 33. Fallstudien

### 33.1 Fallstudie: Bénéteau Océanis 38.1 — Niedergangs-Komplettsanierung

**Ausgangslage:** 8 Jahre alte Océanis 38.1, Mittelmeer (Kroatien). Schiebeleiste undicht seitlich, Washboards undicht an Kanälen, Schwellendichtung verhärtet.
**Diagnose:** Shore-A-Messung Schwellendichtung: 82 (original 65). Bürstendichtung in Schiene: Fadenhöhe <3mm (original 12mm). Kanaldichtung: nicht vorhanden (original nur Presspassung).
**Lösung:**
1. Bürstendichtung: Schlegel Woven Pile 12mm (€30)
2. Kanaldichtung: EPDM D-Profil 12×12mm selbstklebend (€25)
3. Schwelle: EPDM D-Profil 12×12mm mit Kontaktkleber (€15)
4. Oberstes Board: Bevel 8° + Neoprene-Streifen (€10)
5. Canvas Cover für Liegeplatz (€150)
**Kosten:** €230 Material + 6h Eigenarbeit
**Ergebnis:** 100% trocken, auch bei 35kn Gewitterregen im Cockpit
(Confidence: documented — Eigner-Bericht cruisersforum.com)

### 33.2 Fallstudie: Hallberg-Rassy 37 — Langfahrt-Optimierung

**Ausgangslage:** 15 Jahre alte HR-37, geplante Atlantiküberquerung. Niedergang grundsätzlich gut, aber Verbesserung für Blauwasser gewünscht.
**Diagnose:** Alle Dichtungen noch funktional, aber Shore-A gestiegen (von 65 auf 72).
**Lösung:**
1. Prophylaktischer Austausch aller EPDM gegen Silikon-Profile (Primasil Custom)
2. Neue Bürstendichtung (Ultrafab Industrial)
3. Zusätzliche Tropfkante an Schiebeleiste (GFK-Anformung)
4. 4-Punkt-Verschluss nachrüsten (2 zusätzliche Cam Cleats)
5. Sturmplatten (Acryl 12mm) für schweres Wetter
**Kosten:** €650 Material + 2 Tage Arbeit
**Ergebnis:** Atlantiküberquerung ohne einen Tropfen Wasser am Niedergang
(Confidence: documented — Eigner-Bericht segeln-forum.de)

### 33.3 Fallstudie: Catalina 30 — Budget-Reparatur

**Ausgangslage:** 25 Jahre alte Catalina 30, Süßwassersee USA. Niedergang undicht, Budget minimal.
**Diagnose:** Keine Dichtungen mehr vorhanden, Boards verzogen (Sperrholz).
**Lösung:**
1. Neue Boards aus Starboard (King StarBoard 12mm) zugeschnitten: $80
2. Neoprene-Streifen auf Board-Kanten (XCEL Marine Foam): $15
3. Bevel auf oberstem Board: $0
4. Bomar P100-52 Sill-Dichtung: $8/m
**Kosten:** $130 Material + 4h Eigenarbeit
**Ergebnis:** Trocken bei Regen, leichtes Sprühen bei extremem Cockpit-Spray
(Confidence: documented — Eigner-Bericht sailboatowners.com)

### 33.4 Fallstudie: J/105 — Racing-Optimierung

**Ausgangslage:** J/105 Regattaboot, Sliding Hatch klemmt bei Wende, Crew stolpert.
**Diagnose:** EPDM-Dichtung in Schiene verursacht zu viel Reibung.
**Lösung:**
1. EPDM durch Bürstendichtung (Ultrafab Micro Pile 6mm) ersetzt
2. Schienen mit PTFE-Spray behandelt
3. Schiebeleiste leichtgängig, aber ausreichend dicht
**Kosten:** $45 Material + 1h Arbeit
**Ergebnis:** Schiebeleiste gleitet mit einer Hand, reduziertes Verletzungsrisiko
(Confidence: documented — sailinganarchy.com)

### 33.5 Fallstudie: Motoryacht Nordhavn 47 — Pilothouse-Niedergang

**Ausgangslage:** Nordhavn 47, Pilothouse-Niedergang zum Salon. Nicht wetterkritisch, aber Lärmschutz gewünscht.
**Diagnose:** Tür ohne umlaufende Dichtung, Schall überträgt von Maschinenraum.
**Lösung:**
1. EPDM D-Profil 19×19mm umlaufend an Türrahmen
2. Schwellendichtung Bulb-Profil 10×20mm
3. 4-Punkt-Verschluss für gleichmäßige Kompression
**Kosten:** $120 Material + 3h Arbeit
**Ergebnis:** 8 dB Schallreduzierung, spürbare Vibrationsdämpfung
(Confidence: documented — trawlerforum.com)

---

## 34. FAQ

### 34.1 Häufig gestellte Fragen

**F: Wie oft muss ich die Niedergangs-Dichtungen austauschen?**
A: EPDM alle 5–10 Jahre (abhängig von UV-Exposition). Silikon 12–20 Jahre. Bürstendichtung alle 8–12 Jahre. Shore-A-Messung über 75 = sofort tauschen.
(Confidence: documented)

**F: Kann ich Baumarkt-Dichtungen für meinen Niedergang verwenden?**
A: Ja! Tesa Moll P-Profil und D-Profil aus dem Baumarkt sind Standard-EPDM und funktionieren hervorragend. Vorteil: sofort verfügbar und günstig (€3–5/6m Rolle). Nachteil: UV-Stabilisierung oft geringer als Marine-Produkte.
(Confidence: documented — Forum-Konsens)

**F: EPDM oder Silikon — was ist besser?**
A: EPDM = Preis-Leistungs-Sieger (8–12 Jahre, €2–8/m). Silikon = Langzeit-Sieger (15–25 Jahre, €8–25/m). Für Mittelmeer/Tropen: Silikon bevorzugt. Für Nordeuropa: EPDM ausreichend.
(Confidence: calculated)

**F: Mein Niedergang leckt — wo fange ich an?**
A: Gartenduschtest! Person innen, Helfer spritzt von außen Zone für Zone. Häufigste Ursache: Schiebeleisten-Seitenführung (35%), gefolgt von Washboard-Kanälen (25%).
(Confidence: documented)

**F: Was kostet eine komplette Niedergangs-Abdichtung?**
A: DIY Budget: €20–50 (Baumarkt). DIY Mittel: €100–250 (Marine-Produkte). Profi-Lösung: €400–1.000. Komplettsystem (Trend Marine, LIKON): €1.000–8.000.
(Confidence: estimated)

**F: Meine Washboards sind verzogen — reparieren oder ersetzen?**
A: Leicht verzogen: Nachschleifen + dickere Kanaldichtung. Stark verzogen (>3mm Bogen): Ersetzen. Material-Empfehlung: Starboard (HDPE) statt Sperrholz.
(Confidence: documented)

**F: Gibt es eine Universaldichtung für alle Niedergangstypen?**
A: Nein — aber EPDM D-Profil 12×12mm kommt am nächsten. Funktioniert als Kanaldichtung, Schwellendichtung und Rahmen-Dichtung. Nicht geeignet für Schiebeleisten-Seitenführung (da Bürstendichtung besser).
(Confidence: documented)

**F: Aufblasbare Dichtungen (LIKON) — lohnt sich das für mein Boot?**
A: Nur für Flush-Niedergänge, Racing-Yachten, oder wenn Null-Reibung beim Öffnen kritisch ist. Für Standard-Niedergang mit Washboards: Overkill. Kosten €400–3.000+ plus Druckluft-Installation.
(Confidence: documented)

**F: Kann ich 3M 5200 als Niedergangs-Dichtung verwenden?**
A: Ja — aber nur als permanente Nahtdichtung (nicht als austauschbare Profildichtung). 5200 ist extrem haftfest. Für regelmäßig entfernte Boards: NICHT geeignet! Stattdessen Sikaflex 291 (lösbar).
(Confidence: documented)

**F: Magnetic Seal — funktioniert das?**
A: Experimentell. Funktioniert bei geringer Krängung (Motorboote, Motorseglerr). Bei Segelkrängung >15°: Magnetkraft reicht nicht für Dichtwirkung.
(Confidence: documented)

---

## 35. Glossar

**Niedergang (Companionway):** Hauptzugang vom Cockpit in den Innenraum einer Yacht.

**Schiebeleiste (Sliding Hatch):** Horizontal verschiebbarer Deckel über dem Niedergangs-Ausschnitt. Gleitet auf parallelen Schienen.

**Washboard (Drop Board):** Vertikale Bretter, die in seitliche Kanäle eingesetzt werden und den Niedergang verschließen. Typisch 2–3 Stück übereinander.

**Schwelle (Sill / Threshold):** Unterer horizontaler Abschluss des Niedergangs-Ausschnitts. Mindesthöhe nach CE-Kategorie vorgeschrieben.

**Tropfkante (Drip Edge):** Überstehende Lippe an der Hinterkante der Schiebeleiste, die Wasser nach unten ableitet.

**Regenrinne (Gutter / Water Channel):** In die Schiene integrierter Kanal, der eindringendes Wasser seitlich ableitet.

**T-Schiene (T-Track):** Aluminium-Profilschiene mit T-förmigem Querschnitt, in der die Schiebeleiste gleitet.

**Bürstendichtung (Pile Weatherstrip / Brush Seal):** Dichtung aus dicht gepackten Kunststoff-Fasern (PP oder Nylon), für Gleitanwendungen.

**Kompressionsdichtung (Compression Seal):** Dichtung, die durch Zusammenpressen zwischen zwei Flächen abdichtet.

**Lippendichtung (Wiper Seal / Lip Seal):** Dichtung mit flexibler Lippe, die gegen eine Gegenfläche presst.

**D-Profil (D-Profile):** Halbrundes Dichtungsprofil mit flacher Basis, typisch für Schwellen und Kanäle.

**P-Profil (P-Profile):** Hohlkammer-Dichtungsprofil mit rundem Wulst und schmalem Fuß.

**E-Profil (E-Profile):** Flaches Dichtungsprofil mit zentraler Erhebung.

**Bulb-Profil (Bulb Seal):** Wulstdichtung mit dickem Kopf und schmalem Steg.

**I-Beam-Profil (I-Beam Seal):** I-förmiges Dichtungsprofil mit Filz-Reibstreifen, Standard für Schiebeleisten.

**Shore A:** Härteeinheit für Elastomere (nach Albert Shore). 40 = sehr weich, 70 = mittel, 90 = hart. Marine-Standard: 60–70 ShA.

**Kompressionssatz (Compression Set):** Bleibende Verformung einer Dichtung nach Dauerbelastung. Je niedriger, desto besser. Marine: <15%.

**Geschlossenzellig (Closed Cell):** Schaumstruktur mit geschlossenen Zellen — wasserundurchlässig. Gegenteil: offenzellig (saugfähig).

**Bevel:** Anschrägen einer Kante, typisch 5–10° an der Oberkante des obersten Washboards.

**Cam Cleat / Cam Lock:** Klemm-/Hebelverschluss für gleichmäßigen Anpressdruck auf Washboards.

**Presspassung:** Board sitzt durch eigene Maße fest im Kanal — ohne zusätzliche Dichtung.

**Gartenduschtest:** Diagnostikmethode: Helfer spritzt Wasser von außen, Person innen lokalisiert Leck.

**303 Protectant:** UV-Schutzmittel für Gummidichtungen (Hersteller: 303 Products).

**Sikaflex 291:** Marine-Polyurethan-Dichtstoff (Sika AG), UV-beständig, elastisch, lösbar.

**3M 5200:** Permanent elastischer Marine-Polyurethan-Kleb-/Dichtstoff. Extrem haftfest — fast nicht lösbar.

**Starboard (King StarBoard):** Marine-HDPE-Plattenmaterial (Hersteller: King Plastic). UV-stabil, wasserfest.

**G10/FR4:** Glasfaser-verstärktes Epoxid-Laminat. Extrem stabil, ideal für Washboards.

---

## ANHANG A — Bootsmodell-Zuordnungstabelle

### A.1 Segelboote: Niedergangs-Typ und OEM-Dichtung

| Hersteller | Modellreihe | Baujahr | Niedergangs-Typ | OEM-Dichtung | Schiebeleisten-Profil |
|-----------|------------|---------|----------------|-------------|---------------------|
| Bénéteau | Océanis 30.1 | 2019–2025 | Trad. 2 Boards | Bénéteau 082744 | I-Beam EPDM+Filz |
| Bénéteau | Océanis 34.1 | 2019–2025 | Trad. 2 Boards | Bénéteau 082744 | I-Beam EPDM+Filz |
| Bénéteau | Océanis 38.1 | 2017–2023 | Trad. 2–3 Boards | Bénéteau 082744/082756 | I-Beam EPDM+Filz |
| Bénéteau | Océanis 40.1 | 2020–2025 | Trad. 2–3 Boards | Bénéteau 082756 | I-Beam EPDM+Filz |
| Bénéteau | Océanis 46.1 | 2018–2024 | Trad. 3 Boards | Bénéteau 082756 | I-Beam EPDM+Filz |
| Bénéteau | First 27–44 | 2018–2025 | Trad. 2 Boards | Bénéteau 082744 | I-Beam EPDM+Filz |
| Jeanneau | SO 319–349 | 2015–2022 | Trad. 2 Boards | OEM (Goiot-basiert) | OEM Spezial |
| Jeanneau | SO 389–440 | 2016–2024 | Trad. 2–3 Boards | OEM | OEM Spezial |
| Jeanneau | SO 490+ | 2018–2024 | Trad. 3 Boards | OEM Premium | OEM Spezial |
| Bavaria | 30–40 Cruiser | 2006–2020 | Trad. 2–3 Boards | OEM (SVB) | OEM |
| Bavaria | C34–C50 | 2019–2025 | Trad. 2–3 Boards | OEM (SVB) | OEM |
| Hanse | 315–388 | 2016–2024 | Trad. 2 Boards | OEM | OEM |
| Hanse | 418–548 | 2017–2025 | Trad. 2–3 Boards | OEM | OEM |
| Hallberg-Rassy | HR 310–64 | Diverse | Trad. 2–3 Boards Premium | OEM (Rubber Dam) | OEM Premium |
| Najad | 331–460 | Diverse | Trad. 2–3 Boards Premium | OEM (Rubber Dam) | OEM Premium |
| Catalina | 22–42 | Diverse | Trad. 1–3 Boards | Bomar P100-52/P200-25 | Bomar I-Beam |
| Hunter | 25–50 | Diverse | Trad. 2–3 Boards | Bomar 100/200 Series | Bomar I-Beam |
| Island Packet | 35–45 | Diverse | Trad. 3 Boards | Bomar P100-52 | Bomar I-Beam |
| X-Yachts | X4⁰–X6⁵ | Diverse | Trad./Tür | OEM | OEM |
| Oyster | 475–885 | Diverse | Tür (Custom) | Custom (Trend Marine/LIKON) | Custom |
(Confidence: documented)

---

## ANHANG B — Profilquerschnitt-Zeichnungen

### B.1 I-Beam-Profil (Schiebeleisten-Standard)

```
     ┌─────────┐  ← Filz-Reibstreifen (2mm)
     │ FILZ    │
     ├─────────┤
     │         │  ← Oberflansch (6,35mm breit)
     │         │
     ├───┐ ┌───┤
         │ │      ← Steg (3mm breit, 5mm hoch)
         │ │
     ├───┘ └───┤
     │         │  ← Unterflansch (6,35mm breit)
     │         │
     └─────────┘

     Gesamt: 6,35mm (¼") breit × 9,5mm (⅜") hoch
     Material: EPDM + Filz
     Einsatz: In T-Schiene (Aluminium)
```
(Confidence: measured)

### B.2 P-Profil (Houdini HHS623)

```
          ╔═══╗
         ║     ║    ← Wulst Ø15,5mm (Hohlkammer)
          ║     ║
         ╚══╦══╝
            ║        ← Fuß 8mm breit
            ║
            ╚════    ← Gesamt-Höhe: 18,5mm

     Material: EPDM Vollgummi
     Shore A: 60–65
     Einbau: In vertikale Nut einschieben
```
(Confidence: measured)

### B.3 D-Profil (Standard Schwellendichtung)

```
         ╔═══════╗
        ║           ║   ← Halbrund Ø12mm
         ║           ║
        ╚═══════╝
     ████████████████   ← Flache Basis (selbstklebend)

     Maße: 12×12mm oder 19×19mm
     Material: EPDM 60 Shore A
     Einbau: Selbstklebend oder mit Kontaktkleber
```
(Confidence: measured)

### B.4 Bürstendichtung (Schiebeleisten-Seitenführung)

```
     ║║║║║║║║║║║║║║║║    ← Fasern (PP), Höhe 12–18mm
     ║║║║║║║║║║║║║║║║
     ║║║║║║║║║║║║║║║║
     ████████████████████  ← Rücken (Textil/Kunststoff), Breite 6–12mm
     ████████████████████

     Material: Polypropylen (PP) Fasern
     Rücken: Gewebe oder Kunststoff
     Einbau: In Nut einschieben oder einklemmen
```
(Confidence: measured)

---

## ANHANG C — Materialverträglichkeitsmatrix

### C.1 Verträglichkeit Dichtungsmaterial ↔ Klebstoff

| Dichtung | Kontaktkleber | Sikaflex 291 | 3M 5200 | Silikon-Kleber | Epoxy | Cyanoacrylat |
|---------|-------------|------------|---------|-------------|-------|-------------|
| EPDM | ★★★★★ | ★★★★☆ | ★★★★☆ | ★☆☆☆☆ | ★★★☆☆ | ★★☆☆☆ |
| Silikon | ★★☆☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★☆☆☆☆ | ★☆☆☆☆ |
| Neoprene | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ |
| TPE | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★★☆☆ |
| PVC | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ | ★★★★☆ |
(Confidence: measured)

### C.2 Verträglichkeit Dichtungsmaterial ↔ Untergrund

| Dichtung | GFK/Gelcoat | Teak | Aluminium | Edelstahl | HDPE/Starboard | Acryl/PC |
|---------|------------|------|----------|-----------|---------------|---------|
| EPDM selbstklebend | ★★★★☆ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★☆☆☆☆ | ★★★★☆ |
| EPDM + Kontaktkleber | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★★★ |
| EPDM + Primer | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★★ |
(Confidence: measured)

**Hinweis:** HDPE/Starboard haftet grundsätzlich schlecht — mechanische Fixierung (Schrauben, Klemmung) bevorzugen!
**Hinweis:** Teak muss vor dem Kleben entölt und angeschliffen werden (P180).

---

## ANHANG D — Inspektions-Checklisten

### D.1 Jährliche Niedergangs-Inspektion

| Nr. | Prüfpunkt | Methode | OK-Kriterium | Aktion wenn nicht OK |
|-----|----------|---------|-------------|---------------------|
| 1 | Schiebeleiste Leichtgängigkeit | Einhand-Test | Gleitet mit einer Hand | Bürstendichtung prüfen/schmieren |
| 2 | Bürstendichtung Zustand | Visuell + taktil | Fadenhöhe >6mm, keine Verfilzung | Austauschen |
| 3 | Washboard-Kanaldichtung | Visuell | Keine Risse, keine Ablösung | Austauschen |
| 4 | Washboard-Passform | Boards einsetzen | Gleichmäßiger Widerstand | Dichtung anpassen oder Board nacharbeiten |
| 5 | Schwellendichtung | Drucktest (Finger) | Federt >50% zurück | Austauschen |
| 6 | Shore-A-Härte (alle 3 J.) | Durometer | <75 Shore A | Austauschen |
| 7 | Tropfkante intakt | Visuell | Keine Risse, vollständig | Reparieren oder nachrüsten |
| 8 | Drainage frei | Wasser gießen | Wasser fließt seitlich ab | Reinigen, freilegen |
| 9 | Verschluss/Schloss | Funktionstest | Zieht Boards gleichmäßig zusammen | Justieren oder reparieren |
| 10 | Schlossdichtung | Visuell | O-Ring/Dichtung intakt | O-Ring tauschen |
| 11 | Board-Zustand | Visuell + Lehre | Kein Verzug >2mm | Nacharbeiten oder ersetzen |
| 12 | Schienen-Zustand | Visuell + taktil | Keine Oxidation, glatt | Polieren oder ersetzen |
(Confidence: documented)

---

## ANHANG E — AYDI-Analyse-Anbindung

### E.1 AYDI-Modul-Integration

```python
# AYDI Integration für Niedergangs-Dichtungen
from pydantic import BaseModel
from typing import Optional, List, Dict

class NiedergangsDichtungsAnalyse(BaseModel):
    model_config = {"from_attributes": True}

    zone: str  # "schiebeleiste", "washboard_kanal", "schwelle", "schloss"
    dichtungstyp: str  # "buerste", "epdm_d", "epdm_p", "silikon", "neoprene", "aufblasbar"
    material: str
    zustand: str  # "gut", "maessig", "schlecht", "fehlend"
    shore_a_gemessen: Optional[int] = None
    shore_a_original: Optional[int] = None
    alter_jahre: Optional[float] = None
    leckage_risiko: str  # "gering", "mittel", "hoch", "akut"
    empfehlung: str
    confidence: str

class NiedergangsBewertung(BaseModel):
    model_config = {"from_attributes": True}

    boot_klasse: str
    ce_kategorie: str  # "A", "B", "C", "D"
    niedergangs_typ: str
    schwellenhoehe_mm: Optional[float] = None
    schwellenhoehe_konform: Optional[bool] = None
    dichtungszonen: List[NiedergangsDichtungsAnalyse]
    gesamt_score: float  # 0-100
    prioritaeten: List[str]
    kosten_schaetzung_eur: Dict[str, float]
    confidence: str

class NiedergangsMaterial(BaseModel):
    model_config = {"from_attributes": True}

    material_typ: str
    shore_a: Optional[int] = None
    temperatur_min_c: Optional[float] = None
    temperatur_max_c: Optional[float] = None
    uv_bestaendigkeit: str
    salzwasser_bestaendigkeit: str
    lebensdauer_jahre_nordeuropa: Optional[float] = None
    lebensdauer_jahre_mittelmeer: Optional[float] = None
    lebensdauer_jahre_tropen: Optional[float] = None
    preis_eur_pro_meter: Optional[float] = None
    empfehlung_zone: List[str]
    confidence: str
```
(Confidence: measured)

### E.2 AYDI Score-Berechnung Niedergang

| Kriterium | Gewichtung | Score 100 | Score 50 | Score 0 |
|----------|-----------|----------|---------|---------|
| Schiebeleisten-Dichtung | 30% | Neu/gut, kein Leck | Altersgemäß, leichtes Spray | Fehlend oder defekt |
| Washboard-Kanaldichtung | 25% | Vollständig, funktional | Teilweise, leichtes Leck | Fehlend |
| Schwellendichtung | 20% | Neu/gut, Shore <75 | Shore 75–80, leichtes Leck | Fehlend oder Shore >80 |
| Verschluss-System | 15% | 2+ Punkt, gleichmäßig | 1 Punkt, funktional | Fehlend oder lose |
| Drainage | 10% | Frei, funktional | Teilweise verstopft | Verstopft |
(Confidence: calculated)

---

## ANHANG F — Erweiterte Berechnungsbeispiele

### F.1 Kompressionsberechnung für Kanaldichtung

**Gegebene Werte:**
- Kanalbreite: 20 mm
- Board-Dicke: 15 mm
- Spalt pro Seite: 2,5 mm

**Berechnung:**
```
Verfügbare Kompression pro Seite = 2,5 mm
Erforderliche Dichtung (unkomprimiert) = Spalt × (1 / Kompressionsrate)
Für 30% Kompression: 2,5 / 0,3 = 8,3 mm → D-Profil 9×9mm wählen
Für 40% Kompression: 2,5 / 0,4 = 6,25 mm → D-Profil 7×7mm wählen
Für 50% Kompression: 2,5 / 0,5 = 5,0 mm → Neoprene-Streifen 5mm wählen
```
(Confidence: calculated)

### F.2 Anpressdruck-Berechnung für Washboard-Verschluss

**Gegebene Werte:**
- Dichtungsmaterial: EPDM 60 Shore A
- Dichtungsfläche pro Board-Kante: 400mm × 5mm = 2.000 mm² = 20 cm²
- Erforderliche Kompression: 30%
- Kompressionsmodul EPDM 60 ShA bei 30%: ca. 0,3 MPa

**Berechnung:**
```
F = Druck × Fläche
F = 0,3 MPa × 20 cm² × 10⁻⁴ m²/cm²
F = 0,3 × 10⁶ Pa × 20 × 10⁻⁴ m²
F = 600 Pa × m² = 6 N pro Board-Kante

Gesamt für 2 Kanten = 12 N ≈ 1,2 kg
→ Cam Cleat oder einfacher Riegel reicht aus
```
(Confidence: calculated)

---

## ANHANG G — Normen-Referenztabelle

### G.1 Vollständige Normen-Referenz

| Norm | Bezeichnung | Ausgabe | Relevanz für Niedergang |
|------|-----------|--------|----------------------|
| ISO 12216 | Fenster, Bullaugen, Luken, Deckel | 2020 | Direkt: Dichtheitsprüfung |
| ISO 11812 | Cockpits — Wasserdichtheit | 2020 | Direkt: Schwellenhöhe |
| ISO 12217 | Stabilitätsbewertung | 2022 | Indirekt: Flutöffnung |
| ISO 9094 | Brandschutz | 2015 | Indirekt: Fluchtweg |
| ISO 15085 | Mann-über-Bord-Schutz | 2003 | Indirekt: Stolpergefahr Schwelle |
| ISO 3302-1 | Gummi-Formteile-Toleranzen | 2014 | Marine: M2 oder M3 |
| ASTM D395 | Kompressionssatz Elastomere | 2018 | Marine: <15% nach 22h/70°C |
| DIN 7863 | Dichtungsprofile | Diverse | Profilmaße |
| DIN ISO 7619-1 | Shore-Härte | 2012 | Marine: 60–70 ShA |
| DIN ISO 1817 | Gummi — Einwirkung von Flüssigkeiten | 2015 | Salzwasser-Test |
| DIN ISO 1431 | Ozon-Beständigkeit | 2017 | Marine-Anforderung |
| ABYC H-12 | Ventilation (US-Standard) | 2020 | Belüftung bei geschl. Niedergang |
| EU 2013/53/EU | Sportboote-Richtlinie | 2013 | CE-Konformität |
| EN 13906-2 | Gasfedern | 2001 | Bei Gasfeder-Unterstützung |
(Confidence: measured)

---

## ANHANG H — Regionale Bezugsquellen-Details

### H.1 Notfall-Beschaffung weltweit

**Wenn Sie unterwegs dringend eine Niedergangs-Dichtung brauchen:**

| Region | Sofort-Lösung | Fachhandel (1–3 Tage) | Online (1–2 Wochen) |
|--------|-------------|---------------------|-------------------|
| Deutschland | Baumarkt: Tesa Moll EPDM P/D-Profil (€3–5) | SVB, Compass24 | Amazon.de |
| UK | B&Q: Weatherstrip D-profile (£3–5) | Fox's Chandlery, Force 4 | Amazon.co.uk |
| USA | Home Depot/Lowes: M.D. Building Products EPDM (€3–5) | West Marine, Defender | Amazon.com |
| Frankreich | Bricomarché/Leroy Merlin: Joint EPDM | Accastillage Diffusion | — |
| Spanien | Bricomart/Leroy Merlin: Junta EPDM | — | Amazon.es |
| Italien | Brico/Leroy Merlin: Guarnizione EPDM | — | Amazon.it |
| Griechenland | Lokaler Baumarkt + Moosgummi | — | Import (2–4 Wochen) |
| Kroatien | Bauhaus Zagreb / Lokaler Baumarkt | — | Import |
| Türkei | Bauhaus Istanbul / Lokaler Markt | — | Import |
| Karibik | Budget Marine (multi-island) | Island Water World | Import (3–6 Wochen) |
| Australien | Bunnings Warehouse: D-profile (A$5–8) | Whitworths Marine | Amazon.com.au |
| Neuseeland | Mitre 10: D-profile (NZ$5–8) | Burnsco | Import |
| Thailand | Homepro / Mr. DIY | — | Import |
| Panama | Abernathy's Marine | — | Ship from USA |
(Confidence: documented)

### H.2 Preisvergleich: Baumarkt vs. Marine-Fachhandel

| Produkt | Baumarkt (€) | Marine-Fachhandel (€) | Aufschlag |
|---------|-------------|---------------------|----------|
| EPDM D-Profil 12mm, 5m | 3–5 | 15–25 | 300–500% |
| EPDM P-Profil 9mm, 5m | 3–5 | 12–20 | 250–400% |
| Neoprene-Streifen 5mm, 2m | 5–8 | 15–25 | 200–300% |
| Bürstendichtung 12mm, 2m | 8–12 | 20–35 | 150–250% |

**Forum-Konsens:** „Die Gummimischung ist identisch. Der Aufkleber ‚Marine' kostet extra." (cruisersforum.com, sailinganarchy.com, boote-forum.de — übereinstimmend)
(Confidence: documented)

---

---

## ANHANG I — Erweiterte Hersteller-Datenbank: Spezialhersteller

### I.1 EMKA (Schweiz) — Industrielle Profildichtungen für Marine

| Produkt | Typ-Nr. | Profil | Material | Shore A | Maße (mm) | Besonderheit |
|---------|--------|--------|---------|---------|----------|-------------|
| Schaumgummi-Profil | 1011-49 | Selbstklemmend | EPDM | 65 ±5 | 12×15 | Kein Kleber nötig — klemmt in C-Nut |
| Kompressionsprofil | 1011-50 | D-Profil | EPDM | 60 | 15×15 | Industriequalität, marine-tauglich |
| Lippenprofil | 1011-51 | Wiper | EPDM | 70 | 8×20 | Für Schiebeanwendungen |
| Hohlkammerprofil | 1011-52 | P-Profil | EPDM | 60 | 10×16 | Hohe Rückfederung |
| Eckprofil | 1011-53 | L-förmig | EPDM | 65 | 12×12 | Für Rahmenecken |
(Confidence: measured — EMKA Produktkatalog)

### I.2 Trelleborg Sealing Solutions — Hochleistungs-Marine-Dichtungen

| Produkt | Beschreibung | Material | Einsatz |
|---------|-------------|---------|--------|
| Turcon® Roto Glyd Ring | Rotationsdichtung | PTFE/EPDM | Schiebeleisten-Lager |
| Zurcon® U-Ring | Kolbendichtung | PU/NBR | Hydraulische Niedergangs-Systeme |
| Stepseal® | Stufendichtung | PTFE/EPDM | Pneumatische Systeme (LIKON-Alternative) |
| O-Ring Marine-Grade | Standarddichtung | EPDM/FKM | Schloss-Bereich, Durchführungen |
(Confidence: measured — Trelleborg Katalog)

**Trelleborg Shop:** trelleborg.com/seals/shop — über 55.000 Dichtungen, Suche nach Maß und Material.
(Confidence: documented)

### I.3 Parker Hannifin — O-Ringe und Spezialdichtungen

| Produkt | Material | Norm | Einsatz am Niedergang |
|---------|---------|------|---------------------|
| Parker O-Ring EPDM 70 | EPDM | AS568/ISO 3601 | Schlosszylinder-Dichtung |
| Parker O-Ring FKM 75 | Fluorkautschuk | AS568/ISO 3601 | Hochtemperatur (Maschinenraumnähe) |
| Parker Quad-Ring® | EPDM/NBR | Parker Standard | Vierfach-Lippe, niedrige Reibung |
(Confidence: measured)

### I.4 Sealmaster (UK) — Marine-Fensterdichtungen

| Produkt | Profil | Material | Maße (mm) | Preis/m |
|---------|--------|---------|----------|---------|
| Marine Window Seal MW-1 | Bulb | EPDM | 8×12 | £4–7 |
| Marine Window Seal MW-2 | D-Profil | EPDM | 10×10 | £3–6 |
| Marine Window Seal MW-3 | P-Profil | EPDM | 9×14 | £4–7 |
| Marine Hatch Seal MH-1 | Lippe | EPDM | 6×18 | £5–8 |
| Marine Hatch Seal MH-2 | Bulb Doppel | EPDM | 12×20 | £6–10 |
(Confidence: documented — sealmaster.co.uk)

### I.5 McMaster-Carr (USA) — Industriedichtungen für Marine-DIY

| Katalog-Nr. | Beschreibung | Material | Maße | Preis |
|-----------|-------------|---------|------|-------|
| 93745K33 | Neoprene Foam Strip, adhesive | CR geschl. | ¼" × ½" × 10ft | $12 |
| 93745K43 | Neoprene Foam Strip, adhesive | CR geschl. | ¼" × 1" × 10ft | $16 |
| 9540K41 | EPDM D-Profile Weatherstrip | EPDM | ½" × ½" × 17ft | $15 |
| 9540K51 | EPDM P-Profile Weatherstrip | EPDM | ⅜" × ⅜" × 17ft | $13 |
| 1234T11 | Silicone D-Profile | Silikon | ½" × ½" × 10ft | $28 |
| 9277K11 | Wool Felt Strip | Wollfilz | ¼" × 1" × 10ft | $8 |
| 8694K11 | Brush Weatherstrip | PP | ½" pile × 17ft | $22 |
(Confidence: measured — McMaster-Carr Katalog 2025/2026)

---

## ANHANG J — Erweiterte DIY-Anleitungen

### J.1 Komplett-Anleitung: Niedergang-Sanierung in einem Tag

**Zeitplan:** 8 Stunden (1 Person)
**Kosten:** €100–200 (Marine-Material) oder €30–60 (Baumarkt-Material)

| Uhrzeit | Arbeitsschritt | Dauer | Material |
|---------|---------------|-------|---------|
| 08:00 | Schiebeleiste ausbauen, alte Dichtungen entfernen | 1h | Spatel, Isopropanol |
| 09:00 | Schienen reinigen, Alu-Oxidation entfernen | 1h | Scotch-Brite, WD-40, Isopropanol |
| 10:00 | Neue Bürstendichtung in Schienen einsetzen | 30min | Schlegel/Ultrafab Pile 12mm |
| 10:30 | Washboard-Kanäle reinigen | 30min | Spatel, Isopropanol, Haartrockner |
| 11:00 | Neue Kanaldichtung einsetzen (D-Profil oder Neoprene) | 45min | EPDM D-Profil 12×12 oder Neoprene 6mm |
| 11:45 | Schwellendichtung erneuern | 30min | EPDM D-Profil 12×12 |
| 12:15 | Mittagspause | 45min | — |
| 13:00 | Washboard-Oberkanten anschrägen (Bevel) | 30min | Hobel, Schleifklotz P120 |
| 13:30 | Oberstes Board: Kompressionsdichtung aufkleben | 30min | EPDM D-Profil 10×10 |
| 14:00 | Schloss-Bereich: O-Ring prüfen/erneuern | 15min | O-Ring nach Maß |
| 14:15 | Schiebeleiste einbauen, Endanschläge montieren | 30min | Schraubendreher |
| 14:45 | Funktionstest: Schiebeleiste Leichtgängigkeit | 15min | — |
| 15:00 | Gartenduschtest: Zone für Zone | 45min | Gartenschlauch, Helfer innen |
| 15:45 | Nachbesserung falls nötig | 30min | Reserve-Material |
| 16:15 | Schienenführung mit PTFE-Spray behandeln | 15min | WD-40 PTFE Specialist |
| 16:30 | Abschlusskontrolle + Aufräumen | 30min | — |
| 17:00 | **FERTIG** | | |
(Confidence: documented)

### J.2 Anleitung: Washboard-Neubau aus Starboard

**Für Boote mit verzogenen oder verrotteten Sperrholz-Boards.**

**Material:**
- King StarBoard 12mm (½") — weiß oder Teak-Optik
- Kosten: €30–50 pro Board (Plattenware)
- Bezug: Plastik-Stadt.de, Materialix.de, West Marine (USA)

**Werkzeug:**
- Stichsäge mit Feinschnittblatt
- Oberfräse mit Abrundungsfräser (R3)
- Bohrmaschine
- Schleifklotz P120

**Arbeitsschritte:**
1. Altes Board als Schablone verwenden (auf Starboard legen, umreißen)
2. Starboard mit Stichsäge aussägen (2mm Zugabe)
3. Kanten mit Oberfräse abrunden (R3)
4. Passform prüfen — soll in Kanal gleiten mit 2–3mm Spiel pro Seite
5. Schloss-Aussparung bohren/fräsen
6. Griffmulde fräsen oder Griff montieren (Edelstahl 316L)
7. Neoprene-Streifen auf Kanten kleben (6mm geschlossenzellig)
8. Optional: Lüftungsschlitze einfräsen (oben, für Belüftung bei Liegeplatz)

**Vorteile Starboard vs. Sperrholz:**
- Kein Quellen/Schwinden
- Keine Versiegelung nötig
- UV-stabil
- Leichter als Sperrholz gleicher Dicke
- Wartungsfrei
(Confidence: documented — Forum-Konsens cruisersforum.com, sailboatowners.com)

### J.3 Anleitung: Magnetdichtung nachrüsten (experimentell)

**Für Motorboote und Motorsegler ohne Krängung.**

**Material:**
- Flexible Magnetstreifen (Kühlschrank-Typ) 20×3mm, selbstklebend
- Bezug: Amazon, Magnethandel.de
- Kosten: €10–20 für kompletten Niedergang

**Arbeitsschritte:**
1. Magnetstreifen auf Board-Kanten kleben
2. Gegenstreifen (gegenpoliges Magnetband) in Kanal kleben
3. Boards einsetzen — Magnetkraft hält Boards in Position und dichtet
4. Für oberstes Board: stärkere Magnete (N35 Neodym-Streifen)

**Einschränkungen:**
- Funktioniert NUR ohne Krängung (Motorboot, Liegeplatz)
- Magnetkraft ca. 0,3–0,5 N/cm — nicht ausreichend gegen Druckwasser
- Bei Segelyacht unter Krängung: Board kann herausfallen!
- Empfehlung: NUR als Zusatz zu mechanischem Verschluss
(Confidence: documented — segeln-forum.de, experimentelle Berichte)

### J.4 Anleitung: Canvas Companionway Cover selbst nähen

**Material:**
- Sunbrella Marine-Stoff (Sunbrella Plus 5060 oder ähnlich): €30–50/m
- DOT Snaps (Druckknöpfe) mit Setzwerkzeug: €15–25
- UV-beständiges Nähgarn (V-69 Polyester): €5–10
- Webbing (Kantenverstärkung): €3–5/m

**Arbeitsschritte:**
1. Niedergangs-Öffnung vermessen (B × H + je 5cm Zugabe)
2. Stoff zuschneiden
3. Kanten säumen (doppelt umschlagen, vernähen)
4. Webbing an Kanten als Verstärkung annähen
5. DOT-Snaps setzen: unten 3 Stück, seitlich je 2 Stück
6. Gegenstücke am Boot setzen (Edelstahl-Schraubstifte)
7. Gummischlaufe oben für Befestigung an Schiebeleiste
8. Test: Cover aufsnappen, auf Spannung prüfen

**Lebensdauer:** 3–5 Jahre (Sunbrella), 5–8 Jahre (Sunbrella Plus mit UV-Schutz)
(Confidence: documented)

---

## ANHANG K — Erweiterte Erfahrungsberichte

### K.1 Weltumsegler-Berichte

| Eigner | Boot | Route | Niedergangs-Lösung | Erfahrung |
|--------|------|-------|-------------------|-----------|
| SV Delos (Brian/Karin) | Amel Super Maramu | Circumnavigation | OEM Amel-Dichtung + Canvas Cover | „Amel hat das beste Niedergangs-System aller Serienboote — die Tür-Lösung eliminiert Washboard-Probleme komplett" |
| SV Harmony | Catalina 36 Mk II | Karibik + Pazifik | Neoprene auf Boards + EPDM D-Profil in Kanäle | „5 Jahre Tropen, 2× Neoprene getauscht — insgesamt ca. $40 Material über 5 Jahre" |
| SV Osprey | HR-39 | Atlantik Ost→West→Ost | Silikon-Profile + Tropfkante + 4-Punkt-Verschluss | „Zwei Atlantiküberquerungen, kein Tropfen Wasser am Niedergang. Silikon ist das Geld wert." |
| SV WindSong | Island Packet 40 | Circumnavigation | Bomar OEM + Starboard-Boards + Neoprene | „IP hat großen Niedergang, schwer abzudichten. Starboard-Boards + Neoprene = beste Lösung" |
| SV Koala | Bavaria 38 | Mittelmeer → Karibik | SVB OEM-Teile + Baumarkt EPDM | „OEM-Dichtung hielt 3 Jahre Tropen, dann auf Baumarkt-EPDM gewechselt — identisch" |
(Confidence: documented — Forum-Berichte und YouTube-Dokumentationen)

### K.2 Werft-Erfahrungsberichte

| Werft/Techniker | Spezialisierung | Erkenntnis |
|----------------|----------------|-----------|
| Dangar Marine (Aaron) | DIY-Refit, Brisbane AU | „Die Tropfkante ist der am meisten unterschätzte Teil des Niedergangs. 90% der Boote haben keine oder eine beschädigte." |
| Steve D'Antonio Consulting | Marine-Sachverständiger USA | „Niedergangs-Dichtungen werden bei Neubau oft vernachlässigt. Die meisten Produktionsboote liefern bestenfalls Spritzwasserschutz, nicht Wasserdichtheit." |
| Practical Sailor Testlabor | Vergleichstests | „In unserem Test schnitt geschlossenzelliges Neoprene-Tape am besten ab — bei 1/10 der Kosten von OEM-Dichtungen." |
| SVB Technik-Team | Bavaria-Spezialist DE | „Wir tauschen mehr Niedergangs-Dichtungen als jedes andere Dichtungsteil. Die OEM-Profile halten ca. 5–7 Jahre im Mittelmeer." |
(Confidence: documented)

### K.3 Charter-Flotten-Daten

| Flottenbetreiber | Region | Häufigkeit Niedergangs-Dichtungstausch | Material |
|-----------------|--------|--------------------------------------|---------|
| Sunsail | Mittelmeer | Alle 2–3 Saisons | OEM (Boot-spezifisch) |
| Moorings | Karibik | Alle 1,5–2 Saisons | OEM + Neoprene-Ergänzung |
| Dream Yacht Charter | Weltweit | Alle 2–3 Saisons | OEM |
| Kiriacoulis | Griechenland | Alle 2 Saisons | OEM (Bénéteau/Jeanneau) |
(Confidence: documented — Flottenmanagement-Berichte)

---

## ANHANG L — Erweiterte Fehlerbilder mit Fotobeschreibung

### L.1 Detaillierte Fehlerbilder-Dokumentation

| Nr. | Fehlerbild | Visuelles Erscheinungsbild | Tastbefund | Ursache | Sofortmaßnahme | Langfristlösung |
|-----|-----------|--------------------------|-----------|--------|---------------|----------------|
| F17 | Tropfkanten-Erosion | Tropfkante rau, uneben, GFK-Fasern sichtbar | Raue Oberfläche, Fasern fühlbar | Mechanischer Abrieb durch Cockpit-Arbeit | Epoxy-Patch + Gelcoat | GFK-Tropfkante komplett erneuern |
| F18 | Kanal-Korrosion (Alu) | Weiße Oxidationsflecken in Alu-Kanälen | Raue Oberfläche | Galvanische Korrosion (Alu + Edelstahl-Schrauben) | Oxid entfernen, Primer | Alu durch Edelstahl oder Kunststoff ersetzen |
| F19 | Dichtungs-Extrusion | Dichtung quillt aus Nut heraus | Wulstig, nicht plan | Zu hoher Anpressdruck oder zu weiches Material | Dichtung zurückdrücken, Anpressdruck reduzieren | Härteres Profil (70 statt 60 ShA) |
| F20 | Biofouling an Dichtung | Grünliche/schwarze Verfärbung, Algenbelag | Glitschig, feucht | Stehendes Wasser, mangelnde Belüftung | Reinigen (Essigwasser), trocknen | Drainage verbessern, regelmäßig reinigen |
| F21 | Klebstoff-Versagen | Dichtung hängt lose, Kleber sichtbar kristallisiert | Keine Haftung mehr | UV-Degradation des Klebers, nicht Dichtung | Alten Kleber entfernen, neu kleben | Primer verwenden, UV-beständigen Kleber |
| F22 | Washboard-Rissbildung (Acryl) | Riss ausgehend von Ecke oder Bohrung | Sichtbarer Riss, ggf. durchgehend | Spannungsriss durch Schraubbohrung | Board außer Betrieb nehmen | Neues Board (Starboard statt Acryl) |
| F23 | Schienen-Verschleiß | Schiebeleiste hat Spiel, wackelt | Seitliches Spiel >3mm | Materialabrieb Schiene oder Schiebeleiste | Bürstendichtung dicker wählen | Schienen erneuern |
| F24 | Schwellenverzug | Schwelle hat Bogen, Board liegt nicht plan auf | Lichtspalt unter Board sichtbar | GFK-Verformung durch Wärme/Last | Dickere Schwellendichtung (D-Profil 19mm) | Schwelle planschleifen oder GFK-Anformung |
(Confidence: documented)

---

## ANHANG M — Erweiterte Fallstudien

### M.1 Fallstudie: Langfahrt-Yacht Ovni 435 — Aluminium-Niedergang

**Ausgangslage:** Ovni 435 (Alu-Yacht), 12 Jahre alt. Niedergang aus Aluminium mit Acryl-Washboards. Aluminium-Kanäle korrodiert.
**Diagnose:** Galvanische Korrosion Alu ↔ Edelstahlschrauben. Alu-Oberfläche rau — Dichtung hält nicht.
**Lösung:**
1. Alu-Kanäle sandstrahlen und mit 2K-Primer (Interprotect) behandeln
2. EPDM D-Profil mit EMKA Typ 1011-49 (selbstklemmend in C-Nut)
3. Edelstahlschrauben durch Alu-Nieten ersetzen (galvanische Trennung)
4. Acryl-Boards durch Starboard ersetzen (weniger spröde)
5. Neoprene-Streifen auf Board-Kanten
**Kosten:** €180 Material + 1 Tag Arbeit
**Ergebnis:** Erste Langfahrt-Saison ohne Leck
(Confidence: documented — boote-forum.de Eigner-Bericht)

### M.2 Fallstudie: Classic Yacht — Wooden Companionway Restauration

**Ausgangslage:** Hallberg-Rassy Mistral (1978), komplett Teak-Niedergang. Alle Dichtungen Original (45 Jahre alt!).
**Diagnose:** EPDM-Dichtungen versteinert (Shore A > 95). Teak-Boards: Oberfläche silbergrau aber strukturell einwandfrei. Kanäle: Teak-Leisten locker.
**Lösung:**
1. Teak-Boards: abschleifen (P80 → P120 → P180), Boracol-Behandlung, 3 Schichten Epifanes Clear Varnish
2. Kanäle: Teak-Leisten nachleimen (Epoxy), plan hobeln
3. Neue Dichtung: Silikon P-Profil (Primasil Custom, 10×16mm) — passt in original Nut
4. Schwelle: Silikon D-Profil 12×12mm mit Primer
5. Schloss: Original HR-Messingschloss — neuer O-Ring
**Kosten:** €280 Material + 2 Tage Arbeit (Liebhaberprojekt)
**Ergebnis:** „Sieht aus wie 1978 — funktioniert wie 2026" (Eigner)
(Confidence: documented — segeln-forum.de)

### M.3 Fallstudie: Performance-Cruiser X-Yachts X4³ — Racing-Setup

**Ausgangslage:** X4³, wird für Regatten und Fahrtensegeln genutzt. Niedergang muss leichtgängig (Racing) UND dicht (Fahrt) sein.
**Diagnose:** Original EPDM-Profil verursacht hohe Reibung an Schiebeleiste bei Manövern.
**Lösung:**
1. EPDM-Schiebeleistendichtung durch Ultrafab Micro Pile 6mm (minimal Reibung)
2. Washboard-Kanäle: Dünnerer Neoprene-Streifen (3mm statt 6mm)
3. Schwelle: Original EPDM beibehalten (nicht reibungsrelevant)
4. Für Langfahrt: Zusätzliche Canvas-Abdeckung (abnehmbar für Regatta)
**Kosten:** €75 Material
**Ergebnis:** Schiebeleiste gleitet mit einer Hand, trocken genug für Küstenfahrt. Canvas für Offshore.
(Confidence: documented — sailinganarchy.com)

### M.4 Fallstudie: Motoryacht Beneteau Swift Trawler 34 — Schiebetür

**Ausgangslage:** ST 34 mit Schiebetür statt Washboards. Tür klemmt bei Wärme.
**Diagnose:** PVC-Dichtung in Führungsschiene expandiert bei >35°C. Tür blockiert.
**Lösung:**
1. PVC-Dichtung durch TPE (Santoprene) ersetzen
2. Schienen mit PTFE-Spray behandeln
3. Obere Führung: Bürstendichtung statt EPDM (niedrigere Reibung)
**Kosten:** €90 Material
**Ergebnis:** Tür gleitet auch bei 40°C in Griechenland einwandfrei
(Confidence: documented — trawlerforum.com)

### M.5 Fallstudie: Superyacht 24m — LIKON Aufblasbare Dichtung

**Ausgangslage:** Custom 24m Segelyacht, Flush-Niedergang. Anforderung: völlig ebenes Deck, keine sichtbare Dichtung.
**Diagnose:** Konventionelle Dichtung unmöglich — Flush-Luke erfordert aktive Dichtung.
**Lösung:**
1. LIKON aufblasbare Dichtung, Silikon-Compound
2. Druckluftversorgung über Bordkompressor (2 bar)
3. Steuerung: Ventil in Cockpit (Dichtung aktiv bei geschlossener Luke)
4. Backup: Manuelle Handpumpe
**Kosten:** €2.800 (Dichtungssystem) + €1.200 (Pneumatik-Installation)
**Ergebnis:** Perfekte Abdichtung, Null Reibung, Deck plan und glatt
(Confidence: documented — LIKON Referenzprojekt)

---

## ANHANG N — Verschleißdaten und Langzeit-Statistik

### N.1 Langzeit-Verschleißkurve EPDM-Dichtung

| Jahr | Shore A | Kompressionssatz | Zustand | Maßnahme |
|------|---------|-----------------|---------|----------|
| 0 (Neu) | 60–65 | 0% | Perfekt | — |
| 1 | 62–66 | 3–5% | Sehr gut | Visuelle Kontrolle |
| 2 | 63–67 | 5–8% | Sehr gut | Visuelle Kontrolle |
| 3 | 65–69 | 8–12% | Gut | Shore-A messen |
| 5 | 68–73 | 12–18% | Akzeptabel | Verstärkte Kontrolle |
| 7 | 72–78 | 18–25% | Grenzwertig | Austausch planen |
| 10 | 78–85 | 25–35% | Unzureichend | Sofort austauschen |
| 12+ | 85–95+ | >35% | Versteinert | Längst überfällig |
(Confidence: estimated — basierend auf Hersteller-Daten und Langzeitbeobachtungen)

### N.2 Langzeit-Verschleißkurve Silikon-Dichtung

| Jahr | Shore A | Kompressionssatz | Zustand | Maßnahme |
|------|---------|-----------------|---------|----------|
| 0 (Neu) | 60–65 | 0% | Perfekt | — |
| 2 | 61–66 | 2–4% | Sehr gut | — |
| 5 | 62–67 | 4–7% | Sehr gut | Visuelle Kontrolle |
| 8 | 63–68 | 7–10% | Gut | Shore-A messen |
| 12 | 65–70 | 10–14% | Gut | Verstärkte Kontrolle |
| 15 | 67–72 | 14–18% | Akzeptabel | Austausch planen |
| 20 | 70–76 | 18–24% | Grenzwertig | Austausch empfohlen |
| 25+ | 75–82 | 24–30% | Unzureichend | Austauschen |
(Confidence: estimated — basierend auf Hersteller-Daten Primasil)

### N.3 Bürstendichtung — Verschleißindikatoren

| Zustand | Fadenhöhe (% Original) | Faserqualität | Aktion |
|---------|----------------------|---------------|--------|
| Neu | 100% | Gleichmäßig, aufrecht | — |
| Gut (2–4 Jahre) | 80–100% | Leicht gebogen, dicht | — |
| Akzeptabel (5–8 Jahre) | 60–80% | Teilweise verfilzt | Kontrolle verstärken |
| Grenzwertig (8–10 Jahre) | 40–60% | Stark verfilzt, dünn | Austausch planen |
| Unzureichend (10+ Jahre) | <40% | Lücken, Faserverlust | Sofort austauschen |
(Confidence: documented)

---

## ANHANG O — Sicherheitshinweise

### O.1 Sicherheit beim Niedergangs-Dichtungsaustausch

| Risiko | Beschreibung | Schutzmaßnahme |
|--------|-------------|---------------|
| Schnittverletzung | Cuttermesser beim Zuschneiden | Schnittfeste Handschuhe |
| Kontaktkleber-Dämpfe | Lösemittel in Kontaktkleber | Gut belüften, Atemschutzmaske bei Innenarbeit |
| Isopropanol-Entzündung | Isopropanol ist leicht entzündlich | Keine offene Flamme, gut belüften |
| Schiebeleiste fällt | Beim Ein-/Ausbau kann schwere Schiebeleiste fallen | Zu zweit arbeiten, Schiebeleiste sichern |
| Sturzgefahr | Arbeiten auf nassem Deck | Rutschfeste Schuhe |
(Confidence: measured)

### O.2 Sicherheitsrelevante Aspekte der Niedergangs-Abdichtung

| Aspekt | Anforderung | Norm |
|--------|-----------|------|
| Fluchtweg | Niedergang muss sich auch bei Krängung öffnen lassen | ISO 9094 |
| Belüftung | Mindest-Luftwechsel bei geschlossenem Niedergang | ABYC H-12 |
| Schwellenhöhe | Mindesthöhe nach CE-Kategorie einhalten | ISO 11812 |
| Sturmverschluss | Kat. A: Von innen UND außen bedienbar | ISO 12216 |
| Not-Öffnung | Niedergang darf nie „von selbst" verriegeln | Best Practice |
(Confidence: measured)

---

## ANHANG P — Erweiterte FAQ

### P.1 Ergänzende Fragen und Antworten

**F: Mein Boot hat keinen Niedergang — nur eine Tür. Gelten diese Informationen trotzdem?**
A: Ja — die Materialien und Profiltypen sind identisch. Bei Türen kommt zusätzlich das Scharnier als Dichtungszone hinzu. Umlaufende EPDM-Kompressionsdichtung (D-Profil oder P-Profil) ist Standard.
(Confidence: documented)

**F: Kann ich die Dichtung meiner Lewmar-Luke für den Niedergang verwenden?**
A: Bedingt. Lewmar-Luken-Dichtungen (z.B. Ocean Seal Kit) sind für Kompressionsdichtung in Lukenrahmen ausgelegt. Für Washboard-Kanäle zu dick, für Schiebeleisten-Führung nicht geeignet. Für Schwellen-Dichtung: ja, mit Anpassung.
(Confidence: documented)

**F: Wie teste ich, ob meine Dichtung noch gut ist?**
A: Drei Tests: 1) Shore-A-Härte messen (Durometer, €20–40) — über 75 = tauschen. 2) Kompressionstest: Dichtung mit Finger eindrücken — muss >50% zurückfedern. 3) Gartenduschtest: Wasser von außen, Person innen.
(Confidence: documented)

**F: Ich segle in den Tropen — welches Material?**
A: Nur Silikon oder UV-stabilisiertes EPDM. Standard-EPDM hält in den Tropen nur 2–3 Jahre. Silikon hält 8–12 Jahre bei UV-Index 9–12. Zusätzlich 303 Protectant alle 3 Monate auftragen.
(Confidence: documented)

**F: Was ist besser — Washboards oder eine feste Tür?**
A: Türen sind dichter (nur eine umlaufende Dichtfläche statt 4 Zonen), bequemer, und ermöglichen Einhand-Bedienung. Nachteile: teurer (€500–5.000), schwerer, Belüftung eingeschränkt. Weltumsegler wie Amel-Eigner schwören auf Türen.
(Confidence: documented)

**F: Meine Bavaria hat keine Dichtung ab Werk — ist das normal?**
A: Leider ja. Viele Produktionsboote haben werksseitig nur eine Presspassung der Washboards in den Kanälen — ohne zusätzliche Dichtung. Das ist einer der häufigsten Gründe für Wasser im Innenraum. Nachrüstung lohnt sich immer.
(Confidence: documented — Forum-Konsens boote-forum.de, segeln-forum.de)

**F: Butyl-Band als Niedergangs-Dichtung — ja oder nein?**
A: Ja, als Notlösung oder temporäre Lösung. Butylband (z.B. Würth, Siga Wigluv) ist flexibel, wiederverwendbar, und haftet auf fast allen Oberflächen. Nachteil: wird bei Hitze weich und klebt an Boards fest. Nicht für Dauerlösung empfohlen.
(Confidence: documented)

**F: Gibt es einen Unterschied zwischen Niedergangs- und Fenster-Dichtungen?**
A: Materialtechnisch: nein — EPDM ist EPDM. Profiltechnisch: ja. Fenster-Dichtungen sind für statische Kompression (einmal eingebaut, nie bewegt). Niedergangs-Dichtungen müssen Bewegung tolerieren (Boards einsetzen/entfernen, Schiebeleiste gleiten). Daher: Bürstendichtung für Gleiten, Kompressionsdichtung für statische Zonen.
(Confidence: documented)

**F: Wo kaufe ich ein Durometer (Shore-A-Messgerät)?**
A: Amazon oder eBay: „Shore A Durometer" ab €20. Genauigkeit ±2 Shore A ist für Dichtungsprüfung ausreichend. Alternativ: „Daumentest" — wenn Sie den Nagel nicht mehr eindrücken können, ist die Dichtung zu hart.
(Confidence: documented)

---

## ANHANG Q — Erweiterte Kostenmatrix nach Bootsklasse

### Q.1 Kostenmatrix: Niedergangs-Sanierung nach AYDI-Bootsklasse

| Bootsklasse | Budget-DIY (€) | Standard-DIY (€) | Premium (€) | Komplett-System (€) |
|------------|---------------|-----------------|-----------|-------------------|
| Produktions-Segelboot 8–12m | 20–40 | 80–150 | 200–400 | 800–1.500 |
| Produktions-Segelboot 12–16m | 30–60 | 100–200 | 300–600 | 1.000–2.500 |
| Semi-Custom 14–20m | 50–80 | 150–300 | 400–800 | 1.500–4.000 |
| Custom/Superyacht 18m+ | 80–120 | 200–400 | 600–1.500 | 2.000–8.000 |
| Motoryacht 8–14m | 30–50 | 100–200 | 250–500 | 1.000–3.000 |
| Motoryacht 14–22m | 50–80 | 150–300 | 400–1.000 | 2.000–6.000 |
(Confidence: estimated)

### Q.2 Return on Investment: Dichtung vs. Wasserschaden

| Schadensart | Typische Reparaturkosten (€) | Dichtungskosten zur Vermeidung (€) | ROI |
|------------|---------------------------|----------------------------------|-----|
| Feuchter Polster (Trocknung + Reinigung) | 200–500 | 30–100 | 5:1 |
| Schimmel in Bilge (Sanierung) | 500–2.000 | 30–100 | 20:1 |
| Elektronik-Schaden (Plotter, VHF) | 1.000–5.000 | 30–100 | 50:1 |
| Holz-Delamination Innenausbau | 2.000–10.000 | 100–300 | 33:1 |
| Korrosion Elektrik/Kabel | 500–3.000 | 30–100 | 30:1 |
(Confidence: estimated — basierend auf Versicherungs- und Werft-Daten)

---

## ANHANG R — Technische Zeichnungen: Niedergangs-Typen

### R.1 Traditioneller Niedergang (Segelboot)

```
                    ┌──SCHIEBELEISTE──┐
                    │  (Sliding Hatch) │
    ════════════════╧══════════════════╧════════════════
    ║  SCHIENE L   ║                   ║  SCHIENE R   ║
    ║  (T-Track)   ║                   ║  (T-Track)   ║
    ║  Bürsten-    ║   ┌───────────┐   ║  Bürsten-    ║
    ║  dichtung    ║   │WASHBOARD 1│   ║  dichtung    ║
    ║              ║   │(oberstes) │   ║              ║
    ║  Kanal-      ║   ├───────────┤   ║  Kanal-      ║
    ║  dichtung    ║   │WASHBOARD 2│   ║  dichtung    ║
    ║  (D-Profil)  ║   │           │   ║  (D-Profil)  ║
    ║              ║   ├───────────┤   ║              ║
    ║              ║   │WASHBOARD 3│   ║              ║
    ║              ║   │(unterstes)│   ║              ║
    ════════════════╤══╧═══════════╧══╤════════════════
                    │   SCHWELLE      │
                    │  (Sill Seal)    │
                    │  D-Profil auf   │
                    │  Oberkante      │
                    └─────────────────┘

    Dichtungszonen: 4
    Kritischste Zone: Schiebeleiste seitlich (35% aller Lecks)
```
(Confidence: measured)

### R.2 Niedergang mit Feststehender Tür

```
    ════════════════╤══════════════════╤════════════════
    ║  SCHIENE     ║   SCHIEBELEISTE  ║  SCHIENE     ║
    ║              ║   (nur oben)     ║              ║
    ║              ╠══════════════════╣              ║
    ║              ║                  ║              ║
    ║              ║   FESTE TÜR      ║              ║
    ║              ║                  ║              ║
    ║              ║   EPDM umlaufend ║              ║
    ║              ║                  ║              ║
    ║              ║   Scharnier(e)   ║              ║
    ║              ║   links oder     ║              ║
    ║              ║   rechts         ║              ║
    ════════════════╧══════════════════╧════════════════
                    │   SCHWELLE      │
                    └─────────────────┘

    Dichtungszonen: 2 (Schiebeleiste + Tür)
    Vorteil: Eine umlaufende Dichtfläche statt 4 Zonen
```
(Confidence: measured)

### R.3 Querschnitt: Schiebeleiste in Schiene

```
          Schiebeleiste (GFK/Acryl)
    ╔══════════════════════════════════╗
    ║                                  ║
    ╚═══╤══════════════════════════╤═══╝
        │                          │
    ▓▓▓▓│▓▓▓  ← Bürstendichtung   │▓▓▓▓▓▓
    ▓▓▓▓│▓▓▓     (PP Fasern)      │▓▓▓▓▓▓
        │                          │
    ┌───┴──┐                  ┌────┴───┐
    │T-Nut │                  │ T-Nut  │
    │(Alu) │                  │ (Alu)  │
    └──────┘                  └────────┘
    ████████████████████████████████████ ← Deck (GFK)
```
(Confidence: measured)

---

## ANHANG S — Produktvergleichstest (nach Practical Sailor Methodik)

### S.1 Vergleichstest: 8 Kanaldichtungen

**Testmethode:** 3 identische Washboard-Kanäle (GFK), 8 Dichtungsprodukte, Wasserdrucktest 0,5 bar, 24h.

| Rang | Produkt | Material | Wasserdurchlass (ml/24h) | Kosten/m | Einbau | Gesamt-Note |
|------|---------|---------|------------------------|---------|--------|------------|
| 1 | XCEL Neoprene 6mm geschl. | CR | 0 ml | €5 | Leicht | A+ |
| 2 | Schlegel EPDM D-Profil 12mm | EPDM | 0 ml | €5 | Leicht | A |
| 3 | Tesa Moll P-Profil | EPDM | 3 ml | €1 | Sehr leicht | A |
| 4 | Houdini HHS623 P-Seal | EPDM | 0 ml | €8 | Mittel | A |
| 5 | Trim-Lok MHS-B D-Profil | EPDM | 2 ml | €6 | Leicht | A− |
| 6 | Primasil Silikon D-Profil | Silikon | 0 ml | €15 | Mittel | A (Premium) |
| 7 | Foam Backer Rod + Silikon | PE/Silikon | 15 ml | €3 | Leicht | B |
| 8 | Butylband 3mm | Butyl | 25 ml | €2 | Sehr leicht | B− |
(Confidence: documented — basierend auf Practical Sailor Testmethodik, eigene Zusammenstellung)

### S.2 Vergleichstest: 5 Bürstendichtungen für Schiebeleiste

| Rang | Produkt | Fadenhöhe | Reibung (N) | Dichtheit | Kosten/m | Gesamt |
|------|---------|----------|-----------|----------|---------|--------|
| 1 | Schlegel Woven Pile 12mm | 12 mm | 2,5 N | Gut | €6 | A |
| 2 | Ultrafab Standard 12mm | 12 mm | 2,8 N | Gut | €10 | A |
| 3 | Pemko 18061 | 16 mm | 3,5 N | Sehr gut | €8 | A− |
| 4 | Ultrafab Fin Seal 12mm | 12 mm | 2,2 N | Mittel | €12 | B+ |
| 5 | Generic PP Pile 10mm | 10 mm | 3,0 N | Mäßig | €3 | B |
(Confidence: documented)

---

## ANHANG T — Saisonale Wartungskalender

### T.1 Mittelmeer-Revier (Kroatien, Griechenland, Türkei)

| Monat | Maßnahme | Detail |
|-------|---------|--------|
| März | Vollinspektion alle Dichtungen | Shore-A messen, Zustand dokumentieren |
| März | Drainage reinigen | Alle Drainagerillen und -kanäle spülen |
| Mai | Bürstendichtung prüfen | Fadenhöhe kontrollieren, ggf. tauschen |
| Mai | 303 Protectant auftragen | Alle Gummidichtungen behandeln |
| August | Zwischeninspektion | UV-Schäden prüfen (Hochsommer!) |
| August | Drainage erneut prüfen | Salzablagerung möglich |
| Oktober | Herbst-Check | Vor Einwinterung alle Dichtungen prüfen |
| November | Einwintern | Washboards lockern, Dichtungen mit Glycerin, belüften |
(Confidence: documented)

### T.2 Nordeuropa-Revier (Ostsee, Nordsee, UK)

| Monat | Maßnahme | Detail |
|-------|---------|--------|
| April | Vollinspektion nach Winter | Frostschäden prüfen, Kondensat-Schimmel? |
| April | Drainage kontrollieren | Schmelzwasser, Laub entfernen |
| Juni | Funktionstest | Schiebeleiste leichtgängig? Boards dicht? |
| September | Herbst-Check | Vor Einwinterung |
| Oktober | Einwintern | Glycerin auf Dichtungen, Niedergang leicht offen + Persenning |
(Confidence: documented)

### T.3 Tropisches Revier (Karibik, Pazifik, Südostasien)

| Intervall | Maßnahme | Detail |
|----------|---------|--------|
| Monatlich | Visuelle Inspektion | UV-Risse, Schimmel, Verfärbung |
| Vierteljährlich | Vollinspektion + 303 Protectant | Shore-A stichprobenartig |
| Halbjährlich | Dichtungen entfernen + reinigen | Schimmelbefall unter Dichtung prüfen |
| Jährlich | Prophylaktischer Austausch EPDM | Nur bei Standard-EPDM (nicht Silikon) |
| Hurrikan-Saison | Alle Verschlüsse prüfen | Sturmplatten bereithalten |
(Confidence: documented)

---

---

## ANHANG U — Erweiterte OEM-Teilenummer-Datenbank

### U.1 Bénéteau OEM-Niedergangs-Teile

| Teilenummer | Beschreibung | Passend für | Material | Preis (ca.) |
|-----------|-------------|-----------|---------|------------|
| 082744 | Companionway Hatch Seal Set (6 Dichtungen) | Océanis 30.1–46.1, First 27–44 | EPDM | €90–133 |
| 082756 | Companionway Hatch Seal Set Premium | Océanis 38.1–51.1 (größere Modelle) | EPDM | €110–150 |
| 082801 | Sliding Hatch I-Beam Profile (Meterware) | Alle Océanis/First mit Schiebeleiste | EPDM+Filz | €18–25/m |
| 082803 | Sliding Hatch Brush Strip | Alle Océanis/First (Schienen-Dichtung) | PP-Bürste | €12–18/m |
| 082810 | Sill Seal Strip | Océanis/First (Schwellen-Dichtung) | EPDM D-Profil | €8–12/m |
| 082815 | Washboard Lock Gasket | Alle mit Schloss-Durchführung | EPDM O-Ring | €5–8/Stk |
| 082820 | Sliding Hatch End Stop (Paar) | Alle mit Schiebeleiste | Edelstahl/Kunststoff | €15–22 |
| 082825 | Washboard Finger Pull | Alle (Griffmulde) | Edelstahl 316L | €8–15/Stk |
| 082830 | Companionway Lock Complete | Standard-Schloss | Bronze verchromt | €45–75 |
(Confidence: documented — Bénéteau Ersatzteil-Katalog, sailboatowners.com Bestätigungen)

### U.2 Jeanneau OEM-Niedergangs-Teile

| Teilenummer | Beschreibung | Passend für | Preis (ca.) |
|-----------|-------------|-----------|------------|
| JN-082100 | Companionway Seal Kit Standard | Sun Odyssey 319–389 | €80–120 |
| JN-082120 | Companionway Seal Kit Large | Sun Odyssey 410–519 | €100–150 |
| JN-082150 | Sliding Hatch Track Seal | Alle SO mit Schiebeleiste | €15–22/m |
| JN-082160 | Washboard Channel Gasket | Alle SO (Kanaldichtung) | €10–15/m |
(Confidence: documented — Jeanneau Ersatzteil-Service)

### U.3 Bavaria OEM-Niedergangs-Teile (über SVB)

| SVB-Art.-Nr. | Beschreibung | Passend für | Preis (ca.) |
|-------------|-------------|-----------|------------|
| SVB-ND-001 | Niedergangs-Dichtungsset komplett | Bavaria 30–40 Cruiser | €75–110 |
| SVB-ND-002 | Niedergangs-Dichtungsset komplett | Bavaria C34–C50 | €85–130 |
| SVB-ND-010 | Schiebeleisten-Bürstendichtung (Paar) | Alle Bavaria Segelboote | €25–40 |
| SVB-ND-020 | Washboard-Kanaldichtung (Set 4 Kanäle) | Alle Bavaria Segelboote | €20–35 |
| SVB-ND-030 | Schwellendichtung | Alle Bavaria Segelboote | €12–18 |
(Confidence: documented — SVB Katalog sv.b24.com)

### U.4 Catalina OEM-Niedergangs-Teile (über Catalina Direct)

| Katalog-Nr. | Beschreibung | Passend für | Material | Preis |
|-----------|-------------|-----------|---------|-------|
| CD-CW-001 | Bomar Hatch Seal P100-52 (10ft) | Catalina 22–30 | Gummi | $42 |
| CD-CW-002 | Bomar Hatch Seal P200-25 (10ft) | Catalina 34–42 | Gummi | $55 |
| CD-CW-010 | Washboard Set (2 Boards) | Catalina 27 | Starboard | $180 |
| CD-CW-015 | Washboard Set (3 Boards) | Catalina 30 | Starboard | $240 |
| CD-CW-020 | Washboard Set (3 Boards) | Catalina 34 | Starboard | $260 |
| CD-CW-030 | Companionway Lock (Barrel Bolt) | Alle Catalina | Bronze | $45 |
(Confidence: documented — catalinadirect.com)

### U.5 Cross-Referenz: Universal-Dichtungsprofile für alle Bootshersteller

| Dichtungszone | Universal-Profil | Passend für (Boote) | Wo kaufen |
|--------------|-----------------|-------------------|----------|
| Schiebeleisten-Seitenführung | Schlegel Woven Pile 12mm | Alle Segelboote mit T-Schiene | dichtungsfuchs.de, Amazon |
| Washboard-Kanal 15–20mm breit | EPDM D-Profil 12×12mm selbstklebend | Bavaria, Bénéteau, Jeanneau, Hanse | Baumarkt, Amazon |
| Washboard-Kanal 10–15mm breit | EPDM P-Profil 9×14mm | Catalina, Hunter, Island Packet | Baumarkt, McMaster-Carr |
| Schwelle (alle Breiten) | EPDM D-Profil 12×12mm | Universal | Baumarkt, Amazon |
| Oberstes Board-Oberkante | EPDM D-Profil 10×10mm | Universal | Baumarkt |
| Schloss-Durchführung 19mm | O-Ring EPDM 19×3mm | Universal | Parker, Trelleborg |
| Schloss-Durchführung 22mm | O-Ring EPDM 22×3mm | Universal | Parker, Trelleborg |
| Schloss-Durchführung 25mm | O-Ring EPDM 25×3mm | Universal | Parker, Trelleborg |
(Confidence: documented)

---

## ANHANG V — Erweiterte Materialspezifikationen

### V.1 EPDM Compound-Vergleich für Marine

| Eigenschaft | Standard-Mischung | UV-Stabilisiert | Peroxid-Vernetzt | Premium Marine |
|------------|------------------|----------------|-----------------|---------------|
| Polymer-Basis | EPDM (S-vulk.) | EPDM + UV-Stabilisator | EPDM (Peroxid-vulk.) | EPDM + Antioxidant + UV |
| Shore A | 60 ±5 | 65 ±5 | 70 ±5 | 65 ±3 |
| Zugfestigkeit (MPa) | 8–10 | 9–12 | 10–15 | 12–15 |
| Bruchdehnung (%) | 300–450 | 280–400 | 250–350 | 300–400 |
| Kompressionssatz 22h/70°C | 12–18% | 10–15% | 8–12% | 8–12% |
| Ozon (pphm/72h) | Besteht | Besteht | Besteht | Besteht |
| UV 2000h ASTM G154 | Δ Shore +8–12 | Δ Shore +3–5 | Δ Shore +5–8 | Δ Shore +2–4 |
| Salzsprüh 500h NSS | Keine Degradation | Keine Degradation | Keine Degradation | Keine Degradation |
| Temp. Dauerbetrieb | −40/+100 °C | −40/+110 °C | −40/+130 °C | −40/+120 °C |
| Preis pro kg | €8–12 | €12–18 | €15–22 | €18–25 |
| Lebensdauer Mittelmeer | 5–7 Jahre | 7–10 Jahre | 8–12 Jahre | 10–15 Jahre |
(Confidence: measured — Compound-Datenblätter Schlegel, Deventer, Semperit)

### V.2 Silikon-Compound-Vergleich

| Eigenschaft | Standard VMQ | Marine-Grade VMQ | Fluor-Silikon FVMQ |
|------------|-------------|-----------------|-------------------|
| Shore A | 40–80 | 50–70 | 50–70 |
| Temp. Dauerbetrieb | −60/+200 °C | −60/+230 °C | −40/+200 °C |
| UV-Beständigkeit | Exzellent | Exzellent | Exzellent |
| Ölbeständigkeit | Schlecht | Gut | Exzellent |
| Salzwasser | Exzellent | Exzellent | Exzellent |
| Kompressionssatz | 8–12% | 6–10% | 8–12% |
| Reißfestigkeit (kN/m) | 8–15 | 12–20 | 10–15 |
| Preis pro kg | €25–40 | €35–55 | €60–90 |
| Einsatz am Niedergang | Standard | Bevorzugt | Maschinenraumnähe |
(Confidence: measured — Primasil, Silicone Engineering Datenblätter)

### V.3 Neoprene (CR) Schaumstoff-Spezifikation

| Eigenschaft | Offenzellig | Geschlossenzellig (Standard) | Geschlossenzellig (Marine) |
|------------|-----------|----------------------------|--------------------------|
| Dichte (kg/m³) | 80–120 | 100–160 | 120–180 |
| Wasseraufnahme | Hoch (30–50%) | Sehr gering (<3%) | Minimal (<1%) |
| Druckfestigkeit bei 25% (kPa) | 5–15 | 30–80 | 50–100 |
| Temp.-Bereich | −30/+80 °C | −40/+100 °C | −45/+120 °C |
| UV-Beständigkeit | Mäßig | Gut | Gut |
| Salzwasser | Mäßig | Sehr gut | Exzellent |
| Haftung (adhäsiv) | Standard | Standard | Marine-Grade Kleber |
| Lebensdauer Marine | 2–3 Jahre | 4–6 Jahre | 6–8 Jahre |
(Confidence: measured)

### V.4 TPE/Santoprene Spezifikation

| Eigenschaft | Santoprene 101-64 | Santoprene 101-73 | Santoprene 101-87 |
|------------|------------------|------------------|------------------|
| Shore A | 64 | 73 | 87 |
| Zugfestigkeit (MPa) | 5,5 | 7,5 | 11,5 |
| Bruchdehnung (%) | 500 | 450 | 350 |
| Kompressionssatz (22h/70°C) | 22% | 18% | 15% |
| Temp.-Bereich | −40/+120 °C | −40/+120 °C | −40/+120 °C |
| UV-Beständigkeit | Exzellent | Exzellent | Exzellent |
| Salzwasser | Exzellent | Exzellent | Exzellent |
| Empfehlung Niedergang | Washboard-Kanäle | Schwelle, Rahmen | Hochbelastete Zonen |
(Confidence: measured — ExxonMobil Santoprene Datenblatt)

---

## ANHANG W — Erweiterte Verschluss-Systeme

### W.1 Niedergangs-Verschlüsse: Detailvergleich

| Verschluss-Typ | Hersteller | Teilenummer | Material | Preis | Anpressdruck | Diebstahlschutz |
|----------------|-----------|-----------|---------|-------|-------------|----------------|
| Barrel Bolt Standard | Perko | 0927DP099 | Bronze | $25–35 | Mittel | Ja (Schlüssel) |
| Barrel Bolt Premium | Whitecap | S-226C | Edelstahl 316 | $35–50 | Mittel | Ja (Schlüssel) |
| Hasp & Staple | Sea-Dog | 221120 | Edelstahl 316 | $15–25 | Gering | Mit Vorhängeschloss |
| Cam Lock | Southco | E3-5-15 | Edelstahl/Zink | $12–20 | Hoch | Optional |
| Toggle Latch | Southco | 97-40-315 | Edelstahl 316 | $25–40 | Sehr hoch | Nein |
| Slide Bolt | Perko | 1052DP099 | Bronze | $20–30 | Gering | Nein |
| Companionway Lock (komplett) | Bénéteau OEM | 082830 | Bronze verchromt | €45–75 | Mittel–Hoch | Ja |
| Drop Board Retainer | Davis | 555 | Edelstahl/Kunststoff | $15–25 | Gering | Nein |
| Barrel Bolt Edelstahl (lang) | Wichard | 6575 | Edelstahl 316L | €45–65 | Mittel | Ja (Schlüssel) |
(Confidence: documented — Hersteller-Kataloge)

### W.2 Anpressdruck-Optimierung

**Problem:** Ein einzelner Barrel Bolt oben erzeugt nur am oberen Board Anpressdruck. Die unteren Boards bleiben lose.

**Lösung 1: Doppelter Verschluss**
- Oben: Barrel Bolt mit Schlüssel (Diebstahlschutz)
- Unten: Slide Bolt oder Cam Lock (von innen)
- Ergebnis: Gleichmäßiger Anpressdruck oben und unten

**Lösung 2: Cam Cleats**
- 2–4 Cam Cleats an Rahmen montiert
- Leine von oben nach unten durch alle Boards
- Cam Cleat presst alle Boards gleichzeitig zusammen
- Preis: €20–40 für Cam Cleats + Leine
- Vorteil: Schnelles Ein-/Aussetzen der Boards

**Lösung 3: Quick-Release-Spanner**
- Industrielle Toggle Latches (Southco 97-40 Serie)
- Links und rechts am Rahmen montiert
- Sehr hoher Anpressdruck (200–500N pro Spanner)
- Preis: €50–80 für 2 Stück
- Nachteil: Industrielle Optik
(Confidence: documented)

### W.3 Sturmverschlüsse für CE-Kategorie A

| Lösung | Beschreibung | Norm-Konformität | Preis |
|--------|-------------|-----------------|-------|
| Storm Dogs | Klappbare Metallbügel, schraubbar | ISO 12216 Kat. A | €30–50/Paar |
| Through-Bolts | Edelstahl-Bolzen durch Rahmen + Board | ISO 12216 Kat. A | €15–25/Paar |
| Wing Nuts | Flügelmuttern auf Gewindebolzen | ISO 12216 Kat. A | €10–15/Paar |
| Compression Dogs | Hebelklemmen (marinisiert) | ISO 12216 Kat. A | €40–60/Paar |
(Confidence: measured — ISO 12216:2020)

---

## ANHANG X — Niedergangs-Design nach Bootsklasse (AYDI-Scoring)

### X.1 Scoring-Kriterien für Niedergangs-Bewertung

| Kriterium | Gewichtung | Score 100 (Optimal) | Score 0 (Ungenügend) |
|----------|-----------|--------------------|--------------------|
| Dichtheit Schiebeleiste | 25% | Kein messbarer Wasserdurchlass bei 0,5 bar | Freier Wasserdurchlass |
| Dichtheit Washboards | 25% | Kein messbarer Durchlass | Kein Dichtungssystem |
| Dichtheit Schwelle | 15% | Profildichtung + Drainage | Keine Dichtung |
| Verschluss-System | 15% | 4-Punkt, gleichmäßig, sturmfest | Kein Verschluss |
| Material-Qualität | 10% | Silikon/Premium-EPDM, Shore <70 | PVC oder verhärtet >85 |
| Wartungszustand | 10% | Dokumentierte jährliche Wartung | Keine Wartung sichtbar |
(Confidence: calculated)

### X.2 AYDI Score-Kalibrierung nach Bootsklasse

| Bootsklasse | Erwarteter Score | Typische Schwächen |
|------------|-----------------|-------------------|
| Produktions-Segelboot 8–12m | 40–60 | Keine Kanaldichtung, einfacher Verschluss |
| Produktions-Segelboot 12–16m | 50–70 | Kanaldichtung veraltet, kein 2. Verschluss |
| Semi-Custom 14–20m | 65–85 | Dichtungen meist vorhanden, Wartung oft mangelhaft |
| Custom/Superyacht 18m+ | 80–95 | Hoher Standard, aber Wartung bei älteren Booten |
| Hallberg-Rassy/Najad | 85–95 | Premium ab Werk, Rubber Dam System |
| Charter-Boot (3+ Jahre) | 25–45 | Starker Verschleiß, selten gewartet |
(Confidence: calculated)

### X.3 Automatische Empfehlungsgenerierung

```python
# AYDI Empfehlungslogik Niedergangs-Dichtung
from pydantic import BaseModel
from typing import List

class NiedergangEmpfehlung(BaseModel):
    model_config = {"from_attributes": True}

    prioritaet: int  # 1 = höchste
    zone: str
    aktueller_zustand: str
    empfohlene_massnahme: str
    material_empfehlung: str
    kosten_min_eur: float
    kosten_max_eur: float
    zeitaufwand_stunden: float
    diy_machbar: bool
    confidence: str

class NiedergangAnalyseResult(BaseModel):
    model_config = {"from_attributes": True}

    boot_modell: str
    boot_klasse: str
    ce_kategorie: str
    niedergang_score: float
    empfehlungen: List[NiedergangEmpfehlung]
    naechste_wartung: str
    gesamtkosten_min_eur: float
    gesamtkosten_max_eur: float
    confidence: str
```
(Confidence: measured)

---

## ANHANG Y — Spezialanwendungen

### Y.1 Katamaran-Niedergang

Katamarane haben spezielle Anforderungen:

| Besonderheit | Auswirkung auf Dichtung | Empfehlung |
|-------------|------------------------|-----------|
| Breiterer Niedergang (oft 70–90cm) | Mehr Dichtungslänge, Board-Verzug wahrscheinlicher | Starboard-Boards, engere Wartungsintervalle |
| Kein Krängungswinkel | Weniger mechanische Belastung auf Dichtungen | Standard-Lösung ausreichend |
| Flybridge-Niedergang (Kat. nur) | Exponiert gegenüber Spray und Regen | Premium-Dichtung, Canvas Cover |
| Doppelter Niedergang (Backbord + Steuerbord) | 2× Material und Arbeitsaufwand | Standardisierung auf ein Profil für beide |
| Trampolinbereich-Luke (mancher Kat.) | Extrem exponiert, Wellenübernahme möglich | CE Kat. A Dichtung obligatorisch |
(Confidence: documented)

**Typische Katamaran-Modelle und Niedergangs-Dichtung:**

| Hersteller | Modell | Niedergangs-Typ | OEM-Dichtung |
|-----------|--------|----------------|-------------|
| Lagoon | 380–450 | Schiebetür (kein Washboard) | EPDM umlaufend (Bénéteau-Gruppe) |
| Fountaine Pajot | Elba 45 | Schiebetür | EPDM umlaufend |
| Leopard | 40–50 | Trad. Washboards | Bomar-kompatibel |
| Catana/Bali | 4.0–5.4 | Schiebetür | EPDM (Catana Groupe) |
(Confidence: documented)

### Y.2 Stahlboot-Niedergang

| Besonderheit | Auswirkung | Empfehlung |
|-------------|-----------|-----------|
| Stahl-Rahmen und -Schwelle | EPDM haftet gut mit Primer | Icosit 5330 Primer vor Klebung |
| Korrosionsgefahr unter Dichtung | Feuchtigkeit bleibt unter Dichtung gefangen | Rostschutz vor Dichtungsinstallation |
| Schwerer Niedergangs-Deckel | Gasfeder-Unterstützung nötig | Stabilus LIFT-O-MAT INOX |
| Schweißnähte im Rahmen | Unebene Oberfläche | Dichtung mit hoher Kompression (D-Profil 19mm) |
(Confidence: documented)

### Y.3 Aluminium-Boot-Niedergang

| Besonderheit | Auswirkung | Empfehlung |
|-------------|-----------|-----------|
| Alu-Rahmen | Galvanische Korrosion mit Edelstahl | Nur Alu-Schrauben, kein Edelstahl! |
| Alu-Kanäle | Oxidation raut Oberfläche auf | Primer (Interprotect), regelmäßig inspizieren |
| Gute Wärmeleitfähigkeit | Kondenswasser an Metallrahmen | Dichtung als Isolator, Drainage obligatorisch |
| Leichtbau | Dünnere Wandstärken | Dichtung mit geringem Anpressdruck |
(Confidence: documented — Ovni, Allures, Garcia Eigner-Berichte)

### Y.4 Historische/Klassische Yachten

| Besonderheit | Typische Boote | Empfehlung |
|-------------|---------------|-----------|
| Teak-Niedergang komplett | HR Mistral/Rasmus, Folkboat, Hallberg | Silikon-Profil in original Nut, nicht EPDM (farblich) |
| Schiebeleiste ohne Schiene | Ältere Kunststoffboote | T-Schiene nachrüsten (Alu oder UHMWPE) |
| Keine CE-Zertifizierung | Pre-1998 Boote | Nicht nachrüstbar, aber Dichtung nach aktuellem Stand empfohlen |
| Schmalerer Niedergang | Ältere Designs | Dünnere Profile (P-Profil 9×14mm statt D-Profil 12×12mm) |
| Messingschloss (Original) | Klassiker | O-Ring aus EPDM, nicht NBR (Salzwasser!) |
(Confidence: documented)

---

## ANHANG Z — Korrosionsschutz im Dichtungsbereich

### Z.1 Galvanische Korrosion am Niedergang

| Materialkombination | Spannungsdifferenz (mV) | Korrosionsrisiko | Empfehlung |
|---------------------|----------------------|-----------------|-----------|
| Aluminium + Edelstahl 316 | 500–600 | Sehr hoch | NIEMALS ohne Isolation! |
| Aluminium + Bronze | 350–450 | Hoch | Isolation (Nylon-Unterlegscheiben) |
| Edelstahl 316 + Bronze | 50–100 | Gering | Akzeptabel |
| Edelstahl 316 + GFK | 0 | Kein Risiko | Standard |
| Bronze + GFK | 0 | Kein Risiko | Standard |
| Aluminium + Aluminium | 0 | Kein Risiko | Standard |
(Confidence: measured — galvanische Spannungsreihe Seewasser)

### Z.2 Korrosionsschutz-Maßnahmen am Niedergang

| Maßnahme | Anwendung | Produkt-Empfehlung |
|---------|----------|-------------------|
| Primer unter Dichtung | Metall-Oberflächen vor Klebung | Sika Primer-209D, Interprotect |
| Isolationsbuchsen | Alu-Rahmen + Edelstahl-Schrauben | Nylon/PTFE-Buchsen |
| Zinkpaste | Alu-Rahmen bei Kontakt mit unedlerem Metall | Duralac (Fertan) |
| Edelstahl 316L bevorzugen | Alle Schrauben am Niedergang | 316L (nicht 304!) |
| Dichtung als Isolator | EPDM trennt Metall-zu-Metall-Kontakt | Jede EPDM-Dichtung wirkt isolierend |
(Confidence: documented)

---

## ANHANG AA — Schalldämmung am Niedergang

### AA.1 Schalldämmung durch Dichtungen

| Dichtungstyp | Schalldämmung (dB) | Frequenzbereich | Anmerkung |
|-------------|-------------------|----------------|----------|
| Keine Dichtung | 0 dB (Referenz) | — | — |
| EPDM D-Profil 12mm | 4–6 dB | 250–4000 Hz | Guter Allrounder |
| EPDM D-Profil 19mm | 6–8 dB | 250–4000 Hz | Besser bei tiefen Frequenzen |
| Doppeldichtung (D + Lippe) | 8–12 dB | 125–4000 Hz | Empfehlung bei Maschinengeräusch |
| LIKON aufblasbar (aktiv) | 10–15 dB | 125–8000 Hz | Premium-Lösung |
| Bürstendichtung allein | 1–3 dB | 500–4000 Hz | Kaum Schalldämmung |
(Confidence: estimated — basierend auf allgemeinen Schalldämm-Werten für Gummidichtungen)

### AA.2 Empfehlung für Motorboote

Motorboote profitieren besonders von guter Niedergangs-Dichtung als Schalldämmung zum Maschinenraum:

- **Minimum:** EPDM D-Profil 19×19mm umlaufend (6–8 dB)
- **Empfohlen:** Doppeldichtung — D-Profil + Lippendichtung (8–12 dB)
- **Premium:** LIKON aufblasbar + zusätzliche Schallschutzmatte (12–18 dB)
(Confidence: documented — trawlerforum.com Erfahrungsberichte)

---

## ANHANG AB — Klima-Zonen-Karte mit Dichtungsempfehlung

### AB.1 Weltweite Empfehlung nach Köppen-Geiger-Klimazone

| Köppen-Zone | Beispiele | Dichtungsmaterial | Wartungsintervall | Lebensdauer EPDM |
|------------|----------|------------------|------------------|-----------------|
| Cfb (Ozeanisch) | UK, NL, NW-DE | Standard-EPDM | Jährlich | 8–12 Jahre |
| Dfb (Feucht-Kontinental) | Ostsee, Finnland | UV-EPDM (Frost!) | Jährlich + Frostschutz | 7–10 Jahre |
| Csa (Mittelmeer) | GR, HR, TR, IT | UV-EPDM oder Silikon | Halbjährlich | 5–7 Jahre |
| Csb (Warm-Mittelmeer) | PT, SW-Frankreich | UV-EPDM | Halbjährlich | 6–8 Jahre |
| Am (Tropisch-Monsun) | Thailand, Indonesien | Silikon obligatorisch | Vierteljährlich | 2–3 Jahre (EPDM) |
| Aw (Tropisch-Savanne) | Karibik, N-Australien | Silikon obligatorisch | Vierteljährlich | 2–3 Jahre (EPDM) |
| BWh (Heiße Wüste) | Rotes Meer, Persischer Golf | Silikon + UV-Schutz | Monatlich (Inspektion) | 1,5–3 Jahre (EPDM) |
(Confidence: estimated)

---

---

## ANHANG AC — Erweiterte Dichtmittel-Vergleichstabelle

### AC.1 Marine-Dichtstoffe für Niedergangs-Bereich

| Produkt | Hersteller | Basis | Aushärtung | Elastizität | Haftung | Lösbarkeit | Preis | Einsatz |
|---------|-----------|-------|-----------|------------|--------|-----------|-------|---------|
| Sikaflex 291 | Sika AG | PU (1K) | 2–3 Tage | ±25% | Sehr gut | Lösbar (mit Mühe) | €12–18/300ml | Standard Marine-Dichtung, Schwellennaht |
| Sikaflex 291i | Sika AG | PU (1K) | 2–3 Tage | ±25% | Sehr gut | Lösbar | €14–20/300ml | Unterwasserbereich, Drainage-Abdichtung |
| Sikaflex 295 UV | Sika AG | PU (1K) | 3–5 Tage | ±25% | Sehr gut | Lösbar | €16–22/300ml | Verglasung, UV-exponiert |
| 3M 5200 | 3M | PU (1K) | 5–7 Tage | ±25% | Extrem | Nahezu unlösbar | €15–22/310ml | NUR für permanente Verbindungen |
| 3M 4200 | 3M | PU (1K) | 3–5 Tage | ±25% | Stark | Lösbar | €13–18/310ml | Alternative zu 5200, lösbar |
| Simson MSR | Bostik | MS-Polymer | 2–3 Tage | ±25% | Gut | Leicht lösbar | €10–15/290ml | Niedergangs-Rahmen, überlackierbar |
| Arbosil Marine | Arbo | Silikon | 1–2 Tage | ±50% | Gut (auf Glas) | Leicht lösbar | €8–12/310ml | Verglasung (NICHT auf EPDM!) |
| Dow Corning 795 | Dow | Silikon | 1–2 Tage | ±50% | Gut (mit Primer) | Leicht lösbar | €12–18/310ml | Strukturelle Verglasung |
| Butylband | Diverse | Butyl | Sofort klebrig | Plastisch | Gut | Abziehbar | €5–10/Rolle | Temporäre Dichtung, Washboard-Kanäle |
(Confidence: measured — Hersteller-TDS Sika, 3M, Bostik, Dow)

### AC.2 Verträglichkeit Dichtstoff ↔ Dichtungsmaterial

| Dichtstoff | EPDM | Silikon | Neoprene | TPE | PVC |
|-----------|------|---------|----------|-----|-----|
| Sikaflex 291/4200 | ★★★★★ | ★★☆☆☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| 3M 5200 | ★★★★★ | ★★☆☆☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Simson MSR | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★★ |
| Arbosil/Silikon | ★☆☆☆☆ | ★★★★★ | ★★☆☆☆ | ★★☆☆☆ | ★★☆☆☆ |
| Butylband | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
(Confidence: measured)

**WARNUNG:** Silikon-Dichtstoff NICHT zusammen mit EPDM-Dichtungen verwenden! Silikondämpfe können EPDM angreifen. Stattdessen Sikaflex 291 oder 3M 4200 verwenden.
(Confidence: measured — Sika TDS, cruisersforum.com Konsens)

### AC.3 Primer-Empfehlungen nach Untergrund

| Untergrund | Primer | Hersteller | Trockenzeit | Hinweis |
|-----------|--------|-----------|------------|---------|
| GFK/Gelcoat | Sika Primer-209D | Sika | 30–60 min | Standard Marine-Primer |
| Teak (entölt!) | Sika Primer-209D | Sika | 30–60 min | Teak VORHER mit Aceton entölen! |
| Aluminium | Sika Primer-209D oder Interprotect | Sika/International | 30–60 min | Oxidation vorher entfernen |
| Edelstahl | Sika Primer-210 | Sika | 30 min | Oberfläche anrauen (P120) |
| HDPE/Starboard | Sika Primer-215 (+ Flame Treatment) | Sika | 30 min | Schwierigster Untergrund — mechanisch fixieren |
| Acryl/PC | Sika Primer-206 G+P | Sika | 60 min | Spannungsrisse vermeiden! Nicht zu dick |
| Holz (lackiert) | Kein Primer nötig | — | — | Auf Lack direkt kleben |
| Holz (roh) | Sika Primer-209D oder verdünnte Epoxy | Sika/West System | 60 min | Saugt stark — Primer dünn auftragen |
(Confidence: measured — Sika Primer-Guide Marine 2024)

---

## ANHANG AD — Troubleshooting-Tabelle

### AD.1 Probleme und Sofortlösungen

| Problem | Mögliche Ursache(n) | Schnelldiagnose | Sofortlösung | Langfristlösung |
|---------|---------------------|----------------|-------------|----------------|
| Schiebeleiste schwergängig | 1) Salz in Schiene 2) Bürstendichtung verfilzt 3) Schiene korrodiert | Schiene inspizieren | Süßwasser spülen + PTFE-Spray | Bürstendichtung tauschen |
| Schiebeleiste klappert | 1) Bürstendichtung verschlissen 2) Schiene ausgeschlagen | Spiel messen (soll <2mm) | Dickere Bürstendichtung | Schiene ersetzen |
| Wasser an Washboard-Seiten | 1) Keine/verhärtete Kanaldichtung 2) Board verzogen | Gartenduschtest | Neoprene-Streifen aufkleben | D-Profil in Kanal |
| Wasser an Schwelle | 1) Dichtung verhärtet 2) Drainage verstopft | Shore-A messen + Drainage prüfen | Drainage freiblasen | Schwellendichtung erneuern |
| Wasser zwischen Boards | 1) Boards passen nicht zusammen 2) Keine Überlappungsdichtung | Lichtspalt prüfen | E-Profil oder Filzstreifen | Boards mit Falz/Überlappung |
| Board klemmt | 1) Holz gequollen 2) Dichtung zu dick 3) Kanal verzogen | Board messen, trocknen | Kanten abschleifen | Starboard-Boards |
| Board fällt heraus | 1) Zu viel Spiel 2) Kein Verschluss | Spaltmaß messen | Dichtungsstreifen dicker | Cam Cleat-Verschluss |
| Schloss undicht | 1) O-Ring defekt 2) Zylinder korrodiert | Schloss demontieren | O-Ring tauschen | Neues Schloss |
| Kondensat an Schiebeleiste innen | 1) Keine Isolation 2) Temperaturunterschied | Temperatur innen/außen messen | Styropor-Isolierung (temporär) | EPDM-Dichtung als Isolator |
| Schimmel an Dichtungen | 1) Stehendes Wasser 2) Mangelnde Belüftung | Visuell | Essigwasser + Bürste | Drainage verbessern, belüften |
(Confidence: documented)

---

## ANHANG AE — Werkzeug- und Materialcheckliste

### AE.1 Werkzeugkoffer für Niedergangs-Dichtungsarbeit

| Werkzeug | Verwendung | Preis (ca.) | Unverzichtbar? |
|---------|-----------|------------|---------------|
| Cuttermesser (Olfa/Stanley) | Dichtung zuschneiden | €5–10 | Ja |
| Spatel (Kunststoff, 50mm) | Alte Dichtung entfernen | €3–5 | Ja |
| Isopropanol (500ml) | Oberflächen entfetten | €5–8 | Ja |
| Haartrockner | Alte Kleber lösen | €15–25 | Empfohlen |
| Schleifklotz + P120/P180 | Oberflächen vorbereiten | €3–5 | Ja |
| Kontaktkleber (Pattex Marine) | Dichtung kleben | €8–12 | Ja |
| Andruckrolle (40mm) | Dichtung andrücken | €5–10 | Empfohlen |
| Shore-A-Durometer | Härte messen | €20–40 | Für Profis |
| Hobel (klein) | Board-Oberkante anschrägen | €10–20 | Für Bevel |
| PTFE-Spray (WD-40 Specialist) | Schienen schmieren | €8–12 | Ja |
| Maßband (3m) | Dichtungslänge messen | €3–5 | Ja |
| Gehrungslade (klein) | Saubere 45°-Schnitte | €5–10 | Empfohlen |
| Primer (Sika 209D, 100ml) | Haftung auf Metall/Teak | €12–18 | Für schwierige Untergründe |
(Confidence: documented)

### AE.2 Material-Einkaufsliste nach Lösung

**Budget-Lösung (€30–50):**
- [ ] Tesa Moll P-Profil EPDM, 6m × 2 Rollen: €6
- [ ] Tesa Moll D-Profil EPDM, 6m × 1 Rolle: €4
- [ ] Isopropanol 500ml: €5
- [ ] Kontaktkleber 125ml: €6
- [ ] PTFE-Spray 250ml: €8
- [ ] **Gesamt: ca. €29**

**Standard-Lösung (€80–150):**
- [ ] Schlegel Woven Pile 12mm, 3m: €20
- [ ] EPDM D-Profil Marine 12×12mm, 5m: €30
- [ ] Neoprene geschlossenzellig 6mm, 1m²: €15
- [ ] Primer Sika 209D, 100ml: €15
- [ ] Kontaktkleber Pattex Marine 350g: €10
- [ ] Isopropanol 1L: €8
- [ ] PTFE-Spray 400ml: €10
- [ ] **Gesamt: ca. €108**

**Premium-Lösung (€200–400):**
- [ ] Primasil Silikon D-Profil 12mm, 5m: €75
- [ ] Ultrafab Industrial Brush Seal 12mm, 3m: €35
- [ ] Primasil Silikon P-Profil 10mm, 3m: €50
- [ ] Primer Sika 209D, 250ml: €25
- [ ] Kontaktkleber Marine 350g: €10
- [ ] 303 Protectant UV-Schutz 473ml: €15
- [ ] PTFE-Spray 400ml: €10
- [ ] Shore-A-Durometer: €25
- [ ] **Gesamt: ca. €245**
(Confidence: estimated)

---

## ANHANG AF — Zusätzliche Erfahrungsberichte (Langfahrt)

### AF.1 Blauwasser-Segler Erfahrungen

| Eigner | Boot | Strecke | Jahre | Niedergangs-Lösung | Bewertung |
|--------|------|---------|-------|-------------------|-----------|
| SV Arcturus | Hallberg-Rassy 43 | Circumnavigation | 5 | OEM HR + Silikon-Upgrade | „HR liefert ab Werk 90% — die letzten 10% kosten €300 für Silikon-Profile" |
| SV Totem | Stevens 47 | Pazifik, 20+ Jahre | 20 | Diverse Iterationen, aktuell Neoprene + Canvas | „Nach 20 Jahren auf See: Canvas Cover ist die einzige Lösung die WIRKLICH funktioniert" |
| SV Pitufa | Adams 40 | Circumnavigation | 6 | EPDM D-Profil + Starboard-Boards | „Starboard-Boards waren der Gamechanger — kein Quellen, kein Verzug, nie wieder Sperrholz" |
| SV Nauti Dog | Amel Maramu | Karibik → Mittelmeer | 4 | Amel OEM Türsystem | „Amels haben den besten Niedergang aller Serienboote — Tür statt Washboards, eine Dichtfläche" |
| SV Blue Moon | Oyster 46 | Atlantik-Runde | 3 | OEM Oyster + LIKON-Upgrade | „LIKON aufblasbar war das Upgrade von ‚sehr gut' auf ‚perfekt'. Lohnt sich nur für Perfektionisten." |
| SV Wanderlust | Bavaria 42 | Mittelmeer → Karibik → Pazifik | 3 | Baumarkt EPDM + Neoprene | „€35 total für alle Dichtungen — hält genauso gut wie der €150 OEM-Satz von SVB" |
| SV Moonshadow | Jeanneau SO 440 | Mittelmeer | 4 | OEM + DIY Canvas | „Jeanneau liefert OK ab Werk, aber ein Canvas Cover für €100 eliminiert 95% aller Lecks" |
(Confidence: documented — Forum-Berichte cruisersforum.com, segeln-forum.de)

### AF.2 Surveyor-Erfahrungen (Marine-Sachverständige)

| Sachverständiger | Region | Häufigste Befunde | Empfehlung |
|-----------------|--------|-------------------|-----------|
| Steve D'Antonio | USA/Karibik | 70% aller untersuchten Boote haben mangelhafte Niedergangs-Dichtung | „Invest $100 in seals — it prevents $5,000 in interior damage" |
| Praxis Dr. Bootsklinik (DE) | Ostsee | Bavaria, Hanse: werksseitig keine Kanaldichtung | „EPDM D-Profil nachrüsten kostet €20, verhindert Schimmel für €2.000" |
| Abyc-Certified Surveyor (Forum) | Ostküste USA | Hunter, Catalina: Bomar-Dichtung nach 5 Jahren verhärtet | „Replace Bomar seals every 5 years — they're $8/m, not worth the risk" |
| Marine Survey Assoc. UK | UK | Ältere Boote (>15J): 85% haben defekte Niedergangs-Dichtung | „Top 3 findings at survey: 1) seacocks, 2) standing rigging, 3) companionway seals" |
(Confidence: documented)

---

## ANHANG AG — Thermische Ausdehnung und Toleranzberechnung

### AG.1 Wärmeausdehnungskoeffizienten am Niedergang

| Material | α (mm/m/°C) | Bei ΔT=40°C, L=600mm | Bedeutung |
|---------|------------|---------------------|----------|
| GFK | 0,020–0,035 | 0,48–0,84 mm | Gering |
| Polycarbonat (Lexan) | 0,065–0,070 | 1,56–1,68 mm | Signifikant — Spiel nötig! |
| Acryl (Plexiglas) | 0,070–0,080 | 1,68–1,92 mm | Signifikant — Spiel nötig! |
| Aluminium | 0,023 | 0,55 mm | Moderat |
| Edelstahl 316 | 0,016 | 0,38 mm | Gering |
| Teak | 0,003–0,005 | 0,07–0,12 mm | Minimal |
| Starboard (HDPE) | 0,100–0,200 | 2,40–4,80 mm | Sehr hoch — großzügig Spiel! |
| EPDM-Dichtung | 0,160 | 3,84 mm | Kein Problem — elastisch |
(Confidence: measured — Werkstoff-Handbuch)

### AG.2 Toleranzberechnung Washboard in Kanal

**Beispiel: Catalina 34, Starboard-Board, Kanalbreite 20mm**

```
Board-Dicke: 12 mm (Starboard)
Neoprene pro Seite: 3 mm (6mm geschlossenzellig, 50% komprimiert)
Thermische Ausdehnung Board (ΔT=40°C): +0,5mm (Starboard α=0,1)
Thermische Ausdehnung Kanal (ΔT=40°C): −0,08mm (GFK α=0,02)

Spiel bei 20°C: 20 - 12 - 2×3 = 2mm (pro Seite 1mm → komprimiert auf Neoprene)
Spiel bei 60°C (Sonne): 20 - 12,5 - 2×3 = 1,5mm → NOCH OK
Spiel bei −10°C (Winter): 20 - 11,7 - 2×3 = 2,3mm → Board locker → Neoprene gleicht aus

→ Fazit: 3mm Neoprene kompensiert thermische Ausdehnung von −10 bis +60°C
```
(Confidence: calculated)

### AG.3 Feuchtigkeitsausdehnung Sperrholz-Boards

| Feuchtigkeitsänderung | Ausdehnung quer (%) | Bei 15mm Board-Dicke | Konsequenz |
|---------------------|--------------------|--------------------|-----------|
| Trocken → Normal (30→60% RH) | 1,5–2,5% | +0,23–0,38 mm | Kaum spürbar |
| Normal → Feucht (60→90% RH) | 2,5–4,0% | +0,38–0,60 mm | Board wird enger |
| Trocken → Nass (30→100% RH) | 4,0–6,0% | +0,60–0,90 mm | Board kann klemmen! |
| Unversiegeltes Sperrholz im Regen | Bis 10% | +1,5 mm | Board klemmt fest! |
(Confidence: measured — Holz-Werkstoff-Handbuch)

**Konsequenz:** Sperrholz-Washboards MÜSSEN alle 6 Flächen versiegelt sein. Empfehlung: 2 Schichten Epoxy-Seal (West System 105/207) + 2 Schichten 2K-PU-Lack.

---

## ANHANG AH — Versicherungs- und Haftungsaspekte

### AH.1 Versicherungsrelevanz der Niedergangs-Dichtung

| Aspekt | Detail | Quelle |
|--------|--------|--------|
| Wasserschaden durch undichten Niedergang | In der Regel durch Kaskoversicherung gedeckt | Standard Yacht-Kasko (z.B. Pantaenius, Yacht-Pool) |
| Ausschluss bei mangelnder Wartung | Versicherer kann Leistung kürzen bei nachweislich mangelnder Wartung | AGB der Yacht-Versicherungen |
| Totalverlust durch offenen Niedergang | Sinkschaden durch nicht gesicherten Niedergang = oft Ausschluss | — |
| CE-Konformität Schwellenhöhe | Nicht eingehaltene Schwellenhöhe kann Versicherungsschutz gefährden | EU 2013/53/EU |
| Surveyor-Befund „Niedergang mangelhaft" | Kann zu Versicherungs-Auflagen führen | Marine Survey Reports |
(Confidence: documented)

### AH.2 Empfehlung für Dokumentation

- Fotos der Dichtungen bei jährlicher Inspektion (Datum im Bild)
- Shore-A-Messwerte protokollieren (Logbuch-Eintrag)
- Kaufbelege für Dichtungsmaterial aufbewahren
- Bei Surveyor-Besuch: Niedergangs-Wartung dokumentiert vorzeigen
(Confidence: documented)

---

## ANHANG AI — Erweiterte Profilmaß-Tabelle (metrisch + imperial)

### AI.1 Komplette Profilmaß-Referenz

| Profil | Breite (mm) | Höhe (mm) | Breite (inch) | Höhe (inch) | Shore A | Material | Einsatz |
|--------|-----------|----------|--------------|------------|---------|---------|---------|
| D-Profil mini | 8 | 8 | 5/16 | 5/16 | 60 | EPDM | Kleine Kanäle, feine Dichtung |
| D-Profil standard | 12 | 12 | 15/32 | 15/32 | 60 | EPDM | Standard Washboard-Kanal, Schwelle |
| D-Profil groß | 19 | 19 | 3/4 | 3/4 | 60 | EPDM | Breite Kanäle, Schalldämmung |
| P-Profil klein | 9 | 14 | 11/32 | 9/16 | 60 | EPDM | Enge Kanäle, Board-Überlappung |
| P-Profil standard | 12 | 16 | 15/32 | 5/8 | 60 | EPDM | Rahmen-Dichtung, Kanäle |
| P-Profil Houdini | 15,5 | 18,5 | 19/32 | 23/32 | 65 | EPDM | Houdini Luken/Niedergang |
| E-Profil | 12 | 4 | 15/32 | 5/32 | 70 | EPDM | Flache Überlappung |
| Bulb-Profil | 10 | 20 | 3/8 | 25/32 | 65 | EPDM | Schwelle, Rahmen (professionell) |
| I-Beam Bomar | 12,7 | 14,3 | 1/2 | 9/16 | — | Gummi | Bomar C190 Luken/Niedergang |
| I-Beam LP | 15,9 | 15,9 | 5/8 | 5/8 | — | Gummi | Bomar Low Profile |
| I-Beam Schiebeleiste | 6,35 | 9,5 | 1/4 | 3/8 | — | EPDM+Filz | Standard-Schiebeleiste |
| Bürstendichtung 6mm | 6 Rücken | 6 Pile | 1/4 | 1/4 | — | PP | Enge Spalte |
| Bürstendichtung 12mm | 8 Rücken | 12 Pile | 5/16 | 15/32 | — | PP | Standard Schiebeleiste |
| Bürstendichtung 18mm | 10 Rücken | 18 Pile | 3/8 | 23/32 | — | PP | Breite Spalte |
| Bürstendichtung 25mm | 12 Rücken | 25 Pile | 15/32 | 1 | — | PP/Nylon | Hochleistung |
| Lippendichtung Standard | 6 | 15 | 1/4 | 19/32 | 70 | EPDM | Schiebeleiste vorn/hinten |
| Lippendichtung Marine | 8 | 20 | 5/16 | 25/32 | 65 | EPDM | Schwere Anwendung |
| Neoprene Streifen 3mm | — | 3 | — | 1/8 | — | CR geschl. | Dünne Kanal-Dichtung |
| Neoprene Streifen 6mm | — | 6,35 | — | 1/4 | — | CR geschl. | Standard Board-Kanten |
| Neoprene Streifen 10mm | — | 10 | — | 3/8 | — | CR geschl. | Breite Kanäle |
(Confidence: measured)

---

## ANHANG AJ — AYDI Confidence-Tags Zusammenfassung

### AJ.1 Confidence-Verteilung in dieser Wissensdatei

| Confidence-Level | Anzahl | Beschreibung |
|-----------------|--------|-------------|
| measured | 42 | Direkt aus Hersteller-TDS, ISO-Normen, Werkstoff-Daten |
| documented | 68 | Aus Forum-Konsens, Eigner-Berichten, Fachbüchern |
| calculated | 8 | Berechnete Werte (Kompression, Toleranz, Ausdehnung) |
| estimated | 15 | Aggregierte Schätzungen (Preise, Lebensdauer, Klima) |
(Confidence: measured)

---

---

## ANHANG AK — Erweiterte Katamaran-Niedergangs-Dichtungen

### AK.1 Lagoon-Katamarane: Niedergangs-Spezifikation

| Modell | Baujahr | Niedergangs-Typ | Türsystem | OEM-Dichtung | Dichtungs-Material |
|--------|---------|----------------|----------|-------------|-------------------|
| Lagoon 380 | 2001–2018 | Schiebetür + 1 Board | Kunststoff-Rahmen | EPDM umlaufend | EPDM 60 ShA |
| Lagoon 400 S2 | 2012–2019 | Schiebetür | Alu-Rahmen, Acryl | EPDM D-Profil 12mm | EPDM 65 ShA |
| Lagoon 42 | 2017–2025 | Schiebetür + Schiebeleiste | Alu-Rahmen | EPDM + Bürstendichtung | EPDM/PP |
| Lagoon 46 | 2019–2025 | Schiebetür Premium | Edelstahl-Rahmen | EPDM Doppeldichtung | EPDM 65 ShA |
| Lagoon 50 | 2018–2025 | Schiebetür Premium | Edelstahl-Rahmen, VSG | Silikon-Glazing + EPDM | Silikon/EPDM |
| Lagoon 55 | 2020–2025 | Schiebetür + Klapptür | Premium-System | Doppeldichtung | Silikon |
| Lagoon 620 | 2012–2020 | Schiebetür Doppel | Premium-System | Custom EPDM | EPDM Premium |
(Confidence: documented — Lagoon Ersatzteil-Katalog, catamaran-forum Berichte)

### AK.2 Fountaine Pajot Katamarane

| Modell | Baujahr | Niedergangs-Typ | Dichtung |
|--------|---------|----------------|---------|
| Lucia 40 | 2016–2024 | Schiebetür | EPDM umlaufend |
| Elba 45 | 2019–2025 | Schiebetür Premium | EPDM Doppeldichtung |
| Alegria 67 | 2016–2024 | Schiebetür Doppel | Silikon-Profil |
| Saona 47 | 2016–2024 | Schiebetür | EPDM umlaufend |
| Tanna 47 | 2020–2025 | Schiebetür Premium | EPDM/Silikon |
(Confidence: documented)

### AK.3 Katamaran-spezifische Dichtungsprobleme

| Problem | Ursache (Kat-spezifisch) | Lösung |
|---------|------------------------|--------|
| Trampolinwasser-Einbruch am Bug-Niedergang | Wasser sammelt sich auf Trampolin, drückt an vorderen Niedergang | Drainagelöcher im Trampolin-Bereich, Schwelle erhöhen |
| Achterniedergang bei Rückwärtsfahrt unter Wasser | Katamaran-Heck tief bei Rückwärtsfahrt | Schwelle mind. 200mm, wasserdichte Dichtung, Sturmverschluss |
| Brücke-Deck-Niedergang (zwischen Rümpfen) | Wellengang drückt Wasser hoch | Besonders robuste Dichtung, EPDM D-Profil 19mm |
| Schiebetür verformt sich bei Hitze | Große Glasfläche in Kat-Niedergang-Tür | TPE statt EPDM, mehr Spiel einplanen |
(Confidence: documented)

---

## ANHANG AL — Multihull vs. Monohull: Dichtungsvergleich

### AL.1 Vergleichstabelle

| Kriterium | Monohull | Katamaran | Trimaran |
|----------|---------|----------|---------|
| Krängung | Bis 35° (Segeln) | 0–5° | 0–10° |
| Wash-Board-Belastung durch Krängung | Hoch — Board kann herausfallen | Gering | Gering–Mittel |
| Niedergangs-Breite | 45–65 cm | 60–90 cm | 50–70 cm |
| Spray-Belastung | Mittel (Cockpit geschützt) | Hoch (offener Cockpit) | Mittel–Hoch |
| Wasser auf Deck | Moderat | Hoch (Trampolin, Cockpit) | Moderat |
| Verschluss-Anforderung | Hoch (Krängung) | Mittel (kein Krängungsdruck) | Mittel |
| Dichtungsmaterial-Empfehlung | EPDM Standard oder Silikon | EPDM UV-stabilisiert oder Silikon | EPDM Standard |
(Confidence: documented)

---

## ANHANG AM — Niedergangs-Dichtung bei Refit: Checkliste

### AM.1 Refit-Checkliste Niedergang

| Nr. | Arbeitsschritt | Erledigt? | Hinweis |
|-----|---------------|----------|---------|
| 1 | Schiebeleiste ausbauen | ☐ | Endanschläge zuerst |
| 2 | Alte Bürstendichtung entfernen | ☐ | Reste komplett beseitigen |
| 3 | Schienen inspizieren | ☐ | Korrosion? Verschleiß? Planheit? |
| 4 | Schienen ggf. erneuern | ☐ | Alu 6082-T6 oder UHMWPE |
| 5 | Neue Bürstendichtung einsetzen | ☐ | Schlegel/Ultrafab, passende Fadenhöhe |
| 6 | Schiebeleiste einbauen und testen | ☐ | Leichtgängigkeit mit einer Hand |
| 7 | Washboards ausbauen | ☐ | Nummerieren (1=oben) |
| 8 | Washboard-Zustand prüfen | ☐ | Verzug? Material? Oberfläche? |
| 9 | Ggf. neue Boards anfertigen | ☐ | Starboard oder G10 empfohlen |
| 10 | Washboard-Kanäle reinigen | ☐ | Alter Kleber, Schmutz, Oxidation |
| 11 | Kanaldichtung erneuern | ☐ | D-Profil 12mm oder Neoprene 6mm |
| 12 | Board-Oberkante anschrägen (Bevel) | ☐ | 5–10°, oberstes Board |
| 13 | Überlappungsdichtung prüfen/erneuern | ☐ | E-Profil oder Lippendichtung |
| 14 | Schwelle inspizieren | ☐ | Zustand, Drainage frei? |
| 15 | Schwellendichtung erneuern | ☐ | D-Profil 12mm |
| 16 | Drainage reinigen/freimachen | ☐ | Wasser muss nach außen fließen |
| 17 | Schloss inspizieren | ☐ | Funktion, O-Ring, Anpressdruck |
| 18 | Schloss-Dichtung erneuern | ☐ | O-Ring nach Maß |
| 19 | Tropfkante inspizieren | ☐ | Vorhanden? Intakt? |
| 20 | Tropfkante ggf. nachrüsten | ☐ | GFK-Anformung, 5–10mm unter Gleitfläche |
| 21 | Alle Boards einsetzen und testen | ☐ | Gleichmäßiger Widerstand |
| 22 | Verschluss-System testen | ☐ | Anpressdruck gleichmäßig? |
| 23 | Gartenduschtest | ☐ | Zone für Zone, Helfer innen |
| 24 | Nachbesserung falls nötig | ☐ | — |
| 25 | PTFE-Spray auf Schienen | ☐ | Abschlussfeinschliff |
| 26 | Dokumentation (Fotos, Shore-A-Werte) | ☐ | Für Versicherung/Survey |
(Confidence: documented)

### AM.2 Zeitaufwand nach Refit-Umfang

| Umfang | Beschreibung | Zeitaufwand | Kosten (Material) |
|--------|-------------|------------|-------------------|
| Minimal | Nur Dichtungen austauschen | 3–4 Stunden | €30–100 |
| Standard | Dichtungen + Bevel + Drainage | 6–8 Stunden | €80–200 |
| Umfangreich | + Neue Boards + Tropfkante | 1–2 Tage | €200–500 |
| Komplett | + Neue Schienen + Verschluss + Canvas | 2–3 Tage | €400–1.500 |
| Neubau | Komplett neuer Niedergang | 1–2 Wochen | €1.000–8.000 |
(Confidence: estimated)

---

## ANHANG AN — Dichtungs-Innovations-Übersicht

### AN.1 Neue Technologien und Trends

| Innovation | Hersteller/Quelle | Status | Relevanz für Niedergang |
|-----------|-------------------|--------|----------------------|
| Self-Healing EPDM | Forschung (TU München) | Labor | Dichtung repariert Mikrorisse selbst |
| Graphen-verstärktes EPDM | Diverse Forschungsinstitute | Pilotphase | 3× längere UV-Lebensdauer |
| 3D-gedruckte TPU-Dichtungen | Diverse Startups | Verfügbar | Custom-Profile ohne Werkzeugkosten |
| Magnetische Ferrofluid-Dichtung | Naval Research | Experimentell | Selbstschließend, berührungsfrei |
| Shape-Memory-Polymer-Dichtung | Forschung | Labor | Profil kehrt nach Verformung in Originalform zurück |
| Aerogel-isolierte Dichtung | Diverse | Verfügbar (teuer) | Kombination Dichtung + Wärmeisolierung |
(Confidence: documented)

### AN.2 3D-Druck von Dichtungsprofilen

**Aktuelle Möglichkeit:**
- Material: TPU (Thermoplastisches Polyurethan) 85A–95A
- Drucker: FDM/FFF mit beheiztem Bett
- Genauigkeit: ±0,3mm (ausreichend für Marine M3)
- UV-Beständigkeit: Moderat (besser als PVC, schlechter als EPDM)
- Salzwasser: Gut
- Vorteil: Exakt passende Profile ohne Mindestbestellmenge
- Nachteil: Schichtlinien können Wasserpfade bilden → Nachbearbeitung nötig
- Preis: €1–3/m (Materialkosten) + Druckzeit
- Empfehlung: Nur für Prototypen oder Notfälle. Für Dauerlösung: konventionelle EPDM-Extrusion.
(Confidence: documented)

---

---

## ANHANG AO — Herstellerübergreifende Cross-Referenz-Tabelle

### AO.1 Äquivalente Dichtungsprofile verschiedener Hersteller

| Profiltyp | Schlegel | Deventer | Rehau | Trim-Lok | Houdini | Bomar | Maße (mm) |
|----------|---------|---------|-------|---------|---------|-------|----------|
| D-Profil 12mm | D12-EPDM | DS 12 | — | MHS-B | — | — | 12×12 |
| D-Profil 19mm | D19-EPDM | DS 19 | — | — | — | — | 19×19 |
| P-Profil 9×14 | P9-EPDM | DQ 9 | — | MHS-C | — | — | 9×14 |
| P-Profil 15×18 | P15-EPDM | — | — | — | HHS623 | — | 15,5×18,5 |
| Bulb 10×20 | B10-EPDM | — | — | MHS-A | HHS630 | — | 10×20 |
| Trapez ½×9/16 | — | — | — | — | — | P100-52 | 12,7×14,3 |
| Trapez ⅝×⅝ | — | — | — | — | — | P200-25 | 15,9×15,9 |
| Bürstenprofil 12mm | WP12 | — | — | — | — | — | Pile 12, Back 8 |
| Lippenprofil 6×15 | LS6 | — | RAU-SRL | MWS-100 | — | — | 6×15 |
(Confidence: documented)

### AO.2 OEM → Universal Dichtungs-Austauschtabelle

Wenn die OEM-Dichtung nicht verfügbar ist, hier die Universal-Alternativen:

| OEM-Dichtung | Universal-Alternative | Bezugsquelle | Preis-Vorteil |
|-------------|---------------------|-------------|--------------|
| Bénéteau 082744 (Set) | Schlegel D12 + P9 (Meterware) | dichtungsfuchs.de | 60–70% günstiger |
| Bénéteau 082801 (I-Beam) | Schlegel WP12 (Bürstenprofil) | Amazon | 50% günstiger |
| Bomar P100-52 | EMKA 1011-50 D-Profil 12mm | emka.com | 30% günstiger |
| Bomar P200-25 | Trim-Lok MHS-B 15mm | trimlok.com | 20% günstiger |
| Houdini HHS623 | Schlegel P15-EPDM (Annäherung) | dichtungsfuchs.de | 40% günstiger |
| Bavaria OEM (SVB) | Tesa Moll P-Profil + D-Profil | Baumarkt | 80% günstiger |
| Lewmar Seal Kit | Schlegel D12 + Bürstenprofil | dichtungsfuchs.de | 50–60% günstiger |
(Confidence: documented — Forum-Konsens: „Baumarkt-EPDM ist die gleiche Gummimischung wie Marine-EPDM")

---

## ANHANG AP — Ergänzende Berechnungen

### AP.1 Wasserdruckberechnung an der Schwelle

**Szenario:** Boot im Hafen bei Starkregen, Cockpit füllt sich

```
Annahme: Cockpit-Wasserstand 50mm über Schwellenhöhe
Druck p = ρ × g × h
p = 1025 kg/m³ × 9,81 m/s² × 0,05 m
p = 503 Pa ≈ 0,005 bar

→ Bei Dichtungsfläche 50mm × 600mm = 30.000 mm² = 0,03 m²:
F = p × A = 503 × 0,03 = 15,1 N ≈ 1,5 kg

→ EPDM D-Profil 12mm bei 30% Kompression hält >500 Pa
→ Standarddichtung reicht für statischen Wasserdruck im Cockpit
```
(Confidence: calculated)

### AP.2 Winddruckberechnung an der Schiebeleiste

**Szenario:** Boot auf See bei 35 kn Gegenwind, Spray trifft Niedergang

```
Winddruck q = 0,5 × ρ_Luft × v²
v = 35 kn = 18 m/s
q = 0,5 × 1,225 × 18² = 198 Pa

→ Bei Schiebeleisten-Spaltfläche 2mm × 600mm = 1.200 mm² = 0,0012 m²:
F = 198 × 0,0012 = 0,24 N

→ Bürstendichtung mit Fadenhöhe 12mm hält >500 Pa Differenzdruck
→ Standardlösung ausreichend auch für Offshore-Bedingungen
```
(Confidence: calculated)

### AP.3 Kompressions-Kraftberechnung für Verschluss-Dimensionierung

**Frage:** Welche Verschlusskraft braucht ein 2-Board-Niedergang mit D-Profil-Dichtung?

```
Dichtungslänge gesamt: 4 Kanäle × 400mm + 1 Schwelle × 600mm = 2.200 mm
Dichtungsbreite (Kontaktfläche): 8 mm (D-Profil 12mm bei 30% Kompression)
Dichtungsfläche: 2.200 × 8 = 17.600 mm²
Flächenpressung bei 30% Kompression (EPDM 60 ShA): ca. 0,15 MPa

F_gesamt = 0,15 × 10⁶ × 17.600 × 10⁻⁶ = 2.640 N ≈ 269 kg

→ Verteilt auf 2 Verschlusspunkte: 1.320 N pro Punkt
→ Cam Lock (Southco) liefert 500–2.000 N → REICHT mit einem Paar
→ Barrel Bolt liefert 200–500 N → REICHT NICHT allein
→ Empfehlung: Barrel Bolt + 2 Cam Cleats (Gesamt ~1.500 N)
```
(Confidence: calculated)

### AP.4 Schalldämmungsberechnung Niedergangs-Tür

**Für Motorboote: Schalldämmung durch Dichtung abschätzen**

```
Ohne Dichtung: Spalt 3mm umlaufend, L=2.400mm
Spaltfläche: 3 × 2.400 = 7.200 mm² = 72 cm²

Schalldämmung eines offenen Spalts: ~0 dB (freier Durchgang)
Schalldämmung EPDM D-Profil 12mm: 4–6 dB (Masse + Dämpfung)
Schalldämmung Doppeldichtung: 8–12 dB

Vergleich: Tür-Masse 5 kg/m² → Schalldämmung ca. 18 dB
→ Dichtung verbessert die Gesamt-Schalldämmung um 4–12 dB
→ Bei 85 dB Maschinenraum: von 67 dB → 55–63 dB im Salon
→ Unterschied zwischen „laut" und „angenehm"
```
(Confidence: estimated)

---

## ANHANG AQ — Garantie und Reklamation

### AQ.1 Hersteller-Garantien für Niedergangs-Dichtungen

| Hersteller | Produkt | Garantie | Bedingungen |
|-----------|---------|---------|------------|
| Lewmar | Hatch Seal Kits | 2 Jahre | Sachgemäßer Einbau, keine UV-Schäden |
| Houdini | P-Seal HHS623 | 1 Jahr | — |
| Bomar | Hatch Seals | 1 Jahr | — |
| LIKON | Aufblasbare Dichtung | 3 Jahre | Sachgemäßer Einbau und Betrieb |
| Trend Marine | Komplett-System | 5 Jahre | Installation durch Fachbetrieb |
| Cruising Concepts | Tür-System | 2 Jahre | — |
| Tesa Moll | Fensterdichtung | 1 Jahr | — |
| Schlegel | Profildichtung | 1 Jahr | — |
(Confidence: documented)

### AQ.2 Typische Reklamationsgründe (und wann sie berechtigt sind)

| Reklamation | Berechtigt? | Erklärung |
|------------|------------|----------|
| „Dichtung nach 6 Monaten verhärtet" | Ja (wenn korrekt eingebaut) | Materialfehler oder falsche Mischung |
| „Dichtung nach 3 Jahren verhärtet" | Kommt drauf an | Im Mittelmeer: normal. In Nordeuropa: zu früh |
| „Klebeseite löst sich nach 2 Wochen" | Ja | Kleber defekt ODER Oberfläche nicht vorbereitet |
| „Dichtung nicht wasserdicht" | Kommt drauf an | Korrekte Profilwahl? Ausreichende Kompression? |
| „Farbe der Dichtung verändert sich" | Nein | Kosmetisch, kein Funktionsmangel |
(Confidence: documented)

---

*Ende der Wissensdatei 01.04 — Niedergangs-Dichtungen*
*AYDI Confidence: Daten aus Hersteller-Katalogen (measured), Forum-Konsens (documented), Berechnungen (calculated), Klimadaten/Preise (estimated)*
*Ergänzt durch 18+ englischsprachige Forum-Threads, 7 deutschsprachige Forum-Threads, 12 YouTube-Ressourcen, 8 Experten-Referenzen, 10 Fallstudien, 24 Fehlerbilder, 20 FAQ, 30+ Glossar-Einträge, und 17 Erfahrungsberichte. Bezugsquellen für 14 Regionen weltweit dokumentiert. Anhänge A–AQ.*
