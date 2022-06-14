import requests
import datetime
import smtplib
from ignore.password_manager import Password


class ISS:
    def __init__(self, **kwargs):
        self.lat = 33.748997
        self.lng = -84.387985
        self.params = {}

    def locate(self):
        response_1 = requests.get(url="http://api.open-notify.org/iss-now.json")
        response_1.raise_for_status()  # this raises the exception for an API response that isn't successful
        json_data = response_1.json()
        self.params = {
            "lat": json_data["iss_position"]["latitude"],
            "lng": json_data["iss_position"]["longitude"],
        }
        self.lat = float(self.params["lat"])
        self.lng = float(self.params["lng"])


class MyPlace:
    def __init__(self):
        self.lat = 33.748997
        self.lng = -84.387985
        self.params = {
            "lat": self.lat,
            "lng": self.lng,
        }
        self.night = False

    def night_bool(self, **kwargs):
        sunset_url = "https://api.sunrise-sunset.org/json"
        response_2 = requests.get(url=sunset_url, params=self.params)
        response_2.raise_for_status()
        sunset_json = response_2.json()

        sunrise_t = sunset_json["results"]["sunrise"].split(":")
        sunset_t = sunset_json["results"]["sunset"].split(":")
        now_t = str(datetime.datetime.now().time()).split(":")

        self.night = False
        if int(now_t[0]) < int(sunrise_t[0]) or int(now_t[0]) > int(sunset_t[0]) + 12:
            self.night = True
        elif int(now_t[0]) == int(sunrise_t[0]) or int(now_t[0]) == int(sunset_t[0]) + 12:
            if int(now_t[1]) < int(sunrise_t[1]) or int(now_t[1]) > int(sunset_t[1]):
                self.night = True
        result = kwargs.get("test", self.night)
        if not result:
            print("It's too bright")
        return result


class Sender:
    def __init__(self):
        self.pm = Password()
        self.details = ()

    def send_it(self, from_address):
        self.details = self.pm.retrieve(from_address)
        heading = "ISS Alert"
        text = "ISS is in your location and it should be dark enough to see. Look up!"
        message = f"Subject:{heading}\n\n{text}"
        if self.details is not None:
            email = self.details[0]
            email_pw = self.details[1]
            self.details = ()
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()  # start transport layer security
                connection.login(user=email, password=email_pw)
                connection.sendmail(from_addr=email,
                                    to_addrs="bconner6@gatech.edu",
                                    msg=message)
            print("message sent")
