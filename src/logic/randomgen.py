from random import randint, getrandbits


class SatunnaislukuGeneraattori:
    def satunnainen_int_valilla(self, a, b):
        return randint(a, b)

    def satunnainen_int_n_bittia(self, n):
        return getrandbits(n)
