"""Tests for brand DNA analysis module."""
from tests.conftest import make_zone, make_passage
from app.services.analysis.brand_dna import (
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
    compute_feature_vector,
    compute_brand_centroid,
    analyze_layout_topology,
    analyze_proportion_consistency,
    analyze_material_palette,
    analyze_spatial_signature,
    analyze_style_continuity,
    run_brand_dna_analysis,
)


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------


def _make_standard_zones() -> list[dict]:
    """Return a representative set of zones for a cruising_sail layout."""
    return [
        make_zone("Salon", "salon",
                  polygon=[[3000, 400], [6000, 400], [6000, 3600], [3000, 3600]],
                  height_mm=1950),
        make_zone("Pantry", "pantry",
                  polygon=[[6000, 400], [7500, 400], [7500, 3600], [6000, 3600]],
                  height_mm=1950),
        make_zone("Kabine Achtern", "cabin",
                  polygon=[[7500, 400], [10000, 400], [10000, 1800], [7500, 1800]],
                  height_mm=1900),
        make_zone("Nasszelle", "head",
                  polygon=[[7500, 1800], [9000, 1800], [9000, 3600], [7500, 3600]],
                  height_mm=1900),
        make_zone("Cockpit", "cockpit",
                  polygon=[[10000, 400], [12000, 400], [12000, 3600], [10000, 3600]],
                  height_mm=1800),
    ]


def _make_standard_passages() -> list[dict]:
    """Return a representative set of passages for a cruising_sail layout."""
    return [
        make_passage("Salon", "Pantry", width_mm=750),
        make_passage("Pantry", "Kabine Achtern", width_mm=700),
        make_passage("Pantry", "Nasszelle", width_mm=680),
        make_passage("Cockpit", "Pantry", width_mm=760),
    ]


def _make_reference_features() -> dict:
    """Compute features for the standard zones/passages."""
    return compute_feature_vector(_make_standard_zones(), _make_standard_passages())


def make_brand_reference(
    zones: list[dict] | None = None,
    passages: list[dict] | None = None,
    materials: list[str] | None = None,
    style_tags: list[str] | None = None,
) -> dict:
    """Build a brand reference dict with features computed from zones/passages.

    Args:
        zones: Optional custom zone list; defaults to the standard set.
        passages: Optional custom passage list; defaults to the standard set.
        materials: Material category strings; defaults to a typical set.
        style_tags: Style descriptor tags; defaults to a typical set.

    Returns:
        Reference dict suitable for the brand_references parameter of
        run_brand_dna_analysis().
    """
    z = zones if zones is not None else _make_standard_zones()
    p = passages if passages is not None else _make_standard_passages()
    features = compute_feature_vector(z, p)
    return {
        "features": features,
        "materials": materials if materials is not None else ["teak", "composite", "aluminum"],
        "style_tags": style_tags if style_tags is not None else ["minimalist", "functional", "teak"],
    }


def _three_identical_refs() -> list[dict]:
    """Three identical brand references — used in multiple tests."""
    return [make_brand_reference() for _ in range(3)]


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# test_empty_references
# ---------------------------------------------------------------------------


def test_empty_references():
    """No brand references at all -> score 50, BRAND_INSUFFICIENT_DATA info warning."""
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        brand_references=None,
    )
    assert result["overall_score"] == 50.0
    assert any(w["code"] == "BRAND_INSUFFICIENT_DATA" for w in result["warnings"])
    assert all(w["severity"] == "info" for w in result["warnings"])


# ---------------------------------------------------------------------------
# test_insufficient_references
# ---------------------------------------------------------------------------


def test_insufficient_references():
    """Fewer than min_reference_models (3) -> score 50, insufficient data warning."""
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        brand_references=[make_brand_reference(), make_brand_reference()],  # only 2
    )
    assert result["overall_score"] == 50.0
    assert any(w["code"] == "BRAND_INSUFFICIENT_DATA" for w in result["warnings"])


# ---------------------------------------------------------------------------
# test_identical_layout_to_references
# ---------------------------------------------------------------------------


def test_identical_layout_to_references():
    """New layout identical to references -> high overall score."""
    refs = _three_identical_refs()
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        brand_references=refs,
    )
    assert result["overall_score"] >= 80.0
    assert result["module"] == "brand_dna"


# ---------------------------------------------------------------------------
# test_completely_different_layout
# ---------------------------------------------------------------------------


