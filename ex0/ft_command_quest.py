# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: helaouta <helaouta@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 11:30:33 by helaouta          #+#    #+#              #
#    Updated: 2026/03/16 11:50:05 by helaouta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Authorized: sys, sys.argv, len(), print()
# Your Quest: Build a simple command interpreter that shows you’ve mastered the art
# of receiving external data.
# What makes this magical:
# • Discover how programs can receive information from the command line
# • Learn to process different types of input data
# • Handle cases where no information is provided
# • Display information in a user-friendly way
# Power-up tip: Every program is like a character in an RPG—it needs to know what
# the player wants it to do. The command line is how players communicate their wishes!

def print_value(label: str, value) -> None:
    print(f"{label.title()}: {value}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    argc = len(sys.argv)

    print_value("program name", sys.argv[0])

    if argc > 1:
        print_value("arguments received", argc - 1)
        i = 1
        while i < argc:
            print_value(f"argument {i}", sys.argv[i])
            i += 1
    else:
        print("No arguments provided!")

    print_value("total arguments", argc)


    
# $> python3 ft_command_quest.py
# === Command Quest ===
# No arguments provided!
# Program name: ft_command_quest.py
# Total arguments: 1
# $> python3 ft_command_quest.py hello world 42
# === Command Quest ===
# Program name: ft\_command\_quest.py
# Arguments received: 3
# Argument 1: hello
# Argument 2: world
# Argument 3: 42
# Total arguments: 4
# $> python3 ft_command_quest.py "Data Quest"
# === Command Quest ===
# Program name: ft_command_quest.py
# Arguments received: 1
# Argument 1: Data Quest
# Total arguments: 2