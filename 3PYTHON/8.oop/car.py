class Car:
    def __init__(self, make, model, year, odo_meter=0):
        self.make = make
        self.model = model
        self.year = year
        self.odo_meter = odo_meter

    @property
    def odo_meter(self):
        return self.__odo_meter

    @odo_meter.setter
    def odo_meter(self, odo_meter):
        if odo_meter < 0:
            raise ValueError("Invalid Valud")
        self.__odo_meter = odo_meter

    @classmethod
    def get_car(cls, make, model, year):
        return cls(make, model, year)

    def get_descriptive_name(self):
        print(f"{self.year} {self.make} {self.model}")

    def read_odo_meter(self):
        return f"The car has {self.odo_meter:,} miles on it."

    def update_odo_meter(self, milage):
        if not milage >= self.odo_meter:
            raise ValueError("Invalid Milage Enterd.")
        self.odo_meter = milage

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


def main():
    car = Car.get_car("audi", "a4", 2019)
    print(car)
    car.update_odo_meter(10000)
    print(car.read_odo_meter())


if __name__ == "__main__":
    main()
