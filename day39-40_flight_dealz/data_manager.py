import os
import dotenv
import requests
import datetime as dt
from flight_search import FlightSearch
from sms_sender import Sms
dotenv.load_dotenv()
flight_search = FlightSearch()
sms = Sms()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/b8d04519722a79fcddd581cc25f58317/flightDeals/prices"
        # self.api = os.getenv("SHEET_TOK")
        self.header = {
            "Authorization": f"Bearer {os.getenv('SHEET_TOK')}"
        }
        response = requests.get(url=self.url, headers=self.header)
        self.sheet_data = response.json()


    def fill_codes(self):
        # print(self.sheet_data)
        for row_data in self.sheet_data["prices"]:
            if row_data["iataCode"] == "":
                row_index = row_data["id"]
                code = flight_search.get_city(row_data["city"])
                sheet_inputs = {
                    "price": {
                        "iataCode": code,
                    }
                }
                response = requests.put(url=f"{self.url}/{row_index}", json=sheet_inputs, headers=self.header)

    def check_prices(self):
        pass
    # def check_prices(self):
    #     tmr = dt.datetime.today() + dt.timedelta(days=1)
    #     start = tmr.strftime("%d/%m/%Y")
    #     end = (tmr + dt.timedelta(days=180)).strftime("%d/%m/%Y")
    #     for row_data in self.sheet_data["prices"]:
    #         city_code = row_data["iataCode"]
    #         best_i_can_do = row_data["lowestPrice"]
    #         text = flight_search.get_deals(city_code, start, end, best_i_can_do)
    #         if type(text) is str:
    #             sms.send(text)

dm = DataManager()
dm.check_prices()

# f_search = FlightSearch()
# result = f_search.get_city("Paris")
# print(result)
