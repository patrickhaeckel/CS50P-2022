import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = index.json()
        for results in o["USD"]:
            print(results["rate_float"])

    else:
        sys.exit("Missing command-line argument")




    ...
except (requests.RequestException, IndexError,):
    pass