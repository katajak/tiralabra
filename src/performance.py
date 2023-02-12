import time
from logic.keygen import AvainGeneraattori
from logic.primegen import AlkulukuGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from entities.keychain import Avaimenpera


def main():
    print("Kaikissa testeissä lasketaan keskiarvo 20:ltä suorituskerralta.")
    avaingeneraattori = AvainGeneraattori((AlkulukuGeneraattori(SatunnaislukuGeneraattori())), Avaimenpera())
    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(1024, "testi1024")
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"1024 bit: {sum(ajat)/len(ajat)} sekuntia")

    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(2048, "testi2048")
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"2048 bit: {sum(ajat)/len(ajat)} sekuntia")

    ajat = []
    for _ in range(20):
        alku = time.time()
        avaingeneraattori.generoi_avaimet(4096, "testi4096")
        loppu = time.time()
        ajat.append(loppu-alku)
    print(f"4096 bit: {sum(ajat)/len(ajat)} sekuntia")

if __name__ == "__main__":
    main()
