# 06.07 — Hydraulikschläuche (Ruder/Winschen/Stabilisatoren)

> **Dokumentversion:** 2.1
> **Letzte Aktualisierung:** 2026-04-23
> **Autor:** AYDI Knowledge Engineering
> **Geltungsbereich:** Alle Hydrauliksysteme auf Yachten 6–60 m (Ruderanlagen, Winschen, Stabilisatoren, Bug-/Heckstrahlruder, Trimmklappen, Kräne, Passerellen, Davits)
> **Sprache Fachtext:** Deutsch | **Code:** Englisch
> **Maßeinheiten:** mm, bar, °C, EUR, Scores 0–100

---

## Einführung & Regulatorischer Rahmen

### Sicherheitskritische Bedeutung

Hydraulikschläuche gehören zu den **sicherheitskritischsten Komponenten** auf einer Yacht. Ein Versagen der Ruderhydraulik führt unmittelbar zum Verlust der Steuerungsfähigkeit — ein Szenario, das gemäß SOLAS-Regularien als **Worst-Case-Ereignis** klassifiziert wird. Auf See, insbesondere bei schwerer See oder in verkehrsreichen Gewässern, kann ein Lenkversagen lebensbedrohlich sein.

Im Gegensatz zu Motorschläuchen, deren Versagen primär Umwelt- und Brandrisiken erzeugt, betreffen Hydraulikschläuche in Ruderanlagen direkt die **Manövrierfähigkeit**. Die CE-Richtlinie 2013/53/EU klassifiziert Ruderanlagen als **wesentliche Sicherheitsbauteile** der Kategorie I.

### Regulatorische Anforderungen

#### CE-Richtlinie 2013/53/EU (Recreational Craft Directive)
- **Anhang I, Abschnitt 3.3**: Steuersysteme müssen unter allen vorhersehbaren Betriebsbedingungen funktionsfähig bleiben
- **Anhang I, Abschnitt 5.1.3**: Hydrauliksysteme müssen gegen Überdruck geschützt sein
- **Redundanzanforderung Kat. A/B**: Yachten >12 m LOA mit Hydrauliksteuerung benötigen Notsteuerung

#### ISO-Normen

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 1436:2017 | Gummischläuche und -schlauchleitungen — Drahtgeflechtverstärkte Hydraulikschläuche | Grundnorm Schlauchkonstruktion |
| ISO 4079:2017 | Gummischläuche — Textilverstärkte Hydraulikschläuche | Niederdruckschläuche |
| ISO 6605:2017 | Hydraulik-Prüfverfahren für Schläuche | Prüfmethodik |
| ISO 6803:2017 | Impulsprüfung für Schläuche | Lebensdauerprüfung |
| ISO 3862:2020 | Gummischläuche — Spiralverstärkt | Hochdruckschläuche |

#### SAE-Standards

| Standard | Titel | Relevanz |
|----------|-------|----------|
| SAE J517 | Hydraulic Hose (100R series) | Hauptklassifikation aller Schlauchtypen |
| SAE J1942:2016 | Hose and Hose Assemblies for Marine Applications | **Marine-spezifische Norm** |
| SAE J343 | Test and Test Procedures for SAE 100R Series | Prüfverfahren |
| SAE J1065 | Pressure Ratings for Hydraulic Tubing | Rohrleitungsdrücke |

#### DIN EN-Normen

| Norm | Titel | Anwendung |
|------|-------|-----------|
| DIN EN 853:2015 | Drahtgeflechtverstärkte Schläuche 1SN/2SN | Standard-Hydraulikschläuche |
| DIN EN 854:2015 | Textilverstärkte Schläuche 1TE/2TE/3TE | Niederdruckleitungen |
| DIN EN 856:2015 | Spiralverstärkte Schläuche 4SP/4SH | Hochdruckleitungen |
| DIN EN 857:2015 | Kompaktschläuche 1SC/2SC | Enge Einbauräume |

#### Klassifikationsgesellschaften

**DNV-GL (Det Norske Veritas — Germanischer Lloyd):**
- Rules for Classification — Pt.4 Ch.6 Sec.5: Piping systems
- Hydraulikschläuche auf klassifizierten Yachten müssen DNV-GL-typgeprüft sein
- Jährliche Inspektion bei Klasse-Yachten obligatorisch
- Schlauchlebensdauer max. 6 Jahre (unabhängig vom Zustand) bei Klasse

**Lloyd's Register (LR):**
- Rules for Special Service Craft, Part 10: Steering
- LR-zertifizierte Schläuche tragen LR Type Approval-Nummer
- Spezifische Anforderungen an Brandschutz bei Maschinenraum-Verlegung

**RINA (Registro Italiano Navale):**
- Regolamento per la Classificazione delle Navi
- Akzeptiert DNV-GL-zugelassene Schläuche in den meisten Fällen

#### ABYC-Standards (American Boat & Yacht Council)

| Standard | Titel | Kerninhalt |
|----------|-------|------------|
| ABYC H-32 | Hydraulic Systems | Schlauchauswahl, Verlegung, Prüfung |
| ABYC P-21 | Hydraulic Steering Systems | Spezifisch für Ruderhydraulik |
| ABYC P-1 | Installation of Exhaust Systems | Abstände Schlauch↔Abgas |
| ABYC E-11 | AC & DC Electrical | Abstände Schlauch↔Elektrik |

> ⚠️ **ZU PRÜFEN (Audit):** Die durchgängige Zuordnung „ABYC H-32 = Hydraulic Systems" (in diesem Dokument ~11×, inkl. Unterabschnitte 32.5–32.8) ist normseitig falsch. **ABYC H-32** ist tatsächlich „Ventilation of Boats Using Diesel Fuel"; der einschlägige ABYC-Standard für Hydrauliksysteme ist **ABYC H-30 (Hydraulic Systems)**. Empfehlung: alle „H-32"-Verweise auf **H-30** umstellen — nicht automatisiert geändert, da die Unterabschnitts­nummerierung von H-30 (30.x) nicht verifiziert werden konnte und ein Teil-Sweep neue Inkonsistenzen erzeugen würde. Quelle: ABYC Standards List (abycinc.org).

**ABYC H-32 Kernanforderungen:**
- Arbeitsdruck ≥ 4× Betriebsdruck (Berstdruck ≥ 4× Arbeitsdruck ist SAE-Standard)
- Schläuche müssen gegen Scheuern geschützt verlegt werden
- Mindestbiegeradius des Herstellers muss eingehalten werden
- Feuerfeste Schläuche im Maschinenraum (30 min Brandbeständigkeit)
- Schläuche dürfen nicht als tragende Elemente verwendet werden

---

## Zukunftstechnologien

### Digitale Schlauchüberwachung (Smart Hoses)

**Parker IoT-Hydraulik (ab 2024):**
- **SensoControl SCM**: Drucksensoren inline, Bluetooth-Übertragung
- Continuous Health Monitoring für kritische Leitungen
- Alarmierung bei Druckabfall >5% in <2 s
- Temperaturüberwachung mit Grenzwertwarnung
- Teilenummer: Parker SCPSD-016-14-27 (0–400 bar, 4–20 mA)
- Preis: ca. 380–520 EUR pro Sensor + Gateway

**Gates iQ Hose Monitoring:**
- RFID-Tags in Schlauchmantel integriert
- Installations- und Wartungsdaten über NFC abrufbar
- Lebensdauer-Tracking ab Fertigungsdatum
- Keine aktive Drucküberwachung, nur Logistik/Wartungsmanagement

**Eaton LifeSense:**
- Leitfähiger Draht in der Außendecke
- Bricht bei Außendeckenschaden → Alarm
- Speziell für sicherheitskritische Anwendungen
- Bereits in Luftfahrt bewährt, Marine-Adaption ab 2025
- Preis: ca. 45% Aufschlag auf Standard-Schlauch

### Biologisch abbaubare Hydraulikfluide

| Fluid | Norm | Vorteile | Nachteile |
|-------|------|----------|-----------|
| HETG (Pflanzenöl-basiert) | ISO 15380 | Biologisch abbaubar, hoher VI | Oxidationsempfindlich, Temperaturbereich eingeschränkt |
| HEES (Synthetischer Ester) | ISO 15380 | Biologisch abbaubar, guter Temperaturbereich | 3–4× teurer als Mineralöl |
| HEPG (Polyglykol) | ISO 15380 | Schwer entflammbar | Nicht mischbar mit Mineralöl, greift Dichtungen an |

**Empfehlung für Yachten:**
- HEES-Fluide für ökologisch sensible Reviere (Wattenmeer, Ostsee-Schutzgebiete)
- Schlauchmaterial-Kompatibilität prüfen (NBR-Schläuche nicht für HEPG geeignet)
- Mehrkosten: ca. 80–120 EUR/l vs. 15–25 EUR/l für Mineralöl

### Elektrohydraulische Hybride

- Trend zu dezentralen elektrohydraulischen Aktuatoren (EHA)
- Kurze Schlauchlängen, weniger Verlegung
- Beispiel: Rolls-Royce/Kongsberg EHA für Ruderanlagen
- Reduziert Schlauchbedarf um 60–80%
- Nachteil: höhere Komponentenkosten, Elektronik-Abhängigkeit

---

## Best Practices nach Revier

### Mittelmeer (Salzwasser, hohe UV-Belastung, 5–35°C)
- **UV-Schutz**: Schläuche mit UV-resistenter EPDM-Außendecke oder Spiralschutz
- **Salzwasserkühlung**: Edelstahl-316L-Fittings obligatorisch
- **Temperatur**: Maschinenraum-Temperaturen bis 65°C → Schläuche für -40/+100°C
- **Wartungsintervall**: Sichtprüfung alle 6 Monate, Druckprüfung jährlich
- **Typisches Problem**: UV-Versprödung der Außendecke an Deck verlegter Schläuche

### Nordeuropa / Ostsee (Brackwasser, Frost, 2–22°C)
- **Frostschutz**: Hydraulikfluid mit Frostschutz bis -30°C oder Ethylenglykol-Beimischung
- **Kondensation**: Belüftete Schlauchführungen gegen Kondenswasserbildung
- **Biofouling**: Geringeres Risiko als Mittelmeer, aber Muschelbewuchs an Durchführungen
- **Wartungsintervall**: Vor und nach Winterlager, Sichtprüfung quartalsweise
- **Typisches Problem**: Kondenswasser im Hydrauliksystem nach Winterlager

### Tropen (Salzwasser, hohe UV, 25–45°C Maschinenraum bis 75°C)
- **Temperaturresistenz**: Schläuche mit Temperaturbereich -20/+125°C
- **Biologischer Befall**: Antifungale Außendecke oder Schutzschlauch
- **Hohe Luftfeuchtigkeit**: Dichtungsmaterialien NBR/FKM statt Standard-Buna
- **Wartungsintervall**: Sichtprüfung quartalsweise, Ölanalyse halbjährlich
- **Typisches Problem**: Bakterieller Befall des Hydrauliköls, Dichtungsquellung

### Hochsee / Offshore (extremste Bedingungen)
- **Vibrationsfestigkeit**: Spiralverstärkte Schläuche (4SP/4SH) bevorzugen
- **Redundanz**: Doppelte Schlauchleitungen für Ruderanlage obligatorisch
- **Impulsfestigkeit**: Schläuche mit ≥500.000 Impulszyklen
- **Feuerfestigkeit**: IMO-A.753(18)-konforme Schläuche im Maschinenraum
- **Wartungsintervall**: Monatliche Sichtprüfung, halbjährliche Druckprüfung

---

## Regional Sourcing

### Deutschland / DACH
| Händler | Standort | Spezialität | Kontakt |
|---------|----------|-------------|---------|
| Hansa-Flex AG | Bremen/bundesweit | Hydraulikschläuche, Sofortfertigung | hansa-flex.com |
| Pirtek Deutschland | 40+ Standorte | Mobile Schlauchfertigung 24/7 | pirtek.de |
| Hydac International | Sulzbach/Saar | Hydraulikkomponenten, Filter | hydac.com |
| Bauer Hydraulik | Hamburg | Marine-Spezialist | bauer-hydraulik.de |
| SVB (Schiffs-Versorgung Bremen) | Bremen | Yacht-Hydraulik komplett | svb.de |

### Frankreich
| Händler | Standort | Spezialität |
|---------|----------|-------------|
| Lecomble & Schmitt | Boulogne-sur-Mer | Hydraulische Ruderanlagen |
| Hydrokit | Poitiers | Hydraulikkomponenten |
| Pirtek France | 30+ Standorte | Mobile Schlauchfertigung |

### Italien
| Händler | Standort | Spezialität |
|---------|----------|-------------|
| Manuli Hydraulics | Ascoli Piceno | Schlauchfertigung |
| MC² Quick S.p.A. | Ravenna | Stabilisatoren-Hydraulik |
| Vetus Italia | Genua | Marine-Hydraulik |

### Großbritannien
| Händler | Standort | Spezialität |
|---------|----------|-------------|
| Pirtek UK | 90+ Standorte | Mobile Schlauchfertigung |
| Hydrasun | Aberdeen | Offshore-Hydraulik |
| TechnoFlex Marine | Southampton | Marine-Schlauchleitungen |

### Notfall-Kontakte Mittelmeer-Häfen
- **Palma de Mallorca**: Pirtek Mallorca, +34 971 xxx xxx
- **Antibes/Golfe Juan**: Pirtek Côte d'Azur, +33 4 xx xx xx xx
- **La Spezia**: Manuli Service Center, +39 0187 xxx xxx
- **Athen/Piräus**: Hydraulic Systems Greece, +30 210 xxx xxxx

---

## Zweck dieser Wissensdatei

Diese Datei dient dem AYDI-Analysemodul als vollständige Wissensgrundlage zur Bewertung von Hydraulikschlauchleitungen auf Yachten. Sie wird verwendet durch:

1. **Pipeline A (Structured)**: Spezifikationsvergleich, Lebensdauerberechnung, Normenprüfung
2. **Pipeline B (Visual)**: Schadensbilderkennung, Zustandsbewertung aus Fotos
3. **Pipeline C (Text)**: Auswertung von Serviceberichten, Werkstattprotokollen

### Bewertungsdimensionen
- **Sicherheit**: Ist das Hydrauliksystem betriebssicher? (Gewichtung: 40%)
- **Normkonformität**: Entsprechen Schläuche und Fittings den geltenden Normen? (25%)
- **Zustand**: Wie ist der aktuelle Zustand der Schlauchleitungen? (20%)
- **Wartung**: Wird das System ordnungsgemäß gewartet? (15%)

---

## Pydantic-Modelle

```python
"""
Pydantic v2 models for hydraulic hose assessment.
All measurements in mm, pressures in bar, temperatures in °C, costs in EUR.
Scores: 0–100.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class SAEHoseType(str, Enum):
    """SAE 100R hose classification."""
    R1 = "100R1"    # 1-Drahtgeflecht, Standardhydraulik
    R2 = "100R2"    # 2-Drahtgeflecht, höherer Druck
    R3 = "100R3"    # 2-Textilgeflecht, Niederdruck
    R4 = "100R4"    # Saugschlauch, Drahtwendel
    R5 = "100R5"    # 1-Drahtgeflecht, Textildecke
    R6 = "100R6"    # 1-Textilgeflecht, Niederdruck
    R7 = "100R7"    # Thermoplastisch, 1-Drahtgeflecht
    R8 = "100R8"    # Thermoplastisch, 2-Drahtgeflecht
    R12 = "100R12"  # 4-Spirallagen, Hochdruck
    R13 = "100R13"  # 4-/6-Spirallagen, Höchstdruck
    R14 = "100R14"  # PTFE-Seele, Edelstahl-Geflecht
    R15 = "100R15"  # 4-/6-Spirallagen, Compact
    R16 = "100R16"  # Kompakt 1-Drahtgeflecht
    R17 = "100R17"  # Kompakt 2-Drahtgeflecht


class HoseApplication(str, Enum):
    """Application area on the yacht."""
    STEERING = "steering"
    STABILIZER = "stabilizer"
    WINCH = "winch"
    THRUSTER = "thruster"
    TRIM_TAB = "trim_tab"
    CRANE = "crane"
    PASSERELLE = "passerelle"
    DAVIT = "davit"
    ANCHOR_WINDLASS = "anchor_windlass"
    CAPSTAN = "capstan"
    GENERIC_HYDRAULIC = "generic_hydraulic"


class HoseConditionRating(str, Enum):
    """Visual/inspection condition rating."""
    EXCELLENT = "excellent"       # Neuwertig, keine Mängel
    GOOD = "good"                 # Leichte Gebrauchsspuren, voll funktionsfähig
    FAIR = "fair"                 # Sichtbare Alterung, funktionsfähig
    POOR = "poor"                 # Deutliche Mängel, Austausch planen
    CRITICAL = "critical"         # Sicherheitsrelevante Mängel, sofort tauschen
    NOT_ASSESSABLE = "not_assessable"  # Nicht beurteilbar


class FittingType(str, Enum):
    """Hydraulic fitting connection type."""
    JIC_37_DEGREE = "jic_37"      # SAE J514, 37° Konus
    SAE_O_RING = "sae_oring"      # SAE J1926, O-Ring Boss
    BSP_PARALLEL = "bsp_parallel" # BS 5200, paralleles Gewinde
    BSP_TAPERED = "bsp_tapered"   # BS 21, konisches Gewinde
    METRIC_S = "metric_s"         # DIN 2353, Schneidring
    METRIC_L = "metric_l"         # DIN 2353, leichte Reihe
    ORFS = "orfs"                 # O-Ring Face Seal, SAE J1453
    FLANGE_CODE_61 = "flange_61"  # SAE J518, Code 61
    FLANGE_CODE_62 = "flange_62"  # SAE J518, Code 62
    QUICK_DISCONNECT = "quick_disconnect"


class HydraulicFluidType(str, Enum):
    """Hydraulic fluid classification."""
    MINERAL_HLP = "hlp"           # DIN 51524-2, Standard
    MINERAL_HVLP = "hvlp"         # DIN 51524-3, Hoher Viskositätsindex
    SYNTHETIC_ESTER = "hees"      # ISO 15380, biologisch abbaubar
    PLANT_OIL = "hetg"            # ISO 15380, Pflanzenöl
    POLYGLYCOL = "hepg"           # ISO 15380, Polyglykol
    ATF = "atf"                   # Automatic Transmission Fluid
    WATER_GLYCOL = "hfc"          # Schwer entflammbar


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for assessment results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class CrimpType(str, Enum):
    """Crimping method for hose fittings."""
    CRIMPED_PERMANENT = "crimped_permanent"
    REUSABLE_SCREW = "reusable_screw"
    PUSH_ON = "push_on"
    SWAGED = "swaged"


# --- Core Models ---

class HydraulicHoseSpec(BaseModel):
    """Technical specification of a hydraulic hose assembly."""

    model_config = {"from_attributes": True}

    # Identification
    hose_id: str = Field(..., description="Unique hose identifier, e.g. 'HYD-RUD-001'")
    manufacturer: str = Field(..., description="Hose manufacturer, e.g. 'Parker Hannifin'")
    product_line: str = Field("", description="Product line, e.g. 'GlobalCore 481'")
    part_number: str = Field("", description="Manufacturer part number")
    sae_type: SAEHoseType = Field(..., description="SAE 100R classification")
    application: HoseApplication = Field(..., description="Application area")

    # Dimensions (mm)
    inner_diameter_mm: float = Field(..., ge=3.0, le=102.0, description="Inner diameter in mm")
    outer_diameter_mm: float = Field(..., ge=8.0, le=140.0, description="Outer diameter in mm")
    length_mm: float = Field(..., ge=50.0, le=30000.0, description="Assembly length in mm")
    min_bend_radius_mm: float = Field(..., ge=20.0, le=800.0, description="Minimum bend radius in mm")

    # Pressure ratings (bar)
    working_pressure_bar: float = Field(..., ge=5.0, le=700.0, description="Maximum working pressure in bar")
    burst_pressure_bar: float = Field(..., ge=20.0, le=2800.0, description="Minimum burst pressure in bar")
    test_pressure_bar: float = Field(0.0, ge=0.0, description="Factory test pressure in bar")

    # Temperature range (°C)
    temp_min_c: float = Field(-40.0, ge=-60.0, le=0.0, description="Minimum operating temperature")
    temp_max_c: float = Field(100.0, ge=60.0, le=200.0, description="Maximum operating temperature")

    # Construction
    inner_tube_material: str = Field("NBR", description="Inner tube material (NBR, EPDM, PTFE, CPE)")
    reinforcement_type: str = Field("", description="Reinforcement (wire braid, wire spiral, textile)")
    outer_cover_material: str = Field("CR", description="Outer cover material (CR, EPDM, PU, CPE)")

    # Fittings
    fitting_end_a: FittingType = Field(..., description="Fitting type end A")
    fitting_end_b: FittingType = Field(..., description="Fitting type end B")
    fitting_size_a: str = Field("", description="Fitting size end A, e.g. '-8' or '1/2\"'")
    fitting_size_b: str = Field("", description="Fitting size end B")
    fitting_material: str = Field("steel_zinc", description="Fitting material")
    crimp_type: CrimpType = Field(CrimpType.CRIMPED_PERMANENT, description="Crimping method")

    # Fluid compatibility
    fluid_type: HydraulicFluidType = Field(HydraulicFluidType.MINERAL_HLP, description="Hydraulic fluid type")

    # Installation
    installation_date: Optional[date] = Field(None, description="Installation date")
    max_service_life_years: int = Field(6, ge=1, le=15, description="Max service life in years (DNV: 6)")

    # Cost
    unit_cost_eur: float = Field(0.0, ge=0.0, description="Cost of hose assembly in EUR")
    installation_cost_eur: float = Field(0.0, ge=0.0, description="Installation labor cost in EUR")

    @field_validator("burst_pressure_bar")
    @classmethod
    def burst_must_exceed_working(cls, v: float, info) -> float:
        wp = info.data.get("working_pressure_bar", 0)
        if wp and v < wp * 2.5:
            raise ValueError(
                f"Burst pressure ({v} bar) must be ≥ 2.5× working pressure ({wp} bar)"
            )
        return v


class HydraulicHoseCondition(BaseModel):
    """Condition assessment of a hydraulic hose assembly."""

    model_config = {"from_attributes": True}

    hose_id: str = Field(..., description="Reference to HydraulicHoseSpec.hose_id")
    assessment_date: date = Field(..., description="Date of assessment")
    assessor: str = Field("AYDI_visual", description="Assessor (person or system)")

    # Overall condition
    condition_rating: HoseConditionRating = Field(..., description="Overall condition rating")
    condition_score: int = Field(..., ge=0, le=100, description="Numerical condition score 0-100")
    confidence: ConfidenceLevel = Field(..., description="Confidence level of assessment")

    # Specific checks
    outer_cover_intact: Optional[bool] = Field(None, description="Outer cover without cracks/abrasion")
    outer_cover_score: int = Field(50, ge=0, le=100, description="Outer cover condition 0-100")
    fitting_corrosion: Optional[bool] = Field(None, description="Corrosion visible on fittings")
    fitting_score: int = Field(50, ge=0, le=100, description="Fitting condition 0-100")
    leakage_detected: Optional[bool] = Field(None, description="Any leakage detected")
    leakage_severity: str = Field("none", description="none/seeping/dripping/spraying")
    bend_radius_respected: Optional[bool] = Field(None, description="Min bend radius respected")
    abrasion_marks: Optional[bool] = Field(None, description="Abrasion marks visible")
    age_years: Optional[float] = Field(None, ge=0, le=30, description="Age in years")
    age_exceeded: Optional[bool] = Field(None, description="Service life exceeded (>6 years)")
    uv_degradation: Optional[bool] = Field(None, description="UV degradation visible on cover")
    kinking_observed: Optional[bool] = Field(None, description="Kinking or flattening observed")
    swelling_observed: Optional[bool] = Field(None, description="Hose swelling/ballooning observed")

    # Routing assessment
    routing_score: int = Field(50, ge=0, le=100, description="Routing quality 0-100")
    chafe_protection_present: Optional[bool] = Field(None, description="Chafe protection installed")
    proper_clamping: Optional[bool] = Field(None, description="Proper clamping/support")
    thermal_proximity_ok: Optional[bool] = Field(None, description="Distance to heat sources OK")

    # Findings
    findings: list[str] = Field(default_factory=list, description="List of findings (German)")
    recommendations: list[str] = Field(default_factory=list, description="Recommendations (German)")
    replacement_urgency: str = Field(
        "routine",
        description="Urgency: immediate/soon/planned/routine/not_required"
    )

    # Cost estimate
    estimated_replacement_cost_eur: float = Field(0.0, ge=0.0)

    @field_validator("condition_score")
    @classmethod
    def score_matches_rating(cls, v: int, info) -> int:
        rating = info.data.get("condition_rating")
        if rating == HoseConditionRating.CRITICAL and v > 25:
            raise ValueError("CRITICAL rating requires score ≤ 25")
        if rating == HoseConditionRating.EXCELLENT and v < 85:
            raise ValueError("EXCELLENT rating requires score ≥ 85")
        return v


class HydraulicSystemAssessment(BaseModel):
    """Complete hydraulic system assessment for a yacht."""

    model_config = {"from_attributes": True}

    # Yacht reference
    yacht_id: str = Field(..., description="AYDI yacht identifier")
    assessment_date: datetime = Field(..., description="Assessment timestamp")
    assessor: str = Field("AYDI_system", description="Assessor identifier")
    confidence: ConfidenceLevel = Field(..., description="Overall confidence level")

    # Yacht context
    yacht_loa_mm: float = Field(..., ge=6000, le=60000, description="LOA in mm")
    yacht_type: str = Field(..., description="motor/sail/catamaran/trawler")
    yacht_age_years: float = Field(0, ge=0, le=60, description="Yacht age in years")
    ce_category: str = Field("B", description="CE design category A/B/C/D")

    # System inventory
    hose_count: int = Field(0, ge=0, le=200, description="Total number of hose assemblies")
    hose_specs: list[HydraulicHoseSpec] = Field(default_factory=list)
    hose_conditions: list[HydraulicHoseCondition] = Field(default_factory=list)

    # System scores (0-100)
    overall_score: int = Field(50, ge=0, le=100, description="Overall hydraulic system score")
    steering_score: int = Field(50, ge=0, le=100, description="Steering hydraulics score")
    stabilizer_score: Optional[int] = Field(None, ge=0, le=100, description="Stabilizer score")
    winch_score: Optional[int] = Field(None, ge=0, le=100, description="Winch hydraulics score")
    thruster_score: Optional[int] = Field(None, ge=0, le=100, description="Thruster hydraulics score")

    # Compliance
    sae_j1942_compliant: Optional[bool] = Field(None, description="SAE J1942 marine compliance")
    abyc_h32_compliant: Optional[bool] = Field(None, description="ABYC H-32 compliance")
    class_society_approved: Optional[bool] = Field(None, description="Class society approved")
    class_society: Optional[str] = Field(None, description="DNV-GL/LR/RINA/BV/ABS")

    # Critical findings
    critical_findings: list[str] = Field(default_factory=list)
    replacement_plan: list[dict] = Field(default_factory=list)

    # Cost
    total_replacement_cost_eur: float = Field(0.0, ge=0.0)
    annual_maintenance_cost_eur: float = Field(0.0, ge=0.0)

    # Summary (German)
    summary_de: str = Field("", description="German summary of hydraulic system condition")
    recommendation_de: str = Field("", description="German overall recommendation")
```

---

## Grundlagen

### SAE 100R-Klassifikation — Vollständige Übersicht

Die SAE J517-Norm definiert die **100R-Serie** als internationale Referenz für Hydraulikschläuche. Jede Klasse hat spezifische Konstruktionsmerkmale, Druckbereiche und Einsatzgebiete.

