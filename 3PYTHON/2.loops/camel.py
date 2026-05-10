def main():
    camel_case = input('camelCase: ')
    print(f'snake_case: {change_case(camel_case)}')

def change_case(camel):
    snake_case = ''
    for char in camel:
        if char.isupper():
            snake_case += '_' + char.lower()
            continue
        snake_case += char
    return snake_case

if __name__ == '__main__':
    main()