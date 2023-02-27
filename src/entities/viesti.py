class Viesti:
    def __init__(self, viesti, tiedoston_nimi, muokkausaika):
        self.viesti = viesti
        self.tiedoston_nimi = tiedoston_nimi
        self.muokkausaika = muokkausaika

    def __str__(self):
        return f"{self.tiedoston_nimi}, kirjoitettu {self.muokkausaika}"