#### SAE 100R1 (1SN nach DIN EN 853)
- **Konstruktion**: Innenrohr (NBR/Synthese-Kautschuk) + 1 Drahtgeflechtlage + Außendecke (CR/Synthese)
- **Druckbereich**: 40–250 bar (je nach DN)
- **Yacht-Einsatz**: Standard-Ruderanlagen Boote bis 12 m, Trimmklappen, Niederdruck-Aggregate
- **Innendurchmesser**: DN 5 (3/16") bis DN 51 (2")
- **Temperatur**: -40°C bis +100°C (Standard), -40°C bis +125°C (Spezial)
- **Berstdruck**: 4× Arbeitsdruck
- **Impulsfestigkeit**: min. 200.000 Zyklen (SAE J343)
- **Typische Parker-Nummer**: 481-6 (DN 10, 3/8")
- **Typische Gates-Nummer**: MXT-6 (DN 10)
- **Preis**: 8–25 EUR/m je nach DN

| DN (mm) | Zoll | Arbeitsdruck (bar) | Berstdruck (bar) | Biegeradius (mm) |
|---------|------|-------------------|------------------|-------------------|
| 5 | 3/16" | 250 | 1000 | 65 |
| 6 | 1/4" | 225 | 900 | 75 |
| 8 | 5/16" | 215 | 860 | 90 |
| 10 | 3/8" | 180 | 720 | 105 |
| 12 | 1/2" | 160 | 640 | 125 |
| 16 | 5/8" | 130 | 520 | 150 |
| 19 | 3/4" | 115 | 460 | 180 |
| 25 | 1" | 90 | 360 | 240 |
| 32 | 1-1/4" | 63 | 252 | 300 |
| 38 | 1-1/2" | 50 | 200 | 360 |
| 51 | 2" | 40 | 160 | 460 |

#### SAE 100R2 (2SN nach DIN EN 853)
- **Konstruktion**: Innenrohr (NBR) + 2 Drahtgeflechtlagen + Außendecke (CR)
- **Druckbereich**: 80–400 bar (je nach DN)
- **Yacht-Einsatz**: Hauptruderanlage, Stabilisatoren, Winschen, Bugstrahlruder
- **Temperatur**: -40°C bis +100°C
- **Berstdruck**: 4× Arbeitsdruck
- **Impulsfestigkeit**: min. 200.000 Zyklen
- **Typische Parker-Nummer**: 482-8 (DN 12, 1/2")
- **Typische Gates-Nummer**: MegaSys 4220-8
- **Preis**: 12–45 EUR/m

| DN (mm) | Zoll | Arbeitsdruck (bar) | Berstdruck (bar) | Biegeradius (mm) |
|---------|------|-------------------|------------------|-------------------|
| 5 | 3/16" | 400 | 1600 | 75 |
| 6 | 1/4" | 400 | 1600 | 100 |
| 8 | 5/16" | 350 | 1400 | 115 |
| 10 | 3/8" | 330 | 1320 | 130 |
| 12 | 1/2" | 275 | 1100 | 180 |
| 16 | 5/8" | 250 | 1000 | 200 |
| 19 | 3/4" | 215 | 860 | 240 |
| 25 | 1" | 165 | 660 | 300 |
| 32 | 1-1/4" | 125 | 500 | 420 |
| 38 | 1-1/2" | 100 | 400 | 500 |
| 51 | 2" | 80 | 320 | 630 |

#### SAE 100R5 (1-Drahtgeflecht, Textildecke)
- **Konstruktion**: Innenrohr (NBR) + 1 Textilgeflecht + 1 Drahtgeflecht + Textildecke
- **Druckbereich**: 35–175 bar
- **Yacht-Einsatz**: Niederdruckleitungen, Rücklaufleitungen, Servosteuerung
- **Besonderheit**: Textildecke — leichter, flexibler, aber weniger abriebfest
- **Temperatur**: -40°C bis +100°C
- **Preis**: 6–18 EUR/m

#### SAE 100R7 (Thermoplastisch, 1-Drahtgeflecht)
- **Konstruktion**: Thermoplastisches Innenrohr (Polyester/Nylon) + 1 Drahtgeflecht + Thermoplast-Außendecke
- **Druckbereich**: 70–350 bar
- **Yacht-Einsatz**: Autopiloten, kompakte Steuerungssysteme, Instrumentenleitungen
- **Besonderheit**: Kleiner Biegeradius, geringes Gewicht, kein Volumenzuwachs unter Druck
- **Temperatur**: -40°C bis +93°C
- **Typisch**: Teleflex/SeaStar Steuerleitungen
- **Preis**: 10–30 EUR/m

#### SAE 100R8 (Thermoplastisch, 2-Drahtgeflecht)
- **Konstruktion**: Thermoplastisches Innenrohr + 2 Drahtgeflechtlagen + Thermoplast-Außendecke
- **Druckbereich**: 140–700 bar
- **Yacht-Einsatz**: Hochdruck-Steuerungssysteme, Winschen-Direktantrieb
- **Besonderheit**: Wie R7, aber für höhere Drücke
- **Temperatur**: -40°C bis +100°C
- **Preis**: 15–45 EUR/m

#### SAE 100R12 (4-Spirallagen, Hochdruck)
- **Konstruktion**: Innenrohr (NBR) + 4 Spiraldrahtlagen + Außendecke (CR)
- **Druckbereich**: 210–420 bar (je nach DN, nur ab DN 12)
- **Yacht-Einsatz**: Hydraulische Großwinschen, Kräne, Davits, Ankerspill
- **Temperatur**: -40°C bis +121°C
- **Impulsfestigkeit**: min. 500.000 Zyklen
- **Typische Parker-Nummer**: 787-12 (DN 19)
- **Preis**: 35–90 EUR/m

| DN (mm) | Zoll | Arbeitsdruck (bar) | Berstdruck (bar) | Biegeradius (mm) |
|---------|------|-------------------|------------------|-------------------|
| 12 | 1/2" | 420 | 1680 | 180 |
| 16 | 5/8" | 380 | 1520 | 200 |
| 19 | 3/4" | 350 | 1400 | 240 |
| 25 | 1" | 280 | 1120 | 340 |
| 32 | 1-1/4" | 210 | 840 | 420 |
| 38 | 1-1/2" | 210 | 840 | 500 |
| 51 | 2" | 210 | 840 | 630 |

#### SAE 100R13 (4-/6-Spirallagen, Höchstdruck)
- **Konstruktion**: Innenrohr (NBR) + 4 oder 6 Spiraldrahtlagen + Außendecke
- **Druckbereich**: 350–700 bar
- **Yacht-Einsatz**: Selten auf Yachten; nur bei industriellen Hydraulikaggregaten auf Superyachten
- **Temperatur**: -40°C bis +121°C
- **Preis**: 50–150 EUR/m

#### SAE 100R14 (PTFE-Seele, Edelstahl-Geflecht)
- **Konstruktion**: PTFE-Innenrohr + 1 Edelstahl-Drahtgeflecht (kein Außenmantel)
- **Druckbereich**: 100–280 bar
- **Yacht-Einsatz**: Chemisch aggressive Medien, hohe Temperaturen, Bremshydraulik
- **Besonderheit**: Chemisch inert, höchste Temperaturbeständigkeit
- **Temperatur**: -73°C bis +204°C (Dauer), bis +260°C (kurzzeitig)
- **Preis**: 25–80 EUR/m

#### SAE 100R15 (Kompakt, 4-/6-Spirallagen)
- **Konstruktion**: Wie R12/R13 aber mit reduziertem Außendurchmesser
- **Druckbereich**: 280–420 bar
- **Yacht-Einsatz**: Platzoptimierte Hochdruckleitungen
- **Preis**: 40–110 EUR/m

#### SAE 100R16 / R17 (Kompakt 1SC/2SC nach DIN EN 857)
- **Konstruktion**: Kompakte Version von R1/R2 mit dünnerem Aufbau
- **Yacht-Einsatz**: Enge Einbauräume, Autopiloten, kleine Steuerungszylinder
- **Preis**: R16: 10–28 EUR/m, R17: 14–40 EUR/m

### Schlauchaufbau — Detaillierte Konstruktionsbeschreibung

#### Schichtaufbau eines typischen 2SN-Schlauchs (SAE 100R2AT)

```
Querschnitt (von innen nach außen):

┌──────────────────────────────────────────────┐
│                                              │
│    ╔══════════════════════════════════╗       │
│    ║  Schicht 1: INNENROHR (Seele)   ║       │
│    ║  Material: NBR (Nitrilkautschuk)║       │
│    ║  Dicke: 1.0–1.5 mm             ║       │
│    ║  Funktion: Medienführung,       ║       │
│    ║  Dichtheit, Fluidkompatibilität ║       │
│    ╚══════════════════════════════════╝       │
│    ┌──────────────────────────────────┐       │
│    │  Schicht 2: 1. DRAHTGEFLECHT    │       │
│    │  Material: Hochfester Stahldraht│       │
│    │  Drahtdurchmesser: 0.3–0.5 mm  │       │
│    │  Flechtwinkel: 54°44' (optimal) │       │
│    │  Funktion: Druckaufnahme,       │       │
│    │  Impulsfestigkeit               │       │
│    └──────────────────────────────────┘       │
│    ┌──────────────────────────────────┐       │
│    │  Schicht 3: ZWISCHENLAGE        │       │
│    │  Material: Synthese-Kautschuk   │       │
│    │  Dicke: 0.3–0.5 mm             │       │
│    │  Funktion: Haftung zwischen den │       │
│    │  Geflechtlagen, Vibrationsdämpf.│       │
│    └──────────────────────────────────┘       │
│    ┌──────────────────────────────────┐       │
│    │  Schicht 4: 2. DRAHTGEFLECHT    │       │
│    │  (identisch mit Schicht 2)      │       │
│    │  Gegenläufig geflochten für     │       │
│    │  Torsionsneutralität            │       │
│    └──────────────────────────────────┘       │
│    ╔══════════════════════════════════╗       │
│    ║  Schicht 5: AUSSENDECKE (Cover) ║       │
│    ║  Material: CR (Chloropren)      ║       │
│    ║  Dicke: 0.8–1.2 mm             ║       │
│    ║  Funktion: Schutz vor UV,       ║       │
│    ║  Abrasion, Chemikalien, Ozon    ║       │
│    ║  Aufdruckbereich für Markierung ║       │
│    ╚══════════════════════════════════╝       │
│                                              │
└──────────────────────────────────────────────┘
```

#### Aufdruck auf Außendecke — Informationen decodieren

**Beispiel-Aufdruck:**
```
PARKER GLOBALCORE 482  SAE 100R2AT  DIN EN 853 2SN  -8  WP 275 bar (4000 PSI)  
BP 1100 bar (16000 PSI)  III-Q2/2024  MADE IN GERMANY  DNV-GL TA
```

**Decodierung:**

| Feld | Bedeutung | Erklärung |
|------|-----------|-----------|
| PARKER GLOBALCORE 482 | Hersteller + Produktlinie | Parker Hannifin, GlobalCore Serie 482 |
| SAE 100R2AT | SAE-Klassifikation | 2-Drahtgeflecht, Typ AT (Standard) |
| DIN EN 853 2SN | Europäische Norm | Equivalent 2SN |
| -8 | Dash-Size | Innendurchmesser 8/16" = 1/2" = 12.7 mm |
| WP 275 bar | Arbeitsdruck | Max. Dauerbetriebsdruck |
| BP 1100 bar | Berstdruck | Mindest-Berstdruck |
| III-Q2/2024 | Herstellungsdatum | Werk III, 2. Quartal 2024 |
| MADE IN GERMANY | Herstellungsort | Fertigung in Deutschland |
| DNV-GL TA | Zulassung | DNV-GL Type Approved |

**Datumscode verschiedener Hersteller:**
- **Parker**: Werk-Nr., Quartal/Jahr (z.B. "III-Q2/2024")
- **Gates**: Jahreszahl + Kalenderwoche (z.B. "24-15" = KW 15/2024)
- **Continental**: Monat/Jahr (z.B. "06/24" = Juni 2024)
- **Eaton**: DOT-Code (Quartal/Jahr, z.B. "2Q24")
- **Manuli**: Fortlaufende Losnummer + Quartal/Jahr

### Schlauchschutz-Systeme

#### Spiralschutz (Plastic Spiral Wrap)

| Eigenschaft | Wert |
|------------|------|
| Material | PE (Polyethylen) oder PA (Polyamid) |
| Temperaturbereich | -40°C bis +120°C |
| UV-Beständigkeit | Gut (PA besser als PE) |
| Montage | Aufwickeln in Spiralform um Schlauch |
| Farben | Schwarz, Gelb (Warnfarbe), Rot, Blau |
| Größen | 9–34 mm Wickeldurchmesser |
| Preis | 2–8 EUR/m |
| Hersteller | Parker Partek, Gates, Hansa-Flex |

#### Textilschutz (Textile Sleeve)

| Eigenschaft | Wert |
|------------|------|
| Material | Polyester-Geflecht oder Nylon |
| Temperaturbereich | -40°C bis +150°C |
| UV-Beständigkeit | Ausgezeichnet |
| Montage | Über Schlauch schieben (vor Fitting-Montage) |
| Abriebschutz | Sehr gut |
| Preis | 3–12 EUR/m |
| Hersteller | Parker, Continental, Techflex |

#### Feuerschutz (Fire Sleeve)

| Eigenschaft | Wert |
|------------|------|
| Material | Silikonbeschichtetes Glasfasergewebe |
| Temperaturbereich | Dauerhaft bis +260°C, kurzzeitig bis +1600°C |
| Brandklasse | IMO-A.753(18), UL-94 V-0 |
| Montage | Über Schlauch schieben + Befestigungsschellen |
| Pflicht | Im Maschinenraum bei <100 mm Abstand zu Abgas |
| Preis | 8–25 EUR/m |
| Hersteller | Parker FireGuard, Continental, Techflex Firesleeve |

#### Metallschutz (Spring Guard)

| Eigenschaft | Wert |
|------------|------|
| Material | Federstahldraht, verzinkt oder 316L |
| Temperaturbereich | bis +200°C |
| Einsatz | Extreme mechanische Belastung, Maschinenraum |
| Montage | Über Schlauch schieben, Schlauchschellen fixieren |
| Preis | 5–20 EUR/m |
| Hersteller | Hansa-Flex, Parker, diverse |

### Marine-Empfehlung nach Anwendung

| Anwendung | Empfohlener SAE-Typ | Druck (bar) | DN (mm) |
|-----------|---------------------|-------------|---------|
| Ruderanlage bis 12 m | R1/R7 | 70–150 | 6–10 |
| Ruderanlage 12–20 m | R2/R7 | 100–250 | 10–16 |
| Ruderanlage 20–40 m | R2/R12 | 150–350 | 12–25 |
| Ruderanlage 40–60 m | R12/R13 | 200–420 | 19–38 |
| Stabilisator (Flossen) | R2/R12 | 150–350 | 12–19 |
| Stabilisator (Gyro-Hydraulik) | R2 | 100–200 | 10–16 |
| Winsch (Segel, bis 15 m) | R2 | 150–250 | 10–16 |
| Winsch (Segel/Motor, 15–30 m) | R2/R12 | 200–350 | 12–25 |
| Winsch (Superyacht, >30 m) | R12/R13 | 250–420 | 19–38 |
| Bugstrahlruder (bis 15 m) | R2 | 100–200 | 10–19 |
| Bugstrahlruder (15–30 m) | R2/R12 | 150–300 | 16–25 |
| Heckstrahlruder | R2/R12 | 150–300 | 16–25 |
| Trimmklappen | R1/R5 | 50–120 | 6–10 |
| Passerelle/Gangway | R2 | 100–200 | 8–12 |
| Davit/Kran | R2/R12 | 150–350 | 12–25 |
| Ankerspill (hydraulisch) | R2/R12 | 150–300 | 12–19 |

### Hydraulikflüssigkeiten — Detailübersicht

#### Mineralöl HLP (DIN 51524-2)
- **Beschreibung**: Standard-Hydrauliköl mit Verschleißschutz-Additiven (EP)
- **Viskosität**: ISO VG 15, 22, 32, 46, 68 (häufigste: VG 15 für Steuerung, VG 32/46 für Power Packs)
- **Temperaturbereich**: -30°C bis +80°C (VG 32)
- **Produkte**: Shell Tellus S2 M 32, Mobil DTE 25, Total Azolla ZS 32
- **Kompatibilität**: NBR-Schläuche, Standard-Dichtungen
- **Preis**: 5–15 EUR/l

#### Mineralöl HVLP (DIN 51524-3)
- **Beschreibung**: Hydrauliköl mit hohem Viskositätsindex (VI >140)
- **Vorteil**: Gleichmäßige Viskosität über großen Temperaturbereich
- **Empfehlung**: Yachten mit großen Temperaturschwankungen (Nordeuropa↔Tropen)
- **Produkte**: Shell Tellus S3 M 46, Mobil SHC 525, Total Equivis ZS 46
- **Preis**: 8–22 EUR/l

#### ATF (Automatic Transmission Fluid)
- **Beschreibung**: Sehr niedrigviskoses Fluid, ursprünglich für Automatikgetriebe
- **Yacht-Einsatz**: SeaStar/BayStar-Steuersysteme, Teleflex-Systeme
- **ACHTUNG**: Nicht mit HLP mischbar! Systemwechsel erfordert Spülung
- **Produkte**: Teleflex/SeaStar Hydraulic Steering Fluid, Dexron III/VI kompatibel
- **Preis**: 8–18 EUR/l

#### Synthetischer Ester HEES (ISO 15380)
- **Beschreibung**: Biologisch abbaubares Hydraulikfluid auf Esterbasis
- **Yacht-Einsatz**: Ökologisch sensible Reviere, Superyachten mit Umweltzertifizierung
- **Kompatibilität**: Spezielle Dichtungen erforderlich (FKM bevorzugt)
- **Produkte**: Panolin HLP SYNTH 46, Fuchs Plantohyd S 46
- **Preis**: 25–60 EUR/l

### Schlauchmaterialien

#### Innenrohr (Seele)

| Material | Kürzel | Temperatur | Druckbereich | Medienkompatibilität | Yacht-Eignung |
|----------|--------|------------|--------------|---------------------|---------------|
| Nitril-Kautschuk | NBR | -40/+100°C | bis 420 bar | Mineralöl, ATF | Standard, sehr gut |
| Chloropren | CR | -35/+100°C | bis 350 bar | Mineralöl, Wasser-Glykol | Gut, bedingt Biodiesel |
| EPDM | EPDM | -50/+150°C | bis 200 bar | Wasser, Glykol, HEPG | Nicht für Mineralöl! |
| PTFE | PTFE | -73/+260°C | bis 280 bar | Universell | Spezial, teuer |
| CPE | CPE | -40/+125°C | bis 400 bar | Mineralöl, Biodiesel | Erweitert, modern |
| Polyester | — | -40/+93°C | bis 700 bar | Mineralöl, ATF | Thermoplast, R7/R8 |

#### Außendecke (Mantel)

| Material | Kürzel | Eigenschaften | Yacht-Eignung |
|----------|--------|---------------|---------------|
| Chloropren | CR | Ölresistent, UV-mäßig, Abrieb gut | Standard |
| EPDM | EPDM | UV-excellent, Ozon-excellent, Öl-schlecht | Deckverlegung, UV-belastet |
| Polyurethan | PU | Abrieb-excellent, UV-gut, Öl-gut | Hochbeanspruchte Bereiche |
| Textil | — | Leicht, flexibel, wenig Abriebschutz | R5, Niederdruckleitungen |
| Edelstahl-Geflecht | SS316 | Maximaler Schutz, korrosionsresistent | PTFE-Schläuche, Maschinenraum |

### Fittings — JIC / SAE / BSP / Metrisch

#### JIC 37° (SAE J514)
- **Beschreibung**: 37° Konus-Dichtung, häufigster Standard in US/Marine-Hydraulik
- **Vorteile**: Wiederverwendbar, dicht ohne Zusatzdichtung, vibrationsfest
- **Nachteile**: Erfordert präzise Konusflächen, Überdrehmoment → Undichtheit
- **Gewindegrößen**: -2 (1/8") bis -32 (2")
- **Marine-Einsatz**: SeaStar, Kobelt, Parker Marine, alle US-Hersteller
- **Material**: Stahl verzinkt, Edelstahl 316, Messing (Niederdruck)

| JIC-Größe | Dash | Gewindemaß UNF | Schlauchanschluss |
|-----------|------|-----------------|-------------------|
| -4 | 4 | 7/16"-20 | DN 6 (1/4") |
| -6 | 6 | 9/16"-18 | DN 8 (5/16") |
| -8 | 8 | 3/4"-16 | DN 10–12 (3/8"–1/2") |
| -10 | 10 | 7/8"-14 | DN 12–16 (1/2"–5/8") |
| -12 | 12 | 1-1/16"-12 | DN 16–19 (5/8"–3/4") |
| -16 | 16 | 1-5/16"-12 | DN 19–25 (3/4"–1") |
| -20 | 20 | 1-5/8"-12 | DN 25–32 (1"–1-1/4") |
| -24 | 24 | 1-7/8"-12 | DN 32–38 (1-1/4"–1-1/2") |

#### SAE O-Ring Boss (SAE J1926)
- **Beschreibung**: O-Ring-Dichtung in gerader Bohrung
- **Vorteile**: Sehr dicht, vibrationsfest, kein Überdrehmoment-Risiko
- **Nachteile**: O-Ring als Verschleißteil, nicht für hohe Temperaturen
- **Marine-Einsatz**: Stabilisatoren, Winschen, Power Packs
- **O-Ring-Material**: NBR (Standard), FKM/Viton (Hochtemperatur)

#### BSP (British Standard Pipe)
- **BSP Parallel (BSPP, G-Gewinde)**: Mit O-Ring oder Dichtring, europäischer Standard
- **BSP Konisch (BSPT, R-Gewinde)**: Selbstdichtend durch Gewindekonizität, Teflonband nötig
- **Marine-Einsatz**: Lecomble & Schmitt, Vetus, europäische Hersteller
- **ACHTUNG**: BSP und NPT (US-konisch) sind NICHT kompatibel, obwohl ähnlich!

#### Metrisch (DIN 2353, Schneidring)
- **Beschreibung**: Schneidringverschraubung mit 24°-Konus
- **Vorteile**: Europäischer Standard, sehr verbreitet, zuverlässig
- **Reihen**: L (leichte Reihe, bis 160 bar), S (schwere Reihe, bis 400 bar)
- **Marine-Einsatz**: Deutsche/europäische Werften, Reckmann, Hydraulik Nord

#### ORFS (O-Ring Face Seal, SAE J1453)
- **Beschreibung**: O-Ring in Planfläche, modernster Standard
- **Vorteile**: Leckagefrei, vibrationsfest, wiederverwendbar
- **Nachteile**: Höhere Komponentenkosten
- **Marine-Einsatz**: Superyacht-Neubauten, Naiad Dynamics, MC² Quick

---

## Hersteller — Vollständige Übersicht

### Parker Hannifin (USA/Global)

**Marktposition**: Weltmarktführer Hydraulikschläuche, breitestes Marine-Sortiment

**Produktlinien für Marine:**

| Produktlinie | SAE-Typ | Druckbereich | Besonderheit |
|-------------|---------|--------------|--------------|
| GlobalCore 481 | 100R1 (1SN) | 40–250 bar | Standard, SuperTough-Decke |
| GlobalCore 482 | 100R2 (2SN) | 80–400 bar | Marine-Arbeitspferd |
| GlobalCore 487 | 100R12 (4SP) | 210–420 bar | Hochdruck, Spiralverstärkt |
| No-Skive 71 | 100R1 | 40–250 bar | Ohne Außendecke-Entfernung crimpbar |
| No-Skive 72 | 100R2 | 80–400 bar | Einfachste Verarbeitung |
| Compact Spiral 777 | 100R15 | 280–420 bar | 30% kleiner als Standard |
| Parflex 540N | 100R7 | 70–350 bar | Thermoplastisch, Autopilot |
| Parflex 550B | 100R8 | 140–700 bar | Thermoplastisch, Hochdruck |
| Parflex 510A/520A | 100R14 | 100–280 bar | PTFE, Edelstahl |
| Push-Lok 801/831 | — | 10–35 bar | Niederdruck, ohne Crimpwerkzeug |

**Parker Marine-spezifische Produkte:**
- **Parker Marine Steering Kit MSK-xx**: Komplettsets für Ruderhydraulik
- **Parker Hydraulic Power Unit HPU-xx**: Marine-Aggregate mit Tankeinheit
- **Parker SensoControl SCPSD**: Drucküberwachung digital

**Parker Crimp-Systeme:**
- **Parkrimp 2**: Standard-Crimpmaschine, 50+ Presswerkzeuge
- **Parkrimp 1**: Portable Crimpmaschine für Bordwerkstatt
- **Karrykrimp 2 (82C-080)**: Mobile Crimpmaschine für Servicefahrzeuge

**Kontakt DACH**: Parker Hannifin Manufacturing Germany GmbH, Bielefeld
**Marine Katalog**: Parker Marine Hose Catalog 4400 (online verfügbar)

### Gates Corporation (USA/Global)

**Marktposition**: Zweitgrößter Hersteller, stark im OEM-Markt

**Produktlinien für Marine:**

| Produktlinie | SAE-Typ | Druckbereich | Besonderheit |
|-------------|---------|--------------|--------------|
| MegaSys MXT | 100R1/R2 | 40–400 bar | MegaCrimp-System |
| MegaSys 4000 | 100R12 | 210–420 bar | 4-Spirallagen |
| MegaSys G2XTR | erweitert R2 | bis 450 bar | Extended pressure R2 |
| MXT Plus | 100R2 enhanced | bis 445 bar | 1.000.000 Impulszyklen |
| C5E/C5C | 100R5 | 35–175 bar | Textildecke |
| Marine Fluid Power | Marine-spezifisch | diverse | SAE J1942 zertifiziert |

**Gates Crimp-System:**
- **MegaCrimp**: GC32 (stationär), GC20 (portabel)
- **Gates Mobile Crimp**: MobileCrimp 4-20 (Vor-Ort-Service)

### Eaton/Aeroquip (USA/Global)

**Marktposition**: Stark im Luft-/Raumfahrtbereich, Premium-Qualität

**Produktlinien für Marine:**

| Produktlinie | SAE-Typ | Druckbereich | Besonderheit |
|-------------|---------|--------------|--------------|
| Matchmate GH781 | 100R1 | 40–250 bar | Einfache Montage |
| Matchmate GH793 | 100R2 | 80–400 bar | Standard-Marine |
| Synflex 34CT | 100R7 | 70–350 bar | Thermoplastisch |
| FC300 | 100R5 | 35–175 bar | Textildecke |
| GH663 | 100R12 | 210–420 bar | 4-Spirallagen |
| AE701 | 100R14 | 100–280 bar | PTFE/SS316 |

**Eaton Crimp-System:**
- **Weatherhead ET1000**: Stationäre Crimpmaschine
- **Weatherhead Coll-O-Crimp**: Portable für Service

### Continental ContiTech (Deutschland)

**Marktposition**: Größter europäischer Hersteller, stark in Marine/Offshore

**Produktlinien für Marine:**

| Produktlinie | SAE-Typ | Druckbereich | Besonderheit |
|-------------|---------|--------------|--------------|
| Flexon 1SN | 100R1 | 40–250 bar | DNV-GL-zugelassen |
| Flexon 2SN | 100R2 | 80–400 bar | DNV-GL, LR zugelassen |
| Flexon 4SP | 100R12 | 210–420 bar | Marine-Offshore |
| Goldflex | 100R1/R2 | bis 400 bar | Höchste Impulsfestigkeit |
| Pushmaster | — | bis 35 bar | Ohne Crimpwerkzeug |

**Besonderheit Continental:**
- Fertigung in Deutschland (Korbach, Hannover)
- DNV-GL Type Approval für alle Flexon-Serien
- Lloyd's Register Type Approval
- Umfassende Marine-Zertifizierungen
- Schulungsprogramm für Marine-Verarbeiter

