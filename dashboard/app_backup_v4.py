import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from streamlit_option_menu import option_menu

from src.database_manager import DatabaseManager
from src.sample_users import create_users
from src.recommender import RecommendationEngine

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Recommendation Platform",
    page_icon="🛒",
    layout="wide"
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

db = DatabaseManager()

products = db.load_products()

users = create_users()

engine = RecommendationEngine(products)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.main {
    padding-top: 0rem;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    selected = option_menu(
        menu_title="AI Platform",
        options=[
            "Executive Overview",
            "Product Intelligence",
            "Customer Intelligence",
            "AI Recommendation Lab",
            "Analytics",
            "System Health"
        ],
        icons=[
            "house",
            "box",
            "people",
            "cpu",
            "bar-chart",
            "gear"
        ],
        menu_icon="robot",
        default_index=0
    )

# ----------------------------------
# EXECUTIVE OVERVIEW
# ----------------------------------

if selected == "Executive Overview":

    st.title("🚀 AI Recommendation Platform")

    total_products = len(products)

    total_users = len(users)

    avg_rating = round(
        sum(
            product.rating
            for product in products.values()
        ) / total_products,
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Products",
            total_products
        )

    with col2:
        st.metric(
            "👥 Users",
            total_users
        )

    with col3:
        st.metric(
            "⭐ Avg Rating",
            avg_rating
        )

    with col4:
        st.metric(
            "🤖 AI Engine",
            "ONLINE"
        )

    st.markdown("---")

    st.subheader("Business Summary")

    st.info(
        f"""
        Product Catalog Size: {total_products}

        Active Users: {total_users}

        Average Product Rating: {avg_rating}

        Recommendation Engine Status: Active
        """
    )

# ----------------------------------
# PRODUCT INTELLIGENCE
# ----------------------------------

elif selected == "Product Intelligence":

    st.title("📦 Product Intelligence")

    product_data = []

    for product in products.values():

        product_data.append(
            {
                "ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Price": product.price,
                "Rating": product.rating
            }
        )

    df = pd.DataFrame(product_data)

    search = st.text_input(
        "🔍 Search Product"
    )

    if search:

        df = df[
            df["Name"]
            .str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )


# ----------------------------------
# CUSTOMER INTELLIGENCE
# ----------------------------------

elif selected == "Customer Intelligence":

    st.title("👥 Customer Intelligence")

    selected_user = st.selectbox(
        "Select User",
        [user.name for user in users.values()]
    )

    user = next(
        u
        for u in users.values()
        if u.name == selected_user
    )

    st.subheader("Customer Profile")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Purchases",
            len(user.purchase_history)
        )

    with metric2:
        st.metric(
            "Searches",
            len(user.search_history)
        )

    with metric3:
        st.metric(
            "Cart Items",
            len(user.cart_items)
        )

    def product_names(product_ids):

        names = []

        for product_id in product_ids:

            if product_id in products:

                names.append(
                    products[product_id].name
                )

        return names

    purchases = product_names(
        user.purchase_history
    )

    searches = product_names(
        user.search_history
    )

    cart = product_names(
        user.cart_items
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🛒 Purchases")

        for item in purchases:
            st.success(item)

    with col2:

        st.subheader("🔍 Searches")

        for item in searches:
            st.info(item)

    with col3:

        st.subheader("🛍 Cart")

        for item in cart:
            st.warning(item)




# ----------------------------------
# AI RECOMMENDATION LAB PRO
# ----------------------------------

elif selected == "AI Recommendation Lab":

    st.title("🤖 AI Recommendation Lab")

    selected_user_name = st.selectbox(
        "Choose User",
        [user.name for user in users.values()]
    )

    if st.button(
        "🚀 Generate Recommendations"
    ):

        selected_user = next(
            user
            for user in users.values()
            if user.name == selected_user_name
        )

        recommendations = engine.recommend(
            selected_user,
            users,
            top_n=5
        )

        st.success(
            f"{len(recommendations)} Recommendations Generated"
        )

        # -----------------------------
        # RECOMMENDATION CARDS
        # -----------------------------

        for rank, item in enumerate(
            recommendations,
            start=1
        ):

            product = item["product"]
            score = item["score"]

            confidence = min(
                round(score * 10),
                100
            )

            if score >= 10:
                status = "🔥 Strong Match"

            elif score >= 8:
                status = "🟡 Medium Match"

            else:
                status = "⚪ Low Match"

            st.markdown("---")

            st.subheader(
                f"🏆 Recommendation #{rank}"
            )

            col1, col2 = st.columns([3, 1])

            with col1:

                st.write(
                    f"**Product:** {product.name}"
                )

                st.write(
                    f"**Category:** {product.category}"
                )

                st.write(
                    f"**Price:** ₹{product.price}"
                )

                st.write(
                    f"**Rating:** ⭐ {product.rating}"
                )

                st.write(
                    f"**Score:** {score}"
                )

                st.write(
                    f"**Match Quality:** {status}"
                )
                st.write("💡 Why Recommended")

                for reason in item["reason"]:
                   st.success(reason)

            with col2:

                st.metric(
                    "Confidence",
                    f"{confidence}%"
                )

            st.progress(
                confidence / 100
            )

        # ====================================
        # PHASE 18 INSIGHTS DASHBOARD
        # ====================================

        st.markdown("---")
        st.header("📈 Recommendation Insights")

        # -----------------------------
        # BEST SCORE
        # -----------------------------

        best_score = max(
            item["score"]
            for item in recommendations
        )

        st.metric(
            "🏆 Best Recommendation Score",
            round(best_score, 2)
        )

        st.markdown("---")

        # -----------------------------
        # PRODUCT POPULARITY
        # -----------------------------

        st.subheader(
            "🔥 Product Popularity Ranking"
        )

        popularity_data = []

        for product in products.values():

            popularity_data.append(
                {
                    "Product":
                        product.name,

                    "Popularity":
                        round(
                            product.rating * 20,
                            2
                        )
                }
            )

        popularity_df = pd.DataFrame(
            popularity_data
        )

        popularity_df = popularity_df.sort_values(
            by="Popularity",
            ascending=False
        )

        st.dataframe(
            popularity_df,
            use_container_width=True
        )

        st.markdown("---")

        # -----------------------------
        # CONFIDENCE ANALYTICS
        # -----------------------------

        st.subheader(
            "🎯 Recommendation Confidence"
        )

        confidence_data = []

        for item in recommendations:

            confidence_data.append(
                {
                    "Product":
                        item["product"].name,

                    "Confidence":
                        min(
                            round(
                                item["score"] * 10
                            ),
                            100
                        )
                }
            )

        confidence_df = pd.DataFrame(
            confidence_data
        )

        confidence_chart = px.bar(
            confidence_df,
            x="Product",
            y="Confidence",
            text="Confidence",
            title="Recommendation Confidence"
        )

        st.plotly_chart(
            confidence_chart,
            use_container_width=True
        )

        st.markdown("---")

        # -----------------------------
        # USER MATCH HEATMAP
        # -----------------------------

        st.subheader(
            "🔥 User Match Heatmap"
        )

        heatmap_data = []

        for user in users.values():

            recs = engine.recommend(
                user,
                users,
                top_n=5
            )

            scores = []

            for item in recs:
                scores.append(
                    item["score"]
                )

            while len(scores) < 5:
                scores.append(0)

            heatmap_data.append(
                scores
            )

        heatmap_fig = go.Figure(
            data=go.Heatmap(
                z=heatmap_data,
                x=[
                    "Rec1",
                    "Rec2",
                    "Rec3",
                    "Rec4",
                    "Rec5"
                ],
                y=[
                    user.name
                    for user in users.values()
                ]
            )
        )

        heatmap_fig.update_layout(
            title="User Recommendation Similarity"
        )

        st.plotly_chart(
            heatmap_fig,
            use_container_width=True
        )

# ----------------------------------
# ANALYTICS PRO
# ----------------------------------

elif selected == "Analytics":

    st.title("📊 Executive Analytics Dashboard")

    # -------------------------
    # DATA PREPARATION
    # -------------------------

    product_data = []

    for product in products.values():

        product_data.append(
            {
                "ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Price": product.price,
                "Rating": product.rating
            }
        )

    df = pd.DataFrame(product_data)

    # -------------------------
    # KPI CARDS
    # -------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Products",
            len(df)
        )

    with col2:
        st.metric(
            "📂 Categories",
            df["Category"].nunique()
        )

    with col3:
        st.metric(
            "⭐ Avg Rating",
            round(
                df["Rating"].mean(),
                2
            )
        )

    with col4:
        st.metric(
            "💰 Avg Price",
            f"₹{round(df['Price'].mean())}"
        )

    st.markdown("---")

    # -------------------------
    # PIE CHART
    # -------------------------

    st.subheader(
        "🥧 Product Category Distribution"
    )

    pie_fig = px.pie(
        df,
        names="Category",
        title="Products by Category"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    st.markdown("---")

    # -------------------------
    # BAR CHART
    # -------------------------

    st.subheader(
        "📊 Products by Category"
    )

    category_count = (
        df["Category"]
        .value_counts()
        .reset_index()
    )

    category_count.columns = [
        "Category",
        "Count"
    ]

    bar_fig = px.bar(
        category_count,
        x="Category",
        y="Count",
        text="Count",
        title="Category Breakdown"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

    st.markdown("---")

    # -------------------------
    # RATING DISTRIBUTION
    # -------------------------

    st.subheader(
        "⭐ Product Ratings"
    )

    rating_fig = px.histogram(
        df,
        x="Rating",
        nbins=10,
        title="Rating Distribution"
    )

    st.plotly_chart(
        rating_fig,
        use_container_width=True
    )

    st.markdown("---")

    # -------------------------
    # TOP PRODUCTS
    # -------------------------

    st.subheader(
        "🏆 Top Rated Products"
    )

    top_products = (
        df.sort_values(
            by="Rating",
            ascending=False
        )
        .head(5)
    )

    st.dataframe(
        top_products,
        use_container_width=True
    )

# ----------------------------------
# SYSTEM HEALTH
# ----------------------------------

elif selected == "System Health":

    st.title("⚙️ System Health")

    st.success(
        "🟢 SQLite Database Connected"
    )

    st.success(
        "🟢 Recommendation Engine Active"
    )

    st.success(
        "🟢 Dashboard Online"
    )

    st.success(
        "🟢 Report Generator Available"
    )

db.close()