from src.database_manager import DatabaseManager


def seed_products():

    db = DatabaseManager()

    db.create_tables()

    products = [
        (101, "Wireless Mouse", "Electronics", 799, 4.7),
        (102, "Mechanical Keyboard", "Electronics", 2499, 4.8),
        (103, "Laptop Stand", "Electronics", 999, 4.5),
        (104, "USB Hub", "Electronics", 699, 4.4),
        (105, "Gaming Headset", "Electronics", 1999, 4.6),
        (106, "Running Shoes", "Fashion", 2999, 4.5),
        (107, "T-Shirt", "Fashion", 599, 4.2),
        (108, "Jeans", "Fashion", 1499, 4.4),
        (109, "Water Bottle", "Sports", 499, 4.3),
        (110, "Yoga Mat", "Sports", 899, 4.6),
        (111, "Cricket Bat", "Sports", 2499, 4.7),
        (112, "Smart Watch", "Electronics", 3999, 4.8)
    ]

    for product in products:

        db.insert_product(
            product[0],
            product[1],
            product[2],
            product[3],
            product[4]
        )

    print("✅ Database Seeded Successfully")

    db.close()


if __name__ == "__main__":
    seed_products()