import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/Twitter_Data.csv")

# Show first 5 rows
print(df.head())

# Show dataset size
print("\nShape of dataset:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())
# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Rename the column
df = df.rename(columns={"clean_text": "text"})

# Save cleaned dataset
df.to_csv("data/raw/tweets.csv", index=False)

print("\nDataset cleaned successfully!")
print("New Shape:", df.shape)