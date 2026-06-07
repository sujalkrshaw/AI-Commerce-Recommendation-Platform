class User:
    """
    Represents a user in the e-commerce system.
    """

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        self.purchase_history = []
        self.search_history = []
        self.cart_items = []

    def add_purchase(self, product_id):
        """
        Add purchased product.
        """
        self.purchase_history.append(product_id)

    def add_search(self, product_id):
        """
        Add searched product.
        """
        self.search_history.append(product_id)

    def add_to_cart(self, product_id):
        """
        Add product to cart.
        """
        self.cart_items.append(product_id)

    def to_dict(self):
        """
        Convert user object to dictionary.
        """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "purchase_history": self.purchase_history,
            "search_history": self.search_history,
            "cart_items": self.cart_items
        }

    def __str__(self):
        """
        String representation of user.
        """
        return (
            f"User ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Purchases: {self.purchase_history}\n"
            f"Searches: {self.search_history}\n"
            f"Cart: {self.cart_items}"
        )