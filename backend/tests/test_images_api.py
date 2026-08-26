"""HTTP-Tests für die Bild-Routen (Pipeline B).

Deckt die Audit-Befunde ab:

* ROB-7  — ``/quick-analysis/{id}/images`` rief den synchronen Analyzer-Wrapper
  direkt im laufenden Event-Loop auf. Dessen ``asyncio.run`` wirft dort einen
  ``RuntimeError``, der in ``_try_visual_analysis`` verschluckt wurde: die Route
  antwortete 201, Pipeline B lief aber nie.
* ROB-8  — fehlgeschlagene Analysen wurden mit ``ai_analysis_version='1.0'``
  gespeichert, obwohl nie ein Modell gelaufen ist.
* SEC-4  — die visuelle Analyse (PRO-Feature ``VISUAL_ANALYSIS``) war an diesen
  Routen nicht tarif-gegated.
* SEC-12 — Uploads an eine Schnellanalyse prüften keinerlei Bezug zwischen
  Aufrufer und Schnellanalyse.

Die Tests ersetzen den prozessweiten ``VisualAnalyzer`` durch ein Fake-Objekt;
es wird also nie die echte Claude-Vision-API aufgerufen.
"""

import asyncio
import io

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.api.routes import images as images_routes
from app.core.permissions import get_current_user
from app.db.database import get_db
from app.main import app
from app.models.models import Base, Project, QuickAnalysisResult, User
from app.services.visual import analyzer as analyzer_mod


def _png_bytes(size: int = 16) -> bytes:
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (size, size), (12, 34, 56)).save(buf, format="PNG")
    return buf.getvalue()


def _upload_files():
    return {"file": ("test.png", _png_bytes(), "image/png")}


class _FakeAnalyzer:
    """Stand-in for VisualAnalyzer — records calls, never touches the API."""

    def __init__(self):
        self.calls: list[dict] = []
        self.mode = "success"

    async def analyze_image(
        self,
        image_path: str,
        image_type: str,
        boat_class: str,
        zone_type: str | None = None,
        analysis_depth: str = "standard",
        context: dict | None = None,
        boat_dna: object | None = None,
    ) -> dict:
        # Ensures the call really happens off the request event loop.
        await asyncio.sleep(0)
        self.calls.append(
            {"image_path": image_path, "image_type": image_type, "boat_class": boat_class}
        )
        if self.mode == "error":
            return {
                "image_path": image_path,
                "image_type": image_type,
                "analysis": None,
                "confidence": {"level": "visual_insufficient", "is_usable": False},
                "score": None,
                "error": "API vorübergehend nicht verfügbar",
            }
        return {
            "image_path": image_path,
            "image_type": image_type,
            "boat_class": boat_class,
            "model_used": "fake-vision-model",
            "analysis": {
                "findings": [],
                "positive_aspects": ["Saubere Verarbeitung"],
                "concerns": [],
                "recommendations": [],
            },
            "confidence": {"level": "visual_high", "is_usable": True},
            "score": 77.0,
        }


