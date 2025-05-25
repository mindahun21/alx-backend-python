import sqlite3


class ExecuteQuery:

    def __init__(self, db_name, query, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    db_file = "users.db"

    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(db_file, query, (25,)) as result:
        print("Users older than 25:")
        for row in result:
            print(row)
