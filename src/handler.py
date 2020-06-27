import json
from domainClient import Configuration, ListingsApi, ApiClient
from domain_authentication import get_access_token
from utils import json_serial
import os


# Generate Access Token
scopes = ['api_listings_read', 'api_agencies_read']
auth_info = get_access_token(os.getenv('CLIENT_ID'),
                             os.getenv('CLIENT_SECRET'),
                             scopes)

# Configure Authentication Client
configuration = Configuration()
configuration.access_token = auth_info['access_token']

search_parameters = {}
search_parameters['listing_type'] = 'Sale'
search_parameters['minBedrooms'] = 2
search_parameters['maxBedrooms'] = 4
search_parameters['minBathrooms'] = 1
search_parameters['maxBathrooms'] = 4
search_parameters['minCarspaces'] = 1
search_parameters['maxCarspaces'] = 4
search_parameters['minPrice'] = 500000
search_parameters['maxPrice'] = 5500000
locations_list = [{
    "state": "VIC"
}]

search_parameters['pageSize'] = 200
search_parameters['locations'] = locations_list


def search(event, context):

    listings = ListingsApi(ApiClient(configuration))
    results = listings.listings_detailed_residential_search(search_parameters)
    results = [result.to_dict() for result in results]

    response = {
        "statusCode": 200,
        "body": json.dumps(results, default = json_serial)
    }

    return response
