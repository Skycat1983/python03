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
