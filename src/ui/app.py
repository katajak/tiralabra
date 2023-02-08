import os


class UI:
    """Komentorivikäyttöliittymä.
        io injektoidaan jotta käyttöliittymän testaaminen olisi mahdollista.
    """
    def __init__(self, io, avaimet, avaingeneraattori, salaus_purku):
        self.io = io
        self.yksityinen_avain = avaimet[0]
        self.julkinen_avain = avaimet[1]
        self.avaingeneraattori = avaingeneraattori
        self.salaus_purku = salaus_purku
        self.run = True

    def tyhjenna_naytto(self):
        """Metodi, joka tyhjentää näytön oikealla komennolla
            käyttöjärjestelmästä riippuen.
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def suorita(self):
        """Metodi, jolla käynnistetään komentorivikäyttöliittymä.
        """
        self.tyhjenna_naytto()
        self.io.kirjoita("Tervetuloa ohjelmaan! Mitä haluat tehdä?")
        while self.run:
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
                self.io.kirjoita("3: RSA 4096-bittiä")
                syote = self.io.lue("\nValinta: ")
                self.tyhjenna_naytto()
                self.io.kirjoita("Generoidaan avaimia...")
                if syote == "1":
                    syote = 1024
                    self.avaingeneraattori.generoi_avaimet(syote, self.yksityinen_avain,
                                                           self.julkinen_avain)
                elif syote == "2":
                    syote = 2048
                    self.avaingeneraattori.generoi_avaimet(syote, self.yksityinen_avain,
                                                           self.julkinen_avain)
                elif syote == "3":
                    syote = 4096
                    self.avaingeneraattori.generoi_avaimet(syote, self.yksityinen_avain,
                                                           self.julkinen_avain)
                self.tyhjenna_naytto()
                self.io.kirjoita("Avaimet generoitu onnistuneesti.")

            elif syote == "2":
                syote = self.io.lue("Kirjoita viesti: ")
                pituus = len(syote.encode())
                salattu_viesti = self.salaus_purku.salaa_viesti(self.julkinen_avain, syote)
                self.io.kirjoita(f"\nSalattu viesti:\n{salattu_viesti}")
                self.io.kirjoita("\nViesti salattu onnistuneesti.")

            elif syote == "3":
                purettu_viesti = self.salaus_purku.pura_salaus(self.yksityinen_avain,
                                                               salattu_viesti, pituus)
                self.io.kirjoita(f"Purettu viesti:\n{purettu_viesti}")

            elif syote == "q":
                self.run = False
