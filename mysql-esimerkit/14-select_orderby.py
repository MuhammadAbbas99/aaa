import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

# ALPHABETICALLY BY COLUMN
cursor.execute("SELECT * FROM customers ORDER BY name")
result = cursor.fetchall()

for x in result:
  print(x)

# ALPHABETICALLY BY COLUMN REVERSED 
cursor.execute("SELECT * FROM customers ORDER BY name DESC")
result = cursor.fetchall()

for x in result:
  print(x)