### Manuli Hydraulics (Italien/Global)

**Marktposition**: Italienischer Hersteller, stark in Superyacht-Segment

**Produktlinien für Marine:**

| Produktlinie | SAE-Typ | Druckbereich | Besonderheit |
|-------------|---------|--------------|--------------|
| Rockmaster 1SN | 100R1 | 40–250 bar | Kompakter Aufbau |
| Rockmaster 2SN | 100R2 | 80–400 bar | Marine-Standard |
| Rockmaster 4SP | 100R12 | 210–420 bar | Spiralverstärkt |
| Superflex | 100R16/R17 | bis 400 bar | Ultrakompakt |
| Goldenfluid | PTFE | bis 280 bar | Chemische Medien |

**Besonderheit Manuli:**
- Italienische Werften (Benetti, Azimut, Ferretti) als Stammkunden
- Vor-Ort-Service in italienischen Yachthäfen
- Eigene Marine-Crimpmaschinen (Manuli ProFit)

### Vetus (Niederlande)

**Marktposition**: Marine-Spezialist, vollständige Steuerungssysteme

**Hydraulik-Steuerungssysteme:**

| Produkt | Typ | Bootsgrößen | Besonderheit |
|---------|-----|-------------|--------------|
| HTP20 | Hydraulikpumpe | 6–12 m | Einzel-Steuerstand |
| HTP42 | Hydraulikpumpe | 10–18 m | Doppelstation möglich |
| HTC52 | Steuerzylinder | bis 18 m | Für Innenbordruder |
| HTC82 | Steuerzylinder | bis 25 m | Für große Ruder |
| MTP42 | Power Assist Pump | 12–20 m | Servohydraulik |

**Vetus Hydraulikschläuche:**
- Eigene Schlauchsätze als Zubehör (vorkonfektioniert)
- Schlauch-DN: 6 mm (1/4") und 10 mm (3/8") Standard
- Fittings: BSP-Anschlüsse (europäischer Standard)
- Empfohlene Fluide: Vetus Hydraulic Steering Fluid (VG 15)
- Preisbereich Schlauchsatz: 85–220 EUR

### Lecomble & Schmitt (Frankreich)

**Marktposition**: Französischer Spezialist für Marine-Hydrauliksteuerung

**Steuerungssysteme:**

| Produkt | Typ | Bootsgrößen | Besonderheit |
|---------|-----|-------------|--------------|
| HB 4210 | Steuerpumpe | 7–14 m | Einzylindersteuerung |
| HB 4310 | Steuerpumpe | 12–20 m | Zweizylindersteuerung |
| HS 4810 | Servopumpe | 15–25 m | Elektrohydraulisch |
| CT 90 | Steuerzylinder | bis 14 m | Kompakt, Innenbord |
| CT 250 | Steuerzylinder | bis 25 m | Für schwere Ruder |

**Besonderheit:**
- Breite Verwendung in französischen Werften (Beneteau, Jeanneau, Lagoon)
- Proprietäre Schlauchsätze mit metrischen Anschlüssen
- Empfohlenes Fluid: LHM Plus (Citroen-Typ Mineralöl, VG 10)

### Kobelt Manufacturing (Kanada)

**Marktposition**: Premium-Hersteller für Steuerungshydraulik, Fischereiflotten und Yachten

**Steuerungssysteme:**

| Produkt | Typ | Anwendung | Besonderheit |
|---------|-----|-----------|--------------|
| Model 7003 | Steuerpumpe | 8–18 m | MIL-spec-Qualität |
| Model 7004 | Steuerpumpe | 15–30 m | Doppelstation |
| Model 7012 | Steuerpumpe | 25–60 m | Power Steering |
| Model 2020 | Steuerzylinder | bis 30 m | Edelstahl 316 |
| Model 6527 | Power Pack | 15–40 m | Elektrohydraulisch |

**Fittings**: JIC 37° Standard, Edelstahl 316 optional
**Schläuche**: SAE 100R2 empfohlen, JIC-Anschlüsse

### SeaStar Solutions / BayStar (Dometic Marine, USA)

**Marktposition**: Marktführer für Steuerungssysteme bis 15 m

**Produktlinien:**

| Produkt | Typ | Bootsgrößen | Besonderheit |
|---------|-----|-------------|--------------|
| BayStar HK4200A | Hydraulikkit | 6–9 m (Außenborder) | Budget-Steuerung |
| SeaStar Pro HK7500A | Hydraulikkit | 9–14 m (Außenborder) | Power Assist möglich |
| SeaStar HC5345 | Steuerzylinder | bis 14 m | Frontmontage |
| SeaStar HC5348 | Steuerzylinder | bis 14 m | Seitenmontage |
| SeaStar PA1200-2 | Power Assist | bis 18 m | Autopilot-kompatibel |

