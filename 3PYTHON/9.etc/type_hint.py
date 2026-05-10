def meow(n: int) -> str:
    """
    Meow n times.

    :param n :number of times to meow
    :type n:int
    :raise TypeError :if n is not int
    :return :a sting of meows
    :rtype str 
    """
    return "meow\n" * n

def main():
    number: int = int(input("n: "))
    meows: str = meow(number)
    print(meows, end="")

if __name__ == "__main__":
    main()