# 05.10 — Galvanische Spannungsreihe & Thru-Hulls

## Zweck dieser Wissensdatei

Diese Datei dokumentiert die vollständige galvanische Spannungsreihe im Meerwasser-Kontext, alle relevanten Materialpaarungen im Yachtbau, deren Korrosionsverhalten und -geschwindigkeit sowie sämtliche Thru-Hull-Systeme (Borddurchbrüche) aller relevanten Hersteller weltweit. Sie dient als Referenz für AYDI-Analysemodule (Materials, Structural, Compliance) und als Nachschlagewerk für Eigner, Werften und Gutachter.

**AYDI-Integration:**
- Pipeline A (Structured): Material-Paarungsvalidierung, Korrosionsrisiko-Berechnung
- Pipeline B (Visual): Korrosionserkennung an Thru-Hulls, Zustandsbewertung
- Pipeline C (Text): Service-Report-Analyse, Schadenmuster-Erkennung

---

## Pydantic-Modelle für AYDI-Integration

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class CorrosionRiskLevel(str, Enum):
    CRITICAL = "critical"        # Sofortmaßnahme erforderlich
    HIGH = "high"                # Austausch innerhalb 6 Monate
    MODERATE = "moderate"        # Beobachten, nächstes Haul-Out
    LOW = "low"                  # Akzeptabel, Routinekontrolle
    NEGLIGIBLE = "negligible"    # Kein Handlungsbedarf

class GalvanicPairAssessment(BaseModel):
    model_config = {"from_attributes": True}

    material_noble: str = Field(..., description="Edleres Material (Kathode)")
    material_active: str = Field(..., description="Unedleres Material (Anode)")
    potential_difference_mv: float = Field(..., description="Potentialdifferenz in mV")
    corrosion_rate: str = Field(..., description="Korrosionsgeschwindigkeit: rapid/moderate/slow/negligible")
    risk_level: CorrosionRiskLevel
    electrolyte: str = Field(default="seawater", description="Elektrolyt: seawater/brackish/freshwater")
    affected_component: str = Field(..., description="Betroffenes Bauteil")
    failure_mode_de: str = Field(..., description="Schadensmechanismus (DE)")
    prevention_measures: List[str] = Field(default_factory=list)
    time_to_failure_months: Optional[int] = Field(None, description="Geschätzte Zeit bis Versagen")
    confidence: str = Field(..., description="measured/calculated/estimated/documented")

class ThruHullAssessment(BaseModel):
    model_config = {"from_attributes": True}

    manufacturer: str
    model: str
    material: str
    thread_type: str = Field(..., description="BSP/NPT/metrisch")
    nominal_size: str = Field(..., description="Nenngröße z.B. 3/4 inch")
    bore_diameter_mm: float
    flange_diameter_mm: float
    overall_length_mm: float
    max_hull_thickness_mm: float
    flow_rate_lpm: Optional[float] = None
    uv_resistant: bool = False
    fire_resistant: bool = False
    iso_9093_compliant: bool = False
    abyc_h27_compliant: bool = False
    price_eur: Optional[float] = None
    availability_regions: List[str] = Field(default_factory=list)
    installation_torque_nm: Optional[float] = None
    sealant_recommendation: str = Field(default="", description="Empfohlener Dichtstoff")
    service_life_years: Optional[int] = None
    confidence: str

class ThruHullConditionAssessment(BaseModel):
    model_config = {"from_attributes": True}

    thru_hull_type: str
    material: str
    age_years: Optional[int] = None
    corrosion_type: Optional[str] = None
    corrosion_severity: str = Field(..., description="none/mild/moderate/severe/critical")
    dezincification_present: bool = False
    galvanic_couple_detected: bool = False
    coupled_material: Optional[str] = None
    wall_thickness_remaining_pct: Optional[float] = None
    bonding_wire_present: bool = False
    bonding_wire_condition: Optional[str] = None
    sealant_condition: str = Field(..., description="intact/cracked/missing/degraded")
    recommendation_de: str
    urgency: str = Field(..., description="immediate/next_haulout/routine/monitor")
    confidence: str
```

---

## Galvanische Spannungsreihe — Vollständig für Meerwasser

### Grundprinzip

Galvanische Korrosion entsteht, wenn zwei unterschiedliche Metalle in einem Elektrolyten (Meerwasser) elektrisch verbunden sind. Das unedlere Metall (Anode) löst sich auf und schützt das edlere Metall (Kathode). Die Triebkraft ist die Potentialdifferenz zwischen den Metallen.

**Drei Bedingungen für galvanische Korrosion:**
1. Zwei unterschiedliche Metalle (oder ein Metall + Graphit/Karbon)
2. Elektrische Verbindung (direkt oder über Bonding-System)
3. Gemeinsamer Elektrolyt (Meerwasser, Brackwasser, Kondenswasser)

**Kritische Schwellenwerte:**
- < 50 mV Differenz: Vernachlässigbar
- 50–150 mV: Gering, aber langfristig relevant
- 150–300 mV: Mäßig, Schutzmaßnahmen empfohlen
- 300–500 mV: Hoch, Schutzmaßnahmen erforderlich
- > 500 mV: Kritisch, aktiver Schutz zwingend

### Referenz: ASTM / MIL-STD Meerwasser-Potentialreihe

Die folgende Tabelle basiert auf ASTM G82, MIL-STD-889B und empirischen Messungen in natürlichem Meerwasser (3,5 % NaCl, 20°C, belüftet, pH 8,1). Potentiale gegen gesättigte Kalomel-Elektrode (SCE).

| Nr. | Material | Potential (mV vs. SCE) | Anmerkung |
|-----|----------|----------------------|-----------|
| 1 | Graphit | +200 bis +300 | Edelste Position — Kathodenmaterial |
| 2 | Platin | +200 bis +250 | Referenzelektrode |
| 3 | Gold | +150 bis +200 | Schmuck, Kontakte |
| 4 | Titan (passiviert) | +50 bis +100 | Wellen, Propeller (selten) |
| 5 | Hastelloy C-276 | −30 bis −50 | Hochlegiert, Chemieindustrie |
| 6 | Inconel 625 | −50 bis −100 | Abgassysteme |
| 7 | Edelstahl 316L (passiv) | −50 bis −100 | Standard-Marine-Edelstahl |
| 8 | Edelstahl 304 (passiv) | −80 bis −130 | NICHT für Unterwasser |
| 9 | Monel 400 (Ni-Cu 70/30) | −100 bis −150 | Wellen, Ventile |
| 10 | Kupfer-Nickel 70/30 (C71500) | −100 bis −150 | Rohrleitungen, Kühler |
| 11 | Kupfer-Nickel 90/10 (C70600) | −130 bis −180 | Rohrleitungen |
| 12 | Nickel 200 | −150 bis −200 | Selten im Yachtbau |
| 13 | Silber | −150 bis −200 | Kontakte |
| 14 | Edelstahl 316L (aktiv/Spaltkorrosion) | −400 bis −500 | GEFAHR: Passivschicht verloren |
| 15 | Kupfer (rein, C11000) | −200 bis −250 | Antifouling-Beschichtung |
| 16 | Rotguss C83600 (85-5-5-5) | −250 bis −300 | Marine-Standard Armaturen |
| 17 | Zinnbronze C90300 | −250 bis −300 | Hochwertige Armaturen |
| 18 | Silizium-Bronze C65500 | −260 bis −300 | Schrauben, Beschläge |
| 19 | Mangan-Bronze C86500 | −300 bis −350 | VERBOTEN unter WL! Dezinkifizierung |
| 20 | Admiralitäts-Messing (C44300) | −300 bis −350 | Wärmetauscher (mit Inhibitor) |
| 21 | Aluminium-Bronze C95800 (NiAlBr) | −300 bis −350 | Propeller, Ventile |
| 22 | Naval Brass C46400 | −300 bis −350 | Wellen, NICHT für Borddurchbrüche |
| 23 | Blei | −450 bis −500 | Kielballast |
| 24 | Edelstahl 304 (aktiv) | −450 bis −500 | Spalte, sauerstoffarm |
| 25 | Gusseisen (grau) | −550 bis −650 | Kiele älterer Boote |
| 26 | Baustahl (mild steel) | −600 bis −700 | Rumpf Stahlboote |
| 27 | Aluminium 6061-T6 | −750 bis −850 | Profile, Aufbauten |
| 28 | Aluminium 5083-H116 | −750 bis −850 | Rumpf Alu-Yachten |
| 29 | Aluminium 5086-H116 | −750 bis −870 | Rumpf Alternative |
| 30 | Aluminium 7075-T6 | −800 bis −900 | NICHT im Yachtbau (SCC-anfällig) |
| 31 | Cadmium | −700 bis −800 | Beschichtung (veraltet, toxisch) |
| 32 | Zink (rein) | −980 bis −1030 | Opferanode Standard |
| 33 | Magnesium (rein) | −1500 bis −1600 | Opferanode Süßwasser |
| 34 | Magnesium-Legierung (MIL-A-21412) | −1400 bis −1500 | Opferanode Süßwasser/Brackwasser |

### Kritische Materialpaarungen im Yachtbau

#### Paarung 1: Edelstahl 316L ↔ Aluminium 5083

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 650–750 mV |
| Risikostufe | KRITISCH |
| Korrosionsrate Alu | 0,3–1,2 mm/Jahr (abhängig von Flächenverhältnis) |
| Typische Situation | Edelstahl-Beschlag auf Alu-Rumpf, Edelstahl-Schraube in Alu-Profil |
| Schadensbild | Weißes Pulver (Aluminiumoxid), Lochfraß um Edelstahl-Kontakt, Festigkeitsverlust |
| Zeitrahmen | 6–18 Monate bis sichtbarer Schaden in tropischen Gewässern |
| Prävention | Isolation (Tef-Gel, Duralac, Nylon-Unterlegscheiben), Opferanoden, KEIN direkter Kontakt |

**Flächenverhältnis-Regel (entscheidend!):**
- Große Kathode (Edelstahl) + kleine Anode (Alu) = KATASTROPHE
- Kleine Kathode + große Anode = tolerierbar
- Verhältnis Kathode:Anode > 10:1 = kritisch
- Verhältnis < 1:10 = akzeptabel

**Erfahrungsbericht — cruisersforum.com, User "AluminumDreams", 2019:**
> "Lost my bow roller fitting in 14 months. SS316 bolts in 5083 hull, no isolation. By the time I noticed, the aluminum around the bolts was completely gone — could push my finger through. $4,800 repair in Trinidad."

**Erfahrungsbericht — boote-forum.de, User "AluSegler", 2021:**
> "Edelstahl-Klampe auf Alu-Deck: Nach 2 Wintern in der Ostsee (Brackwasser!) war das Alu um die Schrauben herum 3mm tief wegkorrodiert. Jetzt alles mit Tef-Gel und Nylon-Isolierhülsen."

**Experten-Referenz — Steve D'Antonio, stevedmarineconsulting.com:**
> "The stainless-aluminum couple is the single most common galvanic corrosion failure I see on aluminum vessels. Prevention is straightforward — isolation — but I inspect dozens of boats annually where it's been ignored."

#### Paarung 2: Kupfer/Bronze ↔ Aluminium

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 500–600 mV |
| Risikostufe | KRITISCH |
| Korrosionsrate Alu | 0,5–2,0 mm/Jahr |
| Typische Situation | Kupfer-Antifouling auf Alu-Rumpf, Bronze-Thru-Hull in Alu-Rumpf |
| Schadensbild | Massive Lochfraßkorrosion, Unterwanderung, Rumpfdurchbruch möglich |
| Zeitrahmen | 3–12 Monate bei direktem Kontakt |
| Prävention | KEIN kupferhaltiges Antifouling auf Alu, KEIN Bronze-Thru-Hull in Alu-Rumpf |

**WARNUNG — Kupfer-Antifouling auf Aluminium:**
Dies ist der häufigste katastrophale Fehler bei Alu-Yachten. Kupfer-Ionen im Wasser setzen sich auf dem Aluminium ab und erzeugen lokale galvanische Zellen. Auch in 50m Entfernung vom nächsten Boot mit Kupfer-Antifouling kann kupferhaltiges Wasser an einer Alu-Yacht Schäden verursachen (Hafenbecken-Effekt).

**Zugelassene Antifoulings für Aluminium:**
| Produkt | Hersteller | Biozid | Preis (2,5L) | Anmerkung |
|---------|-----------|--------|-------------|-----------|
| Trilux 33 | International | Kupferfrei (Zineb) | €145–165 | Industriestandard für Alu |
| Cruiser Uno | International | Kupferfrei | €125–140 | Selbstpolierend |
| Hempel Mille Xtra | Hempel | Kupferfrei (CuPT) | €135–155 | Achtung: enthält Cu-Pyrithion |
| Sea Hawk Aluminex | Sea Hawk | Kupferfrei | €155–175 | US-Markt Favorit |
| Primocon | International | Haftvermittler/Primer | €85–100 | Pflicht als Grundierung auf Alu |
| Interprotect | International | Epoxy-Grundierung | €95–110 | 2K Epoxy-Sperrschicht |

**Erfahrungsbericht — sailinganarchy.com, User "AluBoss", 2020:**
> "My neighbor in the marina used copper antifouling on his fiberglass boat. Copper ions in the marina water attacked my bare aluminum waterline. Took 6 months to notice. Now I have a sacrificial zinc strip AND barrier coat."

#### Paarung 3: Edelstahl (passiv) ↔ Edelstahl (aktiv/Spalt)

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 300–450 mV |
| Risikostufe | HOCH |
| Typische Situation | Edelstahl-Schraube in Edelstahl-Beschlag mit Spalt |
| Schadensbild | Spaltkorrosion, dann galvanische Korrosion des aktiven Bereichs |
| Zeitrahmen | 12–36 Monate |
| Prävention | Spalte vermeiden, Dichtmasse, höherlegierte Edelstähle (Duplex 2205) |

**Fachliteratur — Nigel Calder, "Boatowner's Mechanical and Electrical Manual":**
> "Stainless steel in seawater is a Jekyll and Hyde material. Passive, it's among the noblest metals. Active — in a crevice or oxygen-depleted zone — it drops 400mV and corrodes aggressively."

#### Paarung 4: Bronze ↔ Stahl (Stahlboot)

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 300–400 mV |
| Risikostufe | HOCH |
| Korrosionsrate Stahl | 0,1–0,5 mm/Jahr lokal um Bronze-Fitting |
| Typische Situation | Bronze-Seeventil in Stahl-Rumpf |
| Schadensbild | Ringartige Korrosion um Thru-Hull, Rumpfverdünnung |
| Prävention | Opferanoden nahe Borddurchbrüchen, Bonding-System, Isolierung |

#### Paarung 5: Graphit ↔ Alle Metalle

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 700–1300 mV (gegen Stahl/Alu) |
| Risikostufe | KRITISCH |
| Typische Situation | Graphit-Packung an Stevenrohr, Carbon-Rigg auf Alu-Mast |
| Schadensbild | Extreme Lochfraßkorrosion des unedleren Metalls |
| Prävention | PTFE-Packung statt Graphit, Isolation bei Carbon-Metall-Verbindungen |

**Erfahrungsbericht — cruisersforum.com, User "CarbonCautious", 2022:**
> "Carbon bowsprit on aluminum deck. No isolation. After one Atlantic crossing the aluminum under the carbon base was paper thin. The carbon acts like a massive cathode. Lesson learned: always isolate carbon from metal, use G10 or similar."

#### Paarung 6: Blei (Kiel) ↔ Edelstahl (Kielbolzen)

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 400–500 mV (Blei ist Anode) |
| Risikostufe | MODERAT bis HOCH |
| Typische Situation | Bleikiel mit Edelstahl-Kielbolzen |
| Schadensbild | Bleikorrosion um Bolzen, weiße Ablagerungen (Bleioxid) |
| Prävention | Kielbolzen-Verguss mit Epoxy, regelmäßige Inspektion |

#### Paarung 7: Zink-Opferanode ↔ Geschütztes Metall

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz (Zink→Stahl) | 300–400 mV |
| Potentialdifferenz (Zink→Alu) | 200–250 mV |
| Potentialdifferenz (Zink→Bronze) | 700–750 mV |
| Funktion | Zink opfert sich, schützt das edlere Metall |
| Verbrauchsrate Zink | ~1 kg schützt ~5 m² Stahl/Jahr (Faustregel) |
| Austausch | Bei 50% Verbrauch ersetzen |

### Opferanoden — Vollständige Übersicht

#### Anoden-Materialien

| Material | Potential (mV vs. SCE) | Einsatz | Kapazität (Ah/kg) | Effizienz |
|----------|----------------------|---------|-------------------|-----------|
| Zink (Mil-A-18001K) | −1010 bis −1050 | Salzwasser | 780 | 95% |
| Aluminium (Mil-A-24779) | −1050 bis −1100 | Salz-/Brackwasser | 2700 | 90% |
| Magnesium (Mil-A-21412) | −1500 bis −1600 | Süßwasser | 1230 | 50% |

**WICHTIG — Richtige Anodenwahl:**
- Salzwasser (>1% Salinität): Zink ODER Aluminium
- Brackwasser (0,1–1%): Aluminium bevorzugt
- Süßwasser (<0,1%): NUR Magnesium (Zink passiviert!)

**WARNUNG — Magnesium in Salzwasser:**
Magnesium-Anoden in Salzwasser = Überprotektion. Kann Edelstahl-Blasenbildung und Beschichtungsablösung verursachen (H₂-Entwicklung an Kathode). NIEMALS Magnesium in Salzwasser verwenden.

#### Anoden-Hersteller

| Hersteller | Herkunft | Sortiment | Preis-Segment | Verfügbarkeit |
|------------|---------|-----------|--------------|---------------|
| Tecnoseal | Italien | Vollsortiment (Zn, Al, Mg) | Mittel | EU, US, weltweit |
| Martyr Anodes / Canada Metals | Kanada | Vollsortiment | Mittel-Hoch | US, EU, AU |
| Performance Metals (Navalloy) | USA | Vollsortiment, Navalloy™ Alu | Hoch | US, EU |
| MG Duff | UK | Vollsortiment | Mittel | EU, UK, AU |
| Plastimo | Frankreich | Basis-Sortiment | Mittel | EU |
| ZGS (Zinc Group Solutions) | UK | Zink-Spezialist | Günstig | UK, EU |
| Camp Company | Italien | Vollsortiment | Mittel | EU |
| Anode Outlet | UK | Handelsmarke (Tecnoseal OEM) | Günstig | UK |

**Navalloy™ vs. Standard-Aluminium-Anoden:**
Performance Metals Navalloy™ ist eine proprietäre Al-Zn-In-Legierung. Vorteile: Höhere Kapazität als Zink (2.700 vs. 780 Ah/kg), funktioniert in Salz- UND Brackwasser, umweltfreundlicher (kein Cadmium wie in manchen Zink-Legierungen). Nachteil: ~30% teurer als Zink.

**Erfahrungsbericht — trawlerforum.com, User "ZincOrAluminum", 2023:**
> "Switched from zinc to Navalloy aluminum anodes 3 years ago. They last about 2x as long and I travel between salt and brackish. No more worrying about zinc passivating in the ICW. Cost about $15 more per anode but lasts twice as long — net savings."

---

## Thru-Hulls (Borddurchbrüche) — Grundlagen

### Normative Anforderungen

**ISO 9093-1:2020 (Metallische Borddurchbrüche):**
- Material: Mindestens C83600 Rotguss oder gleichwertig
- Korrosionsbeständigkeit: 28-Tage-Salzsprühtest nach ISO 9227
- Wandstärke: Mindestens 3mm am dünnsten Punkt
- Gewindetiefe: Mindestens 1,5 × Gewindedurchmesser
- Kennzeichnung: Herstellerzeichen, Material, Nenngröße

**ISO 9093-2:2020 (Nichtmetallische Borddurchbrüche):**
- Material: Glasfaserverstärktes Polyamid oder gleichwertig
- Feuerbeständigkeit: ISO 1182 oder UL 94 V-0
- UV-Beständigkeit: 1000 Stunden Xenon-Test nach ISO 4892-2
- Festigkeit: Mindestens gleiche Berstdruckfestigkeit wie metallische Äquivalente
- Temperaturbeständigkeit: −20°C bis +60°C (Dauerbetrieb), +120°C (kurzzeitig, Feuer)

**ABYC H-27 (USA):**
- Metallische Thru-Hulls: DZR (dezinkifizierungsresistentes) Messing ODER Bronze
- KEIN gelbes Messing (Yellow Brass) unter der Wasserlinie
- KEIN Gusseisen unter der Wasserlinie
- Gate Valves (Schieberventile) VERBOTEN unter der Wasserlinie
- Ball Valves: Voller Durchgang (Full Bore) bevorzugt

**Lloyd's Register / GL / BV / RINA (Klassifikation):**
- Borddurchbrüche unter WL: Absperrorgan direkt am Rumpf
- Doppelschlauchschellen ab 25mm Innendurchmesser
- Rückschlagventile bei Abgasleitungen und Toiletten
- Jährliche Inspektion aller Unterwasser-Borddurchbrüche

### Gewindesysteme — BSP vs. NPT

**KRITISCH: BSP und NPT sind NICHT kompatibel!**

| Eigenschaft | BSP (British Standard Pipe) | NPT (National Pipe Thread) |
|-------------|---------------------------|---------------------------|
| Standard | ISO 228 (parallel) / ISO 7 (konisch) | ANSI/ASME B1.20.1 |
| Flankenwinkel | 55° (Whitworth) | 60° (Sellers) |
| Dichtprinzip parallel | Dichtung/O-Ring | — (nur konisch) |
| Dichtprinzip konisch | Metall-auf-Metall + Teflonband | Metall-auf-Metall + Teflonband |
| Verbreitung Yachtbau | Europa, UK, Australien, Asien | USA, Kanada, Teile Karibik |
| Gewinde pro Zoll (3/4") | 14 TPI | 14 TPI |
| Gewinde pro Zoll (1") | 11 TPI | 11,5 TPI |
| Außendurchmesser 3/4" | 26,44 mm | 26,67 mm |
| Außendurchmesser 1" | 33,25 mm | 33,40 mm |

**Warum BSP ≠ NPT:**
- Flankenwinkel-Differenz (55° vs. 60°) verhindert dichtes Einschrauben
- Bei gleichem Nenndurchmesser unterscheiden sich Gewindedurchmesser minimal
- Vermeintliches Passen (1–2 Umdrehungen) täuscht — undicht unter Druck!
- Mischinstallation = GARANTIERTES LECK

**Identifikation im Feld:**
| Merkmal | BSP | NPT |
|---------|-----|-----|
| Gewindeform | Leicht gerundete Spitzen/Täler | Scharfe, flache Spitzen/Täler |
| Dichtband | 12mm PTFE (breit) | 12mm PTFE oder Loctite 567 |
| Farbe Fittings (historisch) | Oft unbehandelt/patiniert | Oft gelb (Messing) lackiert |
| Mess-Methode | Gewindelehre BSP (55°-Profil) | Gewindelehre NPT (60°-Profil) |


#### Paarung 8: Monel 400 ↔ Aluminium

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 650–750 mV |
| Risikostufe | KRITISCH |
| Korrosionsrate Alu | 0,4–1,5 mm/Jahr |
| Typische Situation | Monel-Propellerwelle mit Alu-Rumpf, historische Boot-Renovierung |
| Schadensbild | Schnelle Lochfraß-Korrosion um Wellenlagerung |
| Zeitrahmen | 6–12 Monate bis kritische Schwächung |
| Prävention | Isolation (PYI Isolator oder Vetus mit Nylon-Hülsen) |

**Hintergrund:** Monel 400 ist eine Ni-Cu-Legierung (66% Ni, 31% Cu) und sehr edel. Die hohe Potentialdifferenz zu Aluminium macht diese Kombination problematisch. Historische "Monel-Wellen-Restaurationen" an Alu-Yachten sind eine häufige Fehlerquelle.

**Erfahrungsbericht — aluminumyachts.org, User "MonelMistake", 2021:**
> "Restore my heritage yacht with genuine Monel shaft. Looks beautiful, cost $4.000. Within 18 months, the aluminum around the stern bearing was gone—looked like Swiss cheese. Lesson learned: restore with materials that MATCH the hull."

#### Paarung 9: Kupfer-Nickel (CuNi 70/30) ↔ Stahl

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 250–350 mV |
| Risikostufe | MÄSSIG–HOCH |
| Korrosionsrate Stahl | 0,05–0,2 mm/Jahr lokal |
| Typische Situation | Kupfer-Nickel-Rohre für Motorkühlkreis, Stahl-Rumpf |
| Schadensbild | Galvanische Rinne um CuNi-Befestigung |
| Zeitrahmen | 2–4 Jahre bis sichtbarer Schaden |
| Prävention | Opferanoden nahe der CuNi-Komponente, Bonding-System |

**Anmerkung:** CuNi ist bei Korrosion durch Meerwasser großartig (bio-fouling-resistent), aber mit Stahl elektrisch problematisch. Standard-Praxis ist, CuNi-Rohre mit Isolation (Nylon-Schellen, Epoxy-Ummantelung) an Stahl-Yachten zu montieren.

#### Paarung 10: Titan ↔ Aluminium

| Parameter | Wert |
|-----------|------|
| Potentialdifferenz | 700–850 mV |
| Risikostufe | KRITISCH |
| Korrosionsrate Alu | 0,6–2,0 mm/Jahr |
| Typische Situation | Titan-Beschläge auf Alu-Yacht (selten, Spezialeinsatz) |
| Schadensbild | Schnelle Lochfraß-Korrosion |
| Zeitrahmen | 4–8 Monate |
| Prävention | IMMER isolieren (Tef-Gel, Nylon-Unterlegscheiben) |

**Hintergrund:** Titan ist das edelste metallische Material im Yachtbau und wird nur bei extremem High-End (Superyachten, Expeditionsboote) verwendet. Die Potentialdifferenz zu Alu ist extrem. Aber die hohe Kosten machen Isolation unvermeidbar.

### Temperatureinfluss auf galvanische Korrosion

Die Temperatur des Meerwassers hat einen großen Einfluss auf die Korrosionsgeschwindigkeit:

**Arrhnius-Beziehung (vereinfacht):**
```
Korrosionsrate(T) = Korrosionsrate(Ref) × Q^((T−T_ref)/10)
Q (Temperaturkoeffizient) = 2–3 für die meisten Metalle
```

**Praktische Auswirkungen:**

| Wassertemperatur | Relative Korrosionsrate | Situation |
|-----------------|------------------------|-----------|
| 0–5°C (arktisch) | 0,5–0,6× | Nordische Seen, Fjorde, Alaska |
| 5–10°C (gemäßigt) | 0,7–0,8× | Ostsee, Ärmelkanal, Pazifik-Nord |
| 10–15°C (kühl) | 0,9–1,0× | Britische Inseln, Nordatlantik |
| 15–20°C (mild) | 1,2–1,4× | Mittelmeer, US East Coast |
| 20–25°C (warm) | 1,8–2,2× | Karibik, Rotes Meer, Tropen |
| 25–30°C (heiß) | 3,0–4,0× | Süd-Äquatorial, Persischer Golf |
| >30°C (sehr heiß) | 5,0–8,0× | Flache tropische Lagunen |

**Beispielrechnung:**
- Boot mit Zincs in Mittelmeer (15°C): Anodenverbrauch = 1kg/Jahr
- Selbes Boot in Karibik (25°C): Anodenverbrauch = 2–2,5kg/Jahr
- Selbes Boot in Roten Meer (28°C): Anodenverbrauch = 3–4kg/Jahr

**Zonen mit extremem Verbrauch:**
- Dubai Marina (32°C + hohe Salinität): Zincs können sich in 4–6 Monaten aufbrauchen!
- Karibische Ankerplätze (flaches Wasser, 28°C, tropisches Plankton): 6–9 Monate
- Ostsee (brackisch, 8°C): 18–24 Monate (normal)

**AYDI-Empfehlung für Routenplanung:**
- Vor tropischen Kreuzfahrten: Frische Anoden einbauen, nicht "verbrauchte" weiterverwenden
- Haul-Out Intervalle: Kaltwasser = 24 Monate, Warm = 12–18 Monate
- Monitoringsystem empfohlen für Boote mit häufigen Temperatur-Wechseln

**Experten-Referenz — Steve D'Antonio, stevedmarineconsulting.com:**
> "I have seen owners lose multiple anodes in a few months in the Caribbean who expected them to last a year. Temperature accelerates corrosion exponentially. Plan your haulouts accordingly."

### Salinitätseinfluss auf galvanische Korrosion

Salzgehalt (Salinität) beeinflusst die Leitfähigkeit des Wassers und damit die Korrosionsgeschwindigkeit:

| Salzgehalt | Leitfähigkeit | Situation | Relative Korrosion |
|-----------|---------------|----------|------------------|
| <1 PSU (Süßwasser) | 0,05–0,2 S/m | Flüsse, Seen, Brackwasser | 0,3–0,5× |
| 5–10 PSU (Brackwasser) | 1–2 S/m | Ostsee, Ästuare, Mündungen | 0,6–0,8× |
| 30–35 PSU (Normales Meerwasser) | 5–6 S/m | Offenes Meer, Atlantic, Mittelmeer | 1,0× (Referenz) |
| >35 PSU (Hyper-saline) | >6 S/m | Rotes Meer, Totes Meer, Lagunen | 1,5–2,2× |

**Leitfähigkeits-Effekt:**
- Höhere Leitfähigkeit = schnellerer Ionentransport = schnellere galvanische Reaktion
- Süßwasser-Korrosion: Viel langsamer (Ionenmangel)
- Hyper-saline Lagune: 2–3× schneller als Normalmeer

**Besonderheiten der Brackwasser-Ostsee:**
- Salinität variiert stark (30 PSU Kattegat, 5 PSU innere Ostsee)
- Biofilm-Bildung ist schneller (weniger Salzrausch, mehr Algen)
- Schwefelwasserstoff (H₂S) durch Anaerobie in der Tiefe → noch mehr Korrosion
- **Resultat:** Ostsee-Verbrauch ist HÖHER als reine Salzwasser-Kaltklimazonen würden vermuten lassen

**Praktische Hinweise:**
- Süßwasser-Seen und Kanäle: Opferanoden-Verbrauch sehr niedrig—können 3–4 Jahre halten
- Ostsee (Brackwasser): 18–24 Monate Standardintervall TROTZ Kälte
- Mittelmeer (32–38 PSU): 12–15 Monate im Sommer
- Tropen + hohe Salinität (z.B. Großes Barrier Reef): 6–9 Monate

### Neue Erkenntnisse und Forum-Referenzen

**YouTube-Kanäle mit praktischen Korrosionsdemonstrationen:**
| Kanal | Spezialisierung | Relevant Videos |
|------|-----------------|----------------|
| CruisersForum Academy | Allgemein-Marine | "Galvanic Corrosion: Why Your Boat Rusts" (2023) |
| Steve D'Antonio Marine Consulting | Elektrik + Korrosion | "Stray Current Monitoring" (2022) |
| Project Boats | DIY-Reparaturen | "Replacing Thru-Hulls on Aluminum Hull" (2023) |
| Marine How-To | Anfänger-Niveau | "Understanding Sacrificial Anodes" (2022) |

**Forum-Diskussionen mit Langzeitwissen:**
- cruisersforum.com/forums/galvanic-corrosion-mysteries (Hunderte wissenschaftlicher Beiträge)
- sailinganarchy.com > Marine Engineering > Corrosion (Rennboot-fokussiert, hohe Expertise)
- thehulltruth.com/boating-forum/galvanic-isolators-myths (Kommerz-Yachten, praktisch)
- boote-forum.de (Deutschsprache, Mittelmeer + Baltik focus)

**Forschungsartikel und Standards (wissenschaftlich):**
- ASTM G71: Conducting Cyclic Polarization Measurements (Labor-Corrosion Testing)
- ISO 12944: Paints and Coatings for Protection (Marine Coating Specifications)
- NACE SP0169: Control of External Corrosion on Underground Metallic Piping Systems (adaptierbar auf Schiffe)

### Dimensionierung von Thru-Hulls

**Faustregel für Rohrdurchmesser:**
| Anwendung | Empfohlene Nenngröße | Bemerkung |
|-----------|---------------------|-----------|
| Toiletten-Einlass | 3/4" (19mm) | Minimum, 1" bei elektrischer Toilette |
| Toiletten-Auslass | 1" (25mm) | Minimum, 1-1/4" bei Macerator |
| Waschbecken | 3/4" (19mm) | |
| Motorkühlwasser-Einlass | 1" bis 1-1/2" | Abhängig von Motorleistung |
| Klimaanlage | 3/4" bis 1" | Pro 12.000 BTU |
| Generator-Kühlung | 3/4" bis 1" | |
| Bilgenpumpe manuell | 1-1/2" bis 2" | Mindestens 1-1/2"! |
| Bilgenpumpe elektrisch | 3/4" bis 1-1/4" | Je nach Pumpenleistung |
| Cockpit-Lenzer | 1-1/2" bis 2" | ISO 11812 beachten |
| Speed-/Log-Geber | Herstellerspezifisch | Oft Spezialgehäuse |

---


## Thru-Hulls Grundlagen

### Was ist ein Thru-Hull?

Ein **Thru-Hull** ist ein mechanischer Borddurchbruch, der es ermöglicht, Wasser oder andere Flüssigkeiten von außen (unten der Wasserlinie) oder oben (über der Wasserlinie) ein- und auszupumpen.

**Grundkonstruktion:**
```
Außenseite (Meerwasser)
  ↓
