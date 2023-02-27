class Postilaatikko:
    """Luokka, joka säilyttää viestit listassa.
    """
    def __init__(self, tiedostonkasittelija):
        self.postilaatikko = []
        self.tiedostonkasittelija = tiedostonkasittelija

    def lisaa_viesti(self, viesti, tiedoston_nimi):
        """Metodi lisää viestin postilaatikkoon ja kirjoittaa viestin tiedostoon.
        """
        self.tiedostonkasittelija.kirjoita_viesti_tiedostoon(viesti, tiedoston_nimi)
        self.postilaatikko.append(viesti)

    def lisaa_viestit_tiedostoista(self):
        """Metodi lisää tiedostoissa olevat viestit postilaatikkoon.
        Suoritetaan kerran ohjelman käynnistyksen yhteydessä.
        """
        viestit = self.tiedostonkasittelija.lue_viestit_tiedostoista()
        for viesti in viestit:
            self.postilaatikko.append(viesti)

    def viestien_maara(self):
        """Metodi, joka kertoo viestien määrän.
        """
        return len(self.postilaatikko)

    def viestit(self):
        """Metodi, joka palauttaa listan viesteistä.
        """
        return self.postilaatikko
