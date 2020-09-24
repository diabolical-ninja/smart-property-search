"""Unit tests for src/walkscore.py."""

import os
import sys

import pytest

sys.path.append(os.path.join(os.getcwd(), "src"))

from walkscore import WalkScore  # noqa


@pytest.fixture
def setup_walkscore() -> None:
    """Create an instance of walkscore to test against.

    Returns:
        WalkScore: Instantiated WalkScore client
    """
    ws_client = WalkScore(os.getenv("WSAPIKEY"))
    return ws_client


@pytest.mark.parametrize(
    "lat, lon, address",
    [
        (-33.8938522, 151.176926, "177 Australia Street, Newtown"),
        (-37.8177834, 144.959732, "439 Collins St Collins Street, Melbourne"),
    ],
)
def test_get_score(
    setup_walkscore: object, lat: float, lon: float, address: str
) -> None:
    """Tests retrieval of the walkscore.

    Args:
        setup_walkscore (object): Instantiated walkscore object
        lat (float): Address latitude
        lon (float): Address longtitude
        address (str): Display address
    """
    response = setup_walkscore.get_score(lat, lon, address)

    assert isinstance(response, dict)
    assert set(response.keys()) == set(
        [
            "status",
            "walkscore",
            "description",
            "updated",
            "logo_url",
            "more_info_icon",
            "more_info_link",
            "ws_link",
            "help_link",
            "snapped_lat",
            "snapped_lon",
            "transit",
        ]
    )
    assert set(response["transit"].keys()) == set(["score", "description", "summary"])


@pytest.mark.parametrize(
    "lat, lon, address, transit, bike",
    [
        (-37.8177834, 144.959732, "439 Collins St Collins Street, Melbourne", 1, 1),
        (-37.8177834, 144.959732, "439 Collins St Collins Street, Melbourne", 0, 1),
        (-37.8177834, 144.959732, "439 Collins St Collins Street, Melbourne", 1, 0),
    ],
)
def test_get_score_transit_bike(
    setup_walkscore: object,
    lat: float,
    lon: float,
    address: str,
    transit: int,
    bike: int,
) -> None:
    """Tests retrieval of the walkscore with transit & bike parameter changes.

    Args:
        setup_walkscore (object): Instantiated walkscore object
        lat (float): Address latitude
        lon (float): Address longtitude
        address (str): Display address
        transit (int): Whether or not to include transit information
        bike (int): Whether or not to request bike information
    """
    response = setup_walkscore.get_score(lat, lon, address, transit, bike)

    assert isinstance(response, dict)

    if transit == 0:
        assert "transit" not in response

    if transit == 1:
        assert "transit" in response
        assert set(response["transit"].keys()) == set(["score", "description", "summary"])


def test_get_score_failure(setup_walkscore: object) -> None:
    """Tests generation of an exception message.

    Args:
        setup_walkscore (object): Instantiated walkscore object
    """
    with pytest.raises(Exception):
        setup_walkscore.get_score(latitude="not a latitude",
                                  longitude="not a longitude",
                                  address="not an address")
