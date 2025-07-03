from flask import request, render_template
import sqlite3

def register_search_routes(app):

    @app.route("/search", methods=["GET", "POST"])
    def search():
        if request.method == "POST":
            ingredients_input = request.form["ingredients"]
            input_list = [i.strip().lower() for i in ingredients_input.split(",")]

            # Fetch recipes from the database
            conn = sqlite3.connect("recipes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT RecipeId, Name, RecipeIngredientParts FROM recipes")
            rows = cursor.fetchall()
            conn.close()

            matches = []
            for recipe_id, name, ing in rows:
                ing_lower = ing.lower()

                # Support both old and new formats
                if ing_lower.startswith("c("):
                    clean_ing = ing_lower.replace('c(', '').replace(')', '').replace('"', '').replace("'", '')
                else:
                    clean_ing = ing_lower

                # Check if all ingredients are present
                if all(word in clean_ing for word in input_list):
                    # Highlight each matched ingredient
                    for word in input_list:
                        clean_ing = clean_ing.replace(
                            word, f"<mark>{word}</mark>"
                        )

                    matches.append((name, clean_ing, recipe_id))
                    if len(matches) == 5:
                        break

            return render_template("results.html", recipes=matches)

        return render_template("search_form.html")
