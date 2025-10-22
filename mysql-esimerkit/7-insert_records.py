import mysql_connection as db


cursor = db.conn.cursor()
cursor.execute("USE testDB")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, values)

db.conn.commit()
print(cursor.rowcount, "was inserted.")

# SHOW LAST INSERTED ID (needs commit to function)
print(cursor.lastrowid)

# RUN TWICE, PRACTICE DELETING DUPLICATES