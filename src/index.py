from ui.io import IO
from ui.sovellus import UI
from logic.alkulukugen import AlkulukuGeneraattori
from logic.avaingen import AvainGeneraattori
from logic.satunnaisgen import SatunnaislukuGeneraattori
from logic.salauspurku import SalausJaPurku
from entities.avaimenpera import Avaimenpera
from entities.postilaatikko import Postilaatikko
from repositories.tiedostonkasittelija import TiedostonKasittelija


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
