class Product:
    """
    A class representing a product in a store.

    The Product class stores information about a single product,
    including its name, price, quantity, and active status. It provides
    methods to check availability, update stock, display details, and
    process purchases.

    Attributes:
        name (str): The name of the product. Cannot be empty.
        price (float): The price of the product. Must be non-negative.
        quantity (int): The number of items in stock. Must be non-negative.
        active (bool): Indicates whether the product is available for sale.

    Methods:
        get_quantity() -> int:
            Returns the current quantity of the product in stock.
        set_quantity(quantity: int):
            Updates the product quantity. Deactivates the product if quantity is 0.
        is_active() -> bool:
            Returns True if the product is active, False otherwise.
        activate():
            Reactivates the product if quantity > 0.
        show() -> str:
            Returns a string representation of the product details.
        buy(quantity: int) -> float:
            Reduces the stock by the specified quantity and returns the total price.
            Raises an exception if quantity is invalid or exceeds available stock.
    """
    def __init__(self, name: str, price: float, quantity: int):
        # Check
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")


        # Instance Variable
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return current quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Update quantity (cannot be negative). Deactivate if zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Reactivate product (if quantity > 0"""
        if self.quantity > 0:
            self.active = True

    def show(self):
        """Return product details as a string"""
        return (f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, "
                f"Active: {self.active}")

    def buy(self, quantity) -> float:
        """Buy given quantity of the product.
        Reduce stock and return total price.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price