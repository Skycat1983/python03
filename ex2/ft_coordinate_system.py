import sys


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

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    argc = len(sys.argv)
    if (argc == 1):
        x1 = 10
        x2 = 20
        x3 = 5
        x_pos = tuple(x1, x2, x3)
    input("")



# $> python3 ft_coordinate_system.py
# === Game Coordinate System ===
# Position created: (10, 20, 5)
# Distance between (0, 0, 0) and (10, 20, 5): 22.91
# Parsing coordinates: "3,4,0"
# Parsed position: (3, 4, 0)
# Distance between (0, 0, 0) and (3, 4, 0): 5.0
# Parsing invalid coordinates: "abc,def,ghi"
# Error parsing coordinates: invalid literal for int() with base 10: 'abc'
# Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: 'abc'",)
# Unpacking demonstration:
# Player at x=3, y=4, z=0
# Coordinates: X=3, Y=4, Z=0