import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "qasim9"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph9"
headers = {
     "X-USER-TOKEN": TOKEN,
}

user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# user_response = requests.post(pixela_endpoint, json=user_params)
# print(user_response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }

# graph_response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km today? ")
}
pixel_response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "7"
# }
# update_response = requests.put(update_endpoint, json=new_pixel_data, headers=headers)
# print(update_response.text)
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete_response = requests.delete(delete_endpoint, headers=headers)
# print(delete_response.text)