import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")
cursor.execute("DELETE c1 FROM customers c1 \
               INNER JOIN customers c2 \
               WHERE \
               c1.id > c2.id AND \
               c1.name = c2.name AND \
               c1.address = c2.address")

db.conn.commit()