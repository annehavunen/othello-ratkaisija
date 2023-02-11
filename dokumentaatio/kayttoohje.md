# Käyttöohje

Ohjeissa oletetaan, että koneelle on asennettu poetry ja vähintään Pythonin versio 3.8.

### Asennus

1. Kloonaa projekti komennolla:
> git clone git@github.com:annehavunen/othello-ratkaisija.git

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
