"""10 Analysis Domains for AYDI.

Maps the 10 yacht system domains to analysis modules, zone types,
component categories, and knowledge base sections.

Every analysis, benchmark, and finding is tagged with its domain.
No domain-agnostic fallbacks — if domain-specific logic is missing,
it must be flagged as a gap, not silently replaced with generic values.
"""

from __future__ import annotations

from enum import Enum
from typing import NamedTuple


class AnalysisDomain(str, Enum):
    """The 10 yacht system analysis domains."""
    HULL_STRUCTURE = "hull_structure"
    RIGGING_SAILS = "rigging_sails"
    PROPULSION_ENGINE = "propulsion_engine"
    ELECTRICAL_ELECTRONICS = "electrical_electronics"
    SANITARY_WATER = "sanitary_water"
    DECK_FITTINGS = "deck_fittings"
    INTERIOR = "interior"
    SAFETY = "safety"
    NAVIGATION = "navigation"
    MAINTENANCE_SERVICE = "maintenance_service"


class DomainConfig(NamedTuple):
    """Configuration for a single analysis domain."""
    i18n_key: str
    zone_types: frozenset[str]
    component_categories: frozenset[str]
    relevant_modules: frozenset[str]  # Analysis module names
    knowledge_prefixes: frozenset[str]  # Knowledge base file prefixes
    iso_standards: frozenset[str]
    critical_checks: list[str]


# ---------------------------------------------------------------------------
# Domain configurations
# ---------------------------------------------------------------------------

