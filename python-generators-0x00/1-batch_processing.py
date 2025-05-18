import psycopg2
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """
    Generator that yields user records in batches of given size from the user_data table.
    """
    conn = connect_to_prodev()
    if conn is None:
        return

    cursor = conn.cursor(name='user_batch_cursor') 
    cursor.itersize = batch_size
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield [
            {
                "user_id": str(row[0]),
                "name": row[1],
                "email": row[2],
                "age": int(row[3])
            }
            for row in rows
        ]

    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """
    Filters users older than 25 from each batch and prints them.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
