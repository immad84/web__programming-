def main():
    x = float(input('What\'s x ? '))
    y = float(input('What\'s y ? '))

    print(f'x + y = {add(x, y)}')
    print(f'x - y = {subtract(x, y):.2f}')
    print(f'x * y = {multiply(x, y):.2f}')
    print(f'x / y = {divide(x, y):.2f}')
    print(f'x ** 2 = {exponent(x):.2f}')
    print(f'x // y = {f_divide(x, y):.2f}')
    print(f'x % y = {mod(x, y):.2f}')


def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

def f_divide(a , b):
    return a // b

def exponent(a):
    return a ** 2

def mod(a , b):
    return a % b

main()
