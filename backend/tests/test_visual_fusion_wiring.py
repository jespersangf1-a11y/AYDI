"""Pipeline B beeinflusst die Bewertung — vorher war sie folgenlos.

``score_fusion.py`` war vollstaendig implementiert und getestet, hatte aber
**keinen einzigen Aufrufer**: Ein hochgeladenes und analysiertes Foto veraenderte
keinen Score, waehrend CLAUDE.md eine Gewichtstabelle fuehrte, die nichts
steuerte.

Zwei Dinge fehlten dazwischen und sind der Grund fuer ``visual_fusion.py``:

* **Andere Schluesselung** — die Fusion erwartet Ergebnisse je *Modul*, der
  Analyzer liefert sie je *Bild*.
* **Anderes Konfidenzformat** — die Fusion erwartet einen String, der Analyzer
  liefert ein Dict. ``CONFIDENCE_DISCOUNT.get(dict)`` waere mit
  ``TypeError: unhashable type: 'dict'`` abgebrochen; die Fusion war also nicht
  nur unverdrahtet, sie waere beim blossen Anschliessen abgestuerzt.
"""

import asyncio

import pytest

from app.services.analysis.orchestrator import AnalysisContext, run_full_analysis
from app.services.analysis.visual_fusion import (
    IMAGE_TYPE_TO_MODULES,
    visual_results_to_module_scores,
)

ZONES = [
    {
        "name": name,
        "zone_type": zone_type,
        "polygon": [[0, i * 1500], [3200, i * 1500], [3200, (i + 1) * 1500], [0, (i + 1) * 1500]],
        "height_mm": 1900,
    }
    for i, (name, zone_type) in enumerate(
        [("Salon", "saloon"), ("Kabine", "cabin"), ("Nasszelle", "head"), ("Cockpit", "cockpit")]
    )
]
PASSAGES = [{"name": "P1", "from_zone": "Salon", "to_zone": "Kabine", "width_mm": 620}]


def _analysis(visual: list[dict] | None = None) -> dict:
    return asyncio.run(
        run_full_analysis(
            AnalysisContext(
                zones=ZONES,
                passages=PASSAGES,
                boat_class="cruising_sail",
                length_m=10.85,
                beam_m=3.50,
                tier="pro",
                visual_analyses=visual or [],
            )
        )
    )


def _photo(score: float, level: str = "visual_high", usable: bool = True) -> dict:
    """Ein Ergebnis im ECHTEN Analyzer-Format — confidence als Dict."""
    return {
        "image_type": "interior_overview",
        "score": score,
        "confidence": {"level": level, "is_usable": usable, "image_quality": 0.9},
    }


class TestAdapter:
    def test_nested_confidence_dict_is_accepted(self):
        """Genau hier waere die Fusion abgestuerzt."""
        result = visual_results_to_module_scores([_photo(80.0)])
        assert result
        assert all(isinstance(v["confidence"], str) for v in result.values())

    def test_flat_confidence_string_is_also_accepted(self):
        flat = {"image_type": "interior_overview", "score": 80.0, "confidence": "visual_high"}
        assert visual_results_to_module_scores([flat])

    def test_unusable_result_is_dropped(self):
        """Der Waechter hat Unsicherheit festgestellt — sie darf keine Zahl werden."""
        assert visual_results_to_module_scores([_photo(90.0, usable=False)]) == {}

    def test_insufficient_confidence_is_dropped(self):
        assert visual_results_to_module_scores([_photo(90.0, level="visual_insufficient")]) == {}

    def test_error_result_is_dropped(self):
        broken = {"image_type": "interior_overview", "score": 0.0, "error": "API-Fehler"}
        assert visual_results_to_module_scores([broken]) == {}

    def test_unknown_image_type_contributes_to_nothing(self):
        """Lieber keine Aussage als eine hergeleitete."""
        odd = {"image_type": "drohnenaufnahme", "score": 90.0, "confidence": "visual_high"}
        assert visual_results_to_module_scores([odd]) == {}

    def test_several_images_are_averaged(self):
        result = visual_results_to_module_scores([_photo(60.0), _photo(80.0)])
        assert result["ergonomics"]["score"] == pytest.approx(70.0)
        assert result["ergonomics"]["image_count"] == 2

    def test_worst_confidence_wins(self):
        """Zwei mittelmaessige Fotos ergeben keine hohe Sicherheit."""
        result = visual_results_to_module_scores(
            [_photo(70.0, "visual_high"), _photo(70.0, "visual_low")]
        )
        assert result["ergonomics"]["confidence"] == "visual_low"

    def test_empty_input_is_harmless(self):
        assert visual_results_to_module_scores(None) == {}
        assert visual_results_to_module_scores([]) == {}

    def test_every_mapped_module_is_a_real_module(self):
        from app.services.analysis.orchestrator import ALL_MODULE_NAMES

        for image_type, modules in IMAGE_TYPE_TO_MODULES.items():
            unknown = set(modules) - ALL_MODULE_NAMES
            assert not unknown, f"{image_type} zeigt auf unbekannte Module: {unknown}"

    def test_every_mapped_image_type_exists(self):
        from app.services.visual.prompts import PROMPT_REGISTRY

        unknown = set(IMAGE_TYPE_TO_MODULES) - set(PROMPT_REGISTRY)
        assert not unknown, f"Bildtypen ohne Prompt: {unknown}"


