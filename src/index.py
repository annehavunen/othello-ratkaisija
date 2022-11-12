from ui import UI
from pelilauta import Pelilauta


def main():
    pelilauta = Pelilauta().hae_pelilauta()
    peli = UI(pelilauta)
    peli.kaynnista()

if __name__ == "__main__":
    main()