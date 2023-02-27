import os


class UI:
    """Komentorivikäyttöliittymä.
    """
    def __init__(self, io, avaimenpera, postilaatikko, avaingeneraattori, salaus_purku):
        self.io = io
        self.avaimenpera = avaimenpera
        self.postilaatikko = postilaatikko
        self.avaingeneraattori = avaingeneraattori
        self.salaus_purku = salaus_purku
        self.run = True
        self.tyhjenna = False
        self.viesti_kayttajalle = []

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
        self.avaimenpera.lisaa_avaimet_tiedostoista()
        self.postilaatikko.lisaa_viestit_tiedostoista()
        self.io.kirjoita("Tervetuloa ohjelmaan! Mitä haluat tehdä?\n")
        while self.run:
            if self.tyhjenna:
                self.tyhjenna_naytto()
                self.tyhjenna = False
            while self.viesti_kayttajalle:
                if len(self.viesti_kayttajalle) == 1:
                    self.io.kirjoita(f"{self.viesti_kayttajalle.pop(0)}\n")
                else:
                    self.io.kirjoita(self.viesti_kayttajalle.pop(0))

            syote = self.io.lue_lista("Valinta", ["Generoi avaimet", "Salaa viesti", "Pura salattu viesti",
                                                  "Listaa avaimet", "Listaa viestit", "Lopeta ohjelma"])

            self.tyhjenna_naytto()
            if syote == "Generoi avaimet":
                tyyppi = self.io.lue_lista("Avaimen tyyppi", ["RSA 1024-bittiä", "RSA 2048-bittiä", "RSA 4096-bittiä"])

                nimi = self.io.lue("Anna nimi avaimille: ")
                if len(nimi) == 0:
                    self.tyhjenna = True
                    self.viesti_kayttajalle.append("Toiminto peruutettu.")
                    continue
                tiedoston_nimi_yksityinen = nimi + ".priv"
                tiedoston_nimi_julkinen = nimi + ".pub"

                self.tyhjenna_naytto()
                self.io.kirjoita("Generoidaan avaimia...")
                if tyyppi == "RSA 1024-bittiä":
                    koko = 1024
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                elif tyyppi == "RSA 2048-bittiä":
                    koko = 2048
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                elif tyyppi == "RSA 4096-bittiä":
                    koko = 4096
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                self.tyhjenna = True
                self.viesti_kayttajalle.append("Avaimet generoitu onnistuneesti.")

            elif syote == "Salaa viesti":
                if self.avaimenpera.avainten_maara() > 0:
                    julkinen_avain = self.io.lue_lista("Käytettävä avain", self.avaimenpera.julkiset_avaimet())

                    tiedosto = self.io.lue("Anna viestin tiedoston nimi: ")
                    tiedosto = tiedosto + ".msg"
                    if len(tiedosto)-4 == 0:
                        self.tyhjenna = True
                        self.viesti_kayttajalle.append("Toiminto peruutettu.")
                        continue

                    syote = self.io.lue("\nKirjoita viesti:\n\n")
                    if len(syote) == 0:
                        self.tyhjenna = True
                        self.viesti_kayttajalle.append("Toiminto peruutettu.")
                        continue

                    self.salaus_purku.salaa_viesti(julkinen_avain, syote, tiedosto)
                    self.tyhjenna = True
                    self.viesti_kayttajalle.append("Viesti salattu onnistuneesti.")
                else:
                    self.viesti_kayttajalle.append("Julkisia avaimia ei löytynyt.")

            elif syote == "Pura salattu viesti":
                if self.avaimenpera.avainten_maara() > 0:
                    if self.postilaatikko.viestien_maara() == 0:
                        self.tyhjenna = True
                        self.viesti_kayttajalle.append("Viestejä ei löytynyt.")
                        continue

                    yksityinen_avain = self.io.lue_lista("Käytettävä avain", self.avaimenpera.yksityiset_avaimet())

                    self.tyhjenna_naytto()
                    salattu_viesti = self.io.lue_lista("Purettava viesti", self.postilaatikko.viestit())
                    purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)

                    self.tyhjenna_naytto()
                    self.io.kirjoita(purettu_viesti)
                    self.io.lue("\nPaina Enter jatkaaksesi")
                    self.tyhjenna = True
                else:
                    self.viesti_kayttajalle.append("Yksityisiä avaimia ei löytynyt.")

            elif syote == "Listaa avaimet":
                if self.avaimenpera.avainten_maara() > 0:
                    for avain in self.avaimenpera.avaimet():
                        self.viesti_kayttajalle.append(avain)
                else:
                    self.viesti_kayttajalle.append("Avaimia ei löytynyt.")

            elif syote == "Listaa viestit":
                if self.postilaatikko.viestien_maara() > 0:
                    for viesti in self.postilaatikko.viestit():
                        self.viesti_kayttajalle.append(viesti)
                else:
                    self.viesti_kayttajalle.append("Viestejä ei löytynyt.")

            elif syote == "Lopeta ohjelma":
                self.run = False
