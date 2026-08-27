"""Schranken an der Schema-Grenze (ROB-1, ROB-2, ROB-3, SEC-9).

Warum an dieser Stelle geprueft wird:

``app/core/validation.py`` prueft erst beim EINTRITT in ein Analysemodul auf
Endlichkeit. Ein Layout mit NaN-Koordinate wird davor aber schon per POST
angelegt (201) und liegt dauerhaft in der DB — jede spaetere Analyse und jede
Response-Serialisierung (JSON kennt kein NaN) laeuft dann in einen 500er. Die
Schnellanalyse ist zusaetzlich UNAUTHENTIFIZIERT: unbegrenzte Zaehler wie
``cabin_count`` erzeugen je eine Zone, und die Ergonomie-Analyse ist quadratisch
in der Zonenzahl (gemessen: 5.000 Kabinen = 75 s in EINEM Modul).

Die Grenzen sind bewusst grosszuegig: die Gegenproben unten stellen sicher, dass
ein 180-m-Superyacht-Entwurf mit 40 Kabinen und feinaufgeloesten CAD-Konturen
weiterhin akzeptiert wird.
"""

import asyncio
import json

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.main import app
from app.models.models import Base, Project, User
from app.schemas.quick_analysis import PublicSpecs
from app.schemas.schemas import (
    MAX_PASSAGES_PER_LAYOUT,
    MAX_POLYGON_POINTS,
    MAX_ZONES_PER_LAYOUT,
    LayoutCreate,
    LayoutUpdate,
    PassageData,
    ZoneData,
)

TRIANGLE = [[0, 0], [1000, 0], [1000, 1000]]
MINI_ZONE = {"name": "Z", "zone_type": "cabin", "polygon": TRIANGLE}
MINI_PASSAGE = {"from_zone": "a", "to_zone": "b", "width_mm": 700}


# ---------------------------------------------------------------------------
# ROB-1 — NaN/Infinity in der Layout-Geometrie
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("bad", [float("nan"), float("inf"), float("-inf")])
def test_zone_polygon_rejects_non_finite_coordinates(bad):
    with pytest.raises(ValidationError) as exc:
        ZoneData(name="Kabine", zone_type="cabin", polygon=[[bad, 0], [1, 0], [1, 1]])
    assert "endliche Zahlenwerte" in str(exc.value)


def test_layout_create_rejects_raw_json_nan_literal():
    """Der Weg aus dem Audit: rohes JSON-Literal ``NaN`` im Polygon.

    ``json.loads`` erzeugt daraus float('nan') — genau so kommt es durch
    FastAPI im Request-Body an.
    """
    raw = (
        '{"name":"Deck","version":"v1.0","zones":[{"name":"K","zone_type":"cabin",'
        '"polygon":[[NaN,0],[1000,0],[1000,1000]]}],"passages":[],'
        '"deck_height_mm":2100}'
    )
    with pytest.raises(ValidationError) as exc:
        LayoutCreate.model_validate(json.loads(raw))
    assert "endliche Zahlenwerte" in str(exc.value)


def test_zone_polygon_rejects_absurd_coordinate_magnitude():
    with pytest.raises(ValidationError):
        ZoneData(name="K", zone_type="cabin", polygon=[[1e30, 0], [1, 0], [1, 1]])


def test_zone_polygon_rejects_malformed_point():
    with pytest.raises(ValidationError) as exc:
        ZoneData(name="K", zone_type="cabin", polygon=[[0], [1, 0], [1, 1]])
    assert "Koordinaten" in str(exc.value)


@pytest.mark.parametrize("field", ["height_mm", "visibility_angle"])
def test_zone_scalar_fields_reject_nan(field):
    with pytest.raises(ValidationError) as exc:
        ZoneData(name="K", zone_type="cabin", polygon=TRIANGLE, **{field: float("nan")})
    assert "endliche Zahlenwerte" in str(exc.value)


def test_passage_width_rejects_nan_and_negative():
    with pytest.raises(ValidationError) as exc:
        PassageData(from_zone="a", to_zone="b", width_mm=float("nan"))
    assert "endliche Zahlenwerte" in str(exc.value)
    with pytest.raises(ValidationError):
        PassageData(from_zone="a", to_zone="b", width_mm=-500)


def test_passage_points_reject_non_finite():
    with pytest.raises(ValidationError) as exc:
        PassageData(
            from_zone="a", to_zone="b", width_mm=700,
            points=[[0, 0], [float("inf"), 0]],
        )
    assert "endliche Zahlenwerte" in str(exc.value)


def test_properties_dict_rejects_non_finite_value():
    """NaN versteckt sich sonst im freien properties-Dict und wandert von dort
    ungeprueft in die Module (z.B. sill_height_mm der CE-Suellpruefung)."""
    with pytest.raises(ValidationError) as exc:
        PassageData(
            from_zone="a", to_zone="b", width_mm=700,
            properties={"sill_height_mm": float("nan")},
        )
    assert "endliche Zahlenwerte" in str(exc.value)


