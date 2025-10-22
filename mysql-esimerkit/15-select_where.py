import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

# EXACT MATCH
cursor.execute("SELECT * FROM customers WHERE name='Michael'")
result = cursor.fetchall()

for x in result:
    print(x)

# EXACT MATCH (WITH VARIABLE, PREFERRED (PREVENTS SQL INJECTION))

sql = ("SELECT * FROM customers WHERE name=%s")
value = ("Michael",) # must be of type list, tuple or dict
cursor.execute(sql,value)
result = cursor.fetchall()

for x in result:
    print(x)
