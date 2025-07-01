from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        ingredients_input = request.form["ingredients"]

        # Clean input list (remove spaces, empty strings)
        input_list = [i.strip().lower() for i in ingredients_input.split(",") if i.strip()]

        # If no valid input, return 0 results
        if not input_list:
            return render_template("results.html", recipes=[])

        # Connect to database
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Name, RecipeIngredientParts FROM recipes")
        rows = cursor.fetchall()
        conn.close()

        matches = []
        for name, ing in rows:
            ing_lower = ing.lower()

            # Clean and prepare ingredients
            clean_ing = (
                ing_lower.replace('c(', '')
                         .replace(')', '')
                         .replace('"', '')
                         .replace("'", '')
            )

            # Create a list of individual ingredient words
            ingredient_words = clean_ing.replace(',', '').split()

            # Match full words only
            if all(word in ingredient_words for word in input_list):
                matches.append((name, clean_ing))
                if len(matches) == 5:
                    break

        return render_template("results.html", recipes=matches)

    return render_template("search_form.html")

if __name__ == "__main__":
    app.run(debug=True)
