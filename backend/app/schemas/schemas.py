# backend/app/schemas/schemas.py
import math
from datetime import date, datetime
from enum import Enum
from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)

# ---------------------------------------------------------------------------
# Schranken für Layout-Geometrie (ROB-1, SEC-9)
#
# Warum an der Schema-Grenze: `app/core/validation.py` prüft erst beim Eintritt
# in ein Analysemodul auf Endlichkeit. Ein Layout mit NaN-Koordinaten wird davor
# aber schon per POST angelegt (201) und liegt dann dauerhaft in der DB — jede
# spätere Analyse und jede Response-Serialisierung (JSON kennt kein NaN) läuft
# darauf in einen 500er. Der Schutz gehört deshalb an die Schema-Grenze.
#
# Die Werte sind bewusst großzügig: ein 180-m-Superyacht-Deck misst rund
# 180.000 mm, alle Grenzen liegen um Größenordnungen darüber. Sie sollen
# Unsinn und Missbrauch abfangen, nicht legitime Entwürfe.
# ---------------------------------------------------------------------------

MAX_COORD_MM = 1_000_000.0        # 1 km — jede reale Yacht liegt weit darunter
MAX_POLYGON_POINTS = 5_000        # feinaufgelöste CAD-Kontur bleibt möglich
MAX_ZONES_PER_LAYOUT = 500        # Superyacht-Layouts liegen bei ~100-200 Zonen
MAX_PASSAGES_PER_LAYOUT = 2_000
MAX_PROPERTY_KEYS = 200
MAX_PASSAGE_WIDTH_MM = 100_000.0  # 100 m
MAX_PASSAGE_LENGTH_MM = 1_000_000.0
MAX_ZONE_AREA_M2 = 100_000.0


NON_FINITE_SENTINEL = "__nicht_endliche_zahl__"


def _sanitize_non_finite(value: Any, _depth: int = 0) -> Any:
    """Ersetzt NaN/Infinity im ROHEN Request-Body durch einen Marker-String.

    Grund: FastAPIs 422-Antwort spiegelt den Eingabewert zurück
    (``detail[].input``). Ein rohes NaN darin ist selbst nicht
    JSON-serialisierbar — die Fehlerantwort scheitert dann und der Client
    bekommt 500 statt 422. Der Marker ist serialisierbar; die Feld-Validatoren
    übersetzen ihn unten in eine deutsche Meldung.
    """
    if _depth > 12:
        return value
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, float):
        return NON_FINITE_SENTINEL if not math.isfinite(value) else value
    if isinstance(value, list):
        return [_sanitize_non_finite(item, _depth + 1) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize_non_finite(item, _depth + 1) for item in value)
    if isinstance(value, dict):
        return {key: _sanitize_non_finite(item, _depth + 1) for key, item in value.items()}
    return value


class FiniteNumbersMixin(BaseModel):
    """Entschärft NaN/Infinity, bevor Pydantic sie in die Fehlerantwort schreibt."""

    @model_validator(mode="before")
    @classmethod
    def _sanitize_payload(cls, data):
        if isinstance(data, dict):
            return _sanitize_non_finite(data)
        return data


def require_finite(value: Any, feld: str) -> Any:
    """Weist NaN/Infinity mit deutscher Meldung ab; alles andere passiert unverändert.

    Läuft als ``mode="before"``-Validator, damit die deutsche Meldung vor den
    generischen ge/le-Meldungen von Pydantic greift.
    """
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float)):
        if not math.isfinite(float(value)):
            raise ValueError(
                f"{feld}: Nur endliche Zahlenwerte sind zulässig "
                f"(NaN und Infinity werden abgelehnt)."
            )
    elif value == NON_FINITE_SENTINEL:
        raise ValueError(
            f"{feld}: Nur endliche Zahlenwerte sind zulässig "
            f"(NaN und Infinity werden abgelehnt)."
        )
    elif isinstance(value, str):
        # Pydantic würde "NaN"/"Infinity" als String noch in float wandeln.
        try:
            parsed = float(value)
        except (TypeError, ValueError):
            return value
        if not math.isfinite(parsed):
            raise ValueError(
                f"{feld}: Nur endliche Zahlenwerte sind zulässig "
                f"(NaN und Infinity werden abgelehnt)."
            )
    return value


