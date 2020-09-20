"""Unit tests for src/smart_search.py."""

import os
import sys
from datetime import datetime

import pytest

from pytz import timezone

sys.path.append(os.path.join(os.getcwd(), "src"))

from smart_search import SmartSearch  # noqa


default_search_parameters = {
    "listingType": "Sale",
    "propertyTypes": ["Penthouse", "ApartmentUnitFlat"],
    "minBedrooms": 4,
    "minBathrooms": 3,
    "minPrice": 4500000,
    "locations": [{"state": "VIC", "postcode": "3000"}],
}


@pytest.fixture
def setup_smart_search() -> None:
    """Create an instance to test against.

    Returns:
        SmartSearch: Instantiated smart search class
    """
    scopes = ["api_listings_read", "api_agencies_read"]
    searcher = SmartSearch(
        domain_client_id=os.getenv("CLIENT_ID"),
        domain_client_secret=os.getenv("CLIENT_SECRET"),
        domain_scopes=scopes,
        google_maps_key=os.getenv("GOOGLE_MAPS_KEY"),
    )
    return searcher


def test_listings_search(setup_smart_search: object) -> None:
    """Tests that search results can be returned.

    Args:
        setup_smart_search (object): Initialises the class
    """
    setup_smart_search.listings_search(default_search_parameters)

    assert hasattr(setup_smart_search, "search_results")
    assert len(setup_smart_search.search_results) > 0
    assert isinstance(setup_smart_search.search_results, list)


@pytest.mark.parametrize(
    "input_max_travel_time, input_destination",
    [
        (20, "Spring St, East Melbourne VIC 3002"),
        (10, "18 Lower Esplanade, St Kilda VIC 3182"),
        (40, "Spencer St, Docklands VIC 3008"),
    ],
)
def test_filter_by_travel_time(
    setup_smart_search: object, input_max_travel_time: int, input_destination: str
) -> None:
    """Tests that search results can be filtered by travel time.

    Args:
        setup_smart_search (object): Initialises the class
        input_max_travel_time (int): Input value to travel time threshold
        input_destination (str): Input value to target destination
    """
    setup_smart_search.listings_search(default_search_parameters)
    initial_number_of_search_results = len(setup_smart_search.search_results)
    setup_smart_search.filter_by_travel_time(input_max_travel_time, input_destination)

    assert len(setup_smart_search.search_results) <= initial_number_of_search_results


@pytest.mark.parametrize(
    "input_travel_time, input_max_travel_time, expected",
    [(1, 2, True), (2, 2, True), (3, 2, False), ("No Result", 1, False)],
)
def test__travel_time_less_than_threshold(
    input_travel_time: int, input_max_travel_time: int, expected: bool
) -> None:
    """Tests staticmethod that determines if travel time is acceptable.

    Args:
        input_travel_time (int): Test actual travel time
        input_max_travel_time (int): Test max travel time
        expected (bool): Expected outcome
    """
    assert (
        SmartSearch._travel_time_less_than_threshold(
            input_travel_time, input_max_travel_time
        ) == expected
    )


@pytest.mark.parametrize(
    "input_destination",
    [
        "Spring St, East Melbourne VIC 3002",
        "18 Lower Esplanade, St Kilda VIC 3182",
        "Spencer St, Docklands VIC 3008",
    ],
)
def test_calculate_travel_time(
    setup_smart_search: object, input_destination: str
) -> None:
    """Tests calculation of travel time.

    Args:
        setup_smart_search (object): Initialises the class
        input_destination (str): Input value to target destination
    """
    setup_smart_search.listings_search(default_search_parameters)
    setup_smart_search.calculate_travel_time(input_destination)

    for item in setup_smart_search.search_results:
        assert "travel_info" in item
        assert len(item["travel_info"].keys()) == 2


