from copy import deepcopy
import time
from othello import Othello

PAINOT = [[120, -20, 20, 5, 5, 20, -20, 120],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [120, -20, 20, 5, 5, 20, -20, 120]]


class OthelloAI:
    def __init__(self):
        """Tekoäly, joka laskee tietokoneen siirron.
        Toteutettu minimax-algoritmilla ja tehostettu alfa-beeta-karsinnalla.
        """
    def valitse_siirto(self, syvyys, othello):
        """Aloittaa maksimoijan ensimmäisellä kierroksella ja kutsuu minimaxia.

        Args:
            syvyys: Kokonaisluku, jossa on suurin mahdollinen laskentasyvyys.
            othello: Othello-olio, joka sisältää nykyisen pelitilanteen.

        Returns:
            paras_siirto: Tuple, joka on tekoälyn valitseman siirron koordinaatit.
        """
        parhaat_siirrot = {}
        alfa = -100000
        beta = 100000
        jarjestetyt_siirrot = self.hae_jarjestetyt_siirrot(othello, True)
        paras_siirto = None
        for i in range(3, syvyys + 1):
            alfa = -100000
            paras_arvo = -100000
            start = time.time()
            for siirto in jarjestetyt_siirrot:
                kopio_othello = self.kopioi_othello(othello)
                if siirto != "x":
                    kopio_othello.tee_siirto(siirto, True, jarjestetyt_siirrot)
                arvo = self.minimax(i, kopio_othello, alfa, beta, False, parhaat_siirrot)
                if arvo > paras_arvo:
                    paras_arvo = arvo
                    paras_siirto = siirto
                    alfa = max(alfa, arvo)
            if time.time() - start > 2:
                break
            jarjestetyt_siirrot.remove(paras_siirto)
            jarjestetyt_siirrot.insert(0, paras_siirto)
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
            parhaat_siirrot: Dictionary, jossa pidetään kirjaa pelitilanteen parhaasta siirrosta.

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
                kopio_othello = self.kopioi_othello(othello)
                if siirto != "x":
                    kopio_othello.tee_siirto(siirto, True, mahdolliset_siirrot)
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
                kopio_othello = self.kopioi_othello(othello)
                if siirto != "x":
                    kopio_othello.tee_siirto(siirto, False, mahdolliset_siirrot)
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
        for i in range(8):
            for j in range(8):
                if pelilauta[i][j] == 2:
                    arvio += PAINOT[i][j]
                elif pelilauta[i][j] == 1:
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
            kopio_othello = self.kopioi_othello(othello)
            kopio_othello.tee_siirto(siirto, maksimoi_pelaaja, mahdolliset_siirrot)
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

    def kopioi_othello(self, othello):
        """Kopioi othello-olion ja palauttaa uuden kopion.

        Args:
            othello: Othello-olio, jossa on tämänhetkinen pelitilanne.

        Returns:
            kopio_othello: Uusi Othello-olio.
        """
        lauta = othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        return kopio_othello

def laske_avain(pelilauta, maksimoi_pelaaja):
    """Laskee kokonaisluvun, joka ilmaisee pelitilanteen eli pelilaudan yksiselitteisesti.

    Args:
        pelilauta: Matriisi, joka kuvaa pelitilannetta.
        maksimoi_pelaaja: Boolean, joka on True, jos on maksimoijan vuoro.

    Returns:
        avain: Kokonaisluku, joka ilmaisee pelitilanteen.
    """
    avain = 0
    for i in range(8):
        for j in range(8):
            if pelilauta[i][j] == 2:
                avain += 2
            elif pelilauta[i][j] == 1:
                avain += 1
            avain *= 3
    avain *= 2
    if maksimoi_pelaaja:
        avain += 1
    return avain
