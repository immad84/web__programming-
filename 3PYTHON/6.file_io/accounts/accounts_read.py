from tabulate import tabulate

table = []
headers = ['Account', 'Name', 'Amount']

with open('acounts.txt') as accounts:
    # accounts.seek(40)
    for record in accounts:
        table.append(record.split())

print(tabulate(table, headers, tablefmt='grid', colalign=["left"]))