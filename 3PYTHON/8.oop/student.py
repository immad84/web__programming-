class Student:
    # can do error checking
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    @classmethod
    def get(cls, name, house):
        return cls(name, house)

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    name = input("Name: ")
    house = input("House: ")
    student = Student.get(name, house)
    print(student)


if __name__ == "__main__":
    main()
