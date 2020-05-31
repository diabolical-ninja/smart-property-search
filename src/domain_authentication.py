"""
Helper function to generate authentication token for the Domain Client
"""

import requests


def GetAccessTokenJson(client_id: str, secret: str, scopes: list):

    oauth_url = "https://auth.domain.com.au/v1/connect/token"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Request for all scopes
    payload = {
        'grant_type': 'client_credentials',
        'scope': ' '.join(scopes)
    }

    try:
        response = requests.post(url = oauth_url,
                                 headers = headers,
                                 data = payload,
                                 auth = (client_id, secret))

        return response.json()

    except Exception as ex:
        raise Exception(ex)
