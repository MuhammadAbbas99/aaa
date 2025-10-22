import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for x in result:
  print(x)