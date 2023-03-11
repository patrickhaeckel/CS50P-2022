import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        lista = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = lista.json()
        for key, value in o["bpi"].items():
            print(value["rate_float"])

    else:
        sys.exit("Missing command-line argument")




    ...
except (requests.RequestException, IndexError,):
    pass