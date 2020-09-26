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
    "propertyTypes": ["House", "NewApartments"],
    "minBedrooms": 3,
    "minBathrooms": 2,
    "minCarspaces": 1,
    "locations": [
        {
            "state": "Vic",
            "region": "",
            "area": "",
            "suburb": "Melbourne",
            "postCode": "",
            "includeSurroundingSuburbs": False,
        }
    ],
}

sample_listing = {
    "type": "PropertyListing",
    "listing": {
        "listing_type": "Sale",
        "id": 2013958589,
        "advertiser": {
            "type": "Agency",
            "id": 4697,
            "name": "Urbane Inner West",
            "logo_url": "https://images.domain.com.au/img/Agencys/4697/logo_4697.GIF?date=2015-03-31-10-20-47",  # noqa
            "preferred_colour_hex": "#019FC4",
            "banner_url": "https://images.domain.com.au/img/Agencys/4697/banner_4697.GIF",
            "contacts": [
                {
                    "name": "Charles Bailey",
                    "photo_url": "https://images.domain.com.au/img/4697/contact_1153031.JPG?mod=171030-201656",  # noqa
                }
            ],
        },
        "price_details": {"display_price": "Contact Agent"},
        "media": [
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2013958589_1_0_171026_043335-w4500-h3000",  # noqa
            }
        ],
        "property_details": {
            "state": "NSW",
            "features": ["Gas", "Study"],
            "property_type": "House",
            "all_property_types": ["House"],
            "bathrooms": 2,
            "bedrooms": 3,
            "carspaces": 1,
            "unit_number": "",
            "street_number": "177",
            "street": "Australia Street",
            "area": "Inner West",
            "region": "Sydney Region",
            "suburb": "NEWTOWN",
            "postcode": "2042",
            "displayable_address": "177 Australia Street, Newtown",
            "latitude": -33.8938522,
            "longitude": 151.176926,
            "landArea": 120,
        },
        "headline": "Classic terrace enhanced for modern urban living",
        "summary_description": "<b>Classic terrace enhanced for modern urban living</b><br />This traditional two-level terrace has been cleverly renovated throughout and now offers a bright and stylish home with tastefully appointed interiors and a fresh modern feel. Positioned in a...",  # noqa
        "has_floorplan": True,
        "has_video": False,
        "labels": ["New"],
        "auction_schedule": {
            "time": "2017-11-18T09:00:00",
            "auction_location": "On Site",
        },
        "inspection_schedule": {
            "by_sppointment": False,
            "recurring": False,
            "times": [
                {
                    "opening_time": "2017-11-01T17:30:00",
                    "closing_time": "2017-11-01T18:00:00",
                }
            ],
        },
        "listing_slug": "177-australia-street-newtown-nsw-2042-2013958589",
    },
}

sample_listing_empty = {
    "listing": {
        "property_details": {
            "displayable_address": "123 fake st, Willywonka",
            "state": "NSW",
        }
    }
}

sample_listing_with_nbn = {
    "listing": {},
    "nbn_details": {
        "timestamp": 1600684835755,
        "servingArea": {
            "csaId": "CSA200000000647",
            "techType": "HFC",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "serviceCategory": "brownfields",
            "rfsMessage": "Oct 2018",
            "description": "Newtown",
        },
        "addressDetail": {
            "id": "LOC000098725003",
            "latitude": -33.893853,
            "longitude": 151.176923,
            "reasonCode": "HFC_CT",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "disconnectionStatus": "PAST",
            "disconnectionDate": "Nov 2019",
            "techType": "HFC",
            "formattedAddress": "LOT 4 177 AUSTRALIA ST NEWTOWN NSW 2042 Australia",
            "address1": "Lot 4 177 Australia St",
            "address2": "Newtown NSW 2042 Australia",
            "statusMessage": "connected-true",
            "frustrated": False,
            "zeroBuildCost": True,
            "cbdpricing": False,
            "ee": True,
        },
    },
}

