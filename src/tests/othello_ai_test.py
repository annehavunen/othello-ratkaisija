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

    def test_valitaan_nopein_voitto(self):
        siirto1 = self.othello_ai.valitse_siirto(6, self.othello7)
        siirto2 = self.othello_ai.valitse_siirto(6, self.othello8)
        self.assertEqual((siirto1, siirto2), ("h1", "f2"))

    def test_valitaan_hitain_tappio(self):
        siirto = self.othello_ai.valitse_siirto(6, self.othello9)
        self.assertEqual(siirto, "d8")

    def test_valitaan_tasapeli_ennen_tappiota(self):
        siirto = self.othello_ai.valitse_siirto(6, self.othello10)
        self.assertEqual(siirto, "e1")

    def test_valitaan_voitto_eika_tasapeli(self):
        siirto = self.othello_ai.valitse_siirto(6, self.othello11)
        self.assertEqual(siirto, "d8")

    def test_heuristinen_arvio_laskee_oikein(self):
        arvio = self.othello_ai.arvioi_pelilauta(self.othello1)
        self.assertEqual(arvio, -234)
