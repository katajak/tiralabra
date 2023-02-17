class Avaimenpera:
    """Luokka, joka säilyttää avaimet listassa.
    """
    def __init__(self, tiedostonkasittelija):
        self.avaimenpera = []
        self.tiedostonkasittelija = tiedostonkasittelija

    def avaimet(self):
        """Metodi, joka palauttaa listan avaimista.
        """
        return self.avaimenpera

    def avainten_maara(self):
        """Metodi, joka kertoo avainten määrän.
        """
        return len(self.avaimenpera)

    def hae_julkinen_avain_nimella(self, nimi):
        """Metodi, joka hakee avaimenperästä julkisen avaimen sen nimen perusteella.
        """
        for avain in self.avaimenpera:
            if nimi == avain.nimi and avain.tyyppi == "julkinen":
                return avain
        return None

    def hae_yksityinen_avain_nimella(self, nimi):
        """Metodi, joka hakee avaimenperästä yksityisen avaimen sen nimen perusteella.
        """
        for avain in self.avaimenpera:
            if nimi == avain.nimi and avain.tyyppi == "yksityinen":
                return avain
        return None

    def julkiset_avaimet(self):
        """Metodi, joka palauttaa listan julkisista avaimista.
        """
        avaimet = []
        for avain in self.avaimenpera:
            if avain.tyyppi == "julkinen":
                avaimet.append(avain)
        return avaimet

    def lisaa_avaimet_tiedostoista(self):
        """Metodi lisää tiedostoissa olevat avaimet avaimenperään.
        """
        avaimet = self.tiedostonkasittelija.lue_avaimet_tiedostoista()
        for avain in avaimet:
            self.avaimenpera.append(avain)

    def lisaa_avain(self, avain, tiedoston_nimi):
        """Metodi lisää avaimen avaimenperään ja kirjoittaa avaimen tiedostoon.
        """
        self.tiedostonkasittelija.kirjoita_avain_tiedostoon(avain, tiedoston_nimi)
        self.avaimenpera.append(avain)

    def yksityiset_avaimet(self):
        """Metodi, joka palauttaa listan yksityisistä avaimista.
        """
        avaimet = []
        for avain in self.avaimenpera:
            if avain.tyyppi == "yksityinen":
                avaimet.append(avain)
        return avaimet
