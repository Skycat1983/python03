import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for parameter in sys.argv[1:]:
        parts = parameter.split(":")

        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item_name, quantity_text = parts

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item_name, quantity in inventory.items():
        percent = round(quantity / total_quantity * 100, 1)
        print(f"Item {item_name} represents {percent}%")

    most_name = ""
    most_quantity = -1
    least_name = ""
    least_quantity = 0

    for item_name, quantity in inventory.items():
        if quantity > most_quantity:
            most_name = item_name
            most_quantity = quantity

        if least_name == "" or quantity < least_quantity:
            least_name = item_name
            least_quantity = quantity

    print(
        f"Item most abundant: {most_name} "
        f"with quantity {most_quantity}"
    )
    print(
        f"Item least abundant: {least_name} "
        f"with quantity {least_quantity}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
