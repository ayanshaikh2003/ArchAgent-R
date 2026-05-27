import sqlite3
from datetime import datetime

DB_NAME = "archagent.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            input_text TEXT NOT NULL,
            modification TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()

def create_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )

    conn.commit()
    conn.close()

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user

def save_history(user_id, input_text, modification):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (user_id, input_text, modification, created_at) VALUES (?, ?, ?, ?)",
        (user_id, input_text, modification, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )

    conn.commit()
    conn.close()

def get_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT input_text, modification, created_at FROM history WHERE user_id = ? ORDER BY id DESC",
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return rows