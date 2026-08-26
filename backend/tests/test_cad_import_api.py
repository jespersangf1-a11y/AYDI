"""Regressionstests für den STEP/IGES-Import.

Deckt zwei Audit-Befunde ab:

* ROB-5 / SEC-8: Der STEP/IGES-Upload las die hochgeladene Datei unbegrenzt und
  vollständig in den Speicher. Jetzt gilt dieselbe Obergrenze wie im DXF-Pfad
  (25 MB), mit demselben Statuscode (413) und derselben deutschen Meldung, und
  der Lesevorgang bricht ab, sobald die Grenze überschritten ist.
* ROB-13: Der STEP-Textparser übernahm NaN/Infinity aus CARTESIAN_POINT
  ungeprüft in die Zonenpolygone. Jetzt werden solche Punkte verworfen und im
  Log gemeldet.

Route-Tests folgen dem etablierten Muster (get_db + get_current_user
überschreiben, isolierte SQLite-DB) aus tests/test_layout_update_api.py.
"""

import asyncio
import logging
import math

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.api.routes.import_cad import MAX_CAD_UPLOAD_BYTES, _read_upload_limited
from app.core.permissions import get_current_user
from app.db.database import get_db
from app.main import app
from app.models.models import Base, Project, User
from app.services.cad_import.step_parser import _parse_step_text

VALID_STEP = (
    "ISO-10303-21;\n"
    "HEADER;\n"
    "ENDSEC;\n"
    "DATA;\n"
    "#1=CARTESIAN_POINT('',(0.0,0.0,0.0));\n"
    "#2=CARTESIAN_POINT('',(5000.0,0.0,0.0));\n"
    "#3=CARTESIAN_POINT('',(5000.0,3000.0,0.0));\n"
    "#4=CARTESIAN_POINT('',(0.0,3000.0,0.0));\n"
    "ENDSEC;\n"
    "END-ISO-10303-21;\n"
).encode("utf-8")


