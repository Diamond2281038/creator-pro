from database import db

def add_balance(user_id, amount):

    conn = db()
    c = conn.cursor()

    c.execute(
        "UPDATE users SET balance = balance + ? WHERE id=?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()
