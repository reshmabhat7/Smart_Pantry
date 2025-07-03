from flask import Flask, render_template
from search_routes import register_search_routes
from dashboard_routes import dashboard_r
from Add_recipe import add_recipe_route  
from favorite_routes import register_favorite_routes

app = Flask(__name__)
register_search_routes(app)
dashboard_r(app)
add_recipe_route(app)
register_favorite_routes(app)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
