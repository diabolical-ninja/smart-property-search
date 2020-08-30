"""Main class for searching & filtering functionality."""

import datetime
from itertools import compress

from domain_listings import DomainListings

from googlemaps import Client

import pytz

from utils import chunks, extend_dictionary

from yaml import safe_load


class SmartSearch(DomainListings, Client):
    """Main class for searching & filtering functionality.

    Args:
        DomainListings (DomainListings): DomainListings search object
        Client (Client): Google maps Client
    """

    def __init__(
        self,
        domain_client_id: str,
        domain_client_secret: str,
        domain_scopes: list,
        google_maps_key: str,
    ):
        """Instantiates base classes

        Args:
            domain_client_id (str): Your client ID
            domain_client_secret (str): Your client secret
            domain_scopes (list): Desired scope(s) to provide authentication for
                                  Required scopes provided in: https://developer.domain.com.au/docs/apis   # noqa
            google_maps_key (str): API key for google maps
        """

        DomainListings.__init__(
            self, domain_client_id, domain_client_secret, domain_scopes
        )
        Client.__init__(self, key=google_maps_key)
        self.filter_parameters = safe_load(open("filter_parameters.yml"))

    def listings_search(self, search_parameters: dict) -> None:
        """Retrieves listings based on initial search parameters.

        Args:
            search_parameters (dict): Parameters as defined by Domain
                                        - https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialsearch  # noqa
        """
        results = self.retrieve_residential_search_listings(search_parameters)
        # Results with None listing are projects & for now these can be excluded
        # Likely a better way to handle this though
        self.search_results = [x for x in results if x["listing"] is not None]

    def filter_by_travel_time(self, max_travel_time: int, destination: str) -> None:
        """Filters properties based on max travel threshold.

        Args:
            max_travel_time (int): Max allowable travel time in minutes
            destination (str): Desination location
        """
        # Convert to seconds
        max_travel_time_sec = max_travel_time * 60

        # Filter
        self.calculate_travel_time(destination=destination)
        self.search_results = [
            x
            for x in self.search_results
            if self.__travel_time_less_than_threshold(
                x["travel_info"]["duration"], max_travel_time_sec
            )
        ]

    @staticmethod
    def __travel_time_less_than_threshold(
        travel_time: int, max_travel_time: int
    ) -> bool:

        output = False
        if travel_time != "No Result":
            if travel_time <= max_travel_time:
                output = True

        return output

    def calculate_travel_time(self, destination: str) -> None:
        """Calculates travel time for each property listing.

        Args:
            destination (str): Target destination
        """
        # Extract location lat/long for each returned property
        results_lat_long = [
            (
                x["listing"]["property_details"]["latitude"],
                x["listing"]["property_details"]["longitude"],
            )
            for x in self.search_results
        ]

        # Get the travel time for each search result & append (distance, duration)
        distances = self.get_distances(results_lat_long, destination)
        self.search_results = [
            extend_dictionary(x[0], x[1], "travel_info")
            for x in zip(self.search_results, distances)
        ]

    def get_distances(
        self, origins: list, destination: str, chunk_size: int = 50
    ) -> list:
        """Gets travel time & distance from Google.

        Args:
            origins (list): Lat & lot for property listings
            destination (str): Address for destination
            chunk_size (:obj: `int`, optional): How many origins to send at a time.
                                        Defaults to 50.

        Returns:
            list: All properties & their travel time to the destination
        """
        # Create next Tuesday
        # Why Tuesday? Less likely to be a long weekend me thinks?
        target_arrival_time = self.__create_next_day(2).timestamp()

        # Get travel information
        distances = []
        for origin_set in chunks(origins, chunk_size):

            # Query google to get travel time & distance
            matrix = self.distance_matrix(
                origin_set,
                destination,
                mode="transit",
                transit_mode="rail",
                transit_routing_preference="fewer_transfers",
                arrival_time=target_arrival_time,
            )

            # Extract Duration & Distance
            distances.extend(
                [
                    self.__extract_distance_duration(x["elements"][0])
                    for x in matrix["rows"]
                ]
            )

        return distances

    @staticmethod
    def __create_next_day(
        target_day_of_week: int,
        target_hour: int = 9,
        target_minute: int = 0,
        timezone: str = "Australia/Melbourne",
    ) -> datetime.datetime:
        """Creates the datetime corresponding to the next day of interest, relative to today.

        Eg, today is Tuesday, ask for the next wednesday & the date for tomorrow is returned

        Args:
            target_day_of_week (int): Target day of week where 1=Monday & 7=Sunday
            target_hour (int, optional): Target hour of the day.
                                         Defaults to 9.
            target_minute (int, optional): Target minute of the hour.
                                           Defaults to 0.
            timezone (str, optional): Target timezone.
                                      Defaults to "Australia/Melbourne".

        Returns:
            datetime: The timestamp corresponding to the requested day
        """
        # Create Next Date
        day = datetime.date.today()
        diff = target_day_of_week + 7 - day.isoweekday()

        # Create Datetime
        tz = pytz.timezone(timezone)
        constructed_datetime = datetime.datetime.combine(
            day + datetime.timedelta(diff), datetime.time(target_hour, target_minute)
        )

        return tz.localize(constructed_datetime)

    @staticmethod
    def __extract_distance_duration(result: dict) -> dict:
        """Extract distance & duration from gmaps distance object.

        Args:
            result (dict): Resulting distance object from gmaps search

        Returns:
            dict: Containing travel time & distance, noting:
                    - Distance: Metres
                    - Duration: Seconds
        """
        try:
            return {
                "distance": result["distance"]["value"],
                "duration": result["duration"]["value"],
            }
        except Exception:
            return {"distance": "No Result", "duration": "No Result"}

    def filter_by_attribute(self, wanted_attributes: list) -> None:
        """Filter listings based off desired attributes.

        Args:
            wanted_attributes (list): Key for each attribute search
        """
        satisfies_search = list()

        # For each property, get detailed listing, filter & return true/false
        for result in self.search_results:

            # Get detailed listing
            detailed_listing = self.single_detailed_listing(result["listing"]["id"])

            # Run through search filter
            satisfies_search.append(
                all(
                    self.has_feature(
                        search_features=self.filter_parameters["features"][feature][
                            "domain"
                        ],
                        feature_search_words=self.filter_parameters["features"][
                            feature
                        ]["desc"],
                        property_details_features=result["listing"]["property_details"][
                            "features"
                        ],
                        property_description=detailed_listing["description"],
                    )
                    for feature in self.filter_parameters["features"]
                    if feature in wanted_attributes
                )
            )

        # Apply filter
        self.search_results = list(compress(self.search_results, satisfies_search))

    @staticmethod
    def has_feature(
        search_features: list,
        feature_search_words: list,
        property_details_features: list,
        property_description: str
    ) -> bool:
        """Determines whether a feature is present in a listing.

        Checking is niave ATM where by it checks for one of:
            - Does the listing have that attribute tagged
            - Do any of the keywords exist in the description

        Args:
            search_features (list): Desired features as tagged in the listing "propertyFeatures".
            feature_search_words (list): Feature terms to search for in the description.
            property_details_features (list): The listings "propertyFeatures".
            property_description (str): The listings description.

        Returns:
            bool: Flag indicating if the feature is present
        """
        attribute_in_features = any(
            feature in property_details_features for feature in search_features
        )

        # Test if attribute listed elsewhere
        attribute_in_description = any(
            val in property_description.lower() for val in feature_search_words
        )

        if attribute_in_features or attribute_in_description:
            return True
        else:
            return False
