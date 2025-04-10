from datetime import datetime
import sqlite3

def customer_agent(user_id, category):
    conn = sqlite3.connect("shopgenie.db")
    c = conn.cursor()
    c.execute("INSERT INTO user_data VALUES (?, ?, ?)",
              (user_id, category, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
