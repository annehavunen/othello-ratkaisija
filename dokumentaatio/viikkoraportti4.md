# Viikkoraportti 4

Ensimmäisiä muutoksia koodiin tällä viikolla oli pelilaudan siirtojen järjestäminen alfa-beeta-karsinnan tehostamiseksi.
Siirrot järjestetään valitse_siirto-funktiossa siten, että vähiten vastustajan nappuloita kääntävät siirrot ovat ensiksi.
Lukemani mukaan tämä on usein paras taktiikka, vaikka loppuvaiheessa yritetäänkin vallata vastustajan nappulat.

Aloitin OthelloAI-luokan testaamisen ja huomasin, että jokin meni koko ajan pieleen tekoälyn toiminnassa.
Yhdeksi syylliseksi osoittautui vähän yllättäenkin pelilaudan kopioiminen,
joten tee_siirto_ja_kopioi_othello-funktiossa on ainakin tällä hetkellä massiivinen kopiointirumba virheen välttämiseksi.

Havaitsin toiseksi ongelmaksi sen, että tekoäly ei osannut reagoida sellaiseen tilanteeseen,
jossa pelaaja1 tekee siirron, pelaaja2 ei pysty tekemään siirtoa ja pelaaja1 jatkaa sen jälkeen, ehkä jopa voittosiirrolla.
Pelkkä heuristinen arvio olisi nähdäkseni tässä kohtaa riittämätön,
sillä pelaaja1:lle on edullista ja myös sääntöjen mukaista jatkaa peliä.
Olenkin pyrkinyt ottamaan tilanteen huomioon siten, että jos pelaajalla ei ole siirtoja, käydään läpi vastustajan siirtoja.

Minimax-parannusten jälkeen nostin testikattavuutta ja päivitin dokumentaatiota monin tavoin.
Opin minimaxin testaamisesta muun muassa, että varmuudella voidaan tietää vain paras siirto 
ja erityisasemassa ovat voitot ja tappiot. 
Pelin tulee pyrkiä voittamaan nopeasti ja häviämään hitaasti. 
Tämä selkeytti testaamista, vaikka olenkin sen suhteen yhä epävarma.

Ensi viikolla voisin ainakin toteuttaa iteratiivisen syvenemisen sekä täydentää dokumentaatiota.
En kuitenkaan tiedä, mitä iteratiivisella syvenemisellä tarkoitetaan, joten voisinko saada siihen neuvoa?
Saan sen käsityksen, että osittain asia liittyy siihen, että minimax laskee siirtoja niin syvälle kuin se ehtii asetetussa aikarajassa.
Materiaalissa tähän kuitenkin liitetään myös siirtojen järjestäminen 
ja lisäksi mainitaan, että riippuu tapauksesta, "miltä syvyydeltä kannattaa aloittaa".
En siis ymmärrä, mitä kokonaisuudessaan haetaan.

Käytetty työaika: 15 h