sample_listing_with_walkscore = {
    "listing": {},
    "walkscore": {
        "status": 1,
        "walkscore": 92,
        "description": "Walker's Paradise",
        "updated": "2020-04-20 09:16:05.993243",
        "logo_url": "https://cdn.walk.sc/images/api-logo.png",
        "more_info_icon": "https://cdn.walk.sc/images/api-more-info.gif",
        "more_info_link": "https://www.redfin.com/how-walk-score-works",
        "ws_link": "https://www.walkscore.com/score/9.slash.100-Commercial-Road-South-Yarra/lat=-37.8454742/lng=144.984787/?utm_source=nick.klein@rutgers.edu&utm_medium=ws_api&utm_campaign=ws_api",  # noqa
        "help_link": "https://www.redfin.com/how-walk-score-works",
        "snapped_lat": -37.845,
        "snapped_lon": 144.9855,
        "transit": {
            "score": 95,
            "description": "Rider's Paradise ",
            "summary": "18 nearby routes: 4 bus, 14 rail, 0 other",
        },
    },
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
        walkscore_api_key=os.getenv("WSAPIKEY"),
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
        )
        == expected
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

        assert (
            generated_test_value.date() >= datetime.now(timezone(input_timezone)).date()
        )
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


@pytest.mark.parametrize(
    "input_search_features, input_feature_search_words, expected",
    [
        (["AirConditioning"], [], True),
        (["BalconyDeck", "GardenCourtyard"], [], True),
        ([], ["air"], True),
        ([], ["not a match", "conditioning"], True),
        ([], ["airconditioning"], True),
        (["Not a Feature"], [], False),
        ([], ["AIR"], False),
        ([], ["no", "matching", "terms"], False),
        (["Not a Feature"], ["no", "matching", "terms"], False),
    ],
)
def test__has_feature(
    input_search_features: list, input_feature_search_words: list, expected: bool
) -> None:
    """Tests for identification of a feature.

    Args:
        input_search_features (list): List of test desired domain features
        input_feature_search_words (list): List of test feature search words
        expected (bool): Expected output
    """
    test_search_description = "This place has airconditioning, aint it great"
    available_property_features = [
        "AirConditioning",
        "BuiltInWardrobes",
        "CableOrSatellite",
        "Ensuite",
        "Floorboards",
        "Gas",
        "InternalLaundry",
        "PetsAllowed",
        "SecureParking",
        "SwimmingPool",
        "Furnished",
        "GroundFloor",
        "WaterViews",
        "NorthFacing",
        "CityViews",
        "IndoorSpa",
        "Gym",
        "AlarmSystem",
        "Intercom",
        "BroadbandInternetAccess",
        "Bath",
        "Fireplace",
        "SeparateDiningRoom",
        "Heating",
        "Dishwasher",
        "Study",
        "TennisCourt",
        "Shed",
        "FullyFenced",
        "BalconyDeck",
        "GardenCourtyard",
        "OutdoorSpa",
        "DoubleGlazedWindows",
        "EnergyEfficientAppliances",
        "WaterEfficientAppliances",
        "WallCeilingInsulation",
        "RainwaterStorageTank",
        "GreywaterSystem",
        "WaterEfficientFixtures",
        "SolarHotWater",
        "SolarPanels",
    ]

    assert (
        SmartSearch._has_feature(
            search_features=input_search_features,
            feature_search_words=input_feature_search_words,
            property_details_features=available_property_features,
            property_description=test_search_description,
        )
        == expected
    )


@pytest.mark.parametrize(
    "input_nbn_value",
    [
        (["FTTP"]),
        (["FTTN"]),
        (["FTTB"]),
        (["HFC"]),
        (["FTTC"]),
        (["FTTN"]),
        (["FTTB", "HFC"]),
        (["FTTN", "FTTC", "FTTB"]),
    ],
)
def test_filter_nbn(setup_smart_search: object, input_nbn_value: list) -> None:
    """Tests that results are filtered based on the presence of NBN.

    Args:
        setup_smart_search (object): Initialises the class
        input_nbn_value (list): NBN tech types to filter on
    """
    setup_smart_search.listings_search(default_search_parameters)
    initial_number_of_search_results = len(setup_smart_search.search_results)

    setup_smart_search.filter_nbn(input_nbn_value)

    assert len(setup_smart_search.search_results) <= initial_number_of_search_results
    assert isinstance(setup_smart_search.search_results, list)


