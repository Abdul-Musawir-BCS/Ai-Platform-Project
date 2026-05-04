import sqlite3
from config import Config

def init_db():
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        enhanced_prompt TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_image(prompt, enhanced, path):
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()

    c.execute(
        "INSERT INTO images (prompt, enhanced_prompt, image_path) VALUES (?, ?, ?)",
        (prompt, enhanced, path)
    )

    conn.commit()
    image_id = c.lastrowid
    conn.close()
    return image_id

def get_history():
    conn = sqlite3.connect(Config.DB_PATH)
    c = conn.cursor()

    c.execute("SELECT * FROM images")
    data = c.fetchall()

    conn.close()
    return data
