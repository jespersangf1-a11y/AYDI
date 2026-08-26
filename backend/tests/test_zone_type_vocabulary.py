"""Tests fuer das Zonentyp-Vokabular (Validierung <-> Domaenen <-> Synonyme).

Hintergrund: Ein Zonentyp, den `get_domain_for_zone_type()` nicht kennt, faellt
still aus der Domaenen-Abdeckung heraus. Das Ergebnis wirkt vollstaendig, ist es
aber nicht. Zwei Fehlerquellen gab es dafuer:

1. Die beiden Vokabulare (`VALID_ZONE_TYPES` in validation.py und die
   `zone_types` der Domaenen) waren um je 4 Eintraege auseinandergelaufen.
2. Gebraeuchliche Synonyme ("galley" fuer die Bordkueche) waren ueberhaupt nicht
   abgebildet und wurden nur als Warnung geloggt.
"""

import pytest

from app.core.domains import get_all_zone_types, get_domain_for_zone_type
from app.core.validation import (
    VALID_ZONE_TYPES,
    ZONE_TYPE_ALIASES,
    normalize_zone_type,
    validate_zone,
    validate_zones,
)


class TestZoneTypeVocabularyConsistency:
    def test_every_domain_zone_type_is_valid(self):
        """Ein Typ, den eine Domaene kennt, muss die Validierung passieren."""
        unknown = sorted(set(get_all_zone_types()) - VALID_ZONE_TYPES)
        assert not unknown, (
            f"Domaenen kennen Zonentypen, die VALID_ZONE_TYPES nicht enthaelt: {unknown}"
        )

    def test_every_valid_zone_type_maps_to_a_domain(self):
        """Ein gueltiger Typ ohne Domaene verschwindet aus der Abdeckung."""
        orphans = sorted(zt for zt in VALID_ZONE_TYPES if get_domain_for_zone_type(zt) is None)
        assert not orphans, (
            f"Gueltige Zonentypen ohne Domaenenzuordnung: {orphans}"
        )


class TestZoneTypeAliases:
    def test_galley_is_understood(self):
        """'galley' ist der englische Standardbegriff fuer die Bordkueche."""
        assert normalize_zone_type("galley") == "pantry"
        assert get_domain_for_zone_type(normalize_zone_type("galley")) is not None

    @pytest.mark.parametrize(
        "synonym,canonical",
        [
            ("Galley", "pantry"),
            ("  KITCHEN  ", "pantry"),
            ("wc", "head"),
            ("nasszelle", "head"),
            ("salon", "saloon"),
            ("maschinenraum", "engine_room"),
            ("chart_table", "nav_station"),
            ("lazarette", "storage"),
            ("v_berth", "forepeak"),
        ],
    )
    def test_synonyms_map_to_canonical(self, synonym, canonical):
        assert normalize_zone_type(synonym) == canonical

    def test_every_alias_target_is_canonical(self):
        """Ein Alias darf nie auf einen ebenfalls unbekannten Typ zeigen."""
        broken = {a: t for a, t in ZONE_TYPE_ALIASES.items() if t not in VALID_ZONE_TYPES}
        assert not broken, f"Aliase zeigen auf ungueltige Zonentypen: {broken}"

    def test_no_alias_shadows_a_canonical_type(self):
        """Ein kanonischer Typ darf nicht als Alias auf etwas anderes zeigen."""
        shadowing = {a for a in ZONE_TYPE_ALIASES if a in VALID_ZONE_TYPES}
        assert not shadowing, f"Aliase ueberschreiben kanonische Typen: {sorted(shadowing)}"

    def test_unknown_type_passes_through_unchanged(self):
        assert normalize_zone_type("voellig_unbekannt") == "voellig_unbekannt"


class TestZoneNormalisationIsWrittenBack:
    def test_validate_zone_rewrites_zone_type(self):
        zone = {"name": "Kombuese", "zone_type": "galley", "polygon": [[0, 0], [1, 0], [1, 1]]}
        result = validate_zone(zone)
        assert result["zone_type"] == "pantry"

    def test_validate_zone_rewrites_legacy_type_key(self):
        zone = {"name": "Kombuese", "type": "galley"}
        result = validate_zone(zone)
        assert result["type"] == "pantry"

    def test_validate_zones_normalises_the_whole_list(self):
        zones = [{"name": "a", "zone_type": "galley"}, {"name": "b", "zone_type": "wc"}]
        result = validate_zones(zones)
        assert [z["zone_type"] for z in result] == ["pantry", "head"]

    def test_canonical_type_is_left_alone(self):
        zone = {"name": "a", "zone_type": "saloon"}
        assert validate_zone(zone)["zone_type"] == "saloon"
