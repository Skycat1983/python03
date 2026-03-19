# This exercise requires the use of dictionaries to store inventory
# data with nested structures (items containing name, type, quantity,
# value). You must use dict methods like keys(), values(), items(),
# get(), and update() to manage the inventory.
if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, dict[str, int | str]] = {

        "potion": {
            "name": "potion",
            "type": "consumable",
            "quantity": 5,
            "value": 10,
        },
        "armor": {
            "name": "armor",
            "type": "armor",
            "quantity": 3,
            "value": 80,
        },
        "shield": {
            "name": "shield",
            "type": "armor",
            "quantity": 2,
            "value": 40,
        },
        "sword": {
            "name": "sword",
            "type": "weapon",
            "quantity": 1,
            "value": 50,
        },
        "helmet": {
            "name": "helmet",
            "type": "armor",
            "quantity": 1,
            "value": 25,
        },
    }

    total_items = 0
    for item in inventory.values():
        total_items += item["quantity"]

    print(f"Total items in inventory: {total_items}")
    unique_item_types = len(inventory.keys())
    print(f"Unique item types: {unique_item_types}")
    print("\n=== Current Inventory ===")

    for name, item in inventory.items():
        quantity = item["quantity"]
        percent = quantity / total_items * 100

        unit = "unit" if quantity == 1 else "units"

        print(f"{name}: {quantity} {unit} ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most_name = ""
    most_qty = -1

    least_name = ""
    least_qty = float("inf")

    for name, item in inventory.items():
        quantity = item["quantity"]

        if quantity > most_qty:
            most_qty = quantity
            most_name = name

        if quantity < least_qty:
            least_qty = quantity
            least_name = name

    print(f"Most abundant: {most_name} ({most_qty} units)")
    print(f"Least abundant: {least_name} ({least_qty} units)")
    print("\n=== Item Categories ===")

    categories: dict[str, dict[str, int]] = {
        "Moderate": {},
        "Scarce": {},
    }

    for name, item in inventory.items():
        quantity = item["quantity"]

        if quantity >= 5:
            categories["Moderate"][name] = quantity
        else:
            categories["Scarce"][name] = quantity

    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    print("\n=== Management Suggestions ===")

    restock = []

    for name, item in inventory.items():
        if item["quantity"] <= 1:
            restock.append(name)

    print(f"Restock needed: {', '.join(restock)}")
    print("\n=== Dictionary Properties Demo ===")

    keys = ", ".join(inventory.keys())
    print(f"Dictionary keys: {keys}")

    values = ", ".join(str(item["quantity"]) for item in inventory.values())
    print(f"Dictionary values: {values}")

    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