@pytest.fixture(scope="module")
def ctx(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("images_api")
    db_path = tmp / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            pro = User(
                email="pro@img.example", hashed_password="x",
                full_name="Pro", role="user", tier="pro",
            )
            free = User(
                email="free@img.example", hashed_password="x",
                full_name="Free", role="user", tier="free",
            )
            stranger = User(
                email="stranger@img.example", hashed_password="x",
                full_name="Stranger", role="user", tier="pro",
            )
            session.add_all([pro, free, stranger])
            await session.flush()

            project = Project(
                user_id=pro.id, name="Bildboot", description="",
                boat_class="cruising_sail", length_m=11.0, beam_m=3.8,
                status="active",
            )
            project_free = Project(
                user_id=free.id, name="Freiboot", description="",
                boat_class="cruising_sail", length_m=9.0, beam_m=3.0,
                status="active",
            )
            qa = QuickAnalysisResult(
                boat_class="cruising_sail", length_m=11.0,
                specs_input={"boat_class": "cruising_sail", "length_m": 11.0},
                overall_score=61.0, module_results={},
            )
            qa2 = QuickAnalysisResult(
                boat_class="cruising_sail", length_m=11.0,
                specs_input={"boat_class": "cruising_sail", "length_m": 11.0},
                overall_score=61.0, module_results={},
            )
            session.add_all([project, project_free, qa, qa2])
            await session.commit()
            return {
                "pro": pro.id,
                "free": free.id,
                "stranger": stranger.id,
                "project": project.id,
                "project_free": project_free.id,
                "qa": qa.id,
                "qa2": qa2.id,
            }

    ids = asyncio.run(_seed())
    current = {"user_id": ids["pro"]}

    async def override_get_db():
        async with session_factory() as session:
            yield session

    async def override_get_current_user():
        async with session_factory() as session:
            return await session.get(User, current["user_id"])

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user

    fake = _FakeAnalyzer()
    prev_analyzer = analyzer_mod._default_analyzer
    prev_dir = images_routes.UPLOAD_DIR
    analyzer_mod._default_analyzer = fake
    images_routes.UPLOAD_DIR = tmp / "uploads"

    client = TestClient(app)
    yield client, ids, current, fake

    analyzer_mod._default_analyzer = prev_analyzer
    images_routes.UPLOAD_DIR = prev_dir
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def _reset(ctx):
    _client, _ids, current, fake = ctx
    current["user_id"] = _ids["pro"]
    fake.calls.clear()
    fake.mode = "success"
    yield


# ---------------------------------------------------------------------------
# ROB-7 — Pipeline B muss auf ALLEN Upload-Wegen tatsächlich laufen
# ---------------------------------------------------------------------------


def test_quick_analysis_upload_actually_runs_visual_analysis(ctx):
    """ROB-7: der synchrone Wrapper darf nicht im Event-Loop laufen."""
    client, ids, _current, fake = ctx
    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    body = res.json()
    assert len(fake.calls) == 1, "Visuelle Analyse wurde nie ausgeführt"
    assert body["ai_analysis"] is not None
    assert body["ai_analysis"]["score"] == 77.0
    assert body["ai_analysis_version"] == "1.0"


def test_standalone_and_project_upload_run_visual_analysis(ctx):
    client, ids, _current, fake = ctx
    res = client.post(
        "/api/v1/images/analyze",
        files=_upload_files(),
        data={"image_type": "interior_overview", "boat_class": "cruising_sail"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["ai_analysis"]["score"] == 77.0

    res = client.post(
        f"/api/v1/projects/{ids['project']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["ai_analysis"]["score"] == 77.0
    assert len(fake.calls) == 2


# ---------------------------------------------------------------------------
# ROB-8 — keine vorgetäuschte Analyse-Version
# ---------------------------------------------------------------------------


def test_failed_analysis_stores_no_version(ctx):
    """ROB-8: ohne gelaufenes Modell darf keine Version gespeichert werden."""
    client, ids, _current, fake = ctx
    fake.mode = "error"

    res = client.post(
        "/api/v1/images/analyze",
        files=_upload_files(),
        data={"image_type": "interior_overview", "boat_class": "cruising_sail"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["ai_analysis_version"] is None

    res = client.post(
        f"/api/v1/projects/{ids['project']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["ai_analysis_version"] is None

    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["ai_analysis_version"] is None


# ---------------------------------------------------------------------------
# SEC-4 — Tarif-Gate für die visuelle Analyse (PRO)
# ---------------------------------------------------------------------------


def test_free_user_denied_standalone_analysis(ctx):
    client, ids, current, fake = ctx
    current["user_id"] = ids["free"]

    res = client.post(
        "/api/v1/images/analyze",
        files=_upload_files(),
        data={"image_type": "interior_overview", "boat_class": "cruising_sail"},
    )
    assert res.status_code == 403
    detail = res.json()["detail"]
    assert "PRO" in detail and "Bildanalyse" in detail
    assert fake.calls == [], "FREE-Nutzer hat einen Vision-Aufruf ausgelöst"


def test_free_user_denied_batch_analysis(ctx):
    client, ids, current, fake = ctx
    current["user_id"] = ids["free"]

    res = client.post(
        "/api/v1/images/analyze-batch",
        files=[("files", ("a.png", _png_bytes(), "image/png"))],
        data={"boat_class": "cruising_sail"},
    )
    assert res.status_code == 403
    assert "PRO" in res.json()["detail"]
    assert fake.calls == []


def test_free_user_project_upload_is_stored_without_vision_call(ctx):
    """Upload bleibt erlaubt, die kostenpflichtige Analyse nicht."""
    client, ids, current, fake = ctx
    current["user_id"] = ids["free"]

    res = client.post(
        f"/api/v1/projects/{ids['project_free']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    body = res.json()
    assert fake.calls == [], "FREE-Nutzer hat einen Vision-Aufruf ausgelöst"
    assert body["ai_analysis"]["available"] is False
    assert "PRO" in body["ai_analysis"]["reason"]
    assert body["ai_analysis_version"] is None


def test_free_user_quick_analysis_upload_skips_vision(ctx):
    client, ids, current, fake = ctx
    current["user_id"] = ids["free"]

    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa2']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    body = res.json()
    assert fake.calls == [], "FREE-Nutzer hat einen Vision-Aufruf ausgelöst"
    assert body["ai_analysis"]["available"] is False
    assert "PRO" in body["ai_analysis"]["reason"]
    assert body["ai_analysis_version"] is None


# ---------------------------------------------------------------------------
# SEC-12 — Bezug zwischen Aufrufer und Schnellanalyse
# ---------------------------------------------------------------------------


def test_stranger_cannot_attach_image_to_claimed_quick_analysis(ctx):
    client, ids, current, _fake = ctx
    current["user_id"] = ids["pro"]
    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text
    assert res.json()["metadata_extra"]["uploaded_by_user_id"] == str(ids["pro"])

    current["user_id"] = ids["stranger"]
    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 403, res.text
    assert "Schnellanalyse" in res.json()["detail"]

    # Der ursprüngliche Uploader darf weiterhin.
    current["user_id"] = ids["pro"]
    res = client.post(
        f"/api/v1/quick-analysis/{ids['qa']}/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 201, res.text


def test_unknown_quick_analysis_still_404(ctx):
    client, _ids, _current, _fake = ctx
    res = client.post(
        "/api/v1/quick-analysis/00000000-0000-0000-0000-000000000000/images",
        files=_upload_files(),
        data={"image_type": "interior_overview"},
    )
    assert res.status_code == 404