# ---------------------------------------------------------------------------
# ROB-2 — NaN in der unauthentifizierten Schnellanalyse
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "field",
    [
        "draft_m", "displacement_kg", "cockpit_area_sqm", "salon_area_sqm",
        "engine_hp", "fuel_capacity_l", "water_capacity_l", "sail_area_sqm",
        "max_speed_kn", "price_eur", "deck_height_mm", "storage_volume_l",
    ],
)
@pytest.mark.parametrize("bad", [float("nan"), float("inf")])
def test_public_specs_reject_non_finite(field, bad):
    with pytest.raises(ValidationError) as exc:
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, **{field: bad})
    assert "endliche Zahlenwerte" in str(exc.value)


def test_public_specs_reject_non_finite_string_form():
    """"NaN" als String wuerde Pydantic sonst noch in float('nan') wandeln."""
    with pytest.raises(ValidationError) as exc:
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, draft_m="NaN")
    assert "endliche Zahlenwerte" in str(exc.value)


def test_public_specs_reject_negative_measures():
    with pytest.raises(ValidationError):
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, deck_height_mm=-1e9)
    with pytest.raises(ValidationError):
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, price_eur=-1.0)


# ---------------------------------------------------------------------------
# ROB-3 — unbegrenzte Zaehler blockieren den Event-Loop
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("field", ["cabin_count", "head_count", "berth_count", "engine_count"])
def test_public_specs_counts_are_bounded(field):
    with pytest.raises(ValidationError):
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, **{field: 500_000})
    with pytest.raises(ValidationError):
        PublicSpecs(boat_class="cruising_sail", length_m=12.0, **{field: -5})


def test_bounded_cabin_count_keeps_estimation_fast():
    """Die Obergrenze muss die Laufzeit tatsaechlich kappen, nicht nur die Zahl."""
    from app.services.analysis.ergonomics import run_ergonomics_analysis
    from app.services.inference.layout_estimator import estimate_layout_from_specs

    specs = PublicSpecs(
        boat_class="superyacht", length_m=180.0, cabin_count=100, head_count=100
    )
    estimated = estimate_layout_from_specs(
        boat_class=specs.boat_class, length_m=specs.length_m,
        cabin_count=specs.cabin_count, head_count=specs.head_count,
    )
    # Der Schaetzer erzeugt je Kabine/Nasszelle eine Zone — mit der Schranke
    # bleibt das im dreistelligen Bereich statt im sechsstelligen.
    assert len(estimated["zones"]) < 400
    run_ergonomics_analysis(
        estimated["zones"], estimated["passages"], "superyacht",
        data_source="estimated",
    )


# ---------------------------------------------------------------------------
# SEC-9 — Element-Limits fuer Listen und Dicts
# ---------------------------------------------------------------------------

def test_layout_create_bounds_zone_count():
    with pytest.raises(ValidationError):
        LayoutCreate(name="x", zones=[MINI_ZONE] * (MAX_ZONES_PER_LAYOUT + 1), passages=[])


def test_layout_create_bounds_passage_count():
    with pytest.raises(ValidationError):
        LayoutCreate(
            name="x", zones=[MINI_ZONE],
            passages=[MINI_PASSAGE] * (MAX_PASSAGES_PER_LAYOUT + 1),
        )


def test_layout_update_bounds_zone_count():
    with pytest.raises(ValidationError):
        LayoutUpdate(zones=[MINI_ZONE] * (MAX_ZONES_PER_LAYOUT + 1))


def test_polygon_point_count_is_bounded():
    with pytest.raises(ValidationError) as exc:
        ZoneData(name="K", zone_type="cabin", polygon=[[0, 0]] * (MAX_POLYGON_POINTS + 1))
    assert "Punkte je Kontur" in str(exc.value)


def test_properties_key_count_is_bounded():
    with pytest.raises(ValidationError) as exc:
        ZoneData(
            name="K", zone_type="cabin", polygon=TRIANGLE,
            properties={str(i): i for i in range(100_000)},
        )
    assert "Eigenschaften je Element" in str(exc.value)


# ---------------------------------------------------------------------------
# Gegenproben — legitime Entwuerfe duerfen NICHT abgelehnt werden
# ---------------------------------------------------------------------------

def test_superyacht_specs_still_accepted():
    specs = PublicSpecs(
        boat_class="superyacht", length_m=180.0, beam_m=25.0, draft_m=5.5,
        displacement_kg=8_000_000, cabin_count=40, berth_count=90, head_count=12,
        engine_hp=15_000, engine_count=4, fuel_capacity_l=1_000_000,
        water_capacity_l=200_000, price_eur=250_000_000, max_speed_kn=22.0,
        deck_height_mm=2400, storage_volume_l=80_000, year=2024,
    )
    assert specs.cabin_count == 40
    assert specs.price_eur == 250_000_000


