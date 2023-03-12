# Määrittelydokumentti

Othello-ratkaisija on toteutettu Python-ohjelmointikielellä suomeksi. Harjoitustyö on osa tietojenkäsittelytieteen kandidaatin tutkintoa.

Ratkaisija on minimax-algoritmilla toteutettu tekoäly, jota vastaan käyttäjä voi pelata.
Othello, toiselta nimeltään reversi, on kaksin pelattava, täydellisen tiedon nollasummapeli, ja minimax on yleinen ratkaisualgoritmi tämän tyylisissä peleissä.
Algoritmia tehostaa alfa-beeta-karsinta.

Minimax on peruuttavaan hakuun ja raakaan voimaan perustuva algoritmi.
Othello-ratkaisijassa tekoäly on maksimoiva osapuoli.
Se käy läpi kaikki mahdolliset aloittavat siirtonsa ja kysyy minimoijalta, mikä on tämän paras siirto kussakin seuraavassa pelitilanteessa.
Minimoija käy puolestaan läpi omat siirtonsa ja kysyy taas maksimoijan parasta siirtoa näissä tilanteissa.
Näin käydään läpi kaikki mahdolliset pelitilanteet, kunnes saavutetaan tietty syvyys tai pelin päättävä tilanne.

Koska jokaisessa pelitilanteessa käydään lähtökohtaisesti läpi kaikki mahdolliset siirrot,
on minimax-algoritmin aikavaativuus eksponentiaalinen suhteessa laskennan syvyyteen.
Tämän vuoksi minimaxia tehostetaan alfa-beeta-karsinnalla, jolla karsitaan läpikäytäviä siirtoja.
Tämä ei sinänsä muuta aikavaativuutta, mutta yleensä kuitenkin tehostaa minimaxia merkittävästi.

Alfa-beeta-karsinnan tehokkuus riippuu siirtojen järjestyksestä.
Mikäli paras siirto käydään läpi viimeiseksi, ei siirtoja päästä karsimaan lainkaan.
Pelissä saattaa myös olla tilanteita, johon päädytään usean eri siirtosarjan kautta.
On edullista, jos jo aiemmin laskettua tietoa päästään näissä tapauksissa hyödyntämään.
Othello-ratkaisijassa tallennetaan tieto kierroksen parhaasta siirrosta ja pelitilanteesta transpositiotauluun.
Mikäli myöhemmin kohdataan sama pelitilanne, nostetaan siihen liitetty siirto läpikäytävien siirtojen ensimmäiseksi.
Transpositiotaulu ei vaadi erityisiä tietorakenteita, vaan se on toteutettu Pythonin dictionary-hajautustaululla.

Peli visualisoidaan ASCII-grafiikalla ja sitä pelataan tekstikäyttöliittymällä.
Ohjelma saa syötteenä käyttäjän tekemän siirron ja ratkaisija laskee sen perusteella seuraavan siirron.
Käyttäjä antaa syötteen muodossa "a1" ja ohjelma muuntaa sen pelilaudan koordinaatit sisältäväksi monikoksi.

# Lähteet

["Minimax", Wikipedia (2022)](https://en.wikipedia.org/wiki/Minimax)

[Minimax-pelit](https://tiralabra.github.io/2023_p3/fi/aiheet/minimax.pdf)

[Barber, A.; Pretorius, W.; Qureshi, U.; Kumar, D. (2020). "An Analysis of Othello AI Strategies"](https://barberalec.github.io/pdf/An_Analysis_of_Othello_AI_Strategies.pdf)
