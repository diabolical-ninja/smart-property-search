"""Unofficial client for the Walkscore API."""

import logging

from requests import get


class WalkScore:
    """Interacts with the WalkScore API."""

    def __init__(self, api_key: str):
        """Sets base values required for API calls.

        Args:
            api_key (str): Your Walk Score API Key
        """
        self.LOGGER = logging.getLogger("standard")
        self.walkscore_base_url = "https://api.walkscore.com/score"
        self.api_key = api_key

    def get_score(
        self,
        latitude: float,
        longitude: float,
        address: str,
        transit: int = 1,
        bike: int = 1,
    ) -> dict:
        """ Gets the Walk, Transit and Bike Score for the requested location.

        API Details: https://www.walkscore.com/professional/api.php

        Args:
            latitude (float): The latitude of the requested location
            longitude (float): The longitude of the requested location
            address (str): The address
            transit (int, optional): Set 1 to request Transit Score.
                    - Defaults to 1
                    - Allowable values are 0 or 1
            bike (int, optional): Set to 1 to request Bike Score.
                    - Defaults to 1
                    - Allowable values are 0 or 1

        Raises:
            Exception: General message of the error generated

        Returns:
            dict: Walkscore information
                    - status: Status code of the result (see information below).
                    - walkscore: The Walk Score of the location.
                    - description: An English description of the Walk Score. E.G. Somewhat Walkable.
                    - updated: When the Walk Score was calculated.
                    - logo_url: Link to the Walk Score logo.
                    - more_info_icon: Link to question mark icon to display next to the score.
                    - more_info_link: URL for the question mark to link to.
                    - ws_link: A link to the walkscore.com score and map for the point.
                    - help_link: A link to the "How Walk Score Works" page.
                    - snapped_lat: All points are "snapped" to a grid (roughly 500 feet wide per grid cell). This value is the snapped latitude for the point.  # noqa
                    - snapped_lon: The snapped longitude for the point.
        """
        params = {
            "format": "json",
            "address": address,
            "wsapikey": self.api_key,
            "lat": latitude,
            "lon": longitude,
            "transit": transit,
            "bike": bike,
        }

        response = get(url=self.walkscore_base_url, params=params)

        if response.status_code == 200:
            if response.json()["status"] == 1:
                return response.json()
            else:
                log_items = {
                    "message": "Invalid walkscore parameters passed",
                    "params": params,
                    "request_info": response.__dict__,
                }
                self.LOGGER.error(log_items)
                raise Exception(log_items["message"])
        else:
            log_items = {
                "message": "Unable to query walkscore API",
                "params": params,
                "request_info": response.__dict__,
            }
            self.LOGGER.error(log_items)
            raise Exception(log_items["message"])
