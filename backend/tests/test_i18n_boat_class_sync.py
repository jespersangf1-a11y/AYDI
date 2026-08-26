"""Regressionstests fuer i18n-Befunde I18N-7 und I18N-3.

I18N-7: format_number haengte bei decimals=0 einen leeren Dezimaltrenner an.
I18N-3: BoatClass-Enum und boat_class-Katalog waren auseinandergedriftet —
        fuenf Klassen lieferten den rohen englischen Schluessel als Anzeigetext.
"""

import pytest

from app.core.i18n import (
    LEGACY_BOAT_CLASS_KEYS,
    Locale,
    NumberFormatter,
    get_all_keys,
    has_key,
    t,
)
from app.schemas.schemas import BoatClass


class TestFormatNumberZeroDecimals:
    """I18N-7 — bei decimals=0 darf kein Dezimaltrenner uebrig bleiben."""

    @pytest.mark.parametrize("locale", list(Locale))
    @pytest.mark.parametrize("value", [1234.56, 0.6, -9876.4, 12.5, 999999.99])
    def test_no_trailing_decimal_separator(self, value, locale):
        out = NumberFormatter.format_number(value, decimals=0, locale=locale)
        sep = NumberFormatter.FORMATS[locale]["decimal_sep"]
        assert not out.endswith(sep), f"Dezimaltrenner am Ende: {out!r} ({locale.value})"
        assert sep not in out, f"Unerwarteter Dezimaltrenner in {out!r} ({locale.value})"

    def test_rounds_to_integer(self):
        assert NumberFormatter.format_number(1234.56, decimals=0, locale=Locale.DE) == "1.235"
        assert NumberFormatter.format_number(1234.56, decimals=0, locale=Locale.EN) == "1,235"
        assert NumberFormatter.format_number(-9876.4, decimals=0, locale=Locale.DE) == "-9.876"
        assert NumberFormatter.format_number(0.6, decimals=0, locale=Locale.DE) == "1"

    def test_int_and_float_paths_agree(self):
        """Ganzzahliger und gebrochener Eingabewert muessen gleich formatiert werden."""
        assert NumberFormatter.format_number(1234, decimals=0, locale=Locale.DE) == \
            NumberFormatter.format_number(1234.4, decimals=0, locale=Locale.DE)

    def test_decimals_still_work(self):
        assert NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.DE) == "1.234,56"
        assert NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.EN) == "1,234.56"

    def test_currency_and_percentage_without_decimals(self):
        assert NumberFormatter.format_currency(1234.56, decimals=0, locale=Locale.DE) == "1.235 \u20ac"
        assert NumberFormatter.format_percentage(0.4567, decimals=0, locale=Locale.DE) == "46 %"


class TestBoatClassCatalogSync:
    """I18N-3 — Enum und Katalog muessen dauerhaft deckungsgleich bleiben."""

    def test_every_boat_class_has_a_key(self):
        missing = [bc.value for bc in BoatClass if not has_key(f"boat_class.{bc.value}")]
        assert not missing, f"Bootsklassen ohne Katalogeintrag: {missing}"

    @pytest.mark.parametrize("boat_class", [bc.value for bc in BoatClass])
    @pytest.mark.parametrize("locale", list(Locale))
    def test_every_locale_has_a_real_label(self, boat_class, locale):
        key = f"boat_class.{boat_class}"
        label = t(key, locale=locale)
        assert label != key, f"Kein Anzeigetext fuer {key} in {locale.value}"
        assert label.strip(), f"Leerer Anzeigetext fuer {key} in {locale.value}"
        assert boat_class not in label, (
            f"Roher Enum-Schluessel als Anzeigetext: {key} -> {label!r} ({locale.value})"
        )

    def test_no_unknown_boat_class_keys(self):
        """Katalogschluessel ohne Enum-Entsprechung sind Drift (Ausnahme: Alt-Schluessel)."""
        catalog = {k for k in get_all_keys() if k.startswith("boat_class.")}
        known = {f"boat_class.{bc.value}" for bc in BoatClass} | LEGACY_BOAT_CLASS_KEYS
        assert not (catalog - known), f"Unbekannte boat_class-Schluessel: {sorted(catalog - known)}"

    def test_legacy_keys_are_not_enum_values(self):
        """Alt-Schluessel duerfen keine aktuellen Enum-Werte verdecken."""
        enum_keys = {f"boat_class.{bc.value}" for bc in BoatClass}
        assert not (LEGACY_BOAT_CLASS_KEYS & enum_keys)

    def test_labels_are_distinct_per_boat_class_in_german(self):
        """DE ist kanonisch: jede Klasse braucht eine eigene Bezeichnung."""
        labels = [t(f"boat_class.{bc.value}", locale=Locale.DE) for bc in BoatClass]
        assert len(set(labels)) == len(labels), f"Doppelte DE-Bezeichnungen: {labels}"
