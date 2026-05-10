from person import Person
from vault import Vault


class Student(Person):
    def __init__(self, name, house, patronus=None, galleons=0, sickles=0, knuts=0):
        super().__init__(name)
        self.house = house
        self.patronus = patronus
        self.vault = Vault(galleons, sickles, knuts)

    @classmethod
    def get(cls, name, house):
        return cls(name, house)

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing Name")
    #     self.__name = name

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.__house = house

    def set_patronus(self, patronus):
        self.patronus = patronus

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

    def update_vault(self, galleons=0, sickles=0, knuts=0):
        self.vault.galleons = galleons
        self.vault.sickles = sickles
        self.vault.knuts = knuts

    def __str__(self):
        return f"{self.name} From {self.house}"
