from student import Student


def main():
    harry = get_student()
    harry.update_vault(120, 30, 25)
    print(harry.vault)
    weasley = get_student()
    weasley.update_vault(22, 11, 1)
    print(weasley.vault)
    total = harry.vault + weasley.vault
    print(total)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student.get(name, house)


if __name__ == "__main__":
    main()
