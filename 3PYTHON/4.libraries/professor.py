import random
import sys


def main():
    level = get_level()
    score = 0
    for _ in range(1, 11):
        try:
            x = generate_integer(level)
            y = generate_integer(level)

            for i in range(1, 4):
                try:
                    answer = int(input(f"{x} + {y} = "))
                    if answer == x + y:
                        score += 1
                        break
                    elif i == 3:
                        print(f"{x} + {y} = {x + y}")
                    else:
                        raise ValueError("")
                except ValueError:
                    print("EEE")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit()
            
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0 or n >= 4:
                continue
            return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
