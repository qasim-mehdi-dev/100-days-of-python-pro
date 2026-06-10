import os
import re
import smtplib
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

ZENROWS_API_KEY = os.getenv("ZENROWS_API_KEY")
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6"
BUY_PRICE = 999999
MAX_RETRIES = 5

ZENROWS_PAYLOAD = {
    "apikey": ZENROWS_API_KEY,
    "url": AMAZON_URL,
    "js_render": "true",
    "premium_proxy": "true",
    "custom_headers": "true",
}

ZENROWS_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
for attempt in range(MAX_RETRIES):
    response = requests.get("https://api.zenrows.com/v1/", params=ZENROWS_PAYLOAD, headers=ZENROWS_HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    price_elem = soup.find("span", class_="a-offscreen")

    if price_elem:
        print(f"✅ Price found on attempt {attempt + 1}")
        break

    print(f"❌ Attempt {attempt + 1} failed, retrying in 3 seconds...")
    time.sleep(3)
else:
    print("Could not fetch price after 5 attempts. Try again later.")
    exit()

price = price_elem.getText()
price_as_float = float(re.search(r'[\d,]+\.?\d*', price).group().replace(",", ""))
title = soup.find(id="productTitle").get_text().strip()

print(f"Product: {title}")
print(f"Current Price: {price} → Parsed: {price_as_float}")

if price_as_float < BUY_PRICE:
    message = f"{title} is now available for {price}!\n\nLink to purchase: {AMAZON_URL}"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject: Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
    print("✅ Alert email successfully dispatched!")
else:
    print(f"Price {price} is above target {BUY_PRICE}. No alert sent.")