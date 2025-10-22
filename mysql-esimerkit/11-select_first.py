import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

cursor.execute("SELECT * FROM customers")
result = cursor.fetchone()

print(result)