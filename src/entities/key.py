class Avain:
    """Luokka, joka säilyttää tarvittavat tiedot avaimesta.
    self.nimi = käyttäjän antama nimi avaimelle
    self.tyyppi = yksityinen tai julkinen
    self.bittimaara = 1024, 2048 tai 4096
    """
    def __init__(self, nimi, tyyppi, bittimaara, modulus, eksponentti):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.bittimaara = bittimaara
        self.modulus = modulus
        self.eksponentti = eksponentti

    def __str__(self):
        return f"{self.nimi}, {self.tyyppi}, {self.bittimaara} bittiä"
