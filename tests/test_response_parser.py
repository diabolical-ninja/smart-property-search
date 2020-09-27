"""Unit tests for src/response_parser.py."""

import os
import sys

import pytest

sys.path.append(os.path.join(os.getcwd(), "src"))

from response_parser import (
    clean_domain,
    clean_response,
    clean_travel_info,
    clean_walkscore,
)


sample_one = {
    "type": "PropertyListing",
    "listing": {
        "promo_level": None,
        "listing_type": "Sale",
        "id": 2016359058,
        "project_id": None,
        "advertiser": {
            "type": "Agency",
            "id": 31049,
            "name": "Austrump Glen Pty Ltd",
            "logo_url": "https://images.domain.com.au/img/Agencys/31049/logo_31049.png",
            "preferred_colour_hex": "#000000",
            "banner_url": "https://images.domain.com.au/img/Agencys/31049/banner_31049.png",
            "contacts": [
                {
                    "name": "Emily Liu",
                    "photo_url": "https://images.domain.com.au/img/31049/contact_1754765.jpeg?mod=200812-181210",
                },
                {
                    "name": "Angus Liu",
                    "photo_url": "https://images.domain.com.au/img/31049/contact_1616963.png?mod=200810-112540",
                },
            ],
        },
        "price_details": {
            "price": None,
            "price_from": None,
            "price_to": None,
            "display_price": "Contact agent",
        },
        "media": [
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016359058_1_1_200708_012540-w1140-h624",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016359058_2_1_200708_012540-w1227-h738",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016359058_3_1_200708_012540-w1197-h614",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016359058_4_1_200708_012534-w977-h546",
            },
        ],
        "property_details": {
            "state": "VIC",
            "features": [
                "AirConditioning",
                "BuiltInWardrobes",
                "Floorboards",
                "SecureParking",
                "CityViews",
                "Bath",
            ],
            "property_type": "ApartmentUnitFlat",
            "all_property_types": ["ApartmentUnitFlat"],
            "bathrooms": 2.0,
            "bedrooms": 3.0,
            "carspaces": 1,
            "unit_number": "",
            "street_number": "",
            "street": "",
            "area": "North",
            "region": "Melbourne Region",
            "suburb": "FOOTSCRAY",
            "suburb_id": None,
            "postcode": "3011",
            "displayable_address": "Footscray",
            "latitude": -37.7989,
            "longitude": 144.892365,
            "map_certainty": None,
            "land_area": None,
            "building_area": None,
            "only_show_properties": None,
            "display_address_type": None,
            "is_rural": None,
            "top_spot_keywords": None,
            "is_new": None,
            "tags": None,
        },
        "headline": "Brand 3bedroom new spacious attraction with affordability price",
        "summary_description": "<b></b><br />Choose from low or high level, this 3 bed, 2 bath 1 car park floorplan will accommodate you with a commitment for contemporary and blissful lifestyle. It sets in a grand scaled complex, with an impressively spacious layout, delivering the ...",
        "has_floorplan": True,
        "has_video": False,
        "labels": [],
        "auction_schedule": None,
        "date_available": None,
        "date_listed": None,
        "inspection_schedule": {
            "by_appointment": True,
            "recurring": False,
            "times": [],
        },
        "sold_data": None,
        "listing_slug": "footscray-vic-3011-2016359058",
    },
    "listings": None,
    "project": None,
    "travel_info": {"distance": 6885, "duration": 1440},
    "nbn_details": {
        "timestamp": 1601087093781,
        "servingArea": {
            "csaId": "CSA300000000325",
            "techType": "FTTC",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "serviceCategory": "brownfields",
            "rfsMessage": "Apr 2018",
            "description": "Footscray",
        },
        "addressDetail": {
            "latitude": -37.7988987,
            "longitude": 144.892357,
            "reasonCode": "FTTC_SA",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "techType": "FTTC",
            "ee": False,
        },
    },
    "walkscore": {
        "status": 1,
        "walkscore": 94,
        "description": "Walker's Paradise",
        "updated": "2020-09-11 01:15:56.111427",
        "logo_url": "https://cdn.walk.sc/images/api-logo.png",
        "more_info_icon": "https://cdn.walk.sc/images/api-more-info.gif",
        "more_info_link": "https://www.redfin.com/how-walk-score-works",
        "ws_link": "https://www.walkscore.com/score/Footscray/lat=-37.7989/lng=144.892365/?utm_source=nick.klein@rutgers.edu&utm_medium=ws_api&utm_campaign=ws_api",
        "help_link": "https://www.redfin.com/how-walk-score-works",
        "snapped_lat": -37.7985,
        "snapped_lon": 144.8925,
        "transit": {
            "score": 76,
            "description": "Excellent Transit",
            "summary": "30 nearby routes: 19 bus, 11 rail, 0 other",
        },
    },
}