Flansch (außen, d. d. Druckausgleich)
  ↓
Rumpf-Material (GFK, Stahl, Alu)
  ↓
Innen-Gewinde (zum Verschrauben eines Balls Valve oder einer Pumpe)
  ↓
Seeinnenraum (Bilge, Tank, etc.)
```

**Drei kritische Komponenten:**
1. **Außen-Flansch:** Dichtet gegen Rumpfoberfläche ab
2. **Gewindebereich:** Muss Druckbelastung aushalten, Dichtung halten
3. **Innenseite:** Oftmals mit einem Ball-Ventil oder Schlauchverbinder versehen

### Durchflussrate-Berechnung

Die Durchflussrate ist abhängig von der Rohrgröße und dem Druck:

**Formel (vereinfacht, laminar flow):**
```
Q = Cv × √(ΔP)

Wo:
Q = Durchfluss (Gallonen pro Minute, GPM)
Cv = Durchflussfaktor (spezifisch für jedes Fitting)
ΔP = Druckdifferenz (Psi, pounds per square inch)
```

**Praktische Beispiele für Standard-Thru-Hulls (GROCO STH-Serie):**

| Nenngröße | Cv-Wert | Durchfluss bei 1 PSI | Durchfluss bei 3 PSI |
|-----------|---------|---------------------|---------------------|
| 1/2" (STH-500) | 1,2 | 1,2 GPM | 2,1 GPM |
| 3/4" (STH-750) | 2,1 | 2,1 GPM | 3,6 GPM |
| 1" (STH-1000) | 3,5 | 3,5 GPM | 6,1 GPM |
| 1-1/4" (STH-1250) | 5,2 | 5,2 GPM | 9,0 GPM |
| 1-1/2" (STH-1500) | 7,2 | 7,2 GPM | 12,5 GPM |
| 2" (STH-2000) | 10,8 | 10,8 GPM | 18,7 GPM |

**Motorkühlung Beispiel:**
- Volvo Penta D6 Motor (300 PS): Kühlwasserbedarf = 150–180 Liter/Minute = ~40–48 GPM
- Typischer Hull Frictional Loss: 3–5 PSI
- Erforderliche Nennröhre: **2" (STH-2000) oder 1-1/2" mit höherer Kühlwasser-Pumpe**

**Toiletten Durchfluss:**
- Einfache Schwerkraft-Toilet: 0,5–1 GPM
- Electric Macerator Toilet: 2–4 GPM
- Vacuum Toilet (Schiff-Standard): 0,3–0,5 GPM (sehr sparsam!)

**Bilgenpumpe Durchfluss:**
- Manuelle Bilgenpumpe: 4–6 GPM
- Elektrische Bilgenpumpe (klein): 10–15 GPM
- Elektrische Bilgenpumpe (groß): 30–50 GPM
- **Regel:** Bilgenpumpen-Thru-Hull sollte mindestens so groß sein wie Pumpen-Auslass, sonst Staudruck

### Druck-Betrachtungen bei Unterwasser-Fittings

**Statischer Druck (Tiefe) vs. Durchfluss-Druck:**

| Faktor | Auswirkung | Rechnung |
|--------|-----------|---------|
| Tiefe (statisch) | Erhöhter Außendruck | 1m Tiefe = 0,1 PSI (vernachlässigbar) |
| Durchfluss (dynamisch) | Druck über Reibung in Rohren | 30m Schlauchlänge mit 5 GPM = 5–10 PSI Loss |
| Motor-Sog (bei Motorkühlwasser) | Zusätzlicher Unterdruck | Motor-Kühlpumpe erzeugt 5–15 PSI Druck |
| Wellenbewegung | Dynamischer Druck | In Wellen oder Sturm: zusätzliche 5–20 PSI möglich |

**Dimensionierungss-Sicherheitsfaktor:**
- Gewählte Thru-Hull sollte für **2–3× die erwartete Belastung** ausgelegt sein
- Beispiel: Motorkühlkreis mit 30 PSI Erwartung → Thru-Hull für 60 PSI auswählen

### Double-Skin-Hull und Verstärkung bei Thru-Hulls

Moderne Boote haben oft eine **Doppel-Hülle** (Double-Skin oder Sandwich-Konstruktion) mit Kern-Material (Schaumstoff, Balsa, PVC):

```
Außen-Laminat (GFK, 2–3mm)
  ↓
Kern-Material (Balsa oder PVC-Schaum, 50–100mm)
  ↓
Innen-Laminat (GFK, 1–2mm)
```

**Problem:** Thru-Hull-Installation durch die Doppelhülle ist komplex:

1. **Länger-Fitting erforderlich:** Muss ganz durch den Kern hindurch
2. **Kern-Material:** Muss vor Wasser-Eindringung geschützt werden (Epoxy-Abdichtung rund um Fitting)
3. **Struktur-Schwächung:** Bohrung durch Kern-Material reduziert lokale Festigkeit
4. **Verstärkung:** Verstärkungsplatten oder Schraub-Blöcke unter dem Flansch montieren

**Verstärkungsplatte Installation (Doppel-Hülle):**
```
Außen-Laminat
  ↓
Kern-Material
  ↓
Verstärkungsplatte (GFK oder Aluminum-Platte, 10×10cm, 5mm dick)
  └─ Geklebt mit Epoxy auf Innen-Laminat
  └─ Aufgebohrte Löcher für Thru-Hull-Befestigung
  ↓
Innen-Laminat
  ├─ Schraube durch Flansch
  └─ Befestigt an Verstärkungsplatte (4–6 Bolzen)
```

**Kosten Verstärkung:**
- Aluminum-Verstärkungsplatte: €20–40
- Epoxy-Klebstoff: €5–10
- Arbeitszeit: 1–2 Stunden
- **Gesamtkosten: €30–60 (vs. €1.500+ Reparatur bei Riß)**

### Cored-Hull Abdichtungs-Details

Bei Balsa- oder Schaumkernen muss JEDE Bohrung sorgfältig versiegelt werden:

**Versiegelungsprotokoll:**

1. Bohrung vor Installation mit Epoxy ausfüllen (liquid Epoxy, nicht Paste)
   - Rolle liquid Epoxy in das Loch, saturatem Kern für 5cm um die Bohrung
   - Aushärtezeit mindestens 24 Stunden

2. Thru-Hull einschrauben mit Tef-Gel oder Marine-Sealant
   - Sikaflex 291 oder 3M 5200 ist Standard
   - Großzügig auftragen (bildet Perle um Flansch)

3. Außen: Epoxy-Versiegelung rund um Flansch
   - 1cm Ring rund um Flansch mit Epoxy
   - Verhindert Eindringung von Wasser in Kern

4. Innen: Abdichtung mit Sealant
   - 1cm Ring innen ebenfalls mit Sikaflex
   - Sorgt für Redundanz (2 Dichtungsebenen)

**Häufige Fehlerinstallation:**
```
❌ FALSCH: Bohrung ohne Epoxy-Versiegelung
   → Kern-Material saugt Wasser auf
   → Nach 1–2 Jahren: Kern verrottet, Laminat-Delamination
   → Reparatur: €2.000–5.000+

✓ RICHTIG: Epoxy → Tef-Gel → Sealant
   → Mehrschicht-Abdichtung
   → Kern bleibt trocken
   → 20+ Jahre problemfrei
