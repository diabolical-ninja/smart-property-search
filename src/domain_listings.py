"""Wrapper class to authenticate & access listings methods."""

import logging

import requests

from domainClient import ApiClient, Configuration, ListingsApi  # noqa


class DomainListings:
    """Wrapper class to authenticate & access listings methods."""
    def __init__(self, client_id: str, client_secret: str, scopes: list):
        """Initialises & generates access token.

        Args:
            client_id (str): Your client ID
            client_secret (str): Your client secret
            scopes (list): Desired scope(s) to provide authentication for
                           Required scopes provided in: https://developer.domain.com.au/docs/apis
        """
        self.LOGGER = logging.getLogger("standard")
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.auth_info = self.get_access_token()
        self.listings = self.create_listings_client()

    def get_access_token(self) -> dict:
        """Generate access token via the OAUTH2 grant method
        Reference: https://developer.domain.com.au/docs/authentication/oauth/client-credentials-grant   # noqa

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
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # Request for all scopes
        payload = {"grant_type": "client_credentials", "scope": " ".join(self.scopes)}

        try:
            response = requests.post(
                url=oauth_url,
                headers=headers,
                data=payload,
                auth=(self.client_id, self.client_secret),
            )

            self.LOGGER.debug(response.__dict__)
            return response.json()

        except Exception as ex:
            self.LOGGER.error(ex)
            raise Exception(ex)

    def create_listings_client(self) -> ListingsApi:
        """Instantiates Listings Object.

        Returns:
            ListingsApi: Instantiated & authenticated object
        """
        # Configure Authentication Client
        configuration = Configuration()
        configuration.access_token = self.auth_info["access_token"]
        return ListingsApi(ApiClient(configuration))

    def single_detailed_listing(self, listing_id: int) -> dict:
        """Retrieval of detailed information for a single property.

        Args:
            listing_id (int): Property ID

        Returns:
            dict: Detailed property listing information
        """
        return self.listings.listings_get(listing_id).to_dict()

    def retrieve_residential_search_listings(self, data: dict) -> list:
        """Iterative retrieval of property listings based on search criteria.

        Args:
            data (dict): Search criteria for domain, based on:
                         https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialsearch   # noqa

        Returns:
            list: Returned properties from search
        """        
        # As per docs, search results are limited to the first 1000 results.
        # Max results per search = 1000
        max_results = 1000

        # Initialise parameters for the search
        data["pageNumber"], data["pageSize"] = 1, 200
        results = []
        response_length = 1

        while (data["pageNumber"] * data["pageSize"] <= max_results) and (
            response_length != 0
        ):

            response = self.listings.listings_detailed_residential_search(data)
            results.extend(response)

            # Capture progress to determine whether or not to continue
            response_length = len(response)
            data["pageNumber"] += 1

        results = [result.to_dict() for result in results]
        return results
