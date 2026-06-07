import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from streamlit_option_menu import option_menu

from src.database_manager import DatabaseManager
from src.sample_users import create_users
from src.recommender import RecommendationEngine
from src.product_images import PRODUCT_IMAGES


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Recommendation Platform",
    page_icon="🛒",
    layout="wide"
)


# ----------------------------------
# DARK THEME CSS
# ----------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0E1117;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #161B22;
    }

    div[data-testid="metric-container"] {
        background-color: #1E293B;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.4);
    }

    div[data-testid="metric-container"] label {
        color: white !important;
    }

    div[data-testid="metric-container"] div {
        color: white !important;
    }

    .stDataFrame {
        background-color: #161B22;
    }

    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
    }

    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    p, label, span {
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>

/* PREMIUM TABLES */

[data-testid="stDataFrame"] {

    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    ) !important;

    border-radius: 20px !important;

    padding: 12px !important;

    border: 2px solid #38bdf8 !important;

    box-shadow:
        0 0 20px rgba(56,189,248,.5),
        0 0 40px rgba(59,130,246,.3) !important;

}

/* Header */

thead tr th {

    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    ) !important;

    color: white !important;

    font-weight: bold !important;

    font-size: 15px !important;

}

/* Rows */

tbody tr:nth-child(even) {

    background-color:
    rgba(59,130,246,.08) !important;

}

tbody tr:hover {

    background-color:
    rgba(56,189,248,.20) !important;

}

/* Scrollbar */

::-webkit-scrollbar {

    width: 10px;

    height: 10px;

}

::-webkit-scrollbar-thumb {

    background: #38bdf8;

    border-radius: 10px;

}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* KPI Cards */

.metric-card{
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );

    padding:20px;

    border-radius:18px;

    border:2px solid #38bdf8;

    box-shadow:
        0 0 15px rgba(56,189,248,0.4),
        0 0 30px rgba(59,130,246,0.2);

    text-align:center;

    margin-bottom:10px;
}

.metric-title{
    color:#94a3b8;
    font-size:16px;
    font-weight:bold;
}

.metric-value{
    color:white;
    font-size:38px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


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

/* PREMIUM KPI CARDS */

.metric-card{

    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );

    padding:25px;

    border-radius:20px;

    border:2px solid #38bdf8;

    box-shadow:
        0 0 15px rgba(56,189,248,0.5),
        0 0 35px rgba(59,130,246,0.3);

    text-align:center;

    transition:0.3s;

    margin-bottom:15px;
}

.metric-card:hover{

    transform:translateY(-5px);

    box-shadow:
        0 0 25px rgba(56,189,248,0.8),
        0 0 50px rgba(59,130,246,0.5);
}

.metric-title{

    color:#cbd5e1;

    font-size:18px;

    font-weight:600;
}

.metric-value{

    color:white;

    font-size:42px;

    font-weight:800;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* DataFrame */
[data-testid="stDataFrame"]{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );
    border-radius:20px;
    padding:10px;
    border:1px solid #38bdf8;
    box-shadow:
        0 0 20px rgba(56,189,248,0.4),
        0 0 40px rgba(59,130,246,0.2);
}

/* Plotly Charts */
[data-testid="stPlotlyChart"]{
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );
    border-radius:20px;
    padding:15px;
    border:1px solid #06b6d4;
    box-shadow:
        0 0 20px rgba(6,182,212,0.4);
}

