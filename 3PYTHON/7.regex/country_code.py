import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    try:
        phoneNo = input("PhoneNo: ")
        pattern = r"^(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}$"
        if match := re.search(pattern, phoneNo, flags=re.IGNORECASE):
            print(locations[match.group("country_code")])
    except KeyError as e:
        print(f"{e} unknown country code")


if __name__ == "__main__":
    main()