**SeaStar-Schläuche:**
- Thermoplastisch (SAE 100R7-Typ)
- Fittings: JIC 37° (-4, 1/4" Standard)
- Fluid: SeaStar Hydraulic Steering Fluid (ATF-basiert)
- Vorkonfektionierte Längen: 3 m, 6 m, 9 m, 12 m, 15 m, 18 m, 24 m
- Preise: 35 EUR (3 m) bis 120 EUR (24 m)

---

## Anlagen-spezifische Zuordnung

### Ruderhydraulik (Steering Systems)

#### Systemübersicht

```
[Steuerrad] → [Steuerpumpe] →→ Druckleitung →→ [Steuerzylinder] → [Ruderquadrant/Hebel]
                              ←← Rücklaufleitung ←←
                              ↕
                        [Ölvorratsbehälter]
                              ↕ (optional)
                        [Power Assist Pump]
                              ↕ (optional)
                        [Autopilot-Aktuator]
```

#### Druckbereiche nach Bootsgröße

| Bootsgröße | Arbeitsdruck | Schlauch-DN | SAE-Typ | Fluid |
|------------|-------------|-------------|---------|-------|
| 6–9 m (Gleiter) | 50–80 bar | 6 mm (1/4") | R7 | ATF |
| 9–14 m (Verdränger/Gleiter) | 70–120 bar | 6–10 mm | R7/R1 | ATF/HLP 15 |
| 14–20 m (Motor/Segel) | 100–180 bar | 10–12 mm | R2/R7 | HLP 22/32 |
| 20–30 m (Motoryacht) | 150–250 bar | 12–16 mm | R2 | HLP 32/46 |
| 30–45 m (Superyacht) | 180–300 bar | 16–25 mm | R2/R12 | HLP 46 |
| 45–60 m (Megayacht) | 200–350 bar | 19–32 mm | R12 | HLP 46/68 |

#### Schlauchlängen-Richtwerte (Steuerleitung)

| Bootsgröße | Steuerstand → Ruder | Hin + Rück | Empfohlene Zusatzlänge |
|------------|--------------------|-----------|-----------------------|
| 8 m | 3–5 m | 6–10 m | +20% für Bögen |
| 12 m | 5–8 m | 10–16 m | +20% |
| 18 m | 8–14 m | 16–28 m | +15% |
| 24 m | 12–20 m | 24–40 m | +15% |
| 35 m | 15–25 m | 30–50 m | +10% (Rohrleitungsanteil höher) |

#### Redundanz-Anforderungen

- **< 12 m**: Keine Redundanz erforderlich, Notpinne empfohlen
- **12–24 m, CE Kat. A/B**: Notsteuerung erforderlich (kann Notpinne sein)
- **> 24 m**: Redundante Hydraulik empfohlen (zwei unabhängige Systeme)
- **Klasse-Yachten**: Redundante Steuerhydraulik mit automatischer Umschaltung obligatorisch
- **> 45 m**: Zwei unabhängige Pumpen, zwei unabhängige Leitungssätze, Umschaltventil

### Stabilisatoren-Hydraulik

#### Flossen-Stabilisatoren (Fin Stabilizers)

**Hersteller und Systeme:**

| Hersteller | System | Bootsgrößen | Arbeitsdruck | Besonderheit |
|-----------|--------|-------------|-------------|--------------|
| Naiad Dynamics | NAIAD S1000 | 18–35 m | 140–210 bar | Marktführer Segelyachten |
| Naiad Dynamics | NAIAD D1500 | 25–60 m | 180–280 bar | Große Motoryachten |
| MC² Quick | MC² Quick Gyro | 12–25 m | 100–180 bar | Hybridstabilisierung |
| MC² Quick | MC² Quick Fin | 18–45 m | 150–250 bar | Zero-Speed-Fähigkeit |
| Humphree | Interceptor | 10–30 m | 100–180 bar | Trimmklappen-Integration |
| ABT TRAC | Fin Stabilizer | 20–60 m | 160–300 bar | Nordische Qualität |
| Quantum Marine | MAGLift | 20–80 m | 180–350 bar | Zero-Speed |

**Typischer Schlauchbedarf Stabilisator (pro Seite):**
- 2× Druckleitung (Extend/Retract): DN 12–19, SAE R2/R12, je 2–4 m
- 2× Rücklaufleitung: DN 16–25, SAE R1/R2, je 2–4 m
- 1× Leckölleitung: DN 6–10, SAE R1/R5, 2–4 m
- **Gesamt pro Seite**: 5 Schläuche, 10–20 m Schlauchlänge
- **Gesamt beide Seiten**: 10 Schläuche, 20–40 m Schlauchlänge

**Besonderheiten Stabilisator-Schläuche:**
- Hohe Impulsfestigkeit erforderlich (kontinuierliche Regelbewegung)
- Empfehlung: min. 500.000 Impulszyklen (Parker GlobalCore 482/487)
- Kurze, gerade Schlauchlängen bevorzugen (weniger Druckverlust)
- Vibrationsdämpfende Befestigung erforderlich
- Regelmäßige Ölanalyse (Partikelzählung) empfohlen

### Winsch-Hydraulik (Hydraulic Winches)

**Hersteller und Systeme:**

| Hersteller | System | Bootsgrößen | Arbeitsdruck | Anwendung |
|-----------|--------|-------------|-------------|-----------|
| Lewmar | H-Series | 12–25 m | 150–250 bar | Segel-/Motoryachten |
| Lewmar | V-Series | 20–60 m | 200–350 bar | Superyachten |
| Harken | UniPower | 14–30 m Segel | 150–280 bar | Regatta/Cruising |
| Harken | Performa | 25–60 m Segel | 200–350 bar | Superyacht-Segler |
| Reckmann | HS-Series | 20–60 m Segel | 180–300 bar | Rollreffsysteme |
| Reckmann | HW-Series | 18–50 m | 180–280 bar | Hydraulik-Winschen |
| Antal | W-Series | 12–25 m | 150–250 bar | Mittelmeer-Yachten |
| Pontos | Marine Winch | 12–30 m | 150–280 bar | Cruising-Yachten |

**Typischer Schlauchbedarf Winschsystem:**
- Pro Winsch: 2× Druckleitung + 2× Rücklauf (DN 10–16)
- Versorgungsleitung Power Pack → Deck: DN 12–25, Länge 5–15 m
- Rücklaufleitung Deck → Tank: DN 16–32, Länge 5–15 m
- **4 Winschen + Furler**: ca. 12 Schlauchverbindungen, 40–80 m Gesamtlänge

**Besonderheiten Winsch-Schläuche:**
- Decksdurchführungen müssen wasserdicht sein
- UV-geschützte Außendecke für Deck-verlegte Schläuche
- Schnellkupplungen an Winschen für einfachen Anschluss
- Druckspitzen beim Winschstart berücksichtigen (+30% über Nennarbeitsdruck)

### Bugstrahlruder-Hydraulik (Bow/Stern Thrusters)

**Hersteller und Systeme:**

| Hersteller | System | Schubkraft | Arbeitsdruck | Bootsgrößen |
|-----------|--------|-----------|-------------|-------------|
| Side-Power | SH80-SH240 | 80–240 kgf | 100–200 bar | 8–25 m |
| Side-Power | SH420-SH740 | 420–740 kgf | 150–280 bar | 20–45 m |
| Vetus | BOW/STERN PRO | 45–180 kgf | 80–180 bar | 6–20 m |
| Vetus | MAXPOWER | 110–340 kgf | 120–220 bar | 12–30 m |
| Lewmar | HB/HT Series | 100–300 kgf | 120–250 bar | 10–30 m |
| ABT TRAC | Retractable | 150–600 kgf | 150–300 bar | 15–60 m |
| Craftsman Marine | HYD | 80–200 kgf | 100–200 bar | 8–20 m |

**Typischer Schlauchbedarf Bugstrahlruder:**
- 2× Druckleitung: DN 12–25, SAE R2, je 3–8 m
- 2× Rücklauf: DN 16–25, SAE R1/R2, je 3–8 m
- 1× Saugleitung (zum Tank): DN 25–38, SAE R4 (Saugschlauch), 1–3 m
- **Gesamt**: 5 Schläuche, 15–30 m Gesamtlänge

---

## Schlauchschellen & Verbindungstechnik

### Crimp-Fittings (Permanente Pressung)

**Prinzip**: Der Fitting wird maschinell auf den Schlauch gepresst (gecrimpt). Die Hülse verformt sich plastisch und erzeugt eine formschlüssige Verbindung.

**Vorteile:**
- Höchste Sicherheit (keine Lockerung durch Vibration)
- Reproduzierbare Qualität (definierte Crimp-Durchmesser)
- Kein Nachziehen erforderlich
- SAE J1942 Marine-konform

**Nachteile:**
- Erfordert Crimpmaschine (ca. 3.000–15.000 EUR)
- Nicht auf See reparierbar (ohne mobile Maschine)
- Verschiedene Crimpdorne für verschiedene Schlauch/Fitting-Kombinationen

**Marine-Crimpmaschinen:**

| Hersteller | Modell | Typ | Crimpbereich | Preis (EUR) |
|-----------|--------|-----|-------------|-------------|
| Parker | Karrykrimp 2 (82C-080) | Mobil | DN 6–32 | ca. 8.500 |
| Parker | Parkrimp 2 (85C-A01) | Stationär | DN 3–51 | ca. 12.000 |
| Gates | GC20 MobileCrimp | Mobil | DN 6–25 | ca. 7.800 |
| Gates | GC32 MegaCrimp | Stationär | DN 6–51 | ca. 14.000 |
| Uniflex | HM 200 | Portabel | DN 6–32 | ca. 9.500 |
| Finn-Power | P20CS | Stationär | DN 6–51 | ca. 11.000 |
| Manuli | ProFit M200 | Portabel | DN 6–25 | ca. 7.200 |

### Reusable-Fittings (Wiederverwendbare Verschraubung)

**Prinzip**: Überwurfmutter drückt Klemmhülse auf Schlauch, kann mit Schraubenschlüssel montiert werden.

**Vorteile:**
- Montage an Bord ohne Spezialwerkzeug
- Wiederverwendbar bei Schlauchwechsel
- Notreparatur auf See möglich

**Nachteile:**
- Lockerung durch Vibration möglich (Nachziehen nötig)
- Nicht für alle SAE-Typen verfügbar (R1, R2, R5 ja; R12, R13 nein)
- Geringere Sicherheitsmarge als Crimp
- SAE J1942: nur für Leitungen ≤ 100 bar empfohlen

**Typische Reusable-Fittings:**
- Parker 10143/10243: Reusable für R1/R2
- Eaton Weatherhead: Coll-O-Crimp reusable
- Aeroquip FD83: Reusable Field Attachable

### Drehgelenke (Swivel Fittings)
- Ermöglichen Rotation an Fitting-Anschlüssen
- Essentiell bei Ruderzylindern (Bewegung des Ruderquadranten)
- Material: Edelstahl 316L empfohlen
- O-Ring-Dichtung: FKM/Viton für Langlebigkeit

### Schnellkupplungen (Quick Disconnect)
- **Flat-Face-Kupplungen**: Tropffreies Trennen, für Deckwinschen
- **ISO A (Push-Pull)**: Standard, nicht tropffrei
- **ISO B (Schraubkupplung)**: Vibrationssicher, nicht tropffrei
- **Stäubli**: Premium-Qualität, Serienpreise 45–150 EUR

---

## Technische Referenz & Berechnungen

### Druckverlustberechnung

**Formel (Darcy-Weisbach für Schläuche):**

```
Δp = λ × (L/d) × (ρ × v²) / 2

Wobei:
  Δp = Druckverlust (Pa)
  λ  = Rohrreibungszahl (Schlauch: 0.02–0.04)
  L  = Schlauchlänge (m)
  d  = Innendurchmesser (m)
  ρ  = Fluiddichte (kg/m³), Hydrauliköl: ~870 kg/m³
  v  = Strömungsgeschwindigkeit (m/s)
```

**Empfohlene Strömungsgeschwindigkeiten:**

| Leitung | Geschwindigkeit (m/s) | Max. (m/s) |
|---------|----------------------|------------|
| Druckleitung | 3–5 | 6 |
| Rücklaufleitung | 2–3 | 4 |
| Saugleitung | 0.5–1.5 | 2 |

**Volumenstrom-Berechnung:**

```
Q = v × A = v × π × (d/2)²

Wobei:
  Q = Volumenstrom (m³/s)
  v = Geschwindigkeit (m/s)
  A = Querschnittsfläche (m²)
  d = Innendurchmesser (m)
```

**Praktische Richtwerte Druckverlust:**

| DN (mm) | Q (l/min) | v (m/s) | Δp (bar/m) |
|---------|-----------|---------|------------|
| 6 | 5 | 2.9 | 0.35 |
| 8 | 10 | 3.3 | 0.28 |
| 10 | 15 | 3.2 | 0.18 |
| 12 | 25 | 3.7 | 0.16 |
| 16 | 40 | 3.3 | 0.09 |
| 19 | 60 | 3.5 | 0.07 |
| 25 | 100 | 3.4 | 0.04 |

### Schlauch-Dimensionierung

```python
def calculate_hose_size(
    flow_rate_lpm: float,
    max_velocity_mps: float = 4.0,
) -> float:
    """
    Calculate minimum hose inner diameter.

    Args:
        flow_rate_lpm: Flow rate in liters per minute
        max_velocity_mps: Maximum allowed velocity in m/s

    Returns:
        Minimum inner diameter in mm
    """
    import math
    q_m3s = flow_rate_lpm / 60000  # l/min → m³/s
    area_m2 = q_m3s / max_velocity_mps
    d_m = math.sqrt(4 * area_m2 / math.pi)
    d_mm = d_m * 1000
    # Round up to next standard DN
    standard_dns = [5, 6, 8, 10, 12, 16, 19, 25, 32, 38, 51]
    for dn in standard_dns:
        if dn >= d_mm:
            return dn
    return standard_dns[-1]
```

### Lebensdauer-Berechnung

```python
def calculate_hose_remaining_life(
    installation_date: str,
    max_life_years: int = 6,
    condition_score: int = 50,
    application: str = "steering",
) -> dict:
    """
    Calculate remaining service life and replacement urgency.

    Returns dict with remaining_years, urgency, and recommendation (German).
    """
    from datetime import date, datetime

    install = datetime.strptime(installation_date, "%Y-%m-%d").date()
    age_days = (date.today() - install).days
    age_years = age_days / 365.25

    remaining = max_life_years - age_years

    # Condition-adjusted remaining life
    if condition_score < 25:
        remaining = 0  # Immediate replacement
        urgency = "immediate"
    elif condition_score < 50:
        remaining = min(remaining, 0.5)
        urgency = "soon"
    elif condition_score < 70:
        remaining = min(remaining, remaining * 0.7)
        urgency = "planned"
    else:
        urgency = "routine" if remaining > 1 else "planned"

    # Application criticality factor
    critical_apps = {"steering", "stabilizer"}
    if application in critical_apps and remaining < 1:
        urgency = "soon" if urgency == "planned" else urgency

    recommendation = {
        "immediate": "SOFORTIGER Austausch erforderlich — sicherheitskritisch!",
        "soon": "Austausch innerhalb der nächsten 3 Monate einplanen.",
        "planned": "Austausch bei nächster planmäßiger Wartung vornehmen.",
        "routine": "Routinemäßige Überwachung fortsetzen.",
    }

    return {
        "age_years": round(age_years, 1),
        "remaining_years": round(max(0, remaining), 1),
        "urgency": urgency,
        "recommendation_de": recommendation[urgency],
    }
```

### Kosten-Schätzung

```python
def estimate_hose_replacement_cost(
    sae_type: str,
    inner_diameter_mm: float,
    length_mm: float,
    fitting_type: str = "jic_37",
    fitting_material: str = "steel_zinc",
    quantity: int = 1,
) -> dict:
    """
    Estimate cost for hydraulic hose assembly replacement.

    Returns dict with material_cost, labor_cost, total_cost in EUR.
    """
    # Base hose cost per meter (EUR/m)
    hose_costs = {
        "100R1": {6: 8, 8: 10, 10: 14, 12: 18, 16: 22, 19: 28, 25: 38},
        "100R2": {6: 12, 8: 16, 10: 22, 12: 28, 16: 36, 19: 44, 25: 58},
        "100R7": {6: 10, 8: 14, 10: 20, 12: 26},
        "100R12": {12: 38, 16: 48, 19: 62, 25: 82, 32: 105},
        "100R14": {6: 28, 8: 38, 10: 52, 12: 68},
    }

    dn = int(inner_diameter_mm)
    costs = hose_costs.get(sae_type, hose_costs["100R2"])
    cost_per_m = costs.get(dn, 25)  # Default fallback

    length_m = length_mm / 1000
    hose_material = cost_per_m * length_m

    # Fitting costs (pair)
    fitting_costs = {
        "jic_37": {"steel_zinc": 12, "steel_316": 45, "brass": 18},
        "sae_oring": {"steel_zinc": 18, "steel_316": 55},
        "bsp_parallel": {"steel_zinc": 10, "steel_316": 40, "brass": 15},
        "metric_s": {"steel_zinc": 14, "steel_316": 48},
        "orfs": {"steel_zinc": 22, "steel_316": 65},
    }
    fitting_pair = fitting_costs.get(fitting_type, {}).get(fitting_material, 20) * 2

    # Crimping cost
    crimp_cost = 15  # EUR per end, standard

    material_total = (hose_material + fitting_pair + crimp_cost * 2) * quantity

    # Labor estimate (EUR)
    labor_per_hose = 45 + length_m * 15  # Base + per meter
    labor_total = labor_per_hose * quantity

    return {
        "hose_material_eur": round(hose_material * quantity, 2),
        "fittings_eur": round(fitting_pair * quantity, 2),
        "crimping_eur": round(crimp_cost * 2 * quantity, 2),
        "material_total_eur": round(material_total, 2),
        "labor_eur": round(labor_total, 2),
        "total_eur": round(material_total + labor_total, 2),
        "confidence": "estimated",
    }
```

---

## Einbau-/Austausch-Anleitung

### Vorbereitung

1. **System drucklos machen**: Lenkrad/Steuerstand mehrfach hin und her bewegen bei abgestelltem Motor
2. **Auffangwanne** unter alle Anschlüsse stellen (Ölbindemittel bereithalten)
3. **Alten Schlauch fotografieren**: Verlegung, Befestigungspunkte, Fittingtypen dokumentieren
4. **Neuen Schlauch prüfen**: Korrekte Länge, Fittings, SAE-Typ, Druckklasse
5. **Sauberkeit**: Schutzstopfen erst unmittelbar vor Montage entfernen

### Demontage

1. Auffangbehälter positionieren
2. Gabelschlüssel an Fitting und Gegenstück ansetzen (ZWEI Schlüssel, Kontern!)
3. Fitting langsam lösen — Restdruck entweichen lassen
4. Schlauch abnehmen, Anschlüsse sofort mit Stopfen verschließen
5. Altöl-Menge dokumentieren (für Neubefüllung)
6. Fitting-Gewinde und Dichtflächen inspizieren

### Montage

1. **Schlauch nicht verdrillen**: Linie auf Schlauchdecke als Referenz verwenden
2. **Mindestbiegeradius einhalten**: Siehe Herstellerangabe, nie knicken
3. **Fitting handfest anziehen**, dann mit Drehmomentschlüssel:

| Fitting-Größe | JIC Drehmoment (Nm) | BSP Drehmoment (Nm) | Metrisch Drehmoment (Nm) |
|--------------|---------------------|---------------------|-------------------------|
| -4 / 1/4" | 14–16 | 20–25 | 18–22 |
| -6 / 3/8" | 24–27 | 35–40 | 30–35 |
| -8 / 1/2" | 50–55 | 60–70 | 55–65 |
| -10 / 5/8" | 75–80 | 85–95 | 80–90 |
| -12 / 3/4" | 100–110 | 110–125 | 105–120 |
| -16 / 1" | 140–160 | 155–175 | 145–165 |

4. **Schlauchbefestigung**: Schellen alle 300–500 mm, Gummipuffer gegen Scheuern
5. **Thermische Abstände**: Min. 50 mm zu heißen Oberflächen, 25 mm zu beweglichen Teilen
6. **Bewegungsfreiheit**: Schlauch muss bei max. Lenkeinschlag/Ruderlage spannungsfrei liegen

### Befüllung und Entlüftung

1. Hydraulikfluid gemäß Herstellervorgabe einfüllen (Typ und Viskosität prüfen!)
2. **Entlüften**: Lenkrad mehrfach von Anschlag zu Anschlag drehen (20–30×)
3. Fluidstand prüfen und nachfüllen
4. Auf Leckagen prüfen (alle Anschlüsse)
5. Erneut entlüften — Luft im System = schwammige Steuerung
6. **Druckprüfung**: System auf Arbeitsdruck bringen, 5 min halten
7. Alle Fittings nochmals auf Leckage prüfen
8. Fluidstand final prüfen

### Dokumentation

- Schlauch-Typ, Hersteller, Teilenummer notieren
- Installationsdatum auf Schlauch markieren (Kabelbinder mit Beschriftung)
- Foto der fertigen Installation anfertigen
- Wartungsprotokoll aktualisieren
- Nächste Inspektion terminieren (max. 12 Monate)

---

## Lebensdauer und Alterungsmechanismen

### Maximale Lebensdauer

| Vorgabe | Max. Lebensdauer | Bemerkung |
|---------|-----------------|-----------|
| DNV-GL Klasse | 6 Jahre | Unabhängig vom Zustand |
| SAE J1942 (Marine) | 10 Jahre (Lagerung) + 5 Jahre (Betrieb) | Oder 15 Jahre ab Herstellung |
| Parker Empfehlung | 6 Jahre Betrieb | Für Marine-Anwendungen |
| Gates Empfehlung | 6–10 Jahre | Je nach Anwendung/Bedingung |
| ABYC H-32 | Keine feste Grenze | Zustandsbasiert, jährliche Inspektion |
| Praxis-Empfehlung AYDI | **6 Jahre (Ruder/Stabilisator)** | **8 Jahre (Winschen/Thruster)** |

### Alterungsmechanismen

#### 1. Innere Alterung (Innenrohr)
- **Chemischer Angriff**: Hydraulikfluid-Zersetzungsprodukte greifen NBR an
- **Hydrolyse**: Wasser im Hydrauliköl → NBR-Quellung → Erweichung
- **Temperaturalterung**: Jede 10°C über Nenntemperatur halbiert die Lebensdauer
- **Abrasion**: Partikel im Öl schleifen Innenrohr → Partikelgeneration → Kettenreaktion
- **Erkennung**: Dunkle Partikel im Ölfilter, Ölanalyse zeigt erhöhte Gummiwerte

#### 2. Äußere Alterung (Außendecke)
- **UV-Degradation**: Sonnenlicht → CR/NBR-Verhärtung → Rissbildung
- **Ozonrissbildung**: Ozon → Mikrorisse quer zur Beanspruchungsrichtung
- **Abrasion**: Scheuern an Schotts, Kabeln, anderen Schläuchen
- **Chemischer Angriff**: Diesel, Lösungsmittel, Batteriesäure auf Außendecke
- **Erkennung**: Sichtbare Risse, Verhärtung, Farbveränderung

#### 3. Drahtgeflecht-Ermüdung
- **Impulsfatigue**: Zyklische Druckschwankungen → Drahtbrüche → Beulbildung
- **Korrosion**: Feuchtigkeit durch beschädigte Außendecke → Drahtrostung
- **Erkennung**: Lokale Aufblähung (Beule), Rost an Schnittflächen

#### 4. Fitting-Alterung
- **Korrosion**: Salzluft auf Stahl-Fittings → Rost → Undichtheit
- **Spannungsrisskorrosion**: 316L-Edelstahl bei Cl⁻-Konzentration + Spannung
- **O-Ring-Alterung**: Aushärtung, Druckverformungsrest → Undichtheit
- **Lockerung**: Vibration → Fitting-Lösung (bei Reusable-Fittings)
- **Erkennung**: Ölfilm, Tropfenbildung, Salzablagerungen, Korrosionsspuren

#### 5. Biegeradius-Ermüdung
- **Dauerbiegung**: Wiederholte Biegung unter Mindestradius → Innenrohrfalte → Riss
- **Torsion**: Verdrehter Schlauch + Druck → beschleunigte Ermüdung
- **Erkennung**: Falte, Abflachung, Knick im Schlauchverlauf

### Lebensdauer-Verlängerung: Best Practices

1. **Ölpflege**: Jährliche Ölanalyse (Partikelzählung, Wassergehalt, Säurezahl)
2. **UV-Schutz**: Schläuche an Deck mit Spiralschutz oder Textilmantel umhüllen
3. **Temperaturkontrolle**: Maschinenraum-Belüftung optimieren
4. **Scheuerschutz**: Gummipuffer an allen Kontaktstellen
5. **Druckbegrenzung**: Überdruckventil korrekt eingestellt
6. **Fluidwechsel**: Alle 2 Jahre oder 1.000 Betriebsstunden
7. **Filterwechsel**: Alle 500 Betriebsstunden oder jährlich
8. **Sichtprüfung**: Quartalsweise auf Risse, Leckagen, Scheuerstellen

---

## Fehlerbild-Atlas

### Fehlerbild 1: Außendeckenrisse (UV-Degradation)
- **Erscheinung**: Netzartige Oberflächenrisse, parallel zur Schlauchachse, Verhärtung des Mantels
- **Ursache**: UV-Strahlung auf ungeschütztem Schlauch, typisch bei Deckverlegung ohne Schutz
- **Häufigkeit**: Sehr häufig bei Mittelmeer-Yachten, ab 3–4 Jahren Exposition
- **Betroffene Schläuche**: Alle mit CR-Außendecke ohne UV-Schutz
- **Bewertung**: Score 40–60, Austausch innerhalb 12 Monate planen
- **Risiko**: Feuchtigkeit dringt zum Drahtgeflecht → Korrosion → Festigkeitsverlust
- **Sofortmaßnahme**: Spiralschutzschlauch aufbringen, Inspektion intensivieren
- **Vermeidung**: EPDM-Außendecke wählen, Spiralschutz ab Montage installieren
- **Confidence**: visual_high (eindeutiges Schadensbild)
- **AYDI-Trigger**: "Risse", "spröde", "hart", "UV", "Deck"
- **Kosten Austausch**: 120–350 EUR pro Schlauch (inkl. Arbeit)
- **Normverweis**: SAE J1942 Abschnitt 4.5 — Umgebungsbedingungen

### Fehlerbild 2: Leckage an Crimpverbindung
- **Erscheinung**: Ölfilm oder Tropfenbildung an der Übergangszone Schlauch/Fitting
- **Ursache**: Falsche Crimpdurchmesser, Schlauch/Fitting-Inkompatibilität, Alterung
- **Häufigkeit**: Mittelhäufig, oft nach 5+ Jahren oder bei Billigfittings
- **Betroffene Schläuche**: Alle Crimp-Verbindungen, häufiger bei No-Name-Produkten
- **Bewertung**: Score 20–40, Austausch zeitnah (3–6 Monate), bei Steuerung sofort
- **Risiko**: Progressiver Druckverlust, Systemversagen, Ölverschmutzung
- **Sofortmaßnahme**: Leckrate dokumentieren, Fluidstand überwachen, ggf. Notsteuerung
- **Vermeidung**: Nur OEM-zugelassene Schlauch/Fitting-Kombinationen, Crimp-Protokoll
- **Confidence**: visual_high
- **AYDI-Trigger**: "Leck", "tropft", "Öl", "Fitting", "nass"
- **Kosten Austausch**: 80–250 EUR pro Verbindung
- **Normverweis**: SAE J517 Anhang — Crimpspezifikationen

### Fehlerbild 3: Schlauchbeule (Drahtbruch)
- **Erscheinung**: Lokale Aufblähung des Schlauchs, oft einseitig, 20–50 mm Ausdehnung
- **Ursache**: Drahtgeflechtbrüche durch Impulsfatigue oder Korrosion
- **Häufigkeit**: Selten bis mittelhäufig, typisch bei Stabilisator-Schläuchen
- **Bewertung**: Score 0–15, **SOFORTIGER Austausch** — Berstgefahr!
- **Risiko**: Berstversagen unter Druck, Hochdruck-Ölstrahl = Injektionsverletzung
- **Sofortmaßnahme**: System sofort drucklos machen, Anlage nicht mehr betreiben
- **Vermeidung**: Regelmäßige Sichtinspektion, Lebensdauergrenzen einhalten
- **Confidence**: visual_high (sehr eindeutig)
- **AYDI-Trigger**: "Beule", "aufgebläht", "Blase", "geschwollen"
- **Kosten Austausch**: 150–400 EUR
- **Normverweis**: ISO 6803 — Impulsprüfung, Lebensdauergrenzen
- **SICHERHEITSHINWEIS**: Schlauch mit Beule NICHT berühren wenn unter Druck!

### Fehlerbild 4: Fitting-Korrosion (Salzwasser)
- **Erscheinung**: Rotbraune Rostablagerungen, weiße Salzausblühungen auf Fittings
- **Ursache**: Stahl-Fittings (nicht Edelstahl) in Salzwasserumgebung
- **Häufigkeit**: Häufig bei verzinkten Fittings im Maschinenraum von Salzwasseryachten
- **Bewertung**: Score 30–50, Austausch planen, auf Edelstahl 316L upgraden
- **Risiko**: Gewindekorrosion → Undichtheit, Fitting-Bruch unter Last
- **Sofortmaßnahme**: Korrosionsschutzspray auftragen, engmaschig kontrollieren
- **Vermeidung**: 316L-Edelstahl-Fittings verwenden, Korrosionsschutz auftragen
- **Confidence**: visual_high
- **AYDI-Trigger**: "Rost", "Korrosion", "Salz", "weiß", "braun", "Fitting"
- **Kosten Austausch**: 100–300 EUR (Upgrade auf 316L: +30–80 EUR/Paar)
- **Normverweis**: ABYC H-32 — Material requirements

### Fehlerbild 5: Knick im Schlauch (Unterschreitung Biegeradius)
- **Erscheinung**: Scharfer Knick oder Falte im Schlauchverlauf, Querschnittsverengung
- **Ursache**: Falsche Verlegung, zu kurzer Schlauch, fehlende Führung
- **Häufigkeit**: Häufig bei Eigeneinbauten und nachträglichen Änderungen
- **Bewertung**: Score 20–40, Neuverlegung oder Verlängerung erforderlich
- **Risiko**: Strömungswiderstand erhöht, Innenrohrfalte → Riss → Leckage
- **Sofortmaßnahme**: Schlauchverlauf korrigieren, ggf. Bogenadapter einsetzen
- **Vermeidung**: Mindestbiegeradius beachten, 90°-Bogen-Fittings verwenden
- **Confidence**: visual_high
- **AYDI-Trigger**: "Knick", "geknickt", "Bogen", "Schleife", "eng"
- **Kosten Korrektur**: 60–200 EUR (Neuverlegung: 150–400 EUR)
- **Normverweis**: Herstellerangabe Mindestbiegeradius, SAE J517

### Fehlerbild 6: Scheuerstelle (Abrasion)
- **Erscheinung**: Aufgeraute, dünne Stelle in der Außendecke, ggf. Drahtgeflecht sichtbar
- **Ursache**: Schlauch scheuert an Schott, Rohr, Kabel oder anderem Schlauch
- **Häufigkeit**: Sehr häufig, besonders in engen Maschinenräumen
- **Bewertung**: Score 30–55, je nach Tiefe der Scheuerstelle
- **Risiko**: Drahtgeflecht-Freilegung → Korrosion → Festigkeitsverlust
- **Sofortmaßnahme**: Scheuerschutz anbringen (Spiralschutz, Gummipuffer)
- **Vermeidung**: Schlauchschellen mit Gummipuffer, Trennlagen zwischen Schläuchen
- **Confidence**: visual_high
- **AYDI-Trigger**: "scheuert", "durchgescheuert", "Abrieb", "dünn", "blank"
- **Kosten Reparatur**: 20–50 EUR (Schutz), 150–350 EUR (Austausch wenn tiefgreifend)
- **Normverweis**: ABYC H-32 — Hose protection

### Fehlerbild 7: Ölverfärbung / Fluid-Degradation
- **Erscheinung**: Hydraulikfluid dunkel verfärbt, trüb, Geruch nach verbrannt
- **Ursache**: Überhitzung, Oxidation, Wassereinbruch, Partikelkontamination
- **Häufigkeit**: Mittelhäufig, oft bei mangelhafter Wartung
- **Bewertung**: Score 35–55, Ölwechsel erforderlich, Ursache ermitteln
- **Risiko**: Beschleunigter Verschleiß aller Hydraulikkomponenten
- **Sofortmaßnahme**: Ölprobe entnehmen → Laboranalyse, Fluidwechsel planen
- **Vermeidung**: Regelmäßiger Ölwechsel (2 Jahre), Filterwechsel (jährlich)
- **Confidence**: visual_medium (Farbbeurteilung subjektiv)
- **AYDI-Trigger**: "dunkel", "Öl", "schwarz", "trüb", "Geruch"
- **Kosten Ölwechsel**: 80–400 EUR (je nach Systemgröße und Fluidtyp)
- **Normverweis**: ISO 4406 — Partikelzählung, Reinheitsklassen

### Fehlerbild 8: Schwammige Lenkung (Luft im System)
- **Erscheinung**: Steuerrad fühlt sich weich an, unpräzise Lenkung, Nachlauf
- **Ursache**: Luft im Hydrauliksystem, oft nach Wartung oder bei Mikroleckage
- **Häufigkeit**: Häufig nach Schlauchwechsel ohne korrekte Entlüftung
- **Bewertung**: Score 40–60, Entlüftung erforderlich
- **Risiko**: Eingeschränkte Steuerungspräzision, bei viel Luft: Lenkversagen
- **Sofortmaßnahme**: System entlüften (Lenkrad 20–30× Anschlag zu Anschlag)
- **Vermeidung**: Sorgfältige Entlüftung nach jeder Wartung, Fluidstand prüfen
- **Confidence**: documented (Symptom, nicht visuell)
- **AYDI-Trigger**: "schwammig", "weich", "unpräzise", "Luft", "Entlüften"
- **Kosten**: 50–120 EUR (Entlüftung + Fluidnachfüllung)
- **Normverweis**: Herstelleranweisung Entlüftungsverfahren

### Fehlerbild 9: Schlauchverformung unter Druck (Volumenzunahme)
- **Erscheinung**: Schlauch dehnt sich unter Druck sichtbar aus, ø-Zunahme >5%
- **Ursache**: Alterung des Innenrohrs, falscher Schlauchtyp, thermoplastische Verformung
- **Häufigkeit**: Selten bei korrekter Auswahl, häufig bei Billigschläuchen
- **Bewertung**: Score 25–45, Austausch erforderlich
- **Risiko**: Verzögerte Steuerreaktion (Sponge-Effekt), erhöhter Energieverbrauch
- **Sofortmaßnahme**: Drucktest dokumentieren, Schlauch markieren
- **Vermeidung**: Qualitätsschläuche verwenden, SAE J1942-konform
- **Confidence**: visual_medium (erfordert Druckvergleich)
- **AYDI-Trigger**: "aufblähen", "dick", "weich unter Druck", "Dehnung"
- **Kosten Austausch**: 120–350 EUR
- **Normverweis**: SAE J517 — Volumetric expansion limits

### Fehlerbild 10: Mikroleckage (Schwitzwasser)
- **Erscheinung**: Hauchfeiner Ölfilm an Fitting oder Schlauchoberfläche, kein sichtbarer Tropfen
- **Ursache**: Porösität des Schlauchmaterials, Mikrorisse, O-Ring-Druckverformungsrest
- **Häufigkeit**: Häufig bei älteren Schläuchen (>5 Jahre), oft übersehen
- **Bewertung**: Score 40–55, Beobachtung und Planung
- **Risiko**: Schleichender Fluidverlust, Verschmutzung, Brandgefahr bei heißen Teilen
- **Sofortmaßnahme**: Reinigen, markieren, nach 24h/7d kontrollieren
- **Vermeidung**: Lebensdauergrenzen einhalten, regelmäßige Inspektion
- **Confidence**: visual_medium (schwer erkennbar)
- **AYDI-Trigger**: "feucht", "Ölfilm", "schwitzt", "Film"
- **Kosten**: 80–250 EUR (Austausch wenn progressiv)
- **Normverweis**: SAE J343 — Permeation test

### Fehlerbild 11: Verdrehter Schlauch (Torsion)
- **Erscheinung**: Layline (Linie auf Schlauchdecke) spiralförmig verdreht statt gerade
- **Ursache**: Falsche Montage, Schlauch beim Anziehen verdreht
- **Häufigkeit**: Häufig bei Eigeneinbauten
- **Bewertung**: Score 35–50, je nach Verdrehungsgrad
- **Risiko**: 70% reduzierte Lebensdauer, erhöhtes Berstrisiko
- **Sofortmaßnahme**: Fitting lösen, Schlauch gerade richten, neu anziehen
- **Vermeidung**: Layline beachten, Fitting kontern beim Anziehen
- **Confidence**: visual_high (Layline ist eindeutiger Indikator)
- **AYDI-Trigger**: "verdreht", "Torsion", "spiralförmig", "Linie"
- **Kosten**: 40–80 EUR (Neuausrichtung), 150–350 EUR (Austausch)
- **Normverweis**: SAE J1273 — Recommended practices for hydraulic hose assemblies

### Fehlerbild 12: Thermische Schädigung
- **Erscheinung**: Verhärtete, brüchige, verfärbte (braun/schwarz) Außendecke, Blasenbildung
- **Ursache**: Nahverlegung an Abgasanlage, Motor, Turbolader ohne ausreichenden Abstand
- **Häufigkeit**: Mittelhäufig in engen Maschinenräumen
- **Bewertung**: Score 15–35, zügiger Austausch, Ursache beheben
- **Risiko**: Festigkeitsverlust aller Schlauchschichten, Berstgefahr
- **Sofortmaßnahme**: Wärmeschutz anbringen, System auf Leckagen prüfen
- **Vermeidung**: Min. 50 mm Abstand zu heißen Teilen, Hitzeschutzhülle verwenden
- **Confidence**: visual_high
- **AYDI-Trigger**: "verbrannt", "braun", "hart", "spröde", "Hitze", "heiß"
- **Kosten**: 150–400 EUR (Austausch + Hitzeschutzhülle: 15–40 EUR/m)
- **Normverweis**: ABYC P-1 — Abstand zu Abgasanlagen, ISO 9094 — Brandschutz

---

## Fehlerbehebungs-Leitfaden

### Problem 1: Steuerung reagiert träge / schwammig

**Symptome:**
- Lenkrad fühlt sich weich an, erhöhter Leerweg
- Ruder reagiert verzögert auf Lenkeingabe
- Unpräzise Geradeausfahrt

**Mögliche Ursachen (Reihenfolge der Wahrscheinlichkeit):**
1. Luft im System (häufigste Ursache)
2. Niedriger Fluidstand
3. Schlauch mit Volumenzunahme (gealtert)
4. Interner Bypass im Steuerzylinder
5. Steuerpumpe verschlissen

**Diagnose-Schritte:**
1. Fluidstand prüfen → nachfüllen wenn nötig
2. System entlüften (20–30× Anschlag zu Anschlag)
3. Sichtprüfung aller Schläuche auf Aufblähung unter Druck
4. Druckmessung am Zylinder: Soll vs. Ist vergleichen
5. Wenn weiterhin schwammig: Zylinder/Pumpe prüfen lassen

**Kosten-Rahmen:**
- Entlüftung: 50–120 EUR
- Schlauchwechsel: 150–400 EUR
- Zylinderreparatur: 300–800 EUR
- Pumpenaustausch: 400–1.500 EUR

### Problem 2: Hydrauliköl-Leckage

**Symptome:**
- Ölflecken unter Hydraulikkomponenten
- Sinkender Fluidstand im Vorratsbehälter
- Ölgeruch im Maschinenraum

**Mögliche Ursachen:**
1. Undichte Fitting-Verbindung (häufigste)
2. Schlauch-Außendecke beschädigt → Leckage durch Geflecht
3. O-Ring im Fitting defekt
4. Zylinderdichtung undicht (nicht Schlauch!)
5. Pumpenanschluss undicht

**Diagnose-Schritte:**
1. Alle Fittings mit Papiertuch abtupfen → Leckstelle lokalisieren
2. UV-Lecksuchspray verwenden (Fluoreszenz unter UV-Lampe)
3. System auf Arbeitsdruck bringen → beobachten
4. Fitting nachziehen (NICHT überdrehen!)
5. Wenn weiterhin undicht: Schlauch/Fitting erneuern

**Kosten-Rahmen:**
- Nachziehen: 30–60 EUR
- O-Ring-Wechsel: 20–50 EUR
- Schlauchwechsel: 150–400 EUR
- Zylinderdichtung: 200–600 EUR

### Problem 3: Geräusche im Hydrauliksystem

**Symptome:**
- Pfeifgeräusche bei Lenkbewegung
- Klopfgeräusche (Kavitation)
- Brummgeräusche bei Autopilot-Betrieb

**Mögliche Ursachen:**
1. Luft im System → Pfeifen/Zischen
2. Kavitation → Klopfen (Saugleitung zu klein/lang oder Filter verstopft)
3. Überdruckventil spricht an → Hochfrequentes Pfeifen
4. Schlauch knickt bei Ruderbewegung → intermittierendes Geräusch
5. Pumpe verschlissen → mechanisches Brummen

**Diagnose-Schritte:**
1. Art des Geräuschs kategorisieren (Pfeifen/Klopfen/Brummen)
2. Zeitpunkt: Beim Lenken? Bei Autopilot? Im Stand?
3. Entlüften und Fluidstand prüfen
4. Saugfilter/Rücklauffilter prüfen
5. Schlauchverlegung bei Ruderbewegung beobachten

**Kosten-Rahmen:**
- Entlüftung: 50–120 EUR
- Filteraustausch: 30–80 EUR
- Schlauch-Neuverlegung: 150–400 EUR
- Pumpenaustausch: 400–1.500 EUR

### Problem 4: Steuerung blockiert / geht schwer

**Symptome:**
- Lenkrad lässt sich nur mit großem Kraftaufwand drehen
- Steuerung blockiert in einer Richtung
- Ruckartiges Lenken

**Mögliche Ursachen:**
1. Schlauch intern kollabiert (Innenrohr löst sich → blockiert Strömung)
2. Überdruckventil defekt (zu niedrig eingestellt)
3. Fluid falsche Viskosität (zu dick bei Kälte)
4. Zylinder mechanisch blockiert (Ruderlager)
5. Power-Assist-Pumpe ausgefallen

**Diagnose-Schritte:**
1. Druckmessgerät an beiden Zylinder-Anschlüssen installieren
2. Lenkbewegung ausführen → Druckdifferenz messen
3. Überdruckventil prüfen (Einstellwert vs. Ist)
4. Fluidtyp und Viskosität prüfen
5. Schläuche einzeln abklemmen → isolieren

**Kosten-Rahmen:**
- Schlauchwechsel: 150–400 EUR
- Überdruckventil: 80–250 EUR
- Fluidwechsel: 80–300 EUR
- Ruderlager: 500–2.000 EUR

### Problem 5: Hydrauliksystem überhitzt

**Symptome:**
- Hydraulikfluid >80°C (Messung am Tank)
- Thermische Verfärbung an Schläuchen
- Fluid riecht verbrannt

**Mögliche Ursachen:**
1. Zu kleine Schlauchdimensionierung → hoher Druckverlust → Wärmeentwicklung
2. Kontinuierlicher Bypass-Flow (defektes Ventil)
3. Zu hohe Zyklusrate (Stabilisatoren in rauer See)
4. Kühler verstopft/ausgefallen
5. Falsche Fluidviskosität

**Diagnose-Schritte:**
1. Öltemperatur messen (Infrarot-Thermometer)
2. Rücklauftemperatur vs. Tanktemperatur vergleichen
3. Kühler-Durchfluss prüfen (falls vorhanden)
4. Druckverlust über Schlauchleitungen messen
5. Hydraulik-Ölanalyse durchführen

**Kosten-Rahmen:**
- Schlauch-Upgrade (größerer DN): 200–600 EUR
- Ölkühler nachrüsten: 300–800 EUR
- Fluidwechsel: 80–300 EUR
- Systemoptimierung: 500–1.500 EUR

---

## FAQ — Häufig gestellte Fragen

### HY-001: Wie oft müssen Hydraulikschläuche auf einer Yacht ausgetauscht werden?
**Antwort**: Gemäß DNV-GL und Parker-Empfehlung alle **6 Jahre** für sicherheitskritische Systeme (Ruder, Stabilisatoren). Winschen und Thruster alle 8 Jahre. Unabhängig vom sichtbaren Zustand. Jährliche Sichtinspektion ist Pflicht.
**Confidence**: benchmark

### HY-002: Kann ich Hydraulikschläuche selbst anfertigen?
**Antwort**: Ja, wenn Sie über eine kalibrierte Crimpmaschine, die korrekten Crimpdorne und Erfahrung verfügen. Für Ruderanlagen empfiehlt AYDI professionelle Anfertigung. Reusable-Fittings sind für Notreparaturen an Bord geeignet, aber nicht als Dauerlösung für Steuerleitungen.
**Confidence**: benchmark

### HY-003: Sind SeaStar/BayStar-Schläuche mit anderen Systemen kompatibel?
**Antwort**: SeaStar verwendet proprietäre JIC-4 (1/4") Anschlüsse mit ATF-kompatiblen Thermoplastschläuchen. Standardschläuche SAE 100R7 mit JIC-4-Fittings sind kompatibel, sofern ATF-Verträglichkeit gegeben ist. NICHT mit Mineralöl-Systemen mischen!
**Confidence**: measured

### HY-004: Kann ich Mineralöl und ATF mischen?
**Antwort**: **NEIN!** Mineralöl (HLP/HVLP) und ATF sind chemisch inkompatibel. Mischung führt zu Dichtungsquellung, Schlammbildung, Systemausfall. Bei Systemwechsel: Komplettspülung mit dem neuen Fluid (3× füllen/entleeren).
**Confidence**: measured

### HY-005: Was kostet ein kompletter Hydraulikschlauch-Satz für eine 12-m-Yacht?
**Antwort**: Für eine typische 12-m-Segelyacht mit hydraulischer Steuerung: 2 Steuerschläuche (je 6–8 m, DN 6, R7) + Fittings = ca. 250–400 EUR Material + 200–350 EUR Arbeit. Gesamt: **450–750 EUR**.
**Confidence**: estimated

### HY-006: Wie erkenne ich den SAE-Typ meines Schlauchs?
**Antwort**: Auf der Außendecke ist der SAE-Typ aufgedruckt, z.B. "SAE 100R2AT" oder "EN 853 2SN". Bei verblasstem Aufdruck: Konstruktion prüfen (Drahtgeflechtlagen zählen an Schnittfläche) oder Hersteller-Datenblatt anfordern.
**Confidence**: benchmark

### HY-007: Brauche ich Edelstahl-Fittings?
**Antwort**: Für Salzwasser-Yachten **dringend empfohlen** (316L). Verzinkte Stahl-Fittings korrodieren im Salzwasserumfeld innerhalb 2–4 Jahren. Mehrkosten ca. 30–80 EUR pro Paar, aber deutlich längere Lebensdauer.
**Confidence**: benchmark

### HY-008: Was bedeutet "Dash-Size" bei Fittings?
**Antwort**: Die Dash-Size gibt den Nenn-Innendurchmesser in 1/16-Zoll-Schritten an. -4 = 4/16" = 1/4" = 6,35 mm. -8 = 8/16" = 1/2" = 12,7 mm. Die häufigsten Marine-Größen sind -4, -6, -8, -10, -12.
**Confidence**: measured

### HY-009: Wie entlüfte ich ein Hydraulik-Steuersystem?
**Antwort**: Motor abstellen. Lenkrad 20–30× von Anschlag zu Anschlag drehen. Fluidstand prüfen, nachfüllen. Vorgang wiederholen bis blasenfreies Lenken. Profisysteme haben Entlüftungsschrauben am Zylinder — dort ebenfalls entlüften.
**Confidence**: benchmark

### HY-010: Welches Öl gehört in meine Ruderhydraulik?
**Antwort**: **Immer** gemäß Hersteller! SeaStar/BayStar: ATF-basiert. Lecomble & Schmitt: LHM Plus (VG 10). Kobelt: HLP 15/22. Vetus: Eigenes VG 15. Im Zweifel: Typenschild am Steuerpumpengehäuse oder Bedienungsanleitung.
**Confidence**: benchmark

### HY-011: Sind biologisch abbaubare Hydraulikfluide empfehlenswert?
**Antwort**: HEES (synthetische Ester) sind für ökologisch sensible Reviere eine gute Alternative. Sie erfordern aber kompatible Dichtungen (FKM/Viton statt NBR). Kosten: 3–4× höher als Mineralöl. HETG (Pflanzenöl) ist temperaturempfindlicher und für Tropen nicht geeignet.
**Confidence**: benchmark

### HY-012: Kann ein Hydraulikschlauch explodieren?
**Antwort**: Ja. Ein geborstener Hochdruckschlauch setzt einen Ölstrahl mit enormem Druck frei (bis 420 bar). Dies kann zu **Injektionsverletzungen** führen — Hydrauliköl dringt durch die Haut ins Gewebe. Sofortige chirurgische Behandlung erforderlich! Nie mit bloßer Hand nach Leckagen tasten.
**Confidence**: measured

### HY-013: Was ist der Unterschied zwischen 1SN und 2SN?
**Antwort**: 1SN = 1 Drahtgeflechtlage (SAE R1), 2SN = 2 Drahtgeflechtlagen (SAE R2). 2SN hat ca. doppelten Arbeitsdruck bei gleichem Durchmesser. Für Ruderanlagen >12 m immer 2SN oder besser.
**Confidence**: measured

### HY-014: Wie lagere ich Ersatzschläuche an Bord?
**Antwort**: Trocken, dunkel, UV-geschützt. Schutzstopfen auf Fittings belassen. Nicht knicken, nicht auf engem Radius wickeln. Max. Lagerdauer: 10 Jahre (SAE J1942). Produktionsdatum auf Schlauch beachten.
**Confidence**: benchmark

### HY-015: Braucht mein Boot eine Notsteuerung?
**Antwort**: CE Kat. A/B über 12 m: Ja, Notsteuerung ist vorgeschrieben. Dies kann eine Notpinne, ein zweites unabhängiges Hydrauliksystem oder eine mechanische Verbindung sein. Regelmäßig testen!
**Confidence**: measured

### HY-016: Wie prüfe ich Hydraulikschläuche vor einer Langfahrt?
**Antwort**: 1) Sichtprüfung: Risse, Beulen, Scheuerstellen. 2) Fittings: Leckage, Korrosion. 3) Fluidstand prüfen. 4) Druckprüfung: Steuerung auf volle Ruderlage, 5 min halten. 5) Ersatzschlauch-Set an Bord haben.
**Confidence**: benchmark

