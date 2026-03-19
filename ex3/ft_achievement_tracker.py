# This exercise requires the use of sets to store unique achievements
# ! and set operations (union, intersection, difference) to analyze
# achievement collections across players.
# ! double check if bitwise is allowed
if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    shared_by_at_least_two = (
        alice.intersection(bob)
        .union(alice.intersection(charlie))
        .union(bob.intersection(charlie))
    )

    rare = all_achievements.difference(shared_by_at_least_two)
    print(f"Rare achievements (1 player): {rare}")

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")
