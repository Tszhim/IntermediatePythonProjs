from datetime import datetime, timedelta

from flight_search import FlightSearch
from sheety_data_storage import SheetyDataStorage
from twilio_sms_manager import TwilioSMSManager

# Setting up relevant components.
data_storage = SheetyDataStorage()
sheet_data = data_storage.data
flight_search = FlightSearch()
twilio_sms_manager = TwilioSMSManager()

# Filling IATA codes if necessary.
if not data_storage.iatacodes_filled():
    cities = data_storage.get_cities()

    for entry in sheet_data:
        entry["iataCode"] = flight_search.get_iatacode(entry["city"])

    data_storage.data = sheet_data
    data_storage.update_data()

# Checking for flight deals.
for destination in sheet_data:
    interval_start = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    interval_end = (datetime.now() + timedelta(days=365)).strftime("%d/%m/%Y")
    flight_deals = flight_search.check_flight_deals("JFK", destination["iataCode"], interval_start=interval_start, interval_end=interval_end)

    if flight_deals is not None and flight_deals.parse_price() < destination["lowestPrice"]:
        twilio_sms_manager.notify(flight_deals.compose_msg())