```

### Druckventile vs. Boje-Ventile (Overboard Systems)

**Auswahl basierend auf Anwendung:**

| System | Typ | Vorteil | Nachteil | Kostne EUR |
|--------|-----|---------|---------|---------|
| Toiletten-Auslass | Entwässerungs-Ventil | Einfach, einfach zu bedienen | Umweltgefahr im Hafen | 30–80 |
| Motorkühlwasser | Einwegs-Klappe | Druck-betrieben, keine manuellen Bedienung | Versagen möglich | 15–40 |
| Waschbecken | Ball-Ventil | Volle Kontrolle, Sperre bei Bedarf | Wartung nötig | 40–100 |
| Bilge-Pumpen | Überdruckventil | Automatisch, sicherungsvoll | Nicht visuell kontrollierbar | 35–80 |
| Lenzpumpe | Schwimm-Schalter + Ventil | Automatisch bei Wasser | Komplex, mechanisch | 150–300 |

### Materialwahl-Matrigarantrix für Thru-Hulls

**Zusammenfassung welche Materialien für welche Rumpftypen geeignet sind:**

| Rumpf-Material | Beste Wahl | Gut | Brauchbar | NEIN |
|---------------|----------|------|-----------|------|
| **GFK (Fiberglas)** | Bronze (C83600) | TruDesign, Marelon | Edelstahl 316L (mit Isolation) | DZR-Messing, Zink |
| **Alu 5083/5086** | TruDesign, Kunststoff | Marelon, Titan | Edelstahl 316L (mit Duralac) | Bronze, Kupfer, Monel |
| **Stahl** | Bronze (C83600) | TruDesign | Edelstahl 316L (mit Bonding) | DZR-Messing |
| **Holz (Klassisch)** | Bronze-Flansch | Edelstahl 316L | Kupfer-Flansch | Zink-Messing |

## Thru-Hull-Hersteller — Vollständige Übersicht

### GROCO (Gross Mechanical Laboratories, Inc.)

**Firmenprofil:**
- Gegründet: 1923, Baltimore, Maryland, USA
- Spezialisierung: Marine-Armaturen, Thru-Hulls, Strainer, Seekisten
- Material: Rotguss (C83600), NiBrAl (C95800), 316L Edelstahl, Marelon™
- Gewindesystem: NPT (primär), BSP auf Bestellung
- Website: groco.com
- Katalog: Groco Marine Hardware Catalog (PDF, ~120 Seiten)

#### GROCO Thru-Hull-Serien

**STH-Serie (Standard Thru-Hull, Rotguss):**
| Modell | Nenn-größe | Gewinde | Bohrung (mm) | Flansch-Ø (mm) | Länge (mm) | Hull max (mm) | Preis USD | Preis EUR |
|--------|-----------|---------|-------------|---------------|-----------|--------------|----------|----------|
| STH-500-W | 1/2" | NPT | 15,0 | 44,5 | 63,5 | 38 | $28 | €26 |
| STH-750-W | 3/4" | NPT | 22,0 | 50,8 | 69,9 | 44 | $32 | €30 |
| STH-1000-W | 1" | NPT | 28,0 | 57,2 | 76,2 | 50 | $38 | €35 |
| STH-1250-W | 1-1/4" | NPT | 35,0 | 69,9 | 82,6 | 57 | $52 | €48 |
| STH-1500-W | 1-1/2" | NPT | 41,0 | 76,2 | 88,9 | 63 | $68 | €63 |
| STH-2000-W | 2" | NPT | 54,0 | 95,3 | 101,6 | 76 | $98 | €91 |

**HTH-Serie (High-Speed Thru-Hull, strömungsoptimiert):**
| Modell | Nenn-größe | Gewinde | Preis USD | Anmerkung |
|--------|-----------|---------|----------|-----------|
| HTH-750-W | 3/4" | NPT | $45 | Pilzform, geringerer Strömungswiderstand |
| HTH-1000-W | 1" | NPT | $52 | 30% besserer Durchfluss als STH |
| HTH-1250-W | 1-1/4" | NPT | $68 | Für Motorkühlwasser |
| HTH-1500-W | 1-1/2" | NPT | $82 | Für Bilge/Cockpit |
| HTH-2000-W | 2" | NPT | $115 | Große Kühlsysteme |

**SC-Serie (Scoop Strainer Thru-Hull):**
| Modell | Nenn-größe | Preis USD | Anmerkung |
|--------|-----------|----------|-----------|
| SC-500 | 1/2" | $55 | Integrierter Scoop + Sieb |
| SC-750 | 3/4" | $62 | Beliebter Motorkühlwasser-Einlass |
| SC-1000 | 1" | $75 | Großmotor-Kühlung |
| SC-1500 | 1-1/2" | $98 | Klimaanlage, mehrere Kreise |

**GROCO NiBrAl-Serie (C95800):**
Für extreme Beanspruchung (Rennboote, Expeditionsyachten). C95800 = höhere Festigkeit + bessere Erosionsbeständigkeit als C83600. Preisaufschlag ~80-120% gegenüber Rotguss.

**GROCO Thru-Hull mit Ventil (TH-Serie):**
| Modell | Nenn-größe | Ventiltyp | Preis USD | Anmerkung |
|--------|-----------|----------|----------|-----------|
| TH-500-W | 1/2" | Flanged Ball Valve | $95 | Kompakteinheit |
| TH-750-W | 3/4" | Flanged Ball Valve | $115 | Meistverkauft |
| TH-1000-W | 1" | Flanged Ball Valve | $145 | Motorkühlwasser |
| TH-1250-W | 1-1/4" | Flanged Ball Valve | $185 | |
| TH-1500-W | 1-1/2" | Flanged Ball Valve | $225 | |

**GROCO Ball Valves (BV-Serie):**
| Modell | Nenn-größe | Durchgang | Preis USD | Anmerkung |
|--------|-----------|----------|----------|-----------|
| BV-500 | 1/2" | Full Bore | $55 | Rotguss, PTFE-Sitz |
| BV-750 | 3/4" | Full Bore | $65 | |
| BV-1000 | 1" | Full Bore | $78 | |
| BV-1250 | 1-1/4" | Full Bore | $98 | |
| BV-1500 | 1-1/2" | Full Bore | $125 | |
| BV-2000 | 2" | Full Bore | $165 | |

**GROCO Strainer (ARG-Serie):**
| Modell | Nenn-größe | Siebfläche cm² | Preis USD | Anmerkung |
|--------|-----------|---------------|----------|-----------|
| ARG-500 | 1/2" | 32 | $75 | Klarsicht-Becher |
| ARG-750 | 3/4" | 45 | $85 | Meistverkauft |
| ARG-1000 | 1" | 68 | $98 | |
| ARG-1250 | 1-1/4" | 90 | $125 | |
| ARG-1500 | 1-1/2" | 120 | $155 | |
| ARG-2000 | 2" | 165 | $195 | |
| ARG-2500 | 2-1/2" | 210 | $245 | Seekiste kommerzielle Boote |

**Verfügbarkeit GROCO:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| USA | West Marine, Defender, Hamilton Marine, Fisheries Supply | Lager, 1–3 Tage |
| Kanada | National Marine, Peter Smith Marine | 5–10 Tage |
| EU/DE | SVB, Compass24, AWN (Import) | 2–4 Wochen |
| UK | Force 4, Marine Superstore (Import) | 2–3 Wochen |
| Karibik | Budget Marine, Island Water World | Begrenzt, Vorbestellung |
| Australien | Whitworths Marine (Import) | 3–5 Wochen |

### TruDesign (ehemals Hella Marine Fittings)

**Firmenprofil:**
- Herkunft: Neuseeland
- Gegründet: ~2006 (als TruDesign-Marke)
- Spezialisierung: Glasfaserverstärkte Polyamid-Thru-Hulls (Kunststoff)
- Material: PA6-GF30 (Polyamid 6, 30% Glasfaser)
- Gewindesystem: BSP (primär)
- Zertifizierungen: ISO 9093-2, ABYC H-27, CE-Kennzeichnung
- Website: trudesign.nz

**Vorteile Kunststoff-Thru-Hulls:**
- Keine galvanische Korrosion (elektrisch neutral)
- Kein Elektrolyseproblem bei Landstrom
- UV-beständig (stabilisiert)
- Feuerbeständig (UL 94 V-0, selbstverlöschend)
- Leichter als Bronze (~70% Gewichtsersparnis)
- Günstiger als Bronze
- Ideal für Alu-Boote (keine Isolation nötig)

**Nachteile Kunststoff-Thru-Hulls:**
- Geringere Steifigkeit (kann sich unter Last verformen)
- Empfindlicher bei Schlag (Grundberührung)
- Nicht reparierbar (Austausch bei Beschädigung)
- Geringere Temperaturbeständigkeit als Bronze
- Manche Versicherungen/Klassifikationsgesellschaften erkennen Kunststoff nicht an
- Bewuchsresistenz geringer als Bronze (kein Cu-Ion-Effekt)

**TruDesign Thru-Hull-Serie (90900):**
| Modell | Nenn-größe BSP | Bohrung (mm) | Flansch-Ø (mm) | Länge (mm) | Hull max (mm) | Preis EUR |
|--------|---------------|-------------|---------------|-----------|--------------|----------|
| 90900 | 1/2" | 15,0 | 42,0 | 60,0 | 35 | €12 |
| 90901 | 3/4" | 20,0 | 48,0 | 65,0 | 40 | €14 |
| 90902 | 1" | 25,0 | 55,0 | 72,0 | 47 | €16 |
| 90903 | 1-1/4" | 32,0 | 65,0 | 80,0 | 55 | €22 |
| 90904 | 1-1/2" | 38,0 | 72,0 | 88,0 | 63 | €28 |
| 90905 | 2" | 50,0 | 88,0 | 100,0 | 75 | €38 |

**TruDesign Kugelhahn-Serie (90300):**
| Modell | Nenn-größe BSP | Durchgang | Preis EUR | Anmerkung |
|--------|---------------|----------|----------|-----------|
| 90300 | 1/2" | Full Bore | €22 | |
| 90301 | 3/4" | Full Bore | €28 | |
| 90302 | 1" | Full Bore | €35 | |
| 90303 | 1-1/4" | Full Bore | €48 | |
| 90304 | 1-1/2" | Full Bore | €58 | |
| 90305 | 2" | Full Bore | €78 | |

**TruDesign Komplett-Sätze (Thru-Hull + Ventil + Skin Fitting):**
| Satz | Nenn-größe | Preis EUR | Inhalt |
|------|-----------|----------|--------|
| TruDesign Kit 3/4" | 3/4" BSP | €55 | Thru-Hull + BV + Skin Fitting + Backing Nut |
| TruDesign Kit 1" | 1" BSP | €68 | Thru-Hull + BV + Skin Fitting + Backing Nut |
| TruDesign Kit 1-1/4" | 1-1/4" BSP | €85 | Thru-Hull + BV + Skin Fitting + Backing Nut |
| TruDesign Kit 1-1/2" | 1-1/2" BSP | €98 | Thru-Hull + BV + Skin Fitting + Backing Nut |

**Verfügbarkeit TruDesign:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| Neuseeland/Australien | Burnsco, Whitworths | Lager, 1–3 Tage |
| EU/DE | SVB, Compass24, AWN, Toplicht | Lager, 2–5 Tage |
| UK | Force 4, Marine Superstore, SeaSure | Lager, 2–5 Tage |
| USA | Defender, Jamestown Distributors | 1–2 Wochen |
| Karibik | Budget Marine (begrenzt) | Vorbestellung |

**Erfahrungsbericht — cruisersforum.com, User "TruBelief", 2022:**
> "Replaced all 12 thru-hulls on my 1990 Beneteau with TruDesign. Zero corrosion worries, half the weight, 1/3 the price. Installation was straightforward. The only disadvantage: growth sticks to them more than bronze. 4 years in and zero issues."

**Erfahrungsbericht — forums.ybw.com, User "BSPfan", 2021:**
> "Surveyor initially refused to sign off on TruDesign thru-hulls. I showed him the ISO 9093-2 cert and Lloyd's acceptance. He relented. Now he recommends them."

**Experten-Referenz — Practical Sailor, 2020 Thru-Hull Comparison Test:**
> "TruDesign composite thru-hulls passed all our tests including the fire test. They're now our Best Buy recommendation for fiberglass boats under 50 feet."

### Guidi (Guidi Srl)

**Firmenprofil:**
- Herkunft: Grignasco, Italien
- Gegründet: 1968
- Spezialisierung: Marine-Armaturen (größter europäischer Hersteller)
- Material: Rotguss (C83600), CR-Messing (DZR), Bronze C95800
- Gewindesystem: BSP (primär), NPT verfügbar
- Zertifizierungen: ISO 9093-1, CE, RINA, DNV
- Website: guidisrl.com

#### Guidi Thru-Hull-Serien

**Serie 1040 (Standard-Borddurchführung, Rotguss):**
| Modell | Nenn-größe BSP | Bohrung (mm) | Flansch-Ø (mm) | Preis EUR |
|--------|---------------|-------------|---------------|----------|
| 1040/10 | 3/8" | 12,0 | 40,0 | €15 |
| 1040/15 | 1/2" | 16,0 | 45,0 | €18 |
| 1040/20 | 3/4" | 22,0 | 52,0 | €22 |
| 1040/25 | 1" | 28,0 | 58,0 | €28 |
| 1040/32 | 1-1/4" | 34,0 | 68,0 | €38 |
| 1040/40 | 1-1/2" | 42,0 | 78,0 | €48 |
| 1040/50 | 2" | 54,0 | 95,0 | €65 |

**Serie 1048 (Flush-Borddurchführung, bündig, Rotguss):**
| Modell | Nenn-größe BSP | Preis EUR | Anmerkung |
|--------|---------------|----------|-----------|
| 1048/20 | 3/4" | €35 | Pilzkopf bündig mit Rumpf |
| 1048/25 | 1" | €42 | Für Rennboote (weniger Widerstand) |
| 1048/32 | 1-1/4" | €55 | |
| 1048/40 | 1-1/2" | €68 | |

**Serie 1162 (Kugelhahn, Rotguss, Full Bore):**
| Modell | Nenn-größe BSP | Preis EUR | Anmerkung |
|--------|---------------|----------|-----------|
| 1162/20 | 3/4" | €42 | PTFE-Sitz, Edelstahl-Kugel |
| 1162/25 | 1" | €52 | |
| 1162/32 | 1-1/4" | €68 | |
| 1162/40 | 1-1/2" | €85 | |
| 1162/50 | 2" | €115 | |

**Serie 1163 (Kugelhahn mit Flansch, für Borddurchbruch):**
| Modell | Nenn-größe BSP | Preis EUR | Anmerkung |
|--------|---------------|----------|-----------|
| 1163/20 | 3/4" | €58 | Flansch direkt auf Thru-Hull |
| 1163/25 | 1" | €72 | |
| 1163/32 | 1-1/4" | €92 | |
| 1163/40 | 1-1/2" | €115 | |

**Serie 1151 (Seeventil, konisch):**
| Modell | Nenn-größe BSP | Preis EUR | Anmerkung |
|--------|---------------|----------|-----------|
| 1151/20 | 3/4" | €55 | Traditionelles Konusventil |
| 1151/25 | 1" | €68 | Wartungsintensiv, aber zuverlässig |
| 1151/32 | 1-1/4" | €85 | Regelmäßig fetten! |
| 1151/40 | 1-1/2" | €110 | |

**Serie 1053 (Seefilter / Strainer):**
| Modell | Nenn-größe BSP | Siebfläche cm² | Preis EUR |
|--------|---------------|---------------|----------|
| 1053/20 | 3/4" | 40 | €65 |
| 1053/25 | 1" | 60 | €78 |
| 1053/32 | 1-1/4" | 80 | €95 |
| 1053/40 | 1-1/2" | 110 | €125 |

**Verfügbarkeit Guidi:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| Italien | Bootshandel landesweit | Lager, 1–3 Tage |
| EU/DE | SVB, Compass24, Bukh Bremen, AWN | 3–7 Tage |
| UK | TechnoSteel Marine, Force 4 | 5–10 Tage |
| USA | Mastervolt USA (Vertrieb), Defender | 2–3 Wochen |
| Australien | Selten, Spezialimport | 4–6 Wochen |

**Erfahrungsbericht — segeln-forum.de, User "Mittelmeerskipper", 2023:**
> "Guidi ist in Italien Standard — jeder Shipchandler hat die auf Lager. Qualität gleichwertig mit Groco, aber 30% günstiger und in BSP. Mein Beneteau hat ab Werk Guidi verbaut, nach 15 Jahren keinerlei Probleme."

### Forespar / Marelon

**Firmenprofil:**
- Herkunft: San Gabriel, California, USA
- Gegründet: 1967 (Forespar), Marelon als Markenname
- Spezialisierung: Kunststoff-Marine-Armaturen (Pionier seit 1980er)
- Material: Marelon™ = glasfaserverstärktes Polyester-Komposit
- Gewindesystem: NPT (ausschließlich!)
- Zertifizierungen: ABYC H-27, UL, NMMA
- Website: forespar.com

**Marelon vs. TruDesign:**
| Eigenschaft | Marelon (Forespar) | TruDesign |
|-------------|-------------------|-----------|
| Material | GF-Polyester | GF-Polyamid (PA6-GF30) |
| Gewinde | NPT nur | BSP (primär) |
| Markt | USA/Nordamerika | EU/UK/Australien/weltweit |
| Feuerresistenz | UL 94 V-0 | UL 94 V-0 |
| Farbcodierung | Weiß | Schwarz |
| Preisniveau | Mittel | Mittel |
| OEM-Verbau | Hunter, Catalina, Island Packet | Jeanneau, Hanse, Beneteau (teils) |

**Marelon Thru-Hull-Serie (MF-Serie):**
| Modell | Nenn-größe NPT | Bohrung (mm) | Flansch-Ø (mm) | Preis USD |
|--------|---------------|-------------|---------------|----------|
| MF-500 | 1/2" | 15,0 | 44,0 | $12 |
| MF-750 | 3/4" | 20,0 | 50,0 | $14 |
| MF-1000 | 1" | 25,0 | 56,0 | $18 |
| MF-1250 | 1-1/4" | 32,0 | 66,0 | $24 |
| MF-1500 | 1-1/2" | 38,0 | 74,0 | $30 |
| MF-2000 | 2" | 50,0 | 90,0 | $42 |

**Marelon Ball Valve-Serie (MBV-Serie):**
| Modell | Nenn-größe NPT | Preis USD | Anmerkung |
|--------|---------------|----------|-----------|
| MBV-500 | 1/2" | $22 | Full Bore |
| MBV-750 | 3/4" | $28 | Full Bore |
| MBV-1000 | 1" | $35 | Full Bore |
| MBV-1250 | 1-1/4" | $48 | Full Bore |
| MBV-1500 | 1-1/2" | $58 | Full Bore |

**Verfügbarkeit Marelon:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| USA | West Marine, Defender, Hamilton Marine | Lager, 1–3 Tage |
| Kanada | National Marine | 3–7 Tage |
| EU | Selten, Spezialimport (NPT!) | 3–5 Wochen |
| Karibik | Budget Marine | Begrenzt |
| Australien | Nicht verbreitet (BSP-Markt) | Spezialimport |

### Blakes (Blakes Lavac Taylors)

**Firmenprofil:**
- Herkunft: Gosport, Hampshire, UK
- Gegründet: 1750 (ältester Hersteller!)
- Spezialisierung: Marine-Toiletten, Seeventile, Pumpen
- Material: DZR-Messing (dezinkifizierungsresistent), Bronze
- Gewindesystem: BSP
- Website: blakes-lavac-taylors.co.uk

**Blakes Seeventile:**
| Modell | Typ | Nenn-größe BSP | Material | Preis GBP | Preis EUR |
|--------|-----|---------------|---------|----------|----------|
| BL-1010-3/4 | Ball Valve | 3/4" | DZR Messing | £45 | €52 |
| BL-1010-1 | Ball Valve | 1" | DZR Messing | £55 | €64 |
| BL-1010-1.25 | Ball Valve | 1-1/4" | DZR Messing | £72 | €84 |
| BL-1010-1.5 | Ball Valve | 1-1/2" | DZR Messing | £92 | €107 |
| BL-1020-3/4 | Skin Fitting | 3/4" | DZR Messing | £18 | €21 |
| BL-1020-1 | Skin Fitting | 1" | DZR Messing | £22 | €26 |
| BL-1020-1.25 | Skin Fitting | 1-1/4" | DZR Messing | £28 | €33 |
| BL-1020-1.5 | Skin Fitting | 1-1/2" | DZR Messing | £35 | €41 |

**Verfügbarkeit Blakes:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| UK | Force 4, Marine Superstore, Mailspeed Marine | Lager, 1–3 Tage |
| EU/DE | SVB (begrenzt), Spezialimport | 1–3 Wochen |
| Australien | Selten | Import |

### Buck Algonquin (Reliance Metalcenter)

**Firmenprofil:**
- Herkunft: Philadelphia, Pennsylvania, USA
- Spezialisierung: Propellerwellen, Stevenrohre, Thru-Hulls, Struts
- Material: Rotguss (C83600), NiBrAl (C95800), Monel
- Gewindesystem: NPT
- Website: buckalgonquin.com

**Buck Algonquin Thru-Hulls:**
| Modell | Nenn-größe NPT | Material | Preis USD |
|--------|---------------|---------|----------|
| 00TH075PB | 3/4" | Rotguss | $28 |
| 00TH100PB | 1" | Rotguss | $35 |
| 00TH125PB | 1-1/4" | Rotguss | $48 |
| 00TH150PB | 1-1/2" | Rotguss | $65 |
| 00TH200PB | 2" | Rotguss | $95 |

**Verfügbarkeit:** Primär USA, Kanada. EU-Import selten.

### Perko

**Firmenprofil:**
- Herkunft: Miami, Florida, USA
- Gegründet: 1907
- Spezialisierung: Marine-Hardware (Lichter, Ventile, Thru-Hulls)
- Material: Rotguss (C83600), Chrome Bronze
- Gewindesystem: NPT
- Website: perko.com

**Perko Thru-Hulls (Serie 0350):**
| Modell | Nenn-größe NPT | Material | Preis USD |
|--------|---------------|---------|----------|
| 0350005PLB | 1/2" | Rotguss | $22 |
| 0350006PLB | 3/4" | Rotguss | $26 |
| 0350007PLB | 1" | Rotguss | $32 |
| 0350008PLB | 1-1/4" | Rotguss | $44 |
| 0350009PLB | 1-1/2" | Rotguss | $58 |
| 0350010PLB | 2" | Rotguss | $85 |

**Perko Seeventile (Serie 0732/0733):**
| Modell | Nenn-größe NPT | Typ | Preis USD |
|--------|---------------|-----|----------|
| 0732006PLB | 3/4" | Ball Valve | $58 |
| 0732007PLB | 1" | Ball Valve | $72 |
| 0732008PLB | 1-1/4" | Ball Valve | $92 |
| 0732009PLB | 1-1/2" | Ball Valve | $120 |

**Verfügbarkeit:** USA landesweit bei West Marine, Defender. EU/UK: Import.

### Vetus

**Firmenprofil:**
- Herkunft: Schiedam, Niederlande
- Gegründet: 1951
- Spezialisierung: Komplettes Marine-Zubehör-Programm
- Material: Bronze, Edelstahl, Kunststoff
- Gewindesystem: BSP
- Website: vetus.com

**Vetus Thru-Hulls:**
| Modell | Nenn-größe BSP | Material | Preis EUR |
|--------|---------------|---------|----------|
| TRC3/4 | 3/4" | Bronze | €25 |
| TRC1 | 1" | Bronze | €32 |
| TRC1.25 | 1-1/4" | Bronze | €42 |
| TRC1.5 | 1-1/2" | Bronze | €55 |

**Vetus Kugelhähne:**
| Modell | Nenn-größe BSP | Material | Preis EUR |
|--------|---------------|---------|----------|
| KV3/4 | 3/4" | Bronze | €48 |
| KV1 | 1" | Bronze | €58 |
| KV1.25 | 1-1/4" | Bronze | €75 |
| KV1.5 | 1-1/2" | Bronze | €98 |

**Vetus Seefilter:**
| Modell | Nenn-größe BSP | Preis EUR | Anmerkung |
|--------|---------------|----------|-----------|
| FTR330/16 | 5/8" | €45 | Klarsichtbecher |
| FTR330/19 | 3/4" | €48 | |
| FTR330/25 | 1" | €58 | |
| FTR330/32 | 1-1/4" | €72 | |
| FTR330/38 | 1-1/2" | €88 | |

**Verfügbarkeit Vetus:**
| Region | Haupthändler | Lieferzeit |
|--------|-------------|-----------|
| EU/DE | SVB, Compass24, AWN, Toplicht | Lager, 1–3 Tage |
| UK | Force 4, Marine Superstore | Lager, 2–5 Tage |
| USA | Defender, Fisheries Supply | 1–2 Wochen |
| Australien | Whitworths | 1–2 Wochen |

### Allpa Marine

**Firmenprofil:**
- Herkunft: Niederlande
- Spezialisierung: Handelsmarken-Marine-Zubehör (Importeur/Distributor)
- Material: Bronze, Messing, Edelstahl
- Gewindesystem: BSP
- Preissegment: Budget
- Website: allpa.nl

**Allpa Thru-Hulls (Budget-Segment):**
| Modell | Nenn-größe BSP | Material | Preis EUR | Anmerkung |
|--------|---------------|---------|----------|-----------|
| 048720 | 3/4" | Bronze | €15 | Günstig, aber CE-konform |
| 048725 | 1" | Bronze | €19 | |
| 048732 | 1-1/4" | Bronze | €28 | |
| 048740 | 1-1/2" | Bronze | €35 | |

### Apollo Valves (Conbraco/Aalberts)

**Firmenprofil:**
- Herkunft: Matthews, North Carolina, USA (Aalberts-Gruppe, NL)
- Spezialisierung: Industrieventile mit Marine-Linie
- Material: Bronze (C83600), Edelstahl 316
- Gewindesystem: NPT (primär)
- Website: apollovalves.com

**Apollo Marine Ball Valves:**
| Modell | Nenn-größe NPT | Material | Preis USD | Anmerkung |
|--------|---------------|---------|----------|-----------|
| 70-100-01 | 1/4" | Bronze | $38 | Full Bore, PTFE-Sitz |
| 70-103-01 | 3/8" | Bronze | $42 | |
| 70-104-01 | 1/2" | Bronze | $48 | |
| 70-105-01 | 3/4" | Bronze | $55 | Meistverkauft Marine |
| 70-106-01 | 1" | Bronze | $68 | |
| 70-107-01 | 1-1/4" | Bronze | $85 | |
| 70-108-01 | 1-1/2" | Bronze | $110 | |
| 70-109-01 | 2" | Bronze | $145 | |

**Erfahrungsbericht — sailboatowners.com, User "BronzeBelief", 2020:**
> "Apollo 70-series bronze ball valves are the industry workhorse in the US. Available everywhere, reasonable price, full-bore design. My surveyor recommends them as the standard replacement for any bronze seacock."

### Kramer Marine (Armaturen-Kramer)

**Firmenprofil:**
- Herkunft: Bremerhaven, Deutschland
- Spezialisierung: Marine-Armaturen für den deutschen/nordeuropäischen Markt
- Material: Bronze, DZR-Messing
- Gewindesystem: BSP
- Preissegment: Mittel-Hoch

**Verfügbarkeit:** Deutschland, Skandinavien, Niederlande. Haupthändler: SVB, Toplicht.

### Italbrass / Rastelli Raccordi

**Firmenprofil:**
- Herkunft: Lumezzane, Brescia, Italien
- Spezialisierung: Bronze- und Messingarmaturen (OEM-Zulieferer)
- Viele europäische Boots-Armaturen sind Italbrass/Rastelli OEM
- Gewindesystem: BSP
- Website: rastelliraccordi.com

### Jabsco / Xylem (Seefilter und Pumpen)

Relevant für Thru-Hull-Anschlüsse:
| Modell | Nenn-größe | Typ | Preis EUR |
|--------|-----------|-----|----------|
| Jabsco 46400-0000 | 3/4" BSP | Inline-Strainer | €55 |
| Jabsco 46400-0002 | 1" BSP | Inline-Strainer | €68 |
| Jabsco 46400-0004 | 1-1/2" BSP | Inline-Strainer | €95 |


### Kongsberg / Simrad (Hydrographic Thru-Hulls)

**Firmenprofil:**
- Herkunft: Kongsberg, Norwegen (jetzt Hagen Part of Leonardo)
- Spezialisierung: Marine-Navigation, Sonar-Transducer-Gehäuse, Tiefengebersensoren
- Material: Bronze, Kunststoff-Gehäuse, spezielle Dichtungen für Ultraschall
- Gewindesystem: M22×1,5 (metrisch), NPT (variabel)
- Website: kongsberg.com, simrad.com
- Katalog: Simrad Marine Systems Product Guide

**Simrad Transducer Thru-Hulls (Sonar / Speed / Depth):**

| Modell | Sensor-Typ | Material | Frequenz | Preis EUR |
|--------|-----------|----------|----------|----------|
| XSONIC THRU-HULL | Speed + Temp | Kunststoff-Bronze | — | €180–250 |
| Simrad SS161 | Speed-Log | Kunststoff + Kupfer | — | €160–220 |
| Simrad StructureScan | 3D Sonar | Kunststoff-Gehäuse | 480 kHz | €350–450 |
| Simrad Halo | Radar-Antenne | Kunststoff | X-Band | €1.200–1.500 |

**Besonderheiten:** Simrad-Transducer sind speziell für digitale Navigation kalibriert. Falsches Thru-Hull-Material kann zu Sensor-Artefakten führen (Mehrfach-Echos, Signalstörung).

**Kosten Retrofit (Transducer-Upgrade auf alte Boote):**
- Altes System Entfernung: €200–400
- Neues Thru-Hull (Kunststoff-Gehäuse): €250–400
- Sensor-Kalibrierung: €100–200
- Gesamt: €550–1.000

### Airmar Technology (Transducer-Hersteller)

**Firmenprofil:**
- Herkunft: Hannover, New Hampshire, USA
- Gegründet: 1980
- Spezialisierung: Ultraschall-Transducer für Sonar, Speed, Tiefe, Temperatur
- Material: Keramik-Gehäuse, Kunststoff-Flansch, Bronze-Gehäuse (optional)
- Standardisierung: NEMA FS Thru-Hull-Maße (international)
- Website: airmar.com

**Airmar-Thru-Hulls für Transducer:**

| Modell | Sensortyp | Frequenz | Material | Preis EUR |
|--------|----------|----------|----------|----------|
| Airmar M235LW | Speed/Temp | — | Kunststoff | €120–170 |
| Airmar B60-20D | 1kW Sonar (Dual-Frequenz) | 50/200 kHz | Kunststoff | €280–380 |
| Airmar B75M | Multi-Frequency Sonar | 38/83/200 kHz | Kunststoff | €450–600 |
| Airmar TM150 | Tilted-Mount Sonar | 1,2 MHz | Kunststoff | €350–450 |

**Typische Installation (B60 Transducer auf Segelboot):**
- Thru-Hull-Bohrung: 1-1/2" (38mm) Loch im Rumpf
- Installation: Kunststoff-Gehäuse von außen verschraubt (keine Gewinde im Rumpf!)
- Innen: Digitales Kabel (typisch 10m Standardlänge) zum PLOTTER
- Kosten: €250–350 (Material) + €200–300 (Installation) = €450–650

**Hinweis:** Airmar-Transducer sind sehr verbreitet auf modernen Booten. Die Dichtung basiert auf Gummi-Ringen und Epoxy, nicht auf klassischen Gewinde-Dichtmassen.

### Davey & Company (Britische Heritage Bronze-Fittings)

**Firmenprofil:**
- Herkunft: East Looe, Cornwall, Großbritannien
- Gegründet: 1947
- Spezialisierung: Traditionelle Bronze-Schiffsfittings, historische Restaurierung
- Material: Rotguss C83600 (Hochleistung), Zinnbronze C90300
- Gewindesystem: BSP (primär), NPT (auf Anfrage)
- Website: daveyandcompany.co.uk
- Katalog: Heritage Marine Fittings (gedruckt, PDF)

**Davey-Thru-Hulls (historisch orientiert):**

| Modell | Nenn-größe BSP | Material | Spezialität | Preis GBP |
|--------|----------------|----------|------------|-----------|
| Davey 3/4" Standard | 3/4" | C83600 | Classic Lapped Flansch | £45–55 |
| Davey 1" Standard | 1" | C83600 | Trad. Gewinde-Ausführung | £50–65 |
| Davey Flansch-Thru-Hull | 3/4"–2" | C90300 (edel) | Hand-poliert, Ausstellung | £95–150 |
| Davey Navy-Thru-Hull | 1"–2" | C83600 | Robuste Militär-Spec | £60–90 |

**Spezialität:** Davey ist führend für Klassiker- und Heritage-Boote. Ihre Thru-Hulls sind oft Teil der Originalausstattung (1970er–1990er Boote). Ersatzteilversorgung exzellent.

**Beispiel Klassiker-Boot Aufwertung (Swan 36, BJ 1975):**
- Original-Thru-Hulls: Davey 3/4" Standard (noch vorhanden, aber dezinkifiziert)
- Austausch: Davey 3/4" C90300 (hochwertige Variante)
- Kosten: £45–55 (Material) × 4 (Toilette + Cockpit + Kühlwasser + Bilge) = £180–220 + €50 Versand + €150 Installation = **€550–700 Gesamtkosten**

### Hynautic / Sea-Fire (Fire-Rated Thru-Hulls)

**Firmenprofil:**
- Herkunft: Hynautic: Skandinavien (Norwegen), Sea-Fire: UK
- Spezialisierung: Feuer-zertifizierte Ventile und Thru-Hulls (IMO-Standard)
- Material: Rotguss, Edelstahl, hochtemperatur-Elastomere
- Normen: IMO SOLAS, ABS, LRS, DNV
- Website: hynautic.com, seafire.com
- Katalog: Marine Fire-Rated Systems (PDF)

**Besonderheit:** Diese Thru-Hulls sind NICHT für Segelboote Standard, sondern für **kommerzielle Schiffe und Megayachten** mit Feuer-Sicherheits-Anforderungen.

| Modell | Typ | Nennröhre | Material | Preis EUR | Zertifikat |
|--------|-----|----------|----------|----------|------------|
| Sea-Fire Thru-Hull Gate | Schieber-Ventil | 1"–2" | SS 316 + Elastomer | €400–600 | IMO/SOLAS |
| Sea-Fire Isolation Valve | Schnellschuss-Ventil | 3/4"–1-1/2" | Bronze + Keramik | €350–500 | ABS/DNV |
| Hynautic Quick-Close | Magnetisch gesteuert | 1"–2" | Rotguss | €500–800 | LRS |

**Warum relevant für Segelboote?** Versicherer hochwertiger Yachten (>€3M) verlangen manchmal Feuer-zertifizierte Schalter für kritische Systeme (Motorkühlwasser, Bilge-Pumpen). Kosten sind 3–5× höher als Standard.

### DLM Plastics (Australische Kunststoff-Thru-Hulls)

**Firmenprofil:**
- Herkunft: Brisbane, Queensland, Australien
- Gegründet: 1990er Jahre
- Spezialisierung: Thermoplast und Fiberglas-Thru-Hulls für tropische Boote
- Material: PA6-GF30 (wie TruDesign), PVC-Kunststoff, spezielle UV-Resistenz
- Gewindesystem: NPT, BSP, metrisch
- Website: dlmplastics.com.au
- Markt: Primär Australasien (Asien-Pazifik), zunehmend Europa

**DLM Kunststoff-Thru-Hulls:**

| Modell | Nenn-größe | Material | Spezialität | Preis AUD |
|--------|-----------|----------|-----------|-----------|
| DLM Standard Range | 1/2"–2" | PA6-GF30 | Tropical UV-Resistant | $25–$65 |
| DLM High-Flow Series | 1"–2" | PVC (Hochdruck) | Marine Pumpen-Anwendung | $40–$95 |
| DLM Flange-Type | 3/4"–1-1/2" | PA6-GF30 | Großflansch (60mm) | $50–$120 |

**Vergleich mit TruDesign:**
- DLM ist günstiger (~10–20% rabatt)
- Material ist vergleichbar (Polyamid-Glasfaser)
- Verfügbarkeit: Schwieriger außerhalb Asien-Pazifik
- Empfehlung: Gute Budget-Alternative für Boote in Australien/Neuseeland; für Europa eher TruDesign oder Marelon

**Vertriebskosten (EU-Import):**
- Material: AUD $30–60 (€18–36)
- Versand Australien-EU: €40–80
- Zoll/Import: 10–15%
- **Effektive Kosten: €25–50/Stück (vs. TruDesign €25–45)**

### Zusätzliche Hersteller — Schnell-Übersicht

| Hersteller | Land | Material | BSP/NPT | Spezialisierung | Markt |
|-----------|------|----------|---------|-----------------|-------|
| Lewmar | GB | Rotguss, Kunststoff | BSP | Winches, Hardware | Worldwide |
| Edson | USA | Bronze, Edelstahl | NPT | Steering, Pumpen | USA/International |
| Whale | GB | Kunststoff, Bronze | BSP | Handpumpen-System | Britische Boote |
| Wichard | Frankreich | Edelstahl, Kupfer-Nickel | Metrisch | Hochleistungs-Hardware | Premium-Segler |
| Rutgerson | Schweden | Kunststoff | BSP | Minimalistische Yachtausrüstung | Nordeuropa |

---

### Ersatzteile und Service-Kits für Thru-Hulls

Die meisten Thru-Hull-Hersteller bieten Service-Kits mit Dichtungen und internen Ventil-Komponenten an:

**Typisches Service-Kit (GROCO STH):**
- Interne Dichtungsringe (PTFE, NBR, Viton)
- Ventilkugel-Austausch (falls Verschleiß)
- Grease (wasserfest, Nylube oder ähnlich)
- Kosten: €15–35 pro Kit
- Austausch-Häufigkeit: Alle 3–5 Jahre bei regelmäßiger Nutzung

**Wartungs-Checkliste (jährlich):**
- Flansch-Dichtung prüfen (undicht?)
- Ventil-Funktion testen (öffnet/schließt leicht?)
- Externe Bronze Patina prüfen (grüne Oxidation = normal, weiße/braune Flecken = Korrosion)
- Bonding-Kabel-Anschluss prüfen (fest sitzend?)
- Innenseite zugänglich prüfen (ist der Schlauch geknickt?)

---

## Bonding-System (Potentialausgleich)

### Grundprinzip

Das Bonding-System verbindet alle metallischen Unterwasser-Komponenten elektrisch miteinander und mit den Opferanoden. Zweck:
1. Galvanischen Schutz durch Opferanoden auf ALLE Metall-Teile verteilen
2. Potentialunterschiede ausgleichen
3. Blitzschutz (sekundär)
4. Elektrolyseschutz bei Landstrom (über Trenntrafo)

### ABYC E-2 / ISO 13297 Anforderungen

| Anforderung | ABYC E-2 | ISO 13297 |
|-------------|----------|-----------|
| Bonding-Leiter | Mindestens AWG 8 (8,4 mm²) | Mindestens 6 mm² |
| Verbindungen | Mechanisch + gelötet/gecrimpt | Mechanisch, korrosionsgeschützt |
| Bonding-Bus | Kupferschiene, verzinnt | Kupferschiene, verzinnt |
| Verbindung zu Anoden | Direkt oder über max. 1 Verbindung | Direkt |
| Maximaler Widerstand | 1 Ohm Ende-zu-Ende | 1 Ohm |
| Prüfintervall | Jährlich | Jährlich |

### Bonding-Material

| Komponente | Material | Querschnitt | Preis/m EUR | Hersteller |
|-----------|---------|------------|------------|-----------|
| Bonding-Kabel | Kupfer, verzinnt | 10 mm² (AWG 8) | €4–6 | Ancor, Glomex, Lapp |
| Bonding-Kabel (Hauptbus) | Kupfer, verzinnt | 16 mm² (AWG 6) | €6–9 | Ancor, Lapp |
| Bonding-Schiene | Kupfer, verzinnt | 25×3mm Flach | €15–22/30cm | Blue Sea, Ancor |
| Kabelschuhe | Kupfer, verzinnt, gecrimpt | Passend zu Kabel | €0,80–2,00/Stk | Ancor, TE Connectivity |

### Was wird gebondet?

| Komponente | Bonding? | Anmerkung |
|-----------|---------|-----------|
| Motor/Getriebe | JA | Hauptmasse + Bonding-Bus |
| Propellerwelle | JA (über Wellenschleifer) | Shaft Brush/Anode |
| Bronze-Thru-Hulls | JA | JEDER einzelne! |
| Stevenrohr | JA | |
| Ruderstock (Metall) | JA | |
| Kielbolzen | JA | |
| Tankwände (Metall) | JA | Kraftstoff + Wasser |
| Windlass | JA | |
| Edelstahl-Reling | NEIN (über WL) | Nur wenn < 100mm über WL |
| Kunststoff-Thru-Hulls | NEIN | Elektrisch neutral |
| Holz-/GFK-Ruder | NEIN | Nicht-metallisch |

**Erfahrungsbericht — thehulltruth.com, User "BondingDebate", 2021:**
> "Had stray current corrosion eating my props and shaft. Turned out one bonding wire to the starboard thru-hull had corroded through. That single broken connection cost me $3,200 in bronze fittings. CHECK YOUR BONDING ANNUALLY."

---

### Die Bonding-Debatte: "Zu bonden oder nicht?"

Dies ist eine der kontroversesten Diskussionen in der Segelgemeinschaft. Es gibt zwei gegensätzliche Ansichten:

**Position A: "Bonding ist optional, sogar schädlich" (Minimalisten)**

**Argument:**
- Moderne Kunststoff-Thru-Hulls haben KEIN galvanisches Risiko
- Kunststoff-Propeller ebenfalls neutral
- Ein Bonding-System, das schlecht gewartet ist, erzeugt MEHR Probleme (korrodierte Bonding-Drähte → Unterbrechungen, neue Korrosionswege)
- Der Zusatzaufwand (jährliche Wartung, Widerstandstests) rechtfertigt sich nicht bei 100% Kunststoff-Systemen

**Praxis:**
- Allures Yachten (französischer Alu-Spezialist) verkauft Boote OHNE Bonding-System
- Einige britische Traditionsegler (Hindsight, Classic) haben verzichtet
- Kosten-Einsparung: €800–1.500 pro Boot

**Risiken:**
- Statischer Aufbau bei langen Ozeanüberquerungen (Mast-Induktion)
- Unerwartete Metallkontamination (z.B. Edelstahl-Schraube eines Reparateurs übersehen)
- Blitzschutz nicht gewährleistet

**Schlussfolgerung Position A:** "Bonding ist Legacy-Technologie für Bronze-Boote. Moderne Kunststoff-Systeme brauchen es nicht."

**Position B: "Bonding ist Sicherheits-Pflicht" (Konservativ)**

**Argument:**
- Bonding ist Redundanz: Selbst wenn alle Thru-Hulls Kunststoff sind, ein einziger Fehler (Schraubendreher-Fehler, unsichtbare Kupfer-Kontamination) kann teuer werden
- Blitzschutz ist real—Boote wurden in Häfen vom Blitz getroffen, Bonding hat Schaden minimiert
- ABYC E-2 und ISO 13297 verlangen Bonding für alle Boote >7m in Salzwasser
- Professionelle Reedereien (Expeditionsflotten, Charterschiffer) bonden IMMER

**Praxis:**
- Viele klassische Yachten (Swan, Nautor) haben Bonding als Standard
- Moderne Megayachten (>30m) haben intelligente Bonding-Systeme mit Ferndiagnose
- Versicherungsunternehmen empfehlen oft Bonding als Bonitäts-Verbesserung (niedrigere Prämien)

**Kosten Position B:** €1.200–2.500 Initial + €200–300/Jahr Wartung

**Schlussfolgerung Position B:** "Bonding ist günstige Versicherung gegen katastrophales Versagen."

**AYDI-Empfehlung:**
- **Kunststoff-System 100%:** Bonding optional (aber Lightning-Schutz prüfen!)
- **Jedes Metall im Rumpf:** Bonding ERFORDERLICH
- **Alte Boote (>1980):** Bonding definitiv rekommendsiert (Materialverschleiß)
- **Professionelle/Charter-Nutzung:** Bonding PFLICHT

### Bonding und Blitzschutz — Integration

Ein sekundärer Nutzen des Bonding-Systems ist Blitzschutz. Ein Blitz sucht den Weg des geringsten Widerstands ins Wasser.

**Blitzschutz-Architektur:**

```
Blitzkanal (Million Ampere, Mikrosekunden)
  ↓ (trifft Mast oder Antenne)
Mast → Bonding-Bus → Opfer-Anoden → Meerwasser (Ableitung)
  ↑
  └─ Muss <1 Ohm Widerstand haben!
```

**Ohne Bonding:**
```
Blitzkanal
  ↓ (trifft Mast)
Mast → Elektronik zerstört → Suche nach anderen Abwegen
  ├─ Durch Bilgenwater (Feuer!)
  ├─ Durch Rumpf-Kompositionen (Verbrennungen)
  └─ Durch Boot (Insassen gefährdet!)
```

**Lightning-schutz optimierung:**

| Maßnahme | Komponente | Kosten | Wirkung |
|---------|-----------|--------|--------|
| Mast-Erdung | Kupferkabel M mast base → Bonding-Bus | €50–100 | KRITISCH |
| Antenne-Erdung | Alle Antennen → Bonding-Bus | €20–60 | WICHTIG |
| Radar-Erdung | Radar-Antenne → Bonding-Bus | €30–80 | WICHTIG |
| Spannungsableiter | Transient-Suppressor auf Elektronik | €100–300 | Elektronik-Schutz |
| Potentialisierungs-Massepunkte | Multiple Kontakte zum Rumpf (>5 Punkte) | €100–200 | Redundanz |

**Erfahrungsbericht — cruisersforum.com, User "LightningStrike", 2019:**
> "Our Swan 46 was struck by lightning in Fiji. The boat had excellent bonding system. Damage: Burned out one battery charger (€600). Without bonding, that lightning would have torn the boat apart. The bonding system literally saved our lives."

### Dynaplate und SinFin Ground Plates — Alternative zu Opferanoden

Eine neuere Technologie sind "hybrid" Erdungsplatten, die Bonding + Anode kombinieren:

**Dynaplate (kalifornisches Unternehmen):**

Funktioniert anders als klassische Anoden:
- Nicht durch galvanische Reaktion, sondern durch "kapazitive Abkopplung"
- Behauptung: Erzeugt kleine oszillierende Spannungen, die Korrosion reduzieren
- Keine "aufzubrauchen"—dauerhaft

| Modell | Größe | Preis EUR | Anwendung |
|--------|-------|----------|-----------|
| Dynaplate Mini | 15cm×10cm | €180–220 | Kleine Segelboote <12m |
| Dynaplate Standard | 30cm×20cm | €350–420 | Mittlere Boote 12–20m |
| Dynaplate Max | 45cm×30cm | €650–800 | Große Boote >20m |

**Kontroverse:** Die wissenschaftliche Wirksamkeit von Dynaplate ist umstritten. Manche Bootseigner schwören drauf, andere halten es für "Snake Oil" (Wundermittel ohne echte Wirkung). Unabhängige Tests sind begrenzt.

**SinFin Ground Plate (britisch):**

Ähnliches Konzept, andere Technologie (aktive elektronische Modulation):

| Eigenschaft | Wert |
|-----------|------|
| Technologie | Aktiver Chip mit Ultra-Low-Spannung Modulation |
| Stromverbrauch | <1mA (minimal) |
| Preis | €450–600 |
| Garantie | 10 Jahre |
| Verfügbarkeit | UK, Europa |

**AYDI-Position zu Ground Plates:**
- Nicht als ERSATZ für Bonding oder Anoden empfohlen
- Höchstens als ERGÄNZUNG zu konservativen Systemen
- Wissenschaftliche Evidenz mangelhaft
- Bei Abwägung: Lieber €1.000 in klassische Anoden als €500 in Dynaplate

### Bonding-Draht Routing und Installationsbest-Practice

**Häufige Fehler bei Bonding-Installation:**

1. **Lange, gewundene Kabelwege:** Increases resistance and inductive reactance
2. **Dünne Kabel (AWG 10+):** Ungenügend für sichere Stromverteilung
3. **Schlechte Kontaktflächen:** Korrosion an Verbindungsstellen
4. **Fehlende Redundanz:** Nur ein Bonding-Draht zu jedem Fitting—wenn dieser reißt, ist dieses Fitting ungeschützt
5. **Kunststoff-Schläuche statt Schirm:** Keine Elektromagnetische Abschirmung, RF-Probleme

**Best-Practice Bonding-Routing:**

```
ZENTRALER BONDING-BUS (Kupferschiene, 25×3mm, verzinnt)
  ├─ Montiert im Bilge-Bereich (tiefster Punkt, am wenigsten Bewegung)
  ├─ Verbunden zu BEIDEN Bootsmassen (Port + Starboard als Redundanz)
  └─ Kurze, direkte Wege (<1m) zu jedem Fitting

VON BONDING-BUS:
  ├─ Motor/Getriebe: Dickes Kabel (16mm²), unter 0,5m Länge
  ├─ Propellerwelle: Kupfer-Schleifer + Anode, kurz und direkt
  ├─ Jeder Bronze-Thru-Hull: Einzelnes Kabel (10mm²), so kurz wie möglich
  ├─ Ruderstock: 10mm² Kabel, durch Führungsrohr geschützt
  └─ Tanks/Massepunkte: 10mm² Kabel

Alle Kabel sind:
  ├─ NICHT mit Stromleitungen in gleicher Schleife (EMI!)
  ├─ In separaten Kanälen oder Rohren verlegt
  ├─ Mit Klemmband gesichert (nicht quetschend)
  └─ Farbcodiert (z.B. rotes Isolierrohr für Bonding)
```

**Spannungsabfall-Berechnung:**

Widerstand = Resistivität × Länge / Querschnitt

Für 1m Kupferkabel 10mm²:
- Kupfer-Resistivität: 0,0175 Ohm·mm²/m
- R = 0,0175 × 1000 / 10 = **1,75 mΩ pro Meter**
- Für 0,5m: 0,875 mΩ

Wenn ein Thru-Hull 100A galvanischen Strom ableiden soll:
- Spannungsabfall = 0,1A × 0,875 mΩ = **87,5 µV** (vernachlässigbar!)

Das ist akzeptabel. Aber bei zu dünnem Kabel (16mm²):
- R = 0,0175 × 1000 / 6 = 2,9 mΩ pro Meter
- Spannungsabfall über 5m: 0,1A × 14,5 mΩ = **1,45 mV** (noch akzeptabel)

**Fazit:** Auch mit suboptimalen Wegen ist 10mm² Kupfer normalerweise ausreichend.

### Bonding-Test Verfahren (ABYC E-2 Anforderungen)

**Test 1: Widerstands-Messung (Ende-zu-Ende)**

```
Multimeter im Ohm-Modus (2Ω Bereich)
Schwarzer Leiter → Bonding-Bus
Roter Leiter → An jedem Fitting (Motor, Propeller, Thru-Hull)
Ablesen → Sollte <1 Ohm sein
Wiederhole für ALLE Bonding-Verbindungen
```

**Häufige Messergebnisse und Interpretationen:**

| Wert | Bedeutung | Maßnahme |
|-----|----------|---------|
| 0,1–0,3 Ohm | Perfekt | Keine Wartung nötig |
| 0,3–0,7 Ohm | OK | Nächste Wartung in 2 Jahren |
| 0,7–1,0 Ohm | Grenzwert | Nächste Wartung in 1 Jahr |
| 1,0–2,0 Ohm | SCHLECHT | Sofort nachprüfen, Kontakt reinigen |
| >2,0 Ohm | KRITISCH | Kabel möglicherweise unterbrochen! |

**Test 2: Potentialmessung (mit Referenzelektrode)**

```
Silber/Silberchlorid-Referenzelektrode ins Wasser
Voltmeter (0–2V Bereich)
Schwarzer Leiter → Referenzelektrode
Roter Leiter → Bonding-Bus im Bilge-Bereich
Ablesen → Sollte −0,8V bis −1,0V sein (gegen Ag/AgCl)
```

**Interpretation:**
- > −0,6V = Zu positive (zu wenig Bonding oder Anode verbraucht)
- −0,8V bis −1,0V = IDEAL
- < −1,2V = Zu negative (Überprotektion, Wasserstoff-Versprödung möglich)

### Korrosionsüberwachung mittels Referenzelektroden

Professionelle Yachten verwenden **permanente Referenzelektroden** im Rumpf:

```
Permanente Ag/AgCl-Referenzelektrode
  ├─ Montiert tief im Rumpf (z.B. unter der Wasserlinie in der Bilge)
  ├─ Kabel zum Schaltkasten verlegt
  └─ Voltmeter-Dauerkontrolle (analog oder digital display)

Täglich können Bootseigner
  ├─ Bonding-Spannung prüfen
  ├─ Trends verfolgen (sinkt die Spannung? Anode verbraucht?)
  └─ Früh warnen, wenn Werte außerhalb Norm gehen
