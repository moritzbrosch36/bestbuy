from products import Product
from store import Store

"""
main.py
________
This module provides a simple command-line interface (CLI) for interacting with
the Store and Product classes. It allows the user to list products, check total
inventory quantity, place an order and exit the program.
"""

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price = 1450, quantity = 100),
    Product("Bose QuietComfort Earbuds", price = 250, quantity = 500),
    Product("Google Pixel 7", price = 500, quantity = 250)
]
best_buy = Store(product_list)


def start(store: Store):
    """
    Start the interactive menu for the given store.

    Args:
    store (Store): The store object containing available products.

    Menu Options:
        1. List all products in store
        2. Show total amount in store
            - Display the total quantity of all products in stock.
        3. Make an order
            - Allows the user to choose products by number and specify a quantity.
              The user can keep adding items until they provide empty input.
              When finished, the total cost of the order is calculated and displayed.
        4. Quit
            - Exits the program.
    The function runs in a loop until the user selects option 4.
    """
    while True:
        print("\n===== Best Buy Store Menu =====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable products:")
            for idx, product in enumerate(store.get_all_products(), start = 1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            print("\nTotal quantity in store:", store.get_total_quantity())


        elif choice == "3":
            products = store.get_all_products()
            if not products:
                print("⚠️No products available in store.")
                continue

            print("------")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.name}, "
                      f"Price: ${product.price}, "
                      f"Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            while True:
                selection = input("Which product do you want? ")
                if selection.strip() == "":
                    break  # empty input → complete order

                if not selection.isdigit():
                    print("⚠️Please enter a valid product number.")
                    continue

                selection = int(selection)
                if selection < 1 or selection > len(products):
                    print("❌Invalid product number.")
                    continue

                try:
                    quantity_str = input("What amount do you want? ")
                    if not quantity_str.isdigit():
                        print("❌Invalid quantity, please enter a number.")
                        continue
                    quantity = int(quantity_str)

                    shopping_list.append((products[selection - 1], quantity))
                    print("Product added to list!\n")
                except ValueError:
                    print("❌Invalid input. Please enter a number.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print("********")
                    print(f"✅Order made! Total payment: ${total_price}")
                except ValueError as e:
                    print("❌Order failed:", e)

        elif choice == "4":
            print("\nThank you for visiting Best Buy 👋")
            break

        else:
            print("❌Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    start(best_buy)
