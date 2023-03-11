import requests
import sys



try:
    numbtc = (input())
    if numbtc.isdigit():
        numbtc = float(numbtc)
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(index.json())
        print(f"${index:,.4f}")



    ...
except requests.RequestException:
    pass