DOMAIN_CONFIGS: dict[AnalysisDomain, DomainConfig] = {
    AnalysisDomain.HULL_STRUCTURE: DomainConfig(
        i18n_key="domain.hull_structure",
        zone_types=frozenset({"hull", "keel", "rudder", "bulkhead", "frame", "transom"}),
        component_categories=frozenset({
            "hull_laminate", "keel_bolt", "rudder_bearing", "hull_fitting",
            "gelcoat", "fairing", "osmosis_barrier", "structural_bulkhead",
        }),
        relevant_modules=frozenset({"structural", "materials", "compliance", "production"}),
        knowledge_prefixes=frozenset({"04_", "hull_construction"}),
        iso_standards=frozenset({"ISO 12217", "ISO 12215"}),
        critical_checks=[
            "osmosis_inspection", "keel_bolt_check", "hull_thickness",
            "gelcoat_condition", "delamination_check", "rudder_play",
            "structural_integrity", "blister_inspection",
        ],
    ),

    AnalysisDomain.RIGGING_SAILS: DomainConfig(
        i18n_key="domain.rigging_sails",
        zone_types=frozenset({"mast", "rigging", "deck_hardware", "sail_storage"}),
        component_categories=frozenset({
            "mast", "boom", "shroud", "forestay", "backstay",
            "spreader", "turnbuckle", "chainplate", "halyard",
            "sheet", "block", "winch", "furler", "sail",
            "spinnaker_pole", "vang", "traveler",
        }),
        relevant_modules=frozenset({"structural", "materials", "production", "cost"}),
        knowledge_prefixes=frozenset({"06_rigg"}),
        iso_standards=frozenset({"ISO 12215-9"}),
        critical_checks=[
            "rigging_fatigue", "swage_fitting_condition", "chainplate_corrosion",
            "mast_step_condition", "spreader_alignment", "sail_uv_damage",
            "furler_drum_wear", "block_sheave_wear", "halyard_chafe",
        ],
    ),

    AnalysisDomain.PROPULSION_ENGINE: DomainConfig(
        i18n_key="domain.propulsion_engine",
        zone_types=frozenset({"engine", "engine_room", "fuel_tank", "shaft_tunnel"}),
        component_categories=frozenset({
            "diesel_engine", "saildrive", "shaft", "propeller", "gearbox",
            "fuel_filter", "fuel_tank", "fuel_line", "exhaust_system",
            "raw_water_pump", "coolant_system", "engine_mount",
            "throttle_cable", "alternator", "starter_motor",
        }),
        relevant_modules=frozenset({"structural", "materials", "cost", "service_patterns", "compliance"}),
        knowledge_prefixes=frozenset({"06_antrieb", "06_kuehl"}),
        iso_standards=frozenset({"ISO 9094", "ISO 10088", "ISO 8665"}),
        critical_checks=[
            "engine_hours", "oil_analysis", "coolant_condition",
            "raw_water_pump_impeller", "exhaust_elbow_corrosion",
            "shaft_alignment", "cutlass_bearing_wear", "propeller_condition",
            "fuel_system_integrity", "engine_mount_condition",
            "saildrive_seal", "gearbox_oil",
        ],
    ),

    AnalysisDomain.ELECTRICAL_ELECTRONICS: DomainConfig(
        i18n_key="domain.electrical_electronics",
        zone_types=frozenset({"electrical_panel", "battery_compartment", "charger_area"}),
        component_categories=frozenset({
            "battery_bank", "charger", "inverter", "solar_panel",
            "wind_generator", "shore_power", "circuit_breaker",
            "fuse_panel", "wiring", "bus_bar", "battery_switch",
            "battery_monitor", "voltage_regulator", "led_lighting",
            "nmea2000_backbone", "signalk_server",
        }),
        relevant_modules=frozenset({"compliance", "materials", "cost", "service_patterns"}),
        knowledge_prefixes=frozenset({"06_elektrik"}),
        iso_standards=frozenset({"ISO 10133", "ISO 13297", "ISO 10239"}),
        critical_checks=[
            "battery_capacity", "charge_balance", "wiring_gauge",
            "circuit_protection", "grounding", "galvanic_isolation",
            "cable_routing", "terminal_corrosion", "panel_labeling",
            "load_calculation", "solar_output", "shore_power_safety",
        ],
    ),

    AnalysisDomain.SANITARY_WATER: DomainConfig(
        i18n_key="domain.sanitary_water",
        zone_types=frozenset({"head", "shower", "water_tank", "holding_tank"}),
        component_categories=frozenset({
            "freshwater_tank", "watermaker", "water_pump", "accumulator_tank",
            "water_heater", "seacock", "through_hull", "hose",
            "hose_clamp", "toilet", "holding_tank", "y_valve",
            "macerator", "shower_sump", "deck_fill", "vent",
        }),
        relevant_modules=frozenset({"compliance", "materials", "cost", "service_patterns"}),
        knowledge_prefixes=frozenset({"06_sanitaer"}),
        iso_standards=frozenset({"ISO 8099", "ISO 9093", "ISO 15084"}),
        critical_checks=[
            "seacock_operation", "hose_condition", "hose_clamp_double",
            "through_hull_material", "tank_integrity", "pump_operation",
            "watermaker_membrane", "toilet_seal", "holding_tank_vent",
            "freshwater_quality",
        ],
    ),

    AnalysisDomain.DECK_FITTINGS: DomainConfig(
        i18n_key="domain.deck_fittings",
        zone_types=frozenset({"cockpit", "foredeck", "side_deck", "swim_platform", "flybridge"}),
        component_categories=frozenset({
            "cleat", "winch", "anchor_windlass", "anchor_chain",
            "anchor", "stanchion", "lifeline", "pulpit",
            "hatch", "portlight", "window", "hatch_seal",
            "window_seal", "teak_deck", "non_skid", "davit",
            "bimini", "dodger", "sprayhood",
        }),
        relevant_modules=frozenset({"materials", "compliance", "production", "cost", "ergonomics"}),
        knowledge_prefixes=frozenset({"01_", "05_", "06_deck"}),
        iso_standards=frozenset({"ISO 15085", "ISO 12216", "ISO 11812", "ISO 15584"}),
        critical_checks=[
            "hatch_seal_condition", "window_seal_condition",
            "stanchion_base_corrosion", "lifeline_tension",
            "windlass_operation", "teak_caulking", "cleat_bolt_condition",
            "non_skid_effectiveness", "drain_function", "railing_height",
        ],
    ),

    AnalysisDomain.INTERIOR: DomainConfig(
        i18n_key="domain.interior",
        zone_types=frozenset({
            "cabin", "saloon", "pantry", "storage", "workshop",
            "forepeak", "aft_cabin", "quarter_berth",
        }),
        component_categories=frozenset({
            "berth", "mattress", "cushion", "upholstery",
            "joinery", "cabinet", "drawer", "locker",
            "galley_stove", "oven", "refrigerator", "sink",
            "faucet", "countertop", "flooring", "headliner",
            "ventilation_hatch", "dorade_vent", "insulation",
            "curtain", "blind", "table", "chart_table",
        }),
        relevant_modules=frozenset({"ergonomics", "volume_storage", "emotional", "materials", "production"}),
        knowledge_prefixes=frozenset({"06_innen", "craftsmanship_wood"}),
        iso_standards=frozenset({"ISO 9094", "ISO 11105"}),
        critical_checks=[
            "joinery_tolerance", "drawer_operation", "locker_retention",
            "ventilation_adequacy", "insulation_condition",
            "upholstery_mold", "stove_safety", "galley_ergonomics",
            "berth_dimensions", "headroom",
        ],
    ),

    AnalysisDomain.SAFETY: DomainConfig(
        i18n_key="domain.safety",
        zone_types=frozenset({"safety_locker", "liferaft_storage", "fire_station"}),
        component_categories=frozenset({
            "liferaft", "life_jacket", "harness", "tether",
            "jackline", "fire_extinguisher", "fire_blanket",
            "smoke_detector", "co_detector", "bilge_pump",
            "manual_bilge_pump", "float_switch", "epirb",
            "personal_locator_beacon", "flare", "dan_buoy",
            "horseshoe_buoy", "lightning_protection", "first_aid",
        }),
        relevant_modules=frozenset({"compliance", "service_patterns", "cost"}),
        knowledge_prefixes=frozenset({"06_sicherheit"}),
        iso_standards=frozenset({
            "ISO 9094", "ISO 15085", "ISO 12217",
            "ISO 9650", "ISO 12402", "SOLAS",
        }),
        critical_checks=[
            "liferaft_service_date", "flare_expiry", "epirb_battery",
            "fire_extinguisher_inspection", "bilge_pump_test",
            "jackline_condition", "harness_webbing",
            "smoke_detector_battery", "co_detector_function",
            "man_overboard_equipment",
        ],
    ),

    AnalysisDomain.NAVIGATION: DomainConfig(
        i18n_key="domain.navigation",
        zone_types=frozenset({"helm", "nav_station", "flybridge_helm"}),
        component_categories=frozenset({
            "chart_plotter", "autopilot", "autopilot_drive",
            "radar", "ais_transponder", "ais_receiver",
            "vhf_radio", "ssb_radio", "satellite_phone",
            "wind_instrument", "speed_log", "depth_sounder",
            "compass", "gps_antenna", "radar_reflector",
            "navigation_light", "horn", "bell",
        }),
        relevant_modules=frozenset({"compliance", "cost", "service_patterns"}),
        knowledge_prefixes=frozenset({"06_navigation"}),
        iso_standards=frozenset({"ISO 16147", "ISO 8729", "COLREG"}),
        critical_checks=[
            "compass_deviation", "gps_accuracy", "radar_function",
            "ais_transmission", "vhf_test", "autopilot_calibration",
            "navigation_lights", "depth_sounder_calibration",
            "wind_instrument_calibration", "chart_update_status",
        ],
    ),

    AnalysisDomain.MAINTENANCE_SERVICE: DomainConfig(
        i18n_key="domain.maintenance_service",
        zone_types=frozenset({"service_area", "maintenance_hatch", "boatyard"}),  # Maintenance-specific zones
        component_categories=frozenset({
            "antifouling", "zinc_anode", "engine_oil", "gear_oil",
            "coolant", "impeller", "fuel_filter", "oil_filter",
            "air_filter", "v_belt", "seal_kit", "grease_fitting",
            "bottom_paint", "wax", "teak_oil", "varnish",
        }),
        relevant_modules=frozenset({"service_patterns", "materials", "cost"}),
        knowledge_prefixes=frozenset({"03_", "aging_lifecycle"}),
        iso_standards=frozenset(set()),  # Maintenance follows manufacturer specs
        critical_checks=[
            "antifouling_condition", "zinc_anode_consumption",
            "oil_change_interval", "impeller_age", "belt_condition",
            "winterization_status", "bottom_paint_thickness",
            "service_log_completeness", "manufacturer_recall_check",
            "survey_due_date",
        ],
    ),
}


