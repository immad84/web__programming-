import random


def main():
    n = get_input("Level: ")
    rand_number = random.randint(1, n)
    play_game(rand_number)


def play_game(rand):
    while True:
        try:
            guess = get_input("Guess: ")
            if guess < rand:
                print("Too small!")
            elif guess > rand:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass


def get_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
