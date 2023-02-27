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

            syote = self.io.lue_lista("valinta", "Valinta", ["Generoi avaimet", "Salaa viesti", "Pura salattu viesti",
                                                             "Listaa avaimet", "Listaa viestit", "Lopeta ohjelma"])

            self.tyhjenna_naytto()
            if syote["valinta"] == "Generoi avaimet":
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
                tiedoston_nimi_yksityinen = nimi + ".priv"
                tiedoston_nimi_julkinen = nimi + ".pub"

                self.tyhjenna_naytto()
                self.io.kirjoita("Generoidaan avaimia...")
                if syote == "1":
                    koko = 1024
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                elif syote == "2":
                    koko = 2048
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                elif syote == "3":
                    koko = 4096
                    self.avaingeneraattori.generoi_avaimet(koko, nimi, tiedoston_nimi_yksityinen,
                                                           tiedoston_nimi_julkinen)
                self.tyhjenna = True
                self.viesti_kayttajalle.append("Avaimet generoitu onnistuneesti.")

            elif syote["valinta"] == "Salaa viesti":
                if self.avaimenpera.avainten_maara() > 0:
                    self.io.kirjoita("Julkiset avaimet:\n")
                    for avaimet in self.avaimenpera.julkiset_avaimet():
                        self.io.kirjoita(avaimet)
                    nimi = self.io.lue("\nAnna käytettävän avaimen nimi: ")
                    if len(nimi) == 0:
                        self.tyhjenna = True
                        continue
                    julkinen_avain = self.avaimenpera.hae_julkinen_avain_nimella(nimi)
                    tiedosto = self.io.lue("\nAnna viestin tiedoston nimi: ")
                    tiedosto = tiedosto + ".msg"
                    if len(tiedosto) == 0:
                        self.tyhjenna = True
                        continue
                    syote = self.io.lue("\nKirjoita viesti:\n\n")
                    if len(syote) == 0:
                        self.tyhjenna = True
                        continue
                    self.salaus_purku.salaa_viesti(julkinen_avain, syote, tiedosto)
                    self.tyhjenna = True
                    self.viesti_kayttajalle.append("Viesti salattu onnistuneesti.")
                else:
                    self.viesti_kayttajalle.append("Julkisia avaimia ei löytynyt.")

            elif syote["valinta"] == "Pura salattu viesti":
                if self.avaimenpera.avainten_maara() > 0:
                    self.io.kirjoita("Yksityiset avaimet:\n")
                    for avaimet in self.avaimenpera.yksityiset_avaimet():
                        self.io.kirjoita(avaimet)
                    nimi = self.io.lue("\nAnna käytettävän avaimen nimi: ")
                    if len(nimi) == 0:
                        self.tyhjenna = True
                        continue
                    yksityinen_avain = self.avaimenpera.hae_yksityinen_avain_nimella(nimi)
                    self.tyhjenna_naytto()
                    self.io.kirjoita("Tiedostot:\n")
                    for viesti in self.postilaatikko.viestit():
                        self.io.kirjoita(viesti.tiedoston_nimi[:-4])
                    tiedosto = self.io.lue("\nAnna viestin tiedoston nimi: ")
                    tiedosto = tiedosto + ".msg"
                    salattu_viesti = self.postilaatikko.hae_viesti_nimella(tiedosto)
                    purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)

                    self.tyhjenna_naytto()
                    self.io.kirjoita(purettu_viesti)
                    self.io.lue("\nPaina Enter jatkaaksesi")
                    self.tyhjenna = True
                else:
                    self.viesti_kayttajalle.append("Yksityisiä avaimia ei löytynyt.")

            elif syote["valinta"] == "Listaa avaimet":
                if self.avaimenpera.avainten_maara() > 0:
                    for avaimet in self.avaimenpera.avaimet():
                        self.viesti_kayttajalle.append(avaimet)
                else:
                    self.viesti_kayttajalle.append("Avaimia ei löytynyt.")

            elif syote["valinta"] == "Listaa viestit":
                if self.postilaatikko.viestien_maara() > 0:
                    for viesti in self.postilaatikko.viestit():
                        self.viesti_kayttajalle.append(viesti.tiedoston_nimi)
                else:
                    self.viesti_kayttajalle.append("Viestejä ei löytynyt.")

            elif syote["valinta"] == "Lopeta ohjelma":
                self.run = False