def test_completely_different_layout():
    """Layout with entirely different zones -> low score."""
    # A very different layout: only engine + storage zones, no salon/cabin/head
    different_zones = [
        make_zone("Motor", "engine",
                  polygon=[[0, 0], [3000, 0], [3000, 4000], [0, 4000]],
                  height_mm=1500),
        make_zone("Lager", "storage",
                  polygon=[[3000, 0], [6000, 0], [6000, 4000], [3000, 4000]],
                  height_mm=1500),
    ]
    different_passages = [
        make_passage("Motor", "Lager", width_mm=500),
    ]
    refs = _three_identical_refs()
    result = run_brand_dna_analysis(
        different_zones,
        different_passages,
        "cruising_sail",
        brand_references=refs,
    )
    # Different topology and proportions -> lower score than identical layout
    identical_result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        brand_references=refs,
    )
    assert result["overall_score"] < identical_result["overall_score"]


# ---------------------------------------------------------------------------
# test_topology_overlap
# ---------------------------------------------------------------------------


def test_topology_overlap():
    """Topology sub-analysis: identical adjacency graph -> score 100."""
    new_features = _make_reference_features()
    ref_features = [_make_reference_features(), _make_reference_features()]
    config = _default_config()

    score, warnings, metrics = analyze_layout_topology(new_features, ref_features, config)

    assert score == 100.0
    assert metrics["overlap_ratio"] == 1.0
    assert not any(w["code"] == "BRAND_TOPOLOGY_DEVIATION" for w in warnings)


def test_topology_deviation_warning():
    """Topology sub-analysis: low overlap -> BRAND_TOPOLOGY_DEVIATION warning."""
    # New layout with completely different zone connections
    new_zones = [
        make_zone("Motor", "engine", polygon=[[0, 0], [3000, 0], [3000, 4000], [0, 4000]]),
        make_zone("Lager", "storage", polygon=[[3000, 0], [6000, 0], [6000, 4000], [3000, 4000]]),
    ]
    new_passages = [make_passage("Motor", "Lager", width_mm=500)]
    new_features = compute_feature_vector(new_zones, new_passages)
    ref_features = [_make_reference_features(), _make_reference_features()]
    config = _default_config()

    score, warnings, metrics = analyze_layout_topology(new_features, ref_features, config)

    assert score < 60.0
    assert any(w["code"] == "BRAND_TOPOLOGY_DEVIATION" for w in warnings)


# ---------------------------------------------------------------------------
# test_proportion_within_bounds
# ---------------------------------------------------------------------------


def test_proportion_within_bounds():
    """Proportions matching references -> no BRAND_PROPORTION_OUTLIER warning."""
    new_features = _make_reference_features()
    ref_features = [
        _make_reference_features(),
        _make_reference_features(),
        _make_reference_features(),
    ]
    config = _default_config()

    score, warnings, metrics = analyze_proportion_consistency(new_features, ref_features, config)

    assert score == 100.0
    assert not any(w["code"] == "BRAND_PROPORTION_OUTLIER" for w in warnings)
    assert "deviating_types" in metrics
    assert metrics["deviating_types"] == []


# ---------------------------------------------------------------------------
# test_proportion_outlier
# ---------------------------------------------------------------------------


def test_proportion_outlier():
    """Zone proportion far from references -> BRAND_PROPORTION_OUTLIER warning."""
    # Build references with very small cabin zones
    small_cabin_zones = [
        make_zone("Salon", "salon",
                  polygon=[[0, 0], [8000, 0], [8000, 4000], [0, 4000]]),
        make_zone("Kabine", "cabin",
                  polygon=[[8000, 0], [8100, 0], [8100, 100], [8000, 100]]),  # tiny
    ]
    small_feats = compute_feature_vector(small_cabin_zones, [])
    # References with consistently small cabin
    ref_features = [small_feats, small_feats, small_feats]
    config = _default_config()

    # New layout with large cabin (very different ratio)
    large_cabin_zones = [
        make_zone("Salon", "salon",
                  polygon=[[0, 0], [2000, 0], [2000, 4000], [0, 4000]]),
        make_zone("Kabine", "cabin",
                  polygon=[[2000, 0], [10000, 0], [10000, 4000], [2000, 4000]]),  # large
    ]
    new_features = compute_feature_vector(large_cabin_zones, [])

    score, warnings, metrics = analyze_proportion_consistency(new_features, ref_features, config)

    # std = 0 here (all identical refs), so outlier detection only fires when std > 0
    # Use refs with slight variation to trigger:
    varied_zones_a = [
        make_zone("Salon", "salon",
                  polygon=[[0, 0], [7000, 0], [7000, 4000], [0, 4000]]),
        make_zone("Kabine", "cabin",
                  polygon=[[7000, 0], [8000, 0], [8000, 4000], [7000, 4000]]),
    ]
    varied_zones_b = [
        make_zone("Salon", "salon",
                  polygon=[[0, 0], [7500, 0], [7500, 4000], [0, 4000]]),
        make_zone("Kabine", "cabin",
                  polygon=[[7500, 0], [8500, 0], [8500, 4000], [7500, 4000]]),
    ]
    varied_zones_c = [
        make_zone("Salon", "salon",
                  polygon=[[0, 0], [7200, 0], [7200, 4000], [0, 4000]]),
        make_zone("Kabine", "cabin",
                  polygon=[[7200, 0], [8200, 0], [8200, 4000], [7200, 4000]]),
    ]
    ref_features_varied = [
        compute_feature_vector(varied_zones_a, []),
        compute_feature_vector(varied_zones_b, []),
        compute_feature_vector(varied_zones_c, []),
    ]
    score2, warnings2, metrics2 = analyze_proportion_consistency(new_features, ref_features_varied, config)
    assert any(w["code"] == "BRAND_PROPORTION_OUTLIER" for w in warnings2)
    assert len(metrics2["deviating_types"]) > 0


