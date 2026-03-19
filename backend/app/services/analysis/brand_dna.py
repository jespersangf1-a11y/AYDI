"""Brand DNA analysis module for yacht layouts.

Compares a new layout design against a shipyard's established portfolio to measure
how well it fits the brand's spatial identity. Pure function module — no database
access. All user-facing strings are in German.

Requires at least `min_reference_models` brand reference dicts to produce a
meaningful score. If fewer references are provided, returns score 50 with an
informational warning.
"""
import logging
import math

try:
    import numpy as np

    def _cosine_similarity(a: list[float], b: list[float]) -> float:
        """Cosine similarity between two numeric vectors using numpy."""
        va = np.array(a, dtype=float)
        vb = np.array(b, dtype=float)
        norm_a = float(np.linalg.norm(va))
        norm_b = float(np.linalg.norm(vb))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return float(np.dot(va, vb) / (norm_a * norm_b))

except ImportError:  # pragma: no cover
    np = None  # type: ignore[assignment]

    def _cosine_similarity(a: list[float], b: list[float]) -> float:
        """Cosine similarity fallback — pure Python dot product."""
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)


logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS: dict[str, dict] = {
    "small_sail": {
        "min_reference_models": 3,
        "proportion_deviation_threshold": 2.0,
        "weights": {
            "topology": 0.25,
            "proportions": 0.25,
            "materials": 0.20,
            "spatial": 0.20,
            "style": 0.10,
        },
    },
    "cruising_sail": {
        "min_reference_models": 3,
        "proportion_deviation_threshold": 2.0,
        "weights": {
            "topology": 0.20,
            "proportions": 0.25,
            "materials": 0.20,
            "spatial": 0.25,
            "style": 0.10,
        },
    },
    "large_motor": {
        "min_reference_models": 3,
        "proportion_deviation_threshold": 1.8,
        "weights": {
            "topology": 0.20,
            "proportions": 0.20,
            "materials": 0.20,
            "spatial": 0.25,
            "style": 0.15,
        },
    },
    "superyacht": {
        "min_reference_models": 3,
        "proportion_deviation_threshold": 1.5,
        "weights": {
            "topology": 0.15,
            "proportions": 0.20,
            "materials": 0.20,
            "spatial": 0.25,
            "style": 0.20,
        },
    },
}

SEVERITY_ORDER: dict[str, int] = {"critical": 0, "warning": 1, "info": 2}


# ---------------------------------------------------------------------------
# Feature extraction helpers
# ---------------------------------------------------------------------------


def _calculate_zone_area(polygon: list[list[float]]) -> float:
    """Compute polygon area using the Shoelace formula.

    Coordinates are in millimetres; returns area in square metres.
    """
    n = len(polygon)
    if n < 3:
        return 0.0
    signed_area = 0.0
    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % n]
        signed_area += x0 * y1 - x1 * y0
    area_mm2 = abs(signed_area) / 2.0
    return area_mm2 / 1_000_000.0  # mm² → m²