# ---------------------------------------------------------------------------
# Domain lookup utilities
# ---------------------------------------------------------------------------

def get_domain_for_zone_type(zone_type: str) -> AnalysisDomain | None:
    """Find which domain a zone type belongs to.

    Returns None if the zone type is not mapped to any domain.
    """
    zone_type_lower = zone_type.lower().strip()
    for domain, config in DOMAIN_CONFIGS.items():
        if zone_type_lower in config.zone_types:
            return domain
    return None


def get_domain_for_component(component_category: str) -> AnalysisDomain | None:
    """Find which domain a component category belongs to."""
    cat_lower = component_category.lower().strip()
    for domain, config in DOMAIN_CONFIGS.items():
        if cat_lower in config.component_categories:
            return domain
    return None


def get_domains_for_module(module_name: str) -> list[AnalysisDomain]:
    """Find which domains an analysis module contributes to."""
    return [
        domain
        for domain, config in DOMAIN_CONFIGS.items()
        if module_name in config.relevant_modules
    ]


def get_all_zone_types() -> set[str]:
    """Return all known zone types across all domains."""
    result: set[str] = set()
    for config in DOMAIN_CONFIGS.values():
        result |= config.zone_types
    return result


def get_all_component_categories() -> set[str]:
    """Return all known component categories across all domains."""
    result: set[str] = set()
    for config in DOMAIN_CONFIGS.values():
        result |= config.component_categories
    return result


def get_critical_checks(domain: AnalysisDomain) -> list[str]:
    """Get the critical inspection checks for a domain."""
    return DOMAIN_CONFIGS[domain].critical_checks


def get_domain_coverage_report(
    available_data: dict[str, bool],
) -> dict[str, dict[str, bool]]:
    """Generate a coverage report showing which domains have data.

    Args:
        available_data: Dict of zone_type/component -> bool (has data).

    Returns:
        Dict of domain -> {zone_types: bool, components: bool, overall: bool}
    """
    report = {}
    for domain, config in DOMAIN_CONFIGS.items():
        has_zones = any(
            available_data.get(zt, False) for zt in config.zone_types
        )
        has_components = any(
            available_data.get(cc, False) for cc in config.component_categories
        )
        report[domain.value] = {
            "has_zone_data": has_zones,
            "has_component_data": has_components,
            "can_analyze": has_zones or has_components,
        }
    return report
