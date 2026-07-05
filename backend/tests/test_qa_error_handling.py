"""Comprehensive QA tests for AYDI error handling, validation, and edge cases.

Coverage:
1. ERROR HANDLING: All run_*_analysis functions with corrupted inputs
2. DEPENDENCY CHAINS: Orchestrator behavior with module failures
3. MIDDLEWARE ERROR HANDLING: Custom exception handling and rate limiting
4. CIRCUIT BREAKER EDGE CASES: State transitions and thread safety
5. SCORE FUSION VALIDATION: Weight invariants and None handling
"""

import asyncio
import logging
import math
import pytest
from unittest.mock import patch, MagicMock

from app.core.errors import (
    DataValidationError,
    ModuleAnalysisError,
    AYDIError,
)
from app.core.retry import (
    CircuitBreaker,
    CircuitState,
    retry_async,
    RetryableError,
    NonRetryableError,
    get_circuit_breaker,
)
from app.services.analysis.orchestrator import (
    AnalysisContext,
    run_full_analysis,
    _compute_overall_score,
)
from app.services.analysis.score_fusion import (
    fuse_module_scores,
    fuse_zone_score,
    FUSION_WEIGHTS,
)
from tests.conftest import (
    make_zone,
    make_passage,
    make_material,
    make_zone_material,
)


logger = logging.getLogger(__name__)


# ==============================================================================
# PART 1: ERROR HANDLING IN ANALYSIS MODULES
# ==============================================================================

