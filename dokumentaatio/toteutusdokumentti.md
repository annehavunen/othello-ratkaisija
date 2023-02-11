# Toteutusdokumentti

Othello-ohjelman toteutus jakautuu kolmeen luokkaan: UI, Othello ja OthelloAI.
Näiden lisäksi on tiedosto index,py, josta peli käynnistetään.
Käyttöliittymä sijaitsee luokassa UI, ja siellä tapahtuu kommunikointi käyttäjän kanssa
ja yleensäkin peliä pyörittävä silmukka.
Luokassa Othello on pelin tarvitsemat toiminnot, 
kuten mahdollisten siirtojen hakeminen, siirron toteutus ja pelitilanteen laskeminen.
OthelloAI on minimax-tekoälyn toteuttava luokka.
Sovelluksessa tekoäly pelaa valkoista (joka on tekstikäyttöliittymässä "o").

Sovelluksessa yksikkötestataan luokkia Othello ja OthelloAI.
Testit hyödyntävät luokkaa PelilautaStub, jossa on erilaisia pelilautoja tilanteiden tutkimiseksi.

Algoritmin aikavaativuus on eksponentiaalinen suhteessa laskennan syvyyteen.
Erityisiä tietorakenteita ei esim. listojen lisäksi tarvita.

Työtä voisi parantaa ainakin lisäämällä iteratiivisen syvenemisen sen sijaan,
että lasketaan aina jollekin kiinteälle syvyydelle.


## Lähteet

[Minimax-pelit](https://tiralabra.github.io/2023_p3/fi/aiheet/minimax.pdf)