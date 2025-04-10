import sqlite3

def init_db():
    conn = sqlite3.connect("shopgenie.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_data (
                    user_id TEXT,
                    last_browsed_category TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def get_log():
    conn = sqlite3.connect("shopgenie.db")
    c = conn.cursor()
    rows = c.execute("SELECT * FROM user_data").fetchall()
    conn.close()
    return rows
