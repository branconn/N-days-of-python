# Day 37: Habit Tracker
import os
import requests
import datetime
from dotenv import load_dotenv  # pip install python-dotenv
load_dotenv()
"""
Notes: 
    HTTP Requests:
    Get: we get data
    Post: we give data, get confirmation
    Put: we update a piece of data
    Delete: we delete a piece a data
Post habit tracking data to Pixela

using headers for api tokens is more secure than sending as a parameter
https requests are encrypted, but still not fully secure

"""
USERNAME = os.getenv("PIX_USER")
TOKEN = os.getenv("PIX_API")
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
datum_endpoint = f"{graph_endpoint}/{GRAPHID}"
tod = datetime.datetime.today().strftime("%Y%m%d")
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
graph_config = {
    "id": GRAPHID,
    "name": "dev time",
    "unit": "hr",
    "type": "float",
    "color": "shibafu"
}
datum_bits = {
    "date": "20211205",
    "quantity": "2",
}
datum_update = {
    "quantity": "1.5",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response = requests.post(url=datum_endpoint, json=datum_bits, headers=headers)
# response = requests.put(url=f"{datum_endpoint}/{tod}", json=datum_update, headers=headers)
# response = requests.delete(url=f"{datum_endpoint}/20211205", headers=headers)

# print(response.text)
