from googlemaps import Client
from domain_listings import DomainListings
from utils import *


class SmartSearch(DomainListings, Client):

    def __init__(self,
                 domain_client_id,
                 domain_client_secret,
                 domain_scopes,
                 google_maps_key
                 ):

        DomainListings.__init__(self, domain_client_id, domain_client_secret, domain_scopes)
        Client.__init__(self, key = google_maps_key)

    def listing_search(self, search_parameters):
        self.search_results = self.retrieve_residential_search_listings(search_parameters)

    def calculate_travel_time(self, destination, target_arrival_time=None):

        # Extract location lat/long for each returned property
        results_lat_long = [(x['listing']['property_details']['latitude'],
                             x['listing']['property_details']['longitude']) for x
                            in self.search_results]

        # Should be autodefined &/or an argument
        # Consider timezones for Adelaide, Perth, etc
        target_arrival_time = timestamp_to_epoch('2020-08-13T09:00:00', '+1100')

        # Get the travel time for each search result & append (distance, duration)
        distances = self.get_distances(results_lat_long, destination, target_arrival_time)
        self.search_results = [extend_dictionary(x[0], x[1], 'travel_info') for x
                               in zip(self.search_results, distances)]

    def get_distances(self, origins, destination, target_arrival_time, chunk_size=50):

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
            distances.extend([self.extract_distance_duration(x['elements'][0])
                              for x in matrix['rows']])

        return distances

    def extract_distance_duration(self, result):
        """
        Distance: Metres
        Duration: Seconds
        """

        return {
            'distance': result['distance']['value'],
            'duration': result['duration']['value']
        }
