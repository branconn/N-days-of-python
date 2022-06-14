# I decided to make this OOP
from config import ISS, MyPlace, Sender

iss = ISS()
my_place = MyPlace()
sender = Sender()


# If the ISS is close to my current position:
def is_close(**kwargs):
    if kwargs.get("test", False):
        pass
    else:
        iss.locate()
    if (-5 < (my_place.lat - iss.lat) < 5) and (-5 < (my_place.lng - iss.lng) < 5):
        return True
    else:
        print("ISS not close")
        return False


if is_close(test=True) and my_place.night_bool(test=True):
    sender.send_it("gmail")


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



