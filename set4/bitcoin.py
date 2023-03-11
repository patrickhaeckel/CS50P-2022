import requests
import sys

numbtc = float(input())
indexx = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(indexx)
