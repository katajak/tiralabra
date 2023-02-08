class AvainGeneraattori:
    """Luokka, jonka tehtävänä on luoda RSA-avaimet
    """
    def __init__(self, alkulukugeneraattori):
        self.alkulukugeneraattori = alkulukugeneraattori

    def generoi_avaimet(self, bittimaara):
        p, q = self.alkulukugeneraattori.generoi_alkuluvut(bittimaara)
        n = p*q

    def syt(self, p, q):
        """https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
        """
        if q == 0:
            return p
        else:
            return self.syt(q, p%q)

    def carmichaelin_funktio(self, p, q):
        pass
