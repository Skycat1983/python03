import random
from typing import Generator


def gen_event(
    names: list[str],
    actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(names), random.choice(actions)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        idx = random.randrange(len(events))
        yield events.pop(idx)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    names: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    event_gen: Generator[tuple[str, str], None, None] = gen_event(
        names,
        actions,
    )

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_tuples: list[tuple[str, str]] = []
    for _ in range(10):
        ten_tuples.append(next(event_gen))

    print(f"Built list of 10 events: {ten_tuples}")

    for event in consume_event(ten_tuples):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_tuples}")
