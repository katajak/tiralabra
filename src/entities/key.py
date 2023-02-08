class Avain:
    def __init__(self, nimi, tyyppi, modulus, eksponentti):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.modulus = modulus
        self.eksponentti = eksponentti

    def __str__(self):
        return f"{self.nimi}, {self.tyyppi} bittiä"