sample_two = {
    "type": "PropertyListing",
    "listing": {
        "promo_level": None,
        "listing_type": "Sale",
        "project_id": None,
        "advertiser": {
            "type": "Agency",
            "id": 27501,
            "name": "Aumeca Group Pty Ltd",
            "logo_url": "https://images.domain.com.au/img/Agencys/27501/logo_27501.GIF?date=2016-03-04-09-53-37",
            "preferred_colour_hex": "#E67817",
            "banner_url": "https://images.domain.com.au/img/Agencys/27501/banner_27501.GIF",
            "contacts": [
                {
                    "name": "Zack Liu",
                    "photo_url": "https://images.domain.com.au/img/27501/contact_1639021.jpeg?mod=200703-195050",
                },
                {
                    "name": "Terrence Shen",
                    "photo_url": "https://images.domain.com.au/img/27501/contact_1707425.jpeg?mod=200703-195200",
                },
            ],
        },
        "media": [
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016210813_12_1_200412_115522-w2736-h1827",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016072725_2_1_200327_113015-w3000-h2000",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016210813_1_1_200412_115522-w2736-h1827",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016210813_3_1_200412_115522-w2736-h1827",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016210813_4_1_200412_115522-w2736-h1827",
            },
        ],
        "headline": "Unique Three-Bedroom Apartment in Urban Living Locale",
        "summary_description": "<b></b><br />PRIVATE INSPECTION and VIRTUAL WALK THROUGH AVAILABLE.\r\n\r\nCentrally located in the heart of Kensington this unique three-bedroom apartment boasts a court yard and is an impressive rare find.  \r\nA short walking distance to the finest amenit...",
        "has_floorplan": True,
        "has_video": False,
        "labels": [],
        "auction_schedule": None,
        "date_available": None,
        "date_listed": None,
        "inspection_schedule": {
            "by_appointment": False,
            "recurring": False,
            "times": [],
        },
        "sold_data": None,
    },
    "listings": None,
    "project": None,
    "travel_info": {"distance": 3958, "duration": 755},
    "nbn_details": {
        "timestamp": 1601087094794,
        "servingArea": {
            "csaId": "CSA300000010316",
            "techType": "FTTB",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "serviceCategory": "brownfields",
            "rfsMessage": "Feb 2020",
            "description": "72 ALTONA ST KENSINGTON, VIC 3031",
        },
        "addressDetail": {
            "id": "LOC000091047187",
            "latitude": -37.79708778,
            "longitude": 144.9264671,
            "reasonCode": "FTTB_C",
            "serviceType": "Fixed line",
            "serviceStatus": "available",
            "disconnectionStatus": "FUTURE",
            "disconnectionDate": "Sep 2021",
            "techType": "FTTB",
            "formattedAddress": "APT 107 72 ALTONA ST KENSINGTON VIC 3031 Australia",
            "address1": "Apt 107 72 Altona St",
            "address2": "Kensington VIC 3031 Australia",
            "statusMessage": "connected",
            "frustrated": False,
            "zeroBuildCost": True,
            "wp1DisconnectionDate": "10 September 2021",
            "wp1DisconnectionStatus": "FUTURE",
            "wp2DisconnectionDate": "10 September 2021",
            "wp2DisconnectionStatus": "FUTURE",
            "wp3DisconnectionDate": "10 September 2021",
            "wp3DisconnectionStatus": "FUTURE",
            "wp4DisconnectionDate": "10 September 2021",
            "wp4DisconnectionStatus": "FUTURE",
            "cbdpricing": False,
            "ee": True,
            "TC2SME": True,
        },
    },
    "walkscore": {
        "status": 1,
        "walkscore": 85,
        "description": "Very Walkable",
        "updated": "2020-03-21 12:32:06.005826",
        "logo_url": "https://cdn.walk.sc/images/api-logo.png",
        "more_info_icon": "https://cdn.walk.sc/images/api-more-info.gif",
        "more_info_link": "https://www.redfin.com/how-walk-score-works",
        "ws_link": "https://www.walkscore.com/score/107.slash.72-Altona-Street-Kensington/lat=-37.7969246/lng=144.92627/?utm_source=nick.klein@rutgers.edu&utm_medium=ws_api&utm_campaign=ws_api",
        "help_link": "https://www.redfin.com/how-walk-score-works",
        "snapped_lat": -37.797,
        "snapped_lon": 144.927,
        "transit": {
            "score": 70,
            "description": "Excellent Transit",
            "summary": "9 nearby routes: 3 bus, 6 rail, 0 other",
        },
    },
}


