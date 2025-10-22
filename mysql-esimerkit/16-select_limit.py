import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

# LIMIT TO FIRST 5 RESULTS
cursor.execute("SELECT * FROM customers LIMIT 5") 
result = cursor.fetchall()

for x in result:
  print(x)


print("\n")

# IGNORE FIRST 2 RESULTS AND LIMIT TO 5 (NEXT) RESULTS
cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
result = cursor.fetchall()

for x in result:
  print(x)