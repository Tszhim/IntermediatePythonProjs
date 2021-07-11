# StockTradingNewsAlerter

This Python program alerts users with an SMS text message whenever the stocks they are tracking increases or decreases by 3% or greater in the past two business days.
The SMS text messages includes the ticker symbol, percentage change, and the top three relevant article headlines with a short description to assist the user in understanding stock price changes.

Note that personal information must provided in the following files:

main.py: stock_symbols

av_data_extract.py: av_api_key

news_data_extract.py: news_api_key

SMSsender.py: twilio_sid, auth_token, sender, receiver

The av_api_key can be created at https://www.alphavantage.co/support/#api-key.

The news_api_key can be created at https://newsapi.org/.

The twilio_sid, auth_token, and sender phone number can be created at https://www.twilio.com/.
