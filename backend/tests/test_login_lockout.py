"""Die Anmeldesperre darf sich nicht per Kopfzeile umgehen lassen.

Nach fuenf Fehlversuchen je Absenderadresse antwortet die Anmeldung fuer 15
Minuten mit 429. Der Zaehler haengt an der Adresse, die ``client_ip``
ermittelt — und genau dort lagen nach dem Zusammenfuehren der beiden Zweige
ZWEI Fassungen nebeneinander: die aus ``core/middleware.py`` prueft
``TRUST_PROXY_HEADERS``, bevor sie ``X-Forwarded-For`` glaubt, die aus
``routes/auth.py`` glaubte ihm bedingungslos. Es lief die zweite.

Damit genuegte ein frei gewaehlter ``X-Forwarded-For``-Wert je Anfrage, um
jedes Mal einen frischen Zaehler zu bekommen: die Sperre je Adresse war
wirkungslos, und Passwortraten ueber viele Konten hinweg blieb unbegrenzt.

Diese Tests halten beides fest — dass die Sperre greift, und dass die
Kopfzeile sie nicht aushebelt, solange der Proxy nicht ausdruecklich als
vertrauenswuerdig konfiguriert ist.
"""

import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.auth import hash_password
from app.db.database import get_db
from app.main import app
from app.models.models import Base, User

EMAIL = "sperre@aydi.example"
PASSWORT = "Korrektes-Passwort-9!"


@pytest.fixture
def client(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("lockout") / "test.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _setup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            session.add(
                User(
                    email=EMAIL,
                    hashed_password=hash_password(PASSWORT),
                    full_name="Sperrtest",
                    role="user",
                    tier="free",
                )
            )
            await session.commit()

    asyncio.run(_setup())

    async def _override():
        async with session_factory() as session:
            yield session

    app.dependency_overrides[get_db] = _override
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.pop(get_db, None)


@pytest.fixture(autouse=True)
def _leerer_zaehler():
    """Der Sperrzaehler liegt im Modulzustand — zwischen Tests leeren."""
    from app.api.routes import auth

    auth._failed_logins.clear()
    yield
    auth._failed_logins.clear()


def _anmelden(client, passwort, **kwargs):
    return client.post(
        "/api/v1/auth/login", json={"email": EMAIL, "password": passwort}, **kwargs
    )


def test_sperre_greift_nach_fuenf_fehlversuchen(client):
    for _ in range(5):
        assert _anmelden(client, "falsch").status_code == 401

    gesperrt = _anmelden(client, "falsch")
    assert gesperrt.status_code == 429
    assert "Retry-After" in gesperrt.headers


def test_richtiges_passwort_hilft_waehrend_der_sperre_nicht(client):
    """Sonst waere die Sperre nur eine Bremse fuer Tippfehler."""
    for _ in range(5):
        _anmelden(client, "falsch")

    assert _anmelden(client, PASSWORT).status_code == 429


def test_gefaelschter_forwarded_header_umgeht_die_sperre_nicht(client, monkeypatch):
    """Der Kern: ohne vertrauenswuerdigen Proxy zaehlt der Header nicht.

    Zuvor lief hier die Fassung aus auth.py, die X-Forwarded-For blind
    glaubte — jeder Versuch bekam mit einer neuen erfundenen Adresse einen
    eigenen Zaehler und 429 trat nie ein.
    """
    from app.core import middleware as mw

    monkeypatch.setattr(mw.settings, "TRUST_PROXY_HEADERS", False, raising=False)

    for i in range(5):
        antwort = _anmelden(client, "falsch", headers={"X-Forwarded-For": f"10.0.0.{i}"})
        assert antwort.status_code == 401

    gesperrt = _anmelden(client, "falsch", headers={"X-Forwarded-For": "10.0.0.99"})
    assert gesperrt.status_code == 429, (
        "Eine erfundene Absenderadresse in X-Forwarded-For hat einen frischen "
        "Sperrzaehler verschafft — die Sperre je Adresse ist damit wirkungslos."
    )


def test_hinter_vertrauenswuerdigem_proxy_zaehlt_der_header(client, monkeypatch):
    """Die Kehrseite: auf Render kommt JEDE Anfrage vom selben Proxy.

    Ohne TRUST_PROXY_HEADERS teilen sich dort alle Nutzer einen Zaehler, und
    fuenf Fehlversuche irgendeines Besuchers sperren alle uebrigen aus. Mit
    der Einstellung zaehlt wieder die tatsaechliche Absenderadresse.
    """
    from app.core import middleware as mw

    monkeypatch.setattr(mw.settings, "TRUST_PROXY_HEADERS", True, raising=False)

    for _ in range(5):
        _anmelden(client, "falsch", headers={"X-Forwarded-For": "203.0.113.7"})
    assert _anmelden(client, "falsch", headers={"X-Forwarded-For": "203.0.113.7"}).status_code == 429

    # Eine andere Adresse ist davon nicht betroffen.
    andere = _anmelden(client, "falsch", headers={"X-Forwarded-For": "203.0.113.8"})
    assert andere.status_code == 401
