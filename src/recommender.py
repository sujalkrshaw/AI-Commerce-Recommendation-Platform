import heapq

class RecommendationEngine:


 def __init__(self, products):
    self.products = products

 def calculate_popularity(self, users):

    popularity = {}

    for user in users.values():

        interactions = (
            user.purchase_history
            + user.search_history
            + user.cart_items
        )

        for product_id in interactions:

            popularity[product_id] = (
                popularity.get(product_id, 0) + 1
            )

    return popularity

 def get_favorite_category(self, user):

    category_count = {}

    for product_id in user.purchase_history:

        if product_id in self.products:

            category = self.products[product_id].category

            category_count[category] = (
                category_count.get(category, 0) + 1
            )

    if not category_count:
        return None

    return max(
        category_count,
        key=category_count.get
    )

 def similarity_score(self, user1, user2):

    purchases1 = set(user1.purchase_history)
    purchases2 = set(user2.purchase_history)

    return len(
        purchases1.intersection(purchases2)
    )

 def generate_reason(self, user):

    reasons = []

    if user.purchase_history:
        reasons.append(
            "Based on your purchase history"
        )

    if user.search_history:
        reasons.append(
            "Matches your search interests"
        )

    reasons.append(
        "Popular among similar users"
    )

    return reasons

 def recommend(
    self,
    user,
    users,
    top_n=5
):

    popularity_scores = (
        self.calculate_popularity(users)
    )

    favorite_category = (
        self.get_favorite_category(user)
    )

    interacted_products = set(
        user.purchase_history
        + user.search_history
        + user.cart_items
    )

    scores = {}

    for product_id, product in self.products.items():

        if product_id in interacted_products:
            continue

        score = 0

        if (
            favorite_category
            and product.category == favorite_category
        ):
            score += 3

        score += product.rating * 2

        score += popularity_scores.get(
            product_id,
            0
        )

        for other_user in users.values():

            if other_user.user_id != user.user_id:

                score += self.similarity_score(
                    user,
                    other_user
                )

        scores[product_id] = score

    top_products = heapq.nlargest(
        top_n,
        scores.items(),
        key=lambda x: x[1]
    )

    recommendations = []

    for product_id, score in top_products:

        recommendations.append(
            {
                "product": self.products[product_id],
                "score": round(score, 2),
                "reason": self.generate_reason(user)
            }
        )

    return recommendations

