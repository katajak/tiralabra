from math import isqrt


class AlkulukuGeneraattori:
    """Luokka, jonka tehtävänä on luoda oikean pituisia alkulukuja avaimen generointia varten.
    """
    def __init__(self, satunnaislukugeneraattori):
        self.satunnaislukugeneraattori = satunnaislukugeneraattori

    def esitarkistus(self, luku):
        """Metodi, joka alustavasti tarkistaa, onko annettu luku alkuluku.
            Toimii jakamalla annettua lukua pienillä alkuluvuilla.
            Palauttaa True jos annettu luku ei ole jaettavissa millään pienellä
            alkuluvulla välillä 2 < luku < sqrt(luku).
            https://en.wikipedia.org/wiki/Primality_test#Simple_methods
        """
        alkuluvut = self.generoi_pienet_alkuluvut(100)
        for alkuluku in alkuluvut:
            if alkuluku > isqrt(luku):
                break
            if luku%alkuluku == 0:
                return False
        return True

    def generoi_alkuluvut(self, bittimaara):
        """Metodi, joka generoi oikean pituiset alkuluvut avainten luontia varten.
            Palauttaa tuplessa kaksi erisuuruista alkulukua p ja q.
        """
        while True:
            p = self.satunnaislukugeneraattori.satunnainen_int_n_bittia(bittimaara//2)
            if p%2 == 0:
                continue
            if self.tarkista_onko_alkuluku(p):
                break
        while True:
            q = self.satunnaislukugeneraattori.satunnainen_int_n_bittia(bittimaara//2)
            if p == q or p%2 == 0:
                continue
            if self.tarkista_onko_alkuluku(q):
                break
        return p, q

    def generoi_pienet_alkuluvut(self, n):
        """Metodi, joka generoi pieniä alkulukua lukuun n asti Eratostheneen seulalla.
            Palauttaa listan alkuluvuista n asti
        """
        alkulukulista = [True for _ in range(n+1)]
        a_luku = 2
        while a_luku*a_luku <= n:
            if alkulukulista[a_luku]:
                for i in range(a_luku*a_luku, n+1, a_luku):
                    alkulukulista[i] = False
            a_luku += 1

        alkuluvut = []
        for a_luku in range(2, n+1):
            if alkulukulista[a_luku]:
                alkuluvut.append(a_luku)
        return alkuluvut

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
            a = self.satunnaislukugeneraattori.satunnainen_int_mr(n)
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
        if luku in (2, 3):
            return True
        if not self.esitarkistus(luku):
            return False
        if not self.miller_rabin(luku, 40):
            return False
        return True
