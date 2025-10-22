import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" # NOTICE: country omitted
values = ("Diana", "AppleStreet 111")
cursor.execute(sql, values)

db.conn.commit() # REMEMBER