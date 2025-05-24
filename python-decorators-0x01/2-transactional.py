import sqlite3 
import functools
with_db_connection = __import__('1-with_db_connection').with_db_connection

def transactional(func):
  @functools.wraps(func)
  def wrapper(con, *args, **kwargs):
    try:
      result = func(con, *args, **kwargs)
      con.commit()
      return result
    except Exception as e:
      con.rollback()
      print("Transaction Failed {e}")
      raise
    
  return wrapper 

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
  cursor = conn.cursor() 
  cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, user_id)) 
  #### Update user's email with automatic transaction handling 

update_user_email(user_id=2, new_email='Crawford_Cartwright@hotmail.com')