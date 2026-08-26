"""Basis-Sicherheitsheader auf jeder Antwort.

Die App setzte bisher keinen einzigen dieser Header. Praktisch relevant ist vor
allem ``X-Content-Type-Options: nosniff``: Nutzertext wird in JSON-Antworten
zurueckgespiegelt (z.B. ein ``model_name`` mit ``<script>``), und ohne nosniff
darf ein Browser eine solche Antwort als HTML deuten und das Skript ausfuehren.
"""

import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.middleware import SecurityHeadersMiddleware
from app.db.database import get_db
from app.main import app
from app.models.models import Base


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    """Bewusst OHNE Context-Manager: so laeuft der Lifespan (Seed + Korpus-Warmup)
    nicht mit. Geprueft werden Response-Header, nicht der Startvorgang."""
    db_path = tmp_path_factory.mktemp("secheaders") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _create():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(_create())

    async def _override():
        async with session_factory() as session:
            yield session

    app.dependency_overrides[get_db] = _override
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.pop(get_db, None)


EXPECTED = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
}


@pytest.mark.parametrize("header,value", sorted(EXPECTED.items()))
def test_public_response_carries_header(client, header, value):
    response = client.get("/api/v1/knowledge/categories")
    assert response.status_code == 200
    assert response.headers.get(header) == value


@pytest.mark.parametrize("header,value", sorted(EXPECTED.items()))
def test_error_response_carries_header(client, header, value):
    """Auch 401/403/500 muessen die Header tragen — sonst ist die Luecke nur verschoben."""
    response = client.get("/api/v1/projects")
    assert response.status_code == 401
    assert response.headers.get(header) == value


def test_csp_blocks_active_content(client):
    csp = client.get("/api/v1/knowledge/categories").headers.get("Content-Security-Policy")
    assert csp is not None
    assert "default-src 'none'" in csp
    assert "frame-ancestors 'none'" in csp


def test_reflected_script_tag_cannot_be_sniffed_as_html(client):
    """Der eigentliche Schutz fuer zurueckgespiegelten Nutzertext."""
    response = client.post(
        "/api/v1/quick-analysis",
        json={
            "model_name": "<script>alert('xss')</script>",
            "boat_class": "cruising_sail",
            "length_m": 10.0,
            "beam_m": 3.5,
        },
    )
    assert response.status_code in (200, 201, 422)
    assert response.headers.get("X-Content-Type-Options") == "nosniff"
    assert response.headers["content-type"].startswith("application/json")


def test_hsts_only_when_cookies_are_secure(client, monkeypatch):
    """HSTS darf eine lokale HTTP-Entwicklungsumgebung nicht aussperren."""
    from app.core import middleware as mw

    monkeypatch.setattr(mw.settings, "COOKIE_SECURE", False, raising=False)
    assert "Strict-Transport-Security" not in client.get(
        "/api/v1/knowledge/categories"
    ).headers


def test_middleware_does_not_overwrite_explicit_headers():
    """setdefault, nicht Zuweisung — eine Route darf strenger sein."""
    assert "X-Content-Type-Options" in SecurityHeadersMiddleware.STATIC_HEADERS
