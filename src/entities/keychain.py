class Avaimenpera:
    """Luokka, joka säilyttää avaimet listassa.
    Julkinen ja yksityinen avain ovat samassa tuplessa.
    """
    def __init__(self):
        self.avaimenpera = []

    def lisaa_avaimet(self, yksityinen_avain, julkinen_avain):
        """Metodi lisää yksityisen avaimen ja julkisen avaimen
        tuplessa avaimenperään.
        """
        self.avaimenpera.append((yksityinen_avain, julkinen_avain))

    def avaimet(self):
        """Metodi, joka palauttaa listan avaimista.
        """
        return self.avaimenpera

    def hae_avaimet_nimella(self, nimi):
        """Metodi, joka hakee avaimenperästä avaimen sen nimen perusteella.
        """
        for avaimet in self.avaimenpera:
            if nimi in (avaimet[0].nimi, avaimet[1].nimi):
                return avaimet
            return None, None

    def avainten_maara(self):
        """Metodi, joka kertoo avainten määrän.
        Huomaa kuitenkin että tässä 1 avain tarkoittaa tuplea jossa
        on julkinen JA yksityinen avain.
        """
        return len(self.avaimenpera)
