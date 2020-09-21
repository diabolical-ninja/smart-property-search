"""Unit tests for src/nbn.py."""

from nbn import NBN


class TestNBN:
    """Tests get_location_ids_from_lat_long functionality."""

    def setup_class(self) -> None:
        """Instantiate NBN Class for testing."""
        self.nbn = NBN()

    def test_get_location_ids_from_lat_long(self) -> None:
        """Test retrieving location ID from lat/long."""
        response = self.nbn.get_location_ids_from_lat_long(
            latitude=-37.817155, longitude=144.967067
        )
        assert isinstance(response, dict)

    def test_location_information(self) -> None:
        """Test retreive location information."""
        response = self.nbn.location_information(location_id="LOC000050228944")
        assert isinstance(response, dict)

    def test_get_location_ids_from_address(self) -> None:
        """Test retrieving location for street address."""
        response = self.nbn.get_location_ids_from_address(
            "1 Flinders Street, Melbourne VIC"
        )
        assert isinstance(response, dict)
