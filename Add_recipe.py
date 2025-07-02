from flask import request, render_template
import sqlite3

def add_recipe_route(app):

    @app.route("/add-recipe", methods=["GET", "POST"])
    def add_recipe():
        if request.method == "POST":
            name = request.form.get("name")
            ingredients = request.form.get("ingredients")

            # Insert into DB
            conn = sqlite3.connect("recipes.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO recipes (Name, RecipeIngredientParts) VALUES (?, ?)", (name, ingredients))
            conn.commit()
            conn.close()

            return render_template("confirmation.html", recipe_name=name)

        return render_template("add_recipe.html")
