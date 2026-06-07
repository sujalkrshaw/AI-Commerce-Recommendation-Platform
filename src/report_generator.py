import os
from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate_report(user, recommendations):

        os.makedirs("outputs", exist_ok=True)

        report_path = "outputs/recommendation_report.txt"

        with open(report_path, "w", encoding="utf-8") as file:

            file.write("=" * 50 + "\n")
            file.write("E-COMMERCE RECOMMENDATION REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write(
                f"Generated On: "
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            file.write(f"User ID: {user.user_id}\n")
            file.write(f"User Name: {user.name}\n\n")

            file.write("PURCHASE HISTORY\n")
            file.write("-" * 30 + "\n")

            if user.purchase_history:
                for product_id in user.purchase_history:
                    file.write(f"{product_id}\n")
            else:
                file.write("No purchases found.\n")

            file.write("\n")

            file.write("SEARCH HISTORY\n")
            file.write("-" * 30 + "\n")

            if user.search_history:
                for product_id in user.search_history:
                    file.write(f"{product_id}\n")
            else:
                file.write("No searches found.\n")

            file.write("\n")

            file.write("CART ITEMS\n")
            file.write("-" * 30 + "\n")

            if user.cart_items:
                for product_id in user.cart_items:
                    file.write(f"{product_id}\n")
            else:
                file.write("No cart items found.\n")

            file.write("\n")

            file.write("TOP RECOMMENDATIONS\n")
            file.write("-" * 30 + "\n")

            for index, item in enumerate(
                recommendations,
                start=1
            ):

                product = item["product"]

                file.write(
                    f"{index}. {product.name}\n"
                )

                file.write(
                    f"   Category: "
                    f"{product.category}\n"
                )

                file.write(
                    f"   Rating: "
                    f"{product.rating}\n"
                )

                file.write(
                    f"   Score: "
                    f"{item['score']}\n\n"
                )

            file.write("=" * 50 + "\n")

        return report_path