import requests
import datetime
import os

GENDER = "Male"
WEIGHT_KG = 79
HEIGHT_CM = 168
AGE = 20


APP_ID = "ee7a6a83"
API_KEY = "8ad4ed949f88eb20283237c936220847"
USERNAME = "gautam"
PASSWORD = "sureshpriya"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/2e55329412d2b2541c1210d6553c048a/workoutTracking/workouts"

exercise_text = input("tell me which exercise you did: ")

headers ={
    "X-APP-ID": APP_ID,
    "X-APP-KEY": API_KEY,
}

exercise_data = {
    "query": exercise_text
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
result = response.json()

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      USERNAME,
      PASSWORD,
  )
)

print(sheet_response.text)
