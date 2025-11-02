# tried to make it work but i couldn't get into the coincap website

import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    request = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = request.json()
    print(data)


try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    price = data["bitcoin"]["usd"]
    amount = bitcoins * price
    print("${amount:,.4f}")

    ...
except requests.RequestException:
    sys.exit("Request failed")