def _check_point_list(value: Any, feld: str, max_points: int) -> Any:
    """Prüft eine Punktliste ([[x, y], ...]) auf Länge, Stelligkeit und Endlichkeit."""
    if not isinstance(value, list):
        return value
    if len(value) > max_points:
        raise ValueError(
            f"{feld}: Maximal {max_points} Punkte je Kontur "
            f"({len(value)} übergeben)."
        )
    for point in value:
        if not isinstance(point, list):
            continue
        if len(point) < 2 or len(point) > 3:
            raise ValueError(
                f"{feld}: Jeder Punkt braucht 2 oder 3 Koordinaten "
                f"(gefunden: {len(point)})."
            )
        for coord in point:
            require_finite(coord, feld)
    return value


def _check_properties(value: Any, feld: str, _depth: int = 0) -> Any:
    """Begrenzt die Größe eines frei befüllbaren properties-Dicts (SEC-9)
    und weist NaN/Infinity darin ab (ROB-1) — auch verschachtelt.

    Das properties-Dict ist der einzige unstrukturierte Kanal in die Module
    (z.B. ``sill_height_mm`` der CE-Süllprüfung). Ohne Prüfung wandert ein NaN
    von hier ungehindert in eine Berechnung.
    """
    if _depth > 6:
        return value
    if isinstance(value, list):
        if len(value) > MAX_PROPERTY_KEYS:
            raise ValueError(
                f"{feld}: Maximal {MAX_PROPERTY_KEYS} Einträge je Eigenschaft "
                f"({len(value)} übergeben)."
            )
        for entry in value:
            _check_properties(entry, feld, _depth + 1)
        return value
    if not isinstance(value, dict):
        return require_finite(value, feld)
    if len(value) > MAX_PROPERTY_KEYS:
        raise ValueError(
            f"{feld}: Maximal {MAX_PROPERTY_KEYS} Eigenschaften je Element "
            f"({len(value)} übergeben)."
        )
    for key, entry in value.items():
        _check_properties(entry, f"{feld}.{key}", _depth + 1)
    return value


# Eine Zahl, die endlich sein muss, aber keine Koordinate ist (Laenge, Breite,
# Sichtwinkel ...). Die Pruefung laeuft VOR den Schranken, damit bei NaN die
# verstaendliche Begruendung erscheint und nicht die einer Schranke, die den
# Leser in die falsche Richtung schickt.
EndlicheZahl = Annotated[float, BeforeValidator(lambda v: require_finite(v, "Zahlenwert"))]

