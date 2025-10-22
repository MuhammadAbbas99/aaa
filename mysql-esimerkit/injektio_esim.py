title = input("Input movie title:")
# tässä komentorivin input, mutta voisi olla 
# vaikka web-sivun käyttäjän nimi esim tsm.


sql = f"SELECT * from movies WHERE title = '{title}'"
cursor.execute(sql)

    #jos käyttäjä syättäisi titleiksi:
#   'OR1=1 --

#   SELECT * FROM movies WHERE TITLE = ' OR1=1

# Placeholder:
# SELECT * FROM movies WHERE title = ?
# ? ->raw data, ei string

# SQLITE ESIM,
cursor.execute("SELECT * FROM movies WHERE title =?" , ["Inception"])

PREPARE stmt FROM 'SELECT * FROM movies WHERE TITLE=?';
BIND 'Inception' to PARAM1;
EXECUTE stmt;

# Inception'; DROP TABLE movies;--  # -> luettaisiin ei osana SQL:lause