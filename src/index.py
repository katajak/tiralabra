from ui.readerwriter import IO
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori

def main():
    io = IO()
    alkulukugeneraattori = AlkulukuGeneraattori()
    avaingeneraattori = AvainGeneraattori(alkulukugeneraattori)
    sovellus = UI(io, avaingeneraattori)
    sovellus.suorita()

if __name__ == "__main__":
    main()
