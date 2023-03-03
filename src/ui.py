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
            self.tulosta_pelilauta()

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
                self.tulosta_siirrot(sallitut)
                if not tekoalyn_vuoro:
                    syote = input("Musta, anna syöte: ")
                    if syote == "q":
                        break
                    if len(syote) != 2 or syote[0] not in "abcdefgh" or int(syote[1]) not in range(1, 9):
                        print("Siirto ei ole sallittu")
                        print()
                        continue
                    koordinaatit = self.merkkijono_koordinaateiksi(syote)
                else:
                    koordinaatit = self.hae_tekoalyn_siirto()
                    syote = self.koordinaatit_merkkijonoksi(koordinaatit)
                laillinen = self.othello.tee_siirto(koordinaatit, tekoalyn_vuoro, sallitut)
                if not laillinen:
                    print("Siirto ei ole sallittu.")
                else:
                    print("Siirto: ", syote)
                    tekoalyn_vuoro = self.vaihda_vuoroa(tekoalyn_vuoro)
                print()

    def hae_tekoalyn_siirto(self):
        lauta = self.othello.hae_pelilauta()
        kopiolauta = deepcopy(lauta)
        kopio_othello = Othello(kopiolauta)
        siirto = self.othello_ai.valitse_siirto(20, kopio_othello)
        return siirto

    def vaihda_vuoroa(self, tekoalyn_vuoro):
        if tekoalyn_vuoro:
            tekoalyn_vuoro = False
        else:
            tekoalyn_vuoro = True
        return tekoalyn_vuoro

    def tulosta_siirrot(self, siirrot):
        aakkosjarjestyksessa = []
        for siirto in siirrot:
            aakkosjarjestyksessa.append(self.koordinaatit_merkkijonoksi(siirto))
        aakkosjarjestyksessa.sort()
        for i in range(len(aakkosjarjestyksessa) - 1):
            print(aakkosjarjestyksessa[i], end=", ")
        print(aakkosjarjestyksessa[-1])

    def merkkijono_koordinaateiksi(self, syote):
        sarakkeet = "abcdefgh"
        rivi = int(syote[1]) - 1
        sarake = sarakkeet.find(syote[0])
        return (rivi, sarake)

    def koordinaatit_merkkijonoksi(self, koordinaatit):
        sarakkeet = "abcdefgh"
        return f"{sarakkeet[koordinaatit[1]]}{koordinaatit[0] + 1}"

    def tulosta_pelilauta(self):
        """Tulostaa pelilaudan ASCII-grafiikalla."""
        pelilauta = self.othello.hae_pelilauta()
        print("  a b c d e f g h")
        for i in range(8):
            print(f"{i + 1}", end=" ")
            for j in range(8):
                if pelilauta[i][j] == 0:
                    print("_", end=" ")
                elif pelilauta[i][j] == 1:
                    print("x", end=" ")
                else:
                    print("o", end=" ")
            print()
