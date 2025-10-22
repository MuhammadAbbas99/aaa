import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

#sql = "DELETE FROM customers WHERE name = 'Ben'" # syntax ok, but not preferred
sql = "DELETE FROM customers WHERE name =%s" # use %s also here!
value = ('Susan',)
cursor.execute(sql,value)
db.conn.commit()