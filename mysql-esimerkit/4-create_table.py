import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB") # no need if database specified in mysql_connection
cursor.execute("CREATE TABLE IF NOT EXISTS customers \
               (id INT AUTO_INCREMENT PRIMARY KEY, \
               name VARCHAR(255), \
               address VARCHAR(255))")
