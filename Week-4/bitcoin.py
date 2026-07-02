import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "88b9fee99f4a9f8a7e9366ea31ca858b35ed05a4bcc99d8f60eaac98fb45697f"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Could not fetch Bitcoin price data")

    data = response.json()
    try:
        price_usd = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing Bitcoin price from response")

    total_cost = bitcoins * price_usd

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
