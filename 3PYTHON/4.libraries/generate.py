# from random import choice, choices, randint, shuffle
import random

# choice = random.choice(["head", "tail"])
# print(choice)

cards = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
# random.seed(10)
choices = random.choices(cards, k=5)
print(choices)
cards = ['King', 'Queen', 'Jack']
choices = random.choices(cards,weights=[75, 50, 50], k=3)
print(choices)

# Sampling Without Replacement
choices = random.sample(['Alpha', 'Beta', 'Charli'], k = 3)
print(choices)

number = random.randint(1, 10)
print(number)

# cards = ["King", "Queen", "Jack"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
