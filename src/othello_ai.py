from othello import Othello


class OthelloAI:
    def hae_seuraava_siirto(self, syvyys, othello, maksimoi_pelaaja):
        arvo, siirto = self.minimax(syvyys, othello, maksimoi_pelaaja)
        return siirto

    def minimax(self, syvyys, othello, maksimoi_pelaaja):
        if syvyys == 0 or not othello.sallitut():
            return self.arvioi_pelilauta(othello), None

        if maksimoi_pelaaja:
            paras_siirto = None
            max_arvo = float("-inf")
            sallitut = othello.sallitut()
            for siirto in sallitut:
                othello.tee_siirto(siirto)
                lauta = othello.hae_pelilauta()
                kopiolauta = [[lauta[x][y] for y in range(len(lauta[0]))] for x in range(len(lauta))]
                kopio_othello = Othello(kopiolauta)
                arvo, _ = self.minimax(syvyys - 1, kopio_othello, False)
                if arvo > max_arvo:
                    max_arvo = arvo
                    paras_siirto = siirto
            return max_arvo, paras_siirto
        else:
            paras_siirto = None
            min_arvo = float("inf")
            sallitut = othello.sallitut()
            for siirto in sallitut:
                othello.tee_siirto(siirto)
                lauta = othello.hae_pelilauta()
                kopiolauta = [[lauta[x][y] for y in range(len(lauta[0]))] for x in range(len(lauta))]
                kopio_othello = Othello(kopiolauta)
                kopio_othello.vaihda_vuoroa()
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
        sallitut_valk = othello.hae_sallittujen_maara("o")
        sallitut_musta = othello.hae_sallittujen_maara("x")
        arvio = (valkoiset - mustat) + \
                (10 * kulmapaikat_valk - 10 * kulmapaikat_musta) + \
                (5 * reunapaikat_valk - 5 * reunapaikat_musta) + \
                (sallitut_valk - sallitut_musta)
        return arvio
