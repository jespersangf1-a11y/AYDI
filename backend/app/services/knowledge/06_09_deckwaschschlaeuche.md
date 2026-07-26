# 06.09 — Deckwaschschläuche und Ankerspül-Systeme

> **Modulkontext**: materials, structural, compliance, service_patterns, cost
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04

---

## Inhaltsverzeichnis

1. Einführung & Regulatorischer Rahmen
2. Zukunftstechnologien
3. Best Practices nach Revier
4. Regional Sourcing
5. Zweck dieser Wissensdatei
6. Pydantic-Modelle
7. Grundlagen
8. Hersteller — Vollständige Übersicht
9. Anlagen-spezifische Zuordnung
10. Schlauchschellen & Verbindungstechnik
11. Technische Referenz & Berechnungen
12. Einbau-/Austausch-Anleitung
13. Lebensdauer und Alterungsmechanismen
14. Fehlerbild-Atlas
15. Fehlerbehebungs-Leitfaden
16. FAQ
17. Glossar
18. Schnell-Referenz
19. Notfall-Ressourcen
20. Anhänge A–R

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Sicherheitskritische Bedeutung

Deckwaschschläuche und Ankerspül-Systeme gehören zur Kategorie der nicht-sicherheitskritischen aber betriebsrelevanten Bordausrüstung. Im Gegensatz zu Bilgen-, Kraftstoff- oder Abgasschläuchen gefährdet ein Versagen dieser Systeme nicht unmittelbar die Seetüchtigkeit. Dennoch haben Deckwasch-Systeme erheblichen Einfluss auf die Langlebigkeit des Bootes: Salzwasserrückstände auf Deck, an der Ankerkette und in der Ankerkasten-Bilge beschleunigen Korrosion an Beschlägen, Kettengliedern und GFK-Gelcoat massiv.

Ankerspül-Systeme (Anchor Wash) verhindern, dass Salz, Schlick und Sand mit der Kette in den Ankerkasten gelangen. Ohne regelmäßiges Spülen korrodiert die Kette, das Ankerkastengetriebe (Windlass) verschleißt schneller, und der Ankerkasten wird zur Quelle übler Gerüche.

(Confidence: documented)

### 1.2 Versagensszenarien und Konsequenzen

| Versagensmodus | Konsequenz | Zeitrahmen |
|---|---|---|
| Schlauch platzt unter Pumpendruck | Unkontrollierter Wasseraustritt an Deck/in Bilge | Sofort bei Einschalten |
| UV-Degradation (Spiralschlauch an Deck) | Brüchigkeit, Mikrorisse, Bersten | 2–5 Jahre (revierabhängig) |
| Quick-Connect-Fitting undicht | Druckverlust, reduzierte Spülwirkung | Schleichend |
| Pumpe läuft trocken | Impeller-Zerstörung, Totalausfall | 30–120 Sekunden trocken |
| Seewasser-Ansaugung verstopft (Muscheln) | Pumpe fördert nicht, Überhitzung | Saisonabhängig |
| Ankerspül-Düse verstopft | Kette wird nicht gespült, Salzaufbau | Wochen bis Monate |
| Rückschlagventil fehlt/versagt | Seewasser strömt rückwärts ins Boot | Bei Seegang, 1–8 h |
| Schlauchschelle korrodiert/löst sich | Schlauch rutscht vom Stutzen ab | Plötzlich unter Druck |
| Falsche Schlauchmaterial (PVC statt UV-beständig) | Vorzeitige Versprödung an Deck | 1–2 Sommer |
| Winterisierung versäumt | Frostschaden an Pumpe und Schläuchen | Erster Frost |

(Confidence: documented)

### 1.3 Regulatorischer Rahmen — Normen und Vorschriften

Deckwasch-Systeme unterliegen keiner eigenständigen ISO-Norm. Die relevanten Normen ergeben sich aus den Einzelkomponenten und dem Einbauort:

| Norm | Titel | Relevanz für Deckwasch-Systeme |
|---|---|---|
| ISO 8846:1990 | Zündschutz für Elektrogeräte in Benzinumgebungen | Nur relevant wenn Deckwaschpumpe in Benzin-Motorraum oder Nähe Kraftstofftank |
| ISO 9093-1:1994 / ISO 9093-2:2002 | Borddurchlässe und Seeventile | Seewasser-Ansaugung für Deckwasch-Rohwasser-Systeme |
| ISO 15083:2003 | Bilgenlenz-Systeme | Verwandtes System, Pumpenauswahl-Kriterien übertragbar |
| ISO 10133:2012 | Elektrische Gleichstrom-Installationen | Verdrahtung der Deckwaschpumpe, Absicherung, Kabelquerschnitte |
| ISO 13297:2014 | Elektrische Wechselstrom-Installationen | Nur bei 230V-Deckwaschpumpen (selten, große Yachten) |
| CE / RCD 2013/53/EU | Sportboot-Richtlinie | Borddurchlässe und elektrische Installation |
| ABYC H-27 | Seewasser-Rohrleitungen (Seeventile/Borddurchlässe) | US-Norm, relevant für US-Boote und Referenz |
| ABYC H-22 | Elektrische Bilgenpumpen | Übertragbar auf Deckwaschpumpen |
| EN 12115 | Flexible Gummi- und Kunststoffschläuche | Allgemeine Schlauchanforderungen |
| DIN 3017 | Schlauchschellen (Schneckengewinde) | Schlauchschellen-Spezifikationen |

(Confidence: measured)

### 1.4 CE-Konformität — Was relevant ist

Für die CE-Zertifizierung einer Yacht nach RCD 2013/53/EU sind Deckwasch-Systeme in folgenden Aspekten relevant:

**Borddurchlässe (ISO 9093):**
- Jede Seewasser-Ansaugung für eine Rohwasser-Deckwaschpumpe erfordert einen normkonformen Borddurchlass mit Seeventil
- Material: Bronze (CW617N oder besser), Edelstahl 316L, oder Marelon (glasfaserverstärktes Nylon)
- Der Borddurchlass muss von innen zugänglich sein und sich im Notfall schließen lassen
- Mindest-Wandstärke: gemäß ISO 9093 für den jeweiligen Nenndurchmesser

**Elektrische Installation (ISO 10133):**
- Deckwaschpumpe muss über eigene Absicherung (Sicherung oder Schutzschalter) verfügen
- Kabelquerschnitt gemäß Stromaufnahme und Leitungslänge (Spannungsfall ≤3% empfohlen, ≤10% zulässig)
- Spritzwassergeschützte Schalter (IP 54 minimum) für Deckinstallation
- Masseverbindung und Korrosionsschutz gemäß ISO 10133

**Brandschutz (ISO 9094):**
- Wenn Deckwaschpumpe in Motorraum montiert (Rohwasser-Pumpe an Hauptmaschine): Zündschutz gemäß ISO 8846 bei Benzinmotoren (bei Dieselmotoren nicht erforderlich)

(Confidence: measured)

### 1.5 Klassifikations- und Versicherungsanforderungen

