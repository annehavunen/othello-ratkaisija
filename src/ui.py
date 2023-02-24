from copy import deepcopy
from othello import Othello
from othello_ai import OthelloAI


class UI:
    def __init__(self, pelilauta):
        self.othello = Othello(pelilauta)
        self.othello_ai = OthelloAI()

    def kaynnista(self):
        tekoalyn_vuoro = False
        while True:
            print("Lopeta: q. Syöte esim.: d3")
            mustat, valkoiset = self.othello.hae_mustat_ja_valkoiset()
            print(f"x: {mustat}, o: {valkoiset}")
            self.othello.tulosta_pelilauta()

            sallitut = self.othello.mahdolliset_siirrot(tekoalyn_vuoro)
            if not sallitut:
                if self.othello.game_over():
                    voittaja = self.othello.hae_voittaja()
                    print("Peli päättyi.")
                    print(f"Voittaja: {voittaja}")
                    break
                tekoalyn_vuoro = self.vaihda_vuoroa(tekoalyn_vuoro)
            else:
                sallitut.sort()
                print("Mahdolliset siirrot: ", end="")
                for i in range(len(sallitut) - 1):
                    print(f"{sallitut[i]}, ", end="")
                print(sallitut[-1])
                syote = self.hae_siirto(tekoalyn_vuoro)
                if syote == "q":
                    break
                laillinen = self.othello.tee_siirto(syote, tekoalyn_vuoro)
                if not laillinen:
                    print("Siirto ei ole sallittu.")
                else:
                    print("Siirto: ", syote)
                    tekoalyn_vuoro = self.vaihda_vuoroa(tekoalyn_vuoro)
            print()

    def hae_siirto(self, tekoalyn_vuoro):
        if tekoalyn_vuoro:
            lauta = self.othello.hae_pelilauta()
            kopiolauta = deepcopy(lauta)
            kopio_othello = Othello(kopiolauta)
            syote = self.othello_ai.valitse_siirto(20, kopio_othello)
        else:
            syote = input("Musta, anna syöte: ")
        return syote

    def vaihda_vuoroa(self, tekoalyn_vuoro):
        if tekoalyn_vuoro:
            tekoalyn_vuoro = False
        else:
            tekoalyn_vuoro = True
        return tekoalyn_vuoro
