from seed import connect_to_prodev

def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    connection.close()
    return [
        {
            "user_id": str(row[0]),
            "name": row[1],
            "email": row[2],
            "age": int(row[3])
        }
        for row in rows
    ]

def lazy_pagination(page_size):
    """
    Generator that yields pages of user data lazily using pagination.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
