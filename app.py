import streamlit as st
import pandas as pd
import plotly.express as px
from modules.filters import apply_filters

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Social Media Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3 {
    font-weight: 600;
}

section[data-testid="stSidebar"] {
    background-color: #f5f5f5;
}

div[data-testid="metric-container"] {
    border: 1px solid #e6e6e6;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)
# -----------------------------
# Load Dataset
# -----------------------------
try:
    df = pd.read_csv("data/processed/sentiment.csv")
except FileNotFoundError:
    st.error("sentiment.csv not found!")
    st.stop()

# -----------------------------
# Title
# -----------------------------
st.title("Social Media Sentiment Dashboard")
st.caption("AI Internship | Minor Project")

# -----------------------------
# KPI Cards
# -----------------------------

total_posts = len(df)
positive = (df["sentiment"] == "Positive").sum()
neutral = (df["sentiment"] == "Neutral").sum()
negative = (df["sentiment"] == "Negative").sum()

with st.container(border=True):

    st.subheader("Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Posts", total_posts)
    col2.metric("Positive", positive)
    col3.metric("Neutral", neutral)
    col4.metric("Negative", negative)


# -----------------------------
# Sidebar Filters
# -----------------------------
filtered_df = apply_filters(df)

st.sidebar.info(
    """
    **About**

    This dashboard visualizes
    sentiment trends from
    social media posts.

    Group 4
    """
)
# -----------------------------
# Charts
# -----------------------------
st.subheader("Sentiment Analysis")

with st.container(border=True):

    st.subheader("Sentiment Analysis")

    chart_data = filtered_df["sentiment"].value_counts()

    col1, col2 = st.columns(2)

with col1:
    pie = px.pie(
    values=chart_data.values,
    names=chart_data.index,
    hole=0.45,
    color_discrete_sequence=[
        "#2E86DE",
        "#E74C3C",
        "#F1C40F"
    ]
)

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with col2:
    bar = px.bar(
    x=chart_data.index,
    y=chart_data.values,
    color=chart_data.index,
    color_discrete_sequence=[
        "#2E86DE",
        "#E74C3C",
        "#F1C40F"
    ]
)

    st.plotly_chart(
        bar,
        use_container_width=True
    )

# -----------------------------
# Trend Graph
# -----------------------------
if "date" in filtered_df.columns:

    trend = (
        filtered_df
        .groupby(["date","sentiment"])
        .size()
        .reset_index(name="count")
    )

    st.subheader("Sentiment Trend Over Time")

    line = px.line(
        trend,
        x="date",
        y="count",
        color="sentiment",
        markers=True
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )
# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("Dataset Preview")
st.write(f"Showing **{len(filtered_df)}** of **{len(df)}** posts")

if filtered_df.empty:
    st.warning("No posts found for the selected filters.")
else:
    st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# Download CSV
# -----------------------------
csv = filtered_df.to_csv(index=False).encode()

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_sentiment.csv",
    mime="text/csv"
)

# -----------------------------
# Footer
# -----------------------------

st.caption("Minor Project • AI Internship")