import os
from dotenv import load_dotenv
import requests

load_dotenv()

GENDER = "Male"
WEIGHT_KG = 102.3
HEIGHT_CM = 177
AGE = 32

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
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

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
json_response = response.json()
print(json_response)