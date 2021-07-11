import requests

from dates import Dates


class AVData:

    # Setting default values and preparing to retrieve data.
    def __init__(self, stock_symbols):
        self.av_api_key = "your Alpha Vintage API key"
        self.av_function = "TIME_SERIES_INTRADAY"
        self.av_interval = "60min"
        self.dates = Dates()
        self.stock_symbols = stock_symbols
        self.percentages = []
        self.data_retrieval()

    # Retrieving data from Alpha Vantage API.
    def data_retrieval(self):
        # Making API calls for each stock symbol to obtain percent changes in the last two days.
        for stock_symbol in self.stock_symbols:
            av_call_params = {
                "function": self.av_function,
                "symbol": stock_symbol,
                "interval": self.av_interval,
                "apikey": self.av_api_key
            }
            av_api_call = requests.get(url="https://www.alphavantage.co/query", params=av_call_params)
            av_api_call.raise_for_status()
            stock_data = av_api_call.json()

            # Isolating relevant data.
            close_last_business_day = float(
                stock_data["Time Series (60min)"][str(self.dates.last_business_day) + " 20:00:00"].get("4. close"))
            open_second_last_business_day = float(
                stock_data["Time Series (60min)"][str(self.dates.second_last_business_day) + " 05:00:00"].get(
                    "1. open"))

            # Calling calculate_changes() to analyze results.
            self.calculate_changes(close_last_business_day, open_second_last_business_day)

    # Calculating percent changes in stock prices, then storing them.
    def calculate_changes(self, close_last, open_second):
        self.percentages.append(round(((close_last - open_second) / open_second * 100), 2))
