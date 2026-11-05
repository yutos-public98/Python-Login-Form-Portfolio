import sqlite3


def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_user(email, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (email,password) VALUES(?,?)", (email, password))

    connection.commit()
    connection.close()
