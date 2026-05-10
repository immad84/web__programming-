def main():
    exp = input('Expression: ')
    x, y, z = exp.split(' ')
    x = float(x)
    z = float(z)
    # print(get_result(x, y, z))
    print(get_result_match(x, y, z))

def get_result(a, b, c):
    if b == '+':
        return f'{a + c:.1f}'
    elif b == '-':
        return f'{a - c:.1f}'
    elif b == '*':
        return f'{a * c:.1f}'
    elif b == '/':
        if c == 0:
            return 'Denominator must be non-zero'
        else:
            return f'{a / c:.1f}'

def get_result_match(a, b, c):
    match b:
        case '+':
            return f'{a + c:.1f}'
        case '-':
            return f'{a - c:.1f}'
        case '*':
            return f'{a * c:.1f}'
        case '/':
            if c == 0:
                return 'Denominator must be non-zero'
            else:
                return f'{a / c:.1f}'


if __name__ == '__main__':
    main()
