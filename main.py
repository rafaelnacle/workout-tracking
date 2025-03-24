import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

GENDER = "Male"
WEIGHT_KG = 102.3
HEIGHT_CM = 177
AGE = 32

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
EMAIL = os.getenv("EMAIL")
TOKEN = os.getenv("TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0280f87b4f179fca1b41989e9ec5c2da/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
# {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 40.02, 'met': 9.8, 'nf_calories': 668.69, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}
response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
json_response = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in json_response["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=sheety_headers)
    print(sheety_response.text)
