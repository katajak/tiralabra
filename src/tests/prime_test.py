import unittest
from logic.primegen import AlkulukuGeneraattori


# Miller-Rabinissa käytetään 40 iteraatiota
# https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes

class TestPrimes(unittest.TestCase):
    def setUp(self):
        self.primes = AlkulukuGeneraattori()

    def test_alkulukuja(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(4), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(5), True)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(8), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(7), True)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(14), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(7919), True)

    def test_suuri_yhdistetty_luku(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006), False)

    def test_suuri_alkuluku(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(658022943938739185871458866307770079897174821494059569390843141003821573902527915325288309969616387359598647884041145828085844935102559751264041474960034891373105411778512053365875908139836021077669943205482706750747047089158140435421164720274122715508250725540470763849114048823299427951761411454403), True)

    def test_generoiduilla_alkuluvuilla(self):
        alkuluvut = self.primes.generoi_alkuluvut(1024)
        self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluvut[0]))
        self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluvut[1]))

    def test_eratostheneen_seula(self):
        alkuluvut = self.primes.generoi_pienet_alkuluvut(29)
        self.assertEqual(alkuluvut[0], 2)
        self.assertEqual(alkuluvut[1], 3)
        self.assertEqual(alkuluvut[2], 5)
        self.assertEqual(alkuluvut[3], 7)
        self.assertEqual(alkuluvut[4], 11)
        self.assertEqual(alkuluvut[5], 13)
        self.assertEqual(alkuluvut[6], 17)
        self.assertEqual(alkuluvut[7], 19)
        self.assertEqual(alkuluvut[8], 23)
        self.assertEqual(alkuluvut[9], 29)

    def test_miller_rabin(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(4), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(5), True)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(8), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(7), True)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(14), False)
        self.assertEqual(self.primes.tarkista_onko_alkuluku(7919), True)
