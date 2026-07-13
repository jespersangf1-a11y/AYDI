"""Tests for the score fusion service."""
from app.services.analysis.score_fusion import (
    FUSION_WEIGHTS,
    DEFAULT_WEIGHTS,
    CONFIDENCE_DISCOUNT,
    DISAGREEMENT_THRESHOLD,
    fuse_module_scores,
    fuse_all_modules,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _structured(score: float, confidence: str = "measured") -> dict:
    return {"overall_score": score, "confidence": confidence}


def _visual(score: float, confidence: str = "high") -> dict:
    return {"score": score, "confidence": confidence}


# ---------------------------------------------------------------------------
# Both structured and visual available
# ---------------------------------------------------------------------------


def test_fuse_both_high_confidence():
    """Both sources, high visual confidence -> weighted fusion."""
    result = fuse_module_scores(
        _structured(80.0), _visual(90.0, "high"), "ergonomics", "cruising_sail"
    )
    assert result["fused_score"] is not None
    assert result["data_sources"] == ["structured", "visual"]
    assert result["confidence"] == "measured"  # canonical: dominant source (structured)
    # ergonomics: sw=0.75, vw=0.25, high discount=1.0 -> effective same
    expected = 80.0 * 0.75 + 90.0 * 0.25
    assert abs(result["fused_score"] - round(expected, 1)) < 0.2


def test_fuse_both_medium_confidence():
    """Medium visual confidence discounts visual weight."""
    result = fuse_module_scores(
        _structured(80.0), _visual(90.0, "medium"), "ergonomics", "cruising_sail"
    )
    # vw=0.25 * 0.8 = 0.20, sw=1.0-0.20=0.80, normalized: sw=0.80, vw=0.20
    effective_vw = 0.25 * 0.8
    effective_sw = 1.0 - effective_vw
    expected = round(80.0 * effective_sw + 90.0 * effective_vw, 1)
    assert result["fused_score"] == expected


def test_fuse_both_low_confidence():
    """Low visual confidence heavily discounts visual weight."""
    result = fuse_module_scores(
        _structured(80.0), _visual(90.0, "low"), "ergonomics", "cruising_sail"
    )
    # vw=0.25 * 0.5 = 0.125, sw=1.0-0.125=0.875
    effective_vw = 0.25 * 0.5
    effective_sw = 1.0 - effective_vw
    expected = round(80.0 * effective_sw + 90.0 * effective_vw, 1)
    assert result["fused_score"] == expected
    assert result["visual_confidence"] == "low"


def test_fuse_both_insufficient_confidence():
    """Insufficient confidence zeroes visual weight -> pure structured."""
    result = fuse_module_scores(
        _structured(80.0), _visual(90.0, "insufficient"), "ergonomics", "cruising_sail"
    )
    # vw=0.30 * 0.0 = 0.0, so structured takes over
    assert result["fused_score"] == 80.0
    assert result["visual_confidence"] == "insufficient"


def test_fuse_both_equal_scores():
    """When both scores are equal, fused should equal the same value."""
    result = fuse_module_scores(
        _structured(75.0), _visual(75.0, "high"), "ergonomics", "cruising_sail"
    )
    assert result["fused_score"] == 75.0


# ---------------------------------------------------------------------------
# Disagreement detection
# ---------------------------------------------------------------------------


def test_disagreement_flag_triggered():
    """Disagreement >25 points triggers flag."""
    result = fuse_module_scores(
        _structured(90.0), _visual(50.0, "high"), "ergonomics", "cruising_sail"
    )
    assert result["disagreement"] is not None
    assert "manuelle Pruefung" in result["disagreement"]["message"]
    assert result["disagreement"]["structured_score"] == 90.0
    assert result["disagreement"]["visual_score"] == 50.0


def test_no_disagreement_when_close():
    """Scores within 25 points -> no disagreement flag."""
    result = fuse_module_scores(
        _structured(80.0), _visual(60.0, "high"), "ergonomics", "cruising_sail"
    )
    assert result["disagreement"] is None


def test_disagreement_exactly_at_threshold():
    """Exactly 25 points difference -> no flag (> not >=)."""
    result = fuse_module_scores(
        _structured(75.0), _visual(50.0, "high"), "ergonomics", "cruising_sail"
    )
    assert result["disagreement"] is None


# ---------------------------------------------------------------------------
# Structured only
# ---------------------------------------------------------------------------


def test_structured_only():
    """Only structured available -> passthrough with weight 1.0."""
    result = fuse_module_scores(
        _structured(85.0), None, "ergonomics", "cruising_sail"
    )
    assert result["fused_score"] == 85.0
    assert result["data_sources"] == ["structured"]
    assert result["fusion_weights"]["structured"] == 1.0
    assert result["fusion_weights"]["visual"] == 0.0
    assert result["visual_score"] is None
    assert result["disagreement"] is None


def test_structured_only_preserves_confidence():
    """Structured-only preserves its confidence field."""
    result = fuse_module_scores(
        _structured(70.0, "estimated"), None, "emotional", "cruising_sail"
    )
    assert result["confidence"] == "estimated"


# ---------------------------------------------------------------------------
# Visual only
# ---------------------------------------------------------------------------


def test_visual_only():
    """Only visual available -> passthrough with weight 1.0."""
    result = fuse_module_scores(
        None, _visual(72.0, "medium"), "emotional", "cruising_sail"
    )
    assert result["fused_score"] == 72.0
    assert result["data_sources"] == ["visual"]
    assert result["fusion_weights"]["structured"] == 0.0
    assert result["fusion_weights"]["visual"] == 1.0
    assert result["structured_score"] is None
    assert result["visual_confidence"] == "medium"


# ---------------------------------------------------------------------------
# No data
# ---------------------------------------------------------------------------


def test_no_data():
    """Neither source -> fused_score None, confidence insufficient."""
    result = fuse_module_scores(None, None, "ergonomics", "cruising_sail")
    assert result["fused_score"] is None
    assert result["confidence"] == "visual_insufficient"
    assert result["data_sources"] == []
    assert result["structured_score"] is None
    assert result["visual_score"] is None


# ---------------------------------------------------------------------------
# Module-specific weights
# ---------------------------------------------------------------------------


def test_cost_module_zero_visual_weight():
    """Cost module has vw=0.0, so visual never contributes."""
    result = fuse_module_scores(
        _structured(90.0), _visual(50.0, "high"), "cost", "cruising_sail"
    )
    # sw=1.0, vw=0.0 -> effective_vw=0*1.0=0, sw stays 1.0
    assert result["fused_score"] == 90.0
    assert result["nominal_weights"]["visual"] == 0.0


def test_emotional_module_visual_dominates():
    """Emotional module: vw=0.75 so visual has major influence (agreeing scores)."""
    # Scores within the disagreement threshold so the weighted blend applies.
    result = fuse_module_scores(
        _structured(60.0), _visual(80.0, "high"), "emotional", "cruising_sail"
    )
    expected = round(60.0 * 0.25 + 80.0 * 0.75, 1)
    assert result["fused_score"] == expected
    assert result["nominal_weights"]["structured"] == 0.25
    assert result["nominal_weights"]["visual"] == 0.75


def test_compliance_module_structured_dominates():
    """Compliance module: sw=0.95 so structured dominates."""
    result = fuse_module_scores(
        _structured(85.0), _visual(60.0, "high"), "compliance", "cruising_sail"
    )
    expected = round(85.0 * 0.95 + 60.0 * 0.05, 1)
    assert result["fused_score"] == expected
    assert result["nominal_weights"]["structured"] == 0.95


def test_unknown_module_uses_default_weights():
    """Unknown module falls back to 50/50 default."""
    result = fuse_module_scores(
        _structured(80.0), _visual(60.0, "high"), "unknown_module", "cruising_sail"
    )
    expected = round(80.0 * 0.50 + 60.0 * 0.50, 1)
    assert result["fused_score"] == expected
    assert result["nominal_weights"]["structured"] == 0.50
    assert result["nominal_weights"]["visual"] == 0.50


def test_each_module_has_correct_nominal_weights():
    """All defined modules return their expected nominal weights."""
    for module, (sw, vw) in FUSION_WEIGHTS.items():
        result = fuse_module_scores(_structured(50.0), None, module, "cruising_sail")
        assert result["nominal_weights"]["structured"] == sw, f"{module} sw"
        assert result["nominal_weights"]["visual"] == vw, f"{module} vw"


# ---------------------------------------------------------------------------
# Score rounding
# ---------------------------------------------------------------------------


def test_score_rounding():
    """Fused score is always rounded to 1 decimal."""
    result = fuse_module_scores(
        _structured(77.777), _visual(88.888, "high"), "production", "cruising_sail"
    )
    score_str = str(result["fused_score"])
    decimals = len(score_str.split(".")[1]) if "." in score_str else 0
    assert decimals <= 1


def test_structured_only_rounding():
    """Structured-only score is also rounded to 1 decimal."""
    result = fuse_module_scores(_structured(77.777), None, "ergonomics", "cruising_sail")
    assert result["fused_score"] == 77.8


# ---------------------------------------------------------------------------
# fuse_all_modules
# ---------------------------------------------------------------------------


def test_fuse_all_modules_mixed():
    """fuse_all_modules handles mixed availability across modules."""
    structured = {
        "ergonomics": _structured(80.0),
        "compliance": _structured(90.0),
    }
    visual = {
        "ergonomics": _visual(70.0, "high"),
        "emotional": _visual(85.0, "medium"),
    }
    fused = fuse_all_modules(structured, visual, "cruising_sail")

    # Should include all three modules
    assert "ergonomics" in fused
    assert "compliance" in fused
    assert "emotional" in fused

    # Ergonomics: both
    assert fused["ergonomics"]["data_sources"] == ["structured", "visual"]
    # Compliance: structured only
    assert fused["compliance"]["data_sources"] == ["structured"]
    # Emotional: visual only
    assert fused["emotional"]["data_sources"] == ["visual"]


def test_fuse_all_modules_empty():
    """Empty inputs -> empty result."""
    fused = fuse_all_modules({}, {}, "cruising_sail")
    assert fused == {}


def test_fuse_all_modules_sorted():
    """Modules are returned in sorted order."""
    structured = {"volume_storage": _structured(50.0), "ergonomics": _structured(60.0)}
    fused = fuse_all_modules(structured, {}, "cruising_sail")
    keys = list(fused.keys())
    assert keys == sorted(keys)


# ---------------------------------------------------------------------------
# Fusion weight constants
# ---------------------------------------------------------------------------


def test_all_weights_sum_to_one():
    """Nominal weights for every module sum to 1.0."""
    for module, (sw, vw) in FUSION_WEIGHTS.items():
        assert abs(sw + vw - 1.0) < 0.001, f"{module}: {sw} + {vw} != 1.0"


def test_confidence_discount_values():
    """Confidence discount has expected keys and values."""
    assert CONFIDENCE_DISCOUNT["high"] == 1.0
    assert CONFIDENCE_DISCOUNT["medium"] == 0.8
    assert CONFIDENCE_DISCOUNT["low"] == 0.5
    assert CONFIDENCE_DISCOUNT["insufficient"] == 0.0
