# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 14:11:30 by helaouta          #+#    #+#              #
#    Updated: 2026/03/16 14:14:06 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import sys
import math

# ! check erros handling messages. 

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