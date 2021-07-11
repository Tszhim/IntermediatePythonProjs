class FlightData:
    
    # Stores JSON object retrieved from Tequila API.
    def __init__(self, data):
        self.data = data
    
    # Parsing price from JSON object.
    def parse_price(self):
        return self.data["price"]
    
    # Parsing origin location from JSON object.
    def parse_origin_location(self):
        return self.data["route"][0]["cityFrom"]
    
    # Parsing origin IATA code from JSON object.
    def parse_origin_iataCode(self):
        return self.data["route"][0]["flyFrom"]
    
    # Parsing destinatino location from JSON object.
    def parse_destination_location(self):
        return self.data["route"][0]["cityTo"]
    
    # Parsing destination IATA code from JSON object.
    def parse_destination_iataCode(self):
        return self.data["route"][0]["flyTo"]
    
    # Parsing depature date from JSON object.
    def parse_departure(self):
        return self.data["route"][0]["local_departure"].split("T")[0]
    
    # Parsing return date from JSON object
    def parse_return(self):
        return self.data["route"][1]["local_departure"].split("T")[0]
  
    # Returns message to send user informing them of a great deal.
    def compose_msg(self):
        return "Great flight deal!\n$" + str(self.parse_price()) + " to fly from " + self.parse_origin_location() \
               + " (" + self.parse_origin_iataCode() + ") " + "to " + self.parse_destination_location() \
               + " (" + self.parse_destination_iataCode() + "), from " + self.parse_departure() + " to " + self.parse_return() \
               + "."
