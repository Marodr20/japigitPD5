import urllib.request
import sys
import json

def getStockData():
    apiKEY = "FGAMG8B9J2UC7MX5"
    function = "BatchStockQuotes"
    APPL_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=msft&apikey=FGAMG8B9J2UC7MX5"
    symbol = ""
    filename = "japi.out"
    while symbol != 'stop':
        symbol = input('Enter Stock symbol, [tpye "stop" to quit]: ')
        if symbol != "stop":
            fullurl = APPL_URL + function + "&symbols=" + symbol + "&apikey=" + apiKEY
            connection = urllib.request.urlopen(fullurl)
            responseString = connection.read().decode()
            json_data = json.dumps(responseString)
            parsed_json = json.loads(responseString)
            d = (f"The current price of {parsed_json['Stock Quotes'][0]['1. symbol']} is {parsed_json['Stock Quotes'][0]['2. price']}.")
            print(responseString)
            print(d)
            with open(filename,'a') as f:
                f.write(responseString)
                f.write(d)
        else:
            print("Stock Quotes retrieved sucessfully!")
def main():
        getStockData()


main()





master version
