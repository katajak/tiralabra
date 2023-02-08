from random import randint, getrandbits


class SatunnaislukuGeneraattori:
    """Luokka, joka toimii kuten randint ja getrandbits.
    Eristetty testaamisen vuoksi.
    """
    def satunnainen_int_valilla(self, a, b):
        return randint(a, b)

    def satunnainen_int_n_bittia(self, n):
        return getrandbits(n)
