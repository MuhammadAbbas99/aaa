import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

# CREATE ANOTHER TABLE WITH DATA FIRST
cursor.execute("CREATE TABLE IF NOT EXISTS products \
               (id INT AUTO_INCREMENT PRIMARY KEY, \
               name VARCHAR(255))")

sql = "INSERT INTO products (name) VALUES (%s)"
values = ("Chocolate Cake",) #notice tuple 
cursor.execute(sql, values)
db.conn.commit() # REMEMBER!

print(cursor.rowcount, "record(s) affected") 

#-------------------------------------

# JOIN = INNER JOIN, BOTH CAN BE USED
sql = "SELECT customers.name,products.name \
    FROM customers \
    INNER JOIN products ON customers.id = products.id" 

cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)