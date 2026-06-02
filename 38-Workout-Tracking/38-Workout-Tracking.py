import os
import requests
from datetime import datetime

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = "male"
WEIGHT_KG = 64
HEIGHT_CM = 167
AGE = 27
YOUR_TOKEN = os.environ.get("YOUR_TOKEN")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c2935051a3c6c59ede703928eb3fe56b/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercise you did: ")
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight": WEIGHT_KG,
    "height": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {YOUR_TOKEN}",
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)