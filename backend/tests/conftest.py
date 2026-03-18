def make_zone(
    name: str,
    zone_type: str,
    polygon: list[list[float]] | None = None,
    is_crew_area: bool = False,
    is_guest_area: bool = False,
    visibility_angle: float | None = None,
    height_mm: float | None = None,
    properties: dict | None = None,
) -> dict:
    if polygon is None:
        polygon = [[0, 0], [2000, 0], [2000, 2000], [0, 2000]]
    zone = {
        "name": name,
        "zone_type": zone_type,
        "polygon": polygon,
        "is_crew_area": is_crew_area,
        "is_guest_area": is_guest_area,
        "visibility_angle": visibility_angle,
    }
    if height_mm is not None:
        zone["height_mm"] = height_mm
    if properties is not None:
        zone["properties"] = properties
    return zone


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


def make_material(
    name: str = "Test Material",
    category: str = "interior",
    subcategory: str = "wood",
    cost_per_unit: float = 100.0,
    cost_unit: str = "sqm",
    lifespan_years: float = 20.0,
    maintenance_interval_months: int = 12,
    maintenance_cost_factor: float = 0.02,
    known_issues: list[dict] | None = None,
    properties: dict | None = None,
) -> dict:
    return {
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "cost_per_unit": cost_per_unit,
        "cost_unit": cost_unit,
        "lifespan_years": lifespan_years,
        "maintenance_interval_months": maintenance_interval_months,
        "maintenance_cost_factor": maintenance_cost_factor,
        "known_issues": known_issues or [],
        "properties": properties or {},
    }


def make_zone_material(
    zone_name: str = "salon",
    surface_type: str = "floor",
    area_sqm: float = 10.0,
    material: dict | None = None,
) -> dict:
    if material is None:
        material = make_material()
    return {
        "zone_name": zone_name,
        "surface_type": surface_type,
        "area_sqm": area_sqm,
        "material": material,
    }
