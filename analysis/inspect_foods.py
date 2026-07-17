import pandas as pd

df = pd.read_csv("food.csv")

print("Rows:", len(df))
print()

print("Categories:")
print(df["Category"].value_counts().head(50))

print()
print("Sample Foods:")
print(df["Description"].sample(20).tolist())