import streamlit as st


def apply_filters(df):
    """
    Apply keyword and sentiment filters
    and return the filtered dataframe.
    """

    st.sidebar.header("Search & Filters")

    sentiment_filter = st.sidebar.selectbox(
        "Sentiment",
        ["All"] + sorted(df["sentiment"].unique().tolist())
    )

    keyword = st.sidebar.text_input("Search Posts")

    filtered_df = df.copy()

    if sentiment_filter != "All":
        filtered_df = filtered_df[
            filtered_df["sentiment"] == sentiment_filter
        ]

    if keyword:
        filtered_df = filtered_df[
            filtered_df["text"].str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

    return filtered_df