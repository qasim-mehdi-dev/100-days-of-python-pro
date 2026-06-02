import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")

class DataManager:

    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "LowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._authorization
        )

    def get_customer_emails(self):
            print("Using local backup customer database...")
            self.customer_data = [
                {"email": "AlexMark5@gmail.com"},
                {"email": "JoshEllison45@gmail.com"},
                {"email": "Maddison99@gmail.com"},
                {"email": "qasimtest0@gmail.com"}
            ]
            return self.customer_data