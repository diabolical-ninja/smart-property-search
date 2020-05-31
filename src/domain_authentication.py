""" Helper function to generate authentication token for the Domain Client """

import requests


def get_access_token(client_id: str, secret: str, scopes: list):
    """Generate access token via the OAUTH2 grant method
    Reference: https://developer.domain.com.au/docs/authentication/oauth/client-credentials-grant

    Args:
        client_id (str): Your client ID
        secret (str): Your client secret
        scopes (list): Desired scope(s) to provide authentication for
                       Required scopes provided in: https://developer.domain.com.au/docs/apis

    Raises:
        Exception: Any issues present when attempting token generation

    Returns:
        dict: JSON result with access token containing:
                - access_token: Your token required for API interaction
                - expires_in: The lifetime in seconds of the token
                - token_type: Token type, in this case "bearer"
    """

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
