import mysql_connection as db

cursor = db.conn.cursor()
cursor.execute("CREATE DATABASE testDB") #will be done as testdb