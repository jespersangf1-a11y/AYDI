"""Invitation flow (pillar 4, stage 2): anti-enumeration, lifecycle,
accept/decline, expiry, conflicts — for both project and org scopes."""

import asyncio
from datetime import datetime, timedelta, timezone
from uuid import UUID

import pytest

from app.models.models import Invitation, Organization, OrganizationMember, ProjectMember
from tests.conftest_stage2 import make_ctx


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("invitations") / "test.db"
    client, ids, current, sf = make_ctx(db_path)
    yield client, ids, current, sf
    from app.main import app
    app.dependency_overrides.clear()


def _as(current, ids, who):
    current["user_id"] = ids[who]


def test_project_invite_anti_enumeration(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    base = f"/api/v1/projects/{ids['project']}/invitations"

    # Registered email (sarah) and a totally unknown email must yield
    # byte-identical response SHAPES and the same 201 status.
    r1 = client.post(base, json={"email": "sarah@yard.example", "role": "editor"})
    r2 = client.post(base, json={"email": "ghost@nowhere.example", "role": "viewer"})
    assert r1.status_code == 201 and r2.status_code == 201, (r1.text, r2.text)
    assert set(r1.json().keys()) == set(r2.json().keys())
    assert r1.json()["status"] == "pending"
    # No account-existence signal in the body
    assert "account" not in r1.text.lower()


def test_invite_appears_in_recipient_inbox_and_accept(ctx):
    client, ids, current, sf = ctx
    # sarah has a pending project invite from the previous test
    _as(current, ids, "sarah")
    inbox = client.get("/api/v1/invitations/mine").json()
    proj_inv = next(i for i in inbox if i["scope"] == "project")
    assert proj_inv["target_name"] == "Werftprojekt"

    # Accept → becomes a project member (editor)
    res = client.post(f"/api/v1/invitations/{proj_inv['id']}/accept")
    assert res.status_code == 200, res.text
    # Now sarah can access the project as editor
    base = f"/api/v1/projects/{ids['project']}"
    assert client.get(base).json()["access_role"] == "editor"
    # Invitation no longer pending in the inbox
    assert not any(i["id"] == proj_inv["id"] for i in client.get("/api/v1/invitations/mine").json())


def test_accept_is_idempotent_and_recipient_scoped(ctx):
    client, ids, current, sf = ctx
    # Create a fresh invite for hans
    _as(current, ids, "elena")
    base = f"/api/v1/projects/{ids['project']}/invitations"
    inv = client.post(base, json={"email": "hans@yard.example", "role": "viewer"}).json()

    # A different user (stranger) cannot see or accept it → 404 (IDs not probeable)
    _as(current, ids, "stranger")
    assert client.post(f"/api/v1/invitations/{inv['id']}/accept").status_code == 404

    # hans accepts; a second accept is idempotent (already handled → 410 pending-gone)
    _as(current, ids, "hans")
    assert client.post(f"/api/v1/invitations/{inv['id']}/accept").status_code == 200
    assert client.post(f"/api/v1/invitations/{inv['id']}/accept").status_code == 410


def test_conflicts(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    base = f"/api/v1/projects/{ids['project']}/invitations"

    # sarah is already a member (accepted earlier) → 409
    assert client.post(base, json={"email": "sarah@yard.example", "role": "editor"}).status_code == 409
    # owner's own email → 409
    assert client.post(base, json={"email": "elena@yard.example", "role": "viewer"}).status_code == 409
    # duplicate pending → 409
    client.post(base, json={"email": "neu@extern.example", "role": "viewer"})
    assert client.post(base, json={"email": "neu@extern.example", "role": "viewer"}).status_code == 409


def test_revoke_removes_from_inbox(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    base = f"/api/v1/projects/{ids['project']}/invitations"
    inv = client.post(base, json={"email": "widerruf@extern.example", "role": "viewer"}).json()
    # Register that user
    import asyncio as _a
    from app.models.models import User
    async def _mk_user():
        async with sf() as s:
            u = User(email="widerruf@extern.example", hashed_password="x",
                     full_name="Wider Ruf", role="user", tier="free")
            s.add(u)
            await s.commit()
            return u.id
    uid = _a.run(_mk_user())
    ids["widerruf"] = uid

    # Revoke
    assert client.delete(f"{base}/{inv['id']}").status_code == 204
    # Recipient no longer sees it
    _as(current, ids, "widerruf")
    assert not any(i["id"] == inv["id"] for i in client.get("/api/v1/invitations/mine").json())
    # Accepting a revoked invite → 410
    assert client.post(f"/api/v1/invitations/{inv['id']}/accept").status_code == 410


def test_expired_invite_not_accepted(ctx):
    client, ids, current, sf = ctx
    # Directly insert an expired invite for stranger
    async def _mk_expired():
        async with sf() as s:
            inv = Invitation(
                email="stranger@yard.example", project_id=ids["project"], role="viewer",
                invited_by_user_id=ids["elena"], status="pending",
                expires_at=datetime.now(timezone.utc) - timedelta(days=1),
            )
            s.add(inv)
            await s.commit()
            return inv.id
    inv_id = asyncio.run(_mk_expired())

    _as(current, ids, "stranger")
    # Expired invites are filtered from /mine
    assert not any(i["id"] == str(inv_id) for i in client.get("/api/v1/invitations/mine").json())
    # And cannot be accepted
    assert client.post(f"/api/v1/invitations/{inv_id}/accept").status_code == 410


def test_org_invitation_admin_role_owner_only(ctx):
    client, ids, current, sf = ctx
    # Build an org with elena=owner, hans=admin
    _as(current, ids, "elena")
    org = client.post("/api/v1/orgs", json={"name": "Invite-Org"}).json()
    oid = UUID(org["id"])

    async def _add_admin():
        async with sf() as s:
            s.add(OrganizationMember(organization_id=oid, user_id=ids["hans"], org_role="admin"))
            await s.commit()
    asyncio.run(_add_admin())

    obase = f"/api/v1/orgs/{org['id']}/invitations"
    # Admin (hans) may invite a member...
    _as(current, ids, "hans")
    assert client.post(obase, json={"email": "neuermitarbeiter@extern.example", "role": "member"}).status_code == 201
    # ...but NOT an admin (owner-only)
    assert client.post(obase, json={"email": "moechtegern@extern.example", "role": "admin"}).status_code == 403

    # Owner (elena) may invite an admin
    _as(current, ids, "elena")
    assert client.post(obase, json={"email": "vertreter@extern.example", "role": "admin"}).status_code == 201


def test_org_invite_accept_creates_membership(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    org = client.post("/api/v1/orgs", json={"name": "Beitritt-Org"}).json()
    obase = f"/api/v1/orgs/{org['id']}/invitations"
    client.post(obase, json={"email": "stranger@yard.example", "role": "member"})

    _as(current, ids, "stranger")
    inbox = client.get("/api/v1/invitations/mine").json()
    org_inv = next(i for i in inbox if i["scope"] == "org" and i["target_name"] == "Beitritt-Org")
    assert client.post(f"/api/v1/invitations/{org_inv['id']}/accept").status_code == 200
    # stranger is now a member → the org shows up in their list
    assert any(o["id"] == org["id"] for o in client.get("/api/v1/orgs").json())


def test_decline(ctx):
    client, ids, current, sf = ctx
    _as(current, ids, "elena")
    base = f"/api/v1/projects/{ids['project']}/invitations"
    client.post(base, json={"email": "ablehner@extern.example", "role": "viewer"})
    # Register + decline
    from app.models.models import User
    async def _mk():
        async with sf() as s:
            u = User(email="ablehner@extern.example", hashed_password="x",
                     full_name="Ab Lehner", role="user", tier="free")
            s.add(u)
            await s.commit()
            return u.id
    uid = asyncio.run(_mk())
    ids["ablehner"] = uid
    _as(current, ids, "ablehner")
    inv = client.get("/api/v1/invitations/mine").json()[0]
    assert client.post(f"/api/v1/invitations/{inv['id']}/decline").status_code == 204
    assert client.get("/api/v1/invitations/mine").json() == []
