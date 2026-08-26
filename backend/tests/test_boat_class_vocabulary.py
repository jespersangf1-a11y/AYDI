"""Das Bootsklassen-Vokabular darf nicht vom BoatClass-Enum abdriften.

Gemessener Zustand vorher: ``VALID_BOAT_CLASSES`` war eine handgepflegte Kopie
und gegenueber dem Enum verrutscht.

* **Abgelehnt** wurden fuenf echte Klassen: ``racing_sail``, ``daysailer``,
  ``catamaran_motor``, ``sport_cruiser``, ``explorer`` — obwohl das Frontend sie
  zur Auswahl anbietet (``frontend/src/types/index.ts``) und alle Analysemodule
  ``BOAT_CLASS_DEFAULTS`` fuer sie fuehren.
* **Weiter gueltig** waren fuenf zurueckgezogene Namen.

Besonders getroffen hat das die Level-1-Schnellanalyse: Sie nimmt ``boat_class``
als freien String entgegen (``schemas/quick_analysis.py``), nicht als Enum — die
Pruefung passiert also erst hier. Wer im Frontend "Daysailer" waehlte, lief in
eine Validierungswarnung.

Die Liste wird jetzt aus dem Enum abgeleitet; diese Tests halten das fest.
"""

import pytest

from app.core.validation import (
    BOAT_CLASS_ALIASES,
    VALID_BOAT_CLASSES,
    DataValidationError,
    normalize_boat_class,
    validate_boat_class,
)
from app.schemas.schemas import BoatClass


class TestVokabularDeckung:
    def test_valid_set_matches_the_enum_exactly(self):
        assert VALID_BOAT_CLASSES == {bc.value for bc in BoatClass}

    def test_there_are_thirteen_boat_classes(self):
        """CLAUDE.md: 13 Klassen — nicht 4, wie in archivierten Design-Dokumenten."""
        assert len(VALID_BOAT_CLASSES) == 13

    @pytest.mark.parametrize("boat_class", sorted(bc.value for bc in BoatClass))
    def test_every_enum_value_passes_validation(self, boat_class):
        assert validate_boat_class(boat_class) == boat_class

    @pytest.mark.parametrize(
        "boat_class",
        ["racing_sail", "daysailer", "catamaran_motor", "sport_cruiser", "explorer"],
    )
    def test_the_five_previously_rejected_classes_pass(self, boat_class):
        """Genau diese fuenf lehnte die Validierung ab."""
        assert validate_boat_class(boat_class) == boat_class

    def test_every_class_has_module_defaults(self):
        """Eine gueltige Klasse ohne Defaults faellt in den Analysemodulen zurueck."""
        from app.services.analysis.ergonomics import BOAT_CLASS_DEFAULTS as ergo
        from app.services.analysis.service_patterns import BOAT_CLASS_DEFAULTS as svc

        for defaults, name in ((ergo, "ergonomics"), (svc, "service_patterns")):
            missing = sorted(VALID_BOAT_CLASSES - set(defaults))
            assert not missing, f"{name}: keine Defaults fuer {missing}"


class TestZurueckgezogeneNamen:
    def test_every_alias_target_is_canonical(self):
        broken = {a: t for a, t in BOAT_CLASS_ALIASES.items() if t not in VALID_BOAT_CLASSES}
        assert not broken, f"Aliase zeigen auf ungueltige Klassen: {broken}"

    def test_no_alias_shadows_a_canonical_class(self):
        shadowing = sorted(a for a in BOAT_CLASS_ALIASES if a in VALID_BOAT_CLASSES)
        assert not shadowing, f"Aliase ueberschreiben kanonische Klassen: {shadowing}"

    @pytest.mark.parametrize(
        "retired,canonical",
        [
            ("catamaran_power", "catamaran_motor"),
            ("performance_sail", "racing_sail"),
            ("bluewater_sail", "cruising_sail"),
            ("dinghy", "daysailer"),
            ("cruising_motor", "small_motor"),
        ],
    )
    def test_retired_names_normalise(self, retired, canonical):
        assert normalize_boat_class(retired) == canonical
        assert validate_boat_class(retired) == canonical

    def test_case_and_whitespace_are_tolerated(self):
        assert validate_boat_class("  Cruising_Sail  ") == "cruising_sail"


class TestUnbekanntes:
    def test_unknown_class_is_rejected(self):
        with pytest.raises(DataValidationError):
            validate_boat_class("segelboot_gross")

    def test_normalize_passes_unknown_through(self):
        """Der Aufrufer soll noch warnen koennen — nicht still verschlucken."""
        assert normalize_boat_class("segelboot_gross") == "segelboot_gross"

    def test_empty_is_rejected(self):
        with pytest.raises(DataValidationError):
            validate_boat_class("")
