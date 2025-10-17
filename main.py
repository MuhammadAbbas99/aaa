import sqlite3  #sqlite3 tulee python-asennusken mukana
import re       # regular expression

_IDENTIFIER_RE_ = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

#luo test.db tiedosto jos sitä ei ole samassa kansiossa
conn =  sqlite3.connect("test.db")

#luodaan kursori
cursor = conn.cursor()

def create_table():

    #annetaan kurosille sql-lause
    cursor.execute("""CREATE TABLE IF NOT EXISTS tyontekija (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL)
                """)

    #commit tulee käyttä INSERT, UPDATE, DELETE
    #Oletuksena sqlite:ssa auto-commit mode päällä
    conn.commit()     #tallentaa muutoksen pysyvästi


def insert_to_table():
#region huono tapa
    # mahdollistaa sql-injektion
    # (jos käyttään nimeä vaikka kysytään, 
    # hän voi syöttää nimen sijaan vahingollista sql-syntaksia)
    # cursor.execute("INSERT INTO tyontekija (name) VALUES ('"+username+"')")
#endregion

#region parempi tapa 
    # (estää injektion)
    cursor.execute("INSERT INTO tyontekija (name) VALUES (?)", ('RoopeAnkka',))
    conn.commit()
#endregion

#insert_to_table()
def insert_to(conn, table, columns:list, values):
    if not _IDENTIFIER_RE_.match(table):
        raise ValueError(f"Invalid table name")
    cols_sql = ",".join(columns)
    placeholders = ",".join(["?"]*len(values))
    sql= f"""INSERT INTO {table} ({cols_sql}) VALUES ({placeholders})"""
    cursor = conn.cursor()  # Tässä ei tarvittaisiin,
                            # mutta jos olisi vaikka loukan metodi

    try:
        cursor.execute(sql,values)
        conn.commit()
    # except jos halutaan logata tiedostoon tai konsoliin jotain
    finally:    # tänne mennään joka tapauksessa onnistui try tai ei
        cursor.close()
        # conn.close()

insert_to(conn, "tyontekija", ["name", "address", "email"], ["Superman", "Kotikuja 2", "superman@gmail.com"])
#cursor.close()


# Harjoitus
# Luo haluamallasi tavalla (komentorivi/GitHubDektop tms.
# Git GUI Client tai suoraan GiHubissa)
# ja vie main.py tiedosto ja test.db omaan githubisi.

def update_table():
    cursor.execute("UPDATE tyontekija SET address=? WHERE name=?", ("Valimotie 8", "Batman"))
    conn.commit()

update_table()
conn.close()