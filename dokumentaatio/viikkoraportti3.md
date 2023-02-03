# Viikkoraportti 3

Sain tällä viikolla paljon apua ohjaussessiosta.
Yritin muokata minimax-algoritmia toimivammaksi saamieni neuvojen perusteella. Lisäsin alfa-beeta-karsinnan. 
Poistin luokasta othello.py kolme luokkamuuttujaa, eli niiden suhteen toimitaan nyt parametrien avulla. 
Paransin heuristista arviointia siten, että jokaisella pelilaudan ruudulla on tietty paino. 
Arviointi tehdään laskemalla näitä painoja. Löysin arvot painoille internetistä [tältä](http://dhconnelly.com/paip-python/docs/paip/othello.html) sivulta,
mutta painoja voi tietysti säätää vielä myöhemmin.
Paransin testikattavuutta sekä aloitin testausdokumentin kirjoittamisen.

Tällä viikolla opin lisää minimaxista, alfa-beeta-karsinnasta sekä heuristisesta arvioinnista pelilaudan painoja hyödyntämällä.
Haasteena ovat silti edelleen kaikki edellä mainitut.
Jos ohjaaja ehtii, niin voisiko erityisesti OthelloAI-luokasta vilkaista, näkyykö siinä ainakaan päällisin puolin selviä virheitä? 
Tekoäly pelaa merkkiä "o" eli valkoista, valkoinen on maksimoija ja valitse_siirto-funktio on maksimoijan ensimmäinen kierros. 
Funktiota valitse_siirto ei kutsuta käyttöliittymästä, jos mahdollisia siirtoja ei ole. 

Ensi viikolla olisi OthelloAI-luokassa hyvä pyrkiä järjestämään mahdolliset siirrot parhaimmasta huonompaan,
että alfa-beeta-karsinta olisi tehokkaampi. Jos ymmärsin minimax-materiaalista oikein, 
niin yksinkertainen tapa järjestämiseen on tehdä jokaisesta siirrosta heuristinen arvio syvyydellä 1,
järjestää siirrot sen perusteella suurimmasta arviosta pienimpään ja sitten toteuttaa varsinainen minimax normaalisti.
Onko tähän kommenttia tai neuvoa?

Pian olisi syytä aloittaa suorituskykytestaus sekä OthelloAI-luokan testaus. En vielä tiedä, miten ne toteutetaan.
Lisäksi on ehkä aiheellista toteuttaa jokin pelisiirtoja sisältävä syötesarja, jonka ohjelma voi ajaa automaattisesti ilman manuaalista näppäilyä.

Käytetty työaika: 17h
