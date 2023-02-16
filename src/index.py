from ui.readerwriter import IO
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.keychain import Avaimenpera
from entities.inbox import Postilaatikko
from repositories.datahandler import TiedostonKasittelija


def main():
    io = IO()
    tiedostonkasittelija = TiedostonKasittelija()
    avaimenpera = Avaimenpera(tiedostonkasittelija)
    postilaatikko = Postilaatikko(tiedostonkasittelija)
    alkulukugeneraattori = AlkulukuGeneraattori(SatunnaislukuGeneraattori())
    avaingeneraattori = AvainGeneraattori(alkulukugeneraattori, avaimenpera)
    salaus_purku = SalausJaPurku(postilaatikko)
    sovellus = UI(io, avaimenpera, postilaatikko, avaingeneraattori, salaus_purku)
    sovellus.suorita()

if __name__ == "__main__":
    main()
