# Määrittelydokumentti

Othello-ratkaisija on toteutettu Python-ohjelmointikielellä suomeksi. Harjoitustyö on osa tietojenkäsittelytieteen kandidaatin tutkintoa.

Ratkaisija on minimax-algoritmilla toteutettu tekoäly, jota vastaan käyttäjä voi pelata.
Othello on kaksin pelattava, täydellisen tiedon nollasummapeli, ja minimax on yleinen ratkaisualgoritmi tämän tyylisissä peleissä.
Algoritmia tehostaa alfa-beeta-karsinta.
Siirtojen järjestäminen tehostaa minimaxia edelleen, ja iteratiivinen syveneminen tuo joustavuutta laskentasyvyyteen. 

Minimax-algoritmin aikavaativuus on eksponentiaalinen suhteessa laskennan syvyyteen,
minkä vuoksi laskennan tehostaminen on suotavaa.

Peli visualisoidaan ASCII-grafiikalla ja sitä pelataan tekstikäyttöliittymällä. 
Ohjelma saa syötteenä käyttäjän tekemän siirron ja ratkaisija laskee sen perusteella seuraavan siirron.
Käyttäjä antaa syötteen muodossa "a1" ja ohjelma muuntaa sen pelilaudan koordinaatit sisältäväksi monikoksi.
Tausta-ajatuksena on niin sanottu pelipuu, jossa jokainen mahdollinen siirto synnyttää joukon mahdollisia vastustajan siirtoja.
Tekoäly käy mahdollisuuksia läpi ja valitsee siirron, joka johtaa pelipuussa sille suotuisimpaan pelitilanteeseen.

# Lähteet

["Minimax", Wikipedia (2022)](https://en.wikipedia.org/wiki/Minimax)

[Minimax-pelit](https://tiralabra.github.io/2023_p3/fi/aiheet/minimax.pdf)

[Barber, A.; Pretorius, W.; Qureshi, U.; Kumar, D. (2020). "An Analysis of Othello AI Strategies"](https://barberalec.github.io/pdf/An_Analysis_of_Othello_AI_Strategies.pdf)
