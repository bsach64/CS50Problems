import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        amount = n * response["bpi"]["USD"]["rate_float"]
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")