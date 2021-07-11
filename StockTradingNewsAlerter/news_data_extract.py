import requests

from dates import Dates


class NewsData:

    # Setting default values and preparing to retrieve data.
    def __init__(self, stock_symbols):
        self.news_api_key = "your NewsAPI key"
        self.news_sort = "popularity"
        self.stock_symbols = stock_symbols
        self.dates = Dates()
        self.top_articles = []
        self.headlines = []
        self.briefings = []
        self.data_retrieval()

    # Retrieving data from NewsAPI.
    def data_retrieval(self):

        # Making API call for each stock symbol to obtain popular news for stocks.
        for stock_symbol in self.stock_symbols:
            news_call_params = {
                "q": stock_symbol,
                "from": str(self.dates.second_last_business_day),
                "to": str(self.dates.last_business_day),
                "sortBy": self.news_sort,
                "apiKey": self.news_api_key
            }
            news_api_call = requests.get(url="https://newsapi.org/v2/everything", params=news_call_params)
            news_api_call.raise_for_status()
            news_data = news_api_call.json()

            # Getting top three relevant news articles.
            self.top_articles.append(news_data["articles"][:3])

        # Calling data_isolation to further narrow results.
        self.data_isolation()

    # Storing the titles and descriptions of each article.
    def data_isolation(self):
        for articles in self.top_articles:
            for article in articles:
                self.headlines.append(article.get("title"))
                self.briefings.append(article.get("description"))
