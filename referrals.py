from database import db
from config import REF_REWARD

def reward(ref):

    conn = db()
    c = conn.cursor()

    c.execute(
        "UPDATE users SET balance = balance + ? WHERE id=?",
        (REF_REWARD, ref)
    )

    conn.commit()
    conn.close()
