count = 0
for i in range(2, 100, 2):
    print(id(i), end=' ')
    count += 1
print('Total Evens: ', count)
