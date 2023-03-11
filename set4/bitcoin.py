import requests
import sys

numbtc = (input())

try:
    if numbtc.isdigit():
        numbtc = float(numbtc)
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(f"${index:,.4f}")



    ...
except requests.RequestException:
    pass