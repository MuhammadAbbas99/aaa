import mysql_connection as db

cursor = db.conn.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)