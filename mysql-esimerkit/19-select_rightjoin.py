import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")


# ALL PRODUCTS WITH MATCHING CUSTOMER ID (Customer=None, if no match found)
sql = "SELECT customers.name,products.name \
    FROM customers \
    RIGHT JOIN products ON customers.id = products.id" 

cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)