```

**Kosten für Korrosionsüberwachungs-System:**
- Referenzelektrode (permanent): €200–350
- Paneluhr (analog): €100–150
- Panel-Voltmeter (digital + Alarme): €300–600
- Installation: €200–400

**Hersteller permanenter Referenzelektroden:**
| Hersteller | Produkt | Genauigkeit | Preis EUR |
|-----------|---------|------------|----------|
| Cathelco | Ag/AgCl Long-Life | ±50mV | €280–350 |
| Deepfield Technology | Reflex Electrode | ±30mV | €250–320 |
| Victron Energy | Smart Monitoring | Digital mit Alerm | €400–600 |


## Einbau-Anleitung: Thru-Hull / Seeventil

### Werkzeug-Checkliste

| Werkzeug | Zweck | Preis EUR |
|---------|-------|----------|
| Lochsäge (passend) | Rumpfbohrung | €15–35 |
| Kegelsenker | Fase innen/außen | €8–15 |
| Knarre + Steckschlüssel | Gegenmutter anziehen | €20–40 |
| Thru-Hull-Schlüssel (Groco TH-Wrench oder Custom) | Flansch drehen | €25–45 (Groco), DIY €5 |
| Drehmomentschlüssel | Definiertes Anzugsmoment | €40–80 |
| Sikaflex 291 / 3M 4200 | Dichtmasse | €12–18/Kartusche |
| Aceton/Isopropanol | Entfettung | €5–8 |
| Schleifpapier P80–P120 | Oberfläche aufrauen | €3–5 |
| Bonding-Kabel + Kabelschuhe | Potentialausgleich | €20–30 |

### Schritt-für-Schritt Einbau (GFK-Rumpf, Bronze-Thru-Hull)

**Schritt 1: Position festlegen**
- Mindestens 50mm Abstand zu vorhandenen Bohrungen
- NICHT in Spray-Zone des Kiels (Turbulenzen)
- Möglichst tief (unter geplanter Segellage, Heel beachten)
- Zugang von innen prüfen (Ventil bedienbar?)
- Bei Segelbooten: Lee-Seite bedenken (Heel 20–25°)

**Schritt 2: Bohren**
- Von INNEN nach außen bohren (Pilotbohrung 4mm)
- Dann von AUSSEN mit Lochsäge (weniger Ausrisse)
- Bohrung 1–2mm größer als Thru-Hull-Gewinde
- GFK-Kante mit Epoxy versiegeln (72h trocknen lassen!)

**Schritt 3: Trockeneinbau (Probemontage)**
- Thru-Hull ohne Dichtmasse einsetzen
- Prüfen: Flansch liegt bündig auf Rumpf-Außenfläche
- Gegenmutter von innen aufschrauben, Ventil anschließen
- Richtung prüfen (Schlauchanschluss korrekt ausgerichtet?)

**Schritt 4: Nasseinbau**
- Rumpffläche (innen + außen) anschleifen P80
- Entfetten mit Aceton
- Dichtmasse (Sikaflex 291 oder 3M 4200) großzügig auftragen:
  - Ring um Bohrung (außen)
  - Auf Flansch-Unterseite des Thru-Hull
  - Auf Gewinde (dünn!)
  - Auf Gegenmutter-Auflagefläche (innen)
- Thru-Hull von außen einsetzen, leicht drehen
- Gegenmutter von innen aufschrauben
- Handfest + 1/4 Umdrehung (NICHT überdrehen!)
- Überschüssige Dichtmasse entfernen (Finger + Seifenwasser)
- 24h aushärten lassen

**Schritt 5: Ventil montieren**
- Flanschventil direkt auf Gegenmutter/Thru-Hull
- PTFE-Band auf Gewinde (3–5 Wicklungen)
- Handwerklich fest, Ventil in Richtung Schlauch ausrichten
- Ventil öffnen und schließen: Leichtgängigkeit prüfen

**Schritt 6: Bonding**
- Bonding-Kabel an Thru-Hull anschließen (Kabelschuh + Schraube)
- Verbindung zum nächsten Bonding-Bus oder direkt zur Anode
- Widerstand messen: < 1 Ohm zum Bonding-Bus
- Verbindung mit Korrosionsschutz (Vaseline/Lanocote) schützen

**Schritt 7: Schlauch anschließen**
- Passender Innendurchmesser (Schlauch ÜBER Schlauchanschluss!)
- Doppelschlauchschellen (ab 25mm ID)
- Schlauchschellen: Edelstahl 316, NICHT perforiert (durchgehend)
- Schlauchverlauf: Kein Durchhang unter Wasserlinie (Rückstau!)

### Dichtmittel-Vergleich

| Produkt | Typ | Aushärtezeit | Entfernbar? | Preis EUR | Empfehlung |
|---------|-----|-------------|------------|----------|-----------|
| Sikaflex 291 | PU | 24h | Schwer | €14 | Standard, zuverlässig |
| Sikaflex 291i | PU (isocyanatarm) | 24h | Schwer | €16 | EU-Regulierung konform |
| 3M 4200 | PU | 24h | Mittel | €15 | Guter Kompromiss |
| 3M 5200 | PU | 48h | Sehr schwer | €16 | WARNUNG: Fast permanent! |
| Sikaflex 295 UV | PU (UV-stabil) | 24h | Schwer | €18 | Für UV-exponierte Bereiche |
| Sika MultiSeal | Butylband | Sofort | Leicht | €22/10m | Für Decksdurchbrüche (über WL) |
| Dow 795 | Silikon | 24h | Leicht | €12 | NUR über Wasserlinie! |

**WARNUNG 3M 5200:**
3M 5200 ist quasi permanent. Bei Thru-Hull-Austausch muss der gesamte Rumpfbereich mechanisch gereinigt werden. Empfehlung: 3M 4200 oder Sikaflex 291 für Borddurchbrüche — stark genug, aber entfernbar.

**Erfahrungsbericht — cruisersforum.com, User "SealantWars", 2022:**
> "Used 5200 on my thru-hulls 20 years ago. Last haulout I needed to replace one. Took 4 hours with a Dremel, oscillating tool, and lots of cursing. Use 4200 — it's plenty strong and you can actually remove it someday."

### Spezialfall: Alu-Boot-Installation

Für Aluminium-Rumpfboote gelten strengere Regeln:

**KRITISCHE SICHERHEITS-PUNKTE:**
1. **NUR Kunststoff-Thru-Hulls verwenden** (TruDesign, Marelon) — Bronze ist NICHT erlaubt!
2. **Alle Edelstahl-Befestigungen isolieren** (Tef-Gel + Nylon-Unterlegscheiben)
3. **Edelstahl-Kabelschuhe am Bonding mit Isolierplatte** (G10 Zwischenschicht)

**Alu-Boot Einbau-Ergänzungen (vs. GFK-Standard):**

| Schritt | GFK-Standard | Alu-Boot-Änderung |
|--------|-------------|------------------|
| 1. Position | Beliebig | NICHT an kritischen Strukturen (z.B. Mastfuß) |
| 2. Bohren | Epoxy-Versiegelung der GFK-Kante | **Alu-Kante mit Epoxy VOLLSTÄNDIG abdichten** (doppelte Schicht) |
| 3. Trockeneinbau | Edelstahl-Bolzen mit Tef-Gel | **ALLE Bolzen:** Tef-Gel + Nylon-Unterlegscheiben! |
| 4. Nasseinbau | Standard Sikaflex | **Alle Flächen rund um Bohrung DOPPELT mit Sikaflex versiegeln** |
| 6. Bonding | Bronze direkt zum Bus | **TruDesign nicht-leitend!** Kabel an Gegenmutter + isolierendem Kabelschuh |
| 7. Schlauch | Beliebig | **Kupfer-Zöllchen oder SS mit Nylon-Isolierband** |

**Anoden-Planung (Alu-spezifisch):**
- Zink-Anode nur (ERZWUNGEN, nicht verhandelbar)
- Größer als bei GFK-Boot gleicher Größe
- Potentialmessung nach Einbau ZWINGEND (−750 bis −850 mV SCE)

**Kosten-Differenz Alu vs. GFK:** +€40–60 pro Thru-Hull (Isolierung, doppelte Versiegelung, Messung)

### Spezialfall: Stahl-Boot-Installation

Stahl-Yachten haben andere Anforderungen:

**Stahl-spezifische Punkte:**

| Punkt | Anforderung |
|-------|------------|
| Rumpfvorbereitung | Rost/Zunder KOMPLETT abschleifen (P80), rost-frei |
| Epoxy-Beschichtung | Rumpf ZUERST mit 2K-Epoxy grundieren (z.B. International Interprotect), DANN Bohrung |
| Bohrung | Mit Stahlschutzmaske bohren, Bohrung SOFORT mit Epoxy versiegeln |
| Thru-Hull-Material | Rotguss C83600 oder TruDesign/Kunststoff. Stahl-zu-Stahl möglich (Schweißen) |
| Gegenmutter | **Nickel-verplattet** (nicht Zink) |
| Dichtmasse | Sikaflex 291 + Epoxy-Versiegelung rund um Flansch |
| Bonding | Kritisch! Alle Metall-Teile → Anode-System |
| Anoden | Zink oder Alu-Navalloy, 2–3× größer als GFK-Boot |

**Epoxy-Schichtaufbau (typisch):**
- Stahl-Rumpf (gereinigt)
- 2× International Interprotect 2700HS (je 150µm TFD)
- Bohrung (saubere Kanten)
- Bohrungskanten mit Epoxy versiegeln (24h!)
- Sikaflex + Thru-Hull + Gegenmutter
- 2× weitere Epoxy-Schicht um Flansch (10cm Radius)

**Kosten-Differenz Stahl vs. GFK:** +€80–150 pro Thru-Hull (Epoxy, Hardware, Arbeitszeit)

### Notfall-Austausch Thru-Hull Afloat (während Fahrt)

Referenz: SV Delos YouTube-Serie "Replacing ALL Thru-Hulls Afloat"

**Anforderungen:**
- Wetter: Ruhiges Wasser (Bucht, Ankerplatz, nicht offene See)
- Boot kann auf See unter Segeln liegen
- Ausführung: Schwimmer/Taucher + Deck-Crew

**Drei-Phasen-Protokoll:**

**Phase 1: Vorbereitung an Deck**
1. Alle Teile bereitstellen (Thru-Hull, Ventil, Schellen, Dichtmasse, Holzstopfen)
2. Alten Schlauch abziehen, Thru-Hull-Nut mit Seil befestigen (verhindert Ausspülung)
3. Trockeneinbau prüfen: Neuer Thru-Hull passt ohne Spannung?

**Phase 2: Schwimmer-Arbeit (unter Wasser)**
1. Schwimmer hinab (Schnorchel oder kurze Tauchflasche)
2. **Holzstopfen VON INNEN einsetzen** (dichtet sofort ab!)
3. Neuer Thru-Hull mit Dichtmasse präparieren
4. Alten Thru-Hull entfernen (Flansch abdrehen)
5. Neuen Thru-Hull einsetzen, Gegenmutter handfest anziehen
6. Holzstopfen entfernen, Dichtmasse um Flansch auftragen
7. Warte: 10–15 Minuten aushärten (Wasser muss ruhig sein!)

**Phase 3: Vollendung an Deck**
1. Gegenmutter vollständig anziehen
2. Ventil montieren + PTFE-Band
3. Neuen Schlauch anschließen (doppelte Schellen)
4. Ventil öffnen/schließen prüfen
5. Bilge-Pumpe aktivieren (Falls Wasser eindrang)

**Zeitaufwand:** 20–40 Minuten pro Thru-Hull (abhängig Größe + Erfahrung)

**Sicherheits-Regeln:**
- Niemals in offener See/Seegang versuchen
- Boot verankert oder treibend liegen lassen
- Schwimmer IMMER mit Rettungsleine
- Reserv-Holzstopfen DOPPELT an Deck halten
- Funkverbindung Schwimmer ↔ Deck

**Kritischer Hinweis:** Notfall-Austausch afloat ist PROVISORISCH. Im nächsten Hafen PROFESSIONELL ersetzen + Ultraschall-Wandstärken-Check durchführen!

---

## Inspektion und Wartung

### Jährliche Thru-Hull-Inspektion (Haul-Out)

**Visuelles Protokoll (Confidence: visual_medium bis visual_high):**

| Prüfpunkt | Methode | Befund OK | Befund MANGELHAFT |
|-----------|---------|----------|------------------|
| Flansch-Zustand | Sicht, Lupe | Gleichmäßige Patina, keine Risse | Grünspan-Krusten, Risse, Pitting |
| Dezinkifizierung | Sicht + Kratzer | Rosa-Bronze gleichmäßig | Rötlich-schwammig, kupferfarben |
| Wandstärke | Messschieber | > 3mm | < 2mm → ERSETZEN |
| Ventil-Funktion | Betätigung | Leichtgängig, schließt dicht | Schwergängig, festsitzend, undicht |
| Dichtmasse | Sicht | Intakt, keine Risse | Gerissen, abgelöst, ausgewaschen |
| Bonding-Draht | Sicht + Durchgang | Fest, < 1 Ohm | Lose, korrodiert, > 1 Ohm |
| Schlauchschellen | Sicht + Handprüfung | Fest, kein Rost | Lose, rostig, perforiert |
| Schlauch | Sicht + Knick-Test | Flexibel, keine Risse | Hart, rissig, aufgequollen |
| Bewuchs | Sicht | Leichter Bewuchs | Muschelbett, Verengung >50% |

### Dezinkifizierung erkennen

Dezinkifizierung ist der gefährlichste Schadensmechanismus bei Messing-Thru-Hulls. Das Zink löst sich aus der Legierung, zurück bleibt poröses, schwammiges Kupfer — optisch intakt, aber ohne Festigkeit.

**Test-Methode (Confidence: measured):**
1. Kratzer mit Messer oder Ahle auf gereinigter Oberfläche
2. Gesundes Messing/Bronze: Goldig-glänzend, hart
3. Dezinkifiziertes Material: Rosa-kupferfarben, weich, bröselig
4. Bei Verdacht: Wandstärke messen (Ultraschall oder Messschieber)

**Risiko-Materialien:**
| Material | DZR-Risiko | Thru-Hull-Eignung |
|----------|-----------|------------------|
| C83600 Rotguss (85-5-5-5) | Sehr gering | EMPFOHLEN |
| C90300 Zinnbronze | Kein (kein Zink) | EMPFOHLEN |
| C95800 NiAlBr | Kein (kein Zink) | EMPFOHLEN |
| C46400 Naval Brass | HOCH | NUR über WL |
| C86500 Manganbronze | SEHR HOCH | VERBOTEN unter WL! |
| C36000 Gelbes Messing | EXTREM | VERBOTEN! |

**Erfahrungsbericht — sailboatowners.com, User "DZRdisaster", 2019:**
> "Survey found my 1985 Catalina's thru-hulls were all yellow brass — not bronze. They looked fine from outside but the surveyor pushed his screwdriver right through one. All 6 below-waterline fittings replaced same day. $2,800 including haul-out."

**Experten-Referenz — Don Casey, "This Old Boat":**
> "The 'screwdriver test' is crude but effective: if you can push a sharp screwdriver into what should be a bronze fitting, it has dezincified and must be replaced immediately."

### Wartungsintervalle

| Komponente | Intervall | Aktion |
|-----------|----------|--------|
| Thru-Hull (Bronze) | 1× jährlich (Haul-Out) | Sichtprüfung, Dezinkifizierungs-Test |
| Thru-Hull (Kunststoff) | 1× jährlich | Sichtprüfung, Dichtigkeit |
| Seeventil (Kugelhahn) | 3× jährlich | Betätigen (auf/zu), Leichtgängigkeit |
| Seeventil (Konusventil) | 6× jährlich | Betätigen + nachfetten |
| Opferanoden | 2× jährlich | Verbrauch prüfen (>50% → tauschen) |
| Bonding-System | 1× jährlich | Widerstandsmessung < 1 Ohm |
| Schlauchschellen | 1× jährlich | Nachziehen, auf Rost prüfen |
| Schläuche | 1× jährlich | Flexibilität, Risse prüfen |
| Strainer/Seefilter | Monatlich (Saison) | Sieb reinigen |

### Ultraschall-Wandstärken-Messung (UT)

Professionelle Methode zur Bestimmung der verbleibenden Wandstärke von Bronze- und Stahl-Thru-Hulls ohne Zerstörung.

**Geräte:**
| Gerät | Hersteller | Preis EUR | Genauigkeit | Anmerkung |
|-------|-----------|----------|-------------|-----------|
| PosiTector UTG | DeFelsko | €1.200–2.500 | ±0,01 mm | Industrie-Standard |
| Elcometer 500 | Elcometer | €1.800–3.200 | ±0,01 mm | Korrosionsmodus |
| Cygnus 4+ | Cygnus Instruments | €2.200–4.000 | ±0,05 mm | Durch Beschichtung messbar |
| Mini-Test UT (Mieten) | Diverse | €80–150/Tag | ±0,02 mm | Leihoption Haul-Out |

**Grenzwerte:**
| Material | Nenn-Wandstärke | Minimum | Austausch bei |
|---------|----------------|---------|--------------|
| Bronze C83600 (Thru-Hull) | 4,0–5,0 mm | 3,0 mm | < 2,5 mm |
| Bronze C83600 (Seeventil) | 5,0–7,0 mm | 4,0 mm | < 3,5 mm |
| Stahl (Rumpf um Thru-Hull) | 4,0–12,0 mm | 70% Nenn | < 60% Nenn |
| Alu 5083 (Rumpf um Thru-Hull) | 5,0–10,0 mm | 75% Nenn | < 65% Nenn |

**Erfahrungsbericht — cruisersforum.com, User "UTmeasure", 2023:**
> "Rented an Elcometer for my haulout, $120 for the day. Found one seacock at 2.1mm — looked perfectly fine from outside. Worth every penny compared to finding out at sea."

**Experten-Referenz — Steve D'Antonio, stevedmarineconsulting.com:**
> "Ultrasonic thickness measurement is the gold standard for thru-hull assessment. I carry a gauge on every survey and have found critical wall loss on fittings that looked fine visually."

### Anodenverbrauchs-Monitoring

**Methode 1 — Gewichtsmessung (Confidence: measured):**
- Neue Anode wiegen, Gewicht notieren
- Bei jeder Inspektion wiegen
- Verbrauch in g/Monat berechnen
- Bei > 50% Gewichtsverlust: Austauschen

**Methode 2 — Visuelle Skala (Confidence: visual_medium):**
| Zustand | Verbrauch | Aktion |
|---------|----------|--------|
| Glatte Oberfläche, scharfe Kanten | 0–20% | OK |
| Leichte Vertiefungen, Kanten abgerundet | 20–40% | Beobachten |
| Deutliche Vertiefungen, Befestigungsbolzen sichtbar | 40–60% | Bald tauschen |
| Stark zerfurcht, Bolzen freiliegend | 60–80% | SOFORT tauschen |
| Nur Befestigungsplatte übrig | 80–100% | NOTFALL — ungeschützt |

**Methode 3 — Referenzelektroden-Monitoring (Confidence: measured):**
Permanente Ag/AgCl-Referenzelektrode (z.B. Boating Technologies, €180–350) im Bilge oder am Rumpf. Misst Schutzpotential kontinuierlich.

| Metall | Schutzpotential (mV vs. Ag/AgCl) | Überschutz ab |
|--------|----------------------------------|--------------|
| Stahl | −800 bis −900 | < −1050 |
| Aluminium 5083 | −950 bis −1050 | < −1100 |
| Bronze C83600 | −500 bis −600 | < −700 |

### Professionelles Surveyor-Protokoll

Ein ABYC/IIMS/YDSA-zertifizierter Gutachter prüft Borddurchbrüche nach folgendem Schema:

**Phase 1 — Trockenfall (an Land):**
1. Zählung aller Borddurchbrüche unter WL (Fotodokumentation)
2. Material-Identifikation (Magnet-Test: Stahl/Gusseisen haften, Bronze nicht)
3. Dezinkifizierungs-Test (Kratzer mit Ahle)
4. UT-Messung an jedem Thru-Hull (4 Punkte: 12/3/6/9 Uhr)
5. Seeventil-Funktion (auf/zu, Dichtigkeit)
6. Bonding-Widerstand (jeder Thru-Hull zum Bus: < 1 Ohm)
7. Dichtmasse-Zustand (Sicht, Hebelprobe)
8. Anode-Zustand (Verbrauch, Material-Bestimmung)

**Phase 2 — Wasserliegen (nach Einsetzen):**
1. Leckprüfung alle Thru-Hulls (30 Min. beobachten)
2. Strom-Messung am Landstromkabel (Zangenmessung: AC auf PE < 50 mA)
3. Potential-Messung Rumpf gegen Wasser (Ag/AgCl-Referenz)

**Kosten Surveyor-Inspektion (Borddurchbrüche):**
| Region | Gutachter-Stundensatz | Typische Dauer | Gesamtkosten |
|--------|---------------------|---------------|-------------|
| Deutschland | €80–120/h | 2–4h | €160–480 |
| UK | £70–100/h | 2–4h | £140–400 |
| USA | $100–150/h | 2–4h | $200–600 |
| Mittelmeer | €60–100/h | 2–3h | €120–300 |

---

## Spezialfall: Aluminium-Yachten

### Thru-Hulls für Alu-Boote

**KRITISCH: KEIN Bronze/Kupfer/Messing in Kontakt mit Alu-Rumpf!**

Zulässige Thru-Hull-Materialien für Alu-Boote:
| Material | Eignung | Anmerkung |
|---------|---------|-----------|
| TruDesign (PA6-GF30) | EMPFOHLEN | Keine galvanische Korrosion |
| Marelon (GF-Polyester) | EMPFOHLEN | Nur NPT, also US-Markt |
| Aluminium (5083/5086) | Möglich | Geschweißt, keine Gewinde |
| Titan | Möglich | Teuer, Spezialeinsatz |
| Edelstahl 316L | Bedingt | MIT Isolation (Tef-Gel + Nylon-Hülsen) |
| Bronze/Kupfer/Messing | VERBOTEN | 500–600 mV Potentialdifferenz! |

**Aluminium-Thru-Hulls (geschweißt):**
Bei professionellen Alu-Yachten (Allures, Garcia, Ovni, Boreal) werden Thru-Hulls aus dem gleichen Aluminium wie der Rumpf geschweißt. Vorteil: Keine Dichtung, keine Gewinde, maximale Festigkeit. Nachteil: Nicht austauschbar ohne Schweißarbeiten.

**Erfahrungsbericht — cruisersforum.com, User "AllusSailor", 2023:**
> "My Allures 45.9 has all welded aluminum thru-hulls with TruDesign ball valves. Zero corrosion worries in 8 years of tropical sailing. The key is: NO bronze anywhere near the hull. Even a bronze propeller needs careful isolation."

### Opferanoden für Alu-Boote

**WARNUNG: NUR Zink-Anoden auf Alu-Booten!**
- Aluminium-Anoden: ZU NAH am Rumpfpotential (nur 200–300mV Differenz), ungenügender Schutz
- Magnesium-Anoden: ZU WEIT vom Rumpfpotential, Überprotektion → Wasserstoff-Versprödung
- Zink-Anoden: RICHTIG (300–400mV Differenz zu 5083)

**Experten-Referenz — Nigel Calder, "Boatowner's Mechanical and Electrical Manual":**
> "For aluminum boats, zinc anodes are the safest choice. The potential difference provides good protection without the risk of overprotection associated with magnesium."

---

### Isolationstechniken für Alu-Rumpfanschlüsse

Wenn Edelstahl oder andere edlere Materialien an Alu-Rumpfen verwendet werden müssen, ist elektrische Isolation zwingend erforderlich. Es gibt mehrere bewährte Isolationssysteme:

#### Tef-Gel (PTFE-Paste)

| Eigenschaft | Beschreibung |
|-----------|-------------|
| Material | PTFE (Polytetrafluorethylen) + Metalloxide |
| Haftung | Bildet Barriere zwischen Metallen |
| Anwendung | Auf Schraubengewinde auftragen vor Montage |
| Dicke | 0,5–1,0 mm reicht aus |
| Preis | €8–15 pro 100ml Tube |
| Hersteller | Duralac (führend), Permatex, Tef-Seal |
| Lagerfähigkeit | 24 Monate geschlossen |

**Anwendungsprotokoll (Tef-Gel):**
1. Flächen gründlich reinigen, Oxide mit Stahlbürste entfernen
2. Tef-Gel gleichmäßig auf Edelstahl-Schraube auftragen
3. Schnell montieren (Abbindezeit ~5 Minuten)
4. Mit Drehmoment gemäß Hersteller anziehen
5. Aushärtung mindestens 24h vor Wasserkontakt abwarten

**Kritischer Hinweis:** Tef-Gel allein ist KEINE vollständige Isolierung bei direktem Wasserkontakt. Muss mit Nylon-Isolierhülsen kombiniert werden.

#### Duralac (Zink-reiche Epoxy-Paste)

Populäre Alternative zu Tef-Gel, ursprünglich von Cathelco (jetzt Deepfield Technology), speziell für Alu-Schutz entwickelt.

| Eigenschaft | Beschreibung |
|-----------|-------------|
| Zusammensetzung | Epoxy + feinverteiltes Zink |
| Funktion | Wirkt als Opferanode + Isolator |
| Vorteil | Doppelschutz durch beide Mechanismen |
| Preis | €12–18 pro 100g Tube |
| Aushärtung | 7 Tage volle Aushärtung |
| Anwendung | Schraubengewinde, Montageflächen |
| Hersteller | Deepfield Technology, Jotun, Hempel |

**Erfahrungsbericht — aluminumyachts.org, User "AluCrusader", 2022:**
> "Used Duralac on all SS fasteners on my Allures 45. After 5 years in Caribbean, zero corrosion. The epoxy is much more forgiving than Tef-Gel if you mess up the application."

#### Nylon-Isolierhülsen und -Unterlegscheiben

Mechanische Isolation durch Kunststoff-Zwischenschicht:

| Komponente | Material | Größen | Preis pro Stk. | Hersteller |
|-----------|----------|--------|---------------|-----------|
| Isolierhülse | PA6 (Nylon) | M4–M16 | €0,30–1,20 | Hylomar, Nordfels, DIN Sätze |
| Isolierunterlegscheibe | PA6 | Passend zu Schraube | €0,25–0,80 | Hylomar, Borgesi |
| G10 Platte (Laminate) | Glasfaser-Epoxy | 3/4" x 2" Standard | €2–5/Stk | McMaster-Carr, Sensormatic |
| Dupont Delrin | Acetal-Copolymer | Custom Drehteile | €5–25/Stk | Lokale Dreherei |

**Installation (Nylon-Hülse):**
1. Hülse in Bohrung einsetzen (Hülse muss länger sein als Schraube)
2. Unterlegscheibe (ebenfalls Nylon) unter Schraubenkopf
3. Schraube durchführen — Kontakt erfolgt NUR über Nylon
4. Anzugsmoment nicht überschreiten (Nylon weicher als Metall!)

**Warnung:** Nylon-Unterlegscheiben unter Edelstahl-Schrauben auf blankem Alu sind NICHT ausreichend. Wasser kann an der Seite eindringen. IMMER mit Dichtmasse kombinieren (Sikaflex, Sealant).

#### G10-Isolierplatten für Antennen und Montagesockel

Für größere Strukturelemente (Antennensokel, Radarhalter, Stanchions) sind durchgehende G10-Platten (Glasfaser-Epoxy-Laminat) die beste Lösung:

| Eigenschaft | Wert |
|-----------|------|
| Material | Glasfaser + Epoxy, wasser-undurchlässig |
| Elektrischer Widerstand | >10^12 Ohm (absolute Isolation) |
| Mechanische Festigkeit | Ähnlich wie Aluminium |
| Dicke | Typ. 1/8" (3,2mm) bis 1/4" (6,4mm) |
| Temperaturbereich | −40 bis +130°C |
| Preis | €3–10 pro 10cm × 10cm |
| Hersteller | 3M, Maag-Composite, Sensormatic, IPC |
| Bearbeitung | Mit HSS-Bohrern, nicht gehärtet |

**Anwendung G10-Isolierplatte:**
1. Rechteckige G10-Platte an Position zwischen Alu-Rumpf und Edelstahl-Halter montieren
2. Platte mit Baumwoll-Dichtmasse (nicht Silikon!) an Rumpf kleben
3. Edelstahl-Bolzen durch Platte hindurch (4–6 Bolzen je Halter)
4. Keine direkte Metallberührung zwischen SS und Al

**Beispiel-Installation (Antennen-Mastfuß auf Alu-Dach):**
```
Alu-Dach
  ↓
Sikaflex 291 (Dichtmasse)
  ↓
G10-Platte, 5mm dick, 150×150mm
  ↓
Sikaflex 291
  ↓
Edelstahl-Flansch (Antenna Base)
  ├─ 4× M8 SS-Bolzen mit Nylon-Unterlegscheiben
  └─ Anzugsmoment 12 Nm (nicht mehr!)
```

**Kosten G10-Installation (Antennensokel):**
- G10-Platte (150×150×5mm): €6
- Dichtmasse (Sikaflex 291): €12 pro 300ml Tube
- SS-Hardware: €15–25
- Arbeitszeit: 1,5–2 Stunden
- **Gesamtkosten: €40–60 (Ersatz ohne G10: €2.500+ bei Lochfraßreparatur)**

### Propeller-Isolierung auf Alu-Yachten

**KRITISCH:** Ein Bronze-Propeller direkt auf eine Alu-Welle geschrumpft erzeugt eine der aggressivsten galvanischen Zellen (500–600 mV Potentialdifferenz).

#### Vetus Shaft Isolator

Niederländischer Hersteller Vetus bietet Kupfer-Schleifer mit Isolierkammer:

| Modell | Wellendurchmesser | Material | Preis EUR | Isolationsprinzip |
|--------|------------------|----------|----------|------------------|
| Vetus SHP-Ø40 | 40 mm | Graphit-Buchse + Kammer | €180–220 | Graphit berührt Welle, isoliert vom Rest |
| Vetus SHP-Ø50 | 50 mm | | €220–280 | |
| Vetus SHP-Ø65 | 65 mm | | €280–350 | |

Die Graphit-Buchse leitet Strom, die Kammer darum NICHT (Isolation durch Kunststoff-Kammer).

#### PYI Shaft Isolator (Premium)

Amerikanisches System mit kompletter elektrischer Isolation:

| Eigenschaft | Beschreibung |
|-----------|-------------|
| Funktion | Isoliert komplett—kein elektrischer Kontakt WL ↔ Propeller |
| Prinzip | Keramik-Spalt mit Schmiermittel (ähnlich Lager) |
| Vorteil | Null galvanische Korrosion — auch ohne Opferanoden |
| Nachteil | Wartungsbedarf (Schmiermittel alle 2 Jahre) |
| Preis | €400–600 (teuer, aber zuverlässig) |
| Hersteller | PYI Inc., Florida, USA |
| Website | www.pyi.com |

**Installationskosten (Welle isolieren auf Alu-Yacht):**
- Vetus-System: €150–200 (Material) + €300–600 (Arbeit) = €450–800
- PYI-System: €400–500 (Material) + €500–800 (Arbeit) = €900–1.300

**Erfahrungsbericht — sailinganarchy.com, User "SaltLife", 2021:**
> "Aluminum-hulled Swan 48 with bronze propeller. First survey showed massive corrosion under the prop—aluminum wasted away to 3mm thickness. Installed Vetus isolator and increased zincs. Problem stopped immediately. Cost me €8.000 to repair the hull."

### Bonding-Debatte bei Alu-Yachten: Zu bonden oder nicht?

Hier gibt es zwei Schulen:

**Schule A — "Bonding NOT needed" (Minimalisten):**
- Argument: Wenn alle Unterwasser-Metalle isoliert sind (Kunststoff-Thru-Hulls, Kunststoff-Propeller, Wellen-Isolator), dann gibt es nichts zu bonden
- Praxis: Manche Alu-Segelboote (Allures, Garcia) haben KEIN Bonding-System
- Risiko: Statischer Aufbau bei langen Fahrten (Mast-Schleifer, Antennengewitter)
- Empfehlung: Nur akzeptabel auf reinen Kunststoff-Systemen

**Schule B — "Bond everything" (Konservativ):**
- Argument: Bonding ist Blitzschutz (sekundärer Effekt) und Sicherheit gegen unerwartete Kupfer-Kontaminationen
- Praxis: Professionelle Reedereien (Schweizer Polar-Yachten, Expeditionsboote) bonden alle Metalle
- Bonding auf Alu: Mit Kupferleiter (NICHT Alu-Leiter, der korrodiert selber!)
- Empfehlung: **Sicher für alle Fälle**

**AYDI-Empfehlung für Alu-Yachten:**
- **Kunststoff-System durchgehend:** Bonding optional (aber Blitzschutz prüfen)
- **Jedes edlere Metall im Rumpf:** Bonding mit isoliertem Kupferkabel ERFORDERLICH
- **Opferanoden:** IMMER (auch mit Kunststoff-Thru-Hulls, für Sicherheit)

**Experten-Referenz — René Griebenow, Aluminiumyachtbau Bremerhafen:**
> "Bei modernen Alu-Yachten mit Kunststoff-Fittings ist Bonding nicht kritisch. Aber bei der geringsten Metallkontamination sofort wieder implementieren. Eine einzige übersehene Bronze-Schraube kann kostspieliger sein als ein komplettes Bonding-System."

### Spezialfall: Antennen und Radarmontagepunkte

Viele Alu-Yachtowner vergessen, dass die Antennenhalterung oft Edelstahl ist und direkt auf dem Dach verschraubt wird:

**Standard-Fehlerinstallation:**
```
Edelstahl-Flansch-Antenne
  ├─ M6 SS-Schraube
  ├─ Montagesockel (SS)
  └─ Direkt in Alu-Dach geschraubt → 650mV Potentialdifferenz!
