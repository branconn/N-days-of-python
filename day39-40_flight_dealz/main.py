# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from sms_sender import Sms
from flight_data import FlightData
f_s = FlightSearch()
d_m = DataManager()
sms = Sms()
f_d = FlightData()

d_m.fill_codes()
f_d.check_prices(d_m.sheet_data)
# f_d.check_prices()
# f_s.get_deals()
a = d_m.sheet_data

# def fill_codes(table):
#     pass
