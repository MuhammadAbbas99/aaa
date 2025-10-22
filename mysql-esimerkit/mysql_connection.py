import mysql.connector
import pw


try:
    conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password=pw.PASSWORD
    # optional:
    #,
    #database="mydatabase"
    )

except:
    print("check connection parameters")



