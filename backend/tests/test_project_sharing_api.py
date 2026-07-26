"""
HTTP tests for project sharing (pillar 4, stage 1 — decision 'Option C').

Access matrix: owner / editor-member / viewer-member / stranger across the
role-gated route boundaries, plus the member management endpoints.
"""

import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.main import app
from app.db.database import get_db
from app.core.permissions import get_current_user
from app.models.models import Base, Layout, Project, User

ZONES = [
    {"name": "Salon", "zone_type": "salon", "polygon": [[0, 0], [4000, 0], [4000, 3000], [0, 3000]]},
]


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("sharing") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            users = {
                key: User(
                    email=f"{key}@share.example", hashed_password="x",
                    full_name=key.capitalize(), role="user",
                    # stranger is FREE tier → doubles as the benchmark
                    # tier-gate probe (PRO feature)
                    tier="free" if key == "stranger" else "pro",
                )
                for key in ("owner", "editor", "viewer", "stranger")
            }
            session.add_all(users.values())
            await session.flush()

            project = Project(
                user_id=users["owner"].id, name="Geteiltes Boot", description="",
                boat_class="cruising_sail", length_m=11.0, beam_m=3.8,
                status="active",
            )
            session.add(project)
            await session.flush()
            layout = Layout(
                project_id=project.id, name="Deck", version="v1.0",
                file_type="json", zones=ZONES, passages=[], deck_height_mm=1950,
            )
            session.add(layout)
            await session.commit()
            return {
                **{k: u.id for k, u in users.items()},
                "project": project.id,
                "layout": layout.id,
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


def _as(current, ids, who):
    current["user_id"] = ids[who]


def test_owner_shares_project(ctx):
    client, ids, current = ctx
    _as(current, ids, "owner")

    for email, role in (("editor@share.example", "editor"), ("viewer@share.example", "viewer")):
        res = client.post(
            f"/api/v1/projects/{ids['project']}/members",
            json={"email": email, "role": role},
        )
        assert res.status_code == 201, res.text
        assert res.json()["role"] == role

    # Duplicate → 409; unknown email → 404; owner self-add → 409
    res = client.post(
        f"/api/v1/projects/{ids['project']}/members",
        json={"email": "viewer@share.example", "role": "viewer"},
    )
    assert res.status_code == 409
    # Duplicate share points to the in-place role change (stage 2)
    assert "Rolle" in res.json()["detail"]
    res = client.post(
        f"/api/v1/projects/{ids['project']}/members",
        json={"email": "niemand@share.example", "role": "viewer"},
    )
    assert res.status_code == 404
    res = client.post(
        f"/api/v1/projects/{ids['project']}/members",
        json={"email": "owner@share.example", "role": "editor"},
    )
    assert res.status_code == 409

    members = client.get(f"/api/v1/projects/{ids['project']}/members").json()
    assert {m["role"] for m in members} == {"owner", "editor", "viewer"}


def test_member_cannot_manage_members(ctx):
    client, ids, current = ctx
    _as(current, ids, "editor")
    res = client.post(
        f"/api/v1/projects/{ids['project']}/members",
        json={"email": "stranger@share.example", "role": "viewer"},
    )
    assert res.status_code == 403, res.text
    res = client.delete(
        f"/api/v1/projects/{ids['project']}/members/{ids['viewer']}"
    )
    assert res.status_code == 403


def test_viewer_reads_but_cannot_write(ctx):
    client, ids, current = ctx
    _as(current, ids, "viewer")
    base = f"/api/v1/projects/{ids['project']}"

    # Reads: project, layouts, versions
    res = client.get(base)
    assert res.status_code == 200
    assert res.json()["access_role"] == "viewer"
    assert client.get(f"{base}/layouts").status_code == 200
    assert client.get(f"{base}/layouts/{ids['layout']}/versions").status_code == 200

    # Writes → 403 with role message
    res = client.patch(
        f"{base}/layouts/{ids['layout']}", json={"deck_height_mm": 2000}
    )
    assert res.status_code == 403, res.text
    assert "viewer" in res.json()["detail"]
    res = client.post(
        f"{base}/analyze",
        json={"module": "ergonomics", "layout_id": str(ids["layout"])},
    )
    assert res.status_code == 403
    # Project delete is owner-only even for editors/viewers
    assert client.delete(base).status_code == 403


def test_editor_can_write(ctx):
    client, ids, current = ctx
    _as(current, ids, "editor")
    base = f"/api/v1/projects/{ids['project']}"
    res = client.patch(
        f"{base}/layouts/{ids['layout']}",
        json={"deck_height_mm": 2000, "change_summary": "Editor-Test"},
    )
    assert res.status_code == 200, res.text
    assert client.delete(base).status_code == 403  # not owner


def test_shared_project_in_member_listing(ctx):
    client, ids, current = ctx
    _as(current, ids, "viewer")
    projects = client.get("/api/v1/projects").json()
    entry = next(p for p in projects if p["id"] == str(ids["project"]))
    assert entry["access_role"] == "viewer"

    _as(current, ids, "owner")
    projects = client.get("/api/v1/projects").json()
    entry = next(p for p in projects if p["id"] == str(ids["project"]))
    assert entry["access_role"] == "owner"


def test_stranger_still_404(ctx):
    client, ids, current = ctx
    _as(current, ids, "stranger")
    base = f"/api/v1/projects/{ids['project']}"
    assert client.get(base).status_code == 404
    assert client.get(f"{base}/layouts").status_code == 404
    assert client.get(f"{base}/members").status_code == 404
    assert client.get("/api/v1/projects").json() == []


def test_editor_patch_project_returns_access_role(ctx):
    # Project PATCH is editor-level (deliberate: metadata edits are part of
    # collaborative refit work); response must carry the caller's role so the
    # UI badge stays correct after an edit.
    client, ids, current = ctx
    base = f"/api/v1/projects/{ids['project']}"

    _as(current, ids, "editor")
    res = client.patch(base, json={"description": "Editor-Metadaten-Test"})
    assert res.status_code == 200, res.text
    assert res.json()["access_role"] == "editor"

    _as(current, ids, "viewer")
    assert client.patch(base, json={"description": "x"}).status_code == 403

    _as(current, ids, "owner")
    res = client.patch(base, json={"description": "Owner-Test"})
    assert res.status_code == 200
    assert res.json()["access_role"] == "owner"


def test_version_changed_by_is_server_set(ctx):
    # Audit trail: changed_by is the authenticated user's email; a
    # client-supplied value (removed from the schema) must be ignored.
    client, ids, current = ctx
    _as(current, ids, "editor")
    res = client.post(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}/versions",
        json={
            "change_summary": "Spoof-Test",
            "changed_by": "gefaelscht@evil.example",  # extra field → ignored
        },
    )
    assert res.status_code == 201, res.text
    assert res.json()["changed_by"] == "editor@share.example"


