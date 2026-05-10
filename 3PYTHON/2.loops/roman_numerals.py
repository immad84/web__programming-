roman_numbers = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
print('I', roman_numbers['I'])
print('II', roman_numbers['II'])
print('III', roman_numbers['III'])
print('V', roman_numbers['V'])
print('X', roman_numbers['X'])

# Updating / changing value in dict
roman_numbers['X'] = 10
print('Updated value of X',roman_numbers['X'])

# Add key-value in dict
roman_numbers['L'] = 100
print('New Value added, L', roman_numbers['L'])

#delete value III in dict
del roman_numbers['III']
print('III deleted')

print(roman_numbers.pop('I'))

