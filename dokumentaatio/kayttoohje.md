# Käyttöohje

Ohjeissa oletetaan, että koneelle on asennettu Poetry ja vähintään Pythonin versio 3.8.

### Asennus

1. Kloonaa projekti komennolla:
> git clone git<span>@</span>github.com:annehavunen/othello-ratkaisija.git

2. Siirry kansion sisään. Asenna riippuvuudet komennolla:
> poetry install

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:
>poetry run python3 src/index.py

### Testaaminen

Testit suoritetaan komennolla:
>poetry run coverage run --branch -m pytest

Testikattavuuden voi generoida komennolla:
>poetry run coverage html

Raportti generoituu *htmlcov*-hakemistoon.

### Pylint

Tiedoston [.pylintrc](https://github.com/annehavunen/othello-ratkaisija/blob/master/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:
>poetry run pylint src

### Pelin pelaaminen

Käyttäjä pelaa mustaa väriä, jota edustaa symboli "x", 
ja tekoäly valkoista, jota edustaa "o".
Syöte annetaan tekstikäyttöliittymässä muodossa "a1".
Kirjain merkitsee saraketta ja numero riviä.
Peli päättyy, kun kummallakaan pelaajalla ei ole mahdollisia siirtoja,
tai keskeyttämällä sen syötteellä "q".
Tavoitteena on, että pelin päättyessä enemmistö pelilaudan nappuloista on omaa väriä.
Säännöt voi tarkistaa Wikipediasta:
<https://fi.wikipedia.org/wiki/Othello_(lautapeli)>
