import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "TESLA Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_lst = [value for (key, value) in data.items()]

yesterday_data = data_lst[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_lst[1]
day_before_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price) * 100), 2)
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
                           f"Headline: {article['title']}, \n"
                           f"Brief: {article['description'] if article['description'] else article.get('content', 'No summary available.')}")
                          for article in three_articles]
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    to_phone = os.getenv("TO_PHONE")
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+16182282859',
            to=to_phone
        )