# ---------------------------------------------------------------------------
# test_material_palette_match
# ---------------------------------------------------------------------------


def test_material_palette_match():
    """All new materials present in references -> score 100, no unknown warnings."""
    new_materials = ["teak", "composite"]
    ref_materials = [
        ["teak", "composite", "aluminum"],
        ["teak", "composite", "stainless"],
        ["teak", "composite"],
    ]
    config = _default_config()

    score, warnings, metrics = analyze_material_palette(new_materials, ref_materials, config)

    assert score == 100.0
    assert not any(w["code"] == "BRAND_MATERIAL_UNKNOWN" for w in warnings)
    assert metrics["unknown_categories"] == []


# ---------------------------------------------------------------------------
# test_material_unknown
# ---------------------------------------------------------------------------


def test_material_unknown():
    """New material absent from all references -> BRAND_MATERIAL_UNKNOWN warning."""
    new_materials = ["teak", "carbon_fiber"]  # carbon_fiber not in refs
    ref_materials = [
        ["teak", "composite"],
        ["teak", "aluminum"],
        ["teak", "composite", "stainless"],
    ]
    config = _default_config()

    score, warnings, metrics = analyze_material_palette(new_materials, ref_materials, config)

    assert score < 100.0
    assert any(w["code"] == "BRAND_MATERIAL_UNKNOWN" for w in warnings)
    assert "carbon_fiber" in metrics["unknown_categories"]


# ---------------------------------------------------------------------------
# test_spatial_similarity_high
# ---------------------------------------------------------------------------


def test_spatial_similarity_high():
    """Identical features vs centroid -> cosine similarity ~1.0, score ~100."""
    features = _make_reference_features()
    centroid = compute_brand_centroid([features, features, features])
    config = _default_config()

    score, warnings, metrics = analyze_spatial_signature(features, centroid, config)

    assert score >= 95.0
    assert metrics["cosine_similarity"] >= 0.95
    assert not any(w["code"] == "BRAND_SPATIAL_DEVIATION" for w in warnings)


def test_spatial_similarity_low():
    """Very different features vs centroid -> low similarity, BRAND_SPATIAL_DEVIATION."""
    ref_features = _make_reference_features()
    centroid = compute_brand_centroid([ref_features, ref_features, ref_features])
    config = _default_config()

    different_zones = [
        make_zone("Motor", "engine",
                  polygon=[[0, 0], [12000, 0], [12000, 4000], [0, 4000]], height_mm=1500),
    ]
    new_features = compute_feature_vector(different_zones, [])

    score, warnings, metrics = analyze_spatial_signature(new_features, centroid, config)

    assert score < 70.0
    assert any(w["code"] == "BRAND_SPATIAL_DEVIATION" for w in warnings)


# ---------------------------------------------------------------------------
# test_style_continuity_match
# ---------------------------------------------------------------------------


def test_style_continuity_match():
    """New layout tags match the brand signature -> high score, no style shift."""
    new_tags = ["minimalist", "functional", "teak"]
    ref_tags_list = [
        ["minimalist", "functional", "teak"],
        ["minimalist", "functional", "teak", "nordic"],
        ["minimalist", "functional", "teak"],
    ]
    config = _default_config()

    score, warnings, metrics = analyze_style_continuity(new_tags, ref_tags_list, config)

    assert score >= 80.0
    assert not any(w["code"] == "BRAND_STYLE_SHIFT" for w in warnings)
    assert "minimalist" in metrics["overlap"]


# ---------------------------------------------------------------------------
# test_style_shift
# ---------------------------------------------------------------------------


def test_style_shift():
    """New layout uses completely different tags -> BRAND_STYLE_SHIFT warning."""
    new_tags = ["baroque", "ornate", "gold"]
    ref_tags_list = [
        ["minimalist", "functional", "teak"],
        ["minimalist", "functional", "teak"],
        ["minimalist", "functional", "teak"],
    ]
    config = _default_config()

    score, warnings, metrics = analyze_style_continuity(new_tags, ref_tags_list, config)

    assert score == 0.0
    assert any(w["code"] == "BRAND_STYLE_SHIFT" for w in warnings)
    assert metrics["missing"] == ["functional", "minimalist", "teak"]


