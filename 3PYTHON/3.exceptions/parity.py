def main():
    number = get_input('What\'s x ? ')
    print(f'{number} is even')

def get_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                if is_even(n):
                    # break
                    return n
        except ValueError:
            print('n in not integer.')
        # else:
        #     if n > 0:
        #         if is_even(n):
        #             break
    # return n

def is_even(no):
    return no % 2 == 0

if __name__ == '__main__':
    main()