import pandas as pd

df = pd.read_csv("food.csv")

foods = df.rename(
    columns={
        "Nutrient Data Bank Number": "food_id",
        "Description": "food_name",
        "Data.Kilocalories": "calories",
        "Data.Protein": "protein",
        "Data.Carbohydrate": "carbs",
        "Data.Fat.Total Lipid": "fat",
        "Data.Fiber": "fiber",
        "Data.Sugar Total": "sugar",
        "Data.Major Minerals.Sodium": "sodium"
    }
)

foods = foods[
    [
        "food_id",
        "Category",
        "food_name",
        "calories",
        "protein",
        "carbs",
        "fat",
        "fiber",
        "sugar",
        "sodium"
    ]
]

foods.to_csv("foods_clean.csv", index=False)

print("Saved foods_clean.csv")
