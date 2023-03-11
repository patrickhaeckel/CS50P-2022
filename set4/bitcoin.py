import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        for 
        print(json.dumps(index.json(), indent=2))




    ...
except (requests.RequestException, IndexError, ValueError):
    pass