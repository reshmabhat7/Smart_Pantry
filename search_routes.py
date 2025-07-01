from flask import render_template, request
import sqlite3

def register_search_routes(app):

    @app.route("/search", methods=["GET", "POST"])
    def search():
        if request.method == "POST":
            ingredients_input = request.form["ingredients"]
            input_list = [i.strip().lower() for i in ingredients_input.split(",") if i.strip()]

            if not input_list:
                return render_template("results.html", recipes=[])

            conn = sqlite3.connect("recipes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT Name, RecipeIngredientParts FROM recipes")
            rows = cursor.fetchall()
            conn.close()

            matches = []
            for name, ing in rows:
                ing_lower = ing.lower()
                clean_ing = (
                    ing_lower.replace('c(', '')
                             .replace(')', '')
                             .replace('"', '')
                             .replace("'", '')
                )
                ingredient_words = clean_ing.replace(',', '').split()
                for word in input_list:
                    clean_ing = clean_ing.replace(
                        word, f"<mark>{word}</mark>"
                    )

                if all(word in ingredient_words for word in input_list):
                    matches.append((name, clean_ing))
                    if len(matches) == 5:
                        break

            return render_template("results.html", recipes=matches)

        return render_template("search_form.html")