def compute_feature_vector(zones: list[dict], passages: list[dict]) -> dict:
    """Extract a comparable feature dict from a layout.

    Returned keys:
    - zone_proportions: dict mapping zone_type → fraction of total area (0–1)
    - adjacency_graph: set of frozensets, one per passage connection
    - avg_passage_width_mm: mean passage width, or 0.0 if no passages
    - cabin_count: number of cabin zones
    - head_count: number of head zones
    - deck_height_avg: mean height_mm across zones that declare it, else 0.0

    Args:
        zones: List of zone dicts as used throughout the AYDI analysis engine.
        passages: List of passage dicts.

    Returns:
        Feature dict.
    """
    # --- zone proportions ---
    areas_by_type: dict[str, float] = {}
    total_area = 0.0
    cabin_count = 0
    head_count = 0
    heights: list[float] = []

    for z in zones:
        polygon = z.get("polygon") or []
        area = _calculate_zone_area(polygon)
        ztype = z.get("zone_type", "unknown")
        areas_by_type[ztype] = areas_by_type.get(ztype, 0.0) + area
        total_area += area

        if ztype == "cabin":
            cabin_count += 1
        elif ztype == "head":
            head_count += 1

        h = z.get("height_mm")
        if h is not None:
            heights.append(float(h))

    zone_proportions: dict[str, float] = {}
    if total_area > 0:
        for ztype, a in areas_by_type.items():
            zone_proportions[ztype] = a / total_area

    # --- adjacency graph ---
    adjacency_graph: set[frozenset] = set()
    widths: list[float] = []
    for p in passages:
        frm = p.get("from_zone", "")
        to = p.get("to_zone", "")
        if frm and to:
            adjacency_graph.add(frozenset({frm, to}))
        w = p.get("width_mm")
        if w is not None:
            widths.append(float(w))

    return {
        "zone_proportions": zone_proportions,
        "adjacency_graph": adjacency_graph,
        "avg_passage_width_mm": sum(widths) / len(widths) if widths else 0.0,
        "cabin_count": cabin_count,
        "head_count": head_count,
        "deck_height_avg": sum(heights) / len(heights) if heights else 0.0,
    }


def compute_brand_centroid(reference_features: list[dict]) -> dict:
    """Aggregate a list of reference feature dicts into a single brand centroid.

    Zone proportions are averaged across references.  Adjacency edges are
    unioned.  Numeric scalars are averaged.

    Args:
        reference_features: List of feature dicts from compute_feature_vector().

    Returns:
        A single feature dict representing the brand centroid.
    """
    if not reference_features:
        return {
            "zone_proportions": {},
            "adjacency_graph": set(),
            "avg_passage_width_mm": 0.0,
            "cabin_count": 0.0,
            "head_count": 0.0,
            "deck_height_avg": 0.0,
        }

    n = len(reference_features)

    # Aggregate zone proportions
    all_zone_types: set[str] = set()
    for f in reference_features:
        all_zone_types.update(f.get("zone_proportions", {}).keys())

    centroid_proportions: dict[str, float] = {}
    for ztype in all_zone_types:
        centroid_proportions[ztype] = (
            sum(f.get("zone_proportions", {}).get(ztype, 0.0) for f in reference_features) / n
        )

    # Union adjacency edges
    union_edges: set[frozenset] = set()
    for f in reference_features:
        union_edges.update(f.get("adjacency_graph", set()))

    # Average numeric scalars
    def _avg(key: str) -> float:
        vals = [f.get(key, 0.0) for f in reference_features]
        return sum(vals) / len(vals)

    return {
        "zone_proportions": centroid_proportions,
        "adjacency_graph": union_edges,
        "avg_passage_width_mm": _avg("avg_passage_width_mm"),
        "cabin_count": _avg("cabin_count"),
        "head_count": _avg("head_count"),
        "deck_height_avg": _avg("deck_height_avg"),
    }


def _features_to_vector(features: dict) -> list[float]:
    """Convert a feature dict to a flat numeric vector for cosine similarity.

    Layout:
    - Zone proportion values, sorted alphabetically by zone_type key
    - avg_passage_width_mm (normalised by 1000)
    - cabin_count
    - head_count
    - deck_height_avg (normalised by 1000)

    Args:
        features: Feature dict from compute_feature_vector() or compute_brand_centroid().

    Returns:
        List of floats.
    """
    proportions = features.get("zone_proportions", {})
    sorted_types = sorted(proportions.keys())
    vector = [proportions[t] for t in sorted_types]

    vector.append(features.get("avg_passage_width_mm", 0.0) / 1000.0)
    vector.append(float(features.get("cabin_count", 0)))
    vector.append(float(features.get("head_count", 0)))
    vector.append(features.get("deck_height_avg", 0.0) / 1000.0)

    return vector


