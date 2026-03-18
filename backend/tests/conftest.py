def make_zone(
    name: str,
    zone_type: str,
    polygon: list[list[float]] | None = None,
    is_crew_area: bool = False,
    is_guest_area: bool = False,
    visibility_angle: float | None = None,
) -> dict:
    if polygon is None:
        polygon = [[0, 0], [2000, 0], [2000, 2000], [0, 2000]]
    return {
        "name": name,
        "zone_type": zone_type,
        "polygon": polygon,
        "is_crew_area": is_crew_area,
        "is_guest_area": is_guest_area,
        "visibility_angle": visibility_angle,
    }


def make_passage(
    from_zone: str,
    to_zone: str,
    width_mm: float = 700,
    is_primary: bool = True,
) -> dict:
    return {
        "from_zone": from_zone,
        "to_zone": to_zone,
        "width_mm": width_mm,
        "is_primary": is_primary,
    }