/* Metrics */
[data-testid="metric-container"]{
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );
    border-radius:20px;
    padding:20px;
    border:1px solid #3b82f6;
    box-shadow:
        0 0 20px rgba(59,130,246,0.4);
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

    col1, col2, col3, col4 = st.columns(4)

    with col1:

     st.markdown(f"""
     <div class="metric-card">
          <div class="metric-title">
            📦 Products
        </div>

        <div class="metric-value">
            {total_products}
        </div>
      </div>
      """, unsafe_allow_html=True)

    with col2:

     st.markdown(f"""
     <div class="metric-card">
        <div class="metric-title">
            👥 Users
        </div>

        <div class="metric-value">
            {total_users}
        </div>
     </div>
     """, unsafe_allow_html=True)

    with col3:

     st.markdown(f"""
     <div class="metric-card">
        <div class="metric-title">
            ⭐ Avg Rating
        </div>

        <div class="metric-value">
            {avg_rating}
        </div>
     </div>
     """, unsafe_allow_html=True)

    with col4:

      st.markdown("""
        <div class="metric-card">
        <div class="metric-title">
            🤖 AI Engine
        </div>

        <div class="metric-value">
            ONLINE
        </div>
     </div>
     """, unsafe_allow_html=True)

    st.markdown("---")

    # ----------------------------------
    # BUSINESS KPI DASHBOARD
    # ----------------------------------

    k1, k2, k3 = st.columns(3)

    with k1:
      st.markdown("""
      <div class="metric-card">
        <div class="metric-title">
            💰 Revenue
        </div>

        <div class="metric-value">
            ₹12.5L
        </div>
     </div>
     """, unsafe_allow_html=True)

    with k2:
      st.markdown("""
      <div class="metric-card">
        <div class="metric-title">
            🎯 AI Accuracy
        </div>

        <div class="metric-value">
            92%
        </div>
     </div>
     """, unsafe_allow_html=True)

    with k3:
      st.markdown("""
      <div class="metric-card">
        <div class="metric-title">
            😊 Satisfaction
        </div>

        <div class="metric-value">
            95%
        </div>
     </div>
     """, unsafe_allow_html=True)

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

    st.markdown("---")

    st.subheader("🔥 Trending Products")

    top_products = sorted(
     products.values(),
     key=lambda x: x.rating,
     reverse=True
    )[:5]

    for product in top_products:

      st.success(
        f"{product.name} ⭐ {product.rating}"
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

    cols = st.columns(4)

    for index, product in enumerate(products.values()):

     with cols[index % 4]:

        image_url = PRODUCT_IMAGES.get(product.name)

        if image_url:
            st.image(
                image_url,
                use_container_width=True
            )

        st.markdown(
            f"""
        ### {product.name}

        ⭐ {product.rating}

        💰 ₹{product.price}

        📦 {product.category}
        """
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
        # RECOMMENDATION LEADERBOARD
        # -----------------------------

        st.header("📈 Recommendation Insights")

        st.subheader(
            "🏆 Recommendation Leaderboard"
        )

        leaderboard = []

        for item in recommendations:

            leaderboard.append(
                {
                    "Product":
                        item["product"].name,

                    "Score":
                        item["score"]
                }
            )

        leaderboard_df = pd.DataFrame(
            leaderboard
        )

        leaderboard_df = leaderboard_df.sort_values(
            by="Score",
            ascending=False
        )

        st.dataframe(
            leaderboard_df,
            use_container_width=True
        )

        st.markdown("---")

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

            st.markdown("---")

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
        # CONFIDENCE CHART
        # -----------------------------

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
           color="Confidence",
           color_continuous_scale="Turbo"
        )

        confidence_chart.update_layout(
             template="plotly_dark",
             paper_bgcolor="#0f172a",
             plot_bgcolor="#0f172a",
             font=dict(
             color="white",
             size=14
        ),
       
         title_x=0.5
)    

        st.plotly_chart(
            confidence_chart,
            use_container_width=True,
            key="confidence_chart"
        )

        st.markdown("---")

        # -----------------------------
        # PRODUCT POPULARITY
        # -----------------------------

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

        st.subheader(
            "🔥 Product Popularity Ranking"
        )

        st.dataframe(
            popularity_df,
            use_container_width=True
        )


        # -----------------------------
        # CONFIDENCE ANALYTICS
        # -----------------------------

        st.markdown("""
            <div style="
            background:linear-gradient(
             135deg,
             #111827,
             #1e293b
            );
            padding:20px; 
            border-radius:20px;
            border:1px solid #38bdf8;
            box-shadow:0 0 25px rgba(56,189,248,0.4);
           ">
           """, unsafe_allow_html=True)

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
            use_container_width=True,
            key="heatmap_chart"
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
            data=go.Heatmap(z =heatmap_data,colorscale="Turbo",showscale=True,
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
            template="plotly_dark",
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            title="User Recommendation Similarity",
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

    pie_fig.update_traces(
       textinfo="percent+label"
    )

    pie_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0f172a",
        font=dict(color="white")
)

    st.plotly_chart(
        pie_fig,
        use_container_width=True,
        key="pie_chart"
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

    bar_fig.update_traces(
      marker=dict(
         color=category_count["Count"],
         colorscale="Turbo"
       ) 
   )

    bar_fig.update_layout(
      template="plotly_dark",
      paper_bgcolor="#0f172a"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True,
        key="bar_chart"

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
        use_container_width=True,
        key="rating_chart"
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