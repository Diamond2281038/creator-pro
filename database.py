import sqlite3
from config import DATABASE

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        token TEXT,
        file TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_bot(user_id, token, file):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO bots (user_id, token, file) VALUES (?, ?, ?)",
        (user_id, token, file)
    )

    conn.commit()
    conn.close()

def get_user_bots(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT file FROM bots WHERE user_id=?",
        (user_id,)
    )

    data = cursor.fetchall()
    conn.close()

    return data
