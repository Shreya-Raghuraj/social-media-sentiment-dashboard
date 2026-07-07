import pandas as pd

print("Reading dataset...")

df = pd.read_csv("data/raw/tweets.csv")

print(df.head())

sentiment_map = {
    -1: "Negative",
     0: "Neutral",
     1: "Positive"
}

df["sentiment"] = df["category"].map(sentiment_map)

print("Saving file...")

df.to_csv("data/processed/sentiment.csv", index=False)

print("Done!")