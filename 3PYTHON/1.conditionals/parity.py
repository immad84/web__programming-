def main():
    number = int(input('Enter a number! '))
    if is_even(number):
        print('It\'s even number.')
    else:
        print('It\'s odd number.')

def is_even(n):
    return n % 2 == 0 # n % 2 == 0 is a boolean expression.
    # return True if n % 2 == 0 else False # conditional expression

main()