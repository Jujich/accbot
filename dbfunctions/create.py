from sqlite3 import connect
conn = connect('../database.db')


def create_user(user_id:int, name: str, role: str = "user"):
    conn.execute(
        "INSERT INTO users (user_id, name, role) VALUES (?, ?, ?)",
        (user_id, name, role)
    )
