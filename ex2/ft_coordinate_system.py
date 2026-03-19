import sys
import math


def validate_int(n: str) -> int:
    try:
        return int(n)
    except ValueError:
        raise ValueError(f"Value {n} is not an int")


def parse_str(string: str) -> tuple[int, int, int]:
    parts = string.split(",")

    if len(parts) != 3:
        raise ValueError("Coordinates must contain exactly 3 values")

    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
    except ValueError:
        raise ValueError("Coordinates must be integers")

    return (x, y, z)


def calc_distance(
    abc: tuple[int, int, int],
    xyz: tuple[int, int, int]
) -> float:
    a, b, c = abc
    x, y, z = xyz
    return math.sqrt((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    argc = len(sys.argv)

    if argc == 1:
        abc = (0, 0, 0)
        xyz = (10, 20, 5)
        distance = calc_distance(abc, xyz)

        print(f"\nPosition created: {xyz}")
        print(f"Distance between {abc} and {xyz}: {distance:.2f}")

        print('\nParsing coordinates: "3,4,0"')
        parsed = parse_str("3,4,0")
        parsed_distance = calc_distance(abc, parsed)
        print(f"Parsed position: {parsed}")
        print(f"Distance between {abc} and {parsed}: {parsed_distance}")

        print('\nParsing invalid coordinates: "abc,def,ghi"')
        try:
            invalid = parse_str("abc,def,ghi")
            print(f"Parsed position: {invalid}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(
                f"Error details - Type: {type(e).__name__}, Args: {e.args}"
            )

        print("\nUnpacking demonstration:")
        x, y, z = parsed
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    else:
        try:
            parsed = parse_str(sys.argv[1])
            origin = (0, 0, 0)
            distance = calc_distance(origin, parsed)

            print(f"Parsed position: {parsed}")
            print(f"Distance between {origin} and {parsed}: {distance}")

            print("Unpacking demonstration:")
            x, y, z = parsed
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")

        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(
                f"Error details - Type: {type(e).__name__}, Args: {e.args}"
            )
