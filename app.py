import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns


icon = Image.open("youtube_icon.png")

st.set_page_config(
    page_title="YouTube Ad Revenue Prediction",
    page_icon= icon,
    layout="wide"
)

st.markdown("""
<style>
div[data-testid="stMetric"] {
    background-color: #c92c34;
    border: 2px solid #CC0000;
    padding: 15px;
    border-radius: 12px;
    text-align: center;

}
</style>
""", unsafe_allow_html=True)

#st.image(icon, width=40)

#st.title("YouTube Ad Revenue Prediction")
col1, col2 = st.columns([1, 10],vertical_alignment="center")

with col1:
    st.image(icon, width=55)

with col2:
    st.markdown(
        "<h1 style='margin-top:12px;'>YouTube Ad Revenue Prediction</h1>",
        unsafe_allow_html=True
    )

df = pd.read_csv("Cleaned_youtube_dataset.csv")
model = joblib.load("youtube_revenue_model.pkl")
scaler = joblib.load("scaler.pkl")
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dataset",
        "Visualization",
        "Prediction",
        "Model Insights"
    ]
)
if page=="Home":

    st.header("Project Overview")

    st.write("""
    This application predicts YouTube Advertisement Revenue using Machine Learning.

    Features include:

    - Dataset Preview
    - Visualizations
    - Revenue Prediction
    """)
    col1,col2,col3 = st.columns(3)

    col1.metric(
        "Total Videos",
        len(df),border=True
    )

    col2.metric(
        "Average Revenue",
        f"${df['ad_revenue_usd'].mean():.2f}",
        border=True
    )

    col3.metric(
        "Maximum Revenue",
        f"${df['ad_revenue_usd'].max():.2f}",
        border=True
    )
elif page=="Dataset":

    st.header("Dataset")

    st.dataframe(df)

    st.write("Shape:", df.shape)
elif page=="Visualization":

    st.header("Visualizations")

    fig, ax = plt.subplots()

    ax.hist(df["ad_revenue_usd"], bins=30)

    ax.set_title("Revenue Distribution")

    st.pyplot(fig)
    corr = df.corr(numeric_only=True)

    st.write(corr)

    ax.set_title("Views vs Revenue")

    fig, ax = plt.subplots()

    ax.scatter(
        df["views"],
        df["ad_revenue_usd"]
    )

    ax.set_xlabel("Views")
    ax.set_ylabel("Revenue")

    st.pyplot(fig)

    ##Correlation Heatmap

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Feature Correlation")

    st.pyplot(fig)
elif page=="Prediction":

    st.header("Revenue Prediction")

    views = st.number_input("Views", min_value=0)

    likes = st.number_input("Likes", min_value=0)

    comments = st.number_input("Comments", min_value=0)

    watch_time = st.number_input("Watch Time (Minutes)", min_value=0.0)

    video_length = st.number_input("Video Length", min_value=0.0)

    subscribers = st.number_input("Subscribers", min_value=0)

    year = st.number_input("Year", value=2024)

    month = st.slider("Month",1,12)

    day = st.slider("Day",1,31)

    weekday = st.slider("Weekday",0,6)

    engagement_rate = (likes+comments)/views if views>0 else 0

    like_rate = likes/views if views>0 else 0

    comment_rate = comments/views if views>0 else 0

    avg_watch_time = watch_time/views if views>0 else 0

    views_per_subscriber = views/subscribers if subscribers>0 else 0

    is_weekend = 1 if weekday>=5 else 0

    category = st.selectbox(
    "Category",
        [
            "Education",
            "Entertainment",
            "Gaming",
            "Lifestyle",
            "Music",
            "Tech"
        ]
    )
    device = st.selectbox(
    "Device",
        [
            "Desktop",
            "Mobile",
            "TV",
            "Tablet"
        ]
    )
    country = st.selectbox(
    "Country",
        [
            "AU",
            "CA",
            "DE",
            "IN",
            "UK",
            "US"
        ]
    )
    input_data = {
    "views":views,
    "likes":likes,
    "comments":comments,
    "watch_time_minutes":watch_time,
    "video_length_minutes":video_length,
    "subscribers":subscribers,
    "year":year,
    "month":month,
    "day":day,
    "weekday":weekday,
    "category_Entertainment":0,
    "category_Gaming":0,
    "category_Lifestyle":0,
    "category_Music":0,
    "category_Tech":0,
    "device_Mobile":0,
    "device_TV":0,
    "device_Tablet":0,
    "country_CA":0,
    "country_DE":0,
    "country_IN":0,
    "country_UK":0,
    "country_US":0,
    "engagement_rate":engagement_rate,
    "like_rate":like_rate,
    "comment_rate":comment_rate,
    "avg_watch_time":avg_watch_time,
    "views_per_subscriber":views_per_subscriber,
    "is_weekend":is_weekend,
    }
    if category!="Education":
        input_data[f"category_{category}"]=1

    if device!="Desktop":
        input_data[f"device_{device}"]=1

    if country!="AU":
        input_data[f"country_{country}"]=1

    if st.button("Predict Revenue",type="primary"):

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        st.success(
            f"Estimated Ad Revenue : ${prediction[0]:.2f}"
        )
elif page == "Model Insights":

    st.header("📊 Basic Visual Analytics & Model Insights")
    #Model Performance Table
    results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting",
        "KNN"
    ],
    "MAE":[3.122,3.620,3.562,5.285,13.202],
    "RMSE":[13.480,13.530,13.841,19.431,19.497],
    "R² Score":[0.9525,0.9522,0.9499,0.9014,0.9007]
    })

    st.subheader("Model Comparison")

    st.dataframe(results)
    ## Best Model
    best = results.loc[
    results["R² Score"].idxmax()
    ]

    st.success(
        f"🏆 Best Model: {best['Model']} (R² = {best['R² Score']:.4f})"
    )
    ## R² Comparison Chart
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7,4))

    ax.bar(
        results["Model"],
        results["R² Score"]
    )

    ax.set_ylabel("R² Score")
    ax.set_title("Model Performance Comparison")

    plt.xticks(rotation=20)

    st.pyplot(fig)
    ## Error comparison
    fig, ax = plt.subplots(figsize=(7,4))

    ax.bar(
        results["Model"],
        results["RMSE"]
    )

    ax.set_ylabel("RMSE")

    ax.set_title("RMSE Comparison")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    ## Feature Influences
    feature_names = joblib.load("feature_names.pkl")


    coef = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": model.coef_
    })

    st.subheader("Top Influential Features")

    st.dataframe(coef.head(10))

    ## Feature Influence chart
    top = coef.head(10)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        top["Feature"],
        top["Coefficient"]
    )

    ax.set_title("Top Influential Features")

    st.pyplot(fig)


    st.subheader("Model Insights")

    st.write("""
    • Views have the strongest influence on advertisement revenue.

    • Watch Time contributes significantly to revenue prediction.

    • Subscriber count positively affects revenue.

    • Engagement metrics (likes and comments) improve prediction accuracy.

    • Linear Regression achieved the highest R² score and was selected as the final model.
    """)