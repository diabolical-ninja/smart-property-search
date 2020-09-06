"""Entry point for API."""

import json
import os

from smart_search import SmartSearch

from utils import json_serial


# Instantiate searcher
scopes = ["api_listings_read", "api_agencies_read"]
searcher = SmartSearch(
    domain_client_id=os.getenv("CLIENT_ID"),
    domain_client_secret=os.getenv("CLIENT_SECRET"),
    domain_scopes=scopes,
    google_maps_key=os.getenv("GOOGLE_MAPS_KEY"),
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
        # Extract POST body information
        data = json.loads(event["body"])
        domain_request = data["domain"]
        smart_filters = data["filters"]

        # Retrieve initial search results
        searcher.listings_search(domain_request)

        # Filter by travel time
        if "travelTime" in smart_filters:
            searcher.filter_by_travel_time(
                max_travel_time=smart_filters["travelTime"]["maxTravelTime"],
                destination=smart_filters["travelTime"]["destinationAddress"],
            )

        # Filter by desired features
        if "features" in smart_filters and len(smart_filters["features"]) > 0:
            searcher.filter_by_attribute(smart_filters["features"])

        # Filter by NBN requirements
        if "nbn" in smart_filters:
            searcher.filter_nbn(smart_filters["nbn"])

        response = {
            "statusCode": 200,
            "body": json.dumps(searcher.search_results, default=json_serial),
        }

        return response

    except Exception as ex:

        print(ex)

        response = {"statusCode": 200, "error": json.dumps(str(ex))}

        return response
