from entities.key import Avain


class AvainGeneraattori:
    """Luokka, jonka tehtävänä on luoda RSA-avaimet
    """
    def __init__(self, alkulukugeneraattori, avaimenpera):
        self.alkulukugeneraattori = alkulukugeneraattori
        self.avaimenpera = avaimenpera

    def generoi_avaimet(self, bittimaara, nimi):
        p, q = self.alkulukugeneraattori.generoi_alkuluvut(bittimaara)
        n = p*q
        l = self.carmichaelin_funktio(p, q)
        e = 65537
        d = pow(e, -1, l)
        yksityinen_avain = Avain(nimi, bittimaara, n, d)
        julkinen_avain = Avain(nimi, bittimaara, n, e)
        self.avaimenpera.lisaa_avaimet(yksityinen_avain, julkinen_avain)

    def syt(self, p, q):
        """https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
        """
        while q:
            t = q
            q = p%q
            p = t
        return p

    def carmichaelin_funktio(self, p, q):
        return abs((p-1)*(q-1)) // self.syt(p-1, q-1)
