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


def make_cost_item(
    category: str = "material",
    subcategory: str | None = None,
    quantity: float = 1.0,
    unit: str = "piece",
    unit_cost_eur: float = 100.0,
    total_cost_eur: float | None = None,
    zone_name: str | None = None,
    source: str = "estimate",
) -> dict:
    """Create a cost item dict for use in cost analysis tests.

    Args:
        category: Cost category — material, labor, equipment, or overhead.
        subcategory: Optional subcategory label (e.g. "GFK-Laminat").
        quantity: Amount of units.
        unit: Unit of measure (e.g. "piece", "sqm", "hour").
        unit_cost_eur: Cost per unit in euros.
        total_cost_eur: Total cost in euros. Defaults to quantity * unit_cost_eur.
        zone_name: Optional associated zone name.
        source: Data source quality — "quote", "contract", "budget", or "estimate".

    Returns:
        Dict representing a single cost item.
    """
    if total_cost_eur is None:
        total_cost_eur = quantity * unit_cost_eur
    item: dict = {
        "category": category,
        "quantity": quantity,
        "unit": unit,
        "unit_cost_eur": unit_cost_eur,
        "total_cost_eur": total_cost_eur,
        "source": source,
    }
    if subcategory is not None:
        item["subcategory"] = subcategory
    if zone_name is not None:
        item["zone_name"] = zone_name
    return item


def make_competitor(
    key_metrics: dict | None = None,
    length_m: float = 12.0,
    price_range_eur: dict | None = None,
) -> dict:
    """Build a competitor dict with sensible defaults for a cruising_sail segment.

    Args:
        key_metrics: Dict of numeric metric values keyed by metric name.
        length_m: Overall boat length in metres.
        price_range_eur: Dict with "min" and "max" keys in EUR.

    Returns:
        Dict representing a single competitor model.
    """
    if key_metrics is None:
        key_metrics = {
            "cockpit_area_sqm": 8.0,
            "salon_area_sqm": 14.0,
            "cabin_count": 2,
            "head_count": 1,
            "berth_count": 4,
            "storage_volume_l": 600.0,
            "deck_height_mm": 1950.0,
        }
    if price_range_eur is None:
        price_range_eur = {"min": 180_000.0, "max": 220_000.0}
    return {
        "key_metrics": key_metrics,
        "length_m": length_m,
        "price_range_eur": price_range_eur,
    }


def make_service_report(
    report_type: str = "maintenance",
    category: str = "interior",
    zone_type: str = "cabin",
    severity: str = "medium",
    description: str = "Test issue",
    boat_age_months: int = 24,
    materials_involved: list[str] | None = None,
    cost_eur: float | None = None,
) -> dict:
    report: dict = {
        "report_type": report_type,
        "category": category,
        "zone_type": zone_type,
        "severity": severity,
        "description": description,
        "boat_age_months": boat_age_months,
        "materials_involved": materials_involved or [],
    }
    if cost_eur is not None:
        report["cost_eur"] = cost_eur
    return report


def make_community_report(
    source_forum="boote-forum.de",
    boat_manufacturer="Bavaria",
    boat_model="38 Cruiser",
    boat_year=2018,
    hull_material="grp_solid",
    hull_construction="hand_layup",
    propulsion="sail",
    issues=None,
    positives=None,
    reliability=0.8,
    source_url=None,
    source_date=None,
    raw_text=None,
):
    if issues is None:
        issues = [{
            "category": "material_degradation",
            "zone_type": "hull",
            "description": "Osmoseblasen am Unterwasserschiff nach 6 Jahren",
            "severity": "major",
            "boat_age_months": 72,
        }]
    return {
        "source_forum": source_forum,
        "source_url": source_url,
        "source_date": source_date,
        "boat_manufacturer": boat_manufacturer,
        "boat_model": boat_model,
        "boat_year": boat_year,
        "hull_material": hull_material,
        "hull_construction": hull_construction,
        "propulsion": propulsion,
        "issues": issues,
        "positives": positives or [],
        "reliability": reliability,
        "raw_text": raw_text,
    }


def make_community_pattern(
    manufacturer="Bavaria",
    boat_model="38 Cruiser",
    issue_category="material_degradation",
    zone_type="hull",
    description="Osmoseblasen am Unterwasserschiff",
    report_count=5,
    severity_mode="major",
    typical_onset_years=6.0,
    materials_involved=None,
    construction_methods_involved=None,
    confidence=0.7,
    source_report_ids=None,
    is_positive=False,
):
    return {
        "manufacturer": manufacturer,
        "boat_model": boat_model,
        "issue_category": issue_category,
        "zone_type": zone_type,
        "description": description,
        "report_count": report_count,
        "severity_mode": severity_mode,
        "typical_onset_years": typical_onset_years,
        "materials_involved": materials_involved or ["grp_solid"],
        "construction_methods_involved": construction_methods_involved or ["hand_layup"],
        "confidence": confidence,
        "source_report_ids": source_report_ids or [1, 2, 3, 4, 5],
        "is_positive": is_positive,
    }
