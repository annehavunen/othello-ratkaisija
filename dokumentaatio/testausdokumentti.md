# Testausdokumentti

![Testikattavuusraportti](testikattavuusraportti.png)

Sovelluksessa on tehty yksikkötestaus tiedostosta othello.py, jossa sijaitsee pelin toteuttava luokka Othello.
Kirjoitushetkellä kaikki muu on testattu paitsi pelilaudan tulostava funktio.
Käytössä on luokka PelilautaStub, josta haetaan testiluokan käyttöön erilaisia pelilautoja eli pelitilanteita.
Pelilautojen ja mahdollisten siirtojen avulla testataan erilaisia skenaarioita 
ja tutkitaan, toimivatko luokan Othello funktiot ennakoidulla tavalla.

Tällä hetkellä pystyn ajamaan testit ja luomaan kattavuusraportin virtuaaliympäristössä komennolla coverage run --branch -m pytest; coverage html.
Myöhemmin testien (ja yleensäkin ohjelman) ajamisesta tulee ohje githubiin.
Raporttiin kuuluvat tiedostot othello.py ja othello_ai.py, mutta vain othello.py on toistaiseksi testattu.
