import pandas as pd
import sqlite3

df = pd.read_csv("RAW_recipes.csv")[["RecipeId", "Name", "RecipeIngredientParts"]].head(300)

conn = sqlite3.connect("recipes.db")
df.to_sql("recipes", conn, if_exists="replace", index=False)

cursor = conn.cursor()

print("\n First 5 recipes:")
for row in cursor.execute("SELECT * FROM recipes LIMIT 5"):
    print(row)

cursor.execute("SELECT COUNT(*) FROM recipes")
count = cursor.fetchone()[0]
print(f"\b Total number of recipes: {count}")

cursor.execute("SELECT Name FROM recipes WHERE RecipeId = 42")
result = cursor.fetchone()
if result:
    print(f"\n Recipe with ID 42: {result[0]}")
else:
    print("\n No recipe found with ID 42")

conn.close()
