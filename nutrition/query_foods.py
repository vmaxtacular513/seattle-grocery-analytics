import sqlite3

conn = sqlite3.connect("nutrition/nutrition.db")

query = """
SELECT Category,
        COUNT(*) AS foods
FROM foods
WHERE Category NOT IN (
    'FAST FOODS',
    'MCDONALD''S',
    'POPEYES',
    'KENTUCKY FRIED CHICK',
    'CAMPBELL',
    'CAMPBELL SOUP COMPANY'
)
GROUP BY Category
ORDER BY foods DESC
LIMIT 100;
"""

results = conn.execute(query)

for row in results:
    print(row)

conn.close()