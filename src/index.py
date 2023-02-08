from ui.readerwriter import IO
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.key import Avain


def main():
    io = IO()
    yksityinen_avain = Avain()
    julkinen_avain = Avain()
    avaimet = yksityinen_avain, julkinen_avain
    salaus_purku = SalausJaPurku()
    satunnaislukugeneraattori = SatunnaislukuGeneraattori()
    alkulukugeneraattori = AlkulukuGeneraattori(satunnaislukugeneraattori)
    avaingeneraattori = AvainGeneraattori(alkulukugeneraattori)
    sovellus = UI(io, avaimet, avaingeneraattori, salaus_purku)
    sovellus.suorita()

if __name__ == "__main__":
    main()
