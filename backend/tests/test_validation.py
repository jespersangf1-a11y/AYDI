"""Tests for the input validation framework."""

import math
import pytest
from app.core.errors import DataValidationError
from app.core.validation import (
    VALID_BOAT_CLASSES,
    validate_boat_class,
    validate_confidence,
    validate_enum,
    validate_in_range,
    validate_install_year,
    validate_non_empty_string,
    validate_passages,
    validate_positive,
    validate_score,
    validate_severity,
    validate_year,
    validate_zones,
)


class TestValidatePositive:
    def test_valid_positive(self):
        assert validate_positive(5.0, "test") == 5.0

    def test_valid_zero_when_allowed(self):
        assert validate_positive(0, "test", allow_zero=True) == 0.0

    def test_zero_rejected_by_default(self):
        with pytest.raises(DataValidationError):
            validate_positive(0, "test")

    def test_negative_rejected(self):
        with pytest.raises(DataValidationError):
            validate_positive(-1.0, "test")

    def test_none_when_allowed(self):
        assert validate_positive(None, "test", allow_none=True) is None

    def test_none_rejected_by_default(self):
        with pytest.raises(DataValidationError):
            validate_positive(None, "test")

    def test_nan_rejected(self):
        with pytest.raises(DataValidationError):
            validate_positive(float("nan"), "test")

    def test_inf_rejected(self):
        with pytest.raises(DataValidationError):
            validate_positive(float("inf"), "test")

    def test_max_value_exceeded(self):
        with pytest.raises(DataValidationError):
            validate_positive(500.0, "test", max_value=300.0)

    def test_max_value_ok(self):
        assert validate_positive(100.0, "test", max_value=300.0) == 100.0

    def test_string_rejected(self):
        with pytest.raises(DataValidationError):
            validate_positive("not_a_number", "test")


class TestValidateInRange:
    def test_within_range(self):
        assert validate_in_range(5.0, "test", 0.0, 10.0) == 5.0

    def test_at_min(self):
        assert validate_in_range(0.0, "test", 0.0, 10.0) == 0.0

    def test_at_max(self):
        assert validate_in_range(10.0, "test", 0.0, 10.0) == 10.0

    def test_below_min(self):
        with pytest.raises(DataValidationError):
            validate_in_range(-1.0, "test", 0.0, 10.0)

    def test_above_max(self):
        with pytest.raises(DataValidationError):
            validate_in_range(11.0, "test", 0.0, 10.0)

    def test_nan(self):
        with pytest.raises(DataValidationError):
            validate_in_range(float("nan"), "test", 0.0, 10.0)


class TestValidateNonEmptyString:
    def test_valid(self):
        assert validate_non_empty_string("hello", "test") == "hello"

    def test_strips_whitespace(self):
        assert validate_non_empty_string("  hello  ", "test") == "hello"

    def test_empty_rejected(self):
        with pytest.raises(DataValidationError):
            validate_non_empty_string("", "test")

    def test_whitespace_only_rejected(self):
        with pytest.raises(DataValidationError):
            validate_non_empty_string("   ", "test")

    def test_none_when_allowed(self):
        assert validate_non_empty_string(None, "test", allow_none=True) is None

    def test_too_long(self):
        with pytest.raises(DataValidationError):
            validate_non_empty_string("x" * 501, "test")


class TestValidateBoatClass:
    def test_all_known_classes(self):
        for cls in VALID_BOAT_CLASSES:
            assert validate_boat_class(cls) == cls

    def test_case_insensitive(self):
        assert validate_boat_class("CRUISING_SAIL") == "cruising_sail"

    def test_unknown_rejected(self):
        with pytest.raises(DataValidationError):
            validate_boat_class("unknown_class")

    def test_none_rejected(self):
        with pytest.raises(DataValidationError):
            validate_boat_class(None)


class TestValidateZones:
    def test_valid_zones(self):
        zones = [
            {"name": "salon", "zone_type": "saloon", "polygon": [[0, 0], [1, 0], [1, 1], [0, 1]]},
        ]
        result = validate_zones(zones)
        assert len(result) == 1

    def test_none_returns_empty(self):
        assert validate_zones(None) == []

    def test_non_list_raises(self):
        with pytest.raises(DataValidationError):
            validate_zones("not a list")

    def test_non_dict_zone_raises(self):
        with pytest.raises(DataValidationError):
            validate_zones(["not a dict"])

    def test_empty_list_ok(self):
        assert validate_zones([]) == []

    def test_zone_with_unknown_type_passes_with_warning(self):
        """Unknown zone types should pass but log a warning."""
        zones = [{"name": "test", "zone_type": "exotic_unknown"}]
        result = validate_zones(zones)
        assert len(result) == 1


class TestValidatePassages:
    def test_valid_passages(self):
        passages = [{"from": "a", "to": "b", "width_mm": 800}]
        result = validate_passages(passages)
        assert len(result) == 1

    def test_none_returns_empty(self):
        assert validate_passages(None) == []

    def test_non_dict_raises(self):
        with pytest.raises(DataValidationError):
            validate_passages([42])


class TestValidateYear:
    def test_valid_year(self):
        assert validate_year(2020, "build_year") == 2020

    def test_too_old(self):
        with pytest.raises(DataValidationError):
            validate_year(1700, "build_year")

    def test_too_new(self):
        with pytest.raises(DataValidationError):
            validate_year(2050, "build_year")

    def test_none_when_allowed(self):
        assert validate_year(None, "build_year", allow_none=True) is None


class TestValidateInstallYear:
    def test_valid(self):
        assert validate_install_year(2020) == 2020

    def test_future_rejected(self):
        with pytest.raises(DataValidationError):
            validate_install_year(2030, current_year=2026)

    def test_current_year_ok(self):
        assert validate_install_year(2026, current_year=2026) == 2026

    def test_none_ok(self):
        assert validate_install_year(None) is None


class TestValidateScore:
    def test_valid(self):
        assert validate_score(75.0) == 75.0

    def test_none_returns_none(self):
        assert validate_score(None) is None

    def test_clamped_above_100(self):
        assert validate_score(150.0) == 100.0

    def test_clamped_below_0(self):
        assert validate_score(-10.0) == 0.0

    def test_nan_returns_none(self):
        assert validate_score(float("nan")) is None

    def test_string_returns_none(self):
        assert validate_score("not_a_score") is None


class TestValidateConfidence:
    def test_known_levels(self):
        assert validate_confidence("measured") == "measured"
        assert validate_confidence("visual_high") == "visual_high"
        assert validate_confidence("estimated") == "estimated"

    def test_unknown_defaults_to_estimated(self):
        assert validate_confidence("unknown") == "estimated"

    def test_none_defaults_to_estimated(self):
        assert validate_confidence(None) == "estimated"

    def test_case_insensitive(self):
        assert validate_confidence("MEASURED") == "measured"


class TestValidateSeverity:
    def test_known_levels(self):
        assert validate_severity("critical") == "critical"
        assert validate_severity("high") == "high"

    def test_unknown_defaults_to_info(self):
        assert validate_severity("unknown") == "info"

    def test_none_defaults_to_info(self):
        assert validate_severity(None) == "info"
