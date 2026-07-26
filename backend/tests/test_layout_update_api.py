"""
HTTP tests for the layout-update endpoint (pillar 3: owner refit loop) and
the /analyze tier gate — using FastAPI dependency overrides with an isolated
sqlite database (no writes to the dev DB, no auth transport needed).

This establishes the route-test pattern the audit flagged as missing:
override get_db + get_current_user, seed an isolated DB, exercise real routes.
"""

import asyncio
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.main import app
from app.db.database import get_db
from app.core.permissions import get_current_user
from app.models.models import Base, Layout, Project, User

ZONES_V1 = [
    {"name": "Salon", "zone_type": "salon", "polygon": [[0, 0], [4000, 0], [4000, 3000], [0, 3000]]},
    {"name": "Pantry", "zone_type": "pantry", "polygon": [[4000, 0], [6000, 0], [6000, 3000], [4000, 3000]]},
]
ZONES_V2 = [
    {"name": "Salon XL", "zone_type": "salon", "polygon": [[0, 0], [5000, 0], [5000, 3000], [0, 3000]]},
]
PASSAGES = [
    {"from_zone": "Salon", "to_zone": "Pantry", "width_mm": 600},
]


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    """Isolated DB + dependency overrides. Yields (client, ids, current)."""
    db_path = tmp_path_factory.mktemp("layout_api") / "test.db"
    engine = create_async_engine(
        f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool
    )
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            owner = User(
                email="owner@test.example", hashed_password="x",
                full_name="Owner", role="user", tier="pro",
            )
            stranger = User(
                email="stranger@test.example", hashed_password="x",
                full_name="Stranger", role="user", tier="pro",
            )
            free_user = User(
                email="free@test.example", hashed_password="x",
                full_name="Free", role="user", tier="free",
            )
            session.add_all([owner, stranger, free_user])
            await session.flush()

            project = Project(
                user_id=owner.id, name="Testboot", description="",
                boat_class="cruising_sail", length_m=11.0, beam_m=3.8,
                status="active",
            )
            free_project = Project(
                user_id=free_user.id, name="Freeboot", description="",
                boat_class="cruising_sail", length_m=9.0, beam_m=3.2,
                status="active",
            )
            session.add_all([project, free_project])
            await session.flush()

            layout = Layout(
                project_id=project.id, name="Hauptdeck", version="v1.0",
                file_type="json", zones=ZONES_V1, passages=PASSAGES,
                deck_height_mm=1950,
            )
            free_layout = Layout(
                project_id=free_project.id, name="Deck", version="v1.0",
                file_type="json", zones=ZONES_V1, passages=PASSAGES,
                deck_height_mm=1900,
            )
            session.add_all([layout, free_layout])
            await session.commit()
            return {
                "owner": owner.id,
                "stranger": stranger.id,
                "free_user": free_user.id,
                "project": project.id,
                "free_project": free_project.id,
                "layout": layout.id,
                "free_layout": free_layout.id,
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


def _versions(client, ids):
    res = client.get(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}/versions"
    )
    assert res.status_code == 200, res.text
    return res.json()


def test_patch_updates_and_auto_snapshots(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"zones": ZONES_V2, "change_summary": "Salon vergrößert"},
    )
    assert res.status_code == 200, res.text
    body = res.json()
    assert len(body["zones"]) == 1
    assert body["zones"][0]["name"] == "Salon XL"

    versions = _versions(client, ids)
    assert len(versions) == 1
    snapshot = versions[0]
    # The snapshot preserves the PREVIOUS state (refit loop base)
    assert len(snapshot["zones_snapshot"]) == 2
    assert snapshot["zones_snapshot"][0]["name"] == "Salon"
    assert "Salon vergrößert" in snapshot["change_summary"]
    assert snapshot["changed_by"] == "owner@test.example"


def test_second_patch_increments_version(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]

    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"deck_height_mm": 2050},
    )
    assert res.status_code == 200, res.text
    assert res.json()["deck_height_mm"] == 2050

    versions = _versions(client, ids)
    assert [v["version_number"] for v in versions] == [2, 1]
    # Version 2 snapshots the post-first-patch state (ZONES_V2)
    assert len(versions[0]["zones_snapshot"]) == 1


def test_patch_without_changes_rejected(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"change_summary": "nur Kommentar"},
    )
    assert res.status_code == 422


