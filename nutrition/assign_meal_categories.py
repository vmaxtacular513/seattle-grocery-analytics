import pandas as pd
from category_map import MEAL_PLANNER_CATEGORIES

foods = pd.read_csv("nutrition/foods_clean.csv")

category_lookup = {}

for meal_category, usda_categories in MEAL_PLANNER_CATEGORIES.items():
    for usda_category in usda_categories:
        category_lookup[usda_category] = meal_category

foods["meal_category"] = (
    foods["Category"]
    .map(category_lookup)
    .fillna("Unclassified")
)

print(
    foods[
        ["food_name", "Category", "meal_category"]
    ].head(20)
)

missing = foods[foods["meal_category"].isna()]

print("Missing categories:", missing["Category"].nunique())

print(
    missing["Category"]
    .value_counts()
    .head(25)
)

foods.to_csv(
    "foods_meal_categories.csv",
    index=False
)

print("Saved foods_meal_categories.csv")

print("\nMeal Category Counts:")
print(foods["meal_category"].value_counts())

unclassified = foods[
    foods["meal_category"] == "Unclassified"
]

print("\nTop Unclassified Categories")
print(
    unclassified["Category"]
    .value_counts()
    .head(50)
)