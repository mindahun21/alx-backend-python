import sqlite3 
import functools

seed = __import__('seed')

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      con = seed.connect_to_sqlite()
      result = func(con, *args, **kwargs)
      con.close()
      return result
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
  cursor = conn.cursor() 
  cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) 
  return cursor.fetchone() 

user = get_user_by_id(user_id=1)
print(user)