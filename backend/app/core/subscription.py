"""Subscription tier gating for AYDI.

Defines which features/modules are available per tier (Free, Pro, Enterprise).
Gating is enforced server-side — never rely on frontend hiding alone.

Tiers:
- Free: Quick analysis (Level 1), limited knowledge base, basic components
- Pro: Full analysis (Level 2), full knowledge base, community intelligence,
       component database, visual analysis, multi-language support
- Enterprise (Shipyard): Everything in Pro + fleet management, API access,
       multi-tenancy, collaboration, custom reports, priority support
"""

from __future__ import annotations

import logging
from enum import Enum
from typing import Any

from fastapi import HTTPException, status

from app.core.i18n import t

logger = logging.getLogger(__name__)


class SubscriptionTier(str, Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


# ---------------------------------------------------------------------------
# Feature definitions
# ---------------------------------------------------------------------------

class Feature(str, Enum):
    """All gated features in AYDI."""
    # Analysis
    QUICK_ANALYSIS = "quick_analysis"
    FULL_ANALYSIS = "full_analysis"
    VISUAL_ANALYSIS = "visual_analysis"
    COMMUNITY_INTELLIGENCE = "community_intelligence"

    # Analysis modules (Level 2)
    MODULE_ERGONOMICS = "module_ergonomics"
    MODULE_VOLUME = "module_volume"
    MODULE_EMOTIONAL = "module_emotional"
    MODULE_COMPLIANCE = "module_compliance"
    MODULE_PRODUCTION = "module_production"
    MODULE_MATERIALS = "module_materials"
    MODULE_STRUCTURAL = "module_structural"
    MODULE_COST = "module_cost"
    MODULE_SERVICE_PATTERNS = "module_service_patterns"
    MODULE_BRAND_DNA = "module_brand_dna"
    MODULE_MARKET = "module_market"
    MODULE_COMMUNITY = "module_community"

    # Data
    KNOWLEDGE_BASE_FULL = "knowledge_base_full"
    COMPONENT_DATABASE = "component_database"
    MANUFACTURER_DATA = "manufacturer_data"
    FORUM_INTELLIGENCE = "forum_intelligence"

    # Import/Export
    CAD_IMPORT = "cad_import"
    REPORT_EXPORT = "report_export"
    REPORT_EXPORT_PDF = "report_export_pdf"

    # Collaboration
    COLLABORATION = "collaboration"
    VERSION_HISTORY = "version_history"

    # Enterprise
    FLEET_MANAGEMENT = "fleet_management"
    API_ACCESS = "api_access"
    CUSTOM_REPORTS = "custom_reports"
    MULTI_TENANCY = "multi_tenancy"
    PRIORITY_SUPPORT = "priority_support"
    BENCHMARK_DATABASE = "benchmark_database"

    # Settings
    MULTI_LANGUAGE = "multi_language"
    IMPERIAL_UNITS = "imperial_units"


# ---------------------------------------------------------------------------
# Tier -> Feature mapping
# ---------------------------------------------------------------------------

# Each tier includes all features from lower tiers.
_TIER_FEATURES: dict[SubscriptionTier, set[Feature]] = {
    SubscriptionTier.FREE: {
        Feature.QUICK_ANALYSIS,
        # Level 1 modules only (estimated results)
        Feature.MODULE_ERGONOMICS,
        Feature.MODULE_VOLUME,
        Feature.MODULE_EMOTIONAL,
        Feature.MODULE_MARKET,
    },
    SubscriptionTier.PRO: {
        # All Free features +
        Feature.FULL_ANALYSIS,
        Feature.VISUAL_ANALYSIS,
        Feature.COMMUNITY_INTELLIGENCE,
        # All analysis modules
        Feature.MODULE_ERGONOMICS,
        Feature.MODULE_VOLUME,
        Feature.MODULE_EMOTIONAL,
        Feature.MODULE_COMPLIANCE,
        Feature.MODULE_PRODUCTION,
        Feature.MODULE_MATERIALS,
        Feature.MODULE_STRUCTURAL,
        Feature.MODULE_COST,
        Feature.MODULE_SERVICE_PATTERNS,
        Feature.MODULE_BRAND_DNA,
        Feature.MODULE_MARKET,
        Feature.MODULE_COMMUNITY,
        # Data
        Feature.KNOWLEDGE_BASE_FULL,
        Feature.COMPONENT_DATABASE,
        Feature.MANUFACTURER_DATA,
        Feature.FORUM_INTELLIGENCE,
        # Import/Export
        Feature.CAD_IMPORT,
        Feature.REPORT_EXPORT,
        Feature.REPORT_EXPORT_PDF,
        # Collaboration
        Feature.COLLABORATION,
        Feature.VERSION_HISTORY,
        # Settings
        Feature.MULTI_LANGUAGE,
        Feature.IMPERIAL_UNITS,
        Feature.BENCHMARK_DATABASE,
    },
    SubscriptionTier.ENTERPRISE: {
        # All Pro features +
        Feature.FLEET_MANAGEMENT,
        Feature.API_ACCESS,
        Feature.CUSTOM_REPORTS,
        Feature.MULTI_TENANCY,
        Feature.PRIORITY_SUPPORT,
    },
}

# Build inclusive sets (each tier includes lower tiers)
TIER_ALLOWED_FEATURES: dict[SubscriptionTier, set[Feature]] = {}
_cumulative: set[Feature] = set()
for _tier in [SubscriptionTier.FREE, SubscriptionTier.PRO, SubscriptionTier.ENTERPRISE]:
    _cumulative = _cumulative | _TIER_FEATURES[_tier]
    TIER_ALLOWED_FEATURES[_tier] = _cumulative.copy()


# ---------------------------------------------------------------------------
# Module -> Feature mapping (for orchestrator gating)
# ---------------------------------------------------------------------------

MODULE_FEATURE_MAP: dict[str, Feature] = {
    "ergonomics": Feature.MODULE_ERGONOMICS,
    "volume_storage": Feature.MODULE_VOLUME,
    "emotional": Feature.MODULE_EMOTIONAL,
    "compliance": Feature.MODULE_COMPLIANCE,
    "production": Feature.MODULE_PRODUCTION,
    "materials": Feature.MODULE_MATERIALS,
    "structural": Feature.MODULE_STRUCTURAL,
    "cost": Feature.MODULE_COST,
    "service_patterns": Feature.MODULE_SERVICE_PATTERNS,
    "brand_dna": Feature.MODULE_BRAND_DNA,
    "market": Feature.MODULE_MARKET,
    "community": Feature.MODULE_COMMUNITY,
}


# ---------------------------------------------------------------------------
# Tier checking functions
# ---------------------------------------------------------------------------

def has_feature(tier: str | SubscriptionTier, feature: Feature) -> bool:
    """Check if a subscription tier has access to a feature.

    Args:
        tier: User's subscription tier (string or enum).
        feature: The feature to check.

    Returns:
        True if the tier allows the feature.
    """
    if isinstance(tier, str):
        try:
            tier = SubscriptionTier(tier.lower())
        except ValueError:
            logger.warning("Unknown tier %r, treating as free", tier)
            tier = SubscriptionTier.FREE

    return feature in TIER_ALLOWED_FEATURES.get(tier, TIER_ALLOWED_FEATURES[SubscriptionTier.FREE])


def get_allowed_modules(tier: str | SubscriptionTier) -> list[str]:
    """Get list of analysis module names allowed for a tier.

    Returns:
        List of module name strings (e.g., ["ergonomics", "volume_storage"]).
    """
    return [
        module_name
        for module_name, feature in MODULE_FEATURE_MAP.items()
        if has_feature(tier, feature)
    ]


def require_feature(tier: str | SubscriptionTier, feature: Feature) -> None:
    """Raise HTTPException if tier doesn't allow the feature.

    Used in route handlers for server-side gating.
    """
    if not has_feature(tier, feature):
        required_tier = _minimum_tier_for_feature(feature)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=t(
                "auth.tier_upgrade_required",
                tier=t(f"tier.{required_tier.value}"),
            ),
        )