class TestFusionImOrchestrator:
    def test_without_photos_nothing_changes(self):
        """Die Fusion ist rein additiv."""
        result = _analysis()
        assert result["fused_module_count"] == 0
        assert result["fusion"] == {}

    def test_a_photo_moves_the_overall_score(self):
        """Der Kern des Befunds: Vorher blieb die Note identisch."""
        without = _analysis()["overall_score"]
        with_good = _analysis([_photo(90.0)])["overall_score"]
        assert with_good != without

    def test_a_better_photo_never_scores_worse_than_a_bad_one(self):
        good = _analysis([_photo(90.0)])["overall_score"]
        bad = _analysis([_photo(30.0)])["overall_score"]
        assert good >= bad

    def test_structured_score_is_preserved(self):
        """Nachvollziehbarkeit: Beide Rohwerte bleiben sichtbar."""
        result = _analysis([_photo(85.0)])
        module = result["modules"]["ergonomics"]
        assert module.get("structured_score") is not None
        assert module.get("fusion")

    def test_unusable_photo_behaves_like_no_photo(self):
        assert (
            _analysis([_photo(90.0, usable=False)])["overall_score"]
            == _analysis()["overall_score"]
        )


class TestWiderspruchsregel:
    """CLAUDE.md: 'CAD vs photo discrepancy -> flag, don't average.'"""

    @pytest.fixture(scope="class")
    def conflicted(self) -> dict:
        # Strukturiert liegt hier deutlich unter 95 -> Abstand > 25 Punkte.
        return _analysis([_photo(95.0)])["modules"]["ergonomics"]

    def test_disagreement_is_flagged(self, conflicted):
        assert conflicted.get("needs_review") is True

    def test_disagreement_is_not_averaged(self, conflicted):
        """Die strukturierte Messung bleibt massgeblich."""
        assert conflicted["overall_score"] == conflicted["structured_score"]

    def test_visual_weight_drops_to_zero_in_conflict(self, conflicted):
        assert conflicted["fusion"]["fusion_weights"] == {"structured": 1.0, "visual": 0.0}

    def test_both_raw_scores_stay_visible(self, conflicted):
        disagreement = conflicted["fusion"]["disagreement"]
        assert disagreement["structured_score"] is not None
        assert disagreement["visual_score"] is not None
        assert "abweichen" in disagreement["message"].lower() or "weichen" in disagreement["message"].lower()

    def test_agreement_blends_instead(self):
        """Bei kleinem Abstand wird gemischt — sonst waere die Fusion wirkungslos."""
        structured = _analysis()["modules"]["ergonomics"]["overall_score"]
        blended = _analysis([_photo(structured + 5.0)])["modules"]["ergonomics"]
        assert blended.get("needs_review") is not True
        assert blended["overall_score"] != blended["structured_score"]
