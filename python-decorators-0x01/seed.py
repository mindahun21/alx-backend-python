import sqlite3
import csv
import uuid
import os

def connect_to_sqlite():
    return sqlite3.connect("users.db")

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age REAL NOT NULL
        );
    """)
    connection.commit()
    print("Table users created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (row['email'],))
            if cursor.fetchone()[0] == 0:
                uid = str(uuid.uuid4())
                cursor.execute(
                    "INSERT INTO users (user_id, name, email, age) VALUES (?, ?, ?, ?)",
                    (uid, row['name'], row['email'], float(row['age']))
                )
            print("user data read successfully!")
    connection.commit()
    cursor.close()

if __name__ == "__main__":
    conn = connect_to_sqlite()
    create_table(conn)
    insert_data(conn, "user_data.csv")
    conn.close()
