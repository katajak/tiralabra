from random import randint


class MillerRabin:
    """Luokka, johon toteutettu Miller-Rabin testi.
        Palauttaa True jos annettu luku n on suurella todennäköisyydellä alkuluku.
        Testi suoritetaan k kertaa.
        Toimii jos n on suurempi kuin 3.
        https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    def __init__(self):
        pass

    def testaa(self, n, k):
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
            for _ in range(0, t-1):
                x = pow(x, 2, n)
                if x == n-1:
                    break
            else:
                return False
        return True
