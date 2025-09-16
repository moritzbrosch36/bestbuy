class Product:
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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

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