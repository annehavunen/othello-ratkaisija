# Viikkoraportti 6

Viikon teemana on ollut minimaxin tehostaminen ja yleinen optimointi.
Otin ohjaajan opastamana käyttöön välimuistin, johon talletetaan minimaxissa paras siirto tietyssä pelitilanteessa.
Opin ennen kaikkea yleisesti sen, että tehokkuuden merkityksen korostuessa täytyy koodissa kiinnittää huomiota pienempiin yksityiskohtiin,
mihin olen tottunut.

Ohjaussession suuntaamana jatkoin itsenäisesti monien pienien muutosten parissa,
joista kaikilla oli ainakin pieni myönteinen vaikutus ohjelman tehokkuuteen.
Muutoksista tärkeimmät olivat seuraavat:
Pelaajia ei ilmaista merkkijonoilla "valkoinen" ja "musta" vaan totuusarvoilla True ja False.
Pelilauta on pelin sisäisessä toteutuksessa kooltaan nyt 8x8 eikä 9x9.
Pelilaudan sisältö ilmaistaan merkkien sijaan numeroilla 0, 1 ja 2.
Pelaajan antamaa syötettä käsitellään pelin sisäisessä toteutuksessa merkkijonon sijaan tuplena, jossa on koordinaatit.

Ennen loppudemoa tavoitteeni on muuttaa pelilautaa ilmaiseva 2-ulotteinen lista numpy.arrayksi,
jonka pitäisi lisätä ohjelman tehokkuutta.
Saatan muuttaa pelilaudan käsittelyä niin, että pelilautaa kuljetetaan funktioiden parametrina.
Aion laajentaa testejä ja täydentää dokumentaatiota. 

Käytetty työaika: 15 h