### HY-017: Was ist SAE J1942 und warum ist es wichtig?
**Antwort**: SAE J1942 ist die spezifische Norm für **marine Hydraulikschläuche**. Sie enthält zusätzliche Anforderungen für Salzwasser, UV, Vibration und Temperaturwechsel, die über SAE J517 hinausgehen. Marine-zertifizierte Schläuche sind für Yachten die beste Wahl.
**Confidence**: measured

### HY-018: Kann ich einen 1SN-Schlauch durch einen 2SN ersetzen?
**Antwort**: Ja, ein Upgrade von 1SN auf 2SN ist immer zulässig (gleicher DN). Umgekehrt NIE! Der 2SN hat höheren Arbeitsdruck, ähnliche Flexibilität aber etwas größeren Außendurchmesser. Einbauraum prüfen.
**Confidence**: measured

### HY-019: Wann brauche ich Spiralschläuche (R12/R13)?
**Antwort**: Ab 250 bar Arbeitsdruck oder bei hoher Impulsfestigkeit (Stabilisatoren, große Winschen). Auf Yachten unter 25 m sind R2-Schläuche in der Regel ausreichend. Spiralschläuche haben größere Biegeradien und sind steifer.
**Confidence**: benchmark

### HY-020: Wie wichtig ist die Ölreinheit?
**Antwort**: Sehr wichtig. 75% aller Hydraulikausfälle sind auf Partikelkontamination zurückzuführen. Empfohlene Reinheitsklasse: ISO 4406: 18/16/13 (Standard) bis 16/14/11 (Servosysteme). Regelmäßiger Filterwechsel und Ölanalyse sind essentiell.
**Confidence**: benchmark

### HY-021: Darf ich Teflonband auf JIC-37°-Fittings verwenden?
**Antwort**: **NEIN!** JIC-37°-Fittings dichten metalisch an der Konusfläche. Teflonband kann Partikel ins System einbringen und die Konusdichtung beeinträchtigen. Teflonband nur bei konischen Rohrgewinden (NPT, BSPT) verwenden.
**Confidence**: measured

### HY-022: Was tun bei Hydraulik-Leckage auf See?
**Antwort**: 1) Ruhe bewahren. 2) Notsteuerung aktivieren (falls Ruderhydraulik betroffen). 3) Leckstelle identifizieren und wenn möglich abdichten (Lappen + Kabelbinder als Notbehelf). 4) Fluidverlust minimieren. 5) Nächsten Hafen anlaufen. NICHT mit bloßer Hand nach Lecks tasten!
**Confidence**: benchmark

### HY-023: Brauche ich einen Druckspeicher (Akkumulator)?
**Antwort**: Bei Power-Steering-Systemen empfohlen — dämpft Druckspitzen und ermöglicht Notlenkvorgänge bei Pumpenausfall. Auf Yachten >20 m mit elektrohydraulischer Steuerung Standard. Blase alle 2 Jahre prüfen lassen.
**Confidence**: benchmark

### HY-024: Wie oft sollte ein Ölwechsel im Hydrauliksystem erfolgen?
**Antwort**: Alle 2 Jahre oder 1.000 Betriebsstunden, je nachdem was zuerst eintritt. Bei Ölanalyse mit schlechten Werten (Wassergehalt >0.1%, Säurezahl >2.0 mgKOH/g): sofort wechseln. Filter bei jedem Ölwechsel erneuern.
**Confidence**: benchmark

### HY-025: Kann ich Hydraulikschläuche verschiedener Hersteller mischen?
**Antwort**: Ja, sofern SAE-Typ, Druckklasse und Fitting-Standard übereinstimmen. Ein Parker-Schlauch mit Gates-Fitting ist technisch zulässig, wenn die Crimp-Spezifikationen beider Hersteller eingehalten werden. Im Zweifelsfall: gleiches System bevorzugen.
**Confidence**: benchmark

---

## Glossar (40+ Begriffe)

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **1SN / 2SN** | Europäische Bezeichnung (DIN EN 853) für 1- bzw. 2-lagige Drahtgeflechtschläuche, entspricht SAE 100R1/R2 |
| 2 | **4SP / 4SH** | Europäische Bezeichnung (DIN EN 856) für 4-Spirallagen-Schläuche, entspricht SAE 100R12/R13 |
| 3 | **ABYC** | American Boat & Yacht Council — US-Normenorganisation für Bootsbau |
| 4 | **Akkumulator** | Druckspeicher (Membran- oder Blasenspeicher) — puffert Druckspitzen und ermöglicht Notbetrieb |
| 5 | **Arbeitsdruck** | Maximaler Dauerbetriebsdruck eines Schlauchs (Working Pressure, WP) |
| 6 | **ATF** | Automatic Transmission Fluid — niedrigviskoses Hydraulikfluid, verwendet in SeaStar/BayStar-Systemen |
| 7 | **Außendecke** | Äußere Schutzschicht des Schlauchs (Cover) — schützt vor UV, Abrasion, Chemikalien |
| 8 | **Biegeradius** | Minimaler Biegeradius — kleinster erlaubter Krümmungsradius des Schlauchs unter Druck |
| 9 | **Berstdruck** | Druck, bei dem der Schlauch versagt (Burst Pressure) — typisch 4× Arbeitsdruck |
| 10 | **BSP** | British Standard Pipe — Gewindenorm mit parallelem (BSPP/G) und konischem (BSPT/R) Gewinde |
| 11 | **Crimpung** | Maschinelles Verpressen einer Hülse auf Schlauch und Fitting — permanente Verbindung |
| 12 | **CE-Kat.** | CE-Entwurfskategorie (A–D) gemäß Recreational Craft Directive 2013/53/EU |
| 13 | **CPE** | Chloriertes Polyethylen — modernes Innenrohr-/Außendeckenmaterial, öl- und ozonresistent |
| 14 | **CR** | Chloropren-Kautschuk (Neoprene) — Standard-Außendeckenmaterial |
| 15 | **Dash-Size** | Nenn-Innendurchmesser in 1/16-Zoll-Schritten (-4 = 1/4", -8 = 1/2" usw.) |
| 16 | **DN** | Nennweite (Diameter Nominal) — Innendurchmesser des Schlauchs in mm |
| 17 | **DNV-GL** | Det Norske Veritas — Germanischer Lloyd — Klassifikationsgesellschaft |
| 18 | **Drahtgeflecht** | Wire Braid — Verstärkungslage aus geflochtenen Stahldrähten |
| 19 | **EPDM** | Ethylen-Propylen-Dien-Kautschuk — UV-/ozonresistent, NICHT ölresistent |
| 20 | **FKM / Viton** | Fluorkautschuk — Hochtemperatur-Dichtungsmaterial, chemisch beständig |
| 21 | **Fitting** | Anschlussarmatur am Schlauchende (Verschraubung, Flansch, Schnellkupplung) |
| 22 | **Flat-Face** | Schnellkupplung mit planer Dichtfläche — tropffreies Trennen |
| 23 | **HLP** | Hydrauliköl mit Verschleißschutz-Additiven nach DIN 51524-2 |
| 24 | **HVLP** | Hydrauliköl mit hohem Viskositätsindex nach DIN 51524-3 |
| 25 | **Impulsfestigkeit** | Anzahl der Druckzyklen bis zum Versagen (Impulse fatigue life) |
| 26 | **Injektionsverletzung** | Eindringen von Hydraulikfluid unter die Haut durch Hochdruck-Ölstrahl — chirurgischer Notfall! |
| 27 | **Innenrohr** | Innere Schicht des Schlauchs (Inner Tube) — medienberührend |
| 28 | **ISO VG** | ISO Viskositätsgrade (VG 10, 15, 22, 32, 46, 68) — Einteilung der Ölviskosität |
| 29 | **JIC** | Joint Industry Council — 37°-Konus-Fitting nach SAE J514 |
| 30 | **Kavitation** | Dampfblasenbildung bei Unterdruck in Saugseite — zerstörerisch für Pumpe und Schläuche |
| 31 | **Layline** | Markierungslinie auf der Schlauchdecke zur Erkennung von Torsion |
| 32 | **LHM** | Liquide Hydraulique Minérale — Spezialfluid für Citroen-Typ-Systeme (Lecomble & Schmitt) |
| 33 | **NBR** | Nitril-Butadien-Kautschuk — Standard-Innenrohrmaterial, ölresistent |
| 34 | **Notsteuerung** | Backup-Steuerungssystem bei Ausfall der Haupthydraulik (Notpinne, Notsystem) |
| 35 | **ORFS** | O-Ring Face Seal — leckagefreie Verschraubung nach SAE J1453 |
| 36 | **Power Assist** | Elektrohydraulische Unterstützungspumpe für die Rudersteuerung |
| 37 | **PTFE** | Polytetrafluorethylen (Teflon) — chemisch inertes Innenrohr, hohe Temperaturbeständigkeit |
| 38 | **SAE** | Society of Automotive Engineers — US-Normungsorganisation |
| 39 | **Schneidring** | Cutting Ring — Metallring bei metrischen Verschraubungen, greift in Rohr/Fitting |
| 40 | **Spiralverstärkung** | Wire Spiral — Verstärkungslage aus spiralförmig gewickelten Stahldrähten |
| 41 | **Steuerzylinder** | Hydraulikzylinder, der die Ruderbewegung ausführt |
| 42 | **Steuerpumpe** | Handpumpe am Steuerrad, die Hydraulikdruck erzeugt |
| 43 | **Torsion** | Verdrehung des Schlauchs um seine Längsachse — lebensdauermindernd |
| 44 | **Volumenzunahme** | Volumetrische Ausdehnung des Schlauchs unter Druck (Sponge-Effekt) |
| 45 | **Zero-Speed** | Stabilisator-Betriebsmodus im Hafen/bei Stillstand (nur aktive Systeme) |

---

## Schnell-Referenz

### Schlauchauswahl in 5 Schritten

```
1. ANWENDUNG bestimmen → Ruder / Stabilisator / Winsch / Thruster
2. DRUCK ermitteln → Herstellerangabe, Typenschild Power Pack
3. DURCHMESSER berechnen → Q (l/min) und v (m/s) → DN
4. SAE-TYP wählen → R1/R2/R7/R12 basierend auf Druck
5. FITTINGS bestimmen → JIC/BSP/Metrisch → Dash-Size/Gewinde
```

### Checkliste Jährliche Inspektion

```
□ Sichtprüfung aller Schläuche (Risse, Beulen, Scheuerstellen)
□ Fittings auf Korrosion und Leckage prüfen
□ Fluidstand und -zustand prüfen (Farbe, Geruch)
□ Schlauch-Alter prüfen (Installationsdatum)
□ Biegeradien kontrollieren (keine Knicke)
□ Befestigungen prüfen (Schellen, Klemmen)
□ Thermische Abstände prüfen (>50 mm zu heißen Teilen)
□ Steuerung auf Funktion testen (Anschlag zu Anschlag)
□ Entlüftungsschrauben prüfen
□ Ölfilter-Zustand prüfen
□ Notsteuerung testen
□ Befunde dokumentieren (Fotos, Protokoll)
```

### Notfall-Kit an Bord (Empfehlung)

| Artikel | Menge | Bemerkung |
|---------|-------|-----------|
| Ersatzschlauch (passend für Steuerung) | 1× | Vorkonfektioniert, Fittings montiert |
| Reusable-Fittings (passende Größe) | 4× | Für Notreparatur |
| Hydraulikfluid (Systemtyp!) | 2 l | In verschlossenem Behälter |
| Gabelschlüssel-Set (zöllig + metrisch) | 1× | Passend für alle Fittings |
| Teflonband | 1 Rolle | NUR für konische Gewinde! |
| Lappen, Ölbindemittel | 5× | Für Ölaufnahme |
| Kabelbinder, Schlauchschellen | 10× | Befestigung und Notabdichtung |

---

## Notfall-Ressourcen

### Injektionsverletzung durch Hydrauliköl

**LEBENSBEDROHLICHER NOTFALL!**

1. **Sofort** ärztliche Hilfe rufen (Seenotruf VHF Kanal 16 / 112)
2. **NICHT** abwarten — Injektionsverletzungen verschlimmern sich rapide
3. Wunde NICHT auswaschen oder Druck ausüben
4. **Chirurgische Behandlung** innerhalb 6 Stunden erforderlich
5. Information an Arzt: "Injection injury with hydraulic oil at [pressure] bar"
6. Öltyp/Sicherheitsdatenblatt bereithalten

### Totalausfall Ruderhydraulik auf See

1. **Notsteuerung** aktivieren (Notpinne / Notruder)
2. Geschwindigkeit reduzieren
3. Crew informieren
4. Position markieren, Seenotzentrale informieren (falls nötig)
5. Nächsten Hafen anlaufen (unter Notsteuerung)
6. NICHT versuchen, unter Druck an Hydraulikleitungen zu arbeiten

### Wichtige Notrufnummern

| Dienst | Nummer | Bereich |
|--------|--------|---------|
| Seenotrettung DE (DGzRS) | VHF Kanal 70 (DSC) / 16 (Sprache) | Deutsche Küste |
| MRCC Bremen | +49 421 536870 | Deutsche Nordsee |
| CROSS (Frankreich) | VHF 16 / +33 1 7310 7010 | Französische Küste |
| Guardia Costiera (IT) | VHF 16 / +39 06 5922 7000 | Italienische Küste |
| MRCC Piraeus (GR) | VHF 16 / +30 210 4112500 | Griechische Gewässer |
| US Coast Guard | VHF 16 / 911 | US-Gewässer |

---

## ANHANG A — Cross-Reference: Schlauch-Hersteller-Teilenummern

### SAE 100R2 (2SN), DN 12 (1/2")

| Hersteller | Teilenummer | Arbeitsdruck | Berstdruck | Biegeradius | Preis/m |
|-----------|------------|-------------|------------|-------------|---------|
| Parker | 482-8 (GlobalCore) | 275 bar | 1100 bar | 180 mm | 28 EUR |
| Parker | No-Skive 72-8 | 275 bar | 1100 bar | 180 mm | 30 EUR |
| Gates | MXT-8 | 275 bar | 1100 bar | 180 mm | 26 EUR |
| Gates | MegaSys 4220-8 | 275 bar | 1100 bar | 180 mm | 27 EUR |
| Eaton | GH793-8 | 275 bar | 1100 bar | 180 mm | 29 EUR |
| Continental | Flexon 2SN-12 | 275 bar | 1100 bar | 180 mm | 25 EUR |
| Manuli | Rockmaster 2SN-12 | 275 bar | 1100 bar | 180 mm | 24 EUR |

### SAE 100R7, DN 6 (1/4") — Marine-Steuerung

| Hersteller | Teilenummer | Arbeitsdruck | Berstdruck | Biegeradius | Preis/m |
|-----------|------------|-------------|------------|-------------|---------|
| Parker | Parflex 540N-4 | 207 bar | 827 bar | 40 mm | 14 EUR |
| Gates | Polyflex 2750N-04 | 207 bar | 827 bar | 38 mm | 13 EUR |
| Eaton | Synflex 34CT-04 | 207 bar | 827 bar | 40 mm | 15 EUR |
| SeaStar | HA5420 (Bulk) | 172 bar | 690 bar | 45 mm | 12 EUR |

---

## ANHANG B — SAE-Vergleichstabelle (SAE ↔ DIN EN ↔ ISO)

| SAE J517 | DIN EN | ISO | Lagen | Typ | Druckbereich |
|----------|--------|-----|-------|-----|-------------|
| 100R1AT | EN 853 1SN | ISO 1436 Type 1 | 1 Drahtgeflecht | Standard | 40–250 bar |
| 100R2AT | EN 853 2SN | ISO 1436 Type 2 | 2 Drahtgeflecht | Standard | 80–400 bar |
| 100R3 | EN 854 2TE | — | 2 Textilgeflecht | Niederdruck | 10–63 bar |
| 100R4 | — | — | Drahtwendel + Textil | Saug | 7–35 bar (Vakuum) |
| 100R5 | — | — | 1 Draht + 1 Textil | Textildecke | 35–175 bar |
| 100R6 | EN 854 1TE | — | 1 Textilgeflecht | Niederdruck | 7–35 bar |
| 100R7 | — | — | 1 Draht, Thermoplast | Kompakt | 70–350 bar |
| 100R8 | — | — | 2 Draht, Thermoplast | Kompakt HD | 140–700 bar |
| 100R12 | EN 856 4SP | ISO 3862 Type 1 | 4 Spirallagen | Hochdruck | 210–420 bar |
| 100R13 | EN 856 4SH/6SH | ISO 3862 Type 2 | 4/6 Spirallagen | Höchstdruck | 350–700 bar |
| 100R14 | — | — | PTFE + SS-Geflecht | Chemisch | 100–280 bar |
| 100R15 | — | — | 4/6 Spiral, Kompakt | Kompakt HD | 280–420 bar |
| 100R16 | EN 857 1SC | — | 1 Draht, Kompakt | Kompakt | 100–350 bar |
| 100R17 | EN 857 2SC | — | 2 Draht, Kompakt | Kompakt HD | 160–450 bar |

---

## ANHANG C — Biegeradien-Tabelle (alle SAE-Typen, alle DN)

### Mindestbiegeradien in mm

| DN (mm) | R1/1SN | R2/2SN | R7 | R12/4SP | R13/4SH | R14 | R16/1SC | R17/2SC |
|---------|--------|--------|-----|---------|---------|------|---------|---------|
| 5 | 65 | 75 | 30 | — | — | 25 | 50 | 60 |
| 6 | 75 | 100 | 40 | — | — | 30 | 55 | 70 |
| 8 | 90 | 115 | 55 | — | — | 40 | 65 | 90 |
| 10 | 105 | 130 | 65 | — | — | 50 | 80 | 100 |
| 12 | 125 | 180 | 75 | 180 | 200 | 65 | 100 | 125 |
| 16 | 150 | 200 | 90 | 200 | 240 | 80 | 130 | 160 |
| 19 | 180 | 240 | — | 240 | 280 | 100 | 160 | 200 |
| 25 | 240 | 300 | — | 340 | 380 | 140 | 200 | 260 |
| 32 | 300 | 420 | — | 420 | 480 | — | — | — |
| 38 | 360 | 500 | — | 500 | 560 | — | — | — |
| 51 | 460 | 630 | — | 630 | 710 | — | — | — |

---

## ANHANG D — Confidence-Mapping für AYDI-Analysemodule

### Visuell erkennbare Merkmale (Pipeline B)

| Merkmal | Confidence | Score-Einfluss | Bemerkung |
|---------|-----------|---------------|-----------|
| Außendeckenrisse | visual_high | -20 bis -40 | Eindeutig erkennbar |
| Schlauchbeule | visual_high | -60 bis -80 | Kritisch, sofort handeln |
| Fitting-Korrosion | visual_high | -15 bis -35 | Rost/Salz gut erkennbar |
| Scheuerstelle | visual_high | -10 bis -30 | Bei tiefem Abrieb |
| Ölfilm/Leckage | visual_high | -20 bis -50 | An Fittings gut sichtbar |
| Knick/Abflachung | visual_high | -15 bis -35 | Geometrie erkennbar |
| Verdrehung (Layline) | visual_medium | -10 bis -25 | Layline nicht immer sichtbar |
| Thermische Schädigung | visual_high | -25 bis -45 | Verfärbung eindeutig |
| Schlauch-Alter | visual_low | -5 bis -30 | Datum nur bei lesbarem Aufdruck |
| Fluid-Zustand | visual_medium | -10 bis -25 | Farbbeurteilung subjektiv |
| Schlauchtyp (SAE) | visual_medium | ±0 | Aufdruck muss lesbar sein |
| Biegeradius-Einhaltung | visual_medium | -10 bis -20 | Schätzung ohne Messung |

### Daten-basierte Merkmale (Pipeline A)

| Merkmal | Confidence | Score-Einfluss | Quelle |
|---------|-----------|---------------|--------|
| Schlauch-Spezifikation | measured | Basis | CAD/Datenblatt |
| Alter (bekannt) | measured | -5/Jahr | Installationsdatum |
| Druck-/Temperaturbereich | measured | ±0 bis -30 | Auslegungsdaten |
| Normkonformität | calculated | ±0 bis -40 | Spezifikationsvergleich |
| Lebensdauerberechnung | calculated | variabel | Berechnungsmodell |
| Kostenermittlung | estimated | — | Parametrisches Modell |

---

## ANHANG E — Bordausstattung und Ersatzteile

### Empfohlene Bordausrüstung nach Bootsklasse

#### Tagesboot / Coastal Cruiser (6–10 m)

| Artikel | Anzahl | Kosten (EUR) |
|---------|--------|-------------|
| Ersatzschlauch Steuerung (R7, DN 6, vorkonfektioniert) | 1× | 45–80 |
| SeaStar/BayStar Hydraulikfluid | 1 l | 15–25 |
| Gabelschlüssel 7/16" + 9/16" | je 1× | 15–25 |
| Lappen, Kabelbinder | Set | 10 |
| **Gesamt** | | **85–140** |

#### Küstenkreuzer / Blue Water (10–16 m)

| Artikel | Anzahl | Kosten (EUR) |
|---------|--------|-------------|
| Ersatzschlauch Steuerung (DN 6/8, vorkonfektioniert) | 2× | 90–180 |
| Reusable-Fittings (passend) | 4× | 60–120 |
| Hydraulikfluid (Systemtyp) | 2 l | 30–60 |
| Schlüsselsatz (zöllig + metrisch) | 1× | 30–50 |
| Teflonband + Dichtmittel | Set | 15 |
| Schlauchschellen + Spiralschutz | 5× | 20–30 |
| **Gesamt** | | **245–455** |

#### Offshore Cruiser / Yacht (16–25 m)

| Artikel | Anzahl | Kosten (EUR) |
|---------|--------|-------------|
| Ersatzschläuche (Steuerung + Autopilot) | 3–4× | 200–500 |
| Reusable-Fittings (diverse Größen) | 8× | 120–250 |
| Hydraulikfluid (5 l) | 1× | 50–150 |
| Crimpzange oder portable Crimpmaschine | 1× | 250–800 |
| O-Ring-Sortiment (NBR/FKM) | 1× | 30–50 |
| Druckmessgerät (0–250 bar) | 1× | 80–150 |
| Schlüsselsatz komplett | 1× | 50–80 |
| **Gesamt** | | **780–1.980** |

#### Superyacht (25–60 m)

| Artikel | Anzahl | Kosten (EUR) |
|---------|--------|-------------|
| Schlauchsortiment (alle Systeme) | 10–20× | 1.500–5.000 |
| Portable Crimpmaschine (Parker/Gates) | 1× | 7.000–9.000 |
| Crimp-Dornensatz | 1× | 2.000–4.000 |
| Hydraulikfluid (20 l) | 1× | 200–600 |
| O-Ring-Sortiment XL | 1× | 80–150 |
| Druckmessgerät-Set | 1× | 200–400 |
| Ölanalyse-Kit | 1× | 150–300 |
| Werkzeugsatz Hydraulik komplett | 1× | 300–600 |
| **Gesamt** | | **11.430–20.050** |

---

## ANHANG F — Fallstudien

### Fallstudie 1: Steuerungsausfall auf Blauwasser-Segelyacht (45 ft, Baujahr 2014)
- **Yacht**: Bavaria 45 Cruiser, hydraulische Steuerung (Lecomble & Schmitt HB 4310)
- **Problem**: Totalausfall der Steuerung bei Starkwind im Golf von Biskaya
- **Ursache**: Innenrohr-Kollaps eines 8 Jahre alten Schlauch (SAE R1, DN 6)
- **Folgen**: 4 Stunden Notsteuerung mit Notpinne, Einlaufen in La Coruña
- **Befund**: Schlauch visuell unauffällig, Innenrohr hatte sich gelöst und blockierte Durchfluss
- **Kosten**: 380 EUR (2 neue Schläuche R2 + Arbeit) + 1.200 EUR (Hafengebühren, Verzögerung)
- **Lektion**: **Schlauchtyp-Upgrade auf R2, Alter max. 6 Jahre, regelmäßige Funktionsprüfung**
- **AYDI-Score**: Vorher: 45 (estimated, Alter bekannt), Nachher: 92 (measured, neu)

### Fallstudie 2: Stabilisator-Leckage auf Motoryacht (62 ft, Baujahr 2019)
- **Yacht**: Princess 62, Naiad S1000 Stabilisatoren
- **Problem**: Progressiver Ölverlust, ca. 0.5 l/Woche, Stabilisator-Wirkung nachlassend
- **Ursache**: Fitting-Korrosion an verzinktem Stahlverbindung (Salzwasser-Exposition)
- **Befund**: 2 von 10 Fittings mit sichtbarer Korrosion und Mikroleckage
- **Maßnahme**: Alle 10 Fittings auf Edelstahl 316L aufgerüstet, Schläuche beibehalten (3 Jahre alt)
- **Kosten**: 680 EUR (Fittings + Arbeit) + 120 EUR (Öl + Spülung)
- **Lektion**: **Bei Salzwasser-Yachten von Anfang an 316L-Fittings spezifizieren**
- **AYDI-Score**: 35 (visual_high, Korrosion) → 88 (measured, nach Austausch)

### Fallstudie 3: Hydraulische Winsch-Probleme auf Regattayacht (52 ft, Baujahr 2021)
- **Yacht**: Grand Soleil 52 LC, Harken UniPower Winschen
- **Problem**: Winschen reagieren langsam, ungleichmäßige Geschwindigkeit
- **Ursache**: Zu kleiner Schlauchdurchmesser (DN 8 statt DN 12) — Werftfehler
- **Befund**: Druckverlust >15 bar über 12 m Schlauchlänge, Fluid überhitzt
- **Maßnahme**: Alle Versorgungsschläuche auf DN 12 aufgerüstet (SAE R2)
- **Kosten**: 1.850 EUR (6 Schläuche + Fittings + Arbeit + Decksdurchführungen)
- **Lektion**: **Schlauchdimensionierung immer berechnen, nicht von Vorgänger übernehmen**
- **AYDI-Score**: 42 (calculated, Druckverlust) → 90 (measured, nach Upgrade)

### Fallstudie 4: UV-Schaden an Deck-Hydraulik (Katamaran, 42 ft, Baujahr 2016)
- **Yacht**: Lagoon 42, hydraulisches Ankerspill + Davit
- **Problem**: Rissige Schläuche auf dem Vorschiff, sichtbare Drahtgeflechtlage
- **Ursache**: CR-Außendecke ohne UV-Schutz, 6 Jahre Mittelmeer-Exposition
- **Befund**: 3 von 4 Schläuchen mit Außendeckenrissen, 1 Schlauch mit Drahtrostung
- **Maßnahme**: Alle 4 Schläuche ersetzt (EPDM-Außendecke), Spiralschutz installiert
- **Kosten**: 520 EUR (Material + Arbeit) + 45 EUR (Spiralschutz)
- **Lektion**: **An Deck immer EPDM-Außendecke oder Spiralschutz verwenden**
- **AYDI-Score**: 28 (visual_high) → 95 (measured, EPDM + Schutz)

### Fallstudie 5: Bugstrahlruder-Totalausfall auf Charteryacht (37 ft, Baujahr 2012)
- **Yacht**: Jeanneau Sun Odyssey 379, Vetus BOW PRO
- **Problem**: Bugstrahlruder ohne Funktion beim Anlegemanöver in engen Hafen
- **Ursache**: Geplatzter Saugschlauch (SAE R4, 10 Jahre alt, Gummiverhärtung)
- **Befund**: Saugschlauch hatte Riss, System saugte Luft, Pumpe kavitierte
- **Maßnahme**: Saugschlauch erneuert, Filter gereinigt, Ölwechsel
- **Kosten**: 280 EUR (Schlauch + Arbeit + Öl)
- **Lektion**: **Saugschläuche sind kritisch — auch bei Niederdrucksystemen auf Alter achten**
- **AYDI-Score**: 18 (documented, Totalausfall) → 85 (measured, nach Reparatur)

