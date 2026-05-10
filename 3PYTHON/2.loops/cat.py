def main():
    number = get_input()
    print_meow(number)

def get_input():
    # infinite while loop breaks out with break keyword
    while True:
        n = int(input('Enter a positive number ? '))
        if n > 0:
            break
        else:
            continue
    return n

def print_meow(n):
    for _ in range(n):
        print('meow')

if __name__ == '__main__':
    main()