Coordinate = Annotated[float, Field(ge=-MAX_COORD_MM, le=MAX_COORD_MM)]
PolygonPoint = Annotated[list[Coordinate], Field(min_length=2, max_length=3)]


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
class ZoneData(FiniteNumbersMixin):
    """Eingabeform einer Zone. Wird beim Anlegen eines Layouts geprueft."""

    # allow_inf_nan=False ist der maschinelle Riegel gegen NaN/Infinity; die
    # Validatoren darunter liefern zusätzlich die deutsche Fehlermeldung (ROB-1).
    model_config = ConfigDict(allow_inf_nan=False)

    name: str = Field(..., min_length=1, max_length=100)
    zone_type: str = Field(..., min_length=1, max_length=50)
    polygon: list[PolygonPoint] = Field(..., max_length=MAX_POLYGON_POINTS)
    height_mm: float | None = Field(None, ge=0, le=10000)
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: EndlicheZahl | None = Field(None, ge=0, le=360)
    properties: dict | None = None

    @field_validator("polygon", mode="before")
    @classmethod
    def _validate_polygon(cls, value):
        # Unter drei Punkten gibt es keine Flaeche. Die Auswertungsmodule
        # rechneten daraus stillschweigend 0 m² und meldeten anschliessend zu
        # kleine Zonen — der eigentliche Fehler lag aber schon in der Eingabe.
        if isinstance(value, list) and len(value) < 3:
            raise ValueError(
                f"Ein Zonenpolygon braucht mindestens drei Punkte, "
                f"angegeben sind {len(value)}"
            )
        return _check_point_list(value, "polygon", MAX_POLYGON_POINTS)

    @field_validator("height_mm", "visibility_angle", mode="before")
    @classmethod
    def _validate_zone_numbers(cls, value, info):
        return require_finite(value, info.field_name)

    @field_validator("properties", mode="before")
    @classmethod
    def _validate_zone_properties(cls, value):
        return _check_properties(value, "properties")


class PassageData(FiniteNumbersMixin):
    model_config = ConfigDict(allow_inf_nan=False)

    from_zone: str = Field(..., min_length=1, max_length=100)
    to_zone: str = Field(..., min_length=1, max_length=100)
    # Optional, weil ein aus DXF importierter Durchgang KEINE ableitbare Breite
    # hat (siehe services/dxf/parser.py::_detect_shared_edges). Dort stand
    # frueher ersatzweise eine erfundene 100 — die Ergonomie meldete daraufhin
    # jeden importierten Durchgang als "kritisch schmal" mit Konfidenz
    # "measured". None heisst hier ausdruecklich "nicht bekannt", nicht 0.
    width_mm: float | None = Field(None, ge=0, le=MAX_PASSAGE_WIDTH_MM)
    length_mm: float | None = Field(None, ge=0, le=MAX_PASSAGE_LENGTH_MM)
    points: list[PolygonPoint] | None = Field(None, max_length=MAX_POLYGON_POINTS)
    is_primary: bool = True
    # Passage-level attributes (e.g. sill_height_mm for the CE companionway-sill
    # check). Without this, Pydantic silently dropped the field and
    # CE_NO_SILL_DATA fired permanently — the check was unreachable via the API.
    properties: dict | None = None

    @field_validator("width_mm", "length_mm", mode="before")
    @classmethod
    def _validate_passage_numbers(cls, value, info):
        return require_finite(value, info.field_name)

    @field_validator("points", mode="before")
    @classmethod
    def _validate_points(cls, value):
        if isinstance(value, list) and len(value) < 2:
            raise ValueError(
                f"Ein Durchgangsverlauf braucht mindestens zwei Punkte, "
                f"angegeben sind {len(value)}"
            )
        return _check_point_list(value, "points", MAX_POLYGON_POINTS)

    @field_validator("properties", mode="before")
    @classmethod
    def _validate_passage_properties(cls, value):
        return _check_properties(value, "properties")

    model_config = ConfigDict(from_attributes=True)


# Pydantic v2 validation schemas for zones and passages
class ZoneSchema(FiniteNumbersMixin):
    name: str
    zone_type: str
    area_m2: float | None = Field(None, ge=0, le=MAX_ZONE_AREA_M2)
    polygon: list | None = Field(None, max_length=MAX_POLYGON_POINTS)
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True, allow_inf_nan=False)

    @field_validator("area_m2", mode="before")
    @classmethod
    def _validate_area(cls, value, info):
        return require_finite(value, info.field_name)

    @field_validator("polygon", mode="before")
    @classmethod
    def _validate_polygon(cls, value):
        return _check_point_list(value, "polygon", MAX_POLYGON_POINTS)

    @field_validator("properties", mode="before")
    @classmethod
    def _validate_properties(cls, value):
        return _check_properties(value, "properties")