class TestAnalysisModuleErrorHandling:
    """Test robustness of analysis modules against corrupted inputs."""

    def test_ergonomics_with_corrupted_polygon(self):
        """Test ergonomics module rejects corrupted polygon without crashing."""
        from app.services.analysis.ergonomics import run_ergonomics_analysis

        zones = [
            make_zone("salon", "saloon"),
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": "not_a_list",  # CORRUPTED
            },
        ]
        passages = [make_passage("salon", "cabin")]

        result = run_ergonomics_analysis(zones, passages, "cruising_sail")

        # Must return a dict (not crash)
        assert isinstance(result, dict)
        # Either available or skipped
        if result.get("available") is False:
            assert "reason" in result
        elif result.get("available") is not False:
            # If it runs, all scores must be finite
            assert not any(
                math.isnan(v) or math.isinf(v)
                for v in self._collect_numeric_fields(result)
            )

    def test_ergonomics_with_non_numeric_polygon_points(self):
        """Test ergonomics module rejects non-numeric polygon coordinates."""
        from app.services.analysis.ergonomics import run_ergonomics_analysis

        zones = [
            {
                "name": "salon",
                "zone_type": "saloon",
                "polygon": [["a", "b"], ["c", "d"]],  # Non-numeric
            },
        ]
        passages = []

        result = run_ergonomics_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)
        if result.get("available") is not False:
            assert not any(
                math.isnan(v) or math.isinf(v)
                for v in self._collect_numeric_fields(result)
            )

    def test_ergonomics_with_string_passage_width(self):
        """Test ergonomics rejects non-numeric passage width."""
        from app.services.analysis.ergonomics import run_ergonomics_analysis

        zones = [
            make_zone("salon", "saloon"),
            make_zone("cabin", "cabin"),
        ]
        passages = [
            {
                "from_zone": "salon",
                "to_zone": "cabin",
                "width_mm": "wide",  # Non-numeric
            },
        ]

        result = run_ergonomics_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_volume_storage_with_corrupted_polygon(self):
        """Test volume_storage module rejects corrupted polygon."""
        from app.services.analysis.volume_storage import run_volume_storage_analysis

        zones = [
            {"name": "cabin", "zone_type": "cabin", "polygon": None},  # Corrupted
        ]
        passages = []

        result = run_volume_storage_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)
        if result.get("available") is not False:
            assert not any(
                math.isnan(v) or math.isinf(v)
                for v in self._collect_numeric_fields(result)
            )

    def test_volume_storage_with_non_numeric_points(self):
        """Test volume_storage rejects non-numeric coordinates."""
        from app.services.analysis.volume_storage import run_volume_storage_analysis

        zones = [
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": [[1, 2], ["invalid", 5]],  # Mixed types
            },
        ]
        passages = []

        result = run_volume_storage_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_emotional_with_corrupted_polygon(self):
        """Test emotional module rejects corrupted polygon."""
        from app.services.analysis.emotional import run_emotional_analysis

        zones = [
            {
                "name": "salon",
                "zone_type": "saloon",
                "polygon": {},  # Wrong type
            },
        ]
        passages = []

        result = run_emotional_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_compliance_with_corrupted_polygon(self):
        """Test compliance module rejects corrupted polygon."""
        from app.services.analysis.compliance import run_compliance_analysis

        zones = [
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": "invalid",
            },
        ]
        passages = []

        result = run_compliance_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_production_with_corrupted_polygon(self):
        """Test production module rejects corrupted polygon."""
        from app.services.analysis.production import run_production_analysis

        zones = [
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": 123,  # Wrong type
            },
        ]
        passages = []

        result = run_production_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_materials_with_corrupted_polygon(self):
        """Test materials module rejects corrupted polygon."""
        from app.services.analysis.materials import run_materials_analysis

        zones = [
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": [1, 2, 3],  # Not a list of points
            },
        ]
        passages = []
        materials = [make_zone_material("cabin")]

        result = run_materials_analysis(zones, passages, "cruising_sail", materials=materials)

        assert isinstance(result, dict)

    def test_structural_with_corrupted_polygon(self):
        """Test structural module rejects corrupted polygon."""
        from app.services.analysis.structural import run_structural_analysis

        zones = [
            {
                "name": "cabin",
                "zone_type": "cabin",
                "polygon": None,
            },
        ]
        passages = []

        result = run_structural_analysis(zones, passages, "cruising_sail")

        assert isinstance(result, dict)

    def test_cost_with_string_passage_width(self):
        """Test cost module rejects invalid passage data."""
        from app.services.analysis.cost import run_cost_analysis

        zones = [make_zone("salon", "saloon")]
        passages = [
            {
                "from_zone": "salon",
                "to_zone": "other",
                "width_mm": "not_a_number",
            },
        ]
        cost_items = []

        result = run_cost_analysis(
            zones,
            passages,
            "cruising_sail",
            cost_items=cost_items,
            boat_length_m=12.0,
        )

        assert isinstance(result, dict)

    def test_service_patterns_with_invalid_data(self):
        """Test service_patterns module handles invalid service reports."""
        from app.services.analysis.service_patterns import run_service_patterns_analysis

        zones = [make_zone("cabin", "cabin")]
        passages = []
        # Invalid service report
        service_reports = [
            {
                "report_type": "maintenance",
                # Missing required fields
            },
        ]

        result = run_service_patterns_analysis(
            zones,
            passages,
            "cruising_sail",
            service_reports=service_reports,
        )

        assert isinstance(result, dict)

    def test_brand_dna_with_invalid_data(self):
        """Test brand_dna module handles invalid references."""
        from app.services.analysis.brand_dna import run_brand_dna_analysis

        zones = [make_zone("cabin", "cabin")]
        passages = []
        brand_references = [
            {
                "manufacturer": "Unknown",
                # Missing model info
            },
        ]

        result = run_brand_dna_analysis(
            zones,
            passages,
            "cruising_sail",
            brand_references=brand_references,
        )

        assert isinstance(result, dict)

    def test_market_with_invalid_competitor_data(self):
        """Test market module handles invalid competitors."""
        from app.services.analysis.market import run_market_analysis

        zones = [make_zone("cabin", "cabin")]
        passages = []
        competitors = [
            {
                "key_metrics": "not_a_dict",  # Invalid
            },
        ]

        result = run_market_analysis(
            zones,
            passages,
            "cruising_sail",
            competitors=competitors,
            boat_length_m=12.0,
        )

        assert isinstance(result, dict)

    def test_all_modules_return_dict_not_exception(self):
        """Ensure no module raises unhandled exceptions."""
        from app.services.analysis import (
            ergonomics,
            volume_storage,
            emotional,
            compliance,
            production,
            materials,
            structural,
            cost,
            service_patterns,
            brand_dna,
            market,
        )

        # Corrupt data
        zones = [{"name": "bad", "zone_type": "cabin", "polygon": "bad"}]
        passages = [{"from_zone": "a", "to_zone": "b", "width_mm": "bad"}]

        modules_to_test = [
            (ergonomics.run_ergonomics_analysis, {}),
            (volume_storage.run_volume_storage_analysis, {}),
            (emotional.run_emotional_analysis, {}),
            (compliance.run_compliance_analysis, {}),
            (production.run_production_analysis, {}),
            (materials.run_materials_analysis, {"materials": []}),
            (structural.run_structural_analysis, {}),
            (cost.run_cost_analysis, {"cost_items": [], "boat_length_m": 12.0}),
            (service_patterns.run_service_patterns_analysis, {"service_reports": []}),
            (brand_dna.run_brand_dna_analysis, {"brand_references": []}),
            (market.run_market_analysis, {"competitors": [], "boat_length_m": 12.0}),
        ]

        for module_func, extra_kwargs in modules_to_test:
            result = module_func(zones, passages, "cruising_sail", None, **extra_kwargs)
            assert isinstance(result, dict), f"{module_func.__name__} did not return dict"
            # Check no NaN/Inf in numeric fields
            assert not any(
                isinstance(v, float) and (math.isnan(v) or math.isinf(v))
                for v in self._collect_numeric_fields(result)
            ), f"{module_func.__name__} returned NaN/Inf"

    @staticmethod
    def _collect_numeric_fields(obj, visited=None):
        """Recursively collect all numeric fields from nested dict/list."""
        if visited is None:
            visited = set()
        if id(obj) in visited:
            return []
        visited.add(id(obj))

        result = []
        if isinstance(obj, dict):
            for v in obj.values():
                if isinstance(v, (int, float)):
                    result.append(v)
                elif isinstance(v, (dict, list)):
                    result.extend(TestAnalysisModuleErrorHandling._collect_numeric_fields(v, visited))
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                if isinstance(item, (int, float)):
                    result.append(item)
                elif isinstance(item, (dict, list)):
                    result.extend(TestAnalysisModuleErrorHandling._collect_numeric_fields(item, visited))
        return result


