from othello import Othello


class UI:
    def __init__(self, pelilauta):
        self.othello = Othello(pelilauta)

    def kaynnista(self):
        while True:
            print(f"Lopeta: q. Syöte esim.: d3. Vuoron numero: {self.othello.hae_vuorot()}")
            self.othello.laske_tilanne()
            mustat, valkoiset = self.othello.hae_mustat_ja_valkoiset()
            print(f"x: {mustat}, o: {valkoiset}")
            self.othello.tulosta_pelilauta()

            sallitut = self.othello.sallitut()
            if not sallitut:
                if self.othello.hae_ei_siirtoja() == self.othello.hae_vuorot() - 1: # kummallakaan pelaajalla ei ole mahdollisia siirtoja
                    break
                else:
                    self.othello.aseta_ei_siirtoja(self.othello.hae_vuorot())
                    self.othello.vaihda_vuoroa()
            else:
                sallitut.sort()
                print("sallitut siirrot: ", sallitut)
                syote = input(f"{self.othello.hae_pelaaja()}, anna syöte: ")
                if syote == "q":
                    break
                elif syote not in sallitut:
                    print("Siirto ei ole sallittu.")
                else:
                    print("Siirto: ", syote)
                    self.othello.tee_siirto(syote)
                    self.othello.vaihda_vuoroa()

