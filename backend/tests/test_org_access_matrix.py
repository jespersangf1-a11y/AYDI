"""Organization access matrix + effective tier + attach/detach + fleet view
+ brand-reference org scoping (pillar 4, stage 2).

The fixture seeds a fully-formed org (elena=owner, sarah=member, hans=admin)
with Elena's project attached, so access tests don't depend on ordering.
Governance tests that mutate membership structure (last-owner, role changes)
build their own fresh ctx to avoid cross-test coupling.
"""

import pytest

from app.models.models import Organization, OrganizationMember, Project
from tests.conftest_stage2 import make_ctx


async def _seed_org(session, ids):
    org = Organization(name="Werft Nord", tier="free", created_by_user_id=ids["elena"])
    session.add(org)
    await session.flush()
    session.add_all([
        OrganizationMember(organization_id=org.id, user_id=ids["elena"], org_role="owner"),
        OrganizationMember(organization_id=org.id, user_id=ids["sarah"], org_role="member"),
        OrganizationMember(organization_id=org.id, user_id=ids["hans"], org_role="admin"),
    ])
    # Attach Elena's project + a private project owned by hans
    proj = await session.get(Project, ids["project"])
    proj.org_id = org.id
    private = Project(
        user_id=ids["hans"], name="Hans privat", description="",
        boat_class="daysailer", length_m=8.0, beam_m=2.5, status="active",
    )
    session.add(private)
    await session.flush()
    ids["org"] = org.id
    ids["private"] = private.id


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("orgmatrix") / "test.db"
    client, ids, current, sf = make_ctx(db_path, seed_extra=_seed_org)
    yield client, ids, current, sf
    from app.main import app
    app.dependency_overrides.clear()


def _as(current, ids, who):
    current["user_id"] = ids[who]