@pytest.mark.parametrize(
    "sample_listing, expected_nbn_addition",
    [
        (
            sample_listing,
            {
                "nbn_details": {
                    "timestamp": 1600684835755,
                    "servingArea": {},
                    "addressDetail": {},
                }
            },
        ),
        (sample_listing_empty, {"nbn_details": {}}),
    ],
)
def test__append_nbn(
    setup_smart_search: object, sample_listing: dict, expected_nbn_addition: dict
) -> None:
    """Tests retrieving and append NBN info to a listing.

    Args:
        setup_smart_search (object): Initialises the class
        sample_listing (dict): Sample domain listing
        expected_nbn_addition (dict): NBN keys that should be appended to the listing
    """
    setup_smart_search.listings_search(default_search_parameters)

    listing_with_nbn = setup_smart_search._append_nbn(sample_listing)
    sample_listing["nbn_details"] = expected_nbn_addition

    assert isinstance(listing_with_nbn, dict)
    assert "nbn_details" in listing_with_nbn

    assert set(listing_with_nbn.keys()) == set(sample_listing.keys())

    assert set(listing_with_nbn["nbn_details"].keys()) == set(
        sample_listing["nbn_details"].keys()
    )


@pytest.mark.parametrize(
    "sample_listing, desired_nbn, expected",
    [
        ({"listing": {}, "nbn_details": {}}, ["FTTN"], False),
        (sample_listing_with_nbn, ["HFC"], True,),
        (sample_listing_with_nbn, ["FTTC", "HFC"], True,),
        (sample_listing_with_nbn, ["FTTN"], False,),
        (sample_listing_with_nbn, ["FTTN", "FTTB"], False,),
        (
            {
                "listing": {},
                "nbn_details": {
                    "timestamp": 1600684835755,
                    "servingArea": {},
                    "addressDetail": {},
                },
            },
            [],
            True,
        ),
    ],
)
def test__has_desired_nbn(
    sample_listing: dict, desired_nbn: list, expected: bool
) -> None:
    """Tests to see if the desired NBN technology is present.

    Args:
        sample_listing (dict): Listing with NBN information to test against
        desired_nbn (list): Desired NBN technology
        expected (bool): Expected outcome
    """
    assert SmartSearch._has_desired_nbn(sample_listing, desired_nbn) == expected


@pytest.mark.parametrize("walkscore_test_value", [0, 50, 80, 100])
def test_filter_walkscore(
    setup_smart_search: object, walkscore_test_value: int
) -> None:
    """Tests that results are filtered based on the desired walkscore.

    Args:
        setup_smart_search (object): Initialises the class
        walkscore_test_value (list): Walkscore threshold
    """
    setup_smart_search.listings_search(default_search_parameters)
    initial_number_of_search_results = len(setup_smart_search.search_results)

    setup_smart_search.filter_walkscore(walkscore_test_value)

    assert len(setup_smart_search.search_results) <= initial_number_of_search_results
    assert isinstance(setup_smart_search.search_results, list)


@pytest.mark.parametrize(
    "sample_listing",
    [
        {
            "listing": {
                "property_details": {
                    "latitude": -31.3399963,
                    "longitude": 151.513855,
                    "displayable_address": "340 Flags Niangala Road, Walcha",
                }
            }
        },
        {
            "listing": {
                "property_details": {
                    "latitude": -37.8177834,
                    "longitude": 144.959732,
                    "displayable_address": "439 Collins St Collins Street, Melbourne",
                }
            }
        },
    ],
)
def test__append_walkscore(setup_smart_search: object, sample_listing: dict) -> None:
    """Tests retrieving and append walkscore info to a listing.

    Args:
        setup_smart_search (object): Initialises the class
        sample_listing (dict): Small sample domain listing with just address info
    """
    setup_smart_search.listings_search(default_search_parameters)
    listing_with_walkscore = setup_smart_search._append_walkscore(sample_listing)

    assert isinstance(listing_with_walkscore, dict)
    assert "walkscore" in listing_with_walkscore
    assert "walkscore" in listing_with_walkscore["walkscore"]


@pytest.mark.parametrize(
    "sample_listing, walkscore_test_value, expected",
    [
        ({"listing": {}, "walkscore": {}}, 50, False),
        (sample_listing_with_walkscore, 0, True),
        (sample_listing_with_walkscore, 50, True),
        (sample_listing_with_walkscore, 100, False),
    ],
)
def test__has_sufficient_walkscore(
    sample_listing: dict, walkscore_test_value: int, expected: bool
) -> None:
    """Tests to see if the minimum walkscore threshold is satisfied.

    Args:
        sample_listing (dict): Listing with walkscore information to test against
        walkscore_test_value (int): Minimum acceptable walkscore
        expected (bool): Expected outcome
    """
    assert (
        SmartSearch._has_sufficient_walkscore(sample_listing, walkscore_test_value)
        == expected
    )
