"""Shared fixture builder for pillar-4 stage-2 HTTP tests (orgs, invitations,
effective tier). Uses the established dependency-override pattern; crucially the
current-user override attaches ``effective_tier`` via resolve_effective_tier so
tier gating behaves exactly as in production.
"""
import asyncio

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.main import app
from app.db.database import get_db
from app.core.permissions import get_current_user, resolve_effective_tier
from app.models.models import Base, Layout, Project, User

ZONES = [
    {"name": "Salon", "zone_type": "salon", "polygon": [[0, 0], [4000, 0], [4000, 3000], [0, 3000]]},
]


def make_ctx(tmp_path, seed_extra=None):
    """Return (client, ids, current). ``seed_extra(session, ids)`` may add rows."""
    engine = create_async_engine(f"sqlite+aiosqlite:///{tmp_path}", poolclass=NullPool)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def _seed():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        async with session_factory() as session:
            users = {}
            # roles/tiers: elena=enterprise personal, others free personal
            specs = {
                "elena": ("free", "user"),
                "sarah": ("free", "user"),
                "hans": ("free", "user"),      # org member
                "stranger": ("free", "user"),  # no org
                "admin": ("free", "admin"),    # platform admin
            }
            for key, (tier, role) in specs.items():
                u = User(
                    email=f"{key}@yard.example", hashed_password="x",
                    full_name=key.capitalize(), role=role, tier=tier,
                )
                users[key] = u
            session.add_all(users.values())
            await session.flush()

            # Elena's private project (no org yet)
            project = Project(
                user_id=users["elena"].id, name="Werftprojekt", description="",
                boat_class="cruising_sail", length_m=12.0, beam_m=4.0, status="active",
            )
            session.add(project)
            await session.flush()
            layout = Layout(
                project_id=project.id, name="Deck", version="v1.0",
                file_type="json", zones=ZONES, passages=[], deck_height_mm=1950,
            )
            session.add(layout)
            await session.flush()

            ids = {
                **{k: u.id for k, u in users.items()},
                "project": project.id,
                "layout": layout.id,
            }
            if seed_extra:
                await seed_extra(session, ids)
            await session.commit()
            return ids

    ids = asyncio.run(_seed())
    current = {"user_id": ids["elena"]}

    async def override_get_db():
        async with session_factory() as session:
            yield session

    async def override_get_current_user():
        async with session_factory() as session:
            user = await session.get(User, current["user_id"])
            # Mirror production: attach the effective tier for gate reads.
            user.effective_tier = await resolve_effective_tier(user, session)
            return user

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user
    client = TestClient(app)
    return client, ids, current, session_factory