def test_membership_listing_and_no_leak(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    orgs = client.get("/api/v1/orgs").json()
    assert any(o["id"] == str(ids["org"]) and o["org_role"] == "owner" for o in orgs)

    _as(current, ids, "stranger")
    assert client.get("/api/v1/orgs").json() == []
    assert client.get(f"/api/v1/orgs/{ids['org']}").status_code == 404  # no leak


def test_org_derived_project_access(ctx):
    client, ids, current, sf = ctx
    base = f"/api/v1/projects/{ids['project']}"

    # member -> editor (read + write, no delete)
    _as(current, ids, "sarah")
    assert client.get(base).json()["access_role"] == "editor"
    assert client.patch(f"{base}/layouts/{ids['layout']}", json={"deck_height_mm": 1980}).status_code == 200
    assert client.delete(base).status_code == 403

    # admin -> owner
    _as(current, ids, "hans")
    assert client.get(base).json()["access_role"] == "owner"

    # stranger -> 404
    _as(current, ids, "stranger")
    assert client.get(base).status_code == 404


def test_org_membership_does_not_expose_private_project(ctx):
    client, ids, current, sf = ctx
    # sarah is an org colleague of hans, but hans's private project (org_id NULL)
    # must stay invisible.
    _as(current, ids, "sarah")
    assert client.get(f"/api/v1/projects/{ids['private']}").status_code == 404


def test_effective_tier_from_org(ctx):
    client, ids, current, sf = ctx
    # Baseline: free member gated out of PRO benchmark
    _as(current, ids, "sarah")
    assert client.get("/api/v1/class-benchmarks/cruising_sail").status_code == 403

    # Platform admin raises org to enterprise
    _as(current, ids, "admin")
    res = client.post(f"/api/v1/admin/orgs/{ids['org']}/tier", json={"tier": "enterprise"})
    assert res.status_code == 200, res.text

    # Sarah (free personal) now passes PRO gate + ENTERPRISE fleet view
    _as(current, ids, "sarah")
    assert client.get("/api/v1/class-benchmarks/cruising_sail").status_code == 200
    fleet = client.get(f"/api/v1/orgs/{ids['org']}/projects")
    assert fleet.status_code == 200, fleet.text
    assert any(p["id"] == str(ids["project"]) for p in fleet.json())

    # Stranger (no org) still gated
    _as(current, ids, "stranger")
    assert client.get("/api/v1/class-benchmarks/cruising_sail").status_code == 403


def test_org_tier_is_admin_only(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")  # org owner, but NOT platform admin
    assert client.post(f"/api/v1/admin/orgs/{ids['org']}/tier", json={"tier": "pro"}).status_code == 403
    # PATCH /orgs cannot change tier (field not in schema → ignored)
    before = client.get(f"/api/v1/orgs/{ids['org']}").json()["tier"]
    client.patch(f"/api/v1/orgs/{ids['org']}", json={"name": "Werft Nord 2", "tier": "free"})
    assert client.get(f"/api/v1/orgs/{ids['org']}").json()["tier"] == before


def test_brand_reference_org_scoping(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "hans")  # org admin
    res = client.post("/api/v1/brand-references", json={
        "model_name": "Nord 40", "boat_class": "cruising_sail", "org_id": str(ids["org"]),
    })
    assert res.status_code == 201, res.text
    ref_id = res.json()["id"]

    # member sees it; stranger does not (list + direct get 404)
    _as(current, ids, "sarah")
    assert any(r["id"] == ref_id for r in client.get("/api/v1/brand-references").json())
    _as(current, ids, "stranger")
    assert not any(r["id"] == ref_id for r in client.get("/api/v1/brand-references").json())
    assert client.get(f"/api/v1/brand-references/{ref_id}").status_code == 404
    # stranger cannot create in a foreign org (404, no enumeration)
    assert client.post("/api/v1/brand-references", json={
        "model_name": "Fake", "boat_class": "cruising_sail", "org_id": str(ids["org"]),
    }).status_code == 404

    # member cannot delete an org ref; admin can
    _as(current, ids, "sarah")
    assert client.delete(f"/api/v1/brand-references/{ref_id}").status_code == 403
    _as(current, ids, "hans")
    assert client.delete(f"/api/v1/brand-references/{ref_id}").status_code == 204


# --- Governance tests use their own fresh ctx (they mutate membership) ---


def test_attach_requires_project_owner_and_membership(tmp_path):
    client, ids, current, sf = make_ctx(tmp_path / "attach.db")
    try:
        # Elena creates an org
        _as(current, ids, "elena")
        org = client.post("/api/v1/orgs", json={"name": "A"}).json()

        # Non-owner (sarah) cannot attach Elena's project
        _as(current, ids, "sarah")
        assert client.patch(f"/api/v1/projects/{ids['project']}/org",
                            json={"org_id": org["id"]}).status_code in (403, 404)

        # Elena owns the project but must be a member of the target org.
        # She IS (creator) → attach works.
        _as(current, ids, "elena")
        res = client.patch(f"/api/v1/projects/{ids['project']}/org", json={"org_id": org["id"]})
        assert res.status_code == 200, res.text
        # Double attach → 409
        assert client.patch(f"/api/v1/projects/{ids['project']}/org",
                            json={"org_id": org["id"]}).status_code == 409
        # Detach back to private
        assert client.patch(f"/api/v1/projects/{ids['project']}/org",
                            json={"org_id": None}).status_code == 200
    finally:
        from app.main import app
        app.dependency_overrides.clear()


def test_attach_to_foreign_org_404(tmp_path):
    client, ids, current, sf = make_ctx(tmp_path / "attach2.db")
    try:
        # stranger creates an org; elena is not a member
        _as(current, ids, "stranger")
        org = client.post("/api/v1/orgs", json={"name": "Fremd"}).json()
        _as(current, ids, "elena")
        assert client.patch(f"/api/v1/projects/{ids['project']}/org",
                            json={"org_id": org["id"]}).status_code == 404
    finally:
        from app.main import app
        app.dependency_overrides.clear()


def test_admin_cannot_remove_owner_but_can_remove_member(tmp_path):
    # Review fix: remove_org_member must enforce the role hierarchy, not just
    # the last-owner guard — an admin must NOT be able to evict an owner or
    # a co-admin via the delete path.
    import asyncio
    from uuid import UUID
    client, ids, current, sf = make_ctx(tmp_path / "removerank.db")
    try:
        _as(current, ids, "elena")
        org = client.post("/api/v1/orgs", json={"name": "Rank"}).json()
        oid = UUID(org["id"])

        async def _add():
            async with sf() as s:
                s.add_all([
                    OrganizationMember(organization_id=oid, user_id=ids["hans"], org_role="admin"),
                    OrganizationMember(organization_id=oid, user_id=ids["sarah"], org_role="member"),
                    OrganizationMember(organization_id=oid, user_id=ids["stranger"], org_role="admin"),
                ])
                await s.commit()
        asyncio.run(_add())

        _as(current, ids, "hans")  # admin
        # cannot remove the owner
        assert client.delete(f"/api/v1/orgs/{org['id']}/members/{ids['elena']}").status_code == 403
        # cannot remove a co-admin
        assert client.delete(f"/api/v1/orgs/{org['id']}/members/{ids['stranger']}").status_code == 403
        # CAN remove a plain member
        assert client.delete(f"/api/v1/orgs/{org['id']}/members/{ids['sarah']}").status_code == 204
    finally:
        from app.main import app
        app.dependency_overrides.clear()


def test_org_delete_reverts_projects_and_cleans_up(tmp_path):
    # Review fix: org delete must revert projects/brand-refs to private and
    # drop members/invitations — on SQLite too (FK enforcement now on, plus
    # explicit cleanup in the endpoint).
    import asyncio
    import datetime as _dt
    from uuid import UUID
    from sqlalchemy import select
    from app.models.models import BrandReferenceModel, Invitation
    from app.models.models import OrganizationMember as OM, Project
    client, ids, current, sf = make_ctx(tmp_path / "orgdel.db")
    try:
        _as(current, ids, "elena")
        org = client.post("/api/v1/orgs", json={"name": "Weg"}).json()
        oid = UUID(org["id"])
        client.patch(f"/api/v1/projects/{ids['project']}/org", json={"org_id": org["id"]})
        client.post("/api/v1/brand-references", json={
            "model_name": "X", "boat_class": "cruising_sail", "org_id": org["id"],
        })

        async def _seed():
            async with sf() as s:
                s.add(OM(organization_id=oid, user_id=ids["sarah"], org_role="member"))
                s.add(Invitation(email="x@y.example", organization_id=oid, role="member",
                                 status="pending", expires_at=_dt.datetime(2099, 1, 1)))
                await s.commit()
        asyncio.run(_seed())

        assert client.delete(f"/api/v1/orgs/{org['id']}").status_code == 204

        async def _check():
            async with sf() as s:
                proj = await s.get(Project, ids["project"])
                assert proj is not None and proj.org_id is None  # survives, private
                assert (await s.execute(select(BrandReferenceModel).where(
                    BrandReferenceModel.org_id == oid))).scalars().all() == []
                assert (await s.execute(select(OM).where(
                    OM.organization_id == oid))).scalars().all() == []
                assert (await s.execute(select(Invitation).where(
                    Invitation.organization_id == oid))).scalars().all() == []
        asyncio.run(_check())
    finally:
        from app.main import app
        app.dependency_overrides.clear()


def test_brand_reference_analysis_loader_respects_visibility(tmp_path):
    # Review fix (HOCH): the brand_dna ANALYSIS loader must apply the same
    # tenancy filter as the CRUD path — otherwise it leaks a foreign org's
    # private brand references into the analysis warnings.
    import asyncio
    from uuid import UUID
    from app.api.routes.layouts import _load_brand_references
    from app.models.models import BrandReferenceModel, OrganizationMember as OM, User
    client, ids, current, sf = make_ctx(tmp_path / "brandvis.db")
    try:
        _as(current, ids, "elena")
        org = client.post("/api/v1/orgs", json={"name": "Geheim"}).json()
        oid = UUID(org["id"])
        # Elena creates a PRIVATE org brand ref
        client.post("/api/v1/brand-references", json={
            "model_name": "Privat 40", "boat_class": "cruising_sail", "org_id": org["id"],
        })

        async def _check():
            async with sf() as s:
                elena = await s.get(User, ids["elena"])
                stranger = await s.get(User, ids["stranger"])
                # Elena (org member) sees the ref in the loader
                mine = await _load_brand_references("cruising_sail", elena, s)
                assert len(mine) >= 1
                # Stranger (not in org) must NOT see the org-private ref
                theirs = await _load_brand_references("cruising_sail", stranger, s)
                assert theirs == []
        asyncio.run(_check())
    finally:
        from app.main import app
        app.dependency_overrides.clear()


def test_last_owner_protection_and_role_changes(tmp_path):
    import asyncio
    client, ids, current, sf = make_ctx(tmp_path / "gov.db")
    try:
        from uuid import UUID
        _as(current, ids, "elena")
        org = client.post("/api/v1/orgs", json={"name": "Gov"}).json()
        oid = org["id"]
        oid_uuid = UUID(oid)

        async def _add_members():
            async with sf() as s:
                s.add_all([
                    OrganizationMember(organization_id=oid_uuid, user_id=ids["sarah"], org_role="member"),
                    OrganizationMember(organization_id=oid_uuid, user_id=ids["hans"], org_role="admin"),
                ])
                await s.commit()
        asyncio.run(_add_members())

        # Sole owner cannot leave
        _as(current, ids, "elena")
        assert client.delete(f"/api/v1/orgs/{oid}/members/{ids['elena']}").status_code == 409

        # Admin (hans) cannot change roles — owner only
        _as(current, ids, "hans")
        assert client.patch(f"/api/v1/orgs/{oid}/members/{ids['sarah']}",
                            json={"org_role": "admin"}).status_code == 403

        # Owner promotes hans to owner, then can leave
        _as(current, ids, "elena")
        assert client.patch(f"/api/v1/orgs/{oid}/members/{ids['hans']}",
                            json={"org_role": "owner"}).status_code == 200
        assert client.delete(f"/api/v1/orgs/{oid}/members/{ids['elena']}").status_code == 204
    finally:
        from app.main import app
        app.dependency_overrides.clear()
