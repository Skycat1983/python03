# Mission Briefing: Now that you’ve mastered command communication, time for your
# first real data quest! The PixelMetrics 3000 needs a Score Cruncher module. Think of it
# like the leaderboard system in your favorite game—but you’re building the engine that
# powers it!
# Your mission (should you choose to accept it):
# • Accept player scores from the command line (like cheat codes, but legal!)
# • Use lists to store and organize the scores
# • Calculate some basic stats that would make any game dev happy
# • Handle the "oops, I typed ’banana’ instead of ’1000’" scenarios gracefully
# • Make the output look cool enough to impress your gaming buddies
# Power-up tip: Lists are like your inventory in an RPG—you can add items, count them,
# find the best one, and organize them however you want!
# python3 ft_score_analytics.py 1500 2300 1800 2100 1950
# 10

import sys


# ? should this be rounding decimals?
# ? should i print the error or raise it?
def validate_int(n: str) -> int:
    try:
        return int(n)
    except ValueError:
        raise ValueError(f"Value {n} is not an int")

# ? should i use 'try' here too?
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    i = 1
    scores: list[int] = []

    while i < argc:
        scores.append(validate_int(sys.argv[i]))
        i += 1

    if len(scores):
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")





# Data Quest Mastering Python Collections for Data Engineering
# $> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
# === Player Score Analytics ===
# Scores processed: [1500, 2300, 1800, 2100, 1950]
# Total players: 5
# Total score: 9650
# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800
# $> python3 ft_score_analytics.py
# === Player Score Analytics ===
# No scores provided. Usage: python3 ft_score_analytics.py <score1> <sc