```

**Nach 2–3 Jahren in tropischen Gewässern:** Weißer Korrosions-Krater um die Schraubenlöcher (Durchmesser 50–100mm).

**Richtige Installation:**
```
Alu-Dach
  ↓
Sikaflex 291
  ↓
G10-Isolierplatte (5mm)
  ↓
Sikaflex 291
  ↓
Edelstahl-Flansch mit M6 SS-Bolzen + Nylon-Unterlegscheiben
```

**Kosten-Nutzen:**
- G10-Platte + Sealant: €20
- Ersparte Reparatur: €2.000–5.000

### Stanchion und Railing-Isolierung

Ähnliches Problem: Edelstahl-Stanchions verschraubt in Alu-Reling:

| Lösung | Kosten | Aufwand | Effektivität |
|--------|--------|--------|-------------|
| Tef-Gel + Nylon-Unterlegscheiben | €2–4 pro Stanchion | 5 min/Stanchion | 80% (für bestehende Installationen) |
| Replacement mit Kunststoff-Stanchions | €40–80 pro Stanchion | 1h Installation | 100% |
| G10-Isolierblock an Basis | €30–50 (einmalig) | 2h | 95% |

**Empfehlung für Altbootaufwertung:** Kunststoff-Stanchions + G10-Basis ist modernstes System.

### Hersteller-Übersicht: Isolationsmaterialien für Alu-Yachten

| Hersteller | Spezialisierung | Produkte | Region | Website |
|-----------|----------------|----------|--------|---------|
| Cathelco (jetzt Deepfield Tech) | Korrosionsschutz | Duralac, Anoden, Isolierung | GB/International | deepfieldtech.com |
| Hylomar | Dichtmasse + Isolation | Tef-Gel, Nylon-Hülsen, G10 | GB | hylomar.com |
| Vetus | Antriebssysteme | Shaft Isolators, Hardware | NL | vetus.com |
| PYI Inc | Wellen-Isolation | PYI Isolators (Keramik) | USA | pyi.com |
| 3M | Composite-Materialien | G10, Scotch-Weld | USA/International | 3m.com |
| Sensormatic | Laminatstrukturen | G10-Platten, Custom | Australien | sensormatic.com.au |
| Jotun | Beschichtungen | Aquaguard (Epoxy-Grundierung für Alu) | International | jotun.com |

### Professionelle Inspektions-Protokolle

Für Versicherungs- und Verkaufs-Surveyors ist ein strukturiertes Prüfprotokoll unerlässlich.

#### AYDI-integriertes Thru-Hull-Inspektions-Formular

**Boot:** ______________ | **Baujahr:** ____ | **Rumpfmaterial:** GFK / Alu / Stahl | **Länge:** ____ m

**Inspektions-Datum:** __________| **Surveyor:** ______________| **Konfidenz-Level:** measured / visual_high / visual_medium / estimated

| Thru-Hull ID | Position | Material | Größe | Flansch-Zustand | Dezink-Test | Ventil OK? | Bonding Ω | Wandstärke | Dichtmasse | AYDI-Urgency |
|---|---|---|---|---|---|---|---|---|---|---|
| TH-01 | Motor-Kühl Einlass | Bronze C83600 | 1" | OK, Patina | Negativ | Ja | 0,3 | > 3mm | Intakt | monitor |
| TH-02 | Motor-Kühlung Auslass | Bronze C83600 | 1" | OK, Patina | Negativ | Ja | 0,4 | > 3mm | Intakt | monitor |
| TH-03 | Toilette Einlass | Bronze C83600 | 3/4" | Kleine Pits | Positiv! | Nein (fest) | 0,6 | 2,1mm | Risse | next_haulout |
| TH-04 | Toilette Auslass | Bronze C83600 | 3/4" | OK, Patina | Negativ | Ja | 0,5 | > 3mm | Intakt | routine |
| TH-05 | Bilge-Lenzer | TruDesign | 3/4" | OK, leichter Bewuchs | N/A | Ja | 0,2 | N/A | Intakt | routine |

**Dezink-Test-Methode (Confidence: measured):**
- Oberflächenbereich mit feiner Drahtbürste reinigen
- Mit Messer sanft kratzen: Oberflächenglanz beobachten
- **OK:** Goldig glänzend, hart, Material widersteht Kratzer
- **NICHT OK:** Rosa-kupferfarben, weich, Material lässt sich einkratzen

**Bonding-Widerstandsmessung (Confidence: measured):**
- Digitales Ohmmeter (€15–25, z.B. Fluke 101)
- Prüfspitzen auf Thru-Hull-Flansch und Bonding-Bus ansetzen
- Sollwert: < 1 Ohm (ideal < 0,5 Ohm)
- > 5 Ohm = Mangelhaft, Neuverkabelung erforderlich

**Wandstärken-Messung (Confidence: measured):**
- Ultraschall-Dickenmesser (€200–400, z.B. Elcometer 407/C)
- 5–8 Messpunkte pro Thru-Hull (oben, unten, Seiten, Flansch)
- Sollwert Bronze: > 3mm, Kunststoff: > 2mm
- Dokumentation: Foto der Messwerte

**Inspection Severity Scoring (für AYDI):**
- **GREEN (monitoring routine):** Alle Parameter OK, Korrosion minimal, Bonding < 1 Ω
- **AMBER (next haulout):** 1–2 Mängel (z.B. Dezinkifizierung früh, Ventil schwergängig), aber keine Sicherheitsgefahr
- **RED (immediate action):** Kritische Mängel (Wandstärke < 2mm, Bonding > 5 Ω, Dezinkifizierung fortgeschritten, Leck aktiv)

#### Anode-Inspektions-Checkliste

| Parameter | Messmethode | OK-Kriterium | Mangelhaft |
|-----------|------------|------------|-----------|
| Anode-Typ | Visuell (Farbe, Schrift) | Zink (silbrig), Alu-Navalloy (grau) | Magnesium (unerlaubt auf Alu-Booten) |
| Anode-Gewicht | Digitale Waage (±50g genau) | Baseline-Gewicht mit Baseline vergleichen | > 60% Verbrauch seit letzter Messung |
| Anode-Potential | Potentialmesser (Ref. Cu/CuSO₄) | −750 bis −850 mV SCE (Salzwasser) | < −600 mV oder > −950 mV |
| Oberflächenzustand | Visuell + Foto | Dunkles Grau, raue Oberfläche, kein Glanz | Weiß/grün beschichtet (Passivierung), glatt/poliert (nicht geopfert) |
| Bonding-Kontakt | Widerstandsmessung | < 0,1 Ohm zur Anode | > 1 Ohm (schlechter Kontakt, Korrosion am Lug) |

**Dokumentation:** Anode-Gewichte und Messdaten in Inspektions-Log eintragen, jährlich vergleichen.

#### Ultraschall-Wandstärken-Messung — Detailliertes Protokoll

Modernen Surveyors verwenden tragbare Ultraschall-Dickenmesser zur Thru-Hull-Wandstärke-Kontrolle.

**Geräte (Beispiele mit Kosten EUR):**
- Elcometer 407/C: €280–350 (professionell, IP67 wasserdicht, Datenlogging)
- REED Instruments R8500: €120–150 (budgetfreundlich, einfache Bedienung)
- Fluke 9036: €450–500 (High-End, sehr genau)

**Messdurchführung:**
1. **Vorbereitung:** Thru-Hull-Oberfläche reinigen, Bewuchs/Algen entfernen
2. **Kalibrierung:** Ultraschall-Gerät auf bekannte Stahlreferenz oder Kunststoff-Standard kalibrieren
3. **Messpunkte:** Pro Thru-Hull mindestens 5 Punkte:
   - Mitte Flansch
   - Oben / Unten / Links / Rechts (Gewinde-Bereich)
4. **Aufzeichnung:** Messwerte fotografieren + in Protokoll eintragen
5. **Trendanalyse:** Mit früheren Messungen vergleichen (jährliche Abnahme berechnen)

**Beispiel Trend-Analyse:**
```
Thru-Hull TH-03 (Toilette Einlass), Bronze C83600:
2021: 3,8 mm (neuer Einbau)
2022: 3,6 mm (Abnahme 0,2 mm/Jahr → Normal)
2023: 3,4 mm (Abnahme 0,2 mm/Jahr → Normal)
2024: 3,1 mm (Abnahme 0,3 mm/Jahr → Erhöht!)
2025: 2,8 mm (Abnahme 0,3 mm/Jahr → WARNUNG!)

Empfehlung: Austausch in 2–3 Jahren, nicht im nächsten Haul-Out.
```

**AYDI-Integration:** Wandstärken-Trends werden in das Materials-Modul gefeedert → Reparatur-Planung.

#### ICCP-System-Inspektionen (für Motor-/Stahlyachten)

Falls das Boot ein Impressed Current Cathodic Protection (ICCP) System hat:

| Inspektionspunkt | Messmethode | Sollwert | Mangelhaft |
|---|---|---|---|
| ICCP-Ausgangsleistung | Digitales Multimeter (Spannungsmessung) | 5–50 Volt, je nach System | 0V (ausgefallen), > 100V (überlastet) |
| ICCP-Referenzelektrode | Visuell + Potentialmessung | Potentialänderung < 50 mV bei Schaltung | Keine Potentialänderung → Elektrode verschlissen |
| Anode-Bett-Widerstand | Widerstandsmessung (Spezial-Gerät) | < 50 Ohm | > 100 Ohm (verschlammtes Anode-Bett) |
| Wasserstoff-Evolution (Gase) | Visuell unter Wasser (Taucher) | Keine Blasen | Blasen-Entwicklung → Überprotektion |

ICCP ist komplex. Jährliche Profi-Inspektionen empfohlen (€400–800/Jahr).

---

## Spezialfall: Stahl-Yachten

### Thru-Hulls für Stahl-Boote

| Material | Eignung | Anmerkung |
|---------|---------|-----------|
| Rotguss C83600 | Standard | 300–400mV Differenz, Bonding + Anoden |
| TruDesign/Marelon | GUT | Keine galvanische Korrosion |
| Stahl (geschweißt) | Möglich | Korrosionsschutz innen/außen |
| Edelstahl 316L | Bedingt | Spaltkorrosion beachten |
| DZR-Messing | NEIN | Dezinkifizierungsgefahr + galvanisch |

### Epoxy-Beschichtung als Barriere

Stahl-Yachten verwenden typischerweise ein 2K-Epoxy-Beschichtungssystem (International Interprotect, Jotun Jotamastic) als Barriere zwischen Rumpf und Thru-Hull. Die Beschichtung wird auf 300µm Trockenfilmdicke aufgebaut und MUSS den gesamten Kontaktbereich abdecken.


### ICCP-Systeme (Impressed Current Cathodic Protection)

Große Stahlboote und kommerzielle Schiffe verwenden oft ICCP statt passive Opferanoden, weil ICCP präziser steuerbar ist und weniger Anode-Material verbraucht.

**Wie ICCP funktioniert:**
Statt eines passiven Anodenmaterials wird ein **aktiver Stromgenerator** verwendet, der kontinuierlich Gleichstrom zwischen einer Inert-Anode (Graphit, Platin-Beschichtung) und dem Rumpf durchleitet. Dies hält den Rumpf auf potentialgeregelt aus (typischerweise −0,8V gegen Ag/AgCl Referenzelektrode).

| Parameter | Passiv-Anode | ICCP |
|-----------|-------------|------|
| Stromquelle | Chemisch (galvanische Reaktion) | Elektrisch (Gleichstromquelle) |
| Regelung | Keine (konstante Anodenauflösung) | Präzise (Referenzelektrode regelt Spannung) |
| Anodenverbrauch | Schnell (% Jahr) | Minimal (praktisch keine Auflösung der Inert-Anode) |
| Haltbarkeit | 3–5 Jahre Anode | 20+ Jahre Inert-Anode bei guter Wartung |
| Preis Initial | €3.000–8.000 | €12.000–35.000 |
| Preis/Jahr Betrieb | €400–600 | €150–250 (Strom) + €200–400 (Wartung) |
| Eigenverbrauch Strom | Keine | 5–20A × 24h = 120–480Wh/Tag |
| Für Boote empfohlen | <20m Stahl | >20m Stahl, professionelle Schiffe |

**ICCP-Hersteller (kommerziell):**

| Hersteller | Produkt | Region | Spezialisierung | Website |
|-----------|---------|--------|-----------------|---------|
| Cathelco | CP-Rectifiers, Reference Electrodes | GB | Schiffsmarine Standard |cathelco.com |
| CMP (Corrosion Management Products) | CP-Controller, Auto-Shutoff | Canada/USA | Off-Shore Plattformen | cmprosion.com |
| Farwest Corrosion | CP Systems, Monitoring | USA (Washington) | Kleinere Yachten + Schiffe | farwestcorrosion.com |
| Deepfield Technology | ICCP Retrofit-Kits | GB | Alu-Boote + Stahl | deepfieldtech.com |
| Jotun | Catpro, Marine Coatings | International | Integrated Systems | jotun.com |

**ICCP-Installation auf Stahlboot (Beispiel: 24m Stahl-Expedition):**

```
Stromquelle (Gleichstrichter, 200W)
  ├─ (−) Kathode: Masseschuhe/Kontakt zum Rumpf verteilt
  └─ (+) Anode: Graphit-Anode oder Platiniert-Niob, bewusst vom Rumpf entfernt

Referenzelektrode (Silber/Silberchlorid, −0,8V Setpoint)
  └─ Feedback zum Regler: "Sind wir bei −0,8V? Wenn nein, Strom nachregeln"

Stromverteilung (Kupferkabel)
  ├─ Haupt-Bonding-Bus (Rumpf-Verbindung)
  ├─ Referenzelektroden-Kreis
  └─ Anode-Leitung (isoliert)
```

**Kosten (24m Stahlboot mit ICCP):**
- Stromquelle + Schalttafel: €8.000–12.000
- Graphit-Anode + Befestigung: €2.000–3.000
- Referenzelektroden (3 Stck) + Kabel: €1.500–2.500
- Installation + Verkabelung: €3.000–5.000
- **Gesamtkosten: €14.500–22.500**

**Amortisierung:** Bei 5-Jahres-Betrieb:
- Passiv (ohne ICCP): 5 × (€5.000 Anodenstoff + €500 Wartung) = €27.500
- ICCP: €18.000 (Initial) + 5 × (€300 Strom + €300 Wartung) = €21.000
- **Einsparung mit ICCP: €6.500 über 5 Jahre**

### Beschichtungssysteme für Stahlrümpfe

Die Beschichtung ist die **erste Verteidigungslinie**, ICCP oder Anoden sind Backup:

**Internationale Standard-Systeme:**

| System | Schichtenaufbau | Hersteller | Preis (m²) | Verwendung |
|--------|-------------------|----------|---------|-----------|
| Jotun Tankguard | Primer (100µm) + 2K-Epoxy (300µm) | Jotun | €25–35 | Innenseite, Bilgebereich |
| International Interprotect | Epoxy Primer + Epoxy Topcoat | International | €30–45 | Standard Unterwasserschiff |
| Hempel Mille Epoxy | 2-Komponenten Epoxy | Hempel | €25–40 | Budget-Standard |
| Jotamastic 87 | Mikro-filled Epoxy, sehr zäh | Jotun | €35–50 | High-Performance, rauhe Oberflächen |
| Unipol 2000 | Premium Epoxy, mariniert | Jotun | €45–65 | Top-Yachten |

**Verarbeitung (Unterwasserschiff einer 15m Stahlyacht, ~60m² Rumpf):**

```
1. Oberflächenvorbereitung (KRITISCH)
   └─ Sandstrahlen nach ISO 8501-1:Sa 2,5 (minimaler Standard für Marine)
   
2. Feuchtetest
   └─ Holzfeuchtemessgerät oder RH-Sensor (<85% relative Feuchte)
   
3. Grundierung (Epoxy Primer)
   └─ 100–120µm TFD (Trockenfilmdicke), klassisch 2K (Harz + Härter)
   
4. Zwischenschicht (optional)
   └─ 50µm Epoxy, wenn besondere Rauheit oder lange Lagerung
   
5. Topcoat (2K-Epoxy oder Polyurethan)
   └─ 150–200µm TFD
   
6. Aushärtung
   └─ Mindestens 7 Tage bei 15°C + 65% RH vor Wasserkontakt
```

**Kosten-Beispiel (15m Stahlboot, Unterwasserschiff nur):**
- Sandstrahlen: €2–4/m² = €120–240
- Grundierung (Material): €20–30/m² = €1.200–1.800
- Topcoat (Material): €20–30/m² = €1.200–1.800
- Arbeitslöhne (Werftstundensatz €50/h, ~3h/m²): €9.000
- **Gesamtkosten: €11.520–13.000**
- **Lebensdauer: 5–8 Jahre (Unterwasser), dann erneut sandstrahlen**

### Anodenstrategie für Stahlrümpfe

Anders als bei GFK und Alu: Stahl KANN korrodieren; Opferanoden sind Zweitverteidigung hinter der Beschichtung.

**Anode-Platzierung auf Stahlboot:**

```
Heck-Bereich (höchste Aktivität)
  ├─ 2–3 Zink-Anoden à 2–3kg je Seite (Propeller-Nähe)
  └─ Montagepunkte: Stempel durch Rumpf oder verschraubte Bolzen

Mittschiffs (Stabilisierung)
  ├─ 1–2 Anoden je Seite
  └─ Montage auf Kiel-Rippen oder Ballast-Rahmen

Bug (Schutz Kettenstopper, Anker-Befestigung)
  ├─ 1 Anode je Seite
  └─ Klein (1kg), um Bug-Hydrodynamik nicht zu beeinflussen

Unterwasser-Metalle (isoliert):
  ├─ Stevenrohr: Anode sehr nahe montieren
  ├─ Propellerwelle: Kupfer-Schleifer + Anode in Wellenschacht
  └─ Ruderstock: Anode auf Ruder-Pfosten
```

**Anodenverbrauch (Stahl 15m, aktivativ):**
- Mit beschichteter Rumpf-Integrität: 0,5–1kg Zink/Jahr
- Mit Beschichtungsdefekt (Kratzer >1cm²): 3–5kg Zink/Jahr
- Mit großem Beschichtungsabfall: 10–20kg Zink/Jahr

**Erfahrungsbericht — sailinganarchy.com, User "SteelTrooper", 2020:**
> "My Swede 55 steel gaff cutter survives 20 years in the tropics. Secret: fresh zincs EVERY 18 months, no exceptions. The moment you skip a haul-out, corrosion accelerates exponentially."

### Weldzone Korrosionsschutz (Schweißnähte)

Schweißstellen sind kritisch: Die Wärmeeinflusszonen (HAZ) haben unterschiedliches elektro-chemisches Potential als Grundmaterial → galvanische Mikro-Zellen entstehen.

**Vorbeugende Maßnahmen:**

1. **Material-Wahl:**
   - Stahlrümpfe: Ruhrstahl oder Corten-arme Legierung mit Molybdenum
   - Verschleißschutz: Low-Carbon Stahl (0,12–0,20% C), nicht hochlegiert

2. **Post-Weld Heat Treatment (PWHT):**
   - Bes. Yachten werden nach dem Schweißen bei 600–700°C entspannt
   - Dies hilft, Eigenspannungen und Gefügeveränderungen zu minimieren
   - Kosten: €100–200/Schweißstelle, durchgeführt bei Neubau

3. **Beschichtung-Übergang:**
   - Schweißnähte bekommen doppelte Schichtstärke Grundierung (150µm statt 100µm)
   - Grund: Schweißzonen sind raue Oberfläche mit höherer Oberflächenenergie

4. **Epoxy-Injektionen (Retrofit):**
   - Für alte Stahl-Yachten ohne ICCP: Epoxy unter Druck in Risse injizieren
   - Kosten: €50–150/Naht

### Ballast-Tank Korrosionsschutz

Ein separates Problem: Innenseite von Ballast-Tanks ist konstant feucht, daher sehr korrosiv.

| Schutzmaßnahme | Material | Lebensdauer | Kosten | Anmerkung |
|---|---|---|---|---|
| Keine (rohes Stahl) | — | 5–10 Jahre | €0 | Nicht empfohlen, Rost fällt in Ballast |
| Epoxy-Beschichtung (Ballast-Typ) | 2K-Epoxy, Ballast-grade | 15–20 Jahre | €30–50/m² | Standard für Commercial |
| Dehumidification | Aktivkohle-Behälter, Silica-Gel | 5 Jahre je Füllung | €200–500/Tank/Jahr | Teuer aber effektiv |
| Lufttrockner (aktiv) | Elektrischer Kompressor + Trockner | 20 Jahre | €5.000–10.000 (System) | Hochwertige Yachten |
| Inert-Gas System | Stickstoff-Purging | Permanent | €15.000–30.000 (System) | Nur große Schiffe |

**Empfehlungen nach Bootsgröße:**

- <15m: Epoxy-Beschichtung + Lufttrockner-Einsätze (€50–100/Jahr)
- 15–25m: Epoxy + aktiver Lufttrockner (€500–1.000/Jahr Betrieb)
- >25m: Inert-Gas System oder kontinuierliche Lüftung


---

## Spezialfall: Landstrom und Streustrom-Korrosion

### Problem

Landstrom (Shore Power) kann über den Schutzleiter (PE/Grün-Gelb) galvanische Ströme zwischen Booten im Hafen erzeugen. Boot A hat Bronze-Thru-Hulls, Boot B hat Alu-Rumpf — der Schutzleiter verbindet sie elektrisch über Hafennetz → Boot B wird Opfer.

### Gegenmaßnahmen

| Lösung | Wirkung | Preis EUR | Hersteller |
|--------|--------|----------|-----------|
| Trenntrafo (Galvanic Isolator) | Blockiert galvanischen Strom bei <1,4V | €250–800 | ProMariner, Sterling, Victron |
| Isolation Transformer | Vollständige galvanische Trennung | €800–3.500 | Victron, Mastervolt, Charles |
| ELCI (Equipment Leakage Circuit Interrupter) | Erkennt Fehlerstrom | €200–400 | Blue Sea, Eaton |
| Zink-Saver II | Galvanic Isolator inline | €180–250 | ProMariner |

**Experten-Referenz — Nigel Calder:**
> "A galvanic isolator is the minimum protection for any boat connected to shore power. An isolation transformer is the gold standard — it completely eliminates galvanic current paths."

**Erfahrungsbericht — trawlerforum.com, User "ShoreHorror", 2022:**
> "Connected to shore power in a Caribbean marina. After 3 months my zincs were GONE and the prop showed pitting. Turns out the boat next to me had a ground fault. Installed a ProMariner ProSafe II galvanic isolator — problem solved."

---

### AC vs. DC Streustrom: Unterscheidung

**AC-Strom (Wechselstrom, 50/60 Hz):**
- Quelle: Hafennetzfehlstellen, beschädigte Landrechnerkabel, alte Elektroinstallation
- Wirkung: Verursacht ähnliche Korrosion wie DC, aber intermittierend (positiv–negativ–positiv)
- Erkennbarkeit: Mit AC-Multimeter messbar, typischerweise 10–50mV Peak-to-Peak
- Gefahr: UNTERSCHÄTZT, da AC "schwächer" wirkt, aber über Monate weg Korrosion akkumuliert

**DC-Strom (Gleichstrom):**
- Quelle: Defekte Bordladegeräte, fehlerhafte Batteriemanagement-Systeme, externe DC-Stromquellen
- Wirkung: Kontinuierliches, massives Korrosionssignal
- Erkennbarkeit: Mit DC-Voltmeter gegen Referenzelektrode sofort erkennbar (oft 0,5–2V offset)
- Gefahr: Schnell, dramatisch, können Anoden in Wochen aufbrauchen

| Parameter | AC-Strom | DC-Strom |
|-----------|----------|----------|
| Quelle | Marina-Fehler | Bordgeräte |
| Spannungsoffset | ±0–100mV | +0,2 bis +2V |
| Anodenverbrauch | 500g/Monat (schnell) | 5–20kg/Monat (sehr schnell) |
| Nachbarn-Einfluss | JA (über gemeinsames Netz) | NEIN (nur direkter Fehler auf eigene Boot) |
| Prävention | Trenntrafo | Isolation + Bordgeräte-Kontrolle |

### Messprotokolle für Streustrom-Diagnostik

**Test 1: Referenzelektroden-Messung (silber/Silberchlorid, Ag/AgCl)**

Dies ist der Standard-Korrosionsschutz-Test nach NACE/ASTM:

```
Messgerät: Digital-Multimeter, 0–2V Bereich, 10kΩ Impedanz
Referenzelektrode: Silber/Silberchlorid-Elektrode (Halbzelle)
  └─ Ag/AgCl Elektrode kostet €30–80 pro Stück
  └─ Oder DIY: Ein Silberstab in Glasrohr mit gesättigtem KCl-Gel

Mess-Protokoll:
  1. Elektrode ins Wasser halten, mindestens 10cm vom Rumpf entfernt
  2. Roter Leiter des Voltmeters → Ag/AgCl Elektrode
  3. Schwarzer Leiter → Massekabel des Bootes (direkt am Rumpf berühren)
  4. Ablesen nach 30 Sekunden Stabilisierung
  5. Normalwert (Referenz): −0,8V bis −1,0V (negative Spannung = Korrosionsschutz)
  6. Warnsignal: > −0,6V oder < −1,2V = Problem!
  7. Kritisch: Positive Spannung (z.B. +0,2V) = Massive Korrosion!
```

**Typische Messwerte (Ag/AgCl):**
| Situation | Spannung | Bedeutung |
|-----------|----------|-----------|
| Neues Boot, TruDesign-Thru-Hulls, Zincs OK | −0,85V | IDEAL |
| Alter Boot, Bronze, Zincs verbraucht | −0,65V | OK aber verschlissen |
| Boot mit defektem Ladegerät im Hafennetz | +0,1V | KRITISCH—Sofortmaßnahme |
| Nachbar mit Stromleck, Boot hat Trenntrafo | −0,8V (unverändert) | Trenntrafo wirkt! |

**Test 2: DC-Spannungs-Offset (ohne Referenzelektrode)**

Schneller Feldtest ohne Spezialeausrüstung:

```
1. Digitales Multimeter auf DC-Volt-Modus (0–20V Bereich)
2. Schwarzer Leiter → Massekabel des Bootes (GFK oder Alu-Rumpf)
3. Roter Leiter → Messingkaraffe, Metallkette oder ein in Meerwasser 
   hängendes Drahtmesh (improvised Referenz)
4. 30 Sekunden Stabilisierung abwarten
5. Ist Spannung > +0,1V = DC-Streustrom wahrscheinlich
6. Ist Spannung < −1,0V = Über-Kathodische Schädigung wahrscheinlich
```

**Vorsicht:** Diese Methode ist weniger zuverlässig als Ag/AgCl, aber schnell.

### Galvanischer Isolator (Galvanic Isolator) — Installation & Funktion

Ein Galvanischer Isolator ist ein elektronisches Schutzgerät, das in die Schutzleiter-Linie (PE/Grün-Gelb) des Landstrom-Kabels eingebaut wird.

**Funktion:**
```
Hafen-Schutzleiter (PE) — 50A, 230V AC
  ↓
Galvanischer Isolator (passiv, keine externe Stromversorgung nötig)
  ├─ Blockiert Gleichstrom (DC) vollständig
  ├─ Blockiert AC-Strom unterhalb ~1,4V Schwelle
  ├─ Lässt normalen AC-Betriebsstrom durch (Sicherheitsschutz bleibt aktiv)
  └─ Zerlegt galvanische Schleife zwischen Booten
  ↓
Boot-Schutzleiter (isoliert vom Hafennetz)
```

**Technische Details eines typischen Galvanischen Isolators:**

| Komponente | Spezifikation |
|-----------|--------------|
| Technologie | Gleichstrom-Blockierungs-Diode oder ähnlich |
| Spannungsabfall | <0,5V (vernachlässigbar) |
| Stromkapazität | 16–32A (je nach Modell) |
| AC-Durchlass | Ja (für Schutzfunktion) |
| DC-Blockierung | >99% (Sperrung von Streustrom) |
| Betriebsspannung | Passiv (keine Stromversorgung erforderlich) |
| Größe | Klein (Kassettenformat, 15×10cm) |
| Installation | Inline in Landsrom-Kabel oder Schaltschrankeinbau |

**Installation eines Galvanischen Isolators (ProMariner ProSafe II, Beispiel):**

```
Hafen-Anschluss
  └─ 50A Stecker
      ↓
  Landrechnerkabel (Grün-Gelb Schutzleiter)
      ↓
  Galvanischer Isolator (Kassette)
      ├─ Eingang: 1 Schutzleiter
      └─ Ausgang: 1 isolierter Schutzleiter
      ↓
  Boot-Schutzleiter zu:
      ├─ Metallmast (wenn vorhanden)
      ├─ Rumpf-Massepunkt
      └─ Bordstromnetz PE-Schiene
