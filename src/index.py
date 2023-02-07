from ui.readerwriter import IO
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori


def main():
    io = IO()
    satunnaislukugeneraattori = SatunnaislukuGeneraattori()
    alkulukugeneraattori = AlkulukuGeneraattori(satunnaislukugeneraattori)
    avaingeneraattori = AvainGeneraattori(alkulukugeneraattori)
    sovellus = UI(io, avaingeneraattori)
    sovellus.suorita()

if __name__ == "__main__":
    main()
