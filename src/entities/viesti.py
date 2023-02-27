class Viesti:
    def __init__(self, viesti, tiedoston_nimi):
        self.viesti = viesti
        self.tiedoston_nimi = tiedoston_nimi

    def __str__(self):
        return self.tiedoston_nimi
