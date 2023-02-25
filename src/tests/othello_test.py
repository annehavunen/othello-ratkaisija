import unittest
from othello import Othello
from pelilauta_stub import PelilautaStub


class TestOthello(unittest.TestCase):
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

        pelilauta6 = PelilautaStub().hae_pelilauta6()
        self.othello6 = Othello(pelilauta6)

    def test_laske_tilanne_toimii(self):
        mustat, valkoiset = self.othello1.hae_mustat_ja_valkoiset()
        self.assertEqual((mustat, valkoiset), (8, 11))

    def test_sallitut_palauttaa_oikean_listan_mustia(self):
        sallitut = self.othello3.mahdolliset_siirrot(False)
        self.assertEqual(sallitut, [(0, 0), (0, 7), (1, 0), (1, 1), (1, 7), (2, 3), (7, 1), (7, 7)])

    def test_sallitut_palauttaa_oikean_listan_valkoisia(self):
        sallitut = self.othello4.mahdolliset_siirrot(True)
        self.assertEqual(sallitut, [(0, 0), (0, 7), (1, 0), (1, 1), (1, 7), (2, 3), (7, 1), (7, 7)])

    def test_tee_siirto_kaantaa_joka_suunnan_mustia(self):
        self.othello1.tee_siirto((2, 2), False)
        lopputulos = [
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]]
        self.assertEqual(self.othello1.hae_pelilauta(), lopputulos)

    def test_tee_siirto_kaantaa_joka_suunnan_valkoisia(self):
        self.othello2.tee_siirto((2, 2), True)
        lopputulos = [
                [2, 0, 2, 0, 2, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [2, 0, 2, 0, 2, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0]]
        self.assertEqual(self.othello2.hae_pelilauta(), lopputulos)

    def test_kaanna_suunta_ei_kaanna_ilman_vastaparia(self):
        koordinaatit, suunta, vastustaja, oma = (0, 3), (-1, 0), 1, 2
        self.othello1.kaanna_suunta(koordinaatit, suunta, vastustaja, oma)
        lopputulos = [
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 2, 0, 2, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 0, 2, 0, 1, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]]
        self.assertEqual(self.othello1.hae_pelilauta(), lopputulos)

    def test_sallitut_ei_anna_laittomia_siirtoja(self):
        sallitut = self.othello5.mahdolliset_siirrot(False)
        self.assertEqual(sallitut, [])

    def test_laiton_siirto_ei_muuta_pelilautaa(self):
        self.othello1.tee_siirto((4, 0), False)
        lopputulos = [
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 2, 0, 2, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 0, 2, 0, 1, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]]
        self.assertEqual(self.othello1.hae_pelilauta(), lopputulos)

    def test_ei_siirtoja_on_game_over(self):
        loppu = self.othello5.game_over()
        self.assertEqual(loppu, True)

    def test_ei_game_over_jos_toisella_on_siirtoja(self):
        loppu = self.othello2.game_over()
        self.assertEqual(loppu, False)

    def test_hae_voittaja_palauttaa_oikein(self):
        voittaja1 = self.othello1.hae_voittaja()
        voittaja2 = self.othello2.hae_voittaja()
        voittaja3 = self.othello6.hae_voittaja()
        self.assertEqual([voittaja1, voittaja2, voittaja3], ["valkoinen", "musta", "tasapeli"])
