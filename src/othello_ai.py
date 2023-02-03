from copy import deepcopy
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
    def valitse_siirto(self, syvyys, othello):
        alfa = -100000
        beta = 100000
        mahdolliset_siirrot = othello.mahdolliset_siirrot("valkoinen")
        paras_siirto = None
        paras_arvo = alfa
        for siirto in mahdolliset_siirrot:
            kopio_othello = self.tee_siirto_ja_kopioi_lauta(othello, siirto, "valkoinen")
            arvo = self.minimax(syvyys - 1, kopio_othello, alfa, beta, False)
            if arvo > paras_arvo:
                paras_arvo = arvo
                paras_siirto = siirto
                alfa = max(alfa, arvo)
        return paras_siirto

    def minimax(self, syvyys, othello, alfa, beta, maksimoi_pelaaja):
        if othello.game_over():
            voittaja = othello.hae_voittaja()
            if voittaja == "valkoinen":
                return 10000 + syvyys
            if voittaja == "musta":
                return -10000 - syvyys
            return 0
        if syvyys == 0:
            return self.arvioi_pelilauta(othello)
        if maksimoi_pelaaja and not othello.mahdolliset_siirrot("valkoinen"):
            return self.arvioi_pelilauta(othello)
        if not maksimoi_pelaaja and not othello.mahdolliset_siirrot("musta"):
            self.minimax(syvyys - 1, othello, alfa, beta, True)

        if maksimoi_pelaaja:
            paras_arvo = alfa
            for siirto in othello.mahdolliset_siirrot("valkoinen"):
                kopio_othello = self.tee_siirto_ja_kopioi_lauta(othello, siirto, "valkoinen")
                paras_arvo = max(paras_arvo, self.minimax(syvyys - 1, kopio_othello, alfa, beta, False))
                alfa = max(alfa, paras_arvo)
                if paras_arvo >= beta:
                    break
            return paras_arvo
        else:
            paras_arvo = beta
            for siirto in othello.mahdolliset_siirrot("musta"):
                kopio_othello = self.tee_siirto_ja_kopioi_lauta(othello, siirto, "musta")
                paras_arvo = min(paras_arvo, self.minimax(syvyys - 1, kopio_othello, alfa, beta, True))
                beta = min(beta, paras_arvo)
                if paras_arvo <= alfa:
                    break
            return paras_arvo

    def arvioi_pelilauta(self, othello):
        pelilauta = othello.hae_pelilauta()
        arvio = 0
        for i in range(9):
            for j in range(9):
                if pelilauta[i][j] == "o":
                    arvio += PAINOT[i][j]
                elif pelilauta[i][j] == "x":
                    arvio -= PAINOT[i][j]
        return arvio

    def tee_siirto_ja_kopioi_lauta(self, othello, siirto, vari):
        othello.tee_siirto(siirto, vari)
        lauta = othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        return kopio_othello
