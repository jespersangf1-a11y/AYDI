"""
HTTP tests for zone-material assignments (pillar 3: owner refit — material
swap per zone) using the dependency-override route-test pattern.

Covers the previously untested CRUD routes plus the integration that gives
them meaning: an assignment feeding the materials analysis module.
"""

import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.main import app
from app.db.database import get_db
from app.core.permissions import get_current_user
from app.models.models import Base, Layout, Material, Project, User

ZONES = [
    {"name": "Salon", "zone_type": "salon", "polygon": [[0, 0], [4000, 0], [4000, 3000], [0, 3000]]},
    {"name": "Pantry", "zone_type": "pantry", "polygon": [[4000, 0], [6000, 0], [6000, 3000], [4000, 3000]]},
]
PASSAGES = [{"from_zone": "Salon", "to_zone": "Pantry", "width_mm": 600}]


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("zone_materials") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            owner = User(
                email="owner@zm.example", hashed_password="x",
                full_name="Owner", role="user", tier="pro",
            )
            stranger = User(
                email="stranger@zm.example", hashed_password="x",
                full_name="Stranger", role="user", tier="pro",
            )
            session.add_all([owner, stranger])
            await session.flush()

            project = Project(
                user_id=owner.id, name="Materialboot", description="",
                boat_class="cruising_sail", length_m=11.0, beam_m=3.8,
                status="active",
            )
            session.add(project)
            await session.flush()

            layout = Layout(
                project_id=project.id, name="Hauptdeck", version="v1.0",
                file_type="json", zones=ZONES, passages=PASSAGES,
                deck_height_mm=1950,
            )
            teak = Material(
                name="Teak Burma Grade A", category="wood", subcategory="deck",
                manufacturer="Testwerft", cost_per_unit=450.0, cost_unit="sqm",
                lifespan_years=20.0, maintenance_interval_months=12,
                maintenance_cost_factor=0.05,
                known_issues=["black_staining", "uv_checking"],
            )
            session.add_all([layout, teak])
            await session.commit()
            return {
                "owner": owner.id,
                "stranger": stranger.id,
                "project": project.id,
                "layout": layout.id,
                "material": teak.id,
            }

    ids = asyncio.run(_seed())
    current = {"user_id": ids["owner"]}

    async def override_get_db():
        async with session_factory() as session:
            yield session

    async def override_get_current_user():
        async with session_factory() as session:
            return await session.get(User, current["user_id"])

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user
    client = TestClient(app)
    yield client, ids, current
    app.dependency_overrides.clear()


def _base(ids) -> str:
    return f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}/materials"


def test_assign_list_delete_roundtrip(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon",
            "surface_type": "floor",
            "material_id": str(ids["material"]),
            "area_sqm": 12.0,
        },
    )
    assert res.status_code == 201, res.text
    assignment = res.json()
    assert assignment["zone_name"] == "Salon"

    res = client.get(_base(ids))
    assert res.status_code == 200
    assert len(res.json()) == 1

    res = client.delete(f"{_base(ids)}/{assignment['id']}")
    assert res.status_code == 204
    assert client.get(_base(ids)).json() == []


def test_assign_unknown_material_404(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon",
            "surface_type": "floor",
            "material_id": "00000000-0000-0000-0000-000000000000",
            "area_sqm": 5.0,
        },
    )
    assert res.status_code == 404


def test_foreign_user_cannot_touch_assignments(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["stranger"]
    assert client.get(_base(ids)).status_code == 404
    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon",
            "surface_type": "floor",
            "material_id": str(ids["material"]),
            "area_sqm": 5.0,
        },
    )
    assert res.status_code == 404
    current["user_id"] = ids["owner"]


def test_assign_rejects_invalid_payloads(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    # Negative area would SUBTRACT lifecycle cost/weight in the analysis
    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon", "surface_type": "floor",
            "material_id": str(ids["material"]), "area_sqm": -50,
        },
    )
    assert res.status_code == 422

    # Free-form surface types bypass the analysis' surface handling
    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon", "surface_type": "banana",
            "material_id": str(ids["material"]), "area_sqm": 5.0,
        },
    )
    assert res.status_code == 422

    # Phantom zones must not silently flow into the analysis
    res = client.post(
        _base(ids),
        json={
            "zone_name": "Gibtsnicht", "surface_type": "floor",
            "material_id": str(ids["material"]), "area_sqm": 5.0,
        },
    )
    assert res.status_code == 422


