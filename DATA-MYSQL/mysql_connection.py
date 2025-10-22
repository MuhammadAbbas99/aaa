
#region Python ohjeet (jos ilman uv:ta):
    # >python -m venv env    
    # >env\scripts\acivate      tai powershelliissa:  .\env\scripts\activate.psi
    # >pip install mysql.connector
#-------------------------------
#endregion
 

#region uv ohjeet
# # Terminal:issa asenna mysql.connector -moduuli
# (jos uv ei ole asennettu:)
# >winget install --id=astral-sh.uv -e

# >uv init
# >uv add mysql.connector


# download Xampp https://www.apachefriends.org/download.html
# in xampp folder:
# open xampp-control.exe
# Apache -> Start
# Mysql -> Start
# http://localhost:8000/phpmyadmin/      # databases will be created here.


import mysql.connector
import secret       #importattu samasta kansiosta secret.py:sta

# testataan yhetyttä
try:
    conn = mysql.connector.connect(
        host="localhost",
        #user="joulupukki",         # manuaali
        user=secret.USER,           # username importattu käyttäjä.py:sta
        #password="joulu!",         #,  # pilkku tarvitaan jos database määritetty
        password=secret.PASSWORD,    # importattu secret.py tiedostosta
        database="harjoitus"       # käyttä sql_harjoitukseele
    )
    if conn.is_connected():
        print("yhteys muodostettiin!")
        print(conn.get_server_info())
except:
    print("yhteys ei onnistunut!")

#finally:    # mennään joka tapauksessa
#    if conn.is_connected():
#        print("connectiuon suljettu")
#        conn.close()

#endregion

# aja  komennolla:
# >uv run mysql_connection.py