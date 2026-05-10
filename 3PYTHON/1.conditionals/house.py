def main():
    name = input('What\'s your name ? ').lower().strip()
    house(name)
    house_match(name)

def house(n):
    if n == 'harry' or n == 'hermione' or n == 'ron':
        print('Gryffindor')
    elif n == 'draco':
        print('Slytherin')
    else:
        print('Who?') 

def house_match(n):
    match n:
        case 'harry' | 'hermione' | 'ron':
            print('Gryffindor')
        case 'draco':
            print('Slytherin')
        case _:
            print('Who?')

main()