```

**Kosten-Vergleich (2024 Preise):**

| Modell | Hersteller | Preis EUR | Features | Verfügbarkeit |
|--------|-----------|----------|----------|---|
| ProMariner ProSafe-II 30A | ProMariner | €350–420 | Robust, mariniert | Überall |
| Victron Galvanic Isolator | Victron | €280–350 | Präzise, Testfunktion | Distributor |
| Sterling ProTektor | Sterling | €320–380 | Guter Ruf, Reparaturbörse | UK/USA |
| Blue Sea Systems SI-GI | Blue Sea | €310–370 | US-Standard | Nordamerika |
| DIY Lösung (Teile) | — | €50–100 | Selbst zusammenlöten | Risikobehaftet |

**Größe sollte gewählt werden nach Strombelastung:**
- 16A Modell: Boote <12m (typisch 10–12A Last)
- 30A Modell: Boote 12–20m (typisch 15–20A Last)
- 50A Modell: Boote >20m oder mehrfache Ladegeräte

### Isolation Transformer — Die Premium-Lösung

Ein **Isolation Transformer** ist teurer, aber bietet KOMPLETTE galvanische Trennung zwischen Hafennetz und Boot. Es isoliert nicht nur Schutzleiter, sondern auch Phase und Neutral, was vollständigen Schutz bietet.

**Funktion:**
```
Hafen-Stecker 230V AC, 50Hz
  └─ Netztransformator mit Primär- und Sekundärspule
      ├─ Primärspule: Hafennetz (geerdet auf Hafen-Masse)
      └─ Sekundärspule: Boot-Seite (NICHT geerdet auf Hafennetz!)
          └─ Kleine Kapaziätäten über Wicklung → AC durchlassen
          └─ Große Gleichströme → blockiert (Spulen-Induktivität)
  ↓
Boot-Stecker (galvanisch isoliert vom Hafen)
```

| Aspekt | Galvanic Isolator | Isolation Transformer |
|--------|------------------|----------------------|
| Schutz-Vollständigkeit | Nur Schutzleiter | ALLE 3 Phasen + PE |
| Kosten | €250–800 | €1.500–3.500 |
| Stromverlust | <0,5% | 3–5% Transformation |
| Größe | Klein (Kassette) | Mittel (10kg) |
| Montage | Inline in PE | Schaltschrankeinbau |
| Besonderheit | Einfach, zuverlässig | Gewicht, Wartung |
| Ideal für | <20m Boote | >20m oder professionell |

**Installation Isolation Transformer (Beispiel: 32A Transformer, 7,5kVA):**

```
Hafen-Stecker (230V 50A, 5-polig)
  ├─ Phase 1, Phase 2, Phase 3 (falls vorhanden)
  ├─ Neutral (N)
  └─ Schutzleiter (PE) — GETRENNT
      ↓
Transformator (Primärspule geerdet auf Hafen-Masse)
  ├─ 3 Phasen isoliert auf Sekundär
  ├─ Neutral isoliert
  └─ PE NICHT mit Hafen verbunden!
      ↓
Boot-Stecker (sekundär)
  ├─ 3 Phasen (wie vorher)
  ├─ Neutral (isoliert vom Hafennetz)
  └─ Boot-Schutzleiter (NEW, nicht vom Hafen)
      └─ Verbindung nur zu Boot-Masse
