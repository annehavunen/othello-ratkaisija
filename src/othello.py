SUUNNAT = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class Othello:
    def __init__(self, pelilauta):
        self.pelilauta = pelilauta
        self.pelaaja = "musta"
        self.mustat, self.valkoiset = 0, 0

    def sallitut(self):
        sallitut = []
        for i in range(9):
            for j in range(9):
                if self.pelaaja == "musta":
                    oma_maa = "x"
                    vastustajan_maa = "o"
                else:
                    oma_maa = "o"
                    vastustajan_maa = "x"
                if self.pelilauta[i][j] == oma_maa:
                    for suunta in SUUNNAT:
                        sallittu_suunta = self.tutki_suunta((i, j), suunta, vastustajan_maa, "_")
                        if sallittu_suunta and sallittu_suunta not in sallitut:
                            sallitut.append(sallittu_suunta)

        sallitut.sort()
        return sallitut

    def tutki_suunta(self, lahtopaikka, liike, vastustajan_maa, maaranpaa):
        rivi = lahtopaikka[0] + liike[0]
        sarake = lahtopaikka[1] + liike[1]
        if 1 <= rivi <= 8 and 1 <= sarake <= 8 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi += liike[0]
            sarake += liike[1]            
            while 1 <= rivi <= 8 and 1 <= sarake <= 8:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi += liike[0]
                    sarake += liike[1]
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{rivi}"
                else:
                    return None

    def tee_siirto(self, syote):
        sallitut = self.sallitut()
        if syote in sallitut:
            sarakkeet = "0abcdefgh"
            sarake = int(sarakkeet.index(syote[0]))
            rivi = int(syote[1])
            if self.pelaaja == "musta":
                oma_maa = "x"
                vastustajan_maa = "o"
            else:
                oma_maa = "o"
                vastustajan_maa = "x"
            self.pelilauta[rivi][sarake] = oma_maa
            for suunta in SUUNNAT:
                self.kaanna_suunta((rivi, sarake), suunta, vastustajan_maa, oma_maa)
            self.laske_tilanne()
            return True
        return False

    def kaanna_suunta(self, lahtopaikka, liike, vastustajan_maa, oma_maa):
        vastapari = self.tutki_suunta(lahtopaikka, liike, vastustajan_maa, oma_maa)
        if vastapari:
            sarakkeet = "0abcdefgh"
            rivi = lahtopaikka[0] + liike[0]
            sarake = lahtopaikka[1] + liike[1]
            kohderivi = int(vastapari[1])
            kohdesarake = int(sarakkeet.index(vastapari[0]))
            while rivi != kohderivi or sarake != kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi += liike[0]
                sarake += liike[1]

    def laske_tilanne(self):
        mustat = 0
        valkoiset = 0
        for i in range(9):
            for j in range(9):
                if self.pelilauta[i][j] == "x":
                    mustat += 1
                elif self.pelilauta[i][j] == "o":
                    valkoiset += 1
        self.mustat = mustat
        self.valkoiset = valkoiset

    def tulosta_pelilauta(self):
        for rivi in self.pelilauta:
            for ruutu in rivi:
                print(ruutu, end=" ")
            print()

    def game_over(self):
        if not self.sallitut():
            self.vaihda_vuoroa()
            if not self.sallitut():
                return True
            self.vaihda_vuoroa()
        return False

    def vaihda_vuoroa(self):
        if self.pelaaja == "musta":
            self.pelaaja = "valkoinen"
        else:
            self.pelaaja = "musta"

    def hae_pelaaja(self):
        return self.pelaaja

    def hae_mustat_ja_valkoiset(self):
        self.laske_tilanne()
        return self.mustat, self.valkoiset
