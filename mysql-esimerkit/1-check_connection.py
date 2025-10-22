# python -m venv env
# env\scripts\activate
# pip install mysql-connector-python

import mysql_connection as db

try:
    print(db.conn)
except:
    print("no connection to db")
