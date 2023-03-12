import requests
import json
import sys
try:

    if len(sys.argv) == 2
        x = int(sys.argv[1])
        lista = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        dict = lista.json()
        value = (dict["bpi"]["USD"]["rate_float"])
        value = float(value) * x
        print(f"${value:,.4f}")

    else:
        sys.exit("Missing command-line argument")


except (requests.RequestException, IndexError,):
    pass