class Othello:
    def __init__(self, pelilauta):
        self.pelilauta = pelilauta
        self.pelaaja = "P1" # musta eli x aloittaa
        self.mustat, self.valkoiset = 0, 0
        self.vuorot = 1
        self.ei_siirtoja = 0

    def sallitut(self):
        sallitut = []
        for i in range(9):
            for j in range(9):
                if self.pelaaja == "P1":
                    oma_maa = "x"
                    vastustajan_maa = "o"
                else:
                    oma_maa = "o"
                    vastustajan_maa = "x"
                if self.pelilauta[i][j] == oma_maa:
                    sallittu_vasemmalla = self.tutki_vasen(i, j, vastustajan_maa, "_")
                    if sallittu_vasemmalla and sallittu_vasemmalla not in sallitut:
                        sallitut.append(sallittu_vasemmalla)

                    sallittu_oikealla = self.tutki_oikea(i, j, vastustajan_maa, "_")
                    if sallittu_oikealla and sallittu_oikealla not in sallitut:
                        sallitut.append(sallittu_oikealla)
                    
                    sallittu_ylhaalla = self.tutki_ylhaalta(i, j, vastustajan_maa, "_")
                    if sallittu_ylhaalla and sallittu_ylhaalla not in sallitut:
                        sallitut.append(sallittu_ylhaalla)

                    sallittu_alhaalla = self.tutki_alhaalta(i, j, vastustajan_maa, "_")
                    if sallittu_alhaalla and sallittu_alhaalla not in sallitut:
                        sallitut.append(sallittu_alhaalla)

                    sallittu_vas_ylaviistossa = self.tutki_vasen_ylaviisto(i, j, vastustajan_maa, "_")
                    if sallittu_vas_ylaviistossa and sallittu_vas_ylaviistossa not in sallitut:
                        sallitut.append(sallittu_vas_ylaviistossa)

                    sallittu_oik_ylaviistossa = self.tutki_oikea_ylaviisto(i, j, vastustajan_maa, "_")
                    if sallittu_oik_ylaviistossa and sallittu_oik_ylaviistossa not in sallitut:
                        sallitut.append(sallittu_oik_ylaviistossa)

                    sallittu_vas_alaviistossa = self.tutki_vasen_alaviisto(i, j, vastustajan_maa, "_")
                    if sallittu_vas_alaviistossa and sallittu_vas_alaviistossa not in sallitut:
                        sallitut.append(sallittu_vas_alaviistossa)

                    sallittu_oik_alaviistossa = self.tutki_oikea_alaviisto(i, j, vastustajan_maa, "_")
                    if sallittu_oik_alaviistossa and sallittu_oik_alaviistossa not in sallitut:
                        sallitut.append(sallittu_oik_alaviistossa)
        return sallitut

    def vaihda_vuoroa(self):
        if self.pelaaja == "P1":
            self.pelaaja = "P2"
        else:
            self.pelaaja = "P1"
        self.vuorot += 1

    def tee_siirto(self, syote):
        sarakkeet = "0abcdefgh"
        sarake = int(sarakkeet.index(syote[0]))
        rivi = int(syote[1])
        if self.pelaaja == "P1":
            oma_maa = "x"
            vastustajan_maa = "o"
        else:
            oma_maa = "o"
            vastustajan_maa = "x"
        self.pelilauta[rivi][sarake] = oma_maa
        self.kaanna_vasemmat(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_oikeat(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_ylhaalta(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_alhaalta(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_vasen_ylaviisto(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_oikea_ylaviisto(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_vasen_alaviisto(rivi, sarake, oma_maa, vastustajan_maa)
        self.kaanna_oikea_alaviisto(rivi, sarake, oma_maa, vastustajan_maa)
        self.laske_tilanne()

    def laske_tilanne(self):
        mustat = 0
        valkoiset = 0
        for i in range(8):
            for j in range(8):
                if self.pelilauta[i][j] == "x":
                    mustat += 1
                elif self.pelilauta[i][j] == "o":
                    valkoiset += 1
        self.mustat = mustat
        self.valkoiset = valkoiset

    def tutki_vasen(self, i, j, vastustajan_maa, maaranpaa):
        sarake = j - 1
        if j >= 3 and self.pelilauta[i][sarake] == vastustajan_maa:
            sarake -= 1
            while sarake >= 1:
                if self.pelilauta[i][sarake] == vastustajan_maa:
                    sarake -= 1
                elif self.pelilauta[i][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{i}"
                else:
                    return None

    def tutki_oikea(self, i, j, vastustajan_maa, maaranpaa):
        sarake = j + 1
        if j <= 6 and self.pelilauta[i][sarake] == vastustajan_maa:
            sarake += 1
            while sarake <= 8:
                if self.pelilauta[i][sarake] == vastustajan_maa:
                    sarake += 1
                elif self.pelilauta[i][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{i}"
                else:
                    return None

    def tutki_ylhaalta(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i - 1
        if i >= 3 and self.pelilauta[rivi][j] == vastustajan_maa:
            rivi -= 1
            while rivi >= 1:
                if self.pelilauta[rivi][j] == vastustajan_maa:
                    rivi -= 1
                elif self.pelilauta[rivi][j] == maaranpaa:
                    return f"{self.pelilauta[0][j]}{rivi}"
                else:
                    return None

    def tutki_alhaalta(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i + 1
        if i <= 6 and self.pelilauta[rivi][j] == vastustajan_maa:
            rivi += 1
            while rivi <= 8:
                if self.pelilauta[rivi][j] == vastustajan_maa:
                    rivi += 1
                elif self.pelilauta[rivi][j] == maaranpaa:
                    return f"{self.pelilauta[0][j]}{rivi}"
                else:
                    return None

    def tutki_vasen_ylaviisto(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i - 1
        sarake = j-1
        if i >= 3 and j >= 3 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi -= 1
            sarake -= 1
            while rivi >= 1 and sarake >= 1:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi -= 1
                    sarake -= 1
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{rivi}"
                else:
                    return None

    def tutki_oikea_ylaviisto(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i - 1
        sarake = j + 1
        if i >= 3 and j <= 6 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi -= 1
            sarake += 1
            while rivi >= 1 and sarake <= 8:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi -= 1
                    sarake += 1
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{rivi}"
                else:
                    return None

    def tutki_vasen_alaviisto(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i + 1
        sarake = j - 1
        if i <= 6 and j >= 3 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi += 1
            sarake -= 1
            while rivi <= 8 and sarake >= 1:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi += 1
                    sarake -= 1
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{rivi}"
                else:
                    return None

    def tutki_oikea_alaviisto(self, i, j, vastustajan_maa, maaranpaa):
        rivi = i + 1
        sarake = j + 1
        if i <= 6 and j <= 6 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi += 1
            sarake += 1
            while rivi <= 8 and sarake <= 8:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi += 1
                    sarake += 1
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return f"{self.pelilauta[0][sarake]}{rivi}"
                else:
                    return None

    def kaanna_vasemmat(self, rivi, sarake, oma_maa, vastustajan_maa):
        vasen = self.tutki_vasen(rivi, sarake, vastustajan_maa, oma_maa)
        if vasen:
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(vasen[0]))
            sarake -= 1
            while sarake > kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                sarake -= 1

    def kaanna_oikeat(self, rivi, sarake, oma_maa, vastustajan_maa):
        oikea = self.tutki_oikea(rivi, sarake, vastustajan_maa, oma_maa)
        if oikea:
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(oikea[0]))
            sarake += 1
            while sarake < kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                sarake += 1

    def kaanna_ylhaalta(self, rivi, sarake, oma_maa, vastustajan_maa):
        ylapuoli = self.tutki_ylhaalta(rivi, sarake, vastustajan_maa, oma_maa)
        if ylapuoli:
            kohderivi = int(ylapuoli[1])
            rivi -= 1
            while rivi > kohderivi:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi -= 1

    def kaanna_alhaalta(self, rivi, sarake, oma_maa, vastustajan_maa):
        alapuoli = self.tutki_alhaalta(rivi, sarake, vastustajan_maa, oma_maa)
        if alapuoli:
            kohderivi = int(alapuoli[1])
            rivi += 1
            while rivi < kohderivi:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi += 1

    def kaanna_vasen_ylaviisto(self, rivi, sarake, oma_maa, vastustajan_maa):
        vas_ylaviisto = self.tutki_vasen_ylaviisto(rivi, sarake, vastustajan_maa, oma_maa)
        if vas_ylaviisto:
            kohderivi = int(vas_ylaviisto[1])
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(vas_ylaviisto[0]))
            rivi -= 1
            sarake -= 1
            while rivi > kohderivi and sarake > kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi -= 1
                sarake -= 1

    def kaanna_oikea_ylaviisto(self, rivi, sarake, oma_maa, vastustajan_maa):
        oik_ylaviisto = self.tutki_oikea_ylaviisto(rivi, sarake, vastustajan_maa, oma_maa)
        if oik_ylaviisto:
            kohderivi = int(oik_ylaviisto[1])
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(oik_ylaviisto[0]))
            rivi -= 1
            sarake += 1
            while rivi > kohderivi and sarake < kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi -= 1
                sarake += 1

    def kaanna_vasen_alaviisto(self, rivi, sarake, oma_maa, vastustajan_maa):
        vas_alaviisto = self.tutki_vasen_alaviisto(rivi, sarake, vastustajan_maa, oma_maa)
        if vas_alaviisto:
            kohderivi = int(vas_alaviisto[1])
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(vas_alaviisto[0]))
            rivi += 1
            sarake -= 1
            while rivi < kohderivi and sarake > kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi += 1
                sarake -= 1

    def kaanna_oikea_alaviisto(self, rivi, sarake, oma_maa, vastustajan_maa):
        oik_alaviisto = self.tutki_oikea_alaviisto(rivi, sarake, vastustajan_maa, oma_maa)
        if oik_alaviisto:
            kohderivi = int(oik_alaviisto[1])
            sarakkeet = "0abcdefgh"
            kohdesarake = int(sarakkeet.index(oik_alaviisto[0]))
            rivi += 1
            sarake += 1
            while rivi < kohderivi and sarake < kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi += 1
                sarake += 1

    def tulosta_pelilauta(self):
        for rivi in self.pelilauta:
            for ruutu in rivi:
                print(ruutu, end=" ")
            print()

    def hae_vuorot(self):
        return self.vuorot

    def hae_mustat_ja_valkoiset(self):
        return self.mustat, self.valkoiset

    def hae_pelaaja(self):
        return self.pelaaja

    def hae_ei_siirtoja(self):
        return self.ei_siirtoja

    def aseta_ei_siirtoja(self, vuorot):
        self.ei_siirtoja = vuorot
