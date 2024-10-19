import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # Update with your host (e.g., '127.0.0.1')
            user="root",   # Update with your MySQL username
            password="harare"  # Update with your MySQL password
        )

        cursor = connection.cursor()
        db_name = "alx_book_store"
        
        # Create database if it doesn't exist
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
        
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: Incorrect username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)

if __name__ == "__main__":
    create_database()
