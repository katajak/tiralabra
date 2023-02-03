import os

class UI:
    """Komentorivikäyttöliittymä.
        io injektoidaan jotta käyttöliittymän testaaminen olisi mahdollista.
    """
    def __init__(self, io, avaingeneraattori):
        self.io = io
        self.avaingeneraattori = avaingeneraattori
        self.run = True

    def tyhjenna_naytto(self):
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    def suorita(self):
        self.tyhjenna_naytto()
        while self.run:
            self.io.kirjoita("Tervetuloa ohjelmaan! Mitä haluat tehdä?")
            self.io.kirjoita("\n1: Generoi avaimet")
            self.io.kirjoita("2: Salaa viesti")
            self.io.kirjoita("3: Pura salattu viesti")
            self.io.kirjoita("q: Lopeta ohjelma")
            syote = self.io.lue("\nValinta: ")

            self.tyhjenna_naytto()
            if syote == "1":
                self.io.kirjoita("Valitse avaimen tyyppi")
                self.io.kirjoita("\n1: RSA 1024-bittiä")
                self.io.kirjoita("2: RSA 2048-bittiä")
                syote = self.io.lue("\nValinta: ")
                if syote == "1":
                    syote = 1024
                    self.avaingeneraattori.generoi_avaimet(syote)
                if syote == "2":
                    syote = 2048
                    self.avaingeneraattori.generoi_avaimet(syote)
                self.tyhjenna_naytto()

            elif syote == "2":
                pass

            elif syote == "3":
                pass

            elif syote == "q":
                self.run = False
