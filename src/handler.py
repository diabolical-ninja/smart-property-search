"""Entry point for API."""

import json
import os

from logging_setup import configure_logger

from smart_search import SmartSearch

from utils import json_serial

# Instantiate Logger as per config
LOGGER = configure_logger()


# Instantiate searcher
scopes = ["api_listings_read", "api_agencies_read"]
searcher = SmartSearch(
    domain_client_id=os.getenv("CLIENT_ID"),
    domain_client_secret=os.getenv("CLIENT_SECRET"),
    domain_scopes=scopes,
    google_maps_key=os.getenv("GOOGLE_MAPS_KEY"),
    walkscore_api_key=os.getenv("WSAPIKEY"),
)


def search(event: dict, context: object) -> dict:
    """Entry point function for the API to manage & handle requests.

    Args:
        event (dict): API request including gateway information
        context (object): Methods and properties that provide information about the invocation,
                          function, and execution environment

    Returns:
        dict: Filtered properties based on search criteria
    """
    try:
        # Capture request information
        LOGGER.debug(event)
        LOGGER.debug(context)

        # Extract POST body information
        LOGGER.info("Extract request body from API payload")
        data = json.loads(event["body"])
        domain_request = data["domain"]
        smart_filters = data.get("filters", {})

        # Retrieve initial search results
        LOGGER.info("Retrieve unfiltered search results")
        searcher.listings_search(domain_request)
        LOGGER.info("Retrieve unfiltered search results...Done")

        # Filter by travel time
        if "travelTime" in smart_filters:
            LOGGER.info("Filtering by travel time")
            searcher.filter_by_travel_time(
                max_travel_time=smart_filters["travelTime"]["maxTravelTime"],
                destination=smart_filters["travelTime"]["destinationAddress"],
            )
            LOGGER.info("Filtering by travel time...Done")

        # Filter by desired features
        if "features" in smart_filters and len(smart_filters["features"]) > 0:
            LOGGER.info("Filtering by smart features")
            searcher.filter_by_attribute(smart_filters["features"])
            LOGGER.info("Filtering by smart features...Done")

        # Filter by NBN requirements
        if "nbn" in smart_filters:
            LOGGER.info("Filtering by NBN requirements")
            searcher.filter_nbn(smart_filters["nbn"])
            LOGGER.info("Filtering by NBN requirements...Done")

        # Filter by walkscore
        if "walkscore" in smart_filters:
            LOGGER.info("Filtering by minimum walkscore")
            searcher.filter_walkscore(smart_filters["walkscore"])
            LOGGER.info("Filtering by minimum walkscore...Done")

        response = {
            "statusCode": 200,
            "body": json.dumps(searcher.search_results, default=json_serial)
        }

        return response

    except Exception as ex:

        LOGGER.error(ex, exc_info=True)

        response = {"statusCode": 500, "error": json.dumps(str(ex))}

        return response
