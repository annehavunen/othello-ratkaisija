SUUNNAT = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


class Othello:
    """Luokka, jonka avulla Othello-peliä pelataan.
    Vastaavuudet pelinappuloissa: musta = 1 = False, valkoinen = 2 = True

    Attributes:
        pelilauta: Pelilauta-matriisi, jolla Othello-peli aloitetaan.
    """

    def __init__(self, pelilauta):
        """Luokan konstruktori, joka luo uuden Othello-pelin.

        Args:
            pelilauta: Pelilauta-matriisi, jolla Othello-peli aloitetaan.
        """
        self.pelilauta = pelilauta

    def mahdolliset_siirrot(self, tekoalyn_vuoro):
        """Käy läpi pelilaudan ja etsii tutki_suunta-funktion avulla mahdolliset siirrot.

        Args:
            pelaaja: Boolean, joka on tekoälyn vuorolla True.

        Returns:
            mahdolliset_siirrot: Lista, jossa on sallitut siirrot.
        """
        mahdolliset_siirrot = []
        for i in range(8):
            for j in range(8):
                if tekoalyn_vuoro:
                    oma_maa = 2
                    vastustajan_maa = 1
                else:
                    oma_maa = 1
                    vastustajan_maa = 2
                if self.pelilauta[i][j] == oma_maa:
                    for suunta in SUUNNAT:
                        sallittu_suunta = self.tutki_suunta((i, j), suunta, vastustajan_maa, 0)
                        if sallittu_suunta and sallittu_suunta not in mahdolliset_siirrot:
                            mahdolliset_siirrot.append(sallittu_suunta)
        # mahdolliset_siirrot.sort()
        return mahdolliset_siirrot

    def tutki_suunta(self, lahtopaikka, liike, vastustajan_maa, maaranpaa):
        """Tutkii, onko liikkeen ilmoittamassa suunnassa maaranpaata.
        Aloittaa etsinnän lahtopaikasta.

        Args:
            lahtopaikka: Tuple, jossa on aloittavat koordinaatit pelilaudalla.
            liike: Tuple, esim. (0, 1), jonka avulla lasketaan liike pelilaudalla.
            vastustajan_maa: Kokonaisluku 1 tai 2, joka ilmaisee vastustajan merkkiä.
            maaranpaa: Kokonaisluku 0 - 2 joka ilmaisee, mitä jollain ruudulla pitäisi mahdollisesti olla.

        Returns:
            Maaranpaan koordinaatit pelilaudalla, jos se löytyy.
            None, jos määränpäätä ei löydy.
        """
        rivi = lahtopaikka[0] + liike[0]
        sarake = lahtopaikka[1] + liike[1]
        if 0 <= rivi <= 7 and 0 <= sarake <= 7 and self.pelilauta[rivi][sarake] == vastustajan_maa:
            rivi += liike[0]
            sarake += liike[1]
            while 0 <= rivi <= 7 and 0 <= sarake <= 7:
                if self.pelilauta[rivi][sarake] == vastustajan_maa:
                    rivi += liike[0]
                    sarake += liike[1]
                elif self.pelilauta[rivi][sarake] == maaranpaa:
                    return (rivi, sarake)
                else:
                    return None

    def tee_siirto(self, koordinaatit, tekoalyn_vuoro, sallitut_siirrot): # sallitut_siirrot
        """Huolehtii siirron toteutuksesta.
        Käyttää apunaan funktioita mahdolliset_siirrot sekä kaanna_suunta.

        Args:
            koordinaatit: Pelaajan valitseman siirron koordinaatit.
            tekoalyn_vuoro: Boolean, joka on True tekoälyn vuorolla.

        Returns:
            True, jos siirto on sallittu.
            False, jos siirto ei ole sallittu.
        """
        # sallitut = self.mahdolliset_siirrot(tekoalyn_vuoro) # pois tarkistus täältä? Ehkä parametrina?
        if koordinaatit in sallitut_siirrot:
            if tekoalyn_vuoro:
                oma_maa = 2
                vastustajan_maa = 1
            else:
                oma_maa = 1
                vastustajan_maa = 2
            self.pelilauta[koordinaatit[0]][koordinaatit[1]] = oma_maa
            for suunta in SUUNNAT:
                self.kaanna_suunta(koordinaatit, suunta, vastustajan_maa, oma_maa)
            return True
        return False

    def kaanna_suunta(self, lahtopaikka, liike, vastustajan_maa, oma_maa):
        """Aloittaa lähtöpaikasta ja kääntää vastustajan maat, kunnes vastaan tulee oma maa.
        Etenee liikkeen ilmaisemaan suuntaan.
        Funktio tutki_suunta tarkistaa, onko suunnassa käännettävää.

        Args:
            lahtopaikka: Tuple, jossa on aloittavat koordinaatit pelilaudalla.
            liike: Tuple, esim. (0, 1), jonka avulla lasketaan liike pelilaudalla.
            vastustajan_maa: Kokonaisluku 0 tai 1, joka ilmaisee vastustajan maata.
            oma_maa: Kokonaisluku 0 tai 1, joka ilmaisee omaa maata.
        """
        vastapari = self.tutki_suunta(lahtopaikka, liike, vastustajan_maa, oma_maa)
        if vastapari:
            rivi = lahtopaikka[0] + liike[0]
            sarake = lahtopaikka[1] + liike[1]
            kohderivi = int(vastapari[0])
            kohdesarake = int(vastapari[1])
            while rivi != kohderivi or sarake != kohdesarake:
                self.pelilauta[rivi][sarake] = oma_maa
                rivi += liike[0]
                sarake += liike[1]

    def game_over(self):
        """Tutkii, onko pelissä mahdollista tehdä enää siirtoja.

        Returns:
            True, jos siirtoja ei ole enää jäljellä.
            False, jos siirtoja on jäljellä.
        """
        if not self.mahdolliset_siirrot(True) and not self.mahdolliset_siirrot(False):
            return True
        return False

    def hae_mustat_ja_valkoiset(self):
        """Laskee, montako mustaa (x / 1) ja valkoista (o / 2) nappulaa pelilaudalla on
        ja palauttaa tiedon niiden määrästä.

        Returns: mustat, valkoiset: Kokonaisluvut, joissa on nollien ja ykkösten määrä pelilaudalla.
        """
        mustat = 0
        valkoiset = 0
        for i in range(8):
            for j in range(8):
                if self.pelilauta[i][j] == 1:
                    mustat += 1
                elif self.pelilauta[i][j] == 2:
                    valkoiset += 1
        return mustat, valkoiset

    def hae_voittaja(self):
        """Tarkistaa, kumpaa maata laudalla on enemmän vai onko tasapeli.

        Returns:
            Merkkijono, joka on "musta", "valkoinen" tai "tasapeli".
        """
        mustat, valkoiset = self.hae_mustat_ja_valkoiset()
        if mustat - valkoiset > 0:
            return "musta"
        if mustat - valkoiset < 0:
            return "valkoinen"
        return "tasapeli"

    def hae_pelilauta(self):
        return self.pelilauta
