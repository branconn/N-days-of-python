# Day 35: API Keys, Authentication, Sending SMS
"""
Notes:
We've already covered (1) API Endpoints and (2) API Parameters
We will now cover how to authenticate

APIs sell access to valuable data
    A lot of APIs have a free option
        This is managed through an API key
        The key allows the provider to track usage

"""
import os
import requests
from twilio.rest import Client
from ignore.password_manager import Password
pm = Password()
OWM_ENDPOINT, OWM_KEY = pm.retrieve("OWM_API")
T_SSID, T_TOK = pm.retrieve("twilio_API")
P_SENDER, P_RECIP = pm.retrieve("twilio_phones")
LAT = "33.748997"
LNG = "-84.387985"


def send_sms(text):
    client = Client(T_SSID, T_TOK)

    message = client.messages \
        .create(
            body=text,
            from_=P_SENDER,
            to=P_RECIP
        )
    print(message)


parameters = {
    "lat": LAT,
    "lon": LNG,
    "exclude": "current,minutely,daily,alerts",
    "appid": OWM_KEY,
}
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
response_data = response.json()
hourly_data = response_data["hourly"][:12]
umbrella = False
for hour in hourly_data:
    weather_code = hour["weather"][0]["id"]
    if weather_code < 800:
        umbrella = True
if umbrella:
    body = "You're gonna need a bigger umbrella"
else:
    body = "You'll be aight"

send_sms(body)




