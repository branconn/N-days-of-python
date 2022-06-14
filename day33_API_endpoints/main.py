# Day 33: API Endpoints & API Parameters
"""
Notes:
API: Application Programming Interface
    the interface between you and the database
    There are simple get requests, and other requests that require more
    API Endpoint is the location of the accessible data (URL)
    Responses:
        1XX - still processing
        2XX - successful request
        3XX - do not have permission
        4XX - you screwed up (file not found)
        5XX - the server screwed up

API Parameters:
    give an input when making a request to get specific data
    not all APIs have parameters, others are required
        check the API docs
EndpointUrl + ? + key=value + & key2=value2

"""
import requests
import datetime

MY_LAT = 33.748997
MY_LNG = -84.387985

response_1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response_1.raise_for_status()  # this raises the exception for an API response that isn't successful
json_data = response_1.json()
iss_parameters = {
    "lat": json_data["iss_position"]["latitude"],
    "lng": json_data["iss_position"]["longitude"],
}
my_parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

sunset_url = "https://api.sunrise-sunset.org/json"
response_2 = requests.get(url=sunset_url, params=my_parameters)
response_2.raise_for_status()
sunset_json = response_2.json()


sunrise_t = sunset_json["results"]["sunrise"].split(":")
sunset_t = sunset_json["results"]["sunset"].split(":")
now_t = str(datetime.datetime.now().time()).split(":")

night = False
if int(now_t[0]) < int(sunrise_t[0]) or int(now_t[0]) > int(sunset_t[0])+12:
    night = True
elif int(now_t[0]) == int(sunrise_t[0]) or int(now_t[0]) == int(sunset_t[0])+12:
    if int(now_t[1]) < int(sunrise_t[1]) or int(now_t[1]) > int(sunset_t[1]):
        night = True

if night:
    print("night")
else:
    print("day")

# print(data)


