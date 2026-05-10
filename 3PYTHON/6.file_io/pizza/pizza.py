import csv
from tabulate import tabulate
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    pizza = []

    try:
        csv_file = is_valid_file(sys.argv)
        with open(f"{csv_file}") as file:
            reader = csv.DictReader(file)
            for item in reader:
                pizza.append(item)
        print(tabulate(pizza, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File Does Not Exist")
    except ValueError:
        sys.exit("Not a CSV file")


def is_valid_file(arg):
    name = arg[1]
    is_extension_exist = name.rfind(".")
    if is_extension_exist < 0 or not name.endswith("csv"):
        raise ValueError("Not a csv file")
    return name


if __name__ == "__main__":
    main()
