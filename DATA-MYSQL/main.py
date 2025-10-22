import mysql_connection as db       # ajaa mysql_connection.py-moduuliin

def main():
    #print("Hello from data-mysql!")
    
    # tulostetaan tietokannat #pass
    cursor = db.conn.cursor()
    cursor.execute("SHOW DATABASES")

    for database in cursor:
        print(database)

    db.conn.close()

if __name__ == "__main__":
    main()