class PassageSchema(FiniteNumbersMixin):
    from_zone: str
    to_zone: str
    # Optional, weil ein aus DXF importierter Durchgang KEINE ableitbare Breite
    # hat (siehe services/dxf/parser.py::_detect_shared_edges). Dort stand
    # frueher ersatzweise eine erfundene 100 — die Ergonomie meldete daraufhin
    # jeden importierten Durchgang als "kritisch schmal" mit Konfidenz
    # "measured". None heisst hier ausdruecklich "nicht bekannt", nicht 0.
    width_mm: float | None = Field(None, ge=0, le=MAX_PASSAGE_WIDTH_MM)
    type: str
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True, allow_inf_nan=False)

    @field_validator("width_mm", mode="before")
    @classmethod
    def _validate_width(cls, value, info):
        return require_finite(value, info.field_name)

    @field_validator("properties", mode="before")
    @classmethod
    def _validate_properties(cls, value):
        return _check_properties(value, "properties")


# Project schemas
class ProjectCreate(FiniteNumbersMixin):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    boat_class: BoatClass
    length_m: EndlicheZahl = Field(..., gt=0, le=300, description="Bootslänge in Metern")
    beam_m: EndlicheZahl = Field(..., gt=0, le=50, description="Bootsbreite in Metern")


class ProjectUpdate(FiniteNumbersMixin):
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
    # Organization ownership (pillar 4, stage 2), None for private projects.
    org_id: UUID | None = None
    # Caller's relationship to the project: "owner" / "editor" / "viewer".
    # Drives the "geteilt"-badge and owner-only UI (sharing dialog).
    access_role: str | None = None

    model_config = ConfigDict(from_attributes=True)


# Project sharing (pillar 4, stage 1)
class ProjectMemberCreate(BaseModel):
    email: EmailStr
    role: Literal["viewer", "editor"] = "viewer"


class ProjectMemberRoleUpdate(BaseModel):
    role: Literal["viewer", "editor"]


class ProjectMemberResponse(BaseModel):
    user_id: UUID
    email: str
    full_name: str
    role: str  # owner, editor, viewer

    model_config = ConfigDict(from_attributes=True)


# Project org attachment (pillar 4, stage 2)
class ProjectOrgUpdate(BaseModel):
    # None = detach the project back to private
    org_id: UUID | None = None


# ---------------------------------------------------------------------------
# Organizations (pillar 4, stage 2)
# ---------------------------------------------------------------------------

class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)


class OrganizationUpdate(BaseModel):
    # Rename only. tier is deliberately NOT here — it is platform-admin-only
    # (self-service tier changes would be a privilege escalation).
    name: str = Field(..., min_length=1, max_length=200)


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    tier: str
    created_at: datetime
    # Caller's org_role ("owner"/"admin"/"member") — for UI gating.
    org_role: str | None = None
    member_count: int | None = None

    model_config = ConfigDict(from_attributes=True)


class OrgMemberResponse(BaseModel):
    user_id: UUID
    email: str
    full_name: str
    org_role: str  # owner, admin, member

    model_config = ConfigDict(from_attributes=True)


class OrgMemberRoleUpdate(BaseModel):
    org_role: Literal["owner", "admin", "member"]


class OrgTierUpdate(BaseModel):
    # Platform-admin-only endpoint payload.
    tier: Literal["free", "pro", "enterprise"]


# ---------------------------------------------------------------------------
# Invitations (pillar 4, stage 2)
# ---------------------------------------------------------------------------

class ProjectInvitationCreate(BaseModel):
    email: EmailStr
    role: Literal["viewer", "editor"] = "viewer"


class OrgInvitationCreate(BaseModel):
    email: EmailStr
    role: Literal["member", "admin"] = "member"


class InvitationResponse(BaseModel):
    id: UUID
    email: str
    role: str
    status: str
    scope: str  # "project" | "org"
    project_id: UUID | None = None
    organization_id: UUID | None = None
    # Human-readable target name, filled by the endpoint (project/org name).
    target_name: str | None = None
    invited_by_email: str | None = None
    created_at: datetime
    expires_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Layout schemas
