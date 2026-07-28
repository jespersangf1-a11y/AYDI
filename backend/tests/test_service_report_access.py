"""Access-control tests for service reports (L-9).

Before the fix the routes had no ownership at all — any authenticated user could
list, read, modify and delete every other user's confidential service reports.
Owner A creates a report; stranger B must be unable to see or touch it.
"""

import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.main import app
from app.db.database import get_db
from app.core.permissions import get_current_user
from app.models.models import Base, User

BASE = "/api/v1"


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("svc_access") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            users = {
                key: User(
                    email=f"{key}@svc.example", hashed_password="x",
                    full_name=key.capitalize(), role="user", tier="pro",
                )
                for key in ("owner", "stranger")
            }
            session.add_all(users.values())
            await session.commit()
            return {k: u.id for k, u in users.items()}

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


def _make_report():
    return {
        "report_type": "repair",
        "category": "structure",
        "zone_type": "engine",
        "description": "VERTRAULICH: Konstruktionsfehler im Motorfundament",
        "severity": "critical",
        "cost_eur": 24500.0,
    }


def test_stranger_cannot_access_foreign_service_reports(ctx):
    client, ids, current = ctx

    # Owner creates a confidential report.
    _as(current, ids, "owner")
    res = client.post(f"{BASE}/service-reports", json=_make_report())
    assert res.status_code == 201, res.text
    report_id = res.json()["id"]
    assert client.get(f"{BASE}/service-reports").json(), "owner sees own report"

    # Stranger must not see it in the list, nor read/modify/delete it.
    _as(current, ids, "stranger")
    listing = client.get(f"{BASE}/service-reports")
    assert listing.status_code == 200
    assert all(r["id"] != report_id for r in listing.json()), "leak in list!"

    assert client.get(f"{BASE}/service-reports/{report_id}").status_code == 404
    assert client.patch(
        f"{BASE}/service-reports/{report_id}",
        json={"description": "Von einem Fremden ueberschrieben"},
    ).status_code == 404
    assert client.delete(f"{BASE}/service-reports/{report_id}").status_code == 404

    # Owner's report is untouched.
    _as(current, ids, "owner")
    got = client.get(f"{BASE}/service-reports/{report_id}")
    assert got.status_code == 200
    assert "VERTRAULICH" in got.json()["description"]


def test_owner_can_manage_own_report(ctx):
    client, ids, current = ctx
    _as(current, ids, "owner")
    rid = client.post(f"{BASE}/service-reports", json=_make_report()).json()["id"]

    patched = client.patch(
        f"{BASE}/service-reports/{rid}", json={"severity": "high"}
    )
    assert patched.status_code == 200 and patched.json()["severity"] == "high"
    assert client.delete(f"{BASE}/service-reports/{rid}").status_code == 204
    assert client.get(f"{BASE}/service-reports/{rid}").status_code == 404