def test_benchmarks_tier_gate_and_k_anonymity(ctx):
    client, ids, current = ctx

    # FREE tier → 403 (PRO feature, server-side gate)
    _as(current, ids, "stranger")
    res = client.get("/api/v1/class-benchmarks/cruising_sail")
    assert res.status_code == 403, res.text

    # PRO tier, but sample of 1 → k-anonymity: no metrics, German notice
    _as(current, ids, "owner")
    res = client.get("/api/v1/class-benchmarks/cruising_sail")
    assert res.status_code == 200, res.text
    body = res.json()
    assert body["sample_size"] == 1
    assert body["metrics"] == {}
    assert body["analysis_scores"] == {}
    assert "Zu wenige" in body["message"]


def test_competitor_mutation_guard(ctx):
    # Competitor data feeds every user's market analysis — only the creator
    # (or an admin) may change/delete it. Same IDOR class as brand references.
    client, ids, current = ctx
    _as(current, ids, "owner")
    res = client.post(
        "/api/v1/competitors",
        json={"brand": "Testwerft", "model_name": "Guard 36", "boat_class": "cruising_sail"},
    )
    assert res.status_code == 201, res.text
    competitor_id = res.json()["id"]

    _as(current, ids, "stranger")
    res = client.patch(
        f"/api/v1/competitors/{competitor_id}", json={"notes": "Sabotage"}
    )
    assert res.status_code == 403, res.text
    assert client.delete(f"/api/v1/competitors/{competitor_id}").status_code == 403

    _as(current, ids, "owner")
    res = client.patch(
        f"/api/v1/competitors/{competitor_id}", json={"notes": "Eigene Pflege"}
    )
    assert res.status_code == 200, res.text
    assert client.delete(f"/api/v1/competitors/{competitor_id}").status_code == 204


def test_owner_changes_member_role_in_place(ctx):
    # Stage 2: PATCH replaces the remove-then-reshare workaround.
    client, ids, current = ctx
    base = f"/api/v1/projects/{ids['project']}/members"

    # Owner promotes the viewer to editor...
    _as(current, ids, "owner")
    res = client.patch(f"{base}/{ids['viewer']}", json={"role": "editor"})
    assert res.status_code == 200, res.text
    assert res.json()["role"] == "editor"

    # ...the promoted member can now write...
    _as(current, ids, "viewer")
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"deck_height_mm": 1990},
    )
    assert res.status_code == 200, res.text

    # ...and demotion revokes it again.
    _as(current, ids, "owner")
    res = client.patch(f"{base}/{ids['viewer']}", json={"role": "viewer"})
    assert res.status_code == 200
    _as(current, ids, "viewer")
    res = client.patch(
        f"/api/v1/projects/{ids['project']}/layouts/{ids['layout']}",
        json={"deck_height_mm": 2000},
    )
    assert res.status_code == 403

    # Non-owners cannot change roles; unknown member → 404; bad role → 422
    _as(current, ids, "editor")
    assert client.patch(f"{base}/{ids['viewer']}", json={"role": "editor"}).status_code == 403
    _as(current, ids, "owner")
    assert client.patch(f"{base}/{ids['stranger']}", json={"role": "editor"}).status_code == 404
    assert client.patch(f"{base}/{ids['viewer']}", json={"role": "owner"}).status_code == 422


def test_member_can_leave_and_revocation_works(ctx):
    client, ids, current = ctx

    # Viewer leaves the project themselves
    _as(current, ids, "viewer")
    res = client.delete(
        f"/api/v1/projects/{ids['project']}/members/{ids['viewer']}"
    )
    assert res.status_code == 204, res.text
    assert client.get(f"/api/v1/projects/{ids['project']}").status_code == 404

    # Owner revokes the editor
    _as(current, ids, "owner")
    res = client.delete(
        f"/api/v1/projects/{ids['project']}/members/{ids['editor']}"
    )
    assert res.status_code == 204
    _as(current, ids, "editor")
    assert client.get(f"/api/v1/projects/{ids['project']}").status_code == 404
