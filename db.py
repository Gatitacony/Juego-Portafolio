import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        ''')
    conn.close()

def add_user(username, email, password):
    conn = get_db_connection()
    with conn:
        conn.execute('INSERT INTO user (username, email, password) VALUES (?, ?, ?)',
                     (username, email, password))
    conn.close()
