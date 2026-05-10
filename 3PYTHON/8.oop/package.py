class Package:
    def __init__(self, id, sender, receipent, weight):
        self.id = id
        self.sender = sender
        self.receipent = receipent
        self.weight = weight

    def __str__(self):
        return f"Package {self.id}: {self.sender} to {self.receipent}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
        Package(id=1, sender="Harry", receipent="Bob", weight=10),
        Package(id=2, sender="Weasley", receipent="Draco", weight=5),
    ]

    for package in packages:
        print(f"{package}, costs ${package.calculate_cost(2)}")


if __name__ == "__main__":
    main()
