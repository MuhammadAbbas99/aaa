import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

sql = "UPDATE customers SET address = %s WHERE address = %s"
values =("Valley 345","Park Lane 38")

cursor.execute(sql,values)
db.conn.commit()

print(cursor.rowcount, "record(s) affected") # to see if anything changed