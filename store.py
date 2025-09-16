from typing import List, Tuple
from products import Product  # class Product in products.py


class Store:
    """
    A class that represents a store containing multiple products.

    The Store class manages an inventory of Product objects,
    allows adding and removing products, and provides utility
    methods to retrieve available products, total quantities,
    and to process customer orders.

    Attributes:
        products (List[Product]): A list of Product objects available in the store.

    Methods:
        add_product(product: Product):
            Add a product to the store.
        remove_product(product: Product):
            Remove a product from the store if it exists.
        get_total_quantity() -> int:
            Return the total quantity of all products in the store.
        get_all_products() -> List[Product]:
            Return all products that are currently active (available for purchase).
        order(shopping_list: List[Tuple[Product, int]]) -> float:
            Accepts a shopping list of (Product, quantity) tuples,
            validates availability, processes the purchase, and returns
            the total price of the order.
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

