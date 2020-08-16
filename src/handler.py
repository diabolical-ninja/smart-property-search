import json
from smart_search import SmartSearch
from utils import json_serial
import os


# Instantiate searcher
scopes = ['api_listings_read', 'api_agencies_read']
searcher = SmartSearch(domain_client_id = os.getenv('CLIENT_ID'),
                       domain_client_secret = os.getenv('CLIENT_SECRET'),
                       domain_scopes = scopes,
                       google_maps_key = os.getenv('GOOGLE_MAPS_KEY')
                       )


def search(event, context):

    try:
        # Extract POST body information
        data = json.loads(event['body'])
        domain_request = data['domain']
        smart_filters = data['filters']

        # Retrieve initial search results
        searcher.listings_search(domain_request)

        # Append results with travel information
        # southern_cross = (-37.818294, 144.952447)
        # searcher.calculate_travel_time(destination=southern_cross)

        response = {
            "statusCode": 200,
            "body": json.dumps(searcher.search_results, default = json_serial)
        }

        return response

    except Exception as ex:

        print(ex)

        response = {
            "statusCode": 200,
            "error": json.dumps(str(ex))
        }

        return response
