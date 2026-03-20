"""Integration tests for Community Intelligence with orchestrator and resolver."""
import pytest
from tests.conftest import make_zone, make_passage, make_community_pattern


class TestOrchestratorIntegration:
    def test_community_in_execution_tiers(self):
        from app.services.analysis.orchestrator import EXECUTION_TIERS
        tier1 = EXECUTION_TIERS[0]
        assert "community" in tier1

    def test_community_in_overall_weights(self):
        from app.services.analysis.orchestrator import OVERALL_WEIGHTS
        for boat_class in ["small_sail", "cruising_sail", "large_motor", "superyacht"]:
            assert "community" in OVERALL_WEIGHTS[boat_class]

    def test_build_module_kwargs_community(self):
        from app.services.analysis.orchestrator import _build_module_kwargs, AnalysisContext
        context = AnalysisContext(
            zones=[make_zone("salon", "salon")],
            passages=[make_passage("salon", "cockpit")],
            boat_class="cruising_sail",
        )
        context.community_patterns = [make_community_pattern()]
        kwargs = _build_module_kwargs("community", context)
        assert "community_patterns" in kwargs
        assert len(kwargs["community_patterns"]) == 1

    def test_community_module_runs_in_orchestrator(self):
        """Full orchestrator run with community patterns."""
        import asyncio
        from app.services.analysis.orchestrator import run_full_analysis, AnalysisContext

        context = AnalysisContext(
            zones=[make_zone("salon", "salon"), make_zone("cockpit", "cockpit")],
            passages=[make_passage("salon", "cockpit")],
            boat_class="cruising_sail",
        )
        context.community_patterns = [
            make_community_pattern(severity_mode="major", confidence=0.7),
        ]

        result = asyncio.run(run_full_analysis(context))
        module_names = list(result.get("modules", {}).keys())
        assert "community" in module_names


class TestScoreFusionIntegration:
    def test_community_in_fusion_weights(self):
        from app.services.analysis.score_fusion import FUSION_WEIGHTS
        assert "community" in FUSION_WEIGHTS
        assert FUSION_WEIGHTS["community"] == (1.0, 0.0)


class TestBoatDNAResolverIntegration:
    def test_resolver_includes_community_config(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        dna = BoatDNA.from_boat_class("cruising_sail")
        resolver = BoatDNAResolver()
        result = resolver.resolve(dna)

        assert "community" in result
        assert "min_confidence" in result["community"]
        assert "max_patterns" in result["community"]

    def test_resolver_overall_weights_include_community(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        dna = BoatDNA.from_boat_class("cruising_sail")
        resolver = BoatDNAResolver()
        result = resolver.resolve(dna)

        assert "overall_weights" in result
        assert "community" in result["overall_weights"]
        assert result["overall_weights"]["community"] > 0

    def test_all_weights_sum_to_one(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        for bc in ["small_sail", "cruising_sail", "large_motor", "superyacht"]:
            dna = BoatDNA.from_boat_class(bc)
            resolver = BoatDNAResolver()
            result = resolver.resolve(dna)
            weights = result["overall_weights"]
            total = sum(weights.values())
            assert abs(total - 1.0) < 0.001, f"{bc}: weights sum to {total}"
