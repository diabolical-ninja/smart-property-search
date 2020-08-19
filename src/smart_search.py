from googlemaps import Client
from domain_listings import DomainListings
import datetime
import pytz
from utils import chunks, extend_dictionary


class SmartSearch(DomainListings, Client):

    def __init__(self,
                 domain_client_id,
                 domain_client_secret,
                 domain_scopes,
                 google_maps_key
                 ):

        DomainListings.__init__(self, domain_client_id, domain_client_secret, domain_scopes)
        Client.__init__(self, key = google_maps_key)

    def listings_search(self, search_parameters):
        results = self.retrieve_residential_search_listings(search_parameters)
        # Results with None listing are projects & for now these can be excluded
        # Likely a better way to handle this though
        self.search_results = [x for x in results if x['listing'] is not None]

    def filter_by_travel_time(self, max_travel_time, destination):

        # Convert to seconds
        max_travel_time_sec = max_travel_time * 60

        # Filter
        self.calculate_travel_time(destination = destination)
        self.search_results = [x for x in self.search_results if
                               self.__travel_time_less_than_threshold(
                                   x['travel_info']['duration'], max_travel_time_sec)
                               ]

    @staticmethod
    def __travel_time_less_than_threshold(travel_time, max_travel_time):

        output = False
        if travel_time != 'No Result':
            if travel_time <= max_travel_time:
                output = True

        return output

    def calculate_travel_time(self, destination):

        # Extract location lat/long for each returned property
        results_lat_long = [(x['listing']['property_details']['latitude'],
                             x['listing']['property_details']['longitude']) for x
                            in self.search_results]

        # Get the travel time for each search result & append (distance, duration)
        distances = self.get_distances(results_lat_long, destination)
        self.search_results = [extend_dictionary(x[0], x[1], 'travel_info') for x
                               in zip(self.search_results, distances)]

    def get_distances(self, origins, destination, chunk_size=50):

        # Create next Tuesday
        # Why Tuesday? Less likely to be a long weekend me thinks?
        target_arrival_time = self.__create_next_day(2).timestamp()

        # Get travel information
        distances = []
        for origin_set in chunks(origins, chunk_size):

            # Query google to get travel time & distance
            matrix = self.distance_matrix(origin_set,
                                          destination,
                                          mode = 'transit',
                                          transit_mode = 'rail',
                                          transit_routing_preference = 'fewer_transfers',
                                          arrival_time = target_arrival_time)

            # Extract Duration & Distance
            distances.extend([self.__extract_distance_duration(x['elements'][0])
                              for x in matrix['rows']])

        return distances

    @staticmethod
    def __create_next_day(target_day_of_week, target_hour=9, target_minute=0, timezone="Australia/Melbourne"):

        # Create Next Date
        day = datetime.date.today()
        diff = target_day_of_week + 7 - day.isoweekday()

        # Create Datetime
        tz = pytz.timezone(timezone)
        constructed_datetime = datetime.datetime.combine(day + datetime.timedelta(diff),
                                                         datetime.time(target_hour, target_minute))

        return tz.localize(constructed_datetime)

    @staticmethod
    def __extract_distance_duration(result):
        """
        Distance: Metres
        Duration: Seconds
        """

        try:
            return {
                'distance': result['distance']['value'],
                'duration': result['duration']['value']
            }
        except Exception:
            return {
                'distance': 'No Result',
                'duration': 'No Result'
            }
