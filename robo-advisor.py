import json
import os
import requests

#from dotenv import load_dotenv



#load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("9437TKPHKRA9TX6O") #Remove API Key later

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response=requests.get(request_url)
#print(type(response)) 
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text) #convert str to dic

#breakpoint ()
tsd = parsed_response["Time Series (Daily)"]

dates=list(tsd.keys()) #Convert doctionary to List
latest_day = dates [0] #Pulls latest date b/c ordered from most current to oldest


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]

high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)

low_prices = []

for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_low = min(low_prices)

def to_usd (my_price):
    return "${0:0.2f}".format(my_price)

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