# ---------------------------------------------------------------------------
# Fixture: isolierte DB + Dependency-Overrides
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cad_import_api") / "test.db"
    engine = create_async_engine(
        "sqlite+aiosqlite:///" + db_path.as_posix(), poolclass=NullPool
    )
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            owner = User(
                email="cadowner@test.example", hashed_password="x",
                full_name="Owner", role="user", tier="pro",
            )
            session.add(owner)
            await session.flush()
            project = Project(
                user_id=owner.id, name="Importboot", description="",
                boat_class="cruising_sail", length_m=12.0, beam_m=4.0,
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
    client = TestClient(app)
    yield client, ids
    app.dependency_overrides.clear()


def _oversized_payload() -> bytes:
    """Gerade eben über der Obergrenze — 1 MB Puffer für den Chunk-Abbruch."""
    return b"ISO-10303-21;\n" + b"A" * (MAX_CAD_UPLOAD_BYTES + 1024 * 1024)


# ---------------------------------------------------------------------------
# ROB-5 / SEC-8 — Größenlimit für STEP/IGES
# ---------------------------------------------------------------------------

class TestCadUploadSizeLimit:
    def test_step_upload_over_limit_returns_413(self, ctx):
        client, ids = ctx
        res = client.post(
            f"/api/v1/projects/{ids['project']}/import/step",
            files={"file": ("huge.step", _oversized_payload(), "application/octet-stream")},
        )
        assert res.status_code == 413, res.text
        assert res.json()["detail"] == "Datei zu gross. Maximal 25 MB erlaubt."

    def test_iges_upload_over_limit_returns_413(self, ctx):
        client, ids = ctx
        res = client.post(
            f"/api/v1/projects/{ids['project']}/import/iges",
            files={"file": ("huge.iges", _oversized_payload(), "application/octet-stream")},
        )
        assert res.status_code == 413, res.text
        assert res.json()["detail"] == "Datei zu gross. Maximal 25 MB erlaubt."

    def test_limit_matches_dxf_path(self):
        """Gleiche Obergrenze wie der DXF-Upload (layouts.import_dxf)."""
        assert MAX_CAD_UPLOAD_BYTES == 25 * 1024 * 1024

    def test_step_upload_within_limit_still_parses(self, ctx):
        client, ids = ctx
        res = client.post(
            f"/api/v1/projects/{ids['project']}/import/step",
            files={"file": ("klein.step", VALID_STEP, "application/octet-stream")},
        )
        assert res.status_code == 200, res.text
        assert "zones" in res.json()

    def test_empty_upload_still_400(self, ctx):
        client, ids = ctx
        res = client.post(
            f"/api/v1/projects/{ids['project']}/import/step",
            files={"file": ("leer.step", b"", "application/octet-stream")},
        )
        assert res.status_code == 400, res.text
        assert "Leere Datei" in res.json()["detail"]


class _CountingUpload:
    """Minimaler UploadFile-Ersatz, der mitzählt, wie viel gelesen wurde."""

    def __init__(self, total_bytes: int):
        self.remaining = total_bytes
        self.bytes_read = 0

    async def read(self, size: int = -1) -> bytes:
        if self.remaining <= 0:
            return b""
        n = self.remaining if size < 0 else min(size, self.remaining)
        self.remaining -= n
        self.bytes_read += n
        return b"A" * n


class TestReadUploadLimited:
    """Der Lesevorgang bricht ab, statt erst alles zu lesen und dann zu prüfen."""

    def test_aborts_early_without_reading_everything(self):
        upload = _CountingUpload(total_bytes=200 * 1024 * 1024)
        with pytest.raises(HTTPException) as exc:
            asyncio.run(_read_upload_limited(upload, max_bytes=2 * 1024 * 1024))
        assert exc.value.status_code == 413
        assert exc.value.detail == "Datei zu gross. Maximal 2 MB erlaubt."
        # Höchstens Limit + ein Chunk gepuffert — nicht die vollen 200 MB.
        assert upload.bytes_read <= 2 * 1024 * 1024 + 1024 * 1024
        assert upload.remaining > 0

    def test_reads_full_content_within_limit(self):
        upload = _CountingUpload(total_bytes=3 * 1024 * 1024)
        content = asyncio.run(_read_upload_limited(upload, max_bytes=25 * 1024 * 1024))
        assert len(content) == 3 * 1024 * 1024
        assert upload.remaining == 0

    def test_exact_limit_is_accepted(self):
        upload = _CountingUpload(total_bytes=1024)
        content = asyncio.run(_read_upload_limited(upload, max_bytes=1024))
        assert len(content) == 1024


# ---------------------------------------------------------------------------
# ROB-13 — nicht-finite Koordinaten im STEP-Textparser
# ---------------------------------------------------------------------------

STEP_WITH_NON_FINITE = (
    "ISO-10303-21;\n"
    "DATA;\n"
    "#1=CARTESIAN_POINT('',(0.0,0.0,0.0));\n"
    "#2=CARTESIAN_POINT('',(5000.0,0.0,0.0));\n"
    "#3=CARTESIAN_POINT('',(5000.0,3000.0,0.0));\n"
    "#4=CARTESIAN_POINT('',(0.0,3000.0,0.0));\n"
    "#5=CARTESIAN_POINT('',(NaN,Infinity,0.0));\n"
    "#6=CARTESIAN_POINT('',(1E999,-1E999,nan));\n"
    "ENDSEC;\n"
).encode("utf-8")


class TestStepTextParserNonFinite:
    def test_non_finite_points_never_reach_polygons(self):
        zones, decks, _ = _parse_step_text(STEP_WITH_NON_FINITE)
        assert zones, "Die finiten Punkte müssen weiterhin eine Zone ergeben"
        for zone in zones:
            for point in zone["polygon"]:
                assert all(math.isfinite(c) for c in point), point
        assert all(math.isfinite(d.z_mm) for d in decks)

    def test_geometry_equals_clean_file(self):
        """Die verworfenen Punkte verfälschen die Hülle nicht."""
        clean_zones, _, _ = _parse_step_text(VALID_STEP)
        dirty_zones, _, _ = _parse_step_text(STEP_WITH_NON_FINITE)
        assert dirty_zones[0]["polygon"] == clean_zones[0]["polygon"]

    def test_warning_is_logged(self, caplog):
        with caplog.at_level(logging.WARNING, logger="app.services.cad_import.step_parser"):
            _parse_step_text(STEP_WITH_NON_FINITE)
        assert any(
            "nicht-finiten" in rec.getMessage() for rec in caplog.records
        ), caplog.text

    def test_only_non_finite_points_yields_no_zones(self):
        content = (
            "ISO-10303-21;\n"
            "DATA;\n"
            "#1=CARTESIAN_POINT('',(NaN,NaN,NaN));\n"
            "#2=CARTESIAN_POINT('',(Infinity,0.0,0.0));\n"
            "ENDSEC;\n"
        ).encode("utf-8")
        zones, decks, warnings = _parse_step_text(content)
        assert zones == []
        assert decks == []
        assert any("Keine Koordinaten" in w for w in warnings)

    def test_finite_points_unaffected(self):
        zones, decks, _ = _parse_step_text(VALID_STEP)
        assert len(zones) == 1
        assert len(zones[0]["polygon"]) >= 3
