from othello import Othello
from othello_ai import OthelloAI


class UI:
    def __init__(self, pelilauta):
        self.othello = Othello(pelilauta)
        self.othello_ai = OthelloAI()

    def kaynnista(self):
        while True:
            print("Lopeta: q. Syöte esim.: d3")
            self.othello.laske_tilanne()
            mustat, valkoiset = self.othello.hae_mustat_ja_valkoiset()
            print(f"x: {mustat}, o: {valkoiset}")
            self.othello.tulosta_pelilauta()

            sallitut = self.othello.sallitut()
            if not sallitut:
                if self.othello.game_over():
                    break
                self.othello.vaihda_vuoroa()
            else:
                sallitut.sort()
                print("sallitut siirrot: ", sallitut)
                syote = self.hae_siirto()
                if syote == "q":
                    break
                laillinen = self.othello.tee_siirto(syote)
                if not laillinen:
                    print("Siirto ei ole sallittu.")
                else:
                    print("Siirto: ", syote)
                    self.othello.vaihda_vuoroa()

    def hae_siirto(self):
        if self.othello.hae_pelaaja() == "valkoinen":
            lauta = self.othello.hae_pelilauta()
            kopiolauta = [[lauta[x][y] for y in range(len(lauta[0]))] for x in range(len(lauta))]
            kopio_othello = Othello(kopiolauta)
            kopio_othello.vaihda_vuoroa()
            syote = self.othello_ai.hae_seuraava_siirto(3, kopio_othello, True)
        else:
            syote = input(f"{self.othello.hae_pelaaja()}, anna syöte: ")

        return syote
