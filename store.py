from typing import List, Tuple
from products import Product  # class Product in products.py


class Store:
    """
    Start the interactive console menu for the store.

    Args:
        store (Store): An instance of the Store class containing available products.

    The menu provides the following options:
        1. List all products in the store.
        2. Show the total quantity of items in the store.
        3. Make an order by selecting products and quantities.
        4. Quit the program.

    Behavior:
        - If option 1 is chosen, all active products with details will be listed.
        - If option 2 is chosen, the sum of all available quantities will be shown.
        - If option 3 is chosen, the user can build an order by repeatedly selecting
          product numbers and quantities until they finish. The program then calculates
          and displays the total order cost.
        - If option 4 is chosen, the program will exit gracefully.

    Input validation:
        - Ensures menu choices are between 1 and 4.
        - Ensures product selections and quantities are valid numbers.
        - Prevents invalid or empty orders from being processed.
    """
    def __init__(self, products: List[Product] = None):
        """Initialize store with an optional list of products."""
        self.products = products if products else []

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Accepts a list of tuples (Product, quantity).
        Buys the products and returns the total price.
        """
        total_price = 0.0

        # Erste Validierung: check ob alle Bestellungen möglich sind
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} not found in store.")
            if quantity > product.get_quantity():
                raise ValueError(
                    f"Not enough stock of {product.name}. Requested {quantity}, available {product.get_quantity()}."
                )

        # Wenn alles passt → Bestellung ausführen
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

