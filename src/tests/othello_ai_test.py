import unittest
from othello import Othello
from othello_ai import OthelloAI
from pelilauta_stub import PelilautaStub


class TestOthello(unittest.TestCase):
    def setUp(self):
        self.othello_ai = OthelloAI()

        pelilauta1 = PelilautaStub().hae_pelilauta1()
        self.othello1 = Othello(pelilauta1)

        pelilauta7 = PelilautaStub().hae_pelilauta7()
        self.othello7 = Othello(pelilauta7)

        pelilauta8 = PelilautaStub().hae_pelilauta8()
        self.othello8 = Othello(pelilauta8)

        pelilauta9 = PelilautaStub().hae_pelilauta9()
        self.othello9 = Othello(pelilauta9)

        pelilauta10 = PelilautaStub().hae_pelilauta10()
        self.othello10 = Othello(pelilauta10)

        pelilauta11 = PelilautaStub().hae_pelilauta11()
        self.othello11 = Othello(pelilauta11)

        pelilauta12 = PelilautaStub().hae_pelilauta12()
        self.othello12 = Othello(pelilauta12)

    def test_valitaan_nopein_voitto(self):
        siirto1 = self.othello_ai.valitse_siirto(10, self.othello7)
        siirto2 = self.othello_ai.valitse_siirto(10, self.othello8)
        self.assertEqual([siirto1, siirto2], [(0, 7), (1, 5)])

    def test_valitaan_hitain_tappio(self):
        siirto = self.othello_ai.valitse_siirto(10, self.othello9)
        self.assertEqual(siirto, (7, 3))

    def test_valitaan_tasapeli_ennen_tappiota(self):
        siirto1 = self.othello_ai.valitse_siirto(6, self.othello10)
        siirto2 = self.othello_ai.valitse_siirto(6, self.othello12)
        self.assertEqual([siirto1, siirto2], [(0, 4), (0, 4)])

    def test_valitaan_voitto_eika_tasapeli(self):
        siirto = self.othello_ai.valitse_siirto(10, self.othello11)
        self.assertEqual(siirto, (7, 3))

    def test_heuristinen_arvio_laskee_oikein(self):
        arvio = self.othello_ai.arvioi_pelilauta(self.othello1)
        self.assertEqual(arvio, -234)
