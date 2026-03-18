"""Seed script with example yacht projects.

Run with: PYTHONPATH=. python -m app.db.seed
"""
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import async_session, engine
from app.models.models import Base, Layout, Project


SEED_PROJECTS = [
    {
        "name": "Meridian 40 Cruiser",
        "description": "12m Fahrtensegler mit optimiertem Innenraumlayout für Langfahrt",
        "boat_class": "cruising_sail",
        "length_m": 12.2,
        "beam_m": 3.8,
        "status": "active",
    },
    {
        "name": "Nordic 28 Weekender",
        "description": "Kompakte Segelyacht für Wochenendtörns",
        "boat_class": "small_sail",
        "length_m": 8.5,
        "beam_m": 2.8,
        "status": "draft",
    },
    {
        "name": "Avalon 65 Flybridge",
        "description": "Große Motoryacht mit Flybridge und Crewbereich",
        "boat_class": "large_motor",
        "length_m": 19.8,
        "beam_m": 5.2,
        "status": "draft",
    },
]

MERIDIAN_ZONES = [
    {"name": "cockpit", "zone_type": "cockpit",
     "polygon": [[0, 0], [3800, 0], [3800, 2500], [0, 2500]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    {"name": "salon", "zone_type": "salon",
     "polygon": [[0, 2500], [3800, 2500], [3800, 5500], [0, 5500]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    {"name": "pantry", "zone_type": "pantry",
     "polygon": [[0, 5500], [1800, 5500], [1800, 7500], [0, 7500]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    {"name": "helm", "zone_type": "helm",
     "polygon": [[1800, 5500], [3800, 5500], [3800, 7500], [1800, 7500]],
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": 230},
    {"name": "fwd_cabin", "zone_type": "cabin",
     "polygon": [[500, 7500], [3300, 7500], [3300, 10000], [500, 10000]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    # Intentionally overlaps with cockpit — demonstrates suboptimal layout
    {"name": "aft_cabin", "zone_type": "cabin",
     "polygon": [[0, 0], [1800, 0], [1800, 2000], [0, 2000]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    {"name": "head", "zone_type": "head",
     "polygon": [[3300, 7500], [3800, 7500], [3800, 9000], [3300, 9000]],
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None},
    {"name": "engine_room", "zone_type": "engine",
     "polygon": [[1800, 0], [3800, 0], [3800, 1500], [1800, 1500]],
     "is_crew_area": True, "is_guest_area": False, "visibility_angle": None},
    {"name": "storage_aft", "zone_type": "storage",
     "polygon": [[0, 2000], [1000, 2000], [1000, 2500], [0, 2500]],
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": None},
]

MERIDIAN_PASSAGES = [
    {"from_zone": "cockpit", "to_zone": "salon", "width_mm": 750, "is_primary": True},
    {"from_zone": "salon", "to_zone": "pantry", "width_mm": 700, "is_primary": True},
    {"from_zone": "salon", "to_zone": "helm", "width_mm": 700, "is_primary": True},
    {"from_zone": "helm", "to_zone": "fwd_cabin", "width_mm": 650, "is_primary": True},
    {"from_zone": "fwd_cabin", "to_zone": "head", "width_mm": 600, "is_primary": False},
    {"from_zone": "cockpit", "to_zone": "aft_cabin", "width_mm": 550, "is_primary": True},
    {"from_zone": "cockpit", "to_zone": "engine_room", "width_mm": 500, "is_primary": False},
    {"from_zone": "cockpit", "to_zone": "storage_aft", "width_mm": 650, "is_primary": False},
]


async def seed():
    async with async_session() as session:
        result = await session.execute(select(Project))
        if result.scalars().first():
            print("Seed data already exists, skipping.")
            return

        projects = []
        for data in SEED_PROJECTS:
            project = Project(**data)
            session.add(project)
            projects.append(project)

        await session.flush()

        meridian = projects[0]
        layout = Layout(
            project_id=meridian.id,
            name="Hauptdeck v1.0",
            version="v1.0",
            file_type="json",
            zones=MERIDIAN_ZONES,
            passages=MERIDIAN_PASSAGES,
            deck_height_mm=1950,
        )
        session.add(layout)

        await session.commit()
        print(f"Seeded {len(projects)} projects and 1 layout.")


if __name__ == "__main__":
    asyncio.run(seed())
