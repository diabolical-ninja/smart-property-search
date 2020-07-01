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


def search(event, context):

    data = json.loads(event['body'])

    listings = ListingsApi(ApiClient(configuration))
    results = listings.listings_detailed_residential_search(data)
    results = [result.to_dict() for result in results]

    response = {
        "statusCode": 200,
        "body": json.dumps(results, default = json_serial)
    }

    return response
