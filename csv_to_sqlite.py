import sqlite3          # tulee python-asennuksen mukana (versiosta 2.5>)

from pathlib import Path
import pandas as pd     # uv add pandas

# Luodaan tyhjä tiedosto (kuten Linuxissa)
# Path('movies.db').touch()     # joka tämä rivi vai rivi conn = sqlite3.connect('movie.db')

# Luodaan tietokantaa ja kursoiri
conn = sqlite3.connect('movies.db')      # luo tiedoston jos ei löydy rivi 7:lta

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS movies
               (id INT,
               title TEXT, 
               overview TEXT,
               popularity REAL,
               release_date TEXT,
               vote_average REAL,
               vote_count INT)
               """)

# Ota teamsista Top_rated_movies1.csv -tiesodsto projektikanisoon

# luetaan  csv-tiedosto pandasin dataframeen
movies = pd.read_csv('Top_rated_movies1.csv')

#kirjoitetaan dataframin sisältö sqlite-tauluun
            # taulu,    kanta,  vapaa valintaine,       lisääkö 1.kolumniksi index 0..n
movies.to_sql('movies', conn,   if_exists = 'append',   index = False)
# movies.to_sql('movies', conn,   if_exists = 'replace',   index = True)    
    # se luo uuden sarakkeen, joka nimetään replace:ata sen append:in sijaan

    
