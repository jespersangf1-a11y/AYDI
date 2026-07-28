# backend/app/schemas/schemas.py
import math
from datetime import date, datetime
from enum import Enum
from typing import Annotated
from uuid import UUID

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)


def _endlich(wert: object) -> object:
    """Weist NaN, Infinity und -Infinity ab.

    Der json-Parser von Python nimmt diese drei Literale klaglos an — sie sind
    zwar kein gueltiges JSON, aber die Standardbibliothek erlaubt sie beim
    Lesen. Bei begrenzten Feldern faellt das nicht auf: jeder Vergleich mit NaN
    ist falsch, also schlaegt eine Schranke wie ``ge=0`` beilaeufig zu. Die
    Geometriefelder hatten keine Schranke, der Wert landete unveraendert in der
    JSON-Spalte — und beim Ausliefern schreibt Starlette mit
    ``allow_nan=False``, bricht also mit einem Serverfehler ab. Eine einzige so
    angelegte Zone machte damit die gesamte Layout-Liste des Projekts
    unlesbar.
    """
    if isinstance(wert, float) and (math.isnan(wert) or math.isinf(wert)):
        raise ValueError("Zahlenwert muss endlich sein (weder NaN noch Infinity)")
    return wert


# Vor der eigentlichen Zahlenpruefung, damit bei NaN diese Begruendung
# erscheint und nicht die einer Schranke ("darf hoechstens 50000 sein"), die
# den Leser in die falsche Richtung schickt.
EndlicheZahl = Annotated[float, BeforeValidator(_endlich)]

# Eine Koordinate in mm. Ohne obere Schranke, weil ein Nullpunkt frei gewaehlt
# werden darf — aber immer endlich.
Koordinate = EndlicheZahl


def _punkte_pruefen(punkte: list[list[float]], feldname: str) -> list[list[float]]:
    """Jeder Punkt muss genau zwei Koordinaten haben (x, y in mm)."""
    for nummer, punkt in enumerate(punkte, start=1):
        if len(punkt) != 2:
            raise ValueError(
                f"{feldname}: Punkt {nummer} hat {len(punkt)} Koordinaten, "
                "erwartet werden genau zwei (x, y in mm)"
            )
    return punkte


class BoatClass(str, Enum):
    small_sail = "small_sail"
    cruising_sail = "cruising_sail"
    racing_sail = "racing_sail"
    daysailer = "daysailer"
    motorsailer = "motorsailer"
    catamaran_sail = "catamaran_sail"
    catamaran_motor = "catamaran_motor"
    small_motor = "small_motor"
    large_motor = "large_motor"
    sport_cruiser = "sport_cruiser"
    trawler = "trawler"
    explorer = "explorer"
    superyacht = "superyacht"


class ProjectStatus(str, Enum):
    draft = "draft"
    active = "active"
    review = "review"
    archived = "archived"


# Zone / Passage data (JSON within Layout)
class ZoneData(BaseModel):
    """Eingabeform einer Zone. Wird beim Anlegen eines Layouts geprueft."""

    name: str = Field(..., min_length=1, max_length=100)
    zone_type: str = Field(..., min_length=1, max_length=50)
    polygon: list[list[Koordinate]]
    height_mm: EndlicheZahl | None = Field(None, ge=0, le=10000)
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: EndlicheZahl | None = Field(None, ge=0, le=360)
    properties: dict | None = None

    @field_validator("polygon")
    @classmethod
    def _polygon_pruefen(cls, wert: list[list[float]]) -> list[list[float]]:
        # Unter drei Punkten gibt es keine Flaeche. Die Auswertungsmodule
        # rechneten daraus stillschweigend 0 m² und meldeten anschliessend zu
        # kleine Zonen — der eigentliche Fehler lag aber schon in der Eingabe.
        if len(wert) < 3:
            raise ValueError(
                f"Ein Zonenpolygon braucht mindestens drei Punkte, angegeben sind {len(wert)}"
            )
        return _punkte_pruefen(wert, "polygon")


