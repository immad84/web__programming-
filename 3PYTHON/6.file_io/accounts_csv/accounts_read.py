import csv
from tabulate import tabulate

account_list = []
sorted_account_list = []
with open('accounts.csv') as accounts:
    reader = csv.DictReader(accounts)
    # account_no, name, amount = reader.fieldnames
    # print(f'{account_no:<20}{name:<10}{amount:>10}')
    for record in reader:
        account_list.append(record)
        # print(f'{record["Account_No"]:<20}{record["Name"]:<10}{record["Amount"]:>10}')

# print('Sorted List of Account By Name:')

for acc in sorted(account_list, key=lambda account: account["Name"]):
    sorted_account_list.append(acc)

print(tabulate(sorted_account_list, headers = "keys", tablefmt="grid", colalign=["left"]))