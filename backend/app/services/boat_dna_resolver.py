"""BoatDNA Resolver — translates BoatDNA profiles into module configs."""
from __future__ import annotations

import copy
import math

from app.models.boat_dna import BoatDNA


class BoatDNAResolver:
    """Translates a BoatDNA profile into concrete analysis parameters."""

    _LEGACY_CONFIGS: dict[str, dict[str, dict]] | None = None

    @classmethod
    def _build_legacy_configs(cls) -> dict[str, dict[str, dict]]:
        from app.services.analysis.ergonomics import BOAT_CLASS_DEFAULTS as ERGO_D
        from app.services.analysis.compliance import BOAT_CLASS_DEFAULTS as COMP_D
        from app.services.analysis.structural import BOAT_CLASS_DEFAULTS as STRUCT_D
        from app.services.analysis.production import BOAT_CLASS_DEFAULTS as PROD_D
        from app.services.analysis.cost import BOAT_CLASS_DEFAULTS as COST_D
        from app.services.analysis.emotional import BOAT_CLASS_DEFAULTS as EMO_D
        from app.services.analysis.materials import BOAT_CLASS_DEFAULTS as MAT_D
        from app.services.analysis.volume_storage import BOAT_CLASS_DEFAULTS as VOL_D
        from app.services.analysis.brand_dna import BOAT_CLASS_DEFAULTS as BRAND_D
        from app.services.analysis.market import BOAT_CLASS_DEFAULTS as MARKET_D
        from app.services.analysis.service_patterns import BOAT_CLASS_DEFAULTS as SVC_D
        from app.services.analysis.community import BOAT_CLASS_DEFAULTS as COMM_D

        module_sources = {
            "ergonomics": ERGO_D, "compliance": COMP_D,
            "structural": STRUCT_D, "production": PROD_D,
            "cost": COST_D, "emotional": EMO_D,
            "materials": MAT_D, "volume_storage": VOL_D,
            "brand_dna": BRAND_D, "market": MARKET_D,
            "service_patterns": SVC_D,
            "community": COMM_D,
        }
        configs: dict[str, dict[str, dict]] = {}
        for boat_class in (
            "small_sail", "cruising_sail", "racing_sail", "daysailer", "motorsailer",
            "catamaran_sail", "catamaran_motor", "small_motor", "large_motor",
            "sport_cruiser", "trawler", "explorer", "superyacht"
        ):
            configs[boat_class] = {}
            for module_name, defaults in module_sources.items():
                if boat_class in defaults:
                    configs[boat_class][module_name] = defaults[boat_class]
        return configs

    @classmethod
    def _get_legacy_configs(cls) -> dict[str, dict[str, dict]]:
        if cls._LEGACY_CONFIGS is None:
            cls._LEGACY_CONFIGS = cls._build_legacy_configs()
        return cls._LEGACY_CONFIGS

    def resolve(self, dna: BoatDNA) -> dict[str, dict]:
        if dna._legacy_class:
            result = copy.deepcopy(self._get_legacy_configs()[dna._legacy_class])
            result["overall_weights"] = self._resolve_overall_weights(dna)
            return result
        return self._resolve_custom(dna)

    def resolve_and_validate(self, dna: BoatDNA) -> dict[str, dict]:
        result = self.resolve(dna)
        for module_name, config in result.items():
            if module_name == "overall_weights":
                total = sum(config.values())
                assert abs(total - 1.0) < 1e-9, f"overall_weights sum={total}"
                continue
            weights = config.get("weights", {})
            if weights:
                total = sum(weights.values())
                assert abs(total - 1.0) < 1e-9, (
                    f"{module_name} weights sum={total}"
                )
        return result

    # ------------------------------------------------------------------
    # Overall module weights
    # ------------------------------------------------------------------

    def _resolve_overall_weights(self, dna: BoatDNA) -> dict[str, float]:
        """Generate overall module weights based on DNA profile."""
        is_sail = dna.propulsion in ("sail", "sail_motor")
        is_performance = dna.primary_use in ("racing", "racing_cruiser")
        is_luxury = dna.builder_quality_tier in ("luxury", "superyacht")
        is_cruising = dna.primary_use in (
            "coastal_cruising", "offshore_cruising", "bluewater",
        )

        w = {
            "ergonomics": 0.15 + (0.05 if is_performance else 0.0) - (0.03 if is_luxury else 0.0),
            "volume_storage": 0.10 + (0.05 if is_cruising else 0.0) - (0.05 if is_luxury else 0.0),
            "emotional": 0.15 + (0.10 if is_luxury else 0.0) - (0.05 if is_performance else 0.0),
            "compliance": 0.12 + (0.03 if dna.operating_waters in ("offshore", "ocean") else 0.0),
            "production": 0.10,
            "materials": 0.12 + (0.03 if is_luxury else 0.0),
            "structural": 0.08 + (0.02 if is_sail else 0.0),
            "cost": 0.08 + (0.02 if dna.production_type == "mass_production" else 0.0),
        }
        if dna.length_m > 12 or dna.builder_quality_tier in ("premium", "luxury", "superyacht"):
            w["brand_dna"] = 0.05
        if is_luxury or dna.length_m > 15:
            w["market"] = 0.03

        w["community"] = 0.05
        # Increase for mass production boats
        if dna.production_type == "mass_production":
            w["community"] = 0.08

        return self._normalize_weights(w)

    # ------------------------------------------------------------------
    # Custom DNA resolution
    # ------------------------------------------------------------------

    def _resolve_custom(self, dna: BoatDNA) -> dict[str, dict]:
        """Generate configs via continuous formulas for non-legacy DNA."""
        result: dict[str, dict] = {
            "ergonomics": self._resolve_ergonomics(dna),
            "compliance": self._resolve_compliance(dna),
            "structural": self._resolve_structural(dna),
            "production": self._resolve_production(dna),
            "cost": self._resolve_cost(dna),
            "emotional": self._resolve_emotional(dna),
            "materials": self._resolve_materials(dna),
            "volume_storage": self._resolve_volume(dna),
            "brand_dna": self._resolve_segment_module(dna, "brand_dna"),
            "market": self._resolve_segment_module(dna, "market"),
            "service_patterns": self._resolve_segment_module(dna, "service_patterns"),
            "community": self._resolve_community(dna),
            "overall_weights": self._resolve_overall_weights(dna),
        }
        return result

    # ------------------------------------------------------------------
    # Community
    # ------------------------------------------------------------------

    def _resolve_community(self, dna: BoatDNA) -> dict:
        """Resolve community module config from BoatDNA."""
        config = {
            "max_patterns": 20,
            "min_confidence": 0.3,
            "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
        }
        if dna.builder_quality_tier == "superyacht":
            config["max_patterns"] = 25
            config["min_confidence"] = 0.2
        if dna.length_m < 10:
            config["max_patterns"] = 15
            config["min_confidence"] = 0.4
        return config

    # ------------------------------------------------------------------
    # Segment-module fallback (brand_dna, market, service_patterns)
    # ------------------------------------------------------------------

    def _closest_legacy_class(self, dna: BoatDNA) -> str:
        if dna.propulsion in ("sail", "sail_motor"):
            return "small_sail" if dna.length_m < 14 else "cruising_sail"
        else:
            return "large_motor" if dna.length_m < 28 else "superyacht"

    def _resolve_segment_module(self, dna: BoatDNA, module: str) -> dict:
        cls = self._closest_legacy_class(dna)
        return copy.deepcopy(self._get_legacy_configs()[cls][module])

    # ------------------------------------------------------------------
    # Ergonomics
    # ------------------------------------------------------------------

    def _resolve_ergonomics(self, dna: BoatDNA) -> dict:
        length = dna.length_m

        # min_passage_width_mm
        duration_base = {
            "day": 550, "weekend": 575, "week": 600,
            "extended": 600, "liveaboard": 600,
        }
        base = duration_base.get(dna.typical_duration, 575)
        pw = base + 15 * max(0, length - 8)
        if dna.primary_use == "racing":
            pw = 500
        pw = max(500, min(1000, pw))
        min_passage_width_mm = int(round(pw))

        # critical_passage_width_mm
        cpw = max(400, min_passage_width_mm - 150)

        # max_steps_cockpit_pantry
        if dna.primary_use in ("racing", "daysailing"):
            steps = 5
        elif dna.typical_duration == "weekend":
            steps = 8
        elif length > 18:
            steps = 15
        else:
            steps = 10

        # min_helm_area_sqm
        helm = 1.5 + (length - 8) * 0.15
        helm = max(1.5, min(6.0, helm))

        # min_helm_visibility_deg
        vis_map = {"sheltered": 200, "coastal": 225, "offshore": 240, "ocean": 270}
        visibility = vis_map.get(dna.operating_waters, 225)

        # crew_guest_separation
        crew_sep = (
            dna.typical_crew > 4
            and dna.primary_use in ("charter", "superyacht_private", "explorer")
            and length > 15
        )

        # heel_angle_deg
        if dna.propulsion == "motor":
            heel = 0
        elif dna.propulsion == "sail":
            if dna.primary_use == "racing":
                heel = 25
            elif dna.primary_use == "racing_cruiser":
                heel = 20
            else:
                heel = 20
        else:  # sail_motor
            if dna.primary_use == "racing":
                heel_base = 25
            elif dna.primary_use == "racing_cruiser":
                heel_base = 20
            else:
                heel_base = 20
            heel = heel_base / 2

        # weights
        tier_index = ["standard", "premium", "luxury", "superyacht"].index(
            dna.builder_quality_tier
        )
        w_pw = max(0.13, 0.23 - 0.02 * tier_index)
        w_path = 0.15 + (0.02 if crew_sep else 0.0)
        if crew_sep:
            w_crew_sep = 0.10 + 0.05 * tier_index  # scales to 0.25 for superyacht
            if dna.builder_quality_tier == "superyacht":
                w_crew_sep = 0.30
        else:
            w_crew_sep = 0.04
        w_access = max(0.13, 0.22 - 0.02 * tier_index)
        w_helm = 0.11 + (0.03 if dna.operating_waters in ("offshore", "ocean") else 0.0)
        w_heel = 0.10 if dna.propulsion in ("sail", "sail_motor") else 0.0
        w_morning = 0.08
        w_acc_complexity = 0.07

        weights = self._normalize_weights({
            "passage_width": w_pw,
            "path_efficiency": w_path,
            "crew_guest_separation": w_crew_sep,
            "accessibility": w_access,
            "helm_ergonomics": w_helm,
            "heel_impact": w_heel,
            "morning_circulation": w_morning,
            "access_complexity": w_acc_complexity,
        })

        return {
            "min_passage_width_mm": min_passage_width_mm,
            "critical_passage_width_mm": cpw,
            "max_steps_cockpit_pantry": steps,
            "min_helm_area_sqm": round(helm, 1),
            "min_helm_visibility_deg": visibility,
            "crew_guest_separation": crew_sep,
            "heel_angle_deg": heel,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Compliance
    # ------------------------------------------------------------------

    def _resolve_compliance(self, dna: BoatDNA) -> dict:
        length = dna.length_m
        is_sail = dna.propulsion in ("sail", "sail_motor")

        # ce_category
        waters_cat = {
            "ocean": "A",
            "offshore": "A" if length >= 12 else "B",
            "coastal": "C",
            "sheltered": "D",
        }
        ce_cat = waters_cat.get(dna.operating_waters, "C")

        # companionway_sill_mm
        sill_map = {"A": 300, "B": 250, "C": 150, "D": 0}
        sill = sill_map[ce_cat]

        # max_escape_hops
        hops = math.ceil(length / 2.5)
        hops = max(4, min(10, hops))

        # min_engine_clearance_mm
        if is_sail:
            clearance = 500 if length < 12 else 600
        else:
            if length < 18:
                clearance = 700
            else:
                clearance = 800 + int((length - 18) * 10)
        clearance = max(500, min(1200, clearance))

        # min_engine_area_sqm
        if is_sail:
            eng_area = 0.4 + length * 0.04
        else:
            eng_area = 0.5 + length * 0.08
        eng_area = max(0.5, min(5.0, round(eng_area, 1)))

        # min_electrical_area_sqm
        if is_sail:
            elec = 0.15 + length * 0.015
        else:
            elec = 0.1 + length * 0.02
        elec = max(0.2, min(2.0, round(elec, 1)))

        # required_railing_zones
        railing = ["foredeck", "cockpit"]
        if not is_sail and length > 15:
            railing.append("flybridge")
        if not is_sail and length > 18:
            railing.append("swim_platform")

        # norm_versions (constant)
        norm_versions = {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        }

        # weights
        is_ocean = dna.operating_waters in ("offshore", "ocean")
        has_flybridge = not is_sail and length > 15
        w = {
            "escape_routes": 0.20 + (0.04 if is_sail and length < 12 else 0.0) - (0.04 if has_flybridge else 0.0),
            "fire_safety": 0.16 + (0.04 if not is_sail else 0.0),
            "stability": 0.12 + (0.04 if is_ocean and is_sail else 0.0) - (0.04 if not is_sail else 0.0),
            "railing": 0.08 + (0.04 if has_flybridge else 0.0) + (0.04 if dna.builder_quality_tier == "superyacht" else 0.0),
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        }
        weights = self._normalize_weights(w)

        return {
            "min_escape_width_mm": 600,
            "max_escape_hops": hops,
            "min_engine_clearance_mm": clearance,
            "min_engine_area_sqm": eng_area,
            "min_electrical_area_sqm": elec,
            "required_railing_zones": railing,
            "ce_category": ce_cat,
            "cockpit_depth_mm": 300,
            "companionway_sill_mm": sill,
            "norm_versions": norm_versions,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Structural
    # ------------------------------------------------------------------

    def _resolve_structural(self, dna: BoatDNA) -> dict:
        length = dna.length_m
        is_sail = dna.propulsion in ("sail", "sail_motor")

        # ideal_cog_x_range
        if is_sail:
            base_low, base_high = 0.42, 0.52
            if dna.primary_use in ("coastal_cruising", "offshore_cruising", "bluewater"):
                base_low += 0.02
                base_high += 0.02
            elif dna.primary_use in ("racing", "racing_cruiser"):
                base_low += 0.03
                base_high += 0.03
        else:
            base_low, base_high = 0.46, 0.56
            if dna.primary_use not in ("sport_fishing",):
                base_low += 0.02
                base_high += 0.02
            else:
                base_low += 0.04
                base_high += 0.04

        # lateral_tolerance_pct
        if is_sail:
            lat_tol = 0.03
            if dna.primary_use in ("coastal_cruising", "offshore_cruising", "bluewater"):
                lat_tol += 0.02
            elif dna.primary_use in ("racing", "racing_cruiser"):
                lat_tol -= 0.015
        else:
            lat_tol = 0.06
            if length > 20:
                lat_tol += 0.02
        lat_tol = max(0.015, min(0.10, lat_tol))

        # boat_class_weight_factor
        wf = 0.5 + length * 0.035
        wf = max(0.6, min(2.0, round(wf, 1)))

        # max_trim_deg
        trim = 2.0 if is_sail else 1.0

        # weights
        w_fore_aft = 0.26 + (0.04 if is_sail and dna.primary_use in ("racing", "racing_cruiser", "daysailing") else 0.0) - (0.05 if not is_sail else 0.0)
        w_heavy = 0.17 + (0.09 if not is_sail else 0.0)
        w = {
            "fore_aft": max(0.21, w_fore_aft),
            "lateral": 0.21,
            "heavy_placement": w_heavy,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        }
        weights = self._normalize_weights(w)

        return {
            "ideal_cog_x_range": (round(base_low, 2), round(base_high, 2)),
            "lateral_tolerance_pct": round(lat_tol, 3),
            "central_band": (0.20, 0.80),
            "concentration_warn_threshold": 0.55,
            "boat_class_weight_factor": wf,
            "max_trim_deg": trim,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Production
    # ------------------------------------------------------------------

    def _resolve_production(self, dna: BoatDNA) -> dict:
        tier = dna.builder_quality_tier
        tier_index = ["standard", "premium", "luxury", "superyacht"].index(tier)

        # min_sharp_angle_deg
        angle_map = {"standard": 30, "premium": 30, "luxury": 35, "superyacht": 40}
        min_angle = angle_map[tier]

        # min_service_access_mm
        access = 500 + tier_index * 100
        access = max(500, min(900, access))

        # standard_door_widths_mm
        # Check production_type first for more specific sizing
        if dna.production_type == "mass_production":
            doors = [600]
        elif dna.production_type == "one_off":
            doors = [700, 800, 900]
        else:
            # Fall back to tier-based mapping
            door_map = {
                "standard": [600],
                "premium": [600, 700],
                "luxury": [600, 700, 800],
                "superyacht": [700, 800, 900],
            }
            doors = door_map[tier]

        # standard_berth_width_mm
        berth_map = {"standard": 700, "premium": 700, "luxury": 800, "superyacht": 900}
        berth = berth_map[tier]

        # standardization_tolerance_mm
        tol = 75 if tier == "superyacht" else 50

        # target_flat_panel_ratio
        panel_map = {
            "mass_production": 0.70, "semi_custom": 0.60,
            "full_custom": 0.50, "one_off": 0.40,
        }
        panel_ratio = panel_map.get(dna.production_type, 0.60)

        # weights
        is_mass = dna.production_type == "mass_production"
        w = {
            "assembly_sequence": 0.21 if is_mass else 0.13 + tier_index * 0.02,
            "form_complexity": max(0.09, 0.25 - tier_index * 0.05),
            "service_access": 0.17 + tier_index * 0.01,
            "standardization": 0.21 if is_mass else max(0.09, 0.17 - tier_index * 0.02),
            "cable_routing": 0.09 + tier_index * 0.05,
            "mold_complexity": 0.08,
            "flat_panel_ratio": 0.07,
        }
        weights = self._normalize_weights(w)

        return {
            "min_sharp_angle_deg": min_angle,
            "min_service_access_mm": access,
            "standard_door_widths_mm": doors,
            "standard_berth_width_mm": berth,
            "standardization_tolerance_mm": tol,
            "target_flat_panel_ratio": panel_ratio,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Cost
    # ------------------------------------------------------------------

    def _resolve_cost(self, dna: BoatDNA) -> dict:
        tier = dna.builder_quality_tier
        is_sail = dna.propulsion in ("sail", "sail_motor")

        # benchmark_cost_per_meter
        bench_map = {
            "standard": 20000, "premium": 32000,
            "luxury": 65000, "superyacht": 120000,
        }
        benchmark = bench_map[tier]

        # labor_rate_eur_hour
        labor_map = {
            "standard": 55, "premium": 60,
            "luxury": 65, "superyacht": 75,
        }
        labor = labor_map[tier]

        # ideal_distribution by production_type
        dist_map = {
            "mass_production": {"material": 0.40, "labor": 0.35, "equipment": 0.15, "overhead": 0.10},
            "semi_custom": {"material": 0.38, "labor": 0.35, "equipment": 0.17, "overhead": 0.10},
            "full_custom": {"material": 0.35, "labor": 0.30, "equipment": 0.20, "overhead": 0.15},
            "one_off": {"material": 0.30, "labor": 0.30, "equipment": 0.25, "overhead": 0.15},
        }
        ideal_dist = dist_map.get(dna.production_type, dist_map["semi_custom"])

        # parametric_model by propulsion
        if is_sail:
            parametric = {
                "base_cost_per_m": benchmark,
                "hull_pct": 0.22,
                "deck_rigging_pct": 0.13,
                "interior_pct": 0.38,
                "systems_pct": 0.17,
                "design_pct": 0.10,
            }
        else:
            parametric = {
                "base_cost_per_m": benchmark,
                "hull_pct": 0.18,
                "deck_rigging_pct": 0.10,
                "interior_pct": 0.40,
                "systems_pct": 0.22,
                "design_pct": 0.10,
            }

        # weights
        tier_index = ["standard", "premium", "luxury", "superyacht"].index(tier)
        is_luxury = tier in ("luxury", "superyacht")
        w = {
            "material_costs": 0.23 - (0.05 if is_luxury else 0.0),
            "labor_estimate": 0.18 - (0.04 if tier == "superyacht" else 0.0),
            "cost_per_meter": 0.18 + (0.04 if is_luxury else 0.0),
            "distribution": 0.13 + (0.05 if tier == "superyacht" else 0.0),
            "risk": 0.18,
            "parametric_estimate": 0.10,
        }
        weights = self._normalize_weights(w)

        return {
            "benchmark_cost_per_meter": benchmark,
            "labor_rate_eur_hour": labor,
            "boat_length_m": 0,
            "ideal_distribution": ideal_dist,
            "parametric_model": parametric,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Emotional
    # ------------------------------------------------------------------

    def _resolve_emotional(self, dna: BoatDNA) -> dict:
        length = dna.length_m
        focus = dna.interior_focus

        # Focus index: spartan=0, comfortable=1, refined=2, opulent=3
        focus_map = {
            "spartan_functional": 0,
            "comfortable_practical": 1,
            "refined_elegant": 2,
            "opulent_luxury": 3,
        }
        focus_idx = focus_map.get(focus, 1)

        # ideal_proportion_range
        prop_map = {
            0: (0.75, 0.90), 1: (0.70, 0.85),
            2: (0.65, 0.80), 3: (0.60, 0.75),
        }
        ideal_proportion = prop_map[focus_idx]

        # ideal_salon_proportion
        salon_map = {
            0: (0.60, 0.70), 1: (0.55, 0.65),
            2: (0.50, 0.62), 3: (0.45, 0.58),
        }
        ideal_salon = salon_map[focus_idx]

        # target_window_ratio_salon
        tw_salon = max(0.28, min(0.40, 0.28 + focus_idx * 0.03))
        # target_window_ratio_cabin
        tw_cabin = max(0.16, min(0.28, 0.16 + focus_idx * 0.03))
        # target_window_ratio_pantry
        tw_pantry = max(0.10, min(0.20, 0.10 + focus_idx * 0.02))

        # min_sightline_m
        sightline = max(1.2, min(3.0, 1.2 + length * 0.04))

        # ideal_material_range
        mat_map = {0: (2, 4), 1: (3, 5), 2: (3, 6), 3: (4, 7)}
        ideal_mat = mat_map[focus_idx]

        # min_ceiling_mm
        ceil_min = 1700 + (length - 8) * 13
        ceil_min = int(max(1700, min(2100, ceil_min)))

        # standard_ceiling_mm
        ceil_std = ceil_min + 100

        # min_cockpit_passage_mm — same as ergonomics min_passage_width_mm
        ergo = self._resolve_ergonomics(dna)
        cockpit_pw = ergo["min_passage_width_mm"]

        # weights
        is_small = length < 12
        is_perf = dna.primary_use in ("racing", "racing_cruiser")
        is_luxury = dna.builder_quality_tier in ("luxury", "superyacht")
        w = {
            "room_proportion": 0.18 if (is_small or is_perf) else 0.14 - (0.05 if is_luxury else 0.0),
            "light_distribution": 0.14 + (0.04 if is_luxury else 0.0),
            "sightline": 0.09 + (0.14 if is_luxury else 0.05 if not is_small else 0.0),
            "visual_calm": 0.09 + (0.09 if is_luxury else 0.04 if not is_small else 0.0),
            "ceiling_perception": 0.26 if is_small else (0.09 if is_luxury else 0.13),
            "inside_outside_flow": 0.13 + (0.01 if is_small else 0.0),
            "sightline_rays": 0.10,
        }
        # Ensure all are positive
        for k in w:
            w[k] = max(0.05, w[k])
        weights = self._normalize_weights(w)

        return {
            "ideal_proportion_range": ideal_proportion,
            "ideal_salon_proportion": ideal_salon,
            "target_window_ratio_salon": round(tw_salon, 2),
            "target_window_ratio_cabin": round(tw_cabin, 2),
            "target_window_ratio_pantry": round(tw_pantry, 2),
            "min_sightline_m": round(sightline, 1),
            "ideal_material_range": ideal_mat,
            "min_ceiling_mm": ceil_min,
            "standard_ceiling_mm": ceil_std,
            "min_cockpit_passage_mm": cockpit_pw,
            "validation_level": "literaturbasiert",
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Materials
    # ------------------------------------------------------------------

    def _resolve_materials(self, dna: BoatDNA) -> dict:
        tier = dna.builder_quality_tier
        tier_index = ["standard", "premium", "luxury", "superyacht"].index(tier)

        lifespan_map = {"standard": 15, "premium": 20, "luxury": 20, "superyacht": 25}
        maint_map = {"standard": 0.03, "premium": 0.025, "luxury": 0.02, "superyacht": 0.015}
        weight_map = {"standard": 25, "premium": 30, "luxury": 35, "superyacht": 40}
        cost_map = {"standard": 50, "premium": 75, "luxury": 100, "superyacht": 150}

        # weights
        w = {
            "durability": max(0.17, 0.25 - tier_index * 0.03),
            "maintenance": 0.21 - (0.04 if tier == "superyacht" else 0.0),
            "known_issues": 0.17 + (0.04 if tier_index >= 2 else 0.0),
            "compatibility": 0.13 + (0.04 if tier == "superyacht" else 0.0),
            "weight": 0.09 + (0.04 if tier_index >= 1 else 0.0),
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        }
        weights = self._normalize_weights(w)

        return {
            "min_lifespan_years": lifespan_map[tier],
            "max_annual_maintenance_pct": maint_map[tier],
            "max_zone_weight_kg_sqm": weight_map[tier],
            "max_annualized_cost_per_sqm": cost_map[tier],
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Volume / Storage
    # ------------------------------------------------------------------

    def _resolve_volume(self, dna: BoatDNA) -> dict:
        length = dna.length_m
        focus = dna.interior_focus
        is_perf = dna.primary_use in ("racing", "racing_cruiser")
        is_cruising = dna.primary_use in (
            "coastal_cruising", "offshore_cruising", "bluewater",
        )

        # target_utilization
        if is_perf:
            t_util = 0.78
        elif is_cruising:
            t_util = 0.72
        elif dna.design_priority == "comfort":
            t_util = 0.70
        elif dna.builder_quality_tier in ("luxury", "superyacht"):
            t_util = 0.65
        else:
            t_util = 0.70

        # min_utilization
        m_util = max(0.35, t_util - 0.22)

        # target_storage_ratio
        if is_perf:
            t_stor = 0.18
        elif is_cruising:
            t_stor = 0.15
        elif dna.design_priority == "comfort":
            t_stor = 0.12
        elif dna.builder_quality_tier in ("luxury", "superyacht"):
            t_stor = 0.10
        else:
            t_stor = 0.12

        # min_storage_ratio
        m_stor = max(0.08, t_stor - 0.03)

        # min_storage_zones
        szones = 2 + math.ceil(length / 6)
        szones = max(2, min(6, szones))

        # max_distribution_imbalance
        if length < 14:
            imb = 0.6
        elif length <= 20:
            imb = 0.5
        else:
            imb = 0.4

        # furniture ratios by interior focus
        focus_map = {
            "spartan_functional": 0,
            "comfortable_practical": 1,
            "refined_elegant": 2,
            "opulent_luxury": 3,
        }
        fidx = focus_map.get(focus, 1)
        max_furn_map = {0: 0.55, 1: 0.50, 2: 0.50, 3: 0.45}
        min_furn_map = {0: 0.15, 1: 0.20, 2: 0.22, 3: 0.25}
        max_furn = max_furn_map[fidx]
        min_furn = min_furn_map[fidx]

        # weights
        is_luxury = dna.builder_quality_tier in ("luxury", "superyacht")
        w = {
            "utilization": 0.30 if is_perf else (0.15 if is_luxury else 0.20),
            "storage_ratio": 0.25 if is_perf else (0.15 if is_luxury else 0.20),
            "storage_accessibility": 0.20 + (0.05 if is_luxury else 0.0),
            "storage_distribution": 0.15 + (0.05 if is_luxury else 0.0),
            "furniture_ratio": 0.10 + (0.10 if is_luxury else 0.05 if is_cruising else 0.0),
        }
        weights = self._normalize_weights(w)

        return {
            "target_utilization": t_util,
            "min_utilization": round(m_util, 2),
            "target_storage_ratio": t_stor,
            "min_storage_ratio": round(m_stor, 2),
            "min_storage_zones": szones,
            "max_distribution_imbalance": imb,
            "max_furniture_ratio": max_furn,
            "min_furniture_ratio": min_furn,
            "weights": weights,
        }

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    @staticmethod
    def _normalize_weights(weights: dict[str, float]) -> dict[str, float]:
        total = sum(weights.values())
        if total == 0:
            return weights
        normalized = {k: round(v / total, 10) for k, v in weights.items()}
        keys = list(normalized.keys())
        normalized[keys[-1]] = round(1.0 - sum(normalized[k] for k in keys[:-1]), 10)
        return normalized
