import os


class UI:
    """Komentorivikäyttöliittymä.
    """
    def __init__(self, io, avaimenpera, avaingeneraattori, salaus_purku):
        self.io = io
        self.avaimenpera = avaimenpera
        self.avaingeneraattori = avaingeneraattori
        self.salaus_purku = salaus_purku
        self.run = True
        self.tyhjenna = False

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
            if self.tyhjenna:
                self.tyhjenna_naytto()
                self.tyhjenna = False
            self.io.kirjoita("\n1: Generoi avaimet")
            self.io.kirjoita("2: Salaa viesti")
            self.io.kirjoita("3: Pura salattu viesti")
            self.io.kirjoita("4: Listaa avaimet")
            self.io.kirjoita("q: Lopeta ohjelma")
            syote = self.io.lue("\nValinta: ")

            self.tyhjenna_naytto()
            if syote == "1":
                self.io.kirjoita("Valitse avaimen tyyppi")
                self.io.kirjoita("\n1: RSA 1024-bittiä")
                self.io.kirjoita("2: RSA 2048-bittiä")
                self.io.kirjoita("3: RSA 4096-bittiä")
                syote = self.io.lue("\nValinta: ")
                if len(syote) == 0:
                    self.tyhjenna = True
                    continue
                nimi = self.io.lue("\nAnna nimi avaimille: ")
                if len(nimi) == 0:
                    self.tyhjenna = True
                    continue
                self.tyhjenna_naytto()
                self.io.kirjoita("Generoidaan avaimia...")
                if syote == "1":
                    syote = 1024
                    self.avaingeneraattori.generoi_avaimet(syote, nimi)
                elif syote == "2":
                    syote = 2048
                    self.avaingeneraattori.generoi_avaimet(syote, nimi)
                elif syote == "3":
                    syote = 4096
                    self.avaingeneraattori.generoi_avaimet(syote, nimi)
                self.tyhjenna_naytto()
                self.io.kirjoita("Avaimet generoitu onnistuneesti.")

            elif syote == "2":
                if self.avaimenpera.avainten_maara() > 0:
                    for avaimet in self.avaimenpera.avaimet():
                        self.io.kirjoita(avaimet[1])
                    nimi = self.io.lue("\nAnna käytettävän avaimen nimi: ")
                    if len(nimi) == 0:
                        self.tyhjenna = True
                        continue
                    julkinen_avain = self.avaimenpera.hae_avaimet_nimella(nimi)[1]
                    syote = self.io.lue("\nKirjoita viesti:\n\n")
                    if len(syote) == 0:
                        self.tyhjenna = True
                        continue
                    pituus = len(syote.encode())
                    salattu_viesti = self.salaus_purku.salaa_viesti(julkinen_avain, syote)
                    self.io.kirjoita("\nViesti salattu onnistuneesti.")
                else:
                    self.io.kirjoita("Et ole vielä generoinut avaimia!")

            elif syote == "3":
                if self.avaimenpera.avainten_maara() > 0:
                    for avaimet in self.avaimenpera.avaimet():
                        self.io.kirjoita(avaimet[1])
                    nimi = self.io.lue("\nAnna käytettävän avaimen nimi: ")
                    if len(nimi) == 0:
                        self.tyhjenna = True
                        continue
                    yksityinen_avain = self.avaimenpera.hae_avaimet_nimella(nimi)[0]
                    purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain,
                                                                salattu_viesti, pituus)
                    self.io.kirjoita(purettu_viesti)
                else:
                    self.io.kirjoita("Et ole vielä generoinut avaimia!")

            elif syote == "4":
                if self.avaimenpera.avainten_maara() > 0:
                    for avaimet in self.avaimenpera.avaimet():
                        self.io.kirjoita(avaimet[0])
                else:
                    self.io.kirjoita("Et ole vielä generoinut avaimia!")

            elif syote == "q":
                self.run = False
