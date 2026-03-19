"""Estimate a layout from publicly available yacht specifications."""
from typing import Optional


# Beam estimation if not provided: beam ≈ length * factor
BEAM_ESTIMATE_FACTORS = {
    "small_sail": 0.32,
    "cruising_sail": 0.30,
    "large_motor": 0.25,
    "superyacht": 0.22,
}

CLASS_LAYOUT_TEMPLATES = {
    "small_sail": {
        "interior_depth_factor": 0.42,
        "deck_height_mm": 1850,
        "typical_zones": [
            {"name": "Cockpit", "type": "cockpit", "area_pct": 0.22},
            {"name": "Salon", "type": "salon", "area_pct": 0.25},
            {"name": "Pantry", "type": "pantry", "area_pct": 0.08},
            {"name": "Vorschiffskabine", "type": "cabin", "area_pct": 0.12, "per_cabin": True},
            {"name": "Nasszelle", "type": "head", "area_pct": 0.06, "per_head": True},
            {"name": "Steuerstand", "type": "helm", "area_pct": 0.05},
            {"name": "Motorraum", "type": "engine", "area_pct": 0.07},
            {"name": "Stauraum", "type": "storage", "area_pct": 0.10},
        ],
        "typical_passages": [
            {"from": "Cockpit", "to": "Salon", "type": "primary"},
            {"from": "Salon", "to": "Pantry", "type": "primary"},
            {"from": "Salon", "to": "Vorschiffskabine", "type": "primary"},
            {"from": "Salon", "to": "Nasszelle", "type": "primary"},
            {"from": "Cockpit", "to": "Steuerstand", "type": "primary"},
        ],
        "passage_widths": {"primary": 650, "secondary": 550, "service": 500},
        "default_cabins": 1,
        "default_heads": 1,
    },
    "cruising_sail": {
        "interior_depth_factor": 0.45,
        "deck_height_mm": 1950,
        "typical_zones": [
            {"name": "Cockpit", "type": "cockpit", "area_pct": 0.20},
            {"name": "Salon", "type": "salon", "area_pct": 0.22},
            {"name": "Pantry", "type": "pantry", "area_pct": 0.09},
            {"name": "Achterkabine", "type": "cabin", "area_pct": 0.11, "per_cabin": True},
            {"name": "Nasszelle", "type": "head", "area_pct": 0.05, "per_head": True},
            {"name": "Steuerstand", "type": "helm", "area_pct": 0.05},
            {"name": "Motorraum", "type": "engine", "area_pct": 0.06},
            {"name": "Stauraum", "type": "storage", "area_pct": 0.12},
            {"name": "Vorschiff", "type": "foredeck", "area_pct": 0.05},
        ],
        "typical_passages": [
            {"from": "Cockpit", "to": "Salon", "type": "primary"},
            {"from": "Salon", "to": "Pantry", "type": "primary"},
            {"from": "Salon", "to": "Achterkabine", "type": "primary"},
            {"from": "Salon", "to": "Nasszelle", "type": "primary"},
            {"from": "Cockpit", "to": "Steuerstand", "type": "primary"},
            {"from": "Salon", "to": "Motorraum", "type": "secondary"},
        ],
        "passage_widths": {"primary": 750, "secondary": 600, "service": 550},
        "default_cabins": 2,
        "default_heads": 1,
    },
    "large_motor": {
        "interior_depth_factor": 0.50,
        "deck_height_mm": 2050,
        "typical_zones": [
            {"name": "Cockpit", "type": "cockpit", "area_pct": 0.15},
            {"name": "Salon", "type": "salon", "area_pct": 0.20},
            {"name": "Pantry", "type": "pantry", "area_pct": 0.08},
            {"name": "Kabine", "type": "cabin", "area_pct": 0.10, "per_cabin": True},
            {"name": "Nasszelle", "type": "head", "area_pct": 0.04, "per_head": True},
            {"name": "Steuerstand", "type": "helm", "area_pct": 0.06},
            {"name": "Maschinenraum", "type": "engine", "area_pct": 0.08},
            {"name": "Stauraum", "type": "storage", "area_pct": 0.08},
            {"name": "Flybridge", "type": "flybridge", "area_pct": 0.12},
            {"name": "Crew", "type": "crew_quarters", "area_pct": 0.05},
        ],
        "typical_passages": [
            {"from": "Cockpit", "to": "Salon", "type": "primary"},
            {"from": "Salon", "to": "Pantry", "type": "primary"},
            {"from": "Salon", "to": "Kabine", "type": "primary"},
            {"from": "Salon", "to": "Nasszelle", "type": "primary"},
            {"from": "Cockpit", "to": "Flybridge", "type": "primary"},
            {"from": "Salon", "to": "Steuerstand", "type": "primary"},
            {"from": "Maschinenraum", "to": "Crew", "type": "secondary"},
        ],
        "passage_widths": {"primary": 850, "secondary": 700, "service": 600},
        "default_cabins": 3,
        "default_heads": 2,
    },
    "superyacht": {
        "interior_depth_factor": 0.55,
        "deck_height_mm": 2150,
        "typical_zones": [
            {"name": "Cockpit", "type": "cockpit", "area_pct": 0.10},
            {"name": "Salon", "type": "salon", "area_pct": 0.18},
            {"name": "Pantry", "type": "pantry", "area_pct": 0.06},
            {"name": "Gästesuite", "type": "cabin", "area_pct": 0.08, "per_cabin": True},
            {"name": "Gästebad", "type": "head", "area_pct": 0.03, "per_head": True},
            {"name": "Brücke", "type": "helm", "area_pct": 0.05},
            {"name": "Maschinenraum", "type": "engine", "area_pct": 0.07},
            {"name": "Stauraum", "type": "storage", "area_pct": 0.06},
            {"name": "Flybridge", "type": "flybridge", "area_pct": 0.10},
            {"name": "Sky Lounge", "type": "sky_lounge", "area_pct": 0.08},
            {"name": "Beach Club", "type": "beach_club", "area_pct": 0.06},
            {"name": "Crew", "type": "crew_quarters", "area_pct": 0.06},
            {"name": "Tender Garage", "type": "tender_garage", "area_pct": 0.04},
        ],
        "typical_passages": [
            {"from": "Cockpit", "to": "Salon", "type": "primary"},
            {"from": "Salon", "to": "Pantry", "type": "primary"},
            {"from": "Salon", "to": "Gästesuite", "type": "primary"},
            {"from": "Gästesuite", "to": "Gästebad", "type": "primary"},
            {"from": "Cockpit", "to": "Flybridge", "type": "primary"},
            {"from": "Salon", "to": "Sky Lounge", "type": "primary"},
            {"from": "Cockpit", "to": "Beach Club", "type": "primary"},
            {"from": "Maschinenraum", "to": "Crew", "type": "secondary"},
            {"from": "Crew", "to": "Pantry", "type": "service"},
        ],
        "passage_widths": {"primary": 1000, "secondary": 800, "service": 700},
        "default_cabins": 4,
        "default_heads": 3,
    },
}


