import os
import time
from tempfile import NamedTemporaryFile
from logic.keygen import AvainGeneraattori
from logic.primegen import AlkulukuGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from entities.keychain import Avaimenpera
from repositories.datahandler import TiedostonKasittelija


def main():
    print("Kaikissa testeissä lasketaan keskiarvo 20:ltä suorituskerralta.")
    avaingeneraattori = AvainGeneraattori((AlkulukuGeneraattori(SatunnaislukuGeneraattori())),
                                           Avaimenpera(TiedostonKasittelija()))
    testi1024_yks = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    testi1024_jul = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(1024, "testi1024", testi1024_yks.name, testi1024_jul.name)
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"1024 bit: {sum(ajat)/len(ajat)} sekuntia")
    testi1024_yks.close()
    testi1024_jul.close()
    os.unlink(testi1024_yks.name)
    os.unlink(testi1024_jul.name)

    testi2048_yks = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    testi2048_jul = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(2048, "testi2048", testi2048_yks.name, testi2048_jul.name)
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"2048 bit: {sum(ajat)/len(ajat)} sekuntia")
    testi2048_yks.close()
    testi2048_jul.close()
    os.unlink(testi2048_yks.name)
    os.unlink(testi2048_jul.name)

    testi4096_yks = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    testi4096_jul = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(4096, "testi4096", testi4096_yks.name, testi4096_jul.name)
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"4096 bit: {sum(ajat)/len(ajat)} sekuntia")
    testi4096_yks.close()
    testi4096_jul.close()
    os.unlink(testi4096_yks.name)
    os.unlink(testi4096_jul.name)

if __name__ == "__main__":
    main()
