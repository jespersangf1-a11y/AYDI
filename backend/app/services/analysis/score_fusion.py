"""Score fusion: combines structured analysis results with visual analysis results.

Structured analysis produces deterministic scores from geometric data (zones,
passages, measurements).  Visual analysis produces scores from photo-based
assessment via a vision model.  This module fuses both into a single per-module
score, taking confidence and module-specific weighting into account.
"""

from __future__ import annotations

# Fusion weights per module: (structured_weight, visual_weight)
# These represent the *nominal* split when both sources are available at high
# confidence.  The actual effective weights are adjusted by visual confidence.
FUSION_WEIGHTS: dict[str, tuple[float, float]] = {
    "ergonomics":       (0.75, 0.25),
    "emotional":        (0.25, 0.75),
    "volume_storage":   (0.85, 0.15),
    "materials":        (0.35, 0.65),
    "production":       (0.55, 0.45),
    "compliance":       (0.95, 0.05),
    "structural":       (0.95, 0.05),
    "cost":             (1.00, 0.00),
    "service_patterns": (0.65, 0.35),
    "brand_dna":        (0.35, 0.65),
    "market":           (0.60, 0.40),
    "community":        (1.00, 0.00),
}

# Default weights for unknown modules
DEFAULT_WEIGHTS: tuple[float, float] = (0.50, 0.50)

# Confidence discount factors — how much we trust the visual score
CONFIDENCE_DISCOUNT: dict[str, float] = {
    "high": 1.0,
    "visual_high": 1.0,
    "medium": 0.8,
    "visual_medium": 0.8,
    "low": 0.5,
    "visual_low": 0.5,
    "insufficient": 0.0,
    "visual_insufficient": 0.0,
}

# Disagreement threshold in score points
DISAGREEMENT_THRESHOLD: float = 25.0


def fuse_module_scores(
    structured_result: dict | None,
    visual_result: dict | None,
    module: str,
    boat_class: str,
) -> dict:
    """Combine structured and visual analysis into a single module score.

    Args:
        structured_result: Result dict from structured analysis (must have
            ``overall_score``).
        visual_result: Result dict from visual analysis (must have ``score``
            and ``confidence``).
        module: Analysis module name (e.g. ``"ergonomics"``).
        boat_class: Boat class for context (e.g. ``"cruising_sail"``).

    Returns:
        Dict with ``fused_score``, ``confidence``, ``data_sources``,
        individual scores, fusion weights, and optional disagreement flag.
    """
    sw, vw = FUSION_WEIGHTS.get(module, DEFAULT_WEIGHTS)

    if structured_result and visual_result:
        return _fuse_both(structured_result, visual_result, sw, vw)
    elif structured_result:
        return _structured_only(structured_result, sw, vw)
    elif visual_result:
        return _visual_only(visual_result, sw, vw)
    else:
        return _no_data(sw, vw)


def fuse_all_modules(
    structured_results: dict[str, dict],
    visual_results: dict[str, dict],
    boat_class: str,
) -> dict:
    """Fuse scores for all modules that have results.

    Args:
        structured_results: Mapping of module name to structured result dict.
        visual_results: Mapping of module name to visual result dict.
        boat_class: Boat class for context.

    Returns:
        Dict mapping module name to fused result dict.
    """
    all_modules = set(list(structured_results.keys()) + list(visual_results.keys()))
    fused: dict[str, dict] = {}
    for module in sorted(all_modules):
        fused[module] = fuse_module_scores(
            structured_results.get(module),
            visual_results.get(module),
            module,
            boat_class,
        )
    return fused


