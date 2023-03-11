import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = index.json()
        for algo in o[]
        print(json.dumps(index.json(), indent=2))

    else:
        sys.exit("Missing command-line argument")




    ...
except (requests.RequestException, IndexError,):
    pass