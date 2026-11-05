import sqlite3
import hashlib


def authenticate_user(email, password):
    encoded_password = password.encode()
    hashed_password = hashlib.sha256(encoded_password)
    password_hash = hashed_password.hexdigest()

    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE email = ? AND password = ?
            """,
            (email, password_hash),
        )

        user = cursor.fetchone()

    if user is not None:
        return True

    return False