def fuse_zone_score(
    zone_name: str,
    module: str,
    structured_score: float | None,
    visual_score: float | None,
    structured_confidence: str = "measured",
    visual_confidence: str = "visual_medium",
) -> dict:
    """Fuse structured and visual scores for a specific zone.

    Returns dict with score, confidence, sources, components, and optional discrepancy note.
    """
    sw, vw = FUSION_WEIGHTS.get(module, DEFAULT_WEIGHTS)

    if structured_score is not None and visual_score is None:
        return {
            "zone_name": zone_name,
            "score": round(structured_score, 1),
            "confidence": structured_confidence,
            "sources": ["structured"],
            "structured_component": round(structured_score, 1),
            "visual_component": None,
            "discrepancy_note": None,
        }
    if visual_score is not None and structured_score is None:
        return {
            "zone_name": zone_name,
            "score": round(visual_score, 1),
            "confidence": visual_confidence,
            "sources": ["visual"],
            "structured_component": None,
            "visual_component": round(visual_score, 1),
            "discrepancy_note": None,
        }
    if structured_score is None and visual_score is None:
        return {
            "zone_name": zone_name,
            "score": None,
            "confidence": "visual_insufficient",
            "sources": [],
            "structured_component": None,
            "visual_component": None,
            "discrepancy_note": None,
        }

    # Both available
    discrepancy = abs(structured_score - visual_score)
    if discrepancy > DISAGREEMENT_THRESHOLD:
        # Flag, do not blend: report the structured (measurement) score and
        # mark for manual review rather than averaging a conflict away.
        return {
            "zone_name": zone_name,
            "score": round(structured_score, 1),
            "confidence": structured_confidence,
            "sources": ["structured", "visual"],
            "structured_component": round(structured_score, 1),
            "visual_component": round(visual_score, 1),
            "needs_review": True,
            "discrepancy_note": (
                f"Strukturdaten ({structured_score:.0f}) und Bildbewertung ({visual_score:.0f}) "
                f"weichen um {discrepancy:.0f} Punkte ab. Bitte manuell pruefen."
            ),
        }

    fused = structured_score * sw + visual_score * vw

    # Confidence: best (highest-rank) of the two canonical codes.
    conf_rank = {
        "measured": 5, "calculated": 4, "visual_high": 4,
        "visual_medium": 3, "estimated": 2, "documented": 3,
        "visual_low": 1, "benchmark": 2,
    }
    best_conf = structured_confidence if conf_rank.get(structured_confidence, 0) >= conf_rank.get(visual_confidence, 0) else visual_confidence

    return {
        "zone_name": zone_name,
        "score": round(fused, 1),
        "confidence": best_conf,
        "sources": ["structured", "visual"],
        "structured_component": round(structured_score, 1),
        "visual_component": round(visual_score, 1),
        "needs_review": False,
        "discrepancy_note": None,
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _fuse_both(
    structured_result: dict,
    visual_result: dict,
    sw: float,
    vw: float,
) -> dict:
    """Fuse when both structured and visual results are available."""
    s_score = structured_result["overall_score"]
    v_score = visual_result["score"]
    s_conf = structured_result.get("confidence", "measured")
    v_confidence = visual_result.get("confidence", "visual_medium")

    disagreement = abs(s_score - v_score)
    if disagreement > DISAGREEMENT_THRESHOLD:
        # Reliability rule: on CAD-vs-photo disagreement, FLAG — do NOT blend
        # into a single misleading number. Report the more authoritative
        # structured (measurement) score with its own confidence, surface both
        # raw scores, and set needs_review for human-in-the-loop assessment.
        return {
            "fused_score": round(s_score, 1),
            "confidence": s_conf,
            "data_sources": ["structured", "visual"],
            "structured_score": round(s_score, 1),
            "visual_score": round(v_score, 1),
            "fusion_weights": {"structured": 1.0, "visual": 0.0},
            "nominal_weights": {"structured": sw, "visual": vw},
            "visual_confidence": v_confidence,
            "needs_review": True,
            "disagreement": {
                "message": (
                    f"Strukturelle und visuelle Bewertung weichen um "
                    f"{disagreement:.0f} Punkte ab — manuelle Pruefung empfohlen."
                ),
                "structured_score": round(s_score, 1),
                "visual_score": round(v_score, 1),
            },
        }

    # Agreement: blend, discounting the visual weight by its confidence.
    discount = CONFIDENCE_DISCOUNT.get(v_confidence, 0.5)
    effective_vw = vw * discount
    effective_sw = 1.0 - effective_vw

    # Normalize so weights sum to 1.0
    total = effective_sw + effective_vw
    if total > 0:
        effective_sw /= total
        effective_vw /= total

    fused_score = s_score * effective_sw + v_score * effective_vw

    # Canonical confidence = the confidence code of the dominant source
    # (avoids the non-canonical "measured+visual").
    fused_conf = s_conf if effective_sw >= effective_vw else v_confidence

    return {
        "fused_score": round(fused_score, 1),
        "confidence": fused_conf,
        "data_sources": ["structured", "visual"],
        "structured_score": round(s_score, 1),
        "visual_score": round(v_score, 1),
        "fusion_weights": {
            "structured": round(effective_sw, 3),
            "visual": round(effective_vw, 3),
        },
        "nominal_weights": {"structured": sw, "visual": vw},
        "visual_confidence": v_confidence,
        "needs_review": False,
        "disagreement": None,
    }


def _structured_only(structured_result: dict, sw: float, vw: float) -> dict:
    """Return result when only structured analysis is available."""
    return {
        "fused_score": round(structured_result["overall_score"], 1),
        "confidence": structured_result.get("confidence", "measured"),
        "data_sources": ["structured"],
        "structured_score": round(structured_result["overall_score"], 1),
        "visual_score": None,
        "fusion_weights": {"structured": 1.0, "visual": 0.0},
        "nominal_weights": {"structured": sw, "visual": vw},
        "visual_confidence": None,
        "disagreement": None,
    }


def _visual_only(visual_result: dict, sw: float, vw: float) -> dict:
    """Return result when only visual analysis is available."""
    return {
        "fused_score": round(visual_result["score"], 1),
        "confidence": visual_result.get("confidence", "visual_medium"),
        "data_sources": ["visual"],
        "structured_score": None,
        "visual_score": round(visual_result["score"], 1),
        "fusion_weights": {"structured": 0.0, "visual": 1.0},
        "nominal_weights": {"structured": sw, "visual": vw},
        "visual_confidence": visual_result.get("confidence", "medium"),
        "disagreement": None,
    }


def _no_data(sw: float, vw: float) -> dict:
    """Return result when no analysis data is available."""
    return {
        "fused_score": None,
        "confidence": "visual_insufficient",
        "data_sources": [],
        "structured_score": None,
        "visual_score": None,
        "fusion_weights": {"structured": 0.0, "visual": 0.0},
        "nominal_weights": {"structured": sw, "visual": vw},
        "visual_confidence": None,
        "disagreement": None,
    }