def require_module(tier: str | SubscriptionTier, module_name: str) -> None:
    """Raise HTTPException if tier doesn't allow the analysis module."""
    feature = MODULE_FEATURE_MAP.get(module_name)
    if feature is None:
        logger.warning("Unknown module %r, allowing by default", module_name)
        return
    require_feature(tier, feature)


def _minimum_tier_for_feature(feature: Feature) -> SubscriptionTier:
    """Find the lowest tier that includes a feature."""
    for tier in [SubscriptionTier.FREE, SubscriptionTier.PRO, SubscriptionTier.ENTERPRISE]:
        if feature in TIER_ALLOWED_FEATURES[tier]:
            return tier
    return SubscriptionTier.ENTERPRISE


# ---------------------------------------------------------------------------
# Downgrade handling
# ---------------------------------------------------------------------------

def get_downgrade_impact(
    current_tier: SubscriptionTier,
    new_tier: SubscriptionTier,
) -> dict[str, Any]:
    """Calculate what a user loses when downgrading.

    Returns dict with:
    - lost_features: list of Feature names no longer available
    - affected_modules: list of module names that will be locked
    - data_retention: whether existing analysis results are retained (always True)
    """
    current_features = TIER_ALLOWED_FEATURES[current_tier]
    new_features = TIER_ALLOWED_FEATURES[new_tier]
    lost = current_features - new_features

    return {
        "lost_features": [f.value for f in lost],
        "affected_modules": [
            name for name, feat in MODULE_FEATURE_MAP.items() if feat in lost
        ],
        "data_retention": True,  # Existing data is always retained, just not accessible
    }
