import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = get_amount(response)
        amount = rate * n
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        print("Request Exception")


def get_amount(res):
    response = res.json()
    price_index = response["bpi"]
    usd_price_index = price_index["USD"]
    rate_float = usd_price_index["rate_float"]
    return rate_float


if __name__ == "__main__":
    main()
