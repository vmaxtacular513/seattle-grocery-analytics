import pandas as pd
import sqlite3

df = pd.read_csv("nutrition/foods_clean.csv")

conn = sqlite3.connect("nutrition.db")

df.to_sql(
    "foods",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created.")