import mysql.connector
from contextlib import contextmanager

# Database connection details
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "autoapply_db"
}

@contextmanager
def get_db_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    try:
        yield connection
    finally:
        connection.close()
