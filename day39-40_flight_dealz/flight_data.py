import datetime as d_t
from flight_search import FlightSearch
from data_manager import DataManager
from sms_sender import Sms
f_s = FlightSearch()
d_m = DataManager()
sms = Sms()


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.g_sheet_data = []

    def check_prices(self, g_sheet):
        self.g_sheet_data = g_sheet
        tmr = d_t.datetime.today() + d_t.timedelta(days=1)
        start = tmr.strftime("%d/%m/%Y")
        end = (tmr + d_t.timedelta(days=180)).strftime("%d/%m/%Y")
        for row_data in self.g_sheet_data["prices"]:
            city_code = row_data["iataCode"]
            best_i_can_do = row_data["lowestPrice"]
            text = f_s.get_deals(city_code, start, end, best_i_can_do)
            if type(text) is str:
                sms.send(text)
    pass
