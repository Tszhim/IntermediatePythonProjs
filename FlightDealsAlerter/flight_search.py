from pprint import pprint

import requests

from flight_data import FlightData

class FlightSearch:
    
    # Instantiating information necessary to make Tequila API call.
    def __init__(self):
        self.data_retrieval_endpoint = "https://tequila-api.kiwi.com/"
        self.authentication = {
            "apikey": "myAPIkey"
        }
    
    # Returns IATA code corresponding to a city.
    def get_iatacode(self, city):
        iatacode_endpoint = self.data_retrieval_endpoint + "locations/query"
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=iatacode_endpoint, headers=self.authentication, params=params)
        data = response.json()["locations"]
        return data[0]["code"]
    
    # Returns great flight deals, if any.
    def check_flight_deals(self, origin_iataCode, destination_iataCode, interval_start, interval_end):
        params = {
            "fly_from": origin_iataCode,
            "fly_to": destination_iataCode,
            "date_from": interval_start,
            "date_to": interval_end,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        try:
            response = requests.get(url=self.data_retrieval_endpoint + "v2/search", headers=self.authentication, params=params)
            print(response.status_code)
            pprint(response.json())
            data = response.json()["data"][0]
            return FlightData(data)
        except IndexError:
            return None





