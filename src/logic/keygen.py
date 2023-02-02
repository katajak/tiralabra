class AvainGeneraattori:
    def __init__(self, alkulukugeneraattori):
        self.alkulukugeneraattori = alkulukugeneraattori

    def generoi_avaimet(self, bittimaara):
        p, q = self.alkulukugeneraattori.generoi_alkuluvut(bittimaara)
        n = p*q