def test_duplicate_zone_surface_rejected(ctx):
    # One material per (zone, surface): the analysis sums per assignment —
    # a second material on the same surface would double-count area/cost.
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.post(
        _base(ids),
        json={
            "zone_name": "Pantry", "surface_type": "floor",
            "material_id": str(ids["material"]), "area_sqm": 6.0,
        },
    )
    assert res.status_code == 201, res.text
    assignment_id = res.json()["id"]

    res = client.post(
        _base(ids),
        json={
            "zone_name": "Pantry", "surface_type": "floor",
            "material_id": str(ids["material"]), "area_sqm": 6.0,
        },
    )
    assert res.status_code == 409, res.text
    assert "bereits" in res.json()["detail"]

    # Cleanup so other tests see a defined state
    client.delete(f"{_base(ids)}/{assignment_id}")


def test_material_mutation_bound_to_creator(ctx):
    # The material DB is global (feeds OTHER users' analyses): only the
    # creator or an admin may mutate; legacy rows (no creator) are admin-only.
    client, ids, current = ctx

    current["user_id"] = ids["stranger"]
    res = client.post(
        "/api/v1/materials",
        json={"name": "Fremdes Eichenfurnier", "category": "wood", "subcategory": "veneer"},
    )
    assert res.status_code == 201, res.text
    foreign_material_id = res.json()["id"]

    # Non-creator: no PATCH, no DELETE
    current["user_id"] = ids["owner"]
    res = client.patch(
        f"/api/v1/materials/{foreign_material_id}", json={"cost_per_unit": 1.0}
    )
    assert res.status_code == 403, res.text
    assert client.delete(f"/api/v1/materials/{foreign_material_id}").status_code == 403

    # Legacy/seed material (created_by_user_id=None) is admin-managed
    res = client.patch(
        f"/api/v1/materials/{ids['material']}", json={"cost_per_unit": 1.0}
    )
    assert res.status_code == 403

    # Creator may mutate and delete their own material
    current["user_id"] = ids["stranger"]
    res = client.patch(
        f"/api/v1/materials/{foreign_material_id}", json={"cost_per_unit": 99.0}
    )
    assert res.status_code == 200, res.text
    assert client.delete(f"/api/v1/materials/{foreign_material_id}").status_code == 204
    current["user_id"] = ids["owner"]


def test_material_delete_blocked_while_in_use(ctx):
    # ZoneMaterial cascades on material delete — deleting an in-use material
    # would silently wipe assignments (possibly in OTHER users' projects).
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.post(
        "/api/v1/materials",
        json={"name": "Eigenes Teakdeck", "category": "wood", "subcategory": "deck"},
    )
    assert res.status_code == 201, res.text
    material_id = res.json()["id"]

    res = client.post(
        _base(ids),
        json={
            "zone_name": "Pantry", "surface_type": "wall",
            "material_id": material_id, "area_sqm": 8.0,
        },
    )
    assert res.status_code == 201, res.text
    assignment_id = res.json()["id"]

    res = client.delete(f"/api/v1/materials/{material_id}")
    assert res.status_code == 409, res.text
    assert "Zonenzuweisung" in res.json()["detail"]

    # After removing the assignment the delete goes through
    assert client.delete(f"{_base(ids)}/{assignment_id}").status_code == 204
    assert client.delete(f"/api/v1/materials/{material_id}").status_code == 204


def test_assignment_feeds_materials_analysis(ctx):
    # The point of the whole feature: an assignment must reach the materials
    # analysis module and produce a real (non-fabricated) result.
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.post(
        _base(ids),
        json={
            "zone_name": "Salon",
            "surface_type": "floor",
            "material_id": str(ids["material"]),
            "area_sqm": 12.0,
        },
    )
    assert res.status_code == 201, res.text

    res = client.post(
        f"/api/v1/projects/{ids['project']}/analyze",
        json={"module": "materials", "layout_id": str(ids["layout"])},
    )
    assert res.status_code == 201, res.text
    result = res.json()
    assert 0 <= result["overall_score"] <= 100
    assert result["module"] == "materials"
