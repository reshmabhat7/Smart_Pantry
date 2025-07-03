# 🧠 Smart Pantry

Smart Pantry is a simple, beginner-friendly web app that helps users find recipes based on the ingredients they already have. It also supports adding your own recipes, saving favorites, and visualizing popular ingredients.

---

## 💻 Tech Stack

- **Python 3**
- **Flask** – web framework
- **SQLite** – database for storing recipes and favorites
- **pandas** – for CSV processing
- **matplotlib** – for ingredient frequency charts

---

## 🚀 How to Run

1. Clone this repo  
2. Install dependencies (Flask, pandas, matplotlib)
3. Make sure you have `recipes.db` ready  
4. Run the app:

```bash
python app.py
````

Then open your browser at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 How to Run Tests

If unit tests are included (e.g. `test_utils.py`), run:

```bash
pytest
```

Make sure `pytest` is installed.

---

## ✨ Features

* ✅ Search recipes by entering comma-separated ingredients
* ✅ Add new recipes through a simple form
* ✅ Favorites system with ⭐ click
* ✅ Dashboard chart showing top 10 most used ingredients
* ✅ Uses SQL JOINs to display linked data between recipes and favorites
* ✅ Includes unit tests for helper functions

---

## 📸 Screenshots

### 🏠 Homepage

![Homepage](screenshots/homepage.png)
**Clean welcome message and “Start Searching” button**

---

### 🔎 Search Results

![Search](screenshots/search_results.png)
**Search recipes using ingredients with “☆ Favorite” links**

---

### 📝 Add Recipe Form

![Add Recipe](screenshots/add_recipe.png)
**Submit new recipes using a simple form with name + ingredients**

---

### ⭐ Favorites Page

![Favorites](screenshots/favorites.png)
**List of saved favorite recipes using SQL JOIN**

---

### 📊 Dashboard – Top Ingredients

![Dashboard](screenshots/dashboard.png)
**Bar chart showing the top 10 most used ingredients**

---

### ✅ Final Result Example

![Result](screenshots/result.png)
**Cleaned result view after search, showing recipe name + readable ingredients**

---

## 🧩 Extra Notes

* This app uses SQL JOINs to fetch recipes favorited by users
* Data is stored in a permanent SQLite file (`recipes.db`)
* Written with clarity and beginner-friendly structure
* Can be extended with login, remove-favorite, or recipe ratings

---

**Made with 💚 by Reshma Bhat – for learning, growth, and delicious possibilities!**

```

---

📝 Paste this into your `README.md`  
💾 Save the file  
🚀 Push to GitHub

Let me know if you’d like to add project badges or deploy this project live!
```
