"""Client for the unofficial NBN API."""

from requests import get


class NBN:
    """Interacts with NBN's unofficial API."""
    def __init__(self):
        """Sets base values required for API calls."""
        self.base_url = "https://places.nbnco.net.au/places"
        self.headers = {
            "Referer": "https://www2.nbnco.com.au/residential/learn/rollout-map"
        }

    def get_location_ids_from_lat_long(self, latitude: float, longitude: float) -> dict:
        """Returns NBN location ID's present near the lat & long combination.

        Location ID looks like LOC000000000000

        Args:
            latitude (float): Address latitude
            longitude (float): Address longitude

        Returns:
            dict: Locations & their ID's for addresses near the lat/long pairs
        """
        url = f"{self.base_url}/v1/nearby"

        params = {"lat": latitude, "lng": longitude, "source": "website_rollout_map"}

        response = get(url=url, params=params, headers=self.headers)

        return response.json()

    def location_information(self, location_id: str) -> dict:
        """Get connection type & details for given location.

        Args:
            location_id (str): NBN Location ID

        Returns:
            dict: Information regarding the connection details & type
        """
        url = f"{self.base_url}/v2/details/{location_id}"

        params = {"source": "website_rollout_map"}

        response = get(url=url, params=params, headers=self.headers)

        return response.json()

    def get_location_ids_from_address(self, address: str) -> dict:
        """Returns NBN location ID's present near the given address.

        Location ID looks like LOC000000000000

        Args:
            address (str): Location address

        Returns:
            dict: Locations & their ID's the address
        """
        try:
            url = f"{self.base_url}/v1/autocomplete"

            params = {"query": address}

            response = get(url=url, params=params, headers=self.headers)
            print("## get_location_ids_from_address")
            print(response.status_code)
            print(response.text)
            print(response.content)

            return response.json()
        except Exception as ex:
            print(ex)
            raise
