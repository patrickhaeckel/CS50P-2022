import requests
import json
import sys
try:

    if sys.argv[1].isdigit():
        lista = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        o = lista.json()
        value = (o["bpi"]["USD"]["rate"])
        value = value*(sys.argv[1])
        print(value)

    else:
        sys.exit("Missing command-line argument")


except (requests.RequestException, IndexError,):
    pass