def test_patch_foreign_project_is_404(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["stranger"]
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"name": "Gekapert"},
    )
    assert res.status_code == 404
    current["user_id"] = ids["owner"]


def test_patch_validates_zone_shape(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"zones": [{"zone_type": "salon"}]},  # name/polygon fehlen
    )
    assert res.status_code == 422


def test_patch_explicit_null_rejected_no_phantom_version(ctx):
    # Explicit nulls previously passed the "any changes?" gate, created a
    # phantom snapshot version and applied nothing (200 no-op).
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    before = len(_versions(client, ids))
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"deck_height_mm": None},
    )
    assert res.status_code == 422, res.text
    assert len(_versions(client, ids)) == before, "phantom version created"


def test_patch_empty_zones_rejected(ctx):
    # Emptying a layout is not a refit operation (min_length=1)
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"zones": []},
    )
    assert res.status_code == 422


def test_snapshot_includes_meta_and_restore_roundtrip(ctx):
    # deck_height_mm is analysis-relevant: the snapshot must capture it and a
    # restore must bring it back (previously destructive/unrestorable).
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    base = f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}"

    current_layout = client.get(base).json()
    height_before = current_layout["deck_height_mm"]

    res = client.patch(base, json={"deck_height_mm": height_before + 100})
    assert res.status_code == 200, res.text

    versions = _versions(client, ids)
    snapshot = versions[0]
    assert snapshot["layout_meta_snapshot"]["deck_height_mm"] == height_before

    # Restore = what the frontend sends: geometry + meta deck height
    res = client.patch(
        base,
        json={
            "zones": snapshot["zones_snapshot"],
            "passages": snapshot["passages_snapshot"] or PASSAGES,
            "deck_height_mm": snapshot["layout_meta_snapshot"]["deck_height_mm"],
            "change_summary": f"Wiederhergestellt von Version {snapshot['version_number']}",
        },
    )
    assert res.status_code == 200, res.text
    assert res.json()["deck_height_mm"] == height_before


def test_version_number_unique_constraint():
    # The read-max-then-insert numbering is guarded by a DB unique constraint
    # on (layout_id, version_number): a concurrent collision must fail hard
    # (handled as 409) instead of silently producing two "Version N" rows.
    from app.models.models import LayoutVersion

    constraints = {c.name for c in LayoutVersion.__table__.constraints}
    assert "uq_layout_version_number" in constraints


def test_zone_rename_cascades_to_references(ctx):
    # Zone renames must follow into zone_name-referencing rows (structural
    # items etc.) — otherwise a rename silently orphans measured data and the
    # next analysis drops it without a trace.
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    base = f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}"

    res = client.post(
        f"{base}/structural",
        json={
            "name": "Motor", "item_type": "engine", "zone_name": "Salon XL",
            "weight_kg": 250.0, "position_x_mm": 2000.0, "position_y_mm": 1500.0,
        },
    )
    assert res.status_code == 201, res.text
    item_id = res.json()["id"]

    current_zones = client.get(base).json()["zones"]
    renamed = [
        {**z, "name": "Salon Royal" if z["name"] == "Salon XL" else z["name"]}
        for z in current_zones
    ]
    res = client.patch(
        base,
        json={
            "zones": renamed,
            "zone_renames": {"Salon XL": "Salon Royal"},
            "change_summary": "Salon umbenannt",
        },
    )
    assert res.status_code == 200, res.text

    items = client.get(f"{base}/structural").json()
    item = next(i for i in items if i["id"] == item_id)
    assert item["zone_name"] == "Salon Royal"


def test_analyze_tier_gate_blocks_free_user(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["free_user"]
    res = client.post(
        f"/api/v1/projects/{ids['free_project']}/analyze",
        json={"module": "structural", "layout_id": str(ids["free_layout"])},
    )
    assert res.status_code == 403, res.text
    assert "PRO" in res.json()["detail"]
    current["user_id"] = ids["owner"]


def test_analyze_unknown_module_still_400(ctx):
    client, ids, current = ctx
    current["user_id"] = ids["owner"]
    res = client.post(
        f"/api/v1/projects/{ids['project']}/analyze",
        json={"module": "gibtsnicht", "layout_id": str(uuid.uuid4())},
    )
    assert res.status_code == 400