@pytest.mark.parametrize(
    "input_destination, input_chunk_size",
    [
        ("Spring St, East Melbourne VIC 3002", 1),
        ("Spring St, East Melbourne VIC 3002", 3),
        ("Spring St, East Melbourne VIC 3002", 7),
    ],
)
def test_get_distance(
    setup_smart_search: object, input_destination: str, input_chunk_size: int
) -> None:
    """Test retrieval of travel time for each listing.

    Args:
        setup_smart_search (object): Initialises the class
        input_destination (str): Input value to target destination
        input_chunk_size (int): How many origins to use in each batch
    """
    origin_lat_longs = [
        (-26.4097576, 153.07724),
        (-33.7776146, 151.188339),
        (-27.9072475, 153.406281),
        (-33.0098228, 151.632324),
        (-28.6467628, 153.615677),
        (-33.8796043, 151.239563),
        (-34.76952, 150.626236),
        (-32.9259758, 151.634979),
        (-35.0999451, 147.501328),
        (-33.8941422, 151.21225),
        (-33.9146767, 151.255173),
        (-33.90792, 151.257736),
        (-33.855217, 151.151764),
        (-33.9003868, 151.266663),
        (-34.670887, 150.545441),
    ]

    distances = setup_smart_search.get_distances(
        origin_lat_longs, input_destination, input_chunk_size
    )

    assert isinstance(distances, list)
    assert len(origin_lat_longs) == len(distances)


class TestCreateNextDay:
    """Suite of tests for create_next_day calculation."""

    @pytest.mark.parametrize(
        "input_target_day_of_week, input_target_hour, input_target_minute, input_timezone",
        [
            (1, 1, 10, "Australia/Melbourne"),
            (2, 4, 20, "Australia/Adelaide"),
            (3, 8, 30, "Australia/Sydney"),
            (4, 12, 40, "Australia/Perth"),
            (5, 15, 50, "Australia/Hobart"),
            (6, 22, 12, "Australia/Canberra"),
            (7, 7, 4, "Australia/Brisbane"),
        ],
    )
    def test__create_next_day_valid_input(
        self,
        input_target_day_of_week: int,
        input_target_hour: int,
        input_target_minute: int,
        input_timezone: str,
    ) -> None:
        """Tests the generated day of week.

        Args:
            input_target_day_of_week (int): Target ISO day of week number
            input_target_hour (int): Target hour of the day in 24hr time
            input_target_minute (int): Target minute of the hour
            input_timezone (str): Target timezone
        """
        generated_test_value = SmartSearch._create_next_day(
            input_target_day_of_week,
            input_target_hour,
            input_target_minute,
            input_timezone,
        )

        assert generated_test_value > datetime.now(timezone(input_timezone))
        assert generated_test_value.isoweekday() == input_target_day_of_week
        assert generated_test_value.hour == input_target_hour
        assert generated_test_value.minute == input_target_minute

    @pytest.mark.parametrize(
        "input_target_day_of_week, input_target_hour, input_target_minute, input_timezone",
        [(3, 24, 30, "Australia/Sydney"), (5, 15, 65, "Australia/Hobart")],
    )
    def test__create_next_day_invalid_input(
        self,
        input_target_day_of_week: int,
        input_target_hour: int,
        input_target_minute: int,
        input_timezone: str,
    ) -> None:
        """Tests the generated day of week.

        Args:
            input_target_day_of_week (int): Target ISO day of week number
            input_target_hour (int): Target hour of the day in 24hr time
            input_target_minute (int): Target minute of the hour
            input_timezone (str): Target timezone
        """
        with pytest.raises(ValueError):
            SmartSearch._create_next_day(
                input_target_day_of_week,
                input_target_hour,
                input_target_minute,
                input_timezone,
            )


@pytest.mark.parametrize(
    "input_distance_result",
    [
        {
            "distance": {"text": "942 km", "value": 942041},
            "duration": {"text": "15 hours 34 mins", "value": 56012},
            "status": "OK",
        },
        {"status": "ZERO_RESULTS"},
    ],
)
def test__extract_distance_duration(input_distance_result: dict) -> None:
    """Tests extraction of distance information from gmaps result.

    Args:
        input_distance_result (dict): gmaps distance element
    """
    result = SmartSearch._extract_distance_duration(input_distance_result)

    assert isinstance(result, dict)
    assert len(result.keys()) == 2
    assert "distance" in result
    assert "duration" in result


@pytest.mark.parametrize(
    "input_wanted_attributes", [[], ["AirConditioning"], ["Heating", "Outside"]]
)
def test_filter_by_attributes(
    setup_smart_search: object, input_wanted_attributes: list
) -> None:
    """Tests attribute only filtering.

    Args:
        setup_smart_search (object): Initialises the class
        input_wanted_attributes (list): Items to filter results by
    """
    setup_smart_search.listings_search(default_search_parameters)
    initial_number_of_search_results = len(setup_smart_search.search_results)

    setup_smart_search.filter_by_attribute(input_wanted_attributes)
    assert isinstance(setup_smart_search.search_results, list)
    assert len(setup_smart_search.search_results) <= initial_number_of_search_results