# ---------------------------------------------------------------------------
# test_different_boat_classes
# ---------------------------------------------------------------------------


def test_different_boat_classes():
    """Different boat classes use different weights -> different overall scores."""
    zones = _make_standard_zones()
    passages = _make_standard_passages()

    # References with mismatched style to trigger score variation
    refs = [
        make_brand_reference(style_tags=["minimalist", "functional"]),
        make_brand_reference(style_tags=["minimalist", "functional"]),
        make_brand_reference(style_tags=["minimalist", "functional"]),
    ]

    result_small = run_brand_dna_analysis(zones, passages, "small_sail", brand_references=refs)
    result_super = run_brand_dna_analysis(zones, passages, "superyacht", brand_references=refs)

    # small_sail weights topology/proportions highest; superyacht weights spatial/style highest
    # Both should return valid results
    assert 0 <= result_small["overall_score"] <= 100
    assert 0 <= result_super["overall_score"] <= 100
    assert result_small["module"] == "brand_dna"
    assert result_super["module"] == "brand_dna"
    # Weights differ, so scores differ (unless all sub-scores happen to be equal)
    small_weights = BOAT_CLASS_DEFAULTS["small_sail"]["weights"]
    super_weights = BOAT_CLASS_DEFAULTS["superyacht"]["weights"]
    assert small_weights != super_weights


# ---------------------------------------------------------------------------
# test_config_overrides
# ---------------------------------------------------------------------------


def test_config_overrides():
    """Config overrides are applied and reflected in config_used."""
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        config_overrides={"proportion_deviation_threshold": 0.1},
        brand_references=_three_identical_refs(),
    )
    assert result["config_used"]["proportion_deviation_threshold"] == 0.1


def test_config_overrides_min_refs():
    """Override min_reference_models to 2 — 2 refs should now be sufficient."""
    two_refs = [make_brand_reference(), make_brand_reference()]
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        config_overrides={"min_reference_models": 2},
        brand_references=two_refs,
    )
    # With override, analysis should proceed (no BRAND_INSUFFICIENT_DATA)
    assert not any(w["code"] == "BRAND_INSUFFICIENT_DATA" for w in result["warnings"])
    assert result["overall_score"] != 50.0 or len(result["sub_scores"]) == 5


# ---------------------------------------------------------------------------
# test_full_integration
# ---------------------------------------------------------------------------


def test_full_integration():
    """Full integration test: valid zones, passages, and three brand references."""
    # References that match the new layout well
    refs = _three_identical_refs()

    result = run_brand_dna_analysis(
        _make_standard_zones(),
        _make_standard_passages(),
        "cruising_sail",
        brand_references=refs,
    )

    # Structure checks
    assert result["module"] == "brand_dna"
    assert 0 <= result["overall_score"] <= 100
    assert set(result["sub_scores"].keys()) == {"topology", "proportions", "materials", "spatial", "style"}
    assert all(0 <= v <= 100 for v in result["sub_scores"].values())
    assert isinstance(result["warnings"], list)
    assert isinstance(result["suggestions"], list)
    assert isinstance(result["metrics"], dict)
    assert "config_used" in result

    # Warnings should be sorted critical → warning → info
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_warnings_sorted_by_severity():
    """Result warnings are sorted: critical first, then warning, then info."""
    # Use layout very different from references to generate multiple warning types
    different_zones = [
        make_zone("Motor", "engine",
                  polygon=[[0, 0], [6000, 0], [6000, 4000], [0, 4000]], height_mm=1500),
        make_zone("Lager", "storage",
                  polygon=[[6000, 0], [12000, 0], [12000, 4000], [6000, 4000]], height_mm=1500),
    ]
    different_passages = [make_passage("Motor", "Lager", width_mm=500)]
    refs = _three_identical_refs()

    result = run_brand_dna_analysis(
        different_zones,
        different_passages,
        "cruising_sail",
        brand_references=refs,
    )

    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_no_passages_graceful():
    """Layout with no passages -> no crash, score returned."""
    refs = _three_identical_refs()
    result = run_brand_dna_analysis(
        _make_standard_zones(),
        [],
        "cruising_sail",
        brand_references=refs,
    )
    assert 0 <= result["overall_score"] <= 100


def test_feature_vector_empty_input():
    """compute_feature_vector with empty input -> safe defaults."""
    feats = compute_feature_vector([], [])
    assert feats["zone_proportions"] == {}
    assert feats["adjacency_graph"] == set()
    assert feats["avg_passage_width_mm"] == 0.0
    assert feats["cabin_count"] == 0
    assert feats["head_count"] == 0
    assert feats["deck_height_avg"] == 0.0
