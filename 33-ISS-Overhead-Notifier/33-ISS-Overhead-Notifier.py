import smtplib
from datetime import datetime
import requests
import time

MY_LAT = 17.385044
MY_LONG = 78.486671
MY_EMAIL = "qasimtest0@gmail.com"
PASSWORD = ""

def iss_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()

  data = response.json()
  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  if MY_LAT-5 <=iss_latitude <=MY_LAT+5 and MY_LONG-5 <=iss_longitude <=MY_LONG+5:
      return True
  return False

def is_night():
    parameters ={
        "latitude": MY_LAT,
        "longitude": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    iss_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    iss_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= iss_sunset or time_now <= iss_sunrise:
        return True
    return False

while True:
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: Look Up👆\n\nThe ISS is above you"
                                )
    time.sleep(60)