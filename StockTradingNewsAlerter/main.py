from av_data_extract import AVData
from news_data_extract import NewsData
from sms_generator import SMSGenerator
from sms_sender import SMSSender

# Stock symbols to notify about.
stock_symbols = ["TSLA", "AAPL", "FB"]

# Alpha Vantage API data retrieval. 
av_data = AVData(stock_symbols)
stock_changes = av_data.percentages

# NewsAPI data retrieval.
news_data = NewsData(stock_symbols)
article_headings = news_data.headlines
article_briefings = news_data.briefings

# Generate SMS with information to send.
sms_generator = SMSGenerator(stock_symbols, stock_changes, article_headings, article_briefings)

# If SMS message is not empty, send.
if sms_generator.completed_text != "":
    sms_sender = SMSSender(sms_generator.completed_text)
