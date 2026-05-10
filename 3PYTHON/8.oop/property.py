class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        self.patronus = patronus

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.__name = name

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid House.")
        self.__house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

    def set_patronus(self, patronus):
        self.patronus = patronus

    @classmethod
    def get(cls, name, house):
        return cls(name, house)

    def __str__(self):
        return f"{self.name} From {self.house}"


def main():
    name = input("Name: ")
    house = input("House: ")
    student = Student.get(name, house)
    print(student)
    student.set_patronus("Otter")
    # student.house = 'Number Four, Priver Drive'
    print(student.charm())


if __name__ == "__main__":
    main()
