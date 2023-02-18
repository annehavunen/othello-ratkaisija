# Viikkoraportti 5

Sain tällä viikolla paljon apua erityisesti iteratiiviseen syvenemiseen, siirtojen järjestämiseen ja testitulostamiseen liittyen.
Ohjaussessio oli hyvin opettavainen ja tarpeellinen, sillä en olisi itse osannut edetä asioiden kanssa.

Testaamisen alaisena oli tutkia, miten siirtojen järjestäminen vaikuttaa tehokkuuteen.
Järjestämiskokeilu eteni kolmessa vaiheessa: siirtojen järjestäminen valitse_siirrossa, noston lisääminen valitse_siirtoon
sekä siirtojen järjestäminen minimaxissa.
Ideana oli, että jokainen edellä mainituista vähentää nollatason heuristiikan laskennan määrää tai nostaa laskentasyvyyttä. 
Ohjauksen lopussa kysymyksiä herätti se, miksi muutokset järjestämisessä tai nostoissa vaikuttivat tuloksiin yllättävän vähän.

Alun perin järjestämisalgoritmi oli sellainen, että ne siirrot ovat ensin, jotka kääntävät vähiten vastustajan nappuloita,
sillä tämä mainitaan joskus hyväksi alkuvaiheen strategiaksi.
Vaihdoin kuitenkin ne siirrot ensimmäiseksi, 
joiden jälkeen vastustajalla on vähiten mahdollisia siirtoja. 
Aiempaan verrattuna tämä antoi huomattavasti selkeämpiä tuloksia; 
erot nollaheuristiikan laskurissa olivat usein kymmenissätuhansissa, ja välillä laskentasyvyys parani yhdellä. 
Tämä oli muuten johdonmukaista, mutta siirtosarjoissa oli pari poikkeusta, joissa tulos pysyi samana tai huononi. 
Valitut siirrot olivat testisarjoissa samat, ja molemmat pelaajat tekivät kahdeksan siirtoa.

Tein tällä viikolla myös vertaisarvioinnin, päivitin tuttuun tapaan dokumentaatiota sekä yritin selvittää,
mistä transpositiotaulussa on kyse ja miten pelitilanteen voisi esittää kokonaislukuna.
Sinnikkäistä yrityksistäni huolimatta en käytännössä ratkaissut kumpaakaan asiaa.
Jos nämä haluaa vielä lisätä työhön, joudun turvautumaan ohjaajan apuun.

Viikko päättyi testiotteluun tietokonetta vastaan.
En ole erityisen hyvä othellossa, mutta oli silti mukavaa, kun tekoäly vihdoin päihitti minut.

Käytetty työaika: 10 h
