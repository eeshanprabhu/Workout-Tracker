import requests
from datetime import datetime
print("Hello world")
APP_ID="f23e2493"
APP_KEY="d05e7363073a4fbbf273e9a44f4157a2"

endpoint=f"https://trackapi.nutritionix.com/v2/natural/exercise"

headers={
    'Content-Type':'application/json',
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY
}
parameters={
    'query':input("Tell me which exercises you did")
}

exercise_response=requests.post(url=endpoint,headers=headers,json=parameters)
exercise_data=exercise_response.json()
print(exercise_data)
print(exercise_data["exercises"][0]["duration_min"])
AUTH_KEY="Basic ZWVzaGFuNTU1OmFzZGZnaGprbEAx"

sheety_header={
    "Authorization":AUTH_KEY
}
sheets_endpoint="https://api.sheety.co/3b533d3a177e6399389b12494a7c7f31/workouts/workouts"
for i in range(len(exercise_data["exercises"])):

    workouts={
        'workout':{
            'date': datetime.today().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'exercise': exercise_data["exercises"][i]["name"].title(),
            'duration': f'{exercise_data["exercises"][i]["duration_min"]} mins',
            'calories': exercise_data["exercises"][i]["nf_calories"]
        }
    }
    sheets_response = requests.post(url=sheets_endpoint, json=workouts,headers=sheety_header)
    print(sheets_response.text)

