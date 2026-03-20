"""Seed script with example yacht projects.

Run with: PYTHONPATH=. python -m app.db.seed
"""
import asyncio
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import async_session, engine
from app.models.models import Base, Layout, Project

logger = logging.getLogger(__name__)


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
     "height_mm": 2200,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"has_railing": True, "material_count": 3}},
    {"name": "salon", "zone_type": "salon",
     "polygon": [[0, 2500], [3800, 2500], [3800, 5500], [0, 5500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.30, "material_count": 5, "furniture_area_pct": 0.45}},
    {"name": "pantry", "zone_type": "pantry",
     "polygon": [[0, 5500], [1800, 5500], [1800, 7500], [0, 7500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.12, "material_count": 4, "furniture_area_pct": 0.55}},
    {"name": "helm", "zone_type": "helm",
     "polygon": [[1800, 5500], [3800, 5500], [3800, 7500], [1800, 7500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": 230,
     "properties": {"material_count": 3}},
    {"name": "fwd_cabin", "zone_type": "cabin",
     "polygon": [[500, 7500], [3300, 7500], [3300, 10000], [500, 10000]],
     "height_mm": 1900,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.18, "material_count": 4, "furniture_area_pct": 0.50}},
    # Intentionally overlaps with cockpit — demonstrates suboptimal layout
    {"name": "aft_cabin", "zone_type": "cabin",
     "polygon": [[0, 0], [1800, 0], [1800, 2000], [0, 2000]],
     "height_mm": 1850,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.10, "material_count": 3, "furniture_area_pct": 0.48}},
    {"name": "head", "zone_type": "head",
     "polygon": [[3300, 7500], [3800, 7500], [3800, 9000], [3300, 9000]],
     "height_mm": 1900,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.05, "material_count": 3, "furniture_area_pct": 0.35}},
    {"name": "engine_room", "zone_type": "engine",
     "polygon": [[1800, 0], [3800, 0], [3800, 1500], [1800, 1500]],
     "height_mm": 1500,
     "is_crew_area": True, "is_guest_area": False, "visibility_angle": None,
     "properties": {"material_count": 2}},
    {"name": "storage_aft", "zone_type": "storage",
     "polygon": [[0, 2000], [1000, 2000], [1000, 2500], [0, 2500]],
     "height_mm": 1200,
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": None,
     "properties": {"furniture_area_pct": 0.80}},
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

        await seed_community_data(session)


async def seed_community_data(db):
    """Seed realistic community reports and run aggregation."""
    from app.models.models import CommunityReport, CommunityPattern
    from app.services.community.aggregator import aggregate_reports_to_patterns

    # Check if data already exists
    result = await db.execute(select(CommunityReport).limit(1))
    if result.scalar_one_or_none():
        logger.info("Community data already seeded")
        return

    reports_data = [
        # Bavaria 38 — Osmose (5 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Osmoseblasen am Unterwasserschiff",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.8 + i * 0.02,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
            "boote-forum.de", "sailboatowners.com",
        ])],

        # Bavaria 38 — Hull/deck fastener loosening (4 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Rumpf/Deck-Verschraubung lockert nach 5-8 Jahren",
                "severity": "major",
                "boat_age_months": 60 + i * 6,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.05,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com", "boote-forum.de",
        ])],

        # Hanse 415 — Railing loosening (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2017,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Relingstützen lockern sich nach 3-5 Jahren",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de", "myhanse.com",
        ])],

        # Hanse 415 — Galley countertop (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2018,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "galley",
                "description": "Arbeitsplatten splittern an Kanten",
                "severity": "cosmetic",
                "boat_age_months": 12 + i * 6,
            }],
            "positives": [],
            "reliability": 0.65,
        } for i, forum in enumerate([
            "myhanse.com", "boote-forum.de", "segeln-forum.de",
        ])],

        # Hallberg-Rassy 40 — Positive: keel (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "40",
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Kielstruktur direkt laminiert — von Gutachtern besser bewertet als modular",
            }],
            "reliability": 0.9,
        } for forum in [
            "segeln-forum.de", "cruisersforum.com", "ybw.com",
        ]],

        # Cross-manufacturer GRP hand_layup — Print-through (4 reports from 3+ mfrs)
        *[{
            "source_forum": "boote-forum.de",
            "boat_manufacturer": mfr,
            "boat_model": None,
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Print-through der Gewebestruktur sichtbar",
                "severity": "cosmetic",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, mfr in enumerate([
            "Bavaria", "Hanse", "Jeanneau", "Dufour",
        ])],

        # Jeanneau Sun Odyssey — Chainplate cracks (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 410",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "rigging",
                "description": "Haarrisse an Wantenplatten nach 8-12 Jahren",
                "severity": "critical",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.85,
        } for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Bavaria general — Positive: price/value (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": None,
            "boat_year": None,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "design_flaw",
                "zone_type": "cabin",
                "description": "Gutes Preis-Leistungs-Verhältnis für Innenraum und Ausstattung",
            }],
            "reliability": 0.7,
        } for forum in [
            "boote-forum.de", "segeln-forum.de", "boote-forum.de",
        ]],
    ]

    # Insert reports
    for rd in reports_data:
        report = CommunityReport(**rd)
        db.add(report)
    await db.flush()

    # Run aggregation
    all_reports = (await db.execute(select(CommunityReport))).scalars().all()
    report_dicts = [{
        "id": r.id,
        "boat_manufacturer": r.boat_manufacturer,
        "boat_model": r.boat_model,
        "hull_material": r.hull_material,
        "hull_construction": r.hull_construction,
        "propulsion": r.propulsion,
        "issues": r.issues or [],
        "positives": r.positives or [],
        "reliability": r.reliability,
    } for r in all_reports]

    pattern_dicts = aggregate_reports_to_patterns(report_dicts)
    for pd in pattern_dicts:
        pattern = CommunityPattern(
            manufacturer=pd["manufacturer"],
            boat_model=pd["boat_model"],
            issue_category=pd["issue_category"],
            zone_type=pd["zone_type"],
            description=pd["description"],
            report_count=pd["report_count"],
            severity_mode=pd["severity_mode"],
            typical_onset_years=pd["typical_onset_years"],
            materials_involved=pd["materials_involved"],
            construction_methods_involved=pd["construction_methods_involved"],
            confidence=pd["confidence"],
            source_report_ids=pd["source_report_ids"],
            is_positive=pd.get("is_positive", False),
        )
        db.add(pattern)

    await db.commit()
    logger.info(f"Seeded {len(reports_data)} community reports → {len(pattern_dicts)} patterns")


if __name__ == "__main__":
    asyncio.run(seed())
