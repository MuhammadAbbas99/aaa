# HARJOITUS:

# luo python-skripti(t) joka luo mysql-tietokannan ja tauln ja lisää
# sinne dataa. Voit käyttään mysql_connection.py -tiedostoa.

# Jos tiedät jo, mitren CREAT TABLE yms. toimii, niin
# voit graafisesti myös luoda tietokannan ja taulun ja dataa, ja tehdä funktioita,
# jotka palauttavar dataa pythoniin muuttuujii(voit tulosta skriptilla
# mysql-kannasta haluamasi asioita).


# VINKKI: (KATSO esimerkkejä tarvittasessa Teamsistä .zip-tiedostosta)
# import mysql_connection2 as db

# cursor = db.conn.cursor()
# sql = "INSERT INTO employees(name) VALUES(%s)"
# values = (username,)    # esim.
# cursor.execute(sql,values)
# db.conn.commit()

import mysql_connection as db

cursor = db.conn.cursor()
#cursor.execute("CREATE DATABASE harjoitus") #will be done as harjoitusDB

#Luo tietokanta
cursor.execute("USE harjoitus") # no need if database specified in mysql_connection2
cursor.execute("CREATE TABLE IF NOT EXISTS employees \
               (id INT AUTO_INCREMENT PRIMARY KEY, \
               name VARCHAR(255))")

db.conn.commit()

#INSERT monta arvot
sql = "INSERT IGNORE INTO employees (id, name) VALUES (%s, %s)"
values = [('0', 'Johnny'),
          ('1', 'Mikey'),
          ('2', 'Leevi'),
          ('3', 'Kalle'),
          ('4', 'Holma'),
          ('5', 'Scott'),
          ('6', 'ABBA')
          ]
cursor.executemany(sql, values)

db.conn.commit()
print(cursor.rowcount, "row(s) inserted.")

# SHOW LAST INSERTED ID (needs commit to function)
print(cursor.lastrowid)
db.conn.commit()


     # UPDATE name nettisivu tietokanta
sql = "UPDATE employees SET name = %s WHERE name = %s"
values =("DREAM THEATRE","ABBA")

# #     # UPDATE id nettisivu tietokanta
# # sql = "UPDATE employees SET id = %s WHERE id = %s"
# # values =("2","22")

# cursor.execute(sql,values)
# db.conn.commit()

# sql = "DELETE FROM employees WHERE id=%s name =%s"  # use %s also here!
# value = ("22","Leevi")
# cursor.execute(sql,value)
# db.conn.commit()