import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        x = float(sys.argv[1])
        lista = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = lista.json()
        value = (o["bpi"]["USD"]["rate_float"])
        value = float(value) * x
        print(value)

    else:
        sys.exit("Missing command-line argument")


except (requests.RequestException, IndexError,):
    pass