### Fallstudie 6: Autopilot-Leckage auf Langfahrtyacht (48 ft, Baujahr 2017)
- **Yacht**: Hallberg-Rassy 48 MK II, Raymarine Type 2 Autopilot
- **Problem**: Autopilot verliert nach 2–3 Stunden die Steuerung, schwammiges Lenken
- **Ursache**: Mikroleckage an Reusable-Fitting (vom Vorbesitzer installiert)
- **Befund**: Reusable-Fitting hatte sich durch Vibration gelockert, O-Ring verhärtet
- **Maßnahme**: Reusable-Fittings durch Crimp-Fittings ersetzt, Schläuche beibehalten (4 J.)
- **Kosten**: 220 EUR (Fittings + Crimpen + Öl)
- **Lektion**: **Reusable-Fittings regelmäßig nachziehen oder auf Crimp umsteigen**
- **AYDI-Score**: 40 (documented) → 82 (measured, Crimp)

### Fallstudie 7: Hydraulik-Brand auf Motoryacht (55 ft, Baujahr 2008)
- **Yacht**: Fairline Squadron 55, hydraulische Passerelle + Davit
- **Problem**: Hydrauliköl-Brand im Maschinenraum
- **Ursache**: Schlauch an Auspuffrohr gescheuert (Befestigung gelöst), Ölstrahl auf heißen Turbo
- **Folgen**: Feuerlöschanlage ausgelöst, Motor abgestellt, keine Personenschäden
- **Befund**: Schlauchbefestigung korrodiert und gebrochen, 15 Jahre alter Schlauch
- **Maßnahme**: Kompletterneuerung Maschinenraum-Hydraulik, Feuerschutz-Schläuche
- **Kosten**: 8.500 EUR (Schläuche + Fittings + Verlegung) + 12.000 EUR (Brandschäden)
- **Lektion**: **Maschinenraum-Schläuche: Feuerschutz, sichere Befestigung, max. 6 Jahre**
- **AYDI-Score**: 0 (documented, Brandfall) → 95 (measured, Kompletterneuerung)

### Fallstudie 8: Trimmklappen-Vibration auf Sportboot (28 ft, Baujahr 2020)
- **Yacht**: Bayliner 285, Bennett Trimmklappen
- **Problem**: Trimmklappen vibrieren und flattern bei hoher Geschwindigkeit
- **Ursache**: Zu lange, ungeführte Hydraulikschläuche (SAE R1) schwingen in Resonanz
- **Befund**: Schläuche ohne Befestigung über 1.5 m Länge, Eigenfrequenz = Motordrehzahl
- **Maßnahme**: Schlauchführung mit Gummipuffer-Schellen alle 300 mm, kürzere Schläuche
- **Kosten**: 180 EUR (Schellen + Neuverlegung)
- **Lektion**: **Schlauchbefestigung alle 300–500 mm, besonders bei Hochgeschwindigkeitsbooten**
- **AYDI-Score**: 48 (visual_medium) → 88 (measured, korrekte Verlegung)

---

## ANHANG G — Experten und Ansprechpartner

### Schulungen und Zertifizierungen

| Anbieter | Kurs | Dauer | Kosten | Ort |
|----------|------|-------|--------|-----|
| Parker Hannifin | Hydraulic Hose Assembly Certification | 2 Tage | 650 EUR | Bielefeld / online |
| Gates | MegaCrimp Certification | 1 Tag | 450 EUR | Aachen / mobil |
| Hansa-Flex | Hydraulik-Grundlagen Marine | 3 Tage | 890 EUR | Bremen |
| Bosch Rexroth | Hydraulik-Instandhaltung | 5 Tage | 2.200 EUR | Lohr am Main |
| VDMA Hydraulik-Akademie | Marine-Hydraulik | 2 Tage | 780 EUR | Frankfurt |

### Fachverbände

| Verband | Fokus | Website |
|---------|-------|---------|
| VDMA Fluidtechnik | Deutsche Hydraulik-Industrie | vdma.org |
| BVHI | Bundesverband der Hydraulik-Industrie | — |
| NFPA (USA) | National Fluid Power Association | nfpa.com |
| CETOP (EU) | European Fluid Power Committee | cetop.org |
| ICOMIA | International Council of Marine Industry Associations | icomia.org |

---

## ANHANG H — Risk Matrix: Hydraulikschlauch-Versagen

### Risikobewertung nach Anwendung und Versagensart

| Anwendung | Versagensart | Wahrscheinlichkeit | Auswirkung | Risiko-Score | Maßnahme |
|-----------|-------------|-------------------|-----------|-------------|----------|
| Ruderanlage | Totalausfall (Bersten) | Niedrig | Katastrophal | **HOCH** | Redundanz, 6-Jahres-Limit |
| Ruderanlage | Leckage (progressiv) | Mittel | Schwer | **HOCH** | Jährliche Inspektion |
| Ruderanlage | Schwammige Steuerung | Hoch | Mittel | **MITTEL** | Entlüftung, Wartung |
| Stabilisator | Bersten | Niedrig | Mittel | **MITTEL** | Inspektion, Impulsfestigkeit |
| Stabilisator | Leckage | Mittel | Gering | **NIEDRIG** | Regelmäßige Prüfung |
| Winsch | Bersten | Niedrig | Mittel | **MITTEL** | Überdruckventil |
| Winsch | Leckage | Mittel | Gering | **NIEDRIG** | Sichtprüfung |
| Thruster | Bersten | Niedrig | Gering | **NIEDRIG** | Standard-Wartung |
| Thruster | Totalausfall | Mittel | Mittel | **MITTEL** | Ersatzteile vorhalten |
| Trimmklappen | Bersten | Sehr niedrig | Gering | **SEHR NIEDRIG** | Standard-Wartung |
| Davit/Kran | Bersten | Niedrig | Schwer | **MITTEL** | Lastprüfung, Inspektion |
| Passerelle | Bersten | Niedrig | Mittel | **MITTEL** | Jährliche Prüfung |

---

## ANHANG I — Audit-/Compliance-Checkliste

### Pre-Purchase Survey: Hydrauliksystem-Prüfung

```
AYDI HYDRAULIK-AUDIT | Yacht: __________ | Datum: __________

1. DOKUMENTATION
   □ Herstellerangaben aller Hydraulikschläuche vorhanden
   □ Installationsdaten dokumentiert
   □ Letzte Wartung/Inspektion dokumentiert
   □ Hydraulikfluid-Typ dokumentiert
   □ Originalschaltplan vorhanden

2. STEUERUNG
   □ Schlauchtyp identifiziert: _____ (SAE-Typ)
   □ Schlauchalter: _____ Jahre
   □ Sichtprüfung Schläuche: □ OK □ Mängel: __________
   □ Sichtprüfung Fittings: □ OK □ Mängel: __________
   □ Leckagetest: □ OK □ Mängel: __________
   □ Funktionstest (Anschlag ↔ Anschlag): □ OK □ Mängel
   □ Notsteuerung vorhanden und getestet: □ Ja □ Nein

3. STABILISATOREN (falls vorhanden)
   □ System: __________ (Hersteller/Modell)
   □ Schlauchzustand: □ OK □ Mängel: __________
   □ Fitting-Zustand: □ OK □ Mängel: __________
   □ Ölstand: □ OK □ Niedrig
   □ Ölzustand (Farbe/Geruch): □ OK □ Auffällig

4. WINSCHEN (falls hydraulisch)
   □ System: __________ (Hersteller/Modell)
   □ Schlauchzustand: □ OK □ Mängel: __________
   □ Decksdurchführungen dicht: □ Ja □ Nein
   □ Funktionstest: □ OK □ Mängel

5. BUGSTRAHLRUDER (falls hydraulisch)
   □ System: __________ (Hersteller/Modell)
   □ Schlauchzustand: □ OK □ Mängel: __________
   □ Saugschlauch-Zustand: □ OK □ Mängel
   □ Funktionstest: □ OK □ Mängel

6. ALLGEMEIN
   □ Alle Schläuche korrekt befestigt (Schellen alle 300–500 mm)
   □ Mindestbiegeradien eingehalten
   □ Abstände zu heißen Oberflächen ≥50 mm
   □ Scheuerschutz an Kontaktstellen
   □ UV-Schutz für Deck-verlegte Schläuche
   □ Hydraulikfluid-Typ einheitlich im System
   □ Filter sauber/gewechselt

GESAMTBEWERTUNG: □ Gut □ Akzeptabel □ Mängel □ Kritisch
EMPFEHLUNG: ____________________________________________

Prüfer: __________________  Unterschrift: __________________
```

---

## ANHANG J — Material-Datenblätter (Kurzübersicht)

### NBR (Nitril-Butadien-Kautschuk) — Innenrohr

| Eigenschaft | Wert | Einheit |
|------------|------|---------|
| Shore-Härte | 60–80 | Shore A |
| Zugfestigkeit | 10–25 | MPa |
| Bruchdehnung | 200–600 | % |
| Temperaturbereich | -40 bis +100 | °C |
| Ölbeständigkeit | Ausgezeichnet | — |
| Ozonbeständigkeit | Schlecht | — |
| UV-Beständigkeit | Schlecht | — |
| Wasserbeständigkeit | Gut | — |

### CR (Chloropren, Neoprene) — Außendecke

| Eigenschaft | Wert | Einheit |
|------------|------|---------|
| Shore-Härte | 40–90 | Shore A |
| Zugfestigkeit | 7–25 | MPa |
| Bruchdehnung | 100–600 | % |
| Temperaturbereich | -35 bis +100 | °C |
| Ölbeständigkeit | Mäßig bis gut | — |
| Ozonbeständigkeit | Gut | — |
| UV-Beständigkeit | Mäßig | — |
| Abriebfestigkeit | Gut | — |

### EPDM (Ethylen-Propylen-Dien) — Außendecke

| Eigenschaft | Wert | Einheit |
|------------|------|---------|
| Shore-Härte | 30–90 | Shore A |
| Zugfestigkeit | 7–20 | MPa |
| Bruchdehnung | 100–500 | % |
| Temperaturbereich | -50 bis +150 | °C |
| Ölbeständigkeit | **Schlecht** | — |
| Ozonbeständigkeit | Ausgezeichnet | — |
| UV-Beständigkeit | Ausgezeichnet | — |
| Abriebfestigkeit | Mäßig | — |

### PTFE (Polytetrafluorethylen) — Innenrohr

| Eigenschaft | Wert | Einheit |
|------------|------|---------|
| Shore-Härte | 50–65 | Shore D |
| Zugfestigkeit | 20–35 | MPa |
| Bruchdehnung | 200–400 | % |
| Temperaturbereich | -73 bis +260 | °C |
| Ölbeständigkeit | Ausgezeichnet | — |
| Chemische Beständigkeit | Universell | — |
| Reibungskoeffizient | 0.04 (niedrigster aller Kunststoffe) | — |
| Preis-Faktor vs. NBR | 4–6× | — |

---

## ANHANG K — Prüfverfahren

### Druckprüfung (Abdrückprüfung)

**Ziel**: Nachweis der Dichtheit und Festigkeit einer Schlauchleitung nach Montage.

**Durchführung:**
1. Alle Fittings handfest + Drehmoment angezogen
2. System mit Hydraulikfluid (NICHT Luft!) füllen und entlüften
3. Druck langsam aufbauen auf 1.5× Arbeitsdruck (Prüfdruck)
4. Prüfdruck 5 Minuten halten
5. Druckabfall messen: max. 5% Abfall zulässig
6. Alle Fittings visuell auf Leckage prüfen
7. Prüfung dokumentieren (Datum, Druck, Ergebnis)

**Beispiel**: Arbeitsdruck 200 bar → Prüfdruck 300 bar → 5 min halten → OK wenn ≤285 bar nach 5 min

### Impulsprüfung (nach ISO 6803)

**Ziel**: Nachweis der Ermüdungsfestigkeit unter zyklischer Druckbelastung.

**Parameter:**
- Druckschwankung: 0 → 133% des Arbeitdrucks
- Frequenz: 0.5–1.25 Hz
- Temperatur: Obere Betriebstemperatur
- Mindest-Zyklen: 200.000 (R1/R2), 500.000 (R12)

### Berstprüfung

**Ziel**: Ermittlung der tatsächlichen Berstfestigkeit.

**Durchführung:**
- Druck gleichmäßig steigern: max. 50 bar/s
- Bis zum Bersten des Schlauchs
- Berstdruck muss ≥ Nenn-Berstdruck sein
- **Nur als Werksprüfung — nie an Bord durchführen!**

### Sichtprüfung (nach ABYC H-32)

**Checkliste visuelle Inspektion:**
1. Außendecke: Risse, Verhärtung, UV-Schäden, Verfärbung
2. Beulen: Lokale Aufblähungen (Drahtbruch)
3. Fittings: Korrosion, Ölfilm, Salzablagerung
4. Verlegung: Biegeradien, Knicke, Scheuerstellen
5. Befestigung: Schellen vorhanden und fest
6. Thermisch: Abstand zu heißen Teilen
7. Alter: Produktionsdatum und Installationsdatum

---

## ANHANG L — Top 15 Fehler bei Hydraulikschlauch-Installation

| Nr. | Fehler | Folge | Vermeidung |
|-----|--------|-------|------------|
| 1 | Schlauch unter Mindestbiegeradius verlegt | Früher Bruch, Knick | Biegeradius-Tabelle beachten |
| 2 | Schlauch verdreht montiert (Torsion) | 70% reduzierte Lebensdauer | Layline beachten |
| 3 | Falscher Schlauchtyp (zu niedriger Druck) | Bersten unter Last | SAE-Typ nach Arbeitsdruck wählen |
| 4 | Falscher Fluid-Typ eingefüllt | Dichtungsversagen | Herstellerangabe prüfen |
| 5 | Fitting übergedreht | Konusschaden, Undichtheit | Drehmomentschlüssel verwenden |
| 6 | Fitting nicht gekontert | Schlauch-Torsion | Immer zwei Schlüssel verwenden |
| 7 | Schlauch zu kurz | Zugbelastung, Abriss | 10–20% Zusatzlänge einplanen |
| 8 | Schlauch zu lang | Scheuern, Knicken | Saubere Verlegung planen |
| 9 | Fehlende Scheuerschutz | Außendeckenschaden | Spiralschutz, Gummipuffer |
| 10 | Keine Entlüftung nach Montage | Schwammige Steuerung | 20–30× Anschlag zu Anschlag |
| 11 | Verschiedene Fluid-Typen gemischt | Schlammbildung, Versagen | System vorher spülen |
| 12 | Schlauch an heißem Teil verlegt | Thermische Schädigung | Min. 50 mm Abstand |
| 13 | Crimp mit falschem Dorn | Leckage oder Abriss | Herstellervorgabe exakt einhalten |
| 14 | Schutzstopfen zu früh entfernt | Verschmutzung | Stopfen erst beim Anschluss entfernen |
| 15 | Kein Installationsdatum dokumentiert | Alter unbekannt | Datum auf Kabelbinder am Schlauch |

---

## ANHANG M — Zusammenfassung der Schlüsselkennwerte

### Quick-Reference: Druckklassen

| Anwendung | Min. Arbeitsdruck | Empfohlener SAE-Typ | Min. DN |
|-----------|------------------|--------------------|---------| 
| Steuerung Boot <12 m | 100 bar | R7 oder R1 | 6 mm |
| Steuerung Boot 12–25 m | 200 bar | R2 | 10 mm |
| Steuerung Yacht >25 m | 300 bar | R2 oder R12 | 16 mm |
| Stabilisator | 250 bar | R2 oder R12 | 12 mm |
| Winsch | 250 bar | R2 | 10 mm |
| Bugstrahlruder | 200 bar | R2 | 12 mm |
| Trimmklappen | 100 bar | R1 | 6 mm |

### Quick-Reference: Lebensdauer

| Faktor | Richtwert |
|--------|-----------|
| Max. Betriebsdauer (DNV-GL) | 6 Jahre |
| Max. Betriebsdauer (Praxis) | 6–8 Jahre |
| Max. Lagerdauer (SAE J1942) | 10 Jahre |
| Max. Gesamtalter (SAE J1942) | 15 Jahre ab Herstellung |
| Inspektionsintervall | 12 Monate (max.) |
| Ölwechselintervall | 24 Monate oder 1.000 Bh |
| Filterwechselintervall | 12 Monate oder 500 Bh |

---

## ANHANG N — Spezialanwendungen

### Hydraulische Gangways / Passerellen

**Hersteller**: Besenzoni (IT), Opacmare (IT), Mar.Co (IT), Nautical Structures (NL)

**Besonderheiten:**
- Zylinderdruck: 100–200 bar
- Schläuche: SAE R2, DN 8–12
- Häufige Bewegung → Impulsfestigkeit wichtig
- Salzwasser-Exposition der Fittings → 316L obligatorisch
- Sicherheitsventil (Halteventil) am Zylinder pflicht

### Hydraulische Schwimmplattformen / Bathing Platforms

**Hersteller**: Nautical Structures, Opacmare, Besenzoni, Custom-Lösungen

**Besonderheiten:**
- Zylinderdruck: 150–250 bar (hohe Lasten)
- Schläuche: SAE R2/R12, DN 12–19
- Salzwasser-direkte-Exposition
- Korrosionsschutz höchster Stufe
- Sicherheitsventile (Rohrbruchsicherung) obligatorisch

### Hydraulische Rollreffsysteme

**Hersteller**: Reckmann (DE), Profurl (FR), Facnor (FR), Harken (IT/US)

**Besonderheiten:**
- Niedrige Drehzahl, hohes Drehmoment
- Systemdruck: 150–280 bar
- Schläuche: SAE R2, DN 10–16
- Decksdurchführung mit UV-Schutz
- Rotation: Drehgelenk-Fittings an Motor/Zylinder

### Hydraulische Ankerwindschen

**Hersteller**: Lewmar, Lofrans, Maxwell, Quick (IT), Muir (AU)

**Besonderheiten:**
- Intermittierender Betrieb (hohe Ströme, kurze Dauer)
- Druckspitzen beim Ankerbruch berücksichtigen (+50%)
- Saugschlauch (R4) kritisch — Kavitation vermeiden
- Typische Konfiguration: Power Pack im Maschinenraum, Schläuche zum Bug

### Hydraulische Hubdächer und Hardtops

**Hersteller**: Webasto, Alu-Design (DE), Opacmare (IT), Nautical Structures (NL)

**Besonderheiten:**
- Zylinderdruck: 80–150 bar
- Schläuche: SAE R1/R2, DN 6–10
- Langsame, kontrollierte Bewegung (Drossel/Proportionalventil)
- Äußere Schläuche: UV-Schutz obligatorisch
- Sicherheitsventil (Rohrbruchsicherung) an allen Hubzylindern
- Schlauchführung muss Dachbewegung folgen (Schleppkette oder Spiralschlauch)

**Typischer Schlauchbedarf:**
- 2× Druckleitung: DN 6–8, SAE R1/R2, je 3–5 m
- 2× Rücklauf: DN 8–10, SAE R1, je 3–5 m
- Gesamt: 4 Schläuche, 12–20 m

### Hydraulische Tender-Lift-Systeme

**Hersteller**: Nautical Structures, Opacmare, Besenzoni, Mar.Co, NautaLift

**Besonderheiten:**
- Hohe Lasten (Tender: 500–5.000 kg)
- Zylinderdruck: 200–350 bar
- Schläuche: SAE R2/R12, DN 12–25
- Rohrbruchsicherung an allen Lastzylindern **obligatorisch**
- Regelmäßige Lastprüfung (jährlich, mit 125% Nennlast)
- Schlauchinspektion bei jeder Lastprüfung
- Salzwasser-Direktexposition → 316L-Fittings, EPDM-Außendecke

**Sicherheitsanforderungen:**
- DNV-GL: Sicherheitsfaktor Schlauch ≥ 5:1 (statt 4:1) für Lastaufnahmemittel
- Rohrbruchsicherung: max. Absinkgeschwindigkeit 0.3 m/s bei Schlauchbruch
- Doppelter Sicherungskreis: mechanische UND hydraulische Verriegelung
- Notablass: manuelle Absenkung bei Stromausfall muss möglich sein

**Typischer Schlauchbedarf:**
- 2× Druckleitung: DN 16–25, SAE R12, je 4–8 m
- 2× Rücklauf: DN 19–25, SAE R2, je 4–8 m
- 1× Lecköl: DN 6–10, SAE R1, 4–8 m
- Gesamt: 5 Schläuche, 20–40 m
- Kosten: 1.200–3.500 EUR (nur Schläuche + Fittings)

---

## ANHANG O — Umwelt und Entsorgung

### Altöl-Entsorgung

- Hydrauliköl ist **Sonderabfall** — niemals ins Meer oder Bilge!
- Sammlung in dichten Behältern (PE-Kanister)
- Abgabe bei Hafenmeisterei (Bilge-/Ölsammelstelle) oder Wertstoffhof
- Kosten: 0–2 EUR/l bei Yachthäfen, kostenlos bei vielen Recyclinghöfen
- **Bußgelder bei illegaler Entsorgung**: bis 50.000 EUR (Deutschland)

### Schlauch-Entsorgung

- Alte Hydraulikschläuche: Kategorie Gummi-Metall-Verbund
- Wertstoffhof: Kategorie "Sperrmüll" oder "Gummi"
- Spezial-Recycling: Pyrolyse-Verfahren für Energiegewinnung
- Fittings (Stahl/Edelstahl): Metallrecycling

### Ökologische Alternativen

- HEES-Fluide (biologisch abbaubare synthetische Ester) für umweltsensible Gebiete
- HETG-Fluide (Rapsöl-basiert) als Alternative, aber temperaturempfindlich
- Leckage-Minimierung durch hochwertige Fittings und regelmäßige Wartung
- Auffangwannen unter Power Packs (ABYC H-32 empfohlen)

---

## ANHANG P — Erweiterte FAQ

### HY-026: Kann ich einen Hydraulikschlauch kürzen?
**Antwort**: Nein, nicht ohne Neuvercrimpung. Ein Crimp-Schlauch kann nicht gekürzt und wieder verwendet werden. Ein neuer Schlauch in korrekter Länge muss angefertigt werden. Nur Reusable-Fittings erlauben eine Anpassung an Bord.
**Confidence**: measured

### HY-027: Was ist der Unterschied zwischen JIC und ORFS?
**Antwort**: JIC dichtet metalisch am 37°-Konus (Metall-auf-Metall). ORFS dichtet über einen O-Ring an einer planen Fläche. ORFS ist vibrationsfester und leckagefreier, aber teurer. Für Neuanlagen auf Yachten >25 m wird ORFS zunehmend bevorzugt.
**Confidence**: measured

### HY-028: Brauche ich feuerfeste Schläuche im Maschinenraum?
**Antwort**: Gemäß ISO 9094 und ABYC P-1 müssen Hydraulikschläuche im Maschinenraum entweder 30 Minuten feuerfest sein ODER ausreichenden Abstand zu Zündquellen haben. Parker FireGuard (FR881) und Continental Flexon Fire sind marine-zugelassene feuerfeste Schläuche.
**Confidence**: measured

### HY-029: Wie messe ich den Druck in meinem Hydrauliksystem?
**Antwort**: Mit einem Manometer über einen T-Stück-Adapter an der Druckleitung. Messbereich: 2× erwarteter Arbeitsdruck. Digitale Manometer (Parker SCJN-016-01) sind genauer und einfacher abzulesen. Nie die Messstelle unter Druck öffnen!
**Confidence**: benchmark

### HY-030: Was bedeutet die Farbmarkierung auf Hydraulikschläuchen?
**Antwort**: Verschiedene Hersteller verwenden Farbcodes für Druckklassen oder Produktlinien. Parker GlobalCore: Blau (481/R1), Rot (482/R2), Gelb (487/R12). Gates: Schwarz mit farbigem Streifen. Die Farbcodierung ist NICHT normiert — immer Aufdruck lesen!
**Confidence**: benchmark

### HY-031: Kann ich Hydraulikschläuche durch Stahlrohre ersetzen?
**Antwort**: Teilweise ja — für gerade, starre Abschnitte sind nahtlose Stahlrohre (DIN 2391, Werkstoff 1.4571) sogar vorzuziehen (kein Altern, höhere Druckfestigkeit). Schläuche sind nur dort nötig, wo Flexibilität erforderlich ist (Motorlager, Ruderbewegung, Vibrationsentkopplung).
**Confidence**: benchmark

### HY-032: Wie erkenne ich gefälschte Hydraulikschläuche?
**Antwort**: Warnsignale: fehlende oder unvollständige Aufdruck-Information, kein Herstellerlogo, unrealistisch niedriger Preis, keine Begleitdokumentation. Originalschläuche haben: DOT-Nummer, Herstellername, SAE-Typ, Druckklasse, Herstellungsdatum. Im Zweifel: nur bei autorisierten Händlern kaufen.
**Confidence**: benchmark

### HY-033: Was ist der Unterschied zwischen Saug- und Druckschlauch?
**Antwort**: Saugschläuche (SAE R4) haben eine Drahtwendel gegen Kollabieren bei Unterdruck und einen größeren Durchmesser für niedrige Strömungsgeschwindigkeit. Druckschläuche (R1/R2) haben Drahtgeflecht/Spirale gegen Aufweitung. Nie einen Druckschlauch als Saugschlauch verwenden!
**Confidence**: measured

### HY-034: Wie wichtig ist die korrekte Schlauchlänge?
**Antwort**: Sehr wichtig. Zu kurz: Zugbelastung auf Fittings, Knickgefahr. Zu lang: Scheuern, Schwingen, Knicken. Faustregel: Gerade Verbindung + 5–10% Zusatzlänge für Bogenverlauf und thermische Ausdehnung. Bei Ruderleitungen: max. Ruderlage berücksichtigen!
**Confidence**: benchmark

### HY-035: Darf ich verschiedene Schlauchmarken in einem System verwenden?
**Antwort**: Ja, sofern SAE-Typ, Druckklasse und Fluidkompatibilität übereinstimmen. Es wird jedoch empfohlen, innerhalb eines Kreislaufs (z.B. Steuerung) einheitliche Produkte zu verwenden, um die Wartung zu vereinfachen und Verwechslungen zu vermeiden.
**Confidence**: benchmark

---

## ANHANG Q — Zeitleiste: Entwicklung der Yacht-Hydraulik

