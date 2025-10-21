import sqlite3          # tulee python-asennuksen mukana (versiosta 2.5>)
from pathlib import Path
import pandas as pd     # uv add pandas

# Luodaan tyhjä tiedosto (kuten Linuxissa)
Path('employees.db').touch()     # joka tämä rivi vai rivi10: conn = sqlite3.connect('movie.db')

# Luodaan tietokantaa ja kursoiri
conn = sqlite3.connect('employees.db')      # luo tiedoston jos ei löydy rivi 7:lta

#region_1_ Joka tämä koodi vai alhalla code-block (koodilohko)
'''cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees_table
               ("first_name" TEXT NOT NULL,
               "company_name" TEXT NOT NULL,
               "address" TEXT,
               "city" TEXT,
               "county" TEXT,
               "state" TEXT,
               "zip" INT,
               "phone1" NUMERIC,
               "phone2" NUMERIC,
               "email" TEXT,
               "web" TEXT)
               """)
'''
#endregion


# luetaan  csv-tiedosto pandasin dataframeen
employees = pd.read_csv('us-500.csv')


#region_2_: Joka tämä koodi vai ylhalla code-block (koodilohko)

    #kirjoitetaan dataframin sisältö sqlite-tauluun
                # taulu,    kanta,  vapaa valintaine,       lisääkö 1.kolumniksi index 0..n
employees.to_sql('employees_table', conn,   if_exists = 'replace',   index = True)
# employees.to_sql('employees_table', conn,   if_exists = 'append',   index = False)    
    # se luo uuden sarakkeen, joka nimetään replace:ata sen append:in sijaan
#endregion