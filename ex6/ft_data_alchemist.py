# Authorized: import random, random.*, print(), len(), sum(), round()


# This exercise requires the use of list and dictionary comprehensions to transform and
# filter data efficiently. These are fundamental Python features for data processing.
# Create a list of player names, where some are capitalized and others are not. 
# ! Build two list comprehensions: the first one creates a new list with all names capitalized, 
# ! the second one creates a new list with only the capitalized names from the initial list.
# Now, let’s create a dictionary from this full capitalized list of player names. Names will
# be the keys, and values will be randomly generated scores in a defined range. Of course, a
# comprehension will build this dictionary. Then a second dict will be created, with scores
# higher than the average, also using a comprehension.


# $> python3 ft_data_alchemist.py
# === Game Data Alchemist ===
# Initial list of players: ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam
# ']
# New list with all names capitalized: ['Alice', 'Bob', 'Charlie', 'Dylan', 'Emma', 'Gregory', 'John', '
# Kevin', 'Liam']
# New list of capitalized names only: ['Alice', 'Charlie', 'Emma', 'Gregory', 'Liam']
# Score dict: {'Alice': 263, 'Bob': 666, 'Charlie': 907, 'Dylan': 170, 'Emma': 568, 'Gregory': 446, 'John
# ': 90, 'Kevin': 527, 'Liam': 54}
# Score average is 410.11
# High scores: {'Bob': 666, 'Charlie': 907, 'Emma': 568, 'Gregory': 446, 'Kevin': 527}

import random


def gen_score(lower: int, upper: int) -> int:
    return (random.randint(lower, upper))


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]
    capitalised: list[str] = [player.title() for player in players]
    already_capitalised: list[str] = [player for player in players if player.istitle()]
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalised}")
    print(f"New list of capitalized names only {already_capitalised}")
    print()
    gen = gen_score(1, 100)
    dict_1: dict[str, int] = {name: random.randint(1, 100) for name in capitalised}
    print(f"Score doct: {dict_1}")
    # score = dict_1 
    total = sum(dict_1[score] for score in dict_1)
    average = total / len(dict_1)
    print(f"Score average: {average}")


