import sqlite3

# Connect to your existing recipes.db
conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

# Create the favorites table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

print("✅ favorites table created successfully in recipes.db")
