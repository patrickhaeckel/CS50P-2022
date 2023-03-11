import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        lista = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = lista.json()
        for result in o["bpi"]:
            print(o["time"])

    else:
        sys.exit("Missing command-line argument")




    ...
except (requests.RequestException, IndexError,):
    pass