def _align_vectors(vec_a: list[float], keys_a: list[str], keys_b: list[str]) -> list[float]:
    """Align vector_a to the union of keys_a and keys_b, inserting 0 for missing keys.

    Used so two feature vectors with different zone_type keys can be compared.
    """
    all_keys = sorted(set(keys_a) | set(keys_b))
    a_by_key = dict(zip(keys_a, vec_a[: len(keys_a)]))
    # scalar tail (last 4 elements after zone proportions)
    a_scalars = vec_a[len(keys_a):]

    aligned = [a_by_key.get(k, 0.0) for k in all_keys]
    aligned.extend(a_scalars)
    return aligned


# ---------------------------------------------------------------------------
# Sub-analysis 1: Layout topology
# ---------------------------------------------------------------------------


def analyze_layout_topology(
    new_features: dict,
    reference_features: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare the adjacency graph of the new layout against reference models.

    Score = (common edges / union edges) × 100.
    Emits BRAND_TOPOLOGY_DEVIATION if score < 60.

    Args:
        new_features: Feature dict for the new layout.
        reference_features: List of feature dicts from brand references.
        config: Active configuration dict.

    Returns:
        (score 0–100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not reference_features:
        return 50.0, warnings, {"common_edges": 0, "union_edges": 0, "overlap_ratio": 0.0}

    new_edges: set[frozenset] = new_features.get("adjacency_graph", set())

    # Union of all reference edges
    ref_union: set[frozenset] = set()
    for rf in reference_features:
        ref_union.update(rf.get("adjacency_graph", set()))

    if not new_edges and not ref_union:
        return 50.0, warnings, {"common_edges": 0, "union_edges": 0, "overlap_ratio": 0.0}

    total_union = new_edges | ref_union
    common = new_edges & ref_union

    union_count = len(total_union)
    common_count = len(common)
    overlap = common_count / union_count if union_count > 0 else 0.0
    score = overlap * 100.0

    if score < 60.0:
        missing = sorted(str(set(e)) for e in (ref_union - new_edges))
        extra = sorted(str(set(e)) for e in (new_edges - ref_union))
        detail_parts = []
        if missing:
            detail_parts.append(f"Fehlende Verbindungen: {', '.join(missing[:3])}")
        if extra:
            detail_parts.append(f"Unbekannte Verbindungen: {', '.join(extra[:3])}")
        detail = "; ".join(detail_parts) if detail_parts else "Abweichende Zonenstruktur."
        warnings.append({
            "code": "BRAND_TOPOLOGY_DEVIATION",
            "severity": "warning",
            "message": (
                f"Zonentopologie weicht von der Markenidentität ab "
                f"(Übereinstimmung: {score:.0f}%). {detail}"
            ),
            "suggestion": (
                "Zonenverbindungen an typische Markenmodelle angleichen, "
                "um die räumliche Kontinuität der Baureihe sicherzustellen."
            ),
        })

    return round(score, 1), warnings, {
        "common_edges": common_count,
        "union_edges": union_count,
        "overlap_ratio": round(overlap, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 2: Proportion consistency
# ---------------------------------------------------------------------------


def analyze_proportion_consistency(
    new_features: dict,
    reference_features: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if zone proportions match the brand's typical range.

    Per zone_type: computes mean and standard deviation from references.
    If the new design's proportion deviates by more than
    `proportion_deviation_threshold` × std, emits BRAND_PROPORTION_OUTLIER.
    Score = 100 − 10 × number_of_deviating_zone_types (floor 0).

    Args:
        new_features: Feature dict for the new layout.
        reference_features: List of feature dicts from brand references.
        config: Active configuration dict.

    Returns:
        (score 0–100, warnings, metrics dict).
    """
    warnings: list[dict] = []
    threshold = config.get("proportion_deviation_threshold", 2.0)

    if not reference_features:
        return 50.0, warnings, {"deviating_types": [], "checked_types": []}

    new_props: dict[str, float] = new_features.get("zone_proportions", {})

    # Collect all zone types from references
    ref_types: set[str] = set()
    for rf in reference_features:
        ref_types.update(rf.get("zone_proportions", {}).keys())

    deviating: list[str] = []
    checked: list[str] = []

    for ztype in ref_types:
        ref_vals = [rf.get("zone_proportions", {}).get(ztype, 0.0) for rf in reference_features]
        mean = sum(ref_vals) / len(ref_vals)
        variance = sum((v - mean) ** 2 for v in ref_vals) / len(ref_vals)
        std = math.sqrt(variance)

        new_val = new_props.get(ztype, 0.0)
        checked.append(ztype)

        # Only flag if std > 0 (otherwise every value is "normal")
        if std > 0 and abs(new_val - mean) > threshold * std:
            deviating.append(ztype)
            warnings.append({
                "code": "BRAND_PROPORTION_OUTLIER",
                "severity": "warning",
                "message": (
                    f"Zonentyp '{ztype}': Flächenanteil {new_val:.1%} weicht deutlich "
                    f"vom Marken-Mittelwert {mean:.1%} ± {std:.1%} ab."
                ),
                "suggestion": (
                    f"Flächenanteil für '{ztype}' auf ca. {mean:.1%} anpassen, "
                    f"um Markenkontinuität zu wahren."
                ),
            })

    score = max(0.0, 100.0 - 10.0 * len(deviating))

    return round(score, 1), warnings, {
        "deviating_types": deviating,
        "checked_types": checked,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 3: Material palette
# ---------------------------------------------------------------------------


def analyze_material_palette(
    new_materials: list[str],
    reference_materials: list[list[str]],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare the new design's material categories against brand references.

    Computes: overlap(new, union_of_ref_materials) / len(new) × 100.
    Emits BRAND_MATERIAL_UNKNOWN for each category absent from all references.

    Args:
        new_materials: List of material category strings for the new layout.
        reference_materials: List of lists — one list per reference model.
        config: Active configuration dict.

    Returns:
        (score 0–100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not new_materials:
        warnings.append({
            "code": "BRAND_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialangaben für die neue Planung vorhanden.",
            "suggestion": "Materialkategorien in den Zoneneigenschaften hinterlegen.",
        })
        return 50.0, warnings, {"known_categories": [], "unknown_categories": [], "overlap_ratio": 0.0}

    if not reference_materials:
        return 50.0, warnings, {"known_categories": list(new_materials), "unknown_categories": [], "overlap_ratio": 0.0}

    # Union of all reference material categories
    ref_union: set[str] = set()
    for rm in reference_materials:
        ref_union.update(rm)

    new_set = set(new_materials)
    known = sorted(new_set & ref_union)
    unknown = sorted(new_set - ref_union)

    for cat in unknown:
        warnings.append({
            "code": "BRAND_MATERIAL_UNKNOWN",
            "severity": "warning",
            "message": (
                f"Materialkategorie '{cat}' ist in keinem Referenzmodell der Werft vorhanden."
            ),
            "suggestion": (
                f"Prüfen, ob '{cat}' bewusst eingesetzt wird oder durch eine "
                f"markentypische Materialkategorie ersetzt werden sollte."
            ),
        })

    overlap = len(known) / len(new_set) if new_set else 0.0
    score = overlap * 100.0

    return round(score, 1), warnings, {
        "known_categories": known,
        "unknown_categories": unknown,
        "overlap_ratio": round(overlap, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 4: Spatial signature
# ---------------------------------------------------------------------------


def analyze_spatial_signature(
    new_features: dict,
    brand_centroid: dict,
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compute cosine similarity between the new layout and the brand centroid.

    Score = cosine_similarity × 100.  Emits BRAND_SPATIAL_DEVIATION if < 70.

    The feature vectors must share the same zone_type key space, so alignment
    padding is applied before computing similarity.

    Args:
        new_features: Feature dict for the new layout.
        brand_centroid: Aggregated centroid from compute_brand_centroid().
        config: Active configuration dict.

    Returns:
        (score 0–100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    new_props = new_features.get("zone_proportions", {})
    centroid_props = brand_centroid.get("zone_proportions", {})

    new_keys = sorted(new_props.keys())
    centroid_keys = sorted(centroid_props.keys())
    all_keys = sorted(set(new_keys) | set(centroid_keys))

    # Build padded vectors
    new_vec = [new_props.get(k, 0.0) for k in all_keys] + [
        new_features.get("avg_passage_width_mm", 0.0) / 1000.0,
        float(new_features.get("cabin_count", 0)),
        float(new_features.get("head_count", 0)),
        new_features.get("deck_height_avg", 0.0) / 1000.0,
    ]
    centroid_vec = [centroid_props.get(k, 0.0) for k in all_keys] + [
        brand_centroid.get("avg_passage_width_mm", 0.0) / 1000.0,
        float(brand_centroid.get("cabin_count", 0.0)),
        float(brand_centroid.get("head_count", 0.0)),
        brand_centroid.get("deck_height_avg", 0.0) / 1000.0,
    ]

    similarity = _cosine_similarity(new_vec, centroid_vec)
    score = max(0.0, min(100.0, similarity * 100.0))

    if score < 70.0:
        warnings.append({
            "code": "BRAND_SPATIAL_DEVIATION",
            "severity": "warning",
            "message": (
                f"Räumliche Signatur des Entwurfs stimmt nur zu {score:.0f}% "
                f"mit dem Marken-Profil überein."
            ),
            "suggestion": (
                "Flächenverteilung, Kabinen-/Sanitäranzahl und Raumhöhen "
                "stärker an die Referenzmodelle der Werft angleichen."
            ),
        })

    return round(score, 1), warnings, {"cosine_similarity": round(similarity, 4)}


# ---------------------------------------------------------------------------
# Sub-analysis 5: Style continuity
# ---------------------------------------------------------------------------


def analyze_style_continuity(
    new_tags: list[str],
    reference_tags_list: list[list[str]],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare style tags of the new layout against brand reference tags.

    Identifies the most common tags across references (present in > 50% of
    models) as the brand's style signature.  Score = overlap / total brand
    tags × 100.  Emits BRAND_STYLE_SHIFT if score < 60.

    Args:
        new_tags: Style tags for the new layout (e.g. ["minimalist", "teak"]).
        reference_tags_list: List of tag lists, one per reference model.
        config: Active configuration dict.

    Returns:
        (score 0–100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not reference_tags_list:
        return 50.0, warnings, {
            "brand_signature_tags": [],
            "new_tags": list(new_tags),
            "overlap": [],
            "missing": [],
        }

    # Determine brand signature: tags present in >50% of reference models
    n_refs = len(reference_tags_list)
    tag_counts: dict[str, int] = {}
    for tags in reference_tags_list:
        for t in tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1

    brand_signature = sorted(t for t, count in tag_counts.items() if count > n_refs / 2)

    if not brand_signature:
        # No dominant tags — lenient scoring
        return 75.0, warnings, {
            "brand_signature_tags": [],
            "new_tags": list(new_tags),
            "overlap": [],
            "missing": [],
        }

    new_set = set(new_tags)
    sig_set = set(brand_signature)
    overlap = sorted(new_set & sig_set)
    missing = sorted(sig_set - new_set)

    ratio = len(overlap) / len(sig_set) if sig_set else 0.0
    score = ratio * 100.0

    if score < 60.0:
        missing_str = ", ".join(f"'{t}'" for t in missing[:5])
        warnings.append({
            "code": "BRAND_STYLE_SHIFT",
            "severity": "warning",
            "message": (
                f"Stilsprache weicht von der Markenidentität ab "
                f"(Übereinstimmung: {score:.0f}%). "
                f"Fehlende Marken-Tags: {missing_str}."
            ),
            "suggestion": (
                "Stilmerkmale der Referenzmodelle übernehmen, um einen "
                "konsistenten Markenauftritt sicherzustellen."
            ),
        })

    return round(score, 1), warnings, {
        "brand_signature_tags": brand_signature,
        "new_tags": list(new_tags),
        "overlap": overlap,
        "missing": missing,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_brand_dna_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    brand_references: list[dict] | None = None,
    data_source: str = "measured",
) -> dict:
    """Orchestrator — runs all Brand DNA sub-analyses.

    Each brand reference dict must contain:
    - features (dict): pre-computed feature dict (from compute_feature_vector)
      OR will be computed from zones/passages if not provided
    - materials (list[str]): material category strings
    - style_tags (list[str]): style descriptor tags

    If brand_references is None or contains fewer models than
    `min_reference_models`, returns score 50.0 with an informational warning.

    Args:
        zones: Layout zones for the new design.
        passages: Layout passages for the new design.
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.
        brand_references: List of reference model dicts from the shipyard portfolio.

    Returns:
        Standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    min_refs = config.get("min_reference_models", 3)

    # --- Insufficient reference data ---
    if not brand_references or len(brand_references) < min_refs:
        actual = len(brand_references) if brand_references else 0
        return {
            "module": "brand_dna",
            "overall_score": 50.0,
            "sub_scores": {k: 50.0 for k in weights},
            "warnings": [
                {
                    "code": "BRAND_INSUFFICIENT_DATA",
                    "severity": "info",
                    "message": (
                        f"Brand DNA nicht verfügbar — mindestens {min_refs} "
                        f"Referenzmodelle erforderlich (vorhanden: {actual})."
                    ),
                    "suggestion": (
                        f"Mindestens {min_refs} frühere Modelle der Werft als "
                        f"Referenz hinterlegen, um die Markenanalyse zu aktivieren."
                    ),
                }
            ],
            "suggestions": [
                f"Mindestens {min_refs} frühere Modelle der Werft als "
                f"Referenz hinterlegen, um die Markenanalyse zu aktivieren."
            ],
            "metrics": {},
            "config_used": config,
            "confidence": data_source,
            "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        }

    # --- Feature extraction for new layout ---
    new_features = compute_feature_vector(zones, passages)

    # --- Extract reference components ---
    reference_features: list[dict] = []
    reference_materials: list[list[str]] = []
    reference_tags_list: list[list[str]] = []

    for ref in brand_references:
        feats = ref.get("features")
        if feats is None:
            ref_zones = ref.get("zones", [])
            ref_passages = ref.get("passages", [])
            feats = compute_feature_vector(ref_zones, ref_passages)
        reference_features.append(feats)
        reference_materials.append(ref.get("materials") or [])
        reference_tags_list.append(ref.get("style_tags") or [])

    brand_centroid = compute_brand_centroid(reference_features)

    # New layout material categories and style tags
    new_materials: list[str] = []
    for z in zones:
        props = z.get("properties") or {}
        cats = props.get("material_categories")
        if isinstance(cats, list):
            new_materials.extend(cats)

    new_tags: list[str] = []
    for z in zones:
        props = z.get("properties") or {}
        tags = props.get("style_tags")
        if isinstance(tags, list):
            new_tags.extend(tags)

    # --- Sub-analyses ---
    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_metrics: dict[str, dict] = {}

    analyses: list[tuple[str, object]] = [
        (
            "topology",
            lambda: analyze_layout_topology(new_features, reference_features, config),
        ),
        (
            "proportions",
            lambda: analyze_proportion_consistency(new_features, reference_features, config),
        ),
        (
            "materials",
            lambda: analyze_material_palette(new_materials, reference_materials, config),
        ),
        (
            "spatial",
            lambda: analyze_spatial_signature(new_features, brand_centroid, config),
        ),
        (
            "style",
            lambda: analyze_style_continuity(new_tags, reference_tags_list, config),
        ),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()  # type: ignore[operator]
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in brand_dna sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Brand-DNA-Analyse: {name}",
                "suggestion": "Eingabedaten und Referenzmodelle überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    # Collect unique suggestions from warnings
    all_suggestions: list[str] = []
    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "brand_dna",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
