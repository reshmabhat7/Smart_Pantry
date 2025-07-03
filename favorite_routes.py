from flask import redirect, render_template
import sqlite3

def register_favorite_routes(app):

    @app.route("/fav/<int:recipe_id>")
    def fav(recipe_id):
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()

        # ✅ Check if recipe is already in favorites
        cursor.execute("SELECT 1 FROM favorites WHERE recipe_id = ?", (recipe_id,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute("INSERT INTO favorites (recipe_id) VALUES (?)", (recipe_id,))
            conn.commit()

        conn.close()
        return redirect("/favorites")

    @app.route("/favorites")
    def favorites():
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT r.Name, r.RecipeIngredientParts, f.created_at
            FROM favorites f
            JOIN recipes r ON r.RecipeId = f.recipe_id
            ORDER BY f.created_at DESC;
        """)

        raw_rows = cursor.fetchall()
        rows = []
        for name, ingredients, created_at in raw_rows:
            clean_ing = (
                ingredients.replace('c(', '')
                           .replace(')', '')
                           .replace('"', '')
                           .replace("'", '')
            )
            rows.append((name, clean_ing, created_at))

        conn.close()
        return render_template("favorites.html", favorites=rows)
