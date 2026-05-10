# This program will get first and last name and print full name.
# and print first name multiple times.
def main():
    first = input('What\'s your first name ? ')
    last = input('What\'s your last name ? ')

    full_name(first, last)

    n = int(input('How many times to print first name ? '))
    print(first_name_multiplier(first, n))


def full_name(x , y):
    name = x + ' ' + y
    name = name.strip().title()
    print('Hello,', name)


def first_name_multiplier(x , n):
    return (x + ' ') * n

main()