# Tehtävä 2.
'''
content - f.read()
    - lukee koko tiedoston tai määritetyn määrän tavuje YHDEKSI STRINGIKSI
    - palauttaa stringiä koko tiedoston ssältö
    print(content[0:50])    # lukisi 50 ensimmäisiä merkiä
    - hyvä suhteelisen pieniin tiedostoihin

lines - file.readlines()
    - luke tiedostoon sisällö LISTAKSI RIVEJÄ
    - palautta listan string-muotoisena, jokainen aikoion listassa on yksi rivi
    - hyvä käyttä, jos haluaa yksittäisiä rivejä manipuloida
    - jos on iso tiedosto, parempi käuydä riviltä läpi:
        for line in f:
            ...mitä haluaakaan tehdä    # muistille kevyempi

f.write("HWELLO WORLD")
    - HUOMIO: EI AUTOMAATISESTI LISÄÄ \n
    - hyvä jos haluaa kirjoittaa yhden pitkä stringin tai rivi riviltä tiedostoa

    
lines = ["Rivi" 1\n", "Rivi 2\n", "Rivi 3\n"]
f.writelines(lines)
    - HUOMIO: EI AUTOMAATISESTI newlines \n
    - hyvä jos haluaa kirjoittaa useita rivejä kerralla tai muokattuaan tiedostton sisältö

'''

# luetaan vanha tiedoston sisältö muuttujaan
with open('tekstia.txt', 'r') as f:
    vanha_teksti = f.read() 
    # löytyy read(), readlines(), write(), writelines()

'''
#kirjoitetaan ussi teksti ennen vanhaa sisältöa
with open('tekstia.txt','w+') as f:
    f.write('HELLO WORLD\n' + vanha_teksti)
'''

# jos tiedoston loppuun
with open('tekstia.txt','a') as f:
    f.write('\nVIIMMEINEN RIVI\n')

# from pathlib import Path
# file_path = Path ("tekstia".txt)
#   if file_path_exists():      # jos tiedosto löytyi
    # ...