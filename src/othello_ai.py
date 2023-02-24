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

# Kommentit ovat väliaikaisesti koodissa.
class OthelloAI:
    def __init__(self):
        """Tekoäly, joka laskee tietokoneen siirron.
        Toteutettu minimax-algoritmilla ja tehostettu alfa-beeta-karsinnalla.
        """
        # self.laskuri = 0
    def valitse_siirto(self, syvyys, othello):
        """Aloittaa maksimoijan ensimmäisellä kierroksella ja kutsuu minimaxia.

        Args:
            syvyys: Kokonaisluku, jossa on suurin mahdollinen laskentasyvyys.
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.

        Returns:
            paras_siirto: Tekoälyn valitsema siirto, joka on muodossa "a1".
        """
        parhaat_siirrot = {}
        alfa = -100000
        beta = 100000
        jarjestetyt_siirrot = self.hae_jarjestetyt_siirrot(othello, True)
        paras_siirto = None
        # self.laskuri = 0
        # print("jarjestetyt ennen nostoja: ", jarjestetyt_siirrot)
        # alkuaika = time.time()
        for i in range(3, syvyys + 1):
            # print("syvyys ", i)
            alfa = -100000
            paras_arvo = -100000
            start = time.time()
            for siirto in jarjestetyt_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, True)
                arvo = self.minimax(i, kopio_othello, alfa, beta, False, parhaat_siirrot)
                if arvo > paras_arvo:
                    paras_arvo = arvo
                    paras_siirto = siirto
                    alfa = max(alfa, arvo)
            if time.time() - start > 2:
                break
            jarjestetyt_siirrot.remove(paras_siirto)
            jarjestetyt_siirrot.insert(0, paras_siirto)
        #     print("paras siirto: ", paras_siirto)
        #     print("järjestetyt noston jälkeen: ", jarjestetyt_siirrot)
        # print("laskenta-aika: ", time.time() - alkuaika)
        # print("laskuri: ", self.laskuri)
        return paras_siirto

    def minimax(self, syvyys, othello, alfa, beta, maksimoi_pelaaja, parhaat_siirrot):
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
            # self.laskuri += 1
            arvio = self.arvioi_pelilauta(othello)
            return arvio

        if maksimoi_pelaaja:
            mahdolliset_siirrot = othello.mahdolliset_siirrot(True)
        else:
            mahdolliset_siirrot = othello.mahdolliset_siirrot(False)

        paras_siirto = None
        avain = 0
        if not mahdolliset_siirrot:
            mahdolliset_siirrot = ["x"]
        else:
            avain = laske_avain(othello.hae_pelilauta(), maksimoi_pelaaja)
            paras_siirto = parhaat_siirrot.get(avain)
            if paras_siirto:
                mahdolliset_siirrot.remove(paras_siirto)
                mahdolliset_siirrot.insert(0, paras_siirto)

        if maksimoi_pelaaja:
            paras_arvo = -100000
            for siirto in mahdolliset_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, True)
                arvo = self.minimax(syvyys - 1, kopio_othello, alfa, beta, False, parhaat_siirrot)
                if arvo > paras_arvo:
                    paras_arvo = arvo
                    paras_siirto = siirto
                alfa = max(alfa, paras_arvo)
                if paras_arvo >= beta:
                    break
            if mahdolliset_siirrot[0] != "x":
                parhaat_siirrot[avain] = paras_siirto
            return paras_arvo
        else:
            paras_arvo = 100000
            for siirto in mahdolliset_siirrot:
                kopio_othello = self.tee_siirto_ja_kopioi_othello(othello, siirto, False)
                arvo = self.minimax(syvyys - 1, kopio_othello, alfa, beta, True, parhaat_siirrot)
                if arvo < paras_arvo:
                    paras_arvo = arvo
                    paras_siirto = siirto
                beta = min(beta, paras_arvo)
                if paras_arvo <= alfa:
                    break
            if mahdolliset_siirrot[0] != "x":
                parhaat_siirrot[avain] = paras_siirto
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

    def hae_jarjestetyt_siirrot(self, othello, maksimoi_pelaaja):
        """Palauttaa pelaajan mahdolliset siirrot järjestyksessä, jossa ensin on siirrot,
        jotka kääntävät vähiten vastustajan nappuloita.

        Args:
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.
            maksimoi_pelaaja: Boolean, joka on maksimoijalla eli tekoälyllä True.

        Returns:
            jarjestetyt_siirrot: Lista, jossa on pelaajan mahdolliset siirrot järjestettyinä.
        """
        mahdolliset_siirrot = othello.mahdolliset_siirrot(maksimoi_pelaaja)
        maarat_siirrot = []
        for siirto in mahdolliset_siirrot:
            lauta = othello.hae_pelilauta()
            kopiolauta = deepcopy(lauta)
            kopio_othello = Othello(kopiolauta)
            kopio_othello.tee_siirto(siirto, maksimoi_pelaaja)
            if maksimoi_pelaaja:
                vastustajan_mahdolliset = kopio_othello.mahdolliset_siirrot(False)
            else:
                vastustajan_mahdolliset = kopio_othello.mahdolliset_siirrot(True)
            maarat_siirrot.append((len(vastustajan_mahdolliset), siirto))
        maarat_siirrot.sort()
        jarjestetyt_siirrot = []
        for maara_siirto in maarat_siirrot:
            jarjestetyt_siirrot.append(maara_siirto[1])
        return jarjestetyt_siirrot

    def tee_siirto_ja_kopioi_othello(self, othello, siirto, tekoalyn_vuoro):
        """Kopioi othello-olion, tekee halutun siirron ja palauttaa uuden kopion.

        Args:
            othello: Othello-olio, jossa on tämänhetkinen pelitilanne.
            siirto: Tieto siitä, mihin kohtaan siirto tehdään pelilaudalla.
            tekoalyn_vuoro: Boolean, joka ilmaisee, kumman pelaajan vuoro on.

        Returns:
            kopio_othello: Othello-olio, jossa on uusi pelitilanne.
        """
        lauta = othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        if siirto != "x":
            kopio_othello.tee_siirto(siirto, tekoalyn_vuoro)
        return kopio_othello

def laske_avain(pelilauta, maksimoi_pelaaja):
    """Laskee kokonaisluvun, joka ilmaisee pelitilanteen yksiselitteisesti.

    Args:
        pelilauta: Matriisi, joka kuvaa pelitilannetta.
        maksimoi_pelaaja: Boolean, joka on True, jos on maksimoijan vuoro.

    Returns:
        avain: Kokonaisluku, joka ilmaisee pelitilanteen.
    """
    avain = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if pelilauta[i][j] == "o":
                avain += 2
            elif pelilauta[i][j] == "x":
                avain += 1
            avain *= 3
    avain *= 2
    if maksimoi_pelaaja:
        avain += 1
    return avain
