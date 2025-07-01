import matplotlib
matplotlib.use('Agg')  # Prevent macOS GUI crash

import matplotlib.pyplot as plt
import sqlite3
from flask import render_template
from collections import Counter
from io import BytesIO
import base64

def dashboard_r(app):

    @app.route("/dashboard")
    def dash():
        # Step 1: Load ingredients from DB
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT RecipeIngredientParts FROM recipes")
        rows = cursor.fetchall()
        conn.close()

        # Step 2: Clean and flatten ingredient list
        all_ingredients = []
        for row in rows:
            raw = row[0].lower().replace('c(', '').replace(')', '').replace('"', '').replace("'", '')
            items = [i.strip() for i in raw.split(",") if i.strip()]
            all_ingredients.extend(items)

        # Step 3: Count and get top 10 ingredients
        ingredient_counts = Counter(all_ingredients)
        top_10 = ingredient_counts.most_common(10)

        if not top_10:
            return render_template("dashboard.html", chart_data=None)

        labels, values = zip(*top_10)

        # Step 4: Generate bar chart in memory
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.xticks(rotation=45, ha='right')
        plt.title("Top 10 Most Common Ingredients")
        plt.xlabel("Ingredient")
        plt.ylabel("Count")
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()

        return render_template("dashboard.html", chart_data=image_base64)
