from ui.readerwriter import IO
from ui.app import UI
from logic.prime import AlkulukuGeneraattori

def main():
    io = IO()
    alkulukugeneraattori = AlkulukuGeneraattori()
    sovellus = UI(io, alkulukugeneraattori)
    sovellus.suorita()

if __name__ == "__main__":
    main()
