def main():
    percentage = get_percentage('Fraction: ')
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage}%') 

def get_percentage(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if x > y:
                continue
            div = x / y  
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except EOFError:
            print('EOF Error')
        except KeyboardInterrupt:
            print('Keyboard Interupt.')
        else:
            per = round(div * 100)
            return per

if __name__=='__main__':
    main()