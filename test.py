import mysql.connector

connection = mysql.connector.connect(
            host="localhost",       # Update with your host (e.g., '127.0.0.1')
            user="root",   # Update with your MySQL username
            password="harare" # Update with your MySQL password
        )

mydb = connection.cursor()

mydb.execute("show databases")

for i in mydb:
    print(i)