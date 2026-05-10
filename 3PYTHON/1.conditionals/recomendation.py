def main():
    guests = int(input('How many guests ? '))
    if not guests == 1 or guests == 2 or guests == 3:
        print('Incorrect Guests.')
        return

    taste = input('Enter your taste ? ')
    if not (taste == 'Hot' or taste == 'Medium' or taste == 'Mild'):
        print('Incorrect Taste.')
        return

    if guests == 1 and taste == 'Hot':
        print('Small Hot and Spicy Pizza')
    elif guests == 1 and taste == 'Medium':
        print('Small Vagitarian Pizza')
    elif guests == 1 and taste == 'Mild':
        print('Small Cheese And Tomato Pizza')
    elif guests == 2 and taste == 'Hot':
        print('Medium Hot and Spicy Pizza')
    elif guests == 2 and taste == 'Medium':
        print('Medium Vegetatien Pizza')
    elif guests == 2 and taste == 'Mild':
        print('Medium Cheese And Tomato Pizza')
    elif guests == 3 and taste == 'Hot':
        print('Large Hot and Spicy Pizza')
    elif guests == 3 and taste == 'Medium':
        print('Large Vegetatien Pizza')
    else:
        print('Large Cheese And Tomato Pizza')

main()