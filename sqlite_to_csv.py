# DB Browsewr for sqlite: https://sqlitebrowser.org/dl/
# use DB Browser for SQLite - PortableApp

import sqlite3          # tulee python-asennuksen mukana (versiosta 2.5>)
import pandas as pd
from pathlib import Path
import csv

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

#rows = cursor.execute(" SELECT * FROM movies").fetchone()   # palautta 1.rivin
rows = cursor.execute(" SELECT * FROM movies")  #.fetchall() palautta listan

print(rows)
print(type(rows))

# for row in rows:
#    print(row)      # tulostan kokona csv-tiedosto sisältö komentorivissa

# helpompi tapa (jos onnistuu) - SQL-CSV pandas dataframella 
df = pd.read_sql("SELECT * FROM movies", conn)
# print(df)
df.to_csv('elokuvat_sqlista.csv', index = False)


