import os
import dotenv
dotenv.load_dotenv()
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey": os.getenv("KIWI_API"),
        }
        self.loc_url = "https://tequila-api.kiwi.com/locations/query"
        self.fs_url = "https://tequila-api.kiwi.com/v2/search"

    def get_city(self, query):
        params = {
            "term": query,
            "location_types": "city"
        }
        response = requests.get(url=self.loc_url, params=params, headers=self.header)
        result = response.json()
        return result["locations"][0]["code"]

    def get_deals(self, code, start, end, highest):
        params = {
            "fly_from": "ATL",
            "fly_to": code,
            "dateFrom": start,
            "dateTo": end,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "curr": "USD",
            "price_to": int(highest),
            "price_from": round(int(highest) * 0.5),
            "sort": "quality",
            "limit": 3,
        }
        high = 251
        t_params = {
            "fly_from": "ATL",
            "fly_to": "PIT",
            "dateFrom": "12/12/2021",
            "dateTo": "12/06/2022",
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "curr": "USD",
            "price_to": high,
            "price_from": round(int(highest) * 0.5),
            "sort": "quality",
            "limit": 1,
        }
        response = requests.get(url=self.fs_url, params=params, headers=self.header)
        deals_data = response.json()
        return deals_data
        # print(deals_data)
        # I should separate the below process into another object

        for flight in deals_data["data"]:
            if type(flight["availability"]["seats"]) is int:
                from_code = flight["flyFrom"]
                to_code = flight["flyTo"]
                to_city = flight["cityTo"]
                price = flight["price"]
                departure = flight["local_departure"][:10]
                dur = flight["nightsInDest"]
                message = (f"We found a flight to {to_city} in your budget:\n{from_code} -> {to_code} "
                      f"departing {departure} and returning in {dur} days for ${price}")
                return message
            # else:
            #     return f"Nothing to {code}"

