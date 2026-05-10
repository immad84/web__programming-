from tabulate import tabulate
import os

table = []
headers = ['Account', 'Name', 'Amount']

with open('acounts.txt', 'r') as accounts, open('temp_file.txt', 'w+') as temp_file:
    for record in accounts:
        account, name, amount = record.split()
        if account != '200':
            temp_file.write(record)
        else:
            temp_record = ' '.join([account, 'David', amount])
            temp_file.write(temp_record + '\n')
    
    # after writing the file pointer is at the end need to move it back to begining.
    temp_file.seek(0)

    for line in temp_file:
        table.append(line.split())

os.remove('acounts.txt')
os.rename('temp_file.txt', 'acounts.txt')
print(tabulate(table, headers, tablefmt='grid'))