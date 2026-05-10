def main():
    grocery = get_grocery_list()
    for item in sorted(grocery):
        print(grocery[item], item.upper())

def get_grocery_list():
    list = {}
    while True:
        try:
            item = input('')
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            print()
            return list

if __name__ == '__main__':
    main()