| Jahr | Meilenstein |
|------|------------|
| 1950er | Erste hydraulische Ruderanlagen auf Großyachten, Industriehydraulik adaptiert |
| 1960er | Teleflex (SeaStar) entwickelt erschwingliche Hydrauliksteuerung für Sportboote |
| 1970er | Naiad Dynamics entwickelt erste Flossen-Stabilisatoren für Yachten |
| 1975 | SAE J517 100R-Serie etabliert als globaler Standard |
| 1980er | Lewmar und Harken führen hydraulische Winschen ein |
| 1985 | Thermoplastische Schläuche (R7/R8) für kompakte Marine-Steuerung |
| 1990er | Parker GlobalCore-System vereinheitlicht Crimp-Technologie |
| 1995 | ABYC H-32 Standard für marine Hydrauliksysteme veröffentlicht |
| 2000 | Superyacht-Boom treibt Entwicklung komplexer Hydrauliksysteme |
| 2005 | Zero-Speed-Stabilisatoren revolutionieren Ankerkomfort |
| 2010 | DNV-GL verschärft Anforderungen an Schlauch-Lebensdauer (6-Jahres-Regel) |
| 2015 | Biologisch abbaubare Hydraulikfluide gewinnen Bedeutung |
| 2016 | SAE J1942 aktualisiert mit verschärften Marine-Anforderungen |
| 2020 | Elektrohydraulische Aktuatoren reduzieren Schlauchbedarf |
| 2023 | Parker IoT-Hydraulik ermöglicht digitale Schlauchüberwachung |
| 2025 | Eaton LifeSense Draht-Überwachung für marine Anwendungen |

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitt |
|-----------|-----------|
| 1SN / 2SN | Grundlagen — SAE 100R1/R2, Anhang B |
| ABYC H-32 | Einführung — Regulatorischer Rahmen |
| Alterungsmechanismen | Lebensdauer und Alterungsmechanismen |
| ATF (Fluid) | Grundlagen — Hydraulikflüssigkeiten |
| Außendecke | Grundlagen — Schlauchmaterialien |
| Beule (Schlauch) | Fehlerbild-Atlas — Fehlerbild 3 |
| Biegeradius | Anhang C, Fehlerbild 5 |
| Bordausstattung | Anhang E |
| BSP-Gewinde | Grundlagen — Fittings |
| Bugstrahlruder | Anlagen-spezifische Zuordnung |
| CE-Richtlinie | Einführung — Regulatorischer Rahmen |
| Crimpung | Schlauchschellen & Verbindungstechnik |
| Dash-Size | Grundlagen — JIC 37°, Glossar |
| DIN EN 853/856/857 | Einführung — DIN EN-Normen |
| DNV-GL | Einführung — Klassifikationsgesellschaften |
| Druckverlust | Technische Referenz — Berechnung |
| Entlüftung | Einbau-/Austausch-Anleitung |
| Fallstudien | Anhang F |
| Fehlerbild-Atlas | Fehlerbild-Atlas |
| Feuerfeste Schläuche | Anhang P — HY-028 |
| Fittings (JIC/SAE/BSP) | Grundlagen — Fittings |
| Fluid-Typen | Grundlagen — Hydraulikflüssigkeiten |
| Gates | Hersteller — Gates |
| GlobalCore (Parker) | Hersteller — Parker |
| Hydraulikfluid | Grundlagen — Hydraulikflüssigkeiten |
| Injektionsverletzung | Notfall-Ressourcen, Glossar |
| JIC 37° | Grundlagen — Fittings |
| Kobelt | Hersteller — Kobelt |
| Korrosion (Fitting) | Fehlerbild-Atlas — Fehlerbild 4 |
| Kostenberechnung | Technische Referenz — Kosten |
| Lebensdauer | Lebensdauer und Alterungsmechanismen |
| Leckage | Fehlerbild-Atlas — Fehlerbild 2, 10 |
| Lecomble & Schmitt | Hersteller — Lecomble & Schmitt |
| Manuli | Hersteller — Manuli |
| Naiad Dynamics | Anlagen-spezifische Zuordnung — Stabilisatoren |
| Notsteuerung | FAQ — HY-015, Notfall-Ressourcen |
| ORFS | Grundlagen — Fittings, FAQ — HY-027 |
| Parker Hannifin | Hersteller — Parker |
| Passerelle | Anhang N — Spezialanwendungen |
| Prüfverfahren | Anhang K |
| Pydantic-Modelle | Pydantic-Modelle |
| Risk Matrix | Anhang H |
| Rollreffsystem | Anhang N — Spezialanwendungen |
| Ruderhydraulik | Anlagen-spezifische Zuordnung |
| SAE 100R-Serie | Grundlagen — SAE 100R |
| SAE J1942 | Einführung — SAE-Standards, FAQ — HY-017 |
| Schnellkupplungen | Schlauchschellen & Verbindungstechnik |
| Schnell-Referenz | Schnell-Referenz |
| SeaStar/BayStar | Hersteller — SeaStar |
| Sichtprüfung | Anhang K — Prüfverfahren |
| Spiralverstärkung | Grundlagen — SAE 100R12 |
| Stabilisator | Anlagen-spezifische Zuordnung |
| Steuerung (schwammig) | Fehlerbehebungs-Leitfaden — Problem 1 |
| Thruster | Anlagen-spezifische Zuordnung |
| Torsion | Fehlerbild-Atlas — Fehlerbild 11 |
| UV-Degradation | Fehlerbild-Atlas — Fehlerbild 1 |
| Vetus | Hersteller — Vetus |
| Winsch | Anlagen-spezifische Zuordnung |
| Zero-Speed | Glossar, Anhang Q |
| Zukunftstechnologien | Zukunftstechnologien |

---

## ANHANG R-1 — Detaillierte Normenanforderungen

### SAE J1942:2016 — Hose and Hose Assemblies for Marine Applications

#### Abschnitt 4 — Anforderungen im Detail

**4.1 Allgemeine Konstruktionsanforderungen:**
- Schläuche müssen für die vorgesehene Anwendung und den vorgesehenen Druck geeignet sein
- Konstruktionsfaktor (Berstdruck / Arbeitsdruck) ≥ 4:1 für marine Anwendungen
- Alle Materialien müssen salzwasserbeständig sein
- Fittings müssen korrosionsbeständig (min. 316L oder gleichwertig) sein

**4.2 Impulsfestigkeit (verschärft gegenüber SAE J517):**
- Marine-Schläuche müssen 150% der J517-Impulsfestigkeit aufweisen
- Prüfung bei 133% des Arbeitsdrucks, 1 Hz, bei Betriebstemperatur
- R1/R2: min. 300.000 Zyklen (vs. 200.000 bei J517)
- R12/R13: min. 750.000 Zyklen (vs. 500.000 bei J517)

**4.3 Umgebungsbedingungen:**
- UV-Beständigkeit: ASTM G154, 1000 h, keine sichtbaren Risse
- Salzsprühnebelbeständigkeit: ISO 9227, 500 h, keine funktionsmindernde Korrosion
- Ozonbeständigkeit: ISO 1431, 100 h, 50 pphm, keine sichtbaren Risse
- Vibrationsfestigkeit: Sinusförmig, 10–200 Hz, 1.5 g, 10 h

**4.4 Kennzeichnung:**
- Herstellername oder -zeichen
- SAE J1942 Referenz
- Schlauchtyp (SAE 100R-Nummer)
- Nenn-Innendurchmesser (Dash-Size oder mm)
- Arbeitsdruck (bar oder psi)
- Quartal und Jahr der Herstellung
- Losnummer für Rückverfolgbarkeit

**4.5 Lagerung und Lebensdauer:**
- Max. Lagerdauer: 10 Jahre ab Herstellungsdatum
- Max. Betriebsdauer: 5 Jahre ab Installation ODER 15 Jahre ab Herstellung
- Lagerung: trocken, dunkel, <30°C, ozonarm, nicht auf engem Radius

### ABYC H-32 (2019) — Hydraulic Systems — Detailierte Anforderungen

**Abschnitt 32.5 — Schlauchauswahl:**
- Arbeitsdruck des Schlauchs ≥ maximaler Systemdruck (inkl. Druckspitzen)
- Temperaturbereich des Schlauchs muss Betriebsbereich abdecken (inkl. Maschinenraum)
- Fluidkompatibilität muss vom Schlauchhersteller bestätigt sein
- Schläuche müssen den Mindestbiegeradius des Herstellers einhalten

**Abschnitt 32.6 — Schlauchverlegung:**
- Schläuche dürfen nicht als tragende Elemente verwendet werden
- Schläuche müssen gegen Scheuern, Abrieb und mechanische Beschädigung geschützt sein
- Schläuche im Maschinenraum: feuerfest oder min. 25 mm Abstand zu Zündquellen
- Schläuche dürfen nicht an beweglichen Maschinenteilen scheuern
- Auffangwannen unter Hydraulikaggregaten empfohlen

**Abschnitt 32.7 — Fittings:**
- Fittings müssen zum Schlauchtyp und -hersteller passen
- Crimp-Fittings: nach Herstellervorgabe verarbeitet (Crimp-Protokoll)
- Reusable-Fittings: jährliche Inspektion auf Lockerung
- Fittings im Salzwasserbereich: korrosionsbeständig (316L empfohlen)

**Abschnitt 32.8 — Prüfung:**
- Druckprüfung nach Installation: 1.5× Arbeitsdruck, 5 Minuten
- Jährliche Sichtinspektion
- Dokumentation aller Hydraulikkomponenten (Typ, Hersteller, Installationsdatum)

### DNV-GL Rules for Classification — Hydrauliksysteme

**Part 4, Chapter 6, Section 5 — Piping Systems:**

**5.1 Allgemeine Anforderungen:**
- Alle Hydraulikschläuche auf klassifizierten Yachten müssen DNV-GL Type Approved sein
- Type Approval-Nummer muss auf dem Schlauch dauerhaft aufgebracht sein
- Schlauchlebensdauer: max. 6 Jahre unabhängig vom Zustand
- Jährliche Inspektion durch qualifiziertes Personal

**5.2 Steuerungssysteme:**
- Hauptruderanlage: Berstdruck ≥ 4× Arbeitsdruck
- Redundante Steuerhydraulik auf Yachten >24 m Lpp
- Automatische Umschaltung auf Notsystem bei Druckverlust
- Notruder-Betätigung ohne Energie (Handpumpe oder Pinne)

**5.3 Brandschutz:**
- Schläuche im Maschinenraum: IMO-A.753(18)-konform ODER feuerbeständig 30 min
- Min. 100 mm Abstand zu Abgassystemen (ohne Feuerschutzhülle)
- Auffangeinrichtung unter Hydraulikaggregaten (Ölfangwanne)

**5.4 Dokumentation:**
- Hydraulikschaltplan an Bord
- Wartungshandbuch für Hydrauliksystem
- Ersatzteilliste mit Teilenummern
- Wartungsprotokoll (Inspektionen, Ölwechsel, Schlauchwechsel)

### ISO 6605:2017 — Prüfverfahren für Hydraulikschläuche (Zusammenfassung)

| Prüfung | Methode | Akzeptanzkriterium |
|---------|---------|-------------------|
| Druckprüfung | 2× WP, 60 s | Keine Leckage, keine Verformung |
| Berstprüfung | Drucksteigerung bis Versagen | ≥ Nenn-Berstdruck |
| Impulsprüfung | ISO 6803, 133% WP | ≥ Nennimpulszyklenzahl |
| Biegeprüfung | Biegen auf Mindestradius unter WP | Keine Leckage |
| Zugprüfung | Axiale Belastung | Keine Trennung bei 100% WP |
| Kälteprüfung | Biegen bei Tmin | Keine Rissbildung |
| Volumenausdehnung | Druckbeaufschlagung | ≤ Nenn-Volumenzunahme |
| Leitfähigkeit | Elektrische Messung | ≤ 10⁶ Ω/m (für statische Entladung) |
| Kompatibilität | 168 h bei Tmax in Fluid | Δ Volumen/Härte innerhalb Grenzen |

### Vergleichstabelle: Normenanforderungen Marine vs. Industrie

| Kriterium | Industrie (SAE J517) | Marine (SAE J1942) | Klasse (DNV-GL) |
|-----------|---------------------|-------------------|-----------------|
| Berstfaktor | 4:1 | 4:1 | 4:1 |
| Impulsfestigkeit R2 | 200.000 | 300.000 | 300.000 |
| Impulsfestigkeit R12 | 500.000 | 750.000 | 750.000 |
| UV-Beständigkeit | Nicht gefordert | 1000 h ASTM G154 | 1000 h |
| Salzsprühnebel | Nicht gefordert | 500 h ISO 9227 | 500 h |
| Max. Lebensdauer | Nicht festgelegt | 15 Jahre total | **6 Jahre Betrieb** |
| Jährliche Inspektion | Empfohlen | Empfohlen | **Obligatorisch** |
| Redundanz Steuerung | Nicht gefordert | Ab 12 m (CE Kat. A/B) | Ab 24 m Lpp |
| Feuerfestigkeit | Nicht gefordert | Maschinenraum empfohlen | IMO-A.753(18) |
| Dokumentation | Schlauchkennzeichnung | Erweiterte Kennzeichnung | Vollständig |
| Materialzertifikat | 2.1 | 2.2 | 3.1 (EN 10204) |
| Fitting-Korrosionsschutz | Verzinkung genügt | 316L empfohlen | 316L gefordert |

---

## ANHANG R-1a — Kostenkalkulation: Gesamtsysteme nach Bootsgröße

### Kostenrahmen Hydrauliksystem-Neubau (Material + Arbeit)

#### Segelyacht 12 m (Ruder + Autopilot)

