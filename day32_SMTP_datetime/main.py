##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as r
import smtplib
from ignore.password_manager import Password
pm = Password()

# 1. Update the birthdays.csv
bday_df = pd.read_csv("birthdays.csv")
# print(type(bday_df))

# 2. Check if today matches a birthday in the birthdays.csv


def check_em(df):
    now = dt.datetime.now()
    mon = now.month
    date = now.day
    bday_mons = df[df.month == mon]
    if not bday_mons.empty:
        bday_day = bday_mons[bday_mons.day == date]
        if not bday_day.empty:
            write_em(bday_day)
        else:
            print("no matching birthday")
    else:
        print("no matching birthday")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

def write_em(resi):
    b_name = resi.name.values[0]
    b_email = resi.email.values[0]
    # print(f"it's yah boy, {b_name} @ {b_email}")
    eenie_meenie = r.randint(1, 3)
    letter_path = f"./letter_templates/letter_{eenie_meenie}.txt"
    with open(file=letter_path, mode="r") as letter:
        letter_body = letter.read()
    letter_body = letter_body.replace("[NAME]", b_name)
    letter_body = letter_body.replace("Angela", "Brandon")
    send_em(b_email, letter_body)


# 4. Send the letter generated in step 3 to that person's email address.

def send_em(recipient, text):
    heading = "Steadily marching towards the abyss"
    message = f"Subject:{heading}\n\n{text}"
    details = pm.retrieve("gmail")
    if details is not None:
        email = details[0]
        email_pw = details[1]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # start transport layer security
            connection.login(user=email, password=email_pw)
            connection.sendmail(from_addr=email,
                                to_addrs="bconner6@gatech.edu",
                                msg=message)
        print("message sent")


check_em(bday_df)

