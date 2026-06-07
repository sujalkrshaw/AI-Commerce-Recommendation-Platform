from src.product import Product
from src.user import User
from src.recommender import RecommendationEngine
from src.report_generator import ReportGenerator
from src.sample_users import create_users


def create_products():
    products = {
        101: Product(101, "Wireless Mouse", "Electronics", 799, 4.7),
        102: Product(102, "Mechanical Keyboard", "Electronics", 2499, 4.8),
        103: Product(103, "Laptop Stand", "Electronics", 999, 4.5),
        104: Product(104, "USB Hub", "Electronics", 699, 4.4),
        105: Product(105, "Gaming Headset", "Electronics", 1999, 4.6),
        106: Product(106, "Running Shoes", "Fashion", 2999, 4.5),
        107: Product(107, "T-Shirt", "Fashion", 599, 4.2),
        108: Product(108, "Jeans", "Fashion", 1499, 4.4),
        109: Product(109, "Water Bottle", "Sports", 499, 4.3),
        110: Product(110, "Yoga Mat", "Sports", 899, 4.6),
        111: Product(111, "Cricket Bat", "Sports", 2499, 4.7),
        112: Product(112, "Smart Watch", "Electronics", 3999, 4.8),
    }

    return products




def display_products(products):

    print("\nAVAILABLE PRODUCTS\n")

    for product in products.values():
        print(product)


def display_users(users):

    print("\nREGISTERED USERS\n")

    for user in users.values():
        print("-" * 50)
        print(user)


def generate_recommendations(engine, users):

    try:

        user_id = int(input("\nEnter User ID: "))

        if user_id not in users:
            print("User not found.")
            return

        recommendations = engine.recommend(
            users[user_id],
            users,
            top_n=5
        )

        print("\nTOP RECOMMENDATIONS\n")

        for index, item in enumerate(
            recommendations,
            start=1
        ):

            product = item["product"]

            print(
                f"{index}. "
                f"{product.name} | "
                f"{product.category} | "
                f"Score: {item['score']}"
            )

        report_path = ReportGenerator.generate_report(
            users[user_id],
            recommendations
        )

        print(
            f"\nReport Generated Successfully:\n"
            f"{report_path}"
        )

    except ValueError:
        print("Invalid input.")


def main():

    from src.database_manager import DatabaseManager

    db = DatabaseManager()

    products = db.load_products()

    users = create_users()

    engine = RecommendationEngine(products)

    while True:

        print("\n" + "=" * 40)
        print("E-COMMERCE RECOMMENDATION ENGINE")
        print("=" * 40)

        print("1. View Products")
        print("2. View Users")
        print("3. Get Recommendations")
        print("4. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            display_products(products)

        elif choice == "2":
            display_users(users)

        elif choice == "3":
            generate_recommendations(
                engine,
                users
            )

        elif choice == "4":
            print("\nThank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()