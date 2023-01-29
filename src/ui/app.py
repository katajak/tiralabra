class UI:
    """Komentorivikäyttöliittymä.
        io injektoidaan jotta käyttöliittymän testaaminen olisi mahdollista.
    """
    def __init__(self, io):
        self.io = io
        self.run = True

    def suorita(self):
        self.io.kirjoita("Tervetuloa ohjelmaan! Mitä haluat tehdä?")
        while self.run:
            self.io.kirjoita("\n1: Generoi avaimet")
            self.io.kirjoita("2: Salaa viesti")
            self.io.kirjoita("3: Pura salattu viesti")
            self.io.kirjoita("q: Lopeta ohjelma")

            syote = self.io.lue("\nValinta: ")

            if syote == "1":
                pass

            elif syote == "2":
                pass

            elif syote == "3":
                pass

            elif syote == "q":
                self.run = False
