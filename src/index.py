from ui.readerwriter import IO
from ui.app import UI

def main():
    io = IO()
    sovellus = UI(io)
    sovellus.suorita()

if __name__ == "__main__":
    main()
