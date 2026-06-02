import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c2935051a3c6c59ede703928eb3fe56b/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "Lowest_Price": new_price
            }
        }
        requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", json=new_data, auth=self.authorization)