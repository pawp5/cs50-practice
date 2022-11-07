import sys
import requests


# Handling command-line errors.
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument.")
try:
    coins = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Command-line argument is not a number.")

# Handling requests errors.
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Try again.")
else:
    x = response.json()
    amount = x["bpi"]["USD"]["rate"]


for i in amount:
    if "," in i:
        coin_cost = float(amount.replace(",", ""))

print("${:,.4f}".format(coins * coin_cost))