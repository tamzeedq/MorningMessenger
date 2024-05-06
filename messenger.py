import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load environment variables
load_dotenv()

# Google Tasks API
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]
creds = Credentials.from_authorized_user_file("token.json", SCOPES)

# Auth Keys/Tokens
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
weather_key = os.environ['OPEN_WEATHER_API_KEY']
twilio_phone = os.environ['TWILIO_PHONE_NUMBER']
personal_phone = os.environ['PERSONAL_PHONE_NUMBER']

# Twilio API
client = Client(account_sid, auth_token)
text_message = ""

# Google Tasks API
try:
    service = build("tasks", "v1", credentials=creds)

    # Call the Tasks API
    lists = service.tasklists().list().execute()
    items = lists.get("items")
    tasks = service.tasks().list(tasklist=items[0]["id"]).execute()
    
    # Build task text
    text_message += "\nTasks: \n"
    for item in tasks["items"]:
        text_message += "-" + item["title"] + "\n"
            
except HttpError as err:
    print(err)

# Weather API
lat = 49.26054915669519
lon = -123.24599380297762

weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=metric'
r = requests.get(weather_url)
if (r.status_code == 200):
    weather = r.json()["main"]
        
    # Build weather text
    text_message += "\nWeather: \n"
    text_message += r.json()["weather"][0]["description"].capitalize() + "\n"
    text_message += "Feels like " + str(weather["feels_like"]) + "°C\n"
    text_message += "Min: " + str(weather["temp_min"]) + "°C\n"
    text_message += "Max: " + str(weather["temp_max"]) + "°C\n"
    
# Send text message
message = client.messages.create(
  from_=twilio_phone,
  body=text_message,
  to=personal_phone
)

print(message.sid)