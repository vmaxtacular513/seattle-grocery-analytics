import pandas as pd

# Load CSV
df = pd.read_csv("food.csv")

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATES ===")
print(df.duplicated().sum())

print("\n=== NUMERIC SUMMARY ===")
print(df.describe())