from othello import Othello
from copy import deepcopy


class OthelloAI:
    def hae_seuraava_siirto(self, syvyys, othello, maksimoi_pelaaja):
        arvo, siirto = self.minimax(syvyys, othello, maksimoi_pelaaja)
        return siirto

    def minimax(self, syvyys, othello, maksimoi_pelaaja):
        if syvyys == 0 or not othello.mahdolliset_siirrot("musta") or not othello.mahdolliset_siirrot("valkoinen"):
            return self.arvioi_pelilauta(othello), None

        if maksimoi_pelaaja:
            paras_siirto = None
            max_arvo = float("-inf")
            sallitut = othello.mahdolliset_siirrot("valkoinen")
            for siirto in sallitut:
                othello.tee_siirto(siirto, "valkoinen")
                lauta = othello.hae_pelilauta()
                kopiolauta = deepcopy(lauta)
                kopio_othello = Othello(kopiolauta)
                arvo, _ = self.minimax(syvyys - 1, kopio_othello, False)
                if arvo > max_arvo:
                    max_arvo = arvo
                    paras_siirto = siirto
            return max_arvo, paras_siirto
        else:
            paras_siirto = None
            min_arvo = float("inf")
            sallitut = othello.mahdolliset_siirrot("musta")
            for siirto in sallitut:
                othello.tee_siirto(siirto, "musta")
                lauta = othello.hae_pelilauta()
                kopiolauta = deepcopy(lauta)
                kopio_othello = Othello(kopiolauta)
                arvo, _ = self.minimax(syvyys - 1, kopio_othello, True)
                if arvo < min_arvo:
                    min_arvo = arvo
                    paras_siirto = siirto
            return min_arvo, paras_siirto

    def arvioi_pelilauta(self, othello):
        mustat, valkoiset = othello.hae_mustat_ja_valkoiset()
        kulmapaikat_valk = othello.hae_kulmapaikat("o")
        kulmapaikat_musta = othello.hae_kulmapaikat("x")
        reunapaikat_valk = othello.hae_reunapaikat("o")
        reunapaikat_musta = othello.hae_reunapaikat("x")
        sallitut_valk = len(othello.mahdolliset_siirrot("valkoinen"))
        sallitut_musta = len(othello.mahdolliset_siirrot("musta"))
        arvio = (valkoiset - mustat) + \
                (10 * kulmapaikat_valk - 10 * kulmapaikat_musta) + \
                (5 * reunapaikat_valk - 5 * reunapaikat_musta) + \
                (sallitut_valk - sallitut_musta)
        return arvio
