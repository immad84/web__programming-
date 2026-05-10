def main():
    DUE_AMOUNT = 50
    amount = 0
    while True:
        if amount < DUE_AMOUNT:
            print(f'Amount Due: {DUE_AMOUNT - amount}')
            coin = get_coins()
            amount += coin
        elif amount > DUE_AMOUNT or amount == DUE_AMOUNT:
            print(f'Change Owed: {amount - DUE_AMOUNT}')
            break


def get_coins():
    c = int(input(f'Insert Coin: '))
    match c:
        case 25 | 10 | 5:
            return c
        case _:
            return 0


if __name__ == '__main__':
    main()