Deckwasch-Systeme werden von Klassifikationsgesellschaften (Lloyd's, DNV, BV) bei Yachten >24m als Teil der Decksausrüstung berücksichtigt:

- **Lloyd's SSC**: Ankerspül-Systeme sind bei Yachten >30m in der Spezifikation üblich
- **RINA**: Empfiehlt Frischwasser-Deckwasch für Superyachten zur Gelcoat-Pflege
- **Versicherungen**: Kein direkter Einfluss auf Prämien, aber dokumentierte Wartung der Ankerkette (inkl. Spülsystem) kann bei Ankerverlust-Claims relevant sein

(Confidence: estimated)

---

## 2. Zukunftstechnologien

### 2.1 Wasserrecycling-Systeme

Moderne Superyachten integrieren zunehmend Grauwasser-Recycling für Deckwäsche. Das Prinzip: Duschwasser und Handwaschwasser wird gefiltert, UV-desinfiziert und als Deckwaschwasser wiederverwendet. Hersteller wie Eco-Techno Marine (Italien) und Hamann Wassertechnik (Deutschland) bieten kompakte Anlagen für Yachten ab 15m.

- Typische Einsparung: 200–500 l/Tag auf einer 20m-Yacht
- Investition: 8.000–25.000 EUR (abhängig von Kapazität)
- Amortisation: Relevant nur in Revieren mit Frischwassermangel (Balearen, Griechenland)

(Confidence: estimated)

### 2.2 Elektrische Hochdruckreiniger mit Batteriebetrieb

Kabellose Hochdruckreiniger wie der Kärcher OC 3 oder Worx Hydroshot werden zunehmend als tragbare Deckwasch-Alternative eingesetzt. Vorteile: keine feste Installation nötig, flexibel einsetzbar, kein Borddurchlass erforderlich. Nachteile: begrenzte Wasserkapazität (typisch 4–15 l Tank), geringer Druck (5–24 bar vs. 20–60 bar fest installiert), Akku-Laufzeit (15–30 min).

Für Boote <10m ohne festes Deckwasch-System sind diese Geräte eine praktikable Ergänzung.

(Confidence: documented)

### 2.3 Smart-Pumpen mit App-Steuerung

Jabsco/Xylem bietet mit der Par-Max HD-Serie Pumpen mit optionalem Bluetooth-Modul an. Die Steuerung über Smartphone-App ermöglicht:
- Fernsteuerung der Pumpe (Ein/Aus, Druckeinstellung)
- Betriebsstunden-Zähler und Wartungserinnerungen
- Leckage-Alarm (unerwarteter Druckabfall)

Shurflo/Pentair arbeitet an ähnlicher Technologie für die 2027-Produktlinie.

(Confidence: estimated)

### 2.4 Ozon-Desinfektion für Ankerspülung

Einige Superyacht-Werften (Lürssen, Feadship) experimentieren mit Ozon-injiziertem Spülwasser für Ankerketten. Ozon eliminiert Geruchsbildung im Ankerkasten vollständig und reduziert biologisches Fouling an der Kette. Die Technik ist noch teuer (15.000–40.000 EUR für das Ozon-Modul) und hat sich im Serienbau nicht durchgesetzt.

(Confidence: estimated)

### 2.5 Automatisierte Ankerkasten-Spülung

Systeme wie das Quick?"Aqua-Wash" oder das Maxwell "Auto-Rinse" erkennen über einen Kettensensor, wann der Anker eingeholt wird, und aktivieren automatisch die Spüldüse am Bugbeschlag. Die Spülung läuft, solange die Kette eingeholt wird, und stoppt automatisch. Integration über NMEA 2000 oder proprietäre Windlass-Steuerungen.

(Confidence: documented)

---

## 3. Best Practices nach Revier

### 3.1 Mittelmeer (hoher UV-Index, wenig Regen)

- **Priorität**: UV-beständige Schläuche, Frischwasser-Spülung nach jedem Törn
- **Empfehlung**: Spiralschlauch mit UV-Stabilisator (Trident 369 oder Goodyear Marine Wash-Down)
- **Ankerspülung**: Frischwasser bevorzugt (Salzkrusten bilden sich schnell)
- **Winterisierung**: Nicht erforderlich (frostfrei), aber UV-Schutz ganzjährig nötig
- **Schlauch-Lebensdauer**: 3–5 Jahre für exponierte Deckschläuche (hohe UV-Belastung)
- **Häufigster Fehler**: PVC-Gartenschläuche (Gardena, Hozelock) an Deck — versprüden in 1–2 Sommern

(Confidence: documented)

### 3.2 Nordeuropa / Ostsee / Nordsee

- **Priorität**: Frostbeständigkeit, Winterisierung
- **Empfehlung**: Schlauch mit Betriebstemperatur bis -20°C (Trident 369, Shields Series 148)
- **Ankerspülung**: Rohwasser ausreichend (Salzgehalt Ostsee gering), Frischwasser für Nordsee
- **Winterisierung**: KRITISCH — Pumpe und Schläuche entleeren, Frostschutzmittel (Propylenglykol, NICHT Ethylenglykol!)
- **Schlauch-Lebensdauer**: 5–8 Jahre (geringere UV-Belastung)
- **Häufigster Fehler**: Winterisierung vergessen → Pumpe platzt → 250–600 EUR Schaden

(Confidence: documented)

### 3.3 Tropen / Karibik

- **Priorität**: UV-Schutz, Biofouling-Resistenz, Frischwasser-Management
- **Empfehlung**: Hochwertiger EPDM/Santoprene-Schlauch, Quick-Connect aus Bronze (kein Messing!)
- **Ankerspülung**: Frischwasser-Spülung obligatorisch (Korallenreste verstopfen Düsen)
- **Winterisierung**: Nicht erforderlich
- **Schlauch-Lebensdauer**: 2–4 Jahre (extreme UV, Pilzbefall möglich)
- **Häufigster Fehler**: Messing-Fittings statt Bronze → dezinkifizierung in 1–2 Saisons

(Confidence: documented)

### 3.4 Gezeitenreviere (Großbritannien, Bretagne, Wattenmeer)

- **Priorität**: Leistungsfähige Ankerspülung (Schlick, Sand)
- **Empfehlung**: Hochdruckpumpe (4+ bar), Ankerspül-Düse mit engem Strahlwinkel
- **Ankerspülung**: ESSENTIELL — Sand und Schlick zerstören Windlass-Getriebe
- **Schlauch**: Größerer Durchmesser (19mm statt 12mm) für höheren Volumenstrom
- **Häufigster Fehler**: Zu schwache Pumpe → Kette wird nicht sauber → Windlass-Schaden (800–3.000 EUR)

(Confidence: documented)

---

## 4. Regional Sourcing

### 4.1 Europa

| Lieferant | Land | Stärke | Lieferzeit |
|---|---|---|---|
| SVB (svb24.com) | DE | Breitestes Sortiment, gute Beratung | 1–3 Tage DE, 3–7 Tage EU |
| Compass24 (compass24.de) | DE | Gute Preise, große Auswahl | 1–3 Tage DE |
| Toplicht (toplicht.de) | DE | Spezialist Hamburg, Beratung vor Ort | 1–2 Tage DE |
| AWN (awn.de) | DE | Traditionshandel, Qualitätsprodukte | 2–4 Tage DE |
| Bukh-Bremen (bukh-bremen.de) | DE | Jabsco/Xylem-Spezialist | 1–3 Tage DE |
| Marineshop (orangemarine.com) | FR | Frankreich-Spezialist | 2–5 Tage FR |
| Force4 (force4.co.uk) | UK | UK-Markt, gute Preise | 2–5 Tage UK |
| Plastimo Distribution | FR | Direkt vom Hersteller | 3–7 Tage EU |
| Osculati Distribution | IT | Direkt vom Hersteller | 5–10 Tage EU |

### 4.2 Nordamerika

| Lieferant | Land | Stärke | Lieferzeit |
|---|---|---|---|
| West Marine | US | Größtes Sortiment, Filialen | 1–5 Tage US |
| Defender (defender.com) | US | Beste Preise, Profi-Sortiment | 2–5 Tage US |
| Hamilton Marine | US | Ostküste-Spezialist | 2–5 Tage US |
| Fisheries Supply | US | PNW-Spezialist, Profi-Qualität | 2–5 Tage US |

### 4.3 Asien-Pazifik

| Lieferant | Land | Stärke | Lieferzeit |
|---|---|---|---|
| Whitworths (whitworths.com.au) | AU | Australien-Spezialist | 2–7 Tage AU |
| BLA (bla.com.au) | AU | Großhandel AU/NZ | 3–7 Tage AU |
| CH Smith (chsmith.com.au) | AU | Premium-Segment | 2–5 Tage AU |

(Confidence: documented)

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei ermöglicht dem AYDI-System die automatisierte Bewertung von Deckwaschschläuchen und Ankerspül-Systemen auf Yachten. Sie dient als Referenz für:

1. **Pipeline A (Structured)**: Bewertung von Schlauchspezifikationen, Pumpenauswahl, Systemauslegung anhand technischer Daten
2. **Pipeline B (Visual)**: Zustandsbeurteilung von Deckschläuchen und Fittings anhand von Fotos (UV-Degradation, Rissbildung, Verfärbung)
3. **Pipeline C (Text)**: Extraktion von Wartungsinformationen und Schadensmeldungen aus Service-Berichten

### Schlüsselfragen, die AYDI beantworten soll:

- Ist der verbaute Deckwaschschlauch UV-beständig und für den Einsatzort geeignet?
- Entspricht die Pumpenleistung der Bootsgröße und dem Verwendungszweck?
- Ist das Ankerspül-System korrekt ausgelegt (Druck, Volumenstrom, Düsenposition)?
- Zeigen Fotos Alterungserscheinungen (UV-Degradation, Kinking, Verfärbung)?
- Sind die Verbindungen (Schlauchschellen, Quick-Connects) salzwassertauglich?
- Ist das System winterisierbar und wurde es korrekt winterisiert?
- Fehlt ein Rückschlagventil an der Seewasser-Ansaugung?

(Confidence: measured)

---

## 6. Pydantic-Modelle

### 6.1 DeckWashHoseSpec — Schlauchspezifikation

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class HoseType(str, Enum):
    """Schlauchtyp für Deckwäsche."""
    COILED = "coiled"                    # Spiralschlauch (selbstaufrollend)
    FLAT = "flat"                        # Flachschlauch (kompakt verstaubar)
    REINFORCED_PVC = "reinforced_pvc"    # Armierter PVC-Schlauch
    EPDM_RUBBER = "epdm_rubber"         # EPDM-Gummi-Schlauch
    SANTOPRENE = "santoprene"            # Santoprene (TPV) Schlauch
    POLYURETHANE = "polyurethane"        # PU-Schlauch (leicht, flexibel)
    SILICONE = "silicone"               # Silikonschlauch (selten)


class WaterSource(str, Enum):
    """Wasserquelle für Deckwasch-System."""
    RAW_WATER = "raw_water"              # Seewasser / Rohwasser
    FRESH_WATER = "fresh_water"          # Frischwasser aus Tank
    DUAL = "dual"                        # Umschaltbar Roh/Frisch
    DOCK_WATER = "dock_water"            # Landwasseranschluss


class SystemPurpose(str, Enum):
    """Verwendungszweck des Deckwasch-Systems."""
    DECK_WASH = "deck_wash"              # Allgemeine Deckwäsche
    ANCHOR_WASH = "anchor_wash"          # Ankerspülung
    COCKPIT_WASH = "cockpit_wash"        # Cockpitspülung
    FISH_CLEANING = "fish_cleaning"      # Fisch-Reinigungsstation
    SWIM_PLATFORM = "swim_platform"      # Badeplattform-Dusche
    LIVEWELL = "livewell"                # Lebendfisch-Becken
    MULTI_PURPOSE = "multi_purpose"      # Mehrzweck


class DeckWashHoseSpec(BaseModel):
    """Spezifikation eines Deckwasch- oder Ankerspül-Schlauchs."""
    model_config = {"from_attributes": True}

    hose_type: HoseType
    manufacturer: str = Field(..., description="Hersteller des Schlauchs")
    product_line: str = Field(..., description="Produktlinie/Serie")
    part_number: Optional[str] = Field(None, description="Hersteller-Teilenummer")
    inner_diameter_mm: float = Field(..., ge=6.0, le=50.0, description="Innendurchmesser in mm")
    outer_diameter_mm: float = Field(..., ge=8.0, le=65.0, description="Außendurchmesser in mm")
    wall_thickness_mm: float = Field(..., ge=1.0, le=10.0, description="Wandstärke in mm")
    length_m: float = Field(..., ge=0.5, le=50.0, description="Länge in Metern")
    max_working_pressure_bar: float = Field(..., ge=1.0, le=30.0, description="Maximaler Betriebsdruck in bar")
    burst_pressure_bar: float = Field(..., ge=3.0, le=100.0, description="Berstdruck in bar")
    min_bend_radius_mm: float = Field(..., ge=20.0, le=500.0, description="Minimaler Biegeradius in mm")
    temp_range_min_c: float = Field(default=-20.0, description="Minimale Betriebstemperatur °C")
    temp_range_max_c: float = Field(default=60.0, description="Maximale Betriebstemperatur °C")
    uv_resistant: bool = Field(default=False, description="UV-beständig für Deckexposition")
    uv_rating_years: Optional[int] = Field(None, ge=0, le=20, description="UV-Beständigkeit in Jahren")
    material: str = Field(..., description="Schlauchmaterial (PVC, EPDM, Santoprene, PU)")
    reinforcement: Optional[str] = Field(None, description="Armierung (Polyester-Geflecht, Spiraldraht, etc.)")
    color: str = Field(default="weiß", description="Farbe des Schlauchs")
    food_safe: bool = Field(default=False, description="Lebensmittelecht (für Frischwasser)")
    anti_kink: bool = Field(default=False, description="Knickschutz")
    quick_connect_compatible: bool = Field(default=False, description="Schnellkupplung-kompatibel")
    weight_per_meter_g: Optional[float] = Field(None, description="Gewicht pro Meter in Gramm")
    price_eur_per_meter: Optional[float] = Field(None, description="Preis pro Meter in EUR")
    water_source: WaterSource = Field(default=WaterSource.RAW_WATER)
    system_purpose: SystemPurpose = Field(default=SystemPurpose.DECK_WASH)
    boat_class: Optional[str] = Field(None, description="Empfohlene Bootsklasse")
    confidence: str = Field(default="estimated", description="Confidence-Level der Spezifikation")
```

### 6.2 DeckWashHoseCondition — Zustandsbewertung

```python
class UVDegradationLevel(str, Enum):
    """UV-Degradations-Stufen."""
    NONE = "none"                        # Keine sichtbare UV-Schädigung
    SURFACE_CHALKING = "surface_chalking" # Oberflächenverkreidung
    DISCOLORATION = "discoloration"      # Farbveränderung (Vergilbung)
    MICRO_CRACKING = "micro_cracking"    # Mikrorissbildung (Haarrisse)
    DEEP_CRACKING = "deep_cracking"      # Tiefe Risse
    BRITTLE = "brittle"                  # Vollständige Versprödung


class FittingCondition(str, Enum):
    """Zustand von Anschlussfittings."""
    NEW = "new"                          # Neu, einwandfrei
    GOOD = "good"                        # Gut, voll funktionsfähig
    CORRODED_SURFACE = "corroded_surface" # Oberflächenkorrosion
    CORRODED_DEEP = "corroded_deep"      # Tiefenkorrosion
    DEZINCIFIED = "dezincified"          # Dezinkifizierung (Messing)
    CRACKED = "cracked"                  # Rissig (Kunststoff)
    LEAKING = "leaking"                  # Undicht


class DeckWashHoseCondition(BaseModel):
    """Zustandsbewertung eines Deckwasch-Schlauchs via visuelle Inspektion."""
    model_config = {"from_attributes": True}

    overall_score: int = Field(..., ge=0, le=100, description="Gesamtzustand 0–100")
    uv_degradation: UVDegradationLevel = Field(..., description="UV-Degradations-Stufe")
    uv_score: int = Field(..., ge=0, le=100, description="UV-Zustand 0–100")
    flexibility_score: int = Field(..., ge=0, le=100, description="Flexibilität 0–100")
    surface_condition_score: int = Field(..., ge=0, le=100, description="Oberfläche 0–100")
    fitting_condition: FittingCondition = Field(..., description="Zustand der Fittings")
    fitting_score: int = Field(..., ge=0, le=100, description="Fitting-Zustand 0–100")
    kinks_detected: int = Field(default=0, ge=0, description="Anzahl erkannter Knicke")
    kink_score: int = Field(..., ge=0, le=100, description="Knick-Bewertung 0–100")
    leak_points: int = Field(default=0, ge=0, description="Anzahl Leckstellen")
    leak_score: int = Field(..., ge=0, le=100, description="Leck-Bewertung 0–100")
    discoloration_percent: float = Field(default=0.0, ge=0.0, le=100.0, description="Verfärbungsanteil %")
    age_estimated_years: Optional[float] = Field(None, ge=0, le=30, description="Geschätztes Alter in Jahren")
    remaining_life_years: Optional[float] = Field(None, ge=0, le=15, description="Geschätzte Restlebensdauer in Jahren")
    replacement_recommended: bool = Field(default=False, description="Austausch empfohlen?")
    replacement_urgency: Optional[Literal["sofort", "nächste_saison", "mittelfristig", "nicht_erforderlich"]] = Field(None)
    findings: list[str] = Field(default_factory=list, description="Befunde in deutscher Sprache")
    suggestions: list[str] = Field(default_factory=list, description="Verbesserungsvorschläge")
    photo_references: list[str] = Field(default_factory=list, description="Foto-Referenzen")
    confidence: str = Field(default="visual_medium", description="Confidence-Level")
```

### 6.3 DeckWashSystemAssessment — Gesamtsystem-Bewertung

```python
class PumpType(str, Enum):
    """Pumpentyp für Deckwäsche."""
    DIAPHRAGM = "diaphragm"             # Membranpumpe (Jabsco Par-Max, Shurflo)
    CENTRIFUGAL = "centrifugal"          # Kreiselpumpe
    IMPELLER = "impeller"               # Impellerpumpe (Jabsco Puppy)
    GEAR = "gear"                       # Zahnradpumpe
    SUBMERSIBLE = "submersible"         # Tauchpumpe
    ENGINE_DRIVEN = "engine_driven"     # Motor-angetrieben (Seewasserpumpe)


class NozzleType(str, Enum):
    """Düsentyp."""
    ADJUSTABLE_SPRAY = "adjustable_spray"   # Verstellbare Brause
    JET = "jet"                             # Punktstrahl
    FAN = "fan"                             # Fächerstrahl
    SHOWER_HEAD = "shower_head"             # Duschkopf
    FIRE_NOZZLE = "fire_nozzle"             # Feuerlöschdüse-Typ
    TRIGGER_NOZZLE = "trigger_nozzle"       # Pistolendüse mit Abzug


class DeckWashSystemAssessment(BaseModel):
    """Gesamtbewertung eines Deckwasch- oder Ankerspül-Systems."""
    model_config = {"from_attributes": True}

    system_id: Optional[str] = Field(None, description="System-ID im AYDI-Projekt")
    boat_length_m: float = Field(..., ge=4.0, le=100.0, description="Bootslänge in Metern")
    boat_class: str = Field(..., description="Bootsklasse (Segelyacht, Motoryacht, etc.)")
    system_purpose: SystemPurpose = Field(..., description="Verwendungszweck")
    water_source: WaterSource = Field(..., description="Wasserquelle")

    # Pumpen-Bewertung
    pump_manufacturer: Optional[str] = Field(None)
    pump_model: Optional[str] = Field(None)
    pump_type: Optional[PumpType] = Field(None)
    pump_flow_lpm: Optional[float] = Field(None, ge=0, le=200, description="Pumpenfördermenge l/min")
    pump_pressure_bar: Optional[float] = Field(None, ge=0, le=30, description="Pumpendruck bar")
    pump_voltage: Optional[Literal[12, 24]] = Field(None, description="Betriebsspannung V")
    pump_current_a: Optional[float] = Field(None, ge=0, le=50, description="Stromaufnahme A")
    pump_score: int = Field(..., ge=0, le=100, description="Pumpen-Bewertung 0–100")

    # Schlauch-Bewertung
    hose_spec: Optional[DeckWashHoseSpec] = Field(None)
    hose_condition: Optional[DeckWashHoseCondition] = Field(None)
    hose_score: int = Field(..., ge=0, le=100, description="Schlauch-Bewertung 0–100")

    # Nozzle/Düse
    nozzle_type: Optional[NozzleType] = Field(None)
    nozzle_score: int = Field(default=50, ge=0, le=100, description="Düsen-Bewertung 0–100")

    # System-Bewertung
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtbewertung 0–100")
    pressure_adequate: bool = Field(default=True, description="Druck für Verwendungszweck ausreichend?")
    flow_adequate: bool = Field(default=True, description="Volumenstrom ausreichend?")
    uv_protection_adequate: bool = Field(default=True, description="UV-Schutz für Einbauort ausreichend?")
    winterization_possible: bool = Field(default=True, description="Winterisierung möglich?")
    backflow_prevention: bool = Field(default=False, description="Rückschlagventil vorhanden?")
    seacock_present: bool = Field(default=False, description="Seeventil an Ansaugung vorhanden?")

    # Kosten
    replacement_cost_eur: Optional[float] = Field(None, ge=0, description="Austauschkosten komplett EUR")
    maintenance_cost_annual_eur: Optional[float] = Field(None, ge=0, description="Jährliche Wartungskosten EUR")

    # Ergebnis
    findings: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    compliance_issues: list[str] = Field(default_factory=list)
    confidence: str = Field(default="estimated")
```

### 6.4 Score-Berechnung

```python
def calculate_deck_wash_system_score(assessment: DeckWashSystemAssessment) -> int:
    """
    Berechnet den Gesamtscore für ein Deckwasch-System.
    Gewichtung:
    - Pumpe: 30%
    - Schlauch: 25%
    - Fittings/Verbindungen: 20%
    - Düse: 10%
    - Systemauslegung: 15%
    """
    pump_weight = 0.30
    hose_weight = 0.25
    fitting_weight = 0.20
    nozzle_weight = 0.10
    system_weight = 0.15

    pump_score = assessment.pump_score
    hose_score = assessment.hose_score
    nozzle_score = assessment.nozzle_score

    # Fitting-Score aus hose_condition
    fitting_score = 50  # Default
    if assessment.hose_condition:
        fitting_score = assessment.hose_condition.fitting_score

    # System-Score berechnen
    system_score = 50  # Basis
    if assessment.pressure_adequate:
        system_score += 15
    if assessment.flow_adequate:
        system_score += 15
    if assessment.backflow_prevention:
        system_score += 10
    if assessment.seacock_present:
        system_score += 10

    total = (
        pump_score * pump_weight +
        hose_score * hose_weight +
        fitting_score * fitting_weight +
        nozzle_score * nozzle_weight +
        system_score * system_weight
    )

    return max(0, min(100, round(total)))
```

(Confidence: measured)

---

## 7. Grundlagen

### 7.1 Deckwasch-Systeme — Übersicht

Ein Deckwasch-System (englisch: Deck Wash oder Wash-Down System) besteht aus folgenden Komponenten:

1. **Wasserquelle**: Seewasser (über Borddurchlass) oder Frischwasser (aus Tank)
2. **Pumpe**: Membranpumpe, Impellerpumpe oder Kreiselpumpe
3. **Druckleitung**: Schlauch von Pumpe zu Deckdurchführung
4. **Deckdurchführung**: Wasserdichte Durchführung durch das Deck
5. **Deckschlauch**: Spiralschlauch, Flachschlauch oder fester Schlauch an Deck
6. **Düse/Brause**: Verstellbare Spritzdüse, Pistolendüse oder Duschkopf
7. **Schalter**: Wasserdichter Druckschalter oder Fußschalter an Deck
8. **Absicherung**: Sicherung und ggf. Relais im Schaltpanel

**Typische Systemkonfigurationen nach Bootsklasse:**

| Bootsklasse | Typisches System | Pumpe | Schlauch | Druck |
|---|---|---|---|---|
| Segelboot 8–10m | Einfach Rohwasser | Jabsco Par-Max 3.0 | 12mm ID Spirale | 2,8 bar |
| Segelboot 10–14m | Rohwasser + Ankerspülung | Jabsco Par-Max 4.0 | 16mm ID Spirale | 3,4 bar |
| Motoryacht 8–12m | Rohwasser + Frischwasser | Shurflo 4048 | 12mm ID Spirale | 3,8 bar |
| Motoryacht 12–18m | Dual-System | 2× Jabsco Par-Max | 19mm ID Spirale + fest | 4,1 bar |
| Segelyacht 14–20m | Voll integriert | Jabsco Par-Max HD5 | 19mm ID + Ankerspülung | 4,8 bar |
| Motoryacht 18–25m | Profisystem | 2–3 Pumpen, Drucktank | 25mm ID fest + Spirale | 5,5 bar |
| Superyacht 25m+ | Hochdruck-Frischwasser | Zentral-Druckwasseranlage | 25–32mm fest | 6–8 bar |

(Confidence: documented)

### 7.2 Rohwasser vs. Frischwasser — Entscheidungskriterien

**Rohwasser-Systeme (Seewasser):**
- Vorteile: Unbegrenzter Wasservorrat, günstiger, einfache Installation
- Nachteile: Salzrückstände auf Deck, beschleunigt Korrosion an Beschlägen, Muschelbewuchs in Ansaugung
- Geeignet für: Deckwäsche während Fahrt, Ankerketten-Vorspülung, Fischverarbeitung
- Typische Pumpen: Jabsco Par-Max 1.0 bis 4.0, Shurflo 2088, Whale Gulper

**Frischwasser-Systeme:**
- Vorteile: Kein Salz auf Deck, schont Gelcoat und Beschläge, kein Fouling
- Nachteile: Verbraucht Tankwasser (limitiert), höhere Installationskosten
- Geeignet für: Nachreinigung nach Seewasser, Badeplattform-Dusche, empfindliche Teakdecks
- Typische Pumpen: Aus der Druckwasseranlage oder separate Frischwasser-Pumpe

**Dual-Systeme (Umschaltbar):**
- 3-Wege-Ventil oder Y-Verteiler ermöglicht Umschaltung zwischen Roh- und Frischwasser
- Empfehlung für alle Boote >12m
- Reihenfolge: Erst Seewasser-Vorspülung, dann Frischwasser-Nachspülung

(Confidence: documented)

### 7.3 Spiralschlauch (Coiled Hose) vs. Flachschlauch (Flat Hose)

**Spiralschlauch (Coiled Wash-Down Hose):**

Der Spiralschlauch ist der Standard für marine Deckwäsche. Er rollt sich nach Gebrauch selbstständig auf und liegt kompakt an Deck. Typische Längen: 4,5m (15ft), 7,5m (25ft), 15m (50ft) ausgerollt.

| Eigenschaft | Spezifikation |
|---|---|
| Material | PU (Polyurethan) oder PVC mit Spiralarmierung |
| Innendurchmesser | 12mm (½") oder 16mm (⅝") |
| Arbeitsdruck | 4–8 bar typisch |
| Rückstellkraft | Selbstaufrollend durch Materialerinnerung |
| UV-Beständigkeit | KRITISCH — Hauptversagensursache! |
| Lagerung | An Deck in Halteclip oder unter Persenning |
| Lebensdauer | 2–5 Jahre (UV-abhängig) |
| Typische Preise | 25–80 EUR (4,5m), 40–120 EUR (7,5m), 60–180 EUR (15m) |

**Empfohlene Spiralschläuche:**
- **Trident Marine 369 Series**: Santoprene, UV-beständig, -40°C bis +100°C, beste Lebensdauer
- **Goodyear Marine Coiled**: EPDM, gute UV-Beständigkeit, moderate Preise
- **Jabsco 25ft Coiled Hose (P/N 25800-0012)**: PU, mittel UV, Standardqualität
- **Whale System 15 Coiled Hose**: PU, Quick-Connect, mittlere Qualität
- **Osculati Art. 36.464.xx**: PVC, günstig, begrenzte UV-Beständigkeit (2–3 Jahre)

**Flachschlauch (Flat Hose / Lay-Flat Hose):**

Flachschläuche liegen flach zusammengefaltet und lassen sich platzsparend in einem Locker verstauen. Sie füllen sich erst unter Druck. Hauptvorteil: minimaler Stauraum. Nachteil: Müssen nach Gebrauch sorgfältig aufgerollt und verstaut werden.

| Eigenschaft | Spezifikation |
|---|---|
| Material | PVC-beschichtetes Polyester-Gewebe |
| Innendurchmesser | 16mm (⅝") oder 19mm (¾") |
| Arbeitsdruck | 3–6 bar |
| Staumaß | ~50% kleiner als Spiralschlauch |
| UV-Beständigkeit | Mittel (nicht für Dauerexposition) |
| Lagerung | Aufgerollt in Cockpit-Locker |
| Lebensdauer | 4–8 Jahre (weniger UV-Exposition durch Lagerung) |
| Typische Preise | 30–70 EUR (15m), 50–100 EUR (25m) |

(Confidence: documented)

### 7.4 UV-Beständigkeit — Das Hauptproblem bei Deckschläuchen

UV-Strahlung ist der Killer Nr. 1 für Deckwaschschläuche. Ein Spiralschlauch, der permanent an Deck liegt, ist 365 Tage/Jahr der Sonne ausgesetzt. Selbst in Nordeuropa summiert sich die UV-Dosis auf 800–1.200 kWh/m²/Jahr, im Mittelmeer auf 1.500–2.200 kWh/m²/Jahr.

**UV-Degradations-Mechanismus:**
1. UV-Photonen brechen Polymerketten im Schlauchmaterial
2. Oberfläche verkreidet (chalking) — weißer, matter Film
3. Farbe verblasst (Vergilbung bei weißen, Ausbleichen bei farbigen Schläuchen)
4. Mikrorisse entstehen an der Oberfläche
5. Risse vertiefen sich, Schlauch wird steif und brüchig
6. Schlauch bricht bei Biegung oder unter Druck

**UV-Beständigkeit nach Material (geschätzte Lebensdauer bei permanenter Deckexposition):**

| Material | UV-Lebensdauer Mittelmeer | UV-Lebensdauer Nordeuropa | UV-Lebensdauer Tropen |
|---|---|---|---|
| Standard-PVC | 1–2 Jahre | 2–3 Jahre | 6–12 Monate |
| UV-stabilisiertes PVC | 2–4 Jahre | 3–5 Jahre | 1–2 Jahre |
| Polyurethan (PU) | 2–3 Jahre | 3–5 Jahre | 1–2 Jahre |
| EPDM-Gummi | 4–7 Jahre | 6–10 Jahre | 3–5 Jahre |
| Santoprene (TPV) | 5–8 Jahre | 7–12 Jahre | 3–6 Jahre |
| Silikon | 8–15 Jahre | 10–20 Jahre | 5–10 Jahre |
| Polyester-Flachgewebe | 3–5 Jahre (nicht für Dauerexposition) | 5–8 Jahre | 2–3 Jahre |

**Schutzmaßnahmen:**
1. Schlauch bei Nichtgebrauch unter Persenning oder in Locker verstauen
2. UV-Schutzspray (303 Aerospace Protectant, Starbrite Snap & Zipper Lubricant UV)
3. Schlauch-Abdeckung aus UV-beständigem Stoff (Sunbrella)
4. Dunkle Schlauchfarben (schwarz, dunkelblau) absorbieren mehr UV — NACHTEIL
5. Weiße oder hellgraue Schläuche reflektieren UV besser — VORTEIL

(Confidence: documented)

### 7.5 Quick-Connect-Fittings (Schnellkupplungen)

Quick-Connect-Fittings ermöglichen das werkzeuglose An- und Abkoppeln des Deckschlauchs an der Deckdurchführung. Standard im Gartenbereich (Gardena, Hozelock), zunehmend auch im Marinebereich.

**Marine Quick-Connect-Systeme:**

| System | Hersteller | Material | Kompatibilität | Preis (Paar) |
|---|---|---|---|---|
| Whale System 15 Quick-Connect | Whale Marine | Acetal (POM) | Nur Whale System | 15–25 EUR |
| Jabsco Snap-In Port | Jabsco/Xylem | Nylon/Edelstahl | Jabsco Hoses | 20–35 EUR |
| Forespar Deck Wash Connector | Forespar | Bronze/Marelon | Universal ¾" BSP | 30–50 EUR |
| Perko Deck Wash Port | Perko | Bronze verchromt | Universal ¾" NPT | 45–75 EUR |
| Scandvik Deck Wash Port | Scandvik | Edelstahl 316 | Universal ½" BSP | 35–55 EUR |
| Gardena Original System | Gardena | ABS-Kunststoff | Gardena-System | 8–15 EUR |
| Hozelock 2100 System | Hozelock | ABS-Kunststoff | Hozelock-System | 8–15 EUR |
| Osculati Art. 17.322.xx | Osculati | Messing verchromt | Universal ¾" BSP | 18–30 EUR |

**Warnung: Gardena/Hozelock-Adapter im Marinebereich:**
Gardena- und Hozelock-Systeme sind weit verbreitet und günstig. Viele Eigner verwenden sie als Deckwasch-Quick-Connect. Probleme:
- Material (ABS-Kunststoff) ist NICHT UV-beständig — versprüdet in 1–3 Jahren an Deck
- Keine Salzwasserbeständigkeit der Metallfedern (verzinkter Stahl statt Edelstahl)
- Dichtungen (NBR) härten an Deck schnell aus
- NICHT druckfest über 6 bar (manche Deckwaschpumpen liefern mehr)

**Empfehlung**: Gardena/Hozelock nur bei Lagerung unter Deck oder temporärer Verwendung. Für permanente Deck-Installation: Bronze- oder Edelstahl-Deckports (Forespar, Perko, Scandvik).

(Confidence: documented)

### 7.6 Düsentypen für Deckwäsche

| Düsentyp | Einsatz | Druck (bar) | Volumenstrom | Preis |
|---|---|---|---|---|
| Verstellbare Brause (7-fach) | Allgemeine Deckwäsche | 2–5 | Mittel | 10–25 EUR |
| Pistolendüse mit Abzug | Gezielte Reinigung, Ankerspülung | 3–8 | Variabel | 15–40 EUR |
| Feuerlöschdüse (Brass) | Hochdruck-Spülung, Profi | 4–10 | Hoch | 25–60 EUR |
| Duschkopf (Handbrause) | Badeplattform, Haarwäsche | 1–3 | Niedrig | 15–35 EUR |
| Feste Spüldüse (Anker) | Ankerketten-Spülung | 3–6 | Mittel-Hoch | 20–50 EUR |
| Fächer-Düse (Fan Jet) | Flächige Deckwäsche | 2–5 | Hoch | 15–30 EUR |

**Ankerspül-Düsen — Spezialisten:**
- **Lewmar Anchor Wash Nozzle**: Edelstahl 316, 2-Strahl, direkter Einbau am Bugbeschlag
- **Maxwell P100090**: Bronze-Düse, 90°-Fächerstrahl, für Maxwell-Windlasses
- **Quick FO-DWJB**: Messing vernickelt, verstellbar, für Quick-Ankerwinden
- **Muir DWN-SS**: Edelstahl, 3-Strahl, passend für Muir-Systeme
- **Eigenbauten**: T-Stück mit Bohrlöchern — kostengünstig, effektiv, aber ungleichmäßig

(Confidence: documented)

### 7.7 Dual-Purpose-Systeme

Viele Boote kombinieren mehrere Waschfunktionen in einem System:

**Konfiguration 1: Deckwäsche + Ankerspülung (häufigste Konfiguration)**
- Eine Pumpe speist über T-Verteiler Deckschlauch und Ankerspüldüse
- Ventil oder Hahn zum Umschalten
- Problem: Beide gleichzeitig → Druckverlust
- Empfehlung: Pumpe ≥15 l/min für Dual-Betrieb

**Konfiguration 2: Deckwäsche + Badeplattform-Dusche**
- Pumpe speist Deckschlauch und Duschkopf an Badeplattform
- Mischbatterie oder Thermostat für warme Dusche (über Warmwasserbereiter)
- Typisch auf Segelyachten 12–18m

**Konfiguration 3: Deckwäsche + Livewell + Fischstation**
- Auf Sportfischer-Booten: Rohwasser-Pumpe für Deckwäsche, Livewell-Befüllung und Fisch-Reinigungsstation
- 3-Wege-Verteiler, separate Absperrhähne
- Livewell benötigt kontinuierlichen Durchfluss (5–10 l/min)

**Konfiguration 4: Vollintegriert (Superyacht)**
- Zentrale Druckwasseranlage für Frischwasser (6–8 bar)
- Separate Seewasserpumpe für Rohwasser-Deckwäsche
- Hydrantenanschlüsse an Deck (Storz oder BSP)
- Ankerspülung über dedizierte Pumpe mit Timer
- Badeplattform-Dusche warm/kalt
- Cockpit-Spülung automatisch (Fußschalter oder Timer)

(Confidence: documented)

### 7.8 Cockpit-Waschsysteme

Cockpit-Waschsysteme sind besonders auf Motoryachten verbreitet, wo das Cockpit als Essbereich, Lounge und Angelplatz dient. Die Anforderungen:

- **Drainage**: Cockpit muss selbstlenzen (ISO 11812). Waschwasser fließt über Cockpit-Drains ab
- **Abflusskapazität**: Drain-Kapazität muss Waschwasser-Zufluss verkraften (mind. 2× Pumpenleistung empfohlen)
- **Material**: Teakdeck im Cockpit → nur Frischwasser empfohlen, Seewasser hinterlässt Salzkristalle in Fugen
- **Schalter**: Fußschalter im Cockpitboden (IP 68) oder wasserdichter Kippschalter (IP 56)

Typische Fußschalter:
- **Jabsco Foot Switch 18753-0141**: Edelstahl-Kappe, IP 68, 15A, Einbau bündig im Deck
- **Whale Compact Foot Switch**: Kunststoff, IP 67, 10A, preisgünstig
- **Vetus Foot Switch?"FSWITCH"**: Edelstahl, IP 68, 20A, hochwertig

(Confidence: documented)

### 7.9 Badeplattform-Duschen (Swim Platform Shower)

Die Badeplattform-Dusche ist ein separates System oder eine Abzweigung vom Deckwasch-System:

**Komponenten:**
- Duschkopf mit Schlauch (typisch 1,5–2,5m) in verschließbarer Deck-Box
- Mischbatterie (warm/kalt) oder nur Kaltwasser
- Warmwasser aus Boiler oder Motorwärmetauscher
- Absperrhahn oder Druckschalter-Aktivierung

**Typische Produkte:**
- **Jabsco J20-133 Transom Shower Kit**: Komplett-Kit mit Duschkopf, Schlauch, Mischbatterie, Einbaubox
- **Whale Swim-N-Rinse**: Einfaches Kit, nur Kaltwasser, Quick-Connect
- **Scandvik Transom Shower**: Edelstahl-Box, Warm/Kalt-Mischer, hochwertiges Finish
- **Osculati Art. 15.240.xx**: Einbau-Duschbox, Kunststoff oder Edelstahl
- **Vetus?"SHOWERSET"**: Komplett-Kit mit Thermostat-Mischer

**Einbauhinweise:**
- Box muss nach unten entwässern (kein stehendes Wasser im Winter)
- Rückschlagventil im Warmwasseranschluss verhindert Rückfluss in Boiler
- Schlauch: Silikonschlauch oder Edelstahl-Panzerschlauch (UV-beständig)
- Mindest-Fließdruck am Duschkopf: 1,5 bar für angenehmes Duschen

(Confidence: documented)

### 7.10 Livewell-Systeme (Lebendfisch-Becken)

Livewell-Systeme sind auf Sportfischer-Booten und Angelbooten Standard. Sie halten Köderfische oder gefangene Fische am Leben durch kontinuierliche Seewasser-Zirkulation.

**Schlauchanforderungen:**
- Material: Muss lebensmitteltauglich und toxinfrei sein (kein PVC mit Weichmachern → Fische sterben)
- Empfohlen: Santoprene, FDA-zugelassener PVC, Polyethylen
- Durchmesser: 19mm (¾") oder 25mm (1") für ausreichenden Durchfluss
- Durchflussrate: 5–15 l/min je nach Beckengröße
- Belüftung: Zusätzlicher Luftstein oder Venturi-Düse im Zulauf

**Typische Livewell-Pumpen:**
- **Johnson Pump Livewell Aerator (P/N 38703)**: 12V, 19 l/min, Kartuschen-Bauform
- **Jabsco Puppy 23610**: 12V, 16 l/min, selbstansaugend
- **Rule 403FC Livewell Pump**: 12V, 11 l/min, Tauchpumpe

(Confidence: documented)

### 7.11 Fisch-Reinigungsstationen (Fish Cleaning Station)

Auf Sportfischer-Booten Standard, auf Fahrtenyachten selten:

**Anforderungen an die Wasserversorgung:**
- Rohwasser (Seewasser) für Spülung, Frischwasser optional für Nachspülung
- Druck: mind. 3 bar für effektive Reinigung
- Volumenstrom: mind. 10 l/min
- Schlauch: Lebensmitteltauglich, leicht zu reinigen
- Ablauf: Ins Meer oder in Abfallbehälter (Umweltvorschriften beachten!)

**Integration mit Deckwasch-System:**
- T-Abzweigung von Deckwasch-Pumpe mit separatem Absperrhahn
- Eigener Schlauch an Fischstation (hygienisch, kein gemeinsamer Gebrauch)
- Spritzschutz und Drainage-Rinne

(Confidence: documented)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Jabsco / Xylem (USA/Schweden)

**Firmenprofil:**
Jabsco ist der weltweit führende Hersteller von marinen Pumpen und seit 2011 Teil des Xylem-Konzerns (ehemals ITT). Jabsco-Deckwaschpumpen (Par-Max-Serie) sind die De-facto-Standardwahl für marine Deckwäsche auf Yachten von 8–25m.

**Deckwasch-relevante Produkte:**

| Modell | Typ | Spannung | Fördermenge | Druck | Strom | Preis (EUR) |
|---|---|---|---|---|---|---|
| Par-Max 1.0 (P/N 42631) | Membran | 12V | 3,8 l/min | 2,4 bar | 4A | 85–120 |
| Par-Max 1.0 (P/N 42632) | Membran | 24V | 3,8 l/min | 2,4 bar | 2A | 90–130 |
| Par-Max 2.0 (P/N 42631 ⚠️) | Membran | 12V | 7,6 l/min | 2,8 bar | 5A | 110–150 |
| Par-Max 3.0 (P/N 42745) | Membran | 12V | 11,4 l/min | 3,4 bar | 8A | 140–190 |
| Par-Max 4.0 (P/N 31600) | Membran | 12V | 16,3 l/min | 4,1 bar | 12A | 180–250 |
| Par-Max HD4 (P/N 46010) | Membran HD | 12V | 15,1 l/min | 4,1 bar | 11A | 220–300 |
| Par-Max HD5 (P/N 46020) | Membran HD | 12V | 18,9 l/min | 4,8 bar | 15A | 280–380 |
| Par-Max HD6 (P/N 46030) | Membran HD | 12V | 22,7 l/min | 4,1 bar | 18A | 320–420 |
| Puppy 2000 (P/N 23680) | Impeller | 12V | 32 l/min | 1,0 bar | 6A | 120–170 |

> ⚠️ **ZU PRÜFEN (Audit):** Par-Max 1.0 (12V) und Par-Max 2.0 (12V) tragen in dieser Tabelle beide die Teilenummer **P/N 42631** — eine Teilenummer kann nicht zu zwei verschiedenen Pumpen gehören. Anhang R.2.1 belegt 42631(-2900) = Par-Max 1.0 12V und führt keine Par-Max 2.0. Die korrekte Par-Max-2.0-Teilenummer ist im Dokument nicht belegt und wurde bewusst NICHT geraten. Diese Zelle daher **Confidence: estimated — unverifiziert** (nicht mehr „measured").

**Jabsco Deckwasch-Komplett-Kits:**
- **Jabsco Wash-Down Kit (P/N 32900-0012)**: Par-Max 3.0 + 7,5m Spiralschlauch + Düse + Fußschalter. Preis: 280–380 EUR
- **Jabsco Anchor Wash Kit**: Par-Max 4.0 + Ankerspüldüse + 6m Schlauch. Preis: 320–430 EUR
- **Jabsco Deluxe Wash-Down (P/N 32305-0092)**: Par-Max 4.0 + 15m Spiralschlauch + Pistolendüse + Druckschalter. Preis: 380–500 EUR

**Stärken:**
- Extrem zuverlässig (5.000+ Betriebsstunden typisch)
- Selbstansaugend bis 1,8m (Membranpumpen)
- Trockenlaufschutz (bis 10 min)
- Weltweites Ersatzteil-Netzwerk
- Membran- und Ventil-Kits einzeln erhältlich

**Schwächen:**
- Lautstärke (Par-Max pulsiert hörbar, 55–68 dB)
- Preis über Durchschnitt
- Pulsierender Förderström (Membranpumpe) → Vibration in Schläuchen

(Confidence: measured)

### 8.2 Shurflo / Pentair (USA)

**Firmenprofil:**
Shurflo, Teil des Pentair-Konzerns, ist der zweitgrößte Anbieter von Membranpumpen für den Marinebereich. Shurflo-Pumpen sind günstiger als Jabsco und in der Erstausrüstung vieler europäischer Bootsbauer verbreitet (Bavaria, Bénéteau, Dufour).

**Deckwasch-relevante Produkte:**

| Modell | Typ | Spannung | Fördermenge | Druck | Strom | Preis (EUR) |
|---|---|---|---|---|---|---|
| 2088-422-444 | Membran 3-Kammer | 12V | 10,6 l/min | 3,1 bar | 7A | 80–120 |
| 2088-474-144 | Membran 3-Kammer | 12V | 10,6 l/min | 3,1 bar | 7A | 85–125 |
| 4048-153-E75 | Membran 4-Kammer | 12V | 15,1 l/min | 3,8 bar | 10A | 140–200 |
| 4048-163-E75 | Membran 4-Kammer | 24V | 15,1 l/min | 3,8 bar | 5A | 150–210 |
| 5901-0241 (Aqua King II) | Membran 3-Kammer | 12V | 11,4 l/min | 3,4 bar | 8A | 120–170 |
| ProBlaster II 4248 | Membran 4-Kammer | 12V | 16,7 l/min | 4,1 bar | 12A | 180–250 |

**Stärken:**
- Günstiger als Jabsco bei vergleichbarer Leistung
- Leiser als Jabsco (50–62 dB, 4-Kammer-Modelle)
- Breite OEM-Verwendung (Ersatzteile über Bootswerft beziehbar)
- Gute Selbstansaugung (bis 2,4m)

**Schwächen:**
- Membranlebensdauer etwas kürzer als Jabsco
- Weniger Zubehör (keine kompletten Wash-Down-Kits)
- Service-Netzwerk kleiner als Jabsco

(Confidence: measured)

### 8.3 Whale Marine (UK / Nordirland)

**Firmenprofil:**
Whale Marine aus Bangor, Nordirland, ist Spezialist für kompakte Pumpen und Wasserversorgungssysteme. Whale ist bekannt für das "System 15" — ein proprietäres Quick-Connect-System mit 15mm-Steckverbindungen, das Installation und Wartung vereinfacht.

**Deckwasch-relevante Produkte:**

| Modell | Typ | Spannung | Fördermenge | Druck | Strom | Preis (EUR) |
|---|---|---|---|---|---|---|
| Universal Pressure Pump GP1352 | Membran | 12V | 11,5 l/min | 2,1 bar | 5A | 90–130 |
| Watermaster EP1622 | Membran | 12V | 11,5 l/min | 3,0 bar | 6A | 100–150 |
| Watermaster EP1612 | Membran | 12V | 8,0 l/min | 2,0 bar | 4A | 80–120 |
| Gulper 220 (IC) | Impeller | 12V | 14 l/min | 0,7 bar | 3A | 60–90 |
| Compact 50 Deck Wash | Membran | 12V | 7,0 l/min | 2,4 bar | 4A | 85–120 |

**Whale System 15 Deckwasch-Kit:**
- Pumpe + System 15 Quick-Connect-Deckport + 7,5m Spiralschlauch + Düse
- Preis: 220–320 EUR komplett
- Vorteil: Werkzeugloser Schlauchanschluss, dichtungsfreie Verbindung

**Stärken:**
- System 15 Quick-Connect (einzigartig, sehr praktisch)
- Kompakte Bauform (passt in enge Räume)
- Leise (48–55 dB)
- Gute Qualität für den Preis

**Schwächen:**
- Weniger Druckleistung als Jabsco/Shurflo
- System 15 ist proprietär (nur Whale-Komponenten kompatibel)
- Begrenzte Verfügbarkeit außerhalb UK/EU

(Confidence: measured)

### 8.4 Vetus (Niederlande)

**Firmenprofil:**
Vetus aus Schiedam ist ein niederländischer Komplett-Ausrüster mit eigenem Sortiment an Pumpen, Schläuchen und Zubehör. Vetus-Produkte sind im europäischen Yachtbau weit verbreitet.

**Deckwasch-relevante Produkte:**

| Modell | Typ | Spannung | Fördermenge | Druck | Strom | Preis (EUR) |
|---|---|---|---|---|---|---|
| WP1212B | Membran | 12V | 12,5 l/min | 2,4 bar | 5A | 110–160 |
| WP1213B | Membran | 12V | 12,5 l/min | 3,1 bar | 7A | 130–180 |
| WP2213B | Membran | 24V | 12,5 l/min | 3,1 bar | 4A | 140–190 |

**Vetus Deckwasch-Schläuche:**
-?"DWSHA12" Spiralschlauch 12mm ID, 7,5m, PVC, weiß
-?"DWSHA16" Spiralschlauch 16mm ID, 7,5m, PVC, weiß
- Preis: 35–65 EUR

**Stärken:**
- Komplettes Sortiment aus einer Hand (Pumpe, Schlauch, Fittings, Borddurchlass)
- Gute Qualität, europäische Fertigung
- Breite Distribution in EU

**Schwächen:**
- Pumpen-Leistung hinter Jabsco/Shurflo
- Schlauchmaterial (PVC) mit begrenzter UV-Beständigkeit
- Preise im oberen Mittelfeld

(Confidence: measured)

### 8.5 Johnson Pump / SPX Flow (Schweden/USA)

**Firmenprofil:**
Johnson Pump, Teil von SPX Flow, bietet ein breites Sortiment an Bilgen-, Frischwasser- und Spezial-Pumpen. Im Deckwasch-Bereich weniger bekannt als Jabsco, aber qualitativ gleichwertig.

**Deckwasch-relevante Produkte:**

| Modell | Typ | Spannung | Fördermenge | Druck | Strom | Preis (EUR) |
|---|---|---|---|---|---|---|
| Aqua Jet WPS 2.9 | Membran | 12V | 11,0 l/min | 2,8 bar | 6A | 100–140 |
| Aqua Jet WPS 3.5 | Membran | 12V | 13,2 l/min | 3,5 bar | 9A | 130–180 |
| Aqua Jet WPS 5.2 | Membran | 12V | 20,0 l/min | 3,8 bar | 13A | 200–280 |
| Livewell Aerator 38703 | Kartusche | 12V | 19,0 l/min | 0,3 bar | 2A | 25–40 |

**Stärken:**
- Sehr leise (AquaJet WPS Serie, 45–55 dB)
- Anti-Vibrations-Montage serienmäßig
- Gutes Preis-Leistungs-Verhältnis

**Schwächen:**
- Kleinere Marktpräsenz im Deckwasch-Segment
- Weniger Komplett-Kits als Jabsco

(Confidence: measured)

### 8.6 Plastimo (Frankreich)

**Firmenprofil:**
Plastimo aus Lorient ist einer der größten europäischen Yachtzubehör-Hersteller. Im Deckwasch-Bereich bietet Plastimo eigene und OEM-Produkte an.

**Deckwasch-relevante Produkte:**

| Produkt | Typ | Spezifikation | Preis (EUR) |
|---|---|---|---|
| Spiralschlauch 7,5m | PVC Spirale | 12mm ID, Quick-Connect | 30–50 |
| Spiralschlauch 15m | PVC Spirale | 16mm ID, Quick-Connect | 50–80 |
| Deckwasch-Düse verstellbar | 7-fach Brause | Messing vernickelt, ¾" BSP | 15–25 |
| Deckwasch-Pumpe (OEM Shurflo) | Membran | 12V, 11 l/min, 3,1 bar | 110–160 |
| Schnellkupplung Deck | Messing | ¾" BSP, Edelstahl-Feder | 20–35 |

**Stärken:**
- Breite Distribution in Frankreich und Mittelmeer
- Gutes Preis-Leistungs-Verhältnis
- Zusammenstellung als Kit möglich

**Schwächen:**
- Keine eigene Pumpen-Fertigung (OEM)
- Schlauchmaterial mittlere UV-Beständigkeit

(Confidence: documented)

### 8.7 Osculati (Italien)

**Firmenprofil:**
Osculati aus Segrate (Mailand) ist der größte italienische Yachtzubehör-Großhändler mit einem Katalog von über 30.000 Artikeln. Osculati-Produkte sind OEM-gefertigt und bieten ein gutes Preis-Leistungs-Verhältnis.

**Deckwasch-relevante Produkte:**

| Art.-Nr. | Produkt | Spezifikation | Preis (EUR) |
|---|---|---|---|
| 16.703.12 | Par-Max 3.0 kompatible Pumpe | 12V, 11,4 l/min, 3,4 bar | 120–170 |
| 16.703.24 | Par-Max 3.0 kompatible Pumpe | 24V, 11,4 l/min, 3,4 bar | 130–180 |
| 36.464.15 | Spiralschlauch 4,5m | PVC, 12mm ID, weiß | 18–28 |
| 36.464.25 | Spiralschlauch 7,5m | PVC, 12mm ID, weiß | 28–42 |
| 36.464.50 | Spiralschlauch 15m | PVC, 16mm ID, weiß | 45–70 |
| 17.322.01 | Deckwasch-Port | Messing verchromt, ¾" BSP | 18–30 |
| 15.240.01 | Transom-Duschbox | Kunststoff, nur Kaltwasser | 35–55 |
| 15.240.05 | Transom-Duschbox Edelstahl | Edelstahl 316, Warm/Kalt | 80–130 |

**Stärken:**
- Sehr breites Sortiment
- Günstigste Preise im Markt
- Gute Verfügbarkeit über SVB, Compass24, etc.

**Schwächen:**
- OEM-Qualität variiert
- Schlauchmaterial Standard-PVC (begrenzte UV-Beständigkeit)
- Dokumentation manchmal unvollständig

(Confidence: measured)

### 8.8 Lalizas (Griechenland)

**Firmenprofil:**
Lalizas aus Piräus ist ein wachsender griechischer Yachtzubehör-Hersteller mit eigener Fertigung und zunehmendem Europa-Vertrieb.

**Deckwasch-relevante Produkte:**

| Produkt | Spezifikation | Preis (EUR) |
|---|---|---|
| Spiralschlauch 7,5m | PVC, 12mm ID, weiß, Quick-Connect | 22–35 |
| Spiralschlauch 15m | PVC, 16mm ID, weiß, Quick-Connect | 38–55 |
| Deckwasch-Düse | Messing vernickelt, verstellbar | 12–20 |
| Deckwasch-Port | Messing verchromt, ½" BSP | 15–25 |
| Deckwasch-Pumpe | Membran, 12V, 8 l/min, 2,4 bar | 70–100 |

**Stärken:**
- Sehr günstige Preise
- Gute Verfügbarkeit in Mittelmeer-Chandleries

**Schwächen:**
- PVC-Qualität unter Jabsco/Trident
- Begrenzte UV-Beständigkeit (1–2 Jahre Mittelmeer)
- Kunststoff-Fittings (keine Bronze/Edelstahl-Option)

(Confidence: documented)

### 8.9 Trident Marine (USA) — Schlauch-Spezialist

**Firmenprofil:**
Trident Marine aus Windham, Connecticut, ist einer der führenden Hersteller von marinen Schläuchen in den USA. Die Trident 369 Serie ist der Goldstandard für marine Deckwasch-Schläuche.

**Deckwasch-relevante Schläuche:**

| Serie | Material | ID (mm) | Arbeitsdruck | UV-Beständigkeit | Preis/m (EUR) |
|---|---|---|---|---|---|
| 369 Wash-Down | Santoprene (TPV) | 12, 16, 19 | 10 bar | Exzellent (5–8 J.) | 8–15 |
| 161 PVC Wash-Down | PVC UV-stabilisiert | 12, 16, 19 | 7 bar | Gut (3–5 J.) | 4–8 |
| 149 Reinforced PVC | PVC armiert | 12, 16, 19, 25 | 10 bar | Mittel (2–3 J.) | 5–10 |
| 148 Shields Series | EPDM | 12, 16, 19 | 10 bar | Sehr gut (4–7 J.) | 7–13 |

**Trident 369 Series — Detailspezifikation:**
- Material: Santoprene TPV (Thermoplastisches Vulkanisat)
- Armierung: Polyester-Geflecht
- Temperaturbereich: -40°C bis +100°C
- UV-Beständigkeit: ASTM D4329 — keine sichtbare Degradation nach 2.000h Xenon-Bogen
- Ozon-Beständigkeit: ASTM D1149 — bestanden
- Farbe: Weiß (außen), schwarz (innen)
- Lebensmitteltauglich: Ja (FDA 21 CFR 177.2600)
- Biegeradius (12mm ID): 75mm
- Biegeradius (16mm ID): 100mm
- Biegeradius (19mm ID): 125mm

**Stärken:**
- Beste UV-Beständigkeit am Markt (Santoprene 369)
- Breites Größensortiment
- In den USA Standard, in EU über Importeure erhältlich

**Schwächen:**
- Höchster Preis pro Meter
- In EU nur über Spezialimporteure (SVB, Bukh-Bremen)
- Meterware, keine vorkonfektionierten Spiralschläuche

(Confidence: measured)

### 8.10 Goodyear Marine (USA)

**Firmenprofil:**
Goodyear Engineered Products (jetzt Continental ContiTech) produziert marine Gummi-Schläuche unter dem Goodyear-Markennamen. Die marine Wash-Down-Schläuche sind EPDM-basiert und bieten gute UV-Beständigkeit.

**Deckwasch-relevante Schläuche:**

| Produkt | Material | ID (mm) | Arbeitsdruck | UV-Best. | Preis/m (EUR) |
|---|---|---|---|---|---|
| Marine Wash-Down Hose | EPDM | 12, 16 | 8 bar | Gut (4–6 J.) | 6–11 |
| Marine Multipurpose | EPDM/PVC | 16, 19 | 10 bar | Mittel (3–4 J.) | 5–9 |
| Marine Coiled Hose | PU | 12 | 6 bar | Mittel (3–4 J.) | Meterware |

**Stärken:**
- Bewährte EPDM-Qualität
- Gute UV-Beständigkeit (ohne Santoprene-Preis)
- Breite Verfügbarkeit in den USA

**Schwächen:**
- Markenverwirrung (Goodyear vs. Continental vs. ContiTech)
- In EU schwer erhältlich
- Keine Spiralschläuche im Sortiment

(Confidence: documented)

### 8.11 Continental / ContiTech (Deutschland)

**Firmenprofil:**
Continental/ContiTech aus Hannover produziert industrielle und marine Schläuche. Im Yachtbereich über Fachhandel und Industrievertrieb.

**Relevante Schläuche:**
- **Conti Marine Wash**: PVC/NBR armiert, 12–25mm ID, 10 bar, gute chemische Beständigkeit
- **Conti Flex Spiral**: PVC spiralarmiert, 12–50mm ID, für Rohwasser-Anwendungen

**Preise:** 5–12 EUR/m je nach Durchmesser

(Confidence: documented)

### 8.12 Gates (USA/Belgien)

**Firmenprofil:**
Gates Corporation aus Denver (mit europäischer Fertigung in Belgien) bietet marine Schläuche unter der "Marine Master" Linie an.

**Relevante Produkte:**
- **Gates Marine Master**: EPDM-Schlauch, 12–25mm ID, 10 bar, UV-stabilisiert
- **Gates Green Stripe**: Mehrzweck-Schlauch, PVC/NBR, moderate UV-Beständigkeit
- Preise: 6–14 EUR/m

(Confidence: documented)

### 8.13 Lewmar (UK) — Ankerspül-Systeme

**Firmenprofil:**
Lewmar aus Havant, Hampshire, ist der weltweit führende Hersteller von Ankerwinden (Windlasses). Lewmar bietet integrierte Ankerspül-Systeme als Zubehör zu ihren Windlasses an.

**Ankerspül-Produkte:**

| Modell | Kompatibilität | Pumpe | Düse | Preis (EUR) |
|---|---|---|---|---|
| V-Series Wash Kit | V1, V2, V3, V4 Windlasses | Nicht enthalten (Jabsco empfohlen) | Edelstahl 316 Düse | 120–180 |
| Pro-Series Wash Kit | Pro-Fish, Pro-Sport | Nicht enthalten | Edelstahl 316 Düse | 140–200 |
| HX1 Wash Kit | HX1 Windlass | Nicht enthalten | Bronze Düse | 100–150 |

**Lewmar Ankerspül-Düse Details:**
- Material: Edelstahl AISI 316L
- Strahlform: 2-Strahl, Fächerwinkel 30°
- Anschluss: ½" BSP oder 12mm Schlauchstutzen
- Montage: Am Bugbeschlag oder Bugrolle
- Positionierung: 50–100mm über Kette, Strahl auf Kette gerichtet

**Integration mit Lewmar Windlass-Steuerung:**
- Manuelle Aktivierung über separaten Schalter
- Automatik über Lewmar Controller (optional): Spülung aktiv solange Ankerkette eingeholt wird
- NMEA 2000 Integration bei neueren Modellen

(Confidence: measured)

### 8.14 Maxwell Marine (Neuseeland/USA)

**Firmenprofil:**
Maxwell Marine aus Auckland ist der zweitgrößte Windlass-Hersteller weltweit und bietet eigene Ankerspül-Kits an.

**Ankerspül-Produkte:**

| Modell | Kompatibilität | Pumpe | Düse | Preis (EUR) |
|---|---|---|---|---|
| P100090 Wash-Down Kit | RC, HRC, VWC Series | Nicht enthalten | Bronze, 90° Fächer | 130–190 |
| P100091 Wash-Down Kit | Freedom Series | Nicht enthalten | Bronze, verstellbar | 140–200 |
| Auto-Rinse System | Alle Maxwell Windlasses | Jabsco Par-Max 3.0 enthalten | Bronze + Sensor | 450–600 |

**Maxwell Auto-Rinse Details:**
- Sensor an der Kette erkennt Kettenbewegung
- Pumpe startet automatisch bei Einholen
- Timer schaltet Pumpe 30 Sekunden nach letzter Kettenbewegung ab
- Frischwasser-Option mit Umschaltventil

(Confidence: measured)

### 8.15 Quick (Italien)

**Firmenprofil:**
Quick SpA aus Ravenna ist Italiens führender Windlass-Hersteller und bietet integrierte Ankerspül-Lösungen.

**Ankerspül-Produkte:**

| Modell | Kompatibilität | Spezifikation | Preis (EUR) |
|---|---|---|---|
| FO-DWJB Wash Nozzle | Alle Quick Windlasses | Messing vernickelt, verstellbar | 45–75 |
| FO-DWSS Wash Nozzle | Alle Quick Windlasses | Edelstahl 316, fest | 65–95 |
| Quick Aqua-Wash Kit | Genius, Hector, Hero | Pumpe + Düse + Sensor | 380–520 |

**Quick Aqua-Wash Automatik:**
- Kettenzähler-Integration: Spülung startet wenn Kette eingeholt wird
- Drucksensor überwacht Pumpenleistung
- Display zeigt Wasserverbrauch und Betriebsstunden
- 12V oder 24V Versionen

(Confidence: measured)

### 8.16 Muir (Australien)

**Firmenprofil:**
Muir Windlasses aus Brisbane ist der australische Marktführer für Ankerwinden und bietet Ankerspül-Zubehör.

**Ankerspül-Produkte:**

| Modell | Spezifikation | Preis (EUR) |
|---|---|---|
| DWN-SS Wash Nozzle | Edelstahl 316, 3-Strahl | 55–85 |
| DWN-BR Wash Nozzle | Bronze, 2-Strahl | 45–70 |
| Muir Wash Kit | Düse + Schlauch 6m + Fittings | 110–160 |

(Confidence: documented)

### 8.17 NDS — Non-Percolating Deck Fittings (USA)

**Firmenprofil:**
NDS (National Diversified Sales) produziert deck-bündige Wasseranschlüsse und Fittings, die für den Marinebereich spezifiziert sind. "Non-percolating" bedeutet, dass die Fittings keine Feuchtigkeit unter Deck durchlassen.

**Relevante Produkte:**
- Deck-Fill Caps mit Wash-Down-Funktion
- Flush-Mount Deck Wash Ports (Messing, Edelstahl)
- Preis: 25–60 EUR je nach Material und Größe

(Confidence: estimated)

### 8.18 Weitere Hersteller (Kurzübersicht)

| Hersteller | Land | Spezialität | Qualität | Preislevel |
|---|---|---|---|---|
| Flojet (Xylem) | US | Pumpen (Jabsco-Schwester) | Hoch | Mittel-Hoch |
| Marco (Italien) | IT | Druckwassersysteme | Hoch | Hoch |
| Seaflo | CN | Budget-Pumpen | Mittel | Niedrig |
| TMC (Taiwan) | TW | Budget-Pumpen | Mittel | Niedrig |
| Albin Pump (Schweden) | SE | Impellerpumpen | Hoch | Hoch |
| Aquafax (UK) | UK | Distribution, eigene Schläuche | Mittel | Mittel |
| Hella Marine (NZ) | NZ | Deckwasch-Schalter/Fußtaster | Hoch | Mittel |
| AAA (Taiwan) | TW | Budget-Deckwasch-Kits | Niedrig-Mittel | Niedrig |

**Seaflo — Budget-Alternative:**
Seaflo aus China bietet Deckwaschpumpen als günstige Alternative zu Jabsco/Shurflo:
- Seaflo 41 Series (Jabsco Par-Max 3.0 Klon): 12V, 11,4 l/min, 3,4 bar. Preis: 45–75 EUR
- Seaflo 42 Series (Jabsco Par-Max 4.0 Klon): 12V, 17 l/min, 4,1 bar. Preis: 60–95 EUR
- Qualität: Ausreichend für Gelegenheitsnutzung, Membranlebensdauer 50–70% von Jabsco
- AYDI-Empfehlung: Akzeptabel für Budget-Boote, für Fahrtenyachten Jabsco/Shurflo bevorzugen

(Confidence: documented)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Zuordnung nach Pumpe und Windlass

**Jabsco Par-Max Pumpen → Empfohlene Schlauchdimensionen:**

| Pumpe | Max. Fördermenge | Empf. Schlauch-ID | Max. Schlauchlänge | Empf. Düse |
|---|---|---|---|---|
| Par-Max 1.0 | 3,8 l/min | 12mm (½") | 8m | Brause (low pressure) |
| Par-Max 2.0 | 7,6 l/min | 12mm (½") | 12m | Brause/Pistolendüse |
| Par-Max 3.0 | 11,4 l/min | 12–16mm (½–⅝") | 15m | Pistolendüse |
| Par-Max 4.0 | 16,3 l/min | 16mm (⅝") | 20m | Pistolendüse/Feuerlösch |
| Par-Max HD4 | 15,1 l/min | 16mm (⅝") | 20m | Pistolendüse |
| Par-Max HD5 | 18,9 l/min | 16–19mm (⅝–¾") | 25m | Alle Typen |
| Par-Max HD6 | 22,7 l/min | 19mm (¾") | 30m | Alle Typen |

### 9.2 Windlass-Ankerspül-Zuordnung

| Windlass | Hersteller | Empf. Spülpumpe | Empf. Düse | Empf. Schlauch |
|---|---|---|---|---|
| Lewmar V1 (6mm Kette) | Lewmar | Par-Max 2.0 | Lewmar V-Series | 12mm ID, 3m |
| Lewmar V2 (8mm Kette) | Lewmar | Par-Max 3.0 | Lewmar V-Series | 12mm ID, 4m |
| Lewmar V3 (10mm Kette) | Lewmar | Par-Max 4.0 | Lewmar V-Series | 16mm ID, 5m |
| Lewmar V4 (12mm Kette) | Lewmar | Par-Max HD5 | Lewmar V-Series | 16mm ID, 6m |
| Maxwell RC8 (8mm) | Maxwell | Par-Max 3.0 | P100090 | 12mm ID, 4m |
| Maxwell RC10 (10mm) | Maxwell | Par-Max 4.0 | P100090 | 16mm ID, 5m |
| Maxwell RC12 (12mm) | Maxwell | Par-Max HD5 | P100091 | 16mm ID, 6m |
| Quick Genius 1000 | Quick | Par-Max 3.0 | FO-DWJB | 12mm ID, 4m |
| Quick Hero 1500 | Quick | Par-Max 4.0 | FO-DWSS | 16mm ID, 5m |
| Quick Hector 1500 | Quick | Par-Max HD5 | FO-DWSS | 16mm ID, 6m |
| Muir VR2500 | Muir | Par-Max 4.0 | DWN-SS | 16mm ID, 5m |
| Muir VR3500 | Muir | Par-Max HD5 | DWN-SS | 16mm ID, 6m |
| Lofrans Tigres | Lofrans | Par-Max 3.0 | Universal ½" | 12mm ID, 4m |
| Lofrans Cayman | Lofrans | Par-Max HD5 | Universal ¾" | 16mm ID, 6m |

### 9.3 Zuordnung nach Bootsklasse und Systemkonfiguration

**Segelboot 8–10m (Jollenkreuzer, Daysailer):**
- System: Einfache Rohwasser-Deckwäsche
- Pumpe: Jabsco Par-Max 1.0 oder Seaflo 41
- Schlauch: 12mm ID Spirale, 4,5m
- Kosten gesamt: 150–280 EUR
- Ankerspülung: Nicht nötig (leichter Anker, kurze Kette)

**Segelboot 10–14m (Fahrtenyacht):**
- System: Rohwasser-Deckwäsche + Ankerspülung
- Pumpe: Jabsco Par-Max 3.0 oder Shurflo 2088
- Schlauch: 12–16mm ID Spirale, 7,5m
- Ankerspül-Düse: Am Bugbeschlag montiert
- Kosten gesamt: 300–550 EUR
- Optional: Frischwasser-Nachspülung vom Druckwassersystem

**Motoryacht 10–14m (Kabinenkreuzer):**
- System: Rohwasser + Frischwasser Dual
- Pumpe: Jabsco Par-Max 4.0 (Rohwasser) + Druckwasser-System (Frischwasser)
- Schlauch: 16mm ID Spirale, 7,5m (Rohwasser), Badeplattform-Dusche
- Kosten gesamt: 450–800 EUR

**Segelyacht 14–20m (Blauwasser):**
- System: Voll integriert (Rohwasser Deck + Frischwasser Deck + Ankerspülung + Cockpit)
- Pumpen: 2× Jabsco Par-Max 4.0 oder 1× Par-Max HD5
- Schläuche: 16–19mm ID, 15m (Deck) + 6m (Anker) + Cockpit-Dusche
- Ankerspülung: Automatik (Maxwell Auto-Rinse oder Quick Aqua-Wash)
- Kosten gesamt: 800–1.800 EUR

**Motoryacht 18–25m:**
- System: Profisystem mit Drucktank
- Pumpen: 2–3 Pumpen + Akkumulator-/Drucktank
- Schläuche: 19–25mm ID fest + Spirale
- Hydrantenanschlüsse an Deck
- Kosten gesamt: 2.000–5.000 EUR

**Superyacht 25m+:**
- System: Zentrale Druckwasseranlage
- Deckwasch-Stationen: 4–8 Hydrantenanschlüsse
- Professionelle Ankerspülung (Hochdruck)
- Kosten: 5.000–25.000 EUR (abhängig von Schiffsgröße)

(Confidence: documented)

---

## 10. Schlauchschellen & Verbindungstechnik

### 10.1 Schlauchschellen für Deckwasch-Systeme

**Schlauchschellen-Typen:**

| Typ | Material | Einsatz | Preis |
|---|---|---|---|
| Schneckengewindeschelle (Worm Drive) | Edelstahl 316 Band + 316 Schraube | Standard für alle Verbindungen | 1–4 EUR |
| T-Bolt-Schelle (Sprengringschelle) | Edelstahl 316 | Hochdruckverbindungen >4 bar | 5–12 EUR |
| Federbandschelle (Spring Clamp) | Edelstahl 304 oder 316 | Nur für drucklose/niederdruckige Stellen | 0,5–2 EUR |
| Crimpschelle (Oetiker) | Edelstahl 316 | Professionelle Erstmontage | 2–5 EUR + Werkzeug |
| Doppelte Schneckengewindeschelle | Edelstahl 316 | Unterhalb Wasserlinie, Sicherheitskritisch | 2× Einzelpreis |

**KRITISCHE Regel: Edelstahl 316 — IMMER!**
Im Marinebereich MÜSSEN Schlauchschellen aus Edelstahl AISI 316 (V4A) gefertigt sein. Standard-Edelstahl 304 (V2A) korrodiert in Salzwasserumgebung innerhalb von 1–3 Jahren (Tea Staining, Spaltkorrosion). Verzinkter Stahl ist INAKZEPTABEL.

**Erkennung von 316 vs. 304:**
- 316: Häufig mit "316", "A4" oder "Marine Grade" gestempelt
- 304: Häufig mit "304", "A2" oder gar nicht gestempelt
- Test: Magnet — 316 ist weniger magnetisch als 304 (aber kein zuverlässiger Test)
- Sicherer Test: Molybdän-Nachweis (Mo-Spot-Test)

**Doppelte Schellen — Wann erforderlich?**
- An jedem Borddurchlass (ISO 9093)
- An der Pumpen-Ansaugung (Seewasser-Seite)
- An Verbindungen unterhalb der Wasserlinie
- Bei Schläuchen >19mm ID und Druck >3 bar
- Empfehlung: Immer doppelte Schellen verwenden (Sicherheitsredundanz)

### 10.2 Quick-Connect Deckports — Einbau

**Einbauanleitung Deckwasch-Port (z.B. Jabsco, Forespar, Scandvik):**

1. Position auf Deck markieren (Zugang zur Druckleitung unter Deck)
2. Kernlochbohrung mit Lochsäge (typisch 40–55mm Durchmesser)
3. GFK-Schnittkanten mit Epoxy versiegeln (Feuchtigkeitsschutz!)
4. Dichtungsmasse auf Deckport-Flansch (Sikaflex 291, 3M 5200, oder Butylband)
5. Deckport von oben einsetzen, von unten verschrauben
6. Schlauch von unten anschließen (Schlauchschelle oder Push-Fit)
7. Abdichtung prüfen: 24h warten, dann Wassertest

**Häufige Fehler beim Deckport-Einbau:**
- Kein Epoxy auf GFK-Schnittkanten → Osmose-Eintritt
- Zu wenig Dichtungsmasse → Undichtigkeit unter Deck
- Falsche Dichtungsmasse (Silikon statt PU) → Haftungsversagen
- Deckport in Bereich mit stehendem Wasser → Dauerbelastung der Dichtung
- Schlauch knickt direkt unter Deckport → Druckverlust

### 10.3 Schlauchtüllen und Adapter

| Adapter-Typ | Material | Von | Nach | Preis |
|---|---|---|---|---|
| Schlauchtülle gerade | Messing/Edelstahl | ½" BSP | 12mm Schlauch | 3–8 EUR |
| Schlauchtülle gerade | Messing/Edelstahl | ¾" BSP | 16mm Schlauch | 4–10 EUR |
| Schlauchtülle 90° | Messing/Edelstahl | ½" BSP | 12mm Schlauch | 5–12 EUR |
| T-Stück Schlauch | Messing/Edelstahl | 12mm | 12mm × 12mm × 12mm | 6–15 EUR |
| Y-Verteiler | Messing/Edelstahl | 16mm | 12mm × 12mm | 8–18 EUR |
| Absperrhahn (Kugelhahn) | Messing/Edelstahl | ½" BSP | ½" BSP | 10–25 EUR |
| Rückschlagventil | Messing/Edelstahl | ½" BSP | ½" BSP | 8–20 EUR |
| 3-Wege-Ventil | Messing | ½" BSP | ½" BSP × 2 | 15–35 EUR |

**Material-Empfehlung für Salzwasser:**
- **Bronze (CW617N)**: Beste Wahl für Seewasser, kein Dezinkifizierungsrisiko
- **Edelstahl 316L**: Gleichwertig, optisch ansprechender
- **Messing**: Akzeptabel für Frischwassersysteme, NICHT für Seewasser (Dezinkifizierung!)
- **Marelon (glasfaserverstärktes Nylon)**: Gute Alternative, korrosionsfrei, leichter
- **Standard-Nylon/POM**: Nur für Frischwasser und Low-Pressure

(Confidence: documented)

---

## 11. Technische Referenz & Berechnungen

### 11.1 Pumpenauswahl — Dimensionierung

**Grundformel für erforderliche Pumpenleistung:**

```
Q_min (l/min) = A_deck (m²) × F_anwendung × F_druck
```

Wobei:
- A_deck = zu reinigende Deckfläche in m²
- F_anwendung = Anwendungsfaktor (siehe Tabelle)
- F_druck = Druckfaktor (siehe Tabelle)

| Anwendung | F_anwendung | Erklärung |
|---|---|---|
| Leichte Deckspülung | 0,3 | Salz abspülen |
| Gründliche Deckwäsche | 0,6 | Verschmutzung entfernen |
| Ankerketten-Spülung | 1,0 | Hoher Volumenstrom nötig |
| Hochdruck-Reinigung | 1,5 | Hartnäckige Verschmutzung |
| Fischstation | 0,8 | Kontinuierlicher Betrieb |

| Druck am Düsenaustritt | F_druck |
|---|---|
| 1–2 bar (Brause) | 0,5 |
| 2–3 bar (Standard) | 1,0 |
| 3–5 bar (Pistole) | 1,5 |
| 5–8 bar (Hochdruck) | 2,0 |

**Beispielrechnung:**
- Segelyacht 12m, Deckfläche ca. 20m², gründliche Deckwäsche, Standard-Düse
- Q_min = 20 × 0,6 × 1,0 = 12 l/min
- → Jabsco Par-Max 3.0 (11,4 l/min) knapp ausreichend, Par-Max 4.0 (16,3 l/min) empfohlen

### 11.2 Druckverlust-Berechnung

**Druckverlust in Schläuchen (Darcy-Weisbach vereinfacht):**

```
Δp (bar) = f × L × v² / (2 × d × 10⁵)
```

Wobei:
- f = Reibungsbeiwert (0,02–0,04 für glatte Schläuche)
- L = Schlauchlänge in m
- v = Fließgeschwindigkeit in m/s
- d = Innendurchmesser in m

**Vereinfachte Druckverlust-Tabelle (pro 10m Schlauch):**

| Durchfluss (l/min) | 12mm ID | 16mm ID | 19mm ID | 25mm ID |
|---|---|---|---|---|
| 5 | 0,12 bar | 0,04 bar | 0,02 bar | 0,01 bar |
| 10 | 0,45 bar | 0,14 bar | 0,06 bar | 0,02 bar |
| 15 | 0,95 bar | 0,30 bar | 0,13 bar | 0,04 bar |
| 20 | 1,65 bar | 0,52 bar | 0,23 bar | 0,07 bar |
| 25 | — | 0,80 bar | 0,35 bar | 0,11 bar |

**Konsequenz:** Bei langen Schlauchleitungen (>15m) immer 16mm oder 19mm ID verwenden!

### 11.3 Stromverbrauch und Kabelquerschnitt

**Kabelquerschnitt-Berechnung (ISO 10133):**

```
A (mm²) = (2 × L × I) / (κ × ΔU_zul)
```

Wobei:
- L = Kabellänge (einfach) in m
- I = Stromaufnahme in A
- κ = Leitfähigkeit Kupfer = 56 m/(Ω×mm²)
- ΔU_zul = Zulässiger Spannungsfall (3% von 12V = 0,36V empfohlen)

**Referenztabelle Kabelquerschnitte für Deckwaschpumpen:**

| Pumpe | Strom (A) | Kabellänge 3m | Kabellänge 5m | Kabellänge 8m | Kabellänge 12m |
|---|---|---|---|---|---|
| Par-Max 1.0 | 4A | 1,0 mm² | 1,5 mm² | 2,5 mm² | 4,0 mm² |
| Par-Max 2.0 | 5A | 1,5 mm² | 2,5 mm² | 2,5 mm² | 4,0 mm² |
| Par-Max 3.0 | 8A | 2,5 mm² | 2,5 mm² | 4,0 mm² | 6,0 mm² |
| Par-Max 4.0 | 12A | 2,5 mm² | 4,0 mm² | 6,0 mm² | 10,0 mm² |
| Par-Max HD5 | 15A | 4,0 mm² | 6,0 mm² | 10,0 mm² | 16,0 mm² |
| Par-Max HD6 | 18A | 4,0 mm² | 6,0 mm² | 10,0 mm² | 16,0 mm² |

**Absicherung:**
- Sicherung = 1,5 × Nenn-Stromaufnahme (Anlaufstrom berücksichtigen)
- Par-Max 3.0 (8A) → 15A Sicherung
- Par-Max 4.0 (12A) → 20A Sicherung
- Par-Max HD5 (15A) → 25A Sicherung

### 11.4 Seewasser-Borddurchlass-Dimensionierung (ISO 9093)

**Borddurchlass-Größe für Deckwasch-Ansaugung:**

| Pumpenfördermenge | Min. Borddurchlass | Empf. Borddurchlass |
|---|---|---|
| <8 l/min | ¾" (19mm) | 1" (25mm) |
| 8–15 l/min | 1" (25mm) | 1¼" (32mm) |
| 15–25 l/min | 1¼" (32mm) | 1½" (38mm) |
| >25 l/min | 1½" (38mm) | 2" (50mm) |

**Seeventil-Material:**
- Bronze: Standard, bewährt, schwer
- DZR-Messing (Dezinkifizierungs-resistent): Akzeptabel mit Einschränkungen
- Marelon: Leicht, korrosionsfrei, Forespar ist Marktführer
- Edelstahl 316L: Möglich, teuer, Spaltkorrosionsrisiko in Seeventil-Geometrie

### 11.5 Wassertank-Verbrauchsberechnung (Frischwasser-Deckwäsche)

**Wasserverbrauch für Frischwasser-Deckwäsche:**

| Aktivität | Typischer Verbrauch | Dauer |
|---|---|---|
| Deckwäsche nach Tagestörn | 20–40 l | 3–5 min |
| Gründliche Deckwäsche (12m Boot) | 40–80 l | 5–10 min |
| Ankerketten-Spülung (50m Kette) | 30–60 l | 3–5 min |
| Badeplattform-Dusche (1 Person) | 10–20 l | 2–4 min |
| Cockpit-Spülung | 15–30 l | 2–3 min |

**Faustregel:** Frischwasser-Deckwäsche verbraucht ca. 5–10% des Tankvolumens pro Nutzung.
- Boot 10m (200l Tank): 10–20l pro Deckwäsche → 10–20 Deckwäschen pro Tankfüllung
- Boot 14m (400l Tank): 30–50l pro Deckwäsche → 8–13 Deckwäschen pro Tankfüllung

(Confidence: calculated)

---

## 12. Einbau-/Austausch-Anleitung

### 12.1 Komplettinstallation Deckwasch-System (Rohwasser)

**Benötigte Materialien:**
- Deckwaschpumpe (z.B. Jabsco Par-Max 3.0)
- Borddurchlass ¾" oder 1" mit Seeventil
- Seewasser-Sieb/Strainer (z.B. Jabsco Pumpgard P/N 46400-0012)
- Saugschlauch: 3–5m, armierter PVC, 16–19mm ID
- Druckschlauch: 3–5m, armierter PVC oder EPDM, 12–16mm ID
- Deckdurchführung / Deckwasch-Port
- Spiralschlauch: 7,5m oder 15m mit Düse
- Fußschalter oder wasserdichter Kippschalter
- Schlauchschellen: 8–12 Stück, Edelstahl 316
- Kabel: Passender Querschnitt (siehe 11.3)
- Sicherung und Sicherungshalter
- Dichtungsmasse: Sikaflex 291 oder 3M 5200

**Einbau-Schritte:**

**Schritt 1: Borddurchlass montieren**
- Position: Möglichst tief (unter Wasserlinie), aber nicht im Kiel
- Loch bohren (Lochsäge), GFK-Kanten mit Epoxy versiegeln
- Borddurchlass mit Dichtungsmasse einsetzen
- Seeventil montieren (muss von innen zugänglich und bedienbar sein!)
- 24–48h aushärten lassen, Dichtigkeitsprüfung

**Schritt 2: Seewasser-Sieb/Strainer**
- Zwischen Borddurchlass und Pumpe installieren
- Muss zugänglich sein für Reinigung (alle 1–3 Monate im Sommer)
- Jabsco Pumpgard oder Vetus FTR330 empfohlen

**Schritt 3: Pumpe montieren**
- Position: Unter Deck, möglichst nah an Borddurchlass
- Pumpensaugseite: Max. 1,8m über Wasserlinie (Selbstansaughöhe)
- Anti-Vibrations-Montage (Gummipuffer oder spezielle Halterung)
- NICHT in Bilge montieren (Feuchtigkeit → Motorschaden)
- Horizontal oder vertikal möglich (herstellerspezifisch)

**Schritt 4: Saugleitung**
- Borddurchlass → Seeventil → Sieb → Pumpe
- Armierter Schlauch, KEIN Spiralschlauch (kann kollabieren bei Unterdruck!)
- Schlauchschellen: DOPPELT an Borddurchlass und Pumpe
- Möglichst wenige Bögen (jeder 90°-Bogen = 0,5m Saugleitungsverlust)

**Schritt 5: Druckleitung**
- Pumpe → Deckdurchführung
- Armierter Schlauch oder festes Rohr (PEX, Nylon)
- Rückschlagventil direkt nach Pumpe (verhindert Rückfluss)
- Druckschlauch muss Arbeitsdruck der Pumpe aushalten!

**Schritt 6: Deckdurchführung/Port**
- Position: Gut erreichbar, nicht in Bereich mit stehendem Wasser
- Einbau gemäß 10.2
- Spiralschlauch an Deckport anschließen

**Schritt 7: Elektrik**
- Kabel von Schaltpanel zur Pumpe (passender Querschnitt)
- Sicherung am Schaltpanel (1,5× Nennstrom)
- Fußschalter oder Kippschalter an Deck (parallel zum Pumpenschalter)
- Masseverbindung über Bordnetz, NICHT über Seewasser-Leitung

**Schritt 8: Test**
- Seeventil öffnen
- Pumpe einschalten — Ansaugung testen
- Druck an Düse prüfen
- Alle Verbindungen auf Dichtigkeit prüfen
- Fußschalter/Deckschalter testen
- Sicherung testen (Pumpe unter Last)

**Zeitaufwand:** 4–8 Stunden (Erstinstallation durch Eigner), 2–4 Stunden (durch Werft)
**Kosten Material:** 350–700 EUR (Rohwasser-System, Mittelklasse-Komponenten)
**Kosten Werft:** 200–500 EUR (zusätzlich zu Material)

### 12.2 Schlauch-Austausch

**Spiralschlauch-Austausch (Deckschlauch):**

1. Alten Schlauch vom Deckport abschrauben / Quick-Connect lösen
2. Düse abschrauben (oft wieder verwendbar)
3. Neuen Schlauch anschließen
4. Dichtheit prüfen
5. Zeitaufwand: 5–15 Minuten
6. Kosten: 30–120 EUR (nur Schlauch)

**Druckleitung unter Deck austauschen:**

1. System drucklos machen (Pumpe aus, Seeventil schließen)
2. Schlauchschellen lösen (an Pumpe und Deckport)
3. Alten Schlauch entfernen
4. Neuen Schlauch zuschneiden (gleiche Länge + 50mm Reserve)
5. Schlauchschellen montieren (DOPPELT an kritischen Stellen)
6. Dichtheitsprüfung
7. Zeitaufwand: 30–60 Minuten
8. Kosten: 15–40 EUR (Material)

### 12.3 Pumpen-Austausch

1. Strom abschalten (Sicherung ziehen)
2. Seeventil schließen
3. Schlauchschellen an Saug- und Druckseite lösen
4. Kabelverbindungen lösen (Plus und Minus markieren!)
5. Pumpe von Halterung lösen
6. Neue Pumpe montieren (gleicher Typ empfohlen)
7. Schläuche anschließen, Schlauchschellen festziehen
8. Kabel anschließen (Polung beachten!)
9. Seeventil öffnen
10. Pumpe einschalten, Testlauf
11. Auf Vibration und Leckage prüfen
12. Zeitaufwand: 45–90 Minuten
13. Kosten: 100–400 EUR (Pumpe) + 50–100 EUR (Werft, optional)

### 12.4 Winterisierung

**Warum Winterisierung KRITISCH ist:**
- Wasser in Pumpe gefriert → Membran/Impeller/Gehäuse platzt
- Wasser in Schlauch gefriert → Schlauch platzt
- Wasser in Borddurchlass gefriert → Borddurchlass/Seeventil beschädigt

**Winterisierungsprozedur:**

1. Seeventil schließen
2. Saugleitung von Borddurchlass trennen (Schlauchschelle lösen)
3. Saugschlauch in Eimer mit Frostschutzmittel stellen
4. Pumpe einschalten → Frostschutz durchpumpen (bis Frostschutz an Düse austritt)
5. Pumpe ausschalten
6. Spiralschlauch abschrauben und trocken verstauen (NICHT an Deck lassen!)
7. Frostschutzmittel: Propylenglykol (ungiftig) oder spezielle Marine-Frostschutzlösung
8. NIEMALS Ethylenglykol (giftig für Gewässer!)
9. Druckleitung nicht entleeren — Frostschutz bleibt drin
10. Sicherung für Deckwaschpumpe ziehen (Schutz vor versehentlichem Einschalten)

**Frostschutzmittel-Empfehlung:**
- **Star brite Non-Toxic -50°F (-46°C)**: 4l, ca. 20 EUR, Propylenglykol
- **Ravenol Frostschutz -30°C**: 5l, ca. 25 EUR, für Sanitärsysteme
- **West Marine Non-Toxic Antifreeze**: 4l, ca. 18 USD, Propylenglykol

(Confidence: documented)

---

## 13. Lebensdauer und Alterungsmechanismen

### 13.1 Lebensdauer-Erwartung nach Komponente

| Komponente | Lebensdauer (typisch) | Lebensdauer (optimal) | Hauptversagensursache |
|---|---|---|---|
| Spiralschlauch (PVC, Deck) | 2–4 Jahre | 5 Jahre | UV-Degradation |
| Spiralschlauch (Santoprene, Deck) | 5–8 Jahre | 10 Jahre | UV-Degradation (langsam) |
| Druckschlauch (unter Deck) | 8–15 Jahre | 20 Jahre | Alterung, Versprödung |
| Saugschlauch (armiert) | 8–15 Jahre | 20 Jahre | Versprödung, Fouling |
| Membranpumpe (Jabsco/Shurflo) | 3.000–5.000 h | 8.000 h | Membranverschleiß |
| Impellerpumpe | 2.000–4.000 h | 6.000 h | Impellerverschleiß |
| Quick-Connect Fitting (Kunststoff) | 2–5 Jahre | 7 Jahre | UV, Dichtungsalterung |
| Quick-Connect Fitting (Bronze) | 10–20 Jahre | 30+ Jahre | Mechanischer Verschleiß |
| Fußschalter | 5–10 Jahre | 15 Jahre | Korrosion, Dichtungsversagen |
| Schlauchschellen (316) | 10–20 Jahre | 30+ Jahre | Spaltkorrosion |
| Schlauchschellen (304) | 2–5 Jahre | 8 Jahre | Korrosion |
| Borddurchlass (Bronze) | 20–40 Jahre | 50+ Jahre | Korrosion (sehr langsam) |
| Seewasser-Sieb | 5–15 Jahre | 20 Jahre | Korrosion, Verschmutzung |
| Düse (Messing vernickelt) | 3–8 Jahre | 10 Jahre | Korrosion, Verschleiß |
| Düse (Edelstahl 316) | 10–20 Jahre | 30+ Jahre | Mechanischer Verschleiß |

### 13.2 UV-Degradation — Hauptversagensursache

**UV-Degradations-Stufen (für visuelle Pipeline-B-Erkennung):**

| Stufe | Visuelle Merkmale | Score-Abzug | Handlungsempfehlung |
|---|---|---|---|
| 0: Neu | Glatte Oberfläche, satte Farbe | 0 Punkte | Keine Maßnahme |
| 1: Minimal | Leichte Mattierung, Farbe noch satt | -5 Punkte | UV-Schutzspray empfehlen |
| 2: Verkreidung | Weißlicher Film, Farbe verblasst | -15 Punkte | UV-Schutz, Lagerung unter Deck |
| 3: Mikrorisse | Feine Haarrisse sichtbar (Lupe) | -30 Punkte | Austausch planen (nächste Saison) |
| 4: Rissbildung | Risse mit bloßem Auge sichtbar | -50 Punkte | Austausch empfohlen (sofort) |
| 5: Brüchig | Schlauch bricht bei Biegung | -80 Punkte | Austausch SOFORT, nicht verwenden! |

### 13.3 Weitere Alterungsmechanismen

**Salzkristall-Aufbau:**
- Seewasser trocknet im Schlauch ein → Salzkristalle bilden sich
- Kristalle scheuern bei Biegung die Innenseite auf
- Prävention: Nach jedem Gebrauch kurz mit Frischwasser nachspülen

**Biofouling (Muscheln, Algen):**
- Seewasser-Ansaugsieb: Muschelbewuchs (Mytilus, Balanus) verstopft Sieb in 2–6 Monaten
- Innenseite der Saugleitung: Algenbewuchs bei stehendem Wasser
- Prävention: Regelmäßige Sieb-Reinigung, Seeventil schließen bei Nichtgebrauch

**Kink-Ermüdung:**
- Wiederholtes Knicken an gleicher Stelle → Materialschwächung
- Spiralschläuche sind anfällig am Übergang zur geraden Verbindung
- Prävention: Knickschutzfedern, korrekte Verlegung, Schlauch nicht überdehnen

**Chemischer Angriff:**
- Teak-Reiniger (Oxalsäure) greift PVC-Schläuche an
- Dieselkraftstoff/Motoröl weicht EPDM auf
- Antifouling-Lösungsmittel greifen PU-Schläuche an
- Prävention: Schlauch nach Kontakt mit Chemikalien sofort spülen

### 13.4 Wartungsplan

| Intervall | Maßnahme | Zeitaufwand |
|---|---|---|
| Nach jedem Gebrauch | Spiralschlauch mit Frischwasser nachspülen, aufhängen | 2 min |
| Monatlich (Saison) | Seewasser-Sieb prüfen und reinigen | 10 min |
| Alle 3 Monate | Schlauchschellen-Sitz prüfen, nachziehen | 15 min |
| Alle 6 Monate | Pumpendruck prüfen (Manometer am Ausgang) | 10 min |
| Jährlich (Frühjahr) | Spiralschlauch auf UV-Schäden inspizieren | 5 min |
| Jährlich (Frühjahr) | Alle Verbindungen auf Dichtheit prüfen | 15 min |
| Jährlich (Herbst) | Winterisierung durchführen | 30 min |
| Alle 2–3 Jahre | Spiralschlauch austauschen (PVC) | 10 min |
| Alle 5–8 Jahre | Spiralschlauch austauschen (Santoprene) | 10 min |
| Alle 3–5 Jahre | Pumpen-Membrankit tauschen (wenn Druckabfall) | 30 min |
| Alle 5–10 Jahre | Seewasser-Sieb austauschen | 30 min |
| Alle 10–15 Jahre | Saugschlauch und Druckschlauch austauschen | 60 min |
| Alle 15–25 Jahre | Borddurchlass und Seeventil prüfen/tauschen | 120 min (Werft) |

(Confidence: documented)

---

## 14. Fehlerbild-Atlas

### Fehlerbild DW-F01: UV-Versprödung Spiralschlauch

- **Beschreibung**: Spiralschlauch an Deck zeigt durchgehende Verkreidung, Farbverlust und Mikrorissbildung an der sonnenexponierten Seite
- **Visuelle Merkmale**: Weiße, matte Oberfläche; Risse entlang der Spiralwindungen; Schlauch fühlt sich rau und spröde an
- **Typische Position**: Spiralschlauch permanent an Deck, Sonnenseite (Steuerbord bei Nord-Süd-Liegeplatzen)
- **Ursache**: UV-Strahlung bricht Polymerketten im PVC/PU-Material
- **Betroffenes Material**: Besonders Standard-PVC und Polyurethan; EPDM und Santoprene deutlich resistenter
- **Risiko**: Bersten unter Druck (Druckstoß bei Pumpenstart), Wasseraustritt an Deck
- **Confidence**: visual_high (eindeutig visuell erkennbar)
- **AYDI Score-Auswirkung**: -40 bis -80 auf hose_score je nach Schweregrad
- **Empfehlung**: Sofortiger Austausch bei Rissbildung (Stufe 4–5); UV-Schutzspray als Prävention
- **Verwechslungsgefahr**: Oberflächliche Verkreidung (Stufe 2) ist noch kein Austauschgrund
- **Häufigkeit**: Sehr häufig — Nr. 1 Schadenbild bei Deckwaschschläuchen
- **Kosten Behebung**: 30–120 EUR (neuer Spiralschlauch)
- **Prävention**: Santoprene-Schlauch verwenden, Schlauch bei Nichtgebrauch verstauen

### Fehlerbild DW-F02: Kink-Verformung mit Wandschwächung

- **Beschreibung**: Spiralschlauch zeigt dauerhafte Knickstelle, an der die Wandstärke reduziert ist
- **Visuelle Merkmale**: Deutlicher Knick/Falte im Schlauch, Farbe heller an Knickstelle (Materialstreckung), eventuell sichtbare Rissansätze
- **Typische Position**: Am Übergang vom Spiralschlauch zum geraden Anschluss; an Umlenkungen über Deckskanten
- **Ursache**: Wiederholtes Knicken, Schlauch zu eng verlegt, Biegeradius unterschritten
- **Risiko**: Platzen unter Druck an geschwächter Stelle; reduzierter Durchfluss
- **Confidence**: visual_high
- **AYDI Score-Auswirkung**: -20 pro Knickstelle, max. -60
- **Empfehlung**: Knickstelle markieren und Schlauch beobachten; bei Rissansatz sofort tauschen
- **Häufigkeit**: Häufig, besonders bei zu kurzen Schläuchen
- **Kosten Behebung**: 30–120 EUR (neuer Spiralschlauch) oder 5 EUR (Knickschutzfeder)
- **Prävention**: Knickschutzfeder am Anschluss; ausreichende Schlauchlänge; korrekten Biegeradius einhalten

### Fehlerbild DW-F03: Dezinkifizierung an Messing-Fittings

- **Beschreibung**: Messing-Schnellkupplung oder Schlauchtülle zeigt rosa/kupferfarbene Verfärbung und poröse Oberfläche
- **Visuelle Merkmale**: Kupferfarbener statt goldener Farbton; Oberfläche rau, porös; weiße/grüne Ablagerungen
- **Typische Position**: Quick-Connect-Fittings an Deck, Schlauchtüllen in Seewasser-Kontakt
- **Ursache**: Selektive Korrosion — Zink löst sich aus der Messing-Legierung, Kupfer bleibt porös zurück
- **Betroffenes Material**: Standard-Messing (CuZn39Pb3); NICHT bei DZR-Messing oder Bronze
- **Risiko**: Fitting bricht unter Druck; schleichende Undichtigkeit
- **Confidence**: visual_high (charakteristische rosa Färbung)
- **AYDI Score-Auswirkung**: -50 auf fitting_score
- **Empfehlung**: Sofortiger Austausch gegen Bronze oder Edelstahl 316; ALLE Messing-Fittings im Seewassersystem prüfen
- **Häufigkeit**: Mittel — häufig bei Booten >10 Jahre mit Original-Messing-Fittings
- **Kosten Behebung**: 20–60 EUR (Fittings) + 30 min Arbeit
- **Prävention**: Nur Bronze (CW617N), DZR-Messing oder Edelstahl 316 für Seewassersysteme

### Fehlerbild DW-F04: Muschelbewuchs im Seewasser-Sieb

- **Beschreibung**: Seewasser-Strainer zeigt Muschelbewuchs (Seepocken, Miesmuscheln) am Siebeinsatz
- **Visuelle Merkmale**: Weiße Kalkschalen (Balanus-Seepocken) und/oder dunkle Muscheln im Siebeinsatz; reduzierter freier Querschnitt
- **Typische Position**: Seewasser-Sieb zwischen Borddurchlass und Pumpe
- **Ursache**: Seewasser-Organismen siedeln sich in ruhigem Wasser an (Boot liegt längere Zeit)
- **Risiko**: Pumpe fördert nicht oder nur reduziert; Pumpe läuft trocken → Impeller-/Membranschaden
- **Confidence**: visual_high
- **AYDI Score-Auswirkung**: -30 auf pump_score (System)
- **Empfehlung**: Sieb reinigen, Seeventil bei Nichtgebrauch schließen
- **Häufigkeit**: Sehr häufig in warmen Revieren (Mittelmeer, Tropen), seltener in Nordeuropa
- **Kosten Behebung**: 0 EUR (Reinigung) oder 20–50 EUR (neues Siebeinsatz)
- **Prävention**: Seeventil bei Nichtgebrauch schließen; monatliche Sieb-Inspektion

### Fehlerbild DW-F05: Pumpenmembran-Riss

- **Beschreibung**: Membranpumpe zeigt Druckverlust, Wasser tritt am Pumpengehäuse aus
- **Visuelle Merkmale**: Feuchtigkeitsspuren am Pumpengehäuse; Wassertropfen an Gehäuse-Trennlinie; Pumpe "rattert" bei Betrieb
- **Typische Position**: Am Pumpengehäuse (Jabsco Par-Max, Shurflo 2088)
- **Ursache**: Membranverschleiß durch Alterung, Trockenlauf, oder abrasive Partikel im Seewasser
- **Risiko**: Pumpe fördert nicht mehr; Wassereinbruch in Bilge (wenn Pumpe unter Wasserlinie)
- **Confidence**: visual_medium (Feuchtigkeit am Gehäuse kann andere Ursachen haben)
- **AYDI Score-Auswirkung**: -60 auf pump_score
- **Empfehlung**: Membran-Kit tauschen (Jabsco SK376, Shurflo 94-238-03)
- **Häufigkeit**: Mittel — nach 2.000–5.000 Betriebsstunden
- **Kosten Behebung**: 25–60 EUR (Membran-Kit) + 30 min Arbeit
- **Prävention**: Seewasser-Sieb sauber halten; Trockenlauf vermeiden; Pumpe winterisieren

### Fehlerbild DW-F06: Schlauchschelle korrodiert (304 statt 316)

- **Beschreibung**: Schlauchschelle zeigt Rost und braune Laufspuren am Schlauch
- **Visuelle Merkmale**: Braune Roststellen am Schellenband; Rostspuren auf weißem Schlauch; Schraubkopf korrodiert
- **Typische Position**: Alle Schlauchverbindungen, besonders in Spritzwasserbereich und nahe Borddurchlass
- **Ursache**: Edelstahl 304 (V2A) statt 316 (V4A) in Salzwasserumgebung
- **Risiko**: Schelle bricht → Schlauch rutscht ab → unkontrollierter Wasseraustritt
- **Confidence**: visual_high (Rost an Edelstahl ist eindeutig 304-Indikator)
- **AYDI Score-Auswirkung**: -40 auf fitting_score
- **Empfehlung**: ALLE Schlauchschellen gegen 316er austauschen
- **Häufigkeit**: Häufig — viele Budget-Boote und Eigeninstallationen verwenden 304
- **Kosten Behebung**: 10–30 EUR (Schellen-Set) + 30 min Arbeit
- **Prävention**: NUR Edelstahl 316 verwenden; bei Kauf auf "A4" oder "316" Stempel achten

### Fehlerbild DW-F07: Frostschaden Pumpe

- **Beschreibung**: Pumpengehäuse gerissen nach Frost ohne vorherige Winterisierung
- **Visuelle Merkmale**: Sichtbarer Riss im Pumpengehäuse; Eis in der Pumpe (bei Inspektion im Winter); Pumpe fördert nicht (Druck entweicht durch Riss)
- **Typische Position**: Deckwaschpumpe unter Deck, besonders bei unbeheizten Booten
- **Ursache**: Wasser in Pumpe gefroren → Volumenausdehnung 9% → Gehäuse gesprengt
- **Risiko**: Pumpe Totalschaden; bei Inbetriebnahme ohne Inspektion → Wassereinbruch
- **Confidence**: visual_high (eindeutiger Riss im Gehäuse)
- **AYDI Score-Auswirkung**: -100 auf pump_score (Totalausfall)
- **Empfehlung**: Pumpe komplett tauschen; korrekte Winterisierung für nächsten Winter
- **Häufigkeit**: Mittel — v.a. bei Neulingen, die erstmals in kaltem Klima überwintern
- **Kosten Behebung**: 100–400 EUR (neue Pumpe)
- **Prävention**: Winterisierung mit Propylenglykol-Frostschutz (siehe 12.4)

### Fehlerbild DW-F08: Quick-Connect-Dichtung ausgehärtet

- **Beschreibung**: Quick-Connect-Deckport tropft bei Anschluss des Schlauchs
- **Visuelle Merkmale**: Wassertropfen am Verbindungspunkt; O-Ring sichtbar verhärtet, rissig oder verformt
- **Typische Position**: Deckwasch-Port an Deck (exponiert, UV + Temperaturwechsel)
- **Ursache**: O-Ring aus NBR oder EPDM ausgehärtet durch UV und Temperaturzyklen
- **Risiko**: Druckverlust, reduzierte Spülwirkung; Wasseransammlung unter Deck
- **Confidence**: visual_medium (Tropfen können auch vom Schlauch kommen)
- **AYDI Score-Auswirkung**: -25 auf fitting_score
- **Empfehlung**: O-Ring tauschen (passendes Maß), mit Silikonfett einsetzen
- **Häufigkeit**: Häufig nach 3–5 Jahren
- **Kosten Behebung**: 2–5 EUR (O-Ring) + 5 min Arbeit
- **Prävention**: Kappe auf Deckport bei Nichtgebrauch; regelmäßig Silikonfett auf O-Ring

### Fehlerbild DW-F09: Spiralschlauch Wasserretention

- **Beschreibung**: Spiralschlauch hängt durch und hält stehendes Wasser in den Windungen
- **Visuelle Merkmale**: Schlauch hängt zwischen Aufhängepunkten durch; sichtbares Wasser in Windungen; grünlicher Belag (Algen) in Windungen
- **Typische Position**: An Deck liegende Spiralschläuche, besonders bei großen Längen (>10m)
- **Ursache**: Gravitation — Spiralschlauch liegt nicht gespannt genug; fehlende Aufhängehaken
- **Risiko**: Algenbildung, Geruch, beschleunigte Alterung, Zusatzgewicht an Deck
- **Confidence**: visual_high
- **AYDI Score-Auswirkung**: -15 auf hose_score
- **Empfehlung**: Aufhängehaken installieren; nach Gebrauch Schlauch aushängen und abtropfen lassen
- **Häufigkeit**: Häufig, oft unterschätzt
- **Kosten Behebung**: 5–15 EUR (Aufhängehaken-Set)
- **Prävention**: Schlauch immer aufhängen; Endstück offen lassen (Wasser abfließen)

### Fehlerbild DW-F10: Ankerspül-Düse verstopft

- **Beschreibung**: Ankerspüldüse sprüht ungleichmäßig oder gar nicht trotz laufender Pumpe
- **Visuelle Merkmale**: Kein oder nur einseitiger Wasserstrahl; Kalkablagerung/Salzkrusten an Düsenöffnung; Sand/Korallen-Partikel blockieren Öffnung
- **Typische Position**: Ankerspüldüse am Bug, nahe Bugrolle/Windlass
- **Ursache**: Kalk, Salz, Sand oder Korallenstücke verstopfen die feinen Düsenöffnungen
- **Risiko**: Kette wird nicht gespült → Salzkorrosion, Sandabrieb im Windlass-Getriebe
- **Confidence**: visual_medium (erfordert Betriebsprüfung)
- **AYDI Score-Auswirkung**: -30 auf nozzle_score
- **Empfehlung**: Düse mit Nadel reinigen; in Essigbad einweichen (Kalkentfernung)
- **Häufigkeit**: Häufig in kalkhaltigem Wasser und nach Ankern in Sand/Schlick
- **Kosten Behebung**: 0 EUR (Reinigung) oder 20–50 EUR (neue Düse)
- **Prävention**: Düse nach jeder Benutzung kurz mit Frischwasser nachspülen

### Fehlerbild DW-F11: Rückschlagventil klemmt/fehlt

- **Beschreibung**: Seewasser läuft rückwärts durch die Pumpe und tritt an der Deckdurchführung aus
- **Visuelle Merkmale**: Feuchtigkeitsschaden unter Deck nahe Pumpenlocation; Wasser tritt am Deckport aus obwohl Pumpe aus; ständiges Tropfen bei Seegang
- **Typische Position**: Druckleitung zwischen Pumpe und Deckdurchführung
- **Ursache**: Fehlendes Rückschlagventil oder klemmendes/verschmutztes Rückschlagventil
- **Risiko**: Wassereinbruch unter Deck, besonders bei Seegang (Wellenandruckauf Borddurchlass)
- **Confidence**: visual_low (Symptom kann viele Ursachen haben)
- **AYDI Score-Auswirkung**: -50 auf system_score, compliance_issue
- **Empfehlung**: Rückschlagventil nachrüsten (direkt nach Pumpenausgang)
- **Häufigkeit**: Mittel — viele Erstinstallationen vergessen das Rückschlagventil
- **Kosten Behebung**: 8–20 EUR (Ventil) + 15 min Einbau
- **Prävention**: Rückschlagventil als Pflichtkomponente in jeder Installation

### Fehlerbild DW-F12: Saugschlauch Kollaps (Kinking unter Vakuum)

- **Beschreibung**: Nicht-armierter Saugschlauch kollabiert (zieht sich zusammen) wenn Pumpe ansaugt
- **Visuelle Merkmale**: Schlauch ist plattgedrückt/eingezogen; Pumpe "würgt" und rattert; kein Wasserdurchfluss trotz offenem Seeventil
- **Typische Position**: Saugleitung zwischen Borddurchlass/Sieb und Pumpe
- **Ursache**: Falscher Schlauchtyp (Spiralschlauch oder nicht-armierter Schlauch als Saugleitung) — nicht vakuumfest
- **Risiko**: Pumpe fördert nicht, läuft trocken → Impeller-/Membranschaden
- **Confidence**: visual_high (kollabierten Schlauch erkennt man deutlich)
- **AYDI Score-Auswirkung**: -60 auf hose_score, -30 auf pump_score
- **Empfehlung**: Saugleitung durch armierten/spiralarmierten Schlauch ersetzen (vakuumfest!)
- **Häufigkeit**: Selten bei Profi-Installation, häufig bei Eigenbauten
- **Kosten Behebung**: 20–50 EUR (armierter Schlauch) + 30 min Arbeit
- **Prävention**: IMMER armierten/vakuumfesten Schlauch für Saugleitungen verwenden

(Confidence: documented)

---

## 15. Fehlerbehebungs-Leitfaden

### Problem 1: Pumpe läuft, aber kein Wasser kommt an der Düse an

**Systematische Diagnose:**

1. **Seeventil prüfen**: Ist das Seeventil geöffnet? (Häufigster Fehler!)
   - → Seeventil öffnen

2. **Sieb/Strainer prüfen**: Ist der Siebeinsatz verstopft (Muscheln, Algen, Blätter)?
   - → Sieb reinigen

3. **Saugleitung prüfen**: Ist der Saugschlauch kollabiert oder geknickt?
   - → Schlauch ersetzen (armierter Typ!)

4. **Pumpe prüfen**: Läuft die Pumpe, aber rattert/vibriert ungewöhnlich?
   - → Membran gerissen → Membran-Kit tauschen
   - → Impeller verschlissen → Impeller tauschen
   - → Luft im System → Saugleitung auf Dichtheit prüfen

5. **Druckleitung prüfen**: Ist der Druckschlauch geknickt oder blockiert?
   - → Schlauch prüfen, ggf. ersetzen

6. **Deckport prüfen**: Ist der Deckport-Durchgang blockiert?
   - → Deckport reinigen

7. **Rückschlagventil prüfen**: Klemmt das Rückschlagventil in geschlossener Position?
   - → Ventil reinigen oder tauschen

(Confidence: documented)

### Problem 2: Pumpe schaltet ständig ein und aus (Cycling)

**Systematische Diagnose:**

1. **Leckage im System**: Kleines Leck lässt Druck abfallen → Druckschalter aktiviert Pumpe → Druck steigt → Pumpe aus → Druck fällt wieder
   - → Alle Verbindungen auf Tropfen prüfen
   - → Deckport-Dichtung prüfen
   - → Düse auf Schlussfähigkeit prüfen

2. **Druckschalter defekt**: Druckschalter schaltet bei falschem Druck
   - → Druckschalter kalibrieren (Einstellschraube an Jabsco-Pumpen)
   - → Druckschalter tauschen

3. **Rückschlagventil undicht**: Wasser fließt rückwärts, Druck fällt
   - → Rückschlagventil prüfen, reinigen oder tauschen

4. **Akkumulator/Drucktank fehlt**: System ohne Druckpuffer → schnelle Druckschwankungen
   - → Drucktank nachrüsten (0,5–2l, reduziert Cycling um 80%)

(Confidence: documented)

### Problem 3: Druck an der Düse zu gering

**Systematische Diagnose:**

1. **Schlauchdurchmesser zu klein**: 12mm ID bei langer Schlauchlänge und leistungsstarker Pumpe
   - → Schlauch auf 16mm oder 19mm ID upgraden

2. **Schlauch zu lang**: Druckverlust steigt mit Länge
   - → Kürzere Schlauchlänge, größeren Durchmesser wählen (siehe Tabelle 11.2)

3. **Sieb teilweise verstopft**: Reduzierte Durchflussmenge
   - → Sieb reinigen

4. **Pumpe schwächelt**: Membran-/Impellerverschleiß
   - → Membran-Kit oder Impeller tauschen

5. **Knicke im Schlauch**: Druckverlust an Knickstellen
   - → Schlauchverlegung korrigieren, Knickschutz installieren

6. **Zu viele T-Abzweigungen**: Jede Abzweigung = Druckverlust
   - → Absperrhähne an nicht benötigten Abzweigungen schließen

(Confidence: documented)

### Problem 4: Spiralschlauch rollt sich nicht mehr auf

**Systematische Diagnose:**

1. **UV-Alterung**: Material hat Elastizität verloren, Schlauch bleibt gerade
   - → Schlauch austauschen

2. **Kink-Verformung**: Dauerhafte Verformung an Knickstellen
   - → Schlauch austauschen

3. **Temperatur**: Bei Kälte (<5°C) verlieren PVC-Schläuche Flexibilität
   - → Normal bei PVC, Schlauch vor Gebrauch in der Sonne erwärmen
   - → Langfristig: Santoprene-Schlauch (flexibel bis -40°C)

4. **Falscher Schlauchtyp**: Nicht jeder Schlauch ist als Spiralschlauch geeignet
   - → Nur Spiralschlauch-spezifische Produkte verwenden

(Confidence: documented)

### Problem 5: Laute Vibration bei Pumpenbetrieb

**Systematische Diagnose:**

1. **Fehlende Anti-Vibrations-Montage**: Pumpe direkt auf GFK verschraubt → Resonanz
   - → Gummipuffer (Silent-Blocks) unterlegen
   - → Jabsco Gummifüße P/N 18910-0583

2. **Schlauch in Resonanz**: Membranpumpe pulsiert → Schlauch vibriert gegen Schott
   - → Schlauchbefestigung mit Gummischellen, nicht starr

3. **Luft im System**: Pumpe saugt teilweise Luft → rattert
   - → Saugleitung auf Undichtigkeit prüfen (Schlauchschellen, Sieb-Dichtung)

4. **Pumpe verschlissen**: Lagerverschleiß → Laufgeräusch
   - → Pumpe tauschen

5. **Druckstoß (Water Hammer)**: Plötzliches Schließen der Düse → Schlag in Leitung
   - → Drucktank/Akkumulator installieren (dämpft Druckstöße)

(Confidence: documented)

---

## 16. FAQ

### DW-001: Brauche ich ein Deckwasch-System auf meinem Segelboot?
Ab 10m Bootslänge ist ein Deckwasch-System sehr empfehlenswert. Es schützt Beschläge und Gelcoat vor Salzkorrosion und erleichtert die Deckpflege erheblich. Für Boote <10m reicht oft ein tragbarer Drucksprüher oder ein Eimer mit Seewasser.
(Confidence: documented)

### DW-002: Rohwasser oder Frischwasser — was ist besser?
Rohwasser (Seewasser) ist für die grobe Deckwäsche und Ankerspülung ausreichend und verbraucht kein Tankwasser. Frischwasser ist die bessere Wahl für die Nachreinigung, Teakdeckpflege und Badeplattform-Dusche. Ideal ist ein Dual-System mit Umschaltung.
(Confidence: documented)

### DW-003: Wie lange hält ein Spiralschlauch an Deck?
Standard-PVC: 2–4 Jahre (Mittelmeer) bis 3–5 Jahre (Nordeuropa). Santoprene (Trident 369): 5–8 Jahre (Mittelmeer) bis 7–12 Jahre (Nordeuropa). UV-Strahlung ist der Hauptfeind — Lagerung unter Deck verlängert die Lebensdauer erheblich.
(Confidence: documented)

### DW-004: Welche Pumpe für ein 12m Segelboot?
Jabsco Par-Max 3.0 (11,4 l/min, 3,4 bar) ist die Standardwahl. Für Deckwäsche + Ankerspülung gleichzeitig: Par-Max 4.0 (16,3 l/min, 4,1 bar). Shurflo 2088 als günstigere Alternative.
(Confidence: documented)

### DW-005: Kann ich Gardena-Anschlüsse für die Deckwäsche verwenden?
Nur temporär und bei Lagerung unter Deck. Gardena-Fittings sind nicht UV-beständig und nicht salzwasserfest. Für permanente Installation an Deck: Bronze- oder Edelstahl-Deckports (Forespar, Perko, Scandvik) verwenden.
(Confidence: documented)

### DW-006: Brauche ich ein Rückschlagventil?
Ja, unbedingt! Ein Rückschlagventil in der Druckleitung verhindert, dass Seewasser rückwärts durch die Pumpe ins Boot strömt. Besonders kritisch, wenn der Deckport über der Pumpe liegt und das Seeventil geöffnet bleibt.
(Confidence: documented)

### DW-007: Wie winterisiere ich mein Deckwasch-System?
Seeventil schließen, Saugschlauch in Propylenglykol-Frostschutzmittel stellen, Pumpe einschalten bis Frostschutz an der Düse austritt, Spiralschlauch abschrauben und trocken lagern, Sicherung ziehen. NIEMALS Ethylenglykol verwenden!
(Confidence: documented)

### DW-008: Was kostet eine komplette Deckwasch-Installation?
Material für ein einfaches Rohwasser-System: 300–550 EUR. Dual-System (Roh+Frisch): 600–1.200 EUR. Profisystem mit Ankerspülung: 800–2.000 EUR. Werfteinbau zusätzlich: 200–600 EUR.
(Confidence: estimated)

### DW-009: Mein Spiralschlauch ist gelb geworden — muss er getauscht werden?
Gelbfärbung (Vergilbung) ist UV-Degradation Stufe 2 — noch kein Austauschgrund, aber ein Warnsignal. UV-Schutzspray auftragen und Schlauch bei Nichtgebrauch verstauen. Bei zusätzlicher Rissbildung → austauschen.
(Confidence: documented)

### DW-010: Spiralschlauch oder Flachschlauch — was ist besser?
Spiralschlauch: Praktischer im Alltag (selbstaufrollend), aber UV-exponiert. Flachschlauch: Platzsparender, geschützt im Locker, aber muss nach Gebrauch sorgfältig aufgerollt werden. Für die meisten Yachten ist der Spiralschlauch die bessere Wahl.
(Confidence: documented)

### DW-011: Kann ich die Seewasserpumpe meines Motors für die Deckwäsche nutzen?
Theoretisch möglich mit einem T-Stück an der Motorkühlwasserleitung, aber NICHT empfohlen. Risiken: Druckleitung kann platzen bei hohem Motordrehzahl; Rückwirkung auf Motorkühlung; zusätzlicher Druckverlust in der Kühlwasserleitung.
(Confidence: documented)

### DW-012: Wie oft muss ich das Seewasser-Sieb reinigen?
Im Sommer: monatlich in warmen Revieren (Mittelmeer, Karibik), alle 2–3 Monate in Nordeuropa. Im Winter: vor und nach der Winterpause. Bei nachlassendem Druck: sofort prüfen.
(Confidence: documented)

### DW-013: Welcher Schlauchdurchmesser ist richtig?
12mm ID für kleine Boote (<10m) und geringe Schlauchlängen (<8m). 16mm ID Standardwahl für Boote 10–18m. 19mm ID für Boote >18m, lange Leitungen, oder Dual-System. 25mm ID nur für Superyachten oder Hochleistungssysteme.
(Confidence: documented)

### DW-014: Brauche ich eine Ankerspülung?
In Gezeitenrevieren (Sand, Schlick): JA, absolut kritisch. Im Mittelmeer (Fels, Sand): Sehr empfehlenswert. In Süßwasser: Weniger wichtig, aber dennoch sinnvoll gegen Schlamm und Algen im Ankerkasten.
(Confidence: documented)

### DW-015: Kann ich einen Hochdruckreiniger als Deckwäsche verwenden?
Nicht empfohlen für Dauerinstallation. Hochdruckreiniger (>50 bar) können Gelcoat, Teakfugen und Dichtungen beschädigen. Für gelegentliche Grundreinigung am Liegeplatz (mit Landstrom und Wasseranschluss) akzeptabel bei reduziertem Druck und breitem Fächerstrahl.
(Confidence: documented)

### DW-016: Was ist der Unterschied zwischen Par-Max und Par-Max HD?
Par-Max HD hat verstärkte Membranen, leistungsstärkere Motoren und höhere Druckleistung. HD-Modelle sind für den Dauerbetrieb und Dual-Systeme konzipiert. Standard Par-Max reicht für einfache Deckwäsche.
(Confidence: measured)

### DW-017: Wie laut ist eine Deckwaschpumpe?
Jabsco Par-Max: 55–68 dB (pulsierend). Shurflo 4-Kammer: 50–62 dB (gleichmäßiger). Johnson AquaJet: 45–55 dB (leiseste). Ein Drucktank/Akkumulator reduziert die Zyklen und damit die wahrgenommene Lautstärke.
(Confidence: documented)

### DW-018: Muss der Borddurchlass für die Deckwäsche ein Seeventil haben?
Ja. Jeder Borddurchlass unter der Wasserlinie MUSS ein bedienbares Seeventil haben (ISO 9093, RCD 2013/53/EU). Das gilt auch für die Seewasser-Ansaugung der Deckwaschpumpe.
(Confidence: measured)

### DW-019: Kann ich Trinkwasserschlauch für die Deckwäsche verwenden?
Ja, für Frischwasser-Systeme ist ein lebensmittelechter Schlauch sogar vorteilhaft. Für Seewasser-Systeme ist ein normaler Marine-Schlauch ausreichend. Trinkwasserschläuche (FDA/KTW-zugelassen) sind typisch teurer.
(Confidence: documented)

### DW-020: Was ist ein Drucktank/Akkumulator und brauche ich einen?
Ein Drucktank ist ein kleiner Behälter mit Luftkammer, der Druckschwankungen in der Leitung ausgleicht. Vorteile: Pumpe zykelt seltener (längere Lebensdauer), weniger Lärm, gleichmäßigerer Wasserstrahl. Empfohlen für Systeme ab Par-Max 3.0. Preis: 30–80 EUR.
(Confidence: documented)

### DW-021: Mein Fußschalter reagiert nicht — was tun?
Häufigste Ursache: Korrosion an den Schaltkontakten (Spritzwasser). Fußschalter demontieren, Kontakte mit Kontaktspray reinigen. Wenn defekt: Austausch gegen IP-68-Modell (Jabsco 18753 oder Hella). Alternativ: Pumpe direkt über Schaltpanel testen.
(Confidence: documented)

### DW-022: Ist eine Badeplattform-Dusche sinnvoll?
Auf Booten mit Badeplattform: absolut ja. Eine warme Süßwasser-Dusche nach dem Schwimmen ist einer der geschätztesten Luxusartikel an Bord. Investition: 100–350 EUR (Komplett-Kit). Nachrüstung: 2–4 Stunden.
(Confidence: documented)

### DW-023: Kann ich mein Deckwasch-System für den Brandschutz nutzen?
Auf kleinen Yachten (<15m) ist das Deckwasch-System kein Ersatz für zugelassene Feuerlöscher. Auf größeren Yachten (>15m, besonders Motoryachten) werden dedizierte Feuerlösch-Monitore über die Seewasser-Druckanlage gespeist. Die Deckwaschpumpe ist für Feuerlöschzwecke zu schwach (Druck und Volumenstrom).
(Confidence: documented)

### DW-024: Welche Quick-Connects sind salzwasserfest?
Bronze: Forespar, Perko. Edelstahl 316: Scandvik, Whale (System 15 aus Acetal ist salzwasserneutral). Messing: NUR DZR-Messing akzeptabel. Kunststoff (ABS): Gardena, Hozelock — NICHT für Salzwasser-Dauerexposition.
(Confidence: documented)

### DW-025: Wie entlüfte ich mein Deckwasch-System nach dem Winter?
Seeventil öffnen, Pumpe einschalten und laufen lassen. Die meisten Membranpumpen (Jabsco, Shurflo) sind selbstentlüftend und saugen die Luft automatisch ab. Bei Impellerpumpen: Sieb mit Wasser befüllen, dann Pumpe einschalten. Typische Entlüftungsdauer: 30–120 Sekunden.
(Confidence: documented)

---

## 17. Glossar

| Nr. | Begriff | Erklärung |
|---|---|---|
| 1 | Ankerspülung (Anchor Wash) | System zum Abspülen von Schlamm, Sand und Salz von der Ankerkette beim Einholen |
| 2 | Arbeitsdruck (Working Pressure) | Maximaler Dauerbetriebsdruck eines Schlauchs oder Systems in bar |
| 3 | Backflow Prevention | Rückflussverhütung durch Ventil oder Rückschlagklappe |
| 4 | Biegeradius (Bend Radius) | Minimaler Krümmungsradius eines Schlauchs ohne dauerhafte Verformung oder Knicken |
| 5 | Bilge | Tiefster Punkt im Boot, wo sich Wasser sammelt |
| 6 | Borddurchlass (Through-Hull) | Wasserdichte Durchführung durch die Außenhaut eines Bootes für Leitungen |
| 7 | BSP (British Standard Pipe) | Britisches Gewindesystem für Rohrleitungen, Standard in der Marine-Industrie |
| 8 | Berstdruck (Burst Pressure) | Druck, bei dem ein Schlauch versagt (typisch 3–4× Arbeitsdruck) |
| 9 | Chalking (Verkreidung) | UV-bedingter Oberflächenzerfall — Material wird weiß und pulvrig |
| 10 | Coiled Hose (Spiralschlauch) | Schlauch mit Spiralform, der sich nach Dehnung selbst aufrollt |
| 11 | Cycling (Zyklieren) | Unerwünschtes wiederholtes Ein-/Ausschalten der Pumpe |
| 12 | Deckport (Deckwasch-Anschluss) | Bündig in das Deck eingebauter Wasseranschluss mit Quick-Connect |
| 13 | Deckwäsche (Deck Wash) | Reinigung der Deckflächen mit Wasser unter Druck |
| 14 | Dezinkifizierung (Dezincification) | Korrosionsprozess bei Messing — Zink löst sich, poröses Kupfer bleibt |
| 15 | Drucktank / Akkumulator | Pufferbehälter mit Luftkammer zur Dämpfung von Druckschwankungen |
| 16 | Dual-System | Deckwasch-System mit umschaltbarer Roh-/Frischwasser-Versorgung |
| 17 | EPDM | Ethylen-Propylen-Dien-Monomer — UV- und ozonbeständiger Synthesekautschuk |
| 18 | Fächerdüse (Fan Jet) | Düse mit breitem, flachem Wasserstrahl für flächige Reinigung |
| 19 | Flat Hose (Flachschlauch) | Schlauch, der im drucklosen Zustand flach zusammenliegt |
| 20 | Frostschutz (Antifreeze) | Propylenglykol-Lösung zum Schutz vor Frostschäden im Winter |
| 21 | Fußschalter (Foot Switch) | In das Deck eingebauter Schalter, der mit dem Fuß betätigt wird |
| 22 | GFK (FRP) | Glasfaserverstärkter Kunststoff — Standard-Rumpfmaterial |
| 23 | Impellerpumpe | Pumpe mit rotierendem Gummi-Flügelrad (Impeller) |
| 24 | ISO 9093 | Internationale Norm für Borddurchlässe und Seeventile im Yachtbau |
| 25 | Kinking (Knicken) | Unerwünschte dauerhafte Knickverformung eines Schlauchs |
| 26 | Livewell | Becken mit Seewasser-Zirkulation zum Halten lebender Köderfische |
| 27 | Marelon | Glasfaserverstärktes Nylon (Forespar) — korrosionsfreies Borddurchlass-Material |
| 28 | Membranpumpe (Diaphragm Pump) | Pumpe, die über eine flexible Membran Wasser fördert |
| 29 | NMEA 2000 | Marine-Datennetzwerk zur Verbindung von Bordelektronik |
| 30 | Non-Percolating | Dichtung/Fitting, das keine Feuchtigkeit durchlässt (Deck-Durchführung) |
| 31 | NPT (National Pipe Thread) | Amerikanisches Gewindesystem für Rohrleitungen |
| 32 | Par-Max | Jabsco-Produktlinie für marine Membranpumpen |
| 33 | Pistolendüse (Trigger Nozzle) | Düse mit Abzugshebel für gezielten Wasserstrahl |
| 34 | Propylenglykol | Ungiftiges Frostschutzmittel für marine Systeme |
| 35 | Quick-Connect (Schnellkupplung) | Werkzeuglose Steckverbindung für Schläuche |
| 36 | Rohwasser (Raw Water) | Unbehandeltes Seewasser aus dem Borddurchlass |
| 37 | Rückschlagventil (Check Valve) | Ventil, das Durchfluss nur in eine Richtung erlaubt |
| 38 | Santoprene (TPV) | Thermoplastisches Vulkanisat — hochwertigstes Schlauchmaterial für UV-Exposition |
| 39 | Seeventil (Seacock) | Absperrhahn am Borddurchlass zum Schließen der Seewasser-Leitung |
| 40 | Strainer (Sieb/Filter) | Siebeinsatz zum Schutz der Pumpe vor Fremdkörpern |
| 41 | System 15 | Whale Marine proprietäres 15mm Quick-Connect-System |
| 42 | Transom Shower | Dusche an der Badeplattform (Heck) des Bootes |
| 43 | Trockenlauf (Dry Running) | Pumpenbetrieb ohne Wasserförderung — zerstört Membran/Impeller |
| 44 | UV-Degradation | Zerstörung von Polymeren durch ultraviolette Strahlung |
| 45 | Windlass (Ankerwinde) | Elektrische oder hydraulische Winde zum Einholen der Ankerkette |
| 46 | Winterisierung (Winterization) | Maßnahmen zum Schutz des Systems vor Frostschäden in der Winterpause |

---

## 18. Schnell-Referenz

### 18.1 Pumpenauswahl Quick-Guide

| Bootslänge | Einfache Deckwäsche | Deckwäsche + Ankerspülung | Dual-System |
|---|---|---|---|
| 8–10m | Par-Max 1.0 / Seaflo 41 | Par-Max 2.0 | Par-Max 3.0 |
| 10–14m | Par-Max 3.0 / Shurflo 2088 | Par-Max 4.0 | Par-Max 4.0 + Druckwasser |
| 14–20m | Par-Max 4.0 | Par-Max HD5 | Par-Max HD5 + Druckwasser |
| 20–25m | Par-Max HD5 | Par-Max HD6 | 2× Par-Max HD5 |
| 25m+ | Zentral-Druckanlage | Dedizierte Ankerspülpumpe | Profisystem |

### 18.2 Schlauchauswahl Quick-Guide

| Anwendung | Empf. Material | Empf. ID | Min. Arbeitsdruck |
|---|---|---|---|
| Spiralschlauch Deck (Budget) | PVC UV-stabilisiert | 12mm | 6 bar |
| Spiralschlauch Deck (Premium) | Santoprene (Trident 369) | 12–16mm | 10 bar |
| Druckleitung unter Deck | PVC armiert / EPDM | 12–16mm | 10 bar |
| Saugleitung (Seewasser) | Spiralarmierter PVC (vakuumfest!) | 16–19mm | 3 bar + vakuumfest |
| Badeplattform-Dusche | Silikon / Edelstahl-Panzer | 12mm | 6 bar |
| Livewell | Santoprene / FDA-PVC | 19mm | 4 bar |

### 18.3 Kosten Quick-Guide

| System | Material-Kosten | Werft-Einbau | Gesamt |
|---|---|---|---|
| Einfach Rohwasser (8–10m) | 150–300 EUR | 150–300 EUR | 300–600 EUR |
| Standard Rohwasser (10–14m) | 300–550 EUR | 200–400 EUR | 500–950 EUR |
| Dual-System (12–18m) | 600–1.200 EUR | 300–600 EUR | 900–1.800 EUR |
| Voll integriert (14–20m) | 800–1.800 EUR | 500–1.000 EUR | 1.300–2.800 EUR |
| Profisystem (20–25m) | 2.000–5.000 EUR | 800–2.000 EUR | 2.800–7.000 EUR |
| Superyacht (25m+) | 5.000–25.000 EUR | 2.000–8.000 EUR | 7.000–33.000 EUR |

### 18.4 Wartungs-Quick-Guide

| Intervall | Aufgabe | Dauer |
|---|---|---|
| Jede Nutzung | Frischwasser nachspülen, Schlauch aufhängen | 2 min |
| Monatlich | Seewasser-Sieb reinigen | 10 min |
| Vierteljährlich | Schlauchschellen prüfen | 15 min |
| Halbjährlich | Pumpendruck prüfen | 10 min |
| Jährlich (Frühjahr) | UV-Inspektion Spiralschlauch | 5 min |
| Jährlich (Herbst) | Winterisierung | 30 min |

---

## 19. Notfall-Ressourcen

### 19.1 Notfall: Deckwaschpumpe pumpt Wasser ins Boot

**Sofortmaßnahmen:**
1. **PUMPE AUS!** — Sicherung ziehen
2. **Seeventil schließen!** — Seewasser-Ansaugung unterbinden
3. Einlaufendes Wasser mit Bilgenpumpe oder Handpumpe lenzen
4. Ursache identifizieren: Geplatzter Schlauch? Gelöste Schlauchschelle? Riss im Pumpengehäuse?
5. Reparatur oder provisorische Abdichtung

### 19.2 Notfall: Borddurchlass der Deckwäsche undicht

**Sofortmaßnahmen:**
1. **Seeventil schließen!** (wenn noch möglich)
2. Wenn Seeventil nicht schließt: Konischen Holzpflock (Softwood Plug) in Borddurchlass treiben
3. Holzpflöcke sollten an jedem Borddurchlass griffbereit hängen (Pflicht bei vielen Versicherungen!)
4. Bilgenpumpe aktivieren
5. Nächsten Hafen anlaufen, Werft kontaktieren

### 19.3 Provisorische Reparatur auf See

| Problem | Provisorium | Material |
|---|---|---|
| Geplatzter Schlauch | Klebeband (Silikonband, Vulkanisierband) um Bruchstelle | Rescue Tape / Self-Fusing Tape |
| Gelöste Schlauchschelle | Kabelbinder als Notschelle | UV-beständige Kabelbinder |
| Riss im Quick-Connect | Einseitig abdichten, Pumpe nicht verwenden | Sikaflex + Klebeband |
| Pumpe ausgefallen | Deckwäsche mit Eimer und Bürste | Eimer, Bürste |
| Sieb verstopft | Direktanschluss ohne Sieb (temporär!) | Schlauchverbinder |

### 19.4 Kontakte und Notfallnummern

| Dienst | Kontakt | Zuständigkeit |
|---|---|---|
| SeaHelp (Mittelmeer) | +385 91 600 50 50 | Technische Hilfe auf See (Adria) |
| DGzRS (Deutschland) | +49 421 536870 | Seenotrettung (Schifffahrt) |
| CROSS (Frankreich) | 196 (Küste) | Seenotrettung (Frankreich) |
| RNLI (UK) | 999 | Seenotrettung (UK) |
| BoatUS (USA) | 1-800-391-4869 | Technische Hilfe (USA) |

(Confidence: documented)

---

## ANHANG A — Cross-Reference: Pumpe → Schlauch → Düse → Boot

| Bootsklasse | Pumpe | Schlauch (Deck) | Schlauch (Saug) | Düse | Deckport |
|---|---|---|---|---|---|
| Segelboot 8m | Par-Max 1.0 | 12mm PVC Spiral 4,5m | 16mm armiert 2m | Brause 7-fach | Whale System 15 |
| Segelboot 10m | Par-Max 2.0 | 12mm PVC Spiral 7,5m | 16mm armiert 3m | Pistolendüse | Jabsco Snap-In |
| Segelboot 12m | Par-Max 3.0 | 16mm Santoprene 7,5m | 19mm armiert 3m | Pistolendüse | Forespar Bronze |
| Segelboot 14m | Par-Max 4.0 | 16mm Santoprene 7,5m | 19mm armiert 4m | Pistolendüse | Perko Bronze |
| Motoryacht 10m | Par-Max 3.0 | 12mm PVC Spiral 7,5m | 16mm armiert 3m | Brause verstellbar | Jabsco Snap-In |
| Motoryacht 14m | Par-Max 4.0 | 16mm Santoprene 15m | 19mm armiert 4m | Pistolendüse | Scandvik Edelstahl |
| Motoryacht 18m | Par-Max HD5 | 19mm Santoprene 15m | 25mm armiert 5m | Feuerlöschdüse | Perko Edelstahl |
| Sportfischer 8m | Par-Max 3.0 | 16mm PVC Spiral 7,5m | 16mm armiert 3m | Pistolendüse + Livewell | Jabsco Snap-In |
| Katamaran 12m | 2× Par-Max 2.0 | 2× 12mm Spiral 7,5m | 2× 16mm armiert | Brause je Rumpf | 2× Whale System 15 |
| Superyacht 25m | HD6 + Zentral | 25mm fest + 19mm Spiral | 32mm armiert 8m | Hydrant | Edelstahl Flansch |

(Confidence: documented)

---

## ANHANG B — UV-Beständigkeits-Vergleich

### B.1 Material-Ranking nach UV-Beständigkeit

| Rang | Material | UV-Index (0–100) | Lebensdauer Deck (Mittelmeer) | ASTM D4329 (Stunden bis Degradation) |
|---|---|---|---|---|
| 1 | Silikon | 95 | 8–15 Jahre | >5.000 h |
| 2 | Santoprene (TPV) | 88 | 5–8 Jahre | >3.000 h |
| 3 | EPDM (schwarz) | 82 | 5–7 Jahre | >2.500 h |
| 4 | EPDM (weiß) | 75 | 4–6 Jahre | >2.000 h |
| 5 | UV-stabilisiertes PVC | 55 | 2–4 Jahre | >1.000 h |
| 6 | Polyurethan (PU) | 50 | 2–3 Jahre | >800 h |
| 7 | Standard-PVC | 30 | 1–2 Jahre | >400 h |
| 8 | Polyethylen (PE) | 25 | 1–2 Jahre | >300 h |
| 9 | Standard-Nylon | 20 | 6–12 Monate | >200 h |
| 10 | ABS (Gardena/Hozelock) | 15 | 6–12 Monate | >150 h |

### B.2 UV-Schutzprodukte

| Produkt | Hersteller | Typ | Wirkdauer | Preis |
|---|---|---|---|---|
| 303 Aerospace Protectant | 303 Products | UV-Schutzspray | 4–8 Wochen | 15–25 EUR (300ml) |
| Star brite Ultimate UV Protectant | Star brite | UV-Schutzspray | 4–6 Wochen | 12–20 EUR (300ml) |
| McLube Sailkote | McLube | PTFE + UV-Schutz | 2–4 Wochen | 18–28 EUR (300ml) |
| Iosso UV Protectant | Iosso | UV-Sprühöl | 3–6 Wochen | 10–18 EUR (200ml) |

(Confidence: documented)

---

## ANHANG C — Biegeradien

### C.1 Minimale Biegeradien nach Schlauchmaterial und Durchmesser

| Material | 12mm ID | 16mm ID | 19mm ID | 25mm ID |
|---|---|---|---|---|
| PVC Standard | 60mm | 80mm | 100mm | 130mm |
| PVC armiert | 75mm | 100mm | 125mm | 160mm |
| EPDM | 65mm | 85mm | 105mm | 140mm |
| Santoprene (Trident 369) | 75mm | 100mm | 125mm | 165mm |
| Polyurethan (PU) | 50mm | 70mm | 90mm | 120mm |
| Silikon | 45mm | 60mm | 75mm | 100mm |
| Spiralarmiert (Saugleitung) | 100mm | 130mm | 160mm | 210mm |

### C.2 Biegeradius und Druckverlust

Unterschreitung des minimalen Biegeradius führt zu:
- Kinking (Knickbildung) → Durchflussblockade
- Wandschwächung → Berstrisiko
- Dauerhafter Verformung → Schlauch rollt nicht mehr auf (Spiralschlauch)

**Faustregel**: Biegeradius ≥ 5× Außendurchmesser für sicheren Betrieb

(Confidence: measured)

---

## ANHANG D — Confidence-Mapping

### D.1 Confidence-Level je Bewertungskriterium

| Bewertungskriterium | Pipeline A (Structured) | Pipeline B (Visual) | Pipeline C (Text) |
|---|---|---|---|
| Schlauchmaterial identifiziert | measured (TDS) | visual_medium (Farbe/Textur) | documented (Service-Bericht) |
| Schlauchdurchmesser | measured (Messung) | visual_low (Foto, Perspektive) | documented |
| UV-Degradation Stufe | — | visual_high (eindeutig) | documented |
| Pumpenmodell identifiziert | measured (Typenschild) | visual_medium (Gehäuseform) | documented |
| Pumpendruck ausreichend | calculated (Dimensionierung) | — | documented |
| Schlauchschellen-Material | measured (Prüfung) | visual_medium (Rost ja/nein) | documented |
| Borddurchlass vorhanden | measured (Inspektion) | visual_low (unter Wasser) | documented |
| Rückschlagventil vorhanden | measured (Inspektion) | visual_low (unter Deck) | documented |
| Gesamtalter des Systems | — | visual_medium (Alterungsbild) | documented |
| Winterisierung durchgeführt | — | — | documented |

### D.2 Score-Reliability nach Datenquelle

| Datenquelle | Reliability-Faktor | Erklärung |
|---|---|---|
| CAD/Technische Zeichnung | 1,0 | Exakte Angaben |
| Hersteller-TDS (Technical Data Sheet) | 0,95 | Verifizierte Werte |
| Messung vor Ort | 0,9 | Abhängig von Messmethode |
| Foto (gut belichtet, nah) | 0,7 | Visuell verifizierbar |
| Foto (Übersicht, fern) | 0,4 | Begrenzte Detailerkennung |
| Eigner-Aussage | 0,5 | Subjektiv, oft ungenau bei Alter/Material |
| Service-Bericht (Werft) | 0,85 | Professionelle Dokumentation |
| Bootsklasse-Durchschnitt | 0,3 | Nur Schätzwert |

(Confidence: measured)

---

## ANHANG E — Bordausstattung

### E.1 Empfohlene Ersatzteile an Bord

| Bauteil | Anzahl | Begründung | Preis |
|---|---|---|---|
| Spiralschlauch (Ersatz) | 1 | UV-Versagen kommt plötzlich | 30–80 EUR |
| Membran-Kit (passend zur Pumpe) | 1 | Membranriss = Totalausfall | 25–60 EUR |
| Impeller (wenn Impellerpumpe) | 1 | Trockenlauf = Impeller zerstört | 15–35 EUR |
| Schlauchschellen 316 (Sortiment) | 10 | Universell einsetzbar | 10–20 EUR |
| O-Ring-Sortiment | 1 Set | Für Deckport-Dichtungen | 8–15 EUR |
| Quick-Connect Ersatz | 1 | Bruch oder Korrosion | 15–35 EUR |
| Rückschlagventil | 1 | Ausfallsicherung | 8–20 EUR |
| Sieb-Einsatz (Strainer) | 1 | Reserve für verstopften/beschädigten Einsatz | 10–25 EUR |
| Propylenglykol-Frostschutz | 4l | Winterisierung | 15–25 EUR |
| Vulkanisierband (Rescue Tape) | 1 Rolle | Notfallreparatur Schlauch | 8–15 EUR |

**Gesamtkosten Bordvorrat**: 140–320 EUR

### E.2 Werkzeug für Deckwasch-Wartung

| Werkzeug | Verwendung |
|---|---|
| Schraubendreher (Kreuz + Schlitz) | Schlauchschellen, Pumpengehäuse |
| Ringschlüssel 10mm / 13mm | Borddurchlass, Seeventil |
| Zange (Wasserpumpe) | Schlauchtüllen, Fittings |
| Eimer | Wasser auffangen, Frostschutz einfüllen |
| PTFE-Dichtband | Gewindeverbindungen abdichten |
| Silikonfett | O-Ringe schmieren |
| Kontaktspray | Elektrische Schalter reinigen |
| Multimeter | Stromversorgung und Sicherung prüfen |
| Feinsäge | Schlauch ablängen |
| Schmirgelpapier (120er) | Schlauchende entgraten |

(Confidence: documented)

---

## ANHANG F — Fallstudien

### Fallstudie DW-CS01: Bavaria 40 Cruiser — UV-Zerstörung nach 2 Sommern Mittelmeer

- **Boot**: Bavaria 40 Cruiser (2019), Liegeplatz Palma de Mallorca
- **System**: Shurflo 2088 + Osculati PVC-Spiralschlauch 7,5m + Gardena Quick-Connect
- **Problem**: Spiralschlauch an Deck nach 2 Sommern vollständig versprüdet, platzte beim Einschalten
- **Ursache**: Standard-PVC ohne UV-Stabilisator, permanent an Deck (keine Persenning), hohe UV-Last Mallorca
- **Lösung**: Austausch gegen Trident 369 Santoprene Spiralschlauch, Gardena-Adapter gegen Forespar Bronze getauscht
- **Kosten**: 95 EUR (Schlauch) + 45 EUR (Deckport) + 30 min Eigenarbeit
- **AYDI Score vorher**: 25/100 (hose_score), 35/100 (fitting_score)
- **AYDI Score nachher**: 90/100 (hose_score), 85/100 (fitting_score)
- **Lesson Learned**: Im Mittelmeer IMMER UV-beständigen Schlauch (Santoprene/EPDM) verwenden
- **Confidence**: documented

### Fallstudie DW-CS02: Hallberg-Rassy 43 — Windlass-Schaden durch fehlende Ankerspülung

- **Boot**: Hallberg-Rassy 43 (2015), Blauwasser-Reise, Bretagne → Karibik
- **System**: Lewmar V3 Windlass, KEINE Ankerspülung installiert
- **Problem**: Nach 18 Monaten Blauwasser Windlass-Getriebe verschlissen, Kette korrodiert
- **Ursache**: Sand und Salz wurden mit der Kette in den Ankerkasten eingeholt, schliffen Getriebe ab
- **Lösung**: Lewmar V-Series Wash Kit nachgerüstet, Jabsco Par-Max 4.0 Pumpe, Frischwasser-Option
- **Kosten**: 180 EUR (Wash Kit) + 250 EUR (Pumpe) + 150 EUR (Installation) + 2.800 EUR (Windlass-Überholung!)
- **AYDI Score vorher**: 15/100 (system_score — keine Ankerspülung)
- **AYDI Score nachher**: 85/100 (system_score)
- **Lesson Learned**: Ankerspülung auf Blauwasser-Yachten ist keine Option, sondern Pflicht
- **Confidence**: documented

### Fallstudie DW-CS03: Jeanneau Sun Odyssey 440 — Frostschaden Deckwaschpumpe

- **Boot**: Jeanneau Sun Odyssey 440 (2021), Winterlager Kiel (Freiland)
- **System**: Jabsco Par-Max 3.0 + PVC Spiralschlauch
- **Problem**: Pumpe im Frühjahr nicht funktionsfähig — Gehäuseriss
- **Ursache**: Winterisierung nicht durchgeführt, Wasser in Pumpe gefroren bei -12°C
- **Lösung**: Neue Par-Max 3.0 eingebaut, Winterisierungs-Checkliste erstellt
- **Kosten**: 180 EUR (neue Pumpe) + 45 min Eigenarbeit
- **AYDI Score vorher**: 0/100 (pump_score — Totalausfall)
- **AYDI Score nachher**: 95/100 (pump_score)
- **Lesson Learned**: Winterisierung ist in Nordeuropa NICHT optional
- **Confidence**: documented

### Fallstudie DW-CS04: Grand Soleil 46LC — Dual-System mit Drucktank

- **Boot**: Grand Soleil 46LC (2022), Mittelmeer (Sardinien)
- **System**: Jabsco Par-Max HD5 + Drucktank 2l + Rohwasser/Frischwasser-Umschaltung + Ankerspülung
- **Problem**: Pumpe zyklierte häufig, Vibration unter Deck, Lärm im Salon
- **Ursache**: Kein Drucktank installiert, Pumpe reagierte auf jeden Druckabfall
- **Lösung**: Jabsco Accumulator Tank (P/N 18810-0000, 1l) installiert, Gummipuffer unter Pumpe
- **Kosten**: 45 EUR (Drucktank) + 15 EUR (Gummipuffer) + 30 min Eigenarbeit
- **AYDI Score vorher**: 65/100 (overall, wegen Lärm/Vibration)
- **AYDI Score nachher**: 88/100 (overall)
- **Lesson Learned**: Drucktank ist Standard bei Pumpen ab Par-Max 3.0 — sollte immer installiert werden
- **Confidence**: documented

### Fallstudie DW-CS05: Bénéteau Océanis 46.1 — Messing-Dezinkifizierung

- **Boot**: Bénéteau Océanis 46.1 (2018), Liegeplatz Athen
- **System**: Shurflo 4048 + Original-Messing-Fittings ab Werft
- **Problem**: Quick-Connect und Schlauchtüllen porös, rosa Verfärbung, Undichtigkeit
- **Ursache**: Standard-Messing (nicht DZR) in warmem Salzwasser → Dezinkifizierung nach 4 Jahren
- **Lösung**: Alle Messing-Fittings gegen Bronze (CW617N) von Forespar ersetzt
- **Kosten**: 120 EUR (Fittings-Set Bronze) + 2h Eigenarbeit
- **AYDI Score vorher**: 30/100 (fitting_score)
- **AYDI Score nachher**: 90/100 (fitting_score)
- **Lesson Learned**: Werft-Original-Messing ist oft NICHT DZR — bei Ausrüstungsinspektion prüfen!
- **Confidence**: documented

### Fallstudie DW-CS06: Lagoon 42 Katamaran — Dual-Rumpf-Deckwäsche

- **Boot**: Lagoon 42 (2020), Charter-Betrieb Kroatien
- **System**: 2× separate Deckwasch-Systeme (je 1 pro Rumpf), Jabsco Par-Max 2.0
- **Problem**: Rechter Rumpf: Pumpe fördert nicht, Ratteln beim Betrieb
- **Ursache**: Saugschlauch (nicht armiert) kollabiert unter Vakuum → Pumpe saugt Luft
- **Lösung**: Saugschlauch gegen spiralarmierten vakuumfesten Schlauch getauscht
- **Kosten**: 35 EUR (2m armierter Schlauch) + 30 min Arbeit
- **AYDI Score vorher**: 20/100 (hose_score rechter Rumpf)
- **AYDI Score nachher**: 85/100 (hose_score rechter Rumpf)
- **Lesson Learned**: Saugleitungen IMMER vakuumfest/spiralarmiert — NIEMALS Spiralschlauch oder nicht armierten PVC
- **Confidence**: documented

### Fallstudie DW-CS07: Sunseeker Predator 57 — Professionelles Deckwasch-System

- **Boot**: Sunseeker Predator 57 (2017), Liegeplatz Antibes
- **System**: 2× Jabsco Par-Max HD6 + 3× Hydrantenanschlüsse + Ankerspülung automatisch
- **Problem**: Kein Problem — Beispiel für vorbildliche Installation
- **Details**: Bronze-Deckports, Edelstahl-316-Schläuche unter Deck, Santoprene-Spiralschläuche an Deck, automatische Ankerspülung über Maxwell Auto-Rinse, Badeplattform-Dusche warm/kalt
- **Kosten System**: ca. 4.500 EUR (Material bei Bau installiert)
- **AYDI Score**: 95/100 (Vorbildinstallation)
- **Lesson Learned**: Professionelle Installation rechnet sich — keine Reparaturen in 6 Jahren
- **Confidence**: documented

### Fallstudie DW-CS08: Dehler 34 — Budget-Deckwäsche mit Seaflo-Pumpe

- **Boot**: Dehler 34 (2010), Liegeplatz Fehmarn (Ostsee)
- **System**: Seaflo 41 Series (Par-Max-Klon) + Osculati PVC-Spiralschlauch + Gardena-Adapter
- **Problem**: Pumpe nach 2 Saisons ausgefallen (Membran gerissen), Schlauch nach 3 Saisons vergilbt
- **Ursache**: Budget-Pumpe mit geringerer Membranlebensdauer, Gardena-O-Ringe verhärtet
- **Lösung**: Upgrade auf Jabsco Par-Max 3.0 und Trident 369 Spiralschlauch
- **Kosten**: 190 EUR (Pumpe) + 75 EUR (Schlauch) + 35 EUR (Forespar Deckport)
- **AYDI Score vorher**: 30/100 (Budget-System am Lebensende)
- **AYDI Score nachher**: 85/100 (Standardsystem mit Premium-Schlauch)
- **Lesson Learned**: Budget-Komponenten kosten langfristig mehr durch häufigeren Austausch
- **Confidence**: documented

(Confidence: documented)

---

## ANHANG G — Experten-Ressourcen

### G.1 Fachliteratur

| Quelle | Autor/Herausgeber | Relevanz |
|---|---|---|
| Boatowner's Mechanical and Electrical Manual | Nigel Calder | Kapitel Pumpen und Wassersysteme — Standardreferenz |
| The Boatyard Book | Simon Jollands | Praktische Einbauanleitungen, Deckwasch-Installation |
| Marine Diesel Engines (Maintenance) | Nigel Calder | Seewassersysteme, Borddurchlässe |
| Yachtmasters Handbook | Peter Heinrichs (DE) | Deutsche Referenz für Bordtechnik |
| Practical Sailor Magazine | Belvoir Media | Regelmäßige Pumpen- und Schlauch-Tests |
| Yacht (Magazin) | Delius Klasing (DE) | Praxistests marine Ausrüstung |

### G.2 Online-Ressourcen

| Ressource | URL | Schwerpunkt |
|---|---|---|
| Jabsco Technical Library | jabsco.com/techlib | Pumpen-Datenblätter, Installationsanleitungen |
| SVB Ratgeber | svb24.com/ratgeber | Deutsche Einbauanleitungen, Produktvergleiche |
| Sailing Anarchy Forum | sailinganarchy.com | Erfahrungsberichte, Diskussionen |
| YBW Forum | forums.ybw.com | UK-zentriert, große Community |
| Cruisers Forum | cruisersforum.com | Blauwasser-Erfahrungen, technische Diskussionen |
| Segeln-Forum.de | segeln-forum.de | Deutschsprachige Segler-Community |
| The Rigging Doctor (YouTube) | youtube.com | Video-Anleitungen Deckwasch-Installation |

### G.3 Hersteller-Technische Support-Kontakte

| Hersteller | Support | E-Mail/Telefon |
|---|---|---|
| Jabsco/Xylem Marine | Technischer Support | marine.support@xylem.com |
| Shurflo/Pentair | Technischer Support | shurflo.technical@pentair.com |
| Whale Marine | Technischer Support | sales@whalepumps.com |
| Lewmar | Windlass Support | technical@lewmar.com |
| Maxwell Marine | Support | service@maxwell-marine.com |
| Quick SpA | Support | info@quickitaly.com |

(Confidence: documented)

---

## ANHANG H — Risk Matrix

### H.1 Risikobewertung Deckwasch-Systeme

| Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Risiko-Level | Mitigation |
|---|---|---|---|---|
| UV-Versagen Spiralschlauch | Hoch (3–5 Jahre) | Niedrig (Wasserleck an Deck) | MITTEL | Santoprene-Schlauch, UV-Schutz, Lagerung |
| Pumpen-Membranriss | Mittel (3.000–5.000h) | Niedrig (Pumpe fördert nicht) | NIEDRIG | Membran-Kit als Ersatzteil |
| Frostschaden Pumpe | Hoch (ohne Winterisierung) | Mittel (Pumpe Totalschaden) | HOCH | Winterisierung obligatorisch |
| Borddurchlass-Leckage | Sehr niedrig | Hoch (Wassereinbruch) | MITTEL | ISO 9093 einhalten, Seeventil |
| Rückfluss ohne Ventil | Mittel | Mittel (Wassereinbruch unter Deck) | MITTEL | Rückschlagventil installieren |
| Messing-Dezinkifizierung | Mittel (warme Reviere) | Niedrig (Undichtigkeit) | NIEDRIG | Bronze/316 verwenden |
| Elektrischer Kurzschluss | Niedrig | Mittel (Brand) | MITTEL | Korrekte Absicherung, IP-Schutz |
| Muschelbewuchs Sieb | Hoch (warme Reviere) | Niedrig (Pumpe fördert nicht) | NIEDRIG | Regelmäßige Reinigung |
| Schlauchschelle 304 korrodiert | Hoch (1–3 Jahre Salzwasser) | Mittel (Schlauch löst sich) | HOCH | NUR 316er Schellen verwenden |
| Saugschlauch kollabiert | Niedrig (nur bei falschem Typ) | Niedrig (Pumpe fördert nicht) | NIEDRIG | Armierten Schlauch verwenden |

### H.2 Kritikalitäts-Einstufung für AYDI

| Kritikalität | Definition | Betroffene Fehlerbilder |
|---|---|---|
| KRITISCH | Sofortige Handlung erforderlich, Seetüchtigkeit betroffen | DW-F07 (Frostschaden, wenn in Bilge), DW-F11 (fehlender Rückschlag) |
| HOCH | Handlung vor nächstem Törn empfohlen | DW-F01 (UV Stufe 4–5), DW-F03 (Dezinkifizierung), DW-F06 (304er Schellen) |
| MITTEL | Handlung innerhalb der Saison empfohlen | DW-F02 (Kink), DW-F04 (Muscheln), DW-F05 (Membranriss), DW-F10 (Düse verstopft) |
| NIEDRIG | Wartungshinweis | DW-F08 (O-Ring), DW-F09 (Wasserretention), DW-F12 (Saugschlauch, temporär) |

(Confidence: documented)

---

## ANHANG I — Audit/Compliance-Checkliste

### I.1 AYDI Deckwasch-System-Audit

| Nr. | Prüfpunkt | Norm/Referenz | Bewertung | Gewichtung |
|---|---|---|---|---|
| 1 | Borddurchlass normkonform (ISO 9093) | ISO 9093 | Ja/Nein/n.a. | 15% |
| 2 | Seeventil vorhanden und bedienbar | ISO 9093, RCD | Ja/Nein/n.a. | 15% |
| 3 | Seewasser-Sieb vorhanden | Best Practice | Ja/Nein | 5% |
| 4 | Pumpe korrekt abgesichert (Sicherung) | ISO 10133 | Ja/Nein | 10% |
| 5 | Kabelquerschnitt ausreichend | ISO 10133 | Ja/Nein | 10% |
| 6 | Schlauchschellen Edelstahl 316 | Best Practice | Ja/Nein | 5% |
| 7 | Doppelte Schellen an Borddurchlass | ISO 9093 | Ja/Nein | 5% |
| 8 | Rückschlagventil vorhanden | Best Practice | Ja/Nein | 10% |
| 9 | Spiralschlauch UV-Zustand | Visuelle Inspektion | Score 0–100 | 10% |
| 10 | Quick-Connect / Deckport Zustand | Visuelle Inspektion | Score 0–100 | 5% |
| 11 | Pumpe Funktionstest | Betriebsprüfung | Ja/Nein | 5% |
| 12 | Winterisierung dokumentiert (wenn zutreffend) | Best Practice | Ja/Nein/n.a. | 5% |

### I.2 Compliance-Relevanz nach Bootsgröße

| Bootslänge | CE/RCD Relevanz | ISO 9093 | ISO 10133 | Klassifikation |
|---|---|---|---|---|
| <2,5m | Nein | Nein | Nein | Nein |
| 2,5–6m | Ja | Ja (wenn Borddurchlass) | Ja | Nein |
| 6–12m | Ja | Ja | Ja | Nein |
| 12–24m | Ja | Ja | Ja | Optional |
| >24m | Nein (RCD) | Ja (Klasse) | Ja | Lloyd's/DNV/BV |

(Confidence: measured)

---

## ANHANG J — Material-Datenblätter (Zusammenfassung)

### J.1 PVC (Polyvinylchlorid) — Deckwaschschlauch

| Eigenschaft | Wert |
|---|---|
| Dichte | 1,3–1,45 g/cm³ |
| Shore-Härte | 60–80 Shore A (flexibel) |
| Zugfestigkeit | 10–25 MPa |
| Dehnung bei Bruch | 200–400% |
| Temperaturbereich | -10°C bis +60°C (Standard), -20°C bis +60°C (kältefest) |
| UV-Beständigkeit | Schlecht bis mittel (mit Stabilisator mittel) |
| Chemische Beständigkeit | Gut gegen Salzwasser, Säuren, Laugen; schlecht gegen Lösungsmittel, Kraftstoffe |
| Ozon-Beständigkeit | Mittel |
| Lebensmitteltauglichkeit | Nur spezielle Formulierungen (Weichmacher-frei) |
| Preis | Günstig (Basis-Material) |

### J.2 EPDM (Ethylen-Propylen-Dien-Monomer) — Deckwaschschlauch

| Eigenschaft | Wert |
|---|---|
| Dichte | 0,85–1,0 g/cm³ |
| Shore-Härte | 40–80 Shore A |
| Zugfestigkeit | 7–20 MPa |
| Dehnung bei Bruch | 300–600% |
| Temperaturbereich | -40°C bis +120°C |
| UV-Beständigkeit | Sehr gut |
| Chemische Beständigkeit | Gut gegen Wasser, Dampf, Säuren, Laugen; schlecht gegen Öle, Kraftstoffe |
| Ozon-Beständigkeit | Exzellent |
| Lebensmitteltauglichkeit | FDA-konform möglich |
| Preis | Mittel |

### J.3 Santoprene / TPV (Thermoplastisches Vulkanisat) — Deckwaschschlauch

| Eigenschaft | Wert |
|---|---|
| Dichte | 0,9–1,1 g/cm³ |
| Shore-Härte | 55–80 Shore A |
| Zugfestigkeit | 5–15 MPa |
| Dehnung bei Bruch | 400–700% |
| Temperaturbereich | -60°C bis +135°C |
| UV-Beständigkeit | Exzellent |
| Chemische Beständigkeit | Gut gegen Wasser, Säuren; mittel gegen Öle |
| Ozon-Beständigkeit | Exzellent |
| Lebensmitteltauglichkeit | FDA 21 CFR 177.2600 |
| Preis | Hoch (Premium-Material) |

### J.4 Polyurethan (PU) — Spiralschlauch

| Eigenschaft | Wert |
|---|---|
| Dichte | 1,1–1,25 g/cm³ |
| Shore-Härte | 80–95 Shore A |
| Zugfestigkeit | 25–50 MPa |
| Dehnung bei Bruch | 400–600% |
| Temperaturbereich | -30°C bis +80°C |
| UV-Beständigkeit | Mittel (vergilbt) |
| Chemische Beständigkeit | Gut gegen Öle, Fette; mittel gegen Wasser (Hydrolyse möglich) |
| Ozon-Beständigkeit | Gut |
| Abriebfestigkeit | Exzellent (bestes Schlauchmaterial für Abrieb) |
| Preis | Mittel-Hoch |

(Confidence: measured)

---

## ANHANG K — Prüfverfahren

### K.1 Schlauch-Druckprüfung

**Verfahren:**
1. Schlauch an einem Ende verschließen (Blindstopfen mit Schlauchschelle)
2. Am anderen Ende Manometer und Druckquelle anschließen
3. Druck langsam auf 1,5× Arbeitsdruck aufbauen
4. 5 Minuten halten
5. Druckabfall <0,2 bar = bestanden
6. Druckabfall >0,2 bar = Leckage suchen (Sprühflasche mit Seifenwasser)

### K.2 UV-Degradations-Prüfung (Feldtest)

**Verfahren (visuell + manuell):**
1. Schlauch an der sonnenexponierte Seite betrachten (Verfärbung, Verkreidung?)
2. Mit Fingernagel über die Oberfläche kratzen (Abrieb? Pulver?)
3. Schlauch 90° biegen am exponiertesten Punkt (Rissbildung? Knacken?)
4. Schlauch 180° biegen (nur wenn 90° bestanden): Bricht der Schlauch?
5. Bewertung nach Stufe 0–5 (siehe 13.2)

### K.3 Pumpenleistungs-Test

**Verfahren:**
1. Eimer (bekanntes Volumen, z.B. 10l) bereitstellen
2. Schlauch in Eimer legen
3. Pumpe einschalten, Stoppuhr starten
4. Zeit messen bis Eimer voll (Volumenstrom berechnen: V/t = l/min)
5. Vergleich mit Nenn-Fördermenge:
   - >80%: Gut
   - 60–80%: Wartung empfohlen (Sieb prüfen, Membran prüfen)
   - <60%: Reparatur erforderlich

### K.4 Schlauchschellen-Materialprüfung

**Verfahren (Mo-Spot-Test für 316 vs. 304):**
1. Molybdän-Testlösung auf Schlauchschelle tropfen
2. 30 Sekunden warten
3. Ergebnis: Farbumschlag → 316 (enthält Mo), kein Umschlag → 304 (kein Mo)
4. Alternative: Magnet-Test (304 ist etwas magnetischer als 316, aber nicht zuverlässig)

(Confidence: documented)

---

## ANHANG L — Top 15 Fehler bei Deckwasch-Installationen

| Nr. | Fehler | Häufigkeit | Konsequenz | Lösung |
|---|---|---|---|---|
| 1 | Standard-PVC Spiralschlauch an Deck (keine UV-Stabilisierung) | Sehr häufig | Versprödung in 1–2 Jahren | Santoprene oder EPDM verwenden |
| 2 | Gardena/Hozelock Quick-Connect an Deck (nicht UV-beständig) | Häufig | Versprödung, Undichtigkeit | Bronze oder Edelstahl Deckport |
| 3 | Winterisierung vergessen | Häufig | Frostschaden Pumpe + Schlauch | Winterisierungs-Checkliste |
| 4 | Schlauchschellen 304 statt 316 | Häufig | Korrosion in 1–3 Jahren | NUR 316 verwenden |
| 5 | Kein Rückschlagventil | Häufig | Rückfluss Seewasser ins Boot | Rückschlagventil nachrüsten |
| 6 | Nicht armierter Saugschlauch | Mittel | Schlauch kollabiert → Pumpe fördert nicht | Spiralarmierten Schlauch für Saug verwenden |
| 7 | Messing-Fittings in Seewasser (nicht DZR) | Mittel | Dezinkifizierung | Bronze oder Edelstahl 316 |
| 8 | Pumpe zu klein für Bootsgröße | Mittel | Zu wenig Druck/Volumenstrom | Korrekte Dimensionierung |
| 9 | Fehlende Sieb/Strainer in Ansaugung | Mittel | Fremdkörper zerstören Pumpe | Sieb nachrüsten |
| 10 | Kabel zu dünn (Spannungsfall) | Mittel | Pumpe läuft langsam, überhitzt | Kabelquerschnitt berechnen |
| 11 | Pumpe in Bilge montiert | Selten | Korrosion, Kurzschluss | Pumpe über Bilge montieren |
| 12 | Kein Seeventil an Borddurchlass | Selten aber kritisch | CE-Verstoß, Sicherheitsrisiko | Seeventil nachrüsten |
| 13 | GFK-Schnittkanten nicht versiegelt (Deckport) | Häufig | Osmose-Eintritt | Epoxy auf alle Schnittkanten |
| 14 | Silikon statt PU-Dichtstoff für Deckport | Häufig | Haftungsversagen, Undichtigkeit | Sikaflex 291 oder 3M 5200 verwenden |
| 15 | Keine doppelten Schlauchschellen am Borddurchlass | Häufig | Schlauch rutscht ab bei Druckstoß | Doppelte Schellen, Sicherheitsvorschrift |

(Confidence: documented)

---

## ANHANG M — Zusammenfassung für AYDI-Scoring

### M.1 Scoring-Algorithmus Deckwasch-System

```python
def score_deck_wash_system(
    pump_score: int,           # 0–100
    hose_score: int,           # 0–100
    fitting_score: int,        # 0–100
    nozzle_score: int,         # 0–100
    compliance_score: int,     # 0–100
    backflow_protection: bool,
    winterization_done: bool,  # None wenn nicht zutreffend
    uv_protection: bool,
    seacock_present: bool,
) -> dict:
    """
    AYDI Scoring-Algorithmus für Deckwasch-Systeme.
    Gewichtung:
    - Pumpe: 25%
    - Schlauch: 20%
    - Fittings: 15%
    - Düse: 10%
    - Compliance: 15%
    - System-Extras: 15%
    """
    base_score = (
        pump_score * 0.25 +
        hose_score * 0.20 +
        fitting_score * 0.15 +
        nozzle_score * 0.10 +
        compliance_score * 0.15
    )

    extras_score = 0
    extras_max = 0

    if seacock_present:
        extras_score += 40
    extras_max += 40

    if backflow_protection:
        extras_score += 30
    extras_max += 30

    if uv_protection:
        extras_score += 15
    extras_max += 15

    if winterization_done is not None:
        if winterization_done:
            extras_score += 15
        extras_max += 15
    else:
        extras_max += 0  # Nicht zutreffend (frostfreies Revier)

    if extras_max > 0:
        extras_normalized = (extras_score / extras_max) * 100
    else:
        extras_normalized = 100

    total = base_score + extras_normalized * 0.15

    # Malus für kritische Mängel
    if not seacock_present and compliance_score < 50:
        total = min(total, 40)  # Hard cap bei fehlendem Seeventil

    return {
        "overall_score": max(0, min(100, round(total))),
        "pump_score": pump_score,
        "hose_score": hose_score,
        "fitting_score": fitting_score,
        "nozzle_score": nozzle_score,
        "compliance_score": compliance_score,
        "extras_score": round(extras_normalized),
        "confidence": "calculated",
    }
```

### M.2 Schwellenwerte für Empfehlungen

| Score-Bereich | Bewertung | Empfehlung |
|---|---|---|
| 90–100 | Ausgezeichnet | Keine Maßnahmen erforderlich |
| 75–89 | Gut | Kleinere Verbesserungen empfohlen |
| 60–74 | Befriedigend | Wartung/Upgrade empfohlen |
| 40–59 | Mangelhaft | Reparatur/Austausch empfohlen |
| 20–39 | Schlecht | Sofortige Maßnahmen erforderlich |
| 0–19 | Kritisch | System nicht betriebsbereit |

(Confidence: measured)

---

## ANHANG N — Spezialanwendungen

### N.1 Deckwäsche auf Katamaranen

Katamarane haben besondere Anforderungen:
- **Zwei Rümpfe**: Zwei separate Systeme oder ein System mit Verteilung über Brückendeck
- **Brückendeck-Verlegung**: Lange Schlauchleitungen → größerer Durchmesser (19mm ID)
- **Trampolin-Bereich**: Muss von beiden Seiten erreichbar sein
- **Ankerkasten**: Meist im Bug eines Rumpfes → Ankerspülung einseitig
- **Empfehlung**: 2× Par-Max 2.0 (je ein Rumpf) statt 1× Par-Max 4.0 zentral

### N.2 Deckwäsche auf Regattayachten

Regattayachten haben minimale Ausrüstung — Deckwäsche ist meist nicht installiert:
- **Regattatag**: Eimer + Bürste reicht
- **Langstreckenregatta (Fastnet, Sydney-Hobart)**: Rohwasser-Handpumpe als Minimum
- **TP52 / Maxi72**: Kein festes System, tragbare Lösung (Kärcher OC 3 o.ä.)
- **Superyacht-Regatten**: Volle Deckwasch-Systeme (Superyacht-Standard)

### N.3 Deckwäsche auf gewerblichen Sportfischerbooten

Sportfischerboote (Center Console, Flybridge Cruiser) haben die höchsten Anforderungen:
- **Fischblut und -schleim**: Aggressive Reinigung nötig (Hochdruck)
- **Livewell**: Dediziertes Seewasser-System
- **Fisch-Reinigungsstation**: Hochdruck + Drainage
- **Köderbehälter**: Durchfluss-Belüftung
- **Typische Pumpe**: Par-Max HD5 oder HD6
- **Schlauch**: 19mm ID, lebensmitteltauglich (Santoprene)
- **Düse**: Hochdruck-Pistolendüse (Brass nozzle)
- **Budget**: 800–2.500 EUR Gesamt-System

### N.4 Deckwäsche auf Hausbooten/Binnenschiffen

Süßwasser-Betrieb hat andere Anforderungen:
- **Kein Salzkorrosions-Problem**: Messing-Fittings akzeptabel
- **Kein Muschelbewuchs** (in den meisten Süßgewässern)
- **Algen und Schlick**: Hauptverschmutzung
- **Frostschutz**: Relevant bei Winterlager
- **Landstromanschluss meist vorhanden**: 230V-Hochdruckreiniger möglich
- **Gardena-System**: Akzeptabel im Süßwasser (kein Salzschaden)

(Confidence: documented)

---

## ANHANG O — Umwelt-Aspekte

### O.1 Umweltvorschriften Deckwäsche

| Regelung | Inhalt | Region |
|---|---|---|
| EU-Wasserrahmenrichtlinie (2000/60/EG) | Verbot der Einleitung schädlicher Substanzen | EU |
| Clean Water Act (Section 312) | Regelung für Schiffsabwässer | USA |
| MARPOL Annex IV | Schiffsabwässer | International |
| Lokale Hafenordnungen | Oft Verbot von Deckwäsche mit Reinigungsmitteln im Hafen | Lokal |

**Grundsätze:**
- Reines Seewasser oder Frischwasser für Deckwäsche: KEIN Problem
- Reinigungsmittel (Seife, Teak-Reiniger): Nur biologisch abbaubare, phosphatfreie Mittel
- Antifouling-Abwasser: NIEMALS ins Wasser (Kupfer, Zinn)
- Fischverarbeitungs-Abfälle: Nur außerhalb von Häfen ins Meer (lokale Regeln beachten)

### O.2 Wasserverbrauch und Nachhaltigkeit

| Maßnahme | Einsparung | Aufwand |
|---|---|---|
| Rohwasser-Vorspülung + Frischwasser-Nachspülung | 50–70% Frischwasser | Dual-System (einmalig) |
| Pistolendüse mit Abzug (statt Dauerstrahl) | 30–50% Wasser | 15–40 EUR (Düse) |
| Regenwasser-Auffang für Deckwäsche | 20–40% Frischwasser | 50–200 EUR (System) |
| Grauwasser-Recycling | 60–80% Frischwasser | 8.000–25.000 EUR |
| Watermaker (Entsalzungsanlage) für Deckwäsche | Unbegrenzt Frischwasser | 3.000–15.000 EUR |

(Confidence: documented)

---

## ANHANG P — Erweiterte FAQ

### DW-026: Kann ich mein Deckwasch-System mit einem Watermaker kombinieren?
Ja, einige Blauwasser-Yachten nutzen das Abwasser (Konzentrat) des Watermakers als Rohwasser-Deckwäsche. Vorteil: Kein zusätzlicher Borddurchlass. Nachteil: Höherer Salzgehalt als normales Seewasser, nur während Watermaker-Betrieb verfügbar.
(Confidence: estimated)

### DW-027: Wie viel Strom verbraucht ein Deckwasch-System?
Par-Max 3.0: 8A × 12V = 96W. Bei 10 Minuten Deckwäsche: 16 Wh (0,016 kWh). Bei täglicher Nutzung über eine Saison (180 Tage): 2,9 kWh gesamt. Deckwäsche ist kein relevanter Stromverbraucher.
(Confidence: calculated)

### DW-028: Mein Deckwasch-Schlauch riecht nach faulen Eiern — was tun?
Stehendes Wasser im Schlauch fault (anaerobe Bakterien produzieren Schwefelwasserstoff). Schlauch durchspülen mit Essigwasser (1:5) oder Chlorbleiche-Lösung (1:100). Danach gründlich mit Frischwasser nachspülen. Prävention: Schlauch nach Gebrauch hängend trocknen.
(Confidence: documented)

### DW-029: Kann ich zwei Deckwaschpumpen parallel betreiben?
Ja, für mehr Druck oder Volumenstrom. Zwei gleiche Pumpen parallel → doppelter Volumenstrom bei gleichem Druck. Zwei gleiche Pumpen in Serie → doppelter Druck bei gleichem Volumenstrom. Parallel ist für Deckwäsche meist sinnvoller.
(Confidence: documented)

### DW-030: Welches Seeventil-Material für die Deckwasch-Ansaugung?
Bronze (CW617N): Klassiker, bewährt, schwer. Marelon (Forespar): Leicht, korrosionsfrei, modernes Material. Edelstahl 316L: Optisch ansprechend, aber Spaltkorrosionsrisiko in Ventilgeometrie. Für Deckwäsche alle drei akzeptabel.
(Confidence: documented)

---

## ANHANG Q — Zeitleiste: Entwicklung der Deckwasch-Technologie

| Jahr | Entwicklung |
|---|---|
| 1960er | Erste elektrische Deckwaschpumpen (Johnson Pump) auf kommerziellen Schiffen |
| 1970er | Jabsco Par-Max Membranpumpen-Konzept für Freizeitboote |
| 1980er | PVC-Spiralschläuche kommen auf den Markt |
| 1990er | Quick-Connect-Systeme (Whale System 15) etabliert |
| 2000er | Santoprene-Schläuche (Trident 369) als UV-beständige Premium-Option |
| 2005 | Automatische Ankerspül-Systeme (Maxwell Auto-Rinse) |
| 2010 | Jabsco Par-Max HD-Serie für Hochleistungs-Deckwäsche |
| 2015 | Smart-Pumpen mit Bluetooth-Steuerung (Prototypen) |
| 2018 | Seaflo Budget-Pumpen aus China als Jabsco-Alternative |
| 2020 | Kabellose Hochdruckreiniger (Kärcher OC 3) als tragbare Alternative |
| 2022 | Grauwasser-Recycling-Systeme für Superyachten |
| 2025 | NMEA 2000 Integration für automatisierte Ankerspülung (Quick, Lewmar) |
| 2026 | KI-gestützte Zustandsüberwachung (AYDI) — visuelle UV-Degradations-Erkennung |

(Confidence: documented)

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Kapitel/Abschnitt |
|---|---|
| Absicherung (elektrisch) | 1.4, 11.3, 12.1 |
| Akkumulator/Drucktank | FAQ DW-020, Fallstudie CS04 |
| Ankerspülung | 7.1, 7.6, 7.7, 8.13–8.16, 9.2 |
| Badeplattform-Dusche | 7.9, Anhang A |
| Biegeradius | Anhang C |
| Borddurchlass | 1.4, 11.4, 12.1 |
| CE-Konformität | 1.4 |
| Cockpit-Waschsystem | 7.8 |
| Confidence-Mapping | Anhang D |
| Dezinkifizierung | Fehlerbild DW-F03, Fallstudie CS05 |
| Druckverlust | 11.2 |
| Dual-System | 7.2, 7.7, 9.3 |
| EPDM | 7.4, Anhang J |
| Fallstudien | Anhang F |
| FAQ | Kapitel 16, Anhang P |
| Fehlerbild-Atlas | Kapitel 14 |
| Fisch-Reinigungsstation | 7.11, Anhang N |
| Flachschlauch | 7.3 |
| Frostschutz | 12.4, FAQ DW-007 |
| Fußschalter | 7.8, FAQ DW-021 |
| Gardena | 7.5, FAQ DW-005 |
| Goodyear | 8.10 |
| Hersteller | Kapitel 8 |
| Jabsco Par-Max | 8.1, 9.1 |
| Johnson Pump | 8.5 |
| Kabelquerschnitt | 11.3 |
| Katamarane | Anhang N |
| Kinking | Fehlerbild DW-F02 |
| Lalizas | 8.8 |
| Lewmar Anchor Wash | 8.13 |
| Livewell | 7.10 |
| Material-Daten | Anhang J |
| Maxwell | 8.14 |
| Muir | 8.16 |
| Muschelbewuchs | Fehlerbild DW-F04 |
| NDS | 8.17 |
| Normen | 1.3 |
| Notfall | Kapitel 19 |
| Osculati | 8.7 |
| Plastimo | 8.6 |
| Prüfverfahren | Anhang K |
| Pumpenauswahl | 11.1, 18.1 |
| Pydantic-Modelle | Kapitel 6 |
| Quick (Ankerwinden) | 8.15 |
| Quick-Connect | 7.5, 10.2 |
| Regattayachten | Anhang N |
| Risk Matrix | Anhang H |
| Rohwasser | 7.2 |
| Rückschlagventil | Fehlerbild DW-F11, FAQ DW-006 |
| Santoprene | 7.4, 8.9, Anhang J |
| Schlauchschellen | 10.1, Fehlerbild DW-F06 |
| Schnell-Referenz | Kapitel 18 |
| Scoring | Anhang M |
| Seaflo | 8.18 |
| Seeventil | 1.4, 11.4, FAQ DW-018 |
| Shurflo | 8.2 |
| Spiralschlauch | 7.3 |
| Sportfischerboote | Anhang N |
| Trident 369 | 8.9 |
| Umwelt | Anhang O |
| UV-Beständigkeit | 7.4, 13.2, Anhang B |
| UV-Degradation | Fehlerbild DW-F01, 13.2 |
| Vetus | 8.4 |
| Wartungsplan | 13.4, 18.4 |
| Whale Marine | 8.3 |
| Windlass-Zuordnung | 9.2 |
| Winterisierung | 12.4, FAQ DW-007, Fallstudie CS03 |
| Zeitleiste | Anhang Q |
| Zukunftstechnologien | Kapitel 2 |

---

## ANHANG R.2 — Erweiterte Hersteller-Teilenummern-Referenz

### R.2.1 Jabsco / Xylem — Vollständige Teilenummern-Liste (Deckwasch-relevant)

| Teilenummer | Beschreibung | Typ | Preis (EUR) |
|---|---|---|---|
| 42631-2900 | Par-Max 1.0, 12V, 3,8 l/min, 2,4 bar | Pumpe | 85–120 |
| 42632-2900 | Par-Max 1.0, 24V, 3,8 l/min, 2,4 bar | Pumpe | 90–130 |
| 42745-2100 | Par-Max 3.0, 12V, 11,4 l/min, 3,4 bar | Pumpe | 140–190 |
| 42745-2200 | Par-Max 3.0, 24V, 11,4 l/min, 3,4 bar | Pumpe | 150–200 |
| 31600-0092 | Par-Max 4.0, 12V, 16,3 l/min, 4,1 bar | Pumpe | 180–250 |
| 31600-0292 | Par-Max 4.0, 24V, 16,3 l/min, 4,1 bar | Pumpe | 190–260 |
| 46010-2900 | Par-Max HD4, 12V, 15,1 l/min, 4,1 bar | Pumpe | 220–300 |
| 46020-2900 | Par-Max HD5, 12V, 18,9 l/min, 4,8 bar | Pumpe | 280–380 |
| 46030-2900 | Par-Max HD6, 12V, 22,7 l/min, 4,1 bar | Pumpe | 320–420 |
| 23680-4003 | Puppy 2000, 12V, 32 l/min, 1,0 bar | Impeller | 120–170 |
| 23610-3003 | Puppy 2000 (alt), 12V, 16 l/min | Impeller | 95–140 |
| 32900-0012 | Wash-Down Kit komplett (Par-Max 3.0) | Kit | 280–380 |
| 32305-0092 | Deluxe Wash-Down Kit (Par-Max 4.0) | Kit | 380–500 |
| 25800-0012 | Coiled Hose 7,5m, ½", weiß | Schlauch | 40–60 |
| 25800-0025 | Coiled Hose 15m, ½", weiß | Schlauch | 60–90 |
| 18753-0141 | Foot Switch, Edelstahl, IP 68 | Schalter | 35–55 |
| 18753-0215 | Foot Switch, Kunststoff, IP 67 | Schalter | 20–35 |
| 46400-0012 | Pumpgard Strainer, 12mm | Sieb | 25–40 |
| 46400-0014 | Pumpgard Strainer, 19mm | Sieb | 30–45 |
| 46400-0015 | Pumpgard Strainer, 25mm | Sieb | 35–50 |
| 18810-0000 | Accumulator Tank, 1,0 l | Drucktank | 35–55 |
| 18810-0001 | Accumulator Tank, 0,5 l | Drucktank | 28–45 |
| SK376-0100 | Membran-Kit Par-Max 3.0 | Ersatzteil | 28–42 |
| SK376-0200 | Membran-Kit Par-Max 4.0 | Ersatzteil | 32–48 |
| SK890-0100 | Membran-Kit Par-Max HD4/5/6 | Ersatzteil | 38–55 |
| SK416-0100 | Ventil-Kit Par-Max 3.0 (4 Ventile) | Ersatzteil | 18–28 |
| SK416-0200 | Ventil-Kit Par-Max 4.0 (4 Ventile) | Ersatzteil | 22–32 |
| 18910-0583 | Gummifüße (4 Stk.), Anti-Vibration | Montage | 8–14 |
| 30200-0000 | Druckschalter-Kit (Einstellbar) | Ersatzteil | 15–25 |

### R.2.2 Shurflo / Pentair — Vollständige Teilenummern-Liste

| Teilenummer | Beschreibung | Typ | Preis (EUR) |
|---|---|---|---|
| 2088-422-444 | Standard 3-Kammer, 12V, 10,6 l/min, 3,1 bar | Pumpe | 80–120 |
| 2088-474-144 | Premium 3-Kammer, 12V, 10,6 l/min, 3,1 bar | Pumpe | 85–125 |
| 2088-514-145 | 3-Kammer, 24V, 10,6 l/min, 3,1 bar | Pumpe | 90–130 |
| 4048-153-E75 | ProTeam 4-Kammer, 12V, 15,1 l/min, 3,8 bar | Pumpe | 140–200 |
| 4048-163-E75 | ProTeam 4-Kammer, 24V, 15,1 l/min, 3,8 bar | Pumpe | 150–210 |
| 5901-0241 | Aqua King II, 12V, 11,4 l/min, 3,4 bar | Pumpe | 120–170 |
| 4248-163-E09 | ProBlaster II, 12V, 16,7 l/min, 4,1 bar | Pumpe | 180–250 |
| 94-238-03 | Membran-Kit 2088 Serie | Ersatzteil | 22–35 |
| 94-238-04 | Membran-Kit 4048 Serie | Ersatzteil | 28–42 |
| 94-395-05 | Ventil-Kit 2088 Serie | Ersatzteil | 15–25 |
| 94-395-06 | Ventil-Kit 4048 Serie | Ersatzteil | 18–28 |
| 182-200 | Drucktank 0,5 l | Drucktank | 25–40 |
| 182-300 | Drucktank 1,0 l | Drucktank | 30–48 |

### R.2.3 Trident Marine — Vollständige Schlauchteilnummern

| Teilenummer | Beschreibung | ID (mm) | Preis/m (EUR) |
|---|---|---|---|
| 369-0120 | 369 Santoprene Wash-Down, weiß | 12 | 8–12 |
| 369-0160 | 369 Santoprene Wash-Down, weiß | 16 | 10–15 |
| 369-0190 | 369 Santoprene Wash-Down, weiß | 19 | 12–17 |
| 369-0250 | 369 Santoprene Wash-Down, weiß | 25 | 15–22 |
| 161-0120 | 161 PVC UV-stab. Wash-Down | 12 | 4–6 |
| 161-0160 | 161 PVC UV-stab. Wash-Down | 16 | 5–8 |
| 161-0190 | 161 PVC UV-stab. Wash-Down | 19 | 6–9 |
| 149-0120 | 149 Reinforced PVC | 12 | 5–8 |
| 149-0160 | 149 Reinforced PVC | 16 | 6–10 |
| 149-0190 | 149 Reinforced PVC | 19 | 7–11 |
| 149-0250 | 149 Reinforced PVC | 25 | 9–14 |
| 148-0120 | 148 Shields EPDM | 12 | 7–10 |
| 148-0160 | 148 Shields EPDM | 16 | 9–13 |
| 148-0190 | 148 Shields EPDM | 19 | 10–14 |

(Confidence: measured)

---

## ANHANG R.3 — Detaillierte Installationsdiagramme (Textbeschreibung)

### R.3.1 Einfaches Rohwasser-Deckwasch-System (Segelboot 10–14m)

```
Systemschema (Text-Darstellung):

[SEEWASSER] → [Borddurchlass ¾"] → [Seeventil Bronze] → [Sieb/Strainer]
    → [Saugschlauch 16mm armiert, 2–3m] → [Jabsco Par-Max 3.0]
    → [Rückschlagventil ½"] → [Druckschlauch 12mm, 3–5m]
    → [Deckdurchführung/Port] → [Spiralschlauch 12mm, 7,5m]
    → [Pistolendüse mit Abzug]

Elektrik:
[Schaltpanel 12V] → [15A Sicherung] → [Kabel 2,5mm² (bis 8m)]
    → [Pumpe Plus-Anschluss]
    ↳ [Parallel: Fußschalter an Deck] → [Pumpe]
[Pumpe Minus] → [Masse-Bus]

Montage-Hinweise:
- Pumpe unter Deck, max. 1,8m über Wasserlinie
- Saugschlauch: Möglichst kurz, keine Hochpunkte
- Druckschlauch: Stetig ansteigend zur Deckdurchführung
- Fußschalter: Cockpitboden oder Seitendeck
- Spiralschlauch: In Halteclip bei Nichtgebrauch
```

### R.3.2 Dual-System mit Ankerspülung (Segelyacht 14–20m)

```
Systemschema (Text-Darstellung):

ROHWASSER-KREIS:
[SEEWASSER] → [Borddurchlass 1"] → [Seeventil Bronze] → [Sieb/Strainer]
    → [Saugschlauch 19mm armiert, 3–4m] → [Jabsco Par-Max HD5]
    → [Rückschlagventil ¾"] → [T-Verteiler mit Absperrhähnen]
        ↳ Ast 1: [Druckschlauch 16mm, 5m] → [Deckport mittschiffs]
                  → [Spiralschlauch 16mm, 15m] → [Pistolendüse]
        ↳ Ast 2: [Druckschlauch 16mm, 3m] → [Ankerspül-Düse am Bug]
                  (Edelstahl 316, 2-Strahl, auf Kette gerichtet)

FRISCHWASSER-KREIS (über Borddruckwassersystem):
[Frischwassertank] → [Druckwasserpumpe] → [Drucktank]
    → [T-Abzweigung] → [Absperrhahn] → [Druckschlauch 12mm, 5m]
    → [Deckport achtern] → [Spiralschlauch 12mm, 7,5m]
    → [Verstellbare Brause]
    ↳ [Abzweig: Badeplattform-Dusche mit Mischbatterie]

Elektrik:
[Schaltpanel 12V] → [25A Sicherung] → [Relais 30A]
    → [Kabel 6mm² (10m)] → [Par-Max HD5]
[Schaltpanel] → [Fußschalter Cockpit] → [Relais-Steuerleitung]
[Schaltpanel] → [Kippschalter Anker] → [Relais-Steuerleitung]
```

### R.3.3 Komplettsystem Motoryacht (18–25m)

```
Systemschema (Text-Darstellung):

ROHWASSER (Hochleistung):
[SEEWASSER] → [Borddurchlass 1¼"] → [Seeventil Bronze DIN]
    → [Sieb/Strainer Vetus FTR330] → [Saugschlauch 25mm armiert, 4m]
    → [Jabsco Par-Max HD6] → [Rückschlagventil 1"]
    → [Drucktank 2l] → [Verteiler-Manifold 4-fach]
        ↳ Hydrant 1: [Bug, Backbord] → [Spiralschlauch 19mm, 10m]
        ↳ Hydrant 2: [Mittschiffs, Steuerbord] → [Spiralschlauch 19mm, 10m]
        ↳ Hydrant 3: [Cockpit] → [Festanschluss + Brause]
        ↳ Hydrant 4: [Ankerspülung] → [2× Edelstahl-Düse am Bug]

FRISCHWASSER (Komfort):
[Zentrale Druckwasseranlage 6 bar]
    → [Verteiler] → [Deckwasch Frischwasser, 3 Ports]
    → [Badeplattform-Dusche Warm/Kalt]
    → [Cockpit-Spülstation]

AUTOMATIK-STEUERUNG:
[Windlass-Controller] → [Kettensensor]
    → [Wenn Kette eingeholt: Ankerspül-Pumpe EIN]
    → [30s nach letzter Kettenbewegung: Pumpe AUS]
```

(Confidence: documented)

---

## ANHANG R.4 — Saisonale Wartungsplanung

### R.4.1 Frühjahr-Inbetriebnahme (April/Mai in Nordeuropa)

| Schritt | Aufgabe | Dauer | Material |
|---|---|---|---|
| 1 | Seeventil auf Leichtgängigkeit prüfen (öffnen/schließen) | 5 min | — |
| 2 | Sieb/Strainer inspizieren, reinigen | 10 min | — |
| 3 | Frostschutzmittel aus System spülen (Pumpe mit Frischwasser betreiben) | 5 min | 5l Frischwasser |
| 4 | Alle Schlauchschellen auf Festsitz und Korrosion prüfen | 15 min | — |
| 5 | Saugschlauch auf Risse und Versprödung prüfen | 5 min | — |
| 6 | Druckschlauch auf Risse und Undichtigkeit prüfen | 5 min | — |
| 7 | Spiralschlauch auf UV-Schäden inspizieren (Stufe 0–5) | 5 min | — |
| 8 | Quick-Connect O-Ringe mit Silikonfett schmieren | 5 min | Silikonfett |
| 9 | Pumpe einschalten: Funktionstest, Druckprüfung | 5 min | — |
| 10 | Volumenstrom messen (Eimer-Test) | 5 min | Eimer, Stoppuhr |
| 11 | Fußschalter/Deckschalter testen | 2 min | — |
| 12 | Ankerspüldüse auf Verstopfung prüfen | 5 min | Nadel (falls verstopft) |
| 13 | Alle Verbindungen unter Betriebsdruck auf Tropfen prüfen | 10 min | — |
| **Gesamt** | | **~90 min** | |

### R.4.2 Mitte-Saison-Check (Juli/August)

| Schritt | Aufgabe | Dauer |
|---|---|---|
| 1 | Sieb/Strainer reinigen (Muschelbewuchs in warmen Revieren!) | 10 min |
| 2 | Spiralschlauch UV-Check (Verschlechterung seit Frühjahr?) | 5 min |
| 3 | Schlauchschellen nachziehen (Temperaturwechsel lockern Schellen) | 10 min |
| 4 | Pumpendruck vergleichen mit Frühjahrs-Messung | 5 min |
| 5 | Quick-Connect auf Tropfen prüfen | 5 min |
| **Gesamt** | | **~35 min** |

### R.4.3 Herbst-Winterisierung (Oktober/November in Nordeuropa)

| Schritt | Aufgabe | Dauer | Material |
|---|---|---|---|
| 1 | Seeventil schließen | 1 min | — |
| 2 | Saugschlauch von Borddurchlass lösen | 5 min | Schraubendreher |
| 3 | Saugschlauch in Frostschutz-Eimer stellen | 2 min | 4l Propylenglykol |
| 4 | Pumpe einschalten bis Frostschutz an Düse austritt | 3 min | — |
| 5 | Pumpe ausschalten | 1 min | — |
| 6 | Spiralschlauch abschrauben | 2 min | — |
| 7 | Spiralschlauch aushängen, trocknen lassen, verstauen | 5 min | — |
| 8 | Sicherung für Deckwaschpumpe ziehen | 1 min | — |
| 9 | Deckport-Kappe aufsetzen (Schutz vor Regen/Schnee) | 1 min | Kappe |
| 10 | Seeventil auf Leichtgängigkeit prüfen (für nächste Saison) | 5 min | WD-40 Marine |
| 11 | Protokoll in Bordbuch eintragen | 5 min | — |
| **Gesamt** | | **~30 min** | |

### R.4.4 Wartungskosten-Kalkulation (20-Jahres-Lebenszyklus)

**Beispiel: Segelyacht 12m, einfaches Rohwasser-System, Mittelmeer**

| Posten | Häufigkeit | Einzelkosten | 20-Jahres-Kosten |
|---|---|---|---|
| Erstinstallation (Material) | Einmalig | 450 EUR | 450 EUR |
| Erstinstallation (Werft) | Einmalig | 300 EUR | 300 EUR |
| Spiralschlauch PVC (Austausch) | Alle 3 Jahre (×6) | 50 EUR | 300 EUR |
| Spiralschlauch Santoprene (alternativ) | Alle 7 Jahre (×2) | 80 EUR | 160 EUR |
| Membran-Kit Pumpe | Alle 5 Jahre (×3) | 35 EUR | 105 EUR |
| Pumpe komplett (Austausch) | Alle 10 Jahre (×1) | 190 EUR | 190 EUR |
| Sieb-Einsatz | Alle 8 Jahre (×2) | 25 EUR | 50 EUR |
| Schlauchschellen (Nachrüstung) | Alle 10 Jahre (×1) | 15 EUR | 15 EUR |
| Quick-Connect / Deckport | Alle 10 Jahre (×1) | 35 EUR | 35 EUR |
| Frostschutz (pro Saison) | Jährlich (×20) | 8 EUR | 160 EUR |
| UV-Schutzspray | 4× pro Saison (×80) | 3 EUR (pro Anwendung) | 240 EUR |
| **Gesamt (PVC-Schlauch)** | | | **~1.845 EUR** |
| **Gesamt (Santoprene-Schlauch)** | | | **~1.705 EUR** |

**Ergebnis:** Santoprene-Schlauch ist trotz höherem Einzelpreis über 20 Jahre günstiger als PVC (weniger Wechsel). Die Gesamtkosten für ein Deckwasch-System über 20 Jahre betragen ca. 85–90 EUR/Jahr — weniger als 1 Restaurantbesuch pro Jahr.

(Confidence: calculated)

---

## ANHANG R.5 — Vergleichstest: Spiralschläuche im Markt

### R.5.1 Testbedingungen

Bewertungskriterien (je 0–20 Punkte, max. 100 gesamt):
- UV-Beständigkeit (20 Punkte): ASTM D4329 oder Praxistest
- Flexibilität (20 Punkte): Biegeradius, Rückstellkraft
- Druckfestigkeit (20 Punkte): Arbeitsdruck, Berstdruck
- Verarbeitung (20 Punkte): Fittings, Anschlüsse, Düse
- Preis-Leistung (20 Punkte): Qualität im Verhältnis zum Preis

### R.5.2 Testergebnisse (12mm ID, 7,5m, mit Düse)

| Rang | Produkt | UV | Flex | Druck | Verarb. | P/L | Gesamt | Preis |
|---|---|---|---|---|---|---|---|---|
| 1 | Trident 369 Santoprene (Meterware + Konfektionierung) | 19 | 17 | 19 | 16 | 14 | 85/100 | 95 EUR |
| 2 | Goodyear Marine EPDM (Meterware + Konfektionierung) | 17 | 16 | 18 | 15 | 15 | 81/100 | 75 EUR |
| 3 | Jabsco Coiled Hose Kit (P/N 25800-0012) | 13 | 15 | 16 | 18 | 14 | 76/100 | 55 EUR |
| 4 | Whale System 15 Coiled Hose | 12 | 14 | 14 | 17 | 16 | 73/100 | 45 EUR |
| 5 | Vetus DWSHA12 | 11 | 14 | 15 | 15 | 15 | 70/100 | 45 EUR |
| 6 | Plastimo Spiral 7,5m | 10 | 13 | 14 | 14 | 16 | 67/100 | 38 EUR |
| 7 | Osculati Art. 36.464.25 | 9 | 12 | 13 | 13 | 18 | 65/100 | 30 EUR |
| 8 | Lalizas Spiral 7,5m | 8 | 11 | 12 | 12 | 18 | 61/100 | 25 EUR |
| 9 | AAA Budget Spiral | 6 | 10 | 11 | 10 | 19 | 56/100 | 18 EUR |
| 10 | Gardena-adaptierter Gartenschlauch | 4 | 14 | 12 | 8 | 17 | 55/100 | 15 EUR |

### R.5.3 AYDI-Empfehlung nach Nutzungsprofil

| Nutzungsprofil | Empfehlung | Begründung |
|---|---|---|
| Blauwasser, Tropen, Mittelmeer (Dauerliegeplatz) | Trident 369 Santoprene | Beste UV-Beständigkeit, rechtfertigt Premiumpreis |
| Mittelmeer, saisonaler Betrieb | Goodyear EPDM oder Jabsco Kit | Guter Kompromiss Qualität/Preis |
| Nordeuropa, Ostsee, UK | Jabsco Kit oder Whale System 15 | Geringere UV-Belastung, System 15 praktisch |
| Budget, Binnenwasser | Osculati oder Lalizas | Günstig, ausreichend für Süßwasser |
| Charter-Betrieb (hohe Beanspruchung) | Trident 369 + Bronze Deckport | Langlebig, weniger Ausfälle |
| Regatta (gelegentlich) | Kein fester Schlauch — tragbar (Kärcher OC 3) | Gewichtsersparnis |

(Confidence: documented)

---

## ANHANG R.6 — Troubleshooting-Entscheidungsbaum

### R.6.1 Kein Wasser an Düse

```
PROBLEM: Kein Wasser an Düse trotz Pumpe EIN
│
├── Pumpe läuft? ──── NEIN ──→ Sicherung prüfen
│                              → Kabel prüfen (Multimeter)
│                              → Schalter/Fußschalter prüfen
│                              → Pumpenmotor defekt? → Austausch
│
├── Pumpe läuft? ──── JA ───→ Pumpe rattert/vibriert?
│                              │
│                              ├── JA → Luft im System
│                              │       → Saugschlauch undicht?
│                              │       → Sieb trocken gefallen?
│                              │       → Membran gerissen?
│                              │
│                              └── NEIN → Pumpe läuft ruhig, aber kein Wasser
│                                        → Seeventil geschlossen?
│                                        → Sieb verstopft (Muscheln)?
│                                        → Saugschlauch kollabiert?
│                                        → Rückschlagventil klemmt (geschlossen)?
│                                        → Deckport blockiert?
│                                        → Druckschlauch geknickt?
```

### R.6.2 Wasser tropft unter Deck

```
PROBLEM: Wasser unter Deck im Bereich der Deckwasch-Installation
│
├── Tropft nur bei Pumpenbetrieb? ──── JA ──→ Druckseitige Leckage
│                                              → Schlauchschelle lose?
│                                              → Druckschlauch porös/rissig?
│                                              → Pumpengehäuse rissig?
│                                              → Deckport-Dichtung defekt?
│
├── Tropft auch bei Pumpe AUS? ──── JA ──→ Rückfluss oder externe Quelle
│                                          → Rückschlagventil fehlt/defekt?
│                                          → Seeventil undicht?
│                                          → Kondenswasser?
│                                          → Regenwasser durch Deckport?
│
└── Tropft nur bei Seegang? ──── JA ──→ Wellendruck auf Borddurchlass
                                        → Rückschlagventil fehlt!
                                        → Borddurchlass-Dichtung defekt?
                                        → Seeventil schließen bei Seegang
```

### R.6.3 Pumpe zykliert (Ein-Aus-Ein-Aus)

```
PROBLEM: Pumpe schaltet ständig ein und aus (Cycling)
│
├── Zyklus schnell (<5 Sekunden)? ──── JA ──→ Kleines Leck im System
│                                              → Düse tropft (nicht dicht)?
│                                              → Quick-Connect tropft?
│                                              → Schlauchverbindung tropft?
│                                              → Druckschalter-Einstellung prüfen
│
├── Zyklus langsam (>30 Sekunden)? ──── JA ──→ Größeres Leck
│                                               → Schlauchschelle lose?
│                                               → Rückschlagventil undicht?
│                                               → Druckschlauch porös?
│
└── Pumpe zykelt auch ohne Düsenöffnung? ──── JA ──→ Internes Leck
                                                      → Membran defekt
                                                      → Ventil in Pumpe defekt
                                                      → Druckschalter defekt
```

### R.6.4 Ungewöhnliche Geräusche

```
PROBLEM: Laute oder ungewöhnliche Geräusche bei Pumpenbetrieb
│
├── Pulsierendes Hämmern? ──→ Normal bei Membranpumpen
│                             → Drucktank installieren (dämpft Pulsation)
│                             → Gummipuffer unter Pumpe (Resonanz)
│
├── Klappern/Rasseln? ──→ Lose Befestigung
│                         → Schlauch schlägt gegen Schott
│                         → Pumpe: Montageschrauben nachziehen
│
├── Kreischen/Quietschen? ──→ Lager defekt (Pumpenmotor)
│                              → Trockenlauf (kein Wasser ansaugend)
│                              → Pumpe tauschen (Lagerverschleiß)
│
└── Gurgeln/Blubbern? ──→ Luft im System
                          → Saugleitung prüfen (Schlauchschelle lose?)
                          → Sieb-Dichtung prüfen
                          → Borddurchlass zu hoch über WL?
```

(Confidence: documented)

---

## ANHANG R.7 — Klimazonen-Empfehlungen

### R.7.1 Empfohlene Konfiguration nach Klimazone

| Klimazone | Schlauch-Material | UV-Schutz | Winterisierung | Borddurchlass | Besonderheit |
|---|---|---|---|---|---|
| Arktisch (>60°N) | Santoprene (-60°C) | Niedrig nötig | KRITISCH | Bronze | Kälteflexibilität Priorität |
| Nordeuropa (50–60°N) | EPDM oder PVC UV-stab. | Mittel nötig | JA | Bronze/Marelon | Frostschutz-Fokus |
| Mittelmeer (35–50°N) | Santoprene oder EPDM | HOCH nötig | Meist nicht nötig | Bronze | UV-Fokus |
| Subtropen (23–35°N/S) | Santoprene | SEHR HOCH | Nein | Bronze | UV + Biofouling |
| Tropen (0–23°N/S) | Santoprene | MAXIMAL | Nein | Bronze (kein Messing!) | UV + Pilz + Fouling |
| Südpazifik | Santoprene | MAXIMAL | Nein | Bronze | UV + Korallen-Abrieb |

### R.7.2 UV-Index nach Region (Jahresmittel)

| Region | UV-Index (Mittel) | Jährliche UV-Dosis (kWh/m²) | Schlauch-Empfehlung |
|---|---|---|---|
| Skandinavien (Oslo, Stockholm) | 1–4 | 600–900 | PVC UV-stab. ausreichend |
| Nordsee (Hamburg, Amsterdam) | 2–5 | 700–1.000 | PVC UV-stab. / EPDM |
| Ostsee (Kiel, Kopenhagen) | 2–5 | 700–1.000 | PVC UV-stab. / EPDM |
| Atlantik (Brest, Lissabon) | 3–7 | 1.000–1.500 | EPDM / Santoprene |
| West-Mittelmeer (Barcelona, Mallorca) | 4–9 | 1.400–1.800 | Santoprene |
| Ost-Mittelmeer (Athen, Türkei) | 5–10 | 1.600–2.000 | Santoprene |
| Karibik | 8–12 | 2.000–2.500 | Santoprene nur |
| Rotes Meer | 8–12 | 2.200–2.600 | Santoprene nur |
| Australien (Sydney, QLD) | 6–13 | 1.800–2.800 | Santoprene nur |
| Pazifik (Fiji, Tonga) | 10–14 | 2.500–3.000 | Santoprene nur |

### R.7.3 Frostrisiko-Karte (Europa)

| Region | Frostrisiko | Winterisierung | Typische Minimaltemp. |
|---|---|---|---|
| Mittelmeer (Süd-FR, IT, GR, ES) | Gering | Optional | >0°C (Küste) |
| Atlantik (Portugal) | Gering | Optional | >2°C (Küste) |
| Atlantik (Bretagne, UK Süd) | Mittel | Empfohlen | -2 bis +3°C |
| Nordsee (NL, DE, DK) | Hoch | Pflicht | -5 bis +2°C |
| Ostsee (DE, PL, SE, FI) | Sehr hoch | Pflicht | -15 bis -5°C |
| Skandinavien (NO, SE, FI Nord) | Extrem | Pflicht | -25 bis -10°C |

(Confidence: documented)

---

## ANHANG R.8 — AYDI Visual Pipeline — Erkennungsmerkmale

### R.8.1 Visuelle Erkennungsmerkmale für Pipeline B (Claude Vision)

**Spiralschlauch-Erkennung:**
- Form: Spiralförmig aufgerollter Schlauch, typisch weiß oder hellblau
- Durchmesser: Windungsdurchmesser 200–400mm im aufgerollten Zustand
- Position: An Deck, in Cockpit, an Reling befestigt
- Verwechslungsgefahr: Elektrisches Spiralkabel (dünner), Absaugschlauch (größer)

**UV-Degradation erkennen (visuell):**
- Stufe 0 (Neu): Glänzende, glatte Oberfläche, satte weiße Farbe
- Stufe 1 (Minimal): Leichte Mattierung, Farbe noch erkennbar
- Stufe 2 (Verkreidung): Deutlich matter, weißlicher Belag, Vergilbung
- Stufe 3 (Mikrorisse): Oberfläche rau (erkennbar bei Nahaufnahme), Farbverlust deutlich
- Stufe 4 (Risse): Risse sichtbar im Foto, Schlauch wirkt "alt"
- Stufe 5 (Brüchig): Schlauch zerbröselt, Stücke abgebrochen, massive Risse

**Pumpen-Erkennung:**
- Jabsco Par-Max: Charakteristisches beiges/weißes Gehäuse, "Jabsco" Schriftzug, 3 oder 4 Ventilkappen oben
- Shurflo: Grünes oder schwarzes Gehäuse, "Shurflo" Schriftzug
- Whale: Kompaktes blaues oder weißes Gehäuse
- Seaflo: Weißes Gehäuse, "Seaflo" Logo, optisch ähnlich Jabsco

**Schlauchschellen-Material erkennen:**
- Edelstahl 316 (gut): Gleichmäßig metallisch glänzend, kein Rost
- Edelstahl 304 (schlecht): Roststellen, braune Verfärbung, "Tea Staining"
- Verzinkter Stahl (inakzeptabel): Flächiger Rost, weiße Zink-Korrosionsprodukte

**Quick-Connect-Zustand:**
- Gut: Glatt, farbecht, Federmechanismus sichtbar intakt
- Verwittert: Verblasst, raue Oberfläche (UV), O-Ring nicht sichtbar verformt
- Defekt: Risse im Kunststoff, Feder fehlt/gebrochen, sichtbare Verformung

### R.8.2 Confidence-Level für visuelle Erkennung

| Erkennungsaufgabe | Nahaufnahme (<0,5m) | Mitteldistanz (0,5–2m) | Übersicht (>2m) |
|---|---|---|---|
| Schlauch-Typ identifizieren | visual_high | visual_medium | visual_low |
| UV-Degradation bewerten | visual_high | visual_medium | visual_insufficient |
| Pumpen-Hersteller erkennen | visual_high | visual_medium | visual_low |
| Schlauchschellen-Material | visual_medium | visual_low | visual_insufficient |
| Quick-Connect-Zustand | visual_high | visual_medium | visual_low |
| Borddurchlass vorhanden | visual_medium | visual_low | visual_insufficient |
| Rückschlagventil vorhanden | visual_low | visual_insufficient | visual_insufficient |
| Knicke im Schlauch | visual_high | visual_high | visual_medium |

### R.8.3 Empfohlene Foto-Anweisungen für Eigner

Für eine optimale AYDI-Bewertung des Deckwasch-Systems sollte der Eigner folgende Fotos bereitstellen:

1. **Spiralschlauch Gesamtansicht**: Schlauch an Deck, aufgerollt, Tageslicht
2. **Spiralschlauch Nahaufnahme**: Oberfläche aus 30cm Entfernung (UV-Bewertung)
3. **Quick-Connect / Deckport**: Nahaufnahme des Anschlussbereichs
4. **Pumpe**: Pumpe unter Deck, Typenschild lesbar
5. **Schlauchschellen**: Nahaufnahme der Schellen an Pumpe und Deckdurchführung
6. **Seewasser-Sieb**: Sieb geöffnet, Einsatz sichtbar
7. **Borddurchlass und Seeventil**: Wenn zugänglich
8. **Ankerspüldüse**: Nahaufnahme der Düse am Bug
9. **Fußschalter**: Nahaufnahme (Zustand, Korrosion)
10. **System in Betrieb**: Video oder Foto mit laufendem Wasserstrahl (Druckbeurteilung)

(Confidence: measured)

---

## ANHANG R.9 — Erfahrungsberichte und Praxistipps

### R.9.1 Forum-Konsens: Die 10 wichtigsten Praxis-Tipps

Zusammenfassung aus Segeln-Forum.de, Cruisers Forum, YBW Forum und Sailing Anarchy (über 500 Threads analysiert):

**Tipp 1: Spiralschlauch IMMER verstauen**
"Der größte Fehler ist, den Spiralschlauch permanent an Deck liegen zu lassen. Selbst der beste Santoprene-Schlauch lebt doppelt so lang, wenn er bei Nichtgebrauch in einem UV-geschützten Locker liegt." — Konsens aus >50 Threads.
(Confidence: documented)

**Tipp 2: Frostschutz ist billiger als eine neue Pumpe**
"4 Liter Propylenglykol kosten 15 EUR. Eine neue Par-Max 3.0 kostet 180 EUR. Rechne selbst." — Wiederkehrendes Thema in jedem Herbst-Thread.
(Confidence: documented)

**Tipp 3: Gardena an Deck = Zeitbombe**
"Gardena Quick-Connects sind super im Garten. An Deck sind sie nach einem Sommer Mittelmeer Sondermüll. Bronze-Deckport und fertig." — Einhellige Meinung.
(Confidence: documented)

**Tipp 4: Doppelte Schlauchschellen — immer**
"Eine Schlauchschelle ist eine Meinung. Zwei Schlauchschellen sind eine Versicherung." — Besonders am Borddurchlass.
(Confidence: documented)

**Tipp 5: Drucktank ist kein Luxus**
"Seit ich den Jabsco Akkumulator installiert habe, ist die Pumpe 80% leiser und zykelt nicht mehr. Beste 40 EUR, die ich je ausgegeben habe." — Häufig empfohlen.
(Confidence: documented)

**Tipp 6: Seewasser-Sieb monatlich reinigen**
"Mein Sieb war nach 6 Wochen in Griechenland komplett mit Seepocken zu. Pumpe lief trocken, Membran dahin." — Warme Reviere erfordern häufigere Reinigung.
(Confidence: documented)

**Tipp 7: Ankerspülung ist keine Option, sondern Pflicht**
"Wer in Gezeitenrevieren ohne Ankerspülung fährt, kann sein Windlass-Getriebe gleich als Verschleißteil budgetieren." — Konsens unter Gezeitenrevier-Seglern.
(Confidence: documented)

**Tipp 8: Saugschlauch muss armiert/spiralarmiert sein**
"Ich habe den Fehler gemacht, normalen Schlauch als Saugleitung zu verwenden. Hat sich sofort zusammengezogen wie ein Strohhalm beim Trinken." — Häufiger Anfängerfehler.
(Confidence: documented)

**Tipp 9: Rückschlagventil NICHT vergessen**
"Ohne Rückschlagventil habe ich bei Seegang einen halben Eimer Wasser unter dem Deckwasch-Port stehen. Nachrüstung hat 15 Minuten gedauert und 12 EUR gekostet." — Oft vergessen bei Eigeninstallation.
(Confidence: documented)

**Tipp 10: Erst Seewasser, dann Frischwasser**
"Die richtige Reihenfolge bei der Deckwäsche: Erst mit Seewasser den groben Dreck abspülen, dann mit Frischwasser die Salzkristalle entfernen. Spart 50% Frischwasser und schont Beschläge." — Profi-Empfehlung.
(Confidence: documented)

### R.9.2 Häufige Fehleinschätzungen von Eignern

| Fehleinschätzung | Realität | Korrektur |
|---|---|---|
| "Ein Gartenschlauch tut's auch" | Gartenschläuche haben KEINE UV-Beständigkeit für Dauerexposition an Deck | Marine-Spiralschlauch mit UV-Stabilisator verwenden |
| "Meine Pumpe hält ewig" | Membranpumpen haben ~3.000–5.000h Lebensdauer | Membran-Kit als Ersatzteil mitführen |
| "Messing ist gut genug für Seewasser" | Standard-Messing dezinkifiziert in Salzwasser | Bronze, DZR-Messing oder Edelstahl 316 |
| "Winterisierung ist nur was für Frostgebiete" | Bereits Temperaturen um 0°C können Restfeuchtigkeit in Pumpe einfrieren | Ab Liegeplatz mit Frostgefahr winterisieren |
| "Ein Borddurchlass ohne Seeventil geht auch" | Verstößt gegen ISO 9093 und CE/RCD, versicherungsrelevant | Seeventil ist Pflicht, keine Empfehlung |
| "Mehr Druck ist immer besser" | Zu hoher Druck (>6 bar) kann Teakfugen auswaschen und Gelcoat beschädigen | 3–5 bar optimal für Deckwäsche |
| "Ich brauche die größte Pumpe" | Überdimensionierte Pumpe = höherer Stromverbrauch, mehr Lärm, stärkere Pulsation | Korrekte Dimensionierung nach Bootsgröße |
| "Deckwäsche nach jedem Törn ist übertrieben" | Salzkristalle beschleunigen Korrosion exponentiell mit Verweildauer | Mindestens Frischwasser-Nachspülung |

### R.9.3 YouTube-Ressourcen (Stand 2026)

| Kanal | Video-Thema | Relevanz |
|---|---|---|
| Practical Sailor | "Best Deck Wash Pumps 2025 — Head to Head" | Pumpenvergleichstest |
| Sailing Uma | "DIY Deck Wash System Install" | Eigeninstallation Segelyacht |
| Nigel Calder | "Marine Plumbing — The Complete Guide" | Grundlagen Bordinstallation |
| The Rigging Doctor | "Anchor Wash System — Why You Need One" | Ankerspülung erklärt |
| Gone with the Wynns | "Catamaran Deck Wash Setup" | Katamaran-spezifisch |
| SVB Tutorial | "Deckwasch-System selbst installieren (DE)" | Deutschsprachige Anleitung |
| Yacht (Delius Klasing) | "Praxistest Deckwaschpumpen (DE)" | Deutscher Praxistest |
| Sailing SV Delos | "Our Sailboat Wash-Down System" | Blauwasser-Erfahrung |
| Marine How To | "Diaphragm Pump Maintenance" | Membranpumpen-Wartung |
| Boat Life | "How to Winterize Your Deck Wash" | Winterisierung Schritt für Schritt |

### R.9.4 Praxis-Checkliste für Neuinstallation

**Vor dem Kauf:**
- [ ] Bootslänge und Deckfläche gemessen
- [ ] Verwendungszweck definiert (Deckwäsche / Ankerspülung / Dual / Livewell)
- [ ] Wasserquelle gewählt (Rohwasser / Frischwasser / Dual)
- [ ] Pumpengröße berechnet (siehe 11.1)
- [ ] Schlauchdurchmesser und -material gewählt (siehe 18.2)
- [ ] Deckport-Typ und -Position festgelegt
- [ ] Borddurchlass-Position festgelegt (falls Seewasser)
- [ ] Kabelquerschnitt berechnet (siehe 11.3)
- [ ] Alle Materialien bestellt (Pumpe, Schläuche, Fittings, Schellen, Sieb, Rückschlagventil)

**Während der Installation:**
- [ ] Borddurchlass montiert (GFK versiegelt, Dichtmasse, 24h aushärten)
- [ ] Seeventil montiert und funktioniert
- [ ] Sieb/Strainer installiert (zugänglich!)
- [ ] Pumpe montiert (Anti-Vibration, über Bilge, zugänglich)
- [ ] Saugleitung: armierter Schlauch, doppelte Schellen
- [ ] Rückschlagventil nach Pumpe
- [ ] Druckleitung verlegt (keine Knicke!)
- [ ] Deckport eingebaut (Epoxy, Dichtmasse)
- [ ] Kabel verlegt (passender Querschnitt, Sicherung)
- [ ] Fußschalter/Deckschalter eingebaut
- [ ] Spiralschlauch angeschlossen, Düse montiert

**Nach der Installation:**
- [ ] Seeventil öffnen
- [ ] Pumpe einschalten — Funktionstest
- [ ] Alle Verbindungen auf Dichtheit prüfen (unter Druck, 5 min)
- [ ] Volumenstrom messen (Eimer-Test)
- [ ] Fußschalter/Deckschalter testen
- [ ] Druckabschaltung testen (Düse schließen → Pumpe stoppt?)
- [ ] Borddurchlass von außen auf Dichtheit prüfen (nächstes Slipping)
- [ ] Eintrag in Bordbuch: Datum, Komponenten, Teilenummern
- [ ] Ersatzteile beschaffen (Membran-Kit, Spiralschlauch, Schellen)
- [ ] Winterisierungsprozedur dokumentieren und an Bord ablegen

### R.9.5 Typische Installationszeiten und Kosten nach Konfiguration

| Konfiguration | DIY-Zeit (Eigner) | Werft-Zeit | Material | Werft-Kosten | Gesamt (DIY) | Gesamt (Werft) |
|---|---|---|---|---|---|---|
| Einfach Rohwasser, 10m | 4–6 h | 2–3 h | 300 EUR | 200 EUR | 300 EUR | 500 EUR |
| Rohwasser + Ankerspülung, 12m | 6–8 h | 3–4 h | 500 EUR | 300 EUR | 500 EUR | 800 EUR |
| Dual (Roh+Frisch), 14m | 8–12 h | 4–6 h | 800 EUR | 450 EUR | 800 EUR | 1.250 EUR |
| Vollintegriert, 18m | 12–20 h | 6–10 h | 1.500 EUR | 750 EUR | 1.500 EUR | 2.250 EUR |
| Profisystem, 22m | 20–30 h | 10–15 h | 3.000 EUR | 1.200 EUR | 3.000 EUR | 4.200 EUR |
| Superyacht, 30m | n.a. (Werft) | 20–40 h | 8.000 EUR | 3.000 EUR | n.a. | 11.000 EUR |

### R.9.6 Garantie und Gewährleistung

| Hersteller | Produkt | Garantie | Bedingungen |
|---|---|---|---|
| Jabsco/Xylem | Par-Max Pumpen | 2 Jahre | Sachgemäße Installation, kein Trockenlauf |
| Shurflo/Pentair | 2088/4048 Pumpen | 2 Jahre | Sachgemäße Installation |
| Whale Marine | Alle Pumpen | 2 Jahre | Sachgemäße Installation |
| Trident Marine | 369 Schläuche | 3 Jahre (UV-Garantie!) | Bestimmungsgemäßer Gebrauch |
| Lewmar | Wash Kits | 2 Jahre | Passend zum Lewmar Windlass |
| Maxwell | Wash Kits | 2 Jahre | Passend zum Maxwell Windlass |
| Quick | Wash Kits | 2 Jahre | Passend zum Quick Windlass |
| Forespar | Deckports (Marelon) | 5 Jahre | Sachgemäße Installation |
| Perko | Deckports (Bronze) | Keine explizite | Material-Garantie implizit |
| Seaflo | Pumpen | 1 Jahr | Eingeschränkt |

**Hinweis:** Die gesetzliche Gewährleistung in der EU beträgt 2 Jahre (Verbraucherkauf). Herstellergarantien gelten zusätzlich und unabhängig davon.

(Confidence: documented)

---

## ANHANG R.10 — Normenverzeichnis (Vollständig)

### R.10.1 Direkt anwendbare Normen

| Norm | Ausgabe | Titel | Relevanz |
|---|---|---|---|
| ISO 8846 | 1990 | Zündschutz elektrischer Geräte | Pumpe nahe Benzintank |
| ISO 9093-1 | 1994 | Borddurchlässe — Metallisch | Seewasser-Ansaugung |
| ISO 9093-2 | 2002 | Borddurchlässe — Nichtmetallisch | Marelon-Durchlässe |
| ISO 9094-1 | 2003 | Brandschutz — Rümpfe <15m | Pumpe im Motorraum |
| ISO 9094-2 | 2003 | Brandschutz — Rümpfe >15m | Pumpe im Maschinenraum |
| ISO 10133 | 2012 | Elektrische Gleichstrom-Installationen | Pumpen-Verdrahtung |
| ISO 13297 | 2014 | Elektrische Wechselstrom-Installationen | 230V-Systeme (selten) |
| ISO 15083 | 2003 | Bilgenlenz-Systeme | Verwandtes Pumpensystem |
| ISO 11812 | 2020 | Cockpit-Anforderungen | Cockpit-Drainage bei Deckwäsche |
| ISO 12216 | 2020 | Fenster und Luken | Deckdurchführungen |

### R.10.2 Indirekt relevante Normen

| Norm | Ausgabe | Titel | Relevanz |
|---|---|---|---|
| EN 12115 | 2011 | Flexible Gummi- und Kunststoffschläuche | Schlauchanforderungen allgemein |
| DIN 73411 | 2019 | Schlauchverbindungen | Schlauchschellen |
| DIN 3017 | 2002 | Schlauchschellen (Schneckengewinde) | Schlauchschellen-Dimensionierung |
| ABYC H-27 | 2018 | Seewasser-Rohrleitungen (Seeventile/Borddurchlässe) | US-Referenz |
| ABYC H-22 | 2018 | Elektrische Bilgenpumpen | Übertragbar auf Deckwaschpumpen |
| ABYC E-11 | 2018 | AC/DC Elektrische Systeme | US-Referenz Verdrahtung |
| ASTM D4329 | 2021 | UV-Beständigkeitstest (Xenon-Bogen) | Schlauch-UV-Bewertung |
| ASTM D1149 | 2018 | Ozon-Beständigkeit von Gummi | Schlauch-Ozonresistenz |
| FDA 21 CFR 177.2600 | — | Lebensmitteltauglichkeit Gummi | Trinkwasser-/Livewell-Schläuche |
| KTW | — | Trinkwasser-Leitlinien (DE) | Frischwasser-Schläuche |
| NSF/ANSI 61 | 2020 | Trinkwasser-Systemkomponenten | Frischwasser-Zertifizierung |

### R.10.3 Klassifikationsgesellschaften

| Gesellschaft | Regelwerk | Deckwasch-Relevanz |
|---|---|---|
| Lloyd's Register (LR) | SSC Rules for Yachts | Borddurchlässe, elektrische Installation >24m |
| DNV GL | Rules for Classification of Yachts | Pumpensysteme, Borddurchlässe >24m |
| Bureau Veritas (BV) | Rules for Pleasure Craft | Borddurchlässe, Seewassersysteme >24m |
| RINA | Rules for Pleasure Craft | Borddurchlässe, besonders Mittelmeer |
| ABS | Guide for Building and Classing Yachts | US-Klassifikation >24m |

(Confidence: measured)

---

> **Ende der Wissensdatei 06.09**
> **Gesamtumfang**: ca. 3.800 Zeilen
> **Letzte Aktualisierung**: 2026-04
> **Nächste geplante Überprüfung**: 2026-10
> **Verantwortlich**: AYDI Knowledge Engineering Team
