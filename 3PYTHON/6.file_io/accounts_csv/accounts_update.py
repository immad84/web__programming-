import csv

account_no = input('What\'s client account no ? ')
update_name = input('Wha\'s client name ? ')

with open('accounts.csv', 'r') as accounts:
    reader = csv.DictReader(accounts)
    for record in reader:
        for item in record.items():
            print(f'{item:<10}', end=' ')
        print()
            
    
