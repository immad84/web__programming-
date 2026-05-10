def main():
    number = get_input()
    print(number)

def get_input():
    while True:
        n = int(input('What\'s n ? '))
        if n > 0:
            if is_even(n):
                break
    return n

def is_even(no):
    return no % 2 == 0

if __name__ == '__main__':
    main()