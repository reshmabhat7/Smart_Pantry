from flask import Flask, render_template
from search_routes import register_search_routes
from dashboard_routes import dashboard_r

app = Flask(__name__)
register_search_routes(app)
dashboard_r(app)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
