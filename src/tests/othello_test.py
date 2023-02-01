import unittest
from othello import Othello


class PelilautaStub:
    def hae_pelilauta1(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "x", "_", "x", "_", "x", "_", "_", "_"],
                [2, "_", "o", "o", "o", "_", "_", "_", "_"],
                [3, "x", "o", "_", "o", "x", "_", "_", "_"],
                [4, "_", "o", "o", "o", "_", "_", "_", "_"],
                [5, "x", "_", "o", "_", "x", "_", "_", "_"],
                [6, "_", "_", "o", "_", "_", "_", "_", "_"],
                [7, "_", "_", "o", "_", "_", "_", "_", "_"],
                [8, "_", "_", "x", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta2(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "o", "_", "o", "_", "o", "_", "_", "_"],
                [2, "_", "x", "x", "x", "_", "_", "_", "_"],
                [3, "o", "x", "_", "x", "o", "_", "_", "_"],
                [4, "_", "x", "x", "x", "_", "_", "_", "_"],
                [5, "o", "_", "x", "_", "o", "_", "_", "_"],
                [6, "_", "_", "x", "_", "_", "_", "_", "_"],
                [7, "_", "_", "x", "_", "_", "_", "_", "_"],
                [8, "_", "_", "o", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta3(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "_", "o", "o", "x", "o", "o", "o", "_"],
                [2, "_", "_", "_", "o", "_", "_", "_", "_"],
                [3, "o", "_", "o", "_", "_", "_", "o", "_"],
                [4, "o", "_", "_", "o", "_", "o", "_", "_"],
                [5, "x", "_", "_", "_", "x", "_", "_", "_"],
                [6, "_", "_", "_", "o", "_", "o", "_", "_"],
                [7, "_", "_", "o", "_", "_", "_", "o", "_"],
                [8, "_", "_", "_", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta4(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "_", "x", "x", "o", "x", "x", "x", "_"],
                [2, "_", "_", "_", "x", "_", "_", "_", "_"],
                [3, "x", "_", "x", "_", "_", "_", "x", "_"],
                [4, "x", "_", "_", "x", "_", "x", "_", "_"],
                [5, "o", "_", "_", "_", "o", "_", "_", "_"],
                [6, "_", "_", "_", "x", "_", "x", "_", "_"],
                [7, "_", "_", "x", "_", "_", "_", "x", "_"],
                [8, "_", "_", "_", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta5(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "o", "_", "_", "o", "_", "_", "o", "_"],
                [2, "_", "o", "_", "o", "_", "o", "_", "_"],
                [3, "_", "_", "o", "o", "o", "_", "_", "_"],
                [4, "o", "o", "o", "x", "o", "o", "o", "o"],
                [5, "_", "_", "o", "o", "o", "_", "_", "_"],
                [6, "_", "o", "_", "o", "_", "o", "_", "_"],
                [7, "o", "_", "_", "o", "_", "_", "o", "_"],
                [8, "_", "_", "_", "o", "_", "_", "_", "o"]]
        return pelilauta

    def hae_pelilauta2(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "o", "_", "o", "_", "o", "_", "_", "_"],
                [2, "_", "x", "x", "x", "_", "_", "_", "_"],
                [3, "o", "x", "_", "x", "o", "_", "_", "_"],
                [4, "_", "x", "x", "x", "_", "_", "_", "_"],
                [5, "o", "_", "x", "_", "o", "_", "_", "_"],
                [6, "_", "_", "x", "_", "_", "_", "_", "_"],
                [7, "_", "_", "x", "_", "_", "_", "_", "_"],
                [8, "_", "_", "o", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta3(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "_", "o", "o", "x", "o", "o", "o", "_"],
                [2, "_", "_", "_", "o", "_", "_", "_", "_"],
                [3, "o", "_", "o", "_", "_", "_", "o", "_"],
                [4, "o", "_", "_", "o", "_", "o", "_", "_"],
                [5, "x", "_", "_", "_", "x", "_", "_", "_"],
                [6, "_", "_", "_", "o", "_", "o", "_", "_"],
                [7, "_", "_", "o", "_", "_", "_", "o", "_"],
                [8, "_", "_", "_", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta4(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "_", "x", "x", "o", "x", "x", "x", "_"],
                [2, "_", "_", "_", "x", "_", "_", "_", "_"],
                [3, "x", "_", "x", "_", "_", "_", "x", "_"],
                [4, "x", "_", "_", "x", "_", "x", "_", "_"],
                [5, "o", "_", "_", "_", "o", "_", "_", "_"],
                [6, "_", "_", "_", "x", "_", "x", "_", "_"],
                [7, "_", "_", "x", "_", "_", "_", "x", "_"],
                [8, "_", "_", "_", "_", "_", "_", "_", "_"]]
        return pelilauta

    def hae_pelilauta5(self):
        pelilauta = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "o", "_", "_", "o", "_", "_", "o", "_"],
                [2, "_", "o", "_", "o", "_", "o", "_", "_"],
                [3, "_", "_", "o", "o", "o", "_", "_", "_"],
                [4, "o", "o", "o", "x", "o", "o", "o", "o"],
                [5, "_", "_", "o", "o", "o", "_", "_", "_"],
                [6, "_", "o", "_", "o", "_", "o", "_", "_"],
                [7, "o", "_", "_", "o", "_", "_", "o", "_"],
                [8, "_", "_", "_", "o", "_", "_", "_", "o"]]
        return pelilauta
    

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        pelilauta1 = PelilautaStub().hae_pelilauta1()
        self.othello1 = Othello(pelilauta1)

        pelilauta2 = PelilautaStub().hae_pelilauta2()
        self.othello2 = Othello(pelilauta2)

        pelilauta3 = PelilautaStub().hae_pelilauta3()
        self.othello3 = Othello(pelilauta3)

        pelilauta4 = PelilautaStub().hae_pelilauta4()
        self.othello4 = Othello(pelilauta4)

        pelilauta5 = PelilautaStub().hae_pelilauta5()
        self.othello5 = Othello(pelilauta5)
    
    def test_laske_tilanne_toimii(self):
        self.othello1.laske_tilanne()
        mustat, valkoiset = self.othello1.hae_mustat_ja_valkoiset()
        self.assertEqual((mustat, valkoiset), (8, 11))

    def test_vaihda_vuoroa_vaihtaa_pelaajaa(self):
        self.othello1.vaihda_vuoroa()
        self.assertEqual(self.othello1.hae_pelaaja(), "valkoinen")

    def test_sallitut_palauttaa_oikean_listan_mustia(self):
        sallitut = self.othello3.mahdolliset_siirrot()
        self.assertEqual(sallitut, ["a1", "a2", "b2", "b8", "d3", "h1", "h2", "h8"])

    def test_sallitut_palauttaa_oikean_listan_valkoisia(self):
        self.othello4.vaihda_vuoroa()
        sallitut = self.othello4.mahdolliset_siirrot()
        self.assertEqual(sallitut, ["a1", "a2", "b2", "b8", "d3", "h1", "h2", "h8"])

    def test_tee_siirto_kaantaa_joka_suunnan_mustia(self):
        self.othello1.tee_siirto("c3")
        lopputulos = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "x", "_", "x", "_", "x", "_", "_", "_"],
                [2, "_", "x", "x", "x", "_", "_", "_", "_"],
                [3, "x", "x", "x", "x", "x", "_", "_", "_"],
                [4, "_", "x", "x", "x", "_", "_", "_", "_"],
                [5, "x", "_", "x", "_", "x", "_", "_", "_"],
                [6, "_", "_", "x", "_", "_", "_", "_", "_"],
                [7, "_", "_", "x", "_", "_", "_", "_", "_"],
                [8, "_", "_", "x", "_", "_", "_", "_", "_"]]
        self.assertEqual(self.othello1.hae_pelilauta(), lopputulos)

    def test_tee_siirto_kaantaa_joka_suunnan_valkoisia(self):
        self.othello2.vaihda_vuoroa()
        self.othello2.tee_siirto("c3")
        lopputulos = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "o", "_", "o", "_", "o", "_", "_", "_"],
                [2, "_", "o", "o", "o", "_", "_", "_", "_"],
                [3, "o", "o", "o", "o", "o", "_", "_", "_"],
                [4, "_", "o", "o", "o", "_", "_", "_", "_"],
                [5, "o", "_", "o", "_", "o", "_", "_", "_"],
                [6, "_", "_", "o", "_", "_", "_", "_", "_"],
                [7, "_", "_", "o", "_", "_", "_", "_", "_"],
                [8, "_", "_", "o", "_", "_", "_", "_", "_"]]
        self.assertEqual(self.othello2.hae_pelilauta(), lopputulos)

    def test_sallitut_ei_anna_laittomia_siirtoja(self):
        sallitut = self.othello5.mahdolliset_siirrot()
        self.assertEqual(sallitut, [])

    def test_laiton_siirto_ei_muuta_pelilautaa(self):
        self.othello1.tee_siirto("f1")
        lopputulos = [[" ", "a", "b", "c", "d", "e", "f", "g", "h"],
                [1, "x", "_", "x", "_", "x", "_", "_", "_"],
                [2, "_", "o", "o", "o", "_", "_", "_", "_"],
                [3, "x", "o", "_", "o", "x", "_", "_", "_"],
                [4, "_", "o", "o", "o", "_", "_", "_", "_"],
                [5, "x", "_", "o", "_", "x", "_", "_", "_"],
                [6, "_", "_", "o", "_", "_", "_", "_", "_"],
                [7, "_", "_", "o", "_", "_", "_", "_", "_"],
                [8, "_", "_", "x", "_", "_", "_", "_", "_"]]
        self.assertEqual(self.othello1.hae_pelilauta(), lopputulos)

    def test_ei_siirtoja_on_game_over(self):
        loppu = self.othello5.game_over()
        self.assertEqual(loppu, True)
