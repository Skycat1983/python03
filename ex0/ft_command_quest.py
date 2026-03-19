import sys

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
