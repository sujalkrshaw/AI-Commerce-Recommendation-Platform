class Product:
    """
    Represents a product in the e-commerce system.
    """

    def __init__(
        self,
        product_id,
        name,
        category,
        price,
        rating,
        image_url=""
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating
        self.image_url = image_url

    def to_dict(self):
        """
        Convert product object to dictionary.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "rating": self.rating,
            "image_url": self.image_url
        }

    def __str__(self):
        """
        String representation of product.
        """
        return (
            f"ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Price: ₹{self.price} | "
            f"Rating: {self.rating}"
        )