class PassageData(BaseModel):
    """Eingabeform eines Durchgangs zwischen zwei Zonen."""

    from_zone: str = Field(..., min_length=1, max_length=100)
    to_zone: str = Field(..., min_length=1, max_length=100)
    width_mm: EndlicheZahl = Field(..., gt=0, le=50000, description="Durchgangsbreite in mm")
    length_mm: EndlicheZahl | None = Field(None, gt=0, le=100000)
    points: list[list[Koordinate]] | None = None
    is_primary: bool = True

    @field_validator("points")
    @classmethod
    def _punkte(cls, wert: list[list[float]] | None) -> list[list[float]] | None:
        if wert is None:
            return None
        if len(wert) < 2:
            raise ValueError(
                f"Ein Durchgangsverlauf braucht mindestens zwei Punkte, angegeben sind {len(wert)}"
            )
        return _punkte_pruefen(wert, "points")


class ZoneOut(BaseModel):
    """Ausgabeform einer Zone — bewusst ohne die Pruefungen von ZoneData.

    Was einmal in der Datenbank steht, muss lesbar bleiben. Wuerde hier
    dieselbe Pruefung greifen, machte ein einziger Altbestand-Datensatz die
    Liste dauerhaft unerreichbar, statt sie nur einmal beim Anlegen
    abzuweisen. Fehlerhafte Geometrie aus der Zeit vor dieser Pruefung wird
    beim Start einmalig bereinigt (siehe db/schema_sync.py).
    """

    name: str
    zone_type: str
    polygon: list[list[float]] = []
    height_mm: float | None = None
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: float | None = None
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True)


class PassageOut(BaseModel):
    """Ausgabeform eines Durchgangs — siehe ZoneOut."""

    from_zone: str
    to_zone: str
    width_mm: float | None = None
    length_mm: float | None = None
    points: list[list[float]] | None = None
    is_primary: bool = True

    model_config = ConfigDict(from_attributes=True)


# Pydantic v2 validation schemas for zones and passages
class ZoneSchema(BaseModel):
    name: str
    zone_type: str
    area_m2: float | None = None
    polygon: list | None = None
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True)


class PassageSchema(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    type: str
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True)


# Project schemas
class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    boat_class: BoatClass
    length_m: EndlicheZahl = Field(..., gt=0, le=300, description="Bootslänge in Metern")
    beam_m: EndlicheZahl = Field(..., gt=0, le=50, description="Bootsbreite in Metern")


class ProjectUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    boat_class: BoatClass | None = None
    length_m: EndlicheZahl | None = Field(None, gt=0, le=300)
    beam_m: EndlicheZahl | None = Field(None, gt=0, le=50)
    status: ProjectStatus | None = None


class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    boat_class: BoatClass
    length_m: float
    beam_m: float
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Layout schemas
class LayoutCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    version: str = Field("v1.0", min_length=1, max_length=50)
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int = Field(2100, ge=500, le=10000)

    @model_validator(mode="after")
    def _bezuege_pruefen(self) -> "LayoutCreate":
        """Ein Durchgang darf nur Zonen dieses Layouts verbinden.

        Bisher wurden ``from_zone``/``to_zone`` ungeprueft uebernommen. Ein
        Tippfehler im Zonennamen fuehrte deshalb nicht zu einer Fehlermeldung,
        sondern zu einem Durchgang, den kein Modul findet: die Ergonomie sah
        eine unerreichbare Kabine, die Fluchtwegpruefung meldete einen zu
        langen Weg. Der Befund landete beim Layout, die Ursache lag in der
        Eingabe.
        """
        namen = [z.name for z in self.zones]
        mehrfach = sorted({n for n in namen if namen.count(n) > 1})
        if mehrfach:
            raise ValueError(
                "Zonennamen muessen eindeutig sein, mehrfach vergeben: "
                + ", ".join(mehrfach)
            )

        bekannt = set(namen)
        for nummer, durchgang in enumerate(self.passages, start=1):
            for feld, wert in (
                ("from_zone", durchgang.from_zone),
                ("to_zone", durchgang.to_zone),
            ):
                if wert not in bekannt:
                    verfuegbar = ", ".join(sorted(bekannt)) or "keine"
                    raise ValueError(
                        f"Durchgang {nummer}: '{wert}' ({feld}) ist keine Zone "
                        f"dieses Layouts. Vorhanden: {verfuegbar}"
                    )
        return self


class LayoutResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    version: str
    file_path: str | None
    file_type: str | None
    zones: list[ZoneOut]
    passages: list[PassageOut]
    deck_height_mm: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Analysis schemas
class AnalysisRequest(BaseModel):
    layout_id: UUID
    module: str
    config_overrides: dict | None = None


class FullAnalysisRequest(BaseModel):
    """Request body for running all analysis modules on a layout."""
    layout_id: UUID
    config_overrides: dict | None = None


class WarningData(BaseModel):
    code: str | None = None
    severity: str
    message: str
    location: str | None = None
    value: float | None = None
    threshold: float | None = None
    suggestion: str
    norm: str | None = None


class AnalysisResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    module: str
    overall_score: float
    sub_scores: dict[str, float]
    warnings: list[WarningData]
    suggestions: list[str]
    metrics: dict
    config_used: dict
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# DXF Import
class DxfImportResponse(BaseModel):
    zones: list[ZoneData]
    passages: list[PassageData]
    warnings: list[str]


# Report schemas
class ReportRequest(BaseModel):
    layout_id: UUID
    report_type: str = "full"  # full, summary, executive


class ReportResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    report_type: str
    report_data: dict
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# CAD Import (STEP/IGES)
class DeckInfo(BaseModel):
    z_mm: float
    name: str
    face_count: int = 0


class CadImportResponse(BaseModel):
    zones: list[ZoneData]
    passages: list[PassageData]
    warnings: list[str]
    decks: list[DeckInfo] = []


# Error
class ErrorResponse(BaseModel):
    detail: str
    errors: list[str] | None = None


# Community Intelligence schemas
class CommunityIssue(BaseModel):
    category: str
    zone_type: str
    description: str
    severity: str
    boat_age_months: int | None = None


class CommunityPositive(BaseModel):
    category: str
    zone_type: str
    description: str


class CommunityReportCreate(BaseModel):
    source_forum: str = Field(..., min_length=1, max_length=100)
    source_url: str | None = Field(None, max_length=2000)
    source_date: date | None = None
    boat_manufacturer: str = Field(..., min_length=1, max_length=200)
    boat_model: str | None = Field(None, max_length=200)
    boat_year: int | None = Field(None, ge=1900, le=2100)
    hull_material: str | None = Field(None, max_length=100)
    hull_construction: str | None = Field(None, max_length=100)
    propulsion: str | None = Field(None, max_length=100)
    issues: list[CommunityIssue] = []
    positives: list[CommunityPositive] = []
    reliability: float = Field(..., ge=0.0, le=1.0)
    raw_text: str | None = Field(None, max_length=50000)


class CommunityReportResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    source_forum: str
    source_url: str | None = None
    source_date: date | None = None
    boat_manufacturer: str
    boat_model: str | None = None
    boat_year: int | None = None
    hull_material: str | None = None
    hull_construction: str | None = None
    propulsion: str | None = None
    issues: list[dict] = []
    positives: list[dict] = []
    reliability: float
    raw_text: str | None = None
    model_config = ConfigDict(from_attributes=True)


class CommunityPatternResponse(BaseModel):
    id: int
    created_at: datetime
    manufacturer: str | None = None
    boat_model: str | None = None
    issue_category: str
    zone_type: str | None = None
    description: str
    report_count: int
    severity_mode: str
    typical_onset_years: float | None = None
    materials_involved: list[str] | None = None
    construction_methods_involved: list[str] | None = None
    confidence: float
    source_report_ids: list[int]
    is_positive: bool
    model_config = ConfigDict(from_attributes=True)


class AggregationResultResponse(BaseModel):
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int
