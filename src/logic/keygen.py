class AvainGeneraattori:
    def __init__(self, alkulukugeneraattori):
        self.alkulukugeneraattori = alkulukugeneraattori

    def generoi_avaimet(self, bittimaara):
        p, q = self.alkulukugeneraattori.generoi_alkuluvut(bittimaara)
        print(f"p: {p}")
        print(f"pituus (binääri): {len(bin(p))}")
        print("")
        print(f"q: {q}")
        print(f"pituus (binääri): {len(bin(q))}")
