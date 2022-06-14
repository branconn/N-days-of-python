# Imports
import os
import requests
import datetime
from dotenv import load_dotenv  # pip install python-dotenv
load_dotenv()

# Globes
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = os.getenv("STOCK_API")
NEWS_API = os.getenv("NEWS_API")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
response_data = response.json()
ticker_values = response_data["Time Series (Daily)"]
latest = datetime.date.today() - datetime.timedelta(days=1)
weekday = False
while not weekday:
    dow = latest.isoweekday()
    if dow > 5:
        latest -= datetime.timedelta(days=1)
    else:
        weekday = True
pre_latest = latest - datetime.timedelta(days=1)
weekday = False
while not weekday:
    dow = pre_latest.isoweekday()
    if dow > 5:
        pre_latest -= datetime.timedelta(days=1)
    else:
        weekday = True
t_close = ticker_values[str(latest)]["4. close"]
t1_close = ticker_values[str(pre_latest)]["4. close"]
delt = float(t_close)/float(t1_close) - 1
if abs(delt) >= 0.05:
    print("Movement")
else:
    print("Nominal fluctuations")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

