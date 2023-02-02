from random import randint, getrandbits


class AlkulukuGeneraattori:
    """Luokka, jonka tehtävänä on luoda oikean pituisia alkulukuja avaimen generointia varten.
    """
    def __init__(self):
        pass

    def miller_rabin(self, n, k):
        """Metodi, johon toteutettu Miller-Rabin testi
            Palauttaa True jos annettu luku n on suurella todennäköisyydellä alkuluku.
            Testi suoritetaan k kertaa.
            Toimii jos n on suurempi kuin 3.
            https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
        """
        s = n-1
        t = 0
        while s%2 == 0:
            s = s//2
            t += 1

        for _ in range(k):
            a = randint(2, n-2)
            x = pow(a, s, n)
            if x in (1, n-1):
                continue
            for _ in range(t-1):
                x = pow(x, 2, n)
                if x == n-1:
                    break
            else:
                return False
        return True

    def tarkista_onko_alkuluku(self, luku):
        """Metodi, joka tarkistaa, onko annettu luku alkuluku.
            Ensin katsotaan esitarkastuksella, sitten Miller-Rabinilla.
            Palauttaa True jos annettu luku n on alkuluku.
        """
        if not self.esitarkistus(luku):
            return False
        if not self.miller_rabin(luku, 40):
            return False
        return True

    def generoi_alkuluvut(self, bittimaara):
        """Metodi, generoi oikean pituiset alkuluvut avainten luontia varten.
            Palauttaa tuplessa kaksi erisuuruista alkulukua p ja q.
        """
        while True:
            p = getrandbits(bittimaara//2)
            if len(bin(p)) != bittimaara//2:
                continue
            if self.tarkista_onko_alkuluku(p):
                break
        while True:
            q = getrandbits(bittimaara//2)
            if p == q or len(bin(q)) != bittimaara//2:
                continue
            if self.tarkista_onko_alkuluku(q):
                break
        return p, q

    def esitarkistus(self, luku):
        """Metodi, joka alustavasti tarkistaa, onko annettu luku alkuluku.
            Toimii jakamalla annettua lukua pienillä alkuluvuilla.
            Palauttaa True jos annettu luku ei ole jaettavissa millään pienellä
            alkuluvulla (paitsi itsellään).
        """
        alkuluvut = self.generoi_pienet_alkuluvut(100)
        for alkuluku in alkuluvut:
            if luku == alkuluku:
                continue
            if luku%alkuluku == 0:
                return False
        return True

    def generoi_pienet_alkuluvut(self, n):
        """Metodi, joka generoi pieniä alkulukua lukuun n asti.
            Palauttaa listan alkuluvuista n asti
        """
        alkuluvut = []
        for luku in range(n+1):
            if luku > 1:
                for i in range(2, luku):
                    if luku%i == 0:
                        break
                else:
                    alkuluvut.append(luku)
        return alkuluvut