def estimate_beam(length_m: float, boat_class: str) -> float:
    """Estimate beam from length and boat class if not provided."""
    factor = BEAM_ESTIMATE_FACTORS.get(boat_class, 0.28)
    return round(length_m * factor, 2)


def _generate_rectangle_polygon(
    x_start: float, y_start: float, width: float, height: float
) -> list[list[float]]:
    """Generate a simple rectangular polygon in mm coordinates."""
    return [
        [x_start, y_start],
        [x_start + width, y_start],
        [x_start + width, y_start + height],
        [x_start, y_start + height],
    ]


def estimate_layout_from_specs(
    boat_class: str,
    length_m: float,
    beam_m: Optional[float] = None,
    cabin_count: Optional[int] = None,
    head_count: Optional[int] = None,
    cockpit_area_sqm: Optional[float] = None,
    salon_area_sqm: Optional[float] = None,
    deck_height_mm: Optional[float] = None,
    has_flybridge: Optional[bool] = None,
    has_crew_quarters: Optional[bool] = None,
    storage_volume_l: Optional[float] = None,
    **kwargs,
) -> dict:
    """
    Generate an estimated layout from publicly available specifications.

    Returns dict with:
        zones: list of zone dicts (with estimated polygons)
        passages: list of passage dicts
        deck_height_mm: float
        confidence: "estimated"
        specs_provided: int (count of non-None optional inputs)
        specs_inferred: int (count of inferred values)
    """
    template = CLASS_LAYOUT_TEMPLATES.get(boat_class)
    if not template:
        template = CLASS_LAYOUT_TEMPLATES["cruising_sail"]

    # Estimate beam if not provided
    effective_beam = beam_m if beam_m is not None else estimate_beam(length_m, boat_class)
    effective_deck_height = deck_height_mm if deck_height_mm is not None else template["deck_height_mm"]
    effective_cabins = cabin_count if cabin_count is not None else template["default_cabins"]
    effective_heads = head_count if head_count is not None else template["default_heads"]

    # Count provided vs inferred
    optional_fields = [
        beam_m, cabin_count, head_count, cockpit_area_sqm, salon_area_sqm,
        deck_height_mm, has_flybridge, has_crew_quarters, storage_volume_l,
    ]
    specs_provided = sum(1 for f in optional_fields if f is not None) + 2  # +2 for required boat_class + length_m

    # Calculate total interior area
    total_interior_sqm = length_m * effective_beam * template["interior_depth_factor"]

    # Convert to mm for polygon generation
    beam_mm = effective_beam * 1000

    zones = []
    x_cursor = 0.0  # Track position along length for zone placement
    inferred_count = 0

    for zt in template["typical_zones"]:
        zone_type = zt["type"]

        # Skip flybridge if explicitly not present
        if zone_type == "flybridge" and has_flybridge is False:
            continue
        # Skip crew quarters if explicitly not present
        if zone_type == "crew_quarters" and has_crew_quarters is False:
            continue

        # Determine count (for cabins/heads)
        count = 1
        if zt.get("per_cabin"):
            count = effective_cabins
        elif zt.get("per_head"):
            count = effective_heads

        for i in range(count):
            # Calculate area for this zone
            if zone_type == "cockpit" and cockpit_area_sqm is not None:
                area_sqm = cockpit_area_sqm
            elif zone_type == "salon" and salon_area_sqm is not None:
                area_sqm = salon_area_sqm
            else:
                area_sqm = total_interior_sqm * zt["area_pct"]
                inferred_count += 1

            # Generate simple rectangular polygon
            area_mm2 = area_sqm * 1e6
            zone_width = min(beam_mm * 0.85, (area_mm2 / (beam_mm * 0.6)) if beam_mm > 0 else 2000)
            zone_depth = area_mm2 / zone_width if zone_width > 0 else 2000

            y_offset = (beam_mm - zone_width) / 2  # Center zones
            polygon = _generate_rectangle_polygon(x_cursor, y_offset, zone_depth, zone_width)

            name = zt["name"]
            if count > 1:
                name = f"{zt['name']} {i + 1}"

            zones.append({
                "name": name,
                "zone_type": zone_type,
                "polygon": polygon,
                "height_mm": effective_deck_height,
                "is_crew_area": zone_type in ("crew_quarters",),
                "is_guest_area": zone_type not in ("crew_quarters", "engine", "storage", "technical"),
                "confidence": "estimated",
                "properties": {},
            })

            x_cursor += zone_depth * 0.3  # Overlap zones slightly for realistic spacing

    # Generate passages
    passages = []
    zone_names = {z["name"] for z in zones}
    for pt in template["typical_passages"]:
        from_zone = pt["from"]
        to_zone = pt["to"]

        # Handle numbered zones (e.g., "Kabine 1", "Kabine 2")
        matching_from = [z for z in zone_names if z.startswith(from_zone)]
        matching_to = [z for z in zone_names if z.startswith(to_zone)]

        if not matching_from or not matching_to:
            continue

        # Connect first matching zones
        passages.append({
            "from_zone": matching_from[0],
            "to_zone": matching_to[0],
            "width_mm": template["passage_widths"].get(pt["type"], 700),
            "is_primary": pt["type"] == "primary",
            "confidence": "estimated",
        })

        # For cabins: connect each additional cabin to salon
        if len(matching_to) > 1 and to_zone != from_zone:
            for extra_zone in matching_to[1:]:
                passages.append({
                    "from_zone": matching_from[0],
                    "to_zone": extra_zone,
                    "width_mm": template["passage_widths"].get(pt["type"], 700),
                    "is_primary": pt["type"] == "primary",
                    "confidence": "estimated",
                })

    return {
        "zones": zones,
        "passages": passages,
        "deck_height_mm": effective_deck_height,
        "confidence": "estimated",
        "data_source": "public_specs",
        "specs_provided": specs_provided,
        "specs_inferred": inferred_count,
        "effective_beam_m": effective_beam,
        "effective_length_m": length_m,
    }
