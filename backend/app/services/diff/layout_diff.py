"""Layout diff service for comparing two yacht layout versions.

Computes a git-style structured diff between two layout dicts, detecting
added, removed, and modified zones and passages.
Pure function module — no database access.
"""
import logging

logger = logging.getLogger(__name__)

# Fields compared per zone (polygon is handled separately due to area calc)
_ZONE_SCALAR_FIELDS = [
    "zone_type",
    "height_mm",
    "is_crew_area",
    "is_guest_area",
    "properties",
]

# Fields compared per passage
_PASSAGE_SCALAR_FIELDS = [
    "width_mm",
    "length_mm",
    "is_primary",
    "points",
]


def _polygon_area(polygon: list[list[float]]) -> float:
    """Compute polygon area in mm² using the shoelace formula.

    Returns 0.0 for degenerate inputs (fewer than 3 vertices).
    """
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


def _compute_zone_changes(zone_a: dict, zone_b: dict) -> list[dict]:
    """Return a list of field-level changes between two zone dicts.

    Each entry has the form::

        {"field": <field_name>, "old": <value_a>, "new": <value_b>}

    For polygon changes an additional ``area_change_sqm`` key is included,
    giving the signed difference (B − A) in square metres.
    """
    changes: list[dict] = []

    for field in _ZONE_SCALAR_FIELDS:
        old_val = zone_a.get(field)
        new_val = zone_b.get(field)
        if old_val != new_val:
            changes.append({"field": field, "old": old_val, "new": new_val})

    poly_a = zone_a.get("polygon") or []
    poly_b = zone_b.get("polygon") or []
    if poly_a != poly_b:
        area_a = _polygon_area(poly_a)
        area_b = _polygon_area(poly_b)
        area_change_sqm = round((area_b - area_a) / 1_000_000, 4)
        changes.append({
            "field": "polygon",
            "old": poly_a,
            "new": poly_b,
            "area_change_sqm": area_change_sqm,
        })

    return changes


def _compute_passage_changes(passage_a: dict, passage_b: dict) -> list[dict]:
    """Return a list of field-level changes between two passage dicts.

    Each entry has the form::

        {"field": <field_name>, "old": <value_a>, "new": <value_b>}
    """
    changes: list[dict] = []
    for field in _PASSAGE_SCALAR_FIELDS:
        old_val = passage_a.get(field)
        new_val = passage_b.get(field)
        if old_val != new_val:
            changes.append({"field": field, "old": old_val, "new": new_val})
    return changes


def compute_layout_diff(
    version_a: dict,
    version_b: dict,
) -> dict:
    """Compare two layout versions and return a structured diff.

    Parameters
    ----------
    version_a:
        Layout dict with keys ``"zones"`` and ``"passages"`` representing the
        baseline (old) version.
    version_b:
        Layout dict with the same shape representing the new version.

    Returns
    -------
    dict
        A structured diff with the following top-level keys:

        * ``zones`` — sub-dict with ``added``, ``removed``, ``modified``,
          and ``unchanged`` lists.
        * ``passages`` — sub-dict with ``added``, ``removed``, and
          ``modified`` lists.
        * ``summary`` — aggregate counts and area change.
    """
    zones_a: dict[str, dict] = {z["name"]: z for z in (version_a.get("zones") or [])}
    zones_b: dict[str, dict] = {z["name"]: z for z in (version_b.get("zones") or [])}

    passages_a: dict[tuple[str, str], dict] = {
        (p["from_zone"], p["to_zone"]): p for p in (version_a.get("passages") or [])
    }
    passages_b: dict[tuple[str, str], dict] = {
        (p["from_zone"], p["to_zone"]): p for p in (version_b.get("passages") or [])
    }

    # --- Zone diff ---
    added_zones: list[dict] = []
    removed_zones: list[dict] = []
    modified_zones: list[dict] = []
    unchanged_zones: list[str] = []

    for name, zone_b in zones_b.items():
        if name not in zones_a:
            added_zones.append({"name": name, "zone": zone_b})
        elif zones_a[name] != zone_b:
            changes = _compute_zone_changes(zones_a[name], zone_b)
            modified_zones.append({"name": name, "changes": changes})
        else:
            unchanged_zones.append(name)

    for name, zone_a in zones_a.items():
        if name not in zones_b:
            removed_zones.append({"name": name, "zone": zone_a})

    # --- Passage diff ---
    added_passages: list[dict] = []
    removed_passages: list[dict] = []
    modified_passages: list[dict] = []

    for key, passage_b in passages_b.items():
        if key not in passages_a:
            added_passages.append({"from_zone": key[0], "to_zone": key[1], "passage": passage_b})
        elif passages_a[key] != passage_b:
            changes = _compute_passage_changes(passages_a[key], passage_b)
            modified_passages.append({"from_zone": key[0], "to_zone": key[1], "changes": changes})

    for key, passage_a in passages_a.items():
        if key not in passages_b:
            removed_passages.append({"from_zone": key[0], "to_zone": key[1], "passage": passage_a})

    # --- Summary statistics ---
    total_area_a = sum(_polygon_area(z.get("polygon") or []) for z in zones_a.values())
    total_area_b = sum(_polygon_area(z.get("polygon") or []) for z in zones_b.values())
    total_area_change_sqm = round((total_area_b - total_area_a) / 1_000_000, 2)

    has_changes = bool(
        added_zones
        or removed_zones
        or modified_zones
        or added_passages
        or removed_passages
        or modified_passages
    )

    return {
        "zones": {
            "added": added_zones,
            "removed": removed_zones,
            "modified": modified_zones,
            "unchanged": unchanged_zones,
        },
        "passages": {
            "added": added_passages,
            "removed": removed_passages,
            "modified": modified_passages,
        },
        "summary": {
            "zones_added": len(added_zones),
            "zones_removed": len(removed_zones),
            "zones_modified": len(modified_zones),
            "zones_unchanged": len(unchanged_zones),
            "passages_added": len(added_passages),
            "passages_removed": len(removed_passages),
            "passages_modified": len(modified_passages),
            "total_area_change_sqm": total_area_change_sqm,
            "has_changes": has_changes,
        },
    }