def test_large_but_realistic_layout_still_accepted():
    # Eindeutige Zonennamen, und jeder Durchgang verbindet Zonen dieses
    # Layouts: beides seit dem Zusammenfuehren Pflicht. Ein realistisches
    # Layout erfuellt es ohnehin — ZoneMaterial, StructuralItem und CostItem
    # verweisen auf Zonen ueber den NAMEN, doppelte Namen waeren dort nicht
    # aufloesbar.
    zonen = [
        {"name": f"Z{i}", "zone_type": "cabin", "polygon": TRIANGLE}
        for i in range(300)
    ]
    durchgaenge = [
        {"from_zone": f"Z{i % 300}", "to_zone": f"Z{(i + 1) % 300}", "width_mm": 700}
        for i in range(1500)
    ]
    layout = LayoutCreate(
        name="Superyacht Hauptdeck",
        zones=zonen,
        passages=durchgaenge,
        deck_height_mm=2400,
    )
    assert len(layout.zones) == 300
    assert len(layout.passages) == 1500


def test_fine_cad_contour_at_superyacht_coordinates_still_accepted():
    zone = ZoneData(
        name="Rumpf", zone_type="hull",
        polygon=[[180_000.0, -12_000.0]] * 4000,
    )
    assert len(zone.polygon) == 4000


def test_passage_sill_property_still_accepted():
    passage = PassageData(
        from_zone="Cockpit", to_zone="Salon", width_mm=700.0,
        properties={"sill_height_mm": 300},
    )
    assert passage.properties["sill_height_mm"] == 300


# ---------------------------------------------------------------------------
# HTTP-Ebene: die Schranken muessen 422 liefern, nicht 201/500
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def http(tmp_path_factory):
    """Isolierte DB + Dependency-Overrides (Muster aus test_layout_update_api)."""
    db_path = tmp_path_factory.mktemp("schema_bounds") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            owner = User(
                email="bounds-owner@test.example", hashed_password="x",
                full_name="Owner", role="user", tier="pro",
            )
            session.add(owner)
            await session.flush()
            project = Project(
                user_id=owner.id, name="Testboot", description="",
                boat_class="cruising_sail", length_m=11.0, beam_m=3.8,
                status="active",
            )
            session.add(project)
            await session.commit()
            return {"owner": owner.id, "project": project.id}

    ids = asyncio.run(_seed())

    async def override_get_db():
        async with session_factory() as session:
            yield session

    async def override_get_current_user():
        async with session_factory() as session:
            return await session.get(User, ids["owner"])

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user
    try:
        yield TestClient(app), ids
    finally:
        app.dependency_overrides.clear()


def test_post_layout_with_nan_coordinate_is_rejected_at_the_boundary(http):
    """Vor dem Fix: 201 — das NaN-Layout landete in der DB und jede Folge-
    analyse antwortete mit 500."""
    client, ids = http
    body = (
        '{"name":"Deck","version":"v1.0","zones":[{"name":"K","zone_type":"cabin",'
        '"polygon":[[NaN,0],[4000,0],[4000,3000]]}],'
        '"passages":[],"deck_height_mm":2100}'
    )
    res = client.post(
        f"/api/v1/projects/{ids['project']}/layouts",
        content=body,
        headers={"Content-Type": "application/json"},
    )
    assert res.status_code == 422, res.text
    assert "endliche Zahlenwerte" in res.text


def test_post_layout_with_excessive_zone_count_is_rejected(http):
    client, ids = http
    res = client.post(
        f"/api/v1/projects/{ids['project']}/layouts",
        json={
            "name": "Deck",
            "zones": [MINI_ZONE] * (MAX_ZONES_PER_LAYOUT + 1),
            "passages": [],
        },
    )
    assert res.status_code == 422, res.text


def test_quick_analysis_rejects_nan_and_huge_cabin_count(http):
    """Der unauthentifizierte Endpunkt — hier zaehlt jede Schranke doppelt."""
    client, _ = http
    res = client.post(
        "/api/v1/quick-analysis",
        content='{"boat_class":"cruising_sail","length_m":12.0,"draft_m":NaN}',
        headers={"Content-Type": "application/json"},
    )
    assert res.status_code == 422, res.text
    assert "endliche Zahlenwerte" in res.text

    res = client.post(
        "/api/v1/quick-analysis",
        json={"boat_class": "cruising_sail", "length_m": 12.0, "cabin_count": 500_000},
    )
    assert res.status_code == 422, res.text


def test_nested_properties_reject_non_finite():
    """properties ist der einzige unstrukturierte Kanal in die Module — ein NaN
    darf sich dort auch nicht eine Ebene tiefer verstecken."""
    with pytest.raises(ValidationError) as exc:
        ZoneData(
            name="K", zone_type="cabin", polygon=TRIANGLE,
            properties={"messwerte": {"headroom_mm": float("nan")}},
        )
    assert "endliche Zahlenwerte" in str(exc.value)
