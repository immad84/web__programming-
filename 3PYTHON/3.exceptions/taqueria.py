def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    
    get_total(menu)
    
def get_total(menu):
    total_price = 0
    while True:
        try:
            item = input('Item: ').title()
            # price = menu.get(item, 'Unknown')
            price = menu[item]
            total_price += price
        except KeyError:
            pass
        except EOFError:
            print()
            return total_price
        else:
            print(f'Total: ${total_price:.2f}')

if __name__ == '__main__':
    main()
