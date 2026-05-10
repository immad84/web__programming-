def main():
    # x = get_input('What\'s x ? ')
    x = get_int('What\'s x ? ')
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            # x = int(input('What\'s x ? '))
            # return x
            return int(input(prompt))
        except ValueError:
            # print('x in not Integer')
            pass
        # else:
        #     return x
        
def get_input(prompt):
    while True:
        x = input(prompt)
        if x.isnumeric():
            return x
        

if __name__ == '__main__':
    main()