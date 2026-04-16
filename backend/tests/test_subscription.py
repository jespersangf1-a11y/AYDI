"""Tests for subscription tier gating."""

import pytest
from fastapi import HTTPException

from app.core.subscription import (
    Feature,
    SubscriptionTier,
    get_allowed_modules,
    get_downgrade_impact,
    has_feature,
    require_feature,
    require_module,
)


class TestHasFeature:
    # --- Free tier ---
    def test_free_has_quick_analysis(self):
        assert has_feature("free", Feature.QUICK_ANALYSIS) is True

    def test_free_has_basic_modules(self):
        assert has_feature("free", Feature.MODULE_ERGONOMICS) is True
        assert has_feature("free", Feature.MODULE_VOLUME) is True
        assert has_feature("free", Feature.MODULE_EMOTIONAL) is True
        assert has_feature("free", Feature.MODULE_MARKET) is True

    def test_free_lacks_pro_modules(self):
        assert has_feature("free", Feature.MODULE_STRUCTURAL) is False
        assert has_feature("free", Feature.MODULE_COMPLIANCE) is False
        assert has_feature("free", Feature.MODULE_MATERIALS) is False
        assert has_feature("free", Feature.MODULE_COST) is False

    def test_free_lacks_full_analysis(self):
        assert has_feature("free", Feature.FULL_ANALYSIS) is False

    def test_free_lacks_visual_analysis(self):
        assert has_feature("free", Feature.VISUAL_ANALYSIS) is False

    def test_free_lacks_cad_import(self):
        assert has_feature("free", Feature.CAD_IMPORT) is False

    # --- Pro tier ---
    def test_pro_has_all_modules(self):
        for feature in [
            Feature.MODULE_ERGONOMICS, Feature.MODULE_VOLUME,
            Feature.MODULE_EMOTIONAL, Feature.MODULE_COMPLIANCE,
            Feature.MODULE_PRODUCTION, Feature.MODULE_MATERIALS,
            Feature.MODULE_STRUCTURAL, Feature.MODULE_COST,
            Feature.MODULE_SERVICE_PATTERNS, Feature.MODULE_BRAND_DNA,
            Feature.MODULE_MARKET, Feature.MODULE_COMMUNITY,
        ]:
            assert has_feature("pro", feature) is True, f"Pro should have {feature}"

    def test_pro_has_visual_analysis(self):
        assert has_feature("pro", Feature.VISUAL_ANALYSIS) is True

    def test_pro_has_cad_import(self):
        assert has_feature("pro", Feature.CAD_IMPORT) is True

    def test_pro_has_knowledge_base(self):
        assert has_feature("pro", Feature.KNOWLEDGE_BASE_FULL) is True

    def test_pro_has_multi_language(self):
        assert has_feature("pro", Feature.MULTI_LANGUAGE) is True

    def test_pro_lacks_enterprise_features(self):
        assert has_feature("pro", Feature.FLEET_MANAGEMENT) is False
        assert has_feature("pro", Feature.API_ACCESS) is False
        assert has_feature("pro", Feature.MULTI_TENANCY) is False

    # --- Enterprise tier ---
    def test_enterprise_has_everything(self):
        for feature in Feature:
            assert has_feature("enterprise", feature) is True, f"Enterprise should have {feature}"

    # --- Unknown tier ---
    def test_unknown_tier_treated_as_free(self):
        assert has_feature("unknown_tier", Feature.QUICK_ANALYSIS) is True
        assert has_feature("unknown_tier", Feature.FULL_ANALYSIS) is False


class TestGetAllowedModules:
    def test_free_modules(self):
        modules = get_allowed_modules("free")
        assert "ergonomics" in modules
        assert "volume_storage" in modules
        assert "emotional" in modules
        assert "market" in modules
        assert "structural" not in modules
        assert "compliance" not in modules

    def test_pro_has_all_modules(self):
        modules = get_allowed_modules("pro")
        assert len(modules) == 12  # All 12 analysis modules

    def test_enterprise_has_all_modules(self):
        modules = get_allowed_modules("enterprise")
        assert len(modules) == 12


class TestRequireFeature:
    def test_allowed_does_not_raise(self):
        require_feature("pro", Feature.FULL_ANALYSIS)  # Should not raise

    def test_disallowed_raises_403(self):
        with pytest.raises(HTTPException) as exc_info:
            require_feature("free", Feature.FULL_ANALYSIS)
        assert exc_info.value.status_code == 403


class TestRequireModule:
    def test_allowed_module(self):
        require_module("pro", "structural")  # Should not raise

    def test_disallowed_module(self):
        with pytest.raises(HTTPException):
            require_module("free", "structural")

    def test_unknown_module_allowed(self):
        require_module("free", "nonexistent_module")  # Unknown modules allowed by default


class TestDowngradeImpact:
    def test_pro_to_free(self):
        impact = get_downgrade_impact(SubscriptionTier.PRO, SubscriptionTier.FREE)
        assert len(impact["lost_features"]) > 0
        assert "structural" in impact["affected_modules"]
        assert "compliance" in impact["affected_modules"]
        assert impact["data_retention"] is True

    def test_enterprise_to_pro(self):
        impact = get_downgrade_impact(SubscriptionTier.ENTERPRISE, SubscriptionTier.PRO)
        assert "fleet_management" in impact["lost_features"]
        assert "api_access" in impact["lost_features"]
        # Module access should not be affected (Pro has all modules)
        assert impact["affected_modules"] == []

    def test_same_tier_no_impact(self):
        impact = get_downgrade_impact(SubscriptionTier.PRO, SubscriptionTier.PRO)
        assert impact["lost_features"] == []
        assert impact["affected_modules"] == []
