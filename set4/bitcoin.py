import requests
import sys
numbtc = (input())
if numbtc.isdigit():
    numbtc = float(numbtc)
    index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    index.json(numbtc)
    print(index)


try:
    numbtc = (input())
    if numbtc.isdigit():
        numbtc = float(numbtc)
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        index.json(numbtc)
        print(index)




    ...
except requests.RequestException:
    pass