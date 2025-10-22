import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

# USING WILDCARDS
sql = ("SELECT * FROM customers WHERE name LIKE %s")
value = ("%Mich%",) # must be of type list, tuple or dict
cursor.execute(sql,value)
result = cursor.fetchall()

for x in result:
    print(x)