# ALX_prodev Database Seeder

This Python script sets up a PostgreSQL database named **`ALX_prodev`** for development purposes. It creates the database, defines a `user_data` table, and populates it from a CSV file.

## 📦 Project Structure

- `seed.py` – Contains functions to connect to the database, create the database and table, and insert data.
- `0-main.py` – Entry point to execute all the functions in order.
- `user_data.csv` – CSV file containing user data to seed the database.

## 📋 Requirements

- Python 3.6+
- PostgreSQL
- `psycopg2` Python package

Install dependencies:

```bash
pip install psycopg2
```
