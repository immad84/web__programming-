with open('acounts.txt', 'w') as accounts:  # why not 'a' mode ?
    accounts.write('100 Jones 34.3\n')
    accounts.write('200 Doe 334.3\n')
    accounts.write('300 White -19.55\n')
    accounts.write('400 Harry 11.5\n')
    accounts.write('500 Hermione 990.3\n')
    print('600 Draco 12.90\n', file=accounts)