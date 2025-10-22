import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")
cursor.execute("ALTER TABLE customers ADD COLUMN IF NOT EXISTS country VARCHAR(30)")