sample_three = {
    "type": "PropertyListing",
    "listing": {
        "promo_level": None,
        "listing_type": "Sale",
        "id": 2016113445,
        "project_id": None,
        "advertiser": {
            "type": "Agency",
            "id": 4478,
            "name": "Nelson Alexander Flemington",
            "logo_url": "https://images.domain.com.au/img/Agencys/4478/logo_4478.jpeg",
            "preferred_colour_hex": "#1e0f14",
            "banner_url": "https://images.domain.com.au/img/Agencys/4478/banner_4478.jpeg",
            "contacts": [
                {
                    "name": "Ryan Currie",
                    "photo_url": "https://images.domain.com.au/img/4478/contact_1316286.jpeg?mod=200806-142003",
                },
                {
                    "name": "Sally Carr",
                    "photo_url": "https://images.domain.com.au/img/4478/contact_1486900.jpeg?mod=200806-150334",
                },
            ],
        },
        "price_details": {
            "price": None,
            "price_from": None,
            "price_to": None,
            "display_price": "Private Sale $679,000",
        },
        "media": [
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016113445_1_1_200227_064936-w1600-h1067",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016113445_2_1_200227_064936-w1600-h1067",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016113445_3_1_200227_064936-w1600-h1067",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016113445_4_1_200227_064936-w1600-h1067",
            },
            {
                "category": "Image",
                "url": "https://bucket-api.domain.com.au/v1/bucket/image/2016113445_5_1_200227_064936-w1600-h1067",
            },
        ],
        "property_details": {
            "state": "VIC",
            "features": ["AirConditioning", "BuiltInWardrobes", "Gas", "Dishwasher"],
            "property_type": "Townhouse",
            "all_property_types": ["Townhouse"],
            "bathrooms": 2.0,
            "bedrooms": 3.0,
            "carspaces": 1,
            "unit_number": "",
            "street_number": "2A",
            "street": "Oscar Street",
            "area": "West",
            "region": "Melbourne Region",
            "suburb": "SEDDON",
            "suburb_id": None,
            "postcode": "3011",
            "displayable_address": "2A Oscar Street, Seddon",
            "latitude": -37.808197,
            "longitude": 144.884888,
            "map_certainty": None,
            "land_area": None,
            "building_area": None,
            "only_show_properties": None,
            "display_address_type": None,
            "is_rural": None,
            "top_spot_keywords": None,
            "is_new": None,
            "tags": None,
        },
        "headline": "ONE OF THE BEST VALUE TOWNHOMES CURRENTLY ON THE MARKET",
        "summary_description": "<b></b><br />*Due to Melbourne's Stage 4 Restrictions, all Nelson Alexander team members are working from home. Please contact us via email or phone to speak about your options to view this property virtually. Thank you.*\n\nSituated in the heart of Sedd...",
        "has_floorplan": True,
        "has_video": False,
        "labels": [],
        "auction_schedule": None,
        "date_available": None,
        "date_listed": None,
        "inspection_schedule": {
            "by_appointment": True,
            "recurring": False,
            "times": [],
        },
        "sold_data": None,
        "listing_slug": "2a-oscar-street-seddon-vic-3011-2016113445",
    },
    "listings": None,
    "project": None,
    "travel_info": {"distance": 8039, "duration": 1663},
    "nbn_details": {},
    "walkscore": {
        "status": 1,
        "walkscore": 77,
        "description": "Very Walkable",
        "updated": "2020-04-26 05:34:58.616991",
        "logo_url": "https://cdn.walk.sc/images/api-logo.png",
        "more_info_icon": "https://cdn.walk.sc/images/api-more-info.gif",
        "more_info_link": "https://www.redfin.com/how-walk-score-works",
        "ws_link": "https://www.walkscore.com/score/2A-Oscar-Street-Seddon/lat=-37.808197/lng=144.884888/?utm_source=nick.klein@rutgers.edu&utm_medium=ws_api&utm_campaign=ws_api",
        "help_link": "https://www.redfin.com/how-walk-score-works",
        "snapped_lat": -37.8075,
        "snapped_lon": 144.885,
    },
}


