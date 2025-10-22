
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


import mysql.connector
import secret
try:
    conn = mysql.connector.connect(
        host="localhost",
        user=secret.USER,            # username importattu käyttäjä.py:sta
        #password="joulu!",      #,  # pilkku tarvitaan jos database määritetty
        password=secret.PASSWORD,     # importattu secret.py tiedostosta
        database="harjoitus")
        
    if conn.is_connected():
        print("yhteys muodostettiin!")
        print(conn.get_server_info())
except:
    print("yhteys ei onnistunut!")