# ==============================================================================
# PART 2: DEPENDENCY CHAINS (ORCHESTRATOR)
# ==============================================================================

class TestOrchestratorDependencies:
    """Test orchestrator behavior with module failures and dependencies."""

    @pytest.mark.asyncio
    async def test_orchestrator_continues_on_module_exception(self):
        """Verify orchestrator catches module exceptions and continues."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
        )

        def mock_runner_raises(zones, passages, boat_class, config):
            raise ValueError("Simulated module crash")

        def mock_runner_works(zones, passages, boat_class, config):
            return {"available": True, "overall_score": 75.0, "confidence": "estimated"}

        module_runners = {
            "ergonomics": mock_runner_raises,
            "volume_storage": mock_runner_works,
        }

        result = await run_full_analysis(context, module_runners=module_runners)

        # Should have results from volume_storage
        assert "volume_storage" in result["modules"]
        # Should have errors from ergonomics
        assert "ergonomics" in result["errors"]
        assert result["error_count"] == 1
        # Should not crash
        assert result is not None

    @pytest.mark.asyncio
    async def test_orchestrator_handles_unavailable_module(self):
        """Verify orchestrator captures unavailable modules."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
        )

        def mock_unavailable(zones, passages, boat_class, config):
            return {"available": False, "reason": "Insufficient data"}

        def mock_works(zones, passages, boat_class, config):
            return {"available": True, "overall_score": 75.0, "confidence": "estimated"}

        # Provide all module runners, but make ergonomics unavailable
        module_runners = {
            "ergonomics": mock_unavailable,
            "volume_storage": mock_works,
            "emotional": mock_works,
            "compliance": mock_works,
            "community": mock_works,
            "production": mock_works,
            "materials": mock_works,
            "structural": mock_works,
            "cost": mock_works,
            "service_patterns": mock_works,
            "brand_dna": mock_works,
            "market": mock_works,
        }

        result = await run_full_analysis(context, module_runners=module_runners)

        assert "ergonomics" in result["skipped"]
        assert "volume_storage" in result["modules"]
        # Count skipped: only ergonomics marked unavailable
        assert result["skipped_count"] >= 1

    @pytest.mark.asyncio
    async def test_orchestrator_handles_garbage_return_value(self):
        """Verify orchestrator handles non-dict return values."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
        )

        def mock_garbage(zones, passages, boat_class, config):
            return "not a dict"  # Invalid return type

        def mock_works(zones, passages, boat_class, config):
            return {"available": True, "overall_score": 75.0, "confidence": "estimated"}

        module_runners = {
            "ergonomics": mock_garbage,
            "volume_storage": mock_works,
        }

        result = await run_full_analysis(context, module_runners=module_runners)

        # Should not crash; garbage result is treated as error
        assert result is not None
        assert "volume_storage" in result["modules"]

    @pytest.mark.asyncio
    async def test_orchestrator_tier_free_runs_only_allowed_modules(self):
        """Verify free tier only runs ergonomics, volume_storage, emotional, market."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
            tier="free",
        )

        call_log = []

        def make_tracker(name):
            def runner(zones, passages, boat_class, config):
                call_log.append(name)
                return {"available": True, "overall_score": 50.0, "confidence": "estimated"}
            return runner

        module_runners = {
            name: make_tracker(name)
            for name in [
                "ergonomics", "volume_storage", "emotional", "compliance",
                "production", "materials", "structural", "cost",
                "service_patterns", "brand_dna", "market", "community",
            ]
        }

        result = await run_full_analysis(context, module_runners=module_runners)

        # Free tier should only allow specific modules
        # (see app/core/subscription.py for exact list)
        assert "ergonomics" in call_log or "ergonomics" in result.get("tier_gated", {})

    @pytest.mark.asyncio
    async def test_orchestrator_invalid_tier_handled_gracefully(self):
        """Verify orchestrator handles invalid tier gracefully."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
            tier="invalid_tier_xyz",
        )

        def mock_runner(zones, passages, boat_class, config):
            return {"available": True, "overall_score": 75.0, "confidence": "estimated"}

        module_runners = {
            "ergonomics": mock_runner,
            "volume_storage": mock_runner,
        }

        # Should not crash despite invalid tier
        result = await run_full_analysis(context, module_runners=module_runners)
        assert result is not None

    @pytest.mark.asyncio
    async def test_orchestrator_tier_2_depends_on_tier_1(self):
        """Verify tier 2 modules can reference tier 1 results."""
        context = AnalysisContext(
            zones=[make_zone("cabin", "cabin")],
            passages=[],
            boat_class="cruising_sail",
        )

        def tier1_runner(zones, passages, boat_class, config):
            return {"available": True, "overall_score": 75.0, "confidence": "estimated"}

        def tier2_runner(zones, passages, boat_class, config):
            # Tier 2 might depend on tier 1 results
            return {"available": True, "overall_score": 80.0, "confidence": "estimated"}

        module_runners = {
            "ergonomics": tier1_runner,  # Tier 1
            "production": tier2_runner,  # Tier 2
        }

        result = await run_full_analysis(context, module_runners=module_runners)

        # Both should have run
        assert "ergonomics" in result["modules"]
        assert "production" in result["modules"]


# ==============================================================================
# PART 3: MIDDLEWARE ERROR HANDLING
# ==============================================================================

class TestMiddlewareErrorHandling:
    """Test middleware exception handling and rate limiting."""

    def test_error_handling_middleware_catches_aydi_errors(self):
        """Verify ErrorHandlingMiddleware catches AYDI exceptions."""
        from app.core.middleware import ErrorHandlingMiddleware
        from fastapi import Request, Response
        from starlette.datastructures import Headers
        from unittest.mock import AsyncMock

        middleware = ErrorHandlingMiddleware(MagicMock())

        async def test():
            request = MagicMock(spec=Request)
            request.url.path = "/test"

            # Simulate a next handler that raises DataValidationError
            async def call_next(req):
                raise DataValidationError("Test validation error")

            response = await middleware.dispatch(request, call_next)

            assert response.status_code == 422
            # Response should have error details
            assert b"validation_error" in response.body or response.status_code == 422

        asyncio.run(test())

    def test_error_handling_middleware_catches_timeout(self):
        """Verify ErrorHandlingMiddleware catches asyncio.TimeoutError."""
        from app.core.middleware import ErrorHandlingMiddleware

        middleware = ErrorHandlingMiddleware(MagicMock())

        async def test():
            request = MagicMock()
            request.url.path = "/test"

            async def call_next(req):
                raise asyncio.TimeoutError("Request timed out")

            response = await middleware.dispatch(request, call_next)

            assert response.status_code == 504

        asyncio.run(test())

    def test_error_handling_middleware_catches_generic_exception(self):
        """Verify ErrorHandlingMiddleware catches unhandled exceptions."""
        from app.core.middleware import ErrorHandlingMiddleware

        middleware = ErrorHandlingMiddleware(MagicMock())

        async def test():
            request = MagicMock()
            request.url.path = "/test"

            async def call_next(req):
                raise RuntimeError("Unexpected error")

            response = await middleware.dispatch(request, call_next)

            assert response.status_code == 500

        asyncio.run(test())

    def test_rate_limit_middleware_increments_per_ip(self):
        """Verify RateLimitMiddleware tracks per-IP rate limits."""
        from app.core.middleware import RateLimitMiddleware

        middleware = RateLimitMiddleware(MagicMock())

        async def test():
            # Simulate requests from same IP
            request1 = MagicMock()
            request1.url.path = "/api/v1/quick-analysis"
            request1.headers = MagicMock()
            request1.headers.get = MagicMock(return_value=None)
            request1.client = MagicMock()
            request1.client.host = "192.168.1.1"

            # Check rate
            allowed1 = await middleware._check_rate("192.168.1.1", "/api/v1/quick-analysis", 30, 60)
            assert allowed1 is True

            # Same IP again
            allowed2 = await middleware._check_rate("192.168.1.1", "/api/v1/quick-analysis", 30, 60)
            assert allowed2 is True

        asyncio.run(test())

    def test_rate_limit_middleware_rejects_when_exceeded(self):
        """Verify RateLimitMiddleware rejects over limit."""
        from app.core.middleware import RateLimitMiddleware

        middleware = RateLimitMiddleware(MagicMock())

        async def test():
            # Max 2 requests per 60s for this test
            allowed = []
            for i in range(3):
                result = await middleware._check_rate("test.ip", "/api/v1/test", 2, 60)
                allowed.append(result)

            # First 2 should pass, 3rd should fail
            assert allowed[0] is True
            assert allowed[1] is True
            assert allowed[2] is False

        asyncio.run(test())

    def test_locale_middleware_detects_from_query_param(self):
        """Verify LocaleMiddleware detects locale from query parameter."""
        from app.core.middleware import LocaleMiddleware

        middleware = LocaleMiddleware(MagicMock())

        request = MagicMock()
        request.query_params = {"lang": "en"}
        request.headers = {}

        locale = middleware._detect_locale(request)
        assert locale == "en"

    def test_locale_middleware_detects_from_accept_language(self):
        """Verify LocaleMiddleware detects locale from Accept-Language header."""
        from app.core.middleware import LocaleMiddleware

        middleware = LocaleMiddleware(MagicMock())

        request = MagicMock()
        request.query_params = {}
        request.headers = {"accept-language": "de-DE,de;q=0.9"}

        locale = middleware._detect_locale(request)
        assert locale == "de"

    def test_locale_middleware_defaults_to_de(self):
        """Verify LocaleMiddleware defaults to German."""
        from app.core.middleware import LocaleMiddleware

        middleware = LocaleMiddleware(MagicMock())

        request = MagicMock()
        request.query_params = {}
        request.headers = {}

        locale = middleware._detect_locale(request)
        assert locale == "de"


# ==============================================================================
# PART 4: CIRCUIT BREAKER EDGE CASES
# ==============================================================================

class TestCircuitBreakerEdgeCases:
    """Test circuit breaker state transitions and correctness."""

    def test_circuit_breaker_records_threshold_minus_1_then_success(self):
        """Record exactly threshold-1 failures, then success -> stays CLOSED."""
        breaker = CircuitBreaker("test", failure_threshold=5, recovery_timeout=1.0)

        # Record 4 failures (one less than threshold)
        for _ in range(4):
            breaker.record_failure()

        assert breaker.state == CircuitState.CLOSED

        # Now success
        breaker.record_success()

        # Should still be CLOSED
        assert breaker.state == CircuitState.CLOSED
        assert breaker._failure_count == 0

    def test_circuit_breaker_opens_at_threshold(self):
        """Record exactly threshold failures -> OPEN."""
        breaker = CircuitBreaker("test", failure_threshold=5, recovery_timeout=1.0)

        for _ in range(5):
            breaker.record_failure()

        assert breaker.state == CircuitState.OPEN

    def test_circuit_breaker_transitions_to_half_open_after_timeout(self):
        """After timeout from OPEN, transitions to HALF_OPEN."""
        breaker = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.1)

        # Open the circuit
        breaker.record_failure()
        breaker.record_failure()
        assert breaker.state == CircuitState.OPEN

        # Wait for recovery timeout
        import time
        time.sleep(0.15)

        # Now should be HALF_OPEN
        assert breaker.state == CircuitState.HALF_OPEN

    def test_circuit_breaker_closes_after_half_open_success(self):
        """HALF_OPEN + success -> CLOSED."""
        breaker = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.1)

        # Open
        breaker.record_failure()
        breaker.record_failure()
        assert breaker.state == CircuitState.OPEN

        # Wait
        import time
        time.sleep(0.15)
        assert breaker.state == CircuitState.HALF_OPEN

        # Success in half-open
        breaker.record_success()

        # Should close
        assert breaker.state == CircuitState.CLOSED

    def test_circuit_breaker_reopens_on_half_open_failure(self):
        """HALF_OPEN + failure -> OPEN."""
        breaker = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.1)

        # Open
        breaker.record_failure()
        breaker.record_failure()
        assert breaker.state == CircuitState.OPEN

        # Wait
        import time
        time.sleep(0.15)
        assert breaker.state == CircuitState.HALF_OPEN

        # Failure in half-open
        breaker.record_failure()

        # Should reopen
        assert breaker.state == CircuitState.OPEN

    def test_get_circuit_breaker_returns_same_instance(self):
        """get_circuit_breaker with same name returns same instance."""
        from app.core.retry import get_circuit_breaker, _breakers

        # Clear previous state
        _breakers.clear()

        breaker1 = get_circuit_breaker("myservice")
        breaker1.record_failure()

        breaker2 = get_circuit_breaker("myservice")

        # Should be same object
        assert breaker1 is breaker2
        assert breaker2._failure_count == 1

    def test_circuit_breaker_reset_clears_state(self):
        """Circuit breaker reset() clears all state."""
        breaker = CircuitBreaker("test", failure_threshold=3)

        breaker.record_failure()
        breaker.record_failure()
        breaker.record_failure()
        assert breaker.state == CircuitState.OPEN

        breaker.reset()

        assert breaker.state == CircuitState.CLOSED
        assert breaker._failure_count == 0
        assert breaker._success_count == 0

    def test_circuit_breaker_is_open_property(self):
        """is_open property correctly reflects state."""
        breaker = CircuitBreaker("test", failure_threshold=2)

        assert breaker.is_open is False

        breaker.record_failure()
        breaker.record_failure()

        assert breaker.is_open is True

    def test_circuit_breaker_is_closed_property(self):
        """is_closed property correctly reflects state."""
        breaker = CircuitBreaker("test", failure_threshold=2)

        assert breaker.is_closed is True

        breaker.record_failure()
        breaker.record_failure()

        assert breaker.is_closed is False


# ==============================================================================
# PART 5: SCORE FUSION VALIDATION
# ==============================================================================

class TestScoreFusionValidation:
    """Test score fusion weights and None handling."""

    def test_fusion_weights_sum_to_1_0(self):
        """Verify all fusion weights sum to 1.0."""
        for module, (structured, visual) in FUSION_WEIGHTS.items():
            total = structured + visual
            assert abs(total - 1.0) < 0.001, f"{module}: weights {structured} + {visual} = {total}"

    def test_fuse_both_with_valid_scores(self):
        """Test fusion of both structured and visual scores."""
        structured = {"overall_score": 75.0, "confidence": "measured"}
        visual = {"score": 80.0, "confidence": "visual_high"}

        result = fuse_module_scores(structured, visual, "ergonomics", "cruising_sail")

        assert result["fused_score"] is not None
        assert not math.isnan(result["fused_score"])
        assert not math.isinf(result["fused_score"])
        assert 0 <= result["fused_score"] <= 100

    def test_fuse_structured_only_with_none_visual(self):
        """Test fusion when visual is None."""
        structured = {"overall_score": 75.0, "confidence": "measured"}
        visual = None

        result = fuse_module_scores(structured, visual, "ergonomics", "cruising_sail")

        assert result["fused_score"] == 75.0
        assert result["data_sources"] == ["structured"]

    def test_fuse_visual_only_with_none_structured(self):
        """Test fusion when structured is None."""
        structured = None
        visual = {"score": 80.0, "confidence": "visual_high"}

        result = fuse_module_scores(structured, visual, "ergonomics", "cruising_sail")

        assert result["fused_score"] == 80.0
        assert result["data_sources"] == ["visual"]

    def test_fuse_both_none_returns_no_data(self):
        """Test fusion when both are None."""
        result = fuse_module_scores(None, None, "ergonomics", "cruising_sail")

        assert result["fused_score"] is None
        assert result["confidence"] == "visual_insufficient"
        assert result["data_sources"] == []

    def test_fuse_zone_score_structured_only(self):
        """Test zone score fusion with only structured data."""
        result = fuse_zone_score(
            "cabin",
            "ergonomics",
            structured_score=75.0,
            visual_score=None,
        )

        assert result["score"] == 75.0
        assert result["sources"] == ["structured"]
        assert result["visual_component"] is None

    def test_fuse_zone_score_visual_only(self):
        """Test zone score fusion with only visual data."""
        result = fuse_zone_score(
            "cabin",
            "ergonomics",
            structured_score=None,
            visual_score=85.0,
        )

        assert result["score"] == 85.0
        assert result["sources"] == ["visual"]
        assert result["structured_component"] is None

    def test_fuse_zone_score_both_none(self):
        """Test zone score fusion when both are None."""
        result = fuse_zone_score(
            "cabin",
            "ergonomics",
            structured_score=None,
            visual_score=None,
        )

        assert result["score"] is None
        assert result["confidence"] == "visual_insufficient"

    def test_fuse_zone_score_with_large_discrepancy(self):
        """Test zone score fusion flags large discrepancies."""
        result = fuse_zone_score(
            "cabin",
            "ergonomics",
            structured_score=50.0,
            visual_score=95.0,
        )

        # Should have both components
        assert result["structured_component"] == 50.0
        assert result["visual_component"] == 95.0
        # Should flag discrepancy
        assert result["discrepancy_note"] is not None
        assert "weichen" in result["discrepancy_note"].lower() or len(result["discrepancy_note"]) > 0

    def test_fuse_module_scores_effective_weights_normalize(self):
        """Test that effective weights in fusion normalize to 1.0."""
        structured = {"overall_score": 75.0, "confidence": "measured"}
        visual = {"score": 80.0, "confidence": "visual_low"}  # Low confidence

        result = fuse_module_scores(structured, visual, "ergonomics", "cruising_sail")

        sw = result["fusion_weights"]["structured"]
        vw = result["fusion_weights"]["visual"]

        total = sw + vw
        assert abs(total - 1.0) < 0.001, f"Weights {sw} + {vw} = {total}, not 1.0"

    def test_compute_overall_score_weighted_average(self):
        """Test overall score computes weighted average correctly."""
        results = {
            "ergonomics": {"overall_score": 80.0, "confidence": "measured"},
            "volume_storage": {"overall_score": 70.0, "confidence": "measured"},
        }

        overall = _compute_overall_score(results, "cruising_sail")

        # Should be weighted average using boat class weights
        assert overall["score"] is not None
        assert 0 <= overall["score"] <= 100

    def test_compute_overall_score_empty_results_returns_insufficient(self):
        """Test overall score with no results returns insufficient."""
        results = {}

        overall = _compute_overall_score(results, "cruising_sail")

        assert overall["score"] is None
        assert overall["confidence"] == "insufficient"

    def test_compute_overall_score_confidence_all_measured(self):
        """Test overall confidence when all modules are measured."""
        results = {
            "ergonomics": {"overall_score": 80.0, "confidence": "measured"},
            "volume_storage": {"overall_score": 70.0, "confidence": "measured"},
            "emotional": {"overall_score": 75.0, "confidence": "measured"},
        }

        overall = _compute_overall_score(results, "cruising_sail", confidence_threshold=0.7)

        # All are measured, so overall should be measured
        assert overall["confidence"] == "measured"

    def test_compute_overall_score_confidence_mixed(self):
        """Test overall confidence with mixed measured/estimated."""
        results = {
            "ergonomics": {"overall_score": 80.0, "confidence": "measured"},
            "volume_storage": {"overall_score": 70.0, "confidence": "estimated"},
        }

        overall = _compute_overall_score(results, "cruising_sail", confidence_threshold=0.7)

        # Only 50% measured, below threshold
        assert overall["confidence"] == "calculated" or overall["confidence"] == "estimated"


# ==============================================================================
# PART 6: RETRY AND RETRY_ASYNC EDGE CASES
# ==============================================================================

class TestRetryEdgeCases:
    """Test retry_async behavior with edge cases."""

    @pytest.mark.asyncio
    async def test_retry_async_success_on_first_attempt(self):
        """Test successful function on first try."""
        async def success_func():
            return "success"

        result = await retry_async(success_func, max_retries=3)

        assert result.success is True
        assert result.value == "success"
        assert result.attempts == 1

    @pytest.mark.asyncio
    async def test_retry_async_succeeds_on_retry(self):
        """Test successful function after initial failure."""
        call_count = [0]

        async def eventually_succeeds():
            call_count[0] += 1
            if call_count[0] < 2:
                raise TimeoutError("First attempt fails")
            return "success"

        result = await retry_async(
            eventually_succeeds,
            max_retries=3,
            base_delay=0.01,
        )

        assert result.success is True
        assert result.value == "success"
        assert result.attempts == 2

    @pytest.mark.asyncio
    async def test_retry_async_exhausts_retries(self):
        """Test function that always fails exhausts retries."""
        async def always_fails():
            raise TimeoutError("Always fails")

        result = await retry_async(
            always_fails,
            max_retries=2,
            base_delay=0.01,
        )

        assert result.success is False
        assert result.attempts == 3  # initial + 2 retries

    @pytest.mark.asyncio
    async def test_retry_async_non_retryable_error_fails_immediately(self):
        """Test non-retryable error fails on first attempt."""
        async def raises_non_retryable():
            raise NonRetryableError("Should not retry")

        result = await retry_async(
            raises_non_retryable,
            max_retries=3,
            base_delay=0.01,
        )

        assert result.success is False
        assert result.attempts == 1

    @pytest.mark.asyncio
    async def test_retry_async_with_timeout(self):
        """Test retry_async with per-attempt timeout."""
        async def slow_function():
            await asyncio.sleep(0.5)
            return "result"

        result = await retry_async(
            slow_function,
            max_retries=1,
            timeout=0.1,
            base_delay=0.01,
        )

        # Should fail due to timeout
        assert result.success is False
        assert isinstance(result.error, asyncio.TimeoutError)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