@pytest.mark.parametrize(
    "sample_search_result, expected",
    [
        (
            sample_one,
            {
                "listing": {
                    "id": 2016359058,
                    "listing_slug": "footscray-vic-3011-2016359058",
                    "price": "Contact agent",
                    "address": {
                        "displayable_address": "Footscray",
                        "postcode": "3011",
                        "state": "VIC",
                    },
                    "property_details": {
                        "property_type": "ApartmentUnitFlat",
                        "features": [
                            "AirConditioning",
                            "BuiltInWardrobes",
                            "Floorboards",
                            "SecureParking",
                            "CityViews",
                            "Bath",
                        ],
                        "bathrooms": 2.0,
                        "bedrooms": 3.0,
                        "carspaces": 1,
                    },
                },
                "travel_details": {"distance": "6.88km", "travel_time": "24.0mins"},
                "nbn": "FTTC",
                "walkscore": {
                    "walkscore": 94,
                    "summary": "Walker's Paradise",
                    "transit": {
                        "score": 76,
                        "description": "Excellent Transit",
                        "summary": "30 nearby routes: 19 bus, 11 rail, 0 other",
                    },
                },
            },
        ),
        (
            sample_two,
            {
                "listing": {
                    "id": None,
                    "listing_slug": "",
                    "price": "",
                    "address": {
                        "displayable_address": "",
                        "postcode": "",
                        "state": "",
                    },
                    "property_details": {
                        "property_type": "",
                        "features": [],
                        "bathrooms": None,
                        "bedrooms": None,
                        "carspaces": None,
                    },
                },
                "travel_details": {"distance": "3.96km", "travel_time": "12.58mins"},
                "nbn": "FTTB",
                "walkscore": {
                    "walkscore": 85,
                    "summary": "Very Walkable",
                    "transit": {
                        "score": 70,
                        "description": "Excellent Transit",
                        "summary": "9 nearby routes: 3 bus, 6 rail, 0 other",
                    },
                },
            },
        ),
        (
            sample_three,
            {
                "listing": {
                    "id": 2016113445,
                    "listing_slug": "2a-oscar-street-seddon-vic-3011-2016113445",
                    "price": "Private Sale $679,000",
                    "address": {
                        "displayable_address": "2A Oscar Street, Seddon",
                        "postcode": "3011",
                        "state": "VIC",
                    },
                    "property_details": {
                        "property_type": "Townhouse",
                        "features": [
                            "AirConditioning",
                            "BuiltInWardrobes",
                            "Gas",
                            "Dishwasher",
                        ],
                        "bathrooms": 2.0,
                        "bedrooms": 3.0,
                        "carspaces": 1,
                    },
                },
                "travel_details": {"distance": "8.04km", "travel_time": "27.72mins"},
                "nbn": None,
                "walkscore": {
                    "walkscore": 77,
                    "summary": "Very Walkable",
                    "transit": {},
                },
            },
        ),
    ],
)
def test_clean_response(sample_search_result: dict, expected: dict) -> None:
    """Tests the response parser.

    Args:
        sample_search_result (dict): Sample SmartSearch result
        expected (dict): Expected output
    """
    assert clean_response(sample_search_result) == expected


