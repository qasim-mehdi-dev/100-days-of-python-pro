import requests
from twilio.rest import Client
import os

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")

account_sid = os.getenv("TWILIO")
auth_token = os.getenv("AUTH_TOKEN")
to_phone = os.getenv("TO_PHONE")

weather_params = {
    "lat": 17.385044,
    "lon": 78.486671,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"][:4]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+16182282859',
        to=to_phone
    )
    print(message.status)