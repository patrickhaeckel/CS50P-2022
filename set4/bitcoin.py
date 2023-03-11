import requests
import sys

numbtc = float(input())
try:

    requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    ...
except requests.RequestException: