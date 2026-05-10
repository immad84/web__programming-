class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = n

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("Invalid Size")
        self.__size = size

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        total_cookies = self.size + n
        if n < 0 or total_cookies > self.capacity:
            raise ValueError("Cannot deposit, over capacity")
        self.size += n

    def withdraw(self, n):
        if n < 0 or n > self.size:
            raise ValueError("Cannot withdraw, not enough cookies")
        self.size -= n

def main():
    jar = Jar(capacity=10)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)

if __name__ == '__main__':
    main()
