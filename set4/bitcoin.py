import requests
import sys
try:
    numbtc =float(input())
    index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(index.json())




    ...
except requests.RequestException:
    pass