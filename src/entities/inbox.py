class Postilaatikko:
    def __init__(self, tiedostonkasittelija):
        self.postilaatikko = []
        self.tiedostonkasittelija = tiedostonkasittelija

    def hae_viesti_nimella(self, nimi):
        for viesti in self.postilaatikko:
            if nimi == viesti.tiedoston_nimi:
                return viesti
        return None

    def lisaa_viesti(self, viesti, tiedoston_nimi):
        self.tiedostonkasittelija.kirjoita_viesti_tiedostoon(viesti, tiedoston_nimi)
        self.postilaatikko.append(viesti)

    def lisaa_viestit_tiedostoista(self):
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
