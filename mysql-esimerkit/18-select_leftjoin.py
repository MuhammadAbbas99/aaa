import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")


# ALL CUSTOMERS WITH MATCHING PRODUCT ID (Product=None, if no match found)
sql = "SELECT customers.name,products.name \
    FROM customers \
    LEFT JOIN products ON customers.id = products.id" 

cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)