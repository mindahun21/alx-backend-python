import psycopg2
import csv
import uuid

def connect_db():
    try:
        return psycopg2.connect(
            host="localhost",
            user="alx",
            password="alxalx",
            dbname="alx"
        )
    except Exception as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT datname FROM pg_database")
        dbs = [row[0] for row in cursor.fetchall()]
        if "ALX_prodev" not in dbs:
            cursor.execute('CREATE DATABASE "ALX_prodev"')
        else:
            print("Database ALX_prodev already exists.")
    except psycopg2.errors.DuplicateDatabase:
        print("Database ALX_prodev already exists (caught in except block).")
    finally:
        cursor.close()

def connect_to_prodev():
    try:
        return psycopg2.connect(
            host="localhost",
            user="alx",
            password="alxalx",
            dbname="ALX_prodev"
        )
    except Exception as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id UUID PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON user_data(user_id);")
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (row['email'],))
            if cursor.fetchone()[0] == 0:
                uid = str(uuid.uuid4())
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (uid, row['name'], row['email'], row['age'])
                )
    connection.commit()
    cursor.close()