class LayoutCreate(FiniteNumbersMixin):
    name: str = Field(..., min_length=1, max_length=200)
    version: str = Field("v1.0", min_length=1, max_length=50)
    # SEC-9: Ohne Obergrenze kann ein einziger Request beliebig viele Zonen
    # einliefern; jede Folgeanalyse ist quadratisch in der Zonenzahl.
    zones: list[ZoneData] = Field(..., max_length=MAX_ZONES_PER_LAYOUT)
    passages: list[PassageData] = Field(..., max_length=MAX_PASSAGES_PER_LAYOUT)
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



class LayoutUpdate(FiniteNumbersMixin):
    """Partial layout update (pillar 3: owner refit loop).

    Every applied update auto-snapshots the PREVIOUS state as a LayoutVersion,
    so edits are never destructive and before/after comparison always works.
    """
    name: str | None = Field(None, min_length=1, max_length=200)
    version: str | None = Field(None, min_length=1, max_length=50)
    # min_length=1: emptying a layout is not a refit operation — a bare
    # zones=[] would only ever appear by accident (e.g. missing snapshot)
    # and every following analysis would fail on empty geometry.
    zones: list[ZoneData] | None = Field(
        None, min_length=1, max_length=MAX_ZONES_PER_LAYOUT
    )
    passages: list[PassageData] | None = Field(
        None, max_length=MAX_PASSAGES_PER_LAYOUT
    )
    deck_height_mm: int | None = Field(None, ge=1000, le=5000)
    # Zone renames performed in this update ({old_name: new_name}) — the
    # server cascades them to ZoneMaterial/StructuralItem/CostItem rows,
    # which reference zones BY NAME and would otherwise be orphaned.
    zone_renames: dict[str, str] | None = Field(
        None, max_length=MAX_ZONES_PER_LAYOUT
    )
    # Recorded on the auto-created version snapshot
    change_summary: str | None = Field(None, max_length=500)


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
    # Optional: not every finding carries a suggestion, and requiring a string
    # here made GET /analyses raise ResponseValidationError (500) on any stored
    # warning with suggestion=None.
    suggestion: str | None = None
    # Per-finding confidence badge propagated by the orchestrator (M-1).
    confidence: str | None = None
    norm: str | None = None


class AnalysisResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    run_id: UUID | None = None
    module: str
    overall_score: float
    # Eine Teilanalyse ohne Datengrundlage traegt None (siehe
    # services/analysis/scoring.py). Ohne das Optional scheitert die
    # Antwort an der eigenen Ausgabepruefung, sobald ein Modul ehrlich
    # "nicht bewertbar" sagt.
    sub_scores: dict[str, float | None]
    warnings: list[WarningData]
    suggestions: list[str]
    metrics: dict
    config_used: dict
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AnalysisRunResponse(BaseModel):
    """Header of one full-analysis run (H-3)."""
    id: UUID
    project_id: UUID
    layout_id: UUID
    overall_score: float | None
    overall_confidence: str | None
    module_count: int
    skipped_count: int
    error_count: int
    tier: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AnalysisUnavailableResponse(BaseModel):
    """Antwort, wenn ein Modul mangels Datengrundlage nicht urteilen kann.

    Bewusst eine eigene Form ohne ``overall_score``: ein Modul ohne Daten hat
    keinen Wert, und ein Platzhalter waere in der Oberflaeche nicht von einem
    gemessenen zu unterscheiden. Es wird auch nichts gespeichert — ein solcher
    Lauf ist kein Befund, der im Verlauf des Projekts stehen sollte.
    """

    module: str
    available: bool = False
    reason: str
    suggestions: list[str] = []


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


class CommunityReportCreate(FiniteNumbersMixin):
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
