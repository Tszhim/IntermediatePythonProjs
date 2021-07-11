import requests
from bs4 import BeautifulSoup
import smtplib

# Preparing web scraping endpoint.
http_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept Language": "en-US,en;q=0.9"}
url = "https://www.amazon.com/OnePlus-Glacial-Unlocked-Android-Smartphone/dp/B08723759H/ref=sr_1_3?crid=3R3QY31603LS5&dchild=1&keywords=android+phone&qid=1626041888&sprefix=android%2Caps%2C211&sr=8-3"

# Making a request and obtaining raw data.
response = requests.get(url, headers=http_headers)
soup = BeautifulSoup(response.text, "html.parser")

# Parsing data from html.
item_name = soup.find(id="productTitle").get_text().strip()
item_price_spans = soup.find(name="span", id="priceblock_ourprice")
item_price = float(item_price_spans.getText().split("$")[1])

# Sending email if price is ideal for purchasing.
if item_price < 500.0:
    message = f"{item_name} is now {item_price}"

    with smtplib.SMTP("your_smtp_address", port=587) as connection:
        connection.starttls()
        connection.sendmail(
            from_addr="your_email",
            to_addrs="your_email",
            msg=f"Subject:Amazon Python Alert\n{message}\n{url}"
        )


