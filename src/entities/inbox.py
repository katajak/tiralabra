class Postilaatikko:
    def __init__(self, tiedostonkasittelija):
        self.postilaatikko = []
        self.tiedostonkasittelija = tiedostonkasittelija

    def lisaa_viesti(self, viesti, tiedoston_nimi):
        self.tiedostonkasittelija.kirjoita_viesti_tiedostoon(viesti, tiedoston_nimi)
        self.postilaatikko.append(viesti)

    def lisaa_viestit_tiedostoista(self):
        viestit = self.tiedostonkasittelija.lue_viestit_tiedostoista()
        for viesti in viestit:
            self.postilaatikko.append(viesti)

    def hae_viesti_nimella(self, nimi):
        for viesti in self.postilaatikko:
            return viesti
        return None
