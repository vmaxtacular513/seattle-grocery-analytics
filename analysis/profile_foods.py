import pandas as pd

df = pd.read_csv("food.csv")

print("\nRows:", len(df))

print("\nUnique Categories:")
print(df["Category"].nunique())

print("\nUnique Foods:")
print(df["Description"].nunique())

print("\nDuplicate Food Names:")
print(df["Description"].duplicated().sum())

print("\nTop 10 Highest Protein Foods")
print(
    df[["Description", "Data.Protein"]]
    .sort_values("Data.Protein", ascending=False)
    .head(10)
)

print("\nTop 10 Highest Calorie Foods")
print(
    df[["Description", "Data.Kilocalories"]]
    .sort_values("Data.Kilocalories", ascending=False)
    .head(10)
)