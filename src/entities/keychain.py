class Avaimenpera:
    def __init__(self):
        self.avaimenpera = []

    def lisaa_avaimet(self, yksityinen_avain, julkinen_avain):
        self.avaimenpera.append((yksityinen_avain, julkinen_avain))

    def avaimet(self):
        return self.avaimenpera

    def hae_avaimet_nimella(self, nimi):
        for avaimet in self.avaimenpera:
            if nimi in (avaimet[0].nimi, avaimet[1].nimi):
                return avaimet
            return None

    def avainten_maara(self):
        return len(self.avaimenpera)
