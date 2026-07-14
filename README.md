# Seattle Grocery Analytics

A Python data analytics project focused on nutrition analysis, meal planning, and grocery budgeting.

## Project Goal

This project explores food and nutrition data using Python and pandas to answer questions such as:

- Which foods provide the most protein?
- Which foods provide the most protein per calorie?
- What foods are best for high-protein meal planning?
- How can nutrition and grocery pricing data be combined to create budget-friendly meal plans?

Future versions of the project will integrate grocery pricing data from the Kroger/QFC API.

---

## Skills Demonstrated

- Python
- Pandas
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualization
- Jupyter Notebooks
- Git & GitHub

---

## Dataset

Current dataset:

- Nutrition and food composition dataset from Kaggle

Key fields include:

- Food description
- Calories
- Protein
- Carbohydrates
- Fat
- Vitamins and minerals

---

## Project Structure

```text
grocery_meal_planner/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## Current Analysis

The first notebook explores:

- Dataset structure
- Nutrition distributions
- Highest-protein foods
- Protein-per-calorie rankings

During exploration, protein-per-calorie analysis revealed that very-low-calorie beverages could distort rankings. Additional filtering was introduced to focus on foods with meaningful protein content.

---

## Future Enhancements

- Data cleaning pipeline
- Meal recommendation engine
- Weekly meal planning
- Grocery cost estimation
- Kroger/QFC API integration
- Interactive dashboard using Streamlit