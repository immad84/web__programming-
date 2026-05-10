import inflect


def main():
    names = get_names()
    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(names)}")


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break
    return names


if __name__ == "__main__":
    main()
