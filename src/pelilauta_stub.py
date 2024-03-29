class PelilautaStub:
    """Luokka, jossa on erilaisia pelilautoja testaamista varten."""
    def hae_pelilauta1(self):
        pelilauta = [
                [1, 0, 1, 0, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 2, 0, 2, 1, 0, 0, 0],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [1, 0, 2, 0, 1, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta2(self):
        pelilauta = [
                [2, 0, 2, 0, 2, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0],
                [2, 1, 0, 1, 2, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0],
                [2, 0, 1, 0, 2, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta3(self):
        pelilauta = [
                [0, 2, 2, 1, 2, 2, 2, 0],
                [0, 0, 0, 2, 0, 0, 0, 0],
                [2, 0, 2, 0, 0, 0, 2, 0],
                [2, 0, 0, 2, 0, 2, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 2, 0, 2, 0, 0],
                [0, 0, 2, 0, 0, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta4(self):
        pelilauta = [
                [0, 1, 1, 2, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 1, 0, 0],
                [2, 0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta5(self):
        pelilauta = [
                [2, 0, 0, 2, 0, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 0],
                [0, 0, 2, 2, 2, 0, 0, 0],
                [2, 2, 2, 1, 2, 2, 2, 2],
                [0, 0, 2, 2, 2, 0, 0, 0],
                [0, 2, 0, 2, 0, 2, 0, 0],
                [2, 0, 0, 2, 0, 0, 2, 0],
                [0, 0, 0, 2, 0, 0, 0, 2]]
        return pelilauta

    def hae_pelilauta6(self):
        pelilauta = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta7(self):
        """Siirtosarjat valkoisen voittoon: h1, h2, h8 VS h8, e4, f1, h1"""
        pelilauta = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 2, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [2, 1, 1, 1, 1, 1, 1, 0]]
        return pelilauta

    def hae_pelilauta8(self):
        """Siirtosarja voittoon: f2, h8"""
        pelilauta = [
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 2, 1, 1, 0, 0, 1],
                [0, 0, 0, 2, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [2, 1, 1, 1, 1, 1, 1, 0]]
        return pelilauta

    def hae_pelilauta9(self):
        """Siirtosarjat tappioon: a1, h8 VS d8, h8, a1, c8"""
        pelilauta = [
                [0, 1, 1, 1, 1, 1, 2, 1],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 1, 2, 2, 0]]
        return pelilauta

    def hae_pelilauta10(self):
        """Siirtosarja tasapeliin: e1, h6
        Siirtosarja häviöön: e6, h6, e1, d6
        """
        pelilauta = [
                [2, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 1]]
        return pelilauta

    def hae_pelilauta11(self):
        """Siirtosarja tasapeliin: h8, a5
        Siirtosarja voittoon: d8, a5, h8
        """
        pelilauta = [
                [1, 1, 0, 0, 0, 0, 0, 2],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [2, 0, 0, 0, 0, 0, 0, 1],
                [2, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 2, 0, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta12(self):
        """Siirtosarja tasapeliin: e1, d1
        Siirtosarja tappioon: g6, a1, d6"""
        pelilauta = [
                [0, 2, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        return pelilauta

    def hae_pelilauta13(self):
        """Aloittava voittosiirto: h1"""
        pelilauta = [
                [1, 2, 1, 1, 1, 1, 2, 0],
                [1, 2, 1, 2, 1, 2, 2, 1],
                [1, 2, 1, 2, 1, 2, 1, 1],
                [1, 2, 1, 2, 1, 2, 2, 1],
                [1, 2, 1, 2, 1, 2, 1, 2],
                [1, 2, 1, 2, 1, 2, 2, 2],
                [1, 2, 1, 2, 1, 2, 1, 0],
                [1, 2, 1, 2, 1, 1, 2, 0]]
        return pelilauta