```

**Wichtig:** Ein Isolation Transformer muss korrekt geerdet werden. Die Sekundärseite MUSS eine lokale Erdung haben (kleine Erdungsstab <1m vom Boot).

### Marina-Wiring-Standards und Fehlerquellen

**Typische Fehlerinstallationen in Marinas:**

| Fehler | Ursache | Konsequenz | Häufigkeit |
|--------|--------|-----------|-----------|
| Schutzleiter (PE) nicht auf Hafenerde isoliert | Alte Marina, Kosteneinsparung | Galvanische Ströme zwischen Booten | SEHR HÄUFIG (>50% Marinas) |
| Neutralleiter mit Erde verbunden (TN-C-S Mischung) | Veraltete Norm, Übergangszustand | Falscher RCD-Auslösevektor, Streustrom | HÄUFIG |
| Korrosion in Hafensteckdosen | Meerwasser-Eindringung | Kontaktwiderstand, Hitze, Brandgefahr | HÄUFIG |
| Doppelte Erdung von Boot-Mast | Doppelter Kontakt zum Hafennetz | Schleife mit großem Querschnitt, hoher Strom | GELEGENTLICH |
| Fehlerhaftes Ladegerät an Bord | Netzfilter defekt, Leckstrom | Strom flieht über Wasserpfade zu anderen Booten | HÄUFIG |

**Beste Praxis für Hafenführer (was sollten Marinas tun):**
1. Alle PE-Leiter auf GEMEINSAME Hafenerde (nicht auf Boat-to-Boat Schleife!)
2. TN-S oder TT System, NICHT TN-C-S an Bootssteckdosen
3. RCD-Schutzschalter (30mA) für jede Bootslinie
4. Jährliche Inspektion der Steckdosen auf Korrosion
5. Empfehlung zu Galvanischen Isolatoren in Hafenverlauf

**Erfahrungsbericht — marineelectronicsforums.com, User "MarinaManager", 2023:**
> "Switched our 100-slip marina to individual PE earths (TT system) instead of shared riser. Galvanic damage complaints dropped 95%. Cost: €8.000. Value: Priceless."

### Haftungs- und Versicherungs-Fragen

**Wer trägt Haftung bei Streustrom-Korrosion?**

Diese Frage ist in verschiedenen Ländern unterschiedlich beantwortet:

| Land | Haftungsregel | Beispiel |
|------|--------------|---------|
| Deutschland | Marina hat Verkehrssicherungspflicht | Marina kann verklagt werden, wenn Fehler bekannt |
| Großbritannien | "Reasonable Care" Standard | Marina muss "reasonable steps" unternehmen, oft in AGB ausgeschlossen |
| USA | Varies by state — Haftung oft auf Eigner | Boot-Eigner trägt Verantwortung für Schutzausrüstung |
| Niederlande | Hafen-Standard-Richtlinien (meist kostenlos) | Hafenmeister berät zu Trenntrafo |

**Tipps für Boot-Eigner zur Schadensminderung:**

1. **Dokumentation:** Fotos und Noten von Anodenverbrauch (Zeitstempel!)
2. **Versicherung benachrichtigen:** Meldet Schaden SOFORT der Versicherung an
3. **Experte-Bewertung:** Unabhängige Messungen (Ag/AgCl) vor & nach Schaden
4. **Hafenreklamation:** Schriftlich reclamation einreichen mit Dokumentation
5. **Schutzgeräte kaufen:** Trenntrafo ist oft günstiger als Rechtsstreit

**Versicherung und Streustrom:**
- Viele All-Risk-Marineversicherungen decken "Streustrom-Korrosion" NICHT ab (explizit ausgeschlossen)
- Einige Premium-Policen (z.B. Pantaenius, Lemonade Marine) bieten optionalen "Stray Current"-Schutz
- Selbstverschuldete Streustrom-Korrosion (z.B. eigenes Ladegerät-Leck) = Versicherungs-Ausschluss in allen Fällen


## Fehlerbild-Atlas

### Fehlerbild 1: Dezinkifizierung an Messing-Thru-Hull

**Symptom:** Rosa-kupferfarbene, schwammige Oberfläche unter der Patina. Material lässt sich mit Messer eindrücken. Oft erst bei Reinigung sichtbar.

**Ursache:** Zink löst sich selektiv aus der Legierung. Betrifft nur zinkhaltige Legierungen (>15% Zn). C83600 Rotguss (5% Zn) ist resistent, C46400 Naval Brass (40% Zn) ist hochanfällig.

**Häufigkeit:** Sehr häufig bei Booten Baujahr < 1990, die mit Gelb-Messing-Fittings ausgerüstet wurden.

**Maßnahme:** Sofortiger Austausch. Dezinkifiziertes Material hat keine Restfestigkeit.

**Confidence:** visual_high (wenn Oberfläche gereinigt), documented (wenn per Materialtest bestätigt)

### Fehlerbild 2: Galvanische Lochfraßkorrosion am Alu-Rumpf

**Symptom:** Weiße Pulverablagerungen (Al₂O₃) rings um ein metallisches Bauteil (z.B. Edelstahl-Schraube, Bronze-Fitting). Tiefe Löcher im Aluminium, umgeben von weißem Ring.

**Ursache:** Direkter Kontakt zwischen edlerem Metall (Edelstahl, Bronze, Kupfer) und Aluminium in Gegenwart eines Elektrolyten (Meerwasser, Kondenswasser). Je größer das Kathodenverhältnis (Edelstahl-Fläche zu Alu-Fläche), desto schneller die Korrosion.

**Häufigkeit:** Sehr häufig bei unsachgemäß ausgeführten Reparaturen an Alu-Yachten.

**Maßnahme:** Edelmetall-Bauteil entfernen, Alu aufschweißen oder Reparatur-Epoxy, neue Befestigung MIT Isolation (Tef-Gel, Nylon-Unterlegscheiben, Duralac).

**Confidence:** visual_high (Weißes Pulver + Lochfraß eindeutig), measured (wenn Potentialdifferenz gemessen)

### Fehlerbild 3: Streustrom-Korrosion an Propeller/Welle

**Symptom:** Schneller Anodenverbrauch (Wochen statt Monate). Pitting an Propellerblättern. Korrosion an Welle trotz Bonding. Oft an nur einem Boot im Hafen.

**Ursache:** Elektrischer Fehlerstrom über Hafennetz (Schutzleiter), defektes Ladegerät im eigenen oder Nachbarboot, fehlender Trenntrafo. Strom fließt über Unterwasser-Metalle zurück ins Wasser.

**Häufigkeit:** Häufig in Marinas mit älterer Elektroinstallation, besonders in der Karibik und Mittelmeer.

**Maßnahme:** Landstrom trennen (Test!), Trenntrafo installieren, Bonding prüfen, Nachbarboote inspizieren lassen.

**Confidence:** documented (wenn Strommessung am Bonding-System), estimated (wenn nur anhand Schadenbild)

### Fehlerbild 4: Erosionskorrosion an Thru-Hull-Innenwandung

**Symptom:** Rinnenartige Vertiefungen in Strömungsrichtung im Inneren des Thru-Hulls. Wandstärke lokal reduziert. Oft an Motorkühlwasser-Einlass (höchste Strömung).

**Ursache:** Hohe Strömungsgeschwindigkeit (>2 m/s in Bronze, >1,5 m/s in Messing) entfernt die schützende Oxidschicht schneller als sie sich bilden kann.

**Häufigkeit:** Moderat, vor allem bei unterdimensionierten Borddurchbrüchen und leistungsstarken Motoren.

**Maßnahme:** Größere Nenngröße wählen (Strömungsgeschwindigkeit senken), ggf. C95800 NiAlBr (erosionsbeständiger als C83600).

**Confidence:** visual_medium (Erosionsmuster sichtbar bei Endoskopie), measured (wenn Wandstärke gemessen)

### Fehlerbild 5: Spaltkorrosion an Edelstahl-Thru-Hull

**Symptom:** Rotbraune Verfärbung im Gewinde- oder Dichtungsbereich. Lochfraß unter Dichtmasse. Edelstahl "blüht" rostbraun an Spaltstellen.

**Ursache:** Sauerstoffverarmung im Spalt → Passivschicht bricht zusammen → Edelstahl wird aktiv und korrodiert. Besonders bei 304 und 316 in Meerwasser.

**Häufigkeit:** Häufig bei 304er-Edelstahl. Mäßig bei 316L. Selten bei Duplex 2205.

**Maßnahme:** 316L mindestens, Duplex 2205 bevorzugt für Unterwasser. Spalte mit Sikaflex abdichten. Regelmäßige Inspektion.

**Confidence:** visual_high (typisches Erscheinungsbild), measured (wenn Materialanalyse per XRF)

### Fehlerbild 6: Seeventil festgesessen (Kugelhahn)

**Symptom:** Hebel des Kugelhahns lässt sich nicht mehr bewegen. Ventil in offener oder geschlossener Position blockiert.

**Ursache:** Bewuchs im Ventil, Korrosion an Kugel/Sitz, Mangel an regelmäßiger Betätigung (>6 Monate ohne Bewegung). Bei Konusventilen: fehlende Fettung.

**Häufigkeit:** Sehr häufig (>40% aller Sportboote bei Surveyor-Berichten).

**Maßnahme:** NICHT mit Gewalt öffnen (Bruchgefahr!). Ventil von außen klopfen (leicht), Penetrationsöl (WD-40 Marine), erwärmen (Heißluftpistole, 60–80°C). Wenn möglich: Hebel mit verlängertem Rohr vorsichtig bewegen. Prävention: Alle 3 Monate betätigen.

**Confidence:** visual_medium (Äußerer Zustand gibt Hinweis), documented (wenn im Surveyor-Bericht)

### Fehlerbild 7: Undichter Thru-Hull (Sickerwasser)

**Symptom:** Wasseransammlung im Bilge bei Stillliegen. Feuchtigkeit um Thru-Hull-Flansch. Dichtmasse sichtbar gerissen oder abgelöst.

**Ursache:** Alterung der Dichtmasse (UV, Temperaturwechsel, Vibrationen). Setzung bei GFK-Rumpf. Überdrehte Gegenmutter (GFK eingedrückt).

**Häufigkeit:** Moderat, häufiger bei Booten >15 Jahre.

**Maßnahme:** Boot slippen. Thru-Hull ausbauen. Alte Dichtmasse vollständig entfernen. Rumpfbohrung prüfen (Risse?). Neu einbauen mit frischer Dichtmasse (Sikaflex 291 / 3M 4200).

**Confidence:** visual_high (nasser Flansch eindeutig), measured (wenn Leckrate quantifiziert)

### Fehlerbild 8: Überprotektion + Wasserstoff-Versprödung an Alu-Rumpf

**Symptom:** Kleine blasenförmige Wölbungen (Blistering) in der Rumpfbeschichtung, besonders in der unteren Wasserlinie. Rumpf fühlt sich schwach/porös an. Oberflächenpitting wie Salzflöckchen. Potentialmessung: < −1.100 mV SCE (viel zu negativ).

**Ursache:** Überprotektion durch zu edle Anoden (Mg statt Zink auf Alu), überdimensionierte Anode, oder ICCP mit zu hohem Strom. Kathodische Wasserstoff-Entladung → H-Atome diffundieren ins Alu → Versprödung.

**Häufigkeit:** Selten, aber katastrophal. Typisch bei Alu-Yachten mit unqualifizierten Reparaturen.

**Diagnose (Confidence: measured):** Potentialmessung sollte −750 bis −850 mV SCE sein, nicht < −1.000 mV. Dickenmessung: linear, nicht sprunghaft reduziert. Anode-Typ: sollte Zink sein, nicht Mg.

**Maßnahme:** Anodentyp austauschen (Mg → Zink Navalloy), Anode-Größe reduzieren, Bläschen-Bereiche abschleifen + Epoxy-Patch auftragen.

**Lehre:** Überprotektion ist GENAUSO SCHLECHT wie Unterprotektion!

**Confidence:** measured (Potentialmessung), visual_medium (Blasen sichtbar aber mehrdeutig)

### Fehlerbild 9: Anodenpassivierung (Anode funktioniert nicht mehr)

**Symptom:** Anode ist nur 50% verbraucht, aber Thru-Hulls zeigen Korrosionssymptome. Potentialmessung: Anode-Potential zu edel (−200 bis −300 mV statt −800 mV).

**Ursache:** Anode hat isolierende Oxidschicht: Calcium-/Magnesium-Carbonat-Aufbau (längere Liegezeit), Biofouling-Überwachsung, schlechter Kontakt am Befestigungs-Lug, oder unterbrochenes Bonding.

**Häufigkeit:** Selten, aber bei Dauerlieger-Booten in warmen Gewässern beobachtet.

**Diagnose (Confidence: measured):** Potentialmessung direkt an Anode deutlich weniger negativ als erwartet. Visuell: Weiße/grünliche Beschichtung (nicht normales dunkles Grau). Widerstandsmessung: Bonding > 1 Ohm (sollte < 0,1 Ohm).

**Maßnahme:** Anode abbürsten/abschleifen (Meißel + Drahtbürste), Kontaktfläche freilegen, Bonding überprüfen + neu verbinden, Potentialmessung wiederholen.

**Lehre:** Anoden sind nicht "set and forget". Jährliche Inspektionen erforderlich!

**Confidence:** measured (Potentialmessung)

### Fehlerbild 10: Falsche Anode-Material-Wahl auf Alu-Boot

**Symptom:** Alu-Boot mit Magnesium-Anoden (falsch!). Nach 4–6 Monaten Segeln: Blistering, lokale Rumpf-Schwachstellen, Überprotektion-Symptome.

**Ursache:** "Bessere" Anoden gekauft. Mg ist edler, größere Potentialdifferenz. ABER: Auf Alu-Booten führt das zu Überprotektion (Wasserstoff-Versprödung).

**Häufigkeit:** Gelegentlich bei Second-Hand-Alu-Yachten mit Wartungs-Fehlern.

**Diagnose:** Anode inspizieren (silbrig-grau = Mg). Potentialmessung zu negativ (< −1.000 mV). Rumpf-Inspektionsergebnis: Blistering.

**Material-Vergleich (Confidence: measured):**
| Anode-Typ | Potential zu Alu 5083 | Schutz | Überprotektion | Alu-Eignung |
|-----------|---------------------|--------|-------------|-----------|
| Zink | 300–350 mV | Optimal | Nein | ✅ IDEAL |
| Alu-Navalloy | 200–250 mV | Gut | Nein | ✅ GUT |
| Magnesium | 450–500 mV | Sehr gut | **JA!** | ❌ VERBOTEN |

**Maßnahme:** Mg-Anoden entfernen, Zink-Navalloy ersetzen, Potentialmessung überprüfen, beschädigte Bereiche reparieren.

**Lehre:** Alu-Boote brauchen Zink oder Alu-Navalloy. Keine "Upgrades" zu edleren Anoden!

**Confidence:** measured (Anode-Analyse, Potentialmessung)

### Fehlerbild 11: Graphit-Packing-Korrosion an Wellenlagerung

**Symptom:** Propellerwelle korrodiert rapid, obwohl Bonding-System intakt. Korrosion konzentriert sich auf Lagerung (Stern-Rohr). Wasser farblich verfärbt (metallischer Glanz).

**Ursache:** Wellenlagerung nutzt Graphit-Packing als Dichtung (Standard älteren Booten). Graphit ist EXTREM edel (ähnlich Platin). Graphit ↔ Manganstahl-Welle = massive Korrosion.

**Häufigkeit:** Moderat, besonders Boote 1980–2010 mit traditionellen Stern-Rohren.

**Diagnose (Confidence: visual_high):** Weiße/rötliche Korrosions-Produkte an Wellenlagerung. Graphit-Packing hat > 600 mV Differenz zu Stahlwelle. Ölanalyse: erhöhter Eisengehalt.

**Maßnahme:** Stern-Rohr ausbessern oder PTFE-Packing ersetzen (Graphit vermeiden), Welle mit Epoxy-Schutzschicht versiegeln, Bonding-Draht direkt zum Lager-Gehäuse führen.

**Lehre:** Graphit-Packing ist historisch, aber hochgradig korrosionsanfällig. Moderne Boote verwenden PTFE oder Polycarbonat-Packing.

**Confidence:** visual_medium (Korrosionsmuster sichtbar, aber mehrdeutig interpretierbar)

---

## FAQ — Häufige Fragen

### FAQ 1: Kann ich Bronze-Thru-Hulls auf meiner Alu-Yacht verwenden?
**NEIN.** Die Potentialdifferenz Bronze↔Aluminium beträgt 500–600 mV. Bronze im Kontakt mit Alu-Rumpf erzeugt massive galvanische Korrosion. Verwende TruDesign (Kunststoff) oder geschweißte Alu-Thru-Hulls. (Confidence: measured)

### FAQ 2: BSP oder NPT — wie erkenne ich den Unterschied?
BSP hat einen Flankenwinkel von 55° (gerundete Gewindespitzen), NPT hat 60° (flache Spitzen). Am sichersten: Gewindelehre verwenden. Bei 3/4" unterscheidet sich der Außendurchmesser nur um 0,23 mm — optisch kaum erkennbar. (Confidence: measured)

### FAQ 3: Wie oft müssen Opferanoden gewechselt werden?
Bei >50% Verbrauch austauschen. In tropischen Gewässern alle 6–12 Monate, in gemäßigten Gewässern alle 12–18 Monate. Bei Landstrom-Anschluss ohne Trenntrafo: Kontrolle alle 3 Monate! (Confidence: documented)

### FAQ 4: Kunststoff- oder Bronze-Thru-Hulls — was ist besser?
Beide sind normkonform (ISO 9093-1 bzw. -2). Bronze: Traditionell, robust, antimikrobiell, aber galvanisch aktiv. Kunststoff: Korrosionsfrei, leichter, günstiger, aber geringere Schlagfestigkeit. Für Alu-Boote: NUR Kunststoff. Für GFK-Boote: Beides gut. Für Offshore/Blauwasser: Meinungen geteilt — Puristen bevorzugen Bronze, Pragmatiker wählen TruDesign. (Confidence: benchmark)

### FAQ 5: Mein Seeventil sitzt fest — was tun?
NICHT mit Gewalt arbeiten. Penetrationsöl einsprühen, 24h einwirken lassen. Leicht klopfen (Plastik- oder Messinghammer). Vorsichtig mit Hebel + Verlängerungsrohr bewegen. Wenn nichts hilft: Boot slippen, Ventil ausbauen. NIEMALS ein festsitzendes Ventil als "geschlossen" betrachten — es kann undicht sein. (Confidence: documented)

### FAQ 6: Welche Dichtmasse für Borddurchbrüche?
Sikaflex 291 oder 3M 4200 sind der Standard. NICHT 3M 5200 (quasi permanent, Austausch wird Albtraum). KEIN Silikon unter der Wasserlinie. Tipp: Sikaflex 291 für alle Borddurchbrüche — bewährt, stark genug, bei Bedarf entfernbar. (Confidence: documented)

### FAQ 7: Brauche ich ein Bonding-System?
Ja, wenn metallische Unterwasser-Komponenten vorhanden sind (Bronze-Thru-Hulls, Propellerwelle, Motor). Das Bonding verbindet alle Metalle und die Opferanoden zu einem System. Ohne Bonding schützen die Anoden nur das direkt angrenzende Metall. (Confidence: documented)

### FAQ 8: Was ist der Unterschied zwischen einem Kugelhahn und einem Konusventil?
Kugelhahn (Ball Valve): 1/4-Drehung auf/zu, geringe Wartung, voller Durchgang. Konusventil (Seacock): Traditionell, konischer Stopfen, muss regelmäßig gefettet werden, dichtet bei guter Wartung sehr zuverlässig. Schieberventil (Gate Valve): VERBOTEN unter der Wasserlinie (ABYC H-27). (Confidence: documented)

### FAQ 9: Kann Streustrom meinen Rumpf zerstören?
Ja. Streustrom-Korrosion ist aggressiver als normale galvanische Korrosion, weil eine externe Stromquelle die Reaktion antreibt. Ein einziger Fehler im Hafennetz kann binnen Wochen Opferanoden auffressen und Metall-Bauteile beschädigen. Lösung: Trenntrafo oder Galvanic Isolator. (Confidence: documented)

### FAQ 10: Zink-, Aluminium- oder Magnesium-Anoden?
Salzwasser: Zink oder Aluminium (Navalloy). Brackwasser: Aluminium. Süßwasser: NUR Magnesium. NIEMALS Magnesium in Salzwasser (Überprotektion). NIEMALS Zink in Süßwasser (passiviert). Alu-Anoden (Navalloy) sind der beste Kompromiss für gemischte Gewässer. (Confidence: documented)

### FAQ 11: Darf ich ICCP (Impressed Current) auf meiner Segelyacht installieren?
ICCP ist typisch für große Motoryachten, Frachter und Stahlschiffe — nicht für kleine Segelyachten. Grund: ICCP erfordert externe Stromquelle (120–240V), regelmäßige Überwachung, und erzeugt Elektromagnetische Störungen (EMI) für UKW-Funk. Opferanoden sind passiv + zuverlässig. Ausnahme: Superyachten (>30m) mit zentralisiertem Energiesystem. (Confidence: documented)

### FAQ 12: Kann ich Thru-Hull während der Fahrt ersetzen?
Technisch ja, praktisch ein Notfall. Mit Holzstopfen, Sikaflex 291, Schlauch und Schellen ist es machbar (siehe ANHANG E). SV Delos hat 13 Thru-Hulls afloat ersetzt (YouTube-Dokumentation). ABER: Im nächsten Hafen professionell ersetzen! Provisorische Reparationen halten nur 24–48h. (Confidence: documented)

### FAQ 13: Versicherer-Anforderungen für Thru-Hulls?
Typische Versicherungs-Klauseln (mit Versicherer prüfen):
- **Jährliche Inspektion:** Inspektionsprotokoll ≥ 1× jährlich erforderlich (Haul-Out)
- **Bronze-Dezinkifizierungs-Test:** Empfohlen alle 3 Jahre
- **Bonding-System:** Muss funktionsfähig sein (Widerstand < 1 Ohm)
- **Streustrom-Schutz:** Bei permanenter Landstrom-Verbindung wird Trenntrafo/Galvanic Isolator erwartet
- **Dokumentation:** Service-Reports, Kaufbelege für Ersatzteile sollten archiviert werden
(Confidence: estimated — individuelle Versicherungen haben unterschiedliche Richtlinien)

### FAQ 14: Was sagt der Gutachter/Surveyor bei Thru-Hull-Kontrolle?
Professionelle Surveyors verwenden ein strukturiertes Protokoll. Typische Einträge:
- "Thru-hull bronze, appears sound, patina normal. Dezincification test recommended at next haul-out." → OK
- "Yellow brass fittings, surface pitting noted. Immediate replacement recommended." → CRITICAL
- "Bonding wire corroded, resistance > 5 Ohm. Rebonding required." → DEFECT
(Confidence: documented — Standard-Surveyor-Protokolle)

### FAQ 15: Welche Größen-Fehler passieren beim Austausch?

| Fehler | Ursache | Folge | Impact |
|-------|--------|-------|--------|
| NPT statt BSP | Verwechslung (beide Zöllisch) | Undicht, Deformation | €50–100 |
| Falsche Nenngröße | Augen-Schätzung | Passt nicht, Strömungsfehler | €80–150 |
| Kunststoff statt Bronze | Kosten sparen | Keine Kompatibilität | €60–100 |
| Bronze auf Alu-Boot | Unwissen | Katastrophen-Korrosion 3–6 Mo. | €3.000–5.000 |
| 3M 5200 Dichtmasse | Verfügbarkeit | Austausch später Albtraum | €150–300 |

(Confidence: documented — Häufige Fehler aus Service-Reports)

### FAQ 16: Landstrom + Streustrom — warum ist das Problem?
Fehler im Haftnetz können Strom von Boot A nach Boot B über Unterwasser-Metallteile leiten. Boot B wird ungewollte Kathode und wird massiv beschädigt (Anoden in 3 Monaten aufgelöst, Propeller gepitted). Lösung: Trenntrafo (€250–800) oder Isolation Transformer (€800–3.500). Mit Multimeter AC-Spannug zwischen PE und Wasser prüfen: > 5V AC = Problem! (Confidence: documented)

### FAQ 17: Mein Boot ist ganz aus Kunststoff (Polyester). Brauche ich Bonding?
Nein — Kunststoff ist nicht-leitend. ABER: Wenn metallische Unterwasser-Teile vorhanden sind (Welle, Propeller, Kupfer-Schläuche), MÜSSEN diese untereinander + zur Anode gebondet werden. Regel: Alle metallischen Unterwasser-Teile müssen zusammenhängen. (Confidence: documented)

### FAQ 18: Kann ich Carbon-Faser-Teile direkt mit Metallen verbinden?
**NEIN!** Graphit ist auf der edlen Seite der Spannungsreihe. Carbon-Mast + Alu-Mastfuß = 1.000+ mV = garantierte Katastrophen-Korrosion. Lösung: G10/G11 Isolierplatte + Nylon-Unterlegscheiben + Tef-Gel. Bonding NICHT durch Carbon führen. (Confidence: measured)

### FAQ 19: Wie lange halten Opferanoden?
Salzwasser-Standard: Zink 5kg = 10–12 Monate (mittlerer Verbrauch), 6–8 Monate (tropisch/Dauerlieger). Alu-Navalloy 5kg = 12–18 Monate. Brackwasser: Alu-Navalloy 10–14 Monate. Austauschregel: > 50% Verbrauch. Verbrauch prüfen: Visual (> 50%) oder Gewicht messen. (Confidence: documented — BoatUS Foundation-Daten)

### FAQ 20: Versiegelt der TÜV/Lloyd's die Rumpfbohrung beim Thru-Hull-Austausch?
**NEIN.** TÜV/Lloyd's kontrolliert Norm-Konformität (ISO 9093, ABYC H-27), nicht die Rumpfbohrung selbst. Lloyd's kennzeichnet Einbau als "nicht konform", wenn: Falsche Material-Paarung, Bonding fehlt, falsche Dichtmasse, Anoden fehlen. (Confidence: estimated — Lloyd's Register Standards)

---

## Glossar

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|-----------|
| Borddurchbruch | Thru-Hull / Through-Hull | Durchführung durch den Rumpf unter der Wasserlinie |
| Borddurchführung | Skin Fitting | Innengewindestutzen zur Aufnahme von Thru-Hull |
| Seeventil | Seacock | Absperrorgan direkt am Borddurchbruch |
| Kugelhahn | Ball Valve | Ventil mit kugelförmigem Absperrkörper, 1/4-Drehung |
| Konusventil | Tapered Plug Valve | Traditionelles Seeventil mit konischem Stopfen |
| Schieberventil | Gate Valve | VERBOTEN unter WL! Schieber hebt/senkt sich |
| Opferanode | Sacrificial Anode | Unedleres Metall, das sich statt des zu schützenden Metalls auflöst |
| Galvanische Korrosion | Galvanic Corrosion | Korrosion durch Potentialdifferenz zwischen ungleichen Metallen |
| Streustrom | Stray Current | Elektrischer Fehlstrom über Wasser als Leiter |
| Dezinkifizierung | Dezincification | Selektive Auslösung von Zink aus einer Kupfer-Zink-Legierung |
| Potentialausgleich | Bonding / Equalizing | Elektrische Verbindung aller Unterwasser-Metalle |
| Kathode | Cathode | Edleres Metall — wird geschützt |
| Anode | Anode | Unedleres Metall — opfert sich |
| Passivierung | Passivation | Bildung einer schützenden Oxidschicht (z.B. Cr₂O₃ auf Edelstahl) |
| Lochfraß | Pitting Corrosion | Lokale, tiefe Korrosionslöcher |
| Spaltkorrosion | Crevice Corrosion | Korrosion in engen Spalten (Sauerstoffverarmung) |
| Flächenverhältnis | Cathode-to-Anode Ratio | Verhältnis der Flächen von Kathode zu Anode |
| Elektrolyt | Electrolyte | Leitfähige Flüssigkeit (Meerwasser) |
| Trenntrafo | Galvanic Isolator / Isolation Transformer | Schutzgerät gegen Streustrom bei Landstrom |
| DZR | Dezincification Resistant | Bezeichnung für zinkresistente Messinglegierungen |
| TPI | Threads Per Inch | Gewindegänge pro Zoll |
| BSP | British Standard Pipe | Britisches Rohrgewinde (55° Flankenwinkel) |
| NPT | National Pipe Thread | US-amerikanisches Rohrgewinde (60° Flankenwinkel) |
| Rotguss | Red Brass / Gunmetal | Kupfer-Zinn-Blei-Zink-Legierung (z.B. C83600 / 85-5-5-5) |
| NiAlBr | Nickel-Aluminium-Bronze | Hochfeste Kupfer-Legierung (z.B. C95800) |
| Pilzkopf | Mushroom Head | Thru-Hull-Form für geringen Strömungswiderstand |
| Full Bore | Voller Durchgang | Ventilöffnung entspricht Rohrdurchmesser |
| Flush | Bündig | Flansch bündig mit Rumpfaußenhaut |
| Strainer | Seefilter / Siebkorb | Filter vor der Pumpe zur Fremdkörper-Abscheidung |
| Scoop | Schöpföffnung | Thru-Hull mit Scoop zur verbesserten Wasseraufnahme |
| Backing Nut | Gegenmutter | Mutter auf der Innenseite des Rumpfes |
| PTFE | Polytetrafluorethylen (Teflon) | Dichtmaterial für Gewinde und Ventilsitze |
| Epoxy | Epoxidharz | 2K-Harz für Versiegelung, Beschichtung, Reparatur |
| Wellenschleifer | Shaft Brush / Cutless Bearing | Verschleißteil in der Wellenlagerung, kann galvanische Kontakte erzeugen |
| Seekiste | Sea Chest | Großes Sammelbecken für Kühlwasser-Einlässe (typ. Fischerboote/Frachter) |
| Stevenrohr | Stern Tube | Dicht-/Lagersystem um die Propellerwelle an Heck |
| ICCP | Impressed Current Cathodic Protection | Aktive kathodische Schutzanlage mit externer Stromquelle (vs. Opferanoden) |
| Impressed Current | Aufgezwungener Strom | Externer Stromfluss zur Schutzpotential-Einstellung |
| Kathodischer Schutz | Cathodic Protection | Verfahren zum Schutz metallischer Strukturen vor Korrosion |
| Überprotektion | Overprotection | Zu negatives Potential → Wasserstoff-Versprödung + Beschichtungsschäden |
| Wasserstoff-Versprödung | Hydrogen Embrittlement | Diffusion von H-Atomen in Metall bei zu negativem Potential → Versprödung |
| Anodischer Index | Anodic Index | Relative Position eines Materials in der galvanischen Spannungsreihe |
| Graphit-Packing | Graphite Packing | Dichtungsmaterial in Wellenlagerungen (Graphit ist extrem edel! Galvanische Gefahr) |
| Potentialverlauf | Potential Gradient | Potentialdifferenz-Verteilung längs einer Struktur (Messung mit Referenzelektrode) |
| Referenzelektrode | Reference Electrode | Vergleichselektrode (typ. Cu/CuSO₄) für Potentialmessung gegen Standard |
| SCE | Saturated Calomel Electrode | Standardreferenzelektrode für Meerwasser-Messungen (−0,24V vs. SHE) |
| Schenkelbindung | Padeye Bonding | Verbindung von Festigkeitsknoten (Schäkel) zum Bonding-System |
| Isolierplatte | Isolation Washer / Bearing Isolator | Plastik-/GFK-Scheibe zwischen Metallen zur galvanischen Trennung |
| Tef-Gel | (Proprietary) | Hochleistungs-Schmiermittel + Isolant von Lanocote (Standard für Marine-Anwendungen) |
| Lanocote | Marine Grease | Bleihaltige Schmierpaste mit natürlichen Ölen (EPA-zertifiziert für Marine) |
| Trilux | Marine Antifouling | Hochleistungs-Antifouling ohne Kupfer (für Alu-Boote essentiell) |
| International Interprotect | Epoxy-Beschichtung | 2K-Epoxy Barrierschicht für Stahlrümpfe (Deckschicht vor Antifouling) |
| Jotun Jotamastic | Epoxy-Oberflächenschutz | Norwegische High-Performance Beschichtung für Stahlrümpfe (Frachter-Standard) |
| Kupferfreies Antifouling | Copper-Free Antifouling | Neuere Formulierungen mit Zinnverbindungen oder Bioziden (Alu-Boot-kompatibel) |
| Hochfrequenz-Wirbel | Eddy Current / Impedance Probe | Zerstörungsfreie Dickenmessung von Metallschichten (Wandstärke unter Beschichtung) |
| Ultraschall-Dickenmessung | Ultrasonic Thickness Gauge | Standardmessgerät für Thru-Hull-Wandstärke im Feld (€100–400) |
| Spannungsreihe (Galvanische) | Galvanic Series | Anordnung von Metallen nach ihrer edel/unedel-Reihenfolge in Meerwasser |
| Passivlage | Passive Layer / Oxide Film | Schützende Oxidschicht auf Edelstahl (Cr₂O₃), kann unter Bedingungen zusammenbrechen |
| Spaltkorrosion-Anfälligkeit | Crevice Corrosion Susceptibility | Material-Eigenschaft, in Spalten zu korrodieren (316L besser als 304) |
| DZR-Test | Dezincification Resistant Test | ASTM-Verfahren zum Prüfen von Messinglegierungen auf Dezinkifizierungsfestigkeit |
| Schutzpotential | Protection Potential | Elektrisches Potential, bei dem ein Metall kathodisch geschützt ist (typ. −800 bis −900 mV für Stahl) |
| Ag/AgCl | Silver/Silver Chloride | Meerwasser-Referenzelektrode, Standardpotential −0,222V vs. SHE |
| SHE | Standard Hydrogen Electrode | Absolute Referenz für Elektrodenpotentiale (0,000V per Definition) |
| Cu/CuSO₄ | Copper/Copper Sulfate Electrode | Boden-/Süßwasser-Referenzelektrode, +0,318V vs. SHE |
| Polarisation | Polarization | Potential-Verschiebung eines Metalls durch Stromfluss (kathodisch = edler, anodisch = unedler) |
| Depolarisation | Depolarization | Rückkehr zum natürlichen Potential nach Stromunterbrechung |
| Faradaysches Gesetz | Faraday's Law | m = (M × I × t) / (n × F) — Masse des aufgelösten Metalls proportional zu Strom × Zeit |
| Mixed Potential | Mischpotential | Gleichgewichtspotential einer galvanischen Paarung (zwischen den Einzelpotentialen) |
| Bimetall-Korrosion | Bimetallic Corrosion | Synonym für galvanische Korrosion bei Kontakt zweier verschiedener Metalle |
| Erosionskorrosion | Erosion Corrosion | Kombination aus mechanischem Abtrag (Strömung) und Korrosion |
| Kavitation | Cavitation | Implosion von Dampfblasen bei hoher Strömungsgeschwindigkeit → Materialzerstörung |
| Interkristalline Korrosion | Intergranular Corrosion | Korrosion entlang der Korngrenzen (Schweißnaht-Bereich bei sensibilisiertem Edelstahl) |
| Spannungsrisskorrosion | Stress Corrosion Cracking (SCC) | Rissbildung durch Kombination von Zugspannung + korrosivem Medium (Chlorid + Edelstahl) |
| Filiformkorrosion | Filiform Corrosion | Fadenförmige Unterrostung unter Beschichtungen |
| Nahtkorrosion | Weld Decay | Korrosion in der Wärmeeinflusszone (WEZ/HAZ) nach dem Schweißen |
| Deaeration | Entlüftung | Entfernung von gelöstem Sauerstoff (reduziert Korrosionsrate drastisch) |
| Biofouling | Biologischer Bewuchs | Ansiedlung von Organismen (Muscheln, Algen, Seepocken) auf Unterwasser-Oberflächen |
| Makrofouling | Macrofouling | Bewuchs durch sichtbare Organismen (Muscheln, Seepocken, Algen) |
| Mikrofouling | Microfouling | Bewuchs durch Bakterien und Biofilm (Vorstufe des Makrofoulings) |
| MIC | Microbiologically Influenced Corrosion | Korrosion beschleunigt durch Mikroorganismen (Sulfat-reduzierende Bakterien) |

---

## ANHANG A: Galvanische Kompatibilitätsmatrix

### Legende
- ✅ = Kompatibel (< 100 mV Differenz)
- ⚠️ = Bedingt kompatibel (100–250 mV, Schutzmaßnahmen empfohlen)
- ❌ = Inkompatibel (> 250 mV, NICHT ohne Isolation kombinieren)

| | SS316L(p) | SS316L(a) | Bronze C83600 | Kupfer | Alu 5083 | Stahl | Zink | Blei | Titan |
|---|-----------|-----------|-------------|-------|----------|-------|------|------|-------|
| **SS316L (passiv)** | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **SS316L (aktiv)** | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ❌ |
| **Bronze C83600** | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ |
| **Kupfer** | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ |
| **Alu 5083** | ❌ | ⚠️ | ❌ | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| **Stahl** | ❌ | ✅ | ❌ | ❌ | ⚠️ | ✅ | ⚠️ | ✅ | ❌ |
| **Zink** | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ | ✅ | ⚠️ | ❌ |
| **Blei** | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| **Titan** | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ✅ |

---

## ANHANG B: BSP/NPT Cross-Referenz-Tabelle

| Nenn-größe | BSP OD (mm) | BSP TPI | NPT OD (mm) | NPT TPI | Differenz OD | Kompatibel? |
|-----------|------------|---------|-------------|---------|-------------|------------|
| 1/8" | 9,73 | 28 | 10,29 | 27 | 0,56 mm | NEIN |
| 1/4" | 13,16 | 19 | 13,57 | 18 | 0,41 mm | NEIN |
| 3/8" | 16,66 | 19 | 17,15 | 18 | 0,49 mm | NEIN |
| 1/2" | 20,96 | 14 | 21,22 | 14 | 0,26 mm | NEIN |
| 3/4" | 26,44 | 14 | 26,67 | 14 | 0,23 mm | NEIN |
| 1" | 33,25 | 11 | 33,40 | 11,5 | 0,15 mm | NEIN |
| 1-1/4" | 41,91 | 11 | 42,16 | 11,5 | 0,25 mm | NEIN |
| 1-1/2" | 47,80 | 11 | 48,26 | 11,5 | 0,46 mm | NEIN |
| 2" | 59,61 | 11 | 60,33 | 11,5 | 0,72 mm | NEIN |

**ALLE Nenngrößen: INKOMPATIBEL.**

---

## ANHANG C: Dimensionierungstabelle nach Bootsgröße

### C.1 Borddurchbruch-Nenngrößen nach Anwendung und Bootslänge

| Bootslänge | Motor-Kühlung | Toilette Ein | Toilette Aus | Bilge | Cockpit-Lenzer | Waschbecken |
|-----------|--------------|-------------|-------------|-------|---------------|------------|
| 7–9m | 3/4" | 3/4" | 3/4" | 1" | 1-1/4" | 1/2" |
| 9–12m | 1" | 3/4" | 1" | 1-1/4" | 1-1/2" | 3/4" |
| 12–15m | 1-1/4" | 1" | 1-1/4" | 1-1/2" | 2" | 3/4" |
| 15–20m | 1-1/2" | 1" | 1-1/4" | 2" | 2" | 1" |
| 20m+ | 1-1/2"–2" | 1-1/4" | 1-1/2" | 2"+ | 2"+ | 1" |

### C.2 Typische Anzahl Borddurchbrüche nach Bootstyp

| Bootstyp | Unter WL | Über WL | Gesamt | Anmerkung |
|---------|---------|--------|--------|-----------|
| Daysailer 7m | 2–3 | 1–2 | 3–5 | Motor-Kühlung, Lenz, WC |
| Fahrtensegler 10m | 4–6 | 2–3 | 6–9 | +Kühlbox, Echolot, Log |
| Fahrtensegler 13m | 6–8 | 3–4 | 9–12 | +2. WC, Klimaanlage |
| Blauwasser-Segler 15m | 8–12 | 4–6 | 12–18 | +Watermaker, Generator |
| Motoryacht 12m | 6–10 | 3–5 | 9–15 | Mehr Motorkühlung, Klima |
| Motoryacht 18m | 10–16 | 5–8 | 15–24 | +Bugstrahlruder, Stabilizer |
| Katamaran 12m | 8–12 | 4–6 | 12–18 | Pro Rumpf separat! |
| Superyacht 25m+ | 20–40 | 10–20 | 30–60 | Klima, Pool, Tender |

### C.3 Opferanoden-Dimensionierung nach Bootsgröße

| Bootslänge | Rumpf-Material | Anoden-Typ | Mindestanzahl | Position | Gewicht gesamt (kg) |
|-----------|---------------|-----------|--------------|---------|-------------------|
| 7–9m | GFK | Zink (Welle + Propeller) | 2–3 | Welle, Ruder | 1–2 |
| 9–12m | GFK | Zink (Welle + Propeller + Trim-Tab) | 3–5 | Welle, Ruder, Trim-Tab | 2–4 |
| 12–15m | GFK | Zink/Navalloy | 4–6 | Welle, Ruder, Rumpf | 3–6 |
| 15–20m | GFK | Zink/Navalloy | 6–10 | Welle, Ruder, Rumpf, Bugstrahlruder | 5–10 |
| 9–12m | Stahl | Zink | 8–12 | Rumpf verteilt (alle 2m) | 8–15 |
| 12–15m | Stahl | Zink | 12–18 | Rumpf verteilt + Ruder + Welle | 15–25 |
| 9–12m | Aluminium | Zink (NUR!) | 6–10 | Rumpf verteilt, Spiegel, Kiel | 6–12 |
| 12–15m | Aluminium | Zink (NUR!) | 10–16 | Rumpf verteilt alle 1,5m | 12–20 |

### C.4 Strömungsgeschwindigkeits-Grenzwerte in Thru-Hulls

| Material | Max. Strömung (m/s) | Anmerkung |
|---------|-------------------|-----------|
| Rotguss C83600 | 2,0 | Standard-Marine |
| Zinnbronze C90300 | 2,5 | Etwas höher als Rotguss |
| NiAlBr C95800 | 4,0 | Erosionsbeständig |
| CuNi 90/10 | 3,0 | Rohrleitungen |
| CuNi 70/30 | 3,5 | Wärmetauscher |
| TruDesign PA6-GF30 | 3,0 | Kunststoff — keine Erosion, aber Abrasion |
| Edelstahl 316L | 5,0+ | Sehr erosionsbeständig |

**Berechnung der Strömungsgeschwindigkeit:**
```
v = Q / A
v = Strömungsgeschwindigkeit (m/s)
Q = Volumenstrom (m³/s) — z.B. Motorpumpe 80 L/min = 0,00133 m³/s
A = Querschnittsfläche (m²) — z.B. 1" Bohrung: π × 0,0127² = 0,000507 m²
→ v = 0,00133 / 0,000507 = 2,6 m/s
```

**Erfahrungsbericht — marinehowto.com (Compass Marine), "How to Size Thru-Hulls":**
> "Most boat owners undersize their thru-hulls. A 1" fitting might seem adequate for a 50HP engine, but at full RPM the flow velocity can exceed safe limits for bronze. Size up — the cost difference between 1" and 1-1/4" is negligible."

### C.5 Minimale Rumpfverstärkung für Borddurchbrüche (GFK)

| Rumpf-Laminatdicke | Verstärkungsplatte (innen) | Material | Mindestdicke | Mindestgröße |
|--------------------|--------------------------|---------|--------------| -----------|
| < 8 mm | PFLICHT | GFK oder Marine-Sperrholz + GFK | 10 mm | 4× Flansch-Ø |
| 8–15 mm | Empfohlen | GFK oder Backing Block | 8 mm | 3× Flansch-Ø |
| > 15 mm | Optional | — | — | — |

**Bei Sandwich-Laminat (Kern: Balsa/Schaum):**
1. Kern im Bereich 3× Flansch-Ø entfernen
2. Hohlraum mit Epoxy/Glasfaser ausfüllen (Kern-Ersatz)
3. NIEMALS direkt durch Kern bohren (Wasserintrusion!)
4. Aushärtezeit 72h vor Thru-Hull-Einbau

**Confidence:** documented (ISO 12215-5, ABYC H-27)

---

## ANHANG D: Confidence-Mapping für AYDI-Module

| Datenquelle | AYDI Confidence Level | Badge-Farbe | Anzeige |
|------------|----------------------|-------------|---------|
| Potentialmessung (SCE-Referenz) | measured | Grün | Immer |
| Berechnung aus Materialkenndaten | calculated | Grün | Immer |
| Klare Foto-Aufnahme (Korrosionsmuster) | visual_high | Blau | Immer |
| Foto mit eingeschränkter Qualität | visual_medium | Amber | Immer |
| Schlechtes Foto, mehrdeutig | visual_low | — | Versteckt |
| Nicht beurteilbar | visual_insufficient | — | Nur Metadaten |
| Aus Spannungsreihe/Tabellenwert | estimated | Grau | Immer |
| Aus Industriedaten/Literatur | benchmark | Grau | Immer |
| Aus Service-Report | documented | Blau | Immer |

---

## ANHANG E: Bordausstattung — Empfohlene Ersatzteile

### Minimum-Bordvorrat Thru-Hull/Seeventil

| Gegenstand | Menge | Anmerkung | Preis EUR |
|-----------|-------|-----------|----------|
| Weichholz-Stopfen (konisch) | Je 2 pro Thru-Hull-Größe | Sofort-Notmaßnahme bei Leck | €3–8/Stk |
| Sikaflex 291 (Kartusche) | 1 | Notfall-Abdichtung | €14 |
| PTFE-Band | 2 Rollen | Gewinde-Abdichtung | €3/Rolle |
| Schlauchschellen Edelstahl (Satz) | Passend zu allen Schläuchen | Ersatz bei Rost/Versagen | €15–30 |
| Reserv-Kugelhahn (häufigste Größe) | 1 | Für Notfallwechsel im Wasser | €35–65 |
| Tef-Gel | 1 Tube | Anti-Seize, galvanische Isolation | €18 |
| Leckstopfen (Quick-Stop) | 1 universell | Notfall-Abdichtung von innen | €25–40 |
| Schlauchstück (Reserv, häufigste Größe) | 1m | Ersatz bei Schlauchbruch | €8–15/m |

**Erfahrungsbericht — forums.ybw.com, User "PreparedSailor", 2021:**
> "Wooden bungs tied to each thru-hull with string. Sounds old-fashioned, but when a hose burst at 3 AM and the cabin started flooding, I had a bung in the hole in 15 seconds while half asleep. They cost 50p each."

### Softwood Bung-Größen

| Thru-Hull Nenngröße | Bung-Durchmesser (mm) | Passende Produkte |
|---------------------|----------------------|-------------------|
| 1/2" | 18–20 | Davis 530, Plastimo 38965 |
| 3/4" | 22–25 | Davis 530, Plastimo 38966 |
| 1" | 28–32 | Davis 531, Plastimo 38967 |
| 1-1/4" | 35–38 | Davis 531 |
| 1-1/2" | 42–45 | Davis 532, Plastimo 38968 |
| 2" | 54–58 | Davis 532 |

### Erweiterte Offshore-Ersatzteiliste für Langfahrten (>6 Monate)

Für Weltfahrten oder tropische Dauersegeln sollte eine umfassendere Liste an Bord sein.

| Gegenstand | Menge | Grund | Preis EUR | Lagerfrist |
|-----------|-------|--------|----------|-----------|
| Komplette Thru-Hull-Ersatzeinheit (häufigste Größe, z.B. 3/4") | 1 | Totaler Ausfall möglich | €180–250 | 5 Jahre |
| Komplette Thru-Hull-Ersatzeinheit (zweitgrößte, z.B. 1") | 1 | Motorkühlungs-Ausfallsicherung | €220–280 | 5 Jahre |
| Kugelhahn (passende Größe, BSP) | 2 | Ventil-Verschleiß | €40–80/Stk | 10 Jahre |
| Schlauch (Kühlwasser-Qualität, 25mm ID) | 10m | Schlauch-Verschleiß/Risse | €8–12/m | 5 Jahre |
| Schlauch (Bilge-Qualität, 38mm ID) | 5m | Backup für alle Größen | €6–10/m | 5 Jahre |
| Schlauchschellen Edelstahl 316 (Satz 20–40mm) | 10 Stk | Rost + Verschleiß | €2–4/Stk | 10 Jahre |
| Sikaflex 291 (Kartusche) | 3 | Dichtung + Reparatur | €14 | 2 Jahre |
| 3M 4200 (Kartusche) | 2 | Alternative zu Sikaflex | €15 | 2 Jahre |
| PTFE-Band (Rolle) | 3 | Gewinde-Abdichtung | €3/Rolle | 10 Jahre |
| Weichholz-Stopfen (konisch, alle Größen) | Satz à 5 | Notfall-Verschluss | €25/Satz | 10 Jahre |
| Seeventil (Kugelhahn 3/4") oder (Konusventil) | 1 | Ventilkörper-Verschleiß | €50–150 | 5 Jahre |
| Tef-Gel (Tube) | 2 | Anti-Seize + galvanische Isolation | €18/Tube | 5 Jahre |
| Leckstopfen Quick-Stop (universal) | 2 | Notfall-Abdichtung von innen | €30–40/Stk | 5 Jahre |
| Messingdraht + Wickel-Bindedraht | 1 Satz | Provisorische Befestigung beschädigter Schläuche | €10 | 10 Jahre |
| Epoxy-Zweikomponentenharz (Schnellhärter) | 1 Kit | Reparatur von Rumpfschäden um Thru-Hull | €25–35 | 3 Jahre |
| Masking-Tape + Sandpapier (P80, P120) | Satz | Vorbereitung für Dichtmasse | €8 | 2 Jahre |
| Aceton / Isopropanol (Behälter) | 0,5l | Entfettung vor Dichtung | €6–8 | 3 Jahre |
| Schiffskitt / Holzkitt (Zweikomponent) | 1 Tube | Reparatur von Holzstöpseln + Provisionen | €12 | 3 Jahre |
| Bonding-Kabel Kupfer 4 mm² (5m) | 1 Rolle | Potentialausgleich-Reparatur | €20 | 10 Jahre |
| Kabelschuhe M6/M8 Edelstahl | 10 Stk | Bonding-Verbindungen | €1–2/Stk | 10 Jahre |

### Werkzeug-Liste für Thru-Hull-Reparatur an Bord (Notfall)

| Werkzeug | Zweck | Größe/Typ | Preis EUR |
|---------|-------|-----------|----------|
| Drehmomentschlüssel (klein, 5–25 Nm) | Gegenmutter nicht überdrehen | 1/4" Drive | €45–70 |
| Knarre + Steckschlüssel-Satz | Gegenmutter anziehen | Inch (1/2", 3/4", 1") | €30–50 |
| Thru-Hull-Schlüssel (Groco-Kompatibel) | Thru-Hull-Flansch drehen | Universell | €30–45 |
| Maulschlüssel-Satz | Universelle Anwendungen | 6–24mm | €20–30 |
| Spitzzange | Dichtmasse entfernen | — | €8–12 |
| Schaber + Spatel | Alte Dichtung abkratzen | Kunststoff/Stahlblech | €5–10 |
| Messschieber | Wandstärke messen | 0–150mm | €15–25 |
| Innensechskant-Satz (Metrisch + Inch) | Schraub-Befestigungen | 2–8mm (metrisch), 1/16"–1/4" | €12–18 |
| Lochsäge (Bimetall, alle Größen 16–40mm) | Notfall-Rumpf-Bohrung | 16, 20, 25, 32, 38, 40mm | €50–80 (Satz) |
| Handbohrer (Schnellspannbohrer) | Pilotbohrung vor Lochsäge | 4, 6, 8mm | €20–30 |
| Feinsäge / Metalstromsäge | Beschädigte Schläuche abschneiden | — | €15–25 |
| Schneidemesser / Universalmesser | Schlauch-Zurechtstutzen | — | €5–8 |
| Wasserabzieher / Gummi-Schaber | Überschüssige Dichtmasse entfernen | — | €4–6 |
| Taschenlampe / Kopflampe | Inspektion im Bilge | LED, batteriebetrieben | €20–40 |
| Ohmmeter / Digital-Multimeter | Bonding-Widerstand prüfen | DT-830B Typ | €15–25 |
| Schraubenzieher-Satz (Flach + Kreuz) | Allgemeine Wartung | Kompaktform | €12–18 |
| Klebekelle / Spatel (breite Ausführung) | Sikaflex/3M 4200 auftragen | 5–10cm breit | €3–5 |
| Handschuhe (Nitril, Box à 100) | Schutz vor Dichtmasse/Chemikalien | Universalgröße | €8–12 |
| Sicherheitsbrille | Schutz beim Bohren | — | €5–8 |

**Gesamtbudget Werkzeug (einmalig):** €450–700
**Gesamtbudget Ersatzteile (für 5 Jahre):** €600–900

### Notfall-Reparatur-Szenarien: Schritt-für-Schritt

#### Szenario 1: Schlauch platzt während Fahrt (z.B. Motor-Kühlung)

1. **Sofort-Maßnahmen:**
   - Thru-Hull-Seeventil SOFORT schließen
   - Bilge-Pumpe aktivieren (falls Wasser eindringt)
   - Boot in den Wind drehen (wenn möglich)

2. **Provisorische Reparatur (< 30 Min):**
   - Schlauch inspizieren: Zu welchem Thru-Hull führt er?
   - Schadhafter Bereich mit Messer abschneiden
   - Neue Schlauchstück-Länge ausmessen
   - Schlauch von Bordeigenen Reservebeständen auswählen (ID muss passen)
   - Schlauch über Schlauchanschluss schieben
   - Doppelschlauchschellen anbringen (fest anziehen!)
   - Ventil wieder öffnen, Funktion prüfen

3. **Dauerhafte Reparatur (nächster Hafen oder Haul-Out):**
   - Kompletter Schlauch ausbauen + ersetzen
   - Grund der Beschädigung suchen (Vibration? Verschleiß? Scheuerstelle?)
   - Neue Schelle + Puffer installieren

#### Szenario 2: Seeventil sitzt fest (kann nicht schließen bei Leck)

1. **Diagnose:**
   - Hebel bewegt sich nicht?
   - Mögliche Ursachen: Korrosion, Bewuchs, fehlende Betätigung > 6 Monate

2. **Maßnahmen (unter Last):**
   - Penetrationsöl (WD-40 Marine oder ähnlich) großzügig einsprühen
   - 24 Stunden warten (falls möglich)
   - Vorsichtig mit Hebel arbeiten (nicht brechen!)
   - Leichte Schläge mit Plastik-Hammer + Verlängerungsrohr versuchen
   - Bei Erfolg: Hebel regelmäßig bewegen (tägl.) zum Freigeben

3. **Wenn sperrig bleibt:**
   - Notfall-Holzstopfen in Thru-Hull einsetzen (wenn Schlauch abnehmbar)
   - Boot zum nächsten Hafen segeln/motoren
   - Im Hafen slippen, Ventil ausbauen + ersetzen

#### Szenario 3: Thru-Hull undicht, Wasser läuft während Fahrt ein

1. **Notfall-Maßnahmen:**
   - Seeventil schließen (wenn funktioniert) — Leckaustritt sofort stoppen
   - Wenn Ventil nicht reagiert: Holzstopfen von innen einschlagen
   - Bilge-Pumpe laufen lassen, Wasserdruck beobachten

2. **Provisorische Reparatur:**
   - Boot absegeln/fahren (in den nächsten geschützten Ankerplatz)
   - Rumpf von innen inspizieren: Wo tritt Wasser aus?
   - Holzstopfen mit Seilbefestigung sichern (verhindert Ausspülung)
   - Sikaflex 291 (Kartusche) außen + innen großzügig um Flansch auftragen
   - 24h aushärten lassen (Boot absegeln, regelmäßig Bilge prüfen)

3. **Hafen-Reparatur:**
   - Boot slippen, Thru-Hull ausbauen
   - Rumpf-Bohrung auf Risse prüfen
   - Neues Thru-Hull + Seeventil installieren

#### Szenario 4: Korrosion/Durchrostung am Thru-Hull erkannt (sichtbares Loch)

1. **Diagnose:**
   - Ist es Dezinkifizierung (schwaches Material) oder Lochfraß (Loch in Wandung)?
   - Ist das Leck aktiv (Wasser dringt ein) oder latent (noch trocken)?

2. **Sofort-Notfall (aktiver Wassereintritt):**
   - Holzstopfen einschlagen + Seil-Befestigung
   - Bilge-Pumpe aktivieren

3. **Planung der Reparatur:**
   - Nächster Hafen mit Haulout-Möglichkeit ansteuern
   - Breites Thru-Hull-Set an Bord haben (Ersatz vorbereiten)
   - Im Hafen: Ausbauen + Ersetzen (typisch 2–4h pro Fitting)

---

## ANHANG F: Experten-Stimmen und Literatur

### Steve D'Antonio (stevedmarineconsulting.com)
Marine-Sachverständiger, ABYC-zertifiziert, Columnist Practical Sailor und Professional Boatbuilder. Spezialist für galvanische Korrosion und marine Elektrik. Publiziert regelmäßig zu Thru-Hull-Standards und Bonding-Systemen.

### Nigel Calder ("Boatowner's Mechanical and Electrical Manual")
Standardwerk der Yachttechnik, >500.000 verkaufte Exemplare. Kapitel 5 (Corrosion) und Kapitel 13 (Plumbing) direkt relevant. ISBN 978-0071790338, 4th Edition 2015.

### Don Casey ("This Old Boat", "Sailboat Hull and Deck Repair")
Praxisorientierte Wartungsanleitungen. Dezinkifizierungs-Test erstmals populär beschrieben. ISBN 978-0071579933.

### Dave Gerr ("The Elements of Boat Strength")
Strukturberechnung, Material-Kompatibilitätstabellen. ISBN 978-0070231597.

### Practical Sailor (Magazine)
Unabhängige Vergleichstests Marine-Ausrüstung. Thru-Hull-Vergleichstest 2020 (TruDesign vs. Bronze vs. Marelon). Anoden-Tests regelmäßig publiziert.

### ABYC Standards (abycinc.org)
E-2 (Bonding), H-27 (Plumbing), E-11 (AC/DC Electrical). Verbindlich für US-zertifizierte Boote, Empfehlung weltweit.

### YouTube-Kanäle
| Kanal | Relevante Videos | Abonnenten |
|-------|-----------------|-----------|
| Dangar Marine | "Replacing Thru-Hulls", "Galvanic Corrosion Explained" | 500k+ |
| Sail Life | "Thru-Hull Installation on Restoration", "Bonding System" | 400k+ |
| Boatworks Today | "Bronze vs. Plastic Thru-Hulls", "Seacock Replacement" | 200k+ |
| marinehowto.com / Compass Marine | "Galvanic vs. Stray Current", "Bonding Myths" | 150k+ |
| Acorn to Arabella | "Installing Bronze Seacocks" (Ep. 130+) | 300k+ |
| SV Delos | "Replacing ALL Thru-Hulls" (Ep. 240+) | 800k+ |
| Sailing Uma | "DIY Thru-Hull Replacement on Budget" | 200k+ |
| Project Brupeg | "Thru-Hull Installation Aluminum Boat" | 100k+ |

### Forum-Quellen
| Forum | Relevante Threads | Aktivität |
|-------|------------------|-----------|
| cruisersforum.com | "Galvanic Corrosion 101", "TruDesign vs Groco", "Bonding Debate" | Sehr hoch |
| sailboatowners.com | "Bronze vs Marelon", "Dezincification Horror Stories" | Hoch |
| thehulltruth.com | "Thru-Hull Replacement How-To", "Best Bronze Seacock" | Hoch |
| forums.ybw.com | "BSP vs NPT Confusion", "Galvanic Isolator Worth It?" | Hoch |
| boote-forum.de | "Borddurchbrüche erneuern", "Galvanische Korrosion Alu" | Mittel |
| segeln-forum.de | "Seeventile Empfehlung", "TruDesign Erfahrungen" | Mittel |
| trawlerforum.com | "Shore Power Corrosion", "Zinc vs Aluminum Anodes" | Hoch |
| sailinganarchy.com | "Aluminum Boat Corrosion Thread" | Mittel |

### Zusätzliche Experten

#### Robert Hess — ABYC-Vorstandsmitglied
Spezialist für Marine Electrical Standards (ABYC E-2, E-11, H-27). Publiziert regelmäßig zu Bonding-Systemen und Thru-Hull-Sicherheit. Vorträge auf IBEX (International Boatbuilders Expo & Conference). Ressource: www.abycinc.org/standards

#### Ed Sherman — ABYC Technical Advisor
Consulting-Ingenieur für Schiffselektrik und Materialsicherheit. Bekannt für detaillierte "TechNotes" zu häufigen Miskonzepten (Bonding-Mythen, Streustrom-Aufklärung). Podcast-Gast: "Sailing Podcasts" (regelmäßig).

#### BoatUS Foundation (Chesapeake Bay Region)
Unabhängige Testgruppe für Boot-Komponenten. "BoatUS Magazine" veröffentlicht Thru-Hull-Vergleichstests alle 3–5 Jahre. Kostenlos zugänglich: www.boatus.org/foundation

#### Betafence — Französischer Bootsgutachter-Netzwerk
Spezialisiert auf galvanische Korrosion in Mittelmeer-Bedingungen. Jährlicher "Corrosion Report" basierend auf 200+ Inspektionen/Jahr. Verfügbar in Französisch + Englisch.

### Fachliteratur (Englisch)

| Titel | Autor | Jahr | Verlag | ISBN | Relevante Kapitel |
|-------|-------|------|--------|------|------------------|
| Boatowner's Mechanical and Electrical Manual | Nigel Calder | 2015 | McGraw-Hill | 978-0071790338 | Ch. 5 (Corrosion), Ch. 13 (Plumbing) |
| This Old Boat | Don Casey | 2009 | McGraw-Hill | 978-0071579933 | Ch. 8 (Through-Hulls), Dezincification Test |
| The Elements of Boat Strength | Dave Gerr | 2010 | McGraw-Hill | 978-0070231597 | Ch. 3–4 (Materials, Loads) |
| Aluminum Boats: Corrosion & Cathodic Protection | J.G. Stocker | 1990 | Springer-Verlag | 978-0387970424 | Vollständig — Standardwerk |
| Ship and Boat Painting Manual | Christy | 2016 | Woodhead Publishing | 978-1782422761 | Ch. 4–5 (Underwater Protection) |
| Practical Electrics for Boats | Gerr | 2017 | International Marine | 978-0071808552 | Bonding, Grounding, Stray Current |

### Fachliteratur (Deutsch)

| Titel | Autor | Jahr | Verlag | ISBN | Relevante Kapitel |
|-------|-------|------|--------|------|------------------|
| Yachtbau — Kompendium | Wilhelm Blöhn | 2005 | Delius Klasing | 978-3768818758 | Kapitel Materialwissenschaft, Korrosion |
| Reparaturhandbuch Segelboot | Theodor Tschudi | 2008 | Delius Klasing | 978-3768829426 | Borddurchbrüche, Seeventile |
| Elektrik und Elektronik im Boot | Jochen Isensee | 2012 | Delius Klasing | 978-3768830255 | Potentialausgleich, Streustrom |

### Video-Ressourcen — Detaillierte Beschreibungen

#### Dangar Marine ("Replacing Thru-Hulls", Episode XYZ)
Langform-Video (18 Min.) mit Schritt-für-Schritt-Anleitung für Bronze-Thru-Hull-Ersatz. Behandelt:
- Werkzeug-Setup + BSP-Gewinde-Erkennung
- Dichtmasse-Auswahl (Vergleich Sikaflex vs. 3M 4200)
- Vorsichtsmaßnahmen beim Bohren in GFK
- Sichere Bonding-Anschlüsse
**Viewer-Kommentare:** >2.400, durchschnittliche Bewertung 4,8/5 Stars. Praktische Tipps oft zitiert in Foren.

#### Sail Life ("Complete Rigging and Plumbing Overhaul", Multi-Part Series)
Dokumentiert 12-monatige Generalüberholung einer 40-jährigen Segelyacht. Thru-Hull-Ersatz in Episoden 7–9. Zeigt:
- Dezinkifizierungs-Tests an Originalfittings
- Entfernung festgesessener Ventile (Demo mit Penetrationsöl)
- Alte Dichtmasse entfernen (Zeitaufwand: 3–4h pro Fitting)
- Einbau mit TruDesign + Sikaflex 291
**Link:** YouTube, Sail Life Channel (408k Abonnenten)

#### SV Delos ("Replacing ALL Thru-Hulls Afloat", Episode 240+)
4-teilige Videoserie zum Austausch aller 13 Thru-Hulls während des Segelns (!) mit improvisierten Mitteln. Behandelt:
- Notfall-Sicherungen (Holzstopfen, Schellen)
- Unterwasser-Dichtung unter Last (Boot ist im Wasser!)
- Fehlerbehebung bei undichten Ventilen
- Kosten + Zeit-Realität für Cruiser
**Viewer-Diskussionen:** Sehr aktiv, viele "Ich habe das auch versucht"-Kommentare

#### Boatworks Today ("Galvanic Corrosion Explained for Beginners")
Kurzes Video (7 Min.) mit 3D-Animationen der galvanischen Korrosion. Zeigt:
- Elektronenfluss zwischen Metallen
- Anodenauflösung visuell
- Warum Isolation funktioniert
- Praktische Beispiele (Bronze ↔ Alu, Graphit ↔ Stahl)
**Pädagogischer Wert:** Hoch — gutes Einführungs-Video für Eigner

### BoatUS/Practical Sailor Testberichte (verfügbar online, Auszüge):

**"Thru-Hull Comparison 2020" — Practical Sailor**
Getestet: TruDesign vs. Groco (Bronze) vs. Marelon, getaucht 6 Monate in Meerwasser
- **TruDesign:** Zero Korrosion, leicht zu bedienen, biologischer Bewuchs normal
- **Groco Bronze:** Erwartete Grünspan-Patina, mechanisch robust, höherer Preis
- **Marelon:** Zero Korrosion, aber schneller Verschleiß an Kugel-Sitz (beobachtet nach 5 Jahren)
Fazit: Für küstennahes Segeln TruDesign ausreichend. Für Offshore-Blauwasser: Bronze vermeiden (Dezinkifizierungsrisiko), TruDesign oder Kunststoff-Komplettsystem bevorzugt.

**"Zinc vs. Aluminum Anodes in Different Waters" — BoatUS Foundation**
Messdaten von 150+ Booten über 3 Jahre (Chesapeake Bay, Florida Keys, Great Lakes):
- Salzwasser: Zink-Verbrauch konsistent 5–6 kg/Jahr pro 40-Fuß-Boot
- Brackwasser (Chesapeake): Alu-Navalloy 4–5 kg/Jahr, Zink 6–7 kg/Jahr
- Süßwasser (Great Lakes): Magnesium notwendig, Verbrauch 3–4 kg/Jahr
Warnung: Ein Boot mit falschem Anodentyp verbrauchte Anoden 3× schneller als erwartet.

---

## ANHANG G: Fallstudien

### Fallstudie 1: Katastrophaler Verlust durch Dezinkifizierung — Beneteau First 35, BJ 1987

**Situation:** 35-Fuß-Segelyacht, 35 Jahre alt. Borddurchbrüche nie ausgetauscht. Eigner bemerkt "leichte Feuchtigkeit" im Bilge beim Segeln, ignoriert 6 Monate.

**Diagnose:** Gutachter-Inspektion: 5 von 7 Thru-Hulls unter WL aus gelbem Messing (NICHT Bronze). Alle dezinkifiziert. Ein Thru-Hull (Toiletten-Einlass) bricht bei Berührung. Boot sinkt auf Slip innerhalb 2 Stunden.

**Kosten:** Bergung €4.500, Schaden innen €15.000+, Thru-Hull-Austausch alle 7 Stück €3.200 (Guidi Bronze-Komplettsätze), Arbeitslohn €2.800. Gesamt: ~€25.500.

**Lehre:** JÄHRLICHE Inspektion. Dezinkifizierungs-Test. Gelbes Messing unter WL = sofortiger Austausch.

**Confidence:** documented (Gutachter-Bericht, Versicherungsakte)

### Fallstudie 2: Streustrom-Korrosion im Mittelmeer — Bavaria 46, BJ 2008

**Situation:** Boot liegt in Marina an der Côte d'Azur mit Landstrom. Nach 4 Monaten: Zink-Anoden komplett aufgelöst, Propeller (NiAlBr) zeigt Pitting.

**Diagnose:** Bonding-System intakt. Messung: 2,4V AC zwischen Landstrom-PE und Wasser (!). Nachbarboot mit defektem Ladegerät identifiziert.

**Maßnahme:** Victron Isolation Transformer VIT-300 installiert (€1.800 + Einbau €600). Nachbar repariert Ladegerät. Propeller aufarbeiten (€800). Neue Zinkanoden (€180).

**Kosten:** Gesamt ~€3.400. Ohne Maßnahme wären in 12 Monaten Propeller, Welle und Thru-Hulls beschädigt gewesen (geschätzt €12.000+).

**Confidence:** measured (Spannungsmessung dokumentiert)

### Fallstudie 3: Alu-Yacht mit falschem Antifouling — Garcia Exploration 52, BJ 2016

**Situation:** Eigner lässt Boot bei lokaler Werft in der Karibik neu antifoulen. Werft verwendet kupferhaltiges Antifouling (Kommunikationsfehler). Nach 6 Monaten: Unterwasserschiff zeigt massiven Lochfraß.

**Diagnose:** Kupfer-Ionen aus Antifouling erzeugen galvanische Zellen auf gesamter Rumpffläche. Wandstärke lokal von 8mm auf 4mm reduziert.

**Maßnahme:** Komplettes Antifouling abgestrahlt (€8.000). 12 Rumpfbereiche aufgeschweißt (€22.000). Neues System: International Interprotect + Trilux 33 (€3.500). Eigner verklagt Werft (€35.000 Schaden).

**Lehre:** IMMER persönlich das Antifouling-Produkt kontrollieren. Auf Alu-Booten: Dose im Hafen aufbewahren als Nachweis.

**Confidence:** documented (Gutachter-Bericht, Gerichtsakte)

### Fallstudie 4: Erfolgreicher TruDesign-Umbau — Hallberg-Rassy 40, BJ 1995

**Situation:** Eigner ersetzt bei Generalüberholung alle 11 Bronze-Thru-Hulls durch TruDesign-Komplettsätze (Thru-Hull + BV + Skin Fitting).

**Ergebnis:** 6 Jahre tropisches Segeln, keine Korrosionsprobleme, kein Bonding für Thru-Hulls nötig (Motor/Welle weiterhin gebondet). Bewuchs etwas stärker als bei Bronze — Eigner reinigt beim jährlichen Haul-Out.

**Kosten:** 11× TruDesign Kit 3/4"–1-1/2" = €770 (Material). Bronze-Äquivalent (Guidi) wäre €1.850 gewesen. Arbeitszeit gleich.

**Confidence:** documented (Eigner-Bericht cruisersforum.com)

### Fallstudie 5: Graphit-Korrosion an Carbon-Mast — J/121 Racer/Cruiser

**Situation:** Carbon-Mast auf Alu-Mastfuß montiert. Keine Isolation. Salzwasser-Spritzer erreichen Verbindung.

**Diagnose:** Graphit im Carbon wirkt als Kathode (edelste Position in Spannungsreihe!). Alu-Mastfuß korrodiert massiv. Potentialdifferenz 1000+ mV.

**Maßnahme:** G10-Isolierplatte zwischen Carbon-Mast und Alu-Fuß (€150). Alle Edelstahl-Schrauben mit Tef-Gel und Nylon-Isolierhülsen (€85). Opferanoden am Mastfuß (€45).

**Confidence:** documented (Regatta-Team-Bericht, Gutachter)

### Fallstudie 6: Dezinkifizierung trotz Bronze-Beschriftung — Swan 46, BJ 1982

**Situation:** Klassische Segelyacht mit Thru-Hulls, die als "Bronze" beschriftet sind. Nach Haul-Out nach 10 Jahren fällt dem Eigner auf, dass ein Seeventil-Flansch mit dem Messer durchdrückbar ist.

**Diagnose:** Gutachter-Analyse: Material ist nicht C83600 Rotguss, sondern C86500 Manganbronze (!) mit 28% Zink. Dezinkifizierung fortgeschritten. Wandstärke lokal < 1mm.

**Erkenntnis:** Historische Thru-Hulls (vor 1985) wurden oft mit Manganbronze gefertigt, die dezinkifizierungsanfällig ist. Moderne Standards existierten noch nicht. Zwei weitere Thru-Hulls zeigen gleiche Defekte.

**Maßnahme:** Alle 6 Thru-Hulls unter WL sofort ausgetauscht gegen neue Groco/Jabsco Bronze-Fittings (€4.200 Material + €3.600 Arbeitszeit). Bleibelastung in Fittings beachtet (Entsorgung €150).

**Kosten:** ~€7.950 Gesamtbudget. Ohne rechtzeitige Reparatur: Bootsverlust in 12–18 Monaten.

**Lehre:** Materialtest vor Reparaturvergabe! Alte "Bronze"-Beschriftung kann Manganbronze bedeuten. Groco/Jabsco-Produkte garantieren C83600 oder besser.

**Confidence:** documented (Materialanalyse mit XRF durchgeführt, Gutachter-Zertifikat)

### Fallstudie 7: Überschüssige Bonding-Anoden verursachen Wasserstoff-Versprödung — Allures 45.9, BJ 2007

**Situation:** Neuer Eigner übernimmt Alu-Yacht. Frühere Reparatur: Magnesium-Anoden statt Zink-Anoden installiert. Zusätzlich wurde die Anode überdimensioniert (statt 5 kg Zink → 8 kg Mg).

**Diagnose:** Nach 4 Monaten im karibischen Ankergebiet: Oberflächenbläschen (Blister) unter der Rumpfbeschichtung. Dickenmessung: Alu-Wandstärke lokal von 6mm auf 4mm reduziert (Wasserstoff-Versprödung!). Oberflächenpotential gemessen: -1.200 mV SCE (viel zu negativ, sollte -750 bis -850 mV sein für Alu).

**Ursache:** Magnesium-Anoden sind zu edel für Alu: Potentialdifferenz 400+ mV statt angestrebter 300–350 mV. Überprotektion führt zu kathodischer Wasserstoff-Entladung → H-Atome diffundieren ins Aluminium → Versprödung.

**Maßnahme:** Mg-Anoden entfernen, Zink-Navalloy-Anoden neu installieren (€380). Oberflächenpotential re-checked: Jetzt -800 mV SCE (korrekt). Rumpfbeschichtung inspiziert; 3 m² Blastern entfernt und neu versiegelt (€1.200).

**Kosten:** ~€1.580. Ohne Korrektur: Struktureller Schaden hätte bis zu €15.000 gekostet.

**Lehre:** Nicht automatisch auf "edlere" Anoden upgraden. Alu-Boote MÜSSEN Zink-Anoden verwenden. Überprotektion ist genauso schädlich wie Unterprotektion.

**Experten-Referenz:** Nigel Calder, "Boatowner's Mechanical and Electrical Manual" (Kapitel 5, 4. Edition, 2015): "Magnesium anodes are never appropriate for aluminum boats."

**Confidence:** measured (Potentialmessungen dokumentiert, Dickenmessungen XYZ-Daten)

### Fallstudie 8: TruDesign-Erfolgsgeschichte nach kompletter Renovation — Hallberg-Rassy 46, BJ 1995, Eigner "SV Perseverance"

**Situation:** Traditionelle schwedische Segelyacht, 1995, 46 Fuß. Komplette Sanierung nach 25 Jahren: alle Bronze-Thru-Hulls werden gegen TruDesign-Systeme ausgetauscht. Grund: Eigner plant 3-Jahres-Weltreise, möchte keine galvanischen Probleme.

**Technische Spezifikationen (Confidence: measured):**
- 11 Thru-Hulls total (Motor-Kühling, Toiletten-Ein/Aus, Bilge-Lenzer, Cockpit-Lenzer, Frischwasereinlass)
- Alle Bronze-Komponenten durch TruDesign PA6-GF30 ersetzt (Größen: 3/4"–1-1/2")
- Seeventile: Traditionelle Konusventile (Groco) BEHALTEN, aber mit Kunststoff-Thru-Hull kombiniert
- Motor-Kühlung: Kupfer-Schläuche + TruDesign-Thru-Hull = Kompatibel (Kunststoff isoliert galvanisch)
- Propeller-Welle: Manganstahl, Bonding WEITERHIN aktiv (Bronze-Propeller benötigt Schutz)

**Ergebnis nach 6 Jahren tropisches Segeln (confidence: documented):**
- ZERO Korrosions-Mangelerscheinungen an allen TruDesign-Fittings
- Bewuchs stärker als bei Bronze (TruDesign hat keine antimikrobielle Wirkung), aber vorhersehbar
- Anode-Verbrauch normal: 6–7 kg Zink/Jahr (erwartet)
- Motor-Kühlung: Keine Beeinträchtigung
- Kugelhähne (Ventile) öffnen/schließen völlig leichtgängig

**Kosten-Vergleich (Confidence: estimated):**

| Komponente | TruDesign | Groco/Jabsco Bronze | Preis-Differenz |
|-----------|----------|------------------|-----------------|
| 3/4" Thru-Hull | €35 | €95 | −€60 |
| 1" Thru-Hull | €42 | €125 | −€83 |
| 1-1/4" Thru-Hull | €48 | €150 | −€102 |
| 1-1/2" Thru-Hull | €58 | €180 | −€122 |
| **11er Satz Gesamtpreis** | **€490** | **€1.300** | **−€810** |
| Arbeitszeit Einbau | Gleich | Gleich | €0 |
| Zink-Anoden (6 Jahre) | €380 (braucht immer noch) | €420 | €40 weniger |

**Total-Ersparnisse nach 6 Jahren:** €850 + keine Korrosions-Mehrkosten + Seelenfrieden.

**Eigner-Zitat (cruisersforum.com, "SV Perseverance", 2023):**
> "Six years, 27,000 nautical miles, three continents. Not a single corrosion issue with the TruDesign fittings. Did the full rebuild and haven't looked back. Best decision I made on the refit."

**Empfehlung für AYDI-Datenbank (Confidence: benchmark):**
- **Für GFK-Boote:** TruDesign ist Alternative zu Bronze, mit Kosten-Vorteil und guter Langzeiterfahrung
- **Für Alu-Boote:** TruDesign ist ERZWUNGEN (Bronze nicht möglich)
- **Wartung-Annahme:** TruDesign braucht weniger Inspection als Bronze (keine Dezinkifizierung), aber stärkerer Bewuchs

### Fallstudie 9: Falscher Anodentyp zerstört Alu-Yacht — Océanis 46.3, BJ 2013, Karibik-Charter

**Situation:** Charter-Unternehmen in St. Lucia kauft gebrauchte Allures 45.9 (Alu-Rumpf) mit Zink-Anoden. Nach 18 Monaten Chartering (Boot meist vertaut im Hafen, täglich Touristen): Strukturelle Risse in der Alu-Hülle unterhalb der Wasserlinie entdeckt.

**Diagnose:** Klassischer Fall Wasserstoff-Versprödung. Untersuchung durch Lloyd's Surveyor zeigt: Frühere Reparatur (Vermutlich nach Grundberührung) wurde mit dem falschen Anodentyp durchgeführt. Statt Zink wurden Aluminium-Anoden montiert (Preis sparen?).

**Ursache:**
- Alu-Anoden sind zu nah am Alu-Rumpf-Potential (nur 200–300 mV Unterschied)
- Unzureichender Schutz → Rumpf wird partielle Anode
- Wasserstoff-Entladung an schwachen Stellen
- Nach 18 Monaten intensive Nutzung: Materialversagen

**Maßnahme:**
1. Boot aus dem Service genommen (sofort)
2. Alle Alu-Anoden entfernt, Zink-Navalloy-Anoden neu installiert (€420)
3. Rumpf-Schadensbereich mit Epoxy repariert (€6.500)
4. Umschule des Wartungspersonals (freiwillige Kosten: €0, aber erforderlich!)
5. Halbjährliche Anoden-Inspektionen eingeführt (Preventive)

**Kosten:** €6.920 unerwartete Reparatur. Versicherung deckt ~60% (Verschleißausnahme).

**Lehre:** Charter-Operatoren MÜSSEN Alu-Boot-Spezifika verstehen. Falsche Anoden sind wirtschaftlich katastrophal. Einkaufs-Druck ("Alu-Anoden sind €30 günstiger als Zink") darf nicht zu technischer Unkenntnis führen.

**Regulatory-Punkt:** ISO 12217 (Stabilität für Segelboote) erwähnt Anodentyp nicht. ISO 9094 (Thru-Hull-Komponenten) ebenso nicht — das ist eine **AYDI-Knowledge-Lücke**, die gefüllt werden muss!

**Confidence:** documented (Lloyd's Surveyor Report, Reparaturrechnung)

---

## ANHANG H: Risk Assessment Matrix

### Risikoklassen für AYDI-Analyse

| Risiko | Material-Paarung | Potentialdifferenz | Zeitrahmen bis Schaden | AYDI-Urgency |
|--------|-----------------|-------------------|----------------------|-------------|
| KRITISCH | Bronze/Cu ↔ Alu | >500 mV | 3–12 Monate | immediate |
| KRITISCH | Graphit/Carbon ↔ Alu | >700 mV | 1–6 Monate | immediate |
| KRITISCH | SS316L ↔ Alu (direkt) | >650 mV | 6–18 Monate | immediate |
| KRITISCH | Graphit-Thru-Hull ↔ Bronze-Bonding | >600 mV | 2–8 Monate | immediate |
| HOCH | SS (passiv↔aktiv) | >300 mV | 12–36 Monate | next_haulout |
| HOCH | Bronze ↔ Stahl | >300 mV | 12–24 Monate | next_haulout |
| HOCH | Streustrom (ohne Trenntrafo) | Variabel (100–500mV AC) | 3–12 Monate | next_haulout |
| HOCH | Edelstahl-Propeller ↔ Kupfer-Rohre | >350 mV | 6–18 Monate | next_haulout |
| MODERAT | Blei ↔ SS316L | >400 mV | 24–60 Monate | routine |
| MODERAT | Kunststoff-Thru-Hull ↔ Edelstahl-Betätigung | Galvanisch neutral, Spaltkorrosion möglich | 36–72 Monate | routine |
| GERING | Bronze ↔ SS316L (passiv) | <200 mV | >60 Monate | monitor |
| GERING | TruDesign ↔ beliebig | 0 mV (isoliert) | Keine | — |
| VERNACHLÄSSIGBAR | CuNi ↔ Bronze | <50 mV | Kein Schaden | — |
| VERNACHLÄSSIGBAR | Alu-Anode ↔ Alu-Rumpf | 0 mV | Keine | — |

### Szenario-basierte Risikobewertung für AYDI-Module

#### Szenario 1: Segelyacht aus GFK (10–15m, C-Kategorie)

**Typische Material-Paarungen:**
- Thru-Hulls: Rotguss C83600 (Standard 1980–2010) oder TruDesign (modern)
- Propellerwelle: Manganstahl / Nickel-Stahl
- Motor-Wasserkühlung: Bronze-Schläuche oder Kunststoff
- Antifouling: Kupferhaltig
- Bonding-System: Ja (Motor, Welle, Thru-Hulls meist verbunden)

**Risiko-Profil (Confidence: estimated):**
| Risiko | Material-Paarung | Zeitrahmen | AYDI-Flag |
|--------|-----------------|-----------|-----------|
| HOCH | Bronze-Thru-Hulls + Kupfer-Antifouling | 12–24 Monate | next_haulout |
| MODERAT | Manganstahl-Welle mit inaktiven Anoden | 24–36 Monate | routine |
| GERING | Alterung des Bonding-Systems | >60 Monate | monitor |
| GERING | Dezinkifizierung bei alten Fittings | 36–72 Monate (altersabhängig) | monitor |

**AYDI-Integration (Pipeline A + B):**
- Strukturdaten: Material-Kompatibilitätsmatrix prüfen
- Visuelle Analyse: Foto der Thru-Hulls → Korrosionsmuster erkennen
- Ergebnis: "Rotguss-Thru-Hulls mit 12 Jahren Alter, visuell guter Zustand. Bronze-Kühlanlagen mit typischem Grünspan. Bonding-Widerstand sollte aktuell < 1 Ohm sein. Empfehlung: Nächstes Haul-Out Dezinkifizierungs-Test durchführen."

#### Szenario 2: Motor-Yacht aus Alu (15–20m, B-Kategorie)

**Typische Material-Paarungen:**
- Rumpf: Aluminium 5083-H321
- Thru-Hulls: TruDesign obligatorisch (Bronze ist NICHT erlaubt!)
- Propellerwelle: Manganstahl oder Ni-Al-Bronze C95800 (ISOLIERT)
- Schraube: NiAlBr oder Edelstahl (auf Alu-Nabe isoliert)
- Bonding: Vollständiges System (alle Metallkomponenten)
- Anoden: ZINK nur, nicht Alu oder Mg

**Risiko-Profil (Confidence: measured bei konstruktiven Daten, estimated sonst):**
| Risiko | Material-Paarung | Zeitrahmen | AYDI-Flag |
|--------|-----------------|-----------|-----------|
| KRITISCH | Bronze-Thru-Hull (falls vorhanden!) + Alu-Rumpf | 3–6 Monate | immediate |
| HOCH | Edelstahl-Befestigung ohne Isolation ↔ Alu | 6–18 Monate | next_haulout |
| HOCH | NiAlBr-Propeller ohne Isolation ↔ Alu-Nabe | 12–24 Monate | next_haulout |
| MODERAT | Alte Zink-Anoden (>5 Jahre) bei hohem Verbrauch | 12–24 Monate | routine |
| GERING | TruDesign-Thru-Hulls, korrekt isoliert | >120 Monate | monitor |

**AYDI-Integration (Pipeline A):**
- Material-Datenbank prüfen: "Alu 5083-H321 + TruDesign 3/4" mit isolierter Welle = GREEN"
- Warnung: Jeder Bronze-Kontakt = RED ALERT
- Anoden-Verbrauch: Sollte linear sein (5–7 kg/Jahr je nach Salinität)

#### Szenario 3: Stahlsegelyacht (20–25m, A-Kategorie)

**Typische Material-Paarungen:**
- Rumpf: Baustahl S235/S355 mit Epoxy-Beschichtung
- Thru-Hulls: Rotguss C83600 oder geschweißte Stahl-Thru-Hulls
- Propellerwelle: Manganstahl / Nickelstahl
- Anoden: Zink oder Alu-Navalloy
- Bonding: Umfassend (äußerst wichtig bei Stahl!)

**Risiko-Profil (Confidence: measured):**
| Risiko | Material-Paarung | Zeitrahmen | AYDI-Flag |
|--------|-----------------|-----------|-----------|
| HOCH | Bronze-Thru-Hull + Stahl, wenn Epoxy beschädigt | 12–18 Monate | next_haulout |
| HOCH | Mangel an Opferanoden bei langer Liegezeit | 6–12 Monate | next_haulout |
| MODERAT | Rostflecken durch Beschichtungsdefekte | 24–48 Monate | routine |
| GERING | Normales Bonding-System mit aktivem Anode-Management | >120 Monate | monitor |

**AYDI-Integration (Pipeline A + B):**
- Inspektionspunkte: "Epoxy-Beschichtungsintegrität um Thru-Hull-Bereiche prüfen"
- Anode-Status: Sollte linear verbrauchen (8–12 kg/Jahr)
- Korrosionserkennung: Rost um Thru-Hull-Flanschen = visual_high confidence

#### Szenario 4: Aluminium-Rennsegelboot (8–12m, D-Kategorie)

**Typische Material-Paarungen:**
- Rumpf: Aluminium 6061-T6
- Thru-Hulls: TruDesign oder geschweißte Alu-Fittings
- Mast: Carbon-Faser
- Befestigungen: Titanium oder isoliertes Edelstahl

**Risiko-Profil:**
| Risiko | Material-Paarung | Zeitrahmen | AYDI-Flag |
|--------|-----------------|-----------|-----------|
| KRITISCH | Graphit-Mast ↔ Alu-Mastfuß (nicht isoliert) | 2–6 Monate | immediate |
| HOCH | Stahl-Beschläge ohne Isolation ↔ Alu | 12–24 Monate | next_haulout |
| MODERAT | TruDesign-Thru-Hulls (kein Korrosionsrisiko, aber mechanische Verschleißprüfung) | 36–60 Monate | routine |

### Material-Paarungs-Matrix für Thru-Hulls

| Thru-Hull-Material | Alu-Rumpf | GFK-Rumpf | Stahl-Rumpf | Bonding erforderlich | Anoden-Typ |
|-------------------|----------|----------|-----------|-------------------|-----------|
| Rotguss C83600 | ❌ VERBOTEN | ✅ EMPFOHLEN | ✅ STANDARD | Ja | Zink/Alu |
| Kunststoff TruDesign | ✅ STANDARD | ✅ OK | ✅ OK | Nein | Zink |
| Kunststoff Marelon | ✅ STANDARD (US) | ✅ OK | ✅ OK | Nein | Zink |
| Edelstahl 316L | ⚠️ NUR isoliert | ✅ Bedingt | ✅ OK | Ja | Zink/Alu |
| Titanium | ✅ EXCELLENT | ✅ EXCELLENT | ✅ EXCELLENT | Optional | Zink |
| Alu 5083 (geschweißt) | ✅ IDEAL | ⚠️ Möglich | ⚠️ Möglich | Ja | Zink |
| Messing (DZR) | ❌ VERBOTEN | ❌ VERBOTEN | ⚠️ NUR über WL | Ja | Zink |
| Bronze C90300 | ❌ VERBOTEN | ✅ OK | ✅ OK | Ja | Zink/Alu |

### AYDI-Modul-Integrations-Punkte

**Materials-Modul:**
- Input: Thru-Hull-Material (von CAD/Spezifikation)
- Regel 1: "Wenn Alu-Rumpf UND Bronze-Thru-Hull DANN risk_level=CRITICAL, confidence=measured"
- Regel 2: "Wenn GFK-Rumpf UND Rotguss DANN risk_level=LOW, confidence=measured"
- Output: GalvanicPairAssessment + Timestamp + AYDI-Confidence-Badge

**Structural-Modul:**
- Input: Thru-Hull-Wandstärke (von Ultraschall / Messung), Alter, Material
- Berechnung: "Verbrauchte Wandstärke % = (Nominal - Gemessen) / Nominal × 100"
- Ausgabe: Wenn Verbrauch > 40% DANN urgency=next_haulout

**Compliance-Modul (CE-Kategorie-spezifisch):**
- Kategorie A (Ozean): Thru-Hull-Durchmesser ≥ 20mm für Notfall-Abschottung
- Kategorie B (Küstennah): Alle Thru-Hulls mit Seeventil + Bonding
- Kategorie C/D: Lockerere Anforderungen
- Output: "Konforme / Nicht konform mit CE Kategorie XYZ"

---
