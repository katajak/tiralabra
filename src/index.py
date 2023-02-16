from ui.readerwriter import IO
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.keychain import Avaimenpera
from repositories.datahandler import TiedostonKasittelija


def main():
    io = IO()
    avaimenpera = Avaimenpera(TiedostonKasittelija())
    salaus_purku = SalausJaPurku()
    satunnaislukugeneraattori = SatunnaislukuGeneraattori()
    alkulukugeneraattori = AlkulukuGeneraattori(satunnaislukugeneraattori)
    avaingeneraattori = AvainGeneraattori(alkulukugeneraattori, avaimenpera)
    sovellus = UI(io, avaimenpera, avaingeneraattori, salaus_purku)
    sovellus.suorita()

if __name__ == "__main__":
    main()
