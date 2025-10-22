import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

#sql = "DROP TABLE customers" 
sql = "DROP TABLE IF EXISTS customers" # to prevent errors if not found
cursor.execute(sql)