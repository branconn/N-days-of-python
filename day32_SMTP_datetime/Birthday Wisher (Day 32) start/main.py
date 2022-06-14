import smtplib
import datetime as dt
import random as r
from ignore.password_manager import Password
pm = Password()
details = pm.retrieve("gmail")
test_email = details[0]
test_password = details[1]
# sdf
# test_message = "Subject:Introduction\n\nHello, Mr. Anderson"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # start transport layer security
#     connection.login(user=test_email, password=test_password)
#     connection.sendmail(from_addr=test_email,
#                         to_addrs="bconner6@gatech.edu",
#                         msg=test_message)


def send_that_quote():
    with open("quotes.txt", mode="r") as quotes:
        quote_list = quotes.readlines()
    daily_quote = r.choice(quote_list)
    heading = "Weekly Inspiration"
    message = f"Subject:{heading}\n\n{daily_quote}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # start transport layer security
        connection.login(user=test_email, password=test_password)
        connection.sendmail(from_addr=test_email,
                            to_addrs="bconner6@gatech.edu",
                            msg=message)
    print("message sent")


now = dt.datetime.now()
if now.weekday() == 2:
    print("day matches")
    # send_that_quote()
else:
    print(now.weekday())

# create datetime obj:
dob = dt.datetime(year=1990, month=1, day=1)
# print(dob)
