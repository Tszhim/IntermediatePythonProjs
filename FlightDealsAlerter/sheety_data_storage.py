import requests

class SheetyDataStorage:
    
    # Instantiating relevant information to make Sheety API call.
    def __init__(self):
        self.data_retrieval_endpoint = "https://api.sheety.co/82649be7cc4c862e8680a24eeb81e5d9/flightDeals/flights"
        self.data_add_endpoint = "https://api.sheety.co/82649be7cc4c862e8680a24eeb81e5d9/flightDeals/flights"
        self.authentication = {
            "Authorization": "Bearer " + "apiKey"
        }
        self.data = None
        self.retrieve_data()
    
    # Returns data stored in spreadsheet as JSON object.
    def retrieve_data(self):
        response = requests.get(self.data_retrieval_endpoint, headers=self.authentication)
        data = response.json()
        self.data = data["flights"]
    
    # Updates data in spreadsheet.
    def update_data(self):
        for destination in self.data:
            updated_data = {
                "flights": {
                    "iataCode": destination["iataCode"]
                }
            }
            requests.put(url=self.data_retrieval_endpoint + "/" + str(destination["id"]), headers=self.authentication, json=updated_data)
    
    # Returns list of cities in spreadsheet.
    def get_cities(self):
        cities = []
        for destination in self.data:
            cities.append(destination["city"])
        return cities
    
    # Checks if IATA codes are filled in the spreadsheet.
    def iatacodes_filled(self):
        for destination in self.data:
            if destination["iataCode"] == "":
                return False
        return True

