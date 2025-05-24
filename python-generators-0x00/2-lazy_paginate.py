import psycopg2
seed = __import__('seed')

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    connection.close()
    return [dict(zip(column_names, row)) for row in rows]

    

def lazy_pagination(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
