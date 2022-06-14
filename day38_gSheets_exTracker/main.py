# Day 38: Exercise Tracking with Python and Google Sheets
import os
import requests
from datetime import *
import dotenv
dotenv.load_dotenv()
"""
Notes:
    OpenAI API is a user-friendly natural language processor
    We're going to use it to write sentences about our exercise
    
"""
APP_ID = os.getenv("NUT_ID")
API_KEY = os.getenv("NUT_KEY")
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_END = "https://api.sheety.co/b8d04519722a79fcddd581cc25f58317/workoutTracker/workouts"
SHEET_TOKEN = os.getenv("SHEET_TOK")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    # "query": input("What exercise did you do?")
    "query": "ran 2 miles and swam 200 meters"
}

sheet_header = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

response = requests.post(url=NUT_ENDPOINT, json=params, headers=header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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
    response2 = requests.post(url=SHEET_END, json=sheet_inputs, headers=sheet_header)
print(response2)
