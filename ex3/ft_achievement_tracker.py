import random


def gen_player_achievements(a_list: list[str]) -> set:
    num = random.randrange(1, len(a_list) + 1)
    a_set = set()
    while len(a_set) < num:
        a_set.add(random.choice(a_list))
    return a_set


def gen_players(p_list: list[str], num: int) -> set:
    p_set = set()
    while len(p_set) < num:
        p_set.add(random.choice(p_list))
    return p_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
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
    print(f"All distinct achievements: {unique_achievements}")
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
        all_achievements = set.union(
            all_achievements,
            player_achievements[player]
        )

    for player in player_achievements:
        other_union = set()
        for other_player in player_achievements:
            if other_player != player:
                other_union = set.union(
                    other_union,
                    player_achievements[other_player]
                )
        only_player = set.difference(player_achievements[player], other_union)
        print(f"Only {player} has: {only_player}")

    print()

    for player in player_achievements:
        missing = set.difference(all_achievements, player_achievements[player])
        print(f"{player} is missing: {missing}")
