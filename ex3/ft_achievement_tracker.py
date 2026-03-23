# This exercise requires the use of sets to store unique achievements and perform operations
# (union, intersection, difference) to analyze achievement collections across players.

# Create a function gen_player_achievements() that will use a large fixed list of achieve-
# ments to randomly assign a set to a player. Choose a random number of achievements,
# then pick this number of achievements from the list to build and return the set.

# Authorized: len(), print(), import random, random.*, set(), set.union(),
# set.intersection(), set.difference()
import random


def gen_player_achievements(a_list: list[str]) -> set:
    num = random.randrange(len(a_list) + 1)
    a_set = set()
    while (len(a_set) < num):
        r_a = random.choice(a_list)
        a_set.add(r_a)
    return (a_set)


def gen_players(p_list: list[str], num: int) -> set:
    p_set = set()
    while (len(p_set) < num):
        r_p = random.choice(p_list)
        p_set.add(r_p)
    return (p_set)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan", "Eve", "Fi", "Geb"]
    achievements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder"
    ]
    players = gen_players(names, 4)
    player_achievements = {}

    for player in players:
        player_achievements[player] = gen_player_achievements(achievements)
        print(f"Player {player}: {player_achievements[player]}")

    unique_achievements = set(achievements)
    print()
    print(f"All distincet achievements: {unique_achievements}")
    common_achievements = None

    for player in player_achievements:
        if common_achievements is None:
            common_achievements = player_achievements[player]
        else:
            common_achievements = set.intersection(
                common_achievements,
                player_achievements[player]
            )
    print()
    print(f"Common achievements: {common_achievements}\n")
    all_achievements = set()
    for player in player_achievements:
        all_achievements = set.union(all_achievements, player_achievements[player])

    for player in player_achievements:
        other_union = set()
        for other_player in player_achievements:
            if other_player != player:
                other_union = set.union(other_union, player_achievements[other_player])
        only_player = set.difference(player_achievements[player], other_union)
        print(f"Only {player} has: {only_player}")

    print()

    for player in player_achievements:
        missing = set.difference(all_achievements, player_achievements[player])
        print(f"{player} is missing: {missing}")
