"""Unit tests for src/domain_listings.py."""

import os
import sys

sys.path.append(os.path.join(os.getcwd(), "src"))

from domain_listings import DomainListings  # noqa

from domainClient import ListingsApi  # noqa


class TestDomainListings:
    """Tests the DomainListings class."""

    def setup_class(self) -> None:
        """Create an instance to test against."""
        scopes = ["api_listings_read", "api_agencies_read"]
        self.domain_listings_object = DomainListings(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            scopes=scopes,
        )

    def test_create_listings_client(self) -> None:
        """Tests instantiation of domain listings object."""
        assert isinstance(
            self.domain_listings_object.create_listings_client(), ListingsApi
        )

    def test_single_detailed_listing(self) -> None:
        """Tests requesting information for a single listing.

        Utilisese the ID from Domain's docs:
        https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_get
        """
        response = self.domain_listings_object.single_detailed_listing(6311594)
        assert isinstance(response, dict)

    def test_retrieve_residential_search_listings(self) -> None:
        """Tests retrieval of many listings based on search criteria.

        Utilises the example from Domain's docs:
        https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialsearch
        """
        search_parameters = {
            "listingType": "Sale",
            "propertyTypes": ["House", "NewApartments"],
            "minBedrooms": 3,
            "minBathrooms": 2,
            "minCarspaces": 1,
            "locations": [
                {
                    "state": "NSW",
                    "region": "",
                    "area": "",
                    "suburb": "Newtown",
                    "postCode": "",
                    "includeSurroundingSuburbs": False,
                }
            ],
        }

        response = self.domain_listings_object.retrieve_residential_search_listings(
            search_parameters
        )
        assert isinstance(response, list)
        assert isinstance(response[0], dict)


class TestAccessToken:
    """Tests the access token functionality."""

    def setup_method(self) -> None:
        """For each test creat a new, clean instance to get against."""
        scopes = ["api_listings_read", "api_agencies_read"]
        self.domain_listings_object = DomainListings(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            scopes=scopes,
        )

    def test_get_access_token(self) -> None:
        """Test deneration of access token."""
        access_token = self.domain_listings_object.get_access_token()
        assert isinstance(access_token, dict)
        assert list(access_token.keys()) == ["access_token", "expires_in", "token_type"]

    def test_wrong_client_id(self) -> None:
        """Test access token generation with an client id."""
        self.domain_listings_object.client_id = "not a real client id"

        response = self.domain_listings_object.get_access_token()
        assert list(response.keys()) == ["error"]
        assert response["error"] == "invalid_client"

    def test_wrong_client_secret(self) -> None:
        """Test access token generation with an client secret."""
        self.domain_listings_object.client_id = "not a real client secret"

        response = self.domain_listings_object.get_access_token()
        assert list(response.keys()) == ["error"]
        assert response["error"] == "invalid_client"

    def test_wrong_scope(self) -> None:
        """Test access token generation with an incorrect scope."""
        self.domain_listings_object.scopes = "not a real scope"

        response = self.domain_listings_object.get_access_token()
        assert list(response.keys()) == ["error"]
        assert response["error"] == "invalid_scope"
