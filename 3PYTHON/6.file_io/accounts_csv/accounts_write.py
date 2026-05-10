import csv

account_no = input('What\'s account no ? ')
name = input('What\'s client name ? ')
amount = input('What\'s client amount ? ')

with open('accounts.csv', 'a') as accounts:
    writer = csv.DictWriter(accounts, fieldnames=['Account_No', 'Name', 'Amount'])
    writer.writerow({'Account_No': account_no, 'Name': name, 'Amount': amount})



