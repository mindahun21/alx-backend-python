import psycopg2
from seed import connect_to_prodev

def stream_users():
    conn = connect_to_prodev()
    
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    for row in cursor:
        yield {
            "user_id": str(row[0]),
            "name": row[1],
            "email": row[2],
            "age": int(row[3])
        }

    cursor.close()
    conn.close()
