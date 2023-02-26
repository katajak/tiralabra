from secrets import randbelow, randbits


class SatunnaislukuGeneraattori:
    """Luokka, joka toimii kuten randbelow ja randbits.
    Eristetty testaamisen vuoksi.
    """
    def satunnainen_int_mr(self, n):
        """Metodi, joka valitsee satunnaisen luvun oikealta väliltä
        Miller-Rabin testiä varten kun sille annetaan n.
        """
        return 2+randbelow(n-3)

    def satunnainen_int_n_bittia(self, n):
        return randbits(n)
