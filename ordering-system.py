menu = {
    1: {"name": "espresso", "price": 1.99},
    2: {"name": "coffee", "price": 2.50},
    3: {"name": "cake", "price": 2.79},
    4: {"name": "soup", "price": 4.50},
    5: {"name": "sandwich", "price": 4.99}
}

TAX_RATE = 0.15


def calculate_subtotal(order):
    return round(sum(item["price"] for item in order), 2)


def calculate_tax(subtotal):
    return round(subtotal * TAX_RATE, 2)


def summarize_order(order):
    names = [item["name"] for item in order]
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)

    return names, subtotal, tax, total


def print_order(order):
    print(f"You have ordered {len(order)} items")

    for item in order:
        print(f"Item: {item['name']}, Price: ${item['price']:.2f}")


def display_menu():
    print("------- Menu -------")

    for number, item in menu.items():
        print(f"{number}. {item['name']:<9} | ${item['price']:>5.2f}")

    print()


def take_order():
    display_menu()
    order = []

    for count in range(1, 4):
        selection = int(
            input(f"Select menu item number {count} (from 1 to 5): ")
        )
        order.append(menu[selection])

    return order


def main():
    order = take_order()
    print_order(order)

    names, subtotal, tax, total = summarize_order(order)

    print(f"Subtotal for the order is: ${subtotal:.2f}")
    print(f"Tax for the order is: ${tax:.2f}")
    print(f"Order summary: Items: {names}, Total: ${total:.2f}")


if __name__ == "__main__":
    main()