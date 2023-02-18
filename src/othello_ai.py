from copy import deepcopy
import time
from othello import Othello

PAINOT = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 120, -20, 20, 5, 5, 20, -20, 120],
        [0, -20, -40, -5, -5, -5, -5, -40, -20],
        [0, 20, -5, 15, 3, 3, 15, -5, 20],
        [0, 5, -5, 3, 3, 3, 3, -5, 5],
        [0, 5, -5, 3, 3, 3, 3, -5, 5],
        [0, 20, -5, 15, 3, 3, 15, -5, 20],
        [0, -20, -40, -5, -5, -5, -5, -40, -20],
        [0, 120, -20, 20, 5, 5, 20, -20, 120]]


class OthelloAI:
    def __init__(self):
        """Tekoäly, joka laskee tietokoneen siirron.
        Toteutettu minimax-algoritmilla ja tehostettu alfa-beeta-karsinnalla.
        """
    def valitse_siirto(self, syvyys, othello):
        """Aloittaa maksimoijan ensimmäisellä kierroksella ja kutsuu minimaxia.
        Laskee niin syvälle kuin aikarajan puitteissa ehtii.

        Args:
            syvyys: Kokonaisluku, jossa on suurin mahdollinen laskentasyvyys.
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.

        Returns:
            paras_siirto: Tekoälyn valitsema siirto, joka on muodossa "a1".
        """
        alfa = -100000
        beta = 100000
        jarjestetyt_siirrot = self.hae_jarjestetyt_siirrot(othello, "valkoinen")
        paras_siirto = None
        for i in range(2, syvyys + 1):
            alfa = -100000
            paras_arvo = -100000
            start = time.time()
            for siirto in jarjestetyt_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, "valkoinen")
                arvo = self.minimax(i, kopio_othello, alfa, beta, False)
                if arvo > paras_arvo:
                    paras_arvo = arvo
                    paras_siirto = siirto
                    alfa = max(alfa, arvo)
            if time.time() - start > 2:
                break
            jarjestetyt_siirrot.remove(paras_siirto)
            jarjestetyt_siirrot.insert(0, paras_siirto)
        return paras_siirto

    def minimax(self, syvyys, othello, alfa, beta, maksimoi_pelaaja):
        """Rekursiivinen funktio, jossa käydään läpi siirtoja ja arvioidaan niiden hyvyyttä.
        Minimoija ja maksimoija vuorottelevat.

        Args:
            syvyys: Kokonaisluku, joka ilmaisee laskentasyvyyttä.
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.
            alfa: Kokonaisluku, jota käytetään alfa-beeta-karsintaan.
            beta: Kokonaisluku, jota käytetään alfa-beeta-karsintaan.
            maksimoi_pelaaja: Boolean, josta tiedetään, onko minimoijan vai maksimoijan vuoro.

        Returns:
            Arvo, jonka perusteella valitse_siirto etsii parasta siirtoa.
        """
        if othello.game_over():
            voittaja = othello.hae_voittaja()
            if voittaja == "valkoinen":
                return 10000 + syvyys
            if voittaja == "musta":
                return -10000 - syvyys
            return 0
        if syvyys == 0:
            arvio = self.arvioi_pelilauta(othello)
            return arvio

        if maksimoi_pelaaja:
            mahdolliset_siirrot = othello.mahdolliset_siirrot("valkoinen")
        else:
            mahdolliset_siirrot = othello.mahdolliset_siirrot("musta")

        if mahdolliset_siirrot:
            if maksimoi_pelaaja:
                mahdolliset_siirrot = self.hae_jarjestetyt_siirrot(othello, "valkoinen")
            else:
                mahdolliset_siirrot = self.hae_jarjestetyt_siirrot(othello, "musta")

        if not mahdolliset_siirrot:
            mahdolliset_siirrot = ["x"]

        if maksimoi_pelaaja:
            paras_arvo = -100000
            for siirto in mahdolliset_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, "valkoinen")
                paras_arvo = max(paras_arvo, self.minimax(syvyys - 1, kopio_othello, alfa, beta, False))
                alfa = max(alfa, paras_arvo)
                if paras_arvo >= beta:
                    break
            return paras_arvo
        else:
            paras_arvo = 100000
            for siirto in mahdolliset_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, "musta")
                paras_arvo = min(paras_arvo, self.minimax(syvyys - 1, kopio_othello, alfa, beta, True))
                beta = min(beta, paras_arvo)
                if paras_arvo <= alfa:
                    break
            return paras_arvo

    def arvioi_pelilauta(self, othello):
        """Laskee heuristisen arvion pelitilanteen hyvyydestä.

        Args:
            othello: Othello-olio, joka sisältää arvioitavan pelitilanteen.

        Returns:
            arvio: Kokonaisluku, joka on laskettu pelilaudan painojen mukaan.
        """
        pelilauta = othello.hae_pelilauta()
        arvio = 0
        for i in range(9):
            for j in range(9):
                if pelilauta[i][j] == "o":
                    arvio += PAINOT[i][j]
                elif pelilauta[i][j] == "x":
                    arvio -= PAINOT[i][j]
        return arvio

    def hae_jarjestetyt_siirrot(self, othello, pelaaja):
        """Palauttaa pelaajan mahdolliset siirrot järjestyksessä, jossa ensin on siirrot,
        jotka kääntävät vähiten vastustajan nappuloita.

        Args:
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.
            pelaaja: Vuorossa olevan pelaajan väri.

        Returns:
            jarjestetyt_siirrot: Lista, jossa on pelaajan mahdolliset siirrot järjestettyinä.
        """
        mahdolliset_siirrot = othello.mahdolliset_siirrot(pelaaja)
        maarat_siirrot = []
        for siirto in mahdolliset_siirrot:
            lauta = othello.hae_pelilauta()
            kopiolauta = deepcopy(lauta)
            kopio_othello = Othello(kopiolauta)
            kopio_othello.tee_siirto(siirto, pelaaja)
            if pelaaja == "valkoinen":
                vastustajan_mahdolliset = kopio_othello.mahdolliset_siirrot("musta")
            else:
                vastustajan_mahdolliset = kopio_othello.mahdolliset_siirrot("valkoinen")
            maarat_siirrot.append((len(vastustajan_mahdolliset), siirto))
        maarat_siirrot.sort()
        jarjestetyt_siirrot = []
        for maara_siirto in maarat_siirrot:
            jarjestetyt_siirrot.append(maara_siirto[1])
        return jarjestetyt_siirrot

    def tee_siirto_ja_kopioi_othello(self, othello, siirto, vari):
        """Kopioi othello-olion, tekee halutun siirron ja palauttaa uuden kopion.

        Args:
            othello: Othello-olio, jossa on tämänhetkinen pelitilanne.
            siirto: Tieto siitä, mihin kohtaan siirto tehdään pelilaudalla.
            vari: Siirron tekevän maan väri.

        Returns:
            kopio_othello: Othello-olio, jossa on uusi pelitilanne.
        """
        lauta = othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        if siirto != "x":
            kopio_othello.tee_siirto(siirto, vari)
        lauta = kopio_othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        return kopio_othello
