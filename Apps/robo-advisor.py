#Robo Advisor App - Based on Walkthrough by Prof. Rossetti (https://www.youtube.com/watch?v=UXAVOP1oCog&t=847s)
import json
import os
import requests
import datetime
import pandas
import csv


#gets data from alphaadvantage
API_KEY = os.environ.get("9437TKPHKRA9TX6O") #Remove API Key later

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response=requests.get(request_url)
#print(type(response)) 
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text) #convert str to dic

#breakpoint ()
tsd = parsed_response["Time Series (Daily)"] #save dictionary as a simple variable

dates=list(tsd.keys()) #Convert doctionary to List
latest_day = dates [0] #Pulls latest date b/c ordered from most current to oldest


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]

high_prices = [] #empty list

#from list get recent highs and recent lows

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)

low_prices = []

for date in dates:
    daily_prices = tsd[date]
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_low = min(low_prices)

#input time
time_now = datetime.datetime.now() #> datetime.datetime(2019, 3, 3, 14, 44, 57, 139564)
formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S") #> '2019-03-03 14:45:27'

#Convert to CSV
#breakpoint() #remove after getting keys
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "monthly_sales.csv")

csv_headers = ["timestamp", "open", "low", "high", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        writer.writerow ({
            "timestamp":date,
            "open":daily_prices ["1. open"],
            "high":daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })
    
#format to USD
def to_usd (my_price):
    return "${0:0.2f}".format(my_price)

#Calculation



#Recommendation

#output
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUESTED AT: {formatted_time_now}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

