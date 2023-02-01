from othello import Othello
from othello_ai import OthelloAI
from copy import deepcopy


class UI:
    def __init__(self, pelilauta):
        self.othello = Othello(pelilauta)
        self.othello_ai = OthelloAI()

    def kaynnista(self):
        pelaaja = "musta"
        while True:
            print("Lopeta: q. Syöte esim.: d3")
            mustat, valkoiset = self.othello.hae_mustat_ja_valkoiset()
            print(f"x: {mustat}, o: {valkoiset}")
            self.othello.tulosta_pelilauta()

            sallitut = self.othello.mahdolliset_siirrot(pelaaja)
            if not sallitut:
                if self.othello.game_over():
                    break
                pelaaja = self.vaihda_vuoroa()
            else:
                sallitut.sort()
                print("Mahdolliset siirrot: ", sallitut)
                syote = self.hae_siirto(pelaaja)
                if syote == "q":
                    break
                laillinen = self.othello.tee_siirto(syote, pelaaja)
                if not laillinen:
                    print("Siirto ei ole sallittu.")
                else:
                    print("Siirto: ", syote)
                    pelaaja = self.vaihda_vuoroa(pelaaja)

    def hae_siirto(self, pelaaja):
        if pelaaja == "valkoinen":
            lauta = self.othello.hae_pelilauta()
            kopiolauta = deepcopy(lauta)
            kopio_othello = Othello(kopiolauta)
            syote = self.othello_ai.hae_seuraava_siirto(3, kopio_othello, True)
        else:
            syote = input(f"{pelaaja}, anna syöte: ")

        return syote

    def vaihda_vuoroa(self, pelaaja):
        if pelaaja == "musta":
            pelaaja = "valkoinen"
        else:
            pelaaja = "musta"
        return pelaaja
