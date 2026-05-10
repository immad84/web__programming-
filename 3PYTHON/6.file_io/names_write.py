
# file = open('names.txt', 'a')
# file.write(f'{name}\n')
# file.close()

with open('names.txt', 'a') as file:
    while True:
        try:
            name = input('What\'s your name ? ')
            file.write(f'{name}\n')
        except EOFError:
            print()
            break