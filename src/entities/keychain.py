class Avaimenpera:
    """Luokka, joka säilyttää avaimet listassa.
    """
    def __init__(self):
        self.avaimenpera = []

    def lisaa_avain(self, avain):
        """Metodi lisää avaimen avaimenperään.
        """
        self.avaimenpera.append(avain)

    def avaimet(self):
        """Metodi, joka palauttaa listan avaimista.
        """
        return self.avaimenpera

    def yksityiset_avaimet(self):
        """Metodi, joka palauttaa listan yksityisistä avaimista.
        """
        avaimet = []
        for avain in self.avaimenpera:
            if avain.tyyppi == "yksityinen":
                avaimet.append(avain)
        return avaimet

    def julkiset_avaimet(self):
        """Metodi, joka palauttaa listan julkisista avaimista.
        """
        avaimet = []
        for avain in self.avaimenpera:
            if avain.tyyppi == "julkinen":
                avaimet.append(avain)
        return avaimet

    def hae_yksityinen_avain_nimella(self, nimi):
        """Metodi, joka hakee avaimenperästä yksityisen avaimen sen nimen perusteella.
        """
        for avain in self.avaimenpera:
            if nimi == avain.nimi and avain.tyyppi == "yksityinen":
                return avain
        return None

    def hae_julkinen_avain_nimella(self, nimi):
        """Metodi, joka hakee avaimenperästä julkisen avaimen sen nimen perusteella.
        """
        for avain in self.avaimenpera:
            if nimi == avain.nimi and avain.tyyppi == "julkinen":
                return avain
        return None

    def avainten_maara(self):
        """Metodi, joka kertoo avainten määrän.
        """
        return len(self.avaimenpera)
