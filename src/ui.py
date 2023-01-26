from othello import Othello


class UI:
    def __init__(self, pelilauta):
        self.othello = Othello(pelilauta)

    def kaynnista(self):
        while True:
            print(f"Lopeta: q. Syöte esim.: d3")
            self.othello.laske_tilanne()
            mustat, valkoiset = self.othello.hae_mustat_ja_valkoiset()
            print(f"x: {mustat}, o: {valkoiset}")
            self.othello.tulosta_pelilauta()

            sallitut = self.othello.sallitut()
            if not sallitut:
                if self.othello.game_over():
                    break
                else:
                    self.othello.vaihda_vuoroa()
            else:
                sallitut.sort()
                print("sallitut siirrot: ", sallitut)
                syote = self.hae_siirto()
                if syote == "q":
                    break
                else:
                   laillinen = self.othello.tee_siirto(syote)
                   if not laillinen:
                       print("Siirto ei ole sallittu.")
                   else:
                       print("Siirto: ", syote)
                       self.othello.vaihda_vuoroa()

    def hae_siirto(self):
        syote = input(f"{self.othello.hae_pelaaja()}, anna syöte: ")
        return syote