| Komponente | Material (EUR) | Arbeit (EUR) | Gesamt (EUR) |
|-----------|---------------|-------------|-------------|
| Steuerpumpe (Lecomble & Schmitt HB 4210) | 680 | 200 | 880 |
| Steuerzylinder (CT 90) | 450 | 150 | 600 |
| Schläuche (2× R7 DN 6, je 8 m) | 220 | 180 | 400 |
| Hydraulikfluid (LHM Plus, 2 l) | 35 | — | 35 |
| Fittings (8× BSP 1/4") | 80 | — | 80 |
| Autopilot-Anbindung (Raymarine Ventil) | 380 | 120 | 500 |
| **Gesamt** | **1.845** | **650** | **2.495** |

#### Motoryacht 18 m (Ruder + Bugstrahlruder + Trimmklappen)

| Komponente | Material (EUR) | Arbeit (EUR) | Gesamt (EUR) |
|-----------|---------------|-------------|-------------|
| Steuerpumpe (Kobelt 7003) | 1.200 | 300 | 1.500 |
| Steuerzylinder (Kobelt 2020) | 980 | 250 | 1.230 |
| Power Pack Steuerung | 1.800 | 400 | 2.200 |
| Steuerschläuche (4× R2 DN 10, 28 m) | 620 | 350 | 970 |
| Bugstrahlruder HPU (Side-Power SH160) | 2.400 | 500 | 2.900 |
| Bugstrahlruder-Schläuche (5× R2, 22 m) | 480 | 300 | 780 |
| Trimmklappen-Hydraulik (Bennett) | 680 | 200 | 880 |
| Trimmklappen-Schläuche (4× R1 DN 6, 16 m) | 180 | 150 | 330 |
| Hydraulikfluid (HLP 32, 15 l) | 180 | — | 180 |
| Fittings (alle, JIC) | 380 | — | 380 |
| **Gesamt** | **8.900** | **2.450** | **11.350** |

#### Motoryacht 35 m (Komplettsystem)

| Komponente | Material (EUR) | Arbeit (EUR) | Gesamt (EUR) |
|-----------|---------------|-------------|-------------|
| Ruderanlage (redundant) | 8.500 | 2.500 | 11.000 |
| Stabilisatoren (Naiad S1000) | 45.000 | 8.000 | 53.000 |
| Bugstrahlruder (hydraulisch) | 6.500 | 2.000 | 8.500 |
| Heckstrahlruder | 5.800 | 1.800 | 7.600 |
| Ankerspill (hydraulisch) | 3.200 | 1.200 | 4.400 |
| Passerelle (hydraulisch) | 4.500 | 1.500 | 6.000 |
| Davit (hydraulisch) | 3.800 | 1.200 | 5.000 |
| Schwimmplattform | 5.200 | 1.800 | 7.000 |
| Hydraulikschläuche gesamt (ca. 150 m) | 6.800 | 4.500 | 11.300 |
| Hydraulikfluid (HLP 46, 80 l) | 1.200 | — | 1.200 |
| Zentrales Power Pack | 12.000 | 3.000 | 15.000 |
| **Gesamt** | **102.500** | **27.500** | **130.000** |

### Wartungskosten über 20 Jahre (Lebenszyklus)

| Bootsklasse | Jährliche Wartung | Schlauchwechsel (3×) | Ölwechsel (10×) | Filter (20×) | 20-Jahres-Gesamt |
|-------------|------------------|---------------------|-----------------|-------------|-----------------|
| Segelyacht 12 m | 200 EUR/Jahr | 3 × 500 EUR | 10 × 80 EUR | 20 × 40 EUR | **6.500 EUR** |
| Motoryacht 18 m | 500 EUR/Jahr | 3 × 2.000 EUR | 10 × 250 EUR | 20 × 120 EUR | **20.900 EUR** |
| Motoryacht 35 m | 2.000 EUR/Jahr | 3 × 12.000 EUR | 10 × 1.200 EUR | 20 × 500 EUR | **98.000 EUR** |

---

## ANHANG R-2 — Erweiterte technische Datenblätter

### Parker GlobalCore 481 (SAE 100R1AT / DIN EN 853 1SN) — Vollständige Spezifikation

| Parameter | DN 6 | DN 8 | DN 10 | DN 12 | DN 16 | DN 19 | DN 25 |
|-----------|-------|-------|--------|--------|--------|--------|--------|
| Innendurchmesser (mm) | 6.4 | 7.9 | 9.5 | 12.7 | 15.9 | 19.1 | 25.4 |
| Außendurchmesser (mm) | 13.4 | 15.1 | 17.4 | 20.6 | 23.8 | 27.0 | 33.3 |
| Arbeitsdruck (bar) | 225 | 215 | 180 | 160 | 130 | 115 | 90 |
| Berstdruck (bar) | 900 | 860 | 720 | 640 | 520 | 460 | 360 |
| Biegeradius (mm) | 75 | 90 | 105 | 125 | 150 | 180 | 240 |
| Gewicht (g/m) | 220 | 270 | 340 | 440 | 550 | 680 | 950 |
| Temperatur (°C) | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 |
| Innenrohr | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A |
| Verstärkung | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht | 1× Stahldrahtgeflecht |
| Außendecke | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR |
| Impulsfestigkeit | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 |

### Parker GlobalCore 482 (SAE 100R2AT / DIN EN 853 2SN) — Vollständige Spezifikation

| Parameter | DN 6 | DN 8 | DN 10 | DN 12 | DN 16 | DN 19 | DN 25 |
|-----------|-------|-------|--------|--------|--------|--------|--------|
| Innendurchmesser (mm) | 6.4 | 7.9 | 9.5 | 12.7 | 15.9 | 19.1 | 25.4 |
| Außendurchmesser (mm) | 15.7 | 18.3 | 20.6 | 24.2 | 28.2 | 31.4 | 38.9 |
| Arbeitsdruck (bar) | 400 | 350 | 330 | 275 | 250 | 215 | 165 |
| Berstdruck (bar) | 1600 | 1400 | 1320 | 1100 | 1000 | 860 | 660 |
| Biegeradius (mm) | 100 | 115 | 130 | 180 | 200 | 240 | 300 |
| Gewicht (g/m) | 360 | 450 | 560 | 720 | 920 | 1120 | 1580 |
| Temperatur (°C) | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 |
| Innenrohr | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A |
| Verstärkung | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht | 2× Stahldrahtgeflecht |
| Außendecke | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR |
| Impulsfestigkeit | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 | 200.000 |

### Parker GlobalCore 487 (SAE 100R12 / DIN EN 856 4SP) — Vollständige Spezifikation

| Parameter | DN 12 | DN 16 | DN 19 | DN 25 | DN 32 | DN 38 | DN 51 |
|-----------|--------|--------|--------|--------|--------|--------|--------|
| Innendurchmesser (mm) | 12.7 | 15.9 | 19.1 | 25.4 | 31.8 | 38.1 | 50.8 |
| Außendurchmesser (mm) | 27.4 | 30.6 | 34.1 | 42.1 | 50.0 | 56.4 | 70.6 |
| Arbeitsdruck (bar) | 420 | 380 | 350 | 280 | 210 | 210 | 210 |
| Berstdruck (bar) | 1680 | 1520 | 1400 | 1120 | 840 | 840 | 840 |
| Biegeradius (mm) | 180 | 200 | 240 | 340 | 420 | 500 | 630 |
| Gewicht (g/m) | 1050 | 1280 | 1580 | 2200 | 3100 | 3800 | 5200 |
| Temperatur (°C) | -40/+121 | -40/+121 | -40/+121 | -40/+121 | -40/+121 | -40/+121 | -40/+121 |
| Innenrohr | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A | NBR, Klasse A |
| Verstärkung | 4× Spiraldraht | 4× Spiraldraht | 4× Spiraldraht | 4× Spiraldraht | 4× Spiraldraht | 4× Spiraldraht | 4× Spiraldraht |
| Außendecke | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR | SuperTough CR |
| Impulsfestigkeit | 500.000 | 500.000 | 500.000 | 500.000 | 500.000 | 500.000 | 500.000 |

### Gates MegaSys MXT (SAE 100R2AT) — Vollständige Spezifikation

| Parameter | DN 6 | DN 10 | DN 12 | DN 16 | DN 19 | DN 25 |
|-----------|-------|--------|--------|--------|--------|--------|
| Innendurchmesser (mm) | 6.4 | 9.5 | 12.7 | 15.9 | 19.1 | 25.4 |
| Außendurchmesser (mm) | 15.5 | 20.2 | 23.8 | 27.8 | 31.0 | 38.5 |
| Arbeitsdruck (bar) | 400 | 330 | 275 | 250 | 215 | 165 |
| Berstdruck (bar) | 1600 | 1320 | 1100 | 1000 | 860 | 660 |
| Biegeradius (mm) | 100 | 130 | 180 | 200 | 240 | 300 |
| Temperatur (°C) | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 |
| MegaCrimp kompatibel | Ja | Ja | Ja | Ja | Ja | Ja |
| Gates Teilenummer | MXT-4 | MXT-6 | MXT-8 | MXT-10 | MXT-12 | MXT-16 |

### Continental Flexon 2SN (DIN EN 853 2SN) — Vollständige Spezifikation

| Parameter | DN 6 | DN 10 | DN 12 | DN 16 | DN 19 | DN 25 |
|-----------|-------|--------|--------|--------|--------|--------|
| Innendurchmesser (mm) | 6.3 | 9.5 | 12.5 | 16.0 | 19.0 | 25.0 |
| Außendurchmesser (mm) | 15.2 | 19.8 | 23.4 | 27.4 | 30.6 | 38.0 |
| Arbeitsdruck (bar) | 400 | 330 | 275 | 250 | 215 | 165 |
| Berstdruck (bar) | 1600 | 1320 | 1100 | 1000 | 860 | 660 |
| Biegeradius (mm) | 100 | 130 | 180 | 200 | 240 | 300 |
| Temperatur (°C) | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 | -40/+100 |
| DNV-GL Type Approval | Ja | Ja | Ja | Ja | Ja | Ja |
| Lloyd's Register | Ja | Ja | Ja | Ja | Ja | Ja |

---

## ANHANG R-3 — Detaillierte Systemschemata

### Schema: Vollständige Ruderhydraulik (Motoryacht 20 m)

```
                      ┌─────────────────────────────────┐
                      │         STEUERSTAND              │
                      │                                   │
                      │  ┌──────────────────┐            │
                      │  │ Steuerrad         │            │
                      │  │ ↓                 │            │
                      │  │ Steuerpumpe       │            │
                      │  │ (Kobelt 7003)     │            │
                      │  │ Port A    Port B  │            │
                      │  └──┬──────────┬─────┘            │
                      │     │          │                   │
                      └─────┼──────────┼──────────────────┘
                            │          │
              SAE R2 DN 10  │          │  SAE R2 DN 10
              JIC -6 Fittings│         │  JIC -6 Fittings
              Länge: 12 m   │          │  Länge: 12 m
                            │          │
                      ┌─────┼──────────┼──────────────────┐
                      │     │ MASCHINENRAUM                │
                      │     │          │                   │
                      │  ┌──▼──────────▼─────┐            │
                      │  │  Magnetventilblock │            │
                      │  │  (Autopilot-       │            │
                      │  │   Integration)     │            │
                      │  └──┬──────────┬─────┘            │
                      │     │          │                   │
                      │  ┌──▼──────────▼─────┐            │
                      │  │  Power Pack        │            │
                      │  │  (Kobelt 6527)     │            │
                      │  │  - E-Motor 1.1 kW  │            │
                      │  │  - Pumpe 3.5 l/min │            │
                      │  │  - Tank 5 l        │            │
                      │  │  - Filter 10 µm    │            │
                      │  │  - ÜDV 250 bar     │            │
                      │  └──┬──────────┬─────┘            │
                      │     │          │                   │
                      └─────┼──────────┼──────────────────┘
                            │          │
              SAE R2 DN 12  │          │  SAE R2 DN 12
              JIC -8 Fittings│         │  JIC -8 Fittings
              Länge: 4 m    │          │  Länge: 4 m
                            │          │
                      ┌─────┼──────────┼──────────────────┐
                      │  ┌──▼──────────▼─────┐ LAZARETTE  │
                      │  │  Steuerzylinder    │            │
                      │  │  (Kobelt 2020)     │            │
                      │  │  Hub: 250 mm       │            │
                      │  │  Kraft: 45 kN      │            │
                      │  └──────┬─────────────┘            │
                      │         │                          │
                      │  ┌──────▼─────────────┐            │
                      │  │  Ruderquadrant     │            │
                      │  │  ↓                 │            │
                      │  │  Ruderwelle        │            │
                      │  │  ↓                 │            │
                      │  │  Ruderblatt        │            │
                      │  └────────────────────┘            │
                      └────────────────────────────────────┘
```

**Schlauchbedarf gesamt (dieses System):**

| Position | SAE-Typ | DN | Länge | Fittings | Stück | Kosten |
|----------|---------|-----|-------|----------|-------|--------|
| Steuerstand → MR (Druck) | R2 | 10 | 12 m | JIC -6 | 1 | 380 EUR |
| Steuerstand → MR (Rücklauf) | R2 | 10 | 12 m | JIC -6 | 1 | 380 EUR |
| Power Pack → Zylinder (Druck A) | R2 | 12 | 4 m | JIC -8 | 1 | 180 EUR |
| Power Pack → Zylinder (Druck B) | R2 | 12 | 4 m | JIC -8 | 1 | 180 EUR |
| Autopilot-Leitungen | R7 | 6 | 2×3 m | JIC -4 | 2 | 160 EUR |
| **Gesamt** | | | **38 m** | | **6** | **1.280 EUR** |

### Schema: Stabilisator-Hydraulik (Naiad S1000, Motoryacht 25 m)

```
┌───────────────────────────────────────────────────────┐
│                    MASCHINENRAUM                       │
│                                                       │
│  ┌────────────────────┐    ┌────────────────────┐    │
│  │ Power Pack (BB)     │    │ Power Pack (SB)     │    │
│  │ Naiad HPU-S1000    │    │ (oder gemeinsames   │    │
│  │ - E-Motor 7.5 kW  │    │  HPU mit 2 Kreisen) │    │
│  │ - Pumpe 20 l/min  │    │                      │    │
│  │ - Tank 30 l       │    │                      │    │
│  │ - Servoventil     │    │                      │    │
│  │ - Druckfilter 5µm │    │                      │    │
│  └──┬─┬─┬────────────┘    └──┬─┬─┬──────────────┘    │
│     │ │ │                     │ │ │                    │
│     │ │ └── Lecköl DN 6      │ │ └── Lecköl DN 6    │
│     │ └──── Rücklauf DN 16   │ └──── Rücklauf DN 16 │
│     └────── Druck DN 12      └────── Druck DN 12    │
│                                                       │
└──────┼─┼─┼────────────────────┼─┼─┼──────────────────┘
       │ │ │                    │ │ │
       │ │ │  (Schottdurchführung wasserdicht)
       │ │ │                    │ │ │
┌──────▼─▼─▼────────┐  ┌───────▼─▼─▼──────────────────┐
│  Aktuator BACKBORD │  │  Aktuator STEUERBORD          │
│  Naiad AD-200      │  │  Naiad AD-200                 │
│  - Flossenfläche   │  │  - Flossenfläche              │
│    0.35 m²         │  │    0.35 m²                    │
│  - Schwenkwinkel   │  │  - Schwenkwinkel              │
│    ±25°            │  │    ±25°                       │
│  - 2 Hydraulik-    │  │  - 2 Hydraulik-               │
│    zylinder        │  │    zylinder                   │
└────────────────────┘  └───────────────────────────────┘
```

**Schlauchbedarf Stabilisator (beide Seiten):**

| Position | SAE-Typ | DN | Länge | Stück | Kosten |
|----------|---------|-----|-------|-------|--------|
| Druck Extend (BB+SB) | R2 | 12 | 3 m | 2 | 260 EUR |
| Druck Retract (BB+SB) | R2 | 12 | 3 m | 2 | 260 EUR |
| Rücklauf (BB+SB) | R2 | 16 | 3 m | 2 | 300 EUR |
| Lecköl (BB+SB) | R1 | 6 | 3 m | 2 | 100 EUR |
| Pilot/Servo (BB+SB) | R7 | 6 | 2 m | 4 | 200 EUR |
| **Gesamt** | | | **34 m** | **12** | **1.120 EUR** |

### Schema: Hydraulische Winsch (Lewmar H-Series, Segelyacht 18 m)

```
┌───────────────────────────────────────────────────┐
│                    MASCHINENRAUM                   │
│                                                   │
│  ┌────────────────────────────────┐               │
│  │ Hydraulik Power Pack            │               │
│  │ Lewmar HPU-12                  │               │
│  │ - E-Motor 5.5 kW              │               │
│  │ - Pumpe 12 l/min @ 210 bar    │               │
│  │ - Tank 15 l (HLP 32)          │               │
│  │ - Rücklauffilter 25 µm        │               │
│  │ - Druckfilter 10 µm           │               │
│  │ - Wärmetauscher (Seewasser)    │               │
│  │                                │               │
│  │  Druck OUT ──→  SAE R2 DN 16  │               │
│  │  Rücklauf IN ←── SAE R2 DN 19 │               │
│  └────────────────────────────────┘               │
│                                                   │
└─────────── DURCH DECK ──────────────── ↑ ↓ ──────┘
             (Decksdurchführung)
             (wasserdicht, UV-geschützt)
             
┌───────────────────────────────────────────────────┐
│                    AN DECK                         │
│                                                   │
│  Verteilerblock (Deck-Manifold)                   │
│  ┌──────────────────────────────────┐              │
│  │  Eingang: DN 16 Druck / DN 19 RL│              │
│  │                                  │              │
│  │  Port 1 → Winsch BB vorne       │              │
│  │  Port 2 → Winsch SB vorne       │              │
│  │  Port 3 → Winsch BB achtern     │              │
│  │  Port 4 → Winsch SB achtern     │              │
│  │  Port 5 → Furler                 │              │
│  │  Port 6 → Reserve               │              │
│  └──────────────────────────────────┘              │
│                                                   │
│  Schläuche Manifold → Winschen:                   │
│  SAE R2, DN 10, JIC -6, je 2–5 m                 │
│  (mit UV-Spiralschutz)                            │
│                                                   │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌──────┐       │
│  │W BB│  │W SB│  │W BB│  │W SB│  │Furler │       │
│  │vorn│  │vorn│  │ach.│  │ach.│  │Reckm. │       │
│  └────┘  └────┘  └────┘  └────┘  └──────┘       │
└───────────────────────────────────────────────────┘
```

**Schlauchbedarf Winschsystem:**

| Position | SAE-Typ | DN | Länge | Stück | Kosten |
|----------|---------|-----|-------|-------|--------|
| MR → Deck (Druck) | R2 | 16 | 6 m | 1 | 320 EUR |
| MR → Deck (Rücklauf) | R2 | 19 | 6 m | 1 | 380 EUR |
| Manifold → Winsch (je) | R2 | 10 | 3 m | 10 | 1.200 EUR |
| Manifold → Furler | R2 | 10 | 8 m | 2 | 400 EUR |
| **Gesamt** | | | **52 m** | **14** | **2.300 EUR** |

---

## ANHANG R-4 — Schlauchverlegung: Detaillierte Planungsregeln

### Allgemeine Verlegungsregeln

1. **Biegeradius**: Immer ≥ Mindestbiegeradius (Tabelle Anhang C). Im Zweifel: 1,5× Mindestwert verwenden
2. **Torsion**: Max. ±5° Verdrehung pro 300 mm Schlauchlänge. Layline kontrollieren
3. **Zugbelastung**: Schlauch darf NICHT auf Zug beansprucht werden. Immer Entlastungsschlaufe vorsehen
4. **Bewegungsfreiheit**: Bei beweglichen Anschlüssen (Ruderzylinder, Stabilisator) Schlauch in max. Ausschlag prüfen
5. **Befestigungsabstand**: Alle 300–500 mm eine Schlauchschelle oder Klemme
6. **Scheuerschutz**: Gummipuffer, Spiralschutz oder Textilmantel an allen Kontaktpunkten
7. **Thermischer Abstand**: Min. 50 mm zu Abgasanlagen, 25 mm zu heißen Motorflächen
8. **Elektrischer Abstand**: Min. 50 mm zu Hochspannungskabeln (230V/400V)
9. **Kreuzungen**: Schläuche kreuzen sich maximal im 90°-Winkel, nie parallel reiben
10. **Durchführungen**: Gummitüllen oder Schottverschraubungen verwenden, nie scharfkantig

### Spezielle Verlegungsregeln Marine

11. **Decksdurchführungen**: Wasserdicht (IP67), mit Abtropfring, UV-geschützt
12. **Bilge-Bereich**: Schläuche min. 100 mm über Bilgewasserniveau verlegen
13. **Maschinenraum**: Feuerfeste Schläuche oder Feuerschutzmantel bei <100 mm Abstand zu Abgas
14. **Kielbereich**: Schläuche gegen Grundberührung schützen (Schutzrohr)
15. **Mast-Durchführung**: Flexible Schlauchführung mit Mastbewegung (Rigg-Spannung)
16. **Tankraum**: Schläuche außerhalb von Kraftstofftankräumen verlegen (wenn möglich)
17. **Batterieraum**: Min. 300 mm Abstand zu Batterien (Säure-Dämpfe greifen CR an)

### Farbcodierung der Hydraulikleitungen (Empfehlung)

| Farbe | Leitung | Druckbereich |
|-------|---------|-------------|
| Rot | Druckleitung (Hochdruck) | >100 bar |
| Blau | Rücklaufleitung | <50 bar |
| Gelb | Lecköl / Drainageleitung | <10 bar |
| Grün | Saugleitung | Unterdruck |
| Orange | Steuerleitung / Pilot | 30–100 bar |
| Schwarz | Universell (nicht codiert) | variabel |

**Kennzeichnung**: Farbige Kabelbinder oder Schrumpfschlauch am Fitting, alle 2 m entlang der Leitung

---

## ANHANG R-5 — Drehmoment-Tabellen für alle Fitting-Typen

### JIC 37° Flare Fittings (SAE J514) — Stahl verzinkt

| Dash-Size | Gewinde UNF | Drehmoment Stahl (Nm) | Drehmoment 316L (Nm) | Max. Drehmoment (Nm) |
|-----------|-------------|----------------------|---------------------|---------------------|
| -3 | 3/8"-24 | 10–12 | 8–10 | 14 |
| -4 | 7/16"-20 | 14–16 | 12–14 | 19 |
| -5 | 1/2"-20 | 19–22 | 16–19 | 25 |
| -6 | 9/16"-18 | 24–27 | 20–24 | 32 |
| -8 | 3/4"-16 | 50–55 | 42–50 | 65 |
| -10 | 7/8"-14 | 75–80 | 62–75 | 95 |
| -12 | 1-1/16"-12 | 100–110 | 85–100 | 130 |
| -14 | 1-3/16"-12 | 115–125 | 95–115 | 150 |
| -16 | 1-5/16"-12 | 140–160 | 120–140 | 190 |
| -20 | 1-5/8"-12 | 190–215 | 160–190 | 250 |
| -24 | 1-7/8"-12 | 240–270 | 200–240 | 320 |

### BSP Parallel (BSPP, G-Gewinde) mit Dichtring

| Größe | Gewinde | Drehmoment Stahl (Nm) | Drehmoment 316L (Nm) |
|-------|---------|----------------------|---------------------|
| G 1/8" | G 1/8 | 12–15 | 10–13 |
| G 1/4" | G 1/4 | 20–25 | 17–22 |
| G 3/8" | G 3/8 | 35–40 | 30–36 |
| G 1/2" | G 1/2 | 60–70 | 50–62 |
| G 3/4" | G 3/4 | 85–95 | 72–85 |
| G 1" | G 1 | 110–125 | 95–110 |

### Metrisch Schneidring (DIN 2353), Schwere Reihe S

| Rohrdurchmesser | Gewinde M | Drehmoment Stahl (Nm) | Drehmoment 316L (Nm) |
|----------------|-----------|----------------------|---------------------|
| 6 mm | M 12×1.5 | 18–22 | 15–19 |
| 8 mm | M 14×1.5 | 25–30 | 21–26 |
| 10 mm | M 16×1.5 | 35–40 | 30–35 |
| 12 mm | M 18×1.5 | 50–55 | 42–48 |
| 15 mm | M 22×1.5 | 75–85 | 64–74 |
| 18 mm | M 26×1.5 | 100–115 | 85–100 |
| 22 mm | M 30×2 | 140–160 | 120–140 |
| 28 mm | M 36×2 | 200–230 | 170–200 |

### ORFS (O-Ring Face Seal, SAE J1453)

| Dash-Size | Gewinde UNF | Drehmoment (Nm) | O-Ring (AS568) |
|-----------|-------------|-----------------|----------------|
| -4 | 9/16"-18 | 18–22 | -904 |
| -6 | 11/16"-16 | 32–38 | -906 |
| -8 | 13/16"-16 | 50–58 | -908 |
| -10 | 1"-14 | 70–80 | -910 |
| -12 | 1-3/16"-12 | 95–110 | -912 |
| -16 | 1-7/16"-12 | 135–155 | -916 |
| -20 | 1-11/16"-12 | 180–210 | -920 |

---

## ANHANG R-6 — Erweiterte Berechnungen und Formeln

### Zylindergrößen-Berechnung für Ruderanlage

```python
def calculate_steering_cylinder(
    rudder_torque_nm: float,
    system_pressure_bar: float,
    tiller_arm_mm: float,
) -> dict:
    """
    Calculate required steering cylinder bore diameter.
    
    Args:
        rudder_torque_nm: Required rudder torque in Nm
        system_pressure_bar: System working pressure in bar
        tiller_arm_mm: Tiller arm (quadrant radius) in mm
        
    Returns:
        Dict with cylinder specifications
    """
    import math
    
    # Force required at cylinder rod
    force_n = rudder_torque_nm / (tiller_arm_mm / 1000)
    
    # Pressure in Pa
    pressure_pa = system_pressure_bar * 100000
    
    # Piston area required
    area_m2 = force_n / pressure_pa
    
    # Bore diameter
    bore_m = math.sqrt(4 * area_m2 / math.pi)
    bore_mm = bore_m * 1000
    
    # Standard bore sizes
    standard_bores = [25, 32, 40, 50, 63, 80, 100, 125, 160]
    selected_bore = next((b for b in standard_bores if b >= bore_mm), standard_bores[-1])
    
    # Actual force with selected bore
    actual_area = math.pi * (selected_bore / 2000) ** 2
    actual_force = actual_area * pressure_pa
    
    # Volume per stroke (for hose sizing)
    stroke_mm = 2 * tiller_arm_mm * math.sin(math.radians(35))  # ±35° Ruderlage
    volume_cm3 = actual_area * (stroke_mm / 10) * 10000  # m² × mm → cm³
    
    return {
        "required_force_n": round(force_n, 0),
        "calculated_bore_mm": round(bore_mm, 1),
        "selected_bore_mm": selected_bore,
        "actual_force_n": round(actual_force, 0),
        "safety_factor": round(actual_force / force_n, 2),
        "stroke_mm": round(stroke_mm, 0),
        "volume_per_stroke_cm3": round(volume_cm3, 1),
        "confidence": "calculated",
    }
```

### Volumenstrom-Berechnung für Winschen

```python
def calculate_winch_flow_requirement(
    line_pull_kg: float,
    line_speed_mps: float,
    drum_diameter_mm: float,
    motor_displacement_ccm: float,
    motor_efficiency: float = 0.85,
) -> dict:
    """
    Calculate hydraulic flow requirement for a winch.
    
    Args:
        line_pull_kg: Maximum line pull in kg
        line_speed_mps: Line speed in m/s
        drum_diameter_mm: Winch drum diameter in mm
        motor_displacement_ccm: Hydraulic motor displacement in ccm/rev
        motor_efficiency: Overall motor efficiency (default 0.85)
        
    Returns:
        Dict with flow and pressure requirements
    """
    import math
    
    # Drum speed (rpm)
    drum_circumference_m = math.pi * drum_diameter_mm / 1000
    drum_rpm = (line_speed_mps / drum_circumference_m) * 60
    
    # Required flow
    flow_ccm_min = drum_rpm * motor_displacement_ccm
    flow_lpm = flow_ccm_min / 1000
    
    # Required pressure
    torque_nm = (line_pull_kg * 9.81) * (drum_diameter_mm / 2000)
    pressure_bar = (torque_nm * 2 * math.pi) / (motor_displacement_ccm / 1e6) / 1e5
    pressure_bar = pressure_bar / motor_efficiency
    
    # Hose sizing
    standard_dns = [6, 8, 10, 12, 16, 19, 25, 32]
    max_velocity = 4.0  # m/s
    q_m3s = flow_lpm / 60000
    min_area = q_m3s / max_velocity
    min_d = math.sqrt(4 * min_area / math.pi) * 1000
    selected_dn = next((d for d in standard_dns if d >= min_d), standard_dns[-1])
    
    return {
        "drum_speed_rpm": round(drum_rpm, 1),
        "required_flow_lpm": round(flow_lpm, 1),
        "required_pressure_bar": round(pressure_bar, 0),
        "recommended_hose_dn_mm": selected_dn,
        "recommended_sae_type": "100R2" if pressure_bar <= 400 else "100R12",
        "confidence": "calculated",
    }
```

### Wärmeentwicklung und Kühlerbedarf

```python
def calculate_heat_generation(
    flow_rate_lpm: float,
    pressure_drop_bar: float,
    duty_cycle: float = 0.5,
) -> dict:
    """
    Calculate heat generation in hydraulic system.
    
    Args:
        flow_rate_lpm: System flow rate in l/min
        pressure_drop_bar: Total pressure drop (hose + components) in bar
        duty_cycle: Duty cycle 0.0–1.0 (fraction of operating time)
        
    Returns:
        Dict with heat values and cooler recommendation
    """
    # Power loss = Q × Δp
    q_m3s = flow_rate_lpm / 60000
    dp_pa = pressure_drop_bar * 100000
    power_loss_w = q_m3s * dp_pa
    
    # Average heat generation
    avg_heat_w = power_loss_w * duty_cycle
    
    # Cooler recommendation
    if avg_heat_w < 200:
        cooler = "Kein Kühler erforderlich — natürliche Konvektion reicht"
    elif avg_heat_w < 1000:
        cooler = "Luft-Öl-Kühler empfohlen (Wärmetauscherfläche 0.1–0.5 m²)"
    elif avg_heat_w < 3000:
        cooler = "Seewasser-Öl-Kühler erforderlich (Bowman oder ähnlich)"
    else:
        cooler = "Großer Seewasser-Kühler + Thermostatventil erforderlich"
    
    return {
        "power_loss_w": round(power_loss_w, 0),
        "avg_heat_generation_w": round(avg_heat_w, 0),
        "cooler_recommendation_de": cooler,
        "confidence": "calculated",
    }
```

### Schlauchgewicht-Berechnung (inkl. Fluid)

```python
def calculate_hose_weight(
    sae_type: str,
    inner_diameter_mm: float,
    length_mm: float,
    fluid_density_kg_m3: float = 870,
) -> dict:
    """
    Calculate weight of filled hydraulic hose assembly.
    
    Returns weight in kg for weight distribution analysis.
    """
    import math
    
    # Hose weight per meter (approximate, in g/m)
    hose_weights = {
        "100R1": {6: 220, 8: 270, 10: 340, 12: 440, 16: 550, 19: 680, 25: 950},
        "100R2": {6: 360, 8: 450, 10: 560, 12: 720, 16: 920, 19: 1120, 25: 1580},
        "100R7": {6: 80, 8: 110, 10: 150, 12: 200},
        "100R12": {12: 1050, 16: 1280, 19: 1580, 25: 2200, 32: 3100},
    }
    
    dn = int(inner_diameter_mm)
    weights = hose_weights.get(sae_type, hose_weights["100R2"])
    hose_gpm = weights.get(dn, 500)
    
    length_m = length_mm / 1000
    hose_weight_kg = (hose_gpm / 1000) * length_m
    
    # Fluid weight
    area_m2 = math.pi * (inner_diameter_mm / 2000) ** 2
    volume_m3 = area_m2 * length_m
    fluid_weight_kg = volume_m3 * fluid_density_kg_m3
    
    # Fitting weight (approximate per pair)
    fitting_weights = {6: 0.08, 8: 0.12, 10: 0.18, 12: 0.25, 16: 0.40, 19: 0.55, 25: 0.85}
    fitting_weight_kg = fitting_weights.get(dn, 0.3) * 2
    
    total_kg = hose_weight_kg + fluid_weight_kg + fitting_weight_kg
    
    return {
        "hose_empty_kg": round(hose_weight_kg, 2),
        "fluid_kg": round(fluid_weight_kg, 2),
        "fittings_kg": round(fitting_weight_kg, 2),
        "total_filled_kg": round(total_kg, 2),
        "confidence": "calculated",
    }
```

---

## ANHANG R-7 — Wartungsplan-Vorlagen

### Wartungsplan: Hydraulik Ruderanlage

| Intervall | Tätigkeit | Dauer | Kosten (EUR) |
|-----------|----------|-------|-------------|
| Monatlich | Fluidstand prüfen, nachfüllen wenn nötig | 10 min | 0–20 |
| Monatlich | Sichtprüfung Schläuche auf Leckage | 15 min | 0 |
| Quartalsweise | Fittings auf Korrosion prüfen | 20 min | 0 |
| Quartalsweise | Biegeradien und Scheuerstellen kontrollieren | 15 min | 0 |
| Halbjährlich | Fluidfarbe und -geruch beurteilen | 5 min | 0 |
| Halbjährlich | Steuerungsfunktionstest (Anschlag ↔ Anschlag) | 10 min | 0 |
| Jährlich | Vollständige Sichtinspektion aller Schläuche | 60 min | 80–150 |
| Jährlich | Druckprüfung (1.5× Arbeitsdruck, 5 min) | 30 min | 100–200 |
| Jährlich | Ölfilter wechseln | 30 min | 30–80 |
| Jährlich | Notsteuerung testen | 15 min | 0 |
| 2 Jahre | Hydraulikfluid-Wechsel + Analyse | 120 min | 150–400 |
| 2 Jahre | O-Ringe an Fittings inspizieren/erneuern | 60 min | 50–150 |
| 6 Jahre | **Kompletter Schlauchwechsel (DNV-GL)** | 4–8 h | 800–2.500 |

**Jährliche Gesamtkosten (Wartung ohne Schlauchwechsel):** 260–830 EUR
**6-Jahres-Zyklus-Kosten:** 2.360–7.480 EUR

### Wartungsplan: Hydraulik Stabilisatoren

| Intervall | Tätigkeit | Dauer | Kosten (EUR) |
|-----------|----------|-------|-------------|
| Monatlich | Fluidstand Stabilisator-HPU prüfen | 5 min | 0 |
| Quartalsweise | Sichtprüfung Schläuche + Aktuatoren | 30 min | 0 |
| Halbjährlich | Ölprobennahme → Partikelzählung | 15 min | 80–120 |
| Jährlich | Vollinspektion, Druckprüfung | 2 h | 200–400 |
| Jährlich | Filter wechseln (Druck + Rücklauf) | 45 min | 80–200 |
| 2 Jahre | Komplett-Ölwechsel | 3 h | 400–1.200 |
| 5 Jahre | Aktuator-Dichtungen erneuern | 8 h | 1.500–4.000 |
| 6 Jahre | Schlauchwechsel komplett | 6 h | 1.200–3.500 |

### Wartungsplan: Hydraulische Winschen

| Intervall | Tätigkeit | Dauer | Kosten (EUR) |
|-----------|----------|-------|-------------|
| Monatlich | Fluidstand HPU prüfen | 5 min | 0 |
| Saisonstart | Funktionstest aller Winschen | 30 min | 0 |
| Saisonende | Schläuche auf Deck inspizieren (UV, Scheuern) | 45 min | 0 |
| Jährlich | Vollinspektion, Leckageprüfung | 2 h | 150–300 |
| Jährlich | Filter wechseln | 30 min | 50–120 |
| 2 Jahre | Ölwechsel HPU | 2 h | 200–500 |
| 8 Jahre | Schlauchwechsel (Deck + unter Deck) | 8–12 h | 2.000–5.000 |

---

## ANHANG R-8 — Ölanalyse-Interpretation

### Laborwerte und ihre Bedeutung

| Parameter | Methode | Grenzwert OK | Warnung | Kritisch | Maßnahme bei Überschreitung |
|-----------|---------|-------------|---------|----------|---------------------------|
| Wassergehalt (ppm) | Karl Fischer | <200 | 200–500 | >500 | Fluid wechseln, Leckquelle finden |
| Partikelzahl (ISO 4406) | Automatisch | 18/16/13 | 19/17/14 | >20/18/15 | Filter wechseln, Kontamination suchen |
| Säurezahl (mg KOH/g) | Titration | <1.0 | 1.0–2.0 | >2.0 | Fluid wechseln |
| Viskosität (mm²/s @ 40°C) | Kapillar | ±10% Nennwert | ±15% | >±20% | Fluid wechseln |
| Kupfer (ppm) | ICP-OES | <10 | 10–25 | >25 | Pumpenverschleiß prüfen |
| Eisen (ppm) | ICP-OES | <15 | 15–40 | >40 | Zylinder/Pumpe inspizieren |
| Silizium (ppm) | ICP-OES | <10 | 10–25 | >25 | Verschmutzungseintritt suchen |
| Chrom (ppm) | ICP-OES | <5 | 5–15 | >15 | Zylinderstangenverschleiß |
| Zinn (ppm) | ICP-OES | <5 | 5–15 | >15 | Lagerverschleiß |
| Oxidation (abs/cm) | FTIR | <15 | 15–25 | >25 | Fluid überaltert |

### Probenahme-Anleitung für Ölanalyse

**Benötigtes Material:**
- Saubere Probeflasche (PE, 100 ml), vom Labor gestellt
- Einweghandschuhe
- Sauberer Lappen
- Ölablassschlauch oder Probenahmeventil (Minimess-Anschluss)
- Beschriftungsetikett

**Durchführung:**
1. System auf Betriebstemperatur bringen (min. 10 min Betrieb bei Steuerung)
2. Probenahmestelle reinigen (Staub, Salz entfernen)
3. Erste 50 ml verwerfen (Spülprobe) — diese enthalten Ablagerungen der Entnahmestelle
4. 100 ml in saubere Probeflasche füllen
5. Flasche sofort verschließen (Luftfeuchtigkeit vermeiden)
6. Etikett beschriften: Yacht-Name, System, Fluid-Typ, Datum, Betriebsstunden, letzte Ölfüllung
7. Probe innerhalb 48 Stunden an Labor senden (nicht einfrieren)

**Probenahme-Punkte (bevorzugt):**
- Rücklaufleitung (vor Filter): Beste Probe, repräsentativ für Systemzustand
- Tank-Ablass: Nur wenn Rücklaufleitung nicht zugänglich — enthält Sediment vom Boden
- Druckleitung: Repräsentativ, aber Sicherheitsrisiko bei Entnahme unter Druck
- Minimess-Ventil: Ideale Lösung — definierter Probenahmepunkt, drucklos schaltbar

**Kosten für Minimess-Probenahmeventil:**
- Parker Minimess 1620-xx: 25–45 EUR
- Stauff Minimess SMA: 20–38 EUR
- Montage: T-Stück in Rücklaufleitung, 30 min

### Trendanalyse — Beispiel Ölzustand über Lebensdauer

| Betriebsjahr | Wasser (ppm) | Partikel (ISO) | Säurezahl | Eisen (ppm) | Bewertung |
|-------------|-------------|---------------|-----------|-------------|-----------|
| 0 (neu) | <50 | 16/14/11 | 0.3 | <2 | Ausgezeichnet |
| 1 | 80 | 17/15/12 | 0.5 | 5 | Gut |
| 2 | 120 | 18/16/13 | 0.8 | 10 | Akzeptabel |
| 3 | 180 | 18/16/13 | 1.2 | 12 | Wechsel empfohlen |
| 4 (ohne Wechsel) | 350 | 19/17/14 | 1.8 | 25 | **Warnung** |
| 5 (ohne Wechsel) | 600 | 20/18/15 | 2.5 | 45 | **Kritisch — sofort wechseln** |

**AYDI-Score-Mapping Ölzustand:**

| Ölzustand | AYDI Score | Aktion |
|-----------|-----------|--------|
| Ausgezeichnet (alle Werte OK) | 95–100 | Routineüberwachung |
| Gut (alle Werte innerhalb Grenzen) | 80–94 | Weiterhin jährliche Analyse |
| Akzeptabel (1–2 Werte Warnung) | 60–79 | Ölwechsel bei nächster Wartung |
| Warnung (≥3 Werte Warnung) | 40–59 | Ölwechsel innerhalb 3 Monate |
| Kritisch (≥1 Wert kritisch) | 0–39 | **Sofortiger Ölwechsel + Ursachenanalyse** |

### Partikelzählung nach ISO 4406:1999

**Messprinzip:** Automatische optische Partikelzählung (Laserblockierung)

**Codierung:** Drei Zahlen, z.B. "18/16/13"
- Erste Zahl: Partikel ≥4 µm pro ml
- Zweite Zahl: Partikel ≥6 µm pro ml
- Dritte Zahl: Partikel ≥14 µm pro ml

**Code-Tabelle (Auszug):**

| Code | Partikel/ml (Bereich) |
|------|----------------------|
| 10 | 5–10 |
| 12 | 20–40 |
| 14 | 80–160 |
| 16 | 320–640 |
| 18 | 1.300–2.500 |
| 20 | 5.000–10.000 |
| 22 | 20.000–40.000 |

**Empfohlene Reinheitsklassen Marine-Hydraulik:**

| System | Empfohlene Klasse | Filterfeinheit |
|--------|------------------|---------------|
| Ruderanlage (einfach) | 18/16/13 | 10 µm (β10 ≥ 200) |
| Ruderanlage (Servo) | 17/15/12 | 6 µm (β6 ≥ 200) |
| Stabilisatoren (Servo) | 16/14/11 | 5 µm (β5 ≥ 200) |
| Winschen | 18/16/13 | 10 µm |
| Bugstrahlruder | 19/17/14 | 25 µm |
| Trimmklappen | 20/18/15 | 25 µm |

### Empfohlene Labore für Marine-Ölanalyse

| Labor | Standort | Preis/Probe | Dauer | Kontakt |
|-------|----------|------------|-------|---------|
| OELCHECK GmbH | Brannenburg (DE) | 45–85 EUR | 3–5 Tage | oelcheck.de |
| SGS Deutschland | Hamburg | 65–120 EUR | 5–7 Tage | sgs.com |
| Bureau Veritas | Hamburg | 70–130 EUR | 5–7 Tage | bureauveritas.de |
| Spectro Scientific | (US/EU-Partner) | 50–100 EUR | 3–5 Tage | spectrosci.com |

---

*Ende der Wissensdatei 06.07 — Hydraulikschläuche (Ruder/Winschen/Stabilisatoren)*
*AYDI Knowledge Engineering | Version 2.1 | 2026-04-23*
