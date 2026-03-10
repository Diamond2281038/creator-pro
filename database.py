import sqlite3
from config import DATABASE

def db():
    return sqlite3.connect(DATABASE)

def init_db():

    conn = db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        ref INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS bots(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        token TEXT,
        file TEXT,
        type TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
