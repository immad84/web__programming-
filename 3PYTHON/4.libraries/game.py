import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if is_negative(n):
                continue
        except ValueError:
            pass
        else:
            rand_number = random.randint(1, n)
            check_guess(rand_number)
            break


def check_guess(rand):
    while True:
        try:
            guess = int(input("Guess: "))
            if is_negative(guess):
                continue
        except ValueError:
            pass
        else:
            if guess < rand:
                print("Too small!")
            elif guess > rand:
                print("Too large!")
            else:
                print("Just right!")
                break


def is_negative(n):
    return n <= 0


if __name__ == "__main__":
    main()
