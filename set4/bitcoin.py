import requests
import sys
try:
    numbtc =float(input())
    index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(json.dumps(index.json()), indent=2)




    ...
except requests.RequestException:
    pass