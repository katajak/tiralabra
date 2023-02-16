from entities.key import Avain


class AvainGeneraattori:
    """Luokka, jonka tehtävänä on luoda RSA-avaimet.
    """
    def __init__(self, alkulukugeneraattori, avaimenpera):
        self.alkulukugeneraattori = alkulukugeneraattori
        self.avaimenpera = avaimenpera

    def generoi_avaimet(self, bittimaara, nimi, tiedoston_nimi):
        """Metodi, joka luo avainoliot, ja lisää avaimet avaimenperä-olioon
        Ei varsinaisesti palauta mitään.
        """
        p, q = self.alkulukugeneraattori.generoi_alkuluvut(bittimaara)
        n = p*q
        l = self.carmichaelin_funktio(p, q)
        e = 65537
        d = pow(e, -1, l)
        yksityinen_avain = Avain(nimi, "yksityinen", bittimaara, n, d)
        julkinen_avain = Avain(nimi, "julkinen", bittimaara, n, e)
        self.avaimenpera.lisaa_avain(yksityinen_avain, tiedoston_nimi + ".priv")
        self.avaimenpera.lisaa_avain(julkinen_avain, tiedoston_nimi + ".pub")

    def syt(self, p, q):
        """Eukleideen algoritmi, joka ratkaisee p ja q suurimman yhteisen tekijän.
        https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
        """
        while q:
            t = q
            q = p%q
            p = t
        return p

    def carmichaelin_funktio(self, p, q):
        """Carmichaelin funktio joka laskee lambdan arvon kun sille annetaan p ja q.
        """
        return abs((p-1)*(q-1)) // self.syt(p-1, q-1)
