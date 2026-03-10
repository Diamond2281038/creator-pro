from database import db

def get_stats():

    conn = db()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM users")
    users = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM bots")
    bots = c.fetchone()[0]

    conn.close()

    return users, bots