@pytest.mark.parametrize(
    "input_listing, expected",
    [
        (
            sample_one["listing"],
            {
                "id": 2016359058,
                "listing_slug": "footscray-vic-3011-2016359058",
                "price": "Contact agent",
                "address": {
                    "displayable_address": "Footscray",
                    "postcode": "3011",
                    "state": "VIC",
                },
                "property_details": {
                    "property_type": "ApartmentUnitFlat",
                    "features": [
                        "AirConditioning",
                        "BuiltInWardrobes",
                        "Floorboards",
                        "SecureParking",
                        "CityViews",
                        "Bath",
                    ],
                    "bathrooms": 2.0,
                    "bedrooms": 3.0,
                    "carspaces": 1,
                },
            },
        ),
        (
            sample_two["listing"],
            {
                "id": None,
                "listing_slug": "",
                "price": "",
                "address": {"displayable_address": "", "postcode": "", "state": "",},
                "property_details": {
                    "property_type": "",
                    "features": [],
                    "bathrooms": None,
                    "bedrooms": None,
                    "carspaces": None,
                },
            },
        ),
        (
            sample_three["listing"],
            {
                "id": 2016113445,
                "listing_slug": "2a-oscar-street-seddon-vic-3011-2016113445",
                "price": "Private Sale $679,000",
                "address": {
                    "displayable_address": "2A Oscar Street, Seddon",
                    "postcode": "3011",
                    "state": "VIC",
                },
                "property_details": {
                    "property_type": "Townhouse",
                    "features": [
                        "AirConditioning",
                        "BuiltInWardrobes",
                        "Gas",
                        "Dishwasher",
                    ],
                    "bathrooms": 2.0,
                    "bedrooms": 3.0,
                    "carspaces": 1,
                },
            },
        ),
    ],
)
def test_clean_domain(input_listing: dict, expected: dict) -> None:
    """Tests domain listing parsing & cleaning.

    Args:
        input_listing (dict): Sample domain listing
        expected (dict): Expected output
    """
    assert clean_domain(input_listing) == expected


@pytest.mark.parametrize(
    "input_travel_details, expected",
    [
        (
            {"distance": 1000, "duration": 600},
            {"distance": "1.0km", "travel_time": "10.0mins"},
        ),
        (
            {"distance": 700, "duration": 400},
            {"distance": "0.7km", "travel_time": "6.67mins"},
        ),
        (
            {"distance": 2358, "duration": 1340},
            {"distance": "2.36km", "travel_time": "22.33mins"},
        ),
        (
            {"distance": "No Result", "duration": "No Result"},
            {"distance": "No Result", "travel_time": "No Result"},
        ),
        ({}, {"distance": "No Result", "travel_time": "No Result"},),
    ],
)
def test_clean_travel_info(input_travel_details: dict, expected: dict) -> None:
    """Tests travel info parsing & cleaning.

    Args:
        input_travel_details (dict): Sample travel details
        expected (dict): Expected output
    """
    assert clean_travel_info(input_travel_details) == expected


@pytest.mark.parametrize(
    "input_walkscore, expected",
    [
        (
            sample_one["walkscore"],
            {
                "walkscore": 94,
                "summary": "Walker's Paradise",
                "transit": {
                    "score": 76,
                    "description": "Excellent Transit",
                    "summary": "30 nearby routes: 19 bus, 11 rail, 0 other",
                },
            },
        ),
        (
            sample_two["walkscore"],
            {
                "walkscore": 85,
                "summary": "Very Walkable",
                "transit": {
                    "score": 70,
                    "description": "Excellent Transit",
                    "summary": "9 nearby routes: 3 bus, 6 rail, 0 other",
                },
            },
        ),
        (
            sample_three["walkscore"],
            {"walkscore": 77, "summary": "Very Walkable", "transit": {}},
        ),
        ({}, {"walkscore": None, "summary": "", "transit": {}},),
    ],
)
def test_walkscore(input_walkscore: dict, expected: dict) -> None:
    """Tests walkscore parsing & cleaning.

    Args:
        input_walkscore (dict): Sample walkscore details
        expected (dict): Expected output
    """
    assert clean_walkscore(input_walkscore) == expected
